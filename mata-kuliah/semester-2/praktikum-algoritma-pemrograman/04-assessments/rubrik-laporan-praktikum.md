# Rubrik Penilaian Laporan Praktikum — Praktikum Algoritma dan Pemrograman

> **Mata Kuliah:** Praktikum Algoritma dan Pemrograman — 1 SKS (Praktikum)
> **Kode MK:** INF-102
> **Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.
> **Program Studi:** Informatika, Universitas Al Azhar Indonesia
> **Semester:** Genap 2025/2026
> **Bahasa Pemrograman:** Python
> **Platform Utama:** Google Colab
> **Ko-requisite:** Algoritma dan Pemrograman (INF-101)

---

## 1. Deskripsi

Setiap sesi praktikum mengharuskan mahasiswa mengumpulkan **laporan praktikum** dalam bentuk **Google Colab notebook (.ipynb)**. Notebook ini merupakan catatan lengkap dari aktivitas hands-on mahasiswa selama sesi lab, mencakup seluruh latihan terbimbing, latihan mandiri, serta refleksi pembelajaran.

Terdapat **14 laporan praktikum** sepanjang semester (LP1-LP7 dan LP9-LP14), yang dikumpulkan setelah setiap sesi lab kecuali minggu responsi (Minggu 8 dan 16) dan minggu presentasi proyek (Minggu 15). Komponen laporan praktikum memiliki **bobot 25%** dari nilai akhir mata kuliah.

**Tujuan Laporan Praktikum:**

- Mendokumentasikan proses belajar dan eksplorasi kode mahasiswa
- Membangun kebiasaan menulis kode yang bersih, terdokumentasi, dan terstruktur
- Melatih kemampuan menjelaskan logika pemrograman dengan bahasa sendiri
- Membentuk portofolio keterampilan pemrograman sepanjang semester

---

## 2. Rubrik 4 Dimensi

Setiap laporan praktikum dinilai berdasarkan **4 dimensi** dengan skala **1-4** (Kurang, Cukup, Baik, Sangat Baik). Setiap dimensi memiliki bobot yang berbeda sesuai dengan prioritas pembelajaran praktikum.

### 2.1 Ringkasan Dimensi dan Bobot

| No | Dimensi | Bobot | Fokus Penilaian |
| --- | --- | --- | --- |
| 1 | Kelengkapan | 25% | Seluruh latihan dikerjakan dan seluruh cell dieksekusi |
| 2 | Pemahaman Konsep | 30% | Penjelasan markdown menunjukkan pemahaman, mampu menjelaskan logika kode |
| 3 | Kualitas Kode | 25% | PEP 8, penamaan bermakna, kode bersih, output benar |
| 4 | Dokumentasi & Refleksi | 20% | Komentar jelas, catatan reflektif, AI Usage Log (jika applicable) |

### 2.2 Tabel Rubrik Detail

