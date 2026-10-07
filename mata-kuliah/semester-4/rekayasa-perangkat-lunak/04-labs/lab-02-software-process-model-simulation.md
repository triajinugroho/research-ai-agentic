# Lab 02: Software Process Model Simulation

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 2 dari 13 |
| **Topik** | Simulasi Scrum Sprint, Sprint Planning, Daily Standup, Sprint Review |
| **CPMK** | CPMK-1 (Menjelaskan model proses pengembangan, framework Scrum, Agile Manifesto) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces, GitHub Projects |
| **Prasyarat** | Lab 01 selesai (repository dan Codespace aktif) |

---

## Tujuan

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. **Menjelaskan** (C2) peran, event, dan artifact dalam framework Scrum
2. **Mensimulasikan** (C3) satu siklus sprint lengkap (planning, standup, review, retrospective)
3. **Membuat** (C6) Product Backlog menggunakan GitHub Issues dan GitHub Projects sebagai Scrum board
4. **Membedakan** (C2) aktivitas di setiap Scrum event dan peran setiap Scrum role

---

## Konsep Singkat

### Framework Scrum

Scrum adalah framework Agile paling populer di industri software Indonesia (digunakan oleh Gojek, Tokopedia, Traveloka). Scrum membagi pengembangan menjadi iterasi pendek yang disebut **Sprint** (biasanya 1-4 minggu).

```
Scrum Framework Overview:

  Product    Sprint      Sprint       Daily        Sprint     Sprint
  Backlog    Planning    Backlog      Standup      Review     Retro
    │           │           │           │            │          │
    ▼           ▼           ▼           ▼            ▼          ▼
 ┌──────┐  ┌──────┐   ┌──────┐   ┌──────┐    ┌──────┐   ┌──────┐
 │Semua │  │Tim   │   │Items │   │15min │    │Demo  │   │Apa   │
 │fitur │──│pilih │──▶│yang  │──▶│3 per-│──▶ │hasil │──▶│yang  │
 │yang  │  │items │   │diker-│   │tanya-│    │kerja │   │perlu │
 │ingin │  │sprint│   │jakan │   │an    │    │ke PO │   │diubah│
 │dibuat│  │ini   │   │      │   │      │    │      │   │      │
 └──────┘  └──────┘   └──────┘   └──────┘    └──────┘   └──────┘
                                                              │
                Feedback loop ke Sprint berikutnya ◀──────────┘
```

### Tiga Pilar Scrum

| Pilar | Deskripsi | Contoh Implementasi |
|-------|-----------|-------------------|
| **Transparency** | Semua aspek proses terlihat oleh semua stakeholder | Scrum board yang selalu up-to-date |
| **Inspection** | Tim secara rutin memeriksa progress dan artefak | Daily standup, Sprint review |
| **Adaptation** | Tim menyesuaikan proses berdasarkan temuan inspeksi | Sprint retrospective menghasilkan action items |

### Tiga Peran Scrum

| Peran | Tanggung Jawab | Analogi |
|-------|----------------|---------|
| **Product Owner (PO)** | Menentukan APA yang dibangun, memprioritaskan backlog | "Klien" yang tahu kebutuhan pengguna |
| **Scrum Master (SM)** | Memastikan proses Scrum berjalan, menghilangkan hambatan | "Pelatih" yang memfasilitasi tim |
| **Development Team** | Mengerjakan item backlog, menentukan BAGAIMANA membangun | "Pemain" yang mengeksekusi |

### Empat Event Scrum

1. **Sprint Planning** -- Tim memilih item dari Product Backlog untuk dikerjakan di sprint ini
2. **Daily Standup** -- Meeting 15 menit setiap hari: apa yang dikerjakan, apa yang akan dikerjakan, ada hambatan?
3. **Sprint Review** -- Demo hasil kerja ke Product Owner dan stakeholder
4. **Sprint Retrospective** -- Refleksi tim: apa yang baik, apa yang perlu diperbaiki

