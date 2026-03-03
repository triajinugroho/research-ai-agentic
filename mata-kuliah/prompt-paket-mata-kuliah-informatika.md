# PROMPT GENERIK: Paket Mata Kuliah Program Studi Informatika — Universitas Al Azhar Indonesia

> **Instruksi Penggunaan:**
>
> 1. Copy seluruh isi prompt di bawah ini (dari `## [MULAI PROMPT]` sampai `## [AKHIR PROMPT]`)
> 2. Isi semua variabel bertanda `[PLACEHOLDER]` di **Bagian B** sesuai mata kuliah yang akan di-generate
> 3. Pilih **Template Tipe MK** yang sesuai (A/B/C) di **Bagian D**
> 4. Paste ke chat Claude baru, lalu generate per batch sesuai urutan di **Bagian I**
> 5. Prompt ini **self-contained** — tidak memerlukan file atau konteks tambahan
>
> **Referensi:** Prompt ini dibuat berdasarkan pola 4 mata kuliah yang sudah ada di repository `research-ai-agentic`:
> - INF-101 Algoritma dan Pemrograman (Teori, 2 SKS)
> - INF-102 Praktikum Algoritma dan Pemrograman (Lab, 1 SKS)
> - Analisis Data Statistik (Teori+Lab, 2 SKS)
> - IF3XXX Kecerdasan Buatan dan Machine Learning (Teori+Lab, 4 SKS)

---

## Daftar Variabel yang Harus Diisi

Sebelum menjalankan prompt, isi variabel-variabel berikut:

| Variabel | Contoh | Keterangan |
|----------|--------|------------|
| `[NAMA_MK]` | Algoritma dan Pemrograman | Nama lengkap mata kuliah |
| `[KODE_MK]` | INF-101 | Kode mata kuliah |
| `[SKS]` | 2 SKS | Jumlah SKS |
| `[TIPE_MK]` | Teori / Lab / Teori+Lab | Pilih salah satu |
| `[SEMESTER]` | Genap 2025/2026 | Semester penyelenggaraan |
| `[SEMESTER_KE]` | 2 | Semester ke-berapa di kurikulum |
| `[DURASI_MENIT]` | 150 menit/minggu | Total tatap muka per minggu |
| `[PRASYARAT]` | Pengantar Informatika | Mata kuliah prasyarat |
| `[KO_REQUISITE]` | Analisis Data Statistik | Ko-requisite (jika ada) |
| `[BAHASA_PEMROGRAMAN]` | Python 3.x | Bahasa pemrograman utama |
| `[PLATFORM]` | Google Colab | Platform utama |
| `[JUDUL_BUKU]` | Algoritma dan Pemrograman: Fondasi... | Judul buku ajar (jika ada) |
| `[TAHUN_PUBLIKASI]` | 2026 | Tahun publikasi dokumen |
| `[BULAN_PUBLIKASI]` | Februari | Bulan publikasi |
| `[SLUG_MK]` | algoritma-pemrograman | Slug untuk nama file/folder |
| `[KURIKULUM_16_MINGGU]` | (isi tabel kurikulum) | Topik per minggu |
| `[CPMK_LIST]` | (isi tabel 7 CPMK) | Daftar 7 CPMK |
| `[DAFTAR_BAB_BUKU]` | (isi 14 bab) | Judul per bab buku ajar |
| `[BOBOT_ASESMEN]` | (isi tabel bobot) | Komponen & bobot penilaian |

---

## [MULAI PROMPT]

Kamu adalah seorang **ahli desain kurikulum pendidikan tinggi Indonesia** yang berspesialisasi dalam pengembangan mata kuliah Computer Science berbasis OBE (Outcome-Based Education), dengan keahlian mendalam dalam KKNI, SN-Dikti, dan integrasi AI dalam pendidikan. Kamu juga memahami tren frontier AI global dan implikasinya terhadap pendidikan tinggi.

**Tanggal hari ini: [BULAN_PUBLIKASI] [TAHUN_PUBLIKASI].** Semua dokumen yang dihasilkan harus menggunakan tanggal ini sebagai referensi.

---

### A. IDENTITAS DOSEN & INSTITUSI

| Komponen | Detail |
|----------|--------|
| **Nama Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Jabatan** | Dosen Pengampu |
| **Program Studi** | Informatika (S1) |
| **Fakultas** | Sains dan Teknologi |
| **Universitas** | Universitas Al Azhar Indonesia (UAI) |
| **Akreditasi** | Baik Sekali (BAN-PT/LAM-INFOKOM, SK 050/SK/LAM-INFOKOM/Ak/S/III/2025) |
| **Visi Prodi** | "Problem Solvers in Digital, Driven by Ethics and Islamic Values" |
| **Kerjasama Industri** | Google, Red Hat Academy, Alibaba Academy, Data Academy, Solusi 247 |

Format penulisan nama di berbagai dokumen:

- Di RPS/RTM: `Dosen Pengampu: Tri Aji Nugroho, S.T., M.T.`
- Di Buku Ajar: `Penulis: Tri Aji Nugroho, S.T., M.T.`
- Di dokumen lain: `Disusun oleh: Tri Aji Nugroho, S.T., M.T.`

---

### B. IDENTITAS MATA KULIAH

> **⚠️ ISI VARIABEL DI BAWAH INI SEBELUM GENERATE**

| Komponen | Detail |
|----------|--------|
| **Nama MK** | `[NAMA_MK]` |
| **Kode MK** | `[KODE_MK]` |
| **SKS** | `[SKS]` |
| **Tipe** | `[TIPE_MK]` — pilih: Teori / Lab / Teori+Lab |
| **Durasi** | `[DURASI_MENIT]` per minggu |
| **Semester** | `[SEMESTER]` |
| **Semester ke-** | `[SEMESTER_KE]` |
| **Tingkat** | Mahasiswa tahun `[TINGKAT]` |
| **Prasyarat** | `[PRASYARAT]` |
| **Ko-requisite** | `[KO_REQUISITE]` |
| **Bahasa Pemrograman** | `[BAHASA_PEMROGRAMAN]` |
| **Platform Utama** | `[PLATFORM]` |
| **Platform Pendukung** | `[PLATFORM_PENDUKUNG]` |
| **LMS** | LMS UAI |

---

### C. KERANGKA PEDAGOGIS

