# Pedoman Praktikum Rekayasa Perangkat Lunak

**Kode Mata Kuliah:** IF2206
**Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.
**Program Studi Informatika** — Fakultas Sains dan Teknologi, Universitas Al Azhar Indonesia
**Semester Genap 2025/2026**

---

## 1. Identitas Praktikum

| Komponen | Keterangan |
|----------|------------|
| **Nama Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak |
| **Kode Mata Kuliah** | IF2206 |
| **Bobot SKS** | 1 SKS (Praktikum) |
| **Ko-requisite** | Rekayasa Perangkat Lunak (IF2205) |
| **Prasyarat** | — (Tidak ada) |
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Genap 2025/2026 |
| **Platform** | GitHub Codespaces |
| **Bahasa Pemrograman** | Python 3.x (Flask) + JavaScript (HTML/CSS/JS) |

---

## 2. Deskripsi dan Tujuan

Praktikum Rekayasa Perangkat Lunak (IF2206) merupakan komponen laboratorium dari mata kuliah Rekayasa Perangkat Lunak (IF2205). Dalam praktikum ini, mahasiswa menerapkan konsep-konsep teori rekayasa perangkat lunak yang telah dipelajari di kelas ke dalam praktik pengembangan aplikasi web (*web application development*) menggunakan Python Flask dan JavaScript di lingkungan GitHub Codespaces.

**Tujuan utama praktikum:**
1. Memberikan pengalaman *hands-on* dalam siklus pengembangan perangkat lunak (*Software Development Life Cycle / SDLC*) secara end-to-end
2. Melatih kemampuan kolaborasi tim menggunakan Git branching, pull request, dan code review
3. Membiasakan mahasiswa dengan *workflow* profesional: requirements → design → implementation → testing → deployment
4. Mengembangkan kemampuan menulis kode yang bersih, teruji, dan terdokumentasi
5. Mengembangkan kemampuan menggunakan AI sebagai *pair programmer* secara bertanggung jawab

---

## 3. Tata Tertib Praktikum

### 3.1 Kehadiran
- Kehadiran minimal **75%** dari seluruh sesi praktikum (12 dari 16 pertemuan)
- Mahasiswa yang kehadirannya kurang dari 75% **tidak diperkenankan mengikuti Responsi Akhir Semester (RAS)** dan mendapat nilai **E**
- Ketidakhadiran tanpa keterangan (alpa) mendapat nilai **0 (nol)** untuk laporan praktikum sesi tersebut
- Ketidakhadiran dengan keterangan (izin/sakit) wajib menyertakan bukti (surat izin/surat dokter) paling lambat 3 hari setelah ketidakhadiran

### 3.2 Keterlambatan
- Toleransi keterlambatan: **15 menit** dari jadwal mulai praktikum
- Mahasiswa yang terlambat lebih dari 15 menit **tidak diperkenankan mengikuti** sesi praktikum hari tersebut (dianggap alpa)
- Keterlambatan pengumpulan laporan/tugas dikenai pengurangan **10% per hari** dari nilai maksimal

### 3.3 Perangkat dan Persiapan
- Mahasiswa **wajib** membawa laptop pribadi yang terhubung ke internet
- Mahasiswa **wajib** memiliki akun GitHub yang aktif untuk mengakses GitHub Codespaces
- Mahasiswa **wajib** memiliki akun GitHub dengan benefit GitHub Education (untuk Codespaces gratis)
- Sebelum sesi praktikum, mahasiswa **wajib** membaca modul praktikum dan materi terkait di Buku Ajar

### 3.4 Kode Etik
- Dilarang keras melakukan **plagiarisme** (menyalin kode dari teman, internet, atau sumber lain tanpa atribusi)
- Dilarang keras membagikan kode tugas kepada mahasiswa di luar tim
- Pelanggaran kode etik akan dikenai **sanksi akademik** sesuai peraturan universitas (peringatan hingga nilai E)
- Diperbolehkan berdiskusi konsep dan pendekatan, tetapi **penulisan kode harus dilakukan oleh tim sendiri**
- Penggunaan AI (ChatGPT, Claude, Copilot) diperbolehkan untuk tugas dan laporan, dengan **wajib** mencantumkan AI Usage Log

