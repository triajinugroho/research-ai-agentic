# BAB 1: PENGANTAR KECERDASAN BUATAN

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-1.1 | Menjelaskan definisi, ruang lingkup, dan klasifikasi kecerdasan buatan (Weak/Strong/Super AI) | C2 |
| CPMK-1.2 | Menjelaskan sejarah perkembangan AI dari Turing hingga era LLM | C2 |
| CPMK-1.3 | Membedakan pendekatan rule-based, machine learning, dan deep learning | C2 |

---

## Estimasi Waktu

| Aktivitas | Durasi |
|-----------|--------|
| Membaca materi | 90 menit |
| Mengerjakan latihan soal | 60 menit |
| Eksplorasi AI Corner | 30 menit |
| **Total** | **3 jam** |

---

## Prasyarat

- Tidak ada prasyarat khusus (bab pertama)
- Disarankan: pemahaman dasar pemrograman Python
- Disarankan: kemampuan navigasi Google Colab

---

## 1.1 Definisi Kecerdasan Buatan

### 1.1.1 Apa itu Kecerdasan Buatan?

**Kecerdasan Buatan** (*Artificial Intelligence* / AI) adalah cabang ilmu komputer yang bertujuan menciptakan sistem yang dapat melakukan tugas-tugas yang biasanya memerlukan kecerdasan manusia — seperti belajar, bernalar, memecahkan masalah, memahami bahasa, dan mengenali pola.

> "Artificial Intelligence is the science and engineering of making intelligent machines."
> — John McCarthy, 1956

Definisi AI dapat dipahami dari empat perspektif:

| Perspektif | Deskripsi | Contoh |
|------------|-----------|--------|
| **Thinking Humanly** | Sistem yang berpikir seperti manusia | Cognitive modeling, neural networks |
| **Thinking Rationally** | Sistem yang berpikir secara rasional/logis | Expert systems, logic programming |
| **Acting Humanly** | Sistem yang bertindak seperti manusia | Chatbot, Turing Test |
| **Acting Rationally** | Sistem yang bertindak secara rasional (optimal) | Autonomous agents, robotics |

Dalam mata kuliah ini, kita fokus pada perspektif **Acting Rationally** — membangun sistem yang mengambil keputusan optimal berdasarkan data.

### 1.1.2 Klasifikasi AI Berdasarkan Kemampuan

```
                    KECERDASAN BUATAN
                          │
          ┌───────────────┼───────────────┐
          │               │               │
     WEAK AI         STRONG AI        SUPER AI
   (Narrow AI)     (General AI)   (Superintelligence)
          │               │               │
   Satu tugas        Semua tugas      Melampaui
   spesifik          seperti manusia  manusia
          │               │               │
   ✓ ADA SEKARANG    ✗ BELUM ADA     ✗ HIPOTESIS
```

**Weak AI / Narrow AI (AI Sempit):**
- Dirancang untuk **satu tugas spesifik**
- Semua AI yang ada saat ini termasuk kategori ini
- Contoh: Google Translate, Siri, AlphaGo, ChatGPT, rekomendasi Tokopedia
- ChatGPT terlihat "pintar", tetapi sebenarnya adalah narrow AI yang sangat baik dalam pemrosesan bahasa

**Strong AI / General AI (AGI — Artificial General Intelligence):**
- Mampu melakukan **semua tugas intelektual** yang bisa dilakukan manusia
- Bisa belajar, bernalar, dan beradaptasi di berbagai domain
- **Belum tercapai** — masih menjadi tujuan penelitian aktif
- Estimasi para ahli: 20-100 tahun lagi (atau mungkin tidak pernah)

**Super AI (Superintelligence):**
- Melampaui kecerdasan manusia di **semua aspek**
- Masih bersifat **hipotesis** dan spekulatif
- Dibahas oleh Nick Bostrom dalam buku *Superintelligence* (2014)
- Menimbulkan pertanyaan etika yang mendalam

### 1.1.3 AI Narrow vs General: Mengapa Perbedaannya Penting?

| Aspek | Narrow AI | General AI |
|-------|-----------|------------|
| Lingkup tugas | Satu tugas spesifik | Multi-tugas, multi-domain |
| Transfer learning | Terbatas | Fleksibel |
| Common sense | Tidak memiliki | Memiliki |
| Status | Sudah ada | Belum tercapai |
| Contoh | Deteksi spam, face recognition | Belum ada contoh nyata |

