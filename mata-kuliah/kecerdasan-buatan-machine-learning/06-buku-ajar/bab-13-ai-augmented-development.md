# BAB 13: AI-AUGMENTED DEVELOPMENT DAN MLOps

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| Sub-CPMK 14.1 | Mengevaluasi penggunaan AI sebagai coding partner dalam pengembangan model ML secara kritis dan bertanggung jawab | C5 (Mengevaluasi) |
| Sub-CPMK 14.2 | Merancang workflow MLOps dasar untuk deployment dan monitoring model machine learning | C6 (Mencipta) |

**CPMK-7:** Mengevaluasi dan merancang praktik AI-augmented development serta pipeline MLOps untuk siklus hidup model machine learning.

**Estimasi Waktu:** 3 × 50 menit (2 SKS)

**Prasyarat:** Mahasiswa telah memahami seluruh fondasi machine learning (Bab 1–12): supervised learning, unsupervised learning, neural network, dan computer vision.

---

## 13.1 AI sebagai Coding Partner

### 13.1.1 Prompt Engineering untuk Kode ML

Di era 2025-2026, AI coding assistants telah menjadi bagian integral dari workflow pengembangan ML. Kemampuan menulis **prompt yang efektif** adalah skill yang membedakan developer produktif dari yang tidak.

**Framework CRIDE untuk Prompt Engineering:**

```
C - Context    : Berikan konteks proyek dan teknologi yang digunakan
R - Role       : Tentukan peran AI (reviewer, tutor, pair programmer)
I - Instruction: Berikan instruksi yang spesifik dan jelas
D - Data       : Sertakan data, error message, atau kode yang relevan
E - Expected   : Jelaskan output yang diharapkan
```

**Contoh Penerapan CRIDE:**

```python
# === PROMPT YANG BAIK (menggunakan CRIDE) ===
"""
[Context] Saya sedang membangun model klasifikasi sentiment review
produk di marketplace Indonesia menggunakan TF-IDF dan Naive Bayes
dengan scikit-learn.

[Role] Bertindak sebagai ML engineer senior.

[Instruction] Tolong review kode saya dan identifikasi
potensi masalah performa.

[Data]
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Data review produk
reviews = df['review_text'].values
labels = df['sentiment'].values

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(reviews)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2)

model = MultinomialNB()
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)

[Expected] Identifikasi bug, masalah data leakage, dan saran perbaikan.
"""
```

```python
# === PROMPT YANG KURANG BAIK ===
"""
Buatkan model ML yang bagus untuk analisis sentiment
"""
# Terlalu umum — tidak ada konteks, data, atau spesifikasi
```

### 13.1.2 Menggunakan ChatGPT/Claude untuk Debugging, Code Generation, dan Explanation

**Skenario 1: Debugging Error**

```python
# Kode yang menghasilkan error
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Mahasiswa mendapat error saat training
df = pd.read_csv('data_pelanggan.csv')
X = df[['usia', 'pendapatan', 'kota']]  # 'kota' adalah kolom kategorikal
y = df['churn']

model = RandomForestClassifier()
model.fit(X, y)  # Error: could not convert string to float

# === Prompt ke AI ===
"""
Saya mendapat error 'could not convert string to float' saat melatih
RandomForestClassifier. Kolom 'kota' berisi nama kota (string).
DataFrame saya memiliki kolom: usia (int), pendapatan (float),
kota (string: 'Jakarta', 'Surabaya', 'Bandung').
Bagaimana cara menangani kolom kategorikal ini?
"""

# === Solusi yang disarankan AI ===
from sklearn.preprocessing import LabelEncoder

# Encode kolom kategorikal
le = LabelEncoder()
df['kota_encoded'] = le.fit_transform(df['kota'])

# Gunakan kolom yang sudah di-encode
X = df[['usia', 'pendapatan', 'kota_encoded']]
model.fit(X, y)  # Berhasil!

# Alternatif yang lebih baik: One-Hot Encoding
X = pd.get_dummies(df[['usia', 'pendapatan', 'kota']], columns=['kota'])
model.fit(X, y)
```

**Skenario 2: Memahami Konsep**

```python
# Prompt ke AI untuk penjelasan konsep
"""
Jelaskan perbedaan antara cross_val_score dan train_test_split
dalam scikit-learn. Kapan saya harus menggunakan masing-masing?
Berikan contoh kode untuk dataset klasifikasi dengan 1000 sampel.
Gunakan bahasa Indonesia.
"""
```

**Skenario 3: Code Generation dengan Konteks**

