# Lab 02: Statistika Deskriptif dengan Python

**Mata Kuliah:** Statistika dan Probabilitas
**Program Studi:** Universitas Al Azhar Indonesia
**Minggu:** 2
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. Memuat dan membersihkan dataset menggunakan pandas
2. Menghitung ukuran pemusatan data (mean, median, modus)
3. Menghitung ukuran penyebaran data (range, variance, standard deviation, IQR)
4. Mengidentifikasi outlier menggunakan metode IQR
5. Melakukan analisis grouped (groupby) pada data kategorikal

---

## Persiapan

- Google Colab notebook baru
- Nama file: `Lab02_NamaAnda_NIM.ipynb`
- Pastikan library pandas, numpy, dan matplotlib sudah bisa diimpor

---

## Langkah-langkah

### Langkah 1: Setup dan Import Library

```python
# =============================================
# LANGKAH 1: Setup
# =============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Atur tampilan pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format)

# Set random seed untuk reproducibility
np.random.seed(42)

print("Setup selesai!")
```

### Langkah 2: Membuat Dataset Simulasi BPS

Kita akan membuat data simulasi yang menyerupai data survei sosial ekonomi dari BPS (Badan Pusat Statistik).

```python
# =============================================
# LANGKAH 2: Generate Data Simulasi BPS
# =============================================

n = 200  # jumlah responden

# Generate data simulasi
data = {
    'id_responden': range(1, n + 1),
    'provinsi': np.random.choice(
        ['DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur', 'Banten'],
        size=n, p=[0.25, 0.25, 0.20, 0.20, 0.10]
    ),
    'jenis_kelamin': np.random.choice(['Laki-laki', 'Perempuan'], size=n),
    'usia': np.random.normal(35, 12, size=n).astype(int).clip(18, 65),
    'pendidikan': np.random.choice(
        ['SD', 'SMP', 'SMA', 'D3', 'S1', 'S2'],
        size=n, p=[0.10, 0.15, 0.30, 0.15, 0.25, 0.05]
    ),
    'pendapatan_juta': np.round(np.random.lognormal(mean=1.5, sigma=0.7, size=n), 2),
    'pengeluaran_juta': None,  # akan dihitung
    'jumlah_anggota_keluarga': np.random.choice([1, 2, 3, 4, 5, 6, 7], size=n,
                                                 p=[0.05, 0.10, 0.20, 0.30, 0.20, 0.10, 0.05]),
    'status_pekerjaan': np.random.choice(
        ['PNS', 'Swasta', 'Wiraswasta', 'Freelance', 'Tidak Bekerja'],
        size=n, p=[0.15, 0.35, 0.25, 0.15, 0.10]
    ),
}

df = pd.DataFrame(data)

# Pengeluaran = 60-90% dari pendapatan + noise
rasio = np.random.uniform(0.60, 0.90, size=n)
df['pengeluaran_juta'] = np.round(df['pendapatan_juta'] * rasio, 2)

# Tambahkan beberapa outlier secara sengaja
df.loc[5, 'pendapatan_juta'] = 85.0   # outlier atas
df.loc[15, 'pendapatan_juta'] = 92.5  # outlier atas
df.loc[100, 'pendapatan_juta'] = 0.15 # outlier bawah

print(f"Dataset berhasil dibuat: {df.shape[0]} baris x {df.shape[1]} kolom")
print(f"\nKolom: {list(df.columns)}")
df.head(10)
```

### Langkah 3: Eksplorasi Awal Dataset

```python
# =============================================
# LANGKAH 3: Eksplorasi Awal
# =============================================

# Informasi dataset
print("=== INFO DATASET ===")
print(df.info())

print("\n=== TIPE DATA ===")
print(df.dtypes)

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== 5 BARIS PERTAMA ===")
df.head()
```

### Langkah 4: Statistik Deskriptif dengan df.describe()

```python
# =============================================
# LANGKAH 4: df.describe()
# =============================================

# Statistik untuk kolom numerik
print("=== STATISTIK DESKRIPTIF (NUMERIK) ===")
print(df.describe())

# Statistik untuk kolom kategorikal
print("\n=== STATISTIK DESKRIPTIF (KATEGORIKAL) ===")
print(df.describe(include='object'))
```

### Langkah 5: Menghitung Manual dengan NumPy

