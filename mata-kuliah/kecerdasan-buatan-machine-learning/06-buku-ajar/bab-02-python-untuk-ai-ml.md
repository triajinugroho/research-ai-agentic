# BAB 2: PYTHON UNTUK AI DAN MACHINE LEARNING

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-2.1 | Menerapkan library NumPy dan Pandas untuk manipulasi data dalam konteks machine learning | C3 |
| CPMK-2.2 | Mengimplementasikan tahapan preprocessing data menggunakan scikit-learn | C3 |

---

## Estimasi Waktu

| Aktivitas | Durasi |
|-----------|--------|
| Membaca materi | 90 menit |
| Praktik kode Python | 120 menit |
| Mengerjakan latihan soal | 60 menit |
| Eksplorasi AI Corner | 30 menit |
| **Total** | **5 jam** |

---

## Prasyarat

- Bab 1: Pengantar Kecerdasan Buatan
- Pemahaman dasar pemrograman Python (variabel, fungsi, loop, list)
- Akun Google untuk mengakses Google Colab

---

## 2.1 Ekosistem Python untuk Machine Learning

### 2.1.1 Mengapa Python untuk AI/ML?

Python menjadi bahasa pemrograman **paling populer** untuk AI dan machine learning karena:

| Keunggulan | Penjelasan |
|------------|------------|
| **Sintaks sederhana** | Mudah dibaca, mendekati pseudocode |
| **Ekosistem library** | NumPy, Pandas, scikit-learn, TensorFlow, PyTorch |
| **Komunitas besar** | Stack Overflow, GitHub, Kaggle, forum Indonesia |
| **Gratis & open-source** | Tidak perlu lisensi |
| **Google Colab** | Bisa langsung coding di browser tanpa instalasi |

### 2.1.2 Library Utama untuk ML

```
EKOSISTEM PYTHON UNTUK ML
═══════════════════════════════════════════════════════
                    PYTHON 3.x
                        │
    ┌───────────┬───────┼───────┬───────────┐
    │           │       │       │           │
  NumPy     Pandas  Matplotlib scikit-learn TensorFlow
  (Array &   (Data   (Visuali-  (ML klasik)  (Deep
   Matriks)  Frame)   sasi)                  Learning)
    │           │       │       │           │
  Komputasi  Manipu-  Plot &   Preprocessing PyTorch
  numerik    lasi     chart    Model         (alternatif)
  cepat      data             Training
                              Evaluation
═══════════════════════════════════════════════════════
```

```python
# Instalasi (sudah tersedia di Google Colab)
# !pip install numpy pandas matplotlib seaborn scikit-learn

# Import library utama
import numpy as np          # Komputasi numerik (array, matriks)
import pandas as pd         # Manipulasi data (DataFrame)
import matplotlib.pyplot as plt  # Visualisasi
import seaborn as sns       # Visualisasi statistik
from sklearn import preprocessing, model_selection, tree, metrics

# Cek versi
print(f"NumPy    : {np.__version__}")
print(f"Pandas   : {pd.__version__}")
print(f"Sklearn  : {__import__('sklearn').__version__}")
```

---

## 2.2 NumPy: Fondasi Komputasi Numerik

### 2.2.1 Apa itu NumPy?

**NumPy** (Numerical Python) adalah library untuk komputasi numerik yang menyediakan objek **ndarray** — array multi-dimensi yang sangat efisien.

> Mengapa NumPy, bukan list Python biasa? NumPy array **10-100x lebih cepat** daripada list Python untuk operasi numerik, karena menggunakan kode C di belakang layar.

### 2.2.2 Membuat Array NumPy

```python
import numpy as np

# === MEMBUAT ARRAY ===

# Dari list Python
nilai_uts = np.array([75, 82, 68, 91, 55, 78, 84, 72, 88, 65])
print(f"Nilai UTS: {nilai_uts}")
print(f"Tipe: {type(nilai_uts)}")
print(f"Shape: {nilai_uts.shape}")
print(f"Dtype: {nilai_uts.dtype}")

# Array 2D (matriks)
data_mahasiswa = np.array([
    [75, 80, 85],  # Mahasiswa 1: UTS, UAS, Tugas
    [82, 78, 90],  # Mahasiswa 2
    [68, 72, 75],  # Mahasiswa 3
    [91, 88, 95],  # Mahasiswa 4
    [55, 60, 65],  # Mahasiswa 5
])
print(f"\nData Mahasiswa (5x3):\n{data_mahasiswa}")
print(f"Shape: {data_mahasiswa.shape}")  # (5, 3) = 5 baris, 3 kolom

# Fungsi pembuat array
zeros = np.zeros((3, 4))          # Matriks 3x4 berisi 0
ones = np.ones((2, 3))            # Matriks 2x3 berisi 1
identitas = np.eye(3)             # Matriks identitas 3x3
range_arr = np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)   # 5 angka dari 0 sampai 1

print(f"\nZeros:\n{zeros}")
print(f"Identity:\n{identitas}")
print(f"Range: {range_arr}")
print(f"Linspace: {linspace}")
```

