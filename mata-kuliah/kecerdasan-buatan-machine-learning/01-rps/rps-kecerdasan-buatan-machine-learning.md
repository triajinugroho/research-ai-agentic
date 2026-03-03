# RENCANA PEMBELAJARAN SEMESTER (RPS)

## UNIVERSITAS AL AZHAR INDONESIA
### Fakultas Sains dan Teknologi — Program Studi Informatika

---

## A. IDENTITAS MATA KULIAH

| Komponen | Detail |
|----------|--------|
| **Nama Mata Kuliah** | Kecerdasan Buatan dan Machine Learning |
| **Kode Mata Kuliah** | IF3XXX |
| **Bobot SKS** | 4 SKS (2 SKS Teori + 2 SKS Praktikum) |
| **Semester** | 5 (Ganjil) |
| **Tahun Akademik** | 2026/2027 |
| **Prasyarat** | Algoritma dan Pemrograman (INF-101), Analisis Data Statistik |
| **Ko-requisite** | — (tidak ada) |
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Waktu Pertemuan** | 2x per minggu @ 100 menit (Teori + Praktikum) |
| **Platform** | LMS UAI (utama), Google Colab (coding), GitHub (portfolio) |

---

## B. DESKRIPSI MATA KULIAH

Mata kuliah Kecerdasan Buatan dan Machine Learning memberikan pengetahuan dan keterampilan dalam membangun sistem cerdas berbasis data menggunakan teknik-teknik machine learning modern. Mahasiswa akan mempelajari fondasi kecerdasan buatan, persiapan dan rekayasa fitur data, algoritma supervised dan unsupervised learning, neural network dan deep learning, serta aplikasi AI pada Natural Language Processing (NLP) dan Computer Vision — semuanya diimplementasikan menggunakan Python dengan library scikit-learn, TensorFlow/Keras, dan tools AI sebagai co-developer.

Mata kuliah ini dirancang dengan pendekatan **AI-augmented machine learning education** — mahasiswa tidak hanya menguasai teori dan implementasi algoritma, tetapi juga mampu berkolaborasi dengan AI (ChatGPT, Claude, Copilot) untuk merancang, membangun, mengevaluasi, dan men-deploy pipeline ML secara end-to-end dengan penuh tanggung jawab dan etika.

Sebagai mata kuliah lanjutan, Kecerdasan Buatan dan Machine Learning membangun di atas fondasi yang telah diletakkan oleh Algoritma dan Pemrograman (INF-101) — yang memberikan kemampuan pemrograman Python, computational thinking, dan penyelesaian masalah secara algoritmik — serta Analisis Data Statistik — yang memberikan pemahaman statistika deskriptif, inferensi, probabilitas, regresi, dan eksplorasi data. Dengan prasyarat ini, mahasiswa memasuki mata kuliah dengan kemampuan coding dan analisis data yang memadai untuk langsung fokus pada konsep dan implementasi AI/ML.

Pendekatan pembelajaran menggunakan **Problem-Based Learning (PBL)** dan **Project-Based Learning (PjBL)**, di mana setiap topik diperkenalkan melalui masalah nyata dalam konteks Indonesia — mulai dari analisis sentimen media sosial berbahasa Indonesia, prediksi harga properti di DKI Jakarta, klasifikasi citra produk UMKM, hingga clustering profil konsumen e-commerce lokal. Proyek akhir mengharuskan mahasiswa merancang pipeline ML end-to-end yang menyelesaikan masalah riil, menggunakan AI sebagai co-developer, dan mendokumentasikan seluruh proses secara transparan.

---

## C. CAPAIAN PEMBELAJARAN LULUSAN (CPL) YANG DIBEBANKAN

| Kode | Ranah | Deskripsi CPL |
|------|-------|---------------|
| **CPL-S2** | Sikap | Menunjukkan sikap bertanggung jawab atas pekerjaan di bidang keahliannya secara mandiri, berdasarkan nilai-nilai Islami, termasuk etika dalam pengembangan dan penggunaan AI |
| **CPL-KU2** | Keterampilan Umum | Mampu menunjukkan kinerja mandiri, bermutu, dan terukur dalam membangun sistem berbasis kecerdasan buatan |
| **CPL-KK1** | Keterampilan Khusus | Mampu menerapkan pemikiran logis, kritis, sistematis, dan inovatif dalam konteks pengembangan atau implementasi ilmu pengetahuan dan teknologi |
| **CPL-KK4** | Keterampilan Khusus | Mampu membangun sistem cerdas (intelligent systems) menggunakan teknik machine learning untuk menyelesaikan masalah di berbagai domain |
| **CPL-P2** | Pengetahuan | Menguasai konsep dasar ilmu komputer termasuk kecerdasan buatan, machine learning, dan algoritma |
| **CPL-P3** | Pengetahuan | Menguasai prinsip dasar data science, machine learning, dan kecerdasan buatan serta mampu menerapkannya pada data riil |

---

## D. CAPAIAN PEMBELAJARAN MATA KULIAH (CPMK)

| Kode | CPMK | CPL yang Didukung | Bloom's Taxonomy |
|------|------|-------------------|------------------|
| **CPMK-1** | Menjelaskan konsep dasar AI, sejarah perkembangan AI, jenis-jenis AI, serta prinsip etika AI berdasarkan nilai-nilai Islami | CPL-S2, CPL-P2 | C2 (Understand) |
| **CPMK-2** | Menerapkan teknik persiapan data, preprocessing, dan feature engineering untuk membangun dataset yang siap digunakan dalam pemodelan ML | CPL-KK1, CPL-P2 | C3 (Apply) |
| **CPMK-3** | Menganalisis dan menerapkan algoritma supervised learning (regresi dan klasifikasi) serta mengevaluasi performa model secara kuantitatif | CPL-KK1, CPL-KK4 | C4 (Analyze) |
| **CPMK-4** | Menganalisis data menggunakan teknik unsupervised learning (clustering dan reduksi dimensi) untuk menemukan pola tersembunyi dalam data | CPL-KK4, CPL-P3 | C4 (Analyze) |
| **CPMK-5** | Menerapkan arsitektur neural network dan deep learning dasar untuk menyelesaikan masalah klasifikasi dan regresi | CPL-KK4, CPL-P3 | C3 (Apply) |
| **CPMK-6** | Menerapkan teknik NLP dan Computer Vision dasar untuk memproses data teks dan citra menggunakan pendekatan machine learning dan deep learning | CPL-KK4, CPL-P3 | C3-C4 (Apply-Analyze) |
| **CPMK-7** | Merancang dan membangun proyek ML end-to-end dengan memanfaatkan AI sebagai co-developer secara bertanggung jawab, termasuk konsep dasar MLOps | CPL-KU2, CPL-KK4, CPL-P3 | C5-C6 (Evaluate-Create) |

