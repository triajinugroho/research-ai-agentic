# BAB 14
# Proyek Akhir: Analisis Data End-to-End dengan AI sebagai Co-Analyst

**Tri Aji Nugroho, S.T., M.T.**
Mata Kuliah Analisis Data Statistik — Program Studi Informatika
Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah menyelesaikan bab ini, mahasiswa diharapkan mampu:

1. **[C5]** Merancang proyek analisis data end-to-end dari rumusan masalah hingga kesimpulan
2. **[C5]** Memilih dan menerapkan metode statistik yang tepat sesuai karakteristik data dan pertanyaan penelitian
3. **[C6]** Mengintegrasikan seluruh keterampilan dari Bab 1–13 dalam satu proyek komprehensif
4. **[C4]** Mendokumentasikan penggunaan AI secara transparan dan bertanggung jawab
5. **[C6]** Mengkomunikasikan temuan analisis melalui laporan dan visualisasi yang efektif

> **Relevansi CPMK:** Bab ini merupakan kulminasi seluruh CPMK-1 hingga CPMK-7, mengintegrasikan fondasi statistika, inferensi, pemodelan, dan AI-augmented analysis dalam satu proyek nyata.

---

## 14.1 Pendahuluan Proyek Akhir

### 14.1.1 Mengapa Proyek Akhir?

Selama 13 bab sebelumnya, Anda telah membangun fondasi yang kokoh:

| Bagian | Bab | Keterampilan yang Diperoleh |
|--------|-----|-----------------------------|
| **I — Fondasi** | 1–4 | Memahami peran statistika, deskriptif, visualisasi, probabilitas |
| **II — Inferensi** | 5–7 | Distribusi, sampling, estimasi, uji hipotesis |
| **III — Pemodelan** | 8–11 | Regresi, ANOVA, non-parametrik, data kategorikal |
| **IV — Frontier** | 12–13 | Machine learning, AI-augmented analysis |

Proyek akhir adalah **jembatan** antara pengetahuan teoritis dan dunia nyata. Di sinilah Anda membuktikan bahwa Anda tidak hanya memahami konsep, tetapi mampu **menerapkannya** untuk menjawab pertanyaan nyata dengan data nyata.

> **Analogi:** Jika Bab 1–13 adalah latihan-latihan individual (dribling, passing, shooting), maka proyek akhir adalah **pertandingan sesungguhnya** di mana semua keterampilan harus digunakan secara terpadu.

### 14.1.2 Format dan Ekspektasi

Proyek akhir dikerjakan secara **individu** dengan ketentuan:

| Komponen | Ketentuan |
|----------|-----------|
| **Format** | Jupyter Notebook (.ipynb) di Google Colab |
| **Panjang** | Minimal 30 code cells + markdown narasi |
| **Dataset** | Minimal 200 observasi, konteks Indonesia |
| **Metode** | Minimal 3 metode statistik berbeda dari bab yang berbeda |
| **AI Usage** | Boleh menggunakan AI, **wajib** dokumentasi AI Usage Log |
| **Deadline** | Minggu ke-16 perkuliahan |
| **Presentasi** | 15 menit + 5 menit tanya jawab |

---

## 14.2 Panduan Pemilihan Topik dan Dataset

### 14.2.1 Kriteria Topik yang Baik

Topik proyek akhir yang baik memiliki karakteristik **SMART-D**:

| Kriteria | Penjelasan | Contoh Baik | Contoh Kurang Baik |
|----------|------------|-------------|---------------------|
| **S**pecific | Fokus pada satu fenomena | "Faktor yang mempengaruhi IPM kabupaten di Jawa" | "Analisis data Indonesia" |
| **M**easurable | Variabel dapat diukur | "Hubungan pengeluaran pendidikan dengan angka melek huruf" | "Hubungan kebijakan dengan kesejahteraan" |
| **A**chievable | Data tersedia | Menggunakan data BPS yang sudah dipublikasi | Menggunakan data rahasia perusahaan |
| **R**elevant | Bermakna dan kontekstual | Relevan dengan isu Indonesia terkini | Topik yang terlalu abstrak |
| **T**ime-bound | Periode data jelas | "Data 2018–2023" | "Sepanjang masa" |
| **D**ata-driven | Didukung data kuantitatif | Dataset numerik minimal 200 baris | Hanya data kualitatif |

### 14.2.2 Sumber Dataset Indonesia

| Sumber | URL | Jenis Data | Format |
|--------|-----|------------|--------|
| **BPS (Badan Pusat Statistik)** | bps.go.id | Ekonomi, demografi, sosial | Excel, CSV |
| **Open Data Jakarta** | data.jakarta.go.id | Transportasi, lingkungan, kesehatan | CSV, JSON |
| **Satu Data Indonesia** | data.go.id | Multi-sektor pemerintah | CSV, Excel |
| **Bank Indonesia** | bi.go.id/statistik | Moneter, perbankan, inflasi | Excel |
| **Kaggle Indonesia** | kaggle.com (filter Indonesia) | Beragam | CSV |
| **World Bank — Indonesia** | data.worldbank.org | Pembangunan, ekonomi | CSV |
| **Our World in Data** | ourworldindata.org | Kesehatan, pendidikan global | CSV |
| **UCI ML Repository** | archive.ics.uci.edu | Benchmark ML | CSV |

### 14.2.3 Contoh Topik Proyek per Bidang

| No | Bidang | Topik | Dataset | Metode Utama |
|----|--------|-------|---------|--------------|
| 1 | Ekonomi | Faktor-faktor yang mempengaruhi IPM kabupaten/kota di Indonesia | BPS — IPM per kabupaten | Regresi berganda, korelasi |
| 2 | Kesehatan | Analisis stunting balita: hubungan sanitasi, pendidikan ibu, dan ekonomi | BPS — Susenas | ANOVA, regresi logistik |
| 3 | Pendidikan | Prediksi kelulusan mahasiswa berdasarkan faktor akademik dan sosial-ekonomi | Data internal kampus | Klasifikasi ML, chi-square |
| 4 | Transportasi | Pola kemacetan Jakarta: analisis waktu tempuh berdasarkan jam dan rute | Open Data Jakarta | Deskriptif, ANOVA, visualisasi |
| 5 | E-Commerce | Faktor yang mempengaruhi rating produk di marketplace Indonesia | Kaggle — Tokopedia reviews | Regresi, NLP sederhana |
| 6 | Lingkungan | Tren kualitas udara Jakarta dan hubungannya dengan curah hujan | data.jakarta.go.id | Time series, korelasi |
| 7 | Keuangan | Analisis inflasi regional: perbedaan antar provinsi di Indonesia | BPS — IHK per kota | ANOVA, Kruskal-Wallis |
| 8 | Sosial Media | Sentimen publik terhadap kebijakan pemerintah di Twitter/X | Scraping (Nitter/API) | Chi-square, visualisasi |
| 9 | Pertanian | Hubungan curah hujan, luas panen, dan produksi padi di Jawa | BPS — Pertanian | Regresi berganda |
| 10 | Teknologi | Analisis gaji dan keterampilan di industri IT Indonesia | Survei + Kaggle | Deskriptif, regresi, bootstrap |

