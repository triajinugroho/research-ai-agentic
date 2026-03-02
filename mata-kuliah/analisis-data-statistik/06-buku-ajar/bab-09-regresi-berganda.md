# BAB 9: REGRESI BERGANDA DAN EVALUASI MODEL

**Tri Aji Nugroho, S.T., M.T.**
Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-5.6 | Membangun model regresi linear berganda dengan lebih dari satu prediktor dan menginterpretasi koefisiennya | C4 |
| CPMK-5.7 | Membedakan R² dan Adjusted R², serta menjelaskan kapan masing-masing digunakan | C4 |
| CPMK-5.8 | Mendeteksi multicollinearity menggunakan VIF dan menerapkan strategi penanganannya | C4 |
| CPMK-5.9 | Melakukan diagnostik residual (normalitas, homoscedasticity, independence) untuk mengevaluasi validitas model | C5 |
| CPMK-5.10 | Mengevaluasi dan membandingkan model regresi menggunakan metrik MSE, RMSE, MAE, serta konsep cross-validation | C5 |

---

## 9.1 Dari Regresi Sederhana ke Regresi Berganda

### 9.1.1 Keterbatasan Satu Prediktor

Pada Bab 8, kita memodelkan hubungan antara **satu** variabel independen dan satu variabel dependen. Dalam kenyataannya, hampir tidak ada fenomena yang bisa dijelaskan secara memadai oleh satu faktor saja.

**Contoh:** Memprediksi harga rumah di Jakarta hanya dari luas bangunan mengabaikan faktor-faktor krusial lainnya:

```
Model Sederhana (1 prediktor):
  Harga = b₀ + b₁(Luas)                          → R² = 0.55

Model Berganda (4 prediktor):
  Harga = b₀ + b₁(Luas) + b₂(Kamar) + b₃(Jarak) + b₄(Usia)  → R² = 0.87
```

> "All models are wrong, but some are useful."
> — George E. P. Box

### 9.1.2 Persamaan Model Regresi Berganda

Model regresi linear berganda dengan p prediktor:

```
ŷ = b₀ + b₁x₁ + b₂x₂ + ... + bₚxₚ
```

Dalam notasi populasi:

```
Y = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ + ε       di mana ε ~ N(0, σ²)
```

- **β₀** = intercept (nilai Y ketika semua X = 0)
- **β₁, ..., βₚ** = koefisien regresi untuk masing-masing prediktor
- **ε** = error term (residual)
- **p** = jumlah prediktor

### 9.1.3 Notasi Matriks (Gambaran Umum)

Untuk komputasi, model ditulis sebagai **Y = Xβ + ε** dengan solusi OLS:

```
β̂ = (XᵀX)⁻¹Xᵀy
```

```
      ┌  y₁  ┐       ┌ 1  x₁₁  x₁₂  ...  x₁ₚ ┐       ┌  β₀  ┐
 Y =  │  .   │  X =  │ .   .    .   ...   .   │  β =  │  .   │
      └  yₙ  ┘       └ 1  xₙ₁  xₙ₂  ...  xₙₚ ┘       └  βₚ  ┘
     (n x 1)               (n x (p+1))                ((p+1) x 1)
```

> **Catatan:** Python (`sklearn`, `statsmodels`) menghitung ini secara otomatis. Memahami bahwa regresi berganda adalah operasi matriks membantu menjelaskan mengapa multicollinearity menjadi masalah — matriks XᵀX menjadi hampir singular.

### 9.1.4 Visualisasi Konseptual

```
REGRESI SEDERHANA              REGRESI BERGANDA

  Y                              Y
  │     /                        │     /|
  │    /  garis regresi          │    / |  bidang regresi
  │   /                          │   /  |
  │  /                           │  /   |
  │ /                            │ /    |
  └──────── X₁                   └──────── X₁
                                 /
  1 prediktor → garis (2D)     X₂
                                 p prediktor → hyperplane
```

---

## 9.2 Interpretasi Koefisien

### 9.2.1 Prinsip *Ceteris Paribus*

Kata kunci wajib: ***"holding other variables constant"*** (ceteris paribus).

**Template interpretasi:**

> "Jika X₁ naik 1 unit, **dengan asumsi semua variabel lain tetap**, maka ŷ diperkirakan berubah sebesar b₁ unit."

### 9.2.2 Contoh Interpretasi

Misalkan model menghasilkan:

```
Harga = 200 + 8.5(Luas) + 50(Jml_Kamar) - 15(Jarak_km) - 5(Usia_tahun)
```

| Koefisien | Interpretasi |
|-----------|-------------|
| b₁ = 8.5 | Setiap tambahan 1 m² luas, harga naik Rp 8.5 juta, **ceteris paribus** |
| b₂ = 50 | Setiap tambahan 1 kamar, harga naik Rp 50 juta, **ceteris paribus** |
| b₃ = -15 | Setiap tambahan 1 km dari pusat, harga **turun** Rp 15 juta, **ceteris paribus** |
| b₄ = -5 | Setiap tambahan 1 tahun usia bangunan, harga **turun** Rp 5 juta, **ceteris paribus** |

> **Perhatian:** Interpretasi *ceteris paribus* bersifat **statistik**, bukan kausal. Dalam praktik, variabel-variabel sering saling berkaitan (rumah luas biasanya punya lebih banyak kamar).

### 9.2.3 Koefisien Terstandarisasi

Koefisien biasa tidak bisa dibandingkan langsung karena skala berbeda. **Koefisien terstandarisasi** (β*) mengatasi ini:

```
β*ⱼ = bⱼ × (sⱼ / sᵧ)
```

Artinya: "Jika Xⱼ naik 1 standar deviasi, Y berubah β*ⱼ standar deviasi." Prediktor dengan |β*| terbesar memiliki pengaruh paling besar.

---

## 9.3 R² vs Adjusted R²

### 9.3.1 Masalah R² dalam Regresi Berganda

R² akan **selalu naik** ketika prediktor baru ditambahkan — bahkan jika prediktor tersebut tidak berguna. Model selalu bisa "memeras" sedikit informasi dari variabel tambahan meskipun itu hanya *noise*.

### 9.3.2 Adjusted R² sebagai Solusi

Adjusted R² memberikan **penalti** untuk setiap prediktor tambahan:

```
                    (1 - R²)(n - 1)
Adjusted R² = 1 - ─────────────────
                     (n - p - 1)
```

| Aspek | R² | Adjusted R² |
|-------|-----|-------------|
| Perilaku | Selalu naik jika prediktor bertambah | Bisa **turun** jika prediktor tidak berguna |
| Kegunaan utama | Model dengan prediktor sama | Membandingkan model dengan prediktor **berbeda** |
| Range | 0 - 1 | Bisa < 0 (model sangat buruk) |

**Aturan:** Jika Adjusted R² **turun** saat prediktor ditambahkan, prediktor tersebut sebaiknya dihapus.

### 9.3.3 Demonstrasi Python

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm

np.random.seed(2025)
n = 100
luas = np.random.uniform(36, 200, n)
kamar = np.random.choice([2, 3, 4, 5], n, p=[0.2, 0.4, 0.3, 0.1])
jarak = np.random.uniform(3, 40, n)
usia = np.random.uniform(0, 30, n)
harga = 200 + 8.5*luas + 50*kamar - 15*jarak - 5*usia + np.random.normal(0, 100, n)

rumah = pd.DataFrame({
    'luas_m2': luas.round(1), 'jumlah_kamar': kamar,
    'jarak_pusat_km': jarak.round(1), 'usia_tahun': usia.round(1),
    'harga_juta': harga.round(1)
})
y = rumah['harga_juta']

