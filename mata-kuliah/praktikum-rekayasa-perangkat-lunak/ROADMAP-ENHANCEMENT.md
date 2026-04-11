# Roadmap Enhancement — Praktikum Rekayasa Perangkat Lunak (IF2206)

**Status:** ✅ v2.0 Complete — Enhancement selesai 12 April 2026
**Terakhir diperbarui:** 12 April 2026
**Selaras dengan:** ROADMAP-ENHANCEMENT IF2205 (Rekayasa Perangkat Lunak)

### Hasil Enhancement v2.0

| Kategori | v1.0 | v2.0 | Growth |
|----------|------|------|--------|
| Lab 01-07 (stub rewrite) | 323 baris | 7.576 baris | 23.5x |
| Lab 09-14 (deep enhance) | 1.253 baris | 3.256 baris | 2.6x |
| Assessments (4 file) | 185 baris | 2.127 baris | 11.5x |
| **TOTAL** | **1.761 baris** | **12.959 baris** | **7.4x** |

Target awal ~7.350 baris — hasil aktual **12.959 baris** (176% dari target).

---

## Latar Belakang

Paket praktikum v1.0 sudah lengkap secara struktur (21 file Markdown), namun kedalaman konten sangat tidak merata. **Lab 01-07 masih berupa stub** (45-47 baris) dan **file asesmen 70-90% lebih dangkal** dibanding referensi (Praktikum Algoritma Pemrograman). Analisis komparatif:

| Kategori | v1.0 Sekarang | Referensi (Praktikum AlPro) | Target v2.0 |
|----------|--------------|----------------------------|-------------|
| Lab Modul (stub: 01-07) | 45-47 baris | 209-371 baris | 300-450 baris |
| Lab Modul (existing: 09-14) | 162-257 baris | 329-498 baris | 350-500 baris |
| Assessment Framework | 71 baris | 441 baris | 350-450 baris |
| Project Guidelines | 54 baris | 440 baris | 350-450 baris |
| Rubrik Laporan | 31 baris | 296 baris | 250-300 baris |
| Rubrik Tugas | 29 baris | 661 baris | 500-650 baris |
| Pedoman Praktikum | 287 baris | 278 baris | ✅ Memadai |
| RPS | 107 baris | — | ✅ Memadai |
| RTM | 118 baris | — | ✅ Memadai |
| **Total baris** | **~2.100** | — | **~7.350** |

### Gap Utama per Dimensi

| Dimensi | v1.0 | Referensi | Gap |
|---------|------|-----------|-----|
| Code blocks per lab (stub) | 0 | 10-20+ | Tidak ada sama sekali |
| Code blocks per lab (existing) | 5-8 | 10-20+ | Perlu 2x lipat |
| Penjelasan konseptual per lab | 0 (stub), 1-2 (existing) | 3-5 section | Belum ada/minim |
| Expected output per langkah | 0 | Setiap langkah | Missing total |
| Troubleshooting tips per lab | 0 | 2-3 per lab | Missing total |
| Contoh real-world Indonesia per lab | 0-1 | 2-3 | Hampir tidak ada |
| Rubrik per dimensi penilaian | 1 tabel generik | 4-6 tabel detail per tugas | Sangat kurang |
| Sprint deliverable detail | 4 baris per sprint | 20-30 baris per sprint | Perlu 5-7x |
| AI Usage Log template/contoh | Disebut saja | Template + contoh lengkap | Belum ada |

---

## Hubungan dengan Roadmap IF2205

Enhancement IF2206 harus **selaras minggu per minggu** dengan IF2205:

| Minggu | IF2205 (Teori) | IF2206 (Praktikum) | Keselarasan |
|--------|---------------|---------------------|-------------|
| 1 | Pengantar RPL & SDLC | Setup Dev Environment | Teori → langsung setup tools |
| 2 | Proses & Model Pengembangan | Git Branching & PR Workflow | Teori model → praktik Git workflow |
| 3 | Requirements Engineering | Requirements Documentation (SRS) | Teori RE → praktik menulis SRS |
| 4 | Pemodelan Requirements | User Story & Sprint Planning | Teori pemodelan → praktik user story |
| 5 | Arsitektur & Design Patterns | Frontend Development | Teori arsitektur → praktik frontend layer |
| 6 | Desain UML & Database | Backend Development (Flask API) | Teori desain → praktik backend layer |
| 7 | Software Construction | Database Integration & ORM | Teori construction → praktik database layer |
| 8 | **UTS** | **Responsi Tengah Semester** | Evaluasi selaras |
| 9 | Software Testing | Unit Testing (pytest & Jest) | Teori testing → praktik unit test |
| 10 | Advanced Testing | Integration & API Testing | Teori advanced → praktik integration test |
| 11 | DevOps & CI/CD | CI/CD dengan GitHub Actions | Teori DevOps → praktik CI/CD pipeline |
| 12 | Maintenance & Evolution | Docker & Deployment | Teori maintenance → praktik containerization |
| 13 | AI-Augmented SE | AI Pair Programming & Code Review | Teori AI SE → praktik AI pair programming |
| 14 | Modern SE Trends | Sprint Review & Retrospective | Teori trends → praktik Agile review |
| 15 | Presentasi Proyek Akhir | Demo Proyek Akhir | Selaras — proyek yang sama |
| 16 | **UAS** | **Responsi Akhir Semester** | Evaluasi selaras |

**Prinsip:** Setiap lab praktikum harus **merujuk modul teori minggu yang sama** dan menggunakan **studi kasus proyek yang konsisten** (Sistem Perpustakaan UAI atau proyek tim mahasiswa).

---

## Rencana Enhancement v2.0

### 17 File yang Perlu Di-enhance

Enhancement hanya mencakup file konten — file foundation (RPS, RTM, pedoman, README) sudah memadai.

### 5 Batch Eksekusi (Berurutan berdasarkan Prioritas)

#### Batch P1: Lab 01-07 Rewrite Total — HIGHEST PRIORITY

Lab 01-07 saat ini hanya stub (45-47 baris). Perlu **rewrite hampir total** menjadi hands-on guide lengkap yang bisa diselesaikan mahasiswa dalam 100 menit di GitHub Codespaces.

| File | v1.0 | Target v2.0 | Enhancement Kunci |
|------|------|-------------|-------------------|
| `lab-01-setup-dev-environment-github-codespaces.md` | 46 | 350 | Screenshot guidance Codespaces, devcontainer.json, Python/Flask install step-by-step, Hello World lengkap dengan expected output, troubleshooting common errors, Git init + first commits |
| `lab-02-git-branching-dan-pull-request-workflow.md` | 45 | 400 | Git branch strategy visual, 8+ Git commands dengan expected output, PR workflow step-by-step, merge conflict resolution exercise, conventional commits, studi kasus tim proyek |
| `lab-03-requirements-documentation-srs.md` | 46 | 400 | SRS template IEEE 830 lengkap, studi kasus Sistem Perpustakaan UAI, functional vs non-functional requirements exercise, stakeholder interview role-play guide, validasi requirements checklist |
| `lab-04-user-story-dan-sprint-planning.md` | 46 | 400 | User story INVEST format + 10 contoh, acceptance criteria Given-When-Then, product backlog dengan MoSCoW, sprint planning exercise, GitHub Projects/Issues setup |
| `lab-05-frontend-development-html-css-javascript.md` | 47 | 450 | HTML5 semantic structure, CSS responsive layout, Jinja2 template inheritance, JavaScript DOM manipulation, form validation, 3 halaman lengkap (login, dashboard, CRUD) dengan code runnable |
| `lab-06-backend-development-python-flask-api.md` | 47 | 450 | Flask project structure (factory pattern), 5+ REST endpoints CRUD, request/response handling, error handling & status codes, Flask-CORS, Postman/curl testing, studi kasus API Perpustakaan |
| `lab-07-database-integration-dan-orm.md` | 47 | 450 | SQLAlchemy model definition (3+ models), relationships (1:N, M:N), database migrations (Flask-Migrate), seed data script, CRUD operations via ORM, query examples, ERD → code mapping |

#### Batch P2: Lab 09-14 Deep Enhancement

