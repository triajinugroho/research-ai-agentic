# Lab 14: AI-Augmented ML Pipeline

**Mata Kuliah:** Kecerdasan Buatan dan Machine Learning
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Minggu:** 14
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

- Mendefinisikan problem statement ML dengan konteks Indonesia
- Memuat, mengeksplorasi, dan memahami dataset secara sistematis
- Membangun preprocessing pipeline menggunakan `sklearn.Pipeline`
- Melakukan model selection dengan mencoba beberapa algoritma
- Melakukan hyperparameter tuning dengan `GridSearchCV`
- Mengevaluasi model terbaik secara komprehensif
- Menyimpan dan memuat model dengan `joblib`
- Mendokumentasikan penggunaan AI dalam proses pengembangan ML

---

## Persiapan

1. Buka Google Colab notebook baru
2. Nama file: `Lab14_NamaAnda_NIM.ipynb`
3. Pastikan library `scikit-learn`, `pandas`, `numpy`, `matplotlib`, dan `joblib` sudah bisa diimpor

---

## Langkah-langkah

### Langkah 1: Definisi Problem Statement

```python
# =============================================
# LANGKAH 1: Definisi Problem Statement
# =============================================

print("=" * 60)
print("ML PIPELINE — PREDIKSI KELAYAKAN KREDIT NASABAH")
print("=" * 60)

print("""
PROBLEM STATEMENT:
==================
Sebuah bank di Indonesia ingin memprediksi apakah seorang
nasabah layak mendapatkan kredit atau tidak, berdasarkan
data profil dan riwayat keuangan nasabah.

TUJUAN:
- Membangun model klasifikasi untuk prediksi kelayakan kredit
- Mengidentifikasi faktor-faktor yang mempengaruhi keputusan kredit

KONTEKS INDONESIA:
- Nasabah berasal dari berbagai kota di Indonesia
- Pendapatan dalam satuan juta Rupiah
- Menggunakan data simulasi yang realistis

METRIK EVALUASI:
- Accuracy, Precision, Recall, F1-Score
- Fokus pada Recall (meminimalkan nasabah berisiko yang lolos)

TIPE PROBLEM: Supervised Learning — Binary Classification
TARGET: layak_kredit (0 = Tidak Layak, 1 = Layak)
""")

# Log penggunaan AI
print("\n--- AI Usage Log ---")
print("Prompt 1: 'Bantu saya mendefinisikan problem statement ML")
print("           untuk prediksi kelayakan kredit di Indonesia'")
print("AI Tool : ChatGPT / Claude")
print("Hasil   : Mendapatkan kerangka problem statement di atas")
```

### Langkah 2: Load dan Eksplorasi Dataset

