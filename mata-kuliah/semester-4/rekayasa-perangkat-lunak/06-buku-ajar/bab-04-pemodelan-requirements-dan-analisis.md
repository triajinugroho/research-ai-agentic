# BAB 4: PEMODELAN REQUIREMENTS DAN ANALISIS

**Tri Aji Nugroho, S.T., M.T.**
Rekayasa Perangkat Lunak (IF2205) — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Level Bloom | Estimasi Waktu |
|-----------|-----------|-------------|----------------|
| 2.3 | Membuat Use Case Diagram dan Use Case Narrative untuk memodelkan requirements | C3 (Menerapkan) | 90 menit |
| 2.4 | Menulis User Stories dengan kriteria INVEST dan Acceptance Criteria format Given-When-Then | C3 (Menerapkan) | 90 menit |

---

## Estimasi Waktu

| Aktivitas | Durasi |
|-----------|--------|
| Membaca materi | 120 menit |
| Praktik use case & user stories | 90 menit |
| Mengerjakan latihan soal | 60 menit |
| Eksplorasi AI Corner | 30 menit |
| **Total** | **5 jam** |

---

## Prasyarat

- Bab 3: Requirements Engineering (elicitation, SRS, jenis requirements)
- Pemahaman dasar tentang Agile/Scrum (Bab 2)
- Kemampuan berpikir analitis untuk memodelkan proses bisnis

---

## Peta Konsep Bab

```
                    ┌──────────────────────────────────┐
                    │  PEMODELAN REQUIREMENTS & ANALISIS │
                    └──────────────┬───────────────────┘
                                   │
            ┌──────────────────────┼──────────────────────┐
            │                      │                      │
            ▼                      ▼                      ▼
  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
  │   USE CASE       │  │   USER STORIES   │  │  PRODUCT BACKLOG │
  │   MODELING       │  │   & ACCEPTANCE   │  │  & PRIORITISASI  │
  │                  │  │   CRITERIA       │  │                  │
  │ UC Diagram       │  │ Format "As a..." │  │ Backlog Mgmt     │
  │ UC Narrative     │  │ INVEST Criteria  │  │ MoSCoW Method    │
  │ Actor Ident.     │  │ Given-When-Then  │  │ Story Points     │
  │ Include/Extend   │  │ Story Splitting  │  │ Planning Poker   │
  │ Generalization   │  │ Epic → Stories   │  │ User Story Map   │
  └──────────────────┘  └──────────────────┘  └──────────────────┘
```

---

## 4.1 Use Case Modeling

### 4.1.1 Apa Itu Use Case?

Use Case adalah teknik untuk memodelkan interaksi antara pengguna (*actor*) dan sistem. Use Case menggambarkan **APA** yang bisa dilakukan pengguna, bukan **BAGAIMANA** sistem mengimplementasikannya secara internal.

Use Case pertama kali diperkenalkan oleh **Ivar Jacobson** (1992) dan menjadi bagian integral dari **UML (Unified Modeling Language)**. Use Case digunakan secara luas baik dalam metodologi tradisional (Waterfall, RUP) maupun sebagai pelengkap user stories di Agile.

**Kapan menggunakan Use Case?**

| Situasi | Gunakan Use Case? | Alasan |
|---------|-------------------|--------|
| Proyek besar, banyak stakeholder | Ya | Memberikan gambaran visual yang mudah dipahami semua pihak |
| Sistem dengan interaksi kompleks | Ya | Memperjelas alur interaksi dan relationships |
| Proyek Agile sederhana | Opsional | User stories mungkin cukup, tapi UC Diagram tetap berguna |
| Dokumentasi formal diperlukan | Ya | Standar UML diakui secara internasional |
| Komunikasi dengan non-teknis | Ya | Diagram visual lebih mudah dipahami dari teks |

### 4.1.2 Komponen Use Case Diagram

Use Case Diagram memiliki **7 elemen utama**:

| Elemen | Simbol | Deskripsi | Contoh |
|--------|--------|-----------|--------|
| **Actor** | Stick figure | Entitas yang berinteraksi dengan sistem (bisa manusia, sistem lain, atau waktu) | Mahasiswa, Pustakawan, Payment Gateway |
| **Use Case** | Ellipse (oval) | Satu fungsi atau layanan yang disediakan sistem | Cari Buku, Pinjam Buku |
| **System Boundary** | Rectangle | Batas dari sistem yang dimodelkan | Sistem Perpustakaan Digital |
| **Association** | Garis lurus | Hubungan antara actor dan use case | Mahasiswa --- Cari Buku |
| **Include** | `<<include>>` dashed arrow | Use case yang **wajib** dipanggil oleh use case lain | Login <<include>> Validasi Password |
| **Extend** | `<<extend>>` dashed arrow | Use case **opsional** yang memperluas use case lain | Pinjam Buku <<extend>> Kirim Notifikasi |
| **Generalization** | Solid arrow dengan triangle | Inheritance antar actor atau antar use case | Mahasiswa/Dosen → Anggota |

### 4.1.3 Identifikasi Actor

Actor adalah siapa saja (atau apa saja) yang berinteraksi dengan sistem dari **luar system boundary**.

**Langkah identifikasi actor:**

```
1. Siapa yang MENGGUNAKAN sistem?
   → Mahasiswa, Pustakawan, Dosen

2. Siapa yang MENDAPAT informasi dari sistem?
   → Kepala Perpustakaan (laporan)

3. Siapa yang MEMBERIKAN data ke sistem?
   → Admin (data buku baru)

4. Sistem LAIN yang berinteraksi?
   → Sistem Akademik UAI, Email Server

5. Apakah ada TRIGGER berbasis waktu?
   → Scheduler (kirim reminder otomatis)
```

**Jenis Actor:**

| Jenis | Penjelasan | Contoh |
|-------|-----------|--------|
| **Primary Actor** | Memulai interaksi, mendapatkan nilai dari sistem | Mahasiswa meminjam buku |
| **Secondary Actor** | Mendukung atau dilayani oleh sistem | Email Server mengirim notifikasi |
| **Abstract Actor** | Generalisasi dari beberapa actor konkret | "Anggota" → Mahasiswa, Dosen |

**Contoh Identifikasi Actor — Perpustakaan Digital UAI:**

```
┌─────────────────────────────────────────────────────┐
│            ACTOR IDENTIFICATION TABLE                │
├───────────────────┬─────────────┬───────────────────┤
│ Actor             │ Jenis       │ Interaksi Utama   │
├───────────────────┼─────────────┼───────────────────┤
│ Mahasiswa         │ Primary     │ Cari, pinjam,     │
│                   │             │ perpanjang buku   │
│ Dosen             │ Primary     │ Cari, pinjam,     │
│                   │             │ request buku baru │
│ Pustakawan        │ Primary     │ Kelola katalog,   │
│                   │             │ proses peminjaman │
│ Admin IT          │ Secondary   │ Kelola user,      │
│                   │             │ backup database   │
│ Kepala Perpust.   │ Secondary   │ Lihat laporan     │
│ Sistem Akademik   │ External    │ Verifikasi NIM    │
│ Email Server      │ External    │ Kirim notifikasi  │
│ Scheduler (Cron)  │ Time-based  │ Trigger reminder  │
└───────────────────┴─────────────┴───────────────────┘
```

### 4.1.4 Include vs Extend — Penjelasan Detail

Banyak mahasiswa bingung membedakan `<<include>>` dan `<<extend>>`. Berikut penjelasan detailnya:

