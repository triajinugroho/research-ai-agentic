# RENCANA TUGAS MAHASISWA (RTM)

## Mata Kuliah: Kecerdasan Buatan dan Machine Learning

| Komponen | Detail |
|----------|--------|
| **Kode MK** | IF3XXX |
| **Nama MK** | Kecerdasan Buatan dan Machine Learning |
| **SKS** | 4 SKS (2 Teori + 2 Praktikum) |
| **Semester** | 5 (Ganjil 2026/2027) |
| **Program Studi** | Informatika |
| **Universitas** | Universitas Al Azhar Indonesia |
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |

---

## A. RINGKASAN KOMPONEN TUGAS

| No | Tugas | Minggu | Tipe | Bobot | CPMK |
|----|-------|--------|------|-------|------|
| T1 | Data Preprocessing Pipeline (NumPy, Pandas) | 2 | Individu | 2.5% | CPMK-2 |
| T2 | EDA & Feature Visualization pada Dataset Indonesia | 4 | Individu | 2.5% | CPMK-2, CPMK-3 |
| T3 | Regresi Linear & Logistik: Prediksi Data Riil | 5 | Individu | 2.5% | CPMK-3 |
| T4 | Perbandingan Model Supervised Learning | 7 | Individu | 2.5% | CPMK-4 |
| T5 | Clustering pada Dataset E-commerce Indonesia | 9 | Individu | 2.5% | CPMK-5 |
| T6 | Neural Network untuk Klasifikasi (Keras) | 11 | Individu | 2.5% | CPMK-6 |
| K1 | Kuis 1: Fondasi AI & Data Prep (Minggu 1-4) | 4 | Individu | 4% | CPMK 1-2 |
| K2 | Kuis 2: Supervised Learning (Minggu 5-7) | 7 | Individu | 3% | CPMK 3-4 |
| K3 | Kuis 3: Advanced ML (Minggu 9-12) | 12 | Individu | 3% | CPMK 5-6 |
| PF | Proyek Akhir: ML Pipeline End-to-End | 9-15 | Kelompok (2-3) | 25% | CPMK 1-7 |

### Ringkasan Bobot Penilaian

| Komponen | Bobot |
|----------|-------|
| Tugas Mingguan (T1-T6) | 15% |
| Kuis (K1-K3) | 10% |
| UTS (Minggu 8) | 20% |
| Proyek Akhir (Minggu 9-15) | 25% |
| UAS (Minggu 16) | 25% |
| Partisipasi & Etika AI | 5% |
| **TOTAL** | **100%** |

---

## B. DETAIL SETIAP TUGAS

---

### TUGAS 1: Data Preprocessing Pipeline (NumPy, Pandas)

**Minggu:** 2 | **Deadline:** Minggu 3 (sebelum kelas) | **Tipe:** Individu | **Bobot:** 2.5%

#### Deskripsi

Mahasiswa membangun pipeline preprocessing data lengkap menggunakan NumPy dan Pandas pada dataset Indonesia (sumber: BPS, Kaggle Indonesia, atau dataset terbuka lainnya). Pipeline mencakup data loading, cleaning, transformation, dan feature engineering dasar sebagai fondasi untuk proses machine learning.

#### CPMK yang Dinilai

- **CPMK-2:** Mampu melakukan preprocessing dan eksplorasi data menggunakan library Python untuk kebutuhan machine learning.

#### Petunjuk Pengerjaan

1. Pilih satu dataset dari daftar yang disediakan (minimal 500 baris, 8+ kolom)
2. Lakukan data loading dan inspeksi awal (shape, dtypes, info, describe)
3. Tangani missing values dengan minimal 2 strategi berbeda (mean/median imputation, forward fill, drop, dll.) dan berikan justifikasi pemilihan strategi
4. Deteksi dan tangani outlier menggunakan IQR method atau Z-score
5. Lakukan encoding untuk variabel kategorikal (Label Encoding atau One-Hot Encoding)
6. Lakukan feature scaling (StandardScaler atau MinMaxScaler) dan jelaskan kapan masing-masing digunakan
7. Simpan dataset yang sudah dipreprocess ke file CSV baru
8. Dokumentasikan setiap langkah dengan markdown cell yang menjelaskan keputusan yang diambil

#### Deliverables

1. **Jupyter Notebook (.ipynb)** berisi:
   - Import dan inspeksi dataset (head, info, shape, describe)
   - Handling missing values dengan justifikasi strategi
   - Outlier detection dan treatment
   - Encoding variabel kategorikal
   - Feature scaling
   - Summary statistik sebelum dan sesudah preprocessing
   - Interpretasi tertulis (dalam markdown cell) untuk setiap langkah
2. Upload ke LMS UAI

