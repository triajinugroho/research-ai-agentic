# Minggu 8: UTS Review dan Ujian Tengah Semester

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 8 |
| **Topik** | UTS Review dan Ujian Tengah Semester |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK-1, CPMK-2, CPMK-3 |
| **Sub-CPMK** | Seluruh Sub-CPMK Minggu 1-7 |
| **Bloom's Taxonomy** | C2–C4 (Memahami–Menganalisis / *Understand–Analyze*) |
| **Durasi** | 2 x 100 menit (Review 100 min + Ujian 100 min) |
| **Platform** | Google Colab (untuk review), Closed-book Exam |
| **Metode** | Review interaktif, latihan soal, ujian tertulis |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Merangkum** seluruh konsep fondasi AI dan machine learning yang dipelajari pada Minggu 1-4.
2. **Mengintegrasikan** pemahaman tentang algoritma supervised learning dari Minggu 5-7.
3. **Menganalisis** permasalahan dan memilih algoritma yang tepat berdasarkan karakteristik data dan tujuan.
4. **Menyelesaikan** soal-soal UTS yang mencakup teori, perhitungan, dan analisis kritis.

---

## Materi Pembelajaran

### 1. Review Fase 1: Fondasi AI (Minggu 1-4)

#### Minggu 1: Pengantar AI dan Machine Learning

Konsep-konsep kunci yang harus dikuasai:

| Konsep | Penjelasan Singkat |
|---|---|
| **Artificial Intelligence** | Sistem komputer yang mampu melakukan tugas yang biasanya membutuhkan kecerdasan manusia |
| **Machine Learning** | Subset AI di mana komputer belajar dari data tanpa diprogram secara eksplisit |
| **Deep Learning** | Subset ML yang menggunakan neural networks berlapis |
| **AI Sempit vs AI Umum** | Narrow AI (khusus satu tugas) vs AGI (mampu semua tugas kognitif) |

Sejarah penting:
- 1956: Konferensi Dartmouth -- lahirnya istilah "Artificial Intelligence"
- 1997: Deep Blue mengalahkan Kasparov di catur
- 2016: AlphaGo mengalahkan juara dunia Go
- 2022: ChatGPT dirilis -- era AI generatif

Etika AI:
- Bias dalam data dan model
- Transparansi dan explainability
- Privasi data (UU PDP Indonesia)
- Nilai-nilai Islam: Amanah, Keadilan, Transparansi

#### Minggu 2: Jenis-jenis Machine Learning

```
Machine Learning
├── Supervised Learning (ada label)
│   ├── Klasifikasi (target: kategori)
│   └── Regresi (target: kontinu)
│
├── Unsupervised Learning (tanpa label)
│   ├── Clustering
│   └── Dimensionality Reduction
│
├── Semi-supervised Learning (sebagian label)
│
└── Reinforcement Learning (reward-based)
```

Perbedaan kunci:
- **Supervised**: data berlabel, ada target yang jelas → klasifikasi, regresi
- **Unsupervised**: tanpa label, mencari pola tersembunyi → clustering, PCA
- **Reinforcement**: belajar dari interaksi dengan lingkungan → game, robotik

#### Minggu 3: Data Preprocessing dan Feature Engineering

Langkah-langkah preprocessing:
1. **Handling missing values**: drop, imputation (mean, median, mode)
2. **Encoding**: Label Encoding (ordinal), One-Hot Encoding (nominal)
3. **Scaling**: StandardScaler (z-score), MinMaxScaler (0-1)
4. **Handling outliers**: IQR method, z-score > 3
5. **Feature selection**: korelasi, variance threshold

> **Ingat:** "Garbage in, garbage out" -- kualitas data menentukan kualitas model.

#### Minggu 4: Matematika untuk Machine Learning

Fondasi matematika yang dibutuhkan:
- **Aljabar Linear**: vektor, matriks, perkalian matriks
- **Kalkulus**: turunan, gradient, partial derivatives
- **Probabilitas**: distribusi, Bayes' theorem
- **Statistika**: mean, variance, korelasi

---

### 2. Review Fase 2: Supervised Learning (Minggu 5-7)

#### Minggu 5: Regresi Linear dan Logistik

| Topik | Ringkasan |
|---|---|
| **Simple Linear Regression** | y = mx + b; memodelkan hubungan linear satu fitur dengan target |
| **Multiple Linear Regression** | Y = Xβ; banyak fitur; interpretasi koefisien: perubahan y per unit x |
| **Cost Function (MSE)** | (1/n) Σ(yᵢ - ŷᵢ)²; mengukur error rata-rata kuadrat |
| **Gradient Descent** | Optimasi iteratif; learning rate mengontrol ukuran langkah |
| **Metrik Regresi** | MSE, RMSE, MAE, R² |
| **Logistic Regression** | Fungsi sigmoid σ(z) = 1/(1+e⁻ᶻ); klasifikasi biner |
| **Confusion Matrix** | TP, TN, FP, FN; Accuracy, Precision, Recall, F1-Score |