```python
# =============================================
# LANGKAH 5: Hitung Manual dengan NumPy
# =============================================

pendapatan = df['pendapatan_juta'].values

# --- Ukuran Pemusatan ---
print("=" * 50)
print("UKURAN PEMUSATAN DATA (Central Tendency)")
print("=" * 50)

# Mean (rata-rata)
mean_manual = np.sum(pendapatan) / len(pendapatan)
mean_numpy = np.mean(pendapatan)
print(f"Mean (manual) : {mean_manual:.4f} juta")
print(f"Mean (numpy)  : {mean_numpy:.4f} juta")

# Median (nilai tengah)
sorted_data = np.sort(pendapatan)
n = len(sorted_data)
if n % 2 == 0:
    median_manual = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
else:
    median_manual = sorted_data[n//2]
median_numpy = np.median(pendapatan)
print(f"\nMedian (manual): {median_manual:.4f} juta")
print(f"Median (numpy) : {median_numpy:.4f} juta")

# Modus
from scipy import stats
modus = stats.mode(pendapatan, keepdims=True)
print(f"\nModus: {modus.mode[0]:.4f} juta (frekuensi: {modus.count[0]})")

# Perbandingan mean vs median
print(f"\nMean > Median? {mean_numpy > median_numpy}")
print("-> Jika mean > median, distribusi cenderung right-skewed (condong kanan)")
```

### Langkah 6: Ukuran Penyebaran Data

```python
# =============================================
# LANGKAH 6: Ukuran Penyebaran (Dispersion)
# =============================================

print("=" * 50)
print("UKURAN PENYEBARAN DATA (Measures of Spread)")
print("=" * 50)

# Range
range_val = np.max(pendapatan) - np.min(pendapatan)
print(f"Range: {range_val:.4f} juta")
print(f"  Min: {np.min(pendapatan):.4f}, Max: {np.max(pendapatan):.4f}")

# Variance (variansi)
# Variansi populasi (ddof=0) vs sampel (ddof=1)
var_populasi = np.var(pendapatan, ddof=0)
var_sampel = np.var(pendapatan, ddof=1)
print(f"\nVariansi populasi (ddof=0): {var_populasi:.4f}")
print(f"Variansi sampel   (ddof=1): {var_sampel:.4f}")

# Standard Deviation (simpangan baku)
std_populasi = np.std(pendapatan, ddof=0)
std_sampel = np.std(pendapatan, ddof=1)
print(f"\nStd Dev populasi: {std_populasi:.4f} juta")
print(f"Std Dev sampel  : {std_sampel:.4f} juta")

# Hitung manual variansi sampel
deviasi = pendapatan - np.mean(pendapatan)
deviasi_kuadrat = deviasi ** 2
var_manual = np.sum(deviasi_kuadrat) / (len(pendapatan) - 1)
print(f"\nVariansi sampel (manual): {var_manual:.4f}")
print(f"Cocok dengan numpy? {np.isclose(var_manual, var_sampel)}")

# Quartiles dan IQR
Q1 = np.percentile(pendapatan, 25)
Q2 = np.percentile(pendapatan, 50)  # = median
Q3 = np.percentile(pendapatan, 75)
IQR = Q3 - Q1

print(f"\n--- Quartiles ---")
print(f"Q1 (25%): {Q1:.4f} juta")
print(f"Q2 (50%): {Q2:.4f} juta (median)")
print(f"Q3 (75%): {Q3:.4f} juta")
print(f"IQR (Q3-Q1): {IQR:.4f} juta")

# Coefficient of Variation
cv = (std_sampel / mean_numpy) * 100
print(f"\nCoefficient of Variation: {cv:.2f}%")
```

### Langkah 7: Identifikasi Outlier dengan Metode IQR

```python
# =============================================
# LANGKAH 7: Identifikasi Outlier (Metode IQR)
# =============================================

print("=" * 50)
print("IDENTIFIKASI OUTLIER - METODE IQR")
print("=" * 50)

# Batas bawah dan atas
batas_bawah = Q1 - 1.5 * IQR
batas_atas = Q3 + 1.5 * IQR

print(f"Q1: {Q1:.2f}")
print(f"Q3: {Q3:.2f}")
print(f"IQR: {IQR:.2f}")
print(f"Batas Bawah: Q1 - 1.5*IQR = {batas_bawah:.2f}")
print(f"Batas Atas : Q3 + 1.5*IQR = {batas_atas:.2f}")

# Temukan outlier
outliers = df[(df['pendapatan_juta'] < batas_bawah) |
              (df['pendapatan_juta'] > batas_atas)]

print(f"\nJumlah outlier: {len(outliers)} dari {len(df)} data ({len(outliers)/len(df)*100:.1f}%)")
print("\nData outlier:")
print(outliers[['id_responden', 'provinsi', 'pendapatan_juta', 'status_pekerjaan']])

# Visualisasi boxplot
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Boxplot pendapatan
axes[0].boxplot(df['pendapatan_juta'], vert=True)
axes[0].set_title('Boxplot Pendapatan (Juta Rp)', fontsize=13)
axes[0].set_ylabel('Pendapatan (Juta Rp)')
axes[0].axhline(y=batas_atas, color='red', linestyle='--', alpha=0.7, label=f'Batas Atas: {batas_atas:.1f}')
axes[0].axhline(y=batas_bawah, color='red', linestyle='--', alpha=0.7, label=f'Batas Bawah: {batas_bawah:.1f}')
axes[0].legend(fontsize=9)

# Histogram dengan batas outlier
axes[1].hist(df['pendapatan_juta'], bins=30, color='steelblue', edgecolor='white', alpha=0.8)
axes[1].axvline(x=batas_bawah, color='red', linestyle='--', label=f'Batas Bawah: {batas_bawah:.1f}')
axes[1].axvline(x=batas_atas, color='red', linestyle='--', label=f'Batas Atas: {batas_atas:.1f}')
axes[1].set_title('Histogram Pendapatan dengan Batas Outlier', fontsize=13)
axes[1].set_xlabel('Pendapatan (Juta Rp)')
axes[1].set_ylabel('Frekuensi')
axes[1].legend(fontsize=9)

plt.tight_layout()
plt.show()
```

