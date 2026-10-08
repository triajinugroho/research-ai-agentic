# DASAR KECERDASAN ARTIFISIAL DAN PEMBELAJARAN MESIN

## Buku Ajar

**Tri Aji Nugroho, S.T., M.T.**

**Program Studi Informatika**
**Fakultas Sains dan Teknologi**
**Universitas Al Azhar Indonesia**

**Jakarta, September 2026**

---

## Identitas Buku

| Aspek | Keterangan |
|-------|------------|
| Judul | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin |
| Mata kuliah | `IF52510031` — 3 SKS — Semester 5 |
| Kurikulum | Kurikulum Informatika 2025 — Revisi 2026 |
| Penulis | Tri Aji Nugroho, S.T., M.T. |
| Program studi | Informatika, Universitas Al Azhar Indonesia |
| Tahun | 2026 |
| Bahasa | Indonesia, dengan istilah teknis bilingual |
| Perangkat | Python 3.x · `scikit-learn` · Google Colab |

---

## Capaian yang Ditopang Buku Ini

| Sub-CPMK | Bobot | Bab pendukung |
|----------|-------|---------------|
| `DAIML-Sub-CPMK082-1` — Menganalisis karakteristik permasalahan dan merancang serta mengembangkan model AI/ML | 60% | 1, 2, 6, 7, 8, 9, 10, 12, 13, 14 |
| `DAIML-Sub-CPMK102-1` — Mengolah, menganalisis, dan memvisualisasikan data serta kinerja model | 40% | 3, 4, 5, 11, 14 |

Rumusan lengkap kedua Sub-CPMK ada pada [RPS §E](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md).

---

## Daftar Isi

### Bagian Depan

| | Judul |
|---|-------|
| — | [Mengapa Buku Ini Ditulis](mengapa-buku-ini.md) |

### Bagian I — Memahami Persoalan: *Frame the Problem*

| Bab | Judul | Sub-CPMK | Minggu |
|-----|-------|----------|--------|
| 1 | [Lanskap Kecerdasan Artifisial](bab-01-lanskap-kecerdasan-artifisial.md) | 082-1 | 1 |
| 2 | [Formulasi Masalah dan Daur Hidup Pembelajaran Mesin](bab-02-formulasi-masalah-daur-hidup-ml.md) | 082-1 | 2 |

### Bagian II — Menyiapkan Data: *Data Comes First*

| Bab | Judul | Sub-CPMK | Minggu |
|-----|-------|----------|--------|
| 3 | [Data dan Prapemrosesan](bab-03-data-dan-prapemrosesan.md) | 102-1 | 3 |
| 4 | [Pembagian Data dan Kebocoran Data](bab-04-pembagian-data-dan-kebocoran.md) | 102-1 | 4 |
| 5 | [Rekayasa Fitur](bab-05-rekayasa-fitur.md) | 102-1 | 5 |

### Bagian III — Membangun Model: *Learn from Data*

| Bab | Judul | Sub-CPMK | Minggu |
|-----|-------|----------|--------|
| 6 | [Regresi dan Metriknya](bab-06-regresi-dan-metriknya.md) | 082-1 | 6 |
| 7 | [Klasifikasi dan Metriknya](bab-07-klasifikasi-dan-metriknya.md) | 082-1 | 7 |
| 8 | [Pohon Keputusan dan *Ensemble*](bab-08-pohon-keputusan-dan-ensemble.md) | 082-1 | 9 |
| 9 | [SVM, Naive Bayes, dan Pemilihan Model](bab-09-svm-naive-bayes-pemilihan-model.md) | 082-1 | 10 |
| 10 | [Pembelajaran Tanpa Supervisi](bab-10-pembelajaran-tanpa-supervisi.md) | 082-1 | 11 |

### Bagian IV — Mendiagnosis dan Bertanggung Jawab

| Bab | Judul | Sub-CPMK | Minggu |
|-----|-------|----------|--------|
| 11 | [Reduksi Dimensi dan Visualisasi Kinerja Model](bab-11-reduksi-dimensi-dan-visualisasi.md) | 102-1 | 12 |
| 12 | [Pengantar Jaringan Saraf Tiruan](bab-12-pengantar-jaringan-saraf-tiruan.md) | 082-1 | 13 |
| 13 | [AI Generatif dan AI yang Bertanggung Jawab](bab-13-ai-generatif-dan-ai-bertanggung-jawab.md) | 082-1 | 14 |
| 14 | [Proyek Akhir: Solusi Pembelajaran Mesin *End-to-End*](bab-14-proyek-akhir.md) | Keduanya | 14–15 |

### Bagian Belakang

| | Judul |
|---|-------|
| — | [Lampiran](lampiran.md) — formularium, pohon keputusan pemilihan model, rujukan `scikit-learn`, glosarium |
| — | [Penutup](penutup.md) |

---

## Peta Progresi AI Corner

Setiap bab memuat bagian **AI Corner**. Mata kuliah ini berstatus **tahap U→A→C, mode Core** pada AI Curriculum Infusion Matrix — AI adalah **objek utama pembelajaran**, bukan sekadar alat bantu. Karena itu AI Corner di sini memiliki dua lapis:

1. **AI sebagai yang dipelajari** — bagaimana sistem ini bekerja dan di mana batasnya.
2. **AI sebagai alat kerja** — bagaimana memakainya tanpa menyerahkan penalaran yang justru sedang dinilai.

