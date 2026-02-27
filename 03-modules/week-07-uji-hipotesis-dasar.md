# Minggu 7: Uji Hipotesis

## Mata Kuliah: Analisis Data Statistik
### Prodi Informatika — Universitas Al Azhar Indonesia — Semester Genap 2025/2026

---

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Minggu** | 7 |
| **Topik** | Uji Hipotesis (Hypothesis Testing) |
| **CPMK** | CPMK-4: Menganalisis data menggunakan teknik inferensi statistik meliputi estimasi parameter dan pengujian hipotesis |
| **Sub-CPMK** | 7.1: Melaksanakan uji hipotesis (z-test, t-test) dan menginterpretasi p-value |
| | 7.2: Menjelaskan error Type I/II dan effect size |
| **Bloom's Taxonomy** | C4 (Analyze) |
| **Durasi** | 100 menit (50 menit teori + 50 menit praktikum) |
| **Prasyarat** | Minggu 6 — Sampling dan Estimasi (terutama: CI, SE, CLT) |
| **Tools** | Python, Google Colab, numpy, scipy.stats, matplotlib |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Memformulasikan** hipotesis null (H0) dan hipotesis alternatif (H1) dengan benar
2. **Memilih** uji statistik yang tepat sesuai kondisi data (z-test vs t-test, one-sample vs two-sample)
3. **Melaksanakan** uji hipotesis menggunakan `scipy.stats` di Python
4. **Menginterpretasi** p-value dengan benar dan menghindari miskonsepsi umum
5. **Menjelaskan** Type I Error, Type II Error, dan Power
6. **Menghitung** dan menginterpretasi effect size (Cohen's d)

---

## Peta Konsep Minggu Ini

```
Uji Hipotesis
├── Kerangka Dasar
│   ├── H₀ (null hypothesis) → "tidak ada efek/perbedaan"
│   ├── H₁ (alternative hypothesis) → "ada efek/perbedaan"
│   └── α (significance level) → threshold keputusan
├── Langkah-langkah
│   └── Formulate → Choose test → Compute → Decide → Interpret
├── Jenis Uji
│   ├── z-test → σ populasi diketahui (jarang)
│   ├── One-sample t-test → σ tidak diketahui
│   ├── Independent two-sample t-test → 2 kelompok berbeda
│   └── Paired t-test → 2 pengukuran dari kelompok sama
├── Interpretasi
│   ├── p-value → kekuatan bukti terhadap H₀
│   └── 3 miskonsepsi yang harus dihindari
├── Error dan Power
│   ├── Type I Error (α) → reject H₀ padahal H₀ benar
│   ├── Type II Error (β) → fail to reject H₀ padahal H₀ salah
│   └── Power (1-β) → kemampuan mendeteksi efek
└── Effect Size
    └── Cohen's d → ukuran perbedaan yang bermakna
```

---

## Bagian 1: Kerangka Uji Hipotesis

### 1.1 Analogi Pengadilan

Uji hipotesis mirip dengan sistem peradilan:

| Pengadilan | Uji Hipotesis |
|------------|---------------|
| Terdakwa dianggap **tidak bersalah** sampai terbukti | H0 dianggap **benar** sampai ada bukti cukup |
| Jaksa harus memberikan **bukti kuat** | Data harus memberikan **bukti kuat** (p-value kecil) |
| "Beyond reasonable doubt" | Significance level (alpha) |
| Verdict: **guilty** atau **not guilty** (bukan "innocent"!) | Keputusan: **reject H0** atau **fail to reject H0** (bukan "terima H0"!) |

### 1.2 Hipotesis Null (H0) dan Alternatif (H1)

**H0 (Null Hypothesis):**
- Status quo, tidak ada efek, tidak ada perbedaan
- Selalu mengandung tanda "=" (=, <=, >=)
- Yang ingin kita **tolak** (jika ada cukup bukti)

**H1 (Alternative Hypothesis):**
- Ada efek, ada perbedaan
- Yang ingin kita **buktikan**
- Menentukan apakah uji **one-tailed** atau **two-tailed**

**Jenis uji berdasarkan H1:**

| Jenis | H0 | H1 | Kapan |
|-------|----|----|-------|
| Two-tailed | mu = mu_0 | mu != mu_0 | Tidak tahu arah perbedaan |
| Left-tailed | mu >= mu_0 | mu < mu_0 | Menduga lebih kecil |
| Right-tailed | mu <= mu_0 | mu > mu_0 | Menduga lebih besar |

### 1.3 Significance Level (alpha)

**alpha** adalah probabilitas **maksimum** yang kita toleransi untuk membuat kesalahan **reject H0 padahal H0 benar** (Type I Error).

| alpha | Artinya | Kapan digunakan |
|-------|---------|-----------------|
| 0.10 | 10% toleransi | Studi eksplorasi, awal |
| **0.05** | **5% toleransi** | **Standard paling umum** |
| 0.01 | 1% toleransi | Studi kritis (medis, keamanan) |

### 1.4 Lima Langkah Uji Hipotesis

```
Langkah 1: FORMULATE — Rumuskan H₀ dan H₁
           ↓
Langkah 2: CHOOSE — Pilih uji yang tepat + tentukan α
           ↓
Langkah 3: COMPUTE — Hitung test statistic dan p-value
           ↓
Langkah 4: DECIDE — Bandingkan p-value dengan α
           • Jika p-value < α → Reject H₀
           • Jika p-value >= α → Fail to reject H₀
           ↓
Langkah 5: INTERPRET — Apa artinya dalam konteks masalah?
```

---

## Bagian 2: z-Test

### 2.1 Kapan Digunakan?

z-test digunakan ketika:
- Standard deviation **populasi (sigma) diketahui** (jarang terjadi di dunia nyata)
- Ukuran sampel besar (n >= 30) dan kita menggunakan s sebagai estimasi sigma

**Formula:**

```
z = (x̄ - μ₀) / (σ / √n)

di mana:
  x̄ = mean sampel
  μ₀ = mean hipotesis (dari H₀)
  σ = standard deviation populasi
  n = ukuran sampel
```

### 2.2 Contoh z-Test dengan Python

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# === z-TEST ===
# Konteks: Standar nasional IPK lulusan Informatika = 3.20
# Dosen menduga IPK lulusan UAI berbeda dari standar nasional
# σ populasi diketahui = 0.35 (dari data historis)

# Data: IPK 40 lulusan UAI
np.random.seed(42)
ipk_sampel = np.random.normal(loc=3.30, scale=0.35, size=40)

# Langkah 1: Formulasi hipotesis
mu_0 = 3.20  # mean hipotesis
sigma = 0.35  # sigma populasi (diketahui)
alpha = 0.05

print("=" * 50)
print("z-TEST: IPK Lulusan UAI vs Standar Nasional")
print("=" * 50)
print(f"\nLangkah 1: Formulasi Hipotesis")
print(f"  H₀: μ = {mu_0} (IPK lulusan UAI = standar nasional)")
print(f"  H₁: μ ≠ {mu_0} (IPK lulusan UAI ≠ standar nasional)")
print(f"  α = {alpha} (two-tailed test)")

# Langkah 2: Pilih uji → z-test (σ diketahui)
print(f"\nLangkah 2: Pilih Uji")
print(f"  z-test (σ populasi diketahui = {sigma})")

# Langkah 3: Hitung
n = len(ipk_sampel)
x_bar = ipk_sampel.mean()
se = sigma / np.sqrt(n)
z_stat = (x_bar - mu_0) / se
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))  # two-tailed

