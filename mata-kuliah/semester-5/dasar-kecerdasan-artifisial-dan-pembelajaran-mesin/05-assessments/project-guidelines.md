# Panduan Proyek

## Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — IF52510031

**Semester Ganjil 2026/2027**
**Bobot:** 35% nilai akhir — teknik **Unjuk Kerja** (komponen terbesar)
**Sub-CPMK:** `DAIML-Sub-CPMK082-1` (30%) + `DAIML-Sub-CPMK102-1` (5%)
**Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.

---

## 1. Gambaran Umum

Proyek adalah **tulang punggung mata kuliah ini**, bukan pelengkap akhir semester. Bobotnya (35%) lebih besar daripada UTS (20%) maupun UAS (15%), dan ia merupakan satu-satunya asesmen yang menuntut alur kerja pembelajaran mesin secara utuh pada masalah nyata yang tidak terstruktur.

### Yang Dituntut

> Membangun **solusi pembelajaran mesin utuh** untuk sebuah masalah nyata berkonteks Indonesia: merumuskan *task*, menyiapkan data tanpa kebocoran, membandingkan model secara adil, mengevaluasi dengan metrik yang sesuai, menganalisis kesalahan dan keadilannya, lalu mendokumentasikannya dalam *model card*.

---

## 2. Ketentuan Dasar

| Aspek | Ketentuan |
|-------|-----------|
| Bentuk | Kelompok 3–4 orang |
| Data | **Harus nyata** — BPS, Satu Data Indonesia, Jakarta Open Data, portal daerah, Kaggle berkonteks Indonesia, atau data primer |
| Data sintetis | **Tidak diperkenankan** sebagai data utama; boleh sebagai pembanding dan wajib dinyatakan |
| Ukuran data | **Minimal 500 baris**; disarankan 2.000–100.000 |
| Jenis *task* | Klasifikasi, regresi, atau *clustering* |
| Cakupan wajib | Formulasi · Prapemrosesan dalam `Pipeline` · *Baseline* · **Minimal 3 model dibandingkan** · Analisis kesalahan · Audit *bias* |
| Perangkat | Python di Google Colab; `scikit-learn` |
| Penelusuran versi | Repositori GitHub (disarankan) |

---

## 3. Lima Tahap dan Tenggat

Proyek dikerjakan **bertahap sejak Minggu 5**, bukan menumpuk di Minggu 14.

| Tahap | Kode | Mg | Luaran | Bobot |
|-------|------|----|--------|-------|
| Proposal | P-00 | **5** | PDF 2 halaman | **Prasyarat** |
| Milestone 1 — *baseline* | P-01 | **7** | Notebook + ringkasan | **5%** |
| Milestone 2 — iterasi dan analisis kesalahan | P-02 | **11** | Notebook + ringkasan | **5%** |
| Laporan, notebook, *model card* | P-03 | **14** | PDF + `.ipynb` + `.md` | **15%** |
| Presentasi dan tanya jawab | P-04 | **15** | Slide + presentasi 20' | **10%** |

> Tanpa proposal yang disetujui pada Minggu 5, **tahap berikutnya tidak dinilai**.

---

## 4. P-00 — Proposal (Minggu 5)

### 4.1 Isi Wajib

PDF maksimal 2 halaman berisi:

1. **Identitas kelompok** — nama, NIM, dan **pembagian peran** tiap anggota.
2. **Masalah** — apa masalahnya dan mengapa penting, dalam satu paragraf.
3. **Formulasi *task* ML** — target (tepatnya), jenis *task*, **kapan prediksi dibutuhkan**.
4. **Sumber data** — nama, tautan, **jumlah baris dan kolom yang sudah diperiksa sendiri**, lisensi, tanggal akses.
5. **Fitur yang tidak boleh dipakai** — minimal dua, beserta alasannya.
6. **Metrik keberhasilan** — metrik apa, **mengapa**, dan **berapa ambang keberhasilannya**.
7. **Dampak bila model salah** — siapa yang dirugikan oleh masing-masing jenis kesalahan.
8. **Risiko** yang sudah dapat diperkirakan.

### 4.2 Syarat Persetujuan

