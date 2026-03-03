# BAB 14: PROYEK AKHIR — MACHINE LEARNING END-TO-END

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah menyelesaikan bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| Sub-CPMK 15.1 | Merancang proyek ML end-to-end dari problem definition hingga deployment sederhana | C6 (Merancang) |
| Sub-CPMK 15.2 | Mengevaluasi dan membandingkan performa beberapa model ML untuk menentukan model terbaik | C5 (Mengevaluasi) |
| Sub-CPMK 15.3 | Merancang dokumentasi proyek ML yang komprehensif, termasuk AI Usage Log | C6 (Merancang) |
| Sub-CPMK 15.4 | Mengevaluasi aspek etika, fairness, dan responsible AI dalam proyek ML | C5 (Mengevaluasi) |

**CPMK-7:** Merancang solusi AI end-to-end yang bertanggung jawab dengan konteks Indonesia.

> **Relevansi CPMK:** Bab ini merupakan kulminasi seluruh CPMK-1 hingga CPMK-7, mengintegrasikan fondasi AI, supervised/unsupervised learning, deep learning, NLP, computer vision, dan MLOps dalam satu proyek nyata.

**Estimasi Waktu:** Proyek berjalan dari Minggu 9 hingga Minggu 15 (paralel dengan materi kuliah).

**Prasyarat:** Mahasiswa telah menyelesaikan Bab 1-13 dan memahami seluruh pipeline ML dari data preprocessing hingga model deployment.

---

## 14.1 Panduan Proyek Akhir

### 14.1.1 Mengapa Proyek Akhir?

Selama 13 bab sebelumnya, Anda telah membangun fondasi yang kokoh:

| Bagian | Bab | Keterampilan yang Diperoleh |
|--------|-----|-----------------------------|
| **I — Fondasi AI** | 1-4 | Konsep AI, matematika ML, preprocessing, workflow ML |
| **II — Supervised Learning** | 5-7 | Regresi, klasifikasi, ensemble methods |
| **III — Advanced ML** | 8-10 | Unsupervised learning, deep learning, model evaluation |
| **IV — Applied AI** | 11-13 | NLP, computer vision, MLOps, responsible AI |

Proyek akhir adalah **jembatan** antara pengetahuan teoritis dan dunia nyata. Di sinilah Anda membuktikan bahwa Anda tidak hanya memahami konsep, tetapi mampu **menerapkannya** untuk memecahkan masalah nyata dengan data nyata.

> **Analogi:** Jika Bab 1-13 adalah latihan-latihan individual (dribbling, passing, shooting), maka proyek akhir adalah **pertandingan sesungguhnya** di mana semua keterampilan harus digunakan secara terpadu.

### 14.1.2 Format dan Ekspektasi

Proyek akhir dikerjakan secara **individu** atau **berpasangan** (maksimal 2 orang) dengan ketentuan:

| Komponen | Ketentuan |
|----------|-----------|
| **Format** | Jupyter Notebook (.ipynb) di Google Colab |
| **Panjang** | Minimal 30 code cells + markdown narasi |
| **Dataset** | Minimal 500 observasi, konteks Indonesia |
| **Model** | Minimal 3 model ML berbeda untuk perbandingan |
| **Deployment** | Minimal 1 bentuk deployment sederhana (Flask/Streamlit) |
| **AI Usage** | Boleh menggunakan AI, **wajib** dokumentasi AI Usage Log |
| **Deadline** | Minggu ke-15 perkuliahan |
| **Presentasi** | 15 menit + 5 menit tanya jawab |

### 14.1.3 Timeline Proyek

```
TIMELINE PROYEK AKHIR (Minggu 9-15)
────────────────────────────────────

Minggu 9  : Problem Definition + Dataset Selection
            ├── Pilih topik dan dataset
            ├── Rumuskan pertanyaan dan hipotesis
            └── Submit proposal 1 halaman

Minggu 10 : EDA (Exploratory Data Analysis)
            ├── Load dan inspeksi data
            ├── Statistik deskriptif
            └── Visualisasi eksploratif

Minggu 11 : Feature Engineering + Preprocessing
            ├── Handling missing values dan outliers
            ├── Encoding dan scaling
            └── Feature engineering (buat fitur baru)

Minggu 12 : Model Training + Evaluation
            ├── Latih minimal 3 model berbeda
            ├── Cross-validation
            └── Perbandingan metrik

Minggu 13 : Model Optimization + Deployment
            ├── Hyperparameter tuning model terbaik
            ├── Buat Flask API atau Streamlit dashboard
            └── Testing deployment

Minggu 14 : Dokumentasi + Finalisasi
            ├── Lengkapi AI Usage Log
            ├── Tulis narasi dan kesimpulan
            └── Finalisasi notebook

Minggu 15 : Presentasi + Pengumpulan
            ├── Presentasi 15 menit
            ├── Tanya jawab 5 menit
            └── Submit notebook + artefak
```

---

## 14.2 Tahap 1: Problem Definition dan Dataset Selection

### 14.2.1 Merumuskan Masalah ML

Setiap proyek ML dimulai dengan pertanyaan bisnis atau masalah nyata yang jelas. Konversikan masalah tersebut menjadi **tugas ML** yang spesifik:

```
DARI MASALAH BISNIS KE TUGAS ML
─────────────────────────────────

Masalah Bisnis                          Tugas ML
─────────────────                       ────────
"Pelanggan mana yang akan churn?"   →   Binary Classification
"Berapa harga properti ini?"        →   Regression
"Apa sentimen review ini?"          →   Text Classification (NLP)
"Produk apa yang mirip?"            →   Clustering / Recommender
"Gambar ini batik motif apa?"       →   Image Classification (CV)
"Transaksi ini fraud atau bukan?"   →   Anomaly Detection
```

### 14.2.2 Sumber Dataset Indonesia

| Sumber | URL | Jenis Data | Format |
|--------|-----|------------|--------|
| **BPS (Badan Pusat Statistik)** | bps.go.id | Ekonomi, demografi, sosial | Excel, CSV |
| **Open Data Jakarta** | data.jakarta.go.id | Transportasi, lingkungan, kesehatan | CSV, JSON |
| **Satu Data Indonesia** | data.go.id | Multi-sektor pemerintah | CSV, Excel |
| **Kaggle Indonesia** | kaggle.com (filter Indonesia) | Beragam | CSV |
| **UCI ML Repository** | archive.ics.uci.edu | Benchmark ML | CSV |
| **Bank Indonesia** | bi.go.id/statistik | Moneter, perbankan, inflasi | Excel |
| **Hugging Face Datasets** | huggingface.co/datasets | NLP, vision, tabular | Various |
| **Google Dataset Search** | datasetsearch.research.google.com | Beragam | Various |

### 14.2.3 Contoh Topik Proyek per Domain

| No | Domain | Topik | Dataset | Tipe ML |
|----|--------|-------|---------|---------|
| 1 | E-Commerce | Prediksi rating produk marketplace Indonesia | Kaggle Tokopedia | Regression |
| 2 | Properti | Prediksi harga rumah di Jabodetabek | Rumah123/Lamudi | Regression |
| 3 | Kesehatan | Klasifikasi risiko diabetes berdasarkan data klinik | UCI/Kaggle | Classification |
| 4 | Transportasi | Prediksi waktu tempuh TransJakarta | Open Data Jakarta | Regression |
| 5 | Keuangan | Deteksi transaksi fraud pada data fintech | Kaggle fraud dataset | Classification |
| 6 | NLP | Analisis sentimen review produk Bahasa Indonesia | IndoNLU/scraping | Text Classification |
| 7 | Computer Vision | Klasifikasi motif batik Indonesia | Dataset batik | Image Classification |
| 8 | Pertanian | Prediksi hasil panen berdasarkan data cuaca dan tanah | BPS + BMKG | Regression |
| 9 | Pendidikan | Prediksi kelulusan mahasiswa | Data internal kampus | Classification |
| 10 | Sosial | Clustering kabupaten berdasarkan indikator pembangunan | BPS IPM | Clustering |

