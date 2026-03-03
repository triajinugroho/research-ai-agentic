# Kisi-Kisi Ujian Tengah Semester (UTS)

## Mata Kuliah: Kecerdasan Buatan dan Machine Learning (IF3XXX, 4 SKS)
### Prodi Informatika — UAI — Semester Ganjil 2026/2027
### Dosen Pengampu: Tri Aji Nugroho, S.T., M.T.

---

## Informasi Umum

| Komponen | Detail |
|----------|--------|
| **Waktu** | Minggu 8, 100 menit |
| **Format** | Closed-book, written exam (tanpa akses AI/internet) |
| **Cakupan** | Minggu 1-7 (CPMK 1-3) |
| **Bobot** | 20% dari nilai akhir |
| **Alat yang diizinkan** | Kalkulator non-programmable, alat tulis |

---

## Distribusi Soal

| Tipe Soal | Jumlah | Bobot | Bloom's |
|-----------|--------|-------|---------|
| Pilihan Ganda (PG) | 10 soal @ 2 poin | 20% | C1-C3 |
| Short Answer | 4 soal @ 5 poin | 20% | C2-C4 |
| Code Tracing / Interpretasi Output | 3 soal @ 10 poin | 30% | C3-C4 |
| Tulis Kode / Essay Analisis | 3 soal @ 10 poin | 30% | C3-C5 |
| **Total** | **20 soal** | **100%** (100 poin) | |

---

## Kisi-Kisi Detail per Topik

### Minggu 1: Pengantar Kecerdasan Buatan dan Etika AI (CPMK-1)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Menjelaskan definisi AI, sejarah perkembangan AI (Turing Test, AI Winter, AI Summer) | C2 | PG |
| Membedakan Narrow AI, General AI, dan Super AI | C2 | PG |
| Mengklasifikasikan problem ke supervised/unsupervised/reinforcement learning | C2 | PG |
| Mengidentifikasi isu etika AI dan prinsip responsible AI berdasarkan nilai-nilai Islami | C2 | PG/Short Answer |

**Contoh soal PG:**
> Manakah pernyataan yang BENAR tentang klasifikasi kecerdasan buatan?
> A. Narrow AI dapat menyelesaikan semua jenis tugas kognitif seperti manusia
> B. General AI sudah banyak diimplementasikan di industri saat ini
> C. Narrow AI dirancang untuk menyelesaikan tugas spesifik, seperti pengenalan wajah atau rekomendasi produk
> D. Super AI adalah istilah lain untuk deep learning
>
> **Jawaban: C** — Narrow AI (Artificial Narrow Intelligence) dirancang untuk satu tugas spesifik. General AI yang mampu menyelesaikan berbagai tugas kognitif seperti manusia belum tercapai.

---

### Minggu 2: Data untuk Machine Learning — NumPy, Pandas, dan Preprocessing (CPMK-2)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Menerapkan NumPy dan Pandas untuk manipulasi data dalam konteks ML | C3 | Code Tracing/Tulis Kode |
| Menjelaskan teknik penanganan missing values (deletion, imputation) | C2-C3 | Short Answer |
| Membedakan metode encoding: Label Encoding, One-Hot Encoding, Ordinal Encoding | C2-C3 | PG |
| Menerapkan feature scaling: StandardScaler, MinMaxScaler, RobustScaler | C3 | Code Tracing |

**Contoh soal Code Tracing:**
> Perhatikan kode Python berikut. Tentukan output yang dihasilkan dan jelaskan apa yang terjadi pada langkah scaling. (10 poin)
>
> ```python
> import numpy as np
> from sklearn.model_selection import train_test_split
> from sklearn.preprocessing import StandardScaler
>
> X = np.array([[1, 200], [2, 400], [3, 600], [4, 800],
>               [5, 1000], [6, 1200], [7, 1400], [8, 1600],
>               [9, 1800], [10, 2000]])
> y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
>
> X_train, X_test, y_train, y_test = train_test_split(
>     X, y, test_size=0.3, random_state=42
> )
>
> scaler = StandardScaler()
> X_train_scaled = scaler.fit_transform(X_train)
> X_test_scaled = scaler.transform(X_test)
>
> print(X_train.shape, X_test.shape)
> ```
>
> **Jawaban:**
> ```
> (7, 2) (3, 2)
> ```
>
> **Penjelasan:**
> - Dataset memiliki 10 sampel, 2 fitur.
> - `test_size=0.3` berarti 30% data (3 sampel) untuk test, 70% (7 sampel) untuk training.
> - `fit_transform` pada X_train: menghitung mean & std dari training data, lalu melakukan transformasi.
> - `transform` pada X_test: menggunakan mean & std dari training data (bukan menghitung ulang dari test data) untuk menghindari data leakage.

