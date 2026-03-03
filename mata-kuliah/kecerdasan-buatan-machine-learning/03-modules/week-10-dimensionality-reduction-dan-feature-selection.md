# Minggu 10: Dimensionality Reduction dan Feature Selection

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 10 |
| **Topik** | Dimensionality Reduction dan Feature Selection |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK-4: Menerapkan dan menganalisis algoritma unsupervised learning |
| **Sub-CPMK** | 10.1 Menganalisis teknik dimensionality reduction (PCA) dan dampaknya terhadap representasi data |
| | 10.2 Menganalisis dan membandingkan metode feature selection (filter, wrapper, embedded) untuk meningkatkan performa model |
| **Bloom's Taxonomy** | C4 (Menganalisis / *Analyze*) |
| **Durasi** | 2 x 100 menit (Teori 100 min + Praktikum 100 min) |
| **Platform** | Google Colab |
| **Metode** | Ceramah interaktif, demonstrasi, hands-on coding, diskusi |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** mengapa dimensi tinggi (*high dimensionality*) menjadi masalah dalam machine learning (*curse of dimensionality*).
2. **Menganalisis** cara kerja PCA (Principal Component Analysis) termasuk konsep eigenvalue, eigenvector, dan variance explained.
3. **Mengimplementasikan** PCA menggunakan scikit-learn untuk mereduksi dimensi dataset.
4. **Memvisualisasikan** data berdimensi tinggi dalam 2D/3D menggunakan PCA.
5. **Membandingkan** metode feature selection: filter (korelasi, variance threshold), wrapper (RFE), dan embedded (L1/Lasso).
6. **Menggabungkan** teknik dimensionality reduction dengan model klasifikasi atau clustering untuk meningkatkan performa.

---

## Materi Pembelajaran

### 1. Curse of Dimensionality: Mengapa Dimensi Penting

#### Masalah Dimensi Tinggi

Dalam dunia nyata, dataset seringkali memiliki banyak fitur (*features* atau *dimensions*). Misalnya:
- Data e-commerce: ratusan fitur perilaku pelanggan
- Data teks: ribuan kata unik (setelah TF-IDF)
- Data medis: ratusan variabel pemeriksaan

Ketika jumlah dimensi meningkat, terjadi beberapa masalah yang dikenal sebagai **Curse of Dimensionality**:

| Masalah | Penjelasan |
|---|---|
| **Data menjadi sparse** | Di dimensi tinggi, data tersebar sangat jarang — jarak antar titik cenderung sama |
| **Overfitting** | Model menghafal noise karena terlalu banyak fitur relatif terhadap jumlah sampel |
| **Komputasi lambat** | Waktu training meningkat eksponensial dengan jumlah fitur |
| **Visualisasi sulit** | Manusia hanya bisa memvisualisasikan 2D atau 3D |
| **Noise bertambah** | Fitur yang tidak relevan menambah noise dan mengurangi akurasi model |

```
Dimensi Rendah (2D):          Dimensi Tinggi (100D):
  Data tersebar padat           Data tersebar sangat jarang
  ● ● ● ●                      ●          ●
  ● ● ● ●                            ●
  ● ● ● ●                      ●               ●
  → Mudah menemukan pola        → Sulit menemukan pola
```

> **Aturan Praktis:** Untuk supervised learning, idealnya jumlah sampel minimal **5-10 kali** jumlah fitur. Jika Anda punya 100 fitur, idealnya punya 500-1000 sampel.

#### Dua Solusi Utama

1. **Dimensionality Reduction:** Membuat fitur baru yang lebih sedikit tapi menangkap informasi penting (contoh: PCA)
2. **Feature Selection:** Memilih subset fitur asli yang paling informatif

```
100 fitur asli
     │
     ├── Dimensionality Reduction (PCA)
     │   → 10 komponen baru (kombinasi linear dari 100 fitur asli)
     │
     └── Feature Selection
         → 15 fitur asli terpilih (subset dari 100 fitur)
```

---

### 2. PCA (Principal Component Analysis): Intuisi dan Teori

#### Intuisi PCA

Bayangkan Anda memiliki data 3D (seperti awan titik dalam ruang). **PCA** mencari arah (*direction*) di mana data paling bervariasi (*spread out*), lalu memproyeksikan data ke arah tersebut.

