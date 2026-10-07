# Minggu 14: AI-Augmented Development dan MLOps

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 14 |
| **Topik** | AI-Augmented Development dan MLOps |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK-7: Mengevaluasi dan merancang pipeline ML end-to-end dengan pendekatan AI-augmented dan prinsip responsible AI |
| **Sub-CPMK** | 14.1 Mengevaluasi kualitas kode ML yang dihasilkan AI dan menerapkan praktik MLOps dasar |
| | 14.2 Merancang pipeline ML end-to-end dengan memperhatikan aspek deployment, monitoring, dan etika AI |
| **Bloom's Taxonomy** | C5-C6 (Mengevaluasi-Mencipta / *Evaluate-Create*) |
| **Durasi** | 2 x 100 menit (Teori 100 min + Praktikum 100 min) |
| **Platform** | Google Colab |
| **Metode** | Ceramah interaktif, live coding, studi kasus, diskusi kelompok, pair programming |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menerapkan** teknik prompt engineering yang efektif untuk menghasilkan kode ML berkualitas menggunakan AI assistants.
2. **Mengevaluasi** secara kritis kode ML yang dihasilkan AI melalui testing, debugging, dan verifikasi.
3. **Menjelaskan** konsep dasar MLOps termasuk model lifecycle, versioning, dan experiment tracking.
4. **Menerapkan** teknik menyimpan dan memuat model ML menggunakan joblib dan pickle.
5. **Merancang** konsep deployment model ML sederhana menggunakan Flask API.
6. **Mengevaluasi** isu-isu responsible AI termasuk fairness, accountability, transparency, dan etika.
7. **Menganalisis** ekosistem AI di Indonesia dan peluang karir di bidang AI/ML.

---

## Materi Pembelajaran

### 1. AI sebagai Coding Partner untuk ML

#### Paradigma Baru: AI-Augmented Development

AI-Augmented Development adalah pendekatan pengembangan perangkat lunak di mana AI berfungsi sebagai **partner kolaboratif** (*co-pilot*), bukan pengganti developer. Dalam konteks machine learning, ini berarti menggunakan AI untuk mempercepat proses pengembangan sambil tetap mempertahankan pemahaman dan kontrol penuh.

```
Tradisional                    AI-Augmented
┌──────────┐                   ┌──────────┐
│ Developer │                   │ Developer │ ←→ │ AI Assistant │
│ menulis   │                   │ mengarahkan│    │ membantu     │
│ semua kode│                   │ & evaluasi │    │ generate     │
└──────────┘                   └──────────┘    └─────────────┘
      │                               │
  Lambat tapi                   Cepat DAN
  terkontrol                    terkontrol
```

#### Prompt Engineering untuk Kode ML

**Prompt engineering** adalah seni menyusun instruksi yang tepat agar AI menghasilkan output berkualitas tinggi. Untuk kode ML, ada prinsip-prinsip khusus:

| Prinsip | Contoh Buruk | Contoh Baik |
|---|---|---|
| **Spesifik** | *"Buatkan model ML"* | *"Buatkan model Random Forest untuk klasifikasi 3 kelas bunga iris menggunakan scikit-learn, dengan train-test split 80:20"* |
| **Berikan konteks** | *"Fix error ini"* | *"Kode ini menggunakan pandas dan scikit-learn. Error: ValueError pada line 15. Dataset memiliki kolom kategorikal yang belum di-encode"* |
| **Minta penjelasan** | *"Tulis kode saja"* | *"Tulis kode beserta komentar yang menjelaskan setiap langkah dan alasan pemilihan hyperparameter"* |
| **Iteratif** | Satu prompt panjang | Minta secara bertahap: preprocessing dulu, lalu modeling, lalu evaluasi |

#### Template Prompt untuk ML

```
Saya sedang mengerjakan proyek ML dengan spesifikasi berikut:
- Dataset: [deskripsi dataset, jumlah baris/kolom, tipe data]
- Tujuan: [klasifikasi/regresi/clustering]
- Target variable: [nama kolom target]
- Constraint: [Google Colab, Python 3, library yang tersedia]

Tolong buatkan kode untuk:
1. [langkah spesifik]
2. [langkah spesifik]

Sertakan komentar dalam Bahasa Indonesia dan tampilkan metrik evaluasi.
```

---

### 2. Evaluasi Kritis Kode AI

#### Mengapa Evaluasi Kritis Penting?

Kode yang dihasilkan AI **tidak selalu benar**. Beberapa masalah umum:

