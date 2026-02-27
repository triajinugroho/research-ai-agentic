# Minggu 10: Regresi Berganda dan Evaluasi Model

## Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

**Semester:** Genap 2025/2026
**CPMK:** CPMK-5 — Menganalisis hubungan antar variabel menggunakan korelasi dan model regresi serta mengevaluasi kualitas model
**Sub-CPMK:** 10.1 (Regresi berganda), 10.2 (Diagnostik residual dan evaluasi model)
**Bloom's Taxonomy:** C4-C5 (Analyze-Evaluate)
**Durasi:** 100 menit (50 menit teori + 50 menit praktikum)

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Membangun** model regresi linear berganda (*multiple linear regression*) dengan lebih dari satu prediktor (Sub-CPMK 10.1)
2. **Menginterpretasi** koefisien regresi berganda dalam konteks "holding other variables constant" (Sub-CPMK 10.1)
3. **Membedakan** R² dan Adjusted R², serta menjelaskan mengapa Adjusted R² lebih tepat untuk model berganda (Sub-CPMK 10.2)
4. **Melakukan** diagnostik residual: normalitas, homoscedasticity, dan linearity (Sub-CPMK 10.2)
5. **Mendeteksi** multicollinearity menggunakan VIF (*Variance Inflation Factor*) (Sub-CPMK 10.2)
6. **Mengimplementasikan** regresi berganda dan diagnostik menggunakan Python (sklearn, statsmodels) (Sub-CPMK 10.1-10.2)

---

## Materi

### 10.1 Multiple Linear Regression

#### 10.1.1 Mengapa Perlu Lebih dari Satu Prediktor?

Pada Minggu 9, kita mempelajari regresi linear **sederhana** dengan satu prediktor. Dalam kenyataannya, jarang sekali satu variabel bisa menjelaskan fenomena secara lengkap.

**Contoh:** Memprediksi harga rumah hanya dari luas bangunan akan mengabaikan faktor penting lain seperti lokasi, jumlah kamar, dan usia bangunan. Regresi berganda memungkinkan kita memasukkan semua faktor tersebut.

#### 10.1.2 Model Regresi Berganda

Persamaan model regresi berganda:

```
ŷ = b₀ + b₁x₁ + b₂x₂ + ... + bₚxₚ
```

Di mana:
- **ŷ** = nilai prediksi variabel dependen
- **b₀** = intercept
- **b₁, b₂, ..., bₚ** = koefisien untuk masing-masing prediktor
- **x₁, x₂, ..., xₚ** = variabel prediktor (independen)
- **p** = jumlah prediktor

**Contoh konkret:**

```
Harga_Rumah = b₀ + b₁(Luas) + b₂(Jml_Kamar) + b₃(Jarak_Pusat_Kota)
```

#### 10.1.3 Interpretasi Koefisien Multivariat

Interpretasi koefisien dalam regresi berganda **berbeda** dari regresi sederhana. Kata kuncinya: ***"holding other variables constant"*** (dengan variabel lain tetap).

**Template interpretasi:**

> "Jika x₁ naik 1 unit, **dengan asumsi semua variabel lain tetap (ceteris paribus)**, maka ŷ diperkirakan berubah sebesar b₁ unit."

**Contoh:** Jika model menghasilkan:
```
Harga = 100 + 5.2(Luas) + 30(Jml_Kamar) - 2.5(Jarak_km)
```

- b₁ = 5.2 → "Setiap tambahan 1 m² luas bangunan, harga rumah diperkirakan naik 5.2 juta rupiah, **dengan asumsi** jumlah kamar dan jarak ke pusat kota tetap."
- b₃ = -2.5 → "Setiap tambahan 1 km jarak dari pusat kota, harga rumah diperkirakan **turun** 2.5 juta rupiah, ceteris paribus."

> **Perhatian:** Interpretasi "ceteris paribus" ini adalah interpretasi statistik. Dalam praktik, sulit mengubah satu variabel tanpa mempengaruhi yang lain (misalnya, rumah lebih besar biasanya punya lebih banyak kamar).

---

### 10.2 Evaluasi Model Regresi

#### 10.2.1 R² vs Adjusted R²

**Masalah R² dalam regresi berganda:**
R² akan **selalu naik** (atau minimal tetap) ketika kita menambahkan prediktor baru — bahkan jika prediktor tersebut tidak berguna! Ini karena model selalu bisa "memeras" sedikit informasi dari variabel tambahan meskipun itu hanya noise.