> **Referensi:** Materi lengkap tersedia di modul Minggu 2 (`week-02`) dan Bab 2 Buku Ajar.

---

## Persiapan

| Kebutuhan | Detail |
|-----------|--------|
| Repository | Repository GitHub dari Lab 01 |
| Tim | Kelompok 3-4 orang (sama dengan tim proyek akhir) |
| GitHub Projects | Akses melalui tab "Projects" di repository |
| Peran | Setiap anggota harus punya peran Scrum (PO, SM, Dev) |

**Pembagian peran sebelum lab dimulai:**

| Peran | Jumlah | Tugas di Lab Ini |
|-------|--------|-----------------|
| Product Owner | 1 orang | Memprioritaskan backlog, menerima/menolak item saat review |
| Scrum Master | 1 orang | Memfasilitasi semua event, menjaga timeboxing |
| Developer | 1-2 orang | Memilih dan "mengerjakan" item saat sprint |

---

## Langkah-langkah

### Langkah 1: Pembentukan Tim dan Pembagian Peran (10 menit)

**Mengapa:** Scrum menekankan self-organizing team dengan peran yang jelas. Memahami setiap peran secara langsung lebih efektif daripada hanya membaca teorinya.

**Instruksi:**

1. Bentuk tim 3-4 orang
2. Tentukan siapa yang menjadi PO, SM, dan Developer
3. Buat file `docs/scrum-roles.md` di repository:

```markdown
# Scrum Roles - Tim [Nama Tim]

| Nama | NIM | Peran Scrum | Tanggung Jawab |
|------|-----|-------------|----------------|
| [Nama 1] | [NIM] | Product Owner | Prioritas backlog, acceptance |
| [Nama 2] | [NIM] | Scrum Master | Fasilitator, hapus hambatan |
| [Nama 3] | [NIM] | Developer | Implementasi fitur |
| [Nama 4] | [NIM] | Developer | Implementasi fitur |
```

4. Commit file:

```bash
git add docs/scrum-roles.md
git commit -m "docs: tambah pembagian peran Scrum tim"
git push origin main
```

**Expected Output:** File `docs/scrum-roles.md` tersimpan di repository dengan pembagian peran yang jelas.

> **Diskusi kelas:** Mengapa Product Owner tidak boleh merangkap sebagai Scrum Master? Apa risiko jika satu orang memegang kedua peran?

---

### Langkah 2: Buat Product Backlog dengan GitHub Issues (20 menit)

**Mengapa:** Product Backlog adalah daftar terurut semua fitur yang diinginkan dalam produk. Menggunakan GitHub Issues sebagai backlog item memberikan traceability -- setiap fitur bisa dilacak dari ide hingga implementasi.

**Instruksi:**

Product Owner memimpin pembuatan 10 GitHub Issues untuk proyek Sistem Perpustakaan Digital UAI:

| No | Judul Issue | Label Priority | Label Type | Deskripsi Singkat |
|----|------------|---------------|------------|-------------------|
| 1 | `feat: halaman login mahasiswa` | `must-have` | `feature` | Login dengan NIM dan password |
| 2 | `feat: halaman registrasi` | `must-have` | `feature` | Daftar akun baru dengan validasi |
| 3 | `feat: katalog pencarian buku` | `must-have` | `feature` | Cari buku berdasarkan judul/penulis |
| 4 | `feat: detail informasi buku` | `must-have` | `feature` | Tampilkan info lengkap buku |
| 5 | `feat: peminjaman buku online` | `must-have` | `feature` | Proses pinjam buku via sistem |
| 6 | `feat: daftar peminjaman saya` | `should-have` | `feature` | Riwayat peminjaman user |
| 7 | `feat: notifikasi deadline pengembalian` | `should-have` | `feature` | Reminder H-1 deadline |
| 8 | `feat: dashboard pustakawan` | `should-have` | `feature` | Panel admin untuk pustakawan |
| 9 | `feat: filter buku per kategori` | `could-have` | `feature` | Filter berdasarkan genre/kategori |
| 10 | `feat: dark mode` | `could-have` | `feature` | Tampilan gelap untuk UI |

