# Minggu 8: Review dan Ujian Tengah Semester (UTS)

## Mata Kuliah: Analisis Data Statistik
### Prodi Informatika — Universitas Al Azhar Indonesia — Semester Genap 2025/2026

---

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Minggu** | 8 |
| **Topik** | Review Materi Minggu 1-7 dan Ujian Tengah Semester |
| **CPMK** | CPMK 1-4 (seluruh capaian pembelajaran paruh pertama semester) |
| **Bloom's Taxonomy** | C2-C4 (Understand, Apply, Analyze) |
| **Durasi UTS** | 100 menit |
| **Format** | Closed-book, written exam (individual, tanpa AI) |
| **Cakupan** | Seluruh materi Minggu 1-7 |

---

## Tujuan Modul Review

1. **Memetakan** seluruh materi Minggu 1-7 dalam satu kerangka terintegrasi
2. **Mengidentifikasi** area yang masih lemah dan perlu dipelajari ulang
3. **Berlatih** mengerjakan soal setipe UTS
4. **Memahami** format dan ekspektasi ujian

---

## Bagian 1: Peta Konsep — Seluruh Materi Minggu 1-7

```
ANALISIS DATA STATISTIK — PETA KONSEP PARUH PERTAMA
════════════════════════════════════════════════════

Minggu 1: FONDASI
├── Peran statistika di era AI & data science
├── Tools: Python, Colab, pandas, AI assistants
├── Tipe data: nominal, ordinal, interval, rasio
└── Etika data: privacy, bias, consent, responsible AI

        ↓ "Setelah tahu mengapa, sekarang eksplorasi data"

Minggu 2: STATISTIKA DESKRIPTIF
├── Ukuran Pemusatan: mean, median, modus
├── Ukuran Penyebaran: range, variance, std, IQR
├── Skewness & kurtosis
└── Tools: pandas (describe, info), numpy

        ↓ "Data sudah dieksplorasi, sekarang visualisasikan"

Minggu 3: VISUALISASI DATA
├── Prinsip visualisasi efektif (Tufte)
├── matplotlib: line, bar, scatter, histogram
├── seaborn: boxplot, violin, heatmap, pairplot
└── Storytelling with data: chart → insight → narasi

        ↓ "Dari data ke ketidakpastian"

Minggu 4: PROBABILITAS DASAR
├── Probabilitas dasar, conditional probability
├── Independence
├── Bayes' Theorem: P(A|B) = P(B|A)P(A) / P(B)
└── Simulasi probabilitas dengan Python

        ↓ "Dari probabilitas ke distribusi"

Minggu 5: DISTRIBUSI PROBABILITAS & CLT
├── Diskret: Binomial (n,p), Poisson (λ)
├── Kontinu: Normal (μ,σ), Uniform (a,b)
├── Z-score: z = (x - μ) / σ
├── Central Limit Theorem: X̄ ~ Normal(μ, σ/√n)
└── scipy.stats: pdf, cdf, ppf, rvs

        ↓ "CLT memungkinkan inferensi"

Minggu 6: SAMPLING & ESTIMASI
├── Teknik: SRS, stratified, systematic, cluster
├── Standard Error: SE = s / √n
├── Point vs Interval Estimation
├── Confidence Interval: x̄ ± t* × SE
├── Interpretasi CI yang BENAR
└── Bootstrap method: resampling

        ↓ "Dari estimasi ke pengujian"

Minggu 7: UJI HIPOTESIS
├── H₀ vs H₁, significance level (α)
├── z-test, one-sample t-test
├── Two-sample t-test: independent & paired
├── p-value: interpretasi BENAR (3 miskonsepsi)
├── Type I Error (α), Type II Error (β), Power
└── Effect Size: Cohen's d
```

---

## Bagian 2: Checklist "Apa yang Harus Dikuasai"

### CPMK-1: Peran Statistika dan Etika (Minggu 1)

