# Minggu 1: Pengantar Statistika di Era AI

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Minggu** | 1 |
| **Topik** | Pengantar Statistika di Era AI |
| **CPMK** | CPMK-1: Memahami peran statistika dalam era AI dan data science |
| **Sub-CPMK** | 1.1 Menjelaskan relevansi statistika di era AI dan data science |
| | 1.2 Mengidentifikasi tools modern untuk analisis statistik |
| | 1.3 Mengklasifikasikan tipe data dan skala pengukuran |
| **Bloom's Taxonomy** | C2 (Memahami / *Understanding*) |
| **Durasi** | 2 x 50 menit |
| **Metode** | Ceramah interaktif, diskusi, hands-on Google Colab |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** mengapa statistika merupakan fondasi penting dalam pengembangan AI, data science, dan pengambilan keputusan berbasis data.
2. **Mengidentifikasi** ekosistem tools modern (Python, Google Colab, AI assistants) yang digunakan dalam analisis statistik kontemporer.
3. **Membedakan** tipe data dan skala pengukuran (nominal, ordinal, interval, rasio) serta memahami prinsip etika data dan *responsible AI*.

---

## Materi Pembelajaran

### 1. Mengapa Statistik Penting di Era AI & Data Science

#### Statistika: Bahasa Universal Data

Di era digital saat ini, data dihasilkan dalam jumlah yang sangat besar setiap detiknya. Namun, data mentah tidak bermakna tanpa kemampuan untuk menganalisis, merangkum, dan mengambil kesimpulan darinya. Di sinilah peran statistika menjadi sangat krusial.

#### Setiap Model AI Menggunakan Statistika

Perlu dipahami bahwa **setiap model AI dan machine learning pada dasarnya dibangun di atas fondasi statistika**:

- **Regresi Linear & Logistik** -- teknik statistik klasik yang menjadi dasar banyak model prediktif.
- **Neural Networks** -- menggunakan optimasi berbasis gradien yang berakar pada kalkulus dan statistika.
- **Natural Language Processing (NLP)** -- memanfaatkan distribusi probabilitas kata dan kalimat.
- **Computer Vision** -- menggunakan konvolusi dan transformasi statistik pada piksel gambar.
- **Large Language Models (LLM)** seperti ChatGPT -- pada intinya adalah model probabilistik yang memprediksi kata berikutnya berdasarkan distribusi statistik dari data pelatihan.

> **Insight:** Tanpa memahami konsep seperti *mean*, *variance*, *probability distribution*, dan *hypothesis testing*, seseorang tidak akan benar-benar memahami bagaimana AI bekerja -- hanya bisa menggunakannya sebagai "kotak hitam".

#### Keputusan Berbasis Data Membutuhkan Statistika

Organisasi modern mengandalkan *data-driven decision making*. Ini membutuhkan:

- Kemampuan merangkum data (*descriptive statistics*)
- Kemampuan menarik kesimpulan dari sampel (*inferential statistics*)
- Kemampuan memprediksi tren ke depan (*predictive analytics*)
- Kemampuan mengevaluasi apakah suatu perubahan signifikan (*hypothesis testing*)

#### Contoh dari Konteks Indonesia

| Perusahaan / Institusi | Penggunaan Statistika & Data |
|---|---|
| **GoTo (Gojek + Tokopedia)** | Algoritma penentuan harga dinamis (*surge pricing*), rekomendasi produk, analisis perilaku pengguna |
| **Tokopedia** | A/B testing untuk fitur baru, analisis *conversion rate*, segmentasi pelanggan |
| **Bank Indonesia** | Analisis inflasi, prediksi pertumbuhan ekonomi, survei konsumen |
| **BPS (Badan Pusat Statistik)** | Sensus penduduk, Survei Sosial Ekonomi Nasional (Susenas), Indeks Pembangunan Manusia (IPM) |
| **Kementerian Kesehatan** | Analisis sebaran penyakit, efektivitas vaksinasi, perencanaan fasilitas kesehatan |

Sebagai mahasiswa di Indonesia, memahami statistika berarti memiliki kemampuan untuk berkontribusi pada pengambilan keputusan yang lebih baik, baik di sektor swasta maupun publik.

