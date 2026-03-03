# Minggu 4: Eksplorasi Data dan Feature Engineering

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 4 |
| **Topik** | Eksplorasi Data dan Feature Engineering |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK-2: Menerapkan teknik eksplorasi data dan feature engineering untuk mempersiapkan dataset berkualitas bagi model ML |
| **Sub-CPMK** | 4.1 Menerapkan teknik EDA untuk memahami karakteristik dan pola dalam dataset |
| | 4.2 Menganalisis dan mengimplementasikan teknik feature engineering untuk meningkatkan kualitas input model ML |
| **Bloom's Taxonomy** | C3-C4 (Menerapkan-Menganalisis / *Applying-Analyzing*) |
| **Durasi** | 2 x 100 menit (Teori 100 min + Praktikum 100 min) |
| **Platform** | Google Colab |
| **Metode** | Ceramah interaktif, live coding, hands-on EDA, diskusi |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menerapkan** teknik Exploratory Data Analysis (EDA) — ringkasan statistik, distribusi, korelasi — untuk memahami dataset secara menyeluruh.
2. **Membuat** visualisasi yang informatif untuk ML: scatter matrix, heatmap korelasi, pair plots, dan distribution plots.
3. **Mengimplementasikan** teknik feature engineering: pembuatan fitur baru, encoding, scaling, dan penanganan outlier.
4. **Menganalisis** kualitas data menggunakan data quality checklist dan menentukan langkah perbaikan yang diperlukan sebelum membangun model ML.

---

## Materi Pembelajaran

### 1. Exploratory Data Analysis (EDA)

#### Apa Itu EDA?

**Exploratory Data Analysis (EDA)** adalah proses investigasi awal terhadap data untuk menemukan pola, anomali, menguji hipotesis, dan memeriksa asumsi menggunakan statistik ringkasan dan visualisasi.

EDA dicetuskan oleh statistikawan **John Tukey** pada tahun 1977 dalam bukunya *"Exploratory Data Analysis"*. Filosofinya:

> "The greatest value of a picture is when it forces us to notice what we never expected to see." — John Tukey

#### Mengapa EDA Penting untuk ML?

```
┌─────────────────────────────────────────────────┐
│             ML Pipeline                          │
│                                                  │
│  Data → [ EDA ] → Preprocessing → Model → Eval  │
│           ▲                                      │
│           │                                      │
│   "Understand your data BEFORE modeling!"        │
└─────────────────────────────────────────────────┘
```

Tanpa EDA, Anda membangun model di atas fondasi yang tidak Anda pahami. EDA membantu menjawab:

- Bagaimana distribusi setiap variabel?
- Apakah ada missing values atau outlier?
- Variabel mana yang berkorelasi?
- Apakah data sudah siap untuk model tertentu?

#### Statistical Summary (Ringkasan Statistik)

```python
# ============================================================
# Minggu 4: EDA & Feature Engineering
# Mata Kuliah: Kecerdasan Buatan dan Machine Learning
# Universitas Al Azhar Indonesia
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style untuk visualisasi
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

# ---- Dataset: Data Properti Indonesia (Simulasi) ----
np.random.seed(42)
n = 200

kota_list = ['Jakarta', 'Bandung', 'Surabaya', 'Yogyakarta',
             'Semarang', 'Medan', 'Makassar', 'Bali']
tipe_list = ['Rumah', 'Apartemen', 'Ruko']

data = {
    'kota': np.random.choice(kota_list, n, p=[0.25, 0.15, 0.15, 0.10,
                                               0.10, 0.10, 0.08, 0.07]),
    'tipe_properti': np.random.choice(tipe_list, n, p=[0.50, 0.35, 0.15]),
    'luas_tanah_m2': np.random.uniform(36, 500, n).round(0),
    'luas_bangunan_m2': np.random.uniform(30, 350, n).round(0),
    'kamar_tidur': np.random.choice([1, 2, 3, 4, 5], n, p=[0.05, 0.20, 0.40, 0.25, 0.10]),
    'kamar_mandi': np.random.choice([1, 2, 3, 4], n, p=[0.15, 0.40, 0.30, 0.15]),
    'tahun_dibangun': np.random.randint(1985, 2025, n),
    'jarak_pusat_kota_km': np.random.uniform(1, 30, n).round(1),
    'sertifikat': np.random.choice(['SHM', 'HGB', 'PPJB'], n, p=[0.50, 0.35, 0.15]),
    'ada_garasi': np.random.choice([0, 1], n, p=[0.35, 0.65])
}

# Harga dipengaruhi oleh beberapa faktor
harga_base = (data['luas_tanah_m2'] * 5 +
              data['luas_bangunan_m2'] * 8 +
              data['kamar_tidur'] * 200 -
              data['jarak_pusat_kota_km'] * 50 +
              data['ada_garasi'] * 300)
# Tambahkan faktor kota
kota_premium = {'Jakarta': 1.8, 'Bali': 1.5, 'Bandung': 1.2,
                'Surabaya': 1.1, 'Semarang': 0.9, 'Yogyakarta': 0.85,
                'Medan': 0.8, 'Makassar': 0.75}
for i in range(n):
    harga_base[i] *= kota_premium[data['kota'][i]]

data['harga_juta'] = (harga_base + np.random.normal(0, 500, n)).round(0)
data['harga_juta'] = np.maximum(data['harga_juta'], 200)  # Harga minimal

# Sisipkan beberapa outlier
data['harga_juta'][np.random.choice(n, 5, replace=False)] = np.random.uniform(10000, 20000, 5).round(0)

# Sisipkan missing values
for col in ['luas_tanah_m2', 'luas_bangunan_m2', 'jarak_pusat_kota_km']:
    idx = np.random.choice(n, int(n * 0.05), replace=False)
    data[col][idx] = np.nan

df = pd.DataFrame(data)

print("=== Dataset Properti Indonesia ===")
print(f"Shape: {df.shape}")
print(df.head(10))
```

