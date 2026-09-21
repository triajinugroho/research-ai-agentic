# Lab 03: *Pipeline* Prapemrosesan

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 3 |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-03 |
| Durasi | 100 menit |
| Prasyarat | Lab 2 selesai |
| Bobot | 1,9% (Observasi) |

---

## Tujuan Praktikum

1. Memeriksa kualitas data secara sistematis.
2. Menangani nilai hilang sesuai pola kehilangannya.
3. Menyandikan variabel kategorik dengan tepat.
4. Membangun `Pipeline` dan `ColumnTransformer` yang mencegah kebocoran.

---

## Persiapan

- Notebook `NIM_Nama_Lab03.ipynb` dengan sel pembuka baku.

---

## Langkah-langkah

### LANGKAH 1: Data yang Sengaja Tidak Bersih

```python
# =============================================
# LANGKAH 1: Data mentah dengan masalah nyata
# =============================================
import numpy as np, pandas as pd
rng = np.random.default_rng(RANDOM_STATE)
n = 1500

df = pd.DataFrame({
    "provinsi": rng.choice(
        ["DKI Jakarta", "dki jakarta", "DKI JAKARTA",      # kapitalisasi beda
         "Jawa Barat", "Jawa barat",
         "D.I. Yogyakarta", "DI Yogyakarta",                # ejaan beda
         "Jawa Timur", "Sumatera Utara", "Bali"], size=n),
    "omzet_bulanan": rng.gamma(2.0, 18, size=n).round(1),
    "lama_usaha":    rng.gamma(2.0, 2.5, size=n).round(1),
    "jumlah_pegawai": rng.poisson(4, size=n) + 1,
    "pendidikan_pemilik": rng.choice(
        ["SD", "SMP", "SMA", "D3", "S1", "S2"], size=n,
        p=[0.08, 0.15, 0.40, 0.15, 0.19, 0.03]),
    "jenis_usaha": rng.choice(["Kuliner", "Retail", "Jasa", "Produksi"], size=n),
})

# Masalah 1: kode nilai hilang yang tidak diterjemahkan
idx = rng.choice(n, size=90, replace=False)
df.loc[idx, "omzet_bulanan"] = -99

# Masalah 2: nilai hilang sesungguhnya (NaN)
idx2 = rng.choice(n, size=140, replace=False)
df.loc[idx2, "lama_usaha"] = np.nan

# Masalah 3: kolom numerik terbaca sebagai teks
df["modal_awal"] = [f"Rp {v:,.0f}".replace(",", ".")
                    for v in rng.gamma(2.0, 30_000_000, size=n)]

# Masalah 4: baris duplikat
df = pd.concat([df, df.iloc[:40]], ignore_index=True)

# Target
df["berkembang"] = rng.binomial(
    1, 1 / (1 + np.exp(-(-1.0 + 0.012 * df["omzet_bulanan"].clip(lower=0)))))

print("Dimensi awal:", df.shape)
display(df.head())
```

### LANGKAH 2: Tujuh Perintah Pembuka

```python
# =============================================
# LANGKAH 2: Pemeriksaan kualitas
# =============================================
print("1. Dimensi:", df.shape, "\n")

print("2. Info:")
df.info()

print("\n3. Ringkasan numerik:")
display(df.describe().T.round(2))

print("\n4. Nilai hilang (%):")
print((df.isna().mean() * 100).round(2).sort_values(ascending=False))

print("\n5. Duplikat penuh:", df.duplicated().sum())

print("\n6. Kardinalitas kolom kategorik:")
for kol in df.select_dtypes(include="object").columns:
    print(f"   {kol:22s} {df[kol].nunique():4d} nilai unik")

print("\n7. Sebaran target:")
print(df["berkembang"].value_counts(normalize=True).round(3))
```

**Tulis di sel Markdown: empat masalah apa yang Anda temukan dari keluaran di atas?**

### LANGKAH 3: Memperbaiki Masalah Struktural

Perbaikan struktural dilakukan **sebelum** pembagian data karena tidak melibatkan statistik data — hanya pembacaan ulang nilai.

