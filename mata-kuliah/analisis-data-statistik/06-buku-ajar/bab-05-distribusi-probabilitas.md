# BAB 5: DISTRIBUSI PROBABILITAS DAN CENTRAL LIMIT THEOREM

**Tri Aji Nugroho, S.T., M.T.**
Analisis Data Statistik --- Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-3.6 | Membedakan variabel random diskret dan kontinu serta fungsi probabilitasnya (PMF vs PDF) | C2 |
| CPMK-3.7 | Menerapkan distribusi Bernoulli, Binomial, dan Poisson untuk menghitung probabilitas kejadian diskret | C3 |
| CPMK-3.8 | Menerapkan distribusi Normal (Gaussian) dan z-score untuk menghitung probabilitas kejadian kontinu | C3 |
| CPMK-3.9 | Menjelaskan dan mendemonstrasikan Central Limit Theorem melalui simulasi Python | C3 |
| CPMK-3.10 | Menggunakan `scipy.stats` untuk memodelkan distribusi probabilitas dan memvisualisasikan hasilnya | C3 |

---

## 5.1 Variabel Random dan Distribusi Probabilitas

### 5.1.1 Apa Itu Variabel Random?

**Variabel random** (peubah acak) adalah suatu fungsi yang memetakan setiap hasil dari ruang sampel suatu percobaan ke nilai numerik. Dengan kata lain, variabel random mengubah hasil percobaan menjadi angka yang bisa kita analisis secara matematis.

> "A random variable is a numerical description of the outcome of a statistical experiment."
> --- Walpole et al., *Probability & Statistics for Engineers & Scientists*

**Contoh dalam konteks informatika:**
- Jumlah *bug* yang ditemukan dalam satu sprint (0, 1, 2, 3, ...)
- Waktu respons server dalam milidetik (45.2, 103.7, 88.1, ...)
- Jumlah pengunjung situs web per jam (0, 1, 2, ...)
- Ukuran file yang diunggah pengguna dalam megabyte (0.5, 2.3, 15.8, ...)

### 5.1.2 Diskret vs Kontinu

```
                    VARIABEL RANDOM
                         |
            +------------+------------+
            |                         |
        DISKRET                    KONTINU
   (nilai terhitung)          (nilai tak terhingga)
            |                         |
     +------+------+          +-------+-------+
     |      |      |          |       |       |
   Bernoulli Binomial Poisson Normal Uniform Eksponensial
```

| Aspek | Diskret | Kontinu |
|-------|---------|---------|
| **Nilai** | Terhitung (0, 1, 2, ...) | Bilangan riil (interval) |
| **Fungsi probabilitas** | PMF (*Probability Mass Function*) | PDF (*Probability Density Function*) |
| **P(X = x)** | Bisa > 0 | Selalu = 0 (gunakan interval) |
| **Probabilitas dihitung dari** | Penjumlahan PMF | Integral (luas area) di bawah PDF |
| **Contoh informatika** | Jumlah request gagal, jumlah bug | Response time, throughput, latency |

**Perbedaan penting:** Pada distribusi kontinu, probabilitas untuk nilai *tepat* satu titik selalu nol. Yang bermakna adalah probabilitas dalam suatu *interval*, misalnya P(50 < X < 100). Ini karena terdapat tak terhingga banyaknya titik pada garis bilangan riil.

### 5.1.3 Fungsi Probabilitas: PMF, PDF, dan CDF

**PMF (Probability Mass Function)** --- untuk variabel diskret:
- P(X = k) memberikan probabilitas variabel random bernilai tepat k
- Syarat: semua P(X = k) >= 0 dan jumlah seluruh P(X = k) = 1

**PDF (Probability Density Function)** --- untuk variabel kontinu:
- f(x) memberikan *density* (kerapatan) di titik x
- P(a < X < b) = integral f(x) dx dari a ke b (luas area di bawah kurva)
- Syarat: f(x) >= 0 dan total luas di bawah kurva = 1

**CDF (Cumulative Distribution Function)** --- untuk keduanya:
- F(x) = P(X <= x) --- probabilitas kumulatif sampai titik x
- Selalu naik monoton dari 0 ke 1

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Perbandingan PMF (diskret) vs PDF (kontinu)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# PMF: Distribusi Binomial (diskret)
n, p = 20, 0.4
k = np.arange(0, n + 1)
pmf_values = stats.binom.pmf(k, n, p)
axes[0].bar(k, pmf_values, color='steelblue', edgecolor='black', alpha=0.7)
axes[0].set_title('PMF: Distribusi Binomial (n=20, p=0.4)', fontsize=12)
axes[0].set_xlabel('k (jumlah sukses)')
axes[0].set_ylabel('P(X = k)')
axes[0].grid(axis='y', alpha=0.3)

# PDF: Distribusi Normal (kontinu)
mu, sigma = 8.0, 2.0
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
pdf_values = stats.norm.pdf(x, mu, sigma)
axes[1].plot(x, pdf_values, 'b-', linewidth=2)
axes[1].fill_between(x, pdf_values, alpha=0.15, color='steelblue')
axes[1].set_title('PDF: Distribusi Normal (mu=8, sigma=2)', fontsize=12)
axes[1].set_xlabel('x')
axes[1].set_ylabel('f(x) (density)')
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## 5.2 Distribusi Bernoulli dan Binomial

### 5.2.1 Distribusi Bernoulli

Distribusi Bernoulli adalah distribusi paling sederhana: satu percobaan dengan dua kemungkinan hasil --- **sukses** (1) atau **gagal** (0).

**Parameter:** p (probabilitas sukses)

**PMF:**

$$P(X = k) = p^k (1-p)^{1-k}, \quad k \in \{0, 1\}$$

**Statistik:**
- Mean: E(X) = p
- Variance: Var(X) = p(1 - p)

**Contoh:** Seorang mahasiswa mengerjakan satu soal ujian. Probabilitas menjawab benar adalah 0.7. Maka X ~ Bernoulli(0.7).

### 5.2.2 Distribusi Binomial

Distribusi Binomial adalah **penjumlahan dari n percobaan Bernoulli independen**. Jika kita mengulangi percobaan Bernoulli sebanyak n kali, distribusi Binomial menjawab pertanyaan: **"Berapa kali sukses terjadi dari n percobaan?"**

**Syarat (harus semua terpenuhi):**
1. Jumlah percobaan (n) tetap dan diketahui
2. Setiap percobaan hanya memiliki 2 hasil: sukses atau gagal
3. Probabilitas sukses (p) sama di setiap percobaan
4. Percobaan saling independen

**PMF (formula):**

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

di mana:
- $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ adalah koefisien binomial (kombinasi)
- n = jumlah percobaan
- k = jumlah sukses yang diinginkan (0, 1, 2, ..., n)
- p = probabilitas sukses per percobaan

**Statistik penting:**
- Mean: E(X) = np
- Variance: Var(X) = np(1 - p)
- Standar deviasi: SD(X) = sqrt(np(1 - p))

### 5.2.3 Contoh: Tingkat Kelulusan Ujian

Di sebuah kelas Informatika UAI, probabilitas mahasiswa lulus ujian Statistik adalah 0.75. Dari 20 mahasiswa yang mengikuti ujian:

```python
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Parameter
n = 20      # jumlah mahasiswa
p = 0.75    # probabilitas lulus

# Membuat objek distribusi Binomial
binom_dist = stats.binom(n=n, p=p)

# Hitung probabilitas spesifik
print("=== DISTRIBUSI BINOMIAL: Kelulusan Ujian ===")
print(f"Parameter: n = {n}, p = {p}")
print(f"Mean (expected) = {binom_dist.mean():.2f} mahasiswa lulus")
print(f"Std Dev = {binom_dist.std():.2f}")
print()

# Pertanyaan-pertanyaan:
# 1. Berapa probabilitas tepat 15 mahasiswa lulus?
p_15 = binom_dist.pmf(15)
print(f"P(X = 15) = {p_15:.4f}  --> probabilitas tepat 15 lulus")

# 2. Berapa probabilitas 12 atau kurang yang lulus?
p_leq12 = binom_dist.cdf(12)
print(f"P(X <= 12) = {p_leq12:.4f}  --> 12 atau kurang lulus")

# 3. Berapa probabilitas lebih dari 18 yang lulus?
p_gt18 = 1 - binom_dist.cdf(18)
print(f"P(X > 18) = {p_gt18:.4f}  --> lebih dari 18 lulus")

# 4. Berapa probabilitas antara 14 dan 17 yang lulus (inklusif)?
p_14_17 = binom_dist.cdf(17) - binom_dist.cdf(13)
print(f"P(14 <= X <= 17) = {p_14_17:.4f}  --> antara 14 dan 17 lulus")

# Visualisasi
k_values = np.arange(0, n + 1)
probabilities = binom_dist.pmf(k_values)

plt.figure(figsize=(10, 5))
colors = ['coral' if k < 14 or k > 17 else 'steelblue' for k in k_values]
plt.bar(k_values, probabilities, color=colors, edgecolor='black', alpha=0.7)
plt.xlabel('Jumlah Mahasiswa Lulus (k)', fontsize=11)
plt.ylabel('P(X = k)', fontsize=11)
plt.title(f'Distribusi Binomial: Kelulusan Ujian (n={n}, p={p})', fontsize=13)
plt.xticks(k_values)
plt.grid(axis='y', alpha=0.3)
plt.legend(['Biru = P(14 <= X <= 17)'], fontsize=10)
plt.tight_layout()
plt.show()
```

### 5.2.4 Bentuk Distribusi Binomial (ASCII)

Berikut ilustrasi bentuk distribusi Binomial untuk berbagai nilai p (dengan n = 20):

```
p = 0.2 (skewed kanan)     p = 0.5 (simetris)       p = 0.8 (skewed kiri)

P(X=k)                     P(X=k)                    P(X=k)
 |                          |                          |
 |  ***                     |       ***                |                ***
 | *****                    |     *******              |              *****
 |*******                   |   ***********            |            *******
 |*********                 |  *************           |          *********
 |***********               | ***************          |        ***********
 +-----------> k            +-----------> k            +-----------> k
 0  2  4  6  8              0  5  10  15  20           12  14  16  18  20
```

**Pengamatan:** Semakin p mendekati 0.5, distribusi Binomial semakin simetris. Jika p < 0.5, distribusi condong ke kanan (*right-skewed*); jika p > 0.5, distribusi condong ke kiri (*left-skewed*).

---

## 5.3 Distribusi Poisson

### 5.3.1 Kapan Menggunakan Poisson?

Distribusi Poisson digunakan ketika kita ingin menghitung **jumlah kejadian** dalam suatu **interval waktu atau ruang** tertentu, di mana kejadian terjadi secara **acak dan independen** dengan **rata-rata konstan**.

**Syarat:**
1. Kejadian terjadi secara independen satu sama lain
2. Rata-rata kejadian (*rate*) konstan sepanjang interval
3. Dua kejadian tidak dapat terjadi di titik waktu yang persis sama

**PMF (formula):**

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

di mana:
- $\lambda$ (lambda) = rata-rata jumlah kejadian per interval
- k = jumlah kejadian yang ingin dihitung probabilitasnya (0, 1, 2, ...)
- e = 2.71828... (bilangan Euler)

**Statistik penting:**
- Mean: E(X) = $\lambda$
- Variance: Var(X) = $\lambda$

> **Ciri khas Poisson:** Mean = Variance. Jika Anda menemukan data cacahan di mana mean dan variance hampir sama, distribusi Poisson patut dipertimbangkan.

### 5.3.2 Contoh: Bug Report per Sprint

Tim pengembang aplikasi mobile di sebuah startup Jakarta menerima rata-rata 4 *bug report* per hari dari pengguna.

```python
# === DISTRIBUSI POISSON: Bug Report per Hari ===
lam = 4  # rata-rata 4 bug report per hari

poisson_dist = stats.poisson(mu=lam)

print("=== DISTRIBUSI POISSON: Bug Report ===")
print(f"Parameter: lambda = {lam}")
print(f"Mean = {poisson_dist.mean():.2f}")
print(f"Variance = {poisson_dist.var():.2f}  (sama dengan mean!)")
print()

# Pertanyaan:
# 1. Probabilitas tidak ada bug report sama sekali hari ini?
p_0 = poisson_dist.pmf(0)
print(f"P(X = 0) = {p_0:.4f}  --> tidak ada bug sama sekali")

# 2. Probabilitas tepat 4 bug report?
p_4 = poisson_dist.pmf(4)
print(f"P(X = 4) = {p_4:.4f}  --> tepat 4 bug")

# 3. Probabilitas lebih dari 7 bug report (hari yang buruk)?
p_gt7 = 1 - poisson_dist.cdf(7)
print(f"P(X > 7) = {p_gt7:.4f}  --> lebih dari 7 bug (hari buruk)")

# 4. Probabilitas 3 atau kurang bug report (hari yang baik)?
p_leq3 = poisson_dist.cdf(3)
print(f"P(X <= 3) = {p_leq3:.4f}  --> 3 atau kurang (hari baik)")

# Visualisasi
k_values = np.arange(0, 15)
probabilities = poisson_dist.pmf(k_values)

plt.figure(figsize=(10, 5))
plt.bar(k_values, probabilities, color='coral', edgecolor='black', alpha=0.7)
plt.xlabel('Jumlah Bug Report (k)', fontsize=11)
plt.ylabel('P(X = k)', fontsize=11)
plt.title(f'Distribusi Poisson: Bug Report per Hari (lambda={lam})', fontsize=13)
plt.xticks(k_values)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

### 5.3.3 Binomial vs Poisson: Kapan Pakai yang Mana?

| Aspek | Binomial | Poisson |
|-------|----------|---------|
| **Jumlah percobaan** | Tetap (n diketahui) | Tidak tetap (kejadian dalam interval) |
| **Pertanyaan khas** | "Berapa sukses dari n percobaan?" | "Berapa kejadian dalam interval waktu/ruang?" |
| **Parameter** | n dan p | $\lambda$ saja |
| **Contoh informatika** | Dari 100 request, berapa yang gagal? | Berapa request masuk per detik? |
| **Hubungan** | Jika n besar dan p kecil, mendekati Poisson dengan $\lambda$ = np | --- |

**Panduan memilih:**

```
Apakah jumlah percobaan (n) diketahui dan tetap?
├── YA --> Apakah setiap percobaan hanya sukses/gagal?
│          ├── YA --> BINOMIAL
│          └── TIDAK --> Pertimbangkan distribusi lain
└── TIDAK --> Apakah kita menghitung kejadian dalam interval?
              ├── YA --> POISSON
              └── TIDAK --> Pertimbangkan distribusi lain
