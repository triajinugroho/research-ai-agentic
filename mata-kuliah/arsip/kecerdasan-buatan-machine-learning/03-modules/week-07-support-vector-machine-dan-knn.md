# Minggu 7: Support Vector Machine dan KNN

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 7 |
| **Topik** | Support Vector Machine dan K-Nearest Neighbors |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK-3: Menerapkan dan menganalisis algoritma supervised learning |
| **Sub-CPMK** | 7.1 Menganalisis algoritma KNN dan SVM untuk klasifikasi dan regresi |
| | 7.2 Menganalisis perbandingan model supervised learning menggunakan cross-validation |
| **Bloom's Taxonomy** | C4 (Menganalisis / *Analyze*) |
| **Durasi** | 2 x 100 menit (Teori 100 min + Praktikum 100 min) |
| **Platform** | Google Colab |
| **Metode** | Ceramah interaktif, live coding, hands-on praktikum |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menganalisis** prinsip kerja K-Nearest Neighbors (KNN) termasuk metrik jarak, pemilihan K, dan trade-off bias-variance.
2. **Menerapkan** KNN untuk permasalahan klasifikasi dan regresi dengan scikit-learn.
3. **Menganalisis** konsep Support Vector Machine (SVM) termasuk hyperplane, margin, dan support vectors.
4. **Membandingkan** kernel SVM (linear, polynomial, RBF) dan dampaknya pada decision boundary.
5. **Mengevaluasi** performa berbagai model supervised learning dari segi akurasi, waktu pelatihan, dan interpretabilitas.
6. **Menerapkan** teknik cross-validation (k-fold, stratified k-fold) untuk evaluasi model yang lebih robust.
7. **Mengimplementasikan** Pipeline dan GridSearchCV dari scikit-learn untuk workflow ML yang terstruktur.

---

## Materi Pembelajaran

### 1. K-Nearest Neighbors (KNN): Konsep

#### Prinsip Dasar

KNN adalah algoritma supervised learning yang **tidak membangun model eksplisit** saat pelatihan (*lazy learner*). Prediksi dilakukan dengan mencari K tetangga terdekat dari data baru, lalu mengambil keputusan berdasarkan tetangga tersebut.

#### Analogi Kehidupan Sehari-hari

Bayangkan Anda pindah ke lingkungan baru di Jakarta. Untuk memperkirakan berapa harga rumah di sekitar Anda, cara paling sederhana adalah bertanya ke 5 tetangga terdekat. Rata-rata harga rumah tetangga adalah estimasi terbaik Anda -- inilah konsep KNN!

```
Klasifikasi KNN (K=3):

     o = Kelas A (Disetujui)
     x = Kelas B (Ditolak)
     ? = Data baru

         o
       o   o
     x   ?   o    ← 3 tetangga terdekat: 2 'o', 1 'x'
       x   x      ← Prediksi: Kelas A (mayoritas)
         x
```

#### Algoritma KNN

1. Tentukan nilai K (jumlah tetangga)
2. Hitung jarak dari data baru ke seluruh data training
3. Pilih K data terdekat
4. **Klasifikasi**: voting mayoritas dari K tetangga
5. **Regresi**: rata-rata nilai target dari K tetangga

---

### 2. Distance Metrics dan Pemilihan K

#### Metrik Jarak

| Metrik | Rumus | Kapan Digunakan |
|---|---|---|
| **Euclidean** | √(Σ(xᵢ - yᵢ)²) | Default; cocok untuk data kontinu |
| **Manhattan** | Σ\|xᵢ - yᵢ\| | Cocok untuk data berdimensi tinggi |
| **Minkowski** | (Σ\|xᵢ - yᵢ\|ᵖ)^(1/p) | Generalisasi; p=2 → Euclidean, p=1 → Manhattan |

#### Pentingnya Normalisasi

Karena KNN berbasis jarak, fitur dengan skala besar akan **mendominasi** perhitungan jarak:

```
Contoh tanpa normalisasi:
  Fitur 'gaji'  : 5.000.000 - 50.000.000  (range: 45 juta)
  Fitur 'usia'  : 18 - 65                  (range: 47)

  → Jarak didominasi oleh 'gaji' karena range-nya jauh lebih besar
  → Solusi: StandardScaler atau MinMaxScaler
```

#### Memilih Nilai K

```
Akurasi
  |     Testing
  |   *
  | *   *
  |       * * * * * * *
  |                     * * *
  |
  +--+--+--+--+--+--+--+--+--
     1  3  5  7  9 11 13 15
                K

K kecil (1-3): Sensitif terhadap noise, overfitting
K besar (15+): Terlalu general, underfitting
K optimal   : Dicari dengan cross-validation
```

Pedoman umum:
- K ganjil (menghindari tie pada klasifikasi biner)
- K = √n (n = jumlah data training) sebagai titik awal
- Evaluasi beberapa nilai K dengan cross-validation

---

### 3. Support Vector Machine (SVM): Konsep

#### Hyperplane dan Margin

SVM mencari **hyperplane** (batas keputusan) yang memisahkan dua kelas dengan **margin terbesar**. Margin adalah jarak antara hyperplane dan data terdekat dari masing-masing kelas.

```
     Kelas A (o)          Kelas B (x)

      o    o    |          |    x    x
        o       |  Margin  |      x
      o    o    |          |    x
        o       |          |      x    x
                |          |

           Support Vectors (titik terdekat ke hyperplane)
                ↑          ↑
```

#### Support Vectors

**Support vectors** adalah titik data yang paling dekat dengan hyperplane. Mereka "mendukung" posisi hyperplane -- jika dihapus, hyperplane akan berubah. Titik-titik lain tidak mempengaruhi posisi hyperplane.

#### Mengapa Margin Terbesar?

Margin yang lebih besar memberikan **generalisasi yang lebih baik**. Model dengan margin lebar lebih toleran terhadap variasi data baru. Ini mirip dengan prinsip kehati-hatian -- lebih baik memiliki "jarak aman" yang cukup.

---

### 4. SVM Kernels

#### Masalah Data Non-linear

Tidak semua data dapat dipisahkan dengan garis lurus. Kernel trick memproyeksikan data ke dimensi yang lebih tinggi agar menjadi *linearly separable*.

```
Data 2D (tidak bisa dipisahkan linear):

     x x x
   x o o o x        ← Kelas 'o' di tengah,
   x o o o x           'x' di pinggir
     x x x

Setelah kernel RBF (proyeksi ke 3D):

       x x x x
     x x x x x
   ---o-o-o---  ← Sekarang bisa dipisahkan!
     x x x x x
       x x x x
```

#### Jenis Kernel

| Kernel | Fungsi | Karakteristik |
|---|---|---|
| **Linear** | K(x,y) = xᵀy | Cepat; cocok untuk data linearly separable |
| **Polynomial** | K(x,y) = (γxᵀy + r)ᵈ | Bisa menangkap interaksi fitur; parameter d (degree) |
| **RBF (Radial Basis Function)** | K(x,y) = exp(-γ\|\|x-y\|\|²) | Paling fleksibel; cocok untuk kebanyakan kasus |

#### Parameter Penting SVM

| Parameter | Fungsi | Efek |
|---|---|---|
| **C** (regularization) | Mengontrol trade-off antara margin lebar dan kesalahan klasifikasi | C besar → margin kecil, lebih fit ke training data; C kecil → margin lebar, lebih general |
| **gamma** (γ) | Mengontrol "jangkauan" pengaruh setiap data point (kernel RBF/poly) | gamma besar → decision boundary lebih kompleks; gamma kecil → lebih smooth |
| **kernel** | Jenis transformasi | 'linear', 'poly', 'rbf' |

---

### 5. Perbandingan Model Supervised Learning

Setelah mempelajari berbagai algoritma (Minggu 5-7), berikut perbandingannya:

| Kriteria | Linear/Logistic Regression | Decision Tree | Random Forest | KNN | SVM |
|---|---|---|---|---|---|
| **Interpretabilitas** | Tinggi | Tinggi | Sedang | Rendah | Rendah |
| **Kecepatan Training** | Cepat | Cepat | Sedang | Sangat cepat (lazy) | Lambat (data besar) |
| **Kecepatan Prediksi** | Sangat cepat | Sangat cepat | Cepat | Lambat (hitung jarak) | Cepat |
| **Robust terhadap Outlier** | Rendah | Tinggi | Tinggi | Rendah | Sedang (RBF) |
| **Butuh Normalisasi** | Tidak (LR) | Tidak | Tidak | Ya (wajib) | Ya (wajib) |
| **Cocok untuk Fitur Banyak** | Ya | Sedang | Ya | Tidak (curse of dimensionality) | Ya |
| **Non-linear** | Tidak (tanpa transformasi) | Ya | Ya | Ya | Ya (kernel) |

#### Kapan Menggunakan Apa?

- **Regresi Linear**: target kontinu, hubungan linear
- **Logistic Regression**: klasifikasi biner, butuh interpretasi koefisien
- **Decision Tree**: butuh interpretabilitas tinggi, data campuran
- **Random Forest**: butuh akurasi tinggi, tidak peduli interpretabilitas
- **KNN**: data sedikit, batasan jelas antar kelas
- **SVM**: data berdimensi tinggi, batas non-linear

---

### 6. Cross-Validation

#### Masalah dengan Single Train-Test Split

Satu kali pembagian data bisa menghasilkan evaluasi yang *bias*. Data testing tertentu mungkin kebetulan mudah atau sulit, sehingga tidak merepresentasikan performa sebenarnya.

#### K-Fold Cross-Validation

Data dibagi menjadi K *fold* (lipatan). Model dilatih K kali, setiap kali menggunakan fold berbeda sebagai testing:

```
5-Fold Cross-Validation:

Fold 1: [Test] [Train] [Train] [Train] [Train] → Skor 1
Fold 2: [Train] [Test] [Train] [Train] [Train] → Skor 2
Fold 3: [Train] [Train] [Test] [Train] [Train] → Skor 3
Fold 4: [Train] [Train] [Train] [Test] [Train] → Skor 4
Fold 5: [Train] [Train] [Train] [Train] [Test] → Skor 5

Skor Akhir = Rata-rata(Skor 1, 2, 3, 4, 5)
```

#### Stratified K-Fold

Untuk data yang **imbalanced** (distribusi kelas tidak seimbang), stratified k-fold memastikan setiap fold memiliki proporsi kelas yang sama:

```
Dataset: 80% Kelas A, 20% Kelas B

Stratified: Setiap fold tetap 80% A, 20% B
Regular   : Beberapa fold mungkin 90% A, 10% B (tidak representatif)
```

---

### 7. Scikit-learn Pipeline dan GridSearchCV

#### Mengapa Pipeline?

Pipeline menggabungkan langkah-langkah preprocessing dan modeling menjadi satu objek. Keuntungan:
- Mencegah *data leakage* (informasi test bocor ke training saat preprocessing)
- Kode lebih bersih dan terorganisir
- Bisa langsung digunakan dengan cross-validation dan grid search

```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('scaler', StandardScaler()),      # Langkah 1: Normalisasi
    ('model', SVC(kernel='rbf'))       # Langkah 2: Model SVM
])
```

#### GridSearchCV

GridSearchCV secara otomatis mencoba semua kombinasi hyperparameter dan mengevaluasi dengan cross-validation:

```
Parameter Grid:
  C     : [0.1, 1, 10]
  gamma : [0.01, 0.1, 1]
  kernel: ['rbf', 'linear']

Total kombinasi: 3 × 3 × 2 = 18
Dengan 5-fold CV: 18 × 5 = 90 kali pelatihan
```