**Adjusted R²** mengatasi masalah ini dengan memberikan penalti untuk setiap prediktor tambahan:

```
Adjusted R² = 1 - [(1 - R²)(n - 1) / (n - p - 1)]
```

Di mana:
- n = jumlah observasi
- p = jumlah prediktor

**Perbandingan:**

| Aspek | R² | Adjusted R² |
|-------|-----|-------------|
| Nilai | Selalu naik saat prediktor bertambah | Bisa turun jika prediktor tidak berguna |
| Kegunaan | Regresi sederhana (1 prediktor) | Regresi berganda (>1 prediktor) |
| Range | 0 - 1 | Bisa < 0 (model sangat buruk) |
| Kapan pakai | Membandingkan model dengan jumlah prediktor sama | Membandingkan model dengan jumlah prediktor berbeda |

**Aturan praktis:** Jika Adjusted R² **turun** ketika prediktor ditambahkan, prediktor tersebut kemungkinan tidak berguna.

#### 10.2.2 Diagnostik Residual

Agar model regresi valid, beberapa **asumsi** harus terpenuhi. Kita memeriksa asumsi ini melalui analisis residual (selisih antara nilai aktual dan prediksi).

**Asumsi 1: Linearitas**
- Hubungan antara X dan Y harus linear
- **Cara cek:** Residual plot (residual vs fitted values) — titik-titik harus tersebar acak
- **Jika dilanggar:** Pertimbangkan transformasi variabel atau model non-linear

**Asumsi 2: Normalitas Residual**
- Residual harus berdistribusi normal
- **Cara cek:** Q-Q plot (quantile-quantile plot) — titik-titik harus mendekati garis diagonal
- **Cara cek (formal):** Shapiro-Wilk test
- **Jika dilanggar:** Untuk sampel besar (n > 30), regresi masih cukup robust. Untuk sampel kecil, pertimbangkan transformasi

**Asumsi 3: Homoscedasticity (Variansi Konstan)**
- Variansi residual harus konstan untuk semua nilai prediksi
- **Cara cek:** Residual plot — lebar sebaran harus sama (tidak membentuk corong/funnel)
- **Lawan:** *Heteroscedasticity* — variansi residual berubah-ubah
- **Jika dilanggar:** Gunakan *robust standard errors* atau transformasi variabel dependen (misalnya log)

**Asumsi 4: Independence**
- Residual harus independen satu sama lain
- **Biasanya dilanggar pada:** Data time series atau data yang diambil secara berurutan
- **Cara cek:** Durbin-Watson test

#### 10.2.3 Multicollinearity

**Apa itu multicollinearity?**
Multicollinearity terjadi ketika dua atau lebih variabel prediktor **sangat berkorelasi** satu sama lain. Ini menyebabkan:

- Koefisien regresi tidak stabil (berubah drastis jika data sedikit berubah)
- Standard error koefisien membesar
- Sulit menentukan kontribusi individu setiap prediktor

**Contoh:** Memasukkan "luas bangunan" dan "luas tanah" sebagai prediktor — keduanya biasanya sangat berkorelasi.

**Variance Inflation Factor (VIF):**

VIF mengukur seberapa besar variansi koefisien "meningkat" akibat korelasi dengan prediktor lain.

```
VIF(j) = 1 / (1 - Rⱼ²)
```

Di mana Rⱼ² adalah R² dari regresi xⱼ terhadap semua prediktor lain.

**Interpretasi VIF:**

| VIF | Interpretasi | Tindakan |
|-----|-------------|----------|
| 1 | Tidak ada multicollinearity | Aman |
| 1 - 5 | Multicollinearity ringan | Masih bisa diterima |
| 5 - 10 | Multicollinearity moderat | Perlu perhatian |
| > 10 | Multicollinearity serius | Perlu tindakan: hapus variabel atau gabungkan |

#### 10.2.4 Feature Selection (Konsep Dasar)

Ketika kita punya banyak prediktor, bagaimana memilih yang terbaik?

**Forward Selection:**
1. Mulai dari model tanpa prediktor (hanya intercept)
2. Tambahkan satu prediktor yang paling meningkatkan model
3. Ulangi sampai tidak ada lagi prediktor yang signifikan meningkatkan model

**Backward Elimination:**
1. Mulai dari model dengan semua prediktor
2. Hapus satu prediktor yang paling tidak signifikan (p-value tertinggi)
3. Ulangi sampai semua prediktor tersisa signifikan

