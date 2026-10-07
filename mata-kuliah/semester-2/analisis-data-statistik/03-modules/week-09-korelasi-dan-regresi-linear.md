# Minggu 9: Korelasi dan Regresi Linear Sederhana

## Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

**Semester:** Genap 2025/2026
**CPMK:** CPMK-5 — Menganalisis hubungan antar variabel menggunakan korelasi dan model regresi
**Sub-CPMK:** 9.1 (Koefisien korelasi), 9.2 (Regresi linear sederhana)
**Bloom's Taxonomy:** C4 (Analyze)
**Durasi:** 100 menit (50 menit teori + 50 menit praktikum)

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Menghitung dan menginterpretasi** koefisien korelasi Pearson (r) dan Spearman (ρ) untuk mengukur kekuatan dan arah hubungan antara dua variabel (Sub-CPMK 9.1)
2. **Membedakan** korelasi dari kausalitas (*correlation ≠ causation*) dengan contoh nyata (Sub-CPMK 9.1)
3. **Membangun** model regresi linear sederhana menggunakan metode *least squares* (Sub-CPMK 9.2)
4. **Menginterpretasi** koefisien regresi (slope, intercept) dan R² dalam konteks data riil (Sub-CPMK 9.2)
5. **Mengimplementasikan** analisis korelasi dan regresi menggunakan Python (numpy, sklearn, statsmodels) (Sub-CPMK 9.2)

---

## Materi

### 9.1 Korelasi: Mengukur Hubungan Dua Variabel

#### 9.1.1 Apa Itu Korelasi?

Korelasi adalah ukuran statistik yang menggambarkan **kekuatan** dan **arah** hubungan linear antara dua variabel numerik. Bayangkan kita ingin tahu: apakah mahasiswa yang belajar lebih lama cenderung mendapat nilai lebih tinggi? Korelasi membantu menjawab pertanyaan semacam ini secara kuantitatif.

Dua hal penting yang diukur korelasi:

| Aspek | Penjelasan | Contoh |
|-------|-----------|--------|
| **Arah** | Positif (+) atau negatif (-) | Jam belajar vs nilai (positif); jam main game vs nilai (negatif) |
| **Kekuatan** | Seberapa erat hubungan (0 = tidak ada, 1 = sempurna) | r = 0.95 (sangat kuat); r = 0.20 (lemah) |

#### 9.1.2 Korelasi Pearson (r)

Koefisien korelasi Pearson mengukur hubungan **linear** antara dua variabel. Formulanya:

```
        Σ(xᵢ - x̄)(yᵢ - ȳ)
r = ─────────────────────────────
    √[Σ(xᵢ - x̄)²] × √[Σ(yᵢ - ȳ)²]
```

**Interpretasi nilai r:**

| Rentang r | Interpretasi |
|-----------|-------------|
| 0.80 - 1.00 | Sangat kuat |
| 0.60 - 0.79 | Kuat |
| 0.40 - 0.59 | Sedang |
| 0.20 - 0.39 | Lemah |
| 0.00 - 0.19 | Sangat lemah / tidak ada |

> **Catatan:** Tanda positif/negatif menunjukkan arah, bukan kekuatan. Jadi r = -0.85 itu lebih kuat dari r = +0.40.

**Syarat penggunaan Pearson:**
- Kedua variabel berskala interval atau rasio
- Hubungan antar variabel bersifat linear
- Data tidak memiliki outlier yang ekstrem

#### 9.1.3 Korelasi Spearman (ρ)

Ketika data tidak memenuhi syarat Pearson — misalnya ada outlier atau hubungannya *monotonic* tapi tidak linear — kita gunakan Spearman. Korelasi Spearman bekerja berdasarkan **rank** (peringkat), bukan nilai asli.

Langkah-langkahnya:
1. Urutkan (rank) nilai X dan Y masing-masing
2. Hitung korelasi Pearson dari rank-rank tersebut

**Kapan menggunakan Spearman?**
- Data ordinal (misalnya skala Likert)
- Ada outlier yang mempengaruhi Pearson
- Hubungan monotonic tapi tidak linear

#### 9.1.4 Scatter Plot dan Interpretasi Visual