```python
# =============================================
# LANGKAH 2: Load dan Eksplorasi Dataset
# =============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate dataset simulasi kelayakan kredit
np.random.seed(42)
n = 500

data = {
    'usia': np.random.randint(21, 60, size=n),
    'pendapatan_juta': np.round(np.random.lognormal(2.0, 0.6, size=n), 1),
    'jumlah_tanggungan': np.random.choice([0, 1, 2, 3, 4, 5], size=n,
                                           p=[0.15, 0.20, 0.25, 0.20, 0.12, 0.08]),
    'lama_bekerja_tahun': np.random.randint(0, 30, size=n),
    'total_aset_juta': np.round(np.random.lognormal(3.0, 1.0, size=n), 1),
    'jumlah_pinjaman_aktif': np.random.choice([0, 1, 2, 3, 4], size=n,
                                               p=[0.30, 0.30, 0.20, 0.15, 0.05]),
    'skor_kredit': np.random.randint(300, 850, size=n),
    'pendidikan': np.random.choice(['SMA', 'D3', 'S1', 'S2'], size=n,
                                    p=[0.25, 0.20, 0.40, 0.15]),
    'status_pernikahan': np.random.choice(['Belum Menikah', 'Menikah', 'Cerai'],
                                           size=n, p=[0.30, 0.55, 0.15]),
    'kota': np.random.choice(['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Makassar'],
                              size=n, p=[0.30, 0.20, 0.20, 0.15, 0.15]),
}

df = pd.DataFrame(data)

# Generate target berdasarkan aturan logis
score = (
    (df['skor_kredit'] - 300) / 550 * 40 +
    np.minimum(df['pendapatan_juta'] / 30, 1) * 25 +
    np.minimum(df['lama_bekerja_tahun'] / 15, 1) * 15 +
    (4 - df['jumlah_pinjaman_aktif']) / 4 * 10 +
    np.minimum(df['total_aset_juta'] / 200, 1) * 10
)
noise = np.random.normal(0, 8, size=n)
df['layak_kredit'] = (score + noise > 50).astype(int)

print("=== EKSPLORASI DATASET ===")
print(f"Dimensi: {df.shape[0]} baris x {df.shape[1]} kolom")
print(f"\nDistribusi target:")
print(df['layak_kredit'].value_counts().rename({1: 'Layak', 0: 'Tidak Layak'}))

print(f"\nInfo dataset:")
print(df.info())

print(f"\nStatistik deskriptif:")
print(df.describe().round(2))

# Visualisasi distribusi target
fig, axes = plt.subplots(1, 3, figsize=(16, 4))

# Distribusi target
df['layak_kredit'].value_counts().plot(kind='bar', ax=axes[0],
    color=['#e74c3c', '#2ecc71'], edgecolor='white')
axes[0].set_title('Distribusi Kelayakan Kredit')
axes[0].set_xticklabels(['Tidak Layak', 'Layak'], rotation=0)

# Distribusi pendapatan per kelas
for label, color in zip([0, 1], ['#e74c3c', '#2ecc71']):
    mask = df['layak_kredit'] == label
    name = 'Layak' if label == 1 else 'Tidak Layak'
    axes[1].hist(df.loc[mask, 'pendapatan_juta'], bins=20, alpha=0.6,
                 color=color, label=name)
axes[1].set_title('Distribusi Pendapatan per Kelas')
axes[1].set_xlabel('Pendapatan (Juta Rp)')
axes[1].legend()

# Distribusi skor kredit per kelas
for label, color in zip([0, 1], ['#e74c3c', '#2ecc71']):
    mask = df['layak_kredit'] == label
    name = 'Layak' if label == 1 else 'Tidak Layak'
    axes[2].hist(df.loc[mask, 'skor_kredit'], bins=20, alpha=0.6,
                 color=color, label=name)
axes[2].set_title('Distribusi Skor Kredit per Kelas')
axes[2].set_xlabel('Skor Kredit')
axes[2].legend()

plt.tight_layout()
plt.show()
```

### Langkah 3: Preprocessing Pipeline

```python
# =============================================
# LANGKAH 3: Preprocessing Pipeline
# =============================================

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

# Pisahkan fitur dan target
X = df.drop('layak_kredit', axis=1)
y = df['layak_kredit']

# Identifikasi kolom numerik dan kategorikal
kolom_numerik = ['usia', 'pendapatan_juta', 'jumlah_tanggungan',
                 'lama_bekerja_tahun', 'total_aset_juta',
                 'jumlah_pinjaman_aktif', 'skor_kredit']
kolom_kategorikal = ['pendidikan', 'status_pernikahan', 'kota']

print("=== PREPROCESSING PIPELINE ===")
print(f"Fitur numerik ({len(kolom_numerik)}): {kolom_numerik}")
print(f"Fitur kategorikal ({len(kolom_kategorikal)}): {kolom_kategorikal}")

# Pipeline untuk fitur numerik
pipeline_numerik = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),  # Isi missing value
    ('scaler', StandardScaler())                     # Standardisasi
])

# Pipeline untuk fitur kategorikal
pipeline_kategorikal = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),  # Isi missing value
    ('encoder', OneHotEncoder(drop='first', sparse_output=False))  # One-hot encoding
])

# Gabungkan dalam ColumnTransformer
preprocessor = ColumnTransformer([
    ('num', pipeline_numerik, kolom_numerik),
    ('cat', pipeline_kategorikal, kolom_kategorikal)
])

# Split data: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTraining set: {X_train.shape[0]} sampel")
print(f"Test set: {X_test.shape[0]} sampel")

# Uji preprocessing
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

print(f"\nShape setelah preprocessing:")
print(f"  Training: {X_train_processed.shape}")
print(f"  Test: {X_test_processed.shape}")
print(f"\nPipeline berhasil dibuat!")
```

