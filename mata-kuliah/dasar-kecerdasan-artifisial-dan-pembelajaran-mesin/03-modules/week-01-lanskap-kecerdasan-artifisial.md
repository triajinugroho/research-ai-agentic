# Minggu 1: Lanskap Kecerdasan Artifisial

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 1 dari 16 |
| Topik | Definisi, sejarah, paradigma, dan batas kemampuan AI |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-01 |
| Bloom | C2 (Memahami) → C4 (Menganalisis) |
| Durasi | 150 menit |
| Metode | Kuliah interaktif · Diskusi kasus · Praktik terbimbing |
| Penilaian | Observasi (Lab 1) |

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Menjelaskan** (C2) perbedaan Artificial Intelligence, Machine Learning, dan Deep Learning beserta hubungan himpunannya.
2. **Membedakan** (C4) masalah yang sesuai diselesaikan dengan pembelajaran mesin dari masalah yang cukup diselesaikan dengan aturan biasa.
3. **Mengklasifikasikan** (C3) suatu kasus ke dalam paradigma pembelajaran: terbimbing, tanpa supervisi, atau penguatan.
4. **Menjelaskan** (C2) batas kemampuan sistem AI saat ini dan mengapa batas itu ada.
5. **Menyiapkan** (P2) lingkungan kerja Python untuk pembelajaran mesin.

---

## Materi Pembelajaran

### 1.1 Apa yang Dimaksud Kecerdasan Artifisial

#### 1.1.1 Empat Definisi yang Berbeda

Russell dan Norvig menyusun definisi AI dalam empat kuadran, dan perbedaannya bukan sekadar akademis:

```
                    BERPIKIR                    BERTINDAK
              ┌─────────────────────┬─────────────────────┐
              │  Sistem yang        │  Sistem yang        │
   SEPERTI    │  berpikir seperti   │  bertindak seperti  │
   MANUSIA    │  manusia            │  manusia            │
              │  (ilmu kognitif)    │  (Uji Turing)       │
              ├─────────────────────┼─────────────────────┤
              │  Sistem yang        │  Sistem yang        │
   RASIONAL   │  berpikir rasional  │  bertindak rasional │
              │  (logika)           │  (agen rasional)    │
              └─────────────────────┴─────────────────────┘
```

Kuadran kanan bawah — **agen rasional** — adalah definisi kerja yang dipakai mata kuliah ini: sistem yang menerima persepsi dari lingkungan dan memilih tindakan yang memaksimalkan ukuran kinerja tertentu.

Definisi ini penting karena ia **dapat diukur**. "Bertindak seperti manusia" sulit dinilai; "memaksimalkan ukuran kinerja tertentu" langsung menunjuk pada metrik — dan metrik adalah inti Sub-CPMK kedua mata kuliah ini.

#### 1.1.2 Hubungan AI, ML, dan DL

```
┌───────────────────────────────────────────────────────────┐
│  ARTIFICIAL INTELLIGENCE                                  │
│  Sistem yang menunjukkan perilaku cerdas                  │
│                                                           │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  MACHINE LEARNING                                   │  │
│  │  Sistem yang meningkat kinerjanya dari pengalaman   │  │
│  │  (data), tanpa diprogram aturannya secara eksplisit │  │
│  │                                                     │  │
│  │  ┌───────────────────────────────────────────────┐  │  │
│  │  │  DEEP LEARNING                                │  │  │
│  │  │  ML dengan jaringan saraf berlapis banyak     │  │  │
│  │  │  yang mempelajari representasi bertingkat     │  │  │
│  │  └───────────────────────────────────────────────┘  │  │
│  │                                                     │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                           │
│  Di luar ML: sistem pakar, pencarian, perencanaan,        │
│  penalaran simbolik, logika                               │
└───────────────────────────────────────────────────────────┘
```

Tiga hal yang sering salah dipahami:

1. **Tidak semua AI adalah ML.** Sistem pencarian jalur pada peta digital, penjadwal, dan sistem pakar berbasis aturan adalah AI tanpa pembelajaran.
2. **Tidak semua ML adalah DL.** Pada data tabular — yang mendominasi masalah nyata di organisasi Indonesia — *gradient boosting* masih sering mengungguli jaringan dalam.
3. **DL bukan "ML versi lebih baik".** Ia adalah pilihan yang tepat untuk data tak terstruktur (citra, suara, teks) dan sering berlebihan untuk yang lain.

#### 1.1.3 Definisi Pembelajaran Mesin

Definisi Tom Mitchell (1997) tetap yang paling operasional:

> Sebuah program dikatakan **belajar** dari pengalaman **E** terhadap kelompok tugas **T** dengan ukuran kinerja **P**, apabila kinerjanya pada T — yang diukur dengan P — meningkat seiring bertambahnya E.

Contoh penerapan pada kasus nyata:

| Kasus | T (Tugas) | E (Pengalaman) | P (Kinerja) |
|-------|-----------|----------------|-------------|
| Deteksi transaksi janggal bank | Menandai transaksi sebagai wajar/janggal | Riwayat transaksi berlabel | *Recall* pada kelas janggal |
| Prediksi keterlambatan KRL | Memperkirakan keterlambatan dalam menit | Data perjalanan historis | MAE dalam menit |
| Segmentasi pelanggan e-commerce | Mengelompokkan pelanggan | Riwayat pembelian tanpa label | Skor *silhouette* |

> **Latihan cepat:** rumuskan T, E, dan P untuk "sistem penilaian kelayakan kredit usaha mikro". Perhatikan bahwa P yang berbeda menghasilkan sistem yang berbeda — memaksimalkan akurasi menghasilkan sistem yang berbeda dari memaksimalkan *recall* pada pemohon yang layak.

---

### 1.2 Tiga Gelombang Kecerdasan Artifisial

| Gelombang | Periode | Pendekatan | Kekuatan | Kelemahan yang mengakhirinya |
|-----------|---------|------------|----------|------------------------------|
| **I — Simbolik** | 1956–1980-an | Aturan logika yang ditulis pakar | Dapat dijelaskan; terjamin benar dalam ranahnya | Tidak tahan ketidakpastian; aturan tidak terkelola pada masalah besar |
| **II — Statistik** | 1990-an–2010-an | Belajar pola dari data | Tahan derau; berskala | Membutuhkan banyak data berlabel; sulit dijelaskan |
| **III — Fondasi/Generatif** | 2017–sekarang | Model besar praterlatih | Serbaguna; sedikit contoh cukup | Mahal; kadang mengarang; sulit diaudit |

**Dua musim dingin AI** (1974–1980 dan 1987–1993) terjadi ketika janji melampaui kemampuan. Pelajaran yang tetap relevan: menyatakan batas kemampuan sistem dengan jujur adalah bagian dari pekerjaan profesional, bukan kelemahan.

> **Catatan sejarah keilmuan:** metode-metode yang dipakai sepanjang mata kuliah ini berakar pada tradisi algoritmik yang dinamai dari **Al-Khwarizmi** (w. ±850 M), yang karyanya di bidang aljabar dan prosedur perhitungan sistematis menjadi dasar gagasan "algoritma". Penamaan itu bukan kebetulan historis belaka — ia mengingatkan bahwa perhitungan yang sistematis dan dapat diperiksa adalah warisan intelektual yang panjang.

---

### 1.3 Tiga Paradigma Pembelajaran

#### 1.3.1 Pembelajaran Terbimbing (*Supervised Learning*)

Data memiliki **label** — jawaban yang benar sudah diketahui untuk data latih.

```
   FITUR (X)                          TARGET (y)
   ┌──────────────────────────┐      ┌──────────┐
   │ luas │ kamar │ jarak_tol │      │  harga   │
   ├──────┼───────┼───────────┤      ├──────────┤
   │  90  │   3   │    2,4    │ ───► │  850 jt  │
   │ 120  │   4   │    1,1    │ ───► │ 1.400 jt │
   │  60  │   2   │    5,8    │ ───► │  520 jt  │
   └──────┴───────┴───────────┘      └──────────┘
                    │
                    ▼
          Model mempelajari f: X → y
                    │
                    ▼
   Data baru tanpa label ───► prediksi harga
```

