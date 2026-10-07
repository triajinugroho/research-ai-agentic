# Minggu 16: UAS -- Review dan Ujian Akhir Semester

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 16 dari 16 |
| **Topik** | UAS -- Review dan Ujian Akhir Semester |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK 1-7: Seluruh capaian pembelajaran semester |
| **Sub-CPMK** | Sub-CPMK-16.1: Mengintegrasikan seluruh konsep RPL dalam pemecahan masalah komprehensif (C2-C6) |
| **Durasi** | 150 menit (3 x 50 menit) |
| **Metode** | Review session, Q&A, practice problems, ujian tertulis |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Mengintegrasikan** seluruh konsep RPL (Minggu 1-15) dalam menjawab soal komprehensif (C6)
2. **Menganalisis** studi kasus SE end-to-end dari requirements hingga maintenance (C4)
3. **Mengevaluasi** pilihan teknis dan proses yang tepat untuk berbagai skenario proyek (C5)

---

## Materi Pembelajaran

### 16.1 Peta Materi Semester -- Review Komprehensif

```
Peta Konsep Semester IF2205 -- Rekayasa Perangkat Lunak:

Fase 1: FONDASI RPL (Minggu 1-4)
+-- Minggu 1: Pengantar RPL
|   +-- Definisi SE vs Programming
|   +-- SWEBOK v4 (15 Knowledge Areas)
|   +-- Software Crisis, Etika IEEE/ACM
|   +-- Warisan Al-Khwarizmi
|
+-- Minggu 2: Proses & Model
|   +-- Waterfall, V-Model, Spiral
|   +-- Agile Manifesto (4 values, 12 principles)
|   +-- Scrum (roles, events, artifacts)
|   +-- Kanban, XP, DevOps
|
+-- Minggu 3: Requirements Engineering
|   +-- Elicitation (interview, observation, prototyping)
|   +-- Functional vs Non-Functional Requirements
|   +-- SRS (IEEE 830 / ISO 29148)
|   +-- Requirements Validation
|
+-- Minggu 4: Pemodelan Requirements
    +-- Use Case Diagram & Narrative
    +-- User Stories (INVEST criteria)
    +-- Acceptance Criteria (Given-When-Then)
    +-- Product Backlog, MoSCoW prioritization

Fase 2: DESIGN & CONSTRUCTION (Minggu 5-7)
+-- Minggu 5: Arsitektur Perangkat Lunak
|   +-- Architectural Styles: MVC, Layered, Microservices
|   +-- Quality Attributes (Performance, Security, etc.)
|   +-- SOLID Principles
|   +-- Design Patterns: Singleton, Factory, Observer, Strategy
|
+-- Minggu 6: Desain & UML
|   +-- UML: Class, Sequence, Activity, State Diagram
|   +-- Database Design: ERD, Normalization
|   +-- REST API Design
|
+-- Minggu 7: Software Construction
    +-- Clean Code (PEP 8, ESLint)
    +-- Code Smells & Refactoring
    +-- Git Workflow (branching, PR, code review)
    +-- Conventional Commits

--- Minggu 8: UTS ---

Fase 3: QUALITY & OPERATIONS (Minggu 9-12)
+-- Minggu 9: Software Testing
|   +-- Testing Levels: Unit, Integration, System, Acceptance
|   +-- Test Case Design: EP, BVA, Decision Table
|   +-- TDD (Red-Green-Refactor)
|   +-- pytest (Python), Jest (JavaScript)
|
+-- Minggu 10: Advanced Testing & QA
|   +-- E2E Testing (Playwright)
|   +-- Performance, Security Testing (OWASP)
|   +-- QA vs QC, Quality Metrics
|   +-- Code Coverage, Cyclomatic Complexity
|
+-- Minggu 11: DevOps & CI/CD
|   +-- DevOps Culture (CAMS), DORA Metrics
|   +-- CI vs CD (Delivery) vs CD (Deployment)
|   +-- GitHub Actions (YAML workflow)
|   +-- Docker (Dockerfile, docker-compose)
|   +-- Cloud Deployment, Deployment Strategies
|
+-- Minggu 12: Maintenance & Evolution
    +-- 4 Types of Maintenance
    +-- Lehman's Laws
    +-- Technical Debt (Quadrant, Strategies)
    +-- Refactoring Techniques
    +-- SemVer, Dependency Management, SBOM

Fase 4: MODERN SE (Minggu 13-15)
+-- Minggu 13: AI-Augmented SE
|   +-- AI Tools: Copilot, Claude Code, Cursor
|   +-- AI di setiap fase SDLC
|   +-- CRIDE Framework (Prompt Engineering)
|   +-- Agentic Development
|   +-- Responsible AI, AI Usage Log
|
+-- Minggu 14: Modern Trends
|   +-- Supply Chain Security (SBOM, SCA, Dependabot)
|   +-- Green Software Engineering
|   +-- Platform Engineering, Developer Experience
|   +-- Karir SE di Indonesia, Sertifikasi
|
+-- Minggu 15: Presentasi Proyek Akhir
    +-- Demo Day, Peer Review
```

