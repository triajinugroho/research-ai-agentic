# BAB 9: DIMENSIONALITY REDUCTION DAN FEATURE SELECTION

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| Sub-CPMK 10.1 | Menganalisis dampak curse of dimensionality dan menerapkan PCA untuk mereduksi dimensi data | C4 |
| Sub-CPMK 10.2 | Menganalisis dan membandingkan metode feature selection (filter, wrapper, embedded) untuk memilih fitur optimal | C4 |

**CPMK-4:** Menganalisis data menggunakan algoritma unsupervised learning dan teknik reduksi dimensi.

---

## Estimasi Waktu

| Komponen | Durasi |
|----------|--------|
| Membaca materi | 90 menit |
| Praktik kode Python | 60 menit |
| Latihan soal | 45 menit |
| **Total** | **195 menit** |

---

## Prasyarat

- Pemahaman dasar aljabar linear: matriks, vektor, eigenvalue (Bab 3)
- Konsep preprocessing dan feature engineering (Bab 4)
- Supervised learning dan evaluasi model (Bab 5-7)
- Unsupervised learning: clustering (Bab 8)

---

## 9.1 Curse of Dimensionality

### 9.1.1 Apa itu Curse of Dimensionality?

**Curse of dimensionality** (kutukan dimensi) adalah fenomena di mana performa algoritma machine learning **menurun** ketika jumlah fitur (dimensi) terlalu banyak relatif terhadap jumlah sampel data.

**Masalah utama:**

| Masalah | Deskripsi | Dampak |
|---------|-----------|--------|
| **Sparsity** | Data menjadi sangat jarang di ruang berdimensi tinggi | Model sulit menemukan pola |
| **Jarak menjadi tidak bermakna** | Semua titik hampir sama jauhnya satu sama lain | K-Means, KNN gagal |
| **Overfitting** | Model terlalu banyak parameter relatif terhadap data | Generalisasi buruk |
| **Komputasi mahal** | Waktu dan memori meningkat eksponensial | Training lambat |

```
Dimensi 1D:  |----*--*-*---*----|  (data relatif rapat)
              0                 10

Dimensi 2D:  10|      *
               |  *       *
               |     *
               |            *
              0|________________
               0              10
              (data mulai menyebar)

Dimensi 3D+ : data semakin sparse, "jarak terjauh ≈ jarak terdekat"
```

### 9.1.2 Demonstrasi dengan Python

```python
import numpy as np
import matplotlib.pyplot as plt

# Demonstrasi: rasio jarak max/min meningkat lambat seiring dimensi
np.random.seed(42)
n_sampel = 100
dimensi_list = [2, 5, 10, 20, 50, 100, 500, 1000]

rasio_jarak = []
for d in dimensi_list:
    # Data acak berdimensi d
    data = np.random.uniform(0, 1, (n_sampel, d))

    # Hitung semua pasangan jarak
    from sklearn.metrics import pairwise_distances
    dists = pairwise_distances(data).flatten()
    dists = dists[dists > 0]  # Buang jarak 0 (diagonal)

    rasio = np.max(dists) / np.min(dists)
    rasio_jarak.append(rasio)
    print(f"Dimensi {d:4d}: max/min rasio = {rasio:.2f}, "
          f"std/mean = {np.std(dists)/np.mean(dists):.4f}")

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(dimensi_list, rasio_jarak, 'bo-', linewidth=2)
ax.set_xlabel('Jumlah Dimensi', fontsize=12)
ax.set_ylabel('Rasio Jarak (max/min)', fontsize=12)
ax.set_title('Curse of Dimensionality: Jarak Menjadi Kurang Bermakna', fontsize=14)
ax.set_xscale('log')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('curse_of_dimensionality.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 9.1.3 Solusi: Reduksi Dimensi

Ada dua pendekatan utama untuk mengatasi curse of dimensionality:

```
                    MENGURANGI DIMENSI
                          │
              ┌───────────┴───────────┐
              │                       │
      FEATURE SELECTION         FEATURE EXTRACTION
      (Pilih fitur asli)        (Buat fitur baru)
              │                       │
    ┌─────────┼─────────┐            │
    │         │         │            │
  Filter   Wrapper  Embedded       PCA, t-SNE,
  (corr,   (RFE)    (L1/Lasso,    UMAP, Autoencoder
  variance)          tree-based)