# Model 1: 4 prediktor berguna
X1 = sm.add_constant(rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']])
m1 = sm.OLS(y, X1).fit()

# Model 2: 4 prediktor + 1 noise
rumah['noise'] = np.random.randn(n)
X2 = sm.add_constant(rumah[['luas_m2','jumlah_kamar','jarak_pusat_km','usia_tahun','noise']])
m2 = sm.OLS(y, X2).fit()

print(f"{'Metrik':<16} {'4 Prediktor':<16} {'4 + Noise':<16}")
print(f"{'─'*48}")
print(f"{'R²':<16} {m1.rsquared:<16.6f} {m2.rsquared:<16.6f}")
print(f"{'Adjusted R²':<16} {m1.rsquared_adj:<16.6f} {m2.rsquared_adj:<16.6f}")
print(f"\nR² naik, Adjusted R² TURUN → noise dihukum!")
```

---

## 9.4 Multicollinearity

### 9.4.1 Pengertian dan Dampak

Multicollinearity terjadi ketika prediktor **sangat berkorelasi** satu sama lain, menyebabkan:

```
┌────────────────────────────────────────────────────────┐
│  DAMPAK MULTICOLLINEARITY                              │
│  1. Koefisien regresi TIDAK STABIL                     │
│  2. Standard error koefisien MEMBESAR                  │
│  3. SULIT menentukan kontribusi individu prediktor     │
│  4. p-value bisa MENYESATKAN                           │
└────────────────────────────────────────────────────────┘
```

**Contoh:** Memasukkan "luas bangunan" dan "luas tanah" sebagai prediktor — keduanya biasanya sangat berkorelasi.

### 9.4.2 Variance Inflation Factor (VIF)

```
VIF(j) = 1 / (1 - Rⱼ²)
```

Di mana Rⱼ² adalah R² dari regresi Xⱼ terhadap **semua prediktor lain**.

| VIF | Tingkat | Tindakan |
|-----|---------|----------|
| 1 | Tidak ada multicollinearity | Aman |
| 1 - 5 | Ringan | Masih bisa diterima |
| 5 - 10 | Moderat | Perlu investigasi |
| > 10 | Serius | Hapus variabel, gabungkan, atau gunakan PCA |

### 9.4.3 Implementasi VIF dengan Python

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor

X_vif = rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']]
vif_data = pd.DataFrame({
    'Variabel': X_vif.columns,
    'VIF': [variance_inflation_factor(X_vif.values, i) for i in range(X_vif.shape[1])]
})
vif_data['Status'] = vif_data['VIF'].apply(
    lambda v: "Aman" if v < 5 else "PERHATIAN" if v < 10 else "SERIUS")

print("=== Variance Inflation Factor (VIF) ===")
print(vif_data.to_string(index=False))
```

---

## 9.5 Feature Selection (Pemilihan Variabel)

Tidak semua variabel yang tersedia perlu dimasukkan ke model. Terlalu banyak variabel bisa menyebabkan *overfitting* dan multicollinearity.

### 9.5.1 Forward Selection

```
Langkah 0: ŷ = b₀                                       (hanya intercept)
Langkah 1: ŷ = b₀ + b₁(Luas)                  Adj R² = 0.55  ↑
Langkah 2: ŷ = b₀ + b₁(Luas) + b₂(Jarak)      Adj R² = 0.72  ↑
Langkah 3: ŷ = b₀ + ... + b₃(Kamar)            Adj R² = 0.83  ↑
Langkah 4: ŷ = b₀ + ... + b₄(Noise)            Adj R² = 0.83  → BERHENTI
```

### 9.5.2 Backward Elimination

```
Langkah 0: Model penuh (semua prediktor)
Langkah 1: Hapus variabel dengan p-value tertinggi (jika > 0.05)
Langkah 2: Fit ulang, ulangi langkah 1
Langkah 3: Semua variabel tersisa signifikan → BERHENTI
```

> **Catatan:** Teknik lebih lanjut (stepwise, LASSO, Elastic Net) dipelajari di mata kuliah Machine Learning.

---

## 9.6 Evaluasi Model Regresi

### 9.6.1 Metrik Evaluasi

```
MSE  = (1/n) × Σ(yᵢ - ŷᵢ)²       Mean Squared Error
RMSE = √MSE                         Root Mean Squared Error
MAE  = (1/n) × Σ|yᵢ - ŷᵢ|         Mean Absolute Error
```

| Metrik | Satuan | Sensitivitas Outlier | Kapan Digunakan |
|--------|--------|---------------------|-----------------|
| **MSE** | Satuan² | Sangat sensitif | Optimasi matematis |
| **RMSE** | Satuan asli | Sensitif | Pelaporan error (paling umum) |
| **MAE** | Satuan asli | Kurang sensitif | Jika outlier banyak |

**Tips:** Jika RMSE jauh lebih besar dari MAE, kemungkinan ada outlier besar dalam prediksi.

### 9.6.2 Menghitung Metrik dengan Python

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

y_pred = m1.predict(X1)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y, y_pred)

