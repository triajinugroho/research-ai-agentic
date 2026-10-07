# Lab 10: Regresi Berganda dan Evaluasi Model

**Mata Kuliah:** Statistika — Universitas Al Azhar Indonesia
**Minggu:** 10
**Platform:** Google Colab (Python)

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. Membangun model regresi berganda (*multiple linear regression*) dengan `scikit-learn`
2. Membaca dan menginterpretasikan output OLS summary dari `statsmodels`
3. Melakukan diagnostik model: residual plot, Q-Q plot, dan VIF
4. Membandingkan model sederhana vs berganda menggunakan R² dan adjusted R²
5. Menginterpretasikan feature importance dalam konteks data

---

## Persiapan

### Library yang Dibutuhkan

```python
# Jalankan cell ini terlebih dahulu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# scikit-learn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# statsmodels
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Pengaturan
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
pd.set_option('display.max_columns', 20)

print("Semua library berhasil dimuat!")
```

### Konsep Singkat

**Regresi berganda** memperluas regresi sederhana dengan menggunakan lebih dari satu variabel independen:

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_p X_p + \epsilon$$

**Adjusted R²** memperhitungkan jumlah prediktor sehingga lebih adil untuk perbandingan model:

$$R^2_{adj} = 1 - \frac{(1 - R^2)(n - 1)}{n - p - 1}$$

---

## Langkah-langkah Praktikum

### Langkah 1: Membuat Dataset

```python
# Data simulasi: faktor-faktor yang mempengaruhi IPK mahasiswa
np.random.seed(2024)
n = 150

jam_belajar = np.random.uniform(5, 30, n)          # jam per minggu
kehadiran = np.random.uniform(50, 100, n)           # persentase
jam_tidur = np.random.uniform(4, 9, n)              # jam per hari
penghasilan_ortu = np.random.uniform(3, 25, n)      # juta per bulan
jarak_kampus = np.random.uniform(1, 40, n)          # km

# IPK dipengaruhi oleh jam_belajar, kehadiran, dan jam_tidur
# penghasilan_ortu dan jarak_kampus memiliki pengaruh kecil
ipk = (
    1.5
    + 0.03 * jam_belajar
    + 0.012 * kehadiran
    + 0.08 * jam_tidur
    + 0.005 * penghasilan_ortu
    - 0.002 * jarak_kampus
    + np.random.normal(0, 0.15, n)
)
ipk = np.clip(ipk, 1.0, 4.0)  # batasi IPK antara 1.0 - 4.0

data = pd.DataFrame({
    'jam_belajar': np.round(jam_belajar, 1),
    'kehadiran_persen': np.round(kehadiran, 1),
    'jam_tidur': np.round(jam_tidur, 1),
    'penghasilan_ortu_juta': np.round(penghasilan_ortu, 1),
    'jarak_kampus_km': np.round(jarak_kampus, 1),
    'ipk': np.round(ipk, 2)
})

print("=== Dataset: Faktor yang Mempengaruhi IPK Mahasiswa ===")
print(f"Jumlah data: {len(data)}")
print()
data.head(10)
```

### Langkah 2: Eksplorasi Data

```python
# Statistik deskriptif
print("=== Statistik Deskriptif ===")
data.describe().round(2)
```

```python
# Correlation heatmap
plt.figure(figsize=(10, 8))
corr_matrix = data.corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.3f',
            cmap='RdBu_r', center=0, square=True,
            linewidths=1, cbar_kws={'shrink': 0.8})
plt.title('Matriks Korelasi Antar Variabel')
plt.tight_layout()
plt.show()
```

```python
# Pair plot untuk melihat hubungan antar variabel
sns.pairplot(data, y_vars=['ipk'],
             x_vars=['jam_belajar', 'kehadiran_persen', 'jam_tidur',
                     'penghasilan_ortu_juta', 'jarak_kampus_km'],
             height=3, aspect=1.2)
plt.suptitle('Hubungan Setiap Variabel dengan IPK', y=1.02)
plt.tight_layout()
plt.show()
```

### Langkah 3: Model Regresi Sederhana (Baseline)

```python
# Model sederhana: hanya jam_belajar sebagai prediktor
X_simple = data[['jam_belajar']]
y = data['ipk']

model_simple = LinearRegression()
model_simple.fit(X_simple, y)

print("=== Model Regresi Sederhana (1 prediktor) ===")
print(f"Variabel: jam_belajar")
print(f"Intercept : {model_simple.intercept_:.4f}")
print(f"Slope     : {model_simple.coef_[0]:.4f}")
print(f"R²        : {model_simple.score(X_simple, y):.4f}")
```

### Langkah 4: Model Regresi Berganda dengan scikit-learn