### 16.2 Konsep Kunci per CPMK

| CPMK | Konsep Kunci yang Harus Dikuasai | Minggu |
|------|----------------------------------|--------|
| **CPMK-1** | Definisi SE, SWEBOK v4 KA, model proses (Waterfall vs Agile), Scrum framework | 1-2 |
| **CPMK-2** | Elicitation techniques, SRS IEEE 830, user stories INVEST, acceptance criteria | 3-4 |
| **CPMK-3** | SOLID, design patterns, UML diagrams, ERD, REST API | 5-6 |
| **CPMK-4** | Clean code, code smells, Git workflow, code review | 7 |
| **CPMK-5** | Testing levels, TDD, pytest/Jest, code coverage, QA vs QC | 9-10 |
| **CPMK-6** | DevOps CAMS, CI/CD, GitHub Actions, Docker, SemVer, tech debt | 11-12 |
| **CPMK-7** | AI tools, CRIDE, supply chain security, green software, karir SE | 13-14 |

### 16.3 Format UAS

| Komponen | Detail |
|----------|--------|
| **Durasi** | 120 menit |
| **Sifat** | *Closed-book* + **1 lembar catatan** (A4, bolak-balik, tulis tangan) |
| **Cakupan** | Minggu 1-15 (penekanan pada Minggu 9-14) |
| **AI Tools** | **TIDAK diperbolehkan** |
| **Bobot** | 25% dari nilai akhir |

```
Struktur Soal UAS:
+--------+--------------------------+--------+-------+
| Bagian | Tipe Soal                | Jumlah | Bobot |
+--------+--------------------------+--------+-------+
| A      | Pilihan Ganda            | 15     | 30%   |
|        | (semua CPMK)             |        |       |
+--------+--------------------------+--------+-------+
| B      | Jawaban Singkat & Diagram| 5      | 30%   |
|        | (UML, arsitektur, YAML)  |        |       |
+--------+--------------------------+--------+-------+
| C      | Studi Kasus Komprehensif | 2      | 40%   |
|        | (end-to-end SE scenario) |        |       |
+--------+--------------------------+--------+-------+

Distribusi soal per CPMK:
CPMK-1 (Fondasi):    2 PG + 1 essay
CPMK-2 (Req):        2 PG + bagian studi kasus
CPMK-3 (Design):     2 PG + 1 diagram
CPMK-4 (Code):       1 PG + bagian studi kasus
CPMK-5 (Testing):    3 PG + 1 essay
CPMK-6 (DevOps):     3 PG + 1 essay
CPMK-7 (AI/Modern):  2 PG + 1 essay
```

### 16.4 Tips Persiapan UAS

#### 1. Buat Lembar Catatan yang Efektif

