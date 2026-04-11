# Assessment Framework — Praktikum Rekayasa Perangkat Lunak (IF2206)

| Informasi | Detail |
|-----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **SKS** | 1 SKS (Praktikum) |
| **Co-requisite** | Rekayasa Perangkat Lunak (IF2205, 3 SKS Teori) |
| **Semester** | Genap 2025/2026 |
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Platform** | GitHub Codespaces |
| **Referensi Pedoman** | `00-pedoman-praktikum/pedoman-praktikum-rpl.md` |

---

## A. Komponen dan Bobot Penilaian

| No | Komponen | Bobot (%) | Jumlah Item | Deskripsi | CPMK yang Diukur |
|----|----------|-----------|-------------|-----------|-------------------|
| 1 | Laporan Praktikum | 25 | 13 laporan (L1-L13) | Laporan individual setiap sesi praktikum | CPMK 1-7 |
| 2 | Tugas Pemrograman | 25 | 6 tugas (TP1-TP6) | Tugas coding individual dengan deliverables spesifik | CPMK 1-6 |
| 3 | Proyek Akhir | 35 | 5 sprint (Sprint 0-4) + Demo | Proyek tim berkelanjutan, sama dengan IF2205 | CPMK 2-7 |
| 4 | Responsi | 10 | RTS (5%) + RAS (5%) | Ujian praktik langsung di lab | CPMK 1-6 |
| 5 | Partisipasi | 5 | Kehadiran & keaktifan | Kontribusi di kelas dan diskusi | CPMK 7 |
| | **Total** | **100** | | | |

### Rumus Perhitungan Nilai Akhir

```
Nilai Akhir = (Rata-rata Laporan × 0.25)
            + (Rata-rata Tugas × 0.25)
            + (Nilai Proyek × 0.35)
            + (Nilai Responsi × 0.10)
            + (Nilai Partisipasi × 0.05)
```

**Catatan:** Proyek akhir IF2206 menggunakan proyek yang **sama** dengan IF2205. Penilaian IF2206 fokus pada aspek implementasi teknis (coding, testing, deployment), sedangkan IF2205 fokus pada aspek rekayasa (requirements, desain, manajemen proyek).

---

## B. Pemetaan Detail CPMK × Komponen Asesmen

### B.1 Matriks CPMK ke Komponen

| CPMK | Deskripsi | Laporan | Tugas | Proyek | Responsi | Partisipasi |
|------|-----------|---------|-------|--------|----------|-------------|
| CPMK-1 (Setup & Tools) | Mengonfigurasi environment pengembangan | L1 | TP1 | — | RTS | — |
| CPMK-2 (Version Control) | Menerapkan Git workflow kolaboratif | L2 | TP2 | Sprint 1-4 | RTS | — |
| CPMK-3 (Requirements) | Mendokumentasikan requirements & user stories | L3, L4 | — | Sprint 0 | RTS | — |
| CPMK-4 (Full-Stack Dev) | Mengimplementasikan aplikasi full-stack | L5, L6, L7 | TP3, TP4 | Sprint 0-2 | RTS, RAS | — |
| CPMK-5 (Testing) | Menerapkan testing dan quality assurance | L9, L10 | TP5 | Sprint 1-2 | RAS | — |
| CPMK-6 (CI/CD & Deploy) | Membangun pipeline CI/CD dan deployment | L11, L12 | TP6 | Sprint 2-3 | RAS | — |
| CPMK-7 (Agile & AI & Etika) | Menerapkan Agile, AI tools, dan etika profesional | L13, L14 | — | Sprint 3-4 | — | V |

### B.2 Detail Item Pengukuran per CPMK

**CPMK-1 (Setup & Tools)**
- L1: Dokumentasi proses setup GitHub Codespaces, devcontainer, Python/Flask environment
- TP1: Flask Hello World berjalan + Git init dengan commit history yang benar
- RTS: Demonstrasi kemampuan setup project baru dari scratch