> **Catatan:** Di mata kuliah ini, kita hanya membahas konsep dasar feature selection. Teknik lebih lanjut (stepwise, LASSO, dll.) akan dipelajari di mata kuliah Machine Learning.

---

## Contoh Kode Python

### Persiapan Data: Harga Rumah Sederhana di Jakarta

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Simulasi dataset harga rumah di Jakarta
np.random.seed(2025)
n = 100

luas_bangunan = np.random.uniform(36, 200, n)       # m²
jumlah_kamar = np.random.choice([2, 3, 4, 5], n, p=[0.2, 0.4, 0.3, 0.1])
jarak_pusat = np.random.uniform(3, 40, n)            # km dari Monas
usia_bangunan = np.random.uniform(0, 30, n)          # tahun

# Harga rumah (juta Rp) — relasi dengan variabel di atas + noise
harga = (
    200
    + 8.5 * luas_bangunan
    + 50 * jumlah_kamar
    - 15 * jarak_pusat
    - 5 * usia_bangunan
    + np.random.normal(0, 100, n)
)

rumah = pd.DataFrame({
    'luas_m2': luas_bangunan.round(1),
    'jumlah_kamar': jumlah_kamar,
    'jarak_pusat_km': jarak_pusat.round(1),
    'usia_tahun': usia_bangunan.round(1),
    'harga_juta': harga.round(1)
})

print("=== Preview Dataset Rumah Jakarta ===")
print(rumah.head(10))
print(f"\n{rumah.describe().round(1)}")
```

### Eksplorasi Data Awal

```python
# Correlation matrix — langkah penting sebelum regresi berganda
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Heatmap korelasi
corr_matrix = rumah.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
            fmt='.2f', ax=axes[0])
axes[0].set_title('Correlation Matrix', fontsize=13)

# Pairplot (kecil) — scatter semua pasangan variabel
# Di sini kita plot scatter luas vs harga sebagai sampel
axes[1].scatter(rumah['luas_m2'], rumah['harga_juta'],
                alpha=0.6, color='steelblue', edgecolor='white')
axes[1].set_xlabel('Luas Bangunan (m²)', fontsize=11)
axes[1].set_ylabel('Harga (Juta Rp)', fontsize=11)
axes[1].set_title('Luas Bangunan vs Harga Rumah', fontsize=13)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Cek korelasi antar prediktor (potensi multicollinearity)
print("=== Korelasi Antar Prediktor ===")
prediktor_corr = rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']].corr()
print(prediktor_corr.round(3))
```

### Regresi Berganda dengan sklearn

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Siapkan variabel
X = rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']]
y = rumah['harga_juta']

# Fit model
model = LinearRegression()
model.fit(X, y)

# Hasil
print("=== Regresi Berganda (sklearn) ===")
print(f"Intercept (b₀): {model.intercept_:.2f}")
print(f"\nKoefisien:")
for nama, koef in zip(X.columns, model.coef_):
    print(f"  {nama}: {koef:.4f}")

print(f"\nR²: {model.score(X, y):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y, model.predict(X))):.2f} juta Rp")

# Interpretasi
print(f"\n=== Interpretasi ===")
print(f"Setiap tambahan 1 m² luas → harga naik ~{model.coef_[0]:.1f} juta (ceteris paribus)")
print(f"Setiap tambahan 1 kamar → harga naik ~{model.coef_[1]:.1f} juta (ceteris paribus)")
print(f"Setiap tambahan 1 km dari pusat → harga turun ~{abs(model.coef_[2]):.1f} juta (ceteris paribus)")
print(f"Setiap tambahan 1 tahun usia → harga turun ~{abs(model.coef_[3]):.1f} juta (ceteris paribus)")
```

### Regresi Berganda dengan statsmodels (Output Lengkap)

```python
import statsmodels.api as sm

# Tambahkan konstanta (intercept)
X_sm = sm.add_constant(X)

# Fit model OLS
model_sm = sm.OLS(y, X_sm).fit()

# Tampilkan summary lengkap
print(model_sm.summary())

# Output penting yang perlu diperhatikan:
# - R-squared vs Adj. R-squared → seberapa bagus model
# - coef (koefisien) → besar pengaruh setiap variabel
# - P>|t| (p-value) → apakah variabel signifikan
# - [0.025, 0.975] → confidence interval 95% untuk koefisien
# - F-statistic → apakah model secara keseluruhan signifikan
```

### R² vs Adjusted R²: Demonstrasi

