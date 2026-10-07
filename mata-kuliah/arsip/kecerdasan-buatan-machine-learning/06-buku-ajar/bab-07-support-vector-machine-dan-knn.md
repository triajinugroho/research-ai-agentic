# BAB 7: SUPPORT VECTOR MACHINE DAN K-NEAREST NEIGHBORS

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| Sub-CPMK 7.1 | Menganalisis prinsip kerja KNN dan SVM serta memilih algoritma yang tepat berdasarkan karakteristik data | C4 |
| Sub-CPMK 7.2 | Menganalisis performa berbagai model klasifikasi menggunakan cross-validation dan sklearn Pipeline | C4 |

**CPMK-3:** Menerapkan algoritma supervised learning untuk permasalahan regresi dan klasifikasi.

---

## Estimasi Waktu

| Aktivitas | Durasi |
|-----------|--------|
| Membaca materi | 90 menit |
| Praktik kode Python | 120 menit |
| Mengerjakan latihan soal | 60 menit |
| **Total** | **270 menit (4.5 jam)** |

---

## Prasyarat

- Bab 5: Regresi Linear dan Logistik
- Bab 6: Decision Tree dan Ensemble Methods
- Pemahaman metrik evaluasi klasifikasi (confusion matrix, precision, recall)
- Kemampuan dasar Python, NumPy, pandas, dan sklearn

---

## 7.1 K-Nearest Neighbors (KNN)

### 7.1.1 Concept: Distance-Based Classification (Konsep: Klasifikasi Berbasis Jarak)

**K-Nearest Neighbors (KNN)** adalah algoritma klasifikasi yang bekerja berdasarkan prinsip sederhana: **"katakan siapa temanmu, dan aku akan katakan siapa kamu"** (tell me who your neighbors are, and I'll tell you who you are).

```
Algoritma KNN:
1. Tentukan nilai K (jumlah tetangga terdekat)
2. Untuk setiap data baru yang ingin diklasifikasi:
   a. Hitung jarak ke SEMUA data training
   b. Pilih K data training terdekat
   c. Lakukan voting mayoritas dari K tetangga
   d. Prediksi = kelas dengan suara terbanyak

Contoh (K=3):
                     ● = Kelas A
                     ○ = Kelas B
                     ★ = Data baru

         ●      ●
      ●    ★         ○
         ●      ○
              ○     ○

  3 tetangga terdekat: ●, ●, ○
  Voting: Kelas A = 2, Kelas B = 1
  Prediksi: Kelas A ✓
```

**Sifat penting KNN:**
- **Lazy learner** — tidak ada proses "training" yang sebenarnya (hanya menyimpan data)
- **Instance-based learning** — keputusan dibuat pada saat prediksi
- **Non-parametric** — tidak mengasumsikan distribusi data tertentu

### 7.1.2 Distance Metrics: Euclidean, Manhattan, Minkowski

Kunci dari KNN adalah **cara mengukur jarak** antara dua titik data.

| Metrik | Rumus | Keterangan |
|--------|-------|------------|
| **Euclidean** | √(Σ(xᵢ - yᵢ)²) | Jarak garis lurus (default) |
| **Manhattan** | Σ\|xᵢ - yᵢ\| | Jarak "blok kota" (city block) |
| **Minkowski** | (Σ\|xᵢ - yᵢ\|ᵖ)^(1/p) | Generalisasi: p=1 → Manhattan, p=2 → Euclidean |

```python
import numpy as np

def euclidean_distance(a, b):
    """Jarak Euclidean antara dua titik"""
    return np.sqrt(np.sum((a - b) ** 2))

def manhattan_distance(a, b):
    """Jarak Manhattan antara dua titik"""
    return np.sum(np.abs(a - b))

def minkowski_distance(a, b, p):
    """Jarak Minkowski antara dua titik"""
    return np.sum(np.abs(a - b) ** p) ** (1 / p)

# Contoh: dua mahasiswa dengan feature [jam_belajar, nilai_tugas]
mahasiswa_A = np.array([10, 85])
mahasiswa_B = np.array([15, 92])

print("=== PERBANDINGAN METRIK JARAK ===")
print(f"Euclidean : {euclidean_distance(mahasiswa_A, mahasiswa_B):.4f}")
print(f"Manhattan : {manhattan_distance(mahasiswa_A, mahasiswa_B):.4f}")
print(f"Minkowski (p=3): {minkowski_distance(mahasiswa_A, mahasiswa_B, 3):.4f}")
```

**Penting:** Karena KNN bergantung pada jarak, **feature scaling** (normalisasi/standardisasi) sangat penting. Feature dengan skala besar akan mendominasi perhitungan jarak.

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# Contoh dampak scaling
data = np.array([
    [3, 80000],   # [pengalaman_tahun, gaji_rp_ribu]
    [5, 120000],
    [2, 60000],
])

print("Tanpa Scaling:")
print(f"  Jarak (0,1): {euclidean_distance(data[0], data[1]):.2f}")
print(f"  → Didominasi oleh gaji (skala ribuan)")

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

print(f"\nDengan Scaling:")
print(f"  Jarak (0,1): {euclidean_distance(data_scaled[0], data_scaled[1]):.2f}")
print(f"  → Kedua feature berkontribusi seimbang")
```

### 7.1.3 Choosing K: Bias-Variance Tradeoff

Pemilihan nilai **K** sangat mempengaruhi performa model:

```
K terlalu kecil (misal K=1):
  + Fleksibel, bisa menangkap pola lokal
  - Rentan overfitting dan noise
  - Bias rendah, variance tinggi

K terlalu besar (misal K=n):
  + Stabil, tahan terhadap noise
  - Terlalu general, kehilangan pola lokal
  - Bias tinggi, variance rendah

    Error
    │  \
    │   \         ← Test Error
    │    \_______/
    │   /
    │  /          ← Training Error
    │ /
    └──────────────── K
       1   5  10  20  50
```

```python
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Dataset: klasifikasi kualitas kopi Indonesia
np.random.seed(42)
n = 300

data_kopi = pd.DataFrame({
    'tingkat_keasaman': np.round(np.random.uniform(4.0, 7.0, n), 2),
    'kadar_kafein_mg': np.round(np.random.uniform(50, 200, n), 1),
    'suhu_roasting_c': np.round(np.random.uniform(180, 250, n), 1),
    'waktu_roasting_menit': np.round(np.random.uniform(8, 20, n), 1),
    'kelembaban_persen': np.round(np.random.uniform(5, 15, n), 1),
})

# Label kualitas: 0 = standar, 1 = premium
skor = (
    -abs(data_kopi['tingkat_keasaman'] - 5.5) * 10 +
    data_kopi['kadar_kafein_mg'] * 0.03 +
    -abs(data_kopi['suhu_roasting_c'] - 210) * 0.1 +
    data_kopi['waktu_roasting_menit'] * 0.5 -
    data_kopi['kelembaban_persen'] * 0.3 +
    np.random.normal(0, 1, n)
)
data_kopi['kualitas'] = (skor > 1).astype(int)

X = data_kopi.drop('kualitas', axis=1)
y = data_kopi['kualitas']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scaling (wajib untuk KNN)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# Cari K optimal
k_range = range(1, 31)
cv_scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train_s, y_train, cv=5, scoring='accuracy')
    cv_scores.append(scores.mean())

