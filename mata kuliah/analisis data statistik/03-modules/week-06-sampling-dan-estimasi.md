# Minggu 6: Sampling dan Estimasi

## Mata Kuliah: Analisis Data Statistik
### Prodi Informatika — Universitas Al Azhar Indonesia — Semester Genap 2025/2026

---

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Minggu** | 6 |
| **Topik** | Sampling dan Estimasi |
| **CPMK** | CPMK-4: Menganalisis data menggunakan teknik inferensi statistik meliputi estimasi parameter dan pengujian hipotesis |
| **Sub-CPMK** | 6.1: Menerapkan teknik sampling dan menghitung confidence interval |
| | 6.2: Melakukan bootstrap estimation menggunakan Python |
| **Bloom's Taxonomy** | C3-C4 (Apply-Analyze) |
| **Durasi** | 100 menit (50 menit teori + 50 menit praktikum) |
| **Prasyarat** | Minggu 5 — Distribusi Probabilitas dan CLT |
| **Tools** | Python, Google Colab, numpy, scipy.stats, matplotlib |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Membedakan** populasi dan sampel serta memahami mengapa sampling diperlukan
2. **Menjelaskan** teknik-teknik sampling beserta kelebihan dan kekurangannya
3. **Menghitung** standard error dan menjelaskan hubungannya dengan sampling distribution
4. **Membedakan** point estimation dan interval estimation
5. **Menghitung** dan **menginterpretasi** confidence interval dengan benar
6. **Mengimplementasikan** bootstrap method untuk estimasi interval menggunakan Python

---

## Peta Konsep Minggu Ini

```
Sampling dan Estimasi
├── Populasi vs Sampel (review)
│   └── Mengapa kita perlu sampel? (biaya, waktu, kerusakan)
├── Teknik Sampling
│   ├── Probability Sampling
│   │   ├── Simple Random Sampling
│   │   ├── Stratified Sampling
│   │   ├── Systematic Sampling
│   │   └── Cluster Sampling
│   └── Non-Probability Sampling (awareness)
├── Sampling Distribution & Standard Error
│   └── Koneksi ke CLT (Minggu 5)
├── Estimasi
│   ├── Point Estimation → satu nilai
│   └── Interval Estimation → rentang nilai
│       ├── Confidence Interval (formula-based)
│       └── Bootstrap CI (resampling-based)
└── Studi Kasus: Survei Kepuasan Mahasiswa UAI
```

---

## Bagian 1: Populasi vs Sampel (Review)

### 1.1 Definisi dan Notasi

| Konsep | Populasi | Sampel |
|--------|----------|--------|
| **Definisi** | Seluruh elemen yang ingin dipelajari | Sebagian elemen yang dipilih dari populasi |
| **Ukuran** | N (biasanya sangat besar atau infinite) | n (lebih kecil, bisa dikelola) |
| **Parameter** | mu (mean), sigma (std) — biasanya **tidak diketahui** | x-bar (mean), s (std) — bisa **dihitung** |
| **Tujuan** | Yang ingin kita ketahui | Yang kita gunakan untuk **mengestimasi** |

**Notasi penting:**

```
Populasi          Sampel
────────          ──────
μ (mu)       →    x̄ (x-bar)     : mean
σ (sigma)    →    s              : standard deviation
σ² (sigma²)  →    s²             : variance
p            →    p̂ (p-hat)      : proporsi
N            →    n              : ukuran
```

### 1.2 Mengapa Sampling?

Kita tidak bisa (atau tidak mau) memeriksa seluruh populasi karena:

1. **Biaya terlalu mahal** — Survei 270 juta penduduk Indonesia? Terlalu mahal!
2. **Waktu terlalu lama** — Sensus BPS dilakukan 10 tahun sekali karena butuh waktu
3. **Destruktif** — Menguji ketahanan semua bola lampu = tidak ada yang tersisa untuk dijual
4. **Tidak mungkin** — Populasi infinite (semua lemparan koin yang mungkin terjadi)

**Kuncinya:** Dengan teknik sampling yang tepat dan ukuran sampel yang cukup, kita bisa membuat **kesimpulan yang valid** tentang populasi hanya dari sampel.

---

## Bagian 2: Teknik Sampling

### 2.1 Simple Random Sampling (SRS)

**Konsep:** Setiap anggota populasi memiliki peluang yang **sama** untuk terpilih.

**Cara:** Beri nomor setiap anggota populasi, lalu gunakan random number generator.

**Kelebihan:**
- Paling sederhana dan mudah dipahami
- Tidak ada bias seleksi
- Analisis statistik paling straightforward

