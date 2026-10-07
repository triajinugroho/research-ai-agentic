# Lab 04: EDA dan Feature Engineering

**Mata Kuliah:** Kecerdasan Buatan dan Machine Learning
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Minggu:** 4
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

- Memuat dan melakukan eksplorasi awal pada dataset konteks Indonesia
- Menghitung statistik deskriptif dan menganalisis distribusi data
- Membuat visualisasi distribusi (histogram, boxplot, violin plot)
- Melakukan analisis korelasi dengan heatmap dan pairplot
- Membuat fitur baru (polynomial features, interaction terms)
- Mendeteksi dan menangani outlier dengan metode IQR dan z-score
- Menyusun pipeline EDA lengkap dari awal hingga akhir

---

## Persiapan

1. Buka Google Colab dan buat notebook baru
2. Nama file: `Lab04_NamaAnda_NIM.ipynb`
3. Pastikan library pandas, numpy, matplotlib, seaborn, dan scikit-learn sudah tersedia
4. Pahami konsep statistika deskriptif dari Lab 02

---

## Langkah-langkah

### Langkah 1: Load Dataset Properti Indonesia

```python
# =============================================
# LANGKAH 1: Load Dataset Properti Indonesia
# =============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pengaturan tampilan
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format)
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

np.random.seed(42)

# --- Buat Dataset Simulasi Properti Indonesia ---
n = 500

# Kota dan rata-rata harga per meter persegi (juta Rp)
kota_data = {
    'Jakarta Selatan': {'harga_m2': 35, 'std': 10},
    'Jakarta Pusat': {'harga_m2': 40, 'std': 12},
    'Bandung': {'harga_m2': 15, 'std': 5},
    'Surabaya': {'harga_m2': 18, 'std': 6},
    'Yogyakarta': {'harga_m2': 12, 'std': 4},
    'Depok': {'harga_m2': 14, 'std': 5},
}

kota_list = list(kota_data.keys())
prob_kota = [0.25, 0.15, 0.20, 0.15, 0.10, 0.15]

data = {
    'id_properti': range(1, n + 1),
    'kota': np.random.choice(kota_list, size=n, p=prob_kota),
    'tipe_properti': np.random.choice(
        ['Rumah', 'Apartemen', 'Townhouse', 'Ruko'],
        size=n, p=[0.45, 0.25, 0.15, 0.15]
    ),
    'luas_bangunan_m2': np.random.lognormal(mean=4.2, sigma=0.5, size=n).astype(int).clip(30, 500),
    'luas_tanah_m2': np.random.lognormal(mean=4.5, sigma=0.6, size=n).astype(int).clip(30, 1000),
    'jumlah_kamar': np.random.choice([1, 2, 3, 4, 5, 6], size=n, p=[0.05, 0.20, 0.35, 0.25, 0.10, 0.05]),
    'jumlah_km_mandi': np.random.choice([1, 2, 3, 4], size=n, p=[0.15, 0.40, 0.30, 0.15]),
    'tahun_dibangun': np.random.choice(range(1985, 2026), size=n),
    'sertifikat': np.random.choice(['SHM', 'HGB', 'PPJB', 'Girik'], size=n, p=[0.45, 0.30, 0.15, 0.10]),
    'akses_jalan': np.random.choice(['Lebar > 6m', 'Lebar 4-6m', 'Lebar < 4m'], size=n, p=[0.35, 0.40, 0.25]),
}

df = pd.DataFrame(data)

# Hitung harga berdasarkan kota dan fitur
harga_base = []
for _, row in df.iterrows():
    kota_info = kota_data[row['kota']]
    base = row['luas_bangunan_m2'] * np.random.normal(kota_info['harga_m2'], kota_info['std'])
    # Faktor tambahan
    base *= (1 + (row['jumlah_kamar'] - 3) * 0.05)  # Kamar lebih banyak = lebih mahal
    base *= np.random.uniform(0.85, 1.15)  # Noise
    harga_base.append(max(base, 100))  # Minimal 100 juta

df['harga_juta'] = np.round(harga_base, 0).astype(int)

# Masukkan beberapa missing values
df.loc[np.random.choice(n, 20, replace=False), 'luas_tanah_m2'] = np.nan
df.loc[np.random.choice(n, 10, replace=False), 'tahun_dibangun'] = np.nan

print(f"Dataset Properti Indonesia: {df.shape[0]} baris x {df.shape[1]} kolom")
print(f"\nKolom: {list(df.columns)}")
df.head(10)
```

