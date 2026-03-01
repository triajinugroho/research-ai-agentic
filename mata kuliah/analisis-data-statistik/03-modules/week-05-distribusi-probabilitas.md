# Minggu 5: Distribusi Probabilitas dan Central Limit Theorem

## Mata Kuliah: Analisis Data Statistik
### Prodi Informatika — Universitas Al Azhar Indonesia — Semester Genap 2025/2026

---

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Minggu** | 5 |
| **Topik** | Distribusi Probabilitas dan Central Limit Theorem |
| **CPMK** | CPMK-3: Menerapkan konsep probabilitas dan distribusi probabilitas untuk memodelkan ketidakpastian dalam data |
| **Sub-CPMK** | 5.1: Mengidentifikasi dan menerapkan distribusi probabilitas (Normal, Binomial, Poisson) |
| | 5.2: Menjelaskan dan mendemonstrasikan Central Limit Theorem |
| **Bloom's Taxonomy** | C3 (Apply) |
| **Durasi** | 100 menit (50 menit teori + 50 menit praktikum) |
| **Prasyarat** | Minggu 4 — Probabilitas Dasar dan Bayes' Theorem |
| **Tools** | Python, Google Colab, numpy, scipy.stats, matplotlib |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Membedakan** distribusi diskret dan kontinu serta kapan masing-masing digunakan
2. **Menghitung** probabilitas menggunakan distribusi Binomial, Poisson, dan Normal
3. **Menerapkan** z-score untuk standardisasi data
4. **Menjelaskan** Central Limit Theorem dan signifikansinya dalam statistik inferensial
5. **Menggunakan** `scipy.stats` untuk menghitung PDF, CDF, PPF, dan generate random variates
6. **Mensimulasikan** CLT menggunakan Python dan memvisualisasikan hasilnya

---

## Peta Konsep Minggu Ini

```
Distribusi Probabilitas
├── Distribusi Diskret
│   ├── Binomial (n, p) → "berapa kali sukses dari n percobaan?"
│   └── Poisson (λ) → "berapa kejadian dalam interval waktu/ruang?"
├── Distribusi Kontinu
│   ├── Uniform (a, b) → "semua nilai sama kemungkinannya"
│   └── Normal/Gaussian (μ, σ) → "bell curve, paling penting!"
├── Z-score dan Standardisasi
│   └── Mengubah distribusi apapun ke skala standar
└── Central Limit Theorem
    └── "Rata-rata sampel → Normal, tidak peduli distribusi asalnya"
```

---

## Bagian 1: Distribusi Diskret

### 1.1 Apa Itu Distribusi Probabilitas?

Distribusi probabilitas adalah fungsi matematika yang menggambarkan **semua kemungkinan nilai** dari suatu random variable beserta probabilitasnya.

**Analogi sederhana:**
- Bayangkan kamu melempar dadu 🎲. Distribusi probabilitasnya menjelaskan bahwa setiap angka (1-6) punya peluang 1/6.
- Bayangkan tinggi badan mahasiswa UAI. Distribusinya menjelaskan bahwa kebanyakan mahasiswa memiliki tinggi di sekitar rata-rata, sedikit yang sangat tinggi atau sangat pendek.

**Dua jenis utama:**

| Aspek | Diskret | Kontinu |
|-------|---------|---------|
| **Nilai** | Terhitung (0, 1, 2, ...) | Tak terhingga (bilangan real) |
| **Fungsi** | PMF (Probability Mass Function) | PDF (Probability Density Function) |
| **Contoh** | Jumlah mahasiswa hadir, cacat produk | Tinggi badan, waktu tunggu |
| **Probabilitas** | P(X = k) bisa > 0 | P(X = x) selalu = 0, gunakan interval |

### 1.2 Distribusi Binomial

**Kapan digunakan?**
Ketika kita punya **n percobaan independen**, masing-masing dengan probabilitas sukses **p**, dan kita ingin tahu: **berapa kali sukses terjadi?**