| Masalah | Contoh | Dampak |
|---|---|---|
| **Kode usang** | Menggunakan API yang deprecated | Error saat runtime |
| **Bug tersembunyi** | Data leakage dalam preprocessing | Model overfit, performa buruk di produksi |
| **Logika salah** | Scaling sebelum train-test split | Validasi tidak reliable |
| **Inefisien** | Loop Python vs operasi vektorisasi | Lambat pada data besar |
| **Keamanan** | Hardcoded credentials, unsafe pickle | Vulnerability |

#### Checklist Evaluasi Kode ML dari AI

```
□ Apakah library dan versi yang digunakan kompatibel?
□ Apakah ada data leakage? (scaling/encoding sebelum split?)
□ Apakah random seed di-set untuk reproducibility?
□ Apakah metrik evaluasi sesuai dengan tipe masalah?
□ Apakah kode menangani missing values dengan tepat?
□ Apakah komentar dan variabel deskriptif?
□ Apakah saya memahami setiap baris kode?
□ Sudahkah saya menjalankan dan memverifikasi output?
```

> **Prinsip Amanah:** Sebagai seorang yang dipercaya untuk mengembangkan sistem AI, kita bertanggung jawab memastikan kode berfungsi dengan benar dan tidak merugikan pengguna. Menggunakan kode AI tanpa verifikasi adalah bentuk pengabaian amanah.

---

### 3. MLOps: Manajemen Lifecycle Model

#### Apa itu MLOps?

**MLOps** (*Machine Learning Operations*) adalah sekumpulan praktik yang menggabungkan Machine Learning, DevOps, dan Data Engineering untuk mengelola lifecycle model ML secara efisien dan reliable.

```
ML Lifecycle
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌──────────┐    ┌──────────┐
│ Data     │ →  │ Model    │ →  │ Model   │ →  │ Model    │ →  │ Model    │
│ Prep     │    │ Training │    │ Eval    │    │ Deploy   │    │ Monitor  │
└─────────┘    └──────────┘    └─────────┘    └──────────┘    └──────────┘
     ↑                                                              │
     └──────────────── Feedback Loop ──────────────────────────────┘
```

#### Komponen MLOps

| Komponen | Deskripsi | Tools |
|---|---|---|
| **Version Control** | Versioning kode dan data | Git, DVC |
| **Experiment Tracking** | Mencatat hyperparameter dan metrik | MLflow, Weights & Biases |
| **Pipeline Automation** | Otomasi alur training | Kubeflow, Apache Airflow |
| **Model Registry** | Menyimpan dan mengelola versi model | MLflow Model Registry |
| **Deployment** | Menyajikan model ke pengguna | Flask, FastAPI, Docker |
| **Monitoring** | Memantau performa model di produksi | Prometheus, Grafana |

---

### 4. Model Versioning dan Experiment Tracking

#### Mengapa Perlu Tracking?

Dalam pengembangan model ML, kita sering melakukan banyak eksperimen dengan variasi:
- Hyperparameter yang berbeda
- Fitur yang berbeda
- Algoritma yang berbeda
- Data preprocessing yang berbeda

Tanpa tracking yang baik, kita mudah kehilangan jejak eksperimen mana yang menghasilkan model terbaik.

#### Konsep MLflow

**MLflow** adalah platform open-source untuk mengelola lifecycle ML. Komponen utamanya:

| Komponen | Fungsi |
|---|---|
| **MLflow Tracking** | Mencatat parameter, metrik, dan artefak eksperimen |
| **MLflow Projects** | Standarisasi format proyek ML |
| **MLflow Models** | Format standar untuk packaging model |
| **MLflow Registry** | Registrasi dan versioning model |

#### Contoh Manual Tracking (Alternatif Sederhana)

Jika belum menggunakan MLflow, bisa membuat tracking sederhana menggunakan dictionary dan DataFrame:

```python
# Tracking eksperimen secara manual
eksperimen_log = []

eksperimen_log.append({
    'experiment_id': 1,
    'model': 'Random Forest',
    'n_estimators': 100,
    'max_depth': 10,
    'accuracy': 0.85,
    'f1_score': 0.83,
    'catatan': 'Baseline model'
})
```

---

### 5. Model Deployment: Menyimpan dan Memuat Model

#### Mengapa Perlu Menyimpan Model?

Setelah model dilatih, kita perlu menyimpannya agar bisa digunakan kembali tanpa training ulang. Ini disebut **model persistence** atau **model serialization**.

#### Dua Format Populer