---

## Aktivitas Kelas

### Sesi 1: Teori dan Diskusi (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Review & Pembukaan | Review Decision Tree & Random Forest minggu 6, pengantar KNN |
| 20 menit | Ceramah Interaktif | KNN: konsep, distance metrics, pemilihan K, normalisasi |
| 20 menit | Ceramah Interaktif | SVM: hyperplane, margin, support vectors, kernel trick |
| 15 menit | Ceramah Interaktif | Perbandingan model dan cross-validation |
| 15 menit | Diskusi Kelompok | "Algoritma mana yang terbaik untuk prediksi churn bank? Berikan argumentasi." |
| 10 menit | Pipeline & GridSearchCV | Demonstrasi workflow ML yang terstruktur |
| 10 menit | Tanya Jawab & Info Kuis | Pengumuman K2 Kuis: Supervised Learning (Minggu 5-7) |

### Sesi 2: Praktikum Hands-on (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Setup & Data Loading | Buka Google Colab, import library, load dataset |
| 25 menit | Hands-on KNN | Implementasi KNN, eksperimen nilai K, visualisasi |
| 25 menit | Hands-on SVM | Implementasi SVM dengan berbagai kernel, visualisasi decision boundary |
| 20 menit | Perbandingan & Cross-Val | Bandingkan semua model dengan Pipeline dan cross-validation |
| 15 menit | GridSearchCV | Optimasi hyperparameter model terbaik |
| 5 menit | Wrap-up & Pengumuman | Rangkuman, info UTS minggu depan |

---

## Hands-on: Perbandingan KNN vs SVM pada Dataset Indonesia

### Langkah 1: Import Library

```python
# Import library yang dibutuhkan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from sklearn.model_selection import (train_test_split, cross_val_score,
                                      StratifiedKFold, GridSearchCV)
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import (classification_report, confusion_matrix,
                             accuracy_score)

print("Semua library berhasil di-import!")
```

### Langkah 2: Dataset Klasifikasi Kualitas Pelayanan Rumah Sakit Indonesia

```python
# Dataset simulasi kualitas pelayanan rumah sakit di Indonesia
np.random.seed(42)
n = 400

waktu_tunggu_menit = np.random.exponential(30, n).round(0)
jumlah_dokter = np.random.randint(5, 50, n)
rasio_perawat = np.random.uniform(0.5, 3.0, n).round(2)
bed_occupancy_rate = np.random.uniform(0.3, 1.0, n).round(2)
skor_fasilitas = np.random.randint(1, 11, n)  # 1-10
jumlah_komplain = np.random.poisson(5, n)
indeks_kepuasan = np.random.uniform(1, 5, n).round(1)

# Kualitas pelayanan: Baik (1) atau Perlu Perbaikan (0)
skor = (- 0.02 * waktu_tunggu_menit + 0.03 * jumlah_dokter
        + 0.5 * rasio_perawat - 1.5 * bed_occupancy_rate
        + 0.1 * skor_fasilitas - 0.1 * jumlah_komplain
        + 0.3 * indeks_kepuasan + np.random.normal(0, 0.5, n))
kualitas_baik = (skor > np.median(skor)).astype(int)

df_rs = pd.DataFrame({
    'waktu_tunggu_menit': waktu_tunggu_menit,
    'jumlah_dokter': jumlah_dokter,
    'rasio_perawat_pasien': rasio_perawat,
    'bed_occupancy_rate': bed_occupancy_rate,
    'skor_fasilitas': skor_fasilitas,
    'jumlah_komplain_bulanan': jumlah_komplain,
    'indeks_kepuasan_pasien': indeks_kepuasan,
    'kualitas_baik': kualitas_baik
})

print("Dataset Kualitas Pelayanan Rumah Sakit Indonesia:")
print(df_rs.head(10))
print(f"\nJumlah data: {len(df_rs)}")
print(f"\nDistribusi kualitas:")
print(df_rs['kualitas_baik'].value_counts())
print(f"\nStatistik deskriptif:")
print(df_rs.describe().round(2))
```