#### Rubrik Penilaian

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Kelengkapan pipeline** (30%) | Semua tahap preprocessing lengkap (missing values, outlier, encoding, scaling) dengan justifikasi | Sebagian besar tahap ada, 1-2 tahap kurang detail | Tahap dasar ada tapi tidak lengkap | Banyak tahap yang hilang atau salah |
| **Kode Python** (25%) | Kode bersih, efisien, well-commented, NumPy/Pandas idiomatik, modular | Kode berjalan dengan benar, beberapa comment | Kode berjalan tapi tidak efisien atau tanpa comment | Kode error atau tidak lengkap |
| **Interpretasi & justifikasi** (30%) | Setiap keputusan preprocessing dijustifikasi dengan alasan teknis, perbandingan before/after | Justifikasi ada tapi kurang mendalam | Justifikasi superfisial atau hanya mengulang langkah | Tidak ada justifikasi |
| **Presentasi notebook** (15%) | Notebook terstruktur rapi, markdown headings, flow logis, before/after comparison | Cukup terstruktur | Kurang terorganisir | Berantakan, sulit diikuti |

---

### TUGAS 2: EDA & Feature Visualization pada Dataset Indonesia

**Minggu:** 4 | **Deadline:** Minggu 5 (sebelum kelas) | **Tipe:** Individu | **Bobot:** 2.5%

#### Deskripsi

Mahasiswa melakukan Exploratory Data Analysis (EDA) komprehensif dan visualisasi fitur pada dataset Indonesia. Tujuan utama adalah memahami karakteristik data, menemukan pola dan korelasi, serta mengidentifikasi fitur yang potensial untuk pemodelan machine learning.

#### CPMK yang Dinilai

- **CPMK-2:** Mampu melakukan preprocessing dan eksplorasi data menggunakan library Python untuk kebutuhan machine learning.
- **CPMK-3:** Mampu menerapkan teknik supervised learning untuk klasifikasi dan regresi. *(persiapan feature selection)*

#### Petunjuk Pengerjaan

1. Gunakan dataset Indonesia (e-commerce, transportasi, kesehatan, atau pendidikan)
2. Lakukan analisis univariat: distribusi setiap fitur numerik (histogram, KDE) dan kategorikal (bar chart)
3. Lakukan analisis bivariat: scatter plot, korelasi Pearson/Spearman, cross-tabulation
4. Buat correlation heatmap dan identifikasi fitur yang berkorelasi tinggi
5. Lakukan analisis multivariat: pair plot untuk fitur-fitur terpilih
6. Identifikasi minimal 3 insight yang relevan untuk pemodelan ML
7. Buat rekomendasi fitur mana yang sebaiknya digunakan/di-drop dan mengapa

#### Deliverables

1. **Jupyter Notebook (.ipynb)** berisi:
   - Minimal 8 visualisasi berbeda (histogram, KDE, scatter, box, bar, heatmap, pair plot, violin/swarm)
   - Setiap visualisasi memiliki judul, label axis, legend (jika relevan)
   - Analisis korelasi dengan interpretasi
   - Narasi markdown yang menghubungkan setiap temuan
   - Rekomendasi feature selection untuk pemodelan ML
   - Minimal 3 temuan/insight yang tidak obvious dari data
2. Upload ke LMS UAI

#### Rubrik Penilaian

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Variasi & kesesuaian visualisasi** (25%) | 8+ chart berbeda dan sesuai, termasuk analisis uni/bi/multivariat | 5-7 chart, kebanyakan sesuai | 3-4 chart, beberapa kurang tepat | <3 chart atau banyak yang salah tipe |
| **Analisis korelasi & feature insight** (25%) | Korelasi dianalisis mendalam, feature importance diidentifikasi, rekomendasi ML jelas | Korelasi ada, beberapa rekomendasi | Korelasi dihitung tapi tidak diinterpretasi | Tidak ada analisis korelasi |
| **Storytelling & narasi** (30%) | Narasi mengalir logis dari EDA ke rekomendasi ML, insight mendalam, data-driven conclusion | Ada narasi tapi kurang mengalir | Narasi minim, hanya deskripsi chart | Tidak ada narasi |
| **Kode Python** (20%) | matplotlib/seaborn idiomatik, customized, fungsi reusable, well-documented | Kode benar, beberapa customization | Kode berjalan tapi minimal customization | Kode error |

---

### TUGAS 3: Regresi Linear & Logistik: Prediksi Data Riil

**Minggu:** 5 | **Deadline:** Minggu 6 (sebelum kelas) | **Tipe:** Individu | **Bobot:** 2.5%

#### Deskripsi

Mahasiswa membangun model regresi linear dan regresi logistik pada dataset Indonesia, melakukan evaluasi model, dan membandingkan performa keduanya pada konteks masalah yang berbeda. Tugas ini melatih kemampuan supervised learning dasar.

#### CPMK yang Dinilai

- **CPMK-3:** Mampu menerapkan teknik supervised learning untuk klasifikasi dan regresi.

#### Petunjuk Pengerjaan

