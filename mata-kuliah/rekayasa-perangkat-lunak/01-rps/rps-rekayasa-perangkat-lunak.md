# Rencana Pembelajaran Semester (RPS)

## Mata Kuliah: Rekayasa Perangkat Lunak

---

## A. Identitas Mata Kuliah

| Komponen | Detail |
|----------|--------|
| **Nama Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **SKS** | 3 SKS (Teori) |
| **Semester** | 4 (Genap) |
| **Tahun Akademik** | 2025/2026 |
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika |
| **Fakultas** | Sains dan Teknologi |
| **Universitas** | Al Azhar Indonesia |
| **Prasyarat** | Algoritma dan Pemrograman (INF-101/102) |
| **Ko-requisite** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Platform** | GitHub Codespaces, GitHub, LMS UAI |
| **Bahasa Pemrograman** | Python 3.x + JavaScript/TypeScript |
| **Durasi per Minggu** | 150 menit (3 × 50 menit) |
| **Metode Pembelajaran** | Ceramah interaktif, diskusi, studi kasus, praktik, proyek tim |

---

## B. Deskripsi Mata Kuliah

Mata kuliah Rekayasa Perangkat Lunak (RPL) membekali mahasiswa dengan pemahaman komprehensif tentang proses pengembangan perangkat lunak secara profesional dan sistematis. Kurikulum ini mencakup seluruh Software Development Life Cycle (SDLC) — dari requirements engineering, desain arsitektur, software construction, testing, hingga deployment dan maintenance — dengan pendekatan Agile/Scrum sebagai metodologi utama. Mata kuliah ini mengacu pada **SWEBOK v4 (2024)** sebagai framework referensi dan mengintegrasikan AI tools (GitHub Copilot, Claude Code, Cursor) sebagai coding partner sepanjang semester.

Dirancang menggunakan pendekatan **Outcome-Based Education (OBE)** sesuai standar SN-Dikti/KKNI Level 6, mata kuliah ini mempersiapkan mahasiswa untuk berperan sebagai software engineer yang kompeten, beretika, dan siap menghadapi tantangan industri software Indonesia yang terus berkembang. Proyek akhir berupa pengembangan web application secara tim menggunakan Agile/Scrum, dari requirements hingga deployment, memberikan pengalaman nyata proses rekayasa perangkat lunak end-to-end.

---

## C. CPL (Capaian Pembelajaran Lulusan)

| Kode | Deskripsi | Bloom's |
|------|-----------|---------|
| CPL-S2 | Menunjukkan sikap bertanggung jawab atas pekerjaan di bidang keahliannya secara mandiri, berdasarkan etika profesi dan nilai-nilai Islami | A3 |
| CPL-KU2 | Mampu menunjukkan kinerja mandiri, bermutu, dan terukur | C3 |
| CPL-KK1 | Mampu membangun aplikasi/sistem perangkat lunak dengan menerapkan prinsip-prinsip rekayasa perangkat lunak | C5 |
| CPL-KK4 | Mampu merancang, mengimplementasikan, dan menguji komponen perangkat lunak sesuai spesifikasi yang diberikan | C5 |
| CPL-P2 | Mampu mengambil keputusan secara tepat dalam konteks penyelesaian masalah berbasis data dan informasi | C4 |
| CPL-P3 | Mampu bekerja sama dalam tim serta berkomunikasi secara efektif baik lisan maupun tulisan | A4 |

---

## D. CPMK (Capaian Pembelajaran Mata Kuliah)

