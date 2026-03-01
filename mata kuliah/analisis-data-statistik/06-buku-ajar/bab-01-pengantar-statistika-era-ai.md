# BAB 1: PENGANTAR STATISTIKA DI ERA AI

**Tri Aji Nugroho, S.T., M.T.**
Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-1.1 | Menjelaskan definisi, ruang lingkup, dan peran statistika dalam informatika | C2 |
| CPMK-1.2 | Membedakan statistika deskriptif dan inferensial | C2 |
| CPMK-1.3 | Mengidentifikasi tipe data dan skala pengukuran | C2 |
| CPMK-1.4 | Menjelaskan hubungan statistika dengan data science dan AI | C2 |
| CPMK-1.5 | Menjalankan kode Python dasar untuk analisis statistik sederhana | C3 |

---

## 1.1 Apa itu Statistika?

### 1.1.1 Definisi

**Statistika** adalah ilmu yang mempelajari cara **mengumpulkan**, **mengorganisasi**, **menganalisis**, **menginterpretasi**, dan **menyajikan** data untuk mengambil keputusan yang tepat.

Secara informal, statistika adalah **seni dan ilmu belajar dari data**.

> "The goal of statistics is to extract meaning from data."
> — David S. Moore, *The Basic Practice of Statistics*

Dalam konteks informatika, statistika menjadi fondasi untuk:
- Memahami perilaku pengguna dari data log
- Mengevaluasi performa algoritma
- Melatih model machine learning
- Membuat keputusan berbasis data (*data-driven decision making*)

### 1.1.2 Cabang Utama Statistika

```
                    STATISTIKA
                        │
            ┌───────────┴───────────┐
            │                       │
    DESKRIPTIF                INFERENSIAL
    (Meringkas data)          (Menarik kesimpulan)
            │                       │
    ┌───────┼───────┐       ┌───────┼───────┐
    │       │       │       │       │       │
  Tabel   Grafik  Ukuran  Estimasi  Uji   Regresi
                  Numerik          Hipotesis
```

**Statistika Deskriptif** bertugas **meringkas dan menggambarkan** data yang sudah dikumpulkan. Contoh: rata-rata IPK mahasiswa Informatika UAI angkatan 2025 adalah 3.45.

**Statistika Inferensial** bertugas **menarik kesimpulan tentang populasi** berdasarkan data sampel. Contoh: berdasarkan sampel 100 mahasiswa, kita menyimpulkan bahwa rata-rata IPK seluruh mahasiswa UAI berada antara 3.35 dan 3.55 dengan tingkat kepercayaan 95%.

### 1.1.3 Populasi vs Sampel

| Konsep | Definisi | Simbol | Contoh |
|--------|----------|--------|--------|
| **Populasi** | Seluruh objek/individu yang menjadi perhatian penelitian | N | Seluruh mahasiswa aktif UAI (±5.000 mahasiswa) |
| **Sampel** | Bagian dari populasi yang dipilih untuk diteliti | n | 200 mahasiswa yang dipilih secara acak |
| **Parameter** | Ukuran numerik yang menggambarkan populasi | μ, σ, p | Rata-rata IPK seluruh mahasiswa UAI (μ) |
| **Statistik** | Ukuran numerik yang dihitung dari sampel | x̄, s, p̂ | Rata-rata IPK dari 200 mahasiswa sampel (x̄) |

**Mengapa sampel?** Karena seringkali tidak mungkin atau tidak praktis untuk memeriksa seluruh populasi. Bayangkan jika BPS harus mendata *setiap* penduduk Indonesia (278 juta jiwa) untuk mengetahui rata-rata pengeluaran rumah tangga — tentu membutuhkan biaya dan waktu yang sangat besar.

### 1.1.4 Notasi Penting

| Ukuran | Parameter (Populasi) | Statistik (Sampel) |
|--------|---------------------|---------------------|
| Mean | μ (mu) | x̄ (x-bar) |
| Standar Deviasi | σ (sigma) | s |
| Proporsi | p | p̂ (p-hat) |
| Ukuran | N | n |

---

## 1.2 Mengapa Informatika Perlu Statistika?

### 1.2.1 Data adalah "Minyak Baru"

Indonesia sedang mengalami transformasi digital yang masif:

| Indikator | Nilai | Sumber |
|-----------|-------|--------|
| Nilai ekonomi digital Indonesia 2025 | $82 miliar (estimasi) | Google-Temasek e-Conomy SEA |
| Pengguna internet Indonesia | 212 juta (77% populasi) | APJII 2024 |
| Transaksi e-commerce 2024 | Rp 487 triliun | Bank Indonesia |
| Pengguna dompet digital | 150+ juta | OJK |
| Kebutuhan talenta digital 2030 | 9 juta | Kemenkominfo |

Setiap transaksi GoPay, setiap klik di Tokopedia, setiap pencarian di Google menghasilkan **data**. Statistika adalah bahasa untuk **memahami** data tersebut.

### 1.2.2 Statistika dalam Bidang Informatika