```

---

## 5.4 Distribusi Normal (Gaussian)

### 5.4.1 Mengapa Distribusi Normal Sangat Penting?

Distribusi Normal sering disebut *"The King of Distributions"* karena empat alasan utama:

1. **Banyak fenomena alam dan buatan** mengikuti distribusi Normal: tinggi badan manusia, skor IQ, *error* pengukuran, noise pada sinyal elektronik
2. **Central Limit Theorem** menjamin bahwa rata-rata sampel mendekati distribusi Normal untuk ukuran sampel yang cukup besar
3. **Banyak uji statistik** mengasumsikan data berdistribusi Normal (z-test, t-test, ANOVA, regresi)
4. **Hanya memerlukan 2 parameter** untuk mendeskripsikan seluruh distribusi: mean ($\mu$) dan standar deviasi ($\sigma$)

### 5.4.2 Formula PDF

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$$

di mana:
- $\mu$ (mu) = mean (pusat distribusi)
- $\sigma$ (sigma) = standar deviasi (lebar distribusi)
- $\pi$ = 3.14159...
- e = 2.71828... (bilangan Euler)

Notasi: X ~ N($\mu$, $\sigma^2$) atau X ~ Normal($\mu$, $\sigma$)

### 5.4.3 Sifat-sifat Distribusi Normal

1. **Simetris** terhadap mean ($\mu$)
2. **Mean = Median = Modus** (semuanya berada di titik puncak kurva)
3. Berbentuk **lonceng** (*bell curve*)
4. **Aturan Empiris (68-95-99.7 Rule):**
   - 68.27% data berada dalam $\mu \pm 1\sigma$
   - 95.45% data berada dalam $\mu \pm 2\sigma$
   - 99.73% data berada dalam $\mu \pm 3\sigma$
5. Ekor (*tail*) kurva mendekati nol tetapi **tidak pernah menyentuh** sumbu-x (mendekati tak hingga)
6. **Total luas** di bawah kurva = 1

### 5.4.4 Aturan Empiris (ASCII Diagram)

```
                         68.27%
                     |<--------->|
               95.45%
           |<------------------->|
              99.73%
       |<--------------------------->|

                        *****
                      **     **
                    **         **
                  **             **
                **                 **
              **                     **
           ***                         ***
        ***                               ***
   ****                                       ****
───┼───────┼───────┼───────┼───────┼───────┼───────┼───
 mu-3s   mu-2s   mu-1s    mu    mu+1s   mu+2s   mu+3s

   0.13%   2.15%  13.59%  34.13% 34.13%  13.59%  2.15%  0.13%
```

### 5.4.5 Contoh: Nilai Ujian Mahasiswa

Nilai UTS mata kuliah Analisis Data Statistik berdistribusi Normal dengan mean = 70 dan standar deviasi = 10.

```python
# === DISTRIBUSI NORMAL: Nilai UTS ===
mu = 70      # mean
sigma = 10   # standar deviasi

normal_dist = stats.norm(loc=mu, scale=sigma)

# Generate x untuk plot
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
y = normal_dist.pdf(x)

# Visualisasi dengan aturan 68-95-99.7
fig, ax = plt.subplots(figsize=(12, 6))

# Plot PDF
ax.plot(x, y, 'k-', linewidth=2, label='PDF Normal')

# Shade daerah 68% (mu +/- 1 sigma)
x_1s = np.linspace(mu - sigma, mu + sigma, 100)
ax.fill_between(x_1s, stats.norm.pdf(x_1s, mu, sigma),
                color='steelblue', alpha=0.5, label='68.27% (mu +/- 1 sigma)')

# Shade daerah 95% (mu +/- 2 sigma)
x_2s_left = np.linspace(mu - 2*sigma, mu - sigma, 100)
x_2s_right = np.linspace(mu + sigma, mu + 2*sigma, 100)
ax.fill_between(x_2s_left, stats.norm.pdf(x_2s_left, mu, sigma),
                color='steelblue', alpha=0.3)
ax.fill_between(x_2s_right, stats.norm.pdf(x_2s_right, mu, sigma),
                color='steelblue', alpha=0.3, label='95.45% (mu +/- 2 sigma)')

# Shade daerah 99.7% (mu +/- 3 sigma)
x_3s_left = np.linspace(mu - 3*sigma, mu - 2*sigma, 100)
x_3s_right = np.linspace(mu + 2*sigma, mu + 3*sigma, 100)
ax.fill_between(x_3s_left, stats.norm.pdf(x_3s_left, mu, sigma),
                color='steelblue', alpha=0.15)
ax.fill_between(x_3s_right, stats.norm.pdf(x_3s_right, mu, sigma),
                color='steelblue', alpha=0.15, label='99.73% (mu +/- 3 sigma)')

ax.set_xlabel('Nilai UTS', fontsize=11)
ax.set_ylabel('Density', fontsize=11)
ax.set_title(f'Distribusi Normal: Nilai UTS (mu={mu}, sigma={sigma})', fontsize=13)
ax.legend(fontsize=10)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Hitung probabilitas
print("=== PROBABILITAS DISTRIBUSI NORMAL ===")
print(f"Parameter: mu = {mu}, sigma = {sigma}")
print()

# 1. Berapa persen mahasiswa mendapat nilai di bawah 60?
p_lt60 = normal_dist.cdf(60)
print(f"P(X < 60)       = {p_lt60:.4f} ({p_lt60*100:.2f}%)")

# 2. Berapa persen mahasiswa mendapat nilai antara 60 dan 80?
p_60_80 = normal_dist.cdf(80) - normal_dist.cdf(60)
print(f"P(60 < X < 80)  = {p_60_80:.4f} ({p_60_80*100:.2f}%)")

# 3. Berapa persen mahasiswa mendapat nilai di atas 90?
p_gt90 = 1 - normal_dist.cdf(90)
print(f"P(X > 90)       = {p_gt90:.4f} ({p_gt90*100:.2f}%)")

# 4. Nilai minimum untuk masuk 10% terbaik?
top10 = normal_dist.ppf(0.90)
print(f"\nNilai minimum top 10% = {top10:.2f}")

# 5. Verifikasi aturan empiris
p_1sd = normal_dist.cdf(mu + sigma) - normal_dist.cdf(mu - sigma)
p_2sd = normal_dist.cdf(mu + 2*sigma) - normal_dist.cdf(mu - 2*sigma)
p_3sd = normal_dist.cdf(mu + 3*sigma) - normal_dist.cdf(mu - 3*sigma)
print(f"\n--- Verifikasi Aturan Empiris ---")
print(f"P(mu +/- 1 sigma) = {p_1sd:.4f} (teori: 0.6827)")
print(f"P(mu +/- 2 sigma) = {p_2sd:.4f} (teori: 0.9545)")
print(f"P(mu +/- 3 sigma) = {p_3sd:.4f} (teori: 0.9973)")
```

---

## 5.5 Z-Score dan Standardisasi

### 5.5.1 Apa Itu Z-Score?

**Z-score** (skor standar) mengubah suatu nilai dari distribusi apapun ke **Standard Normal Distribution** dengan mean = 0 dan standar deviasi = 1.

**Formula:**

$$z = \frac{x - \mu}{\sigma}$$

di mana:
- x = nilai yang ingin di-standardisasi
- $\mu$ = mean populasi (atau sampel)
- $\sigma$ = standar deviasi populasi (atau sampel)

**Interpretasi z-score:**
- z = 0 : nilai tepat di mean
- z = +1 : nilai 1 standar deviasi di atas mean
- z = -2 : nilai 2 standar deviasi di bawah mean
- |z| > 2 : nilai cukup jauh dari rata-rata (perlu perhatian)
- |z| > 3 : kemungkinan besar **outlier**

### 5.5.2 Mengapa Standardisasi Penting?

1. **Membandingkan skala berbeda:** Nilai UTS Statistik (skala 0--100) vs skor TOEFL (skala 0--677) --- z-score membuat keduanya bisa dibandingkan secara adil
2. **Mendeteksi outlier:** Pengamatan dengan |z| > 3 patut dicurigai sebagai outlier
3. **Dasar uji statistik:** z-test, t-test, dan banyak uji lain menggunakan nilai terstandarisasi
4. **Preprocessing data untuk ML:** Banyak algoritma machine learning memerlukan fitur yang sudah di-standardisasi

### 5.5.3 Contoh: Membandingkan Performa di Dua Mata Kuliah

```python
# === Z-SCORE: Membandingkan Performa Mahasiswa ===

