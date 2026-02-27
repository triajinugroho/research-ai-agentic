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

Pada Bab 8 (Korelasi dan Regresi Linear Sederhana), kita memodelkan hubungan antara **satu** variabel independen (X) dan satu variabel dependen (Y). Dalam kenyataannya, hampir tidak ada fenomena yang bisa dijelaskan secara memadai oleh satu faktor saja.

**Contoh:** Memprediksi harga rumah di Jakarta hanya berdasarkan luas bangunan akan mengabaikan faktor-faktor krusial lainnya:

```
Model Sederhana (1 prediktor):
  Harga = b₀ + b₁(Luas)
  R² = 0.55  →  Hanya 55% variasi harga terjelaskan

Model Berganda (4 prediktor):
  Harga = b₀ + b₁(Luas) + b₂(Jml_Kamar) + b₃(Jarak_Pusat) + b₄(Usia)
  R² = 0.87  →  87% variasi harga terjelaskan — jauh lebih baik!
```

> "All models are wrong, but some are useful."
> — George E. P. Box

Regresi berganda (*multiple linear regression*) memungkinkan kita memasukkan **banyak prediktor** sekaligus, sehingga model lebih realistis dan prediksi lebih akurat.

### 9.1.2 Persamaan Model Regresi Berganda

Model regresi linear berganda dengan p prediktor ditulis sebagai:

```
ŷ = b₀ + b₁x₁ + b₂x₂ + ... + bₚxₚ
```

Atau dalam notasi populasi:

```
Y = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ + ε
```

Di mana:
- **Y** = variabel dependen (respons)
- **β₀** = intercept (nilai Y ketika semua X = 0)
- **β₁, β₂, ..., βₚ** = koefisien regresi (parameter populasi)
- **X₁, X₂, ..., Xₚ** = variabel independen (prediktor)
- **ε** = error term (residual), diasumsikan ε ~ N(0, σ²)
- **p** = jumlah prediktor

**Contoh konkret:**

```
Harga_Rumah = β₀ + β₁(Luas) + β₂(Jml_Kamar) + β₃(Jarak_Pusat_Kota) + ε
```

### 9.1.3 Notasi Matriks (Gambaran Umum)

Untuk keperluan komputasi, model regresi berganda lebih efisien ditulis dalam notasi matriks:

```
Y = Xβ + ε
```

Di mana:

```
        ┌  y₁  ┐         ┌ 1  x₁₁  x₁₂  ...  x₁ₚ ┐       ┌  β₀  ┐
        │  y₂  │         │ 1  x₂₁  x₂₂  ...  x₂ₚ │       │  β₁  │
  Y  =  │  .   │   X  =  │ .   .    .   ...   .   │  β =  │  .   │
        │  .   │         │ .   .    .   ...   .   │       │  .   │
        └  yₙ  ┘         └ 1  xₙ₁  xₙ₂  ...  xₙₚ ┘       └  βₚ  ┘
       (n x 1)                 (n x (p+1))                  ((p+1) x 1)
```

Solusi *Ordinary Least Squares* (OLS) dalam notasi matriks:

```
β̂ = (XᵀX)⁻¹Xᵀy
```

> **Catatan:** Anda tidak perlu menghitung invers matriks secara manual. Python (melalui `sklearn` dan `statsmodels`) melakukan komputasi ini secara otomatis. Namun, memahami bahwa regresi berganda pada dasarnya adalah **operasi matriks** membantu Anda memahami mengapa multicollinearity (korelasi tinggi antar prediktor) menjadi masalah — matriks XᵀX menjadi hampir singular (tidak bisa di-invers dengan stabil).

### 9.1.4 Visualisasi Konseptual

```
REGRESI SEDERHANA                    REGRESI BERGANDA
─────────────────                    ─────────────────

  Y                                    Y
  │     /                              │      Model = bidang/hyperplane
  │    /  garis regresi                │     /|
  │   /                                │    / |
  │  /                                 │   /  |
  │ /                                  │  /   |
  │/                                   │ /    |
  └──────────── X₁                     └──────────── X₁
                                       /
                                      /
                                    X₂

  1 prediktor → garis (2D)           2 prediktor → bidang (3D)
                                     p prediktor → hyperplane (p+1 dimensi)
```

---

## 9.2 Interpretasi Koefisien dalam Regresi Berganda

### 9.2.1 Prinsip *Ceteris Paribus*

Interpretasi koefisien dalam regresi berganda **berbeda secara fundamental** dari regresi sederhana. Kata kunci yang wajib diingat: ***"holding other variables constant"*** atau ***ceteris paribus*** (dengan variabel lain tetap).

**Template interpretasi:**

> "Jika X₁ naik 1 unit, **dengan asumsi semua variabel lain tetap (ceteris paribus)**, maka ŷ diperkirakan berubah sebesar b₁ unit."

### 9.2.2 Contoh Interpretasi

Misalkan model regresi menghasilkan:

```
Harga = 200 + 8.5(Luas) + 50(Jml_Kamar) - 15(Jarak_km) - 5(Usia_tahun)
```

| Koefisien | Nilai | Interpretasi |
|-----------|-------|-------------|
| b₀ = 200 | Intercept | Harga dasar ketika semua prediktor bernilai 0 (seringkali tidak bermakna secara praktis) |
| b₁ = 8.5 | Luas (m²) | Setiap tambahan 1 m² luas bangunan, harga naik Rp 8.5 juta, **ceteris paribus** |
| b₂ = 50 | Jml Kamar | Setiap tambahan 1 kamar, harga naik Rp 50 juta, **ceteris paribus** |
| b₃ = -15 | Jarak (km) | Setiap tambahan 1 km dari pusat kota, harga **turun** Rp 15 juta, **ceteris paribus** |
| b₄ = -5 | Usia (tahun) | Setiap tambahan 1 tahun usia bangunan, harga **turun** Rp 5 juta, **ceteris paribus** |

> **Perhatian:** Dalam praktik, sulit mengubah satu variabel tanpa mempengaruhi yang lain. Rumah dengan luas lebih besar biasanya memiliki lebih banyak kamar. Interpretasi *ceteris paribus* adalah interpretasi **statistik**, bukan kausal.

### 9.2.3 Koefisien Terstandarisasi (*Standardized Coefficients*)

