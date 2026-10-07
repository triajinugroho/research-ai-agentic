# Panduan Proyek Analisis Data Statistik

## Probabilitas dan Statistik — IF52510033

**Semester Ganjil 2026/2027**
**Bobot:** 10% nilai akhir — teknik **Unjuk Kerja**
**Sub-CPMK:** `PS-Sub-CPMK081-1` (5%) + `PS-Sub-CPMK102-1` (5%)
**Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.

---

## 1. Gambaran Umum

Proyek ini adalah satu-satunya asesmen yang menguji **kedua Sub-CPMK sekaligus** pada persoalan nyata yang tidak terstruktur seperti soal latihan. Di sinilah mahasiswa menghadapi apa yang sebenarnya dihadapi seorang analis: data yang berantakan, pertanyaan yang belum tajam, dan kesimpulan yang harus dipertanggungjawabkan.

### Yang Dituntut

> Melakukan **analisis data statistik end-to-end** atas sebuah persoalan nyata berkonteks Indonesia: merumuskan pertanyaan, memperoleh dan membersihkan data, melakukan analisis deskriptif dan visualisasi, menjalankan inferensi yang sesuai, lalu menarik kesimpulan beserta keterbatasannya.

---

## 2. Ketentuan Dasar

| Aspek | Ketentuan |
|-------|-----------|
| Bentuk | Kelompok 3–4 orang |
| Data | **Harus nyata** — BPS, Satu Data Indonesia, Jakarta Open Data, Kaggle berkonteks Indonesia, atau data primer yang dikumpulkan sendiri |
| Data sintetis | **Tidak diperkenankan** sebagai data utama; boleh hanya sebagai pembanding, dan harus dinyatakan |
| Ukuran data | Minimal 100 baris; disarankan 200–50.000 |
| Cakupan analisis wajib | Statistika deskriptif · Minimal 2 jenis visualisasi · **Minimal 1 uji inferensial** · Pembahasan keterbatasan |
| Perangkat | Python di Google Colab |
| AI | Boleh untuk kode dan penyuntingan bahasa; **tidak boleh** untuk memilih uji atau menafsirkan hasil |

---

## 3. Tahapan dan Tenggat

| Tahap | Minggu | Luaran | Status |
|-------|--------|--------|--------|
| 1. Pembentukan kelompok dan pemilihan tema | 4–5 | — | — |
| 2. **Proposal** | **6** | PDF 2 halaman | **Wajib disetujui** |
| 3. Pengumpulan dan pembersihan data | 7–9 | Catatan pembersihan | — |
| 4. Analisis deskriptif dan visualisasi | 10–11 | Notebook bagian 1 | — |
| 5. Analisis inferensial | 12–13 | Notebook bagian 2 | — |
| 6. **Laporan dan notebook** | **14** | PDF + `.ipynb` | **Dinilai** |
| 7. **Presentasi** | **15** | Slide + presentasi 15' | **Dinilai** |

---

## 4. Proposal (Minggu 6)

### 4.1 Isi Wajib

Dokumen PDF maksimal 2 halaman berisi:

1. **Identitas kelompok** — nama, NIM, dan **pembagian peran** tiap anggota.
2. **Pertanyaan penelitian** — satu pertanyaan utama dan dua pertanyaan turunan.
3. **Sumber data** — nama, tautan, jumlah baris dan kolom, lisensi/ketentuan pakai, tanggal akses.
4. **Rencana analisis** — analisis deskriptif apa, visualisasi apa, dan **uji inferensial apa beserta alasan pemilihannya**.
5. **Potensi keterbatasan** yang sudah dapat diperkirakan sejak awal.

### 4.2 Kriteria Persetujuan

| Kriteria | Penjelasan |
|----------|------------|
| Pertanyaan dapat dijawab | Dengan metode yang dipelajari sampai Minggu 14 |
| Data benar-benar tersedia | Kelompok sudah mengunduh dan membukanya, bukan sekadar menemukan tautannya |
| Realistis | Dapat diselesaikan dalam 8 minggu oleh 3–4 mahasiswa semester 1 |
| Spesifik | Bukan "menganalisis data pendidikan Indonesia", melainkan pertanyaan yang tajam |

### 4.3 Contoh Pertanyaan yang Baik dan yang Lemah