# Skenario: Ahmad mendapat nilai di dua mata kuliah berbeda.
# Di mana dia lebih menonjol relatif terhadap kelasnya?

# Mata kuliah Statistik: mean = 70, std = 10, Ahmad dapat 85
# Mata kuliah Pemrograman: mean = 60, std = 15, Ahmad dapat 80

z_stat = (85 - 70) / 10    # z = 1.50
z_prog = (80 - 60) / 15    # z = 1.33

print("=== PERBANDINGAN Z-SCORE ===")
print(f"Statistik   : Nilai = 85, Z-score = {z_stat:.2f}")
print(f"Pemrograman : Nilai = 80, Z-score = {z_prog:.2f}")
print()

# Hitung persentil
pct_stat = stats.norm.cdf(z_stat) * 100
pct_prog = stats.norm.cdf(z_prog) * 100
print(f"Statistik   : Persentil ke-{pct_stat:.1f} (lebih baik dari {pct_stat:.1f}% kelas)")
print(f"Pemrograman : Persentil ke-{pct_prog:.1f} (lebih baik dari {pct_prog:.1f}% kelas)")
print()
print("Kesimpulan: Ahmad lebih menonjol di Statistik (z lebih tinggi),")
print("meskipun nilai absolut Statistik (85) dan Pemrograman (80)")
print("tampak hanya beda 5 poin.")
```

### 5.5.4 Standardisasi Dataset Lengkap

```python
# === STANDARDISASI DATASET LENGKAP ===
np.random.seed(42)
nilai_ujian = np.random.normal(loc=70, scale=10, size=100)

# Hitung z-score untuk semua data
z_scores = (nilai_ujian - nilai_ujian.mean()) / nilai_ujian.std()

# Visualisasi sebelum dan sesudah standardisasi
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.hist(nilai_ujian, bins=20, color='steelblue', edgecolor='black', alpha=0.7)
ax1.axvline(nilai_ujian.mean(), color='red', linestyle='--', label=f'Mean = {nilai_ujian.mean():.1f}')
ax1.set_title(f'Nilai Asli (mu={nilai_ujian.mean():.1f}, sigma={nilai_ujian.std():.1f})', fontsize=12)
ax1.set_xlabel('Nilai')
ax1.set_ylabel('Frekuensi')
ax1.legend()

ax2.hist(z_scores, bins=20, color='coral', edgecolor='black', alpha=0.7)
ax2.axvline(0, color='red', linestyle='--', label=f'Mean = {z_scores.mean():.4f}')
ax2.set_title(f'Z-Scores (mu={z_scores.mean():.4f}, sigma={z_scores.std():.4f})', fontsize=12)
ax2.set_xlabel('Z-Score')
ax2.set_ylabel('Frekuensi')
ax2.legend()

plt.tight_layout()
plt.show()

# Identifikasi outlier menggunakan z-score
outliers = nilai_ujian[np.abs(z_scores) > 2]
print(f"Nilai dengan |z| > 2 (kemungkinan outlier): {outliers.round(1)}")
print(f"Jumlah outlier: {len(outliers)} dari {len(nilai_ujian)} data")
```

---

## 5.6 Distribusi Lainnya: Uniform dan Eksponensial

### 5.6.1 Distribusi Uniform (Seragam)

Distribusi Uniform mendeskripsikan situasi di mana semua nilai dalam interval [a, b] memiliki **kemungkinan yang sama** untuk terjadi.

**PDF:**

$$f(x) = \frac{1}{b - a}, \quad a \leq x \leq b$$

**Statistik:**
- Mean: E(X) = (a + b) / 2
- Variance: Var(X) = (b - a)^2 / 12

**Contoh informatika:**
- Fungsi `random()` yang menghasilkan bilangan acak antara 0 dan 1
- Waktu kedatangan bus yang hanya diketahui akan datang antara 0--15 menit
- *Load balancing* yang mendistribusikan request secara merata ke beberapa server

```
Distribusi Uniform (a=0, b=10):

f(x)
 |
 |  +--------------------------+
 |  |                          |
 |  |     luas = 1/(b-a)      |
 |  |                          |
 |  +--------------------------+
 +--+--+--+--+--+--+--+--+--+--+--> x
 0  1  2  3  4  5  6  7  8  9  10
```

### 5.6.2 Distribusi Eksponensial

Distribusi Eksponensial mendeskripsikan **waktu antar kejadian** dalam proses Poisson. Jika kejadian terjadi rata-rata $\lambda$ kali per satuan waktu (mengikuti Poisson), maka waktu antar dua kejadian berurutan mengikuti distribusi Eksponensial.

**PDF:**

$$f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$$

**Statistik:**
- Mean: E(X) = 1/$\lambda$
- Variance: Var(X) = 1/$\lambda^2$

**Contoh informatika:**
- Waktu antar kedatangan request ke server (jika rata-rata 10 request/detik, waktu antar request ~ Exp(10))
- Waktu antar kegagalan (*failure*) komponen hardware
- Waktu *session* pengguna di aplikasi web

**Hubungan Poisson-Eksponensial:**

```
POISSON                              EKSPONENSIAL
(diskret)                            (kontinu)
"Berapa kejadian per interval?"      "Berapa lama sampai kejadian berikutnya?"
  X ~ Poisson(lambda)          <-->    T ~ Exp(lambda)

Contoh:
  Rata-rata 5 request/detik    <-->    Waktu antar request ~ Exp(5)
  (lambda = 5)                         Mean = 1/5 = 0.2 detik
```

### 5.6.3 Ringkasan Distribusi Utama

```python
# === RINGKASAN VISUAL: 4 Distribusi Utama ===
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Binomial
ax = axes[0, 0]
for n_val, p_val in [(20, 0.3), (20, 0.5), (20, 0.7)]:
    k = np.arange(0, n_val + 1)
    ax.plot(k, stats.binom.pmf(k, n_val, p_val), 'o-', label=f'n={n_val}, p={p_val}', markersize=4)
ax.set_title('Distribusi Binomial (Diskret)', fontsize=12, fontweight='bold')
ax.set_xlabel('k')
ax.set_ylabel('P(X = k)')
ax.legend()
ax.grid(alpha=0.3)

# 2. Poisson
ax = axes[0, 1]
k = np.arange(0, 20)
for lam_val in [1, 3, 7, 12]:
    ax.plot(k, stats.poisson.pmf(k, lam_val), 'o-', label=f'lambda={lam_val}', markersize=4)
ax.set_title('Distribusi Poisson (Diskret)', fontsize=12, fontweight='bold')
ax.set_xlabel('k')
ax.set_ylabel('P(X = k)')
ax.legend()
ax.grid(alpha=0.3)