```python
# Prompt ke AI untuk generate kode
"""
Buatkan pipeline scikit-learn untuk klasifikasi teks bahasa Indonesia:
1. TF-IDF vectorizer dengan max_features=5000
2. SMOTE untuk handle imbalanced data
3. Random Forest Classifier
4. Cross-validation 5-fold
5. Tampilkan classification report

Gunakan komentar dalam bahasa Indonesia.
"""
```

### 13.1.3 Evaluasi Kritis Kode yang Dihasilkan AI

**PENTING:** Kode dari AI harus selalu **dievaluasi secara kritis** sebelum digunakan.

**Checklist Evaluasi Kode AI:**

| No | Aspek Evaluasi | Pertanyaan Kunci |
|----|---------------|-----------------|
| 1 | **Kebenaran** | Apakah kode menghasilkan output yang benar? |
| 2 | **Data Leakage** | Apakah ada kebocoran data dari test set ke training? |
| 3 | **Efisiensi** | Apakah kode efisien untuk ukuran data yang sebenarnya? |
| 4 | **Reproducibility** | Apakah ada random_state yang di-set? |
| 5 | **Edge Cases** | Bagaimana jika ada missing values, outliers, atau data kosong? |
| 6 | **Library Version** | Apakah API yang digunakan masih valid di versi terbaru? |
| 7 | **Hallucination** | Apakah AI "menghayal" fungsi atau parameter yang tidak ada? |

```python
# Contoh evaluasi kritis kode AI

# === Kode yang dihasilkan AI (mengandung masalah) ===
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# MASALAH: fit_transform pada SELURUH data sebelum split → data leakage!
X_scaled = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# === Kode yang BENAR (setelah evaluasi kritis) ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                      random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # fit hanya pada training
X_test_scaled = scaler.transform(X_test)          # transform saja pada test

model = SVC(kernel='rbf')
model.fit(X_train_scaled, y_train)
```

### 13.1.4 AI Usage Log — Best Practices

Setiap penggunaan AI dalam tugas harus didokumentasikan dalam **AI Usage Log**:

```python
# Contoh format AI Usage Log

ai_usage_log = """
=== AI USAGE LOG ===
Mata Kuliah : Kecerdasan Buatan dan Machine Learning
Tugas       : Tugas 10 - Klasifikasi Gambar dengan CNN
Mahasiswa   : [Nama] - [NIM]
Tanggal     : [Tanggal]

--- Entri 1 ---
AI Tool     : ChatGPT (GPT-4)
Waktu       : 14:30, 15 Maret 2026
Prompt      : "Jelaskan perbedaan antara GlobalAveragePooling2D
               dan Flatten dalam Keras. Kapan masing-masing digunakan?"
Respons AI  : [Ringkasan respons]
Penggunaan  : Memahami konsep — dipelajari, lalu diterapkan
               dengan modifikasi di kode saya.
Evaluasi    : Respons akurat, saya verifikasi dengan dokumentasi Keras.

--- Entri 2 ---
AI Tool     : Claude
Waktu       : 15:45, 15 Maret 2026
Prompt      : "Model CNN saya overfitting. Training acc 97%,
               val acc 68%. Bagaimana cara menambahkan Dropout?"
Respons AI  : [Ringkasan respons + kode]
Penggunaan  : Debugging — menerapkan saran Dropout(0.5)
               dan menambahkan augmentasi data.
Evaluasi    : Kode berfungsi, val acc meningkat ke 82%.

--- Ringkasan ---
Total interaksi AI: 2
Dampak: Mempercepat debugging dan pemahaman konsep.
Semua kode ditulis sendiri dengan bantuan pemahaman dari AI.
"""
print(ai_usage_log)
```

---

## 13.2 MLOps Overview

### 13.2.1 ML Lifecycle: Experimentation → Development → Deployment → Monitoring

**MLOps** (Machine Learning Operations) adalah praktik yang menggabungkan ML, DevOps, dan Data Engineering untuk men-deploy dan memelihara model ML secara andal dan efisien.

```
                    ML LIFECYCLE
    ┌─────────────────────────────────────────┐
    │                                         │
    ▼                                         │
┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐
│ Experiment │──→│ Development│──→│ Deployment │──→│ Monitoring │
│            │   │            │   │            │   │            │
│ - EDA      │   │ - Pipeline │   │ - API      │   │ - Drift    │
│ - Feature  │   │ - Testing  │   │ - Scaling  │   │ - Performa │
│ - Model    │   │ - Version  │   │ - CI/CD    │   │ - Retrain  │
│   Selection│   │   Control  │   │            │   │            │
└────────────┘   └────────────┘   └────────────┘   └──────┬─────┘
                                                          │
                                                          │ Feedback
                                                          ▼
                                                   ┌────────────┐
                                                   │  Retrain   │
                                                   │  & Update  │
                                                   └────────────┘
```