```
<<INCLUDE>> — WAJIB (Mandatory)
══════════════════════════════════════════════════
Use Case A ──<<include>>──▶ Use Case B

"Use Case A SELALU memanggil Use Case B"
"B adalah bagian WAJIB dari A"

Contoh:
  Pinjam Buku ──<<include>>──▶ Validasi Keanggotaan
  (Setiap peminjaman PASTI memvalidasi keanggotaan)


<<EXTEND>> — OPSIONAL (Optional/Conditional)
══════════════════════════════════════════════════
Use Case A ◀──<<extend>>── Use Case B

"Use Case B KADANG-KADANG memperluas Use Case A"
"B hanya terjadi jika kondisi tertentu terpenuhi"

Contoh:
  Pinjam Buku ◀──<<extend>>── Kirim Notifikasi WhatsApp
  (Notifikasi hanya dikirim JIKA mahasiswa mengaktifkan 
   fitur notifikasi)
```

**Tabel Perbandingan:**

| Aspek | <<include>> | <<extend>> |
|-------|-------------|------------|
| **Sifat** | Wajib (mandatory) | Opsional (conditional) |
| **Arah panah** | Base → Included | Extension → Base |
| **Kapan digunakan** | Menghindari duplikasi logic | Menambah perilaku opsional |
| **Analogi** | "Selalu dilakukan" | "Kadang dilakukan, jika..." |
| **Contoh** | Login include Validasi | Checkout extend Pakai Kupon |

### 4.1.5 Contoh Lengkap: Use Case Diagram Perpustakaan Digital UAI

```
┌──────────────── Sistem Perpustakaan Digital UAI ──────────────────┐
│                                                                    │
│  ┌────────────┐                                                    │
│  │  Anggota   │◄─────────────────────────────────┐                │
│  │ (abstract) │                                   │ generalization │
│  └──────┬─────┘                                   │                │
│         │                                    ┌────┴────┐           │
│         │            ┌─────────────────┐     │  Dosen  │           │
│         ├───────────▶│  Cari Buku      │     └─────────┘           │
│         │            └─────────────────┘                           │
│         │            ┌─────────────────┐     ┌─────────────────┐   │
│         ├───────────▶│  Pinjam Buku    │────▶│ Validasi        │   │
│         │            └────────┬────────┘     │ Keanggotaan     │   │
│         │                     │  <<include>> └─────────────────┘   │
│         │                     │                                    │
│         │            ┌────────┴────────┐                           │
│         │            │  Kirim          │                           │
│         │            │  Notifikasi     │  <<extend>>               │
│         │            └─────────────────┘                           │
│         │            ┌─────────────────┐                           │
│         ├───────────▶│  Perpanjang     │                           │
│         │            │  Peminjaman     │                           │
│         │            └─────────────────┘                           │
│         │            ┌─────────────────┐                           │
│         └───────────▶│  Lihat Riwayat  │                           │
│                      │  Peminjaman     │                           │
│                      └─────────────────┘                           │
│                                                                    │
│  ┌────────────┐      ┌─────────────────┐                           │
│  │ Mahasiswa  │      │                 │                           │
│  └────────────┘      │                 │                           │
│     (inherits        │                 │                           │
│      Anggota)        │                 │                           │
│                      │                 │                           │
│  ┌────────────┐      ┌─────────────────┐                           │
│  │Pustakawan  │─────▶│  Kelola Katalog │                           │
│  └──────┬─────┘      └─────────────────┘                           │
│         │            ┌─────────────────┐     ┌─────────────────┐   │
│         ├───────────▶│  Proses         │────▶│ Update Stok     │   │
│         │            │  Pengembalian   │     │ Buku            │   │
│         │            └─────────────────┘     └─────────────────┘   │
│         │             <<include>>                                   │
│         │            ┌─────────────────┐                           │
│         └───────────▶│  Lihat Laporan  │                           │
│                      │  Statistik      │                           │
│                      └─────────────────┘                           │
│                                                                    │
│  ┌────────────┐      ┌─────────────────┐                           │
│  │  Admin IT  │─────▶│  Kelola User    │                           │
│  └──────┬─────┘      └─────────────────┘                           │
│         │            ┌─────────────────┐                           │
│         └───────────▶│  Backup Database│                           │
│                      └─────────────────┘                           │
│                                                                    │
│  ┌────────────┐      ┌─────────────────┐                           │
│  │  Scheduler │─────▶│  Kirim Reminder │                           │
│  │  (Cron)    │      │  Otomatis       │                           │
│  └────────────┘      └─────────────────┘                           │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

### 4.1.6 Use Case Narrative — Template Lengkap

Use Case Narrative mendetailkan **alur interaksi** dari setiap use case. Ini adalah deskripsi tekstual yang melengkapi diagram visual.

**Template Use Case Narrative:**

```
═══════════════════════════════════════════════════════════════
USE CASE NARRATIVE
═══════════════════════════════════════════════════════════════

Use Case ID    : UC-03
Use Case Name  : Pinjam Buku
Version        : 1.0
Last Updated   : 20 Maret 2026
Author         : Tim RE

─── INFORMASI UMUM ──────────────────────────────────────────

Actor(s)       : Mahasiswa (primary), Sistem Akademik (secondary)
Description    : Mahasiswa meminjam buku dari perpustakaan 
                 secara online
Trigger        : Mahasiswa mengklik tombol "Pinjam" pada 
                 halaman detail buku
Priority       : Must Have
Frequency      : ~50 transaksi per hari

─── PRECONDITIONS ───────────────────────────────────────────

PRE-1 : Mahasiswa sudah login ke sistem
PRE-2 : Mahasiswa memiliki status keanggotaan aktif
PRE-3 : Buku yang dipilih tersedia (stok > 0)
PRE-4 : Mahasiswa belum mencapai batas peminjaman (< 3 buku)

─── MAIN FLOW (Alur Utama / Happy Path) ────────────────────

1. Mahasiswa membuka halaman katalog buku
2. Mahasiswa mencari buku berdasarkan judul/penulis/ISBN
3. Sistem menampilkan daftar buku yang sesuai
4. Mahasiswa mengklik buku yang diinginkan
5. Sistem menampilkan detail buku (judul, penulis, ISBN, 
   lokasi rak, stok tersedia)
6. Mahasiswa mengklik tombol "Pinjam Buku"
7. Sistem memvalidasi keanggotaan mahasiswa [<<include>> 
   UC-01: Validasi Keanggotaan]
8. Sistem memvalidasi jumlah peminjaman aktif (< 3 buku)
9. Sistem mencatat transaksi peminjaman:
   - Tanggal pinjam: hari ini
   - Tanggal jatuh tempo: 14 hari dari hari ini
   - Status: "Dipinjam"
10. Sistem mengurangi stok buku (-1)
11. Sistem menampilkan konfirmasi peminjaman beserta 
    tanggal jatuh tempo
12. Sistem mengirim email konfirmasi ke mahasiswa
    [<<extend>> UC-07: Kirim Notifikasi]

─── ALTERNATIVE FLOWS ───────────────────────────────────────

ALT-1: Buku tidak tersedia (di langkah 5)
  5a. Sistem menampilkan "Stok habis - tersedia: 0"
  5b. Sistem menawarkan opsi "Reservasi Buku"
  5c. Jika mahasiswa memilih reservasi, 
      lanjut ke UC-06: Reservasi Buku
  5d. Jika tidak, kembali ke langkah 2

ALT-2: Pencarian tidak menemukan hasil (di langkah 3)
  3a. Sistem menampilkan "Buku tidak ditemukan"
  3b. Sistem menyarankan keyword alternatif
  3c. Kembali ke langkah 2

─── EXCEPTION FLOWS ─────────────────────────────────────────