```

---

## 9.2 PCA (Principal Component Analysis)

### 9.2.1 Intuisi: Arah Variansi Maksimum

**PCA** adalah teknik feature extraction yang mentransformasi data ke **koordinat baru** (principal components) yang menangkap variansi data secara berurutan dari yang terbesar.

**Analogi sederhana:**

> Bayangkan Anda memotret sekumpulan buah di atas meja dari berbagai sudut. Sudut mana yang paling "informatif"? Sudut yang menunjukkan **perbedaan paling besar** antar buah. Itulah principal component pertama (PC1). Sudut tegak lurus berikutnya yang masih informatif adalah PC2, dan seterusnya.

```
Data asli (2D):               Setelah PCA:
  y                            PC2
  |    * *                      |
  |   *   * *                   |  *  *
  |  *  *   *                   |*  * *  *
  | *  *  *                     |_*__*_________ PC1
  |______________x              (PC1 menangkap variansi terbesar)
```

### 9.2.2 Matematika: Covariance Matrix dan Eigendecomposition

**Langkah-langkah PCA secara matematis:**

1. **Standardisasi** data (mean=0, std=1)
2. Hitung **covariance matrix** $C = \frac{1}{n-1} X^T X$
3. Hitung **eigenvalue** ($\lambda$) dan **eigenvector** ($v$) dari $C$
4. Urutkan eigenvector berdasarkan eigenvalue (terbesar dahulu)
5. Pilih **k** eigenvector teratas sebagai principal components
6. Transformasi data: $X_{new} = X \cdot V_k$

```python
import numpy as np

# Demonstrasi PCA manual
np.random.seed(42)

# Buat data 2D yang berkorelasi
n = 200
x1 = np.random.normal(0, 2, n)
x2 = 0.8 * x1 + np.random.normal(0, 1, n)  # x2 berkorelasi dengan x1
X = np.column_stack([x1, x2])

# Langkah 1: Standardisasi (pusatkan ke mean 0)
X_centered = X - X.mean(axis=0)

# Langkah 2: Hitung covariance matrix
cov_matrix = np.cov(X_centered.T)
print("Covariance Matrix:")
print(cov_matrix.round(3))

# Langkah 3: Eigendecomposition
eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

# Urutkan dari eigenvalue terbesar
idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print(f"\nEigenvalues: {eigenvalues.round(3)}")
print(f"Eigenvectors:\n{eigenvectors.round(3)}")

# Explained variance ratio
explained_var = eigenvalues / eigenvalues.sum()
print(f"\nExplained variance ratio: {explained_var.round(4)}")
print(f"PC1 menjelaskan {explained_var[0]*100:.1f}% variansi data")

# Langkah 4: Transformasi
X_pca = X_centered @ eigenvectors
```

### 9.2.3 PCA dengan scikit-learn

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

# Muat dataset Iris (4 fitur → reduksi ke 2)
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
nama_fitur = iris.feature_names
nama_kelas = iris.target_names

print(f"Dimensi asli: {X_iris.shape}")  # (150, 4)

# Standardisasi
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_iris)

# Terapkan PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"Dimensi setelah PCA: {X_pca.shape}")  # (150, 2)
print(f"\nExplained variance ratio: {pca.explained_variance_ratio_.round(4)}")
print(f"Total explained variance: {pca.explained_variance_ratio_.sum()*100:.1f}%")
print(f"\nComponents (loading matrix):")

# Loading matrix: kontribusi fitur asli ke setiap PC
loading_df = pd.DataFrame(
    pca.components_.T,
    columns=['PC1', 'PC2'],
    index=nama_fitur
)
print(loading_df.round(4))
```

### 9.2.4 Scree Plot dan Explained Variance Ratio

