# BUKU AJAR

# REKAYASA PERANGKAT LUNAK
## Proses, Desain, dan Praktik Modern dengan AI

---

### Untuk Mahasiswa Program Studi Informatika

---

**Penulis:**
# Tri Aji Nugroho, S.T., M.T.

---

**Program Studi Informatika**
**Fakultas Sains dan Teknologi**
**Universitas Al Azhar Indonesia**
**Jakarta, 2026**

---

### Identitas Buku

| Komponen | Detail |
|----------|--------|
| **Judul** | Rekayasa Perangkat Lunak: Proses, Desain, dan Praktik Modern dengan AI |
| **Penulis** | Tri Aji Nugroho, S.T., M.T. |
| **Institusi** | Universitas Al Azhar Indonesia |
| **Fakultas** | Sains dan Teknologi |
| **Program Studi** | Informatika |
| **Edisi** | Pertama, 2026 |
| **Jumlah Bab** | 14 Bab + Lampiran |
| **Sasaran Pembaca** | Mahasiswa S1 Informatika Semester 4 |
| **Pendekatan** | Outcome-Based Education (OBE), AI-Augmented |
| **Bahasa Pemrograman** | Python 3.x + JavaScript/TypeScript |
| **Platform** | GitHub Codespaces |

---

### Kata Pengantar

بسم الله الرحمن الرحيم

**Assalamu'alaikum Warahmatullahi Wabarakatuh**

Segala puji bagi Allah SWT yang telah memberikan nikmat ilmu dan kemudahan dalam menyusun buku ajar ini. Shalawat serta salam senantiasa tercurahkan kepada Nabi Muhammad SAW, teladan terbaik dalam menuntut ilmu dan mengamalkannya.

Buku ajar **"Rekayasa Perangkat Lunak: Proses, Desain, dan Praktik Modern dengan AI"** ini disusun sebagai panduan utama mata kuliah Rekayasa Perangkat Lunak untuk mahasiswa Program Studi Informatika, Universitas Al Azhar Indonesia. Buku ini hadir di tengah transformasi besar dalam industri pengembangan perangkat lunak — di mana **AI telah mengubah cara software dibangun, diuji, dan dipelihara**, sementara prinsip-prinsip fundamental rekayasa perangkat lunak tetap menjadi fondasi yang tak tergantikan. Memahami kedua sisi ini — fondasi yang kokoh dan praktik modern yang relevan — adalah kebutuhan mutlak bagi setiap calon software engineer.

Di era di mana GitHub Copilot, Claude Code, dan Cursor telah menjadi bagian dari workflow pengembang profesional, mahasiswa informatika tidak cukup hanya belajar menulis kode. Mereka harus memahami **seluruh siklus hidup perangkat lunak** (*Software Development Life Cycle*) — mulai dari menggali kebutuhan pengguna, merancang arsitektur yang kokoh, membangun kode yang bersih, menguji secara menyeluruh, hingga men-*deploy* dan memelihara sistem di lingkungan produksi. Namun, mayoritas buku rekayasa perangkat lunak berkualitas ditulis dalam bahasa Inggris dengan konteks perusahaan teknologi Barat, menciptakan kesenjangan yang signifikan bagi mahasiswa Indonesia.

Berbeda dari buku RPL konvensional, buku ajar ini dirancang dengan beberapa kekhususan. Pertama, **pendekatan full SDLC end-to-end** — setiap fase pengembangan perangkat lunak tidak hanya dijelaskan secara teori, tetapi langsung dipraktikkan dengan Python dan JavaScript di GitHub Codespaces. Kedua, **AI sebagai co-developer** — buku ini mengajarkan cara menggunakan AI tools (Copilot, Claude Code, Cursor) sebagai mitra pengembangan secara produktif dan bertanggung jawab di setiap tahap SDLC. Ketiga, **konteks Indonesia** — seluruh studi kasus dan proyek menggunakan skenario Indonesia (sistem UMKM, layanan publik, aplikasi kampus), sehingga mahasiswa langsung merasakan relevansi rekayasa perangkat lunak dengan permasalahan nyata di sekitar mereka.

Buku ini terdiri dari **14 bab** yang disusun secara progresif — dari fondasi rekayasa perangkat lunak hingga proyek akhir membangun web application end-to-end dalam tim Agile/Scrum. Setiap bab dilengkapi dengan tujuan pembelajaran yang jelas, penjelasan teori dengan bahasa yang mudah dipahami, contoh kode yang siap dijalankan, studi kasus berbasis konteks Indonesia, latihan soal bertingkat (dasar, menengah, mahir), dan "AI Corner" — panduan interaksi dengan AI untuk topik tersebut. Semoga buku ajar ini bermanfaat bagi mahasiswa, rekan dosen, dan siapa pun yang ingin mempelajari rekayasa perangkat lunak dengan pendekatan yang komprehensif, modern, dan beretika.

