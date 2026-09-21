# Kerangka Asesmen — Probabilitas dan Statistik (IF52510033)

**Program Studi Informatika — Universitas Al Azhar Indonesia**
**Semester Ganjil 2026/2027 · Kurikulum Informatika 2025 Revisi 2026**
**Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.

---

## 1. Prinsip Asesmen

### 1.1 Penelusuran Penuh ke Sub-CPMK

Pada Kurikulum 2025 revisi 2026, bobot penilaian **melekat pada Sub-CPMK**, bukan pada komponen nilai yang ditetapkan bebas oleh dosen. Setiap instrumen penilaian harus dapat ditelusuri ke salah satu dari dua Sub-CPMK mata kuliah ini.

```
   CPL08 ──→ CPMK081 ──→ PS-Sub-CPMK081-1 (45%) ──→ Kuis · Proyek · UAS
   CPL10 ──→ CPMK102 ──→ PS-Sub-CPMK102-1 (55%) ──→ Lab · Proyek · UTS
```

### 1.2 Lima Prinsip yang Dipegang

| Prinsip | Penerapan |
|---------|-----------|
| **Keselarasan konstruktif** | Setiap butir asesmen menguji indikator yang memang diajarkan dan dilatihkan |
| **Frekuensi tinggi, bobot kecil** | 13 lab + 4 kuis agar mahasiswa yang tertinggal terdeteksi dini |
| **Penalaran di atas hitungan** | Jawaban tanpa langkah bernilai maksimal 40%; langkah benar dengan salah hitung tetap bernilai besar |
| **Kejujuran dilindungi** | Hasil "tidak signifikan" tidak mengurangi nilai; yang dinilai adalah ketepatan prosedur |
| **Transparansi AI** | AI Usage Log wajib pada setiap laporan; ujian bebas AI |

---

## 2. Peta Bobot Resmi

Diambil dari sheet `Copy of (Ref) 15. Pemetaan MK-CPMK-SubCPMK` berkas kurikulum.

| Teknik Penilaian | `PS-Sub-CPMK081-1` | `PS-Sub-CPMK102-1` | Total |
|------------------|--------------------|--------------------|-------|
| Partisipasi | – | – | **–** |
| Kuis | 15% | – | **15%** |
| Observasi (Praktek/Tugas) | – | 25% | **25%** |
| Unjuk Kerja (Presentasi/Proyek) | 5% | 5% | **10%** |
| Tes Tulis (UTS) | – | 25% | **25%** |
| Tes Tulis (UAS) | 25% | – | **25%** |
| **Total** | **45%** | **55%** | **100%** |

> Mata kuliah ini **tidak memiliki komponen Partisipasi**. Kehadiran tetap disyaratkan minimal 75% sebagai prasyarat mengikuti UAS, tetapi tidak berbobot nilai.

---

## 3. Rincian Instrumen

### 3.1 Kuis (15% — `PS-Sub-CPMK081-1`)

| Aspek | Ketentuan |
|-------|-----------|
| Jumlah | 4 kuis, masing-masing 3,75% |
| Jadwal | Minggu 3, 5, 10, 13 |
| Bentuk | Tertulis di kelas, 20 menit, *closed book* |
| Isi | 3–4 soal hitungan kontekstual |
| Alat bantu | Kalkulator ilmiah, satu lembar tabel distribusi |
| AI | **Tidak diizinkan** |

**Rubrik kuis** (mengikuti kriteria Sub-CPMK: *ketepatan rumus dan hitung; kecocokan asumsi; kualitas interpretasi*):

| Aspek | Bobot |
|-------|-------|
| Ketepatan rumus | 30% |
| Ketepatan hitung | 30% |
| Kecocokan asumsi | 20% |
| Kualitas interpretasi | 20% |

### 3.2 Observasi — Laporan Lab (25% — `PS-Sub-CPMK102-1`)

| Aspek | Ketentuan |
|-------|-----------|
| Jumlah | 13 laporan (Lab 01–07, 09–14) |
| Bobot | 1,92% per laporan (Lab 14 = 2,04% untuk menggenapkan) |
| Bentuk | Notebook Google Colab `.ipynb` |
| Pengumpulan | Sebelum kelas minggu berikutnya |
| AI | Diizinkan untuk kode, wajib dicatat di AI Usage Log |