```python
# PCA dengan semua komponen untuk scree plot
pca_full = PCA()
pca_full.fit(X_scaled)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Scree plot
axes[0].bar(range(1, 5), pca_full.explained_variance_ratio_, alpha=0.7, color='steelblue')
axes[0].set_xlabel('Principal Component')
axes[0].set_ylabel('Explained Variance Ratio')
axes[0].set_title('Scree Plot')
axes[0].set_xticks(range(1, 5))
axes[0].grid(True, alpha=0.3, axis='y')

# Tambahkan persentase di atas bar
for i, v in enumerate(pca_full.explained_variance_ratio_):
    axes[0].text(i+1, v+0.01, f'{v*100:.1f}%', ha='center', fontsize=11)

# Cumulative explained variance
cum_var = np.cumsum(pca_full.explained_variance_ratio_)
axes[1].plot(range(1, 5), cum_var, 'ro-', linewidth=2)
axes[1].axhline(y=0.95, color='gray', linestyle='--', label='95% threshold')
axes[1].set_xlabel('Jumlah Principal Components')
axes[1].set_ylabel('Cumulative Explained Variance')
axes[1].set_title('Cumulative Explained Variance')
axes[1].set_xticks(range(1, 5))
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('scree_plot.png', dpi=150, bbox_inches='tight')
plt.show()

# Berapa komponen untuk 95% variansi?
n_95 = np.argmax(cum_var >= 0.95) + 1
print(f"Jumlah komponen untuk >= 95% variansi: {n_95}")
```

### 9.2.5 Visualisasi Data Berdimensi Tinggi dalam 2D

```python
# Visualisasi Iris dataset dalam 2D dengan PCA
fig, ax = plt.subplots(figsize=(10, 7))

warna = ['#FF6B6B', '#4ECDC4', '#45B7D1']
for i, kelas in enumerate(nama_kelas):
    mask = y_iris == i
    ax.scatter(
        X_pca[mask, 0], X_pca[mask, 1],
        c=warna[i], label=kelas,
        alpha=0.7, edgecolors='w', s=60
    )

ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)', fontsize=12)
ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)', fontsize=12)
ax.set_title('Iris Dataset — PCA Projection (4D → 2D)', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('pca_iris_2d.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## 9.3 Feature Selection Methods

### 9.3.1 Filter Methods

Filter methods memilih fitur berdasarkan **properti statistik** tanpa melibatkan model ML. Metode ini cepat dan tidak bergantung pada algoritma tertentu.

**A. Variance Threshold — Buang fitur dengan variansi rendah:**

```python
from sklearn.feature_selection import VarianceThreshold
import numpy as np
import pandas as pd

# Contoh: dataset dengan fitur variansi rendah
np.random.seed(42)
df_fitur = pd.DataFrame({
    'fitur_aktif': np.random.normal(50, 10, 200),   # Variansi tinggi
    'fitur_konstan': np.full(200, 3.14),             # Variansi 0
    'fitur_low_var': np.random.normal(100, 0.01, 200),  # Variansi sangat rendah
    'fitur_berguna': np.random.normal(25, 5, 200),   # Variansi cukup
})

print("Variansi setiap fitur:")
print(df_fitur.var().round(4))

# Terapkan VarianceThreshold
selector = VarianceThreshold(threshold=0.1)
X_selected = selector.fit_transform(df_fitur)

fitur_terpilih = df_fitur.columns[selector.get_support()]
print(f"\nFitur terpilih: {list(fitur_terpilih)}")
print(f"Dimensi: {df_fitur.shape[1]} → {X_selected.shape[1]}")
```

**B. Correlation-based — Buang fitur yang sangat berkorelasi:**

```python
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

# Muat dataset breast cancer
cancer = load_breast_cancer()
df_cancer = pd.DataFrame(cancer.data, columns=cancer.feature_names)

# Hitung correlation matrix
corr_matrix = df_cancer.corr().abs()

# Visualisasi
fig, ax = plt.subplots(figsize=(14, 12))
sns.heatmap(corr_matrix, cmap='coolwarm', center=0, ax=ax,
            xticklabels=True, yticklabels=True, fmt='.1f',
            annot=False)
ax.set_title('Correlation Matrix — Breast Cancer Dataset', fontsize=14)
plt.tight_layout()
plt.savefig('correlation_matrix.png', dpi=150, bbox_inches='tight')
plt.show()

# Identifikasi pasangan fitur dengan korelasi > 0.95
upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
fitur_redundan = [col for col in upper_tri.columns if any(upper_tri[col] > 0.95)]
print(f"\nFitur dengan korelasi > 0.95 (kandidat dihapus):")
for f in fitur_redundan:
    print(f"  - {f}")
print(f"\nJumlah fitur redundan: {len(fitur_redundan)} dari {df_cancer.shape[1]}")
```

**C. SelectKBest — Pilih K fitur terbaik berdasarkan uji statistik:**

```python
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif

X_cancer = cancer.data
y_cancer = cancer.target

# SelectKBest dengan ANOVA F-test
selector_f = SelectKBest(score_func=f_classif, k=10)
X_f_selected = selector_f.fit_transform(X_cancer, y_cancer)