| Format | Library | Keunggulan | Keterbatasan |
|---|---|---|---|
| **joblib** | `joblib` | Efisien untuk objek NumPy/scikit-learn | Spesifik Python |
| **pickle** | `pickle` | Bawaan Python, universal | Risiko keamanan (unsafe deserialization) |

#### Konsep Flask API untuk Model Serving

**Flask** adalah web framework ringan Python yang bisa digunakan untuk menyajikan model ML melalui REST API:

```
Client (App/Web)     →    Flask API Server    →    Model ML
[Kirim data input]        [Terima request]        [Prediksi]
                          [Return response]   ←    [Hasil prediksi]
```

---

### 6. Model Monitoring: Concept Drift dan Data Drift

#### Mengapa Model Perlu Dimonitor?

Model ML yang sudah di-deploy **tidak selamanya akurat**. Performa model bisa menurun seiring waktu karena perubahan di dunia nyata.

#### Jenis Drift

| Jenis Drift | Deskripsi | Contoh |
|---|---|---|
| **Data Drift** | Distribusi data input berubah | Demografi pelanggan berubah karena ekspansi pasar |
| **Concept Drift** | Hubungan antara input dan output berubah | Perilaku belanja berubah setelah pandemi |
| **Model Drift** | Performa model menurun secara bertahap | Akurasi turun dari 95% ke 80% dalam 6 bulan |

#### Tanda-tanda Model Perlu Di-retrain

```
Monitoring Alerts
├── Akurasi prediksi menurun signifikan
├── Distribusi data input berubah (Kolmogorov-Smirnov test)
├── Feedback pengguna menunjukkan prediksi sering salah
├── Waktu respons model meningkat drastis
└── Data baru memiliki kategori/fitur yang tidak ada saat training
```

> **Analogi:** Model ML seperti peta navigasi -- peta yang dibuat tahun 2020 mungkin tidak akurat di tahun 2026 karena jalan baru, gedung baru, dan perubahan aturan lalu lintas. Model perlu "diperbarui" secara berkala.

---

### 7. Responsible AI: Fairness, Accountability, Transparency

#### Prinsip-Prinsip Responsible AI

| Prinsip | Deskripsi | Pertanyaan Kunci |
|---|---|---|
| **Fairness** | Model tidak boleh diskriminatif | Apakah model memberikan hasil yang adil untuk semua kelompok? |
| **Accountability** | Ada pihak yang bertanggung jawab | Siapa yang bertanggung jawab jika model salah prediksi? |
| **Transparency** | Proses pengambilan keputusan bisa dijelaskan | Bisakah kita menjelaskan mengapa model memberikan prediksi tertentu? |
| **Privacy** | Data pengguna dilindungi | Apakah data pribadi ditangani sesuai regulasi? |
| **Safety** | Sistem aman dan robust | Apa dampak terburuk jika model gagal? |

#### Bias dalam AI: Studi Kasus

| Kasus | Masalah | Pelajaran |
|---|---|---|
| **Amazon Recruitment AI** | Bias gender -- mendiskriminasi pelamar perempuan | Data historis yang bias menghasilkan model bias |
| **COMPAS Recidivism** | Bias ras dalam prediksi kriminalitas | Model tidak boleh digunakan sebagai satu-satunya penentu keputusan kritis |
| **Google Photos** | Salah label gambar orang berkulit gelap | Dataset training harus representatif dan inklusif |

#### Responsible AI dan Nilai-Nilai Islam

| Nilai Islam | Prinsip Responsible AI | Penerapan |
|---|---|---|
| **Amanah** | Accountability | Bertanggung jawab atas sistem AI yang kita bangun |
| **Al-'Adl** (Keadilan) | Fairness | Memastikan model tidak mendiskriminasi kelompok tertentu |
| **Al-Bayan** (Transparansi) | Transparency | Menjelaskan cara kerja model, tidak menjadi "kotak hitam" |
| **La Dharar** (Tidak Merugikan) | Safety & Privacy | Melindungi data pengguna dan meminimalkan risiko |
| **Ihsan** (Kebaikan) | Beneficial AI | Mengembangkan AI yang membawa manfaat bagi masyarakat |

---

### 8. Karir di Bidang AI/ML

#### Jalur Karir Utama

| Peran | Fokus Utama | Keahlian Kunci |
|---|---|---|
| **Data Scientist** | Analisis data & pemodelan | Statistik, ML, komunikasi bisnis |
| **ML Engineer** | Membangun sistem ML di produksi | Software engineering, MLOps, cloud |
| **AI Researcher** | Riset dan inovasi algoritma baru | Matematika, deep learning, paper writing |
| **Data Engineer** | Infrastruktur dan pipeline data | SQL, Spark, cloud infrastructure |
| **AI Product Manager** | Mengelola produk berbasis AI | Bisnis, teknis, UX |
| **AI Ethics Officer** | Memastikan AI bertanggung jawab | Etika, regulasi, audit model |