# Visualisasi
plt.figure(figsize=(10, 6))
plt.plot(k_range, cv_scores, 'b-o', linewidth=2, markersize=4)
best_k = k_range[np.argmax(cv_scores)]
plt.axvline(x=best_k, color='red', linestyle='--',
            label=f'K optimal = {best_k} (Acc = {max(cv_scores):.4f})')
plt.xlabel('K (Jumlah Tetangga)', fontsize=12)
plt.ylabel('Cross-Validation Accuracy', fontsize=12)
plt.title('Pemilihan K Optimal untuk KNN', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"K optimal: {best_k}")
print(f"CV Accuracy terbaik: {max(cv_scores):.4f}")
```

### 7.1.4 KNN for Classification and Regression

KNN dapat digunakan untuk **klasifikasi** (voting mayoritas) maupun **regresi** (rata-rata nilai tetangga):

```
Klasifikasi: prediksi = modus(kelas K tetangga)
Regresi:     prediksi = mean(nilai K tetangga)
```

### 7.1.5 sklearn: KNeighborsClassifier

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

# Latih KNN dengan K optimal
knn_model = KNeighborsClassifier(
    n_neighbors=best_k,
    metric='euclidean',   # atau 'manhattan', 'minkowski'
    weights='uniform'     # atau 'distance' (bobot berdasarkan jarak)
)
knn_model.fit(X_train_s, y_train)

# Evaluasi
y_pred_knn = knn_model.predict(X_test_s)
print("=== KNN CLASSIFICATION ===")
print(f"K = {best_k}")
print(f"Accuracy: {accuracy_score(y_test, y_pred_knn):.4f}")
print(f"\n{classification_report(y_test, y_pred_knn, target_names=['Standar', 'Premium'])}")

# Bandingkan uniform vs distance weighting
for weights in ['uniform', 'distance']:
    knn_w = KNeighborsClassifier(n_neighbors=best_k, weights=weights)
    knn_w.fit(X_train_s, y_train)
    acc = accuracy_score(y_test, knn_w.predict(X_test_s))
    print(f"  weights='{weights}': accuracy = {acc:.4f}")
```

---

## 7.2 Support Vector Machine (SVM)

### 7.2.1 Concept: Hyperplane and Margin (Konsep: Hyperplane dan Margin)

**Support Vector Machine (SVM)** adalah algoritma klasifikasi yang bekerja dengan mencari **hyperplane** (bidang pemisah) terbaik yang memisahkan dua kelas data. Hyperplane terbaik adalah yang memiliki **margin** (jarak ke data terdekat) paling besar.

