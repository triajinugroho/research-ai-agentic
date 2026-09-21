# RENCANA TUGAS MAHASISWA (RTM)

## UNIVERSITAS AL AZHAR INDONESIA
### PROGRAM STUDI INFORMATIKA

**Kurikulum Informatika 2025 — Revisi 2026**

---

## IDENTITAS

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin |
| Kode | `IF52510031` |
| Bobot | 3 SKS |
| Semester | 5 (Ganjil 2026/2027) |
| Dosen Pengampu | Tri Aji Nugroho, S.T., M.T. |
| Dokumen induk | [RPS](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md) |

---

## A. PETA TUGAS TERHADAP SUB-CPMK

| Kelompok Tugas | Kode | Jumlah | Bobot | `Sub-CPMK082-1` | `Sub-CPMK102-1` |
|----------------|------|--------|-------|-----------------|-----------------|
| Praktikum (Observasi) | T-01…T-14 | 13 | 25% | 15% | 10% |
| Kuis | K-01…K-04 | 4 | 5% | — | 5% |
| Proyek (Unjuk Kerja) | P-00…P-04 | 5 tahap | 35% | 30% | 5% |
| Ujian Tulis | U-01, U-02 | 2 | 35% | 15% | 20% |
| **Total** | | | **100%** | **60%** | **40%** |

---

## B. RINGKASAN SELURUH TUGAS

| Kode | Nama | Mg | Bentuk | Bobot | Sub-CPMK | Tenggat |
|------|------|----|--------|-------|----------|---------|
| T-01 | Penyiapan lingkungan dan eksplorasi dataset pertama | 1 | Notebook | 1,9% | 082-1 | Mg 2 |
| T-02 | Formulasi masalah dan *baseline* | 2 | Notebook + dokumen | 1,9% | 082-1 | Mg 3 |
| T-03 | *Pipeline* prapemrosesan | 3 | Notebook | 1,9% | 102-1 | Mg 4 |
| T-04 | Validasi silang dan perburuan kebocoran | 4 | Notebook + laporan temuan | 1,9% | 102-1 | Mg 5 |
| T-05 | Rekayasa fitur | 5 | Notebook | 1,9% | 102-1 | Mg 6 |
| T-06 | Model regresi dan metriknya | 6 | Notebook | 1,9% | 082-1 | Mg 7 |
| T-07 | Model klasifikasi dan metriknya | 7 | Notebook | 1,9% | 082-1 | Mg 9 |
| T-09 | Pohon keputusan dan *ensemble* | 9 | Notebook | 1,9% | 082-1 | Mg 10 |
| T-10 | SVM, Naive Bayes, dan penyetelan | 10 | Notebook | 1,9% | 082-1 | Mg 11 |
| T-11 | *Clustering* dan metriknya | 11 | Notebook | 1,9% | 082-1 | Mg 12 |
| T-12 | PCA dan visualisasi kinerja model | 12 | Notebook | 1,9% | 102-1 | Mg 13 |
| T-13 | Jaringan saraf tiruan | 13 | Notebook | 1,9% | 082-1 | Mg 14 |
| T-14 | Audit *bias* dan *model card* | 14 | Notebook + *model card* | 1,9% | 102-1 | Mg 15 |
| K-01 | Kuis — data dan kebocoran | 4 | 20 menit | 1,25% | 102-1 | Di kelas |
| K-02 | Kuis — metrik klasifikasi | 7 | 20 menit | 1,25% | 102-1 | Di kelas |
| K-03 | Kuis — pemilihan model | 10 | 20 menit | 1,25% | 102-1 | Di kelas |
| K-04 | Kuis — JST dan evaluasi | 13 | 20 menit | 1,25% | 102-1 | Di kelas |
| P-00 | Proposal proyek | 5 | PDF 2 halaman | Prasyarat | — | Mg 5 |
| P-01 | Milestone 1 — *baseline* | 7 | Notebook + ringkasan | 5% | 082-1 | Mg 7 |
| P-02 | Milestone 2 — iterasi dan analisis kesalahan | 11 | Notebook + ringkasan | 5% | 082-1 | Mg 11 |
| P-03 | Laporan akhir, notebook, *model card* | 14 | PDF + `.ipynb` + MD | 15% | 082-1 (10%) · 102-1 (5%) | Mg 14 |
| P-04 | Presentasi dan tanya jawab | 15 | 20' + tanya jawab | 10% | 082-1 | Mg 15 |
| U-01 | Ujian Tengah Semester | 8 | Tes tulis 120' | 20% | 102-1 | Mg 8 |
| U-02 | Ujian Akhir Semester | 16 | Tes tulis 120' | 15% | 082-1 | Mg 16 |