**Syarat (harus semua terpenuhi):**
1. Jumlah percobaan (n) tetap
2. Setiap percobaan hanya punya 2 hasil: sukses atau gagal
3. Probabilitas sukses (p) sama di setiap percobaan
4. Percobaan saling independen

**Formula:**

```
P(X = k) = C(n,k) * p^k * (1-p)^(n-k)

di mana:
  C(n,k) = n! / (k! * (n-k)!)  → kombinasi
  n = jumlah percobaan
  k = jumlah sukses yang diinginkan
  p = probabilitas sukses per percobaan
```

**Parameter:** n (jumlah percobaan) dan p (probabilitas sukses)

**Statistik penting:**
- Mean: E(X) = n * p
- Variance: Var(X) = n * p * (1-p)

**Contoh nyata di Indonesia:**
- Dari 20 mahasiswa, berapa yang lulus ujian jika probabilitas lulus = 0.75?
- Dari 10 produk UMKM, berapa yang cacat jika tingkat cacat = 5%?

**Kode Python:**

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# === DISTRIBUSI BINOMIAL ===
# Contoh: 20 mahasiswa ujian, probabilitas lulus = 0.75
n = 20  # jumlah percobaan
p = 0.75  # probabilitas sukses

# Membuat distribusi
binom_dist = stats.binom(n=n, p=p)

# Hitung probabilitas spesifik
print(f"P(X = 15) = {binom_dist.pmf(15):.4f}")  # tepat 15 lulus
print(f"P(X <= 12) = {binom_dist.cdf(12):.4f}")  # 12 atau kurang lulus
print(f"P(X > 18) = {1 - binom_dist.cdf(18):.4f}")  # lebih dari 18 lulus
print(f"Mean = {binom_dist.mean():.2f}")
print(f"Std Dev = {binom_dist.std():.2f}")

# Visualisasi
k_values = np.arange(0, n + 1)
probabilities = binom_dist.pmf(k_values)

plt.figure(figsize=(10, 5))
plt.bar(k_values, probabilities, color='steelblue', alpha=0.7, edgecolor='black')
plt.xlabel('Jumlah Mahasiswa Lulus (k)')
plt.ylabel('Probabilitas P(X = k)')
plt.title(f'Distribusi Binomial (n={n}, p={p})')
plt.xticks(k_values)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

### 1.3 Distribusi Poisson

**Kapan digunakan?**
Ketika kita ingin menghitung **jumlah kejadian** dalam suatu **interval waktu atau ruang** tertentu, di mana kejadian terjadi secara **acak dan independen** dengan **rata-rata konstan**.

**Syarat:**
1. Kejadian terjadi secara independen
2. Rata-rata kejadian (rate) konstan
3. Dua kejadian tidak bisa terjadi di titik yang persis sama

**Formula:**

```
P(X = k) = (λ^k * e^(-λ)) / k!

di mana:
  λ (lambda) = rata-rata jumlah kejadian per interval
  k = jumlah kejadian yang ingin dihitung probabilitasnya
  e = 2.71828... (bilangan Euler)
```

**Parameter:** lambda (rata-rata kejadian per interval)

**Statistik penting:**
- Mean: E(X) = lambda
- Variance: Var(X) = lambda (mean = variance, ciri khas Poisson!)

**Contoh nyata di Indonesia:**
- Rata-rata 3 kecelakaan per hari di jalan tol Jakarta-Cikampek. Berapa peluang terjadi 5 kecelakaan hari ini?
- Rata-rata 10 pengunjung per jam di kantin UAI. Berapa peluang lebih dari 15 pengunjung datang dalam 1 jam?

**Kode Python:**

