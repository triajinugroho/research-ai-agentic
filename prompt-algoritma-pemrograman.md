# PROMPT LENGKAP: Paket Mata Kuliah "Algoritma dan Pemrograman"

> **Instruksi**: Copy-paste seluruh isi prompt di bawah ini ke chat Claude baru untuk men-generate paket mata kuliah lengkap. Prompt ini self-contained — tidak memerlukan file atau konteks tambahan.

---

## [MULAI PROMPT]

Kamu adalah seorang **ahli desain kurikulum pendidikan tinggi Indonesia** yang berspesialisasi dalam pengembangan mata kuliah Computer Science berbasis OBE (Outcome-Based Education), dengan keahlian mendalam dalam KKNI, SN-Dikti, dan integrasi AI dalam pendidikan. Kamu juga memahami tren frontier AI global dan implikasinya terhadap pendidikan pemrograman.

**Tanggal hari ini: 28 Februari 2026.** Semua dokumen yang dihasilkan harus menggunakan tanggal ini sebagai referensi.

---

### PROYEK: Buat Paket Mata Kuliah Lengkap "Algoritma dan Pemrograman"

Buatkan **paket mata kuliah lengkap end-to-end** untuk mata kuliah **Algoritma dan Pemrograman** dengan spesifikasi berikut. Semua output harus berupa file markdown di **repository baru yang terpisah**.

---

### A. IDENTITAS DOSEN & INSTITUSI

| Komponen | Detail |
|----------|--------|
| **Nama Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Jabatan** | Dosen Pengampu Mata Kuliah Algoritma dan Pemrograman |
| **Program Studi** | Informatika (S1) |
| **Fakultas** | Sains dan Teknologi |
| **Universitas** | Universitas Al Azhar Indonesia (UAI) |
| **Akreditasi** | Baik Sekali (BAN-PT/LAM-INFOKOM, SK 050/SK/LAM-INFOKOM/Ak/S/III/2025) |
| **Visi Prodi** | "Problem Solvers in Digital, Driven by Ethics and Islamic Values" |
| **Kerjasama Industri** | Google, Red Hat Academy, Alibaba Academy, Data Academy, Solusi 247 |

Seluruh dokumen harus mencantumkan **Tri Aji Nugroho, S.T., M.T.** sebagai penulis/dosen pengampu. Gunakan format konsisten:
- Di RPS/RTM: `Dosen Pengampu: Tri Aji Nugroho, S.T., M.T.`
- Di Buku Ajar: `Penulis: Tri Aji Nugroho, S.T., M.T.`
- Di dokumen lain: `Disusun oleh: Tri Aji Nugroho, S.T., M.T.`

---

### B. IDENTITAS MATA KULIAH

| Komponen | Detail |
|----------|--------|
| **Nama MK** | Algoritma dan Pemrograman |
| **Kode MK** | IF1XXX |
| **SKS** | 3 SKS (Teori + Praktikum Terintegrasi) |
| **Durasi** | 150 menit/minggu (bisa 2×75 menit atau 1×150 menit) |
| **Semester** | 2 (Genap) |
| **Tahun Akademik** | 2025/2026 |
| **Tingkat** | 1 (Mahasiswa tahun pertama) |
| **Prasyarat** | Pengantar Informatika / Logika Matematika (Semester 1) |
| **Ko-requisite** | Analisis Data Statistik |
| **Bahasa Pemrograman** | Python 3.x |
| **Platform Utama** | Google Colab (cloud-based, gratis) |
| **Platform Pendukung** | VS Code / PyCharm (opsional untuk lokal) |
| **LMS** | LMS UAI |

---

### C. KERANGKA PEDAGOGIS

#### C.1 Pendekatan OBE (Outcome-Based Education)

Seluruh materi harus dirancang dengan pemetaan lengkap:
- **CPL** (Capaian Pembelajaran Lulusan) → minimal 5-6 CPL yang didukung
- **CPMK** (Capaian Pembelajaran Mata Kuliah) → 7 CPMK
- **Sub-CPMK** → detail per minggu, setiap Sub-CPMK harus punya kata kerja Bloom yang terukur
- Sesuai standar **KKNI Level 6** dan **SN-Dikti**

#### C.2 Taksonomi Bloom

Setiap tujuan pembelajaran harus menggunakan kata kerja Bloom yang tepat:
- **C1** (Mengingat): mendefinisikan, menyebutkan, mengidentifikasi
- **C2** (Memahami): menjelaskan, membedakan, menginterpretasikan
- **C3** (Menerapkan): menerapkan, mengimplementasikan, menggunakan
- **C4** (Menganalisis): menganalisis, membandingkan, mengevaluasi
- **C5** (Mengevaluasi): menilai, menguji, mengkritisi
- **C6** (Mencipta): merancang, membangun, mengembangkan

#### C.3 AI-Augmented Programming

AI bukan tambahan opsional — AI terintegrasi sebagai **coding partner** sepanjang semester:
- Setiap bab buku ajar memiliki **"AI Corner"** yang mengajarkan penggunaan AI untuk topik tersebut
- Progresi AI Literacy: Dasar (Bab 1-4) → Menengah (Bab 5-7) → Lanjut (Bab 8-11) → Mahir (Bab 12-14)
- Mahasiswa belajar menulis prompt yang efektif, memvalidasi output AI, dan menggunakan AI secara bertanggung jawab
- AI TIDAK diperbolehkan saat ujian (UTS/UAS closed-book)
- Semua tugas yang menggunakan AI harus menyertakan **AI Usage Log**

#### C.4 Integrasi Nilai-Nilai Islami UAI

