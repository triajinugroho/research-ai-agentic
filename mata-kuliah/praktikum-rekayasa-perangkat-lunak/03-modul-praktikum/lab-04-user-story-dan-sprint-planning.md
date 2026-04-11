# Lab 4: User Story dan Sprint Planning

## Informasi Praktikum

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Praktikum** | 4 dari 13 |
| **Topik** | User Story dan Sprint Planning |
| **CPMK** | CPMK-3 (Memodelkan kebutuhan perangkat lunak dengan user story dan sprint planning) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 1-3 selesai, SRS document di `docs/SRS.md` |

**Referensi Teori:** [IF2205 Minggu 4 — Pemodelan Requirements, Use Case, dan User Story](../../../rekayasa-perangkat-lunak/03-modules/week-04-pemodelan-requirements-use-case-dan-user-story.md)

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. **Menulis** (*compose* — C6) user stories yang memenuhi kriteria INVEST untuk Perpustakaan Digital UAI
2. **Menyusun** (*formulate* — C6) acceptance criteria menggunakan format Given-When-Then
3. **Memprioritaskan** (*evaluate* — C5) backlog menggunakan metode MoSCoW dan story points (Fibonacci)
4. **Mengkonfigurasi** (*configure* — C3) GitHub Issues dan GitHub Projects untuk manajemen sprint

---

## Konsep Singkat

### Dari Requirements ke User Stories

Di Lab 3, kita menulis requirements dalam format formal (FR-01, FR-02, ...). Sekarang kita **mengubah requirements tersebut menjadi user stories** — format yang lebih dekat dengan perspektif pengguna dan lebih mudah dikelola dalam framework Agile.

> Pelajari teori lengkap tentang pemodelan requirements dan user story di [Modul IF2205 Minggu 4](../../../rekayasa-perangkat-lunak/03-modules/week-04-pemodelan-requirements-use-case-dan-user-story.md).

### Anatomi User Story

```
┌──────────────────────────────────────────────────────────────┐
│                        USER STORY                            │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   "Sebagai [ROLE],                                           │
│    saya ingin [ACTION],                                      │
│    sehingga [BENEFIT]."                                      │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│   Acceptance Criteria:                                       │
│   ┌────────────────────────────────────────────────────────┐ │
│   │ GIVEN: kondisi awal                                    │ │
│   │ WHEN:  aksi yang dilakukan                             │ │
│   │ THEN:  hasil yang diharapkan                           │ │
│   └────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────┤
│   Story Points: 3 (Fibonacci)                                │
│   Priority: Must-have (MoSCoW)                               │
│   Labels: feature, must-have, sprint-1                       │
└──────────────────────────────────────────────────────────────┘
```

### Kriteria INVEST untuk User Story yang Baik

| Kriteria | Arti | Contoh Baik | Contoh Buruk |
|----------|------|-------------|--------------|
| **I**ndependent | Bisa dikerjakan sendiri | "Cari buku" | "Cari buku (butuh login dulu)" tanpa story login |
| **N**egotiable | Bisa didiskusikan | "Tampilkan daftar buku" | "Gunakan tabel Bootstrap 5.3.2 warna #2E7D32" |
| **V**aluable | Bernilai untuk pengguna | "Lihat ketersediaan buku" | "Buat model database" |
| **E**stimable | Bisa diestimasi effort-nya | "Form login dengan email + password" | "Buat keamanan sistem" |
| **S**mall | Cukup kecil untuk 1 sprint | "Tampilkan detail 1 buku" | "Buat seluruh modul perpustakaan" |
| **T**estable | Bisa ditest | "Pencarian return hasil dalam 2 detik" | "Sistem harus user-friendly" |

### MoSCoW Prioritization

```
┌─────────────────────────────────────────────────────┐
│                    MoSCoW                            │
├──────────────┬──────────────────────────────────────┤
│  Must-have   │ Tanpa ini, sistem TIDAK BISA release │
│  (60%)       │ Login, cari buku, pinjam buku        │
├──────────────┼──────────────────────────────────────┤
│  Should-have │ Penting tapi ada workaround           │
│  (20%)       │ Notifikasi, laporan statistik        │
├──────────────┼──────────────────────────────────────┤
│  Could-have  │ Nice to have jika waktu cukup        │
│  (15%)       │ Reservasi, rekomendasi dosen         │
├──────────────┼──────────────────────────────────────┤
│  Won't-have  │ Tidak dikerjakan semester ini         │
│  (5%)        │ E-book reader, multi-kampus          │
└──────────────┴──────────────────────────────────────┘
```

### Story Points (Fibonacci)

| Points | Effort | Contoh |
|--------|--------|--------|
| 1 | Sangat kecil (< 1 jam) | Ubah teks welcome message |
| 2 | Kecil (1-2 jam) | Tambah 1 route sederhana |
| 3 | Sedang (setengah hari) | Form input dengan validasi |
| 5 | Agak besar (1 hari) | CRUD lengkap 1 entitas |
| 8 | Besar (2-3 hari) | Modul autentikasi lengkap |
| 13 | Sangat besar (1 minggu) | Integrasi payment gateway |

> **Aturan:** Jika story > 8 points, **pecah menjadi story yang lebih kecil**.

---

## Persiapan

Sebelum praktikum dimulai, pastikan:

- [ ] Lab 3 selesai (SRS document ada di `docs/SRS.md`)
- [ ] Sudah membaca [Modul IF2205 Minggu 4](../../../rekayasa-perangkat-lunak/03-modules/week-04-pemodelan-requirements-use-case-dan-user-story.md)
- [ ] Memahami format user story: "Sebagai..., saya ingin..., sehingga..."
- [ ] Memiliki akses ke repository `perpustakaan-uai` di GitHub

**Tools yang akan digunakan:**

| Tool | Fungsi |
|------|--------|
| GitHub Issues | Membuat dan mengelola user stories |
| GitHub Projects | Kanban board untuk sprint planning |
| GitHub Labels | Kategorisasi prioritas dan tipe |
| Markdown | Dokumentasi user stories |

---

## Langkah-langkah