**CPMK-2 (Version Control)**
- L2: Dokumentasi workflow branching dan pull request
- TP2: Branching strategy, conflict resolution, conventional commits, peer review via PR
- Sprint 1-4: Konsistensi penggunaan Git di seluruh sprint proyek
- RTS: Demonstrasi Git commands (branch, merge, rebase, resolve conflicts)

**CPMK-3 (Requirements)**
- L3: Dokumentasi SRS (Software Requirements Specification)
- L4: User stories dengan acceptance criteria
- Sprint 0: Product backlog dan sprint planning proyek tim
- RTS: Kemampuan menulis user story dan acceptance criteria

**CPMK-4 (Full-Stack Dev)**
- L5-L7: Dokumentasi implementasi frontend, backend, dan database
- TP3: REST API dengan 5+ endpoints, error handling, input validation
- TP4: Database CRUD dengan ORM, migrations, query optimization
- Sprint 0-2: Implementasi fitur aplikasi proyek tim
- RTS/RAS: Live coding sederhana (API endpoint atau database query)

**CPMK-5 (Testing)**
- L9-L10: Dokumentasi unit test dan integration test
- TP5: Test suite dengan coverage >= 80%, TDD evidence, edge cases
- Sprint 1-2: Test coverage proyek tim
- RAS: Menulis test case untuk kode yang diberikan

**CPMK-6 (CI/CD & Deploy)**
- L11-L12: Dokumentasi CI/CD pipeline dan Docker deployment
- TP6: Dockerfile, docker-compose, deployment ke cloud platform
- Sprint 2-3: Pipeline CI/CD dan deployment proyek tim
- RAS: Demonstrasi troubleshooting pipeline failure

**CPMK-7 (Agile & AI & Etika)**
- L13: Dokumentasi AI pair programming dan code review
- L14: Sprint review dan retrospective
- Sprint 3-4: Scrum artifacts, AI Usage Log, retrospective
- Partisipasi: Kontribusi aktif di kelas, peer review, diskusi

---

## C. Skala Penilaian (7 Tingkat)

| Huruf | Rentang Nilai | Bobot | Predikat |
|-------|--------------|-------|----------|
| A | 81-100 | 4.00 | Sangat Baik |
| B+ | 75-80 | 3.50 | Baik Sekali |
| B | 69-74 | 3.00 | Baik |
| C+ | 63-68 | 2.50 | Cukup Baik |
| C | 56-62 | 2.00 | Cukup |
| D | 45-55 | 1.00 | Kurang |
| E | 0-44 | 0.00 | Tidak Lulus |

### Persyaratan Kelulusan

1. Nilai akhir minimal **C (56)** untuk lulus mata kuliah.
2. Kehadiran minimal **75%** dari total pertemuan.
3. Wajib mengikuti **RTS dan RAS** (kecuali ada izin resmi).
4. Wajib menyelesaikan **minimal 4 dari 6 TP** dan **minimal 10 dari 13 laporan**.
5. Wajib berpartisipasi dalam **proyek akhir** (tidak boleh tidak berkontribusi).

---

## D. Kebijakan Kehadiran

- Kehadiran minimal **75%** dari total pertemuan praktikum (minimal 12 dari 16 pertemuan).
- Mahasiswa yang tidak memenuhi syarat kehadiran **tidak dapat mengikuti RAS** dan mendapat nilai maksimal **D**.
- Ketidakhadiran dengan surat keterangan resmi (sakit/izin) tidak dihitung sebagai absen, maksimal **3 kali** per semester.
- Keterlambatan lebih dari **15 menit** dianggap sebagai setengah hadir (0.5 kehadiran).
- Mahasiswa wajib hadir di lab sesuai kelompok praktikum yang terdaftar.

---

## E. Kebijakan Keterlambatan Pengumpulan (Late Policy)