1. **Bagian A — Regresi Linear:**
   - Pilih dataset regresi (misal: prediksi harga rumah Jakarta, harga komoditas Indonesia)
   - Lakukan train-test split (80:20)
   - Bangun model regresi linear menggunakan scikit-learn
   - Evaluasi: MAE, MSE, RMSE, R-squared
   - Visualisasi: actual vs predicted scatter plot, residual plot
2. **Bagian B — Regresi Logistik:**
   - Pilih dataset klasifikasi biner (misal: churn pelanggan, deteksi fraud)
   - Lakukan train-test split (80:20) dengan stratified sampling
   - Bangun model regresi logistik menggunakan scikit-learn
   - Evaluasi: accuracy, precision, recall, F1-score, confusion matrix
   - Visualisasi: confusion matrix heatmap, ROC curve
3. Bandingkan kedua model: kapan menggunakan regresi linear vs logistik

#### Deliverables

1. **Jupyter Notebook (.ipynb)** berisi:
   - Bagian A: Model regresi linear + evaluasi + visualisasi
   - Bagian B: Model regresi logistik + evaluasi + visualisasi
   - Perbandingan dan diskusi: perbedaan use case, metric evaluasi, interpretasi
   - Diskusi limitasi masing-masing model
2. Upload ke LMS UAI

#### Rubrik Penilaian

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Model regresi linear** (25%) | Model benar, semua metric evaluasi (MAE, MSE, RMSE, R²), residual analysis | Model benar, 2-3 metric | Model ada tapi evaluasi minim | Model salah atau error |
| **Model regresi logistik** (25%) | Model benar, confusion matrix, ROC, semua metric (accuracy, precision, recall, F1) | Model benar, 2-3 metric | Model ada tapi evaluasi minim | Model salah atau error |
| **Perbandingan & interpretasi** (30%) | Perbandingan mendalam, kontekstual, limitasi didiskusikan, saran perbaikan model | Perbandingan ada tapi kurang mendalam | Perbandingan superfisial | Tidak ada perbandingan |
| **Kode & presentasi** (20%) | scikit-learn idiomatik, well-documented, notebook terstruktur rapi | Kode berjalan, cukup terstruktur | Kode berjalan tapi berantakan | Kode error |

---

### TUGAS 4: Perbandingan Model Supervised Learning

**Minggu:** 7 | **Deadline:** Minggu 9 (sebelum kelas, melewati UTS) | **Tipe:** Individu | **Bobot:** 2.5%

#### Deskripsi

Mahasiswa membandingkan performa minimal 4 algoritma supervised learning pada satu dataset klasifikasi Indonesia. Tugas ini melatih kemampuan model selection, hyperparameter tuning dasar, dan evaluasi komprehensif.

#### CPMK yang Dinilai

- **CPMK-4:** Mampu membandingkan dan mengevaluasi berbagai algoritma machine learning menggunakan metrik yang tepat.

#### Petunjuk Pengerjaan

1. Pilih satu dataset klasifikasi Indonesia (minimal 1000 baris, 3+ kelas diperbolehkan)
2. Lakukan preprocessing dan train-test split (80:20, stratified)
3. Latih minimal 4 model: Logistic Regression, Decision Tree, Random Forest, dan SVM (atau KNN)
4. Untuk setiap model, lakukan:
   - Training dan prediksi
   - Evaluasi: accuracy, precision, recall, F1-score (weighted)
   - Confusion matrix
5. Buat tabel perbandingan performa semua model
6. Lakukan cross-validation (5-fold) untuk model terbaik
7. Diskusikan: model mana yang terbaik dan mengapa, trade-off bias-variance, waktu training

#### Deliverables

1. **Jupyter Notebook (.ipynb)** berisi:
   - Preprocessing lengkap
   - Training 4+ model dengan evaluasi masing-masing
   - Tabel perbandingan komprehensif
   - Cross-validation pada model terbaik
   - Visualisasi: bar chart perbandingan metric, confusion matrix per model
   - Diskusi pemilihan model terbaik dengan justifikasi
2. Upload ke LMS UAI

#### Rubrik Penilaian

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Implementasi model** (25%) | 4+ model diimplementasikan dengan benar, parameter didokumentasikan | 3-4 model benar | 2 model benar | <2 model atau banyak error |
| **Evaluasi & perbandingan** (30%) | Tabel perbandingan lengkap (accuracy, precision, recall, F1), cross-validation, analisis trade-off | Perbandingan ada, 2-3 metric | Perbandingan minimal | Tidak ada perbandingan |
| **Interpretasi & model selection** (25%) | Justifikasi pemilihan model mendalam, diskusi bias-variance, kontekstual | Pemilihan model dijustifikasi | Pemilihan model tanpa justifikasi kuat | Tidak ada diskusi |
| **Kode & visualisasi** (20%) | Kode modular, well-documented, visualisasi informatif dan rapi | Kode berjalan, visualisasi ada | Kode berjalan tapi kurang rapi | Kode error |

---

### TUGAS 5: Clustering pada Dataset E-commerce Indonesia

