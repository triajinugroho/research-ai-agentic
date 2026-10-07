# Minggu 16: UAS Review dan Ujian

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 16 |
| **Topik** | UAS Review dan Ujian Akhir Semester |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK 1-7: Evaluasi komprehensif seluruh capaian pembelajaran |
| **Sub-CPMK** | 16.1 Mengintegrasikan seluruh konsep AI/ML yang dipelajari selama semester |
| | 16.2 Menerapkan kemampuan analisis dan evaluasi dalam penyelesaian soal komprehensif |
| **Bloom's Taxonomy** | C4-C6 (Menganalisis-Mencipta / *Analyze-Create*) |
| **Durasi** | 2 x 100 menit (Review 100 min + Ujian 100 min) |
| **Platform** | Google Colab (review), Paper-based (ujian) |
| **Metode** | Review interaktif, latihan soal, diskusi, ujian tertulis |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Mengintegrasikan** seluruh konsep AI dan machine learning yang dipelajari dari Minggu 1 hingga Minggu 15.
2. **Menganalisis** hubungan antar topik dan menerapkannya pada permasalahan baru.
3. **Mengevaluasi** pendekatan yang tepat untuk berbagai jenis permasalahan ML.
4. **Menyelesaikan** soal-soal ujian komprehensif yang menguji pemahaman konseptual dan kemampuan aplikasi.

---

## Materi Pembelajaran

### 1. Review Fase 3: Advanced ML (Minggu 9-12)

#### Clustering Algorithms (Minggu 9-10)

| Konsep Kunci | Deskripsi | Yang Harus Dikuasai |
|---|---|---|
| **K-Means** | Partitioning clustering, minimasi inertia | Cara kerja iteratif, pemilihan K (elbow method, silhouette) |
| **Hierarchical Clustering** | Agglomerative/divisive, dendrogram | Linkage methods (single, complete, average, ward) |
| **DBSCAN** | Density-based, mendeteksi outlier | Konsep eps dan min_samples, noise points |
| **Evaluasi Clustering** | Metrik internal dan eksternal | Silhouette score, Davies-Bouldin, ARI |

```
Pemilihan Algoritma Clustering
├── Data terstruktur, jumlah cluster diketahui → K-Means
├── Ingin melihat hierarki hubungan data    → Hierarchical
├── Data memiliki bentuk non-spherical      → DBSCAN
└── Data sangat besar                        → Mini-batch K-Means
```

#### PCA & Feature Selection (Minggu 10)

| Konsep | Poin Penting |
|---|---|
| **PCA** | Reduksi dimensi, explained variance ratio, memilih jumlah komponen |
| **Feature Importance** | Dari model (Random Forest), korelasi, mutual information |
| **Curse of Dimensionality** | Mengapa terlalu banyak fitur bisa merugikan performa model |

#### Neural Networks & Deep Learning (Minggu 11-12)

| Konsep | Poin Penting |
|---|---|
| **Perceptron** | Unit dasar neural network, weighted sum + activation |
| **Arsitektur MLP** | Input layer, hidden layers, output layer |
| **Backpropagation** | Cara model belajar: forward pass, loss, backward pass, update weights |
| **Activation Functions** | ReLU, Sigmoid, Softmax -- kapan menggunakan masing-masing |
| **Overfitting** | Dropout, early stopping, regularization (L1/L2) |
| **Keras/TensorFlow** | Sequential model, compile (optimizer, loss, metrics), fit, evaluate |

#### NLP Basics (Minggu 12)

| Konsep | Poin Penting |
|---|---|
| **Text Preprocessing** | Tokenization, stopword removal, stemming/lemmatization |
| **Feature Extraction** | Bag of Words (BoW), TF-IDF |
| **Sentiment Analysis** | Klasifikasi teks positif/negatif/netral |
| **Word Embeddings** | Konsep representasi kata sebagai vektor (Word2Vec, konsep) |

---

### 2. Review Fase 4: Applied AI (Minggu 13-14)

#### Computer Vision & CNN (Minggu 13)