#### Ekosistem AI di Indonesia

| Aspek | Deskripsi |
|---|---|
| **STRANAS-AI** | Strategi Nasional Kecerdasan Artifisial Indonesia 2020-2045 |
| **AI Startups** | Nodeflux (computer vision), Kata.ai (NLP), Prosa.ai (speech), Qlue (smart city) |
| **Big Tech** | Google AI Indonesia, AWS AI, Microsoft AI -- membuka lab riset di Indonesia |
| **Akademik** | UI, ITB, UGM, ITS memiliki program riset AI aktif |
| **Komunitas** | Indonesia AI, Data Science Indonesia, Jakarta Machine Learning |
| **Regulasi** | UU PDP No. 27/2022, draft regulasi AI oleh Kominfo |

> **Motivasi:** Indonesia memiliki potensi besar di bidang AI. Dengan populasi 270+ juta jiwa dan digitalisasi yang pesat, kebutuhan tenaga ahli AI/ML akan terus meningkat. Sebagai mahasiswa Informatika UAI, Anda memiliki kesempatan untuk berkontribusi pada kemajuan AI di Indonesia.

---

### 9. Ekosistem AI Indonesia: STRANAS-AI dan Peluang Karir

#### Lima Fokus STRANAS-AI

1. **Kesehatan** -- AI untuk diagnosis, drug discovery, telemedicine
2. **Reformasi Birokrasi** -- AI untuk pelayanan publik yang efisien
3. **Pendidikan** -- AI untuk personalized learning, adaptive assessment
4. **Ketahanan Pangan** -- AI untuk pertanian presisi, prediksi panen
5. **Mobilitas & Smart City** -- AI untuk transportasi cerdas, IoT

#### Peluang Kerja AI/ML di Indonesia

```
Entry Level (0-2 tahun)          Mid Level (2-5 tahun)        Senior (5+ tahun)
├── Junior Data Scientist        ├── Data Scientist           ├── Lead Data Scientist
├── ML Engineer Intern           ├── ML Engineer              ├── Principal ML Engineer
├── Data Analyst                 ├── AI Product Manager       ├── Head of AI/ML
└── AI Research Assistant        └── AI Ethics Analyst        └── AI Director / CTO
```

---

## Aktivitas Kelas

### Sesi 1: Teori dan Diskusi (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Pembukaan & Review | Review computer vision (Minggu 13), konteks minggu ini |
| 20 menit | Ceramah: AI-Augmented Development | Prompt engineering untuk ML, evaluasi kode AI |
| 15 menit | Live Demo: Prompt Engineering | Demonstrasi live menggunakan AI untuk generate kode ML, evaluasi hasilnya |
| 15 menit | Ceramah: MLOps Fundamentals | Model lifecycle, versioning, experiment tracking |
| 15 menit | Ceramah: Responsible AI | Fairness, bias, transparency, nilai-nilai Islam |
| 15 menit | Diskusi: Karir AI di Indonesia | STRANAS-AI, startup AI, peluang karir |
| 10 menit | Q&A & Transisi Praktikum | Pertanyaan, persiapan hands-on |

### Sesi 2: Praktikum Hands-on (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Setup Environment | Import library, persiapan dataset |
| 20 menit | AI-Augmented Coding | Pair programming dengan AI assistant |
| 20 menit | End-to-End ML Pipeline | Bangun pipeline lengkap: data → model → evaluasi |
| 15 menit | Save & Load Model | Praktik menyimpan dan memuat model |
| 15 menit | Experiment Tracking | Implementasi tracking sederhana |
| 15 menit | Diskusi Responsible AI | Analisis bias pada model yang dibuat |
| 5 menit | Wrap-up & Preview | Rangkuman, preview Minggu 15: Proyek Akhir |

---

## Hands-on: End-to-End ML Pipeline dengan AI-Augmented Development

### Langkah 1: Setup dan Import Library

```python
# Import semua library yang dibutuhkan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, f1_score)

# Model persistence
import joblib
import pickle
import json
import os

print("Semua library berhasil di-import!")
print(f"Waktu eksperimen: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
```

### Langkah 2: Membuat Dataset Indonesia (Simulasi)