| Keterlambatan | Penalti | Contoh |
|---------------|---------|--------|
| Tepat waktu | Tidak ada penalti | Nilai penuh |
| <= 1 hari (24 jam) | Pengurangan 10% | Nilai maks 90 |
| 2-3 hari | Pengurangan 25% | Nilai maks 75 |
| 4-7 hari | Pengurangan 50% | Nilai maks 50 |
| > 7 hari | Tidak diterima (nilai 0) | — |

**Ketentuan tambahan:**
- Late policy berlaku untuk **laporan** dan **tugas pemrograman**.
- Proyek akhir mengikuti deadline sprint — **tidak ada perpanjangan** kecuali keadaan darurat yang disetujui dosen.
- Deadline dihitung berdasarkan waktu commit terakhir di GitHub (timestamp commit).
- Pengumpulan melalui pull request — bukan email atau chat.

---

## F. Kalender Deadline Lengkap

### F.1 Deadline Laporan Praktikum (L1-L13)

| Laporan | Topik | Minggu Lab | Deadline Pengumpulan |
|---------|-------|------------|---------------------|
| L1 | Setup Dev Environment & GitHub Codespaces | 1 | Akhir Minggu 2 |
| L2 | Git Branching & Pull Request Workflow | 2 | Akhir Minggu 3 |
| L3 | Requirements Documentation (SRS) | 3 | Akhir Minggu 4 |
| L4 | User Story & Sprint Planning | 4 | Akhir Minggu 5 |
| L5 | Frontend Development (HTML/CSS/JS) | 5 | Akhir Minggu 6 |
| L6 | Backend Development (Flask API) | 6 | Akhir Minggu 7 |
| L7 | Database Integration & ORM | 7 | Akhir Minggu 8 |
| — | **Minggu 8: Responsi Tengah Semester (RTS)** | 8 | — |
| L8 | Unit Testing (pytest & Jest) | 9 | Akhir Minggu 10 |
| L9 | Integration & API Testing | 10 | Akhir Minggu 11 |
| L10 | CI/CD dengan GitHub Actions | 11 | Akhir Minggu 12 |
| L11 | Docker & Deployment | 12 | Akhir Minggu 13 |
| L12 | AI Pair Programming & Code Review | 13 | Akhir Minggu 14 |
| L13 | Sprint Review & Retrospective | 14 | Akhir Minggu 15 |
| — | **Minggu 16: Responsi Akhir Semester (RAS)** | 16 | — |

### F.2 Deadline Tugas Pemrograman (TP1-TP6)

| Tugas | Topik | CPMK | Diberikan | Deadline |
|-------|-------|------|-----------|----------|
| TP1 | Flask Hello World + Git | CPMK-1, CPMK-4 | Minggu 1 | Minggu 3 |
| TP2 | Git Branching & PR | CPMK-2 | Minggu 2 | Minggu 4 |
| TP3 | REST API CRUD | CPMK-4 | Minggu 6 | Minggu 8 |
| TP4 | Database CRUD + ORM | CPMK-4 | Minggu 7 | Minggu 10 |
| TP5 | Testing Suite | CPMK-5 | Minggu 9 | Minggu 12 |
| TP6 | Docker + Deployment | CPMK-6 | Minggu 12 | Minggu 14 |

### F.3 Deadline Responsi

| Responsi | Minggu | Cakupan | Bobot |
|----------|--------|---------|-------|
| RTS (Responsi Tengah Semester) | Minggu 8 | CPMK 1-4 (Setup, Git, Requirements, Full-Stack) | 5% |
| RAS (Responsi Akhir Semester) | Minggu 16 | CPMK 4-6 (Full-Stack, Testing, CI/CD & Deploy) | 5% |

### F.4 Deadline Proyek Akhir (per Sprint)

| Sprint | Minggu | Deliverable Utama | Deadline Sprint Review |
|--------|--------|-------------------|----------------------|
| Sprint 0 | 5-6 | Frontend + Backend prototype | Akhir Minggu 6 |
| Sprint 1 | 7 + 9 | Database + Unit Testing | Akhir Minggu 9 |
| Sprint 2 | 10-11 | Integration Testing + CI/CD | Akhir Minggu 11 |
| Sprint 3 | 12-13 | Docker + AI Pair Programming | Akhir Minggu 13 |
| Sprint 4 | 14 | Sprint Review & Retrospective | Akhir Minggu 14 |
| Demo | 15 | Presentasi & Demo Proyek Akhir | Minggu 15 |

