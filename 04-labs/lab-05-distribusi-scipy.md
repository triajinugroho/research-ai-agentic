# Lab 05: Distribusi Probabilitas dengan scipy.stats

**Mata Kuliah:** Statistika dan Probabilitas
**Program Studi:** Universitas Al Azhar Indonesia
**Minggu:** 5
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. Menggunakan `scipy.stats` untuk bekerja dengan distribusi probabilitas
2. Men-generate dan memvisualisasikan distribusi Normal, Binomial, dan Poisson
3. Menghitung probabilitas menggunakan CDF dan PPF (inverse CDF)
4. Mensimulasikan dan memvisualisasikan Central Limit Theorem (CLT)
5. Menghitung dan menginterpretasikan Z-score

---

## Persiapan

- Google Colab notebook baru
- Nama file: `Lab05_NamaAnda_NIM.ipynb`
- Library: numpy, scipy.stats, matplotlib, seaborn

---

## Langkah-langkah

### Langkah 1: Setup

```python
# =============================================
# LANGKAH 1: Setup
# =============================================

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

plt.rcParams['figure.dpi'] = 100
sns.set_style("whitegrid")
np.random.seed(42)

print("Setup selesai!")
print(f"scipy version: {stats.__name__} dari scipy {__import__('scipy').__version__}")
```

### Langkah 2: Distribusi Normal

```python
# =============================================
# LANGKAH 2: Distribusi Normal (Gaussian)
# =============================================

# Parameter distribusi normal
mu = 170    # rata-rata tinggi badan (cm)
sigma = 8   # standar deviasi

# Membuat objek distribusi
normal_dist = stats.norm(loc=mu, scale=sigma)

# Generate data dari distribusi
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
pdf = normal_dist.pdf(x)   # Probability Density Function
cdf = normal_dist.cdf(x)   # Cumulative Distribution Function

# Visualisasi PDF dan CDF
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# PDF
axes[0].plot(x, pdf, 'b-', linewidth=2)
axes[0].fill_between(x, pdf, alpha=0.15, color='blue')
axes[0].axvline(mu, color='red', linestyle='--', label=f'Mean = {mu}')
axes[0].axvline(mu - sigma, color='orange', linestyle=':', label=f'Mean - 1 SD = {mu-sigma}')
axes[0].axvline(mu + sigma, color='orange', linestyle=':', label=f'Mean + 1 SD = {mu+sigma}')
axes[0].set_title(f'PDF: Normal(mu={mu}, sigma={sigma})', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Tinggi Badan (cm)')
axes[0].set_ylabel('Density')
axes[0].legend(fontsize=9)

# CDF
axes[1].plot(x, cdf, 'r-', linewidth=2)
axes[1].axhline(0.5, color='gray', linestyle='--', alpha=0.5)
axes[1].axvline(mu, color='gray', linestyle='--', alpha=0.5)
axes[1].set_title(f'CDF: Normal(mu={mu}, sigma={sigma})', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Tinggi Badan (cm)')
axes[1].set_ylabel('P(X <= x)')

plt.tight_layout()
plt.show()

# Properti distribusi
print("=== PROPERTI DISTRIBUSI NORMAL ===")
print(f"Mean     : {normal_dist.mean():.2f}")
print(f"Median   : {normal_dist.median():.2f}")
print(f"Variance : {normal_dist.var():.2f}")
print(f"Std Dev  : {normal_dist.std():.2f}")
```

### Langkah 3: Menghitung Probabilitas dengan CDF