**Perbedaan Software Development vs ML Development:**

| Aspek | Software Tradisional | Machine Learning |
|-------|---------------------|-----------------|
| **Input** | Kode | Kode + Data + Model |
| **Versi** | Source code saja | Code + Data + Model + Config |
| **Testing** | Unit test, integration test | + Model validation, data validation |
| **Bug** | Deterministik | Bisa stochastic (probabilistik) |
| **Deployment** | Deploy kode | Deploy kode + model + data pipeline |
| **Monitoring** | Uptime, latency | + Model accuracy, data drift |

### 13.2.2 Experiment Tracking (Konsep MLflow)

```python
# Konsep experiment tracking menggunakan MLflow
# Instalasi: !pip install mlflow

import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

# Mulai eksperimen
mlflow.set_experiment("klasifikasi-sentiment-produk")

# Jalankan eksperimen dengan tracking
with mlflow.start_run(run_name="rf_baseline"):
    # Parameter
    n_estimators = 100
    max_depth = 10

    # Log parameter
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("dataset", "review_tokopedia_v2")

    # Training
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Evaluasi
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')

    # Log metrik
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("f1_score", f1)

    # Log model
    mlflow.sklearn.log_model(model, "model")

    print(f"Accuracy: {accuracy:.4f}")
    print(f"F1 Score: {f1:.4f}")
```

### 13.2.3 Model Versioning

```python
# Konsep model versioning — tracking berbagai versi model

import json
from datetime import datetime

# Metadata model
model_registry = {
    "model_name": "sentiment_classifier",
    "versions": [
        {
            "version": "1.0.0",
            "tanggal": "2026-02-15",
            "algoritma": "Naive Bayes",
            "accuracy": 0.78,
            "f1_score": 0.75,
            "status": "archived"
        },
        {
            "version": "1.1.0",
            "tanggal": "2026-02-22",
            "algoritma": "Random Forest",
            "accuracy": 0.85,
            "f1_score": 0.83,
            "status": "archived"
        },
        {
            "version": "2.0.0",
            "tanggal": "2026-03-01",
            "algoritma": "XGBoost + TF-IDF",
            "accuracy": 0.89,
            "f1_score": 0.87,
            "status": "production"  # Versi yang aktif di produksi
        }
    ]
}

# Tampilkan registry
for v in model_registry["versions"]:
    status_icon = "[ACTIVE]" if v["status"] == "production" else "[archived]"
    print(f"{status_icon} v{v['version']} - {v['algoritma']} "
          f"- Acc: {v['accuracy']:.2f} - F1: {v['f1_score']:.2f}")
```

---

## 13.3 Model Deployment Basics

### 13.3.1 Menyimpan Model: joblib, pickle, Keras save

```python
# === 1. Menyimpan model scikit-learn dengan joblib ===
import joblib
from sklearn.ensemble import RandomForestClassifier

# Training model (contoh)
model_rf = RandomForestClassifier(n_estimators=100, random_state=42)
model_rf.fit(X_train, y_train)

# Simpan model
joblib.dump(model_rf, 'model_sentiment_rf.joblib')
print("Model scikit-learn berhasil disimpan!")

# === 2. Menyimpan model dengan pickle ===
import pickle

with open('model_sentiment_rf.pkl', 'wb') as f:
    pickle.dump(model_rf, f)
print("Model pickle berhasil disimpan!")

# === 3. Menyimpan model Keras/TensorFlow ===
import tensorflow as tf

# Simpan seluruh model (arsitektur + bobot + optimizer)
model_cnn.save('model_cnn_fashion.keras')
print("Model Keras berhasil disimpan!")

# Simpan bobot saja
model_cnn.save_weights('bobot_cnn_fashion.weights.h5')
print("Bobot model berhasil disimpan!")
```

### 13.3.2 Memuat dan Menggunakan Model Tersimpan