Scatter plot adalah langkah pertama sebelum menghitung korelasi. Selalu visualisasikan data terlebih dahulu.

Dari scatter plot, kita bisa melihat:
- **Arah:** Titik-titik naik ke kanan atas (positif) atau turun (negatif)
- **Kekuatan:** Titik-titik rapat mendekati garis lurus (kuat) atau tersebar (lemah)
- **Pola non-linear:** Misalnya kurva U — di mana Pearson r bisa bernilai mendekati 0 padahal ada hubungan jelas!
- **Outlier:** Titik yang jauh dari pola umum

#### 9.1.5 PENTING: Correlation ≠ Causation

Ini adalah salah satu konsep paling penting dalam statistik. **Korelasi tidak berarti kausalitas** (*correlation does not imply causation*).

**Contoh klasik yang sering disalahartikan:**

| Variabel X | Variabel Y | Korelasi | Apakah X menyebabkan Y? |
|-----------|-----------|----------|------------------------|
| Penjualan es krim | Kasus tenggelam | Positif kuat | TIDAK. Variabel ketiga (cuaca panas) menyebabkan keduanya naik |
| Jumlah film Nicolas Cage | Kasus tenggelam di kolam | Positif (r ≈ 0.67) | TIDAK. Ini *spurious correlation* — kebetulan statistik |
| Konsumsi keju per kapita | Kematian terjerat selimut | Positif (r ≈ 0.95) | TIDAK. Angka kebetulan bergerak bersamaan |

**Kenapa korelasi bisa menipu?**

1. **Confounding variable (variabel perancu):** Ada variabel ketiga yang menyebabkan keduanya berubah. Contoh: Es krim dan tenggelam sama-sama naik karena cuaca panas.
2. **Reverse causation:** Mungkin Y menyebabkan X, bukan sebaliknya.
3. **Spurious correlation:** Secara statistik berkorelasi, tapi tidak ada mekanisme logis yang menghubungkan keduanya.

> **Pesan kunci:** Untuk membuktikan kausalitas, kita butuh **eksperimen terkontrol** (*randomized controlled trial*) atau minimal analisis yang jauh lebih dalam (misalnya *causal inference*). Korelasi adalah langkah awal, bukan kesimpulan akhir.

---

### 9.2 Regresi Linear Sederhana

#### 9.2.1 Dari Korelasi ke Prediksi

Korelasi menjawab: "Apakah ada hubungan?" Regresi menjawab pertanyaan lanjutan: "Seberapa besar pengaruhnya, dan bisakah kita memprediksi?"

Model regresi linear sederhana:

```
ŷ = b₀ + b₁x
```

Di mana:
- **ŷ** (*y-hat*) = nilai prediksi variabel dependen
- **b₀** (*intercept*) = nilai ŷ ketika x = 0
- **b₁** (*slope*) = perubahan ŷ untuk setiap kenaikan 1 unit x
- **x** = variabel independen (prediktor)

#### 9.2.2 Metode Least Squares

Bagaimana kita menemukan garis "terbaik" yang melewati titik-titik data? Kita menggunakan **metode Ordinary Least Squares (OLS)** — yaitu mencari b₀ dan b₁ yang meminimalkan jumlah kuadrat error (*residuals*):

```
Minimize: Σ(yᵢ - ŷᵢ)² = Σ(yᵢ - b₀ - b₁xᵢ)²
```

Rumus untuk slope dan intercept:

```
        Σ(xᵢ - x̄)(yᵢ - ȳ)
b₁ = ──────────────────────
         Σ(xᵢ - x̄)²

b₀ = ȳ - b₁ × x̄
```

**Residual** (eᵢ) adalah selisih antara nilai aktual dan nilai prediksi:

```
eᵢ = yᵢ - ŷᵢ
```

#### 9.2.3 Interpretasi Koefisien

Interpretasi yang tepat sangat penting. Gunakan template berikut:

- **Slope (b₁):** "Jika X naik 1 unit, maka Y **diperkirakan** berubah sebesar b₁ unit."
- **Intercept (b₀):** "Ketika X = 0, nilai Y diperkirakan sebesar b₀." (Tapi hati-hati — X = 0 mungkin tidak masuk akal dalam konteks data!)

