# Minggu 1: Pengantar AI — Sejarah dan Filosofi

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 1 |
| **Topik** | Pengantar AI — Sejarah dan Filosofi |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK-1: Memahami konsep dasar kecerdasan buatan, sejarah perkembangannya, dan landasan filosofisnya |
| **Sub-CPMK** | 1.1 Menjelaskan definisi dan klasifikasi kecerdasan buatan (AI) |
| | 1.2 Menguraikan sejarah perkembangan AI dari Turing hingga era LLM |
| | 1.3 Menjelaskan jenis-jenis AI dan pipeline machine learning |
| **Bloom's Taxonomy** | C2 (Memahami / *Understanding*) |
| **Durasi** | 2 x 100 menit (Teori 100 min + Praktikum 100 min) |
| **Platform** | Google Colab |
| **Metode** | Ceramah interaktif, diskusi, demonstrasi, hands-on Google Colab |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** definisi kecerdasan buatan dan membedakan klasifikasi Weak AI, Strong AI, dan Super AI serta Narrow AI vs General AI.
2. **Menguraikan** sejarah perkembangan AI mulai dari Turing Test (1950) hingga era Large Language Models (2022+) beserta tonggak-tonggak pentingnya.
3. **Membedakan** jenis-jenis pendekatan AI (rule-based, machine learning, deep learning) dan menjelaskan ML pipeline secara garis besar.
4. **Mengidentifikasi** aplikasi AI di Indonesia dan memahami prinsip etika AI yang sejalan dengan nilai-nilai Islami.

---

## Materi Pembelajaran

### 1. Definisi Kecerdasan Buatan (*Artificial Intelligence*)

#### Apa Itu AI?

**Kecerdasan Buatan** (*Artificial Intelligence* / AI) adalah cabang ilmu komputer yang bertujuan menciptakan sistem yang mampu melakukan tugas-tugas yang biasanya memerlukan kecerdasan manusia — seperti belajar, bernalar, memecahkan masalah, memahami bahasa, dan membuat keputusan.

John McCarthy, yang menciptakan istilah *"Artificial Intelligence"* pada tahun 1956, mendefinisikannya sebagai:

> "The science and engineering of making intelligent machines."

#### Klasifikasi AI Berdasarkan Kemampuan

```
Kecerdasan Buatan (AI)
├── Weak AI / Narrow AI (AI Lemah / AI Sempit)
│   └── Dirancang untuk satu tugas spesifik
│       Contoh: Siri, Google Translate, AlphaGo, ChatGPT
│
├── Strong AI / General AI (AI Kuat / AI Umum)
│   └── Mampu memahami dan belajar tugas apapun seperti manusia
│       Status: Belum tercapai (masih teori)
│
└── Super AI (AI Super)
    └── Melampaui kecerdasan manusia di semua bidang
        Status: Masih hipotesis / spekulasi
```

| Tipe AI | Kemampuan | Status | Contoh |
|---|---|---|---|
| **Weak AI** (*Narrow AI*) | Satu tugas spesifik | Sudah ada | Rekomendasi Tokopedia, deteksi spam Gmail |
| **Strong AI** (*General AI*) | Semua tugas kognitif manusia | Belum ada | — (masih riset) |
| **Super AI** | Melampaui manusia | Hipotesis | — (masih spekulasi filosofis) |

> **Insight:** Semua AI yang kita gunakan saat ini — termasuk ChatGPT, Claude, dan Gemini — termasuk kategori **Weak AI / Narrow AI**. Meskipun terlihat "cerdas", mereka dirancang untuk tugas spesifik (menghasilkan teks) dan tidak memiliki pemahaman atau kesadaran sejati.

#### Narrow AI vs. General AI

Perbedaan utama antara *Narrow AI* dan *General AI*:

| Aspek | Narrow AI | General AI |
|---|---|---|
| **Cakupan tugas** | Satu domain spesifik | Semua domain |
| **Kemampuan belajar** | Transfer learning terbatas | Belajar mandiri seperti manusia |
| **Kesadaran** | Tidak ada | Hipotesis: ada kesadaran |
| **Contoh** | GPT-4, DALL-E, AlphaFold | Belum ada |
| **Timeline** | Sekarang | Belum diketahui |

---

