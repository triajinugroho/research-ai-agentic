# Minggu 2: Python untuk AI/ML — Data Preprocessing

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 2 |
| **Topik** | Python untuk AI/ML — Data Preprocessing |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK-2: Menerapkan teknik preprocessing data untuk mempersiapkan dataset bagi model machine learning |
| **Sub-CPMK** | 2.1 Menerapkan operasi NumPy dan Pandas untuk manipulasi data |
| | 2.2 Mengimplementasikan pipeline preprocessing data lengkap (missing values, encoding, scaling, splitting) |
| **Bloom's Taxonomy** | C3 (Menerapkan / *Applying*) |
| **Durasi** | 2 x 100 menit (Teori 100 min + Praktikum 100 min) |
| **Platform** | Google Colab |
| **Metode** | Ceramah interaktif, live coding, hands-on praktikum |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menerapkan** operasi dasar NumPy (array creation, broadcasting, operasi matematika) untuk komputasi numerik.
2. **Menggunakan** Pandas DataFrame dan Series untuk manipulasi, filtering, dan agregasi data tabular.
3. **Mengimplementasikan** teknik preprocessing data: handling missing values, encoding variabel kategorikal, dan feature scaling.
4. **Menerapkan** konsep train-test split untuk mempersiapkan data bagi model machine learning.

---

## Materi Pembelajaran

### 1. NumPy Essentials untuk AI/ML

#### Mengapa NumPy Penting untuk ML?

**NumPy** (*Numerical Python*) adalah fondasi dari hampir semua library machine learning di Python. Scikit-learn, TensorFlow, dan PyTorch semuanya menggunakan NumPy arrays sebagai struktur data dasar.

Keunggulan NumPy dibanding Python list:
- **Kecepatan** — operasi vektor/matriks jauh lebih cepat (hingga 100x)
- **Efisiensi memori** — tipe data homogen, memori terstruktur
- **Broadcasting** — operasi otomatis pada array dengan dimensi berbeda
- **Ekosistem** — kompatibel dengan semua library ML

#### Array Creation (Pembuatan Array)

```python
import numpy as np

# 1D array (vektor)
vektor = np.array([1, 2, 3, 4, 5])
print(f"Vektor: {vektor}")
print(f"Shape: {vektor.shape}")  # (5,)

# 2D array (matriks)
matriks = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
print(f"\nMatriks:\n{matriks}")
print(f"Shape: {matriks.shape}")  # (3, 3)

# Array khusus
zeros = np.zeros((3, 4))       # Matriks nol 3x4
ones = np.ones((2, 3))         # Matriks satu 2x3
identity = np.eye(3)           # Matriks identitas 3x3
linspace = np.linspace(0, 1, 5) # 5 angka merata dari 0 ke 1
arange = np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]

print(f"\nZeros:\n{zeros}")
print(f"\nIdentity:\n{identity}")
print(f"\nLinspace: {linspace}")
```

#### Operasi Array dan Broadcasting

```python
# Operasi element-wise
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(f"a + b = {a + b}")      # [11, 22, 33, 44]
print(f"a * b = {a * b}")      # [10, 40, 90, 160]
print(f"a ** 2 = {a ** 2}")    # [1, 4, 9, 16]

# Broadcasting: operasi skalar dengan array
print(f"a * 3 = {a * 3}")      # [3, 6, 9, 12]
print(f"a + 100 = {a + 100}")  # [101, 102, 103, 104]

# Fungsi statistik
data = np.array([85, 90, 78, 92, 88, 76, 95, 82])
print(f"\nNilai ujian: {data}")
print(f"Mean    : {np.mean(data):.2f}")
print(f"Median  : {np.median(data):.2f}")
print(f"Std Dev : {np.std(data):.2f}")
print(f"Min/Max : {np.min(data)} / {np.max(data)}")
```

#### Random Number Generation

```python
# Random numbers (penting untuk ML: initialization, sampling)
np.random.seed(42)  # Reproducibility!

# Distribusi uniform [0, 1)
uniform = np.random.rand(5)
print(f"Uniform: {uniform}")

# Distribusi normal (mean=0, std=1)
normal = np.random.randn(5)
print(f"Normal: {normal}")

# Random integer
rand_int = np.random.randint(1, 100, size=10)
print(f"Random int: {rand_int}")

# Mengapa seed penting?
# Dalam ML, kita ingin hasil yang reproducible
# Seed yang sama = hasil random yang sama
```