> Bobot tiap lab adalah 25% ÷ 13 ≈ **1,9%**.

---

## C. RINCIAN TUGAS PRAKTIKUM (T-01 s.d. T-14)

### Ketentuan Umum Seluruh Praktikum

| Aspek | Ketentuan |
|-------|-----------|
| Bentuk | Notebook Google Colab (`.ipynb`) |
| Pengumpulan | Tautan Colab (akses "siapa saja dengan tautan") + berkas `.ipynb` |
| Penamaan | `NIM_Nama_LabNN.ipynb` |
| Reproduksibilitas | **Wajib** dapat dijalankan ulang dari sel pertama; `random_state` ditetapkan |
| Komentar kode | Bahasa Indonesia |
| Interpretasi | **Setiap keluaran wajib disertai kalimat penafsiran** |
| AI Usage Log | **Wajib**, di sel terakhir |
| Tenggat | Awal pertemuan minggu berikutnya |

### Rubrik Umum Praktikum (berlaku untuk T-01 s.d. T-14)

| Aspek | Bobot | 4 | 3 | 2 | 1 |
|-------|-------|---|---|---|---|
| Kebenaran teknis | 40% | Seluruh langkah benar; tanpa kebocoran | Benar dengan kekeliruan kecil | Ada kekeliruan yang memengaruhi hasil | Langkah pokok salah |
| Kesesuaian metrik/metode | 25% | Tepat dan beralasan | Tepat, alasan kurang | Dapat diterima tetapi bukan yang optimal | Tidak sesuai |
| Kualitas interpretasi | 25% | Tajam, sebatas data, menyebut keterbatasan | Tepat, keterbatasan kurang dibahas | Ada klaim melampaui data | Tidak ada interpretasi |
| Reproduksibilitas dan kerapian | 10% | Berjalan ulang mulus; terstruktur | Berjalan dengan penyesuaian kecil | Perlu perbaikan agar berjalan | Tidak dapat dijalankan |

---

### T-01 — Penyiapan Lingkungan dan Eksplorasi Dataset Pertama

| Aspek | Keterangan |
|-------|------------|
| Minggu | 1 · **Sub-CPMK082-1** · ICM-01 |
| Tujuan | Menyiapkan lingkungan kerja dan mengenali anatomi masalah ML |
| Luaran | Notebook berisi pemeriksaan dataset dan klasifikasi jenis *task* |
| Kegiatan | Memasang dan memeriksa versi pustaka; memuat tiga dataset berbeda; untuk tiap dataset menentukan: jenis *task*, target, fitur, dan apakah ML memang diperlukan |
| Kriteria khusus | Ketepatan penentuan jenis *task*; alasan tertulis untuk tiap penentuan |

### T-02 — Formulasi Masalah dan *Baseline*

| Aspek | Keterangan |
|-------|------------|
| Minggu | 2 · **Sub-CPMK082-1** · ICM-02 |
| Tujuan | Mengubah masalah nyata menjadi rumusan *task* ML yang dapat dikerjakan |
| Luaran | Dokumen formulasi + notebook *baseline* |
| Kegiatan | Memilih satu masalah dari daftar kasus Indonesia; menuliskan formulasi lengkap (target, fitur, metrik, ambang keberhasilan, dampak kesalahan); membangun *baseline* paling sederhana (`DummyClassifier`/`DummyRegressor`) |
| Kriteria khusus | Metrik dipilih sesuai dampak kesalahan, bukan sesuai kebiasaan; *baseline* dilaporkan sebagai pembanding wajib |