```
Konsep SVM (2D):

  Kelas A (●)              Kelas B (○)

      ●                         ○
    ● ● ●      | margin |    ○ ○
      ●    ●───|────────|───○   ○
      ●  ●     |  hyper |     ○
        ●      |  plane |       ○

  ← support vectors → (data terdekat ke hyperplane)

Tujuan SVM: Maksimalkan margin antara dua kelas
```

**Mengapa margin besar penting?**
- Margin besar → model lebih **general** (tahan terhadap variasi data baru)
- Margin kecil → model rentan **overfitting**

### 7.2.2 Support Vectors

**Support vectors** adalah data point yang terletak tepat di batas margin. Mereka adalah "penentu" posisi hyperplane.

```
Sifat support vectors:
- Hanya SEBAGIAN KECIL dari data training
- Menghilangkan data non-support-vector TIDAK mengubah hyperplane
- Ini membuat SVM sangat efisien secara memori
```

### 7.2.3 Kernel Trick: Linear, Polynomial, RBF

Bagaimana jika data **tidak bisa dipisahkan secara linear**? SVM menggunakan **kernel trick** untuk memetakan data ke dimensi yang lebih tinggi di mana pemisahan linear menjadi mungkin.

```
Data di 2D (tidak bisa dipisahkan linear):

    ○ ○ ○ ● ● ○ ○ ○
    ○ ○ ● ● ● ● ○ ○

Dipetakan ke 3D (bisa dipisahkan linear):

         ● ●
       ● ● ● ●     ← data kelas ● "terangkat"
    ○ ○ ○ ○ ○ ○ ○   ← data kelas ○ tetap
```

| Kernel | Rumus | Kapan Digunakan |
|--------|-------|-----------------|
| **Linear** | K(x,y) = xᵀy | Data linearly separable |
| **Polynomial** | K(x,y) = (γxᵀy + r)ᵈ | Hubungan polynomial antar feature |
| **RBF (Gaussian)** | K(x,y) = exp(-γ\|\|x-y\|\|²) | Default, cocok untuk kebanyakan kasus |

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_moons, make_circles
from sklearn.preprocessing import StandardScaler

# Buat dataset non-linear
X_moon, y_moon = make_moons(n_samples=200, noise=0.15, random_state=42)
scaler = StandardScaler()
X_moon_s = scaler.fit_transform(X_moon)

# Bandingkan kernel
kernels = ['linear', 'poly', 'rbf']
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for ax, kernel in zip(axes, kernels):
    svm = SVC(kernel=kernel, gamma='scale', degree=3, C=1.0)
    svm.fit(X_moon_s, y_moon)
    acc = svm.score(X_moon_s, y_moon)

    # Plot decision boundary
    h = 0.02
    x_min, x_max = X_moon_s[:, 0].min() - 1, X_moon_s[:, 0].max() + 1
    y_min, y_max = X_moon_s[:, 1].min() - 1, X_moon_s[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                          np.arange(y_min, y_max, h))
    Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    ax.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
    ax.scatter(X_moon_s[:, 0], X_moon_s[:, 1], c=y_moon,
               cmap='coolwarm', edgecolors='black', s=40)
    # Tandai support vectors
    ax.scatter(svm.support_vectors_[:, 0], svm.support_vectors_[:, 1],
               s=100, facecolors='none', edgecolors='black', linewidths=2)
    ax.set_title(f'Kernel: {kernel} (Acc: {acc:.2%})', fontsize=12)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')

plt.suptitle('Perbandingan Kernel SVM pada Data Non-Linear', fontsize=14)
plt.tight_layout()
plt.show()
```

### 7.2.4 Soft Margin (Parameter C)

Parameter **C** mengontrol trade-off antara **margin lebar** dan **kesalahan klasifikasi**:

```
C kecil (misal C=0.01):
  - Margin lebar (toleransi tinggi terhadap kesalahan)
  - Model lebih simple, mungkin underfitting
  - Regularisasi kuat

C besar (misal C=100):
  - Margin sempit (toleransi rendah terhadap kesalahan)
  - Model lebih kompleks, mungkin overfitting
  - Regularisasi lemah
```

```python
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

# Bandingkan nilai C
C_values = [0.01, 0.1, 1, 10, 100]
fig, axes = plt.subplots(1, 5, figsize=(25, 4))

for ax, C in zip(axes, C_values):
    svm = SVC(kernel='rbf', C=C, gamma='scale')
    svm.fit(X_moon_s, y_moon)
    acc = svm.score(X_moon_s, y_moon)

    h = 0.02
    x_min, x_max = X_moon_s[:, 0].min() - 1, X_moon_s[:, 0].max() + 1
    y_min, y_max = X_moon_s[:, 1].min() - 1, X_moon_s[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                          np.arange(y_min, y_max, h))
    Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    ax.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
    ax.scatter(X_moon_s[:, 0], X_moon_s[:, 1], c=y_moon,
               cmap='coolwarm', edgecolors='black', s=30)
    ax.set_title(f'C = {C}\nAcc: {acc:.2%}\nSV: {len(svm.support_vectors_)}',
                 fontsize=10)