### Langkah 1: Menulis 15 User Stories (20 menit)

**Mengapa langkah ini penting:**
User stories menerjemahkan requirements teknis menjadi kebutuhan dari sudut pandang pengguna. Ini memastikan tim pengembang selalu **fokus pada value** yang diberikan ke pengguna, bukan hanya fitur teknis.

**Instruksi:**

1. Buka Codespace repository `perpustakaan-uai`
2. Buat branch baru:

```bash
git checkout develop
git pull origin develop
git checkout -b feature/user-stories
```

3. Buat file `docs/user-stories.md`:

```bash
cat > docs/user-stories.md << 'STORIES_EOF'
# User Stories — Perpustakaan Digital UAI

## Epic 1: Pencarian dan Katalog Buku

### US-01: Pencarian Buku
**Sebagai** mahasiswa,
**saya ingin** mencari buku berdasarkan judul, penulis, atau ISBN,
**sehingga** saya dapat menemukan buku yang saya butuhkan dengan cepat.

- **Priority:** Must-have
- **Story Points:** 5
- **Source:** FR-01
- **Sprint:** Sprint 1

### US-02: Melihat Detail Buku
**Sebagai** mahasiswa,
**saya ingin** melihat informasi lengkap sebuah buku (judul, penulis, ISBN, deskripsi, lokasi rak),
**sehingga** saya dapat memutuskan apakah buku tersebut sesuai kebutuhan saya.

- **Priority:** Must-have
- **Story Points:** 3
- **Source:** FR-02
- **Sprint:** Sprint 1

### US-03: Melihat Ketersediaan Buku
**Sebagai** mahasiswa,
**saya ingin** melihat status ketersediaan buku secara real-time,
**sehingga** saya tidak perlu datang ke perpustakaan untuk mengecek.

- **Priority:** Must-have
- **Story Points:** 2
- **Source:** FR-02
- **Sprint:** Sprint 1

### US-04: Filter Buku per Kategori
**Sebagai** mahasiswa,
**saya ingin** memfilter daftar buku berdasarkan kategori (Teknik Informatika, Ekonomi, dsb.),
**sehingga** saya dapat browse buku sesuai bidang studi saya.

- **Priority:** Should-have
- **Story Points:** 3
- **Source:** FR-01
- **Sprint:** Sprint 1

## Epic 2: Peminjaman dan Pengembalian

### US-05: Meminjam Buku Online
**Sebagai** mahasiswa,
**saya ingin** meminjam buku secara online,
**sehingga** saya tidak perlu antri di meja sirkulasi.

- **Priority:** Must-have
- **Story Points:** 8
- **Source:** FR-03
- **Sprint:** Sprint 2

### US-06: Melihat Riwayat Peminjaman
**Sebagai** mahasiswa,
**saya ingin** melihat riwayat semua buku yang pernah saya pinjam,
**sehingga** saya dapat melacak buku referensi yang pernah saya gunakan.

- **Priority:** Must-have
- **Story Points:** 3
- **Source:** FR-11
- **Sprint:** Sprint 2

### US-07: Notifikasi Deadline Pengembalian
**Sebagai** mahasiswa,
**saya ingin** mendapat notifikasi 3 hari sebelum deadline pengembalian,
**sehingga** saya tidak terkena denda keterlambatan.

- **Priority:** Should-have
- **Story Points:** 5
- **Source:** FR-05
- **Sprint:** Sprint 3

### US-08: Reservasi Buku
**Sebagai** mahasiswa,
**saya ingin** mereservasi buku yang sedang dipinjam orang lain,
**sehingga** saya mendapat prioritas ketika buku tersebut dikembalikan.

- **Priority:** Could-have
- **Story Points:** 5
- **Source:** FR-14
- **Sprint:** Sprint 3

## Epic 3: Manajemen Perpustakaan (Pustakawan)

### US-09: Menambah Buku Baru
**Sebagai** pustakawan,
**saya ingin** menambahkan data buku baru ke katalog,
**sehingga** koleksi perpustakaan selalu up-to-date.

- **Priority:** Must-have
- **Story Points:** 5
- **Source:** FR-06
- **Sprint:** Sprint 1

### US-10: Mengedit Data Buku
**Sebagai** pustakawan,
**saya ingin** mengubah informasi buku yang sudah ada,
**sehingga** data buku selalu akurat.

- **Priority:** Must-have
- **Story Points:** 3
- **Source:** FR-06
- **Sprint:** Sprint 1

### US-11: Memproses Pengembalian Buku
**Sebagai** pustakawan,
**saya ingin** memproses pengembalian buku dan menghitung denda otomatis,
**sehingga** proses pengembalian cepat dan akurat.

- **Priority:** Must-have
- **Story Points:** 5
- **Source:** FR-04, FR-13
- **Sprint:** Sprint 2

### US-12: Mengelola Data Anggota
**Sebagai** pustakawan,
**saya ingin** menambah, mengubah, dan menonaktifkan data anggota perpustakaan,
**sehingga** hanya anggota aktif yang dapat meminjam buku.

- **Priority:** Must-have
- **Story Points:** 5
- **Source:** FR-07
- **Sprint:** Sprint 2

## Epic 4: Autentikasi dan Pelaporan

### US-13: Login dengan Email UAI
**Sebagai** pengguna (mahasiswa/dosen/pustakawan),
**saya ingin** login menggunakan email @uai.ac.id,
**sehingga** identitas saya terverifikasi sebagai civitas UAI.

- **Priority:** Must-have
- **Story Points:** 8
- **Source:** FR-12
- **Sprint:** Sprint 1

### US-14: Dashboard Statistik
**Sebagai** kepala perpustakaan,
**saya ingin** melihat dashboard dengan statistik peminjaman, koleksi, dan anggota aktif,
**sehingga** saya dapat membuat keputusan berdasarkan data.

- **Priority:** Should-have
- **Story Points:** 8
- **Source:** FR-10
- **Sprint:** Sprint 3

### US-15: Laporan Bulanan
**Sebagai** kepala perpustakaan,
**saya ingin** mengunduh laporan peminjaman bulanan dalam format PDF,
**sehingga** saya dapat menyertakannya dalam laporan ke rektorat.

- **Priority:** Should-have
- **Story Points:** 5
- **Source:** FR-08
- **Sprint:** Sprint 3

## Ringkasan Story Points

| Epic | Stories | Total Points |
|------|---------|-------------|
| 1. Pencarian & Katalog | US-01 s/d US-04 | 13 |
| 2. Peminjaman & Pengembalian | US-05 s/d US-08 | 21 |
| 3. Manajemen (Pustakawan) | US-09 s/d US-12 | 18 |
| 4. Autentikasi & Pelaporan | US-13 s/d US-15 | 21 |
| **TOTAL** | **15 stories** | **73 points** |
STORIES_EOF
```