### 2.2.3 Operasi Array

```python
import numpy as np

# Data: nilai 10 mahasiswa (UTS dan UAS)
nilai_uts = np.array([75, 82, 68, 91, 55, 78, 84, 72, 88, 65])
nilai_uas = np.array([80, 85, 72, 88, 60, 82, 90, 75, 92, 70])

# === OPERASI ARITMATIKA (element-wise) ===
# Hitung nilai akhir: 40% UTS + 60% UAS
nilai_akhir = 0.4 * nilai_uts + 0.6 * nilai_uas
print(f"Nilai UTS  : {nilai_uts}")
print(f"Nilai UAS  : {nilai_uas}")
print(f"Nilai Akhir: {nilai_akhir}")

# === OPERASI STATISTIK ===
print(f"\n=== STATISTIK NILAI AKHIR ===")
print(f"Mean     : {np.mean(nilai_akhir):.2f}")
print(f"Median   : {np.median(nilai_akhir):.2f}")
print(f"Std Dev  : {np.std(nilai_akhir, ddof=1):.2f}")
print(f"Min      : {np.min(nilai_akhir):.2f}")
print(f"Max      : {np.max(nilai_akhir):.2f}")
print(f"Argmin   : Mahasiswa ke-{np.argmin(nilai_akhir)+1}")
print(f"Argmax   : Mahasiswa ke-{np.argmax(nilai_akhir)+1}")

# === OPERASI BOOLEAN (filtering) ===
lulus = nilai_akhir >= 70
print(f"\nLulus (>=70): {lulus}")
print(f"Jumlah lulus: {np.sum(lulus)}")
print(f"Persentase lulus: {np.mean(lulus)*100:.1f}%")

# Nilai mahasiswa yang lulus
print(f"Nilai yang lulus: {nilai_akhir[lulus]}")
```

### 2.2.4 Broadcasting

Broadcasting adalah mekanisme NumPy yang memungkinkan operasi antara array dengan shape berbeda.

```python
import numpy as np

# Contoh broadcasting: normalisasi data
data = np.array([
    [75, 80, 85],
    [82, 78, 90],
    [68, 72, 75],
    [91, 88, 95],
    [55, 60, 65],
])

# Mean dan std per kolom
col_mean = np.mean(data, axis=0)  # Shape: (3,)
col_std = np.std(data, axis=0, ddof=1)   # Shape: (3,)

# Broadcasting: (5,3) - (3,) → (5,3)
data_normalized = (data - col_mean) / col_std

print("Data asli:")
print(data)
print(f"\nMean per kolom : {col_mean}")
print(f"Std per kolom  : {col_std.round(2)}")
print(f"\nData setelah normalisasi (z-score):")
print(data_normalized.round(2))
```

### 2.2.5 Random Number Generation

```python
import numpy as np

# Set seed agar hasil reproducible
np.random.seed(42)

# Generate data acak — penting untuk simulasi dan testing
sampel_normal = np.random.normal(loc=75, scale=10, size=100)  # Mean=75, Std=10
sampel_uniform = np.random.uniform(low=50, high=100, size=100)
sampel_integer = np.random.randint(low=0, high=100, size=20)

print(f"Normal  - Mean: {sampel_normal.mean():.2f}, Std: {sampel_normal.std():.2f}")
print(f"Uniform - Mean: {sampel_uniform.mean():.2f}, Min: {sampel_uniform.min():.2f}, Max: {sampel_uniform.max():.2f}")
print(f"Integer - Data: {sampel_integer}")

# Shuffle dan sampling
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
np.random.shuffle(data)
print(f"\nSetelah shuffle: {data}")

# Random choice (sampling tanpa replacement)
pilihan = np.random.choice(data, size=5, replace=False)
print(f"Pilihan acak 5 elemen: {pilihan}")
```

---

## 2.3 Pandas: Manipulasi Data untuk ML

### 2.3.1 DataFrame dan Series

**Pandas** adalah library untuk manipulasi dan analisis data yang menyediakan dua struktur data utama: **Series** (1D) dan **DataFrame** (2D).

