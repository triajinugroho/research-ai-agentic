# Lab 03: Requirements Elicitation dan Dokumentasi SRS

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 3 dari 13 |
| **Topik** | Stakeholder Interview Role-Play, SRS IEEE 830, Requirements Validation |
| **CPMK** | CPMK-2 (Menerapkan teknik requirements engineering untuk menghasilkan dokumen kebutuhan yang lengkap) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 01-02 selesai, memahami konsep dasar requirements engineering dari modul Minggu 3 |

---

## Tujuan

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. **Menerapkan** (C3) teknik interview dan observation untuk elicitation requirements dari stakeholder
2. **Membedakan** (C4) functional requirements (FR) dan non-functional requirements (NFR) dengan metrik yang terukur
3. **Menyusun** (C6) dokumen Software Requirements Specification (SRS) sesuai standar IEEE 830
4. **Mengevaluasi** (C5) kualitas requirements menggunakan checklist validasi (jelas, testable, konsisten, lengkap)

---

## Konsep Singkat

### Apa itu Requirements Engineering?

Requirements Engineering (RE) adalah proses sistematis untuk menemukan, menganalisis, mendokumentasikan, dan memvalidasi kebutuhan perangkat lunak. RE merupakan fase **paling kritis** dalam SDLC -- kesalahan di fase ini berdampak 10-100x lebih mahal jika ditemukan di fase testing atau produksi.

```
Biaya Perbaikan Defect Berdasarkan Fase:

  100x │                                              ████
       │                                         ████ ████
   50x │                                    ████ ████ ████
       │                               ████ ████ ████ ████
   10x │                          ████ ████ ████ ████ ████
       │                     ████ ████ ████ ████ ████ ████
    5x │                ████ ████ ████ ████ ████ ████ ████
       │           ████ ████ ████ ████ ████ ████ ████ ████
    1x │      ████ ████ ████ ████ ████ ████ ████ ████ ████
       └──────────────────────────────────────────────────
         Req   Design  Code   Unit   Integ  System  Prod
                                Test   Test   Test
```

### Teknik Elicitation

| Teknik | Deskripsi | Kapan Digunakan |
|--------|-----------|----------------|
| **Interview** | Tanya jawab langsung dengan stakeholder | Memahami kebutuhan spesifik |
| **Observation** | Mengamati pengguna melakukan pekerjaan saat ini | Menemukan kebutuhan implisit |
| **Questionnaire** | Survei tertulis untuk banyak responden | Mengumpulkan data dari banyak user |
| **Prototyping** | Membuat mock-up untuk mendapat feedback | Stakeholder sulit menjelaskan kebutuhan |
| **Document Analysis** | Mempelajari sistem/dokumen yang ada | Ada sistem lama yang akan diganti |
| **Brainstorming** | Diskusi kelompok untuk menemukan ide | Tahap awal eksplorasi kebutuhan |

### Functional vs Non-Functional Requirements

```
Requirements Classification:

  Requirements
  ├── Functional Requirements (FR)
  │   ├── "Sistem HARUS bisa [aksi]"
  │   ├── Contoh: Sistem harus memungkinkan login dengan NIM
  │   └── Contoh: Sistem harus menampilkan daftar buku yang tersedia
  │
  └── Non-Functional Requirements (NFR)
      ├── Performance: "Halaman load dalam < 3 detik"
      ├── Security: "Password di-hash dengan bcrypt"
      ├── Usability: "User baru bisa pakai dalam 5 menit"
      ├── Reliability: "Uptime 99.5%"
      └── Scalability: "Support 1000 concurrent users"
```

### Standar IEEE 830 untuk SRS

IEEE 830 adalah standar industri untuk penulisan SRS. Struktur utamanya:

1. **Pendahuluan** -- tujuan, ruang lingkup, definisi, referensi
2. **Deskripsi Umum** -- perspektif produk, fungsi produk, karakteristik pengguna, batasan
3. **Kebutuhan Spesifik** -- FR, NFR, interface requirements
4. **Lampiran** -- diagram, model data