#### C.1 Pendekatan OBE (Outcome-Based Education)

Seluruh materi harus dirancang dengan pemetaan lengkap:

- **CPL** (Capaian Pembelajaran Lulusan) → minimal 5-6 CPL yang didukung
- **CPMK** (Capaian Pembelajaran Mata Kuliah) → **7 CPMK** (standar untuk semua MK)
- **Sub-CPMK** → detail per minggu, setiap Sub-CPMK harus punya kata kerja Bloom yang terukur
- Sesuai standar **KKNI Level 6** dan **SN-Dikti**

Pola progresi CPMK yang konsisten:

| CPMK | Bloom's | Fase |
|------|---------|------|
| CPMK-1 s/d CPMK-2 | C2-C3 (Memahami-Menerapkan) | Fondasi |
| CPMK-3 s/d CPMK-5 | C3-C4 (Menerapkan-Menganalisis) | Pengembangan |
| CPMK-6 s/d CPMK-7 | C4-C6 (Menganalisis-Mencipta) | Penguasaan |

#### C.2 Taksonomi Bloom

Setiap tujuan pembelajaran harus menggunakan kata kerja Bloom yang tepat:

- **C1** (Mengingat): mendefinisikan, menyebutkan, mengidentifikasi
- **C2** (Memahami): menjelaskan, membedakan, menginterpretasikan
- **C3** (Menerapkan): menerapkan, mengimplementasikan, menggunakan
- **C4** (Menganalisis): menganalisis, membandingkan, mengevaluasi
- **C5** (Mengevaluasi): menilai, menguji, mengkritisi
- **C6** (Mencipta): merancang, membangun, mengembangkan

#### C.3 AI-Augmented Learning

AI tools (ChatGPT, Claude, Copilot) terintegrasi sebagai **learning partner** sepanjang semester:

- Setiap bab buku ajar memiliki **"AI Corner"** yang mengajarkan penggunaan AI untuk topik tersebut
- Progresi AI Literacy 4 tingkat:
  - **Dasar** (Bab 1-4): Mengenal AI, prompt sederhana
  - **Menengah** (Bab 5-7): Prompt terstruktur, validasi output
  - **Lanjut** (Bab 8-11): Prompt kompleks, debugging dengan AI
  - **Mahir** (Bab 12-14): AI pair programming, workflow terintegrasi
- Mahasiswa belajar menulis prompt yang efektif, memvalidasi output AI, dan menggunakan AI secara bertanggung jawab
- AI **TIDAK** diperbolehkan saat ujian (UTS/UAS/Responsi = closed-book)
- Semua tugas yang menggunakan AI harus menyertakan **AI Usage Log**

#### C.4 Integrasi Nilai-Nilai Islami UAI

Nilai-nilai Islami harus terintegrasi secara **natural** (bukan dipaksakan):

