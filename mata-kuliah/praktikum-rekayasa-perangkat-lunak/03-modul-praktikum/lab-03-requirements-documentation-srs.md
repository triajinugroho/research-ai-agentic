# Lab 3: Requirements Documentation & SRS

## Informasi Praktikum

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Praktikum** | 3 dari 13 |
| **Topik** | Requirements Documentation & SRS |
| **CPMK** | CPMK-3 (Menyusun dokumen kebutuhan perangkat lunak menggunakan standar IEEE 830) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 1-2 selesai, repository `perpustakaan-uai` dengan branching workflow |

**Referensi Teori:** [IF2205 Minggu 3 — Requirements Engineering dan Analisis Kebutuhan](../../../rekayasa-perangkat-lunak/03-modules/week-03-requirements-engineering-dan-analisis-kebutuhan.md)

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. **Mengidentifikasi** (*identify* — C4) stakeholder dan kebutuhan mereka untuk Sistem Perpustakaan Digital UAI
2. **Mengklasifikasikan** (*classify* — C4) functional requirements dan non-functional requirements
3. **Menyusun** (*compose* — C6) dokumen SRS mengikuti template IEEE 830 dalam format Markdown
4. **Memvalidasi** (*validate* — C5) requirements menggunakan kriteria SMART

---

## Konsep Singkat

### Mengapa Requirements Engineering Penting?

Riset menunjukkan bahwa **60-70% kegagalan proyek perangkat lunak** disebabkan oleh requirements yang buruk — bukan karena coding yang salah. Memperbaiki kesalahan requirements di tahap implementasi bisa **100x lebih mahal** dibanding memperbaikinya di awal.

> Pelajari teori lengkap Requirements Engineering di [Modul IF2205 Minggu 3](../../../rekayasa-perangkat-lunak/03-modules/week-03-requirements-engineering-dan-analisis-kebutuhan.md).

### Proses Requirements Engineering

```
┌─────────────┐    ┌──────────────┐    ┌──────────────┐    ┌─────────────┐
│  Elicitation │───>│   Analysis   │───>│Specification │───>│ Validation  │
│  (Penggalian)│    │  (Analisis)  │    │  (Penulisan) │    │ (Validasi)  │
└─────────────┘    └──────────────┘    └──────────────┘    └─────────────┘
       │                  │                   │                   │
  Wawancara,         Prioritas,          Dokumen SRS,        Review,
  observasi,         klasifikasi,        use cases,          SMART test,
  kuesioner          resolusi konflik    spesifikasi         traceability
```

### Functional vs Non-Functional Requirements

```
                     REQUIREMENTS
                          │
            ┌─────────────┴─────────────┐
            │                           │
    ┌───────▼──────┐           ┌────────▼────────┐
    │  Functional   │           │ Non-Functional  │
    │ (Apa yang     │           │ (Bagaimana      │
    │  sistem       │           │  sistem harus   │
    │  lakukan)     │           │  bekerja)       │
    └───────┬──────┘           └────────┬────────┘
            │                           │
    - Cari buku                 - Response < 2 detik
    - Pinjam buku              - Uptime 99%
    - Kelola anggota           - Support 100 users
    - Generate laporan         - Data terenkripsi
```

### IEEE 830 — Standar SRS

IEEE 830 adalah standar internasional untuk penulisan Software Requirements Specification. Struktur utamanya:

| Section | Isi |
|---------|-----|
| 1. Pendahuluan | Tujuan, ruang lingkup, definisi, referensi |
| 2. Deskripsi Umum | Perspektif produk, fungsi, karakteristik pengguna, batasan |
| 3. Kebutuhan Spesifik | Functional requirements, non-functional requirements, interface |
| Appendix | Informasi tambahan, traceability matrix |

### Studi Kasus: Perpustakaan Digital UAI

Di lab ini, kita menyusun SRS untuk **Sistem Perpustakaan Digital UAI** — sistem yang sama yang kita bangun sejak Lab 1. Stakeholder utama meliputi mahasiswa, pustakawan, admin IT, dan dosen.

---

## Persiapan

Sebelum praktikum dimulai, pastikan:

- [ ] Lab 1-2 sudah selesai
- [ ] Sudah membaca [Modul IF2205 Minggu 3](../../../rekayasa-perangkat-lunak/03-modules/week-03-requirements-engineering-dan-analisis-kebutuhan.md)
- [ ] Memahami konsep dasar functional vs non-functional requirements
- [ ] Codespace repository `perpustakaan-uai` bisa dibuka

**Tools yang akan digunakan:**

| Tool | Fungsi |
|------|--------|
| Markdown | Penulisan dokumen SRS |
| GitHub Codespaces | Editor dan version control |
| Git | Commit dan PR untuk SRS document |

---

## Langkah-langkah

### Langkah 1: Identifikasi Stakeholder (15 menit)

**Mengapa langkah ini penting:**
Stakeholder yang terlewat berarti kebutuhan yang terlewat. Mengidentifikasi **semua** pihak yang terlibat dengan sistem memastikan kita tidak melewatkan requirements penting.

**Instruksi:**

1. Buka Codespace repository `perpustakaan-uai`
2. Buat branch baru untuk pekerjaan SRS:

```bash
git checkout develop
git pull origin develop
git checkout -b feature/srs-document
```

3. Buat folder dokumentasi:

```bash
mkdir -p docs
```

4. Buat file `docs/stakeholder-analysis.md`:

```bash
cat > docs/stakeholder-analysis.md << 'STAKEHOLDER_EOF'
# Analisis Stakeholder — Perpustakaan Digital UAI

## Daftar Stakeholder

| No | Stakeholder | Peran | Kepentingan | Pengaruh |
|----|-------------|-------|-------------|----------|
| 1 | Mahasiswa | Pengguna utama | Tinggi | Rendah |
| 2 | Pustakawan | Operator sistem | Tinggi | Tinggi |
| 3 | Admin IT | Pengelola infrastruktur | Sedang | Tinggi |
| 4 | Dosen | Pengguna referensi akademik | Sedang | Sedang |
| 5 | Kepala Perpustakaan | Pemilik proses bisnis | Tinggi | Tinggi |
| 6 | Rektorat UAI | Sponsor proyek | Rendah | Tinggi |

## Detail Kebutuhan per Stakeholder

### 1. Mahasiswa
- **Profil:** 3000+ mahasiswa aktif, usia 18-24, melek teknologi
- **Kebutuhan utama:**
  - Mencari buku berdasarkan judul, penulis, atau kategori
  - Melihat ketersediaan buku secara real-time
  - Meminjam dan mengembalikan buku secara online
  - Melihat riwayat peminjaman
  - Mendapat notifikasi deadline pengembalian
- **Pain points saat ini:**
  - Harus datang ke perpustakaan untuk cek ketersediaan
  - Antri panjang saat jam sibuk
  - Tidak tahu buku yang dikembalikan sudah tersedia

### 2. Pustakawan
- **Profil:** 5-8 staff, usia 25-55, kemampuan IT bervariasi
- **Kebutuhan utama:**
  - Mengelola katalog buku (CRUD)
  - Memproses peminjaman dan pengembalian
  - Mengelola data anggota perpustakaan
  - Membuat laporan statistik bulanan
  - Mengirim notifikasi keterlambatan
- **Pain points saat ini:**
  - Pencatatan manual rentan kesalahan
  - Sulit membuat laporan statistik
  - Komunikasi dengan mahasiswa lambat

### 3. Admin IT
- **Profil:** 2-3 staff teknis, memahami server dan jaringan
- **Kebutuhan utama:**
  - Sistem yang mudah di-deploy dan di-maintain
  - Monitoring performa dan log error
  - Backup data otomatis
  - Keamanan data pengguna
- **Pain points saat ini:**
  - Tidak ada sistem digital yang perlu dikelola (semua manual)

### 4. Dosen
- **Profil:** 100+ dosen, usia 30-60, kemampuan IT bervariasi
- **Kebutuhan utama:**
  - Merekomendasikan buku referensi ke mahasiswa
  - Melihat ketersediaan buku ajar
  - Request pembelian buku baru
- **Pain points saat ini:**
  - Tidak tahu koleksi perpustakaan yang tersedia

### 5. Kepala Perpustakaan
- **Profil:** 1 orang, pengambil keputusan
- **Kebutuhan utama:**
  - Dashboard statistik penggunaan
  - Laporan inventaris buku
  - Data untuk perencanaan anggaran

## Matriks Pengaruh-Kepentingan

```
Pengaruh Tinggi │ Admin IT        │ Pustakawan
                │ Rektorat        │ Kep. Perpustakaan
                ├─────────────────┼─────────────────
Pengaruh Rendah │                 │ Mahasiswa
                │ (-)             │ Dosen
                ├─────────────────┼─────────────────
                  Kepentingan      Kepentingan
                  Rendah           Tinggi
```

**Strategi:**
- Pustakawan & Kep. Perpustakaan: Libatkan aktif dalam setiap tahap
- Admin IT & Rektorat: Jaga komunikasi rutin
- Mahasiswa & Dosen: Survey kebutuhan, test usability
STAKEHOLDER_EOF
```

5. Commit:

```bash
git add docs/stakeholder-analysis.md
git commit -m "docs(requirements): add stakeholder analysis for Perpustakaan Digital UAI"
```

**Expected Output:**

File `docs/stakeholder-analysis.md` berisi analisis lengkap 6 stakeholder dengan detail kebutuhan masing-masing.

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| Bingung menentukan stakeholder | Pikirkan: siapa yang akan MENGGUNAKAN, MENGELOLA, dan MEMBIAYAI sistem? |
| Terlalu banyak stakeholder | Fokus pada 5-7 stakeholder utama, kelompokkan yang mirip |

---

### Langkah 2: Mendefinisikan Functional Requirements (15 menit)

**Mengapa langkah ini penting:**
Functional requirements menentukan **apa yang harus bisa dilakukan** oleh sistem. Requirements yang tidak terdokumentasi berisiko terlupakan atau diimplementasikan berbeda dari harapan stakeholder.

**Instruksi:**

1. Buat file `docs/requirements-list.md`:

```bash
cat > docs/requirements-list.md << 'REQ_EOF'
# Daftar Requirements — Perpustakaan Digital UAI

## Functional Requirements (FR)

| ID | Requirement | Prioritas | Stakeholder | Status |
|----|-------------|-----------|-------------|--------|
| FR-01 | Sistem harus memungkinkan mahasiswa mencari buku berdasarkan judul, penulis, ISBN, atau kategori | Must-have | Mahasiswa | Draft |
| FR-02 | Sistem harus menampilkan status ketersediaan buku secara real-time (tersedia/dipinjam) | Must-have | Mahasiswa, Pustakawan | Draft |
| FR-03 | Sistem harus memungkinkan mahasiswa meminjam buku secara online dengan konfirmasi pustakawan | Must-have | Mahasiswa, Pustakawan | Draft |
| FR-04 | Sistem harus mencatat tanggal peminjaman dan deadline pengembalian secara otomatis | Must-have | Pustakawan | Draft |
| FR-05 | Sistem harus mengirim notifikasi email 3 hari sebelum deadline pengembalian | Should-have | Mahasiswa | Draft |
| FR-06 | Sistem harus memungkinkan pustakawan menambah, mengubah, dan menghapus data buku (CRUD) | Must-have | Pustakawan | Draft |
| FR-07 | Sistem harus memungkinkan pustakawan mengelola data anggota perpustakaan (CRUD) | Must-have | Pustakawan | Draft |
| FR-08 | Sistem harus menghasilkan laporan statistik peminjaman bulanan | Should-have | Kep. Perpustakaan | Draft |
| FR-09 | Sistem harus memungkinkan dosen merekomendasikan buku ke mahasiswa | Could-have | Dosen | Draft |
| FR-10 | Sistem harus menyediakan dashboard admin dengan ringkasan statistik | Should-have | Kep. Perpustakaan | Draft |
| FR-11 | Sistem harus memungkinkan mahasiswa melihat riwayat peminjaman mereka | Must-have | Mahasiswa | Draft |
| FR-12 | Sistem harus mendukung login dengan email UAI (@uai.ac.id) | Must-have | Admin IT | Draft |
| FR-13 | Sistem harus menghitung denda keterlambatan otomatis (Rp 1.000/hari) | Should-have | Pustakawan | Draft |
| FR-14 | Sistem harus mendukung reservasi buku yang sedang dipinjam | Could-have | Mahasiswa | Draft |

## Non-Functional Requirements (NFR)

| ID | Requirement | Kategori | Metrik | Prioritas |
|----|-------------|----------|--------|-----------|
| NFR-01 | Halaman harus dimuat dalam waktu kurang dari 2 detik | Performance | Response time < 2s | Must-have |
| NFR-02 | Sistem harus tersedia minimal 99% selama jam operasional (08:00-22:00) | Availability | Uptime >= 99% | Must-have |
| NFR-03 | Sistem harus mampu melayani minimal 100 pengguna bersamaan | Scalability | Concurrent users >= 100 | Should-have |
| NFR-04 | Data password pengguna harus dienkripsi menggunakan bcrypt | Security | Enkripsi bcrypt | Must-have |
| NFR-05 | Sistem harus memiliki antarmuka responsif (desktop dan mobile) | Usability | Responsive design | Must-have |
| NFR-06 | Backup database harus dilakukan otomatis setiap hari | Reliability | Daily backup | Should-have |
| NFR-07 | Sistem harus mendukung browser Chrome, Firefox, Edge, dan Safari | Compatibility | 4 browser | Must-have |
| NFR-08 | API response harus menggunakan format JSON standar | Interoperability | JSON format | Must-have |
REQ_EOF
```

2. Commit:

```bash
git add docs/requirements-list.md
git commit -m "docs(requirements): define 14 functional and 8 non-functional requirements"
```

**Expected Output:**

File `docs/requirements-list.md` berisi 14 FR dan 8 NFR yang terstruktur dengan ID, prioritas, dan stakeholder.

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| Sulit membedakan FR dan NFR | FR = "Sistem harus MELAKUKAN X", NFR = "Sistem harus BERSIFAT Y" |
| Requirements terlalu ambigu | Gunakan metrik terukur: bukan "cepat" tapi "< 2 detik" |
| Overlap antara requirements | Cek apakah satu requirement bisa di-merge dengan yang lain |

---

### Langkah 3: Menulis Dokumen SRS IEEE 830 (25 menit)

**Mengapa langkah ini penting:**
SRS adalah **kontrak teknis** antara developer dan stakeholder. Dokumen ini menjadi acuan utama selama pengembangan dan testing. Menggunakan standar IEEE 830 memastikan kelengkapan dan profesionalisme.

**Instruksi:**

Buat file `docs/SRS.md` dengan struktur IEEE 830 lengkap:

```bash
cat > docs/SRS.md << 'SRS_EOF'
# Software Requirements Specification (SRS)
# Sistem Perpustakaan Digital UAI

**Versi:** 1.0
**Tanggal:** [tanggal hari ini]
**Disusun oleh:** Tim Praktikum RPL IF2206
**Universitas Al Azhar Indonesia**

---

## Daftar Isi

1. [Pendahuluan](#1-pendahuluan)
2. [Deskripsi Umum](#2-deskripsi-umum)
3. [Kebutuhan Spesifik](#3-kebutuhan-spesifik)
4. [Appendix](#4-appendix)

---

## 1. Pendahuluan

### 1.1 Tujuan
Dokumen ini mendeskripsikan Software Requirements Specification (SRS) untuk **Sistem Perpustakaan Digital UAI**. Dokumen ini ditujukan untuk tim pengembang, pustakawan, admin IT, dan stakeholder lainnya sebagai acuan dalam proses pengembangan sistem.

### 1.2 Ruang Lingkup
**Sistem Perpustakaan Digital UAI** adalah aplikasi web yang memfasilitasi pengelolaan perpustakaan Universitas Al Azhar Indonesia secara digital. Sistem ini mencakup:
- Pencarian dan penelusuran katalog buku
- Peminjaman dan pengembalian buku secara online
- Pengelolaan data buku dan anggota
- Pelaporan statistik penggunaan perpustakaan

**Yang TIDAK termasuk dalam ruang lingkup:**
- Pembelian buku online (e-commerce)
- Manajemen perpustakaan antar-kampus
- Digitalisasi konten buku (e-book reader)

### 1.3 Definisi, Akronim, dan Singkatan

| Istilah | Definisi |
|---------|----------|
| SRS | Software Requirements Specification |
| UAI | Universitas Al Azhar Indonesia |
| CRUD | Create, Read, Update, Delete |
| API | Application Programming Interface |
| ISBN | International Standard Book Number |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| MoSCoW | Must-have, Should-have, Could-have, Won't-have |

### 1.4 Referensi
- IEEE Std 830-1998: IEEE Recommended Practice for Software Requirements Specifications
- Modul IF2205 Minggu 3: Requirements Engineering dan Analisis Kebutuhan
- Pedoman Perpustakaan UAI (dokumen internal)

### 1.5 Gambaran Umum Dokumen
- **Bagian 2** mendeskripsikan konteks umum sistem, karakteristik pengguna, dan batasan
- **Bagian 3** mendeskripsikan requirements spesifik (functional dan non-functional)
- **Appendix** berisi informasi tambahan dan traceability matrix

---

## 2. Deskripsi Umum

### 2.1 Perspektif Produk
Sistem Perpustakaan Digital UAI adalah sistem **baru** yang menggantikan proses manual pencatatan peminjaman buku di Perpustakaan UAI. Sistem ini merupakan aplikasi web yang berdiri sendiri (*standalone*) dengan arsitektur client-server.

```
┌──────────────────┐     HTTP/HTTPS     ┌──────────────────┐
│   Client Layer   │◄──────────────────►│   Server Layer   │
│                  │                     │                  │
│  - Browser Web   │                     │  - Flask (Python)│
│  - Mobile Browser│                     │  - REST API      │
│                  │                     │  - SQLAlchemy    │
└──────────────────┘                     └────────┬─────────┘
                                                  │
                                         ┌────────▼─────────┐
                                         │  Database Layer   │
                                         │                  │
                                         │  - SQLite/       │
                                         │    PostgreSQL    │
                                         └──────────────────┘