```python
# === DISTRIBUSI POISSON ===
# Contoh: rata-rata 3 kecelakaan per hari
lam = 3  # lambda

poisson_dist = stats.poisson(mu=lam)

# Probabilitas
print(f"P(X = 5) = {poisson_dist.pmf(5):.4f}")  # tepat 5 kecelakaan
print(f"P(X <= 2) = {poisson_dist.cdf(2):.4f}")  # 2 atau kurang
print(f"P(X > 5) = {1 - poisson_dist.cdf(5):.4f}")  # lebih dari 5
print(f"Mean = {poisson_dist.mean():.2f}")
print(f"Variance = {poisson_dist.var():.2f}")  # sama dengan mean!

# Visualisasi
k_values = np.arange(0, 15)
probabilities = poisson_dist.pmf(k_values)

plt.figure(figsize=(10, 5))
plt.bar(k_values, probabilities, color='coral', alpha=0.7, edgecolor='black')
plt.xlabel('Jumlah Kecelakaan (k)')
plt.ylabel('Probabilitas P(X = k)')
plt.title(f'Distribusi Poisson (λ={lam})')
plt.xticks(k_values)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

### 1.4 Binomial vs Poisson: Kapan Pakai yang Mana?

| Aspek | Binomial | Poisson |
|-------|----------|---------|
| **Jumlah percobaan** | Tetap (n diketahui) | Tidak tetap (kejadian di interval) |
| **Pertanyaan** | "Berapa sukses dari n?" | "Berapa kejadian dalam interval?" |
| **Parameter** | n dan p | lambda saja |
| **Hubungan** | Jika n besar, p kecil → mendekati Poisson dengan lambda = n*p | - |

---

## Bagian 2: Distribusi Kontinu

### 2.1 Distribusi Uniform

**Konsep:** Semua nilai dalam interval [a, b] memiliki probabilitas yang **sama** untuk terjadi.

**Formula PDF:**

```
f(x) = 1 / (b - a)    untuk a <= x <= b
f(x) = 0              untuk x di luar [a, b]
```

**Statistik:**
- Mean: (a + b) / 2
- Variance: (b - a)^2 / 12

**Contoh:** Waktu kedatangan bus (antara 0-10 menit), random number generator.

### 2.2 Distribusi Normal (Gaussian) — "The King of Distributions"

**Mengapa distribusi Normal sangat penting?**

1. **Banyak fenomena alam** mengikuti distribusi Normal (tinggi badan, IQ, error pengukuran)
2. **Central Limit Theorem** menjamin rata-rata sampel mendekati Normal
3. **Banyak uji statistik** mengasumsikan data berdistribusi Normal
4. **Mudah dikarakterisasi** — hanya perlu 2 parameter: mean dan standard deviation

**Formula PDF:**

```
f(x) = (1 / (σ√(2π))) * e^(-(x-μ)² / (2σ²))

di mana:
  μ (mu) = mean (pusat distribusi)
  σ (sigma) = standard deviation (lebar distribusi)
  π = 3.14159...
  e = 2.71828...
```

**Sifat-sifat penting:**
1. Simetris terhadap mean (μ)
2. Mean = Median = Modus
3. Bentuk lonceng (bell curve)
4. **Aturan Empiris (68-95-99.7 Rule):**
   - 68% data berada dalam μ +/- 1σ
   - 95% data berada dalam μ +/- 2σ
   - 99.7% data berada dalam μ +/- 3σ

**Kode Python — Visualisasi Distribusi Normal:**

```python
# === DISTRIBUSI NORMAL ===
mu = 70     # mean (rata-rata nilai ujian)
sigma = 10  # standard deviation

normal_dist = stats.norm(loc=mu, scale=sigma)

# Generate x values
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
y = normal_dist.pdf(x)

# Visualisasi dengan 68-95-99.7 rule
fig, ax = plt.subplots(figsize=(12, 6))

# Plot PDF
ax.plot(x, y, 'k-', linewidth=2, label='PDF')

# Shade regions
ax.fill_between(x, y, where=(x >= mu-sigma) & (x <= mu+sigma),
                color='steelblue', alpha=0.4, label='68% (μ ± 1σ)')
ax.fill_between(x, y, where=(x >= mu-2*sigma) & (x <= mu+2*sigma),
                color='steelblue', alpha=0.2, label='95% (μ ± 2σ)')
