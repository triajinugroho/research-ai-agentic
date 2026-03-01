# Framework Asesmen — Praktikum Algoritma dan Pemrograman

> **Mata Kuliah:** Praktikum Algoritma dan Pemrograman — 1 SKS (Praktikum)
> **Kode MK:** INF-102
> **Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.
> **Program Studi:** Informatika, Universitas Al Azhar Indonesia
> **Semester:** Genap 2025/2026
> **Bahasa Pemrograman:** Python
> **Platform Utama:** Google Colab
> **Ko-requisite:** Algoritma dan Pemrograman (INF-101, 2 SKS Teori)

---

## 1. Filosofi Asesmen

### 1.1 Assessment FOR Learning sebagai Pendekatan Dominan

Framework asesmen mata kuliah praktikum ini dirancang dengan penekanan kuat pada **Assessment FOR Learning (Formatif)** sebagai pendekatan dominan. Berbeda dengan mata kuliah teori yang memiliki porsi sumatif lebih besar melalui UTS dan UAS, praktikum menekankan pembangunan keterampilan secara bertahap dan berkelanjutan melalui latihan langsung (*hands-on*).

**Assessment FOR Learning (Formatif) — Dominan**
Asesmen formatif menjadi tulang punggung evaluasi praktikum. Melalui laporan praktikum mingguan, tugas pemrograman, dan proyek akhir, mahasiswa menerima umpan balik secara terus-menerus yang memungkinkan mereka memperbaiki kode, memperdalam pemahaman, dan membangun kebiasaan pemrograman yang baik. Dosen dan asisten memberikan umpan balik konstruktif pada setiap submission, bukan sekadar nilai angka.

Instrumen formatif meliputi:
- **Laporan Praktikum (L1-L14)**: Umpan balik mingguan atas notebook Google Colab yang dikumpulkan setelah setiap sesi lab
- **Tugas Pemrograman (T1-T6)**: Umpan balik pada kode take-home yang dikerjakan secara mandiri
- **Proyek Akhir**: Umpan balik bertahap melalui proposal, progress check, dan final review
- **Partisipasi Lab**: Observasi langsung dan umpan balik verbal selama sesi praktikum

**Assessment OF Learning (Sumatif) — Pelengkap**
Asesmen sumatif digunakan secara terbatas melalui **Responsi Tengah Semester (RTS)** dan **Responsi Akhir Semester (RAS)** untuk memverifikasi bahwa mahasiswa benar-benar menguasai keterampilan pemrograman secara mandiri tanpa bantuan AI. Responsi berfungsi sebagai checkpoint independensi mahasiswa.

### 1.2 Hands-on Skill Building

Seluruh asesmen dalam mata kuliah praktikum dirancang agar mahasiswa **langsung menulis kode** (*learning by doing*). Tidak ada ujian tertulis di atas kertas — seluruh evaluasi dilakukan melalui implementasi kode Python di Google Colab. Pendekatan ini memastikan:

- **Keterampilan prosedural**: Mahasiswa terbiasa menulis, menjalankan, dan men-debug kode secara mandiri
- **Pembiasaan alat kerja**: Mahasiswa menguasai Google Colab sebagai lingkungan pengembangan
- **Iterasi dan perbaikan**: Mahasiswa dapat memperbaiki kode berdasarkan umpan balik sebelum penilaian akhir
- **Portofolio kode**: Akumulasi laporan dan tugas membentuk portofolio keterampilan pemrograman mahasiswa

### 1.3 Asesmen Autentik melalui Coding

Asesmen autentik berarti setiap tugas dan evaluasi dirancang agar relevan dengan dunia nyata (*real-world relevant*). Prinsip-prinsip asesmen autentik yang diterapkan dalam praktikum:

- **Masalah nyata**: Tugas menggunakan skenario kehidupan sehari-hari di Indonesia (kalkulator, pengolahan data, pencarian dan pengurutan data)
- **Alat dan proses profesional**: Mahasiswa menggunakan Google Colab, menulis dokumentasi, dan menerapkan standar kode (PEP 8) sebagaimana praktik industri
- **End-to-end development**: Proyek akhir mensimulasikan siklus pengembangan perangkat lunak dari analisis masalah hingga presentasi produk
- **AI sebagai coding partner**: Mahasiswa belajar menggunakan AI secara etis dan bertanggung jawab — keterampilan yang esensial di dunia kerja modern