```

### 2.2 Fungsi Produk
Sistem menyediakan fungsi-fungsi utama berikut:
1. **Manajemen Katalog:** Pencarian, penambahan, pengubahan, dan penghapusan data buku
2. **Manajemen Peminjaman:** Proses peminjaman, pengembalian, dan perpanjangan buku
3. **Manajemen Anggota:** Registrasi dan pengelolaan data anggota perpustakaan
4. **Notifikasi:** Pengingat deadline pengembalian dan pemberitahuan keterlambatan
5. **Pelaporan:** Dashboard statistik dan laporan penggunaan perpustakaan

### 2.3 Karakteristik Pengguna

| Pengguna | Jumlah | Kemampuan Teknis | Frekuensi Penggunaan |
|----------|--------|-----------------|---------------------|
| Mahasiswa | ~3000 | Tinggi (digital native) | Harian |
| Pustakawan | 5-8 | Sedang | Harian (full-time) |
| Dosen | ~100 | Bervariasi | Mingguan |
| Admin IT | 2-3 | Tinggi | Sesuai kebutuhan |
| Kep. Perpustakaan | 1 | Sedang | Mingguan |

### 2.4 Batasan (Constraints)
- Sistem harus berjalan di infrastruktur server UAI yang ada
- Budget pengembangan terbatas (proyek mahasiswa)
- Timeline: 1 semester (16 minggu)
- Harus menggunakan Python Flask sebagai backend framework
- Database awal menggunakan SQLite (migrasi ke PostgreSQL untuk production)

### 2.5 Asumsi dan Dependensi
- Semua mahasiswa dan dosen memiliki akun email UAI (@uai.ac.id)
- Koneksi internet tersedia di lingkungan kampus
- Data buku awal akan diimpor dari katalog manual yang ada
- Pustakawan bersedia mengikuti pelatihan penggunaan sistem

---

## 3. Kebutuhan Spesifik

### 3.1 Kebutuhan Fungsional

#### 3.1.1 Modul Pencarian Buku

**FR-01: Pencarian Buku**
- **Deskripsi:** Sistem harus memungkinkan pengguna mencari buku berdasarkan judul, penulis, ISBN, atau kategori
- **Input:** Kata kunci pencarian (string), filter opsional (kategori, tahun)
- **Proses:** Query ke database dengan partial matching
- **Output:** Daftar buku yang sesuai dengan informasi lengkap dan status ketersediaan
- **Prioritas:** Must-have

**FR-02: Status Ketersediaan Buku**
- **Deskripsi:** Sistem harus menampilkan status ketersediaan buku secara real-time
- **Input:** Permintaan halaman detail buku
- **Proses:** Cek jumlah eksemplar tersedia di database
- **Output:** Status "Tersedia (N eksemplar)" atau "Sedang dipinjam semua"
- **Prioritas:** Must-have

#### 3.1.2 Modul Peminjaman

**FR-03: Peminjaman Buku Online**
- **Deskripsi:** Sistem harus memungkinkan mahasiswa meminjam buku secara online dengan konfirmasi pustakawan
- **Input:** ID buku, ID mahasiswa
- **Proses:** Validasi ketersediaan, buat record peminjaman, kurangi stok
- **Output:** Konfirmasi peminjaman dengan nomor referensi dan deadline pengembalian
- **Prioritas:** Must-have

**FR-04: Pencatatan Otomatis**
- **Deskripsi:** Sistem harus mencatat tanggal peminjaman dan deadline pengembalian secara otomatis
- **Input:** Transaksi peminjaman berhasil
- **Proses:** Set tanggal pinjam = hari ini, deadline = hari ini + 14 hari
- **Output:** Record peminjaman dengan tanggal lengkap
- **Prioritas:** Must-have

**FR-05: Notifikasi Deadline**
- **Deskripsi:** Sistem harus mengirim notifikasi email 3 hari sebelum deadline pengembalian
- **Input:** Daftar peminjaman yang mendekati deadline
- **Proses:** Cron job harian, filter H-3, kirim email
- **Output:** Email notifikasi ke mahasiswa
- **Prioritas:** Should-have

#### 3.1.3 Modul Manajemen Data

**FR-06: CRUD Buku**
- **Deskripsi:** Pustakawan dapat menambah, melihat, mengubah, dan menghapus data buku
- **Prioritas:** Must-have

**FR-07: CRUD Anggota**
- **Deskripsi:** Pustakawan dapat mengelola data anggota perpustakaan
- **Prioritas:** Must-have

**FR-08: Laporan Statistik**
- **Deskripsi:** Sistem menghasilkan laporan statistik peminjaman per bulan
- **Prioritas:** Should-have

#### 3.1.4 Modul Tambahan

**FR-09: Rekomendasi Buku oleh Dosen**
- **Deskripsi:** Dosen dapat merekomendasikan buku ke mahasiswa
- **Prioritas:** Could-have

**FR-10: Dashboard Admin**
- **Deskripsi:** Dashboard dengan ringkasan statistik untuk kepala perpustakaan
- **Prioritas:** Should-have

**FR-11: Riwayat Peminjaman**
- **Deskripsi:** Mahasiswa dapat melihat riwayat semua peminjaman mereka
- **Prioritas:** Must-have

**FR-12: Login dengan Email UAI**
- **Deskripsi:** Autentikasi menggunakan email @uai.ac.id
- **Prioritas:** Must-have

**FR-13: Perhitungan Denda Otomatis**
- **Deskripsi:** Sistem menghitung denda keterlambatan Rp 1.000/hari secara otomatis
- **Prioritas:** Should-have

**FR-14: Reservasi Buku**
- **Deskripsi:** Mahasiswa dapat mereservasi buku yang sedang dipinjam orang lain
- **Prioritas:** Could-have

### 3.2 Kebutuhan Non-Fungsional

#### 3.2.1 Performance
- **NFR-01:** Halaman harus dimuat dalam waktu kurang dari 2 detik untuk 95% request
- **NFR-03:** Sistem harus mampu melayani minimal 100 pengguna bersamaan

#### 3.2.2 Availability
- **NFR-02:** Sistem harus tersedia minimal 99% selama jam operasional (08:00-22:00 WIB)

#### 3.2.3 Security
- **NFR-04:** Password pengguna harus dienkripsi menggunakan bcrypt dengan minimal 12 rounds

#### 3.2.4 Usability
- **NFR-05:** Antarmuka harus responsif dan dapat diakses dari desktop dan mobile
- **NFR-07:** Sistem harus mendukung browser Chrome, Firefox, Edge, dan Safari (2 versi terakhir)

#### 3.2.5 Reliability
- **NFR-06:** Backup database otomatis setiap hari pukul 02:00 WIB

#### 3.2.6 Interoperability
- **NFR-08:** Semua API response menggunakan format JSON sesuai standar REST

### 3.3 Kebutuhan Antarmuka

#### 3.3.1 User Interface
- Desain minimalis dan intuitif
- Warna primer: Hijau (#2E7D32) sesuai identitas UAI
- Typography: font sans-serif yang mudah dibaca
- Navigasi utama: Home, Cari Buku, Peminjaman, Profil

#### 3.3.2 API Interface

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/api/books` | Daftar semua buku |
| GET | `/api/books/<id>` | Detail satu buku |
| GET | `/api/books/search?q=` | Pencarian buku |
| POST | `/api/books` | Tambah buku baru (pustakawan) |
| PUT | `/api/books/<id>` | Update data buku (pustakawan) |
| DELETE | `/api/books/<id>` | Hapus buku (pustakawan) |
| POST | `/api/loans` | Buat peminjaman baru |
| PUT | `/api/loans/<id>/return` | Proses pengembalian |
| GET | `/api/users/<id>/loans` | Riwayat peminjaman user |

---

## 4. Appendix

### 4.1 Requirements Traceability Matrix

| Requirement | Stakeholder | Sprint Target | Test Case |
|-------------|-------------|--------------|-----------|
| FR-01 | Mahasiswa | Sprint 1 | TC-01 |
| FR-02 | Mahasiswa, Pustakawan | Sprint 1 | TC-02 |
| FR-03 | Mahasiswa, Pustakawan | Sprint 2 | TC-03 |
| FR-04 | Pustakawan | Sprint 2 | TC-04 |
| FR-05 | Mahasiswa | Sprint 3 | TC-05 |
| FR-06 | Pustakawan | Sprint 1 | TC-06 |
| FR-07 | Pustakawan | Sprint 2 | TC-07 |
| FR-08 | Kep. Perpustakaan | Sprint 3 | TC-08 |
| FR-09 | Dosen | Sprint 3 | TC-09 |
| FR-10 | Kep. Perpustakaan | Sprint 3 | TC-10 |
| FR-11 | Mahasiswa | Sprint 2 | TC-11 |
| FR-12 | Admin IT | Sprint 1 | TC-12 |
| FR-13 | Pustakawan | Sprint 2 | TC-13 |
| FR-14 | Mahasiswa | Sprint 3 | TC-14 |

