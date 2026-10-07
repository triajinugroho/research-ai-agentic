# Lab 14: Audit *Bias* dan *Model Card*

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 14 |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-13 |
| Durasi | 100 menit |
| Prasyarat | Lab 13 selesai; model proyek sudah ada |
| Bobot | 2,0% (Observasi, Sub-CPMK102-1) |
| Diuji pada | scikit-learn 1.6 dan 1.9, pandas 2.2 dan 3.0 (Oktober 2026) |

---

## Tujuan Praktikum

1. Mengukur kinerja model terpisah per kelompok.
2. Menghitung ukuran *fairness* dan menunjukkan mengapa ukuran-ukuran itu tidak dapat dipenuhi sekaligus oleh model yang berguna ketika *base rate* berbeda.
3. Menunjukkan bahwa menghapus atribut sensitif tidak menghapus ketimpangan bila ada fitur **proksi**.
4. Menyusun *model card* yang lengkap dan jujur.

---

## Ketentuan Khusus Lab Ini

> **Audit dilakukan pada model proyek Anda sendiri**, bukan pada contoh. Contoh pada lab ini hanya untuk mempelajari tekniknya. Luaran yang dinilai adalah audit atas model kelompok Anda.

---

## Persiapan

1. Buat notebook baru bernama `NIM_Nama_Lab14.ipynb`.
2. Jalankan **sel pembuka baku** di [Lampiran D](../06-buku-ajar/lampiran.md#lampiran-d-sel-pembuka-baku) — mengimpor pustaka, mencatat versi, dan menetapkan `RANDOM_STATE = 42`. Seluruh langkah di bawah mengandaikan sel itu sudah dijalankan.
3. **Data:** data kredit UMKM pada Langkah 1–7 adalah **data sintetis (simulasi)** yang meniru pola ketimpangan representasi wilayah dalam data terbuka Indonesia; **bukan data resmi BPS/lembaga** mana pun (termasuk bank atau OJK). Proporsi wilayah, rerata jarak ke ibu kota provinsi, skor akses internet, dan besarnya "efek wilayah" pada peluang gagal bayar adalah **asumsi ilustratif**, bukan temuan empiris. Data dirancang agar tiga gejala tampak jelas: (a) *base rate* gagal bayar berbeda antarwilayah; (b) dua fitur **proksi** — `jarak_ibukota_km` dan `skor_akses_internet` — sebarannya sangat bergantung pada wilayah, tetapi **tidak** ikut menentukan label secara langsung; (c) Papua hanya ±1% data, sehingga data latihnya kurang dari 100 baris.

---

## Langkah-langkah

### LANGKAH 1: Data dengan Ketimpangan Representasi dan Fitur Proksi

> **Data sintetis (simulasi)** yang meniru pola pengajuan kredit UMKM dengan data yang terpusat di Jawa; bukan data resmi BPS/lembaga. Peluang gagal bayar dibangkitkan dari omzet, lama usaha, rasio utang, riwayat telat bayar, dan **efek wilayah** (faktor wilayah yang tidak terekam sebagai fitur), ditambah keacakan.

```python
# =============================================
# LANGKAH 1: Data SINTETIS dengan ketimpangan representasi dan fitur proksi
# (simulasi, bukan data resmi BPS/lembaga)
# =============================================
import numpy as np, pandas as pd
rng = np.random.default_rng(RANDOM_STATE)

# Proporsi wilayah sengaja dibuat sangat timpang (asumsi ilustratif) —
# meniru data terbuka Indonesia yang terpusat di Jawa; Papua hanya ±1%
wilayah_nama = ["Jawa", "Sumatera", "Kalimantan", "Sulawesi", "Papua"]
wilayah_prop = [0.62, 0.21, 0.09, 0.07, 0.01]
n = 10_000

wilayah = rng.choice(wilayah_nama, size=n, p=wilayah_prop)
s_wil = pd.Series(wilayah)

# Rerata fitur PROKSI per wilayah (angka ilustratif, bukan data resmi)
rerata_jarak = {"Jawa": 20, "Sumatera": 60, "Kalimantan": 120,
                "Sulawesi": 90, "Papua": 200}          # km ke ibu kota provinsi
rerata_akses = {"Jawa": 85, "Sumatera": 65, "Kalimantan": 50,
                "Sulawesi": 55, "Papua": 30}           # skor akses internet 0–100

df = pd.DataFrame({
    "wilayah":        wilayah,
    "omzet_jt":       rng.gamma(2.0, 20, size=n).round(1),
    "lama_usaha_thn": rng.gamma(2.0, 2.5, size=n).round(1),
    "rasio_utang":    rng.beta(2, 5, size=n).round(3),
    "riwayat_telat":  rng.poisson(0.8, size=n),
    "jenis_usaha":    rng.choice(["Kuliner", "Retail", "Jasa", "Produksi"], size=n),
    # Dua proksi: nilainya ditentukan oleh wilayah + keacakan
    "jarak_ibukota_km":    (s_wil.map(rerata_jarak).to_numpy()
                            * rng.gamma(4.0, 0.25, size=n)).round(1),
    "skor_akses_internet": np.clip(rng.normal(s_wil.map(rerata_akses).to_numpy(), 10),
                                   0, 100).round(0),
})

# Label: proksi TIDAK masuk rumus; wilayah berpengaruh lewat "efek wilayah"
efek_wilayah = {"Jawa": 0.0, "Sumatera": 0.4, "Kalimantan": 0.8,
                "Sulawesi": 0.9, "Papua": 1.4}
logit = (-1.8 - 0.021 * df["omzet_jt"] - 0.15 * df["lama_usaha_thn"]
         + 2.7 * df["rasio_utang"] + 0.40 * df["riwayat_telat"]
         + df["wilayah"].map(efek_wilayah))
df["gagal_bayar"] = rng.binomial(1, 1 / (1 + np.exp(-logit)))

print("Sebaran wilayah:")
print(df["wilayah"].value_counts().to_string())
print(f"\nProporsi gagal bayar keseluruhan: {df['gagal_bayar'].mean():.3f}")
print("\nRingkasan per wilayah (base rate dan rerata proksi):")
print(df.groupby("wilayah")[["gagal_bayar", "jarak_ibukota_km",
                             "skor_akses_internet"]].mean().round(3).to_string())
```

> **Perhatikan:** angka kejadian dasar (*base rate*) gagal bayar berbeda antarwilayah (dari ±0,12 di Jawa sampai ±0,3 di Papua), dan rerata kedua proksi juga sangat berbeda antarwilayah. *Base rate* yang berbeda adalah kondisi yang membuat ukuran-ukuran *fairness* **tidak dapat dipenuhi sekaligus oleh pengklasifikasi yang berguna** — dibuktikan dengan angka pada Langkah 4.

### LANGKAH 2: Melatih Model

```python
# =============================================
# LANGKAH 2: Model — dengan atribut wilayah sebagai fitur
# =============================================
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score, recall_score

X = df.drop(columns=["gagal_bayar"]); y = df["gagal_bayar"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=RANDOM_STATE)

kol_kat = ["wilayah", "jenis_usaha"]
kol_num = [c for c in X.columns if c not in kol_kat]

pra = ColumnTransformer([
    ("num", "passthrough", kol_num),
    ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), kol_kat),
])

# class_weight="balanced": kelas gagal bayar (minoritas) diberi bobot lebih besar.
# Tanpa ini model jarang sekali memprediksi gagal bayar (pada data ini recall
# keseluruhan hanya ±0,04), sehingga audit recall per wilayah tidak bermakna.
model = Pipeline([
    ("pra", pra),
    ("clf", HistGradientBoostingClassifier(max_iter=300, early_stopping=True,
                                           class_weight="balanced",
                                           random_state=RANDOM_STATE)),
]).fit(X_train, y_train)

pred = model.predict(X_test)
prob = model.predict_proba(X_test)[:, 1]
print(f"ROC-AUC keseluruhan: {roc_auc_score(y_test, prob):.4f}")
print(f"Recall keseluruhan : {recall_score(y_test, pred):.4f}")
```

Dengan `class_weight="balanced"`, *recall* keseluruhan sekitar 0,53–0,56 dan ROC-AUC sekitar 0,69 (angka pastinya sedikit berbeda antarversi scikit-learn). Kinerja yang sedang ini disengaja: label dibangkitkan dengan banyak keacakan.

**Pemeriksaan otomatis.** Sel berikut harus lulus tanpa `AssertionError`; bila gagal, pesannya menunjukkan apa yang perlu diperiksa.

```python
# =============================================
# Pemeriksaan otomatis — Langkah 1 dan 2
# =============================================
n_latih_papua = int((X_train["wilayah"] == "Papua").sum())
assert n_latih_papua < 100, (
    f"Data latih Papua {n_latih_papua} baris — seharusnya < 100 agar efek data "
    f"sedikit tampak; periksa wilayah_prop di Langkah 1")
assert recall_score(y_test, pred) >= 0.4, (
    "Recall keseluruhan < 0,4 — audit recall per wilayah tidak bermakna; "
    "periksa class_weight='balanced' di Langkah 2")
print("Pemeriksaan otomatis lulus.")
```

### LANGKAH 3: Audit per Kelompok — Inti Lab Ini

```python
# =============================================
# LANGKAH 3: Fungsi audit
# =============================================
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score, confusion_matrix)

def audit_kelompok(y_true, y_pred, y_prob, kelompok, nama_kelompok="Kelompok"):
    # Menghitung metrik terpisah per kelompok
    baris = []
    for k in pd.unique(kelompok):
        m = (kelompok == k).values if hasattr(kelompok, "values") else (kelompok == k)
        yt, yp = np.asarray(y_true)[m], np.asarray(y_pred)[m]
        cm = confusion_matrix(yt, yp, labels=[0, 1])
        tn, fp, fn, tp = cm.ravel()
        baris.append({
            nama_kelompok: k,
            "n": int(m.sum()),
            "Positif": int(yt.sum()),          # jumlah kasus gagal bayar sebenarnya
            "Base rate": yt.mean(),
            "Akurasi": accuracy_score(yt, yp),
            "Precision": precision_score(yt, yp, zero_division=0),
            "Recall": recall_score(yt, yp, zero_division=0),
            "FPR": fp / (fp + tn) if (fp + tn) else 0.0,
            "Prop. prediksi positif": yp.mean(),
            "ROC-AUC": (roc_auc_score(yt, np.asarray(y_prob)[m])
                        if len(np.unique(yt)) > 1 else np.nan),
        })
    return pd.DataFrame(baris).sort_values("n", ascending=False)

# Recall kelompok yang kasus positifnya sangat sedikit tidak stabil:
# dengan 4 kasus, satu deteksi tambahan menggeser recall 25 poin.
MIN_POSITIF = 20

def selisih(tabel, kolom):
    # Selisih maks-min, hanya pada kelompok yang cukup kasus positifnya
    t = tabel[tabel["Positif"] >= MIN_POSITIF]
    return t[kolom].max() - t[kolom].min()

tabel = audit_kelompok(y_test, pred, prob, X_test["wilayah"], "Wilayah")
print("Audit kinerja per wilayah:")
print(tabel.round(4).to_string(index=False))

print(f"\nKinerja KESELURUHAN — akurasi {accuracy_score(y_test, pred):.4f}, "
      f"recall {recall_score(y_test, pred):.4f}")
kecil = tabel[tabel["Positif"] < MIN_POSITIF]
for w, k in zip(kecil["Wilayah"], kecil["Positif"]):
    print(f"Catatan: {w} hanya {k} kasus positif di data uji — tidak ikut "
          f"dihitung dalam selisih (perkiraannya tidak stabil).")
print(f"\nSelisih recall maks-min   : {selisih(tabel, 'Recall'):.4f}")
print(f"Selisih precision maks-min: {selisih(tabel, 'Precision'):.4f}")
print(f"Selisih FPR maks-min      : {selisih(tabel, 'FPR'):.4f}")
```

**Tulis temuan:** wilayah mana yang *recall*-nya paling rendah, dan wilayah mana yang FPR-nya paling tinggi? Dalam kasus kredit, siapa yang dirugikan oleh tiap jenis kesalahan — pemberi kredit (gagal bayar yang lolos) atau pemohon yang sebenarnya lancar membayar tetapi ditandai berisiko? Mengapa angka Papua tidak ikut dihitung dalam selisih, dan apa artinya bagi orang yang tinggal di sana?

### LANGKAH 4: Tiga Ukuran *Fairness*

```python
# =============================================
# LANGKAH 4: Ukuran fairness dan pertentangannya
# =============================================
print(f"(Semua selisih dihitung tanpa kelompok dengan < {MIN_POSITIF} kasus positif.)\n")
print("Demographic parity — proporsi prediksi positif harus SAMA:")
print(tabel[["Wilayah", "Prop. prediksi positif"]].round(4).to_string(index=False))
print(f"  Selisih maks-min: {selisih(tabel, 'Prop. prediksi positif'):.4f}")

print("\nEqual opportunity — recall harus SAMA:")
print(tabel[["Wilayah", "Recall"]].round(4).to_string(index=False))
print(f"  Selisih maks-min: {selisih(tabel, 'Recall'):.4f}")

print("\nEqualized odds — recall DAN FPR harus SAMA:")
print(tabel[["Wilayah", "Recall", "FPR"]].round(4).to_string(index=False))

print("\nBase rate per wilayah (angka kejadian sebenarnya):")
print(tabel[["Wilayah", "Base rate"]].round(4).to_string(index=False))

# (a) Identitas: P(prediksi positif | wilayah) = FPR + (Recall - FPR) x base rate
prop_hitung = tabel["FPR"] + (tabel["Recall"] - tabel["FPR"]) * tabel["Base rate"]
print("\nIdentitas FPR + (Recall - FPR) x base rate = proporsi prediksi positif:",
      bool(np.allclose(prop_hitung, tabel["Prop. prediksi positif"])))

# Andaikan equalized odds TERCAPAI sempurna: semua wilayah memakai
# recall r dan FPR f yang sama (di sini: nilai keseluruhan model).
tn_all, fp_all, fn_all, tp_all = confusion_matrix(y_test, pred).ravel()
r, f = tp_all / (tp_all + fn_all), fp_all / (fp_all + tn_all)
selisih_br = selisih(tabel, "Base rate")
print(f"Andai recall = {r:.3f} dan FPR = {f:.3f} di semua wilayah, selisih "
      f"proporsi prediksi positif = (r - f) x selisih base rate "
      f"= {r - f:.3f} x {selisih_br:.3f} = {(r - f) * selisih_br:.4f}")
print("-> nol HANYA bila r = f (model tak lebih baik dari tebakan) "
      "atau base rate sama.")

# (b) Pengklasifikasi TRIVIAL: menebak "lancar" untuk semua pemohon
pred_konstan = np.zeros(len(y_test), dtype=int)
tabel_k = audit_kelompok(y_test, pred_konstan, np.zeros(len(y_test)),
                         X_test["wilayah"], "Wilayah")
print(f"\nModel KONSTAN — selisih prop. positif {selisih(tabel_k, 'Prop. prediksi positif'):.1f}, "
      f"selisih recall {selisih(tabel_k, 'Recall'):.1f}, selisih FPR {selisih(tabel_k, 'FPR'):.1f}, "
      f"tetapi recall keseluruhan {recall_score(y_test, pred_konstan):.1f}")

# (c) Kesimpulan DIHITUNG dari hasil, bukan teks tetap
if selisih_br > 0.02:
    print(f"\nBase rate antarwilayah BERBEDA (selisih {selisih_br:.3f}). Akibatnya:")
    print("- demographic parity dan equalized odds tidak dapat dipenuhi bersamaan,")
    print("  kecuali oleh pengklasifikasi trivial seperti model konstan di atas")
    print("  (Barocas, Hardt & Narayanan, 2023);")
    print("- precision (PPV) yang sama dan FPR/FNR yang sama tidak dapat dicapai")
    print("  bersamaan (Chouldechova, 2017; lihat juga Kleinberg et al., 2017).")
    print("Insinyur harus MEMILIH ukuran yang diprioritaskan dan menyatakan alasannya.")
else:
    print(f"\nBase rate antarwilayah hampir sama (selisih {selisih_br:.3f}) — "
          "pertentangan antarukuran pada data ini lemah.")
```

> **Perhatikan polanya.** Pada data ini *precision* antarwilayah hampir sama (selisih ±0,03–0,04), sedangkan selisih *recall* dan FPR sekitar 0,3. Inilah yang diramalkan Chouldechova (2017): bila *base rate* berbeda dan *precision* dibuat setara, galatnya (FPR/FNR) tidak dapat setara. Sebaliknya, andaikan *equalized odds* tercapai sempurna, selisih proporsi prediksi positif masih sekitar 0,02 — tidak nol, karena *base rate* berbeda.
>
> **Yang benar dan yang keliru.** Pernyataan "tidak ada model yang dapat memenuhi semua ukuran *fairness*" **keliru**: model konstan di atas memenuhi *demographic parity* dan *equalized odds* sekaligus — dan tidak berguna. Pernyataan yang tepat: **ketika *base rate* berbeda, tidak ada pengklasifikasi yang berguna (non-trivial) yang dapat memenuhi semuanya.** Kleinberg et al. (2017) membuktikan hal serupa untuk skor risiko: kalibrasi dalam kelompok dan keseimbangan galat untuk kelas positif maupun negatif tidak dapat dipenuhi bersamaan, kecuali *base rate* antarkelompok sama atau prediksinya sempurna.

**Pemeriksaan otomatis.**

```python
# =============================================
# Pemeriksaan otomatis — Langkah 3 dan 4
# =============================================
assert np.allclose(prop_hitung, tabel["Prop. prediksi positif"]), (
    "Identitas FPR + (Recall - FPR) x base rate tidak terpenuhi — "
    "periksa perhitungan FPR dan Recall di audit_kelompok")
assert selisih_br > 0.02, (
    "Base rate antarwilayah hampir sama — periksa efek_wilayah di Langkah 1")
assert max(selisih(tabel_k, c) for c in ["Prop. prediksi positif", "Recall", "FPR"]) == 0, (
    "Model konstan seharusnya memenuhi ketiga ukuran dengan selisih nol")
assert recall_score(y_test, pred_konstan) == 0, (
    "Model konstan 'lancar semua' seharusnya tidak mendeteksi satu pun gagal bayar")
print("Pemeriksaan otomatis lulus.")
```

### LANGKAH 5: Menghapus Atribut Sensitif Tidak Cukup

```python
# =============================================
# LANGKAH 5: Membuang kolom wilayah — apakah ketimpangan hilang?
# =============================================
from sklearn.base import clone
from sklearn.dummy import DummyClassifier
from sklearn.metrics import balanced_accuracy_score

X2 = X.drop(columns=["wilayah"])
X2_train, X2_test = X2.loc[X_train.index], X2.loc[X_test.index]

pra2 = ColumnTransformer([
    ("num", "passthrough", kol_num),
    ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False),
     ["jenis_usaha"]),
])
model2 = Pipeline([
    ("pra", pra2),
    ("clf", HistGradientBoostingClassifier(max_iter=300, early_stopping=True,
                                           class_weight="balanced",
                                           random_state=RANDOM_STATE)),
]).fit(X2_train, y_train)

pred2 = model2.predict(X2_test)
prob2 = model2.predict_proba(X2_test)[:, 1]

# Audit TETAP dilakukan per wilayah, meski wilayah bukan lagi fitur
tabel2 = audit_kelompok(y_test, pred2, prob2, X_test["wilayah"], "Wilayah")
print("Audit setelah kolom wilayah DIBUANG:")
print(tabel2.round(4).to_string(index=False))

selisih1, selisih2 = selisih(tabel, "Recall"), selisih(tabel2, "Recall")
rasio = selisih2 / selisih1
print(f"\nSelisih recall — dengan wilayah : {selisih1:.4f}")
print(f"Selisih recall — tanpa wilayah  : {selisih2:.4f}  ({rasio:.0%} dari semula)")

# Seberapa baik wilayah dapat DITEBAK dari fitur yang tersisa?
proksi = ["jarak_ibukota_km", "skor_akses_internet"]

def tebak_wilayah(kol_num_dipakai):
    # Melatih model untuk menebak wilayah; balanced accuracy pada data uji
    penebak = Pipeline([
        ("pra", ColumnTransformer([
            ("num", "passthrough", kol_num_dipakai),
            ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False),
             ["jenis_usaha"]),
        ])),
        ("clf", HistGradientBoostingClassifier(random_state=RANDOM_STATE)),
    ]).fit(X2_train, X_train["wilayah"])
    return balanced_accuracy_score(X_test["wilayah"], penebak.predict(X2_test))

bacc_dummy = balanced_accuracy_score(
    X_test["wilayah"],
    DummyClassifier(strategy="most_frequent").fit(X2_train, X_train["wilayah"])
                                               .predict(X2_test))
bacc_semua = tebak_wilayah(kol_num)
bacc_tanpa_proksi = tebak_wilayah([c for c in kol_num if c not in proksi])
print(f"\nBalanced accuracy menebak wilayah (5 kelas):")
print(f"  tebakan mayoritas (Dummy)     : {bacc_dummy:.3f}")
print(f"  dari semua fitur yang tersisa : {bacc_semua:.3f}")
print(f"  dari fitur tersisa TANPA proksi: {bacc_tanpa_proksi:.3f}")

# Kesimpulan DIHITUNG dari hasil
if rasio >= 0.5:
    print(f"\nKetimpangan BERTAHAN: selisih recall tanpa wilayah = {rasio:.0%} dari semula.")
elif rasio >= 0.2:
    print(f"\nKetimpangan BERKURANG ({rasio:.0%} dari semula) tetapi tidak hilang.")
else:
    print(f"\nKetimpangan hampir hilang ({rasio:.0%} dari semula) pada data ini.")
if bacc_semua - bacc_dummy >= 0.2:
    print("Wilayah masih dapat ditebak dari fitur lain — terutama dari proksi "
          f"{proksi} — sehingga model tetap dapat membedakan wilayah.")
else:
    print("Wilayah sulit ditebak dari fitur yang tersisa; tetap ukur per kelompok.")
```

> **Kesimpulan yang harus ditulis:** membuang kolom wilayah **tidak** menghapus ketimpangan, karena wilayah masih dapat ditebak kembali dari fitur lain (**proksi**: jarak ke ibu kota provinsi dan akses internet). Pada data ini selisih *recall* antarwilayah setelah kolom wilayah dibuang masih sekitar 70–95% dari semula (bergantung versi scikit-learn), dan wilayah dapat ditebak dari fitur yang tersisa dengan *balanced accuracy* ±0,58 — jauh di atas 0,20 milik tebakan mayoritas; tanpa kedua proksi, angkanya turun ke ±0,20. Karena itu pengukuran per kelompok tetap wajib, **bahkan ketika atributnya tidak dipakai sebagai fitur**. Membuang proksinya juga bukan jalan keluar umum: proksi sering tidak diketahui, dan banyak di antaranya membawa informasi yang sah (lihat Tantangan 4).

**Pemeriksaan otomatis.**

```python
# =============================================
# Pemeriksaan otomatis — Langkah 5
# =============================================
assert rasio >= 0.5, (
    f"Selisih recall tanpa wilayah hanya {rasio:.0%} dari semula — pelajaran "
    f"'proksi mempertahankan ketimpangan' tidak tampak; periksa fitur proksi di Langkah 1")
assert bacc_semua - bacc_dummy >= 0.2, (
    "Wilayah seharusnya dapat ditebak jauh di atas tebakan mayoritas dari fitur proksi")
assert bacc_semua - bacc_tanpa_proksi >= 0.2, (
    "Tanpa kedua proksi, wilayah seharusnya jauh lebih sulit ditebak — "
    "periksa daftar `proksi`")
print("Pemeriksaan otomatis lulus.")
```

### LANGKAH 6: Visualisasi Ketimpangan dan Ketidakpastian

```python
# =============================================
# LANGKAH 6: Menampilkan ketimpangan secara visual
# =============================================
import matplotlib.pyplot as plt

def interval_wilson(k, n, z=1.96):
    # Selang kepercayaan 95% untuk proporsi k/n (metode Wilson)
    p = k / n
    d = 1 + z**2 / n
    pusat = (p + z**2 / (2 * n)) / d
    lebar = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / d
    return pusat - lebar, pusat + lebar

urut = tabel.sort_values("n", ascending=False).copy()
tp_kel = (urut["Recall"] * urut["Positif"]).round().astype(int)
batas = [interval_wilson(k, n) for k, n in zip(tp_kel, urut["Positif"])]
urut["Recall bawah"] = [b[0] for b in batas]
urut["Recall atas"] = [b[1] for b in batas]
# Base rate dari data LATIH — lebih stabil daripada data uji yang kecil
br_latih = y_train.groupby(X_train["wilayah"].values).mean()
urut["Base rate latih"] = urut["Wilayah"].map(br_latih).astype(float)
print(urut[["Wilayah", "n", "Positif", "Base rate latih", "Recall",
            "Recall bawah", "Recall atas"]].round(3).to_string(index=False))

fig, ax = plt.subplots(1, 3, figsize=(16, 4.5))

ax[0].barh(urut["Wilayah"][::-1], urut["n"][::-1])
ax[0].set_xlabel("Jumlah data uji"); ax[0].set_title("1. Representasi dalam data")

galat = [(urut["Recall"] - urut["Recall bawah"])[::-1],
         (urut["Recall atas"] - urut["Recall"])[::-1]]
ax[1].barh(urut["Wilayah"][::-1], urut["Recall"][::-1], xerr=galat,
           color="tab:orange", capsize=4)
ax[1].axvline(recall_score(y_test, pred), color="red", ls="--",
              label=f"Keseluruhan ({recall_score(y_test, pred):.3f})")
ax[1].set_xlabel("Recall (selang 95%)"); ax[1].set_title("2. Recall per wilayah")
ax[1].legend()

ax[2].scatter(urut["Base rate latih"], urut["Recall"], s=urut["n"] / 5)
for _, baris_w in urut.iterrows():
    ax[2].annotate(baris_w["Wilayah"], (baris_w["Base rate latih"], baris_w["Recall"]),
                   xytext=(5, 5), textcoords="offset points", fontsize=8)
ax[2].set_xlabel("Base rate (data latih)"); ax[2].set_ylabel("Recall")
ax[2].set_title("3. Base rate vs recall (ukuran titik ~ n)")

plt.tight_layout(); plt.show()
```

**Tulis pembahasan:** (a) Mengapa selang *recall* Papua jauh lebih lebar daripada wilayah lain? Dari berapa kasus positif angka itu dihitung? (b) Pada data ini, apakah perbedaan *recall* lebih sejalan dengan jumlah data atau dengan *base rate*? (c) Apa implikasinya bagi pengumpulan data di masa depan?

### LANGKAH 7: Satu Model vs Model per Kelompok

```python
# =============================================
# LANGKAH 7: Apakah model terpisah membantu?
# =============================================
baris = []
for w in wilayah_nama:
    m_tr = (X_train["wilayah"] == w).values
    m_te = (X_test["wilayah"] == w).values
    if m_tr.sum() < 100 or len(np.unique(y_test[m_te])) < 2:
        baris.append({"Wilayah": w, "n latih": int(m_tr.sum()),
                      "Recall (model tunggal)": tabel.loc[tabel["Wilayah"]==w,
                                                          "Recall"].iloc[0],
                      "Recall (model terpisah)": np.nan,
                      "Catatan": "data terlalu sedikit"})
        continue
    # clone(): salinan baru praproses agar pra2 di dalam model2 tidak ikut berubah
    m_khusus = Pipeline([
        ("pra", clone(pra2)),
        ("clf", HistGradientBoostingClassifier(max_iter=200, early_stopping=True,
                                               class_weight="balanced",
                                               random_state=RANDOM_STATE)),
    ]).fit(X2_train[m_tr], y_train[m_tr])
    r_khusus = recall_score(y_test[m_te], m_khusus.predict(X2_test[m_te]),
                            zero_division=0)
    baris.append({"Wilayah": w, "n latih": int(m_tr.sum()),
                  "Recall (model tunggal)": tabel.loc[tabel["Wilayah"]==w,
                                                      "Recall"].iloc[0],
                  "Recall (model terpisah)": r_khusus, "Catatan": ""})

hasil7 = pd.DataFrame(baris)
print(hasil7.round(4).to_string(index=False))

sedikit = hasil7[hasil7["Catatan"] == "data terlalu sedikit"]
if len(sedikit):
    daftar = ", ".join(f"{w} ({k} baris latih)"
                       for w, k in zip(sedikit["Wilayah"], sedikit["n latih"]))
    print(f"\nTidak dapat diberi model khusus: {daftar}.")
else:
    print("\nSemua wilayah cukup datanya untuk model khusus.")
```

**Tulis temuan:** apakah model terpisah menaikkan *recall* dibanding model tunggal? Untuk wilayah mana, dan mengapa menurut Anda?

> **Perhatikan baris "data terlalu sedikit"** (pada data ini: Papua, 85 baris latih). Kelompok yang datanya paling sedikit tidak dapat diberi model khusus, dan — seperti terlihat pada selang Langkah 6 — kinerjanya pun tidak dapat diukur dengan andal. Ketimpangan representasi seperti ini tidak dapat diselesaikan secara teknis semata; jalan keluarnya adalah pengumpulan data yang lebih baik dan kehati-hatian dalam menerapkan model pada kelompok itu.

**Pemeriksaan otomatis.**

```python
# =============================================
# Pemeriksaan otomatis — Langkah 6 dan 7
# =============================================
lebar_selang = (urut["Recall atas"] - urut["Recall bawah"]).set_axis(urut["Wilayah"])
assert lebar_selang["Papua"] > 2 * lebar_selang["Jawa"], (
    "Selang recall Papua seharusnya jauh lebih lebar daripada Jawa — "
    "periksa wilayah_prop di Langkah 1")
assert "Papua" in set(sedikit["Wilayah"]), (
    "Papua seharusnya ditandai 'data terlalu sedikit' (< 100 baris latih)")
print("Pemeriksaan otomatis lulus.")
```

### LANGKAH 8: Menyusun *Model Card*

```python
# =============================================
# LANGKAH 8: Model card — luaran wajib
# =============================================
# Buat berkas TERPISAH bernama model_card.md berisi format berikut,
# diisi dari hasil audit di atas.
```

```markdown
# Model Card — [Judul Model Proyek Anda]

## 1. Rincian Model
- Dikembangkan oleh: Kelompok __, IF52510031, Prodi Informatika UAI
- Tanggal: ______  ·  Versi: 1.0
- Jenis model: ______
- Sumber dan lisensi data: ______

## 2. Penggunaan yang Dimaksudkan
- **Untuk:** ______
- **BUKAN untuk:** ______
- Pengguna yang dituju: ______
- Di luar cakupan: ______

## 3. Data
- Sumber, periode, jumlah baris dan kolom: ______
- Cakupan kelompok (wilayah/kategori): ______
- **Yang TIDAK tercakup:** ______
- Prapemrosesan: ______

## 4. Kinerja
| Kelompok | n | Base rate | Precision | Recall | FPR |
|----------|---|-----------|-----------|--------|-----|
| Keseluruhan | | | | | |
| ... | | | | | |

- Baseline (DummyClassifier): ______
- Metrik utama dan alasan pemilihannya: ______

## 5. Keterbatasan
- Kelompok dengan kinerja terendah dan besarnya selisih: ______
- Kelompok yang datanya terlalu sedikit untuk dinilai: ______
- Kondisi ketika model tidak dapat diandalkan: ______
- Asumsi yang dapat gugur seiring waktu: ______

## 6. Pertimbangan Etis
- Siapa yang dapat dirugikan bila model salah: ______
- Fitur yang dapat menjadi proksi atribut sensitif: ______
- **Ukuran fairness yang dipilih DAN ALASANNYA:** ______
- Apa yang dikorbankan dengan pilihan itu: ______
- Mekanisme pengawasan manusia: ______
- Cara mengajukan keberatan atas keputusan: ______

## 7. Pemeliharaan
- Kapan model harus dilatih ulang: ______
- Indikator yang dipantau: ______
- Penanggung jawab: ______
```

### LANGKAH 9: Enam Pertanyaan Tanggung Jawab

```python
# =============================================
# LANGKAH 9: Jawab di sel Markdown
# =============================================
# 1. Siapa yang terdampak bila model salah, dan seberapa berat?
# 2. Adakah kelompok yang dirugikan secara tidak sebanding?
# 3. Adakah pengawasan manusia pada keputusan berdampak besar?
# 4. Dapatkah orang yang terdampak mengetahui bahwa keputusannya
#    melibatkan model?
# 5. Adakah jalan mengajukan keberatan dan memperoleh peninjauan manusia?
# 6. SIAPA yang bertanggung jawab ketika model merugikan seseorang?
#
# Pertanyaan keenam tidak memiliki jawaban teknis. Ia selalu terjawab
# dengan NAMA SESEORANG — tidak pernah dengan nama sebuah model.
```

---

## Tantangan Tambahan

### Tantangan 1 — Ambang per Kelompok

Tetapkan ambang keputusan yang **berbeda** untuk tiap wilayah sehingga *recall*-nya menjadi setara. Apa yang terjadi pada *precision* dan FPR masing-masing? Apakah pendekatan ini adil? Bahas dari dua sisi.

### Tantangan 2 — Bobot Sampel

Latih ulang model dengan `sample_weight` yang menaikkan bobot kelompok kecil. Apakah ketimpangan berkurang? Berapa biayanya pada kinerja keseluruhan?

### Tantangan 3 — Bias Umpan Balik

Simulasikan bias umpan balik: (a) latih model, (b) pakai prediksinya untuk memutuskan siapa yang "diperiksa", (c) hanya data yang diperiksa masuk ke data latih berikutnya, (d) latih ulang. Ulangi lima siklus. Bagaimana sebaran wilayah dalam data latih berubah? Apa pelajarannya?

### Tantangan 4 — Membuang Proksi

Latih ulang model tanpa kolom wilayah **dan** tanpa kedua proksi. Apa yang terjadi pada selisih *recall* antarwilayah dan pada ROC-AUC keseluruhan? Mengapa membuang semua proksi bukan jalan keluar umum pada data nyata, ketika proksi tidak selalu diketahui dan sebagian membawa informasi yang sah?

---

## Checklist Penyelesaian

- [ ] Audit kinerja **model proyek sendiri**, terpisah per minimal dua kelompok
- [ ] Selisih *recall*, *precision*, dan FPR antarkelompok dilaporkan, beserta jumlah kasus positif per kelompok
- [ ] Ketiga ukuran *fairness* dihitung
- [ ] **Pertentangan antarukuran ditunjukkan** dengan bukti *base rate* berbeda, dan dijelaskan mengapa hanya pengklasifikasi trivial yang dapat memenuhi semuanya
- [ ] Diperiksa apakah membuang atribut sensitif menghapus ketimpangan, dan **fitur proksinya diidentifikasi**
- [ ] Representasi data dan ketidakpastian kinerja per kelompok divisualisasikan
- [ ] **Ukuran *fairness* yang dipilih dinyatakan beserta alasan dan pengorbanannya**
- [ ] *Model card* lengkap sebagai berkas terpisah
- [ ] Bagian Keterbatasan dan Pertimbangan Etis **terisi jujur**
- [ ] Enam pertanyaan tanggung jawab dijawab
- [ ] Notebook berjalan ulang tanpa galat dan semua pemeriksaan otomatis lulus
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 14](../03-modules/week-14-ai-generatif-dan-ai-bertanggung-jawab.md)
2. [Bab 13 buku ajar](../06-buku-ajar/bab-13-ai-generatif-dan-ai-bertanggung-jawab.md)
3. Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and Machine Learning*. MIT Press. <https://fairmlbook.org>
4. Mitchell, M., et al. (2019). Model Cards for Model Reporting. *FAT* '19*, 220–229.
5. Kleinberg, J., Mullainathan, S., & Raghavan, M. (2017). Inherent Trade-Offs in the Fair Determination of Risk Scores. *Proceedings of the 8th Innovations in Theoretical Computer Science Conference (ITCS 2017)*, LIPIcs 67, 43:1–43:23. <https://doi.org/10.4230/LIPIcs.ITCS.2017.43> (pracetak 2016: arXiv:1609.05807)
6. Chouldechova, A. (2017). Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments. *Big Data*, 5(2), 153–163. <https://doi.org/10.1089/big.2016.0047>
7. Suresh, H., & Guttag, J. (2021). A Framework for Understanding Sources of Harm throughout the ML Life Cycle. *EAAMO '21*.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
