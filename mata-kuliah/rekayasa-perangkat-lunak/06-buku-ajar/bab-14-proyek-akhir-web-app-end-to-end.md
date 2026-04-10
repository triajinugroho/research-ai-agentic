# BAB 14: PROYEK AKHIR — WEB APP END-TO-END

**Oleh: Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom |
|-----------|-----------|-------------|
| 7.3 | Merancang dan membangun web application end-to-end dalam tim Agile/Scrum | C6 (Mencipta) |
| 7.4 | Mempresentasikan proyek dengan demo, dokumentasi, dan refleksi pembelajaran | C5-C6 |

---

## 14.1 Gambaran Proyek Akhir

### 14.1.1 Tujuan Proyek

Proyek akhir mengintegrasikan **seluruh pengetahuan SE** dari Bab 1-13:
- Requirements engineering → Design → Construction → Testing → Deployment
- Dikerjakan dalam tim 3-4 orang menggunakan Agile/Scrum
- Menghasilkan web app yang **functional, tested, dan deployed**

### 14.1.2 Pilihan Proyek (Konteks Indonesia)

| # | Proyek | Deskripsi | Kompleksitas |
|---|--------|-----------|-------------|
| 1 | Sistem Informasi Perpustakaan | Katalog, peminjaman, pengembalian, notifikasi | Medium |
| 2 | Aplikasi Manajemen UMKM | Inventory, penjualan, laporan keuangan sederhana | Medium |
| 3 | Sistem Antrian Puskesmas | Pendaftaran, antrian real-time, rekam medis | Medium-High |
| 4 | Platform E-Commerce Produk Lokal | Katalog produk, cart, checkout, tracking | Medium-High |
| 5 | Aplikasi Pengelolaan Zakat/Infaq | Pencatatan, distribusi, laporan, muzakki/mustahik | Medium |

## 14.2 Sprint Timeline

### 14.2.1 Empat Sprint (Minggu 5-15)

| Sprint | Minggu | Fokus | Deliverable |
|--------|--------|-------|-------------|
| **Sprint 1** | 5-7 | Requirements + Design + Setup | SRS, UML, ERD, API design, repo setup |
| **Sprint 2** | 9-10 | Core Development | Backend API, frontend pages, database |
| **Sprint 3** | 11-12 | Testing + CI/CD | Unit tests, integration tests, pipeline, Docker |
| **Sprint 4** | 13-14 | Polish + Deploy | Final features, deployment, documentation |

### 14.2.2 Sprint 1: Foundation (Minggu 5-7)

**Sprint Goal:** "Desain lengkap dan repository siap untuk development"

Deliverables:
- [ ] 15 user stories dengan acceptance criteria
- [ ] Product backlog (MoSCoW prioritized)
- [ ] Class Diagram + Sequence Diagram
- [ ] ERD + SQL schema
- [ ] REST API endpoint list
- [ ] GitHub repository dengan branching strategy
- [ ] README.md dengan project description

### 14.2.3 Sprint 2: Core Development (Minggu 9-10)

**Sprint Goal:** "Fitur utama (Must Have) berfungsi end-to-end"

Deliverables:
- [ ] Flask backend dengan minimal 5 API endpoints
- [ ] Frontend halaman utama (login, dashboard, fitur inti)
- [ ] Database terintegrasi (SQLAlchemy models)
- [ ] Authentication (login/register)
- [ ] Minimal 3 fitur Must Have berjalan

### 14.2.4 Sprint 3: Quality (Minggu 11-12)

**Sprint Goal:** "Kode tested, pipeline otomatis, dan ready for deployment"

Deliverables:
- [ ] Unit tests (coverage ≥ 70%)
- [ ] Integration tests untuk API endpoints
- [ ] GitHub Actions CI pipeline
- [ ] Dockerfile + docker-compose.yml
- [ ] Should Have features (jika waktu memungkinkan)

### 14.2.5 Sprint 4: Polish & Deploy (Minggu 13-14)

**Sprint Goal:** "Aplikasi deployed dan siap demo"

Deliverables:
- [ ] Deployment ke cloud (Railway/Render)
- [ ] Final bug fixes dan polish
- [ ] API documentation
- [ ] User guide
- [ ] Presentation slides
- [ ] AI Usage Log lengkap

## 14.3 GitHub Repository Structure

```
nama-proyek/
├── README.md                 # Project overview, setup, API docs
├── requirements.txt          # Python dependencies
├── Dockerfile               # Container configuration
├── docker-compose.yml       # Multi-container setup
├── .github/
│   └── workflows/
│       └── ci.yml           # CI/CD pipeline
├── app/
│   ├── __init__.py          # App factory
│   ├── config.py            # Configuration
│   ├── models/              # SQLAlchemy models
│   ├── routes/              # Flask Blueprints
│   ├── services/            # Business logic
│   └── templates/           # HTML templates
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── tests/
│   ├── test_models.py
│   ├── test_routes.py
│   └── test_services.py
├── docs/
│   ├── srs.md
│   ├── api-docs.md
│   ├── user-guide.md
│   └── ai-usage-log.md
└── migrations/              # Database migrations
```

