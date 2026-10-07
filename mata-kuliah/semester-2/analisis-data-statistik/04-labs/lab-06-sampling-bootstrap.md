# Lab 06: Sampling dan Bootstrap

**Mata Kuliah:** Statistika dan Probabilitas
**Program Studi:** Universitas Al Azhar Indonesia
**Minggu:** 6
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. Mensimulasikan populasi dan mengambil sampel dengan berbagai ukuran
2. Memahami variabilitas sampling melalui simulasi
3. Mengimplementasikan metode bootstrap dari nol (from scratch)
4. Menghitung dan memvisualisasikan bootstrap confidence interval
5. Membandingkan bootstrap CI dengan confidence interval berbasis rumus

---

## Persiapan

- Google Colab notebook baru
- Nama file: `Lab06_NamaAnda_NIM.ipynb`
- Library: numpy, scipy.stats, matplotlib, seaborn

---

## Langkah-langkah

### Langkah 1: Setup dan Membuat Populasi

```python
# =============================================
# LANGKAH 1: Setup dan Populasi
# =============================================

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

plt.rcParams['figure.dpi'] = 100
sns.set_style("whitegrid")
np.random.seed(42)

# Buat populasi simulasi: Penghasilan bulanan (Juta Rp)
# Distribusi log-normal (realistis untuk data penghasilan)
N_populasi = 100_000
populasi = np.random.lognormal(mean=1.8, sigma=0.6, size=N_populasi)

# Parameter populasi (yang sebenarnya -- biasanya tidak diketahui)
mu_pop = populasi.mean()
sigma_pop = populasi.std()
median_pop = np.median(populasi)

print("=" * 55)
print("PARAMETER POPULASI (N = {:,})".format(N_populasi))
print("=" * 55)
print(f"Mean (mu)     : {mu_pop:.4f} juta")
print(f"Median        : {median_pop:.4f} juta")
print(f"Std Dev (sigma): {sigma_pop:.4f} juta")
print(f"Min           : {populasi.min():.4f} juta")
print(f"Max           : {populasi.max():.4f} juta")

# Visualisasi populasi
plt.figure(figsize=(10, 5))
plt.hist(populasi, bins=100, color='steelblue', edgecolor='white', density=True, alpha=0.7)
plt.axvline(mu_pop, color='red', linestyle='--', linewidth=2, label=f'Mean = {mu_pop:.2f}')
plt.axvline(median_pop, color='green', linestyle='--', linewidth=2, label=f'Median = {median_pop:.2f}')
plt.title('Distribusi Populasi: Penghasilan Bulanan', fontsize=14, fontweight='bold')
plt.xlabel('Penghasilan (Juta Rp)')
plt.ylabel('Density')
plt.legend(fontsize=11)
plt.xlim(0, 40)
plt.tight_layout()
plt.show()
```

### Langkah 2: Mengambil Sampel dan Melihat Variabilitas

```python
# =============================================
# LANGKAH 2: Sampling dan Variabilitas
# =============================================

# Ambil beberapa sampel dengan ukuran berbeda
sample_sizes = [10, 30, 100, 500]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

for idx, n in enumerate(sample_sizes):
    ax = axes[idx // 2, idx % 2]

    # Ambil 5 sampel berbeda untuk ukuran yang sama
    for i in range(5):
        sampel = np.random.choice(populasi, size=n, replace=False)
        ax.hist(sampel, bins=20, alpha=0.3, density=True, label=f'Sampel {i+1} (mean={sampel.mean():.2f})')

    ax.axvline(mu_pop, color='red', linestyle='--', linewidth=2, label=f'Pop Mean = {mu_pop:.2f}')
    ax.set_title(f'5 Sampel dengan n = {n}', fontsize=12, fontweight='bold')
    ax.set_xlabel('Penghasilan (Juta Rp)')
    ax.set_ylabel('Density')
    ax.legend(fontsize=7)
    ax.set_xlim(0, 30)

plt.suptitle('Variabilitas Sampling: Sampel Berbeda Menghasilkan Statistik Berbeda',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

### Langkah 3: Distribusi Sampling

```python
# =============================================
# LANGKAH 3: Distribusi Sampling dari Mean
# =============================================