plt.suptitle('Dampak Parameter C pada SVM', fontsize=14)
plt.tight_layout()
plt.show()
```

### 7.2.5 sklearn: SVC

```python
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score

# Gunakan dataset kopi dari sebelumnya
svm_model = SVC(
    kernel='rbf',       # kernel RBF (default)
    C=1.0,              # parameter regularisasi
    gamma='scale',      # parameter kernel (default: 1/(n_features * var))
    random_state=42,
    probability=True    # untuk predict_proba
)
svm_model.fit(X_train_s, y_train)

# Evaluasi
y_pred_svm = svm_model.predict(X_test_s)
print("=== SVM CLASSIFICATION ===")
print(f"Kernel: {svm_model.kernel}, C: {svm_model.C}")
print(f"Jumlah support vectors: {len(svm_model.support_vectors_)}")
print(f"  Kelas 0 (Standar) : {svm_model.n_support_[0]} support vectors")
print(f"  Kelas 1 (Premium) : {svm_model.n_support_[1]} support vectors")
print(f"\nAccuracy: {accuracy_score(y_test, y_pred_svm):.4f}")
print(f"\n{classification_report(y_test, y_pred_svm, target_names=['Standar', 'Premium'])}")
```

---

## 7.3 Model Comparison Framework (Kerangka Perbandingan Model)

### 7.3.1 When to Use KNN vs SVM vs Tree/Forest vs Logistic

| Kriteria | KNN | SVM | Decision Tree | Random Forest | Logistic Regression |
|----------|-----|-----|---------------|---------------|---------------------|
| **Ukuran data kecil** | Baik | Sangat baik | Baik | Cukup | Baik |
| **Ukuran data besar** | Lambat | Lambat | Cepat | Cepat | Cepat |
| **Data non-linear** | Baik | Sangat baik (kernel) | Baik | Sangat baik | Kurang baik |
| **Interpretabilitas** | Rendah | Rendah | Sangat tinggi | Sedang | Tinggi |
| **Feature scaling** | Wajib | Wajib | Tidak perlu | Tidak perlu | Disarankan |
| **Missing values** | Tidak toleran | Tidak toleran | Toleran | Toleran | Tidak toleran |
| **Outlier** | Sensitif | Sedikit sensitif | Robust | Robust | Sensitif |

### 7.3.2 Accuracy, Training Time, Interpretability Comparison

```python
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
import time

# Definisikan model
models = {
    'KNN (K=5)': KNeighborsClassifier(n_neighbors=5),
    'SVM (RBF)': SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42),
    'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Logistic Reg.': LogisticRegression(max_iter=1000, random_state=42),
}

# Evaluasi semua model
results = []
for name, model in models.items():
    start = time.time()

    # Cross-validation
    cv_scores = cross_val_score(model, X_train_s, y_train, cv=5,
                                 scoring='accuracy')

    # Train dan test
    model.fit(X_train_s, y_train)
    train_acc = accuracy_score(y_train, model.predict(X_train_s))
    test_acc = accuracy_score(y_test, model.predict(X_test_s))

    elapsed = time.time() - start

    results.append({
        'Model': name,
        'CV Accuracy': f"{cv_scores.mean():.4f} +/- {cv_scores.std():.4f}",
        'Train Acc': train_acc,
        'Test Acc': test_acc,
        'Time (ms)': f"{elapsed*1000:.1f}",
    })

results_df = pd.DataFrame(results)
print("=== PERBANDINGAN SEMUA MODEL ===")
print(results_df.to_string(index=False))
```

---

## 7.4 Cross-Validation

### 7.4.1 k-fold Cross-Validation

**k-fold Cross-Validation** membagi data training menjadi k subset (folds) dan secara bergantian menggunakan setiap fold sebagai validasi.

```
5-Fold Cross-Validation:

Fold 1: [VAL][TRAIN][TRAIN][TRAIN][TRAIN] → Score₁
Fold 2: [TRAIN][VAL][TRAIN][TRAIN][TRAIN] → Score₂
Fold 3: [TRAIN][TRAIN][VAL][TRAIN][TRAIN] → Score₃
Fold 4: [TRAIN][TRAIN][TRAIN][VAL][TRAIN] → Score₄
Fold 5: [TRAIN][TRAIN][TRAIN][TRAIN][VAL] → Score₅

Final Score = mean(Score₁, Score₂, ..., Score₅)
```

### 7.4.2 Stratified k-fold

**Stratified k-fold** memastikan setiap fold memiliki proporsi kelas yang sama dengan dataset asli — sangat penting untuk **imbalanced dataset**.

```python
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score
import numpy as np

# Perbandingan KFold vs StratifiedKFold
print("=== PERBANDINGAN CROSS-VALIDATION ===")

# KFold biasa
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores_kf = cross_val_score(
    KNeighborsClassifier(n_neighbors=5),
    X_train_s, y_train, cv=kf, scoring='accuracy'
)

# StratifiedKFold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores_skf = cross_val_score(
    KNeighborsClassifier(n_neighbors=5),
    X_train_s, y_train, cv=skf, scoring='accuracy'
)