---

## G. Kebijakan Penggunaan AI (AI Policy)

### G.1 Prinsip Umum

1. AI tools (ChatGPT, Claude, GitHub Copilot) **diizinkan** sebagai mitra belajar (*AI-as-a-partner*).
2. AI **bukan pengganti** — mahasiswa wajib **memahami** setiap baris kode yang dikumpulkan.
3. Setiap penggunaan AI **wajib** didokumentasikan dalam **AI Usage Log**.
4. Plagiasi dari AI tanpa pemahaman dan tanpa log dianggap sebagai **pelanggaran akademik**.
5. Prinsip **amanah** (kejujuran akademik sesuai nilai Islam) menjadi landasan utama.

### G.2 Kebijakan AI per Komponen Asesmen

| Komponen | AI Diizinkan? | Aturan Spesifik |
|----------|--------------|-----------------|
| **Laporan Praktikum** | Ya, dengan log | AI boleh membantu debugging dan penjelasan konsep. Narasi laporan harus ditulis sendiri. AI Usage Log wajib dilampirkan jika menggunakan AI. |
| **Tugas Pemrograman (TP1-TP2)** | **Tidak** | TP1 dan TP2 menguji kemampuan dasar — harus dikerjakan mandiri tanpa AI. |
| **Tugas Pemrograman (TP3-TP6)** | Ya, dengan log | AI boleh digunakan sebagai pair programmer. Mahasiswa harus bisa menjelaskan setiap bagian kode. AI Usage Log wajib. |
| **Proyek Akhir** | Ya, dengan log | AI boleh digunakan untuk coding, debugging, dan code review. AI Usage Log wajib per sprint. Kontribusi AI vs mahasiswa harus jelas. |
| **Responsi (RTS & RAS)** | **Tidak** | Responsi adalah ujian langsung tanpa bantuan AI, internet, atau catatan. |
| **Partisipasi** | Tidak relevan | — |

### G.3 Format AI Usage Log

Setiap penggunaan AI harus didokumentasikan dengan format berikut:

```markdown
## AI Usage Log

| No | Tanggal | Tool | Prompt (ringkas) | Output (ringkas) | Modifikasi yang Dilakukan | Pemahaman (Y/N) |
|----|---------|------|------------------|------------------|---------------------------|-----------------|
| 1 | 2026-03-15 | Claude | "Bantu buat endpoint GET /books" | Kode Flask route | Menambahkan error handling 404 | Y |
| 2 | 2026-03-15 | Copilot | Auto-complete model Book | Suggestion SQLAlchemy model | Menambahkan field isbn, mengubah tipe data | Y |
```

**Ketentuan AI Usage Log:**
- Harus dilampirkan di **setiap laporan dan tugas** yang menggunakan AI.
- Harus dilampirkan di **setiap sprint** proyek akhir (di repository GitHub).
- Kolom "Modifikasi yang Dilakukan" menunjukkan bahwa mahasiswa tidak *copy-paste* mentah.
- Kolom "Pemahaman" harus "Y" — jika "N", mahasiswa harus menjelaskan apa yang belum dipahami.

---

## H. Integritas Akademik

### H.1 Definisi Pelanggaran

| Jenis Pelanggaran | Contoh | Tingkat |
|-------------------|--------|---------|
| Plagiasi kode antar-kelompok | Copy-paste kode dari kelompok lain tanpa atribusi | Berat |
| Plagiasi dari AI tanpa log | Menggunakan AI-generated code tanpa AI Usage Log | Sedang |
| Plagiasi dari internet | Copy-paste dari StackOverflow/GitHub tanpa atribusi | Sedang |
| Fabrikasi output | Screenshot atau output yang dipalsukan | Berat |
| Proxy submission | Meminta orang lain mengerjakan tugas | Berat |
| Kolaborasi tidak sah saat responsi | Berkomunikasi dengan mahasiswa lain saat RTS/RAS | Berat |