---

### 2. Pandas Essentials untuk Data Science

#### DataFrame dan Series

**Pandas** adalah library utama untuk manipulasi data tabular. Dua struktur data utamanya:

- **Series** — array 1D berlabel (seperti satu kolom)
- **DataFrame** — tabel 2D berlabel (seperti spreadsheet)

```python
import pandas as pd

# Membuat DataFrame dari dictionary
data = {
    'nama': ['Ahmad', 'Budi', 'Citra', 'Dewi', 'Eko',
             'Fitri', 'Gunawan', 'Hana', 'Irfan', 'Joko'],
    'kota': ['Jakarta', 'Bandung', 'Surabaya', 'Jakarta', 'Yogyakarta',
             'Bandung', 'Jakarta', 'Surabaya', 'Semarang', 'Jakarta'],
    'usia': [22, 25, 23, 28, 21, 24, 27, 22, 26, 30],
    'gaji_juta': [5.5, 8.0, 6.5, 12.0, 4.5, 7.5, 10.0, 5.0, 9.0, 15.0],
    'pendidikan': ['S1', 'S2', 'S1', 'S2', 'S1', 'S1', 'S2', 'S1', 'S2', 'S2']
}
df = pd.DataFrame(data)
print(df)
```

#### Indexing dan Filtering

```python
# Akses kolom
print("=== Kolom 'nama' ===")
print(df['nama'])

# Akses baris (loc = label-based, iloc = index-based)
print("\n=== Baris pertama (iloc) ===")
print(df.iloc[0])

print("\n=== Baris 2-4 (iloc) ===")
print(df.iloc[1:4])

# Filtering berdasarkan kondisi
print("\n=== Karyawan di Jakarta ===")
print(df[df['kota'] == 'Jakarta'])

print("\n=== Karyawan dengan gaji > 8 juta ===")
print(df[df['gaji_juta'] > 8])

# Multiple conditions
print("\n=== Karyawan di Jakarta dengan S2 ===")
print(df[(df['kota'] == 'Jakarta') & (df['pendidikan'] == 'S2')])
```

#### GroupBy dan Agregasi

```python
# GroupBy: operasi split-apply-combine
print("=== Rata-rata gaji per kota ===")
print(df.groupby('kota')['gaji_juta'].mean().sort_values(ascending=False))

print("\n=== Statistik gaji per pendidikan ===")
print(df.groupby('pendidikan')['gaji_juta'].agg(['mean', 'min', 'max', 'count']))

print("\n=== Jumlah karyawan per kota ===")
print(df['kota'].value_counts())
```

---

### 3. Data Preprocessing Pipeline

Preprocessing data adalah tahap **paling penting** dalam ML pipeline. Model machine learning sangat sensitif terhadap kualitas data. Prinsip terkenal dalam ML:

> **"Garbage In, Garbage Out"** — Model ML hanya sebagus data yang digunakan untuk melatihnya.

#### Pipeline Preprocessing

```
Data Mentah → Handling Missing Values → Encoding Kategorik → Feature Scaling → Train-Test Split → Siap untuk ML
```

#### a) Handling Missing Values (Penanganan Nilai Hilang)

Nilai hilang (*missing values*) adalah masalah umum dalam dataset nyata. Penyebabnya bisa karena:
- Data tidak tersedia saat pengumpulan
- Error pada sensor atau sistem
- Responden tidak menjawab pertanyaan survei

```python
# Membuat dataset dengan missing values
data_mv = {
    'nama': ['Ahmad', 'Budi', 'Citra', 'Dewi', 'Eko',
             'Fitri', 'Gunawan', 'Hana', None, 'Joko'],
    'usia': [22, None, 23, 28, 21, 24, None, 22, 26, 30],
    'gaji_juta': [5.5, 8.0, None, 12.0, 4.5, None, 10.0, 5.0, 9.0, None],
    'kota': ['Jakarta', 'Bandung', 'Surabaya', None, 'Yogyakarta',
             'Bandung', 'Jakarta', None, 'Semarang', 'Jakarta']
}
df_mv = pd.DataFrame(data_mv)

# Cek missing values
print("=== Cek Missing Values ===")
print(df_mv.isnull().sum())
print(f"\nTotal missing: {df_mv.isnull().sum().sum()}")
print(f"Persentase missing: {df_mv.isnull().sum().sum() / df_mv.size * 100:.1f}%")
```