```python
import pandas as pd
import numpy as np

# === MEMBUAT DATAFRAME ===
# Contoh: data mahasiswa peserta mata kuliah AI/ML di UAI
data_mahasiswa = {
    'nim': ['2024001', '2024002', '2024003', '2024004', '2024005',
            '2024006', '2024007', '2024008', '2024009', '2024010'],
    'nama': ['Ahmad Rizki', 'Budi Santoso', 'Citra Dewi', 'Dian Permata',
             'Eko Prasetyo', 'Farah Aulia', 'Gilang Ramadhan', 'Hana Safira',
             'Irfan Maulana', 'Julia Putri'],
    'jenis_kelamin': ['L', 'L', 'P', 'P', 'L', 'P', 'L', 'P', 'L', 'P'],
    'asal_kota': ['Jakarta', 'Bekasi', 'Jakarta', 'Tangerang', 'Depok',
                  'Bogor', 'Jakarta', 'Bekasi', 'Jakarta', 'Tangerang'],
    'ipk': [3.45, 3.12, 3.78, 3.55, 3.21, 3.89, 3.33, 3.67, 3.10, 3.75],
    'nilai_uts': [78, 65, 88, 72, 58, 92, 70, 85, 62, 80],
    'nilai_uas': [82, 70, 90, 78, 63, 95, 75, 88, 68, 85],
    'pengalaman_python': ['Menengah', 'Pemula', 'Mahir', 'Menengah', 'Pemula',
                          'Mahir', 'Menengah', 'Menengah', 'Pemula', 'Mahir']
}

df = pd.DataFrame(data_mahasiswa)
print("=== INFO DATASET ===")
print(df.info())
print(f"\n=== 5 DATA PERTAMA ===")
print(df.head())
print(f"\n=== STATISTIK DESKRIPTIF ===")
print(df.describe().round(2))
```

### 2.3.2 Indexing dan Filtering

```python
# === INDEXING ===
# Mengakses kolom
print("Nama mahasiswa:")
print(df['nama'])

# Mengakses baris
print(f"\nMahasiswa ke-3:")
print(df.iloc[2])  # index ke-2 (0-based)

# Mengakses sel spesifik
print(f"\nIPK mahasiswa ke-3: {df.iloc[2]['ipk']}")
print(f"IPK mahasiswa ke-3 (loc): {df.loc[2, 'ipk']}")

# === FILTERING ===
# Mahasiswa dengan IPK >= 3.5
mahasiswa_berprestasi = df[df['ipk'] >= 3.5]
print(f"\nMahasiswa berprestasi (IPK >= 3.5):")
print(mahasiswa_berprestasi[['nim', 'nama', 'ipk']])

# Filter dengan multiple conditions
# Mahasiswa perempuan dari Jakarta dengan IPK >= 3.5
filter_1 = df[(df['jenis_kelamin'] == 'P') &
              (df['asal_kota'] == 'Jakarta') &
              (df['ipk'] >= 3.5)]
print(f"\nPerempuan Jakarta, IPK >= 3.5:")
print(filter_1[['nama', 'ipk']])

# Mahasiswa dari Jakarta ATAU Bekasi
filter_2 = df[df['asal_kota'].isin(['Jakarta', 'Bekasi'])]
print(f"\nDari Jakarta/Bekasi: {len(filter_2)} mahasiswa")
```

### 2.3.3 GroupBy dan Aggregasi

```python
# === GROUPBY ===
# Rata-rata nilai per kota asal
print("=== RATA-RATA NILAI PER KOTA ===")
print(df.groupby('asal_kota')[['nilai_uts', 'nilai_uas', 'ipk']].mean().round(2))

# Jumlah mahasiswa per jenis kelamin
print(f"\n=== JUMLAH PER JENIS KELAMIN ===")
print(df['jenis_kelamin'].value_counts())

# Multiple aggregations
print(f"\n=== AGREGASI IPK PER PENGALAMAN PYTHON ===")
agg_result = df.groupby('pengalaman_python')['ipk'].agg(['mean', 'min', 'max', 'count'])
print(agg_result.round(2))
```

### 2.3.4 Membuat Kolom Baru dan Merge

```python
# === MEMBUAT KOLOM BARU ===
# Hitung nilai akhir: 40% UTS + 60% UAS
df['nilai_akhir'] = 0.4 * df['nilai_uts'] + 0.6 * df['nilai_uas']

# Tentukan grade berdasarkan nilai akhir
def tentukan_grade(nilai):
    if nilai >= 85:
        return 'A'
    elif nilai >= 75:
        return 'B'
    elif nilai >= 65:
        return 'C'
    elif nilai >= 55:
        return 'D'
    else:
        return 'E'

df['grade'] = df['nilai_akhir'].apply(tentukan_grade)
print("=== NILAI AKHIR DAN GRADE ===")
print(df[['nama', 'nilai_uts', 'nilai_uas', 'nilai_akhir', 'grade']])

# Distribusi grade
print(f"\n=== DISTRIBUSI GRADE ===")
print(df['grade'].value_counts().sort_index())

# === MERGE ===
# Data tambahan: keaktifan organisasi
data_organisasi = pd.DataFrame({
    'nim': ['2024001', '2024003', '2024005', '2024006', '2024008'],
    'organisasi': ['BEM', 'HMIF', 'UKM Robotik', 'HMIF', 'BEM'],
    'jabatan': ['Anggota', 'Ketua', 'Anggota', 'Sekretaris', 'Bendahara']
})

# Left merge — semua mahasiswa, plus data organisasi jika ada
df_merged = df.merge(data_organisasi, on='nim', how='left')
print(f"\n=== SETELAH MERGE ===")
print(df_merged[['nama', 'organisasi', 'jabatan']].fillna('-'))
```