## 14.4 Demo dan Presentasi

### 14.4.1 Demo Checklist

- [ ] Aplikasi berjalan live (bukan localhost)
- [ ] Demo semua fitur Must Have
- [ ] Tunjukkan CI/CD pipeline (green build)
- [ ] Tunjukkan test results dan coverage
- [ ] Demo deployment process

### 14.4.2 Struktur Presentasi (15 menit/tim)

| Bagian | Durasi | Konten |
|--------|--------|--------|
| Intro | 2 menit | Tim, project overview, problem statement |
| Architecture | 3 menit | Tech stack, arsitektur, UML key diagrams |
| Demo | 5 menit | Live demo fitur utama |
| Engineering | 3 menit | Testing, CI/CD, deployment |
| Lessons Learned | 2 menit | Apa yang berjalan baik, apa yang dipelajari |

## 14.5 Grading Rubric

| Komponen | Bobot | Kriteria |
|----------|-------|----------|
| Requirements & Design | 15% | SRS, user stories, UML, ERD |
| Implementation | 25% | Kode quality, fitur lengkap, clean code |
| Testing | 15% | Coverage ≥ 70%, test quality |
| DevOps | 10% | CI/CD, Docker, deployment |
| Presentation | 10% | Demo, slides, komunikasi |
| Teamwork | 10% | Git log, fair contribution, Scrum artifacts |
| Documentation | 10% | README, API docs, user guide |
| AI Integration | 5% | AI Usage Log, responsible usage |

## 14.6 Portfolio Building

### 14.6.1 Tips Portfolio

Proyek akhir bisa menjadi portfolio piece yang kuat:
1. **README yang profesional** — screenshots, tech stack badges, setup instructions
2. **Clean Git history** — conventional commits, meaningful PRs
3. **Live demo URL** — deployed dan bisa diakses
4. **Documentation** — API docs, arsitektur diagram
5. **LinkedIn/GitHub profile** — link ke proyek

### 14.6.2 Refleksi Pembelajaran

Pertanyaan refleksi:
- Apa skill SE yang paling berharga dari proyek ini?
- Bagaimana AI membantu (dan tidak membantu) dalam development?
- Apa yang akan Anda lakukan berbeda jika mengulang proyek?
- Bagaimana pengalaman bekerja dalam tim Agile?

---

## AI Corner: AI sebagai Development Partner (Level: Expert)

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| Architecture review | "Review arsitektur proyek kami: Flask + SQLite + vanilla JS. Apa yang bisa improved untuk scalability?" | Gunakan sebagai second opinion |
| Code completion | "Implement fitur [X] berdasarkan user story dan acceptance criteria berikut: [paste]" | Review setiap baris |
| Final testing | "Generate comprehensive test suite untuk semua API endpoints di proyek kami" | Supplement, bukan replace manual testing |
| Documentation | "Buatkan API documentation lengkap berdasarkan Flask routes berikut: [paste]" | Verify accuracy |

---

## Latihan Soal

### Level Dasar (C1-C2)
1. Sebutkan 4 sprint dan deliverable masing-masing dalam proyek akhir.
2. Jelaskan 8 komponen grading rubric proyek.

### Level Menengah (C3-C4)
3. Buatlah Sprint 1 Backlog untuk proyek Sistem Antrian Puskesmas dengan 10 tasks beserta estimasi.
4. Buatlah repository structure untuk proyek tim Anda.

### Level Mahir (C5-C6)
5. Rancang rencana proyek lengkap dari Sprint 1-4 untuk salah satu opsi proyek — termasuk user stories, arsitektur, timeline, risk register, dan definition of done.
6. Refleksi: evaluasi pengalaman tim Anda selama proyek — apa yang berjalan baik dan apa yang perlu diperbaiki?

---

## Rangkuman

1. **Proyek akhir** mengintegrasikan seluruh pengetahuan SE (Bab 1-13) dalam satu web app.
2. **Empat sprint** membagi proyek: Foundation → Core Development → Quality → Polish & Deploy.
3. **GitHub repository** harus terstruktur profesional dengan docs, tests, CI/CD.
4. **Demo** adalah momen penting — tunjukkan fitur, arsitektur, dan engineering practices.
5. **Grading** mencakup teknis (implementation, testing, DevOps) dan soft skills (teamwork, presentation).
6. **Portfolio** — proyek ini bisa menjadi showcase pertama di karier Anda.

---

## Referensi

1. Cohn, M. (2005). *Agile Estimating and Planning*. Prentice Hall.
2. Humble, J. & Farley, D. (2010). *Continuous Delivery*. Addison-Wesley.
3. GitHub Docs. (2024). *Building a portfolio with GitHub*. docs.github.com.
4. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
