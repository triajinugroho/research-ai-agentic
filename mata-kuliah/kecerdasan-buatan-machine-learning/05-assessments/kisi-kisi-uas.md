# Kisi-Kisi Ujian Akhir Semester (UAS)

## Mata Kuliah: Kecerdasan Buatan dan Machine Learning (IF3XXX, 4 SKS)
### Prodi Informatika — UAI — Semester Ganjil 2026/2027
### Dosen Pengampu: Tri Aji Nugroho, S.T., M.T.

---

## Informasi Umum

| Komponen | Detail |
|----------|--------|
| **Waktu** | Minggu 16, 120 menit |
| **Format** | Closed-book + 1 lembar A4 catatan pribadi (ditulis tangan, boleh bolak-balik) |
| **Cakupan** | Utama: Minggu 9-14 (CPMK 4-7); Komprehensif: CPMK 1-7 |
| **Bobot** | 25% dari nilai akhir |
| **Alat yang diizinkan** | Kalkulator non-programmable, 1 lembar catatan A4, alat tulis |

---

## Distribusi Soal

| Tipe Soal | Jumlah | Bobot | Bloom's |
|-----------|--------|-------|---------|
| Pilihan Ganda (PG) | 10 soal @ 1.5 poin | 15% | C2-C4 |
| Short Answer | 4 soal @ 5 poin | 20% | C3-C5 |
| Code Tracing / Interpretasi Output | 2-3 soal @ ~10 poin | 25% | C4-C5 |
| Tulis Kode | 2-3 soal @ ~10 poin | 25% | C4-C5 |
| Essay Desain Pipeline ML | 1-2 soal @ ~7.5 poin | 15% | C5-C6 |

---

## Kisi-Kisi Detail per Topik

### Minggu 9: Unsupervised Learning — Clustering (CPMK-4)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Menerapkan K-Means clustering dan memilih jumlah cluster optimal (Elbow, Silhouette) | C3-C4 | Code Tracing/Tulis Kode |
| Menerapkan hierarchical clustering dan menginterpretasi dendrogram | C4 | Interpretasi/Short Answer |
| Membedakan K-Means, hierarchical clustering, dan DBSCAN | C4 | PG |
| Mengevaluasi kualitas clustering menggunakan Silhouette score | C4 | Code Tracing |

**Contoh soal Interpretasi Output:**
> Diberikan output Elbow method dan Silhouette score untuk K-Means clustering pada data pelanggan e-commerce Indonesia:
> ```
> K=2: Inertia=15000, Silhouette=0.45
> K=3: Inertia=9500,  Silhouette=0.62
> K=4: Inertia=7800,  Silhouette=0.58
> K=5: Inertia=7200,  Silhouette=0.42
> K=6: Inertia=6900,  Silhouette=0.38
> ```
>
> a. Berdasarkan Elbow method, berapa jumlah cluster optimal? Jelaskan. (4 poin)
> b. Berdasarkan Silhouette score, berapa jumlah cluster optimal? Jelaskan. (3 poin)
> c. Jika kedua metode memberikan hasil berbeda, mana yang Anda pilih dan mengapa? (3 poin)
>
> **Jawaban:**
> a. Dari Elbow method, penurunan inertia melambat signifikan setelah K=3 (dari 15000→9500→7800→7200→6900). "Siku" terlihat pada K=3 karena marginal decrease mulai menurun drastis.
> b. Silhouette score tertinggi adalah pada K=3 (0.62), menandakan cluster dengan K=3 paling compact dan well-separated.
> c. Kedua metode menunjuk ke K=3. Dalam kasus di mana keduanya berbeda, Silhouette score umumnya lebih reliable karena mempertimbangkan baik cohesion (intra-cluster) maupun separation (inter-cluster), bukan hanya intra-cluster distance seperti inertia.

---

