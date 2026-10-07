# BAB 1: LANSKAP KECERDASAN ARTIFISIAL

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK082-1` | Menjelaskan hubungan AI, ML, dan DL serta ketiga paradigma pembelajaran | C2 |
| `DAIML-Sub-CPMK082-1` | Membedakan masalah yang sesuai dan tidak sesuai diselesaikan dengan ML | C4 |
| `DAIML-Sub-CPMK082-1` | Menjelaskan batas kemampuan sistem AI saat ini beserta sebabnya | C2 |

---

## 1.1 Apa yang Dimaksud Kecerdasan Artifisial

### 1.1.1 Definisi yang Dipakai Buku Ini

Russell dan Norvig menyusun definisi AI dalam empat kuadran: berpikir/bertindak × seperti manusia/rasional. Buku ini memakai kuadran **agen rasional** — sistem yang menerima persepsi dari lingkungan dan memilih tindakan yang memaksimalkan ukuran kinerja tertentu.

Pilihan ini bukan sekadar akademis. Definisi "bertindak seperti manusia" sulit dinilai; definisi "memaksimalkan ukuran kinerja tertentu" langsung menunjuk pada **metrik** — dan metrik adalah inti dari salah satu dari dua Sub-CPMK mata kuliah ini.

### 1.1.2 AI, ML, dan DL

```
┌───────────────────────────────────────────────────────────┐
│  ARTIFICIAL INTELLIGENCE                                  │
│  Sistem yang menunjukkan perilaku cerdas                  │
│                                                           │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  MACHINE LEARNING                                   │  │
│  │  Meningkat kinerjanya dari pengalaman (data),       │  │
│  │  tanpa aturan diprogram secara eksplisit            │  │
│  │                                                     │  │
│  │  ┌───────────────────────────────────────────────┐  │  │
│  │  │  DEEP LEARNING                                │  │  │
│  │  │  ML dengan jaringan berlapis banyak yang      │  │  │
│  │  │  mempelajari representasi bertingkat          │  │  │
│  │  └───────────────────────────────────────────────┘  │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                           │
│  Di luar ML: sistem pakar, pencarian, perencanaan,        │
│  penalaran simbolik, logika                               │
└───────────────────────────────────────────────────────────┘
```

Tiga kekeliruan yang sering terjadi:

| Kekeliruan | Yang sebenarnya |
|------------|-----------------|
| "AI = ML" | Sistem pencarian rute, penjadwal, dan sistem pakar adalah AI tanpa pembelajaran |
| "ML = DL" | Pada data tabular, *gradient boosting* masih sering mengungguli jaringan dalam |
| "DL adalah ML versi lebih baik" | DL tepat untuk data tak terstruktur, sering berlebihan untuk yang lain |

### 1.1.3 Definisi Pembelajaran Mesin

Definisi Tom Mitchell (1997) tetap yang paling operasional:

> Sebuah program dikatakan **belajar** dari pengalaman **E** terhadap kelompok tugas **T** dengan ukuran kinerja **P**, apabila kinerjanya pada T — yang diukur dengan P — meningkat seiring bertambahnya E.

Kekuatan definisi ini terletak pada ketiganya harus **dinyatakan secara terukur**:

| Kasus | T (Tugas) | E (Pengalaman) | P (Kinerja) |
|-------|-----------|----------------|-------------|
| Deteksi transaksi janggal | Menandai wajar/janggal | Riwayat transaksi berlabel | *Recall* pada kelas janggal |
| Perkiraan keterlambatan KRL | Memperkirakan menit keterlambatan | Data perjalanan historis | MAE dalam menit |
| Segmentasi pelanggan | Mengelompokkan pelanggan | Riwayat pembelian tanpa label | Skor *silhouette* |
| Kelayakan kredit UMKM | Menilai layak/tidak | Riwayat pengajuan berlabel | *Recall* dengan batas *precision* |

Perhatikan baris terakhir: memilih P yang berbeda menghasilkan **sistem yang berbeda**. Memaksimalkan akurasi menghasilkan model yang berbeda dari memaksimalkan *recall* pada pemohon yang layak — dan perbedaan itu menyentuh kehidupan orang yang pengajuannya dinilai.

---

## 1.2 Tiga Gelombang Kecerdasan Artifisial

| Gelombang | Periode | Pendekatan | Kekuatan | Kelemahan yang mengakhirinya |
|-----------|---------|------------|----------|------------------------------|
| **I — Simbolik** | 1956–1980-an | Aturan logika yang ditulis pakar | Dapat dijelaskan; terjamin benar dalam ranahnya | Tidak tahan ketidakpastian; aturan tidak terkelola |
| **II — Statistik** | 1990-an–2010-an | Belajar pola dari data | Tahan derau; berskala | Butuh banyak data berlabel; sulit dijelaskan |
| **III — Fondasi/Generatif** | 2017–sekarang | Model besar praterlatih | Serbaguna; sedikit contoh cukup | Mahal; dapat mengarang; sulit diaudit |

### 1.2.1 Dua Musim Dingin dan Pelajarannya

Dua periode surutnya pendanaan dan minat terhadap AI — 1974–1980 dan 1987–1993 — terjadi karena hal yang sama: **janji melampaui kemampuan**.

Pelajarannya tetap berlaku hari ini, dan ia bersifat profesional, bukan historis: menyatakan batas kemampuan sistem dengan jujur adalah bagian dari pekerjaan, bukan kelemahan. Seorang insinyur yang mengatakan "model ini bekerja pada kondisi A, B, dan C, tetapi tidak dapat diandalkan pada D" memberi informasi yang jauh lebih berguna daripada yang mengatakan "model ini akurat 94%".

### 1.2.2 Catatan tentang Warisan Keilmuan

Kata **algoritma** berasal dari nama **Al-Khwarizmi** (w. ±850 M), yang karyanya tentang aljabar dan prosedur perhitungan sistematis menjadi salah satu akar tradisi komputasi. Setiap metode dalam buku ini — dari perhitungan *entropy* sampai *backpropagation* — adalah algoritma dalam pengertian itu: rangkaian langkah yang dapat diperiksa, diulang, dan dipertanggungjawabkan.

Penamaan itu mengingatkan sesuatu yang relevan bagi bab-bab berikutnya: **prosedur yang dapat diperiksa** adalah ciri pekerjaan ilmiah, dan ia adalah alasan mengapa reproduksibilitas menjadi kriteria penilaian mata kuliah ini.

---

## 1.3 Tiga Paradigma Pembelajaran

### 1.3.1 Pembelajaran Terbimbing

Data memiliki **label** — jawaban yang benar sudah diketahui untuk data latih.

```
   FITUR (X)                          TARGET (y)
   ┌──────────────────────────┐      ┌──────────┐
   │ omzet │ lama │ rasio_utang│     │ gagal?   │
   ├───────┼──────┼────────────┤     ├──────────┤
   │  45jt │ 3,2  │    0,18    │ ──► │  Tidak   │
   │  12jt │ 0,8  │    0,62    │ ──► │  Ya      │
   │  88jt │ 7,5  │    0,09    │ ──► │  Tidak   │
   └───────┴──────┴────────────┘     └──────────┘
                    │
                    ▼
          Model mempelajari f: X → y
                    │
                    ▼
   Pengajuan baru tanpa label ───► prediksi
