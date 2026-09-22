# Materi Kuliah — Prodi Informatika UAI

**Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.
**Institusi:** Universitas Al Azhar Indonesia

---

Repository ini berisi **materi kuliah lengkap** untuk sepuluh mata kuliah di Program Studi Informatika, Fakultas Sains dan Teknologi, Universitas Al Azhar Indonesia. Seluruh materi dirancang dengan pendekatan **Outcome-Based Education (OBE)** sesuai SN-Dikti/KKNI, dengan integrasi **AI-Augmented Learning** sebagai pendekatan modern dalam proses belajar-mengajar.

Empat mata kuliah terbaru — Probabilitas dan Statistik, Dasar Kecerdasan Artifisial dan Pembelajaran Mesin, Teknopreneur, dan Metodologi Penelitian — disusun **langsung dari [Kurikulum Informatika 2025 Revisi 2026](mata-kuliah/00-kurikulum-if-2025-revisi-2026/)**, dengan Sub-CPMK, indikator, kriteria, dan bobot penilaian yang diturunkan verbatim dari registri.

## Mata Kuliah

### Semester Genap 2025/2026 (Tingkat 1)

| Kode | Mata Kuliah | SKS | Tipe | Deskripsi |
|------|-------------|-----|------|-----------|
| INF-101 | [Algoritma dan Pemrograman](mata-kuliah/algoritma-pemrograman/) | 2 | Teori | Fondasi computational thinking dengan Python dan AI |
| INF-102 | [Praktikum Algoritma dan Pemrograman](mata-kuliah/praktikum-algoritma-pemrograman/) | 1 | Praktikum | Hands-on programming lab (ko-requisite INF-101) |
| — | [Analisis Data Statistik](mata-kuliah/analisis-data-statistik/) | 2 | Teori + Lab | Statistika dan analisis data dengan Python |
| IF2205 | [Rekayasa Perangkat Lunak](mata-kuliah/rekayasa-perangkat-lunak/) | 3 | Teori | Full-stack SE Process: SDLC, requirements, design, testing, DevOps |
| IF2206 | [Praktikum Rekayasa Perangkat Lunak](mata-kuliah/praktikum-rekayasa-perangkat-lunak/) | 1 | Praktikum | Hands-on web app development (ko-requisite IF2205) |

### Semester Ganjil 2026/2027 — Kurikulum Informatika 2025 Revisi 2026

Empat mata kuliah berikut disusun mengikuti registri kurikulum terbaru.

| Kode | Mata Kuliah | SKS | Sem | Tipe | Deskripsi |
|------|-------------|-----|-----|------|-----------|
| `IF52510033` | [Probabilitas dan Statistik](mata-kuliah/probabilitas-dan-statistik/) | 3 | 1 | Teori | Fondasi berpikir di bawah ketidakpastian untuk Informatika |
| `IF52510031` | [Dasar Kecerdasan Artifisial dan Pembelajaran Mesin](mata-kuliah/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/) | 3 | 5 | Teori + Lab | Daur hidup ML dari perumusan masalah sampai AI yang bertanggung jawab |
| `ST52510002` | [Teknopreneur](mata-kuliah/teknopreneur/) | 3 | 5 | MKF | Menemukan persoalan, menilai kelayakan, dan mempertanggungjawabkan usaha |
| `IF52510021` | [Metodologi Penelitian](mata-kuliah/metodologi-penelitian/) | 2 | 7 | MKP | Menyusun argumen penelitian yang dapat diperiksa |

> **Catatan pengampu.** Registri kurikulum menetapkan pengampu Metodologi
> Penelitian adalah **Andi Arniaty Arsyad, Ph.D.** (`AAA`), bukan Tri Aji
> Nugroho. Bahan pada folder tersebut berstatus **rujukan penyelarasan
> kurikulum** dan memerlukan persetujuan dosen pengampu sebelum dipakai.

### Semester Ganjil 2026/2027 — Kurikulum Sebelumnya

| Kode | Mata Kuliah | SKS | Tipe | Deskripsi |
|------|-------------|-----|------|-----------|
| IF3XXX | [Kecerdasan Buatan dan Machine Learning](mata-kuliah/kecerdasan-buatan-machine-learning/) | 4 | Teori + Lab | Fondasi AI/ML, supervised/unsupervised learning, deep learning, NLP, CV |

> Folder ini dipertahankan berdampingan dengan `dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/`.
> Keduanya berbeda kurikulum, kode, bobot SKS, arsitektur CPMK, dan skema penilaian.
> Perbandingannya ada pada [README mata kuliah baru](mata-kuliah/dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/README.md).

## Struktur Repository

