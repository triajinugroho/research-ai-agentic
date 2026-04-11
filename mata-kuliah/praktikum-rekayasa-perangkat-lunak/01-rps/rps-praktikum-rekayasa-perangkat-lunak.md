# Rencana Pembelajaran Semester (RPS) — Praktikum Rekayasa Perangkat Lunak (IF2206)

## A. Identitas Mata Kuliah

| Komponen | Keterangan |
|----------|------------|
| **Kode Mata Kuliah** | IF2206 |
| **Nama Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak |
| **Bobot SKS** | 1 SKS |
| **Semester** | Genap 2025/2026 |
| **Ko-Requisit** | IF2205 — Rekayasa Perangkat Lunak |
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika |
| **Fakultas** | Sains dan Teknologi |
| **Universitas** | Universitas Al Azhar Indonesia |

## B. Deskripsi Mata Kuliah

Praktikum Rekayasa Perangkat Lunak merupakan mata kuliah pendamping (ko-requisit) dari IF2205 Rekayasa Perangkat Lunak yang berfokus pada penerapan langsung (*hands-on*) konsep-konsep rekayasa perangkat lunak melalui pengembangan aplikasi web secara bertahap. Mahasiswa akan membangun aplikasi web menggunakan Flask (Python), mengelola kode sumber dengan Git, menulis pengujian otomatis dengan pytest, melakukan deployment menggunakan Docker, serta mengintegrasikan praktik CI/CD dalam siklus pengembangan. Seluruh kegiatan praktikum mengikuti metodologi Agile/Scrum dengan sprint-sprint yang terstruktur, sehingga mahasiswa memperoleh pengalaman nyata dalam siklus hidup pengembangan perangkat lunak profesional.

## C. Capaian Pembelajaran Lulusan (CPL)

| Kode | Capaian Pembelajaran Lulusan |
|------|------------------------------|
| CPL-KK1 | Mampu menerapkan prinsip-prinsip matematika, sains, dan rekayasa dalam pemecahan masalah informatika |
| CPL-KK4 | Mampu merancang dan mengimplementasikan solusi perangkat lunak yang memenuhi kebutuhan pengguna |
| CPL-P3 | Mampu bekerja secara efektif dalam tim dengan menerapkan komunikasi profesional |
| CPL-KU2 | Mampu menggunakan metode, teknik, dan alat bantu rekayasa perangkat lunak modern |
| CPL-S2 | Mampu menerapkan prinsip etika, nilai-nilai Islam, dan tanggung jawab profesional dalam pengembangan perangkat lunak |
| CPL-P2 | Mampu belajar secara mandiri dan adaptif terhadap perkembangan teknologi termasuk pemanfaatan AI |

## D. Capaian Pembelajaran Mata Kuliah (CPMK)

| Kode | CPMK | CPL |
|------|------|-----|
| CPMK-1 | Mampu menyiapkan lingkungan pengembangan dan menggunakan alat bantu pengembangan modern (C3) | CPL-KU2 |
| CPMK-2 | Mampu mengelola kode sumber menggunakan sistem version control Git (C3) | CPL-KU2 |
| CPMK-3 | Mampu menerjemahkan dokumen kebutuhan menjadi spesifikasi teknis dan user story (C4) | CPL-KK4 |
| CPMK-4 | Mampu mengimplementasikan aplikasi web full-stack dengan arsitektur berlapis (C3) | CPL-KK1, CPL-KK4 |
| CPMK-5 | Mampu merancang dan mengeksekusi pengujian perangkat lunak secara otomatis (C4) | CPL-KK4, CPL-KU2 |
| CPMK-6 | Mampu melakukan deployment dan menerapkan praktik CI/CD (C3) | CPL-KU2 |
| CPMK-7 | Mampu bekerja dalam tim Agile/Scrum dan memanfaatkan AI sebagai mitra pengembangan secara etis (C5) | CPL-P3, CPL-S2, CPL-P2 |

## E. Rencana Pembelajaran 16 Minggu