**Minggu:** 9 | **Deadline:** Minggu 10 (sebelum kelas) | **Tipe:** Individu | **Bobot:** 2.5%

#### Deskripsi

Mahasiswa menerapkan teknik unsupervised learning (clustering) pada dataset e-commerce atau retail Indonesia untuk melakukan customer segmentation. Tugas ini melatih kemampuan penerapan K-Means, evaluasi cluster, dan interpretasi bisnis dari hasil clustering.

#### CPMK yang Dinilai

- **CPMK-5:** Mampu menerapkan teknik unsupervised learning (clustering, dimensionality reduction) untuk menemukan pola dalam data.

#### Petunjuk Pengerjaan

1. Gunakan dataset e-commerce Indonesia (misal: data transaksi Tokopedia/Shopee style, dataset retail UCI yang dikontekstualisasikan)
2. Lakukan feature engineering: RFM (Recency, Frequency, Monetary) atau fitur relevan lainnya
3. Lakukan scaling pada fitur sebelum clustering
4. Terapkan K-Means clustering:
   - Tentukan jumlah cluster optimal menggunakan Elbow Method dan Silhouette Score
   - Visualisasikan Elbow plot dan Silhouette plot
5. Visualisasikan hasil cluster (2D menggunakan PCA jika fitur > 2)
6. Buat profil setiap cluster: karakteristik, ukuran, interpretasi bisnis
7. Bandingkan dengan 1 algoritma clustering lain (misal: DBSCAN atau Hierarchical Clustering)

#### Deliverables

1. **Jupyter Notebook (.ipynb)** berisi:
   - Feature engineering dan preprocessing
   - Penentuan jumlah cluster optimal (Elbow + Silhouette)
   - Implementasi K-Means + 1 algoritma lain
   - Visualisasi cluster (scatter plot 2D, centroid)
   - Profil cluster dengan interpretasi bisnis
   - Perbandingan 2 algoritma clustering
   - Rekomendasi aksi bisnis berdasarkan segmentasi
2. Upload ke LMS UAI

#### Rubrik Penilaian

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Feature engineering** (20%) | RFM atau fitur custom yang relevan, scaling benar, justifikasi lengkap | Fitur relevan, scaling ada | Fitur dasar, scaling ada | Tanpa feature engineering |
| **Penentuan k & clustering** (25%) | Elbow + Silhouette, K-Means + 1 algoritma lain, parameter didokumentasikan | Elbow method, K-Means benar | K-Means dengan k arbitrary | Clustering error |
| **Visualisasi cluster** (20%) | Scatter plot 2D (PCA), centroid ditandai, warna per cluster, informatif | Scatter plot ada, cukup jelas | Visualisasi minimal | Tidak ada visualisasi |
| **Profil & interpretasi bisnis** (25%) | Profil cluster detail, interpretasi bisnis kontekstual Indonesia, rekomendasi aksi | Profil ada, beberapa interpretasi | Profil singkat, tanpa konteks bisnis | Tidak ada profil |
| **Kualitas kode** (10%) | scikit-learn idiomatik, modular, well-documented | Kode berjalan, beberapa comment | Kode berjalan tapi berantakan | Kode error |

---

### TUGAS 6: Neural Network untuk Klasifikasi (Keras)

**Minggu:** 11 | **Deadline:** Minggu 12 (sebelum kelas) | **Tipe:** Individu | **Bobot:** 2.5%

#### Deskripsi

Mahasiswa membangun model neural network sederhana menggunakan Keras/TensorFlow untuk tugas klasifikasi. Tugas ini melatih kemampuan dasar deep learning: arsitektur network, training, evaluasi, dan analisis performa.

#### CPMK yang Dinilai

- **CPMK-6:** Mampu membangun dan melatih model neural network sederhana menggunakan framework deep learning.

#### Petunjuk Pengerjaan

1. Pilih dataset klasifikasi (misal: MNIST, Fashion-MNIST, atau dataset tabular Indonesia)
2. Lakukan preprocessing: normalisasi, one-hot encoding label (jika multiclass)
3. Bangun model Sequential di Keras:
   - Minimal 3 layer (input, 1+ hidden, output)
   - Eksperimen dengan jumlah neuron, activation function (ReLU, sigmoid, softmax)
   - Gunakan Dropout untuk regularisasi
4. Compile model: optimizer (Adam), loss function (categorical_crossentropy / binary_crossentropy), metrics
5. Training: minimal 20 epoch, gunakan validation_split
6. Visualisasi training history: loss curve dan accuracy curve (train vs validation)
7. Evaluasi pada test set: classification report, confusion matrix
8. Eksperimen: bandingkan 2 arsitektur berbeda (misal: beda jumlah layer atau neuron)

#### Deliverables

1. **Jupyter Notebook (.ipynb)** berisi:
   - Preprocessing data untuk neural network
   - Arsitektur model (model.summary())
   - Training dengan history
   - Visualisasi loss/accuracy curve
   - Evaluasi: classification report + confusion matrix
   - Perbandingan 2 arsitektur dengan diskusi
   - Analisis: overfitting/underfitting, efek Dropout, pemilihan hyperparameter