### T-03 — *Pipeline* Prapemrosesan

| Aspek | Keterangan |
|-------|------------|
| Minggu | 3 · **Sub-CPMK102-1** · ICM-03 |
| Tujuan | Menyusun prapemrosesan yang benar dan dapat diulang |
| Luaran | Notebook berisi `Pipeline` dan `ColumnTransformer` yang berfungsi |
| Kegiatan | Memeriksa kualitas data BPS yang belum bersih; menangani nilai hilang, kategorik, dan penskalaan **di dalam `Pipeline`**; mendokumentasikan setiap keputusan |
| Kriteria khusus | Seluruh transformasi berada di dalam `Pipeline` — bukan diterapkan pada data lengkap sebelum pembagian |

### T-04 — Validasi Silang dan Perburuan Kebocoran

| Aspek | Keterangan |
|-------|------------|
| Minggu | 4 · **Sub-CPMK102-1** · ICM-04 |
| Tujuan | Mengenali dan memperbaiki kebocoran data |
| Luaran | Notebook perbaikan + laporan temuan satu halaman |
| Kegiatan | Diberikan notebook yang sengaja mengandung **empat kebocoran berbeda**; mahasiswa menemukan seluruhnya, menjelaskan mekanismenya, memperbaikinya, dan melaporkan selisih kinerja sebelum-sesudah |
| Kriteria khusus | Jumlah kebocoran yang ditemukan; ketepatan penjelasan mekanismenya |

### T-05 — Rekayasa Fitur

| Aspek | Keterangan |
|-------|------------|
| Minggu | 5 · **Sub-CPMK102-1** · ICM-05 |
| Tujuan | Meningkatkan kinerja melalui fitur, bukan melalui model |
| Luaran | Notebook dengan perbandingan sebelum-sesudah |
| Kegiatan | Model dan hiperparameter **dikunci**; mahasiswa hanya boleh mengubah fitur; melaporkan fitur mana yang membantu dan mana yang tidak, beserta dugaan sebabnya |
| Kriteria khusus | Tidak ada fitur yang menimbulkan kebocoran; peningkatan diukur pada data validasi, bukan latih |

### T-06 — Model Regresi dan Metriknya

| Aspek | Keterangan |
|-------|------------|
| Minggu | 6 · **Sub-CPMK082-1** · ICM-06 |
| Tujuan | Membangun dan membandingkan model regresi |
| Luaran | Notebook perbandingan tiga model |
| Kegiatan | Melatih regresi linear, Ridge, dan Lasso pada data harga properti; melaporkan MAE, RMSE, R², dan MAPE; menjelaskan **mengapa metrik-metrik itu berbeda kesimpulannya** |
| Kriteria khusus | Pemilihan metrik dikaitkan dengan konteks masalah; *baseline* disertakan |

### T-07 — Model Klasifikasi dan Metriknya

| Aspek | Keterangan |
|-------|------------|
| Minggu | 7 · **Sub-CPMK082-1** · ICM-07 |
| Tujuan | Memahami mengapa akurasi sering menyesatkan |
| Luaran | Notebook dengan analisis metrik lengkap |
| Kegiatan | Melatih regresi logistik dan k-NN pada data **tak seimbang**; menghitung matriks konfusi secara manual lebih dahulu, lalu memverifikasinya dengan `scikit-learn`; menggeser ambang keputusan dan menganalisis dampaknya |
| Kriteria khusus | Perhitungan manual benar; pemilihan ambang dikaitkan dengan biaya kesalahan |

### T-09 — Pohon Keputusan dan *Ensemble*