Dua jenisnya:

| Jenis | Target | Contoh Indonesia |
|-------|--------|------------------|
| **Regresi** | Bilangan kontinu | Harga rumah Jabodetabek; lama tunggu di puskesmas |
| **Klasifikasi** | Kategori | Kelayakan kredit; deteksi berita palsu; diagnosis awal |

#### 1.3.2 Pembelajaran Tanpa Supervisi (*Unsupervised Learning*)

Tidak ada label. Model mencari **struktur** dalam data.

| Jenis | Yang dicari | Contoh Indonesia |
|-------|-------------|------------------|
| *Clustering* | Kelompok alami | Segmentasi provinsi berdasarkan indikator sosial-ekonomi |
| Reduksi dimensi | Representasi ringkas | Meringkas 40 indikator BPS menjadi 3 sumbu utama |
| Deteksi anomali | Pengamatan tak lazim | Pola konsumsi listrik yang janggal |

Kesulitan pokoknya: **tidak ada jawaban benar untuk dibandingkan**. Karena itu evaluasinya jauh lebih sulit — dibahas tuntas pada Minggu 11.

#### 1.3.3 Pembelajaran Penguatan (*Reinforcement Learning*)

Agen belajar melalui interaksi dengan lingkungan dan menerima **imbalan**.

```
        ┌──────────────┐   tindakan    ┌──────────────┐
        │     AGEN     │──────────────►│  LINGKUNGAN  │
        │              │               │              │
        │              │◄──────────────│              │
        └──────────────┘  keadaan +    └──────────────┘
                          imbalan
```

Contoh: pengaturan lampu lalu lintas adaptif; penjadwalan sumber daya. **Tidak dibahas mendalam** dalam mata kuliah ini — hanya dikenalkan agar peta paradigma lengkap.

#### 1.3.4 Latihan Klasifikasi Paradigma

Tentukan paradigma yang sesuai:

| Kasus | Paradigma | Alasan |
|-------|-----------|--------|
| Memprediksi jumlah penumpang TransJakarta besok dari data historis | Terbimbing (regresi) | Target numerik, data historis berlabel |
| Mengelompokkan keluhan warga menjadi tema-tema | Tanpa supervisi | Tidak ada label tema |
| Menandai e-mail sebagai spam dari contoh berlabel | Terbimbing (klasifikasi) | Label spam/bukan tersedia |
| Mengatur durasi lampu lalu lintas berdasarkan hasil | Penguatan | Belajar dari akibat tindakan |
| Menemukan transaksi yang menyimpang tanpa contoh penipuan | Tanpa supervisi (anomali) | Tidak ada label penipuan |

---

### 1.4 Kapan ML Bukan Jawabannya

Ini bagian terpenting dari pertemuan pertama, dan yang paling sering dilewati.

#### 1.4.1 Lima Keadaan ML Sebaiknya Tidak Dipakai

| Keadaan | Mengapa | Yang sebaiknya dipakai |
|---------|---------|------------------------|
| **Aturannya sudah jelas dan stabil** | ML akan mempelajari kembali sesuatu yang sudah diketahui, dengan hasil lebih buruk | Aturan `if-else` biasa |
| **Data tidak ada atau terlalu sedikit** | Model tidak dapat belajar dari yang tidak ada | Kumpulkan data dahulu, atau pakai aturan |
| **Kesalahan berakibat sangat berat tanpa pengawasan manusia** | Model selalu memiliki galat | Sistem pendukung keputusan, bukan pengambil keputusan |
| **Hubungan sebab-akibat yang dibutuhkan, bukan prediksi** | ML mempelajari korelasi | Rancangan eksperimen; inferensi kausal |
| **Keterjelasan penuh dituntut regulasi** | Banyak model sulit dijelaskan | Model sederhana yang dapat ditafsirkan, atau aturan |

