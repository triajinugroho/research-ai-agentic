# Lab 04: User Story Mapping dan Backlog Prioritization

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 4 dari 13 |
| **Topik** | User Stories (INVEST), Acceptance Criteria (GWT), MoSCoW Prioritization, Product Backlog |
| **CPMK** | CPMK-2 (Menulis User Stories dengan kriteria INVEST dan Acceptance Criteria format Given-When-Then) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces, GitHub Issues |
| **Prasyarat** | Lab 01-03 selesai, memahami requirements engineering dari modul Minggu 4 |

---

## Tujuan

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. **Menulis** (C6) 15 user stories yang memenuhi kriteria INVEST
2. **Menyusun** (C6) acceptance criteria dalam format Given-When-Then (GWT) untuk setiap user story
3. **Menerapkan** (C3) teknik MoSCoW prioritization untuk mengurutkan backlog
4. **Mengestimasi** (C5) story points menggunakan Planning Poker dan membangun product backlog di GitHub Issues

---

## Konsep Singkat

### User Stories vs Requirements Tradisional

User story adalah cara Agile untuk menangkap kebutuhan pengguna dari sudut pandang pengguna itu sendiri. Berbeda dengan requirements tradisional yang ditulis dari perspektif sistem.

```
Requirements Tradisional vs User Story:

  Tradisional (System-centric):
  ┌────────────────────────────────────────────────────┐
  │ "Sistem harus menyediakan fitur pencarian buku     │
  │  berdasarkan judul, penulis, dan ISBN dengan       │
  │  response time < 2 detik"                          │
  └────────────────────────────────────────────────────┘

  User Story (User-centric):
  ┌────────────────────────────────────────────────────┐
  │ "Sebagai mahasiswa, saya ingin mencari buku        │
  │  berdasarkan judul atau penulis, sehingga saya     │
  │  bisa menemukan buku yang saya butuhkan dengan     │
  │  cepat tanpa harus browsing seluruh katalog"       │
  └────────────────────────────────────────────────────┘
```

### Format User Story

```
As a [role/persona],
I want [feature/capability],
So that [business value/benefit].

Contoh:
As a mahasiswa,
I want mencari buku berdasarkan judul,
So that saya bisa menemukan buku yang dibutuhkan dengan cepat.
```

### Kriteria INVEST

Setiap user story yang baik harus memenuhi 6 kriteria INVEST:

| Kriteria | Deskripsi | Contoh Baik | Contoh Buruk |
|----------|-----------|-------------|-------------|
| **I**ndependent | Tidak bergantung pada story lain | "Login dengan NIM" | "Login (tapi harus selesai setelah registrasi)" |
| **N**egotiable | Detail bisa dinegosiasi dengan PO | "Pencarian buku" (cara implementasi fleksibel) | "Pencarian harus pakai Elasticsearch" |
| **V**aluable | Memberikan nilai bagi pengguna | "Lihat stok buku real-time" | "Refactor database schema" |
| **E**stimable | Bisa diestimasi ukurannya | "Form login dengan validasi" | "Integrasi dengan semua sistem kampus" |
| **S**mall | Cukup kecil untuk 1 sprint | "Pencarian berdasarkan judul" | "Semua fitur perpustakaan" |
| **T**estable | Bisa dibuat test case-nya | "Login gagal tampilkan error" | "Sistem harus user-friendly" |

### Acceptance Criteria: Given-When-Then (GWT)

```
Given [initial context/precondition],
When  [action/event occurs],
Then  [expected outcome].

Contoh:
Given mahasiswa sudah login dan berada di halaman pencarian,
When  mahasiswa mengetik "algoritma" di kolom pencarian dan klik "Cari",
Then  sistem menampilkan daftar buku yang judulnya mengandung "algoritma"
      dan setiap hasil menampilkan judul, penulis, dan stok tersedia.
```

### MoSCoW Prioritization

| Kategori | Arti | Proporsi | Contoh |
|----------|------|----------|--------|
| **Must** | Wajib ada, sistem gagal tanpa ini | 60% | Login, pencarian, peminjaman |
| **Should** | Penting tapi sistem masih bisa jalan | 20% | Notifikasi, riwayat, filter |
| **Could** | Bagus jika ada, bukan prioritas | 15% | Dark mode, export PDF |
| **Won't** | Tidak untuk sprint/release ini | 5% | Mobile app, AI recommendation |