```python
# Simulasi dataset: Prediksi kelulusan tepat waktu mahasiswa Indonesia
np.random.seed(42)
n_samples = 500

data = {
    'ipk': np.round(np.random.normal(3.2, 0.4, n_samples).clip(2.0, 4.0), 2),
    'sks_diambil': np.random.randint(18, 24, n_samples),
    'kehadiran_persen': np.random.randint(60, 100, n_samples),
    'jam_belajar_per_minggu': np.random.randint(5, 30, n_samples),
    'organisasi': np.random.choice(['Tidak', 'Ya'], n_samples, p=[0.4, 0.6]),
    'beasiswa': np.random.choice(['Tidak', 'Ya'], n_samples, p=[0.7, 0.3]),
    'asal_sekolah': np.random.choice(['SMA', 'SMK', 'MA'], n_samples, p=[0.5, 0.3, 0.2]),
    'kota_asal': np.random.choice(['Jakarta', 'Bogor', 'Depok', 'Tangerang', 'Bekasi'],
                                   n_samples),
}

# Membuat target variable berdasarkan aturan logis
lulus_tepat_waktu = (
    (np.array(data['ipk']) > 3.0).astype(int) * 2 +
    (np.array(data['kehadiran_persen']) > 75).astype(int) * 2 +
    (np.array(data['jam_belajar_per_minggu']) > 15).astype(int) +
    np.random.randint(0, 3, n_samples)
)
data['lulus_tepat_waktu'] = (lulus_tepat_waktu >= 4).astype(int)

df = pd.DataFrame(data)
print("=== Dataset Prediksi Kelulusan Mahasiswa ===")
print(f"Jumlah data: {len(df)}")
print(f"\nDistribusi target:")
print(df['lulus_tepat_waktu'].value_counts())
print(f"\n5 baris pertama:")
df.head()
```

### Langkah 3: Preprocessing Pipeline

```python
# Preprocessing: encoding dan feature engineering
df_processed = df.copy()

# Label encoding untuk kolom kategorikal
le_organisasi = LabelEncoder()
le_beasiswa = LabelEncoder()
le_sekolah = LabelEncoder()
le_kota = LabelEncoder()

df_processed['organisasi'] = le_organisasi.fit_transform(df_processed['organisasi'])
df_processed['beasiswa'] = le_beasiswa.fit_transform(df_processed['beasiswa'])
df_processed['asal_sekolah'] = le_sekolah.fit_transform(df_processed['asal_sekolah'])
df_processed['kota_asal'] = le_kota.fit_transform(df_processed['kota_asal'])

# Pisahkan fitur dan target
X = df_processed.drop('lulus_tepat_waktu', axis=1)
y = df_processed['lulus_tepat_waktu']

# Train-test split (SEBELUM scaling -- ini penting!)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scaling (SETELAH split -- hindari data leakage!)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Gunakan transform, bukan fit_transform!

print("=== Preprocessing Selesai ===")
print(f"Training set: {X_train_scaled.shape}")
print(f"Test set: {X_test_scaled.shape}")
print(f"\nDistribusi target (training):")
print(y_train.value_counts())
```

### Langkah 4: Experiment Tracking Sederhana

```python
# Membuat sistem experiment tracking sederhana
experiment_log = []

def log_experiment(exp_id, model_name, params, y_true, y_pred, catatan=""):
    """Mencatat hasil eksperimen ke dalam log"""
    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, average='weighted')

    record = {
        'exp_id': exp_id,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'model': model_name,
        'params': str(params),
        'accuracy': round(acc, 4),
        'f1_score': round(f1, 4),
        'catatan': catatan
    }
    experiment_log.append(record)
    print(f"[Exp {exp_id}] {model_name}: Accuracy={acc:.4f}, F1={f1:.4f}")
    return record

print("Fungsi experiment tracking siap digunakan!")
```

### Langkah 5: Melatih Beberapa Model