```
Data asli (2D):               Setelah PCA:
     y                             PC2
     |   /                          |
     |  / ●●●                       |  ●●●
     | / ●●●●                       | ●●●●
     |/ ●●●●●                       |●●●●●
     +--------x                     +--------PC1
                                    (arah variance terbesar)
```

**PCA menemukan sumbu-sumbu baru (Principal Components) yang:**
- Saling tegak lurus (*orthogonal*)
- PC1 menangkap variance terbesar
- PC2 menangkap variance terbesar berikutnya (tegak lurus PC1)
- dan seterusnya...

#### Konsep Matematika (Disederhanakan)

1. **Standardisasi** data (mean=0, std=1)
2. Hitung **covariance matrix** dari data
3. Hitung **eigenvalues** dan **eigenvectors** dari covariance matrix
4. Eigenvalues menunjukkan **berapa banyak variance** yang ditangkap setiap PC
5. Eigenvectors menunjukkan **arah** setiap PC
6. Urutkan berdasarkan eigenvalue terbesar
7. Pilih **k** komponen pertama yang menangkap cukup variance

#### Variance Explained

**Variance explained ratio** menunjukkan proporsi informasi yang ditangkap oleh setiap principal component:

```
PC1: 45% variance  ████████████████████
PC2: 25% variance  ██████████████
PC3: 15% variance  ████████
PC4:  8% variance  ████
PC5:  5% variance  ███
PC6:  2% variance  █

Kumulatif: PC1+PC2 = 70%, PC1+PC2+PC3 = 85%
→ Dengan 3 komponen, kita menangkap 85% informasi dari 6 fitur asli!
```

> **Aturan Praktis:** Pilih jumlah komponen yang menangkap **80-95%** total variance.

---

### 3. Implementasi PCA dengan scikit-learn

PCA di scikit-learn sangat mudah digunakan:

```python
from sklearn.decomposition import PCA

# Langkah 1: Standardisasi (WAJIB sebelum PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Langkah 2: Fit PCA
pca = PCA(n_components=2)  # Reduksi ke 2 dimensi
X_pca = pca.fit_transform(X_scaled)

# Langkah 3: Lihat variance explained
print(f"Variance explained: {pca.explained_variance_ratio_}")
print(f"Total variance explained: {sum(pca.explained_variance_ratio_):.2%}")
```

**Parameter penting:**
- `n_components=2` — Jumlah komponen yang diinginkan
- `n_components=0.95` — Pilih jumlah komponen yang menangkap 95% variance
- `n_components=None` — Hitung semua komponen (untuk analisis)

---

### 4. Visualisasi Data Berdimensi Tinggi dengan PCA

#### Mengapa Visualisasi Penting?

Data dengan 10, 50, atau 100 fitur tidak bisa divisualisasikan secara langsung. PCA memungkinkan kita memproyeksikan data ke 2D atau 3D untuk:
- **Melihat pola** dan cluster dalam data
- **Mengidentifikasi outlier**
- **Memahami separabilitas** kelas
- **Komunikasi** hasil analisis kepada stakeholder

#### Contoh Penggunaan

Iris dataset memiliki 4 fitur (sepal length, sepal width, petal length, petal width). Dengan PCA, kita bisa melihat tiga species iris dalam 2D:

```
PC2
 |    ○○○○
 |   ○○○○○        △△△△
 |   ○○○○      △△△△△△
 |              △△△△△
 |                    ■■■■
 |                  ■■■■■■
 |                  ■■■■■
 +-----------------------------PC1
  ○ Setosa  △ Versicolor  ■ Virginica
```

---

### 5. Feature Selection: Filter, Wrapper, dan Embedded

#### Mengapa Feature Selection?

Berbeda dengan PCA yang membuat fitur baru, **feature selection** memilih fitur asli yang paling penting. Keuntungannya:
- **Interpretabilitas:** Fitur terpilih masih memiliki makna asli
- **Kecepatan:** Mengurangi waktu training
- **Overfitting:** Mengurangi risiko overfitting
- **Domain knowledge:** Hasil bisa divalidasi oleh ahli domain

#### a) Filter Methods

Filter methods mengevaluasi fitur **secara independen** dari model ML:

| Metode | Deskripsi | Kapan Digunakan |
|---|---|---|
| **Variance Threshold** | Hapus fitur dengan variance rendah | Fitur yang hampir konstan |
| **Correlation** | Hapus fitur yang berkorelasi tinggi satu sama lain | Fitur redundan |
| **Chi-Square** | Uji hubungan fitur kategorikal dengan target | Klasifikasi dengan fitur kategorikal |
| **Mutual Information** | Ukur dependensi non-linear fitur dengan target | Umum, fleksibel |

```python
# Contoh: Variance Threshold
from sklearn.feature_selection import VarianceThreshold
selector = VarianceThreshold(threshold=0.01)  # Hapus fitur variance < 0.01
X_selected = selector.fit_transform(X)
```

#### b) Wrapper Methods

Wrapper methods mengevaluasi subset fitur menggunakan **performa model** sebagai kriteria:

| Metode | Deskripsi | Kelebihan | Kekurangan |
|---|---|---|---|
| **RFE** (Recursive Feature Elimination) | Hapus fitur terlemah secara iteratif | Mempertimbangkan interaksi fitur | Komputasi mahal |
| **Forward Selection** | Tambahkan fitur terbaik satu per satu | Sederhana | Bisa terjebak di lokal optimal |
| **Backward Elimination** | Hapus fitur terburuk satu per satu | Dimulai dari semua fitur | Komputasi mahal untuk banyak fitur |

```python
# Contoh: RFE (Recursive Feature Elimination)
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
rfe = RFE(estimator=model, n_features_to_select=5)
X_rfe = rfe.fit_transform(X, y)
print(f"Fitur terpilih: {rfe.support_}")
print(f"Ranking fitur: {rfe.ranking_}")
```

#### c) Embedded Methods

Embedded methods melakukan feature selection **selama proses training** model:

| Metode | Deskripsi |
|---|---|
| **L1 Regularization (Lasso)** | Membuat koefisien fitur tidak penting menjadi nol |
| **Tree-based Feature Importance** | Decision Tree/Random Forest memberikan skor pentingnya fitur |
| **ElasticNet** | Kombinasi L1 dan L2 regularization |

```
Filter:    Fitur → [Evaluasi Statistik] → Fitur Terpilih → Model
Wrapper:   Fitur → [Model sebagai evaluator] → Fitur Terpilih
Embedded:  Fitur → [Model + Seleksi bersama] → Fitur Terpilih + Model
```

---

### 6. Feature Importance dari Tree Models

**Random Forest** dan **Gradient Boosting** secara otomatis menghitung skor pentingnya setiap fitur berdasarkan seberapa banyak fitur tersebut mengurangi impurity (Gini atau entropy) pada node-node pohon.

```python
# Feature importance dari Random Forest
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Ambil feature importance
importances = model.feature_importances_
```

**Interpretasi:**
- Skor tinggi = fitur sangat penting untuk prediksi
- Skor rendah = fitur kurang berpengaruh
- **Hati-hati:** Feature importance bisa bias terhadap fitur dengan banyak kategori atau nilai unik

---

### 7. Menggabungkan Dimensionality Reduction dengan Klasifikasi/Clustering

#### Pipeline: PCA + Klasifikasi

```
Data asli (100 fitur)
    │
    ▼
StandardScaler (standardisasi)
    │
    ▼
PCA (reduksi ke 20 komponen)
    │
    ▼
Classifier (SVM, Random Forest, dll.)
    │
    ▼
Prediksi
```

Keuntungan menggabungkan PCA dengan model:
- **Mengurangi noise** dan overfitting
- **Mempercepat** training secara signifikan
- **Mengatasi** multikolinearitas antar fitur

#### Pipeline: PCA + Clustering

PCA juga sangat berguna sebagai preprocessing sebelum clustering:
- Mereduksi dimensi agar algoritma jarak (*distance-based*) bekerja lebih baik
- Memungkinkan visualisasi hasil clustering
- Menghilangkan fitur noise yang mengganggu clustering

---

## Aktivitas Kelas