```python
# Demonstrasi: menambah variabel acak (tidak berguna)
rumah_copy = rumah.copy()
rumah_copy['random_noise'] = np.random.randn(n)  # Variabel acak — TIDAK berguna

# Model tanpa variabel acak
X1 = sm.add_constant(rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']])
model1 = sm.OLS(y, X1).fit()

# Model dengan variabel acak
X2 = sm.add_constant(rumah_copy[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km',
                                  'usia_tahun', 'random_noise']])
model2 = sm.OLS(y, X2).fit()

print("=== Perbandingan: R² vs Adjusted R² ===")
print(f"{'Metrik':<20} {'Tanpa Random':<18} {'Dengan Random':<18}")
print(f"{'─'*56}")
print(f"{'R²':<20} {model1.rsquared:<18.6f} {model2.rsquared:<18.6f}")
print(f"{'Adjusted R²':<20} {model1.rsquared_adj:<18.6f} {model2.rsquared_adj:<18.6f}")
print(f"\nPerhatikan:")
print(f"  R² naik sedikit ({model2.rsquared - model1.rsquared:.6f})")
print(f"  Adjusted R² turun ({model2.rsquared_adj - model1.rsquared_adj:.6f})")
print(f"  → Adjusted R² 'menghukum' variabel tidak berguna!")
```

### Diagnostik Residual

```python
# Hitung residual dan fitted values
y_pred = model_sm.predict(X_sm)
residuals = model_sm.resid

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Residual vs Fitted (cek linearitas & homoscedasticity)
axes[0, 0].scatter(y_pred, residuals, alpha=0.6, color='steelblue', edgecolor='white')
axes[0, 0].axhline(y=0, color='red', linestyle='--', linewidth=1.5)
axes[0, 0].set_xlabel('Fitted Values (ŷ)', fontsize=10)
axes[0, 0].set_ylabel('Residuals', fontsize=10)
axes[0, 0].set_title('1. Residual vs Fitted\n(Cek Linearitas & Homoscedasticity)', fontsize=11)
axes[0, 0].grid(True, alpha=0.3)

# 2. Q-Q Plot (cek normalitas residual)
stats.probplot(residuals, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('2. Q-Q Plot\n(Cek Normalitas Residual)', fontsize=11)
axes[0, 1].grid(True, alpha=0.3)

# 3. Histogram residual
axes[1, 0].hist(residuals, bins=20, color='steelblue', edgecolor='white', density=True)
x_norm = np.linspace(residuals.min(), residuals.max(), 100)
axes[1, 0].plot(x_norm, stats.norm.pdf(x_norm, residuals.mean(), residuals.std()),
                'r-', linewidth=2, label='Normal fit')
axes[1, 0].set_xlabel('Residuals', fontsize=10)
axes[1, 0].set_ylabel('Density', fontsize=10)
axes[1, 0].set_title('3. Histogram Residual\n(Cek Normalitas)', fontsize=11)
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# 4. Scale-Location (cek homoscedasticity)
axes[1, 1].scatter(y_pred, np.sqrt(np.abs(residuals)),
                   alpha=0.6, color='coral', edgecolor='white')
axes[1, 1].set_xlabel('Fitted Values (ŷ)', fontsize=10)
axes[1, 1].set_ylabel('√|Residuals|', fontsize=10)
axes[1, 1].set_title('4. Scale-Location Plot\n(Cek Homoscedasticity)', fontsize=11)
axes[1, 1].grid(True, alpha=0.3)

plt.suptitle('Diagnostik Residual Model Regresi Berganda', fontsize=14, y=1.01)
plt.tight_layout()
plt.show()

# Uji formal normalitas residual
stat_shapiro, p_shapiro = stats.shapiro(residuals)
print(f"Shapiro-Wilk Test: W = {stat_shapiro:.4f}, p-value = {p_shapiro:.4f}")
print(f"Normalitas residual {'terpenuhi' if p_shapiro > 0.05 else 'TIDAK terpenuhi'} (α = 0.05)")
```

### Deteksi Multicollinearity (VIF)

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Hitung VIF untuk setiap prediktor
X_vif = rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']]

vif_data = pd.DataFrame()
vif_data['Variabel'] = X_vif.columns
vif_data['VIF'] = [variance_inflation_factor(X_vif.values, i) for i in range(X_vif.shape[1])]

# Interpretasi
def interpretasi_vif(vif):
    if vif < 5:
        return "OK"
    elif vif < 10:
        return "PERHATIAN"
    else:
        return "SERIUS"

vif_data['Status'] = vif_data['VIF'].apply(interpretasi_vif)