```
Template Lembar Catatan A4 (Bolak-Balik):

HALAMAN DEPAN:
+--Left Column--+--Right Column--+
| Definisi:     | Diagram:       |
| - SE vs Prog  | - Testing      |
| - SWEBOK KA   |   Pyramid     |
| - SOLID       | - DevOps Cycle |
| - DRY, KISS   | - TDD Cycle   |
|               | - CI/CD Flow   |
| Model Proses: |                |
| - Waterfall   | Perbandingan:  |
| - Agile       | - QA vs QC    |
|   (4 values)  | - CI vs CD    |
| - Scrum       | - Coupling vs |
|   (roles,     |   Cohesion    |
|   events)     |                |
+---------------+----------------+

HALAMAN BELAKANG:
+--Left Column--+--Right Column--+
| Rumus/Format: | Studi Kasus:   |
| - SemVer:     | - Langkah      |
|   MAJOR.MINOR |   menjawab:    |
|   .PATCH      |   1. Model     |
| - CC =        |   2. User Story|
|   decisions+1 |   3. Arsitektur|
| - INVEST:     |   4. Testing   |
|   I,N,V,E,S,T |   5. CI/CD    |
|               |   6. AI Usage  |
| Design Pattern| - Contoh       |
| - Singleton   |   skenario     |
| - Factory     |   Indonesia    |
| - Observer    |                |
| - Strategy    | CRIDE:         |
|               | C-R-I-D-E      |
+---------------+----------------+
```

#### 2. Strategi Menjawab Soal

| Tipe Soal | Strategi | Alokasi Waktu |
|-----------|----------|---------------|
| **PG (15 soal)** | Kerjakan cepat, tandai yang ragu | 25 menit |
| **Jawaban Singkat (5 soal)** | Jawab to-the-point, gunakan diagram jika diminta | 35 menit |
| **Studi Kasus (2 soal)** | Jawab terstruktur: analisis -> keputusan -> justifikasi | 55 menit |
| **Review** | Cek ulang jawaban yang ditandai | 5 menit |

### 16.5 Contoh Soal Latihan

#### Bagian A -- Pilihan Ganda (Contoh)

**Soal 1 (CPMK-1):**
Manakah yang BUKAN termasuk prinsip SOLID?
a) Single Responsibility Principle
b) Open-Closed Principle
c) Liskov Substitution Principle
d) **Dependency Injection** (jawaban: yang benar adalah Dependency *Inversion*)

**Soal 2 (CPMK-5):**
Dalam testing pyramid, jenis test mana yang jumlahnya paling banyak dan paling cepat dijalankan?
a) E2E test
b) Integration test
c) **Unit test** (jawaban)
d) Manual test

**Soal 3 (CPMK-6):**
Apa perbedaan utama antara Continuous Delivery dan Continuous Deployment?
a) CD Delivery tidak memerlukan testing
b) **CD Deployment tidak memerlukan manual approval untuk production** (jawaban)
c) CD Delivery tidak mendeploy ke staging
d) CD Deployment hanya untuk microservices

**Soal 4 (CPMK-7):**
Dalam framework CRIDE untuk prompt engineering, elemen "D" merujuk pada:
a) Documentation
b) Design
c) **Details** (jawaban)
d) Deployment

#### Bagian B -- Jawaban Singkat (Contoh)

**Soal 5 (CPMK-3):**
Gambarkan Class Diagram sederhana (minimal 3 class dengan relasi) untuk sistem pemesanan makanan online. Sertakan atribut dan method utama.

**Soal 6 (CPMK-6):**
Jelaskan perbedaan antara Docker image dan Docker container. Berikan analogi yang tepat.

**Soal 7 (CPMK-5):**
Tulis 3 test case menggunakan teknik Boundary Value Analysis untuk fungsi `validate_age(umur)` yang menerima umur 17-65 tahun.

#### Bagian C -- Studi Kasus (Contoh)

**Soal 8 (CPMK 1-7, bobot 20%):**

> Sebuah koperasi di Yogyakarta ingin membangun aplikasi manajemen simpan pinjam digital. Tim terdiri dari 4 developer mahasiswa + 1 designer. Deadline: 3 bulan. Pengguna target: 500 anggota koperasi.

a) **Model Proses** (4 poin): Rekomendasikan model proses yang tepat dan jelaskan alasannya. Jika memilih Scrum, tentukan panjang sprint dan jelaskan pembagian peran.

b) **Requirements** (4 poin): Tuliskan 3 user stories utama dengan format "Sebagai [role], saya ingin [aksi], sehingga [manfaat]" lengkap dengan acceptance criteria (Given-When-Then).

c) **Arsitektur** (4 poin): Gambarkan arsitektur high-level (backend, frontend, database). Pilih architectural pattern dan jelaskan alasannya.

