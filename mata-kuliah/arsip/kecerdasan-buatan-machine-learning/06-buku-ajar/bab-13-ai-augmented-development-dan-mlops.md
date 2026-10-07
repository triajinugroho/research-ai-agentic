# BAB 13: AI-AUGMENTED DEVELOPMENT DAN MLOps

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| Sub-CPMK 14.1 | Mengevaluasi efektivitas penggunaan AI sebagai coding partner dalam pengembangan sistem ML | C5 (Mengevaluasi) |
| Sub-CPMK 14.2 | Merancang prompt yang efektif untuk berbagai tugas ML development, termasuk debugging dan code review | C6 (Merancang) |
| Sub-CPMK 14.3 | Mengevaluasi pipeline MLOps end-to-end dari data ingestion hingga model deployment | C5 (Mengevaluasi) |
| Sub-CPMK 14.4 | Merancang model serving sederhana menggunakan Flask API dan Streamlit | C6 (Merancang) |
| Sub-CPMK 14.5 | Mengevaluasi aspek fairness, interpretability, dan accountability dalam pengembangan model ML | C5 (Mengevaluasi) |

**CPMK-7:** Merancang solusi AI end-to-end yang bertanggung jawab dengan konteks Indonesia.

**Estimasi Waktu:** 3 x 50 menit (2 SKS)

**Prasyarat:** Mahasiswa telah memahami seluruh konsep ML dari Bab 1-12, termasuk supervised/unsupervised learning, neural networks, NLP, dan computer vision.

---

## 13.1 AI sebagai Coding Partner dalam ML Development

### 13.1.1 Paradigma Baru: Human-AI Collaboration

Sepanjang 12 bab sebelumnya, kita telah membangun fondasi AI dan Machine Learning yang kokoh — dari matematika dasar, supervised learning, unsupervised learning, deep learning, hingga aplikasi NLP dan Computer Vision. Kini, di bab ini, kita membahas bagaimana **AI itu sendiri** dapat menjadi **mitra kerja** (coding partner) dalam proses pengembangan sistem ML, serta bagaimana membawa model ML dari notebook ke production melalui **MLOps**.

Paradigma ini bukan tentang menggantikan kemampuan programming yang telah kalian pelajari, melainkan tentang **memperkuat** dan **mempercepat** proses development dengan memanfaatkan Large Language Models (LLM) secara cerdas dan bertanggung jawab.

```
EVOLUSI PENGEMBANGAN SOFTWARE/ML
────────────────────────────────

Era 1: Manual Coding (1950-2000)
  Developer → Editor Teks → Kompiler → Program
  [100% usaha manusia]

Era 2: IDE-Assisted (2000-2020)
  Developer → IDE (autocomplete, linting) → Program
  [90% manusia, 10% tooling]

Era 3: AI-Augmented (2020-sekarang)
  Developer ←→ AI Partner (LLM) → Program
  [60-70% manusia, 30-40% AI-assisted]

  ┌─────────────┐     ┌─────────────┐
  │   MANUSIA   │◄───►│     AI      │
  │ • Strategi  │     │ • Boilerplate│
  │ • Arsitektur│     │ • Debugging  │
  │ • Validasi  │     │ • Refactoring│
  │ • Keputusan │     │ • Dokumentasi│
  └─────────────┘     └─────────────┘
```

### 13.1.2 Tools AI untuk ML Development

| Tool | Fungsi Utama | Keunggulan | Keterbatasan |
|------|-------------|------------|--------------|
| **GitHub Copilot** | Code completion real-time | Integrasi IDE, cepat | Kurang konteks panjang |
| **ChatGPT** | Dialog untuk coding, debugging | Konteks dialog panjang | Bisa hallucinate |
| **Claude** | Analisis kode, penjelasan | Konteks sangat panjang | Akses terbatas |
| **Cursor** | IDE dengan AI terintegrasi | Full project context | Berbayar |
| **Google Gemini** | Multi-modal, kode + gambar | Integrasi Google Colab | Masih berkembang |

### 13.1.3 Kapan Menggunakan AI Partner?

**Sangat Efektif:**
- Menulis boilerplate code (setup pipeline, konfigurasi)
- Menjelaskan error message yang kompleks
- Refactoring kode agar lebih bersih
- Menulis docstring dan dokumentasi
- Menghasilkan test cases

**Kurang Efektif:**
- Merancang arsitektur sistem besar (perlu pemahaman domain)
- Memvalidasi kebenaran output ML (perlu domain knowledge)
- Membuat keputusan bisnis dari hasil analisis
- Menangani data sensitif (masalah privasi)

> **Prinsip Amanah:** Menggunakan AI dalam pengembangan ML tanpa memahami apa yang AI hasilkan adalah bentuk ketidakjujuran intelektual. Seorang developer ML yang amanah memahami setiap baris kode yang mereka gunakan — baik yang ditulis sendiri maupun yang dihasilkan AI.

---

## 13.2 Prompt Engineering untuk ML Tasks

### 13.2.1 Framework CRIDE untuk ML Prompting

**CRIDE** (Context, Role, Instruction, Data, Evaluation) adalah framework yang efektif untuk merancang prompt dalam konteks ML:

```
┌──────────────────────────────────────────────────┐
│              FRAMEWORK CRIDE                      │
├──────────────────────────────────────────────────┤
│ C - Context    : Latar belakang proyek ML Anda   │
│ R - Role       : Peran yang diminta dari AI      │
│ I - Instruction: Tugas spesifik yang diminta     │
│ D - Data       : Informasi tentang data Anda     │
│ E - Evaluation : Kriteria keberhasilan output    │
└──────────────────────────────────────────────────┘
```

### 13.2.2 Contoh Prompt untuk Berbagai ML Tasks

**Task 1: Feature Engineering**

```
# Prompt BAIK (menggunakan CRIDE)
"""
Context: Saya sedang mengembangkan model prediksi harga rumah di Jakarta
menggunakan dataset dari Rumah123.com. Dataset berisi kolom: luas_tanah,
luas_bangunan, jumlah_kamar, lokasi, tahun_bangun, harga.

Role: Bertindak sebagai ML Engineer senior yang ahli dalam feature engineering.

Instruction: Sarankan 5 fitur baru (engineered features) yang bisa
meningkatkan performa model regresi saya. Untuk setiap fitur, berikan:
1. Nama fitur
2. Formula/cara membuatnya
3. Alasan mengapa fitur ini berguna
4. Kode Python untuk membuatnya

Data: Dataset memiliki 15.000 baris, harga berkisar 200 juta - 15 miliar.
Lokasi dalam format kecamatan Jakarta.

Evaluation: Fitur yang disarankan harus secara logis berkaitan dengan
harga properti dan dapat diimplementasikan langsung di pandas.
"""
```

**Task 2: Model Selection**

