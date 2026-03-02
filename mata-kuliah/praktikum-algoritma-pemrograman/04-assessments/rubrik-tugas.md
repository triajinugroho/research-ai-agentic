# Rubrik Penilaian Tugas — Algoritma dan Pemrograman

> **Mata Kuliah:** Algoritma dan Pemrograman (3 SKS)
> **Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.
> **Program Studi:** Informatika, Universitas Al Azhar Indonesia
> **Semester:** Genap 2025/2026
> **Bahasa Pemrograman:** Python
> **Tanggal:** Jakarta, Februari 2026

---

Dokumen ini memuat rubrik penilaian komprehensif untuk **seluruh jenis tugas dan asesmen** dalam mata kuliah Algoritma dan Pemrograman. Rubrik disusun agar penilaian bersifat transparan, konsisten, dan adil bagi seluruh mahasiswa. Setiap mahasiswa diharapkan membaca dan memahami rubrik ini sejak awal perkuliahan.

**Ringkasan Bobot Komponen Penilaian:**

| No | Komponen | Bobot |
|---|---|---|
| 1 | Tugas Pemrograman (T1–T6) | 15% |
| 2 | Kuis (K1–K3) | 10% |
| 3 | Ujian Tengah Semester (UTS) | 20% |
| 4 | Proyek Akhir | 25% |
| 5 | Ujian Akhir Semester (UAS) | 25% |
| 6 | Partisipasi | 5% |
| | **Total** | **100%** |

---

## 1. Rubrik Tugas Mingguan — Lab/Praktikum (Bobot: 15%)

Tugas mingguan (T1–T6) diberikan sebagai latihan pemrograman individu yang dikerjakan di lab atau sebagai pekerjaan rumah (*take-home*). Setiap tugas dinilai berdasarkan 4 dimensi dengan skala 4 level: **Sangat Baik (4)**, **Baik (3)**, **Cukup (2)**, dan **Kurang (1)**.

### 1.1 Rubrik Penilaian

| Dimensi | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|---|---|---|---|---|
| **Ketepatan Algoritma** (30%) | Program berjalan benar untuk semua kasus uji, termasuk kasus tepi (*edge case*). Logika algoritma tepat dan lengkap. Validasi input menyeluruh. | Program berjalan benar untuk sebagian besar kasus uji. Terdapat kesalahan minor pada kasus tepi. Validasi input ada tetapi belum menyeluruh. | Program berjalan untuk kasus dasar, tetapi gagal pada beberapa kasus uji penting. Logika memerlukan perbaikan signifikan. | Program tidak berjalan atau menghasilkan output yang salah untuk sebagian besar kasus uji. Logika dasar bermasalah. |
| **Kualitas Kode** (25%) | Kode sepenuhnya mematuhi PEP 8. Penamaan variabel deskriptif menggunakan *snake_case*. Struktur kode rapi, mudah dibaca, dan tidak ada duplikasi. Penggunaan fitur Python idiomatik. | Kode sebagian besar mematuhi PEP 8. Penamaan variabel cukup deskriptif. Struktur kode cukup rapi dengan beberapa area yang bisa diperbaiki. | Kode memiliki beberapa pelanggaran PEP 8 (indentasi tidak konsisten, baris terlalu panjang). Penamaan variabel kurang deskriptif (misalnya `x`, `temp`). | Kode tidak mematuhi PEP 8. Penamaan variabel tidak bermakna. Struktur kode sulit dibaca dan dipahami. Format tidak rapi. |
| **Efisiensi Solusi** (25%) | Solusi menggunakan pendekatan efisien dan elegan. Tidak ada perulangan atau operasi yang tidak perlu. Struktur data dipilih dengan tepat. Kompleksitas waktu optimal untuk masalah yang diberikan. | Solusi cukup efisien. Pendekatan secara umum sudah tepat meskipun ada ruang untuk optimasi minor. Struktur data cukup sesuai. | Solusi berfungsi tetapi kurang efisien. Terdapat perulangan berlebihan, kode redundan, atau penggunaan struktur data yang kurang tepat. | Solusi sangat tidak efisien atau menggunakan pendekatan yang sepenuhnya tidak tepat. *Brute force* tanpa alasan yang jelas. |
| **Dokumentasi & Komentar** (20%) | Setiap fungsi memiliki docstring lengkap (deskripsi, args, returns). Komentar menjelaskan logika kompleks. File memiliki header yang jelas (nama, NIM, deskripsi). AI Usage Log terisi detail. | Sebagian besar fungsi memiliki docstring. Komentar ada pada bagian penting. Header file ada. AI Usage Log cukup lengkap. | Komentar minim dan tidak konsisten. Beberapa fungsi tanpa docstring. Header file kurang lengkap. AI Usage Log ada tetapi kurang detail. | Tidak ada komentar atau docstring sama sekali. Tidak ada header file. Tidak ada AI Usage Log. |

### 1.2 Perhitungan Skor Tugas Mingguan

Skor setiap tugas dihitung dengan rumus:

```
Skor Tugas = (Ketepatan x 0.30) + (Kualitas x 0.25) + (Efisiensi x 0.25) + (Dokumentasi x 0.20)
Skor Tugas (skala 100) = (Skor Tugas / 4) x 100
```

**Nilai Akhir Komponen Tugas Mingguan:**

```
Nilai Tugas = Rata-rata(T1, T2, T3, T4, T5, T6)
Kontribusi ke Nilai Akhir = Nilai Tugas x 15%
```

### 1.3 Contoh Penilaian Tugas Mingguan

**Skenario A: Mahasiswa dengan performa tinggi mengerjakan T3 — Perulangan dan Pola**

| Dimensi | Bobot | Level | Skor | Skor Terbobot |
|---|---|---|---|---|
| Ketepatan Algoritma | 30% | Sangat Baik (4) | 4 | 1.20 |
| Kualitas Kode | 25% | Baik (3) | 3 | 0.75 |
| Efisiensi Solusi | 25% | Sangat Baik (4) | 4 | 1.00 |
| Dokumentasi & Komentar | 20% | Cukup (2) | 2 | 0.40 |
| **Total** | | | | **3.35** |