> **Referensi:** Materi lengkap tersedia di modul Minggu 4 (`week-04`) dan Bab 4 Buku Ajar.

---

## Persiapan

| Kebutuhan | Detail |
|-----------|--------|
| Tim | Kelompok 3-4 orang (sama dengan tim proyek) |
| SRS | Dokumen SRS dari Lab 03 (`docs/srs.md`) |
| GitHub Issues | Akses untuk membuat issues di repository tim |
| Alat estimasi | Kartu Planning Poker (atau jari tangan: 1-5, 8, 13) |

---

## Langkah-langkah

### Langkah 1: Identifikasi Persona dan Aktivitas Utama (10 menit)

**Mengapa:** Sebelum menulis user stories, tim harus memahami siapa pengguna sistem dan apa aktivitas utama mereka. User Story Map dimulai dari persona dan aktivitas, bukan fitur.

**Instruksi:**

1. Identifikasi 3 persona utama dari SRS Lab 03:

```markdown
## Persona

### Persona 1: Andi (Mahasiswa Semester 4)
- **Latar belakang:** Informatika, sering meminjam buku referensi
- **Tujuan:** Menemukan dan meminjam buku dengan cepat
- **Pain point:** Buku yang dicari sering tidak tersedia, tidak tahu kapan dikembalikan
- **Tech literacy:** Tinggi (familiar dengan aplikasi web)

### Persona 2: Bu Sari (Pustakawan Senior)
- **Latar belakang:** 10 tahun di perpustakaan UAI
- **Tujuan:** Mengelola koleksi buku dan peminjaman secara efisien
- **Pain point:** Pencatatan manual error-prone, sulit membuat laporan
- **Tech literacy:** Menengah (bisa pakai Microsoft Office)

### Persona 3: Pak Direktur (Kepala Perpustakaan)
- **Latar belakang:** Dosen yang merangkap jabatan struktural
- **Tujuan:** Melihat statistik dan membuat keputusan berdasarkan data
- **Pain point:** Tidak punya data real-time tentang utilisasi perpustakaan
- **Tech literacy:** Rendah (butuh dashboard yang simpel)
```

2. Identifikasi 4-5 aktivitas utama (user activities):

```
User Story Map - Aktivitas Utama:

  ┌──────────────┬────────────────┬───────────────┬──────────────┬─────────────┐
  │  Registrasi  │   Pencarian    │  Peminjaman   │ Pengembalian │  Pelaporan  │
  │  & Login     │   Buku         │  Buku         │ Buku         │  & Statistik│
  └──────┬───────┴───────┬────────┴──────┬────────┴──────┬───────┴──────┬──────┘
         │               │               │               │              │
    User tasks      User tasks      User tasks      User tasks     User tasks
    di bawah        di bawah        di bawah        di bawah       di bawah
```

**Expected Output:** Dokumen persona dan aktivitas utama yang akan menjadi kerangka story map.

---

### Langkah 2: Tulis 15 User Stories dengan INVEST (25 menit)

**Mengapa:** User stories adalah unit kerja terkecil yang bermakna bagi pengguna. Menulis 15 stories melatih kemampuan memecah kebutuhan besar menjadi increment yang bisa dikerjakan dalam sprint.

**Instruksi:**

Setiap anggota tim menulis 4-5 user stories, kemudian tim memvalidasi bersama. Gunakan format standar dan pastikan setiap story memenuhi INVEST.

Buat file `docs/user-stories.md`:

```markdown
# User Stories - Sistem Perpustakaan Digital UAI

## Aktivitas: Registrasi & Login

**US-01:** Sebagai mahasiswa, saya ingin mendaftar akun menggunakan NIM dan email kampus,
sehingga saya bisa mengakses sistem perpustakaan digital.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]

**US-02:** Sebagai mahasiswa, saya ingin login dengan NIM dan password,
sehingga saya bisa mengakses fitur peminjaman yang aman.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]

**US-03:** Sebagai mahasiswa, saya ingin mereset password via email,
sehingga saya tidak kehilangan akses jika lupa password.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]

## Aktivitas: Pencarian Buku

**US-04:** Sebagai mahasiswa, saya ingin mencari buku berdasarkan judul atau penulis,
sehingga saya bisa menemukan buku yang dibutuhkan dengan cepat.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]

**US-05:** Sebagai mahasiswa, saya ingin memfilter hasil pencarian berdasarkan kategori,
sehingga saya bisa mempersempit hasil pencarian.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]

**US-06:** Sebagai mahasiswa, saya ingin melihat detail buku (judul, penulis, sinopsis, stok),
sehingga saya bisa memutuskan apakah akan meminjam buku tersebut.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]

## Aktivitas: Peminjaman Buku

**US-07:** Sebagai mahasiswa, saya ingin meminjam buku secara online,
sehingga saya tidak perlu mengisi form manual di perpustakaan.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]

**US-08:** Sebagai mahasiswa, saya ingin melihat daftar buku yang sedang saya pinjam,
sehingga saya tahu kapan harus mengembalikan.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]

**US-09:** Sebagai mahasiswa, saya ingin menerima notifikasi H-3 sebelum deadline,
sehingga saya tidak terlambat mengembalikan buku.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]

## Aktivitas: Pengembalian Buku

**US-10:** Sebagai pustakawan, saya ingin memproses pengembalian buku dan update stok otomatis,
sehingga data inventaris selalu akurat.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]

**US-11:** Sebagai pustakawan, saya ingin melihat daftar peminjaman yang terlambat,
sehingga saya bisa mengirim reminder ke mahasiswa.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]

**US-12:** Sebagai sistem, denda harus dihitung otomatis (Rp 1.000/hari keterlambatan),
sehingga perhitungan konsisten dan transparan.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]

## Aktivitas: Pengelolaan & Pelaporan

**US-13:** Sebagai pustakawan, saya ingin menambah, mengedit, dan menghapus data buku,
sehingga katalog perpustakaan selalu up-to-date.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]

**US-14:** Sebagai kepala perpustakaan, saya ingin melihat dashboard statistik peminjaman,
sehingga saya bisa mengambil keputusan berbasis data.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]

**US-15:** Sebagai kepala perpustakaan, saya ingin mengekspor laporan bulanan ke PDF,
sehingga bisa dilaporkan ke pimpinan universitas.
- INVEST Check: I[v] N[v] V[v] E[v] S[v] T[v]
```

**Validasi INVEST secara kelompok:** Bacakan setiap story, tim mendiskusikan apakah memenuhi INVEST. Jika tidak, perbaiki bersama.

**Expected Output:** 15 user stories dengan INVEST check. Minimal 12 dari 15 harus memenuhi semua 6 kriteria INVEST.

**Estimasi waktu:** 25 menit

> **Diskusi kelas:** Apakah US-12 ("Sebagai sistem...") adalah user story yang baik? Mengapa atau mengapa tidak? Bagaimana seharusnya ditulis ulang?

---

### Langkah 3: Tulis Acceptance Criteria (Given-When-Then) (20 menit)

**Mengapa:** Acceptance Criteria (AC) mendefinisikan KAPAN sebuah user story dianggap "selesai". Tanpa AC, tidak ada cara objektif untuk menguji apakah implementasi sudah benar. Format GWT sangat cocok karena bisa langsung diterjemahkan menjadi automated test.

**Instruksi:**

Tulis acceptance criteria untuk **5 user stories prioritas tertinggi** menggunakan format Given-When-Then:

```gherkin
# US-02: Login dengan NIM dan password

Scenario 1: Login berhasil
  Given mahasiswa sudah terdaftar dengan NIM "20230001" dan password yang valid
  When mahasiswa mengisi form login dengan NIM "20230001" dan password yang benar
  Then sistem mengarahkan mahasiswa ke halaman dashboard
  And sistem menampilkan pesan "Selamat datang, [Nama Mahasiswa]"
  And session tersimpan selama 24 jam

Scenario 2: Login gagal - password salah
  Given mahasiswa sudah terdaftar dengan NIM "20230001"
  When mahasiswa mengisi form login dengan NIM "20230001" dan password yang salah
  Then sistem menampilkan pesan error "NIM atau password salah"
  And form login tetap ditampilkan (tidak redirect)
  And password field dikosongkan

Scenario 3: Login gagal - NIM tidak terdaftar
  Given NIM "99999999" tidak terdaftar di sistem
  When seseorang mengisi form login dengan NIM "99999999"
  Then sistem menampilkan pesan error "NIM atau password salah"
  And tidak memberitahu bahwa NIM tidak terdaftar (security)

Scenario 4: Login gagal - akun terkunci
  Given mahasiswa dengan NIM "20230001" sudah gagal login 5 kali berturut-turut
  When mahasiswa mencoba login lagi
  Then sistem menampilkan "Akun terkunci. Hubungi admin perpustakaan."
  And akun terkunci selama 30 menit
```

```gherkin
# US-04: Pencarian buku berdasarkan judul atau penulis

Scenario 1: Pencarian dengan hasil
  Given mahasiswa sudah login dan berada di halaman pencarian
  And database memiliki buku berjudul "Algoritma dan Pemrograman"
  When mahasiswa mengetik "algoritma" di kolom pencarian dan klik "Cari"
  Then sistem menampilkan daftar buku yang judulnya mengandung "algoritma"
  And setiap hasil menampilkan: judul, penulis, tahun terbit, dan stok tersedia
  And hasil diurutkan berdasarkan relevansi

Scenario 2: Pencarian tanpa hasil
  Given mahasiswa sudah login dan berada di halaman pencarian
  When mahasiswa mengetik "xyzabc123" di kolom pencarian dan klik "Cari"
  Then sistem menampilkan pesan "Tidak ada buku yang cocok dengan pencarian Anda"
  And menampilkan saran: "Coba gunakan kata kunci yang berbeda"

Scenario 3: Pencarian kosong
  Given mahasiswa sudah login dan berada di halaman pencarian
  When mahasiswa klik "Cari" tanpa mengisi kolom pencarian
  Then sistem menampilkan pesan "Masukkan kata kunci pencarian"
  And tidak melakukan query ke database
```

Tulis AC untuk 3 user stories lainnya (US-07, US-10, US-13) dengan pola serupa. Setiap story minimal 2 scenario (happy path + error/edge case).

**Expected Output:** 5 user stories memiliki acceptance criteria GWT, total minimal 12 scenario.

**Estimasi waktu:** 20 menit

> **Tips:** Scenario happy path (sukses) selalu ditulis pertama. Kemudian pikirkan: apa yang bisa salah? Input tidak valid? Kondisi batas? User tidak authorized?

---

### Langkah 4: MoSCoW Prioritization (15 menit)

**Mengapa:** Tidak semua fitur sama pentingnya. MoSCoW membantu tim dan PO menyepakati prioritas secara objektif. Dalam proyek dengan waktu terbatas (1 semester), fokus pada Must Have adalah kunci keberhasilan.

**Instruksi:**

1. PO memimpin diskusi prioritisasi. Untuk setiap story, tanyakan: "Bisakah sistem digunakan TANPA fitur ini?"
   - Jika TIDAK bisa → **Must**
   - Jika bisa tapi sangat kurang → **Should**
   - Jika bisa dan tetap berguna → **Could**
   - Jika di luar scope semester ini → **Won't**

2. Susun tabel prioritas:

```markdown
## MoSCoW Prioritization

### Must Have (Sistem tidak berfungsi tanpa ini)
| Story | Alasan |
|-------|--------|
| US-01 | Registrasi: entry point ke sistem |
| US-02 | Login: keamanan dasar |
| US-04 | Pencarian: fungsi utama perpustakaan |
| US-06 | Detail buku: informasi sebelum pinjam |
| US-07 | Peminjaman: core business process |
| US-10 | Pengembalian: melengkapi siklus peminjaman |
| US-13 | CRUD buku: pustakawan harus bisa kelola katalog |

### Should Have (Penting tapi sistem masih bisa jalan)
| Story | Alasan |
|-------|--------|
| US-03 | Reset password: penting tapi bisa ditangani manual |
| US-08 | Daftar pinjaman: convenience, bisa cek manual |
| US-11 | Daftar terlambat: penting untuk operasional |
| US-12 | Hitung denda: bisa dihitung manual sementara |

### Could Have (Nice to have)
| Story | Alasan |
|-------|--------|
| US-05 | Filter kategori: enhancement pencarian |
| US-09 | Notifikasi: value-add tapi bukan blocking |
| US-14 | Dashboard: bisa pakai spreadsheet sementara |

### Won't Have (Tidak untuk semester ini)
| Story | Alasan |
|-------|--------|
| US-15 | Export PDF: bisa dilakukan manual |
```