```python
# =============================================
# LANGKAH 3: Menghitung Probabilitas
# =============================================

# Konteks: Tinggi badan mahasiswa ~ Normal(170, 8)

print("=" * 55)
print("MENGHITUNG PROBABILITAS - DISTRIBUSI NORMAL")
print(f"X ~ Normal(mu={mu}, sigma={sigma})")
print("=" * 55)

# 1. P(X < 165) - probabilitas tinggi badan kurang dari 165
p1 = normal_dist.cdf(165)
print(f"\n1. P(X < 165) = {p1:.4f} ({p1*100:.2f}%)")

# 2. P(X > 180) = 1 - P(X <= 180)
p2 = 1 - normal_dist.cdf(180)
print(f"2. P(X > 180) = {p2:.4f} ({p2*100:.2f}%)")

# 3. P(162 < X < 178) = P(X < 178) - P(X < 162)
p3 = normal_dist.cdf(178) - normal_dist.cdf(162)
print(f"3. P(162 < X < 178) = {p3:.4f} ({p3*100:.2f}%)")

# 4. P(mu - 1*sigma < X < mu + 1*sigma) - aturan 68-95-99.7
p_1sd = normal_dist.cdf(mu + sigma) - normal_dist.cdf(mu - sigma)
p_2sd = normal_dist.cdf(mu + 2*sigma) - normal_dist.cdf(mu - 2*sigma)
p_3sd = normal_dist.cdf(mu + 3*sigma) - normal_dist.cdf(mu - 3*sigma)
print(f"\n--- Aturan Empiris (68-95-99.7) ---")
print(f"P(mu +/- 1 SD) = {p_1sd:.4f} ({p_1sd*100:.2f}%) [teori: 68.27%]")
print(f"P(mu +/- 2 SD) = {p_2sd:.4f} ({p_2sd*100:.2f}%) [teori: 95.45%]")
print(f"P(mu +/- 3 SD) = {p_3sd:.4f} ({p_3sd*100:.2f}%) [teori: 99.73%]")

# Visualisasi area probabilitas
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, pdf, 'b-', linewidth=2)

# Shade P(162 < X < 178)
x_fill = np.linspace(162, 178, 300)
ax.fill_between(x_fill, normal_dist.pdf(x_fill), alpha=0.3, color='green',
                label=f'P(162 < X < 178) = {p3:.4f}')

# Shade P(X < 165)
x_fill2 = np.linspace(mu - 4*sigma, 165, 300)
ax.fill_between(x_fill2, normal_dist.pdf(x_fill2), alpha=0.3, color='red',
                label=f'P(X < 165) = {p1:.4f}')

ax.set_title('Visualisasi Probabilitas pada Distribusi Normal', fontsize=13, fontweight='bold')
ax.set_xlabel('Tinggi Badan (cm)')
ax.set_ylabel('Density')
ax.legend(fontsize=10)
plt.tight_layout()
plt.show()
```

### Langkah 4: PPF (Inverse CDF) - Mencari Nilai dari Probabilitas

```python
# =============================================
# LANGKAH 4: PPF (Percent Point Function)
# =============================================

print("=" * 55)
print("PPF: MENCARI NILAI DARI PROBABILITAS")
print("=" * 55)

# 1. Berapa tinggi badan pada persentil ke-90?
p90 = normal_dist.ppf(0.90)
print(f"\n1. Persentil ke-90: {p90:.2f} cm")
print(f"   (90% mahasiswa memiliki tinggi badan < {p90:.2f} cm)")

# 2. Berapa tinggi badan pada persentil ke-25 dan ke-75?
p25 = normal_dist.ppf(0.25)
p75 = normal_dist.ppf(0.75)
print(f"\n2. Q1 (persentil ke-25): {p25:.2f} cm")
print(f"   Q3 (persentil ke-75): {p75:.2f} cm")
print(f"   IQR = {p75 - p25:.2f} cm")

# 3. Berapa batas atas dan bawah untuk 95% data tengah?
batas_bawah_95 = normal_dist.ppf(0.025)
batas_atas_95 = normal_dist.ppf(0.975)
print(f"\n3. 95% data tengah berada di: [{batas_bawah_95:.2f}, {batas_atas_95:.2f}] cm")

# 4. Nilai kritis z untuk berbagai confidence level
print(f"\n--- Nilai Kritis Z ---")
for cl in [0.90, 0.95, 0.99]:
    alpha = 1 - cl
    z_crit = stats.norm.ppf(1 - alpha/2)  # two-tailed
    print(f"  Confidence {cl*100:.0f}%: z* = +/- {z_crit:.4f}")
```

### Langkah 5: Distribusi Binomial