---

### Minggu 3: Fondasi Matematis ML — Linear Algebra, Probabilitas, dan Statistik (CPMK-2)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Menghitung operasi vektor dan matriks dasar (dot product, matrix multiplication) dengan NumPy | C3 | Code Tracing/Tulis Kode |
| Menerapkan Bayes' theorem dalam konteks klasifikasi (Naive Bayes) | C3-C4 | Short Answer/Hitungan |
| Menjelaskan konsep entropy dan information gain sebagai fondasi Decision Tree | C2-C3 | PG/Short Answer |
| Menjelaskan konsep gradient descent dan loss function secara intuitif | C2 | PG |

**Contoh soal Short Answer:**
> Dalam konteks klasifikasi spam email, terdapat data sebagai berikut:
> - P(Spam) = 0.3, P(Not Spam) = 0.7
> - P("promo" | Spam) = 0.8, P("promo" | Not Spam) = 0.1
>
> Menggunakan Bayes' Theorem, hitung probabilitas sebuah email adalah spam jika mengandung kata "promo". (5 poin)
>
> **Jawaban:**
> P(Spam | "promo") = P("promo" | Spam) × P(Spam) / P("promo")
> = (0.8 × 0.3) / (0.8 × 0.3 + 0.1 × 0.7)
> = 0.24 / (0.24 + 0.07) = 0.24 / 0.31 ≈ 0.774 ≈ 77.4%
>
> Meskipun prior probability spam hanya 30%, keberadaan kata "promo" yang sangat sering muncul di spam meningkatkan posterior probability menjadi ~77%.

---

### Minggu 4: EDA untuk ML dan Feature Engineering (CPMK-2)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Melakukan Exploratory Data Analysis (EDA) pada dataset ML menggunakan visualisasi dan statistik | C3-C4 | Code Tracing/Interpretasi |
| Menerapkan teknik feature engineering: polynomial features, log transform, binning | C3 | Short Answer/Tulis Kode |
| Menjelaskan pentingnya train-test split dan stratified split | C2-C3 | PG |
| Mengidentifikasi outlier menggunakan IQR method dan z-score | C3 | PG/Short Answer |

**Contoh soal PG:**
> Mengapa feature scaling penting sebelum melatih model KNN tetapi TIDAK wajib untuk Decision Tree?
> A. KNN menggunakan jarak Euclidean yang sensitif terhadap skala fitur, sedangkan Decision Tree menggunakan threshold splitting yang tidak terpengaruh skala
> B. KNN hanya bekerja dengan data numerik, sedangkan Decision Tree hanya bekerja dengan data kategorikal
> C. Feature scaling membuat KNN lebih lambat tetapi Decision Tree lebih cepat
> D. Feature scaling hanya diperlukan untuk regresi, bukan klasifikasi
>
> **Jawaban: A** — KNN menghitung jarak antar titik data (Euclidean distance) sehingga fitur dengan skala besar akan mendominasi. Decision Tree memilih threshold optimal per fitur, sehingga tidak terpengaruh skala.

---

### Minggu 5: Regresi Linear dan Logistik (CPMK-3)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Membangun model regresi linear dan mengevaluasi performa (MSE, RMSE, R²) | C3-C4 | Code Tracing/Tulis Kode |
| Membangun model regresi logistik untuk klasifikasi biner dan menginterpretasi hasil | C3-C4 | Short Answer/Interpretasi |
| Menginterpretasi confusion matrix, precision, recall, F1-score, ROC-AUC | C4 | Code Tracing |
| Menjelaskan perbedaan Ridge (L2) dan Lasso (L1) regularisasi | C2-C3 | PG |