print(f"KFold biasa:")
print(f"  Scores: {scores_kf}")
print(f"  Mean: {scores_kf.mean():.4f}, Std: {scores_kf.std():.4f}")

print(f"\nStratifiedKFold:")
print(f"  Scores: {scores_skf}")
print(f"  Mean: {scores_skf.mean():.4f}, Std: {scores_skf.std():.4f}")

# Verifikasi distribusi kelas di setiap fold
print(f"\nDistribusi kelas per fold (StratifiedKFold):")
for i, (train_idx, val_idx) in enumerate(skf.split(X_train_s, y_train)):
    y_fold_train = y_train.iloc[train_idx]
    y_fold_val = y_train.iloc[val_idx]
    print(f"  Fold {i+1}: Train {y_fold_train.mean():.2%} positif | "
          f"Val {y_fold_val.mean():.2%} positif")
```

### 7.4.3 cross_val_score in sklearn

```python
from sklearn.model_selection import cross_val_score, cross_validate
import numpy as np

# cross_val_score: evaluasi satu metrik
model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
scores = cross_val_score(model, X_train_s, y_train, cv=5, scoring='accuracy')

print("=== cross_val_score ===")
print(f"Accuracy per fold: {scores}")
print(f"Mean: {scores.mean():.4f}, Std: {scores.std():.4f}")
print(f"95% CI: [{scores.mean() - 2*scores.std():.4f}, "
      f"{scores.mean() + 2*scores.std():.4f}]")

# cross_validate: evaluasi beberapa metrik sekaligus
cv_results = cross_validate(
    model, X_train_s, y_train, cv=5,
    scoring=['accuracy', 'precision', 'recall', 'f1'],
    return_train_score=True
)

print("\n=== cross_validate (multi-metric) ===")
for metric in ['accuracy', 'precision', 'recall', 'f1']:
    train_scores = cv_results[f'train_{metric}']
    test_scores = cv_results[f'test_{metric}']
    print(f"{metric:12s}: Train {train_scores.mean():.4f} | "
          f"Val {test_scores.mean():.4f} +/- {test_scores.std():.4f}")
```

---

## 7.5 sklearn Pipeline

### 7.5.1 Pipeline Concept (Konsep Pipeline)

**Pipeline** menggabungkan beberapa langkah preprocessing dan modeling menjadi satu objek tunggal. Ini menghindari **data leakage** dan membuat kode lebih rapi.

```
Tanpa Pipeline (rawan data leakage):
  1. scaler.fit_transform(X_train)  ← fit pada training
  2. scaler.transform(X_test)       ← transform pada test
  3. model.fit(X_train_scaled)
  4. model.predict(X_test_scaled)

Dengan Pipeline (aman):
  1. pipeline.fit(X_train, y_train)   ← otomatis fit+transform
  2. pipeline.predict(X_test)         ← otomatis transform+predict
```

### 7.5.2 Combining Preprocessing + Classification

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Pipeline SVM
pipe_svm = Pipeline([
    ('scaler', StandardScaler()),           # Langkah 1: Scaling
    ('classifier', SVC(kernel='rbf',        # Langkah 2: Klasifikasi
                        C=1.0,
                        gamma='scale',
                        random_state=42))
])

# Pipeline KNN
pipe_knn = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', KNeighborsClassifier(n_neighbors=5))
])

# Gunakan data ASLI (bukan yang sudah di-scale)
# Pipeline akan handle scaling secara internal
X = data_kopi.drop('kualitas', axis=1)
y = data_kopi['kualitas']
X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Latih dan evaluasi
for name, pipe in [('SVM', pipe_svm), ('KNN', pipe_knn)]:
    pipe.fit(X_train_raw, y_train)
    y_pred = pipe.predict(X_test_raw)
    acc = accuracy_score(y_test, y_pred)
    print(f"{name} Pipeline Accuracy: {acc:.4f}")
```

### 7.5.3 GridSearchCV with Pipeline

```python
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Pipeline untuk SVM
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(random_state=42))
])

# Parameter grid (perhatikan prefix nama langkah)
param_grid = {
    'svm__kernel': ['linear', 'rbf', 'poly'],
    'svm__C': [0.1, 1, 10],
    'svm__gamma': ['scale', 'auto'],
}

# GridSearchCV dengan Pipeline
grid_search = GridSearchCV(
    pipe,
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

grid_search.fit(X_train_raw, y_train)

print("=== GRID SEARCH + PIPELINE ===")
print(f"Parameter terbaik: {grid_search.best_params_}")
print(f"CV Accuracy terbaik: {grid_search.best_score_:.4f}")

# Evaluasi pada data test
y_pred_best = grid_search.predict(X_test_raw)
print(f"Test Accuracy: {accuracy_score(y_test, y_pred_best):.4f}")
print(f"\n{classification_report(y_test, y_pred_best, target_names=['Standar', 'Premium'])}")
```

---

## 7.6 Comprehensive Model Comparison (Perbandingan Komprehensif dengan Dataset Indonesia)