**Contoh:** Jika model regresi pendapatan vs pengeluaran menghasilkan ŷ = 500.000 + 0.6x:
- Slope = 0.6 → "Setiap kenaikan pendapatan Rp 1.000, pengeluaran diperkirakan naik Rp 600."
- Intercept = 500.000 → "Jika pendapatan Rp 0, pengeluaran diperkirakan Rp 500.000." (interpretasi ini perlu hati-hati karena pendapatan = 0 mungkin di luar jangkauan data)

#### 9.2.4 R² (Coefficient of Determination)

R² mengukur **proporsi variasi** dalam Y yang dapat dijelaskan oleh X.

```
R² = 1 - (SS_res / SS_tot)
```

Di mana:
- SS_res = Σ(yᵢ - ŷᵢ)² → variasi yang TIDAK bisa dijelaskan model
- SS_tot = Σ(yᵢ - ȳ)² → variasi total dalam Y

**Interpretasi:**
- R² = 0.78 → "78% variasi dalam Y dapat dijelaskan oleh X. Sisanya 22% dijelaskan oleh faktor lain."
- R² = 0.15 → "Hanya 15% variasi Y dijelaskan oleh X." → model kurang baik

**Catatan penting:** Untuk regresi linear sederhana (satu prediktor), R² = r² (kuadrat dari korelasi Pearson).

---

## Contoh Kode Python

### Persiapan Data

```python
# Import library yang dibutuhkan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Contoh dataset: IPM vs Pendapatan Per Kapita (data simulasi provinsi)
np.random.seed(42)

data = pd.DataFrame({
    'provinsi': [f'Prov_{i}' for i in range(1, 35)],
    'ipm': np.random.normal(70, 5, 34).clip(55, 85),  # Indeks Pembangunan Manusia
    'pendapatan_juta': np.random.normal(40, 15, 34).clip(10, 90)  # Pendapatan per kapita (juta Rp)
})

# Tambahkan hubungan linear + noise
data['pendapatan_juta'] = 5 + 0.8 * data['ipm'] + np.random.normal(0, 5, 34)

print("=== Preview Data ===")
print(data.head(10))
print(f"\nJumlah data: {len(data)} provinsi")
```

### Scatter Plot dan Visualisasi Awal

```python
# Scatter plot: langkah pertama selalu visualisasi!
plt.figure(figsize=(8, 6))
plt.scatter(data['ipm'], data['pendapatan_juta'],
            color='steelblue', edgecolor='white', s=80, alpha=0.8)
plt.xlabel('Indeks Pembangunan Manusia (IPM)', fontsize=12)
plt.ylabel('Pendapatan Per Kapita (Juta Rp)', fontsize=12)
plt.title('Hubungan IPM dan Pendapatan Per Kapita\nProvinsi di Indonesia (Data Simulasi)',
          fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Menghitung Korelasi Pearson dan Spearman

```python
# Korelasi Pearson
pearson_r, pearson_p = stats.pearsonr(data['ipm'], data['pendapatan_juta'])
print(f"Korelasi Pearson: r = {pearson_r:.4f}, p-value = {pearson_p:.6f}")

# Korelasi Spearman
spearman_rho, spearman_p = stats.spearmanr(data['ipm'], data['pendapatan_juta'])
print(f"Korelasi Spearman: ρ = {spearman_rho:.4f}, p-value = {spearman_p:.6f}")

# Interpretasi otomatis
def interpretasi_korelasi(r):
    """Menginterpretasi kekuatan korelasi."""
    abs_r = abs(r)
    if abs_r >= 0.80:
        kekuatan = "sangat kuat"
    elif abs_r >= 0.60:
        kekuatan = "kuat"
    elif abs_r >= 0.40:
        kekuatan = "sedang"
    elif abs_r >= 0.20:
        kekuatan = "lemah"
    else:
        kekuatan = "sangat lemah"
    arah = "positif" if r > 0 else "negatif"
    return f"Hubungan {arah} yang {kekuatan}"

print(f"\nInterpretasi Pearson: {interpretasi_korelasi(pearson_r)}")
print(f"Interpretasi Spearman: {interpretasi_korelasi(spearman_rho)}")
```

### Regresi Linear Sederhana dengan sklearn

```python
from sklearn.linear_model import LinearRegression