```python
# === Memuat model scikit-learn ===
model_loaded = joblib.load('model_sentiment_rf.joblib')

# Prediksi dengan model yang dimuat
review_baru = ["Produk sangat bagus, pengiriman cepat!"]
X_baru = vectorizer.transform(review_baru)
prediksi = model_loaded.predict(X_baru)
print(f"Prediksi sentiment: {prediksi[0]}")

# === Memuat model Keras ===
model_cnn_loaded = tf.keras.models.load_model('model_cnn_fashion.keras')

# Prediksi dengan model Keras yang dimuat
gambar_baru = gambar_baru.reshape(1, 28, 28, 1) / 255.0
prediksi_cnn = model_cnn_loaded.predict(gambar_baru)
kelas_prediksi = prediksi_cnn.argmax()
print(f"Prediksi kelas: {kelas_prediksi}")
```

### 13.3.3 Flask API (Konsep Dasar)

```python
# === Konsep Flask API untuk serving model ===
# File: app.py
# Jalankan di terminal: python app.py

from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Muat model saat startup
model = joblib.load('model_sentiment_rf.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint untuk prediksi sentiment."""
    data = request.get_json()
    review_text = data.get('review', '')

    # Preprocessing dan prediksi
    X = vectorizer.transform([review_text])
    prediksi = model.predict(X)[0]
    probabilitas = model.predict_proba(X)[0].max()

    return jsonify({
        'review': review_text,
        'sentiment': prediksi,
        'confidence': round(float(probabilitas), 4)
    })

@app.route('/health', methods=['GET'])
def health():
    """Endpoint untuk pengecekan kesehatan API."""
    return jsonify({'status': 'ok', 'model': 'sentiment_rf_v2'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# === Contoh request ke API ===
# curl -X POST http://localhost:5000/predict \
#   -H "Content-Type: application/json" \
#   -d '{"review": "Produk bagus, sangat puas!"}'
```

### 13.3.4 Gradio/Streamlit untuk Demo Cepat

```python
# === Gradio — Cara tercepat membuat demo ML ===
# Instalasi: !pip install gradio

import gradio as gr
import joblib

# Muat model
model = joblib.load('model_sentiment_rf.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

def prediksi_sentiment(review):
    """Fungsi prediksi untuk Gradio interface."""
    X = vectorizer.transform([review])
    prediksi = model.predict(X)[0]
    proba = model.predict_proba(X)[0]
    kelas = model.classes_

    # Format output sebagai dictionary probabilitas
    hasil = {kelas[i]: float(proba[i]) for i in range(len(kelas))}
    return hasil

# Buat interface Gradio
demo = gr.Interface(
    fn=prediksi_sentiment,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Masukkan review produk dalam bahasa Indonesia..."
    ),
    outputs=gr.Label(num_top_classes=3),
    title="Analisis Sentiment Review Produk Indonesia",
    description="Masukkan review produk untuk mengetahui sentimentnya.",
    examples=[
        ["Produk bagus, pengiriman cepat, penjual ramah!"],
        ["Barang tidak sesuai deskripsi, kecewa berat"],
        ["Lumayan lah untuk harga segitu"]
    ]
)

# Jalankan
demo.launch(share=True)  # share=True untuk public URL
```

```python
# === Streamlit — Framework web app untuk data science ===
# File: app_streamlit.py
# Jalankan: streamlit run app_streamlit.py

import streamlit as st
import joblib
import pandas as pd

st.title("Analisis Sentiment Review Produk")
st.write("Masukkan review produk Indonesia untuk analisis sentiment.")

# Muat model
model = joblib.load('model_sentiment_rf.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

# Input
review = st.text_area("Review Produk:", height=100)

if st.button("Analisis Sentiment"):
    if review:
        X = vectorizer.transform([review])
        prediksi = model.predict(X)[0]
        proba = model.predict_proba(X)[0]

        # Tampilkan hasil
        st.subheader(f"Sentiment: {prediksi}")
        st.bar_chart(pd.DataFrame({
            'Sentiment': model.classes_,
            'Probabilitas': proba
        }).set_index('Sentiment'))
    else:
        st.warning("Silakan masukkan review terlebih dahulu.")
```

---

## 13.4 Model Monitoring

### 13.4.1 Concept Drift dan Data Drift

Setelah model di-deploy, performanya bisa menurun seiring waktu karena **drift**:

```
Waktu ──────────────────────────────────────────→

Training         Deployment         Drift terjadi!
   │                 │                    │
   ▼                 ▼                    ▼
┌────────┐     ┌──────────┐     ┌──────────────────┐
│ Model  │     │ Model    │     │ Performa menurun │
│ dilatih│────→│ prediksi │────→│ karena data/     │
│        │     │ akurat   │     │ konsep berubah   │
└────────┘     └──────────┘     └──────────────────┘

Data Drift:    Distribusi data input berubah
               Contoh: Pandemi mengubah pola belanja online

Concept Drift: Hubungan input-output berubah
               Contoh: Definisi "spam" berevolusi seiring waktu
```