### 7.6.1 Studi Kasus: Klasifikasi Jenis Batik Indonesia

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import time

# Dataset: Klasifikasi jenis batik berdasarkan fitur warna dan tekstur
# (simulasi berdasarkan analisis citra digital)
np.random.seed(42)
n = 400

# Fitur warna dan tekstur (simulasi dari fitur ekstraksi citra)
data_batik = pd.DataFrame({
    'mean_red': np.round(np.random.uniform(80, 220, n), 1),
    'mean_green': np.round(np.random.uniform(60, 200, n), 1),
    'mean_blue': np.round(np.random.uniform(40, 180, n), 1),
    'contrast': np.round(np.random.uniform(10, 100, n), 2),
    'homogeneity': np.round(np.random.uniform(0.1, 0.9, n), 4),
    'energy': np.round(np.random.uniform(0.01, 0.5, n), 4),
    'correlation': np.round(np.random.uniform(0.5, 0.99, n), 4),
    'entropy_tekstur': np.round(np.random.uniform(3, 8, n), 2),
})

# Label: 3 jenis batik
# Batik Parang: dominan coklat (red tinggi, blue rendah)
# Batik Kawung: kontras tinggi, simetris
# Batik Mega Mendung: biru dominan
jenis = []
for _, row in data_batik.iterrows():
    if row['mean_red'] > 160 and row['mean_blue'] < 100:
        jenis.append('Parang')
    elif row['contrast'] > 60 and row['homogeneity'] > 0.5:
        jenis.append('Kawung')
    elif row['mean_blue'] > 120:
        jenis.append('Mega Mendung')
    else:
        jenis.append(np.random.choice(['Parang', 'Kawung', 'Mega Mendung']))

data_batik['jenis'] = jenis

# Encode label
le = LabelEncoder()
data_batik['jenis_encoded'] = le.fit_transform(data_batik['jenis'])

print("=== DATASET KLASIFIKASI BATIK ===")
print(f"Jumlah sampel: {len(data_batik)}")
print(f"Distribusi kelas:\n{data_batik['jenis'].value_counts()}")

# Feature dan target
feature_cols = ['mean_red', 'mean_green', 'mean_blue', 'contrast',
                'homogeneity', 'energy', 'correlation', 'entropy_tekstur']
X = data_batik[feature_cols]
y = data_batik['jenis_encoded']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Definisikan pipeline untuk setiap model
pipelines = {
    'KNN': Pipeline([
        ('scaler', StandardScaler()),
        ('clf', KNeighborsClassifier(n_neighbors=7))
    ]),
    'SVM (Linear)': Pipeline([
        ('scaler', StandardScaler()),
        ('clf', SVC(kernel='linear', C=1.0, random_state=42))
    ]),
    'SVM (RBF)': Pipeline([
        ('scaler', StandardScaler()),
        ('clf', SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42))
    ]),
    'Decision Tree': Pipeline([
        ('clf', DecisionTreeClassifier(max_depth=5, random_state=42))
    ]),
    'Random Forest': Pipeline([
        ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
    ]),
    'Logistic Reg.': Pipeline([
        ('scaler', StandardScaler()),
        ('clf', LogisticRegression(max_iter=1000, random_state=42))
    ]),
}

# Evaluasi semua model
print("\n=== PERBANDINGAN KOMPREHENSIF ===")
all_results = []

for name, pipe in pipelines.items():
    start = time.time()

    # Cross-validation
    cv_scores = cross_val_score(pipe, X_train, y_train, cv=5,
                                 scoring='accuracy')

    # Train dan test
    pipe.fit(X_train, y_train)
    train_acc = accuracy_score(y_train, pipe.predict(X_train))
    test_acc = accuracy_score(y_test, pipe.predict(X_test))

    elapsed = time.time() - start

    all_results.append({
        'Model': name,
        'CV Mean': cv_scores.mean(),
        'CV Std': cv_scores.std(),
        'Train': train_acc,
        'Test': test_acc,
        'Time (ms)': elapsed * 1000,
    })

    print(f"\n--- {name} ---")
    print(f"CV Accuracy: {cv_scores.mean():.4f} +/- {cv_scores.std():.4f}")
    print(f"Train/Test: {train_acc:.4f} / {test_acc:.4f}")

# Tabel ringkasan
results_df = pd.DataFrame(all_results)
print("\n=== TABEL RINGKASAN ===")
print(results_df.to_string(index=False, float_format='%.4f'))

# Visualisasi perbandingan
fig, ax = plt.subplots(figsize=(12, 6))
x = range(len(results_df))
width = 0.25

ax.bar([i - width for i in x], results_df['Train'], width,
       label='Training', color='steelblue', alpha=0.8)
ax.bar(x, results_df['Test'], width,
       label='Testing', color='coral', alpha=0.8)
ax.bar([i + width for i in x], results_df['CV Mean'], width,
       label='CV Mean', color='forestgreen', alpha=0.8)