```python
# ---- Statistical Summary ----
print("=" * 60)
print("RINGKASAN STATISTIK DATASET")
print("=" * 60)

# Informasi umum
print("\n--- Info Dataset ---")
print(df.info())

# Statistik deskriptif numerik
print("\n--- Statistik Deskriptif (Numerik) ---")
print(df.describe().round(2))

# Statistik deskriptif kategorikal
print("\n--- Statistik Deskriptif (Kategorikal) ---")
print(df.describe(include='object'))

# Missing values
print("\n--- Missing Values ---")
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(1)
print(pd.DataFrame({'Jumlah': missing, 'Persentase (%)': missing_pct})[missing > 0])
```

#### Distribusi Variabel

```python
# ---- Distribusi Variabel Numerik ----
numerik_cols = ['luas_tanah_m2', 'luas_bangunan_m2', 'kamar_tidur',
                'kamar_mandi', 'tahun_dibangun', 'jarak_pusat_kota_km', 'harga_juta']

fig, axes = plt.subplots(3, 3, figsize=(16, 14))
axes = axes.flatten()

for idx, col in enumerate(numerik_cols):
    ax = axes[idx]
    df[col].dropna().hist(bins=25, ax=ax, color='#2196F3', edgecolor='white', alpha=0.8)
    ax.set_title(f'Distribusi: {col}', fontsize=11, fontweight='bold')
    ax.set_xlabel(col)
    ax.set_ylabel('Frekuensi')

    # Tambahkan garis mean dan median
    mean_val = df[col].mean()
    median_val = df[col].median()
    ax.axvline(mean_val, color='red', linestyle='--', label=f'Mean: {mean_val:.1f}')
    ax.axvline(median_val, color='green', linestyle='--', label=f'Median: {median_val:.1f}')
    ax.legend(fontsize=8)

# Hapus subplot kosong
for idx in range(len(numerik_cols), len(axes)):
    fig.delaxes(axes[idx])

plt.suptitle('Distribusi Variabel Numerik — Dataset Properti Indonesia',
             fontsize=14, fontweight='bold', y=1.01)
plt.tight_layout()
plt.show()

print("Insight:")
print("- Jika mean >> median: distribusi right-skewed (ada outlier tinggi)")
print("- Jika mean << median: distribusi left-skewed")
print("- Jika mean ≈ median: distribusi mendekati normal")
```

#### Korelasi Antar Variabel

```python
# ---- Correlation Matrix ----
# Korelasi Pearson: mengukur hubungan linear antar variabel numerik

corr_matrix = df[numerik_cols].corr()

fig, ax = plt.subplots(figsize=(10, 8))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))  # Mask segitiga atas

sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f',
            cmap='RdBu_r', center=0, vmin=-1, vmax=1,
            square=True, linewidths=1, ax=ax)
ax.set_title('Correlation Heatmap — Dataset Properti Indonesia',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Tampilkan korelasi tertinggi dengan harga
print("=== Korelasi dengan Harga ===")
corr_harga = corr_matrix['harga_juta'].drop('harga_juta').sort_values(ascending=False)
print(corr_harga.round(3))
print("\nVariabel dengan korelasi tertinggi terhadap harga:")
print(f"1. {corr_harga.index[0]}: {corr_harga.iloc[0]:.3f}")
print(f"2. {corr_harga.index[1]}: {corr_harga.iloc[1]:.3f}")
```

---

### 2. Visualisasi untuk Machine Learning

#### Scatter Matrix (Pair Plot)

```python
# ---- Pair Plot: Melihat hubungan antar variabel sekaligus ----
# Pilih subset fitur yang paling relevan
fitur_penting = ['luas_tanah_m2', 'luas_bangunan_m2',
                 'jarak_pusat_kota_km', 'harga_juta']

# Hapus rows dengan missing values untuk visualisasi
df_clean = df[fitur_penting].dropna()

g = sns.pairplot(df_clean, diag_kind='hist',
                 plot_kws={'alpha': 0.5, 'color': '#2196F3'},
                 diag_kws={'color': '#2196F3', 'edgecolor': 'white'})
g.fig.suptitle('Scatter Matrix — Fitur Utama Properti Indonesia',
               fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()

print("Insight dari Pair Plot:")
print("- Diagonal: distribusi masing-masing variabel")
print("- Off-diagonal: hubungan antar pasangan variabel")
print("- Cari pola linear, cluster, atau outlier")
```

#### Distribution Plots (Box Plot & Violin Plot)

