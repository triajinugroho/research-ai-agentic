# Panduan Proyek Akhir -- Algoritma dan Pemrograman

> **Mata Kuliah:** Algoritma dan Pemrograman (3 SKS)
> **Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.
> **Program Studi:** Informatika, Universitas Al Azhar Indonesia
> **Semester:** Genap 2025/2026
> **Bahasa Pemrograman:** Python

---

## 1. Deskripsi Proyek

Proyek akhir merupakan asesmen autentik utama yang mengintegrasikan seluruh capaian pembelajaran mata kuliah Algoritma dan Pemrograman. Mahasiswa diminta membangun **aplikasi Python yang lengkap dan fungsional** untuk menyelesaikan masalah dunia nyata.

Proyek dapat dikerjakan secara **individu** atau **berpasangan (maksimal 2 orang)**. Untuk proyek berpasangan, kedua anggota harus berkontribusi secara setara dan mendokumentasikan pembagian tugas secara jelas.

**Bobot Proyek terhadap Nilai Akhir: 25%**

---

## 2. Tujuan Proyek

Melalui proyek akhir, mahasiswa diharapkan mampu:

1. **Mengintegrasikan seluruh konsep** yang telah dipelajari (variabel, seleksi, perulangan, fungsi, struktur data, algoritma)
2. **Merancang solusi** untuk masalah nyata menggunakan pendekatan computational thinking
3. **Mengimplementasikan program modular** dengan fungsi-fungsi yang terorganisir
4. **Menggunakan struktur data** yang tepat (list, dictionary, set/tuple)
5. **Menerapkan algoritma** searching dan/atau sorting dalam konteks nyata
6. **Mengelola data** melalui file I/O (save/load)
7. **Menulis kode bersih** sesuai standar PEP 8
8. **Menggunakan AI secara etis** dan mendokumentasikan penggunaannya
9. **Mempresentasikan** hasil kerja secara profesional

---

## 3. Syarat Teknis

Setiap proyek **wajib** memenuhi syarat teknis minimum berikut:

### 3.1 Persyaratan Wajib

| No | Syarat | Keterangan |
|---|---|---|
| 1 | **Minimal 5 fungsi** | Termasuk fungsi utama (`main()`), fungsi input, fungsi proses, fungsi output, dan minimal 1 fungsi tambahan |
| 2 | **Minimal 3 struktur data berbeda** | Kombinasi dari: list, dictionary, set, dan/atau tuple |
| 3 | **Minimal 1 algoritma searching/sorting** | Linear search, binary search, bubble sort, selection sort, atau insertion sort |
| 4 | **File I/O** | Program dapat menyimpan (save) dan memuat (load) data dari/ke file (TXT, CSV, atau JSON) |
| 5 | **Error handling** | Menggunakan `try-except` minimal untuk validasi input pengguna |
| 6 | **PEP 8 compliance** | Penamaan variabel snake_case, indentasi 4 spasi, baris maksimal 79 karakter |
| 7 | **Komentar dan docstrings** | Setiap fungsi memiliki docstring, komentar pada bagian kode yang kompleks |

### 3.2 Persyaratan Tambahan (Nilai Plus)

| Fitur Tambahan | Keterangan |
|---|---|
| Menu interaktif | Program memiliki menu pilihan untuk navigasi fitur |
| Rekursi | Menggunakan fungsi rekursif untuk masalah yang sesuai |
| Multiple files | Kode diorganisir dalam beberapa file Python (modul) |
| Visualisasi teks | Tampilan tabel atau grafik sederhana di terminal |
| Unit testing | Fungsi-fungsi diuji dengan test sederhana |

---

## 4. Timeline Proyek