### 4.2 Riwayat Perubahan Dokumen

| Versi | Tanggal | Perubahan | Penulis |
|-------|---------|-----------|---------|
| 0.1 | [tanggal] | Draft awal | [nama mahasiswa] |
| 1.0 | [tanggal] | Versi final Lab 3 | [nama mahasiswa] |

---

*Dokumen ini disusun sebagai bagian dari Praktikum Rekayasa Perangkat Lunak (IF2206), Universitas Al Azhar Indonesia.*
SRS_EOF
```

Commit:

```bash
git add docs/SRS.md
git commit -m "docs(requirements): create SRS document following IEEE 830 template

- Section 1: Introduction with scope and definitions
- Section 2: Overall description with system architecture
- Section 3: Specific requirements (14 FR + 8 NFR)
- Appendix: Requirements traceability matrix"
```

**Expected Output:**

File `docs/SRS.md` berisi dokumen SRS lengkap dengan 4 section utama sesuai IEEE 830. Verifikasi:

```bash
wc -l docs/SRS.md
```

Output: sekitar 200+ baris.

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| Bingung apa yang harus ditulis di tiap section | Ikuti template IEEE 830 yang diberikan, isi dengan konteks Perpustakaan UAI |
| Requirements terasa terlalu banyak | Fokus pada Must-have dulu, Should-have dan Could-have bisa ditambahkan nanti |
| Tabel Markdown tidak rapi | Gunakan extension Markdown di VS Code atau validasi di preview |

---

### Langkah 4: Validasi Requirements dengan Kriteria SMART (10 menit)

**Mengapa langkah ini penting:**
Requirements yang ambigu atau tidak terukur akan menyebabkan masalah saat implementasi dan testing. Kriteria SMART memastikan setiap requirement **spesifik, terukur, achievable, relevan, dan time-bound**.

**Instruksi:**

1. Buat file `docs/requirements-validation.md`:

```bash
cat > docs/requirements-validation.md << 'VALID_EOF'
# Validasi Requirements — Kriteria SMART

## Apa itu SMART?

| Kriteria | Pertanyaan | Contoh Baik | Contoh Buruk |
|----------|-----------|-------------|--------------|
| **S**pecific | Apakah jelas dan tidak ambigu? | "Cari buku by judul, penulis, ISBN" | "Cari buku" |
| **M**easurable | Apakah bisa diukur? | "Response time < 2 detik" | "Harus cepat" |
| **A**chievable | Apakah bisa dicapai? | "100 concurrent users" | "1 juta users" |
| **R**elevant | Apakah relevan untuk stakeholder? | "Notifikasi deadline" | "Fitur game" |
| **T**ime-bound | Apakah ada batas waktu? | "Selesai di Sprint 2" | "Kapan-kapan" |

## Hasil Validasi

| ID | Requirement (Ringkas) | S | M | A | R | T | Status | Catatan |
|----|----------------------|---|---|---|---|---|--------|---------|
| FR-01 | Pencarian buku multi-kriteria | Y | Y | Y | Y | Y | Valid | - |
| FR-02 | Status ketersediaan real-time | Y | Y | Y | Y | Y | Valid | - |
| FR-03 | Peminjaman online | Y | Y | Y | Y | Y | Valid | - |
| FR-04 | Pencatatan otomatis | Y | Y | Y | Y | Y | Valid | - |
| FR-05 | Notifikasi email H-3 | Y | Y | Y | Y | Y | Valid | Perlu SMTP server |
| FR-06 | CRUD buku | Y | Y | Y | Y | Y | Valid | - |
| FR-07 | CRUD anggota | Y | Y | Y | Y | Y | Valid | - |
| FR-08 | Laporan bulanan | Y | Y | Y | Y | N | Revisi | Tambahkan sprint target |
| FR-09 | Rekomendasi dosen | Y | N | Y | Y | N | Revisi | Perlu metrik keberhasilan |
| FR-10 | Dashboard admin | Y | N | Y | Y | Y | Revisi | Perlu spesifikasi widget |
| FR-11 | Riwayat peminjaman | Y | Y | Y | Y | Y | Valid | - |
| FR-12 | Login email UAI | Y | Y | Y | Y | Y | Valid | - |
| FR-13 | Denda otomatis | Y | Y | Y | Y | Y | Valid | Rp 1.000/hari |
| FR-14 | Reservasi buku | Y | Y | Y | Y | N | Revisi | Perlu sprint target |
| NFR-01 | Response < 2 detik | Y | Y | Y | Y | Y | Valid | 95th percentile |
| NFR-02 | Uptime >= 99% | Y | Y | Y | Y | Y | Valid | Jam operasional |
| NFR-03 | 100 concurrent users | Y | Y | Y | Y | Y | Valid | Load test needed |
| NFR-04 | Enkripsi bcrypt | Y | Y | Y | Y | Y | Valid | 12 rounds |
| NFR-05 | Responsive design | Y | Y | Y | Y | Y | Valid | Mobile + desktop |
| NFR-06 | Daily backup | Y | Y | Y | Y | Y | Valid | 02:00 WIB |
| NFR-07 | 4 browser support | Y | Y | Y | Y | Y | Valid | 2 versi terakhir |
| NFR-08 | JSON API format | Y | Y | Y | Y | Y | Valid | REST standard |

## Ringkasan

