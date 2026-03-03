# Lab 07: SVM, KNN, dan Model Evaluation

**Mata Kuliah:** Kecerdasan Buatan dan Machine Learning
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Minggu:** 7
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

- Membangun model KNeighborsClassifier dan menganalisis pengaruh nilai K
- Membangun model SVC dengan kernel linear dan RBF
- Memvisualisasikan decision boundary pada ruang 2D
- Melakukan cross-validation menggunakan cross_val_score
- Membandingkan performa beberapa model klasifikasi secara sistematis
- Membangun pipeline preprocessing dan klasifikasi
- Menyusun tabel perbandingan model lengkap

---

## Persiapan

1. Buka Google Colab dan buat notebook baru
2. Nama file: `Lab07_NamaAnda_NIM.ipynb`
3. Pastikan library pandas, numpy, matplotlib, seaborn, dan scikit-learn sudah tersedia
4. Pahami konsep SVM dan KNN dari kuliah teori

---

## Langkah-langkah

### Langkah 1: KNeighborsClassifier - Variasi K

```python
# =============================================
# LANGKAH 1: KNN - Variasi Nilai K
# =============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_classification

# Pengaturan tampilan
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)
np.random.seed(42)

print("=" * 60)
print("KNN - K-NEAREST NEIGHBORS CLASSIFIER")
print("=" * 60)

# --- Buat Dataset Simulasi Diagnosa Penyakit ---
n = 600

data_medis = {
    'usia': np.random.normal(45, 15, n).clip(18, 80).astype(int),
    'bmi': np.round(np.random.normal(25, 5, n).clip(15, 45), 1),
    'tekanan_darah': np.random.normal(120, 20, n).clip(80, 200).astype(int),
    'gula_darah': np.random.normal(100, 30, n).clip(60, 300).astype(int),
    'kolesterol': np.random.normal(200, 40, n).clip(100, 400).astype(int),
    'detak_jantung': np.random.normal(75, 12, n).clip(50, 120).astype(int),
    'riwayat_keluarga': np.random.choice([0, 1], n, p=[0.60, 0.40]),
    'aktivitas_fisik': np.random.choice([0, 1, 2], n, p=[0.30, 0.45, 0.25]),  # rendah, sedang, tinggi
}

df = pd.DataFrame(data_medis)

# Generate target (risiko penyakit jantung)
logit = (-5 + 0.03 * df['usia'] + 0.08 * df['bmi']
         + 0.02 * df['tekanan_darah'] + 0.01 * df['gula_darah']
         + 0.005 * df['kolesterol'] + 0.8 * df['riwayat_keluarga']
         - 0.5 * df['aktivitas_fisik'] + np.random.normal(0, 0.5, n))
prob = 1 / (1 + np.exp(-logit))
df['risiko_jantung'] = (prob > 0.5).astype(int)

print(f"Dataset Medis: {df.shape[0]} baris x {df.shape[1]} kolom")
print(f"Distribusi target:\n{df['risiko_jantung'].value_counts()}")

# --- Persiapan Data ---
fitur_cols = ['usia', 'bmi', 'tekanan_darah', 'gula_darah',
              'kolesterol', 'detak_jantung', 'riwayat_keluarga', 'aktivitas_fisik']

X = df[fitur_cols].values
y = df['risiko_jantung'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scaling (penting untuk KNN!)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# --- Variasi nilai K ---
k_values = range(1, 31)
train_accs = []
test_accs = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_s, y_train)
    train_accs.append(knn.score(X_train_s, y_train))
    test_accs.append(knn.score(X_test_s, y_test))

# Temukan K optimal
best_k = k_values[np.argmax(test_accs)]
best_acc = max(test_accs)

print(f"\n--- Variasi K ---")
print(f"K optimal: {best_k} (akurasi test = {best_acc:.4f})")

# --- Visualisasi ---
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(k_values, train_accs, 'b-o', markersize=4, linewidth=1.5, label='Training Accuracy')
ax.plot(k_values, test_accs, 'r-o', markersize=4, linewidth=1.5, label='Testing Accuracy')
ax.axvline(x=best_k, color='green', linestyle='--', alpha=0.7,
           label=f'Best K = {best_k} (acc = {best_acc:.3f})')

ax.set_xlabel('Nilai K (Jumlah Tetangga)', fontsize=12)
ax.set_ylabel('Accuracy', fontsize=12)
ax.set_title('KNN: Pengaruh Nilai K terhadap Akurasi', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_xticks(range(1, 31, 2))

plt.tight_layout()
plt.show()

print(f"""
Observasi:
- K kecil (1-3): Overfitting - terlalu sensitif terhadap noise
- K besar (>20): Underfitting - terlalu general, mengabaikan pola lokal
- K optimal ({best_k}): Keseimbangan antara bias dan variance
- Catatan: K ganjil lebih disarankan untuk menghindari tie (seri)
""")
```

