# RENCANA TUGAS MAHASISWA (RTM)

## UNIVERSITAS AL AZHAR INDONESIA
### Fakultas Sains dan Teknologi — Program Studi Informatika

---

## IDENTITAS

| Komponen | Detail |
|----------|--------|
| **Nama Mata Kuliah** | Probabilitas dan Statistik |
| **Kode Mata Kuliah** | IF52510033 |
| **Bobot SKS** | 3 SKS |
| **Semester** | 1 (Ganjil) — Tahun Akademik 2026/2027 |
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Kurikulum** | Kurikulum Informatika 2025 — Revisi 2026 |

---

## A. PETA TUGAS TERHADAP SUB-CPMK

Seluruh tugas pada mata kuliah ini menelusuri balik ke dua Sub-CPMK yang ditetapkan kurikulum. Tidak ada tugas yang tidak terhubung ke Sub-CPMK.

| Sub-CPMK | Bobot | Instrumen Penilai |
|----------|-------|-------------------|
| `PS-Sub-CPMK081-1` — menerapkan dan menganalisis probabilitas, peubah acak, distribusi, estimasi, dan inferensi | 45% | Kuis 1–4 (15%), Proyek bagian inferensi (5%), UAS (25%) |
| `PS-Sub-CPMK102-1` — mengolah, menganalisis, dan memvisualisasikan data dengan statistika deskriptif dan inferensial | 55% | Laporan Lab 01–14 (25%), Proyek bagian analisis (5%), UTS (25%) |

---

## B. RINGKASAN SELURUH TUGAS

| Kode | Nama Tugas | Jenis | Sub-CPMK | Bobot | Kumpul |
|------|-----------|-------|----------|-------|--------|
| T-01 | Laporan Lab 01 — Setup dan eksplorasi data pertama | Individu | 102-1 | 1,92% | Minggu 2 |
| T-02 | Laporan Lab 02 — Statistika deskriptif dengan pandas | Individu | 102-1 | 1,92% | Minggu 3 |
| T-03 | Laporan Lab 03 — Studio visualisasi statistik | Individu | 102-1 | 1,92% | Minggu 4 |
| T-04 | Laporan Lab 04 — Simulasi probabilitas Monte Carlo | Individu | 102-1 | 1,92% | Minggu 5 |
| T-05 | Laporan Lab 05 — Teorema Bayes dan penyaring spam | Individu | 102-1 | 1,92% | Minggu 6 |
| T-06 | Laporan Lab 06 — Distribusi diskret dengan `scipy.stats` | Individu | 102-1 | 1,92% | Minggu 7 |
| T-07 | Laporan Lab 07 — Distribusi kontinu dan uji kenormalan | Individu | 102-1 | 1,92% | Minggu 8 |
| T-09 | Laporan Lab 09 — Simulasi Teorema Limit Pusat | Individu | 102-1 | 1,92% | Minggu 10 |
| T-10 | Laporan Lab 10 — Interval kepercayaan dan cakupannya | Individu | 102-1 | 1,92% | Minggu 11 |
| T-11 | Laporan Lab 11 — Uji hipotesis satu sampel | Individu | 102-1 | 1,92% | Minggu 12 |
| T-12 | Laporan Lab 12 — A/B testing dua sampel | Individu | 102-1 | 1,92% | Minggu 13 |
| T-13 | Laporan Lab 13 — ANOVA dan chi-square | Individu | 102-1 | 1,92% | Minggu 14 |
| T-14 | Laporan Lab 14 — Korelasi dan regresi linear | Individu | 102-1 | 2,04% | Minggu 15 |
| K-01 | Kuis 1 — deskriptif dan visualisasi | Individu | 081-1 | 3,75% | Minggu 3 |
| K-02 | Kuis 2 — probabilitas dan Bayes | Individu | 081-1 | 3,75% | Minggu 5 |
| K-03 | Kuis 3 — sampling dan estimasi | Individu | 081-1 | 3,75% | Minggu 10 |
| K-04 | Kuis 4 — uji hipotesis dan ANOVA | Individu | 081-1 | 3,75% | Minggu 13 |
| P-00 | Proposal proyek | Kelompok | — | Syarat | Minggu 6 |
| P-01 | Proyek analisis data statistik | Kelompok | 081-1 + 102-1 | 10% | Minggu 14–15 |
| U-01 | Ujian Tengah Semester | Individu | 102-1 | 25% | Minggu 8 |
| U-02 | Ujian Akhir Semester | Individu | 081-1 | 25% | Minggu 16 |