> **Referensi:** Materi lengkap tersedia di modul Minggu 3 (`week-03`) dan Bab 3 Buku Ajar.

---

## Persiapan

| Kebutuhan | Detail |
|-----------|--------|
| Partner | Minimal 1 partner untuk role-play interview |
| Template SRS | Akan dibuat di Langkah 4 (ikuti template IEEE 830) |
| Skenario | Sistem Perpustakaan Digital UAI (sama dengan Lab 02) |
| Repository | Repository GitHub dari Lab 01-02 |

---

## Langkah-langkah

### Langkah 1: Persiapan Role-Play -- Memahami Stakeholder (10 menit)

**Mengapa:** Sebelum interview, seorang analyst harus memahami siapa stakeholder-nya, apa perannya, dan apa yang mungkin menjadi kebutuhannya. Persiapan yang baik menghasilkan interview yang lebih produktif.

**Instruksi:**

1. Berpasangan dalam tim. Tentukan peran:
   - **Analyst** (pewawancara): Bertugas menggali kebutuhan
   - **Stakeholder** (narasumber): Memerankan salah satu peran berikut

2. Pilih stakeholder yang akan diperankan:

| Stakeholder | Latar Belakang | Kebutuhan Utama |
|-------------|----------------|----------------|
| **Pustakawan** | Bekerja 5 tahun, frustrasi dengan sistem manual | Efisiensi, laporan otomatis |
| **Mahasiswa** | Semester 4, sering tidak menemukan buku | Pencarian mudah, stok real-time |
| **Kepala Perpustakaan** | Bertanggung jawab atas anggaran dan kebijakan | Dashboard statistik, laporan |
| **Admin IT** | Mengelola server dan keamanan kampus | Keamanan, backup, maintenance |

3. Stakeholder mempelajari karakternya (2 menit) dan menyiapkan jawaban berdasarkan pengalaman yang dibayangkan

4. Analyst menyiapkan daftar pertanyaan interview (minimal 8 pertanyaan)

**Expected Output:** Masing-masing tahu perannya dan analyst punya daftar pertanyaan.

---

### Langkah 2: Role-Play Interview Stakeholder (25 menit)

**Mengapa:** Interview adalah teknik elicitation paling umum dan efektif. Latihan ini melatih kemampuan bertanya, mendengarkan aktif, dan menangkap kebutuhan yang sering tidak eksplisit.

**Instruksi:**

**Ronde 1 (12 menit):** Analyst mewawancarai stakeholder.

Contoh pertanyaan yang baik (terbuka, tidak leading):

```markdown
## Interview Script - Sistem Perpustakaan Digital

### Pertanyaan Pembuka (membangun rapport)
1. "Bisa ceritakan tentang pekerjaan Anda sehari-hari di perpustakaan?"
2. "Sudah berapa lama Anda bekerja di sini?"

### Pertanyaan Proses Saat Ini
3. "Bagaimana proses peminjaman buku saat ini dari awal hingga akhir?"
4. "Bisa ceritakan situasi terakhir saat ada masalah dengan proses peminjaman?"
5. "Berapa banyak transaksi peminjaman per hari rata-rata?"

### Pertanyaan Kebutuhan
6. "Jika bisa mengubah satu hal dari sistem saat ini, apa yang akan Anda ubah?"
7. "Fitur apa yang paling penting untuk pekerjaan Anda?"
8. "Bagaimana Anda ingin mendapat notifikasi tentang buku terlambat?"

### Pertanyaan Batasan
9. "Berapa banyak buku dan pengguna yang harus didukung sistem?"
10. "Apakah ada aturan khusus tentang batas peminjaman atau denda?"
11. "Apakah sistem harus bisa diakses dari luar kampus?"

### Pertanyaan Penutup
12. "Ada hal lain yang belum saya tanyakan tapi penting untuk Anda?"
```

**Ronde 2 (12 menit):** Tukar peran -- analyst jadi stakeholder (peran berbeda), stakeholder jadi analyst.