### 1.4 Alignment dengan Taksonomi Bloom

Asesmen praktikum menekankan jenjang kognitif menengah hingga tinggi pada Taksonomi Bloom yang Direvisi, sesuai dengan sifat hands-on mata kuliah:

| Jenjang Bloom | Level | Instrumen Asesmen Praktikum |
|---|---|---|
| Menerapkan (C3) | Menengah | Laporan praktikum, tugas pemrograman T1-T4, responsi |
| Menganalisis (C4) | Menengah | Tugas T5-T6, laporan analisis algoritma, responsi |
| Mengevaluasi (C5) | Tinggi | Perbandingan algoritma (benchmarking), evaluasi kode AI |
| Mencipta (C6) | Tinggi | Proyek akhir (end-to-end program) |

---

## 2. Komponen Penilaian

| No | Komponen | Bobot | Frekuensi | Sifat |
|---|---|---|---|---|
| 1 | Laporan Praktikum (L1-L14) | 25% | 14 laporan (13 sesi lab + 1 sesi AI) | Individu, take-home |
| 2 | Tugas Pemrograman (T1-T6) | 25% | 6 tugas | Individu, take-home |
| 3 | Proyek Akhir | 35% | 1 proyek (3 tahap) | Individu/berpasangan |
| 4 | Responsi (RTS + RAS) | 10% | 2 kali | Individu, closed-book |
| 5 | Partisipasi Lab | 5% | Sepanjang semester | Individu |
| | **Total** | **100%** | | |

---

## 3. Detail per Komponen

### 3.1 Laporan Praktikum (L1-L14) — 25%

Setiap sesi lab mengharuskan mahasiswa mengumpulkan **Google Colab notebook** sebagai laporan praktikum. Notebook ini berisi seluruh latihan yang dikerjakan selama sesi lab beserta latihan mandiri tambahan. Total terdapat 14 laporan yang mencakup 13 sesi lab reguler dan 1 sesi AI-augmented programming.

| Laporan | Minggu | Topik | CPMK |
|---|---|---|---|
| LP1 | 1 | Setup Python & Google Colab | CPMK-1 |
| LP2 | 2 | Variabel, Tipe Data, Operator, I/O | CPMK-2 |
| LP3 | 3 | Struktur Seleksi (if/elif/else) | CPMK-3 |
| LP4 | 4 | Perulangan dan Pattern Printing | CPMK-3 |
| LP5 | 5 | Fungsi dan Refactoring | CPMK-4 |
| LP6 | 6 | Pengolahan String dan Teks | CPMK-4 |
| LP7 | 7 | List dan Tuple | CPMK-4, CPMK-5 |
| — | 8 | *(RTS — tidak ada laporan)* | — |
| LP9 | 9 | Dictionary dan Set | CPMK-5 |
| LP10 | 10 | Algoritma Pencarian | CPMK-6 |
| LP11 | 11 | Algoritma Pengurutan | CPMK-6 |
| LP12 | 12 | Rekursi | CPMK-6 |
| LP13 | 13 | Analisis Empiris Kompleksitas Algoritma | CPMK-6, CPMK-7 |
| LP14 | 14 | AI-Augmented Programming Hands-on | CPMK-7 |

**Ketentuan Laporan Praktikum:**
- **Format**: Google Colab notebook (.ipynb)
- **Penamaan**: `LP[nomor]_NIM_NamaDepan.ipynb` (contoh: `LP01_2025001_Andi.ipynb`)
- **Deadline**: H+3 (3 hari kalender) setelah sesi lab, pukul 23:59 WIB
- **Pengumpulan**: Melalui LMS UAI
- **Rubrik**: Penilaian berdasarkan 4 dimensi — lihat **rubrik-laporan-praktikum.md**

**Perhitungan Nilai Laporan Praktikum:**