# 3. Normal
ax = axes[1, 0]
x = np.linspace(-10, 20, 200)
for mu_val, sigma_val in [(0, 1), (5, 1), (5, 2), (5, 3)]:
    ax.plot(x, stats.norm.pdf(x, mu_val, sigma_val),
            label=f'mu={mu_val}, sigma={sigma_val}')
ax.set_title('Distribusi Normal (Kontinu)', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.grid(alpha=0.3)

# 4. Eksponensial
ax = axes[1, 1]
x = np.linspace(0, 5, 200)
for lam_val in [0.5, 1, 2, 5]:
    ax.plot(x, stats.expon.pdf(x, scale=1/lam_val),
            label=f'lambda={lam_val}')
ax.set_title('Distribusi Eksponensial (Kontinu)', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.grid(alpha=0.3)

plt.suptitle('Perbandingan Distribusi Probabilitas Utama', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

## 5.7 Central Limit Theorem (CLT)

### 5.7.1 Pernyataan CLT

> **Central Limit Theorem:** Jika kita mengambil banyak sampel berukuran n dari **populasi apapun** (distribusi apapun, asalkan variance terhingga), maka **distribusi rata-rata sampel** ($\bar{X}$) akan mendekati **distribusi Normal** seiring bertambahnya n --- **tidak peduli** bagaimana bentuk distribusi asalnya.

**Secara matematis:**

Jika $X_1, X_2, \ldots, X_n$ adalah sampel acak dari populasi dengan mean $\mu$ dan standar deviasi $\sigma$, maka untuk n yang cukup besar:

$$\bar{X} \sim N\left(\mu, \frac{\sigma}{\sqrt{n}}\right)$$

di mana:
- $\bar{X}$ = rata-rata sampel
- $\mu$ = mean populasi
- $\frac{\sigma}{\sqrt{n}}$ = **standard error of the mean** (SE)

**Implikasi penting:** Standard error **mengecil** seiring bertambahnya n. Artinya, semakin besar sampel, semakin akurat estimasi rata-rata sampel terhadap rata-rata populasi.

### 5.7.2 Mengapa CLT Sangat Penting?

CLT adalah **fondasi** dari hampir seluruh statistik inferensial:

1. **Confidence interval** --- mengasumsikan distribusi rata-rata sampel mendekati Normal
2. **Uji hipotesis** --- z-test dan t-test mengandalkan CLT
3. **Estimasi parameter** --- semua bergantung pada distribusi *sampling*
4. **Membebaskan kita dari asumsi normalitas populasi** --- kita tidak perlu tahu distribusi populasi asli untuk melakukan inferensi tentang rata-rata

**Analogi sederhana:** Bayangkan Anda mengumpulkan data waktu respons server. Data aslinya mungkin sangat *skewed* ke kanan (beberapa request sangat lambat). Namun jika Anda mengambil 50 sampel, masing-masing berisi 30 pengamatan, lalu menghitung rata-rata tiap sampel --- 50 rata-rata tersebut akan membentuk kurva lonceng yang indah!

### 5.7.3 Berapa Besar n yang "Cukup Besar"?

| Distribusi Asal | n Minimum |
|-----------------|-----------|
| Sudah mendekati Normal | n >= 10 sudah cukup |
| Sedikit *skewed* | n >= 30 (*rule of thumb* klasik) |
| Sangat *skewed* (misalnya eksponensial) | n >= 50 atau lebih |
| Secara umum | **n >= 30 biasanya aman** |

### 5.7.4 Ilustrasi CLT (ASCII)

```
POPULASI ASLI             DISTRIBUSI RATA-RATA SAMPEL
(bisa bentuk apa saja)    (mendekati Normal!)

Eksponensial:             n=5:          n=30:         n=100:
  |*                       |             |              |
  |**                      | **          |  ***         |  ****
  | ***                    |****         | ******       | *******
  |  *****                 |*****        |*********     |**********
  |    *********           | ******      |**********    |***********
  +----------->            +------>      +------->      +-------->

Uniform:                  n=5:          n=30:         n=100:
  |++++++++++|             |             |              |
  |++++++++++|             | ****        |  *****       |  ******
  |++++++++++|             |******       | ********     | *********
  |++++++++++|             |*******      |**********    |***********
  +----------->            +------>      +------->      +-------->
```

### 5.7.5 Simulasi CLT dengan Python

Berikut simulasi yang **membuktikan** CLT secara empiris menggunakan distribusi yang jelas-jelas bukan Normal:

```python
# === SIMULASI CENTRAL LIMIT THEOREM ===
np.random.seed(42)

def simulate_clt(distribution_func, dist_name, sample_sizes=[5, 30, 100],
                 n_simulations=1000):
    """
    Simulasi CLT: ambil banyak sampel, hitung mean, plot distribusinya.

    Parameters:
    -----------
    distribution_func : callable
        Fungsi yang menghasilkan random sample
    dist_name : str
        Nama distribusi untuk judul plot
    sample_sizes : list
        Daftar ukuran sampel yang akan dicoba
    n_simulations : int
        Berapa kali pengambilan sampel dilakukan
    """
    fig, axes = plt.subplots(1, len(sample_sizes) + 1, figsize=(18, 4))

    # Plot distribusi asli (populasi)
    original_data = distribution_func(size=10000)
    axes[0].hist(original_data, bins=50, color='lightgray', edgecolor='black',
                 alpha=0.7, density=True)
    axes[0].set_title(f'Populasi Asli\n{dist_name}', fontsize=11)
    axes[0].set_ylabel('Density')

    # Simulasi untuk setiap ukuran sampel
    for i, n in enumerate(sample_sizes):
        # Ambil n_simulations sampel, masing-masing berukuran n
        sample_means = [distribution_func(size=n).mean()
                        for _ in range(n_simulations)]

        # Plot distribusi rata-rata sampel
        axes[i + 1].hist(sample_means, bins=40, color='steelblue',
                         edgecolor='black', alpha=0.7, density=True)

        # Overlay kurva Normal teoritis
        mean_of_means = np.mean(sample_means)
        std_of_means = np.std(sample_means)
        x_range = np.linspace(min(sample_means), max(sample_means), 100)
        normal_curve = stats.norm.pdf(x_range, mean_of_means, std_of_means)
        axes[i + 1].plot(x_range, normal_curve, 'r-', linewidth=2,
                         label='Kurva Normal')

        axes[i + 1].set_title(f'Rata-rata Sampel\nn = {n}', fontsize=11)
        axes[i + 1].legend(fontsize=8)

    plt.suptitle(f'Central Limit Theorem --- {dist_name}',
                 fontsize=13, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.show()

# 1. Distribusi Eksponensial (sangat skewed ke kanan)
print("=" * 60)
print("1. DISTRIBUSI EKSPONENSIAL (sangat skewed)")
print("=" * 60)
simulate_clt(
    lambda size: np.random.exponential(scale=2, size=size),
    "Eksponensial (lambda=0.5)"
)

# 2. Distribusi Uniform (flat, bukan Normal sama sekali)
print("\n" + "=" * 60)
print("2. DISTRIBUSI UNIFORM (flat)")
print("=" * 60)
simulate_clt(
    lambda size: np.random.uniform(low=0, high=10, size=size),
    "Uniform (0, 10)"
)

# 3. Distribusi Binomial (diskret dan skewed)
print("\n" + "=" * 60)
print("3. DISTRIBUSI BINOMIAL (diskret, skewed)")
print("=" * 60)
simulate_clt(
    lambda size: np.random.binomial(n=5, p=0.2, size=size),
    "Binomial (n=5, p=0.2)"
)
```

**Yang harus diperhatikan dari simulasi:**

| Kolom | Deskripsi |
|-------|-----------|
| Kolom 1 (Populasi) | Distribusi asli --- bentuknya sangat berbeda dari Normal |
| Kolom 2 (n=5) | Rata-rata sampel mulai bergeser, tetapi belum Normal |
| Kolom 3 (n=30) | Sudah **cukup mirip** Normal! Kurva merah cocok |
| Kolom 4 (n=100) | **Sangat mendekati** Normal, hampir sempurna |

### 5.7.6 Standard Error dan CLT

Standard Error (SE) menunjukkan seberapa bervariasi rata-rata sampel dari satu sampel ke sampel lainnya:

$$SE = \frac{\sigma}{\sqrt{n}}$$

**Implikasi praktis:**
- Jika n naik 4 kali lipat, SE turun 2 kali lipat (akar kuadrat)
- Untuk mendapatkan estimasi 2 kali lebih presisi, diperlukan sampel 4 kali lebih banyak

```python
# === DEMONSTRASI STANDARD ERROR ===
sample_sizes = [5, 10, 25, 50, 100, 200, 500]
sigma_pop = 10  # standar deviasi populasi

se_theory = [sigma_pop / np.sqrt(n) for n in sample_sizes]
se_simulated = []

np.random.seed(42)
for n in sample_sizes:
    means = [np.random.normal(70, sigma_pop, size=n).mean() for _ in range(2000)]
    se_simulated.append(np.std(means))

plt.figure(figsize=(10, 5))
plt.plot(sample_sizes, se_theory, 'b-o', label='SE Teoritis (sigma/sqrt(n))', linewidth=2)
plt.plot(sample_sizes, se_simulated, 'r--s', label='SE Simulasi', linewidth=2)
plt.xlabel('Ukuran Sampel (n)', fontsize=11)
plt.ylabel('Standard Error', fontsize=11)
plt.title('Standard Error Menurun Seiring Bertambahnya n', fontsize=13)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print("  n   | SE Teoritis | SE Simulasi")
print("------+-------------+------------")
for n, se_t, se_s in zip(sample_sizes, se_theory, se_simulated):
    print(f" {n:>4} |   {se_t:.4f}   |   {se_s:.4f}")
```

---

## 5.8 Aplikasi Distribusi di Informatika

### 5.8.1 Network Traffic --- Distribusi Poisson

Jumlah paket yang tiba di router dalam satu detik sering dimodelkan dengan distribusi Poisson. Jika rata-rata ada 50 paket/detik:

```python
# === NETWORK TRAFFIC: Poisson ===
lam_traffic = 50  # rata-rata paket per detik
poisson_traffic = stats.poisson(mu=lam_traffic)

# Probabilitas menerima lebih dari 65 paket (kemacetan)
p_congestion = 1 - poisson_traffic.cdf(65)
print(f"P(paket > 65) = {p_congestion:.4f}")
print(f"Artinya, ada {p_congestion*100:.2f}% kemungkinan kemacetan terjadi dalam satu detik.")
```

### 5.8.2 Bug Rate --- Distribusi Poisson dan Binomial

```python
# === BUG RATE ===
# Skenario 1 (Poisson): Rata-rata 2 bug kritis per minggu
bug_dist = stats.poisson(mu=2)
p_no_bug = bug_dist.pmf(0)
print(f"P(0 bug kritis dalam seminggu) = {p_no_bug:.4f}")

# Skenario 2 (Binomial): Dari 1000 baris kode, probabilitas bug = 0.003 per baris
n_lines = 1000
p_bug = 0.003
bug_binom = stats.binom(n=n_lines, p=p_bug)
print(f"Expected bugs dalam 1000 baris: {bug_binom.mean():.1f}")
print(f"P(lebih dari 5 bugs) = {1 - bug_binom.cdf(5):.4f}")
```

### 5.8.3 Response Time --- Distribusi Eksponensial dan Normal

```python
# === RESPONSE TIME ===
# Waktu antar request ke server: Eksponensial
# Rata-rata 20 request per detik --> waktu antar request ~ Exp(20)
lam_req = 20
exp_dist = stats.expon(scale=1/lam_req)

print("=== Waktu Antar Request (Eksponensial) ===")
print(f"Mean waktu antar request: {exp_dist.mean()*1000:.1f} ms")
print(f"P(waktu > 100ms) = {1 - exp_dist.cdf(0.1):.4f}")

# Response time dari API: sering mengikuti distribusi log-normal
# Tapi jika banyak faktor independen, CLT membuat rata-rata mendekati Normal
print("\n=== Response Time API (Normal, berkat CLT) ===")
rt_dist = stats.norm(loc=200, scale=50)  # mean=200ms, std=50ms
print(f"P(response > 300ms) = {1 - rt_dist.cdf(300):.4f}")
print(f"P(response < 150ms) = {rt_dist.cdf(150):.4f}")
print(f"95% response time < {rt_dist.ppf(0.95):.1f} ms")
```

### 5.8.4 Tabel Ringkasan Aplikasi

| Domain Informatika | Distribusi yang Cocok | Contoh Variabel |
|--------------------|-----------------------|-----------------|
| Network traffic | Poisson | Jumlah paket per detik |
| Bug/defect rate | Poisson / Binomial | Bug per sprint, defect per 1000 LOC |
| Response time | Normal / Log-Normal | API latency (ms) |
| Waktu antar event | Eksponensial | Waktu antar request, time between failures |
| A/B testing | Binomial / Normal (CLT) | Conversion rate, click-through rate |
| Load testing | Normal (CLT) | Rata-rata throughput |
| Random number gen. | Uniform | Nilai random 0--1 |
| Queue simulation | Poisson + Eksponensial | Antrian request di server |

---

## 5.9 Toolkit `scipy.stats` --- Cheat Sheet

### 5.9.1 Fungsi Utama

`scipy.stats` menyediakan **interface yang konsisten** untuk semua distribusi probabilitas:

| Fungsi | Deskripsi | Pertanyaan yang Dijawab |
|--------|-----------|------------------------|
| `pmf(k)` | Probability Mass Function (diskret) | "Berapa P(X = k)?" |
| `pdf(x)` | Probability Density Function (kontinu) | "Berapa density di titik x?" |
| `cdf(x)` | Cumulative Distribution Function | "Berapa P(X <= x)?" |
| `sf(x)` | Survival Function = 1 - CDF | "Berapa P(X > x)?" |
| `ppf(q)` | Percent Point Function (inverse CDF) | "Nilai x di mana P(X <= x) = q?" |
| `rvs(size)` | Random Variates (generate sampel) | "Berikan saya n nilai acak dari distribusi ini" |
| `mean()` | Mean distribusi | Rata-rata teoritis |
| `var()` | Variance distribusi | Variansi teoritis |
| `std()` | Standar deviasi distribusi | Standar deviasi teoritis |

### 5.9.2 Cheat Sheet Kode

```python
# === CHEAT SHEET SCIPY.STATS ===
from scipy import stats
import numpy as np

# --- Distribusi Normal ---
normal = stats.norm(loc=70, scale=10)  # mean=70, std=10
print("=== Normal (mu=70, sigma=10) ===")
print(f"PDF di x=70   : {normal.pdf(70):.4f}")
print(f"CDF di x=80   : {normal.cdf(80):.4f}")     # P(X <= 80)
print(f"SF di x=80    : {normal.sf(80):.4f}")       # P(X > 80) = 1 - CDF
print(f"PPF di q=0.95 : {normal.ppf(0.95):.2f}")    # nilai untuk top 5%
print(f"3 random values: {normal.rvs(size=3).round(2)}")
print()

# --- Distribusi Binomial ---
binom = stats.binom(n=20, p=0.5)
print("=== Binomial (n=20, p=0.5) ===")
print(f"PMF di k=10   : {binom.pmf(10):.4f}")       # P(X = 10)
print(f"CDF di k=12   : {binom.cdf(12):.4f}")       # P(X <= 12)
print(f"PPF di q=0.95 : {binom.ppf(0.95)}")          # kuantil 95%
print(f"3 random values: {binom.rvs(size=3)}")
print()

# --- Distribusi Poisson ---
poisson = stats.poisson(mu=5)
print("=== Poisson (lambda=5) ===")
print(f"PMF di k=3    : {poisson.pmf(3):.4f}")
print(f"CDF di k=7    : {poisson.cdf(7):.4f}")
print(f"P(X > 8)      : {poisson.sf(8):.4f}")
print(f"3 random values: {poisson.rvs(size=3)}")
print()

# --- Distribusi Eksponensial ---
ekspon = stats.expon(scale=2)  # mean = 2 (scale = 1/lambda)
print("=== Eksponensial (lambda=0.5, mean=2) ===")
print(f"PDF di x=1    : {ekspon.pdf(1):.4f}")
print(f"CDF di x=3    : {ekspon.cdf(3):.4f}")
print(f"P(X > 5)      : {ekspon.sf(5):.4f}")
print(f"3 random values: {ekspon.rvs(size=3).round(2)}")
```

### 5.9.3 Tabel Referensi Cepat

| Distribusi | `scipy.stats` | Parameter | Contoh |
|------------|---------------|-----------|--------|
| Bernoulli | `stats.bernoulli(p)` | p = prob. sukses | `stats.bernoulli(0.7)` |
| Binomial | `stats.binom(n, p)` | n = percobaan, p = prob. sukses | `stats.binom(20, 0.5)` |
| Poisson | `stats.poisson(mu)` | mu = rata-rata kejadian | `stats.poisson(5)` |
| Uniform | `stats.uniform(loc, scale)` | loc = a, scale = b-a | `stats.uniform(0, 10)` |
| Normal | `stats.norm(loc, scale)` | loc = mu, scale = sigma | `stats.norm(70, 10)` |
| Eksponensial | `stats.expon(scale)` | scale = 1/lambda | `stats.expon(scale=2)` |
| Standard Normal | `stats.norm()` | mu=0, sigma=1 (default) | `stats.norm()` |

---

## AI Corner

### Menggunakan AI untuk Distribusi Probabilitas

AI assistant seperti ChatGPT dan Claude dapat menjadi *co-analyst* yang sangat berguna saat bekerja dengan distribusi probabilitas. Berikut panduan penggunaannya.

### Prompt yang Efektif

**Prompt 1 --- Memilih distribusi yang tepat:**
```
Saya punya data tentang jumlah email spam yang diterima karyawan per hari
di sebuah perusahaan. Data berupa bilangan cacahan (0, 1, 2, 3, ...).
Rata-rata 6 email spam per hari. Distribusi mana yang paling cocok
untuk memodelkan data ini, dan mengapa? Jelaskan syarat-syaratnya.
```

**Prompt 2 --- Memahami CLT secara intuitif:**
```
Jelaskan Central Limit Theorem seperti menjelaskan ke mahasiswa semester 2
yang baru pertama kali belajar statistik. Gunakan analogi sehari-hari
di Indonesia (misalnya terkait pengiriman paket atau antrian di kantin).
Sertakan contoh numerik sederhana.
```

**Prompt 3 --- Debugging kode distribusi:**
```
Kode Python saya menghasilkan error saat menghitung P(X > 10) untuk
distribusi Poisson dengan lambda = 7 menggunakan scipy.stats.
Berikut kodenya: [tempel kode].
Bantu debug dan jelaskan perbedaan antara pmf, cdf, dan sf.
```

**Prompt 4 --- Verifikasi jawaban:**
```
Saya menghitung P(X <= 3) untuk Binomial(n=10, p=0.4) secara manual
dan mendapatkan 0.3823. Apakah ini benar? Tunjukkan langkah perhitungannya
dan verifikasi dengan scipy.stats di Python.
```

### Apa yang Bisa dan Tidak Bisa Dilakukan AI

| AI Bisa Membantu | AI Tidak Bisa Menggantikan |
|-------------------|---------------------------|
| Menjelaskan konsep distribusi dengan analogi | Memahami konteks masalah Anda yang spesifik |
| Menyarankan distribusi yang tepat berdasarkan deskripsi data | Memutuskan apakah model cocok untuk data nyata |
| Men-generate kode Python yang benar | Menjamin hasil 100% akurat tanpa verifikasi |
| Membantu interpretasi output scipy.stats | Menggantikan pemahaman konseptual mahasiswa |
| Menjelaskan rumus matematika langkah demi langkah | Menilai apakah asumsi distribusi terpenuhi pada data riil |

### Etika Penggunaan

Ingat prinsip yang berlaku di mata kuliah ini:
- **Gunakan AI untuk memperdalam pemahaman**, bukan menggantikan proses belajar
- **Selalu jalankan kode sendiri** di Google Colab untuk memverifikasi
- **Dokumentasikan penggunaan AI** dalam AI Usage Log
- **Bandingkan jawaban AI** dengan materi kuliah dan referensi

---

## Rangkuman Bab 5

1. **Variabel random** memetakan hasil percobaan ke nilai numerik. Variabel random **diskret** memiliki nilai terhitung (PMF), sedangkan **kontinu** memiliki nilai dalam interval (PDF). Probabilitas kontinu dihitung melalui luas area di bawah kurva.

2. **Distribusi Binomial** B(n, p) menjawab pertanyaan "berapa kali sukses dari n percobaan independen?" dengan syarat: n tetap, dua hasil per percobaan, p konstan, dan independen. Mean = np, Variance = np(1-p).

3. **Distribusi Poisson** Pois($\lambda$) menjawab pertanyaan "berapa kejadian dalam suatu interval?" dengan ciri khas **Mean = Variance = $\lambda$**. Cocok untuk memodelkan kejadian langka seperti bug report, network traffic, dan error rate.

4. **Distribusi Normal** N($\mu$, $\sigma^2$) adalah distribusi terpenting dalam statistik, berbentuk lonceng simetris. Aturan Empiris: 68% data dalam $\mu \pm 1\sigma$, 95% dalam $\mu \pm 2\sigma$, dan 99.7% dalam $\mu \pm 3\sigma$.

5. **Z-score** mengstandarisasi nilai ke skala mean=0, std=1, memungkinkan perbandingan antar distribusi berbeda. Formula: z = (x - $\mu$) / $\sigma$. Nilai |z| > 3 mengindikasikan kemungkinan outlier.

6. **Central Limit Theorem (CLT)** menyatakan bahwa distribusi rata-rata sampel mendekati Normal untuk n yang cukup besar (umumnya n >= 30), **tidak peduli** bentuk distribusi populasi asalnya. CLT adalah fondasi confidence interval dan uji hipotesis.

7. **Standard Error** SE = $\sigma / \sqrt{n}$ mengukur variabilitas rata-rata sampel. Semakin besar n, semakin kecil SE, dan semakin akurat estimasi.

8. **`scipy.stats`** menyediakan interface konsisten (pmf/pdf, cdf, sf, ppf, rvs) untuk semua distribusi, memudahkan perhitungan probabilitas dan simulasi di Python.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan antara variabel random diskret dan kontinu. Berikan masing-masing dua contoh dalam konteks informatika.

**Soal 2.** Sebutkan empat syarat yang harus dipenuhi agar suatu situasi dapat dimodelkan dengan distribusi Binomial.

**Soal 3.** Distribusi Poisson memiliki ciri khas bahwa Mean = Variance = $\lambda$. Jelaskan secara intuitif mengapa hal ini masuk akal (petunjuk: pikirkan tentang variabilitas kejadian langka).

**Soal 4.** Apa yang dimaksud dengan aturan empiris (68-95-99.7 rule) pada distribusi Normal? Berikan contoh penerapannya untuk data tinggi badan mahasiswa dengan mean = 168 cm dan standar deviasi = 7 cm.

**Soal 5.** Jelaskan perbedaan antara PMF dan PDF. Mengapa P(X = x) = 0 untuk distribusi kontinu, dan bagaimana kita menghitung probabilitas pada distribusi kontinu?

### Tingkat Menengah (C2-C3)

**Soal 6.** Sebuah perusahaan fintech di Jakarta meluncurkan fitur baru. Dari data historis, 65% pengguna yang melihat halaman promosi akan melakukan registrasi. Jika 30 pengguna mengunjungi halaman tersebut:
- a) Tentukan distribusi yang sesuai dan parameternya
- b) Berapa expected value jumlah pengguna yang registrasi?
- c) Berapa probabilitas tepat 20 pengguna yang registrasi?
- d) Berapa probabilitas kurang dari 15 pengguna yang registrasi?
- e) Tulis kode Python menggunakan `scipy.stats` untuk menjawab semua pertanyaan di atas