**Contoh soal Code Tracing:**
> Perhatikan kode Python berikut. Tentukan output yang dihasilkan. (10 poin)
>
> ```python
> from sklearn.metrics import confusion_matrix, accuracy_score
> from sklearn.metrics import precision_score, recall_score, f1_score
>
> y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
> y_pred = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
>
> cm = confusion_matrix(y_true, y_pred)
> print("Confusion Matrix:")
> print(cm)
> print(f"Accuracy: {accuracy_score(y_true, y_pred):.2f}")
> print(f"Precision: {precision_score(y_true, y_pred):.2f}")
> print(f"Recall: {recall_score(y_true, y_pred):.2f}")
> ```
>
> **Jawaban:**
> ```
> Confusion Matrix:
> [[4 1]
>  [1 4]]
> Accuracy: 0.80
> Precision: 0.80
> Recall: 0.80
> ```
>
> **Penjelasan:**
> - TN=4 (actual 0, predicted 0), FP=1 (actual 0, predicted 1)
> - FN=1 (actual 1, predicted 0), TP=4 (actual 1, predicted 1)
> - Accuracy = (4+4)/10 = 0.80
> - Precision = TP/(TP+FP) = 4/(4+1) = 0.80
> - Recall = TP/(TP+FN) = 4/(4+1) = 0.80

---

### Minggu 6: Decision Tree dan Random Forest (CPMK-3)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Membangun Decision Tree dan menginterpretasi struktur pohon keputusan | C4 | Short Answer/Code Tracing |
| Menjelaskan kriteria splitting: Gini impurity, entropy, information gain | C3-C4 | PG/Short Answer |
| Menerapkan Random Forest dan membandingkan dengan Decision Tree (bias-variance tradeoff) | C4 | PG/Tulis Kode |
| Menginterpretasi feature importance dari Random Forest | C4 | Interpretasi |

**Contoh soal PG:**
> Pada algoritma Random Forest, teknik yang digunakan untuk mengurangi korelasi antar pohon keputusan adalah:
> A. Menggunakan seluruh fitur pada setiap split
> B. Melakukan random feature selection pada setiap split
> C. Mengurangi kedalaman setiap pohon menjadi 1
> D. Menggunakan data training yang sama untuk semua pohon
>
> **Jawaban: B** — Random Forest menggunakan random feature subsampling pada setiap split node (biasanya sqrt(n_features)) untuk mengurangi korelasi antar pohon, sehingga ensemble lebih robust.

**Contoh soal Tulis Kode:**
> Tuliskan kode Python untuk membandingkan performa 3 model (Decision Tree, Random Forest, SVM) menggunakan 5-fold cross-validation pada dataset yang sama. Tampilkan rata-rata accuracy untuk setiap model. (10 poin)
>
> **Jawaban:**
> ```python
> from sklearn.tree import DecisionTreeClassifier
> from sklearn.ensemble import RandomForestClassifier
> from sklearn.svm import SVC
> from sklearn.model_selection import cross_val_score
> from sklearn.preprocessing import StandardScaler
> from sklearn.pipeline import Pipeline
>
> # Definisikan model dalam pipeline (dengan scaling)
> models = {
>     'Decision Tree': Pipeline([
>         ('scaler', StandardScaler()),
>         ('clf', DecisionTreeClassifier(random_state=42))
>     ]),
>     'Random Forest': Pipeline([
>         ('scaler', StandardScaler()),
>         ('clf', RandomForestClassifier(random_state=42))
>     ]),
>     'SVM': Pipeline([
>         ('scaler', StandardScaler()),
>         ('clf', SVC(random_state=42))
>     ])
> }
>
> # Evaluasi setiap model dengan 5-fold CV
> for name, model in models.items():
>     scores = cross_val_score(model, X_train, y_train, cv=5,
>                              scoring='accuracy')
>     print(f"{name}: {scores.mean():.4f} (+/- {scores.std():.4f})")
> ```

---