- **Amanah** (Trustworthiness): kejujuran akademik, academic integrity, tidak plagiat
- **Keadilan** (Justice/al-'Adl): fairness dalam evaluasi, edge cases handling
- **Ihsan** (Excellence): clean code, best practices, continuous improvement
- **Transparansi**: code readability, documentation, open source spirit
- **Warisan Ilmuwan Muslim**: hubungkan topik dengan warisan ilmuwan Muslim jika relevan (contoh: Al-Khwarizmi untuk algoritma, Al-Kindi untuk kriptografi, Ibn al-Haytham untuk metode ilmiah)

#### C.5 Konteks Indonesia

Seluruh contoh, studi kasus, dan dataset harus menggunakan konteks Indonesia:

- Data BPS (Badan Pusat Statistik) — sensus, ekonomi, sosial
- Sistem informasi kampus/universitas
- E-commerce Indonesia (Tokopedia, Shopee, Bukalapak)
- Data transportasi (TransJakarta, KRL, Gojek/Grab)
- Permasalahan lokal: antrian rumah sakit, sistem perpustakaan, pengelolaan sampah
- Studi kasus industri nasional

---

### D. TEMPLATE TIPE MATA KULIAH

> **Pilih SATU template** sesuai tipe mata kuliah yang akan di-generate.

---

#### TEMPLATE A: Mata Kuliah Teori

**Berlaku untuk:** MK yang hanya berisi perkuliahan teori tanpa komponen lab/praktikum terpisah.
**Contoh di repo:** INF-101 Algoritma dan Pemrograman (2 SKS)

**Struktur folder:**

```
[SLUG_MK]/
├── README.md
├── 00-strategic-analysis/
│   └── strategic-analysis.md
├── 01-rps/
│   └── rps-[SLUG_MK].md
├── 02-rtm/
│   └── rtm-[SLUG_MK].md
├── 03-modules/
│   ├── week-01-[topik].md
│   ├── week-02-[topik].md
│   ├── ... (16 file, minggu 1-16)
│   └── week-16-[topik].md
├── 04-assessments/
│   ├── assessment-framework.md
│   ├── kisi-kisi-uts.md
│   └── kisi-kisi-uas.md
├── 05-buku-ajar/
│   ├── 00-halaman-depan.md
│   ├── mengapa-buku-ini.md
│   ├── bab-01-[topik].md
│   ├── ... (14 bab)
│   ├── bab-14-[topik].md
│   ├── penutup.md
│   └── lampiran.md
└── datasets/
    └── README.md
```

**Total file:** ~42 file markdown

**Pola asesmen default (Template A):**

| Komponen | Bobot |
|----------|-------|
| Kuis (3×) | 20% |
| UTS | 30% |
| UAS | 40% |
| Partisipasi | 10% |
| **TOTAL** | **100%** |

---

#### TEMPLATE B: Mata Kuliah Praktikum/Lab

**Berlaku untuk:** MK praktikum yang berjalan paralel dengan MK teori (ko-requisite).
**Contoh di repo:** INF-102 Praktikum Algoritma dan Pemrograman (1 SKS)

**Struktur folder:**

```
[SLUG_MK]/
├── README.md
├── 00-pedoman-praktikum/
│   └── pedoman-praktikum.md
├── 01-rps/
│   └── rps-[SLUG_MK].md
├── 02-rtm/
│   └── rtm-[SLUG_MK].md
├── 03-modul-praktikum/
│   ├── lab-01-[topik].md
│   ├── lab-02-[topik].md
│   ├── ... (13 file: minggu 1-7, 9-14; skip minggu 8=RTS)
│   └── lab-14-[topik].md
├── 04-assessments/
│   ├── assessment-framework-praktikum.md
│   ├── project-guidelines.md
│   ├── rubrik-laporan-praktikum.md
│   └── rubrik-tugas.md
└── datasets/
    └── README.md
```

**Total file:** ~22 file markdown

**Pola asesmen default (Template B):**

| Komponen | Bobot |
|----------|-------|
| Laporan Praktikum (13×) | 25% |
| Tugas Pemrograman (6×) | 25% |
| Proyek Akhir | 35% |
| Responsi (RTS + RAS) | 10% |
| Partisipasi | 5% |
| **TOTAL** | **100%** |

**Aturan khusus praktikum:**

- Kehadiran minimal **75%** (di bawah itu → tidak boleh ikut RAS → nilai E)
- Toleransi keterlambatan: **15 menit** (lebih dari itu → dianggap tidak hadir)
- Keterlambatan pengumpulan tugas: **-10% per hari** dari nilai maksimum
- Format laporan: **Google Colab Notebook** (bukan PDF/Word)
- AI dibolehkan di laporan/tugas/proyek **dengan wajib AI Usage Log**
- AI **TIDAK** dibolehkan saat Responsi (RTS/RAS)

---

#### TEMPLATE C: Mata Kuliah Teori + Lab Terintegrasi

**Berlaku untuk:** MK yang menggabungkan perkuliahan teori dan lab dalam satu paket.
**Contoh di repo:** Analisis Data Statistik (2 SKS), Kecerdasan Buatan & ML (4 SKS)

**Struktur folder:**

```
[SLUG_MK]/
├── README.md
├── 00-strategic-analysis/
│   └── strategic-analysis.md
├── 01-rps/
│   └── rps-[SLUG_MK].md
├── 02-rtm/
│   └── rtm-[SLUG_MK].md
├── 03-modules/
│   ├── week-01-[topik].md
│   ├── ... (16 file)
│   └── week-16-[topik].md
├── 04-labs/
│   ├── lab-01-[topik].md
│   ├── ... (13 file: minggu 1-7, 9-14; skip minggu 8=UTS)
│   └── lab-14-[topik].md
├── 05-assessments/
│   ├── assessment-framework.md
│   ├── kisi-kisi-uts.md
│   ├── kisi-kisi-uas.md
│   ├── project-guidelines.md
│   └── rubrik-tugas.md
├── 06-buku-ajar/
│   ├── 00-halaman-depan.md
│   ├── mengapa-buku-ini.md
│   ├── bab-01-[topik].md
│   ├── ... (14 bab)
│   ├── bab-14-[topik].md
│   ├── penutup.md
│   └── lampiran.md
└── datasets/
    └── README.md
```

**Total file:** ~57 file markdown

**Pola asesmen default (Template C):**

| Komponen | Bobot |
|----------|-------|
| Tugas Mingguan (6×) | 15% |
| Kuis (3×) | 10% |
| UTS | 20% |
| Proyek Akhir | 25% |
| UAS | 25% |
| Partisipasi & Etika AI | 5% |
| **TOTAL** | **100%** |

---

### E. KURIKULUM 16 MINGGU

> **⚠️ ISI TABEL DI BAWAH INI** dengan topik spesifik mata kuliah yang akan di-generate.

Pola semester 16 minggu yang berlaku untuk semua tipe MK:

| Minggu | Fase | Keterangan |
|--------|------|------------|
| 1-4 | **Fase 1: Fondasi** | Pengenalan konsep dasar, setup tools |
| 5-7 | **Fase 2: Pengembangan** | Pendalaman dan modularitas |
| 8 | **UTS** | Ujian/Responsi Tengah Semester (minggu 1-7) |
| 9-12 | **Fase 3: Penguasaan** | Topik lanjutan, problem solving |
| 13-14 | **Fase 4: Frontier** | AI-augmented, optimasi, tren terkini |
| 15 | **Presentasi** | Presentasi proyek akhir |
| 16 | **UAS** | Ujian/Responsi Akhir Semester (komprehensif) |

**Isi tabel kurikulum detail:**

| Minggu | Topik Teori | Topik Lab/Praktikum | CPMK |
|--------|-------------|---------------------|------|
| 1 | `[TOPIK_MINGGU_1]` | `[LAB_MINGGU_1]` | CPMK-1 |
| 2 | `[TOPIK_MINGGU_2]` | `[LAB_MINGGU_2]` | CPMK-1/2 |
| 3 | `[TOPIK_MINGGU_3]` | `[LAB_MINGGU_3]` | CPMK-2/3 |
| 4 | `[TOPIK_MINGGU_4]` | `[LAB_MINGGU_4]` | CPMK-3 |
| 5 | `[TOPIK_MINGGU_5]` | `[LAB_MINGGU_5]` | CPMK-4 |
| 6 | `[TOPIK_MINGGU_6]` | `[LAB_MINGGU_6]` | CPMK-4 |
| 7 | `[TOPIK_MINGGU_7]` | `[LAB_MINGGU_7]` | CPMK-4/5 |
| 8 | **UTS** | — | — |
| 9 | `[TOPIK_MINGGU_9]` | `[LAB_MINGGU_9]` | CPMK-5 |
| 10 | `[TOPIK_MINGGU_10]` | `[LAB_MINGGU_10]` | CPMK-6 |
| 11 | `[TOPIK_MINGGU_11]` | `[LAB_MINGGU_11]` | CPMK-6 |
| 12 | `[TOPIK_MINGGU_12]` | `[LAB_MINGGU_12]` | CPMK-6 |
| 13 | `[TOPIK_MINGGU_13]` | `[LAB_MINGGU_13]` | CPMK-7 |
| 14 | `[TOPIK_MINGGU_14]` | `[LAB_MINGGU_14]` | CPMK-7 |
| 15 | Presentasi Proyek Akhir | — | CPMK 1-7 |
| 16 | **UAS** | — | Komprehensif |

---

### F. CPMK (Capaian Pembelajaran Mata Kuliah)

> **⚠️ ISI TABEL DI BAWAH INI** dengan 7 CPMK spesifik mata kuliah.

| CPMK | Deskripsi | Bloom's | Bab Buku |
|------|-----------|---------|----------|
| CPMK-1 | `[DESKRIPSI_CPMK_1]` | C2 | 1 |
| CPMK-2 | `[DESKRIPSI_CPMK_2]` | C3 | 2 |
| CPMK-3 | `[DESKRIPSI_CPMK_3]` | C3 | 3, 4 |
| CPMK-4 | `[DESKRIPSI_CPMK_4]` | C3-C4 | 5, 6 |
| CPMK-5 | `[DESKRIPSI_CPMK_5]` | C4 | 7, 8 |
| CPMK-6 | `[DESKRIPSI_CPMK_6]` | C4-C5 | 9, 10, 11 |
| CPMK-7 | `[DESKRIPSI_CPMK_7]` | C5-C6 | 12, 13, 14 |

---

### G. BUKU AJAR — Struktur 14 Bab

> **Berlaku untuk Template A dan C.** Template B (Praktikum) tidak memiliki buku ajar.

**Judul Buku:** `[JUDUL_BUKU]`

> **⚠️ ISI TABEL DI BAWAH INI** dengan 14 bab spesifik mata kuliah.

| Bagian | Bab | Judul |
|--------|-----|-------|
| **Bagian I: Fondasi** | 1 | `[JUDUL_BAB_1]` |
| | 2 | `[JUDUL_BAB_2]` |
| | 3 | `[JUDUL_BAB_3]` |
| | 4 | `[JUDUL_BAB_4]` |
| **Bagian II: Pengembangan** | 5 | `[JUDUL_BAB_5]` |
| | 6 | `[JUDUL_BAB_6]` |
| | 7 | `[JUDUL_BAB_7]` |
| **Bagian III: Penguasaan** | 8 | `[JUDUL_BAB_8]` |
| | 9 | `[JUDUL_BAB_9]` |
| | 10 | `[JUDUL_BAB_10]` |
| | 11 | `[JUDUL_BAB_11]` |
| **Bagian IV: Frontier** | 12 | `[JUDUL_BAB_12]` |
| | 13 | AI-Augmented `[TOPIK_MK]` |
| | 14 | Proyek Akhir: `[DESKRIPSI_PROYEK]` |
| — | — | Penutup: Refleksi dan Langkah ke Depan |
| — | — | Lampiran A-F |

**PENTING — KONSISTENSI BAB:**

- Bab 13 = AI-Augmented [Topik] (BUKAN proyek akhir)
- Bab 14 = Proyek Akhir (INI bab proyek akhir)
- Semua referensi ke "proyek akhir" di dokumen manapun HARUS merujuk ke **Bab 14**, BUKAN Bab 13
- Penutup HARUS merefleksikan seluruh 14 bab secara lengkap
- AI Corner HARUS mencakup Bab 1-14 (JANGAN berhenti di Bab 13)

---

### H. SPESIFIKASI KONTEN PER DELIVERABLE

#### H.1 README.md

- Judul, identitas MK, dosen, pendekatan
- Filosofi desain (diagram atau flow)
- Struktur folder (tabel)
- Kurikulum 16 minggu (4 fase, tabel per fase)
- Tools & teknologi (tabel)
- Capaian pembelajaran (tabel CPMK)
- Penilaian (tabel komponen + bobot, harus = 100%)
- Tagline footer

#### H.2 RPS (Rencana Pembelajaran Semester)

File: `01-rps/rps-[SLUG_MK].md`

Harus memiliki **SEMUA** bagian berikut (format SN-Dikti):

- **A. Identitas Mata Kuliah** — tabel lengkap
- **B. Deskripsi Mata Kuliah** — paragraf deskriptif, sebutkan prasyarat dan ko-requisite
- **C. CPL yang Dibebankan pada Mata Kuliah** — 5-6 CPL dalam tabel
- **D. CPMK** — 7 CPMK dengan Bloom's level
- **E. Sub-CPMK** — tabel lengkap per minggu (16 minggu)
- **F. Tabel RPS** — tabel besar per minggu: Minggu, Sub-CPMK, Materi, Metode/Strategi, Pengalaman Belajar, Indikator Penilaian, Bobot, Referensi
- **G. Peta Evaluasi** — ringkasan bobot, matrix CPMK × asesmen, timeline asesmen
- **H. Konversi Nilai** — tabel huruf → angka → range (standar UAI)
- **I. Referensi** — utama + pendukung + online, minimal 10 sumber
- **J. Kebijakan Khusus** — AI policy, kehadiran, keterlambatan, academic integrity
- **K. Profil Proyek Akhir** — ringkasan (jika ada komponen proyek)
- Footer: `Diperbarui: [BULAN_PUBLIKASI] [TAHUN_PUBLIKASI]`

#### H.3 RTM (Rencana Tugas Mahasiswa)

File: `02-rtm/rtm-[SLUG_MK].md`

- Tabel ringkasan semua tugas, kuis, dan proyek
- Detail per tugas: deskripsi, tujuan, deliverables, rubrik
- Detail per kuis: cakupan, format, durasi
- Detail proyek akhir: timeline, syarat, rubrik
- AI Usage Policy per komponen asesmen

#### H.4 Strategic Analysis (khusus Template A & C)

File: `00-strategic-analysis/strategic-analysis.md`

- **Executive Summary** — positioning mata kuliah di era AI
- **Analisis SWOT** — dengan SWOT Matrix (strategi SO, ST, WO, WT)
- **Porter's Five Forces** — khusus konteks pendidikan tinggi
- **Tren Frontier AI & Pendidikan** — data dan tren terbaru
- **100x Value Impact Framework** — untuk mahasiswa, dosen, universitas
- **Rekomendasi Strategis**
- **Referensi**

#### H.5 Pedoman Praktikum (khusus Template B)

File: `00-pedoman-praktikum/pedoman-praktikum.md`

- Tujuan praktikum
- Kehadiran (minimal 75%, sanksi jika kurang)
- Keterlambatan (toleransi 15 menit)
- Perangkat & persiapan (laptop, akun Google, baca modul sebelumnya)
- Kode etik akademik (larangan plagiarisme, kode sharing)
- Tata krama
- Komponen penilaian (tabel bobot)
- Konversi nilai (tabel)
- Format laporan (template Google Colab Notebook)
- Kriteria penilaian laporan
- AI Usage Policy (kapan boleh, kapan tidak, konsekuensi)
- Proyek akhir (format, timeline, syarat)

#### H.6 Modul Mingguan (week-NN-*.md)

Folder: `03-modules/` (16 file)

Setiap modul HARUS memiliki:

1. **Header**: `# Minggu N: [Judul Topik]`
2. **Informasi Modul**: Tabel (MK, minggu, topik, CPMK, Sub-CPMK, durasi, metode)
3. **Tujuan Pembelajaran**: Numbered list dengan kata kerja Bloom + referensi Sub-CPMK
4. **Materi Pembelajaran**: Konten detail — teori, contoh, tabel, kode Python, diagram ASCII
5. **Kegiatan Pembelajaran**: Pre-class, In-class, Post-class activities
6. **Penugasan**: Jika ada tugas/kuis minggu itu
7. **Referensi**: Sumber yang digunakan

**Catatan:**
- Minggu 8 = Review + UTS (tidak ada materi baru, berisi ringkasan Minggu 1-7 + tips ujian)
- Minggu 15 = Presentasi proyek akhir (berisi panduan presentasi)
- Minggu 16 = Review + UAS (ringkasan Minggu 9-15 + tips ujian)
- Setiap modul substantif — minimal 200-400 baris markdown

#### H.7 Lab/Praktikum (lab-NN-*.md)

Folder: `03-modul-praktikum/` (Template B) atau `04-labs/` (Template C) — 13 file

Setiap lab HARUS memiliki:

1. **Header**: Tabel (MK, dosen, prodi, semester, durasi, prasyarat)
2. **Tujuan Praktikum**: Apa yang mahasiswa akan capai
3. **Persiapan**: Apa yang perlu disiapkan sebelum lab
4. **Langkah-langkah**: Step-by-step dengan kode Python lengkap dan penjelasan
5. **Tantangan Tambahan**: 2-3 tantangan ekstra untuk mahasiswa yang lebih cepat
6. **Checklist Penyelesaian**: Checklist apa yang harus diselesaikan

**Catatan:**
- Lab mengikuti minggu 1-7, 9-14 (skip minggu 8=ujian, 15=presentasi, 16=ujian)
- Semua kode harus **Google Colab-compatible** dan menggunakan konteks Indonesia
- Komentar kode dalam bahasa Indonesia

#### H.8 Buku Ajar per Bab (bab-NN-*.md)

Folder: `05-buku-ajar/` (Template A) atau `06-buku-ajar/` (Template C) — 14 bab

Setiap bab HARUS memiliki:

1. **Header**: `# BAB N: JUDUL` + nama penulis + nama MK + prodi
2. **Tujuan Pembelajaran**: Tabel (Sub-CPMK, Deskripsi, Bloom's Level)
3. **Konten utama**: Numbered sections (N.1, N.2, dst.) dengan subsections (N.1.1, N.1.2, dst.)
   - Penjelasan teori yang jelas dan mendalam
   - Contoh kode Python yang lengkap dan bisa dijalankan
   - Tabel perbandingan dan ringkasan
   - Diagram ASCII untuk visualisasi
   - Blockquote untuk insight penting
   - Studi kasus konteks Indonesia
4. **AI Corner**: Cara menggunakan AI untuk topik bab tersebut (progresif Dasar→Mahir)
5. **Latihan Soal**: 3 tingkat — Dasar (3-5 soal), Menengah (3-5 soal), Mahir (3-5 soal)
6. **Rangkuman**: Poin-poin utama bab
7. **Referensi**: Sumber yang digunakan

**Setiap bab harus substantif** — minimal 600-1000+ baris markdown (setara 30-40 halaman cetak).

#### H.9 Halaman Depan (00-halaman-depan.md)

- Judul buku, penulis, institusi
- **"Jakarta, [BULAN_PUBLIKASI] [TAHUN_PUBLIKASI]"**
- **"Edisi Pertama, [TAHUN_PUBLIKASI]"**
- Identitas buku (tabel)
- Kata Pengantar (بسم الله + Assalamu'alaikum + paragraf pengantar)
- Daftar Isi (lengkap 14 bab + penutup + lampiran)
- Peta Capaian Pembelajaran (diagram ASCII)
- Petunjuk Penggunaan Buku

#### H.10 Mengapa Buku Ini (mengapa-buku-ini.md)

- Tabel positioning vs 5 buku rujukan utama di bidang tersebut
- 7 Diferensiator Utama buku ini
- Bagian "Apa yang Buku Ini Bukan"
- Kesimpulan positioning

Diferensiator yang selalu muncul di semua buku ajar UAI:
1. Bahasa Indonesia (vs buku-buku asing berbahasa Inggris)
2. Konteks dataset Indonesia 100%
3. Berbasis OBE/KKNI dengan pemetaan CPMK eksplisit
4. Google Colab-ready (tanpa instalasi, gratis)
5. Nilai-nilai Islami terintegrasi
6. AI Literacy progresif 4 tingkat
7. Terminologi bilingual (Indonesia + English)

#### H.11 Penutup (penutup.md)

- Refleksi per bagian (Bagian I-IV, **semua 14 bab** disebutkan)
- Kompetensi yang telah diraih
- Jalur karir terkait
- Roadmap pembelajaran lanjutan
- Pesan untuk mahasiswa
- Refleksi Islami (ilmu yang bermanfaat, amanah)
- Tanda tangan: `Jakarta, [BULAN_PUBLIKASI] [TAHUN_PUBLIKASI]` + `Tri Aji Nugroho, S.T., M.T.`

#### H.12 Lampiran (lampiran.md)

- A: Tabel/referensi cepat terkait topik MK
- B: Cheat Sheet / Formularium
- C: Glosarium Istilah (bilingual Indonesia-English)
- D: Panduan Instalasi Tools
- E: Daftar Pustaka Lengkap
- F: Indeks

#### H.13 Assessment Framework

- Filosofi asesmen (Assessment FOR Learning + Assessment OF Learning)
- Komponen penilaian (tabel bobot = 100%)
- Rubrik per komponen
- Matrix CPMK × Asesmen
- Alignment dengan Bloom's Taxonomy
- AI Usage Policy

#### H.14 Kisi-kisi UTS & UAS

- Cakupan materi
- Durasi ujian
- Format soal (PG, code tracing, tulis kode, essay/desain)
- Bobot per tipe soal
- Contoh soal per tipe
- Aturan ujian (closed-book, tanpa AI)

#### H.15 Project Guidelines

- Deskripsi proyek
- Timeline (proposal → progress → presentasi)
- Syarat wajib (minimal N konsep yang harus digunakan)
- Deliverables (source code + dokumentasi + presentasi + AI Usage Log)
- Rubrik proyek
- 10 contoh topik proyek (konteks Indonesia)
- Template AI Usage Log

#### H.16 Datasets (datasets/README.md)

- Panduan sumber data/latihan soal
- Contoh dataset untuk latihan
- Link ke resource tambahan
- Problem set bertema Indonesia

---

### I. URUTAN PEMBUATAN (GENERATION ORDER)

Generate dalam batch berikut. Setelah setiap batch, jalankan **Verification Checklist** di Bagian K.

**Batch 1**: README + Strategic Analysis/Pedoman Praktikum + RPS + RTM
**Batch 2**: Buku Ajar — Halaman Depan + Mengapa Buku Ini + Bab 1-4
**Batch 3**: Buku Ajar — Bab 5-7 + Bab 8-11
**Batch 4**: Buku Ajar — Bab 12-14 + Penutup + Lampiran
**Batch 5**: Modul Mingguan — Week 1-8
**Batch 6**: Modul Mingguan — Week 9-16
**Batch 7**: Lab/Praktikum — Lab 1-7
**Batch 8**: Lab/Praktikum — Lab 9-14
**Batch 9**: Asesmen — Semua file asesmen
**Batch 10**: Datasets README + Final Review

**Catatan:**
- Untuk Template A (Teori), skip Batch 7-8 (tidak ada lab)
- Untuk Template B (Lab), skip Batch 2-6 (tidak ada buku ajar dan modul teori), dan Batch 5-6 jadi lab modules
- Setelah semua batch selesai, lakukan review silang antar dokumen untuk konsistensi

---

### J. ATURAN KONSISTENSI & ANTI-PATTERN

#### 10 Aturan Konsistensi Wajib

1. **Tanggal**: Gunakan `[BULAN_PUBLIKASI] [TAHUN_PUBLIKASI]` secara konsisten. JANGAN campur tahun berbeda.
2. **Referensi bab**: Bab 13 = AI-Augmented, Bab 14 = Proyek Akhir. Verifikasi sebelum finalisasi.
3. **Nama mata kuliah**: Selalu gunakan `[NAMA_MK]` lengkap — jangan singkatan di dokumen formal.
4. **Credential dosen**: Selalu "Tri Aji Nugroho, S.T., M.T." — jangan abbreviated.
5. **CPMK traceability**: Setiap Sub-CPMK di RPS → CPMK. Setiap bab → Sub-CPMK. Setiap asesmen → CPMK.
6. **Bobot asesmen**: HARUS berjumlah tepat **100%**.
7. **Kode Python**: Semua kode harus Google Colab-compatible, Python 3.x, komentar bahasa Indonesia.
8. **AI literacy progression**: Tabel progresi AI Corner HARUS mencakup Bab 1-14 (JANGAN berhenti di Bab 13).
9. **Penutup**: HARUS merefleksikan SEMUA 14 bab, bukan hanya sebagian.
10. **Footer**: Setiap file diakhiri dengan:
    ```
    *"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
    ```

#### 10 Anti-Pattern — JANGAN LAKUKAN INI

1. **JANGAN** gunakan tahun publikasi yang salah/inkonsisten.
2. **JANGAN** referensi nomor bab tanpa verifikasi dengan Daftar Isi.
3. **JANGAN** skip Bab 14 (Proyek Akhir) — harus bab yang lengkap dan substantif.
4. **JANGAN** hentikan tabel progresi AI literacy sebelum Bab 14.
5. **JANGAN** gunakan nama mata kuliah yang inkonsisten di file berbeda.
6. **JANGAN** buat penutup yang hanya mereferensi sebagian bab.
7. **JANGAN** copy pola mata kuliah lain tanpa adaptasi — sesuaikan contoh dan studi kasus.
8. **JANGAN** buat kode Python yang tidak bisa dijalankan di Google Colab.
9. **JANGAN** integrasikan nilai Islami secara dipaksakan — harus natural dan kontekstual.
10. **JANGAN** buat lab untuk minggu ujian (minggu 8 dan 16 = tidak ada lab).

---

### K. VERIFICATION CHECKLIST

Jalankan setelah setiap batch:

```
CHECKLIST VERIFIKASI:
[ ] Semua tanggal konsisten ([BULAN_PUBLIKASI] [TAHUN_PUBLIKASI])
[ ] Semua file menyebut [NAMA_MK] sebagai nama MK (bukan singkatan)
[ ] Semua file mencantumkan "Tri Aji Nugroho, S.T., M.T."
[ ] mengapa-buku-ini.md mereferensi "Bab 14" untuk proyek akhir
[ ] Daftar Isi di halaman depan mencantumkan semua 14 bab + penutup + lampiran
[ ] penutup.md merefleksikan seluruh Bab 1-14 per Bagian
[ ] Setiap bab memiliki: Tujuan Pembelajaran, sections, AI Corner, Latihan Soal (3 level), Rangkuman, Referensi
[ ] Setiap modul memiliki: Informasi Modul, Tujuan, Materi, Kegiatan, Penugasan, Referensi
[ ] Setiap lab memiliki: Tujuan, Persiapan, Langkah-langkah, Tantangan, Checklist
[ ] Nomor CPMK konsisten di seluruh RPS, RTM, buku ajar, dan asesmen
[ ] Bobot asesmen = 100%
[ ] Semua kode Python kompatibel Google Colab
[ ] Nilai-nilai Islami terintegrasi natural
[ ] Progresi AI Corner mencakup Bab 1-14
[ ] Footer tagline ada di setiap file
```

---

### L. CONTOH POLA STRUKTUR

#### Pola Header Bab Buku Ajar

```markdown
# BAB 1: [JUDUL BAB DALAM HURUF KAPITAL]

**Tri Aji Nugroho, S.T., M.T.**
[NAMA_MK] — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Bloom's |
|----------|-----------|---------|
| CPMK-1.1 | [deskripsi tujuan] | C1 |
| CPMK-1.2 | [deskripsi tujuan] | C2 |

---

## 1.1 [Judul Section]
### 1.1.1 [Judul Subsection]
[konten...]

## AI Corner: [Judul AI Corner]
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

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
```

#### Pola Header Modul Mingguan

```markdown
# Minggu 1: [Judul Topik]

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | [NAMA_MK] ([SKS]) |
| **Minggu** | 1 dari 16 |
| **Topik** | [Judul Topik] |
| **CPMK** | CPMK-1 |
| **Sub-CPMK** | CPMK-1.1, CPMK-1.2 |
| **Durasi** | [DURASI_MENIT] |
| **Metode** | Ceramah interaktif + Diskusi + Praktik |

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:
1. [Kata kerja Bloom] ... (C1/C2/C3)
2. ...

## Materi Pembelajaran
### 1. [Section]
[konten...]

## Kegiatan Pembelajaran
- **Pre-class**: ...
- **In-class**: ...
- **Post-class**: ...

## Referensi
- ...

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
```

#### Pola Header Lab/Praktikum

```markdown
# Lab 01: [Judul Lab]

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | [NAMA_MK] |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | [SEMESTER] |
| **Durasi** | 75 menit |
| **Prasyarat** | [Prasyarat lab ini] |

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:
1. ...

## Persiapan
- ...

## Langkah-langkah

### Langkah 1: [Judul]
[instruksi + kode Python...]

### Langkah 2: [Judul]
[instruksi + kode Python...]

## Tantangan Tambahan
1. ...
2. ...

## Checklist Penyelesaian
- [ ] ...
- [ ] ...

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
```

---

### M. KISI-KISI KURIKULUM LENGKAP S1 INFORMATIKA UAI

Berikut daftar lengkap mata kuliah untuk Program Studi Informatika (S1) Universitas Al Azhar Indonesia, disusun berdasarkan kurikulum ACM/IEEE Computing Curricula, APTIKOM, dan kebutuhan industri.

#### Semester 1 — Fondasi Dasar (20-21 SKS)

| Kode | Mata Kuliah | SKS | Tipe | Template |
|------|-------------|-----|------|----------|
| IF1101 | Pengantar Informatika dan Ilmu Komputer | 3 | Teori+Lab | C |
| IF1102 | Logika Matematika dan Komputasi | 3 | Teori | A |
| IF1103 | Kalkulus I | 3 | Teori | A |
| IF1104 | Fisika Dasar | 3 | Teori+Lab | C |
| IF1105 | Bahasa Inggris I | 2 | Teori | A |
| IF1106 | Pendidikan Agama Islam | 2 | Teori | A |
| IF1107 | Bahasa Indonesia | 2 | Teori | A |
| IF1108 | Pancasila dan Kewarganegaraan | 2 | Teori | A |

#### Semester 2 — Fondasi Pemrograman (20-21 SKS)

| Kode | Mata Kuliah | SKS | Tipe | Template | Status Repo |
|------|-------------|-----|------|----------|-------------|
| INF-101 | Algoritma dan Pemrograman | 2 | Teori | A | ✅ Sudah |
| INF-102 | Praktikum Algoritma dan Pemrograman | 1 | Lab | B | ✅ Sudah |
| IF1203 | Analisis Data Statistik | 2 | Teori+Lab | C | ✅ Sudah |
| IF1204 | Matematika Diskrit | 3 | Teori | A | |
| IF1205 | Kalkulus II | 3 | Teori | A | |
| IF1206 | Bahasa Inggris II | 2 | Teori | A | |
| IF1207 | Etika Profesi dan Keilmuan Islam | 2 | Teori | A | |
| IF1208 | Aljabar Linear | 3 | Teori | A | |

#### Semester 3 — Inti Pemrograman (20-21 SKS)

| Kode | Mata Kuliah | SKS | Tipe | Template |
|------|-------------|-----|------|----------|
| IF2101 | Pemrograman Berorientasi Objek (OOP) | 3 | Teori+Lab | C |
| IF2102 | Struktur Data | 3 | Teori+Lab | C |
| IF2103 | Basis Data | 3 | Teori+Lab | C |
| IF2104 | Sistem Operasi | 3 | Teori+Lab | C |
| IF2105 | Arsitektur dan Organisasi Komputer | 3 | Teori | A |
| IF2106 | Probabilitas dan Statistika Lanjut | 3 | Teori | A |
| IF2107 | Metodologi Penelitian | 2 | Teori | A |

#### Semester 4 — Inti Sistem (20-21 SKS)

| Kode | Mata Kuliah | SKS | Tipe | Template |
|------|-------------|-----|------|----------|
| IF2201 | Desain dan Analisis Algoritma | 3 | Teori+Lab | C |
| IF2202 | Jaringan Komputer | 3 | Teori+Lab | C |
| IF2203 | Pemrograman Web | 3 | Teori+Lab | C |
| IF2204 | Interaksi Manusia dan Komputer | 3 | Teori+Lab | C |
| IF2205 | Rekayasa Perangkat Lunak | 3 | Teori+Lab | C |
| IF2206 | Teori Bahasa dan Automata | 3 | Teori | A |
| IF2207 | Kewirausahaan Digital | 2 | Teori | A |

#### Semester 5 — Lanjutan & Spesialisasi Awal (20-21 SKS)

| Kode | Mata Kuliah | SKS | Tipe | Template | Status Repo |
|------|-------------|-----|------|----------|-------------|
| IF3XXX | Kecerdasan Buatan dan Machine Learning | 4 | Teori+Lab | C | ✅ Sudah |
| IF3102 | Pengembangan Aplikasi Mobile | 3 | Teori+Lab | C | |
| IF3103 | Keamanan Informasi dan Siber | 3 | Teori+Lab | C | |
| IF3104 | Komputasi Awan (Cloud Computing) | 3 | Teori+Lab | C | |
| IF3105 | Manajemen Proyek Perangkat Lunak | 3 | Teori | A | |
| IF3106 | Pilihan I (Elective) | 3 | Varies | A/C | |

#### Semester 6 — Spesialisasi Lanjutan (18-20 SKS)

| Kode | Mata Kuliah | SKS | Tipe | Template |
|------|-------------|-----|------|----------|
| IF3201 | Pemrosesan Bahasa Alami (NLP) | 3 | Teori+Lab | C |
| IF3202 | Data Mining dan Big Data | 3 | Teori+Lab | C |
| IF3203 | Pengembangan Sistem Terdistribusi | 3 | Teori+Lab | C |
| IF3204 | DevOps dan CI/CD | 3 | Teori+Lab | C |
| IF3205 | Pilihan II (Elective) | 3 | Varies | A/C |
| IF3206 | Kerja Praktik / MBKM | 3 | Praktik | — |

#### Semester 7 — Pra-Tugas Akhir (15-18 SKS)

| Kode | Mata Kuliah | SKS | Tipe | Template |
|------|-------------|-----|------|----------|
| IF4101 | Computer Vision dan Image Processing | 3 | Teori+Lab | C |
| IF4102 | Blockchain dan Teknologi Terdesentralisasi | 3 | Teori+Lab | C |
| IF4103 | Internet of Things (IoT) | 3 | Teori+Lab | C |
| IF4104 | Seminar / Kapita Selekta Informatika | 2 | Teori | A |
| IF4105 | Tugas Akhir I (Proposal) | 2 | Riset | — |
| IF4106 | Pilihan III (Elective) | 3 | Varies | A/C |

#### Semester 8 — Tugas Akhir (12-14 SKS)

| Kode | Mata Kuliah | SKS | Tipe | Template |
|------|-------------|-----|------|----------|
| IF4201 | Tugas Akhir II (Skripsi) | 6 | Riset | — |
| IF4202 | Magang Industri / MBKM Lanjutan | 4 | Praktik | — |
| IF4203 | Pilihan IV (Elective) | 3 | Varies | A/C |

---

#### Ringkasan Kurikulum

| Kategori | Jumlah MK | Total SKS |
|----------|-----------|-----------|
| Mata Kuliah Wajib | ~38 | ~120 |
| Mata Kuliah Pilihan (Elective) | 4 | 12 |
| Tugas Akhir + Kerja Praktik | 3 | 13-15 |
| **TOTAL** | **~45** | **~147 SKS** |

#### Kelompok Bidang Keahlian

| Kelompok | Contoh MK | Semester |
|----------|-----------|----------|
| **Fondasi Matematika & Sains** | Kalkulus, Aljabar Linear, Fisika, Statistik, Probabilitas | 1-3 |
| **Fondasi Pemrograman** | Algoritma, OOP, Struktur Data | 1-3 |
| **Sistem Komputer** | Arsitektur, Sistem Operasi, Jaringan | 3-4 |
| **Rekayasa Perangkat Lunak** | RPL, Desain Algoritma, Manajemen Proyek | 4-5 |
| **Pengembangan Aplikasi** | Web, Mobile, Cloud, DevOps | 4-6 |
| **Data & Kecerdasan Buatan** | AI/ML, NLP, Data Mining, Computer Vision | 5-7 |
| **Keamanan & Sistem Terdistribusi** | Keamanan Siber, Blockchain, IoT | 5-7 |
| **Umum & Universitas** | Agama, Bahasa, Pancasila, Etika, Kewirausahaan | 1-4 |

#### Mata Kuliah Pilihan (Elective Pool)

| Kode | Mata Kuliah | SKS | Tipe |
|------|-------------|-----|------|
| IFE01 | Pengembangan Game | 3 | Teori+Lab |
| IFE02 | Augmented/Virtual Reality | 3 | Teori+Lab |
| IFE03 | Robotika dan Embedded Systems | 3 | Teori+Lab |
| IFE04 | Bioinformatika | 3 | Teori+Lab |
| IFE05 | Quantum Computing (Pengantar) | 3 | Teori |
| IFE06 | Desain UI/UX Lanjutan | 3 | Teori+Lab |
| IFE07 | Pemrograman Fungsional | 3 | Teori+Lab |
| IFE08 | Deep Learning Lanjutan | 3 | Teori+Lab |
| IFE09 | Sistem Rekomendasi | 3 | Teori+Lab |
| IFE10 | Teknologi Finansial (FinTech) | 3 | Teori+Lab |
| IFE11 | Green Computing dan Sustainability | 3 | Teori |
| IFE12 | Etika AI dan Regulasi Digital | 3 | Teori |

---

### N. CONTOH: CARA MENGGUNAKAN PROMPT INI

#### Contoh 1: Generate MK "Pemrograman Berorientasi Objek"

1. **Tipe:** Template C (Teori+Lab)
2. **Isi variabel:**
   - `[NAMA_MK]` = Pemrograman Berorientasi Objek
   - `[KODE_MK]` = IF2101
   - `[SKS]` = 3 SKS
   - `[TIPE_MK]` = Teori+Lab
   - `[SEMESTER]` = Ganjil 2026/2027
   - `[BAHASA_PEMROGRAMAN]` = Python 3.x / Java
   - `[SLUG_MK]` = pemrograman-berorientasi-objek
   - `[JUDUL_BUKU]` = Pemrograman Berorientasi Objek: Paradigma Modern dengan Python dan Java
3. **Isi kurikulum 16 minggu** dengan topik OOP: class, object, encapsulation, inheritance, polymorphism, abstract class, interface, design patterns, SOLID, dll.
4. **Isi 7 CPMK** yang relevan dengan OOP
5. **Copy seluruh prompt** (dengan variabel sudah terisi) ke Claude baru
6. **Generate per batch** sesuai urutan di Bagian I

#### Contoh 2: Generate MK "Praktikum Basis Data"

1. **Tipe:** Template B (Lab)
2. **Isi variabel:**
   - `[NAMA_MK]` = Praktikum Basis Data
   - `[KODE_MK]` = IF2103P
   - `[SKS]` = 1 SKS
   - `[TIPE_MK]` = Lab
   - `[BAHASA_PEMROGRAMAN]` = SQL / Python
   - `[PLATFORM]` = MySQL / PostgreSQL + Google Colab
   - `[SLUG_MK]` = praktikum-basis-data
3. **Isi 13 lab** dengan topik: setup DBMS, CREATE TABLE, INSERT/SELECT, JOIN, subquery, normalisasi, indexing, stored procedure, trigger, Python+SQL, ORM, proyek mini
4. **Generate per batch** (skip batch buku ajar)

---

## [AKHIR PROMPT]

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