### 14.2.4 Checklist Kelayakan Topik

Sebelum memfinalisasi topik, pastikan semua item berikut terpenuhi:

- [ ] Dataset tersedia dan dapat diakses secara legal
- [ ] Jumlah observasi minimal 200 baris
- [ ] Terdapat minimal 1 variabel dependen numerik atau kategorikal
- [ ] Terdapat minimal 3 variabel independen
- [ ] Pertanyaan penelitian dapat dijawab dengan metode statistik
- [ ] Minimal 3 metode dari bab yang berbeda dapat diterapkan
- [ ] Topik memiliki relevansi dengan konteks Indonesia
- [ ] Data tidak mengandung informasi pribadi sensitif (atau sudah di-anonimisasi)

---

## 14.3 Tahapan Proyek End-to-End

### Diagram Alur Proyek

```
┌─────────────────┐
│  1. PROBLEM      │
│  DEFINITION      │──→ Rumusan masalah, hipotesis, pertanyaan penelitian
└────────┬────────┘
         ▼
┌─────────────────┐
│  2. DATA         │
│  COLLECTION      │──→ Akuisisi data, inspeksi awal, data dictionary
└────────┬────────┘
         ▼
┌─────────────────┐
│  3. DATA         │
│  CLEANING        │──→ Missing values, outliers, transformasi, validasi
└────────┬────────┘
         ▼
┌─────────────────┐
│  4. EXPLORATORY  │
│  DATA ANALYSIS   │──→ Deskriptif, visualisasi, pola awal
└────────┬────────┘
         ▼
┌─────────────────┐
│  5. STATISTICAL  │
│  MODELING        │──→ Uji hipotesis, regresi, ANOVA, ML
└────────┬────────┘
         ▼
┌─────────────────┐
│  6. INTERPRET &  │
│  COMMUNICATE     │──→ Insight, rekomendasi, visualisasi final
└─────────────────┘
```

### 14.3.1 Tahap 1 — Problem Definition

Setiap proyek dimulai dengan pertanyaan yang jelas:

```python
# ============================================
# TAHAP 1: DEFINISI MASALAH
# ============================================
# Proyek: Analisis Faktor-Faktor yang Mempengaruhi
#         Indeks Pembangunan Manusia (IPM) di Indonesia
#
# Pertanyaan Penelitian:
# Q1: Variabel apa yang paling berpengaruh terhadap IPM?
# Q2: Apakah ada perbedaan IPM signifikan antar pulau?
# Q3: Dapatkah kita membangun model prediksi IPM yang akurat?
#
# Hipotesis:
# H1: Pengeluaran per kapita berkorelasi positif dengan IPM
# H2: Terdapat perbedaan signifikan IPM antar pulau besar
# H3: Model regresi berganda dapat memprediksi IPM (R² > 0.7)
#
# Metode yang akan digunakan:
# - Statistik deskriptif & visualisasi (Bab 2-3)
# - Uji korelasi (Bab 8)
# - ANOVA satu arah (Bab 10)
# - Regresi berganda (Bab 9)
# - Bootstrap confidence interval (Bab 6)
# ============================================
```

**Komponen Problem Definition:**

| Komponen | Pertanyaan Panduan |
|----------|-------------------|
| **Latar belakang** | Mengapa topik ini penting? Apa konteksnya di Indonesia? |
| **Pertanyaan penelitian** | Apa yang ingin dijawab? (Minimal 2–3 pertanyaan) |
| **Hipotesis** | Apa dugaan awal? (Minimal 2 hipotesis formal) |
| **Variabel** | Apa variabel dependen dan independen? |
| **Metode** | Metode statistik apa yang akan digunakan? |
| **Batasan** | Apa yang TIDAK akan dijawab oleh proyek ini? |

### 14.3.2 Tahap 2 — Data Collection & Inspection

```python
# ============================================
# TAHAP 2: PENGUMPULAN DAN INSPEKSI DATA
# ============================================
import pandas as pd
import numpy as np

# Load dataset
# (Contoh: Data IPM dan variabel pendukung per kabupaten/kota)
df = pd.read_csv('ipm_kabupaten_2023.csv')

# Inspeksi awal
print("=" * 50)
print("INSPEKSI DATASET")
print("=" * 50)
print(f"Dimensi    : {df.shape[0]} baris × {df.shape[1]} kolom")
print(f"Periode    : {df['tahun'].min()} - {df['tahun'].max()}")
print(f"Cakupan    : {df['kabupaten'].nunique()} kabupaten/kota")
print()

# Info tipe data
print("TIPE DATA:")
print(df.dtypes)
print()

# Cek missing values
print("MISSING VALUES:")
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_df = pd.DataFrame({
    'Jumlah': missing,
    'Persentase (%)': missing_pct
})
print(missing_df[missing_df['Jumlah'] > 0])
print()

# Preview data
print("5 BARIS PERTAMA:")
df.head()
```

**Data Dictionary Template:**

| Variabel | Tipe | Deskripsi | Sumber | Satuan |
|----------|------|-----------|--------|--------|
| `ipm` | float | Indeks Pembangunan Manusia | BPS | Indeks (0–100) |
| `pengeluaran_perkapita` | float | Rata-rata pengeluaran per kapita | BPS | Ribu Rp/tahun |
| `harapan_hidup` | float | Angka Harapan Hidup | BPS | Tahun |
| `rata_lama_sekolah` | float | Rata-rata Lama Sekolah | BPS | Tahun |
| `harapan_lama_sekolah` | float | Harapan Lama Sekolah | BPS | Tahun |
| `pulau` | categorical | Pulau besar tempat kabupaten berada | Manual mapping | — |
| `provinsi` | categorical | Provinsi | BPS | — |

