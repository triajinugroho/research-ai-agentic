# Rekayasa Perangkat Lunak

## MK Teori — IF2XXX

## Membangun Sistem Berkualitas dengan Pendekatan Modern dan AI-Augmented

**Prodi Informatika — Universitas Al Azhar Indonesia**
**Semester Genap 2025/2026**

*Dosen Pengampu: Tri Aji Nugroho, S.T., M.T.*

---

## Filosofi Desain

```
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│  Fondasi RPL    │ + │ Kualitas &      │ + │ AI-Augmented SE │
│                 │   │ Pengujian       │   │                 │
│ - SDLC          │   │ - Clean Code    │   │ - AI Code Review│
│ - Requirements  │   │ - Testing       │   │ - AI Testing    │
│ - UML           │   │ - CI/CD         │   │ - Ethics        │
│ - Architecture  │   │ - Git           │   │                 │
└────────┬────────┘   └────────┬────────┘   └────────┬────────┘
         │                     │                     │
         └─────────────────────┼─────────────────────┘
                               ▼
              ┌──────────────────────────────┐
              │ Future-Proof Software Engineer│
              └──────────────────────────────┘
```

Mata kuliah ini dirancang dengan filosofi sebagai berikut:

- **Outcome-Based Education (OBE):** Setiap pertemuan, praktikum, dan asesmen dirancang
  berdasarkan Capaian Pembelajaran Mata Kuliah (CPMK) yang terukur dan selaras dengan
  Capaian Pembelajaran Lulusan (CPL) program studi.
- **AI-Augmented Learning:** Mahasiswa tidak hanya belajar rekayasa perangkat lunak, tetapi
  juga belajar memanfaatkan AI (ChatGPT, Claude, Copilot) sebagai mitra pengembangan dan
  co-developer, dengan tetap menjaga integritas akademik melalui AI Usage Log.
- **Konteks Indonesia:** Contoh kasus, dataset, dan skenario menggunakan konteks lokal
  Indonesia untuk meningkatkan relevansi dan keterlibatan mahasiswa.
- **Islamic Values:** Selaras dengan visi Universitas Al Azhar Indonesia, mata kuliah ini
  menanamkan nilai-nilai etika, kejujuran akademik, dan tanggung jawab sosial dalam
  penggunaan teknologi.

---

## Tentang Mata Kuliah

| Atribut | Detail |
|---------|--------|
| **Nama MK** | Rekayasa Perangkat Lunak |
| **Kode** | IF2XXX |
| **SKS** | 3 SKS (Teori, lab terintegrasi dalam modul) |
| **Semester** | Genap 2025/2026 |
| **Prasyarat** | Algoritma dan Pemrograman (INF-101) |
| **Ko-requisite** | — |
| **Bahasa Pemrograman** | Python 3.x |
| **Platform** | Google Colab, GitHub |

---

## Struktur Repository

| Folder | Isi | Jumlah File |
|--------|-----|-------------|
| `00-strategic-analysis/` | Analisis SWOT, Porter's 5 Forces, tren industri software | 1 |
| `01-rps/` | Rencana Pembelajaran Semester | 1 |
| `02-rtm/` | Rencana Tugas Mahasiswa | 1 |
| `03-modules/` | Modul perkuliahan mingguan | 16 |
| `04-assessments/` | Framework asesmen, kisi-kisi, rubrik | 5 |
| `05-buku-ajar/` | Buku ajar (14 bab + pendukung) | 18 |
| `datasets/` | Panduan resource & latihan | 1 |

---

## Kurikulum 16 Minggu

### Fase 1: Fondasi RPL — "Understand Software" (Minggu 1-4)

| Minggu | Topik |
|--------|-------|
| 1 | Pengantar Rekayasa Perangkat Lunak |
| 2 | Proses dan Model Pengembangan Perangkat Lunak |
| 3 | Rekayasa Kebutuhan |
| 4 | Pemodelan UML dan Desain Sistem |

### Fase 2: Pengembangan — "Build Quality Software" (Minggu 5-8)

| Minggu | Topik |
|--------|-------|
| 5 | Arsitektur Perangkat Lunak |
| 6 | Clean Code dan Refactoring |
| 7 | Version Control dengan Git |
| 8 | **UTS** |

### Fase 3: Penguasaan — "Assure and Manage" (Minggu 9-12)

| Minggu | Topik |
|--------|-------|
| 9 | Pengujian Perangkat Lunak |
| 10 | CI/CD dan DevOps Dasar |
| 11 | Manajemen Proyek Agile/Scrum |
| 12 | Kualitas Perangkat Lunak dan Metrik |

### Fase 4: Frontier — "Innovate Responsibly" (Minggu 13-16)