4. Commit:

```bash
git add docs/user-stories.md
git commit -m "docs(agile): write 15 user stories with INVEST criteria for Perpustakaan UAI

- 4 Epics: Katalog, Peminjaman, Manajemen, Auth & Laporan
- Each story has role, action, benefit, priority, and story points
- Total: 73 story points across 15 stories"
```

**Expected Output:**

File `docs/user-stories.md` berisi 15 user stories terorganisir dalam 4 epic, masing-masing dengan prioritas MoSCoW dan story points Fibonacci.

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| Story terlalu besar (> 8 points) | Pecah menjadi sub-stories yang lebih kecil |
| Story tidak jelas benefit-nya | Tanyakan: "Kenapa pengguna peduli dengan fitur ini?" |
| Bingung menentukan story points | Bandingkan dengan US yang sudah diestimasi — relatif, bukan absolut |

---

### Langkah 2: Menulis Acceptance Criteria untuk Top 5 Stories (15 menit)

**Mengapa langkah ini penting:**
Acceptance criteria mendefinisikan **kapan sebuah story dianggap selesai**. Tanpa AC yang jelas, developer dan product owner bisa memiliki ekspektasi yang berbeda tentang apa artinya "done".

**Instruksi:**

1. Buat file `docs/acceptance-criteria.md`:

```bash
cat > docs/acceptance-criteria.md << 'AC_EOF'
# Acceptance Criteria — Top 5 User Stories

## US-01: Pencarian Buku

### AC-01-1: Pencarian berdasarkan judul
```
GIVEN saya berada di halaman pencarian buku
WHEN saya mengetik "Algorithm" di kolom pencarian dan menekan tombol cari
THEN sistem menampilkan daftar buku yang judulnya mengandung kata "Algorithm"
AND setiap hasil menampilkan judul, penulis, dan status ketersediaan
AND hasil ditampilkan dalam waktu kurang dari 2 detik
```

### AC-01-2: Pencarian tanpa hasil
```
GIVEN saya berada di halaman pencarian buku
WHEN saya mencari dengan kata kunci yang tidak cocok dengan buku manapun
THEN sistem menampilkan pesan "Tidak ada buku yang ditemukan untuk 'xyz'"
AND sistem menyarankan untuk mengubah kata kunci pencarian
```

### AC-01-3: Pencarian dengan kolom kosong
```
GIVEN saya berada di halaman pencarian buku
WHEN saya menekan tombol cari tanpa mengisi kata kunci
THEN sistem menampilkan pesan validasi "Masukkan kata kunci pencarian"
AND fokus kembali ke kolom pencarian
```

---

## US-05: Meminjam Buku Online

### AC-05-1: Peminjaman berhasil
```
GIVEN saya sudah login sebagai mahasiswa
AND buku yang ingin dipinjam berstatus "Tersedia"
WHEN saya menekan tombol "Pinjam Buku" pada halaman detail buku
THEN sistem membuat record peminjaman dengan status "Dipinjam"
AND tanggal peminjaman diisi otomatis dengan tanggal hari ini
AND deadline pengembalian diisi otomatis 14 hari dari sekarang
AND stok buku berkurang 1
AND saya menerima konfirmasi dengan nomor referensi peminjaman
```

### AC-05-2: Peminjaman gagal — buku tidak tersedia
```
GIVEN saya sudah login sebagai mahasiswa
AND buku yang ingin dipinjam berstatus "Sedang dipinjam semua"
WHEN saya melihat halaman detail buku tersebut
THEN tombol "Pinjam Buku" tidak aktif (disabled)
AND pesan "Buku sedang tidak tersedia" ditampilkan
AND opsi "Reservasi" ditampilkan (jika fitur aktif)
```

### AC-05-3: Batas maksimal peminjaman
```
GIVEN saya sudah login sebagai mahasiswa
AND saya sudah meminjam 3 buku (batas maksimal)
WHEN saya mencoba meminjam buku ke-4
THEN sistem menampilkan pesan "Anda telah mencapai batas maksimal peminjaman (3 buku)"
AND peminjaman tidak diproses
```

---

## US-09: Menambah Buku Baru

### AC-09-1: Penambahan buku berhasil
```
GIVEN saya sudah login sebagai pustakawan
AND saya berada di halaman "Tambah Buku Baru"
WHEN saya mengisi semua field wajib (judul, penulis, ISBN, kategori, jumlah eksemplar)
AND menekan tombol "Simpan"
THEN data buku tersimpan di database
AND buku muncul di hasil pencarian
AND sistem menampilkan pesan "Buku berhasil ditambahkan"
AND saya diarahkan ke halaman detail buku yang baru dibuat
```

### AC-09-2: Validasi ISBN duplikat
```
GIVEN saya sudah login sebagai pustakawan
AND saya mengisi form tambah buku
WHEN saya memasukkan ISBN yang sudah ada di database
THEN sistem menampilkan pesan "ISBN sudah terdaftar di sistem"
AND menampilkan link ke buku yang memiliki ISBN tersebut
AND buku baru tidak disimpan
```

---

## US-13: Login dengan Email UAI

### AC-13-1: Login berhasil
```
GIVEN saya berada di halaman login
WHEN saya memasukkan email @uai.ac.id yang terdaftar dan password yang benar
THEN saya diarahkan ke halaman dashboard
AND nama saya ditampilkan di navbar
AND session login berlaku selama 8 jam
```

### AC-13-2: Login gagal — email non-UAI
```
GIVEN saya berada di halaman login
WHEN saya memasukkan email yang bukan @uai.ac.id (contoh: user@gmail.com)
THEN sistem menampilkan pesan "Hanya email @uai.ac.id yang diizinkan"
AND login tidak diproses
```

### AC-13-3: Login gagal — password salah
```
GIVEN saya berada di halaman login
WHEN saya memasukkan email @uai.ac.id yang terdaftar tapi password salah
THEN sistem menampilkan pesan "Email atau password salah"
AND setelah 5 kali gagal, akun terkunci selama 15 menit
```

---

## US-11: Memproses Pengembalian Buku

### AC-11-1: Pengembalian tepat waktu
```
GIVEN saya sudah login sebagai pustakawan
AND ada mahasiswa yang mengembalikan buku sebelum deadline
WHEN saya memproses pengembalian dengan memasukkan nomor referensi peminjaman
THEN status peminjaman berubah menjadi "Dikembalikan"
AND stok buku bertambah 1
AND denda = Rp 0
AND sistem menampilkan pesan "Pengembalian berhasil — tepat waktu"
```

### AC-11-2: Pengembalian terlambat
```
GIVEN saya sudah login sebagai pustakawan
AND ada mahasiswa yang mengembalikan buku 5 hari setelah deadline
WHEN saya memproses pengembalian
THEN status peminjaman berubah menjadi "Dikembalikan (Terlambat)"
AND denda dihitung otomatis: 5 hari x Rp 1.000 = Rp 5.000
AND sistem menampilkan detail denda kepada pustakawan
```
AC_EOF
```

