# BAB 4: EKSPLORASI DATA DAN FEATURE ENGINEERING

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-4.1 | Menerapkan teknik Exploratory Data Analysis (EDA) untuk memahami karakteristik dataset sebelum modeling | C3 |
| CPMK-4.2 | Menganalisis dan merancang fitur-fitur baru (feature engineering) untuk meningkatkan performa model ML | C4 |

---

## Estimasi Waktu

| Aktivitas | Durasi |
|-----------|--------|
| Membaca materi | 90 menit |
| Praktik kode Python (EDA & visualisasi) | 120 menit |
| Mengerjakan latihan soal | 60 menit |
| Eksplorasi AI Corner | 30 menit |
| **Total** | **5 jam** |

---

## Prasyarat

- Bab 1: Pengantar Kecerdasan Buatan
- Bab 2: Python untuk AI dan Machine Learning (NumPy, Pandas, preprocessing)
- Bab 3: Matematika untuk Machine Learning (statistik deskriptif, korelasi)

---

## 4.1 Exploratory Data Analysis (EDA)

### 4.1.1 Apa itu EDA?

**Exploratory Data Analysis (EDA)** adalah proses investigasi awal terhadap data untuk menemukan pola, anomali, dan insight — sebelum membangun model ML.

> "The greatest value of a picture is when it forces us to notice what we never expected to see."
> — John Tukey, pencipta konsep EDA

```
POSISI EDA DALAM ML PIPELINE
═══════════════════════════════════════════════════
Data Collection → [EDA] → Preprocessing → Modeling → Evaluation
                    │
                    ├── Memahami distribusi data
                    ├── Menemukan missing values & outlier
                    ├── Melihat korelasi antar fitur
                    ├── Menentukan strategi preprocessing
                    └── Mengidentifikasi fitur yang informatif
═══════════════════════════════════════════════════
```

### 4.1.2 Statistik Deskriptif untuk ML

Langkah pertama EDA: **kenali data Anda secara numerik**.

```python
import pandas as pd
import numpy as np

# Dataset: Data karyawan perusahaan teknologi Indonesia
np.random.seed(42)
n = 200

data_karyawan = pd.DataFrame({
    'usia': np.random.normal(30, 5, n).astype(int).clip(22, 55),
    'pengalaman_tahun': np.random.exponential(4, n).round(1).clip(0, 25),
    'gaji_juta': np.random.normal(12, 5, n).round(1).clip(4, 50),
    'jam_lembur_per_minggu': np.random.poisson(3, n),
    'jarak_kantor_km': np.random.exponential(15, n).round(1).clip(1, 80),
    'kepuasan_kerja': np.random.choice([1, 2, 3, 4, 5], n, p=[0.05, 0.10, 0.25, 0.35, 0.25]),
    'departemen': np.random.choice(
        ['Engineering', 'Data Science', 'Product', 'Marketing', 'HR'],
        n, p=[0.35, 0.25, 0.20, 0.12, 0.08]
    ),
    'pendidikan': np.random.choice(
        ['S1', 'S2', 'S3', 'D3'],
        n, p=[0.55, 0.30, 0.05, 0.10]
    ),
    'status_resign': np.random.choice([0, 1], n, p=[0.82, 0.18])
})

# Tambahkan noise: beberapa missing values
mask_gaji = np.random.choice(n, 15, replace=False)
mask_kepuasan = np.random.choice(n, 10, replace=False)
data_karyawan.loc[mask_gaji, 'gaji_juta'] = np.nan
data_karyawan.loc[mask_kepuasan, 'kepuasan_kerja'] = np.nan

# === EDA LANGKAH 1: Overview ===
print("=== OVERVIEW DATASET ===")
print(f"Shape: {data_karyawan.shape}")
print(f"Kolom: {list(data_karyawan.columns)}")
print(f"\n{data_karyawan.head()}")

print(f"\n=== INFO ===")
print(data_karyawan.info())

print(f"\n=== MISSING VALUES ===")
missing = data_karyawan.isnull().sum()
missing_pct = (data_karyawan.isnull().mean() * 100).round(1)
print(pd.DataFrame({'Jumlah Missing': missing, 'Persentase (%)': missing_pct}))

# === EDA LANGKAH 2: Statistik Deskriptif ===
print(f"\n=== STATISTIK DESKRIPTIF (NUMERIK) ===")
print(data_karyawan.describe().round(2))

print(f"\n=== STATISTIK DESKRIPTIF (KATEGORIKAL) ===")
for col in ['departemen', 'pendidikan']:
    print(f"\n{col}:")
    print(data_karyawan[col].value_counts())
```

### 4.1.3 Analisis Distribusi

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Menggunakan dataset data_karyawan dari kode sebelumnya

# === ANALISIS DISTRIBUSI FITUR NUMERIK ===
fitur_numerik = ['usia', 'pengalaman_tahun', 'gaji_juta', 'jam_lembur_per_minggu', 'jarak_kantor_km']

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()

