# Kerangka Asesmen

## Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — IF52510031

**Semester Ganjil 2026/2027 · 3 SKS · Semester 5**
**Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.
**Kurikulum Informatika 2025 — Revisi 2026**

---

## 1. Dasar Penyusunan

Seluruh bobot pada dokumen ini **diambil verbatim** dari [pemetaan MK–CPMK–Sub-CPMK kurikulum](../../../00-kurikulum-if-2025-revisi-2026/15d-subcpmk-tingkat-3-semester-5-6.md), bukan disusun ulang. Kurikulum menetapkan bahwa **bobot melekat pada Sub-CPMK**, bukan pada komponen penilaian — dan bahwa hanya enam teknik penilaian baku yang dipakai.

### 1.1 Enam Teknik Penilaian Baku

| Teknik | Wujud pada mata kuliah ini |
|--------|----------------------------|
| Partisipasi | — (berbobot 0%) |
| Kuis | 4 kuis tertulis di kelas |
| Observasi (Praktek/Tugas) | 13 praktikum |
| Unjuk Kerja (Presentasi/Proyek) | Proyek 5 tahap + presentasi |
| Tes Tulis (UTS) | Ujian Tengah Semester |
| Tes Tulis (UAS) | Ujian Akhir Semester |

---

## 2. Bobot Resmi

### 2.1 Matriks Bobot Sub-CPMK × Teknik

| Teknik | `DAIML-Sub-CPMK082-1` | `DAIML-Sub-CPMK102-1` | **Total** |
|--------|----------------------|----------------------|-----------|
| Partisipasi | 0% | 0% | **0%** |
| Kuis | 0% | 5% | **5%** |
| Observasi (Praktek/Tugas) | 15% | 10% | **25%** |
| Unjuk Kerja (Presentasi/Proyek) | 30% | 5% | **35%** |
| Tes Tulis (UTS) | 0% | 20% | **20%** |
| Tes Tulis (UAS) | 15% | 0% | **15%** |
| **Jumlah** | **60%** | **40%** | **100%** |

### 2.2 Dua Ciri Khas yang Perlu Dipahami Sejak Awal

**(a) Partisipasi berbobot 0%.**

Kehadiran tetap wajib memenuhi ketentuan universitas (minimum 75% untuk mengikuti UAS), tetapi **tidak menambah nilai**. Namun 25% nilai berasal dari Observasi atas praktikum yang dikerjakan **di dalam kelas** — sehingga ketidakhadiran tetap berbiaya, meski kehadiran tidak berpahala nilai.

**(b) Unjuk Kerja 35% adalah komponen terbesar.**

Lebih besar daripada UTS (20%) maupun UAS (15%). Proyek bukan pelengkap akhir semester, melainkan tulang punggung mata kuliah. Karena itu ia dikerjakan bertahap sejak Minggu 5, bukan menumpuk di Minggu 14.

---

## 3. Penjabaran Komponen

| Komponen | Kode | Mg | Bobot | 082-1 | 102-1 | Teknik |
|----------|------|----|-------|-------|-------|--------|
| 13 praktikum | T-01…T-14 | 1–14 | 25% | 15% | 10% | Observasi |
| Kuis 1 — data dan kebocoran | K-01 | 4 | 1,25% | — | 1,25% | Kuis |
| Kuis 2 — metrik klasifikasi | K-02 | 7 | 1,25% | — | 1,25% | Kuis |
| Kuis 3 — pemilihan model | K-03 | 10 | 1,25% | — | 1,25% | Kuis |
| Kuis 4 — JST dan evaluasi | K-04 | 13 | 1,25% | — | 1,25% | Kuis |
| Proposal proyek | P-00 | 5 | prasyarat | — | — | — |
| Milestone 1 — *baseline* | P-01 | 7 | 5% | 5% | — | Unjuk Kerja |
| Milestone 2 — iterasi | P-02 | 11 | 5% | 5% | — | Unjuk Kerja |
| Laporan + notebook + *model card* | P-03 | 14 | 15% | 10% | 5% | Unjuk Kerja |
| Presentasi dan tanya jawab | P-04 | 15 | 10% | 10% | — | Unjuk Kerja |
| Ujian Tengah Semester | U-01 | 8 | 20% | — | 20% | Tes Tulis |
| Ujian Akhir Semester | U-02 | 16 | 15% | 15% | — | Tes Tulis |
| | | | **100%** | **60%** | **40%** | |