**Wassalamu'alaikum Warahmatullahi Wabarakatuh**

Jakarta, Februari 2026

**Tri Aji Nugroho, S.T., M.T.**
Dosen Pengampu Mata Kuliah Rekayasa Perangkat Lunak
Program Studi Informatika
Universitas Al Azhar Indonesia

---

### Prakata — Cara Menggunakan Buku Ini

Buku ini dirancang sebagai panduan utama mata kuliah **Rekayasa Perangkat Lunak (IF2205, 3 SKS)** di Program Studi Informatika, Universitas Al Azhar Indonesia. Pendekatan pedagogis yang digunakan adalah **Outcome-Based Education (OBE)** — setiap bab, latihan, dan asesmen dirancang untuk mencapai Capaian Pembelajaran Mata Kuliah (CPMK) yang terukur berdasarkan taksonomi Bloom (C2–C6).

**Pendekatan AI-Augmented Learning**

Buku ini mengintegrasikan penggunaan AI secara progresif melalui fitur **"AI Corner"** di setiap bab. Mahasiswa tidak sekadar belajar *tentang* rekayasa perangkat lunak — mereka belajar *dengan bantuan* AI sebagai mitra kerja, sebagaimana praktik di industri modern. Tingkat literasi AI dibangun secara bertahap: dari penggunaan dasar (prompt sederhana untuk memahami konsep) di bab-bab awal, hingga penggunaan mahir (AI-augmented development workflow untuk membangun web app end-to-end) di bab-bab akhir.

**Untuk Mahasiswa:**
1. Baca setiap bab secara berurutan sebelum perkuliahan (*flipped classroom*)
2. Jalankan semua kode di GitHub Codespaces — baik Python maupun JavaScript
3. Kerjakan latihan soal di akhir bab secara mandiri sebelum melihat pembahasan
4. Gunakan "AI Corner" sebagai panduan untuk berinteraksi dengan AI secara bertanggung jawab
5. Isi **AI Usage Log** setiap kali menggunakan AI tools untuk tugas dan proyek
6. Catat pertanyaan dan diskusikan di kelas atau di forum GitHub Discussions

**Untuk Dosen:**
1. Buku ini dirancang untuk 16 minggu perkuliahan (3 SKS), termasuk UTS, proyek akhir, dan UAS
2. Setiap bab dapat diselesaikan dalam 1–2 pertemuan; Bab 14 (Proyek Akhir) berjalan paralel di minggu 13–16
3. Gunakan bersama RPS, RTM, dan lab manual yang tersedia di repository
4. Latihan soal di buku dapat digunakan sebagai tugas tambahan atau bahan kuis

**Konvensi Penulisan:**

| Simbol | Makna |
|--------|-------|
| `kode` | Kode Python atau JavaScript yang dapat dijalankan |
| **Tebal** | Istilah penting atau konsep kunci |
| *Miring* | Istilah asing atau penekanan |
| > Blockquote | Catatan penting atau tips |
| ⚠️ | Peringatan umum tentang kesalahan yang sering terjadi |

---

### Daftar Isi

| Bab | Judul | Halaman |
|-----|-------|---------|
| — | Halaman Depan | i |
| — | Kata Pengantar | ii |
| — | Prakata — Cara Menggunakan Buku Ini | iv |
| — | Mengapa Buku Ini? — Positioning dan Keunggulan | vi |
| — | Daftar Isi | viii |
| — | Daftar Tabel | x |
| — | Daftar Gambar | xi |
| — | Peta Capaian Pembelajaran | xii |
| **BAGIAN I** | **FONDASI** | |
| 1 | Pengantar Rekayasa Perangkat Lunak | 1 |
| 2 | Proses dan Model Pengembangan Perangkat Lunak | 35 |
| 3 | Requirements Engineering | 70 |
| 4 | Pemodelan Requirements dan Analisis | 105 |
| **BAGIAN II** | **PENGEMBANGAN** | |
| 5 | Arsitektur Perangkat Lunak | 140 |
| 6 | Desain Perangkat Lunak dan UML | 180 |
| 7 | Software Construction dan Version Control | 220 |
| **BAGIAN III** | **PENGUASAAN** | |
| 8 | Software Testing Fundamentals | 260 |
| 9 | Advanced Testing dan Quality Assurance | 300 |
| 10 | DevOps dan Continuous Delivery | 340 |
| 11 | Software Maintenance dan Evolution | 380 |
| **BAGIAN IV** | **FRONTIER** | |
| 12 | Software Project Management dan Agile | 420 |
| 13 | AI-Augmented Software Engineering | 460 |
| 14 | Proyek Akhir: Web App End-to-End | 500 |
| — | **Penutup: Refleksi dan Langkah ke Depan** | 540 |
| **LAMPIRAN** | | |
| A | Instalasi dan Setup GitHub Codespaces | 550 |
| B | Panduan Git dan GitHub untuk Tim | 558 |
| C | Template AI Usage Log | 565 |
| D | Panduan Penggunaan AI secara Bertanggung Jawab | 570 |
| E | Glosarium Istilah Rekayasa Perangkat Lunak | 580 |
| F | Template Dokumen SRS (Software Requirements Specification) | 595 |
| G | Cheat Sheet UML Diagrams | 605 |
| H | Cheat Sheet Docker dan GitHub Actions | 615 |