# Siapkan data (sklearn butuh array 2D untuk X)
X = data['ipm'].values.reshape(-1, 1)
y = data['pendapatan_juta'].values

# Buat dan fit model
model = LinearRegression()
model.fit(X, y)

# Koefisien
b0 = model.intercept_       # Intercept
b1 = model.coef_[0]         # Slope
r_squared = model.score(X, y)  # R²

print("=== Hasil Regresi Linear (sklearn) ===")
print(f"Persamaan: ŷ = {b0:.2f} + {b1:.4f} × IPM")
print(f"Intercept (b₀): {b0:.2f}")
print(f"Slope (b₁): {b1:.4f}")
print(f"R²: {r_squared:.4f}")
print(f"\nInterpretasi slope: Setiap kenaikan 1 poin IPM,")
print(f"  pendapatan per kapita diperkirakan naik Rp {b1:.2f} juta.")
print(f"\nInterpretasi R²: {r_squared*100:.1f}% variasi pendapatan per kapita")
print(f"  dapat dijelaskan oleh IPM.")
```

### Regresi Linear Sederhana dengan statsmodels (Output Lengkap)

```python
import statsmodels.api as sm

# statsmodels membutuhkan penambahan konstanta secara manual
X_sm = sm.add_constant(data['ipm'])  # Menambahkan kolom intercept

# Fit model OLS
model_sm = sm.OLS(data['pendapatan_juta'], X_sm).fit()

# Tampilkan summary lengkap
print(model_sm.summary())

# Summary ini memberikan informasi lengkap:
# - Koefisien, standard error, t-statistic, p-value
# - R², Adjusted R²
# - F-statistic
# - Confidence interval untuk koefisien
```

### Visualisasi Scatter Plot + Regression Line

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Scatter + Regression Line
ax1 = axes[0]
ax1.scatter(data['ipm'], data['pendapatan_juta'],
            color='steelblue', edgecolor='white', s=80, alpha=0.8, label='Data')

# Garis regresi
x_line = np.linspace(data['ipm'].min() - 2, data['ipm'].max() + 2, 100)
y_line = b0 + b1 * x_line
ax1.plot(x_line, y_line, color='red', linewidth=2,
         label=f'ŷ = {b0:.1f} + {b1:.2f}x')

ax1.set_xlabel('IPM', fontsize=11)
ax1.set_ylabel('Pendapatan Per Kapita (Juta Rp)', fontsize=11)
ax1.set_title('Regresi Linear: IPM vs Pendapatan', fontsize=13)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Plot 2: Residual Plot
y_pred = model.predict(X)
residuals = y - y_pred

ax2 = axes[1]
ax2.scatter(y_pred, residuals, color='coral', edgecolor='white', s=80, alpha=0.8)
ax2.axhline(y=0, color='black', linestyle='--', linewidth=1)
ax2.set_xlabel('Nilai Prediksi (ŷ)', fontsize=11)
ax2.set_ylabel('Residual (y - ŷ)', fontsize=11)
ax2.set_title('Residual Plot', fontsize=13)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Jika residual tersebar acak di sekitar garis 0 → asumsi linearitas terpenuhi.")
print("Jika ada pola (misalnya parabola) → hubungan mungkin non-linear.")
```

### Regresi dengan numpy polyfit (Alternatif Cepat)

```python
# numpy polyfit: cara cepat untuk polynomial fitting
# degree=1 artinya linear
koefisien = np.polyfit(data['ipm'], data['pendapatan_juta'], deg=1)
print(f"Dengan numpy polyfit: slope = {koefisien[0]:.4f}, intercept = {koefisien[1]:.2f}")

# Bisa juga untuk polynomial degree > 1
koef_kuadratik = np.polyfit(data['ipm'], data['pendapatan_juta'], deg=2)
print(f"Model kuadratik: y = {koef_kuadratik[0]:.4f}x² + {koef_kuadratik[1]:.2f}x + {koef_kuadratik[2]:.2f}")
```

---

## Studi Kasus: Hubungan IPM dan Pendapatan Per Kapita di Indonesia

### Konteks