| Tahap | Minggu | Deliverable | Bobot | Deadline |
|---|---|---|---|---|
| **Proposal** | 9 | Dokumen proposal 1 halaman | 5% | Jumat, Minggu 9, 23:59 WIB |
| **Progress Report** | 12 | Laporan kemajuan + Demo 50% kode berjalan | 10% | Jumat, Minggu 12, 23:59 WIB |
| **Final Submission** | 14 | Source code lengkap + Dokumentasi + AI Usage Log | 60% | Jumat, Minggu 14, 23:59 WIB |
| **Presentasi** | 15 | Presentasi 10 menit + Demo 5 menit + Tanya Jawab 5 menit | 25% | Sesuai jadwal yang ditentukan |

### Detail per Tahap

**Minggu 9 -- Proposal:**
- Isi proposal sesuai template (lihat Bagian 6)
- Persetujuan dosen diperlukan sebelum mulai implementasi
- Jika proposal ditolak, revisi harus dikumpulkan dalam 3 hari kerja

**Minggu 12 -- Progress Report:**
- Demo minimal 50% fungsionalitas program
- Laporan tertulis mencakup: progres, hambatan, rencana penyelesaian
- Dosen memberikan umpan balik untuk perbaikan

**Minggu 14 -- Final Submission:**
- Submit melalui LMS UAI dalam format ZIP
- Isi ZIP: seluruh file `.py`, file data, `README.md`, AI Usage Log
- Program harus bisa dijalankan tanpa error saat di-extract

**Minggu 15 -- Presentasi:**
- 10 menit presentasi (latar belakang, fitur, struktur kode, AI usage)
- 5 menit demo live (jalankan program, tunjukkan fitur utama)
- 5 menit tanya jawab (dosen dan mahasiswa lain)
- Untuk proyek berpasangan, kedua anggota HARUS presentasi dan menjawab pertanyaan

---

## 5. Contoh Topik Proyek

Berikut 10 contoh topik proyek yang menggunakan konteks Indonesia. Mahasiswa bebas mengusulkan topik lain selama memenuhi syarat teknis.

| No | Topik | Deskripsi | Struktur Data | Algoritma |
|---|---|---|---|---|
| 1 | **Sistem Perpustakaan Mini** | Kelola data buku: tambah, hapus, cari, pinjam, kembalikan. Data disimpan ke file | dict, list, tuple | Linear/binary search |
| 2 | **Kasir Warung Kelontong** | Input barang belanja, hitung total, diskon, cetak struk. Kelola stok barang | dict, list, set | Sorting (harga), searching |
| 3 | **Tebak Kata (Hangman)** | Game tebak kata berbahasa Indonesia. Skor disimpan, leaderboard | list, set, dict | Linear search, sorting |
| 4 | **Antrian Rumah Sakit** | Sistem antrian pasien dengan prioritas. Kelola data pasien dan riwayat | list, dict, tuple | Sorting (prioritas), searching |
| 5 | **Text Analyzer** | Analisis teks: frekuensi kata, kata terpanjang, statistik. Baca dari file | dict, list, set | Sorting (frekuensi), searching |
| 6 | **Buku Telepon Digital** | CRUD kontak, cari berdasarkan nama/nomor, ekspor ke file CSV | dict, list, tuple | Binary search, sorting (nama) |
| 7 | **Kalkulator IPK** | Input mata kuliah, SKS, nilai. Hitung IPK semester dan kumulatif. Simpan riwayat | dict, list, tuple | Sorting (nilai), searching |
| 8 | **Menu Kantin UAI** | Kelola menu makanan, pesan, hitung total, rekomendasi berdasarkan budget | dict, list, set | Sorting (harga), searching |
| 9 | **E-Polling Sederhana** | Buat polling, vote, lihat hasil real-time, grafik teks, ekspor hasil | dict, list, set | Sorting (suara), searching |
| 10 | **Quiz App** | Bank soal dari file, kuis acak, skor, leaderboard, statistik per topik | dict, list, tuple | Sorting (skor), searching |

---

## 6. Template Proposal