```
# Prompt BAIK
"""
Context: Klasifikasi sentimen review produk di Tokopedia (positif/negatif).
Dataset: 50.000 review teks Bahasa Indonesia.
Fitur: TF-IDF dari teks review (5.000 fitur).
Baseline: Logistic Regression mencapai F1-score 0.78.

Instruction: Rekomendasikan 3 model alternatif yang mungkin lebih baik
dari baseline saya. Untuk setiap model:
1. Nama dan konfigurasi hyperparameter awal
2. Mengapa cocok untuk kasus ini
3. Kode scikit-learn untuk training dan evaluasi
4. Potensi improvement dibanding baseline
"""
```

**Task 3: Debugging Error**

```
# Prompt BAIK
"""
Saya mendapat error saat melatih model Random Forest:
ValueError: Input contains NaN, infinity or a value too large for dtype('float64').

Kode saya:
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
```

Data: X_train shape (10000, 25), beberapa kolom hasil one-hot encoding.
Saya sudah cek df.isnull().sum() dan hasilnya 0.

Tolong bantu diagnosis masalah ini dan berikan solusi step-by-step.
"""
```

### 13.2.3 Anti-Pattern: Prompt yang Tidak Efektif

| Prompt Buruk | Mengapa Buruk | Prompt Perbaikan |
|-------------|---------------|------------------|
| "Buatkan model ML yang bagus" | Tidak spesifik, tidak ada konteks data | "Buatkan model klasifikasi untuk dataset tabular 50K baris, 20 fitur numerik, target binary, menggunakan scikit-learn" |
| "Fix error saya" | Tidak ada error message, tidak ada kode | "Fix ValueError: could not convert string to float. Terjadi di kolom 'harga' yang formatnya 'Rp 1.500.000'" |
| "Tulis kode ML lengkap" | Terlalu luas, AI tidak tahu kebutuhan Anda | "Tulis fungsi Python untuk cross-validation 5-fold dengan metrik F1-score, precision, recall untuk model XGBoost" |

---

## 13.3 AI-Assisted Debugging dan Code Review

### 13.3.1 Pola Debugging dengan AI

Ketika menghadapi error atau bug dalam kode ML, gunakan pendekatan terstruktur berikut:

```
ALUR DEBUGGING DENGAN AI PARTNER
─────────────────────────────────

1. IDENTIFIKASI
   │ • Catat error message lengkap
   │ • Catat kode yang bermasalah
   │ • Catat versi library
   ▼
2. ISOLASI
   │ • Tentukan baris yang menyebabkan error
   │ • Cek input data (shape, dtype, NaN)
   │ • Buat minimal reproducible example
   ▼
3. KONSULTASI AI
   │ • Berikan konteks + error + kode ke AI
   │ • Minta penjelasan + solusi
   │ • Minta beberapa alternatif solusi
   ▼
4. VALIDASI
   │ • Jalankan solusi AI
   │ • Verifikasi hasilnya benar
   │ • Pahami MENGAPA solusi itu bekerja
   ▼
5. DOKUMENTASI
   • Catat masalah dan solusi
   • Update AI Usage Log
```

### 13.3.2 Contoh Debugging: Overfitting pada Model

```python
# ============================================================
# CONTOH: Debugging Overfitting dengan Bantuan AI
# ============================================================

# Langkah 1: Identifikasi masalah
# Model kita mencapai training accuracy 99% tapi test accuracy hanya 65%

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Simulasi dataset klasifikasi produk e-commerce Indonesia
np.random.seed(42)
n_sampel = 1000
n_fitur = 50  # Banyak fitur → rentan overfitting

X = np.random.randn(n_sampel, n_fitur)
y = (X[:, 0] + X[:, 1] > 0).astype(int)  # Hanya 2 fitur yang relevan

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model awal — tanpa tuning (overfitting!)
model_overfit = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,       # Tidak dibatasi → overfitting
    min_samples_leaf=1,   # Minimum 1 sampel per leaf
    random_state=42
)
model_overfit.fit(X_train, y_train)

akurasi_train = accuracy_score(y_train, model_overfit.predict(X_train))
akurasi_test = accuracy_score(y_test, model_overfit.predict(X_test))
print(f"Akurasi Training : {akurasi_train:.4f}")  # ~0.99
print(f"Akurasi Testing  : {akurasi_test:.4f}")   # ~0.65-0.75
print(f"Gap              : {akurasi_train - akurasi_test:.4f}")
print("→ OVERFITTING terdeteksi!\n")

# Langkah 2: Solusi — setelah konsultasi AI
# AI menyarankan: batasi depth, tingkatkan min_samples_leaf, kurangi fitur

model_tuned = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,             # Batasi kedalaman pohon
    min_samples_leaf=10,     # Minimal 10 sampel per leaf
    max_features='sqrt',     # Hanya gunakan sqrt(n_fitur) per split
    random_state=42
)
model_tuned.fit(X_train, y_train)

akurasi_train_tuned = accuracy_score(y_train, model_tuned.predict(X_train))
akurasi_test_tuned = accuracy_score(y_test, model_tuned.predict(X_test))
print(f"Akurasi Training (tuned): {akurasi_train_tuned:.4f}")
print(f"Akurasi Testing  (tuned): {akurasi_test_tuned:.4f}")
print(f"Gap              (tuned): {akurasi_train_tuned - akurasi_test_tuned:.4f}")

# Langkah 3: Visualisasi Learning Curve
train_sizes, train_scores, test_scores = learning_curve(
    model_tuned, X_train, y_train, cv=5,
    train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='accuracy'
)

plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_scores.mean(axis=1), 'o-', label='Training')
plt.plot(train_sizes, test_scores.mean(axis=1), 's-', label='Validation')
plt.fill_between(train_sizes,
                 train_scores.mean(axis=1) - train_scores.std(axis=1),
                 train_scores.mean(axis=1) + train_scores.std(axis=1),
                 alpha=0.1)
plt.fill_between(train_sizes,
                 test_scores.mean(axis=1) - test_scores.std(axis=1),
                 test_scores.mean(axis=1) + test_scores.std(axis=1),
                 alpha=0.1)
plt.xlabel('Jumlah Data Training')
plt.ylabel('Akurasi')
plt.title('Learning Curve — Random Forest (setelah tuning)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 13.3.3 AI-Assisted Code Review

Sebelum mengerjakan tugas atau proyek, minta AI untuk melakukan code review:

```python
# Contoh prompt untuk code review:
"""
Review kode ML saya di bawah ini untuk:
1. Bug potensial (data leakage, error handling)
2. Best practices yang belum diterapkan
3. Performa yang bisa dioptimasi
4. Kualitas kode (naming, structure, comments)