| Kriteria | Penjelasan |
|----------|------------|
| Data sudah dibuka | Kelompok sudah mengunduh dan memeriksa dimensinya, bukan sekadar menemukan tautannya |
| Ukuran memadai | Minimal 500 baris |
| Dapat dikerjakan | Dengan metode sampai Minggu 14, oleh 3–4 mahasiswa, dalam 9 minggu |
| Spesifik | Bukan "menganalisis data pendidikan", melainkan *task* yang tajam |
| Ambang ditetapkan | Kriteria keberhasilan ditulis **sebelum** melihat hasil |

### 4.3 Contoh Formulasi yang Baik dan Lemah

| Lemah | Mengapa lemah | Perbaikan |
|-------|---------------|-----------|
| "Memprediksi kemiskinan" | Target tidak jelas | "Klasifikasi biner: apakah rumah tangga tergolong desil 1–2 berdasarkan data Susenas" |
| "Menganalisis data BPS dengan AI" | Bukan *task* | "Regresi: memperkirakan IPM kabupaten dari 8 indikator sosial-ekonomi" |
| "Membuat chatbot" | Melampaui cakupan MK | "Klasifikasi: mengelompokkan keluhan warga ke dalam 6 kategori layanan" |
| "Memprediksi harga saham" | Data deret waktu keuangan di luar cakupan | "Regresi: memperkirakan harga properti dari ciri bangunan dan lokasi" |

### 4.4 Tema yang Disarankan

| Tema | Sumber data | Jenis *task* |
|------|-------------|--------------|
| Kelayakan kredit UMKM | Data koperasi / OJK terbuka | Klasifikasi biner |
| Perkiraan IPM kabupaten | BPS | Regresi |
| Segmentasi wilayah berdasarkan indikator | BPS | *Clustering* |
| Klasifikasi keluhan layanan publik | Jakarta Open Data | Klasifikasi multikelas |
| Perkiraan jumlah penumpang TransJakarta | Jakarta Open Data | Regresi |
| Deteksi anomali konsumsi listrik | Data PLN terbuka / simulasi berbasis pola nyata | Deteksi anomali |
| Prediksi putus sekolah | Dapodik / data sekolah | Klasifikasi biner |
| Perkiraan kualitas udara | BMKG / Jakarta Open Data | Regresi |
| Segmentasi pelanggan UMKM | Data primer survei | *Clustering* |

---

## 5. P-01 — Milestone 1: *Baseline* (Minggu 7) — 5%

### 5.1 Isi Wajib

| # | Yang harus ada |
|---|----------------|
| 1 | Pemeriksaan kualitas data lengkap (tujuh perintah pembuka) |
| 2 | Pembersihan dan prapemrosesan **di dalam `Pipeline`** |
| 3 | Pembagian data dengan strategi yang **sesuai sifat data** |
| 4 | **Skor *baseline*** (`DummyClassifier`/`DummyRegressor`) |
| 5 | Satu model sederhana sebagai pembanding |
| 6 | **Pernyataan eksplisit bebas kebocoran**, beserta pemeriksaan yang dilakukan |
| 7 | Ringkasan 1 halaman |

### 5.2 Rubrik — `Sub-CPMK082-1`, 5%

| Aspek | Bobot | 4 | 3 | 2 | 1 |
|-------|-------|---|---|---|---|
| Kebenaran pembagian data | 2,0% | Strategi tepat sesuai sifat data; alasan ditulis | Tepat, alasan kurang | Dapat diterima tetapi bukan optimal | Salah (misalnya acak pada deret waktu) |
| Kesesuaian metrik | 1,5% | Sesuai masalah dan dampak kesalahan | Sesuai, alasan kurang | Dapat diterima | Tidak sesuai |
| Kejujuran pelaporan | 1,5% | *Baseline* dilaporkan; pemeriksaan kebocoran ditunjukkan | Lengkap dengan kekurangan kecil | *Baseline* ada tetapi tidak ditafsirkan | Tidak ada *baseline* |

---

## 6. P-02 — Milestone 2: Iterasi dan Analisis Kesalahan (Minggu 11) — 5%

### 6.1 Isi Wajib