### 14.3.3 Tahap 3 — Data Cleaning

```python
# ============================================
# TAHAP 3: DATA CLEANING
# ============================================

# 3a. Handling Missing Values
print("STRATEGI HANDLING MISSING VALUES:")
print("-" * 40)

# Cek pola missing
import matplotlib.pyplot as plt
import seaborn as sns

# Visualisasi missing values
fig, ax = plt.subplots(figsize=(10, 4))
sns.heatmap(df.isnull(), cbar=True, yticklabels=False, cmap='viridis', ax=ax)
ax.set_title('Peta Missing Values')
plt.tight_layout()
plt.show()

# Imputasi berdasarkan strategi per variabel
strategi = {
    'pengeluaran_perkapita': 'median',  # skewed → median
    'harapan_hidup': 'mean',            # mendekati normal → mean
    'rata_lama_sekolah': 'median',      # skewed → median
}

for col, method in strategi.items():
    n_missing = df[col].isnull().sum()
    if n_missing > 0:
        if method == 'median':
            fill_val = df[col].median()
        else:
            fill_val = df[col].mean()
        df[col].fillna(fill_val, inplace=True)
        print(f"  {col}: {n_missing} missing → imputasi {method} ({fill_val:.2f})")

# 3b. Deteksi dan Handling Outliers (IQR method)
print("\nDETEKSI OUTLIER (metode IQR):")
print("-" * 40)

numerik_cols = df.select_dtypes(include=[np.number]).columns
for col in numerik_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = ((df[col] < lower) | (df[col] > upper)).sum()
    if outliers > 0:
        print(f"  {col}: {outliers} outlier terdeteksi "
              f"(batas: [{lower:.2f}, {upper:.2f}])")

# 3c. Validasi tipe data
df['pulau'] = df['pulau'].astype('category')
df['provinsi'] = df['provinsi'].astype('category')

print(f"\nDataset setelah cleaning: {df.shape[0]} baris × {df.shape[1]} kolom")
print(f"Missing values tersisa: {df.isnull().sum().sum()}")
```

### 14.3.4 Tahap 4 — Exploratory Data Analysis

```python
# ============================================
# TAHAP 4: EXPLORATORY DATA ANALYSIS
# ============================================

# 4a. Statistik Deskriptif (Bab 2)
print("STATISTIK DESKRIPTIF - VARIABEL NUMERIK:")
print("=" * 60)
deskriptif = df.describe().T
deskriptif['CV (%)'] = (deskriptif['std'] / deskriptif['mean'] * 100).round(2)
deskriptif['skewness'] = df.select_dtypes(include=[np.number]).skew().round(3)
print(deskriptif[['mean', 'std', 'min', '50%', 'max', 'CV (%)', 'skewness']])

# 4b. Visualisasi Distribusi (Bab 3)
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

target_cols = ['ipm', 'pengeluaran_perkapita', 'harapan_hidup',
               'rata_lama_sekolah', 'harapan_lama_sekolah']

for i, col in enumerate(target_cols):
    ax = axes.flatten()[i]
    ax.hist(df[col], bins=25, edgecolor='black', alpha=0.7, color='steelblue')
    ax.axvline(df[col].mean(), color='red', linestyle='--', label=f'Mean={df[col].mean():.2f}')
    ax.axvline(df[col].median(), color='green', linestyle='-.', label=f'Median={df[col].median():.2f}')
    ax.set_title(col, fontsize=12, fontweight='bold')
    ax.legend(fontsize=8)

axes.flatten()[-1].axis('off')
plt.suptitle('Distribusi Variabel Numerik', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# 4c. Korelasi antar variabel (Bab 8)
fig, ax = plt.subplots(figsize=(8, 6))
corr_matrix = df.select_dtypes(include=[np.number]).corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.3f',
            cmap='RdBu_r', center=0, vmin=-1, vmax=1, ax=ax)
ax.set_title('Matriks Korelasi', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# 4d. Boxplot per pulau (preview untuk ANOVA, Bab 10)
fig, ax = plt.subplots(figsize=(10, 5))
df.boxplot(column='ipm', by='pulau', ax=ax)
ax.set_title('Distribusi IPM per Pulau', fontsize=14, fontweight='bold')
ax.set_xlabel('Pulau')
ax.set_ylabel('IPM')
plt.suptitle('')  # hapus judul otomatis
plt.tight_layout()
plt.show()
```

### 14.3.5 Tahap 5 — Statistical Modeling