```python
# ---- Box Plot: Distribusi harga per kota ----
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Box plot
df.boxplot(column='harga_juta', by='kota', ax=axes[0],
           patch_artist=True, boxprops=dict(facecolor='#2196F3', alpha=0.7))
axes[0].set_title('Box Plot: Harga Properti per Kota', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Kota')
axes[0].set_ylabel('Harga (Juta Rp)')
axes[0].tick_params(axis='x', rotation=45)
plt.sca(axes[0])
plt.title('Box Plot: Harga Properti per Kota', fontsize=12, fontweight='bold')

# Violin plot
sns.violinplot(data=df, x='tipe_properti', y='harga_juta',
               palette='Set2', ax=axes[1])
axes[1].set_title('Violin Plot: Harga per Tipe Properti', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Tipe Properti')
axes[1].set_ylabel('Harga (Juta Rp)')

plt.tight_layout()
plt.show()

print("Box Plot menunjukkan:")
print("- Kotak: Q1 (25%) sampai Q3 (75%)")
print("- Garis di kotak: Median")
print("- Whiskers: 1.5 * IQR dari Q1 dan Q3")
print("- Titik di luar whiskers: Outlier")
```

#### Distribusi Kategorikal

```python
# ---- Distribusi variabel kategorikal ----
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Distribusi kota
df['kota'].value_counts().plot(kind='bar', ax=axes[0], color='#2196F3',
                                edgecolor='white')
axes[0].set_title('Distribusi Properti per Kota', fontweight='bold')
axes[0].set_ylabel('Jumlah')
axes[0].tick_params(axis='x', rotation=45)

# Distribusi tipe properti
df['tipe_properti'].value_counts().plot(kind='pie', ax=axes[1],
                                         autopct='%1.1f%%',
                                         colors=['#2196F3', '#4CAF50', '#FF9800'])
axes[1].set_title('Distribusi Tipe Properti', fontweight='bold')
axes[1].set_ylabel('')

# Distribusi sertifikat
df['sertifikat'].value_counts().plot(kind='bar', ax=axes[2], color='#4CAF50',
                                      edgecolor='white')
axes[2].set_title('Distribusi Sertifikat', fontweight='bold')
axes[2].set_ylabel('Jumlah')

plt.suptitle('Distribusi Variabel Kategorikal — Dataset Properti Indonesia',
             fontsize=14, fontweight='bold', y=1.03)
plt.tight_layout()
plt.show()
```

---

### 3. Feature Engineering

Feature engineering adalah **seni dan ilmu** menciptakan fitur-fitur baru dari data yang ada untuk meningkatkan performa model ML. Ini sering kali menjadi perbedaan antara model yang biasa-biasa saja dan model yang sangat baik.

> "Coming up with features is difficult, time-consuming, requires expert knowledge. Applied machine learning is basically feature engineering." — Andrew Ng

#### a) Feature Creation (Pembuatan Fitur Baru)

```python
# ---- Membuat fitur baru dari fitur yang ada ----
df_fe = df.copy()

# Fitur 1: Rasio luas bangunan terhadap luas tanah
df_fe['rasio_bangunan_tanah'] = df_fe['luas_bangunan_m2'] / df_fe['luas_tanah_m2']
print("Fitur baru: rasio_bangunan_tanah")
print(df_fe['rasio_bangunan_tanah'].describe().round(2))
print()

# Fitur 2: Usia bangunan
df_fe['usia_bangunan'] = 2026 - df_fe['tahun_dibangun']
print("Fitur baru: usia_bangunan (tahun)")
print(df_fe['usia_bangunan'].describe().round(2))
print()

# Fitur 3: Total kamar
df_fe['total_kamar'] = df_fe['kamar_tidur'] + df_fe['kamar_mandi']
print("Fitur baru: total_kamar")
print(df_fe['total_kamar'].value_counts().sort_index())
print()

# Fitur 4: Harga per m2 (fitur target engineering)
df_fe['harga_per_m2'] = df_fe['harga_juta'] / df_fe['luas_bangunan_m2']
print("Fitur baru: harga_per_m2 (juta/m2)")
print(df_fe['harga_per_m2'].describe().round(2))
```

#### Polynomial Features (Fitur Polinomial)

```python
from sklearn.preprocessing import PolynomialFeatures

# Fitur polinomial: menangkap hubungan non-linear
# Dari [x1, x2] menjadi [1, x1, x2, x1^2, x1*x2, x2^2]

fitur_asli = df_fe[['luas_tanah_m2', 'luas_bangunan_m2']].dropna()

poly = PolynomialFeatures(degree=2, include_bias=False, interaction_only=False)
fitur_poly = poly.fit_transform(fitur_asli)

print("=== Polynomial Features ===")
print(f"Fitur asli : {fitur_asli.shape[1]} kolom ({list(fitur_asli.columns)})")
print(f"Setelah poly: {fitur_poly.shape[1]} kolom")
print(f"Nama fitur : {poly.get_feature_names_out()}")
print()

# Interaction features saja
poly_interact = PolynomialFeatures(degree=2, include_bias=False, interaction_only=True)
fitur_interact = poly_interact.fit_transform(fitur_asli)
print(f"Interaction only: {fitur_interact.shape[1]} kolom")
print(f"Nama fitur : {poly_interact.get_feature_names_out()}")
```

#### b) Feature Encoding Strategies (Lanjutan)