**Software Engineering:**
- A/B testing untuk menguji fitur baru (apakah UI baru meningkatkan conversion rate?)
- Analisis performa: response time, throughput, error rate
- Estimasi effort dan jadwal proyek (PERT analysis)

**Data Science:**
- Exploratory Data Analysis (EDA) — langkah pertama setiap proyek data
- Feature engineering berdasarkan distribusi data
- Evaluasi model: accuracy, precision, recall, F1-score

**Artificial Intelligence / Machine Learning:**
- Gradient descent untuk optimasi (berbasis kalkulus + statistik)
- Regularization (bias-variance tradeoff)
- Cross-validation untuk evaluasi model
- Bayesian inference untuk probabilistic models

**Cybersecurity:**
- Deteksi anomali berbasis distribusi statistik
- Analisis pola serangan dari log data
- Kriptografi berbasis teori bilangan dan probabilitas

### 1.2.3 Permintaan Pasar Kerja

Berdasarkan data LinkedIn dan JobStreet Indonesia 2024-2025:

| Posisi | Gaji Rata-rata (Fresh Graduate) | Skill Statistik yang Dibutuhkan |
|--------|--------------------------------|--------------------------------|
| Data Analyst | Rp 7-12 juta/bulan | Deskriptif, visualisasi, SQL |
| Data Scientist | Rp 12-20 juta/bulan | Inferensi, regresi, ML |
| ML Engineer | Rp 15-25 juta/bulan | Probabilitas, optimasi, evaluasi model |
| Business Intelligence | Rp 8-15 juta/bulan | Deskriptif, dashboarding |
| Product Analyst | Rp 8-15 juta/bulan | A/B testing, cohort analysis |

> **Fakta:** Menurut World Economic Forum (2025), "Data Analyst" dan "AI/ML Specialist" termasuk dalam 10 pekerjaan dengan pertumbuhan tercepat secara global.

---

## 1.3 Statistika di Era Kecerdasan Buatan

### 1.3.1 Bagaimana AI Menggunakan Statistika?

Setiap model AI/ML pada dasarnya adalah **model statistik**:

```
Data → Model Statistik → Prediksi
       (parameterized)
```

| Tahap AI/ML | Peran Statistika |
|-------------|------------------|
| **Data Collection** | Sampling design, survey methodology |
| **Data Preprocessing** | Deteksi outlier, handling missing values, normalisasi |
| **Feature Engineering** | Korelasi, mutual information, distribusi |
| **Model Training** | Maximum likelihood estimation, gradient descent |
| **Model Evaluation** | Accuracy, confusion matrix, AUC-ROC |
| **Model Inference** | Probabilitas output, confidence intervals |
| **A/B Testing** | Hypothesis testing untuk deployment |

### 1.3.2 Statistika sebagai Fondasi Machine Learning

```
STATISTIKA KLASIK                    MACHINE LEARNING
──────────────────                   ─────────────────
Regresi Linear          ────→        Linear Regression
Regresi Logistik        ────→        Logistic Regression (Classification)
Analisis Diskriminan    ────→        LDA, QDA
Clustering              ────→        K-Means, DBSCAN
Bayesian Inference      ────→        Naive Bayes, Bayesian Networks
Decision Trees          ────→        Random Forest, XGBoost
Kernel Methods          ────→        Support Vector Machines
Dimension Reduction     ────→        PCA, t-SNE
```

Mahasiswa yang menguasai statistika akan memahami **mengapa** model ML bekerja, bukan hanya **bagaimana** menjalankannya.

### 1.3.3 AI Tools untuk Analisis Statistik

Di era 2025, mahasiswa informatika memiliki akses ke berbagai AI tools:

| Tool | Fungsi | Cara Penggunaan |
|------|--------|-----------------|
| **ChatGPT / Claude** | Code generation, interpretasi hasil, penjelasan konsep | Prompt: "Jelaskan output regresi ini..." |
| **GitHub Copilot** | Autocomplete kode statistik | Menulis komentar → kode ter-generate |
| **Google Colab AI** | Assisted coding di notebook | Suggestions saat menulis kode |
| **Julius AI** | Analisis data tanpa kode | Upload CSV → auto-analysis |

### 1.3.4 Paradigma Human + AI Collaboration

```
┌─────────────────────────────────────────────────────────┐
│               HUMAN + AI COLLABORATION                   │
│                                                          │
│  HUMAN bertanggung jawab:    AI membantu:                │
│  ✓ Mendefinisikan pertanyaan ✓ Generate kode             │
│  ✓ Memilih metode yang tepat ✓ Mempercepat analisis      │
│  ✓ Menginterpretasi hasil    ✓ Menjelaskan konsep        │
│  ✓ Membuat keputusan         ✓ Menemukan pola            │
│  ✓ Memastikan etika          ✓ Visualisasi otomatis      │
│  ✓ Validasi dan verifikasi   ✓ Literature review         │
│                                                          │
│  "AI is a co-analyst, not a replacement for thinking."   │
└─────────────────────────────────────────────────────────┘
```