Lab 09-14 sudah punya konten dasar (162-257 baris) tapi perlu diperdalam agar setara referensi (329-498 baris).

| File | v1.0 | Target v2.0 | Enhancement Kunci |
|------|------|-------------|-------------------|
| `lab-09-unit-testing-dengan-pytest-dan-jest.md` | 229 | 400 | Tambah konsep singkat testing theory, expected output setiap test, troubleshooting test failures, edge case examples, coverage analysis walkthrough |
| `lab-10-integration-testing-dan-api-testing.md` | 257 | 420 | Tambah API testing dengan requests/httpx, test database isolation, end-to-end scenario walkthrough, mock vs real database discussion, Postman collection export |
| `lab-11-ci-cd-dengan-github-actions.md` | 181 | 400 | Workflow YAML explained line-by-line, multi-stage pipeline (lint → test → build → deploy), secrets management, status badges, troubleshooting failed runs |
| `lab-12-docker-containerization-dan-deployment.md` | 230 | 420 | Dockerfile best practices, multi-stage build, docker-compose untuk dev vs prod, environment variables, deployment ke Railway/Render step-by-step dengan screenshots guidance |
| `lab-13-ai-pair-programming-dan-code-review.md` | 162 | 380 | AI prompt engineering untuk SE tasks (CRIDE framework), code review checklist, worked examples prompt → output → evaluasi, AI Usage Log template dengan contoh diisi, etika AI |
| `lab-14-sprint-review-dan-retrospective.md` | 194 | 380 | Sprint review presentation template, retrospective facilitation guide (Start-Stop-Continue), velocity calculation, burndown chart, individual contribution reflection, final documentation checklist |

#### Batch P3: Rubrik & Assessment Framework — HIGH PRIORITY

File asesmen saat ini sangat minim. Mahasiswa dan dosen membutuhkan rubrik detail untuk konsistensi penilaian.

| File | v1.0 | Target v2.0 | Enhancement Kunci |
|------|------|-------------|-------------------|
| `assessment-framework-praktikum.md` | 71 | 400 | Matrix CPMK × asesmen lengkap, policy AI per komponen, jadwal deadline, remidi, format laporan standar, integrasi dengan IF2205, flowchart proses penilaian |
| `rubrik-tugas.md` | 29 | 600 | Rubrik detail per tugas (TP1-TP6) masing-masing dengan 4-5 dimensi × 4 level, contoh submission excellent vs inadequate, AI policy per tugas, deliverable checklist per tugas |
| `rubrik-laporan-praktikum.md` | 31 | 280 | Template laporan standar, rubrik 5 dimensi × 4 level, contoh laporan baik vs buruk, format penulisan (Markdown di GitHub), AI Usage Log section requirement |
| `project-guidelines.md` | 54 | 420 | Sprint deliverables detail (20-30 baris per sprint), tech stack requirements expanded, GitHub repo structure template, definition of done per sprint, demo evaluation criteria, peer review form, contoh proyek tahun lalu (fiktif), retrospective template |

#### Batch P4: Datasets & Starter Code Reference

| File | v1.0 | Target v2.0 | Enhancement Kunci |
|------|------|-------------|-------------------|
| `datasets/README.md` | (existing) | 150 | Daftar starter code templates per lab, link ke Flask boilerplate, contoh .devcontainer config, daftar Python/JS packages yang digunakan per lab, referensi tutorial eksternal per topik |

#### Batch P5: Cross-Reference & Integration Pass

Batch terakhir bukan file baru, tapi **pass integrasi** di semua file yang sudah di-enhance:

- [ ] Setiap lab merujuk modul teori IF2205 minggu yang sama (link relatif ke `../rekayasa-perangkat-lunak/03-modules/`)
- [ ] Studi kasus konsisten: gunakan Sistem Perpustakaan UAI sebagai red thread di Lab 03-14
- [ ] Code antar lab saling sambung (lab-05 frontend → lab-06 backend → lab-07 database → lab-09 testing)
- [ ] Proyek akhir deliverables di project-guidelines.md selaras dengan rubrik di assessment-framework
- [ ] AI Usage Log template konsisten di semua lab yang mengizinkan AI
- [ ] CPMK mapping di setiap lab header konsisten dengan RPS