```python
# ---- Encoding strategies yang lebih advanced ----

# 1. Ordinal Encoding dengan mapping kustom
mapping_sertifikat = {'PPJB': 0, 'HGB': 1, 'SHM': 2}
df_fe['sertifikat_encoded'] = df_fe['sertifikat'].map(mapping_sertifikat)
print("=== Ordinal Encoding: Sertifikat ===")
print(f"Mapping: {mapping_sertifikat}")
print(df_fe['sertifikat_encoded'].value_counts().sort_index())

# 2. Target Encoding (Mean Encoding)
# Encode kategori berdasarkan rata-rata target (harga)
target_encoding_kota = df_fe.groupby('kota')['harga_juta'].mean()
df_fe['kota_target_encoded'] = df_fe['kota'].map(target_encoding_kota)

print("\n=== Target Encoding: Kota ===")
print(target_encoding_kota.sort_values(ascending=False).round(0))

# 3. Frequency Encoding
# Encode berdasarkan frekuensi kemunculan
freq_encoding_kota = df_fe['kota'].value_counts(normalize=True)
df_fe['kota_freq_encoded'] = df_fe['kota'].map(freq_encoding_kota)

print("\n=== Frequency Encoding: Kota ===")
print(freq_encoding_kota.round(3))
```

#### c) Feature Scaling Revisited

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Perbandingan tiga scaler
fitur_scale = df_fe[['luas_tanah_m2', 'harga_juta']].dropna()

fig, axes = plt.subplots(1, 4, figsize=(20, 4))

# Original
axes[0].hist(fitur_scale['harga_juta'], bins=25, color='#2196F3', edgecolor='white')
axes[0].set_title('Original\n(Tanpa Scaling)', fontweight='bold')

# StandardScaler
scaler_std = StandardScaler()
scaled_std = scaler_std.fit_transform(fitur_scale)
axes[1].hist(scaled_std[:, 1], bins=25, color='#4CAF50', edgecolor='white')
axes[1].set_title('StandardScaler\n(mean=0, std=1)', fontweight='bold')

# MinMaxScaler
scaler_mm = MinMaxScaler()
scaled_mm = scaler_mm.fit_transform(fitur_scale)
axes[2].hist(scaled_mm[:, 1], bins=25, color='#FF9800', edgecolor='white')
axes[2].set_title('MinMaxScaler\n(range [0,1])', fontweight='bold')

# RobustScaler (tahan terhadap outlier)
scaler_rb = RobustScaler()
scaled_rb = scaler_rb.fit_transform(fitur_scale)
axes[3].hist(scaled_rb[:, 1], bins=25, color='#E91E63', edgecolor='white')
axes[3].set_title('RobustScaler\n(median & IQR, tahan outlier)', fontweight='bold')

plt.suptitle('Perbandingan Feature Scaling Methods — Kolom Harga',
             fontsize=14, fontweight='bold', y=1.05)
plt.tight_layout()
plt.show()

print("Kapan menggunakan scaler mana?")
print("- StandardScaler : Data mendekati normal, tanpa outlier ekstrem")
print("- MinMaxScaler   : Butuh rentang tertentu [0,1], untuk Neural Networks")
print("- RobustScaler   : Data memiliki banyak outlier")
```

#### d) Handling Outliers (Penanganan Outlier)

Outlier adalah data yang sangat berbeda dari mayoritas data. Mereka bisa berupa:
- **Outlier yang valid** — data nyata tapi ekstrem (misalnya villa mewah di Bali)
- **Outlier yang salah** — error pengumpulan data

```python
# ---- Deteksi Outlier ----

# Metode 1: IQR (Interquartile Range)
def detect_outliers_iqr(data, column):
    """Deteksi outlier menggunakan metode IQR"""
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers, lower_bound, upper_bound

outliers_iqr, lower, upper = detect_outliers_iqr(df, 'harga_juta')
print("=== Deteksi Outlier (IQR Method) — Harga ===")
print(f"Q1 = {df['harga_juta'].quantile(0.25):.0f}")
print(f"Q3 = {df['harga_juta'].quantile(0.75):.0f}")
print(f"IQR = {df['harga_juta'].quantile(0.75) - df['harga_juta'].quantile(0.25):.0f}")
print(f"Lower bound: {lower:.0f}")
print(f"Upper bound: {upper:.0f}")
print(f"Jumlah outlier: {len(outliers_iqr)}")
```

```python
# Metode 2: Z-Score
from scipy import stats

def detect_outliers_zscore(data, column, threshold=3):
    """Deteksi outlier menggunakan Z-score"""
    z_scores = np.abs(stats.zscore(data[column].dropna()))
    outlier_mask = z_scores > threshold
    return data[column].dropna()[outlier_mask], z_scores

outliers_z, z_scores = detect_outliers_zscore(df, 'harga_juta')
print(f"\n=== Deteksi Outlier (Z-Score Method, threshold=3) — Harga ===")
print(f"Jumlah outlier: {len(outliers_z)}")
print(f"Nilai outlier:\n{outliers_z}")
```

```python
# ---- Penanganan Outlier ----

# Strategi 1: Capping (Winsorization)
# Batasi nilai ke batas atas/bawah
df_capped = df.copy()
Q1 = df_capped['harga_juta'].quantile(0.05)
Q3 = df_capped['harga_juta'].quantile(0.95)
df_capped['harga_juta'] = df_capped['harga_juta'].clip(lower=Q1, upper=Q3)