[paste kode Anda di sini]
"""
```

Aspek penting yang harus dicek dalam code review ML:

| Aspek | Yang Dicek | Contoh Masalah |
|-------|-----------|----------------|
| **Data Leakage** | Apakah informasi test set bocor ke training? | Fit scaler pada seluruh data, bukan hanya training |
| **Reproducibility** | Apakah hasil bisa direproduksi? | Lupa set random_state |
| **Memory** | Apakah ada pemborosan memori? | Load seluruh dataset ke RAM tanpa batching |
| **Error Handling** | Apakah edge case ditangani? | Tidak ada pengecekan NaN sebelum training |

---

## 13.4 Pengantar MLOps: ML di Production

### 13.4.1 Apa itu MLOps?

**MLOps** (Machine Learning Operations) adalah praktik yang menggabungkan Machine Learning, DevOps, dan Data Engineering untuk mengelola siklus hidup model ML secara end-to-end di lingkungan production.

```
ML DI NOTEBOOK vs ML DI PRODUCTION
────────────────────────────────────

Di Notebook (80% fokus ML Engineer):
┌─────────────────────────────────────┐
│  Data → Preprocessing → Training    │
│          → Evaluation → "Selesai!"  │
└─────────────────────────────────────┘
  Satu kali jalan, satu dataset, manual

Di Production (80% fokus MLOps):
┌─────────────────────────────────────────────────┐
│  Data Pipeline ──→ Feature Store ──→ Training   │
│       │                                  │      │
│  Monitoring ←── Serving API ←── Registry │      │
│       │              │                          │
│  Retraining ←── Alert (drift detected)          │
└─────────────────────────────────────────────────┘
  Berjalan otomatis, banyak dataset, terus-menerus
```

### 13.4.2 Mengapa MLOps Penting?

Menurut riset Google dan industri AI global:

| Fakta | Implikasi |
|-------|-----------|
| **87% model ML tidak pernah sampai ke production** | Tanpa MLOps, model hanya jadi eksperimen |
| **Model ML degradasi seiring waktu** (data drift) | Perlu monitoring dan retraining otomatis |
| **Debugging model production jauh lebih sulit** | Perlu logging, versioning, dan rollback |
| **Regulasi AI semakin ketat** | Perlu audit trail dan reproducibility |

### 13.4.3 Komponen Utama MLOps

```
KOMPONEN EKOSISTEM MLOps
─────────────────────────

1. DATA MANAGEMENT
   ├── Data Pipeline (Airflow, Prefect)
   ├── Feature Store (Feast, Tecton)
   └── Data Versioning (DVC)

2. MODEL DEVELOPMENT
   ├── Experiment Tracking (MLflow, W&B)
   ├── Hyperparameter Optimization (Optuna)
   └── Model Registry (MLflow)

3. MODEL DEPLOYMENT
   ├── Model Serving (Flask, FastAPI, TF Serving)
   ├── Containerization (Docker)
   └── Orchestration (Kubernetes)

4. MONITORING
   ├── Performance Monitoring (Evidently AI)
   ├── Data Drift Detection
   └── Alerting & Retraining Triggers
```

> **Konteks Indonesia:** Beberapa startup dan perusahaan teknologi Indonesia seperti Gojek, Tokopedia, Bukalapak, dan Bank BCA telah mengadopsi praktik MLOps untuk mengelola ratusan model ML yang melayani jutaan pengguna setiap hari.

---

## 13.5 ML Pipeline End-to-End: Data → Model → Deployment

### 13.5.1 Arsitektur Pipeline Sederhana

```
ML PIPELINE END-TO-END (SEDERHANA)
───────────────────────────────────

┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│   DATA   │───→│ FEATURE  │───→│ TRAINING │───→│ EVALUATE │───→│  DEPLOY  │
│ INGESTION│    │ENGINEERING│    │          │    │          │    │          │
└──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
  CSV/API/DB     Cleaning        fit(X,y)       metrics         Flask API
                 Scaling                         comparison      Streamlit
                 Encoding                        threshold
```

### 13.5.2 Implementasi Pipeline dengan scikit-learn

```python
# ============================================================
# ML Pipeline End-to-End dengan scikit-learn
# Studi Kasus: Klasifikasi Churn Pelanggan Telekomunikasi Indonesia
# ============================================================

import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import (classification_report, roc_auc_score,
                             confusion_matrix)
import joblib
import warnings
warnings.filterwarnings('ignore')

# --- Tahap 1: Data Ingestion ---
# Simulasi dataset churn pelanggan telekomunikasi Indonesia
np.random.seed(42)
n = 5000

data = {
    'usia': np.random.randint(18, 65, n),
    'jenis_kelamin': np.random.choice(['Laki-laki', 'Perempuan'], n),
    'lama_berlangganan_bulan': np.random.randint(1, 72, n),
    'paket': np.random.choice(['Prabayar', 'Pascabayar', 'Combo'], n),
    'pengeluaran_bulanan': np.random.uniform(50000, 500000, n),
    'jumlah_keluhan': np.random.poisson(2, n),
    'skor_kepuasan': np.random.uniform(1, 5, n),
}

df = pd.DataFrame(data)

# Buat target: churn berdasarkan logika bisnis
probabilitas_churn = 1 / (1 + np.exp(-(
    -2 + 0.03 * df['jumlah_keluhan']
    - 0.02 * df['lama_berlangganan_bulan']
    - 0.3 * df['skor_kepuasan']
    + 0.000002 * df['pengeluaran_bulanan']
)))
df['churn'] = (np.random.random(n) < probabilitas_churn).astype(int)

print(f"Dataset: {df.shape[0]} baris x {df.shape[1]} kolom")
print(f"Distribusi churn: {df['churn'].value_counts().to_dict()}")

# --- Tahap 2: Feature Engineering Pipeline ---
# Definisikan kolom numerik dan kategorikal
kolom_numerik = ['usia', 'lama_berlangganan_bulan', 'pengeluaran_bulanan',
                 'jumlah_keluhan', 'skor_kepuasan']
kolom_kategorikal = ['jenis_kelamin', 'paket']

# Pipeline preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ]), kolom_numerik),
        ('cat', Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(drop='first', sparse_output=False))
        ]), kolom_kategorikal)
    ]
)

# --- Tahap 3: Model Training ---
X = df.drop('churn', axis=1)
y = df['churn']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Pipeline lengkap: preprocessing + model
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Training
pipeline.fit(X_train, y_train)

# --- Tahap 4: Evaluasi ---
y_pred = pipeline.predict(X_test)
y_proba = pipeline.predict_proba(X_test)[:, 1]

print("\n=== EVALUASI MODEL ===")
print(f"ROC-AUC Score: {roc_auc_score(y_test, y_proba):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred,
                           target_names=['Tidak Churn', 'Churn']))

# --- Tahap 5: Simpan Model ---
joblib.dump(pipeline, 'model_churn_telko.pkl')
print("\nModel tersimpan: model_churn_telko.pkl")
```

---

## 13.6 Model Versioning dan Experiment Tracking

### 13.6.1 Mengapa Experiment Tracking?

Dalam pengembangan ML, kita sering menjalankan puluhan bahkan ratusan eksperimen dengan variasi hyperparameter, fitur, dan algoritma yang berbeda. Tanpa tracking yang baik, kita akan kehilangan jejak eksperimen mana yang menghasilkan performa terbaik.

```
TANPA EXPERIMENT TRACKING:
──────────────────────────
"Model terbaik saya pake hyperparameter apa ya?"
"Eksperimen kemarin hasilnya berapa?"
"File model_v2_final_FINAL_fix.pkl itu yang mana?"

DENGAN EXPERIMENT TRACKING:
───────────────────────────
┌─────────────────────────────────────────────────────┐
│ Run ID │ Model    │ n_est │ depth │ AUC   │ Status  │
├────────┼──────────┼───────┼───────┼───────┼─────────┤
│ run_01 │ RF       │ 100   │ None  │ 0.821 │         │
│ run_02 │ RF       │ 200   │ 10    │ 0.845 │ best    │
│ run_03 │ XGBoost  │ 150   │ 6     │ 0.838 │         │
│ run_04 │ LogReg   │ -     │ -     │ 0.790 │         │
└─────────────────────────────────────────────────────┘
```

### 13.6.2 MLflow: Experiment Tracking Sederhana

**MLflow** adalah platform open-source untuk mengelola siklus hidup ML. Komponen utamanya:

1. **MLflow Tracking** — Mencatat parameter, metrik, dan artefak dari setiap eksperimen
2. **MLflow Models** — Format standar untuk menyimpan model
3. **MLflow Registry** — Versioning dan staging model

```python
# ============================================================
# Experiment Tracking dengan MLflow
# (Jalankan di Google Colab atau environment lokal)
# ============================================================

# Instalasi MLflow di Google Colab
# !pip install mlflow

import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_auc_score, f1_score
import numpy as np

# Konfigurasi MLflow
mlflow.set_experiment("churn-prediction-telko-indonesia")

# Definisikan eksperimen yang akan dijalankan
eksperimen = [
    {
        'nama': 'Random Forest - Default',
        'model': RandomForestClassifier(n_estimators=100, random_state=42),
        'params': {'model': 'RandomForest', 'n_estimators': 100, 'max_depth': 'None'}
    },
    {
        'nama': 'Random Forest - Tuned',
        'model': RandomForestClassifier(n_estimators=200, max_depth=10,
                                        min_samples_leaf=5, random_state=42),
        'params': {'model': 'RandomForest', 'n_estimators': 200, 'max_depth': 10}
    },
    {
        'nama': 'Gradient Boosting',
        'model': GradientBoostingClassifier(n_estimators=150, max_depth=5,
                                            learning_rate=0.1, random_state=42),
        'params': {'model': 'GradientBoosting', 'n_estimators': 150,
                   'max_depth': 5, 'learning_rate': 0.1}
    },
    {
        'nama': 'Logistic Regression',
        'model': LogisticRegression(max_iter=1000, random_state=42),
        'params': {'model': 'LogisticRegression', 'C': 1.0}
    },
]

# Jalankan semua eksperimen dengan MLflow tracking
# (Asumsikan X_train, X_test, y_train, y_test sudah tersedia
#  dan preprocessor sudah di-fit dari bagian 13.5)

hasil_eksperimen = []

for eks in eksperimen:
    with mlflow.start_run(run_name=eks['nama']):
        # Buat pipeline baru untuk setiap eksperimen
        pipeline_eks = Pipeline([
            ('preprocessor', preprocessor),
            ('classifier', eks['model'])
        ])

        # Training
        pipeline_eks.fit(X_train, y_train)

        # Evaluasi
        y_pred = pipeline_eks.predict(X_test)
        y_proba = pipeline_eks.predict_proba(X_test)[:, 1]
        auc = roc_auc_score(y_test, y_proba)
        f1 = f1_score(y_test, y_pred)

        # Log parameter dan metrik ke MLflow
        mlflow.log_params(eks['params'])
        mlflow.log_metric("auc_score", auc)
        mlflow.log_metric("f1_score", f1)

        # Simpan model ke MLflow
        mlflow.sklearn.log_model(pipeline_eks, "model")

        hasil_eksperimen.append({
            'Nama': eks['nama'],
            'AUC': f"{auc:.4f}",
            'F1': f"{f1:.4f}"
        })

        print(f"[{eks['nama']}] AUC: {auc:.4f}, F1: {f1:.4f}")

# Tampilkan ringkasan eksperimen
import pandas as pd
df_hasil = pd.DataFrame(hasil_eksperimen)
print("\n=== RINGKASAN EKSPERIMEN ===")
print(df_hasil.to_string(index=False))
print(f"\nModel terbaik: {df_hasil.loc[df_hasil['AUC'].astype(float).idxmax(), 'Nama']}")
```

### 13.6.3 Model Versioning Sederhana

Jika belum menggunakan MLflow, minimal lakukan versioning manual:

```python
import joblib
import json
from datetime import datetime

def simpan_model_dengan_metadata(model, nama_model, metrik, catatan=""):
    """
    Menyimpan model beserta metadata untuk versioning sederhana.
    """
    # Buat nama file dengan timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nama_file_model = f"{nama_model}_{timestamp}.pkl"
    nama_file_meta = f"{nama_model}_{timestamp}_metadata.json"

    # Simpan model
    joblib.dump(model, nama_file_model)

    # Simpan metadata
    metadata = {
        'nama_model': nama_model,
        'timestamp': timestamp,
        'metrik': metrik,
        'catatan': catatan,
        'versi_python': '3.10',
        'library': {
            'scikit-learn': '1.3.0',
            'pandas': '2.0.0'
        }
    }
    with open(nama_file_meta, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"Model tersimpan: {nama_file_model}")
    print(f"Metadata tersimpan: {nama_file_meta}")
    return nama_file_model

# Contoh penggunaan
simpan_model_dengan_metadata(
    model=pipeline,
    nama_model="churn_rf",
    metrik={'auc': 0.845, 'f1': 0.72},
    catatan="Random Forest dengan tuning max_depth=10"
)
```

---

## 13.7 Model Serving: Flask API dan Streamlit

### 13.7.1 Model Serving dengan Flask API

**Flask** adalah micro-framework Python yang sangat populer untuk membuat REST API sederhana. Kita bisa menggunakannya untuk menyajikan model ML sebagai web service.

```python
# ============================================================
# model_api.py — Flask API untuk Model Prediksi Churn
# Jalankan di terminal: python model_api.py
# ============================================================

from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Muat model yang sudah dilatih
model = joblib.load('model_churn_telko.pkl')

@app.route('/')
def beranda():
    """Halaman utama API — menampilkan informasi."""
    return jsonify({
        'nama': 'API Prediksi Churn Pelanggan Telekomunikasi',
        'versi': '1.0',
        'pembuat': 'Mahasiswa AI/ML UAI',
        'endpoint': {
            '/prediksi': 'POST — Prediksi churn untuk satu pelanggan',
            '/prediksi_batch': 'POST — Prediksi churn untuk banyak pelanggan',
            '/health': 'GET — Cek status API'
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint untuk cek kesehatan API."""
    return jsonify({'status': 'sehat', 'model_loaded': True})

