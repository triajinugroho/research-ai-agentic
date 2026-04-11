# Minggu 15: Presentasi Proyek Akhir

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 15 dari 16 |
| **Topik** | Presentasi Proyek Akhir |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK 1-7: Seluruh capaian pembelajaran diintegrasikan dalam proyek akhir |
| **Sub-CPMK** | Sub-CPMK-15.1: Merancang dan mempresentasikan solusi perangkat lunak end-to-end secara profesional (C6) |
| | Sub-CPMK-15.2: Mengevaluasi proyek tim lain melalui peer review yang konstruktif (C5) |
| **Durasi** | 150 menit (3 x 50 menit) |
| **Metode** | Presentasi tim, demo langsung, peer feedback, Q&A |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Mempresentasikan** proyek perangkat lunak secara profesional dengan demo langsung (*live demo*) (C6)
2. **Menjelaskan** keputusan teknis (arsitektur, teknologi, testing) dan proses (Agile/Scrum) yang digunakan (C5)
3. **Mengevaluasi** proyek tim lain berdasarkan kriteria teknis, proses, dan presentasi (C5)
4. **Memberikan** feedback konstruktif melalui peer review (C5)

---

## Materi Pembelajaran

### 15.1 Format Demo Day

Setiap tim memiliki **15 menit** total yang terbagi sebagai berikut:

```
Timeline Presentasi per Tim (15 menit):
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
| 0     | 2        | 8        |11    |13   |15|
+-------+----------+----------+------+-----+--+
|Intro  | LIVE DEMO| Technical |Lesson| Q&A |  |
|tim &  | fitur    | highlights|learn |dosen|  |
|project| utama &  | arsitektur| &    |& mhs|  |
|       | user flow| CI/CD, AI| retro|     |  |
+-------+----------+----------+------+-----+--+
   2 min    6 min      3 min   2 min  2 min
```

| Waktu | Aktivitas | Tips |
|-------|-----------|------|
| 0-2 menit | Perkenalan tim dan overview proyek | Nama, peran setiap anggota, 1 kalimat deskripsi app |
| 2-8 menit | **Live demo** aplikasi -- tunjukkan fitur utama dan user flow | Gunakan skenario nyata, bukan data dummy |
| 8-11 menit | Technical highlights: arsitektur, teknologi, CI/CD, AI usage | Tunjukkan pipeline hijau, test coverage |
| 11-13 menit | Lessons learned dan refleksi Agile/Scrum | Apa yang berjalan baik, apa yang akan diperbaiki |
| 13-15 menit | Q&A dari dosen dan mahasiswa | Setiap anggota harus siap menjawab |

### 15.2 Panduan Presentasi

#### Checklist Deliverables yang Harus Ditunjukkan

```
Demo Day Checklist:
+-- [1] Aplikasi berjalan (LIVE, bukan screenshot)
|   +-- Deploy ke cloud (Railway/Vercel) ATAU jalankan lokal
|   +-- Tunjukkan minimal 3 user flow utama
|   +-- Gunakan data realistis (bukan "test", "abc")
|
+-- [2] Repository GitHub
|   +-- Commit history teratur (bukan 1 commit besar)
|   +-- Branching strategy (main, develop, feature/*)
|   +-- Minimal 5 Pull Request dengan review comments
|
+-- [3] CI/CD Pipeline (GitHub Actions)
|   +-- Workflow berjalan (badge hijau di README)
|   +-- Minimal: lint + test + build
|   +-- Tunjukkan output pipeline
|
+-- [4] Test Suite
|   +-- Jalankan test di demo (pytest/Jest)
|   +-- Coverage >= 70%
|   +-- Tunjukkan coverage report
|
+-- [5] Dokumentasi
|   +-- README.md lengkap (setup, API, architecture)
|   +-- AI Usage Log (per anggota)
|   +-- docs/ folder: SRS, UML, CI/CD docs
|
+-- [6] Proses Agile/Scrum
|   +-- Sprint backlog / GitHub Projects board
|   +-- Retrospective notes
|   +-- Peran: Scrum Master, Product Owner, Developer
```

#### Tips Presentasi Efektif

| Do | Do Not |
|-----|--------|
| Siapkan **backup video** rekaman demo | Andalkan hanya live demo (internet bisa gagal) |
| Fokus pada **value** untuk pengguna | Terlalu banyak jargon teknis tanpa konteks |
| Gunakan **skenario nyata** | Data dummy: "test123", "aaa@bbb.com" |
| Setiap anggota **berbicara** | Satu orang presentasi semua |
| Tunjukkan **proses**, bukan hanya hasil | Skip bagian Agile/Scrum dan lessons learned |
| Latihan **1-2 kali** sebelum Demo Day | Tidak latihan dan overtime saat demo |
| Siapkan **jawaban FAQ** teknis | Tidak bisa menjelaskan arsitektur sendiri |

#### Kesalahan Umum yang Harus Dihindari

```
Common Demo Day Mistakes:
+-- "Di laptop saya jalan kok..."
|   --> Solusi: deploy ke cloud, test sebelum demo
|
+-- "Fitur ini belum selesai, tapi..."
|   --> Solusi: demo yang sudah jadi, jangan yang setengah jadi
|
+-- "Kode ini di-generate AI semua"
|   --> Solusi: pahami setiap baris, bisa jelaskan saat Q&A
|
+-- "Kami tidak sempat buat test"
|   --> Solusi: test wajib ada, minimal unit test fungsi utama
|
+-- Internet mati saat live demo
|   --> Solusi: siapkan video backup, bisa demo lokal
|
+-- Satu anggota tidak bicara sama sekali
|   --> Solusi: bagi bagian presentasi sejak awal
```

### 15.3 Rubrik Penilaian Proyek Akhir