```python
# === Eksperimen 1: Logistic Regression (Baseline) ===
model_lr = LogisticRegression(random_state=42, max_iter=1000)
model_lr.fit(X_train_scaled, y_train)
y_pred_lr = model_lr.predict(X_test_scaled)
log_experiment(1, 'Logistic Regression', {'max_iter': 1000}, y_test, y_pred_lr, 'Baseline')

# === Eksperimen 2: Random Forest ===
model_rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model_rf.fit(X_train_scaled, y_train)
y_pred_rf = model_rf.predict(X_test_scaled)
log_experiment(2, 'Random Forest', {'n_estimators': 100, 'max_depth': 10}, y_test, y_pred_rf, 'Ensemble method')

# === Eksperimen 3: Random Forest (Tuned) ===
model_rf2 = RandomForestClassifier(n_estimators=200, max_depth=15, min_samples_split=5, random_state=42)
model_rf2.fit(X_train_scaled, y_train)
y_pred_rf2 = model_rf2.predict(X_test_scaled)
log_experiment(3, 'Random Forest (Tuned)', {'n_estimators': 200, 'max_depth': 15}, y_test, y_pred_rf2, 'Hyperparameter tuning')

# === Eksperimen 4: Gradient Boosting ===
model_gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
model_gb.fit(X_train_scaled, y_train)
y_pred_gb = model_gb.predict(X_test_scaled)
log_experiment(4, 'Gradient Boosting', {'n_estimators': 100, 'lr': 0.1}, y_test, y_pred_gb, 'Boosting method')

# Tampilkan ringkasan eksperimen
print("\n=== Ringkasan Semua Eksperimen ===")
df_experiments = pd.DataFrame(experiment_log)
print(df_experiments[['exp_id', 'model', 'accuracy', 'f1_score', 'catatan']].to_string(index=False))
```

### Langkah 6: Visualisasi Perbandingan Model

```python
# Visualisasi perbandingan performa model
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart perbandingan
model_names = df_experiments['model']
accuracies = df_experiments['accuracy']
f1_scores = df_experiments['f1_score']

x = np.arange(len(model_names))
width = 0.35

axes[0].bar(x - width/2, accuracies, width, label='Accuracy', color='steelblue')
axes[0].bar(x + width/2, f1_scores, width, label='F1-Score', color='coral')
axes[0].set_xlabel('Model')
axes[0].set_ylabel('Skor')
axes[0].set_title('Perbandingan Performa Model')
axes[0].set_xticks(x)
axes[0].set_xticklabels(model_names, rotation=45, ha='right')
axes[0].legend()
axes[0].grid(axis='y', alpha=0.3)

# Confusion matrix model terbaik
best_idx = df_experiments['f1_score'].idxmax()
best_model_name = df_experiments.loc[best_idx, 'model']
best_preds = [y_pred_lr, y_pred_rf, y_pred_rf2, y_pred_gb][best_idx]

cm = confusion_matrix(y_test, best_preds)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[1],
            xticklabels=['Tidak Lulus', 'Lulus'], yticklabels=['Tidak Lulus', 'Lulus'])
axes[1].set_title(f'Confusion Matrix - {best_model_name}')
axes[1].set_xlabel('Prediksi')
axes[1].set_ylabel('Aktual')

plt.tight_layout()
plt.show()

print(f"\nModel terbaik: {best_model_name}")
print(f"Classification Report ({best_model_name}):")
print(classification_report(y_test, best_preds, target_names=['Tidak Lulus', 'Lulus']))
```

### Langkah 7: Menyimpan dan Memuat Model

```python
# === Menyimpan model dengan joblib ===
# Simpan model terbaik
best_model = [model_lr, model_rf, model_rf2, model_gb][best_idx]

# Simpan model
joblib.dump(best_model, 'model_kelulusan.joblib')
print("Model disimpan: model_kelulusan.joblib")

# Simpan scaler (penting! scaler harus disimpan bersama model)
joblib.dump(scaler, 'scaler_kelulusan.joblib')
print("Scaler disimpan: scaler_kelulusan.joblib")

# Simpan metadata eksperimen
metadata = {
    'model_name': best_model_name,
    'accuracy': float(df_experiments.loc[best_idx, 'accuracy']),
    'f1_score': float(df_experiments.loc[best_idx, 'f1_score']),
    'features': list(X.columns),
    'target': 'lulus_tepat_waktu',
    'training_date': datetime.now().strftime('%Y-%m-%d'),
    'total_experiments': len(experiment_log)
}

with open('model_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)
print("Metadata disimpan: model_metadata.json")

# === Memuat model kembali ===
print("\n=== Memuat Model Kembali ===")
model_loaded = joblib.load('model_kelulusan.joblib')
scaler_loaded = joblib.load('scaler_kelulusan.joblib')

# Verifikasi: prediksi dengan model yang dimuat
y_pred_loaded = model_loaded.predict(X_test_scaled)
print(f"Akurasi model yang dimuat: {accuracy_score(y_test, y_pred_loaded):.4f}")
print(f"Apakah prediksi sama? {np.array_equal(best_preds, y_pred_loaded)}")
```

### Langkah 8: Simulasi Prediksi untuk Data Baru

