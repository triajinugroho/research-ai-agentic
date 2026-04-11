# Panduan Proyek Akhir — Praktikum Rekayasa Perangkat Lunak (IF2206)

| Informasi | Detail |
|-----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Bobot** | 35% dari nilai akhir |
| **Tim** | 3-4 mahasiswa (sama dengan IF2205) |
| **Timeline** | Sprint 0-4 + Demo (Minggu 5-15) |
| **Tech Stack** | Python Flask + HTML/CSS/JS + SQLite/PostgreSQL |
| **Platform** | GitHub Codespaces |
| **Metode** | Scrum (sprints, daily standup, review, retrospective) |

---

## A. Pilihan Topik Proyek

Tim memilih **satu** dari lima topik berikut (sama dengan proyek IF2205):

### Opsi 1: Sistem Informasi Perpustakaan Digital

**Deskripsi:** Sistem manajemen perpustakaan untuk mengelola koleksi buku, peminjaman, pengembalian, dan anggota. Mendukung pencarian buku, notifikasi keterlambatan, dan laporan statistik.

**Fitur utama:** Katalog buku, manajemen anggota, peminjaman/pengembalian, pencarian & filter, laporan.

### Opsi 2: Sistem Manajemen UMKM

**Deskripsi:** Aplikasi untuk mengelola usaha mikro, kecil, dan menengah — mencakup manajemen produk, pencatatan transaksi penjualan, laporan keuangan sederhana, dan manajemen pelanggan.

**Fitur utama:** Manajemen produk, pencatatan penjualan, laporan keuangan, manajemen pelanggan, dashboard.

### Opsi 3: Sistem Informasi Puskesmas

**Deskripsi:** Sistem untuk mengelola data pasien, pendaftaran antrian, rekam medis sederhana, jadwal dokter, dan laporan kunjungan di puskesmas.

**Fitur utama:** Pendaftaran pasien, antrian, rekam medis, jadwal dokter, laporan kunjungan.

### Opsi 4: Platform E-Commerce Sederhana

**Deskripsi:** Platform jual-beli online sederhana dengan manajemen produk, keranjang belanja, proses checkout, dan tracking pesanan. Tidak perlu integrasi payment gateway nyata.

**Fitur utama:** Katalog produk, keranjang belanja, checkout, tracking pesanan, manajemen toko.

### Opsi 5: Sistem Pengelolaan Zakat

**Deskripsi:** Sistem untuk mengelola pengumpulan dan distribusi zakat — mencakup data muzakki (pembayar), mustahik (penerima), pencatatan pembayaran, dan laporan distribusi.

**Fitur utama:** Data muzakki & mustahik, pencatatan zakat, distribusi, laporan, dashboard.

**Catatan:** Proyek yang sama digunakan untuk **IF2205 (Teori)** dan **IF2206 (Praktikum)**. IF2205 menilai proses rekayasa (requirements, desain, manajemen), sedangkan IF2206 menilai implementasi teknis (kode, testing, deployment).

---

## B. Timeline Sprint

| Sprint | Minggu | Fokus Praktikum | Lab Terkait |
|--------|--------|-----------------|-------------|
| Sprint 0 | 5-6 | Frontend + Backend | Lab 05, Lab 06 |
| Sprint 1 | 7 + 9 | Database + Unit Testing | Lab 07, Lab 09 |
| Sprint 2 | 10-11 | Integration Testing + CI/CD | Lab 10, Lab 11 |
| Sprint 3 | 12-13 | Docker + AI Pair Programming | Lab 12, Lab 13 |
| Sprint 4 | 14 | Sprint Review & Retrospective | Lab 14 |
| Demo | 15 | Presentasi & Demo Proyek Akhir | — |

**Catatan:** Minggu 8 = Responsi Tengah Semester (RTS) — tidak ada aktivitas sprint.

---

## C. Deliverables Detail per Sprint

### Sprint 0: Frontend + Backend (Minggu 5-6)

**Tujuan:** Membangun prototype awal dengan frontend dan backend yang terhubung.

**Deliverables:**

- [ ] **Frontend (HTML/CSS/JS):**
  - [ ] Halaman login/register dengan form validation
  - [ ] Halaman dashboard utama dengan navigation
  - [ ] Minimal 2 halaman CRUD (list + detail/form)
  - [ ] Responsive layout (mobile-friendly)
  - [ ] Jinja2 template inheritance (`base.html` + child templates)