```
Nilai Laporan = Rata-rata(LP1, LP2, LP3, LP4, LP5, LP6, LP7, LP9, LP10, LP11, LP12, LP13, LP14)
Kontribusi ke Nilai Akhir = Nilai Laporan x 25%
```

### 3.2 Tugas Pemrograman (T1-T6) — 25%

Tugas pemrograman adalah tugas *take-home* individu yang menantang mahasiswa untuk menyelesaikan masalah pemrograman secara mandiri. Setiap tugas dirancang untuk menguji penerapan konsep-konsep spesifik yang dipelajari di sesi lab dan perkuliahan teori.

| Tugas | Minggu | Judul | Deskripsi Singkat | CPMK |
|---|---|---|---|---|
| T1 | 2 | Kalkulator Sederhana | Membangun program kalkulator interaktif dengan validasi input menggunakan variabel, tipe data, operator, dan I/O | CPMK-2 |
| T2 | 4 | Pattern Printing | Mencetak pola bintang (segitiga, piramida, berlian) menggunakan nested loop dan teknik perulangan | CPMK-3 |
| T3 | 5 | Refactoring with Functions | Me-refactor kode prosedural dari tugas sebelumnya menjadi kode modular berbasis fungsi dengan docstring | CPMK-4 |
| T4 | 7 | Data Processing with Collections | Membangun program pengolahan data menggunakan list, tuple, dictionary, dan/atau set | CPMK-4, CPMK-5 |
| T5 | 10 | Algoritma Pencarian | Mengimplementasikan linear search dan binary search untuk pencarian data dalam dataset | CPMK-6 |
| T6 | 11 | Algoritma Pengurutan | Mengimplementasikan dan membandingkan algoritma pengurutan (bubble, selection, insertion sort) | CPMK-6 |

**Ketentuan Tugas Pemrograman:**
- **Format**: Google Colab notebook (.ipynb) atau file Python (.py)
- **Penamaan**: `T[nomor]_NIM_NamaDepan.ipynb` (contoh: `T1_2025001_Andi.ipynb`)
- **Deadline**: Jumat pukul 23:59 WIB pada minggu yang ditentukan
- **AI Policy**: AI diperbolehkan dengan wajib AI Usage Log
- **Rubrik**: Penilaian berdasarkan 4 dimensi — lihat **rubrik-tugas.md**

**Perhitungan Nilai Tugas Pemrograman:**

```
Nilai Tugas = Rata-rata(T1, T2, T3, T4, T5, T6)
Kontribusi ke Nilai Akhir = Nilai Tugas x 25%
```

### 3.3 Proyek Akhir — 35%

Proyek akhir merupakan asesmen autentik utama yang mengintegrasikan seluruh capaian pembelajaran praktikum. Mahasiswa membangun **program Python end-to-end** yang menyelesaikan masalah dunia nyata. Proyek dapat dikerjakan secara **individu** atau **berpasangan (maksimal 2 orang)**.

**Timeline Proyek Akhir:**

| Tahap | Minggu | Deliverable | Bobot (dari 35%) | Deadline |
|---|---|---|---|---|
| **Proposal** | 10 | Dokumen proposal 1 halaman | 5% | Jumat, Minggu 10, 23:59 WIB |
| **Progress Report** | 12 | Laporan kemajuan + Demo 50% kode berjalan | 10% | Jumat, Minggu 12, 23:59 WIB |
| **Final Submission + Presentasi** | 15 | Source code lengkap + Dokumentasi + AI Usage Log + Presentasi & Demo | 85% | Sesuai jadwal yang ditentukan |

**Persyaratan Teknis Proyek:**
- Minimal 5 fungsi modular dengan docstring
- Minimal 3 jenis struktur data berbeda (list, dict, set/tuple)
- Minimal 1 algoritma searching dan/atau sorting
- File I/O (save/load data)
- Error handling dengan `try-except`
- Kode sesuai standar PEP 8
- AI Usage Log lengkap

**Detail**: Lihat **project-guidelines.md** untuk panduan lengkap, template proposal, template AI Usage Log, dan rubrik penilaian proyek.