> **Penting:** Ketika media menyebut "AI sudah bisa melakukan X", yang dimaksud hampir selalu adalah **Narrow AI**. Jangan tertipu oleh hype — pahami kemampuan dan keterbatasan sebenarnya.

---

## 1.2 Sejarah Kecerdasan Buatan

### 1.2.1 Timeline Perkembangan AI

```
1950          1956          1960-70        1974-80       1980-87
  │             │              │              │             │
  ▼             ▼              ▼              ▼             ▼
Turing Test  Dartmouth     Golden Age    AI Winter I   Expert Systems
(Alan Turing) Conference   (Perceptron,  (Funding cut, (MYCIN, XCON,
"Can machines (John McCarthy  ELIZA,       overpromise)  Lisp machines)
 think?"       coins "AI")   SHRDLU)

1987-93       1997          2006          2012          2017
  │             │              │              │             │
  ▼             ▼              ▼              ▼             ▼
AI Winter II  Deep Blue     Deep Learning  AlexNet      Transformer
(Expert sys.  beats Kasparov (Hinton, LeCun, (ImageNet    (Attention is
 bubble burst) at chess      Bengio)        revolution)  All You Need)

2020          2022          2023          2024-2025
  │             │              │              │
  ▼             ▼              ▼              ▼
GPT-3        ChatGPT       GPT-4,        Multimodal AI,
(Few-shot    (LLM goes     Claude,       AI Agents,
 learning)    mainstream)   Gemini,       Reasoning models
                            Open-source LLMs
```

### 1.2.2 Era-era Penting dalam Sejarah AI

**1950 — Turing Test:**
Alan Turing mempublikasikan paper *"Computing Machinery and Intelligence"* yang mengajukan pertanyaan fundamental: "Can machines think?" Turing Test menjadi benchmark klasik: jika manusia tidak bisa membedakan respons mesin dari manusia, maka mesin dianggap "cerdas".

**1956 — Konferensi Dartmouth:**
John McCarthy, Marvin Minsky, Nathaniel Rochester, dan Claude Shannon mengadakan workshop musim panas di Dartmouth College. Di sinilah istilah **"Artificial Intelligence"** pertama kali diciptakan. Mereka optimis AI setara manusia bisa tercapai dalam satu generasi — prediksi yang terlalu optimis.

**1960-1970 — Golden Age:**
- **Perceptron** (Frank Rosenblatt, 1958) — neuron buatan pertama
- **ELIZA** (Joseph Weizenbaum, 1966) — chatbot pertama
- **SHRDLU** (Terry Winograd, 1971) — natural language understanding
- Pendanaan besar dari DARPA dan pemerintah

**1974-1980 — AI Winter I:**
- Minsky & Papert membuktikan keterbatasan Perceptron (1969)
- Lighthill Report (1973) mengkritik AI di Inggris
- Pendanaan dipotong drastis
- **Pelajaran:** *overpromise and underdeliver* merusak kredibilitas

**1980-1987 — Era Expert Systems:**
- Sistem berbasis aturan (*rule-based*) yang meniru keahlian pakar
- MYCIN (diagnosis medis), XCON (konfigurasi komputer DEC)
- Industri Lisp machine berkembang
- Jepang meluncurkan proyek Fifth Generation Computer

**1987-1993 — AI Winter II:**
- Expert systems terlalu mahal dan sulit di-maintain
- Lisp machine kalah dari workstation umum
- Pendanaan kembali menurun

**1997 — Deep Blue:**
IBM Deep Blue mengalahkan juara catur dunia Garry Kasparov. Ini momen bersejarah, meskipun Deep Blue menggunakan brute force, bukan "kecerdasan" sejati.

**2006-2012 — Kebangkitan Deep Learning:**
- Geoffrey Hinton memperkenalkan **Deep Belief Networks** (2006)
- GPU memungkinkan training neural network besar
- **AlexNet** (2012) memenangkan ImageNet dengan margin besar — membuktikan kekuatan deep learning untuk computer vision

**2017 — Transformer:**
Paper *"Attention is All You Need"* oleh Vaswani et al. memperkenalkan arsitektur **Transformer** — fondasi untuk semua Large Language Models (LLM) modern.

