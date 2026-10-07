# Minggu 8: Tinjauan dan Ujian Tengah Semester

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 8 dari 16 |
| Topik | Tinjauan menyeluruh Minggu 1–7 dan pelaksanaan UTS |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` — **bobot 20%** |
| Bloom | C2–C4 |
| Durasi | 150 menit (60' tinjauan + 120' ujian, pada sesi terpisah) |
| Metode | Tinjauan terbimbing · Tes tulis |
| Penilaian | **Tes Tulis UTS (20%)** |

---

## Tujuan Pertemuan

1. Merangkai kembali materi Minggu 1–7 sebagai satu kesatuan alur, bukan tujuh topik terpisah.
2. Mengenali kesalahan yang paling sering terjadi dan cara menghindarinya.
3. Mengukur capaian `DAIML-Sub-CPMK102-1` melalui tes tulis.

---

## Bagian I — Tinjauan (60 menit)

### 8.1 Merangkai Tujuh Minggu Menjadi Satu Alur

```
 Mg 1        Mg 2         Mg 3-5              Mg 6-7
┌──────┐   ┌────────┐   ┌──────────────┐   ┌─────────────┐
│ APA  │──►│ MASALAH│──►│    DATA      │──►│   MODEL     │
│ ITU  │   │  APA   │   │              │   │             │
│ ML?  │   │        │   │ • kualitas   │   │ • regresi   │
│      │   │ • task │   │ • bocor      │   │ • klasifi-  │
│ Kapan│   │ • metrik│  │ • fitur      │   │   kasi      │
│ TIDAK│   │ • base- │  │              │   │ • metrik    │
│ pakai│   │   line  │  │              │   │             │
└──────┘   └────────┘   └──────────────┘   └─────────────┘
    │           │              │                   │
    └───────────┴──────────────┴───────────────────┘
                          │
                 Setiap tahap dapat
                 menggagalkan tahap
                 berikutnya
```

Pesan pokok tinjauan: **kesalahan pada tahap awal tidak dapat diperbaiki oleh tahap berikutnya**. Model tercanggih tidak menyelamatkan formulasi masalah yang keliru; metrik terbaik tidak menyelamatkan data yang bocor.

### 8.2 Ringkasan per Minggu

| Mg | Inti yang wajib dikuasai |
|----|--------------------------|
| 1 | AI ⊃ ML ⊃ DL; tiga paradigma; **lima keadaan ML tidak dipakai** |
| 2 | Tujuh pertanyaan formulasi; metrik dari dampak kesalahan; ***baseline* wajib** |
| 3 | Pola nilai hilang (MCAR/MAR/MNAR); nominal vs ordinal; **`Pipeline` mencegah kebocoran** |
| 4 | Tiga peran data; strategi pembagian; **enam jenis kebocoran** |
| 5 | Fitur menentukan batas atas; pemilihan fitur wajib di dalam `Pipeline`; kutukan dimensi |
| 6 | Ridge vs Lasso; MAE vs RMSE; **bias–varians** |
| 7 | Matriks konfusi; *precision* vs *recall*; **akurasi menyesatkan**; ambang dari biaya |

### 8.3 Sepuluh Kesalahan yang Paling Sering Terjadi

| # | Kesalahan | Akibat | Pencegahan |
|---|-----------|--------|------------|
| 1 | Melatih model sebelum masalah dirumuskan | Model menjawab pertanyaan yang salah | Tujuh pertanyaan §Mg2 |
| 2 | Tidak ada *baseline* | Angka kinerja tidak bermakna | `DummyClassifier`/`DummyRegressor` |
| 3 | `fit` pada seluruh data sebelum pembagian | Kebocoran prapemrosesan | `Pipeline` |
| 4 | Pembagian acak pada data deret waktu | Kebocoran temporal | `TimeSeriesSplit` |
| 5 | Memilih fitur di luar `Pipeline` | Kebocoran pemilihan | `SelectKBest` di dalam `Pipeline` |
| 6 | Memberi nomor pada data nominal | Model menganggap ada urutan | `OneHotEncoder` |
| 7 | Melaporkan akurasi saja pada data tak seimbang | Kesimpulan menyesatkan | F1, PR-AUC, *recall* per kelas |
| 8 | Memakai data uji berkali-kali | Kebocoran pemilihan berulang | Data uji dipakai **sekali** |
| 9 | Merayakan skor yang sangat tinggi | Kebocoran yang tidak terdeteksi | **Curigai lebih dahulu** |
| 10 | Menulis "X menyebabkan Y" dari data observasional | Klaim melampaui rancangan | "dikaitkan dengan" |

### 8.4 Latihan Tinjauan

Dikerjakan bersama di kelas sebelum ujian:

1. Diberikan potongan kode, temukan kebocorannya dan jelaskan mekanismenya. *(3 kasus)*
2. Diberikan matriks konfusi, hitung seluruh metrik dan tentukan mana yang paling sesuai kasusnya. *(2 kasus)*
3. Diberikan deskripsi masalah nyata, rumuskan menjadi *task* ML lengkap. *(2 kasus)*
4. Diberikan pasangan galat latih dan validasi, diagnosis kondisi model dan tentukan tindakannya. *(4 kasus)*

---

## Bagian II — Ujian Tengah Semester (120 menit)

### 8.5 Ketentuan Ujian

| Aspek | Ketentuan |
|-------|-----------|
| Bentuk | Tes tulis, ***closed book*** |
| Durasi | 120 menit |
| Alat bantu | **Kalkulator saja** |
| Yang tidak diperkenankan | Catatan, buku, telepon, laptop, **alat bantu AI dalam bentuk apa pun** |
| Bobot | **20%** dari nilai akhir |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` |