```python
# =============================================
# LANGKAH 5: Distribusi Binomial
# =============================================

# Konteks: Ujian pilihan ganda, 20 soal, 4 opsi per soal
# Jika menjawab acak, P(benar) = 1/4 = 0.25

n_soal = 20
p_benar = 0.25

binom_dist = stats.binom(n=n_soal, p=p_benar)

# PMF (Probability Mass Function)
k = np.arange(0, n_soal + 1)
pmf = binom_dist.pmf(k)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# PMF
axes[0].bar(k, pmf, color='steelblue', edgecolor='white')
axes[0].set_title(f'PMF: Binomial(n={n_soal}, p={p_benar})', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Jumlah Jawaban Benar (k)')
axes[0].set_ylabel('P(X = k)')

# CDF
cdf_binom = binom_dist.cdf(k)
axes[1].step(k, cdf_binom, color='coral', linewidth=2, where='mid')
axes[1].set_title(f'CDF: Binomial(n={n_soal}, p={p_benar})', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Jumlah Jawaban Benar (k)')
axes[1].set_ylabel('P(X <= k)')

plt.tight_layout()
plt.show()

# Perhitungan probabilitas
print("=" * 55)
print(f"DISTRIBUSI BINOMIAL: n={n_soal}, p={p_benar}")
print("=" * 55)
print(f"Mean (expected value): {binom_dist.mean():.2f} soal benar")
print(f"Std Dev: {binom_dist.std():.2f}")

print(f"\nP(X = 5) = {binom_dist.pmf(5):.4f} (tepat 5 benar)")
print(f"P(X >= 10) = {1 - binom_dist.cdf(9):.4f} (lulus jika >= 10 benar)")
print(f"P(X <= 3) = {binom_dist.cdf(3):.4f} (3 atau kurang benar)")
print(f"P(X >= 5) = {1 - binom_dist.cdf(4):.6f} (minimal 5 benar)")
```

### Langkah 6: Distribusi Poisson

```python
# =============================================
# LANGKAH 6: Distribusi Poisson
# =============================================

# Konteks: Rata-rata 3 pengunjung per jam datang ke perpustakaan

lam = 3  # lambda (rata-rata)
poisson_dist = stats.poisson(mu=lam)

k = np.arange(0, 15)
pmf_pois = poisson_dist.pmf(k)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# PMF Poisson
axes[0].bar(k, pmf_pois, color='#2ecc71', edgecolor='white')
axes[0].set_title(f'PMF: Poisson(lambda={lam})', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Jumlah Pengunjung (k)')
axes[0].set_ylabel('P(X = k)')

# Beberapa lambda berbeda
for lam_i, color in [(1, '#3498db'), (3, '#2ecc71'), (5, '#e74c3c'), (10, '#9b59b6')]:
    pmf_i = stats.poisson.pmf(k, mu=lam_i)
    axes[1].plot(k, pmf_i, 'o-', color=color, label=f'lambda = {lam_i}', markersize=5)

axes[1].set_title('Perbandingan Distribusi Poisson', fontsize=13, fontweight='bold')
axes[1].set_xlabel('k')
axes[1].set_ylabel('P(X = k)')
axes[1].legend()

plt.tight_layout()
plt.show()

# Perhitungan
print("=" * 55)
print(f"DISTRIBUSI POISSON: lambda={lam}")
print("=" * 55)
print(f"Mean: {poisson_dist.mean():.2f}")
print(f"Variance: {poisson_dist.var():.2f}")
print(f"Std Dev: {poisson_dist.std():.2f}")
print(f"\nP(X = 0) = {poisson_dist.pmf(0):.4f} (tidak ada pengunjung)")
print(f"P(X = 3) = {poisson_dist.pmf(3):.4f} (tepat 3 pengunjung)")
print(f"P(X >= 5) = {1 - poisson_dist.cdf(4):.4f} (5 atau lebih)")
print(f"P(X <= 2) = {poisson_dist.cdf(2):.4f} (2 atau kurang)")
```

### Langkah 7: Perbandingan Tiga Distribusi

