# BAB 14: PROYEK AKHIR

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| CPMK 1-7 | Merancang dan mengimplementasikan pipeline ML end-to-end untuk menyelesaikan masalah nyata | C6 (Mencipta) |

**Estimasi Waktu:** 3 × 50 menit (2 SKS) + waktu mandiri untuk pengerjaan proyek

**Prasyarat:** Seluruh materi Bab 1–13.

---

## 14.1 Tujuan Proyek Akhir

Proyek Akhir adalah **puncak perjalanan belajar** di mata kuliah Kecerdasan Buatan dan Machine Learning. Melalui proyek ini, mahasiswa mendemonstrasikan kemampuan untuk:

1. **Mengidentifikasi** masalah nyata yang dapat diselesaikan dengan ML
2. **Mengumpulkan dan mengolah** data secara mandiri
3. **Mengeksplorasi** data menggunakan teknik EDA
4. **Membangun dan melatih** model ML yang sesuai
5. **Mengevaluasi** performa model secara komprehensif
6. **Menyajikan** hasil dan rekomendasi secara profesional
7. **Mendokumentasikan** seluruh proses termasuk penggunaan AI (AI Usage Log)

> *"The best way to learn data science is by doing data science."*
> — Hadley Wickham

---

## 14.2 ML Pipeline End-to-End

### 14.2.1 Problem Definition dan Business Value

Langkah pertama dan **paling penting** adalah mendefinisikan masalah dengan jelas:

```python
# Template definisi masalah

definisi_masalah = """
=== DEFINISI MASALAH PROYEK ===

1. LATAR BELAKANG
   Jelaskan konteks masalah yang ingin diselesaikan.
   Mengapa masalah ini penting? Siapa yang terdampak?

2. RUMUSAN MASALAH
   Pertanyaan spesifik yang ingin dijawab:
   - "Bisakah kita memprediksi harga properti di Jakarta
      berdasarkan fitur lokasi, luas, dan fasilitas?"

3. TIPE MASALAH ML
   [ ] Klasifikasi (prediksi kategori)
   [ ] Regresi (prediksi nilai numerik)
   [ ] Clustering (pengelompokan)
   [ ] Lainnya: ________________

4. METRIK SUKSES
   - Metrik teknis: Accuracy > 85%, RMSE < Rp 100 juta, dll.
   - Metrik bisnis: Potensi penghematan, peningkatan efisiensi, dll.

5. TARGET PENGGUNA
   Siapa yang akan menggunakan hasil model ini?
"""
print(definisi_masalah)
```

### 14.2.2 Data Collection dan Understanding

```python
import pandas as pd
import numpy as np

# Langkah 1: Memuat data
# Sumber data bisa dari: Kaggle, BPS, API publik, web scraping, survei
df = pd.read_csv('dataset_proyek.csv')

# Langkah 2: Pemahaman awal data
print("=== INFORMASI DATASET ===")
print(f"Jumlah baris: {df.shape[0]:,}")
print(f"Jumlah kolom: {df.shape[1]}")
print(f"\nTipe data:\n{df.dtypes}")
print(f"\nMissing values:\n{df.isnull().sum()}")
print(f"\nStatistik deskriptif:\n{df.describe()}")

# Langkah 3: Cek kualitas data
print("\n=== KUALITAS DATA ===")
print(f"Duplikasi: {df.duplicated().sum()} baris")
print(f"Missing total: {df.isnull().sum().sum()} nilai")
for col in df.select_dtypes(include='object').columns:
    print(f"Unique values '{col}': {df[col].nunique()}")
```

### 14.2.3 EDA dan Feature Engineering

```python
import matplotlib.pyplot as plt
import seaborn as sns

# === Exploratory Data Analysis ===

# Distribusi variabel target
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Histogram
axes[0].hist(df['target'], bins=30, edgecolor='black', alpha=0.7)
axes[0].set_title('Distribusi Target')
axes[0].set_xlabel('Nilai')
axes[0].set_ylabel('Frekuensi')

# Boxplot
axes[1].boxplot(df['target'])
axes[1].set_title('Boxplot Target')
plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
numerik_cols = df.select_dtypes(include=[np.number]).columns
sns.heatmap(df[numerik_cols].corr(), annot=True, cmap='coolwarm',
            fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# === Feature Engineering ===
# Contoh: membuat fitur baru
# df['harga_per_m2'] = df['harga'] / df['luas_m2']
# df['usia_bangunan'] = 2026 - df['tahun_bangun']
# df['jarak_pusat_km'] = haversine(df['lat'], df['lon'], lat_pusat, lon_pusat)
```

