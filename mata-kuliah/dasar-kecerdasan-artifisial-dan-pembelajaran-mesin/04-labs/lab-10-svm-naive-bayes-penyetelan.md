# Lab 10: SVM, Naive Bayes, dan Penyetelan Hiperparameter

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 10 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-09 |
| Durasi | 100 menit |
| Prasyarat | Lab 9 selesai |
| Bobot | 1,9% (Observasi) |

---

## Tujuan Praktikum

1. Menerapkan SVM dengan berbagai *kernel* dan menyetel `C` serta `gamma`.
2. Menerapkan Naive Bayes sebagai pembanding cepat.
3. Menyetel hiperparameter pada data latih saja.
4. Merancang dan menjalankan perbandingan lima model yang adil.

---

## Langkah-langkah

### LANGKAH 1: Data dan Pembagian

```python
# =============================================
# LANGKAH 1: Data
# =============================================
import numpy as np, pandas as pd, time
from sklearn.model_selection import train_test_split, StratifiedKFold

rng = np.random.default_rng(RANDOM_STATE)
n = 3000

df = pd.DataFrame({
    "durasi_kunjungan_mnt": rng.gamma(2.0, 12, size=n).round(1),
    "jumlah_halaman":       rng.poisson(6, size=n) + 1,
    "nilai_keranjang_rb":   rng.gamma(2.0, 200, size=n).round(0),
    "usia_akun_hari":       rng.gamma(3.0, 150, size=n).round(0),
    "diskon_persen":        rng.choice([0, 5, 10, 15, 20, 30], size=n),
    "perangkat":            rng.choice(["Android","iOS","Web"], size=n,
                                       p=[0.55, 0.30, 0.15]),
    "kanal":                rng.choice(["Organik","Iklan","Referal","Surel"], size=n),
})

logit = (-2.0 + 0.018 * df["durasi_kunjungan_mnt"] + 0.10 * df["jumlah_halaman"]
         + 0.0011 * df["nilai_keranjang_rb"] + 0.028 * df["diskon_persen"])
df["beli"] = rng.binomial(1, 1 / (1 + np.exp(-logit)))

X = df.drop(columns=["beli"]); y = df["beli"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE)

print("Dimensi:", df.shape, "| Proporsi positif:", y.mean().round(3))
print("Latih:", X_train.shape, "| Uji:", X_test.shape)
```

### LANGKAH 2: `Pipeline` Dasar

```python
# =============================================
# LANGKAH 2: Pipeline yang dipakai seluruh model
# =============================================
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

kol_kat = ["perangkat", "kanal"]
kol_num = [c for c in X.columns if c not in kol_kat]

def buat_pipa(clf, skala=True):
    pra = ColumnTransformer([
        ("num", StandardScaler() if skala else "passthrough", kol_num),
        ("kat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), kol_kat),
    ])
    return Pipeline([("pra", pra), ("clf", clf)])

CV = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
```

### LANGKAH 3: SVM dengan Tiga *Kernel*

```python
# =============================================
# LANGKAH 3: SVM — penskalaan WAJIB
# =============================================
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

baris = []
for kernel in ["linear", "rbf", "poly"]:
    pipa = buat_pipa(SVC(kernel=kernel, C=1.0, gamma="scale",
                         random_state=RANDOM_STATE))
    t0 = time.time()
    skor = cross_val_score(pipa, X_train, y_train, cv=CV,
                           scoring="roc_auc", n_jobs=-1)
    baris.append({"Kernel": kernel, "ROC-AUC": skor.mean(),
                  "Simpangan": skor.std(), "Waktu (s)": time.time() - t0})

print(pd.DataFrame(baris).round(4).to_string(index=False))
```

### LANGKAH 4: Membuktikan Penskalaan Itu Wajib

```python
# =============================================
# LANGKAH 4: SVM tanpa penskalaan
# =============================================
pipa_skala = buat_pipa(SVC(kernel="rbf", random_state=RANDOM_STATE), skala=True)
pipa_tanpa = buat_pipa(SVC(kernel="rbf", random_state=RANDOM_STATE), skala=False)

s1 = cross_val_score(pipa_skala, X_train, y_train, cv=CV, scoring="roc_auc", n_jobs=-1)
s2 = cross_val_score(pipa_tanpa, X_train, y_train, cv=CV, scoring="roc_auc", n_jobs=-1)

print(f"SVM DENGAN penskalaan : {s1.mean():.4f} ± {s1.std():.4f}")
print(f"SVM TANPA penskalaan  : {s2.mean():.4f} ± {s2.std():.4f}")
print(f"Selisih               : {s1.mean() - s2.mean():+.4f}")
```