| Dimensi (Bobot) | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
| --- | --- | --- | --- | --- |
| **Kelengkapan** (25%) | Seluruh latihan terbimbing dan latihan mandiri dikerjakan lengkap. Seluruh cell kode telah dieksekusi dan menampilkan output. Tidak ada cell yang kosong atau belum dijalankan. Latihan bonus (jika ada) juga dikerjakan. | Seluruh latihan terbimbing dikerjakan lengkap dan sebagian besar latihan mandiri selesai (minimal 80%). Seluruh cell telah dieksekusi. Terdapat 1-2 latihan mandiri yang belum selesai. | Latihan terbimbing sebagian besar dikerjakan (70-80%). Beberapa latihan mandiri belum selesai. Beberapa cell belum dieksekusi atau tidak menampilkan output. | Kurang dari 70% latihan dikerjakan. Banyak cell kosong atau belum dieksekusi. Latihan mandiri sebagian besar tidak dikerjakan. Notebook terkesan tidak lengkap. |
| **Pemahaman Konsep** (30%) | Cell markdown menunjukkan pemahaman mendalam terhadap konsep yang dipraktikkan. Mahasiswa mampu menjelaskan logika kode dengan kata-kata sendiri, bukan sekadar menyalin instruksi modul. Terdapat penjelasan *mengapa* suatu pendekatan dipilih, bukan hanya *apa* yang dilakukan. Mampu menghubungkan konsep praktikum dengan teori di INF-101. | Cell markdown menunjukkan pemahaman yang baik. Penjelasan logika kode ada dan cukup jelas, meskipun beberapa penjelasan masih bersifat deskriptif (menjelaskan *apa*) tanpa analisis mendalam (*mengapa*). Ada upaya menghubungkan dengan teori. | Cell markdown ada tetapi penjelasan dangkal atau hanya mengulang instruksi dari modul praktikum tanpa elaborasi. Pemahaman terhadap logika kode terbatas — mahasiswa menuliskan kode yang benar tetapi tidak mampu menjelaskan alasannya. | Cell markdown tidak ada atau sangat minim. Tidak ada penjelasan logika kode. Mahasiswa tampak menyalin kode tanpa pemahaman. Jika ada penjelasan, isinya tidak relevan atau mengandung miskonsepsi. |
| **Kualitas Kode** (25%) | Kode sepenuhnya mematuhi PEP 8: indentasi 4 spasi konsisten, penamaan variabel menggunakan `snake_case` yang deskriptif, baris tidak melebihi 79 karakter. Kode bersih, terstruktur, dan mudah dibaca. Output program benar untuk semua kasus. Tidak ada kode duplikat yang tidak perlu. Penggunaan fitur Python idiomatik (f-string, list comprehension, dll.) jika sesuai. | Kode sebagian besar mematuhi PEP 8. Penamaan variabel cukup deskriptif. Struktur kode cukup rapi dengan beberapa area yang bisa ditingkatkan. Output program benar untuk sebagian besar kasus. Terdapat sedikit kode redundan. | Kode memiliki beberapa pelanggaran PEP 8 (indentasi tidak konsisten, penamaan variabel kurang deskriptif seperti `x`, `temp`, `data1`). Beberapa output salah atau tidak sesuai harapan. Kode cukup sulit dibaca karena format tidak konsisten. | Kode tidak mematuhi PEP 8. Penamaan variabel tidak bermakna (misalnya `a`, `b`, `c`). Banyak error dan output yang salah. Kode sangat sulit dibaca. Format tidak rapi. Banyak cell menghasilkan error yang tidak ditangani. |
| **Dokumentasi & Refleksi** (20%) | Komentar pada kode jelas dan informatif — menjelaskan logika kompleks, bukan menjelaskan hal yang sudah jelas. Cell refleksi di akhir notebook berisi catatan reflektif yang bermakna: apa yang dipelajari, tantangan yang dihadapi, dan rencana perbaikan. AI Usage Log terisi detail dan lengkap jika AI digunakan (mencakup prompt, output, keputusan, dan refleksi). | Komentar pada kode ada di bagian-bagian penting. Cell refleksi ada dengan konten yang cukup bermakna. AI Usage Log terisi jika AI digunakan, meskipun kurang detail pada beberapa entri. | Komentar minim dan tidak konsisten — ada pada beberapa cell tetapi tidak pada yang lain. Cell refleksi ada tetapi isinya dangkal (misalnya hanya "Saya belajar tentang perulangan"). AI Usage Log ada tetapi kurang lengkap. | Tidak ada komentar pada kode sama sekali. Tidak ada cell refleksi. Tidak ada AI Usage Log padahal ada indikasi penggunaan AI. Notebook tidak memiliki dokumentasi yang bermakna. |

---

## 3. Skala Penilaian — Deskripsi Detail per Level

### Level 4: Sangat Baik (Skor 4)

Laporan praktikum pada level ini menunjukkan **penguasaan penuh** terhadap materi sesi lab. Ciri-ciri utama:

- Seluruh latihan dikerjakan lengkap, termasuk latihan bonus
- Penjelasan markdown menunjukkan pemahaman mendalam dan kemampuan berpikir kritis
- Kode bersih, PEP 8, dan idiomatik
- Refleksi bermakna yang menunjukkan proses belajar aktif
- AI Usage Log (jika ada) lengkap dan reflektif