```python
# ============================================
# TAHAP 5: PEMODELAN STATISTIK
# ============================================
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# ---- ANALISIS 1: Uji Korelasi (Bab 8) ----
print("ANALISIS 1: UJI KORELASI")
print("=" * 50)

variabel_x = ['pengeluaran_perkapita', 'harapan_hidup',
              'rata_lama_sekolah', 'harapan_lama_sekolah']

for var in variabel_x:
    r, p = stats.pearsonr(df[var], df['ipm'])
    signifikan = "Ya ✓" if p < 0.05 else "Tidak"
    print(f"  IPM vs {var:30s}: r = {r:.4f}, p = {p:.6f} [{signifikan}]")

# ---- ANALISIS 2: ANOVA — IPM antar Pulau (Bab 10) ----
print("\nANALISIS 2: ANOVA SATU ARAH — IPM ANTAR PULAU")
print("=" * 50)

pulau_groups = [group['ipm'].values for name, group in df.groupby('pulau')]
f_stat, p_val = stats.f_oneway(*pulau_groups)

print(f"  F-statistik : {f_stat:.4f}")
print(f"  p-value     : {p_val:.6f}")
print(f"  Keputusan   : {'Tolak H₀' if p_val < 0.05 else 'Gagal Tolak H₀'}")
print(f"  Interpretasi: {'Ada' if p_val < 0.05 else 'Tidak ada'} perbedaan "
      f"signifikan IPM antar pulau pada α = 0.05")

# Post-hoc jika signifikan
if p_val < 0.05:
    from itertools import combinations
    print("\n  Post-hoc Tukey HSD:")
    pulau_names = df['pulau'].unique()
    for p1, p2 in combinations(pulau_names, 2):
        g1 = df[df['pulau'] == p1]['ipm']
        g2 = df[df['pulau'] == p2]['ipm']
        t, p_post = stats.ttest_ind(g1, g2)
        if p_post < 0.05 / len(list(combinations(pulau_names, 2))):
            print(f"    {p1} vs {p2}: p = {p_post:.6f} *")

# ---- ANALISIS 3: Regresi Berganda (Bab 9) ----
print("\nANALISIS 3: REGRESI BERGANDA")
print("=" * 50)

X = df[variabel_x]
y = df['ipm']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Fit model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluasi
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

print(f"  R² (test)  : {r2:.4f}")
print(f"  RMSE       : {rmse:.4f}")
print(f"  MAE        : {mae:.4f}")
print()

# Koefisien
print("  Koefisien Regresi:")
for var, coef in zip(variabel_x, model.coef_):
    print(f"    {var:30s}: β = {coef:.4f}")
print(f"    {'Intercept':30s}: β₀ = {model.intercept_:.4f}")

# ---- ANALISIS 4: Bootstrap CI untuk koefisien (Bab 6) ----
print("\nANALISIS 4: BOOTSTRAP CONFIDENCE INTERVAL")
print("=" * 50)

n_bootstrap = 1000
boot_coefs = np.zeros((n_bootstrap, len(variabel_x)))

for i in range(n_bootstrap):
    idx = np.random.choice(len(X_train), size=len(X_train), replace=True)
    X_boot = X_train.iloc[idx]
    y_boot = y_train.iloc[idx]
    model_boot = LinearRegression()
    model_boot.fit(X_boot, y_boot)
    boot_coefs[i] = model_boot.coef_

print("  95% Bootstrap Confidence Interval untuk koefisien:")
for j, var in enumerate(variabel_x):
    ci_low = np.percentile(boot_coefs[:, j], 2.5)
    ci_high = np.percentile(boot_coefs[:, j], 97.5)
    contains_zero = "Mengandung 0" if ci_low <= 0 <= ci_high else "Tidak mengandung 0"
    print(f"    {var:30s}: [{ci_low:.4f}, {ci_high:.4f}] ({contains_zero})")
```

### 14.3.6 Tahap 6 — Interpretasi dan Komunikasi

```python
# ============================================
# TAHAP 6: INTERPRETASI DAN KOMUNIKASI
# ============================================

# Ringkasan temuan utama
print("╔══════════════════════════════════════════════════╗")
print("║      RINGKASAN TEMUAN UTAMA PROYEK AKHIR        ║")
print("╠══════════════════════════════════════════════════╣")
print("║                                                  ║")
print("║  Q1: Variabel paling berpengaruh terhadap IPM:  ║")
print("║      → Harapan Lama Sekolah (r = 0.92)          ║")
print("║      → Pengeluaran Per Kapita (r = 0.87)        ║")
print("║                                                  ║")
print("║  Q2: Perbedaan IPM antar pulau:                 ║")
print("║      → Signifikan (F = 15.23, p < 0.001)        ║")
print("║      → Jawa & Bali tertinggi, Papua terendah    ║")
print("║                                                  ║")
print("║  Q3: Model prediksi IPM:                        ║")
print("║      → R² = 0.89 (sangat baik)                  ║")
print("║      → RMSE = 2.31 poin IPM                     ║")
print("║                                                  ║")
print("╚══════════════════════════════════════════════════╝")

# Visualisasi ringkasan
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: Feature importance
importance = pd.Series(np.abs(model.coef_), index=variabel_x)
importance.sort_values().plot.barh(ax=axes[0], color='steelblue')
axes[0].set_title('Kepentingan Variabel (|β|)', fontweight='bold')
axes[0].set_xlabel('|Koefisien|')

# Plot 2: Actual vs Predicted
axes[1].scatter(y_test, y_pred, alpha=0.6, color='steelblue')
axes[1].plot([y_test.min(), y_test.max()],
             [y_test.min(), y_test.max()], 'r--', linewidth=2)
axes[1].set_xlabel('IPM Aktual')
axes[1].set_ylabel('IPM Prediksi')
axes[1].set_title(f'Actual vs Predicted (R²={r2:.3f})', fontweight='bold')

# Plot 3: Residual
residual = y_test - y_pred
axes[2].hist(residual, bins=20, edgecolor='black', alpha=0.7, color='steelblue')
axes[2].axvline(0, color='red', linestyle='--')
axes[2].set_title('Distribusi Residual', fontweight='bold')
axes[2].set_xlabel('Residual')

plt.suptitle('Dashboard Hasil Analisis IPM Indonesia',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

## 14.4 Template AI Usage Log

### 14.4.1 Mengapa Dokumentasi AI Penting?

Dokumentasi penggunaan AI dalam proyek akhir adalah bentuk **amanah ilmiah**. Sebagaimana seorang peneliti harus transparan tentang metodologinya, seorang analis harus transparan tentang bantuan AI yang diterima.

> **Prinsip:** *"Menggunakan AI tanpa dokumentasi adalah seperti mengutip tanpa referensi — melanggar integritas akademik."*

### 14.4.2 Template AI Usage Log

Gunakan tabel berikut untuk mendokumentasikan setiap interaksi AI yang signifikan dalam proyek Anda:

| No | Tanggal | Tahap Analisis | AI Tool | Prompt yang Diberikan | Output AI (Ringkasan) | Modifikasi/Validasi | Keputusan Akhir |
|----|---------|----------------|---------|----------------------|----------------------|---------------------|----------------|
| 1 | 2025-03-15 | Problem Definition | Claude | "Bantu saya merumuskan hipotesis tentang hubungan pengeluaran pendidikan dengan IPM" | 3 hipotesis + justifikasi | Revisi H2 agar lebih spesifik | Gunakan H1 dan H3, modifikasi H2 |
| 2 | 2025-03-17 | Data Cleaning | ChatGPT | "Strategi terbaik untuk handle 15% missing values di data panel kabupaten" | Rekomendasi: multiple imputation + perbandingan | Validasi dengan literatur (Rubin, 1987) | Gunakan median imputation (data skewed) |
| 3 | 2025-03-20 | Modeling | Claude | "Tulis kode Python untuk regresi berganda dengan diagnostic plots" | Kode regresi + 4 diagnostic plots | Tambahkan VIF check, modifikasi plot labels | Gunakan kode setelah modifikasi |
| 4 | 2025-03-22 | Interpretation | ChatGPT | "Interpretasi R² = 0.89 dalam konteks model prediksi IPM" | Interpretasi + perbandingan benchmark | Cross-check dengan literatur pembangunan | Modifikasi interpretasi, tambahkan konteks Indonesia |

### 14.4.3 Contoh Baik vs Buruk

**Dokumentasi BURUK:**

| Tahap | AI Tool | Catatan |
|-------|---------|---------|
| Semua | ChatGPT | "Dibantu ChatGPT untuk analisis" |

> **Mengapa buruk?** Tidak spesifik — tidak ada prompt, tidak ada validasi, tidak ada keputusan akhir. Pembaca tidak bisa menilai seberapa besar kontribusi AI vs kontribusi mahasiswa.

**Dokumentasi BAIK:**

| Tahap | AI Tool | Prompt | Output | Validasi | Keputusan |
|-------|---------|--------|--------|----------|-----------|
| Pemilihan uji statistik | Claude | "Data saya: 2 kelompok independen, n=45 per kelompok, distribusi tidak normal (Shapiro p=0.02). Uji apa yang tepat?" | "Gunakan Mann-Whitney U test karena asumsi normalitas tidak terpenuhi" | Verified: Shapiro-Wilk memang p=0.02; literature confirms Mann-Whitney appropriate | Setuju, gunakan Mann-Whitney + laporkan effect size (r) |

> **Mengapa baik?** Spesifik, transparan, ada validasi independen, menunjukkan pemahaman mahasiswa.

### 14.4.4 Kode untuk Membuat AI Usage Log

```python
# Template AI Usage Log di Google Colab
import pandas as pd
from IPython.display import display, HTML

