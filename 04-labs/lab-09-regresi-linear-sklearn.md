# Lab 09: Regresi Linear dengan scikit-learn

**Mata Kuliah:** Statistika — Universitas Al Azhar Indonesia
**Minggu:** 9
**Platform:** Google Colab (Python)

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. Memahami konsep regresi linear sederhana (*simple linear regression*)
2. Menghitung korelasi Pearson dan Spearman menggunakan Python
3. Membangun model regresi linear dengan `scikit-learn`
4. Memvisualisasikan garis regresi dan residual
5. Menginterpretasikan slope, intercept, dan R² dalam konteks data nyata

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
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Pengaturan visualisasi
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("Semua library berhasil dimuat!")
```

### Konsep Singkat

**Regresi linear sederhana** memodelkan hubungan antara satu variabel independen (X) dan satu variabel dependen (Y):

$$Y = \beta_0 + \beta_1 X + \epsilon$$

Di mana:
- $\beta_0$ = intercept (nilai Y ketika X = 0)
- $\beta_1$ = slope (perubahan Y untuk setiap kenaikan 1 unit X)
- $\epsilon$ = error (residual)

---

## Langkah-langkah Praktikum

### Langkah 1: Membuat Dataset Ekonomi Indonesia

Kita akan menggunakan data simulasi yang merepresentasikan indikator ekonomi Indonesia.

```python
# Data simulasi: PDB per kapita dan angka harapan hidup provinsi di Indonesia
np.random.seed(42)

n = 34  # jumlah provinsi

# PDB per kapita (dalam juta rupiah)
pdb_per_kapita = np.random.uniform(15, 120, n)
pdb_per_kapita = np.sort(pdb_per_kapita)

# Angka harapan hidup (tahun) — berkorelasi positif dengan PDB
angka_harapan_hidup = 62 + 0.08 * pdb_per_kapita + np.random.normal(0, 1.5, n)

# Buat DataFrame
data = pd.DataFrame({
    'provinsi': [f'Provinsi_{i+1}' for i in range(n)],
    'pdb_per_kapita_juta': np.round(pdb_per_kapita, 2),
    'angka_harapan_hidup': np.round(angka_harapan_hidup, 2)
})

print("=== Data Ekonomi Indonesia (Simulasi) ===")
print(f"Jumlah observasi: {len(data)}")
print()
data.head(10)
```

### Langkah 2: Eksplorasi Data Awal

```python
# Statistik deskriptif
print("=== Statistik Deskriptif ===")
print(data[['pdb_per_kapita_juta', 'angka_harapan_hidup']].describe())
```

```python
# Scatter plot awal
plt.figure(figsize=(10, 6))
plt.scatter(data['pdb_per_kapita_juta'], data['angka_harapan_hidup'],
            color='steelblue', s=80, alpha=0.7, edgecolors='navy')
plt.xlabel('PDB per Kapita (Juta Rupiah)')
plt.ylabel('Angka Harapan Hidup (Tahun)')
plt.title('Hubungan PDB per Kapita dan Angka Harapan Hidup\n(Data Simulasi Provinsi Indonesia)')
plt.tight_layout()
plt.show()
```

**Pertanyaan:** Berdasarkan scatter plot, bagaimana pola hubungan kedua variabel ini?

### Langkah 3: Menghitung Korelasi

```python
# Korelasi Pearson (mengukur hubungan linear)
pearson_r, pearson_p = stats.pearsonr(
    data['pdb_per_kapita_juta'],
    data['angka_harapan_hidup']
)
print(f"Korelasi Pearson (r)  : {pearson_r:.4f}")
print(f"p-value               : {pearson_p:.6f}")
print()

# Korelasi Spearman (mengukur hubungan monoton, berbasis rank)
spearman_r, spearman_p = stats.spearmanr(
    data['pdb_per_kapita_juta'],
    data['angka_harapan_hidup']
)
print(f"Korelasi Spearman (ρ) : {spearman_r:.4f}")
print(f"p-value               : {spearman_p:.6f}")
```

```python
# Interpretasi otomatis
def interpretasi_korelasi(r):
    """Menginterpretasikan kekuatan korelasi."""
    abs_r = abs(r)
    if abs_r < 0.3:
        kekuatan = "lemah"
    elif abs_r < 0.7:
        kekuatan = "sedang"
    else:
        kekuatan = "kuat"

    arah = "positif" if r > 0 else "negatif"
    return f"Korelasi {arah} yang {kekuatan} (r = {r:.4f})"