```python
# Strategi 1: Hapus baris dengan missing values (dropna)
df_dropped = df_mv.dropna()
print(f"Sebelum dropna: {len(df_mv)} baris")
print(f"Setelah dropna: {len(df_dropped)} baris")
# Catatan: Hati-hati! Ini bisa menghilangkan banyak data.

# Strategi 2: Isi dengan nilai tertentu (fillna)
df_filled = df_mv.copy()
df_filled['usia'] = df_filled['usia'].fillna(df_filled['usia'].median())
df_filled['gaji_juta'] = df_filled['gaji_juta'].fillna(df_filled['gaji_juta'].mean())
df_filled['kota'] = df_filled['kota'].fillna(df_filled['kota'].mode()[0])
print("\nSetelah fillna:")
print(df_filled.isnull().sum())
```

```python
# Strategi 3: Menggunakan SimpleImputer dari scikit-learn
from sklearn.impute import SimpleImputer

# Imputer untuk kolom numerik (isi dengan median)
imputer_num = SimpleImputer(strategy='median')
df_imputed = df_mv.copy()
df_imputed[['usia', 'gaji_juta']] = imputer_num.fit_transform(
    df_mv[['usia', 'gaji_juta']]
)

# Imputer untuk kolom kategorikal (isi dengan modus)
imputer_cat = SimpleImputer(strategy='most_frequent')
df_imputed[['kota']] = imputer_cat.fit_transform(df_mv[['kota']])

print("=== Setelah SimpleImputer ===")
print(df_imputed)
print(f"\nMissing values: {df_imputed.isnull().sum().sum()}")
```

#### Kapan Menggunakan Strategi Mana?

| Strategi | Kapan Digunakan | Risiko |
|---|---|---|
| **dropna** | Missing < 5%, data cukup banyak | Kehilangan informasi |
| **fillna (mean/median)** | Kolom numerik, distribusi normal/skewed | Mengurangi variance |
| **fillna (mode)** | Kolom kategorikal | Over-represent satu kategori |
| **SimpleImputer** | Pipeline ML, preprocessing otomatis | Sama seperti fillna tapi lebih modular |
| **KNN Imputer** | Data saling berkorelasi | Lambat untuk dataset besar |

#### b) Encoding Categorical Variables (Encoding Variabel Kategorikal)

Model machine learning umumnya membutuhkan input berupa angka (*numeric*). Variabel kategorikal harus dikonversi:

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Contoh data
kota = ['Jakarta', 'Bandung', 'Surabaya', 'Jakarta', 'Bandung']
pendidikan = ['S1', 'S2', 'S1', 'S2', 'S1']

# ---- Label Encoding ----
# Mengubah kategori menjadi angka (0, 1, 2, ...)
le = LabelEncoder()
kota_encoded = le.fit_transform(kota)
print(f"Kota asli     : {kota}")
print(f"Label Encoded : {kota_encoded}")
print(f"Mapping       : {dict(zip(le.classes_, le.transform(le.classes_)))}")

# Catatan: Label Encoding cocok untuk data ordinal (ada urutan)
# Untuk data nominal, gunakan One-Hot Encoding
```

```python
# ---- One-Hot Encoding ----
# Mengubah setiap kategori menjadi kolom biner (0/1)
import pandas as pd

df_encoding = pd.DataFrame({'kota': kota, 'pendidikan': pendidikan})
print("=== Data Asli ===")
print(df_encoding)

# Menggunakan pd.get_dummies (cara termudah)
df_onehot = pd.get_dummies(df_encoding, columns=['kota'], prefix='kota')
print("\n=== Setelah One-Hot Encoding ===")
print(df_onehot)

# Catatan: One-Hot Encoding cocok untuk data nominal (tidak ada urutan)
# Hati-hati dengan "curse of dimensionality" jika terlalu banyak kategori
```

| Metode | Cocok Untuk | Contoh |
|---|---|---|
| **Label Encoding** | Data ordinal (ada urutan) | Pendidikan: SD=0, SMP=1, SMA=2, S1=3, S2=4 |
| **One-Hot Encoding** | Data nominal (tidak ada urutan) | Kota: Jakarta=[1,0,0], Bandung=[0,1,0] |
| **Ordinal Encoding** | Data ordinal dengan mapping kustom | Kepuasan: Rendah=1, Sedang=2, Tinggi=3 |

#### c) Feature Scaling (Penskalaan Fitur)

Banyak algoritma ML sensitif terhadap skala fitur. Fitur dengan rentang nilai besar (misalnya gaji: jutaan) akan mendominasi fitur dengan rentang kecil (misalnya usia: puluhan).

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Data contoh
data_scale = pd.DataFrame({
    'usia': [22, 25, 23, 28, 21, 24, 27, 22, 26, 30],
    'gaji_juta': [5.5, 8.0, 6.5, 12.0, 4.5, 7.5, 10.0, 5.0, 9.0, 15.0]
})

print("=== Data Asli ===")
print(data_scale.describe())
```