### Langkah 3: Persiapan Data

```python
# Fitur dan target
X = df_rs.drop('kualitas_baik', axis=1)
y = df_rs['kualitas_baik']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Normalisasi (penting untuk KNN dan SVM)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Data training: {len(X_train)} sampel")
print(f"Data testing : {len(X_test)} sampel")
```

### Langkah 4: KNN -- Eksperimen Nilai K

```python
# Eksperimen berbagai nilai K
k_values = range(1, 31, 2)  # K ganjil: 1, 3, 5, ..., 29
train_scores_knn = []
test_scores_knn = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    train_scores_knn.append(knn.score(X_train_scaled, y_train))
    test_scores_knn.append(knn.score(X_test_scaled, y_test))

# Visualisasi
plt.figure(figsize=(10, 6))
plt.plot(k_values, train_scores_knn, 'b-o', label='Training Accuracy', markersize=4)
plt.plot(k_values, test_scores_knn, 'r-o', label='Testing Accuracy', markersize=4)
best_k = list(k_values)[np.argmax(test_scores_knn)]
plt.axvline(x=best_k, color='green', linestyle='--',
            label=f'Best K={best_k} (Acc={max(test_scores_knn)*100:.1f}%)')
plt.xlabel('Nilai K (Jumlah Tetangga)')
plt.ylabel('Accuracy')
plt.title('KNN: Pengaruh Nilai K terhadap Akurasi')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"K optimal: {best_k}")
print(f"Akurasi terbaik: {max(test_scores_knn)*100:.1f}%")
```

### Langkah 5: KNN -- Model dengan K Optimal

```python
# KNN dengan K optimal
knn_best = KNeighborsClassifier(n_neighbors=best_k)
knn_best.fit(X_train_scaled, y_train)
y_pred_knn = knn_best.predict(X_test_scaled)

print(f"=== KNN (K={best_k}) ===")
print(f"Akurasi Training: {knn_best.score(X_train_scaled, y_train)*100:.1f}%")
print(f"Akurasi Testing : {accuracy_score(y_test, y_pred_knn)*100:.1f}%")
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred_knn,
      target_names=['Perlu Perbaikan', 'Kualitas Baik']))
```

### Langkah 6: SVM -- Perbandingan Kernel

```python
# SVM dengan berbagai kernel
kernels = ['linear', 'poly', 'rbf']
svm_results = {}

for kernel in kernels:
    start_time = time.time()
    svm = SVC(kernel=kernel, random_state=42)
    svm.fit(X_train_scaled, y_train)
    train_time = time.time() - start_time

    y_pred_svm = svm.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred_svm)

    svm_results[kernel] = {
        'model': svm,
        'accuracy': acc,
        'train_time': train_time,
        'y_pred': y_pred_svm
    }

    print(f"SVM ({kernel}):")
    print(f"  Akurasi: {acc*100:.1f}%")
    print(f"  Waktu training: {train_time:.3f} detik")
    print()

# Tabel perbandingan
print("=== Perbandingan Kernel SVM ===")
print(f"{'Kernel':<12} {'Accuracy':>10} {'Train Time':>12}")
print("-" * 36)
for kernel, result in svm_results.items():
    print(f"{kernel:<12} {result['accuracy']*100:>9.1f}% {result['train_time']:>10.3f}s")
```

### Langkah 7: Perbandingan Semua Model dengan Cross-Validation