print("Interpretasi Pearson :", interpretasi_korelasi(pearson_r))
print("Interpretasi Spearman:", interpretasi_korelasi(spearman_r))
```

**Pertanyaan:** Kapan kita menggunakan Pearson vs Spearman? Apa perbedaan asumsinya?

### Langkah 4: Membangun Model Regresi Linear dengan scikit-learn

```python
# Siapkan data untuk sklearn
# sklearn membutuhkan X dalam bentuk 2D array (n_samples, n_features)
X = data['pdb_per_kapita_juta'].values.reshape(-1, 1)
y = data['angka_harapan_hidup'].values

# Buat dan latih model
model = LinearRegression()
model.fit(X, y)

# Tampilkan parameter model
print("=== Parameter Model Regresi Linear ===")
print(f"Intercept (β₀) : {model.intercept_:.4f}")
print(f"Slope (β₁)     : {model.coef_[0]:.4f}")
print(f"R² Score        : {model.score(X, y):.4f}")
```

```python
# Prediksi
y_pred = model.predict(X)

# Hitung metrik evaluasi
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

print("=== Metrik Evaluasi ===")
print(f"Mean Squared Error (MSE)  : {mse:.4f}")
print(f"Root MSE (RMSE)           : {rmse:.4f}")
print(f"R² Score                  : {r2:.4f}")
```

### Langkah 5: Interpretasi Model

```python
# Interpretasi dalam konteks
slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, y)

print("=== Interpretasi Model ===")
print(f"""
Persamaan regresi: Ŷ = {intercept:.4f} + {slope:.4f} * X

Artinya:
- Intercept ({intercept:.2f}): Jika PDB per kapita = 0 juta rupiah,
  angka harapan hidup diprediksi sebesar {intercept:.2f} tahun.
  (Catatan: ini adalah ekstrapolasi, mungkin tidak bermakna secara praktis)

- Slope ({slope:.4f}): Setiap kenaikan 1 juta rupiah PDB per kapita,
  angka harapan hidup meningkat sebesar {slope:.4f} tahun.

- R² ({r2:.4f}): Sebesar {r2*100:.2f}% variasi dalam angka harapan hidup
  dapat dijelaskan oleh PDB per kapita.
""")
```

```python
# Prediksi untuk nilai tertentu
pdb_baru = np.array([[30], [60], [90]])
prediksi = model.predict(pdb_baru)

print("=== Prediksi untuk Nilai PDB Tertentu ===")
for pdb_val, pred_val in zip(pdb_baru.flatten(), prediksi):
    print(f"PDB per kapita = {pdb_val} juta → Harapan hidup ≈ {pred_val:.2f} tahun")
```

### Langkah 6: Visualisasi Garis Regresi

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Scatter + Regression Line
axes[0].scatter(X, y, color='steelblue', s=80, alpha=0.7, label='Data aktual')
axes[0].plot(X, y_pred, color='red', linewidth=2, label='Garis regresi')
axes[0].set_xlabel('PDB per Kapita (Juta Rupiah)')
axes[0].set_ylabel('Angka Harapan Hidup (Tahun)')
axes[0].set_title('Scatter Plot dengan Garis Regresi')
axes[0].legend()

# Plot 2: Menggunakan seaborn regplot (lebih mudah)
sns.regplot(x='pdb_per_kapita_juta', y='angka_harapan_hidup', data=data,
            ax=axes[1], scatter_kws={'s': 80, 'alpha': 0.7},
            line_kws={'color': 'red'})
axes[1].set_xlabel('PDB per Kapita (Juta Rupiah)')
axes[1].set_ylabel('Angka Harapan Hidup (Tahun)')
axes[1].set_title('Scatter Plot dengan seaborn regplot\n(termasuk confidence interval)')

plt.tight_layout()
plt.show()
```

### Langkah 7: Analisis Residual

```python
# Hitung residual
residual = y - y_pred

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: Residual vs Fitted
axes[0].scatter(y_pred, residual, color='steelblue', s=60, alpha=0.7)
axes[0].axhline(y=0, color='red', linestyle='--', linewidth=2)
axes[0].set_xlabel('Nilai Prediksi (Ŷ)')
axes[0].set_ylabel('Residual (Y - Ŷ)')
axes[0].set_title('Residual vs Fitted Values')

# Plot 2: Histogram residual
axes[1].hist(residual, bins=10, color='steelblue', edgecolor='navy', alpha=0.7)
axes[1].set_xlabel('Residual')
axes[1].set_ylabel('Frekuensi')
axes[1].set_title('Distribusi Residual')

# Plot 3: Q-Q Plot
stats.probplot(residual, dist="norm", plot=axes[2])
axes[2].set_title('Q-Q Plot Residual')

plt.tight_layout()
plt.show()
```

