# Audit Keselarasan IF2205 × IF2206

**Tanggal:** 11 April 2026 (audit) → 12 April 2026 (semua resolved)
**Cakupan:** Seluruh file foundation (RPS, RTM, Pedoman, Assessment Framework, Rubrik, Project Guidelines)
**Tujuan:** Memastikan sinkronisasi sebelum eksekusi enhancement v2.0
**Status:** ✅ Semua 13 inkonsistensi telah diperbaiki (Fase 0 selesai 11 April 2026). Enhancement v2.0 IF2205 + IF2206 selesai 12 April 2026.

---

## Ringkasan Eksekutif

Ditemukan **13 inkonsistensi**, termasuk **5 inkonsistensi kritis** yang harus diperbaiki sebelum enhancement, karena jika tidak, enhancement akan memperlebar gap-nya. Inkonsistensi terjadi di 3 level:

1. **Antar-MK** (IF2205 vs IF2206) — 6 temuan
2. **Dalam IF2205** (antar-dokumen) — 4 temuan
3. **Dalam IF2206** (antar-dokumen) — 3 temuan

---

## ISU #1: Sprint Timeline — 4 Versi Berbeda ⚠️ KRITIS

Ada **4 timeline sprint yang saling bertentangan** di 4 dokumen berbeda:

### Versi A — IF2205 RTM (rtm-rekayasa-perangkat-lunak.md)
| Sprint | Minggu | Fokus |
|--------|--------|-------|
| Sprint 0 | 5-6 | Planning |
| Sprint 1 | 7-9 | MVP |
| Sprint 2 | 10-11 | Features |
| Sprint 3 | 12-13 | Quality |
| Sprint 4 | 14 | Polish |

### Versi B — IF2205 Project Guidelines (project-guidelines.md)
| Sprint | Minggu | Fokus |
|--------|--------|-------|
| Sprint 1 | 5-7 | Requirements + Design |
| Sprint 2 | 9-10 | Core Development |
| Sprint 3 | 11-12 | Testing + CI/CD |
| Sprint 4 | 13-14 | Polish + Deploy |

### Versi C — IF2206 RTM (rtm-praktikum-rekayasa-perangkat-lunak.md)
| Sprint | Minggu | Fokus |
|--------|--------|-------|
| Sprint 1 | 5-7 | Frontend + Backend dasar |
| Sprint 2 | 9-10 | Backend + Database |
| Sprint 3 | 11-12 | Testing + CI/CD |
| Sprint 4 | 13-14 | Deployment + Polish |

### Versi D — IF2206 Project Guidelines (project-guidelines.md)
| Sprint | Minggu | Fokus |
|--------|--------|-------|
| Sprint 1 | 5-6 | Frontend + Backend |
| Sprint 2 | 7+9 | Database + Integration |
| Sprint 3 | 10-11 | Testing + CI/CD |
| Sprint 4 | 12-13 | Deploy + Polish |

### Rekomendasi
Tetapkan **SATU timeline sprint** yang digunakan di semua dokumen. Rekomendasi berdasarkan keselarasan terbaik dengan jadwal mingguan:

| Sprint | Minggu | IF2205 Fokus (Teori) | IF2206 Fokus (Praktikum) |
|--------|--------|---------------------|--------------------------|
| Sprint 0 | 5-6 | Requirements + Design | Frontend + Backend awal |
| Sprint 1 | 7 + 9 | Construction + Testing awal | Database + Integration |
| Sprint 2 | 10-11 | Advanced Testing + CI/CD | Testing suite + CI/CD pipeline |
| Sprint 3 | 12-13 | Maintenance + AI-Augmented | Docker deployment + AI pair programming |
| Sprint 4 | 14 | Polish + Dokumentasi | Sprint review + Retrospective |
| Demo | 15 | Presentasi | Demo |

---

## ISU #2: Skala Penilaian — 4 Versi Berbeda ⚠️ KRITIS