```
====================================================
PROPOSAL PROYEK AKHIR
Algoritma dan Pemrograman -- Semester Genap 2025/2026
====================================================

Judul Proyek    : [Judul proyek Anda]
Nama / NIM      : [Nama lengkap / NIM]
                  [Nama lengkap / NIM (jika berpasangan)]
Tanggal         : [Tanggal pengumpulan]

1. DESKRIPSI MASALAH
   [Jelaskan masalah dunia nyata yang ingin diselesaikan
    dalam 3-5 kalimat]

2. TUJUAN PROGRAM
   - [Tujuan 1]
   - [Tujuan 2]
   - [Tujuan 3]

3. FITUR UTAMA
   - [Fitur 1: deskripsi singkat]
   - [Fitur 2: deskripsi singkat]
   - [Fitur 3: deskripsi singkat]
   - [Fitur 4: deskripsi singkat]
   - [Fitur 5: deskripsi singkat]

4. RENCANA STRUKTUR DATA & ALGORITMA
   Struktur Data: [list, dict, set/tuple -- jelaskan penggunaannya]
   Algoritma    : [searching/sorting -- jelaskan konteks penggunaannya]

5. RENCANA FUNGSI (minimal 5)
   - main()           : [deskripsi singkat]
   - [nama_fungsi_2](): [deskripsi singkat]
   - [nama_fungsi_3](): [deskripsi singkat]
   - [nama_fungsi_4](): [deskripsi singkat]
   - [nama_fungsi_5](): [deskripsi singkat]

6. RENCANA FILE I/O
   Format file   : [TXT / CSV / JSON]
   Data yang disimpan: [jelaskan data apa yang akan di-save/load]

7. PEMBAGIAN TUGAS (jika berpasangan)
   [Nama 1]: [tugas yang dikerjakan]
   [Nama 2]: [tugas yang dikerjakan]

====================================================
```

---

## 7. Rubrik Penilaian Proyek -- 8 Komponen

### Komponen 1: Perumusan Masalah & Desain (10%)

| Skor | Level | Deskripsi |
|---|---|---|
| 4 | Sangat Baik | Masalah teridentifikasi jelas, solusi dirancang sistematis dengan CT, desain modular lengkap dengan flowchart/pseudocode |
| 3 | Baik | Masalah cukup jelas, desain solusi terstruktur, ada perencanaan fungsi yang memadai |
| 2 | Cukup | Masalah kurang spesifik, desain solusi sederhana, perencanaan minimal |
| 1 | Kurang | Masalah tidak jelas, tidak ada desain/perencanaan yang terlihat |

### Komponen 2: Implementasi Kode & Fungsi (20%)

| Skor | Level | Deskripsi |
|---|---|---|
| 4 | Sangat Baik | Minimal 5 fungsi bermakna, modularitas sangat baik, setiap fungsi memiliki tanggung jawab tunggal (SRP), parameter dan return value tepat |
| 3 | Baik | 5 fungsi atau lebih, modularitas baik, sebagian besar fungsi terstruktur dengan tepat |
| 2 | Cukup | 3-4 fungsi, modularitas kurang, beberapa fungsi terlalu panjang atau tidak fokus |
| 1 | Kurang | Kurang dari 3 fungsi, kode tidak modular, sebagian besar kode di luar fungsi |

### Komponen 3: Penggunaan Struktur Data & Algoritma (15%)

| Skor | Level | Deskripsi |
|---|---|---|
| 4 | Sangat Baik | Minimal 3 struktur data berbeda digunakan tepat, algoritma searching/sorting diimplementasikan dan relevan dengan masalah |
| 3 | Baik | 3 struktur data digunakan, algoritma diimplementasikan dengan benar |
| 2 | Cukup | 2 struktur data, algoritma ada tapi kurang tepat penggunaannya |
| 1 | Kurang | Hanya 1 struktur data, tidak ada algoritma searching/sorting |

### Komponen 4: Penanganan Error & Edge Cases (10%)

| Skor | Level | Deskripsi |
|---|---|---|
| 4 | Sangat Baik | try-except pada semua input pengguna, validasi input komprehensif, program tidak crash pada edge cases, pesan error informatif |
| 3 | Baik | try-except pada input utama, validasi cukup baik, program stabil |
| 2 | Cukup | try-except minimal, beberapa input tidak divalidasi, program kadang crash |
| 1 | Kurang | Tidak ada error handling, program mudah crash pada input tidak valid |