Koefisien regresi biasa (b₁, b₂, ...) tidak bisa dibandingkan langsung karena skala variabel yang berbeda. Untuk mengetahui prediktor mana yang paling berpengaruh, kita menggunakan **koefisien terstandarisasi** (Beta, β*):

```
β*ⱼ = bⱼ × (sⱼ / sᵧ)
```

Di mana sⱼ adalah standar deviasi prediktor ke-j dan sᵧ adalah standar deviasi variabel dependen. Koefisien terstandarisasi menunjukkan: "Jika Xⱼ naik 1 standar deviasi, Y berubah β*ⱼ standar deviasi."

---

## 9.3 R² vs Adjusted R²

### 9.3.1 Masalah R² dalam Regresi Berganda

R² (*coefficient of determination*) mengukur proporsi variasi Y yang dijelaskan oleh model. Namun dalam regresi berganda, R² memiliki kelemahan serius:

> **R² akan selalu naik (atau minimal tetap) ketika prediktor baru ditambahkan — meskipun prediktor tersebut tidak berguna sama sekali!**

Ini terjadi karena model selalu bisa "memeras" sedikit informasi dari variabel tambahan, meskipun itu hanya kebetulan (*noise*).

### 9.3.2 Adjusted R² sebagai Solusi

Adjusted R² mengatasi masalah ini dengan memberikan **penalti** untuk setiap prediktor tambahan:

```
                    (1 - R²)(n - 1)
Adjusted R² = 1 - ─────────────────
                     (n - p - 1)
```

Di mana:
- n = jumlah observasi
- p = jumlah prediktor

### 9.3.3 Perbandingan R² dan Adjusted R²

| Aspek | R² | Adjusted R² |
|-------|-----|-------------|
| Perilaku | Selalu naik jika prediktor bertambah | Bisa **turun** jika prediktor tidak berguna |
| Kegunaan utama | Regresi sederhana (1 prediktor) | Regresi berganda (>1 prediktor) |
| Range | 0 sampai 1 | Bisa < 0 (model sangat buruk) |
| Kapan dipakai | Membandingkan model dengan jumlah prediktor **sama** | Membandingkan model dengan jumlah prediktor **berbeda** |

**Aturan praktis:** Jika Adjusted R² **turun** ketika prediktor ditambahkan, prediktor tersebut kemungkinan tidak berguna dan sebaiknya dihapus.

### 9.3.4 Demonstrasi dengan Python

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Simulasi data harga rumah
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