**Contoh konkret:** menghitung pajak progresif **tidak memerlukan ML**. Aturannya tertulis dalam undang-undang, pasti, dan tidak berubah dari data. Membangun model ML untuk itu menghasilkan sistem yang lebih lambat, lebih mahal, lebih sulit diaudit, dan lebih sering salah.

#### 1.4.2 Uji Kelayakan Enam Pertanyaan

Sebelum memutuskan memakai ML, jawab:

1. Apakah ada **pola** yang harus dipelajari, atau aturannya sudah diketahui?
2. Apakah **data** tersedia dalam jumlah dan mutu yang memadai?
3. Apakah **kesalahan dapat ditoleransi**, dan berapa besar biayanya?
4. Apakah hasil prediksi akan **benar-benar dipakai** untuk mengambil keputusan?
5. Apakah ada **pembanding sederhana** (aturan, rata-rata, kelas terbanyak) yang harus dikalahkan?
6. Apakah **konsekuensi kesalahan** sudah dipahami, termasuk siapa yang dirugikan?

Jika ada satu jawaban "tidak" pada nomor 1–4, pertimbangkan ulang. Jika nomor 5 dilewati, hasil apa pun tidak bermakna. Jika nomor 6 dilewati, sistem berisiko merugikan orang tanpa disadari.

---

### 1.5 Batas Kemampuan Sistem AI Saat Ini

| Batas | Penjelasan | Akibat praktis |
|-------|------------|----------------|
| **Tidak memahami sebab-akibat** | Model mempelajari korelasi dalam data | Prediksi runtuh ketika distribusi berubah |
| **Bergantung mutlak pada data latih** | Model hanya sebaik data yang melatihnya | *Bias* dalam data menjadi *bias* dalam keputusan |
| **Rapuh di luar distribusi latih** | Kinerja anjlok pada data yang berbeda sifat | Model yang bagus di lab gagal di lapangan |
| **Tidak memiliki akal sehat** | Tidak ada pengetahuan dunia di luar data | Keluaran dapat mustahil secara nyata |
| **Sulit dijelaskan** | Model kompleks tidak transparan | Menyulitkan audit dan pemenuhan regulasi |
| **Model generatif dapat mengarang** | Menghasilkan keluaran yang tampak meyakinkan tetapi salah | Setiap keluaran harus diverifikasi |

> **Yang perlu dipegang sepanjang semester:** setiap batas di atas bukan kekurangan yang akan hilang dengan model yang lebih besar. Sebagiannya melekat pada sifat pembelajaran dari data itu sendiri. Tugas seorang insinyur adalah mengetahui batas itu dan merancang sistem yang memperhitungkannya.

---

### 1.6 Perangkat Kerja Semester Ini

```python
# Periksa versi pustaka — dijalankan pada sel pertama setiap notebook
import sys
import numpy as np
import pandas as pd
import matplotlib
import sklearn

print("Python      :", sys.version.split()[0])
print("NumPy       :", np.__version__)
print("pandas      :", pd.__version__)
print("matplotlib  :", matplotlib.__version__)
print("scikit-learn:", sklearn.__version__)

# Menetapkan seed agar hasil dapat direproduksi
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)
```

| Pustaka | Peran sepanjang semester |
|---------|--------------------------|
| `numpy` | Operasi larik dan aljabar linear |
| `pandas` | Pemuatan dan manipulasi data tabular |
| `matplotlib`, `seaborn` | Visualisasi |
| **`scikit-learn`** | **Pustaka ML utama** — dipakai hampir setiap minggu |
| `tensorflow`/`keras` | Hanya pada Minggu 13 |