- [ ] **Backend (Flask API):**
  - [ ] Flask project structure menggunakan factory pattern atau modular
  - [ ] Minimal 5 REST API endpoints (CRUD untuk 1 resource utama)
  - [ ] Route untuk serve frontend templates
  - [ ] Error handling (404, 400, 500)
  - [ ] Flask-CORS terkonfigurasi (jika frontend terpisah)
- [ ] **Git & Project Management:**
  - [ ] Repository GitHub dibuat dengan branch protection
  - [ ] `.gitignore` untuk Python/Flask
  - [ ] `README.md` awal dengan deskripsi proyek dan anggota tim
  - [ ] GitHub Issues untuk backlog items
  - [ ] Sprint 0 board di GitHub Projects
- [ ] **Scrum Artifacts:**
  - [ ] Product Backlog (minimal 15 user stories)
  - [ ] Sprint 0 Backlog (5-8 items)
  - [ ] Sprint 0 Planning meeting notes

**Definition of Done Sprint 0:**
Aplikasi dapat dijalankan (`flask run`), halaman login muncul, dan minimal 1 operasi CRUD berfungsi end-to-end (frontend -> backend -> response).

---

### Sprint 1: Database + Unit Testing (Minggu 7 + 9)

**Tujuan:** Mengintegrasikan database dan menulis unit test dasar.

**Deliverables:**

- [ ] **Database (SQLAlchemy ORM):**
  - [ ] Minimal 3 SQLAlchemy models dengan relationships (1:N minimal)
  - [ ] Flask-Migrate terintegrasi dengan migration files
  - [ ] Seed data script (`seed.py` atau Flask CLI command)
  - [ ] Semua CRUD endpoints menggunakan database (bukan in-memory)
  - [ ] Model validations (required fields, unique constraints)
- [ ] **Unit Testing (pytest):**
  - [ ] File `conftest.py` dengan test fixtures (test client, test database)
  - [ ] Unit tests untuk setiap model (create, read, update, delete)
  - [ ] Unit tests untuk utility functions
  - [ ] Minimal 10 test cases
  - [ ] Coverage report >= 50%
- [ ] **Git & Code Quality:**
  - [ ] Feature branches untuk setiap fitur
  - [ ] Pull requests dengan code review oleh rekan tim
  - [ ] Conventional commit messages
- [ ] **Scrum Artifacts:**
  - [ ] Sprint 1 Backlog
  - [ ] Sprint 1 Planning meeting notes
  - [ ] Sprint 0 Review & Retrospective notes

**Definition of Done Sprint 1:**
Semua data disimpan di database (bukan hardcoded). Minimal 10 unit tests berjalan hijau. Migration files tersedia dan bisa dijalankan dari scratch.

---

### Sprint 2: Integration Testing + CI/CD (Minggu 10-11)

**Tujuan:** Memperluas test coverage dan membangun CI/CD pipeline.

**Deliverables:**

- [ ] **Integration Testing:**
  - [ ] Integration tests untuk API endpoints (test full request-response cycle)
  - [ ] Test database isolation (setiap test menggunakan database bersih)
  - [ ] End-to-end scenario tests (contoh: register -> login -> create item -> view item)
  - [ ] Edge case tests (invalid input, unauthorized access, not found)
  - [ ] Total test cases >= 20
  - [ ] Coverage >= 70%
- [ ] **CI/CD (GitHub Actions):**
  - [ ] `.github/workflows/ci.yml` dengan pipeline:
    - [ ] Step 1: Install dependencies
    - [ ] Step 2: Run linter (flake8 atau pylint)
    - [ ] Step 3: Run tests (`pytest`)
    - [ ] Step 4: Generate coverage report
  - [ ] Status badge di `README.md`
  - [ ] Pipeline berjalan otomatis pada setiap push dan PR
- [ ] **Code Quality:**
  - [ ] Kode lolos linter tanpa error (warning boleh)
  - [ ] Separation of concerns (models, routes, services terpisah)
  - [ ] Environment variables menggunakan `.env` (tidak hardcoded)
- [ ] **Scrum Artifacts:**
  - [ ] Sprint 2 Backlog
  - [ ] Sprint 2 Planning meeting notes
  - [ ] Sprint 1 Review & Retrospective notes