**Tulis penjelasan:** mengapa `nilai_keranjang_rb` (ratusan) menenggelamkan `jumlah_halaman` (satuan) pada perhitungan jarak?

### LANGKAH 5: Naive Bayes sebagai Pembanding Cepat

```python
# =============================================
# LANGKAH 5: Naive Bayes
# =============================================
from sklearn.naive_bayes import GaussianNB

pipa_nb = buat_pipa(GaussianNB())
t0 = time.time()
s_nb = cross_val_score(pipa_nb, X_train, y_train, cv=CV, scoring="roc_auc", n_jobs=-1)
print(f"GaussianNB: {s_nb.mean():.4f} ± {s_nb.std():.4f}  "
      f"({time.time()-t0:.2f} s)")

# Memeriksa asumsi kebebasan: apakah fitur saling berkorelasi?
korelasi = X_train[kol_num].corr()
print("\nKorelasi antarfitur numerik (nilai absolut > 0,3):")
tinggi = korelasi.where(np.triu(np.ones(korelasi.shape), k=1).astype(bool)).stack()
print(tinggi[tinggi.abs() > 0.3].round(3).to_string() or "  (tidak ada)")
```

> Asumsi kebebasan Naive Bayes hampir selalu dilanggar. Yang penting bukan apakah ia dilanggar, melainkan **apakah modelnya tetap berguna** — dan itu diukur, bukan diandaikan.

### LANGKAH 6: Penyetelan Hiperparameter

```python
# =============================================
# LANGKAH 6: GridSearchCV — HANYA pada data latih
# =============================================
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from scipy.stats import loguniform

ruang = {
    "clf__C":     [0.1, 1, 10, 100],
    "clf__gamma": [0.001, 0.01, 0.1, "scale"],
}

pencarian = GridSearchCV(
    buat_pipa(SVC(kernel="rbf", random_state=RANDOM_STATE)),
    ruang, cv=CV, scoring="roc_auc", n_jobs=-1, return_train_score=True,
)
t0 = time.time()
pencarian.fit(X_train, y_train)          # data uji TIDAK disentuh
print(f"Grid search selesai dalam {time.time()-t0:.1f} s")
print("Parameter terbaik:", pencarian.best_params_)
print(f"Skor CV terbaik  : {pencarian.best_score_:.4f}")

# Memeriksa apakah optimum berada di TEPI ruang pencarian
hasil_cv = pd.DataFrame(pencarian.cv_results_)
print("\nLima kombinasi teratas:")
print(hasil_cv.nlargest(5, "mean_test_score")[
    ["param_clf__C", "param_clf__gamma", "mean_test_score", "std_test_score"]
].round(4).to_string(index=False))
```

**Periksa:** apakah nilai `C` atau `gamma` terbaik berada di ujung rentang yang dicoba? Bila ya, ruang pencarian perlu diperluas.

### LANGKAH 7: `best_score_` Bukan Kinerja Akhir

```python
# =============================================
# LANGKAH 7: Perbedaan best_score_ dan skor uji
# =============================================
from sklearn.metrics import roc_auc_score

skor_uji = roc_auc_score(y_test,
                         pencarian.best_estimator_.predict_proba(X_test)[:, 1]
                         if hasattr(pencarian.best_estimator_.named_steps["clf"], "predict_proba")
                         else pencarian.best_estimator_.decision_function(X_test))

print(f"best_score_ (CV data latih): {pencarian.best_score_:.4f}")
print(f"Skor pada data uji         : {skor_uji:.4f}")
print(f"Selisih                    : {pencarian.best_score_ - skor_uji:+.4f}")
print("\nbest_score_ SUDAH DIOPTIMALKAN atas ruang pencarian,")
print("sehingga cenderung lebih tinggi daripada kinerja sebenarnya.")
print("Yang dilaporkan sebagai kinerja akhir adalah skor pada data uji.")
```

### LANGKAH 8: Perbandingan Lima Model yang Adil

