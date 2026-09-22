# Minggu 16: Tinjauan dan Ujian Akhir Semester

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 16 dari 16 |
| Topik | Tinjauan menyeluruh dan pelaksanaan UAS |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` — **bobot 15%** |
| Bloom | C2–C6 |
| Durasi | 150 menit (60' tinjauan + 120' ujian, pada sesi terpisah) |
| Metode | Tinjauan terbimbing · Tes tulis |
| Penilaian | **Tes Tulis UAS (15%)** |

---

## Tujuan Pertemuan

1. Merangkai seluruh materi semester sebagai satu kemampuan utuh.
2. Mengukur capaian `DAIML-Sub-CPMK082-1` melalui tes tulis.
3. Menutup mata kuliah dengan gambaran jalan lanjut.

---

## Bagian I — Tinjauan (60 menit)

### 16.1 Peta Seluruh Semester

```
┌─────────────────────────────────────────────────────────────────┐
│  Sub-CPMK082-1 (60%) — MERANCANG DAN MEMBANGUN MODEL            │
├─────────────────────────────────────────────────────────────────┤
│  Mg 1  Lanskap AI; kapan ML TIDAK dipakai                       │
│  Mg 2  Formulasi task; baseline                                 │
│  Mg 6  Regresi: linear, Ridge, Lasso                            │
│  Mg 7  Klasifikasi: logistik, k-NN                              │
│  Mg 9  Pohon keputusan; Random Forest; boosting                 │
│  Mg 10 SVM; Naive Bayes; pemilihan model                        │
│  Mg 11 Clustering; deteksi anomali                              │
│  Mg 13 Jaringan saraf tiruan                                    │
│  Mg 14 AI generatif; AI bertanggung jawab                       │
└─────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────┐
│  Sub-CPMK102-1 (40%) — MENYIAPKAN DATA DAN MENGEVALUASI         │
├─────────────────────────────────────────────────────────────────┤
│  Mg 3  Kualitas data; prapemrosesan; Pipeline                   │
│  Mg 4  Pembagian data; enam jenis kebocoran                     │
│  Mg 5  Rekayasa fitur; pemilihan fitur                          │
│  Mg 12 PCA; kurva pembelajaran; visualisasi diagnostik          │
└─────────────────────────────────────────────────────────────────┘
```

### 16.2 Dua Belas Hal yang Wajib Terbawa Keluar

| # | Prinsip |
|---|---------|
| 1 | **ML bukan selalu jawabannya** — lima keadaan menuntut pendekatan lain |
| 2 | Masalah harus **diformulasikan** sebelum kode ditulis |
| 3 | **Metrik dipilih dari dampak kesalahan**, bukan dari kebiasaan |
| 4 | ***Baseline* wajib ada** — angka tanpa pembanding tidak bermakna |
| 5 | **Data menentukan batas atas**; model tidak memunculkan informasi yang tidak ada |
| 6 | **`Pipeline` mencegah kebocoran secara struktural** |
| 7 | **Data uji dipakai sekali**, di paling akhir |
| 8 | **Akurasi menyesatkan** pada data tak seimbang |
| 9 | **Selisih yang lebih kecil daripada simpangan bukan perbedaan** |
| 10 | Bila setara, **pilih model yang lebih sederhana** |
| 11 | **Skor yang terlalu bagus adalah tanda bahaya**, bukan keberhasilan |
| 12 | **Tanggung jawab melekat pada manusia**, tidak dapat dialihkan ke model |

### 16.3 Latihan Tinjauan

Dikerjakan bersama sebelum ujian:

1. **Perancangan solusi:** diberikan deskripsi masalah nyata, rancang solusi ML lengkap — formulasi, data yang dibutuhkan, model kandidat, protokol evaluasi, metrik, dan risiko. *(2 kasus)*
2. **Pemilihan model:** diberikan ciri data dan kebutuhan, tentukan model yang sesuai beserta alasannya. *(4 kasus)*
3. **Perhitungan manual:** *entropy* dan *information gain*; satu langkah maju-mundur JST. *(2 soal)*
4. **Diagnosis:** dari kurva pembelajaran dan tabel hasil, tentukan kondisi model dan tindakannya. *(3 kasus)*
5. **Etika:** diberikan tabel kinerja per kelompok, analisis ketimpangannya dan usulkan tindakan. *(1 kasus)*

---

## Bagian II — Ujian Akhir Semester (120 menit)

### 16.4 Ketentuan Ujian

| Aspek | Ketentuan |
|-------|-----------|
| Bentuk | Tes tulis, ***closed book*** |
| Durasi | 120 menit |
| Alat bantu | **Kalkulator saja** |
| Yang tidak diperkenankan | Catatan, buku, telepon, laptop, **alat bantu AI dalam bentuk apa pun** |
| Bobot | **15%** dari nilai akhir |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` |

### 16.5 Cakupan dan Komposisi

| Bagian | Bobot | Bentuk | Penekanan |
|--------|-------|--------|-----------|
| A. Konsep | 25% | Uraian singkat | Seluruh semester |
| B. **Perancangan solusi** | 45% | Merancang solusi ML untuk masalah baru | Minggu 9–14 |
| C. Perhitungan | 30% | Hitung manual | *Entropy*, *information gain*, langkah JST |