Untuk setiap issue, PO menambahkan:
- **Deskripsi** yang jelas (minimal 2-3 kalimat)
- **Labels**: priority (`must-have` / `should-have` / `could-have`) dan type (`feature` / `bug` / `chore`)
- **Acceptance Criteria** (minimal 2 poin per issue)

Contoh deskripsi untuk Issue #1:

```markdown
## Deskripsi
Sebagai mahasiswa, saya ingin login ke sistem perpustakaan menggunakan NIM dan password
agar saya bisa mengakses fitur peminjaman buku.

## Acceptance Criteria
- [ ] Form login menerima NIM (format: 8 digit angka) dan password
- [ ] Jika NIM/password salah, tampilkan pesan error yang jelas
- [ ] Jika berhasil, redirect ke halaman dashboard
- [ ] Session tersimpan selama 24 jam

## Prioritas
Must Have - Sistem tidak bisa digunakan tanpa fitur login
```

**Expected Output:** 10 GitHub Issues dengan label dan deskripsi lengkap.

**Estimasi waktu:** 20 menit

> **Troubleshooting:** Untuk membuat label custom di GitHub, pergi ke Issues tab, klik "Labels", lalu "New label". Buat label `must-have` (merah), `should-have` (kuning), `could-have` (hijau).

---

### Langkah 3: Setup Scrum Board di GitHub Projects (10 menit)

**Mengapa:** Scrum Board memberikan visualisasi real-time tentang status pekerjaan tim. Transparansi ini adalah pilar pertama Scrum -- semua orang bisa melihat progress kapan saja.

**Instruksi:**

1. Di repository, klik tab **"Projects"** lalu **"New project"**
2. Pilih template **"Board"**
3. Beri nama: "Sprint Board - [Nama Tim]"
4. Buat 5 kolom:

```
┌─────────┐  ┌──────────────┐  ┌─────────────┐  ┌──────────┐  ┌──────┐
│ Product  │  │ Sprint       │  │ In Progress  │  │ In Review│  │ Done │
│ Backlog  │  │ Backlog      │  │              │  │          │  │      │
│          │  │              │  │              │  │          │  │      │
│ (Semua   │  │ (Dipilih     │  │ (Sedang      │  │ (Review/ │  │(Sele-│
│  item)   │  │  sprint ini) │  │  dikerjakan) │  │  testing)│  │ sai) │
└─────────┘  └──────────────┘  └─────────────┘  └──────────┘  └──────┘
```

5. Tambahkan semua 10 issues ke kolom **Product Backlog**

**Expected Output:** Board terlihat dengan 10 item di kolom Product Backlog, 4 kolom lainnya kosong.

---

### Langkah 4: Sprint Planning (15 menit)

**Mengapa:** Sprint Planning adalah event di mana tim memutuskan APA yang akan dikerjakan di sprint ini dan BAGAIMANA caranya. Ini melatih kemampuan estimasi dan negosiasi yang krusial di industri.

**Instruksi:**

Scrum Master memfasilitasi Sprint Planning:

1. **Tentukan Sprint Goal** (PO memimpin):
   - Sprint Goal: "Pengguna bisa login dan mencari buku di katalog"
   - Durasi Sprint: 2 minggu (simulasi: 15 menit lab ini)

2. **Pilih Sprint Backlog** (Tim berdiskusi):
   - PO mempresentasikan item berurutan dari atas backlog
   - Tim mendiskusikan apakah item bisa selesai dalam sprint
   - Pindahkan 4-5 item `must-have` ke kolom **Sprint Backlog**

3. **Estimasi Story Points** (Tim melakukan Planning Poker):
   - Gunakan skala Fibonacci: 1, 2, 3, 5, 8, 13
   - Setiap anggota menunjukkan estimasi secara bersamaan (bisa pakai jari tangan)
   - Jika perbedaan > 3, diskusi dan voting ulang

