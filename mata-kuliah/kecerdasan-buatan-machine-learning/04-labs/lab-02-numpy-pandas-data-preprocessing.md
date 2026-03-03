# Lab 02: NumPy, Pandas, dan Data Preprocessing

**Mata Kuliah:** Kecerdasan Buatan dan Machine Learning
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Minggu:** 2
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

- Melakukan operasi dasar NumPy: pembuatan array, reshaping, dan broadcasting
- Menggunakan Pandas untuk membaca CSV, filtering, groupby, dan merge
- Mendeteksi dan menangani missing values dengan berbagai metode
- Melakukan encoding variabel kategorikal (LabelEncoder, OneHotEncoder, get_dummies)
- Menerapkan feature scaling (StandardScaler, MinMaxScaler)
- Membagi data menjadi training dan testing set

---

## Persiapan

1. Buka Google Colab dan buat notebook baru
2. Nama file: `Lab02_NamaAnda_NIM.ipynb`
3. Pastikan library numpy, pandas, dan scikit-learn sudah tersedia
4. Siapkan pemahaman dasar tentang tipe data Python (list, dictionary)

---

## Langkah-langkah

### Langkah 1: NumPy - Pembuatan Array, Reshaping, Broadcasting

```python
# =============================================
# LANGKAH 1: Operasi Dasar NumPy
# =============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 50)
print("OPERASI DASAR NUMPY")
print("=" * 50)

# --- Pembuatan Array ---
print("\n--- Pembuatan Array ---")
arr1 = np.array([1, 2, 3, 4, 5])            # Array 1D
arr2 = np.array([[1, 2, 3], [4, 5, 6]])     # Array 2D
arr_zeros = np.zeros((3, 4))                  # Matriks nol 3x4
arr_ones = np.ones((2, 3))                    # Matriks satu 2x3
arr_range = np.arange(0, 20, 2)              # Array dengan step
arr_linspace = np.linspace(0, 1, 5)          # 5 titik merata dari 0-1
arr_random = np.random.randn(3, 3)           # Matriks random normal

print(f"Array 1D       : {arr1}")
print(f"Array 2D       :\n{arr2}")
print(f"Zeros (3x4)    :\n{arr_zeros}")
print(f"Arange (0-20)  : {arr_range}")
print(f"Linspace (0-1) : {arr_linspace}")

# --- Reshaping ---
print("\n--- Reshaping ---")
arr_flat = np.arange(12)
print(f"Array asli (12,): {arr_flat}")

arr_3x4 = arr_flat.reshape(3, 4)
print(f"Reshape (3,4)  :\n{arr_3x4}")

arr_2x6 = arr_flat.reshape(2, 6)
print(f"Reshape (2,6)  :\n{arr_2x6}")

arr_auto = arr_flat.reshape(4, -1)  # -1 = otomatis hitung
print(f"Reshape (4,-1) :\n{arr_auto}")

# --- Broadcasting ---
print("\n--- Broadcasting ---")
matriks = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
skalar = 10
vektor_baris = np.array([100, 200, 300])

print(f"Matriks + Skalar:\n{matriks + skalar}")
print(f"\nMatriks + Vektor Baris:\n{matriks + vektor_baris}")
print(f"\nMatriks * 2:\n{matriks * 2}")
```

### Langkah 2: Pandas - Baca CSV, Filtering, Groupby, Merge