ax.set_xlabel('Model', fontsize=12)
ax.set_ylabel('Accuracy', fontsize=12)
ax.set_title('Perbandingan Komprehensif: Klasifikasi Batik Indonesia', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(results_df['Model'], rotation=30, ha='right')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3, axis='y')
ax.set_ylim(0.5, 1.05)
plt.tight_layout()
plt.show()

# Classification report untuk model terbaik
best_model_name = results_df.loc[results_df['Test'].idxmax(), 'Model']
best_pipe = pipelines[best_model_name]
best_pipe.fit(X_train, y_train)
y_pred_best = best_pipe.predict(X_test)

print(f"\n=== CLASSIFICATION REPORT: {best_model_name} (TERBAIK) ===")
print(classification_report(y_test, y_pred_best,
                             target_names=le.classes_))

# Rekomendasi
print("\n=== REKOMENDASI ===")
print(f"Model terbaik: {best_model_name}")
print(f"  - Accuracy pada test set: {results_df.loc[results_df['Test'].idxmax(), 'Test']:.4f}")
print(f"  - CV Accuracy: {results_df.loc[results_df['CV Mean'].idxmax(), 'CV Mean']:.4f}")
print(f"\nPertimbangan pemilihan model:")
print(f"  - Jika interpretabilitas penting → Decision Tree")
print(f"  - Jika akurasi tertinggi penting → Random Forest / SVM (RBF)")
print(f"  - Jika kecepatan prediksi penting → Logistic Regression")
print(f"  - Jika data kecil → SVM / KNN")
```

---

## 7.7 AI Corner: Menggunakan AI untuk Memilih Algoritma ML yang Tepat

**Level: Intermediate**

### 7.7.1 Apa yang Bisa AI Bantu?

| AI Bisa | AI Tidak Bisa |
|---------|--------------|
| Menyarankan algoritma berdasarkan karakteristik data | Menjamin algoritma tertentu pasti terbaik |
| Menjelaskan trade-off antar algoritma | Memahami konteks bisnis secara mendalam |
| Membantu tuning hyperparameter | Menentukan apakah ML solusi yang tepat |
| Membuat kode Pipeline dengan cepat | Menggantikan eksperimen dengan data nyata |
| Menginterpretasi hasil perbandingan model | Menjamin hasil generalisasi ke data masa depan |

### 7.7.2 Contoh Prompt yang Baik

```
Prompt 1 (Pemilihan Algoritma):
"Saya memiliki dataset 500 sampel, 10 feature numerik,
2 kelas (imbalanced: 80%/20%), dan perlu model yang
interpretable. Antara KNN, SVM, Decision Tree, dan
Random Forest, mana yang paling cocok? Jelaskan alasannya."

Prompt 2 (Debugging Pipeline):
"Pipeline sklearn saya:
  StandardScaler → PCA(n_components=5) → SVC(kernel='rbf')
menghasilkan accuracy yang lebih rendah dari model tanpa PCA.
Apa kemungkinan penyebabnya?"

Prompt 3 (Optimasi):
"Berikan contoh kode Python lengkap untuk membandingkan
KNN, SVM, Decision Tree, Random Forest, dan Logistic
Regression pada dataset klasifikasi multi-class (3 kelas)
menggunakan Pipeline dan GridSearchCV. Tampilkan
classification report dan confusion matrix untuk model terbaik."
```

### 7.7.3 Alur Kerja dengan AI

```
1. Deskripsikan masalah dan data Anda ke AI
2. Minta AI menyarankan 2-3 algoritma yang cocok
3. Implementasikan sendiri menggunakan Pipeline
4. Minta AI membantu interpretasi hasil
5. Verifikasi jawaban AI dengan literatur
6. Dokumentasikan dalam AI Usage Log
```

### 7.7.4 Template AI Usage Log untuk Bab 7

```markdown
## AI Usage Log — BAB 7: SVM dan KNN