### IF2205 RPS (7 tingkat, tanpa A- dan B-)
| Huruf | Rentang |
|-------|---------|
| A | 85-100 |
| B+ | 77-84 |
| B | 70-76 |
| C+ | 63-69 |
| C | 55-62 |
| D | 45-54 |
| E | 0-44 |

### IF2205 Assessment Framework (9 tingkat)
| Huruf | Rentang |
|-------|---------|
| A | ≥ 85 |
| A- | 80-84 |
| B+ | 75-79 |
| B | 70-74 |
| B- | 65-69 |
| C+ | 60-64 |
| C | 55-59 |
| D | 45-54 |
| E | < 45 |

### IF2206 RPS (9 tingkat, batas bawah A = 80)
| Huruf | Rentang |
|-------|---------|
| A | 80-100 |
| A- | 75-79 |
| B+ | 70-74 |
| B | 65-69 |
| B- | 60-64 |
| C+ | 55-59 |
| C | 50-54 |
| D | 40-49 |
| E | < 40 |

### IF2206 Pedoman (9 tingkat, batas bawah A = 85)
| Huruf | Rentang |
|-------|---------|
| A | 85-100 |
| A- | 80-84 |
| B+ | 75-79 |
| B | 70-74 |
| B- | 65-69 |
| C+ | 60-64 |
| C | 55-59 |
| D | 40-54 |
| E | 0-39 |

### Rekomendasi
Pilih SATU skala untuk kedua MK. Rekomendasi mengikuti standar UAI (jika ada) atau gunakan yang 9 tingkat konsisten. Perlu keputusan dosen apakah batas A = 80 atau 85.

---

## ISU #3: Rubrik Proyek Akhir — 3 Versi Berbeda ⚠️ KRITIS

Proyek akhir adalah **proyek yang sama** untuk IF2205 dan IF2206, tapi rubriknya berbeda di 3 dokumen:

### IF2205 RTM
| Komponen | Bobot |
|----------|-------|
| Problem Formulation & Design | 10% |
| Code Implementation | 20% |
| Architecture & Design | 15% |
| Testing | 10% |
| CI/CD & Deployment | 10% |
| Documentation | 10% |
| **AI Usage Documentation** | **15%** |
| Presentation & Demo | 10% |

### IF2205 Project Guidelines
| Komponen | Bobot |
|----------|-------|
| Requirements & Design | 15% |
| Implementation | 25% |
| Testing | 15% |
| DevOps | 10% |
| Presentation & Demo | 10% |
| Teamwork | 10% |
| Documentation | 10% |
| **AI Integration** | **5%** |

### IF2206 Pedoman
| Komponen | Bobot |
|----------|-------|
| Teknis & Fungsionalitas | 30% |
| Arsitektur & Desain | 25% |
| Kualitas Kode & Testing | 20% |
| Presentasi & Dokumentasi | 15% |
| Kreativitas & Inovasi | 10% |

### Rekomendasi
Karena proyek sama, rubrik harus **satu**, tapi bisa diberi bobot berbeda per MK:
- IF2205 menekankan: Requirements, Design, Documentation, AI Usage (sisi teori/konseptual)
- IF2206 menekankan: Implementation, Testing, CI/CD, Deployment (sisi hands-on)

Rubrik boleh berbeda dimensi, tapi harus **eksplisit** bahwa keduanya menilai proyek yang sama dari perspektif berbeda.

---

## ISU #4: Deadline Tugas Pemrograman IF2206 — 3 Versi Berbeda ⚠️ KRITIS

| Tugas | RTM (rtm-praktikum) | Rubrik (rubrik-tugas) | Pedoman (jadwal) |
|-------|---------------------|----------------------|-------------------|
| TP1 | Minggu 3 | Minggu 2 | Minggu 2 (T1) |
| TP2 | Minggu 4 | Minggu 3 | Minggu 4 (T2) |
| TP3 | Minggu 8 | Minggu 7 | Minggu 5 (T3) |
| TP4 | Minggu 10 | Minggu 9 | Minggu 7 (T4) |
| TP5 | Minggu 12 | Minggu 11 | Minggu 10 (T5) |
| TP6 | Minggu 14 | Minggu 13 | Minggu 11 (T6) |