```python
# =============================================
# LANGKAH 2: Operasi Pandas
# =============================================

print("=" * 50)
print("OPERASI DASAR PANDAS")
print("=" * 50)

# --- Buat Dataset Simulasi E-Commerce Indonesia ---
np.random.seed(42)
n = 300

# Dataset transaksi e-commerce
data_transaksi = {
    'id_transaksi': range(1, n + 1),
    'kota': np.random.choice(
        ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Makassar', 'Semarang'],
        size=n, p=[0.30, 0.20, 0.15, 0.15, 0.10, 0.10]
    ),
    'kategori_produk': np.random.choice(
        ['Elektronik', 'Fashion', 'Makanan', 'Kesehatan', 'Buku'],
        size=n, p=[0.25, 0.30, 0.20, 0.15, 0.10]
    ),
    'harga_ribu': np.round(np.random.lognormal(mean=4.5, sigma=1.0, size=n), 0),
    'jumlah_item': np.random.choice([1, 2, 3, 4, 5], size=n, p=[0.40, 0.25, 0.20, 0.10, 0.05]),
    'metode_bayar': np.random.choice(
        ['Transfer Bank', 'E-Wallet', 'COD', 'Kartu Kredit'],
        size=n, p=[0.30, 0.35, 0.20, 0.15]
    ),
    'rating': np.random.choice([1, 2, 3, 4, 5], size=n, p=[0.05, 0.10, 0.25, 0.35, 0.25]),
}

df = pd.DataFrame(data_transaksi)
df['total_harga'] = df['harga_ribu'] * df['jumlah_item']

# Sengaja masukkan missing values
df.loc[np.random.choice(n, 15, replace=False), 'rating'] = np.nan
df.loc[np.random.choice(n, 10, replace=False), 'metode_bayar'] = np.nan

print(f"Dataset e-commerce: {df.shape[0]} baris x {df.shape[1]} kolom")
print(df.head())

# --- Filtering ---
print("\n--- Filtering ---")
# Transaksi di Jakarta dengan harga > 200 ribu
filter_jkt = df[(df['kota'] == 'Jakarta') & (df['harga_ribu'] > 200)]
print(f"Transaksi Jakarta (harga > 200rb): {len(filter_jkt)} baris")

# Transaksi Elektronik atau Fashion
filter_kategori = df[df['kategori_produk'].isin(['Elektronik', 'Fashion'])]
print(f"Transaksi Elektronik/Fashion: {len(filter_kategori)} baris")

# --- Groupby ---
print("\n--- Groupby: Rata-rata Total Harga per Kota ---")
grouped = df.groupby('kota')['total_harga'].agg(['count', 'mean', 'median', 'sum']).round(0)
grouped.columns = ['Jumlah', 'Mean', 'Median', 'Total']
print(grouped.sort_values('Mean', ascending=False))

# --- Merge ---
print("\n--- Merge (Gabung DataFrame) ---")
# Buat data tambahan: info kota
data_kota = pd.DataFrame({
    'kota': ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Makassar', 'Semarang'],
    'pulau': ['Jawa', 'Jawa', 'Jawa', 'Sumatera', 'Sulawesi', 'Jawa'],
    'populasi_juta': [10.6, 2.9, 2.5, 2.2, 1.5, 1.7]
})

df_merged = pd.merge(df, data_kota, on='kota', how='left')
print(f"Setelah merge: {df_merged.shape}")
print(df_merged[['kota', 'pulau', 'populasi_juta', 'total_harga']].head())
```

### Langkah 3: Deteksi dan Penanganan Missing Values

```python
# =============================================
# LANGKAH 3: Handle Missing Values
# =============================================

print("=" * 50)
print("DETEKSI DAN PENANGANAN MISSING VALUES")
print("=" * 50)

# --- Deteksi Missing Values ---
print("\n--- Deteksi Missing Values ---")
print("Jumlah missing per kolom:")
print(df.isnull().sum())
print(f"\nTotal missing: {df.isnull().sum().sum()}")
print(f"Persentase missing:")
print((df.isnull().sum() / len(df) * 100).round(2))

# Visualisasi missing values
plt.figure(figsize=(10, 4))
missing_pct = (df.isnull().sum() / len(df) * 100)
missing_pct[missing_pct > 0].plot(kind='bar', color='coral', edgecolor='white')
plt.title('Persentase Missing Values per Kolom', fontsize=13)
plt.ylabel('Persentase (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Penanganan Missing Values ---
df_clean = df.copy()

# fillna() - Isi dengan nilai tertentu
# Rating: isi dengan median
median_rating = df_clean['rating'].median()
df_clean['rating'] = df_clean['rating'].fillna(median_rating)
print(f"\nRating diisi dengan median: {median_rating}")

# Metode bayar: isi dengan modus (nilai terbanyak)
modus_bayar = df_clean['metode_bayar'].mode()[0]
df_clean['metode_bayar'] = df_clean['metode_bayar'].fillna(modus_bayar)
print(f"Metode bayar diisi dengan modus: {modus_bayar}")

# dropna() - Hapus baris dengan missing (demonstrasi)
df_dropped = df.dropna()
print(f"\nSebelum dropna: {len(df)} baris")
print(f"Setelah dropna: {len(df_dropped)} baris (kehilangan {len(df) - len(df_dropped)} baris)")

# Verifikasi
print(f"\nMissing values setelah penanganan:")
print(df_clean.isnull().sum())
```

### Langkah 4: SimpleImputer dari scikit-learn