**2022-2025 — Era LLM dan AI Generatif:**
- **ChatGPT** (November 2022) membawa AI ke mainstream
- GPT-4, Claude, Gemini, Llama — LLM semakin canggih
- AI generatif untuk teks, gambar (DALL-E, Midjourney), kode (Copilot)
- Perdebatan tentang AGI semakin intensif

### 1.2.3 Pelajaran dari Sejarah AI

| Periode | Pelajaran |
|---------|-----------|
| AI Winter I & II | Jangan overpromise — tetap realistis tentang kemampuan AI |
| Expert Systems | Pendekatan rule-based memiliki keterbatasan skalabilitas |
| Deep Learning Revival | Data + komputasi + algoritma = breakthrough |
| Era LLM | AI yang berguna = AI yang praktis dan accessible |

---

## 1.3 Jenis AI: Rule-based, Machine Learning, Deep Learning

### 1.3.1 Perbandingan Tiga Pendekatan

```
┌──────────────────────────────────────────────────────────────────┐
│                    PENDEKATAN AI                                  │
│                                                                   │
│  RULE-BASED              MACHINE LEARNING        DEEP LEARNING   │
│  (Simbolik)              (Statistik)             (Neural Network)│
│                                                                   │
│  IF-THEN rules           Belajar dari data       Belajar fitur   │
│  Expert knowledge        Feature engineering     secara otomatis  │
│  Deterministik           Probabilistik           End-to-end       │
│                                                                   │
│  Contoh:                 Contoh:                 Contoh:          │
│  - Spam filter (awal)    - Random Forest         - CNN (gambar)   │
│  - Sistem pakar medis    - SVM                   - RNN/LSTM       │
│  - Chatbot rule-based    - Logistic Regression   - Transformer    │
│                                                                   │
│  ← Lebih interpretable          Lebih powerful →                  │
│  ← Lebih sedikit data           Lebih banyak data →              │
└──────────────────────────────────────────────────────────────────┘
```

### 1.3.2 Rule-based AI (Sistem Berbasis Aturan)

Sistem yang bekerja berdasarkan **aturan IF-THEN** yang ditulis secara eksplisit oleh manusia.

```python
# Contoh rule-based: sistem rekomendasi sederhana
def rekomendasi_produk(kategori, budget):
    """Sistem rekomendasi berbasis aturan"""
    if kategori == "laptop" and budget >= 15000000:
        return "MacBook Air M2 atau ASUS ROG"
    elif kategori == "laptop" and budget >= 8000000:
        return "Lenovo IdeaPad atau Acer Aspire"
    elif kategori == "laptop" and budget < 8000000:
        return "Chromebook atau laptop second"
    elif kategori == "smartphone" and budget >= 10000000:
        return "Samsung Galaxy S24 atau iPhone 15"
    elif kategori == "smartphone" and budget >= 5000000:
        return "Samsung Galaxy A54 atau Xiaomi 13"
    else:
        return "Produk tidak ditemukan"

# Pengujian
print(rekomendasi_produk("laptop", 12000000))
# Output: Lenovo IdeaPad atau Acer Aspire
```

**Kelebihan:** Mudah dipahami, deterministik, transparan
**Kekurangan:** Tidak bisa belajar dari data, sulit di-scale, butuh pakar domain

### 1.3.3 Machine Learning

Sistem yang **belajar pola dari data** tanpa diprogram secara eksplisit untuk setiap aturan.

```python
# Contoh machine learning: klasifikasi menggunakan Decision Tree
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Data: [harga (juta Rp), RAM (GB), storage (GB)] -> kategori
X = np.array([
    [5, 4, 256], [8, 8, 512], [15, 16, 512],
    [20, 16, 1024], [3, 4, 128], [12, 8, 512],
    [25, 32, 1024], [7, 8, 256], [10, 8, 512], [18, 16, 1024]
])
y = np.array([
    'budget', 'mid-range', 'high-end',
    'premium', 'budget', 'mid-range',
    'premium', 'mid-range', 'mid-range', 'high-end'
])

# Melatih model (belajar dari data)
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Prediksi laptop baru
laptop_baru = np.array([[11, 8, 512]])
print(f"Prediksi kategori: {model.predict(laptop_baru)[0]}")
# Output: mid-range
```