---

## E. SUB-CPMK (PER MINGGU)

| Minggu | Sub-CPMK | CPMK | Bloom's |
|--------|----------|------|---------|
| 1 | Sub-CPMK 1.1: Menjelaskan definisi AI, sejarah perkembangan AI (Turing Test, AI Winter, AI Summer), dan klasifikasi AI (narrow, general, super) | CPMK-1 | C2 |
| 1 | Sub-CPMK 1.2: Mengidentifikasi aplikasi AI di berbagai bidang, khususnya konteks Indonesia | CPMK-1 | C1-C2 |
| 1 | Sub-CPMK 1.3: Menjelaskan prinsip etika AI dan responsible AI berdasarkan nilai-nilai Islami | CPMK-1 | C2 |
| 2 | Sub-CPMK 2.1: Menerapkan NumPy dan Pandas untuk manipulasi data dalam konteks machine learning | CPMK-2 | C3 |
| 2 | Sub-CPMK 2.2: Melakukan data preprocessing: penanganan missing values, encoding kategorikal, dan scaling fitur | CPMK-2 | C3 |
| 3 | Sub-CPMK 3.1: Menghitung operasi linear algebra dasar (vektor, matriks, dot product) dengan NumPy | CPMK-2 | C3 |
| 3 | Sub-CPMK 3.2: Menerapkan konsep probabilitas dan statistik yang relevan untuk ML (distribusi, Bayes, entropy) | CPMK-2 | C3 |
| 4 | Sub-CPMK 4.1: Melakukan Exploratory Data Analysis (EDA) pada dataset ML menggunakan visualisasi dan statistik | CPMK-2 | C3-C4 |
| 4 | Sub-CPMK 4.2: Menerapkan teknik feature engineering (encoding, scaling, feature creation) untuk meningkatkan kualitas data | CPMK-2 | C3 |
| 5 | Sub-CPMK 5.1: Membangun model regresi linear dan mengevaluasi performanya (MSE, RMSE, R²) | CPMK-3 | C3-C4 |
| 5 | Sub-CPMK 5.2: Membangun model regresi logistik untuk klasifikasi biner dan menginterpretasi hasilnya | CPMK-3 | C3-C4 |
| 6 | Sub-CPMK 6.1: Membangun Decision Tree dan menginterpretasi struktur pohon keputusan | CPMK-3 | C4 |
| 6 | Sub-CPMK 6.2: Menerapkan Random Forest sebagai ensemble method dan membandingkan dengan Decision Tree tunggal | CPMK-3 | C4 |
| 7 | Sub-CPMK 7.1: Membangun model SVM dan memahami konsep hyperplane, margin, dan kernel trick | CPMK-3 | C4 |
| 7 | Sub-CPMK 7.2: Membangun model KNN dan menganalisis pengaruh parameter K terhadap performa model | CPMK-3 | C4 |
| 8 | **UJIAN TENGAH SEMESTER (UTS)** — Cakupan: Minggu 1-7 | CPMK 1-3 | C2-C4 |
| 9 | Sub-CPMK 9.1: Menerapkan algoritma K-Means clustering dan memilih jumlah cluster optimal (Elbow, Silhouette) | CPMK-4 | C3-C4 |
| 9 | Sub-CPMK 9.2: Menerapkan hierarchical clustering dan menginterpretasi dendrogram | CPMK-4 | C4 |
| 10 | Sub-CPMK 10.1: Menerapkan PCA (Principal Component Analysis) untuk reduksi dimensi dan memvisualisasikan hasilnya | CPMK-4 | C4 |
| 10 | Sub-CPMK 10.2: Melakukan feature selection dan feature extraction untuk optimasi model | CPMK-4 | C4 |
| 11 | Sub-CPMK 11.1: Membangun neural network sederhana (MLP) dengan TensorFlow/Keras | CPMK-5 | C3 |
| 11 | Sub-CPMK 11.2: Menjelaskan mekanisme backpropagation, activation functions, dan optimizer dalam neural network | CPMK-5 | C2-C3 |
| 12 | Sub-CPMK 12.1: Menerapkan text preprocessing untuk teks bahasa Indonesia (tokenisasi, stopword removal, stemming) | CPMK-6 | C3 |
| 12 | Sub-CPMK 12.2: Membangun model klasifikasi teks menggunakan pipeline TF-IDF + classifier | CPMK-6 | C3-C4 |
| 13 | Sub-CPMK 13.1: Menerapkan teknik dasar image processing dengan OpenCV (resize, grayscale, augmentation) | CPMK-6 | C3 |
| 13 | Sub-CPMK 13.2: Membangun model image classification dengan Convolutional Neural Network (CNN) | CPMK-6 | C3-C4 |
| 14 | Sub-CPMK 14.1: Menggunakan AI (ChatGPT, Claude, Copilot) sebagai co-developer dalam pipeline ML | CPMK-7 | C5-C6 |
| 14 | Sub-CPMK 14.2: Menjelaskan konsep dasar MLOps (versioning, experiment tracking, deployment) | CPMK-7 | C2-C3 |
| 15 | Sub-CPMK 15.1: Mempresentasikan proyek akhir ML end-to-end dengan demonstrasi model dan analisis hasil | CPMK 1-7 | C6 |
| 16 | **UJIAN AKHIR SEMESTER (UAS)** — Cakupan komprehensif Minggu 1-15 | CPMK 1-7 | C4-C6 |