2. Upload ke LMS UAI

#### Rubrik Penilaian

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Arsitektur model** (25%) | Model 3+ layer, Dropout, activation function tepat, arsitektur didokumentasikan | Model benar, 2-3 layer | Model 1-2 layer tanpa regularisasi | Model error atau arsitektur salah |
| **Training & visualisasi** (25%) | Training dengan validation, loss/accuracy curve, analisis konvergensi | Training berhasil, curve ada | Training berjalan tapi tanpa visualisasi | Training error |
| **Evaluasi** (20%) | Classification report + confusion matrix + analisis per-class performance | Classification report ada | Hanya accuracy | Tidak ada evaluasi |
| **Eksperimen arsitektur** (20%) | 2+ arsitektur dibandingkan, diskusi trade-off, pemilihan terbaik dijustifikasi | 2 arsitektur dibandingkan | 1 arsitektur saja | Tidak ada eksperimen |
| **Kualitas kode** (10%) | Keras idiomatik, well-documented, reproducible (seed) | Kode berjalan, beberapa comment | Kode berjalan tapi berantakan | Kode error |

---

## C. DETAIL KUIS

---

### KUIS 1: Fondasi AI & Data Prep (Minggu 1-4)

| Komponen | Detail |
|----------|--------|
| **Waktu** | Minggu 4, 30 menit pertama pertemuan |
| **Cakupan** | Pengantar AI & ML, sejarah AI, tipe-tipe learning, data preprocessing, EDA, feature engineering |
| **Durasi** | 30 menit |
| **Format** | Closed-book, kertas, tanpa AI |
| **Jumlah Soal** | 10 PG + 3 soal singkat |
| **Tipe Soal** | Pilihan ganda: definisi, konsep, perbedaan; Soal singkat: langkah preprocessing, identifikasi tipe learning |
| **Bobot** | 4% |
| **Contoh soal PG** | "Manakah yang termasuk supervised learning? (a) K-Means clustering (b) Linear regression (c) PCA (d) Autoencoder" |
| **Contoh soal singkat** | "Jelaskan perbedaan antara feature scaling menggunakan StandardScaler dan MinMaxScaler. Kapan masing-masing lebih tepat digunakan?" |

---

### KUIS 2: Supervised Learning (Minggu 5-7)

| Komponen | Detail |
|----------|--------|
| **Waktu** | Minggu 7, 30 menit terakhir pertemuan |
| **Cakupan** | Regresi linear & logistik, Decision Tree, Random Forest, SVM, KNN, evaluasi model, overfitting/underfitting |
| **Durasi** | 30 menit |
| **Format** | Closed-book, kertas, tanpa AI |
| **Jumlah Soal** | 8 PG + 2 soal interpretasi output + 1 soal essay pendek |
| **Tipe Soal** | PG: konsep algoritma, pemilihan model; Interpretasi: baca confusion matrix / classification report; Essay: diskusi trade-off |
| **Bobot** | 3% |
| **Contoh soal PG** | "Pada confusion matrix, precision dihitung sebagai: (a) TP/(TP+FP) (b) TP/(TP+FN) (c) (TP+TN)/Total (d) TP/Total" |
| **Contoh soal interpretasi** | "Diberikan confusion matrix berikut: [[85, 15], [10, 90]]. Hitung accuracy, precision, dan recall untuk kelas positif." |

---

### KUIS 3: Advanced ML (Minggu 9-12)

| Komponen | Detail |
|----------|--------|
| **Waktu** | Minggu 12, 30 menit pertama pertemuan |
| **Cakupan** | Clustering (K-Means, DBSCAN), dimensionality reduction (PCA), neural network dasar, ensemble methods, model evaluation lanjut |
| **Durasi** | 30 menit |
| **Format** | Closed-book, kertas, tanpa AI |
| **Jumlah Soal** | 8 PG + 2 soal interpretasi output + 1 soal essay pendek |
| **Tipe Soal** | PG: konsep clustering, neural network; Interpretasi: analisis Elbow plot, arsitektur NN; Essay: perbandingan metode |
| **Bobot** | 3% |
| **Contoh soal PG** | "Pada K-Means clustering, Elbow Method digunakan untuk: (a) Memilih fitur terbaik (b) Menentukan jumlah cluster optimal (c) Menghitung jarak antar data (d) Mengurangi dimensi data" |
| **Contoh soal interpretasi** | "Diberikan Elbow plot dan Silhouette Score untuk k=2 hingga k=8. Tentukan jumlah cluster optimal dan berikan justifikasi." |

---

## D. DETAIL UTS (Ujian Tengah Semester)