**Kekurangan:**
- Butuh daftar lengkap populasi (sampling frame)
- Bisa tidak representatif jika ada subkelompok kecil yang penting
- Tidak efisien jika populasi tersebar geografis

```python
import numpy as np
import pandas as pd

# === SIMPLE RANDOM SAMPLING ===
np.random.seed(42)

# Simulasi: populasi 1000 mahasiswa UAI
populasi = pd.DataFrame({
    'id': range(1, 1001),
    'prodi': np.random.choice(['Informatika', 'SI', 'Teknik Elektro',
                                'Manajemen', 'Akuntansi'], size=1000),
    'ipk': np.random.normal(3.2, 0.4, 1000).clip(1.0, 4.0)
})

# Ambil simple random sample n=50
sampel_srs = populasi.sample(n=50, random_state=42)

print(f"Populasi: N = {len(populasi)}")
print(f"Sampel: n = {len(sampel_srs)}")
print(f"\nMean IPK Populasi: {populasi['ipk'].mean():.4f}")
print(f"Mean IPK Sampel: {sampel_srs['ipk'].mean():.4f}")
print(f"Perbedaan: {abs(populasi['ipk'].mean() - sampel_srs['ipk'].mean()):.4f}")
```

### 2.2 Stratified Sampling

**Konsep:** Populasi dibagi ke dalam **strata** (subkelompok homogen), lalu sampel diambil dari setiap stratum secara **proporsional** (atau sama rata).

**Kapan digunakan:** Ketika populasi terdiri dari subkelompok yang berbeda dan kita ingin memastikan semua subkelompok terwakili.

**Kelebihan:**
- Menjamin representasi setiap subkelompok
- Lebih presisi (variance lebih kecil) dibanding SRS
- Memungkinkan analisis per subkelompok

**Kekurangan:**
- Perlu informasi tentang strata sebelumnya
- Lebih rumit dalam pelaksanaan

```python
# === STRATIFIED SAMPLING ===
# Ambil sampel proporsional berdasarkan prodi

def stratified_sample(df, strata_col, n_total, random_state=42):
    """Ambil sampel proporsional berdasarkan strata."""
    proportions = df[strata_col].value_counts(normalize=True)
    samples = []

    for stratum, prop in proportions.items():
        n_stratum = max(1, round(n_total * prop))  # minimal 1 per stratum
        stratum_data = df[df[strata_col] == stratum]
        sample = stratum_data.sample(n=min(n_stratum, len(stratum_data)),
                                      random_state=random_state)
        samples.append(sample)

    return pd.concat(samples)

sampel_stratified = stratified_sample(populasi, 'prodi', n_total=50)

print("=== STRATIFIED SAMPLING ===")
print(f"\nProporsi di populasi:")
print(populasi['prodi'].value_counts(normalize=True).round(3))
print(f"\nProporsi di sampel:")
print(sampel_stratified['prodi'].value_counts(normalize=True).round(3))
print(f"\nMean IPK Populasi: {populasi['ipk'].mean():.4f}")
print(f"Mean IPK Sampel Stratified: {sampel_stratified['ipk'].mean():.4f}")
```

### 2.3 Systematic Sampling

**Konsep:** Pilih elemen pertama secara acak, lalu pilih setiap elemen **ke-k** dari daftar (k = N/n).

**Contoh:** Dari 1000 mahasiswa, ingin sampel 50. k = 1000/50 = 20. Pilih angka acak antara 1-20 (misal 7), lalu ambil mahasiswa ke-7, 27, 47, 67, ...

**Kelebihan:**
- Sangat mudah dilaksanakan
- Tersebar merata di seluruh populasi

**Kekurangan:**
- Bisa bias jika ada pola periodik dalam data

```python
# === SYSTEMATIC SAMPLING ===

N = len(populasi)
n = 50
k = N // n  # interval sampling

# Pilih starting point acak
np.random.seed(42)
start = np.random.randint(0, k)

# Ambil setiap elemen ke-k
indices = list(range(start, N, k))[:n]
sampel_systematic = populasi.iloc[indices]

print(f"=== SYSTEMATIC SAMPLING ===")
print(f"Interval k = {k}")
print(f"Starting point = {start}")
print(f"Ukuran sampel = {len(sampel_systematic)}")
print(f"Mean IPK Populasi: {populasi['ipk'].mean():.4f}")
print(f"Mean IPK Sampel Systematic: {sampel_systematic['ipk'].mean():.4f}")
```