**Definition of Done Sprint 2:**
CI pipeline hijau (all checks pass) pada branch `main`. Coverage >= 70%. Linter berjalan tanpa error.

---

### Sprint 3: Docker + AI Pair Programming (Minggu 12-13)

**Tujuan:** Containerize aplikasi dan memanfaatkan AI untuk improvement.

**Deliverables:**

- [ ] **Docker:**
  - [ ] `Dockerfile` yang bisa di-build tanpa error
  - [ ] `.dockerignore` file
  - [ ] `docker-compose.yml` dengan minimal app service
  - [ ] Aplikasi berjalan di Docker container
  - [ ] Environment variables via `.env` file
- [ ] **Deployment:**
  - [ ] Deploy ke cloud platform (Railway, Render, atau sejenis)
  - [ ] Aplikasi bisa diakses via URL publik
  - [ ] Environment variables dikonfigurasi di platform
  - [ ] Database di production (SQLite atau PostgreSQL)
- [ ] **AI Pair Programming:**
  - [ ] Gunakan AI untuk code review (minimal 3 files di-review AI)
  - [ ] Gunakan AI untuk generate additional test cases
  - [ ] Gunakan AI untuk improve code quality (refactoring suggestions)
  - [ ] AI Usage Log lengkap untuk sprint ini
- [ ] **Scrum Artifacts:**
  - [ ] Sprint 3 Backlog
  - [ ] Sprint 3 Planning meeting notes
  - [ ] Sprint 2 Review & Retrospective notes
  - [ ] AI Usage Log Sprint 3

**Definition of Done Sprint 3:**
Aplikasi berjalan di Docker (`docker-compose up`). Aplikasi live di URL publik. AI Usage Log menunjukkan penggunaan AI yang meaningful.

---

### Sprint 4: Sprint Review & Retrospective (Minggu 14)

**Tujuan:** Finalisasi proyek, dokumentasi lengkap, dan refleksi tim.

**Deliverables:**

- [ ] **Dokumentasi Final:**
  - [ ] `README.md` lengkap (deskripsi, tech stack, cara install, cara run, screenshot, API docs, URL deployment)
  - [ ] API documentation (daftar endpoints, request/response format)
  - [ ] Arsitektur diagram (ASCII atau gambar)
  - [ ] Database schema / ERD
- [ ] **Kualitas Kode:**
  - [ ] Semua tests passing (coverage >= 80%)
  - [ ] CI pipeline hijau
  - [ ] Kode bersih, tidak ada dead code atau debug prints
  - [ ] `.env.example` tersedia
- [ ] **Scrum Artifacts Final:**
  - [ ] Sprint 4 Planning & Review notes
  - [ ] Sprint 3-4 Retrospective (Start-Stop-Continue format)
  - [ ] Peer review form (setiap anggota menilai rekan tim)
  - [ ] Individual contribution summary
  - [ ] AI Usage Log kumulatif (semua sprint)
- [ ] **Persiapan Demo:**
  - [ ] Slide presentasi (5-7 slides)
  - [ ] Demo script (fitur apa yang akan ditunjukkan)
  - [ ] Setiap anggota tahu bagian presentasinya

**Definition of Done Sprint 4:**
README lengkap. Semua Scrum artifacts tersedia. Peer review selesai. Tim siap untuk demo.

---

## D. Struktur Repository GitHub

```
project-name/
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions CI pipeline
├── app/
│   ├── __init__.py                 # Flask app factory
│   ├── models.py                   # SQLAlchemy models
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py                 # Authentication routes
│   │   └── main.py                 # Main resource routes
│   ├── templates/
│   │   ├── base.html               # Base template (Jinja2)
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   └── ...
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
├── tests/
│   ├── conftest.py                 # Test fixtures
│   ├── test_models.py              # Unit tests for models
│   ├── test_routes.py              # Integration tests for API
│   └── test_auth.py                # Authentication tests
├── migrations/                     # Flask-Migrate migration files
│   └── versions/
├── docs/
│   ├── scrum/
│   │   ├── sprint-0-planning.md
│   │   ├── sprint-0-review.md
│   │   ├── sprint-1-planning.md
│   │   ├── sprint-1-review.md
│   │   ├── ...
│   │   └── retrospective-final.md
│   ├── ai-usage-log.md             # Cumulative AI Usage Log
│   ├── peer-review.md              # Peer review results
│   └── api-docs.md                 # API documentation
├── .dockerignore
├── .env.example                    # Environment variable template
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── seed.py                         # Database seed data
├── config.py                       # App configuration
└── README.md                       # Project documentation
```