```python
# =============================================
# LANGKAH 4: SimpleImputer dari sklearn
# =============================================

from sklearn.impute import SimpleImputer

print("=" * 50)
print("SIMPLEIMPUTER DARI SCIKIT-LEARN")
print("=" * 50)

# Buat ulang data dengan missing values untuk demonstrasi
df_demo = df.copy()

# --- Imputer untuk kolom numerik (strategy: mean) ---
imputer_mean = SimpleImputer(strategy='mean')
df_demo['rating_imputed_mean'] = imputer_mean.fit_transform(
    df_demo[['rating']]
)

# --- Imputer untuk kolom numerik (strategy: median) ---
imputer_median = SimpleImputer(strategy='median')
df_demo['rating_imputed_median'] = imputer_median.fit_transform(
    df_demo[['rating']]
)

# --- Imputer untuk kolom kategorikal (strategy: most_frequent) ---
imputer_freq = SimpleImputer(strategy='most_frequent')
df_demo['bayar_imputed'] = imputer_freq.fit_transform(
    df_demo[['metode_bayar']]
).ravel()

print("Perbandingan hasil imputation (baris dengan missing rating):")
missing_idx = df['rating'].isnull()
print(df_demo.loc[missing_idx, ['rating', 'rating_imputed_mean',
                                  'rating_imputed_median']].head(10))

print(f"\nMean rating   : {df['rating'].mean():.2f}")
print(f"Median rating : {df['rating'].median():.2f}")
print(f"\nSimpleImputer mempermudah imputation secara konsisten!")
```

### Langkah 5: Encoding Variabel Kategorikal

```python
# =============================================
# LANGKAH 5: Encoding Variabel Kategorikal
# =============================================

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

print("=" * 50)
print("ENCODING VARIABEL KATEGORIKAL")
print("=" * 50)

df_encode = df_clean.copy()

# --- 1. LabelEncoder (ordinal encoding) ---
print("\n--- LabelEncoder ---")
le_kota = LabelEncoder()
df_encode['kota_encoded'] = le_kota.fit_transform(df_encode['kota'])

print("Mapping kota -> angka:")
for kota, kode in zip(le_kota.classes_, range(len(le_kota.classes_))):
    print(f"  {kota} -> {kode}")

print(df_encode[['kota', 'kota_encoded']].drop_duplicates().sort_values('kota_encoded'))

# --- 2. OneHotEncoder (sklearn) ---
print("\n--- OneHotEncoder (sklearn) ---")
ohe = OneHotEncoder(sparse_output=False, drop='first')  # drop='first' untuk hindari multikolinearitas
kategori_encoded = ohe.fit_transform(df_encode[['kategori_produk']])

# Nama kolom hasil encoding
ohe_columns = ohe.get_feature_names_out(['kategori_produk'])
df_ohe = pd.DataFrame(kategori_encoded, columns=ohe_columns, index=df_encode.index)

print(f"Kolom hasil OneHotEncoder: {list(ohe_columns)}")
print(df_ohe.head())

# --- 3. pd.get_dummies (cara cepat Pandas) ---
print("\n--- pd.get_dummies (Pandas) ---")
df_dummies = pd.get_dummies(df_encode[['metode_bayar']], prefix='bayar', drop_first=True)
print(df_dummies.head())

print(f"\nPerbandingan metode encoding:")
print(f"  LabelEncoder  : 1 kolom (angka ordinal, cocok untuk tree-based model)")
print(f"  OneHotEncoder : {len(ohe_columns)} kolom (binary, cocok untuk linear model)")
print(f"  get_dummies   : {df_dummies.shape[1]} kolom (mirip OHE, langsung dari Pandas)")
```

### Langkah 6: Feature Scaling (StandardScaler, MinMaxScaler)

```python
# =============================================
# LANGKAH 6: Feature Scaling
# =============================================

from sklearn.preprocessing import StandardScaler, MinMaxScaler

print("=" * 50)
print("FEATURE SCALING")
print("=" * 50)

# Pilih kolom numerik untuk scaling
fitur_numerik = df_clean[['harga_ribu', 'jumlah_item', 'total_harga', 'rating']].copy()

print("--- Sebelum Scaling ---")
print(fitur_numerik.describe().round(2))

# --- StandardScaler (Z-Score: mean=0, std=1) ---
scaler_std = StandardScaler()
fitur_standard = pd.DataFrame(
    scaler_std.fit_transform(fitur_numerik),
    columns=[f'{col}_std' for col in fitur_numerik.columns]
)

print("\n--- Setelah StandardScaler ---")
print(fitur_standard.describe().round(4))

# --- MinMaxScaler (Skala 0-1) ---
scaler_mm = MinMaxScaler()
fitur_minmax = pd.DataFrame(
    scaler_mm.fit_transform(fitur_numerik),
    columns=[f'{col}_mm' for col in fitur_numerik.columns]
)

print("\n--- Setelah MinMaxScaler ---")
print(fitur_minmax.describe().round(4))

# Visualisasi perbandingan
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Kolom yang divisualisasi
col = 'harga_ribu'

axes[0].hist(fitur_numerik[col], bins=30, color='steelblue', edgecolor='white')
axes[0].set_title(f'Asli: {col}', fontsize=12)
axes[0].set_xlabel('Nilai')

axes[1].hist(fitur_standard[f'{col}_std'], bins=30, color='coral', edgecolor='white')
axes[1].set_title(f'StandardScaler: {col}', fontsize=12)
axes[1].set_xlabel('Nilai (z-score)')

axes[2].hist(fitur_minmax[f'{col}_mm'], bins=30, color='green', edgecolor='white')
axes[2].set_title(f'MinMaxScaler: {col}', fontsize=12)
axes[2].set_xlabel('Nilai (0-1)')

plt.suptitle('Perbandingan Metode Scaling', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Langkah 7: Train-Test Split

```python
# =============================================
# LANGKAH 7: Train-Test Split
# =============================================