```python
# =============================================
# LANGKAH 3: Perbaikan struktural
# =============================================
n_awal = len(df)

# (a) Kode nilai hilang -> NaN
n_minus99 = (df["omzet_bulanan"] == -99).sum()
df.loc[df["omzet_bulanan"] == -99, "omzet_bulanan"] = np.nan
print(f"(a) {n_minus99} nilai -99 diubah menjadi NaN")

# (b) Kolom teks -> numerik
df["modal_awal"] = (df["modal_awal"]
                    .str.replace("Rp ", "", regex=False)
                    .str.replace(".", "", regex=False)
                    .astype(float))
print(f"(b) modal_awal dikonversi ke numerik, tipe: {df['modal_awal'].dtype}")

# (c) Pembakuan nama provinsi
df["provinsi"] = (df["provinsi"].str.strip().str.title()
                  .replace({"Dki Jakarta": "DKI Jakarta",
                            "D.I. Yogyakarta": "DI Yogyakarta",
                            "Di Yogyakarta": "DI Yogyakarta"}))
print(f"(c) Provinsi dibakukan: {df['provinsi'].nunique()} nilai unik")

# (d) Duplikat dibuang
n_dup = df.duplicated().sum()
df = df.drop_duplicates().reset_index(drop=True)
print(f"(d) {n_dup} baris duplikat dibuang")

print(f"\nBaris: {n_awal} -> {len(df)} ({(n_awal-len(df))/n_awal*100:.1f}% dibuang)")
```

> **Catat setiap keputusan: apa, berapa banyak, mengapa.** Ini kriteria penilaian `Sub-CPMK102-1`.

### LANGKAH 4: Menganalisis Pola Nilai Hilang

```python
# =============================================
# LANGKAH 4: MCAR, MAR, atau MNAR?
# =============================================
# Periksa apakah kehilangan berkaitan dengan variabel lain
for kol_hilang in ["omzet_bulanan", "lama_usaha"]:
    hilang = df[kol_hilang].isna()
    print(f"\n--- {kol_hilang} ({hilang.sum()} hilang) ---")
    for kol_lain in ["jumlah_pegawai", "modal_awal"]:
        rata_hilang = df.loc[hilang, kol_lain].mean()
        rata_ada    = df.loc[~hilang, kol_lain].mean()
        print(f"  {kol_lain:16s}: hilang={rata_hilang:12.1f} "
              f"ada={rata_ada:12.1f} selisih={abs(rata_hilang-rata_ada)/rata_ada*100:5.1f}%")
```

**Tulis kesimpulan:** bila rata-rata variabel lain sangat berbeda antara baris yang hilang dan yang tidak, kehilangan **tidak acak** (MAR atau MNAR), dan penghapusan baris akan menimbulkan bias.

### LANGKAH 5: Pembagian Data — Sebelum Prapemrosesan Statistik

```python
# =============================================
# LANGKAH 5: Pembagian data
# =============================================
from sklearn.model_selection import train_test_split

X = df.drop(columns=["berkembang"])
y = df["berkembang"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE)

print(f"Latih: {X_train.shape}  Uji: {X_test.shape}")
```

> **Urutannya penting.** Imputasi, penskalaan, dan penyandian dilakukan **setelah** pembagian — dan di dalam `Pipeline` agar terjadi otomatis.

### LANGKAH 6: Demonstrasi Kebocoran

```python
# =============================================
# LANGKAH 6: Menunjukkan dampak kebocoran
# =============================================
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

kol_num = ["omzet_bulanan", "lama_usaha", "jumlah_pegawai", "modal_awal"]

# --- CARA SALAH: fit pada seluruh data ---
X_num_semua = X[kol_num].copy()
X_num_semua = pd.DataFrame(
    SimpleImputer(strategy="median").fit_transform(X_num_semua),
    columns=kol_num, index=X.index)
X_num_semua = pd.DataFrame(
    StandardScaler().fit_transform(X_num_semua),
    columns=kol_num, index=X.index)

Xtr_b, Xte_b, ytr_b, yte_b = train_test_split(
    X_num_semua, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE)
m_bocor = LogisticRegression(max_iter=1000, random_state=RANDOM_STATE).fit(Xtr_b, ytr_b)
auc_bocor = roc_auc_score(yte_b, m_bocor.predict_proba(Xte_b)[:, 1])

# --- CARA BENAR: Pipeline ---
from sklearn.pipeline import Pipeline
m_benar = Pipeline([
    ("imputasi", SimpleImputer(strategy="median")),
    ("skala", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000, random_state=RANDOM_STATE)),
]).fit(X_train[kol_num], y_train)
auc_benar = roc_auc_score(y_test, m_benar.predict_proba(X_test[kol_num])[:, 1])

print(f"ROC-AUC dengan kebocoran : {auc_bocor:.4f}")
print(f"ROC-AUC dengan Pipeline  : {auc_benar:.4f}")
print(f"Selisih                  : {auc_bocor - auc_benar:+.4f}")
```

**Tulis penjelasan:** mengapa cara pertama menghasilkan skor yang lebih tinggi, dan mengapa skor itu **tidak jujur**?

> Pada data yang cukup besar dan bersih, selisihnya kecil. Pada data kecil atau berpencilan, selisihnya bisa sangat besar. Yang keliru bukan besarnya selisih, melainkan **prosedurnya**.