**Tips Interview:**
- **Dengarkan aktif** -- jangan langsung menulis, pahami dulu
- **Tanyakan "Mengapa?"** -- gali motivasi di balik permintaan fitur
- **Perhatikan kebutuhan implisit** -- apa yang TIDAK dikatakan tapi tersirat
- **Catat pain points** -- masalah yang dikeluhkan sering jadi FR prioritas tinggi

Catat hasil interview di file `docs/interview-notes.md`:

```markdown
# Hasil Interview - Stakeholder: [Peran]

**Interviewer:** [Nama]
**Narasumber:** [Nama] (sebagai [Peran])
**Tanggal:** [Tanggal]
**Durasi:** 12 menit

## Rangkuman
[2-3 kalimat rangkuman kebutuhan utama]

## Catatan Detail

| No | Pertanyaan | Jawaban | Insight |
|----|-----------|---------|---------|
| 1 | Bagaimana proses peminjaman saat ini? | "Mahasiswa datang, isi form kertas, ..." | Proses manual, rawan error |
| 2 | Masalah utama? | "Buku sering hilang, tidak tahu siapa yang pinjam" | Butuh tracking peminjaman |
| ... | ... | ... | ... |

## Kebutuhan yang Teridentifikasi
1. [Kebutuhan 1]
2. [Kebutuhan 2]
3. ...

## Kebutuhan Implisit (yang tersirat tapi tidak langsung dikatakan)
1. [Kebutuhan implisit 1]
2. [Kebutuhan implisit 2]
```

**Expected Output:** Catatan interview minimal 8 pertanyaan-jawaban dengan insight.

**Estimasi waktu:** 25 menit (termasuk tukar peran)

> **Troubleshooting:** Jika stakeholder "kehabisan jawaban", ingatkan bahwa boleh berimprovisasi berdasarkan pengalaman pribadi menggunakan perpustakaan. Yang penting adalah melatih proses interview, bukan keakuratan jawaban.

---

### Langkah 3: Identifikasi dan Klasifikasi Requirements (15 menit)

**Mengapa:** Dari hasil interview yang mentah, analyst harus mengekstrak requirements yang terstruktur dan terukur. Kemampuan mengubah bahasa natural menjadi requirements formal adalah keterampilan kunci seorang requirements engineer.

**Instruksi:**

Dari hasil interview kedua ronde, identifikasi dan tulis:

**10 Functional Requirements:**

```markdown
## Functional Requirements

| ID | Deskripsi | Sumber | Prioritas | Testable? |
|----|-----------|--------|-----------|-----------|
| FR-01 | Sistem harus memungkinkan mahasiswa login menggunakan NIM dan password | Interview Pustakawan | Must | Ya: login berhasil/gagal |
| FR-02 | Sistem harus menampilkan katalog buku dengan fitur pencarian berdasarkan judul, penulis, atau ISBN | Interview Mahasiswa | Must | Ya: hasil pencarian sesuai keyword |
| FR-03 | Sistem harus memproses peminjaman buku dan mengurangi stok otomatis | Interview Pustakawan | Must | Ya: stok berkurang setelah pinjam |
| FR-04 | Sistem harus mengirim notifikasi H-3 dan H-1 sebelum deadline pengembalian | Interview Pustakawan | Should | Ya: notifikasi terkirim pada waktu yang tepat |
| FR-05 | Sistem harus menampilkan riwayat peminjaman mahasiswa | Interview Mahasiswa | Should | Ya: daftar peminjaman muncul |
| FR-06 | Sistem harus menghitung denda otomatis untuk keterlambatan (Rp 1.000/hari) | Interview Kep. Perpustakaan | Must | Ya: denda sesuai jumlah hari |
| FR-07 | Sistem harus menyediakan dashboard statistik peminjaman bulanan | Interview Kep. Perpustakaan | Should | Ya: grafik/tabel statistik muncul |
| FR-08 | Pustakawan harus bisa menambah, mengedit, dan menghapus data buku | Interview Pustakawan | Must | Ya: CRUD buku berfungsi |
| FR-09 | Sistem harus mendukung pencarian buku berdasarkan kategori | Interview Mahasiswa | Could | Ya: filter kategori berfungsi |
| FR-10 | Sistem harus menampilkan ketersediaan buku secara real-time | Interview Mahasiswa | Must | Ya: stok akurat setelah transaksi |
```