print(f"\nLangkah 3: Hitung")
print(f"  n = {n}")
print(f"  x̄ = {x_bar:.4f}")
print(f"  SE = σ/√n = {sigma}/{np.sqrt(n):.2f} = {se:.4f}")
print(f"  z = (x̄ - μ₀) / SE = ({x_bar:.4f} - {mu_0}) / {se:.4f} = {z_stat:.4f}")
print(f"  p-value = {p_value:.4f}")

# Langkah 4: Keputusan
print(f"\nLangkah 4: Keputusan")
if p_value < alpha:
    print(f"  p-value ({p_value:.4f}) < α ({alpha}) → REJECT H₀")
else:
    print(f"  p-value ({p_value:.4f}) >= α ({alpha}) → FAIL TO REJECT H₀")

# Langkah 5: Interpretasi
print(f"\nLangkah 5: Interpretasi")
if p_value < alpha:
    print(f"  Pada tingkat signifikansi {alpha*100:.0f}%, terdapat cukup bukti")
    print(f"  bahwa rata-rata IPK lulusan UAI berbeda dari standar nasional.")
else:
    print(f"  Pada tingkat signifikansi {alpha*100:.0f}%, tidak cukup bukti")
    print(f"  untuk menyimpulkan bahwa IPK lulusan UAI berbeda dari standar nasional.")
```

---

## Bagian 3: One-Sample t-Test

### 3.1 Kapan Digunakan?

Situasi yang **jauh lebih umum** daripada z-test: ketika sigma **tidak diketahui** dan kita menggunakan s (standard deviation sampel) sebagai estimasi.

**Perbedaan utama dari z-test:**
- Menggunakan **t-distribution** (bukan Normal)
- t-distribution lebih "gemuk" (heavier tails) — lebih konservatif
- Semakin besar n, t-distribution semakin mendekati Normal

**Formula:**

```
t = (x̄ - μ₀) / (s / √n)