```
Skor Tugas (skala 100) = (3.35 / 4) x 100 = 83.75
```

Keterangan: Mahasiswa ini memiliki kemampuan teknis yang baik namun perlu meningkatkan dokumentasi kode.

**Skenario B: Mahasiswa dengan performa rendah mengerjakan T3 — Perulangan dan Pola**

| Dimensi | Bobot | Level | Skor | Skor Terbobot |
|---|---|---|---|---|
| Ketepatan Algoritma | 30% | Cukup (2) | 2 | 0.60 |
| Kualitas Kode | 25% | Kurang (1) | 1 | 0.25 |
| Efisiensi Solusi | 25% | Cukup (2) | 2 | 0.50 |
| Dokumentasi & Komentar | 20% | Kurang (1) | 1 | 0.20 |
| **Total** | | | | **1.55** |

```
Skor Tugas (skala 100) = (1.55 / 4) x 100 = 38.75
```

Keterangan: Mahasiswa ini perlu bimbingan intensif pada kualitas kode dan dokumentasi.

### 1.4 Ketentuan Tambahan Tugas Mingguan

| Aspek | Ketentuan |
|---|---|
| **Format File** | File `.py` atau link Google Colab (pastikan sharing aktif) |
| **Penamaan File** | `T[nomor]_NIM_NamaDepan.py` (contoh: `T1_2025001_Andi.py`) |
| **Deadline** | Jumat pukul 23:59 WIB di minggu yang ditentukan |
| **Keterlambatan** | -10 poin per hari (maks. 3 hari); setelah 3 hari = nilai 0 |
| **Plagiarisme** | Nilai 0 untuk kedua pihak (penyalin dan yang disalin) |
| **AI Usage** | Sesuai kebijakan per tugas; AI Usage Log wajib dilampirkan |

---

## 2. Rubrik Kuis (Bobot: 10%)

Kuis dilaksanakan 3 kali selama semester (K1, K2, K3) secara *in-class* dengan durasi 30–45 menit. Kuis bersifat *closed-book* dan **tanpa bantuan AI**.

### 2.1 Format dan Distribusi Soal Kuis

| Tipe Soal | Jumlah | Poin per Soal | Total Poin | Deskripsi |
|---|---|---|---|---|
| Pilihan Ganda | 5 soal | 4 poin | 20 poin | Konsep dasar, terminologi, prediksi output sederhana |
| *Code Tracing* | 3 soal | 10 poin | 30 poin | Menentukan output program, mengisi tabel trace |
| Jawaban Singkat | 2 soal | 10 poin | 20 poin | Menjelaskan konsep, membandingkan pendekatan |
| Tulis Kode | 3 soal | 10 poin | 30 poin | Menulis potongan kode Python untuk masalah tertentu |
| **Total** | **13 soal** | | **100 poin** | |

### 2.2 Panduan Penilaian per Tipe Soal

#### a. Pilihan Ganda (4 poin/soal)

| Kriteria | Poin |
|---|---|
| Jawaban benar | 4 |
| Jawaban salah | 0 |
| Tidak dijawab | 0 |

Tidak ada pengurangan poin untuk jawaban salah (*no negative marking*).

#### b. Code Tracing (10 poin/soal)

| Kriteria | Poin | Penjelasan |
|---|---|---|
| Trace lengkap dan output akhir benar | 10 | Tabel trace terisi lengkap, output sesuai |
| Proses trace benar, output akhir salah karena kesalahan hitung minor | 7–8 | Alur logika dipahami, kesalahan kecil |
| Proses trace sebagian benar, menunjukkan pemahaman alur | 4–6 | Memahami konsep tetapi ada kekeliruan dalam eksekusi |
| Proses trace salah tetapi ada upaya dan pemahaman dasar terlihat | 1–3 | Upaya terlihat meskipun keliru |
| Tidak dijawab atau sepenuhnya salah tanpa upaya | 0 | Kosong atau tidak relevan |

#### c. Jawaban Singkat (10 poin/soal)

| Kriteria | Poin | Penjelasan |
|---|---|---|
| Jawaban lengkap, akurat, menggunakan terminologi tepat | 9–10 | Menunjukkan pemahaman mendalam |
| Jawaban benar secara substansi, kurang lengkap atau kurang presisi | 6–8 | Pemahaman baik, perlu detail tambahan |
| Jawaban menunjukkan pemahaman dasar tetapi ada kekeliruan | 3–5 | Pemahaman parsial |
| Jawaban tidak relevan atau menunjukkan miskonsepsi fundamental | 1–2 | Pemahaman sangat terbatas |
| Tidak dijawab | 0 | Kosong |

#### d. Tulis Kode (10 poin/soal)

| Kriteria | Poin | Penjelasan |
|---|---|---|
| Kode benar, berjalan tanpa error, logika tepat, penamaan baik | 9–10 | Solusi lengkap dan berkualitas |
| Kode umum benar, kesalahan sintaks minor yang tidak mengubah logika | 7–8 | Pemahaman logika baik, detail kecil terlewat |
| Logika sebagian benar, ada error signifikan tetapi pendekatan terlihat | 4–6 | Upaya dan pemahaman dasar terlihat |
| Upaya menulis kode terlihat, tetapi logika salah atau tidak lengkap | 1–3 | Upaya minimal |
| Tidak dijawab atau kode tidak relevan | 0 | Kosong atau tidak relevan |

### 2.3 Perhitungan Nilai Kuis

```
Nilai Kuis = Rata-rata(K1, K2, K3)
Kontribusi ke Nilai Akhir = Nilai Kuis x 10%
```

### 2.4 Contoh Penilaian Kuis

**Skenario: Mahasiswa C mengerjakan K2 — Materi Perulangan dan List**