print("=== Penanganan Outlier: Capping (Percentile 5-95) ===")
print(f"Sebelum: min={df['harga_juta'].min():.0f}, max={df['harga_juta'].max():.0f}")
print(f"Setelah: min={df_capped['harga_juta'].min():.0f}, max={df_capped['harga_juta'].max():.0f}")

# Strategi 2: Log transformation (untuk distribusi right-skewed)
df_fe['harga_log'] = np.log1p(df_fe['harga_juta'])

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
df_fe['harga_juta'].hist(bins=30, ax=axes[0], color='#2196F3', edgecolor='white')
axes[0].set_title('Harga Asli\n(Right-skewed)', fontweight='bold')
axes[0].set_xlabel('Harga (Juta Rp)')

df_fe['harga_log'].hist(bins=30, ax=axes[1], color='#4CAF50', edgecolor='white')
axes[1].set_title('Harga (Log Transform)\n(Lebih mendekati normal)', fontweight='bold')
axes[1].set_xlabel('Log(Harga)')

plt.suptitle('Efek Log Transformation pada Distribusi Harga',
             fontsize=14, fontweight='bold', y=1.03)
plt.tight_layout()
plt.show()

print("Log transformation membantu:")
print("- Mengurangi pengaruh outlier")
print("- Membuat distribusi lebih mendekati normal")
print("- Cocok untuk harga, pendapatan, jumlah populasi")
```

---

### 4. Data Quality Checklist untuk ML

Sebelum membangun model ML, pastikan data Anda melewati checklist kualitas berikut:

```python
# ============================================================
# Data Quality Checklist
# ============================================================

def data_quality_check(df, target_col=None):
    """
    Melakukan pengecekan kualitas data secara komprehensif.
    Mengembalikan laporan kualitas data.
    """
    print("=" * 60)
    print("DATA QUALITY CHECKLIST")
    print("=" * 60)

    # 1. Shape dan tipe data
    print(f"\n[1] SHAPE: {df.shape[0]} baris, {df.shape[1]} kolom")

    # 2. Missing values
    missing = df.isnull().sum()
    missing_pct = (missing / len(df) * 100)
    has_missing = missing[missing > 0]
    if len(has_missing) > 0:
        print(f"\n[2] MISSING VALUES: {len(has_missing)} kolom memiliki missing values")
        for col in has_missing.index:
            status = "WARNING" if missing_pct[col] > 5 else "OK"
            print(f"    [{status}] {col}: {has_missing[col]} ({missing_pct[col]:.1f}%)")
    else:
        print(f"\n[2] MISSING VALUES: Tidak ada! [OK]")

    # 3. Duplicates
    n_dupes = df.duplicated().sum()
    print(f"\n[3] DUPLIKAT: {n_dupes} baris duplikat {'[WARNING]' if n_dupes > 0 else '[OK]'}")

    # 4. Data types
    print(f"\n[4] TIPE DATA:")
    for col in df.columns:
        print(f"    {col}: {df[col].dtype}")

    # 5. Statistik dasar
    print(f"\n[5] STATISTIK NUMERIK:")
    numerik = df.select_dtypes(include=[np.number])
    for col in numerik.columns:
        skew = numerik[col].skew()
        skew_status = "NORMAL" if abs(skew) < 1 else ("SKEWED" if abs(skew) < 2 else "VERY SKEWED")
        print(f"    {col}: min={numerik[col].min():.1f}, max={numerik[col].max():.1f}, "
              f"skew={skew:.2f} [{skew_status}]")

    # 6. Kardinalitas kategorikal
    print(f"\n[6] KARDINALITAS KATEGORIKAL:")
    kategori = df.select_dtypes(include=['object'])
    for col in kategori.columns:
        n_unique = kategori[col].nunique()
        status = "OK" if n_unique < 20 else ("HIGH" if n_unique < 50 else "VERY HIGH")
        print(f"    {col}: {n_unique} kategori unik [{status}]")

    # 7. Target variable
    if target_col and target_col in df.columns:
        print(f"\n[7] TARGET VARIABLE ({target_col}):")
        if df[target_col].dtype in ['object', 'category']:
            print(f"    Tipe: Klasifikasi")
            print(f"    Distribusi kelas:\n{df[target_col].value_counts()}")
            # Check class imbalance
            counts = df[target_col].value_counts()
            ratio = counts.min() / counts.max()
            print(f"    Rasio min/max: {ratio:.2f} {'[IMBALANCED]' if ratio < 0.5 else '[OK]'}")
        else:
            print(f"    Tipe: Regresi")
            print(f"    Range: {df[target_col].min():.1f} - {df[target_col].max():.1f}")

    print("\n" + "=" * 60)
    print("CHECKLIST SELESAI")
    print("=" * 60)