| No | Topik | Sudah Paham? |
|----|-------|:------------:|
| 1 | Menjelaskan mengapa statistik penting di era AI dan data science | [ ] |
| 2 | Menyebutkan dan menjelaskan fungsi tools modern (Python, Colab, pandas) | [ ] |
| 3 | Membedakan tipe data: nominal, ordinal, interval, rasio | [ ] |
| 4 | Menjelaskan prinsip etika data: privacy, bias, informed consent | [ ] |
| 5 | Menjelaskan apa itu responsible AI dan mengapa penting | [ ] |

### CPMK-2: Statistika Deskriptif dan Visualisasi (Minggu 2-3)

| No | Topik | Sudah Paham? |
|----|-------|:------------:|
| 6 | Menghitung mean, median, modus dari data | [ ] |
| 7 | Menghitung range, variance, standard deviation, IQR | [ ] |
| 8 | Menjelaskan skewness (positive, negative, symmetric) | [ ] |
| 9 | Mengidentifikasi outlier menggunakan IQR method | [ ] |
| 10 | Memilih tipe chart yang tepat untuk data tertentu | [ ] |
| 11 | Membaca dan menginterpretasi boxplot | [ ] |
| 12 | Membuat dan menginterpretasi histogram, scatter plot, bar chart | [ ] |
| 13 | Menggunakan pandas: `describe()`, `info()`, `value_counts()` | [ ] |
| 14 | Menggunakan matplotlib dan seaborn untuk visualisasi | [ ] |

### CPMK-3: Probabilitas dan Distribusi (Minggu 4-5)

| No | Topik | Sudah Paham? |
|----|-------|:------------:|
| 15 | Menghitung probabilitas dasar (P(A), P(A or B), P(A and B)) | [ ] |
| 16 | Menghitung conditional probability P(A given B) | [ ] |
| 17 | Menerapkan Bayes' Theorem | [ ] |
| 18 | Mengidentifikasi kapan pakai Binomial vs Poisson | [ ] |
| 19 | Menghitung probabilitas Binomial: P(X=k) | [ ] |
| 20 | Menghitung probabilitas Poisson: P(X=k) | [ ] |
| 21 | Menyebutkan sifat distribusi Normal (bell curve, 68-95-99.7) | [ ] |
| 22 | Menghitung dan menginterpretasi z-score | [ ] |
| 23 | Menjelaskan Central Limit Theorem dalam kata-kata sendiri | [ ] |
| 24 | Menggunakan scipy.stats: pdf/pmf, cdf, ppf, rvs | [ ] |

### CPMK-4: Inferensi Statistik (Minggu 6-7)

| No | Topik | Sudah Paham? |
|----|-------|:------------:|
| 25 | Membedakan populasi vs sampel, parameter vs statistik | [ ] |
| 26 | Menyebutkan kelebihan/kekurangan teknik sampling | [ ] |
| 27 | Menghitung Standard Error (SE = s / sqrt(n)) | [ ] |
| 28 | Menghitung Confidence Interval | [ ] |
| 29 | Menginterpretasi CI dengan **BENAR** (bukan "95% peluang mu ada di CI") | [ ] |
| 30 | Menjelaskan konsep bootstrap | [ ] |
| 31 | Memformulasikan H0 dan H1 | [ ] |
| 32 | Memilih uji yang tepat (z-test, one-sample t, independent t, paired t) | [ ] |
| 33 | Menginterpretasi p-value dengan BENAR (bukan "P(H0 benar)") | [ ] |
| 34 | Menjelaskan Type I Error, Type II Error, Power | [ ] |
| 35 | Menghitung dan menginterpretasi Cohen's d | [ ] |

**Target:** Jika kamu bisa mencentang semua 35 topik di atas, kamu siap UTS!

---

## Bagian 3: Rumus-Rumus Penting (Formula Sheet)

Berikut rangkuman rumus yang perlu dipahami (bukan dihafal — pahami **kapan** dan **mengapa**):

### Statistika Deskriptif

```
Mean:       x̄ = (Σxᵢ) / n
Variance:   s² = Σ(xᵢ - x̄)² / (n - 1)
Std Dev:    s = √(s²)
IQR:        IQR = Q3 - Q1
Outlier:    x < Q1 - 1.5×IQR  atau  x > Q3 + 1.5×IQR
```

### Probabilitas

