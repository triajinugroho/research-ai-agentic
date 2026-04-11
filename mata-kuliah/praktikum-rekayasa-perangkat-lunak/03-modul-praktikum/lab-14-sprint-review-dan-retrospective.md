# Lab 14: Sprint Review dan Retrospective

## Informasi Praktikum

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Praktikum** | 13 dari 13 (Minggu 14) |
| **Topik** | Sprint Review, Demo, Retrospective, Final Deliverables |
| **CPMK** | CPMK-7 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 01-13 dan proyek tim selesai |
| **Referensi Teori** | IF2205 Minggu 14 — Modern SE Trends |

## Tujuan

1. **Melaksanakan** (C3) Sprint Review: demo produk ke stakeholder (dosen + kelas)
2. **Melakukan** (C4) Sprint Retrospective untuk evaluasi proses tim
3. **Menyiapkan** (C3) deliverables akhir proyek (repository, dokumentasi, deployment)
4. **Merefleksikan** (C5) perjalanan belajar sepanjang semester

## Konsep Singkat

### Agile Ceremonies

Dalam Scrum, ada empat **ceremonies** (acara) yang dilakukan setiap sprint:

```
Agile Ceremonies dalam Satu Sprint
====================================

Sprint Planning        Daily Standup        Sprint Review        Sprint Retrospective
(Awal sprint)          (Setiap hari)        (Akhir sprint)       (Akhir sprint)
==============         ==============       ==============       ====================
APA yang akan          APA yang sudah       DEMO produk          EVALUASI proses
dikerjakan?            dikerjakan?          ke stakeholder       tim
                       ADA hambatan?
Backlog -> Sprint      15 menit berdiri     Feedback dari        Start-Stop-Continue
Backlog                                     stakeholder

   |                      |                     |                      |
   +--- Lab 04 -----------+--- Lab sehari-hari --+--- Lab 14 (ini!) ----+
```

Di Lab 14, kita fokus pada dua ceremony terakhir: **Sprint Review** dan **Sprint Retrospective**.

### Sprint Review vs Sprint Retrospective

| Aspek | Sprint Review | Sprint Retrospective |
|-------|--------------|---------------------|
| **Tujuan** | Demo PRODUK ke stakeholder | Evaluasi PROSES tim |
| **Peserta** | Tim + dosen + kelas | Tim saja (internal) |
| **Pertanyaan utama** | "Apa yang sudah selesai?" | "Bagaimana cara kerja kita?" |
| **Output** | Feedback, updated backlog | Action items untuk improvement |
| **Durasi** | 10 menit per tim (di lab ini) | 25 menit per tim |
| **Format** | Demo live + presentasi | Start-Stop-Continue |

### Velocity dan Burndown

**Velocity** mengukur berapa banyak pekerjaan yang diselesaikan tim dalam satu sprint (biasanya dalam story points).

```
Contoh Velocity Calculation:
===========================

Sprint 1: 15 story points selesai dari 20 yang direncanakan
Sprint 2: 18 story points selesai dari 20 yang direncanakan
Sprint 3: 20 story points selesai dari 20 yang direncanakan

Average Velocity = (15 + 18 + 20) / 3 = 17.7 story points/sprint

Insight:
- Tim semakin produktif setiap sprint (15 -> 18 -> 20)
- Untuk sprint berikutnya, rencanakan ~18 story points (realistis)
```

**Burndown Chart** menunjukkan sisa pekerjaan dari waktu ke waktu:
```
Story Points Remaining
30 |*
   |  *
25 |    *
   |      *
20 |        *  *         <- stuck di sini (Sprint 1, ada blocker)
   |              *
15 |                *
   |                  *
10 |                    *
   |                      *
 5 |                        *
   |                          *
 0 +---+---+---+---+---+---+---+---
   W1  W2  W3  W4  W5  W6  W7  W8
                Minggu
```

> **Referensi teori:** Lihat modul IF2205 Minggu 14 — Modern SE Trends untuk pembahasan tentang Agile metrics, continuous improvement, dan software engineering masa depan.