| Komponen | Detail |
|----------|--------|
| **Waktu** | Minggu 8 |
| **Durasi** | 90 menit |
| **Format** | Closed-book, kertas, tanpa AI, tanpa catatan |
| **Bobot** | 20% |
| **Cakupan** | Minggu 1-7: Pengantar AI & ML, data preprocessing, EDA, supervised learning (regresi, klasifikasi, Decision Tree, Random Forest, SVM, KNN), evaluasi model |
| **CPMK** | CPMK 1-4 |

### Struktur Soal UTS

| Bagian | Tipe | Jumlah | Bobot |
|--------|------|--------|-------|
| A | Pilihan Ganda | 15 soal | 30% |
| B | Soal Singkat / Isian | 5 soal | 20% |
| C | Interpretasi Output | 3 soal | 25% |
| D | Essay / Analisis | 2 soal | 25% |

### Contoh Distribusi Topik UTS

| Topik | Persentase |
|-------|------------|
| Konsep dasar AI, ML, tipe learning | 15% |
| Data preprocessing & feature engineering | 15% |
| EDA & visualisasi | 10% |
| Regresi linear & logistik | 20% |
| Decision Tree, Random Forest, SVM, KNN | 25% |
| Evaluasi model (metric, overfitting, cross-validation) | 15% |

---

## E. DETAIL UAS (Ujian Akhir Semester)

| Komponen | Detail |
|----------|--------|
| **Waktu** | Minggu 16 |
| **Durasi** | 120 menit |
| **Format** | Closed-book, kertas, tanpa AI, 1 lembar catatan A4 (bolak-balik, tulis tangan) |
| **Bobot** | 25% |
| **Cakupan** | Komprehensif Minggu 1-15 (penekanan pada Minggu 9-15: unsupervised learning, neural network, ensemble, deployment, etika AI) |
| **CPMK** | CPMK 1-7 |

### Struktur Soal UAS

| Bagian | Tipe | Jumlah | Bobot |
|--------|------|--------|-------|
| A | Pilihan Ganda | 20 soal | 30% |
| B | Soal Singkat / Isian | 5 soal | 15% |
| C | Interpretasi Output & Diagram | 3 soal | 20% |
| D | Essay / Analisis Kasus | 2 soal | 20% |
| E | Desain Solusi ML | 1 soal | 15% |

### Contoh Distribusi Topik UAS

| Topik | Persentase |
|-------|------------|
| Fondasi AI & preprocessing (review) | 10% |
| Supervised learning (review) | 15% |
| Unsupervised learning (clustering, PCA) | 20% |
| Neural network & deep learning dasar | 20% |
| Ensemble methods & model optimization | 15% |
| ML pipeline, deployment, & etika AI | 20% |

### Catatan Lembar Contekan (Cheat Sheet)

- Mahasiswa **boleh** membawa 1 lembar A4 bolak-balik
- **Harus** ditulis tangan sendiri (bukan print/fotokopi)
- Dikumpulkan bersama lembar jawaban setelah ujian
- Isi disarankan: rumus, arsitektur model, metric evaluasi, langkah pipeline ML

---

## F. DETAIL PROYEK AKHIR

### Deskripsi

Proyek akhir adalah implementasi **ML pipeline end-to-end** secara berkelompok (2-3 orang) pada permasalahan riil Indonesia. Proyek mencakup seluruh tahapan: problem definition, data collection/preparation, EDA, modeling, evaluation, dan presentasi hasil. Proyek ini menguji kemampuan mahasiswa mengintegrasikan seluruh pengetahuan yang dipelajari selama semester.

### CPMK yang Dinilai

- **CPMK 1-7** (semua CPMK diuji secara terintegrasi)

### Milestones Proyek

| Milestone | Minggu | Deliverable | Bobot dari Proyek |
|-----------|--------|-------------|-------------------|
| **Proposal** | 9 | Dokumen proposal: dataset, problem statement, rencana model, pembagian tugas | 10% |
| **Progress 1** | 11 | Notebook: EDA lengkap + baseline model (minimal 1 algoritma) | 20% |
| **Progress 2** | 13 | Notebook: model optimization + evaluasi komprehensif (minimal 3 algoritma) | 25% |
| **Final** | 15 | Presentasi final + laporan PDF + notebook lengkap | 45% |

### Topik Proyek yang Disarankan

1. **Prediksi Harga Properti Jakarta** — regresi pada data properti Indonesia
2. **Klasifikasi Sentimen Review Produk** — NLP dasar pada review e-commerce Indonesia (Tokopedia/Shopee)
3. **Customer Segmentation E-commerce** — clustering pelanggan berdasarkan perilaku belanja
4. **Deteksi Fraud Transaksi** — klasifikasi anomali pada data transaksi keuangan
5. **Prediksi Kualitas Udara Jakarta** — time series / regresi berdasarkan data BMKG/ISPU
6. **Klasifikasi Gambar Batik** — CNN sederhana untuk klasifikasi motif batik Nusantara
7. **Prediksi Kelulusan Mahasiswa** — klasifikasi berdasarkan data akademik
8. **Analisis Pola Transportasi** — clustering pola perjalanan TransJakarta/KRL