EXC-1: Keanggotaan tidak aktif (di langkah 7)
  7a. Sistem menampilkan "Keanggotaan tidak aktif. 
      Silakan hubungi pustakawan."
  7b. Proses berhenti

EXC-2: Batas peminjaman tercapai (di langkah 8)
  8a. Sistem menampilkan "Anda sudah meminjam 3 buku. 
      Kembalikan buku terlebih dahulu."
  8b. Proses berhenti

EXC-3: Session timeout (di langkah mana saja)
  Xa. Sistem menampilkan "Session expired. Silakan login 
      ulang."
  Xb. Redirect ke halaman login

─── POSTCONDITIONS ──────────────────────────────────────────

POST-1 : Transaksi peminjaman tercatat di database
POST-2 : Stok buku berkurang 1
POST-3 : Mahasiswa menerima email konfirmasi
POST-4 : Tanggal jatuh tempo tercatat (14 hari)

─── BUSINESS RULES ──────────────────────────────────────────

BR-1 : Maksimal peminjaman: 3 buku per mahasiswa
BR-2 : Durasi peminjaman: 14 hari kalender
BR-3 : Perpanjangan: maksimal 1 kali per peminjaman
BR-4 : Denda keterlambatan: Rp 1.000 per hari per buku

─── NON-FUNCTIONAL REQUIREMENTS ─────────────────────────────

NFR-1 : Proses peminjaman harus selesai dalam < 10 detik
NFR-2 : Konfirmasi email terkirim dalam < 1 menit
NFR-3 : Data transaksi dienkripsi (AES-256)
```

### 4.1.7 Tips Membuat Use Case yang Baik

```
═══════════════════════════════════════════════════════════════
DO's dan DON'Ts DALAM USE CASE MODELING
═══════════════════════════════════════════════════════════════

DO (Lakukan):
  ✓ Gunakan kata kerja aktif untuk nama use case
    → "Pinjam Buku", "Cari Buku", "Lihat Laporan"
  ✓ Fokus pada GOAL pengguna, bukan langkah teknis
  ✓ Sertakan alternative dan exception flows
  ✓ Validasi diagram bersama stakeholder
  ✓ Gunakan level abstraksi yang konsisten

DON'T (Hindari):
  ✗ Jangan terlalu banyak <<include>> dan <<extend>>
    → Diagram menjadi sulit dibaca (spaghetti)
  ✗ Jangan menulis use case terlalu detail (seperti kode)
    → "Sistem menjalankan query SQL SELECT..."
  ✗ Jangan gunakan use case untuk CRUD sederhana
    → Cukup satu use case "Kelola Data Buku"
  ✗ Jangan campur level abstraksi
    → "Login" dan "Kelola Seluruh Sistem" di diagram yang sama
  ✗ Jangan lupa actor non-manusia
    → Scheduler, external API, payment gateway
```

---

## 4.2 User Stories

### 4.2.1 Apa Itu User Story?

User Story adalah deskripsi **singkat** tentang sebuah fitur dari perspektif pengguna. User story bukan spesifikasi detail — melainkan **placeholder untuk percakapan** (*Card, Conversation, Confirmation* - Ron Jeffries).

**Format standar:**

```
"As a [ROLE], I want [FEATURE], so that [BENEFIT]"
"Sebagai [PERAN], saya ingin [FITUR], agar [MANFAAT]"
```

**Tiga komponen (3C):**

| Komponen | Penjelasan | Contoh |
|----------|-----------|--------|
| **Card** | Deskripsi singkat (1-2 kalimat) | "As a mahasiswa, I want mencari buku..." |
| **Conversation** | Diskusi tim tentang detail implementasi | "Pencarian support fuzzy search ga?" |
| **Confirmation** | Acceptance criteria yang bisa diverifikasi | Given-When-Then scenarios |

### 4.2.2 Contoh User Stories — Perpustakaan Digital UAI

```
═══════════════════════════════════════════════════════════════
USER STORIES — Perpustakaan Digital UAI
═══════════════════════════════════════════════════════════════

US-01: "As a mahasiswa, I want mencari buku berdasarkan 
       judul, penulis, atau ISBN, so that saya bisa 
       menemukan buku yang dibutuhkan dengan cepat."

US-02: "As a mahasiswa, I want meminjam buku secara 
       online, so that saya tidak perlu antri di meja 
       sirkulasi."

US-03: "As a mahasiswa, I want melihat status ketersediaan 
       buku secara real-time, so that saya tidak perlu 
       datang ke perpustakaan jika buku sedang dipinjam."

US-04: "As a mahasiswa, I want menerima notifikasi 3 hari 
       sebelum batas pengembalian, so that saya tidak 
       terkena denda keterlambatan."

US-05: "As a mahasiswa, I want memperpanjang masa peminjaman 
       secara online, so that saya tidak perlu datang ke 
       perpustakaan untuk perpanjangan."

US-06: "As a pustakawan, I want melihat daftar peminjaman 
       yang terlambat, so that saya bisa mengirim 
       reminder kepada mahasiswa."

US-07: "As a pustakawan, I want menambah dan mengedit data 
       buku di katalog, so that koleksi perpustakaan 
       selalu up-to-date."

US-08: "As a kepala perpustakaan, I want melihat laporan 
       statistik peminjaman per bulan, so that saya bisa 
       membuat keputusan pengadaan buku baru."

US-09: "As a dosen, I want merekomendasikan buku untuk 
       mata kuliah tertentu, so that mahasiswa mudah 
       menemukan referensi kuliah."

US-10: "As a admin IT, I want melakukan backup database 
       secara terjadwal, so that data aman jika terjadi 
       kegagalan sistem."
```

### 4.2.3 INVEST Criteria — Detail

User story yang baik memenuhi **semua 6 kriteria INVEST**:

| Kriteria | Penjelasan | Contoh BAIK | Contoh BURUK | Tips Perbaikan |
|----------|-----------|-------------|--------------|----------------|
| **I**ndependent | Tidak bergantung pada story lain untuk diimplementasi | "Cari buku" (berdiri sendiri) | "Cari buku (tapi login harus selesai dulu)" | Pisahkan dependensi, atau gabung jadi satu story |
| **N**egotiable | Detail implementasi bisa didiskusikan; bukan kontrak tetap | "Tampilkan hasil pencarian" (cara tampilan bisa berubah) | "Tampilkan dalam grid 3 kolom dengan font Arial 12pt" | Tulis WHAT, bukan HOW |
| **V**aluable | Memberikan nilai nyata bagi pengguna atau bisnis | "Notifikasi deadline" (mengurangi denda mahasiswa) | "Refactoring database schema" (tidak ada nilai langsung bagi user) | Jika teknis, kaitkan dengan user value |
| **E**stimable | Tim bisa memberikan estimasi effort | "Form pencarian dengan 3 filter" (scope jelas) | "Buat sistem yang bagus dan lengkap" (scope tidak jelas) | Pecah menjadi story yang lebih kecil |
| **S**mall | Cukup kecil untuk selesai dalam 1 sprint (1-3 hari) | "Pencarian buku berdasarkan judul" | "Kelola seluruh proses perpustakaan" (terlalu besar = Epic) | Split menggunakan teknik story splitting |
| **T**estable | Ada acceptance criteria yang bisa diverifikasi | "Pencarian menampilkan max 20 hasil per halaman" | "Pengguna harus puas dengan hasilnya" (subjektif) | Tulis Given-When-Then |

### 4.2.4 Evaluasi User Story dengan INVEST

**Latihan: Evaluasi story berikut**

```
═══════════════════════════════════════════════════════════════
EVALUASI INVEST
═══════════════════════════════════════════════════════════════