| Kode | Deskripsi | Bloom's | CPL Terkait | Bab Buku Ajar |
|------|-----------|---------|-------------|---------------|
| **CPMK-1** | Menjelaskan konsep dasar rekayasa perangkat lunak, model proses pengembangan (SDLC), prinsip-prinsip SWEBOK v4, serta etika profesi insinyur perangkat lunak berdasarkan nilai-nilai Islami | C2 (Memahami) | CPL-S2, CPL-P2 | Bab 1, 2 |
| **CPMK-2** | Menerapkan teknik requirements engineering (elicitation, analysis, specification, validation) untuk menghasilkan dokumen kebutuhan perangkat lunak yang lengkap dan terstruktur | C3 (Menerapkan) | CPL-KK1, CPL-P2 | Bab 3, 4 |
| **CPMK-3** | Menganalisis dan merancang arsitektur perangkat lunak menggunakan architectural patterns, design patterns, UML, dan prinsip desain yang baik (SOLID, DRY, KISS) | C3-C4 (Menerapkan-Menganalisis) | CPL-KK1, CPL-KK4 | Bab 5, 6 |
| **CPMK-4** | Mengimplementasikan perangkat lunak dengan mengikuti coding standards, menerapkan version control (Git), melakukan code review, dan berkolaborasi dalam tim menggunakan metodologi Agile/Scrum | C3-C4 (Menerapkan-Menganalisis) | CPL-KK4, CPL-P3 | Bab 7, 12 |
| **CPMK-5** | Merancang dan melaksanakan strategi pengujian perangkat lunak yang komprehensif (unit, integration, E2E) serta menerapkan quality assurance practices termasuk TDD dan AI-assisted testing | C4-C5 (Menganalisis-Mengevaluasi) | CPL-KK4, CPL-P3 | Bab 8, 9 |
| **CPMK-6** | Menerapkan praktik DevOps, CI/CD pipeline (GitHub Actions), containerization (Docker), cloud deployment, serta memahami software maintenance dan evolusi | C4-C5 (Menganalisis-Mengevaluasi) | CPL-KU2, CPL-KK4 | Bab 10, 11 |
| **CPMK-7** | Merancang dan membangun web application secara end-to-end dalam tim dengan metodologi Agile/Scrum, memanfaatkan AI sebagai co-developer secara bertanggung jawab, dari requirements hingga deployment | C5-C6 (Mengevaluasi-Mencipta) | CPL-KU2, CPL-KK4, CPL-P3 | Bab 13, 14 |

---

## E. Sub-CPMK

| Minggu | Kode | Deskripsi Sub-CPMK | Bloom's | CPMK |
|--------|------|---------------------|---------|------|
| 1 | Sub-CPMK-1.1 | Menjelaskan definisi, sejarah, dan prinsip-prinsip dasar rekayasa perangkat lunak serta perbedaan SE vs programming | C2 | CPMK-1 |
| 1 | Sub-CPMK-1.2 | Menjelaskan 15 Knowledge Areas SWEBOK v4 dan etika profesi software engineer | C2 | CPMK-1 |
| 2 | Sub-CPMK-1.3 | Membedakan model proses pengembangan (Waterfall, Agile, Kanban, XP, DevOps) dan memilih model yang sesuai untuk konteks tertentu | C2 | CPMK-1 |
| 2 | Sub-CPMK-1.4 | Menjelaskan framework Scrum (roles, events, artifacts) dan prinsip Agile Manifesto | C2 | CPMK-1 |
| 3 | Sub-CPMK-2.1 | Menerapkan teknik elicitation (interview, observation, prototyping) untuk mengumpulkan kebutuhan perangkat lunak | C3 | CPMK-2 |
| 3 | Sub-CPMK-2.2 | Menyusun dokumen Software Requirements Specification (SRS) sesuai standar IEEE 830/ISO 29148 | C3 | CPMK-2 |
| 4 | Sub-CPMK-2.3 | Membuat Use Case Diagram dan Use Case Narrative untuk memodelkan requirements | C3 | CPMK-2 |
| 4 | Sub-CPMK-2.4 | Menulis User Stories dengan kriteria INVEST dan Acceptance Criteria format Given-When-Then | C3 | CPMK-2 |
| 5 | Sub-CPMK-3.1 | Menganalisis dan memilih arsitektur perangkat lunak (MVC, layered, microservices) berdasarkan quality attributes | C4 | CPMK-3 |
| 5 | Sub-CPMK-3.2 | Menerapkan prinsip SOLID dan design patterns (Singleton, Factory, Observer, Strategy) dalam desain | C3 | CPMK-3 |
| 6 | Sub-CPMK-3.3 | Membuat diagram UML (Class, Sequence, Activity, State) menggunakan PlantUML/Mermaid | C3 | CPMK-3 |
| 6 | Sub-CPMK-3.4 | Merancang database (ERD, normalization) dan REST API design | C3 | CPMK-3 |
| 7 | Sub-CPMK-4.1 | Menerapkan coding standards (PEP 8, ESLint), mengidentifikasi code smells, dan melakukan refactoring | C3 | CPMK-4 |
| 7 | Sub-CPMK-4.2 | Menerapkan Git workflow (branching, PR, code review) untuk kolaborasi tim | C3 | CPMK-4 |
| 9 | Sub-CPMK-5.1 | Merancang test cases menggunakan teknik equivalence partitioning dan boundary value analysis | C4 | CPMK-5 |
| 9 | Sub-CPMK-5.2 | Mengimplementasikan unit test dan integration test menggunakan pytest (Python) dan Jest (JavaScript) | C3 | CPMK-5 |
| 10 | Sub-CPMK-5.3 | Menerapkan Test-Driven Development (TDD) dan AI-assisted testing | C4 | CPMK-5 |
| 10 | Sub-CPMK-5.4 | Mengevaluasi kualitas perangkat lunak menggunakan metrics (code coverage, cyclomatic complexity) | C5 | CPMK-5 |
| 11 | Sub-CPMK-6.1 | Membangun CI/CD pipeline menggunakan GitHub Actions untuk otomatisasi build, test, dan deploy | C3 | CPMK-6 |
| 11 | Sub-CPMK-6.2 | Menerapkan containerization dengan Docker (Dockerfile, docker-compose) dan cloud deployment | C3 | CPMK-6 |
| 12 | Sub-CPMK-6.3 | Menganalisis technical debt dan menerapkan strategi refactoring yang aman | C4 | CPMK-6 |
| 12 | Sub-CPMK-6.4 | Menerapkan semantic versioning (SemVer) dan dependency management | C3 | CPMK-6 |
| 13 | Sub-CPMK-7.1 | Memanfaatkan AI tools (Copilot, Claude Code, Cursor) untuk setiap fase SDLC secara bertanggung jawab | C5 | CPMK-7 |
| 13 | Sub-CPMK-7.2 | Menerapkan prompt engineering (CRIDE framework) untuk software engineering tasks | C3 | CPMK-7 |
| 14 | Sub-CPMK-7.3 | Mengevaluasi tren modern SE (supply chain security, green software, platform engineering) | C5 | CPMK-7 |
| 14 | Sub-CPMK-7.4 | Merancang roadmap pengembangan karir sebagai software engineer | C6 | CPMK-7 |