| Tipe Drift | Penjelasan | Contoh di Indonesia |
|-----------|-----------|---------------------|
| **Data Drift** | Distribusi fitur input berubah | Tren belanja berubah saat Ramadhan vs hari biasa |
| **Concept Drift** | Hubungan fitur-target berubah | Makna kata slang berubah dalam analisis sentiment |
| **Label Drift** | Distribusi target berubah | Proporsi churn pelanggan meningkat saat kompetitor baru masuk |

### 13.4.2 Strategi Monitoring

```python
# Contoh monitoring sederhana: deteksi data drift

import numpy as np
from scipy import stats

def deteksi_data_drift(data_training, data_produksi, threshold=0.05):
    """
    Mendeteksi data drift menggunakan Kolmogorov-Smirnov test.

    Parameters:
    -----------
    data_training : array-like — distribusi data saat training
    data_produksi : array-like — distribusi data di produksi
    threshold : float — nilai p-value untuk menentukan drift

    Returns:
    --------
    dict — hasil deteksi drift per fitur
    """
    hasil_drift = {}

    for fitur in data_training.columns:
        stat, p_value = stats.ks_2samp(
            data_training[fitur].dropna(),
            data_produksi[fitur].dropna()
        )

        drift_terdeteksi = p_value < threshold
        hasil_drift[fitur] = {
            'ks_statistic': round(stat, 4),
            'p_value': round(p_value, 4),
            'drift': drift_terdeteksi
        }

        if drift_terdeteksi:
            print(f"[PERINGATAN] Drift terdeteksi pada fitur '{fitur}' "
                  f"(p-value: {p_value:.4f})")
        else:
            print(f"[OK] Fitur '{fitur}' stabil (p-value: {p_value:.4f})")

    return hasil_drift

# Contoh penggunaan
# hasil = deteksi_data_drift(df_training, df_minggu_ini)
```

---

## 13.5 Responsible AI

### 13.5.1 Fairness dalam Model ML

**Fairness** (keadilan) dalam ML memastikan model tidak mendiskriminasi kelompok tertentu:

```python
# Contoh analisis fairness sederhana

import pandas as pd
import numpy as np

def analisis_fairness(y_true, y_pred, sensitive_attr):
    """
    Menganalisis fairness model berdasarkan atribut sensitif.

    Parameters:
    -----------
    y_true : array — label sebenarnya
    y_pred : array — prediksi model
    sensitive_attr : array — atribut sensitif (misal: gender)
    """
    df = pd.DataFrame({
        'actual': y_true,
        'predicted': y_pred,
        'group': sensitive_attr
    })

    print("=== ANALISIS FAIRNESS ===\n")

    for group in df['group'].unique():
        subset = df[df['group'] == group]
        accuracy = (subset['actual'] == subset['predicted']).mean()
        positive_rate = (subset['predicted'] == 1).mean()

        print(f"Grup: {group}")
        print(f"  Akurasi: {accuracy:.4f}")
        print(f"  Positive Rate: {positive_rate:.4f}")
        print(f"  Jumlah sampel: {len(subset)}")
        print()

    # Disparate Impact Ratio
    groups = df['group'].unique()
    if len(groups) == 2:
        rate_0 = (df[df['group'] == groups[0]]['predicted'] == 1).mean()
        rate_1 = (df[df['group'] == groups[1]]['predicted'] == 1).mean()
        di_ratio = min(rate_0, rate_1) / max(rate_0, rate_1)
        print(f"Disparate Impact Ratio: {di_ratio:.4f}")
        print(f"{'[OK] Fair' if di_ratio >= 0.8 else '[PERINGATAN] Potensi bias'} "
              f"(threshold: 0.8)")

# Contoh penggunaan
# analisis_fairness(y_test, y_pred, df_test['gender'])
```

### 13.5.2 Accountability dan Transparency

**Prinsip-prinsip Responsible AI:**

| Prinsip | Deskripsi | Implementasi |
|---------|-----------|--------------|
| **Transparency** | Model harus bisa dijelaskan | Gunakan SHAP, LIME untuk model interpretability |
| **Accountability** | Ada pihak yang bertanggung jawab | Dokumentasi keputusan desain model |
| **Privacy** | Data pengguna dilindungi | Anonymisasi, differential privacy |
| **Safety** | Model tidak membahayakan | Testing adversarial, monitoring drift |
| **Inclusiveness** | Model adil untuk semua | Audit fairness, diverse training data |

