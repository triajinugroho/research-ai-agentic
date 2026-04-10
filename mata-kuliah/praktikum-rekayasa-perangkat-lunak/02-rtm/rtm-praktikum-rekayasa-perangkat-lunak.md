# Rencana Tugas Mahasiswa (RTM) — Praktikum Rekayasa Perangkat Lunak (IF2206)

## A. Komponen Tugas

### Laporan Praktikum (L1–L13)

| Kode | Minggu | Topik Laporan | Deadline |
|------|--------|---------------|----------|
| L1 | 1 | Setup Environment & Hello Flask | Minggu 2 |
| L2 | 2 | Git Workflow & Branching | Minggu 3 |
| L3 | 3 | Dokumen SRS | Minggu 4 |
| L4 | 4 | User Story & Product Backlog | Minggu 5 |
| L5 | 5 | Frontend dengan Jinja2 | Minggu 6 |
| L6 | 6 | Backend REST API | Minggu 7 |
| L7 | 7 | Database Integration | Minggu 8 |
| L8 | 9 | Unit Testing dengan pytest | Minggu 10 |
| L9 | 10 | Integration Testing | Minggu 11 |
| L10 | 11 | CI/CD Pipeline | Minggu 12 |
| L11 | 12 | Docker Containerization | Minggu 13 |
| L12 | 13 | AI-Augmented Development | Minggu 14 |
| L13 | 14 | Sprint Review & Retrospective | Minggu 15 |

### Tugas Pemrograman (TP1–TP6)

| Kode | Topik | CPMK | Deadline |
|------|-------|------|----------|
| TP1 | Flask Hello World App | CPMK-1, CPMK-4 | Minggu 3 |
| TP2 | Git Branching & Merge Conflict | CPMK-2 | Minggu 4 |
| TP3 | REST API CRUD | CPMK-4 | Minggu 8 |
| TP4 | Database CRUD dengan SQLAlchemy | CPMK-4 | Minggu 10 |
| TP5 | Testing Suite (unit + integration) | CPMK-5 | Minggu 12 |
| TP6 | Dockerfile & docker-compose | CPMK-6 | Minggu 14 |

### Proyek Tim (Sprint 1–4)

| Sprint | Minggu | Fokus | Deliverable |
|--------|--------|-------|-------------|
| Sprint 1 | 5–7 | Frontend + Backend dasar | Prototipe UI + API endpoint |
| Sprint 2 | 9–10 | Backend + Database | Fitur CRUD lengkap |
| Sprint 3 | 11–12 | Testing + CI/CD | Test suite + pipeline |
| Sprint 4 | 13–14 | Deployment + Polish | Aplikasi terdeploy + dokumentasi |

### Responsi

| Kode | Minggu | Cakupan | Bobot |
|------|--------|---------|-------|
| RTS | 8 | Materi Minggu 1–7 (setup, Git, requirements, frontend, backend, database) | 5% |
| RAS | 16 | Materi Minggu 9–15 (testing, CI/CD, Docker, AI, proyek) | 5% |

## B. Detail Tugas Pemrograman

### TP1 — Flask Hello World App
- **Deskripsi:** Buat aplikasi Flask sederhana dengan minimal 3 route (home, about, contact), template Jinja2, dan CSS dasar.
- **Input:** Tidak ada input khusus.
- **Output:** Aplikasi berjalan di localhost:5000 dengan halaman yang ter-render.
- **Kriteria:** Route berfungsi, template ter-render, styling diterapkan.

### TP2 — Git Branching & Merge Conflict
- **Deskripsi:** Buat repository GitHub dengan branch `main`, `develop`, dan `feature-*`. Simulasikan merge conflict dan selesaikan.
- **Input:** Repository dengan minimal 3 branch dan 10 commit.
- **Output:** Screenshot/log history Git yang menunjukkan branching, merge, dan conflict resolution.
- **Kriteria:** Branching strategy benar, conflict diselesaikan, commit message deskriptif.

### TP3 — REST API CRUD
- **Deskripsi:** Implementasikan REST API untuk entitas utama proyek (misalnya: produk, mahasiswa, atau buku) dengan endpoint GET, POST, PUT, DELETE.
- **Input:** JSON request body.
- **Output:** JSON response dengan status code yang sesuai (200, 201, 404, dll.).
- **Kriteria:** Endpoint RESTful, validasi input, error handling, dokumentasi API.

### TP4 — Database CRUD dengan SQLAlchemy
- **Deskripsi:** Hubungkan aplikasi Flask dengan database SQLite/PostgreSQL menggunakan SQLAlchemy ORM. Implementasikan model, migrasi, dan operasi CRUD.
- **Input:** Data dari form atau API request.
- **Output:** Data tersimpan dan dapat diambil dari database.
- **Kriteria:** Model relasional benar, migrasi berjalan, CRUD berfungsi, query efisien.

### TP5 — Testing Suite
- **Deskripsi:** Tulis test suite menggunakan pytest yang mencakup unit test (minimal 10 test case) dan integration test (minimal 5 test case) untuk aplikasi proyek.
- **Input:** Kode aplikasi proyek.
- **Output:** Laporan pytest dengan coverage minimal 70%.
- **Kriteria:** Test case bermakna, coverage memadai, fixture digunakan, mocking diterapkan.

### TP6 — Dockerfile & docker-compose
- **Deskripsi:** Kontainerisasi aplikasi proyek dengan Dockerfile multi-stage dan docker-compose untuk orkestrasi (app + database).
- **Input:** Kode aplikasi proyek.
- **Output:** Container berjalan di Docker dengan `docker-compose up`.
- **Kriteria:** Dockerfile efisien, docker-compose benar, environment variable digunakan, dokumentasi jelas.

## C. Timeline Semester

```
Minggu:  1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16
         |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
Laporan: L1   L2   L3   L4   L5   L6   L7   --  L8   L9  L10  L11  L12  L13  --   --
Tugas:   --   --  TP1  TP2   --   --   --  TP3  --  TP4   --  TP5   --  TP6  --   --
Sprint:  --   --   --   --  ===Sprint 1===  --  ==Sprint 2==  ==Sprint 3==  S4   --
Responsi:--   --   --   --   --   --   --  RTS  --   --   --   --   --   --   --  RAS
```

## D. Kebijakan Penggunaan AI

| Komponen | Kebijakan AI | Keterangan |
|----------|-------------|------------|
| Laporan Praktikum | Diizinkan dengan log | AI boleh digunakan untuk membantu penulisan, wajib mencantumkan AI Usage Log |
| Tugas Pemrograman | Diizinkan dengan log | AI boleh digunakan sebagai mitra coding, wajib log dan pemahaman kode |
| Proyek Tim | Diizinkan dengan log | AI boleh untuk code review, debugging, refactoring — wajib AI Usage Log per sprint |
| Responsi (RTS/RAS) | **Tidak diizinkan** | Responsi bersifat individu dan closed-book, tanpa akses AI |

### Ketentuan AI Usage Log

Setiap penggunaan AI harus didokumentasikan dengan format:
1. **Tool yang digunakan** (ChatGPT / Claude / Copilot / lainnya)
2. **Prompt yang diberikan** (ringkasan)
3. **Output yang digunakan** (bagian mana yang dipakai)
4. **Modifikasi yang dilakukan** (perubahan dari output AI)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