### Komponen 5: Dokumentasi Kode (10%)

| Skor | Level | Deskripsi |
|---|---|---|
| 4 | Sangat Baik | Setiap fungsi memiliki docstring lengkap (deskripsi, parameter, return), komentar informatif pada bagian kompleks, PEP 8 penuh, README lengkap |
| 3 | Baik | Sebagian besar fungsi memiliki docstring, komentar cukup, PEP 8 sebagian besar diikuti |
| 2 | Cukup | Beberapa docstring ada, komentar minim, beberapa pelanggaran PEP 8 |
| 1 | Kurang | Tidak ada docstring, tidak ada komentar bermakna, PEP 8 tidak diikuti |

### Komponen 6: Dokumentasi AI Usage (15%)

| Skor | Level | Deskripsi |
|---|---|---|
| 4 | Sangat Baik | AI Usage Log lengkap dan detail: setiap interaksi dicatat (prompt, respons AI, modifikasi, refleksi). Mahasiswa menunjukkan pemahaman kritis terhadap output AI |
| 3 | Baik | AI Usage Log cukup lengkap, sebagian besar interaksi didokumentasikan, ada refleksi |
| 2 | Cukup | AI Usage Log ada tapi tidak detail, beberapa interaksi tidak dicatat |
| 1 | Kurang | AI Usage Log tidak ada atau sangat minim / Mengklaim tidak menggunakan AI sama sekali tanpa bukti yang meyakinkan |

**Catatan:** Jika mahasiswa benar-benar tidak menggunakan AI, tuliskan pernyataan tersebut secara eksplisit dalam AI Usage Log dengan penjelasan pendekatan belajar yang digunakan.

### Komponen 7: Presentasi & Demo (15%)

| Skor | Level | Deskripsi |
|---|---|---|
| 4 | Sangat Baik | Presentasi terstruktur dan jelas, demo berjalan lancar tanpa error, mampu menjawab semua pertanyaan dengan mendalam, menunjukkan penguasaan penuh terhadap kode |
| 3 | Baik | Presentasi cukup terstruktur, demo berjalan dengan minor issue, mampu menjawab sebagian besar pertanyaan |
| 2 | Cukup | Presentasi kurang terstruktur, demo ada error, kesulitan menjawab beberapa pertanyaan |
| 1 | Kurang | Presentasi tidak terstruktur, demo gagal, tidak mampu menjawab pertanyaan tentang kode sendiri |

### Komponen 8: Etika & Integritas (5%)

| Skor | Level | Deskripsi |
|---|---|---|
| 4 | Sangat Baik | Integritas akademik terjaga, penggunaan AI sesuai kebijakan, tidak ada plagiarisme, kontribusi setara (jika berpasangan) |
| 3 | Baik | Integritas baik, penggunaan AI sebagian besar sesuai kebijakan |
| 2 | Cukup | Ada indikasi minor ketidaksesuaian penggunaan AI, kontribusi kurang setara |
| 1 | Kurang | Ada indikasi plagiarisme atau pelanggaran kebijakan AI yang signifikan |

### Tabel Ringkasan Bobot Komponen

| No | Komponen | Bobot | Skor Maks |
|---|---|---|---|
| 1 | Perumusan Masalah & Desain | 10% | 4 |
| 2 | Implementasi Kode & Fungsi | 20% | 4 |
| 3 | Penggunaan Struktur Data & Algoritma | 15% | 4 |
| 4 | Penanganan Error & Edge Cases | 10% | 4 |
| 5 | Dokumentasi Kode | 10% | 4 |
| 6 | Dokumentasi AI Usage | 15% | 4 |
| 7 | Presentasi & Demo | 15% | 4 |
| 8 | Etika & Integritas | 5% | 4 |
| | **Total** | **100%** | |