```python
# =============================================
# LANGKAH 7: Perbandingan Distribusi
# =============================================

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Normal
x_norm = np.linspace(-4, 4, 1000)
for mu_i, sigma_i in [(0, 1), (0, 2), (2, 1)]:
    label = f'N({mu_i}, {sigma_i})'
    axes[0].plot(x_norm, stats.norm.pdf(x_norm, mu_i, sigma_i), label=label, linewidth=2)
axes[0].set_title('Distribusi Normal', fontsize=12, fontweight='bold')
axes[0].set_xlabel('x')
axes[0].set_ylabel('Density')
axes[0].legend()

# Binomial
k_binom = np.arange(0, 31)
for n_i, p_i in [(30, 0.3), (30, 0.5), (30, 0.7)]:
    label = f'B({n_i}, {p_i})'
    axes[1].plot(k_binom, stats.binom.pmf(k_binom, n_i, p_i), 'o-',
                 label=label, markersize=4)
axes[1].set_title('Distribusi Binomial', fontsize=12, fontweight='bold')
axes[1].set_xlabel('k')
axes[1].set_ylabel('P(X = k)')
axes[1].legend()

# Poisson
k_pois = np.arange(0, 20)
for lam_i in [1, 4, 8]:
    label = f'Pois({lam_i})'
    axes[2].plot(k_pois, stats.poisson.pmf(k_pois, lam_i), 'o-',
                 label=label, markersize=4)
axes[2].set_title('Distribusi Poisson', fontsize=12, fontweight='bold')
axes[2].set_xlabel('k')
axes[2].set_ylabel('P(X = k)')
axes[2].legend()

plt.suptitle('Perbandingan Tiga Distribusi Probabilitas', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

### Langkah 8: Central Limit Theorem (CLT)

```python
# =============================================
# LANGKAH 8: Central Limit Theorem
# =============================================

# CLT: Rata-rata dari n sampel mendekati distribusi normal
# meskipun populasi asli TIDAK normal

# Populasi: Distribusi Uniform (jelas bukan normal)
pop_min, pop_max = 0, 100
pop_mean = (pop_min + pop_max) / 2    # 50
pop_std = (pop_max - pop_min) / np.sqrt(12)  # ~28.87