```
Planning Poker - Contoh:

Item: "feat: halaman login mahasiswa"

  Developer A: 3  ┐
  Developer B: 5  ├── Perbedaan > 2, diskusi!
  Developer C: 3  ┘

  Diskusi: "B berpikir validasi NIM rumit, A dan C tidak"
  Setelah diskusi: Semua setuju = 3 points
```

4. **Catat hasil** di file `docs/sprint-planning.md`:

```markdown
# Sprint 1 Planning

**Sprint Goal:** Pengguna bisa login dan mencari buku di katalog
**Durasi:** 2 minggu
**Total Story Points:** [N] points

## Sprint Backlog

| # | Item | Assignee | Story Points | Priority |
|---|------|----------|-------------|----------|
| 1 | Halaman login mahasiswa | [Nama] | 3 | Must |
| 2 | Halaman registrasi | [Nama] | 3 | Must |
| 3 | Katalog pencarian buku | [Nama] | 5 | Must |
| 4 | Detail informasi buku | [Nama] | 2 | Must |

**Capacity:** [N] total points tersedia
**Commitment:** [N] points dipilih
```

5. Commit:

```bash
git add docs/sprint-planning.md
git commit -m "docs: catat hasil sprint 1 planning"
git push origin main
```

**Expected Output:** 4-5 item berpindah dari Product Backlog ke Sprint Backlog di board, file planning tersimpan.

**Estimasi waktu:** 15 menit

> **Tips SM:** Jaga agar diskusi tetap fokus. Jika estimasi makan waktu terlalu lama, PO bisa memutuskan untuk memecah item menjadi lebih kecil.

---

### Langkah 5: Simulasi Daily Standup (15 menit)

**Mengapa:** Daily Standup adalah ritual Scrum yang menjaga transparansi dan mendeteksi hambatan lebih awal. Di industri, meeting ini berlangsung 15 menit setiap hari. Di lab ini, kita simulasikan 2 hari dalam 15 menit.

**Instruksi:**

**Simulasi Hari 1:** SM memfasilitasi standup. Setiap anggota menjawab 3 pertanyaan (masing-masing 1-2 menit):

```
┌─────────────────────────────────────────────────────┐
│  DAILY STANDUP - Hari 1                             │
├─────────────────────────────────────────────────────┤
│  [Nama]:                                            │
│  1. Kemarin saya mengerjakan: ________________      │
│  2. Hari ini saya akan mengerjakan: __________      │
│  3. Hambatan: ________________________________      │
├─────────────────────────────────────────────────────┤
│  Scrum Master Notes:                                │
│  - Hambatan yang perlu ditindaklanjuti: _______     │
│  - Action item: ______________________________      │
└─────────────────────────────────────────────────────┘
```

Setelah standup Hari 1:
- Pindahkan 2 item dari Sprint Backlog ke **In Progress**
- Assign developer yang mengerjakan

**Simulasi Hari 2:** Ulangi standup. Kali ini:
- Pindahkan 1 item dari In Progress ke **In Review**
- Pindahkan 1 item baru ke In Progress
- Simulasikan: ada hambatan -- developer tidak mengerti spesifikasi detail buku. PO harus klarifikasi.

Catat semua standup di file `docs/daily-standup.md`:

```markdown
# Daily Standup Log - Sprint 1

## Hari 1 - [Tanggal]

| Anggota | Kemarin | Hari Ini | Hambatan |
|---------|---------|----------|----------|
| [Nama 1] | Setup project | Mulai login page | Tidak ada |
| [Nama 2] | Baca spesifikasi | Design database | Belum jelas format NIM |
| [Nama 3] | Install dependencies | Mulai search API | Tidak ada |

**Action Items:**
- PO klarifikasi format NIM ke stakeholder

## Hari 2 - [Tanggal]
| Anggota | Kemarin | Hari Ini | Hambatan |
|---------|---------|----------|----------|
| ... | ... | ... | ... |
```

**Expected Output:** Board menunjukkan item tersebar di beberapa kolom, file standup tercatat.

**Estimasi waktu:** 15 menit

