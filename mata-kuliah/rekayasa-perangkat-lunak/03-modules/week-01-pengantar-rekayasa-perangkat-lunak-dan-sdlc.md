# Minggu 1: Pengantar Rekayasa Perangkat Lunak dan SDLC

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 1 dari 16 |
| **Topik** | Pengantar RPL, SWEBOK v4, Software Crisis, Etika Profesi |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK-1 |
| **Sub-CPMK** | 1.1 (Definisi & prinsip dasar RPL), 1.2 (SWEBOK v4 & etika profesi) |
| **Durasi** | 150 menit (3 × 50 menit) |
| **Metode** | Ceramah interaktif, diskusi kelompok, video |

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menjelaskan** definisi rekayasa perangkat lunak dan perbedaannya dengan programming (C2)
2. **Mengidentifikasi** faktor-faktor yang menyebabkan software crisis dan kebutuhan akan pendekatan SE yang sistematis (C2)
3. **Menjelaskan** 15 Knowledge Areas dalam SWEBOK v4 (2024) dan relevansinya (C2)
4. **Menjelaskan** prinsip etika profesi software engineer berdasarkan ACM/IEEE Code of Ethics dan nilai-nilai Islami (C2)

## Materi Pembelajaran

### 1.1 Apa Itu Rekayasa Perangkat Lunak?

#### 1.1.1 Definisi

> **Rekayasa Perangkat Lunak** (*Software Engineering*) adalah penerapan pendekatan yang **sistematis, disiplin, dan terukur** terhadap pengembangan, pengoperasian, dan pemeliharaan perangkat lunak (IEEE, 2024).

Software Engineering ≠ Programming:

```
┌─────────────────────────────────────────────────────┐
│ Software Engineering                                 │
│  ┌─────────────────────────────────────────┐        │
│  │ Requirements → Design → Construction →   │        │
│  │ Testing → Deployment → Maintenance       │        │
│  │                                          │        │
│  │  ┌──────────────┐                       │        │
│  │  │ Programming  │ ← hanya satu fase!    │        │
│  │  └──────────────┘                       │        │
│  └─────────────────────────────────────────┘        │
│ + Project Management + Quality Assurance + Ethics    │
└─────────────────────────────────────────────────────┘
```

#### 1.1.2 Sejarah dan Software Crisis

- **1968**: Konferensi NATO di Garmisch, Jerman — istilah "Software Engineering" pertama kali muncul
- **Software Crisis**: Proyek terlambat, over-budget, buggy, tidak sesuai kebutuhan
- **Standish Group CHAOS Report**: Hanya ~30% proyek software yang berhasil sepenuhnya
- **Contoh kegagalan terkenal**: Ariane 5 (1996), Healthcare.gov (2013), Boeing 737 MAX MCAS

#### 1.1.3 Warisan Muslim dalam Ilmu Komputer

- **Al-Khwarizmi** (780-850 M): Bapak Algoritma — kata "algorithm" berasal dari namanya. Pendekatan sistematisnya dalam pemecahan masalah matematika adalah fondasi computational thinking.
- **Al-Jazari** (1136-1206 M): Insinyur mekanik — merancang automata dan mesin otomatis, cikal bakal konsep automation yang menjadi inti DevOps.
- **Ibn al-Haytham** (965-1040 M): Bapak Scientific Method — pendekatan empiris yang menjadi dasar software testing.

### 1.2 SWEBOK v4 (2024)

SWEBOK (*Software Engineering Body of Knowledge*) v4 mendefinisikan 15 Knowledge Areas:

| No | Knowledge Area | Deskripsi Singkat |
|----|---------------|-------------------|
| 1 | Software Requirements | Elicitation, analysis, specification, validation |
| 2 | Software Design | Architecture, detailed design, patterns |
| 3 | Software Construction | Coding, debugging, code review |
| 4 | Software Testing | Levels, techniques, automation |
| 5 | Software Maintenance | Corrective, adaptive, perfective, preventive |
| 6 | Software Configuration Management | Version control, change management |
| 7 | Software Engineering Management | Planning, measurement, risk |
| 8 | Software Engineering Process | Process models, improvement |
| 9 | Software Engineering Models & Methods | Modeling, formal methods |
| 10 | Software Quality | QA, metrics, standards |
| 11 | Software Engineering Professional Practice | Ethics, economics, teamwork |
| 12 | Software Engineering Economics | Cost estimation, value |
| 13 | Computing Foundations | Algorithms, data structures, OS |
| 14 | Mathematical Foundations | Logic, discrete math, statistics |
| 15 | Engineering Foundations | Empirical methods, design |

### 1.3 Mengapa Belajar RPL di Era AI?

AI bisa generate code, lalu mengapa perlu belajar SE?

| AI Bisa | AI Tidak Bisa (Peran SE) |
|---------|--------------------------|
| Generate code dari prompt | Memahami kebutuhan stakeholder yang ambigu |
| Suggest code completion | Merancang arsitektur yang scalable & maintainable |
| Find bugs dalam code | Memutuskan trade-off design (security vs performance) |
| Generate unit tests | Memastikan software memenuhi kebutuhan bisnis |
| Explain code | Mengelola tim dan proses pengembangan |
| Refactor code | Bertanggung jawab atas kualitas dan etika software |

### 1.4 Etika Profesi Software Engineer

#### ACM/IEEE Code of Ethics — 8 Prinsip Utama:
1. **PUBLIC** — Bertindak sesuai kepentingan publik
2. **CLIENT & EMPLOYER** — Bertindak sesuai kepentingan klien dan perusahaan
3. **PRODUCT** — Memastikan produk memenuhi standar profesional
4. **JUDGMENT** — Menjaga integritas dan independensi profesional
5. **MANAGEMENT** — Mengelola pengembangan secara etis
6. **PROFESSION** — Memajukan integritas dan reputasi profesi
7. **COLLEAGUES** — Berlaku adil dan mendukung rekan
8. **SELF** — Terus belajar dan mengembangkan diri

#### Perspektif Islam:
- **Amanah**: Kode yang ditulis harus jujur — tidak menyembunyikan bug, tidak memanipulasi data
- **Keadilan (Al-'Adl)**: Software harus accessible dan fair untuk semua pengguna
- **Ihsan**: Berusaha menulis kode yang excellent — clean code sebagai bentuk ihsan

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Membaca overview SWEBOK v4 di [swebok.org](https://www.computer.org/education/bodies-of-knowledge/software-engineering)
- Menonton video "Software Engineering in 2025" (10 menit)

### In-class (120 menit)
| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-30 menit | Pengantar RPL: definisi, sejarah, software crisis | Ceramah interaktif |
| 30-60 menit | SWEBOK v4: 15 Knowledge Areas & relevansi | Ceramah + diskusi |
| 60-90 menit | Diskusi: "Mengapa SE masih relevan di era AI?" | Diskusi kelompok |
| 90-110 menit | Etika profesi SE: ACM/IEEE + perspektif Islam | Ceramah + refleksi |
| 110-120 menit | Q&A dan preview minggu depan | Tanya jawab |

### Post-class (15 menit)
- Refleksi: Tuliskan 3 hal baru yang dipelajari tentang SE
- Preview: Baca pengantar tentang model proses pengembangan software

## Referensi

1. IEEE Computer Society. (2024). *SWEBOK v4*. IEEE.
2. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 1. Pearson.
3. ACM/IEEE. (2015). *Software Engineering Code of Ethics*.
4. Pressman, R. S. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). Chapter 1.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