```python
# Simulasi: prediksi untuk mahasiswa baru
mahasiswa_baru = pd.DataFrame({
    'ipk': [3.5, 2.8, 3.9],
    'sks_diambil': [21, 18, 22],
    'kehadiran_persen': [90, 65, 95],
    'jam_belajar_per_minggu': [20, 8, 25],
    'organisasi': [1, 0, 1],   # 1=Ya, 0=Tidak
    'beasiswa': [1, 0, 1],
    'asal_sekolah': [2, 1, 0],  # Encoded
    'kota_asal': [0, 2, 1]      # Encoded
})

# Transformasi dengan scaler yang sudah disimpan
mahasiswa_scaled = scaler_loaded.transform(mahasiswa_baru)

# Prediksi
prediksi = model_loaded.predict(mahasiswa_scaled)
probabilitas = model_loaded.predict_proba(mahasiswa_scaled)

print("=== Prediksi Kelulusan Mahasiswa Baru ===")
for i in range(len(mahasiswa_baru)):
    status = "Lulus Tepat Waktu" if prediksi[i] == 1 else "Berisiko Terlambat"
    prob = probabilitas[i][1] * 100
    print(f"Mahasiswa {i+1}: {status} (probabilitas lulus: {prob:.1f}%)")
    print(f"  - IPK: {mahasiswa_baru.iloc[i]['ipk']}, "
          f"Kehadiran: {mahasiswa_baru.iloc[i]['kehadiran_persen']}%, "
          f"Jam belajar: {mahasiswa_baru.iloc[i]['jam_belajar_per_minggu']} jam/minggu")
```

### Langkah 9: Konsep Flask API (Pseudocode)

```python
# === KONSEP: Flask API untuk Model Serving ===
# Kode ini adalah KONSEP / pseudocode -- tidak dijalankan di Colab
# Untuk deployment nyata, kode ini dijalankan di server

"""
# file: app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model dan scaler saat aplikasi dimulai
model = joblib.load('model_kelulusan.joblib')
scaler = joblib.load('scaler_kelulusan.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    # Terima data dari client (format JSON)
    data = request.get_json()

    # Preprocessing
    features = np.array([[
        data['ipk'],
        data['sks_diambil'],
        data['kehadiran_persen'],
        data['jam_belajar_per_minggu'],
        data['organisasi'],
        data['beasiswa'],
        data['asal_sekolah'],
        data['kota_asal']
    ]])

    # Scaling
    features_scaled = scaler.transform(features)

    # Prediksi
    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0]

    # Return hasil
    return jsonify({
        'prediksi': int(prediction),
        'status': 'Lulus Tepat Waktu' if prediction == 1 else 'Berisiko Terlambat',
        'probabilitas_lulus': round(float(probability[1]), 4)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
"""

print("=== Konsep Flask API ===")
print("Kode di atas adalah contoh cara men-deploy model ML sebagai REST API.")
print("Client bisa mengirim request POST ke /predict dengan data JSON.")
print("Server akan mengembalikan hasil prediksi dalam format JSON.")
print("\nContoh request:")
print(json.dumps({
    "ipk": 3.5,
    "sks_diambil": 21,
    "kehadiran_persen": 90,
    "jam_belajar_per_minggu": 20,
    "organisasi": 1,
    "beasiswa": 1,
    "asal_sekolah": 2,
    "kota_asal": 0
}, indent=2))
```

---

## AI Corner: Best Practices untuk AI-Augmented ML Development

> **Level: Expert** -- Minggu ini kita membahas praktik terbaik menggunakan AI dalam pengembangan ML secara profesional.

### Tingkatan Kematangan Penggunaan AI

| Level | Deskripsi | Indikator |
|---|---|---|
| **Beginner** | Menggunakan AI untuk tugas sederhana | Copy-paste kode tanpa modifikasi |
| **Intermediate** | Memahami dan memodifikasi output AI | Bisa menjelaskan kode yang dihasilkan |
| **Advanced** | Berkolaborasi efektif dengan AI | Prompt engineering, iterasi, evaluasi kritis |
| **Expert** | Memimpin proses development dengan AI sebagai tools | Merancang arsitektur, AI membantu implementasi |

### Do's dan Don'ts AI-Augmented Development