# Jalankan checklist
data_quality_check(df, target_col='harga_juta')
```

#### Ringkasan Data Quality Checklist

| No | Aspek | Pertanyaan Kunci | Tindakan |
|---|---|---|---|
| 1 | **Shape** | Berapa banyak baris dan kolom? | Pastikan cukup untuk model |
| 2 | **Missing Values** | Ada kolom dengan > 5% missing? | Impute atau hapus |
| 3 | **Duplikat** | Ada baris duplikat? | Hapus duplikat |
| 4 | **Tipe Data** | Apakah tipe data sudah benar? | Konversi jika perlu |
| 5 | **Distribusi** | Ada distribusi yang sangat skewed? | Log transform atau capping |
| 6 | **Outlier** | Ada outlier yang perlu ditangani? | IQR, z-score, capping |
| 7 | **Kardinalitas** | Ada kategori dengan terlalu banyak nilai unik? | Feature hashing atau target encoding |
| 8 | **Korelasi** | Ada fitur yang sangat berkorelasi? | Pertimbangkan untuk menghapus salah satu |
| 9 | **Class Imbalance** | Distribusi target seimbang? | Oversampling, undersampling, atau SMOTE |
| 10 | **Leakage** | Ada fitur yang "bocor" informasi dari target? | Hapus fitur tersebut |

---

## Aktivitas Kelas

### Sesi 1: Teori dan Demonstrasi (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 5 menit | Pembukaan & Review | Review Minggu 3 (matematika ML), preview hari ini |
| 25 menit | Ceramah: EDA | Statistical summary, distribusi, korelasi, pentingnya EDA |
| 20 menit | Live Demo: Visualisasi | Scatter matrix, heatmap, box plot, violin plot |
| 25 menit | Ceramah: Feature Engineering | Feature creation, encoding, scaling revisited, outlier handling |
| 15 menit | Ceramah: Data Quality Checklist | 10 aspek kualitas data, contoh checklist |
| 5 menit | Diskusi & Tanya Jawab | Pertanyaan tentang strategi EDA dan feature engineering |
| 5 menit | Transisi ke Praktikum | Persiapan hands-on |

### Sesi 2: Hands-on Praktikum (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Setup Notebook | Buka Google Colab, load dataset |
| 30 menit | EDA Lengkap | Implementasi statistical summary, distribusi, korelasi |
| 25 menit | Feature Engineering | Membuat fitur baru, encoding, scaling, outlier handling |
| 15 menit | Data Quality Checklist | Menjalankan dan menginterpretasi checklist |
| 10 menit | Eksplorasi Mandiri | Mahasiswa mencoba dengan dataset berbeda |
| 5 menit | Diskusi Hasil & Wrap-up | Sharing insight, Q&A |
| 5 menit | Tugas & Pengumuman Kuis | Penjelasan Tugas T2 dan pengumuman K1 |

---

## Hands-on: Full EDA Pipeline pada Dataset Indonesia

### EDA Ringkas: Template yang Bisa Digunakan Ulang

```python
# ============================================================
# Template EDA Pipeline — Siap Pakai
# ============================================================