### Deliverables Final (Minggu 15)

1. **Jupyter Notebook (.ipynb)** — kode lengkap, semua cell sudah dijalankan
2. **Laporan PDF** (8-12 halaman) berisi:
   - Latar belakang & problem statement
   - Deskripsi dataset & preprocessing
   - Metodologi: algoritma yang dipilih dan justifikasinya
   - Hasil & evaluasi: metric, visualisasi, perbandingan model
   - Diskusi, limitasi, dan saran pengembangan
   - Pembagian kontribusi anggota
   - Dokumentasi penggunaan AI
3. **Slide presentasi** (10-15 slide, durasi presentasi 15 menit + 5 menit Q&A)

### Rubrik Proyek Akhir

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Problem definition & dataset** (10%) | Problem relevan Indonesia, dataset berkualitas, well-defined scope | Problem jelas, dataset memadai | Problem kurang fokus, dataset minim | Problem tidak jelas, dataset tidak relevan |
| **Data preprocessing & EDA** (15%) | Preprocessing komprehensif, EDA mendalam dengan insight bermakna | Preprocessing lengkap, EDA ada | Preprocessing dasar, EDA minim | Preprocessing tidak ada, EDA tidak ada |
| **Modeling** (25%) | 3+ model dibandingkan, hyperparameter tuning, cross-validation, pipeline terstruktur | 2-3 model, beberapa tuning | 1 model tanpa tuning | Model error atau tidak berjalan |
| **Evaluasi & interpretasi** (20%) | Metric komprehensif, visualisasi performa, interpretasi kontekstual, limitasi didiskusikan | Metric standar, interpretasi ada | Metric minimal, interpretasi kurang | Tidak ada evaluasi |
| **Laporan & presentasi** (15%) | Laporan terstruktur seperti paper, presentasi engaging, Q&A dijawab dengan baik | Laporan cukup, presentasi jelas | Laporan ada tapi kurang terstruktur | Laporan tidak ada atau sangat kurang |
| **Kode & reproducibility** (10%) | Notebook bersih, modular, reproducible, well-documented, versi library dicantumkan | Notebook berjalan, beberapa comment | Notebook berjalan tapi berantakan | Notebook error |
| **Kerja tim & dokumentasi AI** (5%) | Pembagian tugas jelas dan merata, AI usage log lengkap dan reflektif | Pembagian cukup jelas, AI log ada | Pembagian tidak jelas, AI log minim | Tidak ada pembagian tugas, AI log tidak ada |

---

## G. KEBIJAKAN PENGGUNAAN AI

### Tabel Kebijakan AI per Komponen Penilaian

| Komponen | AI Diizinkan? | Ketentuan |
|----------|---------------|-----------|
| **Tugas (T1-T6)** | YA — AI diizinkan sebagai partner | AI Usage Log **wajib** dilampirkan di akhir notebook. Mahasiswa harus mendokumentasikan prompt, output, dan modifikasi yang dilakukan. Kode hasil AI harus dipahami dan dimodifikasi. |
| **Kuis (K1-K3)** | **TIDAK** — Closed-book | Dikerjakan di kertas tanpa akses perangkat elektronik apapun. |
| **UTS** | **TIDAK** — Closed-book | Dikerjakan di kertas tanpa akses perangkat elektronik apapun. Tanpa catatan. |
| **UAS** | **TIDAK** — Closed-book | Dikerjakan di kertas. 1 lembar catatan A4 tulis tangan diperbolehkan. Tanpa perangkat elektronik. |
| **Proyek Akhir** | YA — AI sebagai partner | AI Usage Log **wajib** per milestone. AI boleh digunakan untuk brainstorming, debugging, code review, dan penjelasan konsep. Semua kontribusi AI harus didokumentasikan secara transparan. |

### Prinsip Penggunaan AI

1. **Amanah (Trustworthiness):** Penggunaan AI harus jujur dan transparan. Menyembunyikan penggunaan AI = pelanggaran integritas akademik.
2. **AI sebagai Partner, Bukan Pengganti:** AI membantu memahami konsep dan debugging, bukan mengerjakan tugas sepenuhnya.
3. **Understanding First:** Mahasiswa harus mampu menjelaskan setiap baris kode yang disubmit, termasuk yang dibantu AI.
4. **Progression:** Ketergantungan pada AI harus menurun seiring semester berjalan — mahasiswa harus semakin mandiri.

### Sanksi Pelanggaran

- **Pelanggaran ringan** (AI log tidak lengkap): pengurangan 10% nilai tugas
- **Pelanggaran sedang** (tidak mencantumkan AI log padahal menggunakan AI): nilai tugas = 0
- **Pelanggaran berat** (copy-paste output AI tanpa pemahaman, terdeteksi saat responsi): nilai komponen = 0 + peringatan akademik

---

## H. PANDUAN SUBMISSION

### H.1 Format File