@app.route('/prediksi', methods=['POST'])
def prediksi():
    """
    Endpoint untuk prediksi churn satu pelanggan.
    Input JSON:
    {
        "usia": 35,
        "jenis_kelamin": "Laki-laki",
        "lama_berlangganan_bulan": 24,
        "paket": "Pascabayar",
        "pengeluaran_bulanan": 250000,
        "jumlah_keluhan": 3,
        "skor_kepuasan": 2.5
    }
    """
    try:
        # Ambil data dari request JSON
        data = request.get_json()

        # Validasi input
        kolom_wajib = ['usia', 'jenis_kelamin', 'lama_berlangganan_bulan',
                       'paket', 'pengeluaran_bulanan', 'jumlah_keluhan',
                       'skor_kepuasan']
        for kolom in kolom_wajib:
            if kolom not in data:
                return jsonify({
                    'error': f'Kolom {kolom} tidak ditemukan dalam input'
                }), 400

        # Konversi ke DataFrame
        df_input = pd.DataFrame([data])

        # Prediksi
        prediksi = model.predict(df_input)[0]
        probabilitas = model.predict_proba(df_input)[0]

        # Kembalikan hasil
        return jsonify({
            'prediksi': 'Churn' if prediksi == 1 else 'Tidak Churn',
            'probabilitas_churn': round(float(probabilitas[1]), 4),
            'probabilitas_tetap': round(float(probabilitas[0]), 4),
            'rekomendasi': (
                'Segera hubungi pelanggan dengan penawaran khusus'
                if prediksi == 1
                else 'Pelanggan kemungkinan akan bertahan'
            )
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/prediksi_batch', methods=['POST'])
def prediksi_batch():
    """Endpoint untuk prediksi batch (banyak pelanggan sekaligus)."""
    try:
        data_list = request.get_json()
        df_input = pd.DataFrame(data_list)

        prediksi = model.predict(df_input)
        probabilitas = model.predict_proba(df_input)[:, 1]

        hasil = []
        for i in range(len(df_input)):
            hasil.append({
                'index': i,
                'prediksi': 'Churn' if prediksi[i] == 1 else 'Tidak Churn',
                'probabilitas_churn': round(float(probabilitas[i]), 4)
            })

        return jsonify({
            'jumlah_data': len(hasil),
            'total_churn': int(sum(prediksi)),
            'hasil': hasil
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Jalankan server
if __name__ == '__main__':
    print("API Prediksi Churn berjalan di http://localhost:5000")
    app.run(debug=True, port=5000)
```

**Menguji API dengan Python requests:**

```python
# ============================================================
# test_api.py — Menguji Flask API
# ============================================================

import requests
import json

# URL API (sesuaikan jika berbeda)
BASE_URL = "http://localhost:5000"

# --- Test 1: Health Check ---
response = requests.get(f"{BASE_URL}/health")
print("Health Check:", response.json())

# --- Test 2: Prediksi satu pelanggan ---
data_pelanggan = {
    "usia": 28,
    "jenis_kelamin": "Perempuan",
    "lama_berlangganan_bulan": 6,
    "paket": "Prabayar",
    "pengeluaran_bulanan": 150000,
    "jumlah_keluhan": 5,
    "skor_kepuasan": 2.0
}

response = requests.post(
    f"{BASE_URL}/prediksi",
    json=data_pelanggan,
    headers={'Content-Type': 'application/json'}
)
print("\nPrediksi satu pelanggan:")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))

# --- Test 3: Prediksi batch ---
data_batch = [
    {"usia": 45, "jenis_kelamin": "Laki-laki",
     "lama_berlangganan_bulan": 48, "paket": "Pascabayar",
     "pengeluaran_bulanan": 350000, "jumlah_keluhan": 1,
     "skor_kepuasan": 4.5},
    {"usia": 22, "jenis_kelamin": "Perempuan",
     "lama_berlangganan_bulan": 3, "paket": "Prabayar",
     "pengeluaran_bulanan": 80000, "jumlah_keluhan": 7,
     "skor_kepuasan": 1.5},
]

response = requests.post(f"{BASE_URL}/prediksi_batch", json=data_batch)
print("\nPrediksi batch:")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))
```

### 13.7.2 Dashboard Interaktif dengan Streamlit

**Streamlit** adalah framework Python untuk membuat dashboard data science dan ML secara interaktif tanpa perlu menguasai HTML/CSS/JavaScript.

```python
# ============================================================
# app_streamlit.py — Dashboard Prediksi Churn
# Jalankan di terminal: streamlit run app_streamlit.py
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Churn Telekomunikasi",
    layout="wide"
)