### Langkah 2: Statistical Summary

```python
# =============================================
# LANGKAH 2: Statistical Summary
# =============================================

print("=" * 60)
print("STATISTICAL SUMMARY")
print("=" * 60)

# --- describe() untuk kolom numerik ---
print("\n--- Statistik Deskriptif (Numerik) ---")
print(df.describe().round(2))

# --- describe() untuk kolom kategorikal ---
print("\n--- Statistik Deskriptif (Kategorikal) ---")
print(df.describe(include='object'))

# --- value_counts() untuk setiap kolom kategorikal ---
print("\n--- Distribusi Kota ---")
print(df['kota'].value_counts())

print("\n--- Distribusi Tipe Properti ---")
print(df['tipe_properti'].value_counts())

print("\n--- Distribusi Sertifikat ---")
print(df['sertifikat'].value_counts())

# --- Missing values ---
print("\n--- Missing Values ---")
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_df = pd.DataFrame({'Jumlah': missing, 'Persentase (%)': missing_pct})
print(missing_df[missing_df['Jumlah'] > 0])

# --- Info tipe data ---
print("\n--- Tipe Data ---")
print(df.dtypes)
```

### Langkah 3: Distribution Plots

```python
# =============================================
# LANGKAH 3: Distribution Plots
# =============================================

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Distribusi Variabel Numerik - Dataset Properti Indonesia', fontsize=16, fontweight='bold')

kolom_numerik = ['harga_juta', 'luas_bangunan_m2', 'luas_tanah_m2',
                 'jumlah_kamar', 'jumlah_km_mandi', 'tahun_dibangun']

for i, col in enumerate(kolom_numerik):
    ax = axes[i // 3, i % 3]

    # Histogram dengan KDE
    data_col = df[col].dropna()
    ax.hist(data_col, bins=30, color='steelblue', edgecolor='white', alpha=0.7, density=True)
    data_col.plot.kde(ax=ax, color='red', linewidth=2)

    ax.set_title(f'Distribusi {col}', fontsize=12)
    ax.set_xlabel(col)
    ax.set_ylabel('Density')

    # Tambahkan mean dan median
    mean_val = data_col.mean()
    median_val = data_col.median()
    ax.axvline(mean_val, color='green', linestyle='--', alpha=0.7, label=f'Mean: {mean_val:.0f}')
    ax.axvline(median_val, color='orange', linestyle='--', alpha=0.7, label=f'Median: {median_val:.0f}')
    ax.legend(fontsize=8)

plt.tight_layout()
plt.show()

# --- Boxplot per kategori ---
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Boxplot harga per kota
sns.boxplot(data=df, x='kota', y='harga_juta', ax=axes[0], palette='Set2')
axes[0].set_title('Harga Properti per Kota', fontsize=12)
axes[0].tick_params(axis='x', rotation=45)

# Boxplot harga per tipe properti
sns.boxplot(data=df, x='tipe_properti', y='harga_juta', ax=axes[1], palette='Set3')
axes[1].set_title('Harga Properti per Tipe', fontsize=12)
axes[1].tick_params(axis='x', rotation=45)

# Violin plot harga per sertifikat
sns.violinplot(data=df, x='sertifikat', y='harga_juta', ax=axes[2], palette='pastel')
axes[2].set_title('Distribusi Harga per Sertifikat', fontsize=12)
axes[2].tick_params(axis='x', rotation=45)

plt.suptitle('Boxplot dan Violin Plot - Perbandingan Harga', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Langkah 4: Analisis Korelasi

```python
# =============================================
# LANGKAH 4: Analisis Korelasi
# =============================================