### Rekomendasi
Tetapkan SATU set deadline. Rekomendasi: deadline = minggu setelah lab terkait selesai (beri waktu 1 minggu):

| Tugas | Topik | Lab Terkait | Deadline |
|-------|-------|-------------|----------|
| TP1 | Flask Hello World | Lab 01 (W1) | Minggu 3 |
| TP2 | Git Branching & PR | Lab 02 (W2) | Minggu 4 |
| TP3 | REST API CRUD | Lab 06 (W6) | Minggu 8 (sebelum RTS) |
| TP4 | Database CRUD + ORM | Lab 07 (W7) | Minggu 10 |
| TP5 | Testing Suite | Lab 09-10 (W9-10) | Minggu 12 |
| TP6 | Docker + Deployment | Lab 12 (W12) | Minggu 14 |

---

## ISU #5: CPMK Mapping Tugas IF2206 Tidak Konsisten ⚠️ KRITIS

| Tugas | RTM | Rubrik Tugas |
|-------|-----|-------------|
| TP1 | CPMK-1, **CPMK-4** | CPMK-1 |
| TP2 | **CPMK-2** | **CPMK-1** |
| TP3 | **CPMK-4** | **CPMK-3** |

### Rekomendasi
Sesuaikan dengan isi tugas:
- TP1 (Flask Hello World): CPMK-1 (Setup & Tools) + CPMK-4 (Full-Stack) → benar di RTM
- TP2 (Git Branching): CPMK-2 (Version Control) → benar di RTM
- TP3 (REST API): CPMK-4 (Full-Stack) → benar di RTM

Rubrik tugas perlu diperbaiki mengikuti RTM.

---

## ISU #6: CPL Coding System Berbeda

IF2205 menggunakan: CPL-S2, CPL-KU2, CPL-KK1, CPL-KK4, CPL-P2, CPL-P3 (kode KKNI: S=Sikap, KU=Keterampilan Umum, KK=Keterampilan Khusus, P=Pengetahuan)

IF2206 menggunakan: CPL-1, CPL-2, CPL-3, CPL-4, CPL-5, CPL-6 (numbering sederhana)

### Rekomendasi
Gunakan **satu sistem**. Karena IF2205 sudah menggunakan kode KKNI yang lebih formal dan sesuai SN-Dikti, IF2206 sebaiknya menyesuaikan atau minimal ada **tabel pemetaan** antara CPL-1..6 ke CPL-S/KU/KK/P.

---

## ISU #7: Late Policy Berbeda

### IF2205 (Assessment Framework)
- 1 hari: -10%
- 2-3 hari: -25%
- >3 hari: nilai 0

### IF2206 (Assessment Framework)
- ≤1 hari: -10%
- 2-3 hari: -25%
- 4-7 hari: -50%
- >7 hari: nilai 0

### IF2206 (Pedoman Praktikum)
- Keterlambatan: -10% **per hari** (berbeda dari assessment framework sendiri!)

### Rekomendasi
Seragamkan. Rekomendasi: gunakan versi IF2206 assessment framework (gradual) untuk kedua MK, karena lebih fair dan terstruktur. Perbaiki pedoman agar konsisten.

---

## ISU #8: Sanksi Kehadiran IF2206 Kontradiktif

### IF2206 Pedoman (Section 3.1)
> Kehadiran < 75% → mendapat **nilai E**

### IF2206 Assessment Framework (Section D)
> Kehadiran < 75% → tidak bisa ikut RAS, nilai **maksimal D**

### Rekomendasi
Pilih satu. "Nilai E" lebih ketat dari "maksimal D". Rekomendasi: **tidak bisa ikut RAS dan nilai maksimal D** (lebih proporsional, karena mahasiswa masih bisa lulus jika komponen lain baik).

---

## ISU #9: AI Usage Log Format Berbeda dalam IF2206

### IF2206 Pedoman (Section 6, template laporan)
Tabel 7 kolom: No | Tanggal | Tool AI | Prompt | Output AI | Evaluasi Mahasiswa | Keputusan