### 14.2.4 Model Selection dan Training

```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Persiapan data
X = df.drop('target', axis=1)
y = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Bandingkan beberapa model
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(kernel='rbf', probability=True, random_state=42)
}

print("=== PERBANDINGAN MODEL (Cross-Validation 5-Fold) ===\n")
hasil_model = {}

for nama, model in models.items():
    scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='accuracy')
    hasil_model[nama] = {
        'mean_accuracy': scores.mean(),
        'std_accuracy': scores.std()
    }
    print(f"{nama:25s} | Accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")

# Pilih model terbaik
model_terbaik_nama = max(hasil_model, key=lambda x: hasil_model[x]['mean_accuracy'])
print(f"\nModel terbaik: {model_terbaik_nama}")
```

### 14.2.5 Model Evaluation dan Comparison

```python
from sklearn.metrics import (classification_report, confusion_matrix,
                              roc_curve, auc)

# Training model terbaik pada seluruh training set
model_final = models[model_terbaik_nama]
model_final.fit(X_train_scaled, y_train)

# Prediksi
y_pred = model_final.predict(X_test_scaled)
y_proba = model_final.predict_proba(X_test_scaled)[:, 1]

# Classification Report
print("=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, y_pred))

# Confusion Matrix
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title(f'Confusion Matrix — {model_terbaik_nama}')
plt.xlabel('Prediksi')
plt.ylabel('Aktual')
plt.tight_layout()
plt.show()

# ROC Curve (untuk klasifikasi biner)
fpr, tpr, _ = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, linewidth=2, label=f'ROC (AUC = {roc_auc:.4f})')
plt.plot([0, 1], [0, 1], 'k--', linewidth=1)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 14.2.6 Conclusions dan Recommendations

```python
# Template kesimpulan proyek

kesimpulan = """
=== KESIMPULAN DAN REKOMENDASI ===

1. RINGKASAN HASIL
   - Model terbaik: [nama model]
   - Akurasi: [nilai]%
   - F1-Score: [nilai]
   - AUC-ROC: [nilai]

2. TEMUAN UTAMA
   - Fitur paling berpengaruh: [daftar fitur]
   - Pola yang ditemukan: [deskripsi]
   - Insight bisnis: [deskripsi]

3. LIMITASI
   - Ukuran dataset: [jumlah sampel]
   - Periode data: [rentang waktu]
   - Asumsi yang digunakan: [daftar asumsi]

4. REKOMENDASI
   - Untuk improvement model: [saran teknis]
   - Untuk pengguna: [saran implementasi]
   - Untuk pengembangan lanjut: [saran riset]

5. AI USAGE SUMMARY
   - Total interaksi AI: [jumlah]
   - Tools yang digunakan: [daftar tools]
   - Dampak AI pada proses: [deskripsi]
"""
print(kesimpulan)
```

---

## 14.3 Panduan Proyek

### 14.3.1 Kelompok 2–3 Orang

| Aspek | Ketentuan |
|-------|-----------|
| **Jumlah anggota** | 2–3 mahasiswa per kelompok |
| **Pembagian tugas** | Harus jelas dan terdokumentasi |
| **Kontribusi** | Setiap anggota harus berkontribusi signifikan |
| **Peer Review** | Setiap anggota menilai kontribusi anggota lain |

**Contoh Pembagian Tugas:**

| Peran | Tanggung Jawab |
|-------|---------------|
| **Data Engineer** | Pengumpulan data, cleaning, preprocessing |
| **ML Engineer** | Feature engineering, model training, evaluasi |
| **Analyst/Presenter** | EDA, visualisasi, laporan, presentasi |

> **Catatan:** Dalam kelompok 2 orang, setiap anggota mengambil lebih dari satu peran.

### 14.3.2 Timeline Proyek

```
TIMELINE PROYEK AKHIR
=====================