print(f"MSE  : {mse:,.2f} (juta Rp)²")
print(f"RMSE : {rmse:,.2f} juta Rp")
print(f"MAE  : {mae:,.2f} juta Rp")
print(f"R²   : {r2_score(y, y_pred):.4f}")
```

### 9.6.3 Cross-Validation: Pengantar

Evaluasi pada data yang **sama** dengan data training terlalu optimis. **Cross-validation** membagi data menjadi beberapa *fold*:

```
5-FOLD CROSS-VALIDATION
────────────────────────
Fold 1: [TEST] [Train] [Train] [Train] [Train]  → RMSE₁
Fold 2: [Train] [TEST] [Train] [Train] [Train]  → RMSE₂
Fold 3: [Train] [Train] [TEST] [Train] [Train]  → RMSE₃
Fold 4: [Train] [Train] [Train] [TEST] [Train]  → RMSE₄
Fold 5: [Train] [Train] [Train] [Train] [TEST]  → RMSE₅

Rata-rata RMSE = (RMSE₁ + ... + RMSE₅) / 5
```

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

X = rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']]
model_cv = LinearRegression()
cv_scores = cross_val_score(model_cv, X, y, cv=5, scoring='neg_mean_squared_error')
cv_rmse = np.sqrt(-cv_scores)

print("=== 5-Fold Cross-Validation ===")
for i, val in enumerate(cv_rmse, 1):
    print(f"  Fold {i}: RMSE = {val:.2f} juta Rp")
print(f"\nRata-rata RMSE: {cv_rmse.mean():.2f} +/- {cv_rmse.std():.2f}")
```

---

## 9.7 Diagnostik Residual

### 9.7.1 Empat Asumsi yang Harus Diperiksa

```
┌─────────────────────┬──────────────────────────────────────┐
│ Asumsi              │ Cara Pemeriksaan                     │
├─────────────────────┼──────────────────────────────────────┤
│ 1. Linearitas       │ Residual vs Fitted plot              │
│ 2. Normalitas       │ Q-Q Plot, Shapiro-Wilk test          │
│ 3. Homoscedasticity │ Scale-Location plot                  │
│ 4. Independence     │ Durbin-Watson test                   │
└─────────────────────┴──────────────────────────────────────┘
```

### 9.7.2 Visual Diagnostik

```
LINEARITAS                         NORMALITAS (Q-Q Plot)
 Baik (acak):    Buruk (pola):      Baik:           Buruk:
   •  •              •     •         │      •••/     │        ••
 •    •  •        •          •       │    ••/        │     ••
──────•──── 0      •          •      │  •/           │  •••
   •   •         ──────────── 0      │•/             │••
 •     • •          •     •          └──────         └──────

HOMOSCEDASTICITY
 Baik (lebar tetap):              Buruk (funnel):
  │ •  •  •  •  •                 │        •  •
  ────────────── 0                │     •  •  •
  │ •  •  •  •  •                ──•──•──────── 0
  └──────────────                │•
```

### 9.7.3 Implementasi Diagnostik Lengkap

```python
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.stattools import durbin_watson

# Model dari bagian sebelumnya
X_sm = sm.add_constant(rumah[['luas_m2','jumlah_kamar','jarak_pusat_km','usia_tahun']])
model_sm = sm.OLS(rumah['harga_juta'], X_sm).fit()

y_pred = model_sm.predict(X_sm)
residuals = model_sm.resid

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Residual vs Fitted
axes[0,0].scatter(y_pred, residuals, alpha=0.6, color='steelblue', edgecolor='white')
axes[0,0].axhline(y=0, color='red', linestyle='--')
axes[0,0].set_xlabel('Fitted Values'); axes[0,0].set_ylabel('Residuals')
axes[0,0].set_title('1. Residual vs Fitted (Linearitas & Homoscedasticity)')

# 2. Q-Q Plot
stats.probplot(residuals, dist="norm", plot=axes[0,1])
axes[0,1].set_title('2. Q-Q Plot (Normalitas)')

# 3. Histogram Residual
axes[1,0].hist(residuals, bins=20, color='steelblue', edgecolor='white', density=True)
x_norm = np.linspace(residuals.min(), residuals.max(), 100)
axes[1,0].plot(x_norm, stats.norm.pdf(x_norm, residuals.mean(), residuals.std()), 'r-')
axes[1,0].set_title('3. Histogram Residual')

# 4. Scale-Location
axes[1,1].scatter(y_pred, np.sqrt(np.abs(residuals)), alpha=0.6, color='coral')
axes[1,1].set_title('4. Scale-Location (Homoscedasticity)')

plt.suptitle('Diagnostik Residual', fontsize=14, y=1.01)
plt.tight_layout()
plt.show()

# Uji formal
stat_sw, p_sw = stats.shapiro(residuals)
dw = durbin_watson(residuals)
print(f"Shapiro-Wilk: W={stat_sw:.4f}, p={p_sw:.4f} -> "
      f"{'Normal' if p_sw > 0.05 else 'TIDAK Normal'}")
print(f"Durbin-Watson: {dw:.4f} -> "
      f"{'OK (independen)' if 1.5 < dw < 2.5 else 'Perlu investigasi'}")
```