---

## F. Tabel Rencana Pembelajaran Semester

| Minggu | Sub-CPMK | Materi Pembelajaran | Metode/Strategi | Pengalaman Belajar | Indikator Penilaian | Bobot | Referensi |
|--------|----------|--------------------|-----------------|--------------------|---------------------|-------|-----------|
| 1 | 1.1, 1.2 | Pengantar RPL: Definisi, sejarah (NATO 1968), software crisis, SWEBOK v4 (15 KA), SE vs programming, etika profesi, warisan Al-Khwarizmi | Ceramah interaktif, diskusi kelompok, video | Menyimak presentasi, diskusi tentang pentingnya SE di era AI, refleksi etika | Mampu menjelaskan minimal 5 prinsip dasar RPL dan 10 Knowledge Areas SWEBOK | — | [1][2][3] |
| 2 | 1.3, 1.4 | Proses & Model Pengembangan: Waterfall, V-Model, Iterative, Spiral, Agile Manifesto, Scrum, Kanban, XP, DevOps | Ceramah, simulasi Scrum mini, studi kasus | Simulasi sprint planning mini, diskusi pemilihan model, analisis studi kasus Indonesia | Mampu membedakan minimal 5 model dan memilih model yang sesuai untuk skenario | — | [1][2][4] |
| 3 | 2.1, 2.2 | Requirements Engineering: Elicitation (interview, observation, prototyping), functional vs non-functional, SRS (IEEE 830), validation | Ceramah, role-play elicitation, praktik menulis SRS | Role-play interview stakeholder, menulis SRS untuk sistem perpustakaan kampus | SRS yang memenuhi standar IEEE 830 dengan minimal 10 functional requirements | T1 (2.5%) | [1][5] |
| 4 | 2.3, 2.4 | Pemodelan Requirements: Use Case Diagram & Narrative, User Stories (INVEST), Acceptance Criteria (Given-When-Then), Product Backlog, MoSCoW | Workshop user story, backlog prioritization | Membuat use case diagram, menulis user stories, memprioritaskan backlog | Minimal 15 user stories memenuhi INVEST dengan acceptance criteria | T2 (2.5%), K1 (4%) | [1][4][5] |
| 5 | 3.1, 3.2 | Arsitektur Perangkat Lunak: Architectural styles (MVC, layered, microservices, event-driven), quality attributes, SOLID, design patterns (Singleton, Factory, Observer, Strategy) | Ceramah, analisis arsitektur aplikasi nyata | Menganalisis arsitektur real-world app, implementasi design patterns di Python | Mampu merancang arsitektur dengan ADR dan mengimplementasikan 2+ design patterns | — | [1][6][7] |
| 6 | 3.3, 3.4 | Desain: UML (Class, Sequence, Activity, State), database design (ERD, normalization), API design (REST) | Ceramah, hands-on UML modeling | Membuat UML diagrams dengan PlantUML/Mermaid, merancang ERD dan REST API | 4 jenis UML diagram yang benar untuk proyek web app | T3 (2.5%) | [1][6][8] |
| 7 | 4.1, 4.2 | Software Construction: Clean code, PEP 8, ESLint, code smells, refactoring, Git workflow (branching, PR, code review) | Live coding, pair programming, code review workshop | Identifikasi code smells, refactoring, membuat PR dan melakukan code review | Mampu mengidentifikasi 5+ code smells dan melakukan code review konstruktif | K2 (3%) | [7][9] |
| 8 | — | **UTS**: Ujian Tengah Semester (Minggu 1-7) | Ujian tertulis | 100 menit, closed-book, tanpa AI | PG (30 poin) + Essay (30 poin) + Studi Kasus (40 poin) | UTS (20%) | — |
| 9 | 5.1, 5.2 | Software Testing: Testing levels (unit, integration, system, acceptance), test case design, TDD (Red-Green-Refactor), pytest, Jest | Live coding TDD, hands-on test writing | Menulis unit test dengan pytest dan Jest, menerapkan TDD workflow | Minimal 10 unit tests yang bermakna dengan coverage ≥ 70% | T4 (2.5%) | [1][10] |
| 10 | 5.3, 5.4 | Advanced Testing & QA: E2E testing (Playwright), performance testing, security testing (OWASP), AI-assisted testing, mutation testing, code coverage | Demo E2E test, AI-assisted test generation | Menulis E2E test, menggunakan AI untuk generate test cases, evaluasi kualitas | Mampu menerapkan E2E testing dan mengevaluasi kualitas dengan metrics | — | [1][10] |
| 11 | 6.1, 6.2 | DevOps & CI/CD: DevOps culture (CAMS), GitHub Actions (workflows, YAML), Docker (Dockerfile, docker-compose), cloud deployment (Vercel/Railway) | Live demo CI/CD, hands-on pipeline | Membangun CI/CD pipeline, Dockerize aplikasi, deploy ke cloud | CI/CD pipeline berjalan dengan minimal lint + test + deploy stages | T5 (2.5%) | [11][12] |
| 12 | 6.3, 6.4 | Maintenance & Evolution: Types of maintenance, technical debt, refactoring strategies, software metrics, SemVer, dependency management | Code analysis, refactoring workshop | Menganalisis technical debt, menerapkan refactoring, mengelola versi dan dependencies | Mampu mengidentifikasi dan memprioritaskan technical debt items | K3 (3%) | [1][13] |
| 13 | 7.1, 7.2 | AI-Augmented SE: AI tools (Copilot, Claude Code, Cursor), AI untuk setiap fase SDLC, agentic development, prompt engineering (CRIDE), responsible AI | Hands-on AI pair programming, AI code review | Menggunakan AI untuk requirements → code → test → review, mendokumentasikan AI usage | AI Usage Log yang komprehensif dengan minimal 5 contoh penggunaan AI | T6 (2.5%) | [14][15] |
| 14 | 7.3, 7.4 | Modern SE Trends: Software supply chain security (SBOM), green software, platform engineering, future of SE, career roadmap | Guest lecture simulation, industry trend analysis | Menganalisis tren terkini, merancang personal career roadmap SE | Presentasi analisis 2+ tren SE terkini dengan konteks Indonesia | — | [14][15] |
| 15 | 1-7 (all) | **Presentasi Proyek Akhir**: Demo web application, Q&A, peer review | Presentasi tim, demo live | Mempresentasikan proyek, menerima feedback, peer evaluation | Proyek berjalan, demo sukses, dokumentasi lengkap | Proyek (25%) | — |
| 16 | — | **UAS**: Ujian Akhir Semester (Komprehensif Minggu 1-15) | Ujian tertulis | 120 menit, closed-book + 1 lembar catatan A4 (tulisan tangan) | PG (30 poin) + Essay (30 poin) + Studi Kasus Komprehensif (40 poin) | UAS (25%) | — |