| Lemah | Mengapa lemah | Perbaikan |
|-------|---------------|-----------|
| "Menganalisis data BPS" | Bukan pertanyaan | "Apakah rata-rata IPM provinsi di Indonesia Timur berbeda dari Indonesia Barat?" |
| "Apakah pendidikan penting?" | Tidak dapat dijawab secara statistik | "Apakah ada hubungan antara angka partisipasi sekolah dan IPM provinsi?" |
| "Memprediksi harga rumah" | Melampaui cakupan MK semester 1 | "Seberapa kuat hubungan luas bangunan dengan harga rumah di Jabodetabek?" |
| "Apakah TransJakarta bagus?" | Tidak terukur | "Apakah jumlah penumpang berbeda signifikan antar koridor TransJakarta?" |

### 4.4 Tema yang Disarankan

| Tema | Sumber Data | Uji yang Mungkin |
|------|-------------|------------------|
| Perbandingan IPM antar wilayah | BPS | Uji-t dua sampel / ANOVA |
| Kualitas udara antar stasiun Jakarta | Jakarta Open Data | ANOVA |
| Hubungan angka pengangguran dan tingkat pendidikan | BPS | Korelasi / regresi |
| Pola laporan gangguan layanan publik per hari | Satu Data Indonesia | Chi-square kesesuaian |
| Perbandingan harga properti antar kota | Kaggle Indonesia | Uji-t / ANOVA |
| Survei kebiasaan belajar mahasiswa Informatika UAI | Data primer | Uji-t / korelasi |
| Pola kecelakaan lalu lintas per hari dalam seminggu | BPS/Satu Data | Chi-square |
| Hubungan durasi penggunaan aplikasi dan prestasi | Data primer | Korelasi / regresi |

---

## 5. Notebook Analisis (Minggu 14)

### 5.1 Struktur Wajib

```
1. Pendahuluan
   - Pertanyaan penelitian
   - Latar singkat

2. Data
   - Sumber dan cara memperolehnya
   - Pemeriksaan kualitas awal
   - PEMBERSIHAN DATA — setiap keputusan dicatat dan dijelaskan

3. Analisis Deskriptif
   - Ukuran ringkasan
   - Minimal 2 jenis visualisasi

4. Analisis Inferensial
   - Pemilihan uji beserta ALASANNYA
   - PEMERIKSAAN ASUMSI
   - Hasil uji
   - Ukuran efek dan interval kepercayaan

5. Kesimpulan
   - Jawaban atas pertanyaan penelitian
   - Keterbatasan
   - Apa yang TIDAK dapat disimpulkan

6. AI Usage Log
```

### 5.2 Ketentuan Teknis

- Notebook **harus dapat dijalankan ulang dari sel pertama sampai terakhir tanpa galat**.
- Data dimuat dari tautan atau disertakan dalam pengumpulan.
- *Seed* ditetapkan bila ada proses acak.
- Setiap keluaran statistik disertai kalimat interpretasi.
- Komentar kode dalam bahasa Indonesia.

### 5.3 Dokumentasi Pembersihan Data

Ini bagian yang paling sering diabaikan dan paling sering menjadi sumber kesalahan.

| Yang harus dicatat | Contoh |
|--------------------|--------|
| Berapa baris dibuang dan mengapa | "12 baris dibuang karena kolom IPM kosong (0,9% dari data)" |
| Bagaimana nilai hilang ditangani | "Nilai hilang pada kolom pendapatan tidak diimputasi; baris dikecualikan pada analisis yang melibatkan kolom itu" |
| Apakah ada pencilan dan apa yang dilakukan | "Provinsi DKI Jakarta teridentifikasi sebagai pencilan pada IPM. **Tidak dibuang**, karena merupakan data sah" |
| Transformasi apa yang dilakukan | "Kolom populasi ditransformasi log karena sangat menceng kanan" |

> **Aturan tegas:** membuang data tanpa alasan substantif — termasuk membuang pencilan agar hasil "lebih rapi" — mengurangi nilai pada aspek validitas interpretasi.

---

## 6. Laporan (Minggu 14)

### 6.1 Format

| Aspek | Ketentuan |
|-------|-----------|
| Panjang | 8–12 halaman (tidak termasuk lampiran) |
| Format | PDF, A4, margin 2,5 cm, font 11–12 pt, spasi 1,15 |
| Bahasa | Indonesia baku; istilah teknis boleh bilingual |

### 6.2 Struktur