```

| Jenis | Target | Contoh Indonesia |
|-------|--------|------------------|
| **Regresi** | Bilangan kontinu | Harga properti Jabodetabek; IPM kabupaten |
| **Klasifikasi** | Kategori | Kelayakan kredit; kategori keluhan layanan publik |

### 1.3.2 Pembelajaran Tanpa Supervisi

Tidak ada label; model mencari **struktur**.

| Jenis | Yang dicari | Contoh Indonesia |
|-------|-------------|------------------|
| *Clustering* | Kelompok alami | Segmentasi provinsi berdasarkan indikator BPS |
| Reduksi dimensi | Representasi ringkas | Meringkas 40 indikator menjadi 3 sumbu utama |
| Deteksi anomali | Pengamatan tak lazim | Pola konsumsi listrik yang janggal |

Kesulitan pokoknya: **tidak ada jawaban benar untuk dibandingkan**. Evaluasinya jauh lebih sulit, dan selalu menuntut lapis kedua berupa penilaian manusia — dibahas tuntas pada Bab 10.

### 1.3.3 Pembelajaran Penguatan

Agen belajar melalui interaksi dan imbalan. Contoh: pengaturan lampu lalu lintas adaptif.

**Tidak dibahas mendalam** dalam buku ini — hanya dikenalkan agar peta paradigma lengkap.

---

## 1.4 Kapan Pembelajaran Mesin Bukan Jawabannya

Bagian ini adalah yang terpenting dalam bab ini, dan yang paling sering dilewati.

### 1.4.1 Lima Keadaan

| Keadaan | Mengapa | Yang sebaiknya dipakai |
|---------|---------|------------------------|
| **Aturannya sudah jelas dan stabil** | ML akan mempelajari kembali sesuatu yang sudah diketahui, dengan hasil lebih buruk | Aturan `if-else` |
| **Data tidak ada atau terlalu sedikit** | Model tidak dapat belajar dari yang tidak ada | Kumpulkan data dahulu; atau pakai aturan |
| **Kesalahan berakibat berat tanpa pengawasan manusia** | Model selalu memiliki galat | Sistem pendukung keputusan, bukan pengambil keputusan |
| **Yang dibutuhkan sebab-akibat, bukan prediksi** | ML mempelajari korelasi | Rancangan eksperimen; inferensi kausal |
| **Keterjelasan penuh dituntut regulasi** | Banyak model sulit dijelaskan | Model sederhana yang dapat ditafsirkan; atau aturan |

**Contoh yang paling jelas:** menghitung pajak progresif tidak memerlukan ML. Aturannya tertulis dalam undang-undang, pasti, dan tidak berubah dari data. Membangun model untuk itu menghasilkan sistem yang lebih lambat, lebih mahal, lebih sulit diaudit, dan **lebih sering salah**.

### 1.4.2 Uji Kelayakan Enam Pertanyaan

1. Apakah ada **pola** yang harus dipelajari, atau aturannya sudah diketahui?
2. Apakah **data** tersedia dalam jumlah dan mutu yang memadai?
3. Apakah **kesalahan dapat ditoleransi**, dan berapa besar biayanya?
4. Apakah prediksi akan **benar-benar dipakai** untuk mengambil keputusan?
5. Apakah ada **pembanding sederhana** yang harus dikalahkan?
6. Apakah **konsekuensi kesalahan** sudah dipahami, termasuk siapa yang dirugikan?

Satu jawaban "tidak" pada nomor 1–4 sudah cukup untuk mempertimbangkan ulang. Melewati nomor 5 membuat hasil apa pun tidak bermakna. Melewati nomor 6 berisiko merugikan orang tanpa disadari.

---

## 1.5 Batas Kemampuan Sistem AI Saat Ini

| Batas | Penjelasan | Akibat praktis |
|-------|------------|----------------|
| **Tidak memahami sebab-akibat** | Mempelajari korelasi dalam data | Prediksi runtuh ketika distribusi berubah |
| **Bergantung mutlak pada data latih** | Hanya sebaik data yang melatihnya | *Bias* dalam data menjadi *bias* dalam keputusan |
| **Rapuh di luar distribusi latih** | Kinerja anjlok pada data berbeda sifat | Model bagus di lab gagal di lapangan |
| **Tidak memiliki akal sehat** | Tidak ada pengetahuan dunia di luar data | Keluaran dapat mustahil secara nyata |
| **Sulit dijelaskan** | Model kompleks tidak transparan | Menyulitkan audit dan pemenuhan regulasi |
| **Model generatif dapat mengarang** | Menghasilkan keluaran meyakinkan tetapi salah | Setiap keluaran harus diverifikasi |

> **Yang perlu dipegang sepanjang buku ini:** tidak satu pun batas di atas akan hilang hanya dengan model yang lebih besar. Sebagiannya melekat pada sifat pembelajaran dari data. Tugas seorang insinyur adalah mengetahui batas itu dan merancang sistem yang memperhitungkannya.

---

## 1.6 Perangkat Kerja

```python
# Sel pembuka baku — dipakai pada setiap notebook
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