**Ketentuan repository:**
- Branch protection pada `main` (require PR review sebelum merge)
- Setiap fitur dikembangkan di feature branch
- PR wajib di-review oleh minimal 1 anggota tim lain
- `.env` file **tidak boleh** di-commit (harus ada di `.gitignore`)

---

## E. Definition of Done — Ringkasan

| Sprint | Kriteria Utama |
|--------|---------------|
| Sprint 0 | Aplikasi berjalan, 1 CRUD end-to-end, product backlog ada |
| Sprint 1 | Database terintegrasi, 10+ tests hijau, migration berjalan |
| Sprint 2 | CI pipeline hijau, coverage >= 70%, linter bersih |
| Sprint 3 | Docker berjalan, aplikasi live di URL publik, AI log ada |
| Sprint 4 | README lengkap, semua artifacts ada, peer review selesai, siap demo |

---

## F. Demo Proyek Akhir (Minggu 15)

### F.1 Format Demo

| Aspek | Detail |
|-------|--------|
| **Durasi** | 10 menit per tim (5 menit demo + 5 menit Q&A) |
| **Peserta** | Seluruh anggota tim wajib hadir dan presentasi |
| **Evaluator** | Dosen pengampu + dosen penguji (jika ada) |
| **Aplikasi** | Harus berjalan **live** (URL publik), bukan localhost |

### F.2 Kriteria Evaluasi Demo

| Aspek | Bobot | Yang Dinilai |
|-------|-------|-------------|
| **Fungsionalitas Live** | 30% | Aplikasi berjalan tanpa crash, fitur CRUD berfungsi, data tersimpan |
| **Technical Depth** | 25% | Arsitektur jelas, testing ada, CI/CD berjalan, Docker digunakan |
| **Presentasi** | 20% | Slide jelas, demo terstruktur, setiap anggota berbicara |
| **Q&A Response** | 15% | Setiap anggota bisa menjawab pertanyaan teknis tentang bagiannya |
| **Scrum Evidence** | 10% | Sprint artifacts lengkap, kontribusi merata, retrospective bermakna |

### F.3 Hal yang Dicari Evaluator

**Positif (nilai tinggi):**
- Aplikasi stabil dan responsif
- Arsitektur kode bersih (separation of concerns)
- Test coverage tinggi (>= 80%) dengan tests bermakna
- CI/CD pipeline hijau dan otomatis
- Setiap anggota tim paham keseluruhan kode (bukan hanya bagiannya)
- AI digunakan secara bertanggung jawab dan terdokumentasi

**Negatif (mengurangi nilai):**
- Aplikasi crash saat demo
- Hanya 1-2 anggota yang bisa menjawab pertanyaan teknis
- Test coverage rendah atau tests hanya `assert True`
- Tidak ada CI/CD atau pipeline selalu merah
- Kontribusi tim sangat tidak merata (terlihat dari git log)
- AI Usage Log tidak ada padahal jelas menggunakan AI

---

## G. Rubrik Penilaian Proyek (7 Komponen)

### G.1 Teknis & Fungsionalitas (30%)

| Level | Skor | Kriteria |
|-------|------|----------|
| Excellent | 4 | Semua fitur CRUD berfungsi sempurna, validasi input lengkap, error handling komprehensif, UI responsif, performa baik |
| Good | 3 | Fitur CRUD utama berfungsi, validasi ada, error handling memadai, UI fungsional |
| Adequate | 2 | Sebagian fitur berfungsi, validasi minimal, beberapa error tidak ter-handle |
| Inadequate | 1 | Fitur utama tidak berfungsi, banyak bug, aplikasi sering crash |

### G.2 Arsitektur & Kualitas Kode (20%)

| Level | Skor | Kriteria |
|-------|------|----------|
| Excellent | 4 | Arsitektur bersih (MVC/factory pattern), separation of concerns, naming convention konsisten, kode DRY, modular |
| Good | 3 | Arsitektur jelas, sebagian besar kode terstruktur, ada beberapa duplikasi minor |
| Adequate | 2 | Kode berfungsi tapi tidak terstruktur dengan baik, banyak duplikasi, tidak modular |
| Inadequate | 1 | Semua kode dalam 1 file, tidak ada struktur, sulit dibaca dan di-maintain |