**5 Non-Functional Requirements (dengan metrik terukur):**

```markdown
## Non-Functional Requirements

| ID | Kategori | Deskripsi | Metrik | Target |
|----|----------|-----------|--------|--------|
| NFR-01 | Performance | Waktu loading halaman | Response time | < 3 detik |
| NFR-02 | Security | Password pengguna harus ter-enkripsi | Algoritma hash | bcrypt dengan salt |
| NFR-03 | Usability | User baru bisa menyelesaikan peminjaman | Task completion time | < 5 menit tanpa bantuan |
| NFR-04 | Reliability | Sistem tersedia selama jam operasional | Uptime | 99% (Senin-Sabtu, 07:00-21:00) |
| NFR-05 | Scalability | Jumlah pengguna concurrent | Concurrent users | 200 users bersamaan |
```

**Diskusi kelas (5 menit):** Apa perbedaan antara "Sistem harus cepat" (buruk) dan "Halaman loading < 3 detik" (baik)? Mengapa metrik penting dalam NFR?

**Expected Output:** Tabel FR dan NFR yang terstruktur dengan ID, prioritas, dan indikator testability.

**Estimasi waktu:** 15 menit

---

### Langkah 4: Tulis Dokumen SRS (25 menit)

**Mengapa:** SRS adalah dokumen kontrak antara tim development dan stakeholder. Dokumen yang jelas dan lengkap mengurangi ambiguitas dan menjadi acuan saat development dan testing.

**Instruksi:**

Buat file `docs/srs.md` mengikuti template IEEE 830:

```markdown
# Software Requirements Specification (SRS)
## Sistem Perpustakaan Digital - Universitas Al Azhar Indonesia

**Versi:** 1.0
**Tanggal:** [Tanggal]
**Tim:** [Nama Tim]

---

## 1. Pendahuluan

### 1.1 Tujuan
Dokumen ini menjelaskan kebutuhan perangkat lunak untuk Sistem Perpustakaan
Digital Universitas Al Azhar Indonesia yang akan menggantikan proses manual
peminjaman dan pengelolaan buku.

### 1.2 Ruang Lingkup
Sistem ini mencakup:
- Manajemen katalog buku (CRUD)
- Proses peminjaman dan pengembalian buku
- Pencarian dan filter buku
- Notifikasi dan pelaporan
Sistem ini TIDAK mencakup:
- Pembelian buku online
- Manajemen perpustakaan antar-kampus

### 1.3 Definisi dan Akronim
| Istilah | Definisi |
|---------|----------|
| NIM | Nomor Induk Mahasiswa |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| CRUD | Create, Read, Update, Delete |

### 1.4 Referensi
- IEEE 830-1998: Recommended Practice for Software Requirements Specifications
- Buku Ajar RPL Bab 3: Requirements Engineering

---

## 2. Deskripsi Umum

### 2.1 Perspektif Produk
Sistem ini adalah aplikasi web yang berdiri sendiri (standalone), menggantikan
sistem pencatatan manual yang saat ini digunakan perpustakaan UAI.

### 2.2 Fungsi Produk
[Daftar fungsi utama sistem - rangkuman dari FR]

### 2.3 Karakteristik Pengguna
| Pengguna | Jumlah | Latar Belakang | Frekuensi Penggunaan |
|----------|--------|----------------|---------------------|
| Mahasiswa | ~3000 | Familiar dengan teknologi | Harian |
| Pustakawan | 5 | Bervariasi, perlu training | Harian |
| Admin | 1 | IT background | Mingguan |

### 2.4 Batasan
- Sistem harus berjalan di browser modern (Chrome, Firefox, Safari)
- Budget development terbatas (proyek akademik)
- Waktu pengembangan: 1 semester

### 2.5 Asumsi dan Dependensi
- Setiap mahasiswa sudah memiliki NIM aktif
- Koneksi internet tersedia di kampus
- Data buku awal akan diimport dari spreadsheet yang ada

---

## 3. Kebutuhan Spesifik

### 3.1 Functional Requirements
[Salin tabel FR dari Langkah 3]

### 3.2 Non-Functional Requirements
[Salin tabel NFR dari Langkah 3]

### 3.3 Interface Requirements

#### 3.3.1 User Interface
- Responsive design (desktop + mobile)
- Bahasa Indonesia sebagai bahasa utama
- Konsisten dengan branding UAI

#### 3.3.2 API Interface
- RESTful API untuk komunikasi frontend-backend
- Format data: JSON
- Authentication: JWT token

#### 3.3.3 Database Interface
- SQLite untuk development, PostgreSQL untuk production
- Backup otomatis harian

---

## 4. Lampiran
- [Link ke class diagram]
- [Link ke wireframe/mockup]
```