**Perbedaan kunci:** Model ML menemukan aturan **secara otomatis** dari data, bukan ditulis manual.

### 1.3.4 Deep Learning

Subset dari machine learning yang menggunakan **neural network berlapis-lapis** (deep neural network) untuk belajar representasi data secara hierarkis.

```
Input → [Layer 1: fitur sederhana] → [Layer 2: fitur menengah] → [Layer N: fitur kompleks] → Output

Contoh Computer Vision:
Piksel → Tepi/Edge → Tekstur → Bagian objek → Objek lengkap → "Kucing"
```

| Aspek | Machine Learning | Deep Learning |
|-------|-----------------|---------------|
| Feature engineering | Manual (oleh manusia) | Otomatis (oleh model) |
| Jumlah data | Bisa sedikit (ratusan) | Butuh banyak (ribuan-jutaan) |
| Komputasi | CPU cukup | Butuh GPU/TPU |
| Interpretabilitas | Lebih mudah | Sulit (*black box*) |
| Contoh algoritma | Random Forest, SVM, kNN | CNN, RNN, Transformer, GAN |

### 1.3.5 Kapan Menggunakan Pendekatan Mana?

| Skenario | Pendekatan yang Tepat | Alasan |
|----------|----------------------|--------|
| Aturan bisnis yang jelas dan statis | Rule-based | Tidak butuh data, transparan |
| Data tabular berukuran sedang | Machine Learning | Efisien, interpretable |
| Data gambar, teks, audio besar | Deep Learning | Bisa belajar fitur kompleks |
| Data sangat sedikit (<100 sampel) | Rule-based atau ML sederhana | DL butuh banyak data |
| Real-time, low-latency | Tergantung model | Rule-based tercepat |

---

## 1.4 Machine Learning Pipeline

### 1.4.1 Pipeline End-to-End

Setiap proyek machine learning mengikuti pipeline standar:

```
┌─────────┐    ┌──────────────┐    ┌─────────┐    ┌────────────┐    ┌────────────┐
│  DATA   │───►│ PREPROCESSING│───►│  MODEL  │───►│ EVALUATION │───►│ DEPLOYMENT │
│Collection│    │  & Feature   │    │Training │    │  & Tuning  │    │            │
│         │    │  Engineering │    │         │    │            │    │            │
└─────────┘    └──────────────┘    └─────────┘    └────────────┘    └────────────┘
     │                │                 │               │                │
  Kumpulkan      Bersihkan,        Pilih &          Ukur performa    Implementasi
  data mentah    transformasi,     latih model      (accuracy, F1,   ke produksi
                 buat fitur                         AUC-ROC)
```

### 1.4.2 Penjelasan Setiap Tahap

**1. Data Collection (Pengumpulan Data):**
- Sumber: database, API, web scraping, sensor, survei
- Contoh Indonesia: data BPS, data Open Data Jakarta, dataset Kaggle Indonesia
- Volume data mempengaruhi pilihan algoritma

**2. Data Preprocessing (Pra-pemrosesan Data):**
- Handling missing values (data kosong)
- Encoding variabel kategorikal (Label Encoding, One-Hot Encoding)
- Scaling/normalisasi fitur (StandardScaler, MinMaxScaler)
- Train-test split (membagi data latih dan data uji)
- Feature engineering (membuat fitur baru dari fitur yang ada)

**3. Model Training (Pelatihan Model):**
- Memilih algoritma yang sesuai
- Melatih model dengan data training
- Tuning hyperparameter

**4. Evaluation (Evaluasi):**
- Mengukur performa model pada data testing
- Metrik: accuracy, precision, recall, F1-score, AUC-ROC
- Cross-validation untuk estimasi performa yang lebih robust

**5. Deployment (Penerapan):**
- Mengimplementasikan model ke sistem produksi
- Monitoring performa model di dunia nyata
- Re-training berkala saat data berubah

### 1.4.3 Contoh Pipeline Sederhana dengan Python

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Data Collection — menggunakan dataset Iris (built-in sklearn)
data = load_iris()
X, y = data.data, data.target