```python
# ---- StandardScaler (Z-score normalization) ----
# Mengubah data sehingga mean=0 dan std=1
# Formula: z = (x - mean) / std
scaler_std = StandardScaler()
data_standard = scaler_std.fit_transform(data_scale)
df_standard = pd.DataFrame(data_standard, columns=['usia_std', 'gaji_std'])

print("\n=== Setelah StandardScaler ===")
print(df_standard.describe())

# ---- MinMaxScaler ----
# Mengubah data ke rentang [0, 1]
# Formula: x_scaled = (x - min) / (max - min)
scaler_mm = MinMaxScaler()
data_minmax = scaler_mm.fit_transform(data_scale)
df_minmax = pd.DataFrame(data_minmax, columns=['usia_mm', 'gaji_mm'])

print("\n=== Setelah MinMaxScaler ===")
print(df_minmax.describe())
```

| Metode | Formula | Rentang Hasil | Cocok Untuk |
|---|---|---|---|
| **StandardScaler** | (x - mean) / std | Sekitar -3 sampai +3 | SVM, Logistic Regression, Neural Networks |
| **MinMaxScaler** | (x - min) / (max - min) | [0, 1] | KNN, Neural Networks, jika ingin rentang pasti |

---

### 4. Train-Test Split

Salah satu konsep terpenting dalam ML: **jangan mengevaluasi model pada data yang sama yang digunakan untuk melatihnya**.

```
┌──────────────────────────────────────────────────────────┐
│                    Dataset Lengkap                        │
│                                                          │
│  ┌──────────────────────────────┐ ┌────────────────────┐ │
│  │     Training Set (80%)       │ │  Test Set (20%)    │ │
│  │  Digunakan untuk melatih     │ │ Digunakan untuk    │ │
│  │  model                       │ │ mengevaluasi model │ │
│  └──────────────────────────────┘ └────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

```python
from sklearn.model_selection import train_test_split

# Contoh dengan Iris dataset
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data    # Features
y = iris.target  # Target

# Split: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,       # 20% untuk testing
    random_state=42,     # Reproducibility
    stratify=y           # Proporsi kelas sama di train dan test
)

print("=== Train-Test Split ===")
print(f"Total sampel  : {len(X)}")
print(f"Training set  : {len(X_train)} ({len(X_train)/len(X)*100:.0f}%)")
print(f"Test set      : {len(X_test)} ({len(X_test)/len(X)*100:.0f}%)")

# Verifikasi stratifikasi
import numpy as np
print(f"\nDistribusi kelas (train): {np.bincount(y_train)}")
print(f"Distribusi kelas (test) : {np.bincount(y_test)}")
```

> **Penting:** Parameter `random_state` memastikan split yang sama setiap kali kode dijalankan. Ini penting untuk **reproducibility** — orang lain bisa mendapatkan hasil yang sama.

---

## Aktivitas Kelas

### Sesi 1: Teori dan Live Coding (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 5 menit | Pembukaan & Review | Review singkat materi Minggu 1 |
| 20 menit | Ceramah: NumPy Essentials | Array creation, operasi, broadcasting, random |
| 20 menit | Ceramah: Pandas Essentials | DataFrame, Series, indexing, filtering, groupby |
| 20 menit | Ceramah: Preprocessing | Missing values, encoding, scaling |
| 15 menit | Live Coding Demo | Demonstrasi preprocessing pipeline step-by-step |
| 15 menit | Ceramah: Train-Test Split | Konsep, implementasi, pentingnya stratify |
| 5 menit | Transisi ke Praktikum | Persiapan hands-on |

### Sesi 2: Hands-on Praktikum (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Setup Notebook | Buka Google Colab, import library |
| 25 menit | NumPy & Pandas Practice | Latihan operasi array, DataFrame manipulation |
| 30 menit | Preprocessing Pipeline | Implementasi full pipeline pada dataset Indonesia |
| 20 menit | Eksplorasi Mandiri | Mahasiswa mencoba variasi preprocessing |
| 10 menit | Diskusi Hasil & Wrap-up | Sharing hasil, Q&A |
| 5 menit | Tugas & Penutup | Penjelasan Tugas T1 |

---

## Hands-on: Full Preprocessing Pipeline pada Dataset Indonesia

### Dataset: Data Karyawan Indonesia (Simulasi)

```python
# ============================================================
# Minggu 2: Data Preprocessing Pipeline
# Mata Kuliah: Kecerdasan Buatan dan Machine Learning
# Universitas Al Azhar Indonesia
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Membuat dataset simulasi: Data Karyawan Perusahaan di Indonesia
np.random.seed(42)
n = 100

