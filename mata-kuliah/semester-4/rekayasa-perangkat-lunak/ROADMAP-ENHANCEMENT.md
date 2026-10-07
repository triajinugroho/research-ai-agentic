# Roadmap Enhancement — Rekayasa Perangkat Lunak (IF2205 + IF2206)

**Status:** ✅ v2.0 Complete — Enhancement selesai 12 April 2026
**Terakhir diperbarui:** 12 April 2026

### Hasil Enhancement v2.0

| Kategori | v1.0 | v2.0 | Growth |
|----------|------|------|--------|
| Buku Ajar (14 bab) | 3.652 baris | 20.005 baris | 5.5x |
| Modul Mingguan (16 minggu) | 3.140 baris | 12.034 baris | 3.8x |
| Lab Teori (13 lab) | 1.364 baris | 8.282 baris | 6.1x |
| **TOTAL** | **8.156 baris** | **40.321 baris** | **4.9x** |

Target awal ~26.750 baris — hasil aktual **40.321 baris** (150% dari target).

---

## Latar Belakang

Paket mata kuliah v1.0 sudah lengkap secara struktur (79 file Markdown), namun kedalaman konten masih **30-65% lebih dangkal** dibanding mata kuliah referensi (Algoritma Pemrograman & Kecerdasan Buatan/ML) berdasarkan analisis komparatif berikut:

| Kategori | v1.0 Sekarang | Referensi (AlPro/AI-ML) | Target v2.0 |
|----------|--------------|------------------------|-------------|
| Buku Ajar per bab | 187-327 baris | 688-1849 baris | 700-1200 baris |
| Modul Mingguan | 126-307 baris | 578-967 baris | 400-600 baris |
| Lab Teori | 76-142 baris | 200-350 (target) | 200-350 baris |
| Lab Praktikum | 45-257 baris | 240-498 baris | 250-400 baris |
| **Total baris** | **~9.500** | — | **~26.750** |

### Gap Utama per Dimensi

| Dimensi | v1.0 | Referensi | Gap |
|---------|------|-----------|-----|
| Contoh real-world Indonesia per bab | 5 | 35-39 | 86% kurang |
| Code blocks per modul | 2-3 | 10-20+ | Kurang padat |
| AI Corner subsections per bab | 1-2 | 5-10 | Belum merata |
| ASCII diagram per bab | 15 | 36-170 | Jauh kurang |
| Latihan soal per bab | 7-9 | 15-20 | Perlu 2x lipat |
| Latihan di modul mingguan | 0-1 | 3-4 | Hampir tidak ada |
| Lab praktikum terpendek | 46 baris | 200+ | Stub, perlu rewrite |

---

## Rencana Enhancement v2.0

### 56 File yang Perlu Di-enhance

Enhancement hanya mencakup file **konten pembelajaran** — file foundation (RPS, RTM, assessments, README) sudah memadai.

### 8 Batch Eksekusi (Berurutan berdasarkan Prioritas)

#### Batch 1: Buku Ajar Bab 1-4 (Fondasi) — HIGHEST PRIORITY

| File | v1.0 | Target v2.0 | Enhancement Kunci |
|------|------|-------------|-------------------|
| `bab-01-pengantar-rekayasa-perangkat-lunak.md` | 213 | 800 | Software crisis 10+ kasus, SWEBOK v4 15 KA detail, sejarah SE lengkap, etika IEEE/ACM expanded, AI Corner 5+ subsections |
| `bab-02-proses-dan-model-pengembangan-perangkat-lunak.md` | 255 | 850 | Perbandingan 8 model detail, Agile Manifesto deep dive, Scrum framework lengkap, studi kasus Gojek, Sprint simulation |
| `bab-03-requirements-engineering.md` | 213 | 800 | RE process detail, stakeholder analysis, 6+ elicitation techniques, SRS IEEE 830 template lengkap, studi kasus BPJS |
| `bab-04-pemodelan-requirements-dan-analisis.md` | 235 | 800 | Use case full tutorial, user story INVEST detail, acceptance criteria Given-When-Then, product backlog, studi kasus Perpustakaan UAI |

#### Batch 2: Buku Ajar Bab 5-7 (Pengembangan)