Nilai-nilai Islami harus terintegrasi secara natural (bukan dipaksakan):
- **Amanah** (Trustworthy): kejujuran dalam coding, academic integrity, tidak plagiat
- **Keadilan** (Justice/al-'Adl): fairness dalam testing, edge cases handling
- **Ihsan** (Excellence): clean code, best practices, continuous improvement
- **Transparansi**: code readability, documentation, open source spirit
- **Al-Khwarizmi Heritage**: kata "algoritma" berasal dari nama ilmuwan Muslim Muhammad ibn Musa al-Khwarizmi — ini koneksi budaya unik yang harus diangkat di Bab 1

#### C.5 Konteks Indonesia

Seluruh contoh, studi kasus, dan dataset harus menggunakan konteks Indonesia:
- Data harga barang di pasar tradisional
- Sistem informasi mahasiswa UAI
- E-commerce Indonesia (Tokopedia, Shopee)
- Data transportasi Jakarta (TransJakarta, KRL)
- Data BPS (sensus, ekonomi, sosial)
- Permasalahan lokal: antrian di rumah sakit, sistem perpustakaan, pengelolaan sampah

---

### D. KURIKULUM 16 MINGGU

#### Fase 1: Fondasi — "Think Like a Programmer" (Minggu 1-4)

| Minggu | Topik | Lab | Konsep Kunci |
|--------|-------|-----|--------------|
| 1 | Pengantar Algoritma & Computational Thinking di Era AI | Setup Python & Google Colab | Algoritma, flowchart, pseudocode, computational thinking (decomposition, pattern recognition, abstraction, algorithm design), Al-Khwarizmi |
| 2 | Variabel, Tipe Data, dan Operator | Variabel & Ekspresi Python | int, float, str, bool, operator aritmatika/logika/perbandingan, type conversion, input/output |
| 3 | Struktur Kontrol: Seleksi (if/elif/else) | Conditional Logic | Percabangan, Boolean logic, nested conditions, decision tables |
| 4 | Struktur Kontrol: Perulangan (for/while) | Loops & Patterns | for, while, break, continue, nested loops, pattern printing |

#### Fase 2: Modularitas — "Build with Functions" (Minggu 5-8)

| Minggu | Topik | Lab | Konsep Kunci |
|--------|-------|-----|--------------|
| 5 | Fungsi dan Modularitas | Functions & Decomposition | def, parameters, return, scope, top-down design, DRY principle |
| 6 | String dan Pengolahan Teks | String Processing | String methods, slicing, formatting, f-string, text processing |
| 7 | List, Tuple, dan Operasi Koleksi | Collections & Iteration | List, tuple, list comprehension, slicing, mutation vs immutability |
| 8 | **UTS** (Ujian Tengah Semester) | — | Cakupan Minggu 1-7 |

#### Fase 3: Struktur Data & Algoritma — "Solve Real Problems" (Minggu 9-12)

| Minggu | Topik | Lab | Konsep Kunci |
|--------|-------|-----|--------------|
| 9 | Dictionary, Set, dan Pemilihan Struktur Data | Data Structure Selection | dict, set, kapan pakai apa, hashable vs unhashable |
| 10 | Algoritma Pencarian (Searching) | Linear & Binary Search | Linear search, binary search, perbandingan performa, tracing |
| 11 | Algoritma Pengurutan (Sorting) | Sorting Algorithms | Bubble sort, selection sort, insertion sort, built-in sort, tracing step-by-step |
| 12 | Rekursi dan Pemecahan Masalah | Recursive Problem Solving | Base case, recursive case, factorial, fibonacci, tower of hanoi, call stack |

#### Fase 4: Frontier — "Code with AI & Build Projects" (Minggu 13-16)

| Minggu | Topik | Lab | Konsep Kunci |
|--------|-------|-----|--------------|
| 13 | Kompleksitas Algoritma (Big-O) dan Optimasi | Algorithm Analysis | Big-O notation, time/space complexity, comparing algorithms, plotting growth |
| 14 | AI-Augmented Programming dan Code Quality | AI as Coding Partner | AI pair programming, prompt engineering untuk kode, code review, clean code, ethical AI |
| 15 | Presentasi Proyek Akhir | — | Presentasi dan demo proyek end-to-end |
| 16 | **UAS** (Ujian Akhir Semester) | — | Komprehensif (Minggu 1-15) |

---

### E. CPMK (Capaian Pembelajaran Mata Kuliah) — 7 CPMK

| CPMK | Deskripsi | Bloom's | Bab Buku |
|------|-----------|---------|----------|
| CPMK-1 | Menjelaskan konsep dasar algoritma, computational thinking, dan peran pemrograman di era AI | C2 | 1 |
| CPMK-2 | Menerapkan variabel, tipe data, operator, dan ekspresi untuk menyelesaikan masalah komputasi sederhana | C3 | 2 |
| CPMK-3 | Menerapkan struktur kontrol (seleksi dan perulangan) untuk membangun alur program yang logis | C3 | 3, 4 |
| CPMK-4 | Menerapkan fungsi, string processing, dan prinsip modularitas untuk membangun program terstruktur | C3-C4 | 5, 6 |
| CPMK-5 | Menganalisis dan memilih struktur data yang tepat (list, tuple, dict, set) untuk penyelesaian masalah | C4 | 7, 8 |
| CPMK-6 | Menganalisis dan mengimplementasikan algoritma pencarian, pengurutan, dan rekursi | C4-C5 | 9, 10, 11 |
| CPMK-7 | Mengevaluasi efisiensi algoritma dan merancang solusi pemrograman end-to-end dengan AI sebagai coding partner yang bertanggung jawab | C5-C6 | 12, 13, 14 |

---

### F. BUKU AJAR — Struktur 14 Bab

**Judul Buku:** *Algoritma dan Pemrograman: Fondasi Computational Thinking dengan Python dan AI*

| Bagian | Bab | Judul |
|--------|-----|-------|
| **Bagian I: Fondasi** | 1 | Pengantar Algoritma dan Computational Thinking |
| | 2 | Variabel, Tipe Data, dan Operator |
| | 3 | Struktur Kontrol: Seleksi |
| | 4 | Struktur Kontrol: Perulangan |
| **Bagian II: Modularitas** | 5 | Fungsi dan Modularitas |
| | 6 | String dan Pengolahan Teks |
| | 7 | List, Tuple, dan Operasi Koleksi |
| **Bagian III: Struktur Data & Algoritma** | 8 | Dictionary, Set, dan Pemilihan Struktur Data |
| | 9 | Algoritma Pencarian (Searching) |
| | 10 | Algoritma Pengurutan (Sorting) |
| | 11 | Rekursi dan Pemecahan Masalah |
| **Bagian IV: Frontier** | 12 | Kompleksitas Algoritma (Big-O) dan Optimasi |
| | 13 | AI-Augmented Programming dan Code Quality |
| | 14 | Proyek Akhir: Membangun Solusi End-to-End |
| — | — | Penutup: Refleksi dan Langkah ke Depan |
| — | — | Lampiran A-F |

**PENTING — KONSISTENSI BAB:**
- Bab 13 = AI-Augmented Programming (BUKAN proyek akhir)
- Bab 14 = Proyek Akhir (INI bab proyek akhir)
- Semua referensi ke "proyek akhir" di dokumen manapun HARUS merujuk ke **Bab 14**, BUKAN Bab 13
- Penutup HARUS merefleksikan seluruh 14 bab secara lengkap
- Tabel positioning di "mengapa-buku-ini.md" HARUS menyebut "Ya — Bab 14" untuk proyek akhir

---

### G. TABEL POSITIONING BUKU — vs Buku Ajar Lain

Buat dokumen `mengapa-buku-ini.md` yang memposisikan buku ini dibandingkan 5 buku utama:

| Kriteria | CLRS (Cormen et al.) | Sedgewick & Wayne | Grokking Algorithms | Think Python (Downey) | Learning Python (Lutz) | **Buku Ini** |
|----------|:----:|:----:|:----:|:----:|:----:|:----:|
| **Bahasa** | English | English | English | English | English | **Indonesia** |
| **Target** | Graduate/Advanced | CS2-CS3 | Self-learners | CS1/Intro | General | **Informatika S1 Sem 2** |
| **Bahasa Pemrograman** | Pseudocode | Java | Python | Python | Python | **Python (Google Colab)** |
| **Integrasi AI/LLM** | Tidak | Tidak | Tidak | Tidak | Tidak | **Ya — setiap bab** |
| **Konteks dataset** | American | American | American | American | American | **Indonesia** |
| **Berbasis OBE/KKNI** | Tidak | Tidak | Tidak | Tidak | Tidak | **Ya — pemetaan CPMK** |
| **Nilai-nilai Islami** | Tidak | Tidak | Tidak | Tidak | Tidak | **Ya — terintegrasi** |
| **Visualisasi Algoritma** | Minimal | Excellent | Excellent | Moderate | Minimal | **Ya + interaktif (Colab)** |
| **Latihan bertingkat** | Bab-end problems | Lab exercises | Tidak | Exercises | Tidak | **Ya — 3 level** |
| **Proyek akhir end-to-end** | Tidak | Lab exercises | Tidak | Exercises | Tidak | **Ya — Bab 14** |
| **Harga / Akses** | Komersial | Komersial | Komersial | Gratis | Komersial | **Gratis (institusional)** |
| **Platform** | Textbook cetak | Textbook + website | Textbook cetak | PDF / Online | Textbook cetak | **Google Colab-ready** |

**7 Diferensiator Utama yang harus dijabarkan:**
1. Pertama di Indonesia: AI sebagai Coding Partner terintegrasi setiap bab
2. 100% Konteks Indonesia (contoh, dataset, studi kasus)
3. Berbasis OBE/KKNI dengan pemetaan CPMK eksplisit
4. Google Colab-ready (tanpa instalasi, gratis)
5. Nilai-nilai Islami terintegrasi (termasuk warisan Al-Khwarizmi)
6. AI Literacy progresif 4 tingkat (Dasar → Menengah → Lanjut → Mahir)
7. Bahasa Indonesia dengan terminologi bilingual (Indonesia + English)

**Bagian "Apa yang Buku Ini Bukan":**

| Buku ini bukan... | Untuk itu, lihat... |
|--------------------|---------------------|
| Buku algoritma tingkat lanjut (graduate) | CLRS, Kleinberg & Tardos |
| Buku OOP (Object-Oriented Programming) | Head First Design Patterns, Clean Code |
| Buku struktur data lanjutan | Goodrich, Sedgewick |
| Panduan competitive programming | Halim, Laaksonen |
| Referensi lengkap bahasa Python | Lutz Learning Python, docs.python.org |

---

### H. ASESMEN

#### H.1 Komponen Penilaian

| Komponen | Bobot | Jumlah | Cakupan |
|----------|-------|--------|---------|
| Tugas Mingguan | 15% | 6 tugas (masing-masing 2.5%) | T1-T6 |
| Kuis | 10% | 3 kuis (masing-masing ~3.33%) | K1-K3 |
| UTS | 20% | 1 (Minggu 8) | Minggu 1-7 |
| Proyek Akhir | 25% | 1 (Minggu 9-15) | Komprehensif |
| UAS | 25% | 1 (Minggu 16) | Komprehensif |
| Partisipasi & Etika AI | 5% | Sepanjang semester | — |
| **TOTAL** | **100%** | | |

#### H.2 Rincian Tugas (RTM)

| Tugas | Minggu | Topik | CPMK |
|-------|--------|-------|------|
| T1 | 2 | Program Kalkulator Sederhana (variabel, tipe data, operator, I/O) | CPMK-2 |
| T2 | 4 | Pattern Printing & Loop Challenges (nested loops, logika perulangan) | CPMK-3 |
| T3 | 5 | Refactoring with Functions (dekomposisi program menjadi fungsi) | CPMK-4 |
| T4 | 7 | Data Processing with Collections (operasi list/tuple pada data Indonesia) | CPMK-5 |
| T5 | 10 | Implementasi & Perbandingan Algoritma Pencarian | CPMK-6 |
| T6 | 11 | Implementasi & Perbandingan Algoritma Pengurutan | CPMK-6 |

**Rubrik 4 Dimensi (untuk setiap tugas):**
1. **Teknis** (25%): Kebenaran logika, ketepatan output, penanganan edge cases
2. **Problem Solving** (30%): Pemilihan pendekatan, dekomposisi masalah, efisiensi solusi
3. **Kode Python** (25%): Kebersihan, dokumentasi, penamaan variabel, PEP 8 compliance
4. **Presentasi** (20%): Struktur penjelasan, komentar kode, readme/dokumentasi

#### H.3 Kuis

| Kuis | Minggu | Cakupan | Format |
|------|--------|---------|--------|
| K1 | 4 | Minggu 1-4 (Fondasi) | Closed-book, tracing kode, tulis pseudocode |
| K2 | 7 | Minggu 5-7 (Modularitas) | Closed-book, tulis fungsi, operasi string/list |
| K3 | 12 | Minggu 9-12 (Struktur Data & Algoritma) | Closed-book, tracing searching/sorting/rekursi |

#### H.4 Proyek Akhir

- **Bentuk**: Bangun aplikasi Python lengkap (individual atau berpasangan max 2 orang)
- **Syarat wajib**: Menggunakan fungsi, struktur data yang tepat, minimal 1 algoritma searching/sorting, file I/O
- **AI Usage**: Diperbolehkan sebagai coding partner, WAJIB didokumentasikan dalam AI Usage Log
- **Timeline**: Minggu 9 (proposal) → Minggu 12 (progress) → Minggu 15 (presentasi)
- **Deliverables**: Source code Python + Dokumentasi + Presentasi + AI Usage Log

**10 Contoh Topik Proyek (konteks Indonesia):**
1. Sistem Informasi Perpustakaan Mini
2. Aplikasi Kasir Toko/Warung Sederhana
3. Game Tebak Kata Bahasa Indonesia
4. Sistem Antrian Rumah Sakit/Puskesmas
5. Tool Analisis Teks (frekuensi kata, sentimen sederhana)
6. Buku Alamat / Kontak Manager
7. Kalkulator IPK dan Transkrip Sederhana
8. Sistem Pencarian dan Rekomendasi Menu Kantin
9. Sistem Voting / E-Polling Sederhana
10. Mini Quiz App (bank soal + scoring + leaderboard)

**Rubrik Proyek (8 Komponen, 100 poin):**
1. Perumusan Masalah & Desain: 10%
2. Implementasi Kode & Fungsi: 20%
3. Penggunaan Struktur Data & Algoritma: 15%
4. Penanganan Error & Edge Cases: 10%
5. Dokumentasi Kode: 10%
6. Dokumentasi AI Usage: 15%
7. Presentasi & Demo: 15%
8. Etika & Integritas: 5%

---

### I. ANALISIS STRATEGIS YANG HARUS DIBUAT

Buat dokumen `00-strategic-analysis/strategic-analysis.md` yang mencakup:

#### I.1 Executive Summary
Posisikan mata kuliah AlPro di persimpangan strategis: pemrograman adalah skill paling fundamental di era AI, namun cara mengajarkannya harus berubah drastis. Dengan adanya AI coding assistants (GitHub Copilot, Claude, ChatGPT), mahasiswa perlu belajar *berpikir algoritmik* (computational thinking) lebih dari sekadar menghafal sintaks.

#### I.2 Analisis SWOT
- **Strengths**: Akreditasi Baik Sekali, partnership industri (Google, Red Hat), expertise dosen AI/ML, nilai Islami sebagai diferensiasi, track record lulusan, kurikulum IEEE/ACM/APTIKOM
- **Weaknesses**: Mahasiswa semester 2 masih pemula, 3 SKS terbatas, potensi over-reliance AI, infrastruktur bervariasi
- **Opportunities**: Software engineering job market boom, 92% mahasiswa sudah pakai AI, GitHub Copilot era, MBKM, open-source education, Indonesia digital economy
- **Threats**: Bootcamp/MOOC competition, academic integrity crisis (AI plagiarism), rapid tech change, AI coding replacing junior developers concern, digital divide

Sertakan **SWOT Matrix** dengan strategi kombinasi SO, ST, WO, WT.

#### I.3 Porter's Five Forces
Analisis 5 kekuatan kompetitif khusus untuk pendidikan pemrograman:
1. Threat of New Entrants (bootcamp baru, platform AI-based)
2. Bargaining Power of Buyers (mahasiswa punya banyak pilihan belajar gratis)
3. Threat of Substitutes (YouTube, ChatGPT, Copilot bisa "mengajar" coding)
4. Bargaining Power of Suppliers (dosen, infrastruktur)
5. Competitive Rivalry (antar universitas, bootcamp, MOOC)

#### I.4 Tren Frontier AI & Pendidikan Global
Sertakan data dan tren terbaru (2025-2026):
- AI coding assistants: GitHub Copilot, Claude Code, Cursor, Windsurf
- Computational thinking sebagai core competency (bukan coding semata)
- UNESCO AI & Education guidelines
- McKinsey: personalized learning +30% effectiveness
- Perubahan landscape pekerjaan developer: dari "menulis kode" ke "mengarahkan AI menulis kode"

#### I.5 100x Value Impact Framework
Jelaskan bagaimana mata kuliah ini memberikan 100x value:
- **Untuk Mahasiswa**: foundational skills × AI multiplier × portfolio × career × transferability
- **Untuk Dosen**: teaching efficiency × research opportunities × professional development
- **Untuk Universitas**: differentiation × accreditation × industry alignment × student satisfaction × scalability

---

### J. STRUKTUR FOLDER & FILE LENGKAP

Buat **SEMUA** file berikut di repository baru. Setiap file harus lengkap dan substantif.

```
algoritma-pemrograman-uai/
├── README.md
├── 00-strategic-analysis/
│   └── strategic-analysis.md
├── 01-rps/
│   └── rps-algoritma-pemrograman.md
├── 02-rtm/
│   └── rtm-algoritma-pemrograman.md
├── 03-modules/
│   ├── week-01-pengantar-algoritma-computational-thinking.md
│   ├── week-02-variabel-tipe-data-operator.md
│   ├── week-03-struktur-kontrol-seleksi.md
│   ├── week-04-struktur-kontrol-perulangan.md
│   ├── week-05-fungsi-dan-modularitas.md
│   ├── week-06-string-pengolahan-teks.md
│   ├── week-07-list-tuple-operasi-koleksi.md
│   ├── week-08-uts-review-dan-ujian.md
│   ├── week-09-dictionary-set-struktur-data.md
│   ├── week-10-algoritma-pencarian.md
│   ├── week-11-algoritma-pengurutan.md
│   ├── week-12-rekursi-pemecahan-masalah.md
│   ├── week-13-kompleksitas-algoritma-big-o.md
│   ├── week-14-ai-augmented-programming.md
│   ├── week-15-proyek-akhir-presentasi.md
│   └── week-16-uas-review-dan-ujian.md
├── 04-labs/
│   ├── lab-01-setup-python-colab.md
│   ├── lab-02-variabel-ekspresi.md
│   ├── lab-03-conditional-logic.md
│   ├── lab-04-loops-patterns.md
│   ├── lab-05-functions-decomposition.md
│   ├── lab-06-string-processing.md
│   ├── lab-07-collections-iteration.md
│   ├── lab-09-data-structure-selection.md
│   ├── lab-10-searching-algorithms.md
│   ├── lab-11-sorting-algorithms.md
│   ├── lab-12-recursive-problem-solving.md
│   ├── lab-13-algorithm-analysis.md
│   └── lab-14-ai-augmented-programming.md
├── 05-assessments/
│   ├── assessment-framework.md
│   ├── kisi-kisi-uts.md
│   ├── kisi-kisi-uas.md
│   ├── project-guidelines.md
│   └── rubrik-tugas.md
├── 06-buku-ajar/
│   ├── 00-halaman-depan.md
│   ├── mengapa-buku-ini.md
│   ├── bab-01-pengantar-algoritma-computational-thinking.md
│   ├── bab-02-variabel-tipe-data-operator.md
│   ├── bab-03-struktur-kontrol-seleksi.md
│   ├── bab-04-struktur-kontrol-perulangan.md
│   ├── bab-05-fungsi-dan-modularitas.md
│   ├── bab-06-string-pengolahan-teks.md
│   ├── bab-07-list-tuple-operasi-koleksi.md
│   ├── bab-08-dictionary-set-struktur-data.md
│   ├── bab-09-algoritma-pencarian.md
│   ├── bab-10-algoritma-pengurutan.md
│   ├── bab-11-rekursi-pemecahan-masalah.md
│   ├── bab-12-kompleksitas-algoritma-big-o.md
│   ├── bab-13-ai-augmented-programming.md
│   ├── bab-14-proyek-akhir.md
│   ├── penutup.md
│   └── lampiran.md
└── datasets/
    └── README.md
```

**Total: ~59 file markdown** — semuanya harus dibuat lengkap.

---

### K. SPESIFIKASI KONTEN PER DELIVERABLE

#### K.1 README.md
- Judul, identitas MK, dosen, pendekatan
- Filosofi desain (diagram: `Fondasi Kuat + Python Modern + AI Literacy = Future-Proof Programmer`)
- Struktur folder (tabel)
- Kurikulum 16 minggu (4 fase, tabel per fase)
- Tools & teknologi (tabel)
- Capaian pembelajaran (tabel CPMK)
- Penilaian (tabel komponen + bobot)
- Tagline: *"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — IF UAI

#### K.2 RPS (01-rps/rps-algoritma-pemrograman.md)
Harus memiliki SEMUA bagian berikut (mengikuti format SN-Dikti):
- **A. Identitas Mata Kuliah** (tabel lengkap)
- **B. Deskripsi Mata Kuliah** (paragraf deskriptif, sebutkan ko-requisite dengan Analisis Data Statistik)
- **C. CPL yang Dibebankan pada Mata Kuliah** (6 CPL dalam tabel)
- **D. CPMK** (7 CPMK dengan Bloom's)
- **E. Sub-CPMK** (tabel lengkap per minggu, 16 minggu)
- **F. Tabel RPS** (tabel besar per minggu dengan kolom: Minggu, Sub-CPMK, Materi Pembelajaran, Metode/Strategi, Pengalaman Belajar, Indikator Penilaian, Bobot, Referensi)
- **G. Peta Evaluasi** (ringkasan bobot, matrix CPMK × asesmen, timeline asesmen)
- **H. Konversi Nilai** (tabel huruf → angka → range, sesuai standar UAI)
- **I. Referensi** (utama + pendukung + online, minimal 10 sumber)
- **J. Kebijakan Khusus** (AI policy yang jelas, kehadiran, keterlambatan, academic integrity)
- **K. Profil Proyek Akhir** (ringkasan)
- Footer: `Diperbarui: Februari 2026`

#### K.3 RTM (02-rtm/rtm-algoritma-pemrograman.md)
- Tabel ringkasan semua tugas, kuis, dan proyek
- Detail per tugas (T1-T6): deskripsi, tujuan, deliverables, rubrik 4 dimensi (skala 4 poin)
- Detail per kuis (K1-K3): cakupan, format, durasi
- Detail proyek akhir: timeline, syarat, rubrik 8 komponen
- AI Usage Policy per komponen asesmen

#### K.4 Modul Mingguan (03-modules/week-NN-*.md)
Setiap modul HARUS memiliki struktur:
1. **Header**: Judul, informasi modul (tabel: MK, minggu, topik, CPMK, durasi, metode)
2. **Tujuan Pembelajaran**: Numbered list dengan kata kerja Bloom
3. **Materi Pembelajaran**: Konten detail dengan teori, contoh, tabel, kode Python, diagram ASCII
4. **Kegiatan Pembelajaran**: Aktivitas kelas (pre-class, in-class, post-class)
5. **Penugasan**: Jika ada tugas/kuis minggu itu
6. **Referensi**: Sumber yang digunakan

**Catatan konten spesifik:**
- Week 1: Wajib bahas Al-Khwarizmi, flowchart notation (oval/parallelogram/rectangle/diamond/arrow), pseudocode conventions, 4 pilar computational thinking
- Week 3-4: Gunakan decision table dan loop trace table
- Week 5: Diagram top-down design, visualisasi scope
- Week 10-11: Trace table step-by-step untuk searching dan sorting
- Week 12: Diagram recursion tree, visualisasi call stack
- Week 13: Grafik perbandingan Big-O (O(1), O(log n), O(n), O(n log n), O(n²), O(2^n))
- Week 14: Workflow AI pair programming, prompt engineering untuk coding

#### K.5 Lab Praktikum (04-labs/lab-NN-*.md)
Setiap lab HARUS memiliki:
1. **Tujuan Praktikum**: Apa yang mahasiswa akan capai
2. **Persiapan**: Apa yang perlu disiapkan
3. **Langkah-langkah**: Step-by-step dengan kode Python lengkap dan penjelasan
4. **Tantangan Tambahan**: 2-3 tantangan ekstra
5. **Checklist Penyelesaian**: Checklist apa yang harus diselesaikan

Semua kode harus **Google Colab-compatible** dan menggunakan konteks Indonesia.

**Konten lab spesifik:**
- Lab 01: Setup Colab + Hello World + input/output dasar
- Lab 02: Kalkulator sederhana, konversi suhu, hitung diskon
- Lab 03: Grade calculator, BMI checker, penentuan tarif TransJakarta
- Lab 04: Pattern printing (segitiga, piramida), tabel perkalian, game tebak angka
- Lab 05: Refactoring program "spageti" menjadi fungsi-fungsi modular
- Lab 06: Word counter, Caesar cipher, palindrome checker, text formatter
- Lab 07: Manajemen nilai mahasiswa dengan list, statistik kelas
- Lab 09: Aplikasi buku telepon (dict), analisis frekuensi kata (set)
- Lab 10: Implementasi linear search vs binary search, bandingkan performa
- Lab 11: Implementasi bubble, selection, insertion sort dengan visualisasi step-by-step
- Lab 12: Factorial, fibonacci, tower of hanoi, binary search rekursif
- Lab 13: Timing algorithms, plotting growth curves Big-O
- Lab 14: Sesi AI pair programming — bangun program lengkap dengan bantuan AI, dokumentasikan prosesnya

#### K.6 Asesmen (05-assessments/)

**assessment-framework.md**: Filosofi asesmen autentik, komponen, detail per komponen, AI policy
**kisi-kisi-uts.md**: Cakupan Minggu 1-7, 100 menit, closed-book, tipe soal (PG 20%, code tracing 30%, tulis kode 30%, essay/desain 20%)
**kisi-kisi-uas.md**: Cakupan Minggu 9-15 + komprehensif, 120 menit, closed-book + 1 lembar catatan, tipe soal serupa
**project-guidelines.md**: Panduan proyek akhir lengkap (timeline, syarat, rubrik, contoh topik, template AI Usage Log)
**rubrik-tugas.md**: Rubrik detail 4 dimensi × skala 4 poin untuk semua tugas

#### K.7 Buku Ajar (06-buku-ajar/)

**Setiap bab (bab-01 s/d bab-14) HARUS memiliki:**
1. Header: `# BAB N: JUDUL` + nama penulis
2. **Tujuan Pembelajaran**: Tabel (Sub-CPMK, Deskripsi, Bloom's Level)
3. **Konten utama**: Numbered sections (N.1, N.2, dst.) dengan subsections (N.1.1, N.1.2, dst.)
   - Penjelasan teori yang jelas dan mendalam
   - Contoh kode Python yang lengkap dan bisa dijalankan
   - Tabel perbandingan dan ringkasan
   - Diagram ASCII untuk visualisasi
   - Blockquote untuk insight penting
   - Studi kasus konteks Indonesia
4. **AI Corner**: Cara menggunakan AI untuk topik bab tersebut (progresif dari Dasar ke Mahir)
5. **Latihan Soal**: 3 tingkat (Dasar, Menengah, Mahir), masing-masing 3-5 soal
6. **Rangkuman**: Poin-poin utama bab
7. **Referensi**: Sumber yang digunakan

**Setiap bab harus substantif** — minimal 600-1000+ baris markdown (setara 30-40 halaman cetak).

**Catatan konten bab spesifik:**
- **Bab 1**: Sejarah algoritma (Al-Khwarizmi sebagai warisan Islam!), 4 pilar computational thinking, flowchart notation lengkap, pseudocode conventions, mengapa Python
- **Bab 3**: Decision tables, truth tables, operator boolean, short-circuit evaluation
- **Bab 4**: Loop trace tables, pola-pola umum perulangan, sentinel value, counter vs flag
- **Bab 5**: Diagram top-down design, pass by value, scope rules, DRY principle, docstrings
- **Bab 8**: Kapan pakai list vs dict vs set vs tuple (decision tree)
- **Bab 9-10**: Step-by-step trace tables untuk setiap algoritma, ASCII visualization
- **Bab 11**: Recursion tree diagram, call stack visualization, memoization hint
- **Bab 12**: Grafik perbandingan Big-O, amortized analysis sederhana, space complexity
- **Bab 13**: AI pair programming workflow lengkap, framework CRIDE untuk prompt engineering, cara memvalidasi kode dari AI, ethical guidelines
- **Bab 14**: Panduan proyek end-to-end yang lengkap — dari perumusan masalah hingga presentasi

**00-halaman-depan.md**:
- Judul buku, penulis, institusi
- **"Jakarta, Februari 2026"** (BUKAN 2025!)
- **"Edisi Pertama, 2026"** (BUKAN 2025!)
- Identitas buku (tabel)
- Kata Pengantar (بسم الله + Assalamu'alaikum + paragraf pengantar)
- Daftar Isi (lengkap 14 bab + penutup + lampiran)
- Peta Capaian Pembelajaran (diagram ASCII)
- Petunjuk Penggunaan Buku

**mengapa-buku-ini.md**: Lihat Bagian G di atas — positioning dan 7 diferensiator

**penutup.md**:
- Refleksi per bagian (Bagian I-IV, semua 14 bab disebutkan)
- Kompetensi yang telah diraih
- Jalur karir (Software Engineer, Backend Developer, Full-Stack, Mobile Dev, DevOps, Data Engineer)
- Roadmap lanjutan (OOP, Database, Web Development, Mobile, Cloud, AI/ML)
- Pesan untuk mahasiswa (4 prinsip)
- Refleksi Islami (Al-Khwarizmi, ilmu yang bermanfaat, amanah)
- Tanda tangan: `Jakarta, Februari 2026` + `Tri Aji Nugroho, S.T., M.T.`

**lampiran.md**:
- A: Tabel ASCII
- B: Python Syntax Cheat Sheet (formularium)
- C: Glosarium Istilah (bilingual Indonesia-English)
- D: Panduan Instalasi Python & IDE
- E: Daftar Pustaka Lengkap
- F: Indeks

#### K.8 Datasets (datasets/README.md)
Untuk mata kuliah pemrograman, ini berisi:
- Panduan sumber latihan soal (HackerRank, LeetCode Easy, Advent of Code)
- Contoh file CSV/TXT untuk latihan file I/O
- Problem set bertema Indonesia
- Link ke resource tambahan

---

### L. ATURAN KONSISTENSI & QUALITY CONTROL

**WAJIB dipatuhi di SELURUH dokumen:**

1. **Tanggal**: Hari ini 28 Februari 2026. Semester Genap 2025/2026. Semua dokumen harus konsisten — JANGAN gunakan "2025" sebagai tahun publikasi. Gunakan "Jakarta, Februari 2026" dan "Edisi Pertama, 2026".

2. **Referensi bab**: Setiap referensi ke nomor bab HARUS sesuai dengan Daftar Isi. Proyek akhir = **Bab 14** (BUKAN Bab 13). AI-Augmented Programming = **Bab 13** (BUKAN Bab 14). Verifikasi sebelum finalisasi.

3. **Nama mata kuliah**: Selalu "Algoritma dan Pemrograman" — jangan "Algoritma & Pemrograman", "AlPro", atau variasi lain di dokumen formal.

4. **Credential**: Selalu "Tri Aji Nugroho, S.T., M.T." — jangan abbreviated.

5. **CPMK traceability**: Setiap Sub-CPMK di RPS harus bisa ditelusuri ke CPMK. Setiap bab buku ajar harus menyebutkan Sub-CPMK yang dicakup. Setiap asesmen harus menunjukkan CPMK yang diukur.

6. **Bobot asesmen**: Harus selalu berjumlah 100% (15+10+20+25+25+5 = 100%).

7. **Kode Python**: Semua kode harus Google Colab-compatible, menggunakan Python 3.x, dengan komentar dalam bahasa Indonesia.

8. **AI literacy progression**: Tabel progresi AI Corner HARUS mencakup Bab 1-14 (JANGAN berhenti di Bab 13). Level terakhir (Bab 12-14) = "Mahir".

9. **Penutup**: HARUS merefleksikan SEMUA 14 bab, bukan hanya sebagian.

10. **Footer**: Setiap file diakhiri dengan: `*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia`

---

### M. URUTAN PEMBUATAN (GENERATION ORDER)

Karena volume konten sangat besar, generate dalam batch berikut:

**Batch 1**: Strategic Analysis + RPS + RTM + README
**Batch 2**: Buku Ajar — Halaman Depan + Mengapa Buku Ini + Bab 1-4
**Batch 3**: Buku Ajar — Bab 5-7 + Bab 8-11
**Batch 4**: Buku Ajar — Bab 12-14 + Penutup + Lampiran
**Batch 5**: Modul Mingguan — Week 1-8
**Batch 6**: Modul Mingguan — Week 9-16
**Batch 7**: Lab Praktikum — Lab 1-7
**Batch 8**: Lab Praktikum — Lab 9-14
**Batch 9**: Asesmen — Semua 5 file
**Batch 10**: Datasets README + final review

Setelah setiap batch, jalankan **VERIFICATION CHECKLIST** berikut:

```
CHECKLIST VERIFIKASI:
[ ] Semua tanggal mengacu 2026, BUKAN 2025
[ ] Semua file menyebut "Algoritma dan Pemrograman" sebagai nama MK
[ ] Semua file mencantumkan "Tri Aji Nugroho, S.T., M.T."
[ ] mengapa-buku-ini.md mereferensi "Bab 14" untuk proyek akhir
[ ] Daftar Isi di halaman depan mencantumkan semua 14 bab + penutup + lampiran
[ ] penutup.md merefleksikan seluruh Bab 1-14 per Bagian
[ ] Setiap bab memiliki: Tujuan Pembelajaran, sections, AI Corner, Latihan Soal (3 level), Rangkuman, Referensi
[ ] Setiap modul memiliki: Informasi Modul, Tujuan, Materi, Kegiatan, Penugasan, Referensi
[ ] Setiap lab memiliki: Tujuan, Persiapan, Langkah-langkah, Tantangan, Checklist
[ ] Nomor CPMK konsisten di seluruh RPS, RTM, buku ajar, dan asesmen
[ ] Bobot asesmen = 100% (15+10+20+25+25+5)
[ ] Semua kode Python kompatibel Google Colab
[ ] Nilai-nilai Islami terintegrasi natural
[ ] Progresi AI Corner mencakup Bab 1-14
```

---

### N. CONTOH POLA STRUKTUR

#### Pola Header Bab Buku Ajar:
```markdown
# BAB 1: PENGANTAR ALGORITMA DAN COMPUTATIONAL THINKING

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Bloom's |
|----------|-----------|---------|
| CPMK-1.1 | Mendefinisikan konsep algoritma dan sejarahnya | C1 |
| CPMK-1.2 | Menjelaskan 4 pilar computational thinking | C2 |
| CPMK-1.3 | Membuat flowchart dan pseudocode sederhana | C3 |
| CPMK-1.4 | Menjelaskan peran pemrograman di era AI | C2 |

---

## 1.1 Apa Itu Algoritma?
### 1.1.1 Definisi dan Sejarah
[konten...]

## AI Corner: Memulai dengan AI
[konten progresif...]

## Latihan Soal
### Tingkat Dasar
1. ...
### Tingkat Menengah
1. ...
### Tingkat Mahir
1. ...

## Rangkuman
- ...

## Referensi
- ...
```

#### Pola Header Modul Mingguan:
```markdown
# Minggu 1: Pengantar Algoritma dan Computational Thinking di Era AI

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Algoritma dan Pemrograman (3 SKS) |
| **Minggu** | 1 dari 16 |
| **Topik** | Pengantar Algoritma dan Computational Thinking |
| **CPMK** | CPMK-1 |
| **Durasi** | 150 menit |
| **Metode** | Ceramah interaktif + Diskusi + Praktik |

## Tujuan Pembelajaran
Setelah menyelesaikan modul ini, mahasiswa mampu:
1. Mendefinisikan konsep algoritma... (C1)
2. ...
```

#### Pola Header Lab:
```markdown
# Lab 01: Setup Python dan Google Colab

**Mata Kuliah:** Algoritma dan Pemrograman
**Semester:** Genap 2025/2026
**Durasi:** 75 menit
**Prasyarat:** Tidak ada

---

## Tujuan Praktikum
Setelah menyelesaikan lab ini, mahasiswa mampu:
1. ...

## Persiapan
- ...

## Langkah-langkah
### Langkah 1: ...
```

---

### O. ANTI-PATTERN — JANGAN LAKUKAN INI

1. **JANGAN** gunakan "2025" sebagai tahun publikasi di manapun. Gunakan "2026".
2. **JANGAN** referensi nomor bab di tabel positioning tanpa verifikasi dengan Daftar Isi.
3. **JANGAN** skip bab proyek akhir — Bab 14 harus bab yang lengkap dan substantif.
4. **JANGAN** hentikan tabel progresi AI literacy sebelum Bab 14.
5. **JANGAN** gunakan nama mata kuliah yang inkonsisten di file berbeda.
6. **JANGAN** buat penutup yang hanya mereferensi sebagian bab.
7. **JANGAN** copy pola mata kuliah statistik tanpa adaptasi — ini mata kuliah PEMROGRAMAN, bukan statistik. Contoh-contoh harus tentang menulis kode, bukan menganalisis data.
8. **JANGAN** buat kode Python yang tidak bisa dijalankan di Google Colab.
9. **JANGAN** integrasikan nilai Islami secara dipaksakan — harus natural dan kontekstual.
10. **JANGAN** lupa sertakan lab-08 yang di-skip (karena minggu 8 = UTS, tidak ada lab).

---

Mulai generate dari **Batch 1** (Strategic Analysis + RPS + RTM + README). Setelah selesai, lanjut ke batch berikutnya sesuai urutan. Pastikan setiap file lengkap, substantif, dan konsisten.

## [AKHIR PROMPT]
