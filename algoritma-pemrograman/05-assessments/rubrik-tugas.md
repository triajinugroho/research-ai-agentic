# Rubrik Penilaian Tugas -- Algoritma dan Pemrograman

> **Mata Kuliah:** Algoritma dan Pemrograman (3 SKS)
> **Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.
> **Program Studi:** Informatika, Universitas Al Azhar Indonesia
> **Semester:** Genap 2025/2026
> **Bahasa Pemrograman:** Python

---

## 1. Rubrik Umum 4 Dimensi

Rubrik berikut digunakan untuk menilai seluruh tugas pemrograman (T1-T6). Setiap dimensi dinilai dengan skala 1-4.

---

### Dimensi 1: Teknis / Kebenaran (25%)

| Skor | Level | Deskripsi |
|---|---|---|
| **4** | **Sangat Baik** | Semua output benar untuk seluruh test case, termasuk edge cases. Program berjalan tanpa error. Validasi input lengkap. Tidak ada bug yang terdeteksi. |
| **3** | **Baik** | Output benar untuk semua kasus utama. Minor edge case terlewat (misal: input kosong atau nilai negatif). Program berjalan tanpa crash. |
| **2** | **Cukup** | Beberapa output salah untuk kasus utama. Ada error handling dasar tetapi tidak komprehensif. Program bisa crash pada input tertentu. |
| **1** | **Kurang** | Banyak output salah. Program sering error atau tidak berjalan sempurna. Tidak ada validasi input. Logika dasar bermasalah. |

---

### Dimensi 2: Problem Solving / Pemecahan Masalah (30%)

| Skor | Level | Deskripsi |
|---|---|---|
| **4** | **Sangat Baik** | Pendekatan solusi efisien dan elegan. Dekomposisi masalah jelas menjadi sub-masalah. Logika solid tanpa langkah yang tidak perlu. Pemilihan struktur data dan algoritma tepat. |
| **3** | **Baik** | Pendekatan solusi tepat dan fungsional. Dekomposisi cukup baik. Logika benar meskipun ada beberapa langkah yang bisa dioptimasi. |
| **2** | **Cukup** | Pendekatan kurang efisien (misal: redundansi kode, nested loop berlebihan). Dekomposisi kurang jelas. Beberapa bagian logika berbelit. |
| **1** | **Kurang** | Pendekatan tidak tepat untuk masalah yang diberikan. Tidak ada dekomposisi. Logika sulit diikuti atau salah secara fundamental. |

---

### Dimensi 3: Kode Python / Kualitas Kode (25%)

| Skor | Level | Deskripsi |
|---|---|---|
| **4** | **Sangat Baik** | PEP 8 compliant sepenuhnya. Nama variabel dan fungsi bermakna (snake_case). Komentar tepat dan informatif. Kode bersih, rapi, mudah dibaca. Penggunaan fitur Python yang idiomatik. |
| **3** | **Baik** | Sebagian besar mengikuti PEP 8. Nama variabel cukup bermakna. Komentar ada di bagian penting. Kode cukup rapi. |
| **2** | **Cukup** | Beberapa pelanggaran PEP 8 (indentasi tidak konsisten, baris terlalu panjang). Nama variabel kurang bermakna (misal: `x`, `a`, `temp1`). Komentar minim. |
| **1** | **Kurang** | Tidak mengikuti PEP 8. Nama variabel tidak bermakna. Tidak ada komentar. Kode sulit dibaca dan dipahami. Format tidak rapi. |

---

### Dimensi 4: Presentasi / Dokumentasi (20%)

| Skor | Level | Deskripsi |
|---|---|---|
| **4** | **Sangat Baik** | README lengkap (deskripsi, cara menjalankan, contoh output). Komentar informatif di dalam kode. AI Usage Log terisi detail (prompt, respons, modifikasi, refleksi). |
| **3** | **Baik** | Dokumentasi cukup lengkap. Komentar ada di bagian penting. AI Usage Log terisi dengan informasi yang memadai. |
| **2** | **Cukup** | Dokumentasi minim (hanya nama dan NIM). Komentar sangat sedikit. AI Usage Log ada tetapi tidak detail. |
| **1** | **Kurang** | Tidak ada dokumentasi. Tidak ada komentar bermakna di kode. AI Usage Log tidak ada. |