### 3.5 Tata Krama
- Berpakaian rapi dan sopan sesuai ketentuan universitas
- Ponsel dalam mode *silent* selama praktikum
- Menjaga kebersihan dan ketertiban ruang laboratorium
- Menghargai dosen, asisten, dan sesama mahasiswa

---

## 4. Jadwal Praktikum

| Minggu | Modul | Topik | Komponen Penilaian |
|--------|-------|-------|--------------------|
| 1 | Lab 01 | Setup Dev Environment & GitHub Codespaces | L1 |
| 2 | Lab 02 | Git Branching & Pull Request Workflow | L2, T1 |
| 3 | Lab 03 | Requirements Documentation (SRS) | L3 |
| 4 | Lab 04 | User Story & Sprint Planning | L4, T2 |
| 5 | Lab 05 | Frontend Development (HTML/CSS/JS) | L5, T3 |
| 6 | Lab 06 | Backend Development (Python Flask API) | L6 |
| 7 | Lab 07 | Database Integration & ORM | L7, T4 |
| 8 | — | **Responsi Tengah Semester (RTS)** | RTS |
| 9 | Lab 09 | Unit Testing (pytest & Jest) | L9 |
| 10 | Lab 10 | Integration Testing & API Testing | L10, T5 |
| 11 | Lab 11 | CI/CD dengan GitHub Actions | L11, T6 |
| 12 | Lab 12 | Docker Containerization & Deployment | L12 |
| 13 | Lab 13 | AI Pair Programming & Code Review | L13 |
| 14 | Lab 14 | Sprint Review & Retrospective | L14 |
| 15 | — | **Presentasi & Demo Proyek Akhir** | PA |
| 16 | — | **Responsi Akhir Semester (RAS)** | RAS |

**Keterangan:** L = Laporan, T = Tugas, RTS/RAS = Responsi, PA = Proyek Akhir

---

## 5. Sistem Penilaian

### 5.1 Komponen Penilaian

| No | Komponen | Bobot | Frekuensi | Sifat |
|----|----------|-------|-----------|-------|
| 1 | Laporan Praktikum (L1–L13) | 25% | 13 kali | Tim/Individu, GitHub repository |
| 2 | Tugas Pemrograman (T1–T6) | 25% | 6 kali | Tim/Individu, take-home |
| 3 | Proyek Akhir | 35% | 1 kali | Tim (3-4 orang) |
| 4 | Responsi (RTS + RAS) | 10% | 2 kali | Individu, closed-book |
| 5 | Partisipasi Lab | 5% | Sepanjang semester | Individu |
| | **Total** | **100%** | | |

### 5.2 Penjelasan Komponen

**Laporan Praktikum (25%):**
Laporan dikumpulkan melalui GitHub repository setelah setiap sesi praktikum. Laporan dinilai berdasarkan kelengkapan, kebenaran implementasi, pemahaman konsep, dan kualitas dokumentasi.

**Tugas Pemrograman (25%):**
Tugas pemrograman (T1–T6) adalah *take-home assignment* yang lebih kompleks dari latihan di modul praktikum. Tugas diberikan pada minggu-minggu tertentu dan dikumpulkan sebelum sesi praktikum berikutnya. Detail spesifikasi ada di dokumen RTM Praktikum.

**Proyek Akhir (35%):**
Proyek akhir adalah aplikasi web end-to-end yang dibangun oleh tim (3-4 orang). Proyek ini merupakan proyek yang sama dengan MK teori (IF2205), namun dari perspektif praktikum fokus pada implementasi, testing, dan deployment. Detail di dokumen `04-assessments/project-guidelines.md`.