---

## 2.4 Data Preprocessing

Data preprocessing adalah tahap **paling penting** dalam pipeline ML — data yang bersih dan siap pakai menentukan kualitas model.

```
DATA MENTAH          PREPROCESSING           DATA SIAP ML
───────────         ───────────────          ────────────
Missing values  →   Imputasi               Lengkap
Teks kategori   →   Encoding               Numerik
Skala berbeda   →   Scaling                Seragam
Outlier         →   Treatment              Terkontrol
```

### 2.4.1 Handling Missing Values

```python
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# Contoh dataset dengan missing values
data_survey = {
    'usia': [20, 21, np.nan, 22, 20, 19, np.nan, 21, 22, 20],
    'ipk': [3.5, np.nan, 3.2, 3.8, 3.1, np.nan, 3.6, 3.4, np.nan, 3.7],
    'jam_belajar_per_hari': [3, 4, np.nan, 5, 2, 4, 3, np.nan, 5, 4],
    'punya_laptop': ['Ya', 'Ya', 'Tidak', np.nan, 'Ya', 'Ya', np.nan, 'Ya', 'Tidak', 'Ya']
}

df_survey = pd.DataFrame(data_survey)

# 1. Deteksi missing values
print("=== MISSING VALUES ===")
print(df_survey.isnull().sum())
print(f"\nPersentase missing:")
print((df_survey.isnull().mean() * 100).round(1))

# 2. Metode penanganan: fillna
# Isi dengan mean (untuk numerik)
df_filled = df_survey.copy()
df_filled['usia'] = df_filled['usia'].fillna(df_filled['usia'].mean())
df_filled['ipk'] = df_filled['ipk'].fillna(df_filled['ipk'].median())

# Isi dengan modus (untuk kategorikal)
df_filled['punya_laptop'] = df_filled['punya_laptop'].fillna(
    df_filled['punya_laptop'].mode()[0]
)
print(f"\n=== SETELAH FILLNA ===")
print(df_filled.isnull().sum())

# 3. Menggunakan SimpleImputer dari sklearn
from sklearn.impute import SimpleImputer

# Untuk kolom numerik
imputer_num = SimpleImputer(strategy='mean')  # bisa juga 'median', 'most_frequent'
kolom_numerik = ['usia', 'ipk', 'jam_belajar_per_hari']
df_survey[kolom_numerik] = imputer_num.fit_transform(df_survey[kolom_numerik])

# Untuk kolom kategorikal
imputer_cat = SimpleImputer(strategy='most_frequent')
df_survey[['punya_laptop']] = imputer_cat.fit_transform(df_survey[['punya_laptop']])

print(f"\n=== SETELAH SIMPLEIMPUTER ===")
print(df_survey.isnull().sum())
print(df_survey)
```

### 2.4.2 Encoding Variabel Kategorikal

Machine learning membutuhkan input **numerik**. Variabel kategorikal harus di-encode.

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Data contoh
data = pd.DataFrame({
    'kota': ['Jakarta', 'Bekasi', 'Tangerang', 'Depok', 'Bogor',
             'Jakarta', 'Bekasi', 'Jakarta', 'Depok', 'Bogor'],
    'pengalaman': ['Pemula', 'Menengah', 'Mahir', 'Pemula', 'Menengah',
                   'Mahir', 'Menengah', 'Pemula', 'Menengah', 'Mahir'],
    'ipk': [3.45, 3.12, 3.78, 3.21, 3.55, 3.89, 3.33, 3.10, 3.67, 3.75]
})

# === LABEL ENCODING ===
# Cocok untuk data ordinal (ada urutan alami)
le = LabelEncoder()
data['pengalaman_encoded'] = le.fit_transform(data['pengalaman'])
print("=== LABEL ENCODING (Pengalaman) ===")
print(f"Mapping: {dict(zip(le.classes_, le.transform(le.classes_)))}")
print(data[['pengalaman', 'pengalaman_encoded']])