### H.2 Sanksi

| Pelanggaran | Sanksi |
|-------------|--------|
| Pelanggaran pertama (Sedang) | Nilai **0** untuk komponen terkait + peringatan tertulis |
| Pelanggaran pertama (Berat) | Nilai **0** untuk komponen terkait + laporan ke Prodi |
| Pelanggaran kedua | Nilai **E** untuk mata kuliah + laporan ke Prodi |
| Pelanggaran berulang | Sanksi akademik sesuai peraturan UAI |

### H.3 Prinsip Amanah

Sebagai institusi dengan nilai Islam, UAI menekankan prinsip **amanah** (kejujuran dan tanggung jawab):
- Kode yang dikumpulkan harus dipahami sepenuhnya oleh mahasiswa.
- Setiap mahasiswa bertanggung jawab atas setiap baris kode yang dikumpulkan.
- Kemampuan menjelaskan kode saat responsi menjadi bukti pemahaman.
- Kejujuran dalam AI Usage Log adalah wujud amanah akademik.

---

## I. Kebijakan Remedial

### I.1 Syarat Mengikuti Remedial

1. Mahasiswa dengan nilai komponen < 56 (di bawah C) berhak mengajukan remedial.
2. Remedial hanya tersedia untuk **Tugas Pemrograman (TP)** dan **Laporan Praktikum**.
3. Proyek akhir dan responsi **tidak dapat di-remedial**.
4. Maksimal **2 TP** dan **3 laporan** yang dapat di-remedial per semester.
5. Pengajuan remedial paling lambat **1 minggu** setelah nilai komponen diumumkan.

### I.2 Mekanisme Remedial

| Komponen | Mekanisme Remedial | Nilai Maksimal |
|----------|-------------------|----------------|
| Tugas Pemrograman | Revisi tugas sesuai feedback dosen, deadline 1 minggu | 70 (B) |
| Laporan Praktikum | Revisi laporan sesuai feedback, deadline 1 minggu | 70 (B) |
| Responsi | Tidak ada remedial | — |
| Proyek Akhir | Tidak ada remedial (dinilai per sprint) | — |

### I.3 Proses Remedial

1. Mahasiswa mengajukan remedial melalui email ke dosen dengan menyebutkan komponen yang ingin di-remedial.
2. Dosen memberikan feedback spesifik tentang apa yang perlu diperbaiki.
3. Mahasiswa merevisi dan mengumpulkan ulang dalam **7 hari kalender**.
4. Nilai remedial maksimal **70** (setara B), tidak bisa mendapat A atau B+.

---

## J. Format Laporan Standar

Setiap laporan praktikum harus mengikuti format standar berikut. Detail lengkap tersedia di `00-pedoman-praktikum/pedoman-praktikum-rpl.md`.

### Struktur Laporan

```
1. Header (Nama, NIM, Kelompok, Lab ke-N, Tanggal)
2. Tujuan Praktikum
3. Langkah-langkah yang Dikerjakan
   - Screenshot setiap langkah utama
   - Kode yang ditulis/dimodifikasi
   - Output/hasil yang diperoleh
4. Tantangan Tambahan (jika dikerjakan)
5. Analisis & Refleksi
   - Apa yang dipelajari
   - Kesulitan yang dihadapi dan solusinya
   - Hubungan dengan materi teori IF2205
6. AI Usage Log (jika menggunakan AI)
7. Referensi (jika ada)
```

### Ketentuan Format

- Format: **Markdown** di repository GitHub (bukan PDF atau Word).
- Penamaan file: `laporan-lab-NN-NIM.md` (contoh: `laporan-lab-01-2210001.md`).
- Screenshot disimpan di folder `images/` dalam repository.
- Kode harus dalam code block dengan syntax highlighting.
- Laporan dikumpulkan melalui **pull request** ke repository praktikum.