**Rubrik laporan lab** (mengikuti kriteria Sub-CPMK: *ketepatan prosedur; kesesuaian grafik; validitas interpretasi*):

| Aspek | Bobot | Keterangan |
|-------|-------|------------|
| Ketepatan prosedur | 30% | Langkah statistik benar dan berurutan |
| Kesesuaian grafik | 20% | Jenis grafik cocok, berlabel, jujur |
| Validitas interpretasi | 30% | Kesimpulan ditopang keluaran, tidak melampaui data |
| Tantangan tambahan | 10% | Dikerjakan lengkap dan benar |
| Kerapian dan AI Usage Log | 10% | Notebook terstruktur, log terisi jujur |

> **Aturan mutlak:** notebook yang hanya berisi angka tanpa kalimat interpretasi dinilai **tidak lengkap** dan memperoleh maksimal 50% pada aspek validitas interpretasi.

### 3.3 Unjuk Kerja — Proyek (10% — kedua Sub-CPMK)

| Aspek | Ketentuan |
|-------|-----------|
| Bentuk | Proyek kelompok 3–4 orang |
| Luaran | Proposal (Minggu 6) · Notebook + laporan (Minggu 14) · Presentasi (Minggu 15) |
| Bobot | 5% ke `PS-Sub-CPMK081-1` + 5% ke `PS-Sub-CPMK102-1` |
| AI | Boleh untuk kode dan penyuntingan bahasa; **tidak boleh** untuk memilih uji atau menafsirkan hasil |

Rincian pada [panduan proyek](project-guidelines.md).

### 3.4 Tes Tulis — UTS (25% — `PS-Sub-CPMK102-1`)

| Aspek | Ketentuan |
|-------|-----------|
| Minggu | 8 |
| Durasi | 100 menit |
| Cakupan | Minggu 1–7 |
| Bentuk | *Closed book*; kalkulator ilmiah + tabel distribusi |
| AI | **Tidak diizinkan** |

Rincian pada [kisi-kisi UTS](kisi-kisi-uts.md).

### 3.5 Tes Tulis — UAS (25% — `PS-Sub-CPMK081-1`)

| Aspek | Ketentuan |
|-------|-----------|
| Minggu | 16 |
| Durasi | 120 menit |
| Cakupan | Komprehensif Minggu 1–15, penekanan Minggu 9–14 |
| Bentuk | *Closed book*; kalkulator ilmiah + tabel distribusi |
| AI | **Tidak diizinkan** |
| Prasyarat | Kehadiran minimal 75% |

Rincian pada [kisi-kisi UAS](kisi-kisi-uas.md).

---

## 4. Penentuan Ketuntasan Sub-CPMK

Selain nilai akhir, mata kuliah ini melaporkan **ketuntasan per Sub-CPMK** kepada Program Studi.

### 4.1 Rumus

$$\text{Nilai Sub-CPMK} = \frac{\sum (\text{nilai instrumen} \times \text{bobotnya})}{\sum \text{bobot instrumen}} \times 100$$

### 4.2 Contoh Perhitungan

Seorang mahasiswa memperoleh:

| Instrumen | Sub-CPMK | Bobot | Nilai (0–100) | Kontribusi |
|-----------|----------|-------|---------------|------------|
| Kuis 1–4 (rata-rata) | 081-1 | 15% | 72 | 10,80 |
| Proyek (bagian inferensi) | 081-1 | 5% | 80 | 4,00 |
| UAS | 081-1 | 25% | 68 | 17,00 |
| **Subtotal 081-1** | | **45%** | | **31,80** |
| Lab 01–14 (rata-rata) | 102-1 | 25% | 85 | 21,25 |
| Proyek (bagian analisis) | 102-1 | 5% | 82 | 4,10 |
| UTS | 102-1 | 25% | 75 | 18,75 |
| **Subtotal 102-1** | | **55%** | | **44,10** |
| **Nilai akhir** | | **100%** | | **75,90 → B+** |

**Ketuntasan Sub-CPMK:**

- `PS-Sub-CPMK081-1` = 31,80 / 45 × 100 = **70,67** → tuntas
- `PS-Sub-CPMK102-1` = 44,10 / 55 × 100 = **80,18** → tuntas