---

### Daftar Tabel

| No. | Judul Tabel | Halaman |
|-----|-------------|---------|
| 1.1 | Perbandingan Definisi Rekayasa Perangkat Lunak | 5 |
| 1.2 | Area Pengetahuan SWEBOK v4 (2024) | 12 |
| 1.3 | Kronologi Software Crisis dan Dampaknya | 18 |
| 2.1 | Perbandingan Model Proses Pengembangan | 40 |
| 2.2 | Karakteristik Metodologi Agile | 50 |
| 3.1 | Teknik Requirements Elicitation | 75 |
| 3.2 | Komponen Dokumen SRS | 85 |
| 4.1 | Template User Story dengan Acceptance Criteria | 110 |
| 5.1 | Perbandingan Architectural Patterns | 145 |
| 5.2 | Prinsip SOLID dan Contohnya | 155 |
| 6.1 | Jenis Diagram UML dan Penggunaannya | 185 |
| 7.1 | Perbandingan Git Branching Strategies | 225 |
| 8.1 | Tingkatan Pengujian Perangkat Lunak | 265 |
| 9.1 | Alat Pengujian dan Peruntukkannya | 305 |
| 10.1 | Komponen Pipeline CI/CD | 345 |
| 11.1 | Kategori Technical Debt | 385 |
| 12.1 | Peran dalam Tim Scrum | 425 |
| 13.1 | AI Tools untuk Setiap Tahap SDLC | 465 |
| 14.1 | Rubrik Penilaian Proyek Akhir | 510 |
| *...* | *Daftar lengkap tabel akan diperbarui setelah seluruh bab selesai* | |

---

### Daftar Gambar

| No. | Judul Gambar | Halaman |
|-----|--------------|---------|
| 1.1 | Lanskap Rekayasa Perangkat Lunak Modern | 3 |
| 1.2 | Hubungan SWEBOK v4 Knowledge Areas | 14 |
| 2.1 | Diagram Model Waterfall | 38 |
| 2.2 | Siklus Iteratif Agile/Scrum | 48 |
| 3.1 | Proses Requirements Engineering | 72 |
| 4.1 | Contoh Use Case Diagram | 108 |
| 5.1 | Arsitektur MVC dan Variannya | 143 |
| 5.2 | Arsitektur Microservices vs Monolith | 150 |
| 6.1 | Contoh Class Diagram | 188 |
| 6.2 | Contoh Sequence Diagram | 192 |
| 7.1 | Git Flow Workflow | 228 |
| 8.1 | Piramida Pengujian (Test Pyramid) | 262 |
| 10.1 | Pipeline CI/CD dengan GitHub Actions | 342 |
| 10.2 | Arsitektur Docker Container | 350 |
| 11.1 | Siklus Software Evolution | 382 |
| 12.1 | Scrum Framework Overview | 422 |
| 13.1 | AI-Augmented Development Workflow | 462 |
| 14.1 | Arsitektur Proyek Akhir Web App | 505 |
| *...* | *Daftar lengkap gambar akan diperbarui setelah seluruh bab selesai* | |

---

### Progressive AI Literacy

AI Corner dalam buku ini dirancang secara **progresif** — kemampuan interaksi dengan AI dibangun secara bertahap dari bab ke bab:

| Bab | Level AI Literacy | Contoh Aktivitas |
|-----|-------------------|------------------|
| 1–4 | **Basic** | Menulis prompt sederhana untuk memahami konsep SE; meminta AI menjelaskan perbedaan model proses; menggunakan AI untuk membantu menyusun user story |
| 5–7 | **Intermediate** | Meminta AI membantu merancang arsitektur; menggunakan AI untuk code review; AI-assisted UML diagram generation; pair programming dengan Copilot |
| 8–11 | **Advanced** | AI-assisted test generation; menggunakan AI untuk menulis Dockerfile dan CI/CD pipeline; debugging dengan AI; refactoring suggestions dari AI |
| 12–14 | **Expert** | AI-augmented project management; end-to-end development dengan AI sebagai co-developer; evaluasi kritis output AI; responsible AI usage dalam tim Agile |

