# Kisi-Kisi Ujian Tengah Semester (UTS)

## Mata Kuliah: Analisis Data Statistik
### Prodi Informatika — UAI — Semester Genap 2025/2026

---

## Informasi Umum

| Komponen | Detail |
|----------|--------|
| **Waktu** | Minggu 8, 100 menit |
| **Format** | Closed-book, written exam (tanpa akses AI/internet) |
| **Cakupan** | Minggu 1-7 (CPMK 1-4) |
| **Bobot** | 20% dari nilai akhir |
| **Alat yang diizinkan** | Kalkulator non-programmable, alat tulis |

---

## Distribusi Soal

| Tipe Soal | Jumlah | Bobot | Bloom's |
|-----------|--------|-------|---------|
| Pilihan Ganda | 10 soal | 20% | C1-C3 |
| Hitungan Step-by-Step | 3-4 soal | 40% | C3-C4 |
| Interpretasi Output | 2 soal | 20% | C3-C4 |
| Essay Analisis Kasus | 1 soal | 20% | C4 |

---

## Kisi-Kisi Detail per Topik

### Minggu 1: Pengantar Statistika di Era AI (CPMK-1)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Menjelaskan peran statistika dalam data science dan AI | C2 | PG |
| Membedakan tipe data (nominal, ordinal, interval, rasio) | C2 | PG |
| Mengidentifikasi isu etika dalam penggunaan data | C2 | PG/Essay |

**Contoh soal PG:**
> Manakah yang merupakan data berskala rasio?
> A. Tingkat kepuasan (sangat puas, puas, cukup, kurang)
> B. Nomor punggung pemain sepak bola
> C. Suhu dalam Celsius
> D. Berat badan dalam kilogram
>
> **Jawaban: D** — Berat badan memiliki nol mutlak, sehingga operasi rasio bermakna.

---

### Minggu 2: Statistika Deskriptif (CPMK-2)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Menghitung mean, median, modus dari data | C3 | Hitungan |
| Menghitung range, variance, standard deviation, IQR | C3 | Hitungan |
| Memilih ukuran pemusatan yang tepat untuk distribusi tertentu | C4 | PG/Essay |
| Mengidentifikasi outlier menggunakan metode IQR | C3 | Hitungan |

**Contoh soal hitungan:**
> Diberikan data nilai ujian 10 mahasiswa: 65, 70, 72, 75, 75, 78, 80, 82, 85, 95
>
> a. Hitung mean, median, dan modus (5 poin)
> b. Hitung Q1, Q3, dan IQR (5 poin)
> c. Tentukan batas outlier dan identifikasi apakah ada outlier (5 poin)
> d. Jika outlier dihapus, bagaimana mean berubah? Jelaskan mengapa. (5 poin)
>
> **Jawaban:**
> a. Mean = (65+70+72+75+75+78+80+82+85+95)/10 = 77.7; Median = (75+78)/2 = 76.5; Modus = 75
> b. Q1 = 72; Q3 = 82; IQR = 82-72 = 10
> c. Batas bawah = 72-1.5(10) = 57; Batas atas = 82+1.5(10) = 97. Tidak ada outlier.
> d. Tidak ada outlier yang dihapus. Jika 95 dihapus (meskipun bukan outlier), mean turun menjadi 75.8 karena mean sensitif terhadap nilai ekstrem.

---

### Minggu 3: Visualisasi Data (CPMK-2)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Memilih jenis chart yang tepat untuk tipe data tertentu | C3 | PG |
| Mengidentifikasi misleading visualization | C4 | PG/Interpretasi |
| Menginterpretasi informasi dari chart yang diberikan | C3 | Interpretasi |

**Contoh soal PG:**
> Untuk menunjukkan distribusi frekuensi variabel kontinu, chart yang paling tepat adalah:
> A. Pie chart
> B. Bar chart
> C. Histogram
> D. Line chart
>
> **Jawaban: C** — Histogram dirancang khusus untuk menampilkan distribusi frekuensi data kontinu.

---

### Minggu 4: Probabilitas Dasar (CPMK-3)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Menghitung probabilitas dasar (complement, addition rule) | C3 | Hitungan |
| Menghitung conditional probability | C3 | Hitungan |
| Menerapkan Bayes' theorem | C3-C4 | Hitungan |

**Contoh soal hitungan:**
> Sebuah penyakit langka memiliki prevalensi 1% di populasi. Tes diagnostik memiliki sensitivitas 95% (true positive rate) dan spesifisitas 90% (true negative rate).
>
> a. Jika seseorang dites positif, berapa probabilitas dia benar-benar sakit? (10 poin)
> b. Mengapa hasilnya mungkin mengejutkan? Jelaskan fenomena ini. (5 poin)
>
> **Jawaban:**
> a. P(Sakit|Positif) = P(Positif|Sakit)×P(Sakit) / P(Positif)
>    = (0.95 × 0.01) / (0.95 × 0.01 + 0.10 × 0.99)
>    = 0.0095 / (0.0095 + 0.099) = 0.0095 / 0.1085 ≈ 0.0876 ≈ 8.76%
> b. Meskipun tes positif, probabilitas benar-benar sakit hanya ~9%. Ini karena prevalensi penyakit sangat rendah (1%), sehingga false positives (10% dari 99% sehat) jauh lebih banyak daripada true positives (95% dari 1% sakit). Ini disebut base rate fallacy.