**Total: 100%**

---

## C. RINCIAN TUGAS LABORATORIUM (T-01 s.d. T-14)

### Tujuan Umum

Seluruh laporan lab menilai `PS-Sub-CPMK102-1`: *mampu mengolah, menganalisis, dan memvisualisasikan data menggunakan statistika deskriptif dan inferensial untuk menghasilkan kesimpulan yang valid.*

### Uraian Tugas

**Objek garapan.** Notebook Google Colab berisi kode, keluaran, visualisasi, dan narasi interpretasi untuk topik lab minggu berjalan.

**Batasan.**
- Seluruh kode ditulis dengan Python 3.x dan berjalan di Google Colab tanpa modifikasi.
- Komentar kode ditulis dalam bahasa Indonesia.
- Dataset yang dipakai adalah dataset yang disediakan pada lab atau data Indonesia yang sumbernya disebutkan.
- Setiap keluaran statistik **wajib disertai kalimat interpretasi**. Notebook yang hanya berisi angka tanpa tafsir dinilai tidak lengkap.
- AI Usage Log wajib dilampirkan pada sel terakhir notebook.

**Metode pengerjaan.**
1. Ikuti langkah-langkah pada berkas lab minggu berjalan.
2. Selesaikan seluruh bagian **Tantangan Tambahan**.
3. Tulis bagian **Refleksi** (3–5 kalimat): apa yang baru dipahami, dan bagian mana yang masih membingungkan.
4. Isi AI Usage Log.
5. Unduh sebagai `.ipynb`, unggah ke LMS UAI beserta tautan Colab yang sudah dibuka aksesnya.

**Luaran.** Satu berkas `.ipynb` bernama `LabNN_NIM_NamaLengkap.ipynb`.

### Kriteria Penilaian Laporan Lab

| Aspek | Bobot | Deskripsi |
|-------|-------|-----------|
| Ketepatan prosedur | 30% | Langkah statistik benar dan berurutan; fungsi yang dipakai sesuai |
| Kesesuaian grafik | 20% | Jenis grafik cocok dengan jenis data; berlabel dan terbaca |
| Validitas interpretasi | 30% | Kesimpulan benar-benar ditopang keluaran, tidak melampaui data |
| Tantangan tambahan | 10% | Dikerjakan lengkap dan benar |
| Kerapian dan AI Usage Log | 10% | Notebook terstruktur, log terisi jujur |

---

## D. RINCIAN KUIS (K-01 s.d. K-04)

### Tujuan

Kuis menilai `PS-Sub-CPMK081-1` pada tingkat C3–C4: kemampuan menerapkan rumus dengan benar dan menganalisis asumsi yang menyertainya.

### Ketentuan

| Aspek | Ketentuan |
|-------|-----------|
| **Bentuk** | Tertulis di kelas, 20 menit, *closed book* |
| **Jumlah soal** | 3–4 soal hitungan kontekstual |
| **Alat bantu** | Kalkulator ilmiah dan satu lembar tabel distribusi |
| **AI** | **Tidak diizinkan** |
| **Susulan** | Hanya dengan surat keterangan sakit/tugas institusi, maksimal 7 hari setelah jadwal |

### Cakupan per Kuis

| Kuis | Minggu | Cakupan Materi |
|------|--------|----------------|
| K-01 | 3 | Jenis dan skala data; ukuran pemusatan, penyebaran, posisi; pencilan; pemilihan grafik |
| K-02 | 5 | Aksioma probabilitas; aturan penjumlahan dan perkalian; probabilitas bersyarat; Teorema Bayes; pencacahan |
| K-03 | 10 | Ekspektasi dan varians; distribusi sampling; Teorema Limit Pusat; estimasi titik; interval kepercayaan |
| K-04 | 13 | Uji hipotesis satu dan dua sampel; galat Tipe I/II; ANOVA satu arah; uji chi-square |

### Rubrik Penilaian Kuis

| Aspek | Bobot | Deskripsi |
|-------|-------|-----------|
| Ketepatan rumus | 30% | Rumus yang dipilih sesuai dengan jenis persoalan |
| Ketepatan hitung | 30% | Perhitungan benar sampai hasil akhir, satuan tepat |
| Kecocokan asumsi | 20% | Asumsi yang menyertai uji/distribusi disebutkan dan diperiksa |
| Kualitas interpretasi | 20% | Hasil angka diterjemahkan menjadi kesimpulan kontekstual |