| Konsep | Poin Penting |
|---|---|
| **Representasi Citra** | Pixel, channel (RGB), resolusi, normalisasi |
| **Preprocessing** | Resize, grayscale, filtering, augmentasi |
| **CNN Architecture** | Conv2D, MaxPooling2D, Flatten, Dense |
| **Convolution** | Filter/kernel, feature maps, stride, padding |
| **Transfer Learning** | Pre-trained models, feature extraction, fine-tuning |

```
Arsitektur CNN (Ringkasan)
Input → [Conv2D → ReLU → MaxPool] × N → Flatten → Dense → Dropout → Output
         Feature Extraction                Classification
```

#### AI-Augmented Development & MLOps (Minggu 14)

| Konsep | Poin Penting |
|---|---|
| **Prompt Engineering** | Prinsip: spesifik, konteks, iteratif |
| **Evaluasi Kode AI** | Checklist: data leakage, compatibility, correctness |
| **MLOps** | Model lifecycle: train → evaluate → deploy → monitor |
| **Model Persistence** | joblib, pickle -- menyimpan dan memuat model |
| **Deployment** | Konsep Flask API untuk model serving |
| **Drift** | Data drift, concept drift -- mengapa model perlu di-retrain |
| **Responsible AI** | Fairness, accountability, transparency |

---

### 3. Integrasi: Menghubungkan Semua Konsep

#### Peta Konsep ML End-to-End

```
Problem Definition
        │
        ▼
   Data Collection & Understanding
        │
        ▼
   EDA & Preprocessing ←── Statistik Deskriptif, Visualisasi
        │
        ▼
   Feature Engineering ←── PCA, Feature Selection
        │
        ▼
   Model Selection
   ├── Supervised Learning
   │   ├── Regresi (target kontinu)
   │   ├── Klasifikasi (target diskrit)
   │   │   ├── Tradisional: Logistic Reg, SVM, RF, XGBoost
   │   │   ├── Deep Learning: MLP, CNN (citra), RNN (teks)
   │   │   └── Transfer Learning (data terbatas)
   │   └── Evaluasi: Accuracy, F1, Precision, Recall, RMSE
   │
   └── Unsupervised Learning
       ├── Clustering: K-Means, Hierarchical, DBSCAN
       ├── Dimensionality Reduction: PCA
       └── Evaluasi: Silhouette, Elbow, Davies-Bouldin
        │
        ▼
   Model Evaluation & Selection
        │
        ▼
   Deployment & Monitoring (MLOps)
        │
        ▼
   Responsible AI & Ethics
```

#### Cara Memilih Model yang Tepat

| Pertanyaan | Jawaban | Arah Model |
|---|---|---|
| Apakah ada label/target? | Ya | **Supervised Learning** |
| | Tidak | **Unsupervised Learning** |
| Target kontinu atau diskrit? | Kontinu | **Regresi** |
| | Diskrit | **Klasifikasi** |
| Data berupa gambar? | Ya | **CNN / Transfer Learning** |
| Data berupa teks? | Ya | **NLP (BoW/TF-IDF + Classifier)** |
| Dataset kecil (<1000)? | Ya | Model sederhana + Transfer Learning |
| Dataset besar (>10000)? | Ya | Deep Learning bisa dipertimbangkan |

---

### 4. Kisi-kisi UAS

#### Cakupan Materi

| Bagian | Materi | Bobot Perkiraan |
|---|---|---|
| **A** | Clustering & Unsupervised Learning (Minggu 9-10) | 20% |
| **B** | PCA & Dimensionality Reduction (Minggu 10) | 10% |
| **C** | Neural Networks & Deep Learning (Minggu 11-12) | 25% |
| **D** | NLP Basics (Minggu 12) | 10% |
| **E** | Computer Vision & CNN (Minggu 13) | 20% |
| **F** | MLOps & Responsible AI (Minggu 14) | 15% |

#### Format Ujian

| Jenis Soal | Jumlah | Bobot per Soal | Total |
|---|---|---|---|
| Pilihan Ganda (*Multiple Choice*) | 20 soal | 2 poin | 40 poin |
| Jawaban Singkat (*Short Answer*) | 5 soal | 4 poin | 20 poin |
| Esai / Analisis (*Essay*) | 4 soal | 10 poin | 40 poin |
| **Total** | | | **100 poin** |