| Aspek | Keterangan |
|-------|------------|
| Minggu | 9 · **Sub-CPMK082-1** · ICM-08 |
| Tujuan | Memahami cara kerja pohon dan mengapa *ensemble* lebih kuat |
| Luaran | Notebook + perhitungan manual |
| Kegiatan | Menghitung *entropy* dan *information gain* satu percabangan secara manual; melatih pohon tunggal, *Random Forest*, dan *gradient boosting*; membandingkan kinerja dan kepentingan fitur |
| Kriteria khusus | Perhitungan manual benar; pembahasan mengapa pohon tunggal *overfit* |

### T-10 — SVM, Naive Bayes, dan Penyetelan

| Aspek | Keterangan |
|-------|------------|
| Minggu | 10 · **Sub-CPMK082-1** · ICM-09 |
| Tujuan | Membandingkan model secara adil |
| Luaran | Notebook perbandingan lima model |
| Kegiatan | Menyetel hiperparameter dengan `GridSearchCV` pada data latih saja; membandingkan lima model dengan protokol yang sama; menyajikan hasil dalam satu tabel dengan rerata dan simpangan lipatan |
| Kriteria khusus | Penyetelan tidak menyentuh data uji; perbandingan memakai lipatan yang sama untuk seluruh model |

### T-11 — *Clustering* dan Metriknya

| Aspek | Keterangan |
|-------|------------|
| Minggu | 11 · **Sub-CPMK082-1** · ICM-10 |
| Tujuan | Menerapkan pembelajaran tanpa supervisi dan menafsirkan hasilnya |
| Luaran | Notebook + penafsiran tiap klaster |
| Kegiatan | Segmentasi provinsi Indonesia berdasarkan indikator BPS; membandingkan K-Means, *hierarchical*, dan DBSCAN; menentukan jumlah klaster dengan *elbow* dan *silhouette*; **memberi nama dan penafsiran substantif** pada tiap klaster |
| Kriteria khusus | Penafsiran klaster bermakna, bukan sekadar "klaster 0, klaster 1" |

### T-12 — PCA dan Visualisasi Kinerja Model

| Aspek | Keterangan |
|-------|------------|
| Minggu | 12 · **Sub-CPMK102-1** · ICM-11 |
| Tujuan | Mendiagnosis model melalui visualisasi |
| Luaran | Notebook dengan lima jenis grafik diagnostik |
| Kegiatan | Menerapkan PCA dan melaporkan *explained variance*; membuat kurva pembelajaran, kurva validasi, matriks konfusi ternormalisasi, kurva ROC, dan kurva *precision-recall*; **mendiagnosis kondisi model dari grafik saja** |
| Kriteria khusus | Diagnosis (*overfit*/*underfit*/cukup) tepat dan beralasan dari grafik |

### T-13 — Jaringan Saraf Tiruan

| Aspek | Keterangan |
|-------|------------|
| Minggu | 13 · **Sub-CPMK082-1** · ICM-12 |
| Tujuan | Memahami JST secukupnya untuk menilai kapan ia diperlukan |
| Luaran | Notebook + perhitungan manual satu langkah |
| Kegiatan | Menghitung satu langkah maju dan satu langkah mundur secara manual pada jaringan 2-2-1; melatih `MLPClassifier`; **membandingkannya dengan *Random Forest* pada data tabular yang sama** dan membahas hasilnya |
| Kriteria khusus | Perhitungan manual benar; pembahasan jujur bila JST ternyata tidak lebih unggul |

### T-14 — Audit *Bias* dan *Model Card*

| Aspek | Keterangan |
|-------|------------|
| Minggu | 14 · **Sub-CPMK102-1** · ICM-13 |
| Tujuan | Menilai keadilan model dan mendokumentasikannya |
| Luaran | Notebook audit + *model card* |
| Kegiatan | Mengukur kinerja model buatan sendiri **terpisah per kelompok** (wilayah, jenis kelamin, atau kelompok lain yang relevan); menghitung selisih *recall* dan *precision* antarkelompok; menyusun *model card* lengkap |
| Kriteria khusus | Audit dilakukan pada model sendiri, bukan contoh; *model card* memuat keterbatasan yang jujur |

---

## D. RINCIAN KUIS (K-01 s.d. K-04)