---

## K. Integrasi dengan IF2205 (Rekayasa Perangkat Lunak — Teori)

### K.1 Hubungan Penilaian

| Aspek | IF2205 (Teori) | IF2206 (Praktikum) |
|-------|---------------|---------------------|
| **Proyek** | Fokus: requirements, desain, manajemen proyek (25% bobot IF2205) | Fokus: implementasi, testing, deployment (35% bobot IF2206) |
| **Tim** | Tim yang **sama** untuk kedua MK | Tim yang **sama** untuk kedua MK |
| **Deliverables** | SRS, desain UML, laporan manajemen | Source code, test suite, CI/CD pipeline, Docker |
| **Presentasi** | Presentasi desain dan proses (Minggu 15) | Demo aplikasi berjalan (Minggu 15) |
| **Penilaian** | Proses rekayasa, kualitas dokumentasi | Kualitas teknis, fungsionalitas, deployment |

### K.2 Keselarasan Mingguan

Setiap praktikum IF2206 selaras dengan materi teori IF2205 minggu yang sama:

| Minggu | IF2205 (Teori) | IF2206 (Praktikum) |
|--------|---------------|---------------------|
| 1 | Pengantar RPL & SDLC | Setup Dev Environment |
| 2 | Proses & Model Pengembangan | Git Branching & PR Workflow |
| 3 | Requirements Engineering | Requirements Documentation (SRS) |
| 4 | Pemodelan Requirements | User Story & Sprint Planning |
| 5 | Arsitektur & Design Patterns | Frontend Development |
| 6 | Desain UML & Database | Backend Development (Flask API) |
| 7 | Software Construction | Database Integration & ORM |
| 8 | **UTS** | **Responsi Tengah Semester (RTS)** |
| 9 | Software Testing | Unit Testing (pytest & Jest) |
| 10 | Advanced Testing | Integration & API Testing |
| 11 | DevOps & CI/CD | CI/CD dengan GitHub Actions |
| 12 | Maintenance & Evolution | Docker & Deployment |
| 13 | AI-Augmented SE | AI Pair Programming & Code Review |
| 14 | Modern SE Trends | Sprint Review & Retrospective |
| 15 | Presentasi Proyek Akhir | Demo Proyek Akhir |
| 16 | **UAS** | **Responsi Akhir Semester (RAS)** |

### K.3 Konsekuensi Penilaian Lintas-MK

- Ketidakpartisipasian dalam proyek tim berdampak pada **kedua mata kuliah**.
- Peer review dilakukan sekali dan hasilnya digunakan untuk IF2205 **dan** IF2206.
- Mahasiswa yang tidak lulus IF2206 tetap bisa lulus IF2205, dan sebaliknya — penilaian independen.

---

## L. Flowchart Proses Penilaian

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ALUR PROSES PENILAIAN IF2206                     │
└─────────────────────────────────────────────────────────────────────┘

  ┌──────────────┐
  │  Mahasiswa    │
  │  Mengerjakan  │
  │  Tugas/Lab    │
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐     Tidak     ┌──────────────┐
  │  Kumpul via  │──────────────▶│  Late Policy  │
  │  PR di GitHub│  Terlambat?   │  Berlaku      │
  │  (on time?)  │               │  (-10% s/d 0) │
  └──────┬───────┘               └──────┬───────┘
         │ Ya                           │
         ▼                              ▼
  ┌──────────────────────────────────────┐
  │       Dosen/Asisten Menilai          │
  │  (Rubrik sesuai komponen)            │
  │  • Laporan: 4 dimensi × 4 level     │
  │  • TP: 4-5 dimensi × 4 level        │
  │  • Proyek: 7 komponen rubrik         │
  └──────────────┬───────────────────────┘
                 │
                 ▼
  ┌──────────────┐     Ya      ┌──────────────┐
  │  Nilai < 56  │────────────▶│  Eligible     │
  │  (di bawah C)│             │  Remedial?    │
  └──────┬───────┘             └──────┬───────┘
         │ Tidak                      │ Ya
         ▼                            ▼
  ┌──────────────┐            ┌──────────────┐
  │  Feedback    │            │  Revisi &     │
  │  Diberikan   │            │  Kumpul Ulang │
  │  via GitHub  │            │  (maks 70)    │
  └──────┬───────┘            └──────┬───────┘
         │                           │
         ▼                           ▼
  ┌──────────────────────────────────────┐
  │       Nilai Final Direkap           │
  │  (Input ke sistem akademik UAI)     │
  └─────────────────────────────────────┘