print("Python      :", sys.version.split()[0])
print("NumPy       :", np.__version__)
print("pandas      :", pd.__version__)
print("scikit-learn:", sklearn.__version__)

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (9, 5)

RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)
```

Pencatatan versi bukan kerapian tambahan. Kriteria kurikulum untuk `Sub-CPMK082-1` menyebut **reproduksibilitas eksperimen** sebagai kriteria penilaian. Hasil yang tidak dapat diulang bukan hasil.

---

## AI Corner — Tahap *Understand*

### Memahami Apa yang Sebenarnya Dilakukan Sistem AI

Mata kuliah ini berstatus **mode Core**: AI adalah objek yang dipelajari, bukan sekadar alat bantu. AI Corner pada bab ini karena itu dimulai dari pemahaman, bukan dari cara pakai.

**Pertanyaan yang layak diajukan setiap kali menghadapi sistem yang disebut "AI":**

| Pertanyaan | Mengapa penting |
|------------|-----------------|
| Apakah ia belajar dari data, atau menjalankan aturan? | Menentukan apakah ia ML atau AI simbolik |
| Data apa yang melatihnya, dan siapa yang tercakup di dalamnya? | Menentukan batas keberlakuannya |
| Apa ukuran kinerja yang dioptimalkannya? | Ukuran yang berbeda menghasilkan perilaku yang berbeda |
| Apa yang terjadi ketika ia salah? | Menentukan apakah pengawasan manusia diperlukan |

### AI sebagai Alat Kerja pada Bab Ini

Pada tahap ini, pemakaian AI yang wajar adalah untuk **memahami konsep dengan cara lain**:

```
Saya membaca bahwa perceptron tunggal tidak dapat mempelajari XOR.
Tolong jelaskan mengapa, dengan analogi geometris. Jangan berikan
kode — saya ingin memahami gagasannya lebih dahulu.
```

Prompt ini menunjukkan dua hal: yang diminta adalah penjelasan (bukan pekerjaan), dan batasnya dinyatakan.

**Yang sudah tidak boleh sejak bab pertama:** meminta AI menentukan apakah sebuah masalah memerlukan ML. Itu adalah penerapan uji kelayakan §1.4.2 — dan uji itu menuntut pengetahuan tentang konteks masalah yang tidak dimiliki model bahasa.

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan hubungan himpunan antara AI, ML, dan DL. Berikan satu contoh sistem yang termasuk AI tetapi bukan ML, dan satu contoh ML yang bukan DL.

2. Untuk tiga kasus berikut, tentukan T, E, dan P menurut definisi Mitchell:
   (a) Sistem penyaring komentar bernada kebencian di media sosial.
   (b) Sistem perkiraan waktu tempuh ojek daring.
   (c) Sistem pengelompokan keluhan warga ke dalam tema layanan.

3. Tentukan paradigma pembelajaran yang sesuai untuk masing-masing:
   (a) Memprediksi jumlah penumpang TransJakarta besok dari data historis.
   (b) Mengelompokkan provinsi berdasarkan indikator sosial-ekonomi.
   (c) Menandai transaksi mencurigakan dari contoh berlabel.
   (d) Mengatur durasi lampu lalu lintas berdasarkan akibat tindakan.

4. Sebutkan tiga dari enam batas kemampuan AI pada §1.5, dan jelaskan akibat praktis masing-masing dalam satu kalimat.

### Tingkat Menengah

5. Sebuah perusahaan ingin membangun "sistem AI" untuk menghitung denda keterlambatan pengembalian buku perpustakaan. Aturannya: Rp 1.000 per hari, maksimal Rp 50.000.
   (a) Terapkan uji kelayakan enam pertanyaan §1.4.2.
   (b) Apakah ML diperlukan? Jelaskan.
   (c) Apa kerugian membangun model ML untuk ini?
   (d) Apa yang sebaiknya disarankan kepada perusahaan itu?

6. Sebuah rumah sakit ingin memprediksi pasien yang berisiko tinggi, dengan data 1.200 pasien dari satu rumah sakit di Jakarta.
   (a) Apakah data ini memadai? Jelaskan pertimbangannya.
   (b) Batas kemampuan AI mana (§1.5) yang paling relevan di sini?
   (c) Apa yang terjadi bila model ini dipakai di rumah sakit daerah di Papua?
   (d) Pertanyaan mana dari uji kelayakan yang paling kritis untuk kasus ini?

7. Bandingkan tiga gelombang AI.
   (a) Mengapa gelombang I gagal menangani ketidakpastian?
   (b) Apa yang memungkinkan gelombang II berhasil di mana gelombang I gagal?
   (c) Kelemahan apa dari gelombang II yang diatasi gelombang III?
   (d) Kelemahan apa dari gelombang III yang **belum** teratasi?

8. Sebuah tim membangun model untuk menilai kelayakan pembebasan bersyarat narapidana.
   (a) Secara teknis, apakah ini dapat dimodelkan? Jelaskan.
   (b) Pertanyaan nomor berapa pada uji kelayakan yang paling menentukan di sini?
   (c) Sebutkan dua kelompok yang dapat dirugikan dan bagaimana.
   (d) Apa saran Anda kepada tim itu?

### Tingkat Mahir

9. Lakukan audit atas satu sistem yang diiklankan memakai AI.
   (a) Pilih satu produk atau layanan nyata (aplikasi, layanan publik, produk komersial).
   (b) Tentukan: apakah ia belajar dari data, atau menjalankan aturan?
   (c) Perkirakan T, E, dan P-nya.
   (d) Identifikasi batas kemampuan mana (§1.5) yang paling mungkin menjadi kelemahannya.
   (e) Rancang satu pengujian sederhana yang dapat mengungkap kelemahan itu.

10. Bangun kerangka keputusan "ML atau tidak".
    (a) Kumpulkan sepuluh masalah nyata dari lingkungan Anda (kampus, keluarga, tempat kerja).
    (b) Terapkan uji kelayakan enam pertanyaan pada masing-masing.
    (c) Kelompokkan menjadi: jelas perlu ML, jelas tidak perlu, dan perlu dipertimbangkan.
    (d) Untuk kelompok ketiga, tuliskan informasi apa yang masih dibutuhkan untuk memutuskan.
    (e) Susun menjadi satu diagram alir keputusan satu halaman.

11. Tulislah esai satu halaman berjudul *"Mengapa Batas Kemampuan AI Tidak Akan Hilang dengan Model yang Lebih Besar"*. Sertakan: minimal tiga dari enam batas pada §1.5, alasan mengapa masing-masing bersifat melekat, dan satu contoh nyata kegagalan sistem AI yang berakar pada salah satunya.

---

## Rangkuman

1. **AI ⊃ ML ⊃ DL.** Tidak semua AI belajar dari data; tidak semua ML memakai jaringan dalam.
2. Definisi kerja yang dipakai: **agen rasional** — memaksimalkan ukuran kinerja yang terukur.
3. Definisi Mitchell (**T, E, P**) mengubah gagasan "belajar" menjadi sesuatu yang dapat diuji. **Memilih P yang berbeda menghasilkan sistem yang berbeda.**
4. **Tiga paradigma:** terbimbing (ada label), tanpa supervisi (tanpa label), penguatan (imbalan dari interaksi).
5. Tiga gelombang AI: simbolik → statistik → model fondasi. Dua musim dingin terjadi karena **janji melampaui kemampuan**.
6. **ML bukan selalu jawabannya.** Lima keadaan menuntut pendekatan lain.
7. **Uji kelayakan enam pertanyaan** wajib dilewati sebelum memutuskan memakai ML.
8. **Enam batas kemampuan AI** tidak akan hilang hanya dengan model yang lebih besar.
9. **Reproduksibilitas adalah kriteria penilaian**, bukan kerapian tambahan.

---

## Referensi

1. Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.), Bab 1. Pearson.
2. Mitchell, T. (1997). *Machine Learning*, Bab 1. McGraw-Hill.
3. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 1. O'Reilly.
4. Domingos, P. (2012). A Few Useful Things to Know About Machine Learning. *CACM*, 55(10), 78–87.
5. Grinsztajn, L., Oyallon, E., & Varoquaux, G. (2022). Why Do Tree-Based Models Still Outperform Deep Learning on Tabular Data? *NeurIPS*.
6. ACM/IEEE-CS (2023). *Computer Science Curricula 2023*, Knowledge Area: Artificial Intelligence.
7. UNESCO (2024). *AI Competency Framework for Students*.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