### 13.5.3 Regulasi AI: EU AI Act dan Pendekatan Indonesia

| Regulasi | Cakupan | Status |
|----------|---------|--------|
| **EU AI Act** | Klasifikasi risiko AI (unacceptable, high, limited, minimal) | Berlaku 2024 |
| **STRANAS-AI Indonesia** | Strategi Nasional Kecerdasan Artifisial 2020-2045 | Berjalan |
| **PP 71/2019** | Penyelenggaraan Sistem dan Transaksi Elektronik | Berlaku |
| **RUU PDP** | Perlindungan Data Pribadi | UU No. 27/2022 |

**Fokus STRANAS-AI Indonesia:**
1. Etika dan tata kelola AI
2. Pengembangan talenta AI
3. Infrastruktur data dan komputasi
4. Riset dan inovasi AI
5. Ekosistem industri AI

### 13.5.4 Etika Islam dalam AI: Amanah, Keadilan, Transparansi

Sebagai mahasiswa Universitas Al Azhar Indonesia, pengembangan AI harus berlandaskan nilai-nilai Islam:

| Nilai Islam | Prinsip AI | Implementasi |
|------------|-----------|--------------|
| **Amanah** (Trustworthiness) | Accountability | Dokumentasi lengkap, AI Usage Log, tidak plagiat |
| **Adl** (Keadilan) | Fairness | Model tidak diskriminatif, audit bias berkala |
| **Shiddiq** (Kejujuran) | Transparency | Model yang bisa dijelaskan, tidak menyembunyikan limitasi |
| **Tabligh** (Menyampaikan) | Explainability | Komunikasikan hasil dan keterbatasan model ke stakeholder |
| **Fathonah** (Kecerdasan) | Competence | Terus belajar dan meningkatkan kualitas model |

> *"Sesungguhnya Allah menyuruh kamu menyampaikan amanat kepada yang berhak menerimanya, dan apabila kamu menetapkan hukum di antara manusia, hendaknya kamu menetapkannya dengan adil."*
> — QS An-Nisa [4]: 58

---

## 13.6 AI Career Paths

### 13.6.1 Peran Profesional di Bidang AI

| Peran | Deskripsi | Skills Utama | Gaji (Indonesia)* |
|-------|-----------|-------------|-------------------|
| **Data Scientist** | Analisis data, bangun model ML | Python, statistik, ML, komunikasi | Rp 10-25 juta/bulan |
| **ML Engineer** | Deploy dan optimize model | Python, cloud, Docker, MLOps | Rp 12-30 juta/bulan |
| **AI Researcher** | Riset metode AI baru | Matematika, deep learning, paper writing | Rp 15-35 juta/bulan |
| **Data Engineer** | Bangun data pipeline | SQL, Spark, Airflow, cloud | Rp 10-25 juta/bulan |
| **AI Ethics Officer** | Tata kelola dan etika AI | Hukum, etika, teknis AI, kebijakan | Rp 15-30 juta/bulan |
| **AI Product Manager** | Produk berbasis AI | Bisnis, teknis AI, UX | Rp 15-35 juta/bulan |

*Estimasi 2026, bervariasi berdasarkan pengalaman dan perusahaan.

### 13.6.2 Ekosistem AI Indonesia

**Startup AI Indonesia:**
- **Kata.ai** — NLP dan chatbot bahasa Indonesia
- **Nodeflux** — Computer vision dan face recognition
- **Qlue** — Smart city dan IoT
- **Prosa.ai** — Speech recognition bahasa Indonesia
- **Bukalapak AI Labs** — Rekomendasi produk dan fraud detection

**Lembaga Riset AI:**
- BRIN (Badan Riset dan Inovasi Nasional)
- ITB AI Center
- UI AI and Robotics Research Group
- ITS Computer Vision Lab
- Telkom University AI Lab

**STRANAS-AI Target 2045:**
- Indonesia menjadi hub AI di Asia Tenggara
- 1 juta talenta AI terlatih
- Kontribusi AI ke GDP sebesar 10%

### 13.6.3 Skills Roadmap untuk Karier AI