## Persiapan

- Proyek tim sudah ter-deploy di cloud (Railway/Render)
- Semua fitur utama sudah di-merge ke branch `main`
- CI pipeline hijau (semua tests passing)
- Slide presentasi sudah disiapkan (5-7 slide)

**Pre-check sebelum lab dimulai:**
```bash
# Pastikan branch main up-to-date
git checkout main
git pull

# Pastikan semua test PASS
pytest tests/ -v --tb=short

# Pastikan deployment URL masih aktif
curl https://your-app.up.railway.app/health
```

## Langkah-langkah

### Langkah 1: Persiapan Sprint Review (15 menit)

**Mengapa langkah ini penting?** Demo yang tidak dipersiapkan sering berakhir dengan kegagalan teknis di depan stakeholder. Checklist memastikan demo berjalan lancar.

**Checklist sebelum demo:**

```markdown
## Pre-Demo Checklist
- [ ] Deployment URL aktif dan accessible
- [ ] Semua fitur utama berfungsi (test manual quick check)
- [ ] Data demo sudah disiapkan (BUKAN database kosong)
- [ ] CI pipeline hijau — semua tests passing
- [ ] README.md lengkap (deskripsi, setup, API docs)
- [ ] Slide presentasi siap (5-7 slide)
- [ ] Setiap anggota tim tahu bagian yang akan di-demo
- [ ] Backup plan jika demo live gagal (screenshot/video)
```

**5-Minute Demo Script Template:**

Gunakan script ini sebagai panduan agar demo terstruktur dan tidak melebihi waktu:

```markdown
## Demo Script — Tim [Nama Tim]

### [0:00-0:30] Pembukaan
"Selamat [pagi/siang], kami dari Tim [nama]. Anggota tim: [sebutkan nama + peran].
Kami membangun Sistem Perpustakaan Digital UAI yang membantu mahasiswa
mencari dan meminjam buku secara online."

### [0:30-1:30] Problem & Solution
"Masalah: Proses peminjaman buku di perpustakaan UAI masih manual...
Solusi kami: Aplikasi web yang memungkinkan [sebutkan 3 fitur utama]."
[Tampilkan slide arsitektur: Frontend → Backend → Database]

### [1:30-4:00] Demo Live
"Mari kita lihat aplikasinya di [URL production]."
1. [1:30] Halaman login — login sebagai mahasiswa_demo
2. [2:00] Halaman katalog — cari buku "Python"
3. [2:30] Pinjam buku — klik "Pinjam", lihat konfirmasi
4. [3:00] Daftar peminjaman — lihat buku yang sedang dipinjam
5. [3:30] Kembalikan buku — klik "Kembalikan"
[Jika ada waktu: tunjukkan fitur bonus seperti search, filter, pagination]

### [4:00-4:30] Technical Highlights
"Secara teknis, kami menggunakan:"
- Flask + SQLAlchemy + PostgreSQL
- CI/CD: GitHub Actions (lint + test + build)
- Docker + Railway deployment
- Test coverage: ___%

### [4:30-5:00] Penutup
"Terima kasih. Ada pertanyaan?"
```

**Struktur Slide Presentasi:**

| Slide | Konten | Durasi | Tips |
|-------|--------|--------|------|
| 1 | Judul + Nama Tim + Anggota + Peran | 30 detik | Sertakan foto tim jika ada |
| 2 | Problem Statement + User Stories utama | 1 menit | Fokus pada 3 user story terpenting |
| 3 | Arsitektur & Tech Stack (diagram) | 1 menit | Gunakan diagram sederhana, bukan teks |
| 4 | Demo Live (buka browser, bukan slide) | 3-4 menit | Siapkan data demo, jangan database kosong |
| 5 | Testing & CI/CD Pipeline (screenshot) | 30 detik | Tunjukkan badge CI hijau di README |
| 6 | Lessons Learned + AI Usage Summary | 30 detik | 2-3 poin kunci saja |
| 7 | Q&A | 2 menit | Setiap anggota siap menjawab area masing-masing |