### 8.6 Cakupan dan Komposisi

| Bagian | Bobot | Bentuk | Materi |
|--------|-------|--------|--------|
| A. Konsep | 30% | Uraian singkat | Minggu 1–7 |
| B. Analisis kasus | 40% | Analisis kode/skenario | Kebocoran, pemilihan metrik, diagnosis model |
| C. Perhitungan | 30% | Hitung manual | Matriks konfusi, metrik regresi dan klasifikasi |

Penekanan ada pada **Sub-CPMK102-1**: penyiapan data, pembagian tanpa kebocoran, pemilihan metrik, dan penafsiran hasil.

Kisi-kisi rinci beserta contoh soal ada pada [kisi-kisi UTS](../05-assessments/kisi-kisi-uts.md).

### 8.7 Yang Diuji dan Yang Tidak

| Diuji | Tidak diuji |
|-------|-------------|
| Penalaran atas prosedur | Hafalan nama fungsi |
| Perhitungan metrik manual | Sintaks lengkap `scikit-learn` |
| Menemukan kebocoran dari potongan kode | Menulis program panjang dari nol |
| Memilih metrik beserta alasannya | Menghafal nilai baku hiperparameter |
| Mendiagnosis kondisi model | Menghafal rumus turunan gradien |

> Rumus metrik yang dibutuhkan **disediakan pada lembar soal**. Yang diuji adalah kemampuan memakainya dengan tepat dan menafsirkan hasilnya — bukan kemampuan menghafalnya.

### 8.8 Persiapan yang Disarankan

| Kegiatan | Perkiraan waktu |
|----------|-----------------|
| Membaca ulang Bab 1–7 buku ajar | 5 jam |
| Mengerjakan Latihan Soal tingkat Menengah tiap bab | 4 jam |
| Mengerjakan contoh soal pada kisi-kisi | 3 jam |
| Meninjau kembali lab yang sudah dikerjakan | 2 jam |
| Berlatih perhitungan manual tanpa komputer | 2 jam |

Baris terakhir yang paling sering dilewati dan paling menentukan. Perhitungan metrik pada ujian dikerjakan dengan kalkulator, bukan dengan `scikit-learn`.

---

## Setelah Ujian

- Melanjutkan proyek kelompok; Milestone 2 jatuh tempo Minggu 11.
- Mengerjakan T-07 yang jatuh tempo pada pertemuan Minggu 9.
- Membaca [Bab 8](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md) untuk persiapan Minggu 9.

---

## Rangkuman

1. Tujuh minggu pertama membentuk **satu alur**: apa itu ML → masalah apa → data → model.
2. **Kesalahan pada tahap awal tidak dapat diperbaiki oleh tahap berikutnya.**
3. Sepuluh kesalahan pada §8.3 mencakup sebagian besar kekeliruan yang terjadi di lapangan.
4. UTS menguji **penalaran**, bukan hafalan; rumus disediakan.
5. Perhitungan manual wajib dilatih — ujian bersifat *closed book* tanpa komputer.

---

## Referensi

1. Seluruh referensi Minggu 1–7.
2. [Kisi-kisi UTS](../05-assessments/kisi-kisi-uts.md).
3. [Kerangka asesmen](../05-assessments/assessment-framework.md).
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