# Skor setiap fitur
skor_f = pd.DataFrame({
    'Fitur': cancer.feature_names,
    'F-Score': selector_f.scores_,
    'p-value': selector_f.pvalues_
}).sort_values('F-Score', ascending=False)

print("=== TOP 10 FITUR (ANOVA F-test) ===")
print(skor_f.head(10).to_string(index=False))

# Visualisasi skor
fig, ax = plt.subplots(figsize=(12, 6))
top_10 = skor_f.head(10)
ax.barh(top_10['Fitur'], top_10['F-Score'], color='steelblue')
ax.set_xlabel('F-Score')
ax.set_title('Top 10 Fitur Berdasarkan ANOVA F-test')
ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('selectkbest.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 9.3.2 Wrapper Methods: RFE (Recursive Feature Elimination)

RFE bekerja dengan **melatih model berulang kali**, menghapus fitur terkurang penting di setiap iterasi, hingga tersisa jumlah fitur yang diinginkan.

```python
from sklearn.feature_selection import RFE, RFECV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# RFE dengan Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rfe = RFE(estimator=rf, n_features_to_select=10, step=1)
rfe.fit(X_cancer, y_cancer)

# Fitur terpilih
fitur_rfe = pd.DataFrame({
    'Fitur': cancer.feature_names,
    'Ranking': rfe.ranking_,
    'Terpilih': rfe.support_
}).sort_values('Ranking')

print("=== FITUR TERPILIH OLEH RFE ===")
print(fitur_rfe[fitur_rfe['Terpilih']].to_string(index=False))

# Bandingkan akurasi sebelum dan sesudah
from sklearn.model_selection import cross_val_score

# Semua fitur
skor_semua = cross_val_score(rf, X_cancer, y_cancer, cv=5, scoring='accuracy')
# Fitur terpilih
skor_rfe = cross_val_score(rf, X_cancer[:, rfe.support_], y_cancer, cv=5, scoring='accuracy')

print(f"\nAkurasi semua fitur ({X_cancer.shape[1]}): {skor_semua.mean():.4f} ± {skor_semua.std():.4f}")
print(f"Akurasi RFE ({rfe.support_.sum()} fitur): {skor_rfe.mean():.4f} ± {skor_rfe.std():.4f}")
```

**RFECV — RFE dengan Cross-Validation:**

```python
# RFECV: otomatis menentukan jumlah fitur optimal
rfecv = RFECV(estimator=rf, step=1, cv=5, scoring='accuracy', min_features_to_select=2)
rfecv.fit(X_cancer, y_cancer)

print(f"Jumlah fitur optimal: {rfecv.n_features_}")
print(f"Akurasi terbaik: {rfecv.cv_results_['mean_test_score'].max():.4f}")

# Plot jumlah fitur vs akurasi
fig, ax = plt.subplots(figsize=(10, 5))
n_fitur_range = range(2, len(rfecv.cv_results_['mean_test_score']) + 2)
ax.plot(n_fitur_range, rfecv.cv_results_['mean_test_score'], 'b-o', linewidth=2)
ax.fill_between(
    n_fitur_range,
    rfecv.cv_results_['mean_test_score'] - rfecv.cv_results_['std_test_score'],
    rfecv.cv_results_['mean_test_score'] + rfecv.cv_results_['std_test_score'],
    alpha=0.2
)
ax.axvline(x=rfecv.n_features_, color='r', linestyle='--', label=f'Optimal: {rfecv.n_features_} fitur')
ax.set_xlabel('Jumlah Fitur')
ax.set_ylabel('Accuracy (CV)')
ax.set_title('RFECV: Jumlah Fitur Optimal')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('rfecv.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 9.3.3 Embedded Methods: L1/Lasso dan Tree-Based Importance

Embedded methods melakukan feature selection **sebagai bagian dari proses training** model.

**A. L1 Regularization (Lasso):**

```python
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Standardisasi (wajib untuk Lasso)
scaler = StandardScaler()
X_cancer_scaled = scaler.fit_transform(X_cancer)

# Logistic Regression dengan L1 regularization
lasso = LogisticRegression(penalty='l1', solver='saga', C=0.1,
                           max_iter=5000, random_state=42)
lasso.fit(X_cancer_scaled, y_cancer)

# Fitur dengan koefisien != 0
koefisien = pd.DataFrame({
    'Fitur': cancer.feature_names,
    'Koefisien': lasso.coef_[0]
}).sort_values('Koefisien', key=abs, ascending=False)

fitur_nonzero = koefisien[koefisien['Koefisien'] != 0]
print(f"=== FITUR TERPILIH OLEH LASSO (L1) ===")
print(f"Jumlah fitur non-zero: {len(fitur_nonzero)} dari {X_cancer.shape[1]}")
print(fitur_nonzero.to_string(index=False))
```

**B. Tree-Based Feature Importance:**

```python
from sklearn.ensemble import RandomForestClassifier

# Random Forest feature importance
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_cancer, y_cancer)