| # | Yang harus ada |
|---|----------------|
| 1 | **Minimal tiga model** dibandingkan dengan protokol yang sama |
| 2 | Penyetelan hiperparameter **pada data latih saja** |
| 3 | Tabel perbandingan dengan **rerata dan simpangan antarlipatan** |
| 4 | **Analisis kesalahan** — kasus mana yang salah, adakah polanya |
| 5 | Keputusan model mana yang dilanjutkan, beserta alasannya |
| 6 | Ringkasan 1 halaman |

### 6.2 Rubrik — `Sub-CPMK082-1`, 5%

| Aspek | Bobot | 4 | 3 | 2 | 1 |
|-------|-------|---|---|---|---|
| Keadilan protokol perbandingan | 2,5% | Lipatan sama; anggaran penyetelan sebanding; data uji tak tersentuh | Adil dengan kekurangan kecil | Ada ketidaksetaraan yang memengaruhi kesimpulan | Protokol tidak sah |
| Kedalaman analisis kesalahan | 2,5% | Pola ditemukan dan dijelaskan; kaitan dengan data dibahas | Analisis dilakukan, pola dangkal | Hanya menghitung jumlah kesalahan | Tidak ada analisis kesalahan |

---

## 7. P-03 — Laporan, Notebook, dan *Model Card* (Minggu 14) — 15%

### 7.1 Tiga Luaran

| Luaran | Format | Ketentuan |
|--------|--------|-----------|
| **Laporan** | PDF, 10–15 halaman | A4, margin 2,5 cm, font 11–12 pt, spasi 1,15 |
| **Notebook** | `.ipynb` | **Wajib berjalan ulang dari sel pertama tanpa galat** |
| ***Model card*** | `.md` terpisah | Format Mitchell et al. (2019), lihat Lab 14 |

### 7.2 Struktur Laporan

| Bagian | Isi | Halaman |
|--------|-----|---------|
| Halaman judul | Judul, kelompok, anggota dan NIM, mata kuliah, tanggal | 1 |
| 1. Pendahuluan dan formulasi | Masalah, mengapa penting, formulasi *task*, metrik dan alasannya | 1,5–2 |
| 2. Data dan prapemrosesan | Sumber, kualitas, **setiap keputusan pembersihan**, `Pipeline` | 2–3 |
| 3. Metode dan protokol | Model kandidat, penyetelan, **protokol evaluasi dan bagaimana keadilannya dijaga** | 2–2,5 |
| 4. Hasil dan evaluasi | *Baseline*, tabel perbandingan dengan simpangan, grafik diagnostik | 2,5–3 |
| 5. Analisis kesalahan dan *bias* | Pola kesalahan, **audit kinerja per kelompok** | 2–2,5 |
| 6. Kesimpulan dan keterbatasan | Jawaban, **keterbatasan yang jujur**, apa yang tidak dapat dilakukan model | 1,5 |
| Referensi | Sumber data dan pustaka | 0,5 |
| Lampiran | **AI Usage Log** (wajib) | — |

### 7.3 Ketentuan Notebook

- **Berjalan ulang dari sel pertama sampai terakhir tanpa galat.**
- Versi pustaka tercatat pada sel pertama.
- `random_state` ditetapkan pada setiap proses acak.
- **Seluruh transformasi di dalam `Pipeline`.**
- Data dimuat dari tautan atau disertakan dalam pengumpulan.
- Setiap keluaran disertai kalimat interpretasi.
- Komentar kode dalam bahasa Indonesia.

### 7.4 Dokumentasi Keputusan Data

Bagian yang paling sering diabaikan dan paling sering menjadi sumber kesalahan.

| Yang wajib dicatat | Contoh |
|--------------------|--------|
| Berapa baris dibuang dan mengapa | "184 baris dibuang karena kolom target kosong (3,1% dari data)" |
| Bagaimana nilai hilang ditangani, dan **polanya** | "Kolom omzet hilang 12%, terkait dengan skala usaha (MAR); diimputasi median per kelompok di dalam `Pipeline`" |
| Pencilan: apa yang dilakukan dan mengapa | "DKI Jakarta teridentifikasi sebagai pencilan pada 3 fitur. **Dipertahankan** — data sah, bukan kesalahan pencatatan" |
| Fitur yang dibuat dan yang dibuang | "Fitur `rasio_beban_utang` dibuat; fitur `nomor_invoice` dibuang karena bocor target" |
| Strategi pembagian dan alasannya | "`GroupKFold` dengan grup `id_nasabah`, karena satu nasabah muncul di beberapa baris" |