Story: "As a mahasiswa, I want mengelola semua aspek 
       perpustakaan, so that semuanya berjalan lancar."

  I - Independent?     → Terlalu besar, pasti overlap
  N - Negotiable?      → Ya, tapi "semua aspek" terlalu vague
  V - Valuable?        → "Semuanya lancar" tidak spesifik
  E - Estimable?       → TIDAK — scope tidak jelas
  S - Small?           → TIDAK — ini Epic, bukan story
  T - Testable?        → TIDAK — "lancar" tidak terukur

  VERDICT: GAGAL — perlu dipecah menjadi stories kecil

─── PERBAIKAN ───────────────────────────────────────────────

Story 1: "As a mahasiswa, I want mencari buku berdasarkan 
         judul, so that saya menemukan buku dengan cepat"
Story 2: "As a mahasiswa, I want meminjam buku online, 
         so that saya tidak perlu antri"
Story 3: "As a mahasiswa, I want melihat riwayat 
         peminjaman, so that saya tahu buku apa yang 
         pernah saya pinjam"
```

### 4.2.5 Story Splitting — Teknik Memecah Epic

Jika story terlalu besar (Epic), pecah menggunakan salah satu teknik berikut:

| Teknik | Penjelasan | Contoh |
|--------|-----------|--------|
| **By Workflow** | Pecah berdasarkan langkah proses | Epic "Kelola Peminjaman" → Pinjam, Perpanjang, Kembalikan |
| **By Data** | Pecah berdasarkan jenis data | "Cari Buku" → Cari by judul, Cari by penulis, Cari by ISBN |
| **By Interface** | Pecah berdasarkan channel | "Notifikasi" → Email notification, WhatsApp notification |
| **By Role** | Pecah berdasarkan actor | "Laporan" → Laporan pustakawan, Laporan kepala perpustakaan |
| **By Happy/Sad Path** | Pecah berdasarkan skenario | "Login" → Login berhasil, Login gagal, Reset password |
| **By CRUD** | Pecah berdasarkan operasi | "Kelola Buku" → Tambah buku, Edit buku, Hapus buku |

**Contoh Story Splitting:**

```
═══════════════════════════════════════════════════════════════
STORY SPLITTING: EPIC → USER STORIES
═══════════════════════════════════════════════════════════════

EPIC: "As a mahasiswa, I want mengelola peminjaman buku"
(Story Points: 40 — terlalu besar untuk 1 sprint!)

SPLIT BY WORKFLOW:
┌─────────────────────────────────────────────────────────┐
│ US-01: Mencari buku berdasarkan judul          (3 pts)  │
│ US-02: Melihat detail dan ketersediaan buku    (2 pts)  │
│ US-03: Meminjam buku secara online             (5 pts)  │
│ US-04: Melihat daftar buku yang dipinjam       (3 pts)  │
│ US-05: Memperpanjang masa peminjaman online    (5 pts)  │
│ US-06: Menerima notifikasi batas pengembalian  (5 pts)  │
│ US-07: Melihat riwayat peminjaman              (3 pts)  │
│                                                         │
│ Total: 26 pts (bisa diselesaikan dalam 2 sprint)        │
└─────────────────────────────────────────────────────────┘
```

---

## 4.3 Acceptance Criteria

### 4.3.1 Apa Itu Acceptance Criteria?

**Acceptance Criteria (AC)** adalah kondisi yang harus dipenuhi agar sebuah user story dianggap "selesai" (*Definition of Done* di level story). AC ditulis sebelum implementasi dan menjadi dasar untuk pengujian.

### 4.3.2 Format Given-When-Then (Gherkin)

Format **Given-When-Then** (juga disebut format Gherkin karena digunakan oleh tool BDD Cucumber) adalah format standar untuk menulis acceptance criteria:

```
Given [kondisi awal / precondition]
When  [aksi yang dilakukan pengguna]
Then  [hasil yang diharapkan]
And   [hasil tambahan, jika ada]
```

### 4.3.3 Contoh Acceptance Criteria (5+ Contoh Lengkap)

**AC untuk US-01: Pencarian Buku**

```gherkin
Feature: Pencarian Buku di Katalog Perpustakaan

  Scenario 1: Pencarian berdasarkan judul — hasil ditemukan
    Given mahasiswa sudah login ke sistem perpustakaan
    And database memiliki buku berjudul "Algoritma dan Pemrograman"
    When mahasiswa mengetik "algoritma" di field pencarian
    And mahasiswa mengklik tombol "Cari"
    Then sistem menampilkan daftar buku yang mengandung 
         kata "algoritma" di judulnya
    And setiap hasil menampilkan judul, penulis, tahun terbit, 
        dan status ketersediaan
    And hasil ditampilkan maksimal 20 item per halaman
    And waktu loading hasil < 3 detik

  Scenario 2: Pencarian tanpa hasil
    Given mahasiswa sudah login ke sistem perpustakaan
    When mahasiswa mencari buku dengan keyword "xyzabc123"
    Then sistem menampilkan pesan "Buku tidak ditemukan 
         untuk keyword 'xyzabc123'"
    And sistem menyarankan: "Coba gunakan keyword yang 
        lebih umum"

  Scenario 3: Pencarian dengan field kosong
    Given mahasiswa sudah login ke sistem perpustakaan
    When mahasiswa mengklik tombol "Cari" tanpa mengetik apapun
    Then sistem menampilkan pesan "Silakan masukkan keyword 
         pencarian"
    And field pencarian diberi highlight merah
```

**AC untuk US-03: Peminjaman Buku Online**

```gherkin
Feature: Peminjaman Buku Online

  Scenario 1: Peminjaman berhasil
    Given mahasiswa "Ahmad" sudah login dengan NIM 20230001
    And mahasiswa sedang meminjam 1 buku (batas: 3 buku)
    And buku "Clean Code" memiliki stok tersedia: 2
    When mahasiswa mengklik tombol "Pinjam" pada buku 
         "Clean Code"
    Then sistem menampilkan konfirmasi peminjaman
    And tanggal jatuh tempo = tanggal hari ini + 14 hari
    And stok buku "Clean Code" berkurang menjadi 1
    And jumlah peminjaman mahasiswa bertambah menjadi 2
    And email konfirmasi dikirim ke ahmad@uai.ac.id

  Scenario 2: Peminjaman gagal — batas tercapai
    Given mahasiswa "Budi" sudah login
    And mahasiswa sedang meminjam 3 buku (batas: 3 buku)
    When mahasiswa mengklik tombol "Pinjam" pada buku apapun
    Then sistem menampilkan pesan "Anda sudah mencapai 
         batas peminjaman (3 buku). Kembalikan buku terlebih 
         dahulu untuk meminjam buku baru."
    And tombol "Pinjam" menjadi disabled/gray

  Scenario 3: Peminjaman gagal — buku tidak tersedia
    Given mahasiswa sudah login
    And buku "Software Engineering" memiliki stok tersedia: 0
    When mahasiswa membuka halaman detail buku tersebut
    Then tombol "Pinjam" tidak ditampilkan
    And sistem menampilkan "Stok habis"
    And sistem menawarkan tombol "Reservasi"