### G.3 Testing & Coverage (15%)

| Level | Skor | Kriteria |
|-------|------|----------|
| Excellent | 4 | Coverage >= 80%, unit + integration tests, edge cases, TDD evidence, semua tests hijau |
| Good | 3 | Coverage >= 70%, unit tests bermakna, beberapa integration tests |
| Adequate | 2 | Coverage >= 50%, tests ada tapi minimal, hanya happy path |
| Inadequate | 1 | Coverage < 50%, tests tidak berjalan, atau hanya tests trivial |

### G.4 CI/CD & Deployment (15%)

| Level | Skor | Kriteria |
|-------|------|----------|
| Excellent | 4 | CI pipeline multi-stage (lint + test + build), auto-deploy, status badge, Docker multi-stage, aplikasi live stabil |
| Good | 3 | CI pipeline berjalan (test + lint), Docker berfungsi, aplikasi di-deploy |
| Adequate | 2 | CI pipeline ada tapi sering gagal, Docker basic, deployment tidak stabil |
| Inadequate | 1 | Tidak ada CI/CD, tidak ada Docker, aplikasi tidak di-deploy |

### G.5 Presentasi & Dokumentasi (10%)

| Level | Skor | Kriteria |
|-------|------|----------|
| Excellent | 4 | README lengkap dan profesional, API docs detail, arsitektur diagram, demo lancar, semua anggota presentasi dengan percaya diri |
| Good | 3 | README baik, API docs ada, demo berjalan lancar |
| Adequate | 2 | README minimal, dokumentasi kurang, demo bermasalah minor |
| Inadequate | 1 | README hampir tidak ada, tidak ada API docs, demo gagal |

### G.6 Teamwork & Scrum Artifacts (5%)

| Level | Skor | Kriteria |
|-------|------|----------|
| Excellent | 4 | Scrum artifacts lengkap (planning, review, retrospective per sprint), kontribusi merata (git log), peer review constructive |
| Good | 3 | Scrum artifacts ada untuk sebagian besar sprint, kontribusi cukup merata |
| Adequate | 2 | Scrum artifacts minimal, kontribusi tidak merata tapi semua berkontribusi |
| Inadequate | 1 | Scrum artifacts tidak ada, 1-2 anggota tidak berkontribusi |

### G.7 AI Usage Log (5%)

| Level | Skor | Kriteria |
|-------|------|----------|
| Excellent | 4 | AI Usage Log lengkap per sprint, prompt & output terdokumentasi, modifikasi dicatat, menunjukkan penggunaan AI yang cerdas dan bertanggung jawab |
| Good | 3 | AI Usage Log ada untuk sebagian besar sprint, dokumentasi memadai |
| Adequate | 2 | AI Usage Log ada tapi tidak lengkap, hanya daftar tool tanpa detail |
| Inadequate | 1 | Tidak ada AI Usage Log padahal jelas menggunakan AI |

### Rumus Nilai Proyek

```
Nilai Proyek = (Teknis × 0.30) + (Arsitektur × 0.20) + (Testing × 0.15)
             + (CI/CD × 0.15) + (Presentasi × 0.10) + (Teamwork × 0.05)
             + (AI Log × 0.05)

Semua komponen dalam skala 1-4, lalu:
Nilai Final = (Nilai Proyek / 4) × 100
```

---

## H. Peer Review

### H.1 Form Peer Review

Setiap anggota tim mengisi peer review untuk **semua** rekan tim (anonim terhadap rekan, tapi dosen melihat siapa penilai).

```markdown
## Peer Review Form — Sprint 4

**Penilai:** [Nama / NIM]
**Proyek:** [Nama Proyek]

### Penilaian Rekan Tim

| Aspek | [Nama Rekan 1] | [Nama Rekan 2] | [Nama Rekan 3] |
|-------|----------------|----------------|----------------|
| Kontribusi teknis (1-5) | | | |
| Keaktifan komunikasi (1-5) | | | |
| Tanggung jawab (1-5) | | | |
| Kualitas kode (1-5) | | | |
| **Rata-rata** | | | |

### Komentar (wajib minimal 2 kalimat per rekan)

**[Nama Rekan 1]:** ...
**[Nama Rekan 2]:** ...
**[Nama Rekan 3]:** ...
```