---

### Tabel Ringkasan Rubrik Umum

| Dimensi | Bobot | Skor 4 (Sangat Baik) | Skor 3 (Baik) | Skor 2 (Cukup) | Skor 1 (Kurang) |
|---|---|---|---|---|---|
| Teknis | 25% | Semua benar + edge cases | Benar kasus utama | Beberapa salah | Banyak salah |
| Problem Solving | 30% | Efisien + dekomposisi jelas | Tepat + cukup baik | Kurang efisien | Tidak tepat |
| Kode Python | 25% | PEP 8 penuh + clean code | Sebagian besar PEP 8 | Beberapa pelanggaran | Tidak PEP 8 |
| Dokumentasi | 20% | Lengkap + AI Log detail | Cukup lengkap | Minim | Tidak ada |

**Formula Nilai Tugas:**
```
Nilai Tugas = ((Teknis/4 * 25) + (ProbSolving/4 * 30) + (Kode/4 * 25) + (Dokumentasi/4 * 20))
```

---

## 2. Detail Rubrik per Tugas

### T1: Variabel, Tipe Data, dan Operasi I/O (Minggu 3)

**Deskripsi:** Buat program kalkulator konversi satuan (suhu, panjang, berat) dengan menu interaktif.

**CPMK:** CPMK-1, CPMK-2

| Dimensi | Kriteria Spesifik T1 |
|---|---|
| **Teknis** | Konversi menghasilkan nilai yang tepat. Semua satuan berfungsi. Format output rapi (2 desimal). Type casting benar. |
| **Problem Solving** | Pemilihan rumus konversi tepat. Alur menu logis. Penggunaan variabel efisien. |
| **Kode Python** | Penggunaan tipe data yang tepat (float untuk desimal). Penamaan variabel deskriptif. f-string untuk output. |
| **Dokumentasi** | Header komentar (nama, NIM, deskripsi). Komentar pada rumus konversi. AI Usage Log. |

**Contoh Soal T1:**
Buat program yang meminta pengguna memasukkan suhu dalam Celsius, lalu menampilkan konversi ke Fahrenheit, Kelvin, dan Reamur. Program juga harus menampilkan kategori suhu: "Sangat Dingin" (< 0), "Dingin" (0-15), "Sejuk" (16-24), "Hangat" (25-32), "Panas" (> 32).

---

### T2: Percabangan dan Logika (Minggu 5)

**Deskripsi:** Buat program penentuan tarif parkir berdasarkan jenis kendaraan, durasi, dan hari (weekday/weekend).

**CPMK:** CPMK-2, CPMK-3

| Dimensi | Kriteria Spesifik T2 |
|---|---|
| **Teknis** | Tarif dihitung benar untuk semua kombinasi (motor/mobil, durasi, weekday/weekend). Edge cases: durasi 0, durasi negatif. |
| **Problem Solving** | Struktur if-elif-else efisien, tidak redundan. Logika tarif progresif (jika ada) benar. |
| **Kode Python** | Nested if terstruktur dan readable. Operator logika (`and`, `or`) digunakan tepat. Konstanta untuk tarif dasar. |
| **Dokumentasi** | Tabel tarif dicantumkan di komentar. Alur logika dijelaskan. AI Usage Log. |

**Contoh Soal T2:**
Buat program tarif parkir: Motor (Rp2.000/jam pertama, Rp1.000/jam berikutnya), Mobil (Rp5.000/jam pertama, Rp3.000/jam berikutnya). Weekend: tarif naik 50%. Maksimal tarif harian: Motor Rp15.000, Mobil Rp40.000.

---

### T3: Perulangan dan Pola (Minggu 6)

**Deskripsi:** Buat program yang menghasilkan pola-pola bintang/angka dan menghitung deret matematika.

**CPMK:** CPMK-2, CPMK-3

| Dimensi | Kriteria Spesifik T3 |
|---|---|
| **Teknis** | Semua pola ditampilkan benar sesuai spesifikasi. Deret dihitung tepat. Jumlah baris sesuai input pengguna. |
| **Problem Solving** | Nested loop digunakan efisien. Pola dianalisis dengan tepat (hubungan baris-kolom). Tidak ada hardcode. |
| **Kode Python** | Penggunaan `range()` tepat. Nested loop rapi. `end=""` dan `print()` digunakan benar untuk format output. |
| **Dokumentasi** | Contoh output dicantumkan di komentar untuk setiap pola. AI Usage Log. |