from sklearn.model_selection import train_test_split

print("=" * 50)
print("TRAIN-TEST SPLIT")
print("=" * 50)

# Siapkan fitur (X) dan target (y)
# Contoh: prediksi apakah rating >= 4 (pelanggan puas)
df_final = df_clean.copy()
df_final['puas'] = (df_final['rating'] >= 4).astype(int)

# Pilih fitur numerik yang sudah di-encode
X = df_final[['harga_ribu', 'jumlah_item', 'total_harga']].values
y = df_final['puas'].values

print(f"Dimensi fitur X: {X.shape}")
print(f"Dimensi target y: {y.shape}")
print(f"Distribusi target: {np.bincount(y)}")

# --- Split data: 80% train, 20% test ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% untuk testing
    random_state=42,     # Reproducibility
    stratify=y           # Jaga proporsi kelas
)

print(f"\n--- Hasil Split ---")
print(f"Training set: {X_train.shape[0]} sampel ({X_train.shape[0]/len(X)*100:.0f}%)")
print(f"Testing set : {X_test.shape[0]} sampel ({X_test.shape[0]/len(X)*100:.0f}%)")

# Verifikasi proporsi kelas terjaga
print(f"\nProporsi kelas di training:")
print(f"  Tidak puas (0): {np.sum(y_train == 0)} ({np.sum(y_train == 0)/len(y_train)*100:.1f}%)")
print(f"  Puas (1)      : {np.sum(y_train == 1)} ({np.sum(y_train == 1)/len(y_train)*100:.1f}%)")

print(f"\nProporsi kelas di testing:")
print(f"  Tidak puas (0): {np.sum(y_test == 0)} ({np.sum(y_test == 0)/len(y_test)*100:.1f}%)")
print(f"  Puas (1)      : {np.sum(y_test == 1)} ({np.sum(y_test == 1)/len(y_test)*100:.1f}%)")

# --- Scaling setelah split (PENTING!) ---
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # fit pada training saja
X_test_scaled = scaler.transform(X_test)          # transform pada testing

print(f"\n--- Setelah Scaling ---")
print(f"Mean X_train (setelah scaling): {X_train_scaled.mean(axis=0).round(4)}")
print(f"Std  X_train (setelah scaling): {X_train_scaled.std(axis=0).round(4)}")

print(f"""
PENTING: Urutan yang benar adalah:
1. Split data DULU → train_test_split()
2. Fit scaler pada X_train → scaler.fit_transform(X_train)
3. Transform X_test → scaler.transform(X_test)

JANGAN fit scaler pada seluruh data (data leakage)!
""")
```

---

## Tantangan Tambahan

1. **Pipeline Preprocessing Lengkap:** Gabungkan semua langkah preprocessing (handle missing, encoding, scaling, split) menjadi satu pipeline menggunakan `sklearn.pipeline.Pipeline` dan `ColumnTransformer`. Jalankan pipeline pada dataset e-commerce di atas.

2. **Dataset BPS:** Buat dataset simulasi data BPS tentang Indeks Pembangunan Manusia (IPM) per provinsi. Terapkan semua teknik preprocessing yang telah dipelajari (handle missing, encoding provinsi, scaling indikator numerik).

3. **Visualisasi Perbandingan Encoding:** Buat visualisasi yang membandingkan hasil LabelEncoder vs OneHotEncoder pada kolom `kota` menggunakan scatter plot. Diskusikan kapan masing-masing metode lebih sesuai.

---

## Checklist Penyelesaian

- [ ] Operasi NumPy (array, reshaping, broadcasting) berhasil dijalankan
- [ ] Dataset e-commerce berhasil dibuat dan dieksplorasi
- [ ] Filtering dan groupby berhasil dilakukan
- [ ] Merge dua DataFrame berhasil dilakukan
- [ ] Missing values terdeteksi dan ditangani (fillna, dropna, SimpleImputer)
- [ ] Encoding kategorikal berhasil (LabelEncoder, OneHotEncoder, get_dummies)
- [ ] Feature scaling berhasil (StandardScaler, MinMaxScaler)
- [ ] Train-test split dilakukan dengan benar (stratify, scaling setelah split)
- [ ] Notebook disimpan dengan nama `Lab02_NamaAnda_NIM.ipynb`
- [ ] Minimal 1 tantangan tambahan diselesaikan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