---

## 9.8 Implementasi Python: sklearn vs statsmodels

### 9.8.1 Kapan Menggunakan Masing-masing?

```
┌──────────────────────────────────────────────────────┐
│  sklearn:                                            │
│  + Cepat untuk prediksi & pipeline ML                │
│  + train_test_split, cross_val_score                 │
│  - Tidak ada p-value, CI, uji signifikansi           │
│                                                      │
│  statsmodels:                                        │
│  + Output lengkap (p-value, CI, F-test, diagnostik)  │
│  + Cocok untuk inferensi dan interpretasi             │
│  - Kurang praktis untuk pipeline ML besar             │
│                                                      │
│  Rekomendasi: gunakan KEDUANYA                       │
│  → Analisis & interpretasi  → statsmodels            │
│  → Prediksi & deployment    → sklearn                │
└──────────────────────────────────────────────────────┘
```

### 9.8.2 Workflow Lengkap

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm

# Siapkan data
X = rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']]
y = rumah['harga_juta']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- sklearn: untuk prediksi ---
model_sk = LinearRegression().fit(X_train, y_train)
y_pred_sk = model_sk.predict(X_test)
print(f"=== sklearn (Data Testing) ===")
print(f"R² : {r2_score(y_test, y_pred_sk):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_sk)):.2f} juta Rp")
print(f"\nKoefisien:")
for nama, koef in zip(X.columns, model_sk.coef_):
    print(f"  {nama:20s}: {koef:.4f}")

# --- statsmodels: untuk analisis ---
X_train_sm = sm.add_constant(X_train)
model_ols = sm.OLS(y_train, X_train_sm).fit()
print(f"\n=== statsmodels OLS Summary ===")
print(model_ols.summary())

# Identifikasi variabel signifikan
print("\n=== Signifikansi (alpha = 0.05) ===")
for var in X.columns:
    p = model_ols.pvalues[var]
    print(f"  {var:20s}: p={p:.4f} -> {'SIGNIFIKAN' if p < 0.05 else 'tidak signifikan'}")
```

---

## 9.9 Studi Kasus: Prediksi Harga Properti Indonesia

### 9.9.1 Konteks

Pasar properti Indonesia, khususnya di Jabodetabek, dipengaruhi berbagai faktor. Kita akan membangun model regresi berganda dan mengikuti alur lengkap: EDA, pemodelan, diagnostik, dan evaluasi.

### 9.9.2 Analisis Lengkap

```python
import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# --- Data ---
np.random.seed(2025)
n = 150
luas = np.random.uniform(36, 250, n)
kamar = np.random.choice([2, 3, 4, 5], n, p=[0.15, 0.40, 0.30, 0.15])
jarak = np.random.uniform(5, 50, n)
usia = np.random.uniform(0, 35, n)
lebar_jalan = np.random.uniform(4, 12, n)
harga = 300 + 9*luas + 55*kamar - 12*jarak - 4.5*usia + 20*lebar_jalan + np.random.normal(0, 120, n)

properti = pd.DataFrame({
    'luas_m2': luas.round(1), 'jumlah_kamar': kamar,
    'jarak_pusat_km': jarak.round(1), 'usia_tahun': usia.round(1),
    'lebar_jalan_m': lebar_jalan.round(1), 'harga_juta': harga.round(1)
})

# --- EDA ---
print("=== Korelasi dengan Harga ===")
for col in properti.columns[:-1]:
    r, p = stats.pearsonr(properti[col], properti['harga_juta'])
    sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
    print(f"  {col:<20}: r = {r:+.3f} {sig}")

# --- Model ---
fitur = ['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun', 'lebar_jalan_m']
X = properti[fitur]; y = properti['harga_juta']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_sm = sm.add_constant(X_train)
model = sm.OLS(y_train, X_sm).fit()
print(model.summary())

# --- VIF ---
print("\n=== VIF ===")
for i, col in enumerate(fitur):
    vif = variance_inflation_factor(X.values, i)
    print(f"  {col:<20}: VIF = {vif:.2f}")

