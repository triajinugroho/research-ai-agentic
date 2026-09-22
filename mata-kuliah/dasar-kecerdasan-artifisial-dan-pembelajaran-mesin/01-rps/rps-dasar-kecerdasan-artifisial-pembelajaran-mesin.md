# RENCANA PEMBELAJARAN SEMESTER (RPS)

## UNIVERSITAS AL AZHAR INDONESIA
### FAKULTAS SAINS DAN TEKNOLOGI — PROGRAM STUDI INFORMATIKA

**Kurikulum Informatika 2025 — Revisi 2026**

---

## A. IDENTITAS MATA KULIAH

| Aspek | Keterangan |
|-------|------------|
| Nama Mata Kuliah | **Dasar Kecerdasan Artifisial dan Pembelajaran Mesin** |
| Kode Mata Kuliah | `IF52510031` |
| Kelompok Mata Kuliah | MKP — Mata Kuliah Program Studi |
| Bobot | **3 SKS** |
| Semester | **5** (Ganjil 2026/2027) |
| Status | **Wajib** |
| Rumpun Keilmuan | R06 — Kecerdasan Artifisial (*Artificial Intelligence*) |
| Bahan Kajian | **BK01** — *Artificial Intelligence* · **BK08** — *Mathematical and Statistical Foundations* |
| Prasyarat | Probabilitas dan Statistik; Struktur Data dan Algoritma; Dasar-dasar Pemrograman |
| Dosen Pengampu | **Tri Aji Nugroho, S.T., M.T.** |
| Posisi AI Infusion | Tahap **U→A→C** · Mode **Core** · Pilar **AI Core** |
| Beban belajar | 3 × 170 menit/minggu = 510 menit/minggu (tatap muka 150' + terstruktur 180' + mandiri 180') |

---

## B. DESKRIPSI MATA KULIAH

Mata kuliah ini membekali mahasiswa dengan kemampuan **merumuskan masalah, membangun, dan mengevaluasi model kecerdasan artifisial dan pembelajaran mesin** secara utuh — dari data mentah sampai kesimpulan yang dapat dipertanggungjawabkan.

Cakupannya meliputi lanskap dan batas kemampuan AI; formulasi masalah dan daur hidup ML; prapemrosesan, pembagian data, dan rekayasa fitur; pembelajaran terbimbing untuk regresi dan klasifikasi beserta metriknya; pembelajaran tanpa supervisi; reduksi dimensi dan visualisasi kinerja model; pengantar jaringan saraf tiruan; serta AI generatif dan prinsip AI yang bertanggung jawab.

Pembelajaran berbasis praktik dengan Python dan `scikit-learn` di Google Colab, dengan seluruh kasus memakai **konteks dan data Indonesia**. Mata kuliah berpuncak pada proyek kelompok yang menghasilkan model, dokumentasi (*model card*), dan analisis keterbatasan.

### Yang Tidak Termasuk Cakupan

Agar keluasan alur ML klasik tercakup tuntas dalam 3 SKS, materi berikut **sengaja tidak** dibahas mendalam dan diserahkan kepada mata kuliah yang dirancang untuknya:

| Materi | Mata kuliah yang membahasnya |
|--------|------------------------------|
| Arsitektur *deep learning* (CNN, RNN, Transformer) | Jaringan Syaraf Tiruan dan Pembelajaran Mendalam (IF52510032) |
| Pemrosesan teks dan bahasa | Pengolahan Bahasa Alami (IF52510024) |
| Pemrosesan citra dan visi komputer | Pengolahan Citra (IF52510016) |
| *Pipeline* data skala besar dan MLOps | Sains Data |
| Representasi pengetahuan dan penalaran simbolik lanjut | Web Semantik (IF52510003) |

---

## C. CAPAIAN PEMBELAJARAN LULUSAN (CPL) YANG DIBEBANKAN

Rumusan CPL diambil dari [registri kurikulum terbaru](../../00-kurikulum-if-2025-revisi-2026/03-cpl-prodi.md). Rumusan tidak ditulis ulang di dokumen turunan.

| Kode | Ranah | Rumusan |
|------|-------|---------|
| **CPL08** | Keterampilan Khusus (Wajib) | Mampu merancang dan mengembangkan algoritma untuk berbagai keperluan seperti *Intelligent Systems*, *Information Management*, *Algorithms and Complexity*, *Data Science*, *Human Computer Interaction*, *Graphics & Visual Computing*, *Network Security*, and *Mobile Computing*. |
| **CPL10** | Keterampilan Khusus (Wajib) | Kemampuan merekayasa, membuat pemodelan dan visualisasi data yang tepat untuk kebutuhan organisasi dengan memperhatikan aspek keamanan data. |

---

## D. CAPAIAN PEMBELAJARAN MATA KULIAH (CPMK)

Pada Kurikulum 2025 Revisi 2026, **CPMK bersifat prodi-level** dan dipakai bersama oleh beberapa mata kuliah. Mata kuliah ini membebani dua CPMK.

| Kode | CPL | Rumusan | Bloom | Dipakai oleh |
|------|-----|---------|-------|--------------|
| **CPMK082** | CPL08 | Mampu merancang (C6/P4) dan mengembangkan (C6/P5) algoritma serta metode untuk *Artificial Intelligence*, *Machine Learning*, *Data Science*, *Information Management*, dan *Intelligent Systems*. | C6/P4–P5 | 5 mata kuliah |
| **CPMK102** | CPL10 | Mampu mengolah (C3/P2), menganalisis (C4), dan memvisualisasikan (C3/P3) data menggunakan metode statistik, komputasi, dan kecerdasan artifisial untuk menghasilkan informasi yang mendukung pengambilan keputusan organisasi. | C3–C4, P2–P3 | 7 mata kuliah |

---

## E. SUB-CPMK

Sub-CPMK adalah **pembeda mata kuliah** — tingkat inilah yang menerjemahkan CPMK prodi menjadi capaian khas mata kuliah ini. Rumusan, indikator, kriteria, dan bobot diambil verbatim dari [pemetaan kurikulum](../../00-kurikulum-if-2025-revisi-2026/15d-subcpmk-tingkat-3-semester-5-6.md).

### `DAIML-Sub-CPMK082-1` — Bobot **60%**

| Aspek | Isi |
|-------|-----|
| **Rumusan** | Mampu menganalisis (C4) karakteristik permasalahan dan merancang serta mengembangkan (C6/P4–P5) model AI/ML yang sesuai untuk klasifikasi, regresi, *clustering*, atau *intelligent systems* lainnya. |
| **Bloom** | C4–C6 / P4–P5 |
| **Materi** | *AI fundamentals*; *problem formulation*; *supervised/unsupervised learning*; *model selection*; *training*; *generalization*; pengantar *neural/generative AI*. |
| **Indikator** | 1. Memformulasikan *task* dan memilih model AI/ML; 2. Membangun *pipeline* serta melatih model yang dapat direproduksi. |
| **Kriteria** | Ketepatan pasangan masalah–model; kebenaran proses pelatihan; reproduksibilitas eksperimen. |

### `DAIML-Sub-CPMK102-1` — Bobot **40%**

| Aspek | Isi |
|-------|-----|
| **Rumusan** | Mampu mengolah (C3/P2), menganalisis (C4), dan memvisualisasikan (C3/P3) data serta menganalisis (C4) kinerja model menggunakan metrik yang tepat untuk menghasilkan kesimpulan yang dapat dipertanggungjawabkan. |
| **Bloom** | C3–C4 / P2–P3 |
| **Materi** | *Preprocessing*; *train/validation/test*; *feature engineering*; metrik klasifikasi/regresi; metrik *clustering*; visualisasi; pengantar *bias/fairness*. |
| **Indikator** | 1. Menyiapkan dan membagi data tanpa kebocoran; 2. Menganalisis metrik serta memvisualisasikan hasil model secara tepat. |
| **Kriteria** | Kebenaran prapemrosesan dan pembagian data; kesesuaian metrik; validitas interpretasi. |

---

## F. INDIKATOR CAPAIAN MINGGUAN

Kurikulum menetapkan dua Sub-CPMK untuk 16 minggu. Agar dapat dioperasikan per pertemuan, RPS ini menambahkan lapisan **Indikator Capaian Mingguan (ICM)** yang seluruhnya menelusur ke salah satu Sub-CPMK. Lapisan ini adalah **perangkat pelaksanaan**, bukan penambahan capaian baru.

| ICM | Menelusur ke | Rumusan |
|-----|--------------|---------|
| ICM-01 | 082-1 | Membedakan masalah yang sesuai dan tidak sesuai diselesaikan dengan ML |
| ICM-02 | 082-1 | Memformulasikan masalah nyata menjadi *task* ML yang tepat |
| ICM-03 | 102-1 | Memeriksa kualitas data dan menerapkan prapemrosesan yang sesuai |
| ICM-04 | 102-1 | Membagi data tanpa kebocoran dan menjalankan validasi silang |
| ICM-05 | 102-1 | Merekayasa fitur yang meningkatkan kinerja tanpa menimbulkan kebocoran |
| ICM-06 | 082-1 | Membangun dan melatih model regresi serta menafsirkan metriknya |
| ICM-07 | 082-1 | Membangun dan melatih model klasifikasi serta menafsirkan metriknya |
| ICM-08 | 082-1 | Menerapkan pohon keputusan dan metode *ensemble* |
| ICM-09 | 082-1 | Memilih model dan menyetel hiperparameter secara sistematis |
| ICM-10 | 082-1 | Menerapkan *clustering* dan menilai hasilnya dengan metrik yang sesuai |
| ICM-11 | 102-1 | Menerapkan reduksi dimensi dan memvisualisasikan kinerja model |
| ICM-12 | 082-1 | Menjelaskan prinsip kerja jaringan saraf tiruan dan melatih MLP sederhana |
| ICM-13 | 082-1 | Menjelaskan prinsip AI generatif serta menganalisis *bias* dan dampak model |
| ICM-14 | Keduanya | Menyajikan dan mempertanggungjawabkan hasil proyek secara lisan |

---

## G. TABEL RENCANA PEMBELAJARAN SEMESTER

### Minggu 1 — Lanskap Kecerdasan Artifisial

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK / ICM | `DAIML-Sub-CPMK082-1` / ICM-01 |
| Bahan kajian | Definisi AI; sejarah dan tiga gelombang; AI vs ML vs DL; paradigma pembelajaran; batas kemampuan AI |
| Bentuk pembelajaran | Kuliah interaktif · Diskusi kasus · Praktik terbimbing |
| Pengalaman belajar | Mengklasifikasikan 10 kasus nyata: mana yang ML, mana yang cukup aturan biasa |
| Materi | [Modul Minggu 1](../03-modules/week-01-lanskap-kecerdasan-artifisial.md) · [Bab 1](../06-buku-ajar/bab-01-lanskap-kecerdasan-artifisial.md) · [Lab 1](../04-labs/lab-01-setup-ekosistem-ml.md) |
| Penilaian | Observasi (Lab 1) |

### Minggu 2 — Formulasi Masalah dan Daur Hidup ML

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK / ICM | `DAIML-Sub-CPMK082-1` / ICM-02 |
| Bahan kajian | Dari masalah bisnis ke *task* ML; jenis *task*; *baseline*; daur hidup ML; **kapan tidak memakai ML** |
| Bentuk pembelajaran | Kuliah · Studi kasus · Latihan formulasi |
| Pengalaman belajar | Mengubah tiga masalah nyata Indonesia menjadi rumusan *task* ML lengkap dengan metrik keberhasilan |
| Materi | [Modul Minggu 2](../03-modules/week-02-formulasi-masalah-daur-hidup-ml.md) · [Bab 2](../06-buku-ajar/bab-02-formulasi-masalah-daur-hidup-ml.md) · [Lab 2](../04-labs/lab-02-formulasi-masalah-baseline.md) |
| Penilaian | Observasi (Lab 2) |

### Minggu 3 — Data dan Prapemrosesan

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK / ICM | `DAIML-Sub-CPMK102-1` / ICM-03 |
| Bahan kajian | Kualitas data; nilai hilang; pencilan; penyandian kategorik; penskalaan; `Pipeline` dan `ColumnTransformer` |
| Bentuk pembelajaran | Kuliah · Demonstrasi · Praktikum |
| Pengalaman belajar | Membangun *pipeline* prapemrosesan utuh atas dataset BPS yang belum bersih |
| Materi | [Modul Minggu 3](../03-modules/week-03-data-dan-prapemrosesan.md) · [Bab 3](../06-buku-ajar/bab-03-data-dan-prapemrosesan.md) · [Lab 3](../04-labs/lab-03-pipeline-prapemrosesan.md) |
| Penilaian | Observasi (Lab 3) |

### Minggu 4 — Pembagian Data dan Kebocoran Data

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK / ICM | `DAIML-Sub-CPMK102-1` / ICM-04 |
| Bahan kajian | *Train/validation/test*; validasi silang; stratifikasi; pembagian temporal dan berkelompok; **enam jenis kebocoran data** |
| Bentuk pembelajaran | Kuliah · Demonstrasi kegagalan · Praktikum |
| Pengalaman belajar | Menemukan dan memperbaiki kebocoran pada notebook yang sengaja dibuat salah |
| Materi | [Modul Minggu 4](../03-modules/week-04-pembagian-data-dan-kebocoran.md) · [Bab 4](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md) · [Lab 4](../04-labs/lab-04-validasi-silang-deteksi-kebocoran.md) |
| Penilaian | Observasi (Lab 4) · **Kuis 1** |

### Minggu 5 — Rekayasa Fitur

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK / ICM | `DAIML-Sub-CPMK102-1` / ICM-05 |
| Bahan kajian | Pembuatan fitur; transformasi; penanganan kardinalitas tinggi; fitur waktu dan lokasi; pemilihan fitur; *curse of dimensionality* |
| Bentuk pembelajaran | Kuliah · Praktikum · Kerja kelompok proyek |
| Pengalaman belajar | Meningkatkan kinerja *baseline* semata-mata melalui rekayasa fitur, tanpa mengganti model |
| Materi | [Modul Minggu 5](../03-modules/week-05-rekayasa-fitur.md) · [Bab 5](../06-buku-ajar/bab-05-rekayasa-fitur.md) · [Lab 5](../04-labs/lab-05-rekayasa-fitur.md) |
| Penilaian | Observasi (Lab 5) · **Proposal proyek (P-00)** |

### Minggu 6 — Regresi dan Metriknya

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK / ICM | `DAIML-Sub-CPMK082-1` / ICM-06 |
| Bahan kajian | Regresi linear dan polinomial; regularisasi Ridge/Lasso; MAE, RMSE, R², MAPE; tukar-tambah bias–varians |
| Bentuk pembelajaran | Kuliah · Turunan manual · Praktikum |
| Pengalaman belajar | Membandingkan tiga model regresi pada data harga properti Jabodetabek dengan metrik yang tepat |
| Materi | [Modul Minggu 6](../03-modules/week-06-regresi-dan-metriknya.md) · [Bab 6](../06-buku-ajar/bab-06-regresi-dan-metriknya.md) · [Lab 6](../04-labs/lab-06-model-regresi-dan-metrik.md) |
| Penilaian | Observasi (Lab 6) |

### Minggu 7 — Klasifikasi dan Metriknya

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK / ICM | `DAIML-Sub-CPMK082-1` / ICM-07 |
| Bahan kajian | Regresi logistik; k-NN; matriks konfusi; *precision*, *recall*, F1; ROC-AUC dan PR-AUC; ambang keputusan; data tak seimbang |
| Bentuk pembelajaran | Kuliah · Perhitungan manual · Praktikum |
| Pengalaman belajar | Menunjukkan mengapa akurasi 97% dapat berarti model yang tidak berguna |
| Materi | [Modul Minggu 7](../03-modules/week-07-klasifikasi-dan-metriknya.md) · [Bab 7](../06-buku-ajar/bab-07-klasifikasi-dan-metriknya.md) · [Lab 7](../04-labs/lab-07-klasifikasi-dan-metrik.md) |
| Penilaian | Observasi (Lab 7) · **Kuis 2** · **Milestone proyek 1 (P-01)** |

### Minggu 8 — Ujian Tengah Semester

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK | `DAIML-Sub-CPMK102-1` — **bobot 20%** |
| Cakupan | Minggu 1–7, dengan penekanan pada data, kebocoran, rekayasa fitur, dan metrik |
| Bentuk | Tes tulis, *closed book*, 120 menit, **tanpa alat bantu AI** |
| Materi | [Modul Minggu 8](../03-modules/week-08-uts-review-dan-ujian.md) · [Kisi-kisi UTS](../05-assessments/kisi-kisi-uts.md) |
| Penilaian | **Tes Tulis UTS (20%)** |

### Minggu 9 — Pohon Keputusan dan *Ensemble*

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK / ICM | `DAIML-Sub-CPMK082-1` / ICM-08 |
| Bahan kajian | Pohon keputusan; *entropy* dan *Gini*; *pruning*; *bagging*; *Random Forest*; *gradient boosting*; kepentingan fitur |
| Bentuk pembelajaran | Kuliah · Perhitungan manual *entropy* · Praktikum |
| Pengalaman belajar | Membangun pohon keputusan secara manual, lalu membandingkannya dengan `scikit-learn` |
| Materi | [Modul Minggu 9](../03-modules/week-09-pohon-keputusan-dan-ensemble.md) · [Bab 8](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md) · [Lab 9](../04-labs/lab-09-pohon-keputusan-dan-ensemble.md) |
| Penilaian | Observasi (Lab 9) |

### Minggu 10 — SVM, Naive Bayes, dan Pemilihan Model

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK / ICM | `DAIML-Sub-CPMK082-1` / ICM-09 |
| Bahan kajian | SVM dan *kernel*; Naive Bayes; penyetelan hiperparameter (*grid*/*random search*); validasi silang bersarang; perbandingan model |
| Bentuk pembelajaran | Kuliah · Praktikum · Diskusi hasil |
| Pengalaman belajar | Menjalankan perbandingan lima model secara adil pada satu masalah |
| Materi | [Modul Minggu 10](../03-modules/week-10-svm-naive-bayes-pemilihan-model.md) · [Bab 9](../06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md) · [Lab 10](../04-labs/lab-10-svm-naive-bayes-penyetelan.md) |
| Penilaian | Observasi (Lab 10) · **Kuis 3** |

### Minggu 11 — Pembelajaran Tanpa Supervisi

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK / ICM | `DAIML-Sub-CPMK082-1` / ICM-10 |
| Bahan kajian | K-Means; *hierarchical clustering*; DBSCAN; metrik *silhouette*, Davies-Bouldin, Calinski-Harabasz; penentuan jumlah klaster; deteksi anomali |
| Bentuk pembelajaran | Kuliah · Praktikum · Interpretasi kelompok |
| Pengalaman belajar | Segmentasi wilayah Indonesia berdasarkan indikator sosial-ekonomi BPS, lengkap dengan penafsiran tiap klaster |
| Materi | [Modul Minggu 11](../03-modules/week-11-pembelajaran-tanpa-supervisi.md) · [Bab 10](../06-buku-ajar/bab-10-pembelajaran-tanpa-supervisi.md) · [Lab 11](../04-labs/lab-11-clustering-dan-metriknya.md) |
| Penilaian | Observasi (Lab 11) · **Milestone proyek 2 (P-02)** |

### Minggu 12 — Reduksi Dimensi dan Visualisasi Model

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK / ICM | `DAIML-Sub-CPMK102-1` / ICM-11 |
| Bahan kajian | PCA; *explained variance*; t-SNE dan UMAP sebagai alat visual; kurva pembelajaran; kurva validasi; visualisasi matriks konfusi dan ROC |
| Bentuk pembelajaran | Kuliah · Praktikum visualisasi |
| Pengalaman belajar | Mendiagnosis *overfitting* dan *underfitting* semata-mata dari kurva pembelajaran |
| Materi | [Modul Minggu 12](../03-modules/week-12-reduksi-dimensi-dan-visualisasi.md) · [Bab 11](../06-buku-ajar/bab-11-reduksi-dimensi-dan-visualisasi.md) · [Lab 12](../04-labs/lab-12-pca-dan-visualisasi-model.md) |
| Penilaian | Observasi (Lab 12) |

### Minggu 13 — Pengantar Jaringan Saraf Tiruan

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK / ICM | `DAIML-Sub-CPMK082-1` / ICM-12 |
| Bahan kajian | Perseptron; MLP; fungsi aktivasi; *loss*; *gradient descent*; gagasan *backpropagation*; kapan JST tidak diperlukan |
| Bentuk pembelajaran | Kuliah · Perhitungan manual satu langkah maju-mundur · Praktikum |
| Pengalaman belajar | Melatih MLP dan membandingkannya dengan *Random Forest* pada data tabular yang sama |
| Materi | [Modul Minggu 13](../03-modules/week-13-pengantar-jaringan-saraf-tiruan.md) · [Bab 12](../06-buku-ajar/bab-12-pengantar-jaringan-saraf-tiruan.md) · [Lab 13](../04-labs/lab-13-jaringan-saraf-tiruan.md) |
| Penilaian | Observasi (Lab 13) · **Kuis 4** |

### Minggu 14 — AI Generatif dan AI yang Bertanggung Jawab

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK / ICM | `DAIML-Sub-CPMK082-1` / ICM-13 |
| Bahan kajian | Gagasan model generatif dan LLM; *bias* dalam data dan model; ukuran *fairness*; *explainability*; *model card*; dampak sosial dan tanggung jawab |
| Bentuk pembelajaran | Kuliah · Studi kasus · Audit model |
| Pengalaman belajar | Mengaudit model buatan sendiri untuk *bias* antarkelompok, lalu menyusun *model card* |
| Materi | [Modul Minggu 14](../03-modules/week-14-ai-generatif-dan-ai-bertanggung-jawab.md) · [Bab 13](../06-buku-ajar/bab-13-ai-generatif-dan-ai-bertanggung-jawab.md) · [Lab 14](../04-labs/lab-14-audit-bias-dan-model-card.md) |
| Penilaian | Observasi (Lab 14) · **Laporan proyek (P-03)** |

### Minggu 15 — Presentasi Proyek

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK / ICM | Keduanya / ICM-14 |
| Bahan kajian | Penyajian hasil; pertanggungjawaban keputusan teknis; tanya jawab |
| Bentuk pembelajaran | Presentasi 20 menit per kelompok + tanya jawab |
| Pengalaman belajar | Mempertahankan setiap keputusan teknis di hadapan penguji dan sejawat |
| Materi | [Modul Minggu 15](../03-modules/week-15-presentasi-proyek.md) · [Bab 14](../06-buku-ajar/bab-14-proyek-akhir.md) |
| Penilaian | **Unjuk Kerja — presentasi (P-04)** |

### Minggu 16 — Ujian Akhir Semester

| Aspek | Keterangan |
|-------|------------|
| Sub-CPMK | `DAIML-Sub-CPMK082-1` — **bobot 15%** |
| Cakupan | Seluruh materi, dengan penekanan pada Minggu 9–14 |
| Bentuk | Tes tulis, *closed book*, 120 menit, **tanpa alat bantu AI** |
| Materi | [Modul Minggu 16](../03-modules/week-16-uas-review-dan-ujian.md) · [Kisi-kisi UAS](../05-assessments/kisi-kisi-uas.md) |
| Penilaian | **Tes Tulis UAS (15%)** |

---

## H. PETA EVALUASI (*ASSESSMENT MAP*)

### H.1 Bobot per Teknik dan Sub-CPMK

| Teknik Penilaian | `Sub-CPMK082-1` | `Sub-CPMK102-1` | **Total** |
|------------------|-----------------|-----------------|-----------|
| Partisipasi | 0% | 0% | **0%** |
| Kuis | 0% | 5% | **5%** |
| Observasi (Praktek/Tugas) | 15% | 10% | **25%** |
| Unjuk Kerja (Presentasi/Proyek) | 30% | 5% | **35%** |
| Tes Tulis (UTS) | 0% | 20% | **20%** |
| Tes Tulis (UAS) | 15% | 0% | **15%** |
| **Jumlah** | **60%** | **40%** | **100%** |

### H.2 Penjabaran Komponen

| Komponen | Kode | Minggu | Bobot | Sub-CPMK | Teknik |
|----------|------|--------|-------|----------|--------|
| Lab 1–7, 9–14 (13 lab) | T-01…T-14 | 1–14 | **25%** | 082-1 (15%) · 102-1 (10%) | Observasi |
| Kuis 1 — data dan kebocoran | K-01 | 4 | 1,25% | 102-1 | Kuis |
| Kuis 2 — metrik klasifikasi | K-02 | 7 | 1,25% | 102-1 | Kuis |
| Kuis 3 — pemilihan model | K-03 | 10 | 1,25% | 102-1 | Kuis |
| Kuis 4 — JST dan evaluasi | K-04 | 13 | 1,25% | 102-1 | Kuis |
| Proposal proyek | P-00 | 5 | Prasyarat | — | — |
| Milestone 1 — *baseline* | P-01 | 7 | 5% | 082-1 | Unjuk Kerja |
| Milestone 2 — iterasi model | P-02 | 11 | 5% | 082-1 | Unjuk Kerja |
| Laporan, notebook, *model card* | P-03 | 14 | 15% | 082-1 (10%) · 102-1 (5%) | Unjuk Kerja |
| Presentasi dan tanya jawab | P-04 | 15 | 10% | 082-1 | Unjuk Kerja |
| Ujian Tengah Semester | U-01 | 8 | **20%** | 102-1 | Tes Tulis |
| Ujian Akhir Semester | U-02 | 16 | **15%** | 082-1 | Tes Tulis |
| | | | **100%** | | |

### H.3 Catatan tentang Partisipasi 0%

Kurikulum menetapkan bobot Partisipasi **0%** untuk mata kuliah ini. Konsekuensinya dinyatakan terbuka kepada mahasiswa sejak pertemuan pertama:

- **Kehadiran tetap wajib** memenuhi ketentuan universitas (minimum 75% untuk dapat mengikuti UAS).
- **Kehadiran tidak menambah nilai.** Tidak ada nilai yang diperoleh semata-mata karena hadir.
- **Namun** 25% nilai berasal dari Observasi atas pekerjaan lab yang dikerjakan **di dalam kelas**. Mahasiswa yang tidak hadir kehilangan kesempatan itu.

Dengan kata lain: kehadiran tidak dinilai, tetapi ketidakhadiran tetap berbiaya.

---

## I. KONVERSI NILAI

| Rentang | Huruf | Bobot | Keterangan |
|---------|-------|-------|------------|
| 85,00 – 100 | A | 4,00 | Sangat baik |
| 80,00 – 84,99 | A− | 3,70 | |
| 75,00 – 79,99 | B+ | 3,30 | |
| 70,00 – 74,99 | B | 3,00 | Baik |
| 65,00 – 69,99 | B− | 2,70 | |
| 60,00 – 64,99 | C+ | 2,30 | |
| 55,00 – 59,99 | C | 2,00 | Cukup — **batas lulus** |
| 45,00 – 54,99 | D | 1,00 | Kurang — mengulang |
| < 45,00 | E | 0,00 | Tidak lulus |

### Ketentuan Kelulusan Tambahan

Mahasiswa dinyatakan lulus apabila memenuhi **seluruh** syarat berikut:

1. Nilai akhir ≥ 55,00.
2. **Capaian tiap Sub-CPMK ≥ 50%** dari bobotnya. Mahasiswa yang unggul pada satu Sub-CPMK tetapi gagal total pada yang lain tidak dinyatakan lulus, karena keduanya merupakan capaian yang berbeda.
3. Mengumpulkan proyek akhir dan mengikuti presentasi.
4. Kehadiran memenuhi ketentuan universitas.

---

## J. REFERENSI

### Utama

1. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
2. Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
3. Müller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*. O'Reilly Media.

### Pendukung

4. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2023). *An Introduction to Statistical Learning with Applications in Python*. Springer. (Tersedia gratis: <https://www.statlearning.com>)
5. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.
6. Burkov, A. (2019). *The Hundred-Page Machine Learning Book*.
7. Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and Machine Learning: Limitations and Opportunities*. MIT Press. (Tersedia gratis: <https://fairmlbook.org>)
8. Mitchell, M., et al. (2019). Model Cards for Model Reporting. *FAT* '19*, 220–229.
9. Kapoor, S., & Narayanan, A. (2023). Leakage and the Reproducibility Crisis in ML-based Science. *Patterns*, 4(9).

### Dokumentasi

10. Dokumentasi `scikit-learn` — <https://scikit-learn.org/stable/user_guide.html>
11. Dokumentasi `pandas` — <https://pandas.pydata.org/docs/>

### Dokumen Kurikulum

12. Tim Kurikulum Informatika UAI (2026). *Kurikulum Informatika 2025 — Revisi 2026*. Universitas Al Azhar Indonesia. → [registri di repositori ini](../../00-kurikulum-if-2025-revisi-2026/README.md)
13. ACM/IEEE-CS (2023). *Computer Science Curricula 2023*, Knowledge Area: Artificial Intelligence (AI).
14. UNESCO (2024). *AI Competency Framework for Students*.

---

## K. KEBIJAKAN KHUSUS MATA KULIAH

### K.1 Kebijakan Kecerdasan Artifisial

Mata kuliah ini berstatus **mode Core** pada AI Curriculum Infusion Matrix. AI bukan hanya alat bantu, melainkan objek yang dipelajari. Kebijakannya karena itu lebih rinci daripada mata kuliah lain.

| Kegiatan | Status | Alasan |
|----------|--------|--------|
| Menulis kode `scikit-learn` rutin | **Boleh**, wajib dicatat | Bukan yang dinilai |
| Memperbaiki galat dan menjelaskan dokumentasi | **Boleh** | Bukan yang dinilai |
| Menyarankan jenis visualisasi | **Boleh** | Bukan yang dinilai |
| Menyunting bahasa laporan | **Boleh** | Bukan yang dinilai |
| **Memformulasikan masalah menjadi *task* ML** | **Tidak boleh** | Inti `Sub-CPMK082-1` |
| **Memilih model dan hiperparameter** | **Tidak boleh** | Inti `Sub-CPMK082-1` |
| **Memilih dan menafsirkan metrik** | **Tidak boleh** | Inti `Sub-CPMK102-1` |
| **Menganalisis kesalahan model** | **Tidak boleh** | Inti kedua Sub-CPMK |
| **Menulis *model card* dan analisis keterbatasan** | **Tidak boleh** | Inti `Sub-CPMK102-1` |
| **Selama UTS dan UAS** | **Tidak boleh sama sekali** | Ujian *closed book* |

**AI Usage Log wajib** pada setiap lab dan seluruh tahap proyek. Formatnya ada pada [RTM §I](../02-rtm/rtm-dasar-kecerdasan-artifisial-pembelajaran-mesin.md).

> Mencatat pemakaian AI tidak mengurangi nilai. Tidak mencatatnya, padahal memakainya, adalah pelanggaran integritas akademik.

### K.2 Reproduksibilitas

Kriteria kurikulum untuk `Sub-CPMK082-1` menyebut **reproduksibilitas eksperimen** secara eksplisit. Karena itu:

- Setiap notebook wajib dapat dijalankan ulang dari sel pertama sampai terakhir tanpa galat.
- `random_state` wajib ditetapkan pada setiap proses yang mengandung keacakan.
- Versi pustaka dicatat pada sel pertama.
- Data dimuat dari tautan atau disertakan, bukan dari berkas lokal yang tidak ikut dikumpulkan.

Notebook yang tidak dapat dijalankan ulang dikenai pengurangan nilai sebagaimana diatur pada [panduan proyek](../05-assessments/project-guidelines.md).

### K.3 Kebocoran Data

Kebocoran data pada pekerjaan yang dikumpulkan dikenai sanksi nilai. Ini bukan kekerasan yang berlebihan: kriteria kurikulum untuk `Sub-CPMK102-1` menyebut *"correctness preprocessing dan split"* sebagai kriteria penilaian, dan kebocoran adalah pelanggaran langsung atasnya.

| Temuan | Konsekuensi |
|--------|-------------|
| Kebocoran pada lab | Lab dikembalikan untuk diperbaiki; dinilai sebagai terlambat |
| Kebocoran pada milestone proyek | Wajib diperbaiki sebelum tahap berikutnya |
| Kebocoran pada laporan akhir | Pengurangan hingga 30% nilai proyek |

### K.4 Keterlambatan

| Keterlambatan | Pengurangan |
|---------------|-------------|
| ≤ 24 jam | 10% |
| 24–72 jam | 25% |
| > 72 jam | Tidak dinilai (nilai 0) |

Kecuali dengan alasan yang dapat diterima dan disampaikan **sebelum** tenggat.

### K.5 Kerja Kelompok

- Proyek dikerjakan berkelompok 3–4 orang.
- Lab dikerjakan **perorangan**, meski diskusi diperbolehkan.
- Setiap anggota kelompok wajib memahami keseluruhan proyek; pertanyaan saat presentasi dapat diarahkan kepada siapa saja.
- Pembagian peran dicatat dan dilaporkan; ketimpangan kontribusi yang nyata memengaruhi nilai perorangan.

---

## L. PROFIL PROYEK AKHIR

| Aspek | Ketentuan |
|-------|-----------|
| Bentuk | Kelompok 3–4 orang |
| Bobot | **35%** — komponen terbesar |
| Luaran | Notebook yang dapat dijalankan ulang · Laporan 10–15 halaman · *Model card* · Presentasi |
| Data | **Nyata**, berkonteks Indonesia, minimal 500 baris |
| Cakupan wajib | Formulasi masalah · Prapemrosesan · *Baseline* · Minimal 3 model dibandingkan · Analisis kesalahan · Analisis *bias* |
| Tahapan | P-00 (Mg 5) → P-01 (Mg 7) → P-02 (Mg 11) → P-03 (Mg 14) → P-04 (Mg 15) |
| Rincian | [Panduan Proyek](../05-assessments/project-guidelines.md) |

> **Proyek tidak menuntut model dengan kinerja tinggi.** Yang dinilai adalah ketepatan formulasi, kebenaran prosedur, kesesuaian metrik, dan kejujuran analisis. Proyek yang melaporkan *"model kami tidak mengungguli baseline, dan berikut analisis mengapa"* dengan prosedur yang benar bernilai lebih tinggi daripada proyek dengan akurasi 99% yang ternyata mengandung kebocoran.

---

## M. KETERKAITAN DENGAN MATA KULIAH LAIN

### M.1 Prasyarat yang Dipakai

| Mata kuliah | Yang dipakai di sini |
|-------------|----------------------|
| Probabilitas dan Statistik (sem 1) | Distribusi, Bayes, inferensi, interval kepercayaan, korelasi–regresi, ukuran efek |
| Dasar-dasar Pemrograman (sem 1–2) | Python, struktur kendali, fungsi |
| Struktur Data dan Algoritma (sem 3) | Kompleksitas, struktur pohon, kompromi ruang–waktu |
| Basis Data (sem 4) | Pengambilan dan penggabungan data |

### M.2 Mata Kuliah yang Bergantung

| Mata kuliah | Sem | Yang dibawa dari sini |
|-------------|-----|------------------------|
| Jaringan Syaraf Tiruan dan Pembelajaran Mendalam | 5 | Dasar pelatihan, *loss*, evaluasi, *overfitting* |
| Sains Data | 6 | Seluruh alur ML dan evaluasinya |
| Pengolahan Citra | 6 | Klasifikasi, metrik, validasi |
| Pengolahan Bahasa Alami | 7 | Klasifikasi, evaluasi, *embedding* sebagai fitur |
| Web Semantik | 7 | Representasi dan penalaran atas data |
| Tugas Akhir | 7–8 | Metodologi eksperimen dan pembandingan yang sah |

### M.3 Catatan Koordinasi

- **Dengan Jaringan Syaraf Tiruan (semester yang sama):** pembagian disepakati — mata kuliah ini hanya memberi pengantar MLP pada Minggu 13; arsitektur lanjut sepenuhnya di IF52510032.
- **Dengan Teknopreneur (semester yang sama):** proyek boleh berbagi tema, dengan syarat luaran keduanya berbeda dan dinyatakan terbuka kepada kedua dosen.
- **Dengan Probabilitas dan Statistik:** Bab 4 dan 7 memuat pengulangan terarah, karena rentang empat semester membuat sebagian materi terlupa.

---

## N. PENGESAHAN

| Peran | Nama | Tanda Tangan | Tanggal |
|-------|------|--------------|---------|
| Dosen Pengampu | Tri Aji Nugroho, S.T., M.T. | | |
| Koordinator Rumpun R06 | | | |
| Ketua Program Studi Informatika | | | |

**Jakarta, September 2026**

---

### Riwayat Dokumen

| Versi | Tanggal | Perubahan |
|-------|---------|-----------|
| 1.0 | September 2026 | Penyusunan awal mengacu Kurikulum Informatika 2025 Revisi 2026 |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