| Kriteria | Bobot | Deskripsi | A (85-100) | B (70-84) | C (55-69) |
|----------|-------|-----------|-----------|-----------|-----------|
| **Fungsionalitas** | 25% | Fitur berjalan sesuai requirements | Semua fitur utama berjalan, UX baik | Sebagian besar fitur jalan | Fitur minimal |
| **Kualitas Kode** | 20% | Clean code, design patterns, testing | Coverage >= 70%, SOLID applied | Coverage >= 50%, kode bersih | Coverage < 50% |
| **Proses SE** | 20% | Agile/Scrum, Git flow, code review, CI/CD | 4 sprint lengkap, pipeline hijau | 3 sprint, CI/CD ada | Sprint tidak teratur |
| **Presentasi** | 15% | Komunikasi, demo, Q&A | Demo lancar, Q&A solid | Demo baik, Q&A cukup | Demo bermasalah |
| **AI Integration** | 10% | Penggunaan AI efektif, bertanggung jawab | AI Usage Log lengkap, reflektif | Log ada, cukup detail | Log minimal |
| **Dokumentasi** | 10% | README, API docs, SRS, UML | Lengkap dan terstruktur | Ada tapi kurang detail | Minimal |
| **Total** | **100%** | | | | |

### 15.4 Peer Review Form

Setiap mahasiswa mengisi **Peer Review Form** untuk **2 tim lain**:

```markdown
## Peer Review Form -- Demo Day IF2205

**Tim yang direview:** _______________
**Nama Reviewer:** _______________
**Tanggal:** _______________

### Penilaian (Skor 1-5)

| Aspek | 1 | 2 | 3 | 4 | 5 | Komentar |
|-------|---|---|---|---|---|----------|
| Fungsionalitas & UX | | | | | | |
| Kualitas teknis (kode, test, CI/CD) | | | | | | |
| Kualitas presentasi & demo | | | | | | |
| Kreativitas & inovasi | | | | | | |
| Kerjasama tim (semua anggota terlibat) | | | | | | |

### Feedback Tertulis

**Satu hal terbaik dari proyek ini:**
_______________________________________________

**Satu saran perbaikan yang konstruktif:**
_______________________________________________

**Fitur yang paling impressive:**
_______________________________________________
```

### 15.5 Sprint 4 -- Final Deliverables

```
Sprint 4 Checklist (sebelum Demo Day):
+-- Code & App
|   +-- Semua fitur utama berfungsi
|   +-- Bug kritis sudah diperbaiki
|   +-- Aplikasi ter-deploy di cloud
|
+-- Testing
|   +-- Unit test coverage >= 70%
|   +-- Integration test untuk flow utama
|   +-- Manual testing untuk edge cases
|
+-- CI/CD
|   +-- GitHub Actions workflow berjalan (hijau)
|   +-- Dockerfile dan docker-compose.yml ada
|   +-- Deploy otomatis ke cloud
|
+-- Documentation
|   +-- README.md (setup instructions, API docs)
|   +-- AI Usage Log (setiap anggota)
|   +-- SRS, UML diagrams (updated)
|   +-- Sprint retrospective notes
|
+-- Presentation
|   +-- Slide presentasi (max 10 slide)
|   +-- Backup video demo (2-3 menit)
|   +-- Pembagian peran presentasi
```

> **Nilai Islami -- Husn al-Zhann (Berprasangka Baik):** Berikan feedback dengan niat membangun. Kritik yang konstruktif (*nasihat*) lebih bermanfaat daripada kritik yang menjatuhkan. Rasulullah SAW mengajarkan: "Agama itu nasihat" (HR. Muslim). Apresiasi usaha tim lain sebagaimana kamu ingin usahamu diapresiasi. Dalam peer review, fokuslah pada perbaikan, bukan penjatuhan.

---

## Kegiatan Pembelajaran

### Pre-class (20 menit)

- Finalisasi slide presentasi (max 10 slide) dan persiapan demo
- Pastikan aplikasi berjalan di environment demo (cloud deployment atau lokal)
- Siapkan backup video demo (rekam screen demo 2-3 menit utama)
- Lakukan dry run presentasi bersama tim (minimal 1 kali)
- Pastikan setiap anggota tahu bagiannya dalam presentasi

### In-class (110 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-5 menit | Penjelasan format, rubrik, dan aturan Demo Day | Briefing |
| 5-95 menit | **Presentasi tim** (6 tim x 15 menit per tim) | Presentasi + Live Demo + Q&A |
| 95-105 menit | Pengisian peer review form untuk 2 tim | Individual |
| 105-110 menit | Closing remarks, pengumuman persiapan UAS Minggu 16, refleksi semester | Diskusi kelas |

### Post-class (20 menit)

- Submit peer review form melalui LMS (deadline: H+1 setelah Demo Day)
- Perbaiki proyek berdasarkan feedback (opsional, untuk portfolio di GitHub)
- Push final version ke repository dengan tag `v1.0.0-final`
- Mulai review materi Minggu 1-14 untuk persiapan UAS Minggu 16
- Siapkan 1 lembar catatan UAS (A4, bolak-balik, tulis tangan)

---

## Referensi

1. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering*, 9th ed. Chapter 3 (Agile Development).
2. Schwaber, K. & Sutherland, J. (2020). *The Scrum Guide*. Scrum.org.
3. Spolsky, J. (2005). "The Joel Test: 12 Steps to Better Code." [joelonsoftware.com](https://www.joelonsoftware.com/)
4. Sommerville, I. (2016). *Software Engineering*, 10th ed. Pearson. Chapter 3-4.
5. Hunt, A. & Thomas, D. (2019). *The Pragmatic Programmer*, 20th Anniversary ed. Addison-Wesley.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