Degrees of freedom (df) = n - 1

di mana:
  s = standard deviation SAMPEL (bukan populasi)
```

### 3.2 Contoh One-Sample t-Test

```python
# === ONE-SAMPLE t-TEST ===
# Konteks: Standar waktu respons IT helpdesk UAI = 30 menit
# Apakah waktu respons aktual berbeda dari standar?

np.random.seed(42)
waktu_respons = np.random.normal(loc=35, scale=8, size=25)  # dalam menit

mu_0 = 30  # standar yang diharapkan
alpha = 0.05

print("=" * 50)
print("ONE-SAMPLE t-TEST: Waktu Respons IT Helpdesk")
print("=" * 50)

# Langkah 1
print(f"\nH₀: μ = {mu_0} menit (waktu respons sesuai standar)")
print(f"H₁: μ ≠ {mu_0} menit (waktu respons berbeda dari standar)")

# Langkah 2-3: Gunakan scipy.stats
t_stat, p_value = stats.ttest_1samp(waktu_respons, popmean=mu_0)

n = len(waktu_respons)
x_bar = waktu_respons.mean()
s = waktu_respons.std(ddof=1)
se = s / np.sqrt(n)

print(f"\nStatistik Sampel:")
print(f"  n = {n}")
print(f"  x̄ = {x_bar:.2f} menit")
print(f"  s = {s:.2f} menit")
print(f"  SE = {se:.2f} menit")
print(f"\nHasil Uji:")
print(f"  t-statistic = {t_stat:.4f}")
print(f"  p-value = {p_value:.4f}")
print(f"  df = {n - 1}")

# Langkah 4-5
print(f"\nKeputusan:")
if p_value < alpha:
    print(f"  p-value ({p_value:.4f}) < α ({alpha}) → REJECT H₀")
    print(f"  Kesimpulan: Waktu respons IT helpdesk BERBEDA dari standar {mu_0} menit.")
    print(f"  Rata-rata waktu respons ({x_bar:.2f} menit) lebih tinggi dari standar.")
else:
    print(f"  p-value ({p_value:.4f}) >= α ({alpha}) → FAIL TO REJECT H₀")
    print(f"  Kesimpulan: Tidak cukup bukti bahwa waktu respons berbeda dari standar.")
```

---

## Bagian 4: Two-Sample t-Test

### 4.1 Independent (Unpaired) Two-Sample t-Test

**Kapan digunakan:** Membandingkan mean dari **dua kelompok berbeda** yang tidak saling terkait.

**Asumsi:**
1. Kedua sampel independen
2. Data mendekati Normal (atau n cukup besar, berkat CLT)
3. Variance kedua kelompok kurang lebih sama (jika tidak, gunakan Welch's t-test)

```python
# === INDEPENDENT TWO-SAMPLE t-TEST ===
# Konteks: Apakah ada perbedaan nilai ujian Statistik antara
# Kelas A (metode tradisional) dan Kelas B (metode active learning)?

np.random.seed(42)
kelas_a = np.random.normal(loc=70, scale=12, size=30)  # tradisional
kelas_b = np.random.normal(loc=76, scale=10, size=35)  # active learning

print("=" * 50)
print("INDEPENDENT TWO-SAMPLE t-TEST")
print("Nilai Ujian: Kelas A vs Kelas B")
print("=" * 50)

print(f"\nH₀: μ_A = μ_B (tidak ada perbedaan nilai antar kelas)")
print(f"H₁: μ_A ≠ μ_B (ada perbedaan nilai antar kelas)")

# Statistik deskriptif
print(f"\nKelas A (tradisional):  n={len(kelas_a)}, mean={kelas_a.mean():.2f}, std={kelas_a.std(ddof=1):.2f}")
print(f"Kelas B (active learn): n={len(kelas_b)}, mean={kelas_b.mean():.2f}, std={kelas_b.std(ddof=1):.2f}")

# Uji hipotesis
# equal_var=True → Student's t-test (asumsi variance sama)
# equal_var=False → Welch's t-test (tidak asumsi variance sama, lebih aman)
t_stat, p_value = stats.ttest_ind(kelas_a, kelas_b, equal_var=False)