### IF2206 RTM (Section D)
Format 4 poin naratif:
1. Tool yang digunakan
2. Prompt yang diberikan
3. Output yang digunakan
4. Modifikasi yang dilakukan

### IF2205 RTM (Rubrik T1)
Dimensi AI Usage Log: "prompt, output, modifikasi, refleksi" (4 elemen, tapi ada "refleksi")

### Rekomendasi
Tetapkan SATU template. Rekomendasi: gunakan tabel 7 kolom dari pedoman (lebih terstruktur), tapi tambahkan kolom "Refleksi" sehingga menjadi 8 kolom. Template ini dirujuk dari semua dokumen.

---

## ISU #10: Tugas IF2205 T4 — Topik Berbeda

### IF2205 RTM
T4: **Test Plan & Unit Test Suite** (CPMK-5, Minggu 9)

### IF2205 Rubrik Tugas
T4: **Collaborative Coding & Code Review** (mengukur Git log, code quality, PR & review, conventional commits)

### Rekomendasi
Ini bukan hanya inkonsistensi nama — ini dua tugas yang berbeda total. RTM mengatakan testing, rubrik mengatakan collaborative coding. Perlu diputuskan:
- Jika T4 = Testing → rubrik perlu ditulis ulang
- Jika T4 = Collaborative Coding → RTM perlu dikoreksi

Rekomendasi: **T4 = Test Plan & Unit Test Suite** (sesuai RTM), karena collaborative coding sudah tercakup di kegiatan Lab 07 dan proyek akhir. Rubrik tugas perlu diperbaiki.

---

## ISU #11: Tugas IF2205 T5/T6 vs Rubrik — Topik Berbeda

### IF2205 RTM
- T5: CI/CD Pipeline Configuration (CPMK-6, Minggu 11)
- T6: AI-Augmented Code Review Report (CPMK-7, Minggu 13)

### IF2205 Rubrik Tugas
- T5: Testing Strategy (mengukur coverage, test quality, TDD, dokumentasi)
- T6: DevOps Pipeline (mengukur CI/CD, Docker, deployment, dokumentasi)

### Rekomendasi
RTM menyebut:
- T4 = Testing, T5 = CI/CD, T6 = AI Review

Rubrik menyebut:
- T4 = Collaborative Coding, T5 = Testing, T6 = DevOps

Jadi rubrik **geser 1 nomor** dari T4 (harusnya T5 = Testing di rubrik = T4 di RTM). Ini kemungkinan error saat penulisan. **Perbaiki rubrik agar sesuai RTM.**

---

## ISU #12: IF2205 RPS Durasi K2 vs RTM

### IF2205 RTM
K2: 30 menit, 10 PG + 2 uraian (5 poin) = 40 poin

### IF2205 Rubrik Tugas
K2: 20 menit, 10 PG + 2 uraian singkat

### Rekomendasi
Seragamkan. Rekomendasi: 30 menit (konsisten dengan K1).

---

## ISU #13: Proyek Akhir — Milestone IF2206 Pedoman vs Project Guidelines

### IF2206 Pedoman (Section 8.3)
| Minggu | Milestone |
|--------|-----------|
| 10 | Proposal |
| 12 | Progress Report |
| 15 | Final Submission |

### IF2206 Project Guidelines
| Sprint | Minggu | Fokus |
|--------|--------|-------|
| Sprint 1 | 5-6 | Frontend + Backend |
| Sprint 2 | 7+9 | Database + Integration |
| Sprint 3 | 10-11 | Testing + CI/CD |
| Sprint 4 | 12-13 | Deploy + Polish |

### Rekomendasi
Pedoman mengatakan proposal baru minggu 10, tapi project guidelines sudah coding sejak minggu 5. Ini kontradiksi. **Sesuaikan pedoman**: proposal harus sebelum Sprint 1 (paling lambat Minggu 5), bukan Minggu 10.

---

## Matriks Perbaikan: File Mana Perlu Diubah