### Interaksi 1
- **Tool:** [Claude / ChatGPT / Copilot]
- **Prompt:** [Copy-paste prompt Anda]
- **Output:** [Ringkasan jawaban AI]
- **Verifikasi:** [Sudah / Belum diverifikasi? Hasilnya?]
- **Modifikasi:** [Apa yang Anda ubah/tambahkan]
- **Refleksi:** [Apa yang Anda pelajari?]
```

---

## Rangkuman Bab 7

1. **K-Nearest Neighbors (KNN)** adalah algoritma lazy learning yang mengklasifikasi data baru berdasarkan voting mayoritas dari K tetangga terdekat. Feature scaling wajib dilakukan karena KNN bergantung pada jarak.

2. Pemilihan **K** melibatkan bias-variance tradeoff: K kecil (overfitting, variance tinggi) vs K besar (underfitting, bias tinggi). Gunakan cross-validation untuk menemukan K optimal.

3. **Support Vector Machine (SVM)** mencari hyperplane pemisah dengan margin terbesar. Kernel trick (linear, polynomial, RBF) memungkinkan SVM menangani data non-linear. Parameter C mengontrol trade-off antara margin dan kesalahan klasifikasi.

4. Tidak ada algoritma yang "terbaik untuk semua masalah" (**No Free Lunch Theorem**). Pemilihan algoritma bergantung pada ukuran data, linearitas, interpretabilitas, dan kebutuhan bisnis.

5. **Cross-validation** (terutama stratified k-fold) memberikan estimasi performa model yang lebih reliable dibandingkan single train-test split.

6. **sklearn Pipeline** menggabungkan preprocessing dan modeling menjadi satu objek, mencegah data leakage dan membuat kode lebih rapi. Pipeline bisa dikombinasikan dengan GridSearchCV untuk hyperparameter tuning yang aman.

7. Dalam perbandingan komprehensif, selalu pertimbangkan **accuracy, waktu komputasi, interpretabilitas**, dan **stabilitas** (CV standard deviation) sebelum memilih model final.

---

## Latihan Soal

### Tingkat Dasar (C2-C3)

**Soal 1.** Jelaskan prinsip kerja KNN menggunakan analogi sederhana. Mengapa KNN disebut "lazy learner"?

**Soal 2.** Hitung jarak Euclidean dan Manhattan antara dua titik data berikut:
- Titik A: (3, 5, 2)
- Titik B: (7, 1, 4)

**Soal 3.** Jelaskan mengapa feature scaling sangat penting untuk KNN dan SVM, tetapi tidak diperlukan untuk Decision Tree.

**Soal 4.** Apa yang dimaksud dengan kernel trick pada SVM? Jelaskan secara intuitif mengapa kernel RBF bisa memisahkan data yang tidak linearly separable.

**Soal 5.** Jelaskan perbedaan antara k-fold cross-validation dan stratified k-fold. Kapan stratified lebih tepat digunakan?

### Tingkat Menengah (C3-C4)

**Soal 6.** Tulis kode Python menggunakan sklearn Pipeline untuk mengklasifikasikan **jenis ikan laut Indonesia** (Tuna, Cakalang, Tongkol) berdasarkan feature: panjang, berat, warna_skala, dan suhu_habitat. Gunakan:
- a) KNN dengan K optimal (cari menggunakan cross-validation)
- b) SVM dengan kernel RBF
- c) Bandingkan keduanya dan tentukan model terbaik

**Soal 7.** Sebuah model KNN (K=1) menghasilkan accuracy 98% pada training set tetapi hanya 65% pada test set. Model KNN lain (K=20) menghasilkan 72% pada training dan 70% pada testing. Analisis:
- a) Apa yang terjadi pada model pertama?
- b) Apa yang terjadi pada model kedua?
- c) Apa solusi yang tepat?

**Soal 8.** Implementasikan GridSearchCV dengan Pipeline untuk mencari kombinasi terbaik dari:
- Scaler: StandardScaler vs MinMaxScaler
- Model: SVM (C=[0.1, 1, 10], kernel=['linear', 'rbf']) vs KNN (K=[3, 5, 7, 11])

Gunakan dataset kualitas kopi dari materi bab ini.

**Soal 9.** Jelaskan dampak parameter C pada SVM. Buat visualisasi decision boundary SVM dengan C=0.01, C=1, dan C=100 pada dataset make_moons.

### Tingkat Mahir (C4-C5)

**Soal 10.** Anda diminta membangun sistem klasifikasi otomatis untuk **jenis batik** berdasarkan fitur citra digital. Dataset memiliki 1000 sampel, 20 feature, dan 5 kelas. Implementasikan pipeline lengkap yang mencakup:
- a) Eksplorasi data awal
- b) Feature selection (pilih 10 fitur terbaik)
- c) Perbandingan 5 algoritma menggunakan cross-validation
- d) Hyperparameter tuning untuk 2 model terbaik
- e) Evaluasi final pada test set dengan classification report
- f) Rekomendasi model terbaik dengan justifikasi

**Soal 11.** Implementasikan KNN dari nol (tanpa sklearn). Kode Anda harus:
- a) Menghitung jarak Euclidean
- b) Menemukan K tetangga terdekat
- c) Melakukan voting mayoritas
- d) Menghitung accuracy
- e) Bandingkan hasilnya dengan `KNeighborsClassifier` dari sklearn

**Soal 12.** Lakukan eksperimen komprehensif untuk menjawab: "Apakah SVM atau Random Forest lebih baik untuk dataset kecil (n < 500) dengan banyak feature (p > 20)?" Buat dataset sintetik dengan berbagai ukuran dan jumlah feature, lalu buat plot perbandingan yang mendukung kesimpulan Anda.

---

## Referensi

1. Cover, T. M., & Hart, P. E. (1967). Nearest Neighbor Pattern Classification. *IEEE Transactions on Information Theory*, 13(1), 21-27.
2. Cortes, C., & Vapnik, V. (1995). Support-Vector Networks. *Machine Learning*, 20(3), 273-297.
3. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2023). *An Introduction to Statistical Learning* (2nd ed.). Springer.
4. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
5. Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.
6. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.
7. Schölkopf, B., & Smola, A. J. (2002). *Learning with Kernels*. MIT Press.

---

*Bab berikutnya: **Bab 8 — Neural Networks dan Deep Learning***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