### 3.4 Responsi (RTS + RAS) — 10%

Responsi adalah ujian praktik (*coding test*) yang bertujuan memverifikasi penguasaan mandiri mahasiswa terhadap materi pemrograman. Responsi bersifat **closed-book**, **tanpa AI tools**, dan dikerjakan secara **individu** di Google Colab.

| Responsi | Minggu | Cakupan | Durasi | Bobot | Sifat |
|---|---|---|---|---|---|
| **RTS** (Responsi Tengah Semester) | 8 | Minggu 1-7: Setup, variabel, tipe data, operator, seleksi, perulangan, fungsi, string, list, tuple | 60 menit | 5% | Closed-book, tanpa AI, individu |
| **RAS** (Responsi Akhir Semester) | 16 | Minggu 9-14: Dictionary, set, searching, sorting, rekursi, analisis kompleksitas, AI-augmented programming | 60 menit | 5% | Closed-book, tanpa AI, individu |

**Ketentuan Responsi:**
- Dikerjakan secara mandiri di Google Colab tanpa akses AI tools, internet (selain Colab), atau catatan
- Soal berupa implementasi kode Python (menulis program yang berjalan dan menghasilkan output benar)
- Mahasiswa yang tidak hadir tanpa alasan sah mendapat nilai 0 untuk komponen tersebut
- Responsi susulan hanya diberikan dengan surat keterangan resmi, paling lambat 1 minggu setelah jadwal asal
- Nilai maksimal responsi susulan: 80% dari nilai penuh

**Perhitungan Nilai Responsi:**

```
Nilai Responsi = (Nilai RTS x 0.50) + (Nilai RAS x 0.50)
Kontribusi ke Nilai Akhir = Nilai Responsi x 10%
```

### 3.5 Partisipasi Lab — 5%

Partisipasi lab dinilai secara akumulatif sepanjang semester berdasarkan observasi langsung selama sesi praktikum.

| Aspek | Bobot (dari 5%) | Deskripsi |
|---|---|---|
| **Kehadiran** | 40% | Persentase kehadiran di sesi praktikum. Minimal 75% untuk lulus |
| **Keaktifan Coding** | 35% | Aktif mengerjakan latihan selama sesi, tidak pasif atau mengerjakan hal lain |
| **Peer Help** | 25% | Membantu rekan yang kesulitan tanpa memberikan jawaban langsung (*scaffolding*), berkontribusi dalam diskusi teknis |

**Penilaian Kehadiran:**

| Persentase Kehadiran | Skor | Keterangan |
|---|---|---|
| 90-100% | 100 | Komitmen kehadiran sangat baik |
| 80-89% | 80 | Kehadiran baik |
| 75-79% | 60 | Kehadiran cukup, memenuhi batas minimal |
| < 75% | 0 | **Tidak lulus mata kuliah** (nilai E otomatis) |

**Perhitungan Nilai Partisipasi:**

```
Nilai Partisipasi = (Kehadiran x 0.40) + (Keaktifan Coding x 0.35) + (Peer Help x 0.25)
Kontribusi ke Nilai Akhir = Nilai Partisipasi x 5%
```

---

## 4. Matriks CPMK x Asesmen

Tabel berikut menunjukkan keterkaitan antara setiap CPMK dengan instrumen asesmen yang mengukurnya:

| CPMK | Deskripsi | Laporan | Tugas | Proyek Akhir | Responsi | Partisipasi |
|---|---|---|---|---|---|---|
| **CPMK-1** | Menyiapkan lingkungan pemrograman dan alur kerja di Google Colab | LP1 | — | — | RTS | v |
| **CPMK-2** | Mengimplementasikan variabel, tipe data, operator, dan ekspresi | LP2 | T1 | — | RTS | — |
| **CPMK-3** | Mengimplementasikan struktur kontrol (seleksi dan perulangan) | LP3, LP4 | T2, T3 | v | RTS | — |
| **CPMK-4** | Mengimplementasikan fungsi, string processing, dan modularitas | LP5, LP6, LP7 | T3, T4 | v | RTS | v |
| **CPMK-5** | Mengimplementasikan dan memanipulasi struktur data (list, tuple, dict, set) | LP7, LP9 | T4 | v | RAS | — |
| **CPMK-6** | Mengimplementasikan algoritma pencarian, pengurutan, dan rekursi | LP10, LP11, LP12, LP13 | T5, T6 | v | RAS | — |
| **CPMK-7** | Membangun solusi end-to-end dengan memanfaatkan AI secara bertanggung jawab | LP14 | — | v | RAS | v |