### Langkah 4: Model Selection — Coba Beberapa Algoritma

```python
# =============================================
# LANGKAH 4: Model Selection
# =============================================

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

print("=" * 60)
print("MODEL SELECTION — MEMBANDINGKAN 6 ALGORITMA")
print("=" * 60)

# Definisikan model-model kandidat
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
    'SVM (RBF)': SVC(kernel='rbf', random_state=42),
    'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=5),
}

# Evaluasi setiap model dengan cross-validation
results = {}
print(f"\n{'Model':<25} {'Akurasi (CV)':>12} {'Std':>8}")
print("-" * 47)

for name, model in models.items():
    # Buat pipeline lengkap (preprocessing + model)
    full_pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', model)
    ])

    # Cross-validation 5-fold
    scores = cross_val_score(full_pipeline, X_train, y_train,
                             cv=5, scoring='accuracy')
    results[name] = {'mean': scores.mean(), 'std': scores.std(),
                     'scores': scores}
    print(f"{name:<25} {scores.mean():>12.4f} {scores.std():>8.4f}")

# Visualisasi perbandingan
plt.figure(figsize=(10, 5))
names = list(results.keys())
means = [r['mean'] for r in results.values()]
stds = [r['std'] for r in results.values()]

colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c']
bars = plt.bar(range(len(names)), means, yerr=stds, capsize=5,
               color=colors, edgecolor='white')
plt.xticks(range(len(names)), names, rotation=30, ha='right')
plt.ylabel('Akurasi (5-Fold CV)')
plt.title('Perbandingan Algoritma — Prediksi Kelayakan Kredit')
plt.grid(axis='y', alpha=0.3)

for bar, mean in zip(bars, means):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
             f'{mean:.3f}', ha='center', fontsize=10)

plt.tight_layout()
plt.show()

# Pilih model terbaik
best_model_name = max(results, key=lambda x: results[x]['mean'])
print(f"\nModel terbaik: {best_model_name} "
      f"(Akurasi: {results[best_model_name]['mean']:.4f})")
```

### Langkah 5: Hyperparameter Tuning dengan GridSearchCV

```python
# =============================================
# LANGKAH 5: Hyperparameter Tuning
# =============================================

from sklearn.model_selection import GridSearchCV

print("=" * 60)
print("HYPERPARAMETER TUNING — GridSearchCV")
print("=" * 60)

# Pipeline dengan Random Forest (atau model terbaik)
pipeline_tuning = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Grid parameter untuk Random Forest
param_grid = {
    'classifier__n_estimators': [50, 100, 200],
    'classifier__max_depth': [5, 10, 20, None],
    'classifier__min_samples_split': [2, 5, 10],
    'classifier__min_samples_leaf': [1, 2, 4],
}

print(f"Jumlah kombinasi parameter: "
      f"{3 * 4 * 3 * 3} = {3*4*3*3}")

# GridSearchCV
grid_search = GridSearchCV(
    pipeline_tuning,
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,        # Gunakan semua CPU core
    verbose=1
)

print("\nMemulai Grid Search (ini mungkin membutuhkan beberapa menit)...")
grid_search.fit(X_train, y_train)

print(f"\n=== HASIL GRID SEARCH ===")
print(f"Best Score (CV): {grid_search.best_score_:.4f}")
print(f"\nBest Parameters:")
for param, value in grid_search.best_params_.items():
    param_name = param.replace('classifier__', '')
    print(f"  {param_name}: {value}")

# Top 5 kombinasi parameter
results_df = pd.DataFrame(grid_search.cv_results_)
top5 = results_df.nsmallest(5, 'rank_test_score')[
    ['rank_test_score', 'mean_test_score', 'std_test_score', 'params']
]
print(f"\nTop 5 kombinasi:")
for _, row in top5.iterrows():
    print(f"  Rank {int(row['rank_test_score'])}: "
          f"Akurasi = {row['mean_test_score']:.4f} "
          f"(+/- {row['std_test_score']:.4f})")
```