> **Pencatatan versi bukan formalitas.** Kriteria kurikulum untuk `Sub-CPMK082-1` menyebut **reproduksibilitas eksperimen**. Hasil yang tidak dapat diulang bukan hasil.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 1 buku ajar](../06-buku-ajar/bab-01-lanskap-kecerdasan-artifisial.md).
- Menyiapkan akun Google Colab dan memastikan dapat membuat notebook.
- Mencatat satu contoh sistem AI yang ditemui sehari-hari, dan menduga paradigma pembelajarannya.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 15' | Perkenalan; kontrak kuliah; penjelasan bobot penilaian dan kebijakan AI |
| Konsep | 45' | AI/ML/DL; tiga gelombang; tiga paradigma |
| Diskusi | 30' | **Kegiatan inti:** sepuluh kasus nyata — mana yang ML, mana yang cukup aturan biasa. Dikerjakan berpasangan, dibahas bersama |
| Demonstrasi | 30' | Penyiapan Colab; memuat dataset pertama; mengenali fitur dan target |
| Praktik | 20' | Memulai Lab 1 |
| Penutup | 10' | Rangkuman; penugasan |

**Kegiatan inti — sepuluh kasus:**

1. Menghitung denda keterlambatan pengembalian buku perpustakaan
2. Menandai komentar bernada kebencian di media sosial
3. Menentukan urutan tampilan produk di aplikasi belanja
4. Menghitung gaji karyawan berdasarkan golongan dan masa kerja
5. Memperkirakan waktu tempuh ojek daring
6. Memeriksa kelengkapan berkas pendaftaran mahasiswa baru
7. Mengenali tanda-tanda awal penyakit dari citra rontgen
8. Menentukan pemenang lelang berdasarkan penawaran tertinggi
9. Mengelompokkan keluhan warga ke dalam tema layanan
10. Memutuskan apakah seorang tahanan layak mendapat pembebasan bersyarat

> Nomor 10 sengaja disertakan dan dibahas paling akhir. Secara teknis ia dapat dimodelkan; pertanyaannya adalah **apakah seharusnya**. Diskusi ini menjadi pembuka bagi materi Minggu 14.

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 1](../04-labs/lab-01-setup-ekosistem-ml.md).
- Mengerjakan Latihan Soal tingkat Dasar Bab 1.

---

## Penugasan

**T-01 — Penyiapan Lingkungan dan Eksplorasi Dataset Pertama**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook Colab |
| Isi | (a) Pemeriksaan versi pustaka; (b) Memuat tiga dataset berbeda; (c) Untuk tiap dataset: tentukan jenis *task*, target, fitur, dan **apakah ML memang diperlukan** beserta alasannya |
| Tenggat | Awal pertemuan Minggu 2 |
| Bobot | 1,9% (Observasi) |

---

## Rangkuman

1. **AI ⊃ ML ⊃ DL.** Tidak semua AI belajar dari data; tidak semua ML memakai jaringan dalam.
2. Definisi kerja AI yang dipakai: **agen rasional** — memaksimalkan ukuran kinerja yang terukur.
3. Definisi Mitchell (**T, E, P**) mengubah gagasan "belajar" menjadi sesuatu yang dapat diuji.
4. Tiga paradigma: **terbimbing** (ada label), **tanpa supervisi** (tanpa label), **penguatan** (imbalan dari interaksi).
5. Tiga gelombang AI: simbolik → statistik → model fondasi. Dua musim dingin terjadi karena janji melampaui kemampuan.
6. **ML bukan selalu jawabannya.** Lima keadaan menuntut pendekatan lain; uji kelayakan enam pertanyaan wajib dilewati lebih dahulu.
7. Enam batas kemampuan AI saat ini tidak akan hilang hanya dengan model yang lebih besar.
8. **Reproduksibilitas** adalah kriteria penilaian, bukan kerapian tambahan.

---

## Referensi

1. Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.), Bab 1. Pearson.
2. Mitchell, T. (1997). *Machine Learning*, Bab 1. McGraw-Hill.
3. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 1. O'Reilly.
4. Domingos, P. (2012). A Few Useful Things to Know About Machine Learning. *Communications of the ACM*, 55(10), 78–87.
5. ACM/IEEE-CS (2023). *Computer Science Curricula 2023*, Knowledge Area: Artificial Intelligence.
6. Tim Kurikulum Informatika UAI (2026). *AI Curriculum Infusion Matrix*.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