**Keterangan:**
- LP(n) = Laporan Praktikum spesifik yang mengukur CPMK
- T(n) = Tugas Pemrograman spesifik yang mengukur CPMK
- v = Diukur melalui instrumen asesmen tersebut
- RTS/RAS = Diukur melalui responsi yang bersangkutan

---

## 5. Kebijakan Penggunaan AI (AI Usage Policy)

Mata kuliah praktikum ini mengadopsi pendekatan **"AI as Coding Partner"** di mana AI dianggap sebagai alat bantu yang harus digunakan secara etis, transparan, dan bertanggung jawab.

### 5.1 Tabel Kebijakan AI per Komponen

| No | Komponen | AI Diperbolehkan? | AI Usage Log Wajib? | Keterangan |
|---|---|---|---|---|
| 1 | Laporan Praktikum (L1-L14) | Ya, sebagai referensi | Ya, jika digunakan secara signifikan | AI boleh untuk membantu pemahaman konsep; kode harus ditulis dan dipahami sendiri |
| 2 | Tugas Pemrograman (T1-T6) | Ya, dengan batasan | Ya, wajib | AI sebagai tutor dan debugger, bukan penulis kode utama |
| 3 | Proyek Akhir | Ya, dengan batasan | Ya, wajib (detail) | AI boleh untuk brainstorm, debug, refactor; bukan generate seluruh kode |
| 4 | Responsi (RTS + RAS) | **Tidak** | Tidak | Closed-book, tanpa AI tools, dikerjakan mandiri |
| 5 | Partisipasi Lab | Ya (untuk persiapan) | Tidak | Boleh gunakan AI untuk menyiapkan diri sebelum sesi lab |

### 5.2 Prinsip AI Usage

1. **Transparansi**: Selalu dokumentasikan penggunaan AI dalam AI Usage Log
2. **Pemahaman**: Mahasiswa harus mampu menjelaskan setiap baris kode yang dihasilkan AI jika diminta oleh dosen atau asisten
3. **Kreativitas**: AI digunakan untuk mempercepat, bukan menggantikan proses berpikir
4. **Integritas**: Mengklaim karya AI sebagai karya sendiri tanpa dokumentasi merupakan pelanggaran akademik

### 5.3 Sanksi Pelanggaran

| Pelanggaran | Sanksi |
|---|---|
| Tidak mengisi AI Usage Log padahal menggunakan AI (tugas/proyek) | Pengurangan 30% dari nilai komponen terkait |
| Menggunakan AI saat Responsi (RTS/RAS) | Nilai 0 untuk komponen tersebut |
| Copy-paste kode AI tanpa pemahaman (terdeteksi saat tanya jawab/responsi) | Nilai 0 untuk komponen terkait + pelaporan ke prodi |
| Plagiarisme antar mahasiswa | Nilai 0 untuk semua pihak yang terlibat + pelaporan ke prodi |

---

## 6. Formula dan Konversi Nilai

### 6.1 Formula Perhitungan Nilai Akhir

```
Nilai Akhir = (Laporan Praktikum x 0.25) + (Tugas Pemrograman x 0.25) +
              (Proyek Akhir x 0.35) + (Responsi x 0.10) + (Partisipasi Lab x 0.05)
```

### 6.2 Konversi Nilai Huruf

Konversi nilai akhir numerik ke huruf mengikuti ketentuan Universitas Al Azhar Indonesia:

| Rentang Nilai | Huruf Mutu | Angka Mutu | Predikat |
|---|---|---|---|
| 85 - 100 | A | 4.00 | Sangat Baik |
| 80 - 84 | A- | 3.70 | Sangat Baik |
| 75 - 79 | B+ | 3.30 | Baik |
| 70 - 74 | B | 3.00 | Baik |
| 65 - 69 | B- | 2.70 | Cukup Baik |
| 60 - 64 | C+ | 2.30 | Cukup |
| 55 - 59 | C | 2.00 | Cukup |
| 40 - 54 | D | 1.00 | Kurang |
| 0 - 39 | E | 0.00 | Sangat Kurang |

### 6.3 Syarat Kelulusan

- Nilai minimal **C (55)** untuk lulus mata kuliah
- Kehadiran minimal **75%** dari total sesi praktikum
- Proyek akhir **wajib dikumpulkan** (tidak mengumpulkan proyek = tidak lulus)

### 6.4 Contoh Perhitungan Nilai Akhir

**Skenario A: Mahasiswa dengan Performa Baik**

| Komponen | Nilai (0-100) | Bobot | Kontribusi |
|---|---|---|---|
| Laporan Praktikum | 82 | 25% | 20.50 |
| Tugas Pemrograman | 85 | 25% | 21.25 |
| Proyek Akhir | 88 | 35% | 30.80 |
| Responsi | 75 | 10% | 7.50 |
| Partisipasi Lab | 90 | 5% | 4.50 |
| **Nilai Akhir** | | **100%** | **84.55** |

Nilai Akhir: **84.55** --> Huruf Mutu: **A-** (Angka Mutu: 3.70, Predikat: Sangat Baik)

**Skenario B: Mahasiswa dengan Performa Cukup**

| Komponen | Nilai (0-100) | Bobot | Kontribusi |
|---|---|---|---|
| Laporan Praktikum | 65 | 25% | 16.25 |
| Tugas Pemrograman | 60 | 25% | 15.00 |
| Proyek Akhir | 62 | 35% | 21.70 |
| Responsi | 55 | 10% | 5.50 |
| Partisipasi Lab | 70 | 5% | 3.50 |
| **Nilai Akhir** | | **100%** | **61.95** |

Nilai Akhir: **61.95** --> Huruf Mutu: **C+** (Angka Mutu: 2.30, Predikat: Cukup)

---

## 7. Kalender Asesmen

Tabel berikut merangkum seluruh jadwal asesmen sepanjang semester:

| Minggu | Laporan | Tugas | Responsi | Proyek |
|---|---|---|---|---|
| 1 | LP1 | | | |
| 2 | LP2 | **T1**: Kalkulator Sederhana | | |
| 3 | LP3 | | | |
| 4 | LP4 | **T2**: Pattern Printing | | |
| 5 | LP5 | **T3**: Refactoring with Functions | | |
| 6 | LP6 | | | |
| 7 | LP7 | **T4**: Data Processing with Collections | | |
| 8 | — | | **RTS** (Minggu 1-7) | |
| 9 | LP9 | | | |
| 10 | LP10 | **T5**: Algoritma Pencarian | | **Proposal Proyek** |
| 11 | LP11 | **T6**: Algoritma Pengurutan | | |
| 12 | LP12 | | | **Progress Report** |
| 13 | LP13 | | | Pengerjaan Proyek |
| 14 | LP14 | | | Pengerjaan Proyek |
| 15 | — | | | **Final Submission + Presentasi** |
| 16 | — | | **RAS** (Minggu 9-14) | |

**Catatan Deadline:**
- Laporan Praktikum: H+3 setelah sesi lab, pukul 23:59 WIB
- Tugas Pemrograman: Jumat pada minggu yang ditentukan, pukul 23:59 WIB
- Proposal Proyek: Jumat Minggu 10, pukul 23:59 WIB
- Progress Report: Jumat Minggu 12, pukul 23:59 WIB
- Final Submission: sesuai jadwal Minggu 15
- Responsi: sesuai jadwal yang ditentukan oleh dosen

---

## 8. Kebijakan Pengumpulan

### 8.1 Keterlambatan Pengumpulan