### 14.2.4 Template Problem Definition

```python
# ============================================================
# TAHAP 1: PROBLEM DEFINITION
# ============================================================
# Judul Proyek  : [Judul Proyek Anda]
# Nama          : [Nama Mahasiswa]
# NIM           : [NIM]
# Kelas         : Informatika — Kecerdasan Buatan dan Machine Learning
# Dosen         : Tri Aji Nugroho, S.T., M.T.
# ============================================================
#
# LATAR BELAKANG:
# [Jelaskan mengapa masalah ini penting, apa konteksnya di Indonesia]
#
# PERTANYAAN:
# Q1: [Pertanyaan utama yang ingin dijawab]
# Q2: [Pertanyaan pendukung]
# Q3: [Pertanyaan tambahan]
#
# HIPOTESIS:
# H1: [Hipotesis tentang model atau fitur]
# H2: [Hipotesis tentang performa atau pola]
#
# TIPE ML:
# [Classification / Regression / Clustering / dll]
#
# TARGET VARIABEL:
# [Nama variabel target dan penjelasannya]
#
# METRIK EVALUASI:
# [Accuracy, F1-score, RMSE, dll — jelaskan mengapa]
#
# MODEL YANG AKAN DICOBA:
# 1. [Model 1 — sebagai baseline]
# 2. [Model 2]
# 3. [Model 3]
#
# BATASAN:
# [Apa yang TIDAK akan dijawab oleh proyek ini]
# ============================================================
```

---

## 14.3 Tahap 2: Exploratory Data Analysis (EDA)

### 14.3.1 Panduan EDA untuk Proyek ML

EDA bukan sekadar membuat grafik — ini adalah proses untuk **memahami data** sebelum membangun model:

```
KERANGKA EDA UNTUK ML
──────────────────────

1. INSPEKSI AWAL
   ├── Shape dan tipe data
   ├── Missing values
   ├── Duplikat
   └── Data dictionary

2. UNIVARIATE ANALYSIS
   ├── Distribusi setiap variabel
   ├── Statistik deskriptif
   └── Outlier detection

3. BIVARIATE ANALYSIS
   ├── Korelasi dengan target
   ├── Scatter plots (numerik vs target)
   └── Box plots (kategorikal vs target)

4. MULTIVARIATE ANALYSIS
   ├── Matriks korelasi
   ├── Pair plots
   └── Clustering awal (jika relevan)

5. INSIGHT & KEPUTUSAN
   ├── Fitur mana yang paling informatif?
   ├── Transformasi apa yang diperlukan?
   └── Model apa yang cocok?
```

### 14.3.2 Template Kode EDA

```python
# ============================================================
# TAHAP 2: EXPLORATORY DATA ANALYSIS
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Konfigurasi visualisasi
plt.rcParams['figure.figsize'] = (10, 6)
sns.set_style('whitegrid')
sns.set_palette('Set2')

# Load dataset
# df = pd.read_csv('nama_dataset.csv')

# --- 2a. Inspeksi Awal ---
print("=" * 60)
print("INSPEKSI DATASET")
print("=" * 60)
print(f"Dimensi      : {df.shape[0]} baris x {df.shape[1]} kolom")
print(f"Memori       : {df.memory_usage(deep=True).sum() / 1024:.1f} KB")
print()

print("TIPE DATA:")
print(df.dtypes)
print()

print("MISSING VALUES:")
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_info = pd.DataFrame({'Jumlah': missing, 'Persentase (%)': missing_pct})
print(missing_info[missing_info['Jumlah'] > 0])
print()

print("DUPLIKAT:")
print(f"Jumlah baris duplikat: {df.duplicated().sum()}")
print()

# --- 2b. Statistik Deskriptif ---
print("STATISTIK DESKRIPTIF:")
deskriptif = df.describe().T
deskriptif['CV (%)'] = (deskriptif['std'] / deskriptif['mean'] * 100).round(2)
print(deskriptif[['count', 'mean', 'std', 'min', '50%', 'max', 'CV (%)']])

# --- 2c. Distribusi Target Variable ---
if df['target'].dtype in ['int64', 'float64']:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].hist(df['target'], bins=30, edgecolor='black', alpha=0.7)
    axes[0].set_title('Distribusi Target Variable')
    axes[0].set_xlabel('Nilai')
    axes[0].set_ylabel('Frekuensi')

    # Box plot
    axes[1].boxplot(df['target'])
    axes[1].set_title('Box Plot Target Variable')
    plt.tight_layout()
    plt.show()

# --- 2d. Matriks Korelasi ---
fig, ax = plt.subplots(figsize=(10, 8))
numerik_cols = df.select_dtypes(include=[np.number]).columns
corr = df[numerik_cols].corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, fmt='.2f',
            cmap='RdBu_r', center=0, vmin=-1, vmax=1, ax=ax)
ax.set_title('Matriks Korelasi', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# --- 2e. Insight EDA ---
print("\n" + "=" * 60)
print("INSIGHT EDA")
print("=" * 60)
print("1. [Tuliskan insight pertama dari EDA Anda]")
print("2. [Tuliskan insight kedua]")
print("3. [Tuliskan insight ketiga]")
```

---

## 14.4 Tahap 3: Feature Engineering dan Preprocessing

### 14.4.1 Checklist Preprocessing

```
CHECKLIST PREPROCESSING
───────────────────────

[ ] Missing values ditangani (impute atau hapus, dengan justifikasi)
[ ] Outliers diidentifikasi dan ditangani (jika perlu)
[ ] Variabel kategorikal di-encode (One-Hot / Label / Target encoding)
[ ] Variabel numerik di-scale (StandardScaler / MinMaxScaler)
[ ] Feature engineering: fitur baru yang bermakna dibuat
[ ] Data split: train/test (atau train/val/test) dengan stratify
[ ] TIDAK ada data leakage: scaler di-fit hanya pada data training
```

### 14.4.2 Template Feature Engineering

```python
# ============================================================
# TAHAP 3: FEATURE ENGINEERING & PREPROCESSING
# ============================================================

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# --- 3a. Feature Engineering ---
# Contoh: buat fitur baru dari fitur yang ada
# df['rasio_harga_luas'] = df['harga'] / df['luas_bangunan']
# df['usia_bangunan'] = 2026 - df['tahun_bangun']
# df['log_harga'] = np.log1p(df['harga'])

print("Fitur baru yang dibuat:")
# print(f"  - rasio_harga_luas: harga / luas_bangunan")
# print(f"  - usia_bangunan: 2026 - tahun_bangun")

# --- 3b. Definisi Kolom ---
kolom_numerik = ['fitur_num_1', 'fitur_num_2', 'fitur_num_3']
kolom_kategorikal = ['fitur_cat_1', 'fitur_cat_2']
kolom_target = 'target'

# --- 3c. Split Data (SEBELUM preprocessing untuk mencegah data leakage) ---
X = df.drop(kolom_target, axis=1)
y = df[kolom_target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42,
    stratify=y  # Untuk klasifikasi; hapus untuk regresi
)

print(f"\nData Training : {X_train.shape[0]} sampel")
print(f"Data Testing  : {X_test.shape[0]} sampel")

# --- 3d. Preprocessing Pipeline ---
preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ]), kolom_numerik),
        ('cat', Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(drop='first', sparse_output=False,
                                      handle_unknown='ignore'))
        ]), kolom_kategorikal)
    ]
)

print("\nPreprocessing pipeline siap.")
```

---

## 14.5 Tahap 4: Model Selection dan Training