# 2. Preprocessing — split dan scaling
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Model Training
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# 4. Evaluation
y_pred = model.predict(X_test_scaled)
print(f"Akurasi: {accuracy_score(y_test, y_pred):.2%}")
print(f"\nClassification Report:\n{classification_report(y_test, y_pred, target_names=data.target_names)}")

# 5. Deployment — model siap digunakan untuk prediksi baru
sampel_baru = scaler.transform([[5.1, 3.5, 1.4, 0.2]])
prediksi = model.predict(sampel_baru)
print(f"\nPrediksi untuk sampel baru: {data.target_names[prediksi[0]]}")
```

---

## 1.5 Aplikasi AI di Indonesia

### 1.5.1 AI di Industri Indonesia

Indonesia memiliki ekosistem AI yang berkembang pesat:

| Perusahaan/Institusi | Aplikasi AI | Dampak |
|---------------------|-------------|--------|
| **GoTo (Gojek+Tokopedia)** | Rekomendasi produk, dynamic pricing, route optimization, fraud detection | Melayani 100+ juta pengguna |
| **Tokopedia** | Visual search (cari produk dari foto), chatbot seller, demand forecasting | Meningkatkan konversi 30% |
| **Halodoc** | AI-assisted triage, chatbot kesehatan, drug interaction checker | 20+ juta pengguna telemedicine |
| **Bank Indonesia** | Prediksi inflasi, analisis sentimen pasar, deteksi anomali transaksi | Stabilitas moneter nasional |
| **Grab** | ETA prediction, driver allocation, safety scoring | Optimasi jutaan perjalanan/hari |
| **Bukalapak** | Chatbot Mitra, product categorization, pricing intelligence | Mendukung 15+ juta UMKM |

### 1.5.2 STRANAS-AI: Strategi Nasional Kecerdasan Buatan Indonesia

Pemerintah Indonesia meluncurkan **Strategi Nasional Kecerdasan Artifisial (STRANAS-AI) 2020-2045** dengan lima fokus:

```
STRANAS-AI INDONESIA
═══════════════════════════════════════════════════
1. KESEHATAN        → AI untuk diagnosis, drug discovery
2. BIROKRASI        → Otomasi layanan publik, smart government
3. PENDIDIKAN       → Adaptive learning, AI tutor
4. KETAHANAN PANGAN → Precision agriculture, prediksi cuaca
5. MOBILITAS        → Smart transportation, autonomous vehicles
═══════════════════════════════════════════════════
Target: Indonesia menjadi hub AI di Asia Tenggara 2045
```

### 1.5.3 Peluang Karier AI di Indonesia

Berdasarkan data LinkedIn dan Glints Indonesia 2024-2025:

| Posisi | Gaji Fresh Graduate (Rp/bulan) | Skill Utama |
|--------|-------------------------------|-------------|
| AI/ML Engineer | 12-25 juta | Python, TensorFlow, PyTorch, MLOps |
| Data Scientist | 10-20 juta | Statistik, ML, SQL, komunikasi data |
| Data Engineer | 10-18 juta | SQL, Spark, Airflow, cloud platform |
| NLP Engineer | 15-25 juta | NLP, Transformer, Hugging Face |
| Computer Vision Engineer | 12-22 juta | CNN, OpenCV, image processing |
| AI Product Manager | 15-30 juta | Pemahaman AI, product strategy |

> **Fakta:** Indonesia membutuhkan **600.000 talenta digital tambahan per tahun** hingga 2030 (Kemenkominfo, 2024). Keahlian AI/ML adalah salah satu skill yang paling dicari.

---

## 1.6 Etika AI dan Nilai-Nilai Islami

### 1.6.1 Isu Etika dalam AI

AI membawa tantangan etika yang serius:

| Isu Etika | Deskripsi | Contoh Kasus |
|-----------|-----------|--------------|
| **Bias & Diskriminasi** | Model mempelajari bias dari data historis | Amazon AI recruitment yang bias terhadap wanita |
| **Privasi Data** | Pengumpulan dan penggunaan data pribadi | Clearview AI memindai wajah tanpa izin |
| **Transparansi** | AI "black box" sulit dijelaskan | Penolakan kredit tanpa alasan yang jelas |
| **Penggantian Pekerjaan** | Otomasi mengancam pekerjaan tertentu | Self-checkout menggantikan kasir |
| **Deepfake** | Pemalsuan konten yang sangat realistis | Video palsu untuk disinformasi |
| **Senjata Otonom** | AI dalam konteks militer | Drone otonom tanpa pengawasan manusia |

### 1.6.2 Prinsip Etika AI Global

Berbagai organisasi telah merumuskan prinsip etika AI:

1. **Fairness (Keadilan):** AI tidak boleh mendiskriminasi berdasarkan ras, gender, agama, atau kelompok
2. **Transparency (Transparansi):** Proses pengambilan keputusan AI harus bisa dijelaskan
3. **Privacy (Privasi):** Data pribadi harus dilindungi
4. **Accountability (Akuntabilitas):** Ada pihak yang bertanggung jawab atas keputusan AI
5. **Safety (Keamanan):** AI harus aman dan tidak membahayakan

### 1.6.3 Perspektif Islam terhadap AI

Sebagai mahasiswa Universitas Al Azhar Indonesia, kita memaknai etika AI melalui nilai-nilai Islami:

**Amanah (Kepercayaan dan Integritas):**
- Menggunakan AI dengan jujur dan bertanggung jawab
- Tidak mengklaim output AI sebagai karya sendiri
- Menjaga keamanan data yang dipercayakan
- Hadits: *"Tanda orang munafik ada tiga: jika berbicara berdusta, jika berjanji mengingkari, dan jika dipercaya berkhianat."* (HR. Bukhari-Muslim)

**Keadilan ('Adl):**
- Memastikan model AI tidak diskriminatif
- Mempertimbangkan dampak AI terhadap semua kelompok masyarakat
- Al-Qur'an: *"Berlaku adillah, karena adil itu lebih dekat kepada takwa."* (QS. Al-Maidah: 8)

**Transparansi (Shaffafiyyah):**
- Menjelaskan bagaimana model AI mengambil keputusan
- Mendokumentasikan penggunaan AI dalam pekerjaan akademik
- Terbuka tentang keterbatasan dan risiko model

**Al-Khwarizmi Heritage:**
Perlu dicatat bahwa kata **"algoritma"** berasal dari nama ilmuwan Muslim **Abu Abdallah Muhammad ibn Musa al-Khwarizmi** (780-850 M) dari Persia. Beliau menulis buku *"Kitab al-Jabr wal-Muqabalah"* yang menjadi dasar aljabar dan ilmu komputasi. Sebagai mahasiswa informatika muslim, kita mewarisi tradisi keilmuan yang panjang dan mulia.

```
AL-KHWARIZMI (780-850 M)
═══════════════════════════════════════════════
Kontribusi:
├── Kitab al-Jabr wal-Muqabalah → ALJABAR
├── Sistem bilangan Hindu-Arab → ANGKA 0-9
├── Metode penyelesaian sistematik → ALGORITMA
└── Tabel astronomi → KOMPUTASI NUMERIK