---

## G. Evaluasi dan Penilaian

### Komponen Penilaian

| Komponen | Bobot | Frekuensi | Sifat | CPMK yang Diuji |
|----------|-------|-----------|-------|------------------|
| Tugas Mingguan (T1-T6) | 15% | 6 tugas × 2.5% | Individu, take-home | CPMK 2-7 |
| Kuis (K1-K3) | 10% | K1: 4%, K2: 3%, K3: 3% | Individu, in-class | CPMK 1-6 |
| UTS | 20% | 1× (Minggu 8) | Individu, closed-book | CPMK 1-4 |
| Proyek Akhir | 25% | 1 proyek (Minggu 5-15) | Kelompok 3-4 orang | CPMK 1-7 |
| UAS | 25% | 1× (Minggu 16) | Individu, closed-book + catatan | CPMK 1-7 |
| Partisipasi & Etika AI | 5% | Sepanjang semester | Individu | — |
| **Total** | **100%** | | | |

### Skala Penilaian

| Huruf | Rentang | Bobot |
|-------|---------|-------|
| A | 85-100 | 4.00 |
| B+ | 77-84 | 3.50 |
| B | 70-76 | 3.00 |
| C+ | 63-69 | 2.50 |
| C | 55-62 | 2.00 |
| D | 45-54 | 1.00 |
| E | 0-44 | 0.00 |

