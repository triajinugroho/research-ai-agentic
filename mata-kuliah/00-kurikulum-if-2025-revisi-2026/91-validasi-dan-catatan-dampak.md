# Validasi Berkas Sumber dan Catatan Dampak

**Sumber:** `Revisi_2026_Kurikulum_OBE_IF_2025_2.xlsx` + isi repositori `mata-kuliah/`  
**Sifat:** Analisis turunan — **bukan** transkripsi sheet  
**Kurikulum:** Kurikulum Informatika 2025 — Revisi 2026  
**Ekstraksi:** September 2026  

---

> **Sifat dokumen.** Bagian 1 adalah hasil **pemeriksaan otomatis** terhadap berkas sumber.
> Bagian 2 adalah **analisis dampak** terhadap materi yang sudah ada di repositori ini.
> Keduanya merupakan catatan kerja, **bukan** bagian dari dokumen kurikulum resmi. Tidak ada
> data sumber yang diubah diam-diam — temuan dicatat apa adanya.

## 1. Hasil Pemeriksaan Konsistensi Berkas Sumber

### 1.1 Yang sudah konsisten

| Pemeriksaan | Hasil |
|---|---|
| Jumlah mata kuliah lintas sheet 8, 9, 11, 14, 15 | 58 MK — konsisten |
| Jumlah pasangan MK × CPMK pada sheet 14 dan 15 | 154 — konsisten |
| Setiap Sub-CPMK memiliki kode unik | 154 kode, tidak ada duplikat |
| Setiap CPMK terpakai oleh minimal satu mata kuliah | 26/26 terpakai |
| Kolom *BK Utama* vs matriks centang pada sheet 8 | 58/58 cocok |
| Jumlah BK pembentuk per CPL pada sheet 7 | Cocok dengan baris total sheet |
| **Bobot penilaian per mata kuliah** | **58/58 berjumlah tepat 100%** |
| Kelengkapan kolom Indikator dan Kriteria | 154/154 terisi |

### 1.2 Temuan yang perlu dikonfirmasi

| No | Temuan | Lokasi | Usulan |
|---|---|---|---|
| T-1 | Kolom `CPL` tidak cocok dengan CPL induk CPMK: baris `CPMK051` diberi `CPL03` (seharusnya `CPL05`), baris `CPMK071` diberi `CPL08` (seharusnya `CPL07`) | Sheet `Copy of (Ref) 15`, mata kuliah **Logika Informatika** | Sheet `9. CPL-MK` menetapkan Logika Informatika pada CPL05 dan CPL07 — dugaan salah ketik pada kolom CPL sheet 15 |
| T-2 | Kolom `Deskripsi Sub-CPMK` kosong untuk `LOGIF-Sub-CPMK051-1` dan `LOGIF-Sub-CPMK071-1` | Sheet `Copy of (Ref) 15`, **Logika Informatika** | Perlu diisi; kolom Materi, Indikator, Kriteria, dan bobot sudah lengkap |
| T-3 | **Praktikum Basis Data** sudah berkode `IF52510034` pada sheet 11, 14, dan 15, tetapi kolom Kode MK masih kosong pada sheet 8 dan bertuliskan `BELUM ADA` pada sheet 9 | Sheet 8 dan 9 | Sinkronkan kode `IF52510034` ke sheet 8 dan 9 |
| T-4 | Tiga mata kuliah ditempatkan pada semester berbeda antara kolom `semester` dan grid penempatan SKS: Kapita Selekta Informatika (5 vs 7), Komputasi Awan (7 vs 8), Infrastruktur TI Modern (7 vs 8) | Sheet `11` | Kolom `semester` konsisten dengan sheet 8, 9, 14, 15 — grid penempatan yang perlu diperbaiki |
| T-5 | Baris total per semester pada sheet 11 (`20 · 19 · 20 · 22 · 21 · 18 · 16 · 7`) dan baris `Jumlah MK` (total 56 dari 58 MK) tidak dapat direproduksi dari isi tabelnya sendiri | Sheet `11` | Hitung ulang sebagai formula sebelum dokumen kurikulum dicetak |
| T-6 | Kode validator ditulis `ENR` pada sheet 7, sedangkan daftar koordinator pada sheet yang sama dan kolom Kode Dosen pada sheet 8/11 memakai `ERN` | Sheet `7. CPL-BK` | Seragamkan menjadi `ERN` (Ir. Endang Ripmiatin, M.T.) |
| T-7 | Cakupan CPL BK19 ditulis `CPLFST1`, sedangkan kode resminya `CPL-FSTS1` | Sheet `7. CPL-BK`, baris BK19 | Seragamkan penulisan kode |
| T-8 | Matriks kecil di bagian bawah sheet 7 (baris 35–54) memberi hasil berbeda dengan matriks utama untuk BK15 | Sheet `7. CPL-BK` | Matriks utama (baris 5–24) dipakai sebagai acuan; matriks kecil tampak sisa draf |
| T-9 | CPMK untuk mata kuliah Universitas/Fakultas (`CPMKUAI*`, `CPMKFSTS*`) adalah rumusan Prodi Informatika | Sheet `13` (catatan pemilik dokumen) | Perlu konfirmasi ke Akademik Universitas/Fakultas |
| T-10 | Pemetaan `BK16 Systems Fundamentals` ke CPL08 dan CPL09 dipertanyakan | Sheet `7. CPL-BK` (catatan pemilik dokumen) | Perlu direview bersama koordinator rumpun |