Rumus-rumus penting:

```
Regresi Linear: y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
Sigmoid       : σ(z) = 1 / (1 + e⁻ᶻ)
R² Score      : 1 - (SS_res / SS_tot)
Precision     : TP / (TP + FP)
Recall        : TP / (TP + FN)
F1-Score      : 2 × (Precision × Recall) / (Precision + Recall)
```

#### Minggu 6: Decision Tree dan Random Forest

| Topik | Ringkasan |
|---|---|
| **Decision Tree** | Pohon keputusan; memecah data berdasarkan fitur terbaik |
| **Entropy** | -Σ pᵢ × log₂(pᵢ); mengukur ketidakpastian |
| **Information Gain** | Pengurangan entropy setelah split |
| **Gini Impurity** | 1 - Σ pᵢ²; alternatif entropy yang lebih cepat |
| **Overfitting** | Pohon terlalu dalam menghafal data training |
| **Pruning** | Pre-pruning (max_depth) dan post-pruning |
| **Bagging** | Bootstrap Aggregating; sampling dengan pengembalian |
| **Random Forest** | Banyak pohon + random fitur; voting untuk prediksi |
| **Feature Importance** | Kontribusi fitur terhadap pengurangan impurity |

#### Minggu 7: SVM dan KNN

| Topik | Ringkasan |
|---|---|
| **KNN** | Lazy learner; prediksi berdasarkan K tetangga terdekat |
| **Distance Metrics** | Euclidean √(Σ(xᵢ-yᵢ)²), Manhattan Σ\|xᵢ-yᵢ\| |
| **SVM** | Mencari hyperplane dengan margin terbesar |
| **Support Vectors** | Titik data terdekat ke hyperplane |
| **Kernel Trick** | Proyeksi ke dimensi tinggi: linear, poly, RBF |
| **Cross-Validation** | K-fold, stratified k-fold; evaluasi lebih robust |
| **Pipeline** | Menggabungkan preprocessing dan model |
| **GridSearchCV** | Pencarian hyperparameter otomatis |

---

### 3. Kisi-kisi UTS

#### Distribusi Materi

| Fase | Minggu | Topik | Bobot |
|---|---|---|---|
| Fase 1 | 1-4 | Fondasi AI, jenis ML, preprocessing, matematika | 40% |
| Fase 2 | 5-7 | Regresi, Decision Tree, Random Forest, SVM, KNN | 60% |

#### Tipe Soal

| Tipe | Jumlah | Bobot | Level Bloom |
|---|---|---|---|
| Pilihan Ganda | 20 soal | 40% | C2-C3 |
| Isian Singkat / Perhitungan | 5 soal | 25% | C3-C4 |
| Esai Analitis | 3 soal | 35% | C4 |

#### Topik yang Wajib Dikuasai

1. Perbedaan supervised vs unsupervised learning
2. Langkah-langkah data preprocessing
3. Rumus dan interpretasi MSE, RMSE, R², MAE
4. Konsep gradient descent dan learning rate
5. Perbedaan regresi linear vs logistic regression
6. Confusion matrix: menghitung accuracy, precision, recall, F1
7. Entropy, information gain, Gini impurity
8. Perbedaan Decision Tree vs Random Forest
9. Konsep KNN: pemilihan K, normalisasi, distance metrics
10. Konsep SVM: hyperplane, margin, kernel
11. Cross-validation: k-fold, stratified
12. Kapan menggunakan algoritma tertentu (pemilihan model)

---

### 4. Contoh Soal dan Pembahasan

#### Soal 1: Pilihan Ganda (C2)

**Manakah yang merupakan perbedaan utama antara supervised learning dan unsupervised learning?**

A. Supervised learning lebih cepat daripada unsupervised learning
B. Supervised learning menggunakan data berlabel, unsupervised learning tidak
C. Unsupervised learning hanya bisa digunakan untuk klasifikasi
D. Supervised learning tidak membutuhkan data training

**Jawaban:** B

**Pembahasan:** Supervised learning membutuhkan data yang sudah diberi label (target/output yang diketahui), sedangkan unsupervised learning mencari pola dari data tanpa label.

---

#### Soal 2: Perhitungan (C3)