```
P(A or B) = P(A) + P(B) - P(A and B)
P(A and B) = P(A) × P(B|A)
P(A|B) = P(B|A) × P(A) / P(B)          ← Bayes' Theorem
```

### Distribusi

```
Binomial:   P(X=k) = C(n,k) × p^k × (1-p)^(n-k)
            Mean = np, Var = np(1-p)

Poisson:    P(X=k) = (λ^k × e^(-λ)) / k!
            Mean = λ, Var = λ

Normal:     68-95-99.7 rule (μ ± 1σ, 2σ, 3σ)

Z-score:    z = (x - μ) / σ
```

### Inferensi

```
Standard Error:     SE = s / √n
Confidence Int.:    CI = x̄ ± t* × (s / √n)
t-statistic:        t = (x̄ - μ₀) / (s / √n)        [one-sample]
                    t = (x̄₁ - x̄₂) / SE_pooled       [two-sample]
Cohen's d:          d = (x̄₁ - x̄₂) / s_pooled
```

---

## Bagian 4: Contoh Soal Latihan UTS (10 Soal dengan Jawaban)

### Soal 1: Tipe Data (C2 — Understand)

**Soal:** Klasifikasikan masing-masing variabel berikut ke dalam tipe data yang tepat (nominal, ordinal, interval, rasio):
- a) Golongan darah mahasiswa (A, B, AB, O)
- b) Tingkat kepuasan (Sangat Tidak Puas, Tidak Puas, Netral, Puas, Sangat Puas)
- c) Suhu udara dalam Celsius
- d) Penghasilan bulanan dalam Rupiah

**Jawaban:**
- a) **Nominal** — kategori tanpa urutan
- b) **Ordinal** — ada urutan, tapi jarak antar level tidak tentu sama
- c) **Interval** — ada urutan dan jarak sama, tapi 0 derajat Celsius bukan berarti "tidak ada suhu"
- d) **Rasio** — ada urutan, jarak sama, dan 0 Rupiah berarti benar-benar tidak ada penghasilan

---

### Soal 2: Statistika Deskriptif (C3 — Apply)

**Soal:** Diberikan data nilai kuis 10 mahasiswa: 45, 52, 60, 62, 65, 68, 70, 75, 78, 95

a) Hitung mean, median, Q1, Q3, dan IQR
b) Apakah ada outlier? Tunjukkan dengan metode IQR
c) Apakah data cenderung skewed? Ke arah mana?

**Jawaban:**

a) Perhitungan:
```
Data terurut: 45, 52, 60, 62, 65, 68, 70, 75, 78, 95

Mean = (45+52+60+62+65+68+70+75+78+95) / 10 = 670/10 = 67.0
Median = (65+68) / 2 = 66.5

Q1 = median dari 5 data bawah {45,52,60,62,65} = 60
Q3 = median dari 5 data atas {68,70,75,78,95} = 75
IQR = Q3 - Q1 = 75 - 60 = 15
```

b) Batas outlier:
```
Lower fence = Q1 - 1.5 × IQR = 60 - 22.5 = 37.5
Upper fence = Q3 + 1.5 × IQR = 75 + 22.5 = 97.5

Semua data berada dalam [37.5, 97.5] → TIDAK ADA OUTLIER
(Catatan: 95 mendekati upper fence tapi masih di dalam batas)
```

c) Mean (67.0) > Median (66.5) menunjukkan sedikit **positive skew** (ekor ke kanan), karena ada nilai tinggi 95 yang menarik mean ke atas.

---

### Soal 3: Visualisasi (C2 — Understand)

**Soal:** Untuk masing-masing situasi berikut, chart apa yang paling tepat?
- a) Membandingkan distribusi nilai ujian 3 kelas
- b) Melihat hubungan antara jam belajar dan nilai ujian
- c) Melihat proporsi mahasiswa per prodi
- d) Melihat distribusi frekuensi usia mahasiswa

**Jawaban:**
- a) **Box plot** (atau violin plot) — efektif membandingkan distribusi beberapa kelompok
- b) **Scatter plot** — menampilkan hubungan dua variabel numerik
- c) **Bar chart** (atau pie chart untuk sedikit kategori) — menampilkan proporsi kategori
- d) **Histogram** — menampilkan distribusi frekuensi variabel kontinu