### Langkah 6: Evaluasi Model Terbaik

```python
# =============================================
# LANGKAH 6: Evaluasi Model Terbaik
# =============================================

from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, classification_report, confusion_matrix,
                             roc_curve, auc)

# Gunakan model terbaik dari GridSearchCV
best_model = grid_search.best_estimator_

# Prediksi pada test set
y_pred = best_model.predict(X_test)
y_pred_prob = best_model.predict_proba(X_test)[:, 1]

print("=== EVALUASI MODEL TERBAIK PADA TEST SET ===\n")
print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall   : {recall_score(y_test, y_pred):.4f}")
print(f"F1-Score : {f1_score(y_test, y_pred):.4f}")

print(f"\n--- Classification Report ---")
print(classification_report(y_test, y_pred,
                            target_names=['Tidak Layak', 'Layak']))

# Visualisasi
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0],
            xticklabels=['Tidak Layak', 'Layak'],
            yticklabels=['Tidak Layak', 'Layak'])
axes[0].set_xlabel('Prediksi')
axes[0].set_ylabel('Aktual')
axes[0].set_title('Confusion Matrix')

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
roc_auc = auc(fpr, tpr)

axes[1].plot(fpr, tpr, 'b-', linewidth=2,
             label=f'ROC (AUC = {roc_auc:.4f})')
axes[1].plot([0, 1], [0, 1], 'r--', alpha=0.5, label='Random')
axes[1].set_xlabel('False Positive Rate')
axes[1].set_ylabel('True Positive Rate')
axes[1].set_title('ROC Curve')
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.suptitle('Evaluasi Model — Prediksi Kelayakan Kredit', fontsize=14)
plt.tight_layout()
plt.show()

# Feature Importance
rf_model = best_model.named_steps['classifier']
feature_names_transformed = (
    kolom_numerik +
    list(best_model.named_steps['preprocessor']
         .named_transformers_['cat']
         .named_steps['encoder']
         .get_feature_names_out(kolom_kategorikal))
)
importances = rf_model.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 5))
plt.bar(range(len(importances)), importances[indices], color='steelblue')
plt.xticks(range(len(importances)),
           [feature_names_transformed[i] for i in indices],
           rotation=45, ha='right', fontsize=9)
plt.ylabel('Importance')
plt.title('Feature Importance — Model Terbaik')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 7: Simpan Model dengan joblib

```python
# =============================================
# LANGKAH 7: Simpan Model
# =============================================

import joblib
import os

# Simpan model lengkap (preprocessing + classifier)
model_filename = 'model_kredit_terbaik.joblib'
joblib.dump(best_model, model_filename)

file_size = os.path.getsize(model_filename) / 1024  # KB
print("=== MODEL BERHASIL DISIMPAN ===")
print(f"Nama file: {model_filename}")
print(f"Ukuran file: {file_size:.1f} KB")
print(f"Pipeline tersimpan mencakup:")
print(f"  1. Preprocessor (scaler + encoder)")
print(f"  2. Classifier (Random Forest terbaik)")
```

### Langkah 8: Load dan Gunakan Model Tersimpan

```python
# =============================================
# LANGKAH 8: Load dan Prediksi
# =============================================

# Load model dari file
model_loaded = joblib.load(model_filename)
print("=== MODEL BERHASIL DI-LOAD ===\n")

# Simulasi data nasabah baru
nasabah_baru = pd.DataFrame([
    {
        'usia': 35, 'pendapatan_juta': 15.5, 'jumlah_tanggungan': 2,
        'lama_bekerja_tahun': 8, 'total_aset_juta': 120.0,
        'jumlah_pinjaman_aktif': 1, 'skor_kredit': 720,
        'pendidikan': 'S1', 'status_pernikahan': 'Menikah', 'kota': 'Jakarta'
    },
    {
        'usia': 25, 'pendapatan_juta': 4.5, 'jumlah_tanggungan': 0,
        'lama_bekerja_tahun': 2, 'total_aset_juta': 15.0,
        'jumlah_pinjaman_aktif': 3, 'skor_kredit': 450,
        'pendidikan': 'SMA', 'status_pernikahan': 'Belum Menikah', 'kota': 'Medan'
    },
    {
        'usia': 45, 'pendapatan_juta': 25.0, 'jumlah_tanggungan': 3,
        'lama_bekerja_tahun': 20, 'total_aset_juta': 350.0,
        'jumlah_pinjaman_aktif': 0, 'skor_kredit': 780,
        'pendidikan': 'S2', 'status_pernikahan': 'Menikah', 'kota': 'Surabaya'
    },
])