Indeks Pembangunan Manusia (IPM) adalah ukuran komposit dari kesehatan, pendidikan, dan standar hidup. Apakah provinsi dengan IPM lebih tinggi cenderung memiliki pendapatan per kapita lebih tinggi? Mari kita analisis.

### Langkah Analisis

```python
# ============================================================
# STUDI KASUS: IPM vs Pendapatan Per Kapita
# Sumber data: Simulasi berdasarkan pola BPS Indonesia
# ============================================================

# 1. Membuat data simulasi (dalam praktik nyata, unduh dari bps.go.id)
np.random.seed(2025)
n_prov = 34

ipm_values = np.array([
    65.5, 72.3, 71.0, 76.1, 68.7, 70.2, 73.5, 69.8, 74.3, 78.5,
    80.2, 72.8, 71.5, 75.0, 67.3, 66.1, 73.0, 70.5, 69.0, 77.8,
    64.3, 68.0, 72.1, 74.7, 80.8, 71.3, 67.5, 63.0, 61.5, 69.5,
    75.5, 66.8, 78.0, 82.0
])

# Pendapatan terkait IPM + noise
pendapatan = 5 + 0.7 * ipm_values + np.random.normal(0, 4, n_prov)

studi_kasus = pd.DataFrame({
    'ipm': ipm_values,
    'pendapatan_juta': pendapatan
})

# 2. Eksplorasi awal
print("=== Statistik Deskriptif ===")
print(studi_kasus.describe().round(2))

# 3. Korelasi
r, p = stats.pearsonr(studi_kasus['ipm'], studi_kasus['pendapatan_juta'])
print(f"\nKorelasi Pearson: r = {r:.4f}, p-value = {p:.6f}")
print(f"Korelasi {'signifikan' if p < 0.05 else 'tidak signifikan'} pada α = 0.05")

# 4. Regresi
X_sk = studi_kasus['ipm'].values.reshape(-1, 1)
y_sk = studi_kasus['pendapatan_juta'].values

model_sk = LinearRegression().fit(X_sk, y_sk)
print(f"\n=== Model Regresi ===")
print(f"ŷ = {model_sk.intercept_:.2f} + {model_sk.coef_[0]:.4f} × IPM")
print(f"R² = {model_sk.score(X_sk, y_sk):.4f}")

# 5. Prediksi
ipm_baru = 75
prediksi = model_sk.predict([[ipm_baru]])
print(f"\nPrediksi: Provinsi dengan IPM {ipm_baru}")
print(f"  → Pendapatan per kapita diperkirakan: Rp {prediksi[0]:.2f} juta")
```

### Diskusi Studi Kasus

1. **Apakah hubungan ini kausal?** Tidak bisa dipastikan hanya dari korelasi. Mungkin pendapatan tinggi menyebabkan IPM tinggi (investasi di pendidikan dan kesehatan), bukan sebaliknya.
2. **Confounding variables?** Faktor seperti kebijakan pemerintah daerah, sumber daya alam, dan urbanisasi bisa mempengaruhi keduanya.
3. **Limitasi model:** Regresi linear sederhana hanya menggunakan satu prediktor. Realitanya, banyak faktor yang mempengaruhi pendapatan per kapita.

---

## AI Corner: Menggunakan AI untuk Analisis Korelasi dan Regresi

### Prompt yang Efektif

Berikut contoh prompt yang bisa digunakan saat berkolaborasi dengan AI:

> "Saya punya dataset 34 provinsi dengan variabel IPM dan pendapatan per kapita. Tolong bantu saya: (1) hitung korelasi Pearson dan Spearman, (2) buat model regresi linear sederhana, (3) interpretasikan hasilnya dalam bahasa non-teknis."

### Kapan AI Membantu

- Menjelaskan konsep yang sulit dipahami (misalnya: "jelaskan R² dengan analogi sederhana")
- Memeriksa apakah interpretasi kita sudah tepat
- Debugging kode Python yang error
- Menyarankan visualisasi yang tepat

### Kapan Harus Kritis terhadap AI

- AI mungkin memberikan interpretasi kausal dari korelasi → **selalu cek apakah AI mengklaim kausalitas**
- AI bisa salah menghitung → **selalu verifikasi angka-angka penting**
- AI mungkin tidak tahu konteks Indonesia → **kita yang lebih paham konteks lokal**