Minggu 10: Proposal
├── Pembentukan kelompok
├── Pemilihan tema dan dataset
├── Definisi masalah dan metodologi
└── Submit: Dokumen proposal (1-2 halaman)

Minggu 12: Progress 1
├── Data collection selesai
├── EDA dan preprocessing lengkap
├── Eksperimen model awal
└── Submit: Notebook progress + update

Minggu 14: Progress 2
├── Model final terlatih dan dievaluasi
├── Visualisasi hasil
├── Draft laporan
└── Submit: Notebook lengkap + draft laporan

Minggu 16: Final Submission
├── Notebook final (bersih dan terdokumentasi)
├── Laporan proyek (format template)
├── Presentasi (10-15 menit per kelompok)
├── AI Usage Log lengkap
└── Peer review form
```

### 14.3.3 Deliverables

**1. Notebook Google Colab:**
- Kode lengkap, terstruktur, dan terdokumentasi
- Markdown cells untuk narasi dan penjelasan
- Output visualisasi tersimpan
- Bisa dijalankan dari awal sampai akhir tanpa error

**2. Laporan Proyek (format .pdf atau .md):**
- Halaman judul
- Abstrak (150-200 kata)
- Bab 1: Pendahuluan (latar belakang, rumusan masalah, tujuan)
- Bab 2: Data dan Metodologi
- Bab 3: Hasil dan Analisis
- Bab 4: Kesimpulan dan Saran
- Daftar Pustaka
- Lampiran: AI Usage Log

**3. Presentasi:**
- Durasi: 10–15 menit presentasi + 5 menit tanya jawab
- Slide: 10–15 slide
- Demo langsung dari notebook (opsional tapi direkomendasikan)

---

## 14.4 Rubrik Penilaian

| Komponen | Bobot | Kriteria Sangat Baik (A) | Kriteria Baik (B) | Kriteria Cukup (C) | Kriteria Kurang (D) |
|----------|:-----:|--------------------------|--------------------|--------------------|---------------------|
| **Problem Definition** | 10% | Masalah jelas, relevan, business value kuat | Masalah jelas, relevan | Masalah cukup jelas | Masalah tidak jelas |
| **Data & EDA** | 20% | EDA komprehensif, insight mendalam, visualisasi excellent | EDA lengkap, visualisasi baik | EDA dasar, visualisasi standar | EDA minimal |
| **Feature Engineering** | 10% | Fitur kreatif dan berdampak signifikan pada model | Fitur yang tepat dan relevan | Fitur standar | Tidak ada feature engineering |
| **Modeling** | 20% | Multiple model dibandingkan, hyperparameter tuning, justifikasi kuat | 2+ model dibandingkan | 1 model, konfigurasi standar | Model tidak tepat |
| **Evaluation** | 15% | Evaluasi komprehensif (multiple metrics, confusion matrix, ROC, interpretasi) | Evaluasi lengkap dengan multiple metrics | Evaluasi dasar (accuracy saja) | Evaluasi tidak memadai |
| **Code Quality** | 10% | Kode bersih, terdokumentasi, reproducible, mengikuti best practice | Kode baik, ada dokumentasi | Kode berfungsi tapi kurang rapi | Kode tidak terstruktur |
| **Presentasi & Laporan** | 10% | Presentasi profesional, laporan komprehensif | Presentasi dan laporan baik | Presentasi dan laporan cukup | Presentasi atau laporan kurang |
| **AI Usage Log** | 5% | Log lengkap, reflektif, menunjukkan penggunaan AI yang bertanggung jawab | Log lengkap dan jujur | Log ada tapi tidak detail | Log tidak ada |
| **TOTAL** | **100%** | | | | |

**Skala Penilaian:**

| Nilai | Rentang | Deskripsi |
|-------|---------|-----------|
| A | 85-100 | Sangat Baik — exceeds expectations |
| B | 70-84 | Baik — meets expectations |
| C | 55-69 | Cukup — partially meets expectations |
| D | 40-54 | Kurang — below expectations |
| E | < 40 | Sangat Kurang — fails to meet expectations |

---

## 14.5 Contoh Tema Proyek (Konteks Indonesia)

### 14.5.1 Prediksi Harga Properti Jakarta

**Deskripsi:** Membangun model regresi untuk memprediksi harga properti di Jakarta berdasarkan fitur lokasi, luas tanah, luas bangunan, jumlah kamar, dan fasilitas sekitar.

**Dataset:** Scraped dari situs properti Indonesia (Rumah123, OLX Properti) atau dataset Kaggle.

**Teknik:** Regresi Linear, Random Forest Regressor, XGBoost Regressor.

### 14.5.2 Klasifikasi Sentiment Review Produk Indonesia

**Deskripsi:** Mengklasifikasikan sentiment (positif/negatif/netral) dari review produk di marketplace Indonesia.

**Dataset:** Scraping dari Tokopedia, Shopee, atau dataset yang sudah tersedia di GitHub/Kaggle.

**Teknik:** TF-IDF + Naive Bayes, TF-IDF + SVM, atau word embeddings + LSTM.

### 14.5.3 Segmentasi Pelanggan E-commerce

**Deskripsi:** Mengelompokkan pelanggan e-commerce berdasarkan perilaku pembelian menggunakan teknik clustering.

**Dataset:** Dataset transaksi e-commerce (bisa menggunakan dataset publik atau simulasi).

**Teknik:** K-Means, DBSCAN, analisis RFM (Recency, Frequency, Monetary).

### 14.5.4 Deteksi Penyakit dari Data Medis Indonesia

**Deskripsi:** Membangun model klasifikasi untuk mendeteksi penyakit (diabetes, jantung, atau stroke) berdasarkan data klinis.

**Dataset:** Dataset publik yang relevan di Kaggle, disesuaikan dengan konteks Indonesia.

**Teknik:** Logistic Regression, Random Forest, Gradient Boosting, Neural Network.

### 14.5.5 Klasifikasi Gambar Makanan Indonesia

**Deskripsi:** Membangun model computer vision untuk mengklasifikasikan jenis makanan Indonesia dari foto.

**Dataset:** Kumpulkan sendiri (minimal 100 gambar per kelas) atau gunakan dataset yang ada.

**Teknik:** CNN from scratch, Transfer Learning (MobileNetV2, ResNet50).

---

## 14.6 Tips Sukses Proyek Akhir

```
TIPS SUKSES PROYEK AKHIR
=========================