### Sesi 1: Teori dan Diskusi (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Pembukaan & Review | Review clustering minggu lalu, transisi ke dimensionality reduction |
| 20 menit | Ceramah: Curse of Dimensionality & PCA | Masalah dimensi tinggi, intuisi PCA, eigenvalues |
| 15 menit | Ceramah: Variance Explained & Visualisasi | Cara menentukan jumlah komponen, contoh visual |
| 20 menit | Ceramah: Feature Selection Methods | Filter, wrapper, embedded — perbandingan |
| 15 menit | Ceramah: Feature Importance & Pipeline | Tree-based importance, menggabungkan PCA dengan model |
| 10 menit | Diskusi Kelompok | Kapan menggunakan PCA vs feature selection? |
| 10 menit | Rangkuman & Transisi | Key takeaways, persiapan hands-on |

### Sesi 2: Hands-on Praktikum (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Setup & Load Data | Buka Google Colab, import libraries, load datasets |
| 25 menit | PCA pada Iris Dataset | Implementasi PCA, scree plot, visualisasi 2D |
| 25 menit | Feature Selection dengan RFE | RFE dengan Random Forest, perbandingan fitur |
| 20 menit | Pipeline: PCA + Classifier | Membandingkan akurasi dengan dan tanpa PCA |
| 10 menit | Eksplorasi & Eksperimen | Mahasiswa mencoba variasi parameter |
| 10 menit | Wrap-up & Preview | Rangkuman, preview minggu depan |

---

## Hands-on: PCA dan Feature Selection

### Langkah 1: Import Library dan Persiapan

```python
# Import library yang diperlukan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, load_wine
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.feature_selection import RFE, VarianceThreshold, SelectKBest, f_classif
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

# Mengatur style visualisasi
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
print("Library berhasil di-import!")
```

### Langkah 2: Load dan Eksplorasi Dataset

```python
# Load Iris dataset
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
feature_names_iris = iris.feature_names
target_names_iris = iris.target_names

print("=== Iris Dataset ===")
print(f"Jumlah sampel: {X_iris.shape[0]}")
print(f"Jumlah fitur: {X_iris.shape[1]}")
print(f"Nama fitur: {feature_names_iris}")
print(f"Kelas: {target_names_iris}")

# Load Wine dataset (lebih banyak fitur)
wine = load_wine()
X_wine = wine.data
y_wine = wine.target
feature_names_wine = wine.feature_names

print(f"\n=== Wine Dataset ===")
print(f"Jumlah sampel: {X_wine.shape[0]}")
print(f"Jumlah fitur: {X_wine.shape[1]}")
print(f"Nama fitur: {feature_names_wine}")
print(f"Kelas: {wine.target_names}")
```

### Langkah 3: PCA pada Iris Dataset — Visualisasi 2D

```python
# Standardisasi data (WAJIB sebelum PCA!)
scaler = StandardScaler()
X_iris_scaled = scaler.fit_transform(X_iris)

# PCA: reduksi dari 4 fitur ke 2 komponen
pca_iris = PCA(n_components=2)
X_iris_pca = pca_iris.fit_transform(X_iris_scaled)

print("=== Hasil PCA pada Iris ===")
print(f"Dimensi asli: {X_iris.shape[1]} fitur")
print(f"Dimensi setelah PCA: {X_iris_pca.shape[1]} komponen")
print(f"Variance explained ratio: {pca_iris.explained_variance_ratio_}")
print(f"Total variance explained: {sum(pca_iris.explained_variance_ratio_):.2%}")

# Visualisasi PCA 2D
plt.figure(figsize=(10, 7))
colors = ['#e74c3c', '#2ecc71', '#3498db']
for i, (target, color) in enumerate(zip(target_names_iris, colors)):
    mask = y_iris == i
    plt.scatter(X_iris_pca[mask, 0], X_iris_pca[mask, 1],
                c=color, label=target, alpha=0.7,
                edgecolors='black', linewidth=0.5, s=80)

plt.xlabel(f'PC1 ({pca_iris.explained_variance_ratio_[0]:.1%} variance)', fontsize=12)
plt.ylabel(f'PC2 ({pca_iris.explained_variance_ratio_[1]:.1%} variance)', fontsize=12)
plt.title('PCA: Iris Dataset dalam 2D', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\nInterpretasi: Dengan hanya 2 komponen, kita bisa melihat bahwa")
print("Setosa terpisah jelas dari Versicolor dan Virginica.")
```