---

### 2. Landscape Tools Modern untuk Analisis Statistik

#### Ekosistem Python untuk Statistika

Python telah menjadi bahasa pemrograman paling populer untuk data science dan statistika. Berikut adalah library utama yang akan kita gunakan sepanjang semester:

| Library | Fungsi Utama | Contoh Penggunaan |
|---|---|---|
| **pandas** | Manipulasi dan analisis data tabular | Membaca CSV, filtering, groupby, pivot |
| **numpy** | Komputasi numerik dan array | Operasi matriks, fungsi matematika |
| **scipy** | Fungsi statistik lanjutan | Uji hipotesis, distribusi probabilitas |
| **scikit-learn** | Machine learning | Regresi, klasifikasi, clustering |
| **matplotlib** | Visualisasi data dasar | Line plot, bar chart, scatter plot |
| **seaborn** | Visualisasi statistik yang lebih estetis | Heatmap, boxplot, violin plot |

#### Google Colab: Laboratorium Virtual Kita

**Google Colaboratory** (Colab) adalah lingkungan notebook berbasis cloud yang disediakan gratis oleh Google. Keunggulannya:

- Tidak perlu instalasi apapun di komputer lokal
- Sudah terinstal library Python untuk data science
- Bisa diakses dari browser manapun
- Menyediakan GPU gratis untuk komputasi berat
- Terintegrasi dengan Google Drive untuk menyimpan file