### 14.5.1 Strategi Pemilihan Model

```
STRATEGI PEMILIHAN MODEL
─────────────────────────

1. MULAI DENGAN BASELINE SEDERHANA
   ├── Klasifikasi: LogisticRegression, DecisionTree
   └── Regresi: LinearRegression, DecisionTreeRegressor

2. COBA MODEL MENENGAH
   ├── Klasifikasi: RandomForest, SVM, KNN
   └── Regresi: RandomForest, SVR, KNN

3. COBA MODEL ADVANCED
   ├── Klasifikasi: XGBoost, LightGBM, Neural Network
   └── Regresi: XGBoost, LightGBM, Neural Network

4. BANDINGKAN DENGAN CROSS-VALIDATION
   └── Pilih model terbaik berdasarkan metrik yang relevan
```

### 14.5.2 Template Training dan Comparison

```python
# ============================================================
# TAHAP 4: MODEL SELECTION & TRAINING
# ============================================================

from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import (RandomForestClassifier, RandomForestRegressor,
                              GradientBoostingClassifier, GradientBoostingRegressor)
from sklearn.svm import SVC, SVR
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import (accuracy_score, f1_score, classification_report,
                             mean_squared_error, r2_score, mean_absolute_error)
import time

# Definisikan model yang akan dicoba
# (Contoh untuk klasifikasi — sesuaikan jika regresi)
model_candidates = {
    'Logistic Regression': Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(max_iter=1000, random_state=42))
    ]),
    'Random Forest': Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ]),
    'Gradient Boosting': Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', GradientBoostingClassifier(n_estimators=100,
                                                   random_state=42))
    ]),
}

# --- Training dan Cross-Validation ---
hasil_model = []

print("=" * 70)
print("PERBANDINGAN MODEL DENGAN 5-FOLD CROSS-VALIDATION")
print("=" * 70)

for nama, pipeline_model in model_candidates.items():
    waktu_mulai = time.time()

    # Cross-validation
    cv_scores = cross_val_score(pipeline_model, X_train, y_train,
                                 cv=5, scoring='f1_weighted')

    # Training pada seluruh data training
    pipeline_model.fit(X_train, y_train)

    # Evaluasi pada test set
    y_pred = pipeline_model.predict(X_test)
    akurasi = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')

    waktu_selesai = time.time()
    durasi = waktu_selesai - waktu_mulai

    hasil_model.append({
        'Model': nama,
        'CV F1 (mean)': f'{cv_scores.mean():.4f}',
        'CV F1 (std)': f'{cv_scores.std():.4f}',
        'Test Accuracy': f'{akurasi:.4f}',
        'Test F1': f'{f1:.4f}',
        'Waktu (detik)': f'{durasi:.2f}'
    })

    print(f"\n{nama}:")
    print(f"  CV F1-Score   : {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
    print(f"  Test Accuracy : {akurasi:.4f}")
    print(f"  Test F1-Score : {f1:.4f}")
    print(f"  Waktu Training: {durasi:.2f} detik")

# Tabel ringkasan
print("\n" + "=" * 70)
print("RINGKASAN PERBANDINGAN MODEL")
print("=" * 70)
df_hasil = pd.DataFrame(hasil_model)
print(df_hasil.to_string(index=False))

# Tentukan model terbaik
best_idx = df_hasil['Test F1'].astype(float).idxmax()
model_terbaik_nama = df_hasil.loc[best_idx, 'Model']
print(f"\nModel terbaik: {model_terbaik_nama}")
```

---

## 14.6 Tahap 5: Model Evaluation dan Comparison

### 14.6.1 Evaluasi Mendalam Model Terbaik

```python
# ============================================================
# TAHAP 5: EVALUASI MENDALAM MODEL TERBAIK
# ============================================================

from sklearn.metrics import (classification_report, confusion_matrix,
                             roc_curve, roc_auc_score, precision_recall_curve)

# Ambil model terbaik
model_terbaik = model_candidates[model_terbaik_nama]
y_pred = model_terbaik.predict(X_test)
y_proba = model_terbaik.predict_proba(X_test)[:, 1]

# --- 5a. Classification Report ---
print("CLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred))

# --- 5b. Confusion Matrix ---
cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
ax.set_xlabel('Prediksi')
ax.set_ylabel('Aktual')
ax.set_title(f'Confusion Matrix — {model_terbaik_nama}')
plt.tight_layout()
plt.show()

# --- 5c. ROC Curve ---
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
auc_score = roc_auc_score(y_test, y_proba)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# ROC Curve
axes[0].plot(fpr, tpr, 'b-', linewidth=2, label=f'AUC = {auc_score:.4f}')
axes[0].plot([0, 1], [0, 1], 'k--', alpha=0.5)
axes[0].set_xlabel('False Positive Rate')
axes[0].set_ylabel('True Positive Rate')
axes[0].set_title('ROC Curve')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Precision-Recall Curve
precision, recall, _ = precision_recall_curve(y_test, y_proba)
axes[1].plot(recall, precision, 'r-', linewidth=2)
axes[1].set_xlabel('Recall')
axes[1].set_ylabel('Precision')
axes[1].set_title('Precision-Recall Curve')
axes[1].grid(True, alpha=0.3)

plt.suptitle(f'Evaluasi Model: {model_terbaik_nama}', fontsize=14,
             fontweight='bold')
plt.tight_layout()
plt.show()

# --- 5d. Feature Importance ---
if hasattr(model_terbaik.named_steps['classifier'], 'feature_importances_'):
    importances = model_terbaik.named_steps['classifier'].feature_importances_
    # Dapatkan nama fitur setelah preprocessing
    nama_fitur = (model_terbaik.named_steps['preprocessor']
                  .get_feature_names_out())

    fi_df = pd.DataFrame({
        'Fitur': nama_fitur,
        'Importance': importances
    }).sort_values('Importance', ascending=False).head(15)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(range(len(fi_df)), fi_df['Importance'].values, color='steelblue')
    ax.set_yticks(range(len(fi_df)))
    ax.set_yticklabels(fi_df['Fitur'].values)
    ax.invert_yaxis()
    ax.set_xlabel('Feature Importance')
    ax.set_title('Top 15 Fitur Paling Penting')
    plt.tight_layout()
    plt.show()
```

---

## 14.7 Tahap 6: Model Deployment (Sederhana)

### 14.7.1 Menyimpan Model Final

```python
# ============================================================
# TAHAP 6: DEPLOYMENT SEDERHANA
# ============================================================

import joblib
import json
from datetime import datetime

# --- 6a. Simpan Model ---
nama_file_model = 'model_final_proyek.pkl'
joblib.dump(model_terbaik, nama_file_model)

# Simpan metadata
metadata = {
    'nama_proyek': '[Judul Proyek Anda]',
    'model': model_terbaik_nama,
    'metrik': {
        'accuracy': float(accuracy_score(y_test, y_pred)),
        'f1_score': float(f1_score(y_test, y_pred, average='weighted')),
        'auc': float(auc_score)
    },
    'tanggal_training': datetime.now().strftime('%Y-%m-%d %H:%M'),
    'fitur': kolom_numerik + kolom_kategorikal,
    'pembuat': '[Nama Mahasiswa]'
}

with open('model_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2, ensure_ascii=False)

print(f"Model tersimpan: {nama_file_model}")
print(f"Metadata tersimpan: model_metadata.json")
```

### 14.7.2 Deployment dengan Streamlit (Template)

