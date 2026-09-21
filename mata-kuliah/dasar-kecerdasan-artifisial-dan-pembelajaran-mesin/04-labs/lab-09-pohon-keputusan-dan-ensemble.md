# Lab 09: Pohon Keputusan dan *Ensemble*

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 9 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-08 |
| Durasi | 100 menit |
| Prasyarat | Lab 7 selesai; UTS |
| Bobot | 1,9% (Observasi) |

---

## Tujuan Praktikum

1. Menghitung *entropy* dan *information gain* secara manual.
2. Menunjukkan *overfitting* pada pohon tanpa batas kedalaman.
3. Membandingkan pohon tunggal, *Random Forest*, dan *gradient boosting*.
4. Menafsirkan kepentingan fitur beserta keterbatasannya.

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

print(export_text(pohon, feature_names=["omzet"]))
print("\nEntropy akar menurut sklearn:", round(pohon.tree_.impurity[0], 4))
print("Entropy akar hitungan manual  :", round(H_induk, 4))
```

### LANGKAH 3: Data Nyata

```python
# =============================================
# LANGKAH 3: Data kelayakan kredit UMKM
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

logit = (-1.8 - 0.022 * df["omzet_bulanan_jt"] - 0.16 * df["lama_usaha_thn"]
         + 2.8 * df["rasio_beban_utang"] + 0.42 * df["riwayat_telat_12bln"])
df["gagal_bayar"] = rng.binomial(1, 1 / (1 + np.exp(-logit)))

print("Dimensi:", df.shape)
print("Proporsi gagal bayar:", df["gagal_bayar"].mean().round(3))
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
```

> **Inilah kelebihan pohon yang hilang pada *ensemble*:** keputusan untuk satu nasabah dapat ditelusuri sebagai rangkaian pertanyaan yang dapat dijelaskan. Pada bidang yang menuntut keterjelasan, ini bernilai tinggi.

### LANGKAH 6: *Ensemble*

```python
# =============================================
# LANGKAH 6: Random Forest dan Gradient Boosting
# =============================================
from sklearn.ensemble import (RandomForestClassifier,
                              HistGradientBoostingClassifier)
from sklearn.model_selection import cross_val_score, StratifiedKFold
import time

CV = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

kandidat = {
    "Pohon (max_depth=5)": DecisionTreeClassifier(max_depth=5,
                                                  random_state=RANDOM_STATE),
    "Random Forest": RandomForestClassifier(n_estimators=300, max_features="sqrt",
                                            random_state=RANDOM_STATE, n_jobs=-1),
    "Gradient Boosting": HistGradientBoostingClassifier(
        max_iter=300, learning_rate=0.1, early_stopping=True,
        random_state=RANDOM_STATE),
}

baris = []
for nama, clf in kandidat.items():
    pipa = Pipeline([("pra", pra), ("clf", clf)])
    t0 = time.time()
    skor = cross_val_score(pipa, X_train, y_train, cv=CV,
                           scoring="roc_auc", n_jobs=-1)
    durasi = time.time() - t0
    baris.append({"Model": nama, "ROC-AUC": skor.mean(),
                  "Simpangan": skor.std(), "Min": skor.min(),
                  "Maks": skor.max(), "Waktu (s)": durasi})

tabel = pd.DataFrame(baris).sort_values("ROC-AUC", ascending=False)
print(tabel.round(4).to_string(index=False))
```

**Tulis analisis:** apakah selisih antarmodel lebih besar daripada simpangan antarlipatan? Bila tidak, apa kesimpulan yang sah?

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
```

> **Yang harus diperhatikan:** `kode_cabang` berisi 120 nilai acak yang **tidak** berhubungan dengan target. Kepentingan bawaan cenderung memberinya nilai tinggi karena kardinalitasnya tinggi; kepentingan permutasi mendekati nol. Inilah bias yang diperingatkan Strobl et al. (2007).

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

Buang `kode_cabang` dari data, lalu latih ulang ketiga model. Apakah kinerjanya berubah? Jelaskan hubungannya dengan temuan Langkah 7.

---

## Checklist Penyelesaian

- [ ] **Perhitungan manual** *entropy* dan *information gain*, diverifikasi dengan sklearn
- [ ] Gini dihitung sebagai pembanding
- [ ] *Overfitting* pohon tanpa batas ditunjukkan dengan selisih F1 latih dan uji
- [ ] Struktur pohon dangkal ditampilkan dan dibaca
- [ ] Tiga model dibandingkan dengan **lipatan yang sama**
- [ ] Rerata, simpangan, min, maks, dan waktu dilaporkan
- [ ] **Kesimpulan memperhatikan simpangan**, bukan hanya rerata
- [ ] Kepentingan bawaan **dan** permutasi dibandingkan
- [ ] Bias terhadap fitur berkardinalitas tinggi ditunjukkan pada `kode_cabang`
- [ ] Stabilitas peringkat kepentingan diperiksa lintas *seed*
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 9](../03-modules/week-09-pohon-keputusan-dan-ensemble.md)
2. [Bab 8 buku ajar](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md)
3. Strobl, C., et al. (2007). Bias in Random Forest Variable Importance Measures. *BMC Bioinformatics*, 8(25).
4. Dokumentasi scikit-learn — *Ensemble methods*. <https://scikit-learn.org/stable/modules/ensemble.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