### Langkah 2: SVC - Linear Kernel vs RBF Kernel

```python
# =============================================
# LANGKAH 2: SVM - Support Vector Machine
# =============================================

print("=" * 60)
print("SVM - SUPPORT VECTOR MACHINE")
print("=" * 60)

# --- SVM dengan kernel Linear ---
svm_linear = SVC(kernel='linear', C=1.0, random_state=42)
svm_linear.fit(X_train_s, y_train)
y_pred_linear = svm_linear.predict(X_test_s)
acc_linear = accuracy_score(y_test, y_pred_linear)

print(f"SVM Linear Kernel:")
print(f"  Akurasi: {acc_linear:.4f}")
print(f"  Jumlah Support Vectors: {svm_linear.n_support_}")

# --- SVM dengan kernel RBF ---
svm_rbf = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
svm_rbf.fit(X_train_s, y_train)
y_pred_rbf = svm_rbf.predict(X_test_s)
acc_rbf = accuracy_score(y_test, y_pred_rbf)

print(f"\nSVM RBF Kernel:")
print(f"  Akurasi: {acc_rbf:.4f}")
print(f"  Jumlah Support Vectors: {svm_rbf.n_support_}")

# --- Variasi parameter C ---
print(f"\n--- Efek Parameter C (Regularisasi) ---")
C_values = [0.001, 0.01, 0.1, 1, 10, 100]

for C in C_values:
    svm_temp = SVC(kernel='rbf', C=C, gamma='scale', random_state=42)
    svm_temp.fit(X_train_s, y_train)
    train_acc = svm_temp.score(X_train_s, y_train)
    test_acc = svm_temp.score(X_test_s, y_test)
    print(f"  C = {C:>7.3f} | Train: {train_acc:.4f} | Test: {test_acc:.4f} | SV: {sum(svm_temp.n_support_)}")

# --- Variasi kernel ---
print(f"\n--- Perbandingan Kernel ---")
kernels = ['linear', 'rbf', 'poly', 'sigmoid']
for kernel in kernels:
    try:
        svm_k = SVC(kernel=kernel, C=1.0, random_state=42)
        svm_k.fit(X_train_s, y_train)
        acc = svm_k.score(X_test_s, y_test)
        print(f"  Kernel {kernel:>8s}: Akurasi = {acc:.4f}")
    except Exception as e:
        print(f"  Kernel {kernel:>8s}: Error - {e}")
```

### Langkah 3: Visualisasi Decision Boundary (2D)