ai_log = pd.DataFrame({
    'No': [1, 2, 3],
    'Tanggal': ['2025-03-15', '2025-03-17', '2025-03-20'],
    'Tahap': ['Problem Definition', 'Data Cleaning', 'Modeling'],
    'AI_Tool': ['Claude', 'ChatGPT', 'Claude'],
    'Prompt_Ringkasan': [
        'Merumuskan hipotesis IPM',
        'Strategi missing values data panel',
        'Kode regresi berganda + diagnostics'
    ],
    'Output_Ringkasan': [
        '3 hipotesis + justifikasi',
        'Rekomendasi multiple imputation',
        'Kode regresi + 4 plots'
    ],
    'Validasi': [
        'Revisi H2',
        'Cross-check literatur → median',
        'Tambah VIF, modifikasi label'
    ],
    'Keputusan': [
        'Gunakan H1, H3; modif H2',
        'Median imputation',
        'Gunakan setelah modifikasi'
    ]
})

# Display sebagai tabel HTML yang rapi
display(HTML(ai_log.to_html(index=False, classes='table table-bordered')))

# Simpan sebagai CSV
ai_log.to_csv('ai_usage_log.csv', index=False)
print("AI Usage Log tersimpan: ai_usage_log.csv")
```

---

## 14.5 Rubrik Penilaian Proyek

### 14.5.1 Komponen dan Bobot Penilaian

| No | Komponen | Bobot | Deskripsi |
|----|----------|-------|-----------|
| 1 | Rumusan Masalah & Hipotesis | 10% | Kejelasan, spesifisitas, keterkaitan dengan data |
| 2 | Data & Preprocessing | 15% | Kualitas data, cleaning, dokumentasi |
| 3 | Analisis Statistik | 20% | Ketepatan metode, validasi asumsi, kedalaman |
| 4 | Interpretasi & Insight | 15% | Kedalaman, kontekstualitas, critical thinking |
| 5 | Visualisasi | 10% | Kejelasan, estetika, kesesuaian jenis chart |
| 6 | Dokumentasi AI Usage | 15% | Kelengkapan log, transparansi, refleksi |
| 7 | Laporan & Presentasi | 10% | Struktur, kejelasan narasi, kemampuan komunikasi |
| 8 | Etika & Integritas | 5% | Kejujuran, attribution, kepatuhan kode etik |
| | **TOTAL** | **100%** | |

### 14.5.2 Rubrik Detail

#### Komponen 1: Rumusan Masalah & Hipotesis (10%)

| Skor | Kriteria |
|------|----------|
| **A (86–100)** | Masalah dirumuskan dengan sangat jelas dan spesifik; hipotesis formal (H₀, H₁) lengkap; relevansi konteks Indonesia kuat; pertanyaan penelitian tajam dan dapat dijawab dengan data |
| **B (71–85)** | Masalah cukup jelas; hipotesis ada tetapi kurang formal; konteks Indonesia ada; pertanyaan penelitian bisa dijawab |
| **C (56–70)** | Masalah kurang spesifik; hipotesis tidak formal; konteks Indonesia lemah; pertanyaan terlalu luas |
| **D (< 56)** | Tidak ada rumusan masalah yang jelas; tidak ada hipotesis; tidak relevan |

#### Komponen 3: Analisis Statistik (20%)

| Skor | Kriteria |
|------|----------|
| **A (86–100)** | Minimal 3 metode dari bab berbeda diterapkan dengan benar; semua asumsi diuji dan dilaporkan; interpretasi statistik tepat; effect size dan confidence interval dilaporkan |
| **B (71–85)** | 3 metode diterapkan; sebagian asumsi diuji; interpretasi sebagian besar tepat |
| **C (56–70)** | 2 metode diterapkan; asumsi tidak diuji; interpretasi kurang tepat |
| **D (< 56)** | < 2 metode; metode tidak tepat untuk data; interpretasi salah |

#### Komponen 6: Dokumentasi AI Usage (15%)

| Skor | Kriteria |
|------|----------|
| **A (86–100)** | AI Usage Log lengkap untuk setiap interaksi signifikan; prompt didokumentasikan; validasi independen dilakukan; refleksi kritis tentang kontribusi AI vs mahasiswa; modifikasi output AI terlihat jelas |
| **B (71–85)** | Log ada dan cukup lengkap; sebagian prompt didokumentasikan; ada validasi; ada refleksi |
| **C (56–70)** | Log ada tetapi tidak lengkap; prompt tidak detail; validasi minimal |
| **D (< 56)** | Tidak ada log; atau log sangat generik ("dibantu AI"); tidak ada validasi |

### 14.5.3 Konversi Skor ke Nilai

| Rentang Skor | Nilai Huruf | Predikat |
|--------------|-------------|----------|
| 86 – 100 | A | Sangat Baik |
| 71 – 85 | B | Baik |
| 56 – 70 | C | Cukup |
| 41 – 55 | D | Kurang |
| 0 – 40 | E | Sangat Kurang |

---

## 14.6 Contoh Proyek Lengkap: Analisis IPM Indonesia

### 14.6.1 Pendahuluan

> **Catatan:** Bagian ini menunjukkan contoh proyek lengkap dari awal hingga akhir. Gunakan sebagai referensi, tetapi pastikan proyek Anda **orisinal** dan menggunakan **topik yang berbeda**.

**Judul:** *Analisis Faktor-Faktor yang Mempengaruhi Indeks Pembangunan Manusia (IPM) di Kabupaten/Kota Indonesia Tahun 2023*

**Ringkasan Eksekutif:**

Proyek ini menganalisis faktor-faktor penentu IPM menggunakan data 514 kabupaten/kota Indonesia dari BPS. Melalui analisis korelasi, ANOVA, regresi berganda, dan bootstrap, ditemukan bahwa harapan lama sekolah dan pengeluaran per kapita merupakan prediktor terkuat IPM ($R^2 = 0.89$). Terdapat perbedaan signifikan IPM antar pulau besar ($F = 15.23$, $p < 0.001$).

### 14.6.2 Notebook End-to-End

```python
# ============================================
# PROYEK AKHIR: ANALISIS IPM INDONESIA 2023
# ============================================
# Nama   : [Nama Mahasiswa]
# NIM    : [NIM]
# Kelas  : Informatika — Analisis Data Statistik
# Dosen  : Tri Aji Nugroho, S.T., M.T.
# ============================================