2. Commit:

```bash
git add docs/acceptance-criteria.md
git commit -m "docs(agile): write Given-When-Then acceptance criteria for top 5 user stories

- US-01 (Pencarian): 3 acceptance criteria
- US-05 (Peminjaman): 3 acceptance criteria
- US-09 (Tambah Buku): 2 acceptance criteria
- US-13 (Login): 3 acceptance criteria
- US-11 (Pengembalian): 2 acceptance criteria"
```

**Expected Output:**

File `docs/acceptance-criteria.md` berisi 13 acceptance criteria untuk 5 user stories dalam format Given-When-Then.

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| GIVEN/WHEN/THEN membingungkan | GIVEN = setup, WHEN = aksi pengguna, THEN = hasil yang diharapkan |
| AC terlalu detail | Fokus pada perilaku (behavior), bukan implementasi teknis |
| Lupa edge cases | Selalu pikirkan: apa yang terjadi jika input salah? Jika kosong? Jika duplikat? |

---

### Langkah 3: Setup GitHub Labels (10 menit)

**Mengapa langkah ini penting:**
Labels membantu **mengkategorikan dan memfilter** issues dengan cepat. Tanpa labels, seiring bertambahnya issues, akan sulit membedakan mana yang urgent dan mana yang bisa ditunda.

**Instruksi:**

Kita akan membuat labels menggunakan GitHub CLI (`gh`) yang tersedia di Codespaces:

```bash
# Hapus default labels yang tidak diperlukan
gh label delete "bug" --yes 2>/dev/null
gh label delete "documentation" --yes 2>/dev/null
gh label delete "duplicate" --yes 2>/dev/null
gh label delete "enhancement" --yes 2>/dev/null
gh label delete "good first issue" --yes 2>/dev/null
gh label delete "help wanted" --yes 2>/dev/null
gh label delete "invalid" --yes 2>/dev/null
gh label delete "question" --yes 2>/dev/null
gh label delete "wontfix" --yes 2>/dev/null

# Buat labels untuk MoSCoW prioritization
gh label create "must-have" --description "Harus ada di release" --color "B60205"
gh label create "should-have" --description "Penting tapi ada workaround" --color "D93F0B"
gh label create "could-have" --description "Nice to have" --color "FBCA04"
gh label create "wont-have" --description "Tidak di scope semester ini" --color "D4C5F9"

# Buat labels untuk tipe
gh label create "user-story" --description "User story" --color "0075CA"
gh label create "bug" --description "Bug fix" --color "E11D48"
gh label create "docs" --description "Dokumentasi" --color "0E8A16"
gh label create "chore" --description "Maintenance task" --color "C2E0C6"

# Buat labels untuk sprint
gh label create "sprint-0" --description "Sprint 0: Setup & Planning" --color "BFD4F2"
gh label create "sprint-1" --description "Sprint 1: Core Features" --color "7DC4E4"
gh label create "sprint-2" --description "Sprint 2: Extended Features" --color "4A90D9"
gh label create "sprint-3" --description "Sprint 3: Polish & Reports" --color "1D76DB"

# Buat labels untuk epic
gh label create "epic:katalog" --description "Epic: Pencarian & Katalog" --color "5319E7"
gh label create "epic:peminjaman" --description "Epic: Peminjaman & Pengembalian" --color "8B5CF6"
gh label create "epic:manajemen" --description "Epic: Manajemen Perpustakaan" --color "A855F7"
gh label create "epic:auth-laporan" --description "Epic: Autentikasi & Pelaporan" --color "C084FC"

# Buat labels untuk story points
gh label create "sp:1" --description "Story Point: 1" --color "E6E6E6"
gh label create "sp:2" --description "Story Point: 2" --color "D4D4D4"
gh label create "sp:3" --description "Story Point: 3" --color "BFBFBF"
gh label create "sp:5" --description "Story Point: 5" --color "A3A3A3"
gh label create "sp:8" --description "Story Point: 8" --color "737373"
```

**Expected Output:**

Setiap perintah `gh label create` menampilkan:

```
Creating label "must-have" in owner/perpustakaan-uai
```

Verifikasi di browser: Settings > Labels — seharusnya ada 20+ labels baru.

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| `gh: command not found` | Jalankan: `gh auth login` dan ikuti instruksi autentikasi |
| "Label already exists" | Abaikan error tersebut, label sudah ada |
| "Resource not accessible" | Pastikan Anda memiliki akses write ke repository |