> **Penting:** UAS bersifat **closed-book**. Penggunaan AI (ChatGPT, Claude, dll.) **TIDAK diizinkan** selama ujian. Ini menguji pemahaman mandiri Anda.

---

### 5. Contoh Soal dan Pembahasan

#### Contoh Soal Pilihan Ganda

**Soal 1:** Pada algoritma K-Means, metode *elbow* digunakan untuk...

a) Menghitung jarak antar cluster
b) Menentukan jumlah cluster optimal
c) Mengevaluasi kualitas centroid
d) Mendeteksi outlier dalam data

**Jawaban:** b) Menentukan jumlah cluster optimal
**Pembahasan:** Metode elbow melihat grafik SSE (Sum of Squared Errors) vs jumlah K, dan mencari titik "siku" di mana penambahan cluster tidak lagi menurunkan SSE secara signifikan.

---

**Soal 2:** Dalam arsitektur CNN, fungsi lapisan MaxPooling2D adalah...

a) Menambahkan non-linearity ke model
b) Mengurangi dimensi spasial feature map
c) Menghubungkan semua neuron
d) Melakukan konvolusi dengan filter

**Jawaban:** b) Mengurangi dimensi spasial feature map
**Pembahasan:** MaxPooling mengambil nilai maksimum dari setiap region, sehingga mengurangi ukuran feature map dan mengurangi jumlah parameter yang perlu dipelajari.

---

**Soal 3:** Apa yang dimaksud dengan *concept drift* dalam konteks MLOps?

a) Model mengalami underfitting
b) Hubungan antara input dan output berubah seiring waktu
c) Data training terlalu sedikit
d) Performa GPU menurun

**Jawaban:** b) Hubungan antara input dan output berubah seiring waktu
**Pembahasan:** Concept drift terjadi ketika pola yang dipelajari model tidak lagi berlaku karena perubahan di dunia nyata, misalnya perubahan perilaku konsumen setelah pandemi.

#### Contoh Soal Jawaban Singkat

**Soal 4:** Jelaskan perbedaan antara *feature extraction* dan *fine-tuning* dalam transfer learning. (4 poin)

**Jawaban:**
- **Feature extraction**: Seluruh lapisan model pre-trained dibekukan (*frozen*), hanya lapisan klasifikasi baru yang dilatih. Digunakan ketika dataset baru sangat kecil atau sangat mirip dengan dataset asal. (2 poin)
- **Fine-tuning**: Sebagian lapisan model pre-trained (biasanya lapisan atas) dibuka dan ikut dilatih ulang bersama lapisan baru. Digunakan ketika dataset cukup besar atau berbeda signifikan dari dataset asal. (2 poin)

#### Contoh Soal Esai

**Soal 5:** Anda diminta membangun sistem AI untuk mengklasifikasikan jenis sampah (organik, anorganik, B3) dari foto untuk mendukung program pengelolaan sampah di DKI Jakarta. (10 poin)

a) Jelaskan arsitektur model yang akan Anda gunakan dan alasannya. (3 poin)
b) Jelaskan langkah preprocessing yang diperlukan untuk data citra. (3 poin)
c) Bagaimana Anda akan mengevaluasi performa model? Metrik apa yang paling penting dan mengapa? (2 poin)
d) Dari perspektif responsible AI, apa potensi masalah etika dan bagaimana mengatasinya? (2 poin)

**Panduan Jawaban:**
- a) CNN dengan transfer learning (MobileNetV2/ResNet50), karena dataset lokal kemungkinan terbatas dan transfer learning memanfaatkan fitur visual yang sudah dipelajari dari ImageNet.
- b) Resize ke ukuran seragam (224x224), normalisasi pixel (0-1), augmentasi (rotasi, flip, brightness) untuk memperbanyak data.
- c) Precision dan recall per kelas penting, terutama untuk B3 (bahan berbahaya) di mana false negative sangat berbahaya. F1-score sebagai metrik keseimbangan.
- d) Bias jika dataset tidak representatif (hanya sampah tertentu), dampak jika B3 salah diklasifikasikan. Solusi: dataset beragam, threshold tinggi untuk kelas B3, human-in-the-loop.

