# Panduan Proyek Akhir — Rekayasa Perangkat Lunak (IF2205)

## Informasi Proyek

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Bobot** | 25% nilai akhir |
| **Tim** | 3-4 mahasiswa |
| **Timeline** | Sprint 1-4 (Minggu 5-15) |
| **Tech Stack** | Python Flask + HTML/CSS/JS + SQLite/PostgreSQL |
| **Platform** | GitHub Codespaces |
| **AI Policy** | AI sebagai partner + wajib AI Usage Log |

## Pembentukan Tim

- **Ukuran:** 3-4 mahasiswa per tim
- **Pembentukan:** Mandiri (mahasiswa memilih sendiri) — deadline Minggu 4
- **Roles (Scrum):** Product Owner, Scrum Master, Developer(s) — rotasi per sprint dianjurkan
- Tim yang sama digunakan untuk Praktikum RPL (IF2206)

## Pilihan Proyek

| # | Proyek | Deskripsi | Stakeholder |
|---|--------|-----------|-------------|
| 1 | **Sistem Informasi Perpustakaan** | Katalog buku, peminjaman, pengembalian, notifikasi | Pustakawan, mahasiswa |
| 2 | **Aplikasi Manajemen UMKM** | Inventory, penjualan, laporan keuangan sederhana | Pemilik UMKM, karyawan |
| 3 | **Sistem Antrian Puskesmas** | Pendaftaran, antrian real-time, rekam medis | Pasien, petugas, dokter |
| 4 | **Platform E-Commerce Produk Lokal** | Katalog produk, cart, checkout, tracking | Pembeli, penjual |
| 5 | **Aplikasi Pengelolaan Zakat/Infaq** | Pencatatan, distribusi, laporan | Muzakki, amil, mustahik |

Tim boleh mengajukan proyek lain dengan persetujuan dosen (deadline Minggu 5).

## Timeline Sprint

| Sprint | Minggu | Fokus | Deliverable |
|--------|--------|-------|-------------|
| **Sprint 0** | 5-6 | Planning: Team formation, SRS, User Stories, Architecture, Repo setup | SRS, User Stories, UML, ERD, API Design, Repo Setup |
| **Sprint 1** | 7 + 9 | MVP: Backend API, Frontend pages, Database, Basic tests | Backend API, Frontend, Database, Auth. Minggu 8 = UTS (tidak ada aktivitas sprint) |
| **Sprint 2** | 10-11 | Features: Advanced features, Integration tests, CI pipeline | Additional features, Integration tests, CI pipeline |
| **Sprint 3** | 12-13 | Quality: E2E tests, Docker, Deployment, AI-assisted review | E2E tests, Docker, Deployment, AI-assisted review |
| **Sprint 4** | 14 | Polish: Bug fixes, Documentation, Presentation prep | Bug fixes, documentation, presentation slides, AI Usage Log |
| **Demo** | 15 | Presentasi | Live demo, slides, refleksi |

## Deliverables per Sprint

### Sprint 1
- [ ] 15 user stories (INVEST) + acceptance criteria
- [ ] Product Backlog (MoSCoW prioritized)
- [ ] Class Diagram + Sequence Diagram
- [ ] ERD + SQL schema
- [ ] REST API endpoint list
- [ ] GitHub repo + README + branching strategy

### Sprint 2
- [ ] Flask backend (5+ API endpoints)
- [ ] Frontend (login, dashboard, fitur inti)
- [ ] Database (SQLAlchemy models + relationships)
- [ ] Authentication
- [ ] Must Have features berfungsi

### Sprint 3
- [ ] Unit tests (coverage ≥ 70%)
- [ ] Integration tests
- [ ] GitHub Actions CI pipeline
- [ ] Dockerfile + docker-compose.yml

### Sprint 4
- [ ] Cloud deployment (Railway/Render)
- [ ] Bug fixes + polish
- [ ] API documentation
- [ ] User guide
- [ ] Presentation slides
- [ ] AI Usage Log

## Rubrik Penilaian

| Komponen | Bobot | Kriteria |
|----------|-------|----------|
| Requirements & Design | 15% | SRS lengkap, user stories INVEST, UML benar, ERD normalized |
| Implementation | 25% | Fitur berjalan, clean code, modular, error handling |
| Testing | 15% | Coverage ≥ 70%, test quality, TDD evidence |
| DevOps & Deployment | 10% | CI/CD working, Docker, successful deployment |
| Teamwork & Scrum | 10% | Git log adil, Scrum artifacts, fair contribution |
| Documentation | 10% | README, API docs, user guide lengkap |
| Presentation & Demo | 10% | Live demo lancar, slides profesional, Q&A |
| AI Integration & Usage Log | 5% | AI Usage Log lengkap, responsible usage |

## Persyaratan GitHub Repository

```
nama-proyek/
├── README.md            # Overview, setup, API docs
├── requirements.txt     # Python dependencies
├── Dockerfile
├── docker-compose.yml
├── .github/workflows/ci.yml
├── app/                 # Source code
├── tests/               # Test files
├── static/              # CSS, JS, images
└── docs/                # SRS, UML, AI Usage Log
```

## Demo Checklist

- [ ] Aplikasi berjalan live (bukan localhost)
- [ ] Demo semua Must Have features
- [ ] Tunjukkan CI/CD pipeline (green build)
- [ ] Tunjukkan test results + coverage
- [ ] Setiap anggota tim presentasi

## Presentasi (15 menit/tim)

| Bagian | Durasi | Konten |
|--------|--------|--------|
| Intro | 2 min | Tim, problem statement, proyek overview |
| Architecture | 3 min | Tech stack, arsitektur, diagram kunci |
| Demo | 5 min | Live demo fitur utama |
| Engineering | 3 min | Testing, CI/CD, deployment |
| Lessons | 2 min | Apa yang berjalan baik, apa yang dipelajari |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