Commit file SRS:

```bash
git add docs/srs.md
git commit -m "docs: buat dokumen SRS IEEE 830 untuk sistem perpustakaan"
git push origin main
```

**Expected Output:** File `docs/srs.md` lengkap dengan 4 section utama IEEE 830.

**Estimasi waktu:** 25 menit

> **Tips:** Tidak perlu sempurna di iterasi pertama. SRS adalah living document yang akan diperbarui seiring pemahaman bertambah. Yang penting strukturnya benar dan requirements-nya jelas.

---

### Langkah 5: Validasi Requirements (15 menit)

**Mengapa:** Requirements yang buruk (ambigu, tidak testable, tidak konsisten) menyebabkan mayoritas kegagalan proyek software. Validasi memastikan kualitas requirements sebelum development dimulai.

**Instruksi:**

Tukarkan SRS dengan tim lain. Reviewer menggunakan checklist berikut untuk mengevaluasi setiap requirement:

```markdown
## Checklist Validasi Requirements

Untuk setiap requirement, periksa 4 kriteria kualitas:

### Clarity (Kejelasan)
- [ ] Apakah requirement bisa dipahami tanpa penjelasan tambahan?
- [ ] Apakah tidak ada kata ambigu ("cepat", "mudah", "banyak")?
- [ ] Apakah hanya ada SATU interpretasi yang mungkin?

### Testability (Bisa Diuji)
- [ ] Apakah bisa dibuat test case untuk memverifikasi requirement ini?
- [ ] Apakah ada metrik yang terukur (angka, kondisi)?

### Consistency (Konsistensi)
- [ ] Apakah requirement ini tidak bertentangan dengan requirement lain?
- [ ] Apakah terminologi konsisten di seluruh dokumen?

### Completeness (Kelengkapan)
- [ ] Apakah semua skenario sudah tercakup (termasuk error handling)?
- [ ] Apakah ada kebutuhan yang tersirat tapi belum ditulis?
```

**Contoh evaluasi:**

| ID | Requirement | Clarity | Testable | Consistent | Complete | Catatan |
|----|------------|---------|----------|------------|----------|---------|
| FR-01 | Login dengan NIM | OK | OK | OK | Kurang | Bagaimana jika NIM salah? Error message? |
| FR-04 | Notifikasi sebelum deadline | Ambigu | Kurang | OK | Kurang | "Sebelum" = berapa hari? Via apa (email, web)? |
| NFR-01 | Halaman loading cepat | Ambigu | Kurang | OK | OK | "Cepat" = berapa detik? Di jaringan apa? |

Berikan **minimal 5 komentar perbaikan** yang konstruktif kepada tim lain.

Setelah menerima feedback, perbaiki SRS dan commit:

```bash
git add docs/srs.md
git commit -m "docs: perbaiki SRS berdasarkan feedback validasi"
git push origin main
```

**Expected Output:** SRS yang telah divalidasi dengan catatan perbaikan, minimal 5 requirements diperbaiki.

**Estimasi waktu:** 15 menit

> **Diskusi kelas:** Dari pengalaman validasi, requirement mana yang paling sering bermasalah? Mengapa NFR cenderung lebih sulit ditulis dengan baik dibanding FR?

---

### Langkah 6: Traceability Matrix (10 menit)