# === ONE-HOT ENCODING ===
# Cocok untuk data nominal (tidak ada urutan)
# Menggunakan pd.get_dummies (cara paling mudah)
data_onehot = pd.get_dummies(data, columns=['kota'], prefix='kota', dtype=int)
print(f"\n=== ONE-HOT ENCODING (Kota) ===")
print(data_onehot.head())

# Menggunakan OneHotEncoder dari sklearn
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse_output=False, drop='first')  # drop='first' menghindari multicollinearity
kota_encoded = ohe.fit_transform(data[['kota']])
print(f"\nOneHotEncoder (drop first):\n{kota_encoded}")
print(f"Feature names: {ohe.get_feature_names_out()}")
```

**Kapan menggunakan apa?**

| Metode | Digunakan untuk | Contoh |
|--------|----------------|--------|
| **Label Encoding** | Data ordinal (ada urutan) | Pendidikan: SD=0, SMP=1, SMA=2, S1=3 |
| **One-Hot Encoding** | Data nominal (tidak ada urutan) | Kota: Jakarta, Bekasi, Depok |
| **Ordinal Encoding** | Data ordinal dengan mapping kustom | Rating: Buruk=1, Cukup=2, Baik=3 |

### 2.4.3 Feature Scaling

Algoritma ML tertentu sensitif terhadap skala fitur (terutama yang berbasis jarak seperti kNN, SVM, dan neural network).

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Data dengan skala berbeda
data_fitur = pd.DataFrame({
    'usia': [20, 21, 22, 19, 20, 23, 21, 22, 20, 19],
    'ipk': [3.45, 3.12, 3.78, 3.21, 3.55, 3.89, 3.33, 3.67, 3.10, 3.75],
    'pengeluaran_rp': [2500000, 1800000, 3200000, 1500000, 2100000,
                       3800000, 2000000, 2800000, 1600000, 3000000],
    'jam_belajar': [3, 4, 5, 2, 3, 6, 4, 5, 2, 4]
})

print("=== DATA ASLI ===")
print(data_fitur.describe().round(2))

# === STANDARD SCALER (Z-Score Normalization) ===
# Mengubah data sehingga mean = 0 dan std = 1
# Rumus: z = (x - mean) / std
scaler_std = StandardScaler()
data_standardized = pd.DataFrame(
    scaler_std.fit_transform(data_fitur),
    columns=data_fitur.columns
)

print(f"\n=== SETELAH STANDARD SCALER ===")
print(data_standardized.describe().round(2))

# === MIN-MAX SCALER ===
# Mengubah data ke range [0, 1]
# Rumus: x_scaled = (x - min) / (max - min)
scaler_mm = MinMaxScaler()
data_minmax = pd.DataFrame(
    scaler_mm.fit_transform(data_fitur),
    columns=data_fitur.columns
)

print(f"\n=== SETELAH MIN-MAX SCALER ===")
print(data_minmax.describe().round(2))
```

**Perbandingan StandardScaler vs MinMaxScaler:**

| Aspek | StandardScaler | MinMaxScaler |
|-------|---------------|-------------|
| Rumus | z = (x - μ) / σ | x' = (x - min) / (max - min) |
| Hasil | Mean=0, Std=1 | Range [0, 1] |
| Cocok untuk | Data terdistribusi normal | Data dengan range terbatas |
| Sensitif terhadap outlier | Cukup robust | Sangat sensitif |
| Digunakan oleh | SVM, Logistic Regression, PCA | Neural Networks, kNN |

---

## 2.5 Train-Test Split

### 2.5.1 Mengapa Perlu Membagi Data?

```
OVERFITTING vs GENERALIZATION
═══════════════════════════════════════════════
Model yang baik harus bisa MENGGENERALISASI —
yaitu bekerja baik pada data yang BELUM PERNAH dilihat.

Jika kita evaluasi model pada data yang sama
dengan data latih → TIDAK FAIR!

Analogi: Seperti memberikan soal ujian yang persis
sama dengan soal latihan — tidak mengukur pemahaman.
═══════════════════════════════════════════════
```

### 2.5.2 Implementasi Train-Test Split

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Contoh dataset: prediksi kelulusan mahasiswa
np.random.seed(42)
n = 100

data = pd.DataFrame({
    'jam_belajar': np.random.normal(4, 1.5, n).round(1),
    'kehadiran_persen': np.random.uniform(60, 100, n).round(1),
    'ipk_sebelumnya': np.random.normal(3.2, 0.4, n).round(2),
    'tugas_selesai': np.random.randint(5, 15, n),
})

# Target: lulus jika jam_belajar > 3 DAN kehadiran > 75 DAN ipk > 2.8
data['lulus'] = ((data['jam_belajar'] > 3) &
                  (data['kehadiran_persen'] > 75) &
                  (data['ipk_sebelumnya'] > 2.8)).astype(int)