### Langkah 2: Sprint Review — Demo (40 menit)

**Mengapa langkah ini penting?** Sprint Review adalah momen akuntabilitas — menunjukkan hasil kerja nyata ke stakeholder. Ini melatih kemampuan presentasi teknis yang penting di dunia kerja.

**Format Demo (per tim, 10 menit):**

**1. Pembukaan (1 menit):**
- Nama tim, anggota, dan peran masing-masing
- Problem statement yang diselesaikan
- Overview singkat solusi

**2. Demo Live (5 menit):**
- Tunjukkan 3-5 user story utama yang sudah selesai
- Demo langsung di URL production (bukan localhost!)
- Tunjukkan happy path untuk setiap fitur
- Tunjukkan error handling (apa yang terjadi jika input salah?)

**3. Technical Highlights (2 menit):**
- Arsitektur (MVC/layered architecture)
- CI/CD pipeline hijau (tunjukkan tab Actions)
- Test coverage (tunjukkan badge atau angka)
- Docker deployment

**4. Q&A (2 menit):**
- Pertanyaan dari dosen dan mahasiswa lain
- Setiap anggota tim harus bisa menjawab tentang area masing-masing

**Rubrik Penilaian Demo:**

| Kriteria | Bobot | 4 (Excellent) | 3 (Good) | 2 (Fair) | 1 (Poor) |
|----------|-------|---------------|----------|----------|----------|
| Fungsionalitas | 30% | Semua fitur utama berjalan, error handling baik | Mayoritas berjalan, minor bug | Sebagian berjalan, beberapa error | Banyak error, fitur utama gagal |
| Technical Quality | 25% | CI hijau, tests >80%, Docker, deployed | CI + tests >70%, deployed | Hanya tests ada, belum deploy | Tidak ada test atau CI |
| Presentasi | 20% | Jelas, terstruktur, sesuai waktu, demo lancar | Cukup jelas, sedikit over-time | Kurang terstruktur, demo bermasalah | Tidak jelas, demo gagal |
| Kerja Tim | 15% | Kontribusi merata, semua bisa menjawab | Mayoritas berkontribusi | Tidak merata, beberapa pasif | 1 orang dominan, lainnya tidak tahu |
| AI Usage | 10% | Log lengkap, kritis, evaluasi mendalam | Log ada, evaluasi cukup | Log ada, minim evaluasi | Tidak ada log |

### Langkah 3: Sprint Retrospective (25 menit)

**Mengapa langkah ini penting?** Retrospective bukan formalitas — ini adalah mekanisme **continuous improvement**. Tim yang melakukan retro secara jujur selalu berkembang lebih baik.

**Fasilitasi Retrospective (Start-Stop-Continue):**

Setiap tim melakukan retrospective internal. Satu anggota menjadi **fasilitator** yang memimpin diskusi:

**Panduan Fasilitator:**
1. (2 menit) Buka dengan icebreaker: "Dalam 1 kata, bagaimana perasaan Anda tentang proyek ini?"
2. (5 menit) **START** — setiap anggota tulis di sticky note (atau kertas): "Apa yang harus kita MULAI lakukan di proyek berikutnya?"
3. (5 menit) **STOP** — "Apa yang harus kita BERHENTI lakukan?"
4. (5 menit) **CONTINUE** — "Apa yang sudah BAIK dan harus dilanjutkan?"
5. (3 menit) Diskusikan dan pilih TOP 3 action items
6. (5 menit) Tulis dokumentasi retrospective

```markdown
## Sprint Retrospective — Tim [Nama Tim]
Tanggal: [tanggal]
Fasilitator: [nama]

### START (Mulai lakukan di proyek berikutnya)
1. ___
2. ___
3. ___

### STOP (Berhenti lakukan)
1. ___
2. ___
3. ___

### CONTINUE (Sudah baik, lanjutkan)
1. ___
2. ___
3. ___

### Velocity & Metrics
- Total user stories planned: ___
- Total user stories completed: ___
- Completion rate: ___%
- Total commits: ___
- Total PRs merged: ___
- Test coverage: ___%
- CI pipeline runs (total): ___
- CI pipeline success rate: ___%
- Bugs found in production: ___

### Top 3 Action Items
1. [Action] — [Penanggung jawab] — [Deadline]
2. [Action] — [Penanggung jawab] — [Deadline]
3. [Action] — [Penanggung jawab] — [Deadline]
```