---

### Langkah 4: Membuat GitHub Issues untuk Setiap User Story (20 menit)

**Mengapa langkah ini penting:**
GitHub Issues adalah **single source of truth** untuk tracking pekerjaan. Setiap user story menjadi satu issue yang bisa di-assign, dilabel, dan dipindahkan di project board.

**Instruksi:**

Buat issue untuk setiap user story menggunakan `gh`:

```bash
# US-01: Pencarian Buku
gh issue create \
  --title "US-01: Pencarian buku berdasarkan judul, penulis, atau ISBN" \
  --body "**Sebagai** mahasiswa,
**saya ingin** mencari buku berdasarkan judul, penulis, atau ISBN,
**sehingga** saya dapat menemukan buku yang saya butuhkan dengan cepat.

## Acceptance Criteria
- [ ] Pencarian by judul menampilkan hasil yang relevan
- [ ] Pencarian by penulis menampilkan hasil yang relevan
- [ ] Pencarian by ISBN menampilkan buku yang tepat
- [ ] Hasil pencarian kosong menampilkan pesan informatif
- [ ] Response time < 2 detik

## Notes
- Source: FR-01
- Story Points: 5" \
  --label "user-story,must-have,sprint-1,epic:katalog,sp:5"
```

```bash
# US-02: Melihat Detail Buku
gh issue create \
  --title "US-02: Melihat informasi lengkap sebuah buku" \
  --body "**Sebagai** mahasiswa,
**saya ingin** melihat informasi lengkap sebuah buku (judul, penulis, ISBN, deskripsi, lokasi rak),
**sehingga** saya dapat memutuskan apakah buku tersebut sesuai kebutuhan saya.

## Acceptance Criteria
- [ ] Halaman detail menampilkan semua informasi buku
- [ ] Status ketersediaan terlihat jelas
- [ ] Ada tombol aksi (pinjam/reservasi)

## Notes
- Source: FR-02
- Story Points: 3" \
  --label "user-story,must-have,sprint-1,epic:katalog,sp:3"
```

```bash
# US-03: Melihat Ketersediaan Buku
gh issue create \
  --title "US-03: Melihat status ketersediaan buku secara real-time" \
  --body "**Sebagai** mahasiswa,
**saya ingin** melihat status ketersediaan buku secara real-time,
**sehingga** saya tidak perlu datang ke perpustakaan untuk mengecek.

## Acceptance Criteria
- [ ] Status tersedia/dipinjam ditampilkan di listing buku
- [ ] Jumlah eksemplar tersedia ditampilkan
- [ ] Status update otomatis setelah peminjaman/pengembalian

## Notes
- Source: FR-02
- Story Points: 2" \
  --label "user-story,must-have,sprint-1,epic:katalog,sp:2"
```

```bash
# US-04: Filter Buku per Kategori
gh issue create \
  --title "US-04: Filter daftar buku berdasarkan kategori" \
  --body "**Sebagai** mahasiswa,
**saya ingin** memfilter daftar buku berdasarkan kategori,
**sehingga** saya dapat browse buku sesuai bidang studi saya.

## Acceptance Criteria
- [ ] Dropdown/sidebar filter kategori tersedia
- [ ] Filter bisa dikombinasikan dengan pencarian
- [ ] Jumlah buku per kategori ditampilkan

## Notes
- Source: FR-01
- Story Points: 3" \
  --label "user-story,should-have,sprint-1,epic:katalog,sp:3"
```

```bash
# US-05: Meminjam Buku Online
gh issue create \
  --title "US-05: Meminjam buku secara online" \
  --body "**Sebagai** mahasiswa,
**saya ingin** meminjam buku secara online,
**sehingga** saya tidak perlu antri di meja sirkulasi.

## Acceptance Criteria
- [ ] Tombol pinjam aktif jika buku tersedia dan user sudah login
- [ ] Peminjaman mencatat tanggal pinjam dan deadline otomatis (14 hari)
- [ ] Stok buku berkurang setelah peminjaman
- [ ] Konfirmasi dengan nomor referensi ditampilkan
- [ ] Batas maksimal 3 buku per mahasiswa

## Notes
- Source: FR-03
- Story Points: 8" \
  --label "user-story,must-have,sprint-2,epic:peminjaman,sp:8"
```

```bash
# US-06: Melihat Riwayat Peminjaman
gh issue create \
  --title "US-06: Melihat riwayat semua buku yang pernah dipinjam" \
  --body "**Sebagai** mahasiswa,
**saya ingin** melihat riwayat semua buku yang pernah saya pinjam,
**sehingga** saya dapat melacak buku referensi yang pernah saya gunakan.

## Acceptance Criteria
- [ ] Daftar peminjaman aktif dan selesai ditampilkan
- [ ] Setiap entry menampilkan judul, tanggal pinjam, deadline, status
- [ ] Bisa di-sort berdasarkan tanggal

## Notes
- Source: FR-11
- Story Points: 3" \
  --label "user-story,must-have,sprint-2,epic:peminjaman,sp:3"
```