print(f"Dataset: {data.shape}")
print(f"Distribusi target:\n{data['lulus'].value_counts()}")

# === SPLIT DATA ===
X = data.drop('lulus', axis=1)  # Fitur (features)
y = data['lulus']                # Target (label)

# 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% untuk testing
    random_state=42,     # Agar reproducible
    stratify=y           # Menjaga proporsi kelas
)

print(f"\n=== HASIL SPLIT ===")
print(f"Training set : {X_train.shape[0]} sampel ({X_train.shape[0]/len(X)*100:.0f}%)")
print(f"Testing set  : {X_test.shape[0]} sampel ({X_test.shape[0]/len(X)*100:.0f}%)")
print(f"\nDistribusi target (training):\n{y_train.value_counts()}")
print(f"\nDistribusi target (testing):\n{y_test.value_counts()}")
```

### 2.5.3 Strategi Split yang Umum

| Strategi | Rasio | Kapan Digunakan |
|----------|-------|-----------------|
| 80/20 | 80% train, 20% test | Paling umum, data cukup besar |
| 70/30 | 70% train, 30% test | Data menengah |
| 60/20/20 | 60% train, 20% validation, 20% test | Untuk hyperparameter tuning |
| Cross-validation | K-fold (k=5 atau 10) | Data terbatas |

> **Penting:** JANGAN PERNAH menggunakan data test untuk melatih model. Data test harus benar-benar "tidak terlihat" (*unseen*) oleh model sampai evaluasi akhir.

---

## 2.6 Scikit-learn API Pattern

### 2.6.1 Konsistensi API scikit-learn

Salah satu keunggulan **scikit-learn** adalah API yang **konsisten** — semua model mengikuti pola yang sama:

```
┌─────────────────────────────────────────────────────┐
│              SCIKIT-LEARN API PATTERN                 │
│                                                       │
│   1. model = ModelClass(hyperparameters)    # Inisialisasi   │
│   2. model.fit(X_train, y_train)           # Training        │
│   3. predictions = model.predict(X_test)    # Prediksi       │
│   4. score = model.score(X_test, y_test)   # Evaluasi        │
│                                                       │
│   Pola ini SAMA untuk SEMUA algoritma:               │
│   DecisionTree, RandomForest, SVM, kNN, dll          │
└─────────────────────────────────────────────────────┘
```

### 2.6.2 Contoh Lengkap: Pipeline ML dengan scikit-learn

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# === 1. PERSIAPAN DATA ===
np.random.seed(42)
n = 200

data = pd.DataFrame({
    'jam_belajar': np.random.normal(4, 1.5, n).round(1),
    'kehadiran': np.random.uniform(50, 100, n).round(1),
    'ipk': np.random.normal(3.0, 0.5, n).clip(0, 4).round(2),
    'tugas_selesai': np.random.randint(3, 14, n),
    'pengalaman_python': np.random.choice(
        ['Pemula', 'Menengah', 'Mahir'], n, p=[0.4, 0.4, 0.2]
    )
})

# Target: grade berdasarkan kombinasi fitur
skor = (data['jam_belajar'] * 5 + data['kehadiran'] * 0.3 +
        data['ipk'] * 10 + data['tugas_selesai'] * 2)
data['grade'] = pd.cut(skor, bins=3, labels=['C', 'B', 'A'])

print(f"Dataset shape: {data.shape}")
print(f"Distribusi grade:\n{data['grade'].value_counts()}")

# === 2. PREPROCESSING ===
# Encode kolom kategorikal
le_exp = LabelEncoder()
data['pengalaman_encoded'] = le_exp.fit_transform(data['pengalaman_python'])

le_grade = LabelEncoder()
data['grade_encoded'] = le_grade.fit_transform(data['grade'])

# Fitur dan target
fitur_kolom = ['jam_belajar', 'kehadiran', 'ipk', 'tugas_selesai', 'pengalaman_encoded']
X = data[fitur_kolom]
y = data['grade_encoded']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # PENTING: transform saja, bukan fit_transform!

# === 3. TRAINING ===
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train_scaled, y_train)

# === 4. PREDIKSI & EVALUASI ===
y_pred = model.predict(X_test_scaled)

print(f"\n=== EVALUASI MODEL ===")
print(f"Akurasi: {accuracy_score(y_test, y_pred):.2%}")
print(f"\nClassification Report:")
print(classification_report(
    y_test, y_pred,
    target_names=le_grade.classes_
))

# Confusion Matrix
print(f"Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# === 5. PREDIKSI DATA BARU ===
mahasiswa_baru = pd.DataFrame({
    'jam_belajar': [5.0],
    'kehadiran': [85.0],
    'ipk': [3.5],
    'tugas_selesai': [10],
    'pengalaman_encoded': [le_exp.transform(['Menengah'])[0]]
})

mahasiswa_baru_scaled = scaler.transform(mahasiswa_baru)
prediksi = model.predict(mahasiswa_baru_scaled)
print(f"\n=== PREDIKSI MAHASISWA BARU ===")
print(f"Grade: {le_grade.inverse_transform(prediksi)[0]}")
```