### H.2 Penggunaan Hasil Peer Review

- Peer review digunakan sebagai **faktor penyesuaian** nilai proyek individual.
- Jika peer review konsisten menunjukkan kontribusi rendah, nilai individu bisa dikurangi hingga **20%** dari nilai proyek tim.
- Jika peer review konsisten menunjukkan kontribusi sangat tinggi, nilai individu bisa ditambah hingga **10%** dari nilai proyek tim.
- Peer review yang tidak diisi dianggap sebagai kontribusi rendah pada aspek Teamwork.

---

## I. Individual Contribution Tracking

### I.1 Git Log Analysis

Kontribusi individual dilacak melalui **Git log**:

```bash
# Jumlah commits per anggota
git shortlog -sn --all

# Lines of code per anggota
git log --author="Nama" --pretty=tformat: --numstat | awk '{add+=$1; del+=$2} END {print add, del}'

# Commits per minggu per anggota
git log --author="Nama" --format="%aI" | cut -d'T' -f1 | sort | uniq -c
```

**Catatan:** Jumlah commits dan lines bukan satu-satunya ukuran kontribusi. Kualitas kode, code review, dan Scrum facilitation juga dihitung.

### I.2 Ekspektasi Kontribusi

| Tim 3 orang | Tim 4 orang |
|-------------|-------------|
| Masing-masing ~33% kontribusi | Masing-masing ~25% kontribusi |
| Toleransi: 20-45% per orang | Toleransi: 15-35% per orang |
| Red flag: < 15% atau > 55% | Red flag: < 10% atau > 45% |

Jika ada anggota dengan kontribusi di bawah threshold, dosen akan meminta **penjelasan tertulis** dari tim.

---

## J. Sprint Retrospective Template

Gunakan format **Start-Stop-Continue** untuk setiap sprint retrospective:

```markdown
## Sprint [N] Retrospective

**Tanggal:** [DD Bulan YYYY]
**Peserta:** [Nama anggota tim]
**Facilitator:** [Nama]

### Start (Mulai lakukan)
- [ ] [Hal baru yang harus mulai dilakukan di sprint berikutnya]
- [ ] ...

### Stop (Berhenti lakukan)
- [ ] [Hal yang harus dihentikan karena tidak efektif]
- [ ] ...

### Continue (Terus lakukan)
- [ ] [Hal yang sudah baik dan harus dilanjutkan]
- [ ] ...

### Action Items
| Action | PIC | Deadline |
|--------|-----|----------|
| ... | ... | ... |

### Metrics
| Metrik | Sprint [N-1] | Sprint [N] | Trend |
|--------|-------------|------------|-------|
| Completed stories | | | |
| Test coverage | | | |
| Open bugs | | | |
| CI pass rate | | | |
```

---

## K. Team Agreement Template

Di awal proyek (Sprint 0), tim membuat kesepakatan kerja:

```markdown
## Team Agreement — [Nama Proyek]

**Tim:** [Nama anggota]
**Tanggal:** [DD Bulan YYYY]

### Communication
- Channel komunikasi utama: [WhatsApp/Discord/...]
- Response time: maksimal [N] jam
- Standup: [harian/3x seminggu] via [chat/video]

### Git Workflow
- Branching strategy: [Git Flow / Trunk-based / ...]
- Branch naming: feature/[nama-fitur], fix/[nama-fix]
- Commit message: conventional commits (feat:, fix:, docs:, ...)
- PR review: minimal 1 approval sebelum merge
- Main branch: protected, no direct push

### Coding Standards
- Python style: PEP 8
- Linter: flake8 / pylint
- Naming: snake_case untuk Python, camelCase untuk JavaScript
- Comments: Bahasa Indonesia untuk penjelasan, English untuk code comments

### Meeting Schedule
- Sprint Planning: [hari, jam]
- Sprint Review: [hari, jam]
- Retrospective: setelah Sprint Review

### Conflict Resolution
1. Diskusi langsung antar anggota terlibat
2. Eskalasi ke seluruh tim
3. Eskalasi ke dosen (jika tidak terselesaikan)

### AI Usage Agreement
- AI tools yang digunakan: [ChatGPT / Claude / Copilot / ...]
- AI Usage Log: diisi oleh setiap anggota di `docs/ai-usage-log.md`
- Review output AI sebelum commit
- Setiap anggota harus memahami kode yang di-commit
```