### Langkah 4: Scree Plot dan Kumulatif Variance — Wine Dataset

```python
# PCA pada Wine dataset (13 fitur → berapa komponen cukup?)
X_wine_scaled = scaler.fit_transform(X_wine)

# Fit PCA dengan semua komponen untuk analisis
pca_wine_full = PCA()
pca_wine_full.fit(X_wine_scaled)

# Scree plot dan kumulatif variance
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Scree plot (individual variance)
axes[0].bar(range(1, len(pca_wine_full.explained_variance_ratio_) + 1),
            pca_wine_full.explained_variance_ratio_,
            alpha=0.7, color='steelblue', edgecolor='black')
axes[0].set_xlabel('Principal Component', fontsize=12)
axes[0].set_ylabel('Variance Explained Ratio', fontsize=12)
axes[0].set_title('Scree Plot — Wine Dataset', fontsize=13)
axes[0].set_xticks(range(1, 14))

# Kumulatif variance
cumulative_var = np.cumsum(pca_wine_full.explained_variance_ratio_)
axes[1].plot(range(1, len(cumulative_var) + 1), cumulative_var,
             'ro-', linewidth=2, markersize=8)
axes[1].axhline(y=0.80, color='green', linestyle='--', label='80% threshold')
axes[1].axhline(y=0.95, color='orange', linestyle='--', label='95% threshold')
axes[1].set_xlabel('Jumlah Komponen', fontsize=12)
axes[1].set_ylabel('Kumulatif Variance Explained', fontsize=12)
axes[1].set_title('Kumulatif Variance Explained', fontsize=13)
axes[1].set_xticks(range(1, 14))
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Berapa komponen untuk 80% dan 95%?
for threshold in [0.80, 0.95]:
    n_comp = np.argmax(cumulative_var >= threshold) + 1
    print(f"Untuk {threshold:.0%} variance: butuh {n_comp} komponen "
          f"(dari 13 fitur asli)")
```

### Langkah 5: Feature Selection dengan RFE

```python
# Recursive Feature Elimination (RFE) pada Wine dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_wine_scaled, y_wine, test_size=0.3, random_state=42
)

# Model dasar: Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# RFE: pilih 5 fitur terbaik
rfe = RFE(estimator=rf_model, n_features_to_select=5, step=1)
rfe.fit(X_train, y_train)

# Tampilkan fitur terpilih
print("=== Hasil RFE (5 Fitur Terpilih) ===\n")
for i, (name, selected, rank) in enumerate(
    zip(feature_names_wine, rfe.support_, rfe.ranking_)
):
    status = "TERPILIH" if selected else f"rank {rank}"
    print(f"  {name:30s} → {status}")

# Evaluasi: model dengan semua fitur vs fitur terpilih
rf_all = RandomForestClassifier(n_estimators=100, random_state=42)
rf_all.fit(X_train, y_train)
acc_all = accuracy_score(y_test, rf_all.predict(X_test))

rf_rfe = RandomForestClassifier(n_estimators=100, random_state=42)
X_train_rfe = rfe.transform(X_train)
X_test_rfe = rfe.transform(X_test)
rf_rfe.fit(X_train_rfe, y_train)
acc_rfe = accuracy_score(y_test, rf_rfe.predict(X_test_rfe))

print(f"\n=== Perbandingan Akurasi ===")
print(f"Semua 13 fitur: {acc_all:.4f}")
print(f"5 fitur (RFE):  {acc_rfe:.4f}")
print(f"Pengurangan fitur: {13-5} fitur ({(13-5)/13:.0%})")
```

### Langkah 6: Feature Importance dari Random Forest

```python
# Feature importance dari Random Forest
rf_full = RandomForestClassifier(n_estimators=100, random_state=42)
rf_full.fit(X_wine_scaled, y_wine)

# Visualisasi feature importance
importances = rf_full.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(12, 6))
plt.bar(range(len(importances)), importances[indices],
        alpha=0.8, color='steelblue', edgecolor='black')
plt.xticks(range(len(importances)),
           [feature_names_wine[i] for i in indices],
           rotation=45, ha='right')
plt.xlabel('Fitur', fontsize=12)
plt.ylabel('Importance Score', fontsize=12)
plt.title('Feature Importance — Random Forest (Wine Dataset)', fontsize=14)
plt.tight_layout()
plt.show()

# Tampilkan ranking
print("\n=== Ranking Feature Importance ===")
for rank, idx in enumerate(indices, 1):
    print(f"  {rank:2d}. {feature_names_wine[idx]:30s} — {importances[idx]:.4f}")
```