| Minggu | Topik |
|--------|-------|
| 13 | AI-Augmented Software Engineering |
| 14 | Etika Perangkat Lunak dan Tren Masa Depan |
| 15 | Proyek Akhir — Presentasi |
| 16 | **UAS** |

---

## Capaian Pembelajaran (CPMK)

| CPMK | Deskripsi | Bloom's |
|------|-----------|---------|
| CPMK-1 | Menjelaskan konsep dasar RPL, sejarah, model-model proses pengembangan (Waterfall, Agile, Spiral), serta prinsip etika pengembangan PL | C2 |
| CPMK-2 | Menerapkan teknik rekayasa kebutuhan dan pemodelan UML untuk mendokumentasikan kebutuhan PL secara sistematis | C3 |
| CPMK-3 | Menerapkan prinsip arsitektur PL dan design patterns untuk merancang solusi yang modular, scalable, dan maintainable | C3 |
| CPMK-4 | Menganalisis kualitas kode menggunakan prinsip clean code, SOLID, teknik refactoring, serta mengelola kolaborasi menggunakan Git | C3-C4 |
| CPMK-5 | Menganalisis dan menerapkan strategi pengujian PL serta membangun pipeline CI/CD untuk otomasi | C4 |
| CPMK-6 | Mengevaluasi kualitas PL menggunakan metrik standar (ISO 25010), menerapkan manajemen proyek Agile/Scrum | C4-C5 |
| CPMK-7 | Merancang dan membangun proyek PL end-to-end dengan memanfaatkan AI sebagai co-developer secara bertanggung jawab | C5-C6 |

---

## Penilaian

| Komponen | Bobot |
|----------|-------|
| Tugas Mingguan (T1-T6) | 15% |
| Kuis (K1-K3) | 10% |
| UTS | 25% |
| Proyek Akhir | 20% |
| UAS | 25% |
| Partisipasi | 5% |
| **Total** | **100%** |

---

## Tools & Teknologi

| Tool | Kegunaan | Akses |
|------|----------|-------|
| Python 3.x | Bahasa pemrograman utama | python.org |
| Google Colab | Cloud IDE untuk menulis dan menjalankan kode | colab.research.google.com |
| Git / GitHub | Version control dan kolaborasi | github.com |
| GitHub Actions | CI/CD pipeline | Built-in GitHub |
| pytest | Testing framework | pip install |
| pylint / flake8 | Static analysis | pip install |
| PlantUML / Draw.io | UML diagrams | Free online |
| Trello / GitHub Projects | Agile board | Free tier |
| ChatGPT / Claude / Copilot | AI sebagai coding partner — wajib mengisi AI Usage Log | Masing-masing platform |

---

## Buku Ajar

**"Rekayasa Perangkat Lunak: Membangun Sistem Berkualitas dengan Pendekatan Modern dan AI-Augmented"**

Buku ajar pendamping mata kuliah ini terdiri dari 14 bab utama, bagian penutup, dan
lampiran pendukung. Buku ini dirancang secara khusus untuk mendukung proses pembelajaran
di Program Studi Informatika, Universitas Al Azhar Indonesia, dengan pendekatan OBE dan
integrasi AI.

| Bab | Judul |
|-----|-------|
| 1 | Pengantar Rekayasa Perangkat Lunak |
| 2 | Proses dan Model Pengembangan Perangkat Lunak |
| 3 | Rekayasa Kebutuhan (Requirements Engineering) |
| 4 | Pemodelan UML dan Desain Sistem |
| 5 | Arsitektur Perangkat Lunak dan Design Patterns |
| 6 | Clean Code dan Refactoring |
| 7 | Version Control dengan Git |
| 8 | Pengujian Perangkat Lunak (Software Testing) |
| 9 | CI/CD dan DevOps Dasar |
| 10 | Manajemen Proyek Agile dan Scrum |
| 11 | Kualitas Perangkat Lunak dan Metrik (ISO 25010) |
| 12 | Keamanan Perangkat Lunak (Software Security) |
| 13 | AI-Augmented Software Engineering |
| 14 | Proyek Akhir: Integrasi dan Penerapan |
| — | Penutup & Lampiran |

---

## Kontak

**Dosen Pengampu:**
Tri Aji Nugroho, S.T., M.T.

**Afiliasi:**
Program Studi Informatika
Fakultas Sains dan Teknologi
Universitas Al Azhar Indonesia

---

## Lisensi

(c) 2026 Tri Aji Nugroho, S.T., M.T. — Universitas Al Azhar Indonesia

Materi ini dikembangkan untuk keperluan akademik Prodi Informatika UAI.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