```
SKILLS ROADMAP AI CAREER
========================

Semester 1-2 (Fondasi):
├── Python Programming
├── Statistika dan Probabilitas
├── Aljabar Linear
└── Struktur Data dan Algoritma

Semester 3-4 (Intermediate):
├── Machine Learning (supervised, unsupervised)
├── Data Wrangling (pandas, SQL)
├── Visualisasi Data
└── Version Control (Git)

Semester 5-6 (Advanced):
├── Deep Learning (CNN, RNN, Transformer)
├── NLP atau Computer Vision (spesialisasi)
├── Cloud Computing (GCP, AWS)
└── MLOps Dasar

Semester 7-8 (Professional):
├── Proyek Industri / Magang
├── Riset / Skripsi AI
├── Portofolio di GitHub dan Kaggle
└── Soft Skills (presentasi, writing)

Setelah Lulus:
├── Sertifikasi (Google ML, AWS ML, TensorFlow)
├── Kontribusi Open Source
├── Networking (komunitas AI Indonesia)
└── Continuous Learning
```

---

## AI Corner — Level: Expert

### Full AI-Augmented Development Workflow

| Aspek | Deskripsi |
|-------|-----------|
| **Level** | Expert — AI sebagai partner penuh dalam siklus pengembangan ML |
| **Tools** | ChatGPT, Claude, GitHub Copilot, Cursor AI |
| **Fokus** | End-to-end AI-assisted development, evaluasi kritis, MLOps |

### Workflow AI-Augmented Development

```
┌─────────────────────────────────────────────────────────┐
│              AI-AUGMENTED ML DEVELOPMENT                │
│                                                         │
│  1. Problem Definition ──→ AI brainstorm pendekatan     │
│  2. Data Exploration ────→ AI generate kode EDA         │
│  3. Feature Engineering ─→ AI suggest fitur baru        │
│  4. Model Selection ─────→ AI compare algoritma         │
│  5. Debugging ───────────→ AI diagnosa error            │
│  6. Optimization ────────→ AI suggest hyperparameter    │
│  7. Documentation ───────→ AI bantu tulis report        │
│  8. Deployment ──────────→ AI generate boilerplate API  │
│                                                         │
│  SELALU: Evaluasi kritis + AI Usage Log                 │
└─────────────────────────────────────────────────────────┘
```

### Refleksi: AI sebagai Tool, Bukan Pengganti

AI adalah **tool yang sangat powerful**, namun tetap membutuhkan **pemikiran kritis manusia**:

1. **AI tidak mengerti konteks bisnis** — hanya mahasiswa yang tahu tujuan sebenarnya
2. **AI bisa menghasilkan kode yang tampak benar tapi salah secara logika** — selalu verifikasi
3. **AI tidak bertanggung jawab** — mahasiswa yang bertanggung jawab atas kode yang disubmit
4. **AI tidak menggantikan pemahaman fundamental** — mahasiswa harus paham statistik, linear algebra, dan ML theory

### Kebijakan Penggunaan AI

| Aktivitas | Kebijakan |
|-----------|-----------|
| **Tugas Mingguan** | AI BOLEH digunakan, WAJIB didokumentasikan dalam AI Usage Log |
| **Kuis** | AI TIDAK BOLEH digunakan (closed-book, di kelas) |
| **UTS** | AI TIDAK BOLEH digunakan (closed-book) |
| **Proyek Akhir** | AI BOLEH digunakan, WAJIB didokumentasikan dalam AI Usage Log |
| **UAS** | AI TIDAK BOLEH digunakan (closed-book) |

---

## Rangkuman Bab 13

1. **AI sebagai Coding Partner** — Gunakan framework CRIDE (Context, Role, Instruction, Data, Expected) untuk prompt engineering yang efektif. Selalu evaluasi kode AI secara kritis.
2. **AI Usage Log** wajib didokumentasikan untuk setiap penggunaan AI dalam tugas — mencerminkan nilai amanah dan transparansi.
3. **MLOps** mengelola siklus hidup model ML dari eksperimen hingga monitoring di produksi — berbeda dari software development tradisional.
4. **Experiment Tracking** (MLflow) dan **Model Versioning** memastikan reproducibility dan traceability eksperimen ML.
5. **Model Deployment** bisa dilakukan dengan menyimpan model (joblib/pickle/Keras save) dan menyediakan API (Flask) atau demo interaktif (Gradio/Streamlit).
6. **Model Monitoring** penting untuk mendeteksi data drift dan concept drift yang menurunkan performa model seiring waktu.
7. **Responsible AI** mencakup fairness, accountability, transparency, privacy, dan safety — dilandasi etika Islam: amanah, keadilan, dan kejujuran.
8. **Karier AI di Indonesia** berkembang pesat — Data Scientist, ML Engineer, AI Researcher adalah beberapa peran yang diminati, didukung ekosistem startup dan riset yang growing.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan apa itu framework CRIDE dalam prompt engineering. Berikan contoh penerapan masing-masing komponen.