```python
# =============================================
# LANGKAH 3: Visualisasi Decision Boundary
# =============================================

# Gunakan hanya 2 fitur terbaik untuk visualisasi 2D
# Pilih BMI dan tekanan darah
X_2d = df[['bmi', 'tekanan_darah']].values
y_2d = df['risiko_jantung'].values

X_train_2d, X_test_2d, y_train_2d, y_test_2d = train_test_split(
    X_2d, y_2d, test_size=0.2, random_state=42, stratify=y_2d
)

scaler_2d = StandardScaler()
X_train_2ds = scaler_2d.fit_transform(X_train_2d)
X_test_2ds = scaler_2d.transform(X_test_2d)

# --- Latih 4 model ---
models_2d = {
    'KNN (K=5)': KNeighborsClassifier(n_neighbors=5),
    'SVM Linear': SVC(kernel='linear', C=1.0, random_state=42),
    'SVM RBF': SVC(kernel='rbf', C=1.0, random_state=42),
    'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=42),
}

fig, axes = plt.subplots(2, 2, figsize=(14, 12))

for ax, (name, model) in zip(axes.flatten(), models_2d.items()):
    # Fit model
    model.fit(X_train_2ds, y_train_2d)
    acc = model.score(X_test_2ds, y_test_2d)

    # Buat grid untuk decision boundary
    x_min, x_max = X_train_2ds[:, 0].min() - 1, X_train_2ds[:, 0].max() + 1
    y_min, y_max = X_train_2ds[:, 1].min() - 1, X_train_2ds[:, 1].max() + 1
    xx, yy = np.meshgrid(
        np.arange(x_min, x_max, 0.02),
        np.arange(y_min, y_max, 0.02)
    )
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot
    ax.contourf(xx, yy, Z, alpha=0.3, cmap='RdBu')
    ax.scatter(X_test_2ds[y_test_2d == 0, 0], X_test_2ds[y_test_2d == 0, 1],
               c='blue', label='Tidak Risiko', edgecolors='black', s=30, alpha=0.7)
    ax.scatter(X_test_2ds[y_test_2d == 1, 0], X_test_2ds[y_test_2d == 1, 1],
               c='red', label='Risiko', edgecolors='black', s=30, alpha=0.7)
    ax.set_xlabel('BMI (scaled)', fontsize=10)
    ax.set_ylabel('Tekanan Darah (scaled)', fontsize=10)
    ax.set_title(f'{name}\nAkurasi: {acc:.3f}', fontsize=12)
    ax.legend(fontsize=8, loc='upper right')

plt.suptitle('Perbandingan Decision Boundary (2D)', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.show()

print("Decision boundary menunjukkan bagaimana tiap model membagi ruang fitur.")
print("- SVM Linear: batas linier (garis lurus)")
print("- SVM RBF: batas non-linier (kurva fleksibel)")
print("- KNN: batas non-linier berbasis jarak tetangga")
print("- Decision Tree: batas berbentuk kotak (axis-aligned)")
```

### Langkah 4: Cross-Validation dengan k-Fold

```python
# =============================================
# LANGKAH 4: Cross-Validation
# =============================================

print("=" * 60)
print("CROSS-VALIDATION (K-FOLD)")
print("=" * 60)

# Model yang akan dibandingkan (menggunakan semua fitur)
models_cv = {
    'KNN (K=5)': KNeighborsClassifier(n_neighbors=best_k),
    'SVM Linear': SVC(kernel='linear', C=1.0, random_state=42),
    'SVM RBF': SVC(kernel='rbf', C=1.0, random_state=42),
}

# --- Cross-Validation 5-Fold ---
print(f"\n--- 5-Fold Cross-Validation (data sudah di-scale) ---")

# Gabungkan data untuk CV
X_all_s = np.vstack([X_train_s, X_test_s])
y_all = np.concatenate([y_train, y_test])

cv_results = {}
for name, model in models_cv.items():
    scores = cross_val_score(model, X_all_s, y_all, cv=5, scoring='accuracy')
    cv_results[name] = scores
    print(f"\n{name}:")
    print(f"  Fold scores : {scores.round(4)}")
    print(f"  Mean (+/-std): {scores.mean():.4f} (+/- {scores.std():.4f})")

# --- Variasi jumlah fold ---
print(f"\n--- Efek Jumlah Fold pada SVM RBF ---")
for k_fold in [3, 5, 10, 15]:
    scores = cross_val_score(SVC(kernel='rbf', C=1.0, random_state=42),
                             X_all_s, y_all, cv=k_fold, scoring='accuracy')
    print(f"  {k_fold:2d}-Fold: {scores.mean():.4f} +/- {scores.std():.4f}")

# --- Visualisasi ---
fig, ax = plt.subplots(figsize=(10, 6))

positions = range(len(cv_results))
bp = ax.boxplot(cv_results.values(), positions=positions, widths=0.6,
                patch_artist=True, showmeans=True,
                meanprops=dict(marker='D', markerfacecolor='red', markersize=8))

colors_box = ['#3498db', '#e74c3c', '#2ecc71']
for patch, color in zip(bp['boxes'], colors_box):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax.set_xticks(positions)
ax.set_xticklabels(cv_results.keys(), fontsize=11)
ax.set_ylabel('Accuracy', fontsize=12)
ax.set_title('5-Fold Cross-Validation Results', fontsize=14)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

### Langkah 5: Perbandingan Model Lengkap

```python
# =============================================
# LANGKAH 5: Perbandingan Model Lengkap
# =============================================