| Tipe Soal | Detail Penilaian | Poin Diperoleh | Poin Maksimal |
|---|---|---|---|
| Pilihan Ganda (5 soal) | 3 benar, 2 salah: 3 x 4 = 12 | 12 | 20 |
| Code Tracing (3 soal) | Soal 1: sempurna (10), Soal 2: minor error (7), Soal 3: parsial (5) | 22 | 30 |
| Jawaban Singkat (2 soal) | Soal 1: cukup lengkap (8), Soal 2: kurang presisi (6) | 14 | 20 |
| Tulis Kode (3 soal) | Soal 1: sempurna (9), Soal 2: minor syntax (7), Soal 3: logika parsial (4) | 20 | 30 |
| **Total** | | **68** | **100** |

Nilai K2 Mahasiswa C: **68/100**.

### 2.5 Jadwal Kuis

| Kuis | Minggu ke- | Cakupan Materi |
|---|---|---|
| K1 | 4 | Variabel, tipe data, I/O, percabangan |
| K2 | 9 | Perulangan, fungsi, list |
| K3 | 14 | Dictionary, searching, sorting, rekursi |

---

## 3. Rubrik Tugas Mandiri

Tugas mandiri adalah tugas *take-home* yang diberikan untuk topik tertentu dengan tenggat waktu 1–2 minggu. Tugas mandiri termasuk dalam komponen Tugas Pemrograman (T1–T6) dan memiliki tingkat kesulitan lebih tinggi dibandingkan tugas lab reguler, menuntut kemampuan analisis serta pendekatan *problem solving* yang lebih mendalam.

### 3.1 Rubrik Penilaian

| Dimensi | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|---|---|---|---|---|
| **Pendekatan Problem Solving** (30%) | Masalah dianalisis secara sistematis. Pseudocode atau flowchart disertakan. Pendekatan menunjukkan *computational thinking* yang kuat: dekomposisi, abstraksi, pengenalan pola, dan pemikiran algoritmik. | Masalah dianalisis dengan baik. Ada deskripsi pendekatan sebelum kode, meskipun belum dalam bentuk pseudocode formal. | Langsung menulis kode tanpa analisis mendalam, tetapi pendekatan secara umum sudah menuju solusi yang benar. | Tidak ada bukti analisis masalah. Pendekatan solusi tidak terstruktur atau tidak relevan dengan permasalahan. |
| **Kualitas Kode** (25%) | Kode modular dengan fungsi-fungsi yang memiliki tanggung jawab tunggal. PEP 8 diterapkan sepenuhnya. Penggunaan struktur data tepat. Error handling dengan `try-except` diterapkan. Kode DRY. | Kode cukup modular. Sebagian besar sesuai PEP 8. Struktur data sesuai. Error handling ada pada bagian penting. | Kode berfungsi tetapi kurang modular (satu blok besar). Beberapa pelanggaran PEP 8. Error handling minimal. | Kode tidak berjalan atau memiliki error fundamental. Tidak modular. Tidak sesuai PEP 8. Tidak ada error handling. |
| **Testing & Validasi** (25%) | Mahasiswa menyertakan minimal 5 kasus uji yang mencakup kasus normal, batas (*boundary*), dan *edge case*. Semua kasus uji didokumentasikan dengan input, output yang diharapkan, dan hasil aktual. | Mahasiswa menyertakan 3–4 kasus uji yang mencakup kasus normal dan beberapa kasus batas. Dokumentasi kasus uji cukup. | Mahasiswa menyertakan 1–2 kasus uji dasar saja. Tidak ada pengujian *edge case*. Dokumentasi pengujian terbatas. | Tidak ada kasus uji yang disertakan. Tidak ada bukti bahwa program telah diuji. |
| **Orisinalitas** (20%) | Solusi menunjukkan pemikiran orisinal. Jika menggunakan AI, mahasiswa menunjukkan pemahaman mendalam melalui modifikasi signifikan dan penjelasan yang meyakinkan. AI Usage Log lengkap dan reflektif. | Solusi menunjukkan upaya sendiri dengan bantuan referensi yang wajar. AI Usage Log cukup lengkap. Ada upaya modifikasi dari sumber referensi. | Solusi sangat mirip dengan contoh dari sumber lain dengan modifikasi minimal. AI Usage Log ada tetapi kurang lengkap. | Solusi terbukti disalin tanpa pemahaman. Tidak ada AI Usage Log padahal ada indikasi penggunaan AI. |

### 3.2 Contoh Penilaian Tugas Mandiri

**Skenario: Mahasiswa D — Tugas Mandiri Implementasi Algoritma Sorting untuk Data Nilai Mahasiswa**

| Dimensi | Bobot | Level | Skor | Skor Terbobot |
|---|---|---|---|---|
| Pendekatan Problem Solving | 30% | Baik (3) | 3 | 0.90 |
| Kualitas Kode | 25% | Sangat Baik (4) | 4 | 1.00 |
| Testing & Validasi | 25% | Baik (3) | 3 | 0.75 |
| Orisinalitas | 20% | Sangat Baik (4) | 4 | 0.80 |
| **Total** | | | | **3.45** |

```
Skor Tugas (skala 100) = (3.45 / 4) x 100 = 86.25
```

Keterangan: Mahasiswa D menunjukkan kualitas kode dan orisinalitas yang tinggi; perbaikan pada pendekatan analitis (misalnya menyertakan pseudocode) akan meningkatkan skor lebih lanjut.

---

## 4. Rubrik Proyek Akhir (Bobot: 25%)

Proyek akhir merupakan asesmen autentik utama yang mengintegrasikan seluruh capaian pembelajaran. Mahasiswa membangun aplikasi Python yang lengkap dan fungsional untuk menyelesaikan masalah dunia nyata. Proyek dapat dikerjakan secara **individu** atau **berpasangan (maksimal 2 orang)**. Penilaian terdiri atas 6 dimensi.

### 4.1 Rubrik Penilaian Detail

#### Dimensi 1: Definisi Masalah & Analisis (15%)