# Prediksi
prediksi = model_loaded.predict(nasabah_baru)
probabilitas = model_loaded.predict_proba(nasabah_baru)

print("--- Prediksi Nasabah Baru ---\n")
for i, (_, nasabah) in enumerate(nasabah_baru.iterrows()):
    label = "LAYAK" if prediksi[i] == 1 else "TIDAK LAYAK"
    prob = probabilitas[i][1]
    print(f"Nasabah {i+1}:")
    print(f"  Usia: {nasabah['usia']}, Pendapatan: {nasabah['pendapatan_juta']} juta")
    print(f"  Kota: {nasabah['kota']}, Skor Kredit: {nasabah['skor_kredit']}")
    print(f"  Prediksi: {label} (probabilitas layak: {prob:.3f})")
    print()

# Verifikasi: model loaded memberikan hasil sama dengan model asli
pred_original = best_model.predict(nasabah_baru)
pred_loaded = model_loaded.predict(nasabah_baru)
print(f"Verifikasi: model asli == model loaded? {np.array_equal(pred_original, pred_loaded)}")
```

### Langkah 9: Dokumentasi Penggunaan AI

```python
# =============================================
# LANGKAH 9: Dokumentasi AI Usage
# =============================================

print("=" * 60)
print("DOKUMENTASI PENGGUNAAN AI (AI USAGE LOG)")
print("=" * 60)

ai_log = """
=== AI USAGE LOG — Lab 14: ML Pipeline ===
Nama   : [Nama Mahasiswa]
NIM    : [NIM]
Tanggal: [Tanggal Pengerjaan]

1. DEFINISI PROBLEM (Langkah 1)
   AI Tool  : ChatGPT / Claude
   Prompt   : "Bantu definisikan problem statement ML untuk
               prediksi kelayakan kredit nasabah di Indonesia"
   Hasil    : Mendapatkan kerangka problem statement
   Modifikasi: Disesuaikan konteks bank Indonesia

2. FEATURE ENGINEERING (Langkah 2-3)
   AI Tool  : Claude
   Prompt   : "Fitur apa saja yang relevan untuk prediksi
               kelayakan kredit?"
   Hasil    : Daftar 10 fitur yang relevan
   Modifikasi: Disesuaikan satuan ke Rupiah

3. MODEL SELECTION (Langkah 4)
   AI Tool  : ChatGPT
   Prompt   : "Algoritma ML terbaik untuk binary classification
               dengan dataset tabular?"
   Hasil    : Rekomendasi 6 algoritma
   Modifikasi: Menambahkan SVM sesuai materi kuliah

4. DEBUGGING (Langkah 5)
   AI Tool  : GitHub Copilot
   Prompt   : Auto-complete untuk GridSearchCV syntax
   Hasil    : Template parameter grid
   Modifikasi: Menyesuaikan parameter range

5. INTERPRETASI (Langkah 6)
   AI Tool  : Claude
   Prompt   : "Cara menginterpretasi confusion matrix
               untuk kasus kredit"
   Hasil    : Penjelasan False Positive vs False Negative
   Modifikasi: Tidak ada, langsung dipahami

REFLEKSI:
- AI membantu mempercepat penulisan kode boilerplate
- AI memberikan ide fitur yang mungkin terlewat
- Tetap perlu pemahaman konsep untuk validasi output AI
- AI BUKAN pengganti pemahaman fundamental ML
"""

print(ai_log)

print("Catatan Penting:")
print("- Selalu verifikasi saran AI dengan pengetahuan sendiri")
print("- AI dapat memberikan kode yang salah — selalu test!")
print("- Dokumentasikan SEMUA penggunaan AI untuk transparansi")
print("- Pahami MENGAPA kode bekerja, bukan hanya BAGAIMANA")
```

### Langkah 10: Ringkasan ML Pipeline

```python
# =============================================
# LANGKAH 10: Ringkasan ML Pipeline
# =============================================