| Isu | File yang Perlu Diperbaiki | Prioritas |
|-----|---------------------------|-----------|
| #1 Sprint Timeline | IF2205: RTM, project-guidelines · IF2206: RTM, project-guidelines | KRITIS |
| #2 Skala Penilaian | IF2205: RPS, assessment-framework · IF2206: RPS, pedoman, assessment | KRITIS |
| #3 Rubrik Proyek | IF2205: RTM, project-guidelines · IF2206: pedoman | KRITIS |
| #4 Deadline TP | IF2206: RTM, rubrik-tugas, pedoman | KRITIS |
| #5 CPMK TP | IF2206: rubrik-tugas | KRITIS |
| #6 CPL Coding | IF2206: RPS | MEDIUM |
| #7 Late Policy | IF2205: assessment · IF2206: pedoman, assessment | MEDIUM |
| #8 Sanksi Kehadiran | IF2206: pedoman ATAU assessment | LOW |
| #9 AI Log Format | IF2206: RTM · IF2205: RTM | MEDIUM |
| #10 T4 Topik | IF2205: rubrik-tugas | KRITIS |
| #11 T5/T6 Topik | IF2205: rubrik-tugas | KRITIS |
| #12 Durasi K2 | IF2205: rubrik-tugas | LOW |
| #13 Milestone PA | IF2206: pedoman | MEDIUM |

### Total file yang perlu diperbaiki: 12 file unik

| # | File | Jumlah Isu |
|---|------|-----------|
| 1 | `rekayasa-perangkat-lunak/02-rtm/rtm-rekayasa-perangkat-lunak.md` | #1, #3, #9 |
| 2 | `rekayasa-perangkat-lunak/05-assessments/project-guidelines.md` | #1, #3 |
| 3 | `rekayasa-perangkat-lunak/05-assessments/rubrik-tugas.md` | #10, #11, #12 |
| 4 | `rekayasa-perangkat-lunak/05-assessments/assessment-framework.md` | #2, #7 |
| 5 | `rekayasa-perangkat-lunak/01-rps/rps-rekayasa-perangkat-lunak.md` | #2 |
| 6 | `praktikum-rekayasa-perangkat-lunak/02-rtm/rtm-praktikum-rekayasa-perangkat-lunak.md` | #1, #4, #5, #9 |
| 7 | `praktikum-rekayasa-perangkat-lunak/04-assessments/project-guidelines.md` | #1, #3 |
| 8 | `praktikum-rekayasa-perangkat-lunak/04-assessments/rubrik-tugas.md` | #4, #5 |
| 9 | `praktikum-rekayasa-perangkat-lunak/04-assessments/assessment-framework-praktikum.md` | #2, #7, #8 |
| 10 | `praktikum-rekayasa-perangkat-lunak/00-pedoman-praktikum/pedoman-praktikum.md` | #2, #7, #8, #13 |
| 11 | `praktikum-rekayasa-perangkat-lunak/01-rps/rps-praktikum-rekayasa-perangkat-lunak.md` | #2, #6 |
| 12 | `praktikum-rekayasa-perangkat-lunak/README.md` | (update setelah perbaikan) |

---

## Dampak terhadap Enhancement v2.0

Jika enhancement dieksekusi **tanpa memperbaiki inkonsistensi ini dulu**:

1. **Lab modules** yang di-enhance akan merujuk sprint timeline yang salah
2. **Rubrik** yang diperdalam akan memperbesar inkonsistensi (karena menambah detail pada data yang salah)
3. **Buku ajar** yang mereferensi proyek akhir akan merujuk rubrik/timeline yang berbeda-beda
4. **Modul mingguan** akan merujuk deadline tugas yang salah

### Urutan Eksekusi yang Benar

```
FASE 0: Sinkronisasi Foundation (12 file) ← HARUS DULUAN
   └─ Perbaiki 13 inkonsistensi di file foundation
   
FASE 1: Enhancement IF2205 (Batch 1-7)
   └─ Buku ajar, modul, lab teori
   
FASE 2: Enhancement IF2206 (Batch P1-P5)
   └─ Lab praktikum, rubrik, assessment
```

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