# Judul dan deskripsi
st.title("Dashboard Prediksi Churn Pelanggan Telekomunikasi")
st.markdown("""
Dashboard ini menggunakan model Machine Learning untuk memprediksi
kemungkinan pelanggan berhenti berlangganan (*churn*).
Dikembangkan sebagai bagian dari mata kuliah **Kecerdasan Buatan dan
Machine Learning** — Universitas Al Azhar Indonesia.
""")

# Muat model
@st.cache_resource
def muat_model():
    return joblib.load('model_churn_telko.pkl')

model = muat_model()

# Sidebar — input data pelanggan
st.sidebar.header("Data Pelanggan")

usia = st.sidebar.slider("Usia", 18, 65, 30)
jenis_kelamin = st.sidebar.selectbox("Jenis Kelamin",
                                      ["Laki-laki", "Perempuan"])
lama_langganan = st.sidebar.slider("Lama Berlangganan (bulan)", 1, 72, 12)
paket = st.sidebar.selectbox("Paket", ["Prabayar", "Pascabayar", "Combo"])
pengeluaran = st.sidebar.number_input("Pengeluaran Bulanan (Rp)",
                                       50000, 500000, 200000, step=10000)
keluhan = st.sidebar.slider("Jumlah Keluhan", 0, 15, 2)
kepuasan = st.sidebar.slider("Skor Kepuasan", 1.0, 5.0, 3.5, step=0.1)

# Buat DataFrame dari input
data_input = pd.DataFrame([{
    'usia': usia,
    'jenis_kelamin': jenis_kelamin,
    'lama_berlangganan_bulan': lama_langganan,
    'paket': paket,
    'pengeluaran_bulanan': pengeluaran,
    'jumlah_keluhan': keluhan,
    'skor_kepuasan': kepuasan
}])