- **Valid:** 18 requirements (82%)
- **Perlu revisi:** 4 requirements (18%)
- **Tindak lanjut:** Revisi FR-08, FR-09, FR-10, FR-14 untuk menambahkan metrik dan timeline
VALID_EOF
```

2. Commit:

```bash
git add docs/requirements-validation.md
git commit -m "docs(requirements): add SMART validation for all requirements

- 18 of 22 requirements pass SMART validation
- 4 requirements flagged for revision (missing metrics/timeline)"
```

**Expected Output:**

File validasi menunjukkan bahwa 82% requirements sudah memenuhi kriteria SMART, dan 4 requirements perlu diperbaiki.

---

### Langkah 5: Membuat Requirements Traceability Matrix (10 menit)

**Mengapa langkah ini penting:**
Traceability matrix menghubungkan requirements ke stakeholder, sprint, dan test case. Ini memastikan **tidak ada requirement yang terlupakan** selama development dan testing.

**Instruksi:**

1. Buat file `docs/traceability-matrix.md`:

```bash
cat > docs/traceability-matrix.md << 'RTM_EOF'
# Requirements Traceability Matrix (RTM)
# Perpustakaan Digital UAI

## Forward Traceability: Requirement → Implementation → Test

| Req ID | Requirement | Modul/Komponen | Sprint | Test Case | Status |
|--------|-------------|---------------|--------|-----------|--------|
| FR-01 | Pencarian buku | `routes/books.py` | Sprint 1 | TC-01: search by title, author, ISBN | Planned |
| FR-02 | Status ketersediaan | `routes/books.py` | Sprint 1 | TC-02: display available/unavailable | Planned |
| FR-03 | Peminjaman online | `routes/loans.py` | Sprint 2 | TC-03: create loan, validate stock | Planned |
| FR-04 | Pencatatan otomatis | `models/loan.py` | Sprint 2 | TC-04: auto-set dates | Planned |
| FR-05 | Notifikasi email | `services/notification.py` | Sprint 3 | TC-05: send email H-3 | Planned |
| FR-06 | CRUD buku | `routes/books.py` | Sprint 1 | TC-06: create, read, update, delete book | Planned |
| FR-07 | CRUD anggota | `routes/users.py` | Sprint 2 | TC-07: CRUD user operations | Planned |
| FR-08 | Laporan statistik | `routes/reports.py` | Sprint 3 | TC-08: monthly report generation | Planned |
| FR-09 | Rekomendasi dosen | `routes/recommendations.py` | Sprint 3 | TC-09: create recommendation | Planned |
| FR-10 | Dashboard admin | `routes/dashboard.py` | Sprint 3 | TC-10: display statistics | Planned |
| FR-11 | Riwayat peminjaman | `routes/loans.py` | Sprint 2 | TC-11: list user's loan history | Planned |
| FR-12 | Login email UAI | `routes/auth.py` | Sprint 1 | TC-12: login, validate @uai.ac.id | Planned |
| FR-13 | Denda otomatis | `models/loan.py` | Sprint 2 | TC-13: calculate penalty | Planned |
| FR-14 | Reservasi buku | `routes/reservations.py` | Sprint 3 | TC-14: reserve unavailable book | Planned |

## Backward Traceability: Test → Requirement → Stakeholder

| Test Case | Requirement | Stakeholder Utama | Prioritas |
|-----------|-------------|-------------------|-----------|
| TC-01 | FR-01 | Mahasiswa | Must-have |
| TC-02 | FR-02 | Mahasiswa | Must-have |
| TC-03 | FR-03 | Mahasiswa, Pustakawan | Must-have |
| TC-04 | FR-04 | Pustakawan | Must-have |
| TC-05 | FR-05 | Mahasiswa | Should-have |
| TC-06 | FR-06 | Pustakawan | Must-have |
| TC-07 | FR-07 | Pustakawan | Must-have |
| TC-08 | FR-08 | Kep. Perpustakaan | Should-have |
| TC-09 | FR-09 | Dosen | Could-have |
| TC-10 | FR-10 | Kep. Perpustakaan | Should-have |
| TC-11 | FR-11 | Mahasiswa | Must-have |
| TC-12 | FR-12 | Admin IT | Must-have |
| TC-13 | FR-13 | Pustakawan | Should-have |
| TC-14 | FR-14 | Mahasiswa | Could-have |

## Sprint Coverage

| Sprint | Requirements | Jumlah | Coverage |
|--------|-------------|--------|----------|
| Sprint 1 | FR-01, FR-02, FR-06, FR-12 | 4 | 29% |
| Sprint 2 | FR-03, FR-04, FR-07, FR-11, FR-13 | 5 | 36% |
| Sprint 3 | FR-05, FR-08, FR-09, FR-10, FR-14 | 5 | 36% |
| **Total** | | **14** | **100%** |
RTM_EOF
```

2. Commit:

```bash
git add docs/traceability-matrix.md
git commit -m "docs(requirements): add requirements traceability matrix