### Minggu 10: Reduksi Dimensi dan Feature Selection (CPMK-4)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Menerapkan PCA dan menginterpretasi explained variance ratio | C4 | Code Tracing/Interpretasi |
| Memilih jumlah komponen PCA berdasarkan scree plot dan cumulative variance | C4 | PG/Short Answer |
| Membedakan feature selection (filter, wrapper, embedded) dan feature extraction (PCA) | C4 | PG |
| Menjelaskan curse of dimensionality dan relevansinya untuk ML | C3 | PG/Short Answer |

**Contoh soal PG:**
> Setelah menerapkan PCA pada dataset dengan 20 fitur, diperoleh explained variance ratio sebagai berikut: PC1=0.35, PC2=0.25, PC3=0.15, PC4=0.08, PC5=0.05, sisanya <0.03. Jika threshold cumulative variance yang diinginkan adalah 80%, berapa komponen minimal yang diperlukan?
> A. 2 komponen (cumulative: 60%)
> B. 3 komponen (cumulative: 75%)
> C. 4 komponen (cumulative: 83%)
> D. 5 komponen (cumulative: 88%)
>
> **Jawaban: C** — Cumulative variance: PC1=35%, PC1+PC2=60%, PC1-PC3=75%, PC1-PC4=83%. Dengan 4 komponen, cumulative variance mencapai 83% yang melewati threshold 80%.

---

### Minggu 11: Neural Network dan Deep Learning Dasar (CPMK-5)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Membangun neural network sederhana (MLP) dengan TensorFlow/Keras | C3 | Tulis Kode |
| Menjelaskan mekanisme forward propagation dan backpropagation secara intuitif | C2-C3 | Short Answer/PG |
| Memilih activation function yang tepat (Sigmoid, ReLU, Tanh, Softmax) untuk kasus tertentu | C3-C4 | PG |
| Mengidentifikasi overfitting pada neural network dan menerapkan teknik regularisasi (dropout, early stopping) | C4 | Interpretasi/PG |

**Contoh soal PG:**
> Untuk layer output pada masalah klasifikasi multi-class dengan 5 kategori, kombinasi activation function dan loss function yang paling tepat adalah:
> A. Sigmoid + binary_crossentropy
> B. ReLU + mean_squared_error
> C. Softmax + categorical_crossentropy
> D. Tanh + sparse_categorical_crossentropy
>
> **Jawaban: C** — Softmax menghasilkan distribusi probabilitas yang totalnya 1.0 untuk setiap kelas, cocok untuk multi-class classification. `categorical_crossentropy` adalah loss function standar untuk multi-class classification dengan one-hot encoded labels.

**Contoh soal Short Answer:**
> Jelaskan proses backpropagation pada neural network. Mengapa dibutuhkan fungsi aktivasi non-linear? (5 poin)
>
> **Jawaban:**
> - **Backpropagation:** Setelah forward pass menghitung prediksi dan loss, backpropagation menghitung gradien loss terhadap setiap weight menggunakan chain rule. Gradien ini digunakan untuk memperbarui weight (gradient descent) agar loss berkurang.
> - **Fungsi aktivasi non-linear:** Tanpa non-linearitas, jaringan multi-layer hanya ekuivalen dengan satu transformasi linear (komposisi fungsi linear = fungsi linear). Fungsi non-linear (ReLU, sigmoid, tanh) memungkinkan network mempelajari hubungan non-linear yang kompleks dalam data.

---

### Minggu 12: Natural Language Processing (NLP) Dasar (CPMK-6)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Menerapkan text preprocessing untuk teks bahasa Indonesia (tokenisasi, stopword removal, stemming Sastrawi) | C3 | Code Tracing/Tulis Kode |
| Membangun pipeline klasifikasi teks: TF-IDF + classifier | C3-C4 | Tulis Kode |
| Menjelaskan perbedaan Bag of Words dan TF-IDF | C2-C3 | PG |
| Mengevaluasi model klasifikasi teks dengan metrik per kelas | C4 | Interpretasi |