| Aspek | Ketentuan |
|-------|-----------|
| Bentuk | Tertulis di kelas, 20 menit, *closed book* |
| Alat bantu AI | **Tidak diperkenankan** |
| Kalkulator | Diperkenankan |
| Bobot | 1,25% per kuis |
| Sub-CPMK | Seluruhnya `DAIML-Sub-CPMK102-1` |

| Kode | Mg | Cakupan | Bentuk soal |
|------|----|---------|-------------|
| K-01 | 4 | Kualitas data, prapemrosesan, jenis kebocoran | 2 soal analisis kasus: temukan kebocoran pada potongan kode |
| K-02 | 7 | Matriks konfusi, *precision*/*recall*/F1, pemilihan metrik | 1 soal hitung + 1 soal pemilihan metrik beralasan |
| K-03 | 10 | Validasi silang, penyetelan, perbandingan model | 2 soal analisis protokol eksperimen |
| K-04 | 13 | Diagnosis dari kurva, metrik *clustering*, evaluasi JST | 2 soal pembacaan grafik dan diagnosis |

> Seluruh kuis menguji **penalaran atas prosedur**, bukan hafalan sintaks. Tidak ada soal yang menanyakan nama fungsi.

---

## E. RINCIAN PROYEK (P-00 s.d. P-04)

Proyek adalah komponen terbesar (**35%**) dan dikerjakan bertahap sejak Minggu 5. Rincian lengkap ada pada [Panduan Proyek](../05-assessments/project-guidelines.md); bagian ini merangkum tenggat dan luarannya.

### P-00 — Proposal (Minggu 5) — *Prasyarat, tidak berbobot*

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | PDF maksimal 2 halaman |
| Isi wajib | Anggota dan pembagian peran · Masalah dan mengapa penting · **Formulasi *task* ML** (target, fitur, jenis *task*) · Sumber data dengan dimensi yang sudah diperiksa · Metrik keberhasilan **beserta alasan** · Dampak bila model salah · Risiko yang sudah dapat diperkirakan |
| Syarat persetujuan | Data **sudah diunduh dan dibuka**; masalah dapat diselesaikan dengan metode sampai Minggu 14; ukuran data memadai (≥ 500 baris) |
| Konsekuensi | Tanpa proposal yang disetujui, milestone berikutnya tidak dinilai |

### P-01 — Milestone 1: *Baseline* (Minggu 7) — **5%** · `Sub-CPMK082-1`

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook + ringkasan 1 halaman |
| Isi wajib | Data sudah dibersihkan dengan `Pipeline` · Pembagian data yang benar · **Skor *baseline*** (`Dummy`) · Satu model sederhana sebagai pembanding · Pernyataan eksplisit bahwa tidak ada kebocoran, beserta pemeriksaannya |
| Kriteria | Kebenaran pembagian data · Kesesuaian metrik · Kejujuran pelaporan |

### P-02 — Milestone 2: Iterasi dan Analisis Kesalahan (Minggu 11) — **5%** · `Sub-CPMK082-1`

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook + ringkasan 1 halaman |
| Isi wajib | Minimal **tiga model** dibandingkan dengan protokol sama · Penyetelan hiperparameter · **Analisis kesalahan**: kasus mana yang salah diprediksi dan adakah polanya · Keputusan model mana yang dilanjutkan, beserta alasannya |
| Kriteria | Keadilan protokol perbandingan · Kedalaman analisis kesalahan |

### P-03 — Laporan Akhir, Notebook, dan *Model Card* (Minggu 14) — **15%**

| Komponen | Bobot | Sub-CPMK |
|----------|-------|----------|
| Kebenaran teknis dan reproduksibilitas | 10% | 082-1 |
| Evaluasi, visualisasi, dan interpretasi | 5% | 102-1 |