```python
# ============================================================
# app_proyek.py — Template Streamlit untuk Proyek Akhir
# Jalankan: streamlit run app_proyek.py
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json

# Konfigurasi halaman
st.set_page_config(
    page_title="[Judul Proyek Anda]",
    layout="wide"
)

# Muat model dan metadata
@st.cache_resource
def muat_model():
    model = joblib.load('model_final_proyek.pkl')
    with open('model_metadata.json', 'r') as f:
        metadata = json.load(f)
    return model, metadata

model, metadata = muat_model()

# Header
st.title("[Judul Proyek Anda]")
st.markdown(f"""
**Model:** {metadata['model']}
| **Akurasi:** {metadata['metrik']['accuracy']:.2%}
| **F1-Score:** {metadata['metrik']['f1_score']:.4f}
| **AUC:** {metadata['metrik']['auc']:.4f}
""")

# Sidebar — Input
st.sidebar.header("Input Data")
# Sesuaikan input di bawah ini dengan fitur proyek Anda
# fitur_1 = st.sidebar.number_input("Fitur 1", ...)
# fitur_2 = st.sidebar.selectbox("Fitur 2", [...])

# Tombol prediksi
if st.sidebar.button("Prediksi", type="primary"):
    # Buat DataFrame dari input
    # data_input = pd.DataFrame([{...}])

    # Prediksi
    # prediksi = model.predict(data_input)[0]
    # proba = model.predict_proba(data_input)[0]

    # Tampilkan hasil
    # st.metric("Prediksi", prediksi)
    pass

# Footer
st.markdown("---")
st.markdown(
    "*Proyek Akhir — Kecerdasan Buatan dan Machine Learning, "
    "Universitas Al Azhar Indonesia*"
)
```

---

## 14.8 Tahap 7: Dokumentasi dan Presentasi

### 14.8.1 Struktur Notebook yang Baik

```
STRUKTUR NOTEBOOK PROYEK AKHIR
───────────────────────────────

Cell 1  : [Markdown] Judul, Nama, NIM, Kelas
Cell 2  : [Markdown] Latar Belakang & Problem Definition
Cell 3  : [Code]     Import library
Cell 4  : [Code]     Load dataset
Cell 5  : [Markdown] Deskripsi Dataset & Data Dictionary
Cell 6  : [Code]     Inspeksi awal (shape, dtypes, missing)
Cell 7  : [Code]     Statistik deskriptif
Cell 8  : [Code]     Visualisasi distribusi
Cell 9  : [Code]     Korelasi & bivariate analysis
Cell 10 : [Markdown] Insight dari EDA
Cell 11 : [Code]     Preprocessing & feature engineering
Cell 12 : [Code]     Train-test split
Cell 13 : [Code]     Model 1: training & evaluasi
Cell 14 : [Code]     Model 2: training & evaluasi
Cell 15 : [Code]     Model 3: training & evaluasi
Cell 16 : [Code]     Perbandingan model
Cell 17 : [Code]     Evaluasi mendalam model terbaik
Cell 18 : [Code]     Feature importance
Cell 19 : [Markdown] Interpretasi & diskusi hasil
Cell 20 : [Code]     Simpan model
Cell 21 : [Markdown] Kesimpulan & rekomendasi
Cell 22 : [Markdown] AI Usage Log
Cell 23 : [Markdown] Referensi
```

### 14.8.2 Tips Presentasi

| Aspek | Tips |
|-------|------|
| **Waktu** | 15 menit — jangan melebihi. Latihan minimal 2 kali sebelumnya |
| **Slide 1** | Judul, nama, topik — langsung ke point |
| **Slide 2-3** | Masalah dan dataset — mengapa ini penting? |
| **Slide 4-5** | Insight EDA — ceritakan data, bukan hanya tunjukkan grafik |
| **Slide 6-7** | Model dan hasil — perbandingan tabel, metrik utama |
| **Slide 8** | Demo (live atau screenshot) — tunjukkan deployment berjalan |
| **Slide 9** | Kesimpulan — 3 temuan utama |
| **Slide 10** | AI Usage — transparansi penggunaan AI |

---

## 14.9 Rubrik Penilaian Proyek

### 14.9.1 Komponen dan Bobot Penilaian

| No | Komponen | Bobot | Deskripsi |
|----|----------|-------|-----------|
| 1 | Problem Definition & Hipotesis | 10% | Kejelasan, spesifisitas, relevansi dengan konteks Indonesia |
| 2 | Data & Preprocessing | 15% | Kualitas data, cleaning, feature engineering, dokumentasi |
| 3 | Model Training & Selection | 20% | Minimal 3 model, cross-validation, perbandingan yang adil |
| 4 | Evaluasi & Interpretasi | 15% | Metrik yang tepat, interpretasi mendalam, feature importance |
| 5 | Deployment | 10% | Flask API atau Streamlit yang berfungsi |
| 6 | Dokumentasi AI Usage | 10% | Kelengkapan log, transparansi, validasi independen |
| 7 | Kualitas Kode & Notebook | 10% | Struktur, komentar, reproducibility |
| 8 | Presentasi | 5% | Kejelasan, kemampuan menjawab pertanyaan |
| 9 | Etika & Responsible AI | 5% | Fairness check, kejujuran, attribution |
| | **TOTAL** | **100%** | |

### 14.9.2 Rubrik Detail

#### Komponen 3: Model Training & Selection (20%)

| Skor | Kriteria |
|------|----------|
| **A (86-100)** | Minimal 3 model berbeda dengan justifikasi pemilihan; cross-validation yang benar; perbandingan fair dan komprehensif; hyperparameter tuning pada model terbaik; metrik evaluasi sesuai dengan tipe masalah |
| **B (71-85)** | 3 model dicoba; cross-validation ada; perbandingan cukup lengkap; ada tuning sederhana |
| **C (56-70)** | 2 model dicoba; cross-validation ada tapi kurang tepat; perbandingan minimal |
| **D (< 56)** | Hanya 1 model; tidak ada cross-validation; tidak ada perbandingan |

#### Komponen 5: Deployment (10%)

| Skor | Kriteria |
|------|----------|
| **A (86-100)** | Flask API atau Streamlit berfungsi dengan baik; input validation; output informatif; dokumentasi cara menjalankan; UI/UX yang bersih |
| **B (71-85)** | Deployment berfungsi; input/output dasar ada; dokumentasi minimal |
| **C (56-70)** | Deployment ada tapi tidak lengkap atau bermasalah |
| **D (< 56)** | Tidak ada deployment; atau hanya kode tanpa bisa dijalankan |

#### Komponen 6: Dokumentasi AI Usage (10%)

| Skor | Kriteria |
|------|----------|
| **A (86-100)** | AI Usage Log lengkap untuk setiap interaksi signifikan; prompt didokumentasikan; validasi independen dilakukan; refleksi kritis tentang kontribusi AI vs mahasiswa |
| **B (71-85)** | Log ada dan cukup lengkap; sebagian prompt didokumentasikan; ada validasi |
| **C (56-70)** | Log ada tetapi tidak lengkap; tidak ada validasi |
| **D (< 56)** | Tidak ada log; atau log sangat generik |

### 14.9.3 Konversi Skor ke Nilai

| Rentang Skor | Nilai Huruf | Predikat |
|--------------|-------------|----------|
| 86 - 100 | A | Sangat Baik |
| 71 - 85 | B | Baik |
| 56 - 70 | C | Cukup |
| 41 - 55 | D | Kurang |
| 0 - 40 | E | Sangat Kurang |

---

## 14.10 Contoh Proyek: Prediksi Harga Properti Indonesia

### 14.10.1 Pendahuluan

> **Catatan:** Bagian ini menunjukkan contoh proyek lengkap dari awal hingga akhir. Gunakan sebagai referensi, tetapi pastikan proyek Anda **orisinal** dan menggunakan **topik yang berbeda**.

**Judul:** *Prediksi Harga Properti Residensial di Jabodetabek Menggunakan Machine Learning*