**Contoh soal Code Tracing:**
> Perhatikan kode NLP berikut. Tentukan output yang dihasilkan. (10 poin)
>
> ```python
> from sklearn.feature_extraction.text import TfidfVectorizer
>
> corpus = [
>     "machine learning adalah cabang AI",
>     "deep learning bagian dari machine learning",
>     "AI membantu analisis data"
> ]
>
> vectorizer = TfidfVectorizer()
> X = vectorizer.fit_transform(corpus)
>
> print(f"Shape matrix TF-IDF: {X.shape}")
> print(f"Jumlah dokumen: {X.shape[0]}")
> print(f"Jumlah kata unik: {X.shape[1]}")
> ```
>
> **Jawaban:**
> ```
> Shape matrix TF-IDF: (3, 11)
> Jumlah dokumen: 3
> Jumlah kata unik: 11
> ```
>
> **Penjelasan:**
> - 3 dokumen dalam corpus menghasilkan 3 baris.
> - TfidfVectorizer melakukan tokenization dan menghitung TF-IDF untuk setiap kata unik.
> - Kata-kata unik: "machine", "learning", "adalah", "cabang", "ai", "deep", "bagian", "dari", "membantu", "analisis", "data" = 11 kata unik.
> - Shape matrix menunjukkan (jumlah dokumen, jumlah kata unik).

**Contoh soal PG:**
> Dalam TF-IDF, kata yang memiliki TF-IDF score tinggi berarti:
> A. Kata tersebut muncul di hampir semua dokumen
> B. Kata tersebut sering muncul dalam satu dokumen tetapi jarang di dokumen lain
> C. Kata tersebut adalah stopword yang umum
> D. Kata tersebut hanya muncul 1 kali di seluruh corpus
>
> **Jawaban: B** — TF-IDF menggabungkan term frequency (frekuensi dalam satu dokumen) dengan inverse document frequency (kebalikan frekuensi di seluruh dokumen). Kata yang sering di satu dokumen tapi jarang di dokumen lain mendapat skor tinggi karena kata tersebut paling diskriminatif.

---

### Minggu 13: Computer Vision Dasar dan CNN (CPMK-6)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Menerapkan image processing dasar dengan OpenCV (resize, grayscale, augmentation) | C3 | Code Tracing/Tulis Kode |
| Membangun model CNN sederhana dengan Keras (Conv2D, MaxPooling2D, Dense) | C3-C4 | Tulis Kode |
| Menjelaskan konsep konvolusi, filter/kernel, pooling, dan stride | C2-C3 | PG/Short Answer |
| Menjelaskan konsep transfer learning dan manfaatnya | C3 | PG |

**Contoh soal Short Answer:**
> Jelaskan apa yang terjadi pada setiap langkah berikut dalam arsitektur CNN dan apa tujuannya:
> 1. Convolutional Layer (Conv2D)
> 2. Max Pooling Layer
> 3. Flatten Layer
> 4. Dense Layer (output)
>
> (5 poin)
>
> **Jawaban:**
> 1. **Conv2D:** Menerapkan filter/kernel pada gambar input untuk mengekstrak fitur lokal (edge, texture, pattern). Filter bergeser di seluruh gambar menghasilkan feature maps. Tujuan: mendeteksi fitur visual secara hierarkis.
> 2. **Max Pooling:** Mengambil nilai maksimum dari setiap window (misal 2x2) untuk mengurangi ukuran feature map. Tujuan: mengurangi dimensi, mengurangi komputasi, dan membuat model lebih robust terhadap pergeseran posisi fitur.
> 3. **Flatten:** Mengubah feature maps 2D menjadi vektor 1D. Tujuan: menyiapkan data untuk input ke fully connected layer.
> 4. **Dense (output):** Fully connected layer yang menghasilkan probabilitas untuk setiap kelas. Tujuan: klasifikasi akhir berdasarkan fitur yang diekstrak oleh layer sebelumnya.

**Contoh soal PG:**
> Transfer learning bermanfaat dalam computer vision karena:
> A. Model pre-trained sudah menghafal dataset baru kita
> B. Layer awal CNN pre-trained telah belajar mendeteksi fitur umum (edge, texture) yang berguna untuk berbagai tugas vision
> C. Transfer learning menghilangkan kebutuhan data training sama sekali
> D. Pre-trained model selalu menghasilkan akurasi 100%
>
> **Jawaban: B** — Layer awal CNN belajar fitur generik (edge, corner, texture) yang berguna untuk hampir semua tugas vision. Transfer learning memanfaatkan fitur ini dan hanya perlu melatih ulang layer akhir untuk tugas spesifik, menghemat waktu training dan data.