```python
# Definisikan semua model dalam Pipeline
models = {
    'Logistic Regression': Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression(random_state=42, max_iter=1000))
    ]),
    'Decision Tree': Pipeline([
        ('model', DecisionTreeClassifier(max_depth=5, random_state=42))
    ]),
    'Random Forest': Pipeline([
        ('model', RandomForestClassifier(n_estimators=100, random_state=42))
    ]),
    'KNN': Pipeline([
        ('scaler', StandardScaler()),
        ('model', KNeighborsClassifier(n_neighbors=best_k))
    ]),
    'SVM (RBF)': Pipeline([
        ('scaler', StandardScaler()),
        ('model', SVC(kernel='rbf', random_state=42))
    ]),
    'SVM (Linear)': Pipeline([
        ('scaler', StandardScaler()),
        ('model', SVC(kernel='linear', random_state=42))
    ])
}

# Cross-validation 5-fold stratified
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
results = {}

print("=== 5-Fold Stratified Cross-Validation ===\n")
print(f"{'Model':<22} {'Mean Acc':>10} {'Std':>8} {'Min':>8} {'Max':>8}")
print("-" * 58)

for name, pipeline in models.items():
    start_time = time.time()
    scores = cross_val_score(pipeline, X, y, cv=cv, scoring='accuracy')
    elapsed = time.time() - start_time

    results[name] = {
        'mean': scores.mean(),
        'std': scores.std(),
        'scores': scores,
        'time': elapsed
    }

    print(f"{name:<22} {scores.mean()*100:>9.1f}% {scores.std()*100:>7.1f}% "
          f"{scores.min()*100:>7.1f}% {scores.max()*100:>7.1f}%")

# Visualisasi boxplot
fig, ax = plt.subplots(figsize=(12, 6))
data_to_plot = [results[name]['scores'] * 100 for name in models.keys()]
bp = ax.boxplot(data_to_plot, labels=models.keys(), patch_artist=True)

colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC', '#99CCFF']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_ylabel('Accuracy (%)')
ax.set_title('Perbandingan Model Supervised Learning (5-Fold CV)')
ax.grid(True, alpha=0.3, axis='y')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
```

### Langkah 8: GridSearchCV untuk Model Terbaik

```python
# GridSearchCV untuk SVM (RBF)
pipeline_svm = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(random_state=42))
])

param_grid_svm = {
    'svm__C': [0.1, 1, 10, 100],
    'svm__gamma': ['scale', 'auto', 0.01, 0.1],
    'svm__kernel': ['rbf', 'linear']
}

grid_svm = GridSearchCV(
    pipeline_svm,
    param_grid_svm,
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

grid_svm.fit(X_train, y_train)

print(f"\n=== Hasil GridSearchCV (SVM) ===")
print(f"Best Parameters: {grid_svm.best_params_}")
print(f"Best Accuracy (CV): {grid_svm.best_score_*100:.1f}%")
print(f"\nAkurasi Testing: {grid_svm.score(X_test, y_test)*100:.1f}%")
print(f"\nClassification Report (Best SVM):")
y_pred_best_svm = grid_svm.predict(X_test)
print(classification_report(y_test, y_pred_best_svm,
      target_names=['Perlu Perbaikan', 'Kualitas Baik']))
```

### Langkah 9: GridSearchCV untuk KNN

```python
# GridSearchCV untuk KNN
pipeline_knn = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])

param_grid_knn = {
    'knn__n_neighbors': [3, 5, 7, 9, 11, 15, 21],
    'knn__weights': ['uniform', 'distance'],
    'knn__metric': ['euclidean', 'manhattan']
}

grid_knn = GridSearchCV(
    pipeline_knn,
    param_grid_knn,
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

grid_knn.fit(X_train, y_train)

print(f"\n=== Hasil GridSearchCV (KNN) ===")
print(f"Best Parameters: {grid_knn.best_params_}")
print(f"Best Accuracy (CV): {grid_knn.best_score_*100:.1f}%")
print(f"\nAkurasi Testing: {grid_knn.score(X_test, y_test)*100:.1f}%")
```

### Langkah 10: Rangkuman Perbandingan Akhir

