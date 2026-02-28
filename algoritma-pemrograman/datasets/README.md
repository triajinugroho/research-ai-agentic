# Panduan Resource dan Latihan Pemrograman

**Mata Kuliah:** Algoritma dan Pemrograman
**Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.
**Program Studi:** Informatika, Universitas Al Azhar Indonesia

Dokumen ini berisi kumpulan resource, platform latihan, contoh data, dan problem set
yang dirancang untuk mendukung pembelajaran pemrograman Python secara mandiri.

## 1. Platform Latihan Online

| Platform        | URL                        | Fokus                         | Level                 | Gratis? |
|-----------------|----------------------------|-------------------------------|-----------------------|---------|
| HackerRank      | hackerrank.com             | Python practice, algorithms   | Beginner-Advanced     | Ya      |
| LeetCode (Easy) | leetcode.com               | Algorithm problems            | Beginner              | Sebagian|
| Replit          | replit.com                 | Online Python IDE             | Beginner              | Ya      |
| Exercism        | exercism.org               | Python track                  | Beginner-Intermediate | Ya      |
| CodingBat       | codingbat.com              | Logic problems                | Beginner              | Ya      |
| Advent of Code  | adventofcode.com           | Annual programming puzzles    | Intermediate          | Ya      |
| Google Colab    | colab.research.google.com  | Notebook IDE                  | All levels            | Ya      |
| Kaggle          | kaggle.com                 | Notebooks, data, competitions | Beginner-Advanced     | Ya      |

> **Tips:** Mulailah dari HackerRank atau CodingBat untuk fondasi logika, lalu gunakan
> Google Colab atau Replit sebagai IDE online untuk mengerjakan tugas kuliah.

## 2. Contoh File Data untuk Latihan File I/O

Berikut contoh file CSV yang dapat di-copy-paste ke Google Colab untuk latihan File I/O.

### a. `mahasiswa.csv`
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

### b. `menu_kantin.csv`
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

### c. `buku_perpustakaan.csv`
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

### d. `transaksi.csv`
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

## 3. Problem Set Bertema Indonesia

| No | Tantangan | Konsep Utama | Kesulitan |
|----|-----------|-------------|-----------|
| 1 | **Hitung Pajak Progresif PPh 21** — Hitung pajak berdasarkan tarif bracket (5%-35%) | `if-elif-else`, aritmatika | Mudah |
| 2 | **Konversi Rupiah Multi-Currency** — Konverter ke USD, EUR, SGD, MYR, JPY | Dictionary, fungsi, loop menu | Mudah |
| 3 | **Sistem Scoring UTBK/SNBT** — Hitung skor dari beberapa subtes berbobot | List, loop, rata-rata berbobot | Mudah-Menengah |
| 4 | **Penjadwalan Sholat** — Tampilkan waktu sholat berikutnya dari waktu saat ini | `datetime`, perbandingan waktu | Menengah |
| 5 | **Kalkulator Zakat** — Hitung zakat mal dan fitrah berdasarkan nisab | Fungsi, parameter, dictionary | Mudah-Menengah |
| 6 | **Analisis Data BPS** — Statistik populasi 38 provinsi dari file CSV | File I/O, sorting, statistik | Menengah |
| 7 | **Sistem Antrian Puskesmas** — Simulasi antrian dengan prioritas lansia | List (queue), menu interaktif | Menengah |
| 8 | **Pencarian Rute TransJakarta** — Cari rute antar halte, maks 1x transit | Dict of lists, pencarian | Menengah-Sulit |
| 9 | **E-Commerce Product Sorting** — Urutkan produk by harga/rating/sales + filter | Sorting, `lambda`, filter | Menengah |
| 10 | **Analisis Sentimen Review** — Word matching positif/negatif Bahasa Indonesia | String processing, File I/O | Menengah-Sulit |

## 4. Referensi Dokumentasi

| Referensi | URL | Keterangan |
|-----------|-----|------------|
| Python 3.x Documentation | docs.python.org/3/ | Dokumentasi resmi, referensi utama |
| PEP 8 Style Guide | peps.python.org/pep-0008/ | Panduan penulisan kode yang rapi |
| Google Colab Getting Started | colab.research.google.com | Panduan memulai notebook di cloud |
| Python Built-in Functions | docs.python.org/3/library/functions.html | Daftar lengkap fungsi bawaan |

## 5. Rekomendasi Belajar Mandiri

**YouTube Channels:**
- **Corey Schafer** — Tutorial Python mendalam dan terstruktur (Bahasa Inggris)
- **Tech With Tim** — Project-based Python tutorials (Bahasa Inggris)
- **Kelas Terbuka** — Tutorial pemrograman dalam Bahasa Indonesia

**Buku:**
- **Think Python** (Allen B. Downey) — Pendekatan ilmu komputer untuk belajar Python
- **Automate the Boring Stuff with Python** (Al Sweigart) — Python melalui otomasi tugas sehari-hari

**Komunitas:**
- **r/learnpython** — Subreddit untuk pemula Python
- **Stack Overflow** — Forum tanya jawab pemrograman terbesar
- **Python Discord** — Komunitas real-time untuk diskusi dan bantuan

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