**Ringkasan:** Proyek ini membangun model prediksi harga properti residensial di area Jabodetabek menggunakan dataset dari marketplace properti Indonesia. Melalui perbandingan Linear Regression, Random Forest, dan Gradient Boosting, ditemukan bahwa Gradient Boosting menghasilkan performa terbaik (RMSE = Rp 285 juta, R-squared = 0.87). Fitur paling berpengaruh adalah luas bangunan, lokasi, dan jumlah kamar tidur.

### 14.10.2 Notebook End-to-End

```python
# ============================================================
# PROYEK AKHIR: PREDIKSI HARGA PROPERTI JABODETABEK
# ============================================================
# Nama   : [Nama Mahasiswa]
# NIM    : [NIM]
# Kelas  : Informatika — Kecerdasan Buatan dan Machine Learning
# Dosen  : Tri Aji Nugroho, S.T., M.T.
# ============================================================

# === SETUP ENVIRONMENT ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import (mean_squared_error, r2_score,
                             mean_absolute_error, mean_absolute_percentage_error)
import joblib
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['figure.figsize'] = (10, 6)
sns.set_style('whitegrid')

print("Library berhasil diimpor.")
```

```python
# ============================================================
# TAHAP 1: PROBLEM DEFINITION
# ============================================================
"""
LATAR BELAKANG:
Pasar properti di Indonesia, khususnya Jabodetabek, sangat dinamis.
Harga properti dipengaruhi oleh banyak faktor: lokasi, luas,
fasilitas, aksesibilitas, dan kondisi ekonomi makro. Model prediksi
harga properti dapat membantu:
- Pembeli: mengetahui harga wajar
- Penjual: menentukan harga jual yang kompetitif
- Investor: mengidentifikasi peluang investasi

PERTANYAAN:
Q1: Fitur apa yang paling berpengaruh terhadap harga properti?
Q2: Model ML mana yang paling akurat untuk prediksi harga?
Q3: Seberapa akurat model dalam memprediksi harga (dalam % error)?

HIPOTESIS:
H1: Luas bangunan memiliki korelasi positif terkuat dengan harga
H2: Model ensemble (Random Forest/Gradient Boosting) lebih baik
    dari Linear Regression
H3: Model dapat mencapai MAPE < 25%

METRIK EVALUASI:
- RMSE (Root Mean Squared Error) — dalam Rupiah
- R-squared — proporsi varians yang dijelaskan model
- MAPE (Mean Absolute Percentage Error) — error dalam persentase

MODEL YANG AKAN DICOBA:
1. Linear Regression (baseline)
2. Random Forest Regressor
3. Gradient Boosting Regressor
"""
print("Tahap 1: Problem Definition selesai.")
```

```python
# ============================================================
# TAHAP 2: DATA LOADING & EDA
# ============================================================

# Simulasi dataset properti Jabodetabek
# (Dalam proyek nyata, load dari CSV/API marketplace properti)
np.random.seed(42)
n = 3000

# Lokasi dan karakteristik
lokasi = np.random.choice(
    ['Jakarta Selatan', 'Jakarta Barat', 'Jakarta Timur',
     'Jakarta Utara', 'Tangerang', 'Tangerang Selatan',
     'Bekasi', 'Depok', 'Bogor'],
    size=n,
    p=[0.15, 0.10, 0.10, 0.08, 0.12, 0.13, 0.12, 0.10, 0.10]
)

# Faktor lokasi untuk harga
faktor_lokasi = {
    'Jakarta Selatan': 1.5, 'Jakarta Barat': 1.1, 'Jakarta Timur': 1.0,
    'Jakarta Utara': 1.05, 'Tangerang': 0.85, 'Tangerang Selatan': 1.2,
    'Bekasi': 0.75, 'Depok': 0.80, 'Bogor': 0.70
}

luas_tanah = np.random.uniform(60, 500, n)
luas_bangunan = luas_tanah * np.random.uniform(0.4, 0.8, n)
jumlah_kamar = np.random.choice([2, 3, 4, 5, 6], n,
                                 p=[0.15, 0.35, 0.30, 0.15, 0.05])
jumlah_kamar_mandi = np.clip(jumlah_kamar - np.random.choice([0, 1], n), 1, 6)
sertifikat = np.random.choice(['SHM', 'HGB', 'SHGB', 'Girik'], n,
                                p=[0.50, 0.25, 0.15, 0.10])
kondisi = np.random.choice(['Baru', 'Bagus', 'Butuh Renovasi'], n,
                            p=[0.30, 0.50, 0.20])
listrik_watt = np.random.choice([1300, 2200, 3500, 5500], n,
                                 p=[0.20, 0.40, 0.25, 0.15])

# Hitung harga berdasarkan formula realistis
harga_dasar_per_m2 = 15_000_000  # Rp 15 juta per m2 (baseline)
faktor_lok_arr = np.array([faktor_lokasi[lok] for lok in lokasi])
faktor_kondisi = np.where(np.array(kondisi) == 'Baru', 1.2,
                 np.where(np.array(kondisi) == 'Bagus', 1.0, 0.8))
faktor_sertifikat = np.where(np.array(sertifikat) == 'SHM', 1.1,
                    np.where(np.array(sertifikat) == 'HGB', 1.0, 0.9))

harga = (harga_dasar_per_m2 * luas_bangunan * faktor_lok_arr *
         faktor_kondisi * faktor_sertifikat *
         (1 + 0.05 * jumlah_kamar) *
         np.random.uniform(0.85, 1.15, n))

# Buat DataFrame
df = pd.DataFrame({
    'lokasi': lokasi,
    'luas_tanah': np.round(luas_tanah, 1),
    'luas_bangunan': np.round(luas_bangunan, 1),
    'jumlah_kamar': jumlah_kamar,
    'jumlah_kamar_mandi': jumlah_kamar_mandi.astype(int),
    'sertifikat': sertifikat,
    'kondisi': kondisi,
    'listrik_watt': listrik_watt,
    'harga': np.round(harga, -6)  # Bulatkan ke jutaan
})

# Inspeksi dataset
print("INSPEKSI DATASET PROPERTI JABODETABEK")
print("=" * 50)
print(f"Dimensi: {df.shape[0]} properti x {df.shape[1]} kolom")
print(f"\nDistribusi Harga:")
print(f"  Min    : Rp {df['harga'].min():>15,.0f}")
print(f"  Median : Rp {df['harga'].median():>15,.0f}")
print(f"  Mean   : Rp {df['harga'].mean():>15,.0f}")
print(f"  Max    : Rp {df['harga'].max():>15,.0f}")
print(f"\nDistribusi per Lokasi:")
print(df['lokasi'].value_counts())
```

```python
# === EDA: Visualisasi ===

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Distribusi harga
axes[0, 0].hist(df['harga'] / 1e9, bins=30, edgecolor='black', alpha=0.7,
                color='steelblue')
axes[0, 0].set_xlabel('Harga (Miliar Rp)')
axes[0, 0].set_ylabel('Frekuensi')
axes[0, 0].set_title('Distribusi Harga Properti')

# 2. Harga vs Luas Bangunan
axes[0, 1].scatter(df['luas_bangunan'], df['harga'] / 1e9, alpha=0.3,
                   color='steelblue', s=10)
axes[0, 1].set_xlabel('Luas Bangunan (m2)')
axes[0, 1].set_ylabel('Harga (Miliar Rp)')
axes[0, 1].set_title('Harga vs Luas Bangunan')

# 3. Boxplot harga per lokasi
df_sorted = df.copy()
median_per_lokasi = df.groupby('lokasi')['harga'].median().sort_values()
df_sorted['lokasi'] = pd.Categorical(df_sorted['lokasi'],
                                       categories=median_per_lokasi.index)
df_sorted.boxplot(column='harga', by='lokasi', ax=axes[1, 0])
axes[1, 0].set_title('Harga per Lokasi')
axes[1, 0].set_xlabel('Lokasi')
axes[1, 0].set_ylabel('Harga (Rp)')
plt.sca(axes[1, 0])
plt.xticks(rotation=45, ha='right', fontsize=8)

# 4. Korelasi heatmap
numerik = df.select_dtypes(include=[np.number])
corr = numerik.corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdBu_r',
            center=0, ax=axes[1, 1])
axes[1, 1].set_title('Matriks Korelasi')

plt.suptitle('EDA — Dataset Properti Jabodetabek', fontsize=14,
             fontweight='bold')
plt.tight_layout()
plt.show()
```