# Ambil importance
importance = pd.DataFrame({
    'Fitur': cancer.feature_names,
    'Importance': rf.feature_importances_
}).sort_values('Importance', ascending=False)

print("=== TOP 15 FITUR (Random Forest Importance) ===")
print(importance.head(15).to_string(index=False))

# Visualisasi
fig, ax = plt.subplots(figsize=(12, 8))
top15 = importance.head(15)
ax.barh(top15['Fitur'], top15['Importance'], color='forestgreen')
ax.set_xlabel('Feature Importance')
ax.set_title('Top 15 Features — Random Forest Importance')
ax.invert_yaxis()
ax.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('rf_importance.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## 9.4 Feature Extraction vs Feature Selection

| Aspek | Feature Selection | Feature Extraction |
|-------|-------------------|--------------------|
| **Apa yang dilakukan** | Memilih subset fitur asli | Membuat fitur baru dari kombinasi fitur asli |
| **Contoh** | RFE, SelectKBest, Lasso | PCA, t-SNE, Autoencoder |
| **Interpretabilitas** | Tinggi (fitur asli tetap) | Rendah (PC1, PC2 sulit diinterpretasi) |
| **Informasi** | Fitur yang dibuang hilang total | Semua informasi dikompresi |
| **Kapan digunakan** | Ingin tahu fitur mana yang penting | Ingin reduksi dimensi untuk visualisasi/efisiensi |

```
Feature Selection:                Feature Extraction:
[F1, F2, F3, F4, F5]             [F1, F2, F3, F4, F5]
      ↓ pilih                           ↓ transformasi
[F1, F3, F5]                     [PC1, PC2]
(fitur asli, mudah dipahami)     (fitur baru, sulit diinterpretasi)
```

---

## 9.5 Menggabungkan PCA dengan Model ML

### 9.5.1 PCA sebagai Preprocessing

```python
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import numpy as np

# Bandingkan performa dengan dan tanpa PCA
# Dataset: Breast Cancer (30 fitur)
X = cancer.data
y = cancer.target

# Pipeline 1: Tanpa PCA
pipe_no_pca = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression(max_iter=5000, random_state=42))
])

# Pipeline 2: Dengan PCA (10 komponen)
pipe_pca_10 = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=10)),
    ('clf', LogisticRegression(max_iter=5000, random_state=42))
])

# Pipeline 3: Dengan PCA (95% variance)
pipe_pca_95 = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=0.95)),  # Otomatis pilih jumlah komponen
    ('clf', LogisticRegression(max_iter=5000, random_state=42))
])

# Evaluasi
hasil = {}
for nama, pipe in [('Tanpa PCA (30 fitur)', pipe_no_pca),
                    ('PCA (10 komponen)', pipe_pca_10),
                    ('PCA (95% variance)', pipe_pca_95)]:
    skor = cross_val_score(pipe, X, y, cv=5, scoring='accuracy')
    hasil[nama] = f"{skor.mean():.4f} ± {skor.std():.4f}"
    print(f"{nama}: Accuracy = {skor.mean():.4f} ± {skor.std():.4f}")

# Berapa komponen untuk 95% variance?
pca_temp = PCA(n_components=0.95)
scaler_temp = StandardScaler()
pca_temp.fit(scaler_temp.fit_transform(X))
print(f"\nJumlah komponen untuk 95% variance: {pca_temp.n_components_}")
```

### 9.5.2 Memilih Jumlah Komponen Optimal

```python
# Grid search: jumlah komponen vs akurasi
komponen_range = range(1, 31)
akurasi_list = []

for n in komponen_range:
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('pca', PCA(n_components=n)),
        ('clf', LogisticRegression(max_iter=5000, random_state=42))
    ])
    skor = cross_val_score(pipe, X, y, cv=5, scoring='accuracy')
    akurasi_list.append(skor.mean())

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(list(komponen_range), akurasi_list, 'b-o', linewidth=2, markersize=4)
ax.axhline(y=max(akurasi_list), color='r', linestyle='--',
           label=f'Akurasi terbaik: {max(akurasi_list):.4f}')
best_n = list(komponen_range)[np.argmax(akurasi_list)]
ax.axvline(x=best_n, color='g', linestyle='--',
           label=f'Komponen optimal: {best_n}')
ax.set_xlabel('Jumlah Principal Components')
ax.set_ylabel('Accuracy (5-fold CV)')
ax.set_title('Akurasi vs Jumlah Komponen PCA')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('pca_vs_accuracy.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## 9.6 Workflow Praktis: Kapan Mereduksi vs Memilih Fitur

### 9.6.1 Panduan Keputusan

```
Apakah fitur sangat banyak (>50) relatif terhadap sampel?
├── Ya → Lakukan reduksi dimensi
│   ├── Butuh interpretabilitas? → Feature Selection (RFE, Lasso)
│   └── Butuh visualisasi/efisiensi? → PCA
└── Tidak → Cek multikolinearitas
    ├── Ada fitur sangat berkorelasi (>0.95)? → Buang salah satu (correlation filter)
    └── Tidak → Mungkin tidak perlu reduksi
```

### 9.6.2 Contoh Workflow Lengkap

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Strategi 1: Filter → Model
pipe_filter = Pipeline([
    ('scaler', StandardScaler()),
    ('select', SelectKBest(score_func=f_classif, k=15)),
    ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Strategi 2: PCA → Model
pipe_pca = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=0.95)),
    ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Strategi 3: Embedded (RF langsung)
pipe_full = Pipeline([
    ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Bandingkan
print("=== PERBANDINGAN STRATEGI ===")
for nama, pipe in [('Filter (top 15)', pipe_filter),
                    ('PCA (95% var)', pipe_pca),
                    ('Full features', pipe_full)]:
    skor = cross_val_score(pipe, X, y, cv=5, scoring='accuracy')
    print(f"{nama:20s}: {skor.mean():.4f} ± {skor.std():.4f}")
```

---

## 9.7 AI Corner: Menggunakan AI untuk Saran Feature Engineering

### Level: Advanced

| Kemampuan AI | Contoh Penggunaan |
|-------------|-------------------|
| Saran fitur baru | Minta AI merekomendasikan fitur turunan berdasarkan domain |
| Interpretasi PCA | Minta AI menjelaskan arti principal components |
| Debugging pipeline | Minta AI memeriksa urutan preprocessing |
| Perbandingan metode | Minta AI menjelaskan kapan PCA vs RFE lebih tepat |

### Contoh Prompt yang Baik

```
Saya punya dataset prediksi harga rumah di Jakarta dengan 25 fitur:
[list fitur]. Setelah PCA, 2 komponen pertama menjelaskan 72% variansi.
Loading matrix menunjukkan PC1 didominasi luas_tanah dan luas_bangunan,
PC2 didominasi jumlah_kamar dan jarak_ke_pusat.

1. Bagaimana interpretasi PC1 dan PC2?
2. Apakah ada fitur turunan baru yang sebaiknya saya buat?
3. Apakah 72% cukup atau perlu menambah komponen?
```

### Contoh Prompt yang Kurang Baik

```
Lakukan PCA pada data saya
```

### Yang Perlu Diingat

1. **PCA components sulit diinterpretasi** — AI bisa membantu memberi makna, tapi verifikasi dengan domain knowledge
2. **Feature engineering membutuhkan pemahaman domain** — AI bisa menyarankan, tapi Anda yang memvalidasi
3. **Jangan blindly reduce** — selalu bandingkan performa sebelum dan sesudah reduksi
4. **Dokumentasikan keputusan** — catat mengapa memilih metode tertentu dalam AI Usage Log

### Template AI Usage Log

```markdown
## AI Usage Documentation — Bab 9
### Tool: [Claude / ChatGPT / Copilot]
### Prompt: "Interpretasikan loading matrix PCA berikut..."
### Output: [Ringkasan interpretasi AI]
### Modifikasi: [Fitur turunan yang saya buat berdasarkan saran AI]
### Refleksi: [Apakah saran AI sesuai dengan konteks domain?]
```

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan apa itu *curse of dimensionality* dan berikan tiga masalah spesifik yang ditimbulkannya pada algoritma machine learning.

**Soal 2.** Apa perbedaan antara feature selection dan feature extraction? Berikan masing-masing dua contoh metode.

**Soal 3.** Dalam PCA, apa arti *explained variance ratio*? Jika PC1 memiliki explained variance ratio 0.65 dan PC2 = 0.20, berapa persen informasi asli yang hilang jika kita hanya menggunakan 2 komponen dari data 10 dimensi?

**Soal 4.** Sebutkan dan jelaskan tiga kategori feature selection (filter, wrapper, embedded) beserta kelebihan dan kekurangan masing-masing.

**Soal 5.** Mengapa standardisasi data wajib dilakukan sebelum PCA? Apa yang terjadi jika tidak dilakukan?

### Tingkat Menengah (C3)

**Soal 6.** Tulis kode Python untuk:
- Memuat dataset `wine` dari sklearn
- Terapkan PCA untuk mereduksi dari 13 fitur ke 2 komponen
- Buat scatter plot 2D yang diberi warna berdasarkan kelas wine
- Tampilkan explained variance ratio dan loading matrix

**Soal 7.** Bandingkan tiga metode feature selection (VarianceThreshold, SelectKBest, RFE) pada dataset breast cancer. Gunakan Logistic Regression sebagai model evaluasi. Metode mana yang menghasilkan akurasi tertinggi dengan jumlah fitur paling sedikit?

**Soal 8.** Buat pipeline scikit-learn yang menggabungkan StandardScaler, PCA, dan RandomForestClassifier. Gunakan GridSearchCV untuk menemukan jumlah komponen PCA optimal (2-15).

### Tingkat Mahir (C4)

**Soal 9.** Sebuah bank di Indonesia ingin membangun model prediksi kredit macet. Dataset memiliki 50 fitur dari 10.000 nasabah. Jelaskan:
- a) Strategi reduksi dimensi yang Anda rekomendasikan (dan mengapa)
- b) Bagaimana menentukan jumlah fitur/komponen optimal
- c) Trade-off antara interpretabilitas dan performa
- d) Implementasikan solusi lengkap dengan kode Python