> Bobot Observasi 25% dibagi sesuai bobot registri per Sub-CPMK: 15% untuk 8 lab `082-1` (masing-masing **1,875%**) dan 10% untuk 5 lab `102-1` (masing-masing **2,0%**).

---

## 4. Kriteria Penilaian Menurut Kurikulum

Kurikulum menetapkan kriteria untuk tiap Sub-CPMK. Seluruh rubrik pada mata kuliah ini diturunkan darinya.

### 4.1 `DAIML-Sub-CPMK082-1`

> **Kriteria kurikulum:** ketepatan problem-model; *correctness training*; reproduksibilitas eksperimen.

| Kriteria | Cara mengukurnya |
|----------|------------------|
| **Ketepatan pasangan masalah–model** | Apakah jenis *task* dan model sesuai dengan sifat masalah dan data? Apakah alasannya tertulis? |
| **Kebenaran proses pelatihan** | Apakah pembagian data benar? Apakah penyetelan dilakukan pada data latih saja? Apakah bebas kebocoran? |
| **Reproduksibilitas eksperimen** | Apakah notebook berjalan ulang tanpa galat? Apakah `random_state` ditetapkan? Apakah versi pustaka tercatat? |

### 4.2 `DAIML-Sub-CPMK102-1`

> **Kriteria kurikulum:** *correctness preprocessing* dan *split*; kesesuaian metrik; validitas interpretasi.

| Kriteria | Cara mengukurnya |
|----------|------------------|
| **Kebenaran prapemrosesan dan pembagian** | Apakah seluruh transformasi di dalam `Pipeline`? Apakah strategi pembagian sesuai sifat data? |
| **Kesesuaian metrik** | Apakah metrik sesuai jenis masalah dan dampak kesalahan? Apakah alasannya tertulis? |
| **Validitas interpretasi** | Apakah kesimpulan sebatas yang didukung data? Apakah keterbatasan dinyatakan? |

---

## 5. Rubrik Umum

Penilaian berbasis rubrik — praktikum (§5.1), proyek (§5.3), dan presentasi — memakai skala 1–4, dikonversi dengan:

$$\text{Nilai aspek} = \frac{\text{skor}}{4} \times \text{bobot aspek}$$

**Pengecualian:** kuis **tidak** memakai skala 1–4, melainkan porsi **40/60** (jawaban 40%, alasan 60%; §5.2); ujian tulis dinilai per butir dengan pedoman skor (§5.4 dan kaidah penilaian pada kisi-kisi). Pengurangan nilai di luar rubrik hanya yang tercantum pada §7.

### 5.1 Rubrik Praktikum (Observasi, 25%)

| Aspek | Bobot | 4 (Sangat Baik) | 3 (Baik) | 2 (Cukup) | 1 (Kurang) |
|-------|-------|-----------------|----------|-----------|------------|
| Kebenaran teknis | 40% | Seluruh langkah benar; tanpa kebocoran | Benar dengan kekeliruan kecil | Ada kekeliruan yang memengaruhi hasil | Langkah pokok salah atau ada kebocoran |
| Kesesuaian metode/metrik | 25% | Tepat dan beralasan tertulis | Tepat, alasan kurang | Dapat diterima tetapi bukan yang optimal | Tidak sesuai |
| Kualitas interpretasi | 25% | Tajam, sebatas data, menyebut keterbatasan | Tepat, keterbatasan kurang dibahas | Ada klaim melampaui data | Tidak ada interpretasi |
| Reproduksibilitas | 10% | Berjalan ulang mulus; versi tercatat; `random_state` ditetapkan | Berjalan dengan penyesuaian kecil | Perlu perbaikan agar berjalan | Tidak dapat dijalankan |