### 2.6.3 Kesalahan Umum yang Harus Dihindari

| Kesalahan | Penjelasan | Solusi |
|-----------|------------|--------|
| **Data leakage** | Fit scaler pada seluruh data (termasuk test) | Fit HANYA pada data training |
| **fit_transform pada test** | Menggunakan `fit_transform` pada data test | Gunakan `transform` saja |
| **Tidak set random_state** | Hasil berbeda setiap kali dijalankan | Selalu set `random_state=42` |
| **Lupa encode kategorikal** | Memasukkan string ke model | Encode semua kategorikal |
| **Tidak scaling** | Fitur dengan skala besar mendominasi | Scale semua fitur numerik |

```python
# SALAH: fit_transform pada test set
# X_test_scaled = scaler.fit_transform(X_test)  # ← JANGAN!

# BENAR: transform saja pada test set
X_test_scaled = scaler.transform(X_test)  # ← BENAR

# Alasan: fit() mempelajari parameter (mean, std) dari data.
# Jika fit pada test set, model "melihat" informasi test → data leakage.
```

---

## 2.7 AI Corner: Menggunakan AI untuk Debugging Preprocessing

### 2.7.1 AI untuk Debugging Kode ML

Level: **Basic**

| AI Bisa | AI Tidak Bisa |
|---------|--------------|
| Menjelaskan error message Python/sklearn | Memahami konteks bisnis data Anda |
| Menyarankan metode preprocessing yang tepat | Menentukan apakah data sudah cukup bersih |
| Menulis kode preprocessing dari deskripsi | Menjamin kode bebas bug 100% |
| Membandingkan StandardScaler vs MinMaxScaler | Memilihkan scaler terbaik tanpa eksperimen |

### 2.7.2 Contoh Prompting untuk Preprocessing

**Prompt yang Baik:**
```
Saya punya DataFrame Pandas dengan 5 kolom:
- usia (int, ada 10% missing values)
- pendapatan (float, range 1jt - 50jt, ada outlier > 100jt)
- kota (string, 5 kategori unik)
- pendidikan (ordinal: SD, SMP, SMA, S1, S2)
- target (binary: 0/1)

Buatkan pipeline preprocessing yang:
1. Handle missing values di usia dengan median
2. Handle outlier pendapatan menggunakan IQR
3. One-hot encode kota
4. Ordinal encode pendidikan
5. StandardScaler untuk fitur numerik
6. Train-test split 80/20 dengan stratify

Gunakan scikit-learn dan pastikan tidak ada data leakage.
```

**Prompt yang Kurang Baik:**
```
Preprocess data saya
```

### 2.7.3 Aktivitas: Debug dengan AI

1. Jalankan kode yang menghasilkan error (misal: ValueError saat fit model)
2. Copy-paste error message ke ChatGPT/Claude
3. Bandingkan solusi AI dengan pemahaman Anda sendiri
4. Dokumentasikan dalam AI Usage Log
5. Coba perbaiki error TANPA AI terlebih dahulu — ini melatih kemampuan debugging

### 2.7.4 Peringatan: Jangan Terlalu Bergantung pada AI

```
┌─────────────────────────────────────────────────┐
│         PERINGATAN KETERGANTUNGAN AI              │
│                                                   │
│  ✗ Copy-paste code dari AI tanpa memahami         │
│  ✗ Langsung bertanya AI setiap kali error         │
│  ✗ Tidak membaca dokumentasi sklearn               │
│                                                   │
│  ✓ Coba debug sendiri dulu (15 menit)             │
│  ✓ Baca error message dengan teliti               │
│  ✓ Gunakan AI untuk MEMAHAMI, bukan hanya SOLUSI  │
│  ✓ Verifikasi kode AI dengan menjalankannya       │
└─────────────────────────────────────────────────┘
```

---

## Rangkuman Bab 2

