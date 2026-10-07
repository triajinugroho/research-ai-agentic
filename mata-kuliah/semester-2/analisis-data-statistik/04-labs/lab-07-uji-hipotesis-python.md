# Lab 07: Uji Hipotesis di Python

**Mata Kuliah:** Statistika dan Probabilitas
**Program Studi:** Universitas Al Azhar Indonesia
**Minggu:** 7
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. Merumuskan hipotesis nol (H0) dan hipotesis alternatif (H1)
2. Melaksanakan one-sample t-test, two-sample independent t-test, dan paired t-test menggunakan `scipy.stats`
3. Memeriksa asumsi normalitas sebelum uji hipotesis
4. Menginterpretasikan p-value dan membuat keputusan statistik
5. Menghitung effect size (Cohen's d)
6. Memvisualisasikan distribusi di bawah H0 dengan rejection region

---

## Persiapan

- Google Colab notebook baru
- Nama file: `Lab07_NamaAnda_NIM.ipynb`
- Library: numpy, scipy.stats, matplotlib, seaborn

---

## Langkah-langkah

### Langkah 1: Setup dan Konsep

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

print("=" * 55)
print("KERANGKA UJI HIPOTESIS")
print("=" * 55)
print("""
Langkah-langkah uji hipotesis:
1. Rumuskan H0 dan H1
2. Tentukan tingkat signifikansi (alpha, biasanya 0.05)
3. Periksa asumsi (normalitas, dll)
4. Hitung statistik uji dan p-value
5. Bandingkan p-value dengan alpha
6. Buat keputusan: Tolak H0 atau Gagal Tolak H0
7. Interpretasikan dalam konteks masalah
8. Hitung effect size untuk menilai signifikansi praktis
""")
```

### Langkah 2: Generate Dataset

```python
# =============================================
# LANGKAH 2: Generate Dataset
# =============================================

np.random.seed(42)

# Dataset 1: Nilai ujian satu kelas (untuk one-sample t-test)
# Dosen mengklaim rata-rata nilai kelas adalah 75
nilai_kelas = np.random.normal(loc=78, scale=10, size=30).round(1)

# Dataset 2: Nilai dua kelas berbeda (untuk independent t-test)
# Kelas A menggunakan metode tradisional, Kelas B menggunakan metode aktif
kelas_a = np.random.normal(loc=72, scale=9, size=35).round(1)
kelas_b = np.random.normal(loc=78, scale=10, size=32).round(1)

# Dataset 3: Nilai sebelum dan sesudah pelatihan (untuk paired t-test)
n_peserta = 25
nilai_sebelum = np.random.normal(loc=65, scale=8, size=n_peserta).round(1)
# Pelatihan meningkatkan rata-rata sekitar 5 poin
peningkatan = np.random.normal(loc=5, scale=4, size=n_peserta)
nilai_sesudah = (nilai_sebelum + peningkatan).round(1)

print("Dataset berhasil dibuat:")
print(f"  Dataset 1 (one-sample): n={len(nilai_kelas)}, mean={nilai_kelas.mean():.2f}")
print(f"  Dataset 2a (Kelas A)  : n={len(kelas_a)}, mean={kelas_a.mean():.2f}")
print(f"  Dataset 2b (Kelas B)  : n={len(kelas_b)}, mean={kelas_b.mean():.2f}")
print(f"  Dataset 3 (sebelum)   : n={len(nilai_sebelum)}, mean={nilai_sebelum.mean():.2f}")
print(f"  Dataset 3 (sesudah)   : n={len(nilai_sesudah)}, mean={nilai_sesudah.mean():.2f}")
```

### Langkah 3: Memeriksa Asumsi Normalitas

```python
# =============================================
# LANGKAH 3: Uji Normalitas (Asumsi t-test)
# =============================================

print("=" * 60)
print("UJI NORMALITAS - Shapiro-Wilk Test")
print("H0: Data berdistribusi normal")
print("H1: Data TIDAK berdistribusi normal")
print("=" * 60)

datasets_check = {
    'Nilai Kelas': nilai_kelas,
    'Kelas A': kelas_a,
    'Kelas B': kelas_b,
    'Sebelum Pelatihan': nilai_sebelum,
    'Sesudah Pelatihan': nilai_sesudah,
    'Selisih (sesudah - sebelum)': nilai_sesudah - nilai_sebelum,
}

for nama, data in datasets_check.items():
    stat, p = stats.shapiro(data)
    normal = "Normal" if p > 0.05 else "TIDAK Normal"
    print(f"  {nama:<30}: W={stat:.4f}, p={p:.4f} -> {normal}")

# QQ-Plot
fig, axes = plt.subplots(2, 3, figsize=(15, 9))

for idx, (nama, data) in enumerate(datasets_check.items()):
    ax = axes[idx // 3, idx % 3]
    stats.probplot(data, dist='norm', plot=ax)
    ax.set_title(f'QQ-Plot: {nama}', fontsize=10, fontweight='bold')

plt.suptitle('QQ-Plot untuk Uji Normalitas', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()

print("\nJika p > 0.05: Gagal tolak H0 -> asumsi normalitas terpenuhi")
print("Jika p <= 0.05: Tolak H0 -> asumsi normalitas TIDAK terpenuhi")
print("\nNote: Untuk n >= 30, t-test cukup robust terhadap pelanggaran normalitas (CLT)")
```

### Langkah 4: One-Sample t-Test

```python
# =============================================
# LANGKAH 4: One-Sample t-Test
# =============================================

# Konteks: Dosen mengklaim rata-rata nilai kelas = 75
# Apakah data mendukung klaim ini?

mu_0 = 75  # nilai yang diklaim
alpha = 0.05

print("=" * 60)
print("ONE-SAMPLE t-TEST")
print("=" * 60)

# Langkah 1: Rumuskan hipotesis
print("\nLangkah 1: Hipotesis")
print(f"  H0: mu = {mu_0} (rata-rata nilai kelas = {mu_0})")
print(f"  H1: mu != {mu_0} (rata-rata nilai kelas != {mu_0}) [two-tailed]")
print(f"  Alpha = {alpha}")

# Langkah 2: Statistik deskriptif
x_bar = nilai_kelas.mean()
s = nilai_kelas.std(ddof=1)
n = len(nilai_kelas)
se = s / np.sqrt(n)

print(f"\nLangkah 2: Statistik Deskriptif")
print(f"  n = {n}")
print(f"  x_bar = {x_bar:.4f}")
print(f"  s = {s:.4f}")
print(f"  SE = {se:.4f}")

# Langkah 3: Hitung t-statistic dan p-value
t_stat, p_value = stats.ttest_1samp(nilai_kelas, mu_0)

# Hitung manual
t_manual = (x_bar - mu_0) / se
p_manual = 2 * stats.t.sf(abs(t_manual), df=n-1)  # two-tailed

print(f"\nLangkah 3: Statistik Uji")
print(f"  t-statistic (scipy): {t_stat:.4f}")
print(f"  t-statistic (manual): {t_manual:.4f}")
print(f"  p-value (scipy): {p_value:.4f}")
print(f"  p-value (manual): {p_manual:.4f}")
print(f"  df = {n-1}")

# Langkah 4: Keputusan
print(f"\nLangkah 4: Keputusan")
if p_value < alpha:
    print(f"  p-value ({p_value:.4f}) < alpha ({alpha})")
    print(f"  -> TOLAK H0")
    print(f"  -> Ada bukti yang cukup bahwa rata-rata nilai berbeda dari {mu_0}")
else:
    print(f"  p-value ({p_value:.4f}) >= alpha ({alpha})")
    print(f"  -> GAGAL TOLAK H0")
    print(f"  -> Tidak ada bukti yang cukup bahwa rata-rata nilai berbeda dari {mu_0}")

# Confidence Interval
t_crit = stats.t.ppf(1 - alpha/2, df=n-1)
ci_lower = x_bar - t_crit * se
ci_upper = x_bar + t_crit * se
print(f"\n  95% CI: [{ci_lower:.2f}, {ci_upper:.2f}]")
print(f"  mu_0 = {mu_0} {'termasuk' if ci_lower <= mu_0 <= ci_upper else 'TIDAK termasuk'} dalam CI")
```

### Langkah 5: Visualisasi One-Sample t-Test

```python
# =============================================
# LANGKAH 5: Visualisasi Distribusi H0 + Rejection Region
# =============================================

fig, ax = plt.subplots(figsize=(12, 6))

# Distribusi t di bawah H0
df = n - 1
x_t = np.linspace(-4.5, 4.5, 1000)
y_t = stats.t.pdf(x_t, df=df)

# Plot distribusi
ax.plot(x_t, y_t, 'b-', linewidth=2, label=f't-distribution (df={df})')
ax.fill_between(x_t, y_t, alpha=0.05, color='blue')

# Rejection region (two-tailed)
t_crit_val = stats.t.ppf(1 - alpha/2, df=df)

# Shade rejection regions
x_reject_left = x_t[x_t <= -t_crit_val]
x_reject_right = x_t[x_t >= t_crit_val]
ax.fill_between(x_reject_left, stats.t.pdf(x_reject_left, df=df),
                color='red', alpha=0.4, label=f'Rejection Region (alpha={alpha})')
ax.fill_between(x_reject_right, stats.t.pdf(x_reject_right, df=df),
                color='red', alpha=0.4)

# Garis batas kritis
ax.axvline(-t_crit_val, color='red', linestyle='--', linewidth=1.5,
           label=f't-critical = +/- {t_crit_val:.3f}')
ax.axvline(t_crit_val, color='red', linestyle='--', linewidth=1.5)

# Nilai t-observed
ax.axvline(t_stat, color='green', linestyle='-', linewidth=2.5,
           label=f't-observed = {t_stat:.3f}')
ax.plot(t_stat, stats.t.pdf(t_stat, df=df), 'go', markersize=10, zorder=5)

# Anotasi
region = "TOLAK H0" if abs(t_stat) > t_crit_val else "GAGAL TOLAK H0"
ax.annotate(f'{region}\np = {p_value:.4f}',
            xy=(t_stat, stats.t.pdf(t_stat, df=df)),
            xytext=(t_stat + 0.8, stats.t.pdf(t_stat, df=df) + 0.05),
            fontsize=12, fontweight='bold', color='green',
            arrowprops=dict(arrowstyle='->', color='green'))

ax.set_title(f'One-Sample t-Test: H0: mu = {mu_0}\n'
             f't = {t_stat:.3f}, p = {p_value:.4f}',
             fontsize=14, fontweight='bold')
ax.set_xlabel('t-value', fontsize=12)
ax.set_ylabel('Density', fontsize=12)
ax.legend(fontsize=10, loc='upper left')
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 6: Two-Sample Independent t-Test

```python
# =============================================
# LANGKAH 6: Two-Sample Independent t-Test
# =============================================

# Konteks: Apakah ada perbedaan nilai antara Kelas A (tradisional)
# dan Kelas B (metode aktif)?

alpha = 0.05

print("=" * 60)
print("TWO-SAMPLE INDEPENDENT t-TEST")
print("=" * 60)

# Langkah 1: Hipotesis
print("\nLangkah 1: Hipotesis")
print("  H0: mu_A = mu_B (tidak ada perbedaan rata-rata)")
print("  H1: mu_A != mu_B (ada perbedaan rata-rata) [two-tailed]")
print(f"  Alpha = {alpha}")

# Langkah 2: Statistik deskriptif
print(f"\nLangkah 2: Statistik Deskriptif")
print(f"  Kelas A: n={len(kelas_a)}, mean={kelas_a.mean():.2f}, std={kelas_a.std(ddof=1):.2f}")
print(f"  Kelas B: n={len(kelas_b)}, mean={kelas_b.mean():.2f}, std={kelas_b.std(ddof=1):.2f}")
print(f"  Perbedaan mean: {kelas_b.mean() - kelas_a.mean():.2f}")

# Langkah 3: Periksa asumsi varians (Levene's test)
stat_levene, p_levene = stats.levene(kelas_a, kelas_b)
print(f"\nLangkah 3: Uji Kesamaan Varians (Levene's Test)")
print(f"  H0: varians A = varians B")
print(f"  Levene stat = {stat_levene:.4f}, p = {p_levene:.4f}")
equal_var = p_levene > 0.05
print(f"  -> Varians {'SAMA' if equal_var else 'BERBEDA'} (equal_var={equal_var})")

# Langkah 4: t-test
t_stat_2, p_value_2 = stats.ttest_ind(kelas_a, kelas_b, equal_var=equal_var)

print(f"\nLangkah 4: Statistik Uji ({'Student' if equal_var else 'Welch'} t-test)")
print(f"  t-statistic: {t_stat_2:.4f}")
print(f"  p-value: {p_value_2:.4f}")

# Langkah 5: Keputusan
print(f"\nLangkah 5: Keputusan")
if p_value_2 < alpha:
    print(f"  p-value ({p_value_2:.4f}) < alpha ({alpha})")
    print(f"  -> TOLAK H0: Ada perbedaan signifikan antara Kelas A dan Kelas B")
else:
    print(f"  p-value ({p_value_2:.4f}) >= alpha ({alpha})")
    print(f"  -> GAGAL TOLAK H0: Tidak ada perbedaan signifikan")

# Visualisasi
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Boxplot perbandingan
import pandas as pd
df_compare = pd.DataFrame({
    'Nilai': np.concatenate([kelas_a, kelas_b]),
    'Kelas': ['Kelas A (Tradisional)'] * len(kelas_a) + ['Kelas B (Metode Aktif)'] * len(kelas_b)
})

sns.boxplot(data=df_compare, x='Kelas', y='Nilai', palette='Set2', ax=axes[0])
axes[0].set_title('Perbandingan Nilai Kelas A vs B', fontsize=12, fontweight='bold')

# Histogram overlay
axes[1].hist(kelas_a, bins=15, alpha=0.5, color='#e74c3c', edgecolor='white', density=True, label=f'Kelas A (mean={kelas_a.mean():.1f})')
axes[1].hist(kelas_b, bins=15, alpha=0.5, color='#3498db', edgecolor='white', density=True, label=f'Kelas B (mean={kelas_b.mean():.1f})')
axes[1].axvline(kelas_a.mean(), color='#e74c3c', linestyle='--', linewidth=2)
axes[1].axvline(kelas_b.mean(), color='#3498db', linestyle='--', linewidth=2)
axes[1].set_title(f'Distribusi Nilai (p = {p_value_2:.4f})', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Nilai')
axes[1].set_ylabel('Density')
axes[1].legend()

plt.tight_layout()
plt.show()
```

### Langkah 7: Paired t-Test

```python
# =============================================
# LANGKAH 7: Paired t-Test
# =============================================

# Konteks: Apakah pelatihan meningkatkan nilai secara signifikan?

alpha = 0.05
selisih = nilai_sesudah - nilai_sebelum

print("=" * 60)
print("PAIRED t-TEST (Dependent Samples)")
print("=" * 60)

# Langkah 1: Hipotesis
print("\nLangkah 1: Hipotesis")
print("  H0: mu_d = 0 (tidak ada peningkatan setelah pelatihan)")
print("  H1: mu_d > 0 (ada peningkatan setelah pelatihan) [one-tailed]")
print(f"  Alpha = {alpha}")

# Langkah 2: Statistik deskriptif
print(f"\nLangkah 2: Statistik Deskriptif")
print(f"  Sebelum : mean={nilai_sebelum.mean():.2f}, std={nilai_sebelum.std(ddof=1):.2f}")
print(f"  Sesudah : mean={nilai_sesudah.mean():.2f}, std={nilai_sesudah.std(ddof=1):.2f}")
print(f"  Selisih : mean={selisih.mean():.2f}, std={selisih.std(ddof=1):.2f}")
print(f"  n = {len(selisih)}")

# Langkah 3: Paired t-test (scipy default = two-tailed)
t_stat_paired, p_value_paired_two = stats.ttest_rel(nilai_sesudah, nilai_sebelum)

# Untuk one-tailed (H1: mu_d > 0):
# Jika t > 0, p_one_tailed = p_two_tailed / 2
p_value_paired = p_value_paired_two / 2 if t_stat_paired > 0 else 1 - p_value_paired_two / 2

print(f"\nLangkah 3: Statistik Uji")
print(f"  t-statistic: {t_stat_paired:.4f}")
print(f"  p-value (two-tailed): {p_value_paired_two:.4f}")
print(f"  p-value (one-tailed): {p_value_paired:.4f}")
print(f"  df = {len(selisih)-1}")

# Langkah 4: Keputusan
print(f"\nLangkah 4: Keputusan (one-tailed, alpha={alpha})")
if p_value_paired < alpha:
    print(f"  p-value ({p_value_paired:.4f}) < alpha ({alpha})")
    print(f"  -> TOLAK H0: Pelatihan secara signifikan meningkatkan nilai")
else:
    print(f"  p-value ({p_value_paired:.4f}) >= alpha ({alpha})")
    print(f"  -> GAGAL TOLAK H0: Tidak cukup bukti pelatihan meningkatkan nilai")

# Visualisasi
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Before vs After (connected dots)
for i in range(len(nilai_sebelum)):
    color = 'green' if selisih[i] > 0 else 'red'
    axes[0].plot([0, 1], [nilai_sebelum[i], nilai_sesudah[i]], '-o',
                 color=color, alpha=0.3, markersize=4)
axes[0].set_xticks([0, 1])
axes[0].set_xticklabels(['Sebelum', 'Sesudah'])
axes[0].set_title('Perubahan Nilai per Peserta\n(Hijau=naik, Merah=turun)',
                   fontsize=11, fontweight='bold')
axes[0].set_ylabel('Nilai')

# Distribusi selisih
axes[1].hist(selisih, bins=12, color='steelblue', edgecolor='white', alpha=0.7)
axes[1].axvline(0, color='red', linestyle='--', linewidth=2, label='d = 0 (H0)')
axes[1].axvline(selisih.mean(), color='green', linestyle='--', linewidth=2,
                label=f'Mean d = {selisih.mean():.2f}')
axes[1].set_title('Distribusi Selisih (Sesudah - Sebelum)', fontsize=11, fontweight='bold')
axes[1].set_xlabel('Selisih Nilai')
axes[1].set_ylabel('Frekuensi')
axes[1].legend()

# Boxplot perbandingan
data_paired = pd.DataFrame({
    'Nilai': np.concatenate([nilai_sebelum, nilai_sesudah]),
    'Waktu': ['Sebelum'] * len(nilai_sebelum) + ['Sesudah'] * len(nilai_sesudah)
})
sns.boxplot(data=data_paired, x='Waktu', y='Nilai',
            order=['Sebelum', 'Sesudah'], palette='Set2', ax=axes[2])
axes[2].set_title(f'Boxplot: Sebelum vs Sesudah\n(p = {p_value_paired:.4f})',
                   fontsize=11, fontweight='bold')

plt.tight_layout()
plt.show()
```

### Langkah 8: Effect Size (Cohen's d)

```python
# =============================================
# LANGKAH 8: Effect Size - Cohen's d
# =============================================

def cohens_d_one_sample(data, mu_0):
    """Cohen's d untuk one-sample t-test."""
    return (data.mean() - mu_0) / data.std(ddof=1)

def cohens_d_independent(group1, group2):
    """Cohen's d untuk independent t-test (pooled std)."""
    n1, n2 = len(group1), len(group2)
    s1, s2 = group1.std(ddof=1), group2.std(ddof=1)
    # Pooled standard deviation
    s_pooled = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))
    return (group1.mean() - group2.mean()) / s_pooled

def cohens_d_paired(before, after):
    """Cohen's d untuk paired t-test."""
    diff = after - before
    return diff.mean() / diff.std(ddof=1)

def interpret_cohens_d(d):
    """Interpretasi Cohen's d."""
    d_abs = abs(d)
    if d_abs < 0.2:
        return "Negligible (sangat kecil)"
    elif d_abs < 0.5:
        return "Small (kecil)"
    elif d_abs < 0.8:
        return "Medium (sedang)"
    else:
        return "Large (besar)"

# Hitung effect size untuk ketiga tes
d_one = cohens_d_one_sample(nilai_kelas, mu_0=75)
d_ind = cohens_d_independent(kelas_a, kelas_b)
d_paired = cohens_d_paired(nilai_sebelum, nilai_sesudah)

print("=" * 60)
print("EFFECT SIZE - COHEN'S d")
print("=" * 60)
print(f"""
Interpretasi Cohen's d:
  |d| < 0.2  : Negligible (sangat kecil)
  0.2 <= |d| < 0.5 : Small (kecil)
  0.5 <= |d| < 0.8 : Medium (sedang)
  |d| >= 0.8 : Large (besar)

Hasil:
  1. One-sample t-test:
     d = {d_one:.4f} -> {interpret_cohens_d(d_one)}
     p = {p_value:.4f}

  2. Independent t-test (Kelas A vs B):
     d = {d_ind:.4f} -> {interpret_cohens_d(d_ind)}
     p = {p_value_2:.4f}

  3. Paired t-test (sebelum vs sesudah):
     d = {d_paired:.4f} -> {interpret_cohens_d(d_paired)}
     p = {p_value_paired:.4f}
""")

print("PENTING: p-value kecil (signifikan secara statistik) TIDAK selalu")
print("berarti efeknya besar secara praktis. Selalu laporkan effect size!")
```

### Langkah 9: Visualisasi Lengkap dengan Rejection Region

```python
# =============================================
# LANGKAH 9: Visualisasi Komprehensif
# =============================================

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

tests = [
    ("One-Sample t-Test", t_stat, p_value, n-1, "two"),
    ("Independent t-Test", t_stat_2, p_value_2, len(kelas_a)+len(kelas_b)-2, "two"),
    ("Paired t-Test", t_stat_paired, p_value_paired, len(selisih)-1, "one"),
]

for idx, (title, t_val, p_val, df_val, tail) in enumerate(tests):
    ax = axes[idx]

    # Distribusi t di bawah H0
    x_t = np.linspace(-5, 5, 1000)
    y_t = stats.t.pdf(x_t, df=df_val)

    ax.plot(x_t, y_t, 'b-', linewidth=2)
    ax.fill_between(x_t, y_t, alpha=0.05, color='blue')

    # Rejection region
    t_crit_val = stats.t.ppf(1 - alpha/2, df=df_val)

    if tail == "two":
        # Two-tailed rejection region
        x_rej_l = x_t[x_t <= -t_crit_val]
        x_rej_r = x_t[x_t >= t_crit_val]
        ax.fill_between(x_rej_l, stats.t.pdf(x_rej_l, df=df_val),
                        color='red', alpha=0.4, label=f'Rejection Region')
        ax.fill_between(x_rej_r, stats.t.pdf(x_rej_r, df=df_val),
                        color='red', alpha=0.4)
        ax.axvline(-t_crit_val, color='red', linestyle='--', linewidth=1)
        ax.axvline(t_crit_val, color='red', linestyle='--', linewidth=1)
    else:
        # One-tailed (right) rejection region
        t_crit_one = stats.t.ppf(1 - alpha, df=df_val)
        x_rej = x_t[x_t >= t_crit_one]
        ax.fill_between(x_rej, stats.t.pdf(x_rej, df=df_val),
                        color='red', alpha=0.4, label=f'Rejection Region')
        ax.axvline(t_crit_one, color='red', linestyle='--', linewidth=1)

    # Observed t-value
    ax.axvline(t_val, color='green', linestyle='-', linewidth=2.5,
               label=f't = {t_val:.3f}')

    # Decision
    if tail == "two":
        reject = abs(t_val) > t_crit_val
    else:
        reject = t_val > t_crit_one

    decision = "TOLAK H0" if reject else "GAGAL TOLAK H0"
    ax.set_title(f'{title}\nt={t_val:.3f}, p={p_val:.4f}\n{decision}',
                 fontsize=11, fontweight='bold',
                 color='red' if reject else 'gray')
    ax.set_xlabel('t-value')
    ax.set_ylabel('Density')
    ax.legend(fontsize=8, loc='upper left')
    ax.grid(alpha=0.3)

plt.suptitle('Visualisasi Keputusan Uji Hipotesis', fontsize=14, fontweight='bold', y=1.04)
plt.tight_layout()
plt.show()
```

### Langkah 10: Ringkasan dan Tabel Hasil

```python
# =============================================
# LANGKAH 10: Ringkasan Hasil
# =============================================

print("=" * 75)
print("RINGKASAN SELURUH UJI HIPOTESIS")
print("=" * 75)

# Tabel ringkasan
print(f"\n{'Uji':<25} {'t-stat':>8} {'p-value':>9} {'alpha':>7} {'Keputusan':<18} {'Cohen d':>8} {'Efek':<12}")
print("-" * 95)

results = [
    ("One-Sample (mu=75)", t_stat, p_value, alpha,
     "Tolak H0" if p_value < alpha else "Gagal Tolak H0",
     d_one, interpret_cohens_d(d_one)),
    ("Independent (A vs B)", t_stat_2, p_value_2, alpha,
     "Tolak H0" if p_value_2 < alpha else "Gagal Tolak H0",
     d_ind, interpret_cohens_d(d_ind)),
    ("Paired (pre vs post)", t_stat_paired, p_value_paired, alpha,
     "Tolak H0" if p_value_paired < alpha else "Gagal Tolak H0",
     d_paired, interpret_cohens_d(d_paired)),
]

for name, t, p, a, decision, d, effect in results:
    print(f"{name:<25} {t:>8.4f} {p:>9.4f} {a:>7.2f} {decision:<18} {d:>8.4f} {effect:<12}")

print(f"""
INTERPRETASI:
1. One-Sample t-Test:
   Rata-rata nilai kelas ({nilai_kelas.mean():.2f}) diuji terhadap klaim mu=75.
   Effect size {interpret_cohens_d(d_one).lower()}.

2. Independent t-Test:
   Perbandingan Kelas A (tradisional, mean={kelas_a.mean():.2f}) vs
   Kelas B (metode aktif, mean={kelas_b.mean():.2f}).
   Effect size {interpret_cohens_d(d_ind).lower()}.

3. Paired t-Test:
   Pelatihan meningkatkan nilai dari mean={nilai_sebelum.mean():.2f}
   menjadi mean={nilai_sesudah.mean():.2f} (selisih={selisih.mean():.2f}).
   Effect size {interpret_cohens_d(d_paired).lower()}.
""")
```

---

## Tugas yang Harus Dikumpulkan

Kumpulkan notebook (.ipynb) yang berisi:

1. **Semua kode** dari Langkah 1-10 yang sudah dijalankan (tanpa error)
2. **Analisis sendiri** menggunakan dataset baru:
   - Buat skenario riset sendiri (misalnya: pengaruh jam belajar terhadap nilai, perbedaan IPK antar jurusan, dll)
   - Lakukan salah satu dari tiga jenis t-test
   - Ikuti langkah-langkah lengkap: hipotesis, cek asumsi, uji, interpretasi, effect size
3. **Refleksi tertulis** (text cell, 2-3 paragraf):
   - Apa perbedaan antara signifikansi statistik dan signifikansi praktis?
   - Mengapa kita perlu melaporkan effect size selain p-value?

---

## Rubrik Singkat

| Kriteria | Bobot | Keterangan |
|----------|-------|------------|
| Kelengkapan kode (Langkah 1-10) | 25% | Semua cell berjalan tanpa error |
| Analisis independen | 30% | Skenario jelas, prosedur lengkap, interpretasi tepat |
| Effect size & visualisasi | 20% | Cohen's d dihitung, visualisasi rejection region |
| Refleksi tertulis | 15% | Pemahaman signifikansi statistik vs praktis |
| Kerapian notebook | 10% | Terstruktur rapi dengan text cell |

---

## Challenge / Bonus

```python
# =============================================
# CHALLENGE: Power Analysis dan Simulasi Type I/II Error
# =============================================

# Berapa probabilitas kita mendeteksi perbedaan yang sebenarnya ada?
# (Statistical Power = 1 - beta)

def simulate_power(n_per_group, true_diff, sigma, alpha=0.05, n_simulations=5000):
    """Simulasi statistical power."""
    rejections = 0
    for _ in range(n_simulations):
        # Generate dua grup dengan perbedaan true_diff
        group1 = np.random.normal(0, sigma, size=n_per_group)
        group2 = np.random.normal(true_diff, sigma, size=n_per_group)

        # t-test
        _, p = stats.ttest_ind(group1, group2)
        if p < alpha:
            rejections += 1

    return rejections / n_simulations

# Power untuk berbagai ukuran sampel
sample_sizes_power = [10, 20, 30, 50, 75, 100, 150, 200]
true_diff = 5  # perbedaan sebenarnya
sigma = 10

powers = [simulate_power(n, true_diff, sigma) for n in sample_sizes_power]

# Power untuk berbagai effect sizes
effect_sizes_d = [0.2, 0.5, 0.8]
n_fixed = 30

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Power vs Sample Size
axes[0].plot(sample_sizes_power, powers, 'o-', color='steelblue', linewidth=2, markersize=8)
axes[0].axhline(0.80, color='red', linestyle='--', alpha=0.5, label='Target Power = 0.80')
axes[0].set_xlabel('Ukuran Sampel per Grup (n)', fontsize=12)
axes[0].set_ylabel('Statistical Power', fontsize=12)
axes[0].set_title(f'Power vs Ukuran Sampel\n(True diff={true_diff}, sigma={sigma}, d={true_diff/sigma:.1f})',
                   fontsize=12, fontweight='bold')
axes[0].legend()
axes[0].grid(alpha=0.3)
axes[0].set_ylim(0, 1.05)

# Plot 2: Power vs Effect Size (fixed n)
for d_val in effect_sizes_d:
    true_diff_i = d_val * sigma
    pow_list = [simulate_power(n, true_diff_i, sigma) for n in sample_sizes_power]
    axes[1].plot(sample_sizes_power, pow_list, 'o-', linewidth=2, markersize=6,
                 label=f'd = {d_val}')

axes[1].axhline(0.80, color='red', linestyle='--', alpha=0.5, label='Target Power = 0.80')
axes[1].set_xlabel('Ukuran Sampel per Grup (n)', fontsize=12)
axes[1].set_ylabel('Statistical Power', fontsize=12)
axes[1].set_title('Power vs Sample Size untuk Berbagai Effect Sizes',
                   fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(alpha=0.3)
axes[1].set_ylim(0, 1.05)

plt.tight_layout()
plt.show()

print("Insight:")
print("- Semakin besar n, semakin tinggi power")
print("- Semakin besar effect size (d), semakin mudah mendeteksi perbedaan")
print("- Target power umumnya >= 0.80 (80%)")
print("- Dengan d=0.5 dan sigma=10, dibutuhkan n ~65 per grup untuk power 80%")
```

---

> **Peringatan:** p-value BUKAN probabilitas bahwa H0 benar. p-value adalah probabilitas mendapatkan data seextrem (atau lebih ekstrem) dari yang diamati, JIKA H0 benar. Selalu interpretasikan p-value dengan benar dan sertakan effect size dalam laporan Anda.