**Responsi (10%):**
Ujian praktik coding secara langsung (closed-book, tanpa AI, tanpa akses internet selain Codespaces):
- **RTS (Minggu 8):** Cakupan materi Minggu 1–7 (5%)
- **RAS (Minggu 16):** Cakupan materi Minggu 9–14 (5%)

**Partisipasi Lab (5%):**
Keaktifan selama sesi praktikum: bertanya, menjawab, membantu teman, menunjukkan inisiatif, kontribusi dalam code review.

### 5.3 Konversi Nilai

| Rentang Nilai | Huruf | Bobot |
|---------------|-------|-------|
| 85 – 100 | A | 4,00 |
| 80 – 84 | A- | 3,75 |
| 75 – 79 | B+ | 3,50 |
| 70 – 74 | B | 3,00 |
| 65 – 69 | B- | 2,75 |
| 60 – 64 | C+ | 2,50 |
| 55 – 59 | C | 2,00 |
| 40 – 54 | D | 1,00 |
| 0 – 39 | E | 0,00 |

---

## 6. Format Laporan Praktikum

Setiap laporan praktikum dikumpulkan melalui **GitHub repository** dengan struktur berikut:

### Template Laporan

```
# Laporan Praktikum [Nomor] — [Judul Modul]

## Identitas
- **Nama:** [Nama Lengkap] / [Nama Tim]
- **NIM:** [Nomor Induk Mahasiswa]
- **Kelas:** [Kelas Praktikum]
- **Tanggal:** [Tanggal Pelaksanaan]
- **Modul:** [Nomor dan Judul Modul]

## 1. Tujuan Praktikum
[Daftar tujuan pembelajaran dari modul — salin dari modul]

## 2. Dasar Teori
[Ringkasan singkat teori yang relevan — referensi ke Buku Ajar IF2205]

## 3. Langkah Praktikum
[Dokumentasi langkah-langkah yang dilakukan, disertai screenshot dan penjelasan]
[Setiap langkah harus disertai penjelasan singkat tentang apa yang dilakukan]

## 4. Hasil dan Analisis
[Penjelasan hasil implementasi]
[Analisis: apakah output sesuai harapan? Mengapa?]
[Screenshot bukti implementasi berjalan]

## 5. Tugas
[Jawaban dari tugas/soal di akhir modul praktikum]

## 6. Kesimpulan
[Apa yang dipelajari dari praktikum ini]
[Kesulitan yang dihadapi dan bagaimana mengatasinya]

## 7. AI Usage Log (jika menggunakan AI)
| No | Tanggal | Tool AI | Prompt yang Diberikan | Output AI | Evaluasi Mahasiswa | Keputusan |
|----|---------|---------|----------------------|-----------|-------------------|-----------|
| 1 | ... | ChatGPT / Claude / Copilot | ... | ... | Benar/Salah/Perlu modifikasi | Diterima / Dimodifikasi / Ditolak |
```

### Kriteria Penilaian Laporan

| Dimensi | Bobot | Deskripsi |
|---------|-------|-----------|
| Kelengkapan | 25% | Semua bagian template terisi lengkap |
| Kebenaran Implementasi | 30% | Program/fitur berjalan benar, output sesuai |
| Pemahaman | 25% | Penjelasan dan analisis menunjukkan pemahaman konsep RPL |
| Dokumentasi | 20% | Komentar kode, markdown penjelasan, screenshot, AI Usage Log |

---

## 7. Kebijakan Penggunaan AI

### 7.1 Prinsip Dasar
AI (ChatGPT, Claude, GitHub Copilot, dll.) diposisikan sebagai **pair programmer** — bukan pengganti berpikir. Mahasiswa bertanggung jawab penuh atas setiap baris kode yang dikumpulkan.

### 7.2 Kapan AI Diperbolehkan
- Saat mengerjakan **laporan praktikum** (L1–L13)
- Saat mengerjakan **tugas pemrograman** (T1–T6)
- Saat mengerjakan **proyek akhir**
- Dengan syarat: **WAJIB** mencantumkan AI Usage Log