| File | v1.0 | Target v2.0 |
|------|------|-------------|
| `bab-05-arsitektur-perangkat-lunak.md` | 327 | 1000 |
| `bab-06-desain-perangkat-lunak-dan-uml.md` | 285 | 950 |
| `bab-07-software-construction-dan-version-control.md` | 272 | 900 |

#### Batch 3: Buku Ajar Bab 8-11 (Penguasaan)

| File | v1.0 | Target v2.0 |
|------|------|-------------|
| `bab-08-software-testing-fundamentals.md` | 264 | 900 |
| `bab-09-advanced-testing-dan-quality-assurance.md` | 217 | 850 |
| `bab-10-devops-dan-continuous-delivery.md` | 295 | 1000 |
| `bab-11-software-maintenance-dan-evolution.md` | 187 | 800 |

#### Batch 4: Buku Ajar Bab 12-14 (Frontier)

| File | v1.0 | Target v2.0 |
|------|------|-------------|
| `bab-12-software-project-management-dan-agile.md` | 230 | 900 |
| `bab-13-ai-augmented-software-engineering.md` | 205 | 1000 |
| `bab-14-proyek-akhir-web-app-end-to-end.md` | 228 | 1200 |

#### Batch 5: Modul Mingguan 1-8

| File | v1.0 | Target v2.0 | Enhancement Kunci |
|------|------|-------------|-------------------|
| `week-01` | 147 | 500 | Definisi SE mendalam, software crisis 5 kasus, SWEBOK 15 KA, etika+Islam, latihan |
| `week-02` | 145 | 500 | 8 model proses, Scrum detail, Sprint ceremony, Kanban board, studi kasus |
| `week-03` | 126 | 480 | RE process, elicitation 6 teknik, SRS IEEE, validasi, studi kasus UMKM |
| `week-04` | 129 | 480 | Use case diagram, user story, acceptance criteria, backlog, MoSCoW |
| `week-05` | 132 | 500 | 5 architectural styles, SOLID detail, 4 GoF patterns, C4 model |
| `week-06` | 240 | 500 | UML 5 diagram types, ERD normalisasi, REST API, SQLAlchemy |
| `week-07` | 221 | 480 | Clean code 10 prinsip, code smells 10+, Git Flow, conventional commits |
| `week-08` | 140 | 280 | Review peta konsep, format UTS, contoh soal diperluas |

#### Batch 6: Modul Mingguan 9-16

| File | v1.0 | Target v2.0 |
|------|------|-------------|
| `week-09` | 268 | 520 |
| `week-10` | 247 | 500 |
| `week-11` | 307 | 550 |
| `week-12` | 271 | 500 |
| `week-13` | 240 | 520 |
| `week-14` | 250 | 500 |
| `week-15` | 137 | 280 |
| `week-16` | 140 | 280 |

#### Batch 7: Lab Teori (13 file) — 76-142 → 200-350 baris

Setiap lab perlu:
- Penjelasan konseptual sebelum langkah-langkah (currently missing)
- Code examples lengkap dan runnable
- Expected output untuk setiap langkah
- Troubleshooting tips
- Screenshot/diagram guidance

#### Batch 8: Lab Praktikum (13 file) — 45-257 → 250-400 baris

Lab 01-07 paling kritis (hanya 45-47 baris — basically stubs):
- Perlu rewrite hampir total menjadi hands-on guides lengkap
- Step-by-step dengan code yang bisa langsung dijalankan di Codespaces
- Setiap lab harus bisa diselesaikan dalam 100 menit

---

## Template Enhancement per Kategori

### Buku Ajar — Setiap Bab Harus Mengandung:

1. **BAB N: JUDUL** + author + course info
2. **Tujuan Pembelajaran** (tabel Sub-CPMK × deskripsi × Bloom's × estimasi waktu)
3. **Peta Konsep Bab** (ASCII diagram)
4. **N.1 - N.5+ Numbered sections** (masing-masing 100-200 baris):
   - Penjelasan konsep mendalam
   - Tabel perbandingan (pro/kontra, tools, techniques)
   - 3-5 code examples per section (Python/JS, lengkap runnable)
   - ASCII diagram untuk setiap konsep visual
   - Contoh real-world Indonesia
   - Tips & Best Practices boxes
5. **Studi Kasus Komprehensif** (walkthrough 50-100 baris)
6. **AI Corner** (5-10 subsections):
   - Prompt Engineering untuk topik ini
   - Worked example: prompt → AI output → evaluasi manusia
   - Ethical considerations
   - Hands-on: "Coba prompt ini, evaluasi hasilnya"
   - Progressive: Basic (Bab 1-4) → Intermediate (5-7) → Advanced (8-11) → Expert (12-14)
7. **Latihan Soal** (15-20 soal):
   - Level Dasar (C1-C2): 5 soal
   - Level Menengah (C3-C4): 5-7 soal
   - Level Mahir (C5-C6): 5-7 soal
8. **Rangkuman** (7-10 poin kunci)
9. **Referensi** (5-8 sumber)
10. **Footer tagline**

### Modul Mingguan — Setiap Modul Harus Mengandung:

1. **Minggu N: Title**
2. **Informasi Modul** (tabel: MK, minggu, topik, CPMK, durasi 150 menit, metode)
3. **Tujuan Pembelajaran** (numbered list, Bloom's verbs)
4. **Materi Pembelajaran** (250-350 baris): konsep detail, 8-12 code examples, 10-15 ASCII diagrams, 10-15 contoh Indonesia, tabel perbandingan, studi kasus mini
5. **Kegiatan Pembelajaran**: Pre-class (20 min) + In-class (110 min) + Post-class (20 min)
6. **Latihan & Diskusi** (3-5 soal bertingkat) — **BARU di v2.0**
7. **Penugasan** (jika ada minggu itu)
8. **Referensi**
9. **Footer**

### Lab (Teori & Praktikum) — Setiap Lab Harus Mengandung:

1. **Header + Informasi Lab** (tabel)
2. **Tujuan** (3-4 objectives, Bloom's verbs)
3. **Konsep Singkat** (30-50 baris pengantar teori) — **BARU di v2.0**
4. **Persiapan** (tools, prerequisites)
5. **Langkah-langkah** (6-8 steps): penjelasan WHY, code lengkap, expected output, troubleshooting
6. **Tantangan Tambahan** (3 challenges bertingkat)
7. **Refleksi & AI Usage Log** reminder
8. **Checklist Penyelesaian**
9. **Footer**

---

## Contoh Real-World Indonesia untuk v2.0

| Perusahaan/Sistem | Konteks SE | Bab Relevan |
|-------------------|-----------|-------------|
| Gojek/GoTo | Microservices architecture, scaling, Agile at scale | 2, 5 |
| Tokopedia | E-commerce platform, A/B testing, CI/CD | 5, 10, 11 |
| Traveloka | API design, payment integration, security | 6, 14 |
| BCA/Bank Mandiri | Security-critical systems, transaction processing | 8, 9 |
| BPJS Kesehatan | Requirements complexity, stakeholder management | 3, 4 |
| TransJakarta | Real-time tracking, queue management | 5, 6 |
| Ruangguru | EdTech platform, user story mapping | 4 |
| Halodoc | Telemedicine, privacy requirements, HIPAA-like | 3, 14 |
| Bukalapak | CI/CD pipeline, deployment strategies | 10, 11 |
| SIPKD (Keuangan Daerah) | Government software, maintenance | 11 |
| MyPertamina | Mobile app, API versioning | 6, 11 |
| Sistem Akademik UAI | Student information system, database design | 6, 14 |

---

## Verification Checklist v2.0

Setelah enhancement selesai:

- [ ] `wc -l` setiap file memenuhi target minimum
- [ ] Setiap bab buku ajar: AI Corner (5+ subsections), Latihan Soal (15+ soal), Studi Kasus, 10+ code blocks
- [ ] Setiap modul mingguan: Latihan & Diskusi section, 8+ code blocks, 10+ contoh Indonesia
- [ ] Setiap lab: Konsep Singkat section, 6+ langkah dengan code, expected output
- [ ] Konsistensi: metadata, CPMK, bobot asesmen, footer tetap benar
- [ ] SWEBOK v4 direferensi di Bab 1
- [ ] AI Corner progressive: Basic → Intermediate → Advanced → Expert
- [ ] Platform: GitHub Codespaces (bukan Google Colab)
- [ ] Bahasa: Indonesia + bilingual technical terms

---

## Estimasi Total

- **56 file** perlu di-enhance
- **~17.600 baris** konten baru perlu ditambahkan
- Total konten v2.0: **~26.750 baris** (dari ~9.500 di v1.0)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