**Mengapa:** Traceability matrix menghubungkan setiap requirement ke stakeholder (asal kebutuhan), test case (validasi), dan komponen sistem (implementasi). Ini memastikan tidak ada requirement yang "hilang" selama development.

**Instruksi:**

Buat Requirements Traceability Matrix (RTM) sederhana:

```markdown
## Requirements Traceability Matrix

| Req ID | Deskripsi | Stakeholder | User Story | Test Case | Status |
|--------|-----------|-------------|-----------|-----------|--------|
| FR-01 | Login NIM | Pustakawan | US-01 | TC-01 | Draft |
| FR-02 | Pencarian buku | Mahasiswa | US-02 | TC-02 | Draft |
| FR-03 | Peminjaman buku | Pustakawan | US-03 | TC-03 | Draft |
| FR-06 | Hitung denda | Kep. Perpus | US-06 | TC-06 | Draft |
| NFR-01 | Response < 3s | Admin IT | - | TC-P01 | Draft |
| NFR-02 | Password hash | Admin IT | - | TC-S01 | Draft |
```

Commit:

```bash
git add docs/srs.md
git commit -m "docs: tambah traceability matrix ke SRS"
git push origin main
```

**Expected Output:** Tabel RTM yang menghubungkan requirements ke stakeholder dan test case.

---

## Tantangan Tambahan

### Tantangan 1: Dasar
Tambahkan **Use Case Narrative** untuk 2 use case utama (Login dan Peminjaman Buku). Setiap narrative harus memiliki: aktor, precondition, main flow (5+ langkah), alternative flow, postcondition, dan exception.

### Tantangan 2: Menengah
Buat **interview script** untuk stakeholder kedua (Mahasiswa). Lakukan interview role-play, identifikasi requirements yang berbeda dari perspektif mahasiswa vs pustakawan, lalu update SRS dengan requirements baru. Perhatikan apakah ada requirements yang berkonflik antara kedua stakeholder.

### Tantangan 3: Lanjutan
Buat analisis **BPJS Kesehatan** atau **Sistem Akademik UAI** sebagai studi kasus requirements complexity. Identifikasi minimal 5 stakeholder, gambarkan stakeholder matrix (influence vs interest), dan jelaskan tantangan elicitation pada sistem berskala besar dengan banyak stakeholder yang kebutuhannya saling bertentangan.

---

## Refleksi & AI Usage Log

Sebelum meninggalkan lab, isi refleksi berikut di file `docs/refleksi-lab-03.md`:

1. **Apa perbedaan antara kebutuhan yang dikatakan stakeholder vs kebutuhan sebenarnya?**
2. **Requirement mana yang paling sulit ditulis? FR atau NFR? Mengapa?**
3. **Apa yang akan Anda lakukan berbeda jika mengulang interview?**

Jika menggunakan AI selama lab, catat di **AI Usage Log**:

| Prompt yang Diberikan | Output AI | Modifikasi yang Dilakukan | Refleksi |
|----------------------|-----------|--------------------------|----------|
| (contoh prompt) | (ringkasan output) | (apa yang diubah) | (apa yang dipelajari) |

---

## Checklist Penyelesaian

- [ ] Interview role-play dilakukan (2 ronde, tukar peran)
- [ ] Catatan interview tercatat di `docs/interview-notes.md` dengan minimal 8 pertanyaan-jawaban
- [ ] 10 Functional Requirements terdokumentasi dengan ID, deskripsi, prioritas, dan testability
- [ ] 5 Non-Functional Requirements terdokumentasi dengan kategori dan metrik terukur
- [ ] Dokumen SRS (`docs/srs.md`) mengikuti struktur IEEE 830 dengan 4 section utama
- [ ] Validasi dilakukan oleh tim lain dengan checklist (minimal 5 komentar perbaikan)
- [ ] SRS diperbaiki berdasarkan feedback validasi
- [ ] Traceability matrix menghubungkan requirements ke stakeholder dan test case
- [ ] Semua file di-commit dan push ke repository
- [ ] File refleksi `docs/refleksi-lab-03.md` terisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