d) **Testing** (4 poin): Rancang strategi testing: level mana yang diprioritaskan? Berapa target coverage? Berikan contoh 2 unit test case untuk fitur simpanan.

e) **AI & Ethics** (4 poin): Jelaskan bagaimana AI tools dapat membantu tim ini secara bertanggung jawab di 2 fase SDLC. Bagaimana prinsip amanah dan transparansi diterapkan dalam penggunaan AI?

### 16.6 Panduan Menilai Sendiri (Self-Assessment)

```
Checklist Kesiapan UAS:
+-- CPMK-1: Bisa jelaskan SE vs Programming?           [Y/N]
+-- CPMK-1: Tahu minimal 5 SWEBOK KA?                  [Y/N]
+-- CPMK-1: Bisa bedakan Waterfall, Agile, Scrum?      [Y/N]
+-- CPMK-2: Bisa tulis user story INVEST?               [Y/N]
+-- CPMK-2: Bisa tulis acceptance criteria GWT?         [Y/N]
+-- CPMK-3: Bisa gambar Class Diagram sederhana?        [Y/N]
+-- CPMK-3: Bisa jelaskan SOLID principles?             [Y/N]
+-- CPMK-4: Bisa identifikasi code smells?              [Y/N]
+-- CPMK-5: Bisa jelaskan TDD cycle?                    [Y/N]
+-- CPMK-5: Bisa tulis unit test dengan pytest?         [Y/N]
+-- CPMK-6: Bisa jelaskan CI vs CD?                     [Y/N]
+-- CPMK-6: Bisa baca/tulis GitHub Actions YAML?        [Y/N]
+-- CPMK-6: Bisa jelaskan Dockerfile layer?             [Y/N]
+-- CPMK-6: Tahu SemVer dan deployment strategies?      [Y/N]
+-- CPMK-7: Bisa tulis prompt CRIDE?                    [Y/N]
+-- CPMK-7: Bisa jelaskan responsible AI usage?         [Y/N]

Jika ada [N], review materi terkait sebelum UAS!
```

---

## Kegiatan Pembelajaran

### Pre-class (20 menit)

- Review catatan dan modul Minggu 1-15
- Siapkan 1 lembar catatan UAS (A4, bolak-balik, **tulis tangan** -- bukan print)
- Tulis 3 pertanyaan yang masih membingungkan untuk ditanyakan di sesi review
- Isi self-assessment checklist di atas -- fokuskan review pada topik yang masih lemah

### In-class (110 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-35 menit | Review komprehensif: peta konsep semester, walk-through per CPMK | Review + Q&A |
| 35-55 menit | Bahas contoh soal dan strategi menjawab (PG, essay, studi kasus) | Latihan + diskusi |
| 55-60 menit | *Break* -- persiapan ujian | -- |
| 60-110 menit | **Ujian Akhir Semester (UAS)** -- 50 menit in-class (atau dijadwalkan terpisah 120 menit sesuai jadwal UAS universitas) | Ujian tertulis |

**Catatan:** Jika UAS dijadwalkan terpisah oleh universitas (bukan di jam kuliah), maka 60-110 menit digunakan untuk review lanjutan dan latihan soal tambahan.

### Post-class (20 menit)

- Refleksi semester: apa konsep paling berharga yang dipelajari di IF2205?
- Lanjutkan pengembangan proyek akhir sebagai portfolio di GitHub (opsional)
- Gunakan skill SE yang dipelajari untuk proyek-proyek di semester berikutnya
- Pertimbangkan kontribusi ke open-source sebagai langkah awal karir SE

---

## Referensi

1. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach*, 9th ed. McGraw-Hill.
2. Sommerville, I. (2016). *Software Engineering*, 10th ed. Pearson.
3. IEEE Computer Society. (2024). *Guide to the Software Engineering Body of Knowledge (SWEBOK) v4*. IEEE.
4. Schwaber, K. & Sutherland, J. (2020). *The Scrum Guide*. Scrum.org.
5. Fowler, M. (2019). *Refactoring*, 2nd ed. Addison-Wesley.
6. Seluruh modul Minggu 1-15 mata kuliah Rekayasa Perangkat Lunak IF2205.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