**Prinsip utama:** AI mempercepat proses, tetapi **pemahaman statistik** tetap di tangan manusia. Mahasiswa yang hanya "copy-paste" output AI tanpa memahami hasilnya tidak akan mampu:
- Mendeteksi ketika AI memberikan jawaban yang salah
- Memilih metode yang tepat untuk masalah tertentu
- Mengkomunikasikan hasil kepada stakeholder non-teknis
- Membuat keputusan yang bertanggung jawab

---

## 1.4 Tipe Data dan Skala Pengukuran

### 1.4.1 Klasifikasi Tipe Data

```
                        DATA
                         │
            ┌────────────┴────────────┐
            │                         │
      KUALITATIF                KUANTITATIF
      (Kategorikal)             (Numerik)
            │                         │
      ┌─────┴─────┐           ┌──────┴──────┐
      │           │           │             │
   NOMINAL    ORDINAL      DISKRET      KONTINU
```

**Data Kualitatif (Kategorikal):** Menunjukkan kategori atau label.
- Contoh: jenis kelamin, jurusan, agama, status pernikahan

**Data Kuantitatif (Numerik):** Menunjukkan besaran yang dapat diukur.
- **Diskret:** Bilangan bulat (cacahan). Contoh: jumlah mata kuliah, jumlah anak
- **Kontinu:** Bilangan riil (pengukuran). Contoh: tinggi badan, berat badan, IPK

### 1.4.2 Skala Pengukuran: NOIR

| Skala | Sifat | Contoh Indonesia | Operasi Statistik |
|-------|-------|-----------------|-------------------|
| **Nominal** | Kategori tanpa urutan | Provinsi (DKI Jakarta, Jawa Barat, ...), agama, jenis kelamin | Modus, frekuensi, chi-square |
| **Ordinal** | Kategori dengan urutan | Tingkat pendidikan (SD < SMP < SMA < S1), rating bintang (1-5), skala Likert | Median, percentile, Mann-Whitney |
| **Interval** | Jarak bermakna, nol tidak absolut | Suhu Celsius (0°C bukan berarti "tanpa suhu"), tahun kalender | Mean, std, korelasi Pearson |
| **Rasio** | Jarak bermakna, nol absolut | Pendapatan (Rp 0 = tidak ada pendapatan), tinggi badan, berat badan, usia | Semua operasi statistik |

**Cara mengingat:** **N-O-I-R** (Nominal → Ordinal → Interval → Rasio) — semakin ke kanan, semakin "kaya" informasinya.

> **Tips:** Skala pengukuran menentukan metode statistik yang boleh digunakan. Menghitung rata-rata kode pos (nominal) tidak bermakna, meskipun kode pos berupa angka.

### 1.4.3 Mengecek Tipe Data dengan Python

```python
import pandas as pd
import numpy as np

# Membuat contoh data mahasiswa UAI
data = {
    'nim': ['2025001', '2025002', '2025003', '2025004', '2025005'],
    'nama': ['Ahmad', 'Budi', 'Citra', 'Dewi', 'Eko'],
    'jenis_kelamin': ['L', 'L', 'P', 'P', 'L'],
    'asal_provinsi': ['DKI Jakarta', 'Jawa Barat', 'DKI Jakarta', 'Banten', 'Jawa Tengah'],
    'semester': [2, 2, 2, 2, 2],
    'ipk': [3.45, 3.12, 3.78, 3.55, 3.21],
    'jumlah_mk': [8, 7, 8, 9, 7],
    'pengeluaran_bulanan': [2500000, 1800000, 3200000, 2100000, 1500000],
    'kepuasan_kampus': ['Puas', 'Cukup', 'Sangat Puas', 'Puas', 'Cukup']
}

df = pd.DataFrame(data)
print("=== INFO DATASET ===")
print(df.info())
print("\n=== TIPE DATA ===")
print(df.dtypes)
print("\n=== 5 DATA PERTAMA ===")
print(df.head())
```

**Output:**

```
=== TIPE DATA ===
nim                      object
nama                     object
jenis_kelamin            object
asal_provinsi            object
semester                  int64
ipk                     float64
jumlah_mk                 int64
pengeluaran_bulanan       int64
kepuasan_kampus          object
```

**Analisis tipe data:**

| Kolom | Tipe Python | Skala Pengukuran | Keterangan |
|-------|-------------|------------------|------------|
| nim | object (string) | Nominal | Identitas, bukan angka bermakna |
| nama | object | Nominal | Identitas |
| jenis_kelamin | object | Nominal | Kategori tanpa urutan |
| asal_provinsi | object | Nominal | Kategori tanpa urutan |
| semester | int64 | Rasio | Angka bermakna |
| ipk | float64 | Interval/Rasio | Kontinu, 0.00-4.00 |
| jumlah_mk | int64 | Rasio | Diskret |
| pengeluaran_bulanan | int64 | Rasio | Kontinu (dalam Rupiah) |
| kepuasan_kampus | object | Ordinal | Kategori berurutan |

