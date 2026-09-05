---
id: uai-inf-registri-bk
tipe: pedoman
judul: Registri Bahan Kajian (BK) dan Matriks BK × CPL — Prodi Informatika
prodi: Informatika
universitas: Universitas Al Azhar Indonesia
versi: 1.0
status: berlaku
sumber: Dokumen kurikulum resmi Program Studi Informatika UAI
diperbarui: 2026-09-05
berlaku_untuk: [INF-101, INF-102, TBD-STAT, IF2205, IF2206, IF3XXX]
---

# Registri Bahan Kajian & Matriks BK × CPL

> **Mengapa berkas ini penting.** Bahan Kajian adalah **rantai penghubung** antara mata kuliah dan CPL. Sebelum registri ini ada, pembebanan CPL pada RPS dipilih tanpa dasar yang dapat ditelusuri. Sekarang alurnya menjadi: **Mata Kuliah → Bahan Kajian → CPL → Profil Lulusan.**

## A. Matriks BK × CPL (22 Bahan Kajian × 11 CPL)

Legenda: **●** = Bahan Kajian menopang CPL tersebut.

| Kode | Bahan Kajian | UAI1 | UAI3 | 03 | 04 | 05 | FSTS1 | 07 | 08 | 09 | 10 | UAI2 | Σ |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| BK01 | Social Issues and Professional Practice | ● | ● | | | | | | | | | | 2 |
| BK02 | Security | ● | ● | ● | ● | | | | ● | ● | | | 6 |
| BK03 | Project Management | | | ● | ● | ● | ● | | | ● | | ● | 6 |
| BK04 | User Experience Design | | | | ● | | | | | ● | | | 2 |
| BK05 | Software Development Fundamentals | | | | ● | ● | ● | | ● | ● | | ● | 6 |
| BK06 | Data Management | | | | ● | ● | | | ● | ● | ● | | 5 |
| BK07 | Parallel and Distributed Computing | | | | | | | | ● | | | | 1 |
| BK08 | Network and Communication | | | ● | | | | | ● | | | | 2 |
| BK09 | Human-Computer Interaction | | | | ● | ● | | | ● | ● | | | 4 |
| BK10 | Software Engineering / Software Design | | | | ● | ● | ● | | ● | ● | | ● | 6 |
| BK11 | Operating Systems | | | ● | | | | | | | | | 1 |
| **BK12** | **Algorithmic Foundations** | | | ● | | | | ● | ● | | | | 3 |
| BK13 | Foundation of Programming Languages | | | ● | ● | ● | | | ● | ● | ● | | 6 |
| **BK14** | **Programming Fundamentals** | | | ● | | | | | | | | | 1 |
| BK15 | Systems Fundamentals | | | ● | | | | | | | | | 1 |
| BK16 | Architecture and Organization | | | ● | | | | | | | | | 1 |
| BK17 | Graphics and Interactive Techniques | | | | | | ● | | ● | | ● | | 3 |
| BK18 | Artificial Intelligence | | | | | | | ● | ● | | ● | | 3 |
| BK19 | Specialized Platform Development | | | | ● | ● | ● | | ● | ● | | ● | 6 |
| BK20 | Mathematical dan Statistical Foundations | | | ● | ● | | | ● | ● | ● | ● | | 6 |
| BK21 | Pengembangan Diri | ● | ● | | | | ● | ● | | | | ● | 5 |
| BK22 | Metodologi Penelitian | | | | | | ● | ● | | | | | 2 |
| | **Σ per CPL** | **3** | **3** | **10** | **10** | **7** | **7** | **5** | **13** | **10** | **5** | **5** | |

> Singkatan kolom: `UAI1` = CPLUAI1 · `UAI3` = CPLUAI3 · `FSTS1` = CPL-FSTS1 · `UAI2` = CPLUAI2 · sisanya CPL03–CPL10.

**Bacaan cepat:** CPL08 (merancang algoritma) adalah CPL dengan tumpuan terluas — 13 dari 22 Bahan Kajian. Sebaliknya CPLUAI1 dan CPLUAI3 (sikap) hanya ditopang 3 BK, sehingga mata kuliah yang mengampu BK01 dan BK21 memikul tanggung jawab besar atas ranah sikap seluruh kurikulum.

## B. Usulan Pembebanan BK per Mata Kuliah

> 🔲 **[PERLU VALIDASI PRODI]** — Penetapan final pembebanan Bahan Kajian ke mata kuliah adalah kewenangan program studi. Tabel berikut adalah **usulan berbasis isi materi yang sudah ada di repositori**, disusun agar pekerjaan dapat berjalan; ganti bila prodi menetapkan lain.

| Mata Kuliah | Bahan Kajian | CPL hasil turunan |
|---|---|---|
| **INF-101** Algoritma dan Pemrograman | BK12, BK14, BK01 | CPL03, CPL07, CPL08, CPLUAI1, CPLUAI3 |
| **INF-102** Praktikum Algoritma dan Pemrograman | BK12, BK14, BK01 | CPL03, CPL07, CPL08, CPLUAI1, CPLUAI3 |
| **TBD-STAT** Analisis Data Statistik | BK20, BK06 | CPL03, CPL04, CPL07, CPL08, CPL09, CPL10 |
| **IF2205** Rekayasa Perangkat Lunak | BK10, BK05, BK03 | CPL03, CPL04, CPL05, CPL-FSTS1, CPL08, CPL09, CPLUAI2 |
| **IF2206** Praktikum Rekayasa Perangkat Lunak | BK10, BK05 | CPL04, CPL05, CPL-FSTS1, CPL08, CPL09, CPLUAI2 |
| **IF3XXX** Kecerdasan Buatan dan Machine Learning | BK18, BK06, BK20 | CPL03, CPL04, CPL07, CPL08, CPL09, CPL10 |

**Prinsip pembebanan:** mata kuliah praktikum **mewarisi** Bahan Kajian dan CPL dari mata kuliah teori pasangannya; yang berbeda hanya tingkat kontribusi dan ranah taksonomi (praktikum menekankan ranah **P/Psikomotorik**).

## C. Skala Tingkat Kontribusi

Dipakai pada matriks `mutu/01-peta-mutu-mk.md` setiap mata kuliah, mengikuti bentuk yang lazim diminta instrumen akreditasi:

| Kode | Tingkat | Makna |
|---|---|---|
| **K** | Kuat | Mata kuliah menjadi penopang utama CPL; diukur langsung oleh asesmen utama |
| **M** | Menengah | Mata kuliah berkontribusi nyata tetapi bukan penopang utama |
| **T** | Tipis | Bersinggungan, diukur secara tidak langsung atau melalui sikap/partisipasi |

Agregasi tingkat kontribusi seluruh mata kuliah menjadi matriks CPL × MK tingkat program dikerjakan pada Fase 3 (`matriks-cpl-mk.md`), untuk memastikan **tidak ada CPL yang yatim** — yaitu CPL yang tidak diampu penuh oleh mata kuliah manapun.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