---

## E. RINCIAN PROYEK (P-00 dan P-01)

### E.1 Proposal Proyek (P-00) — Minggu 6

**Bentuk.** Dokumen 2 halaman (PDF), dikumpulkan per kelompok.

**Isi wajib.**
1. Nama kelompok dan pembagian peran (3–4 orang).
2. **Pertanyaan penelitian** — satu pertanyaan utama dan dua pertanyaan turunan, dirumuskan dengan jelas dan dapat dijawab secara statistik.
3. **Sumber data** — nama sumber, tautan, jumlah baris dan kolom, serta lisensi/ketentuan pakai.
4. **Rencana analisis** — analisis deskriptif apa, visualisasi apa, dan uji inferensial apa yang direncanakan beserta alasannya.
5. **Potensi keterbatasan** yang sudah dapat diperkirakan.

**Status.** Tidak berbobot nilai, tetapi **wajib disetujui** sebelum kelompok boleh melanjutkan ke pengerjaan proyek. Proposal yang belum disetujui dikembalikan untuk diperbaiki paling lambat Minggu 7.

**Kriteria persetujuan.**
- Pertanyaan penelitian dapat dijawab dengan metode yang dipelajari sampai Minggu 14.
- Data benar-benar tersedia dan dapat diakses kelompok.
- Rencana analisis realistis untuk dikerjakan dalam 8 minggu.

### E.2 Proyek Analisis Data Statistik (P-01) — Minggu 14–15

**Tujuan.** Menilai kedua Sub-CPMK sekaligus pada konteks nyata yang tidak terstruktur seperti soal latihan.

**Uraian tugas.**

*Objek garapan:* sebuah persoalan nyata berkonteks Indonesia yang dapat dijawab dengan data dan metode statistik yang dipelajari.

*Batasan:*
- Kelompok 3–4 orang.
- Data harus nyata (BPS, Satu Data Indonesia, Kaggle dengan konteks Indonesia, atau data primer yang dikumpulkan sendiri). **Data sintetis tidak diperkenankan** kecuali sebagai pembanding.
- Minimal mencakup: statistika deskriptif, sekurang-kurangnya dua jenis visualisasi, **sekurang-kurangnya satu uji inferensial**, dan pembahasan keterbatasan.
- AI boleh dipakai untuk membantu penulisan kode dan penyuntingan bahasa, **tidak boleh** untuk menentukan uji statistik atau menafsirkan hasil.

*Metode pengerjaan:*

| Tahap | Minggu | Kegiatan |
|-------|--------|----------|
| 1 | 6 | Perumusan pertanyaan dan proposal |
| 2 | 7–9 | Pengumpulan dan pembersihan data; catat setiap keputusan pembersihan |
| 3 | 10–11 | Analisis deskriptif dan visualisasi |
| 4 | 12–13 | Analisis inferensial; periksa asumsi sebelum menjalankan uji |
| 5 | 14 | Penulisan laporan dan finalisasi notebook |
| 6 | 15 | Presentasi |

**Luaran.**

| Luaran | Format | Ketentuan |
|--------|--------|-----------|
| Notebook analisis | `.ipynb` Google Colab | Dapat dijalankan ulang dari awal sampai akhir tanpa galat |
| Laporan | PDF 8–12 halaman | Struktur: Pendahuluan, Data dan Metode, Hasil, Pembahasan, Kesimpulan dan Keterbatasan, Referensi, AI Usage Log |
| Presentasi | PDF/slide | 15 menit presentasi + 5 menit tanya jawab |

**Rubrik penilaian proyek (10% nilai akhir).**

| Aspek | Sub-CPMK | Bobot dari 10% | Deskripsi |
|-------|----------|----------------|-----------|
| Perumusan pertanyaan dan kesesuaian data | 102-1 | 1,5% | Pertanyaan tajam, data relevan dan memadai |
| Pengolahan dan visualisasi | 102-1 | 2,0% | Pembersihan data terdokumentasi; grafik tepat dan terbaca |
| Ketepatan uji dan pemeriksaan asumsi | 081-1 | 2,5% | Uji yang dipilih sesuai; asumsi diperiksa, bukan diasumsikan |
| Validitas interpretasi dan keterbatasan | 081-1 | 2,5% | Kesimpulan tidak melampaui data; keterbatasan disebut jujur |
| Kualitas presentasi dan penguasaan | 102-1 | 1,5% | Penyampaian jelas; seluruh anggota menguasai isi |