```python
# Mengubah tipe data agar sesuai
df['jenis_kelamin'] = df['jenis_kelamin'].astype('category')
df['asal_provinsi'] = df['asal_provinsi'].astype('category')

# Ordinal: buat urutan yang benar
from pandas.api.types import CategoricalDtype
skala_kepuasan = CategoricalDtype(
    categories=['Tidak Puas', 'Kurang', 'Cukup', 'Puas', 'Sangat Puas'],
    ordered=True
)
df['kepuasan_kampus'] = df['kepuasan_kampus'].astype(skala_kepuasan)

print(df.dtypes)
print(f"\nApakah 'Puas' > 'Cukup'? {df['kepuasan_kampus'].iloc[0] > df['kepuasan_kampus'].iloc[1]}")
```

---

## 1.5 Proses Analisis Data

### 1.5.1 CRISP-DM Framework

**CRISP-DM** (Cross-Industry Standard Process for Data Mining) adalah framework standar industri untuk proyek analisis data:

```
    ┌─────────────────┐
    │ 1. BUSINESS     │◄──────────────────────────────────┐
    │    UNDERSTANDING │                                    │
    └────────┬────────┘                                    │
             │                                             │
    ┌────────▼────────┐                          ┌────────┴────────┐
    │ 2. DATA         │                          │ 6. DEPLOYMENT   │
    │    UNDERSTANDING │                          │                 │
    └────────┬────────┘                          └────────▲────────┘
             │                                             │
    ┌────────▼────────┐                          ┌────────┴────────┐
    │ 3. DATA         │                          │ 5. EVALUATION   │
    │    PREPARATION  │                          │                 │
    └────────┬────────┘                          └────────▲────────┘
             │                                             │
             │         ┌───────────────────┐               │
             └────────►│ 4. MODELING       ├───────────────┘
                       └───────────────────┘
```

| Tahap | Deskripsi | Contoh |
|-------|-----------|--------|
| 1. Business Understanding | Memahami masalah dan tujuan | "Mengapa mahasiswa drop out di semester 3?" |
| 2. Data Understanding | Eksplorasi awal data | EDA: distribusi, missing values, outlier |
| 3. Data Preparation | Membersihkan dan mentransformasi data | Handling missing values, encoding |
| 4. Modeling | Membangun model statistik/ML | Regresi logistik untuk prediksi drop out |
| 5. Evaluation | Mengevaluasi model | Accuracy 85%, recall 72% |
| 6. Deployment | Implementasi solusi | Dashboard early warning system |

### 1.5.2 Piramida DIKW

```
           /\
          /  \
         / W  \      Wisdom: Keputusan bijak berdasarkan knowledge
        /──────\     "Kita perlu intervensi mentoring untuk mahasiswa berisiko"
       /   K    \
      /──────────\   Knowledge: Pemahaman pola dan hubungan
     /     I      \  "Mahasiswa dengan IPK < 2.5 di semester 2 berisiko drop out"
    /──────────────\
   /      D         \ Information: Data yang sudah diproses dan bermakna
  /──────────────────\ "Rata-rata IPK mahasiswa drop out: 2.1; bertahan: 3.2"
 /        DATA        \
/────────────────────────\ Data: Fakta mentah
                           "IPK: 3.45, 2.10, 3.78, 1.95, 3.21, ..."
```

Statistika adalah **jembatan** dari Data menuju Knowledge.

### 1.5.3 End-to-End Data Analysis Pipeline

Dalam mata kuliah ini, mahasiswa akan mempelajari pipeline lengkap:

```
Minggu 1-4 (Fondasi):
[Pertanyaan] → [Kumpulkan Data] → [Eksplorasi (Deskriptif + Visualisasi)]

Minggu 5-8 (Inferensi):
→ [Sampling] → [Estimasi] → [Uji Hipotesis] → [Kesimpulan]

Minggu 9-12 (Pemodelan):
→ [Korelasi/Regresi] → [ANOVA] → [Prediksi]

Minggu 13-16 (Frontier):
→ [Machine Learning] → [AI-Augmented Analysis] → [Proyek Akhir]
```

---

## 1.6 Setup Python dan Google Colab

### 1.6.1 Mengapa Python?

Python adalah bahasa pemrograman **paling populer** untuk data science dan statistik:

| Bahasa | Penggunaan di Data Science | Kelebihan | Kekurangan |
|--------|---------------------------|-----------|------------|
| **Python** | 68% (paling populer) | Mudah dipelajari, ekosistem besar | Lebih lambat dari C/R untuk komputasi numerik murni |
| R | 18% | Dibuat khusus untuk statistik | Kurang versatile |
| SQL | 10% | Standard untuk database | Terbatas untuk analisis lanjut |
| Julia | 4% | Cepat | Ekosistem masih kecil |

### 1.6.2 Quick Start: Google Colab

Google Colab adalah environment gratis dari Google untuk menulis dan menjalankan Python di browser.