```

**AC untuk US-04: Notifikasi Deadline**

```gherkin
Feature: Notifikasi Batas Pengembalian

  Scenario 1: Notifikasi 3 hari sebelum deadline
    Given mahasiswa "Citra" meminjam buku dengan jatuh 
         tempo 25 Maret 2026
    When tanggal sistem menunjukkan 22 Maret 2026 
         (3 hari sebelum)
    Then sistem mengirim email ke citra@uai.ac.id
    And isi email: "Buku [judul] harus dikembalikan pada 
        25 Maret 2026. Sisa waktu: 3 hari."
    And notifikasi juga tampil di dashboard mahasiswa

  Scenario 2: Notifikasi buku terlambat
    Given mahasiswa "Dian" memiliki buku yang jatuh tempo 
         20 Maret 2026
    When tanggal sistem menunjukkan 21 Maret 2026 
         (1 hari terlambat)
    Then sistem mengirim email reminder
    And isi email menyertakan informasi denda: 
        "Denda saat ini: Rp 1.000"
    And denda bertambah Rp 1.000 setiap hari
```

**AC untuk US-05: Perpanjangan Peminjaman**

```gherkin
Feature: Perpanjangan Peminjaman Online

  Scenario 1: Perpanjangan berhasil
    Given mahasiswa meminjam buku "Database Systems"
    And peminjaman belum pernah diperpanjang
    And buku tidak sedang direservasi oleh mahasiswa lain
    When mahasiswa mengklik "Perpanjang" pada buku tersebut
    Then tanggal jatuh tempo diperpanjang 7 hari dari 
         tanggal saat ini
    And status berubah menjadi "Diperpanjang (1/1)"
    And email konfirmasi perpanjangan dikirim

  Scenario 2: Perpanjangan gagal — sudah pernah diperpanjang
    Given mahasiswa sudah memperpanjang buku 1 kali (max: 1)
    When mahasiswa mengklik "Perpanjang"
    Then sistem menampilkan "Perpanjangan hanya diperbolehkan 
         1 kali per peminjaman"
    And tombol "Perpanjang" menjadi disabled
```

### 4.3.4 Tips Menulis Acceptance Criteria yang Baik

| Prinsip | Penjelasan | Contoh |
|---------|-----------|--------|
| **Specific** | Tulis kondisi yang jelas dan terukur | "max 20 item per halaman" bukan "secukupnya" |
| **Testable** | Setiap AC harus bisa di-automate sebagai test | Given-When-Then bisa langsung jadi test script |
| **Complete** | Cover happy path DAN edge cases/error cases | Sertakan skenario gagal |
| **Independent** | Setiap scenario bisa dijalankan sendiri | Jangan bergantung pada scenario lain |
| **User-facing** | Tulis dari perspektif pengguna, bukan teknis | "Sistem menampilkan pesan" bukan "Return HTTP 404" |

### 4.3.5 Hubungan User Story, AC, dan Test Case

```
┌─────────────────┐
│   User Story     │ "As a mahasiswa, I want mencari buku..."
└────────┬────────┘
         │ memiliki
         ▼
┌─────────────────┐
│  Acceptance      │ Scenario 1: Pencarian berhasil
│  Criteria        │ Scenario 2: Pencarian tidak ditemukan
│  (Given-When-    │ Scenario 3: Field kosong
│   Then)          │
└────────┬────────┘
         │ menjadi dasar
         ▼
┌─────────────────┐
│   Test Cases     │ test_search_by_title_found()
│   (Automated)    │ test_search_no_results()
│                  │ test_search_empty_field()
└─────────────────┘
```

---

## 4.4 Product Backlog dan Prioritisasi

### 4.4.1 Apa Itu Product Backlog?

**Product Backlog** adalah **daftar terurut** dari semua yang dibutuhkan untuk produk. Dikelola oleh **Product Owner** dan menjadi satu-satunya sumber kerja bagi tim Scrum.

Karakteristik Product Backlog yang baik mengikuti akronim **DEEP**:

| Kriteria | Penjelasan |
|----------|-----------|
| **D**etailed Appropriately | Item atas lebih detail dari item bawah |
| **E**stimated | Semua item memiliki estimasi effort |
| **E**mergent | Backlog terus berkembang dan berubah |
| **P**rioritized | Item diurutkan berdasarkan nilai bisnis |

### 4.4.2 Contoh Product Backlog — Perpustakaan Digital UAI

```
═══════════════════════════════════════════════════════════════
PRODUCT BACKLOG — Perpustakaan Digital UAI
Product Owner: Kepala Perpustakaan UAI
Last Updated: 20 Maret 2026
═══════════════════════════════════════════════════════════════

Sprint 1 (Must Have — Core Features)
─────────────────────────────────────
│ #  │ User Story                     │ Priority │ SP │ Status  │
│ 1  │ Login dengan NIM + password    │ Must     │ 3  │ To Do   │
│ 2  │ Pencarian buku (judul, penulis)│ Must     │ 5  │ To Do   │
│ 3  │ Lihat detail buku             │ Must     │ 2  │ To Do   │
│ 4  │ Peminjaman buku online        │ Must     │ 8  │ To Do   │
│ 5  │ Lihat buku yang dipinjam      │ Must     │ 3  │ To Do   │
                              Subtotal Sprint 1: 21 SP

Sprint 2 (Must/Should Have)
─────────────────────────────────────
│ 6  │ Pengembalian buku             │ Must     │ 5  │ Backlog │
│ 7  │ Notifikasi deadline (email)   │ Should   │ 5  │ Backlog │
│ 8  │ Kelola katalog (pustakawan)   │ Must     │ 8  │ Backlog │
│ 9  │ Laporan statistik bulanan     │ Should   │ 5  │ Backlog │
│ 10 │ Perpanjangan peminjaman       │ Should   │ 5  │ Backlog │
                              Subtotal Sprint 2: 28 SP

Sprint 3 (Should/Could Have)
─────────────────────────────────────
│ 11 │ Filter pencarian (kategori)   │ Should   │ 3  │ Backlog │
│ 12 │ Reservasi buku                │ Should   │ 5  │ Backlog │
│ 13 │ Riwayat peminjaman            │ Should   │ 3  │ Backlog │
│ 14 │ Notifikasi WhatsApp           │ Could    │ 5  │ Backlog │
│ 15 │ Denda otomatis                │ Should   │ 5  │ Backlog │
                              Subtotal Sprint 3: 21 SP

