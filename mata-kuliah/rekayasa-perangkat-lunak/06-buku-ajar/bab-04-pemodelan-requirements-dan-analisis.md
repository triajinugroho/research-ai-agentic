# BAB 4: PEMODELAN REQUIREMENTS DAN ANALISIS

**Oleh: Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom |
|-----------|-----------|-------------|
| 2.3 | Membuat Use Case Diagram dan Use Case Narrative untuk memodelkan requirements | C3 (Menerapkan) |
| 2.4 | Menulis User Stories dengan INVEST criteria dan Acceptance Criteria | C3 (Menerapkan) |

---

## 4.1 Use Case Modeling

### 4.1.1 Apa Itu Use Case?

Use Case adalah teknik untuk memodelkan interaksi antara pengguna (actor) dan sistem. Use Case menggambarkan **apa** yang bisa dilakukan pengguna, bukan **bagaimana** sistem melakukannya.

### 4.1.2 Elemen Use Case Diagram

| Elemen | Simbol | Deskripsi |
|--------|--------|-----------|
| **Actor** | Stick figure | Siapa yang berinteraksi dengan sistem |
| **Use Case** | Ellipse | Apa yang bisa dilakukan |
| **System Boundary** | Rectangle | Batas sistem |
| **Association** | Garis | Hubungan actor-use case |
| **Include** | `<<include>>` | Use case wajib dipanggil |
| **Extend** | `<<extend>>` | Use case opsional |
| **Generalization** | Triangle arrow | Inheritance antar actors/use cases |

### 4.1.3 Contoh: Sistem Antrian Puskesmas

```
┌─────────────────── Sistem Antrian Puskesmas ────────────────────┐
│                                                                  │
│   ┌─────────────┐     ┌──────────────────┐                     │
│   │   Pasien     │────▶│ Daftar Antrian    │                     │
│   └─────────────┘     └──────────────────┘                     │
│         │              ┌──────────────────┐                     │
│         └─────────────▶│ Lihat Status      │                     │
│                        └──────────────────┘                     │
│                              │ <<extend>>                       │
│                              ▼                                  │
│                        ┌──────────────────┐                     │
│                        │ Terima Notifikasi │                     │
│                        └──────────────────┘                     │
│                                                                  │
│   ┌─────────────┐     ┌──────────────────┐                     │
│   │   Petugas    │────▶│ Panggil Pasien    │                     │
│   └─────────────┘     └──────────────────┘                     │
│         │              ┌──────────────────┐                     │
│         └─────────────▶│ Input Rekam Medis │                     │
│                        └──────────────────┘                     │
│                              │ <<include>>                      │
│                              ▼                                  │
│                        ┌──────────────────┐                     │
│                        │ Validasi Data     │                     │
│                        └──────────────────┘                     │
└──────────────────────────────────────────────────────────────────┘
```

### 4.1.4 Use Case Narrative

| Elemen | Detail |
|--------|--------|
| **Use Case** | Daftar Antrian |
| **Actor** | Pasien |
| **Precondition** | Pasien memiliki nomor BPJS atau KTP terdaftar |
| **Main Flow** | 1. Pasien membuka aplikasi<br>2. Pasien memilih poli tujuan<br>3. Sistem menampilkan estimasi antrian<br>4. Pasien mengkonfirmasi pendaftaran<br>5. Sistem memberikan nomor antrian |
| **Alternative Flow** | 3a. Poli penuh → sistem menawarkan jadwal alternatif |
| **Exception Flow** | 2a. Pasien belum terdaftar → redirect ke pendaftaran |
| **Postcondition** | Pasien terdaftar di antrian dan menerima nomor antrian |

## 4.2 User Stories

### 4.2.1 Format User Story

**"As a [role], I want [feature], so that [benefit]"**

Contoh untuk Sistem Perpustakaan:
- "As a **mahasiswa**, I want **mencari buku berdasarkan judul**, so that **saya bisa menemukan buku yang dibutuhkan dengan cepat**"
- "As a **pustakawan**, I want **melihat daftar peminjaman yang terlambat**, so that **saya bisa mengirim reminder**"
- "As a **admin**, I want **menambah buku baru ke katalog**, so that **koleksi perpustakaan selalu up-to-date**"

### 4.2.2 INVEST Criteria

User story yang baik memenuhi kriteria INVEST:

| Kriteria | Deskripsi | Contoh Baik | Contoh Buruk |
|----------|-----------|-------------|--------------|
| **I**ndependent | Tidak bergantung pada story lain | "Search buku" | "Search buku (setelah login selesai)" |
| **N**egotiable | Bisa didiskusikan dan diubah | Detail bisa berubah | Fixed specification |
| **V**aluable | Memberikan nilai bagi pengguna | Fitur yang user butuhkan | Refactoring internal |
| **E**stimable | Bisa diestimasi effort-nya | Scope jelas | "Buat sistem yang bagus" |
| **S**mall | Cukup kecil untuk 1 sprint | 1-3 hari kerja | Fitur 2 bulan |
| **T**estable | Bisa diverifikasi hasilnya | Ada acceptance criteria | "User harus puas" |

### 4.2.3 Story Splitting

Jika story terlalu besar (Epic), pecah menjadi story yang lebih kecil:

**Epic:** "As a mahasiswa, I want mengelola peminjaman buku"

**Stories:**
1. "As a mahasiswa, I want mencari buku berdasarkan judul"
2. "As a mahasiswa, I want melihat detail buku dan ketersediaannya"
3. "As a mahasiswa, I want meminjam buku secara online"
4. "As a mahasiswa, I want melihat daftar buku yang saya pinjam"
5. "As a mahasiswa, I want memperpanjang masa peminjaman"

## 4.3 Acceptance Criteria