data_karyawan = {
    'nama': [f'Karyawan_{i+1}' for i in range(n)],
    'usia': np.random.randint(21, 55, size=n).astype(float),
    'jenis_kelamin': np.random.choice(['Laki-laki', 'Perempuan'], size=n),
    'pendidikan': np.random.choice(['SMA', 'D3', 'S1', 'S2'], size=n,
                                    p=[0.15, 0.20, 0.45, 0.20]),
    'departemen': np.random.choice(['IT', 'Marketing', 'Finance', 'HR', 'Operasional'],
                                    size=n),
    'pengalaman_tahun': np.random.randint(0, 25, size=n).astype(float),
    'gaji_juta': np.round(np.random.uniform(4, 25, size=n), 1),
    'kota': np.random.choice(['Jakarta', 'Bandung', 'Surabaya', 'Yogyakarta',
                               'Semarang', 'Medan'], size=n),
    'kepuasan_kerja': np.random.choice(['Rendah', 'Sedang', 'Tinggi'], size=n,
                                        p=[0.2, 0.5, 0.3])
}

df = pd.DataFrame(data_karyawan)

# Sisipkan missing values secara random (simulasi data nyata)
for col in ['usia', 'pengalaman_tahun', 'gaji_juta']:
    idx = np.random.choice(n, size=int(n * 0.08), replace=False)
    df.loc[idx, col] = np.nan

for col in ['pendidikan', 'departemen']:
    idx = np.random.choice(n, size=int(n * 0.05), replace=False)
    df.loc[idx, col] = np.nan

print("=== Dataset Karyawan Indonesia ===")
print(f"Shape: {df.shape}")
print(df.head(10))
```

### Pipeline Step 1: Analisis Missing Values

```python
# Analisis missing values
print("=== Missing Values Analysis ===")
missing = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df) * 100).round(1)
missing_report = pd.DataFrame({
    'Jumlah Missing': missing,
    'Persentase (%)': missing_pct
})
print(missing_report[missing_report['Jumlah Missing'] > 0])
print(f"\nTotal missing values: {df.isnull().sum().sum()}")
```

### Pipeline Step 2: Handle Missing Values

```python
from sklearn.impute import SimpleImputer

# Pisahkan kolom numerik dan kategorikal
kolom_numerik = ['usia', 'pengalaman_tahun', 'gaji_juta']
kolom_kategorikal = ['pendidikan', 'departemen']

# Impute kolom numerik dengan median
imputer_num = SimpleImputer(strategy='median')
df[kolom_numerik] = imputer_num.fit_transform(df[kolom_numerik])

# Impute kolom kategorikal dengan modus
imputer_cat = SimpleImputer(strategy='most_frequent')
df[kolom_kategorikal] = imputer_cat.fit_transform(df[kolom_kategorikal])

print("=== Setelah Handling Missing Values ===")
print(f"Total missing: {df.isnull().sum().sum()}")
print("Semua missing values telah ditangani!")
```

### Pipeline Step 3: Encoding Categorical Variables

```python
from sklearn.preprocessing import LabelEncoder

# Label Encoding untuk variabel ordinal
# Pendidikan memiliki urutan: SMA < D3 < S1 < S2
mapping_pendidikan = {'SMA': 0, 'D3': 1, 'S1': 2, 'S2': 3}
df['pendidikan_encoded'] = df['pendidikan'].map(mapping_pendidikan)

# Kepuasan kerja juga ordinal: Rendah < Sedang < Tinggi
mapping_kepuasan = {'Rendah': 0, 'Sedang': 1, 'Tinggi': 2}
df['kepuasan_encoded'] = df['kepuasan_kerja'].map(mapping_kepuasan)