- Forward traceability: requirement to implementation and test
- Backward traceability: test to requirement and stakeholder
- Sprint coverage analysis"
```

**Expected Output:**

RTM menunjukkan setiap requirement terhubung ke modul implementasi, sprint target, dan test case.

---

### Langkah 6: Push dan Buat Pull Request (10 menit)

**Mengapa langkah ini penting:**
Menyimpan dokumentasi di repository (bukan di Word/Google Docs terpisah) memastikan requirements **selalu up-to-date** dan **berversi** — kita bisa melihat bagaimana requirements berevolusi dari waktu ke waktu.

**Instruksi:**

1. Verifikasi semua file:

```bash
ls -la docs/
```

Expected output:

```
stakeholder-analysis.md
requirements-list.md
SRS.md
requirements-validation.md
traceability-matrix.md
git-workflow.md  (dari Lab 2)
```

2. Cek git log:

```bash
git log --oneline
```

Expected output (5 commits di branch ini):

```
abc1234 docs(requirements): add requirements traceability matrix
def5678 docs(requirements): add SMART validation for all requirements
ghi9012 docs(requirements): create SRS document following IEEE 830 template
jkl3456 docs(requirements): define 14 functional and 8 non-functional requirements
mno7890 docs(requirements): add stakeholder analysis for Perpustakaan Digital UAI
```

3. Push branch:

```bash
git push -u origin feature/srs-document
```

4. Buat Pull Request di GitHub:
   - **Base:** `develop`
   - **Compare:** `feature/srs-document`
   - **Title:** `docs(requirements): add complete SRS documentation for Perpustakaan Digital UAI`
   - **Description:**

```markdown
## Ringkasan

Menambahkan dokumentasi requirements lengkap untuk Sistem Perpustakaan Digital UAI mengikuti standar IEEE 830.

## Dokumen yang Ditambahkan

- `docs/stakeholder-analysis.md` — Analisis 6 stakeholder dengan matriks pengaruh-kepentingan
- `docs/requirements-list.md` — 14 Functional Requirements + 8 Non-Functional Requirements
- `docs/SRS.md` — Software Requirements Specification lengkap (IEEE 830)
- `docs/requirements-validation.md` — Validasi SMART (82% pass rate)
- `docs/traceability-matrix.md` — Requirements Traceability Matrix

## Checklist

- [x] Stakeholder teridentifikasi (6 stakeholder)
- [x] 14 FR + 8 NFR terdokumentasi
- [x] SRS mengikuti template IEEE 830
- [x] Validasi SMART dilakukan
- [x] Traceability matrix lengkap
```

5. Merge PR setelah review

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| "Branch has conflicts" | Pull `develop` terbaru: `git pull origin develop`, resolve conflict, push ulang |
| Lupa commit salah satu file | `git add docs/<file>` lalu `git commit --amend` |

---

## Tantangan Tambahan

### Tantangan 1: Use Case Narrative (Basic)

Tulis **use case narrative** lengkap untuk FR-03 (Peminjaman Buku Online) dengan format:

| Komponen | Isi |
|----------|-----|
| Use Case ID | UC-03 |
| Nama | Peminjaman Buku Online |
| Aktor | Mahasiswa, Pustakawan |
| Precondition | Mahasiswa sudah login, buku tersedia |
| Main Flow | 1. Mahasiswa pilih buku... 2. ... |
| Alternative Flow | Buku tidak tersedia... |
| Postcondition | Record peminjaman tercatat |

Simpan di `docs/use-cases/UC-03-peminjaman-buku.md`.

### Tantangan 2: Glossary dan Data Dictionary (Intermediate)

Buat **data dictionary** untuk entitas utama sistem (Buku, User, Peminjaman) yang mendefinisikan setiap field/atribut, tipe data, constraint, dan contoh nilai. Simpan di `docs/data-dictionary.md`.

Contoh format:

| Entitas | Field | Tipe | Constraint | Contoh |
|---------|-------|------|-----------|--------|
| Buku | judul | VARCHAR(200) | NOT NULL | "Clean Code" |

### Tantangan 3: Analisis Risiko Requirements (Advanced)

Identifikasi 5 risiko terkait requirements yang sudah didefinisikan dan buat **risk mitigation plan**:

| Risiko | Probabilitas | Dampak | Mitigasi |
|--------|-------------|--------|----------|
| Stakeholder berubah pikiran tentang FR | Tinggi | Tinggi | Iterasi requirements setiap sprint |

Simpan di `docs/risk-analysis.md`.

---

## Refleksi & AI Usage Log

Setelah menyelesaikan praktikum, isi tabel berikut di laporan Anda:

| No | Tanggal | Tool AI | Prompt yang Diberikan | Output AI | Modifikasi yang Dilakukan | Refleksi Pembelajaran |
|----|---------|---------|----------------------|-----------|--------------------------|----------------------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

**Panduan pengisian:**
- **Tool AI:** ChatGPT, Claude, GitHub Copilot, dll.
- **Prompt:** Apa yang Anda tanyakan ke AI
- **Output AI:** Ringkasan jawaban yang diberikan AI
- **Modifikasi:** Perubahan yang Anda lakukan terhadap output AI
- **Refleksi:** Apa yang Anda pelajari dari interaksi ini

> Kejujuran dalam mencatat penggunaan AI adalah bagian dari nilai **Amanah** yang dijunjung tinggi di UAI.

---

## Checklist Penyelesaian

- [ ] Branch `feature/srs-document` dibuat dari `develop`
- [ ] File `docs/stakeholder-analysis.md` lengkap dengan 6 stakeholder dan matriks pengaruh-kepentingan
- [ ] File `docs/requirements-list.md` berisi minimal 14 FR dan 8 NFR
- [ ] File `docs/SRS.md` mengikuti template IEEE 830 (4 section utama)
- [ ] Setiap FR memiliki ID, deskripsi, prioritas (MoSCoW), dan stakeholder
- [ ] Setiap NFR memiliki metrik yang terukur
- [ ] Validasi SMART dilakukan untuk semua requirements
- [ ] Requirements Traceability Matrix menghubungkan requirement ke sprint dan test case
- [ ] Minimal 5 conventional commits yang deskriptif
- [ ] Pull Request dibuat dan di-merge ke `develop`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