### 2. Sejarah AI: Dari Turing hingga Era LLM

Memahami sejarah AI membantu kita melihat mengapa teknologi ini berkembang seperti sekarang dan ke mana arahnya.

#### Timeline Perkembangan AI

```
1950   1956    1960-70s    1974-80   1980-87   1987-93   1997     2012      2017       2022+
  │      │        │          │         │         │        │        │          │          │
  ▼      ▼        ▼          ▼         ▼         ▼        ▼        ▼          ▼          ▼
Turing  Dart-  Golden    AI       Expert   AI     Deep   Deep     Trans-    ChatGPT
 Test   mouth   Age     Winter   Systems  Winter  Blue  Learning  former    & LLM
              (Optimis)   1       (Boom)    2    (Chess) (ImageNet)  Era       Era
```

#### Tonggak-Tonggak Penting

| Tahun | Peristiwa | Signifikansi |
|---|---|---|
| **1950** | Alan Turing mempublikasikan *"Computing Machinery and Intelligence"* | Mengajukan **Turing Test** — bisakah mesin berpikir? |
| **1956** | **Dartmouth Conference** | Istilah "Artificial Intelligence" resmi diciptakan oleh John McCarthy |
| **1960-an** | Program ELIZA, Logic Theorist | Era optimisme tinggi, AI bisa menyelesaikan masalah sederhana |
| **1974-1980** | **AI Winter pertama** | Pendanaan berkurang, ekspektasi tak terpenuhi |
| **1980-an** | Expert Systems (Sistem Pakar) | Pendekatan rule-based populer di industri |
| **1987-1993** | **AI Winter kedua** | Expert systems terlalu mahal dan kaku |
| **1997** | IBM Deep Blue mengalahkan Garry Kasparov | Tonggak AI dalam permainan strategis |
| **2012** | AlexNet memenangkan ImageNet Challenge | **Revolusi Deep Learning** dimulai |
| **2016** | AlphaGo mengalahkan Lee Sedol | Deep reinforcement learning membuktikan kemampuan AI |
| **2017** | Paper *"Attention Is All You Need"* | Arsitektur **Transformer** lahir — dasar semua LLM modern |
| **2022** | ChatGPT diluncurkan oleh OpenAI | Era **Large Language Models** (LLM) dimulai secara massal |
| **2023-2024** | GPT-4, Claude, Gemini, Llama | LLM multimodal, AI menjadi mainstream |
| **2025-2026** | AI Agents, Reasoning Models | AI yang bisa bernalar dan bertindak secara otonom |

#### Al-Khawarizmi: Warisan Islam dalam AI

Perlu diketahui bahwa kata **"algoritma"** (*algorithm*) berasal dari nama ilmuwan Muslim **Muhammad ibn Musa al-Khawarizmi** (780-850 M), seorang matematikawan dari Persia yang menulis buku *Al-Kitab al-Mukhtasar fi Hisab al-Jabr wal-Muqabala* — yang juga menjadi asal kata **"aljabar"** (*algebra*).

Al-Khawarizmi mengembangkan metode penyelesaian masalah yang sistematis dan langkah demi langkah — yang kini kita kenal sebagai **algoritma**, fondasi dari semua program komputer dan sistem AI.