> **Catatan penting.** Kelompok yang hasil ujinya **tidak signifikan** tidak dirugikan. Yang dinilai adalah ketepatan prosedur dan kejujuran interpretasi. Melaporkan "tidak ditemukan perbedaan yang signifikan" dengan analisis yang benar bernilai lebih tinggi daripada memaksakan hasil signifikan dengan prosedur yang keliru.

---

## F. RINCIAN UJIAN (U-01 dan U-02)

### F.1 Ujian Tengah Semester (U-01)

| Aspek | Ketentuan |
|-------|-----------|
| **Minggu** | 8 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | 25% |
| **Durasi** | 100 menit |
| **Bentuk** | Tes tulis *closed book* |
| **Cakupan** | Minggu 1–7 |
| **Alat bantu** | Kalkulator ilmiah, satu lembar tabel distribusi (disediakan pengawas) |
| **AI** | **Tidak diizinkan** |

Komposisi soal dan bobot per pokok bahasan ada pada [kisi-kisi UTS](../05-assessments/kisi-kisi-uts.md).

### F.2 Ujian Akhir Semester (U-02)

| Aspek | Ketentuan |
|-------|-----------|
| **Minggu** | 16 |
| **Sub-CPMK** | `PS-Sub-CPMK081-1` |
| **Bobot** | 25% |
| **Durasi** | 120 menit |
| **Bentuk** | Tes tulis *closed book* |
| **Cakupan** | Komprehensif Minggu 1–15, penekanan Minggu 9–14 |
| **Alat bantu** | Kalkulator ilmiah, satu lembar tabel distribusi (disediakan pengawas) |
| **AI** | **Tidak diizinkan** |
| **Syarat mengikuti** | Kehadiran minimal 75% |

Komposisi soal ada pada [kisi-kisi UAS](../05-assessments/kisi-kisi-uas.md).

---

## G. JADWAL PENGUMPULAN TERPADU

| Minggu | Yang Dikumpulkan | Batas Waktu |
|--------|------------------|-------------|
| 2 | T-01 | Minggu berikutnya, pukul 23.59 WIB sebelum kelas |
| 3 | T-02 · **K-01 di kelas** | idem |
| 4 | T-03 | idem |
| 5 | T-04 · **K-02 di kelas** | idem |
| 6 | T-05 · **P-00 proposal** | idem |
| 7 | T-06 | idem |
| 8 | T-07 · **U-01 UTS** | idem |
| 10 | T-09 · **K-03 di kelas** | idem |
| 11 | T-10 | idem |
| 12 | T-11 | idem |
| 13 | T-12 · **K-04 di kelas** | idem |
| 14 | T-13 · **P-01 laporan + notebook** | idem |
| 15 | T-14 · **P-01 presentasi** | idem |
| 16 | **U-02 UAS** | — |

---

## H. BEBAN BELAJAR MAHASISWA

Perhitungan mengikuti SN-Dikti: 1 SKS setara 170 menit per minggu, terbagi atas tatap muka, tugas terstruktur, dan belajar mandiri.

| Komponen | Menit/Minggu | Keterangan |
|----------|--------------|------------|
| Tatap muka | 150 | 1 pertemuan @150 menit |
| Tugas terstruktur | 180 | Laporan lab, kuis, tugas proyek |
| Belajar mandiri | 180 | Membaca bab buku ajar, latihan soal |
| **Total** | **510** | Setara **3 SKS** (3 × 170 menit) |

Sepanjang 16 minggu: **136 jam** beban belajar total.

---

## I. AI USAGE LOG — FORMAT WAJIB

Dilampirkan pada setiap laporan lab dan laporan proyek.

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |
| 2 | | | | | |

**Pernyataan wajib (ditandatangani secara elektronik dengan nama dan NIM):**

> *Saya menyatakan bahwa seluruh perhitungan statistik, pemilihan uji, dan interpretasi hasil dalam pekerjaan ini adalah hasil pemahaman saya sendiri. Penggunaan AI telah saya catat seluruhnya pada tabel di atas. Saya bersedia menjelaskan setiap bagian pekerjaan ini apabila diminta.*

Laporan tanpa AI Usage Log — termasuk yang menyatakan "tidak memakai AI" tetapi tidak mengisi tabel — dianggap **belum lengkap** dan dikembalikan.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