- **Tugas:** Jupyter Notebook (.ipynb) — pastikan semua cell sudah dijalankan (output terlihat)
- **Penamaan file:** `T[nomor]_[NIM]_[NamaDepan].ipynb` (contoh: `T1_2026001_Ahmad.ipynb`)
- **Kuis:** Dikerjakan di kertas saat perkuliahan
- **Proyek akhir:** Notebook + Laporan PDF + Slide presentasi

### H.2 Platform Submission

1. **Upload ke LMS UAI** (elearning.uai.ac.id) — **wajib** untuk semua tugas
2. **Push ke GitHub** — **disarankan** untuk membangun portfolio ML (repository pribadi mahasiswa)
3. **Google Colab sharing link** — sebagai backup jika LMS bermasalah

### H.3 Keterlambatan

- Terlambat 1 hari: pengurangan 10%
- Terlambat 2-3 hari: pengurangan 25%
- Terlambat >3 hari: tidak diterima (nilai 0), kecuali ada izin tertulis dari dosen sebelum deadline

### H.4 AI Usage Documentation

Untuk setiap tugas yang menggunakan AI, tambahkan section di akhir notebook:

```markdown
## Dokumentasi Penggunaan AI

### AI Tool yang Digunakan
- [Nama tool, misal: Claude, ChatGPT, GitHub Copilot]

### Prompt yang Digunakan
1. [Copy-paste prompt yang digunakan]
2. [...]

### Output AI yang Dimanfaatkan
- [Deskripsi singkat bagian mana yang menggunakan bantuan AI]

### Modifikasi yang Dilakukan
- [Apa yang diubah dari output AI dan mengapa]

### Refleksi
- [Apa yang dipelajari dari interaksi dengan AI?]
- [Apakah AI membantu pemahaman atau justru menyesatkan?]
- [Bagaimana Anda memvalidasi output AI?]
```

---

## I. JADWAL KOMPONEN PENILAIAN

```
Minggu 1  ─── Perkenalan, setup environment, pengantar AI & ML
Minggu 2  ─── Data Preprocessing → TUGAS 1 (due Minggu 3)
Minggu 3  ─── EDA & Feature Engineering
Minggu 4  ─── KUIS 1 + Feature Visualization → TUGAS 2 (due Minggu 5)
Minggu 5  ─── Regresi Linear & Logistik → TUGAS 3 (due Minggu 6)
Minggu 6  ─── Decision Tree & Random Forest
Minggu 7  ─── SVM & KNN + KUIS 2 → TUGAS 4 (due Minggu 9)
Minggu 8  ─── ════════ UTS ════════
Minggu 9  ─── Clustering → TUGAS 5 (due Minggu 10) + [PROYEK: Proposal due]
Minggu 10 ─── Dimensionality Reduction (PCA) + [PROYEK: EDA mulai]
Minggu 11 ─── Neural Network Dasar → TUGAS 6 (due Minggu 12) + [PROYEK: Progress 1 due]
Minggu 12 ─── KUIS 3 + Ensemble Methods + [PROYEK: Model optimization]
Minggu 13 ─── Model Deployment & Pipeline + [PROYEK: Progress 2 due]
Minggu 14 ─── Etika AI & Responsible ML + [PROYEK: Finalisasi]
Minggu 15 ─── PRESENTASI PROYEK AKHIR
Minggu 16 ─── ════════ UAS ════════
```

### Ringkasan Jadwal dalam Tabel

| Minggu | Komponen Penilaian | Keterangan |
|--------|-------------------|------------|
| 1 | — | Setup & perkenalan |
| 2 | T1 diberikan | Data Preprocessing Pipeline |
| 3 | **T1 due** | Deadline Tugas 1 |
| 4 | **K1** + T2 diberikan | Kuis 1 (Fondasi AI & Data Prep) |
| 5 | **T2 due** + T3 diberikan | Deadline Tugas 2; Regresi |
| 6 | **T3 due** | Deadline Tugas 3 |
| 7 | **K2** + T4 diberikan | Kuis 2 (Supervised Learning) |
| 8 | **UTS** | Ujian Tengah Semester |
| 9 | **T4 due** + T5 diberikan + **Proyek: Proposal** | Deadline Tugas 4; Clustering; Proposal proyek due |
| 10 | **T5 due** | Deadline Tugas 5 |
| 11 | T6 diberikan + **Proyek: Progress 1** | Neural Network; Progress 1 proyek due |
| 12 | **T6 due** + **K3** | Deadline Tugas 6; Kuis 3 (Advanced ML) |
| 13 | **Proyek: Progress 2** | Progress 2 proyek due |
| 14 | — | Etika AI; Finalisasi proyek |
| 15 | **Proyek: Presentasi Final** | Presentasi + laporan + notebook |
| 16 | **UAS** | Ujian Akhir Semester |

---

*Dokumen RTM ini merupakan bagian dari RPS mata kuliah Kecerdasan Buatan dan Machine Learning, Prodi Informatika, Universitas Al Azhar Indonesia.*

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
