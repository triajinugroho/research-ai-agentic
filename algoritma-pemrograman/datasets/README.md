# Panduan Resource dan Latihan Pemrograman

**Mata Kuliah:** Algoritma dan Pemrograman
**Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.
**Program Studi:** Informatika, Universitas Al Azhar Indonesia

Dokumen ini berisi kumpulan resource, platform latihan, contoh data, dan problem set
yang dirancang untuk mendukung pembelajaran pemrograman Python secara mandiri.

---

## 1. Platform Latihan Online

Berikut adalah platform yang direkomendasikan untuk berlatih pemrograman di luar jam kuliah:

| Platform       | URL                          | Fokus                          | Level                 | Gratis? |
|----------------|------------------------------|--------------------------------|-----------------------|---------|
| HackerRank     | hackerrank.com               | Python practice, algorithms    | Beginner-Advanced     | Ya      |
| LeetCode (Easy)| leetcode.com                 | Algorithm problems             | Beginner              | Sebagian|
| Replit         | replit.com                   | Online Python IDE              | Beginner              | Ya      |
| Exercism       | exercism.org                 | Python track                   | Beginner-Intermediate | Ya      |
| CodingBat      | codingbat.com                | Logic problems                 | Beginner              | Ya      |
| Advent of Code | adventofcode.com             | Annual programming puzzles     | Intermediate          | Ya      |
| Google Colab   | colab.research.google.com    | Notebook IDE                   | All levels            | Ya      |
| Kaggle         | kaggle.com                   | Notebooks, data, competitions  | Beginner-Advanced     | Ya      |

> **Tips:** Mulailah dari HackerRank atau CodingBat untuk membangun fondasi logika,
> kemudian gunakan Google Colab atau Replit sebagai IDE online untuk mengerjakan tugas kuliah.

---

## 2. Contoh File Data untuk Latihan File I/O

Berikut adalah contoh file CSV yang dapat dibuat atau di-copy-paste ke Google Colab
untuk latihan membaca, menulis, dan mengolah file menggunakan Python.

### a. `mahasiswa.csv` — Data Mahasiswa (10 baris)

```csv
NIM,Nama,Prodi,IPK
2024001,Aisyah Putri,Informatika,3.75
2024002,Budi Santoso,Informatika,3.50
2024003,Citra Dewi,Sistem Informasi,3.88
2024004,Dimas Prasetyo,Informatika,3.20
2024005,Eka Rahmawati,Sistem Informasi,3.65
2024006,Fajar Hidayat,Informatika,3.42
2024007,Gita Nuraini,Informatika,3.91
2024008,Hasan Abdullah,Sistem Informasi,3.10
2024009,Intan Permata,Informatika,3.78
2024010,Joko Widodo,Sistem Informasi,3.55
```

### b. `menu_kantin.csv` — Menu Kantin Kampus (15 baris)

```csv
Nama_Menu,Harga,Kategori
Nasi Goreng,15000,Makanan
Mie Ayam,13000,Makanan
Soto Betawi,18000,Makanan
Ayam Geprek,16000,Makanan
Gado-Gado,12000,Makanan
Nasi Uduk,10000,Makanan
Bakso,14000,Makanan
Nasi Padang,20000,Makanan
Es Teh Manis,5000,Minuman
Es Jeruk,6000,Minuman
Kopi Susu,10000,Minuman
Jus Alpukat,12000,Minuman
Air Mineral,4000,Minuman
Tahu Crispy,8000,Snack
Risoles,7000,Snack
```

### c. `buku_perpustakaan.csv` — Katalog Buku Perpustakaan (10 baris)

```csv
ISBN,Judul,Penulis,Tahun,Status
978-602-001,Pemrograman Python Dasar,Ahmad Fauzi,2022,Tersedia
978-602-002,Algoritma dan Struktur Data,Budi Raharjo,2021,Dipinjam
978-602-003,Basis Data Relasional,Candra Wijaya,2023,Tersedia
978-602-004,Jaringan Komputer,Dewi Sartika,2020,Tersedia
978-602-005,Kecerdasan Buatan,Eko Prasetyo,2023,Dipinjam
978-602-006,Sistem Operasi Modern,Fitri Handayani,2021,Tersedia
978-602-007,Pemrograman Web,Gunawan Saputra,2022,Dipinjam
978-602-008,Matematika Diskrit,Hendra Kusuma,2019,Tersedia
978-602-009,Rekayasa Perangkat Lunak,Irfan Maulana,2023,Tersedia
978-602-010,Statistika Komputasi,Joni Iskandar,2022,Dipinjam
```

### d. `transaksi.csv` — Data Transaksi Toko (20 baris)

```csv
Tanggal,Item,Qty,Harga
2025-01-02,Buku Tulis,3,8500
2025-01-02,Pensil 2B,5,3000
2025-01-03,Penghapus,2,2500
2025-01-03,Pulpen,4,5000
2025-01-04,Buku Gambar,1,15000
2025-01-05,Spidol,3,7000
2025-01-05,Kertas A4,2,45000
2025-01-06,Map Plastik,10,3500
2025-01-07,Stabilo,2,12000
2025-01-07,Tipe-X,1,8000
2025-01-08,Buku Tulis,6,8500
2025-01-09,Lem Kertas,3,6000
2025-01-10,Gunting,1,15000
2025-01-10,Penggaris,2,5500
2025-01-11,Rautan,4,3000
2025-01-12,Pensil Warna,1,35000
2025-01-13,Buku Tulis,2,8500
2025-01-14,Kertas A4,1,45000
2025-01-15,Pulpen,3,5000
2025-01-15,Spidol,2,7000
```