### 4.3 Ambang Ketuntasan

| Nilai Sub-CPMK | Status | Tindak Lanjut |
|----------------|--------|---------------|
| ≥ 60 | Tuntas | — |
| 50 – 59 | Tuntas bersyarat | Diberi materi pengayaan mandiri |
| < 50 | **Belum tuntas** | Dicatat dalam laporan evaluasi; direkomendasikan remedial |

> Mahasiswa dapat lulus mata kuliah (nilai akhir ≥ 55) tetapi **belum tuntas** pada salah satu Sub-CPMK. Kondisi ini dicatat dan dilaporkan karena berdampak pada mata kuliah hilir.

---

## 5. Konversi Nilai

| Rentang | Huruf | Bobot | Kategori |
|---------|-------|-------|----------|
| 85,00 – 100 | A | 4,00 | Sangat Baik |
| 80,00 – 84,99 | A− | 3,70 | Sangat Baik |
| 75,00 – 79,99 | B+ | 3,30 | Baik |
| 70,00 – 74,99 | B | 3,00 | Baik |
| 65,00 – 69,99 | B− | 2,70 | Cukup Baik |
| 60,00 – 64,99 | C+ | 2,30 | Cukup |
| 55,00 – 59,99 | C | 2,00 | Cukup |
| 45,00 – 54,99 | D | 1,00 | Kurang |
| 0 – 44,99 | E | 0,00 | Gagal |

**Syarat kelulusan:** nilai akhir ≥ 55,00 **dan** kehadiran ≥ 75%.

---

## 6. Kebijakan Penggunaan AI

### 6.1 Dasar Kebijakan

Pada AI Curriculum Infusion Matrix, mata kuliah ini berstatus **tahap F (Foundation), mode K (Kontekstual)** — tidak ada Sub-CPMK AI tersendiri, dan AI bukan objek pembelajaran.

### 6.2 Tabel Izin

| Kegiatan | Status | Ketentuan |
|----------|--------|-----------|
| Memahami konsep, mencari penjelasan alternatif | **Diizinkan** | Bebas |
| Memeriksa ulang hitungan yang sudah dikerjakan sendiri | **Diizinkan** | Hitungan manual harus lebih dulu |
| Membantu menulis atau memperbaiki kode visualisasi | **Diizinkan dengan catatan** | Wajib di AI Usage Log; harus bisa menjelaskan tiap baris |
| Mengerjakan soal latihan atau kuis | **Tidak diizinkan** | Pelanggaran amanah akademik |
| UTS dan UAS | **Tidak diizinkan** | *Closed book* |
| Memilih uji statistik pada proyek | **Tidak diizinkan sebagai penentu** | Keputusan harus dari mahasiswa |
| Menafsirkan hasil uji pada proyek | **Tidak diizinkan sebagai penentu** | Tafsir harus dari mahasiswa |

### 6.3 Format AI Usage Log

Wajib dilampirkan pada setiap laporan lab dan laporan proyek.

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |
| 2 | | | | | |

**Pernyataan wajib:**

> *Saya menyatakan bahwa seluruh perhitungan statistik, pemilihan uji, dan interpretasi hasil dalam pekerjaan ini adalah hasil pemahaman saya sendiri. Penggunaan AI telah saya catat seluruhnya pada tabel di atas. Saya bersedia menjelaskan setiap bagian pekerjaan ini apabila diminta.*
>
> Nama: ______________  NIM: ______________

Laporan tanpa AI Usage Log — termasuk yang menyatakan "tidak memakai AI" tanpa mengisi tabel — dianggap **belum lengkap** dan dikembalikan.

### 6.4 Verifikasi

Dosen berhak meminta mahasiswa menjelaskan bagian mana pun dari pekerjaannya secara lisan. Ketidakmampuan menjelaskan pekerjaan sendiri merupakan indikasi pelanggaran.

---

## 7. Integritas Akademik

### 7.1 Landasan Nilai

Integritas akademik dalam mata kuliah ini berpijak pada **amanah** — apa yang ditulis mahasiswa adalah kesaksian atas pekerjaannya sendiri.

### 7.2 Bentuk Pelanggaran