print("=" * 60)
print("ANALISIS KORELASI")
print("=" * 60)

# --- Heatmap Korelasi ---
kolom_num = ['harga_juta', 'luas_bangunan_m2', 'luas_tanah_m2',
             'jumlah_kamar', 'jumlah_km_mandi', 'tahun_dibangun']

corr_matrix = df[kolom_num].corr()
print("Matriks Korelasi:")
print(corr_matrix.round(3))

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Heatmap korelasi
sns.heatmap(corr_matrix, annot=True, cmap='RdBu_r', center=0,
            fmt='.2f', ax=axes[0], square=True, linewidths=0.5)
axes[0].set_title('Heatmap Korelasi', fontsize=13)

# Korelasi dengan harga (target)
corr_with_harga = corr_matrix['harga_juta'].drop('harga_juta').sort_values(ascending=True)
corr_with_harga.plot(kind='barh', color=['coral' if x < 0 else 'steelblue' for x in corr_with_harga],
                     ax=axes[1], edgecolor='white')
axes[1].set_title('Korelasi Fitur dengan Harga', fontsize=13)
axes[1].set_xlabel('Koefisien Korelasi')
axes[1].axvline(x=0, color='black', linewidth=0.5)

plt.tight_layout()
plt.show()

# --- Pairplot (untuk subset fitur) ---
fitur_subset = ['harga_juta', 'luas_bangunan_m2', 'jumlah_kamar', 'tipe_properti']
g = sns.pairplot(df[fitur_subset].dropna(), hue='tipe_properti', palette='Set2',
                 diag_kind='kde', plot_kws={'alpha': 0.6, 's': 30})
g.fig.suptitle('Pairplot Fitur Utama', y=1.02, fontsize=14)
plt.show()

print("\nKorelasi tertinggi dengan harga:")
for fitur, corr in corr_with_harga.items():
    print(f"  {fitur:25s}: {corr:+.3f}")
```

### Langkah 5: Feature Creation

```python
# =============================================
# LANGKAH 5: Feature Creation
# =============================================

from sklearn.preprocessing import PolynomialFeatures

print("=" * 60)
print("FEATURE CREATION")
print("=" * 60)

df_feat = df.copy()

# --- 1. Fitur Interaksi Manual ---
print("\n--- Fitur Interaksi Manual ---")

# Rasio luas bangunan terhadap luas tanah
df_feat['rasio_bangunan_tanah'] = df_feat['luas_bangunan_m2'] / df_feat['luas_tanah_m2']

# Harga per meter persegi
df_feat['harga_per_m2'] = df_feat['harga_juta'] / df_feat['luas_bangunan_m2']

# Usia bangunan
df_feat['usia_bangunan'] = 2026 - df_feat['tahun_dibangun']

# Total ruangan
df_feat['total_ruangan'] = df_feat['jumlah_kamar'] + df_feat['jumlah_km_mandi']

# Luas per kamar
df_feat['luas_per_kamar'] = df_feat['luas_bangunan_m2'] / df_feat['jumlah_kamar']

fitur_baru = ['rasio_bangunan_tanah', 'harga_per_m2', 'usia_bangunan',
              'total_ruangan', 'luas_per_kamar']
print(f"Fitur baru yang dibuat: {fitur_baru}")
print(df_feat[fitur_baru].describe().round(2))

# --- 2. Polynomial Features (sklearn) ---
print("\n--- Polynomial Features ---")
X_subset = df[['luas_bangunan_m2', 'jumlah_kamar']].dropna().values[:10]

poly = PolynomialFeatures(degree=2, include_bias=False, interaction_only=False)
X_poly = poly.fit_transform(X_subset)