```python
# Rangkuman akhir semua model
print("=" * 65)
print("RANGKUMAN PERBANDINGAN MODEL SUPERVISED LEARNING")
print("Dataset: Kualitas Pelayanan Rumah Sakit Indonesia")
print("=" * 65)

final_models = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    f'KNN (K={grid_knn.best_params_["knn__n_neighbors"]})': grid_knn.best_estimator_,
    f'SVM ({grid_svm.best_params_["svm__kernel"]})': grid_svm.best_estimator_
}

print(f"\n{'Model':<28} {'CV Accuracy':>12} {'Test Accuracy':>14} {'Training Time':>14}")
print("-" * 70)

for name, model in final_models.items():
    start = time.time()
    if 'KNN' in name or 'SVM' in name:
        # Pipeline sudah mengandung scaler
        cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
        model.fit(X_train, y_train)
        test_acc = model.score(X_test, y_test)
    else:
        cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='accuracy')
        model.fit(X_train_scaled, y_train)
        test_acc = model.score(X_test_scaled, y_test)
    elapsed = time.time() - start

    print(f"{name:<28} {cv_scores.mean()*100:>11.1f}% {test_acc*100:>13.1f}% {elapsed:>12.3f}s")
```

---

## AI Corner: Menggunakan AI untuk Memilih Algoritma yang Tepat

> **Level: Intermediate** -- Menggunakan AI sebagai asisten untuk memilih dan membandingkan algoritma ML berdasarkan karakteristik data dan kebutuhan bisnis.

### Cara AI Bisa Membantu

| Skenario | Contoh Prompt ke AI |
|---|---|
| Pemilihan algoritma | *"Saya punya dataset 10.000 baris, 20 fitur, target biner. Fitur campuran numerik dan kategorikal. Algoritma apa yang cocok?"* |
| Interpretasi cross-validation | *"CV scores saya: [0.82, 0.85, 0.78, 0.83, 0.81]. Apakah variansi ini normal? Model cukup stabil?"* |
| Tuning guidance | *"SVM saya dengan RBF kernel memberikan akurasi 70%. Apa yang harus saya tune terlebih dahulu: C atau gamma?"* |
| Diagnosis masalah | *"KNN saya sangat lambat untuk prediksi pada 100.000 data. Alternatif apa yang lebih cepat dengan akurasi serupa?"* |
| Feature engineering | *"Fitur apa yang relevan untuk memprediksi kualitas pelayanan rumah sakit di Indonesia?"* |

### Tips Penting

1. **Jelaskan konteks masalah** secara lengkap ke AI, termasuk ukuran data, tipe fitur, dan tujuan bisnis.
2. **Jangan langsung percaya** rekomendasi algoritma dari AI -- selalu validasi dengan eksperimen.
3. **Gunakan AI untuk memahami** trade-off, bukan untuk memilih jawaban final.
4. **Dokumentasikan** setiap interaksi AI dalam AI Usage Log.

### Contoh Prompt Minggu Ini

Coba masukkan prompt berikut ke ChatGPT atau Claude:

```
Saya membandingkan 5 algoritma supervised learning pada dataset
kualitas pelayanan rumah sakit (400 sampel, 7 fitur numerik).
Hasilnya:
- Logistic Regression: 78%
- Decision Tree: 75%
- Random Forest: 83%
- KNN (K=7): 80%
- SVM (RBF): 82%

1. Model mana yang sebaiknya dipilih dan mengapa?
2. Apakah perbedaan 83% vs 82% signifikan?
3. Untuk deployment di rumah sakit, faktor apa selain akurasi yang perlu dipertimbangkan?
4. Bagaimana menjelaskan model kepada stakeholder non-teknis (direktur RS)?
```

Bandingkan jawaban AI dengan analisis Anda dari praktikum.

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai bahan refleksi:

1. **KNN vs SVM:** Dalam skenario prediksi kualitas rumah sakit, jika Anda harus memilih antara KNN dan SVM, mana yang Anda pilih? Pertimbangkan akurasi, kecepatan, dan interpretabilitas.