---

### Minggu 14: AI sebagai Co-Developer dan Pengantar MLOps (CPMK-7)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Menjelaskan workflow AI-augmented development: human design → AI draft → human review → iterate | C5 | Essay/PG |
| Mengevaluasi output AI dan mengidentifikasi kapan AI membantu vs menyesatkan | C5 | Essay/PG |
| Menjelaskan konsep ML lifecycle dan MLOps dasar (versioning, experiment tracking, deployment) | C2-C3 | PG/Short Answer |
| Menjelaskan prinsip reproducibility dalam ML pipeline | C3 | PG |

**Contoh soal PG:**
> Seorang mahasiswa menggunakan ChatGPT untuk membangun model klasifikasi. AI menyarankan menggunakan deep neural network dengan 10 hidden layers untuk dataset yang hanya memiliki 200 sampel dan 5 fitur. Respons yang paling tepat adalah:
> A. Ikuti saran AI karena deep network selalu lebih baik
> B. Model terlalu kompleks untuk dataset kecil — kemungkinan besar overfitting. Model sederhana (logistic regression, decision tree) lebih tepat
> C. Tambahkan lebih banyak hidden layers agar model lebih akurat
> D. Abaikan semua saran AI dan tidak menggunakan AI sama sekali
>
> **Jawaban: B** — Untuk dataset kecil (200 sampel, 5 fitur), model sederhana lebih tepat. Deep neural network dengan 10 hidden layers memiliki terlalu banyak parameter dan hampir pasti overfitting. Ini contoh pentingnya critical evaluation terhadap output AI.

---

## Soal Komprehensif (dari Materi UTS)

UAS juga mencakup konsep dari Minggu 1-7 secara tersirat, khususnya:
- Konsep dasar AI dan etika (dalam konteks essay desain pipeline)
- Preprocessing dan feature engineering (sebagai bagian pipeline ML end-to-end)
- Supervised learning algorithms (perbandingan dengan unsupervised dan deep learning)
- Evaluasi model (metrik klasifikasi, confusion matrix — diterapkan pada NLP dan CV)
- Bias-variance tradeoff (dalam konteks neural network dan model selection)

---

## Contoh Soal Tulis Kode

**Contoh Soal 1:**
> Tuliskan kode Python lengkap untuk melakukan K-Means clustering pada dataset, menentukan jumlah cluster optimal menggunakan elbow method, dan menghitung silhouette score. Asumsikan data `X` sudah tersedia dan sudah di-scaling. (10 poin)
>
> **Jawaban:**
> ```python
> from sklearn.cluster import KMeans
> from sklearn.metrics import silhouette_score
> import matplotlib.pyplot as plt
>
> # Elbow method - mencari k optimal
> inertias = []
> sil_scores = []
> K_range = range(2, 11)
>
> for k in K_range:
>     kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
>     kmeans.fit(X)
>     inertias.append(kmeans.inertia_)
>     sil_scores.append(silhouette_score(X, kmeans.labels_))
>
> # Plot Elbow
> plt.figure(figsize=(12, 4))
> plt.subplot(1, 2, 1)
> plt.plot(K_range, inertias, 'bo-')
> plt.xlabel('Jumlah Cluster (k)')
> plt.ylabel('Inertia')
> plt.title('Elbow Method')
>
> # Plot Silhouette Score
> plt.subplot(1, 2, 2)
> plt.plot(K_range, sil_scores, 'ro-')
> plt.xlabel('Jumlah Cluster (k)')
> plt.ylabel('Silhouette Score')
> plt.title('Silhouette Score per k')
> plt.tight_layout()
> plt.show()
>
> # Pilih k optimal dan tampilkan hasil
> k_optimal = list(K_range)[sil_scores.index(max(sil_scores))]
> print(f"K optimal berdasarkan silhouette: {k_optimal}")
> print(f"Silhouette score: {max(sil_scores):.4f}")
> ```