print(f"Fitur asli: {['luas_bangunan_m2', 'jumlah_kamar']}")
print(f"Fitur polynomial: {poly.get_feature_names_out(['luas_bangunan', 'jml_kamar'])}")
print(f"Shape asli     : {X_subset.shape}")
print(f"Shape polynomial: {X_poly.shape}")

# Tampilkan contoh
df_poly = pd.DataFrame(X_poly, columns=poly.get_feature_names_out(['luas_bangunan', 'jml_kamar']))
print(df_poly.head())

# --- 3. Interaction Terms ---
print("\n--- Interaction Terms ---")
poly_interact = PolynomialFeatures(degree=2, include_bias=False, interaction_only=True)
X_interact = poly_interact.fit_transform(X_subset)

print(f"Hanya interaction terms: {poly_interact.get_feature_names_out(['luas_bangunan', 'jml_kamar'])}")
print(f"Shape: {X_interact.shape}")
```

### Langkah 6: Feature Encoding Lanjutan

```python
# =============================================
# LANGKAH 6: Feature Encoding Lanjutan
# =============================================

print("=" * 60)
print("FEATURE ENCODING LANJUTAN")
print("=" * 60)

df_enc = df.copy()

# --- 1. Target Encoding ---
print("\n--- Target Encoding ---")
# Encoding kota berdasarkan rata-rata harga (target)
target_mean_kota = df_enc.groupby('kota')['harga_juta'].mean()
df_enc['kota_target_enc'] = df_enc['kota'].map(target_mean_kota)

print("Target encoding (kota -> rata-rata harga):")
for kota, mean_harga in target_mean_kota.sort_values(ascending=False).items():
    print(f"  {kota:20s}: {mean_harga:,.0f} juta")

# --- 2. Binary Encoding Manual ---
print("\n--- Binary Encoding ---")
# Contoh: sertifikat menjadi binary features
df_enc['is_shm'] = (df_enc['sertifikat'] == 'SHM').astype(int)
df_enc['is_hgb'] = (df_enc['sertifikat'] == 'HGB').astype(int)

print("Binary encoding sertifikat:")
print(df_enc[['sertifikat', 'is_shm', 'is_hgb']].drop_duplicates().sort_values('sertifikat'))

# --- 3. Ordinal Encoding ---
print("\n--- Ordinal Encoding ---")
# Akses jalan memiliki urutan alami
ordinal_map = {'Lebar < 4m': 0, 'Lebar 4-6m': 1, 'Lebar > 6m': 2}
df_enc['akses_jalan_ordinal'] = df_enc['akses_jalan'].map(ordinal_map)

print("Ordinal encoding akses jalan:")
for label, kode in ordinal_map.items():
    print(f"  {label} -> {kode}")

# Korelasi fitur baru dengan harga
fitur_enc = ['kota_target_enc', 'is_shm', 'akses_jalan_ordinal']
print(f"\nKorelasi fitur encoded dengan harga:")
for col in fitur_enc:
    corr = df_enc[col].corr(df_enc['harga_juta'])
    print(f"  {col:25s}: {corr:+.3f}")
```

### Langkah 7: Deteksi dan Penanganan Outlier

```python
# =============================================
# LANGKAH 7: Deteksi dan Penanganan Outlier
# =============================================

from scipy import stats

print("=" * 60)
print("DETEKSI DAN PENANGANAN OUTLIER")
print("=" * 60)

# --- 1. Metode IQR ---
print("\n--- Metode IQR ---")
kolom_target = 'harga_juta'
Q1 = df[kolom_target].quantile(0.25)
Q3 = df[kolom_target].quantile(0.75)
IQR = Q3 - Q1

batas_bawah_iqr = Q1 - 1.5 * IQR
batas_atas_iqr = Q3 + 1.5 * IQR