### 2.4 Cluster Sampling

**Konsep:** Populasi dibagi ke dalam **cluster** (kelompok heterogen, seperti kelas, desa, rumah sakit), lalu beberapa cluster dipilih secara acak, dan **semua** anggota cluster terpilih diteliti.

**Kapan digunakan:** Ketika tidak ada sampling frame lengkap, tapi ada daftar cluster.

**Kelebihan:**
- Praktis dan ekonomis (tidak perlu daftar lengkap populasi)
- Efisien jika populasi tersebar geografis

**Kekurangan:**
- Variance lebih besar dari SRS dan stratified
- Cluster yang terpilih mungkin tidak representatif

```python
# === CLUSTER SAMPLING ===
# Misalkan cluster = kelas (setiap prodi = 1 cluster)

# Pilih 2 cluster (prodi) secara acak
np.random.seed(42)
selected_clusters = np.random.choice(populasi['prodi'].unique(),
                                      size=2, replace=False)

sampel_cluster = populasi[populasi['prodi'].isin(selected_clusters)]

print(f"=== CLUSTER SAMPLING ===")
print(f"Cluster terpilih: {selected_clusters}")
print(f"Ukuran sampel: {len(sampel_cluster)}")
print(f"Mean IPK Populasi: {populasi['ipk'].mean():.4f}")
print(f"Mean IPK Sampel Cluster: {sampel_cluster['ipk'].mean():.4f}")
```

### 2.5 Ringkasan Perbandingan

| Metode | Representatif | Kemudahan | Biaya | Presisi |
|--------|--------------|-----------|-------|---------|
| Simple Random | Tinggi (jika n besar) | Mudah | Bisa mahal | Baseline |
| Stratified | Sangat tinggi | Sedang | Sedang | Terbaik |
| Systematic | Tinggi | Sangat mudah | Rendah | Baik |
| Cluster | Bervariasi | Mudah di lapangan | Rendah | Terendah |

---

## Bagian 3: Sampling Distribution dan Standard Error

### 3.1 Sampling Distribution

**Konsep:** Jika kita mengambil **banyak** sampel berukuran n dari populasi, dan menghitung statistik (misal: mean) dari setiap sampel, maka **distribusi dari statistik-statistik tersebut** disebut **sampling distribution**.

**Koneksi ke CLT (Minggu 5):**
Central Limit Theorem menyatakan bahwa sampling distribution of the mean mendekati **Normal** untuk n yang cukup besar, dengan:
- Mean = mu (mean populasi)
- Standard deviation = sigma / sqrt(n) → ini disebut **Standard Error**

### 3.2 Standard Error (SE)

**Formula:**

```
Standard Error of the Mean:

SE = σ / √n        (jika σ diketahui)
SE = s / √n        (jika σ tidak diketahui, gunakan s dari sampel)

di mana:
  σ atau s = standard deviation
  n = ukuran sampel
```

**Interpretasi:** Standard Error mengukur **seberapa bervariasi** rata-rata sampel dari satu sampel ke sampel lainnya.

**Poin penting:**
- SE **bukan** standard deviation data! SE adalah standard deviation dari **sampling distribution**
- Semakin besar n, semakin kecil SE → estimasi semakin presisi
- SE mengecil proporsional terhadap sqrt(n), bukan n

```python
from scipy import stats
import matplotlib.pyplot as plt

# === DEMONSTRASI STANDARD ERROR ===
np.random.seed(42)

# Populasi: tinggi badan mahasiswa (mean=165, std=8)
pop_mean = 165
pop_std = 8

sample_sizes = [5, 10, 30, 100, 500]
n_simulations = 2000

fig, axes = plt.subplots(1, len(sample_sizes), figsize=(20, 4))

for i, n in enumerate(sample_sizes):
    # Ambil 2000 sampel berukuran n, hitung mean masing-masing
    sample_means = [np.random.normal(pop_mean, pop_std, n).mean()
                    for _ in range(n_simulations)]

    se_teoritis = pop_std / np.sqrt(n)
    se_empiris = np.std(sample_means)

    axes[i].hist(sample_means, bins=40, density=True, color='steelblue',
                 alpha=0.7, edgecolor='black')
    axes[i].axvline(pop_mean, color='red', linestyle='--', linewidth=2)
    axes[i].set_title(f'n = {n}\nSE teori={se_teoritis:.2f}\nSE empiris={se_empiris:.2f}')
    axes[i].set_xlabel('Rata-rata Sampel')

plt.suptitle('Sampling Distribution: SE mengecil seiring n bertambah',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

## Bagian 4: Point Estimation vs Interval Estimation

### 4.1 Point Estimation

**Konsep:** Memberikan **satu nilai** sebagai estimasi parameter populasi.

**Contoh:**
- x-bar = 72.5 sebagai estimasi mu (mean populasi)
- s = 8.3 sebagai estimasi sigma
- p-hat = 0.65 sebagai estimasi p (proporsi populasi)

**Masalah:** Seberapa akurat estimasi kita? Apakah mu benar-benar 72.5? Atau bisa 70? Atau 75?

Point estimation **tidak memberikan informasi** tentang ketidakpastian estimasi.

### 4.2 Interval Estimation (Confidence Interval)

**Konsep:** Memberikan **rentang nilai** yang kemungkinan besar mengandung parameter populasi, disertai **tingkat kepercayaan** (confidence level).

**Formula Confidence Interval untuk Mean:**

```
Jika σ diketahui (jarang):
  CI = x̄ ± z* × (σ / √n)