| Do's (Lakukan) | Don'ts (Hindari) |
|---|---|
| Verifikasi setiap output AI | Langsung deploy kode AI tanpa testing |
| Gunakan AI untuk brainstorming ide | Bergantung 100% pada AI untuk solusi |
| Minta AI menjelaskan trade-offs | Abaikan peringatan keamanan dari AI |
| Iterasi dan refine prompts | Gunakan prompt satu kali tanpa evaluasi |
| Dokumentasikan penggunaan AI | Klaim kode AI sebagai karya original |
| Pahami limitasi model AI | Percaya AI selalu benar |

### Contoh Prompt Expert-Level

```
Saya membangun pipeline ML end-to-end untuk prediksi kelulusan mahasiswa.
Dataset: 500 sampel, 8 fitur (campuran numerik dan kategorikal),
target binary (lulus/tidak tepat waktu).

Saya sudah mencoba Random Forest dan mendapat akurasi 85%.
Tolong review dan sarankan:
1. Apakah ada potensi data leakage di pipeline saya?
2. Metrik apa selain accuracy yang sebaiknya saya perhatikan
   mengingat class imbalance?
3. Teknik apa untuk meningkatkan performa tanpa overfitting?
4. Bagaimana cara menambahkan fairness check pada model ini?
```

### Tips Penting

1. **AI untuk boilerplate** -- gunakan AI untuk kode repetitif, fokus energi Anda pada desain dan evaluasi
2. **AI untuk debugging** -- paste error + konteks, minta analisis root cause
3. **AI untuk dokumentasi** -- minta AI generate docstring dan komentar setelah kode berfungsi
4. **AI untuk review** -- minta AI review kode Anda dari segi best practices dan keamanan

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai bahan refleksi:

1. **AI sebagai Partner:** Bagaimana pengalaman Anda menggunakan AI sebagai coding partner selama semester ini? Apa yang paling membantu? Apa yang masih kurang?

2. **Evaluasi Kritis:** Berikan contoh kasus di mana kode AI bisa menyesatkan atau berbahaya dalam konteks ML. Bagaimana cara mengantisipasinya?

3. **MLOps di Industri:** Mengapa perusahaan membutuhkan MLOps? Apa yang terjadi jika model ML di-deploy tanpa monitoring?

4. **Responsible AI:** Bayangkan Anda membangun model prediksi kredit untuk bank di Indonesia. Apa saja potensi bias yang mungkin muncul? Bagaimana prinsip keadilan (Al-'Adl) bisa diterapkan?

5. **Karir AI di Indonesia:** Dari berbagai jalur karir AI yang dibahas, mana yang paling menarik bagi Anda? Apa langkah konkret yang bisa Anda ambil mulai sekarang untuk menuju karir tersebut?

---

## Tugas Mandiri Minggu 14

1. **AI-Augmented Pipeline:** Gunakan AI assistant (ChatGPT/Claude) untuk membangun pipeline ML untuk dataset pilihan Anda. Dokumentasikan: (a) semua prompt yang Anda gunakan, (b) modifikasi yang Anda lakukan pada kode AI, (c) evaluasi kritis terhadap output AI. Sertakan screenshot percakapan dengan AI.

2. **Model Persistence:** Simpan model terbaik Anda dalam format joblib. Buat notebook terpisah yang memuat model dan menjalankan prediksi pada 5 data baru. Pastikan hasil prediksi konsisten.

3. **Refleksi Responsible AI:** Tulis esai singkat (300-500 kata) tentang bagaimana prinsip responsible AI dan nilai-nilai Islam bisa diterapkan dalam proyek ML yang Anda kerjakan. Berikan contoh konkret.

---

## Referensi

### Buku Teks

1. Huyen, C. (2022). *Designing Machine Learning Systems*. O'Reilly Media.
2. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
3. Burkov, A. (2020). *Machine Learning Engineering*. True Positive Inc.

### Sumber Online

4. [MLflow Documentation](https://mlflow.org/docs/latest/index.html) -- Platform open-source untuk ML lifecycle management.
5. [Google Responsible AI Practices](https://ai.google/responsibility/responsible-ai-practices/) -- Panduan responsible AI dari Google.
6. [Flask Documentation](https://flask.palletsprojects.com/) -- Web framework untuk API sederhana.

### Referensi Indonesia

7. [STRANAS-AI](https://ai-innovation.id/) -- Strategi Nasional Kecerdasan Artifisial Indonesia.
8. [Indonesia AI Society](https://indonesiaai.org/) -- Komunitas dan ekosistem AI Indonesia.
9. UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi.

---

> **Preview Minggu Depan:** Minggu 15 adalah **Proyek Akhir dan Presentasi** -- saatnya menampilkan hasil belajar selama satu semester dalam bentuk proyek ML end-to-end!

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