**Soal 7.** Rata-rata terdapat 5 serangan DDoS per bulan yang terdeteksi oleh sistem keamanan suatu data center. Dengan asumsi serangan mengikuti distribusi Poisson:
- a) Berapa probabilitas tidak ada serangan dalam satu bulan?
- b) Berapa probabilitas terjadi lebih dari 8 serangan dalam satu bulan?
- c) Berapa probabilitas terjadi tepat 10 serangan dalam 2 bulan?
- d) Tulis kode Python untuk menghitung jawaban (a)-(c) dan buat plot PMF-nya

**Soal 8.** Waktu respons API sebuah layanan e-commerce berdistribusi Normal dengan mean = 250 ms dan standar deviasi = 40 ms.
- a) Berapa persen request memiliki response time kurang dari 200 ms?
- b) Berapa persen request memiliki response time antara 200 ms dan 300 ms?
- c) Berapa batas response time untuk 5% request paling lambat (persentil ke-95)?
- d) Jika SLA (*Service Level Agreement*) mensyaratkan 99% request di bawah threshold tertentu, berapa threshold tersebut?
- e) Seorang teknisi melaporkan response time 400 ms. Hitung z-score-nya dan tentukan apakah ini outlier.

**Soal 9.** Dua mahasiswa dibandingkan performanya:
- Aisyah mendapat 88 di Statistik (kelas: mean=72, std=8) dan 92 di Basis Data (kelas: mean=78, std=12)
- Bima mendapat 80 di Statistik dan 90 di Basis Data (dengan mean dan std yang sama)