for i, col in enumerate(fitur_numerik):
    data_clean = data_karyawan[col].dropna()

    # Histogram + KDE
    axes[i].hist(data_clean, bins=25, density=True, alpha=0.6, color='steelblue', edgecolor='white')
    data_clean.plot.kde(ax=axes[i], color='red', linewidth=2)

    # Statistik pada plot
    mean_val = data_clean.mean()
    median_val = data_clean.median()
    axes[i].axvline(mean_val, color='green', linestyle='--', label=f'Mean: {mean_val:.1f}')
    axes[i].axvline(median_val, color='orange', linestyle='--', label=f'Median: {median_val:.1f}')

    axes[i].set_title(f'Distribusi {col}', fontsize=11)
    axes[i].legend(fontsize=8)
    axes[i].grid(True, alpha=0.3)

# Hapus subplot kosong
axes[-1].set_visible(False)

plt.suptitle('Analisis Distribusi Fitur Numerik', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('distribusi_fitur.png', dpi=150, bbox_inches='tight')
plt.show()

# Skewness (kemencengan)
print("=== SKEWNESS ===")
for col in fitur_numerik:
    skew = data_karyawan[col].skew()
    tipe = "simetris" if abs(skew) < 0.5 else ("right-skewed" if skew > 0 else "left-skewed")
    print(f"{col:30s}: skewness = {skew:+.3f} ({tipe})")
```

**Interpretasi Skewness:**

| Skewness | Interpretasi | Tindakan |
|----------|-------------|----------|
| -0.5 < skew < 0.5 | Mendekati simetris | Tidak perlu transformasi |
| 0.5 < skew < 1.0 | Moderately right-skewed | Pertimbangkan log transform |
| skew > 1.0 | Highly right-skewed | Log transform atau sqrt |
| skew < -1.0 | Highly left-skewed | Square transform |

### 4.1.4 Analisis Korelasi

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Menggunakan dataset data_karyawan

# === MATRIKS KORELASI ===
# Hanya kolom numerik
kolom_num = ['usia', 'pengalaman_tahun', 'gaji_juta', 'jam_lembur_per_minggu',
             'jarak_kantor_km', 'kepuasan_kerja', 'status_resign']

corr_matrix = data_karyawan[kolom_num].corr()

print("=== MATRIKS KORELASI ===")
print(corr_matrix.round(3))

# Korelasi dengan target (status_resign)
print(f"\n=== KORELASI DENGAN TARGET (status_resign) ===")
target_corr = corr_matrix['status_resign'].drop('status_resign').sort_values(ascending=False)
print(target_corr.round(3))

# Identifikasi korelasi kuat antar fitur (multicollinearity)
print(f"\n=== PASANGAN FITUR DENGAN KORELASI TINGGI (|r| > 0.5) ===")
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        r = corr_matrix.iloc[i, j]
        if abs(r) > 0.5:
            print(f"  {corr_matrix.columns[i]} vs {corr_matrix.columns[j]}: r = {r:.3f}")
```

---

## 4.2 Visualisasi untuk Machine Learning

### 4.2.1 Scatter Plot dan Pair Plot

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Menggunakan dataset data_karyawan

# === SCATTER PLOT: Hubungan antar fitur ===
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. Pengalaman vs Gaji (diwarnai berdasarkan resign)
scatter = axes[0].scatter(
    data_karyawan['pengalaman_tahun'],
    data_karyawan['gaji_juta'],
    c=data_karyawan['status_resign'],
    cmap='RdYlGn_r', alpha=0.6, edgecolors='white', linewidth=0.5
)
axes[0].set_xlabel('Pengalaman (tahun)')
axes[0].set_ylabel('Gaji (juta Rp)')
axes[0].set_title('Pengalaman vs Gaji')
plt.colorbar(scatter, ax=axes[0], label='Resign (0=Tidak, 1=Ya)')

# 2. Usia vs Kepuasan Kerja
axes[1].scatter(
    data_karyawan['usia'],
    data_karyawan['kepuasan_kerja'],
    c=data_karyawan['status_resign'],
    cmap='RdYlGn_r', alpha=0.6, edgecolors='white', linewidth=0.5
)
axes[1].set_xlabel('Usia')
axes[1].set_ylabel('Kepuasan Kerja (1-5)')
axes[1].set_title('Usia vs Kepuasan Kerja')

# 3. Jam Lembur vs Jarak Kantor
axes[2].scatter(
    data_karyawan['jam_lembur_per_minggu'],
    data_karyawan['jarak_kantor_km'],
    c=data_karyawan['status_resign'],
    cmap='RdYlGn_r', alpha=0.6, edgecolors='white', linewidth=0.5
)
axes[2].set_xlabel('Jam Lembur per Minggu')
axes[2].set_ylabel('Jarak Kantor (km)')
axes[2].set_title('Lembur vs Jarak Kantor')

plt.suptitle('Scatter Plot: Fitur vs Target (Resign)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('scatter_plots.png', dpi=150, bbox_inches='tight')
plt.show()

# === PAIR PLOT ===
# Untuk melihat hubungan semua pasangan fitur sekaligus
fitur_pairplot = ['pengalaman_tahun', 'gaji_juta', 'jam_lembur_per_minggu',
                  'kepuasan_kerja', 'status_resign']
sns.pairplot(
    data_karyawan[fitur_pairplot].dropna(),
    hue='status_resign',
    palette='RdYlGn_r',
    diag_kind='kde',
    plot_kws={'alpha': 0.5}
)
plt.suptitle('Pair Plot: Hubungan Antar Fitur', y=1.02)
plt.savefig('pair_plot.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 4.2.2 Heatmap untuk Korelasi

```python
import matplotlib.pyplot as plt
import seaborn as sns

# === HEATMAP KORELASI ===
plt.figure(figsize=(10, 8))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))  # Mask segitiga atas
sns.heatmap(
    corr_matrix,
    mask=mask,
    annot=True,
    fmt='.2f',
    cmap='RdBu_r',
    center=0,
    vmin=-1, vmax=1,
    square=True,
    linewidths=0.5,
    cbar_kws={'label': 'Koefisien Korelasi Pearson'}
)
plt.title('Heatmap Korelasi Antar Fitur', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('heatmap_korelasi.png', dpi=150, bbox_inches='tight')
plt.show()

print("Interpretasi:")
print("- Warna MERAH: korelasi positif kuat")
print("- Warna BIRU: korelasi negatif kuat")
print("- Warna PUTIH: korelasi lemah/tidak ada")
```

### 4.2.3 Distribution Plot (Histogram, Boxplot, Violin)

```python
import matplotlib.pyplot as plt
import seaborn as sns

# === BOXPLOT: Deteksi Outlier ===
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. Boxplot gaji per departemen
sns.boxplot(data=data_karyawan, x='departemen', y='gaji_juta', ax=axes[0], palette='Set2')
axes[0].set_title('Distribusi Gaji per Departemen')
axes[0].tick_params(axis='x', rotation=45)

# 2. Boxplot pengalaman per status resign
sns.boxplot(data=data_karyawan, x='status_resign', y='pengalaman_tahun', ax=axes[1], palette='RdYlGn_r')
axes[1].set_xticklabels(['Bertahan', 'Resign'])
axes[1].set_title('Pengalaman: Bertahan vs Resign')

# 3. Violin plot kepuasan per departemen
sns.violinplot(data=data_karyawan, x='departemen', y='kepuasan_kerja', ax=axes[2], palette='Set2', inner='box')
axes[2].set_title('Distribusi Kepuasan per Departemen')
axes[2].tick_params(axis='x', rotation=45)

plt.suptitle('Boxplot & Violin Plot', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('boxplot_violin.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## 4.3 Feature Engineering

### 4.3.1 Apa itu Feature Engineering?

**Feature engineering** adalah proses menciptakan fitur baru dari fitur yang sudah ada untuk meningkatkan performa model ML.

```
FEATURE ENGINEERING
═══════════════════════════════════════════════════
"Coming up with features is difficult, time-consuming,
 requires expert knowledge. Applied machine learning
 is basically feature engineering."
                                    — Andrew Ng

Fitur ASLI:              Fitur BARU (engineered):
├── usia                  ├── usia_kategori (muda/tua)
├── pengalaman_tahun      ├── rasio_gaji_pengalaman
├── gaji_juta             ├── gaji_per_tahun_pengalaman
├── jam_lembur            ├── lembur_x_jarak (interaksi)
└── jarak_kantor          └── gaji_squared (polynomial)
═══════════════════════════════════════════════════
```

### 4.3.2 Feature Creation: Polynomial dan Interaction Features

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Menggunakan subset data karyawan
fitur = data_karyawan[['pengalaman_tahun', 'gaji_juta', 'jam_lembur_per_minggu', 'jarak_kantor_km']].dropna()

# === 1. FITUR DOMAIN KNOWLEDGE ===
# Fitur baru berdasarkan pemahaman domain
df_eng = fitur.copy()

# Rasio gaji per tahun pengalaman
df_eng['gaji_per_pengalaman'] = df_eng['gaji_juta'] / (df_eng['pengalaman_tahun'] + 1)

# Total "beban" karyawan: lembur × jarak
df_eng['beban_komuter'] = df_eng['jam_lembur_per_minggu'] * df_eng['jarak_kantor_km']

# Apakah commute jauh? (> 30 km)
df_eng['commute_jauh'] = (df_eng['jarak_kantor_km'] > 30).astype(int)

# Apakah lembur berlebihan? (> 5 jam/minggu)
df_eng['lembur_berlebihan'] = (df_eng['jam_lembur_per_minggu'] > 5).astype(int)

print("=== FITUR DOMAIN KNOWLEDGE ===")
print(df_eng.head())
print(f"\nShape baru: {df_eng.shape}")

# === 2. POLYNOMIAL FEATURES ===
# Membuat fitur kuadratik dan interaksi secara otomatis
poly = PolynomialFeatures(degree=2, include_bias=False, interaction_only=False)
X_subset = fitur[['pengalaman_tahun', 'gaji_juta']].values

X_poly = poly.fit_transform(X_subset)
fitur_names = poly.get_feature_names_out(['pengalaman', 'gaji'])

print(f"\n=== POLYNOMIAL FEATURES (degree=2) ===")
print(f"Fitur asli: 2 kolom")
print(f"Fitur setelah polynomial: {X_poly.shape[1]} kolom")
print(f"Nama fitur: {list(fitur_names)}")
print(f"\nContoh 3 baris pertama:")
df_poly = pd.DataFrame(X_poly, columns=fitur_names)
print(df_poly.head(3).round(2))
```

### 4.3.3 Feature Encoding Strategies

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

# === STRATEGI ENCODING UNTUK BERBAGAI TIPE DATA ===

# 1. Ordinal Encoding — untuk data dengan urutan alami
ordinal_map = {
    'pendidikan': {'D3': 1, 'S1': 2, 'S2': 3, 'S3': 4}
}

df_encoded = data_karyawan.copy()
df_encoded['pendidikan_ordinal'] = df_encoded['pendidikan'].map(ordinal_map['pendidikan'])

print("=== ORDINAL ENCODING (Pendidikan) ===")
print(df_encoded[['pendidikan', 'pendidikan_ordinal']].drop_duplicates().sort_values('pendidikan_ordinal'))

# 2. One-Hot Encoding — untuk data nominal
df_onehot = pd.get_dummies(df_encoded, columns=['departemen'], prefix='dept', dtype=int)
print(f"\n=== ONE-HOT ENCODING (Departemen) ===")
dept_cols = [c for c in df_onehot.columns if c.startswith('dept_')]
print(df_onehot[dept_cols].head())

# 3. Frequency Encoding — jumlah kemunculan sebagai nilai encoding
freq_map = data_karyawan['departemen'].value_counts(normalize=True).to_dict()
df_encoded['dept_frequency'] = df_encoded['departemen'].map(freq_map)

print(f"\n=== FREQUENCY ENCODING (Departemen) ===")
print(df_encoded[['departemen', 'dept_frequency']].drop_duplicates().sort_values('dept_frequency', ascending=False))

# 4. Target Encoding (Mean Encoding) — rata-rata target per kategori
# HATI-HATI: hanya gunakan pada data training untuk menghindari data leakage!
target_mean = data_karyawan.groupby('departemen')['status_resign'].mean()
df_encoded['dept_target_enc'] = df_encoded['departemen'].map(target_mean)

print(f"\n=== TARGET ENCODING (Departemen → resign rate) ===")
print(df_encoded[['departemen', 'dept_target_enc']].drop_duplicates().sort_values('dept_target_enc', ascending=False))
```

**Panduan Pemilihan Encoding:**

| Tipe Data | Metode Encoding | Alasan |
|-----------|----------------|--------|
| Nominal (sedikit kategori, < 10) | One-Hot Encoding | Tidak ada urutan, hindari ordinal bias |
| Nominal (banyak kategori, > 10) | Frequency / Target Encoding | One-hot terlalu banyak kolom |
| Ordinal (ada urutan) | Ordinal Encoding | Menjaga urutan alami |
| Binary (2 kategori) | Label Encoding (0/1) | Sederhana dan efektif |

### 4.3.4 Feature Scaling Comparison

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
import matplotlib.pyplot as plt

# Data dengan outlier untuk perbandingan scaler
np.random.seed(42)
data_scaling = pd.DataFrame({
    'gaji_juta': np.append(np.random.normal(12, 3, 95), [45, 50, 55, 60, 65]),
    'pengalaman_tahun': np.append(np.random.exponential(4, 95), [20, 22, 25, 28, 30]),
})

# Tiga scaler
scalers = {
    'StandardScaler': StandardScaler(),
    'MinMaxScaler': MinMaxScaler(),
    'RobustScaler': RobustScaler()  # Robust terhadap outlier
}

fig, axes = plt.subplots(1, 4, figsize=(20, 4))

# Plot data asli
axes[0].boxplot([data_scaling['gaji_juta'], data_scaling['pengalaman_tahun']],
                labels=['Gaji', 'Pengalaman'])
axes[0].set_title('Data Asli')

for idx, (name, scaler) in enumerate(scalers.items(), 1):
    scaled = pd.DataFrame(
        scaler.fit_transform(data_scaling),
        columns=data_scaling.columns
    )
    axes[idx].boxplot([scaled['gaji_juta'], scaled['pengalaman_tahun']],
                      labels=['Gaji', 'Pengalaman'])
    axes[idx].set_title(name)

plt.suptitle('Perbandingan Feature Scaling', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('perbandingan_scaler.png', dpi=150, bbox_inches='tight')
plt.show()

# Statistik perbandingan
print("=== PERBANDINGAN SCALER ===")
for name, scaler in scalers.items():
    scaled = pd.DataFrame(
        scaler.fit_transform(data_scaling),
        columns=data_scaling.columns
    )
    print(f"\n{name}:")
    print(f"  Gaji  - Mean: {scaled['gaji_juta'].mean():.3f}, "
          f"Std: {scaled['gaji_juta'].std():.3f}, "
          f"Min: {scaled['gaji_juta'].min():.3f}, "
          f"Max: {scaled['gaji_juta'].max():.3f}")
```

**Kapan menggunakan scaler mana?**

| Scaler | Rumus | Cocok untuk |
|--------|-------|-------------|
| **StandardScaler** | z = (x - μ) / σ | Data normal, tanpa outlier berat |
| **MinMaxScaler** | x' = (x - min) / (max - min) | Neural networks, data bounded |
| **RobustScaler** | x' = (x - Q2) / (Q3 - Q1) | Data dengan banyak outlier |

---

## 4.4 Data Quality untuk ML

### 4.4.1 Handling Outlier

Outlier (*pencilan*) adalah data point yang berbeda signifikan dari mayoritas data. Outlier bisa **merusak** performa model ML.

```python
import pandas as pd
import numpy as np

# Menggunakan kolom gaji dari data_karyawan
gaji = data_karyawan['gaji_juta'].dropna()

# === METODE 1: IQR (Interquartile Range) ===
Q1 = gaji.quantile(0.25)
Q3 = gaji.quantile(0.75)
IQR = Q3 - Q1

batas_bawah = Q1 - 1.5 * IQR
batas_atas = Q3 + 1.5 * IQR

outlier_iqr = gaji[(gaji < batas_bawah) | (gaji > batas_atas)]

print("=== DETEKSI OUTLIER: METODE IQR ===")
print(f"Q1 = {Q1:.2f}")
print(f"Q3 = {Q3:.2f}")
print(f"IQR = {IQR:.2f}")
print(f"Batas bawah = {batas_bawah:.2f}")
print(f"Batas atas = {batas_atas:.2f}")
print(f"Jumlah outlier = {len(outlier_iqr)}")
print(f"Outlier: {sorted(outlier_iqr.values)}")

# === METODE 2: Z-Score ===
from scipy import stats

z_scores = np.abs(stats.zscore(gaji))
outlier_zscore = gaji[z_scores > 3]  # threshold z > 3

print(f"\n=== DETEKSI OUTLIER: METODE Z-SCORE (|z| > 3) ===")
print(f"Jumlah outlier = {len(outlier_zscore)}")

# === STRATEGI PENANGANAN OUTLIER ===
print(f"\n=== STRATEGI PENANGANAN ===")

# 1. Removal (hapus outlier)
gaji_no_outlier = gaji[(gaji >= batas_bawah) & (gaji <= batas_atas)]
print(f"1. Removal: {len(gaji)} → {len(gaji_no_outlier)} data")

# 2. Capping (clipping ke batas)
gaji_capped = gaji.clip(lower=batas_bawah, upper=batas_atas)
print(f"2. Capping: Min={gaji_capped.min():.1f}, Max={gaji_capped.max():.1f}")

# 3. Log transformation (mengurangi skewness)
gaji_log = np.log1p(gaji)
print(f"3. Log Transform: Skewness asli={gaji.skew():.3f}, "
      f"Setelah log={gaji_log.skew():.3f}")

# Perbandingan statistik
print(f"\n=== PERBANDINGAN STATISTIK ===")
print(f"{'Metode':<20} {'Mean':>8} {'Median':>8} {'Std':>8}")
print(f"{'Asli':<20} {gaji.mean():>8.2f} {gaji.median():>8.2f} {gaji.std():>8.2f}")
print(f"{'No Outlier':<20} {gaji_no_outlier.mean():>8.2f} {gaji_no_outlier.median():>8.2f} {gaji_no_outlier.std():>8.2f}")
print(f"{'Capped':<20} {gaji_capped.mean():>8.2f} {gaji_capped.median():>8.2f} {gaji_capped.std():>8.2f}")
```

### 4.4.2 Data Quality Checklist

Sebelum memulai modeling, pastikan data memenuhi **checklist kualitas** berikut:

```
DATA QUALITY CHECKLIST UNTUK ML
═══════════════════════════════════════════════════
☐ 1. COMPLETENESS — Apakah ada missing values?
     → Berapa persen? Pola missingness (random/systematic)?
     → Strategi: imputasi (mean/median/mode) atau hapus

☐ 2. CORRECTNESS — Apakah data masuk akal?
     → Usia negatif? Gaji 0? IPK > 4.0?
     → Range check setiap kolom numerik

☐ 3. CONSISTENCY — Apakah format konsisten?
     → "Jakarta" vs "JAKARTA" vs "Jkt"
     → Date format: DD/MM/YYYY vs MM-DD-YYYY

☐ 4. OUTLIERS — Apakah ada outlier?
     → IQR method, z-score method
     → Outlier genuine (keep) vs error (remove)

☐ 5. DUPLICATES — Apakah ada data duplikat?
     → Exact duplicates vs near-duplicates

☐ 6. DATA TYPES — Apakah tipe data sesuai?
     → NIM bukan integer! Kode pos bukan numerik!

☐ 7. CLASS BALANCE — Apakah kelas target seimbang?
     → Jika imbalanced (misal 95:5), pertimbangkan
        oversampling/undersampling

☐ 8. FEATURE RELEVANCE — Apakah semua fitur relevan?
     → Hapus fitur yang tidak informatif (ID, nama)
     → Cek korelasi dengan target
═══════════════════════════════════════════════════
```

```python
import pandas as pd
import numpy as np

def data_quality_check(df, target_col=None):
    """Fungsi otomatis untuk mengecek kualitas data"""
    print("=" * 60)
    print("DATA QUALITY REPORT")
    print("=" * 60)

    # 1. Shape
    print(f"\n1. SHAPE: {df.shape[0]} baris × {df.shape[1]} kolom")

    # 2. Missing Values
    missing = df.isnull().sum()
    missing_pct = (df.isnull().mean() * 100).round(1)
    has_missing = missing[missing > 0]
    print(f"\n2. MISSING VALUES: {len(has_missing)} kolom memiliki missing data")
    if len(has_missing) > 0:
        for col in has_missing.index:
            print(f"   - {col}: {missing[col]} ({missing_pct[col]}%)")

    # 3. Duplicates
    n_dup = df.duplicated().sum()
    print(f"\n3. DUPLIKAT: {n_dup} baris duplikat")

    # 4. Data Types
    print(f"\n4. TIPE DATA:")
    for dtype in df.dtypes.unique():
        cols = df.select_dtypes(include=[dtype]).columns.tolist()
        print(f"   - {dtype}: {len(cols)} kolom → {cols}")

    # 5. Outliers (numerik saja, metode IQR)
    print(f"\n5. OUTLIER (metode IQR):")
    for col in df.select_dtypes(include=[np.number]).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        n_outlier = ((df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)).sum()
        if n_outlier > 0:
            print(f"   - {col}: {n_outlier} outlier ({n_outlier/len(df)*100:.1f}%)")

    # 6. Class Balance (jika target diberikan)
    if target_col and target_col in df.columns:
        print(f"\n6. CLASS BALANCE ({target_col}):")
        vc = df[target_col].value_counts()
        for val, count in vc.items():
            print(f"   - {val}: {count} ({count/len(df)*100:.1f}%)")
        ratio = vc.min() / vc.max()
        status = "SEIMBANG" if ratio > 0.5 else ("MODERAT" if ratio > 0.2 else "TIDAK SEIMBANG")
        print(f"   Rasio min/max: {ratio:.2f} → {status}")

    print("\n" + "=" * 60)

# Jalankan quality check
data_quality_check(data_karyawan, target_col='status_resign')
```

---

## 4.5 Studi Kasus Indonesia: EDA pada Dataset E-Commerce

### 4.5.1 Konteks

Kita akan melakukan EDA pada dataset transaksi e-commerce Indonesia (data sintetis berdasarkan pola nyata).

```python
import pandas as pd
import numpy as np

# === GENERATE DATASET E-COMMERCE INDONESIA ===
np.random.seed(42)
n = 500

# Kota-kota besar di Indonesia
kota_list = ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Semarang',
             'Makassar', 'Palembang', 'Tangerang', 'Depok', 'Bekasi']
kota_probs = [0.25, 0.12, 0.10, 0.08, 0.07, 0.06, 0.05, 0.10, 0.09, 0.08]

kategori_list = ['Elektronik', 'Fashion', 'Makanan', 'Kesehatan', 'Hobi',
                 'Olahraga', 'Buku', 'Rumah Tangga']
kategori_probs = [0.20, 0.25, 0.15, 0.10, 0.08, 0.07, 0.05, 0.10]

df_ecom = pd.DataFrame({
    'order_id': [f'ORD-{i:04d}' for i in range(1, n+1)],
    'tanggal': pd.date_range('2025-01-01', periods=n, freq='4h'),
    'kota': np.random.choice(kota_list, n, p=kota_probs),
    'kategori': np.random.choice(kategori_list, n, p=kategori_probs),
    'harga_produk': np.random.lognormal(mean=10.5, sigma=1.2, size=n).round(0).astype(int),
    'kuantitas': np.random.choice([1, 1, 1, 2, 2, 3, 4, 5], n),
    'metode_bayar': np.random.choice(
        ['Transfer Bank', 'E-Wallet', 'COD', 'Kartu Kredit', 'Cicilan'],
        n, p=[0.25, 0.35, 0.15, 0.15, 0.10]
    ),
    'rating': np.random.choice([1, 2, 3, 4, 5], n, p=[0.03, 0.07, 0.15, 0.40, 0.35]),
    'is_returned': np.random.choice([0, 1], n, p=[0.92, 0.08])
})

# Hitung total harga
df_ecom['total_harga'] = df_ecom['harga_produk'] * df_ecom['kuantitas']

# Tambahkan missing values
mask = np.random.choice(n, 25, replace=False)
df_ecom.loc[mask, 'rating'] = np.nan

print("=== DATASET E-COMMERCE INDONESIA ===")
print(f"Shape: {df_ecom.shape}")
print(f"\n{df_ecom.head(10)}")
print(f"\n=== STATISTIK DESKRIPTIF ===")
print(df_ecom.describe().round(2))

# === EDA ===
print(f"\n=== TOP 5 KOTA TRANSAKSI ===")
print(df_ecom['kota'].value_counts().head())

print(f"\n=== TRANSAKSI PER KATEGORI ===")
print(df_ecom.groupby('kategori')['total_harga'].agg(['count', 'mean', 'sum']).round(0).sort_values('sum', ascending=False))

print(f"\n=== METODE PEMBAYARAN ===")
print(df_ecom['metode_bayar'].value_counts())

print(f"\n=== RETURN RATE PER KATEGORI ===")
return_rate = df_ecom.groupby('kategori')['is_returned'].mean().sort_values(ascending=False)
print((return_rate * 100).round(1))
```

### 4.5.2 Visualisasi EDA E-Commerce

```python
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1. Distribusi total harga
axes[0, 0].hist(df_ecom['total_harga'], bins=50, color='steelblue', edgecolor='white', alpha=0.7)
axes[0, 0].set_title('Distribusi Total Harga Transaksi')
axes[0, 0].set_xlabel('Total Harga (Rp)')
axes[0, 0].set_ylabel('Frekuensi')

# 2. Transaksi per kota (horizontal bar)
kota_counts = df_ecom['kota'].value_counts()
axes[0, 1].barh(kota_counts.index, kota_counts.values, color='green', alpha=0.7)
axes[0, 1].set_title('Jumlah Transaksi per Kota')
axes[0, 1].set_xlabel('Jumlah Transaksi')

# 3. Rata-rata harga per kategori
avg_harga = df_ecom.groupby('kategori')['total_harga'].mean().sort_values()
axes[1, 0].barh(avg_harga.index, avg_harga.values, color='coral', alpha=0.7)
axes[1, 0].set_title('Rata-rata Total Harga per Kategori')
axes[1, 0].set_xlabel('Rata-rata Harga (Rp)')

# 4. Distribusi rating
rating_clean = df_ecom['rating'].dropna()
axes[1, 1].hist(rating_clean, bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5],
                color='gold', edgecolor='black', alpha=0.8)
axes[1, 1].set_title('Distribusi Rating Produk')
axes[1, 1].set_xlabel('Rating')
axes[1, 1].set_ylabel('Frekuensi')
axes[1, 1].set_xticks([1, 2, 3, 4, 5])

plt.suptitle('EDA: Dataset E-Commerce Indonesia', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('eda_ecommerce.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 4.5.3 Feature Engineering untuk Dataset E-Commerce

```python
# === FEATURE ENGINEERING ===
df_feat = df_ecom.copy()

# 1. Fitur waktu dari kolom tanggal
df_feat['hari'] = df_feat['tanggal'].dt.day_name()
df_feat['jam'] = df_feat['tanggal'].dt.hour
df_feat['akhir_pekan'] = df_feat['tanggal'].dt.dayofweek.isin([5, 6]).astype(int)

# 2. Fitur harga
df_feat['harga_log'] = np.log1p(df_feat['total_harga'])
df_feat['harga_kategori'] = pd.cut(
    df_feat['total_harga'],
    bins=[0, 50000, 200000, 1000000, float('inf')],
    labels=['Murah', 'Sedang', 'Mahal', 'Premium']
)

# 3. Fitur interaksi
df_feat['high_quantity_expensive'] = (
    (df_feat['kuantitas'] >= 3) & (df_feat['harga_produk'] > df_feat['harga_produk'].median())
).astype(int)

print("=== FITUR BARU ===")
print(df_feat[['tanggal', 'hari', 'jam', 'akhir_pekan', 'total_harga',
               'harga_log', 'harga_kategori', 'high_quantity_expensive']].head(10))

print(f"\n=== TRANSAKSI AKHIR PEKAN vs HARI KERJA ===")
print(df_feat.groupby('akhir_pekan')['total_harga'].agg(['count', 'mean']).round(0))

print(f"\n=== DISTRIBUSI HARGA KATEGORI ===")
print(df_feat['harga_kategori'].value_counts())
```

---

## 4.6 AI Corner: Menggunakan AI untuk EDA

### 4.6.1 AI untuk Saran EDA

Level: **Basic-Intermediate**

| AI Bisa | AI Tidak Bisa |
|---------|--------------|
| Menyarankan visualisasi yang tepat untuk tipe data | Melihat data Anda secara langsung (kecuali Anda share) |
| Menulis kode EDA dari deskripsi dataset | Menentukan insight mana yang paling penting untuk bisnis |
| Menjelaskan interpretasi statistik deskriptif | Menjamin semua pola ditemukan |
| Menyarankan feature engineering ideas | Mengetahui domain knowledge spesifik bisnis Anda |

### 4.6.2 Contoh Prompt untuk EDA

**Prompt yang Baik:**
```
Saya punya dataset transaksi e-commerce Indonesia dengan kolom:
order_id, tanggal, kota (10 kota), kategori (8 kategori),
harga_produk, kuantitas, metode_bayar, rating (1-5, 5% missing),
is_returned (binary), total_harga.

Dataset memiliki 500 baris.

Buatkan kode EDA lengkap yang mencakup:
1. Analisis missing values dan rekomendasi penanganan
2. Statistik deskriptif untuk kolom numerik dan kategorikal
3. Analisis distribusi harga (apakah perlu log transform?)
4. Korelasi antara fitur numerik
5. 3 visualisasi paling informatif (scatter, box, bar)
6. 5 ide feature engineering berdasarkan kolom yang ada

Gunakan matplotlib dan seaborn. Sertakan interpretasi setiap visualisasi.
```

**Prompt yang Kurang Baik:**
```
Buatkan EDA untuk data saya
```

### 4.6.3 Aktivitas: EDA dengan Bantuan AI

1. Upload dataset ke ChatGPT/Claude (atau deskripsikan strukturnya)
2. Minta AI menghasilkan kode EDA
3. Jalankan kode di Google Colab — apakah ada error?
4. Modifikasi visualisasi sesuai preferensi Anda
5. Bandingkan insight dari AI dengan insight yang Anda temukan sendiri
6. Dokumentasikan dalam AI Usage Log

### 4.6.4 Batasan AI untuk EDA

```
┌─────────────────────────────────────────────────┐
│           BATASAN AI DALAM EDA                    │
│                                                   │
│  AI memberikan KODE yang benar secara teknis,     │
│  tetapi INSIGHT memerlukan pemahaman manusia:     │
│                                                   │
│  ✗ AI tidak tahu konteks bisnis Indonesia         │
│  ✗ AI tidak bisa menentukan apakah outlier        │
│    adalah error atau data genuine                  │
│  ✗ AI tidak memahami regulasi lokal               │
│    (OJK, BI, Kominfo)                              │
│  ✗ AI bisa menghasilkan visualisasi yang           │
│    technically correct tapi misleading             │
│                                                   │
│  ✓ ANDA yang harus menginterpretasi hasil          │
│  ✓ ANDA yang memutuskan tindakan                   │
│  ✓ ANDA yang bertanggung jawab atas kesimpulan     │
└─────────────────────────────────────────────────┘
```

---

## Rangkuman Bab 4

1. **EDA (Exploratory Data Analysis)** adalah langkah krusial sebelum modeling — memahami data secara mendalam sebelum membangun model.
2. **Statistik deskriptif** (mean, median, std, skewness) memberikan gambaran numerik tentang distribusi data.
3. **Visualisasi ML** — scatter plot, pair plot, heatmap, boxplot, dan violin plot masing-masing memiliki kegunaan spesifik untuk mengungkap pola berbeda dalam data.
4. **Feature Engineering** menciptakan fitur baru yang lebih informatif: fitur domain knowledge, polynomial features, interaction features, dan fitur temporal.
5. **Feature Encoding** harus disesuaikan dengan tipe data: One-Hot untuk nominal, Ordinal Encoding untuk ordinal, Frequency/Target Encoding untuk kategori banyak.
6. **Outlier** harus dideteksi (IQR, z-score) dan ditangani (removal, capping, log transform) sesuai konteks.
7. **Data Quality Checklist** mencakup: completeness, correctness, consistency, outliers, duplicates, data types, class balance, dan feature relevance.
8. AI bisa membantu menghasilkan kode EDA, tetapi **interpretasi dan insight** tetap memerlukan pemahaman domain oleh manusia.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan apa itu EDA dan mengapa EDA penting dilakukan sebelum membangun model machine learning. Sebutkan minimal 5 hal yang dicari saat EDA.

**Soal 2.** Jelaskan perbedaan penggunaan visualisasi berikut:
- a) Histogram vs Boxplot
- b) Scatter plot vs Heatmap korelasi
- c) Bar chart vs Pie chart
Untuk masing-masing, sebutkan kapan lebih tepat digunakan.

**Soal 3.** Apa yang dimaksud dengan skewness? Jelaskan perbedaan right-skewed, left-skewed, dan distribusi simetris. Berikan contoh data di Indonesia yang kemungkinan memiliki distribusi right-skewed.

**Soal 4.** Sebutkan dan jelaskan 4 strategi encoding untuk variabel kategorikal. Kapan masing-masing digunakan?

**Soal 5.** Apa perbedaan antara StandardScaler, MinMaxScaler, dan RobustScaler? Kapan masing-masing lebih tepat digunakan?

### Tingkat Menengah (C3)

**Soal 6.** Buatlah dataset sintetis 100 baris untuk "data penjualan warung kopi di Jakarta" dengan kolom:
- tanggal, jam, jenis_kopi, ukuran, harga, jumlah_pesanan, metode_bayar, rating
- Lakukan EDA lengkap (statistik deskriptif, missing values, distribusi, korelasi)
- Buat minimal 3 visualisasi yang informatif
- Interpretasikan hasil

**Soal 7.** Untuk dataset di Soal 6, lakukan feature engineering:
- a) Buat minimal 3 fitur baru berdasarkan domain knowledge
- b) Encode semua variabel kategorikal dengan metode yang tepat
- c) Tentukan scaler yang tepat dan jelaskan alasannya
- d) Lakukan data quality check

**Soal 8.** Diberikan dataset dengan 5% missing values pada kolom rating dan 20% missing values pada kolom pendapatan. Jelaskan:
- a) Bagaimana menganalisis apakah missing values bersifat MCAR, MAR, atau MNAR?
- b) Strategi imputasi apa yang paling tepat untuk masing-masing kolom?
- c) Tulis kode Python untuk implementasinya

### Tingkat Mahir (C3-C4)

**Soal 9.** Mini-project EDA: Gunakan dataset publik Indonesia (bisa dari BPS, Open Data Jakarta, atau buat sendiri). Lakukan:
- a) EDA lengkap (minimal 500 kata interpretasi)
- b) Feature engineering (minimal 5 fitur baru)
- c) Data quality check
- d) Rekomendasi: fitur mana yang paling informatif untuk modeling?
- e) Dokumentasikan penggunaan AI (jika ada) dalam AI Usage Log

**Soal 10.** Analisis perbandingan: Buat fungsi Python `compare_feature_engineering()` yang:
- a) Menerima DataFrame dan kolom target
- b) Melatih model sederhana (DecisionTree) dengan fitur ASLI
- c) Melatih model yang sama dengan fitur HASIL ENGINEERING
- d) Membandingkan akurasi kedua model
- e) Menampilkan laporan: fitur baru mana yang paling berkontribusi?
- Tunjukkan bahwa feature engineering meningkatkan performa model.

---

## Daftar Pustaka Bab 4

1. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
2. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
3. Zheng, A., & Casari, A. (2018). *Feature Engineering for Machine Learning*. O'Reilly Media.
4. Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
5. VanderPlas, J. (2016). *Python Data Science Handbook* — Chapter 4: Visualization with Matplotlib. O'Reilly Media.
6. Seaborn Documentation. (2025). *Statistical Data Visualization*. https://seaborn.pydata.org
7. Scikit-learn Documentation. (2025). *Feature Extraction and Preprocessing*. https://scikit-learn.org
8. BPS. (2024). *Statistik Indonesia 2024*. Badan Pusat Statistik.

---

*Bab berikutnya: **Bab 5 — Regresi Linear dan Regresi Logistik***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