```python
# Model berganda: semua prediktor
fitur = ['jam_belajar', 'kehadiran_persen', 'jam_tidur',
         'penghasilan_ortu_juta', 'jarak_kampus_km']
X = data[fitur]
y = data['ipk']

model_multi = LinearRegression()
model_multi.fit(X, y)

print("=== Model Regresi Berganda (5 prediktor) ===")
print(f"Intercept: {model_multi.intercept_:.4f}")
print()
print("Koefisien:")
for nama, koef in zip(fitur, model_multi.coef_):
    print(f"  {nama:25s}: {koef:.6f}")
print()
print(f"R² Score: {model_multi.score(X, y):.4f}")
```

### Langkah 5: Analisis dengan statsmodels OLS

```python
# statsmodels membutuhkan penambahan konstanta secara manual
X_sm = sm.add_constant(X)
model_ols = sm.OLS(y, X_sm).fit()

# Tampilkan summary lengkap
print(model_ols.summary())
```

```python
# Cara membaca OLS Summary
print("""
=== Panduan Membaca OLS Summary ===

1. R-squared vs Adj. R-squared:
   - R² selalu naik jika menambah variabel (meskipun tidak berguna)
   - Adj. R² memperhitungkan jumlah variabel — gunakan ini untuk perbandingan

2. F-statistic dan Prob (F-statistic):
   - Menguji apakah model secara keseluruhan signifikan
   - Jika Prob < 0.05, minimal satu prediktor berpengaruh signifikan

3. Koefisien (coef):
   - Setiap koefisien menunjukkan perubahan Y untuk setiap kenaikan 1 unit X
   - Sambil mengontrol variabel lain tetap konstan (ceteris paribus)

4. P>|t| (p-value per koefisien):
   - < 0.05 → signifikan (berpengaruh)
   - ≥ 0.05 → tidak signifikan

5. [0.025  0.975] → 95% confidence interval untuk koefisien
""")
```

```python
# Identifikasi variabel signifikan
print("=== Signifikansi Variabel (α = 0.05) ===")
for var in fitur:
    p_val = model_ols.pvalues[var]
    sig = "✓ Signifikan" if p_val < 0.05 else "✗ Tidak Signifikan"
    print(f"  {var:25s}: p = {p_val:.4f} → {sig}")
```

### Langkah 6: Diagnostik Model

```python
# Prediksi dan residual
y_pred = model_ols.predict(X_sm)
residual = y - y_pred

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Residual vs Fitted
axes[0, 0].scatter(y_pred, residual, alpha=0.6, color='steelblue')
axes[0, 0].axhline(y=0, color='red', linestyle='--')
axes[0, 0].set_xlabel('Fitted Values')
axes[0, 0].set_ylabel('Residuals')
axes[0, 0].set_title('Residual vs Fitted')

# 2. Q-Q Plot
stats.probplot(residual, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('Normal Q-Q Plot')

# 3. Histogram Residual
axes[1, 0].hist(residual, bins=20, color='steelblue', edgecolor='navy', alpha=0.7)
axes[1, 0].set_xlabel('Residual')
axes[1, 0].set_ylabel('Frekuensi')
axes[1, 0].set_title('Distribusi Residual')

# 4. Scale-Location Plot
std_residual = residual / residual.std()
axes[1, 1].scatter(y_pred, np.sqrt(np.abs(std_residual)), alpha=0.6, color='steelblue')
axes[1, 1].set_xlabel('Fitted Values')
axes[1, 1].set_ylabel('√|Standardized Residuals|')
axes[1, 1].set_title('Scale-Location Plot')

plt.suptitle('Diagnostik Model Regresi', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Langkah 7: Menghitung VIF (Variance Inflation Factor)

```python
# VIF mengukur multikolinearitas antar variabel independen
# VIF > 5 → multikolinearitas moderat
# VIF > 10 → multikolinearitas serius

vif_data = pd.DataFrame()
vif_data['Variabel'] = fitur
vif_data['VIF'] = [
    variance_inflation_factor(X.values, i) for i in range(len(fitur))
]
vif_data['Interpretasi'] = vif_data['VIF'].apply(
    lambda x: 'Aman' if x < 5 else ('Moderat' if x < 10 else 'Serius!')
)

print("=== Variance Inflation Factor (VIF) ===")
print(vif_data.to_string(index=False))
print()
print("Catatan: VIF > 5 mengindikasikan potensi multikolinearitas.")
```

### Langkah 8: Perbandingan Model

```python
# Bandingkan model sederhana vs berganda
# Hitung adjusted R² manual untuk sklearn model
def adjusted_r2(r2, n, p):
    """Menghitung Adjusted R²."""
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)

n_obs = len(y)

# Model sederhana
r2_simple = model_simple.score(X_simple, y)
adj_r2_simple = adjusted_r2(r2_simple, n_obs, 1)

# Model berganda
r2_multi = model_multi.score(X, y)
adj_r2_multi = adjusted_r2(r2_multi, n_obs, 5)

