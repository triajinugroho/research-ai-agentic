# Lab 01: Setup Environment AI/ML

**Mata Kuliah:** Kecerdasan Buatan dan Machine Learning
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Minggu:** 1
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

- Menyiapkan environment Google Colab untuk pengembangan AI/ML
- Mengimpor dan memverifikasi library utama machine learning
- Memuat dataset pertama menggunakan scikit-learn
- Melakukan eksplorasi data dasar (shape, head, describe, info)
- Membuat visualisasi sederhana dari fitur dataset
- Memahami pola dasar API scikit-learn (fit, predict, score)

---

## Persiapan

1. Buka Google Colab di [colab.research.google.com](https://colab.research.google.com)
2. Buat notebook baru dengan nama: `Lab01_NamaAnda_NIM.ipynb`
3. Pastikan runtime menggunakan Python 3 (Runtime > Change runtime type > Python 3)
4. Koneksi internet aktif untuk mengunduh library jika diperlukan

---

## Langkah-langkah

### Langkah 1: Setup Google Colab dan Import Library ML

```python
# =============================================
# LANGKAH 1: Setup Google Colab & Import Library
# =============================================

# Import library utama untuk Machine Learning
import numpy as np              # Komputasi numerik
import pandas as pd             # Manipulasi data
import matplotlib.pyplot as plt # Visualisasi dasar
import seaborn as sns           # Visualisasi statistik

# Library Machine Learning
from sklearn import datasets    # Dataset bawaan sklearn
from sklearn.model_selection import train_test_split  # Pembagian data
from sklearn.preprocessing import StandardScaler      # Normalisasi
from sklearn.linear_model import LogisticRegression   # Model klasifikasi
from sklearn.metrics import accuracy_score            # Evaluasi

# Cek apakah TensorFlow tersedia di Colab
try:
    import tensorflow as tf
    print(f"TensorFlow tersedia: {tf.__version__}")
except ImportError:
    print("TensorFlow tidak tersedia. Install dengan: !pip install tensorflow")

# Pengaturan tampilan
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.4f}'.format)
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

print("=" * 50)
print("SETUP ENVIRONMENT AI/ML BERHASIL!")
print("=" * 50)
print("Semua library utama telah diimpor.")
```

### Langkah 2: Cek Versi Library

```python
# =============================================
# LANGKAH 2: Cek Versi Library
# =============================================

import sklearn
import sys

print("=" * 50)
print("VERSI LIBRARY YANG DIGUNAKAN")
print("=" * 50)

# Daftar library dan versinya
libraries = {
    'Python': sys.version.split()[0],
    'NumPy': np.__version__,
    'Pandas': pd.__version__,
    'Matplotlib': plt.matplotlib.__version__,
    'Seaborn': sns.__version__,
    'Scikit-learn': sklearn.__version__,
}

# Tambahkan TensorFlow jika tersedia
try:
    import tensorflow as tf
    libraries['TensorFlow'] = tf.__version__
except ImportError:
    libraries['TensorFlow'] = 'Tidak terinstall'

# Tampilkan dalam format tabel
for lib, ver in libraries.items():
    print(f"  {lib:15s} : {ver}")

print("\n--- Informasi GPU (jika tersedia) ---")
try:
    gpu_info = tf.config.list_physical_devices('GPU')
    if gpu_info:
        print(f"  GPU terdeteksi: {gpu_info[0].name}")
    else:
        print("  Tidak ada GPU (menggunakan CPU)")
except:
    print("  Tidak dapat mengecek GPU")

print("\nSemua versi library sudah dicek!")
```

### Langkah 3: Load Dataset Iris dengan scikit-learn

```python
# =============================================
# LANGKAH 3: Load Dataset Iris
# =============================================

# Muat dataset iris dari sklearn
iris = datasets.load_iris()

# Konversi ke DataFrame pandas untuk kemudahan eksplorasi
df_iris = pd.DataFrame(
    data=iris.data,
    columns=iris.feature_names
)

# Tambahkan kolom target (jenis bunga)
df_iris['species'] = iris.target
df_iris['species_name'] = df_iris['species'].map({
    0: 'Setosa',
    1: 'Versicolor',
    2: 'Virginica'
})

print("=" * 50)
print("DATASET IRIS BERHASIL DIMUAT")
print("=" * 50)
print(f"\nDeskripsi: {iris.DESCR[:200]}...")
print(f"\nFitur (features): {iris.feature_names}")
print(f"Target (kelas)  : {list(iris.target_names)}")
print(f"Jumlah sampel   : {len(df_iris)}")
print(f"Jumlah fitur    : {len(iris.feature_names)}")

print("\n--- 5 Data Pertama ---")
df_iris.head()
```

### Langkah 4: Eksplorasi Data Dasar

```python
# =============================================
# LANGKAH 4: Eksplorasi Data Dasar
# =============================================

print("=" * 50)
print("EKSPLORASI DATA DASAR")
print("=" * 50)

# 1. Shape (dimensi data)
print(f"\n1. SHAPE (Dimensi Data)")
print(f"   Baris x Kolom: {df_iris.shape}")
print(f"   Jumlah baris : {df_iris.shape[0]}")
print(f"   Jumlah kolom : {df_iris.shape[1]}")

# 2. Head (data awal)
print(f"\n2. HEAD (5 Data Pertama)")
print(df_iris.head())

# 3. Describe (statistik deskriptif)
print(f"\n3. DESCRIBE (Statistik Deskriptif)")
print(df_iris.describe())

# 4. Info (tipe data dan memori)
print(f"\n4. INFO (Tipe Data)")
print(df_iris.info())

# 5. Distribusi kelas target
print(f"\n5. DISTRIBUSI KELAS")
distribusi = df_iris['species_name'].value_counts()
print(distribusi)
print(f"\nDataset {'seimbang (balanced)' if distribusi.nunique() == 1 else 'tidak seimbang (imbalanced)'}")

# 6. Cek missing values
print(f"\n6. MISSING VALUES")
missing = df_iris.isnull().sum()
print(missing)
print(f"\nTotal missing values: {missing.sum()}")
```

### Langkah 5: Visualisasi Sederhana (Scatter Plot Fitur Iris)

```python
# =============================================
# LANGKAH 5: Visualisasi Scatter Plot Iris
# =============================================

# Warna untuk setiap spesies
colors = {'Setosa': '#e74c3c', 'Versicolor': '#3498db', 'Virginica': '#2ecc71'}

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Scatter Plot Fitur Dataset Iris', fontsize=16, fontweight='bold')

# Plot 1: Sepal Length vs Sepal Width
ax = axes[0, 0]
for species in df_iris['species_name'].unique():
    mask = df_iris['species_name'] == species
    ax.scatter(df_iris.loc[mask, 'sepal length (cm)'],
               df_iris.loc[mask, 'sepal width (cm)'],
               c=colors[species], label=species, alpha=0.7, edgecolors='w')
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Sepal Width (cm)')
ax.set_title('Sepal Length vs Sepal Width')
ax.legend()

# Plot 2: Petal Length vs Petal Width
ax = axes[0, 1]
for species in df_iris['species_name'].unique():
    mask = df_iris['species_name'] == species
    ax.scatter(df_iris.loc[mask, 'petal length (cm)'],
               df_iris.loc[mask, 'petal width (cm)'],
               c=colors[species], label=species, alpha=0.7, edgecolors='w')
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Petal Width (cm)')
ax.set_title('Petal Length vs Petal Width')
ax.legend()

# Plot 3: Sepal Length vs Petal Length
ax = axes[1, 0]
for species in df_iris['species_name'].unique():
    mask = df_iris['species_name'] == species
    ax.scatter(df_iris.loc[mask, 'sepal length (cm)'],
               df_iris.loc[mask, 'petal length (cm)'],
               c=colors[species], label=species, alpha=0.7, edgecolors='w')
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Petal Length (cm)')
ax.set_title('Sepal Length vs Petal Length')
ax.legend()

# Plot 4: Heatmap korelasi
ax = axes[1, 1]
fitur_numerik = df_iris[iris.feature_names]
corr_matrix = fitur_numerik.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
            fmt='.2f', ax=ax, square=True)
ax.set_title('Korelasi Antar Fitur')

plt.tight_layout()
plt.show()

print("Visualisasi scatter plot dan heatmap korelasi selesai!")
```

### Langkah 6: Pengenalan Pola API scikit-learn (fit, predict, score)

```python
# =============================================
# LANGKAH 6: Pengenalan API scikit-learn
# =============================================

print("=" * 50)
print("POLA API SCIKIT-LEARN: fit → predict → score")
print("=" * 50)

# --- Tahap 1: Persiapan Data ---
X = iris.data          # Fitur (4 kolom numerik)
y = iris.target        # Target (0, 1, 2 = jenis bunga)

# Bagi data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Data training: {X_train.shape[0]} sampel")
print(f"Data testing : {X_test.shape[0]} sampel")

# --- Tahap 2: Normalisasi (Scaling) ---
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit + transform pada training
X_test_scaled = scaler.transform(X_test)         # hanya transform pada testing

print(f"\nMean sebelum scaling : {X_train[:, 0].mean():.4f}")
print(f"Mean setelah scaling : {X_train_scaled[:, 0].mean():.4f}")

# --- Tahap 3: FIT (Latih Model) ---
model = LogisticRegression(random_state=42, max_iter=200)
model.fit(X_train_scaled, y_train)    # <-- fit: model belajar dari data training
print(f"\nModel berhasil di-fit (dilatih)!")

# --- Tahap 4: PREDICT (Prediksi) ---
y_pred = model.predict(X_test_scaled)  # <-- predict: model membuat prediksi
print(f"\nHasil prediksi (5 pertama) : {y_pred[:5]}")
print(f"Label asli     (5 pertama) : {y_test[:5]}")

# --- Tahap 5: SCORE (Evaluasi) ---
akurasi = model.score(X_test_scaled, y_test)  # <-- score: evaluasi performa
print(f"\nAkurasi model: {akurasi:.4f} ({akurasi*100:.1f}%)")

# Penjelasan pola API
print(f"""
{'=' * 50}
RINGKASAN POLA API SCIKIT-LEARN
{'=' * 50}

1. PERSIAPAN DATA
   X_train, X_test, y_train, y_test = train_test_split(X, y)

2. FIT (Latih Model)
   model.fit(X_train, y_train)
   → Model mempelajari pola dari data training

3. PREDICT (Prediksi)
   y_pred = model.predict(X_test)
   → Model membuat prediksi pada data baru

4. SCORE (Evaluasi)
   akurasi = model.score(X_test, y_test)
   → Mengukur seberapa baik prediksi model

Pola ini SAMA untuk semua model di scikit-learn!
(LinearRegression, DecisionTree, SVM, KNN, dll.)
""")
```

---

## Tantangan Tambahan

1. **Load Dataset Lain:** Muat dataset `load_wine()` atau `load_digits()` dari `sklearn.datasets`. Lakukan eksplorasi data yang sama (shape, head, describe) dan buat visualisasi scatter plot untuk fitur-fitur utamanya.

2. **Dashboard Visualisasi Sederhana:** Buat figure dengan 6 subplot yang menampilkan: histogram setiap fitur iris (4 subplot), scatter plot terbaik (1 subplot), dan bar chart distribusi kelas (1 subplot). Gunakan `plt.subplots(2, 3)`.

3. **Perbandingan Model:** Gunakan pola API scikit-learn untuk melatih model `DecisionTreeClassifier` dan bandingkan akurasinya dengan `LogisticRegression` pada dataset iris.

---

## Checklist Penyelesaian

- [ ] Google Colab environment berhasil disiapkan
- [ ] Semua library (numpy, pandas, sklearn, tensorflow, matplotlib) berhasil diimpor
- [ ] Versi semua library ditampilkan tanpa error
- [ ] Dataset iris berhasil dimuat dan dikonversi ke DataFrame
- [ ] Eksplorasi data dasar (shape, head, describe, info) berhasil dijalankan
- [ ] Scatter plot fitur iris berhasil dibuat dan ditampilkan
- [ ] Pola API scikit-learn (fit, predict, score) dipahami dan dijalankan
- [ ] Notebook disimpan dengan nama `Lab01_NamaAnda_NIM.ipynb`
- [ ] Minimal 1 tantangan tambahan diselesaikan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