### Langkah 8: Analisis Groupby

```python
# =============================================
# LANGKAH 8: Analisis Groupby
# =============================================

print("=" * 50)
print("ANALISIS BERDASARKAN KELOMPOK (GROUPBY)")
print("=" * 50)

# Statistik pendapatan per provinsi
print("\n--- Pendapatan per Provinsi ---")
grouped_provinsi = df.groupby('provinsi')['pendapatan_juta'].agg(
    ['count', 'mean', 'median', 'std', 'min', 'max']
).round(2)
grouped_provinsi.columns = ['N', 'Mean', 'Median', 'Std', 'Min', 'Max']
print(grouped_provinsi)

# Statistik pendapatan per jenis kelamin
print("\n--- Pendapatan per Jenis Kelamin ---")
grouped_gender = df.groupby('jenis_kelamin')['pendapatan_juta'].agg(
    ['count', 'mean', 'median', 'std']
).round(2)
grouped_gender.columns = ['N', 'Mean', 'Median', 'Std']
print(grouped_gender)

# Statistik per status pekerjaan
print("\n--- Pendapatan per Status Pekerjaan ---")
grouped_pekerjaan = df.groupby('status_pekerjaan')['pendapatan_juta'].agg(
    ['count', 'mean', 'median', 'std']
).round(2).sort_values('mean', ascending=False)
grouped_pekerjaan.columns = ['N', 'Mean', 'Median', 'Std']
print(grouped_pekerjaan)

# Cross tabulation
print("\n--- Tabulasi Silang: Provinsi x Jenis Kelamin ---")
cross_tab = pd.crosstab(df['provinsi'], df['jenis_kelamin'], margins=True)
print(cross_tab)
```

### Langkah 9: Tabel Distribusi Frekuensi

```python
# =============================================
# LANGKAH 9: Distribusi Frekuensi
# =============================================

print("=" * 50)
print("DISTRIBUSI FREKUENSI PENDAPATAN")
print("=" * 50)

# Buat kelas interval
bins = [0, 2, 4, 6, 8, 10, 15, 20, 100]
labels = ['0-2', '2-4', '4-6', '6-8', '8-10', '10-15', '15-20', '>20']

df['kelas_pendapatan'] = pd.cut(df['pendapatan_juta'], bins=bins, labels=labels, right=False)

# Tabel frekuensi
freq_table = df['kelas_pendapatan'].value_counts().sort_index().reset_index()
freq_table.columns = ['Kelas Pendapatan (Juta)', 'Frekuensi']
freq_table['Frekuensi Relatif (%)'] = (freq_table['Frekuensi'] / freq_table['Frekuensi'].sum() * 100).round(1)
freq_table['Frekuensi Kumulatif'] = freq_table['Frekuensi'].cumsum()
freq_table['Frek. Kum. Relatif (%)'] = (freq_table['Frekuensi Kumulatif'] / freq_table['Frekuensi'].sum() * 100).round(1)

print(freq_table.to_string(index=False))

# Visualisasi
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart frekuensi
axes[0].bar(freq_table['Kelas Pendapatan (Juta)'], freq_table['Frekuensi'],
            color='steelblue', edgecolor='white')
axes[0].set_title('Distribusi Frekuensi Pendapatan', fontsize=13)
axes[0].set_xlabel('Kelas Pendapatan (Juta Rp)')
axes[0].set_ylabel('Frekuensi')
axes[0].tick_params(axis='x', rotation=45)

# Ogive (frekuensi kumulatif)
axes[1].plot(freq_table['Kelas Pendapatan (Juta)'], freq_table['Frek. Kum. Relatif (%)'],
             marker='o', color='coral', linewidth=2)
axes[1].set_title('Ogive (Frekuensi Kumulatif Relatif)', fontsize=13)
axes[1].set_xlabel('Kelas Pendapatan (Juta Rp)')
axes[1].set_ylabel('Frekuensi Kumulatif (%)')
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

### Langkah 10: Ringkasan Temuan

```python
# =============================================
# LANGKAH 10: Ringkasan
# =============================================