### Contoh Evaluasi Output AI

Jika AI mengatakan: *"IPM menyebabkan kenaikan pendapatan per kapita"* — ini **salah**. Yang benar: *"IPM berkorelasi positif dengan pendapatan per kapita, tetapi hubungan kausal memerlukan analisis lebih lanjut."*

---

## Latihan Mandiri

### Latihan 1: Korelasi (15 menit)

Diberikan data berikut:

| Jam Belajar (X) | 2 | 3 | 5 | 6 | 8 | 9 | 10 |
|-----------------|---|---|---|---|---|---|-----|
| Nilai Ujian (Y) | 55 | 60 | 68 | 72 | 80 | 85 | 90 |

a. Buat scatter plot menggunakan matplotlib
b. Hitung korelasi Pearson menggunakan `scipy.stats.pearsonr`
c. Interpretasikan hasilnya: apa arah dan kekuatan hubungannya?
d. Apakah kita bisa menyimpulkan bahwa "belajar lebih lama menyebabkan nilai lebih tinggi"? Jelaskan.

### Latihan 2: Regresi Linear (20 menit)

Menggunakan data Latihan 1:

a. Bangun model regresi linear menggunakan `sklearn.linear_model.LinearRegression`
b. Tuliskan persamaan regresinya: ŷ = b₀ + b₁x
c. Interpretasikan slope: "Setiap tambahan 1 jam belajar..."
d. Berapa R²? Apa artinya?
e. Prediksi nilai ujian untuk mahasiswa yang belajar 7 jam

### Latihan 3: Studi Kasus Mini (25 menit)

Carilah (atau simulasikan) data tentang salah satu topik berikut:
- Jumlah penduduk vs jumlah UMKM per kabupaten
- Lama penggunaan smartphone vs kualitas tidur mahasiswa
- Suhu rata-rata vs konsumsi listrik rumah tangga

Lakukan analisis lengkap:
1. Scatter plot
2. Korelasi Pearson dan Spearman
3. Regresi linear sederhana (dengan interpretasi koefisien)
4. Visualisasi scatter + regression line
5. Diskusikan: apakah ini korelasi atau kausalitas?

### Latihan 4: Spurious Correlation (10 menit)

Kunjungi website [tylervigen.com/spurious-correlations](https://tylervigen.com/spurious-correlations) (atau cari "spurious correlations" di internet).

a. Pilih satu contoh *spurious correlation* yang menarik
b. Jelaskan mengapa korelasi tersebut bukan kausalitas
c. Adakah kemungkinan *confounding variable*? Jika ya, apa?

---

## Rangkuman

| Konsep | Poin Kunci |
|--------|-----------|
| Korelasi Pearson (r) | Mengukur hubungan linear; syarat: data interval/rasio, linear, tanpa outlier ekstrem |
| Korelasi Spearman (ρ) | Berbasis rank; robust terhadap outlier; untuk data ordinal atau non-linear monotonic |
| Correlation ≠ Causation | Selalu pertimbangkan confounding variable, reverse causation, spurious correlation |
| Regresi Linear Sederhana | ŷ = b₀ + b₁x; metode least squares; meminimalkan jumlah kuadrat residual |
| Interpretasi Slope | "Jika X naik 1 unit, Y diperkirakan berubah b₁ unit" |
| R² | Proporsi variasi Y yang dijelaskan oleh X; 0-1; semakin tinggi semakin baik |

---

## Referensi

1. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics* (4th ed.), Chapter 8: Introduction to Linear Regression.
2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning (ISLP)*, Chapter 3: Linear Regression.
3. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.), Chapter 12: Data Analysis Examples.
4. scikit-learn Documentation: [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
5. statsmodels Documentation: [OLS](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html)
6. Tyler Vigen — Spurious Correlations: [tylervigen.com](https://tylervigen.com/spurious-correlations)
7. BPS (Badan Pusat Statistik) — Data IPM Indonesia: [bps.go.id](https://bps.go.id)

---

*Modul ini adalah bagian dari mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia. Semester Genap 2025/2026.*