Jika σ tidak diketahui (biasanya):
  CI = x̄ ± t* × (s / √n)

di mana:
  x̄ = mean sampel
  z* = z critical value (untuk confidence level tertentu)
  t* = t critical value (df = n-1)
  s = standard deviation sampel
  n = ukuran sampel
```

**Nilai z* yang umum:**

| Confidence Level | z* | t* (approx, df besar) |
|------------------|----|----------------------|
| 90% | 1.645 | 1.645 |
| 95% | 1.960 | 1.960 |
| 99% | 2.576 | 2.576 |

### 4.3 Interpretasi Confidence Interval — YANG BENAR!

Ini adalah salah satu konsep yang **paling sering disalahartikan** dalam statistik.

**Interpretasi yang BENAR:**
> "Jika kita mengulangi proses sampling dan menghitung 95% CI berkali-kali, maka **95% dari CI yang dihasilkan** akan mengandung parameter populasi yang sebenarnya."

**Miskonsepsi umum (SALAH!):**

| No | Miskonsepsi (SALAH) | Mengapa Salah |
|----|---------------------|---------------|
| 1 | "Ada 95% peluang bahwa mu berada di interval ini" | mu adalah **nilai tetap**, bukan random variable. Mu sudah di sana atau tidak. Yang random adalah **interval-nya**. |
| 2 | "95% data berada di interval ini" | CI adalah tentang **mean populasi**, bukan tentang data individual. |
| 3 | "Jika saya ulangi eksperimen, 95% hasilnya akan jatuh di interval ini" | CI berubah setiap kali kita mengambil sampel baru! |

**Visualisasi pemahaman yang benar:**

```python
# === VISUALISASI: APA ARTI 95% CONFIDENCE INTERVAL ===
np.random.seed(42)

pop_mean = 50   # parameter populasi yang TIDAK DIKETAHUI
pop_std = 10
n = 30
n_experiments = 50  # ulangi eksperimen 50 kali
confidence_level = 0.95

fig, ax = plt.subplots(figsize=(10, 12))

contains_mu = 0

for i in range(n_experiments):
    # Ambil sampel
    sample = np.random.normal(pop_mean, pop_std, n)
    x_bar = sample.mean()
    se = sample.std(ddof=1) / np.sqrt(n)
    t_crit = stats.t.ppf((1 + confidence_level) / 2, df=n-1)

    # Hitung CI
    ci_lower = x_bar - t_crit * se
    ci_upper = x_bar + t_crit * se

    # Cek apakah CI mengandung mu
    if ci_lower <= pop_mean <= ci_upper:
        color = 'steelblue'
        contains_mu += 1
    else:
        color = 'red'

    ax.plot([ci_lower, ci_upper], [i, i], color=color, linewidth=2)
    ax.plot(x_bar, i, 'o', color=color, markersize=4)

ax.axvline(pop_mean, color='darkgreen', linestyle='--', linewidth=2,
           label=f'μ sebenarnya = {pop_mean}')
ax.set_xlabel('Nilai')
ax.set_ylabel('Eksperimen ke-')
ax.set_title(f'50 Confidence Intervals (95%)\n'
             f'{contains_mu}/{n_experiments} ({contains_mu/n_experiments*100:.0f}%) '
             f'mengandung μ\n(Merah = tidak mengandung μ)')
ax.legend(loc='upper right')
plt.tight_layout()
plt.show()