print("=" * 60)
print("RINGKASAN ANALISIS STATISTIKA DESKRIPTIF")
print("=" * 60)

print(f"""
Dataset: Simulasi Data Sosial Ekonomi (n={len(df)})

1. UKURAN PEMUSATAN:
   - Mean pendapatan  : {df['pendapatan_juta'].mean():.2f} juta
   - Median pendapatan: {df['pendapatan_juta'].median():.2f} juta
   - Mean > Median -> Distribusi right-skewed

2. UKURAN PENYEBARAN:
   - Std Dev  : {df['pendapatan_juta'].std():.2f} juta
   - IQR      : {IQR:.2f} juta
   - CV       : {cv:.1f}%

3. OUTLIER:
   - Ditemukan {len(outliers)} outlier dari {len(df)} data
   - Batas: [{batas_bawah:.2f}, {batas_atas:.2f}]

4. PERBEDAAN ANTAR KELOMPOK:
   - Provinsi dengan mean pendapatan tertinggi:
     {grouped_provinsi['Mean'].idxmax()} ({grouped_provinsi['Mean'].max():.2f} juta)
   - Status pekerjaan dengan mean tertinggi:
     {grouped_pekerjaan['Mean'].idxmax()} ({grouped_pekerjaan['Mean'].max():.2f} juta)
""")
```

---

## Tugas yang Harus Dikumpulkan

Kumpulkan notebook (.ipynb) yang berisi:

1. **Semua kode** dari Langkah 1-10 yang sudah dijalankan (tanpa error)
2. **Tambahan analisis** untuk kolom `pengeluaran_juta`:
   - Hitung mean, median, std, IQR
   - Identifikasi outlier
   - Buat groupby per provinsi
3. **Interpretasi tertulis** (minimal 3 paragraf) dalam text cell yang menjelaskan temuan utama Anda

---

## Rubrik Singkat

| Kriteria | Bobot | Keterangan |
|----------|-------|------------|
| Kelengkapan kode | 30% | Semua langkah 1-10 dijalankan tanpa error |
| Analisis tambahan | 30% | Analisis pengeluaran lengkap dan benar |
| Interpretasi | 25% | Interpretasi jelas, relevan, dan menunjukkan pemahaman |
| Kerapian notebook | 15% | Notebook terstruktur rapi dengan text cell penjelasan |

---

## Challenge / Bonus

```python
# =============================================
# CHALLENGE: Skewness dan Kurtosis
# =============================================

from scipy.stats import skew, kurtosis

pendapatan = df['pendapatan_juta']

# Hitung skewness dan kurtosis
skewness_val = skew(pendapatan)
kurtosis_val = kurtosis(pendapatan)  # excess kurtosis (Fisher)

print(f"Skewness: {skewness_val:.4f}")
print(f"  -> {'Right-skewed (ekor kanan lebih panjang)' if skewness_val > 0 else 'Left-skewed' if skewness_val < 0 else 'Simetris'}")

print(f"\nKurtosis (excess): {kurtosis_val:.4f}")
print(f"  -> {'Leptokurtic (lebih runcing)' if kurtosis_val > 0 else 'Platykurtic (lebih datar)' if kurtosis_val < 0 else 'Mesokurtic (normal)'}")

# Visualisasi: bandingkan dengan distribusi normal
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(pendapatan, bins=30, density=True, alpha=0.7, color='steelblue',
        edgecolor='white', label='Data Aktual')

# Overlay distribusi normal
x = np.linspace(pendapatan.min(), pendapatan.max(), 100)
from scipy.stats import norm
mu, sigma = pendapatan.mean(), pendapatan.std()
ax.plot(x, norm.pdf(x, mu, sigma), 'r-', linewidth=2, label='Normal (teoritis)')

ax.set_title(f'Distribusi Pendapatan vs Normal\n(Skew={skewness_val:.2f}, Kurt={kurtosis_val:.2f})', fontsize=13)
ax.set_xlabel('Pendapatan (Juta Rp)')
ax.set_ylabel('Density')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---

> **Catatan:** Data dalam lab ini adalah simulasi. Dalam praktik nyata, data BPS dapat diakses melalui [bps.go.id](https://www.bps.go.id) atau [webapi.bps.go.id](https://webapi.bps.go.id).