```python
# ============================================================
# TAHAP 3: FEATURE ENGINEERING & PREPROCESSING
# ============================================================

# Feature engineering
df['rasio_bangunan_tanah'] = df['luas_bangunan'] / df['luas_tanah']
df['total_ruangan'] = df['jumlah_kamar'] + df['jumlah_kamar_mandi']
df['harga_log'] = np.log1p(df['harga'])  # Log-transform target

print("Fitur baru dibuat:")
print("  - rasio_bangunan_tanah: luas_bangunan / luas_tanah")
print("  - total_ruangan: jumlah_kamar + jumlah_kamar_mandi")
print("  - harga_log: log(1 + harga) untuk stabilitas numerik")

# Definisi kolom
kolom_numerik = ['luas_tanah', 'luas_bangunan', 'jumlah_kamar',
                 'jumlah_kamar_mandi', 'listrik_watt',
                 'rasio_bangunan_tanah', 'total_ruangan']
kolom_kategorikal = ['lokasi', 'sertifikat', 'kondisi']

# Split data
X = df[kolom_numerik + kolom_kategorikal]
y = df['harga_log']  # Gunakan log-transformed target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Simpan juga harga asli untuk evaluasi
y_test_asli = np.expm1(y_test)

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ]), kolom_numerik),
        ('cat', Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(drop='first', sparse_output=False,
                                      handle_unknown='ignore'))
        ]), kolom_kategorikal)
    ]
)

print(f"\nData Training: {X_train.shape[0]} sampel")
print(f"Data Testing : {X_test.shape[0]} sampel")
```

```python
# ============================================================
# TAHAP 4-5: MODEL TRAINING, EVALUATION & COMPARISON
# ============================================================

# Definisikan model
models = {
    'Linear Regression': Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ]),
    'Random Forest': Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(
            n_estimators=200, max_depth=15,
            min_samples_leaf=5, random_state=42
        ))
    ]),
    'Gradient Boosting': Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', GradientBoostingRegressor(
            n_estimators=200, max_depth=5,
            learning_rate=0.1, random_state=42
        ))
    ]),
}

# Training dan evaluasi
hasil = []
model_objects = {}

print("=" * 70)
print("PERBANDINGAN MODEL — PREDIKSI HARGA PROPERTI JABODETABEK")
print("=" * 70)

for nama, pipeline_model in models.items():
    # Cross-validation (pada log-scale)
    cv_scores = cross_val_score(pipeline_model, X_train, y_train,
                                 cv=5, scoring='r2')

    # Training
    pipeline_model.fit(X_train, y_train)
    model_objects[nama] = pipeline_model

    # Prediksi (konversi kembali ke skala asli)
    y_pred_log = pipeline_model.predict(X_test)
    y_pred_asli = np.expm1(y_pred_log)

    # Metrik evaluasi
    rmse = np.sqrt(mean_squared_error(y_test_asli, y_pred_asli))
    r2 = r2_score(y_test_asli, y_pred_asli)
    mae = mean_absolute_error(y_test_asli, y_pred_asli)
    mape = mean_absolute_percentage_error(y_test_asli, y_pred_asli) * 100

    hasil.append({
        'Model': nama,
        'CV R2 (mean)': f'{cv_scores.mean():.4f}',
        'RMSE (Juta Rp)': f'{rmse/1e6:.0f}',
        'MAE (Juta Rp)': f'{mae/1e6:.0f}',
        'R2': f'{r2:.4f}',
        'MAPE (%)': f'{mape:.1f}'
    })

    print(f"\n{nama}:")
    print(f"  CV R2        : {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
    print(f"  RMSE         : Rp {rmse/1e6:,.0f} juta")
    print(f"  MAE          : Rp {mae/1e6:,.0f} juta")
    print(f"  R2           : {r2:.4f}")
    print(f"  MAPE         : {mape:.1f}%")

# Ringkasan
print("\n" + "=" * 70)
df_hasil = pd.DataFrame(hasil)
print(df_hasil.to_string(index=False))

# Model terbaik berdasarkan R2
best_model_name = df_hasil.loc[df_hasil['R2'].astype(float).idxmax(), 'Model']
print(f"\nModel Terbaik: {best_model_name}")
```

```python
# === Visualisasi Perbandingan dan Evaluasi Model Terbaik ===

model_terbaik = model_objects[best_model_name]
y_pred_log = model_terbaik.predict(X_test)
y_pred_asli = np.expm1(y_pred_log)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Actual vs Predicted
axes[0, 0].scatter(y_test_asli / 1e9, y_pred_asli / 1e9,
                   alpha=0.4, s=15, color='steelblue')
max_val = max(y_test_asli.max(), y_pred_asli.max()) / 1e9
axes[0, 0].plot([0, max_val], [0, max_val], 'r--', linewidth=2)
axes[0, 0].set_xlabel('Harga Aktual (Miliar Rp)')
axes[0, 0].set_ylabel('Harga Prediksi (Miliar Rp)')
axes[0, 0].set_title(f'Actual vs Predicted — {best_model_name}')

# 2. Distribusi Residual
residual = (y_test_asli - y_pred_asli) / 1e6
axes[0, 1].hist(residual, bins=30, edgecolor='black', alpha=0.7,
                color='steelblue')
axes[0, 1].axvline(0, color='red', linestyle='--')
axes[0, 1].set_xlabel('Residual (Juta Rp)')
axes[0, 1].set_ylabel('Frekuensi')
axes[0, 1].set_title('Distribusi Residual')

# 3. Feature Importance
if hasattr(model_terbaik.named_steps['regressor'], 'feature_importances_'):
    importances = model_terbaik.named_steps['regressor'].feature_importances_
    nama_fitur = model_terbaik.named_steps['preprocessor'].get_feature_names_out()
    fi_df = pd.DataFrame({'Fitur': nama_fitur, 'Importance': importances})
    fi_df = fi_df.sort_values('Importance', ascending=True).tail(10)

    axes[1, 0].barh(fi_df['Fitur'], fi_df['Importance'], color='steelblue')
    axes[1, 0].set_xlabel('Feature Importance')
    axes[1, 0].set_title('Top 10 Fitur Terpenting')

# 4. Perbandingan metrik antar model
model_names = [h['Model'] for h in hasil]
r2_values = [float(h['R2']) for h in hasil]
axes[1, 1].barh(model_names, r2_values, color=['#3498db', '#2ecc71', '#e74c3c'])
axes[1, 1].set_xlabel('R2 Score')
axes[1, 1].set_title('Perbandingan R2 Score')
axes[1, 1].set_xlim(0, 1)
for i, v in enumerate(r2_values):
    axes[1, 1].text(v + 0.01, i, f'{v:.4f}', va='center')

plt.suptitle('Dashboard Evaluasi — Prediksi Harga Properti Jabodetabek',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# --- Kesimpulan ---
print("\n" + "=" * 60)
print("KESIMPULAN PROYEK")
print("=" * 60)
print(f"""
1. Model {best_model_name} menghasilkan prediksi harga properti
   terbaik dengan R2 yang tinggi.

2. Fitur paling berpengaruh: luas bangunan, lokasi, dan
   jumlah kamar — sesuai dengan hipotesis H1.

3. Model ensemble (Random Forest, Gradient Boosting) lebih baik
   dari Linear Regression — mendukung hipotesis H2.

4. Model dapat digunakan sebagai referensi harga wajar untuk
   pembeli dan penjual properti di Jabodetabek.

KETERBATASAN:
- Dataset simulasi, bukan data marketplace sesungguhnya
- Tidak memperhitungkan faktor makroekonomi (inflasi, suku bunga)
- Tidak memperhitungkan tren harga temporal

REKOMENDASI:
- Lanjutkan dengan data marketplace sesungguhnya
- Tambahkan fitur geospasial (jarak ke MRT, jalan tol)
- Implementasikan monitoring untuk deteksi data drift
""")
```