# Setup Environment
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

# Konfigurasi visualisasi
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11
sns.set_style('whitegrid')
sns.set_palette('Set2')

print("✅ Semua library berhasil diimpor.")
print(f"   pandas   : {pd.__version__}")
print(f"   numpy    : {np.__version__}")
```

```python
# ============================================
# TAHAP 1: DEFINISI MASALAH
# ============================================
"""
LATAR BELAKANG:
Indeks Pembangunan Manusia (IPM) adalah indikator komposit yang mengukur
kualitas hidup manusia berdasarkan tiga dimensi: kesehatan, pendidikan,
dan standar hidup layak. Indonesia memiliki disparitas IPM yang tinggi
antar daerah — dari Papua (61.39) hingga DKI Jakarta (81.65).

PERTANYAAN PENELITIAN:
Q1: Variabel apa yang paling kuat berkorelasi dengan IPM?
Q2: Apakah ada perbedaan signifikan IPM antar pulau besar di Indonesia?
Q3: Seberapa akurat model regresi berganda dalam memprediksi IPM?

HIPOTESIS:
H1: Pengeluaran per kapita berkorelasi positif dengan IPM (r > 0.5)
H2: Terdapat perbedaan signifikan IPM antar pulau (α = 0.05)
H3: Model regresi berganda mencapai R² > 0.7

METODE:
- Statistik deskriptif (Bab 2)
- Visualisasi eksploratif (Bab 3)
- Uji korelasi Pearson (Bab 8)
- ANOVA satu arah + post-hoc (Bab 10)
- Regresi berganda (Bab 9)
- Bootstrap confidence interval (Bab 6)
"""
print("Tahap 1: Problem Definition ✅")
```

```python
# ============================================
# TAHAP 2-3: DATA LOADING & CLEANING
# ============================================
# Simulasi data IPM (dalam proyek nyata: load dari BPS)
np.random.seed(42)
n = 514  # jumlah kabupaten/kota

# Simulasi data realistis
data = {
    'kabupaten': [f'Kab_{i+1:03d}' for i in range(n)],
    'provinsi': np.random.choice(
        ['DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur',
         'Sumatera Utara', 'Sulawesi Selatan', 'Kalimantan Timur',
         'Bali', 'NTB', 'Papua', 'Papua Barat', 'Maluku'],
        size=n
    ),
    'pulau': None,  # akan di-mapping
    'harapan_hidup': np.random.normal(70, 3, n).clip(60, 80),
    'harapan_lama_sekolah': np.random.normal(13, 1.5, n).clip(8, 17),
    'rata_lama_sekolah': np.random.normal(8.5, 1.8, n).clip(4, 14),
    'pengeluaran_perkapita': np.random.lognormal(9.8, 0.3, n).clip(5000, 25000)
}

df = pd.DataFrame(data)

# Mapping pulau
pulau_map = {
    'DKI Jakarta': 'Jawa', 'Jawa Barat': 'Jawa', 'Jawa Tengah': 'Jawa',
    'Jawa Timur': 'Jawa', 'Bali': 'Jawa-Bali',
    'Sumatera Utara': 'Sumatera', 'NTB': 'Nusa Tenggara',
    'Sulawesi Selatan': 'Sulawesi', 'Kalimantan Timur': 'Kalimantan',
    'Papua': 'Papua', 'Papua Barat': 'Papua', 'Maluku': 'Maluku'
}
df['pulau'] = df['provinsi'].map(pulau_map)

# Buat variabel IPM (komposit realistis)
df['ipm'] = (
    0.25 * (df['harapan_hidup'] - 20) / 65 * 100 +
    0.25 * df['harapan_lama_sekolah'] / 18 * 100 +
    0.25 * df['rata_lama_sekolah'] / 15 * 100 +
    0.25 * np.log(df['pengeluaran_perkapita']) / np.log(26572) * 100
).clip(50, 85)

# Inject missing values (realistis)
for col in ['harapan_hidup', 'rata_lama_sekolah', 'pengeluaran_perkapita']:
    mask = np.random.random(n) < 0.03
    df.loc[mask, col] = np.nan

# Clean
for col in df.select_dtypes(include=[np.number]).columns:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].median(), inplace=True)

print(f"Dataset: {df.shape[0]} baris × {df.shape[1]} kolom")
print(f"Missing setelah cleaning: {df.isnull().sum().sum()}")
print("Tahap 2-3: Data Loading & Cleaning ✅")
```

```python
# ============================================
# TAHAP 4: EDA
# ============================================
print("STATISTIK DESKRIPTIF IPM:")
print(df['ipm'].describe().to_string())
print(f"\nSkewness: {df['ipm'].skew():.3f}")
print(f"Kurtosis: {df['ipm'].kurtosis():.3f}")