print("=" * 60)
print("PERBANDINGAN 5 MODEL KLASIFIKASI")
print("=" * 60)

# Definisi semua model
all_models = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=7, random_state=42),
    'SVM (RBF)': SVC(kernel='rbf', C=1.0, random_state=42),
    'KNN': KNeighborsClassifier(n_neighbors=best_k),
}

# Evaluasi setiap model
results = []
for name, model in all_models.items():
    # Fit model
    model.fit(X_train_s, y_train)

    # Prediksi
    y_pred = model.predict(X_test_s)

    # Metrik
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    # Cross-validation
    cv_scores = cross_val_score(model, X_all_s, y_all, cv=5, scoring='accuracy')

    results.append({
        'Model': name,
        'Test Accuracy': acc,
        'CV Mean': cv_scores.mean(),
        'CV Std': cv_scores.std(),
        'Precision (1)': report['1']['precision'],
        'Recall (1)': report['1']['recall'],
        'F1 (1)': report['1']['f1-score'],
    })

    print(f"\n{name}:")
    print(f"  Test Accuracy : {acc:.4f}")
    print(f"  CV Accuracy   : {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
    print(f"  Precision (1) : {report['1']['precision']:.4f}")
    print(f"  Recall (1)    : {report['1']['recall']:.4f}")
    print(f"  F1-Score (1)  : {report['1']['f1-score']:.4f}")

# --- Tabel Ringkasan ---
df_results = pd.DataFrame(results)
print(f"\n{'=' * 80}")
print("TABEL PERBANDINGAN MODEL")
print(f"{'=' * 80}")
print(df_results.to_string(index=False, float_format='{:.4f}'.format))

# --- Visualisasi Perbandingan ---
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Barplot akurasi
ax = axes[0]
colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6']
bars = ax.bar(df_results['Model'], df_results['Test Accuracy'], color=colors,
              edgecolor='white', alpha=0.8)
for bar, acc in zip(bars, df_results['Test Accuracy']):
    ax.text(bar.get_x() + bar.get_width()/2., acc + 0.003,
            f'{acc:.3f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_ylabel('Test Accuracy', fontsize=12)
ax.set_title('Perbandingan Akurasi Model', fontsize=13)
ax.tick_params(axis='x', rotation=30)
ax.set_ylim(0.5, 1.0)
ax.grid(axis='y', alpha=0.3)

# Plot 2: Heatmap metrik
ax = axes[1]
metrik_cols = ['Test Accuracy', 'CV Mean', 'Precision (1)', 'Recall (1)', 'F1 (1)']
heatmap_data = df_results[metrik_cols].values
sns.heatmap(heatmap_data, annot=True, fmt='.3f', cmap='YlOrRd',
            xticklabels=metrik_cols, yticklabels=df_results['Model'],
            ax=ax, linewidths=0.5)
ax.set_title('Heatmap Metrik Evaluasi', fontsize=13)

plt.tight_layout()
plt.show()
```

### Langkah 6: Pipeline (StandardScaler + Classifier)

```python
# =============================================
# LANGKAH 6: Pipeline
# =============================================

print("=" * 60)
print("SKLEARN PIPELINE: PREPROCESSING + KLASIFIKASI")
print("=" * 60)

# Gunakan data TANPA scaling (pipeline akan handle scaling)
X_train_raw, X_test_raw, y_train_raw, y_test_raw = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# --- Definisi Pipeline ---
pipelines = {
    'Logistic + Scaler': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(random_state=42, max_iter=1000))
    ]),
    'KNN + Scaler': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', KNeighborsClassifier(n_neighbors=best_k))
    ]),
    'SVM + Scaler': Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', SVC(kernel='rbf', C=1.0, random_state=42))
    ]),
    'RF (no scaler)': Pipeline([
        ('classifier', RandomForestClassifier(n_estimators=100, max_depth=7, random_state=42))
    ]),
    'DT (no scaler)': Pipeline([
        ('classifier', DecisionTreeClassifier(max_depth=5, random_state=42))
    ]),
}