# Tombol prediksi
if st.sidebar.button("Prediksi Churn", type="primary"):
    # Lakukan prediksi
    prediksi = model.predict(data_input)[0]
    probabilitas = model.predict_proba(data_input)[0]

    # Tampilkan hasil
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Prediksi", "CHURN" if prediksi == 1 else "TETAP",
                  delta="Risiko Tinggi" if prediksi == 1 else "Risiko Rendah",
                  delta_color="inverse")

    with col2:
        st.metric("Probabilitas Churn",
                  f"{probabilitas[1]:.1%}")

    with col3:
        st.metric("Probabilitas Tetap",
                  f"{probabilitas[0]:.1%}")

    # Visualisasi probabilitas
    fig, ax = plt.subplots(figsize=(6, 3))
    warna = ['#2ecc71', '#e74c3c']
    ax.barh(['Tetap', 'Churn'], probabilitas, color=warna)
    ax.set_xlim(0, 1)
    ax.set_xlabel('Probabilitas')
    ax.set_title('Distribusi Probabilitas Prediksi')
    for i, v in enumerate(probabilitas):
        ax.text(v + 0.02, i, f'{v:.2%}', va='center')
    st.pyplot(fig)

    # Rekomendasi
    st.subheader("Rekomendasi Tindakan")
    if prediksi == 1:
        st.error("Pelanggan ini berisiko tinggi untuk churn!")
        st.markdown("""
        **Tindakan yang disarankan:**
        1. Hubungi pelanggan dalam 24 jam
        2. Tawarkan diskon atau upgrade paket
        3. Tindak lanjuti keluhan yang belum terselesaikan
        4. Berikan loyalty reward
        """)
    else:
        st.success("Pelanggan ini kemungkinan akan bertahan.")
        st.markdown("""
        **Tindakan preventif:**
        1. Pertahankan kualitas layanan
        2. Kirimkan survey kepuasan berkala
        3. Berikan reward untuk pelanggan loyal
        """)

# Footer
st.markdown("---")
st.markdown(
    "*Dikembangkan oleh mahasiswa Informatika UAI — "
    "Mata Kuliah Kecerdasan Buatan dan Machine Learning*"
)
```

> **Catatan:** Untuk menjalankan Streamlit di Google Colab, gunakan library `pyngrok` atau `localtunnel` untuk membuat tunnel publik.

---

## 13.8 Responsible AI: Fairness, Interpretability, Accountability

### 13.8.1 Mengapa Responsible AI Penting?

Model ML yang di-deploy ke production dapat memiliki dampak nyata terhadap kehidupan manusia. Responsible AI adalah kerangka kerja untuk memastikan sistem AI dikembangkan dan digunakan secara etis, adil, dan bertanggung jawab.

```
PILAR RESPONSIBLE AI
────────────────────

    ┌──────────────┐
    │  RESPONSIBLE  │
    │      AI       │
    └──────┬───────┘
           │
    ┌──────┼──────────────────────┐
    │      │                      │
    ▼      ▼                      ▼
┌────────┐ ┌──────────────┐ ┌──────────────┐
│FAIRNESS│ │INTERPRETAB-  │ │ACCOUNTABILITY│
│(Adil)  │ │ILITY (Dapat  │ │(Bertanggung  │
│        │ │Dijelaskan)   │ │Jawab)        │
└────────┘ └──────────────┘ └──────────────┘
  Tidak       Model bisa       Ada pihak
  diskriminasi  dijelaskan      yang
  terhadap      ke manusia      bertanggung
  kelompok                      jawab atas
  tertentu                      keputusan AI
```

### 13.8.2 Fairness: Keadilan dalam Model ML

Model ML bisa secara tidak sengaja bersifat **diskriminatif** jika data training mengandung bias historis.

**Contoh di Indonesia:**
- Model kredit yang menolak lebih banyak pemohon dari daerah tertentu karena data historis yang bias
- Model rekrutmen yang bias terhadap gender karena data perekrutan masa lalu
- Model kesehatan yang kurang akurat untuk suku tertentu karena kurang terwakili dalam data

```python
# ============================================================
# Evaluasi Fairness Model
# Studi Kasus: Apakah model churn kita adil terhadap gender?
# ============================================================

from sklearn.metrics import accuracy_score, f1_score

def evaluasi_fairness(model, X_test, y_test, kolom_sensitif, df_test):
    """
    Mengevaluasi fairness model terhadap variabel sensitif.
    """
    print(f"=== EVALUASI FAIRNESS: {kolom_sensitif} ===\n")

    # Prediksi keseluruhan
    y_pred = model.predict(X_test)

    # Evaluasi per kelompok
    kelompok_unik = df_test[kolom_sensitif].unique()
    hasil = []

    for kelompok in kelompok_unik:
        mask = df_test[kolom_sensitif] == kelompok
        y_true_k = y_test[mask]
        y_pred_k = y_pred[mask]

        akurasi = accuracy_score(y_true_k, y_pred_k)
        f1 = f1_score(y_true_k, y_pred_k)
        tingkat_positif = y_pred_k.mean()  # Predicted positive rate

        hasil.append({
            'Kelompok': kelompok,
            'Jumlah': mask.sum(),
            'Akurasi': f'{akurasi:.4f}',
            'F1-Score': f'{f1:.4f}',
            'Predicted Positive Rate': f'{tingkat_positif:.4f}'
        })
        print(f"  {kelompok:15s}: Akurasi={akurasi:.4f}, "
              f"F1={f1:.4f}, PPR={tingkat_positif:.4f}")

    # Cek disparitas
    pprs = [float(h['Predicted Positive Rate']) for h in hasil]
    disparitas = max(pprs) - min(pprs)
    print(f"\n  Disparitas Predicted Positive Rate: {disparitas:.4f}")
    print(f"  Status: {'ADIL' if disparitas < 0.05 else 'PERLU PERHATIAN'} "
          f"(threshold: 0.05)")

    return pd.DataFrame(hasil)

# Contoh penggunaan (asumsi df_test tersedia)
# evaluasi_fairness(pipeline, X_test, y_test, 'jenis_kelamin', X_test)
```

### 13.8.3 Interpretability: Model yang Dapat Dijelaskan

```python
# ============================================================
# Model Interpretability dengan Feature Importance
# ============================================================

import matplotlib.pyplot as plt
import numpy as np

def visualisasi_feature_importance(model, nama_fitur):
    """
    Menampilkan feature importance dari model tree-based.
    """
    # Ambil feature importance dari model (setelah pipeline)
    if hasattr(model.named_steps['classifier'], 'feature_importances_'):
        importances = model.named_steps['classifier'].feature_importances_
    else:
        print("Model tidak memiliki feature_importances_")
        return

    # Urutkan berdasarkan importance
    indices = np.argsort(importances)[::-1]

    plt.figure(figsize=(10, 6))
    plt.barh(range(len(importances)),
             importances[indices[::-1]],
             color='steelblue')
    plt.yticks(range(len(importances)),
               [nama_fitur[i] for i in indices[::-1]])
    plt.xlabel('Feature Importance')
    plt.title('Faktor Paling Berpengaruh terhadap Prediksi Churn')
    plt.tight_layout()
    plt.show()

    # Tampilkan tabel
    print("\nPeringkat Fitur:")
    for rank, idx in enumerate(indices, 1):
        print(f"  {rank}. {nama_fitur[idx]:30s}: {importances[idx]:.4f}")