```bash
# US-07 s/d US-15 (lanjutkan pola yang sama)
# US-07
gh issue create \
  --title "US-07: Notifikasi email 3 hari sebelum deadline pengembalian" \
  --body "**Sebagai** mahasiswa,
**saya ingin** mendapat notifikasi 3 hari sebelum deadline pengembalian,
**sehingga** saya tidak terkena denda keterlambatan.

## Acceptance Criteria
- [ ] Email terkirim H-3 sebelum deadline
- [ ] Email berisi judul buku dan tanggal deadline
- [ ] Notifikasi hanya untuk peminjaman aktif

## Notes
- Source: FR-05
- Story Points: 5" \
  --label "user-story,should-have,sprint-3,epic:peminjaman,sp:5"

# US-08
gh issue create \
  --title "US-08: Reservasi buku yang sedang dipinjam" \
  --body "**Sebagai** mahasiswa,
**saya ingin** mereservasi buku yang sedang dipinjam orang lain,
**sehingga** saya mendapat prioritas ketika buku tersebut dikembalikan.

## Acceptance Criteria
- [ ] Tombol reservasi muncul jika buku tidak tersedia
- [ ] Notifikasi dikirim saat buku tersedia
- [ ] Reservasi berlaku 3 hari setelah buku tersedia

## Notes
- Source: FR-14
- Story Points: 5" \
  --label "user-story,could-have,sprint-3,epic:peminjaman,sp:5"

# US-09
gh issue create \
  --title "US-09: Menambahkan data buku baru ke katalog" \
  --body "**Sebagai** pustakawan,
**saya ingin** menambahkan data buku baru ke katalog,
**sehingga** koleksi perpustakaan selalu up-to-date.

## Acceptance Criteria
- [ ] Form input semua field buku (judul, penulis, ISBN, kategori, jumlah)
- [ ] Validasi ISBN tidak duplikat
- [ ] Konfirmasi setelah berhasil simpan

## Notes
- Source: FR-06
- Story Points: 5" \
  --label "user-story,must-have,sprint-1,epic:manajemen,sp:5"

# US-10
gh issue create \
  --title "US-10: Mengubah informasi buku yang sudah ada" \
  --body "**Sebagai** pustakawan,
**saya ingin** mengubah informasi buku yang sudah ada,
**sehingga** data buku selalu akurat.

## Acceptance Criteria
- [ ] Form edit pre-filled dengan data existing
- [ ] Validasi input sebelum simpan
- [ ] Riwayat perubahan tercatat

## Notes
- Source: FR-06
- Story Points: 3" \
  --label "user-story,must-have,sprint-1,epic:manajemen,sp:3"

# US-11
gh issue create \
  --title "US-11: Memproses pengembalian buku dan hitung denda otomatis" \
  --body "**Sebagai** pustakawan,
**saya ingin** memproses pengembalian buku dan menghitung denda otomatis,
**sehingga** proses pengembalian cepat dan akurat.

## Acceptance Criteria
- [ ] Input nomor referensi peminjaman
- [ ] Denda dihitung otomatis (Rp 1.000/hari keterlambatan)
- [ ] Status berubah ke Dikembalikan
- [ ] Stok buku bertambah

## Notes
- Source: FR-04, FR-13
- Story Points: 5" \
  --label "user-story,must-have,sprint-2,epic:manajemen,sp:5"

# US-12
gh issue create \
  --title "US-12: Mengelola data anggota perpustakaan" \
  --body "**Sebagai** pustakawan,
**saya ingin** menambah, mengubah, dan menonaktifkan data anggota perpustakaan,
**sehingga** hanya anggota aktif yang dapat meminjam buku.

## Acceptance Criteria
- [ ] CRUD operations untuk data anggota
- [ ] Bisa menonaktifkan anggota (soft delete)
- [ ] Filter anggota aktif/nonaktif

## Notes
- Source: FR-07
- Story Points: 5" \
  --label "user-story,must-have,sprint-2,epic:manajemen,sp:5"

# US-13
gh issue create \
  --title "US-13: Login menggunakan email @uai.ac.id" \
  --body "**Sebagai** pengguna (mahasiswa/dosen/pustakawan),
**saya ingin** login menggunakan email @uai.ac.id,
**sehingga** identitas saya terverifikasi sebagai civitas UAI.

## Acceptance Criteria
- [ ] Form login email + password
- [ ] Hanya email @uai.ac.id yang diterima
- [ ] Password dienkripsi dengan bcrypt
- [ ] Session berlaku 8 jam
- [ ] Akun terkunci setelah 5x gagal login

## Notes
- Source: FR-12
- Story Points: 8" \
  --label "user-story,must-have,sprint-1,epic:auth-laporan,sp:8"

# US-14
gh issue create \
  --title "US-14: Dashboard statistik peminjaman dan koleksi" \
  --body "**Sebagai** kepala perpustakaan,
**saya ingin** melihat dashboard dengan statistik peminjaman, koleksi, dan anggota aktif,
**sehingga** saya dapat membuat keputusan berdasarkan data.

## Acceptance Criteria
- [ ] Tampilkan total buku, anggota aktif, peminjaman bulan ini
- [ ] Grafik tren peminjaman 6 bulan terakhir
- [ ] Top 10 buku paling sering dipinjam

## Notes
- Source: FR-10
- Story Points: 8" \
  --label "user-story,should-have,sprint-3,epic:auth-laporan,sp:8"

# US-15
gh issue create \
  --title "US-15: Laporan peminjaman bulanan dalam format PDF" \
  --body "**Sebagai** kepala perpustakaan,
**saya ingin** mengunduh laporan peminjaman bulanan dalam format PDF,
**sehingga** saya dapat menyertakannya dalam laporan ke rektorat.

## Acceptance Criteria
- [ ] Pilih bulan dan tahun untuk generate laporan
- [ ] Laporan berisi statistik peminjaman, top buku, grafik
- [ ] Output dalam format PDF yang rapi

## Notes
- Source: FR-08
- Story Points: 5" \
  --label "user-story,should-have,sprint-3,epic:auth-laporan,sp:5"
```

**Expected Output:**

Setelah menjalankan semua perintah di atas, buka tab **Issues** di repository GitHub. Seharusnya ada **15 issues** baru, masing-masing dengan labels yang sesuai.

Verifikasi:

```bash
gh issue list --limit 20
```

Output:

```
#15  US-15: Laporan peminjaman bulanan dalam format PDF          ...
#14  US-14: Dashboard statistik peminjaman dan koleksi           ...
...
#1   US-01: Pencarian buku berdasarkan judul, penulis, atau ISBN ...
```

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| "Label not found" | Pastikan Langkah 3 sudah dijalankan (labels sudah dibuat) |
| Issue tidak muncul | Cek: `gh issue list` — mungkin perlu refresh halaman browser |
| Terlalu lama mengetik | Copy-paste dari modul ini, atau gunakan script bash |

---

### Langkah 5: Setup GitHub Projects Board (15 menit)