Level progresinya mengikuti *AI Competency Framework for Students* dari UNESCO — **Understand → Apply → Create** (acuan [REG-9] pada Pedoman OBE §B.2) — dengan pembagian bab menurut [Pedoman OBE §P](../../../00-pedoman-obe/pedoman-obe-konvensi.md#p-kerangka-kompetensi-ai-unesco-januari-2026):

| Bab | Level UNESCO | Dimensi dominan | Fokus AI Corner |
|-----|--------------|-----------------|-----------------|
| 1–4 | **Understand** | *AI techniques and applications*; *Human-centred mindset* | Memahami apa yang benar-benar dilakukan sistem AI dan kapan ia tidak diperlukan; mengapa AI tidak dapat memutuskan penanganan data dan tidak mengenal konteks data Anda |
| 5–11 | **Apply** | *AI techniques and applications*; *Ethics of AI* | Memakai AI untuk kode sambil mempertahankan rekayasa fitur, pemilihan model, dan pemilihan metrik sebagai keputusan sendiri; memverifikasi keluaran AI dan mengenali kekeliruan khas yang diulangnya |
| 12–14 | **Create** | *AI system design*; *Ethics of AI* | Tanggung jawab penuh atas sistem yang dibangun; dokumentasi dan pelaporan yang jujur |

> Judul AI Corner tiap bab mencantumkan levelnya; bila berbeda, **tabel inilah acuannya**. Label **Tingkat Dasar/Menengah/Mahir** pada Latihan Soal adalah jenjang kesukaran soal, **bukan** level AI Corner — level AI Corner hanya mengikuti tabel UNESCO di atas.

---

## Cara Menggunakan Buku Ini

### Untuk Mahasiswa

1. **Baca bab sebelum kelas.** Setiap bab dirancang untuk dibaca dalam 60–75 menit sebagai persiapan.
2. **Jalankan setiap potongan kode**, jangan hanya membacanya. Kode di buku ini diuji pada Google Colab.
3. **Kerjakan Latihan Soal tingkat Dasar** segera setelah membaca.
4. **Kerjakan tingkat Menengah** setelah kuliah dan praktikum.
5. **Kerjakan tingkat Mahir** sebagai persiapan ujian dan bahan proyek.
6. **Jangan melewati AI Corner** — di situlah batas dan tanggung jawab dibahas.
7. **Hitung manual dulu, baru pakai komputer.** UTS dan UAS bersifat *closed book*: alat bantu yang diperkenankan **hanya kalkulator** — tanpa catatan, tanpa perangkat lain, tanpa AI (lihat [Lampiran](lampiran.md#daftar-lampiran)).

### Untuk Dosen Pengampu

- Setiap bab selaras dengan satu modul mingguan pada `03-modules/` dan satu praktikum pada `04-labs/`.
- Latihan Soal adalah **latihan terbuka untuk belajar mandiri** — terbit bersama buku ini dan dapat dibaca siapa saja. Karena itu Latihan Soal **tidak dipakai** sebagai soal kuis atau ujian: soal UTS disusun sebagai varian Latihan UTS menurut [cetak biru butirnya](../05-assessments/latihan-uts-cetak-biru.md) dan [kisi-kisi UTS](../05-assessments/kisi-kisi-uts.md); soal UAS mengacu pada [kisi-kisi UAS](../05-assessments/kisi-kisi-uas.md); soal kuis mengacu pada cakupan kuis K-01–K-04 pada [RTM §D](../02-rtm/rtm-dasar-kecerdasan-artifisial-pembelajaran-mesin.md#d-rincian-kuis-k-01-sd-k-04). Seluruh naskah itu disusun terpisah dan **tidak dipublikasikan**. Untuk persiapan UTS tersedia [Latihan UTS](../05-assessments/latihan-uts.md) — simulasi dengan [pembahasan](../05-assessments/latihan-uts-pembahasan.md); naskah UTS sebenarnya adalah varian darinya dan tidak dipublikasikan.
- AI Corner dapat menjadi bahan diskusi kelas 15 menit.
- Seluruh contoh dan data berkonteks Indonesia, dapat diganti sesuai kebutuhan.

---

## Ketentuan Kode

| Aspek | Ketentuan |
|-------|-----------|
| Bahasa | Python 3.x |
| Lingkungan | Google Colab (seluruh pustaka sudah tersedia) |
| Pustaka utama | `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn` |
| Komentar | Bahasa Indonesia |
| Reproduksibilitas | `random_state=42` pada seluruh contoh |

Kode di buku ini ditulis untuk **dapat dijalankan apa adanya** setelah sel pembuka baku (Lampiran D) dijalankan.

---

## Rujukan Kurikulum

Rumusan CPL, CPMK, Sub-CPMK, indikator, kriteria, dan bobot **diadaptasi dari** [registri Kurikulum Informatika 2025 Revisi 2026](../../../00-kurikulum-if-2025-revisi-2026/README.md) (diterjemahkan): kode, level Bloom, dan bobot sama persis dengan registri; rumusan Sub-CPMK mengikuti registri; sedangkan materi, indikator, dan kriteria yang di registri bercampur istilah Inggris diterjemahkan ke bahasa Indonesia tanpa mengubah maknanya. Bila terdapat perbedaan, **registri yang berlaku**.

---

## Ucapan Terima Kasih

Buku ini disusun untuk mahasiswa Program Studi Informatika Universitas Al Azhar Indonesia. Terima kasih disampaikan kepada Tim Kurikulum Program Studi Informatika UAI atas kerangka OBE yang menjadi dasar seluruh struktur buku ini.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