---

## F. TABEL RENCANA PEMBELAJARAN SEMESTER

---

### FASE 1: FONDASI AI — "Understand Intelligence" (Minggu 1-4)

---

### Minggu 1: Pengantar Kecerdasan Buatan dan Etika AI

| Komponen | Detail |
|----------|--------|
| **Sub-CPMK** | 1.1, 1.2, 1.3 |
| **Materi Pembelajaran** | (1) Definisi kecerdasan buatan: apa itu AI dan apa bukan AI; (2) Sejarah AI: dari Turing Test (1950) hingga era modern — AI Winter, AI Summer, revolusi deep learning; (3) Klasifikasi AI: Narrow AI vs General AI vs Super AI; (4) Landscape AI modern: machine learning, deep learning, generative AI, LLM; (5) Aplikasi AI di berbagai bidang dengan konteks Indonesia: e-commerce (Tokopedia, Shopee), transportasi (Gojek, Grab), kesehatan, pertanian presisi, smart city Jakarta; (6) Etika AI dan responsible AI: fairness, accountability, transparency, privacy; (7) Perspektif Islam dalam pengembangan AI: amanah, keadilan (al-'adl), kemaslahatan (maslahah); (8) Kontrak kuliah, ekspektasi, dan pengenalan tools (Google Colab, scikit-learn, TensorFlow) |
| **Metode Pembelajaran** | Ceramah interaktif, diskusi kasus etika AI, demo aplikasi AI |
| **Pengalaman Belajar** | Mahasiswa menyiapkan environment Google Colab, menginstal library ML dasar (scikit-learn, tensorflow), menjalankan demo sederhana klasifikasi dengan sklearn, diskusi kasus bias AI di Indonesia (misal: bias algoritma rekrutmen, moderasi konten media sosial) |
| **Indikator Penilaian** | Mampu menjelaskan definisi, sejarah, dan klasifikasi AI; mengidentifikasi minimal 5 aplikasi AI di Indonesia; menjelaskan minimal 3 prinsip etika AI |
| **Bobot Asesmen** | — (setup & orientation) |
| **Referensi** | [R1] Bab 1; [R2] Ch. 1; [R4] Ch. 1 |

### Minggu 2: Data untuk Machine Learning — NumPy, Pandas, dan Preprocessing

| Komponen | Detail |
|----------|--------|
| **Sub-CPMK** | 2.1, 2.2 |
| **Materi Pembelajaran** | (1) Review NumPy: array operations, broadcasting, vectorization untuk komputasi efisien; (2) Review Pandas: DataFrame, indexing, filtering, groupby, merge dalam konteks ML; (3) Tipe data dalam ML: numerical, categorical, ordinal, text, image; (4) Data preprocessing pipeline: (a) Penanganan missing values: deletion vs imputation (mean, median, KNN imputer); (b) Encoding data kategorikal: Label Encoding, One-Hot Encoding, Ordinal Encoding; (c) Feature scaling: StandardScaler, MinMaxScaler, RobustScaler — kapan pakai yang mana; (5) Pengenalan sklearn.preprocessing dan sklearn.pipeline; (6) Studi kasus: preprocessing dataset sensus penduduk Indonesia |
| **Metode Pembelajaran** | Ceramah, live coding demo, hands-on practice |
| **Pengalaman Belajar** | Mahasiswa melakukan preprocessing pada dataset riil Indonesia (misal: data BPS, dataset pendidikan), membangun preprocessing pipeline dengan sklearn, membandingkan dampak scaling terhadap distribusi data |
| **Indikator Penilaian** | Mampu menerapkan NumPy dan Pandas untuk manipulasi data ML; melakukan preprocessing lengkap (missing values, encoding, scaling) pada dataset baru; membangun pipeline preprocessing dengan sklearn |
| **Bobot Asesmen** | **Tugas 1**: 2.5% |
| **Referensi** | [R1] Bab 2; [R2] Ch. 2; [R3] Ch. 3; [R5] preprocessing docs |

### Minggu 3: Fondasi Matematis ML — Linear Algebra, Probabilitas, dan Statistik

| Komponen | Detail |
|----------|--------|
| **Sub-CPMK** | 3.1, 3.2 |
| **Materi Pembelajaran** | (1) Linear algebra untuk ML: vektor, matriks, transpose, dot product, matrix multiplication — implementasi dengan NumPy; (2) Eigenvalues dan eigenvectors: konsep intuitif dan relevansinya untuk PCA; (3) Probabilitas untuk ML: Bayes' theorem dalam konteks klasifikasi (Naive Bayes); (4) Entropy dan information gain: fondasi Decision Tree; (5) Distribusi probabilitas: Normal, Bernoulli, Multinomial — relevansi untuk ML; (6) Gradient dan optimisasi: konsep intuitif gradient descent; (7) Cost function / loss function: MSE, cross-entropy — mengapa perlu diminimalkan |
| **Metode Pembelajaran** | Ceramah dengan visualisasi, simulasi interaktif, problem solving |
| **Pengalaman Belajar** | Mahasiswa mengimplementasikan operasi matriks dengan NumPy, memvisualisasikan gradient descent pada fungsi sederhana, mensimulasikan Bayes' theorem untuk kasus klasifikasi spam email |
| **Indikator Penilaian** | Mampu menghitung operasi vektor dan matriks dengan NumPy; menjelaskan hubungan probabilitas Bayesian dengan klasifikasi; menjelaskan konsep gradient descent secara intuitif |
| **Bobot Asesmen** | **Tugas 2**: 2.5% |
| **Referensi** | [R1] Bab 3; [R2] Ch. 4; [R4] Ch. 2-4 |

### Minggu 4: EDA untuk ML dan Feature Engineering

| Komponen | Detail |
|----------|--------|
| **Sub-CPMK** | 4.1, 4.2 |
| **Materi Pembelajaran** | (1) Exploratory Data Analysis (EDA) dalam konteks ML: tujuan, workflow, tools; (2) Visualisasi EDA: distribusi fitur (histogram, KDE), hubungan antar fitur (scatter matrix, heatmap korelasi), deteksi outlier (boxplot, IQR method, z-score); (3) Feature engineering: (a) Feature creation: polynomial features, interaction features; (b) Feature transformation: log transform, power transform; (c) Binning dan discretization; (d) Encoding lanjutan: target encoding, frequency encoding; (4) Feature selection awal: correlation analysis, variance threshold; (5) Train-test split: konsep, stratified split, random state; (6) Studi kasus: EDA dan feature engineering pada dataset harga properti Jakarta |
| **Metode Pembelajaran** | Ceramah, workshop EDA, hands-on feature engineering |
| **Pengalaman Belajar** | Mahasiswa melakukan EDA komprehensif pada dataset ML riil, membuat fitur-fitur baru, memvisualisasikan korelasi, dan menyiapkan dataset untuk pemodelan |
| **Indikator Penilaian** | Mampu melakukan EDA lengkap dengan visualisasi yang informatif; menerapkan minimal 3 teknik feature engineering; melakukan train-test split yang benar |
| **Bobot Asesmen** | **Kuis 1** (Minggu 1-4): 4% |
| **Referensi** | [R1] Bab 4; [R2] Ch. 2; [R3] Ch. 4; [R5] preprocessing docs |

---

### FASE 2: SUPERVISED LEARNING — "Learn from Data" (Minggu 5-8)

---

### Minggu 5: Regresi Linear dan Logistik

| Komponen | Detail |
|----------|--------|
| **Sub-CPMK** | 5.1, 5.2 |
| **Materi Pembelajaran** | (1) Supervised learning: paradigma, workflow, terminologi (features, target, training, prediction); (2) Regresi linear: (a) Simple linear regression: least squares, interpretasi slope dan intercept; (b) Multiple linear regression: penambahan fitur; (c) Evaluasi model regresi: MSE, RMSE, MAE, R², adjusted R²; (d) Regularisasi: Ridge (L2) dan Lasso (L1) — konsep dan penggunaan; (3) Regresi logistik: (a) Dari regresi ke klasifikasi: sigmoid function; (b) Binary classification: threshold, probability; (c) Evaluasi: accuracy, precision, recall, F1-score, confusion matrix; (d) ROC curve dan AUC; (4) Implementasi dengan sklearn: LinearRegression, LogisticRegression; (5) Studi kasus: prediksi harga rumah di Jakarta (regresi) dan prediksi churn pelanggan (klasifikasi) |
| **Metode Pembelajaran** | Ceramah, live coding, studi kasus, hands-on modeling |
| **Pengalaman Belajar** | Mahasiswa membangun model regresi dan klasifikasi pada dataset Indonesia, mengevaluasi performa, menginterpretasi koefisien, dan membandingkan model dengan dan tanpa regularisasi |
| **Indikator Penilaian** | Mampu membangun model regresi linear dan logistik dengan sklearn; mengevaluasi model dengan metrik yang tepat; menginterpretasi confusion matrix dan ROC curve |
| **Bobot Asesmen** | **Tugas 3**: 2.5% |
| **Referensi** | [R1] Bab 5; [R2] Ch. 4; [R3] Ch. 2; [R5] linear_model docs |

### Minggu 6: Decision Tree dan Random Forest

| Komponen | Detail |
|----------|--------|
| **Sub-CPMK** | 6.1, 6.2 |
| **Materi Pembelajaran** | (1) Decision Tree: (a) Konsep: struktur pohon, node, leaf, splitting; (b) Kriteria splitting: Gini impurity, entropy, information gain; (c) Pruning: pre-pruning (max_depth, min_samples) dan post-pruning; (d) Visualisasi dan interpretasi pohon keputusan; (e) Overfitting pada Decision Tree; (2) Ensemble methods: konsep "wisdom of crowds" dalam ML; (3) Random Forest: (a) Bagging (Bootstrap Aggregating); (b) Feature randomization; (c) Hyperparameter tuning: n_estimators, max_depth, max_features; (d) Feature importance dari Random Forest; (4) Perbandingan Decision Tree vs Random Forest: bias-variance tradeoff; (5) Cross-validation: k-fold, stratified k-fold; (6) Studi kasus: klasifikasi kelayakan kredit nasabah bank Indonesia |
| **Metode Pembelajaran** | Ceramah, live coding, diskusi model comparison |
| **Pengalaman Belajar** | Mahasiswa membangun Decision Tree dan Random Forest pada dataset klasifikasi, memvisualisasikan pohon keputusan, menganalisis feature importance, dan melakukan cross-validation |
| **Indikator Penilaian** | Mampu membangun dan memvisualisasikan Decision Tree; menerapkan Random Forest dan menginterpretasi feature importance; melakukan cross-validation untuk evaluasi model |
| **Bobot Asesmen** | **Tugas 4**: 2.5% |
| **Referensi** | [R1] Bab 6; [R2] Ch. 6-7; [R3] Ch. 2, 5; [R5] ensemble docs |

### Minggu 7: SVM dan KNN

| Komponen | Detail |
|----------|--------|
| **Sub-CPMK** | 7.1, 7.2 |
| **Materi Pembelajaran** | (1) Support Vector Machine (SVM): (a) Konsep hyperplane dan maximum margin; (b) Support vectors: data points yang menentukan boundary; (c) Linear SVM vs non-linear SVM; (d) Kernel trick: linear, polynomial, RBF; (e) Hyperparameter: C (regularization), gamma; (f) SVM untuk klasifikasi multi-class: one-vs-one, one-vs-rest; (2) K-Nearest Neighbors (KNN): (a) Konsep instance-based learning; (b) Distance metrics: Euclidean, Manhattan, Minkowski; (c) Pengaruh parameter K: underfitting vs overfitting; (d) Curse of dimensionality; (e) KNN untuk klasifikasi dan regresi; (3) Model comparison: kapan pakai SVM vs KNN vs tree-based vs linear models; (4) Hyperparameter tuning: GridSearchCV, RandomizedSearchCV; (5) Studi kasus: klasifikasi jenis batik Indonesia berdasarkan fitur tekstur |
| **Metode Pembelajaran** | Ceramah, visualisasi decision boundary, hands-on tuning |
| **Pengalaman Belajar** | Mahasiswa membangun model SVM dan KNN, memvisualisasikan decision boundary, melakukan hyperparameter tuning dengan GridSearchCV, membandingkan performa semua model supervised yang telah dipelajari |
| **Indikator Penilaian** | Mampu membangun model SVM dengan kernel yang sesuai; menganalisis pengaruh K pada KNN; melakukan hyperparameter tuning sistematis; membandingkan performa berbagai model |
| **Bobot Asesmen** | **Kuis 2** (Minggu 5-7): 3% |
| **Referensi** | [R1] Bab 7; [R2] Ch. 5; [R3] Ch. 2; [R5] svm, neighbors docs |

### Minggu 8: UJIAN TENGAH SEMESTER (UTS)

| Komponen | Detail |
|----------|--------|
| **Cakupan** | Minggu 1-7 (CPMK 1-3) |
| **Format** | Closed-book, written exam (individual) |
| **Durasi** | 100 menit |
| **Tipe Soal** | (1) Pilihan ganda konseptual tentang AI, ML, dan algoritma (20%); (2) Soal hitungan: preprocessing, evaluasi model, metrik klasifikasi (25%); (3) Interpretasi output Python/sklearn: confusion matrix, classification report, feature importance (25%); (4) Essay analisis kasus: pemilihan algoritma dan justifikasi untuk skenario tertentu (30%) |
| **Bobot Asesmen** | **20%** dari nilai akhir |

---

### FASE 3: ADVANCED ML — "Model Complex Patterns" (Minggu 9-12)

---

### Minggu 9: Unsupervised Learning — Clustering

| Komponen | Detail |
|----------|--------|
| **Sub-CPMK** | 9.1, 9.2 |
| **Materi Pembelajaran** | (1) Unsupervised learning: paradigma, perbedaan dengan supervised learning, use cases; (2) K-Means Clustering: (a) Algoritma: inisialisasi centroid, assignment, update; (b) Menentukan jumlah cluster optimal: Elbow method, Silhouette score, Calinski-Harabasz index; (c) Limitasi K-Means: asumsi spherical clusters, sensitivity terhadap outlier; (d) K-Means++: inisialisasi yang lebih baik; (3) Hierarchical Clustering: (a) Agglomerative (bottom-up) vs divisive (top-down); (b) Linkage methods: single, complete, average, Ward; (c) Dendrogram: interpretasi dan cutting; (4) DBSCAN: density-based clustering, konsep eps dan min_samples; (5) Evaluasi clustering: internal (Silhouette) vs external metrics; (6) Studi kasus: segmentasi pelanggan e-commerce Indonesia (Tokopedia/Shopee) |
| **Metode Pembelajaran** | Ceramah, visualisasi clustering, hands-on segmentasi |
| **Pengalaman Belajar** | Mahasiswa menerapkan K-Means dan hierarchical clustering pada dataset pelanggan, memvisualisasikan cluster, menginterpretasi dendrogram, dan menentukan jumlah cluster optimal menggunakan berbagai metrik |
| **Indikator Penilaian** | Mampu menerapkan K-Means dengan pemilihan K optimal; menginterpretasi dendrogram; memilih algoritma clustering yang tepat sesuai karakteristik data |
| **Bobot Asesmen** | **Tugas 5**: 2.5% |
| **Referensi** | [R1] Bab 8; [R2] Ch. 9; [R3] Ch. 3; [R5] cluster docs |

### Minggu 10: Reduksi Dimensi dan Feature Selection

| Komponen | Detail |
|----------|--------|
| **Sub-CPMK** | 10.1, 10.2 |
| **Materi Pembelajaran** | (1) Curse of dimensionality: mengapa banyak fitur bisa menjadi masalah; (2) Principal Component Analysis (PCA): (a) Konsep: variance maximization, eigenvectors; (b) Langkah-langkah PCA: standardize, covariance matrix, eigendecomposition; (c) Explained variance ratio dan pemilihan jumlah komponen; (d) Visualisasi PCA: scree plot, biplot; (e) PCA untuk visualisasi data high-dimensional; (3) t-SNE dan UMAP: reduksi dimensi untuk visualisasi (pengantar); (4) Feature selection: (a) Filter methods: correlation, variance threshold, mutual information; (b) Wrapper methods: forward selection, backward elimination, RFE; (c) Embedded methods: Lasso, Random Forest feature importance; (5) Feature extraction vs feature selection: kapan pakai yang mana; (6) Studi kasus: reduksi dimensi pada dataset citra digit (MNIST subset) |
| **Metode Pembelajaran** | Ceramah, visualisasi PCA, hands-on feature engineering |
| **Pengalaman Belajar** | Mahasiswa menerapkan PCA pada dataset high-dimensional, memvisualisasikan hasil reduksi dimensi, melakukan feature selection dengan berbagai metode, dan membandingkan performa model sebelum dan sesudah reduksi dimensi |
| **Indikator Penilaian** | Mampu menerapkan PCA dan menginterpretasi explained variance; melakukan feature selection dengan metode yang tepat; memvisualisasikan data high-dimensional setelah reduksi dimensi |
| **Bobot Asesmen** | — |
| **Referensi** | [R1] Bab 9; [R2] Ch. 8; [R3] Ch. 4; [R5] decomposition docs |

### Minggu 11: Neural Network dan Deep Learning Dasar

| Komponen | Detail |
|----------|--------|
| **Sub-CPMK** | 11.1, 11.2 |
| **Materi Pembelajaran** | (1) Dari model linear ke neural network: perceptron, multi-layer perceptron (MLP); (2) Arsitektur neural network: (a) Input layer, hidden layers, output layer; (b) Neuron: weights, bias, activation; (c) Activation functions: Sigmoid, ReLU, Tanh, Softmax — kapan pakai yang mana; (3) Forward propagation: alur data dari input ke output; (4) Backpropagation: (a) Konsep intuitif: chain rule, gradient propagation; (b) Proses update weights: learning rate; (5) Training neural network: (a) Loss functions: MSE (regresi), cross-entropy (klasifikasi); (b) Optimizers: SGD, Adam, RMSprop; (c) Epochs, batch size, dan learning rate; (d) Overfitting di neural network: dropout, early stopping; (6) TensorFlow/Keras: Sequential API, compile, fit, evaluate; (7) Studi kasus: klasifikasi digit MNIST dengan MLP menggunakan Keras |
| **Metode Pembelajaran** | Ceramah, live coding TensorFlow/Keras, hands-on training |
| **Pengalaman Belajar** | Mahasiswa membangun neural network pertama dengan Keras, melatih model pada dataset MNIST, memvisualisasikan learning curve, bereksperimen dengan hyperparameter (learning rate, jumlah layer/neuron, dropout) |
| **Indikator Penilaian** | Mampu membangun MLP dengan TensorFlow/Keras; menjelaskan mekanisme backpropagation secara intuitif; mengidentifikasi overfitting dan menerapkan teknik regularisasi |
| **Bobot Asesmen** | **Tugas 6**: 2.5% |
| **Referensi** | [R1] Bab 10; [R2] Ch. 10-11; [R4] Ch. 6; [R6] Keras tutorial |

### Minggu 12: Natural Language Processing (NLP) Dasar

| Komponen | Detail |
|----------|--------|
| **Sub-CPMK** | 12.1, 12.2 |
| **Materi Pembelajaran** | (1) NLP overview: mengapa pemrosesan bahasa alami itu sulit; (2) Text preprocessing untuk bahasa Indonesia: (a) Tokenisasi: word-level, subword; (b) Case folding dan normalisasi; (c) Stopword removal: pentingnya stopword list bahasa Indonesia; (d) Stemming: algoritma Nazief-Adriani untuk bahasa Indonesia (library Sastrawi); (e) Lemmatization; (3) Text representation: (a) Bag of Words (BoW); (b) TF-IDF (Term Frequency — Inverse Document Frequency); (c) Pengantar word embeddings: Word2Vec, konsep intuitif; (4) Text classification pipeline: TF-IDF + Naive Bayes / Logistic Regression / SVM; (5) Evaluasi model NLP: accuracy, precision, recall, F1 per kelas; (6) Studi kasus: analisis sentimen ulasan produk e-commerce Indonesia |
| **Metode Pembelajaran** | Ceramah, live coding NLP pipeline, hands-on text classification |
| **Pengalaman Belajar** | Mahasiswa membangun pipeline NLP untuk analisis sentimen teks bahasa Indonesia, dari preprocessing hingga model klasifikasi, menggunakan data ulasan produk dari e-commerce Indonesia |
| **Indikator Penilaian** | Mampu melakukan text preprocessing untuk teks Indonesia; membangun pipeline TF-IDF + classifier; mengevaluasi model klasifikasi teks dengan metrik yang tepat |
| **Bobot Asesmen** | **Kuis 3** (Minggu 9-12): 3% |
| **Referensi** | [R1] Bab 11; [R3] Ch. 7; [R5] feature_extraction.text docs |

---

### FASE 4: APPLIED AI & FRONTIER — "Build Intelligent Systems" (Minggu 13-16)

---

### Minggu 13: Computer Vision Dasar dan CNN

| Komponen | Detail |
|----------|--------|
| **Sub-CPMK** | 13.1, 13.2 |
| **Materi Pembelajaran** | (1) Computer Vision overview: dari pixel ke pemahaman visual; (2) Image processing dasar dengan OpenCV: (a) Membaca, menampilkan, menyimpan gambar; (b) Operasi dasar: resize, crop, rotate, color conversion (RGB, grayscale); (c) Image augmentation: flip, rotation, brightness, zoom — untuk menambah data training; (3) Convolutional Neural Network (CNN): (a) Konsep konvolusi: filter/kernel, feature maps; (b) Arsitektur CNN: Convolutional layer, Pooling layer, Flatten, Dense; (c) Stride, padding, dan pooling (max, average); (d) Transfer learning: menggunakan pre-trained model (VGG16, ResNet) — konsep dan demo; (4) Membangun CNN dengan Keras: Conv2D, MaxPooling2D, compile, fit; (5) Studi kasus: klasifikasi citra produk UMKM Indonesia (batik, makanan, kerajinan) |
| **Metode Pembelajaran** | Ceramah, live coding OpenCV dan CNN, hands-on image classification |
| **Pengalaman Belajar** | Mahasiswa membangun pipeline computer vision dari image preprocessing hingga CNN classification, bereksperimen dengan arsitektur CNN sederhana, dan melakukan transfer learning dengan model pre-trained |
| **Indikator Penilaian** | Mampu melakukan image processing dasar dengan OpenCV; membangun dan melatih model CNN sederhana; menjelaskan konsep transfer learning |
| **Bobot Asesmen** | — |
| **Referensi** | [R1] Bab 12; [R2] Ch. 14; [R4] Ch. 9; [R6] Keras CNN tutorial |

### Minggu 14: AI sebagai Co-Developer dan Pengantar MLOps

| Komponen | Detail |
|----------|--------|
| **Sub-CPMK** | 14.1, 14.2 |
| **Materi Pembelajaran** | (1) AI sebagai co-developer dalam ML: (a) Prompt engineering untuk coding dan ML: menulis prompt efektif untuk ChatGPT/Claude/Copilot; (b) Workflow AI-augmented development: human design → AI draft → human review → iterate; (c) Best practices: verifikasi output AI, critical evaluation, dokumentasi; (d) Kapan AI membantu vs kapan bisa menyesatkan dalam ML; (e) Etika penggunaan AI dalam pengembangan: atribusi, transparansi, amanah; (2) Pengantar MLOps: (a) ML lifecycle: data → training → evaluation → deployment → monitoring; (b) Experiment tracking: logging hyperparameters, metrics, models (pengantar MLflow/Weights & Biases); (c) Model versioning: menyimpan dan mengelola versi model; (d) Model deployment dasar: saving model (joblib, SavedModel), membuat prediction function; (e) Monitoring model di produksi: concept drift, data drift (pengantar konseptual); (3) Reproducibility dalam ML: random seeds, environment management; (4) Studi kasus: membangun end-to-end ML pipeline dengan bantuan AI co-developer |
| **Metode Pembelajaran** | Workshop interaktif, demo AI co-development, hands-on MLOps |
| **Pengalaman Belajar** | Mahasiswa menggunakan AI untuk membangun pipeline ML lengkap, mendokumentasikan setiap interaksi AI dalam AI Usage Log, melakukan experiment tracking, dan menyimpan model yang reproducible |
| **Indikator Penilaian** | Mampu menggunakan AI sebagai co-developer secara efektif dan etis; menjelaskan konsep MLOps; melakukan experiment tracking; menyimpan dan memuat model yang terlatih |
| **Bobot Asesmen** | — |
| **Referensi** | [R1] Bab 13; [R2] Ch. 19; UNESCO AI Ethics (2021); ACM Code of Ethics (2018) |

### Minggu 15: Presentasi Proyek Akhir ML End-to-End

| Komponen | Detail |
|----------|--------|
| **Sub-CPMK** | 15.1 |
| **Kegiatan** | (1) Presentasi proyek akhir kelompok (15 menit per kelompok): demonstrasi model, analisis hasil, lessons learned; (2) Q&A dan diskusi (5 menit per kelompok); (3) Peer review menggunakan rubrik terstruktur; (4) Demo live model prediction; (5) Review AI Usage Log: transparansi penggunaan AI selama proyek; (6) Refleksi perjalanan belajar: dari fondasi AI hingga proyek end-to-end |
| **Metode Pembelajaran** | Presentasi, peer review, refleksi, demo |
| **Pengalaman Belajar** | Mahasiswa mempresentasikan proyek ML end-to-end yang menyelesaikan masalah riil Indonesia, mendemonstrasikan model yang bekerja, menerima feedback dari dosen dan peers, melakukan peer review |
| **Indikator Penilaian** | Kualitas proyek (problem statement, data pipeline, model, evaluasi, dokumentasi); kualitas presentasi dan demo; kelengkapan AI Usage Log; kemampuan menjawab pertanyaan |
| **Bobot Asesmen** | **Proyek Akhir**: **25%** dari nilai akhir (presentasi + notebook + laporan + AI Usage Log) |
| **Referensi** | — |

### Minggu 16: UJIAN AKHIR SEMESTER (UAS)

| Komponen | Detail |
|----------|--------|
| **Cakupan** | Minggu 1-15 — komprehensif (CPMK 1-7, penekanan pada CPMK 4-7) |
| **Format** | Closed-book + open-note (1 lembar A4 catatan, bolak-balik) |
| **Durasi** | 100 menit |
| **Tipe Soal** | (1) Pilihan ganda konseptual tentang ML, DL, NLP, CV (15%); (2) Soal hitungan dan interpretasi: evaluasi model, PCA, clustering metrics (25%); (3) Interpretasi output ML: classification report, confusion matrix, learning curve, dendrogram (25%); (4) Essay analisis kasus: desain pipeline ML untuk masalah riil, pemilihan algoritma, justifikasi keputusan desain (35%) |
| **Bobot Asesmen** | **25%** dari nilai akhir |

---

## G. PETA EVALUASI (ASSESSMENT MAP)

### G.1 Ringkasan Bobot Penilaian

| Komponen | Jumlah | Bobot per Item | Total Bobot |
|----------|--------|----------------|-------------|
| Tugas Mingguan | 6 kali | 2.5% | **15%** |
| Kuis | 3 kali | K1: 4%, K2: 3%, K3: 3% | **10%** |
| UTS | 1 kali | 20% | **20%** |
| Proyek Akhir | 1 kali | 25% | **25%** |
| UAS | 1 kali | 25% | **25%** |
| Partisipasi & Etika AI | Ongoing | 5% | **5%** |
| **TOTAL** | | | **100%** |

### G.2 Peta CPMK vs Asesmen

| CPMK | Tugas | Kuis | UTS | Proyek | UAS | Partisipasi |
|------|-------|------|-----|--------|-----|-------------|
| CPMK-1 | T1 | K1 | V | V | | V |
| CPMK-2 | T1, T2 | K1 | V | V | | |
| CPMK-3 | T3, T4 | K2 | V | V | V | |
| CPMK-4 | T5 | K3 | | V | V | |
| CPMK-5 | T6 | K3 | | V | V | |
| CPMK-6 | | K3 | | V | V | |
| CPMK-7 | | | | V | V | V |

*V = diases dalam komponen tersebut*

### G.3 Timeline Asesmen

```
Minggu:  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16
         |  T1 T2 K1 T3 T4 K2 UTS T5     T6  K3          PF  UAS
              |  |  |  |  |  |     |       |   |           |
              └──┴──┴──┘  └──┘     └───────┘   |           │
              Fase 1      Fase 2   Fase 3      └───────────┘
                                               Fase 4
```
*T=Tugas, K=Kuis, UTS=Ujian Tengah, PF=Proyek Final, UAS=Ujian Akhir*

---

## H. KONVERSI NILAI

| Rentang | Huruf | Bobot | Predikat |
|---------|-------|-------|----------|
| 85 - 100 | A | 4.00 | Sangat Baik |
| 80 - 84 | A- | 3.75 | Sangat Baik |
| 75 - 79 | B+ | 3.50 | Baik |
| 70 - 74 | B | 3.00 | Baik |
| 65 - 69 | B- | 2.75 | Cukup Baik |
| 60 - 64 | C+ | 2.50 | Cukup |
| 55 - 59 | C | 2.00 | Cukup |
| 40 - 54 | D | 1.00 | Kurang |
| 0 - 39 | E | 0.00 | Sangat Kurang |

---

## I. REFERENSI

### Referensi Utama

1. **[R1] Nugroho, T. A. (2026).** *Kecerdasan Buatan dan Machine Learning: Buku Ajar*. Program Studi Informatika, Universitas Al Azhar Indonesia.
2. **[R2] Geron, A. (2022).** *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow (3rd ed.)*. O'Reilly Media.
3. **[R3] Muller, A. C., & Guido, S. (2016).** *Introduction to Machine Learning with Python*. O'Reilly Media.

### Referensi Pendukung

4. **[R4] Goodfellow, I., Bengio, Y., & Courville, A. (2016).** *Deep Learning*. MIT Press. [Tersedia gratis: deeplearningbook.org]
5. **[R5] scikit-learn Documentation**: [scikit-learn.org/stable](https://scikit-learn.org/stable/) — referensi utama API dan tutorial ML
6. **[R6] TensorFlow/Keras Documentation**: [tensorflow.org](https://www.tensorflow.org/) — referensi utama deep learning

### Referensi Online

7. **Google Colab**: [colab.research.google.com](https://colab.research.google.com) — platform coding utama
8. **Kaggle**: [kaggle.com](https://kaggle.com) — dataset dan kompetisi data science
9. **Papers with Code**: [paperswithcode.com](https://paperswithcode.com) — state-of-the-art ML benchmarks
10. **BPS (Badan Pusat Statistik)**: [bps.go.id](https://bps.go.id) — sumber dataset Indonesia

---

## J. KEBIJAKAN KHUSUS MATA KULIAH

### J.1 Kebijakan Penggunaan AI

Mata kuliah ini secara **eksplisit mengizinkan dan mendorong** penggunaan AI assistants (Claude, ChatGPT, Copilot, dll.) dengan ketentuan:

1. **Transparansi wajib**: Setiap penggunaan AI dalam tugas harus didokumentasikan (prompt yang digunakan, output yang dihasilkan, modifikasi yang dilakukan)
2. **AI sebagai co-developer, bukan ghost-coder**: Mahasiswa harus memahami dan bisa menjelaskan setiap baris kode dan keputusan desain model
3. **UTS dan UAS tanpa AI**: Ujian closed-book dilakukan tanpa akses ke AI tools
4. **Etika AI**: Mahasiswa diharapkan menerapkan prinsip responsible AI: verifikasi output, identifikasi bias, jujur tentang limitasi model
5. **Learning log**: Mahasiswa mendokumentasikan refleksi penggunaan AI setiap 4 minggu
6. **Progressive AI integration**: Penggunaan AI meningkat sepanjang semester — dari explorer (Bab 1-4) menjadi co-developer (Bab 5-10) hingga architect (Bab 11-14)

### J.2 Kebijakan Kehadiran

- Kehadiran minimal **75%** dari 16 pertemuan
- Izin/sakit harus disertai bukti dan diajukan maksimal 3 hari setelah ketidakhadiran
- Terlambat >15 menit dihitung sebagai tidak hadir

### J.3 Kebijakan Keterlambatan Tugas

- Keterlambatan 1-3 hari: penalti -20% dari nilai tugas
- Keterlambatan >3 hari: nilai maksimal 50% dari rubrik
- Force majeure: dikonsultasikan dengan dosen pengampu

### J.4 Kebijakan Academic Integrity

- Plagiarisme (termasuk copy-paste kode tanpa atribusi) akan dikenai sanksi sesuai peraturan akademik UAI
- Kolaborasi diperbolehkan untuk tugas tertentu (akan ditandai), tetapi semua pekerjaan yang dikumpulkan harus merupakan pemahaman individual
- Kode yang dihasilkan AI harus dipahami sepenuhnya oleh mahasiswa — jika tidak bisa menjelaskan, dianggap bukan pekerjaan sendiri
- Menyalin model ML orang lain tanpa pemahaman dan modifikasi dianggap pelanggaran integritas akademik

---

## K. PROFIL PROYEK AKHIR

### Deskripsi Singkat

Mahasiswa (kelompok 2-3 orang) merancang dan membangun pipeline ML end-to-end untuk menyelesaikan masalah riil di konteks Indonesia, menggunakan teknik ML yang dipelajari selama semester, dengan AI sebagai co-developer yang didokumentasikan secara transparan.

### Contoh Topik Proyek

- Prediksi harga properti di kota-kota Indonesia menggunakan data OLX/Rumah123
- Analisis sentimen ulasan produk e-commerce Indonesia (Tokopedia, Shopee)
- Klasifikasi jenis batik Indonesia menggunakan computer vision
- Prediksi kualitas udara DKI Jakarta berdasarkan data sensor BMKG
- Deteksi hoax berita berbahasa Indonesia menggunakan NLP
- Segmentasi pelanggan UMKM berdasarkan pola transaksi
- Prediksi hasil pertanian berdasarkan data cuaca dan tanah

### Timeline Proyek

| Minggu | Milestone |
|--------|-----------|
| 9 | Pengumuman proyek, pembentukan kelompok, brainstorm topik |
| 10 | Proposal topik + dataset (disetujui dosen) |
| 11 | Data preprocessing dan EDA selesai |
| 12 | Model pertama (baseline) terbangun dan dievaluasi |
| 13 | Model improvement dan eksperimentasi |
| 14 | Finalisasi pipeline, dokumentasi, persiapan presentasi |
| 15 | **Presentasi + Peer Review + Demo Live** |

### Deliverables

1. **Jupyter Notebook** — Kode ML pipeline lengkap, well-documented, reproducible
2. **Laporan singkat** (5-7 halaman) — Problem statement, data description, methodology, model evaluation, findings, conclusion
3. **Presentasi** (15 menit) — Slide deck + live demo model prediction
4. **AI Usage Log** — Dokumentasi seluruh interaksi AI selama proyek: prompt, output, keputusan yang diambil

*(Detail rubrik tersedia di `05-assessments/project-guidelines.md`)*

---

*Dokumen RPS ini disusun berdasarkan standar SN-Dikti, KKNI Level 6, dan pedoman OBE yang diacu oleh Prodi Informatika Universitas Al Azhar Indonesia.*

*Diperbarui: Februari 2026*

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