### 7.5 Bagian Keterbatasan — Wajib dan Dinilai

Yang harus dibahas:

1. **Keterwakilan data** — kelompok mana yang kurang terwakili? Apa akibatnya?
2. **Kualitas data** — nilai hilang, kemungkinan kesalahan pencatatan, ketepatan waktu.
3. **Batas metode** — asumsi apa yang tidak sepenuhnya terpenuhi?
4. **Batas kesimpulan** — mengapa hubungan yang ditemukan **bukan** sebab-akibat?
5. **Kondisi ketika model tidak dapat diandalkan** — sebutkan secara konkret.

> Kelompok yang menulis "penelitian ini tidak memiliki keterbatasan" memperoleh nilai **nol** pada aspek ini.

### 7.6 Rubrik P-03 — 15%

**Menelusur ke `Sub-CPMK082-1` — 10%**
*Kriteria kurikulum: ketepatan problem-model; correctness training; reproduksibilitas eksperimen.*

| Aspek | Bobot | 4 | 3 | 2 | 1 |
|-------|-------|---|---|---|---|
| Ketepatan pasangan masalah–model | 3,5% | *Task* dan model tepat; alasan tertulis jelas | Tepat, alasan kurang tajam | Dapat diterima tetapi bukan optimal | Tidak sesuai |
| Kebenaran proses pelatihan | 4,0% | Tanpa kebocoran; protokol adil; penyetelan pada data latih saja | Benar dengan kekurangan kecil | Ada kekeliruan yang memengaruhi kesimpulan | Kebocoran atau protokol tidak sah |
| Reproduksibilitas | 2,5% | Notebook berjalan mulus; versi tercatat; `random_state` ditetapkan | Berjalan dengan penyesuaian kecil | Perlu perbaikan agar berjalan | Tidak dapat dijalankan |

**Menelusur ke `Sub-CPMK102-1` — 5%**
*Kriteria kurikulum: correctness preprocessing dan split; kesesuaian metrik; validitas interpretasi.*

| Aspek | Bobot | 4 | 3 | 2 | 1 |
|-------|-------|---|---|---|---|
| Kebenaran prapemrosesan dan pembagian | 2,0% | Seluruhnya di dalam `Pipeline`; strategi sesuai sifat data; keputusan didokumentasikan | Benar, dokumentasi kurang | Dilakukan tanpa penjelasan | Ada kebocoran |
| Kesesuaian metrik dan visualisasi | 1,5% | Metrik tepat beralasan; grafik diagnostik lengkap dan jujur | Tepat dan terbaca | Kurang sesuai | Menyesatkan atau tanpa label |
| Validitas interpretasi | 1,5% | Kesimpulan sebatas data; **audit *bias* dan keterbatasan jujur** | Tepat, keterbatasan kurang dibahas | Ada klaim melampaui data | Klaim sebab-akibat; keterbatasan kosong |

---

## 8. P-04 — Presentasi (Minggu 15) — 10%

Rincian susunan waktu, pertanyaan yang akan diajukan, dan rubriknya ada pada [Modul Minggu 15](../03-modules/week-15-presentasi-proyek.md).

---

## 9. Pengurangan Nilai

| Pelanggaran | Pengurangan |
|-------------|-------------|
| **Kebocoran data pada laporan akhir** | Hingga −30% nilai proyek |
| Notebook tidak dapat dijalankan ulang | −20% nilai proyek |
| Data sintetis dipakai sebagai data utama | −40% nilai proyek |
| Keputusan pembersihan tidak didokumentasikan | −15% nilai proyek |
| Bagian keterbatasan kosong atau formalitas | −15% nilai proyek |
| Tidak menyertakan *baseline* | −10% nilai proyek |
| *Model card* tanpa bagian Keterbatasan atau Etis | Dikembalikan untuk dilengkapi |
| AI Usage Log tidak ada atau tidak lengkap | Dikembalikan; dinilai sebagai terlambat |
| Terlambat mengumpulkan | Mengikuti kebijakan keterlambatan umum |