### 5.2 Rubrik Kuis (5%)

Kuis dinilai dengan kunci jawaban. Setiap soal menuntut **alasan**, bukan hanya jawaban akhir:

| Unsur | Porsi |
|-------|-------|
| Jawaban benar | 40% |
| Alasan/penalaran tertulis | 60% |

> Jawaban benar tanpa alasan memperoleh nilai sebagian. Jawaban keliru dengan penalaran yang tepat tetap memperoleh nilai sebagian.

### 5.3 Rubrik Proyek

Rincian ada pada [panduan proyek](project-guidelines.md) §5–§8 (rubrik P-04 pada [Modul Minggu 15](../03-modules/week-15-presentasi-proyek.md)). Ringkasannya:

| Tahap | Bobot | Aspek utama |
|-------|-------|-------------|
| P-01 *Baseline* | 5% | Kebenaran pembagian · Kesesuaian metrik · Kejujuran pelaporan |
| P-02 Iterasi | 5% | Keadilan protokol · Kedalaman analisis kesalahan |
| P-03 Laporan | 15% | Kebenaran teknis · Reproduksibilitas · Evaluasi · Interpretasi |
| P-04 Presentasi | 10% | Ketepatan formulasi · Kebenaran metode · Kedalaman analisis · Penyajian · Penguasaan |

### 5.4 Rubrik Ujian Tulis

| Bagian | UTS | UAS | Penilaian |
|--------|-----|-----|-----------|
| Konsep | 30% | 25% | Ketepatan dan kelengkapan penjelasan |
| Analisis/Perancangan | 40% | 45% | Ketepatan penalaran; kelengkapan pertimbangan |
| Perhitungan | 30% | 30% | Kebenaran langkah **dan** hasil; langkah yang benar dengan hasil salah tetap bernilai sebagian |

---

## 6. Konversi Nilai

Skala mengikuti [registri konversi nilai](../../../00-pedoman-obe/konversi-nilai.md) — satu-satunya sumber skala di repositori ini.

| Rentang Nilai Akhir | Huruf | Bobot | Kategori |
|---------------------|-------|-------|----------|
| 81,00 – 100,00 | A | 4,00 | Sangat Baik |
| 78,00 – 80,99 | A− | 3,70 | Sangat Baik |
| 75,00 – 77,99 | B+ | 3,30 | Baik |
| 70,00 – 74,99 | B | 3,00 | Baik |
| 65,00 – 69,99 | B− | 2,70 | Baik |
| 60,00 – 64,99 | C+ | 2,30 | Cukup |
| 55,00 – 59,99 | C | 2,00 | Cukup |
| 40,00 – 54,99 | D | 1,00 | Kurang |
| 0,00 – 39,99 | E | 0,00 | Sangat Kurang |

### 6.1 Syarat Kelulusan

Mahasiswa dinyatakan lulus apabila memenuhi **seluruh** syarat:

1. Nilai akhir ≥ 55,00.
2. **Capaian tiap Sub-CPMK ≥ 50%** dari bobotnya:
   - `Sub-CPMK082-1`: ≥ 30 dari 60
   - `Sub-CPMK102-1`: ≥ 20 dari 40
3. Mengumpulkan proyek akhir dan mengikuti presentasi.
4. Kehadiran memenuhi ketentuan universitas.

> Syarat kedua penting: mahasiswa yang sangat unggul dalam membangun model tetapi tidak mampu menyiapkan data dan mengevaluasinya **tidak dinyatakan lulus**, karena keduanya adalah capaian yang berbeda dan keduanya dituntut kurikulum.

---

## 7. Pengurangan Nilai