print(f"\nDari {n_experiments} CI yang dihitung:")
print(f"  {contains_mu} CI ({contains_mu/n_experiments*100:.0f}%) mengandung μ")
print(f"  {n_experiments - contains_mu} CI ({(n_experiments - contains_mu)/n_experiments*100:.0f}%) TIDAK mengandung μ")
```

### 4.4 Menghitung Confidence Interval dengan Python

```python
# === MENGHITUNG CONFIDENCE INTERVAL ===

# Data: nilai ujian 30 mahasiswa
np.random.seed(42)
nilai = np.random.normal(loc=72, scale=10, size=30)

# Statistik sampel
n = len(nilai)
x_bar = nilai.mean()
s = nilai.std(ddof=1)  # ddof=1 untuk sampel
se = s / np.sqrt(n)

print(f"Statistik Sampel:")
print(f"  n = {n}")
print(f"  x̄ = {x_bar:.2f}")
print(f"  s = {s:.2f}")
print(f"  SE = {se:.2f}")
print()

# --- Cara 1: Hitung manual ---
confidence = 0.95
alpha = 1 - confidence
t_crit = stats.t.ppf(1 - alpha/2, df=n-1)

ci_lower = x_bar - t_crit * se
ci_upper = x_bar + t_crit * se

print(f"95% CI (manual): ({ci_lower:.2f}, {ci_upper:.2f})")

# --- Cara 2: Menggunakan scipy.stats ---
ci = stats.t.interval(confidence=confidence, df=n-1, loc=x_bar, scale=se)
print(f"95% CI (scipy):  ({ci[0]:.2f}, {ci[1]:.2f})")

# --- Interpretasi ---
print(f"\nInterpretasi:")
print(f"Kita 95% percaya diri bahwa metode ini menghasilkan interval")
print(f"yang mengandung rata-rata populasi sebenarnya.")
print(f"Interval: ({ci_lower:.2f}, {ci_upper:.2f})")
print(f"Lebar interval: {ci_upper - ci_lower:.2f}")
```

---

## Bagian 5: Bootstrap Method

### 5.1 Apa Itu Bootstrap?

**Bootstrap** adalah teknik **resampling** yang memungkinkan kita mengestimasi distribusi sampling **tanpa asumsi** tentang distribusi populasi.

**Ide dasar:** Jika kita tidak tahu distribusi populasi, gunakan **sampel yang kita punya** sebagai "pengganti" populasi. Ambil ulang (resample) dari sampel ini berkali-kali **dengan pengembalian** (with replacement).

**Langkah-langkah Bootstrap:**

```
1. Dari sampel asli (ukuran n), ambil sampel baru ukuran n
   DENGAN PENGEMBALIAN (data bisa terambil lebih dari sekali)
2. Hitung statistik yang diinginkan (misal: mean)
3. Ulangi langkah 1-2 sebanyak B kali (biasanya B = 1000-10000)
4. Kumpulkan B statistik tersebut → ini adalah bootstrap distribution
5. Gunakan percentile dari bootstrap distribution sebagai CI
```

### 5.2 Mengapa Bootstrap Powerful?

1. **Tidak memerlukan asumsi distribusi** — tidak perlu tahu distribusi populasi Normal atau tidak
2. **Bisa digunakan untuk statistik apapun** — mean, median, rasio, korelasi, dll.
3. **Sederhana secara konseptual** — hanya perlu "ambil ulang dan hitung"
4. **Bekerja baik untuk sampel kecil** (dengan catatan)

### 5.3 Implementasi Bootstrap di Python

```python
# === BOOTSTRAP CONFIDENCE INTERVAL ===

np.random.seed(42)

# Data sampel: waktu respons (milidetik) server UAI
data = np.array([120, 135, 142, 128, 155, 162, 138, 145, 131, 148,
                 160, 125, 140, 133, 152, 167, 129, 143, 137, 158,
                 172, 119, 146, 136, 150, 155, 141, 134, 163, 127])

print(f"Data waktu respons server (ms):")
print(f"  n = {len(data)}")
print(f"  Mean = {data.mean():.2f} ms")
print(f"  Median = {np.median(data):.2f} ms")
print(f"  Std = {data.std(ddof=1):.2f} ms")
print()