### 7.3 Kapan AI TIDAK Diperbolehkan
- Saat **Responsi Tengah Semester (RTS)**
- Saat **Responsi Akhir Semester (RAS)**
- Penggunaan AI saat responsi dianggap sebagai **pelanggaran akademik**

### 7.4 Konsekuensi
- Laporan/tugas tanpa AI Usage Log padahal terdeteksi menggunakan AI: **pengurangan nilai 20%**
- Penggunaan AI saat responsi: **nilai 0 (nol)** untuk komponen tersebut + laporan ke pimpinan prodi

---

## 8. Proyek Akhir

### 8.1 Deskripsi
Proyek akhir adalah tugas kulminasi yang mengintegrasikan seluruh konsep yang dipelajari selama praktikum. Tim mahasiswa (3-4 orang) membangun aplikasi web end-to-end menggunakan Python Flask (backend), HTML/CSS/JS (frontend), dan database. Proyek ini merupakan proyek yang sama dengan MK teori IF2205, namun praktikum berfokus pada aspek implementasi, testing, dan deployment.

### 8.2 Persyaratan
- Dikerjakan secara **tim** (3-4 orang), tim yang sama dengan MK teori IF2205
- Harus mengintegrasikan **minimal 5 komponen** dari praktikum:
  1. Version control dengan Git (branching, pull request, code review)
  2. Frontend development (HTML/CSS/JS responsif)
  3. Backend development (Python Flask REST API)
  4. Database integration (SQLAlchemy ORM)
  5. Testing (unit test dan/atau integration test)
- Opsional: CI/CD pipeline, Docker containerization, AI pair programming (wajib dengan AI Usage Log)

### 8.3 Timeline

| Minggu | Milestone | Deliverable |
|--------|-----------|-------------|
| 10 | Proposal | 1 halaman: judul, latar belakang, fitur utama, arsitektur sistem, pembagian tugas tim |
| 12 | Progress Report | 50% implementasi + demo fitur utama berjalan |
| 15 | Final Submission + Presentasi | GitHub repository lengkap + slide presentasi + live demo |

### 8.4 Komponen Penilaian Proyek

| Dimensi | Bobot | Deskripsi |
|---------|-------|-----------|
| Teknis & Fungsionalitas | 30% | Aplikasi berjalan benar, fitur lengkap, frontend dan backend terintegrasi |
| Arsitektur & Desain | 25% | Pemilihan arsitektur tepat, desain modular, separation of concerns |
| Kualitas Kode & Testing | 20% | Clean code, modular, PEP 8, test coverage memadai |
| Presentasi & Dokumentasi | 15% | Presentasi jelas, dokumentasi lengkap, README profesional |
| Kreativitas & Inovasi | 10% | Ide orisinal, fitur tambahan, UI/UX diperhatikan |

Detail lengkap: lihat `04-assessments/project-guidelines.md`

---

## 9. Referensi

1. **Buku Ajar:** Materi teori dari MK Rekayasa Perangkat Lunak (IF2205) — Tri Aji Nugroho, S.T., M.T.
2. Sommerville, I. (2016). *Software Engineering*. 10th Edition. Pearson.
3. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach*. 9th Edition. McGraw-Hill.
4. Grinberg, M. (2018). *Flask Web Development*. 2nd Edition. O'Reilly Media.
5. Dokumentasi Flask: https://flask.palletsprojects.com/
6. Dokumentasi GitHub: https://docs.github.com/
7. Dokumentasi Docker: https://docs.docker.com/

---

## 10. Kontak dan Konsultasi

| Komponen | Detail |
|----------|--------|
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Jadwal Konsultasi** | Sesuai kesepakatan (buat janji via email atau LMS) |
| **Platform Komunikasi** | Google Classroom / LMS UAI |
| **Repositori Materi** | Tersedia di repositori GitHub mata kuliah |

---

*Pedoman ini berlaku untuk Semester Genap 2025/2026. Perubahan akan diinformasikan melalui platform komunikasi resmi.*

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