print("Pipeline menyederhanakan preprocessing + modeling:")
print("  Pipeline = StandardScaler → Classifier")
print("  - Otomatis fit scaler pada training data")
print("  - Otomatis transform testing data")
print("  - Mencegah data leakage!")

pipe_results = {}
for name, pipe in pipelines.items():
    # Fit pipeline (scaler + model sekaligus)
    pipe.fit(X_train_raw, y_train_raw)

    # Predict dan evaluate
    acc = pipe.score(X_test_raw, y_test_raw)

    # Cross-validation pada pipeline
    cv = cross_val_score(pipe, X, y, cv=5, scoring='accuracy')

    pipe_results[name] = {
        'Test Acc': acc,
        'CV Mean': cv.mean(),
        'CV Std': cv.std()
    }

    print(f"\n{name}:")
    print(f"  Steps     : {[step[0] for step in pipe.steps]}")
    print(f"  Test Acc  : {acc:.4f}")
    print(f"  CV        : {cv.mean():.4f} +/- {cv.std():.4f}")

# Tampilkan ringkasan pipeline
print(f"\n{'=' * 60}")
print(f"{'Pipeline':<25} {'Test Acc':>10} {'CV Mean':>10} {'CV Std':>10}")
print(f"{'-'*55}")
for name, res in pipe_results.items():
    print(f"{name:<25} {res['Test Acc']:>10.4f} {res['CV Mean']:>10.4f} {res['CV Std']:>10.4f}")

print(f"""
Catatan:
- KNN dan SVM MEMERLUKAN scaling → gunakan Pipeline dengan StandardScaler
- Decision Tree dan Random Forest TIDAK memerlukan scaling
- Pipeline memastikan preprocessing dilakukan dengan benar
- Cross-validation pada Pipeline mencegah data leakage
""")
```

### Langkah 7: Tabel Perbandingan Ringkasan

```python
# =============================================
# LANGKAH 7: Tabel Perbandingan Ringkasan
# =============================================

print("=" * 70)
print("TABEL PERBANDINGAN RINGKASAN - SEMUA MODEL")
print("=" * 70)

# --- Buat tabel lengkap ---
summary_data = {
    'Model': ['Logistic Regression', 'Decision Tree', 'Random Forest', 'SVM (RBF)', f'KNN (K={best_k})'],
    'Tipe': ['Linear', 'Non-linear', 'Ensemble', 'Non-linear', 'Instance-based'],
    'Perlu Scaling': ['Ya', 'Tidak', 'Tidak', 'Ya', 'Ya'],
    'Interpretable': ['Tinggi', 'Tinggi', 'Sedang', 'Rendah', 'Rendah'],
    'Kecepatan Training': ['Cepat', 'Cepat', 'Sedang', 'Lambat', 'Cepat'],
    'Kecepatan Prediksi': ['Cepat', 'Cepat', 'Sedang', 'Cepat', 'Lambat'],
}