### Langkah 7: Pipeline — PCA + Classifier

```python
# Membandingkan performa dengan dan tanpa PCA
from sklearn.pipeline import Pipeline

# Pipeline 1: Tanpa PCA (semua 13 fitur)
pipe_no_pca = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', SVC(kernel='rbf', random_state=42))
])

# Pipeline 2: Dengan PCA (5 komponen)
pipe_pca5 = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=5)),
    ('classifier', SVC(kernel='rbf', random_state=42))
])

# Pipeline 3: Dengan PCA (95% variance)
pipe_pca95 = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=0.95)),
    ('classifier', SVC(kernel='rbf', random_state=42))
])

# Cross-validation untuk evaluasi fair
print("=== Perbandingan Pipeline (5-Fold CV) ===\n")
pipelines = {
    'Tanpa PCA (13 fitur)': pipe_no_pca,
    'PCA (5 komponen)': pipe_pca5,
    'PCA (95% variance)': pipe_pca95
}

results = {}
for name, pipe in pipelines.items():
    scores = cross_val_score(pipe, X_wine, y_wine, cv=5, scoring='accuracy')
    results[name] = scores
    print(f"{name:25s}: {scores.mean():.4f} (+/- {scores.std():.4f})")

# Visualisasi perbandingan
plt.figure(figsize=(10, 5))
plt.boxplot(results.values(), labels=results.keys())
plt.ylabel('Accuracy', fontsize=12)
plt.title('Perbandingan Performa: Dengan vs Tanpa PCA', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 8: Perbandingan Metode Feature Selection

```python
# Perbandingan berbagai metode feature selection
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif

n_features_select = 5

# Metode 1: SelectKBest dengan F-statistic (filter)
skb_f = SelectKBest(f_classif, k=n_features_select)
skb_f.fit(X_wine_scaled, y_wine)
selected_f = [feature_names_wine[i] for i in np.where(skb_f.get_support())[0]]

# Metode 2: SelectKBest dengan Mutual Information (filter)
skb_mi = SelectKBest(mutual_info_classif, k=n_features_select)
skb_mi.fit(X_wine_scaled, y_wine)
selected_mi = [feature_names_wine[i] for i in np.where(skb_mi.get_support())[0]]

# Metode 3: RFE (wrapper) — sudah dihitung sebelumnya
selected_rfe = [feature_names_wine[i] for i in np.where(rfe.support_)[0]]

# Metode 4: Feature importance (embedded)
top_indices = np.argsort(importances)[::-1][:n_features_select]
selected_imp = [feature_names_wine[i] for i in top_indices]

print("=== Perbandingan Feature Selection (Top 5) ===\n")
print(f"{'F-Statistic':20s}: {selected_f}")
print(f"{'Mutual Info':20s}: {selected_mi}")
print(f"{'RFE':20s}: {selected_rfe}")
print(f"{'RF Importance':20s}: {selected_imp}")

# Evaluasi akurasi masing-masing metode
print("\n=== Akurasi dengan Fitur Terpilih (5-Fold CV) ===\n")
methods = {
    'Semua fitur (13)': X_wine_scaled,
    'F-Statistic (5)': skb_f.transform(X_wine_scaled),
    'Mutual Info (5)': skb_mi.transform(X_wine_scaled),
    'RFE (5)': rfe.transform(X_wine_scaled),
}

for name, X_selected in methods.items():
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    scores = cross_val_score(rf, X_selected, y_wine, cv=5, scoring='accuracy')
    print(f"  {name:20s}: {scores.mean():.4f} (+/- {scores.std():.4f})")