**Rentang skor terbobot**: 3.50 - 4.00 --> **Konversi ke skala 100: 87.50 - 100.00**

### Level 3: Baik (Skor 3)

Laporan praktikum pada level ini menunjukkan **pemahaman yang baik** dengan ruang perbaikan minor. Ciri-ciri utama:

- Sebagian besar latihan dikerjakan (minimal 80%)
- Penjelasan markdown cukup jelas, menunjukkan pemahaman konsep
- Kode sebagian besar sesuai PEP 8, penamaan cukup deskriptif
- Refleksi ada dengan konten yang cukup bermakna
- AI Usage Log cukup lengkap jika AI digunakan

**Rentang skor terbobot**: 2.50 - 3.49 --> **Konversi ke skala 100: 62.50 - 87.25**

### Level 2: Cukup (Skor 2)

Laporan praktikum pada level ini menunjukkan **pemahaman dasar** yang memerlukan perbaikan signifikan. Ciri-ciri utama:

- Latihan terbimbing sebagian besar dikerjakan, latihan mandiri tidak lengkap
- Penjelasan markdown dangkal atau mengulang instruksi modul
- Kode memiliki beberapa pelanggaran PEP 8 dan output tidak selalu benar
- Dokumentasi dan refleksi minim

**Rentang skor terbobot**: 1.50 - 2.49 --> **Konversi ke skala 100: 37.50 - 62.25**

### Level 1: Kurang (Skor 1)

Laporan praktikum pada level ini menunjukkan **upaya minimal** dan pemahaman yang sangat terbatas. Ciri-ciri utama:

- Sebagian besar latihan tidak dikerjakan
- Tidak ada penjelasan atau penjelasan tidak relevan
- Kode penuh error, tidak mengikuti standar apa pun
- Tidak ada dokumentasi atau refleksi

**Rentang skor terbobot**: 1.00 - 1.49 --> **Konversi ke skala 100: 25.00 - 37.25**

---

## 4. Perhitungan Skor Laporan Praktikum

### 4.1 Formula Perhitungan

Skor setiap laporan praktikum dihitung berdasarkan skor pada 4 dimensi dengan bobot masing-masing:

```text
Skor Laporan = (Kelengkapan x 0.25) + (Pemahaman Konsep x 0.30) +
               (Kualitas Kode x 0.25) + (Dokumentasi & Refleksi x 0.20)

Skor Laporan (skala 100) = (Skor Laporan / 4) x 100
```

### 4.2 Nilai Akhir Komponen Laporan Praktikum

```text
Nilai Laporan = Rata-rata(LP1, LP2, LP3, LP4, LP5, LP6, LP7, LP9, LP10, LP11, LP12, LP13, LP14)
Kontribusi ke Nilai Akhir = Nilai Laporan x 25%
```

---

## 5. Format Pengumpulan

### 5.1 Konvensi Penamaan File

```text
LP[nomor 2 digit]_[NIM]_[NamaDepan].ipynb
```

**Contoh:**

- `LP01_2025001_Andi.ipynb` (Laporan Praktikum 1)
- `LP07_2025001_Andi.ipynb` (Laporan Praktikum 7)
- `LP14_2025001_Andi.ipynb` (Laporan Praktikum 14)

### 5.2 Deadline Pengumpulan

- **Batas waktu**: **H+3** (3 hari kalender) setelah sesi lab, pukul **23:59 WIB**
- Contoh: Jika sesi lab pada hari Selasa, deadline pengumpulan adalah hari Jumat pukul 23:59 WIB

### 5.3 Platform Pengumpulan

- Pengumpulan dilakukan melalui **LMS UAI** (Google Classroom atau sistem yang ditentukan)
- Pastikan pengaturan sharing Google Colab aktif: *Anyone with the link can view*
- Mahasiswa wajib memverifikasi bahwa notebook dapat diakses oleh dosen/asisten setelah dikumpulkan

### 5.4 Struktur Notebook yang Diharapkan

Setiap notebook laporan praktikum sebaiknya memiliki struktur sebagai berikut:

```text
1. Cell Markdown: Header (Nama, NIM, Mata Kuliah, Sesi Lab, Tanggal)
2. Cell Markdown: Tujuan Praktikum
3. Cell Kode + Markdown: Latihan Terbimbing (sesuai modul)
   - Penjelasan sebelum kode
   - Kode yang sudah dieksekusi
   - Analisis output
4. Cell Kode + Markdown: Latihan Mandiri
   - Penjelasan pendekatan
   - Kode yang sudah dieksekusi
   - Analisis output
5. Cell Markdown: Refleksi Pembelajaran
   - Apa yang dipelajari
   - Tantangan yang dihadapi
   - Rencana perbaikan
6. Cell Markdown: AI Usage Log (jika menggunakan AI)
```

### 5.5 Kebijakan Keterlambatan

| Keterlambatan | Penalti |
| --- | --- |
| Tepat waktu (H+3) | Tidak ada penalti |
| Terlambat 1 hari (H+4) | -10% dari nilai |
| Terlambat 2 hari (H+5) | -20% dari nilai |
| Terlambat 3 hari (H+6) | -30% dari nilai |
| Lebih dari 3 hari (> H+6) | **Tidak dinilai** (nilai 0) |

---

## 6. Contoh Penilaian

### 6.1 Skenario A: Mahasiswa dengan Performa Tinggi — LP4 (Perulangan dan Pattern Printing)

Mahasiswa A mengerjakan seluruh latihan terbimbing dan mandiri termasuk latihan bonus cetak pola berlian. Penjelasan markdown detail, menjelaskan mengapa nested loop diperlukan untuk pola 2D dan bagaimana hubungan antara baris dan jumlah bintang. Kode sesuai PEP 8 dengan penamaan variabel seperti `jumlah_baris`, `spasi`, `bintang`. Refleksi menjelaskan bahwa tantangan utama adalah menentukan formula spasi dan bintang pada pola berlian.

| Dimensi | Bobot | Level | Skor | Skor Terbobot |
| --- | --- | --- | --- | --- |
| Kelengkapan | 25% | Sangat Baik (4) | 4 | 1.00 |
| Pemahaman Konsep | 30% | Sangat Baik (4) | 4 | 1.20 |
| Kualitas Kode | 25% | Baik (3) | 3 | 0.75 |
| Dokumentasi & Refleksi | 20% | Sangat Baik (4) | 4 | 0.80 |
| **Total** | | | | **3.75** |

```text
Skor LP4 (skala 100) = (3.75 / 4) x 100 = 93.75
```

**Keterangan:** Mahasiswa A menunjukkan pemahaman dan dokumentasi yang sangat baik. Kualitas kode sedikit di bawah maksimal karena beberapa variabel masih menggunakan nama pendek pada latihan terakhir.

### 6.2 Skenario B: Mahasiswa dengan Performa Sedang — LP4 (Perulangan dan Pattern Printing)

Mahasiswa B mengerjakan seluruh latihan terbimbing dan 3 dari 4 latihan mandiri. Penjelasan markdown ada tetapi sebagian besar mendeskripsikan *apa* yang dilakukan kode, bukan *mengapa*. Kode cukup rapi tetapi beberapa variabel menggunakan nama kurang deskriptif (`n`, `i`, `j`). Refleksi singkat: "Saya belajar tentang nested loop untuk membuat pola."

| Dimensi | Bobot | Level | Skor | Skor Terbobot |
| --- | --- | --- | --- | --- |
| Kelengkapan | 25% | Baik (3) | 3 | 0.75 |
| Pemahaman Konsep | 30% | Cukup (2) | 2 | 0.60 |
| Kualitas Kode | 25% | Baik (3) | 3 | 0.75 |
| Dokumentasi & Refleksi | 20% | Cukup (2) | 2 | 0.40 |
| **Total** | | | | **2.50** |

```text
Skor LP4 (skala 100) = (2.50 / 4) x 100 = 62.50
```

**Keterangan:** Mahasiswa B perlu meningkatkan kedalaman pemahaman dan kualitas refleksi. Disarankan untuk menjelaskan *mengapa* suatu pendekatan dipilih, bukan hanya mendeskripsikan kode.