**Cara Mengakses:**
1. Buka [colab.research.google.com](https://colab.research.google.com)
2. Login dengan akun Google
3. Buat notebook baru: *File > New Notebook*

#### AI Assistants sebagai Co-Analyst

Di era AI, kita memiliki asisten cerdas yang bisa membantu proses analisis:

- **ChatGPT / Claude** -- membantu menulis kode, menjelaskan konsep, debugging
- **GitHub Copilot** -- auto-complete kode di editor
- **Google Gemini** -- terintegrasi di Colab untuk membantu coding

> **Penting:** AI adalah *alat bantu*, bukan pengganti pemahaman. Mahasiswa **wajib memahami** konsep di balik kode yang dihasilkan AI. Kita akan membahas kebijakan penggunaan AI di bagian Kontrak Kuliah.

---

### 3. Review: Tipe Data dan Skala Pengukuran

Sebagai review dari Statistika Semester 1, berikut ringkasan tipe data dan skala pengukuran:

#### Tipe Data

```
Data
├── Data Kualitatif (Kategorikal)
│   ├── Nominal    → Label tanpa urutan
│   └── Ordinal    → Label dengan urutan
│
└── Data Kuantitatif (Numerik)
    ├── Diskrit    → Bilangan bulat (cacahan)
    └── Kontinu    → Bilangan real (pengukuran)
```

#### Skala Pengukuran

| Skala | Karakteristik | Contoh | Operasi yang Valid |
|---|---|---|---|
| **Nominal** | Kategori tanpa urutan | Jenis kelamin, agama, provinsi | Modus, frekuensi |
| **Ordinal** | Kategori dengan urutan | Tingkat kepuasan (1-5), ranking | Median, persentil |
| **Interval** | Jarak bermakna, nol tidak absolut | Suhu (Celsius), tahun kalender | Mean, std. deviasi |
| **Rasio** | Jarak bermakna, nol absolut | Berat badan, pendapatan, usia | Semua operasi statistik |

#### Mengapa Ini Penting?

Pemilihan metode statistik yang tepat bergantung pada tipe data yang kita miliki:

- Data **nominal** -- gunakan *chi-square test*, bukan *t-test*
- Data **ordinal** -- gunakan statistik non-parametrik
- Data **interval/rasio** -- bisa gunakan statistik parametrik

Dalam Python, memahami tipe data juga penting untuk memilih tipe kolom yang tepat di pandas (`object`, `category`, `int64`, `float64`).

---

### 4. Etika Data dan Responsible AI

#### Mengapa Etika Data Penting?

Dengan kekuatan data dan AI, datang pula tanggung jawab besar. Beberapa isu etika yang perlu dipahami:

#### a) Data Privacy (Privasi Data)

- Data pribadi harus dilindungi sesuai regulasi (UU PDP No. 27 Tahun 2022 di Indonesia)
- *Personally Identifiable Information* (PII) harus di-anonimkan sebelum analisis
- Prinsip *data minimization*: hanya kumpulkan data yang benar-benar diperlukan

#### b) Informed Consent (Persetujuan)

- Subjek data harus mengetahui dan menyetujui penggunaan datanya
- Transparansi tentang tujuan pengumpulan data
- Hak untuk menarik persetujuan (*right to withdraw*)

#### c) Bias dan Fairness

- Bias dalam data akan menghasilkan bias dalam model AI
- Contoh: model rekrutmen Amazon yang bias terhadap perempuan karena data historis didominasi pelamar laki-laki
- Perlu dilakukan *bias audit* pada data dan model

#### d) Nilai-Nilai Islam dalam Etika Data

Sebagai institusi yang menjunjung nilai-nilai Islam, Universitas Al Azhar Indonesia menghubungkan etika data dengan prinsip-prinsip berikut:

| Nilai Islam | Penerapan dalam Data & AI |
|---|---|
| **Amanah** (Kepercayaan) | Data yang dipercayakan kepada kita harus dijaga dan digunakan sesuai tujuan. Tidak boleh disalahgunakan. |
| **Keadilan** (Al-'Adl) | Analisis data harus adil, tidak diskriminatif. Model AI harus memberikan hasil yang fair bagi semua kelompok. |
| **Transparansi** (Al-Bayan) | Metode analisis harus transparan dan bisa dipertanggungjawabkan. Tidak boleh memanipulasi data atau hasil. |
| **Tidak Merugikan** (La Dharar) | Penggunaan data tidak boleh merugikan pihak lain. Privasi harus dihormati. |

> **Refleksi:** Sebagai seorang analis data atau data scientist, kita tidak hanya bertanggung jawab secara profesional, tetapi juga secara moral dan spiritual atas bagaimana kita mengelola dan menggunakan data.

---

### 5. Kontrak Kuliah

#### Ekspektasi Perkuliahan

- Hadir minimal 75% dari total pertemuan
- Aktif berpartisipasi dalam diskusi dan hands-on
- Mengerjakan semua tugas mandiri dan kelompok
- Membawa laptop yang sudah bisa mengakses Google Colab

#### Komponen Penilaian

| Komponen | Bobot |
|---|---|
| Partisipasi & Kehadiran | 10% |
| Tugas Individu (mingguan) | 20% |
| Proyek Kelompok (Mid) | 20% |
| Ujian Tengah Semester (UTS) | 20% |
| Proyek Akhir & Presentasi | 30% |

#### Kebijakan Penggunaan AI (*AI Policy*)

Mata kuliah ini mengadopsi pendekatan **AI-Augmented Learning**:

1. **Diizinkan:** Menggunakan AI (ChatGPT, Claude, Gemini, dll.) sebagai alat bantu belajar dan coding.
2. **Wajib:** Setiap penggunaan AI harus di-*cite* dan mahasiswa harus mampu **menjelaskan** kode dan konsep yang dihasilkan AI.
3. **Dilarang:** Menyerahkan output AI mentah tanpa pemahaman. Copy-paste tanpa modifikasi dan pemahaman dianggap pelanggaran akademik.
4. **Prinsip:** "AI sebagai *co-pilot*, bukan *auto-pilot*."

---

## Aktivitas Kelas

### Sesi 1: Teori dan Diskusi (50 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Pembukaan & Ice Breaking | Perkenalan, survei awal pengalaman coding mahasiswa |
| 15 menit | Ceramah Interaktif | Mengapa statistik penting di era AI (dengan contoh nyata) |
| 10 menit | Diskusi Kelompok Kecil | "Sebutkan 3 contoh penggunaan data/statistik yang kalian temui sehari-hari" |
| 10 menit | Presentasi & Review | Review tipe data, skala pengukuran, etika data |
| 5 menit | Transisi ke Hands-on | Setup Google Colab, pastikan semua mahasiswa bisa akses |

### Sesi 2: Hands-on Google Colab (50 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Tour Google Colab | Navigasi interface, menjalankan cell, markdown cell |
| 15 menit | Kode Pertama | Load dataset, print informasi dasar |
| 15 menit | Eksplorasi Mandiri | Mahasiswa mencoba sendiri dengan bimbingan |
| 10 menit | Wrap-up & Preview | Rangkuman, preview minggu depan |

---

## Hands-on: Kode Python Pertama di Google Colab

### Langkah 1: Import Library

```python
# Import library yang kita butuhkan
import pandas as pd
import numpy as np

print("Library berhasil di-import!")
print(f"Versi pandas: {pd.__version__}")
print(f"Versi numpy: {np.__version__}")
```

### Langkah 2: Membuat Dataset Sederhana

```python
# Membuat dataset sederhana tentang mahasiswa
data = {
    'nama': ['Aini', 'Budi', 'Citra', 'Dani', 'Eka',
             'Fani', 'Gilang', 'Hana', 'Irfan', 'Jaya'],
    'jurusan': ['Informatika', 'Sistem Informasi', 'Informatika',
                'Sistem Informasi', 'Informatika', 'Informatika',
                'Sistem Informasi', 'Informatika', 'Sistem Informasi',
                'Informatika'],
    'ipk': [3.75, 3.50, 3.85, 3.20, 3.60,
            3.90, 3.45, 3.70, 3.55, 3.80],
    'semester': [4, 6, 4, 6, 2, 2, 4, 6, 4, 2],
    'kepuasan_kuliah': ['Sangat Puas', 'Puas', 'Sangat Puas', 'Cukup',
                        'Puas', 'Sangat Puas', 'Puas', 'Cukup',
                        'Puas', 'Sangat Puas']
}

df = pd.DataFrame(data)
print("Dataset berhasil dibuat!")
```

### Langkah 3: Menampilkan Informasi Dasar

```python
# Melihat 5 baris pertama
print("=== 5 Baris Pertama ===")
print(df.head())
print()

# Melihat informasi tentang dataset
print("=== Informasi Dataset ===")
print(df.info())
print()

# Melihat dimensi dataset (baris, kolom)
print(f"\nJumlah baris: {df.shape[0]}")
print(f"Jumlah kolom: {df.shape[1]}")
print(f"Nama kolom: {list(df.columns)}")
```

### Langkah 4: Statistik Deskriptif Sederhana

```python
# Statistik deskriptif untuk kolom numerik
print("=== Statistik Deskriptif ===")
print(df.describe())
print()

# Menghitung rata-rata IPK
print(f"Rata-rata IPK: {df['ipk'].mean():.2f}")

# Menghitung jumlah mahasiswa per jurusan
print("\n=== Jumlah Mahasiswa per Jurusan ===")
print(df['jurusan'].value_counts())
```

### Langkah 5: Identifikasi Tipe Data

```python
# Melihat tipe data setiap kolom
print("=== Tipe Data Kolom ===")
print(df.dtypes)
print()

# Diskusi: Kolom mana yang nominal? Ordinal? Rasio?
print("Diskusi:")
print("- 'nama'              -> Nominal")
print("- 'jurusan'           -> Nominal")
print("- 'ipk'               -> Rasio")
print("- 'semester'          -> Rasio (diskrit)")
print("- 'kepuasan_kuliah'   -> Ordinal")
```

---

## AI Corner: Bagaimana AI Bisa Membantu Belajar Statistik?

> **Konsep Baru:** Sepanjang semester ini, setiap modul akan memiliki bagian **AI Corner** yang menunjukkan bagaimana memanfaatkan AI secara bertanggung jawab dalam proses belajar.

### Cara AI Bisa Membantu Anda

| Skenario | Contoh Prompt ke AI |
|---|---|
| Memahami konsep | *"Jelaskan perbedaan mean dan median dengan analogi sederhana"* |
| Debugging kode | *"Kode Python ini error: [paste kode]. Apa yang salah?"* |
| Menghasilkan contoh | *"Berikan contoh penggunaan .groupby() di pandas dengan dataset penjualan"* |
| Review pemahaman | *"Buat 5 soal pilihan ganda tentang skala pengukuran data"* |
| Penjelasan output | *"Apa arti output .describe() berikut ini: [paste output]"* |

### Tips Penting

1. **Selalu verifikasi** jawaban AI dengan referensi terpercaya.
2. **Jangan hanya copy-paste** -- pastikan Anda memahami setiap baris kode.
3. **Gunakan AI untuk belajar**, bukan untuk menggantikan proses berpikir.
4. **Dokumentasikan** kapan dan bagaimana Anda menggunakan AI.

### Contoh Prompt Minggu Ini

Coba masukkan prompt berikut ke ChatGPT atau Claude:

```
Saya mahasiswa semester 2 belajar statistik dan Python.
Jelaskan dengan bahasa sederhana:
1. Apa itu pandas DataFrame?
2. Apa perbedaan antara .head() dan .info()?
3. Mengapa kita perlu tahu tipe data sebelum analisis?
```

Bandingkan jawaban AI dengan materi yang sudah dipelajari hari ini.

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai bahan refleksi:

1. **Relevansi Statistika:** Sebutkan tiga bidang pekerjaan yang menurut Anda akan sangat membutuhkan kemampuan statistika di masa depan. Mengapa?

2. **Data dalam Kehidupan Sehari-hari:** Identifikasi satu contoh penggunaan data dan statistik yang Anda temui dalam kehidupan sehari-hari di Indonesia (bisa dari aplikasi, berita, atau kebijakan pemerintah). Jelaskan data apa yang dikumpulkan dan analisis apa yang mungkin dilakukan.

3. **Etika Data:** Bayangkan Anda bekerja di sebuah perusahaan e-commerce dan diminta menganalisis data pelanggan. Bagaimana Anda menerapkan prinsip amanah dan keadilan dalam pekerjaan tersebut?

4. **Tools vs. Pemahaman:** Menurut Anda, apakah cukup hanya bisa menggunakan tools (Python, Excel, AI) tanpa memahami teori statistiknya? Berikan argumentasi.

5. **Pengalaman Pertama Colab:** Bagaimana pengalaman pertama Anda menggunakan Google Colab? Apa yang paling menarik? Apa yang masih membingungkan?

---

## Tugas Mandiri Minggu 1

1. **Setup:** Pastikan Anda bisa mengakses Google Colab dan menjalankan semua kode di modul ini tanpa error.
2. **Eksplorasi:** Buat sebuah DataFrame baru di Colab yang berisi data tentang topik yang Anda minati (minimal 10 baris dan 4 kolom dengan tipe data yang berbeda). Jalankan `.head()`, `.info()`, `.describe()`, dan `.dtypes`.
3. **Identifikasi:** Untuk setiap kolom di DataFrame Anda, tentukan skala pengukurannya (nominal, ordinal, interval, atau rasio) dan jelaskan alasannya.

---

## Referensi

### Buku Teks

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability & Statistics for Engineers & Scientists* (9th ed.). Pearson.
2. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
3. Bruce, P., Bruce, A., & Gedeck, P. (2020). *Practical Statistics for Data Scientists* (2nd ed.). O'Reilly Media.

### Sumber Online

4. [pandas documentation](https://pandas.pydata.org/docs/) -- Dokumentasi resmi pandas.
5. [Google Colab Welcome Notebook](https://colab.research.google.com/notebooks/intro.ipynb) -- Tutorial pengantar Colab.
6. [BPS - Badan Pusat Statistik](https://www.bps.go.id/) -- Sumber data statistik Indonesia.

### Referensi Etika

7. Undang-Undang No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP).
8. Floridi, L., & Taddeo, M. (2016). What is data ethics? *Philosophical Transactions of the Royal Society A*, 374(2083).

---

> **Preview Minggu Depan:** Kita akan membahas **Statistika Deskriptif dan Eksplorasi Data dengan Python** -- menghitung mean, median, modus, variance, standard deviation, serta membuat ringkasan data menggunakan pandas dan numpy.