---

### Minggu 5: Distribusi Probabilitas (CPMK-3)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Mengidentifikasi distribusi yang sesuai untuk situasi tertentu | C3 | PG |
| Menghitung probabilitas menggunakan distribusi Normal (z-score) | C3 | Hitungan |
| Menjelaskan Central Limit Theorem | C2 | Essay/PG |

**Contoh soal hitungan:**
> Tinggi badan mahasiswa di UAI berdistribusi normal dengan μ = 168 cm dan σ = 6 cm.
>
> a. Berapa probabilitas mahasiswa memiliki tinggi badan > 180 cm? (5 poin)
> b. Berapa tinggi badan yang merupakan persentil ke-90? (5 poin)
>
> **Jawaban:**
> a. z = (180-168)/6 = 2.0; P(Z > 2.0) = 1 - 0.9772 = 0.0228 ≈ 2.28%
> b. z untuk P90 = 1.28; X = μ + zσ = 168 + 1.28(6) = 175.68 cm

---

### Minggu 6: Sampling dan Estimasi (CPMK-4)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Membedakan jenis-jenis teknik sampling | C2 | PG |
| Menghitung confidence interval untuk mean | C3 | Hitungan |
| Menginterpretasi confidence interval dengan benar | C4 | PG/Essay |

**Contoh soal PG:**
> Interpretasi yang BENAR dari "95% confidence interval untuk rata-rata gaji adalah (5.2 juta, 6.8 juta)" adalah:
> A. 95% pegawai memiliki gaji antara 5.2 dan 6.8 juta
> B. Rata-rata gaji populasi pasti berada di interval ini
> C. Jika kita mengulang sampling berkali-kali, 95% interval yang dihasilkan akan mengandung rata-rata populasi
> D. Ada 95% probabilitas rata-rata gaji populasi di interval ini
>
> **Jawaban: C** — CI adalah pernyataan tentang prosedur, bukan tentang parameter tunggal.

---

### Minggu 7: Uji Hipotesis (CPMK-4)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Merumuskan H₀ dan H₁ | C3 | Hitungan |
| Melaksanakan t-test dan menginterpretasi hasilnya | C4 | Hitungan/Interpretasi |
| Menjelaskan p-value dengan benar | C4 | PG/Essay |
| Membedakan Type I dan Type II error | C4 | PG |

**Contoh soal interpretasi output:**
> Diberikan output Python berikut dari uji hipotesis:
> ```
> Ttest_1sampResult(statistic=2.45, pvalue=0.021)
> Sample mean: 73.5
> Population mean (H₀): 70
> Sample size: 30
> ```
>
> a. Tuliskan H₀ dan H₁ (3 poin)
> b. Dengan α = 0.05, apa keputusan Anda? (3 poin)
> c. Apa artinya secara praktis? (4 poin)
> d. Jelaskan apa yang dimaksud p-value = 0.021 dalam konteks ini (5 poin)
>
> **Jawaban:**
> a. H₀: μ = 70; H₁: μ ≠ 70
> b. p-value (0.021) < α (0.05), maka tolak H₀
> c. Terdapat bukti statistik bahwa rata-rata populasi berbeda dari 70. Rata-rata sampel 73.5 menunjukkan rata-rata lebih tinggi dari 70.
> d. p-value 0.021 berarti: Jika H₀ benar (rata-rata populasi = 70), probabilitas mendapatkan sampel dengan rata-rata sejauh atau lebih jauh dari 73.5 adalah hanya 2.1%. Karena probabilitas ini kecil (< 5%), kita menolak H₀.

---

## Contoh Soal Essay

> Sebuah perusahaan e-commerce ingin mengetahui apakah tampilan baru website mereka meningkatkan rata-rata waktu kunjungan. Mereka mengumpulkan data dari 50 user random dengan tampilan lama (mean: 4.2 menit, std: 1.5 menit) dan 50 user random dengan tampilan baru (mean: 5.1 menit, std: 1.8 menit).
>
> a. Desain analisis statistik lengkap: rumuskan hipotesis, pilih uji yang tepat, dan jelaskan mengapa (8 poin)
> b. Apa asumsi yang perlu diperiksa? (4 poin)
> c. Jika p-value = 0.003, apa kesimpulan Anda? Diskusikan baik statistical significance maupun practical significance. (8 poin)

---

## Tips Menghadapi UTS

1. **Pahami konsep, bukan hafal rumus** — Fokus pada MENGAPA, bukan hanya BAGAIMANA
2. **Latihan interpretasi** — Banyak soal tentang interpretasi output, bukan hanya hitung
3. **Perhatikan miskonsepsi umum** — Terutama tentang p-value, confidence interval, dan korelasi
4. **Bawa kalkulator** — Pastikan kalkulator berfungsi dan Anda tahu cara pakainya
5. **Manajemen waktu** — 100 menit untuk ~16 soal, rata-rata 6 menit per soal

---

*Kisi-kisi ini merupakan panduan cakupan materi. Soal ujian sebenarnya mungkin bervariasi dalam format dan tingkat kesulitan.*