**Formula Nilai Proyek:**
```
Nilai Proyek = Sum(Skor_Komponen_i / 4 * Bobot_i) * 100
```

---

## 8. Template AI Usage Log

```
====================================================
AI USAGE LOG -- PROYEK AKHIR
Algoritma dan Pemrograman -- Semester Genap 2025/2026
====================================================

Nama / NIM    : [Nama lengkap / NIM]
Judul Proyek  : [Judul proyek]
AI Tool       : [Nama AI yang digunakan, misal: ChatGPT, GitHub Copilot, dll.]

----------------------------------------------------
INTERAKSI #1
----------------------------------------------------
Tanggal       : [DD/MM/YYYY]
Tujuan        : [Apa yang ingin dicapai? Misal: brainstorm fitur, debug error, dll.]
Prompt        : [Tulis prompt yang diberikan ke AI]
Respons AI    : [Ringkasan respons AI, atau screenshot]
Modifikasi    : [Apa yang Anda ubah dari output AI? Mengapa?]
Refleksi      : [Apa yang Anda pelajari dari interaksi ini?]
Kode Terkait  : [Baris/fungsi mana yang terpengaruh?]

----------------------------------------------------
INTERAKSI #2
----------------------------------------------------
Tanggal       : [DD/MM/YYYY]
Tujuan        : [...]
Prompt        : [...]
Respons AI    : [...]
Modifikasi    : [...]
Refleksi      : [...]
Kode Terkait  : [...]

[Tambahkan interaksi berikutnya sesuai kebutuhan]

----------------------------------------------------
RINGKASAN PENGGUNAAN AI
----------------------------------------------------
Total Interaksi     : [Jumlah]
AI untuk Brainstorm : [Jumlah] interaksi
AI untuk Debugging  : [Jumlah] interaksi
AI untuk Refactoring: [Jumlah] interaksi
AI untuk Lainnya    : [Jumlah] interaksi

Persentase kode yang dipengaruhi AI: [estimasi %]
Pernyataan: Saya memahami seluruh kode dalam proyek ini
            dan dapat menjelaskan setiap baris jika diminta.

Tanda Tangan: [Nama lengkap]
Tanggal     : [DD/MM/YYYY]

====================================================
```

---

## 9. Template README Proyek

```markdown
# [Judul Proyek]

## Deskripsi
[Jelaskan proyek dalam 2-3 kalimat]

## Fitur
- [Fitur 1]
- [Fitur 2]
- [Fitur 3]
- [Fitur 4]
- [Fitur 5]

## Cara Menjalankan
1. Pastikan Python 3.x sudah terinstal
2. Download/extract seluruh file
3. Jalankan: `python main.py`

## Struktur File
```
nama_proyek/
|-- main.py           # Program utama
|-- [modul].py        # [Deskripsi modul]
|-- data/             # Folder data
|   |-- [file].csv    # [Deskripsi file data]
|-- README.md         # Dokumentasi proyek
|-- ai_usage_log.md   # Log penggunaan AI
```

## Struktur Data yang Digunakan
- **List**: [untuk apa]
- **Dictionary**: [untuk apa]
- **Set/Tuple**: [untuk apa]

## Algoritma yang Digunakan
- **[Nama Algoritma]**: [untuk apa, di fungsi mana]

## Daftar Fungsi
| Fungsi | Parameter | Return | Deskripsi |
|---|---|---|---|
| main() | - | - | Fungsi utama program |
| [fungsi_2]() | [param] | [return] | [deskripsi] |
| [fungsi_3]() | [param] | [return] | [deskripsi] |

## Contoh Penggunaan
[Screenshot atau contoh output program]

## Pembuat
- [Nama / NIM]
- [Nama / NIM (jika berpasangan)]

## Mata Kuliah
Algoritma dan Pemrograman -- Semester Genap 2025/2026
Dosen: Tri Aji Nugroho, S.T., M.T.
Program Studi Informatika, Universitas Al Azhar Indonesia
```

---

## 10. FAQ (Frequently Asked Questions)