print(f"\nHasil (Welch's t-test):")
print(f"  t-statistic = {t_stat:.4f}")
print(f"  p-value = {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"\n  p-value < {alpha} → REJECT H₀")
    print(f"  Ada perbedaan signifikan antara nilai Kelas A dan Kelas B.")
else:
    print(f"\n  p-value >= {alpha} → FAIL TO REJECT H₀")
    print(f"  Tidak cukup bukti adanya perbedaan signifikan.")
```

### 4.2 Paired t-Test

**Kapan digunakan:** Membandingkan **dua pengukuran** dari **subjek yang sama** (before-after, pre-post, dsb.)

**Contoh:**
- Nilai mahasiswa **sebelum** dan **sesudah** workshop
- Berat badan **sebelum** dan **sesudah** program diet
- Skor kepuasan **sebelum** dan **sesudah** renovasi lab

```python
# === PAIRED t-TEST ===
# Konteks: Apakah workshop Python meningkatkan skor coding test?
# 20 mahasiswa diuji SEBELUM dan SESUDAH workshop

np.random.seed(42)
n_students = 20
skor_sebelum = np.random.normal(loc=55, scale=12, size=n_students)
# Setelah workshop: peningkatan rata-rata 8 poin + noise
peningkatan = np.random.normal(loc=8, scale=5, size=n_students)
skor_sesudah = skor_sebelum + peningkatan

print("=" * 50)
print("PAIRED t-TEST")
print("Skor Coding Test: Sebelum vs Sesudah Workshop")
print("=" * 50)

print(f"\nH₀: μ_d = 0 (tidak ada perubahan skor setelah workshop)")
print(f"H₁: μ_d > 0 (skor meningkat setelah workshop)")
print(f"(di mana d = sesudah - sebelum)")

# Statistik deskriptif
perbedaan = skor_sesudah - skor_sebelum
print(f"\nSebelum:   mean = {skor_sebelum.mean():.2f}, std = {skor_sebelum.std(ddof=1):.2f}")
print(f"Sesudah:   mean = {skor_sesudah.mean():.2f}, std = {skor_sesudah.std(ddof=1):.2f}")
print(f"Perbedaan: mean = {perbedaan.mean():.2f}, std = {perbedaan.std(ddof=1):.2f}")

# Uji hipotesis
t_stat, p_value_two = stats.ttest_rel(skor_sesudah, skor_sebelum)
# Karena H₁ adalah one-tailed (μ_d > 0), bagi p-value dengan 2
p_value = p_value_two / 2

print(f"\nHasil (Paired t-test, one-tailed):")
print(f"  t-statistic = {t_stat:.4f}")
print(f"  p-value (one-tailed) = {p_value:.4f}")

alpha = 0.05
if p_value < alpha and t_stat > 0:
    print(f"\n  p-value < {alpha} dan t > 0 → REJECT H₀")
    print(f"  Workshop Python SECARA SIGNIFIKAN meningkatkan skor coding test.")
    print(f"  Peningkatan rata-rata: {perbedaan.mean():.2f} poin.")
else:
    print(f"\n  FAIL TO REJECT H₀")
    print(f"  Tidak cukup bukti bahwa workshop meningkatkan skor.")

# Visualisasi
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Before vs After
ax = axes[0]
for i in range(n_students):
    color = 'green' if skor_sesudah[i] > skor_sebelum[i] else 'red'
    ax.plot([0, 1], [skor_sebelum[i], skor_sesudah[i]],
            'o-', color=color, alpha=0.5)
ax.set_xticks([0, 1])
ax.set_xticklabels(['Sebelum', 'Sesudah'])
ax.set_ylabel('Skor Coding Test')
ax.set_title('Skor Individual: Sebelum vs Sesudah Workshop')

# Plot 2: Distribusi perbedaan
ax = axes[1]
ax.hist(perbedaan, bins=10, color='steelblue', alpha=0.7, edgecolor='black')
ax.axvline(0, color='red', linestyle='--', linewidth=2, label='H₀: μ_d = 0')
ax.axvline(perbedaan.mean(), color='green', linestyle='-', linewidth=2,
           label=f'Mean perbedaan = {perbedaan.mean():.2f}')
ax.set_xlabel('Perbedaan Skor (Sesudah - Sebelum)')
ax.set_ylabel('Frekuensi')
ax.set_title('Distribusi Perbedaan Skor')
ax.legend()

plt.suptitle('Paired t-Test: Efektivitas Workshop Python',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()
```

### 4.3 Kapan Pakai yang Mana?

```
Apakah membandingkan 1 sampel vs nilai referensi?
├── Ya → ONE-SAMPLE t-test
└── Tidak → Apakah membandingkan 2 kelompok?
    ├── Ya → Apakah subjek SAMA (before-after)?
    │   ├── Ya → PAIRED t-test
    │   └── Tidak → INDEPENDENT two-sample t-test
    └── Tidak → (akan dipelajari: ANOVA, Minggu 11)
```

---

## Bagian 5: p-Value — Interpretasi yang BENAR

### 5.1 Definisi p-value

> **p-value** adalah probabilitas mendapatkan hasil **seektrem atau lebih ekstrem** dari yang kita amati, **JIKA H0 benar**.

Dengan kata lain: "Seberapa 'aneh' data kita jika H0 memang benar?"
- p-value kecil → data kita sangat "aneh" jika H0 benar → bukti kuat melawan H0
- p-value besar → data kita "wajar" jika H0 benar → tidak cukup bukti

### 5.2 Tiga Miskonsepsi yang HARUS Dihindari

| No | Miskonsepsi (SALAH) | Koreksi (BENAR) |
|----|---------------------|-----------------|
| 1 | "p-value = probabilitas H0 benar" | p-value BUKAN probabilitas H0 benar. Untuk itu kita butuh Bayesian statistics. p-value = probabilitas **data** (given H0 benar). |
| 2 | "p > 0.05 berarti H0 terbukti benar" | Fail to reject H0 BUKAN berarti H0 terbukti. Artinya: tidak cukup bukti untuk menolak H0. Seperti pengadilan: "not guilty" bukan berarti "innocent". |
| 3 | "p-value kecil = efek besar/penting" | p-value kecil hanya berarti bukti kuat melawan H0. Dengan n sangat besar, perbedaan yang sangat kecil pun bisa "signifikan". Selalu cek **effect size**! |

### 5.3 Interpretasi p-Value (Panduan Praktis)

| p-value | Kekuatan Bukti Melawan H0 |
|---------|---------------------------|
| > 0.10 | Tidak ada atau sangat lemah |
| 0.05 - 0.10 | Lemah (marginal) |
| 0.01 - 0.05 | Moderate |
| 0.001 - 0.01 | Kuat |
| < 0.001 | Sangat kuat |

**Catatan:** Batas 0.05 adalah konvensi, bukan "garis sakral". Jangan berpikir bahwa p=0.049 dan p=0.051 berbeda secara fundamental.

---

## Bagian 6: Type I Error, Type II Error, dan Power

### 6.1 Matriks Keputusan

|  | H0 Benar (realita) | H0 Salah (realita) |
|--|--------------------|--------------------|
| **Fail to reject H0** | Keputusan BENAR (probability = 1 - alpha) | **Type II Error** (probability = beta) |
| **Reject H0** | **Type I Error** (probability = alpha) | Keputusan BENAR (probability = 1 - beta = **Power**) |

### 6.2 Penjelasan

**Type I Error (alpha) — False Positive:**
- Reject H0 padahal H0 benar
- "Menuduh orang tidak bersalah"
- Contoh: Menyimpulkan obat efektif padahal sebenarnya tidak
- Dikendalikan oleh significance level alpha

**Type II Error (beta) — False Negative:**
- Fail to reject H0 padahal H0 salah
- "Membebaskan orang yang bersalah"
- Contoh: Menyimpulkan obat tidak efektif padahal sebenarnya efektif
- Lebih sulit dikendalikan

**Power (1 - beta):**
- Probabilitas **mendeteksi efek** yang memang ada
- Power yang baik: >= 0.80 (80%)

### 6.3 Faktor yang Mempengaruhi Power

```
Power meningkat jika:
├── Ukuran sampel (n) lebih BESAR
├── Effect size lebih BESAR
├── Significance level (α) lebih BESAR (trade-off dengan Type I!)
└── Variabilitas data lebih KECIL
```

```python
# === VISUALISASI TYPE I ERROR, TYPE II ERROR, DAN POWER ===

fig, ax = plt.subplots(figsize=(12, 6))

# Distribusi di bawah H0
x = np.linspace(-4, 8, 1000)
h0_dist = stats.norm(loc=0, scale=1)
h1_dist = stats.norm(loc=3, scale=1)  # true effect = 3

# Plot distribusi H0
ax.plot(x, h0_dist.pdf(x), 'b-', linewidth=2, label='Distribusi jika H₀ benar')
ax.plot(x, h1_dist.pdf(x), 'r-', linewidth=2, label='Distribusi jika H₁ benar')

# Critical value untuk alpha = 0.05 (one-tailed)
z_crit = stats.norm.ppf(0.95)

# Shade Type I Error (alpha)
x_fill_alpha = np.linspace(z_crit, 5, 200)
ax.fill_between(x_fill_alpha, h0_dist.pdf(x_fill_alpha), color='blue',
                alpha=0.3, label=f'Type I Error (α = {1-stats.norm.cdf(z_crit):.3f})')

# Shade Type II Error (beta)
x_fill_beta = np.linspace(-4, z_crit, 200)
ax.fill_between(x_fill_beta, h1_dist.pdf(x_fill_beta), color='red',
                alpha=0.3, label=f'Type II Error (β = {h1_dist.cdf(z_crit):.3f})')

# Shade Power
x_fill_power = np.linspace(z_crit, 8, 200)
ax.fill_between(x_fill_power, h1_dist.pdf(x_fill_power), color='green',
                alpha=0.3, label=f'Power (1-β = {1-h1_dist.cdf(z_crit):.3f})')

ax.axvline(z_crit, color='black', linestyle='--', linewidth=1,
           label=f'Critical value = {z_crit:.2f}')

ax.set_xlabel('Test Statistic')
ax.set_ylabel('Density')
ax.set_title('Type I Error, Type II Error, dan Power')
ax.legend(loc='upper right', fontsize=9)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## Bagian 7: Effect Size — Cohen's d

### 7.1 Mengapa Effect Size Penting?

**Masalah statistical significance saja:**
- Dengan n = 1,000,000, perbedaan mean 0.01 poin pun bisa "statistically significant"
- Tapi apakah perbedaan 0.01 poin **bermakna secara praktis**? Biasanya tidak!

**Effect size** mengukur **seberapa besar** perbedaan/efek, terlepas dari ukuran sampel.

### 7.2 Cohen's d

**Formula:**

```
Untuk one-sample:
  d = (x̄ - μ₀) / s

Untuk two-sample (independent):
  d = (x̄₁ - x̄₂) / s_pooled

  di mana s_pooled = √((s₁² + s₂²) / 2)
```

**Interpretasi (Cohen's guidelines):**

| |d| | Interpretasi |
|-----|-------------|
| 0.2 | Efek kecil (small) |
| 0.5 | Efek sedang (medium) |
| 0.8 | Efek besar (large) |
| > 1.0 | Efek sangat besar |

### 7.3 Statistical vs Practical Significance

| Skenario | Statistically Significant? | Effect Size | Practically Significant? |
|----------|---------------------------|-------------|-------------------------|
| n=10000, perbedaan mean 0.5 poin | Ya (p < 0.001) | d = 0.05 (tiny) | **Tidak** |
| n=20, perbedaan mean 15 poin | Mungkin tidak (p = 0.08) | d = 0.80 (large) | **Ya!** |
| n=50, perbedaan mean 10 poin | Ya (p = 0.01) | d = 0.65 (medium) | **Ya** |

**Pesan penting:** Selalu laporkan **both** — p-value DAN effect size!

### 7.4 Menghitung Effect Size di Python

```python
# === EFFECT SIZE: COHEN'S D ===

def cohens_d(group1, group2):
    """Hitung Cohen's d untuk independent two-sample."""
    n1, n2 = len(group1), len(group2)
    s1, s2 = group1.std(ddof=1), group2.std(ddof=1)
    s_pooled = np.sqrt((s1**2 + s2**2) / 2)
    d = (group1.mean() - group2.mean()) / s_pooled
    return d

def cohens_d_one_sample(sample, mu_0):
    """Hitung Cohen's d untuk one-sample."""
    return (sample.mean() - mu_0) / sample.std(ddof=1)

# Contoh: Kelas A vs Kelas B (dari Bagian 4)
d = cohens_d(kelas_b, kelas_a)
print(f"Cohen's d (Kelas B vs Kelas A) = {abs(d):.3f}")

if abs(d) < 0.2:
    interpretasi = "negligible (sangat kecil)"
elif abs(d) < 0.5:
    interpretasi = "small (kecil)"
elif abs(d) < 0.8:
    interpretasi = "medium (sedang)"
else:
    interpretasi = "large (besar)"

print(f"Interpretasi: Efek {interpretasi}")
print()
print(f"Laporan lengkap:")
print(f"  t({len(kelas_a) + len(kelas_b) - 2}) = {t_stat:.2f}, "
      f"p = {p_value:.4f}, d = {abs(d):.2f}")
print(f"  Kelas B (M={kelas_b.mean():.1f}, SD={kelas_b.std(ddof=1):.1f}) "
      f"vs Kelas A (M={kelas_a.mean():.1f}, SD={kelas_a.std(ddof=1):.1f})")
```

---

## Bagian 8: Studi Kasus — Apakah Rata-rata Nilai Ujian Berbeda Antar Kelas?

### 8.1 Konteks

Dosen Statistik di UAI mengajar dua kelas paralel. Kelas Pagi menggunakan metode ceramah tradisional, sementara Kelas Siang menggunakan metode **flipped classroom** (mahasiswa menonton video di rumah, kelas untuk diskusi dan latihan). Dosen ingin tahu apakah metode berpengaruh terhadap nilai ujian.

### 8.2 Analisis Lengkap

```python
# === STUDI KASUS LENGKAP ===
np.random.seed(42)

# Data
kelas_pagi = np.array([68, 72, 65, 75, 70, 63, 78, 71, 69, 74,
                        67, 73, 66, 80, 72, 64, 76, 70, 68, 73,
                        71, 62, 77, 69, 74])  # n=25

kelas_siang = np.array([75, 80, 72, 83, 78, 70, 85, 76, 74, 81,
                         73, 79, 71, 88, 77, 69, 82, 75, 73, 80,
                         76, 68, 84, 74, 79, 82, 77, 71])  # n=28

print("=" * 60)
print("STUDI KASUS: Metode Ceramah vs Flipped Classroom")
print("=" * 60)

# 1. Statistik Deskriptif
print("\n1. STATISTIK DESKRIPTIF:")
print(f"   Kelas Pagi (Ceramah):     n={len(kelas_pagi)}, "
      f"mean={kelas_pagi.mean():.2f}, std={kelas_pagi.std(ddof=1):.2f}")
print(f"   Kelas Siang (Flipped):    n={len(kelas_siang)}, "
      f"mean={kelas_siang.mean():.2f}, std={kelas_siang.std(ddof=1):.2f}")
print(f"   Perbedaan mean:           {kelas_siang.mean() - kelas_pagi.mean():.2f} poin")

# 2. Cek asumsi normalitas (opsional, visual)
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

ax = axes[0]
ax.boxplot([kelas_pagi, kelas_siang], labels=['Pagi\n(Ceramah)', 'Siang\n(Flipped)'])
ax.set_ylabel('Nilai Ujian')
ax.set_title('Box Plot: Perbandingan Nilai')
ax.grid(alpha=0.3)

ax = axes[1]
ax.hist(kelas_pagi, bins=10, alpha=0.6, label='Pagi', color='steelblue', edgecolor='black')
ax.hist(kelas_siang, bins=10, alpha=0.6, label='Siang', color='coral', edgecolor='black')
ax.set_xlabel('Nilai')
ax.set_ylabel('Frekuensi')
ax.set_title('Histogram Perbandingan')
ax.legend()

# 3. Uji hipotesis
t_stat, p_val = stats.ttest_ind(kelas_pagi, kelas_siang, equal_var=False)
d = cohens_d(kelas_siang, kelas_pagi)

ax = axes[2]
# Visualisasi hasil uji
labels = ['t-statistic', 'p-value', "Cohen's d"]
values = [abs(t_stat), p_val, abs(d)]
colors = ['steelblue', 'coral', 'green']
bars = ax.bar(labels, values, color=colors, alpha=0.7, edgecolor='black')
ax.set_title('Hasil Uji Hipotesis')
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
            f'{val:.3f}', ha='center', fontsize=11, fontweight='bold')

plt.suptitle('Studi Kasus: Ceramah vs Flipped Classroom di UAI',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()

# 4. Laporan Lengkap
print(f"\n3. HASIL UJI HIPOTESIS (Welch's t-test):")
print(f"   H₀: μ_pagi = μ_siang")
print(f"   H₁: μ_pagi ≠ μ_siang")
print(f"   t = {t_stat:.4f}")
print(f"   p-value = {p_val:.4f}")
print(f"   Cohen's d = {abs(d):.3f}")

print(f"\n4. KESIMPULAN:")
alpha = 0.05
if p_val < alpha:
    print(f"   Pada α = {alpha}, terdapat perbedaan SIGNIFIKAN antara nilai")
    print(f"   kelas Pagi dan Siang (t = {t_stat:.2f}, p = {p_val:.4f}).")
    print(f"   Kelas Siang (flipped classroom, M = {kelas_siang.mean():.1f}) memperoleh")
    print(f"   nilai lebih tinggi dari Kelas Pagi (ceramah, M = {kelas_pagi.mean():.1f}).")
    print(f"   Effect size: d = {abs(d):.2f} → efek {'besar' if abs(d) >= 0.8 else 'sedang' if abs(d) >= 0.5 else 'kecil'}.")
else:
    print(f"   Tidak cukup bukti adanya perbedaan signifikan pada α = {alpha}.")
```

---

## Bagian 9: Panduan Memilih Uji yang Tepat (Decision Tree)

```python
# === CHEAT SHEET: MEMILIH UJI YANG TEPAT ===
print("""
╔══════════════════════════════════════════════════════════╗
║         DECISION TREE: MEMILIH UJI STATISTIK            ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  Berapa kelompok yang dibandingkan?                      ║
║  ├── 1 kelompok vs nilai referensi                       ║
║  │   ├── σ diketahui → z-test                           ║
║  │   └── σ tidak diketahui → ONE-SAMPLE t-test          ║
║  │       scipy: stats.ttest_1samp(data, popmean)        ║
║  │                                                       ║
║  ├── 2 kelompok                                          ║
║  │   ├── Subjek SAMA (paired/before-after)               ║
║  │   │   └── PAIRED t-test                               ║
║  │   │       scipy: stats.ttest_rel(after, before)       ║
║  │   └── Subjek BERBEDA (independent)                    ║
║  │       └── INDEPENDENT t-test (Welch's)                ║
║  │           scipy: stats.ttest_ind(g1, g2,              ║
║  │                                  equal_var=False)     ║
║  │                                                       ║
║  └── 3+ kelompok → ANOVA (Minggu 11)                    ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")
```

---

## Bagian 10: AI Corner

### Prompt untuk AI Assistant

**Prompt 1 — Memformulasikan hipotesis:**
> "Saya ingin menguji apakah mahasiswa yang menggunakan AI assistant mendapat nilai lebih tinggi dibanding yang tidak. Bantu saya merumuskan H0 dan H1, dan rekomendasikan uji statistik yang tepat."

**Prompt 2 — Interpretasi hasil:**
> "Hasil uji saya: t(48) = 2.15, p = 0.037, Cohen's d = 0.42. Bantu saya menginterpretasi hasil ini. Apakah hasilnya signifikan? Apakah efeknya bermakna secara praktis?"

**Prompt 3 — Debugging miskonsepsi:**
> "Teman saya bilang 'p-value = 0.03 berarti ada 3% peluang bahwa H0 benar.' Apakah ini benar? Jelaskan mengapa benar atau salah."

**Catatan penting:** Selalu verifikasi jawaban AI. AI kadang memberikan interpretasi p-value yang salah!

---

## Rangkuman

| Konsep | Poin Utama |
|--------|-----------|
| **H0 dan H1** | H0 = status quo, H1 = yang ingin dibuktikan |
| **z-test** | Sigma diketahui (jarang) |
| **One-sample t-test** | 1 sampel vs nilai referensi, sigma tidak diketahui |
| **Independent t-test** | 2 kelompok berbeda (unpaired) |
| **Paired t-test** | 2 pengukuran dari subjek sama (before-after) |
| **p-value** | P(data seektrem ini JIKA H0 benar), bukan P(H0 benar) |
| **Type I Error** | Reject H0 padahal benar (alpha) |
| **Type II Error** | Fail to reject H0 padahal salah (beta) |
| **Power** | 1 - beta, kemampuan mendeteksi efek nyata |
| **Cohen's d** | Ukuran effect size: 0.2=kecil, 0.5=sedang, 0.8=besar |

---

## Latihan Mandiri

1. **Formulasi Hipotesis:** Untuk masing-masing skenario berikut, tulis H0 dan H1, lalu tentukan uji yang tepat:
   - a) Rata-rata waktu download website UAI lebih dari 3 detik?
   - b) Apakah ada perbedaan IPK antara mahasiswa laki-laki dan perempuan?
   - c) Apakah kursus online meningkatkan skor TOEFL mahasiswa? (data sebelum dan sesudah tersedia)