# Label Encoding untuk jenis kelamin
le_gender = LabelEncoder()
df['gender_encoded'] = le_gender.fit_transform(df['jenis_kelamin'])
print(f"Gender mapping: {dict(zip(le_gender.classes_, le_gender.transform(le_gender.classes_)))}")

# One-Hot Encoding untuk variabel nominal (departemen, kota)
df_encoded = pd.get_dummies(df, columns=['departemen', 'kota'],
                             prefix=['dept', 'kota'], drop_first=True)

print(f"\n=== Setelah Encoding ===")
print(f"Kolom baru: {df_encoded.shape[1]} (dari {df.shape[1]} kolom)")
print(f"Kolom: {list(df_encoded.columns)}")
```

### Pipeline Step 4: Feature Scaling

```python
from sklearn.preprocessing import StandardScaler

# Pilih fitur numerik untuk scaling
fitur_numerik = ['usia', 'pengalaman_tahun', 'gaji_juta',
                 'pendidikan_encoded', 'kepuasan_encoded']

scaler = StandardScaler()
df_encoded[fitur_numerik] = scaler.fit_transform(df_encoded[fitur_numerik])

print("=== Setelah StandardScaler ===")
print(df_encoded[fitur_numerik].describe().round(2))
print("\nMean mendekati 0, Std mendekati 1 -> Scaling berhasil!")
```

### Pipeline Step 5: Train-Test Split

```python
from sklearn.model_selection import train_test_split

# Definisikan features (X) dan target (y)
# Target: kepuasan_encoded (prediksi kepuasan kerja)
kolom_fitur = [col for col in df_encoded.columns
               if col not in ['nama', 'jenis_kelamin', 'pendidikan',
                               'kepuasan_kerja', 'kepuasan_encoded']]