```
mata-kuliah/
├── 00-kurikulum-if-2025-revisi-2026/     # ★ Referensi kurikulum terbaru — 26 file
│                                         #   Transkripsi Revisi 2026 Kurikulum OBE IF 2025:
│                                         #   PL, CPL, BK, susunan MK, CPMK, Sub-CPMK, bobot penilaian,
│                                         #   AI Curriculum Infusion Matrix
│
├── 00-pedoman-obe/                       # Pedoman & registri OBE internal — 9 file
│
├── algoritma-pemrograman/                # INF-101 — 48 file
│   ├── 00-strategic-analysis/            # Analisis SWOT & tren
│   ├── 01-rps/                           # Rencana Pembelajaran Semester
│   ├── 02-rtm/                           # Rencana Tugas Mahasiswa
│   ├── 03-modules/                       # 16 modul mingguan
│   ├── 04-assessments/                   # Framework asesmen, kisi-kisi, naskah UTS & kunci
│   ├── 05-buku-ajar/                     # Buku ajar (14 bab + pendukung)
│   └── datasets/                         # Panduan resource & latihan
│
├── praktikum-algoritma-pemrograman/      # INF-102 — 24 file
│   ├── 00-pedoman-praktikum/             # Pedoman & tata tertib
│   ├── 01-rps/                           # RPS Praktikum
│   ├── 02-rtm/                           # RTM Praktikum
│   ├── 03-modul-praktikum/              # 13 modul praktikum
│   ├── 04-assessments/                   # Rubrik, panduan proyek, naskah UTS & kunci
│   └── datasets/                         # Referensi dataset
│
├── analisis-data-statistik/              # Statistik — 59 file
│   ├── 00-strategic-analysis/            # Analisis strategis
│   ├── 01-rps/                           # RPS
│   ├── 02-rtm/                           # RTM
│   ├── 03-modules/                       # 16 modul mingguan
│   ├── 04-labs/                          # 13 lab hands-on Python
│   ├── 05-assessments/                   # Framework, rubrik, kisi-kisi, naskah UTS & kunci
│   ├── 06-buku-ajar/                     # Buku ajar (14 bab + pendukung)
│   └── datasets/                         # Panduan dataset
│
├── rekayasa-perangkat-lunak/             # IF2205 — 58 file
│   ├── 00-strategic-analysis/            # Analisis SWOT & tren SE
│   ├── 01-rps/                           # RPS
│   ├── 02-rtm/                           # RTM
│   ├── 03-modules/                       # 16 modul mingguan
│   ├── 04-labs/                          # 13 lab teori
│   ├── 05-assessments/                   # Framework, rubrik, kisi-kisi, proyek
│   ├── 06-buku-ajar/                     # Buku ajar (14 bab + pendukung)
│   └── datasets/                         # Panduan resource
│
├── praktikum-rekayasa-perangkat-lunak/   # IF2206 — 23 file
│   ├── 00-pedoman-praktikum/             # Pedoman & tata tertib
│   ├── 01-rps/                           # RPS Praktikum
│   ├── 02-rtm/                           # RTM Praktikum
│   ├── 03-modul-praktikum/              # 13 modul praktikum
│   ├── 04-assessments/                   # Rubrik & panduan proyek
│   └── datasets/                         # Referensi resource
│
├── kecerdasan-buatan-machine-learning/   # IF3XXX — 57 file (kurikulum sebelumnya)
│   ├── 00-strategic-analysis/            # Analisis SWOT & tren AI/ML
│   ├── 01-rps/ 02-rtm/ 03-modules/       # RPS, RTM, 16 modul mingguan
│   ├── 04-labs/                          # 13 lab hands-on (scikit-learn, TensorFlow/Keras)
│   ├── 05-assessments/ 06-buku-ajar/     # Asesmen, buku ajar (14 bab + pendukung)
│   └── datasets/                         # Panduan dataset ML
│
│   ── Kurikulum Informatika 2025 Revisi 2026 ──────────────────────
│
├── probabilitas-dan-statistik/           # IF52510033 — 57 file
│   ├── 00-strategic-analysis/            # Analisis strategis
│   ├── 01-rps/ 02-rtm/ 03-modules/       # RPS, RTM, 16 modul mingguan
│   ├── 04-labs/                          # 13 lab (scipy.stats, pandas)
│   ├── 05-assessments/                   # Framework, rubrik, kisi-kisi, proyek
│   ├── 06-buku-ajar/                     # Buku ajar (14 bab + lampiran tabel statistik)
│   └── datasets/                         # Panduan dataset
│
├── dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/   # IF52510031 — 57 file
│   ├── 00-strategic-analysis/            # Analisis strategis
│   ├── 01-rps/ 02-rtm/ 03-modules/       # RPS, RTM, 16 modul mingguan
│   ├── 04-labs/                          # 13 lab (scikit-learn)
│   ├── 05-assessments/ 06-buku-ajar/     # Asesmen, buku ajar (14 bab + pendukung)
│   └── datasets/                         # Panduan dataset ML
│
├── teknopreneur/                         # ST52510002 — 57 file
│   ├── 00-strategic-analysis/            # Analisis strategis
│   ├── 01-rps/ 02-rtm/ 03-modules/       # RPS, RTM, 16 modul mingguan
│   ├── 04-labs/                          # 13 studio (kerja lapangan, tanpa pemrograman)
│   ├── 05-assessments/ 06-buku-ajar/     # Asesmen, buku ajar (14 bab + pendukung)
│   └── datasets/                         # Sumber data pasar & UMKM
│
└── metodologi-penelitian/                # IF52510021 — 57 file
    │                                     # ⚠ pengampu registri: Andi Arniaty Arsyad, Ph.D.
    ├── 00-strategic-analysis/            # Analisis strategis
    ├── 01-rps/ 02-rtm/ 03-modules/       # RPS, RTM, 16 modul mingguan
    ├── 04-labs/                          # 13 lokakarya
    ├── 05-assessments/ 06-buku-ajar/     # Asesmen, buku ajar (14 bab + pendukung)
    └── datasets/                         # Sumber pustaka & data penelitian
```