**Contoh Soal 2:**
> Tuliskan kode Python untuk membangun model MLP dengan TensorFlow/Keras untuk klasifikasi 3 kelas. Arsitektur: input 10 fitur → hidden 64 neurons (ReLU) → dropout 0.3 → hidden 32 neurons (ReLU) → output 3 kelas. Gunakan optimizer Adam dan train selama 50 epochs. (10 poin)
>
> **Jawaban:**
> ```python
> import tensorflow as tf
> from tensorflow.keras.models import Sequential
> from tensorflow.keras.layers import Dense, Dropout
>
> # Membangun model MLP
> model = Sequential([
>     Dense(64, activation='relu', input_shape=(10,)),
>     Dropout(0.3),
>     Dense(32, activation='relu'),
>     Dense(3, activation='softmax')
> ])
>
> # Compile model
> model.compile(
>     optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
>     loss='categorical_crossentropy',
>     metrics=['accuracy']
> )
>
> # Training model
> history = model.fit(
>     X_train, y_train,
>     epochs=50,
>     batch_size=32,
>     validation_split=0.2
> )
> ```

---

## Contoh Soal Essay Desain Pipeline ML (15%)

> **Skenario:** Kementerian Pertanian Indonesia ingin membangun sistem AI untuk mendeteksi penyakit tanaman padi dari foto daun yang diambil petani menggunakan smartphone. Sistem harus mampu mengklasifikasikan foto ke dalam 4 kategori: sehat, blas, tungro, dan hawar daun bakteri. Dataset yang tersedia berisi 5.000 gambar (1.500 sehat, 1.200 blas, 1.300 tungro, 1.000 hawar) dengan resolusi bervariasi.
>
> Sebagai data scientist, desain pipeline ML end-to-end:
>
> a. Jelaskan preprocessing yang diperlukan untuk data gambar ini. (5 poin)
> b. Rekomendasikan arsitektur model (CNN from scratch vs transfer learning). Jelaskan keputusan desain Anda, termasuk alasan pemilihan. (5 poin)
> c. Metrik evaluasi apa yang paling relevan untuk kasus ini? Mengapa accuracy saja tidak cukup? (4 poin)
> d. Bagaimana Anda akan menggunakan AI (ChatGPT/Claude/Copilot) sebagai co-developer dalam proyek ini? Berikan 2 contoh prompt spesifik. (4 poin)
> e. Jelaskan 2 tantangan deployment model ini di lapangan (petani di desa) dan solusi yang mungkin. (4 poin)
> f. Dari perspektif etika AI dan nilai Islam (kemaslahatan/maslahah), apa dampak positif dan potensi risiko dari sistem ini? (3 poin)
>
> **Jawaban:**
> a. **Preprocessing gambar:**
>    - Resize semua gambar ke ukuran seragam (misal 224x224 pixel)
>    - Normalisasi pixel values ke range [0, 1] (bagi dengan 255)
>    - Data augmentation: flip horizontal, rotasi (±15°), zoom (0.8-1.2), brightness adjustment — untuk menambah variasi data training
>    - Train-test-validation split: 70-15-15 (stratified)
>
> b. **Rekomendasi arsitektur:** Transfer learning dengan VGG16 atau ResNet50.
>    - Dataset 5.000 gambar termasuk moderat — cukup untuk fine-tuning tapi kurang untuk CNN from scratch yang kompleks
>    - Pre-trained model sudah belajar fitur visual generik (edge, texture, shape) dari ImageNet
>    - Cukup freeze base layers dan train ulang top layers (classifier) untuk adaptasi ke domain penyakit padi
>    - Alternatif: CNN sederhana (3-4 conv layers) from scratch sebagai baseline untuk perbandingan
>
> c. **Metrik evaluasi:**
>    - Accuracy tidak cukup karena dataset sedikit imbalanced (1000-1500 per kelas)
>    - Gunakan precision, recall, F1-score per kelas — penting bahwa setiap penyakit terdeteksi dengan baik
>    - Recall untuk penyakit sangat penting (jangan sampai penyakit terlewat/false negative)
>    - Confusion matrix untuk melihat pola misklasifikasi antar jenis penyakit
>
> d. **Penggunaan AI sebagai co-developer:**
>    - Prompt 1: "Buatkan kode Python untuk membangun pipeline image classification menggunakan transfer learning VGG16 di Keras. Dataset berisi 4 kategori gambar (sehat, blas, tungro, hawar) dengan data augmentation."
>    - Prompt 2: "Saya mendapat validation accuracy 75% pada model CNN klasifikasi penyakit padi. Training accuracy 95%. Bagaimana cara mengatasi overfitting ini?"
>
> e. **Tantangan deployment:**
>    1. **Koneksi internet terbatas di desa:** Solusi — model harus bisa berjalan offline di smartphone (TensorFlow Lite/ONNX), ukuran model harus kecil (quantization)
>    2. **Kualitas foto bervariasi:** Solusi — model harus robust terhadap variasi pencahayaan dan sudut pengambilan (augmentation yang ekstensif saat training), plus panduan pengambilan foto yang jelas
>
> f. **Perspektif etika dan Islam:**
>    - **Dampak positif (kemaslahatan):** Membantu petani mendeteksi penyakit lebih awal sehingga hasil panen meningkat dan ketahanan pangan terjaga — sejalan dengan prinsip kemanfaatan (maslahah) dan menjaga kehidupan (hifz al-nafs)
>    - **Potensi risiko:** Jika model salah diagnosis dan petani memberikan obat yang salah, bisa merusak tanaman. Solusi: model memberikan confidence score dan menyarankan konsultasi dengan penyuluh pertanian jika confidence rendah