### 4.3.1 Format Given-When-Then

```gherkin
Feature: Pencarian Buku

Scenario: Pencarian berdasarkan judul
  Given pustakawan sudah login ke sistem
  When pustakawan mencari buku dengan keyword "algoritma"
  Then sistem menampilkan daftar buku yang mengandung kata "algoritma"
  And setiap buku menampilkan judul, penulis, dan status ketersediaan

Scenario: Pencarian tanpa hasil
  Given mahasiswa sudah login ke sistem
  When mahasiswa mencari buku dengan keyword "xyzabc123"
  Then sistem menampilkan pesan "Buku tidak ditemukan"
  And sistem menyarankan keyword alternatif
```

### 4.3.2 Tips Menulis Acceptance Criteria

1. **Specific** — tulis kondisi yang jelas dan terukur
2. **Testable** — setiap criteria harus bisa di-automate sebagai test
3. **Complete** — cover happy path DAN edge cases
4. **Independent** — setiap scenario bisa dijalankan sendiri

## 4.4 Product Backlog & Prioritisasi

### 4.4.1 Product Backlog

Product Backlog adalah **daftar prioritas** semua yang dibutuhkan produk. Dikelola oleh Product Owner.

Contoh Product Backlog Sistem Perpustakaan:

| # | User Story | Prioritas | Story Points |
|---|------------|-----------|--------------|
| 1 | Login dengan NIM dan password | Must | 3 |
| 2 | Pencarian buku berdasarkan judul | Must | 5 |
| 3 | Peminjaman buku online | Must | 8 |
| 4 | Notifikasi batas pengembalian | Should | 5 |
| 5 | Filter pencarian (tahun, kategori) | Should | 3 |
| 6 | Dark mode | Could | 2 |
| 7 | Rekomendasi buku AI | Won't | 13 |

### 4.4.2 MoSCoW Method

| Prioritas | Deskripsi | Persentase Effort |
|-----------|-----------|-------------------|
| **Must** have | Wajib — sistem tidak berjalan tanpa ini | ~60% |
| **Should** have | Penting tapi tidak kritis | ~20% |
| **Could** have | Nice to have | ~20% |
| **Won't** have (now) | Tidak untuk rilis ini, bisa nanti | 0% |

### 4.4.3 Story Points & Estimation

Story points mengukur **relative effort**, bukan waktu absolut:

| Points | Effort | Contoh |
|--------|--------|--------|
| 1 | Trivial | Ubah warna tombol |
| 2 | Sederhana | Tambah field di form |
| 3 | Kecil | Halaman statis baru |
| 5 | Medium | CRUD sederhana |
| 8 | Besar | Fitur dengan integrasi API |
| 13 | Sangat besar | Fitur kompleks multi-komponen |
| 21 | Epic — perlu dipecah | Modul lengkap |

**Planning Poker:** Tim berdiskusi, lalu setiap anggota menunjukkan kartu estimasi secara bersamaan. Jika ada perbedaan besar, diskusikan alasannya.

---

## AI Corner: AI untuk User Stories (Level: Basic)

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| Generate user stories | "Buatkan 10 user stories format INVEST untuk Sistem E-Commerce UMKM" | Review apakah sesuai konteks pengguna |
| Buat acceptance criteria | "Buatkan acceptance criteria Given-When-Then untuk: 'As a pelanggan, I want checkout pesanan'" | Pastikan mencakup edge cases |
| Estimasi story points | "Berikan estimasi story points (skala Fibonacci) untuk user stories berikut: ..." | AI bisa memberikan baseline, tim yang memutuskan |

---

## Latihan Soal

### Level Dasar (C1-C2)
1. Sebutkan 5 elemen dalam Use Case Diagram.
2. Apa perbedaan antara `<<include>>` dan `<<extend>>`?
3. Jelaskan format user story dan berikan 3 contoh.
4. Sebutkan 6 kriteria INVEST.

### Level Menengah (C3-C4)
5. Buatlah Use Case Diagram untuk Sistem Informasi Perpustakaan Kampus dengan minimal 4 actors dan 8 use cases.
6. Tuliskan Use Case Narrative lengkap untuk "Peminjaman Buku Online".
7. Tulis 15 user stories (format INVEST) untuk Sistem Antrian Puskesmas, lengkap dengan acceptance criteria untuk 5 stories teratas.

### Level Mahir (C5-C6)
8. Evaluasi 10 user stories berikut menggunakan INVEST criteria — identifikasi masalah dan perbaiki.
9. Rancang Product Backlog lengkap untuk Aplikasi Pengelolaan Zakat dengan MoSCoW prioritization dan story points estimation.

---

## Rangkuman

1. **Use Case Diagram** memodelkan interaksi actor-sistem secara visual; **Use Case Narrative** mendetailkan alur (main, alternative, exception flow).
2. **User Stories** menggunakan format "As a [role], I want [feature], so that [benefit]" — fokus pada nilai bagi pengguna.
3. **INVEST criteria** memastikan user story: Independent, Negotiable, Valuable, Estimable, Small, Testable.
4. **Acceptance Criteria** dalam format Given-When-Then mendefinisikan kapan sebuah story "selesai".
5. **Product Backlog** adalah daftar prioritas semua kebutuhan, dikelola Product Owner.
6. **MoSCoW** (Must/Should/Could/Won't) membantu prioritisasi, **Story Points** membantu estimasi relative effort.

---

## Referensi

1. Cohn, M. (2004). *User Stories Applied: For Agile Software Development*. Addison-Wesley.
2. Cockburn, A. (2001). *Writing Effective Use Cases*. Addison-Wesley.
3. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 4. Pearson.
4. Rubin, K. S. (2012). *Essential Scrum*. Addison-Wesley.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