---

## 10. Catatan Penting tentang Hasil

> **Kelompok yang modelnya tidak mengungguli *baseline* TIDAK dirugikan.**
>
> Yang dinilai adalah ketepatan formulasi, kebenaran prosedur, kesesuaian metrik, dan kejujuran analisis. Melaporkan *"model terbaik kami hanya unggul 0,03 dari baseline; berikut analisis mengapa, dan berikut yang akan kami lakukan dengan data lebih banyak"* dengan prosedur yang benar bernilai **lebih tinggi** daripada melaporkan ROC-AUC 0,99 yang ternyata mengandung kebocoran.
>
> Ini bukan kelonggaran. Ini adalah inti dari apa yang hendak diajarkan mata kuliah ini: **amanah dalam melaporkan batas karya sendiri**. Seorang insinyur yang jujur tentang keterbatasan modelnya jauh lebih berharga daripada yang selalu melaporkan hasil mengesankan.

---

## 11. Daftar Periksa Sebelum Mengumpulkan P-03

### Notebook
- [ ] Berjalan ulang dari sel pertama sampai terakhir tanpa galat
- [ ] Versi pustaka tercatat; `random_state` ditetapkan
- [ ] **Seluruh transformasi di dalam `Pipeline`**
- [ ] **Data uji tidak pernah dipakai** untuk memilih atau menyetel
- [ ] Strategi pembagian sesuai sifat data
- [ ] Setiap keluaran disertai kalimat interpretasi
- [ ] Daftar periksa kebocoran (Minggu 4 §4.6) sudah dicentang seluruhnya

### Laporan
- [ ] 10–15 halaman, seluruh bagian ada
- [ ] Formulasi *task* lengkap; metrik beralasan
- [ ] Fitur yang tidak boleh dipakai disebutkan beserta alasannya
- [ ] **Skor *baseline*** dilaporkan
- [ ] Tabel perbandingan memuat **rerata dan simpangan**
- [ ] Setiap grafik punya judul, label sumbu dengan satuan, dan n
- [ ] **Analisis kesalahan** dengan pencarian pola
- [ ] **Audit kinerja per kelompok** disertakan
- [ ] Keterbatasan membahas minimal empat dari lima butir §7.5
- [ ] Sumber data lengkap dengan tautan dan tanggal akses

### *Model card*
- [ ] Seluruh tujuh bagian terisi
- [ ] Tabel kinerja **per kelompok**, bukan hanya keseluruhan
- [ ] Bagian Keterbatasan terisi jujur
- [ ] Bagian Pertimbangan Etis memuat ukuran *fairness* yang dipilih **dan alasannya**

### Integritas
- [ ] AI Usage Log lengkap dan ditandatangani seluruh anggota
- [ ] Empat baris yang wajib "dikerjakan sendiri" terisi demikian
- [ ] Pembagian peran tiap anggota dicatat

---

## 12. Sumber Data

Panduan lengkap sumber data berkonteks Indonesia ada pada [datasets/README.md](../datasets/README.md).

---

## 13. Dokumen Terkait

| Dokumen | Isi |
|---------|-----|
| [Kerangka asesmen](assessment-framework.md) | Bobot resmi dan kriteria kurikulum |
| [RTM §E](../02-rtm/rtm-dasar-kecerdasan-artifisial-pembelajaran-mesin.md) | Ringkasan tenggat tiap tahap |
| [Modul Minggu 15](../03-modules/week-15-presentasi-proyek.md) | Rincian presentasi dan pertanyaan tanya jawab |
| [Lab 14](../04-labs/lab-14-audit-bias-dan-model-card.md) | Teknik audit *bias* dan format *model card* |
| [Bab 14 buku ajar](../06-buku-ajar/bab-14-proyek-akhir.md) | Cara berpikir dalam mengerjakan proyek |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