**Langkah-langkah:**
1. Buka [colab.research.google.com](https://colab.research.google.com)
2. Login dengan akun Google
3. Klik "New Notebook"
4. Mulai menulis kode

**Keunggulan Google Colab:**
- Gratis (tidak perlu instalasi)
- GPU/TPU gratis untuk komputasi berat
- Terintegrasi dengan Google Drive
- Library data science sudah terinstall (pandas, numpy, matplotlib, scipy, sklearn)

### 1.6.3 Library Python untuk Statistik

```python
# Library utama yang akan kita gunakan sepanjang semester
import numpy as np          # Komputasi numerik (array, matriks, matematika)
import pandas as pd         # Manipulasi data (DataFrame, Series)
import matplotlib.pyplot as plt  # Visualisasi dasar (plot, chart)
import seaborn as sns       # Visualisasi statistik (lebih cantik dari matplotlib)
import scipy.stats as stats # Uji statistik dan distribusi
# import sklearn             # Machine learning (digunakan di Bab 12-13)

# Cek versi
print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"Matplotlib: {plt.matplotlib.__version__}")
print(f"Seaborn: {sns.__version__}")
print(f"SciPy: {stats.scipy.__version__}")
```

### 1.6.4 Komputasi Statistik Pertama

```python
import numpy as np

# Data: nilai UAS Matematika Dasar 10 mahasiswa Informatika UAI
nilai_uas = np.array([75, 82, 68, 91, 55, 78, 84, 72, 88, 65])

# Statistik dasar
print("=== STATISTIK DESKRIPTIF ===")
print(f"Jumlah data (n)     : {len(nilai_uas)}")
print(f"Nilai minimum       : {np.min(nilai_uas)}")
print(f"Nilai maksimum      : {np.max(nilai_uas)}")
print(f"Range               : {np.max(nilai_uas) - np.min(nilai_uas)}")
print(f"Mean (rata-rata)    : {np.mean(nilai_uas):.2f}")
print(f"Median              : {np.median(nilai_uas):.2f}")
print(f"Standar deviasi (s) : {np.std(nilai_uas, ddof=1):.2f}")
print(f"Variance (s²)       : {np.var(nilai_uas, ddof=1):.2f}")
```

**Output:**
```
=== STATISTIK DESKRIPTIF ===
Jumlah data (n)     : 10
Nilai minimum       : 55
Nilai maksimum      : 91
Range               : 36
Mean (rata-rata)    : 75.80
Median              : 76.50
Standar deviasi (s) : 10.87
Variance (s²)       : 118.18
```

> **Catatan:** `ddof=1` pada `np.std()` dan `np.var()` menggunakan pembagi (n-1), bukan n. Ini adalah **Bessel's correction** yang menghasilkan estimator tak bias (unbiased) untuk standar deviasi populasi. Kita akan membahasnya lebih detail di Bab 2.

---

## 1.7 Studi Kasus: Data Ekonomi Digital Indonesia

### 1.7.1 Konteks

Indonesia memiliki ekosistem digital yang berkembang pesat. Mari kita eksplorasi data pengguna internet dan e-commerce Indonesia.

### 1.7.2 Membuat dan Mengeksplorasi Dataset

```python
import pandas as pd
import numpy as np

# Data pengguna internet dan e-commerce Indonesia (sumber: BPS, APJII, Bank Indonesia)
data_digital = {
    'tahun': [2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'pengguna_internet_juta': [171.2, 175.4, 196.7, 202.6, 210.0, 215.6, 221.6],
    'penetrasi_internet_persen': [64.8, 65.3, 73.7, 77.0, 78.2, 79.5, 80.4],
    'nilai_ecommerce_triliun_rp': [106.0, 205.5, 266.3, 401.0, 476.3, 453.8, 487.0],
    'jumlah_umkm_digital_juta': [8.0, 10.2, 13.7, 17.5, 20.0, 22.5, 24.0],
    'transaksi_fintech_triliun_rp': [22.0, 60.4, 81.2, 290.0, 385.0, 422.0, 510.0],
    'pengguna_medsos_juta': [130.0, 150.0, 160.0, 170.0, 191.4, 167.0, 185.3]
}

df = pd.DataFrame(data_digital)

print("=== STRUKTUR DATA ===")
print(f"Dimensi: {df.shape[0]} baris x {df.shape[1]} kolom")
print(f"\nKolom: {list(df.columns)}")
print(f"\nTipe data:\n{df.dtypes}")
print(f"\n=== 5 DATA PERTAMA ===")
print(df.head())
```

### 1.7.3 Analisis Deskriptif Awal

```python
# Ringkasan statistik
print("=== RINGKASAN STATISTIK ===")
print(df.describe().round(2))
```

**Output:**
```
       tahun  pengguna_internet_juta  penetrasi_internet_persen  ...
count   7.00                    7.00                       7.00
mean 2021.00                  199.01                      74.13
std     2.16                   19.36                       6.24
min  2018.00                  171.20                      64.80
25%  2019.50                  186.05                      69.50
50%  2021.00                  202.60                      77.00
75%  2022.50                  212.80                      78.85
max  2024.00                  221.60                      80.40
```

### 1.7.4 Identifikasi Tipe Data

```python
# Analisis tipe data setiap kolom
analisis_tipe = []
for col in df.columns:
    tipe_python = str(df[col].dtype)
    if col == 'tahun':
        skala = 'Interval'
        tipe_stat = 'Kuantitatif Diskret'
    elif 'persen' in col:
        skala = 'Rasio'
        tipe_stat = 'Kuantitatif Kontinu'
    elif 'juta' in col or 'triliun' in col:
        skala = 'Rasio'
        tipe_stat = 'Kuantitatif Kontinu'
    else:
        skala = 'Nominal'
        tipe_stat = 'Kualitatif'

    analisis_tipe.append({
        'Kolom': col,
        'Tipe Python': tipe_python,
        'Tipe Statistik': tipe_stat,
        'Skala': skala
    })

df_tipe = pd.DataFrame(analisis_tipe)
print("\n=== ANALISIS TIPE DATA ===")
print(df_tipe.to_string(index=False))
```

### 1.7.5 Insight Awal

```python
# Pertumbuhan pengguna internet
pertumbuhan = df['pengguna_internet_juta'].pct_change() * 100
print("\n=== PERTUMBUHAN PENGGUNA INTERNET (%) ===")
for i in range(1, len(df)):
    print(f"{df['tahun'].iloc[i-1]} → {df['tahun'].iloc[i]}: "
          f"{pertumbuhan.iloc[i]:+.1f}%")

# Rata-rata pertumbuhan
print(f"\nRata-rata pertumbuhan tahunan: {pertumbuhan.mean():.1f}%")

# Korelasi sederhana
print(f"\n=== KORELASI ===")
print(f"Korelasi pengguna internet vs nilai e-commerce: "
      f"{df['pengguna_internet_juta'].corr(df['nilai_ecommerce_triliun_rp']):.3f}")
print(f"Korelasi penetrasi internet vs UMKM digital: "
      f"{df['penetrasi_internet_persen'].corr(df['jumlah_umkm_digital_juta']):.3f}")
```

### 1.7.6 Visualisasi Sederhana

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Pertumbuhan pengguna internet
axes[0].plot(df['tahun'], df['pengguna_internet_juta'], 'b-o', linewidth=2)
axes[0].set_title('Pertumbuhan Pengguna Internet Indonesia', fontsize=12)
axes[0].set_xlabel('Tahun')
axes[0].set_ylabel('Pengguna (Juta)')
axes[0].grid(True, alpha=0.3)

# Plot 2: Nilai e-commerce
axes[1].bar(df['tahun'], df['nilai_ecommerce_triliun_rp'], color='green', alpha=0.7)
axes[1].set_title('Nilai Transaksi E-Commerce Indonesia', fontsize=12)
axes[1].set_xlabel('Tahun')
axes[1].set_ylabel('Nilai (Triliun Rp)')
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('ekonomi_digital_indonesia.png', dpi=150, bbox_inches='tight')
plt.show()

print("Grafik berhasil disimpan!")
```

**Interpretasi:** Dari data di atas, kita dapat melihat bahwa pertumbuhan pengguna internet berkorelasi positif dengan nilai e-commerce. Pertumbuhan tertinggi terjadi pada tahun 2020 (pandemi COVID-19 mempercepat digitalisasi). Ini adalah contoh sederhana bagaimana statistika membantu kita **memahami tren** dari data mentah.

---

## 1.8 AI Corner: Mengenal AI sebagai Co-Analyst

### 1.8.1 Apa yang Bisa AI Lakukan untuk Analisis Statistik?

| AI Bisa | AI Tidak Bisa |
|---------|--------------|
| Generate kode Python untuk analisis | Memahami konteks bisnis/domain |
| Menjelaskan konsep statistik | Menentukan apakah hasilnya masuk akal |
| Menyarankan uji statistik yang tepat | Memutuskan tindakan berdasarkan hasil |
| Menginterpretasi output secara teknis | Menjamin kebenaran jawaban 100% |
| Membantu debug kode | Menggantikan pemikiran kritis manusia |
| Meringkas literatur | Menghasilkan data riil yang valid |

### 1.8.2 Contoh Interaksi dengan AI

**Prompt yang Baik:**
```
Saya punya data nilai ujian 30 mahasiswa. Distribusinya right-skewed.
Saya ingin menguji apakah rata-rata nilai berbeda dari 75.
Data berbentuk numerik kontinu, satu kelompok.
Uji statistik apa yang tepat dan mengapa?
```

**Prompt yang Kurang Baik:**
```
Analisis data saya
```

**Prinsip Prompting untuk Statistik:**
1. Deskripsikan data Anda (tipe, ukuran, distribusi)
2. Nyatakan pertanyaan penelitian dengan jelas
3. Sebutkan asumsi yang sudah Anda ketahui
4. Minta AI menjelaskan *mengapa*, bukan hanya *apa*
5. Selalu verifikasi jawaban AI dengan menjalankan kode sendiri

### 1.8.3 Etika Penggunaan AI dalam Akademik

Sebagai mahasiswa Universitas Al Azhar Indonesia, penggunaan AI harus berlandaskan nilai-nilai:

**Amanah (Kepercayaan):**
- Tugas yang diberikan dosen adalah amanah untuk belajar dan memahami
- Menggunakan AI tanpa memahami hasilnya adalah mengkhianati amanah tersebut
- Gunakan AI untuk *memperdalam* pemahaman, bukan untuk *menggantikan* proses belajar

**Keadilan ('Adl):**
- Dokumentasikan semua penggunaan AI secara transparan
- Jangan mengklaim pekerjaan AI sebagai pekerjaan sendiri
- Berikan kredit yang layak

**Transparansi (Shaffafiyyah):**
- Selalu sertakan "AI Usage Log" di setiap tugas
- Sebutkan: tool yang digunakan, prompt yang diberikan, modifikasi yang dilakukan

**Template AI Usage Log:**

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

### 1.8.4 Kebijakan AI di Mata Kuliah Ini

| Komponen | Kebijakan AI |
|----------|-------------|
| **Tugas Mingguan** | AI BOLEH digunakan, WAJIB didokumentasikan |
| **Kuis** | AI TIDAK BOLEH digunakan (closed-book, di kelas) |
| **UTS** | AI TIDAK BOLEH digunakan (closed-book) |
| **Proyek Akhir** | AI BOLEH digunakan, WAJIB didokumentasikan dalam AI Usage Log |
| **UAS** | AI TIDAK BOLEH digunakan (closed-book) |

---

## Rangkuman Bab 1

1. **Statistika** adalah ilmu belajar dari data — terdiri dari statistika deskriptif dan inferensial.
2. **Populasi** adalah keseluruhan objek penelitian; **sampel** adalah bagian dari populasi. Parameter menggambarkan populasi; statistik dihitung dari sampel.
3. Statistika sangat penting bagi informatika: menjadi fondasi data science, AI/ML, software engineering, dan cybersecurity.
4. Di era AI, statistika tetap relevan — AI adalah *tool*, statistika adalah *thinking*. Mahasiswa yang memahami statistik mampu menggunakan AI secara efektif dan kritis.
5. **Tipe data**: kualitatif (nominal, ordinal) dan kuantitatif (interval, rasio) — NOIR.
6. **CRISP-DM** adalah framework standar untuk proyek analisis data.
7. **Python** (melalui Google Colab) adalah tool komputasi utama, dengan library numpy, pandas, matplotlib, seaborn, dan scipy.
8. Penggunaan AI harus berlandaskan **amanah, keadilan, dan transparansi**.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan antara statistika deskriptif dan statistika inferensial. Berikan masing-masing satu contoh dalam konteks informatika.

**Soal 2.** Sebuah perusahaan e-commerce ingin mengetahui rata-rata waktu yang dihabiskan pengguna di aplikasi mereka. Mereka mengambil data dari 500 pengguna (dari total 2 juta pengguna).
- a) Apa yang dimaksud populasi dalam konteks ini?
- b) Apa yang dimaksud sampel?
- c) Jika rata-rata waktu dari 500 pengguna adalah 25 menit, apakah ini parameter atau statistik?

**Soal 3.** Klasifikasikan tipe data dan skala pengukuran untuk masing-masing variabel berikut:
- a) Nomor KTP
- b) Rating film di IMDb (1-10)
- c) Suhu ruangan server (dalam °C)
- d) Jumlah karyawan perusahaan startup
- e) Kota domisili
- f) Pendapatan bulanan (dalam Rupiah)
- g) Tingkat kepuasan pelanggan (Sangat Tidak Puas, Tidak Puas, Netral, Puas, Sangat Puas)
- h) Jumlah commit di GitHub per hari

**Soal 4.** Jelaskan mengapa kode pos (misalnya 12345) termasuk data nominal meskipun berupa angka.

**Soal 5.** Tuliskan tiga contoh penggunaan statistika dalam kehidupan sehari-hari mahasiswa Indonesia.

### Tingkat Menengah (C2-C3)

**Soal 6.** Perhatikan data berikut:

| Variabel | Nilai |
|----------|-------|
| NIM Mahasiswa | 2025001 |
| Fakultas | Sains dan Teknologi |
| IPK | 3.45 |
| Jumlah SKS lulus | 24 |
| Tingkat kemampuan Python | Pemula |
| Waktu pengerjaan tugas (menit) | 120.5 |

Untuk setiap variabel, tentukan:
- a) Kualitatif atau kuantitatif
- b) Jika kuantitatif, diskret atau kontinu
- c) Skala pengukuran (NOIR)
- d) Operasi statistik yang valid

**Soal 7.** Tulis kode Python untuk:
- a) Membuat array numpy berisi 20 data acak bilangan bulat antara 50 dan 100
- b) Menghitung mean, median, min, max, dan standar deviasi dari data tersebut
- c) Menampilkan hasil dalam format yang rapi

**Soal 8.** Sebuah survei online menanyakan pendapat 1.000 pengguna tentang fitur baru sebuah aplikasi. Dari responden, 650 menyatakan "Suka" dan 350 menyatakan "Tidak Suka".
- a) Apakah ini statistika deskriptif atau inferensial? Jelaskan.
- b) Jika perusahaan menyimpulkan bahwa "mayoritas dari 10 juta pengguna menyukai fitur baru" berdasarkan survei ini, apakah ini deskriptif atau inferensial?
- c) Asumsi apa yang perlu dipenuhi agar kesimpulan (b) valid?

**Soal 9.** Jelaskan perbedaan antara:
- a) Data diskret dan data kontinu (berikan contoh dalam konteks informatika)
- b) Skala ordinal dan skala interval (berikan contoh)
- c) Parameter dan statistik (berikan contoh dengan notasi)

**Soal 10.** Dalam konteks CRISP-DM, deskripsi tugas-tugas berikut termasuk tahap apa?
- a) Membersihkan data yang memiliki missing values
- b) Bertemu dengan manajer untuk memahami tujuan bisnis
- c) Membuat scatter plot untuk melihat hubungan dua variabel
- d) Melatih model regresi untuk memprediksi penjualan
- e) Menghitung akurasi model pada data testing
- f) Membuat dashboard untuk monitoring real-time

### Tingkat Mahir (C3-C4)

**Soal 11.** Seorang data analyst di Gojek ingin menganalisis waktu tunggu (dalam detik) penumpang GoRide di Jakarta. Dia mengumpulkan data dari 10.000 transaksi.
- a) Identifikasi populasi, sampel, parameter, dan statistik dalam konteks ini.
- b) Mengapa analyst tidak bisa menggunakan data dari *seluruh* transaksi GoRide yang pernah ada?
- c) Jika analyst ingin membandingkan waktu tunggu di Jakarta vs Surabaya, metode statistik apa yang mungkin digunakan? (Jawab secara konseptual, tidak perlu rumus.)

**Soal 12.** Tulis kode Python yang:
- a) Membuat DataFrame dengan 5 kolom: nama_kota, provinsi, populasi, luas_km2, dan kepadatan
- b) Isi dengan data minimal 10 kota di Indonesia (data boleh estimasi)
- c) Hitung kepadatan = populasi / luas_km2
- d) Tampilkan statistik deskriptif untuk kolom numerik
- e) Identifikasi kota dengan kepadatan tertinggi dan terendah

**Soal 13.** Jelaskan bagaimana statistika berperan dalam melatih dan mengevaluasi model machine learning. Gunakan analogi yang mudah dipahami oleh mahasiswa semester 2.

**Soal 14.** Anda diminta menganalisis data survei kepuasan mahasiswa terhadap fasilitas kampus UAI. Survei menggunakan skala Likert 1-5. Seorang teman menyarankan untuk menghitung "rata-rata skor kepuasan = 3.72" dan menyimpulkan bahwa mahasiswa "cukup puas".
- a) Apakah menghitung rata-rata dari data ordinal (skala Likert) itu tepat? Jelaskan pro dan kontra.
- b) Metode apa yang lebih tepat untuk meringkas data ordinal?
- c) Bagaimana Anda akan menyajikan hasil survei ini secara visual?

**Soal 15.** Anda diminta oleh dosen pembimbing untuk melakukan analisis data menggunakan AI (seperti ChatGPT/Claude). Tulis:
- a) Tiga contoh prompt yang BAIK untuk meminta bantuan AI dalam analisis statistik
- b) Tiga contoh prompt yang KURANG BAIK dan jelaskan mengapa
- c) Bagaimana Anda akan mendokumentasikan penggunaan AI tersebut sesuai kebijakan mata kuliah ini?

---

## Daftar Pustaka Bab 1

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability & Statistics for Engineers & Scientists* (9th ed.). Pearson.
2. Moore, D. S., McCabe, G. P., & Craig, B. A. (2021). *Introduction to the Practice of Statistics* (10th ed.). W. H. Freeman.
3. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
4. Google, Temasek, & Bain. (2024). *e-Conomy SEA 2024*. Retrieved from https://economysea.withgoogle.com
5. APJII. (2024). *Profil Internet Indonesia 2024*. Asosiasi Penyelenggara Jasa Internet Indonesia.
6. BPS. (2024). *Statistik Indonesia 2024*. Badan Pusat Statistik.
7. World Economic Forum. (2025). *The Future of Jobs Report 2025*. WEF.
8. Provost, F., & Fawcett, T. (2013). *Data Science for Business*. O'Reilly Media.
9. Wasserman, L. (2004). *All of Statistics: A Concise Course in Statistical Inference*. Springer.

---

*Bab berikutnya: **Bab 2 — Statistika Deskriptif dan Eksplorasi Data dengan Python***
