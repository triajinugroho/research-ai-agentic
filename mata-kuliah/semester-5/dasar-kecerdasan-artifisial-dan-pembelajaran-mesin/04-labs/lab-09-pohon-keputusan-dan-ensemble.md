# Lab 09: Pohon Keputusan dan *Ensemble*

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 9 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-08 |
| Durasi | 100 menit |
| Prasyarat | Lab 7 selesai; UTS |
| Bobot | 1,875% (Observasi, Sub-CPMK082-1) |
| Diuji pada | scikit-learn 1.6 dan 1.9, pandas 2.2 dan 3.0 (Oktober 2026) |

---

## Tujuan Praktikum

1. Menghitung *entropy* dan *information gain* secara manual.
2. Menunjukkan *overfitting* pada pohon tanpa batas kedalaman.
3. Membandingkan pohon tunggal, *Random Forest*, dan *gradient boosting*.
4. Menafsirkan kepentingan fitur beserta keterbatasannya.

---

## Persiapan

1. Buat notebook baru bernama `NIM_Nama_Lab09.ipynb`.
2. Jalankan **sel pembuka baku** di [Lampiran D](../06-buku-ajar/lampiran.md#lampiran-d-sel-pembuka-baku) — mengimpor pustaka, mencatat versi, dan menetapkan `RANDOM_STATE = 42`. Seluruh langkah di bawah mengandaikan sel itu sudah dijalankan.
3. **Data:** data kredit pada Langkah 3–8 adalah **data sintetis (simulasi)** yang meniru pola pengajuan kredit UMKM di Indonesia; **bukan data resmi BPS/lembaga** mana pun (termasuk bank atau OJK). Data dibangkitkan pada Langkah 3: 4.000 pengajuan dengan sekitar sepertiga (≈ 35%) berlabel gagal bayar. Proporsi ini **sengaja dibuat tinggi** untuk keperluan latihan agar pohon dangkal pun dapat menemukan pola; angka ini bukan gambaran tingkat gagal bayar kredit UMKM yang sebenarnya. Aturan pembangkit label (omzet kecil, usaha yang masih muda, rasio beban utang tinggi, dan riwayat telat bayar → lebih berisiko) adalah **asumsi ilustratif**, bukan temuan empiris; `jumlah_pegawai`, `jenis_usaha`, `wilayah`, dan `kode_cabang` sengaja **tidak** ikut menentukan label.

---

## Langkah-langkah

### LANGKAH 1: Perhitungan Manual *Entropy*

```python
# =============================================
# LANGKAH 1: Entropy dan information gain — MANUAL
# =============================================
import numpy as np, pandas as pd

def entropy(p_list):
    # Entropy dari daftar proporsi; 0*log(0) diperlakukan sebagai 0
    p = np.array([x for x in p_list if x > 0])
    return float(-(p * np.log2(p)).sum())

# Kasus: 100 pengajuan kredit, 60 setuju (+), 40 tolak (-)
H_induk = entropy([60/100, 40/100])
print(f"H(induk) = -0,6·log2(0,6) - 0,4·log2(0,4) = {H_induk:.4f}")

# Percabangan pada "omzet <= 50 juta"
cabang = [
    {"nama": "omzet <= 50jt", "n": 55, "setuju": 20, "tolak": 35},
    {"nama": "omzet >  50jt", "n": 45, "setuju": 40, "tolak":  5},
]

H_anak_berbobot = 0.0
for c in cabang:
    H_c = entropy([c["setuju"]/c["n"], c["tolak"]/c["n"]])
    bobot = c["n"] / 100
    H_anak_berbobot += bobot * H_c
    print(f"  {c['nama']:16s} n={c['n']:3d}  H={H_c:.4f}  bobot={bobot:.2f}")

IG = H_induk - H_anak_berbobot
print(f"\nH(anak berbobot) = {H_anak_berbobot:.4f}")
print(f"Information Gain = {H_induk:.4f} - {H_anak_berbobot:.4f} = {IG:.4f}")

# Gini sebagai pembanding
def gini(p_list):
    p = np.array(p_list)
    return float(1 - (p ** 2).sum())

print(f"\nGini(induk) = 1 - (0,6² + 0,4²) = {gini([0.6, 0.4]):.4f}")
```

> **Bentuk soal ini muncul pada UAS.** Kerjakan dengan kalkulator lebih dahulu, baru verifikasi dengan kode.

### LANGKAH 2: Verifikasi dengan scikit-learn

```python
# =============================================
# LANGKAH 2: Verifikasi dengan DecisionTreeClassifier
# =============================================
from sklearn.tree import DecisionTreeClassifier, export_text

# Rekonstruksi data yang sesuai dengan kasus manual
X_manual = pd.DataFrame({"omzet": [30]*55 + [80]*45})
y_manual = pd.Series([1]*20 + [0]*35 + [1]*40 + [0]*5)

pohon = DecisionTreeClassifier(criterion="entropy", max_depth=1,
                               random_state=RANDOM_STATE).fit(X_manual, y_manual)

# Catatan: sklearn meletakkan ambang di titik tengah dua nilai yang berdekatan
# (30 dan 80 -> 55); pemisahannya sama dengan "omzet <= 50 juta" pada kasus manual.
print(export_text(pohon, feature_names=["omzet"]))
print("\nEntropy akar menurut sklearn:", round(pohon.tree_.impurity[0], 4))
print("Entropy akar hitungan manual  :", round(H_induk, 4))

# Information gain versi sklearn: entropy akar - rerata berbobot entropy kedua anak
t_manual = pohon.tree_
kiri, kanan = t_manual.children_left[0], t_manual.children_right[0]
IG_sklearn = t_manual.impurity[0] - (
    t_manual.n_node_samples[kiri] * t_manual.impurity[kiri]
    + t_manual.n_node_samples[kanan] * t_manual.impurity[kanan]
) / t_manual.n_node_samples[0]
print("\nInformation gain menurut sklearn:", round(IG_sklearn, 4))
print("Information gain hitungan manual  :", round(IG, 4))
```

**Pemeriksaan otomatis.** Sel berikut harus lulus tanpa `AssertionError`; bila gagal, pesannya menunjukkan apa yang perlu diperiksa.

```python
# =============================================
# Pemeriksaan otomatis — Langkah 1 dan 2
# =============================================
assert abs(t_manual.impurity[0] - H_induk) < 1e-6, (
    "Entropy akar menurut sklearn berbeda dari hitungan manual — "
    "periksa fungsi entropy() dan data rekonstruksi X_manual/y_manual")
assert abs(IG_sklearn - IG) < 1e-6, (
    "Information gain sklearn berbeda dari hitungan manual — "
    "periksa bobot n_cabang/n pada rerata berbobot entropy anak")
print("Pemeriksaan otomatis lulus.")
```

### LANGKAH 3: Data Sintetis Kelayakan Kredit UMKM

> **Data sintetis (simulasi)** yang meniru pola pengajuan kredit UMKM di Indonesia; bukan data resmi BPS/lembaga. Peluang gagal bayar dibangkitkan dari omzet, lama usaha, rasio beban utang, dan riwayat telat bayar, ditambah keacakan; sekitar sepertiga pengajuan berakhir berlabel gagal bayar.

```python
# =============================================
# LANGKAH 3: Data SINTETIS kelayakan kredit UMKM (≈ 35% gagal bayar)
# (simulasi, bukan data resmi BPS/lembaga)
# =============================================
rng = np.random.default_rng(RANDOM_STATE)
n = 4000

df = pd.DataFrame({
    "omzet_bulanan_jt":  rng.gamma(2.0, 20, size=n).round(1),
    "lama_usaha_thn":    rng.gamma(2.0, 2.5, size=n).round(1),
    "jumlah_pegawai":    rng.poisson(4, size=n) + 1,
    "rasio_beban_utang": rng.beta(2, 5, size=n).round(3),
    "riwayat_telat_12bln": rng.poisson(0.8, size=n),
    "jenis_usaha":       rng.choice(["Kuliner","Retail","Jasa","Produksi"], size=n),
    "wilayah":           rng.choice(["Jawa","Sumatera","Kalimantan","Sulawesi"],
                                    size=n, p=[0.5, 0.22, 0.15, 0.13]),
    # Fitur berkardinalitas tinggi — untuk menguji bias kepentingan fitur
    "kode_cabang":       rng.integers(1, 121, size=n),
})

# Aturan pembangkit label (asumsi ilustratif): omzet kecil, usaha yang masih muda,
# rasio beban utang tinggi, dan riwayat telat bayar menaikkan peluang gagal bayar.
# jumlah_pegawai, jenis_usaha, wilayah, dan kode_cabang TIDAK ikut menentukan label.
# Intersep -0,8 membuat sekitar sepertiga pengajuan gagal bayar — sengaja tinggi
# agar pohon dangkal pun dapat menemukan pola (lihat Langkah 5).
logit = (-0.8 - 0.025 * df["omzet_bulanan_jt"] - 0.18 * df["lama_usaha_thn"]
         + 4.5 * df["rasio_beban_utang"] + 0.7 * df["riwayat_telat_12bln"])
df["gagal_bayar"] = rng.binomial(1, 1 / (1 + np.exp(-logit)))

print("Dimensi:", df.shape)
print("Proporsi gagal bayar:", df["gagal_bayar"].mean().round(3))
print("Jumlah per kelas (0 = lancar, 1 = gagal bayar):",
      df["gagal_bayar"].value_counts().sort_index().to_dict())
```

### LANGKAH 4: *Overfitting* pada Pohon Tunggal

```python
# =============================================
# LANGKAH 4: Pohon tanpa batas vs pohon terbatas
# =============================================
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import f1_score, roc_auc_score

X = df.drop(columns=["gagal_bayar"]); y = df["gagal_bayar"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE)

kol_kat = ["jenis_usaha", "wilayah"]
kol_num = [c for c in X.columns if c not in kol_kat]

pra = ColumnTransformer([
    # Pohon TIDAK memerlukan penskalaan
    ("num", "passthrough", kol_num),
    ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), kol_kat),
])

hasil = []
for nama, kedalaman in [("Tanpa batas", None), ("max_depth=3", 3),
                        ("max_depth=5", 5), ("max_depth=8", 8)]:
    p = Pipeline([("pra", pra),
                  ("clf", DecisionTreeClassifier(max_depth=kedalaman,
                                                 min_samples_leaf=1,
                                                 random_state=RANDOM_STATE))]).fit(X_train, y_train)
    f1_tr = f1_score(y_train, p.predict(X_train))
    f1_te = f1_score(y_test, p.predict(X_test))
    hasil.append({"Pohon": nama, "F1 latih": f1_tr, "F1 uji": f1_te,
                  "Selisih": f1_tr - f1_te,
                  "Kedalaman nyata": p.named_steps["clf"].get_depth(),
                  "Jumlah daun": p.named_steps["clf"].get_n_leaves()})

print(pd.DataFrame(hasil).round(4).to_string(index=False))
```

**Tulis kesimpulan:** pada pohon tanpa batas, berapa selisih F1 latih dan uji? Apa yang ditunjukkan jumlah daunnya?

### LANGKAH 5: Menampilkan Struktur Pohon

```python
# =============================================
# LANGKAH 5: Keterjelasan pohon
# =============================================
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

pohon_dangkal = Pipeline([
    ("pra", pra),
    ("clf", DecisionTreeClassifier(max_depth=3, min_samples_leaf=50,
                                   random_state=RANDOM_STATE)),
]).fit(X_train, y_train)

nama_fitur = pohon_dangkal.named_steps["pra"].get_feature_names_out()

fig, ax = plt.subplots(figsize=(18, 8))
plot_tree(pohon_dangkal.named_steps["clf"], feature_names=nama_fitur,
          class_names=["Lancar", "Gagal bayar"], filled=True,
          rounded=True, fontsize=8, ax=ax)
ax.set_title("Pohon keputusan kedalaman 3 — dapat dijelaskan kepada nasabah")
plt.tight_layout(); plt.show()

print(export_text(pohon_dangkal.named_steps["clf"],
                  feature_names=list(nama_fitur), max_depth=3))

# --- Aturan setiap daun, dihitung dari data LATIH (bukan teks tetap) ---
clf_dangkal = pohon_dangkal.named_steps["clf"]
struktur = clf_dangkal.tree_
nama_rapi = [f.split("__", 1)[1] for f in nama_fitur]   # buang awalan num__/kat__
label_kelas = {0: "Lancar", 1: "Gagal bayar"}

def telusuri(node=0, syarat=()):
    # Mengembalikan {id_daun: daftar syarat dari akar sampai daun itu}
    if struktur.children_left[node] == -1:              # -1 menandai daun
        return {node: list(syarat)}
    f, t = nama_rapi[struktur.feature[node]], struktur.threshold[node]
    return {**telusuri(struktur.children_left[node],  syarat + (f"{f} <= {t:.2f}",)),
            **telusuri(struktur.children_right[node], syarat + (f"{f} > {t:.2f}",))}

jalur = telusuri()
daun_latih = clf_dangkal.apply(pohon_dangkal[:-1].transform(X_train))
per_daun = (pd.DataFrame({"daun": daun_latih, "gagal": y_train.to_numpy()})
              .groupby("daun")["gagal"].agg(["size", "mean"]))

tabel_daun = pd.DataFrame([
    {"Prediksi": label_kelas[int(struktur.value[d, 0].argmax())],
     "% gagal": 100 * per_daun.loc[d, "mean"],
     "n latih": int(per_daun.loc[d, "size"]),
     "Aturan": " DAN ".join(jalur[d])}
    for d in jalur
]).sort_values("% gagal", ascending=False)

print("Aturan per daun (diurutkan dari yang paling berisiko):")
for _, r in tabel_daun.iterrows():
    print(f"  [{r['Prediksi']:<11}] {r['% gagal']:5.1f}% gagal dari {r['n latih']:4d} "
          f"pengajuan | JIKA {r['Aturan']}")

# --- Kesimpulan dihitung dari hasil ---
n_daun_gagal = int((tabel_daun["Prediksi"] == "Gagal bayar").sum())
f1_dangkal = f1_score(y_test, pohon_dangkal.predict(X_test))
print(f"\n{n_daun_gagal} dari {len(tabel_daun)} daun memprediksi 'Gagal bayar'; "
      f"F1 uji pohon dangkal = {f1_dangkal:.3f}")
if n_daun_gagal == 0:
    print("Semua daun memprediksi 'Lancar' (F1 = 0): pohon ini mudah dijelaskan, tetapi "
          "tidak menyaring satu pun pengajuan berisiko. Periksa proporsi gagal bayar "
          "atau coba class_weight='balanced' (Lab 7).")
elif n_daun_gagal == len(tabel_daun):
    print("Semua daun memprediksi 'Gagal bayar': pohon ini menandai setiap pengajuan "
          "sebagai berisiko sehingga tidak membedakan nasabah sama sekali. Periksa "
          "class_weight dan proporsi gagal bayar di Langkah 3.")
else:
    lancar_terburuk = tabel_daun.loc[tabel_daun["Prediksi"] == "Lancar", "% gagal"].max()
    print(f"Pohon menghasilkan aturan untuk kedua kelas. Namun daun 'Lancar' yang paling "
          f"berisiko masih memuat {lancar_terburuk:.0f}% gagal bayar —")
    if clf_dangkal.class_weight is None:
        # Tanpa pembobotan: label daun = kelas mayoritas (> 50%) data latih di daun itu
        print("label daun hanyalah suara mayoritas (> 50%), bukan jaminan bahwa nasabahnya aman.")
    else:
        # Dengan class_weight (Tantangan 4): label daun = mayoritas BERBOBOT, sehingga
        # daun "Gagal bayar" dapat memuat kurang dari separuh pengajuan gagal bayar
        gagal_terendah = tabel_daun.loc[tabel_daun["Prediksi"] == "Gagal bayar",
                                        "% gagal"].min()
        rincian = (f"daun 'Gagal bayar' bisa memuat kurang dari separuh gagal bayar "
                   f"(terendah {gagal_terendah:.0f}%)" if gagal_terendah < 50 else
                   f"pada pohon ini setiap daun 'Gagal bayar' masih memuat ≥ "
                   f"{gagal_terendah:.0f}% gagal bayar, tetapi itu tidak dijamin")
        print(f"dengan class_weight={clf_dangkal.class_weight!r}, label daun adalah suara "
              f"mayoritas BERBOBOT, bukan mayoritas > 50%: {rincian}.")
```

> **Inilah kelebihan pohon yang hilang pada *ensemble*:** keputusan untuk satu nasabah dapat ditelusuri sebagai rangkaian pertanyaan yang dapat dijelaskan. Pada bidang yang menuntut keterjelasan, ini bernilai tinggi — **asalkan** pohonnya memang memprediksi kedua kelas. Pohon dangkal yang semua daunnya berlabel "Lancar" tetap mudah dijelaskan, tetapi tidak berguna (F1 = 0).

**Membaca pohon pada data lab ini** (hasil sama pada scikit-learn 1.6 dan 1.9; ambang dibulatkan): pemisah akar adalah `rasio_beban_utang` ≤ 0,41. Pohon berisi 7 daun — cabang `omzet_bulanan_jt` > 74,40 berhenti lebih awal karena `min_samples_leaf=50` — dan **2 daun** berlabel "Gagal bayar":

| Aturan (akar → daun) | Pengajuan latih | Gagal bayar |
|---|---|---|
| `rasio_beban_utang` > 0,41 **dan** `omzet_bulanan_jt` ≤ 74,40 **dan** `lama_usaha_thn` ≤ 9,45 | 550 | 64,5% |
| `rasio_beban_utang` ≤ 0,41 **dan** `omzet_bulanan_jt` ≤ 39,05 **dan** `riwayat_telat_12bln` > 1,5 (telat **2 kali atau lebih**) | 255 | 62,0% |

Dengan bahasa nasabah: *"Pengajuan Bapak/Ibu tergolong berisiko karena rasio beban utang di atas 0,41, omzet di bawah ±74 juta rupiah per bulan, dan usaha berjalan kurang dari ±9,5 tahun."* F1 uji pohon dangkal ini ≈ 0,53 (bandingkan dengan baris `max_depth=3` di Langkah 4). Perhatikan pula daun-daun "Lancar": yang terbesar (`rasio_beban_utang` ≤ 0,41, `omzet_bulanan_jt` ≤ 39,05, `riwayat_telat_12bln` ≤ 1,5; 1.194 pengajuan latih) memuat ≈ 32% gagal bayar, dan yang paling berisiko ≈ 34%.

**Tulis interpretasi:** (a) jelaskan satu aturan "Gagal bayar" dengan kalimat yang dapat dipahami nasabah; (b) mengapa daun berisi lebih dari 30% gagal bayar tetap berlabel "Lancar", dan apa akibatnya bila bank hanya melihat label daun, bukan proporsinya? Hubungkan dengan pemilihan ambang di Lab 7.

**Pemeriksaan otomatis.** Sel berikut harus lulus tanpa `AssertionError`.

```python
# =============================================
# Pemeriksaan otomatis — Langkah 3 sampai 5
# =============================================
proporsi_gagal = y.mean()
assert 0.25 <= proporsi_gagal <= 0.45, (
    f"Proporsi gagal bayar {proporsi_gagal:.1%} di luar rentang 25–45% yang dimaksud — "
    f"periksa intersep logit di Langkah 3")

tanpa_batas = hasil[0]   # baris "Tanpa batas" dari Langkah 4
assert tanpa_batas["F1 latih"] >= 0.99 and tanpa_batas["Selisih"] >= 0.2, (
    f"Pohon tanpa batas seharusnya menghafal data latih (F1 latih ≈ 1) dengan selisih "
    f"F1 latih–uji besar; sekarang F1 latih {tanpa_batas['F1 latih']:.3f}, "
    f"selisih {tanpa_batas['Selisih']:.3f}")

assert n_daun_gagal >= 1 and n_daun_gagal < len(tabel_daun), (
    "Pohon dangkal harus memprediksi kedua kelas (ada daun 'Lancar' dan daun "
    "'Gagal bayar') — periksa proporsi gagal bayar di Langkah 3 atau class_weight")
assert f1_dangkal >= 0.30, (
    f"F1 uji pohon dangkal {f1_dangkal:.3f} terlalu rendah (< 0,30) — pohon belum "
    f"menyaring pengajuan berisiko; periksa data Langkah 3 atau class_weight")
print("Pemeriksaan otomatis lulus.")
```

### LANGKAH 6: *Ensemble*

```python
# =============================================
# LANGKAH 6: Random Forest dan Gradient Boosting — pada lipatan yang SAMA
# =============================================
from sklearn.ensemble import (RandomForestClassifier,
                              HistGradientBoostingClassifier)
from sklearn.model_selection import cross_val_score, StratifiedKFold
import time

# Satu objek lipatan untuk SEMUA perbandingan: setiap model dinilai pada lipatan yang sama
CV = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

def banding_berpasangan(skor_a, skor_b):
    # Membandingkan dua model yang dinilai pada lipatan YANG SAMA (skor berpasangan).
    # d_i = skor_A,i - skor_B,i ; simpangan baku sampel s_d (ddof=1) ; SE = s_d / akar(k)
    # Aturan praktis mata kuliah: selisih BERMAKNA bila |d̄| > 2·SE DAN arah selisih
    # sama dengan d̄ pada sebagian besar lipatan (di sini: >= 80%, yaitu 4 dari 5).
    d = np.asarray(skor_a) - np.asarray(skor_b)
    k = len(d)
    d_bar = d.mean()
    s_d = d.std(ddof=1)
    se = s_d / np.sqrt(k)
    searah = int((np.sign(d) == np.sign(d_bar)).sum())
    bermakna = bool(abs(d_bar) > 2 * se and searah >= 0.8 * k)
    return {"d": d, "k": k, "d_bar": d_bar, "s_d": s_d, "SE": se,
            "searah": searah, "bermakna": bermakna}

kandidat = {
    "Pohon (max_depth=5)": DecisionTreeClassifier(max_depth=5,
                                                  random_state=RANDOM_STATE),
    "Random Forest": RandomForestClassifier(n_estimators=300, max_features="sqrt",
                                            random_state=RANDOM_STATE, n_jobs=-1),
    "Gradient Boosting": HistGradientBoostingClassifier(
        max_iter=300, learning_rate=0.1, early_stopping=True,
        random_state=RANDOM_STATE),
}

baris, skor_lipatan = [], {}
for nama, clf in kandidat.items():
    pipa = Pipeline([("pra", pra), ("clf", clf)])
    t0 = time.time()
    skor = cross_val_score(pipa, X_train, y_train, cv=CV,      # CV yang SAMA
                           scoring="roc_auc", n_jobs=-1)
    durasi = time.time() - t0
    skor_lipatan[nama] = skor                                   # disimpan untuk uji berpasangan
    baris.append({"Model": nama, "ROC-AUC": skor.mean(),
                  "Simpangan": skor.std(ddof=1), "Min": skor.min(),
                  "Maks": skor.max(), "Waktu (s)": durasi})

tabel = (pd.DataFrame(baris).sort_values("ROC-AUC", ascending=False)
           .reset_index(drop=True))
print(tabel.round(4).to_string(index=False))

# Setiap model dibandingkan dengan peringkat 1 secara BERPASANGAN per lipatan
juara = tabel.loc[0, "Model"]
banding = []
for nama in tabel["Model"][1:]:
    b = banding_berpasangan(skor_lipatan[juara], skor_lipatan[nama])
    banding.append({"Dibandingkan dengan": nama, "d̄": b["d_bar"], "s_d": b["s_d"],
                    "SE": b["SE"], "Searah": f"{b['searah']}/{b['k']}",
                    "Bermakna?": "ya" if b["bermakna"] else "tidak"})
print(f"\nSelisih berpasangan: '{juara}' dikurangi model lain (per lipatan)")
print(pd.DataFrame(banding).round(4).to_string(index=False))

# --- Random Forest vs Gradient Boosting: kesimpulan dihitung dari hasil ---
b_ens = banding_berpasangan(skor_lipatan["Gradient Boosting"],
                            skor_lipatan["Random Forest"])
print("\nGradient Boosting − Random Forest")
print("  selisih per lipatan:", np.round(b_ens["d"], 4))
print(f"  d̄ = {b_ens['d_bar']:+.4f} | s_d = {b_ens['s_d']:.4f} | SE = {b_ens['SE']:.4f} "
      f"| batas 2·SE = {2 * b_ens['SE']:.4f} | searah {b_ens['searah']}/{b_ens['k']}")
if b_ens["bermakna"]:
    unggul, lawan = (("Gradient Boosting", "Random Forest") if b_ens["d_bar"] > 0
                     else ("Random Forest", "Gradient Boosting"))
    print(f"Kesimpulan: {unggul} lebih baik daripada {lawan} secara bermakna "
          f"(|d̄| > 2·SE dan searah di sebagian besar lipatan).")
else:
    print("Kesimpulan: TIDAK DAPAT DISIMPULKAN mana yang lebih baik antara Gradient "
          "Boosting dan Random Forest;\n  selisihnya masih dalam jangkauan variasi "
          "antarlipatan.")
```

> **Mengapa berpasangan, dan mengapa SE?** Karena ketiga model dinilai pada lipatan yang **sama** (satu objek `CV`), sebagian variasi skor berasal dari lipatannya sendiri (ada lipatan yang "mudah", ada yang "sulit") dan dialami semua model bersama-sama. Selisih per lipatan $d_i = \text{skor}_{A,i} - \text{skor}_{B,i}$ menghapus variasi bersama itu. Laporkan rerata $\bar d$, simpangan baku sampel $s_d$ (`ddof=1`), dan galat baku $SE = s_d/\sqrt{k}$ — ketidakpastian **rerata** selisih diukur oleh $SE$, bukan oleh simpangan baku skor masing-masing model. Rumus "simpangan gabungan" $\sqrt{s_1^2+s_2^2}$ **tidak dipakai**: rumus itu memperlakukan skor kedua model seolah-olah tidak berpasangan dan memakai simpangan baku (SD) alih-alih galat baku (SE). Inilah cara yang ditetapkan [Bab 8 §8.3.4](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md#834-perbandingan); rinciannya di [Bab 9 §9.4.2](../06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md#942-membaca-hasil-perbandingan) dan [Lampiran A.10](../06-buku-ajar/lampiran.md#a10-perbandingan-model).
>
> **Aturan praktis mata kuliah:** selisih dianggap bermakna bila $|\bar d| > 2 \cdot SE$ **dan** arahnya konsisten di sebagian besar lipatan (di lab ini: minimal 4 dari 5). Aturan ini hanya penyaring kasar: skor antarlipatan tidak benar-benar saling bebas (data latihnya tumpang-tindih), sehingga $SE$ cenderung terlalu kecil. Untuk analisis formal, gunakan *corrected resampled t-test* (Nadeau & Bengio, 2003). Seluruh simpangan baku skor lipatan di lab ini memakai **`ddof=1`** (simpangan baku sampel), sama dengan `pd.Series.std()`.

**Membaca hasil pada data lab ini** (scikit-learn 1.6 dan 1.9; hanya angka *Gradient Boosting* yang sedikit bergeser antarversi): *Gradient Boosting* (ROC-AUC ≈ 0,777–0,778) unggul atas *Random Forest* (≈ 0,768) dengan $\bar d \approx +0{,}009$ sampai $+0{,}011$ dan $SE \approx 0{,}003$ (batas $2 \cdot SE \approx 0{,}006$), searah di 4–5 dari 5 lipatan — **bermakna** menurut aturan praktis. Kedua *ensemble* juga unggul bermakna atas pohon tunggal (≈ 0,736; searah di 5 dari 5 lipatan). Perhatikan apa yang terjadi bila dipakai kaidah lama yang kini ditinggalkan — selisih rerata baru dianggap nyata bila **jauh melampaui** "simpangan gabungan" $\sqrt{s_1^2+s_2^2}$ dari kolom Simpangan, dan selisih yang hanya setara atau lebih kecil berarti **tidak dapat disimpulkan**. Simpangan gabungan kedua *ensemble* ≈ 0,011 pada scikit-learn 1.6 (**setara** dengan $\bar d$) dan ≈ 0,013 pada 1.9 (**lebih besar** daripada $\bar d$), sehingga kaidah lama itu pada kedua versi berujung "tidak dapat disimpulkan" — padahal *Gradient Boosting* unggul di 4–5 dari 5 lipatan.

**Tulis analisis:** (a) Hitung sendiri "simpangan gabungan" kedua *ensemble* dari kolom Simpangan, lalu bandingkan dengan $\bar d$ dan $2 \cdot SE$. Apa kesimpulan kaidah lama (selisih harus **jauh melampaui** simpangan gabungan) pada versi pustaka Anda, dan mengapa kesimpulan itu dapat berbeda dari kesimpulan uji berpasangan? Jelaskan dengan dua alasan: skor yang **berpasangan** per lipatan, dan perbedaan SD dengan SE. (b) Bila kesimpulan yang dicetak "tidak dapat disimpulkan", model mana yang Anda pilih, dan dengan alasan apa (waktu, kepekaan hiperparameter, keterjelasan — lihat tabel Bab 8 §8.3.4)? (c) Apakah selisih yang bermakna menurut aturan praktis juga bermakna **secara praktis** bagi bank yang menyaring pengajuan kredit?

**Pemeriksaan otomatis.**

```python
# =============================================
# Pemeriksaan otomatis — Langkah 6
# =============================================
pohon5 = skor_lipatan["Pohon (max_depth=5)"]
for m in ["Random Forest", "Gradient Boosting"]:
    b_m = banding_berpasangan(skor_lipatan[m], pohon5)
    assert b_m["bermakna"] and b_m["d_bar"] > 0, (
        f"{m} seharusnya mengungguli pohon tunggal secara bermakna pada lipatan yang sama "
        f"(sekarang d̄ = {b_m['d_bar']:+.4f}, SE = {b_m['SE']:.4f}) — periksa kandidat")
d_uji = skor_lipatan["Gradient Boosting"] - skor_lipatan["Random Forest"]
assert np.isclose(b_ens["s_d"], pd.Series(d_uji).std()) and np.isclose(
    b_ens["SE"], pd.Series(d_uji).std() / np.sqrt(len(d_uji))), (
    "SE harus = s_d/√k dengan s_d simpangan baku SAMPEL (ddof=1) dari selisih per lipatan")
assert np.isclose(tabel.set_index("Model").loc["Random Forest", "Simpangan"],
                  pd.Series(skor_lipatan["Random Forest"]).std()), (
    "Kolom Simpangan harus memakai simpangan baku sampel (ddof=1), sama dengan pd.Series.std()")
print("Pemeriksaan otomatis lulus.")
```

### LANGKAH 7: Kepentingan Fitur dan Biasnya

```python
# =============================================
# LANGKAH 7: Kepentingan bawaan vs permutasi
# =============================================
from sklearn.inspection import permutation_importance

rf = Pipeline([("pra", pra),
               ("clf", RandomForestClassifier(n_estimators=300,
                                              random_state=RANDOM_STATE,
                                              n_jobs=-1))]).fit(X_train, y_train)
nm = rf.named_steps["pra"].get_feature_names_out()

bawaan = pd.Series(rf.named_steps["clf"].feature_importances_, index=nm)

perm = permutation_importance(rf, X_test, y_test, n_repeats=10,
                              scoring="roc_auc", random_state=RANDOM_STATE, n_jobs=-1)
permutasi = pd.Series(perm.importances_mean, index=X_test.columns)

print("Kepentingan BAWAAN (10 teratas):")
print(bawaan.sort_values(ascending=False).head(10).round(4).to_string())

print("\nKepentingan PERMUTASI (10 teratas):")
print(permutasi.sort_values(ascending=False).head(10).round(4).to_string())

print("\nPeringkat kode_cabang:")
print("  bawaan   :", bawaan.filter(like="kode_cabang").round(4).to_string())
print("  permutasi:", permutasi.filter(like="kode_cabang").round(4).to_string())

# --- Kesimpulan dihitung dari hasil ---
peringkat_bawaan = int(bawaan.rank(ascending=False)["num__kode_cabang"])
kode_bawaan = bawaan["num__kode_cabang"]
kode_permutasi = permutasi["kode_cabang"]
# Fitur yang benar-benar ikut menentukan label tetapi kalah dari kode_cabang (bawaan)
kalah = [f for f in ["omzet_bulanan_jt", "lama_usaha_thn", "rasio_beban_utang",
                     "riwayat_telat_12bln"] if bawaan[f"num__{f}"] < kode_bawaan]
print(f"\nkode_cabang: peringkat {peringkat_bawaan} dari {len(bawaan)} pada kepentingan "
      f"bawaan ({kode_bawaan:.3f}), permutasi {kode_permutasi:+.4f}.")
if kalah and abs(kode_permutasi) < 0.01:
    print(f"Bias terlihat: fitur acak ini mengungguli {', '.join(kalah)} (yang benar-benar "
          f"menentukan label) pada kepentingan bawaan, padahal kepentingan permutasinya ≈ 0.")
elif abs(kode_permutasi) < 0.01:
    print("Kepentingan permutasi kode_cabang ≈ 0; pada data ini ia tidak mengungguli "
          "fitur penentu label mana pun pada kepentingan bawaan.")
else:
    print("Kepentingan permutasi kode_cabang tidak ≈ 0 — periksa ulang data dan model.")
```

> **Yang harus diperhatikan:** `kode_cabang` berisi 120 nilai acak yang **tidak** berhubungan dengan target. Kepentingan bawaan cenderung memberinya nilai tinggi karena kardinalitasnya tinggi; kepentingan permutasi mendekati nol. Inilah bias yang diperingatkan Strobl et al. (2007). Pada data lab ini, `kode_cabang` berada di peringkat 4 kepentingan bawaan (≈ 0,14) — di atas `riwayat_telat_12bln` yang benar-benar ikut menentukan label — sedangkan kepentingan permutasinya ≈ 0. Fitur lain yang tidak menentukan label, `jumlah_pegawai`, juga memperoleh kepentingan bawaan yang tidak kecil; bandingkan dengan nilai permutasinya.

**Pemeriksaan otomatis.**

```python
# =============================================
# Pemeriksaan otomatis — Langkah 7
# =============================================
assert abs(kode_permutasi) < 0.01, (
    f"Kepentingan permutasi kode_cabang {kode_permutasi:.4f} seharusnya ≈ 0 "
    f"(fitur acak) — periksa apakah permutasi dihitung pada data UJI")
assert kode_bawaan > 0.05 and kode_bawaan > 5 * max(kode_permutasi, 0.001), (
    f"Kepentingan bawaan kode_cabang ({kode_bawaan:.3f}) seharusnya jauh di atas nilai "
    f"permutasinya — inilah bias fitur berkardinalitas tinggi yang ingin ditunjukkan")
print("Pemeriksaan otomatis lulus.")
```

### LANGKAH 8: Stabilitas Kepentingan Fitur

```python
# =============================================
# LANGKAH 8: Apakah urutan kepentingan itu pasti?
# =============================================
peringkat = []
for seed in [1, 7, 42, 99, 2026]:
    m = Pipeline([("pra", pra),
                  ("clf", RandomForestClassifier(n_estimators=300,
                                                 random_state=seed,
                                                 n_jobs=-1))]).fit(X_train, y_train)
    s = pd.Series(m.named_steps["clf"].feature_importances_, index=nm)
    peringkat.append(s.rank(ascending=False))

tabel_peringkat = pd.concat(peringkat, axis=1)
tabel_peringkat.columns = [f"seed={s}" for s in [1, 7, 42, 99, 2026]]
tabel_peringkat["Rentang"] = (tabel_peringkat.max(axis=1)
                              - tabel_peringkat.min(axis=1))
print(tabel_peringkat.sort_values("Rentang", ascending=False).head(10).to_string())
```

**Tulis kesimpulan:** fitur mana yang peringkatnya paling tidak stabil? Apa artinya bagi pelaporan kepentingan fitur dalam laporan proyek?

---

## Tantangan Tambahan

### Tantangan 1 — *Cost-Complexity Pruning*

Gunakan `cost_complexity_pruning_path` untuk memperoleh rentang `ccp_alpha`, lalu buat grafik F1 latih dan uji terhadap `ccp_alpha`. Tentukan nilai optimumnya dan bandingkan dengan pembatasan `max_depth`.

### Tantangan 2 — Pengaruh Jumlah Pohon

Buat grafik ROC-AUC terhadap `n_estimators` pada rentang 10–500 untuk *Random Forest*. Pada titik berapa penambahan pohon berhenti membantu? Apa implikasinya bagi waktu komputasi?

### Tantangan 3 — Menghapus Fitur Tak Berguna

Buang `kode_cabang` dari data, lalu latih ulang ketiga model dengan objek `CV` yang sama. Apakah kinerjanya berubah secara bermakna? Ukur dengan `banding_berpasangan` (skor dengan vs tanpa `kode_cabang`, per lipatan). Jelaskan hubungannya dengan temuan Langkah 7.

### Tantangan 4 — Pohon Dangkal dengan `class_weight`

Latih ulang pohon dangkal Langkah 5 dengan `class_weight="balanced"` (Lab 7), lalu jalankan ulang kode tabel aturan daun. Apakah struktur pohon dan jumlah daun berlabel "Gagal bayar" berubah? Apakah setiap daun "Gagal bayar" masih memuat lebih dari 50% gagal bayar? Baca kalimat kesimpulan yang dicetak, lalu jelaskan arti "mayoritas berbobot". Bandingkan F1 dan *recall* ujinya dengan pohon tanpa pembobotan. Ubah pula intersep logit Langkah 3 dari −0,8 menjadi −2,3 (proporsi gagal bayar turun ke ±13%): apa yang terjadi pada pohon dangkal tanpa pembobotan, dan apakah `class_weight="balanced"` menolongnya? Pada percobaan ini pemeriksaan otomatis Langkah 3–5 memang akan gagal (proporsi di luar 25–45%); kembalikan intersep ke −0,8 setelah selesai.

---

## Checklist Penyelesaian

- [ ] **Perhitungan manual** *entropy* dan *information gain*, diverifikasi dengan sklearn
- [ ] Gini dihitung sebagai pembanding
- [ ] *Overfitting* pohon tanpa batas ditunjukkan dengan selisih F1 latih dan uji
- [ ] Struktur pohon dangkal ditampilkan dan dibaca; pohon memprediksi **kedua kelas** (F1 uji > 0)
- [ ] Satu aturan daun "Gagal bayar" dijelaskan dengan bahasa nasabah
- [ ] Tiga model dibandingkan dengan **lipatan yang sama** (satu objek `CV`; skor per lipatan disimpan)
- [ ] Rerata, simpangan (`ddof=1`), min, maks, dan waktu dilaporkan
- [ ] **Kesimpulan memakai selisih berpasangan per lipatan** ($\bar d$, $s_d$ dengan `ddof=1`, $SE = s_d/\sqrt{k}$), bukan hanya rerata
- [ ] Kepentingan bawaan **dan** permutasi dibandingkan
- [ ] Bias terhadap fitur berkardinalitas tinggi ditunjukkan pada `kode_cabang`
- [ ] Stabilitas peringkat kepentingan diperiksa lintas *seed*
- [ ] Keempat sel **Pemeriksaan otomatis** lulus
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 9](../03-modules/week-09-pohon-keputusan-dan-ensemble.md)
2. [Bab 8 buku ajar](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md)
3. Strobl, C., et al. (2007). Bias in Random Forest Variable Importance Measures. *BMC Bioinformatics*, 8(25).
4. Dokumentasi scikit-learn — *Ensemble methods*. <https://scikit-learn.org/stable/modules/ensemble.html>
5. Nadeau, C., & Bengio, Y. (2003). Inference for the Generalization Error. *Machine Learning*, 52(3), 239–281.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