---

## 14.11 Contoh Proyek: Analisis Sentimen Produk E-Commerce

### 14.11.1 Ringkasan

**Judul:** *Analisis Sentimen Review Produk E-Commerce Indonesia dengan Machine Learning*

**Deskripsi:** Proyek ini membangun model klasifikasi sentimen (positif/negatif) dari teks review produk di marketplace Indonesia. Menggunakan TF-IDF sebagai feature extraction dan membandingkan Logistic Regression, Random Forest, dan SVM.

### 14.11.2 Kerangka Kode

```python
# ============================================================
# PROYEK CONTOH 2: ANALISIS SENTIMEN E-COMMERCE INDONESIA
# ============================================================

import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline

# --- Simulasi Data Review Produk ---
np.random.seed(42)

review_positif = [
    "Barang bagus banget, sesuai deskripsi, pengiriman cepat",
    "Kualitas oke untuk harga segini, recommended seller",
    "Mantap barangnya, packing aman, cepat sampai",
    "Bagus sesuai foto, bahan adem, ukuran pas",
    "Puas banget beli di sini, sudah repeat order",
    "Produk original, seller responsif, pengiriman kilat",
    "Keren banget, anak suka, kualitas premium",
    "Bahan tebal, jahitan rapi, warna sesuai gambar",
    "Harga murah kualitas bagus, tidak mengecewakan",
    "Makasih seller, barang sampai dengan selamat",
] * 100  # 1000 review positif

review_negatif = [
    "Barang jelek, tidak sesuai gambar, kecewa berat",
    "Pengiriman lama banget, sudah seminggu belum sampai",
    "Kualitas buruk, bahan tipis, mudah sobek",
    "Warna beda dari foto, ukuran kekecilan",
    "Seller tidak responsif, chat tidak dibalas",
    "Barang rusak saat diterima, packing tidak aman",
    "Produk palsu, bukan original seperti yang diklaim",
    "Mengecewakan, harga mahal tapi kualitas jelek",
    "Sudah komplain tapi tidak ada solusi dari seller",
    "Menyesal beli di sini, uang terbuang sia-sia",
] * 100  # 1000 review negatif

# Gabungkan dataset
teks = review_positif + review_negatif
label = [1] * len(review_positif) + [0] * len(review_negatif)

# Tambahkan noise (variasi)
for i in range(len(teks)):
    if np.random.random() < 0.3:
        teks[i] = teks[i] + " " + np.random.choice([
            "terima kasih", "semoga awet", "kapok deh",
            "nungguin lama", "worth it", "zonk"
        ])

df_sentimen = pd.DataFrame({'review': teks, 'sentimen': label})
df_sentimen = df_sentimen.sample(frac=1, random_state=42).reset_index(drop=True)

print(f"Dataset: {len(df_sentimen)} review")
print(f"Positif: {sum(df_sentimen['sentimen'] == 1)}")
print(f"Negatif: {sum(df_sentimen['sentimen'] == 0)}")

# --- Preprocessing Teks ---
def bersihkan_teks(teks):
    """Preprocessing teks review Bahasa Indonesia."""
    teks = teks.lower()                         # Lowercase
    teks = re.sub(r'[^a-zA-Z\s]', '', teks)    # Hapus angka dan simbol
    teks = re.sub(r'\s+', ' ', teks).strip()    # Hapus spasi berlebih
    return teks

df_sentimen['review_bersih'] = df_sentimen['review'].apply(bersihkan_teks)

# --- Split Data ---
X = df_sentimen['review_bersih']
y = df_sentimen['sentimen']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# --- Model Comparison ---
models_nlp = {
    'Logistic Regression': Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1, 2))),
        ('clf', LogisticRegression(max_iter=1000, random_state=42))
    ]),
    'Random Forest': Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1, 2))),
        ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
    ]),
    'Linear SVM': Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1, 2))),
        ('clf', LinearSVC(max_iter=2000, random_state=42))
    ]),
}

print("\n" + "=" * 60)
print("PERBANDINGAN MODEL SENTIMEN ANALYSIS")
print("=" * 60)

for nama, model in models_nlp.items():
    cv = cross_val_score(model, X_train, y_train, cv=5, scoring='f1')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"\n{nama}:")
    print(f"  CV F1: {cv.mean():.4f} (+/- {cv.std():.4f})")
    print(classification_report(y_test, y_pred,
                                target_names=['Negatif', 'Positif']))
```

---

## AI Corner — Level: Expert

### AI sebagai Full ML Development Partner

| Aspek | Deskripsi |
|-------|-----------|
| **Level** | Expert — AI sebagai partner penuh dalam seluruh tahap proyek |
| **Tools** | ChatGPT, Claude, GitHub Copilot, Cursor |
| **Fokus** | End-to-end project management, code review, deployment, dokumentasi |

### Kapan Menggunakan AI dalam Proyek?

| Tahap Proyek | Boleh Pakai AI | Contoh Prompt |
|-------------|---------------|---------------|
| Problem Definition | Ya | "Sarankan 3 hipotesis untuk proyek prediksi harga properti Jakarta menggunakan dataset dari marketplace" |
| EDA | Ya | "Visualisasi apa yang paling informatif untuk dataset tabular dengan 1 target numerik dan 10 fitur campuran?" |
| Feature Engineering | Ya | "Sarankan 5 engineered features untuk prediksi harga properti berdasarkan: luas, lokasi, kamar, tahun" |
| Model Selection | Ya | "Dataset saya: 3000 baris, 15 fitur, target regresi. Model apa yang cocok selain Linear Regression?" |
| Debugging | Ya | "Error: ValueError pada OneHotEncoder. Ada kategori di test set yang tidak ada di training set. Bagaimana mengatasinya?" |
| Deployment | Ya | "Tulis template Streamlit untuk model prediksi harga properti dengan input: luas, lokasi, kamar" |
| Interpretasi | Hati-hati | "R2 saya 0.87 untuk prediksi harga properti. Apakah ini baik? Bandingkan dengan benchmark industri" |

### Kapan TIDAK Menggunakan AI?

- Jangan gunakan AI untuk **seluruh** proyek tanpa pemahaman sendiri
- Jangan gunakan AI untuk **memalsukan** data atau hasil
- Jangan gunakan AI untuk menulis **kesimpulan** tanpa memahami analisis
- Jangan gunakan AI sebagai pengganti **belajar** konsep dasar

### Template AI Usage Log untuk Proyek Akhir