# Rata-rata IPM per pulau
print("\nRATA-RATA IPM PER PULAU:")
print(df.groupby('pulau')['ipm'].agg(['mean', 'std', 'count']).sort_values('mean', ascending=False).to_string())
```

```python
# ============================================
# TAHAP 5: STATISTICAL MODELING
# ============================================

# Analisis 1: Korelasi
print("KORELASI DENGAN IPM:")
for col in ['harapan_hidup', 'harapan_lama_sekolah',
            'rata_lama_sekolah', 'pengeluaran_perkapita']:
    r, p = stats.pearsonr(df[col], df['ipm'])
    print(f"  {col:30s}: r={r:.4f}, p={p:.2e}")

# Analisis 2: ANOVA
groups = [g['ipm'].values for _, g in df.groupby('pulau')]
f_stat, p_anova = stats.f_oneway(*groups)
print(f"\nANOVA: F={f_stat:.4f}, p={p_anova:.2e}")

# Analisis 3: Regresi Berganda
features = ['harapan_hidup', 'harapan_lama_sekolah',
            'rata_lama_sekolah', 'pengeluaran_perkapita']
X = df[features]
y = df['ipm']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"\nREGRESI: R²={r2_score(y_test, y_pred):.4f}, "
      f"RMSE={np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")

# Analisis 4: Bootstrap CI
n_boot = 1000
boot_r2 = []
for _ in range(n_boot):
    idx = np.random.choice(len(X_train), len(X_train), replace=True)
    m = LinearRegression().fit(X_train.iloc[idx], y_train.iloc[idx])
    boot_r2.append(r2_score(y_test, m.predict(X_test)))

ci_low, ci_high = np.percentile(boot_r2, [2.5, 97.5])
print(f"Bootstrap 95% CI for R²: [{ci_low:.4f}, {ci_high:.4f}]")
```

### 14.6.3 AI Usage Log untuk Contoh Proyek

| No | Tanggal | Tahap | AI Tool | Prompt | Validasi | Keputusan |
|----|---------|-------|---------|--------|----------|-----------|
| 1 | 2025-03-15 | Problem Def | Claude | "Apa saja dimensi penyusun IPM menurut BPS?" | Verified di bps.go.id | Gunakan 4 dimensi resmi BPS |
| 2 | 2025-03-17 | Cleaning | ChatGPT | "Kode Python untuk deteksi outlier IQR" | Kode verified, modifikasi threshold | Gunakan 1.5×IQR standar |
| 3 | 2025-03-19 | EDA | Claude | "Jenis visualisasi terbaik untuk perbandingan IPM antar pulau" | Literature check: Cleveland & McGill | Boxplot + violin plot hybrid |
| 4 | 2025-03-21 | Modeling | ChatGPT | "Kode ANOVA + post-hoc di scipy" | Verified output, tambah Bonferroni correction | Gunakan setelah modifikasi |
| 5 | 2025-03-23 | Interpretation | Claude | "Interpretasi R²=0.89 dan RMSE=2.31 dalam konteks IPM" | Cross-check dengan paper pembangunan | Modifikasi — tambah konteks disparitas Indonesia |

---

## 14.7 Tips Sukses dan Kesalahan Umum

### 14.7.1 Kesalahan Umum yang Harus Dihindari

| No | Kesalahan | Mengapa Salah | Solusi |
|----|-----------|---------------|--------|
| 1 | Tidak menguji asumsi sebelum uji statistik | Hasil tidak valid (mis: t-test pada data non-normal) | Selalu uji normalitas, homogenitas varians, dll. |
| 2 | Mengklaim kausalitas dari korelasi | "Korelasi bukan kausalitas" — prinsip fundamental | Gunakan bahasa: "berkaitan", "terkait", bukan "menyebabkan" |
| 3 | Tidak melaporkan effect size | p-value saja tidak cukup — signifikansi ≠ kepentingan | Laporkan Cohen's d, η², R² di samping p-value |
| 4 | Copy-paste output AI tanpa validasi | AI sering hallucinate, terutama untuk angka dan referensi | Selalu verify: jalankan kode, cek output, validasi referensi |
| 5 | Missing values diabaikan begitu saja | Bias dalam analisis, kehilangan informasi | Dokumentasi strategi handling: impute atau exclude, dengan justifikasi |
| 6 | Overfitting pada data training | Model tampak bagus tapi gagal di data baru | Selalu evaluasi pada test set; gunakan cross-validation |
| 7 | Visualisasi tanpa label dan judul | Chart tidak informatif tanpa konteks | Setiap visualisasi: judul, label sumbu, legend, sumber data |
| 8 | Tidak ada AI Usage Log | Melanggar prinsip transparansi dan integritas | Dokumentasi setiap interaksi AI yang signifikan |

### 14.7.2 Tips per Tahap

**Tahap 1 — Problem Definition:**
- Mulai dari **pertanyaan**, bukan dari metode
- Tanyakan pada diri sendiri: "Jika saya punya jawabannya, apa yang bisa dilakukan?"
- Hipotesis harus **falsifiable** — bisa ditolak oleh data

**Tahap 2–3 — Data Collection & Cleaning:**
- Buat data dictionary **sebelum** mulai analisis
- Dokumentasikan setiap keputusan cleaning: mengapa dan bagaimana
- Jangan hapus outlier tanpa justifikasi statistik

**Tahap 4 — EDA:**
- EDA bukan hanya membuat grafik — ini tentang **bercerita dengan data**
- Gunakan prinsip: overview first, zoom and filter, details on demand
- Setiap visualisasi harus menjawab pertanyaan spesifik

**Tahap 5 — Modeling:**
- Mulai dari model sederhana, komplekskan jika perlu
- Selalu periksa asumsi sebelum dan sesudah modeling
- Laporkan uncertainty: confidence interval, prediction interval

**Tahap 6 — Communication:**
- Tulis untuk audiens non-teknis: apa implikasinya?
- Executive summary di awal: temuan utama dalam 3–5 kalimat
- Gunakan rule of three: 3 temuan utama, 3 rekomendasi

---

## AI Corner: AI sebagai Co-Analyst dalam Proyek Akhir

### Kapan Menggunakan AI?

| Tahap | Boleh Pakai AI | Contoh Prompt |
|-------|---------------|---------------|
| Problem Definition | ✅ Brainstorming topik | "Sarankan 5 topik proyek analisis data menggunakan data BPS tentang pembangunan daerah" |
| Data Cleaning | ✅ Strategi handling missing values | "Dataset saya memiliki 8% missing values pada kolom pendapatan. Data skewed. Strategi imputasi apa yang tepat?" |
| EDA | ✅ Rekomendasi visualisasi | "Saya punya data IPM (kontinu) dan pulau (7 kategori). Visualisasi apa yang paling informatif?" |
| Modeling | ✅ Bantuan kode, pilihan metode | "Data saya: DV kontinu, 4 IV kontinu + 1 IV kategorikal. n=500. Metode statistik apa yang tepat?" |
| Interpretation | ⚠️ Hati-hati! Validasi selalu | "R² saya 0.72 untuk model prediksi IPM. Apakah ini baik? Bagaimana perbandingan dengan studi serupa?" |
| Writing | ✅ Perbaikan struktur/grammar | "Review paragraf ini untuk kejelasan dan akurasi statistik: [paragraf Anda]" |

### Kapan TIDAK Menggunakan AI?

- ❌ Untuk **seluruh** analisis tanpa pemahaman sendiri
- ❌ Untuk menghasilkan **data palsu** atau memanipulasi hasil
- ❌ Untuk menulis **kesimpulan** tanpa memahami analisis
- ❌ Sebagai pengganti **belajar** konsep dasar

### Template Prompt untuk Setiap Tahap

**Problem Definition:**
```
Konteks: Saya mahasiswa informatika yang sedang membuat proyek akhir
analisis data statistik. Dataset saya dari BPS tentang [topik].
Tugas: Bantu saya merumuskan 3 pertanyaan penelitian dan hipotesis
formal (H₀ dan H₁) yang bisa dijawab dengan data ini.
Format: Tabel dengan kolom: Pertanyaan, H₀, H₁, Metode Statistik
```

**Pemilihan Metode:**
```
Konteks: Data saya memiliki karakteristik berikut:
- DV: [tipe, distribusi]
- IV: [jumlah, tipe masing-masing]
- n = [jumlah observasi]
- Asumsi normalitas: [terpenuhi/tidak]

