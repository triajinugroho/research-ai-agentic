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

> **Mengapa praktikum memakai data sintetis, tetapi proyek wajib data nyata?** Sebagian besar lab memakai **data sintetis (simulasi) yang meniru pola Indonesia** — dinyatakan pada bagian Persiapan setiap lab. Itu disengaja: karena aturan pembangkitnya diketahui, dampak setiap konsep (kebocoran, regularisasi, *bias*) dapat **diukur terhadap "kebenaran"-nya**, bukan sekadar diduga. Proyek menilai hal yang tidak dapat dilatih dengan data sintetis: menelusuri sumber dan definisi variabel, menghadapi data yang berantakan tanpa kunci jawaban, dan menyatakan keterwakilan serta keterbatasan data yang sesungguhnya. Karena itu data sintetis sebagai data utama proyek dikenai pengurangan ([kerangka asesmen §7](assessment-framework.md#7-pengurangan-nilai)). Panduan sumber data: [datasets/README.md](../datasets/README.md).

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
>
> Dua hal berjalan sepanjang tahap: *model card* diisi bertahap sejak P-00 dengan templat Lampiran H (§7.7), dan setiap anggota mengisi Formulir Kontribusi A (Minggu 11) dan B (Minggu 15) (§10).

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
7. **Dampak bila model salah** — siapa yang dirugikan oleh masing-masing jenis kesalahan. Kelompok orang yang disebut di sini menjadi calon **kelompok audit *bias*** pada *model card* (§7.7).
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
| 3 | Tabel perbandingan dengan **rerata dan simpangan baku sampel antarlipatan** (`ddof=1`, yaitu `np.std(x, ddof=1)` atau `pd.Series.std()`); dua model teratas dibandingkan dengan **selisih berpasangan per lipatan** — $\bar d$, $s_d$, $SE = s_d/\sqrt{k}$; selisih dianggap bermakna bila $\lvert\bar d\rvert > 2\cdot SE$ dan arahnya konsisten di sebagian besar lipatan ([Lab 10](../04-labs/lab-10-svm-naive-bayes-penyetelan.md)) |
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
| ***Model card*** | `.md` terpisah | Format Mitchell et al. (2019) dengan [templat Lampiran H](../06-buku-ajar/lampiran.md#lampiran-h-templat-model-card); **diisi bertahap sejak P-00** (§7.7) |

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

> Bagian Keterbatasan yang kosong, atau hanya menyatakan "penelitian ini tidak memiliki keterbatasan", **dikembalikan untuk dilengkapi** — satu-satunya konsekuensinya, menurut [kerangka asesmen §7](assessment-framework.md#7-pengurangan-nilai). Setelah dilengkapi, mutunya dinilai pada aspek **Validitas interpretasi** (§7.6).

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

> Dokumentasi keputusan data (§7.4) dinilai pada aspek **Kebenaran prapemrosesan dan pembagian** (skor 2 = "dilakukan tanpa penjelasan"); tidak ada pengurangan tambahan untuk hal yang sama.

### 7.7 *Model Card* dan Audit *Bias*: Mulai Sejak Awal

P-03 (Minggu 14) menuntut *model card* dan audit *bias*, sedangkan Lab 14 — yang melatih teknik audit — berlangsung pada minggu yang sama. Agar kelompok tidak menunggu Lab 14, *model card* disusun **bertahap sejak awal proyek** dengan [templat Lampiran H](../06-buku-ajar/lampiran.md#lampiran-h-templat-model-card). Bahan yang dapat dibaca lebih awal: [Bab 13 §13.3](../06-buku-ajar/bab-13-ai-generatif-dan-ai-bertanggung-jawab.md#133-mengukur-fairness) (mengukur *fairness*) dan Lampiran A.9 (ukuran *fairness*).

| Tahap | Bagian templat Lampiran H yang diisi (disarankan) |
|-------|----------------------------------------------------|
| P-00 (Mg 5) | Bagian 2 (Penggunaan yang dimaksudkan); **kelompok yang akan diaudit** ditetapkan dari butir 7 proposal |
| P-01 (Mg 7) | Bagian 1 (Rincian model) dan Bagian 3 (Data: sumber, periode, cakupan kelompok, yang tidak tercakup) |
| P-02 (Mg 11) | Bagian 4 (Kinerja) versi awal: kinerja model kandidat **per kelompok**, sebagai bagian analisis kesalahan |
| P-03 (Mg 14) | Bagian 5–7, dan seluruh tabel diperbarui untuk model akhir |

**Penyempurnaan audit *bias* dengan hasil Lab 14.** Tenggat P-03 **tidak berubah**: laporan, notebook, dan *model card* lengkap — termasuk audit *bias* versi awal — tetap dikumpulkan pada Minggu 14. Setelah Lab 14, kelompok **boleh** menyempurnakan bagian audit *bias* (laporan bagian 5 serta *model card* Bagian 4–6) dalam sebuah **adendum** (maksimal 2 halaman, ditambah sel notebook yang berjalan ulang), dikumpulkan bersama slide P-04 (§8.1). Aspek **Validitas interpretasi** (§7.6) dinilai dari versi yang lebih baik antara P-03 dan adendum; aspek lain tetap dinilai dari P-03. Adendum bersifat pilihan dan tidak dikenai pengurangan keterlambatan.

---

## 8. P-04 — Presentasi (Minggu 15) — 10%

Rincian susunan waktu, pertanyaan yang akan diajukan, dan rubriknya ada pada [Modul Minggu 15](../03-modules/week-15-presentasi-proyek.md).

### 8.1 Kapasitas dan Sesi Presentasi Tambahan

Satu pertemuan Minggu 15 (150 menit) memuat **5 kelompok**: 10 menit pengantar, lalu 28 menit per kelompok (20 menit presentasi + 8 menit tanya jawab). Bila jumlah kelompok dalam satu kelas lebih dari 5, berlaku ketentuan berikut:

| Aspek | Ketentuan |
|-------|-----------|
| Jumlah sesi | ⌈jumlah kelompok ÷ 5⌉; sesi pertama pada pertemuan reguler Minggu 15, sesi tambahan **dalam Minggu 15** di luar jam kuliah reguler |
| Jadwal dan urutan | Diundi dan diumumkan paling lambat **Minggu 13**; urutan tidak dipilih kelompok |
| Pengumpulan slide | **Seluruh kelompok** mengumpulkan slide (dan adendum audit *bias*, bila ada) sebelum sesi **pertama** dimulai, sehingga kelompok yang tampil belakangan tidak memperoleh waktu persiapan tambahan |
| Kesetaraan | Durasi, rubrik, dan penguji sama di semua sesi; pertanyaan diambil dari daftar yang sama pada Modul Minggu 15 |
| Kehadiran | Setiap mahasiswa wajib hadir pada sesi kelompoknya; penilaian sejawat atas dua kelompok lain diambil dari sesi yang sama |
| Tenggat lain | Tidak berubah |

---

## 9. Pengurangan Nilai

Seluruh pengurangan nilai proyek — kebocoran, notebook yang tidak berjalan ulang, *baseline* yang tidak ada, data sintetis sebagai data utama, bagian Keterbatasan atau Etis yang kosong, AI Usage Log, dan keterlambatan — mengikuti **satu tabel acuan** pada [kerangka asesmen §7](assessment-framework.md#7-pengurangan-nilai). Tabel itu tidak ditulis ulang di sini agar tidak ada dua versi. Prinsipnya: satu temuan dikenai satu baris tabel saja; hal yang sudah diukur rubrik (mis. dokumentasi keputusan data) tidak dikenai pengurangan tambahan.

---

## 10. Kontribusi Anggota Kelompok dan Nilai Perorangan

[RPS §K.5](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md) menetapkan bahwa ketimpangan kontribusi yang nyata memengaruhi nilai perorangan. Bagian ini menetapkan caranya.

### 10.1 Formulir Kontribusi

Formulir diisi **setiap anggota secara terpisah dan rahasia**, dikumpulkan langsung kepada dosen melalui LMS (tidak dibagikan ke kelompok).

| Formulir | Dikumpulkan | Mencakup | Dipakai untuk |
|----------|-------------|----------|---------------|
| A | Bersama P-02 (Minggu 11) | P-00 s.d. P-02 | Faktor kontribusi P-01 dan P-02; **peringatan dini** |
| B | Paling lambat akhir Minggu 15, setelah presentasi | P-03 dan P-04 | Faktor kontribusi P-03 dan P-04 |

```markdown
## Formulir Kontribusi Anggota — Proyek IF52510031
Kelompok: ________   Formulir: A (P-00–P-02) / B (P-03–P-04)
Pengisi: Nama ____________________  NIM __________

### Bagian 1 — Pekerjaan saya
| Bagian yang saya kerjakan | Bukti (commit GitHub, sel notebook, bagian laporan/slide) |
|---------------------------|------------------------------------------------------------|
|                           |                                                            |

### Bagian 2 — Poin kontribusi anggota LAIN
Bagikan tepat 100 poin kepada anggota lain (bukan diri sendiri) menurut besar
kontribusi nyata mereka pada tahap yang dicakup. Bila setara, bagi rata.

| Anggota lain (Nama, NIM) | Poin | Bagian yang dikerjakan | Alasan* |
|--------------------------|------|------------------------|---------|
|                          |      |                        |         |
| **Jumlah**               | 100  |                        |         |

*Wajib diisi bila poin kurang dari 85% bagian rata
 (≤ 42 poin pada kelompok 3 orang; ≤ 28 poin pada kelompok 4 orang).

**Pernyataan:** Saya mengisi formulir ini dengan jujur dan dapat
mempertanggungjawabkannya (amanah).

Tanda tangan: ____________   Tanggal: __________
```

### 10.2 Rumus Penyesuaian

Untuk kelompok beranggotakan $n$ orang, setiap anggota membagikan 100 poin kepada $n-1$ anggota lain, sehingga **bagian rata** $= 100/(n-1)$. Untuk anggota $j$:

$$\bar P_j = \frac{1}{n-1}\sum_{i \neq j} p_{i \to j} \qquad f_j = \frac{\bar P_j}{100/(n-1)} \qquad FK_j = \min\left(1;\ \frac{f_j}{0{,}85}\right)$$

$$\text{Nilai perorangan tahap} = \text{nilai kelompok tahap} \times FK_j$$

| Keadaan | Akibat |
|---------|--------|
| $f_j \ge 0{,}85$ | $FK_j = 1$: nilai perorangan = nilai kelompok. Variasi wajar tidak mengubah nilai, dan **tidak ada tambahan** di atas nilai kelompok |
| $f_j < 0{,}85$ | Nilai perorangan turun sebanding; $f_j = 0$ berarti nilai tahap itu 0 |
| Anggota tidak mengumpulkan formulir | Poinnya dianggap dibagi rata kepada anggota lain |

Faktor $FK_j$ dikalikan pada nilai tahap secara utuh, sehingga porsi `Sub-CPMK082-1` dan `Sub-CPMK102-1` pada tahap itu (mis. P-03: 10% dan 5%) ikut tersesuaikan dalam perbandingan yang sama.

### 10.3 Verifikasi dan Klarifikasi

1. $FK_j < 1$ **tidak diterapkan otomatis.** Dosen memeriksa bukti: pembagian peran pada P-00, riwayat *commit*, AI Usage Log yang ditandatangani, dan — untuk Formulir B — jawaban anggota itu saat tanya jawab P-04.
2. Anggota yang bersangkutan diberi kesempatan **klarifikasi** sebelum nilai ditetapkan.
3. Bila bukti tidak mendukung penilaian rekan (mis. indikasi kesepakatan untuk menjatuhkan seorang anggota), dosen menetapkan faktor berdasarkan bukti, dengan alasan tertulis.
4. Formulir A juga berfungsi sebagai **peringatan dini**: bila ada anggota dengan $f_j < 0{,}85$, kelompok dipanggil pada Minggu 12 untuk menata ulang pembagian kerja sebelum P-03.
5. Formulir yang terisi dan nilai perorangan **tidak** diunggah ke repositori ini (repositori publik); keduanya disimpan di LMS.

### 10.4 Contoh Perhitungan

Kelompok 4 orang (bagian rata = 100/3 ≈ 33,3 poin). Poin pada Formulir B (baris = pemberi, kolom = penerima):

| Pemberi → | A | B | C | D |
|-----------|---|---|---|---|
| A | — | 40 | 40 | 20 |
| B | 40 | — | 40 | 20 |
| C | 40 | 40 | — | 20 |
| D | 33 | 33 | 34 | — |

| Anggota | $\bar P_j$ | $f_j$ | $FK_j$ | Nilai P-03 kelompok | Nilai P-03 perorangan | Sumbangan ke nilai akhir (× 15%) |
|---------|-----------|-------|--------|---------------------|-----------------------|----------------------------------|
| A | 37,67 | 1,13 | 1 | 80 | 80,00 | 12,00 |
| B | 37,67 | 1,13 | 1 | 80 | 80,00 | 12,00 |
| C | 38,00 | 1,14 | 1 | 80 | 80,00 | 12,00 |
| D | 20,00 | 0,60 | 0,706 | 80 | 56,47 | 8,47 |

Hanya D yang tersesuaikan — setelah diverifikasi menurut §10.3. Perhitungan yang sama dalam Python:

```python
# Menghitung faktor kontribusi dari Formulir Kontribusi (contoh §10.4)
import numpy as np
import pandas as pd

def faktor_kontribusi(poin: pd.DataFrame, nilai_kelompok: float,
                      ambang: float = 0.85) -> pd.DataFrame:
    """poin: baris = pemberi, kolom = penerima; diagonal NaN (tidak menilai diri sendiri)."""
    n = len(poin)
    # Setiap pemberi wajib membagikan tepat 100 poin kepada anggota lain
    assert np.allclose(poin.sum(axis=1), 100), "Setiap baris harus berjumlah 100 poin"
    bagian_rata = 100 / (n - 1)
    rerata_diterima = poin.mean(axis=0)          # rerata poin per penerima (NaN dilewati)
    f = rerata_diterima / bagian_rata            # 1 = kontribusi setara
    fk = (f / ambang).clip(upper=1.0)            # tidak ada tambahan di atas nilai kelompok
    return pd.DataFrame({"P_rerata": rerata_diterima.round(2),
                         "f": f.round(2),
                         "FK": fk.round(3),
                         "nilai_perorangan": (nilai_kelompok * fk).round(2)})

anggota = ["A", "B", "C", "D"]
poin = pd.DataFrame([[np.nan, 40, 40, 20],
                     [40, np.nan, 40, 20],
                     [40, 40, np.nan, 20],
                     [33, 33, 34, np.nan]], index=anggota, columns=anggota)

hasil = faktor_kontribusi(poin, nilai_kelompok=80)
hasil["sumbangan_akhir"] = (hasil["nilai_perorangan"] * 0.15).round(2)   # bobot P-03 = 15%
print(hasil)
```

---

## 11. Catatan Penting tentang Hasil

> **Kelompok yang modelnya tidak mengungguli *baseline* TIDAK dirugikan.**
>
> Yang dinilai adalah ketepatan formulasi, kebenaran prosedur, kesesuaian metrik, dan kejujuran analisis. Melaporkan *"model terbaik kami hanya unggul 0,03 dari baseline; berikut analisis mengapa, dan berikut yang akan kami lakukan dengan data lebih banyak"* dengan prosedur yang benar bernilai **lebih tinggi** daripada melaporkan ROC-AUC 0,99 yang ternyata mengandung kebocoran.
>
> Ini bukan kelonggaran. Ini adalah inti dari apa yang hendak diajarkan mata kuliah ini: **amanah dalam melaporkan batas karya sendiri**. Seorang insinyur yang jujur tentang keterbatasan modelnya jauh lebih berharga daripada yang selalu melaporkan hasil mengesankan.

---

## 12. Daftar Periksa Sebelum Mengumpulkan P-03

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
- [ ] Tabel perbandingan memuat **rerata dan simpangan baku sampel** (`ddof=1`); dua model teratas dibandingkan dengan selisih berpasangan per lipatan
- [ ] Setiap grafik punya judul, label sumbu dengan satuan, dan n
- [ ] **Analisis kesalahan** dengan pencarian pola
- [ ] **Audit kinerja per kelompok** disertakan
- [ ] Keterbatasan membahas minimal empat dari lima butir §7.5
- [ ] Sumber data lengkap dengan tautan dan tanggal akses

### *Model card*
- [ ] Disusun dengan templat [Lampiran H](../06-buku-ajar/lampiran.md#lampiran-h-templat-model-card); seluruh tujuh bagian terisi
- [ ] Tabel kinerja **per kelompok**, bukan hanya keseluruhan
- [ ] Bagian Keterbatasan terisi jujur
- [ ] Bagian Pertimbangan Etis memuat ukuran *fairness* yang dipilih **dan alasannya**

### Integritas
- [ ] AI Usage Log lengkap dan ditandatangani seluruh anggota
- [ ] Lima butir L1–L5 (daftar larangan AI, [RPS §K.1](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md)) terisi "dikerjakan sendiri"
- [ ] Pembagian peran tiap anggota dicatat
- [ ] Setiap anggota tahu tenggat Formulir Kontribusi B (akhir Minggu 15, §10.1)

---

## 13. Sumber Data

Panduan lengkap sumber data berkonteks Indonesia ada pada [datasets/README.md](../datasets/README.md).

---

## 14. Dokumen Terkait

| Dokumen | Isi |
|---------|-----|
| [Kerangka asesmen](assessment-framework.md) | Bobot resmi, kriteria kurikulum, dan **tabel acuan pengurangan nilai (§7)** |
| [RTM §E](../02-rtm/rtm-dasar-kecerdasan-artifisial-pembelajaran-mesin.md) | Ringkasan tenggat tiap tahap |
| [Modul Minggu 15](../03-modules/week-15-presentasi-proyek.md) | Rincian presentasi dan pertanyaan tanya jawab |
| [Lab 14](../04-labs/lab-14-audit-bias-dan-model-card.md) | Teknik audit *bias* dan format *model card* |
| [Lampiran H buku ajar](../06-buku-ajar/lampiran.md#lampiran-h-templat-model-card) | Templat *model card* yang diisi sejak awal proyek |
| [Bab 14 buku ajar](../06-buku-ajar/bab-14-proyek-akhir.md) | Cara berpikir dalam mengerjakan proyek |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