X = df_encoded[kolom_fitur].values
y = df_encoded['kepuasan_encoded'].values

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("=== Hasil Train-Test Split ===")
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape : {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape : {y_test.shape}")
print(f"\nDistribusi kelas (train): {np.bincount(y_train.astype(int))}")
print(f"Distribusi kelas (test) : {np.bincount(y_test.astype(int))}")
print("\nData siap untuk training model ML!")
```

### Ringkasan Pipeline

```python
# Ringkasan seluruh pipeline
print("=" * 60)
print("RINGKASAN DATA PREPROCESSING PIPELINE")
print("=" * 60)
print(f"1. Dataset awal         : {n} baris, data karyawan Indonesia")
print(f"2. Missing values       : Ditangani dengan SimpleImputer")
print(f"3. Encoding             : Ordinal + One-Hot Encoding")
print(f"4. Scaling              : StandardScaler pada fitur numerik")
print(f"5. Train-Test Split     : 80/20 dengan stratifikasi")
print(f"6. Fitur final          : {X_train.shape[1]} kolom")
print(f"7. Data training        : {X_train.shape[0]} sampel")
print(f"8. Data testing         : {X_test.shape[0]} sampel")
print("=" * 60)
print("Pipeline SELESAI! Data siap untuk model ML.")
```

---

## AI Corner: Menggunakan AI untuk Debugging Preprocessing Code

> **Level: Basic** — Mulai menggunakan AI sebagai partner debugging dan learning.

### Cara AI Bisa Membantu Preprocessing

| Skenario | Contoh Prompt ke AI |
|---|---|
| Error saat preprocessing | *"Kode ini error 'ValueError: could not convert string to float'. Bagaimana cara memperbaikinya? [paste kode]"* |
| Memilih strategi imputation | *"Dataset saya punya 15% missing values di kolom numerik. Kapan sebaiknya pakai mean vs median vs KNN imputer?"* |
| Memahami encoding | *"Jelaskan perbedaan Label Encoding dan One-Hot Encoding. Kapan menggunakan masing-masing?"* |
| Memilih scaler | *"Kapan menggunakan StandardScaler vs MinMaxScaler? Dataset saya punya outlier."* |

### Tips Penting

1. **Selalu sertakan error message lengkap** ketika meminta bantuan debugging.
2. **Verifikasi saran AI** — jalankan kode dan cek hasilnya.
3. **Pahami "mengapa"** — jangan hanya tahu kodenya, tapi pahami alasan di balik setiap langkah.
4. **Dokumentasikan** penggunaan AI di AI Usage Log.

### Contoh Prompt Minggu Ini

```
Saya sedang belajar data preprocessing untuk ML.
Dataset saya tentang karyawan Indonesia memiliki:
- Missing values di kolom usia (8%), gaji (8%), pendidikan (5%)
- Kolom kategorikal: jenis_kelamin, pendidikan, departemen, kota
- Kolom numerik: usia, pengalaman_tahun, gaji_juta

Buatkan step-by-step preprocessing pipeline yang optimal.
Jelaskan alasan untuk setiap keputusan yang diambil.
```

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai bahan refleksi:

1. **Missing Values di Dunia Nyata:** Bayangkan Anda bekerja dengan data pasien rumah sakit di Indonesia. Kolom "tekanan darah" memiliki 20% missing values. Strategi apa yang akan Anda gunakan dan mengapa? Apa risiko dari setiap pendekatan?

2. **Encoding Strategy:** Sebuah dataset e-commerce memiliki kolom "provinsi" dengan 34 kategori (seluruh provinsi di Indonesia). Apakah Anda akan menggunakan One-Hot Encoding? Apa masalah yang mungkin muncul?

3. **Scaling Importance:** Mengapa feature scaling penting? Berikan contoh kasus di mana TIDAK melakukan scaling bisa menyebabkan model ML memberikan hasil yang buruk.

4. **Preprocessing dan Etika:** Bagaimana keputusan preprocessing (misalnya menghapus baris dengan missing values) bisa menyebabkan bias? Kaitkan dengan prinsip keadilan (*Al-'Adl*) dalam Islam.

5. **Pipeline Automation:** Mengapa penting untuk menggunakan pipeline yang terstruktur (bukan preprocessing manual) dalam proyek ML?

---

## Tugas Mandiri Minggu 2 — Tugas T1: Data Preprocessing Pipeline

### Deskripsi Tugas

Bangun sebuah **preprocessing pipeline lengkap** pada dataset yang disediakan.

### Instruksi

1. **Load dataset** dari URL berikut (atau gunakan dataset Indonesia lain yang disetujui dosen):

```python
# Contoh: Load dataset dari URL
# Atau buat dataset simulasi tentang konteks Indonesia
# Minimal 100 baris dan 8 kolom (campuran numerik dan kategorikal)
```

2. **Analisis data:** Gunakan `.info()`, `.describe()`, `.isnull().sum()` untuk memahami dataset.

3. **Handle missing values:** Pilih strategi yang tepat untuk setiap kolom, dan **jelaskan alasannya**.

4. **Encode variabel kategorikal:** Gunakan Label Encoding untuk data ordinal dan One-Hot Encoding untuk data nominal.

5. **Scale fitur numerik:** Gunakan StandardScaler atau MinMaxScaler, dan **jelaskan pilihan Anda**.

6. **Train-test split:** Bagi data menjadi 80% training dan 20% testing.

7. **Dokumentasi:** Tulis narasi singkat yang menjelaskan setiap keputusan preprocessing.

### Kriteria Penilaian

| Kriteria | Bobot |
|---|---|
| Kelengkapan pipeline (semua langkah ada) | 30% |
| Kualitas kode (bersih, berkomentar) | 20% |
| Pemilihan strategi yang tepat dan penjelasan | 30% |
| Dokumentasi dan narasi | 20% |

### Pengumpulan

- Format: Google Colab notebook (.ipynb) melalui LMS
- Deadline: Satu hari sebelum pertemuan Minggu 3
- **Wajib:** Sertakan AI Usage Log jika menggunakan AI

---

## Referensi

### Buku Teks

1. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media. Chapter 2: End-to-End Machine Learning Project.
2. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
3. Raschka, S., & Mirjalili, V. (2022). *Machine Learning with PyTorch and Scikit-Learn*. Packt Publishing. Chapter 4: Data Preprocessing.

### Sumber Online

4. [scikit-learn Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html) — Dokumentasi resmi preprocessing.
5. [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html) — Panduan lengkap pandas.
6. [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html) — Tutorial cepat NumPy.

### Referensi Tambahan

7. Zheng, A., & Casari, A. (2018). *Feature Engineering for Machine Learning*. O'Reilly Media.

---

> **Preview Minggu Depan:** Kita akan membahas **Matematika untuk Machine Learning** — aljabar linear (vektor, matriks), probabilitas, dan intuisi gradient descent. Persiapkan diri dengan review materi matematika dasar!

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