**Mengapa langkah ini penting:**
Project board memberikan **visualisasi status pekerjaan** di satu tempat. Dengan board, seluruh tim bisa melihat apa yang sedang dikerjakan, apa yang menunggu review, dan apa yang sudah selesai.

**Instruksi:**

1. Di browser, buka repository > tab **Projects** > **New project**
2. Pilih template **Board** (Kanban)
3. Nama: `Sprint Board — Perpustakaan Digital UAI`
4. Klik **Create project**

5. Rename kolom default dan tambah kolom baru:
   - **Backlog** (rename dari "No status")
   - **Sprint 0 - Planning** (tambah baru)
   - **To Do** (rename jika perlu)
   - **In Progress**
   - **In Review**
   - **Done**

6. Tambahkan semua 15 issues ke project:
   - Klik **+ Add item** di kolom Backlog
   - Ketik `#` dan pilih issues dari repository
   - Atau gunakan CLI:

```bash
# Dapatkan project number (biasanya 1 untuk project pertama)
# Tambahkan issue ke project via web interface karena gh project
# memerlukan project ID yang spesifik
echo "Tambahkan 15 issues ke project board melalui web interface GitHub."
echo "Klik + Add item di kolom Backlog, ketik # dan pilih setiap issue."
```

7. Pindahkan issues ke kolom yang sesuai:
   - **Sprint 0 - Planning:** Semua issues sprint-1 (US-01, 02, 03, 04, 09, 10, 13) = 7 issues
   - **Backlog:** Sisanya (US-05, 06, 07, 08, 11, 12, 14, 15) = 8 issues

**Expected Output:**

Project board menampilkan:

```
┌─────────────┬─────────────────────┬──────────┬─────────────┬───────────┬──────────┐
│   Backlog   │ Sprint 0 - Planning │  To Do   │ In Progress │ In Review │   Done   │
│   (8)       │       (7)           │  (0)     │    (0)      │   (0)     │   (0)    │
├─────────────┼─────────────────────┼──────────┼─────────────┼───────────┼──────────┤
│ US-05       │ US-01               │          │             │           │          │
│ US-06       │ US-02               │          │             │           │          │
│ US-07       │ US-03               │          │             │           │          │
│ US-08       │ US-04               │          │             │           │          │
│ US-11       │ US-09               │          │             │           │          │
│ US-12       │ US-10               │          │             │           │          │
│ US-14       │ US-13               │          │             │           │          │
│ US-15       │                     │          │             │           │          │
└─────────────┴─────────────────────┴──────────┴─────────────┴───────────┴──────────┘
```

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| Projects tab tidak muncul | Pastikan repository bersifat Public, atau aktifkan Projects di Settings |
| Tidak bisa drag-and-drop issue | Refresh halaman, pastikan browser mendukung |
| Kolom tidak bisa ditambah | Klik **+** di sebelah kanan kolom terakhir |

---

### Langkah 6: Perencanaan Sprint 0 (10 menit)

**Mengapa langkah ini penting:**
Sprint planning menentukan **apa yang akan dikerjakan dalam sprint mendatang** berdasarkan kapasitas tim. Sprint 0 khusus untuk **setup fondasi** (environment, arsitektur, data model) sebelum mulai membangun fitur.

**Instruksi:**

1. Buat file `docs/sprint-planning.md`:

```bash
cat > docs/sprint-planning.md << 'SPRINT_EOF'
# Sprint Planning — Perpustakaan Digital UAI

## Tim

| Peran | Nama | Kapasitas/Sprint |
|-------|------|-----------------|
| Product Owner | [Nama PO] | Review & prioritas |
| Scrum Master | [Nama SM] | Fasilitasi & tracking |
| Developer 1 | [Nama Dev 1] | 15 story points |
| Developer 2 | [Nama Dev 2] | 15 story points |
| Developer 3 | [Nama Dev 3] | 15 story points |

**Kapasitas tim per sprint:** ~45 story points (3 developer x 15 SP)

## Sprint 0: Setup & Planning (Minggu 1-4)

**Goal:** Fondasi teknis dan dokumentasi siap, tim bisa mulai develop fitur.

**Deliverables:**

| Item | Deskripsi | Status |
|------|-----------|--------|
| Dev Environment | Codespace + devcontainer + Flask (Lab 1) | Done |
| Git Workflow | Branching strategy + PR workflow (Lab 2) | Done |
| SRS Document | IEEE 830 compliant (Lab 3) | Done |
| User Stories | 15 stories + acceptance criteria (Lab 4) | Done |
| Project Board | GitHub Projects setup | Done |

**Sprint 0 tidak memiliki story points** — ini adalah sprint persiapan.

## Sprint 1: Core Features (Target)

**Goal:** Pengguna bisa mencari buku dan pustakawan bisa mengelola katalog.

| Story | Points | Assignee | Sprint Target |
|-------|--------|----------|--------------|
| US-01: Pencarian buku | 5 | Dev 1 | Sprint 1 |
| US-02: Detail buku | 3 | Dev 1 | Sprint 1 |
| US-03: Ketersediaan buku | 2 | Dev 1 | Sprint 1 |
| US-04: Filter kategori | 3 | Dev 2 | Sprint 1 |
| US-09: Tambah buku | 5 | Dev 2 | Sprint 1 |
| US-10: Edit buku | 3 | Dev 2 | Sprint 1 |
| US-13: Login email UAI | 8 | Dev 3 | Sprint 1 |
| **Total** | **29** | | |

**Kapasitas: 45 SP, Planned: 29 SP** — Buffer 36% untuk unexpected tasks.

## Sprint 2: Extended Features (Target)

| Story | Points | Sprint Target |
|-------|--------|--------------|
| US-05: Peminjaman online | 8 | Sprint 2 |
| US-06: Riwayat peminjaman | 3 | Sprint 2 |
| US-11: Pengembalian + denda | 5 | Sprint 2 |
| US-12: Kelola anggota | 5 | Sprint 2 |
| **Total** | **21** | |

## Sprint 3: Polish & Reports (Target)

| Story | Points | Sprint Target |
|-------|--------|--------------|
| US-07: Notifikasi deadline | 5 | Sprint 3 |
| US-08: Reservasi buku | 5 | Sprint 3 |
| US-14: Dashboard statistik | 8 | Sprint 3 |
| US-15: Laporan PDF | 5 | Sprint 3 |
| **Total** | **23** | |

## Velocity Chart (Estimasi)

```
Story Points
     50 │
     40 │        ┌───┐
     30 │ ┌───┐  │   │
     20 │ │   │  │   │  ┌───┐
     10 │ │   │  │   │  │   │
      0 └─┴───┴──┴───┴──┴───┴──
        Sprint 1  Sprint 2  Sprint 3
         29 SP     21 SP     23 SP