| Bagian | Isi | Halaman |
|--------|-----|---------|
| Halaman judul | Judul, nama kelompok, anggota dan NIM, mata kuliah, tanggal | 1 |
| 1. Pendahuluan | Latar, pertanyaan penelitian, tujuan | 1–1,5 |
| 2. Data dan Metode | Sumber data, deskripsi variabel, **pembersihan**, metode analisis dan alasannya | 2–2,5 |
| 3. Hasil | Deskriptif, visualisasi, hasil inferensial | 2,5–3 |
| 4. Pembahasan | Tafsir hasil dalam konteks masalah | 1,5–2 |
| 5. Kesimpulan dan Keterbatasan | Jawaban atas pertanyaan; **keterbatasan yang jujur** | 1 |
| Referensi | Sumber data dan pustaka | 0,5 |
| Lampiran | **AI Usage Log** (wajib) | — |

### 6.3 Bagian Keterbatasan

Bagian ini **wajib** dan dinilai. Yang harus dibahas:

1. **Keterwakilan sampel** — apakah sampel mewakili populasi yang diklaim?
2. **Kualitas data** — nilai hilang, kemungkinan kesalahan pencatatan, ketepatan waktu data.
3. **Batas metode** — asumsi apa yang tidak sepenuhnya terpenuhi?
4. **Batas kesimpulan** — mengapa hubungan yang ditemukan **bukan** sebab-akibat?
5. **Variabel perancu** yang tidak terukur.

> Kelompok yang menulis "penelitian ini tidak memiliki keterbatasan" memperoleh nilai **nol** pada aspek ini.

---

## 7. Presentasi (Minggu 15)

| Bagian | Durasi | Isi |
|--------|--------|-----|
| 1. Latar dan pertanyaan | 2' | Mengapa penting; pertanyaan yang dijawab |
| 2. Data | 3' | Sumber, ukuran, **proses pembersihan** |
| 3. Analisis deskriptif | 3' | Ringkasan dan visualisasi kunci |
| 4. Analisis inferensial | 4' | Uji, **asumsi**, hasil, ukuran efek |
| 5. Kesimpulan dan keterbatasan | 3' | Jawaban dan batasnya |
| Tanya jawab | 5' | — |

**Ketentuan:**
- Slide maksimal 12 halaman.
- **Setiap anggota wajib berbicara.**
- Seluruh anggota harus menguasai keseluruhan isi; pertanyaan dapat diarahkan kepada siapa saja.

---

## 8. Rubrik Penilaian (10% Nilai Akhir)

### 8.1 Menelusuri ke `PS-Sub-CPMK081-1` — 5%

Kriteria kurikulum: *ketepatan rumus dan hitung; kecocokan asumsi; kualitas interpretasi.*

| Aspek | Bobot | 4 (Sangat Baik) | 3 (Baik) | 2 (Cukup) | 1 (Kurang) |
|-------|-------|-----------------|----------|-----------|------------|
| Ketepatan pemilihan uji | 2,5% | Uji tepat sesuai jenis data dan rancangan; **alasan ditulis jelas** | Uji tepat, alasan kurang jelas | Uji dapat diterima tetapi bukan yang optimal | Uji tidak sesuai jenis data |
| Pemeriksaan asumsi | 1,5% | Seluruh asumsi diperiksa, ditampilkan buktinya, dan ditindaklanjuti bila dilanggar | Asumsi utama diperiksa | Asumsi disebut tanpa diperiksa | Asumsi diabaikan |
| Validitas interpretasi | 1,0% | Kesimpulan persis sebatas data; ukuran efek dan IK dilaporkan | Kesimpulan tepat, efek kurang dibahas | Ada klaim yang melampaui data | Klaim sebab-akibat dari data observasional |

### 8.2 Menelusuri ke `PS-Sub-CPMK102-1` — 5%

Kriteria kurikulum: *ketepatan prosedur; kesesuaian grafik; validitas interpretasi.*

| Aspek | Bobot | 4 (Sangat Baik) | 3 (Baik) | 2 (Cukup) | 1 (Kurang) |
|-------|-------|-----------------|----------|-----------|------------|
| Kualitas data dan pembersihan | 1,5% | Setiap keputusan dijelaskan dan dapat dipertanggungjawabkan | Pembersihan dilakukan, sebagian dijelaskan | Dilakukan tanpa penjelasan | Data dipakai tanpa pemeriksaan |
| Kesesuaian dan kejujuran visualisasi | 1,5% | Grafik tepat, berlabel lengkap, jujur, mencantumkan n dan sumber | Grafik tepat dan terbaca | Kurang sesuai jenis data | Menyesatkan atau tanpa label |
| Kejelasan komunikasi | 1,0% | Alur runtut; istilah dijelaskan; audiens paham | Jelas dengan sedikit lompatan | Sulit diikuti sebagian | Tidak terstruktur |
| Penguasaan saat tanya jawab | 1,0% | Seluruh anggota menjawab tepat dan berbasis data | Sebagian besar menguasai | Hanya satu-dua yang menguasai | Tidak dapat menjawab pertanyaan dasar |