---

### 6. Tips Menghadapi UAS

#### Strategi Persiapan

| Strategi | Cara Implementasi |
|---|---|
| **Review terstruktur** | Baca ulang ringkasan setiap minggu, fokus pada konsep kunci |
| **Latihan soal** | Kerjakan contoh soal dan soal dari modul sebelumnya |
| **Buat mind map** | Hubungkan konsep antar topik menggunakan diagram |
| **Diskusi kelompok** | Jelaskan konsep ke teman -- mengajar adalah cara belajar terbaik |
| **Fokus pada pemahaman** | Pahami *mengapa*, bukan hanya *apa* dan *bagaimana* |

#### Hal-Hal yang Perlu Diperhatikan

```
Checklist Persiapan UAS
├── □ Pahami perbedaan supervised vs unsupervised learning
├── □ Bisa menjelaskan cara kerja setiap algoritma (bukan hanya menggunakan)
├── □ Pahami kapan menggunakan model tertentu
├── □ Kuasai metrik evaluasi dan interpretasinya
├── □ Pahami arsitektur CNN dan konsep transfer learning
├── □ Mengerti konsep MLOps (lifecycle, drift, monitoring)
├── □ Bisa menjelaskan prinsip responsible AI
└── □ Mampu menghubungkan teori dengan konteks Indonesia
```

#### Kesalahan Umum yang Harus Dihindari

| Kesalahan | Koreksi |
|---|---|
| Menghafal kode tanpa memahami logika | Fokus pada konsep di balik kode |
| Bingung antara classification dan regression metrics | Accuracy/F1 untuk klasifikasi, RMSE/MAE untuk regresi |
| Lupa bahwa scaling harus setelah train-test split | Selalu split dulu, baru fit_transform pada training |
| Tidak bisa menjelaskan trade-offs antar model | Pahami kelebihan dan kekurangan setiap algoritma |
| Mengabaikan aspek etika dan responsible AI | Ini bagian penting dari mata kuliah! |

---

### 7. Pesan Penutup Semester

#### Refleksi Perjalanan Belajar

Selama satu semester ini, Anda telah mempelajari fondasi yang kuat dalam Kecerdasan Buatan dan Machine Learning:

```
Perjalanan Belajar AI/ML
Minggu 1-4:   Fondasi ─── Python, statistik, supervised learning dasar
Minggu 5-8:   Pendalaman ─ Model lanjut, evaluasi, tuning (UTS)
Minggu 9-12:  Advanced ─── Clustering, PCA, deep learning, NLP
Minggu 13-14: Applied ──── Computer vision, MLOps, responsible AI
Minggu 15-16: Integrasi ── Proyek akhir, review, UAS
```

#### Pesan dari Dosen

> *"Perjalanan belajar AI dan machine learning tidak berhenti di semester ini. Teknologi AI terus berkembang dengan pesat, dan apa yang Anda pelajari adalah fondasi yang akan terus relevan. Yang terpenting bukan hanya kemampuan teknis, tetapi juga karakter -- amanah dalam mengelola data, adil dalam membangun model, dan bertanggung jawab atas dampak teknologi yang kita ciptakan. Sebagai lulusan Informatika UAI, Anda memiliki bekal unik: keahlian teknis yang kuat DAN landasan etika yang kokoh. Gunakan keduanya untuk menjadi problem solver yang membawa manfaat bagi umat."*
>
> -- Tri Aji Nugroho, S.T., M.T.

#### Langkah Selanjutnya

| Langkah | Rekomendasi |
|---|---|
| **Terus belajar** | Kaggle competitions, online courses (Coursera, fast.ai) |
| **Bangun portofolio** | Upload proyek ke GitHub, tulis blog teknis |
| **Ikut komunitas** | Indonesia AI, Data Science Indonesia, meetup lokal |
| **Riset** | Eksplorasi topik lanjut: reinforcement learning, generative AI, LLM |
| **Kontribusi** | Open source, dataset lokal Indonesia, mentoring |

---

## Aktivitas Kelas