---

### Soal 4: Bayes' Theorem (C3 — Apply)

**Soal:** Di sebuah kampus, 5% mahasiswa positif COVID. Alat rapid test memiliki sensitivitas 90% (benar mendeteksi positif jika memang positif) dan spesifisitas 95% (benar mendeteksi negatif jika memang negatif). Jika seorang mahasiswa dites positif, berapa probabilitas dia benar-benar positif COVID?

**Jawaban:**

```
Diketahui:
  P(COVID) = 0.05
  P(Positif | COVID) = 0.90        ← sensitivitas
  P(Negatif | Sehat) = 0.95        ← spesifisitas
  P(Positif | Sehat) = 1 - 0.95 = 0.05

Ditanya: P(COVID | Positif)

Bayes' Theorem:
  P(COVID | Positif) = P(Positif | COVID) × P(COVID) / P(Positif)

P(Positif) = P(Positif|COVID) × P(COVID) + P(Positif|Sehat) × P(Sehat)
           = 0.90 × 0.05 + 0.05 × 0.95
           = 0.045 + 0.0475
           = 0.0925

P(COVID | Positif) = 0.045 / 0.0925 = 0.4865 ≈ 48.6%

Insight: Meskipun tesnya cukup akurat (90% sensitivitas, 95% spesifisitas),
karena prevalensi COVID rendah (5%), ada peluang ~51% hasil positif
adalah FALSE POSITIVE! Ini menunjukkan pentingnya memahami base rate.
```

---

### Soal 5: Distribusi Probabilitas (C3 — Apply)

**Soal:** Sebuah toko online menerima rata-rata 6 pesanan per jam.

a) Distribusi apa yang tepat untuk memodelkan ini? Mengapa?
b) Berapa probabilitas menerima tepat 4 pesanan dalam 1 jam?
c) Berapa probabilitas menerima lebih dari 8 pesanan dalam 1 jam?

**Jawaban:**

a) **Distribusi Poisson** dengan lambda = 6, karena:
   - Menghitung kejadian (pesanan) dalam interval waktu tertentu (1 jam)
   - Kejadian terjadi secara independen
   - Rata-rata konstan (6 per jam)

b) P(X = 4):
```
P(X=4) = (6^4 × e^(-6)) / 4!
       = (1296 × 0.00248) / 24
       = 3.215 / 24
       = 0.1339 ≈ 13.4%
```

c) P(X > 8) = 1 - P(X <= 8):
```
Ini sulit dihitung manual (perlu jumlahkan P(X=0) sampai P(X=8)).
Menggunakan Python: 1 - stats.poisson.cdf(8, mu=6) ≈ 0.1528 ≈ 15.3%
```

---

### Soal 6: Z-Score (C3 — Apply)

**Soal:** Nilai ujian Statistik berdistribusi Normal dengan mean = 70 dan std = 8.

a) Seorang mahasiswa mendapat 82. Berapa z-score-nya? Apa interpretasinya?
b) Berapa persen mahasiswa mendapat nilai di atas 86?
c) Berapa nilai minimum untuk masuk 10% teratas?

**Jawaban:**

a) z-score:
```
z = (82 - 70) / 8 = 12/8 = 1.5
Interpretasi: Nilai 82 berada 1.5 standard deviation di atas mean.
```

b) P(X > 86):
```
z = (86 - 70) / 8 = 2.0
P(Z > 2.0) = 1 - P(Z <= 2.0) = 1 - 0.9772 = 0.0228 ≈ 2.28%

Sekitar 2.3% mahasiswa mendapat nilai di atas 86.
```

c) Nilai minimum top 10%:
```
Cari z sehingga P(Z <= z) = 0.90 → z = 1.282
x = μ + z × σ = 70 + 1.282 × 8 = 70 + 10.26 = 80.26

Nilai minimum untuk top 10% ≈ 80.3
```

---

### Soal 7: Central Limit Theorem (C2-C3 — Understand-Apply)