def eda_pipeline(df, target_col=None, figsize=(16, 12)):
    """
    Pipeline EDA otomatis untuk dataset apapun.
    Menghasilkan ringkasan statistik dan visualisasi.
    """
    print("=" * 70)
    print("EXPLORATORY DATA ANALYSIS (EDA) PIPELINE")
    print("=" * 70)

    # 1. Overview
    print(f"\n{'='*30} OVERVIEW {'='*30}")
    print(f"Shape: {df.shape}")
    print(f"Kolom: {list(df.columns)}")
    print(f"\nTipe data:\n{df.dtypes}")
    print(f"\nMissing values:\n{df.isnull().sum()[df.isnull().sum() > 0]}")

    # 2. Statistik deskriptif
    print(f"\n{'='*30} STATISTIK {'='*30}")
    print(df.describe().round(2))

    # 3. Visualisasi
    numerik_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    kategori_cols = df.select_dtypes(include=['object']).columns.tolist()

    # 3a. Distribusi numerik
    if len(numerik_cols) > 0:
        n_cols = min(3, len(numerik_cols))
        n_rows = (len(numerik_cols) + n_cols - 1) // n_cols
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(5*n_cols, 4*n_rows))
        if n_rows * n_cols == 1:
            axes = np.array([axes])
        axes = axes.flatten()

        for idx, col in enumerate(numerik_cols):
            if idx < len(axes):
                df[col].dropna().hist(bins=25, ax=axes[idx],
                                       color='#2196F3', edgecolor='white')
                axes[idx].set_title(f'{col}', fontweight='bold')
                axes[idx].axvline(df[col].mean(), color='red',
                                   linestyle='--', label='Mean')
                axes[idx].legend(fontsize=8)

        for idx in range(len(numerik_cols), len(axes)):
            fig.delaxes(axes[idx])

        plt.suptitle('Distribusi Variabel Numerik', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()

    # 3b. Correlation heatmap
    if len(numerik_cols) > 1:
        fig, ax = plt.subplots(figsize=(10, 8))
        corr = df[numerik_cols].corr()
        mask = np.triu(np.ones_like(corr, dtype=bool))
        sns.heatmap(corr, mask=mask, annot=True, fmt='.2f',
                    cmap='RdBu_r', center=0, ax=ax, square=True)
        ax.set_title('Correlation Heatmap', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()

    # 3c. Korelasi dengan target
    if target_col and target_col in numerik_cols:
        print(f"\n{'='*30} KORELASI DENGAN {target_col.upper()} {'='*30}")
        corr_target = df[numerik_cols].corr()[target_col].drop(target_col)
        print(corr_target.sort_values(ascending=False).round(3))

    print(f"\n{'='*30} EDA SELESAI {'='*30}")

# Jalankan EDA pipeline
eda_pipeline(df, target_col='harga_juta')
```

### Fitur Baru untuk Dataset Properti

```python
# ---- Implementasi Feature Engineering Lengkap ----

# Pastikan missing values sudah di-handle
from sklearn.impute import SimpleImputer

df_final = df.copy()

# Handle missing values
imputer = SimpleImputer(strategy='median')
cols_with_missing = ['luas_tanah_m2', 'luas_bangunan_m2', 'jarak_pusat_kota_km']
df_final[cols_with_missing] = imputer.fit_transform(df_final[cols_with_missing])

# Feature Engineering
df_final['rasio_bangunan_tanah'] = df_final['luas_bangunan_m2'] / df_final['luas_tanah_m2']
df_final['usia_bangunan'] = 2026 - df_final['tahun_dibangun']
df_final['total_kamar'] = df_final['kamar_tidur'] + df_final['kamar_mandi']
df_final['harga_log'] = np.log1p(df_final['harga_juta'])

# Encoding
mapping_sertifikat = {'PPJB': 0, 'HGB': 1, 'SHM': 2}
df_final['sertifikat_encoded'] = df_final['sertifikat'].map(mapping_sertifikat)

# Target encoding untuk kota
target_enc_kota = df_final.groupby('kota')['harga_juta'].mean()
df_final['kota_encoded'] = df_final['kota'].map(target_enc_kota)

# One-Hot Encoding untuk tipe properti
df_final = pd.get_dummies(df_final, columns=['tipe_properti'],
                           prefix='tipe', drop_first=True)

print("=== Dataset Setelah Feature Engineering ===")
print(f"Shape: {df_final.shape}")
print(f"Kolom: {list(df_final.columns)}")
print(df_final.head())
```

```python
# ---- Korelasi fitur baru dengan target ----
fitur_baru = ['rasio_bangunan_tanah', 'usia_bangunan', 'total_kamar',
              'sertifikat_encoded', 'kota_encoded']
fitur_asli = ['luas_tanah_m2', 'luas_bangunan_m2', 'kamar_tidur',
              'jarak_pusat_kota_km']

semua_fitur = fitur_asli + fitur_baru
corr_comparison = df_final[semua_fitur + ['harga_juta']].corr()['harga_juta'].drop('harga_juta')

print("=== Korelasi dengan Harga: Fitur Asli vs Fitur Baru ===")
print(corr_comparison.sort_values(ascending=False).round(3))
print("\nApakah fitur baru meningkatkan korelasi?")
```

---

## AI Corner: Menggunakan AI untuk Saran EDA

> **Level: Basic-Intermediate** — Mulai menggunakan AI untuk mendapatkan insight dari data.

### Cara AI Bisa Membantu EDA

| Skenario | Contoh Prompt ke AI |
|---|---|
| Memilih visualisasi | *"Saya punya dataset properti dengan 10 kolom (5 numerik, 5 kategorikal). Visualisasi apa yang paling informatif untuk EDA?"* |
| Interpretasi korelasi | *"Korelasi antara luas_tanah dan harga = 0.72. Apa artinya? Apakah ini cukup kuat untuk ML?"* |
| Feature engineering ideas | *"Dataset saya tentang properti Indonesia memiliki kolom: [daftar kolom]. Fitur baru apa yang bisa saya buat?"* |
| Outlier handling | *"Harga properti saya memiliki outlier (beberapa rumah mewah). Bagaimana cara terbaik menanganinya untuk regresi?"* |
| Interpretasi distribusi | *"Distribusi harga properti saya sangat right-skewed. Apa implikasinya untuk model ML?"* |

### Tips Penting

1. **Berikan konteks** — jelaskan domain data Anda agar AI memberikan saran yang relevan.
2. **Minta penjelasan** — tanyakan "mengapa" di balik setiap saran.
3. **Jangan langsung percaya** — verifikasi saran AI dengan eksplorasi data Anda sendiri.
4. **Iterasi** — EDA adalah proses iteratif. Gunakan AI untuk brainstorming, lalu validasi.

### Contoh Prompt Minggu Ini

```
Saya sedang melakukan EDA pada dataset properti Indonesia dengan kolom:
kota, tipe_properti, luas_tanah_m2, luas_bangunan_m2, kamar_tidur,
kamar_mandi, tahun_dibangun, jarak_pusat_kota_km, sertifikat,
ada_garasi, harga_juta.

Target saya adalah memprediksi harga_juta.

1. Fitur baru apa yang sebaiknya saya buat dari kolom-kolom ini?
2. Visualisasi apa yang paling penting untuk memahami hubungan
   fitur dengan harga?
3. Bagaimana cara menangani distribusi harga yang right-skewed?
4. Apakah ada potensi data leakage yang harus saya waspadai?
```

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai bahan refleksi:

1. **EDA dan Intuisi:** Mengapa EDA penting dilakukan sebelum membangun model ML? Apa risiko jika kita langsung memasukkan data ke model tanpa EDA terlebih dahulu?

2. **Feature Engineering Creativity:** Dataset Anda memiliki kolom tanggal_transaksi. Fitur baru apa saja yang bisa Anda ekstrak dari kolom tanggal? (Hint: pikirkan tentang hari, bulan, musim, hari libur, dll.)

3. **Outlier Dilemma:** Anda menemukan bahwa 3% data harga properti adalah outlier (rumah mewah seharga > 10 miliar). Apakah Anda akan menghapusnya, men-cap-nya, atau membiarkannya? Apa pertimbangan Anda?

4. **Korelasi vs Kausalitas:** Anda menemukan korelasi tinggi (r = 0.85) antara jumlah kamar dan harga properti. Apakah ini berarti menambah kamar akan meningkatkan harga? Jelaskan perbedaan korelasi dan kausalitas.

5. **Etika dalam Data:** Dalam dataset properti, apakah ada variabel yang berpotensi menyebabkan bias atau diskriminasi jika digunakan dalam model ML? (Misalnya: lokasi yang berkaitan dengan etnis tertentu.) Bagaimana Anda menanganinya sesuai prinsip keadilan (*Al-'Adl*)?

---

## Tugas Mandiri Minggu 4 — Tugas T2: EDA & Feature Visualization

### Deskripsi Tugas

Lakukan **EDA lengkap dan feature engineering** pada dataset yang diberikan atau dipilih (dengan persetujuan dosen).

### Instruksi

1. **Pilih dataset** konteks Indonesia (misalnya data e-commerce, pendidikan, kesehatan, transportasi, atau properti).

2. **EDA Lengkap:**
   - Statistical summary (`.info()`, `.describe()`, `.isnull()`)
   - Distribusi setiap variabel (histogram atau density plot)
   - Korelasi antar variabel (correlation heatmap)
   - Minimal 5 visualisasi yang informatif (scatter, box, violin, pair plot, dll.)

3. **Feature Engineering:**
   - Buat minimal 3 fitur baru yang relevan
   - Terapkan encoding yang tepat untuk variabel kategorikal
   - Handle outlier dengan metode yang sesuai
   - Jelaskan alasan untuk setiap keputusan

4. **Data Quality Report:**
   - Jalankan data quality checklist
   - Tuliskan temuan dan rekomendasi

5. **Insight:**
   - Tuliskan minimal 5 insight yang Anda temukan dari EDA
   - Sertakan visualisasi pendukung untuk setiap insight

### Kriteria Penilaian

| Kriteria | Bobot |
|---|---|
| Kelengkapan EDA (statistik + visualisasi) | 25% |
| Kualitas dan kreativitas feature engineering | 25% |
| Interpretasi dan insight | 25% |
| Kualitas kode dan dokumentasi | 15% |
| Estetika visualisasi | 10% |

### Pengumpulan

- Format: Google Colab notebook (.ipynb) melalui LMS
- Deadline: Satu hari sebelum pertemuan Minggu 5
- **Wajib:** Sertakan AI Usage Log jika menggunakan AI

---

## Pengumuman: Kuis K1

> **Kuis K1: Fondasi AI & Data Preparation** akan dilaksanakan pada **Minggu 5**.

### Cakupan Materi

| Minggu | Topik |
|---|---|
| Minggu 1 | Pengantar AI — Sejarah, filosofi, jenis AI, ML pipeline |
| Minggu 2 | Python untuk AI/ML — NumPy, Pandas, preprocessing |
| Minggu 3 | Matematika untuk ML — Aljabar linear, probabilitas, gradient descent |
| Minggu 4 | EDA & Feature Engineering — Distribusi, korelasi, outlier |

### Format Kuis

- **Durasi:** 30 menit
- **Tipe soal:** Pilihan ganda + isian singkat + kode pendek
- **Open/Closed:** Closed-book, **AI TIDAK diizinkan**
- **Platform:** LMS atau kertas

### Tips Persiapan

1. Review semua materi Minggu 1-4
2. Pastikan memahami konsep, bukan hanya menghafal kode
3. Latihan soal di akhir setiap modul
4. Pahami "mengapa" di balik setiap teknik preprocessing dan EDA

---

## Referensi

### Buku Teks

1. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media. Chapter 2: End-to-End Machine Learning Project.
2. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media. Chapter 9-10.
3. Zheng, A., & Casari, A. (2018). *Feature Engineering for Machine Learning*. O'Reilly Media.

### Sumber Online

4. [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html) — Galeri visualisasi seaborn.
5. [Kaggle: EDA Guide](https://www.kaggle.com/learn/data-visualization) — Tutorial EDA interaktif.
6. [scikit-learn Feature Engineering](https://scikit-learn.org/stable/modules/preprocessing.html) — Dokumentasi resmi preprocessing.

### Dataset Indonesia

7. [Open Data Jakarta](https://data.jakarta.go.id/) — Data terbuka DKI Jakarta.
8. [BPS Indonesia](https://www.bps.go.id/) — Badan Pusat Statistik Indonesia.
9. [Kaggle: Indonesian Datasets](https://www.kaggle.com/search?q=indonesia) — Dataset Indonesia di Kaggle.

---

> **Preview Minggu Depan:** Kita akan mulai membangun model ML pertama kita! Topik: **Regresi Linear dan Polynomial** — memahami model prediktif paling dasar, implementasi dengan scikit-learn, dan evaluasi model. Jangan lupa persiapkan Kuis K1!

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