3. Verifikasi proporsi: Must (7/15 = 47%), Should (4/15 = 27%), Could (3/15 = 20%), Won't (1/15 = 7%).

**Expected Output:** Semua 15 stories terprioritaskan dengan alasan yang jelas.

**Estimasi waktu:** 15 menit

> **Diskusi kelas:** Bagaimana jika PO dan Developer tidak sepakat tentang prioritas? Siapa yang membuat keputusan akhir dalam Scrum?

---

### Langkah 5: Story Points Estimation dengan Planning Poker (15 menit)

**Mengapa:** Estimasi adalah kemampuan yang perlu dilatih. Planning Poker menggunakan wisdom of the crowd -- estimasi kolektif lebih akurat daripada estimasi individu. Skala Fibonacci (1,2,3,5,8,13) dipilih karena semakin besar sebuah item, semakin sulit mengestimasi dengan presisi tinggi.

**Instruksi:**

1. Tentukan **reference story** (story paling sederhana, dijadikan patokan 1 point):
   - Contoh: "US-06: Lihat detail buku" = **2 points** (hanya menampilkan data, tidak ada logika kompleks)

2. Lakukan Planning Poker untuk semua stories:

```
Prosedur Planning Poker:

  1. SM membacakan user story + acceptance criteria
  2. Tim berdiskusi 1-2 menit (klarifikasi, bukan debat)
  3. "3... 2... 1..." → semua tunjukkan estimasi bersamaan
     (gunakan jari tangan: 1-5, atau kertas untuk 8/13)
  4. Jika selisih ≤ 2: ambil nilai yang lebih tinggi
     Jika selisih > 2: yang terendah dan tertinggi menjelaskan
                        → diskusi 1 menit → voting ulang
```

3. Catat hasil di tabel:

```markdown
## Story Points Estimation

| Story | Prioritas | Points | Catatan Estimasi |
|-------|-----------|--------|-----------------|
| US-01 | Must | 3 | Registrasi + validasi NIM |
| US-02 | Must | 3 | Login + session + security |
| US-03 | Should | 5 | Email integration kompleks |
| US-04 | Must | 5 | Search + indexing + UI |
| US-05 | Could | 3 | Filter sederhana |
| US-06 | Must | 2 | Display data saja |
| US-07 | Must | 8 | Logika bisnis peminjaman + stok |
| US-08 | Should | 3 | Query + list display |
| US-09 | Could | 5 | Notification service |
| US-10 | Must | 5 | Pengembalian + update stok + denda |
| US-11 | Should | 3 | Query filter + list |
| US-12 | Should | 3 | Perhitungan denda sederhana |
| US-13 | Must | 5 | CRUD lengkap + validasi |
| US-14 | Could | 8 | Dashboard + grafik + query complex |
| US-15 | Won't | 5 | PDF generation |

**Total:** 66 points
**Must Have:** 31 points
**Velocity asumsi per sprint:** ~15-20 points
**Estimasi jumlah sprint:** 4-5 sprint
```

**Expected Output:** Semua stories memiliki story points, total dihitung, estimasi sprint diperkirakan.

---

### Langkah 6: Buat Product Backlog di GitHub Issues (15 menit)

**Mengapa:** Memindahkan user stories ke GitHub Issues menghubungkan perencanaan dengan implementasi. Setiap issue bisa di-assign, dilabeli, dan dilacak progressnya -- ini adalah praktik yang digunakan di industri.

**Instruksi:**

1. Untuk setiap user story, buat GitHub Issue dengan format:

```markdown
## Judul Issue: feat: [ringkasan user story]

### User Story
Sebagai [role], saya ingin [feature], sehingga [benefit].

### Acceptance Criteria
- [ ] Given ... When ... Then ...
- [ ] Given ... When ... Then ...

### Story Points: [N]
### Priority: [Must/Should/Could/Won't]

### Definition of Done
- [ ] Kode di-review oleh minimal 1 anggota tim
- [ ] Unit test ditulis dan passing
- [ ] Tidak ada linter warning
- [ ] Dokumentasi API diperbarui (jika relevan)
```

2. Tambahkan label ke setiap issue:
   - Priority: `must-have`, `should-have`, `could-have`, `wont-have`
   - Points: `1-point`, `2-points`, `3-points`, `5-points`, `8-points`
   - Type: `feature`, `enhancement`

3. Urutkan issues di GitHub Projects board berdasarkan prioritas MoSCoW

**Expected Output:** 15 GitHub Issues terbuat dengan label, description, dan acceptance criteria.

**Estimasi waktu:** 15 menit

Commit dokumentasi:

```bash
git add docs/user-stories.md
git commit -m "docs: tambah 15 user stories dengan INVEST, AC, dan MoSCoW"
git push origin main
```

> **Tips:** Di GitHub, gunakan template issue agar format konsisten untuk seluruh tim. Buat file `.github/ISSUE_TEMPLATE/user-story.md` untuk standarisasi.

---

## Tantangan Tambahan

### Tantangan 1: Dasar
Pecah US-07 (Peminjaman buku online) yang memiliki 8 story points menjadi **3 smaller stories** yang masing-masing 2-3 points. Ini disebut **story splitting**. Pastikan setiap sub-story tetap memenuhi INVEST dan memberikan value secara mandiri.

### Tantangan 2: Menengah
Buat **User Story Map** visual menggunakan Mermaid diagram atau ASCII art. Story map menunjukkan aktivitas pengguna (baris atas), user tasks (baris tengah), dan user stories (baris bawah) yang dikelompokkan per release/sprint.

### Tantangan 3: Lanjutan
Bandingkan proyek perpustakaan dengan proyek berskala lebih besar (misalnya e-commerce seperti Tokopedia). Identifikasi 5 **Epic** untuk Tokopedia, pecah masing-masing menjadi 3-5 user stories, dan jelaskan mengapa story splitting lebih menantang pada proyek berskala besar. Tulis analisis di `docs/epic-analysis.md`.

---

## Refleksi & AI Usage Log

Sebelum meninggalkan lab, isi refleksi berikut di file `docs/refleksi-lab-04.md`:

1. **Apa tantangan terbesar dalam menulis user stories yang memenuhi INVEST?**
2. **Kriteria INVEST mana yang paling sering dilanggar? Mengapa?**
3. **Bagaimana pengalaman estimasi Planning Poker? Apakah tim sering tidak sepakat?**
4. **Apa hubungan antara user stories di lab ini dengan SRS di Lab 03?**

Jika menggunakan AI selama lab, catat di **AI Usage Log**:

| Prompt yang Diberikan | Output AI | Modifikasi yang Dilakukan | Refleksi |
|----------------------|-----------|--------------------------|----------|
| (contoh prompt) | (ringkasan output) | (apa yang diubah) | (apa yang dipelajari) |

---

## Checklist Penyelesaian

- [ ] 3 persona teridentifikasi dengan latar belakang dan pain points
- [ ] 15 user stories tertulis dalam format "As a... I want... So that..."
- [ ] Setiap story divalidasi dengan INVEST (minimal 12/15 memenuhi semua kriteria)
- [ ] Acceptance criteria GWT untuk 5 stories prioritas tertinggi (minimal 12 scenario total)
- [ ] MoSCoW prioritization lengkap untuk semua 15 stories dengan alasan
- [ ] Story points estimation untuk semua stories menggunakan Planning Poker
- [ ] 15 GitHub Issues dibuat dengan label priority, points, dan acceptance criteria
- [ ] Product Backlog terurut di GitHub Projects board
- [ ] Dokumentasi tersimpan di `docs/user-stories.md` dan di-commit
- [ ] File refleksi `docs/refleksi-lab-04.md` terisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