2. **Curse of Dimensionality:** Mengapa KNN tidak cocok untuk data berdimensi tinggi (banyak fitur)? Jelaskan dengan kata-kata sendiri dan hubungkan dengan konsep jarak.

3. **No Free Lunch Theorem:** Apakah ada satu algoritma ML yang terbaik untuk semua masalah? Jelaskan mengapa setiap algoritma memiliki kekuatan dan kelemahan.

4. **Etika dalam Pelayanan Kesehatan:** Jika model AI digunakan untuk mengklasifikasikan kualitas rumah sakit, bagaimana memastikan hasilnya adil dan tidak merugikan rumah sakit di daerah terpencil yang memiliki keterbatasan sumber daya? Hubungkan dengan prinsip *La Dharar* (tidak merugikan).

5. **Cross-Validation:** Mengapa cross-validation lebih baik daripada single train-test split? Berikan analogi dari kehidupan sehari-hari.

---

## Tugas Mandiri: T4 -- Perbandingan Model Supervised Learning

### Deskripsi Tugas

Lakukan perbandingan komprehensif minimal **4 algoritma supervised learning** pada satu dataset konteks Indonesia.

### Langkah-langkah

1. **Pilih dataset** dari konteks Indonesia (boleh dari praktikum atau dataset baru):
   - Contoh: klasifikasi kelayakan kredit, prediksi kepuasan pelanggan, klasifikasi kualitas produk UMKM, prediksi lulus/tidak lulus ujian
2. **Preprocessing**: bersihkan data, normalisasi jika perlu, split data
3. **Latih minimal 4 model**: Logistic Regression, Decision Tree, Random Forest, KNN atau SVM
4. **Evaluasi dengan cross-validation**: 5-fold stratified
5. **Tuning**: gunakan GridSearchCV untuk minimal 2 model
6. **Analisis**: buat tabel perbandingan dan berikan rekomendasi model terbaik dengan alasan
7. **Visualisasi**: minimal 3 visualisasi (confusion matrix, perbandingan akurasi, feature importance)

### Kriteria Penilaian

| Komponen | Bobot |
|---|---|
| Kualitas dataset dan preprocessing | 15% |
| Implementasi model (minimal 4) | 25% |
| Cross-validation dan tuning | 20% |
| Analisis perbandingan dan rekomendasi | 20% |
| Visualisasi dan presentasi | 10% |
| AI Usage Log (jika menggunakan AI) | 10% |

### Format Pengumpulan

- File: Google Colab notebook (.ipynb)
- Deadline: Minggu 9 (setelah UTS)
- Naming: `T4_NIM_NamaLengkap.ipynb`

### Pengumuman Kuis

> **K2 Kuis: Supervised Learning** akan dilaksanakan pada minggu yang dijadwalkan. Materi mencakup seluruh topik Minggu 5-7: Regresi Linear & Logistik, Decision Tree & Random Forest, SVM & KNN, metrik evaluasi, dan cross-validation.

---

## Referensi

### Buku Teks

1. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer. -- Chapter 4 (KNN), Chapter 9 (SVM).
2. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media. -- Chapter 5 (SVM).
3. Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer. -- Chapter 7 (SVM).

### Sumber Online

4. [scikit-learn: KNeighborsClassifier](https://scikit-learn.org/stable/modules/neighbors.html) -- Dokumentasi resmi KNN.
5. [scikit-learn: Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html) -- Dokumentasi resmi SVM.
6. [scikit-learn: Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) -- Dokumentasi Pipeline.
7. [scikit-learn: Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) -- Dokumentasi cross-validation.

### Referensi Konteks Indonesia

8. Kementerian Kesehatan RI. Standar Pelayanan Minimal Rumah Sakit.
9. BPJS Kesehatan. Laporan Pengelolaan Program dan Laporan Keuangan.

---

> **Preview Minggu Depan:** Kita akan melakukan **UTS Review dan Ujian Tengah Semester** -- mencakup seluruh materi Minggu 1-7. Persiapkan diri dengan baik!

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