**Soal:** Jelaskan Central Limit Theorem dengan bahasa sederhana. Kemudian jawab:
Waktu tunggu di kantin UAI berdistribusi eksponensial (bukan Normal!) dengan mean = 10 menit dan std = 10 menit. Jika diambil 36 mahasiswa secara acak:

a) Berapa mean dan standard error dari distribusi rata-rata sampel?
b) Berapa probabilitas rata-rata waktu tunggu 36 mahasiswa ini lebih dari 12 menit?

**Jawaban:**

CLT dalam bahasa sederhana: "Jika kita mengambil banyak sampel dan menghitung rata-ratanya, distribusi rata-rata sampel tersebut akan mendekati kurva Normal — tidak peduli bentuk distribusi aslinya — asalkan ukuran sampel cukup besar."

a) Berdasarkan CLT:
```
Mean distribusi sampling = μ = 10 menit
Standard Error = σ / √n = 10 / √36 = 10/6 = 1.667 menit
```

b) P(X-bar > 12):
```
Berkat CLT (n=36 cukup besar), X̄ ~ Normal(10, 1.667)
z = (12 - 10) / 1.667 = 2 / 1.667 = 1.20
P(Z > 1.20) = 1 - 0.8849 = 0.1151 ≈ 11.5%
```

---

### Soal 8: Confidence Interval (C3-C4 — Apply-Analyze)

**Soal:** Dari survei 49 mahasiswa UAI, diperoleh rata-rata pengeluaran bulanan Rp 2.500.000 dengan standard deviation Rp 500.000.

a) Hitung 95% confidence interval untuk rata-rata pengeluaran seluruh mahasiswa UAI
b) Interpretasikan CI tersebut dengan **benar**
c) Jika dosen berkata "95% CI berarti ada 95% peluang bahwa rata-rata pengeluaran berada di interval itu" — apakah benar? Jelaskan.

**Jawaban:**

a) Hitung 95% CI:
```
n = 49, x̄ = 2.500.000, s = 500.000
SE = s / √n = 500.000 / √49 = 500.000 / 7 = 71.429

Untuk 95% CI, t* ≈ 2.011 (df=48, tapi bisa juga pakai z*=1.96 karena n besar)
Menggunakan z*=1.96:

CI = x̄ ± z* × SE
   = 2.500.000 ± 1.96 × 71.429
   = 2.500.000 ± 140.000
   = (Rp 2.360.000, Rp 2.640.000)
```

b) Interpretasi yang BENAR:
"Jika kita mengulangi proses sampling (mengambil 49 mahasiswa secara acak) dan menghitung 95% CI berkali-kali, maka 95% dari interval yang dihasilkan akan mengandung rata-rata pengeluaran populasi yang sebenarnya."

c) **Tidak benar.** Rata-rata populasi adalah nilai tetap (fixed), bukan random variable. Interval yang kita hitung adalah satu dari banyak kemungkinan interval. Setelah dihitung, interval tersebut sudah mengandung mu atau tidak — tidak ada "probabilitas 95%." Yang benar adalah **metode-nya** memiliki tingkat keberhasilan 95%, bukan interval spesifik ini.

---

### Soal 9: Uji Hipotesis (C4 — Analyze)

**Soal:** Sebuah klaim menyatakan bahwa rata-rata waktu penyelesaian tugas pemrograman mahasiswa UAI adalah 120 menit. Dosen menduga waktu sebenarnya lebih lama. Dari sampel 25 mahasiswa, diperoleh rata-rata 132 menit dan standard deviation 30 menit (alpha = 0.05).

a) Tuliskan H0 dan H1
b) Uji statistik apa yang digunakan? Mengapa?
c) Hitung t-statistic
d) Jika t_critical (one-tailed, df=24, alpha=0.05) = 1.711, apa kesimpulannya?
e) Hitung Cohen's d dan interpretasikan

**Jawaban:**

a) Hipotesis:
```
H₀: μ = 120 menit (waktu sesuai klaim)
H₁: μ > 120 menit (waktu lebih lama dari klaim) → one-tailed test
```