1. MULAI DARI YANG SEDERHANA
   ├── Mulai dengan baseline model yang sederhana
   ├── Pastikan pipeline berjalan end-to-end
   └── Baru kemudian tingkatkan kompleksitas

2. DATA ADALAH KUNCI
   ├── Luangkan waktu untuk memahami data
   ├── Visualisasikan sebelum modeling
   └── Garbage in, garbage out!

3. DOKUMENTASI SEJAK AWAL
   ├── Tulis komentar di setiap langkah
   ├── Gunakan markdown cells di notebook
   └── Jangan tunggu deadline untuk menulis laporan

4. GUNAKAN VERSION CONTROL
   ├── Simpan versi notebook secara berkala
   ├── Beri nama file yang deskriptif
   └── Contoh: proyek_v1.ipynb, proyek_v2_after_tuning.ipynb

5. EVALUASI SECARA KOMPREHENSIF
   ├── Jangan hanya lihat accuracy
   ├── Gunakan precision, recall, F1, AUC
   └── Analisis kesalahan model (error analysis)

6. GUNAKAN AI SECARA BERTANGGUNG JAWAB
   ├── AI boleh digunakan untuk membantu
   ├── Tapi PAHAMI setiap baris kode
   └── Dokumentasikan dalam AI Usage Log

7. KERJA TIM YANG EFEKTIF
   ├── Bagi tugas dengan jelas
   ├── Komunikasi rutin
   └── Review pekerjaan satu sama lain

8. BERLATIH PRESENTASI
   ├── Siapkan demo yang smooth
   ├── Antisipasi pertanyaan
   └── Setiap anggota harus bisa menjelaskan
```

---

## 14.7 Refleksi Akhir Semester

### 14.7.1 AI Literacy yang Telah Dicapai

Selama satu semester, mahasiswa telah menempuh perjalanan AI literacy dari level Basic hingga Expert:

| Level | Bab | Kemampuan yang Dicapai |
|-------|-----|----------------------|
| **Basic** | 1-4 | Memahami konsep dasar AI/ML, tipe data, dan preprocessing |
| **Intermediate** | 5-7 | Menerapkan supervised dan unsupervised learning |
| **Advanced** | 8-12 | Menganalisis model evaluasi, ensemble methods, neural networks, dan computer vision |
| **Expert** | 13-14 | Mengevaluasi AI-augmented development, MLOps, dan membangun proyek end-to-end |

### 14.7.2 Perjalanan Belajar ML

```
PERJALANAN BELAJAR ML — SEMESTER GENAP 2025/2026
=================================================