**Velocity Calculation Exercise:**

Hitung velocity tim Anda:
```
Sprint/Minggu | Story Points Planned | Story Points Completed | Velocity
-------------|---------------------|----------------------|--------
Minggu 9-10  | ___                 | ___                  | ___
Minggu 11-12 | ___                 | ___                  | ___
Minggu 13-14 | ___                 | ___                  | ___
                                                 Average: | ___
```

**Pertanyaan analisis:**
- Apakah velocity meningkat dari sprint ke sprint? Jika ya, mengapa?
- Jika ada sprint dengan velocity rendah, apa penyebabnya?
- Berdasarkan velocity rata-rata, berapa story points realistis untuk sprint berikutnya?

### Langkah 4: Individual Contribution Reflection (10 menit)

**Mengapa langkah ini penting?** Refleksi individual memastikan setiap anggota tim bertanggung jawab atas kontribusinya. Ini juga membantu dosen menilai partisipasi individu secara adil.

**Individual Contribution Reflection Form:**

```markdown
## Refleksi Kontribusi Individual

Nama: ___
Tim: ___
Peran di Tim: ___

### Kontribusi Teknis
- Fitur yang saya kerjakan: ___
- Total commits saya: ___ (dari total ___ commits tim)
- PRs yang saya buat: ___
- PRs yang saya review: ___
- Test yang saya tulis: ___

### Kontribusi Non-Teknis
- Peran saya dalam diskusi/planning: ___
- Bantuan ke anggota tim lain: ___
- Dokumentasi yang saya tulis: ___

### Self-Assessment (1-5 untuk setiap aspek)
| Aspek | Skor | Alasan |
|-------|------|--------|
| Technical skill | _/5 | |
| Teamwork & communication | _/5 | |
| Time management | _/5 | |
| Problem solving | _/5 | |
| AI usage (efektif & etis) | _/5 | |

### Peer Assessment
Berikan skor 1-5 untuk setiap anggota tim lain:

| Anggota | Kontribusi Teknis (1-5) | Kerja Sama (1-5) | Komentar |
|---------|------------------------|-------------------|----------|
| [Nama 1] | | | |
| [Nama 2] | | | |
| [Nama 3] | | | |

### Refleksi Pembelajaran
1. Apa skill terpenting yang saya pelajari semester ini?
   ___
2. Apa tantangan terbesar yang saya hadapi dan bagaimana saya mengatasinya?
   ___
3. Bagaimana pengalaman bekerja dalam tim Agile/Scrum mengubah cara saya bekerja?
   ___
4. Bagaimana AI membantu (dan tidak membantu) proses development saya?
   ___
5. Bagaimana saya menerapkan prinsip amanah dalam proyek ini?
   ___
6. Apa rencana saya untuk mengembangkan skill SE lebih lanjut?
   ___
```

### Langkah 5: Final Repository Cleanup dan Documentation Checklist (10 menit)

**Mengapa langkah ini penting?** Repository adalah deliverable utama proyek. Repository yang rapi dan terdokumentasi menunjukkan profesionalisme dan memudahkan evaluasi.

**Final Documentation Checklist:**