### Sesi 1: Review Komprehensif (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Pembukaan | Gambaran umum review, format UAS |
| 20 menit | Review Fase 3 | Clustering, PCA, neural networks, NLP |
| 20 menit | Review Fase 4 | Computer vision, CNN, MLOps, responsible AI |
| 15 menit | Integrasi Konsep | Menghubungkan semua topik, flowchart pemilihan model |
| 20 menit | Latihan Soal | Mengerjakan contoh soal dan pembahasan bersama |
| 10 menit | Q&A Terbuka | Pertanyaan terakhir sebelum ujian |
| 5 menit | Pesan Penutup | Motivasi dan arahan sebelum UAS |

### Sesi 2: Ujian Akhir Semester (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 5 menit | Persiapan Ujian | Distribusi soal, instruksi pengerjaan |
| 90 menit | Pengerjaan UAS | Closed-book, tanpa AI, tanpa internet |
| 5 menit | Pengumpulan | Pengumpulan lembar jawaban |

---

## AI Corner: Masa Depan AI -- Perjalanan Belajar Tidak Berhenti di Sini

> **Pesan Akhir:** AI Corner terakhir ini bukan tentang teknik baru, melainkan tentang visi ke depan dan motivasi untuk terus belajar.

### Tren AI yang Akan Membentuk Masa Depan

| Tren | Deskripsi | Relevansi untuk Indonesia |
|---|---|---|
| **Generative AI** | LLM, text-to-image, text-to-video | Kreativitas digital, content creation |
| **AI Agents** | Sistem AI yang bisa bertindak otonom | Otomasi layanan publik, customer service |
| **Multimodal AI** | AI yang memproses teks, gambar, audio sekaligus | Aksesibilitas, pendidikan inklusif |
| **Edge AI** | AI di perangkat lokal (HP, IoT) | Smart agriculture, smart city Indonesia |
| **Responsible AI** | Regulasi, etika, transparansi | STRANAS-AI, UU PDP, tata kelola AI |

### Sumber Belajar Lanjutan

| Sumber | Tipe | Level |
|---|---|---|
| [fast.ai](https://www.fast.ai/) | Kursus online gratis | Intermediate-Advanced |
| [Kaggle Learn](https://www.kaggle.com/learn) | Tutorial interaktif | Beginner-Intermediate |
| [CS231n Stanford](http://cs231n.stanford.edu/) | Kursus computer vision | Advanced |
| [Hugging Face Courses](https://huggingface.co/learn) | NLP dan transformer | Intermediate-Advanced |
| [Indonesia AI](https://indonesiaai.org/) | Komunitas dan riset | Semua level |

### Pesan Akhir AI Corner

```
Sepanjang 16 minggu, Anda telah belajar:
  ✓ Menggunakan AI sebagai alat bantu belajar (bukan pengganti)
  ✓ Mengevaluasi output AI secara kritis
  ✓ Berkolaborasi dengan AI untuk membangun solusi ML
  ✓ Memahami batasan dan tanggung jawab penggunaan AI

Ke depan, teruslah belajar dengan prinsip:
  → AI sebagai co-pilot, Anda tetap pilot-nya
  → Pahami konsep sebelum menggunakan tools
  → Bangun dengan etika, deploy dengan tanggung jawab
  → Kontribusi untuk kemajuan AI di Indonesia
```

---

## Referensi

### Buku Review

1. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
2. Chollet, F. (2021). *Deep Learning with Python* (2nd ed.). Manning Publications.
3. Huyen, C. (2022). *Designing Machine Learning Systems*. O'Reilly Media.

### Sumber Online

4. [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) -- Referensi lengkap scikit-learn.
5. [TensorFlow Tutorials](https://www.tensorflow.org/tutorials) -- Tutorial resmi TensorFlow/Keras.
6. [Machine Learning Mastery](https://machinelearningmastery.com/) -- Tutorial dan panduan praktis ML.

### Referensi Indonesia

7. [STRANAS-AI Indonesia](https://ai-innovation.id/) -- Strategi Nasional AI Indonesia.
8. [Indonesia AI Society](https://indonesiaai.org/) -- Komunitas AI Indonesia.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