| Level | Deskripsi | Rentang Skor |
|---|---|---|
| **Sangat Baik** | Masalah didefinisikan dengan jelas dan spesifik. Analisis kebutuhan (*requirement analysis*) lengkap mencakup input, proses, dan output. Konteks dunia nyata di Indonesia relevan dan menarik. Diagram alir atau pseudocode disertakan dan akurat. | 86–100 |
| **Baik** | Masalah cukup jelas. Analisis kebutuhan ada tetapi kurang lengkap pada beberapa aspek. Konteks dunia nyata relevan. | 71–85 |
| **Cukup** | Masalah terlalu umum atau kurang fokus. Analisis kebutuhan minimal. Konteks kurang jelas atau kurang relevan. | 56–70 |
| **Kurang** | Masalah tidak jelas atau tidak relevan. Tidak ada analisis kebutuhan. Tidak ada konteks yang bermakna. | 0–55 |

#### Dimensi 2: Desain Algoritma & Ketepatan (25%)

| Level | Deskripsi | Rentang Skor |
|---|---|---|
| **Sangat Baik** | Algoritma dirancang dengan tepat dan efisien. Program berjalan tanpa error untuk semua skenario penggunaan. Implementasi searching dan/atau sorting sesuai dan benar. Logika program konsisten dan lengkap. Kasus tepi ditangani. | 86–100 |
| **Baik** | Algoritma secara umum tepat. Program berjalan untuk sebagian besar skenario. Terdapat error minor pada kasus tepi. Implementasi searching/sorting ada dan secara umum benar. | 71–85 |
| **Cukup** | Algoritma berfungsi untuk kasus dasar. Program memiliki beberapa bug signifikan. Implementasi searching/sorting ada tetapi tidak sepenuhnya benar atau kurang terintegrasi. | 56–70 |
| **Kurang** | Algoritma tidak tepat. Program tidak berjalan atau menghasilkan output salah secara konsisten. Tidak ada implementasi searching/sorting yang berarti. | 0–55 |

#### Dimensi 3: Kualitas Kode & Best Practices (20%)