**Total: 535 dokumen Markdown** — mencakup referensi kurikulum, RPS, RTM, modul perkuliahan, buku ajar, lab, asesmen, dan dataset.

## Referensi Kurikulum Terbaru

Folder [`mata-kuliah/00-kurikulum-if-2025-revisi-2026/`](mata-kuliah/00-kurikulum-if-2025-revisi-2026/) berisi transkripsi **Revisi 2026 atas Kurikulum OBE Informatika 2025** — rujukan resmi terbaru untuk seluruh penyusunan RPS, modul, buku ajar, dan asesmen di repositori ini: 5 Profil Lulusan, 11 CPL, 19 Bahan Kajian, 58 mata kuliah (144 SKS), 26 CPMK, dan 154 Sub-CPMK lengkap dengan bobot penilaiannya.

> **Perhatian.** Kurikulum baru mengubah kode mata kuliah, arsitektur CPMK, dan skema bobot penilaian. Empat mata kuliah Semester Ganjil 2026/2027 di atas **sudah** disusun mengikutinya; materi mata kuliah Semester Genap 2025/2026 **belum** disesuaikan. Rincian dampak dan usulan tindak lanjut ada pada [`91-validasi-dan-catatan-dampak.md`](mata-kuliah/00-kurikulum-if-2025-revisi-2026/91-validasi-dan-catatan-dampak.md).

### Ciri Mata Kuliah yang Sudah Selaras

| Ciri | Penerapannya |
|------|--------------|
| CPMK tingkat prodi | Pembedaan antarmata kuliah terjadi pada tingkat **Sub-CPMK** |
| Enam teknik penilaian baku | Partisipasi, Kuis, Observasi, Unjuk Kerja, UTS, UAS — berjumlah tepat 100% |
| Verbatim dari registri | Rumusan Sub-CPMK, indikator, kriteria, dan bobot tidak diubah |
| AI Curriculum Infusion Matrix | Tahap, mode, pilar, dan peran AI dinyatakan pada RPS dan buku ajar |
| Ketertelusuran | Setiap klaim, kriteria, dan ambang dapat ditunjuk sumbernya |

## Pendekatan Pembelajaran

- **OBE (Outcome-Based Education)** — Setiap modul, tugas, dan asesmen diturunkan dari CPMK yang terukur
- **AI-Augmented Learning** — AI (ChatGPT, Claude, Copilot) diintegrasikan sebagai coding partner dan co-analyst
- **Konteks Indonesia** — Dataset BPS, kasus lokal, dan skenario berbasis masalah nyata Indonesia
- **Islamic Values** — Etika, kejujuran akademik, dan tanggung jawab sosial dalam penggunaan teknologi

## Tools & Teknologi

| Tool | Fungsi |
|------|--------|
| Python 3.x | Bahasa pemrograman utama |
| Google Colab | Cloud IDE untuk praktikum AlPro & Statistik |
| GitHub Codespaces | Cloud IDE untuk praktikum RPL |
| pandas, numpy, matplotlib, seaborn | Manipulasi data & visualisasi |
| scipy, scikit-learn | Statistik & machine learning |
| TensorFlow/Keras | Deep learning framework |
| NLTK, OpenCV | NLP & Computer Vision |
| ChatGPT / Claude / Copilot | AI sebagai mitra belajar (wajib AI Usage Log) |

## Lisensi

(c) 2026 Tri Aji Nugroho — Universitas Al Azhar Indonesia

Materi ini dikembangkan untuk keperluan pendidikan di lingkungan UAI.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