# --- Evaluasi Testing ---
X_test_sm = sm.add_constant(X_test)
y_pred = model.predict(X_test_sm)
print(f"\n=== Evaluasi (Testing) ===")
print(f"R²  : {r2_score(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f} juta Rp")
print(f"MAE : {mean_absolute_error(y_test, y_pred):.2f} juta Rp")

# --- Prediksi Rumah Baru ---
rumah_baru = pd.DataFrame({'const': [1], 'luas_m2': [100], 'jumlah_kamar': [3],
    'jarak_pusat_km': [20], 'usia_tahun': [5], 'lebar_jalan_m': [8]})
pred = model.predict(rumah_baru)
ci = model.get_prediction(rumah_baru).summary_frame(alpha=0.05)
print(f"\nPrediksi rumah 100m2, 3 kamar, 20 km: Rp {pred[0]:.0f} juta")
print(f"95% CI: Rp {ci['obs_ci_lower'].values[0]:.0f} - {ci['obs_ci_upper'].values[0]:.0f} juta")
```

### 9.9.3 Diskusi

1. **Variabel terkuat:** Luas bangunan dan jarak ke pusat kota biasanya menjadi prediktor terkuat — sesuai dengan realita pasar properti Jakarta.
2. **Kualitas model:** Adjusted R² di atas 0.7 menunjukkan model cukup baik untuk prediksi kasar, tetapi keputusan investasi memerlukan model lebih komprehensif.
3. **Limitasi:** Dataset simulasi. Data riil memiliki lebih banyak variasi (akses tol, sertifikat tanah, developer, fasilitas publik).

---

## 9.10 Studi Kasus: Analisis Faktor Kelulusan Mahasiswa

### 9.10.1 Konteks dan Implementasi

Universitas ingin mengetahui faktor-faktor yang paling mempengaruhi IPK mahasiswa.

```python
# --- Data Mahasiswa ---
np.random.seed(2024)
n = 150
jam_belajar = np.random.uniform(5, 30, n)
kehadiran = np.random.uniform(50, 100, n)
jam_tidur = np.random.uniform(4, 9, n)
penghasilan_ortu = np.random.uniform(3, 25, n)
jarak_kampus = np.random.uniform(1, 40, n)
ipk = np.clip(1.5 + 0.03*jam_belajar + 0.012*kehadiran + 0.08*jam_tidur
              + 0.005*penghasilan_ortu - 0.002*jarak_kampus
              + np.random.normal(0, 0.15, n), 1.0, 4.0)

mhs = pd.DataFrame({
    'jam_belajar': jam_belajar.round(1), 'kehadiran_persen': kehadiran.round(1),
    'jam_tidur': jam_tidur.round(1), 'penghasilan_ortu_juta': penghasilan_ortu.round(1),
    'jarak_kampus_km': jarak_kampus.round(1), 'ipk': ipk.round(2)
})

# --- Model ---
fitur_mhs = ['jam_belajar', 'kehadiran_persen', 'jam_tidur',
             'penghasilan_ortu_juta', 'jarak_kampus_km']
X_mhs = sm.add_constant(mhs[fitur_mhs])
model_ipk = sm.OLS(mhs['ipk'], X_mhs).fit()
print(model_ipk.summary())

# --- Feature Importance (Koefisien Terstandarisasi) ---
from sklearn.preprocessing import StandardScaler
X_scaled = StandardScaler().fit_transform(mhs[fitur_mhs])
model_std = LinearRegression().fit(X_scaled, mhs['ipk'])

importance = pd.DataFrame({
    'Variabel': fitur_mhs, 'Beta_Std': model_std.coef_
}).sort_values('Beta_Std', key=abs, ascending=True)