```

---

## M. Rubrik Ringkas per Komponen

### M.1 Rubrik Laporan Praktikum

Rubrik detail tersedia di `rubrik-laporan-praktikum.md`.

| Dimensi | Bobot | Deskripsi Singkat |
|---------|-------|-------------------|
| Kelengkapan | 25% | Semua langkah lab diselesaikan |
| Kebenaran Implementasi | 30% | Kode berjalan benar sesuai instruksi |
| Pemahaman Konsep | 25% | Analisis menunjukkan pemahaman mendalam |
| Dokumentasi & AI Log | 20% | Format rapi, screenshot lengkap, AI log jika relevan |

### M.2 Rubrik Tugas Pemrograman

Rubrik detail per TP tersedia di `rubrik-tugas.md`.

| TP | Dimensi Utama |
|----|--------------|
| TP1 (Flask) | Fungsionalitas, Struktur Kode, Git Usage, Dokumentasi |
| TP2 (Git) | Branching Strategy, Conflict Resolution, Commit Quality, PR & Review |
| TP3 (API) | REST Compliance, Error Handling, Input Validation, Dokumentasi API |
| TP4 (Database) | Model Design, ORM Usage, Migration, Query Quality |
| TP5 (Testing) | Coverage, Test Quality, TDD Evidence, Edge Cases |
| TP6 (Docker) | Dockerfile Quality, Compose Config, Deployment, Dokumentasi |

### M.3 Rubrik Proyek Akhir

Rubrik detail tersedia di `project-guidelines.md`.

| Komponen | Bobot |
|----------|-------|
| Teknis & Fungsionalitas | 30% |
| Arsitektur & Kualitas Kode | 20% |
| Testing & Coverage | 15% |
| CI/CD & Deployment | 15% |
| Presentasi & Dokumentasi | 10% |
| Teamwork & Scrum Artifacts | 5% |
| AI Usage Log | 5% |

### M.4 Rubrik Responsi

| Aspek | RTS (Minggu 8) | RAS (Minggu 16) |
|-------|---------------|-----------------|
| Format | Live coding di lab, 60 menit | Live coding di lab, 60 menit |
| Cakupan | Setup, Git, Requirements, Full-Stack basics | Full-Stack, Testing, CI/CD, Docker |
| Penilaian | Kebenaran kode (50%), Pemahaman (30%), Kecepatan (20%) | Kebenaran kode (50%), Pemahaman (30%), Kecepatan (20%) |
| AI/Internet | **Tidak diizinkan** | **Tidak diizinkan** |

---

## N. Rekap Dokumen Asesmen Terkait

| Dokumen | Lokasi | Deskripsi |
|---------|--------|-----------|
| Pedoman Praktikum | `00-pedoman-praktikum/pedoman-praktikum-rpl.md` | Aturan umum praktikum |
| RPS | `01-rps/rps-praktikum-rpl.md` | Rencana Pembelajaran Semester |
| RTM | `02-rtm/rtm-praktikum-rpl.md` | Rencana Tugas Mahasiswa |
| Rubrik Laporan | `04-assessments/rubrik-laporan-praktikum.md` | Rubrik detail laporan L1-L13 |
| Rubrik Tugas | `04-assessments/rubrik-tugas.md` | Rubrik detail TP1-TP6 |
| Panduan Proyek | `04-assessments/project-guidelines.md` | Panduan dan rubrik proyek akhir |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