Warisan: Setiap kali kita menulis algoritma,
kita melanjutkan tradisi keilmuan Islam.
═══════════════════════════════════════════════
```

### 1.6.4 Responsible AI Development

Sebagai calon praktisi AI, mahasiswa harus menginternalisasi prinsip **Responsible AI**:

1. **Design with empathy** — pertimbangkan dampak sosial sejak awal
2. **Test for bias** — uji model terhadap berbagai kelompok demografis
3. **Document everything** — catat keputusan desain, data, dan limitasi
4. **Human-in-the-loop** — manusia tetap dalam proses pengambilan keputusan kritis
5. **Continuous monitoring** — pantau model setelah deployment

---

## 1.7 Kontrak Kuliah dan Kebijakan AI

### 1.7.1 Tujuan Mata Kuliah

Mata kuliah **Kecerdasan Buatan dan Machine Learning** bertujuan memberikan mahasiswa:
1. Pemahaman konseptual tentang AI dan ML
2. Kemampuan praktis membangun model ML menggunakan Python
3. Pemahaman matematika dasar di balik algoritma ML
4. Kesadaran etika dalam pengembangan dan penggunaan AI

### 1.7.2 Kebijakan Penggunaan AI

| Komponen | Kebijakan AI |
|----------|-------------|
| **Tugas Mingguan** | AI BOLEH digunakan, WAJIB didokumentasikan dalam AI Usage Log |
| **Kuis** | AI TIDAK BOLEH digunakan (closed-book, di kelas) |
| **UTS** | AI TIDAK BOLEH digunakan (closed-book) |
| **Proyek Akhir** | AI BOLEH digunakan, WAJIB didokumentasikan secara detail |
| **UAS** | AI TIDAK BOLEH digunakan (closed-book) |

### 1.7.3 Template AI Usage Log

Setiap tugas yang menggunakan AI harus menyertakan dokumentasi berikut:

```markdown
## AI Usage Documentation
### Tool yang Digunakan
- [Nama tool: Claude / ChatGPT / GitHub Copilot / dll]