n_experiments = 2000  # jumlah sampel yang diambil

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
colors = ['#e74c3c', '#3498db', '#2ecc71', '#9b59b6']

for idx, n in enumerate(sample_sizes):
    ax = axes[idx // 2, idx % 2]

    # Ambil 2000 sampel dan hitung mean masing-masing
    sample_means = np.array([
        np.random.choice(populasi, size=n, replace=False).mean()
        for _ in range(n_experiments)
    ])

    # Histogram distribusi sampling
    ax.hist(sample_means, bins=50, color=colors[idx], edgecolor='white',
            density=True, alpha=0.7)

    # Overlay normal curve (CLT)
    se = sigma_pop / np.sqrt(n)  # Standard Error
    x_theo = np.linspace(sample_means.min(), sample_means.max(), 200)
    ax.plot(x_theo, stats.norm.pdf(x_theo, mu_pop, se), 'k-', linewidth=2)

    ax.axvline(mu_pop, color='red', linestyle='--', linewidth=2)
    ax.set_title(f'Distribusi Sample Means (n={n})\n'
                 f'SE teoritis={se:.3f}, SE simulasi={sample_means.std():.3f}',
                 fontsize=11, fontweight='bold')
    ax.set_xlabel('Sample Mean')
    ax.set_ylabel('Density')

plt.suptitle('DISTRIBUSI SAMPLING: Semakin Besar n, Semakin Sempit Distribusi',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()

# Tabel ringkasan
print("=" * 65)
print(f"{'n':>6} | {'Mean of Means':>14} | {'SE (simulasi)':>14} | {'SE (teoritis)':>14}")
print("=" * 65)
for n in sample_sizes:
    means = np.array([
        np.random.choice(populasi, size=n, replace=False).mean()
        for _ in range(2000)
    ])
    se_sim = means.std()
    se_teo = sigma_pop / np.sqrt(n)
    print(f"{n:>6} | {means.mean():>14.4f} | {se_sim:>14.4f} | {se_teo:>14.4f}")
```

### Langkah 4: Bootstrap -- Konsep

```python
# =============================================
# LANGKAH 4: Konsep Bootstrap
# =============================================

# Bootstrap: teknik resampling DENGAN pengembalian (with replacement)
# dari SAMPEL yang kita punya, untuk mengestimasi variabilitas statistik

# Dalam praktik nyata, kita TIDAK tahu parameter populasi
# Kita hanya punya SATU SAMPEL

# Ambil satu sampel dari populasi (ini yang kita "punya")
n_sampel = 50
sampel_kita = np.random.choice(populasi, size=n_sampel, replace=False)

print("=" * 55)
print("DATA SAMPEL KITA (n=50)")
print("=" * 55)
print(f"Mean sampel  : {sampel_kita.mean():.4f} juta")
print(f"Median sampel: {np.median(sampel_kita):.4f} juta")
print(f"Std sampel   : {sampel_kita.std(ddof=1):.4f} juta")
print(f"\n(Parameter populasi yang sebenarnya -- biasanya tidak diketahui)")
print(f"Mean populasi: {mu_pop:.4f} juta")

plt.figure(figsize=(10, 4))
plt.hist(sampel_kita, bins=15, color='coral', edgecolor='white', alpha=0.8)
plt.axvline(sampel_kita.mean(), color='blue', linestyle='--', linewidth=2,
            label=f'Sample Mean = {sampel_kita.mean():.2f}')
plt.axvline(mu_pop, color='red', linestyle='--', linewidth=2,
            label=f'Pop Mean = {mu_pop:.2f} (tidak diketahui)')
plt.title('Sampel Kita (n=50)', fontsize=13, fontweight='bold')
plt.xlabel('Penghasilan (Juta Rp)')
plt.ylabel('Frekuensi')
plt.legend()
plt.tight_layout()
plt.show()
```

### Langkah 5: Implementasi Bootstrap dari Nol

```python
# =============================================
# LANGKAH 5: Bootstrap dari Nol (From Scratch)
# =============================================

def bootstrap_statistic(data, stat_func, n_bootstrap=10_000):
    """
    Implementasi bootstrap resampling.

    Parameters:
    - data: array data sampel
    - stat_func: fungsi statistik (np.mean, np.median, dll)
    - n_bootstrap: jumlah resample

    Returns:
    - bootstrap_stats: array statistik dari setiap resample
    """
    n = len(data)
    bootstrap_stats = np.zeros(n_bootstrap)

    for i in range(n_bootstrap):
        # Resample WITH replacement (ukuran sama dengan data asli)
        resample = np.random.choice(data, size=n, replace=True)
        # Hitung statistik dari resample
        bootstrap_stats[i] = stat_func(resample)

    return bootstrap_stats

# Jalankan bootstrap untuk MEAN
n_boot = 10_000
boot_means = bootstrap_statistic(sampel_kita, np.mean, n_bootstrap=n_boot)

print("=" * 55)
print(f"BOOTSTRAP RESULTS (B={n_boot:,} resamples)")
print("=" * 55)
print(f"Original sample mean: {sampel_kita.mean():.4f}")
print(f"Bootstrap mean of means: {boot_means.mean():.4f}")
print(f"Bootstrap SE: {boot_means.std():.4f}")
print(f"Formula SE (s/sqrt(n)): {sampel_kita.std(ddof=1)/np.sqrt(n_sampel):.4f}")

# Visualisasi
plt.figure(figsize=(10, 5))
plt.hist(boot_means, bins=50, color='steelblue', edgecolor='white',
         density=True, alpha=0.7, label='Bootstrap Distribution')
plt.axvline(sampel_kita.mean(), color='blue', linestyle='--', linewidth=2,
            label=f'Sample Mean = {sampel_kita.mean():.2f}')
plt.axvline(mu_pop, color='red', linestyle='--', linewidth=2,
            label=f'Pop Mean = {mu_pop:.2f}')
plt.title(f'Bootstrap Distribution of the Mean (B={n_boot:,})',
          fontsize=14, fontweight='bold')
plt.xlabel('Bootstrap Sample Mean')
plt.ylabel('Density')
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()
```

### Langkah 6: Bootstrap Confidence Interval

```python
# =============================================
# LANGKAH 6: Bootstrap Confidence Interval
# =============================================

# Metode 1: Percentile Method
alpha = 0.05  # 95% confidence
ci_lower_pct = np.percentile(boot_means, 100 * alpha/2)
ci_upper_pct = np.percentile(boot_means, 100 * (1 - alpha/2))

# Metode 2: Basic (Reverse Percentile) Method
ci_lower_basic = 2 * sampel_kita.mean() - ci_upper_pct
ci_upper_basic = 2 * sampel_kita.mean() - ci_lower_pct

# Metode 3: Bootstrap SE Method (Normal approximation)
boot_se = boot_means.std()
z_crit = stats.norm.ppf(1 - alpha/2)
ci_lower_se = sampel_kita.mean() - z_crit * boot_se
ci_upper_se = sampel_kita.mean() + z_crit * boot_se

print("=" * 60)
print("BOOTSTRAP 95% CONFIDENCE INTERVAL")
print("=" * 60)
print(f"\nOriginal sample mean: {sampel_kita.mean():.4f}")
print(f"Population mean (truth): {mu_pop:.4f}")
print(f"\nMetode 1 - Percentile:  [{ci_lower_pct:.4f}, {ci_upper_pct:.4f}]")
print(f"Metode 2 - Basic:       [{ci_lower_basic:.4f}, {ci_upper_basic:.4f}]")
print(f"Metode 3 - SE (Normal): [{ci_lower_se:.4f}, {ci_upper_se:.4f}]")

# Apakah CI menangkap parameter populasi?
for nama, lo, hi in [('Percentile', ci_lower_pct, ci_upper_pct),
                      ('Basic', ci_lower_basic, ci_upper_basic),
                      ('SE', ci_lower_se, ci_upper_se)]:
    captured = lo <= mu_pop <= hi
    print(f"\n{nama}: {'MENANGKAP' if captured else 'TIDAK menangkap'} mu populasi ({mu_pop:.4f})")

# Visualisasi
plt.figure(figsize=(12, 5))
plt.hist(boot_means, bins=50, color='steelblue', edgecolor='white',
         density=True, alpha=0.7)

# Shade CI area
plt.axvspan(ci_lower_pct, ci_upper_pct, alpha=0.2, color='green',
            label=f'95% CI Percentile: [{ci_lower_pct:.2f}, {ci_upper_pct:.2f}]')
plt.axvline(sampel_kita.mean(), color='blue', linestyle='--', linewidth=2,
            label=f'Sample Mean: {sampel_kita.mean():.2f}')
plt.axvline(mu_pop, color='red', linestyle='-', linewidth=2,
            label=f'Pop Mean: {mu_pop:.2f}')
plt.axvline(ci_lower_pct, color='green', linestyle='-', linewidth=2)
plt.axvline(ci_upper_pct, color='green', linestyle='-', linewidth=2)

plt.title('Bootstrap 95% Confidence Interval for the Mean',
          fontsize=14, fontweight='bold')
plt.xlabel('Bootstrap Sample Mean')
plt.ylabel('Density')
plt.legend(fontsize=9)
plt.tight_layout()
plt.show()
```

### Langkah 7: Perbandingan Bootstrap CI vs Formula CI

```python
# =============================================
# LANGKAH 7: Bootstrap CI vs Formula CI
# =============================================

# Formula-based CI: x_bar +/- t * (s / sqrt(n))
x_bar = sampel_kita.mean()
s = sampel_kita.std(ddof=1)
n = len(sampel_kita)
se_formula = s / np.sqrt(n)

# t-critical value (df = n-1)
t_crit = stats.t.ppf(1 - alpha/2, df=n-1)

ci_lower_formula = x_bar - t_crit * se_formula
ci_upper_formula = x_bar + t_crit * se_formula

print("=" * 60)
print("PERBANDINGAN: Bootstrap CI vs Formula CI (95%)")
print("=" * 60)
print(f"Sample mean: {x_bar:.4f}")
print(f"Sample std:  {s:.4f}")
print(f"n:           {n}")
print(f"SE (formula): {se_formula:.4f}")
print(f"SE (bootstrap): {boot_se:.4f}")
print(f"t-critical (df={n-1}): {t_crit:.4f}")

print(f"\n{'Metode':<20} {'CI Lower':>10} {'CI Upper':>10} {'Width':>10}")
print("-" * 55)
methods = [
    ('Formula (t)', ci_lower_formula, ci_upper_formula),
    ('Boot Percentile', ci_lower_pct, ci_upper_pct),
    ('Boot Basic', ci_lower_basic, ci_upper_basic),
    ('Boot SE', ci_lower_se, ci_upper_se),
]
for name, lo, hi in methods:
    print(f"{name:<20} {lo:>10.4f} {hi:>10.4f} {hi-lo:>10.4f}")

# Visualisasi perbandingan
fig, ax = plt.subplots(figsize=(10, 4))

method_names = ['Formula (t)', 'Boot Percentile', 'Boot Basic', 'Boot SE']
lowers = [ci_lower_formula, ci_lower_pct, ci_lower_basic, ci_lower_se]
uppers = [ci_upper_formula, ci_upper_pct, ci_upper_basic, ci_upper_se]
colors_ci = ['#e74c3c', '#3498db', '#2ecc71', '#9b59b6']

for i, (name, lo, hi, c) in enumerate(zip(method_names, lowers, uppers, colors_ci)):
    ax.plot([lo, hi], [i, i], 'o-', color=c, linewidth=3, markersize=8, label=name)

ax.axvline(mu_pop, color='red', linestyle='--', linewidth=2, alpha=0.7, label=f'Pop Mean = {mu_pop:.2f}')
ax.axvline(x_bar, color='blue', linestyle=':', linewidth=2, alpha=0.7, label=f'Sample Mean = {x_bar:.2f}')
ax.set_yticks(range(len(method_names)))
ax.set_yticklabels(method_names)
ax.set_xlabel('Penghasilan (Juta Rp)')
ax.set_title('Perbandingan 95% Confidence Intervals', fontsize=13, fontweight='bold')
ax.legend(loc='upper right', fontsize=9)
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 8: Coverage Probability (Simulasi)

```python
# =============================================
# LANGKAH 8: Coverage Probability
# =============================================

# Pertanyaan: Apakah 95% CI benar-benar menangkap mu 95% dari waktu?
# Simulasi: Ambil banyak sampel, hitung CI, cek berapa persen yang menangkap mu

n_experiments = 200
n_sampel = 50
n_boot_each = 2000

captured_boot = 0
captured_formula = 0

ci_results = []

for exp in range(n_experiments):
    # Ambil sampel baru
    samp = np.random.choice(populasi, size=n_sampel, replace=False)
    xbar = samp.mean()
    s_samp = samp.std(ddof=1)

    # Bootstrap CI (Percentile)
    boot_m = np.array([
        np.random.choice(samp, size=n_sampel, replace=True).mean()
        for _ in range(n_boot_each)
    ])
    ci_boot_lo = np.percentile(boot_m, 2.5)
    ci_boot_hi = np.percentile(boot_m, 97.5)

    # Formula CI (t-interval)
    se_f = s_samp / np.sqrt(n_sampel)
    t_c = stats.t.ppf(0.975, df=n_sampel-1)
    ci_form_lo = xbar - t_c * se_f
    ci_form_hi = xbar + t_c * se_f

    # Check coverage
    boot_ok = ci_boot_lo <= mu_pop <= ci_boot_hi
    form_ok = ci_form_lo <= mu_pop <= ci_form_hi
    captured_boot += boot_ok
    captured_formula += form_ok

    ci_results.append({
        'xbar': xbar, 'boot_lo': ci_boot_lo, 'boot_hi': ci_boot_hi,
        'form_lo': ci_form_lo, 'form_hi': ci_form_hi,
        'boot_ok': boot_ok, 'form_ok': form_ok
    })

coverage_boot = captured_boot / n_experiments * 100
coverage_form = captured_formula / n_experiments * 100

print("=" * 55)
print(f"COVERAGE PROBABILITY ({n_experiments} experiments)")
print("=" * 55)
print(f"Bootstrap Percentile CI: {coverage_boot:.1f}% (target: 95%)")
print(f"Formula t-interval CI  : {coverage_form:.1f}% (target: 95%)")

# Visualisasi: 50 CI pertama
fig, axes = plt.subplots(1, 2, figsize=(14, 10))

n_show = 50
for ax_idx, (ci_type, lo_key, hi_key, ok_key, title) in enumerate([
    ('Bootstrap', 'boot_lo', 'boot_hi', 'boot_ok', f'Bootstrap Percentile CI (Coverage={coverage_boot:.1f}%)'),
    ('Formula', 'form_lo', 'form_hi', 'form_ok', f'Formula t-interval CI (Coverage={coverage_form:.1f}%)')
]):
    ax = axes[ax_idx]
    for i in range(n_show):
        r = ci_results[i]
        color = 'green' if r[ok_key] else 'red'
        ax.plot([r[lo_key], r[hi_key]], [i, i], '-', color=color, linewidth=1.5, alpha=0.7)
        ax.plot(r['xbar'], i, 'o', color=color, markersize=3)

    ax.axvline(mu_pop, color='black', linestyle='--', linewidth=2, label=f'mu = {mu_pop:.2f}')
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.set_xlabel('Penghasilan (Juta Rp)')
    ax.set_ylabel('Experiment #')
    ax.legend()

plt.suptitle('Coverage Probability: 95% CI\n(Hijau = menangkap mu, Merah = tidak)',
             fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

### Langkah 9: Bootstrap untuk Statistik Lain (Median, Std)

```python
# =============================================
# LANGKAH 9: Bootstrap untuk Median dan Std Dev
# =============================================

# Bootstrap bisa digunakan untuk STATISTIK APAPUN, bukan hanya mean!

sampel_kita_2 = np.random.choice(populasi, size=50, replace=False)

# Bootstrap median
boot_medians = bootstrap_statistic(sampel_kita_2, np.median, n_bootstrap=10_000)

# Bootstrap standard deviation
boot_stds = bootstrap_statistic(sampel_kita_2, lambda x: np.std(x, ddof=1), n_bootstrap=10_000)

# Bootstrap IQR
boot_iqrs = bootstrap_statistic(
    sampel_kita_2,
    lambda x: np.percentile(x, 75) - np.percentile(x, 25),
    n_bootstrap=10_000
)

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Median
axes[0].hist(boot_medians, bins=50, color='#3498db', edgecolor='white', alpha=0.7)
ci_med = np.percentile(boot_medians, [2.5, 97.5])
axes[0].axvline(ci_med[0], color='red', linestyle='--')
axes[0].axvline(ci_med[1], color='red', linestyle='--')
axes[0].axvline(median_pop, color='green', linestyle='-', linewidth=2, label=f'Pop Median={median_pop:.2f}')
axes[0].set_title(f'Bootstrap Median\n95% CI: [{ci_med[0]:.2f}, {ci_med[1]:.2f}]',
                   fontsize=11, fontweight='bold')
axes[0].legend(fontsize=9)

# Std Dev
axes[1].hist(boot_stds, bins=50, color='#e74c3c', edgecolor='white', alpha=0.7)
ci_std = np.percentile(boot_stds, [2.5, 97.5])
axes[1].axvline(ci_std[0], color='red', linestyle='--')
axes[1].axvline(ci_std[1], color='red', linestyle='--')
axes[1].axvline(sigma_pop, color='green', linestyle='-', linewidth=2, label=f'Pop Std={sigma_pop:.2f}')
axes[1].set_title(f'Bootstrap Std Dev\n95% CI: [{ci_std[0]:.2f}, {ci_std[1]:.2f}]',
                   fontsize=11, fontweight='bold')
axes[1].legend(fontsize=9)

# IQR
axes[2].hist(boot_iqrs, bins=50, color='#2ecc71', edgecolor='white', alpha=0.7)
ci_iqr = np.percentile(boot_iqrs, [2.5, 97.5])
pop_iqr = np.percentile(populasi, 75) - np.percentile(populasi, 25)
axes[2].axvline(ci_iqr[0], color='red', linestyle='--')
axes[2].axvline(ci_iqr[1], color='red', linestyle='--')
axes[2].axvline(pop_iqr, color='green', linestyle='-', linewidth=2, label=f'Pop IQR={pop_iqr:.2f}')
axes[2].set_title(f'Bootstrap IQR\n95% CI: [{ci_iqr[0]:.2f}, {ci_iqr[1]:.2f}]',
                   fontsize=11, fontweight='bold')
axes[2].legend(fontsize=9)

plt.suptitle('Bootstrap CI untuk Berbagai Statistik', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

### Langkah 10: Pengaruh Ukuran Sampel pada Bootstrap CI

```python
# =============================================
# LANGKAH 10: Ukuran Sampel vs Lebar CI
# =============================================

sample_sizes_test = [10, 20, 30, 50, 100, 200, 500]
ci_widths_boot = []
ci_widths_formula = []

for n in sample_sizes_test:
    samp = np.random.choice(populasi, size=n, replace=False)

    # Bootstrap CI
    b_means = np.array([
        np.random.choice(samp, size=n, replace=True).mean()
        for _ in range(5000)
    ])
    ci_b = np.percentile(b_means, [2.5, 97.5])
    ci_widths_boot.append(ci_b[1] - ci_b[0])

    # Formula CI
    se_f = samp.std(ddof=1) / np.sqrt(n)
    t_c = stats.t.ppf(0.975, df=n-1)
    ci_f_width = 2 * t_c * se_f
    ci_widths_formula.append(ci_f_width)

# Visualisasi
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(sample_sizes_test, ci_widths_boot, 'o-', color='#3498db',
        linewidth=2, markersize=8, label='Bootstrap CI Width')
ax.plot(sample_sizes_test, ci_widths_formula, 's--', color='#e74c3c',
        linewidth=2, markersize=8, label='Formula CI Width')
ax.set_xlabel('Ukuran Sampel (n)', fontsize=12)
ax.set_ylabel('Lebar 95% CI', fontsize=12)
ax.set_title('Pengaruh Ukuran Sampel terhadap Lebar Confidence Interval',
             fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print("=" * 55)
print("LEBAR CI vs UKURAN SAMPEL")
print("=" * 55)
print(f"{'n':>6} | {'Boot CI Width':>14} | {'Formula CI Width':>16}")
print("-" * 42)
for n, bw, fw in zip(sample_sizes_test, ci_widths_boot, ci_widths_formula):
    print(f"{n:>6} | {bw:>14.4f} | {fw:>16.4f}")

print("\nKesimpulan: Semakin besar n, semakin sempit CI")
print("(estimasi kita semakin presisi)")
```

---

## Tugas yang Harus Dikumpulkan

Kumpulkan notebook (.ipynb) yang berisi:

1. **Semua kode** dari Langkah 1-10 yang sudah dijalankan (tanpa error)
2. **Tugas tambahan:**
   - Lakukan bootstrap untuk **median** penghasilan (dari sampel_kita) dan bandingkan CI percentile vs CI SE
   - Buat populasi baru dengan distribusi **bimodal** (campuran dua normal), ambil sampel, dan lakukan bootstrap. Apakah bootstrap masih bekerja dengan baik?
3. **Interpretasi tertulis** (2-3 paragraf):
   - Jelaskan perbedaan antara standard deviation dan standard error
   - Kapan sebaiknya menggunakan bootstrap dibanding formula CI?

---

## Rubrik Singkat

| Kriteria | Bobot | Keterangan |
|----------|-------|------------|
| Kelengkapan kode (Langkah 1-10) | 25% | Semua cell berjalan tanpa error |
| Bootstrap median + perbandingan | 20% | Implementasi benar, CI dihitung |
| Populasi bimodal + bootstrap | 20% | Kreativitas dan analisis tepat |
| Interpretasi tertulis | 20% | Pemahaman SE vs SD, kapan bootstrap |
| Kerapian notebook | 15% | Terstruktur rapi dengan text cell |

---

## Challenge / Bonus

```python
# =============================================
# CHALLENGE: Permutation Test (Uji Permutasi)
# =============================================

# Pertanyaan: Apakah rata-rata penghasilan Kota vs Pedesaan berbeda?

np.random.seed(42)
penghasilan_kota = np.random.lognormal(2.0, 0.5, size=40)
penghasilan_desa = np.random.lognormal(1.7, 0.6, size=35)

# Statistik observasi
diff_observed = penghasilan_kota.mean() - penghasilan_desa.mean()
print(f"Perbedaan mean observasi: {diff_observed:.4f} juta")

# Permutation test
n_permutations = 10_000
combined = np.concatenate([penghasilan_kota, penghasilan_desa])
n_kota = len(penghasilan_kota)

perm_diffs = np.zeros(n_permutations)
for i in range(n_permutations):
    np.random.shuffle(combined)
    perm_kota = combined[:n_kota]
    perm_desa = combined[n_kota:]
    perm_diffs[i] = perm_kota.mean() - perm_desa.mean()

# p-value (two-tailed)
p_value = np.mean(np.abs(perm_diffs) >= np.abs(diff_observed))

plt.figure(figsize=(10, 5))
plt.hist(perm_diffs, bins=50, color='steelblue', edgecolor='white', density=True, alpha=0.7)
plt.axvline(diff_observed, color='red', linestyle='--', linewidth=2,
            label=f'Observed diff = {diff_observed:.3f}')
plt.axvline(-diff_observed, color='red', linestyle='--', linewidth=2)
plt.title(f'Permutation Test: Penghasilan Kota vs Desa\np-value = {p_value:.4f}',
          fontsize=13, fontweight='bold')
plt.xlabel('Perbedaan Mean (Permutasi)')
plt.ylabel('Density')
plt.legend()
plt.tight_layout()
plt.show()

print(f"\nPermutation Test:")
print(f"H0: Tidak ada perbedaan mean penghasilan Kota vs Desa")
print(f"p-value = {p_value:.4f}")
print(f"Keputusan (alpha=0.05): {'Tolak H0' if p_value < 0.05 else 'Gagal tolak H0'}")
```

---

> **Catatan penting:** Bootstrap adalah teknik yang sangat powerful karena tidak memerlukan asumsi distribusi tertentu (non-parametric). Namun, bootstrap tetap memerlukan sampel yang representatif terhadap populasi.