**Diberikan hasil prediksi model klasifikasi sebagai berikut:**

| | Prediksi: Positif | Prediksi: Negatif |
|---|---|---|
| **Aktual: Positif** | 45 | 5 |
| **Aktual: Negatif** | 10 | 40 |

**Hitunglah: (a) Accuracy, (b) Precision, (c) Recall, (d) F1-Score**

**Pembahasan:**

```
TP = 45, FN = 5, FP = 10, TN = 40, Total = 100

(a) Accuracy  = (TP + TN) / Total = (45 + 40) / 100 = 0.85 = 85%
(b) Precision = TP / (TP + FP) = 45 / (45 + 10) = 45/55 = 0.818 = 81.8%
(c) Recall    = TP / (TP + FN) = 45 / (45 + 5) = 45/50 = 0.90 = 90%
(d) F1-Score  = 2 × (0.818 × 0.90) / (0.818 + 0.90) = 2 × 0.736 / 1.718 = 0.857 = 85.7%
```

---

#### Soal 3: Perhitungan Entropy (C3)

**Sebuah dataset memiliki 10 sampel: 6 Kelas A dan 4 Kelas B. Hitunglah entropy dataset tersebut.**

**Pembahasan:**

```
p(A) = 6/10 = 0.6
p(B) = 4/10 = 0.4

Entropy = -Σ pᵢ × log₂(pᵢ)
        = -(0.6 × log₂(0.6) + 0.4 × log₂(0.4))
        = -(0.6 × (-0.737) + 0.4 × (-1.322))
        = -(−0.442 + (−0.529))
        = -(-0.971)
        = 0.971
```

Entropy mendekati 1.0, menunjukkan data cukup campuran (tidak murni satu kelas).

---

#### Soal 4: Esai Analitis (C4)

**Anda diminta membangun model prediksi untuk menentukan apakah seorang nasabah bank akan melakukan churn (berhenti menjadi nasabah) atau tidak. Dataset memiliki 10.000 baris dan 15 fitur numerik. Jawablah:**

**(a)** Jelaskan 3 langkah preprocessing yang perlu dilakukan.
**(b)** Rekomendasikan 2 algoritma yang paling cocok beserta alasannya.
**(c)** Jelaskan metrik evaluasi yang paling penting dan mengapa.

**Pembahasan:**

**(a) Preprocessing:**
1. **Handling missing values** -- cek dan isi nilai yang hilang (imputasi median/mean untuk numerik).
2. **Feature scaling** -- normalisasi fitur agar semua berada pada skala yang sama (penting untuk KNN dan SVM).
3. **Handling class imbalance** -- jika distribusi churn tidak seimbang, gunakan SMOTE, undersampling, atau class weight.

**(b) Rekomendasi algoritma:**
1. **Random Forest** -- akurasi tinggi, mampu menangani fitur banyak, memberikan feature importance untuk insight bisnis.
2. **Logistic Regression** -- interpretable, koefisien menunjukkan kontribusi setiap fitur, cocok untuk regulasi perbankan yang membutuhkan transparansi model.

**(c) Metrik evaluasi:**
**Recall** paling penting karena biaya *false negative* (nasabah churn tidak terdeteksi) lebih tinggi daripada *false positive*. Bank kehilangan nasabah yang sebenarnya bisa dipertahankan. F1-Score juga penting sebagai keseimbangan antara precision dan recall.

---

### 5. Tips Menghadapi UTS

#### Persiapan Sebelum Ujian

1. **Review materi secara bertahap** -- jangan belajar semalam suntuk (*cramming*)
2. **Buat ringkasan rumus** -- tulis di satu halaman semua rumus penting
3. **Latihan soal** -- kerjakan contoh soal di atas dan dari setiap modul
4. **Pahami konsep, bukan menghafal** -- UTS menguji pemahaman, bukan hafalan
5. **Diskusi dengan teman** -- jelaskan konsep ke teman untuk memperdalam pemahaman

#### Strategi Saat Ujian

1. **Baca semua soal terlebih dahulu** -- alokasikan waktu untuk setiap bagian
2. **Kerjakan soal yang paling yakin** terlebih dahulu
3. **Tunjukkan proses perhitungan** -- jawaban benar tanpa proses tidak mendapat nilai penuh
4. **Untuk soal esai**: gunakan struktur yang jelas (poin-poin, bukan paragraf panjang)
5. **Periksa kembali** jawaban sebelum mengumpulkan

#### Aturan Ujian