Future (Could/Won't Have Now)
─────────────────────────────────────
│ 16 │ Rekomendasi buku AI           │ Won't    │ 13 │ Backlog │
│ 17 │ Dark mode                     │ Could    │ 2  │ Backlog │
│ 18 │ Integrasi SIA UAI             │ Won't    │ 13 │ Backlog │
│ 19 │ E-book reader                 │ Won't    │ 21 │ Backlog │
│ 20 │ Barcode scanner mobile        │ Could    │ 8  │ Backlog │
```

### 4.4.3 MoSCoW Prioritization Method

MoSCoW adalah teknik prioritisasi yang membagi requirements ke dalam 4 kategori:

| Prioritas | Deskripsi | Aturan | Contoh |
|-----------|-----------|--------|--------|
| **M**ust have | **Wajib** — sistem tidak berjalan tanpa ini | ~60% total effort | Login, cari buku, pinjam buku |
| **S**hould have | **Penting** tapi sistem tetap bisa berjalan tanpa ini | ~20% total effort | Notifikasi, laporan statistik |
| **C**ould have | **Nice to have** — ditambahkan jika waktu dan budget memungkinkan | ~20% total effort | Dark mode, filter pencarian |
| **W**on't have (this time) | **Tidak untuk rilis ini** — tapi mungkin di versi berikutnya | 0% effort rilis ini | AI recommendation, e-book reader |

**Teknik MoSCoW Prioritization Workshop:**

```
═══════════════════════════════════════════════════════════════
WORKSHOP MOSCOW PRIORITIZATION (60 menit)
═══════════════════════════════════════════════════════════════

PERSIAPAN (10 menit)
  - Tulis semua user stories di sticky notes
  - Siapkan 4 kolom: Must / Should / Could / Won't
  - Peserta: Product Owner + Tim Dev + Stakeholder kunci

RONDE 1: Individual (10 menit)
  - Setiap peserta menempel sticky note di kolom yang
    menurut mereka tepat

RONDE 2: Diskusi (25 menit)
  - Review item yang ada perbedaan pendapat
  - Product Owner memfasilitasi diskusi
  - Gunakan pertanyaan: "Jika kita tidak punya fitur ini,
    apakah sistem masih bisa dipakai?"

VALIDASI (10 menit)
  - Hitung total effort per kategori
  - Must ≈ 60%, Should ≈ 20%, Could ≈ 20%
  - Jika Must > 70%, ada yang perlu diturunkan

FINALISASI (5 menit)
  - Product Owner memberikan keputusan akhir
  - Dokumentasikan hasil di Product Backlog
```

### 4.4.4 Story Points dan Estimation

**Story Points** mengukur **relative effort** untuk menyelesaikan user story. Bukan waktu absolut, melainkan perbandingan kompleksitas antar story.

**Skala Fibonacci yang umum digunakan:**

| Points | Effort Relatif | Contoh Perpustakaan |
|--------|---------------|---------------------|
| 1 | Trivial, < 1 jam | Ubah warna tombol, perbaiki typo |
| 2 | Sederhana, beberapa jam | Tambah field di form, tambah kolom tabel |
| 3 | Kecil, ~1 hari | Halaman statis baru, validasi form |
| 5 | Medium, 2-3 hari | Pencarian buku (CRUD + filter), notifikasi email |
| 8 | Besar, 3-5 hari | Peminjaman buku (logic + validasi + notifikasi) |
| 13 | Sangat besar, ~1 minggu | Integrasi dengan sistem eksternal (SIA, payment) |
| 21 | Epic — harus dipecah | Modul lengkap (terlalu besar untuk 1 sprint) |

### 4.4.5 Planning Poker

**Planning Poker** adalah teknik estimasi kolaboratif yang digunakan oleh tim Agile:

```
═══════════════════════════════════════════════════════════════
PLANNING POKER — Cara Bermain
═══════════════════════════════════════════════════════════════

LANGKAH 1: Product Owner membacakan user story
  "As a mahasiswa, I want meminjam buku secara online..."

LANGKAH 2: Tim berdiskusi tentang story (5-10 menit)
  - "Ini butuh validasi keanggotaan ga?"
  - "Perlu integrasi email ga?"
  - "Stok buku perlu real-time update?"

LANGKAH 3: Setiap anggota memilih kartu secara BERSAMAAN
  ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐
  │ 5 │ │ 8 │ │ 8 │ │ 5 │ │ 13│
  └───┘ └───┘ └───┘ └───┘ └───┘
  Andi   Budi  Citra  Dian   Eko

LANGKAH 4: Jika ada perbedaan besar (5 vs 13), diskusikan
  - Eko (13): "Saya pikir perlu integrasi payment juga"
  - Andi (5): "Oh, saya kira hanya CRUD biasa"
  
LANGKAH 5: Vote ulang sampai konvergen
  ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐
  │ 8 │ │ 8 │ │ 8 │ │ 8 │ │ 8 │
  └───┘ └───┘ └───┘ └───┘ └───┘
  
HASIL: Story Point = 8
```

---

## 4.5 User Story Mapping

### 4.5.1 Apa Itu User Story Mapping?

**User Story Mapping** (Jeff Patton, 2014) adalah teknik untuk memvisualisasikan seluruh backlog dalam bentuk peta 2 dimensi:
- Sumbu horizontal: **alur pengguna** (user journey/workflow)
- Sumbu vertikal: **prioritas** (atas = penting, bawah = kurang penting)

### 4.5.2 Cara Membuat User Story Map

```
═══════════════════════════════════════════════════════════════
USER STORY MAP — Perpustakaan Digital UAI
═══════════════════════════════════════════════════════════════

USER ACTIVITIES (Backbone):
  Register → Login → Cari Buku → Pinjam → Kembalikan → Laporan

STORIES PER ACTIVITY (diurutkan prioritas atas ke bawah):

            Register    Login     Cari Buku   Pinjam      Kembalikan  Laporan
            ─────────  ─────────  ──────────  ──────────  ──────────  ──────────
MVP/        Register   Login      Cari by     Pinjam      Proses      Lihat
Release 1   dgn NIM    NIM+pass   judul       online      pengemba-   riwayat
            ─────────  ─────────  ──────────  ──────────  lian        ──────────
Release 2   Edit       Remember   Cari by     Perpanjang  ──────────  Laporan
            profil     me         penulis     online      Notifikasi  bulanan
            ─────────  ─────────  ──────────  ──────────  deadline    ──────────
Release 3   Upload     Login      Filter      Reservasi   ──────────  Export
            foto       Google     kategori    buku        Denda       CSV
            ─────────  ─────────  ──────────  ──────────  otomatis    ──────────
Future      ─────────  2FA auth   Rekomendasi ──────────  ──────────  Dashboard
                                  AI                                  analytics
```

### 4.5.3 Keuntungan User Story Mapping

| Keuntungan | Penjelasan |
|-----------|-----------|
| **Big Picture** | Melihat seluruh produk dalam satu pandangan |
| **Prioritization** | Memudahkan penentuan MVP dan release plan |
| **Gap Detection** | Mudah menemukan story yang terlewat |
| **Communication** | Tim dan stakeholder punya pemahaman yang sama |
| **Release Planning** | Garis horizontal membagi release/sprint |

---

## 4.6 Studi Kasus: Perpustakaan Digital UAI

### 4.6.1 Konteks Proyek

Perpustakaan UAI saat ini masih menggunakan proses manual berbasis buku log untuk peminjaman buku. Dengan 4.000+ mahasiswa dan koleksi 15.000+ buku, proses manual menyebabkan:
- Antrian panjang di jam sibuk
- Data sering hilang atau tidak akurat
- Tidak ada tracking keterlambatan otomatis
- Tidak ada statistik peminjaman

### 4.6.2 Use Case Diagram (Ringkasan)

```
Actors: Mahasiswa, Dosen, Pustakawan, Admin IT, Scheduler
Use Cases: 12 use cases utama
Relationships: 3 <<include>>, 2 <<extend>>, 1 generalization
```

### 4.6.3 User Stories (Top 10)

```
│ ID    │ User Story                                 │ SP │ MoSCoW │
│ US-01 │ Login dengan NIM                           │ 3  │ Must   │
│ US-02 │ Cari buku (judul, penulis, ISBN)          │ 5  │ Must   │
│ US-03 │ Pinjam buku online                        │ 8  │ Must   │
│ US-04 │ Lihat buku yang dipinjam                  │ 3  │ Must   │
│ US-05 │ Notifikasi deadline                       │ 5  │ Should │
│ US-06 │ Kelola katalog (pustakawan)               │ 8  │ Must   │
│ US-07 │ Perpanjang peminjaman                     │ 5  │ Should │
│ US-08 │ Laporan statistik                         │ 5  │ Should │
│ US-09 │ Reservasi buku                            │ 5  │ Could  │
│ US-10 │ Rekomendasi buku AI                       │ 13 │ Won't  │
│       │                              Total:        │ 60 │        │
│       │                              Sprint Vel:   │ 25 │        │
│       │                              Est. Sprints: │ 3  │        │
```

### 4.6.4 Acceptance Criteria (Top 3 Stories)

Setiap Must Have story memiliki minimal 3 scenarios Given-When-Then (lihat contoh lengkap di Section 4.3.3).

### 4.6.5 Pelajaran dari Studi Kasus

```
═══════════════════════════════════════════════════════════════
LESSONS LEARNED: Perpustakaan Digital UAI
═══════════════════════════════════════════════════════════════

1. MULAI DARI MVP
   → Jangan coba bangun semua fitur sekaligus
   → Sprint 1: Login + Cari + Pinjam = sudah bisa dipakai

2. STAKEHOLDER BERBEDA = PRIORITAS BERBEDA
   → Mahasiswa: cari & pinjam cepat
   → Pustakawan: kelola katalog & laporan
   → Gunakan MoSCoW untuk konsensus

3. NON-FUNCTIONAL SERING DILUPAKAN
   → "Sistem harus cepat" → berapa detik tepatnya?
   → Definisikan NFR dengan metrik terukur

4. ACCEPTANCE CRITERIA = KONTRAK
   → AC yang jelas mengurangi diskusi "sudah selesai belum?"
   → Given-When-Then bisa langsung jadi automated test

5. USER STORY MAP MEMBANTU BIG PICTURE
   → Tanpa story map, backlog terasa seperti daftar belanja
   → Dengan story map, terlihat user journey end-to-end
```

---

## 4.7 Studi Kasus Tambahan: User Stories Ruangguru

### 4.7.1 Konteks

Ruangguru adalah platform EdTech terbesar di Indonesia dengan 30+ juta pengguna. Sebagai platform belajar online, Ruangguru memiliki banyak fitur yang bisa dimodelkan sebagai user stories.

### 4.7.2 Contoh User Stories Ruangguru

```
═══════════════════════════════════════════════════════════════
USER STORIES — Platform Belajar Online (Ruangguru-like)
═══════════════════════════════════════════════════════════════

SISWA:
US-01: "As a siswa SMA, I want memilih mata pelajaran yang 
       ingin dipelajari, so that saya bisa fokus pada 
       pelajaran yang dibutuhkan untuk UTBK."

US-02: "As a siswa, I want menonton video pembelajaran 
       dengan subtitle, so that saya bisa belajar meski 
       di tempat yang berisik."

US-03: "As a siswa, I want mengerjakan latihan soal setelah 
       setiap bab, so that saya bisa mengukur pemahaman."

US-04: "As a siswa, I want melihat progress belajar saya 
       dalam bentuk dashboard, so that saya termotivasi 
       untuk terus belajar."

GURU / TUTOR:
US-05: "As a tutor, I want membuat dan mengupload video 
       pembelajaran, so that siswa bisa belajar kapan saja."

US-06: "As a tutor, I want melihat analytics engagement 
       video saya, so that saya bisa meningkatkan kualitas 
       konten."

ORANG TUA:
US-07: "As a orang tua, I want melihat progress belajar 
       anak saya, so that saya bisa memantau perkembangan 
       akademiknya."

ADMIN PLATFORM:
US-08: "As a admin, I want mengelola langganan (subscription) 
       siswa, so that billing berjalan dengan benar."
```

### 4.7.3 Perbandingan Use Case vs User Story

| Aspek | Use Case | User Story |
|-------|----------|------------|
| **Format** | Diagram + narrative (formal) | 1-2 kalimat (informal) |
| **Detail** | Sangat detail (flows, exceptions) | Ringkas (detail di AC) |
| **Perspektif** | Interaksi actor-system | Nilai bagi pengguna |
| **Metodologi** | Tradisional (RUP, Waterfall) | Agile (Scrum, XP) |
| **Kapan digunakan** | Sistem kompleks, dokumentasi formal | Iteratif, perubahan cepat |
| **Stakeholder** | Baik untuk non-teknis (visual) | Baik untuk tim dev (ringkas) |
| **Komplementer** | Bisa digunakan bersama user stories | Bisa dilengkapi dengan use case |

---

## 4.8 AI Corner: AI untuk User Stories (Level: Basic)

### 4.8.1 Pengantar AI untuk Requirements Modeling

AI tools (ChatGPT, Claude, Copilot) dapat membantu mempercepat pembuatan user stories, acceptance criteria, dan bahkan use case narratives. Namun, AI **tidak menggantikan** pemahaman domain dan validasi stakeholder.

### 4.8.2 Generate User Stories dengan AI

**Prompt:**
```
Kamu adalah seorang Product Owner untuk proyek 
"Perpustakaan Digital Kampus" di universitas di Jakarta 
dengan 4000 mahasiswa.

Buatkan 15 user stories dalam format:
"As a [role], I want [feature], so that [benefit]"

Gunakan minimal 4 roles: mahasiswa, dosen, pustakawan, 
admin IT. Pastikan setiap story memenuhi kriteria INVEST.

Kelompokkan berdasarkan prioritas MoSCoW.
```

**Evaluasi Output AI:**
- Apakah roles sudah sesuai konteks (mahasiswa Indonesia, bukan "student")?
- Apakah benefits realistis dan spesifik?
- Apakah ada story yang terlalu besar (Epic) dan perlu di-split?
- Apakah konteks Indonesia tercermin (NIM, WhatsApp notification, bahasa Indonesia)?

### 4.8.3 Generate Acceptance Criteria dengan AI

**Prompt:**
```
Untuk user story berikut, buatkan acceptance criteria 
dalam format Given-When-Then (Gherkin):

"As a mahasiswa, I want meminjam buku secara online, 
so that saya tidak perlu antri di meja sirkulasi."

Sertakan minimal:
- 2 happy path scenarios
- 2 error/edge case scenarios
- Metrik non-functional (response time, dll)
```

### 4.8.4 Membuat Use Case Narrative dengan AI

**Prompt:**
```
Buatkan Use Case Narrative lengkap untuk "Peminjaman 
Buku Online" di sistem perpustakaan kampus.

Sertakan:
- Use Case ID, Name, Version
- Actor(s), Description, Trigger
- Preconditions (minimal 3)
- Main Flow (minimal 8 langkah)
- Alternative Flows (minimal 2)
- Exception Flows (minimal 2)
- Postconditions (minimal 3)
- Business Rules
- Non-Functional Requirements

Format mengikuti template Cockburn.
```

### 4.8.5 Estimasi Story Points dengan AI

**Prompt:**
```
Berikan estimasi story points (skala Fibonacci: 1,2,3,5,8,
13,21) untuk user stories berikut. Jelaskan alasan untuk 
setiap estimasi berdasarkan kompleksitas, effort, dan risiko.

1. Login dengan NIM dan password
2. Pencarian buku dengan filter
3. Peminjaman buku online
4. Notifikasi email otomatis
5. Integrasi dengan Sistem Akademik

Tim: 3 developer (1 backend, 1 frontend, 1 fullstack)
Sprint duration: 2 minggu
Tech stack: Flask + MySQL + HTML/CSS/JS
```

### 4.8.6 Batasan dan Peringatan

> **PENTING**: AI sangat baik dalam generate user stories yang "terlihat benar" tapi:
> - Mungkin tidak menangkap kebutuhan unik stakeholder spesifik
> - Bisa menghasilkan stories yang terlalu generik
> - Estimasi story points dari AI hanya **baseline** — tim yang memutuskan
> - AI tidak memahami dinamika tim (siapa yang available, skill level, dll.)
> - Acceptance criteria dari AI mungkin miss edge cases spesifik domain
>
> **Gunakan AI sebagai starting point, bukan final output.**

### 4.8.7 Hands-on: Coba dan Evaluasi

**Latihan AI Corner:**

1. **Generate**: Gunakan AI untuk membuat 10 user stories untuk "Sistem Kantin UAI"
2. **Evaluate**: Review setiap story dengan INVEST criteria — tandai mana yang pass/fail
3. **Enhance**: Perbaiki stories yang gagal INVEST — tulis ulang secara manual
4. **AC**: Untuk 3 stories teratas, minta AI generate acceptance criteria (Given-When-Then)
5. **Validate**: Apakah AC mencakup happy path dan edge cases? Tambahkan yang kurang
6. **Log**: Catat di **AI Usage Log**: prompt, output AI, modifikasi Anda, refleksi

---

## Latihan Soal

### Level Dasar (C1-C2): 5 Soal

1. Sebutkan dan jelaskan **7 elemen** dalam Use Case Diagram beserta simbolnya.

2. Jelaskan perbedaan antara `<<include>>` dan `<<extend>>` dalam Use Case Diagram. Berikan masing-masing 2 contoh.

3. Tuliskan format user story dan berikan **5 contoh** user story untuk Sistem Informasi Akademik.

4. Sebutkan dan jelaskan **6 kriteria INVEST** untuk user story yang baik.

5. Jelaskan apa itu **Product Backlog** dan sebutkan 4 karakteristik backlog yang baik (DEEP).

### Level Menengah (C3-C4): 7 Soal

6. Buatlah **Use Case Diagram** untuk Sistem Informasi Perpustakaan Kampus dengan:
   - Minimal 5 actors (termasuk 1 external system)
   - Minimal 10 use cases
   - Minimal 2 <<include>> dan 2 <<extend>> relationships
   - 1 generalization

7. Tuliskan **Use Case Narrative lengkap** (termasuk main flow, alternative flows, dan exception flows) untuk use case "Pengembalian Buku".

8. Tulis **15 user stories** (format INVEST) untuk Sistem Antrian Puskesmas. Kelompokkan berdasarkan prioritas MoSCoW.

9. Buatlah **Acceptance Criteria** format Given-When-Then untuk 5 user stories teratas dari soal nomor 8. Setiap story harus memiliki minimal 2 scenarios (1 happy path, 1 error case).

10. Lakukan **evaluasi INVEST** terhadap 5 user stories berikut. Identifikasi masalah dan perbaiki:
    - "As a user, I want everything to work perfectly"
    - "As a admin, I want to manage the entire system"
    - "As a patient, I want to register, login, view schedule, book appointment, cancel appointment, and view history"
    - "As a system, I want to backup database every night"
    - "As a doctor, I want to see patient records after the patient management module is completed"

11. Buatlah **Product Backlog** lengkap untuk Sistem E-Commerce UMKM dengan:
    - Minimal 20 user stories
    - Story Points estimation untuk setiap story
    - Prioritasi MoSCoW
    - Pembagian ke 3 sprints

12. Buatlah **User Story Map** untuk aplikasi "Sistem Pemesanan Makanan Online" dengan:
    - 5 user activities di backbone
    - 3-4 stories per activity
    - Garis release (MVP, Release 2, Release 3)

### Level Mahir (C5-C6): 7 Soal

13. Bandingkan pendekatan **Use Case** vs **User Stories** untuk proyek berikut. Mana yang lebih cocok dan mengapa?
    - Proyek sistem perbankan (regulatory, formal)
    - Proyek startup mobile app (cepat berubah)
    - Proyek sistem ERP perusahaan besar

14. Evaluasi **10 user stories** berikut menggunakan INVEST criteria — identifikasi semua masalah dan tulis ulang setiap story yang gagal:
    - (Buatlah 10 stories yang intentionally memiliki masalah INVEST)

15. Rancang **Product Backlog lengkap** untuk Aplikasi Pengelolaan Zakat Digital dengan:
    - Stakeholder analysis (3+ stakeholder types)
    - 25+ user stories memenuhi INVEST
    - Acceptance criteria (Given-When-Then) untuk top 10 stories
    - MoSCoW prioritization dengan justifikasi
    - Story points estimation dengan Planning Poker simulation
    - User Story Map dengan 3 releases

16. Anda adalah Product Owner untuk Sistem Informasi Rumah Sakit. Tim developer berkapasitas 20 story points per sprint (2 minggu). Backlog memiliki 80 story points. Stakeholder menginginkan semua fitur selesai dalam 2 sprint. Bagaimana Anda **mengelola ekspektasi** dan melakukan **release planning**?

17. Analisis **trade-off** antara:
    - Detail Use Case Narrative vs kecepatan perubahan di Agile
    - Story granularity (terlalu kecil vs terlalu besar)
    - MoSCoW vs WSJF (Weighted Shortest Job First) untuk prioritisasi
    Berikan rekomendasi kapan masing-masing pendekatan cocok.

18. Rancang proses **end-to-end** dari requirements ke backlog untuk proyek "Digitalisasi Pelayanan Kecamatan":
    - Stakeholder identification dan analysis
    - Elicitation plan (teknik per stakeholder)
    - Use Case Diagram level sistem
    - 20+ user stories dari use cases
    - Acceptance criteria (top 10 stories)
    - Backlog prioritization (MoSCoW)
    - User Story Map
    - Sprint planning (3 sprints)

19. Bandingkan **3 teknik estimasi** (Planning Poker, T-Shirt Sizing, Affinity Mapping) untuk konteks proyek dengan tim 5 orang yang baru pertama kali bekerja bersama. Teknik mana yang paling cocok dan mengapa?

---

## Rangkuman

1. **Use Case Diagram** memodelkan interaksi actor-sistem secara visual menggunakan 7 elemen (actor, use case, system boundary, association, include, extend, generalization).

2. **Use Case Narrative** mendetailkan alur interaksi: main flow, alternative flows, exception flows, preconditions, dan postconditions.

3. **Actor identification** harus mencakup pengguna langsung, tidak langsung, sistem eksternal, dan trigger berbasis waktu.

4. **User Stories** menggunakan format "As a [role], I want [feature], so that [benefit]" — fokus pada **nilai bagi pengguna**, bukan detail teknis.

5. **INVEST criteria** memastikan user story: Independent, Negotiable, Valuable, Estimable, Small, Testable. Story yang gagal INVEST harus diperbaiki atau dipecah.

6. **Acceptance Criteria** dalam format **Given-When-Then** mendefinisikan kapan sebuah story "selesai" — menjadi dasar automated testing.

7. **Product Backlog** adalah daftar terurut semua kebutuhan produk, dikelola Product Owner, dan harus DEEP (Detailed, Estimated, Emergent, Prioritized).

8. **MoSCoW** (Must/Should/Could/Won't) membantu prioritisasi berdasarkan nilai bisnis.

9. **Story Points** mengukur relative effort menggunakan skala Fibonacci; **Planning Poker** memastikan estimasi kolaboratif.

10. **User Story Mapping** memvisualisasikan backlog dalam 2 dimensi (alur pengguna x prioritas) untuk perencanaan release yang lebih baik.

---

## Referensi

1. Cohn, M. (2004). *User Stories Applied: For Agile Software Development*. Addison-Wesley.
2. Cockburn, A. (2001). *Writing Effective Use Cases*. Addison-Wesley.
3. Patton, J. (2014). *User Story Mapping: Discover the Whole Story, Build the Right Product*. O'Reilly.
4. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 4. Pearson.
5. Rubin, K. S. (2012). *Essential Scrum*. Addison-Wesley.
6. Wiegers, K. E. & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press.
7. Schwaber, K. & Sutherland, J. (2020). *The Scrum Guide*. Scrum.org.
8. IEEE Computer Society. (2024). *SWEBOK v4* — Knowledge Area: Software Requirements.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