2. **Hitung Manual:** Diberikan: n=25, x-bar=78.5, s=12.3, mu_0=75, alpha=0.05. Lakukan one-sample t-test (two-tailed). Hitung t-statistic, tentukan keputusan.

3. **Effect Size:** Kelompok A (n=50, mean=82, std=10) vs Kelompok B (n=50, mean=78, std=10). Hitung Cohen's d dan interpretasikan.

4. **Interpretasi p-value:** Koreksi pernyataan-pernyataan berikut:
   - a) "p = 0.03 berarti ada 3% peluang H0 benar"
   - b) "p = 0.07 berarti H0 terbukti benar"
   - c) "p = 0.001 berarti efek pasti besar"

5. **Python Challenge:** Buat simulasi yang menunjukkan bahwa dengan n sangat besar (n=100000), perbedaan mean 0.01 pun bisa "statistically significant" tapi effect size sangat kecil.

---

## Asesmen Minggu Ini

- **Lab 07:** Uji Hipotesis di Python (dikerjakan saat praktikum)
- **Kuis 2:** Materi Minggu 5-7 (30 menit terakhir pertemuan)
- **Tugas 4:** Uji Hipotesis pada Data Riil (deadline: Minggu 9 — melewati UTS)

---

## Referensi

1. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics (4th ed.)*. Chapters 5-6.
2. Downey, A. B. (2021). *Think Stats (2nd ed.)*. Chapter 9.
3. Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences (2nd ed.)*. Lawrence Erlbaum.
4. Wasserstein, R. L., & Lazar, N. A. (2016). "The ASA Statement on p-Values: Context, Process, and Purpose." *The American Statistician*, 70(2), 129-133.

---

## Persiapan Minggu Depan

Minggu 8 adalah **UTS (Ujian Tengah Semester)**. Untuk persiapan:
- Review materi Minggu 1-7
- Kerjakan latihan-latihan di setiap modul
- Fokus pada **interpretasi** — UTS menguji pemahaman konsep, bukan hafalan rumus
- Pelajari modul Minggu 8 (Review dan Tips UTS)

---

*Modul ini merupakan bagian dari mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia.*