```python
# Uji normalitas residual
shapiro_stat, shapiro_p = stats.shapiro(residual)
print(f"Uji Shapiro-Wilk untuk normalitas residual:")
print(f"Statistik = {shapiro_stat:.4f}, p-value = {shapiro_p:.4f}")

if shapiro_p > 0.05:
    print("→ Residual berdistribusi normal (p > 0.05)")
else:
    print("→ Residual TIDAK berdistribusi normal (p ≤ 0.05)")
```

### Langkah 8: Studi Kasus Lanjutan — Inflasi dan Pengangguran

```python
# Data simulasi: hubungan inflasi dan tingkat pengangguran
np.random.seed(123)
n_obs = 50

inflasi = np.random.uniform(2, 10, n_obs)
pengangguran = 8 - 0.3 * inflasi + np.random.normal(0, 0.8, n_obs)

df_kasus = pd.DataFrame({
    'inflasi_persen': np.round(inflasi, 2),
    'pengangguran_persen': np.round(pengangguran, 2)
})

# Bangun model
X2 = df_kasus['inflasi_persen'].values.reshape(-1, 1)
y2 = df_kasus['pengangguran_persen'].values

model2 = LinearRegression()
model2.fit(X2, y2)

print(f"Persamaan: Pengangguran = {model2.intercept_:.4f} + ({model2.coef_[0]:.4f}) × Inflasi")
print(f"R² = {model2.score(X2, y2):.4f}")
print()
print("Interpretasi: Hubungan negatif — saat inflasi naik,")
print("tingkat pengangguran cenderung turun (Phillips Curve).")
```

```python
# Visualisasi studi kasus
plt.figure(figsize=(10, 6))
plt.scatter(X2, y2, color='coral', s=60, alpha=0.7, label='Data')
plt.plot(X2, model2.predict(X2), color='darkred', linewidth=2, label='Regresi')
plt.xlabel('Inflasi (%)')
plt.ylabel('Tingkat Pengangguran (%)')
plt.title('Hubungan Inflasi dan Pengangguran\n(Simulasi Phillips Curve)')
plt.legend()
plt.tight_layout()
plt.show()
```

---

## Tugas yang Harus Dikumpulkan

Buat notebook Google Colab yang berisi:

1. **Eksplorasi Data** (20 poin)
   - Buat dataset sendiri atau gunakan dataset open yang relevan dengan ekonomi/sosial Indonesia
   - Tampilkan statistik deskriptif dan scatter plot

2. **Analisis Korelasi** (20 poin)
   - Hitung korelasi Pearson dan Spearman
   - Jelaskan mengapa kedua nilai bisa berbeda

3. **Model Regresi** (30 poin)
   - Bangun model regresi linear sederhana dengan `sklearn`
   - Tuliskan persamaan regresi dan interpretasikan setiap parameter

4. **Diagnostik Model** (20 poin)
   - Buat residual plot dan Q-Q plot
   - Lakukan uji Shapiro-Wilk pada residual
   - Simpulkan apakah asumsi normalitas terpenuhi

5. **Kesimpulan** (10 poin)
   - Tuliskan kesimpulan dalam 1 paragraf menggunakan bahasa yang mudah dipahami

**Format:** File `.ipynb` diunggah ke Google Classroom
**Deadline:** Satu minggu setelah pertemuan praktikum

---

## Challenge / Bonus

1. **Gunakan data nyata dari BPS** (Badan Pusat Statistik): Unduh data dari [bps.go.id](https://www.bps.go.id/) dan lakukan regresi linear. Misalnya: hubungan pengeluaran pendidikan per kapita dengan angka melek huruf per provinsi.

2. **Bandingkan dua model regresi** untuk variabel dependen yang sama tetapi variabel independen yang berbeda. Mana yang memiliki R² lebih tinggi? Apakah R² lebih tinggi selalu berarti model lebih baik?

3. **Buat fungsi Python** yang menerima dua array dan secara otomatis mengembalikan: korelasi, persamaan regresi, R², dan visualisasi lengkap.