**Contoh Soal T3:**
Buat program yang menampilkan 4 pola berikut berdasarkan input n dari pengguna:
```
Pola 1:        Pola 2:        Pola 3:        Pola 4:
*              *****          1              A
**             ****           12             AB
***            ***            123            ABC
****           **             1234           ABCD
*****          *              12345          ABCDE
```

---

### T4: Fungsi dan Modularitas (Minggu 8)

**Deskripsi:** Refactor program kalkulator sederhana menjadi modular dengan fungsi-fungsi terpisah.

**CPMK:** CPMK-3, CPMK-4

| Dimensi | Kriteria Spesifik T4 |
|---|---|
| **Teknis** | Semua operasi menghasilkan hasil benar. Division by zero ditangani. Fungsi dipanggil dan mengembalikan nilai tepat. |
| **Problem Solving** | Dekomposisi masalah ke fungsi-fungsi tepat. Setiap fungsi memiliki tanggung jawab tunggal. Parameter dan return value dirancang logis. |
| **Kode Python** | Docstring pada setiap fungsi. Parameter memiliki type hints (opsional). Tidak ada variabel global yang tidak perlu. Scope variabel benar. |
| **Dokumentasi** | Docstring lengkap (deskripsi, args, returns). Contoh penggunaan fungsi di komentar. AI Usage Log. |

**Contoh Soal T4:**
Buat kalkulator ilmiah sederhana dengan fungsi-fungsi berikut:
- `tambah(a, b)`, `kurang(a, b)`, `kali(a, b)`, `bagi(a, b)`
- `pangkat(base, exp)`, `akar(n)`, `faktorial(n)`
- `tampilkan_menu()`, `validasi_input(teks)`
- `main()` yang mengelola loop menu utama
Semua fungsi harus memiliki docstring dan error handling.

---

### T5: Struktur Data -- List, Dictionary, Set (Minggu 11)

**Deskripsi:** Buat program pengelola data mahasiswa menggunakan list, dictionary, dan set.

**CPMK:** CPMK-4, CPMK-5

| Dimensi | Kriteria Spesifik T5 |
|---|---|
| **Teknis** | CRUD (Create, Read, Update, Delete) berfungsi benar. Data konsisten antar struktur data. Pencarian menghasilkan hasil tepat. |
| **Problem Solving** | Pemilihan struktur data tepat untuk setiap kebutuhan. Dictionary untuk data terstruktur, set untuk data unik, list untuk koleksi terurut. |
| **Kode Python** | Method list/dict/set digunakan tepat (`.append()`, `.get()`, `.add()`, `.items()`). Comprehension digunakan jika sesuai. |
| **Dokumentasi** | Penjelasan alasan pemilihan struktur data. Contoh penggunaan setiap operasi. AI Usage Log. |

**Contoh Soal T5:**
Buat program data mahasiswa yang menyimpan: nama (str), NIM (str), mata kuliah yang diambil (list), dan nilai (dict: {mata_kuliah: nilai}). Program harus bisa:
- Tambah/hapus mahasiswa
- Tambah mata kuliah dan nilai
- Cari mahasiswa berdasarkan NIM
- Tampilkan mahasiswa dengan IPK tertinggi
- Tampilkan set mata kuliah unik yang diambil seluruh mahasiswa

---

### T6: Algoritma Searching, Sorting, dan Rekursi (Minggu 13)

**Deskripsi:** Implementasikan algoritma searching dan sorting, serta fungsi rekursif untuk masalah tertentu.

**CPMK:** CPMK-5, CPMK-6