# Contoh penggunaan
# nama_fitur_all = kolom_numerik + ['Perempuan', 'Combo', 'Prabayar']
# visualisasi_feature_importance(pipeline, nama_fitur_all)
```

### 13.8.4 Perspektif Islam tentang Etika AI

Dalam konteks Universitas Al Azhar Indonesia, pengembangan AI yang bertanggung jawab memiliki resonansi kuat dengan nilai-nilai Islam:

| Nilai Islam | Relevansi dengan Responsible AI |
|-------------|-------------------------------|
| **Amanah** (Kepercayaan) | Model ML harus dikembangkan dengan penuh tanggung jawab — data pengguna adalah amanah |
| **Adalah** (Keadilan) | Model tidak boleh diskriminatif terhadap kelompok tertentu (fairness) |
| **Ihsan** (Keunggulan) | Berusaha membuat model dengan kualitas terbaik, bukan sekadar "yang penting jalan" |
| **Shidq** (Kejujuran) | Transparan tentang kemampuan dan keterbatasan model — tidak melebih-lebihkan performa |
| **Maslahat** (Kemaslahatan) | AI harus memberikan manfaat bagi masyarakat, bukan mudarat |

> *"Sesungguhnya Allah menyuruh kamu menyampaikan amanat kepada yang berhak menerimanya, dan (menyuruh kamu) apabila menetapkan hukum di antara manusia supaya kamu menetapkan dengan adil."* (QS. An-Nisa: 58)

---

## 13.9 Studi Kasus: End-to-End ML Project dengan AI Partner

### 13.9.1 Skenario Proyek

Bayangkan Anda adalah seorang data scientist junior di sebuah perusahaan e-commerce Indonesia. Tugas Anda: membangun model prediksi rating produk berdasarkan fitur-fitur produk dan review pelanggan.

Berikut adalah bagaimana Anda menggunakan AI sebagai partner dalam setiap tahap:

### 13.9.2 Tahap-tahap dengan AI Partner

```
ALUR PROYEK DENGAN AI PARTNER
──────────────────────────────

Minggu 1: Problem Definition
  ├── Anda: Definisi bisnis problem
  └── AI: Bantu rumuskan hipotesis dan metrik sukses

Minggu 2: Data Exploration
  ├── Anda: Load dan inspeksi data
  └── AI: Sarankan visualisasi yang tepat dan interpretasi awal

Minggu 3: Feature Engineering
  ├── Anda: Domain knowledge tentang e-commerce Indonesia
  └── AI: Implementasi fitur, encoding, transformasi

Minggu 4: Modeling & Evaluation
  ├── Anda: Pilih pendekatan dan validasi hasil
  └── AI: Tuning hyperparameter, generate code evaluasi

Minggu 5: Deployment & Dokumentasi
  ├── Anda: Keputusan deployment dan presentasi
  └── AI: Flask API boilerplate, dokumentasi kode
```

### 13.9.3 Contoh Interaksi dengan AI

**Prompt ke AI:**
```
Context: Saya sedang mengembangkan model prediksi rating produk
e-commerce Indonesia (skala 1-5). Dataset saya memiliki kolom:
nama_produk, kategori, harga, jumlah_terjual, teks_review, rating.
50.000 baris data.

Instruction: Tulis kode Python untuk:
1. Text preprocessing teks_review (Bahasa Indonesia)
2. Ekstraksi fitur TF-IDF dari review
3. Gabungkan dengan fitur numerik
4. Latih model Random Forest untuk regresi
5. Evaluasi dengan RMSE dan MAE

Data: Teks review dalam Bahasa Indonesia, ada typo dan singkatan.
Evaluation: Kode harus bersih, ada komentar, dan siap jalan di Colab.
```

**Langkah Validasi setelah Menerima Output AI:**
1. Baca dan pahami setiap baris kode yang dihasilkan
2. Jalankan kode dan periksa output
3. Verifikasi metrik evaluasi masuk akal
4. Modifikasi sesuai kebutuhan spesifik proyek
5. Dokumentasikan dalam AI Usage Log

### 13.9.4 Template AI Usage Log untuk ML Project

```python
# ============================================================
# Template AI Usage Log — ML Project
# ============================================================

import pandas as pd
from datetime import datetime

ai_log = pd.DataFrame({
    'No': [1, 2, 3, 4, 5],
    'Tanggal': ['2026-03-01', '2026-03-03', '2026-03-05',
                '2026-03-08', '2026-03-10'],
    'Tahap_ML': [
        'Problem Definition',
        'EDA & Preprocessing',
        'Feature Engineering',
        'Model Training',
        'Deployment'
    ],
    'AI_Tool': ['Claude', 'ChatGPT', 'Claude', 'Copilot', 'ChatGPT'],
    'Prompt_Ringkasan': [
        'Rumuskan hipotesis untuk prediksi rating e-commerce',
        'Kode EDA untuk dataset review produk Indonesia',
        'Sarankan engineered features untuk teks review',
        'Autocomplete training pipeline scikit-learn',
        'Boilerplate Flask API untuk model serving'
    ],
    'Validasi_Yang_Dilakukan': [
        'Verifikasi hipotesis relevan dengan data',
        'Jalankan kode, validasi output visualisasi',
        'Cek fitur masuk akal secara domain',
        'Verifikasi pipeline benar, cek data leakage',
        'Test API endpoint, validasi response format'
    ],
    'Modifikasi': [
        'Tambah 1 hipotesis tentang kategori produk',
        'Ganti colormap, tambah label Indonesia',
        'Hapus 1 fitur yang redundant',
        'Tambah cross-validation, ganti metrik',
        'Tambah error handling, validasi input'
    ]
})