def bootstrap_ci(data, statistic_func, n_bootstrap=10000,
                 confidence=0.95, random_state=42):
    """
    Hitung bootstrap confidence interval.

    Parameters:
    -----------
    data : array-like
        Data sampel asli
    statistic_func : callable
        Fungsi statistik (misal: np.mean, np.median)
    n_bootstrap : int
        Jumlah bootstrap resamples
    confidence : float
        Tingkat kepercayaan (0-1)
    random_state : int
        Seed untuk reproducibility

    Returns:
    --------
    tuple: (ci_lower, ci_upper, bootstrap_statistics)
    """
    np.random.seed(random_state)
    n = len(data)

    # Generate bootstrap resamples dan hitung statistik
    bootstrap_stats = np.array([
        statistic_func(np.random.choice(data, size=n, replace=True))
        for _ in range(n_bootstrap)
    ])

    # Percentile method
    alpha = 1 - confidence
    ci_lower = np.percentile(bootstrap_stats, 100 * alpha / 2)
    ci_upper = np.percentile(bootstrap_stats, 100 * (1 - alpha / 2))

    return ci_lower, ci_upper, bootstrap_stats


# Bootstrap CI untuk MEAN
ci_low, ci_high, boot_means = bootstrap_ci(data, np.mean)
print(f"Bootstrap 95% CI untuk Mean: ({ci_low:.2f}, {ci_high:.2f})")

# Bootstrap CI untuk MEDIAN
ci_low_med, ci_high_med, boot_medians = bootstrap_ci(data, np.median)
print(f"Bootstrap 95% CI untuk Median: ({ci_low_med:.2f}, {ci_high_med:.2f})")

# Bandingkan dengan formula-based CI (t-interval)
from scipy import stats

n = len(data)
se = data.std(ddof=1) / np.sqrt(n)
t_ci = stats.t.interval(confidence=0.95, df=n-1, loc=data.mean(), scale=se)
print(f"Formula-based 95% CI untuk Mean: ({t_ci[0]:.2f}, {t_ci[1]:.2f})")
```

### 5.4 Visualisasi Bootstrap

```python
# === VISUALISASI BOOTSTRAP ===

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Bootstrap distribution untuk Mean
ax = axes[0]
ax.hist(boot_means, bins=50, density=True, color='steelblue',
        alpha=0.7, edgecolor='black')
ax.axvline(data.mean(), color='red', linestyle='--', linewidth=2,
           label=f'Sample mean = {data.mean():.2f}')
ax.axvline(ci_low, color='green', linestyle=':', linewidth=2,
           label=f'95% CI: ({ci_low:.2f}, {ci_high:.2f})')
ax.axvline(ci_high, color='green', linestyle=':', linewidth=2)
ax.fill_betweenx([0, ax.get_ylim()[1] if ax.get_ylim()[1] > 0 else 0.5],
                  ci_low, ci_high, color='green', alpha=0.1)
ax.set_title('Bootstrap Distribution: Mean')
ax.set_xlabel('Bootstrap Mean (ms)')
ax.set_ylabel('Density')
ax.legend(fontsize=9)

# Plot 2: Bootstrap distribution untuk Median
ax = axes[1]
ax.hist(boot_medians, bins=50, density=True, color='coral',
        alpha=0.7, edgecolor='black')
ax.axvline(np.median(data), color='red', linestyle='--', linewidth=2,
           label=f'Sample median = {np.median(data):.2f}')
ax.axvline(ci_low_med, color='green', linestyle=':', linewidth=2,
           label=f'95% CI: ({ci_low_med:.2f}, {ci_high_med:.2f})')
ax.axvline(ci_high_med, color='green', linestyle=':', linewidth=2)
ax.set_title('Bootstrap Distribution: Median')
ax.set_xlabel('Bootstrap Median (ms)')
ax.set_ylabel('Density')
ax.legend(fontsize=9)