outliers_iqr = df[(df[kolom_target] < batas_bawah_iqr) | (df[kolom_target] > batas_atas_iqr)]
print(f"Q1 = {Q1:.0f}, Q3 = {Q3:.0f}, IQR = {IQR:.0f}")
print(f"Batas bawah: {batas_bawah_iqr:.0f}")
print(f"Batas atas : {batas_atas_iqr:.0f}")
print(f"Jumlah outlier (IQR): {len(outliers_iqr)} dari {len(df)} ({len(outliers_iqr)/len(df)*100:.1f}%)")

# --- 2. Metode Z-Score ---
print("\n--- Metode Z-Score ---")
z_scores = np.abs(stats.zscore(df[kolom_target].dropna()))
threshold_z = 3  # Z-score > 3 = outlier
outliers_zscore = df.loc[df[kolom_target].dropna().index[z_scores > threshold_z]]

print(f"Threshold z-score: {threshold_z}")
print(f"Jumlah outlier (Z-score): {len(outliers_zscore)} dari {len(df)} ({len(outliers_zscore)/len(df)*100:.1f}%)")

# --- Visualisasi ---
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Boxplot
axes[0].boxplot(df[kolom_target].dropna(), vert=True)
axes[0].axhline(batas_atas_iqr, color='red', linestyle='--', label=f'Batas IQR: {batas_atas_iqr:.0f}')
axes[0].axhline(batas_bawah_iqr, color='red', linestyle='--')
axes[0].set_title('Boxplot Harga Properti', fontsize=12)
axes[0].set_ylabel('Harga (Juta Rp)')
axes[0].legend()

# Histogram dengan batas outlier
axes[1].hist(df[kolom_target].dropna(), bins=40, color='steelblue', edgecolor='white', alpha=0.7)
axes[1].axvline(batas_atas_iqr, color='red', linestyle='--', linewidth=2, label=f'Batas IQR: {batas_atas_iqr:.0f}')
axes[1].set_title('Histogram Harga dengan Batas Outlier', fontsize=12)
axes[1].set_xlabel('Harga (Juta Rp)')
axes[1].legend()

# Z-score distribution
axes[2].hist(z_scores, bins=30, color='coral', edgecolor='white', alpha=0.7)
axes[2].axvline(threshold_z, color='red', linestyle='--', linewidth=2, label=f'Threshold: z={threshold_z}')
axes[2].set_title('Distribusi Z-Score Harga', fontsize=12)
axes[2].set_xlabel('|Z-Score|')
axes[2].legend()