ax.fill_between(x, y, where=(x >= mu-3*sigma) & (x <= mu+3*sigma),
                color='steelblue', alpha=0.1, label='99.7% (μ ± 3σ)')

ax.set_xlabel('Nilai Ujian')
ax.set_ylabel('Density')
ax.set_title(f'Distribusi Normal (μ={mu}, σ={sigma})')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Hitung probabilitas
print(f"P(X < 60) = {normal_dist.cdf(60):.4f}")       # nilai di bawah 60
print(f"P(60 < X < 80) = {normal_dist.cdf(80) - normal_dist.cdf(60):.4f}")
print(f"P(X > 90) = {1 - normal_dist.cdf(90):.4f}")    # nilai di atas 90
print(f"Nilai minimum untuk top 10% = {normal_dist.ppf(0.90):.2f}")
```

---

## Bagian 3: Z-Score dan Standardisasi

### 3.1 Apa Itu Z-Score?

Z-score mengubah nilai dari distribusi **apapun** ke **Standard Normal Distribution** (mean=0, std=1).

**Formula:**

```
z = (x - μ) / σ

di mana:
  x = nilai yang ingin di-standardisasi
  μ = mean populasi (atau sampel)
  σ = standard deviation populasi (atau sampel)
```

**Interpretasi z-score:**
- z = 0 → nilai tepat di mean
- z = 1 → nilai 1 standard deviation di atas mean
- z = -2 → nilai 2 standard deviation di bawah mean
- |z| > 3 → kemungkinan outlier!

### 3.2 Mengapa Standardisasi Penting?

1. **Membandingkan skala berbeda:** Nilai ujian Statistik (skala 0-100) vs nilai TOEFL (skala 0-677) — z-score membuat keduanya setara
2. **Mendeteksi outlier:** Nilai dengan |z| > 3 bisa dianggap outlier
3. **Dasar untuk uji statistik:** Banyak uji (z-test, t-test) menggunakan nilai standar

### 3.3 Contoh Praktis

```python
# === Z-SCORE DAN STANDARDISASI ===

# Contoh: membandingkan performa mahasiswa di dua ujian berbeda
# Ujian Statistik: mean=70, std=10, Ahmad dapat 85
# Ujian Pemrograman: mean=60, std=15, Ahmad dapat 80

z_statistik = (85 - 70) / 10  # = 1.5
z_pemrograman = (80 - 60) / 15  # = 1.33

print(f"Z-score Statistik Ahmad: {z_statistik:.2f}")
print(f"Z-score Pemrograman Ahmad: {z_pemrograman:.2f}")
print(f"\nAhmad lebih menonjol di Statistik karena z-score lebih tinggi!")

# Standardisasi dataset lengkap
np.random.seed(42)
nilai_ujian = np.random.normal(loc=70, scale=10, size=100)

z_scores = (nilai_ujian - nilai_ujian.mean()) / nilai_ujian.std()

# Visualisasi sebelum dan sesudah standardisasi
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.hist(nilai_ujian, bins=20, color='steelblue', alpha=0.7, edgecolor='black')
ax1.set_title(f'Nilai Asli (μ={nilai_ujian.mean():.1f}, σ={nilai_ujian.std():.1f})')
ax1.set_xlabel('Nilai')
ax1.set_ylabel('Frekuensi')

ax2.hist(z_scores, bins=20, color='coral', alpha=0.7, edgecolor='black')
ax2.set_title(f'Z-Scores (μ={z_scores.mean():.4f}, σ={z_scores.std():.4f})')
ax2.set_xlabel('Z-Score')
ax2.set_ylabel('Frekuensi')

plt.tight_layout()
plt.show()
```

---

## Bagian 4: Central Limit Theorem (CLT)

### 4.1 Pernyataan CLT

> **Central Limit Theorem:** Jika kita mengambil banyak sampel berukuran n dari **populasi apapun** (distribusi apapun, asalkan variance terhingga), maka **distribusi rata-rata sampel** akan mendekati **distribusi Normal** seiring bertambahnya n — **tidak peduli** bagaimana bentuk distribusi asalnya.

**Secara matematis:**

```
Jika X₁, X₂, ..., Xₙ sampel acak dari populasi dengan mean μ dan std σ,
maka untuk n cukup besar:

X̄ ~ Normal(μ, σ/√n)

di mana:
  X̄ = rata-rata sampel
  μ = mean populasi
  σ/√n = standard error of the mean
```

### 4.2 Mengapa CLT Sangat Penting?

CLT adalah **fondasi** dari hampir semua inferensi statistik:

1. **Confidence interval** — mengasumsikan distribusi rata-rata sampel mendekati Normal
2. **Uji hipotesis** — z-test dan t-test mengandalkan CLT
3. **Estimasi parameter** — semua bergantung pada distribusi sampling

**Analogi sederhana:**
Bayangkan kamu mengumpulkan data tinggi badan semua mahasiswa UAI. Data aslinya mungkin agak miring (skewed). Tapi jika kamu mengambil 100 sampel, masing-masing 30 orang, lalu hitung rata-rata tiap sampel — 100 rata-rata itu akan membentuk kurva Normal yang indah!

### 4.3 Berapa Besar n yang "Cukup Besar"?

| Distribusi Asal | n Minimum yang Direkomendasikan |
|-----------------|--------------------------------|
| Sudah mendekati Normal | n >= 10 sudah cukup |
| Sedikit skewed | n >= 30 (rule of thumb klasik) |
| Sangat skewed | n >= 50 atau lebih |
| Distribusi apapun | n >= 30 biasanya aman |

### 4.4 Simulasi CLT dengan Python

Ini adalah bagian paling menarik dari modul ini. Kita akan **membuktikan** CLT secara empiris!

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
        Fungsi yang menghasilkan random sample (misal: np.random.exponential)
    dist_name : str
        Nama distribusi untuk judul plot
    sample_sizes : list
        Daftar ukuran sampel yang akan dicoba
    n_simulations : int
        Berapa kali pengambilan sampel dilakukan
    """

    fig, axes = plt.subplots(1, len(sample_sizes) + 1, figsize=(18, 4))

    # Plot distribusi asli
    original_data = distribution_func(size=10000)
    axes[0].hist(original_data, bins=50, color='lightgray', edgecolor='black',
                 alpha=0.7, density=True)
    axes[0].set_title(f'Distribusi Asli\n{dist_name}')
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
                         label='Normal fit')

        axes[i + 1].set_title(f'Rata-rata Sampel\nn={n}')
        axes[i + 1].legend(fontsize=8)

    plt.suptitle(f'Central Limit Theorem — {dist_name}', fontsize=14,
                 fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.show()

# 1. Distribusi Exponential (sangat skewed ke kanan)
print("=" * 60)
print("1. DISTRIBUSI EXPONENTIAL (sangat skewed)")
print("=" * 60)
simulate_clt(
    lambda size: np.random.exponential(scale=2, size=size),
    "Exponential (λ=2)"
)

# 2. Distribusi Uniform (flat, bukan Normal sama sekali)
print("\n" + "=" * 60)
print("2. DISTRIBUSI UNIFORM (flat)")
print("=" * 60)
simulate_clt(
    lambda size: np.random.uniform(low=0, high=10, size=size),
    "Uniform (0, 10)"
)

# 3. Distribusi Binomial (diskret, bisa skewed)
print("\n" + "=" * 60)
print("3. DISTRIBUSI BINOMIAL (diskret)")
print("=" * 60)
simulate_clt(
    lambda size: np.random.binomial(n=5, p=0.2, size=size),
    "Binomial (n=5, p=0.2)"
)
```

**Yang harus diperhatikan dari simulasi:**
1. Kolom pertama: distribusi asli (masing-masing berbeda bentuk)
2. Kolom ke-2 (n=5): distribusi rata-rata sampel mulai berubah, tapi belum Normal
3. Kolom ke-3 (n=30): sudah cukup mirip Normal!
4. Kolom ke-4 (n=100): sangat mendekati Normal, hampir sempurna

---