| Minggu | Sub-CPMK | Materi Praktikum | Metode | Bobot (%) |
|--------|----------|-------------------|--------|-----------|
| 1 | Sub-CPMK 1.1 | Setup Environment: Python, Flask, VS Code/Codespaces, virtual environment | Praktikum terbimbing | 3 |
| 2 | Sub-CPMK 2.1 | Git & GitHub: init, commit, push, pull, branching, merge, pull request | Praktikum terbimbing | 5 |
| 3 | Sub-CPMK 3.1 | Dokumen SRS: menulis Software Requirements Specification dari studi kasus | Praktikum terbimbing | 5 |
| 4 | Sub-CPMK 3.2 | User Story & Backlog: penulisan user story, acceptance criteria, product backlog | Praktikum terbimbing | 5 |
| 5 | Sub-CPMK 4.1 | Frontend Development: HTML, CSS, Jinja2 template, responsive design | Praktikum terbimbing | 7 |
| 6 | Sub-CPMK 4.2 | Backend Development: Flask routing, request/response, REST API endpoint | Praktikum terbimbing | 7 |
| 7 | Sub-CPMK 4.3 | Database Integration: SQLite/PostgreSQL, SQLAlchemy ORM, migrasi database | Praktikum terbimbing | 7 |
| 8 | — | **Responsi Tengah Semester (RTS)** | Responsi praktik | 10 |
| 9 | Sub-CPMK 5.1 | Unit Testing: pytest, test fixtures, mocking, code coverage | Praktikum terbimbing | 7 |
| 10 | Sub-CPMK 5.2 | Integration Testing: pengujian API endpoint, test database, end-to-end scenario | Praktikum terbimbing | 7 |
| 11 | Sub-CPMK 6.1 | CI/CD Pipeline: GitHub Actions, automated testing, linting, deployment pipeline | Praktikum terbimbing | 7 |
| 12 | Sub-CPMK 6.2 | Containerization: Dockerfile, docker-compose, container registry, deployment | Praktikum terbimbing | 7 |
| 13 | Sub-CPMK 7.1 | AI-Augmented Development: GitHub Copilot, ChatGPT/Claude untuk code review dan debugging | Praktikum terbimbing | 5 |
| 14 | Sub-CPMK 7.2 | Sprint Review: demo produk, retrospective, dokumentasi akhir | Praktikum mandiri | 8 |
| 15 | Sub-CPMK 7.3 | Presentasi Proyek: demo final, peer review, evaluasi tim | Presentasi | 5 |
| 16 | — | **Responsi Akhir Semester (RAS)** | Responsi praktik | 5 |

## F. Komponen Asesmen

| Komponen | Bobot (%) | Keterangan |
|----------|-----------|------------|
| **Laporan Praktikum** | 25 | 13 laporan mingguan (L1–L13, tidak termasuk minggu 8 dan 16) |
| **Tugas Pemrograman** | 25 | 6 tugas pemrograman individu (TP1–TP6) |
| **Proyek Akhir** | 35 | Proyek tim 4 sprint (sama dengan tim IF2205) |
| **Responsi** | 10 | RTS (Minggu 8) + RAS (Minggu 16) |
| **Partisipasi** | 5 | Kehadiran, keaktifan, kontribusi diskusi |
| **Total** | **100** | |

## G. Skala Penilaian

| Huruf | Rentang Nilai | Bobot |
|-------|--------------|-------|
| A | 81–100 | 4.00 |
| B+ | 75–80 | 3.50 |
| B | 69–74 | 3.00 |
| C+ | 63–68 | 2.50 |
| C | 56–62 | 2.00 |
| D | 45–55 | 1.00 |
| E | 0–44 | 0.00 |

## H. Referensi

1. Grinberg, M. (2018). *Flask Web Development: Developing Web Applications with Python*, 2nd Edition. O'Reilly Media.
2. Percival, H. J. W. (2017). *Test-Driven Development with Python*, 2nd Edition. O'Reilly Media.
3. Chacon, S., & Straub, B. (2014). *Pro Git*, 2nd Edition. Apress. [https://git-scm.com/book](https://git-scm.com/book)
4. Docker Documentation. [https://docs.docker.com/](https://docs.docker.com/)
5. Sommerville, I. (2015). *Software Engineering*, 10th Edition. Pearson.

---

Jakarta, Februari 2026
Dosen Pengampu,

**Tri Aji Nugroho, S.T., M.T.**

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