| Dimensi | Kriteria Spesifik T6 |
|---|---|
| **Teknis** | Algoritma searching menemukan elemen yang benar (atau mengembalikan "tidak ditemukan"). Sorting menghasilkan urutan yang tepat. Fungsi rekursif mengembalikan hasil benar. |
| **Problem Solving** | Pemilihan algoritma tepat untuk skenario. Implementasi efisien. Analisis Big-O dicantumkan. Base case dan recursive case pada rekursi tepat. |
| **Kode Python** | Implementasi algoritma sesuai pseudocode standar. Variabel lokal digunakan (bukan global). Fungsi rekursif clean dan benar. |
| **Dokumentasi** | Analisis Big-O untuk setiap algoritma dicantumkan. Perbandingan performa (jika ada). Langkah-langkah algoritma dijelaskan. AI Usage Log. |

**Contoh Soal T6:**
Buat program yang:
1. Mengimplementasikan **linear search** dan **binary search** untuk mencari nama mahasiswa
2. Mengimplementasikan **bubble sort** dan **selection sort** untuk mengurutkan data berdasarkan nilai
3. Mengimplementasikan fungsi rekursif **fibonacci(n)** dan **pangkat(base, exp)**
4. Membandingkan jumlah operasi linear search vs binary search pada data 100 elemen
5. Mencantumkan analisis Big-O untuk setiap algoritma di komentar

---

## 3. Ketentuan Pengumpulan

### 3.1 Deadline dan Format

| Aspek | Ketentuan |
|---|---|
| **Deadline** | Setiap tugas memiliki deadline pada hari Jumat, pukul 23:59 WIB, di minggu yang ditentukan |
| **Format File** | File `.py` (Python script) ATAU link Google Colab (pastikan sharing diaktifkan) |
| **Penamaan File** | `T[nomor]_NIM_NamaDepan.py` (contoh: `T1_2025001_Andi.py`) |
| **Platform** | Upload melalui LMS (Learning Management System) UAI |
| **Isi Submission** | File `.py` + AI Usage Log (dalam komentar di kode atau file terpisah) |

### 3.2 Keterlambatan (Late Penalty)

| Keterlambatan | Penalti |
|---|---|
| Tepat waktu | Tidak ada penalti |
| Terlambat 1 hari (Sabtu) | -10% dari nilai yang didapat |
| Terlambat 2 hari (Minggu) | -20% dari nilai yang didapat |
| Terlambat 3 hari (Senin) | -30% dari nilai yang didapat |
| Terlambat > 3 hari | Tidak diterima (nilai 0) |

**Contoh:** Jika nilai asli tugas = 80 dan terlambat 1 hari:
```
Nilai akhir = 80 - (80 x 10%) = 80 - 8 = 72
```

### 3.3 Pengumpulan Ulang

- Mahasiswa boleh mengumpulkan ulang **sebelum deadline** (versi terakhir yang dihitung)
- Setelah deadline, revisi tidak diterima (kecuali mekanisme remedial di assessment-framework)

---

## 4. Kebijakan AI (AI Policy) untuk Tugas

### 4.1 Prinsip Utama

AI (seperti ChatGPT, GitHub Copilot, Gemini, Claude, dll.) **diperbolehkan** untuk tugas T1-T6 dengan ketentuan berikut:

| Diperbolehkan | Tidak Diperbolehkan |
|---|---|
| Bertanya konsep pemrograman | Copy-paste seluruh solusi dari AI |
| Meminta penjelasan error message | Menyalin kode AI tanpa memahami |
| Brainstorm pendekatan solusi | Mengklaim kode AI sebagai karya sendiri tanpa log |
| Debugging dengan bantuan AI | Menggunakan AI untuk tugas yang mengharuskan pemahaman manual |
| Meminta review kode yang sudah ditulis sendiri | Meminta AI menulis seluruh program dari awal sampai akhir |
| Belajar sintaks atau method baru | |

### 4.2 AI Usage Log untuk Tugas

Setiap tugas **wajib** menyertakan AI Usage Log. Log dapat ditulis sebagai:
- Komentar multi-baris di akhir file `.py`, ATAU
- File terpisah `T[nomor]_NIM_AILog.txt`

**Format Minimal AI Usage Log untuk Tugas:**

```python
"""
AI USAGE LOG - Tugas [Nomor]
Nama: [Nama Lengkap]
NIM: [NIM]

1. AI Tool: [Nama AI]
   Tujuan: [Apa yang ditanyakan]
   Hasil: [Ringkasan jawaban AI]
   Modifikasi: [Apa yang diubah/ditambahkan sendiri]

2. [Interaksi berikutnya jika ada]

Jika tidak menggunakan AI:
"Saya tidak menggunakan AI untuk tugas ini.
Sumber belajar: [sebutkan sumber]"
"""
```