---

## Template Enhancement per Kategori

### Lab Praktikum — Setiap Lab Harus Mengandung:

1. **Header + Informasi Lab** (tabel: MK, praktikum ke-N, topik, CPMK, durasi 100 menit, platform, prasyarat)
2. **Tujuan Praktikum** (3-4 objectives dengan Bloom's verbs)
3. **Konsep Singkat** (30-50 baris):
   - Pengantar teori ringkas yang relevan
   - Link ke modul teori IF2205 minggu yang sama
   - Diagram/visual konsep (ASCII)
4. **Persiapan** (tools, dependencies, files yang perlu disiapkan)
5. **Langkah-langkah** (6-8 steps, masing-masing berisi):
   - Penjelasan WHY (mengapa langkah ini penting)
   - Code lengkap dan runnable di GitHub Codespaces
   - Expected output (apa yang seharusnya muncul)
   - Troubleshooting tips (common errors dan solusinya)
   - Estimasi waktu per langkah
6. **Tantangan Tambahan** (3 challenges bertingkat: basic, intermediate, advanced)
7. **Refleksi & AI Usage Log** reminder (template singkat)
8. **Checklist Penyelesaian** (checkbox items yang spesifik dan terukur)
9. **Footer tagline**

### Assessment & Rubrik — Setiap File Harus Mengandung:

1. **Header + Informasi** (mata kuliah, bobot, policy)
2. **Tabel rubrik** (dimensi × level: Excellent/Good/Adequate/Inadequate)
3. **Deliverable checklist** yang spesifik per tugas/sprint
4. **Contoh** submission berkualitas baik (singkat)
5. **AI Policy** yang jelas per komponen
6. **Footer tagline**

---

## Contoh Studi Kasus Konsisten: Sistem Perpustakaan Digital UAI

Seluruh lab menggunakan **satu proyek berkelanjutan** sebagai red thread:

| Lab | Kontribusi ke Proyek |
|-----|---------------------|
| Lab 01 | Setup environment, Flask Hello World |
| Lab 02 | Git repo perpustakaan, branching strategy |
| Lab 03 | SRS Sistem Perpustakaan Digital UAI |
| Lab 04 | User stories: "Sebagai mahasiswa, saya ingin mencari buku..." |
| Lab 05 | Frontend: halaman pencarian buku, katalog, login |
| Lab 06 | Backend: API endpoints GET/POST/PUT/DELETE buku |
| Lab 07 | Database: model Buku, User, Peminjaman + relationships |
| Lab 09 | Unit test: test model, test API endpoint buku |
| Lab 10 | Integration test: test alur peminjaman end-to-end |
| Lab 11 | CI/CD: GitHub Actions untuk lint + test + deploy |
| Lab 12 | Docker: containerize Perpustakaan, deploy ke Railway |
| Lab 13 | AI: gunakan AI untuk code review & generate test cases |
| Lab 14 | Sprint review: demo Perpustakaan, retrospective tim |

---

## Mapping Batch IF2206 ↔ Batch IF2205

Agar eksekusi enhancement **dua mata kuliah bisa berjalan paralel atau berurutan** dengan konsisten:

| Batch IF2205 (Teori) | Batch IF2206 (Praktikum) | Ketergantungan |
|----------------------|--------------------------|----------------|
| Batch 1: Buku Ajar Bab 1-4 | Batch P1: Lab 01-04 | Lab merujuk konsep dari buku ajar |
| Batch 2: Buku Ajar Bab 5-7 | Batch P1: Lab 05-07 | Lab implementasi arsitektur & construction |
| Batch 5: Modul Mingguan 1-8 | Batch P1: Lab 01-07 | Modul memberikan konteks pre-class |
| Batch 3: Buku Ajar Bab 8-11 | Batch P2: Lab 09-12 | Lab testing & DevOps |
| Batch 6: Modul Mingguan 9-16 | Batch P2: Lab 09-14 | Modul memberikan konteks pre-class |
| Batch 4: Buku Ajar Bab 12-14 | Batch P2: Lab 13-14 | Lab AI & Agile review |
| Batch 7: Lab Teori IF2205 | Batch P2: Lab IF2206 | Lab teori = konseptual, lab praktikum = hands-on |
| — | Batch P3: Rubrik & Assessment | Independen, bisa kapan saja |
| — | Batch P4: Datasets/Starter | Independen |
| — | Batch P5: Cross-reference pass | Setelah semua batch selesai |

---

## Verification Checklist v2.0

Setelah enhancement selesai:

- [ ] `wc -l` setiap lab file memenuhi target minimum
- [ ] Setiap lab: Konsep Singkat section, 6+ langkah dengan code, expected output per langkah
- [ ] Lab 01-07: code lengkap runnable (bukan placeholder), troubleshooting tips
- [ ] Lab 09-14: diperdalam dengan konsep, expected output, edge cases
- [ ] Studi kasus Perpustakaan UAI konsisten di Lab 03-14
- [ ] Code antar lab saling sambung (frontend → backend → database → testing → deployment)
- [ ] Setiap lab merujuk modul teori IF2205 yang sesuai
- [ ] Rubrik tugas (TP1-TP6): masing-masing punya rubrik detail 4-5 dimensi × 4 level
- [ ] Project guidelines: deliverables per sprint detail, definition of done
- [ ] AI Usage Log template tersedia dan dirujuk di setiap lab
- [ ] CPMK mapping konsisten dengan RPS di setiap lab header
- [ ] Platform: GitHub Codespaces (bukan Google Colab)
- [ ] Bahasa: Indonesia + bilingual technical terms
- [ ] Footer tagline di setiap file
- [ ] Assessment weights total 100% (Laporan 25% + Tugas 25% + Proyek 35% + Responsi 10% + Partisipasi 5%)

---

## Estimasi Total

- **17 file** perlu di-enhance (13 lab + 4 asesmen)
- **~5.250 baris** konten baru perlu ditambahkan
- Total konten v2.0: **~7.350 baris** (dari ~2.100 di v1.0)
- **Peningkatan 3.5x** dari v1.0

---

## Urutan Eksekusi yang Disarankan (IF2205 + IF2206 Combined)

Untuk efisiensi maksimal, enhancement kedua MK bisa dijalankan dengan urutan berikut:

| Urutan | Batch | MK | File | Prioritas |
|--------|-------|----|------|-----------|
| 1 | Batch 1 | IF2205 | Buku Ajar Bab 1-4 | HIGHEST |
| 2 | **Batch P1a** | **IF2206** | **Lab 01-04 (rewrite)** | **HIGHEST** |
| 3 | Batch 2 | IF2205 | Buku Ajar Bab 5-7 | HIGH |
| 4 | **Batch P1b** | **IF2206** | **Lab 05-07 (rewrite)** | **HIGH** |
| 5 | **Batch P3** | **IF2206** | **Rubrik & Assessment** | **HIGH** |
| 6 | Batch 3 | IF2205 | Buku Ajar Bab 8-11 | MEDIUM |
| 7 | **Batch P2a** | **IF2206** | **Lab 09-12 (enhance)** | **MEDIUM** |
| 8 | Batch 4 | IF2205 | Buku Ajar Bab 12-14 | MEDIUM |
| 9 | **Batch P2b** | **IF2206** | **Lab 13-14 (enhance)** | **MEDIUM** |
| 10 | Batch 5 | IF2205 | Modul Mingguan 1-8 | MEDIUM |
| 11 | Batch 6 | IF2205 | Modul Mingguan 9-16 | LOW |
| 12 | Batch 7 | IF2205 | Lab Teori 13 file | LOW |
| 13 | **Batch P4** | **IF2206** | **Datasets & Starter Code** | **LOW** |
| 14 | Batch 8 | IF2205 | ~~Lab Praktikum~~ (sudah dicakup P1+P2) | MERGED |
| 15 | **Batch P5** | **IF2206** | **Cross-reference pass** | **FINAL** |

> **Catatan:** Batch 8 di roadmap IF2205 (Lab Praktikum 13 file) sekarang **digantikan** oleh Batch P1 + P2 di roadmap ini, karena lebih detail dan terstruktur.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