# Model hanya variabel signifikan
fitur_sig = [var for var in fitur if model_ols.pvalues[var] < 0.05]
X_sig = data[fitur_sig]
model_sig = LinearRegression()
model_sig.fit(X_sig, y)
r2_sig = model_sig.score(X_sig, y)
adj_r2_sig = adjusted_r2(r2_sig, n_obs, len(fitur_sig))

# Tabel perbandingan
perbandingan = pd.DataFrame({
    'Model': ['Sederhana (1 var)', 'Berganda (5 var)', f'Signifikan ({len(fitur_sig)} var)'],
    'R²': [r2_simple, r2_multi, r2_sig],
    'Adjusted R²': [adj_r2_simple, adj_r2_multi, adj_r2_sig],
    'Jumlah Prediktor': [1, 5, len(fitur_sig)]
})

print("=== Perbandingan Model ===")
print(perbandingan.to_string(index=False))
print()
print(f"Variabel signifikan yang digunakan: {fitur_sig}")
```

### Langkah 9: Feature Importance

```python
# Visualisasi feature importance berdasarkan koefisien terstandarisasi
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model_scaled = LinearRegression()
model_scaled.fit(X_scaled, y)

# Koefisien terstandarisasi memungkinkan perbandingan langsung
importance = pd.DataFrame({
    'Variabel': fitur,
    'Koef_Terstandarisasi': model_scaled.coef_,
    'Abs_Koef': np.abs(model_scaled.coef_)
}).sort_values('Abs_Koef', ascending=True)

plt.figure(figsize=(10, 6))
colors = ['green' if x > 0 else 'red' for x in importance['Koef_Terstandarisasi']]
plt.barh(importance['Variabel'], importance['Koef_Terstandarisasi'], color=colors, alpha=0.7)
plt.xlabel('Koefisien Terstandarisasi')
plt.title('Feature Importance (Koefisien Terstandarisasi)\nHijau = positif, Merah = negatif')
plt.axvline(x=0, color='black', linewidth=0.5)
plt.tight_layout()
plt.show()

print("Interpretasi: Variabel dengan koefisien terstandarisasi terbesar")
print("(dalam nilai absolut) memiliki pengaruh paling besar terhadap IPK.")
```

### Langkah 10: Prediksi dengan Model Terbaik

```python
# Prediksi untuk profil mahasiswa tertentu
profil_mahasiswa = pd.DataFrame({
    'jam_belajar': [15, 25, 8],
    'kehadiran_persen': [85, 95, 60],
    'jam_tidur': [7, 7.5, 5],
    'penghasilan_ortu_juta': [10, 15, 8],
    'jarak_kampus_km': [10, 5, 30]
})

prediksi_ipk = model_multi.predict(profil_mahasiswa)

print("=== Prediksi IPK untuk Profil Mahasiswa ===")
for i, (_, row) in enumerate(profil_mahasiswa.iterrows()):
    print(f"\nMahasiswa {i+1}:")
    print(f"  Jam belajar/minggu : {row['jam_belajar']}")
    print(f"  Kehadiran          : {row['kehadiran_persen']}%")
    print(f"  Jam tidur/hari     : {row['jam_tidur']}")
    print(f"  IPK Prediksi       : {prediksi_ipk[i]:.2f}")
```

---

## Tugas yang Harus Dikumpulkan

Buat notebook Google Colab yang berisi:

1. **Dataset dan Eksplorasi** (15 poin)
   - Gunakan dataset dengan minimal 4 variabel independen
   - Buat correlation heatmap dan interpretasikan

2. **Model Regresi Berganda** (25 poin)
   - Bangun model dengan `sklearn` dan `statsmodels`
   - Tampilkan OLS summary dan jelaskan setiap bagian

3. **Diagnostik Model** (25 poin)
   - Buat 4 plot diagnostik (residual, Q-Q, histogram, scale-location)
   - Hitung VIF dan interpretasikan hasilnya
   - Apakah asumsi-asumsi regresi terpenuhi?

4. **Perbandingan Model** (20 poin)
   - Bandingkan minimal 2 model (sederhana vs berganda)
   - Gunakan R² dan Adjusted R² untuk evaluasi
   - Jelaskan mengapa Adjusted R² lebih baik untuk perbandingan

5. **Feature Importance** (15 poin)
   - Buat visualisasi koefisien terstandarisasi
   - Variabel mana yang paling berpengaruh? Mengapa?

**Format:** File `.ipynb` diunggah ke Google Classroom
**Deadline:** Satu minggu setelah pertemuan praktikum

---

## Challenge / Bonus

1. **Gunakan dataset California Housing** dari `sklearn.datasets` (`fetch_california_housing`). Bangun model regresi berganda dan lakukan diagnostik lengkap.

2. **Implementasikan stepwise regression**: mulai dari semua variabel, lalu hapus variabel yang tidak signifikan satu per satu. Bandingkan adjusted R² pada setiap langkah.

3. **Tambahkan interaksi variabel**: Buat variabel baru `jam_belajar × kehadiran_persen` dan lihat apakah model membaik.