b) **One-sample t-test**, karena:
- Membandingkan 1 sampel dengan nilai referensi (120)
- sigma populasi tidak diketahui (gunakan s sampel)
- n = 25 (ukuran sampel tidak terlalu besar)

c) Hitung t:
```
t = (x̄ - μ₀) / (s/√n)
  = (132 - 120) / (30/√25)
  = 12 / (30/5)
  = 12 / 6
  = 2.0
```

d) Keputusan:
```
t_hitung (2.0) > t_critical (1.711) → REJECT H₀

Atau equivalently: p-value = P(t > 2.0 | df=24) ≈ 0.028 < 0.05

Kesimpulan: Pada alpha = 0.05, terdapat cukup bukti bahwa rata-rata
waktu penyelesaian tugas lebih lama dari 120 menit.
```

e) Cohen's d:
```
d = (x̄ - μ₀) / s = (132 - 120) / 30 = 12/30 = 0.40

Interpretasi: Effect size kecil-sedang (small-to-medium).
Meskipun signifikan secara statistik, perbedaan 12 menit dari standar
merupakan efek yang berukuran moderate — perlu pertimbangan apakah
ini bermakna secara praktis.
```

---

### Soal 10: Interpretasi Output Python (C4 — Analyze)

**Soal:** Diberikan output Python berikut dari perbandingan nilai ujian Kelas A dan Kelas B:

```
Kelas A: n=30, mean=72.5, std=10.2
Kelas B: n=32, mean=68.3, std=11.5

Welch's t-test:
  t-statistic = 1.527
  p-value = 0.132

Cohen's d = 0.387
```

a) Tuliskan H0 dan H1 yang diuji
b) Pada alpha = 0.05, apa keputusan dan kesimpulannya?
c) Apakah perbedaan antara Kelas A dan Kelas B bermakna secara praktis? Jelaskan dengan mengacu pada effect size
d) Seorang mahasiswa menyimpulkan: "Karena p = 0.132, maka terbukti bahwa Kelas A dan Kelas B memiliki kemampuan yang sama." Apakah kesimpulan ini benar? Jelaskan.

**Jawaban:**

a) Hipotesis:
```
H₀: μ_A = μ_B (tidak ada perbedaan rata-rata nilai)
H₁: μ_A ≠ μ_B (ada perbedaan rata-rata nilai)
```

b) Keputusan:
```
p-value (0.132) > α (0.05) → FAIL TO REJECT H₀

Kesimpulan: Pada tingkat signifikansi 5%, tidak terdapat cukup
bukti untuk menyimpulkan bahwa ada perbedaan rata-rata nilai
antara Kelas A dan Kelas B.
```

c) Effect size:
```
Cohen's d = 0.387 → efek kecil (small, karena 0.2 < 0.387 < 0.5)
Perbedaan mean = 72.5 - 68.3 = 4.2 poin (sekitar 0.39 standard deviasi)
Ini menunjukkan bahwa perbedaan antar kelas cukup kecil secara praktis.
```

d) **Kesimpulan tersebut SALAH.**
"Fail to reject H0" BUKAN berarti "H0 terbukti benar." Artinya hanya: dengan data dan ukuran sampel yang ada, kita tidak memiliki cukup bukti untuk menolak H0. Bisa jadi perbedaan memang ada tapi terlalu kecil untuk terdeteksi dengan n=30-32 (kurang power). Analogi: "not guilty" dalam pengadilan bukan berarti "proven innocent."

---

## Bagian 5: Tips Menghadapi UTS

### 5.1 Strategi Belajar Sebelum UTS

1. **Kerjakan ulang semua Lab (Lab 01-07)** — coba tanpa melihat jawaban
2. **Review catatan dan modul** — fokus pada konsep, bukan hafalan rumus
3. **Kerjakan latihan mandiri** di setiap modul (Minggu 1-7)
4. **Pahami MENGAPA, bukan hanya BAGAIMANA** — UTS menguji pemahaman konseptual
5. **Buat "cheat sheet" satu halaman** — proses membuatnya adalah proses belajar

### 5.2 Strategi Saat Mengerjakan UTS