Pada akhir buku, mahasiswa memiliki kompetensi untuk menggunakan AI secara produktif, kritis, dan bertanggung jawab dalam seluruh siklus pengembangan perangkat lunak.

---

### Peta Capaian Pembelajaran

```
PROFIL LULUSAN PRODI INFORMATIKA UAI
    │
    ├── CPL-S2  : Menjunjung tinggi nilai-nilai etika dan moral dalam profesi
    ├── CPL-KU2 : Mampu menerapkan pemikiran logis, kritis, dan sistematis
    ├── CPL-KK1 : Menguasai konsep dasar ilmu komputer dan informatika
    ├── CPL-KK3 : Mampu merancang dan mengembangkan perangkat lunak
    ├── CPL-P1  : Mampu menggunakan tools pengembangan perangkat lunak
    └── CPL-P3  : Mampu mengaplikasikan ilmu dalam penyelesaian masalah
         │
         ▼
    CAPAIAN PEMBELAJARAN MATA KULIAH (CPMK)
    ┌───────────────────────────────────────────────────────────────────┐
    │ CPMK-1 [C2] Menjelaskan konsep dasar RPL, model proses          │
    │   pengembangan (SDLC), SWEBOK v4, dan etika profesi SE          │
    │   → Bab 1, 2                                                     │
    │                                                                   │
    │ CPMK-2 [C3] Menerapkan teknik requirements engineering           │
    │   untuk menghasilkan dokumen kebutuhan yang lengkap              │
    │   → Bab 3, 4                                                     │
    │                                                                   │
    │ CPMK-3 [C3-C4] Menganalisis dan merancang arsitektur             │
    │   perangkat lunak menggunakan design patterns, UML,              │
    │   dan prinsip SOLID                                              │
    │   → Bab 5, 6                                                     │
    │                                                                   │
    │ CPMK-4 [C3-C4] Mengimplementasikan perangkat lunak dengan        │
    │   coding standards, Git, code review, dan kolaborasi             │
    │   Agile/Scrum                                                    │
    │   → Bab 7, 12                                                    │
    │                                                                   │
    │ CPMK-5 [C4-C5] Merancang strategi pengujian komprehensif         │
    │   (unit, integration, E2E) serta menerapkan TDD dan              │
    │   AI-assisted testing                                            │
    │   → Bab 8, 9                                                     │
    │                                                                   │
    │ CPMK-6 [C4-C5] Menerapkan DevOps, CI/CD, containerization        │
    │   (Docker), cloud deployment, dan software maintenance           │
    │   → Bab 10, 11                                                   │
    │                                                                   │
    │ CPMK-7 [C5-C6] Merancang dan membangun web app end-to-end        │
    │   dalam tim Agile/Scrum dengan AI sebagai co-developer           │
    │   → Bab 13, 14                                                   │
    └───────────────────────────────────────────────────────────────────┘
```

### Pemetaan CPMK ke Bab

| Bab | CPMK | Bloom's Level | Topik Utama |
|-----|------|---------------|-------------|
| 1 | CPMK-1 | C2 | Pengantar RPL, SWEBOK v4, Software Crisis, Etika Profesi |
| 2 | CPMK-1 | C2 | Model Proses: Waterfall, Agile/Scrum, Kanban, XP, DevOps |
| 3 | CPMK-2 | C3 | Requirements Elicitation, SRS, Validasi |
| 4 | CPMK-2 | C3 | Use Case, User Story, Acceptance Criteria, Backlog |
| 5 | CPMK-3 | C3-C4 | Arsitektur: MVC, Microservices, Layered, SOLID, Design Patterns |
| 6 | CPMK-3 | C3-C4 | UML, Database Design, API Design (REST) |
| 7 | CPMK-4 | C3-C4 | Clean Code, Code Smell, Refactoring, Git Flow, Code Review |
| 8 | CPMK-5 | C4-C5 | Unit Testing, Integration Testing, TDD, pytest, Jest |
| 9 | CPMK-5 | C4-C5 | E2E Testing, Performance Testing, Security Testing, AI-Assisted Testing |
| 10 | CPMK-6 | C4-C5 | GitHub Actions, Docker, Cloud Deployment, CI/CD |
| 11 | CPMK-6 | C4-C5 | Technical Debt, Refactoring, Metrics, SemVer, Maintenance |
| 12 | CPMK-4 | C3-C4 | Scrum, Kanban, Sprint Planning, Estimation, Retrospective |
| 13 | CPMK-7 | C5-C6 | Copilot, Claude Code, Cursor, Agentic Development, Responsible AI |
| 14 | CPMK-7 | C5-C6 | Proyek Akhir: Web App End-to-End dalam Tim Agile/Scrum |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
— Program Studi Informatika, Universitas Al Azhar Indonesia