### Minggu 7: SVM dan KNN (CPMK-3)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Membangun model SVM dan memahami konsep hyperplane, margin, dan kernel trick | C4 | PG/Short Answer |
| Membangun model KNN dan menganalisis pengaruh parameter K terhadap performa | C4 | PG/Code Tracing |
| Membandingkan performa berbagai model supervised learning | C4 | Tulis Kode/Essay |
| Melakukan hyperparameter tuning dengan GridSearchCV dan RandomizedSearchCV | C3-C4 | Short Answer/Tulis Kode |

**Contoh soal Short Answer:**
> Jelaskan perbedaan antara GridSearchCV dan RandomizedSearchCV. Kapan sebaiknya menggunakan masing-masing? (5 poin)
>
> **Jawaban:**
> - **GridSearchCV:** Mencoba semua kombinasi hyperparameter yang didefinisikan. Exhaustive search. Tepat digunakan jika jumlah hyperparameter sedikit dan range sempit.
> - **RandomizedSearchCV:** Mengambil sampel acak dari distribusi hyperparameter. Tidak semua kombinasi dicoba. Tepat digunakan jika jumlah hyperparameter banyak atau range luas, karena lebih efisien secara komputasi.
> - GridSearchCV menjamin menemukan kombinasi terbaik dalam grid, sedangkan RandomizedSearchCV mungkin menemukan kombinasi mendekati optimal dengan waktu jauh lebih singkat.

**Contoh soal PG:**
> Dalam konteks evaluasi model klasifikasi, overfitting dapat diidentifikasi ketika:
> A. Training accuracy rendah dan validation accuracy rendah
> B. Training accuracy tinggi dan validation accuracy tinggi
> C. Training accuracy tinggi tetapi validation accuracy jauh lebih rendah
> D. Training accuracy rendah tetapi validation accuracy tinggi
>
> **Jawaban: C** — Overfitting terjadi ketika model terlalu "menghafal" data training sehingga tidak bisa generalize ke data baru, ditandai gap besar antara training dan validation performance.

---

## Contoh Soal Essay Analisis Kasus

> **Skenario:** Sebuah bank syariah di Indonesia ingin membangun model machine learning untuk memprediksi apakah nasabah akan gagal bayar (default) pada pembiayaan. Dataset yang tersedia berisi 10.000 nasabah dengan fitur: usia, penghasilan bulanan, jumlah pembiayaan, jenis pekerjaan (PNS/Swasta/Wiraswasta/Lainnya), tenor pinjaman, riwayat pembiayaan sebelumnya (lancar/macet), dan status default (ya/tidak). Dataset memiliki class imbalance: 92% lancar, 8% default.
>
> a. Identifikasi tipe data setiap fitur dan jelaskan preprocessing yang diperlukan. (8 poin)
> b. Rekomendasikan 2 algoritma yang cocok untuk masalah ini. Jelaskan alasan pemilihan masing-masing. (6 poin)
> c. Mengapa accuracy BUKAN metrik yang tepat untuk kasus ini? Metrik apa yang lebih relevan? Jelaskan. (6 poin)
> d. Sebagai mahasiswa yang menjunjung nilai amanah, bagaimana Anda memastikan model ini adil (fair) dan tidak mendiskriminasi kelompok tertentu? (5 poin)
> e. Jelaskan strategi yang dapat digunakan untuk menangani class imbalance pada dataset ini. (5 poin)

---

## Tips Menghadapi UTS

1. **Pahami konsep dasar setiap algoritma** — Fokus pada MENGAPA algoritma bekerja, bukan hanya BAGAIMANA memanggilnya di scikit-learn
2. **Kuasai preprocessing** — Banyak soal tentang data cleaning, scaling, encoding, dan feature engineering
3. **Latihan code tracing** — Biasakan membaca kode scikit-learn dan memprediksi output
4. **Hafal metrik evaluasi** — Pahami kapan menggunakan accuracy, precision, recall, F1-score, dan ROC-AUC
5. **Manajemen waktu** — 100 menit untuk 20 soal, rata-rata 5 menit per soal
6. **Jangan lupa konsep etika AI** — 2-3 soal PG tentang bias, fairness, responsible AI, dan nilai-nilai Islam dalam AI

---

*Kisi-kisi ini merupakan panduan cakupan materi. Soal ujian sebenarnya mungkin bervariasi dalam format dan tingkat kesulitan.*

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