> **Refleksi:** Sebagai mahasiswa di universitas Islam, kita memiliki warisan intelektual yang kaya dalam bidang matematika dan sains. Tradisi ilmiah Islam menekankan pencarian ilmu (*'ilm*) sebagai ibadah.

---

### 3. Jenis-Jenis AI: Rule-Based, Machine Learning, Deep Learning

#### Tiga Paradigma Utama AI

```
            Kecerdasan Buatan (AI)
            ┌───────────────────────┐
            │                       │
      Rule-Based AI          Machine Learning
    (Sistem Berbasis           ┌──────────┐
      Aturan)                  │          │
                          Traditional    Deep
                             ML        Learning
                                    (Neural Networks)
```

#### a) Rule-Based AI (Sistem Berbasis Aturan)

Pendekatan paling awal dalam AI, di mana manusia secara eksplisit menuliskan aturan-aturan (*rules*) yang harus diikuti oleh sistem.

```
IF suhu > 38°C AND batuk == True AND sesak_napas == True:
    diagnosis = "Kemungkinan infeksi saluran pernapasan"
    rekomendasi = "Rujuk ke dokter spesialis"
ELIF suhu > 37.5°C AND batuk == True:
    diagnosis = "Kemungkinan flu"
    rekomendasi = "Istirahat dan minum obat"
```

**Kelebihan:** Transparan, mudah dipahami, mudah di-debug.
**Kekurangan:** Tidak bisa menangani situasi yang tidak didefinisikan, sulit di-scale.

#### b) Machine Learning (Pembelajaran Mesin)

Sistem **belajar dari data** tanpa diprogram secara eksplisit. Model menemukan pola (*patterns*) dari data pelatihan (*training data*).

Tipe-tipe Machine Learning:

| Tipe | Deskripsi | Contoh Algoritma | Contoh Kasus |
|---|---|---|---|
| **Supervised** | Belajar dari data berlabel | Regresi Linear, Decision Tree, SVM | Prediksi harga rumah, klasifikasi email spam |
| **Unsupervised** | Menemukan pola tanpa label | K-Means, PCA, DBSCAN | Segmentasi pelanggan, deteksi anomali |
| **Reinforcement** | Belajar dari reward/punishment | Q-Learning, PPO | Game AI, robotika, trading |

#### c) Deep Learning (Pembelajaran Mendalam)

Subset dari machine learning yang menggunakan **neural networks** dengan banyak lapisan (*layers*). Sangat efektif untuk data tidak terstruktur seperti gambar, teks, dan audio.

| Arsitektur | Kegunaan | Contoh Aplikasi |
|---|---|---|
| **CNN** (*Convolutional Neural Network*) | Image recognition | Deteksi wajah, klasifikasi gambar |
| **RNN / LSTM** | Sequential data | Prediksi time series, speech recognition |
| **Transformer** | NLP, multimodal | ChatGPT, Claude, BERT, GPT-4 |
| **GAN** (*Generative Adversarial Network*) | Generasi konten | Deepfake, image synthesis |

---

### 4. ML Pipeline Overview: Dari Data hingga Deployment

Setiap proyek machine learning mengikuti alur (*pipeline*) yang sistematis:

```
┌──────────┐   ┌──────────────┐   ┌───────────┐   ┌────────────┐   ┌────────────┐
│   Data   │──▶│ Preprocessing│──▶│  Modeling  │──▶│ Evaluation │──▶│ Deployment │
│Collection│   │  & Feature   │   │ (Training) │   │  (Testing) │   │(Production)│
└──────────┘   │ Engineering  │   └───────────┘   └────────────┘   └────────────┘
               └──────────────┘
```

| Tahap | Deskripsi | Tools Utama |
|---|---|---|
| **Data Collection** | Mengumpulkan data dari berbagai sumber | Web scraping, API, database |
| **Preprocessing** | Membersihkan dan menyiapkan data | pandas, numpy, scikit-learn |
| **Feature Engineering** | Memilih dan membuat fitur yang relevan | pandas, domain knowledge |
| **Modeling** | Melatih model machine learning | scikit-learn, TensorFlow, PyTorch |
| **Evaluation** | Mengevaluasi performa model | Accuracy, precision, recall, F1-score |
| **Deployment** | Menyebarkan model ke produksi | Flask, FastAPI, Docker, cloud |

> **Catatan:** Sepanjang semester ini, kita akan mempelajari setiap tahap pipeline ini secara mendalam. Minggu ini adalah gambaran besar (*big picture*).

---

### 5. Aplikasi AI di Indonesia

Indonesia memiliki ekosistem AI yang berkembang pesat. Berikut contoh-contoh nyata penerapan AI di berbagai sektor:

#### Sektor Teknologi dan E-Commerce

| Perusahaan | Aplikasi AI | Teknik ML |
|---|---|---|
| **GoTo (Gojek + Tokopedia)** | Rekomendasi produk, estimasi waktu pengiriman, *surge pricing* | Collaborative filtering, time series prediction |
| **Tokopedia** | Search relevance, fraud detection, chatbot | NLP, anomaly detection |
| **Bukalapak** | Product categorization, price suggestion | Classification, regression |
| **Traveloka** | Dynamic pricing, recommendation engine | Reinforcement learning, collaborative filtering |

#### Sektor Keuangan

| Institusi | Aplikasi AI | Teknik ML |
|---|---|---|
| **Bank Indonesia** | Deteksi fraud, analisis risiko | Anomaly detection, classification |
| **OJK** | Surveillance pasar modal | Pattern recognition |
| **Dana / OVO / GoPay** | Credit scoring, fraud detection | Gradient boosting, neural networks |

#### Sektor Kesehatan dan Publik

| Institusi | Aplikasi AI | Teknik ML |
|---|---|---|
| **Halodoc** | Triage pasien, rekomendasi dokter | NLP, classification |
| **Kemenkes** | Prediksi sebaran penyakit | Time series, spatial analysis |
| **BMKG** | Prediksi cuaca dan bencana | Deep learning, ensemble methods |

> **Insight:** Indonesia memiliki peluang besar dalam pengembangan AI karena memiliki jumlah pengguna internet terbesar ke-4 di dunia dan data yang melimpah dari 280+ juta penduduk.

---

### 6. Etika AI dan Nilai-Nilai Islami

#### Mengapa Etika AI Penting?

Dengan kekuatan AI yang semakin besar, muncul pula tantangan etis yang serius:

- **Bias algoritmik** — model AI bisa mendiskriminasi berdasarkan ras, gender, atau kelompok tertentu
- **Deepfake** — teknologi AI untuk membuat konten palsu yang sangat meyakinkan
- **Kehilangan pekerjaan** — otomasi AI berpotensi menggantikan banyak pekerjaan
- **Privasi** — AI memerlukan data besar yang bisa melanggar privasi individu
- **Senjata otonom** — AI yang digunakan untuk keputusan hidup-mati tanpa intervensi manusia

#### Prinsip *Responsible AI*

Industri global mengadopsi prinsip-prinsip *Responsible AI*:

1. **Fairness** (Keadilan) — AI tidak boleh mendiskriminasi
2. **Transparency** (Transparansi) — cara kerja AI harus bisa dijelaskan
3. **Accountability** (Akuntabilitas) — harus ada pihak yang bertanggung jawab
4. **Privacy** (Privasi) — data harus dilindungi
5. **Safety** (Keamanan) — AI harus aman digunakan

#### Nilai-Nilai Islam dalam Pengembangan AI

Sebagai mahasiswa Universitas Al Azhar Indonesia, kita menghubungkan etika AI dengan prinsip-prinsip Islam:

| Nilai Islam | Penerapan dalam AI |
|---|---|
| **Amanah** (Kepercayaan) | Data dan model AI yang dipercayakan harus dijaga integritasnya. Tidak boleh disalahgunakan untuk kepentingan yang merugikan. |
| **Keadilan** (Al-'Adl) | Model AI harus adil — tidak bias terhadap kelompok tertentu. Keputusan AI harus bisa dipertanggungjawabkan. |
| **Transparansi** (Al-Bayan) | Cara kerja AI harus transparan (*explainable AI*). Tidak boleh menjadi "kotak hitam" yang tak bisa dipahami. |
| **Tidak Merugikan** (La Dharar) | AI tidak boleh digunakan untuk merugikan orang lain — baik secara langsung maupun tidak langsung. |
| **Pencarian Ilmu** (Al-'Ilm) | Mengembangkan AI adalah bagian dari pencarian ilmu yang bermanfaat bagi umat manusia. |

> **Refleksi:** "Sebaik-baik manusia adalah yang paling bermanfaat bagi manusia lain." (HR. Ahmad). Sebagai pengembang AI masa depan, bagaimana kita memastikan teknologi yang kita bangun bermanfaat dan tidak merugikan?

---

### 7. Kontrak Kuliah & AI Policy

#### Ekspektasi Perkuliahan

- Hadir minimal 75% dari total pertemuan
- Aktif berpartisipasi dalam diskusi dan hands-on praktikum
- Mengerjakan semua tugas, kuis, dan proyek
- Membawa laptop yang sudah bisa mengakses Google Colab

#### Komponen Penilaian

| Komponen | Bobot | Keterangan |
|---|---|---|
| Tugas Individu | 15% | Tugas mingguan (T1-T5) |
| Kuis | 10% | 3 kuis (K1, K2, K3) |
| UTS | 20% | Ujian Tengah Semester (Minggu 8) |
| Proyek (Mid + Akhir) | 25% | Proyek kelompok |
| UAS | 25% | Ujian Akhir Semester (Minggu 16) |
| Partisipasi | 5% | Kehadiran dan keterlibatan aktif |
| **Total** | **100%** | |

#### Kebijakan Penggunaan AI (*AI Policy*)

Mata kuliah ini mengadopsi pendekatan **AI-Augmented Learning**:

1. **Diizinkan:** Menggunakan AI (ChatGPT, Claude, Copilot, Gemini) sebagai alat bantu belajar, coding, dan debugging.
2. **Wajib:** Setiap penggunaan AI harus didokumentasikan dalam **AI Usage Log**. Mahasiswa harus mampu **menjelaskan** semua kode dan konsep yang dihasilkan AI.
3. **Dilarang:** Menyerahkan output AI mentah tanpa pemahaman. Copy-paste tanpa modifikasi dan pemahaman dianggap pelanggaran akademik.
4. **Prinsip:** "AI sebagai *co-pilot*, bukan *auto-pilot*."
5. **Ujian (UTS/UAS):** AI **TIDAK diizinkan**. Ujian bersifat *closed-book*.

---

## Aktivitas Kelas

### Sesi 1: Teori dan Diskusi (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Pembukaan & Ice Breaking | Perkenalan dosen dan mahasiswa, survei awal pengalaman AI dan coding |
| 20 menit | Ceramah: Definisi & Sejarah AI | Penjelasan definisi AI, klasifikasi, dan timeline sejarah |
| 15 menit | Diskusi Kelompok Kecil | "Sebutkan 3 aplikasi AI yang kalian gunakan sehari-hari. Termasuk kategori AI apa?" |
| 20 menit | Ceramah: Jenis AI & ML Pipeline | Rule-based vs ML vs DL, overview ML pipeline |
| 15 menit | Ceramah: Aplikasi AI di Indonesia | Contoh nyata dari GoTo, Tokopedia, Bank Indonesia, Halodoc |
| 15 menit | Diskusi: Etika AI & Kontrak Kuliah | Prinsip etika AI, nilai-nilai Islami, AI policy |
| 5 menit | Transisi ke Praktikum | Persiapan Google Colab |

### Sesi 2: Hands-on Praktikum (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 15 menit | Setup & Tour Google Colab | Navigasi interface, menjalankan cell, markdown cell |
| 20 menit | Import Library & Cek Versi | Import scikit-learn, pandas, numpy — cek versi, pastikan semua berjalan |
| 25 menit | Load Dataset Pertama | Load Iris dataset, eksplorasi dasar |
| 20 menit | Eksplorasi Mandiri | Mahasiswa mencoba sendiri dengan bimbingan |
| 15 menit | Diskusi Hasil & Wrap-up | Sharing hasil, Q&A, preview minggu depan |
| 5 menit | Tugas & Penutup | Penjelasan tugas mandiri |

---

## Hands-on: Kode Python Pertama untuk AI/ML

### Langkah 1: Cek Versi Library

```python
# ============================================================
# Minggu 1: Pengantar AI - Setup dan Eksplorasi Pertama
# Mata Kuliah: Kecerdasan Buatan dan Machine Learning
# Universitas Al Azhar Indonesia
# ============================================================

# Import library utama untuk AI/ML
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

# Cek versi semua library
print("=" * 50)
print("Setup Environment AI/ML - Berhasil!")
print("=" * 50)
print(f"NumPy version    : {np.__version__}")
print(f"Pandas version   : {pd.__version__}")
print(f"Matplotlib version: {plt.matplotlib.__version__}")
print(f"Scikit-learn version: {sklearn.__version__}")
print("=" * 50)
print("Semua library siap digunakan!")
```

### Langkah 2: Load Dataset Pertama (Iris Dataset)

```python
# Import dataset Iris dari scikit-learn
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()

# Iris adalah dataset klasik dalam ML
# Berisi data pengukuran bunga Iris untuk 3 spesies
print("=== Informasi Dataset Iris ===")
print(f"Nama fitur (features): {iris.feature_names}")
print(f"Nama kelas (target) : {iris.target_names}")
print(f"Jumlah sampel       : {iris.data.shape[0]}")
print(f"Jumlah fitur        : {iris.data.shape[1]}")
```

### Langkah 3: Konversi ke DataFrame dan Eksplorasi

```python
# Konversi ke pandas DataFrame untuk kemudahan analisis
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Tampilkan 10 baris pertama
print("=== 10 Baris Pertama Dataset Iris ===")
print(df.head(10))
print()

# Informasi dataset
print("=== Informasi Dataset ===")
print(df.info())
print()

# Statistik deskriptif
print("=== Statistik Deskriptif ===")
print(df.describe())
```

### Langkah 4: Distribusi Kelas Target

```python
# Hitung jumlah sampel per spesies
print("=== Distribusi Spesies ===")
print(df['species'].value_counts())
print()

# Visualisasi distribusi kelas
fig, ax = plt.subplots(figsize=(8, 5))
df['species'].value_counts().plot(kind='bar', color=['#2196F3', '#4CAF50', '#FF9800'], ax=ax)
ax.set_title('Distribusi Spesies Iris', fontsize=14, fontweight='bold')
ax.set_xlabel('Spesies')
ax.set_ylabel('Jumlah Sampel')
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
plt.tight_layout()
plt.show()
```

### Langkah 5: Visualisasi Sederhana

```python
# Scatter plot: petal length vs petal width
# Ini adalah preview bagaimana data bisa menunjukkan pola
# yang berguna untuk machine learning

fig, ax = plt.subplots(figsize=(10, 6))

colors = {'setosa': '#2196F3', 'versicolor': '#4CAF50', 'virginica': '#FF9800'}
for species in iris.target_names:
    subset = df[df['species'] == species]
    ax.scatter(subset['petal length (cm)'], subset['petal width (cm)'],
               label=species, color=colors[species], alpha=0.7, s=60)

ax.set_xlabel('Petal Length (cm)', fontsize=12)
ax.set_ylabel('Petal Width (cm)', fontsize=12)
ax.set_title('Iris Dataset: Petal Length vs Petal Width\n'
             '(Preview: Data yang Bisa Dipelajari oleh Machine Learning)',
             fontsize=13, fontweight='bold')
ax.legend(title='Spesies', fontsize=10)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\nInsight: Perhatikan bagaimana spesies yang berbeda")
print("membentuk kelompok (cluster) yang terpisah.")
print("Inilah yang akan 'dipelajari' oleh model ML!")
```

### Langkah 6: Preview ML Pipeline — Train-Test Split

```python
from sklearn.model_selection import train_test_split

# Pisahkan data menjadi features (X) dan target (y)
X = iris.data   # Fitur: panjang/lebar sepal dan petal
y = iris.target  # Target: spesies (0, 1, 2)

# Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("=== Preview ML Pipeline: Train-Test Split ===")
print(f"Total sampel       : {len(X)}")
print(f"Data training (80%): {len(X_train)} sampel")
print(f"Data testing (20%) : {len(X_test)} sampel")
print()
print("Minggu depan kita akan belajar preprocessing data")
print("dan membangun model ML pertama kita!")
```

---

## AI Corner: Mengenal AI sebagai *Coding Partner* untuk ML

> **Konsep Baru:** Sepanjang semester ini, setiap modul akan memiliki bagian **AI Corner** yang menunjukkan bagaimana memanfaatkan AI secara bertanggung jawab dalam proses belajar AI/ML. Level: **Basic**.

### Cara AI Bisa Membantu Anda Belajar AI/ML

| Skenario | Contoh Prompt ke AI |
|---|---|
| Memahami konsep | *"Jelaskan perbedaan supervised dan unsupervised learning dengan analogi sederhana"* |
| Debugging kode | *"Kode Python ini error: [paste kode]. Apa yang salah?"* |
| Memahami terminologi | *"Apa perbedaan antara model, algoritma, dan framework dalam konteks ML?"* |
| Menghasilkan contoh | *"Berikan contoh penggunaan train_test_split di scikit-learn"* |
| Penjelasan output | *"Apa arti output .describe() berikut ini: [paste output]"* |

### Tips Penting

1. **Selalu verifikasi** jawaban AI dengan referensi terpercaya (dokumentasi resmi, buku teks).
2. **Jangan hanya copy-paste** — pastikan Anda memahami setiap baris kode.
3. **Gunakan AI untuk belajar**, bukan untuk menggantikan proses berpikir.
4. **Dokumentasikan** kapan dan bagaimana Anda menggunakan AI dalam AI Usage Log.

### Contoh Prompt Minggu Ini

Coba masukkan prompt berikut ke ChatGPT atau Claude:

```
Saya mahasiswa semester 3 yang baru mulai belajar AI dan Machine Learning.
Jelaskan dengan bahasa sederhana dan analogi:
1. Apa perbedaan antara AI, Machine Learning, dan Deep Learning?
2. Apa itu "training" dan "testing" dalam ML?
3. Mengapa dataset Iris sering digunakan untuk belajar ML?
Berikan contoh dari kehidupan sehari-hari di Indonesia.
```

Bandingkan jawaban AI dengan materi yang sudah dipelajari hari ini.

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai bahan refleksi:

1. **Jenis AI di Sekitar Anda:** Sebutkan 5 aplikasi atau layanan yang Anda gunakan sehari-hari yang menerapkan AI. Untuk masing-masing, tentukan apakah termasuk rule-based, machine learning, atau deep learning — dan berikan alasannya.

2. **AI Winter dan AI Spring:** Mengapa AI mengalami "musim dingin" (*AI Winter*)? Faktor apa yang menyebabkan kebangkitan kembali AI di era modern? Pelajaran apa yang bisa kita ambil?

3. **AI di Indonesia:** Identifikasi satu peluang penerapan AI di Indonesia yang belum banyak dieksplorasi. Jelaskan masalah yang bisa diselesaikan dan data apa yang dibutuhkan.

4. **Etika AI:** Bayangkan Anda mengembangkan sistem AI untuk seleksi penerimaan mahasiswa baru di sebuah universitas. Bagaimana Anda memastikan sistem tersebut adil dan tidak diskriminatif? Kaitkan dengan prinsip *Al-'Adl* (keadilan).

5. **Turing Test:** Menurut Anda, apakah ChatGPT atau Claude sudah "lulus" Turing Test? Apakah kemampuan menghasilkan teks yang meyakinkan berarti mesin tersebut benar-benar "berpikir"? Berikan argumentasi.

---

## Tugas Mandiri Minggu 1

1. **Setup Environment:** Pastikan Anda bisa mengakses Google Colab dan menjalankan semua kode di modul ini tanpa error. Screenshot hasil dari setiap langkah.

2. **Eksplorasi Dataset:** Di Google Colab, load dataset lain dari scikit-learn (misalnya `load_wine()` atau `load_digits()`) dan lakukan eksplorasi yang sama seperti kode di atas. Tuliskan insight yang Anda temukan.

3. **Essay Pendek (300-500 kata):** Tuliskan pandangan Anda tentang bagaimana AI akan mempengaruhi Indonesia dalam 10 tahun ke depan. Sebutkan minimal 3 sektor dan kaitkan dengan prinsip *responsible AI* dan nilai-nilai Islami.

---

## Referensi

### Buku Teks

1. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
2. Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
3. Raschka, S., & Mirjalili, V. (2022). *Machine Learning with PyTorch and Scikit-Learn*. Packt Publishing.

### Sumber Online

4. [scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html) — Dokumentasi resmi scikit-learn.
5. [Google Colab Welcome Notebook](https://colab.research.google.com/notebooks/intro.ipynb) — Tutorial pengantar Colab.
6. [Stanford CS229: Machine Learning](https://cs229.stanford.edu/) — Materi kuliah ML dari Stanford.

### Referensi Sejarah AI

7. Turing, A. M. (1950). Computing Machinery and Intelligence. *Mind*, 59(236), 433-460.
8. McCarthy, J., et al. (1955). A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence.

### Referensi Etika

9. Floridi, L., & Cowls, J. (2019). A Unified Framework of Five Principles for AI in Society. *Harvard Data Science Review*, 1(1).
10. Undang-Undang No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP).

---

> **Preview Minggu Depan:** Kita akan membahas **Python untuk AI/ML — Data Preprocessing** — NumPy essentials, Pandas essentials, handling missing values, encoding categorical variables, feature scaling, dan train-test split. Siapkan laptop dan Google Colab Anda!

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