Untuk masing-masing mahasiswa:
- a) Hitung z-score untuk kedua mata kuliah
- b) Tentukan di mata kuliah mana masing-masing mahasiswa lebih menonjol
- c) Hitung persentil masing-masing menggunakan tabel Normal standar atau `scipy.stats`

### Tingkat Mahir (C3-C4)

**Soal 10.** Modifikasi kode simulasi CLT di subbab 5.7.5 untuk menggunakan distribusi **Chi-squared** (`np.random.chisquare(df=3, size=n)`) sebagai populasi asal. Jalankan simulasi dengan n = 5, 30, dan 100.
- a) Apakah CLT tetap berlaku? Jelaskan pengamatan Anda.
- b) Untuk distribusi Chi-squared (yang sangat *skewed*), apakah n = 30 sudah cukup? Berapa n minimum agar distribusi rata-rata sampel terlihat Normal?
- c) Hitung SE teoritis dan bandingkan dengan hasil simulasi.

**Soal 11.** Sebuah tim DevOps memantau tiga metrik server:
- Jumlah error 500 per jam: rata-rata 3 error/jam
- Response time: mean = 180 ms, std = 35 ms
- Jumlah deployment per hari: dari 8 deployment terjadwal, probabilitas sukses masing-masing = 0.95

Untuk setiap metrik:
- a) Tentukan distribusi yang paling sesuai dan jelaskan alasannya
- b) Hitung probabilitas kejadian "buruk" (error > 7/jam, response > 250 ms, deployment sukses < 6)
- c) Tulis kode Python lengkap yang menghitung semua probabilitas dan buat visualisasi yang informatif