n_experiments = 1000  # jumlah percobaan
sample_sizes = [5, 30, 100]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Distribusi populasi (uniform)
populasi = np.random.uniform(pop_min, pop_max, size=100_000)
axes[0, 0].hist(populasi, bins=50, color='gray', edgecolor='white', density=True, alpha=0.7)
axes[0, 0].set_title('Populasi: Uniform(0, 100)', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Nilai')
axes[0, 0].set_ylabel('Density')
axes[0, 0].axvline(pop_mean, color='red', linestyle='--', label=f'Mean = {pop_mean}')
axes[0, 0].legend()

# Plot 2-4: Distribusi sample means untuk n = 5, 30, 100
colors = ['#e74c3c', '#3498db', '#2ecc71']

for idx, n_size in enumerate(sample_sizes):
    ax = axes[(idx + 1) // 2, (idx + 1) % 2]

    # Ambil 1000 sampel, masing-masing berukuran n_size
    sample_means = np.array([
        np.random.uniform(pop_min, pop_max, size=n_size).mean()
        for _ in range(n_experiments)
    ])

    # Plot histogram
    ax.hist(sample_means, bins=40, color=colors[idx], edgecolor='white',
            density=True, alpha=0.7, label=f'Simulasi (n={n_size})')

    # Overlay distribusi normal teoritis (CLT)
    x_theo = np.linspace(sample_means.min(), sample_means.max(), 200)
    se = pop_std / np.sqrt(n_size)  # Standard Error
    ax.plot(x_theo, stats.norm.pdf(x_theo, pop_mean, se), 'k-',
            linewidth=2, label=f'Normal(mu={pop_mean}, SE={se:.2f})')

    ax.set_title(f'Sample Means: n = {n_size} ({n_experiments} sampel)',
                 fontsize=12, fontweight='bold')
    ax.set_xlabel('Rata-rata Sampel')
    ax.set_ylabel('Density')
    ax.legend(fontsize=9)

    # Statistik
    print(f"n={n_size:>3}: Mean sampel = {sample_means.mean():.2f}, "
          f"SD sampel = {sample_means.std():.2f}, "
          f"SE teoritis = {se:.2f}")

plt.suptitle('CENTRAL LIMIT THEOREM\nDistribusi Rata-rata Sampel dari Populasi Uniform',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

### Langkah 9: CLT dari Distribusi Eksponensial

```python
# =============================================
# LANGKAH 9: CLT dari Distribusi Eksponensial (Non-Normal)
# =============================================

# Distribusi eksponensial: sangat skewed
lam_exp = 2  # rate parameter
pop_mean_exp = 1 / lam_exp
pop_std_exp = 1 / lam_exp

fig, axes = plt.subplots(1, 4, figsize=(18, 4))

# Populasi eksponensial
exp_pop = np.random.exponential(1/lam_exp, size=100_000)
axes[0].hist(exp_pop, bins=50, color='gray', edgecolor='white', density=True, alpha=0.7)
axes[0].set_title(f'Populasi: Exp(lambda={lam_exp})', fontsize=11, fontweight='bold')
axes[0].set_xlabel('x')

for idx, n_size in enumerate([5, 30, 100]):
    ax = axes[idx + 1]
    means = np.array([
        np.random.exponential(1/lam_exp, size=n_size).mean()
        for _ in range(1000)
    ])

    ax.hist(means, bins=40, color=colors[idx], edgecolor='white',
            density=True, alpha=0.7)

    se = pop_std_exp / np.sqrt(n_size)
    x_t = np.linspace(means.min(), means.max(), 200)
    ax.plot(x_t, stats.norm.pdf(x_t, pop_mean_exp, se), 'k-', linewidth=2)
    ax.set_title(f'n = {n_size}', fontsize=11, fontweight='bold')
    ax.set_xlabel('Rata-rata Sampel')

plt.suptitle('CLT dari Distribusi Eksponensial (Sangat Skewed)',
             fontsize=13, fontweight='bold', y=1.04)
plt.tight_layout()
plt.show()

print("Meskipun populasi sangat skewed (eksponensial),")
print("distribusi sample means mendekati normal saat n cukup besar!")
```

### Langkah 10: Z-Score

```python
# =============================================
# LANGKAH 10: Z-Score
# =============================================

# Konteks: Nilai ujian mahasiswa ~ Normal(75, 10)
mu_ujian = 75
sigma_ujian = 10

# Generate data nilai
np.random.seed(42)
nilai_ujian = np.random.normal(mu_ujian, sigma_ujian, size=100).round(1)

# Hitung Z-score
z_scores = (nilai_ujian - mu_ujian) / sigma_ujian

print("=" * 55)
print("Z-SCORE ANALYSIS")
print("=" * 55)

# Contoh perhitungan
contoh_nilai = [55, 75, 85, 95]
for nv in contoh_nilai:
    z = (nv - mu_ujian) / sigma_ujian
    percentile = stats.norm.cdf(z) * 100
    print(f"Nilai {nv}: Z = {z:+.2f}, Persentil = {percentile:.1f}%")

# Berapa nilai minimum untuk masuk top 10%?
z_top10 = stats.norm.ppf(0.90)
nilai_top10 = mu_ujian + z_top10 * sigma_ujian
print(f"\nUntuk masuk top 10%: nilai minimal = {nilai_top10:.1f} (Z = {z_top10:.2f})")

# Berapa nilai minimum agar tidak remedial (bottom 5%)?
z_bottom5 = stats.norm.ppf(0.05)
nilai_remedial = mu_ujian + z_bottom5 * sigma_ujian
print(f"Batas remedial (bottom 5%): nilai < {nilai_remedial:.1f} (Z = {z_bottom5:.2f})")

# Visualisasi Z-score
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Distribusi nilai asli
axes[0].hist(nilai_ujian, bins=20, color='steelblue', edgecolor='white', density=True, alpha=0.7)
x_plot = np.linspace(40, 110, 200)
axes[0].plot(x_plot, stats.norm.pdf(x_plot, mu_ujian, sigma_ujian), 'r-', linewidth=2)
axes[0].axvline(nilai_top10, color='green', linestyle='--', label=f'Top 10%: {nilai_top10:.1f}')
axes[0].axvline(nilai_remedial, color='orange', linestyle='--', label=f'Remedial: {nilai_remedial:.1f}')
axes[0].set_title('Distribusi Nilai Ujian', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Nilai')
axes[0].set_ylabel('Density')
axes[0].legend(fontsize=9)

# Distribusi Z-score
axes[1].hist(z_scores, bins=20, color='coral', edgecolor='white', density=True, alpha=0.7)
z_plot = np.linspace(-4, 4, 200)
axes[1].plot(z_plot, stats.norm.pdf(z_plot, 0, 1), 'b-', linewidth=2)
axes[1].axvline(0, color='red', linestyle='--', alpha=0.5)
axes[1].set_title('Distribusi Z-Score (Standardized)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Z-Score')
axes[1].set_ylabel('Density')

plt.tight_layout()
plt.show()

# Tabel Z-score umum
print("\n--- Tabel Z-Score Umum ---")
z_values = [-3, -2.576, -2.326, -2, -1.96, -1.645, -1, 0, 1, 1.645, 1.96, 2, 2.326, 2.576, 3]
print(f"{'Z':>8} | {'P(Z < z)':>10} | {'P(Z > z)':>10}")
print("-" * 35)
for z in z_values:
    p = stats.norm.cdf(z)
    print(f"{z:>8.3f} | {p:>10.4f} | {1-p:>10.4f}")
```

---

## Tugas yang Harus Dikumpulkan

Kumpulkan notebook (.ipynb) yang berisi:

1. **Semua kode** dari Langkah 1-10 yang sudah dijalankan (tanpa error)
2. **Soal-soal berikut** (jawab di code cell + text cell interpretasi):
   - Jika X ~ Normal(mu=500, sigma=100), hitung:
     a. P(X > 650)
     b. P(400 < X < 600)
     c. Nilai x sehingga P(X < x) = 0.95
   - Jika X ~ Binomial(n=50, p=0.6), hitung:
     a. P(X = 30)
     b. P(X >= 35)
     c. E(X) dan Var(X)
   - Simulasi CLT menggunakan distribusi Bernoulli(p=0.3) dengan n = 5, 30, 100
3. **Interpretasi CLT** dalam 2-3 paragraf: apa yang terjadi saat n bertambah?

---

## Rubrik Singkat

| Kriteria | Bobot | Keterangan |
|----------|-------|------------|
| Kelengkapan kode (Langkah 1-10) | 25% | Semua cell berjalan tanpa error |
| Soal perhitungan probabilitas | 30% | Jawaban benar dan disertai kode |
| Simulasi CLT tambahan | 20% | Simulasi Bernoulli benar dan divisualisasikan |
| Interpretasi tertulis | 15% | Penjelasan CLT jelas dan menunjukkan pemahaman |
| Kerapian notebook | 10% | Terstruktur rapi |

---

## Challenge / Bonus

```python
# =============================================
# CHALLENGE: QQ-Plot dan Uji Normalitas
# =============================================

# Apakah data berdistribusi normal? Gunakan QQ-Plot dan Shapiro-Wilk test

# Generate 3 dataset berbeda
np.random.seed(42)
data_normal = np.random.normal(50, 10, 200)
data_skewed = np.random.exponential(5, 200)
data_uniform = np.random.uniform(20, 80, 200)

datasets = {
    'Normal': data_normal,
    'Eksponensial (Skewed)': data_skewed,
    'Uniform': data_uniform
}

fig, axes = plt.subplots(3, 2, figsize=(12, 14))

for idx, (nama, data) in enumerate(datasets.items()):
    # Histogram
    axes[idx, 0].hist(data, bins=25, color='steelblue', edgecolor='white', density=True, alpha=0.7)
    x_fit = np.linspace(data.min(), data.max(), 100)
    mu_fit, sigma_fit = data.mean(), data.std()
    axes[idx, 0].plot(x_fit, stats.norm.pdf(x_fit, mu_fit, sigma_fit), 'r-', linewidth=2)
    axes[idx, 0].set_title(f'Histogram: {nama}', fontsize=11, fontweight='bold')

    # QQ-Plot
    stats.probplot(data, dist='norm', plot=axes[idx, 1])
    axes[idx, 1].set_title(f'QQ-Plot: {nama}', fontsize=11, fontweight='bold')

    # Shapiro-Wilk test
    stat_sw, p_sw = stats.shapiro(data)
    print(f"{nama:>25}: Shapiro-Wilk stat={stat_sw:.4f}, p-value={p_sw:.4f} "
          f"-> {'Normal' if p_sw > 0.05 else 'TIDAK Normal'} (alpha=0.05)")

plt.tight_layout()
plt.show()

print("\nInterpretasi QQ-Plot:")
print("- Jika titik mengikuti garis diagonal -> data normal")
print("- Jika titik melengkung -> data tidak normal (skewed/heavy-tailed)")
```

---

> **Referensi:**
> - [scipy.stats documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)
> - Khan Academy: [Central Limit Theorem](https://www.khanacademy.org/math/statistics-probability/sampling-distributions-library)