```python
# =============================================
# LANGKAH 8: Perbandingan — lipatan SAMA untuk semua
# =============================================
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier

kandidat = {
    "Baseline (mayoritas)": buat_pipa(DummyClassifier(strategy="most_frequent")),
    "Naive Bayes":          buat_pipa(GaussianNB()),
    "Regresi logistik":     buat_pipa(LogisticRegression(max_iter=1000,
                                                         random_state=RANDOM_STATE)),
    "SVM (RBF, disetel)":   pencarian.best_estimator_,
    "Random Forest":        buat_pipa(RandomForestClassifier(
                                n_estimators=300, random_state=RANDOM_STATE, n_jobs=-1),
                                skala=False),
    "Gradient Boosting":    buat_pipa(HistGradientBoostingClassifier(
                                max_iter=300, early_stopping=True,
                                random_state=RANDOM_STATE), skala=False),
}

baris = []
for nama, pipa in kandidat.items():
    t0 = time.time()
    skor = cross_val_score(pipa, X_train, y_train, cv=CV,   # CV yang SAMA
                           scoring="roc_auc", n_jobs=-1)
    baris.append({"Model": nama, "ROC-AUC": skor.mean(), "Simpangan": skor.std(),
                  "Min": skor.min(), "Maks": skor.max(),
                  "Waktu (s)": time.time() - t0})

tabel = pd.DataFrame(baris).sort_values("ROC-AUC", ascending=False)
print(tabel.round(4).to_string(index=False))

# Apakah selisih antara peringkat 1 dan 2 lebih besar daripada simpangannya?
t = tabel.reset_index(drop=True)
selisih = t.loc[0, "ROC-AUC"] - t.loc[1, "ROC-AUC"]
simpangan_gabung = np.sqrt(t.loc[0, "Simpangan"]**2 + t.loc[1, "Simpangan"]**2)
print(f"\nSelisih peringkat 1 dan 2 : {selisih:.4f}")
print(f"Simpangan gabungan        : {simpangan_gabung:.4f}")
print("Kesimpulan:",
      "perbedaan kemungkinan nyata" if selisih > simpangan_gabung
      else "TIDAK DAPAT DISIMPULKAN mana yang lebih baik")
```

### LANGKAH 9: Validasi Silang Bersarang

```python
# =============================================
# LANGKAH 9: Taksiran kinerja yang tidak bias
# =============================================
from sklearn.model_selection import cross_val_score, KFold

lingkar_dalam = StratifiedKFold(n_splits=3, shuffle=True, random_state=RANDOM_STATE)
lingkar_luar  = StratifiedKFold(n_splits=5, shuffle=True, random_state=7)

pencarian_dalam = GridSearchCV(
    buat_pipa(SVC(kernel="rbf", random_state=RANDOM_STATE)),
    {"clf__C": [1, 10], "clf__gamma": [0.01, "scale"]},
    cv=lingkar_dalam, scoring="roc_auc", n_jobs=-1)

skor_bersarang = cross_val_score(pencarian_dalam, X, y, cv=lingkar_luar,
                                 scoring="roc_auc", n_jobs=-1)
print(f"Taksiran tidak bias: {skor_bersarang.mean():.4f} ± {skor_bersarang.std():.4f}")
print(f"Bandingkan dengan best_score_: {pencarian.best_score_:.4f}")
```

---

## Tantangan Tambahan

### Tantangan 1 — *Grid* vs *Random Search*

Jalankan `RandomizedSearchCV` dengan `n_iter=16` (sama banyaknya dengan kombinasi *grid* 4×4) memakai `loguniform`. Bandingkan skor terbaik dan waktunya. Mana yang lebih efisien pada ruang besar, dan mengapa?

### Tantangan 2 — Skala Data dan SVM

Kurangi data menjadi 500, 1.000, 2.000, dan 3.000 baris. Catat waktu pelatihan SVM pada masing-masing. Buat grafik waktu terhadap jumlah baris. Bagaimana bentuk kurvanya, dan apa implikasinya untuk data besar?

### Tantangan 3 — Anggaran Penyetelan yang Tidak Setara

Setel *Random Forest* dengan 4 kombinasi dan SVM dengan 64 kombinasi, lalu bandingkan. Apakah perbandingan itu adil? Jelaskan mengapa anggaran penyetelan yang setara merupakan salah satu syarat perbandingan yang sah.

---

## Checklist Penyelesaian

- [ ] SVM dijalankan dengan tiga *kernel* di dalam `Pipeline` berpenskalaan
- [ ] Dampak tidak adanya penskalaan pada SVM **ditunjukkan dengan angka**
- [ ] Naive Bayes dijalankan sebagai pembanding cepat
- [ ] Asumsi kebebasan diperiksa melalui korelasi antarfitur
- [ ] `GridSearchCV` dijalankan **hanya pada data latih**
- [ ] Diperiksa apakah optimum berada di tepi ruang pencarian
- [ ] Perbedaan `best_score_` dan skor uji dijelaskan
- [ ] Lima model dibandingkan dengan **lipatan yang sama**
- [ ] **Kesimpulan memperhatikan simpangan**, bukan hanya rerata
- [ ] Validasi silang bersarang dijalankan
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 10](../03-modules/week-10-svm-naive-bayes-pemilihan-model.md)
2. [Bab 9 buku ajar](../06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md)
3. Cawley, G. C., & Talbot, N. L. C. (2010). On Over-fitting in Model Selection. *JMLR*, 11, 2079–2107.
4. Dokumentasi scikit-learn — *Grid search*. <https://scikit-learn.org/stable/modules/grid_search.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
