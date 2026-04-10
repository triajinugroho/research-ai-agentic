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

## Tujuan

1. **Melaksanakan** Sprint Review: demo produk ke stakeholder (dosen + kelas)
2. **Melakukan** Sprint Retrospective untuk evaluasi proses tim
3. **Menyiapkan** deliverables akhir proyek (repository, dokumentasi, deployment)
4. **Merefleksikan** perjalanan belajar sepanjang semester

## Persiapan

- Proyek tim sudah ter-deploy di cloud (Railway/Render)
- Semua fitur utama sudah di-merge ke branch `main`
- CI pipeline hijau (semua tests passing)
- Slide presentasi (5-7 slide)

## Langkah-langkah

### Langkah 1: Persiapan Sprint Review (15 menit)

**Checklist sebelum demo:**

```markdown
## Pre-Demo Checklist
- [ ] Deployment URL aktif dan accessible
- [ ] Semua fitur utama berfungsi (test manual)
- [ ] Data demo sudah disiapkan (tidak pakai database kosong)
- [ ] CI pipeline hijau — semua tests passing
- [ ] README.md lengkap (deskripsi, setup, API docs)
- [ ] Slide presentasi siap (5-7 slide)
- [ ] Setiap anggota tim tahu bagian yang akan di-demo
```

**Struktur Slide Presentasi:**

| Slide | Konten | Durasi |
|-------|--------|--------|
| 1 | Judul + Nama Tim + Anggota | 30 detik |
| 2 | Problem Statement + User Stories | 1 menit |
| 3 | Arsitektur & Tech Stack | 1 menit |
| 4 | Demo Live (fitur utama) | 3-4 menit |
| 5 | Testing & CI/CD Pipeline | 1 menit |
| 6 | Lessons Learned + AI Usage Summary | 1 menit |
| 7 | Q&A | 2 menit |

### Langkah 2: Sprint Review — Demo (40 menit)

**Format Demo (per tim, 10 menit):**

1. **Pembukaan** (1 menit):
   - Nama tim, anggota, dan peran masing-masing
   - Problem yang diselesaikan

2. **Demo Live** (5 menit):
   - Tunjukkan 3-5 user story utama yang sudah selesai
   - Demo langsung di URL production (bukan localhost)
   - Tunjukkan happy path untuk setiap fitur

3. **Technical Highlights** (2 menit):
   - Arsitektur (MVC/layered)
   - CI/CD pipeline hijau
   - Test coverage
   - Docker deployment

4. **Q&A** (2 menit):
   - Pertanyaan dari dosen dan mahasiswa lain

**Rubrik Penilaian Demo:**

| Kriteria | Bobot | 4 (Excellent) | 3 (Good) | 2 (Fair) | 1 (Poor) |
|----------|-------|---------------|----------|----------|----------|
| Fungsionalitas | 30% | Semua fitur berjalan | Mayoritas berjalan | Sebagian berjalan | Banyak error |
| Technical Quality | 25% | CI hijau, tests, Docker | CI + tests | Hanya tests | Tidak ada |
| Presentasi | 20% | Jelas, terstruktur | Cukup jelas | Kurang terstruktur | Tidak jelas |
| Kerja Tim | 15% | Kontribusi merata | Mayoritas berkontribusi | Tidak merata | 1 orang dominan |
| AI Usage | 10% | Log lengkap, kritis | Log ada, evaluasi | Log ada, minim evaluasi | Tidak ada log |

### Langkah 3: Sprint Retrospective (25 menit)

**Format: Start-Stop-Continue**

Setiap tim melakukan retrospective internal:

```markdown
## Sprint Retrospective — Tim [Nama Tim]
Tanggal: [tanggal]

### 🟢 START (Apa yang harus kita mulai lakukan?)
1. ___
2. ___
3. ___

### 🔴 STOP (Apa yang harus kita berhenti lakukan?)
1. ___
2. ___
3. ___

### 🔵 CONTINUE (Apa yang sudah baik dan harus dilanjutkan?)
1. ___
2. ___
3. ___

### Metrics
- Total commits: ___
- Total PRs merged: ___
- Test coverage: ___%
- CI pipeline runs: ___
- Bugs found in production: ___

### Individual Reflection
[Setiap anggota menulis 2-3 kalimat tentang pembelajaran mereka]

Anggota 1: ___
Anggota 2: ___
Anggota 3: ___
Anggota 4: ___
```

### Langkah 4: Final Repository Cleanup (15 menit)

Pastikan repository proyek memenuhi standar:

```markdown
## Repository Final Checklist

### Dokumentasi
- [ ] README.md lengkap (deskripsi, arsitektur, setup, API docs)
- [ ] CONTRIBUTING.md (cara kontribusi)
- [ ] .env.example (template environment variables)
- [ ] API documentation up-to-date

### Code Quality
- [ ] Tidak ada kode yang di-comment out tanpa alasan
- [ ] Tidak ada hardcoded secrets/passwords
- [ ] .gitignore mencakup .env, __pycache__, node_modules
- [ ] Semua branches sudah di-merge atau di-cleanup

### CI/CD & Deployment
- [ ] CI pipeline hijau di branch main
- [ ] Dockerfile valid
- [ ] docker-compose.yml valid
- [ ] Production URL accessible

### Testing
- [ ] Test coverage ≥ 70%
- [ ] Semua tests passing
- [ ] Unit + Integration tests ada

### Project Management
- [ ] AI Usage Log lengkap
- [ ] Sprint retrospective terdokumentasi
- [ ] Kontribusi setiap anggota terlihat di Git history
```

### Langkah 5: Refleksi Akhir Semester (5 menit)

Tulis refleksi pribadi (di-submit individual):

1. Apa skill SE terpenting yang Anda pelajari semester ini?
2. Bagaimana pengalaman bekerja dalam tim Agile/Scrum?
3. Bagaimana AI membantu (dan tidak membantu) proses development?
4. Bagaimana Anda menerapkan prinsip amanah dalam proyek ini?
5. Apa rencana Anda untuk mengembangkan skill SE lebih lanjut?

## Tantangan Tambahan

1. Buat video demo 3 menit (screen recording + narasi) untuk portfolio
2. Tulis blog post tentang pengalaman proyek (di Medium atau dev.to)

## Checklist Penyelesaian

- [ ] Demo live berhasil (URL production berfungsi)
- [ ] Slide presentasi ter-submit
- [ ] Sprint Retrospective (Start-Stop-Continue) terdokumentasi
- [ ] Repository final sudah di-cleanup dan memenuhi checklist
- [ ] AI Usage Log lengkap untuk seluruh semester
- [ ] Refleksi akhir semester tertulis
- [ ] Semua deliverables ter-submit sebelum deadline

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
