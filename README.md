# Materi Kuliah — Prodi Informatika UAI

**Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.
**Institusi:** Universitas Al Azhar Indonesia

---

Repository ini berisi **materi kuliah lengkap** untuk enam mata kuliah di Program Studi Informatika, Fakultas Sains dan Teknologi, Universitas Al Azhar Indonesia. Seluruh materi dirancang dengan pendekatan **Outcome-Based Education (OBE)** sesuai SN-Dikti/KKNI, dengan integrasi **AI-Augmented Learning** sebagai pendekatan modern dalam proses belajar-mengajar.

## Mata Kuliah

### Semester Genap 2025/2026 (Tingkat 1)

| Kode | Mata Kuliah | SKS | Tipe | Deskripsi |
|------|-------------|-----|------|-----------|
| INF-101 | [Algoritma dan Pemrograman](mata-kuliah/algoritma-pemrograman/) | 2 | Teori | Fondasi computational thinking dengan Python dan AI |
| INF-102 | [Praktikum Algoritma dan Pemrograman](mata-kuliah/praktikum-algoritma-pemrograman/) | 1 | Praktikum | Hands-on programming lab (ko-requisite INF-101) |
| — | [Analisis Data Statistik](mata-kuliah/analisis-data-statistik/) | 2 | Teori + Lab | Statistika dan analisis data dengan Python |
| IF2205 | [Rekayasa Perangkat Lunak](mata-kuliah/rekayasa-perangkat-lunak/) | 3 | Teori | Full-stack SE Process: SDLC, requirements, design, testing, DevOps |
| IF2206 | [Praktikum Rekayasa Perangkat Lunak](mata-kuliah/praktikum-rekayasa-perangkat-lunak/) | 1 | Praktikum | Hands-on web app development (ko-requisite IF2205) |

### Semester Ganjil 2026/2027 (Tingkat 3)

| Kode | Mata Kuliah | SKS | Tipe | Deskripsi |
|------|-------------|-----|------|-----------|
| IF3XXX | [Kecerdasan Buatan dan Machine Learning](mata-kuliah/kecerdasan-buatan-machine-learning/) | 4 | Teori + Lab | Fondasi AI/ML, supervised/unsupervised learning, deep learning, NLP, CV |

## Struktur Repository

```
mata-kuliah/
├── algoritma-pemrograman/                # INF-101 — 43 file
│   ├── 00-strategic-analysis/            # Analisis SWOT & tren
│   ├── 01-rps/                           # Rencana Pembelajaran Semester
│   ├── 02-rtm/                           # Rencana Tugas Mahasiswa
│   ├── 03-modules/                       # 16 modul mingguan
│   ├── 04-assessments/                   # Framework asesmen, kisi-kisi, naskah UTS & kunci
│   ├── 05-buku-ajar/                     # Buku ajar (14 bab + pendukung)
│   └── datasets/                         # Panduan resource & latihan
│
├── praktikum-algoritma-pemrograman/      # INF-102 — 23 file
│   ├── 00-pedoman-praktikum/             # Pedoman & tata tertib
│   ├── 01-rps/                           # RPS Praktikum
│   ├── 02-rtm/                           # RTM Praktikum
│   ├── 03-modul-praktikum/              # 13 modul praktikum
│   ├── 04-assessments/                   # Rubrik, panduan proyek, naskah UTS & kunci
│   └── datasets/                         # Referensi dataset
│
├── analisis-data-statistik/              # Statistik — 58 file
│   ├── 00-strategic-analysis/            # Analisis strategis
│   ├── 01-rps/                           # RPS
│   ├── 02-rtm/                           # RTM
│   ├── 03-modules/                       # 16 modul mingguan
│   ├── 04-labs/                          # 13 lab hands-on Python
│   ├── 05-assessments/                   # Framework, rubrik, kisi-kisi, naskah UTS & kunci
│   ├── 06-buku-ajar/                     # Buku ajar (14 bab + pendukung)
│   └── datasets/                         # Panduan dataset
│
├── rekayasa-perangkat-lunak/             # IF2205 — 57 file
│   ├── 00-strategic-analysis/            # Analisis SWOT & tren SE
│   ├── 01-rps/                           # RPS
│   ├── 02-rtm/                           # RTM
│   ├── 03-modules/                       # 16 modul mingguan
│   ├── 04-labs/                          # 13 lab teori
│   ├── 05-assessments/                   # Framework, rubrik, kisi-kisi, proyek
│   ├── 06-buku-ajar/                     # Buku ajar (14 bab + pendukung)
│   └── datasets/                         # Panduan resource
│
├── praktikum-rekayasa-perangkat-lunak/   # IF2206 — 22 file
│   ├── 00-pedoman-praktikum/             # Pedoman & tata tertib
│   ├── 01-rps/                           # RPS Praktikum
│   ├── 02-rtm/                           # RTM Praktikum
│   ├── 03-modul-praktikum/              # 13 modul praktikum
│   ├── 04-assessments/                   # Rubrik & panduan proyek
│   └── datasets/                         # Referensi resource
│
└── kecerdasan-buatan-machine-learning/   # IF3XXX — 57 file
    ├── 00-strategic-analysis/            # Analisis SWOT & tren AI/ML
    ├── 01-rps/                           # RPS
    ├── 02-rtm/                           # RTM
    ├── 03-modules/                       # 16 modul mingguan
    ├── 04-labs/                          # 13 lab hands-on (scikit-learn, TensorFlow/Keras)
    ├── 05-assessments/                   # Framework, rubrik, kisi-kisi, proyek
    ├── 06-buku-ajar/                     # Buku ajar (14 bab + pendukung)
    └── datasets/                         # Panduan dataset ML
```

**Total: 264 dokumen Markdown** — mencakup RPS, RTM, modul perkuliahan, buku ajar, lab, asesmen, dan dataset.

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