| Level | Deskripsi | Rentang Skor |
|---|---|---|
| **Sangat Baik** | Kode sepenuhnya sesuai PEP 8. Minimal 5 fungsi dengan penamaan deskriptif dan tanggung jawab tunggal. Minimal 3 struktur data berbeda digunakan dengan tepat. Error handling dengan `try-except` diterapkan secara menyeluruh. Kode DRY (*Don't Repeat Yourself*). | 86–100 |
| **Baik** | Kode sebagian besar sesuai PEP 8. Fungsi-fungsi ada (4–5 fungsi) dan cukup terorganisir. Struktur data bervariasi. Error handling ada pada bagian input utama. | 71–85 |
| **Cukup** | Beberapa pelanggaran PEP 8. Fungsi ada tetapi kurang terorganisir atau terlalu sedikit (2–3 fungsi). Struktur data kurang bervariasi. Error handling minimal. | 56–70 |
| **Kurang** | Kode tidak sesuai PEP 8. Tidak modular (tanpa fungsi yang bermakna atau hanya 1 fungsi). Hanya menggunakan 1 tipe struktur data. Tidak ada error handling. | 0–55 |

#### Dimensi 4: Testing & Validasi (15%)

| Level | Deskripsi | Rentang Skor |
|---|---|---|
| **Sangat Baik** | Laporan pengujian lengkap dengan minimal 10 kasus uji yang terdokumentasi. Mencakup kasus normal, batas, dan *edge case*. Validasi input pengguna komprehensif. Bukti screenshot atau log pengujian disertakan. | 86–100 |
| **Baik** | Laporan pengujian ada dengan 5–9 kasus uji. Mencakup kasus normal dan beberapa kasus batas. Validasi input ada pada fitur utama. | 71–85 |
| **Cukup** | Pengujian ada tetapi kurang sistematis (3–4 kasus uji). Hanya kasus normal yang diuji. Validasi input terbatas. | 56–70 |
| **Kurang** | Tidak ada laporan pengujian atau hanya 1–2 kasus uji trivial. Tidak ada validasi input yang berarti. | 0–55 |

#### Dimensi 5: Dokumentasi & Presentasi (15%)

| Level | Deskripsi | Rentang Skor |
|---|---|---|
| **Sangat Baik** | README lengkap (deskripsi, cara install, cara pakai, contoh penggunaan). Docstring pada setiap fungsi. Presentasi jelas, terstruktur, dan mampu menjawab pertanyaan dosen serta mahasiswa lain. Demo program berjalan lancar. | 86–100 |
| **Baik** | README ada dan cukup lengkap. Docstring pada sebagian besar fungsi. Presentasi cukup jelas dan terstruktur. Demo program berjalan. | 71–85 |
| **Cukup** | Dokumentasi minim (hanya deskripsi singkat). Docstring tidak konsisten. Presentasi kurang terstruktur. Demo memerlukan bantuan atau mengalami kendala minor. | 56–70 |
| **Kurang** | Tidak ada dokumentasi yang berarti. Tidak ada docstring. Presentasi sangat kurang atau tidak dilakukan. Demo gagal atau tidak dilakukan. | 0–55 |

#### Dimensi 6: AI Usage Log & Refleksi (10%)

| Level | Deskripsi | Rentang Skor |
|---|---|---|
| **Sangat Baik** | AI Usage Log lengkap dan detail. Setiap interaksi dengan AI dicatat (prompt, output, keputusan). Refleksi kritis menunjukkan kemampuan mengevaluasi output AI. Bukti belajar dari AI (bukan sekadar menyalin). Atribusi jelas di kode sumber. | 86–100 |
| **Baik** | AI Usage Log ada dan cukup detail. Refleksi menunjukkan pemahaman terhadap output AI. Atribusi ada di kode sumber. | 71–85 |
| **Cukup** | AI Usage Log ada tetapi kurang lengkap. Refleksi dangkal (misalnya hanya "AI membantu membuat kode"). Atribusi kurang jelas atau tidak konsisten. | 56–70 |
| **Kurang** | Tidak ada AI Usage Log padahal ada indikasi penggunaan AI, ATAU AI Usage Log sangat tidak lengkap tanpa refleksi apa pun. | 0–55 |

### 4.2 Perhitungan Nilai Proyek Akhir

```
Nilai Proyek = (Definisi Masalah x 0.15) + (Desain Algoritma x 0.25) +
               (Kualitas Kode x 0.20) + (Testing x 0.15) +
               (Dokumentasi x 0.15) + (AI Usage Log x 0.10)

Kontribusi ke Nilai Akhir = Nilai Proyek x 25%
```

### 4.3 Contoh Penilaian Proyek Akhir

**Skenario A: Mahasiswa E — Proyek "Sistem Manajemen Perpustakaan Mini"**

Mahasiswa E membangun sistem perpustakaan dengan fitur CRUD buku, pencarian dengan binary search, pengurutan berdasarkan judul/tahun dengan selection sort, dan penyimpanan data ke file JSON. Program memiliki 7 fungsi, menggunakan list, dictionary, dan tuple. Dokumentasi lengkap dan presentasi berjalan lancar.

| Dimensi | Bobot | Skor (0–100) | Skor Terbobot |
|---|---|---|---|
| Definisi Masalah & Analisis | 15% | 90 | 13.50 |
| Desain Algoritma & Ketepatan | 25% | 82 | 20.50 |
| Kualitas Kode & Best Practices | 20% | 88 | 17.60 |
| Testing & Validasi | 15% | 75 | 11.25 |
| Dokumentasi & Presentasi | 15% | 85 | 12.75 |
| AI Usage Log & Refleksi | 10% | 78 | 7.80 |
| **Total** | **100%** | | **83.40** |

Nilai Proyek Mahasiswa E: **83.40** (Huruf: **B+**)

**Skenario B: Mahasiswa F — Proyek "Aplikasi Kasir Warung Sederhana"**

Mahasiswa F membangun aplikasi kasir dengan fitur tambah barang dan hitung total. Program hanya memiliki 3 fungsi, menggunakan list dan dictionary. Testing terbatas. AI Usage Log tidak disertakan meskipun ada indikasi penggunaan AI pada beberapa fungsi.

| Dimensi | Bobot | Skor (0–100) | Skor Terbobot |
|---|---|---|---|
| Definisi Masalah & Analisis | 15% | 70 | 10.50 |
| Desain Algoritma & Ketepatan | 25% | 65 | 16.25 |
| Kualitas Kode & Best Practices | 20% | 60 | 12.00 |
| Testing & Validasi | 15% | 55 | 8.25 |
| Dokumentasi & Presentasi | 15% | 68 | 10.20 |
| AI Usage Log & Refleksi | 10% | 40 | 4.00 |
| **Total** | **100%** | | **61.20** |

Nilai Proyek Mahasiswa F: **61.20** (Huruf: **C+**)

> **Catatan:** Mahasiswa F mendapat skor rendah pada AI Usage Log (40) karena tidak menyertakan log meskipun ada indikasi kuat penggunaan AI pada beberapa fungsi. Jika log disertakan dengan refleksi yang baik, dimensi ini bisa bernilai 75–85.

---

## 5. Rubrik Partisipasi (Bobot: 5%)

Partisipasi dinilai secara akumulatif sepanjang semester berdasarkan 3 sub-komponen berikut.

### 5.1 Komponen Penilaian Partisipasi

| Sub-Komponen | Bobot (dari 5%) | Deskripsi |
|---|---|---|
| Kehadiran | 40% | Persentase kehadiran di perkuliahan dan praktikum |
| Diskusi Aktif | 35% | Kontribusi dalam diskusi kelas: bertanya, menjawab, berpendapat |
| Kontribusi Peer Review | 25% | Kualitas umpan balik yang diberikan kepada rekan sejawat |

### 5.2 Rubrik Detail Partisipasi

#### a. Kehadiran (40% dari Partisipasi)

| Persentase Kehadiran | Skor | Keterangan |
|---|---|---|
| 90–100% | 100 | Komitmen kehadiran sangat baik |
| 80–89% | 80 | Kehadiran baik dengan beberapa absensi |
| 70–79% | 60 | Kehadiran cukup, perlu peningkatan |
| 60–69% | 40 | Kehadiran kurang, mendekati batas minimum |
| < 60% | 0 | **Tidak lulus mata kuliah** sesuai peraturan akademik UAI |

> **Catatan:** Ketidakhadiran dengan surat keterangan resmi (sakit dengan surat dokter, tugas institusi, atau izin resmi dari pimpinan fakultas) tidak mengurangi persentase kehadiran.

#### b. Diskusi Aktif (35% dari Partisipasi)

| Level | Deskripsi | Skor |
|---|---|---|
| **Sangat Baik** | Secara konsisten bertanya, menjawab, atau memberikan komentar bermakna di setiap sesi. Menunjukkan persiapan dan pemahaman materi. Membantu rekan yang kesulitan tanpa memberikan jawaban langsung (*scaffolding*). | 86–100 |
| **Baik** | Sering berpartisipasi dalam diskusi (>50% sesi). Pertanyaan atau jawaban menunjukkan pemahaman materi. Sesekali membantu rekan. | 71–85 |
| **Cukup** | Sesekali berpartisipasi (25–50% sesi). Partisipasi terbatas pada jawaban singkat atau pertanyaan dasar. | 56–70 |
| **Kurang** | Jarang berpartisipasi (<25% sesi). Pasif dalam sesi kelas. Tidak menunjukkan inisiatif untuk berkontribusi. | 0–55 |

#### c. Kontribusi Peer Review (25% dari Partisipasi)

| Level | Deskripsi | Skor |
|---|---|---|
| **Sangat Baik** | Memberikan umpan balik yang konstruktif, spesifik, dan membantu rekan memperbaiki kode. Menunjukkan kemampuan membaca dan menganalisis kode orang lain. Umpan balik disampaikan dengan sopan dan profesional. Mengidentifikasi bug spesifik dan menyarankan perbaikan. | 86–100 |
| **Baik** | Memberikan umpan balik yang cukup spesifik dan bermanfaat. Mampu mengidentifikasi beberapa area perbaikan. Nada komunikasi profesional. | 71–85 |
| **Cukup** | Umpan balik ada tetapi terlalu umum (misalnya "sudah bagus" atau "perlu diperbaiki" tanpa penjelasan spesifik). Kurang mendalam. | 56–70 |
| **Kurang** | Tidak memberikan umpan balik, atau umpan balik tidak bermakna dan tidak membantu rekan untuk berkembang. | 0–55 |

### 5.3 Perhitungan Nilai Partisipasi

```
Nilai Partisipasi = (Kehadiran x 0.40) + (Diskusi x 0.35) + (Peer Review x 0.25)
Kontribusi ke Nilai Akhir = Nilai Partisipasi x 5%
```

### 5.4 Contoh Penilaian Partisipasi

**Skenario: Mahasiswa G — Partisipasi Sepanjang Semester**

Mahasiswa G hadir di 13 dari 14 sesi (93%), aktif berdiskusi di 8 dari 14 sesi (57%), dan memberikan peer review dengan kualitas cukup.

| Sub-Komponen | Bobot | Skor | Skor Terbobot |
|---|---|---|---|
| Kehadiran (93% = level 90–100%) | 40% | 100 | 40.00 |
| Diskusi Aktif (57% sesi = level Baik) | 35% | 75 | 26.25 |
| Peer Review (kualitas Cukup) | 25% | 65 | 16.25 |
| **Total** | | | **82.50** |

```
Kontribusi ke Nilai Akhir = 82.50 x 5% = 4.13 poin
```

---

## 6. Pedoman Penilaian AI Usage Log

### 6.1 Latar Belakang

Mahasiswa diperbolehkan menggunakan alat bantu AI (*Artificial Intelligence*) seperti ChatGPT, GitHub Copilot, Claude, Gemini, atau alat sejenis sesuai kebijakan per tugas. Sebagai syarat transparansi dan integritas akademik, mahasiswa **wajib mendokumentasikan penggunaan AI** dalam bentuk AI Usage Log. Pedoman ini mengatur bagaimana AI Usage Log dinilai sebagai komponen asesmen.

### 6.2 Struktur AI Usage Log yang Diharapkan

Setiap entri dalam AI Usage Log harus memuat elemen-elemen berikut:

| No | Elemen | Deskripsi | Wajib? |
|---|---|---|---|
| 1 | Tanggal dan waktu | Kapan interaksi AI dilakukan | Ya |
| 2 | Nama alat AI | ChatGPT, Copilot, Claude, Gemini, dll. | Ya |
| 3 | Prompt yang diberikan | Pertanyaan atau instruksi yang dikirim ke AI | Ya |
| 4 | Ringkasan output AI | Inti dari jawaban atau kode yang dihasilkan AI | Ya |
| 5 | Keputusan mahasiswa | Apakah output diterima, dimodifikasi, atau ditolak — beserta alasan | Ya |
| 6 | Refleksi pembelajaran | Apa yang dipelajari dari interaksi tersebut | Ya |
| 7 | Kode yang dimodifikasi | Perubahan spesifik yang dilakukan terhadap output AI | Jika relevan |

**Contoh Format AI Usage Log:**

```python
"""
AI USAGE LOG - Tugas T5
Nama: Ahmad Fauzi
NIM: 20250042

Entri 1:
  Tanggal: 2026-03-15, 14:30 WIB
  AI Tool: ChatGPT (GPT-4o)
  Prompt: "Bagaimana cara menggunakan dictionary comprehension
           untuk memfilter data mahasiswa berdasarkan IPK?"
  Output AI: AI memberikan contoh kode dict comprehension
             dengan filter kondisi.
  Keputusan: DIMODIFIKASI - Saya mengubah variabel agar sesuai
             dengan struktur data program saya dan menambahkan
             validasi tipe data.
  Refleksi: Saya belajar bahwa dict comprehension lebih ringkas
            dibanding loop biasa untuk membuat dictionary baru
            dengan filter. Namun, saya memilih tetap menggunakan
            loop biasa di fungsi utama agar lebih mudah dibaca.

Entri 2:
  Tanggal: 2026-03-16, 09:00 WIB
  AI Tool: Claude
  Prompt: "Mengapa program saya menghasilkan KeyError saat
           mengakses data mahasiswa?"
  Output AI: AI menjelaskan bahwa KeyError terjadi ketika key
             tidak ada di dictionary, dan menyarankan menggunakan
             .get() dengan default value.
  Keputusan: DITERIMA - Saya mengubah semua akses dictionary
             menjadi .get() dengan default value yang sesuai.
  Refleksi: Saya memahami pentingnya defensive programming.
            Menggunakan .get() lebih aman dibanding akses
            langsung dengan bracket notation.
"""
```

### 6.3 Rubrik Penilaian AI Usage Log

| Dimensi | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|---|---|---|---|---|
| **Kelengkapan Log** (25%) | Semua interaksi AI tercatat lengkap dengan semua elemen wajib terisi. Log kronologis dan terorganisir. Tidak ada interaksi yang terlewat. | Sebagian besar interaksi tercatat. Beberapa elemen mungkin kurang lengkap. Urutan kronologis terjaga. | Log ada tetapi tidak lengkap. Beberapa interaksi tidak tercatat atau banyak elemen wajib yang hilang. | Log tidak ada atau sangat minimal sementara ada bukti kuat penggunaan AI di kode. |
| **Refleksi Kritis** (30%) | Refleksi menunjukkan kemampuan mengevaluasi kelebihan dan keterbatasan output AI. Mahasiswa mengidentifikasi error, inefisiensi, atau ketidaksesuaian pada output AI. Refleksi menunjukkan pemikiran kritis dan mendalam. | Refleksi menunjukkan pemahaman terhadap output AI. Ada upaya evaluasi kualitas output meskipun belum mendalam di semua entri. | Refleksi dangkal, hanya mendeskripsikan apa yang AI berikan tanpa evaluasi kritis. Misalnya: "AI memberikan kode yang benar, saya langsung pakai." | Tidak ada refleksi, atau refleksi tidak relevan dengan output AI yang diterima. |
| **Bukti Pembelajaran** (30%) | Mahasiswa menunjukkan bahwa ia memahami kode atau konsep yang diberikan AI. Ada bukti konkret: memodifikasi kode AI, menjelaskan logika dengan kata-kata sendiri, menerapkan konsep yang dipelajari ke bagian lain program, atau menolak output AI dengan alasan yang valid. | Mahasiswa menunjukkan pemahaman dasar terhadap output AI. Ada upaya untuk memahami dan bukan sekadar menyalin. Beberapa modifikasi dilakukan. | Bukti pembelajaran minim. Kode AI digunakan dengan sedikit modifikasi. Pemahaman terhadap output terbatas. | Tidak ada bukti pembelajaran. Kode AI disalin langsung tanpa pemahaman (*copy-paste* mentah tanpa modifikasi apa pun). |
| **Atribusi** (15%) | Atribusi jelas pada setiap bagian kode yang melibatkan bantuan AI. Komentar dalam kode menandai bagian yang dibantu AI (misalnya `# Dibantu AI: ...`). Konsisten dan transparan di seluruh program. | Atribusi ada pada sebagian besar bagian yang melibatkan AI. Cukup konsisten. | Atribusi minimal atau tidak konsisten — hanya pada beberapa bagian sementara bagian lain yang juga menggunakan AI tidak diatribusikan. | Tidak ada atribusi sama sekali padahal menggunakan AI. |

### 6.4 Perhitungan Skor AI Usage Log

```
Skor AI Log = (Kelengkapan x 0.25) + (Refleksi x 0.30) +
              (Bukti Pembelajaran x 0.30) + (Atribusi x 0.15)
Skor (skala 100) = (Skor AI Log / 4) x 100
```

### 6.5 Contoh Penilaian AI Usage Log

**Skenario A: Mahasiswa H — AI Usage Log untuk Proyek Akhir (Log Baik)**

Mahasiswa H menggunakan ChatGPT untuk membantu membuat fungsi sorting dan Claude untuk memahami konsep file I/O. Detail log:
- 8 entri interaksi AI selama 3 minggu pengerjaan proyek
- Prompt dicatat lengkap beserta ringkasan output
- Pada 3 entri, mahasiswa menuliskan bahwa ia memodifikasi kode AI karena menemukan bug atau inefisiensi
- Pada 2 entri, mahasiswa menjelaskan bahwa ia menolak output AI dan menulis sendiri karena lebih memahami konteks masalah
- Atribusi ditambahkan sebagai komentar di kode sumber pada semua bagian terkait

| Dimensi | Bobot | Level | Skor | Skor Terbobot |
|---|---|---|---|---|
| Kelengkapan Log | 25% | Sangat Baik (4) | 4 | 1.00 |
| Refleksi Kritis | 30% | Sangat Baik (4) | 4 | 1.20 |
| Bukti Pembelajaran | 30% | Baik (3) | 3 | 0.90 |
| Atribusi | 15% | Sangat Baik (4) | 4 | 0.60 |
| **Total** | | | | **3.70** |

```
Skor AI Usage Log (skala 100) = (3.70 / 4) x 100 = 92.50
```

**Skenario B: Mahasiswa K — AI Usage Log untuk Tugas Mandiri (Log Lemah)**

Mahasiswa K menggunakan AI tetapi log hanya berisi 2 entri singkat tanpa refleksi, dan beberapa bagian kode yang jelas dari AI tidak diatribusikan.

| Dimensi | Bobot | Level | Skor | Skor Terbobot |
|---|---|---|---|---|
| Kelengkapan Log | 25% | Cukup (2) | 2 | 0.50 |
| Refleksi Kritis | 30% | Kurang (1) | 1 | 0.30 |
| Bukti Pembelajaran | 30% | Cukup (2) | 2 | 0.60 |
| Atribusi | 15% | Kurang (1) | 1 | 0.15 |
| **Total** | | | | **1.55** |

```
Skor AI Usage Log (skala 100) = (1.55 / 4) x 100 = 38.75
```

### 6.6 Pelanggaran Terkait AI Usage Log

| Pelanggaran | Konsekuensi |
|---|---|
| Tidak menyertakan AI Usage Log padahal kebijakan tugas mewajibkan | Pengurangan 20 poin dari skor tugas terkait |
| AI Usage Log tidak jujur (menyatakan tidak menggunakan AI padahal menggunakan) | Skor tugas menjadi 0; ditangani sebagai pelanggaran integritas akademik |
| Menggunakan AI pada tugas/ujian dengan kebijakan "Tanpa AI" | Skor tugas/ujian menjadi 0; ditangani sebagai pelanggaran integritas akademik |
| Menyalin output AI tanpa modifikasi dan tanpa pemahaman | Pengurangan 30 poin dari skor tugas; wajib mengulang tugas |

### 6.7 Kebijakan AI per Jenis Asesmen

| Jenis Asesmen | Kebijakan AI | AI Usage Log |
|---|---|---|
| Tugas Mingguan (T1–T6) | Bervariasi per tugas (lihat instruksi masing-masing) | Wajib |
| Kuis (K1–K3) | **Tanpa AI** — sepenuhnya dikerjakan sendiri | Tidak diperlukan |
| UTS | **Tanpa AI** — *closed-book*, tanpa perangkat elektronik | Tidak diperlukan |
| Proyek Akhir | **AI diizinkan** dengan ketentuan transparansi | Wajib (detail) |
| UAS | **Tanpa AI** — *closed-book*, tanpa perangkat elektronik | Tidak diperlukan |

---

## 7. Tabel Konversi Nilai

### 7.1 Skala Konversi Nilai Huruf

Konversi nilai akhir numerik ke huruf mengikuti ketentuan Universitas Al Azhar Indonesia:

| Rentang Nilai | Huruf | Bobot | Predikat |
|---|---|---|---|
| 86–100 | A | 4.00 | Sangat Baik |
| 81–85 | A- | 3.75 | Sangat Baik |
| 76–80 | B+ | 3.50 | Baik |
| 71–75 | B | 3.00 | Baik |
| 66–70 | B- | 2.75 | Cukup Baik |
| 61–65 | C+ | 2.25 | Cukup |
| 56–60 | C | 2.00 | Cukup |
| 41–55 | D | 1.00 | Kurang |
| 0–40 | E | 0.00 | Gagal |

### 7.2 Ringkasan Bobot dan Formula Nilai Akhir

| No | Komponen | Bobot | Instrumen | Sifat |
|---|---|---|---|---|
| 1 | Tugas Pemrograman (T1–T6) | 15% | 6 tugas individu | Take-home |
| 2 | Kuis (K1–K3) | 10% | 3 kuis | In-class, closed-book |
| 3 | Ujian Tengah Semester (UTS) | 20% | 1 ujian | Closed-book |
| 4 | Proyek Akhir | 25% | 1 proyek | Individu/berpasangan |
| 5 | Ujian Akhir Semester (UAS) | 25% | 1 ujian | Closed-book |
| 6 | Partisipasi | 5% | Sepanjang semester | Akumulatif |
| | **Total** | **100%** | | |

**Formula Nilai Akhir:**

```
Nilai Akhir = (Tugas x 0.15) + (Kuis x 0.10) + (UTS x 0.20) +
              (Proyek x 0.25) + (UAS x 0.25) + (Partisipasi x 0.05)
```

### 7.3 Contoh Perhitungan Nilai Akhir Lengkap

**Skenario A: Mahasiswa I — Performa Baik**

| Komponen | Nilai (0–100) | Bobot | Kontribusi |
|---|---|---|---|
| Tugas (rata-rata T1–T6) | 83.75 | 15% | 12.56 |
| Kuis (rata-rata K1–K3) | 72.00 | 10% | 7.20 |
| UTS | 78.00 | 20% | 15.60 |
| Proyek Akhir | 83.40 | 25% | 20.85 |
| UAS | 80.00 | 25% | 20.00 |
| Partisipasi | 82.50 | 5% | 4.13 |
| **Nilai Akhir** | | **100%** | **80.34** |

Nilai Akhir Mahasiswa I: **80.34** --> Huruf: **B+** (Bobot: 3.50, Predikat: Baik)

**Skenario B: Mahasiswa J — Performa Kurang**

| Komponen | Nilai (0–100) | Bobot | Kontribusi |
|---|---|---|---|
| Tugas (rata-rata T1–T6) | 55.00 | 15% | 8.25 |
| Kuis (rata-rata K1–K3) | 48.00 | 10% | 4.80 |
| UTS | 50.00 | 20% | 10.00 |
| Proyek Akhir | 61.20 | 25% | 15.30 |
| UAS | 55.00 | 25% | 13.75 |
| Partisipasi | 60.00 | 5% | 3.00 |
| **Nilai Akhir** | | **100%** | **55.10** |

Nilai Akhir Mahasiswa J: **55.10** --> Huruf: **D** (Bobot: 1.00, Predikat: Kurang)

**Skenario C: Mahasiswa L — Performa Sangat Baik**

| Komponen | Nilai (0–100) | Bobot | Kontribusi |
|---|---|---|---|
| Tugas (rata-rata T1–T6) | 92.00 | 15% | 13.80 |
| Kuis (rata-rata K1–K3) | 88.00 | 10% | 8.80 |
| UTS | 85.00 | 20% | 17.00 |
| Proyek Akhir | 90.50 | 25% | 22.63 |
| UAS | 87.00 | 25% | 21.75 |
| Partisipasi | 95.00 | 5% | 4.75 |
| **Nilai Akhir** | | **100%** | **88.73** |

Nilai Akhir Mahasiswa L: **88.73** --> Huruf: **A** (Bobot: 4.00, Predikat: Sangat Baik)

> **Catatan:**
> - Mahasiswa dengan nilai D diperbolehkan mengulang mata kuliah pada semester berikutnya untuk perbaikan nilai.
> - Mahasiswa dengan nilai E dinyatakan **gagal** dan **wajib** mengulang mata kuliah.
> - Mahasiswa dengan kehadiran di bawah 60% **tidak lulus** mata kuliah terlepas dari nilai komponen lain.

---

## 8. Ketentuan Umum

### 8.1 Integritas Akademik

Seluruh tugas dan ujian tunduk pada Kode Etik Akademik Universitas Al Azhar Indonesia. Pelanggaran integritas akademik meliputi:

- Menyalin kode atau jawaban dari mahasiswa lain tanpa izin
- Menggunakan AI tanpa izin pada tugas atau ujian yang melarangnya
- Tidak mencantumkan AI Usage Log padahal menggunakan bantuan AI
- Menyerahkan karya orang lain sebagai karya sendiri
- Membantu mahasiswa lain untuk menyontek pada kuis atau ujian
- Membagikan output AI kepada mahasiswa lain untuk tugas yang sama

### 8.2 Mekanisme Keberatan Nilai

Mahasiswa berhak mengajukan keberatan atas nilai yang diterima dengan prosedur berikut:

1. Keberatan diajukan secara tertulis kepada dosen pengampu paling lambat **7 hari kalender** setelah nilai diumumkan.
2. Keberatan harus mencantumkan komponen penilaian yang dipermasalahkan beserta alasan yang jelas dan bukti pendukung.
3. Dosen akan meninjau ulang dan memberikan keputusan dalam **5 hari kerja**.
4. Keputusan dosen bersifat final kecuali mahasiswa mengajukan banding ke Ketua Program Studi sesuai prosedur akademik yang berlaku.

### 8.3 Remedial

Mahasiswa yang memperoleh nilai akhir di bawah 56 (huruf D atau E) pada komponen tertentu dapat mengikuti remedial sesuai ketentuan dalam *Assessment Framework* mata kuliah. Ketentuan remedial:

- Remedial hanya berlaku untuk tugas pemrograman (T1–T6) dan proyek akhir.
- Nilai maksimal remedial adalah **70** (huruf B-).
- Remedial harus dikerjakan ulang secara mandiri dan memenuhi seluruh kriteria rubrik.

---

*Dokumen ini merupakan bagian dari perangkat pembelajaran mata kuliah Algoritma dan Pemrograman, Semester Genap 2025/2026, Universitas Al Azhar Indonesia.*

*Disusun oleh: Tri Aji Nugroho, S.T., M.T.*
*Jakarta, Februari 2026*