**Soal 2.** Sebutkan minimal 3 hal yang harus dievaluasi saat menerima kode yang dihasilkan oleh AI.

**Soal 3.** Jelaskan perbedaan antara data drift dan concept drift. Berikan contoh masing-masing dalam konteks bisnis Indonesia.

**Soal 4.** Apa perbedaan antara menyimpan model dengan `joblib.dump()` dan `model.save()` pada Keras? Kapan masing-masing digunakan?

**Soal 5.** Sebutkan 5 prinsip Responsible AI dan jelaskan secara singkat.

### Tingkat Menengah (C3-C4)

**Soal 6.** Tulis kode Python untuk:
- a) Melatih model RandomForestClassifier pada dataset pilihan Anda
- b) Menyimpan model dan vectorizer dengan joblib
- c) Memuat kembali model yang disimpan
- d) Melakukan prediksi pada data baru

**Soal 7.** Buat AI Usage Log yang lengkap untuk skenario berikut: Anda menggunakan ChatGPT untuk membantu debugging error pada kode training CNN, lalu menggunakan Claude untuk memahami konsep transfer learning. Dokumentasikan kedua interaksi tersebut.

**Soal 8.** Jelaskan bagaimana MLOps berbeda dari software development tradisional. Gunakan tabel perbandingan untuk minimal 5 aspek.

**Soal 9.** Anda diminta membuat demo model klasifikasi sentiment menggunakan Gradio. Tulis kode lengkap yang mencakup:
- a) Loading model yang sudah disimpan
- b) Fungsi prediksi
- c) Interface Gradio dengan contoh input

### Tingkat Mahir (C5-C6)

**Soal 10.** Seorang teman menggunakan ChatGPT untuk menghasilkan seluruh kode proyek ML-nya tanpa memahami kode tersebut. Dia mengklaim bahwa ini adalah "menggunakan AI secara efektif". Evaluasi pendapat teman Anda berdasarkan:
- a) Prinsip academic integrity
- b) Nilai amanah dalam Islam
- c) Kemampuan belajar jangka panjang
- d) Kebijakan penggunaan AI di mata kuliah ini

**Soal 11.** Rancang strategi monitoring untuk model prediksi harga properti di Jakarta yang sudah di-deploy. Jelaskan:
- a) Metrik apa yang akan Anda monitor?
- b) Bagaimana mendeteksi data drift?
- c) Kapan model perlu di-retrain?
- d) Bagaimana menangani situasi darurat (model sangat tidak akurat)?

**Soal 12.** Anda diminta mengaudit fairness sebuah model ML yang digunakan bank untuk menyetujui kredit. Model ini menggunakan fitur: usia, pendapatan, riwayat kredit, jenis kelamin, dan domisili. Lakukan analisis:
- a) Fitur mana yang berpotensi menimbulkan bias?
- b) Metrik fairness apa yang sebaiknya digunakan?
- c) Bagaimana langkah mitigasi jika bias ditemukan?
- d) Kaitkan dengan prinsip keadilan (adl) dalam Islam

---

## Daftar Pustaka Bab 13

1. Huyen, C. (2022). *Designing Machine Learning Systems*. O'Reilly Media.
2. Burkov, A. (2020). *Machine Learning Engineering*. True Positive Inc.
3. Gift, N., & Deza, A. (2021). *Practical MLOps: Operationalizing Machine Learning Models*. O'Reilly Media.
4. Google. (2025). *Responsible AI Practices*. Retrieved from https://ai.google/responsibility/responsible-ai-practices/
5. Kementerian Kominfo. (2020). *Strategi Nasional Kecerdasan Artifisial (STRANAS-AI) 2020-2045*. Kementerian Komunikasi dan Informatika RI.
6. European Parliament. (2024). *EU Artificial Intelligence Act*. Official Journal of the European Union.
7. Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., & Galstyan, A. (2021). A Survey on Bias and Fairness in Machine Learning. *ACM Computing Surveys*, 54(6), 1-35.
8. MLflow Documentation. (2025). *MLflow: An Open Source Platform for the ML Lifecycle*. Retrieved from https://mlflow.org/docs/latest/index.html
9. Gradio Documentation. (2025). *Gradio: Build Machine Learning Web Apps*. Retrieved from https://gradio.app/docs

---

*Bab berikutnya: **Bab 14 — Proyek Akhir***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
