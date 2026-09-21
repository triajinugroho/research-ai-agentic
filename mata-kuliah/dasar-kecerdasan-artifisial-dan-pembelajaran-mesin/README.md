# Dasar Kecerdasan Artifisial dan Pembelajaran Mesin

## IF52510031 — 3 SKS — Semester 5 (Ganjil 2026/2027)

**Program Studi Informatika · Universitas Al Azhar Indonesia**
**Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.

---

## Identitas Ringkas

| Aspek | Keterangan |
|-------|------------|
| Kode mata kuliah | `IF52510031` |
| Kelompok | MKP (Mata Kuliah Program Studi) |
| Bobot | 3 SKS |
| Semester | 5 (Ganjil 2026/2027) |
| Status | Wajib |
| Rumpun | R06 — Kecerdasan Artifisial (*Artificial Intelligence*) |
| Bahan Kajian | BK01 (Artificial Intelligence) · BK08 (Mathematical and Statistical Foundations) |
| CPL yang dibebankan | CPL08 · CPL10 |
| CPMK | CPMK082 · CPMK102 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` (60%) · `DAIML-Sub-CPMK102-1` (40%) |
| Posisi AI Infusion | **Tahap U→A→C · Mode Core · Pilar AI Core** |
| Rujukan kurikulum | [Kurikulum Informatika 2025 Revisi 2026](../00-kurikulum-if-2025-revisi-2026/README.md) |

---

## Kedudukan dalam Kurikulum

Mata kuliah ini adalah **fondasi wajib AI bagi seluruh mahasiswa Informatika UAI**, bukan mata kuliah peminatan. Pada AI Curriculum Infusion Matrix ia berstatus **Core** — artinya AI merupakan objek utama pembelajaran, bukan sekadar konteks contoh.

Posisinya pada jalur **AI Core & Advanced**:

```
   Fondasi                     AI Core            AI Advanced
┌──────────────┐        ┌─────────────────┐   ┌──────────────────┐
│ Probabilitas │        │                 │   │ Jaringan Syaraf  │
│ & Statistik  │───────►│  DASAR AI DAN   │──►│ Tiruan & Deep    │
│ (sem 1)      │        │  PEMBELAJARAN   │   │ Learning (sem 5) │
│              │        │  MESIN          │   ├──────────────────┤
│ Struktur     │───────►│  (sem 5)        │──►│ Sains Data       │
│ Data (sem 3) │        │  ◄── ANDA DI    │   ├──────────────────┤
│              │        │      SINI       │──►│ Pengolahan       │
│ Basis Data   │───────►│                 │   │ Bahasa Alami     │
│ (sem 4)      │        │                 │   ├──────────────────┤
└──────────────┘        └─────────────────┘   │ Pengolahan Citra │
                                 │            │ Web Semantik     │
                                 ▼            └──────────────────┘
                        ┌─────────────────┐            │
                        │  Tugas Akhir    │◄───────────┘
                        └─────────────────┘