## Bagian 5: scipy.stats — Toolkit Distribusi di Python

### 5.1 Fungsi Utama untuk Setiap Distribusi

`scipy.stats` menyediakan interface yang **konsisten** untuk semua distribusi:

| Fungsi | Deskripsi | Contoh |
|--------|-----------|--------|
| `pdf(x)` / `pmf(k)` | Probability Density/Mass Function | "Berapa density/probabilitas di titik x?" |
| `cdf(x)` | Cumulative Distribution Function | "P(X <= x) = ?" |
| `ppf(q)` | Percent Point Function (inverse CDF) | "Nilai x di mana P(X <= x) = q" |
| `rvs(size)` | Random Variates (generate sampel) | "Generate 1000 nilai acak dari distribusi ini" |
| `mean()` | Mean distribusi | Rata-rata teoritis |
| `var()` | Variance distribusi | Variance teoritis |

### 5.2 Cheat Sheet scipy.stats

```python
# === CHEAT SHEET SCIPY.STATS ===

# --- Distribusi Normal ---
normal = stats.norm(loc=70, scale=10)  # mean=70, std=10
print("=== Normal (μ=70, σ=10) ===")
print(f"PDF di x=70: {normal.pdf(70):.4f}")
print(f"CDF di x=80: {normal.cdf(80):.4f}")    # P(X <= 80)
print(f"PPF di q=0.95: {normal.ppf(0.95):.2f}")  # nilai untuk top 5%
print(f"5 random values: {normal.rvs(size=5).round(2)}")

print()

# --- Distribusi Binomial ---
binom = stats.binom(n=20, p=0.5)
print("=== Binomial (n=20, p=0.5) ===")
print(f"PMF di k=10: {binom.pmf(10):.4f}")     # P(X = 10)
print(f"CDF di k=12: {binom.cdf(12):.4f}")     # P(X <= 12)
print(f"PPF di q=0.95: {binom.ppf(0.95)}")      # kuantil 95%
print(f"5 random values: {binom.rvs(size=5)}")

print()

# --- Distribusi Poisson ---
poisson = stats.poisson(mu=5)
print("=== Poisson (λ=5) ===")
print(f"PMF di k=3: {poisson.pmf(3):.4f}")
print(f"CDF di k=7: {poisson.cdf(7):.4f}")
print(f"P(X > 8): {1 - poisson.cdf(8):.4f}")
print(f"5 random values: {poisson.rvs(size=5)}")
```

### 5.3 Visualisasi Perbandingan Distribusi

```python
# === PERBANDINGAN VISUAL SEMUA DISTRIBUSI ===

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Binomial
ax = axes[0, 0]
for n, p in [(20, 0.3), (20, 0.5), (20, 0.7)]:
    k = np.arange(0, n + 1)
    ax.plot(k, stats.binom.pmf(k, n, p), 'o-', label=f'n={n}, p={p}')
ax.set_title('Distribusi Binomial')
ax.set_xlabel('k')
ax.set_ylabel('P(X = k)')
ax.legend()
ax.grid(alpha=0.3)

# 2. Poisson
ax = axes[0, 1]
for lam in [1, 3, 7, 15]:
    k = np.arange(0, 25)
    ax.plot(k, stats.poisson.pmf(k, lam), 'o-', label=f'λ={lam}')
ax.set_title('Distribusi Poisson')
ax.set_xlabel('k')
ax.set_ylabel('P(X = k)')
ax.legend()
ax.grid(alpha=0.3)

# 3. Normal
ax = axes[1, 0]
x = np.linspace(-10, 20, 200)
for mu, sigma in [(0, 1), (5, 1), (5, 2), (5, 3)]:
    ax.plot(x, stats.norm.pdf(x, mu, sigma), label=f'μ={mu}, σ={sigma}')
ax.set_title('Distribusi Normal')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.grid(alpha=0.3)

# 4. Uniform
ax = axes[1, 1]
for a, b in [(0, 1), (0, 5), (2, 8)]:
    x = np.linspace(-1, 10, 200)
    ax.plot(x, stats.uniform.pdf(x, a, b - a), label=f'[{a}, {b}]')
ax.set_title('Distribusi Uniform')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()
ax.grid(alpha=0.3)

plt.suptitle('Perbandingan Distribusi Probabilitas', fontsize=14,
             fontweight='bold')
plt.tight_layout()
plt.show()
```