---

## 3. Problem Set Bertema Indonesia

Sepuluh tantangan pemrograman dengan konteks lokal Indonesia:

### 1. Hitung Pajak Progresif PPh 21
- **Deskripsi:** Buat program yang menghitung pajak penghasilan berdasarkan tarif progresif (5%, 15%, 25%, 30%, 35%) sesuai bracket penghasilan kena pajak tahunan.
- **Konsep:** Percabangan bertingkat (`if-elif-else`), operasi aritmatika, input/output.
- **Tingkat Kesulitan:** Mudah

### 2. Konversi Rupiah ke Mata Uang Asing (Multi-Currency)
- **Deskripsi:** Program konverter mata uang yang mendukung minimal 5 mata uang (USD, EUR, SGD, MYR, JPY) dengan kurs yang dapat diperbarui.
- **Konsep:** Dictionary, fungsi, loop menu, format angka.
- **Tingkat Kesulitan:** Mudah

### 3. Sistem Scoring UTBK/SNBT
- **Deskripsi:** Simulasi perhitungan skor UTBK dari beberapa subtes (Penalaran Umum, Pengetahuan Kuantitatif, dll.) dengan bobot masing-masing.
- **Konsep:** List, loop, fungsi, perhitungan rata-rata berbobot.
- **Tingkat Kesulitan:** Mudah-Menengah

### 4. Penjadwalan Sholat (Berdasarkan Waktu)
- **Deskripsi:** Program yang menampilkan jadwal sholat harian dan memberi notifikasi waktu sholat berikutnya berdasarkan waktu saat ini.
- **Konsep:** Modul `datetime`, perbandingan waktu, percabangan.
- **Tingkat Kesulitan:** Menengah

### 5. Kalkulator Zakat
- **Deskripsi:** Hitung zakat mal (emas, penghasilan, perdagangan) dan zakat fitrah berdasarkan nisab dan kadar yang berlaku.
- **Konsep:** Fungsi dengan parameter, percabangan, dictionary untuk jenis zakat.
- **Tingkat Kesulitan:** Mudah-Menengah

### 6. Analisis Data BPS (Populasi per Provinsi)
- **Deskripsi:** Baca data populasi 38 provinsi dari file CSV, tampilkan statistik (total, rata-rata, terbesar, terkecil) dan sorting.
- **Konsep:** File I/O, list of dictionaries, sorting, statistik dasar.
- **Tingkat Kesulitan:** Menengah

### 7. Sistem Antrian Puskesmas
- **Deskripsi:** Simulasi sistem antrian pasien dengan fitur: ambil nomor antrian, panggil pasien, lihat daftar tunggu, dan prioritas lansia.
- **Konsep:** List sebagai queue, loop, fungsi, menu interaktif.
- **Tingkat Kesulitan:** Menengah

### 8. Pencarian Rute TransJakarta (Simplified)
- **Deskripsi:** Diberikan daftar halte dan koridor, cari rute dari halte A ke halte B (satu koridor atau transit satu kali).
- **Konsep:** Dictionary of lists, nested loop, pencarian linear, algoritma sederhana.
- **Tingkat Kesulitan:** Menengah-Sulit

### 9. E-Commerce Product Sorting (by Price, Rating, Sales)
- **Deskripsi:** Kelola daftar produk yang bisa diurutkan berdasarkan harga, rating, atau jumlah penjualan, dengan fitur filter kategori.
- **Konsep:** List of dictionaries, sorting dengan key, fungsi `lambda`, filter.
- **Tingkat Kesulitan:** Menengah

### 10. Analisis Sentimen Review Tokopedia (Simplified Word Matching)
- **Deskripsi:** Analisis review produk sederhana menggunakan pencocokan kata positif/negatif dalam Bahasa Indonesia untuk menentukan sentimen.
- **Konsep:** String processing, dictionary, file I/O, loop, persentase.
- **Tingkat Kesulitan:** Menengah-Sulit

---

## 4. Referensi Dokumentasi

| Referensi | URL | Keterangan |
|-----------|-----|------------|
| Python 3.x Documentation | docs.python.org/3/ | Dokumentasi resmi Python, referensi utama |
| PEP 8 Style Guide | peps.python.org/pep-0008/ | Panduan penulisan kode Python yang rapi dan konsisten |
| Google Colab Getting Started | colab.research.google.com | Panduan memulai notebook di cloud |
| Python Built-in Functions | docs.python.org/3/library/functions.html | Daftar lengkap fungsi bawaan Python |

---

## 5. Rekomendasi Belajar Mandiri

### YouTube Channels
- **Corey Schafer** — Tutorial Python mendalam dan terstruktur (Bahasa Inggris)
- **Tech With Tim** — Project-based Python tutorials (Bahasa Inggris)
- **Kelas Terbuka** — Tutorial pemrograman dalam Bahasa Indonesia

### Buku
- **Think Python** (Allen B. Downey) — Pendekatan ilmu komputer untuk belajar Python
- **Automate the Boring Stuff with Python** (Al Sweigart) — Belajar Python melalui otomasi tugas sehari-hari

### Komunitas
- **r/learnpython** — Subreddit untuk pemula Python
- **Stack Overflow** — Forum tanya jawab pemrograman terbesar
- **Python Discord** — Komunitas real-time untuk diskusi dan bantuan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