```

> **Prinsip kurikulum yang dipegang mata kuliah ini:**
> *"Mahasiswa tidak boleh menjadi sekadar pengguna model/API."*
> — Jalur Fondasi AI, AI Curriculum Infusion Matrix

---

## Struktur Folder

| Folder | Isi | Jumlah |
|--------|-----|--------|
| [`00-strategic-analysis/`](00-strategic-analysis/) | Analisis strategis: SWOT, Porter, tren AI 2026 | 1 |
| [`01-rps/`](01-rps/) | Rencana Pembelajaran Semester | 1 |
| [`02-rtm/`](02-rtm/) | Rencana Tugas Mahasiswa | 1 |
| [`03-modules/`](03-modules/) | Modul kuliah mingguan (Minggu 1–16) | 16 |
| [`04-labs/`](04-labs/) | Praktikum Python (Lab 1–7, 9–14) | 13 |
| [`05-assessments/`](05-assessments/) | Kerangka asesmen, kisi-kisi UTS/UAS, rubrik, panduan proyek | 5 |
| [`06-buku-ajar/`](06-buku-ajar/) | Buku ajar: 14 bab + halaman depan + lampiran + penutup | 18 |
| [`datasets/`](datasets/) | Panduan dataset berkonteks Indonesia | 1 |

---

## Sub-CPMK

### `DAIML-Sub-CPMK082-1` — Bobot 60%

> Mampu menganalisis (C4) karakteristik permasalahan dan merancang serta mengembangkan (C6/P4–P5) model AI/ML yang sesuai untuk klasifikasi, regresi, *clustering*, atau *intelligent systems* lainnya.

**Bloom:** C4–C6 / P4–P5 · **CPL08 → CPMK082**

### `DAIML-Sub-CPMK102-1` — Bobot 40%

> Mampu mengolah (C3/P2), menganalisis (C4), dan memvisualisasikan (C3/P3) data serta menganalisis (C4) kinerja model menggunakan metrik yang tepat untuk menghasilkan kesimpulan yang dapat dipertanggungjawabkan.

**Bloom:** C3–C4 / P2–P3 · **CPL10 → CPMK102**

---

## Bobot Penilaian

Bobot melekat pada Sub-CPMK, sesuai ketentuan Kurikulum 2025 Revisi 2026:

| Teknik | Sub-CPMK082-1 | Sub-CPMK102-1 | **Total** |
|--------|---------------|---------------|-----------|
| Partisipasi | 0% | 0% | **0%** |
| Kuis | 0% | 5% | **5%** |
| Observasi (Praktek/Tugas) | 15% | 10% | **25%** |
| Unjuk Kerja (Presentasi/Proyek) | 30% | 5% | **35%** |
| Tes Tulis (UTS) | 0% | 20% | **20%** |
| Tes Tulis (UAS) | 15% | 0% | **15%** |
| **Jumlah** | **60%** | **40%** | **100%** |

> **Dua hal yang perlu diperhatikan sejak awal:**
>
> 1. **Partisipasi berbobot 0%.** Nilai sepenuhnya ditentukan oleh karya — bukan kehadiran. Kehadiran tetap wajib memenuhi ketentuan universitas, tetapi tidak menambah nilai.
> 2. **Unjuk Kerja 35% adalah komponen terbesar.** Proyek bukan pelengkap di akhir semester, melainkan tulang punggung mata kuliah ini.

Rincian lengkap ada pada [kerangka asesmen](05-assessments/assessment-framework.md).

---

## Peta Perkuliahan

| Mg | Topik | Sub-CPMK | Bab | Lab |
|----|-------|----------|-----|-----|
| 1 | Lanskap Kecerdasan Artifisial | 082-1 | [1](06-buku-ajar/bab-01-lanskap-kecerdasan-artifisial.md) | [1](04-labs/lab-01-setup-ekosistem-ml.md) |
| 2 | Formulasi Masalah dan Daur Hidup ML | 082-1 | [2](06-buku-ajar/bab-02-formulasi-masalah-daur-hidup-ml.md) | [2](04-labs/lab-02-formulasi-masalah-baseline.md) |
| 3 | Data dan Prapemrosesan | 102-1 | [3](06-buku-ajar/bab-03-data-dan-prapemrosesan.md) | [3](04-labs/lab-03-pipeline-prapemrosesan.md) |
| 4 | Pembagian Data dan Kebocoran Data | 102-1 | [4](06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md) | [4](04-labs/lab-04-validasi-silang-deteksi-kebocoran.md) |
| 5 | Rekayasa Fitur | 102-1 | [5](06-buku-ajar/bab-05-rekayasa-fitur.md) | [5](04-labs/lab-05-rekayasa-fitur.md) |
| 6 | Regresi dan Metriknya | 082-1 | [6](06-buku-ajar/bab-06-regresi-dan-metriknya.md) | [6](04-labs/lab-06-model-regresi-dan-metrik.md) |
| 7 | Klasifikasi dan Metriknya | 082-1 | [7](06-buku-ajar/bab-07-klasifikasi-dan-metriknya.md) | [7](04-labs/lab-07-klasifikasi-dan-metrik.md) |
| 8 | **UTS** | 102-1 | — | — |
| 9 | Pohon Keputusan dan *Ensemble* | 082-1 | [8](06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md) | [9](04-labs/lab-09-pohon-keputusan-dan-ensemble.md) |
| 10 | SVM, Naive Bayes, dan Pemilihan Model | 082-1 | [9](06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md) | [10](04-labs/lab-10-svm-naive-bayes-penyetelan.md) |
| 11 | Pembelajaran Tanpa Supervisi | 082-1 | [10](06-buku-ajar/bab-10-pembelajaran-tanpa-supervisi.md) | [11](04-labs/lab-11-clustering-dan-metriknya.md) |
| 12 | Reduksi Dimensi dan Visualisasi Model | 102-1 | [11](06-buku-ajar/bab-11-reduksi-dimensi-dan-visualisasi.md) | [12](04-labs/lab-12-pca-dan-visualisasi-model.md) |
| 13 | Pengantar Jaringan Saraf Tiruan | 082-1 | [12](06-buku-ajar/bab-12-pengantar-jaringan-saraf-tiruan.md) | [13](04-labs/lab-13-jaringan-saraf-tiruan.md) |
| 14 | AI Generatif dan AI yang Bertanggung Jawab | 082-1 | [13](06-buku-ajar/bab-13-ai-generatif-dan-ai-bertanggung-jawab.md) | [14](04-labs/lab-14-audit-bias-dan-model-card.md) |
| 15 | Presentasi Proyek | Keduanya | [14](06-buku-ajar/bab-14-proyek-akhir.md) | — |
| 16 | **UAS** | 082-1 | — | — |

---

## Perangkat

| Perangkat | Keperluan |
|-----------|-----------|
| Python 3.x | Bahasa utama |
| Google Colab | Lingkungan kerja seluruh praktikum |
| NumPy, pandas | Manipulasi data |
| Matplotlib, seaborn | Visualisasi |
| **scikit-learn** | Pustaka ML utama sepanjang semester |
| TensorFlow/Keras | Hanya pada Minggu 13 (pengantar JST) |
| Git/GitHub | Pengumpulan proyek dan penelusuran versi |

---

## Catatan tentang Folder `kecerdasan-buatan-machine-learning/`

Repositori ini memuat folder terpisah [`kecerdasan-buatan-machine-learning/`](../kecerdasan-buatan-machine-learning/) berisi materi mata kuliah **Kecerdasan Buatan dan Machine Learning (IF3XXX, 4 SKS)** yang disusun pada kerangka kurikulum **sebelumnya**.

Kedua folder **sengaja dipertahankan berdampingan**:

| Aspek | `kecerdasan-buatan-machine-learning/` | Folder ini |
|-------|---------------------------------------|------------|
| Kode | IF3XXX (sementara) | **IF52510031** |
| Bobot | 4 SKS | **3 SKS** |
| Kurikulum | Kerangka sebelumnya | **2025 Revisi 2026** |
| Arsitektur CPMK | 7 CPMK lokal mata kuliah | **2 CPMK prodi** (CPMK082, CPMK102) |
| Sub-CPMK | Per minggu | **2 Sub-CPMK** dengan bobot melekat |
| Teknik penilaian | Tugas/Kuis/UTS/Proyek/UAS/Partisipasi | **6 teknik baku kurikulum** |
| Status | Rujukan historis | **Acuan pelaksanaan** |

Materi pada folder lama tetap berguna sebagai bank konten — terutama bab-bab Deep Learning, NLP, dan Computer Vision yang pada kurikulum baru **dipisah menjadi mata kuliah tersendiri** (Jaringan Syaraf Tiruan dan Pembelajaran Mendalam, Pengolahan Bahasa Alami, Pengolahan Citra).

---

## Rujukan Kurikulum

Seluruh rumusan CPL, CPMK, Sub-CPMK, indikator, kriteria, dan bobot pada folder ini **diambil verbatim** dari registri kurikulum, bukan ditulis ulang:

| Dokumen | Isi yang dirujuk |
|---------|------------------|
| [`03-cpl-prodi.md`](../00-kurikulum-if-2025-revisi-2026/03-cpl-prodi.md) | Rumusan CPL08 dan CPL10 |
| [`13-cpmk-master.md`](../00-kurikulum-if-2025-revisi-2026/13-cpmk-master.md) | Rumusan CPMK082 dan CPMK102 |
| [`15d-subcpmk-tingkat-3-semester-5-6.md`](../00-kurikulum-if-2025-revisi-2026/15d-subcpmk-tingkat-3-semester-5-6.md) | Sub-CPMK, indikator, kriteria, bobot |
| [`14a-ai-curriculum-infusion-matrix.md`](../00-kurikulum-if-2025-revisi-2026/14a-ai-curriculum-infusion-matrix.md) | Tahap U→A→C, mode Core, pilar AI Core |
| [`06-bahan-kajian.md`](../00-kurikulum-if-2025-revisi-2026/06-bahan-kajian.md) | BK01, BK08 |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