### 6.3 Skenario C: Mahasiswa dengan Performa Rendah — LP4 (Perulangan dan Pattern Printing)

Mahasiswa C hanya mengerjakan latihan terbimbing (tidak ada latihan mandiri). Tidak ada cell markdown penjelasan. Kode memiliki beberapa error (pola segitiga terbalik menghasilkan output yang salah). Tidak ada komentar dalam kode dan tidak ada refleksi di akhir notebook.

| Dimensi | Bobot | Level | Skor | Skor Terbobot |
| --- | --- | --- | --- | --- |
| Kelengkapan | 25% | Kurang (1) | 1 | 0.25 |
| Pemahaman Konsep | 30% | Kurang (1) | 1 | 0.30 |
| Kualitas Kode | 25% | Cukup (2) | 2 | 0.50 |
| Dokumentasi & Refleksi | 20% | Kurang (1) | 1 | 0.20 |
| **Total** | | | | **1.25** |

```text
Skor LP4 (skala 100) = (1.25 / 4) x 100 = 31.25
```

**Keterangan:** Mahasiswa C memerlukan bimbingan intensif. Disarankan untuk menemui dosen atau asisten pada jam konsultasi (*office hours*) dan mengajukan perbaikan laporan sesuai kebijakan remedial.

### 6.4 Simulasi Nilai Komponen Laporan Praktikum

Berikut simulasi nilai akhir komponen Laporan Praktikum untuk Mahasiswa A (performa tinggi) sepanjang semester:

| Laporan | Skor (skala 100) |
| --- | --- |
| LP1 | 87.50 |
| LP2 | 90.00 |
| LP3 | 85.00 |
| LP4 | 93.75 |
| LP5 | 87.50 |
| LP6 | 90.00 |
| LP7 | 85.00 |
| LP9 | 87.50 |
| LP10 | 90.00 |
| LP11 | 93.75 |
| LP12 | 87.50 |
| LP13 | 85.00 |
| LP14 | 90.00 |

```text
Nilai Laporan = Rata-rata seluruh LP = (87.50 + 90.00 + 85.00 + 93.75 + 87.50 + 90.00 +
                85.00 + 87.50 + 90.00 + 93.75 + 87.50 + 85.00 + 90.00) / 13
             = 1151.50 / 13
             = 88.58

Kontribusi ke Nilai Akhir = 88.58 x 25% = 22.15 poin
```

---

## 7. Catatan untuk Dosen dan Asisten Praktikum

### 7.1 Konsistensi Penilaian

- Gunakan rubrik ini secara konsisten untuk setiap laporan dan setiap mahasiswa
- Diskusikan rubrik dengan asisten praktikum di awal semester untuk memastikan pemahaman yang seragam
- Lakukan kalibrasi penilaian: ambil 5 sampel laporan, nilai secara independen oleh dosen dan asisten, kemudian bandingkan dan selaraskan

### 7.2 Umpan Balik

- Berikan umpan balik tertulis singkat (minimal 2-3 kalimat) pada setiap laporan, bukan hanya skor
- Umpan balik harus spesifik dan konstruktif: tunjukkan apa yang sudah baik dan apa yang perlu diperbaiki
- Umpan balik dikembalikan paling lambat **7 hari kerja** setelah deadline pengumpulan

### 7.3 Penanganan Kasus Khusus

| Kasus | Penanganan |
| --- | --- |
| Notebook tidak dapat diakses (sharing tidak aktif) | Hubungi mahasiswa, beri waktu 24 jam untuk memperbaiki. Jika tidak diperbaiki, dianggap belum mengumpulkan |
| Notebook kosong atau hanya berisi header | Nilai 0 untuk laporan tersebut |
| Duplikasi laporan antar mahasiswa | Nilai 0 untuk kedua pihak, ditangani sebagai pelanggaran integritas akademik |
| Mahasiswa sakit/berhalangan hadir di sesi lab | Mahasiswa tetap wajib mengerjakan modul praktikum secara mandiri dan mengumpulkan laporan sesuai deadline |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