```markdown
## Repository Final Checklist

### Dokumentasi
- [ ] README.md lengkap:
  - [ ] Deskripsi proyek
  - [ ] Screenshot aplikasi
  - [ ] Arsitektur diagram
  - [ ] Setup instructions (docker compose up)
  - [ ] API documentation
  - [ ] Deployment URL
  - [ ] CI badge
- [ ] .env.example (template environment variables)
- [ ] CONTRIBUTING.md (cara kontribusi — opsional)

### Code Quality
- [ ] Tidak ada kode yang di-comment out tanpa alasan
- [ ] Tidak ada hardcoded secrets/passwords (periksa .env, config.py)
- [ ] .gitignore mencakup: .env, __pycache__, node_modules, .coverage
- [ ] Semua branches sudah di-merge atau di-cleanup
- [ ] Tidak ada file besar (>10MB) di repository

### CI/CD & Deployment
- [ ] CI pipeline hijau di branch main
- [ ] Dockerfile valid dan teruji
- [ ] docker-compose.yml valid
- [ ] Production URL accessible dan health check OK

### Testing
- [ ] Test coverage >= 70%
- [ ] Semua tests passing
- [ ] Unit tests + Integration tests ada

### Project Management
- [ ] AI Usage Log lengkap (seluruh semester)
- [ ] Sprint retrospective terdokumentasi
- [ ] Kontribusi setiap anggota terlihat di Git history
```

**Project Handoff Guide:**

Bayangkan developer baru bergabung dengan proyek Anda. Bisakah mereka menjalankan proyek hanya dengan membaca README? Verifikasi:

```bash
# Clone repository
git clone https://github.com/USERNAME/REPO.git
cd REPO

# Setup (mengikuti instruksi di README)
cp .env.example .env
docker compose up -d --build

# Verifikasi
curl http://localhost:5000/health
# Harus return: {"status": "healthy"}

# Jalankan test
docker compose exec web pytest tests/ -v
# Semua test harus PASS
```

Jika langkah-langkah di atas gagal, perbaiki README dan konfigurasi sampai berhasil.

## Tantangan Tambahan

1. **Basic:** Buat video demo 3 menit (screen recording + narasi) untuk portfolio pribadi. Upload ke YouTube (unlisted) atau Google Drive
2. **Intermediate:** Tulis blog post 500 kata tentang pengalaman proyek dan pembelajaran yang diperoleh (di Medium, dev.to, atau Hashnode). Fokus pada satu lesson learned yang paling berharga

## Refleksi dan AI Usage Log

### Pertanyaan Refleksi Akhir Semester

1. Dari 13 lab yang sudah Anda selesaikan, lab mana yang paling berkesan? Mengapa?
2. Apakah proses "belajar sambil mengerjakan proyek" efektif bagi Anda dibandingkan kuliah teori saja?
3. Bagaimana pengalaman menggunakan AI tools (Claude/ChatGPT/Copilot) sepanjang semester? Apakah Anda menjadi terlalu bergantung atau justru belajar lebih efektif?
4. Bagaimana prinsip *amanah* dan nilai-nilai Islami lainnya tercermin dalam cara Anda bekerja di proyek ini?
5. Jika Anda bisa mengulangi semester ini, apa yang akan Anda lakukan berbeda?

### Template AI Usage Log (Semester Summary)

| Lab | AI Tool | Penggunaan Utama | Dampak (positif/negatif) |
|-----|---------|-----------------|-------------------------|
| Lab 09 | | | |
| Lab 10 | | | |
| Lab 11 | | | |
| Lab 12 | | | |
| Lab 13 | | | |
| Lab 14 | | | |

## Checklist Penyelesaian

- [ ] Pre-demo checklist selesai (semua item tercentang)
- [ ] Demo live berhasil (URL production berfungsi)
- [ ] Slide presentasi ter-submit
- [ ] Sprint Retrospective (Start-Stop-Continue) terdokumentasi dengan metrics
- [ ] Velocity dihitung dan dianalisis
- [ ] Individual Contribution Reflection form terisi lengkap
- [ ] Peer assessment terisi untuk setiap anggota tim
- [ ] Repository final sudah di-cleanup dan memenuhi documentation checklist
- [ ] Project handoff diverifikasi (developer baru bisa run dari README)
- [ ] AI Usage Log lengkap untuk seluruh semester
- [ ] Refleksi akhir semester tertulis (5 pertanyaan dijawab)
- [ ] Semua deliverables ter-submit sebelum deadline

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