1. **Python** adalah bahasa utama untuk AI/ML berkat ekosistem library yang kaya: NumPy, Pandas, scikit-learn, TensorFlow, dan Matplotlib.
2. **NumPy** menyediakan array multi-dimensi untuk komputasi numerik yang efisien. Operasi broadcasting memungkinkan kalkulasi antara array dengan shape berbeda.
3. **Pandas** menyediakan DataFrame dan Series untuk manipulasi data tabular — termasuk indexing, filtering, groupby, merge, dan pembuatan kolom baru.
4. **Data Preprocessing** adalah tahap krusial dalam ML pipeline:
   - **Missing values**: fillna, SimpleImputer (mean, median, most_frequent)
   - **Encoding**: LabelEncoder (ordinal), OneHotEncoder (nominal)
   - **Scaling**: StandardScaler (z-score), MinMaxScaler (range 0-1)
5. **Train-Test Split** memisahkan data menjadi data latih dan data uji untuk mengevaluasi kemampuan generalisasi model. Gunakan `stratify` untuk menjaga proporsi kelas.
6. **Scikit-learn API** konsisten: `fit()` → `predict()` → `score()` untuk semua algoritma.
7. Hindari **data leakage**: fit scaler HANYA pada data training, gunakan `transform()` (bukan `fit_transform()`) pada data test.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan antara NumPy array dan Python list. Sebutkan minimal 3 keunggulan NumPy array untuk komputasi ML.

**Soal 2.** Buatlah NumPy array 2D berukuran 5x3 yang berisi data acak bilangan bulat antara 60 dan 100 (simulasi nilai 5 mahasiswa untuk 3 mata kuliah). Hitung mean per mahasiswa dan mean per mata kuliah.

**Soal 3.** Jelaskan perbedaan antara `iloc` dan `loc` pada Pandas DataFrame. Berikan contoh penggunaan masing-masing.

**Soal 4.** Mengapa kita perlu melakukan encoding pada variabel kategorikal sebelum melatih model ML? Jelaskan perbedaan antara Label Encoding dan One-Hot Encoding.

**Soal 5.** Apa yang dimaksud dengan data leakage? Berikan satu contoh data leakage dalam konteks preprocessing dan jelaskan bagaimana menghindarinya.

### Tingkat Menengah (C2-C3)

**Soal 6.** Diberikan dataset berikut:

```python
data = {
    'nama_produk': ['Laptop A', 'Laptop B', 'Laptop C', 'Laptop D', 'Laptop E'],
    'harga_juta': [8.5, np.nan, 15.0, 12.0, np.nan],
    'ram_gb': [8, 16, 16, np.nan, 8],
    'kategori': ['Budget', 'Premium', 'Premium', 'Mid-Range', 'Budget'],
    'rating': [4.2, 4.5, np.nan, 4.0, 3.8]
}
```

Tulis kode Python untuk:
- a) Mendeteksi missing values
- b) Mengisi missing values numerik dengan median
- c) One-hot encode kolom 'kategori'
- d) Menampilkan DataFrame hasil preprocessing

**Soal 7.** Tulis kode Python lengkap untuk:
- a) Membuat DataFrame dengan data 20 mahasiswa (nim, nama, kota, ipk, jam_belajar, lulus)
- b) Filter mahasiswa yang lulus dan berasal dari Jakarta
- c) Hitung rata-rata IPK per kota
- d) Tambahkan kolom kategori_ipk berdasarkan IPK (cumlaude >= 3.5, memuaskan >= 3.0, cukup < 3.0)

**Soal 8.** Jelaskan dengan contoh kode kapan menggunakan StandardScaler dan kapan MinMaxScaler. Tunjukkan hasil transformasi untuk kedua metode pada data yang sama.

### Tingkat Mahir (C3-C4)

**Soal 9.** Buatlah pipeline preprocessing lengkap menggunakan scikit-learn untuk dataset berikut (pastikan tidak ada data leakage):

```python
# Dataset: prediksi apakah mahasiswa lulus mata kuliah AI/ML
# Fitur: jam_belajar, kehadiran, ipk_sebelumnya, kota_asal, pengalaman_python
# Target: lulus (0/1)
```

Pipeline harus mencakup: handling missing values, encoding, scaling, dan train-test split.

**Soal 10.** Bandingkan hasil model DecisionTreeClassifier dengan dan tanpa preprocessing (scaling). Apakah scaling mempengaruhi akurasi Decision Tree? Jelaskan mengapa (hint: bagaimana Decision Tree membuat keputusan split).

---

## Daftar Pustaka Bab 2

1. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
2. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media.
3. Scikit-learn Documentation. (2025). *Preprocessing Data*. https://scikit-learn.org/stable/modules/preprocessing.html
4. NumPy Documentation. (2025). *NumPy User Guide*. https://numpy.org/doc/stable/user/
5. Pandas Documentation. (2025). *User Guide*. https://pandas.pydata.org/docs/user_guide/
6. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
7. Muller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*. O'Reilly Media.

---

*Bab berikutnya: **Bab 3 — Matematika untuk Machine Learning***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