| Keterlambatan | Penalti |
|---|---|
| Tepat waktu | Tidak ada penalti |
| Terlambat 1 hari | -10% dari nilai maksimal |
| Terlambat 2 hari | -20% dari nilai maksimal |
| Terlambat 3 hari | -30% dari nilai maksimal |
| Lebih dari 3 hari | **Tidak dinilai** (nilai 0) |

> **Catatan:** Penalti dihitung per hari kalender (termasuk akhir pekan). Pengecualian hanya diberikan dengan alasan sah (sakit dengan surat dokter, keadaan darurat) dan harus dikomunikasikan kepada dosen **sebelum** deadline.

### 8.2 Format Pengumpulan

| Aspek | Ketentuan |
|---|---|
| **Format file** | Google Colab notebook (.ipynb) |
| **Platform** | LMS UAI (Google Classroom / sistem yang ditentukan) |
| **Penamaan Laporan** | `LP[nomor]_NIM_NamaDepan.ipynb` (contoh: `LP01_2025001_Andi.ipynb`) |
| **Penamaan Tugas** | `T[nomor]_NIM_NamaDepan.ipynb` (contoh: `T1_2025001_Andi.ipynb`) |
| **Penamaan Proyek** | `ProyekAkhir_NIM_NamaDepan.zip` |
| **Sharing** | Pastikan pengaturan sharing Google Colab aktif (*Anyone with the link can view*) |

### 8.3 Persyaratan Notebook

Setiap notebook yang dikumpulkan harus memenuhi kriteria berikut:
- **Seluruh cell sudah dieksekusi** — output harus terlihat di notebook
- **Cell markdown** berisi penjelasan dan refleksi
- **Header** berisi Nama, NIM, Mata Kuliah, dan Tanggal
- **Kode berjalan tanpa error** saat dijalankan ulang dari awal (*Runtime > Restart and run all*)
- **AI Usage Log** (jika menggunakan AI) dicantumkan di cell terakhir

---

## 9. Kebijakan Remedial dan Perbaikan

### 9.1 Laporan Praktikum

- Mahasiswa boleh mengumpulkan **perbaikan laporan** maksimal 3 laporan sepanjang semester
- Perbaikan harus dikumpulkan paling lambat **1 minggu** setelah umpan balik diberikan
- Nilai maksimal untuk laporan yang diperbaiki: **80% dari nilai penuh** (setara level Baik)

### 9.2 Tugas Pemrograman

- Mahasiswa boleh mengulang **maksimal 1 tugas** dari T1-T6 dengan nilai maksimal B (74)
- Syarat: tugas asli harus sudah dikumpulkan tepat waktu (termasuk terlambat dengan penalti)
- Revisi harus dikumpulkan paling lambat **1 minggu** setelah nilai diumumkan

### 9.3 Proyek Akhir

- Revisi proyek diperbolehkan jika ada catatan perbaikan dari progress report (Minggu 12)
- Revisi harus dimasukkan dalam final submission (Minggu 15)
- Tidak ada remedial setelah final submission dan presentasi

### 9.4 Responsi

- **Tidak ada remedial** untuk RTS dan RAS
- Responsi susulan hanya dengan surat keterangan resmi (sakit/izin institusi)
- Nilai maksimal responsi susulan: **80% dari nilai penuh**

### 9.5 Partisipasi Lab

- Tidak ada remedial untuk partisipasi
- Ketidakhadiran dengan alasan sah (surat dokter/surat resmi) tidak mengurangi persentase kehadiran

---

## 10. Komunikasi dan Transparansi

- Seluruh nilai diumumkan melalui LMS UAI dalam waktu **7 hari kerja** setelah asesmen
- Umpan balik tertulis diberikan pada setiap laporan praktikum dan tugas pemrograman
- Mahasiswa berhak mengajukan **keberatan nilai** dalam waktu **3 hari kerja** setelah pengumuman
- Dosen menyediakan **office hours** (minimal 1 jam/minggu) untuk konsultasi terkait asesmen
- Komunikasi asesmen dilakukan melalui kanal resmi: LMS UAI, email institusi, atau grup kelas

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