| Aturan | Keterangan |
|---|---|
| **Sifat ujian** | Closed-book (buku tertutup) |
| **AI tools** | **TIDAK DIPERBOLEHKAN** -- tidak boleh menggunakan ChatGPT, Claude, atau AI lainnya |
| **Kalkulator** | Diperbolehkan (kalkulator scientific) |
| **Durasi** | 100 menit |
| **Alat tulis** | Bolpen, pensil, penghapus |

---

## Aktivitas Kelas

### Sesi 1: Review Interaktif (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Pembukaan | Outline review, distribusi materi, tanya jawab awal |
| 20 menit | Review Fase 1 | Fondasi AI, jenis ML, preprocessing, matematika dasar |
| 30 menit | Review Fase 2 | Supervised learning: regresi, tree, ensemble, SVM, KNN |
| 20 menit | Latihan Soal | Mengerjakan contoh soal bersama-sama, pembahasan |
| 10 menit | Kisi-kisi & Tips | Distribusi topik, tips menghadapi UTS |
| 10 menit | Tanya Jawab Terakhir | Sesi terakhir bertanya sebelum ujian |

### Sesi 2: Ujian Tengah Semester (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 5 menit | Distribusi Soal | Pembagian lembar soal dan lembar jawaban |
| 90 menit | Pengerjaan UTS | Ujian tertulis closed-book |
| 5 menit | Pengumpulan | Pengumpulan lembar jawaban |

---

## AI Corner: Mengapa AI Tidak Boleh Digunakan Saat UTS

> **Level Khusus** -- Refleksi tentang integritas akademik dan peran AI dalam pembelajaran.

### Mengapa UTS Harus Tanpa AI?

1. **Mengukur pemahaman sejati**: UTS bertujuan mengukur apa yang sudah Anda pahami dan internalisasi, bukan kemampuan Anda menggunakan tools.

2. **Membangun fondasi kognitif**: Kemampuan menghitung MSE, menjelaskan gradient descent, atau menganalisis confusion matrix secara mandiri adalah fondasi yang dibutuhkan untuk menjadi praktisi ML yang kompeten.

3. **Integritas akademik (Amanah)**: Sebagai mahasiswa di universitas yang menjunjung nilai Islam, mengerjakan ujian secara jujur adalah bentuk amanah -- kepercayaan yang diberikan dosen dan institusi.

4. **Persiapan dunia kerja**: Dalam wawancara kerja, Anda akan ditanya konsep-konsep ini secara langsung tanpa bantuan AI. Pemahaman yang kuat sekarang akan membantu karir Anda di masa depan.

### AI Sebagai Partner Belajar, Bukan Pengganti Berpikir

```
Penggunaan AI yang BENAR (sebelum UTS):
  ✓ Minta AI menjelaskan konsep yang belum dipahami
  ✓ Minta AI membuat soal latihan tambahan
  ✓ Gunakan AI untuk verifikasi pemahaman Anda

Penggunaan AI yang SALAH (saat UTS):
  ✗ Membuka ChatGPT/Claude saat ujian berlangsung
  ✗ Menggunakan AI untuk menjawab soal ujian
  ✗ Meminta bantuan AI melalui perangkat tersembunyi
```

### Sanksi Pelanggaran

Penggunaan AI atau alat bantu tidak sah selama UTS merupakan pelanggaran integritas akademik yang serius dan akan ditindak sesuai peraturan universitas.

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai persiapan UTS:

1. **Peta Konsep:** Buatlah peta konsep (mind map) yang menghubungkan seluruh topik dari Minggu 1-7. Tunjukkan hubungan antara preprocessing, algoritma, dan evaluasi.

2. **Skenario Pemilihan Model:** Diberikan tiga skenario berikut, algoritma apa yang Anda pilih dan mengapa?
   - Prediksi harga saham perusahaan di BEI
   - Klasifikasi email spam vs bukan spam
   - Segmentasi pelanggan e-commerce Indonesia

3. **Refleksi Pembelajaran:** Dari seluruh materi Minggu 1-7, konsep mana yang paling sulit dipahami? Strategi apa yang Anda gunakan untuk memahaminya?

---

## Referensi

### Buku Teks

1. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer.
2. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
3. Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

### Sumber Online

4. [scikit-learn Documentation](https://scikit-learn.org/stable/) -- Referensi utama untuk semua algoritma.
5. [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) -- Tutorial gratis dari Google.
6. [Kaggle Learn](https://www.kaggle.com/learn) -- Tutorial interaktif ML.

---

> **Preview Minggu Depan:** Setelah UTS, kita akan memasuki **Fase 3: Unsupervised Learning** dimulai dengan **Clustering (K-Means dan Hierarchical Clustering)** -- teknik untuk menemukan pola tersembunyi dalam data tanpa label.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