| No | Pelanggaran | Tingkat |
|----|-------------|---------|
| 1 | Menyalin pekerjaan mahasiswa lain | Berat |
| 2 | Memakai keluaran AI tanpa mencantumkannya di log | Berat |
| 3 | **Memanipulasi atau mengarang data agar hasil signifikan** | **Sangat berat** |
| 4 | **Melaporkan hasil uji yang tidak benar-benar dijalankan** | **Sangat berat** |
| 5 | Membawa alat bantu terlarang ke ujian | Sangat berat |
| 6 | Membiarkan pekerjaan sendiri disalin orang lain | Sedang |

### 7.3 Sanksi

| Tingkat | Sanksi |
|---------|--------|
| Sedang | Teguran tertulis; nilai instrumen dikurangi 50% |
| Berat | Nilai nol pada instrumen terkait |
| Sangat berat | Nilai E untuk mata kuliah; dilaporkan ke Program Studi |

> **Catatan khusus statistika.** Butir 3 dan 4 adalah pelanggaran paling khas — dan paling berbahaya — pada mata kuliah ini, karena merusak hal yang justru hendak diajarkan: **kejujuran dalam menghadapi ketidakpastian**.
>
> Hasil yang "tidak signifikan" adalah temuan yang sah dan **tidak mengurangi nilai sedikit pun**. Yang dinilai adalah ketepatan prosedur dan kejujuran interpretasi.

---

## 8. Kebijakan Keterlambatan dan Susulan

### 8.1 Keterlambatan Tugas

| Keterlambatan | Pengurangan |
|---------------|-------------|
| ≤ 24 jam | −10% |
| 24–48 jam | −25% |
| 48–72 jam | −50% |
| > 72 jam | Tidak dinilai |

### 8.2 Susulan

| Instrumen | Ketentuan Susulan |
|-----------|-------------------|
| Kuis | Hanya dengan surat keterangan sah, maksimal 7 hari |
| Lab | Mengikuti kebijakan keterlambatan di atas |
| UTS/UAS | Hanya dengan surat keterangan sah, maksimal 7 hari, soal berbeda |
| Presentasi proyek | Tidak ada susulan; kelompok menyesuaikan pembagian peran |

Alasan yang diterima: sakit dengan surat dokter, tugas resmi institusi dengan surat penugasan, kedaruratan keluarga dengan bukti pendukung.

---

## 9. Umpan Balik

| Instrumen | Waktu Umpan Balik | Bentuk |
|-----------|-------------------|--------|
| Laporan lab | Maksimal 7 hari | Komentar tertulis pada LMS |
| Kuis | Pertemuan berikutnya | Pembahasan di kelas |
| Proposal proyek | Maksimal 5 hari | Komentar tertulis + persetujuan/revisi |
| UTS | Pertemuan Minggu 9 | Pembahasan soal di kelas |
| Presentasi proyek | Langsung saat tanya jawab | Lisan + rubrik tertulis |
| UAS | Sesuai kalender akademik | Nilai; berkas dapat dilihat saat periode sanggah |

---

## 10. Evaluasi Mata Kuliah

| Siklus | Kegiatan | Waktu |
|--------|----------|-------|
| Tengah semester | Rekap capaian dari UTS dan Kuis 1–2; penyesuaian kecepatan materi | Minggu 9 |
| Akhir semester | Rekap ketuntasan kedua Sub-CPMK; analisis butir soal | Minggu 17 |
| Pelaporan | Laporan ketuntasan Sub-CPMK ke Program Studi | Minggu 17 |
| Penyelarasan | Koordinasi dengan pengampu Analisis Data Statistik (Sem 2) | Antar semester |

### Indikator Keberhasilan

| Indikator | Target |
|-----------|--------|
| Ketuntasan `PS-Sub-CPMK081-1` | ≥ 75% mahasiswa mencapai ≥ 60 |
| Ketuntasan `PS-Sub-CPMK102-1` | ≥ 75% mahasiswa mencapai ≥ 60 |
| Kelulusan mata kuliah (≥ C) | ≥ 80% |
| Penyerahan lab tepat waktu | ≥ 85% |
| Proyek dengan asumsi diperiksa | ≥ 70% kelompok |
| Kelengkapan AI Usage Log | 100% laporan |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