# Model dengan 4 prediktor berguna
X1 = sm.add_constant(rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']])
y = rumah['harga_juta']
model1 = sm.OLS(y, X1).fit()

# Model dengan 4 prediktor + 1 variabel acak (tidak berguna)
rumah['noise'] = np.random.randn(n)
X2 = sm.add_constant(rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun', 'noise']])
model2 = sm.OLS(y, X2).fit()

print("=== R² vs Adjusted R²: Efek Menambah Variabel Tidak Berguna ===")
print(f"{'Metrik':<20} {'4 Prediktor':<18} {'4 + Noise':<18}")
print(f"{'─'*56}")
print(f"{'R²':<20} {model1.rsquared:<18.6f} {model2.rsquared:<18.6f}")
print(f"{'Adjusted R²':<20} {model1.rsquared_adj:<18.6f} {model2.rsquared_adj:<18.6f}")
print(f"\nR² naik sedikit: +{model2.rsquared - model1.rsquared:.6f}")
print(f"Adjusted R² TURUN : {model2.rsquared_adj - model1.rsquared_adj:.6f}")
print("=> Adjusted R² 'menghukum' variabel tidak berguna!")
```

---

## 9.4 Multicollinearity

### 9.4.1 Apa itu Multicollinearity?

Multicollinearity terjadi ketika dua atau lebih variabel prediktor **sangat berkorelasi** satu sama lain. Ini menyebabkan:

```
DAMPAK MULTICOLLINEARITY
─────────────────────────
┌────────────────────────────────────────────────────────┐
│  1. Koefisien regresi TIDAK STABIL                     │
│     → berubah drastis jika data sedikit berubah        │
│                                                        │
│  2. Standard error koefisien MEMBESAR                  │
│     → confidence interval sangat lebar                 │
│                                                        │
│  3. SULIT menentukan kontribusi individu prediktor     │
│     → "siapa yang benar-benar berpengaruh?"            │
│                                                        │
│  4. p-value bisa menyesatkan                           │
│     → variabel penting terlihat tidak signifikan       │
└────────────────────────────────────────────────────────┘
```

**Contoh Indonesia:** Memasukkan "luas bangunan" dan "luas tanah" sebagai prediktor harga rumah. Keduanya biasanya sangat berkorelasi (rumah besar berdiri di atas tanah yang luas), sehingga model kesulitan memisahkan kontribusi masing-masing.

### 9.4.2 Variance Inflation Factor (VIF)

VIF mengukur seberapa besar variansi koefisien "membengkak" akibat korelasi dengan prediktor lain:

```
            1
VIF(j) = ─────────
          1 - Rⱼ²
```

Di mana Rⱼ² adalah R² dari regresi Xⱼ terhadap **semua prediktor lain**.

**Interpretasi VIF:**

| VIF | Tingkat | Tindakan |
|-----|---------|----------|
| 1 | Tidak ada multicollinearity | Aman |
| 1 - 5 | Ringan | Masih bisa diterima |
| 5 - 10 | Moderat | Perlu perhatian dan investigasi |
| > 10 | Serius | Perlu tindakan: hapus variabel, gabungkan, atau gunakan PCA |

### 9.4.3 Menghitung VIF dengan Python

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd

# Menggunakan dataset rumah dari bagian sebelumnya
X_vif = rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']]

vif_data = pd.DataFrame()
vif_data['Variabel'] = X_vif.columns
vif_data['VIF'] = [variance_inflation_factor(X_vif.values, i)
                   for i in range(X_vif.shape[1])]

def interpretasi_vif(vif):
    if vif < 5:
        return "Aman"
    elif vif < 10:
        return "PERHATIAN"
    else:
        return "SERIUS"

vif_data['Status'] = vif_data['VIF'].apply(interpretasi_vif)

print("=== Variance Inflation Factor (VIF) ===")
print(vif_data.to_string(index=False))
```

### 9.4.4 Solusi untuk Multicollinearity

1. **Hapus salah satu variabel** yang berkorelasi tinggi (pilih berdasarkan teori/domain knowledge)
2. **Gabungkan variabel** menjadi satu (misal: rata-rata atau PCA)
3. **Gunakan regularization** (Ridge atau LASSO regression — dibahas di mata kuliah Machine Learning)
4. **Kumpulkan lebih banyak data** (kadang membantu, tapi tidak selalu)

---

## 9.5 Feature Selection (Pemilihan Variabel)

### 9.5.1 Mengapa Perlu Feature Selection?

Tidak semua variabel yang tersedia perlu dimasukkan ke dalam model. Memasukkan terlalu banyak variabel bisa menyebabkan:
- **Overfitting** — model terlalu cocok dengan data latih, gagal di data baru
- **Multicollinearity** — variabel yang berkorelasi tinggi saling mengganggu
- **Interpretasi sulit** — model dengan 20 variabel sulit dijelaskan ke stakeholder

### 9.5.2 Forward Selection

```
FORWARD SELECTION
─────────────────
Langkah 0: Model kosong (hanya intercept)
           ŷ = b₀

Langkah 1: Tambahkan variabel TERBAIK
           ŷ = b₀ + b₁(Luas)         → Adj R² = 0.55

Langkah 2: Tambahkan variabel TERBAIK berikutnya
           ŷ = b₀ + b₁(Luas) + b₂(Jarak)  → Adj R² = 0.72

Langkah 3: Tambahkan variabel TERBAIK berikutnya
           ŷ = b₀ + b₁(Luas) + b₂(Jarak) + b₃(Kamar)  → Adj R² = 0.83

Langkah 4: Tambahkan variabel berikutnya
           → Adj R² = 0.83 (tidak naik signifikan) → BERHENTI
```

### 9.5.3 Backward Elimination

```
BACKWARD ELIMINATION
────────────────────
Langkah 0: Model penuh (semua prediktor)
           ŷ = b₀ + b₁X₁ + b₂X₂ + b₃X₃ + b₄X₄ + b₅X₅

Langkah 1: Hapus variabel PALING TIDAK signifikan (p-value tertinggi)
           Misal X₅ punya p-value = 0.82 → hapus X₅

Langkah 2: Fit ulang model, hapus variabel paling tidak signifikan
           Misal X₄ punya p-value = 0.15 → hapus X₄

Langkah 3: Semua variabel tersisa signifikan (p < 0.05) → BERHENTI
```

> **Catatan:** Feature selection di bab ini bersifat **konseptual**. Teknik lebih lanjut seperti stepwise regression, LASSO, dan Elastic Net akan dipelajari di mata kuliah Machine Learning.

---

## 9.6 Evaluasi Model Regresi

### 9.6.1 Metrik Evaluasi

```
METRIK EVALUASI MODEL REGRESI
──────────────────────────────

                        n
  MSE  = (1/n) × Σ (yᵢ - ŷᵢ)²      Mean Squared Error
                       i=1

  RMSE = √MSE                         Root Mean Squared Error

                        n
  MAE  = (1/n) × Σ |yᵢ - ŷᵢ|        Mean Absolute Error
                       i=1
```

| Metrik | Satuan | Sensitivitas terhadap Outlier | Interpretasi |
|--------|--------|-------------------------------|-------------|
| **MSE** | Satuan² | Sangat sensitif (kuadrat error) | Rata-rata kuadrat selisih prediksi |
| **RMSE** | Satuan asli | Sensitif | Rata-rata error dalam satuan asli |
| **MAE** | Satuan asli | Kurang sensitif (absolut) | Rata-rata deviasi absolut prediksi |
| **R²** | Tidak bersatuan | - | Proporsi variasi yang terjelaskan |
| **Adj. R²** | Tidak bersatuan | - | R² dengan penalti jumlah prediktor |

**Aturan praktis:**
- RMSE dan MAE dalam satuan yang sama dengan variabel dependen, sehingga mudah diinterpretasi
- Jika RMSE >> MAE, ada indikasi outlier besar dalam prediksi
- Semakin kecil RMSE/MAE, semakin baik model

### 9.6.2 Menghitung Metrik dengan Python

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

# Menggunakan model dari bagian sebelumnya
y_actual = rumah['harga_juta']
y_pred = model1.predict(X1)

mse = mean_squared_error(y_actual, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_actual, y_pred)
r2 = r2_score(y_actual, y_pred)

print("=== Metrik Evaluasi Model ===")
print(f"MSE  : {mse:,.2f} (juta Rp)²")
print(f"RMSE : {rmse:,.2f} juta Rp")
print(f"MAE  : {mae:,.2f} juta Rp")
print(f"R²   : {r2:.4f}")
print(f"\nInterpretasi:")
print(f"  Rata-rata, prediksi harga meleset sekitar Rp {rmse:.0f} juta (RMSE)")
print(f"  atau sekitar Rp {mae:.0f} juta (MAE)")
```

### 9.6.3 Cross-Validation: Pengantar

Ketika kita mengevaluasi model pada data yang **sama** dengan data yang digunakan untuk membangun model, hasilnya cenderung terlalu optimis. **Cross-validation** mengatasi ini dengan membagi data menjadi beberapa bagian (*fold*):

```
5-FOLD CROSS-VALIDATION
────────────────────────

Fold 1: [TEST] [Train] [Train] [Train] [Train]  → RMSE₁
Fold 2: [Train] [TEST] [Train] [Train] [Train]  → RMSE₂
Fold 3: [Train] [Train] [TEST] [Train] [Train]  → RMSE₃
Fold 4: [Train] [Train] [Train] [TEST] [Train]  → RMSE₄
Fold 5: [Train] [Train] [Train] [Train] [TEST]  → RMSE₅

Rata-rata RMSE = (RMSE₁ + RMSE₂ + RMSE₃ + RMSE₄ + RMSE₅) / 5
```

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

X = rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']]
y = rumah['harga_juta']

model_cv = LinearRegression()

# 5-fold cross-validation (skor negatif MSE — sklearn convention)
cv_scores = cross_val_score(model_cv, X, y, cv=5, scoring='neg_mean_squared_error')
cv_rmse = np.sqrt(-cv_scores)

print("=== 5-Fold Cross-Validation ===")
for i, rmse_val in enumerate(cv_rmse, 1):
    print(f"  Fold {i}: RMSE = {rmse_val:.2f} juta Rp")
print(f"\nRata-rata RMSE : {cv_rmse.mean():.2f} juta Rp")
print(f"Std RMSE       : {cv_rmse.std():.2f} juta Rp")
print(f"\nJika std kecil → model konsisten di berbagai partisi data")
```

---

## 9.7 Diagnostik Residual

### 9.7.1 Mengapa Diagnostik Penting?

Model regresi dibangun di atas **asumsi-asumsi** tertentu. Jika asumsi dilanggar, koefisien, p-value, dan confidence interval bisa tidak valid. Diagnostik residual adalah cara kita **memeriksa kesehatan** model.

```
ASUMSI MODEL REGRESI LINEAR
─────────────────────────────
┌─────────────────────┬──────────────────────────────────────┐
│ Asumsi              │ Cara Pemeriksaan                     │
├─────────────────────┼──────────────────────────────────────┤
│ 1. Linearitas       │ Residual vs Fitted plot              │
│ 2. Normalitas       │ Q-Q Plot, Shapiro-Wilk test          │
│ 3. Homoscedasticity │ Scale-Location plot                  │
│ 4. Independence     │ Durbin-Watson test                   │
│ 5. No multicollin.  │ VIF (dibahas di Bagian 9.4)          │
└─────────────────────┴──────────────────────────────────────┘
```

### 9.7.2 Asumsi 1: Linearitas

Hubungan antara prediktor dan variabel dependen harus **linear** (setelah dikontrol variabel lain).

**Cara cek:** Plot residual vs fitted values. Titik-titik harus tersebar **acak** di sekitar garis nol — tidak boleh membentuk pola (kurva, U, dsb).

```
BAIK (acak):                BURUK (pola kurva):
    •  •                        •     •
  •    •   •                •          •
──────•──────── 0            •           •
    •   •                  ──────────────── 0
  •     •  •                 •           •
      •                       •     •
```

### 9.7.3 Asumsi 2: Normalitas Residual

Residual harus berdistribusi **normal** (mendekati kurva lonceng).

**Cara cek visual:** Q-Q Plot (*Quantile-Quantile Plot*) — titik-titik harus mengikuti garis diagonal.

```
Q-Q PLOT NORMAL:              Q-Q PLOT TIDAK NORMAL:
  │        •••/               │          ••
  │      ••/                  │        ••
  │    ••/                    │     ••
  │   •/                      │  •••
  │ •/                        │••
  │/•                         │•
  └─────────                  └─────────
  Titik mengikuti garis       Titik menyimpang di ujung
  → residual normal           → residual tidak normal (heavy-tailed)
```

**Cara cek formal:** Shapiro-Wilk test
- H₀: Residual berdistribusi normal
- Jika p-value > 0.05, normalitas terpenuhi

### 9.7.4 Asumsi 3: Homoscedasticity

Variansi residual harus **konstan** untuk semua nilai prediksi (fitted values).

```
HOMOSCEDASTICITY (BAIK):           HETEROSCEDASTICITY (BURUK):
  │  •  •   •   •   •             │         •
  │ •  •  •  •  •  •              │       •   •
  ──────────────────── 0           │     •  •  •
  │ •  •  •  •  •  •              ──•──•──────────── 0
  │  •  •   •   •   •             │  •
  └─────────────────              │•
  Lebar tetap sepanjang X         Lebar membesar (bentuk corong/funnel)
```

**Jika dilanggar:** Gunakan *robust standard errors* (metode White/HC) atau transformasi variabel dependen (misalnya log).

### 9.7.5 Asumsi 4: Independence

Residual harus **independen** satu sama lain — tidak ada pola serial. Asumsi ini terutama penting pada data **time series** atau data yang dikumpulkan secara berurutan.

**Cara cek:** Durbin-Watson test (nilai ideal mendekati 2; nilai mendekati 0 menunjukkan autokorelasi positif, mendekati 4 menunjukkan autokorelasi negatif).

### 9.7.6 Implementasi Diagnostik Lengkap dengan Python

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

# Menggunakan model_sm (statsmodels OLS) dari bagian sebelumnya
X_sm = sm.add_constant(rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']])
y = rumah['harga_juta']
model_sm = sm.OLS(y, X_sm).fit()

# Hitung residual dan fitted values
y_pred = model_sm.predict(X_sm)
residuals = model_sm.resid

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Residual vs Fitted (linearitas + homoscedasticity)
axes[0, 0].scatter(y_pred, residuals, alpha=0.6, color='steelblue', edgecolor='white')
axes[0, 0].axhline(y=0, color='red', linestyle='--', linewidth=1.5)
axes[0, 0].set_xlabel('Fitted Values (y-hat)')
axes[0, 0].set_ylabel('Residuals')
axes[0, 0].set_title('1. Residual vs Fitted\n(Cek Linearitas & Homoscedasticity)')
axes[0, 0].grid(True, alpha=0.3)

# 2. Q-Q Plot (normalitas)
stats.probplot(residuals, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('2. Q-Q Plot\n(Cek Normalitas Residual)')
axes[0, 1].grid(True, alpha=0.3)

# 3. Histogram residual
axes[1, 0].hist(residuals, bins=20, color='steelblue', edgecolor='white', density=True)
x_norm = np.linspace(residuals.min(), residuals.max(), 100)
axes[1, 0].plot(x_norm, stats.norm.pdf(x_norm, residuals.mean(), residuals.std()),
                'r-', linewidth=2, label='Kurva Normal')
axes[1, 0].set_xlabel('Residuals')
axes[1, 0].set_ylabel('Density')
axes[1, 0].set_title('3. Histogram Residual\n(Cek Normalitas)')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# 4. Scale-Location (homoscedasticity)
axes[1, 1].scatter(y_pred, np.sqrt(np.abs(residuals)),
                   alpha=0.6, color='coral', edgecolor='white')
axes[1, 1].set_xlabel('Fitted Values (y-hat)')
axes[1, 1].set_ylabel('Akar |Residual|')
axes[1, 1].set_title('4. Scale-Location Plot\n(Cek Homoscedasticity)')
axes[1, 1].grid(True, alpha=0.3)

plt.suptitle('Diagnostik Residual Model Regresi Berganda', fontsize=14, y=1.01)
plt.tight_layout()
plt.show()

# Uji formal
stat_sw, p_sw = stats.shapiro(residuals)
print(f"=== Uji Formal ===")
print(f"Shapiro-Wilk Test : W = {stat_sw:.4f}, p-value = {p_sw:.4f}")
print(f"  Normalitas {'terpenuhi' if p_sw > 0.05 else 'TIDAK terpenuhi'} (alpha = 0.05)")

from statsmodels.stats.stattools import durbin_watson
dw = durbin_watson(residuals)
print(f"\nDurbin-Watson     : {dw:.4f}")
print(f"  Independence {'terpenuhi (mendekati 2)' if 1.5 < dw < 2.5 else 'PERLU INVESTIGASI'}")
```

---

## 9.8 Implementasi Python: sklearn vs statsmodels

### 9.8.1 Kapan Menggunakan Masing-masing?

```
┌─────────────────────────────────────────────────────────────────┐
│             SKLEARN vs STATSMODELS                              │
│                                                                 │
│  sklearn (scikit-learn):                                        │
│  + Mudah dan cepat untuk prediksi                               │
│  + Terintegrasi dengan pipeline ML                              │
│  + Cross-validation, train-test split                           │
│  - Tidak ada p-value, confidence interval                       │
│  - Tidak ada uji signifikansi variabel                          │
│                                                                 │
│  statsmodels:                                                   │
│  + Output statistik lengkap (p-value, CI, F-test)               │
│  + Cocok untuk inferensi dan interpretasi                       │
│  + Diagnostik model (Durbin-Watson, Omnibus, dll.)              │
│  - Kurang praktis untuk pipeline ML besar                       │
│                                                                 │
│  Rekomendasi:                                                   │
│  → Untuk ANALISIS dan INTERPRETASI → statsmodels                │
│  → Untuk PREDIKSI dan DEPLOYMENT  → sklearn                    │
│  → Untuk tugas kuliah ini         → gunakan KEDUANYA            │
└─────────────────────────────────────────────────────────────────┘
```

### 9.8.2 Workflow Lengkap dengan sklearn

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Dataset
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

# Pisahkan fitur dan target
X = rumah[['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun']]
y = rumah['harga_juta']

# Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                      random_state=42)
print(f"Data training: {len(X_train)} sampel")
print(f"Data testing : {len(X_test)} sampel")

# Bangun model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluasi pada data TESTING (bukan training!)
y_pred_test = model.predict(X_test)

print(f"\n=== Evaluasi pada Data Testing ===")
print(f"R²   : {r2_score(y_test, y_pred_test):.4f}")
print(f"RMSE : {np.sqrt(mean_squared_error(y_test, y_pred_test)):.2f} juta Rp")
print(f"MAE  : {mean_absolute_error(y_test, y_pred_test):.2f} juta Rp")

# Koefisien
print(f"\n=== Koefisien Model ===")
print(f"Intercept: {model.intercept_:.2f}")
for nama, koef in zip(X.columns, model.coef_):
    print(f"  {nama:20s}: {koef:.4f}")
```

### 9.8.3 Workflow Lengkap dengan statsmodels

```python
import statsmodels.api as sm

# Tambahkan konstanta (intercept) — statsmodels tidak menambahkan otomatis
X_train_sm = sm.add_constant(X_train)
X_test_sm = sm.add_constant(X_test)

# Fit model OLS
model_ols = sm.OLS(y_train, X_train_sm).fit()

# Tampilkan summary lengkap
print(model_ols.summary())

# ── Cara Membaca Output OLS Summary ──
# 1. R-squared / Adj. R-squared → seberapa baik model
# 2. F-statistic & Prob(F)      → model secara keseluruhan signifikan?
# 3. coef                       → besar pengaruh setiap variabel
# 4. P>|t| (p-value)            → variabel signifikan? (< 0.05)
# 5. [0.025, 0.975]             → 95% confidence interval koefisien

# Identifikasi variabel signifikan
print("\n=== Signifikansi Variabel (alpha = 0.05) ===")
for var in X.columns:
    p_val = model_ols.pvalues[var]
    status = "SIGNIFIKAN" if p_val < 0.05 else "tidak signifikan"
    print(f"  {var:20s}: p = {p_val:.4f} -> {status}")
```

---

## 9.9 Studi Kasus 1: Prediksi Harga Properti Indonesia

### 9.9.1 Konteks

Pasar properti Indonesia, khususnya di kota-kota besar seperti Jakarta, Bandung, dan Surabaya, dipengaruhi oleh berbagai faktor. Dalam studi kasus ini, kita akan membangun model regresi berganda untuk memprediksi harga rumah dan mengikuti seluruh alur analisis: EDA, pemodelan, diagnostik, dan evaluasi.

### 9.9.2 Langkah-langkah Analisis

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ============================================================
# STUDI KASUS: Prediksi Harga Rumah di Jabodetabek
# ============================================================

# --- Langkah 1: Persiapan Data ---
np.random.seed(2025)
n = 150

luas_bangunan = np.random.uniform(36, 250, n)
jumlah_kamar = np.random.choice([2, 3, 4, 5], n, p=[0.15, 0.40, 0.30, 0.15])
jarak_pusat = np.random.uniform(5, 50, n)
usia_bangunan = np.random.uniform(0, 35, n)
lebar_jalan = np.random.uniform(4, 12, n)  # meter

harga = (
    300
    + 9.0 * luas_bangunan
    + 55 * jumlah_kamar
    - 12 * jarak_pusat
    - 4.5 * usia_bangunan
    + 20 * lebar_jalan
    + np.random.normal(0, 120, n)
)

properti = pd.DataFrame({
    'luas_m2': luas_bangunan.round(1),
    'jumlah_kamar': jumlah_kamar,
    'jarak_pusat_km': jarak_pusat.round(1),
    'usia_tahun': usia_bangunan.round(1),
    'lebar_jalan_m': lebar_jalan.round(1),
    'harga_juta': harga.round(1)
})

print("=== Langkah 1: Preview Data ===")
print(properti.head(10))
print(f"\n{properti.describe().round(1)}")

# --- Langkah 2: Eksplorasi Data Awal (EDA) ---
print("\n=== Langkah 2: Korelasi dengan Harga ===")
for col in ['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun', 'lebar_jalan_m']:
    r, p = stats.pearsonr(properti[col], properti['harga_juta'])
    sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
    print(f"  {col:<20}: r = {r:+.3f} {sig}")

# Heatmap korelasi
plt.figure(figsize=(8, 6))
sns.heatmap(properti.corr(), annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Matriks Korelasi — Data Properti Jabodetabek')
plt.tight_layout()
plt.show()

# --- Langkah 3: Model Regresi Berganda ---
fitur = ['luas_m2', 'jumlah_kamar', 'jarak_pusat_km', 'usia_tahun', 'lebar_jalan_m']
X = properti[fitur]
y = properti['harga_juta']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# statsmodels untuk analisis
X_train_sm = sm.add_constant(X_train)
model_ols = sm.OLS(y_train, X_train_sm).fit()
print("\n=== Langkah 3: OLS Summary ===")
print(model_ols.summary())

# --- Langkah 4: Cek Multicollinearity ---
print("\n=== Langkah 4: VIF ===")
for i, col in enumerate(fitur):
    vif = variance_inflation_factor(X.values, i)
    status = "Aman" if vif < 5 else "PERHATIAN" if vif < 10 else "SERIUS"
    print(f"  {col:<20}: VIF = {vif:.2f} ({status})")

# --- Langkah 5: Diagnostik Residual ---
residuals = model_ols.resid
stat_sw, p_sw = stats.shapiro(residuals)
print(f"\n=== Langkah 5: Diagnostik ===")
print(f"Shapiro-Wilk: p = {p_sw:.4f} -> {'Normal' if p_sw > 0.05 else 'Tidak Normal'}")

# --- Langkah 6: Evaluasi pada Data Testing ---
X_test_sm = sm.add_constant(X_test)
y_pred_test = model_ols.predict(X_test_sm)

print(f"\n=== Langkah 6: Evaluasi (Data Testing) ===")
print(f"R²   : {r2_score(y_test, y_pred_test):.4f}")
print(f"RMSE : {np.sqrt(mean_squared_error(y_test, y_pred_test)):.2f} juta Rp")
print(f"MAE  : {mean_absolute_error(y_test, y_pred_test):.2f} juta Rp")

# --- Langkah 7: Prediksi Rumah Baru ---
print(f"\n=== Langkah 7: Prediksi ===")
rumah_baru = pd.DataFrame({
    'const': [1],
    'luas_m2': [100],
    'jumlah_kamar': [3],
    'jarak_pusat_km': [20],
    'usia_tahun': [5],
    'lebar_jalan_m': [8]
})
pred = model_ols.predict(rumah_baru)
pred_detail = model_ols.get_prediction(rumah_baru)
ci = pred_detail.summary_frame(alpha=0.05)
print(f"Rumah: 100 m2, 3 kamar, 20 km dari pusat, usia 5 tahun, jalan 8 m")
print(f"Prediksi: Rp {pred[0]:.0f} juta")
print(f"95% CI : Rp {ci['obs_ci_lower'].values[0]:.0f} - {ci['obs_ci_upper'].values[0]:.0f} juta")
```

---

## 9.10 Studi Kasus 2: Analisis Faktor Kelulusan Tepat Waktu

### 9.10.1 Konteks

Universitas ingin mengetahui faktor-faktor apa yang paling mempengaruhi IPK mahasiswa. Data yang dikumpulkan meliputi jam belajar per minggu, persentase kehadiran, jam tidur per hari, penghasilan orang tua, dan jarak ke kampus.

### 9.10.2 Implementasi

```python
# ============================================================
# STUDI KASUS 2: Faktor yang Mempengaruhi IPK Mahasiswa
# ============================================================

np.random.seed(2024)
n = 150

jam_belajar = np.random.uniform(5, 30, n)
kehadiran = np.random.uniform(50, 100, n)
jam_tidur = np.random.uniform(4, 9, n)
penghasilan_ortu = np.random.uniform(3, 25, n)
jarak_kampus = np.random.uniform(1, 40, n)

ipk = (
    1.5
    + 0.03 * jam_belajar
    + 0.012 * kehadiran
    + 0.08 * jam_tidur
    + 0.005 * penghasilan_ortu
    - 0.002 * jarak_kampus
    + np.random.normal(0, 0.15, n)
)
ipk = np.clip(ipk, 1.0, 4.0)

mhs = pd.DataFrame({
    'jam_belajar': np.round(jam_belajar, 1),
    'kehadiran_persen': np.round(kehadiran, 1),
    'jam_tidur': np.round(jam_tidur, 1),
    'penghasilan_ortu_juta': np.round(penghasilan_ortu, 1),
    'jarak_kampus_km': np.round(jarak_kampus, 1),
    'ipk': np.round(ipk, 2)
})

# Model lengkap
fitur_mhs = ['jam_belajar', 'kehadiran_persen', 'jam_tidur',
             'penghasilan_ortu_juta', 'jarak_kampus_km']
X_mhs = sm.add_constant(mhs[fitur_mhs])
model_ipk = sm.OLS(mhs['ipk'], X_mhs).fit()

print("=== Model Prediksi IPK Mahasiswa ===")
print(model_ipk.summary())

# Identifikasi faktor signifikan
print("\n=== Faktor Signifikan (alpha = 0.05) ===")
for var in fitur_mhs:
    p_val = model_ipk.pvalues[var]
    koef = model_ipk.params[var]
    status = "SIGNIFIKAN" if p_val < 0.05 else "tidak signifikan"
    print(f"  {var:<25}: koef = {koef:+.4f}, p = {p_val:.4f} -> {status}")

# Feature importance dengan koefisien terstandarisasi
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(mhs[fitur_mhs])
model_std = LinearRegression()
model_std.fit(X_scaled, mhs['ipk'])

importance = pd.DataFrame({
    'Variabel': fitur_mhs,
    'Koef_Std': model_std.coef_,
    'Abs_Koef': np.abs(model_std.coef_)
}).sort_values('Abs_Koef', ascending=True)

plt.figure(figsize=(10, 5))
colors = ['green' if x > 0 else 'red' for x in importance['Koef_Std']]
plt.barh(importance['Variabel'], importance['Koef_Std'], color=colors, alpha=0.7)
plt.xlabel('Koefisien Terstandarisasi')
plt.title('Faktor yang Mempengaruhi IPK\n(Hijau = positif, Merah = negatif)')
plt.axvline(x=0, color='black', linewidth=0.5)
plt.tight_layout()
plt.show()

print("\nInterpretasi:")
print("  Variabel dengan koefisien terstandarisasi terbesar (absolut)")
print("  memiliki pengaruh paling besar terhadap IPK mahasiswa.")
print("  Jam belajar, kehadiran, dan jam tidur diharapkan menjadi")
print("  faktor dominan — sesuai dengan intuisi pendidikan.")
```

---

## 9.11 AI Corner: Memanfaatkan AI untuk Pemodelan Regresi

### 9.11.1 Apa yang Bisa AI Bantu dalam Regresi Berganda?

| AI Bisa Membantu | AI Tidak Bisa Menggantikan |
|-------------------|---------------------------|
| Menulis kode regresi berganda | Menentukan variabel mana yang **seharusnya** masuk model (butuh domain knowledge) |
| Menjelaskan output OLS summary | Memutuskan apakah model layak digunakan untuk keputusan bisnis |
| Menyarankan cara mengatasi multicollinearity | Menjamin bahwa model kausal (bukan hanya korelasi) |
| Menginterpretasi Q-Q plot dan residual plot | Memahami konteks pasar properti atau pendidikan Indonesia |
| Men-debug kode Python | Memvalidasi apakah data simulasi realistis |

### 9.11.2 Contoh Prompt yang Efektif

**Prompt yang Baik:**

```
Saya membangun model regresi berganda untuk prediksi harga rumah
di Jakarta. Ini output statsmodels OLS summary saya:

[paste output summary]

Tolong bantu saya:
1. Variabel mana yang signifikan dan mana yang tidak?
2. Apakah Adjusted R² sudah cukup baik?
3. VIF variabel luas_m2 = 7.2 — apakah ini masalah?
4. Apa rekomendasi perbaikan model?
```

**Prompt yang Kurang Baik:**

```
Analisis regresi saya
```

### 9.11.3 Kapan Harus Kritis terhadap AI

- AI mungkin merekomendasikan menghapus variabel **hanya** berdasarkan p-value, tanpa mempertimbangkan teori atau konteks domain
- AI tidak selalu membedakan antara *statistical significance* dan *practical significance*
- Keputusan feature selection sebaiknya didasarkan pada **pemahaman domain + bukti statistik**, bukan salah satu saja
- AI mungkin memberikan interpretasi koefisien yang secara matematis benar tetapi **tidak masuk akal** dalam konteks dunia nyata

### 9.11.4 Latihan AI-Augmented

Coba prompt berikut ke ChatGPT/Claude, lalu evaluasi jawabannya secara kritis:

1. "Jelaskan perbedaan R² dan Adjusted R² dengan analogi kehidupan sehari-hari yang mudah dipahami mahasiswa Indonesia"
2. "Q-Q plot saya menunjukkan titik-titik menyimpang di kedua ujung. Apa artinya dan apa solusinya?"
3. "Saya punya 3 variabel dengan VIF > 10. Mana yang harus saya hapus?"

---

## Rangkuman Bab 9

1. **Regresi linear berganda** memperluas regresi sederhana dengan menggunakan banyak prediktor: ŷ = b₀ + b₁x₁ + b₂x₂ + ... + bₚxₚ. Ini memungkinkan model yang lebih realistis dan prediksi yang lebih akurat.

2. **Interpretasi koefisien** dalam regresi berganda harus selalu menyertakan frasa *"ceteris paribus"* (dengan variabel lain tetap). Koefisien bⱼ menunjukkan perubahan Y untuk setiap kenaikan 1 unit Xⱼ, **dengan semua variabel lain dikontrol konstan**.

3. **Adjusted R²** lebih tepat digunakan daripada R² untuk membandingkan model dengan jumlah prediktor berbeda, karena memberikan penalti untuk prediktor tambahan yang tidak berguna.

4. **Multicollinearity** terjadi ketika prediktor saling berkorelasi tinggi, menyebabkan koefisien tidak stabil. Gunakan **VIF** untuk mendeteksinya: VIF > 10 menandakan masalah serius yang perlu ditangani.

5. **Diagnostik residual** wajib dilakukan untuk memvalidasi model: periksa linearitas (residual vs fitted), normalitas (Q-Q plot, Shapiro-Wilk), homoscedasticity (scale-location plot), dan independence (Durbin-Watson).

6. **Metrik evaluasi** MSE, RMSE, dan MAE mengukur akurasi prediksi model. RMSE paling umum digunakan karena memiliki satuan yang sama dengan variabel dependen dan sensitif terhadap error besar.

7. **Cross-validation** memberikan estimasi performa model yang lebih jujur dibanding evaluasi pada data training, karena menguji model pada data yang belum pernah "dilihat" sebelumnya.

8. Gunakan **statsmodels** untuk analisis dan interpretasi (p-value, confidence interval), dan **sklearn** untuk prediksi dan deployment. Dalam praktik, keduanya saling melengkapi.

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
- c) Interpretasikan koefisien Jam_Belajar menggunakan prinsip *ceteris paribus*.
- d) Jika seorang mahasiswa belajar 20 jam/minggu, kehadiran 85%, dan jarak kampus 10 km, berapa prediksi IPK-nya?

**Soal 3.** Jelaskan mengapa R² selalu naik ketika kita menambahkan prediktor baru, bahkan jika prediktor tersebut tidak berguna. Mengapa Adjusted R² bisa turun dalam situasi yang sama?

**Soal 4.** Sebutkan empat asumsi utama model regresi linear dan jelaskan secara singkat cara memeriksa masing-masing asumsi tersebut.

**Soal 5.** Apa itu multicollinearity? Mengapa multicollinearity menjadi masalah dalam regresi berganda? Sebutkan tiga dampak negatifnya.

### Tingkat Menengah (C2-C3)

**Soal 6.** Perhatikan tabel VIF berikut untuk model prediksi harga rumah:

| Variabel | VIF |
|----------|-----|
| Luas bangunan | 8.5 |
| Luas tanah | 9.2 |
| Jumlah kamar | 3.1 |
| Jarak ke pusat kota | 1.8 |
| Usia bangunan | 1.5 |

- a) Variabel mana yang mengalami multicollinearity? Jelaskan.
- b) Mengapa luas bangunan dan luas tanah memiliki VIF tinggi?
- c) Apa rekomendasi Anda untuk mengatasi masalah ini? Berikan minimal dua solusi.
- d) Jika kita menghapus variabel "luas tanah", apa yang terjadi dengan VIF "luas bangunan"?

**Soal 7.** Tulis kode Python untuk:
- a) Membuat dataset simulasi dengan 100 observasi dan 3 variabel independen
- b) Membangun model regresi berganda menggunakan `sklearn`
- c) Menampilkan koefisien, R², dan RMSE
- d) Membandingkan R² training vs R² testing (gunakan `train_test_split` dengan `test_size=0.2`)

**Soal 8.** Jelaskan perbedaan antara forward selection dan backward elimination. Dalam situasi apa masing-masing metode lebih cocok digunakan?

**Soal 9.** Perhatikan dua model berikut:

| Model | Prediktor | R² | Adjusted R² | RMSE |
|-------|-----------|-----|-------------|------|
| A | Luas, Kamar | 0.72 | 0.71 | 145.3 |
| B | Luas, Kamar, Jarak, Usia, Jalan | 0.78 | 0.76 | 128.7 |
| C | Luas, Kamar, Jarak, Usia, Jalan, Noise1, Noise2 | 0.79 | 0.74 | 135.1 |

- a) Model mana yang paling baik? Jelaskan menggunakan Adjusted R² dan RMSE.
- b) Apa yang terjadi pada Model C? Mengapa R² naik tapi Adjusted R² turun?
- c) Apa bahaya menggunakan Model C untuk prediksi data baru?

**Soal 10.** Diberikan Q-Q plot berikut (deskripsi verbal):
- Pada bagian tengah, titik-titik mengikuti garis diagonal dengan baik.
- Pada ujung kiri dan kanan, titik-titik menyimpang ke atas dan ke bawah dari garis diagonal.

- a) Apa yang ditunjukkan oleh pola ini?
- b) Apa nama distribusi residual yang memiliki pola seperti ini?
- c) Apa tindakan yang bisa dilakukan jika n > 100? Bagaimana jika n < 30?

### Tingkat Mahir (C3-C5)

**Soal 11.** Sebuah perusahaan e-commerce Indonesia ingin memprediksi jumlah penjualan bulanan berdasarkan: budget iklan digital, jumlah produk aktif, rating toko, usia toko (bulan), dan jumlah follower media sosial.

- a) Tulis kode Python lengkap untuk: membuat data simulasi (n=200), membangun model regresi berganda, melakukan diagnostik residual lengkap (4 plot), dan menghitung VIF.
- b) Berdasarkan output model, lakukan backward elimination secara manual: identifikasi dan hapus variabel tidak signifikan satu per satu, fit ulang model, dan bandingkan Adjusted R² setiap tahap.
- c) Lakukan 5-fold cross-validation pada model terbaik dan laporkan rata-rata RMSE beserta standar deviasinya.

**Soal 12.** Evaluasi kritis terhadap model regresi:

Seorang mahasiswa membangun model regresi berganda untuk memprediksi gaji karyawan startup Indonesia berdasarkan: tahun pengalaman, level pendidikan (S1=1, S2=2, S3=3), jumlah sertifikasi, dan jumlah bahasa pemrograman yang dikuasai. Hasil yang diperoleh:
- R² = 0.92 pada data training
- R² = 0.45 pada data testing
- VIF semua variabel < 3
- Residual plot menunjukkan pola funnel (lebih lebar di sisi kanan)

- a) Apa yang ditunjukkan oleh perbedaan besar antara R² training dan testing?
- b) Apa masalah yang ditunjukkan oleh pola funnel pada residual plot?
- c) Apakah memperlakukan level pendidikan sebagai variabel numerik (1, 2, 3) sudah tepat? Apa alternatifnya?
- d) Apa rekomendasi perbaikan model secara keseluruhan? Berikan minimal tiga saran.

**Soal 13.** Tulis kode Python yang mengimplementasikan **backward elimination otomatis**:
- Mulai dari model dengan semua prediktor
- Pada setiap iterasi, hapus variabel dengan p-value tertinggi (jika > 0.05)
- Cetak Adjusted R² pada setiap langkah
- Berhenti ketika semua variabel signifikan
- Gunakan dataset IPK mahasiswa dari Studi Kasus 2

**Soal 14.** Bandingkan performa model regresi berganda pada dataset California Housing dari `sklearn.datasets`:
- a) Muat dataset dengan `fetch_california_housing()`
- b) Bangun model dengan semua 8 fitur dan evaluasi dengan 5-fold CV
- c) Bangun model hanya dengan 4 fitur terbaik (berdasarkan korelasi tertinggi dengan target) dan evaluasi dengan 5-fold CV
- d) Model mana yang lebih baik? Apakah mengurangi fitur selalu menurunkan performa?

**Soal 15.** Refleksi kritis:

Seorang data analyst menggunakan ChatGPT untuk membangun model regresi berganda prediksi harga properti di Bandung. AI merekomendasikan menghapus variabel "jarak ke kampus" karena p-value = 0.08 (tidak signifikan pada alpha = 0.05). Namun, secara domain knowledge, lokasi dekat kampus di Bandung (ITB, Unpad) mempengaruhi harga properti secara signifikan.

- a) Apakah rekomendasi AI sudah tepat? Jelaskan argumen pro dan kontra.
- b) Apa perbedaan antara *statistical significance* dan *practical significance* dalam konteks ini?
- c) Apa yang seharusnya dilakukan analyst? Gunakan prinsip "Human + AI Collaboration".
- d) Tuliskan AI Usage Log sesuai template mata kuliah ini untuk skenario di atas.

---

## Referensi

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability & Statistics for Engineers & Scientists* (9th ed.). Pearson.
2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning with Applications in Python (ISLP)*, Chapter 3: Linear Regression. Springer.
3. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics* (4th ed.), Chapter 9: Multiple and Logistic Regression.
4. Bruce, P., & Bruce, A. (2020). *Practical Statistics for Data Scientists* (2nd ed.), Chapter 4: Regression and Prediction. O'Reilly Media.
5. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
6. scikit-learn Documentation. *LinearRegression*. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
7. statsmodels Documentation. *OLS Regression*. https://www.statsmodels.org/stable/regression.html
8. statsmodels Documentation. *Variance Inflation Factor*. https://www.statsmodels.org/stable/generated/statsmodels.stats.outliers_influence.variance_inflation_factor.html
9. Kutner, M. H., Nachtsheim, C. J., Neter, J., & Li, W. (2005). *Applied Linear Statistical Models* (5th ed.). McGraw-Hill.

---

*Bab berikutnya: **Bab 10 — Analysis of Variance (ANOVA)***