> **Tabel acuan tunggal.** Tabel §7.1 adalah **satu-satunya** daftar pengurangan nilai dan sanksi pada mata kuliah ini. [RPS §K](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md), [RTM](../02-rtm/rtm-dasar-kecerdasan-artifisial-pembelajaran-mesin.md), [rubrik tugas](rubrik-tugas.md), dan [panduan proyek](project-guidelines.md) merujuk ke sini dan tidak memuat versi lain. Bila ada dokumen yang berbeda, tabel ini yang berlaku.

### 7.1 Tabel Pengurangan

| Temuan | Berlaku pada | Konsekuensi |
|--------|--------------|-------------|
| Notebook tidak dapat dijalankan ulang dari sel pertama | Lab; P-01, P-02, P-03 | −20% dari komponen bersangkutan |
| Kebocoran data (§7.2 butir c) | Lab | Dikembalikan; dinilai sebagai terlambat |
| Kebocoran data | Milestone P-01, P-02 | Dinilai menurut rubrik tahap itu; **wajib diperbaiki sebelum tahap berikutnya** (tanpa pengurangan tambahan) |
| **Kebocoran data pada laporan akhir** | P-03 | Hingga −30% nilai proyek, sebanding dengan seberapa jauh kesimpulan terpengaruh |
| Melaporkan akurasi saja pada data tak seimbang | Lab; P-01, P-02, P-03 | −10% dari komponen bersangkutan |
| Tidak menyertakan *baseline* | Lab; P-01, P-02, P-03 | −10% dari komponen bersangkutan |
| Data sintetis dipakai sebagai **data utama** proyek | Proyek | −40% nilai proyek |
| Proposal P-00 belum disetujui | Proyek | Tahap berikutnya tidak dinilai sampai proposal disetujui |
| AI Usage Log tidak ada atau tidak lengkap | Lab; seluruh tahap proyek | Dikembalikan; dinilai sebagai terlambat |
| Log mencantumkan AI pada kegiatan yang **tidak boleh** (butir L1–L5, §8) | Lab; seluruh tahap proyek | Dikembalikan; bagian itu dikerjakan ulang sendiri; dinilai sebagai terlambat |
| Memakai AI tanpa mencatatnya, atau memakai AI saat kuis/ujian (L6) | Semua | **Pelanggaran integritas akademik** — diproses menurut ketentuan integritas akademik universitas, bukan sekadar pengurangan nilai |
| Bagian Keterbatasan kosong atau hanya menyatakan "tidak ada keterbatasan" — pada laporan **atau** *model card* — atau *model card* tanpa bagian Etis | P-03 | Dikembalikan untuk dilengkapi |
| Kontribusi seorang anggota jauh di bawah rekan sekelompoknya | P-01–P-04 | Nilai perorangan disesuaikan dengan faktor kontribusi — [panduan proyek §10](project-guidelines.md#10-kontribusi-anggota-kelompok-dan-nilai-perorangan) |
| Keterlambatan ≤ 24 jam | Lab; seluruh tahap proyek | −10% |
| Keterlambatan > 24 jam s.d. 72 jam | Lab; seluruh tahap proyek | −25% |
| Keterlambatan > 72 jam | Lab; seluruh tahap proyek | Tidak dinilai (nilai 0) |

### 7.2 Cara Menerapkan

a. **Satu temuan, satu konsekuensi.** Setiap temuan dikenai satu baris tabel saja per komponen. **Tanpa sanksi ganda.** Bila satu temuan dikenai pengurangan persentase dari tabel pengurangan, aspek rubrik yang deskriptornya menyebut temuan yang sama dinilai tanpa memperhitungkan temuan itu — mis. notebook yang tidak berjalan ulang dikenai −20%, dan skor Reproduksibilitasnya tidak memperhitungkan kegagalan berjalan ulang itu. Contoh lain: P-01 tanpa *baseline* dikenai −10%, dan aspek Kejujuran pelaporan dinilai dari unsur lainnya (pemeriksaan kebocoran yang ditunjukkan); kebocoran pada P-03 dikenai pengurangan hingga −30% nilai proyek, dan aspek P-03 yang deskriptornya menyebut kebocoran (Kebenaran proses pelatihan; Kebenaran prapemrosesan dan pembagian) dinilai tanpa memperhitungkan kebocoran itu. Sebaliknya, bila baris tabel **bukan** pengurangan persentase — kebocoran pada P-01/P-02 ("dinilai menurut rubrik"), atau pekerjaan "dikembalikan" yang tidak dikumpulkan ulang (butir d) — skor rubrik itulah satu-satunya konsekuensinya. Jadi kebocoran memakai prinsip yang sama di setiap tahap: rubrik **atau** pengurangan, tidak keduanya. Temuan itu **tidak membatasi skor aspek lain** — ketentuan lama "skor maksimum 2 pada Kebenaran teknis" di rubrik tugas tidak berlaku lagi. Hal yang diukur rubrik tetapi **tidak tercantum** pada tabel §7.1 (mis. dokumentasi keputusan data, [panduan proyek §7.4](project-guidelines.md#74-dokumentasi-keputusan-data)) hanya dinilai lewat rubrik, tanpa pengurangan tambahan.

b. **Cara menghitung.** Persentase pengurangan dihitung terhadap nilai maksimum komponen (skala 0–100) lalu dikurangkan dari skor rubrik: $\text{nilai komponen} = \max(0;\ \text{skor rubrik} - \sum \text{pengurangan})$. "Komponen bersangkutan" = satu lab atau satu tahap proyek. "Nilai proyek" = gabungan P-01–P-04 (bobot 35%). Contoh: lab dengan skor rubrik 80 yang terlambat ≤ 24 jam bernilai 80 − 10 = 70.

c. **Yang termasuk kebocoran:** transformasi yang di-*fit* pada data lengkap sebelum pembagian (di luar `Pipeline`), fitur yang baru tersedia setelah saat prediksi, data uji yang dipakai untuk memilih atau menyetel, dan pembagian yang mengabaikan waktu atau kelompok. Transformasi di luar `Pipeline` yang **tidak** menimbulkan kebocoran dinilai melalui aspek Kebenaran teknis, tanpa pengurangan.

d. **"Dikembalikan"** berarti pekerjaan diperbaiki dan dikumpulkan ulang paling lambat **3 hari** setelah dikembalikan. **"Dinilai sebagai terlambat"** berarti versi perbaikan dikenai pengurangan keterlambatan ≤ 24 jam (−10%). Bila tidak dikumpulkan ulang dalam 3 hari: temuan kebocoran dan bagian Keterbatasan/Etis dinilai apa adanya menurut rubrik; AI Usage Log yang tetap tidak ada, atau bagian terlarang yang tidak dikerjakan ulang, membuat pekerjaan tidak dinilai.

e. **Keterlambatan** dapat dikecualikan bila alasannya dapat diterima dan disampaikan **sebelum** tenggat. Kuis dan ujian dikerjakan di kelas, sehingga baris keterlambatan tidak berlaku padanya.

f. **Yang tidak dikenai pengurangan:** model berkinerja rendah, model yang tidak mengungguli *baseline*, dan fitur yang ternyata tidak membantu (§9).

---

## 8. Kebijakan Alat Bantu AI

Mata kuliah ini berstatus **mode Core** pada AI Curriculum Infusion Matrix. Pembatasannya lebih rinci daripada mata kuliah lain justru karena AI adalah objek yang dipelajari.

| Kegiatan | Status | Alasan |
|----------|--------|--------|
| Menulis kode `scikit-learn` rutin | Boleh, wajib dicatat | Bukan yang dinilai |
| Memperbaiki galat; menjelaskan dokumentasi | Boleh | Bukan yang dinilai |
| Menyarankan jenis visualisasi | Boleh | Bukan yang dinilai |
| Menyunting bahasa laporan | Boleh | Bukan yang dinilai |
| **L1. Memformulasikan masalah menjadi *task* ML** | **Tidak boleh** | Inti `Sub-CPMK082-1` |
| **L2. Memilih model dan hiperparameter** | **Tidak boleh** | Inti `Sub-CPMK082-1` |
| **L3. Memilih dan menafsirkan metrik** | **Tidak boleh** | Inti `Sub-CPMK102-1` |
| **L4. Menganalisis kesalahan model** | **Tidak boleh** | Inti kedua Sub-CPMK |
| **L5. Menulis *model card* dan analisis keterbatasan** | **Tidak boleh** | Inti `Sub-CPMK102-1` |
| **L6. Selama kuis, UTS, dan UAS** | **Tidak boleh sama sekali** | Kuis dan ujian *closed book* |

Butir L1–L6 adalah **daftar larangan AI yang sama** dengan [RPS §K.1](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md); RTM §I dan [rubrik tugas §6](rubrik-tugas.md) memakai daftar ini. Konsekuensi pelanggarannya ada pada §7.1.

**AI Usage Log wajib** pada setiap praktikum dan setiap tahap proyek. Formatnya ada pada [RTM §I](../02-rtm/rtm-dasar-kecerdasan-artifisial-pembelajaran-mesin.md).

> Mencatat pemakaian AI **tidak mengurangi nilai**. Tidak mencatatnya, padahal memakainya, adalah pelanggaran integritas akademik.

---

## 9. Catatan tentang Hasil

> **Model yang tidak mengungguli *baseline* tidak merugikan nilai.**
>
> Yang dinilai adalah ketepatan formulasi, kebenaran prosedur, kesesuaian metrik, dan kejujuran interpretasi. Laporan yang menyatakan *"model kami hanya sedikit mengungguli baseline; berikut analisis mengapa"* dengan prosedur yang benar bernilai **lebih tinggi** daripada laporan berakurasi 0,99 yang mengandung kebocoran.
>
> Ini bukan kelonggaran, melainkan penegasan atas apa yang sesungguhnya diukur mata kuliah ini.

---

## 10. Peta Asesmen terhadap Minggu

| Mg | Observasi | Kuis | Unjuk Kerja | Tes Tulis |
|----|-----------|------|-------------|-----------|
| 1 | T-01 | | | |
| 2 | T-02 | | | |
| 3 | T-03 | | | |
| 4 | T-04 | **K-01** | | |
| 5 | T-05 | | P-00 (prasyarat) | |
| 6 | T-06 | | | |
| 7 | T-07 | **K-02** | **P-01** | |
| 8 | | | | **U-01 UTS** |
| 9 | T-09 | | | |
| 10 | T-10 | **K-03** | | |
| 11 | T-11 | | **P-02** | |
| 12 | T-12 | | | |
| 13 | T-13 | **K-04** | | |
| 14 | T-14 | | **P-03** | |
| 15 | | | **P-04** | |
| 16 | | | | **U-02 UAS** |

---

## 11. Dokumen Terkait

| Dokumen | Isi |
|---------|-----|
| [RPS](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md) | Rencana pembelajaran lengkap |
| [RTM](../02-rtm/rtm-dasar-kecerdasan-artifisial-pembelajaran-mesin.md) | Rincian setiap tugas |
| [Kisi-kisi UTS](kisi-kisi-uts.md) | Cakupan dan contoh soal UTS |
| [Kisi-kisi UAS](kisi-kisi-uas.md) | Cakupan dan contoh soal UAS |
| [Panduan Proyek](project-guidelines.md) | Ketentuan lengkap proyek |
| [Rubrik Tugas](rubrik-tugas.md) | Rubrik rinci tiap praktikum |
| [Registri kurikulum](../../../00-kurikulum-if-2025-revisi-2026/README.md) | Sumber seluruh bobot dan kriteria |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