> **Diskusi kelas:** Apa yang terjadi jika satu anggota tim selalu melaporkan "Tidak ada hambatan" padahal progress-nya lambat? Bagaimana SM sebaiknya menangani situasi ini?

---

### Langkah 6: Sprint Review (15 menit)

**Mengapa:** Sprint Review adalah kesempatan tim mendemonstrasikan hasil kerja ke Product Owner. PO memutuskan apakah item memenuhi Definition of Done dan acceptance criteria. Ini melatih kemampuan presentasi dan menerima feedback.

**Instruksi:**

1. Pindahkan 2-3 item ke kolom **Done** (simulasi: item sudah selesai)
2. Tim mempresentasikan setiap item Done ke PO (1-2 menit per item):

```
Sprint Review Script:

Developer: "Untuk item 'Halaman Login', saya sudah mengimplementasikan:
  - Form login dengan field NIM dan password
  - Validasi format NIM 8 digit
  - Error message jika login gagal
  Berikut demo-nya..."

PO: "Saya lihat acceptance criteria sudah terpenuhi.
  Tapi saya ingin tambahkan: bagaimana jika user lupa password?
  → Tambahkan item baru di backlog: 'feat: forgot password'"
```

3. PO memutuskan:
   - **Accept** -- item memenuhi acceptance criteria → tetap di Done
   - **Reject** -- item belum memenuhi → pindahkan kembali ke Sprint Backlog

4. Catat hasil review di `docs/sprint-review.md`:

```markdown
# Sprint 1 Review

**Sprint Goal:** Pengguna bisa login dan mencari buku
**Goal Tercapai:** Ya / Sebagian / Tidak

## Items Reviewed

| Item | Status | Catatan PO |
|------|--------|-----------|
| Halaman login | Accepted | Tambah fitur forgot password di backlog |
| Halaman registrasi | Accepted | - |
| Katalog pencarian | Rejected | Pencarian belum bisa filter kategori |

## Velocity
- Committed: [N] story points
- Completed: [M] story points
- Velocity Sprint 1: [M] points

## Feedback Stakeholder
- [Catat feedback yang diterima]

## New Backlog Items
- feat: forgot password (dari feedback PO)
```

**Expected Output:** Sprint review tercatat, velocity dihitung, item baru ditambahkan ke backlog.

---

### Langkah 7: Sprint Retrospective (15 menit)

**Mengapa:** Retrospective adalah jantung continuous improvement di Scrum. Tim merefleksikan proses (bukan produk) dan membuat komitmen perbaikan konkret untuk sprint berikutnya. Di sinilah nilai **kaizen** (perbaikan berkelanjutan) dipraktikkan.

**Instruksi:**

SM memfasilitasi retrospective menggunakan format **Start-Stop-Continue**:

```
┌─────────────────────────────────────────────────────────────────┐
│                    SPRINT RETROSPECTIVE                         │
├─────────────────┬───────────────────┬───────────────────────────┤
│  START          │  STOP             │  CONTINUE                 │
│  (Mulai lakukan)│  (Berhenti lakukan)│  (Terus lakukan)         │
├─────────────────┼───────────────────┼───────────────────────────┤
│ - Pair          │ - Skip standup    │ - Code review sebelum     │
│   programming   │ - Commit langsung │   merge                   │
│ - Daily update  │   ke main tanpa   │ - Conventional commits    │
│   di grup chat  │   branch          │ - Diskusi estimasi        │
│ - Tulis test    │ - Push tanpa test │   bersama                 │
│   lebih awal    │                   │                           │
└─────────────────┴───────────────────┴───────────────────────────┘
```

1. Setiap anggota menulis di sticky note (atau kertas):
   - 1-2 hal yang ingin **mulai dilakukan** (Start)
   - 1-2 hal yang ingin **berhenti dilakukan** (Stop)
   - 1-2 hal yang ingin **terus dilakukan** (Continue)

2. Diskusikan bersama dan pilih **2-3 action items** yang paling penting