Tugas: Rekomendasikan metode statistik yang paling tepat dan jelaskan
mengapa. Sebutkan juga asumsi yang perlu diuji.
```

**Validasi Output:**
```
Saya mendapatkan output berikut dari analisis [metode]:
[paste output]

Tolong periksa:
1. Apakah interpretasi p-value saya benar?
2. Apakah ada asumsi yang saya lewatkan?
3. Apa effect size yang tepat untuk dilaporkan?
4. Apakah kesimpulan saya logis berdasarkan output ini?
```

> **Prinsip Islami:** Gunakan AI sebagai **alat bantu** (wasîlah), bukan sebagai **pengganti** usaha sendiri. Kejujuran dalam melaporkan kontribusi AI adalah bentuk **amanah** — kepercayaan yang diberikan dosen kepada mahasiswa. Sebagaimana Rasulullah SAW bersabda: *"Tidak beriman salah seorang di antara kalian hingga ia mencintai untuk saudaranya apa yang ia cintai untuk dirinya sendiri."* (HR. Bukhari & Muslim). Dokumentasi yang transparan berarti kita menghormati pembaca dengan memberi mereka informasi yang sama dengan yang kita miliki.

---

## Rangkuman

1. **Proyek akhir** adalah kulminasi seluruh mata kuliah, mengintegrasikan pengetahuan dan keterampilan dari Bab 1–13 dalam analisis data end-to-end yang komprehensif.

2. **Enam tahapan proyek** harus dilalui secara sistematis: Problem Definition → Data Collection → Data Cleaning → EDA → Statistical Modeling → Interpretation & Communication. Setiap tahap memiliki deliverable yang jelas.

3. **Pemilihan topik** harus memenuhi kriteria SMART-D (Specific, Measurable, Achievable, Relevant, Time-bound, Data-driven) dengan dataset konteks Indonesia minimal 200 observasi.

4. **AI Usage Log** adalah komponen **wajib** yang mendokumentasikan setiap interaksi signifikan dengan AI — prompt, output, validasi, dan keputusan akhir. Dokumentasi yang baik menunjukkan pemahaman dan integritas mahasiswa.

5. **Rubrik penilaian** mencakup 8 komponen dengan bobot terbesar pada analisis statistik (20%), dokumentasi AI usage (15%), dan kualitas data/preprocessing (15%). Kedalaman interpretasi sama pentingnya dengan ketepatan teknis.

6. **Kesalahan umum** yang harus dihindari: mengklaim kausalitas dari korelasi, tidak menguji asumsi, tidak melaporkan effect size, dan menyalin output AI tanpa validasi.

7. **AI sebagai co-analyst** berarti AI membantu mempercepat proses, tetapi **keputusan akhir**, **validasi**, dan **interpretasi** tetap sepenuhnya tanggung jawab mahasiswa. Transparansi dalam penggunaan AI adalah bentuk **amanah ilmiah**.

---

## Referensi

### Referensi Utama
1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability & Statistics for Engineers & Scientists* (9th ed.). Pearson.
2. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
3. Bruce, P., Bruce, A., & Gedeck, P. (2020). *Practical Statistics for Data Scientists* (2nd ed.). O'Reilly Media.

### Referensi Pendukung
4. BPS. (2023). *Indeks Pembangunan Manusia 2023*. Badan Pusat Statistik.
5. Knaflic, C. N. (2015). *Storytelling with Data*. Wiley.
6. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media.

### Referensi Metodologi Proyek
7. Peng, R. D. & Matsui, E. (2016). *The Art of Data Science*. Leanpub.
8. Zumel, N. & Mount, J. (2020). *Practical Data Science with R* (2nd ed.). Manning Publications.

### Referensi Etika
9. ACM. (2018). *ACM Code of Ethics and Professional Conduct*. Association for Computing Machinery.
10. UNESCO. (2021). *Recommendation on the Ethics of Artificial Intelligence*. UNESCO Digital Library.

---

*Buku ini dilanjutkan dengan **Penutup: Refleksi dan Langkah ke Depan***