# Tambahkan skor dari evaluasi sebelumnya
for i, name in enumerate(['Logistic Regression', 'Decision Tree', 'Random Forest', 'SVM (RBF)', 'KNN']):
    if i < len(df_results):
        summary_data.setdefault('Test Accuracy', []).append(f"{df_results.iloc[i]['Test Accuracy']:.4f}")
        summary_data.setdefault('CV Mean', []).append(f"{df_results.iloc[i]['CV Mean']:.4f}")
        summary_data.setdefault('F1-Score', []).append(f"{df_results.iloc[i]['F1 (1)']:.4f}")

df_summary = pd.DataFrame(summary_data)
print(df_summary.to_string(index=False))

# --- Rekomendasi ---
best_model_idx = df_results['CV Mean'].idxmax()
best_model_name = df_results.loc[best_model_idx, 'Model']
best_cv = df_results.loc[best_model_idx, 'CV Mean']

print(f"""
{'=' * 70}
REKOMENDASI
{'=' * 70}

Model Terbaik: {best_model_name} (CV Accuracy = {best_cv:.4f})

Panduan Pemilihan Model:
1. Data kecil, perlu interpretasi → Decision Tree
2. Data besar, akurasi tinggi    → Random Forest
3. Data linier, baseline cepat   → Logistic Regression
4. Decision boundary kompleks    → SVM (RBF)
5. Data kecil, pola non-linier   → KNN

Kapan gunakan Pipeline:
- SELALU gunakan Pipeline untuk model yang memerlukan scaling
- Pipeline mencegah data leakage pada cross-validation
- Pipeline mempermudah deployment model
""")

# --- Visualisasi Radar Chart ---
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

categories = ['Test Acc', 'CV Mean', 'Precision', 'Recall', 'F1-Score']
N = len(categories)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]  # Tutup lingkaran

for i, (_, row) in enumerate(df_results.iterrows()):
    values = [row['Test Accuracy'], row['CV Mean'],
              row['Precision (1)'], row['Recall (1)'], row['F1 (1)']]
    values += values[:1]
    ax.plot(angles, values, 'o-', linewidth=2, label=row['Model'], alpha=0.7)
    ax.fill(angles, values, alpha=0.05)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11)
ax.set_ylim(0, 1)
ax.set_title('Perbandingan Model - Radar Chart', fontsize=14, pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9)

plt.tight_layout()
plt.show()

print("\nLab 07 selesai! Anda telah mempelajari KNN, SVM, dan evaluasi model secara komprehensif.")
```

---

## Tantangan Tambahan

1. **Weighted KNN:** Implementasikan KNN dengan parameter `weights='distance'` (tetangga yang lebih dekat memiliki bobot lebih besar). Bandingkan akurasinya dengan KNN uniform standar pada berbagai nilai K.

2. **SVM Multiclass:** Gunakan dataset `load_wine()` dari sklearn (3 kelas). Latih model SVM dengan berbagai kernel dan C. Buat confusion matrix 3x3 dan bandingkan strategi multiclass (OvR vs OvO).

3. **Ensemble Voting:** Buat `VotingClassifier` yang menggabungkan prediksi dari Logistic Regression, SVM, KNN, dan Random Forest. Bandingkan akurasi voting (hard dan soft) dengan akurasi model individual.

---

## Checklist Penyelesaian

- [ ] KNeighborsClassifier berhasil dibangun dengan variasi K dan divisualisasikan
- [ ] SVC berhasil dibangun dengan kernel linear dan RBF
- [ ] Decision boundary berhasil divisualisasikan pada ruang 2D
- [ ] Cross-validation berhasil dilakukan dengan k-fold
- [ ] Perbandingan 5 model (Logistic, Tree, RF, SVM, KNN) berhasil dibuat
- [ ] Pipeline (StandardScaler + Classifier) berhasil diimplementasi
- [ ] Tabel perbandingan ringkasan dan radar chart berhasil dibuat
- [ ] Notebook disimpan dengan nama `Lab07_NamaAnda_NIM.ipynb`
- [ ] Minimal 1 tantangan tambahan diselesaikan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