### 4.3 Sanksi Terkait AI

| Pelanggaran | Sanksi |
|---|---|
| Tugas tanpa AI Usage Log | Pengurangan **30%** dari nilai tugas |
| Terdeteksi copy-paste AI tanpa pemahaman (saat ditanya di kelas) | Nilai **0** untuk tugas tersebut |
| Plagiarisme antar mahasiswa (termasuk berbagi output AI) | Nilai **0** untuk semua pihak yang terlibat |

---

## 5. Contoh Perhitungan Nilai Tugas

### Contoh 1: T3 (Perulangan dan Pola)

| Dimensi | Skor (1-4) | Bobot | Kontribusi |
|---|---|---|---|
| Teknis | 4 | 25% | 25.00 |
| Problem Solving | 3 | 30% | 22.50 |
| Kode Python | 3 | 25% | 18.75 |
| Dokumentasi | 4 | 20% | 20.00 |
| **Total** | | **100%** | **86.25** |

Nilai T3 = **86.25** (A)

### Contoh 2: T5 (Struktur Data) -- dengan keterlambatan

| Dimensi | Skor (1-4) | Bobot | Kontribusi |
|---|---|---|---|
| Teknis | 3 | 25% | 18.75 |
| Problem Solving | 3 | 30% | 22.50 |
| Kode Python | 2 | 25% | 12.50 |
| Dokumentasi | 2 | 20% | 10.00 |
| **Total sebelum penalti** | | | **63.75** |
| **Penalti terlambat 1 hari** | | -10% | **-6.375** |
| **Total akhir** | | | **57.375** |

Nilai T5 = **57.38** (C) -- setelah penalti keterlambatan

### Contoh 3: T4 (Fungsi) -- tanpa AI Usage Log

| Dimensi | Skor (1-4) | Bobot | Kontribusi |
|---|---|---|---|
| Teknis | 4 | 25% | 25.00 |
| Problem Solving | 4 | 30% | 30.00 |
| Kode Python | 4 | 25% | 25.00 |
| Dokumentasi | 1 (tanpa AI Log) | 20% | 5.00 |
| **Total sebelum penalti AI** | | | **85.00** |
| **Penalti tanpa AI Log** | | -30% | **-25.50** |
| **Total akhir** | | | **59.50** |

Nilai T4 = **59.50** (C) -- meskipun kode sangat baik, tidak ada AI Usage Log menyebabkan penurunan signifikan

---

## 6. Perhitungan Nilai Rata-rata Tugas

Nilai akhir komponen tugas (bobot 15% dari nilai akhir) dihitung sebagai **rata-rata dari T1 sampai T6**:

```
Nilai Tugas = (T1 + T2 + T3 + T4 + T5 + T6) / 6
```

**Contoh:**

| Tugas | Nilai |
|---|---|
| T1 | 80 |
| T2 | 75 |
| T3 | 86.25 |
| T4 | 59.50 |
| T5 | 57.38 |
| T6 | 90 |
| **Rata-rata** | **74.69** |

Kontribusi tugas terhadap nilai akhir = 74.69 x 15% = **11.20 poin**

---

## 7. Checklist Pengumpulan Tugas

Sebelum mengumpulkan setiap tugas, pastikan:

- [ ] Program berjalan tanpa error (`python T[nomor]_NIM_Nama.py`)
- [ ] Semua fitur yang diminta sudah diimplementasikan
- [ ] Output sesuai format yang diminta
- [ ] Edge cases ditangani (input kosong, angka negatif, dll.)
- [ ] Nama file sesuai format: `T[nomor]_NIM_NamaDepan.py`
- [ ] Header komentar: nama, NIM, deskripsi tugas
- [ ] Komentar pada bagian kode yang penting
- [ ] Penamaan variabel bermakna (snake_case)
- [ ] Indentasi konsisten (4 spasi)
- [ ] AI Usage Log terisi (atau pernyataan tidak menggunakan AI)
- [ ] Program sudah ditest dengan berbagai input
- [ ] Upload ke LMS sebelum deadline (Jumat 23:59 WIB)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