```

---

## AI Corner: Menggunakan AI untuk Seleksi Fitur

> **Level: Advanced** — Pada minggu ini, kita menggunakan AI untuk membantu keputusan strategis tentang fitur mana yang penting.

### Skenario Penggunaan AI dalam Feature Selection

| Skenario | Contoh Prompt ke AI |
|---|---|
| Memahami PCA | *"Jelaskan dengan analogi sederhana apa itu PCA dan bagaimana cara kerjanya. Saya mahasiswa S1 Informatika."* |
| Interpretasi variance | *"Scree plot saya menunjukkan PC1=35%, PC2=20%, PC3=12%. Berapa komponen yang sebaiknya saya pilih dan mengapa?"* |
| Memilih metode | *"Dataset saya punya 50 fitur numerik dan 5000 sampel untuk klasifikasi 3 kelas. Sebaiknya saya pakai PCA atau feature selection? Mengapa?"* |
| Domain knowledge | *"Berikut 13 fitur dari data wine [daftar fitur]. Dari perspektif domain knowledge, mana yang paling relevan untuk klasifikasi jenis wine?"* |
| Debugging | *"PCA saya hanya menangkap 30% variance di PC1. Apakah ini normal? Apa yang bisa saya lakukan?"* |

### Contoh Prompt Minggu Ini

```
Saya memiliki dataset dengan 50 fitur dan 1000 sampel untuk masalah
klasifikasi (3 kelas). Saya melakukan:
1. PCA → dengan 10 komponen menangkap 92% variance
2. RFE → memilih 15 fitur terbaik
3. Random Forest feature importance → top 15 fitur

Pertanyaan:
1. Pendekatan mana yang lebih baik untuk kasus saya?
2. Kapan saya harus memilih PCA vs feature selection?
3. Apakah saya bisa menggabungkan keduanya? Bagaimana?
4. Apa trade-off antara interpretabilitas dan performa?
```

### Tips Penting

1. **PCA vs Feature Selection bukan pilihan mutlak** — tergantung tujuan analisis.
2. **Jika interpretabilitas penting** (misalnya untuk presentasi ke manajemen), gunakan feature selection.
3. **Jika performa model yang utama**, PCA seringkali lebih baik karena menangkap informasi dari semua fitur.
4. **AI bisa membantu** memilih metode, tapi keputusan akhir harus berdasarkan pemahaman data dan konteks bisnis.

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai bahan refleksi:

1. **Curse of Dimensionality:** Berikan contoh nyata dari industri di Indonesia di mana curse of dimensionality menjadi masalah. Bagaimana Anda akan mengatasinya?

2. **PCA vs Feature Selection:** Seorang data scientist di bank Indonesia ingin membangun model credit scoring. Apakah sebaiknya menggunakan PCA atau feature selection? Pertimbangkan aspek regulasi dan interpretabilitas.

3. **Variance Explained:** Jika PCA menangkap 70% variance dengan 2 komponen dari 20 fitur asli, apakah cukup? Dalam kondisi apa ini cukup dan tidak cukup?

4. **Etika dan Transparansi:** Regulasi perbankan (OJK) mengharuskan model kredit bisa dijelaskan (*explainable AI*). Bagaimana PCA bisa menjadi hambatan dalam konteks ini? Apa alternatifnya?

5. **Praktis vs Teoritis:** Dalam pengalaman hands-on hari ini, apakah PCA selalu meningkatkan performa model? Mengapa atau mengapa tidak?

---

## Referensi

### Buku Teks

1. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media. — Chapter 8: Dimensionality Reduction.
2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer. — Chapter 12.2: Principal Components Analysis.
3. Müller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*. O'Reilly Media. — Chapter 4: Feature Engineering.

### Sumber Online

4. [scikit-learn: Decomposition](https://scikit-learn.org/stable/modules/decomposition.html) — Dokumentasi PCA di scikit-learn.
5. [scikit-learn: Feature Selection](https://scikit-learn.org/stable/modules/feature_selection.html) — Panduan lengkap feature selection.
6. [StatQuest: PCA Step-by-Step](https://www.youtube.com/watch?v=FgakZw6K1QQ) — Video penjelasan PCA yang sangat jelas.

### Referensi Indonesia

7. Data BPS — Badan Pusat Statistik Indonesia. [https://www.bps.go.id/](https://www.bps.go.id/)

---

> **Preview Minggu Depan:** Kita akan membahas **Neural Networks dan Deep Learning Dasar** — memahami perceptron, multi-layer perceptron, backpropagation, dan membangun neural network pertama dengan TensorFlow/Keras.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