1. **Baca semua soal dulu** (5 menit pertama) — identifikasi soal mudah vs sulit
2. **Kerjakan soal yang paling dikuasai terlebih dahulu** — amankan nilai
3. **Tulis rumus yang relevan** sebelum menghitung — menunjukkan pemahaman
4. **Tunjukkan langkah kerja** — partial credit diberikan untuk proses yang benar
5. **Kelola waktu:** target alokasi waktu per bagian
6. **Cek ulang jawaban** jika masih ada waktu — terutama perhitungan

### 5.3 Kesalahan Umum yang Harus Dihindari

| No | Kesalahan | Cara Menghindari |
|----|-----------|------------------|
| 1 | Salah menginterpretasi p-value ("P(H0 benar)") | Ingat: p-value = P(data seektrem ini JIKA H0 benar) |
| 2 | Bilang "terima H0" (bukan "fail to reject H0") | H0 tidak pernah "diterima", hanya "tidak ditolak" |
| 3 | Salah menginterpretasi CI ("95% peluang mu di sini") | Ingat: 95% dari CI yang dibuat berulang kali akan mengandung mu |
| 4 | Lupa ddof=1 saat menghitung variance sampel | Variance sampel: bagi dengan (n-1), bukan n |
| 5 | Salah memilih uji (paired vs independent) | Tanya: apakah subjeknya SAMA atau BERBEDA? |
| 6 | Tidak mengecek asumsi sebelum melakukan uji | Selalu pertimbangkan: apakah data memenuhi syarat uji ini? |
| 7 | Mengabaikan effect size | Selalu laporkan p-value DAN effect size |
| 8 | Bingung antara SE dan std | SE = s/sqrt(n), mengukur variasi RATA-RATA sampel. Std mengukur variasi DATA. |

---

## Bagian 6: Format dan Aturan UTS

### 6.1 Struktur Soal UTS

| Bagian | Tipe Soal | Bobot | Jumlah | Waktu Target |
|--------|-----------|-------|--------|-------------|
| A | Pilihan Ganda (konseptual) | 20% | 10 soal | 20 menit |
| B | Soal Hitungan (step-by-step) | 40% | 3-4 soal | 40 menit |
| C | Interpretasi Output Python/Statistik | 20% | 2-3 soal | 20 menit |
| D | Essay Analisis Kasus | 20% | 1 soal | 20 menit |

**Total: 100 menit**

### 6.2 Aturan Ujian

| Aturan | Detail |
|--------|--------|
| **Format** | Closed-book, written exam (kertas) |
| **Alat yang boleh dibawa** | Alat tulis, kalkulator non-programmable |
| **Alat yang TIDAK boleh** | HP, laptop, tablet, catatan, buku |
| **AI tools** | TIDAK diperbolehkan |
| **Durasi** | 100 menit |
| **Keterlambatan** | Maksimal 15 menit, tidak ada tambahan waktu |
| **Kecurangan** | Sanksi sesuai peraturan akademik UAI |

### 6.3 Cakupan Materi per Bagian Soal

```
Bagian A (Pilihan Ganda — Konseptual):
├── Tipe data dan skala pengukuran (1-2 soal)
├── Statistika deskriptif: mean vs median, skewness (1-2 soal)
├── Probabilitas dasar (1-2 soal)
├── Distribusi: kapan Binomial vs Poisson vs Normal (1-2 soal)
├── CLT dan SE (1 soal)
└── Uji hipotesis: konsep dasar (1-2 soal)

Bagian B (Hitungan Step-by-Step):
├── Hitung statistik deskriptif + deteksi outlier (1 soal)
├── Bayes' Theorem atau probabilitas distribusi (1 soal)
├── Confidence Interval (1 soal)
└── Uji hipotesis (t-test) + effect size (1 soal)

Bagian C (Interpretasi Output):
├── Diberikan output pandas describe() → interpretasikan (1 soal)
├── Diberikan output scipy.stats → interpretasikan p-value, keputusan (1 soal)
└── Diberikan visualisasi (boxplot/histogram) → analisis (1 soal)

Bagian D (Essay):
└── Skenario riil → desain analisis lengkap:
    "formulasi hipotesis → pilih uji → jelaskan langkah → interpretasi"
```