**Soal 10.** Anda mendapat dataset survei dengan 100 pertanyaan (fitur) dan 200 responden. Banyak pertanyaan yang saling berkorelasi tinggi.
- a) Apakah ini masuk akal secara statistik? Jelaskan.
- b) Terapkan PCA dan tentukan berapa "faktor" yang mendasari 100 pertanyaan tersebut.
- c) Bagaimana Anda menginterpretasikan principal components yang dihasilkan?
- d) Bandingkan pendekatan PCA vs SelectKBest untuk preprocessing sebelum klasifikasi.

---

## Rangkuman

1. **Curse of dimensionality** menyebabkan data menjadi sparse, jarak tidak bermakna, dan model overfit ketika fitur terlalu banyak relatif terhadap sampel.
2. **PCA** mentransformasi data ke koordinat baru (principal components) yang menangkap variansi data secara berurutan. Gunakan scree plot dan cumulative explained variance untuk memilih jumlah komponen.
3. **Feature selection** memilih subset fitur asli melalui tiga pendekatan: **filter** (cepat, independen model), **wrapper** (akurat, lambat), dan **embedded** (terintegrasi dalam training).
4. **Feature extraction** (seperti PCA) membuat fitur baru dari kombinasi fitur asli — efektif untuk reduksi dimensi tetapi mengorbankan interpretabilitas.
5. Pilih **feature selection** jika interpretabilitas penting; pilih **PCA** jika tujuan utama adalah efisiensi komputasi atau visualisasi.
6. Selalu **bandingkan performa** sebelum dan sesudah reduksi dimensi menggunakan cross-validation.

---

## Referensi

1. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.
2. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
3. Jolliffe, I. T. (2002). *Principal Component Analysis* (2nd ed.). Springer.
4. scikit-learn documentation. (2026). *Decomposition* & *Feature Selection*. Retrieved from https://scikit-learn.org/stable/
5. Raschka, S., & Mirjalili, V. (2022). *Python Machine Learning* (4th ed.). Packt Publishing.
6. Guyon, I., & Elisseeff, A. (2003). An introduction to variable and feature selection. *Journal of Machine Learning Research*, 3, 1157-1182.

---

*Bab berikutnya: **Bab 10 — Neural Networks dan Deep Learning***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