### Matrix CPMK × Asesmen

| CPMK | T1-T6 | K1-K3 | UTS | Proyek | UAS | Partisipasi |
|------|-------|-------|-----|--------|-----|-------------|
| CPMK-1 | — | K1 | ✓ | ✓ | ✓ | ✓ |
| CPMK-2 | T1, T2 | K1 | ✓ | ✓ | ✓ | — |
| CPMK-3 | T3 | K2 | ✓ | ✓ | ✓ | — |
| CPMK-4 | — | K2 | ✓ | ✓ | ✓ | — |
| CPMK-5 | T4 | K3 | — | ✓ | ✓ | — |
| CPMK-6 | T5 | K3 | — | ✓ | ✓ | — |
| CPMK-7 | T6 | — | — | ✓ | ✓ | ✓ |

---

## H. Kebijakan Penggunaan AI

| Komponen | AI Policy | Ketentuan |
|----------|-----------|-----------|
| Tugas (T1-T6) | **Diizinkan + Documented** | Wajib mengisi AI Usage Log: prompt, output, modifikasi, refleksi |
| Kuis (K1-K3) | **TIDAK diizinkan** | Closed-book, tanpa akses AI/internet |
| UTS | **TIDAK diizinkan** | Closed-book, tanpa akses AI/internet |
| Proyek Akhir | **AI sebagai partner + Documented** | AI Usage Log wajib (10% rubrik proyek), verifikasi pemahaman via demo |
| UAS | **TIDAK diizinkan** | Closed-book + 1 lembar catatan A4 tulisan tangan, tanpa AI |
| Partisipasi | **N/A** | Kontribusi diskusi dan refleksi etika AI |

**Prinsip Utama:** AI adalah *coding partner*, bukan pengganti pemikiran kritis. Mahasiswa wajib memahami dan mampu menjelaskan setiap output AI yang digunakan.

---

## I. Profil Proyek Akhir

| Aspek | Detail |
|-------|--------|
| **Tipe** | Web Application |
| **Ukuran Tim** | 3-4 mahasiswa |
| **Metodologi** | Agile/Scrum (4 Sprint) |
| **Tech Stack** | Flask (backend), HTML/CSS/JS (frontend), SQLite, Docker, GitHub Actions |
| **Platform** | GitHub Codespaces → Deploy ke Vercel/Railway |
| **Timeline** | Sprint 0 (W5-6) → Sprint 1 (W7-9) → Sprint 2 (W10-11) → Sprint 3 (W12-13) → Sprint 4 (W14) → Demo (W15) |
| **Deliverables** | GitHub repo, SRS, UML diagrams, working app, test suite, CI/CD pipeline, demo, AI Usage Log, retrospective |
| **Konteks** | Wajib menggunakan konteks Indonesia (UMKM, layanan publik, pendidikan, dll.) |

---

## J. Referensi

1. Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson.
2. IEEE Computer Society. (2024). *Guide to the Software Engineering Body of Knowledge (SWEBOK) v4*. IEEE.
3. Pressman, R. S., & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill.
4. Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide*. Scrum.org.
5. Wiegers, K. E., & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press.
6. Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
7. Martin, R. C. (2009). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.
8. Fowler, M. (2003). *UML Distilled* (3rd ed.). Addison-Wesley.
9. Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley.
10. Humble, J., & Farley, D. (2010). *Continuous Delivery*. Addison-Wesley.
11. Kim, G., Humble, J., Debois, P., & Willis, J. (2016). *The DevOps Handbook*. IT Revolution Press.
12. Docker Documentation. (2025). https://docs.docker.com/
13. GitHub Actions Documentation. (2025). https://docs.github.com/en/actions
14. Hunt, A., & Thomas, D. (2019). *The Pragmatic Programmer* (20th Anniversary ed.). Addison-Wesley.
15. ACM/IEEE. (2015). *Software Engineering 2014: Curriculum Guidelines*. ACM/IEEE.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