Penekanan ada pada **Sub-CPMK082-1**: kemampuan menganalisis karakteristik masalah dan **merancang** model yang sesuai.

Kisi-kisi rinci beserta contoh soal ada pada [kisi-kisi UAS](../05-assessments/kisi-kisi-uas.md).

### 16.6 Bentuk Soal Bagian B

Bagian terbesar ujian berbentuk perancangan. Contoh bentuknya:

> Sebuah dinas kesehatan provinsi memiliki data kunjungan 40.000 pasien puskesmas selama tiga tahun, mencakup 15 variabel demografis dan klinis. Mereka ingin mengenali pasien yang berisiko tidak kembali untuk pengobatan lanjutan.
>
> (a) Rumuskan menjadi *task* ML: target, jenis *task*, dan **kapan prediksi dibutuhkan**.
> (b) Sebutkan dua fitur yang **tidak boleh** dipakai beserta alasannya.
> (c) Tentukan metrik yang sesuai beserta alasannya, dikaitkan dengan dampak kesalahan.
> (d) Usulkan tiga model kandidat dan alasan pemilihannya.
> (e) Rancang protokol evaluasi yang adil.
> (f) Sebutkan dua risiko etis dan cara menanganinya.

Soal semacam ini **tidak memiliki satu jawaban benar**. Yang dinilai adalah ketepatan penalaran dan kelengkapan pertimbangan.

### 16.7 Yang Diuji dan Yang Tidak

| Diuji | Tidak diuji |
|-------|-------------|
| Merancang solusi untuk masalah yang belum pernah dilihat | Menghafal sintaks pustaka |
| Memilih model dengan alasan yang tepat | Menghafal nilai baku hiperparameter |
| Perhitungan *entropy* dan langkah JST | Menurunkan rumus dari awal |
| Merancang protokol evaluasi yang adil | Menulis program lengkap |
| Menganalisis ketimpangan kinerja antarkelompok | Menghafal nama makalah dan tahunnya |

> Rumus yang dibutuhkan **disediakan pada lembar soal**.

### 16.8 Persiapan yang Disarankan

| Kegiatan | Perkiraan waktu |
|----------|-----------------|
| Membaca ulang Bab 8–13 buku ajar | 5 jam |
| Meninjau kembali Bab 1–7 secara ringkas | 2 jam |
| Mengerjakan Latihan Soal tingkat Mahir tiap bab | 4 jam |
| Berlatih soal perancangan pada kisi-kisi | 4 jam |
| Berlatih perhitungan manual tanpa komputer | 2 jam |

---

## Penutup Mata Kuliah

### 16.9 Apa yang Sudah Dicapai

Mahasiswa yang menyelesaikan mata kuliah ini telah:

- Merumuskan masalah nyata menjadi *task* pembelajaran mesin.
- Menyiapkan data dari keadaan mentah sampai siap dilatih, tanpa kebocoran.
- Membangun dan membandingkan sekurang-kurangnya enam jenis model.
- Mengevaluasi model dengan metrik yang sesuai dan protokol yang adil.
- Mengaudit keadilan model sendiri dan mendokumentasikannya.
- Menghasilkan satu proyek utuh yang dapat dijalankan ulang dan ditunjukkan sebagai portofolio.

### 16.10 Jalan Lanjut

| Minat | Mata kuliah berikutnya |
|-------|------------------------|
| Arsitektur *deep learning* | Jaringan Syaraf Tiruan dan Pembelajaran Mendalam (IF52510032) |
| Alur data dan skala besar | Sains Data |
| Teks dan bahasa | Pengolahan Bahasa Alami (IF52510024) |
| Citra dan penglihatan komputer | Pengolahan Citra (IF52510016) |
| Representasi pengetahuan | Web Semantik (IF52510003) |
| Penelitian mandiri | Metodologi Penelitian → Tugas Akhir |

### 16.11 Kebiasaan yang Layak Dilanjutkan

1. **Selalu bangun *baseline* lebih dahulu**, pada pekerjaan apa pun.
2. **Curigai skor yang terlalu bagus** sebelum merayakannya.
3. **Ukur kinerja per kelompok**, bukan hanya agregat.
4. **Catat keputusan dan alasannya**, termasuk yang ternyata keliru.
5. **Nyatakan keterbatasan** sebelum orang lain menemukannya.

---

## Rangkuman

1. Semester ini terbagi dua: **membangun** (082-1, 60%) dan **menyiapkan-mengevaluasi** (102-1, 40%).
2. Dua belas prinsip §16.2 adalah inti yang layak dibawa keluar.
3. UAS menekankan **perancangan solusi** (45%) untuk masalah yang belum pernah dilihat.
4. Soal perancangan **tidak memiliki satu jawaban benar** — yang dinilai adalah penalarannya.
5. Rumus disediakan; yang diuji adalah **pemakaian dan penafsirannya**.

---

## Referensi

1. Seluruh referensi Minggu 1–15.
2. [Kisi-kisi UAS](../05-assessments/kisi-kisi-uas.md).
3. [Kerangka asesmen](../05-assessments/assessment-framework.md).
4. [Penutup buku ajar](../06-buku-ajar/penutup.md).
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