### Prompt yang Diberikan
- [Copy-paste prompt Anda]

### Output yang Diterima
- [Ringkasan output AI]

### Modifikasi yang Dilakukan
- [Apa yang Anda ubah/tambahkan dari output AI]

### Refleksi Pembelajaran
- [Apa yang Anda pelajari dari interaksi ini?]
```

> **Prinsip:** AI adalah **partner belajar**, bukan pengganti proses berpikir. Mahasiswa yang hanya copy-paste dari AI tidak akan memahami materi dan akan kesulitan saat ujian (closed-book).

---

## 1.8 AI Corner: Mengenal AI — Meta-Learning

### 1.8.1 Menggunakan AI untuk Belajar tentang AI

Level: **Basic**

Di bab pertama ini, kita akan menggunakan AI untuk mempelajari AI itu sendiri — sebuah meta-learning experience.

| AI Bisa | AI Tidak Bisa |
|---------|--------------|
| Menjelaskan konsep AI dengan analogi sederhana | Memahami tingkat pemahaman Anda secara mendalam |
| Memberikan contoh implementasi AI | Menggantikan pengalaman hands-on coding |
| Meringkas sejarah dan tren AI | Memprediksi masa depan AI secara akurat |
| Menjelaskan perbedaan teknik ML | Memilihkan karier AI yang tepat untuk Anda |

### 1.8.2 Latihan Prompting

**Prompt yang Baik:**
```
Saya mahasiswa informatika semester 3 di Indonesia, baru mulai belajar AI/ML.
Jelaskan perbedaan antara supervised learning dan unsupervised learning
menggunakan analogi dari kehidupan sehari-hari di Indonesia.
Berikan 2 contoh aplikasi masing-masing yang relevan dengan Indonesia.
```

**Prompt yang Kurang Baik:**
```
Jelaskan machine learning
```

### 1.8.3 Aktivitas: Eksplorasi dengan AI

1. Tanyakan pada ChatGPT/Claude: *"Sebutkan 5 aplikasi AI yang saya gunakan sehari-hari tanpa sadar"*
2. Verifikasi jawabannya — apakah benar-benar menggunakan AI?
3. Cari satu contoh bias AI di Indonesia atau Asia Tenggara
4. Dokumentasikan dalam AI Usage Log

### 1.8.4 Progresi AI Corner Sepanjang Buku

| Bab | Level | Fokus AI Corner |
|-----|-------|-----------------|
| 1-3 | Basic | Mengenal AI tools, prompting dasar |
| 4-6 | Basic-Intermediate | Menggunakan AI untuk EDA dan preprocessing |
| 7-9 | Intermediate | AI untuk model selection dan debugging |
| 10-12 | Advanced | AI untuk hyperparameter tuning dan interpretasi |
| 13-14 | Expert | AI sebagai co-developer dalam proyek ML |

---

## Rangkuman Bab 1

1. **Kecerdasan Buatan (AI)** adalah ilmu membuat mesin yang dapat melakukan tugas yang memerlukan kecerdasan manusia. AI saat ini termasuk **Narrow AI** — hebat di satu tugas spesifik.
2. **Sejarah AI** penuh dengan siklus optimisme dan kekecewaan (AI Winters). Breakthrough terbaru: deep learning (2012) dan LLM (2022+).
3. Tiga pendekatan utama AI: **rule-based** (aturan manual), **machine learning** (belajar dari data), dan **deep learning** (neural network berlapis).
4. **ML Pipeline** terdiri dari: Data Collection → Preprocessing → Model Training → Evaluation → Deployment.
5. Indonesia memiliki ekosistem AI yang berkembang pesat — GoTo, Halodoc, Bank Indonesia, dan STRANAS-AI 2020-2045.
6. **Etika AI** harus dijunjung tinggi: fairness, transparency, privacy, accountability, safety. Nilai-nilai Islami (amanah, keadilan, transparansi) sejalan dengan prinsip Responsible AI.
7. Kata **"algoritma"** berasal dari nama Al-Khwarizmi — warisan tradisi keilmuan Islam.
8. AI adalah **partner belajar**, bukan pengganti. Penggunaan AI harus didokumentasikan dalam AI Usage Log.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan antara Weak AI (Narrow AI) dan Strong AI (AGI). Berikan masing-masing dua contoh.

**Soal 2.** Sebutkan lima tonggak sejarah penting dalam perkembangan AI (dari 1950 hingga 2025) dan jelaskan signifikansi masing-masing dalam satu kalimat.

**Soal 3.** Apa yang dimaksud dengan "AI Winter"? Mengapa AI Winter terjadi, dan apa pelajaran yang bisa diambil?

**Soal 4.** Jelaskan perbedaan antara pendekatan rule-based dan machine learning. Kapan masing-masing lebih tepat digunakan?

**Soal 5.** Sebutkan lima tahap dalam ML Pipeline dan jelaskan tujuan masing-masing tahap dalam satu kalimat.

### Tingkat Menengah (C2-C3)

**Soal 6.** Perhatikan skenario berikut. Untuk masing-masing, tentukan pendekatan mana yang paling sesuai (rule-based, ML, atau deep learning) dan berikan alasannya:
- a) Mendeteksi email spam berdasarkan kata kunci tertentu
- b) Mengenali wajah dalam foto dengan jutaan variasi
- c) Menghitung diskon berdasarkan level membership pelanggan
- d) Memprediksi harga rumah berdasarkan lokasi, luas, dan fasilitas
- e) Menerjemahkan teks Indonesia ke Inggris secara real-time

**Soal 7.** STRANAS-AI Indonesia memiliki 5 fokus utama. Pilih salah satu dan jelaskan:
- a) Masalah spesifik yang ingin diselesaikan AI di bidang tersebut
- b) Contoh implementasi AI yang sudah ada atau bisa dikembangkan
- c) Tantangan etika yang mungkin muncul

**Soal 8.** Jelaskan bagaimana nilai-nilai Islam (amanah, keadilan, transparansi) dapat diterapkan dalam pengembangan sistem AI rekomendasi produk di e-commerce Indonesia. Berikan contoh konkret untuk setiap nilai.

### Tingkat Mahir (C3-C4)

**Soal 9.** Analisis kasus berikut: Sebuah bank di Indonesia menggunakan model ML untuk menentukan kelayakan kredit nasabah. Model ini dilatih dengan data historis 5 tahun terakhir.
- a) Potensi bias apa yang mungkin ada dalam data historis tersebut?
- b) Bagaimana bias ini bisa berdampak pada kelompok tertentu?
- c) Langkah apa yang harus diambil untuk memastikan model ini adil (fair)?
- d) Bagaimana prinsip transparansi diterapkan jika nasabah ditolak oleh model?

**Soal 10.** Buat esai singkat (200-300 kata) yang membandingkan kondisi ekosistem AI di Indonesia saat ini dengan negara tetangga (Singapura atau Malaysia). Bahas dari aspek: regulasi, talenta, investasi, dan adopsi industri. Gunakan data/referensi yang bisa Anda temukan.

---

## Daftar Pustaka Bab 1

1. Russell, S. J., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
2. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
3. McCarthy, J. (2007). *What is Artificial Intelligence?* Stanford University.
4. Turing, A. M. (1950). Computing Machinery and Intelligence. *Mind*, 59(236), 433-460.
5. Vaswani, A., et al. (2017). Attention is All You Need. *Advances in Neural Information Processing Systems*, 30.
6. Kementerian Komunikasi dan Informatika RI. (2020). *Strategi Nasional Kecerdasan Artifisial Indonesia 2020-2045*.
7. Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press.
8. World Economic Forum. (2025). *The Future of Jobs Report 2025*. WEF.
9. Google, Temasek, & Bain. (2024). *e-Conomy SEA 2024*.

---

*Bab berikutnya: **Bab 2 — Python untuk AI dan Machine Learning***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