plt.figure(figsize=(10, 5))
colors = ['green' if x > 0 else 'red' for x in importance['Beta_Std']]
plt.barh(importance['Variabel'], importance['Beta_Std'], color=colors, alpha=0.7)
plt.xlabel('Koefisien Terstandarisasi')
plt.title('Faktor yang Mempengaruhi IPK\n(Hijau = positif, Merah = negatif)')
plt.axvline(x=0, color='black', linewidth=0.5)
plt.tight_layout()
plt.show()
```

### 9.10.2 Temuan Utama

- **Jam belajar, kehadiran, dan jam tidur** adalah faktor dominan — sesuai intuisi pendidikan.
- **Penghasilan orang tua** berpengaruh kecil; **jarak kampus** berpengaruh negatif minor.
- Model ini dapat digunakan universitas untuk merancang program intervensi akademik bagi mahasiswa berisiko.

---

## AI Corner: Memanfaatkan AI untuk Pemodelan Regresi

### Apa yang Bisa AI Bantu?

| AI Bisa Membantu | AI Tidak Bisa Menggantikan |
|-------------------|---------------------------|
| Menulis kode regresi berganda | Memilih variabel berdasarkan domain knowledge |
| Menjelaskan output OLS summary | Memutuskan apakah model layak untuk keputusan bisnis |
| Menyarankan cara mengatasi multicollinearity | Menjamin hubungan kausal (bukan hanya korelasi) |
| Menginterpretasi Q-Q plot | Memahami konteks pasar properti Indonesia |

### Contoh Prompt Efektif

```
Saya membangun model regresi berganda untuk prediksi harga rumah di Jakarta.
Ini output OLS summary saya: [paste output]. Tolong bantu:
1. Variabel mana yang signifikan dan mana yang tidak?
2. Apakah Adjusted R² sudah cukup baik?
3. VIF luas_m2 = 7.2 — apakah ini masalah?
4. Apa rekomendasi perbaikan model?
```

### Kapan Harus Kritis

- AI mungkin merekomendasikan menghapus variabel **hanya** berdasarkan p-value, tanpa mempertimbangkan teori
- AI tidak selalu membedakan *statistical significance* vs *practical significance*
- Keputusan feature selection harus berdasarkan **domain knowledge + bukti statistik**

---

## Rangkuman Bab 9

1. **Regresi linear berganda** memperluas regresi sederhana dengan banyak prediktor: ŷ = b₀ + b₁x₁ + ... + bₚxₚ, memungkinkan model yang lebih realistis.

2. **Interpretasi koefisien** harus selalu menyertakan *"ceteris paribus"* — perubahan Y untuk setiap kenaikan 1 unit Xⱼ, dengan semua variabel lain dikontrol konstan.

3. **Adjusted R²** lebih tepat dari R² untuk membandingkan model dengan jumlah prediktor berbeda, karena memberikan penalti untuk prediktor yang tidak berguna.

4. **Multicollinearity** (prediktor saling berkorelasi tinggi) menyebabkan koefisien tidak stabil. Gunakan **VIF** untuk deteksi: VIF > 10 menandakan masalah serius.

5. **Diagnostik residual** wajib dilakukan: linearitas, normalitas (Q-Q plot), homoscedasticity (scale-location plot), dan independence (Durbin-Watson).

6. **MSE, RMSE, MAE** mengukur akurasi prediksi. RMSE paling umum karena bersatuan sama dengan variabel dependen.

7. **Cross-validation** memberikan estimasi performa yang lebih jujur dibanding evaluasi pada data training saja.

8. Gunakan **statsmodels** untuk analisis/interpretasi dan **sklearn** untuk prediksi/deployment — keduanya saling melengkapi.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan antara regresi linear sederhana dan regresi linear berganda. Berikan masing-masing satu contoh penerapan dalam konteks Indonesia.

**Soal 2.** Perhatikan model regresi berikut:

```
IPK = 1.2 + 0.04(Jam_Belajar) + 0.015(Kehadiran) - 0.003(Jarak_Kampus)
```

- a) Identifikasi variabel dependen dan variabel independen.
- b) Berapa nilai intercept dan apa artinya?
- c) Interpretasikan koefisien Jam_Belajar dengan prinsip *ceteris paribus*.
- d) Prediksi IPK mahasiswa: belajar 20 jam/minggu, kehadiran 85%, jarak 10 km.

**Soal 3.** Jelaskan mengapa R² selalu naik ketika prediktor ditambahkan, dan mengapa Adjusted R² bisa turun.

**Soal 4.** Sebutkan empat asumsi utama model regresi linear dan cara memeriksa masing-masing.

**Soal 5.** Apa itu multicollinearity? Sebutkan tiga dampak negatifnya terhadap model regresi.

### Tingkat Menengah (C2-C3)

**Soal 6.** Perhatikan tabel VIF berikut:

| Variabel | VIF |
|----------|-----|
| Luas bangunan | 8.5 |
| Luas tanah | 9.2 |
| Jumlah kamar | 3.1 |
| Jarak ke pusat kota | 1.8 |

- a) Variabel mana yang bermasalah? Mengapa luas bangunan dan luas tanah memiliki VIF tinggi?
- b) Berikan dua solusi untuk mengatasi masalah ini.
- c) Jika "luas tanah" dihapus, apa yang terjadi dengan VIF "luas bangunan"?

**Soal 7.** Tulis kode Python untuk: membuat dataset simulasi (n=100, 3 prediktor), membangun model regresi berganda dengan sklearn, dan menampilkan R² training vs R² testing (gunakan `train_test_split`).

**Soal 8.** Jelaskan perbedaan forward selection dan backward elimination. Kapan masing-masing lebih cocok?

**Soal 9.** Perhatikan perbandingan model:

| Model | Prediktor | R² | Adj. R² | RMSE |
|-------|-----------|-----|---------|------|
| A | 2 variabel | 0.72 | 0.71 | 145 |
| B | 5 variabel | 0.78 | 0.76 | 129 |
| C | 7 variabel | 0.79 | 0.74 | 135 |

- a) Model mana paling baik? Gunakan Adjusted R² dan RMSE untuk menjawab.
- b) Apa yang terjadi pada Model C? Mengapa R² naik tapi Adjusted R² turun?

### Tingkat Mahir (C3-C5)

**Soal 10.** Sebuah perusahaan e-commerce ingin memprediksi penjualan berdasarkan: budget iklan, jumlah produk, rating toko, usia toko, dan jumlah follower.

- a) Tulis kode Python lengkap: data simulasi (n=200), model regresi, diagnostik residual (4 plot), dan VIF.
- b) Lakukan backward elimination manual: hapus variabel tidak signifikan satu per satu, bandingkan Adjusted R².
- c) Lakukan 5-fold cross-validation dan laporkan rata-rata RMSE.

**Soal 11.** Evaluasi kritis: Seorang mahasiswa membangun model prediksi gaji karyawan startup dengan hasil R² training = 0.92, R² testing = 0.45, residual plot berbentuk funnel, dan level pendidikan dikodekan sebagai 1/2/3.

- a) Apa yang ditunjukkan perbedaan besar R² training vs testing?
- b) Apa masalah pola funnel pada residual plot?
- c) Apakah level pendidikan sebagai 1/2/3 sudah tepat? Apa alternatifnya?
- d) Berikan tiga rekomendasi perbaikan.

**Soal 12.** Tulis kode Python yang mengimplementasikan **backward elimination otomatis**: mulai dari semua prediktor, hapus variabel dengan p-value tertinggi (> 0.05) pada setiap iterasi, cetak Adjusted R² tiap langkah, berhenti ketika semua variabel signifikan.

**Soal 13.** Bandingkan model pada dataset California Housing (`sklearn.datasets.fetch_california_housing`):
- a) Model dengan semua 8 fitur (5-fold CV)
- b) Model dengan 4 fitur terbaik saja (5-fold CV)
- c) Apakah mengurangi fitur selalu menurunkan performa?

**Soal 14.** Seorang analyst menggunakan AI yang merekomendasikan menghapus variabel "jarak ke kampus" (p=0.08) dari model harga properti Bandung, padahal lokasi dekat kampus ITB/Unpad jelas mempengaruhi harga.

- a) Apakah rekomendasi AI tepat? Jelaskan pro dan kontra.
- b) Apa perbedaan *statistical significance* vs *practical significance*?
- c) Apa yang seharusnya dilakukan? Gunakan prinsip "Human + AI Collaboration".

---

## Referensi

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability & Statistics for Engineers & Scientists* (9th ed.). Pearson.
2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning with Applications in Python (ISLP)*, Chapter 3. Springer.
3. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics* (4th ed.), Chapter 9.
4. Bruce, P., & Bruce, A. (2020). *Practical Statistics for Data Scientists* (2nd ed.), Chapter 4. O'Reilly Media.
5. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
6. scikit-learn Documentation. *LinearRegression*. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
7. statsmodels Documentation. *OLS Regression*. https://www.statsmodels.org/stable/regression.html
8. Kutner, M. H., Nachtsheim, C. J., Neter, J., & Li, W. (2005). *Applied Linear Statistical Models* (5th ed.). McGraw-Hill.

---

*Bab berikutnya: **Bab 10 — Analysis of Variance (ANOVA)***