print("=== AI USAGE LOG — PROYEK ML ===")
print(ai_log.to_string(index=False))
```

---

## AI Corner — Level: Expert

### AI sebagai Full ML Development Partner

| Aspek | Deskripsi |
|-------|-----------|
| **Level** | Expert — Gunakan AI sebagai partner penuh dalam pengembangan ML |
| **Tools** | ChatGPT, Claude, GitHub Copilot, Cursor |
| **Fokus** | MLOps, deployment, code review, debugging tingkat lanjut |

### Peta Progresi AI Literacy dalam Buku Ini

| Bab | Level | Fokus AI |
|-----|-------|----------|
| 1-4 | Basic | Memahami apa itu AI, menggunakan AI untuk belajar konsep |
| 5-7 | Intermediate | Menggunakan AI untuk membantu coding dan debugging model |
| 8-10 | Advanced | Menggunakan AI untuk desain eksperimen dan tuning |
| 11-12 | Advanced | AI untuk domain spesifik (NLP, CV) |
| **13** | **Expert** | **AI sebagai coding partner + MLOps + deployment** |
| 14 | Expert | AI sebagai full project partner (proyek akhir) |

### Best Practices untuk AI-Augmented ML Development

1. **Mulai dari Pemahaman, Bukan dari Prompt** — Pahami masalah dan datanya dulu sebelum meminta bantuan AI
2. **Iterasi, Jangan One-Shot** — Jarang sekali output AI pertama sudah sempurna. Iterasi dan perbaiki
3. **Validasi Selalu** — Setiap output AI harus divalidasi: kode dijalankan, metrik dicek, logika diverifikasi
4. **Pelajari dari Output AI** — Jangan hanya copy-paste; pahami mengapa AI memberikan solusi tertentu
5. **Dokumentasi Transparan** — Catat setiap penggunaan AI di AI Usage Log

### Kebijakan Penggunaan AI

| Aktivitas | Kebijakan |
|-----------|-----------|
| **Tugas Mingguan** | AI BOLEH digunakan, WAJIB didokumentasikan dalam AI Usage Log |
| **Kuis** | AI TIDAK BOLEH digunakan (closed-book, di kelas) |
| **UTS** | AI TIDAK BOLEH digunakan (closed-book) |
| **Proyek Akhir** | AI BOLEH digunakan, WAJIB didokumentasikan dalam AI Usage Log |
| **UAS** | AI TIDAK BOLEH digunakan (closed-book) |

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan antara ML di notebook dan ML di production. Sebutkan minimal 3 tantangan yang muncul ketika membawa model ML ke production.

**Soal 2.** Apa kepanjangan dari MLOps? Sebutkan dan jelaskan 4 komponen utama ekosistem MLOps.

**Soal 3.** Jelaskan framework CRIDE untuk prompt engineering dalam konteks ML. Berikan contoh penerapan untuk tugas feature engineering.

**Soal 4.** Apa perbedaan antara Flask dan Streamlit untuk model serving? Kapan sebaiknya menggunakan masing-masing?

**Soal 5.** Jelaskan tiga pilar Responsible AI (Fairness, Interpretability, Accountability) dan berikan contoh masing-masing dalam konteks model ML di Indonesia.

### Tingkat Menengah (C3-C4)

**Soal 6.** Tulis kode Python menggunakan scikit-learn Pipeline untuk membuat preprocessing pipeline yang menangani:
- 3 kolom numerik (imputasi median + scaling)
- 2 kolom kategorikal (imputasi modus + one-hot encoding)
- 1 model klasifikasi (RandomForest)

**Soal 7.** Anda memiliki model ML yang sudah dilatih dan disimpan sebagai file `.pkl`. Tulis kode Flask API sederhana dengan satu endpoint `/prediksi` yang menerima input JSON dan mengembalikan hasil prediksi.

**Soal 8.** Rancang prompt AI menggunakan framework CRIDE untuk membantu Anda men-debug masalah berikut: model klasifikasi Anda mendapatkan akurasi 50% (seperti random guess) pada dataset binary classification dengan 10.000 sampel dan 30 fitur.

**Soal 9.** Jelaskan bagaimana data leakage terjadi dalam pipeline ML. Berikan 2 contoh data leakage dan cara mencegahnya.

### Tingkat Mahir (C5-C6)

**Soal 10.** Anda ditugaskan membangun sistem prediksi kelayakan kredit untuk sebuah bank di Indonesia. Rancang:
- a) Pipeline ML end-to-end (dari data hingga deployment)
- b) Strategi fairness evaluation (variabel sensitif: gender, daerah)
- c) AI Usage Log template yang akan Anda gunakan selama development
- d) Minimal 3 prompt yang akan Anda gunakan untuk konsultasi AI

**Soal 11.** Bandingkan pendekatan model serving berikut untuk konteks startup Indonesia dengan budget terbatas:
- a) Flask API di server cloud
- b) Streamlit dashboard
- c) Batch prediction (scheduled job)
Untuk masing-masing, jelaskan: kelebihan, kekurangan, biaya estimasi, dan skenario penggunaan yang tepat.

**Soal 12.** Anda menemukan bahwa model prediksi churn yang Anda deploy memiliki disparitas akurasi yang signifikan antara pelanggan di Jawa (akurasi 92%) dan pelanggan di luar Jawa (akurasi 74%). Analisis:
- a) Apa kemungkinan penyebab disparitas ini?
- b) Bagaimana cara mendiagnosis akar masalahnya?
- c) Apa langkah-langkah untuk memperbaikinya?
- d) Bagaimana perspektif nilai keadilan (adalah) dalam Islam relevan di sini?

---

## Rangkuman Bab 13

1. **AI sebagai Coding Partner** mengubah cara kita mengembangkan sistem ML — dari menulis seluruh kode sendiri menjadi berkolaborasi dengan LLM untuk mempercepat development. Namun, pemahaman fundamental tetap wajib dimiliki.

2. **Prompt Engineering** yang efektif menggunakan framework CRIDE (Context, Role, Instruction, Data, Evaluation) dapat menghasilkan output AI yang jauh lebih berkualitas dibanding prompt yang generik.

3. **AI-Assisted Debugging** mengikuti alur terstruktur: Identifikasi → Isolasi → Konsultasi AI → Validasi → Dokumentasi. Validasi independen terhadap solusi AI adalah langkah yang tidak boleh dilewatkan.

4. **MLOps** adalah praktik yang menghubungkan ML development dengan production — mencakup data management, experiment tracking, model deployment, dan monitoring. Tanpa MLOps, 87% model ML tidak pernah sampai ke production.

5. **ML Pipeline** dengan scikit-learn Pipeline dan ColumnTransformer memungkinkan preprocessing dan training yang terstruktur, reproducible, dan mudah di-deploy.

6. **Experiment Tracking** dengan tools seperti MLflow membantu mencatat setiap eksperimen beserta parameter, metrik, dan artefaknya — mencegah hilangnya informasi eksperimen.

7. **Model Serving** dapat dilakukan dengan Flask API (untuk integrasi sistem) atau Streamlit (untuk dashboard interaktif) — keduanya dapat dibangun dengan Python murni.

8. **Responsible AI** mencakup Fairness (keadilan), Interpretability (dapat dijelaskan), dan Accountability (bertanggung jawab) — nilai-nilai yang sejalan dengan prinsip Islam tentang amanah, keadilan, dan kemaslahatan.

---

## Referensi

1. Huyen, C. (2022). *Designing Machine Learning Systems*. O'Reilly Media.
2. Treveil, M., et al. (2020). *Introducing MLOps*. O'Reilly Media.
3. Gift, N. & Deza, A. (2021). *Practical MLOps*. O'Reilly Media.
4. Grinberg, M. (2018). *Flask Web Development* (2nd ed.). O'Reilly Media.
5. MLflow Documentation. (2025). *MLflow: A Machine Learning Lifecycle Platform*. Retrieved from https://mlflow.org/docs/latest/
6. Streamlit Documentation. (2025). *Streamlit — The fastest way to build data apps*. Retrieved from https://docs.streamlit.io/
7. Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and Machine Learning: Limitations and Opportunities*. MIT Press.
8. Molnar, C. (2022). *Interpretable Machine Learning* (2nd ed.). Available at https://christophm.github.io/interpretable-ml-book/
9. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
10. UNESCO. (2021). *Recommendation on the Ethics of Artificial Intelligence*. UNESCO Digital Library.

---

*Bab berikutnya: **Bab 14 — Proyek Akhir: Machine Learning End-to-End***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