| Aspek | Ketentuan |
|-------|-----------|
| Laporan | PDF 10–15 halaman |
| Notebook | `.ipynb` yang **dapat dijalankan ulang tanpa galat** |
| *Model card* | Berkas Markdown terpisah, mengikuti format Mitchell et al. (2019) |
| Struktur laporan | 1. Pendahuluan dan formulasi · 2. Data dan prapemrosesan · 3. Metode dan protokol eksperimen · 4. Hasil dan evaluasi · 5. Analisis kesalahan dan *bias* · 6. Kesimpulan dan keterbatasan · Lampiran: AI Usage Log |

### P-04 — Presentasi dan Tanya Jawab (Minggu 15) — **10%** · `Sub-CPMK082-1`

| Bagian | Durasi | Isi |
|--------|--------|-----|
| Masalah dan formulasi | 3' | Mengapa penting; bagaimana dirumuskan menjadi *task* ML |
| Data dan prapemrosesan | 4' | Sumber, kualitas, keputusan pembersihan |
| Metode dan protokol | 4' | Model yang dibandingkan; bagaimana perbandingannya dijaga adil |
| Hasil dan analisis kesalahan | 6' | Metrik, *baseline*, kasus yang salah |
| Keterbatasan dan dampak | 3' | Apa yang tidak dapat dilakukan model ini; siapa yang berisiko dirugikan |
| **Tanya jawab** | **8'** | Pertanyaan dapat diarahkan kepada anggota mana pun |

**Ketentuan:** slide maksimal 15 halaman; setiap anggota wajib berbicara; seluruh anggota wajib menguasai keseluruhan isi.

---

## F. RINCIAN UJIAN (U-01 dan U-02)

### U-01 — Ujian Tengah Semester (Minggu 8) — **20%** · `Sub-CPMK102-1`

| Aspek | Ketentuan |
|-------|-----------|
| Bentuk | Tes tulis, *closed book*, 120 menit |
| Alat bantu | Kalkulator. **Tanpa catatan, tanpa perangkat, tanpa AI.** |
| Cakupan | Minggu 1–7 |
| Penekanan | Kualitas data, prapemrosesan, kebocoran, rekayasa fitur, metrik regresi dan klasifikasi |
| Komposisi | 30% konsep · 40% analisis kasus · 30% perhitungan manual |
| Kisi-kisi | [kisi-kisi-uts.md](../05-assessments/kisi-kisi-uts.md) |

### U-02 — Ujian Akhir Semester (Minggu 16) — **15%** · `Sub-CPMK082-1`

| Aspek | Ketentuan |
|-------|-----------|
| Bentuk | Tes tulis, *closed book*, 120 menit |
| Alat bantu | Kalkulator. **Tanpa catatan, tanpa perangkat, tanpa AI.** |
| Cakupan | Seluruh materi, penekanan Minggu 9–14 |
| Penekanan | Pemilihan model, *ensemble*, *clustering*, JST, AI bertanggung jawab |
| Komposisi | 25% konsep · 45% perancangan solusi · 30% perhitungan manual |
| Kisi-kisi | [kisi-kisi-uas.md](../05-assessments/kisi-kisi-uas.md) |

---

## G. JADWAL PENGUMPULAN TERPADU

| Mg | Yang jatuh tempo | Yang dimulai |
|----|------------------|--------------|
| 1 | — | T-01 |
| 2 | **T-01** | T-02 |
| 3 | **T-02** | T-03 |
| 4 | **T-03** · **K-01** (di kelas) | T-04 |
| 5 | **T-04** · **P-00 proposal** | T-05 · Proyek |
| 6 | **T-05** | T-06 |
| 7 | **T-06** · **K-02** (di kelas) · **P-01 milestone 1** | T-07 |
| 8 | **U-01 — UTS** | — |
| 9 | **T-07** | T-09 |
| 10 | **T-09** · **K-03** (di kelas) | T-10 |
| 11 | **T-10** · **P-02 milestone 2** | T-11 |
| 12 | **T-11** | T-12 |
| 13 | **T-12** · **K-04** (di kelas) | T-13 |
| 14 | **T-13** · **P-03 laporan + notebook + model card** | T-14 |
| 15 | **T-14** · **P-04 presentasi** | — |
| 16 | **U-02 — UAS** | — |