---

## Bagian 6: AI Corner

### Prompt untuk AI Assistant

Kamu bisa bertanya ke AI assistant untuk memperdalam pemahaman. Berikut contoh prompt yang berguna:

**Prompt 1 — Penjelasan CLT:**
> "Jelaskan Central Limit Theorem seperti kamu menjelaskan ke anak SMA yang pintar tapi belum pernah belajar statistik. Gunakan analogi sehari-hari."

**Prompt 2 — Memilih distribusi:**
> "Saya punya data tentang jumlah kecelakaan per hari di jalan tol. Distribusi mana yang paling cocok dan mengapa? Jelaskan step by step."

**Prompt 3 — Debugging kode:**
> "Kode Python saya untuk simulasi CLT menghasilkan error [tempel error]. Bantu saya debug dan jelaskan apa yang salah."

**Catatan penting:** Selalu **verifikasi** jawaban AI dengan:
1. Menjalankan kode sendiri di Colab
2. Membandingkan dengan materi kuliah
3. Menanyakan "Apakah ada kelemahan dari penjelasan ini?"

---

## Rangkuman

| Konsep | Poin Utama |
|--------|-----------|
| **Binomial** | n percobaan, p sukses, hitung jumlah sukses |
| **Poisson** | Hitung kejadian per interval, parameter lambda |
| **Normal** | Bell curve, mu dan sigma, 68-95-99.7 rule |
| **Z-score** | Standardisasi: z = (x - mu) / sigma |
| **CLT** | Rata-rata sampel mendekati Normal untuk n cukup besar |
| **scipy.stats** | pdf/pmf, cdf, ppf, rvs — interface konsisten |

---

## Latihan Mandiri

1. **Latihan Binomial:** Di sebuah kelas UAI, 80% mahasiswa lulus mata kuliah Statistik. Jika diambil sampel 25 mahasiswa, berapa probabilitas tepat 20 yang lulus?

2. **Latihan Poisson:** Rata-rata ada 4 email spam per jam. Berapa probabilitas menerima 0 email spam dalam 1 jam?

3. **Latihan Normal:** Nilai UTS di sebuah kelas berdistribusi Normal dengan mean=68, std=12. Berapa persen mahasiswa mendapat nilai di atas 80?

4. **Latihan Z-score:** Dua mahasiswa: Budi dapat 90 di Statistik (mean=75, std=8) dan 85 di Pemrograman (mean=70, std=10). Di mata kuliah mana Budi lebih menonjol?

5. **Latihan CLT:** Modifikasi kode simulasi CLT di atas dengan distribusi baru: **Chi-squared** (`np.random.chisquare(df=3, size=n)`). Apakah CLT tetap berlaku?

---

## Asesmen Minggu Ini

- **Lab 05:** Distribusi dengan scipy.stats (dikerjakan saat praktikum)
- **Tugas 3:** Simulasi Distribusi & CLT (deadline: Minggu 6 sebelum kelas)
  - Detail tugas: lihat RTM

---

## Referensi

1. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics (4th ed.)*. Chapter 4.
2. Downey, A. B. (2021). *Think Stats (2nd ed.)*. Chapters 3-6.
3. scipy.stats documentation: https://docs.scipy.org/doc/scipy/reference/stats.html

---

## Persiapan Minggu Depan

Minggu 6 akan membahas **Sampling dan Estimasi**. Untuk persiapan:
- Review konsep populasi vs sampel
- Baca Diez et al. (2019) Chapter 5, bagian awal tentang sampling
- Pastikan memahami CLT — karena CLT adalah fondasi untuk confidence interval!

---

*Modul ini merupakan bagian dari mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia.*