---

## L. AI Usage Log per Sprint

### Format AI Usage Log Proyek

```markdown
## AI Usage Log — [Nama Proyek]

### Sprint [N]

| No | Tanggal | Anggota | Tool | Prompt (ringkas) | Output (ringkas) | Modifikasi | File yang Terpengaruh |
|----|---------|---------|------|------------------|------------------|------------|-----------------------|
| 1 | ... | ... | ... | ... | ... | ... | ... |
```

### Ketentuan AI Usage Log Proyek

1. AI Usage Log **wajib** diisi setiap sprint dan disimpan di `docs/ai-usage-log.md`.
2. Setiap anggota tim bertanggung jawab mencatat penggunaan AI-nya sendiri.
3. Log harus mencakup: tool, prompt, output, modifikasi, dan file yang terpengaruh.
4. AI Usage Log yang kosong padahal jelas menggunakan AI (terlihat dari code style) akan **mengurangi nilai** komponen AI Usage Log.
5. AI Usage Log yang jujur dan detail akan **menambah nilai** — transparansi dihargai.

---

## M. Contoh Proyek (Fiktif — Angkatan Sebelumnya)

### Sistem Perpustakaan Digital "LibraryUAI"

**Tim:** 4 mahasiswa (Ali, Budi, Citra, Dewi)
**Semester:** Genap 2024/2025

**Fitur yang diimplementasikan:**
- Katalog buku dengan pencarian dan filter (judul, penulis, kategori)
- Manajemen anggota (register, login, profil)
- Peminjaman dan pengembalian buku (dengan validasi stok)
- Dashboard statistik (buku terpopuler, peminjaman per bulan)
- Notifikasi keterlambatan pengembalian

**Tech stack:** Flask + Jinja2 + SQLAlchemy + SQLite + pytest + Docker + Railway

**Hasil:**
- 4 SQLAlchemy models (User, Book, Category, Loan) dengan relationships
- 15 REST API endpoints
- 35 test cases (coverage 85%)
- CI/CD via GitHub Actions (lint + test + deploy)
- Docker deployment di Railway

**Catatan evaluasi:**
- Kekuatan: test coverage tinggi, arsitektur bersih, semua anggota berkontribusi merata
- Area perbaikan: UI bisa lebih menarik, dokumentasi API bisa lebih lengkap
- Nilai proyek: 88 (A)

*Catatan: Contoh ini fiktif untuk memberikan gambaran level ekspektasi.*

---

## N. Kebijakan Khusus

### Perubahan Anggota Tim

- Perubahan anggota tim hanya diizinkan hingga **akhir Minggu 4** dengan persetujuan dosen.
- Setelah Minggu 4, tim bersifat final.
- Jika ada anggota yang drop/mengundurkan diri, tim tetap melanjutkan dengan anggota yang tersisa.

### Proyek Gagal Deploy

- Jika aplikasi gagal di-deploy ke cloud platform, tim masih bisa mendapat nilai untuk komponen lain.
- Deployment di localhost (via Docker) tetap dinilai, tapi komponen CI/CD & Deployment maksimal skor 2.

### Proyek Identik

- Proyek antar-tim yang terdeteksi **substansial identik** (> 70% similarity pada kode) akan diinvestigasi.
- Jika terbukti plagiarisme, kedua tim mendapat nilai **0** untuk proyek.

---

## O. Checklist Akhir Proyek

Sebelum demo, pastikan semua item berikut terpenuhi:

### Teknis
- [ ] Aplikasi berjalan di URL publik
- [ ] Semua fitur CRUD berfungsi
- [ ] Test coverage >= 80%
- [ ] CI pipeline hijau
- [ ] Docker build berhasil

### Dokumentasi
- [ ] README lengkap (deskripsi, install, run, screenshot, API, URL)
- [ ] API documentation
- [ ] Arsitektur diagram
- [ ] Database schema / ERD

### Scrum Artifacts
- [ ] Sprint planning notes (Sprint 0-4)
- [ ] Sprint review notes (Sprint 0-4)
- [ ] Sprint retrospective notes (Start-Stop-Continue)
- [ ] Product backlog (GitHub Issues)

### Individual
- [ ] Peer review form diisi
- [ ] AI Usage Log lengkap
- [ ] Individual contribution summary
- [ ] Setiap anggota siap presentasi dan Q&A

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