print("=== Variance Inflation Factor (VIF) ===")
print(vif_data.to_string(index=False))
print(f"\nAturan: VIF < 5 (OK), 5-10 (perlu perhatian), > 10 (multicollinearity serius)")
```

---

## Studi Kasus: Prediksi Harga Rumah Sederhana di Jakarta

### Konteks

Pasar properti di Jakarta sangat dinamis. Banyak faktor mempengaruhi harga rumah: lokasi, ukuran, usia bangunan, akses transportasi, dan lain-lain. Dalam studi kasus ini, kita akan membangun model regresi berganda untuk memprediksi harga rumah berdasarkan beberapa fitur utama.

### Langkah Analisis Lengkap

```python
# ============================================================
# STUDI KASUS: Prediksi Harga Rumah di Jakarta
# ============================================================

# Langkah 1: EDA
print("=== Langkah 1: Eksplorasi Data ===")
print(rumah.describe().round(1))
print(f"\nKorelasi dengan harga:")
for col in ['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']:
    r, p = stats.pearsonr(rumah[col], rumah['harga_juta'])
    sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
    print(f"  {col:<20}: r = {r:+.3f} {sig}")

# Langkah 2: Bangun model
print("\n=== Langkah 2: Model Regresi Berganda ===")
X_full = sm.add_constant(rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']])
model_full = sm.OLS(rumah['harga_juta'], X_full).fit()
print(model_full.summary())

# Langkah 3: Cek VIF
print("\n=== Langkah 3: Multicollinearity Check ===")
X_check = rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']]
for i, col in enumerate(X_check.columns):
    vif = variance_inflation_factor(X_check.values, i)
    print(f"  VIF {col}: {vif:.2f}")

# Langkah 4: Diagnostik Residual
print("\n=== Langkah 4: Diagnostik ===")
residuals_sk = model_full.resid
stat_sw, p_sw = stats.shapiro(residuals_sk)
print(f"  Normalitas (Shapiro-Wilk): p = {p_sw:.4f} → {'OK' if p_sw > 0.05 else 'Pelanggaran'}")

# Langkah 5: Prediksi
print("\n=== Langkah 5: Prediksi ===")
rumah_baru = pd.DataFrame({
    'const': [1],
    'luas_m2': [80],
    'jumlah_kamar': [3],
    'jarak_pusat_km': [15],
    'usia_tahun': [5]
})
prediksi = model_full.predict(rumah_baru)
print(f"Rumah: 80 m², 3 kamar, 15 km dari pusat, usia 5 tahun")
print(f"Prediksi harga: Rp {prediksi[0]:.0f} juta")

# Langkah 6: Confidence interval prediksi
pred_detail = model_full.get_prediction(rumah_baru)
pred_summary = pred_detail.summary_frame(alpha=0.05)
print(f"95% CI: Rp {pred_summary['obs_ci_lower'].values[0]:.0f} - "
      f"{pred_summary['obs_ci_upper'].values[0]:.0f} juta")
```

### Diskusi Studi Kasus

1. **Variabel mana yang paling berpengaruh?** Perhatikan magnitude koefisien dan p-value. Luas bangunan dan jarak ke pusat kota biasanya menjadi prediktor terkuat.
2. **Apakah model ini cukup baik?** Lihat Adjusted R² — jika di atas 0.7, model sudah cukup baik untuk prediksi kasar. Tapi untuk keputusan investasi, perlu model yang lebih komprehensif.
3. **Limitasi:** Dataset ini simulasi. Data riil akan memiliki lebih banyak variasi dan faktor yang tidak tercakup (misalnya: akses tol, sertifikat tanah, developer).
4. **Peluang perbaikan:** Tambahkan variabel seperti zona (Selatan/Utara/Barat/Timur), akses transportasi publik, atau status sertifikat.

---

## AI Corner: AI untuk Diagnostik dan Evaluasi Model

### Prompt yang Efektif

> "Saya membangun model regresi berganda untuk prediksi harga rumah. Ini output statsmodels summary saya: [paste output]. Tolong bantu: (1) apakah ada variabel yang tidak signifikan, (2) apakah model secara keseluruhan signifikan, (3) apa rekomendasi perbaikan?"

### Kapan AI Membantu

- Membaca dan menjelaskan output statsmodels yang kompleks
- Menyarankan transformasi variabel yang tepat untuk mengatasi pelanggaran asumsi
- Memeriksa apakah interpretasi koefisien kita sudah benar
- Menjelaskan konsep VIF dan multicollinearity dengan analogi sederhana

### Kapan Harus Kritis terhadap AI

- AI mungkin merekomendasikan penghapusan variabel hanya berdasarkan p-value tanpa mempertimbangkan teori atau konteks domain
- AI tidak selalu menyadari bahwa data kita simulasi vs data riil
- AI mungkin mengabaikan *practical significance* dan terlalu fokus pada *statistical significance*
- Keputusan feature selection harus didasarkan pada pemahaman domain, bukan hanya statistik

### Latihan AI-Augmented

Coba prompt berikut dan evaluasi hasilnya secara kritis:
1. "Jelaskan perbedaan R² dan Adjusted R² menggunakan analogi kehidupan sehari-hari"
2. "Q-Q plot saya menunjukkan titik-titik yang menyimpang di ujung. Apa artinya dan apa yang harus saya lakukan?"

---

## Latihan Mandiri

### Latihan 1: Membangun Model Regresi Berganda (20 menit)

Menggunakan dataset rumah (atau buat dataset sendiri), lakukan:

a. Bangun model regresi dengan **2 prediktor** saja (luas dan jarak pusat kota)
b. Bangun model regresi dengan **4 prediktor** (semua variabel)
c. Bandingkan R² dan Adjusted R² kedua model
d. Model mana yang lebih baik? Gunakan Adjusted R² untuk menjawab

### Latihan 2: Diagnostik Residual (20 menit)

Untuk model 4 prediktor:

a. Buat 4 plot diagnostik: (1) Residual vs Fitted, (2) Q-Q Plot, (3) Histogram residual, (4) Scale-Location
b. Lakukan Shapiro-Wilk test untuk normalitas residual
c. Identifikasi apakah ada pelanggaran asumsi
d. Jika ada pelanggaran, apa rekomendasi tindakan?

### Latihan 3: Multicollinearity (15 menit)

a. Hitung VIF untuk setiap prediktor
b. Adakah variabel dengan VIF > 5? Jika ya, apa yang sebaiknya dilakukan?
c. Coba tambahkan variabel baru `luas_tanah = luas_m2 * 1.5 + noise`. Hitung ulang VIF. Apa yang terjadi?

### Latihan 4: Feature Selection Sederhana (15 menit)

Lakukan **backward elimination** secara manual:

a. Mulai dari model dengan semua 4 prediktor
b. Lihat p-value setiap variabel dari output statsmodels
c. Hapus variabel dengan p-value tertinggi (jika > 0.05)
d. Fit ulang model dan ulangi
e. Kapan kita berhenti menghapus variabel?

### Latihan 5: Prediksi dan Evaluasi (10 menit)

a. Gunakan model terbaik untuk memprediksi harga rumah dengan spesifikasi: 120 m², 4 kamar, 10 km dari pusat, usia 2 tahun
b. Berapa confidence interval 95% untuk prediksi tersebut?
c. Apakah prediksi ini masuk akal untuk konteks Jakarta? Diskusikan limitasi model.

---

## Rangkuman

| Konsep | Poin Kunci |
|--------|-----------|
| Regresi Berganda | ŷ = b₀ + b₁x₁ + ... + bₚxₚ; memperluas regresi sederhana dengan banyak prediktor |
| Interpretasi Koefisien | "Jika X naik 1 unit, **ceteris paribus**, Y diperkirakan berubah b unit" |
| R² vs Adjusted R² | Adjusted R² menambah penalti untuk prediktor; lebih tepat untuk model berganda |
| Diagnostik Residual | Cek linearitas, normalitas (Q-Q plot), homoscedasticity, independence |
| Multicollinearity | Prediktor saling berkorelasi kuat; deteksi dengan VIF; VIF > 10 = serius |
| Feature Selection | Forward (tambahkan) vs Backward (kurangi); konsep dasar pemilihan model |

---

## Referensi

1. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics* (4th ed.), Chapter 9: Multiple and Logistic Regression.
2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning (ISLP)*, Chapter 3: Linear Regression.
3. Bruce, P., & Bruce, A. (2020). *Practical Statistics for Data Scientists* (2nd ed.), Chapter 4: Regression and Prediction.
4. scikit-learn Documentation: [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
5. statsmodels Documentation: [OLS Regression](https://www.statsmodels.org/stable/regression.html)
6. statsmodels Documentation: [Variance Inflation Factor](https://www.statsmodels.org/stable/generated/statsmodels.stats.outliers_influence.variance_inflation_factor.html)

---

*Modul ini adalah bagian dari mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia. Semester Genap 2025/2026.*