### 8.3 Konversi Skor

$$\text{Nilai aspek} = \frac{\text{skor } (1\text{–}4)}{4} \times \text{bobot aspek}$$

### 8.4 Pengurangan Nilai

| Pelanggaran | Pengurangan |
|-------------|-------------|
| AI Usage Log tidak ada atau tidak lengkap | Laporan dikembalikan; dinilai sebagai terlambat |
| Notebook tidak dapat dijalankan ulang | −20% dari total nilai proyek |
| Data sintetis dipakai sebagai data utama | −40% dari total nilai proyek |
| Pembersihan data tidak didokumentasikan | −15% dari total nilai proyek |
| Bagian keterbatasan kosong atau formalitas | −15% dari total nilai proyek |
| Terlambat mengumpulkan | Mengikuti kebijakan keterlambatan umum |

---

## 9. Catatan Penting tentang Hasil

> **Kelompok yang hasil ujinya tidak signifikan TIDAK dirugikan sama sekali.**
>
> Yang dinilai adalah ketepatan prosedur dan kejujuran interpretasi. Melaporkan *"tidak ditemukan perbedaan yang signifikan (p = 0,34; Cohen's d = 0,12)"* dengan analisis yang benar bernilai **lebih tinggi** daripada memaksakan hasil signifikan dengan prosedur yang keliru.
>
> Ini bukan kelonggaran. Ini adalah inti dari apa yang hendak diajarkan mata kuliah ini: **amanah dalam menghadapi ketidakpastian**. Seorang analis data yang jujur tentang temuan nihil lebih berharga daripada yang selalu menemukan hasil "mengesankan".

---

## 10. Daftar Periksa Sebelum Mengumpulkan

### Notebook
- [ ] Dapat dijalankan ulang dari awal sampai akhir tanpa galat
- [ ] *Seed* ditetapkan bila ada proses acak
- [ ] Setiap keluaran disertai kalimat interpretasi
- [ ] Komentar kode dalam bahasa Indonesia
- [ ] Pembersihan data didokumentasikan langkah per langkah

### Laporan
- [ ] 8–12 halaman
- [ ] Seluruh bagian ada sesuai struktur
- [ ] Setiap grafik punya judul, label sumbu dengan satuan, dan keterangan n
- [ ] Sumber data lengkap dengan tautan dan tanggal akses
- [ ] Asumsi setiap uji ditampilkan hasil pemeriksaannya
- [ ] Ukuran efek dan interval kepercayaan dilaporkan
- [ ] Bagian keterbatasan ditulis jujur, minimal membahas 4 dari 5 butir pada §6.3
- [ ] AI Usage Log lengkap dan ditandatangani

### Presentasi
- [ ] Slide maksimal 12 halaman
- [ ] Sudah dilatih dan pas dalam 15 menit
- [ ] Seluruh anggota tahu bagiannya
- [ ] Seluruh anggota menguasai keseluruhan isi

---

## 11. Pertanyaan yang Akan Diajukan Saat Tanya Jawab

Siapkan jawabannya:

1. Berapa baris yang dibuang, dan atas dasar apa?
2. Apakah sampel Anda representatif? Bila tidak, apa konsekuensinya?
3. Mengapa memilih uji itu dan bukan yang lain?
4. Asumsi apa saja yang harus dipenuhi? Tunjukkan buktinya.
5. Apa yang akan Anda lakukan bila asumsi kenormalan dilanggar?
6. Apa arti *p-value* yang Anda peroleh, dalam kalimat Anda sendiri?
7. Berapa ukuran efeknya? Apakah bermakna secara praktis?
8. Bisakah menyimpulkan sebab-akibat? Mengapa?
9. Apa keterbatasan terbesar penelitian Anda?
10. Bagian mana yang dibantu AI? Jelaskan salah satu baris kodenya.

---

## 12. Sumber Data

Panduan lengkap sumber data berkonteks Indonesia ada pada [datasets/README.md](../datasets/README.md), mencakup BPS, Satu Data Indonesia, Jakarta Open Data, dan ketentuan pengumpulan data primer.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