```

## Definition of Done (DoD)

Sebuah user story dianggap "Done" jika:

- [ ] Kode di-push ke feature branch
- [ ] Pull Request dibuat dengan deskripsi lengkap
- [ ] Code review dilakukan (minimal 1 reviewer)
- [ ] Semua acceptance criteria terpenuhi
- [ ] Unit test ditulis dan passed (Lab 9+)
- [ ] PR di-merge ke develop tanpa conflict
- [ ] Didemokan ke Product Owner
SPRINT_EOF
```

2. Commit dan push:

```bash
git add docs/sprint-planning.md
git commit -m "docs(agile): add sprint planning with velocity estimation

- Sprint 0: setup & planning (completed)
- Sprint 1: 29 SP (core features)
- Sprint 2: 21 SP (extended features)
- Sprint 3: 23 SP (polish & reports)
- Definition of Done defined"
```

```bash
git push -u origin feature/user-stories
```

**Expected Output:**

File `docs/sprint-planning.md` berisi rencana 3 sprint + Sprint 0, lengkap dengan distribusi story points dan definition of done.

---

### Langkah 7: Push dan Buat Pull Request (10 menit)

**Mengapa langkah ini penting:**
Semua dokumentasi Agile planning harus masuk ke repository melalui PR — konsisten dengan workflow yang kita pelajari di Lab 2.

**Instruksi:**

1. Verifikasi semua file yang dibuat:

```bash
git log --oneline
```

Expected (3 commits di branch ini):

```
abc1234 docs(agile): add sprint planning with velocity estimation
def5678 docs(agile): write Given-When-Then acceptance criteria for top 5 user stories
ghi9012 docs(agile): write 15 user stories with INVEST criteria for Perpustakaan UAI
```

2. Buat Pull Request di GitHub:
   - **Base:** `develop`
   - **Compare:** `feature/user-stories`
   - **Title:** `docs(agile): add user stories, acceptance criteria, and sprint planning`
   - **Description:**

```markdown
## Ringkasan

Menambahkan dokumentasi Agile planning lengkap untuk Perpustakaan Digital UAI.

## Dokumen yang Ditambahkan

- `docs/user-stories.md` — 15 user stories (4 epics, 73 total story points)
- `docs/acceptance-criteria.md` — Given-When-Then AC untuk 5 top stories
- `docs/sprint-planning.md` — Sprint 0-3 planning + Definition of Done

## GitHub Setup

- 20+ labels dibuat (MoSCoW, sprint, epic, story points)
- 15 GitHub Issues dibuat untuk setiap user story
- GitHub Projects board dikonfigurasi (6 kolom)

## Checklist

- [x] 15 user stories format INVEST
- [x] Acceptance criteria Given-When-Then untuk top 5
- [x] MoSCoW prioritization diterapkan
- [x] Story points Fibonacci
- [x] GitHub Issues dan Labels
- [x] GitHub Projects board
- [x] Sprint 0 backlog defined
```

3. Merge PR setelah review

---

## Tantangan Tambahan

### Tantangan 1: Story Map (Basic)

Buat **User Story Map** untuk Epic 1 (Pencarian & Katalog) dengan format:

```
User Activity:   Mencari Buku ──────────────────────────────>
                     │
User Tasks:     Buka halaman  │  Ketik keyword  │  Lihat hasil  │  Lihat detail
                     │              │                │              │
Stories:        US-01         US-01           US-01          US-02
                              US-04                          US-03
```

Simpan sebagai `docs/story-map.md`.

### Tantangan 2: Estimation Poker Simulation (Intermediate)

Simulasikan **Planning Poker** untuk 5 user stories baru yang belum diestimasi. Untuk setiap story:
1. Setiap anggota tim (simulasikan 3 orang) memberikan estimasi secara independen
2. Jika estimasi berbeda, diskusikan alasan
3. Lakukan voting ulang hingga konsensus

Dokumentasikan proses dan hasil di `docs/estimation-poker.md`.

### Tantangan 3: Product Backlog Refinement (Advanced)

Lakukan **backlog refinement** dengan:
1. Pecah US-05 (Peminjaman Online, 8 SP) menjadi 3 sub-stories yang lebih kecil
2. Pecah US-13 (Login, 8 SP) menjadi 3 sub-stories
3. Tambahkan **technical stories** yang diperlukan (setup database, setup auth framework)
4. Re-estimasi dan update sprint planning

Buat issues baru di GitHub untuk sub-stories dan technical stories.

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

- [ ] Branch `feature/user-stories` dibuat dari `develop`
- [ ] File `docs/user-stories.md` berisi 15 user stories dalam format INVEST
- [ ] Setiap user story memiliki role, action, benefit, priority, dan story points
- [ ] File `docs/acceptance-criteria.md` berisi Given-When-Then untuk minimal 5 top stories
- [ ] MoSCoW prioritization diterapkan (must/should/could/wont-have)
- [ ] Story points menggunakan Fibonacci (1, 2, 3, 5, 8, 13)
- [ ] 15 GitHub Issues dibuat dengan labels yang sesuai
- [ ] GitHub Labels dikonfigurasi (MoSCoW, sprint, epic, story points)
- [ ] GitHub Projects board aktif dengan kolom Backlog/To Do/In Progress/In Review/Done
- [ ] Sprint 0 backlog didefinisikan di `docs/sprint-planning.md`
- [ ] Definition of Done didokumentasikan
- [ ] Pull Request dibuat dan di-merge ke `develop`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