print("=" * 60)
print("RINGKASAN ML PIPELINE — PREDIKSI KELAYAKAN KREDIT")
print("=" * 60)

print(f"""
1. PROBLEM DEFINITION:
   - Tipe: Binary Classification
   - Target: Kelayakan Kredit (Layak / Tidak Layak)
   - Konteks: Nasabah bank di Indonesia

2. DATASET:
   - Jumlah sampel: {len(df)}
   - Jumlah fitur: {X.shape[1]} ({len(kolom_numerik)} numerik, {len(kolom_kategorikal)} kategorikal)
   - Distribusi: {(y==1).sum()} layak, {(y==0).sum()} tidak layak

3. PREPROCESSING:
   - Numerik: SimpleImputer (median) + StandardScaler
   - Kategorikal: SimpleImputer (most_frequent) + OneHotEncoder
   - Semua terintegrasi dalam sklearn Pipeline

4. MODEL SELECTION:
   - 6 algoritma diuji dengan 5-fold cross-validation
   - Model terbaik: {best_model_name}
   - CV Accuracy: {results[best_model_name]['mean']:.4f}

5. HYPERPARAMETER TUNING:
   - Metode: GridSearchCV (5-fold CV)
   - Best CV Score: {grid_search.best_score_:.4f}

6. EVALUASI FINAL (Test Set):
   - Accuracy : {accuracy_score(y_test, y_pred):.4f}
   - Precision: {precision_score(y_test, y_pred):.4f}
   - Recall   : {recall_score(y_test, y_pred):.4f}
   - F1-Score : {f1_score(y_test, y_pred):.4f}
   - ROC AUC  : {roc_auc:.4f}

7. DEPLOYMENT:
   - Model disimpan: {model_filename}
   - Dapat di-load dan digunakan untuk prediksi baru

8. AI USAGE:
   - 5 interaksi dengan AI tools didokumentasikan
   - Semua output AI divalidasi dan dimodifikasi
""")

print("=" * 60)
print("Pipeline lengkap selesai!")
print("=" * 60)
```

---

## Tantangan Tambahan

1. **Pipeline dengan imblearn:** Install library `imbalanced-learn` dan gunakan `SMOTE` untuk menangani imbalanced dataset di dalam pipeline. Bandingkan performa model sebelum dan sesudah oversampling.

2. **Tambahkan Lebih Banyak Model:** Tambahkan XGBoost (`pip install xgboost`) dan LightGBM (`pip install lightgbm`) ke dalam model selection. Apakah gradient boosting library lebih unggul daripada sklearn?

3. **Deployment Sederhana:** Buat fungsi `prediksi_kredit(data_nasabah)` yang menerima dictionary data nasabah, melakukan preprocessing, dan mengembalikan prediksi beserta probabilitas. Buat antarmuka sederhana menggunakan `ipywidgets` di Colab.

---

## Checklist Penyelesaian

- [ ] Langkah 1: Problem statement didefinisikan dengan jelas
- [ ] Langkah 2: Dataset berhasil dibuat dan dieksplorasi
- [ ] Langkah 3: Preprocessing pipeline berhasil dibangun (numerik + kategorikal)
- [ ] Langkah 4: Minimal 5 algoritma dibandingkan dengan cross-validation
- [ ] Langkah 5: GridSearchCV berhasil menemukan parameter terbaik
- [ ] Langkah 6: Model terbaik dievaluasi pada test set (accuracy, precision, recall, F1)
- [ ] Langkah 7: Model berhasil disimpan dengan joblib
- [ ] Langkah 8: Model berhasil di-load dan digunakan untuk prediksi baru
- [ ] Langkah 9: AI Usage Log diisi dengan lengkap dan jujur
- [ ] Langkah 10: Ringkasan pipeline dibuat
- [ ] Semua kode berjalan tanpa error di Google Colab
- [ ] Notebook disimpan dengan format `Lab14_NamaAnda_NIM.ipynb`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