### 1.3 Dua penamaan rumpun yang hidup berdampingan

Berkas sumber memakai **dua skema rumpun** sekaligus:

| Skema | Kode | Dipakai di | Fungsi |
|---|---|---|---|
| Rumpun mata kuliah | `R01`–`R08` | Sheet 11 | Pengelompokan mata kuliah & karakter penilaian |
| Rumpun bahan kajian | `CS`, `SE`, `P`, `SNS`, `AI`, `SEP`, `RIE` | Sheet 7 | Penugasan koordinator Bahan Kajian |

Keduanya sah, tetapi sebaiknya dijelaskan perbedaan fungsinya di dokumen kurikulum agar tidak terbaca
sebagai dua versi dari hal yang sama.

## 2. Dampak terhadap Materi yang Sudah Ada di Repositori

### 2.1 Pemetaan mata kuliah repositori → kurikulum baru

| Folder Repositori | Kode Lama | Kode Kurikulum 2025/2026 | Nama Resmi Baru | SKS Repo → Baru | Sem | Status |
|---|---|---|---|---|---|---|
| `algoritma-pemrograman/` | INF-101 | `IF52520004` | Algoritma Pemrograman | 2 → 2 | II | Cocok |
| `praktikum-algoritma-pemrograman/` | INF-102 | `IF52520005` | Praktikum Algoritma Pemrograman | 1 → 1 | II | Cocok |
| `analisis-data-statistik/` | TBD-STAT | `IF52520025` | Analisis Data Statistik | **2 → 3** | II | SKS berubah |
| `rekayasa-perangkat-lunak/` | IF2205 | `IF52520011` | Rekayasa Perangkat Lunak | 3 → 3 | IV | Kode berubah; pengampu WNS |
| `praktikum-rekayasa-perangkat-lunak/` | IF2206 | **tidak ada** | — | 1 → — | — | **Tidak ada padanan** |
| `kecerdasan-buatan-machine-learning/` | IF3XXX | `IF52510031` | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin | **4 → 3** | V | SKS & nama berubah |

### 2.2 Perubahan yang berdampak besar

**a. Arsitektur CPMK berubah total.**
Materi yang ada memakai CPMK **lokal per mata kuliah** (`CPMK-1` … `CPMK-7`, tujuh CPMK per MK).
Kurikulum baru memakai CPMK **global milik prodi** yang melekat pada CPL (`CPMK032`, `CPMK101`, …),
dengan hanya **2–3 CPMK per mata kuliah**, dan pembeda antar mata kuliah dipindahkan ke tingkat
**Sub-CPMK**. Seluruh RPS, RTM, kerangka asesmen, dan penelusuran CPMK pada buku ajar perlu
dipetakan ulang.

| Mata Kuliah | CPMK di materi lama | CPMK kurikulum baru | Sub-CPMK |
|---|---|---|---|
| Algoritma Pemrograman | CPMK-1 … CPMK-7 (7) | CPMK032, CPMK033 (2) | 2 |
| Praktikum Algoritma Pemrograman | CPMK-1 … CPMK-7 (7) | CPMK032, CPMK033 (2) | 2 |
| Analisis Data Statistik | CPMK-1 … CPMK-7 (7) | CPMK071, CPMK101, CPMK102 (3) | 3 |
| Rekayasa Perangkat Lunak | CPMK-1 … CPMK-7 (7) | CPMK052, CPMK091, CPMK092, CPMKFSTS11, CPMKFSTS12 (5) | 5 |
| Dasar Kecerdasan Artifisial dan Pembelajaran Mesin | CPMK-1 … CPMK-7 (7) | CPMK082, CPMK102 (2) | 2 |

**b. Bobot penilaian memakai enam teknik, bukan komponen nilai bebas.**
Kurikulum baru menetapkan enam teknik: Partisipasi, Kuis, Observasi (Praktek/Tugas),
Unjuk Kerja (Presentasi/Proyek), Tes Tulis UTS, dan Tes Tulis UAS — dengan bobot melekat pada
**Sub-CPMK**, dan komposisi berbeda untuk tiap mata kuliah. Bobot pada `CLAUDE.md` berbeda:

| Mata Kuliah | Bobot di `CLAUDE.md` | Bobot kurikulum baru |
|---|---|---|
| Algoritma Pemrograman | Kuis 20% · UTS 30% · UAS 40% · Partisipasi 10% | Kuis 5% · Observasi 25% · Unjuk Kerja 30% · UTS 20% · UAS 20% |
| Praktikum Algoritma Pemrograman | Laporan 25% · Tugas 25% · Proyek 35% · Responsi 10% · Partisipasi 5% | Partisipasi 5% · Kuis 5% · Observasi 50% · Unjuk Kerja 20% · UTS 10% · UAS 10% |
| Analisis Data Statistik | Tugas 15% · Kuis 10% · UTS 20% · Proyek 25% · UAS 25% · Partisipasi 5% | Kuis 15% · Observasi 25% · Unjuk Kerja 10% · UTS 25% · UAS 25% |
| Rekayasa Perangkat Lunak | Tugas 15% · Kuis 10% · UTS 20% · Proyek 25% · UAS 25% · Partisipasi 5% | Partisipasi 5% · Kuis 5% · Observasi 30% · Unjuk Kerja 20% · UTS 20% · UAS 20% |
| Dasar Kecerdasan Artifisial dan Pembelajaran Mesin | Tugas 15% · Kuis 10% · UTS 20% · Proyek 25% · UAS 25% · Partisipasi 5% | Kuis 5% · Observasi 25% · Unjuk Kerja 35% · UTS 20% · UAS 15% |

**c. Praktikum Rekayasa Perangkat Lunak (IF2206) tidak ada dalam kurikulum baru.**
Sheet 8, 9, 11, 14, dan 15 tidak memuat mata kuliah praktikum untuk Rekayasa Perangkat Lunak.
Praktikum yang terdaftar hanya: Praktikum Dasar Pemrograman, Praktikum Algoritma Pemrograman,
dan Praktikum Basis Data. Materi pada folder `praktikum-rekayasa-perangkat-lunak/` perlu
diputuskan nasibnya — diarsipkan, dilebur ke `Rekayasa Perangkat Lunak` (IF52520011) atau ke
`Proyek Perangkat Lunak` (IF52520017, 4 SKS, semester VI — 5 Sub-CPMK, bobot Partisipasi 5% · Observasi 35% · Unjuk Kerja 40% · UTS 10% · UAS 10%), atau diusulkan kembali ke prodi.

**d. Rekayasa Perangkat Lunak bukan mata kuliah ampuan Tri Aji Nugroho.**
Sheet 11 mencatat pengampu/pengembang RPS `IF52520011 Rekayasa Perangkat Lunak` adalah
Dr. Ir. Winangsari Pradani, M.T. (kode `WNS`), dan validatornya juga `WNS`.

**e. Ada dua mata kuliah ampuan yang belum punya materi di repositori.**

| Kode MK | Mata Kuliah | SKS | Sem |
|---|---|---|---|
| `IF52510033` | Probabilitas dan Statistik | 3 | I |
| `ST52510002` | Teknopreneur | 3 | V |

`Probabilitas dan Statistik` (semester I) berbeda dari `Analisis Data Statistik` (semester II) —
keduanya diampu Tri Aji Nugroho dan keduanya mengampu `CPMK102`, sehingga pembagian materinya
perlu ditegaskan agar tidak tumpang tindih.

### 2.3 Yang sudah selaras

- **Rumusan 11 CPL** pada `mata-kuliah/00-pedoman-obe/cpl-master.md` **sama persis** dengan
  [03-cpl-prodi.md](03-cpl-prodi.md) — tidak perlu perubahan.
- Penomoran kode CPL (`CPLUAI1`, `CPL-FSTS1`, `CPL03`–`CPL10`, `CPLUAI2`) sudah dipakai konsisten
  di seluruh materi repositori.
- Pendekatan **AI-augmented learning** pada materi yang ada sejalan dengan
  [14a-ai-curriculum-infusion-matrix.md](14a-ai-curriculum-infusion-matrix.md), yang menempatkan
  AI sebagai salah satu dari tiga domain keilmuan resmi prodi.

## 3. Usulan Urutan Tindak Lanjut

1. Konfirmasikan temuan **T-1** s.d. **T-3** ke tim kurikulum — ketiganya salah ketik pada berkas
   sumber, bukan keputusan kurikulum, dan paling cepat diperbaiki.
2. Putuskan nasib `praktikum-rekayasa-perangkat-lunak/` (butir 2.2c) sebelum memetakan ulang CPMK.
3. Petakan ulang CPMK dan bobot penilaian pada empat mata kuliah ampuan yang sudah punya materi,
   mulai dari `algoritma-pemrograman/` dan `praktikum-algoritma-pemrograman/` yang SKS-nya tidak berubah.
4. Sesuaikan SKS `analisis-data-statistik/` (2 → 3) dan `kecerdasan-buatan-machine-learning/` (4 → 3),
   termasuk jumlah pertemuan dan beban tugas.
5. Perbarui `CLAUDE.md` dan `README.md` repositori: kode mata kuliah, SKS, dan aturan bobot penilaian.
6. Tunggu sheet 16–20 final sebelum menyusun instrumen penilaian tingkat prodi.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