plt.suptitle('Bootstrap Confidence Intervals', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()
```

### 5.5 Bootstrap vs Formula-Based CI

| Aspek | Formula-Based (t-interval) | Bootstrap |
|-------|---------------------------|-----------|
| **Asumsi** | Data mendekati Normal (atau n besar) | Minimal asumsi distribusi |
| **Statistik** | Biasanya hanya untuk mean | Bisa untuk statistik apapun |
| **Implementasi** | Hitung rumus | Simulasi komputer |
| **Interpretasi** | Standard (dari teori) | Percentile dari distribusi bootstrap |
| **Kapan lebih baik** | Sampel besar, data Normal | Sampel kecil, distribusi tidak jelas |
| **Kecepatan** | Sangat cepat | Butuh komputasi (tapi tetap cepat di Python) |

---

## Bagian 6: Studi Kasus — Survei Kepuasan Mahasiswa UAI

### 6.1 Konteks

Prodi Informatika UAI ingin mengetahui tingkat kepuasan mahasiswa terhadap fasilitas laboratorium komputer. Tidak mungkin mewawancarai seluruh 500 mahasiswa aktif, sehingga dilakukan **survei** terhadap sampel mahasiswa.

### 6.2 Desain Sampling

```python
# === STUDI KASUS: SURVEI KEPUASAN MAHASISWA UAI ===
np.random.seed(42)

# Simulasi "populasi" 500 mahasiswa
# Skor kepuasan: skala 1-5 (1=sangat tidak puas, 5=sangat puas)
populasi_kepuasan = np.random.choice(
    [1, 2, 3, 4, 5],
    size=500,
    p=[0.05, 0.10, 0.25, 0.40, 0.20]  # distribusi tidak Normal!
)

print(f"=== POPULASI (biasanya tidak diketahui) ===")
print(f"N = {len(populasi_kepuasan)}")
print(f"Mean kepuasan = {populasi_kepuasan.mean():.3f}")
print(f"Distribusi:")
for skor in [1, 2, 3, 4, 5]:
    count = (populasi_kepuasan == skor).sum()
    print(f"  Skor {skor}: {count} ({count/len(populasi_kepuasan)*100:.1f}%)")

# Ambil sampel n=50
sampel = np.random.choice(populasi_kepuasan, size=50, replace=False)

print(f"\n=== SAMPEL ===")
print(f"n = {len(sampel)}")
print(f"Mean kepuasan = {sampel.mean():.3f}")
print(f"Std = {sampel.std(ddof=1):.3f}")
```

### 6.3 Estimasi dan Confidence Interval

```python
# Hitung CI menggunakan kedua metode
n = len(sampel)
x_bar = sampel.mean()
se = sampel.std(ddof=1) / np.sqrt(n)

# 1. Formula-based CI (t-interval)
ci_formula = stats.t.interval(0.95, df=n-1, loc=x_bar, scale=se)
print(f"\n=== ESTIMASI ===")
print(f"Point estimate (mean): {x_bar:.3f}")
print(f"Standard error: {se:.3f}")
print(f"95% CI (formula): ({ci_formula[0]:.3f}, {ci_formula[1]:.3f})")

# 2. Bootstrap CI
ci_low_bs, ci_high_bs, boot_means_kasus = bootstrap_ci(sampel, np.mean)
print(f"95% CI (bootstrap): ({ci_low_bs:.3f}, {ci_high_bs:.3f})")

# Bandingkan dengan populasi sebenarnya
print(f"\nPopulation mean (sebenarnya): {populasi_kepuasan.mean():.3f}")
print(f"Apakah CI formula mengandung μ? {ci_formula[0] <= populasi_kepuasan.mean() <= ci_formula[1]}")
print(f"Apakah CI bootstrap mengandung μ? {ci_low_bs <= populasi_kepuasan.mean() <= ci_high_bs}")
```

### 6.4 Laporan Survei

```python
# === LAPORAN VISUAL ===

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Plot 1: Distribusi kepuasan di sampel
ax = axes[0]
skor_values, counts = np.unique(sampel, return_counts=True)
ax.bar(skor_values, counts, color='steelblue', edgecolor='black', alpha=0.7)
ax.set_xlabel('Skor Kepuasan')
ax.set_ylabel('Jumlah Responden')
ax.set_title(f'Distribusi Kepuasan (n={n})')
ax.set_xticks([1, 2, 3, 4, 5])

# Plot 2: Point estimate + CI
ax = axes[1]
ax.errorbar(1, x_bar, yerr=[[x_bar - ci_formula[0]], [ci_formula[1] - x_bar]],
            fmt='o', color='steelblue', capsize=10, capthick=2, markersize=10,
            label='Formula CI')
ax.errorbar(1.3, x_bar, yerr=[[x_bar - ci_low_bs], [ci_high_bs - x_bar]],
            fmt='s', color='coral', capsize=10, capthick=2, markersize=10,
            label='Bootstrap CI')
ax.axhline(populasi_kepuasan.mean(), color='green', linestyle='--',
           label=f'μ populasi = {populasi_kepuasan.mean():.3f}')
ax.set_xlim(0.5, 2)
ax.set_ylabel('Skor Kepuasan')
ax.set_title('Point Estimate + 95% CI')
ax.legend(fontsize=8)
ax.set_xticks([])

# Plot 3: Bootstrap distribution
ax = axes[2]
ax.hist(boot_means_kasus, bins=40, density=True, color='coral',
        alpha=0.7, edgecolor='black')
ax.axvline(ci_low_bs, color='green', linestyle=':', linewidth=2)
ax.axvline(ci_high_bs, color='green', linestyle=':', linewidth=2)
ax.set_xlabel('Bootstrap Mean')
ax.set_ylabel('Density')
ax.set_title('Bootstrap Distribution')

plt.suptitle('Survei Kepuasan Mahasiswa UAI — Fasilitas Lab Komputer',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

## Bagian 7: AI Corner

### Prompt untuk AI Assistant

**Prompt 1 — Desain sampling:**
> "Saya ingin melakukan survei terhadap mahasiswa di kampus saya untuk mengetahui pendapat mereka tentang fasilitas perpustakaan. Ada 5 fakultas dengan jumlah mahasiswa berbeda-beda. Teknik sampling apa yang sebaiknya saya gunakan dan mengapa?"

**Prompt 2 — Interpretasi CI:**
> "Saya menghitung 95% confidence interval dan mendapatkan (68.5, 75.3). Jelaskan apa artinya ini dalam bahasa yang sederhana. Juga, koreksi saya jika interpretasi saya salah: 'Ada 95% peluang bahwa mean populasi berada di antara 68.5 dan 75.3.'"

**Prompt 3 — Bootstrap:**
> "Jelaskan perbedaan antara bootstrap confidence interval dan traditional confidence interval. Kapan saya harus menggunakan bootstrap?"

**Ingat:** Selalu verifikasi jawaban AI dengan menjalankan kode sendiri dan membandingkan dengan materi kuliah.

---

## Rangkuman

| Konsep | Poin Utama |
|--------|-----------|
| **Simple Random Sampling** | Setiap anggota peluang sama, butuh sampling frame |
| **Stratified Sampling** | Bagi populasi ke strata, paling presisi |
| **Systematic Sampling** | Pilih setiap ke-k, mudah dan praktis |
| **Cluster Sampling** | Pilih kelompok, ekonomis tapi variance besar |
| **Standard Error** | SE = s / sqrt(n), ukuran presisi estimasi |
| **Confidence Interval** | Rentang yang (kemungkinan besar) mengandung parameter |
| **Interpretasi CI** | 95% dari CI yang dibuat akan mengandung mu (BUKAN 95% peluang mu di interval) |
| **Bootstrap** | Resampling with replacement, minimal asumsi |

---

## Latihan Mandiri

1. **Latihan Sampling:** Kamu ingin mensurvei 100 mahasiswa UAI dari 5 prodi yang jumlah mahasiswanya berbeda. Gunakan Python untuk melakukan stratified sampling proporsional.

2. **Latihan CI:** Dari sampel 40 mahasiswa, mean IPK = 3.25 dan std = 0.35. Hitung 90%, 95%, dan 99% confidence interval. Apa yang terjadi pada lebar interval saat confidence level meningkat?

3. **Latihan Bootstrap:** Gunakan data berikut (waktu akses website dalam detik): [2.1, 3.5, 1.8, 4.2, 2.7, 3.1, 5.0, 2.3, 3.8, 1.5]. Hitung bootstrap 95% CI untuk mean dan median. Bandingkan hasilnya.

4. **Latihan Interpretasi:** Jelaskan mengapa pernyataan berikut SALAH: "Confidence interval 95% artinya 95% data berada di dalam interval tersebut."

5. **Latihan Praktis:** Dari studi kasus survei UAI di atas, jika kamu diminta meningkatkan presisi estimasi (mempersempit CI), apa dua cara yang bisa dilakukan? Jelaskan trade-off masing-masing.

---

## Asesmen Minggu Ini

- **Lab 06:** Sampling & Bootstrap (dikerjakan saat praktikum)
- Tidak ada tugas minggu ini, tapi gunakan waktu untuk mempersiapkan materi Minggu 7

---

## Referensi

1. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics (4th ed.)*. Chapter 5.
2. Bruce, P., & Bruce, A. (2020). *Practical Statistics for Data Scientists (2nd ed.)*. Chapter 2.
3. Efron, B., & Tibshirani, R. J. (1993). *An Introduction to the Bootstrap*. Chapman and Hall.

---

## Persiapan Minggu Depan

Minggu 7 akan membahas **Uji Hipotesis**. Untuk persiapan:
- Pastikan memahami confidence interval (fondasi uji hipotesis)
- Review konsep p-value dari materi SMA/kuliah Semester 1
- Baca Diez et al. (2019) Chapter 5, bagian hypothesis testing
- CLT + CI + SE adalah pondasi untuk uji hipotesis — pastikan solid!

---

*Modul ini merupakan bagian dari mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia.*