**Q1: Bolehkah menggunakan library eksternal (pip install)?**
A: Tidak. Proyek hanya boleh menggunakan library bawaan Python (built-in modules). Contoh yang diperbolehkan: `os`, `json`, `csv`, `random`, `datetime`. Library seperti `pandas`, `numpy`, `flask` tidak diperbolehkan.

**Q2: Bolehkah proyek berbasis GUI (Tkinter)?**
A: Proyek harus berbasis terminal/console (CLI). Jika ingin menambahkan GUI sebagai fitur bonus, boleh, tetapi fungsionalitas utama harus tetap berjalan di terminal.

**Q3: Bagaimana jika saya benar-benar tidak menggunakan AI?**
A: Tulis pernyataan eksplisit dalam AI Usage Log bahwa Anda tidak menggunakan AI, beserta penjelasan sumber belajar yang Anda gunakan (buku, video, dokumentasi Python, diskusi teman). Anda tidak akan dihukum karena tidak menggunakan AI.

**Q4: Berapa panjang minimal kode program?**
A: Tidak ada batas panjang minimal. Yang dinilai adalah kualitas, bukan kuantitas. Namun, program yang memenuhi seluruh syarat teknis biasanya memiliki 200-500 baris kode.

**Q5: Bagaimana jika partner saya tidak berkontribusi?**
A: Laporkan ke dosen pengampu paling lambat Minggu 12 (saat progress report). Dosen dapat memutuskan pembagian nilai yang berbeda atau memisahkan proyek menjadi individu.

**Q6: Apakah boleh mengambil inspirasi dari tutorial YouTube atau blog?**
A: Boleh mengambil inspirasi, tetapi kode harus ditulis sendiri dan disesuaikan dengan kebutuhan proyek. Jika mengadaptasi kode dari sumber tertentu, cantumkan referensi di komentar kode. Copy-paste seluruh proyek dari tutorial = plagiarisme.

**Q7: Bagaimana format pengumpulan?**
A: Kumpulkan dalam format ZIP melalui LMS UAI. Nama file: `ProyekAkhir_NIM_NamaDepan.zip`. Untuk proyek berpasangan: `ProyekAkhir_NIM1_NIM2.zip`. Pastikan file dapat di-extract dan dijalankan langsung.

**Q8: Apakah ada presentasi susulan?**
A: Presentasi susulan hanya diberikan dengan alasan resmi (surat sakit/izin dari institusi). Presentasi susulan dilakukan paling lambat 1 minggu setelah jadwal asal, dengan nilai maksimal B+ (79).

**Q9: Bagaimana jika program saya error saat demo?**
A: Minor error yang bisa diperbaiki saat demo dimaklumi (pengurangan kecil di komponen presentasi). Jika program tidak bisa berjalan sama sekali, komponen presentasi dan demo akan mendapat skor rendah, tetapi komponen lain tetap dinilai berdasarkan source code.

**Q10: Bolehkah mengubah topik setelah proposal disetujui?**
A: Perubahan topik harus mendapat persetujuan dosen. Perubahan setelah Minggu 11 tidak diperbolehkan.

---

## 11. Checklist Pengumpulan

Sebelum mengumpulkan proyek, pastikan semua item berikut terpenuhi:

- [ ] Seluruh file `.py` ada dalam folder ZIP
- [ ] Program dapat dijalankan dengan `python main.py` tanpa error
- [ ] Minimal 5 fungsi dengan docstring
- [ ] Minimal 3 struktur data berbeda (list, dict, set/tuple)
- [ ] Minimal 1 algoritma searching/sorting
- [ ] File I/O berfungsi (save dan load)
- [ ] Error handling dengan try-except
- [ ] PEP 8 compliance
- [ ] README.md lengkap sesuai template
- [ ] AI Usage Log terisi (atau pernyataan tidak menggunakan AI)
- [ ] File data contoh disertakan
- [ ] Nama file ZIP sesuai format
- [ ] Tested: program berjalan di komputer lain / fresh environment

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