---

## Bagian 7: Ringkasan Kode Python Penting

Walaupun UTS closed-book tanpa Python, memahami kode membantu pemahaman konsep dan persiapan untuk Bagian C (Interpretasi Output).

```python
# === RANGKUMAN KODE PENTING ===

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# --- STATISTIKA DESKRIPTIF ---
data = pd.Series([...])
data.describe()             # ringkasan statistik
data.mean()                 # mean
data.median()               # median
data.std()                  # standard deviation (ddof=1 default di pandas)
data.quantile([0.25, 0.75]) # Q1 dan Q3

# --- DISTRIBUSI ---
# Normal
stats.norm.cdf(x, loc=mu, scale=sigma)   # P(X <= x)
stats.norm.ppf(q, loc=mu, scale=sigma)   # inverse: nilai x untuk P(X<=x)=q

# Binomial
stats.binom.pmf(k, n, p)    # P(X = k)
stats.binom.cdf(k, n, p)    # P(X <= k)

# Poisson
stats.poisson.pmf(k, mu)    # P(X = k)
stats.poisson.cdf(k, mu)    # P(X <= k)

# --- CONFIDENCE INTERVAL ---
se = s / np.sqrt(n)
ci = stats.t.interval(confidence=0.95, df=n-1, loc=x_bar, scale=se)

# --- UJI HIPOTESIS ---
stats.ttest_1samp(data, popmean=mu_0)              # one-sample t-test
stats.ttest_ind(group1, group2, equal_var=False)    # independent t-test
stats.ttest_rel(after, before)                       # paired t-test
```

---

## Bagian 8: Rencana Belajar 7 Hari Menjelang UTS

| Hari | Fokus | Aktivitas |
|------|-------|-----------|
| **Hari 7** (1 minggu sebelum) | Overview | Baca ulang semua modul Minggu 1-7, tandai yang belum paham |
| **Hari 6** | Minggu 1-3 | Review deskriptif, visualisasi, kerjakan ulang Lab 02-03 |
| **Hari 5** | Minggu 4-5 | Review probabilitas, distribusi, CLT. Kerjakan ulang Lab 04-05 |
| **Hari 4** | Minggu 6-7 | Review sampling, CI, uji hipotesis. Kerjakan ulang Lab 06-07 |
| **Hari 3** | Latihan Soal | Kerjakan 10 soal latihan di modul ini + latihan mandiri di setiap modul |
| **Hari 2** | Weak Spots | Fokus pada topik yang masih lemah, tanya dosen/teman/AI |
| **Hari 1** (malam sebelum) | Quick Review | Baca cheat sheet, tidur cukup! |

---

## Pesan Penutup

UTS ini menguji **pemahaman konseptual** dan **kemampuan menerapkan** statistik, bukan kemampuan menghafal rumus atau menulis kode Python. Jika kamu:

- **Memahami** mengapa kita melakukan sesuatu (bukan hanya bagaimana)
- **Bisa menjelaskan** konsep ke teman yang tidak mengerti
- **Bisa menginterpretasi** hasil dengan benar
- **Mengetahui** kapan harus menggunakan metode apa

...maka kamu sudah siap!

Setelah UTS, kita akan memasuki **Fase 3: Pemodelan** — dimulai dari korelasi dan regresi linear (Minggu 9). Materi paruh kedua membangun langsung di atas fondasi yang kita bangun selama Minggu 1-7, jadi pastikan fondasi ini kuat.

**Selamat belajar dan semoga sukses di UTS!**

---

## Referensi Keseluruhan (Minggu 1-7)

1. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics (4th ed.)*. Chapters 1-6.
2. McKinney, W. (2022). *Python for Data Analysis (3rd ed.)*. Chapters 1-7.
3. Downey, A. B. (2021). *Think Stats (2nd ed.)*. Chapters 1-9.
4. Bruce, P., & Bruce, A. (2020). *Practical Statistics for Data Scientists (2nd ed.)*. Chapters 1-3.
5. Knaflic, C. N. (2015). *Storytelling with Data*.

---

*Modul ini merupakan bagian dari mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia.*