```python
# ============================================================
# AI USAGE LOG — PROYEK AKHIR
# ============================================================
import pandas as pd

ai_log = pd.DataFrame({
    'No': range(1, 8),
    'Tanggal': ['2026-03-01', '2026-03-03', '2026-03-05',
                '2026-03-08', '2026-03-10', '2026-03-12', '2026-03-14'],
    'Tahap': [
        'Problem Definition', 'EDA', 'Feature Engineering',
        'Model Training', 'Evaluation', 'Deployment', 'Dokumentasi'
    ],
    'AI_Tool': [
        'Claude', 'ChatGPT', 'Claude',
        'Copilot', 'Claude', 'ChatGPT', 'Claude'
    ],
    'Prompt': [
        'Rumuskan hipotesis prediksi harga properti',
        'Kode EDA untuk dataset properti 3000 baris',
        'Sarankan engineered features untuk properti',
        'Autocomplete pipeline sklearn',
        'Interpretasi R2=0.87 dalam konteks properti',
        'Template Streamlit untuk model regresi',
        'Review struktur notebook proyek'
    ],
    'Validasi': [
        'Cek relevansi hipotesis dengan data',
        'Jalankan kode, validasi output',
        'Verifikasi fitur masuk akal',
        'Cek data leakage, validasi pipeline',
        'Cross-check dengan literatur',
        'Test deployment berjalan',
        'Revisi struktur berdasarkan rubrik'
    ],
    'Modifikasi': [
        'Tambah hipotesis tentang lokasi',
        'Ganti colormap, tambah label Rp',
        'Hapus 1 fitur redundan',
        'Tambah cross-validation',
        'Tambah konteks pasar properti Indonesia',
        'Tambah error handling',
        'Perbaiki narasi kesimpulan'
    ]
})

# Kebijakan AI untuk proyek:
print("KEBIJAKAN PENGGUNAAN AI DALAM PROYEK AKHIR")
print("=" * 50)
print("1. AI BOLEH digunakan untuk semua tahap proyek")
print("2. Setiap penggunaan WAJIB didokumentasikan")
print("3. Mahasiswa WAJIB memahami kode yang dihasilkan AI")
print("4. Validasi independen WAJIB dilakukan")
print("5. Copy-paste tanpa pemahaman = pelanggaran integritas")
print()
print("AI Usage Log:")
print(ai_log.to_string(index=False))
```

> **Prinsip Amanah:** Proyek akhir adalah ujian kemampuan Anda yang sesungguhnya. Menggunakan AI tanpa memahami hasilnya sama dengan berbohong tentang kemampuan sendiri. Jadilah mahasiswa yang amanah — gunakan AI untuk **memperkuat** kemampuan, bukan untuk **menggantikan** proses belajar. Sebagaimana firman Allah SWT: *"Sesungguhnya Allah menyuruh kamu menyampaikan amanat kepada yang berhak menerimanya."* (QS. An-Nisa: 58)

---

## Checklist Penyelesaian Proyek

Gunakan checklist berikut untuk memastikan proyek Anda lengkap sebelum dikumpulkan:

### Tahap 1: Problem Definition
- [ ] Latar belakang masalah ditulis dengan jelas
- [ ] Minimal 2 pertanyaan penelitian dirumuskan
- [ ] Hipotesis formal ditulis
- [ ] Tipe ML (klasifikasi/regresi/clustering) ditentukan
- [ ] Metrik evaluasi dipilih dengan justifikasi

### Tahap 2: EDA
- [ ] Dataset di-load dan diinspeksi (shape, dtypes, missing)
- [ ] Statistik deskriptif dihitung dan diinterpretasi
- [ ] Minimal 5 visualisasi informatif dibuat
- [ ] Insight dari EDA ditulis (minimal 3 poin)

### Tahap 3: Preprocessing
- [ ] Missing values ditangani dengan justifikasi
- [ ] Outliers diidentifikasi dan ditangani
- [ ] Feature engineering dilakukan (minimal 1 fitur baru)
- [ ] Data di-split sebelum preprocessing (no data leakage)
- [ ] Pipeline preprocessing dibuat dengan ColumnTransformer

### Tahap 4: Model Training
- [ ] Minimal 3 model berbeda dilatih
- [ ] Cross-validation 5-fold diterapkan
- [ ] Perbandingan metrik ditampilkan dalam tabel

### Tahap 5: Evaluation
- [ ] Model terbaik dievaluasi secara mendalam
- [ ] Classification report / regression metrics dilaporkan
- [ ] Confusion matrix atau scatter plot dibuat
- [ ] Feature importance ditampilkan

### Tahap 6: Deployment
- [ ] Model final disimpan (joblib/pickle)
- [ ] Metadata model disimpan (JSON)
- [ ] Flask API atau Streamlit dashboard dibuat
- [ ] Deployment diuji dan berfungsi

### Tahap 7: Dokumentasi
- [ ] Notebook terstruktur dengan markdown narasi
- [ ] Kode memiliki komentar yang jelas
- [ ] Kesimpulan dan rekomendasi ditulis
- [ ] AI Usage Log lengkap dan transparan
- [ ] Referensi dicantumkan

### Presentasi
- [ ] Slide presentasi disiapkan (maksimal 10 slide)
- [ ] Demo deployment siap ditunjukkan
- [ ] Latihan presentasi sudah dilakukan (max 15 menit)

---

## Rangkuman Bab 14

1. **Proyek akhir** adalah kulminasi seluruh mata kuliah AI/ML, mengintegrasikan pengetahuan dan keterampilan dari Bab 1-13 dalam proyek machine learning end-to-end yang komprehensif.

2. **Tujuh tahapan proyek** harus dilalui secara sistematis: Problem Definition, EDA, Feature Engineering, Model Training, Evaluation, Deployment, dan Dokumentasi. Setiap tahap memiliki deliverable yang jelas.

3. **Dataset konteks Indonesia** wajib digunakan — dari BPS, Open Data Jakarta, Kaggle Indonesia, atau sumber lain yang relevan. Minimal 500 observasi dengan fitur yang cukup untuk analisis ML.

4. **Minimal 3 model ML** harus dibandingkan menggunakan cross-validation untuk memilih model terbaik secara fair. Jangan hanya mengandalkan satu model.

5. **Deployment sederhana** (Flask API atau Streamlit dashboard) menunjukkan bahwa mahasiswa tidak hanya mampu membangun model di notebook, tetapi juga membawanya ke bentuk yang bisa digunakan oleh pengguna.

6. **AI Usage Log** adalah komponen wajib yang mendokumentasikan setiap interaksi signifikan dengan AI. Dokumentasi yang baik menunjukkan pemahaman, integritas, dan kemampuan validasi independen mahasiswa.

7. **Rubrik penilaian** terdiri dari 9 komponen dengan total 100%. Bobot terbesar pada model training & selection (20%), data & preprocessing (15%), dan evaluasi & interpretasi (15%).

8. **Prinsip amanah** dalam proyek akhir berarti: menggunakan AI secara transparan, memahami setiap baris kode yang digunakan, dan melakukan validasi independen terhadap setiap output AI.

---

## Referensi

### Referensi Utama
1. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
2. Muller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*. O'Reilly Media.
3. Huyen, C. (2022). *Designing Machine Learning Systems*. O'Reilly Media.

### Referensi Pendukung
4. scikit-learn Documentation. (2025). *scikit-learn User Guide*. Retrieved from https://scikit-learn.org/stable/user_guide.html
5. Streamlit Documentation. (2025). *Streamlit Documentation*. Retrieved from https://docs.streamlit.io/
6. Flask Documentation. (2025). *Flask Documentation*. Retrieved from https://flask.palletsprojects.com/

### Referensi Dataset Indonesia
7. BPS. (2025). *Badan Pusat Statistik — Data Indonesia*. Retrieved from https://www.bps.go.id
8. Open Data Jakarta. (2025). *Portal Data Terbuka Jakarta*. Retrieved from https://data.jakarta.go.id
9. Kaggle. (2025). *Kaggle Datasets — Indonesia*. Retrieved from https://www.kaggle.com/datasets

### Referensi Etika AI
10. UNESCO. (2021). *Recommendation on the Ethics of Artificial Intelligence*. UNESCO Digital Library.
11. ACM. (2018). *ACM Code of Ethics and Professional Conduct*. Association for Computing Machinery.

---

*Buku ini dilanjutkan dengan **Penutup: Refleksi dan Langkah ke Depan***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