3. Catat di `docs/sprint-retrospective.md`:

```markdown
# Sprint 1 Retrospective

## Start
- [ ] Pair programming untuk item yang kompleks
- [ ] Daily update di grup WhatsApp tim

## Stop
- [ ] Commit langsung ke main tanpa branch
- [ ] Skip daily standup

## Continue
- [x] Code review sebelum merge
- [x] Conventional commits

## Action Items untuk Sprint 2
1. **Action:** Mulai pair programming → **PIC:** [Nama] → **Deadline:** Sprint 2 Day 1
2. **Action:** Buat branch protection rule → **PIC:** SM → **Deadline:** Hari ini
```

4. Commit semua dokumentasi:

```bash
git add docs/
git commit -m "docs: tambah catatan sprint review dan retrospective"
git push origin main
```

**Expected Output:** Retrospective tercatat dengan action items konkret yang bisa ditindaklanjuti.

**Estimasi waktu:** 15 menit

> **Refleksi Islami:** Retrospective sejalan dengan konsep **muhasabah** (introspeksi diri) dalam Islam -- secara rutin mengevaluasi diri untuk menjadi lebih baik. Rasulullah SAW mengajarkan agar kita menjadi lebih baik dari hari kemarin.

---

## Tantangan Tambahan

### Tantangan 1: Dasar
Tambahkan **story points** (label Fibonacci: `1-point`, `2-points`, `3-points`, `5-points`, `8-points`) ke setiap issue. Buat milestone "Sprint 1" dan assign semua item Sprint Backlog ke milestone tersebut.

### Tantangan 2: Menengah
Hitung **velocity** Sprint 1 (total story points yang Done). Gunakan velocity tersebut untuk merencanakan Sprint 2: berapa banyak item yang bisa diambil? Buat prediksi kapan seluruh backlog selesai berdasarkan velocity.

### Tantangan 3: Lanjutan
Bandingkan simulasi Scrum yang baru dilakukan dengan model **Waterfall**. Buat dokumen `docs/scrum-vs-waterfall.md` yang menganalisis: (a) Bagaimana jika proyek perpustakaan ini dikerjakan dengan Waterfall? (b) Apa kelebihan dan kekurangan masing-masing model untuk proyek ini? (c) Dalam situasi apa Waterfall lebih tepat daripada Scrum?

---

## Refleksi & AI Usage Log

Sebelum meninggalkan lab, isi refleksi berikut di file `docs/refleksi-lab-02.md`:

1. **Apa perbedaan pengalaman menjadi PO vs SM vs Developer?**
2. **Event Scrum mana yang paling terasa manfaatnya? Mengapa?**
3. **Apa tantangan terbesar dalam estimasi story points?**

Jika menggunakan AI selama lab, catat di **AI Usage Log**:

| Prompt yang Diberikan | Output AI | Modifikasi yang Dilakukan | Refleksi |
|----------------------|-----------|--------------------------|----------|
| (contoh prompt) | (ringkasan output) | (apa yang diubah) | (apa yang dipelajari) |

---

## Checklist Penyelesaian

- [ ] Tim terbentuk dengan peran Scrum yang jelas (PO, SM, Dev)
- [ ] 10 GitHub Issues dibuat dengan label priority, type, dan deskripsi lengkap
- [ ] GitHub Projects board aktif dengan 5 kolom
- [ ] Sprint Planning tercatat: Sprint Goal, Sprint Backlog, story points
- [ ] Daily Standup (2 hari simulasi) tercatat dengan 3 pertanyaan per anggota
- [ ] Sprint Review tercatat: items reviewed, accepted/rejected, velocity
- [ ] Sprint Retrospective tercatat: Start-Stop-Continue dan action items
- [ ] Semua dokumen di-commit ke repository (`docs/scrum-roles.md`, `docs/sprint-planning.md`, `docs/daily-standup.md`, `docs/sprint-review.md`, `docs/sprint-retrospective.md`)
- [ ] File refleksi `docs/refleksi-lab-02.md` terisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