plt.suptitle('Deteksi Outlier: Metode IQR vs Z-Score', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# --- Penanganan Outlier ---
print("\n--- Penanganan Outlier ---")
# Opsi 1: Hapus outlier
df_no_outlier = df[(df[kolom_target] >= batas_bawah_iqr) & (df[kolom_target] <= batas_atas_iqr)]
print(f"Opsi 1 - Hapus outlier: {len(df)} -> {len(df_no_outlier)} baris")

# Opsi 2: Capping (winsorize)
df_capped = df.copy()
df_capped[kolom_target] = df_capped[kolom_target].clip(lower=batas_bawah_iqr, upper=batas_atas_iqr)
print(f"Opsi 2 - Capping: max sebelum = {df[kolom_target].max():.0f}, max setelah = {df_capped[kolom_target].max():.0f}")

# Opsi 3: Log transform
df_log = df.copy()
df_log['harga_log'] = np.log1p(df_log[kolom_target])
print(f"Opsi 3 - Log transform: skewness sebelum = {df[kolom_target].skew():.3f}, setelah = {df_log['harga_log'].skew():.3f}")
```

### Langkah 8: Pipeline EDA Lengkap

```python
# =============================================
# LANGKAH 8: Pipeline EDA Lengkap
# =============================================

print("=" * 60)
print("RINGKASAN PIPELINE EDA")
print("=" * 60)

print(f"""
PIPELINE EDA UNTUK DATASET PROPERTI INDONESIA
{'=' * 55}

1. LOAD DATA
   - Dataset: {df.shape[0]} baris x {df.shape[1]} kolom
   - Tipe: {df.dtypes.value_counts().to_dict()}

2. STATISTICAL SUMMARY
   - Harga rata-rata : {df['harga_juta'].mean():,.0f} juta Rp
   - Harga median    : {df['harga_juta'].median():,.0f} juta Rp
   - Harga min-max   : {df['harga_juta'].min():,.0f} - {df['harga_juta'].max():,.0f} juta Rp

3. MISSING VALUES
   - Total missing: {df.isnull().sum().sum()} ({df.isnull().sum().sum()/(df.shape[0]*df.shape[1])*100:.1f}%)
   - Kolom dengan missing: {list(df.columns[df.isnull().any()])}

4. DISTRIBUSI
   - Harga: {'Right-skewed' if df['harga_juta'].skew() > 0 else 'Left-skewed'} (skew = {df['harga_juta'].skew():.3f})
   - Kota terbanyak: {df['kota'].mode()[0]}
   - Tipe terbanyak: {df['tipe_properti'].mode()[0]}

5. KORELASI DENGAN TARGET (harga_juta)
   - Korelasi tertinggi: luas_bangunan_m2 ({df['luas_bangunan_m2'].corr(df['harga_juta']):.3f})

6. OUTLIER
   - Metode IQR: {len(outliers_iqr)} outlier terdeteksi
   - Metode Z-score: {len(outliers_zscore)} outlier terdeteksi

7. FEATURE ENGINEERING
   - Fitur baru: rasio_bangunan_tanah, harga_per_m2, usia_bangunan, total_ruangan
   - Encoding: target encoding kota, binary encoding sertifikat, ordinal akses jalan
   - Polynomial features: degree 2 menghasilkan fitur interaksi

REKOMENDASI PREPROCESSING:
- Handle missing values luas_tanah dengan median per kota
- Gunakan log transform untuk harga (mengurangi skewness)
- Capping outlier lebih aman daripada menghapus
- Target encoding kota memiliki korelasi tinggi dengan harga
""")
```

---

## Tantangan Tambahan

1. **EDA E-Commerce:** Buat dataset simulasi transaksi e-commerce Indonesia (Tokopedia/Shopee) dengan fitur: kategori produk, harga, jumlah terjual, rating, kota penjual. Lakukan EDA lengkap dan identifikasi faktor yang mempengaruhi jumlah penjualan.

2. **Automated EDA Report:** Buat fungsi Python `eda_report(df, target_col)` yang otomatis menghasilkan: statistik deskriptif, visualisasi distribusi, heatmap korelasi, deteksi outlier, dan rekomendasi preprocessing. Jalankan fungsi ini pada dataset properti.

3. **Feature Selection:** Setelah membuat fitur baru, gunakan korelasi dan variance threshold untuk memilih 5 fitur terbaik untuk memprediksi harga properti. Bandingkan korelasi fitur asli vs fitur engineered.

---

## Checklist Penyelesaian

- [ ] Dataset properti Indonesia berhasil dibuat dan dimuat
- [ ] Statistical summary (describe, value_counts) berhasil dijalankan
- [ ] Distribution plots (histogram, boxplot, violin plot) berhasil ditampilkan
- [ ] Analisis korelasi (heatmap, pairplot) berhasil dibuat
- [ ] Feature creation (polynomial, interaction terms) berhasil dilakukan
- [ ] Feature encoding (target, binary, ordinal) berhasil diterapkan
- [ ] Outlier terdeteksi dan ditangani (IQR, z-score)
- [ ] Pipeline EDA lengkap berhasil dijalankan
- [ ] Notebook disimpan dengan nama `Lab04_NamaAnda_NIM.ipynb`
- [ ] Minimal 1 tantangan tambahan diselesaikan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