> **Minggu 14 adalah titik tersibuk.** Kelompok yang mengerjakan proyek secara bertahap sejak Minggu 5 akan menghadapinya dengan tenang; yang menunda tidak.

---

## H. BEBAN BELAJAR MAHASISWA

Sesuai SN-Dikti, 1 SKS = 170 menit/minggu. Untuk 3 SKS: **510 menit (8,5 jam) per minggu**.

| Kegiatan | Menit/minggu | Keterangan |
|----------|--------------|------------|
| Tatap muka | 150 | Kuliah dan praktik terbimbing |
| Penugasan terstruktur | 180 | Praktikum, kuis, proyek |
| Belajar mandiri | 180 | Membaca bab, latihan soal, eksplorasi |
| **Total** | **510** | |

### Perkiraan Beban per Tahap

| Tahap | Perkiraan jam kelompok |
|-------|------------------------|
| P-00 Proposal | 6–8 jam |
| P-01 Milestone 1 | 10–14 jam |
| P-02 Milestone 2 | 14–18 jam |
| P-03 Laporan akhir | 20–25 jam |
| P-04 Presentasi | 6–8 jam |
| **Total proyek** | **56–73 jam kelompok** |

---

## I. AI USAGE LOG — FORMAT WAJIB

Disertakan pada sel terakhir setiap notebook praktikum dan sebagai lampiran setiap tahap proyek.

```markdown
## AI Usage Log

| No | Bagian | Alat | Permintaan (ringkas) | Dipakai? | Verifikasi |
|----|--------|------|----------------------|----------|------------|
| 1  | Sel 4  | Claude | Sintaks ColumnTransformer untuk kolom campuran | Ya, disesuaikan | Dijalankan; keluaran diperiksa terhadap data |
| 2  | Sel 9  | ChatGPT | Arti peringatan ConvergenceWarning | Ya, penjelasannya | Diperiksa ke dokumentasi scikit-learn |
| 3  | Sel 12 | —      | Pemilihan metrik: dikerjakan sendiri | — | — |
| 4  | Analisis | —    | Interpretasi hasil: dikerjakan sendiri | — | — |

**Pernyataan:** Seluruh keputusan formulasi masalah, pemilihan model, pemilihan
metrik, dan penafsiran hasil dalam notebook ini dibuat oleh saya sendiri.
Bantuan AI terbatas pada hal yang tercatat di atas dan telah saya verifikasi.

Nama: ____________________  NIM: __________  Tanggal: __________
```

### Yang Wajib Ditulis "Dikerjakan Sendiri"

Empat baris berikut **harus** muncul dalam setiap log, karena keempatnya merupakan inti Sub-CPMK dan tidak boleh diserahkan kepada AI:

1. Formulasi masalah menjadi *task* ML
2. Pemilihan model dan hiperparameter
3. Pemilihan dan penafsiran metrik
4. Analisis kesalahan dan keterbatasan

Log yang mencantumkan AI pada salah satu dari empat baris itu dikembalikan, dan pekerjaannya dinilai ulang sesuai ketentuan integritas akademik pada [RPS §K.1](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md).

---

## J. DAFTAR PERIKSA SEBELUM MENGUMPULKAN

Berlaku untuk setiap praktikum dan setiap tahap proyek:

- [ ] Notebook berjalan ulang dari sel pertama sampai terakhir tanpa galat
- [ ] `random_state` ditetapkan pada setiap proses acak
- [ ] Versi pustaka tercatat di sel pertama
- [ ] Seluruh transformasi berada di dalam `Pipeline`
- [ ] Data uji **tidak pernah** dipakai untuk penyetelan atau pemilihan
- [ ] *Baseline* disertakan sebagai pembanding
- [ ] Metrik sesuai jenis masalah, dan alasannya tertulis
- [ ] Setiap keluaran disertai kalimat penafsiran
- [ ] Keterbatasan dinyatakan
- [ ] AI Usage Log lengkap dan ditandatangani
- [ ] Penamaan berkas sesuai ketentuan
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