### LANGKAH 7: `Pipeline` Lengkap dengan `ColumnTransformer`

```python
# =============================================
# LANGKAH 7: Pipeline lengkap
# =============================================
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, RobustScaler

kol_num = ["omzet_bulanan", "lama_usaha", "jumlah_pegawai", "modal_awal"]
kol_nominal = ["provinsi", "jenis_usaha"]
kol_ordinal = ["pendidikan_pemilik"]

# Urutan pendidikan DITENTUKAN sendiri, bukan diserahkan ke abjad
urutan_pendidikan = [["SD", "SMP", "SMA", "D3", "S1", "S2"]]

alur_num = Pipeline([
    ("imputasi", SimpleImputer(strategy="median")),
    # RobustScaler karena omzet dan modal sangat menceng kanan
    ("skala", RobustScaler()),
])

alur_nominal = Pipeline([
    ("imputasi", SimpleImputer(strategy="constant", fill_value="TIDAK_DIKETAHUI")),
    ("sandi", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
])

alur_ordinal = Pipeline([
    ("imputasi", SimpleImputer(strategy="most_frequent")),
    ("sandi", OrdinalEncoder(categories=urutan_pendidikan,
                             handle_unknown="use_encoded_value",
                             unknown_value=-1)),
])

prapemrosesan = ColumnTransformer([
    ("num", alur_num, kol_num),
    ("nom", alur_nominal, kol_nominal),
    ("ord", alur_ordinal, kol_ordinal),
])

model = Pipeline([
    ("pra", prapemrosesan),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced",
                               random_state=RANDOM_STATE)),
])

model.fit(X_train, y_train)
print("ROC-AUC:", roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]).round(4))
```

### LANGKAH 8: Memeriksa Hasil Transformasi

```python
# =============================================
# LANGKAH 8: Apa yang dihasilkan prapemrosesan?
# =============================================
X_tr_transformasi = model.named_steps["pra"].transform(X_train)
nama_kolom = model.named_steps["pra"].get_feature_names_out()

print(f"Kolom sebelum : {X_train.shape[1]}")
print(f"Kolom sesudah : {X_tr_transformasi.shape[1]}")
print(f"\nNama kolom hasil ({len(nama_kolom)}):")
for nm in nama_kolom:
    print("  ", nm)

# Periksa: tidak boleh ada NaN yang tersisa
print("\nNaN tersisa:", np.isnan(X_tr_transformasi).sum())
```

---

## Tantangan Tambahan

### Tantangan 1 — Membandingkan Strategi Imputasi

Bandingkan `SimpleImputer(strategy="median")` dengan `KNNImputer(n_neighbors=5)` pada kolom numerik. Laporkan selisih ROC-AUC dan waktu komputasi. Apakah peningkatannya sepadan?

### Tantangan 2 — Penanda Nilai Hilang

Tambahkan `SimpleImputer(add_indicator=True)`. Apakah informasi "nilai ini hilang" sendiri membantu prediksi? Bila ya, apa artinya tentang pola kehilangan pada data ini?

### Tantangan 3 — Kardinalitas Tinggi

Tambahkan kolom `kecamatan` dengan 200 nilai unik. Bandingkan tiga penanganan: *one-hot* penuh, penggabungan kategori jarang menjadi "LAINNYA", dan *frequency encoding*. Laporkan jumlah kolom hasil dan ROC-AUC masing-masing.

---

## Checklist Penyelesaian

- [ ] Tujuh perintah pembuka dijalankan dan keempat masalah data diidentifikasi
- [ ] Perbaikan struktural dilakukan dan **dicatat: apa, berapa, mengapa**
- [ ] Pola nilai hilang dianalisis (MCAR/MAR/MNAR) dengan bukti
- [ ] Pembagian data dilakukan **sebelum** prapemrosesan statistik
- [ ] Demonstrasi kebocoran dijalankan dan selisihnya dijelaskan
- [ ] `ColumnTransformer` memisahkan numerik, nominal, dan ordinal
- [ ] **Ordinal disandikan dengan urutan yang ditentukan sendiri**
- [ ] `handle_unknown="ignore"` dipakai pada `OneHotEncoder`
- [ ] Seluruh transformasi berada **di dalam** `Pipeline`
- [ ] Tidak ada NaN tersisa setelah transformasi
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 3](../03-modules/week-03-data-dan-prapemrosesan.md)
2. [Bab 3 buku ajar](../06-buku-ajar/bab-03-data-dan-prapemrosesan.md)
3. Dokumentasi scikit-learn — *Preprocessing*. <https://scikit-learn.org/stable/modules/preprocessing.html>
4. Dokumentasi scikit-learn — *ColumnTransformer*. <https://scikit-learn.org/stable/modules/compose.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