Bab 1-2:  "Apa itu AI dan ML?"
          Pengantar, Python untuk ML, statistika dasar

Bab 3-4:  "Data adalah bahan bakar ML"
          Preprocessing, EDA, feature engineering

Bab 5-6:  "Model pertama saya!"
          Regresi, klasifikasi, evaluasi

Bab 7-8:  "Belajar tanpa label"
          Clustering, dimensionality reduction

Bab 9-10: "Meningkatkan performa"
          Ensemble methods, tuning, feature selection

Bab 11-12: "Deep Learning dan Vision"
           Neural networks, CNN, computer vision

Bab 13:   "AI membantu saya coding"
          AI-augmented development, MLOps, Responsible AI

Bab 14:   "Saya bisa membangun ML pipeline!"
          Proyek akhir end-to-end
```

### 14.7.3 Next Steps setelah Mata Kuliah Ini

| Bidang | Langkah Selanjutnya | Resources |
|--------|-------------------|-----------|
| **Deep Learning** | Pelajari RNN, LSTM, Transformer, GPT | Coursera Deep Learning Specialization |
| **NLP** | Text processing, sentiment analysis, chatbot | Hugging Face Course, Stanford CS224N |
| **Computer Vision** | Object detection, segmentation, GANs | Stanford CS231N, fast.ai |
| **MLOps** | Docker, Kubernetes, CI/CD untuk ML | Made With ML, Full Stack Deep Learning |
| **Kaggle** | Ikuti kompetisi, bangun portofolio | kaggle.com/competitions |
| **Riset** | Baca paper, kontribusi open source | arXiv, Papers With Code |
| **Komunitas** | Bergabung komunitas AI Indonesia | Jakarta ML, Indonesia AI Society |

> **Pesan untuk mahasiswa:** Perjalanan belajar AI/ML tidak berakhir di mata kuliah ini. Ini baru **permulaan**. Teruslah belajar, bereksperimen, dan bangun proyek nyata. Ingatlah bahwa sebagai lulusan Informatika UAI, Anda memiliki tanggung jawab untuk menggunakan AI secara **bertanggung jawab, adil, dan bermanfaat** bagi masyarakat Indonesia. *Bismillah.*

---

## AI Corner — Level: Expert

### Refleksi: Bagaimana AI Membantu Perjalanan Belajar ML

| Aspek | Deskripsi |
|-------|-----------|
| **Level** | Expert — Refleksi menyeluruh tentang peran AI dalam pembelajaran |
| **Tools** | ChatGPT, Claude, GitHub Copilot, Kaggle Notebooks |
| **Fokus** | Refleksi perjalanan belajar, evaluasi dampak AI |

### Pertanyaan Reflektif

1. **Bagaimana AI membantu Anda memahami konsep ML yang sulit?**
   - Apakah penjelasan AI lebih mudah dipahami daripada textbook?
   - Apakah Anda pernah menemukan penjelasan AI yang salah?

2. **Apakah AI membuat Anda lebih produktif atau lebih malas?**
   - Berapa banyak kode yang benar-benar Anda tulis sendiri?
   - Apakah Anda memahami kode yang dihasilkan AI?

3. **Bagaimana Anda akan menggunakan AI di karier nanti?**
   - Apakah AI akan menggantikan Data Scientist?
   - Skill apa yang membuat Anda tetap relevan di era AI?

### Kebijakan Penggunaan AI — Proyek Akhir

| Aktivitas | Kebijakan |
|-----------|-----------|
| **Brainstorming tema** | AI BOLEH digunakan |
| **EDA dan kode** | AI BOLEH digunakan, WAJIB dipahami dan didokumentasikan |
| **Interpretasi hasil** | AI BOLEH membantu, tapi analisis final harus dari mahasiswa |
| **Penulisan laporan** | AI BOLEH membantu perbaikan bahasa, BUKAN menulis keseluruhan |
| **Presentasi** | Harus dilakukan sendiri, tidak boleh dibacakan dari AI |
| **AI Usage Log** | WAJIB ada, lengkap, dan jujur |

---

## Rangkuman Bab 14

1. **Proyek Akhir** adalah demonstrasi kemampuan komprehensif — mengintegrasikan seluruh materi Bab 1-13 dalam sebuah pipeline ML end-to-end.
2. **ML Pipeline** terdiri dari: problem definition, data collection, EDA, feature engineering, model selection, training, evaluation, dan conclusions.
3. **Kelompok 2-3 orang** dengan pembagian tugas yang jelas dan peer review.
4. **Timeline** proyek: Proposal (Minggu 10) → Progress 1 (Minggu 12) → Progress 2 (Minggu 14) → Final (Minggu 16).
5. **Deliverables**: Notebook Colab (bersih, reproducible), laporan proyek, dan presentasi.
6. **Rubrik** menilai 8 komponen: problem definition, data & EDA, feature engineering, modeling, evaluation, code quality, presentasi, dan AI Usage Log.
7. **Tema proyek** harus menggunakan **konteks Indonesia**: harga properti Jakarta, sentiment review produk, segmentasi pelanggan, data medis, atau klasifikasi makanan Indonesia.
8. **AI literacy** telah berkembang dari Basic ke Expert — perjalanan belajar ML tidak berakhir di sini, ini baru permulaan.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Sebutkan 6 tahapan utama dalam ML pipeline end-to-end.

**Soal 2.** Apa saja deliverables yang harus dikumpulkan dalam proyek akhir?

**Soal 3.** Jelaskan mengapa problem definition adalah langkah paling penting dalam proyek ML.

### Tingkat Menengah (C3-C4)

**Soal 4.** Anda memilih tema "Klasifikasi Sentiment Review Produk Indonesia". Buatlah:
- a) Definisi masalah yang lengkap menggunakan template di bab ini
- b) Daftar fitur (features) yang akan Anda gunakan
- c) Minimal 3 model yang akan Anda bandingkan
- d) Metrik evaluasi yang sesuai dan jelaskan mengapa

**Soal 5.** Rancang pembagian tugas untuk kelompok Anda (3 orang) dengan tema proyek "Prediksi Harga Properti Jakarta". Buat timeline mingguan yang realistis.

**Soal 6.** Tulis kode Python untuk melakukan perbandingan minimal 3 model machine learning pada dataset pilihan Anda, termasuk cross-validation dan visualisasi hasil.

### Tingkat Mahir (C5-C6)

**Soal 7.** Rancang proposal proyek akhir yang lengkap untuk salah satu tema di bagian 14.5. Proposal harus mencakup:
- a) Latar belakang dan motivasi
- b) Rumusan masalah dan tujuan
- c) Dataset yang akan digunakan (sumber, ukuran estimasi, fitur)
- d) Metodologi (preprocessing, model, evaluasi)
- e) Timeline pengerjaan
- f) Pembagian tugas tim
- g) Rencana penggunaan AI dan dokumentasinya

**Soal 8.** Refleksikan perjalanan belajar ML Anda selama satu semester:
- a) Konsep apa yang paling sulit dipahami? Bagaimana Anda mengatasinya?
- b) Bagaimana peran AI dalam membantu pembelajaran Anda?
- c) Skill apa yang paling berharga yang Anda dapatkan?
- d) Apa rencana Anda untuk terus belajar AI/ML setelah mata kuliah ini?

---

## Daftar Pustaka Bab 14

1. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
2. Muller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*. O'Reilly Media.
3. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media.
4. Huyen, C. (2022). *Designing Machine Learning Systems*. O'Reilly Media.
5. Kaggle. (2026). *Kaggle Competitions and Datasets*. Retrieved from https://www.kaggle.com
6. Google Developers. (2025). *Machine Learning Crash Course*. Retrieved from https://developers.google.com/machine-learning/crash-course
7. BPS. (2025). *Statistik Indonesia 2025*. Badan Pusat Statistik.
8. Kementerian Kominfo. (2020). *Strategi Nasional Kecerdasan Artifisial (STRANAS-AI) 2020-2045*.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