**Soal 12.** Sebuah startup e-commerce ingin melakukan A/B testing. Versi A (kontrol) memiliki conversion rate 4% dan versi B (treatment) memiliki conversion rate 5%. Masing-masing versi diuji dengan 500 pengguna.
- a) Modelkan jumlah konversi di masing-masing versi dengan distribusi Binomial
- b) Gunakan CLT untuk mendekati distribusi rata-rata konversi sebagai Normal. Hitung mean dan standard error untuk masing-masing versi.
- c) Simulasikan 10.000 kali pengambilan sampel untuk masing-masing versi. Plot distribusi rata-rata sampel dan tunjukkan bahwa CLT berlaku.
- d) Berdasarkan simulasi, estimasikan seberapa sering rata-rata versi B lebih tinggi dari versi A. (Ini adalah konsep dasar *statistical power* yang akan dipelajari lebih lanjut di bab selanjutnya.)

**Soal 13.** Buatlah sebuah fungsi Python `identify_distribution(data)` yang:
- a) Menerima input berupa array numpy
- b) Menghitung statistik deskriptif (mean, variance, skewness, kurtosis)
- c) Membandingkan mean dan variance --- jika hampir sama, sarankan Poisson
- d) Menguji normalitas menggunakan Shapiro-Wilk test (`scipy.stats.shapiro`)
- e) Membuat QQ-plot untuk visual assessment
- f) Mengembalikan rekomendasi distribusi beserta parameternya

Uji fungsi tersebut pada tiga dataset yang Anda generate sendiri: satu dari distribusi Normal, satu dari Poisson, dan satu dari Eksponensial.

---

## Referensi

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability & Statistics for Engineers & Scientists* (9th ed.). Pearson. --- Bab 5-6.
2. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics* (4th ed.). OpenIntro. --- Bab 4.
3. Downey, A. B. (2021). *Think Stats: Exploratory Data Analysis in Python* (2nd ed.). O'Reilly Media. --- Bab 3-6.
4. Moore, D. S., McCabe, G. P., & Craig, B. A. (2021). *Introduction to the Practice of Statistics* (10th ed.). W. H. Freeman. --- Bab 4-5.
5. SciPy Documentation. (2025). *scipy.stats --- Statistical Functions*. Retrieved from https://docs.scipy.org/doc/scipy/reference/stats.html
6. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
7. Wasserman, L. (2004). *All of Statistics: A Concise Course in Statistical Inference*. Springer. --- Bab 2-3.
8. Khan Academy. *Central Limit Theorem*. Retrieved from https://www.khanacademy.org/math/statistics-probability/sampling-distributions-library

---

*Bab berikutnya: **Bab 6 --- Sampling dan Estimasi Parameter***