---

## Tips Menghadapi UAS

1. **Buat lembar catatan yang efektif** — Fokuskan pada arsitektur model (CNN layers, hyperparameters), decision tree pemilihan algoritma, dan rumus metrik evaluasi
2. **Latihan interpretasi output** — Banyak soal tentang membaca output clustering, PCA, neural network training, dan classification report
3. **Pahami "kapan pakai apa"** — Decision tree: tipe data + tujuan analisis + ukuran dataset → algoritma yang tepat
4. **Siapkan untuk essay desain** — Latih berpikir pipeline: data → preprocessing → model → evaluasi → deployment → etika
5. **Review konsep UTS** — Fondasi supervised learning tetap penting, terutama evaluasi model dan preprocessing
6. **Jangan hanya hafal API** — UAS menguji kemampuan menerapkan, menganalisis, dan mengevaluasi, bukan menghafal `model.fit()`

### Decision Tree untuk Lembar Catatan

```
Tujuan Analisis
├── Prediksi (Supervised Learning)
│   ├── Target numerik → Regresi Linear / Ridge / Lasso
│   └── Target kategorikal → Klasifikasi
│       ├── Data kecil + interpretatif → Decision Tree / Logistic Regression
│       ├── Data sedang + performa tinggi → Random Forest / SVM / KNN
│       └── Data besar + kompleks → Neural Network / Deep Learning
├── Menemukan pola (Unsupervised Learning)
│   ├── Grouping → Clustering
│   │   ├── Jumlah cluster diketahui → K-Means
│   │   ├── Hierarki diperlukan → Hierarchical Clustering
│   │   └── Cluster tidak beraturan + noise → DBSCAN
│   └── Reduksi dimensi → PCA / t-SNE / UMAP
├── Data teks → NLP Pipeline
│   └── Preprocessing → TF-IDF → Naive Bayes / SVM / Logistic Regression
└── Data gambar → Computer Vision
    ├── Dataset kecil → Transfer Learning (VGG16, ResNet)
    └── Dataset besar → CNN from scratch
```

---

*Kisi-kisi ini merupakan panduan cakupan materi. Soal ujian sebenarnya mungkin bervariasi dalam format dan tingkat kesulitan.*

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
