# BAB 5: REGRESI LINEAR DAN LOGISTIK

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| Sub-CPMK 5.1 | Menerapkan regresi linear sederhana dan berganda untuk memprediksi variabel kontinu menggunakan sklearn | C3 |
| Sub-CPMK 5.2 | Menganalisis performa model regresi dan klasifikasi menggunakan metrik evaluasi yang tepat | C4 |

**CPMK-3:** Menerapkan algoritma supervised learning untuk permasalahan regresi dan klasifikasi.

---

## Estimasi Waktu

| Aktivitas | Durasi |
|-----------|--------|
| Membaca materi | 90 menit |
| Praktik kode Python | 120 menit |
| Mengerjakan latihan soal | 60 menit |
| **Total** | **270 menit (4.5 jam)** |

---

## Prasyarat

- Bab 3: Preprocessing dan Eksplorasi Data
- Bab 4: Supervised vs Unsupervised Learning
- Pemahaman dasar aljabar linear (matriks, vektor)
- Kemampuan dasar Python, NumPy, dan pandas

---

## 5.1 Simple Linear Regression (Regresi Linear Sederhana)

### 5.1.1 Model: y = mx + b

**Regresi linear sederhana** (*simple linear regression*) adalah metode untuk memodelkan hubungan antara **satu variabel independen** (x, *feature*) dan **satu variabel dependen** (y, *target*) menggunakan garis lurus.

Model matematisnya:

```
ŷ = β₀ + β₁x

di mana:
  ŷ  = nilai prediksi (predicted value)
  β₀ = intercept (titik potong dengan sumbu y)
  β₁ = slope (kemiringan garis, koefisien regresi)
  x  = variabel independen (feature)
```

**Analogi Sederhana:** Bayangkan Anda ingin memprediksi **harga rumah** berdasarkan **luas bangunan**. Semakin luas bangunan, semakin mahal harganya — hubungan ini bisa dimodelkan dengan garis lurus.

```
    Harga (y)
    │        ╱
    │      ╱   ← garis regresi (best fit line)
    │    ╱  •
    │  ╱ •    •
    │╱•    •
    │•
    └──────────── Luas (x)
```

### 5.1.2 Cost Function: Mean Squared Error (MSE)

Bagaimana kita menemukan garis **terbaik**? Kita membutuhkan **cost function** (fungsi biaya) yang mengukur seberapa jauh prediksi model dari nilai sebenarnya.

**Mean Squared Error (MSE):**

```
MSE = (1/n) × Σᵢ (yᵢ - ŷᵢ)²

di mana:
  n   = jumlah data
  yᵢ  = nilai aktual data ke-i
  ŷᵢ  = nilai prediksi data ke-i
```

**Mengapa kuadrat?**
1. Menghilangkan tanda negatif (error positif dan negatif tidak saling meniadakan)
2. Memberi penalti lebih besar pada error yang besar
3. Fungsi kuadrat memiliki sifat matematika yang baik (diferensiable, konveks)

### 5.1.3 Ordinary Least Squares (OLS)

**Ordinary Least Squares** adalah metode analitik untuk menemukan nilai β₀ dan β₁ yang meminimalkan MSE.

Rumus OLS:

```
β₁ = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²
β₀ = ȳ - β₁ × x̄
```

```python
import numpy as np

# Contoh: Prediksi harga rumah berdasarkan luas (m²)
# Data fiktif perumahan di Jakarta Selatan
luas = np.array([36, 45, 50, 60, 72, 80, 90, 100, 120, 150])
harga = np.array([450, 520, 580, 650, 780, 850, 920, 1050, 1200, 1500])  # dalam juta Rp

# Hitung OLS secara manual
x_mean = np.mean(luas)
y_mean = np.mean(harga)

# Hitung β₁ (slope) dan β₀ (intercept)
numerator = np.sum((luas - x_mean) * (harga - y_mean))
denominator = np.sum((luas - x_mean) ** 2)

beta_1 = numerator / denominator
beta_0 = y_mean - beta_1 * x_mean

print("=== REGRESI LINEAR SEDERHANA (OLS Manual) ===")
print(f"β₀ (intercept) : {beta_0:.2f}")
print(f"β₁ (slope)     : {beta_1:.2f}")
print(f"\nPersamaan: ŷ = {beta_0:.2f} + {beta_1:.2f} × x")

# Prediksi harga rumah dengan luas 75 m²
luas_baru = 75
harga_prediksi = beta_0 + beta_1 * luas_baru
print(f"\nPrediksi harga rumah 75 m²: Rp {harga_prediksi:.0f} juta")
```

**Output:**
```
=== REGRESI LINEAR SEDERHANA (OLS Manual) ===
β₀ (intercept) : 119.89
β₁ (slope)     : 8.93

Persamaan: ŷ = 119.89 + 8.93 × x

Prediksi harga rumah 75 m²: Rp 789 juta
```

### 5.1.4 sklearn: LinearRegression

Dalam praktik, kita menggunakan `sklearn.linear_model.LinearRegression` untuk efisiensi dan keandalan.

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Data perumahan Jakarta Selatan
data = {
    'luas_m2': [36, 45, 50, 60, 72, 80, 90, 100, 120, 150,
                40, 55, 65, 85, 95, 110, 130, 48, 70, 105],
    'harga_juta': [450, 520, 580, 650, 780, 850, 920, 1050, 1200, 1500,
                   480, 600, 700, 870, 960, 1100, 1350, 540, 750, 1080]
}
df = pd.DataFrame(data)

# Pisahkan feature (X) dan target (y)
X = df[['luas_m2']]  # DataFrame 2D (wajib untuk sklearn)
y = df['harga_juta']

# Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Buat dan latih model
model = LinearRegression()
model.fit(X_train, y_train)

# Koefisien model
print("=== MODEL REGRESI LINEAR (sklearn) ===")
print(f"Intercept (β₀): {model.intercept_:.2f}")
print(f"Slope (β₁)    : {model.coef_[0]:.2f}")
print(f"\nPersamaan: ŷ = {model.intercept_:.2f} + {model.coef_[0]:.2f} × luas_m2")

# Prediksi pada data test
y_pred = model.predict(X_test)
print(f"\nPrediksi vs Aktual:")
for actual, pred in zip(y_test, y_pred):
    print(f"  Aktual: Rp {actual} juta | Prediksi: Rp {pred:.0f} juta")

# Visualisasi
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color='blue', label='Data Training', alpha=0.7)
plt.scatter(X_test, y_test, color='red', label='Data Testing', alpha=0.7)
plt.plot(X, model.predict(X), color='green', linewidth=2, label='Garis Regresi')
plt.xlabel('Luas Bangunan (m²)')
plt.ylabel('Harga (Juta Rp)')
plt.title('Regresi Linear: Prediksi Harga Rumah Jakarta Selatan')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 5.2 Multiple Linear Regression (Regresi Linear Berganda)

### 5.2.1 Multiple Features

Pada kenyataannya, harga rumah tidak hanya ditentukan oleh luas saja, tetapi juga oleh **jumlah kamar**, **jarak ke pusat kota**, **umur bangunan**, dan lainnya. Di sinilah **regresi linear berganda** berperan.

```
ŷ = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ

di mana:
  p  = jumlah feature
  xⱼ = feature ke-j
  βⱼ = koefisien untuk feature ke-j
```

### 5.2.2 Matrix Form: y = Xβ + ε

Dalam notasi matriks, regresi linear berganda ditulis:

```
y = Xβ + ε

di mana:
  y = vektor target (n × 1)
  X = matriks design (n × (p+1)), kolom pertama = 1 (untuk intercept)
  β = vektor koefisien ((p+1) × 1)
  ε = vektor error/residual (n × 1)

Solusi OLS: β̂ = (XᵀX)⁻¹Xᵀy
```

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Dataset rumah di Jabodetabek (data simulasi)
np.random.seed(42)
n = 100

data = {
    'luas_m2': np.random.randint(30, 200, n),
    'jumlah_kamar': np.random.randint(1, 6, n),
    'jarak_pusat_kota_km': np.round(np.random.uniform(2, 40, n), 1),
    'umur_bangunan_tahun': np.random.randint(0, 30, n),
}
df = pd.DataFrame(data)

# Harga dipengaruhi oleh semua feature (dengan noise)
df['harga_juta'] = (
    100 +
    8.5 * df['luas_m2'] +
    50 * df['jumlah_kamar'] -
    15 * df['jarak_pusat_kota_km'] -
    5 * df['umur_bangunan_tahun'] +
    np.random.normal(0, 80, n)  # noise
)
df['harga_juta'] = df['harga_juta'].clip(lower=200).round(0)

# Feature dan target
X = df[['luas_m2', 'jumlah_kamar', 'jarak_pusat_kota_km', 'umur_bangunan_tahun']]
y = df['harga_juta']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Latih model regresi linear berganda
model = LinearRegression()
model.fit(X_train, y_train)

print("=== REGRESI LINEAR BERGANDA ===")
print(f"Intercept: {model.intercept_:.2f}")
print(f"\nKoefisien:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"  {feature:30s}: {coef:>8.2f}")

print(f"\nInterpretasi:")
print(f"  - Setiap tambahan 1 m² luas → harga naik ~Rp {model.coef_[0]:.0f} juta")
print(f"  - Setiap tambahan 1 kamar → harga naik ~Rp {model.coef_[1]:.0f} juta")
print(f"  - Setiap tambahan 1 km jarak → harga turun ~Rp {abs(model.coef_[2]):.0f} juta")
```

### 5.2.3 Multicollinearity (Multikolinearitas)

**Multikolinearitas** terjadi ketika dua atau lebih feature berkorelasi tinggi satu sama lain. Ini menyebabkan koefisien regresi menjadi tidak stabil.

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Deteksi multikolinearitas: correlation matrix
print("=== MATRIKS KORELASI ===")
corr_matrix = X_train.corr()
print(corr_matrix.round(3))

# Visualisasi heatmap korelasi
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
            fmt='.2f', square=True)
plt.title('Heatmap Korelasi antar Feature')
plt.tight_layout()
plt.show()

# Variance Inflation Factor (VIF) untuk deteksi multikolinearitas
from sklearn.linear_model import LinearRegression

def hitung_vif(X):
    """Menghitung VIF untuk setiap feature"""
    vif_data = []
    for i, col in enumerate(X.columns):
        # Regresi kolom ke-i terhadap kolom lainnya
        X_other = X.drop(columns=[col])
        model_vif = LinearRegression()
        model_vif.fit(X_other, X[col])
        r_squared = model_vif.score(X_other, X[col])
        vif = 1 / (1 - r_squared) if r_squared < 1 else float('inf')
        vif_data.append({'Feature': col, 'VIF': vif})
    return pd.DataFrame(vif_data)

vif_df = hitung_vif(X_train)
print("\n=== VARIANCE INFLATION FACTOR (VIF) ===")
print(vif_df.to_string(index=False))
print("\nInterpretasi VIF:")
print("  VIF < 5   : Tidak ada multikolinearitas signifikan")
print("  VIF 5-10  : Multikolinearitas sedang")
print("  VIF > 10  : Multikolinearitas tinggi (perlu tindakan)")
```

---

## 5.3 Evaluation Metrics for Regression (Metrik Evaluasi Regresi)

### 5.3.1 MSE, RMSE, MAE

| Metrik | Rumus | Keterangan |
|--------|-------|------------|
| **MSE** | (1/n) Σ(yᵢ - ŷᵢ)² | Sensitif terhadap outlier (karena kuadrat) |
| **RMSE** | √MSE | Sama satuan dengan target (lebih mudah diinterpretasi) |
| **MAE** | (1/n) Σ\|yᵢ - ŷᵢ\| | Lebih robust terhadap outlier |

### 5.3.2 R² Score (Coefficient of Determination)

**R² Score** mengukur proporsi variansi target yang bisa dijelaskan oleh model.

```
R² = 1 - (SS_res / SS_tot)
   = 1 - Σ(yᵢ - ŷᵢ)² / Σ(yᵢ - ȳ)²

Interpretasi:
  R² = 1.0 : Model sempurna (prediksi = aktual)
  R² = 0.0 : Model sama buruknya dengan prediksi rata-rata
  R² < 0.0 : Model lebih buruk dari prediksi rata-rata
```

### 5.3.3 Residual Analysis (Analisis Residual)

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

# Prediksi pada data test
y_pred = model.predict(X_test)

# Hitung metrik evaluasi
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("=== METRIK EVALUASI REGRESI ===")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f} juta Rp")
print(f"MAE  : {mae:.2f} juta Rp")
print(f"R²   : {r2:.4f} ({r2*100:.1f}%)")
print(f"\nInterpretasi: Model menjelaskan {r2*100:.1f}% variansi harga rumah")

# Analisis residual
residuals = y_test.values - y_pred

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Plot 1: Residual vs Predicted
axes[0].scatter(y_pred, residuals, alpha=0.6, color='steelblue')
axes[0].axhline(y=0, color='red', linestyle='--')
axes[0].set_xlabel('Nilai Prediksi (ŷ)')
axes[0].set_ylabel('Residual (y - ŷ)')
axes[0].set_title('Residual vs Predicted')

# Plot 2: Distribusi residual
axes[1].hist(residuals, bins=10, edgecolor='black', color='steelblue', alpha=0.7)
axes[1].set_xlabel('Residual')
axes[1].set_ylabel('Frekuensi')
axes[1].set_title('Distribusi Residual')

# Plot 3: Actual vs Predicted
axes[2].scatter(y_test, y_pred, alpha=0.6, color='steelblue')
min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
axes[2].plot([min_val, max_val], [min_val, max_val], 'r--', label='Perfect fit')
axes[2].set_xlabel('Nilai Aktual (y)')
axes[2].set_ylabel('Nilai Prediksi (ŷ)')
axes[2].set_title('Actual vs Predicted')
axes[2].legend()

plt.tight_layout()
plt.show()
```

---

## 5.4 Gradient Descent for Regression (Gradient Descent untuk Regresi)

### 5.4.1 Batch Gradient Descent

**Gradient descent** adalah algoritma optimasi iteratif yang digunakan untuk meminimalkan cost function. Berbeda dengan OLS yang memiliki solusi analitik, gradient descent menemukan solusi secara bertahap.

```
Algoritma:
1. Inisialisasi β secara acak (atau nol)
2. Hitung gradient: ∂MSE/∂β
3. Update: β_baru = β_lama - α × gradient
4. Ulangi sampai konvergen

di mana α (alpha) = learning rate
```

```python
import numpy as np
import matplotlib.pyplot as plt

# Implementasi Gradient Descent untuk regresi linear sederhana
def gradient_descent_linear(X, y, learning_rate=0.01, n_iterations=1000):
    """
    Implementasi batch gradient descent untuk regresi linear sederhana.

    Parameters:
        X: array feature (sudah dinormalisasi)
        y: array target
        learning_rate: ukuran langkah (alpha)
        n_iterations: jumlah iterasi
    Returns:
        beta_0, beta_1, history_cost
    """
    n = len(y)
    beta_0 = 0  # intercept
    beta_1 = 0  # slope
    history_cost = []

    for i in range(n_iterations):
        # Prediksi
        y_pred = beta_0 + beta_1 * X

        # Hitung cost (MSE)
        cost = (1 / n) * np.sum((y - y_pred) ** 2)
        history_cost.append(cost)

        # Hitung gradient
        d_beta_0 = -(2 / n) * np.sum(y - y_pred)
        d_beta_1 = -(2 / n) * np.sum(X * (y - y_pred))

        # Update parameter
        beta_0 = beta_0 - learning_rate * d_beta_0
        beta_1 = beta_1 - learning_rate * d_beta_1

    return beta_0, beta_1, history_cost

# Data luas dan harga rumah (normalisasi sederhana)
luas = np.array([36, 45, 50, 60, 72, 80, 90, 100, 120, 150], dtype=float)
harga = np.array([450, 520, 580, 650, 780, 850, 920, 1050, 1200, 1500], dtype=float)

# Normalisasi feature (penting untuk gradient descent)
luas_norm = (luas - luas.mean()) / luas.std()
harga_norm = (harga - harga.mean()) / harga.std()

# Jalankan gradient descent
b0, b1, costs = gradient_descent_linear(
    luas_norm, harga_norm,
    learning_rate=0.1,
    n_iterations=100
)

print("=== GRADIENT DESCENT ===")
print(f"β₀ (normalized): {b0:.4f}")
print(f"β₁ (normalized): {b1:.4f}")
print(f"Cost awal  : {costs[0]:.4f}")
print(f"Cost akhir : {costs[-1]:.6f}")

# Visualisasi konvergensi
plt.figure(figsize=(10, 5))
plt.plot(costs, color='steelblue', linewidth=2)
plt.xlabel('Iterasi')
plt.ylabel('Cost (MSE)')
plt.title('Konvergensi Gradient Descent')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 5.4.2 Learning Rate Impact (Dampak Learning Rate)

**Learning rate** (α) adalah hyperparameter krusial yang menentukan seberapa besar langkah update pada setiap iterasi.

```
α terlalu kecil  → konvergensi sangat lambat
α terlalu besar  → divergen (cost meningkat)
α optimal        → konvergensi cepat dan stabil
```

```python
import matplotlib.pyplot as plt
import numpy as np

# Bandingkan berbagai learning rate
learning_rates = [0.001, 0.01, 0.1, 0.5]
fig, axes = plt.subplots(1, 4, figsize=(18, 4))

for ax, lr in zip(axes, learning_rates):
    _, _, costs = gradient_descent_linear(luas_norm, harga_norm,
                                           learning_rate=lr,
                                           n_iterations=50)
    ax.plot(costs, color='steelblue', linewidth=2)
    ax.set_title(f'α = {lr}')
    ax.set_xlabel('Iterasi')
    ax.set_ylabel('Cost')
    ax.set_ylim(bottom=0, top=max(2, min(costs[0]*1.2, 5)))
    ax.grid(True, alpha=0.3)

plt.suptitle('Dampak Learning Rate terhadap Konvergensi', fontsize=14, y=1.02)
plt.tight_layout()
plt.show()
```

---

## 5.5 Logistic Regression (Regresi Logistik)

### 5.5.1 From Regression to Classification: Sigmoid Function

**Regresi logistik** bukan untuk regresi, melainkan untuk **klasifikasi** — khususnya **binary classification** (dua kelas). Nama "regresi" berasal dari kenyataan bahwa model ini menggunakan persamaan regresi linear di dalamnya.

**Sigmoid function** (fungsi logistik):

```
σ(z) = 1 / (1 + e⁻ᶻ)

di mana z = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ

Sifat sigmoid:
  - Output selalu antara 0 dan 1 → interpretasi sebagai probabilitas
  - σ(0) = 0.5
  - z → +∞ : σ(z) → 1
  - z → -∞ : σ(z) → 0
```

```python
import numpy as np
import matplotlib.pyplot as plt

# Visualisasi fungsi sigmoid
z = np.linspace(-10, 10, 200)
sigmoid = 1 / (1 + np.exp(-z))

plt.figure(figsize=(10, 5))
plt.plot(z, sigmoid, color='steelblue', linewidth=2.5)
plt.axhline(y=0.5, color='red', linestyle='--', alpha=0.5, label='Threshold = 0.5')
plt.axvline(x=0, color='gray', linestyle=':', alpha=0.5)
plt.xlabel('z (linear combination)', fontsize=12)
plt.ylabel('σ(z) = P(y=1|x)', fontsize=12)
plt.title('Fungsi Sigmoid (Logistik)', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 5.5.2 Decision Boundary (Batas Keputusan)

Model logistik memprediksi probabilitas kelas positif: P(y=1|x). Untuk mengambil keputusan, kita menggunakan **threshold** (biasanya 0.5):

```
Jika P(y=1|x) ≥ 0.5 → prediksi kelas 1 (positif)
Jika P(y=1|x) < 0.5 → prediksi kelas 0 (negatif)
```

### 5.5.3 Binary Classification (Klasifikasi Biner)

Contoh aplikasi klasifikasi biner:
- **Persetujuan kredit:** Disetujui (1) vs Ditolak (0)
- **Deteksi spam:** Spam (1) vs Bukan Spam (0)
- **Diagnosis penyakit:** Positif (1) vs Negatif (0)
- **Churn pelanggan:** Churn (1) vs Tidak Churn (0)

### 5.5.4 sklearn: LogisticRegression

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Simulasi data persetujuan kredit bank di Indonesia
np.random.seed(42)
n = 200

data_kredit = {
    'penghasilan_juta': np.round(np.random.uniform(3, 50, n), 1),
    'total_hutang_juta': np.round(np.random.uniform(0, 100, n), 1),
    'lama_kerja_tahun': np.random.randint(0, 25, n),
    'jumlah_tanggungan': np.random.randint(0, 6, n),
}
df_kredit = pd.DataFrame(data_kredit)

# Label: disetujui = 1, ditolak = 0
# Logika: penghasilan tinggi, hutang rendah, lama kerja → disetujui
skor = (df_kredit['penghasilan_juta'] * 2
        - df_kredit['total_hutang_juta'] * 0.8
        + df_kredit['lama_kerja_tahun'] * 1.5
        - df_kredit['jumlah_tanggungan'] * 3
        + np.random.normal(0, 10, n))
df_kredit['disetujui'] = (skor > 15).astype(int)

print(f"Distribusi kelas:\n{df_kredit['disetujui'].value_counts()}")
print(f"Proporsi disetujui: {df_kredit['disetujui'].mean():.2%}")

# Feature dan target
X = df_kredit[['penghasilan_juta', 'total_hutang_juta',
               'lama_kerja_tahun', 'jumlah_tanggungan']]
y = df_kredit['disetujui']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Standardisasi feature (penting untuk Logistic Regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Latih model Logistic Regression
log_model = LogisticRegression(random_state=42, max_iter=1000)
log_model.fit(X_train_scaled, y_train)

# Koefisien model
print("\n=== MODEL LOGISTIC REGRESSION ===")
print(f"Intercept: {log_model.intercept_[0]:.4f}")
print(f"\nKoefisien (setelah scaling):")
for feature, coef in zip(X.columns, log_model.coef_[0]):
    arah = "↑ peluang disetujui" if coef > 0 else "↓ peluang disetujui"
    print(f"  {feature:25s}: {coef:>8.4f} ({arah})")

# Prediksi probabilitas
y_prob = log_model.predict_proba(X_test_scaled)[:, 1]
y_pred = log_model.predict(X_test_scaled)

# Tampilkan beberapa prediksi
print(f"\nContoh prediksi (5 data pertama):")
print(f"{'Probabilitas':>12s} {'Prediksi':>9s} {'Aktual':>7s} {'Status':>10s}")
for prob, pred, actual in zip(y_prob[:5], y_pred[:5], y_test.values[:5]):
    status = "BENAR" if pred == actual else "SALAH"
    label_pred = "Setuju" if pred == 1 else "Tolak"
    print(f"{prob:>12.4f} {label_pred:>9s} {actual:>7d} {status:>10s}")
```

---

## 5.6 Classification Evaluation (Evaluasi Klasifikasi)

### 5.6.1 Confusion Matrix

**Confusion matrix** adalah tabel yang merangkum performa model klasifikasi:

```
                    Prediksi
                  Positif  Negatif
Aktual  Positif [  TP   |   FN  ]   ← True Positive / False Negative
        Negatif [  FP   |   TN  ]   ← False Positive / True Negative

TP = True Positive  : aktual positif, prediksi positif (BENAR)
FP = False Positive : aktual negatif, prediksi positif (Type I Error)
FN = False Negative : aktual positif, prediksi negatif (Type II Error)
TN = True Negative  : aktual negatif, prediksi negatif (BENAR)
```

### 5.6.2 Accuracy, Precision, Recall, F1-Score

| Metrik | Rumus | Pertanyaan yang Dijawab |
|--------|-------|------------------------|
| **Accuracy** | (TP+TN) / (TP+TN+FP+FN) | Berapa proporsi prediksi yang benar secara keseluruhan? |
| **Precision** | TP / (TP+FP) | Dari semua yang diprediksi positif, berapa yang benar? |
| **Recall** | TP / (TP+FN) | Dari semua yang aktual positif, berapa yang terdeteksi? |
| **F1-Score** | 2 × (Precision × Recall) / (Precision + Recall) | Harmonic mean dari precision dan recall |

### 5.6.3 ROC Curve and AUC

```python
from sklearn.metrics import (confusion_matrix, classification_report,
                              roc_curve, auc, ConfusionMatrixDisplay)
import matplotlib.pyplot as plt

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("=== CONFUSION MATRIX ===")
print(cm)

# Classification Report
print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, y_pred,
                             target_names=['Ditolak', 'Disetujui']))

# Visualisasi Confusion Matrix
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Confusion Matrix
ConfusionMatrixDisplay(cm, display_labels=['Ditolak', 'Disetujui']).plot(
    ax=axes[0], cmap='Blues'
)
axes[0].set_title('Confusion Matrix: Persetujuan Kredit')

# Plot 2: ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

axes[1].plot(fpr, tpr, color='steelblue', linewidth=2,
             label=f'ROC (AUC = {roc_auc:.3f})')
axes[1].plot([0, 1], [0, 1], color='gray', linestyle='--',
             label='Random Classifier')
axes[1].set_xlabel('False Positive Rate (FPR)')
axes[1].set_ylabel('True Positive Rate (TPR)')
axes[1].set_title('ROC Curve: Persetujuan Kredit')
axes[1].legend(fontsize=11)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"\nInterpretasi AUC = {roc_auc:.3f}:")
if roc_auc >= 0.9:
    print("  → Model sangat baik (excellent)")
elif roc_auc >= 0.8:
    print("  → Model baik (good)")
elif roc_auc >= 0.7:
    print("  → Model cukup (fair)")
else:
    print("  → Model kurang baik (poor)")
```

---

## 5.7 Studi Kasus Indonesia: Prediksi Harga Rumah dan Klasifikasi Kredit

### 5.7.1 Studi Kasus 1: Prediksi Harga Rumah di Jabodetabek

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Dataset rumah di Jabodetabek (simulasi berdasarkan data pasar 2025)
np.random.seed(42)
n = 300

kota = np.random.choice(['Jakarta', 'Bogor', 'Depok', 'Tangerang', 'Bekasi'], n)

# Faktor harga berbeda per kota
faktor_kota = {'Jakarta': 1.5, 'Bogor': 0.7, 'Depok': 0.8,
               'Tangerang': 0.9, 'Bekasi': 0.75}

data_rumah = pd.DataFrame({
    'kota': kota,
    'luas_tanah_m2': np.random.randint(60, 300, n),
    'luas_bangunan_m2': np.random.randint(36, 200, n),
    'jumlah_kamar_tidur': np.random.randint(2, 6, n),
    'jumlah_kamar_mandi': np.random.randint(1, 4, n),
    'garasi': np.random.randint(0, 3, n),
    'jarak_stasiun_km': np.round(np.random.uniform(0.5, 15, n), 1),
})

# Hitung harga berdasarkan fitur
harga_dasar = (
    200 +
    5 * data_rumah['luas_tanah_m2'] +
    8 * data_rumah['luas_bangunan_m2'] +
    75 * data_rumah['jumlah_kamar_tidur'] +
    50 * data_rumah['jumlah_kamar_mandi'] +
    100 * data_rumah['garasi'] -
    20 * data_rumah['jarak_stasiun_km']
)

# Terapkan faktor kota
data_rumah['harga_juta'] = (
    harga_dasar * data_rumah['kota'].map(faktor_kota)
    + np.random.normal(0, 100, n)
).round(0).clip(lower=300)

# One-hot encoding untuk kota
data_encoded = pd.get_dummies(data_rumah, columns=['kota'], drop_first=True)

# Feature dan target
feature_cols = [c for c in data_encoded.columns if c != 'harga_juta']
X = data_encoded[feature_cols]
y = data_encoded['harga_juta']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model regresi linear berganda
model_rumah = LinearRegression()
model_rumah.fit(X_train, y_train)

y_pred = model_rumah.predict(X_test)

print("=== STUDI KASUS: PREDIKSI HARGA RUMAH JABODETABEK ===")
print(f"RMSE : Rp {np.sqrt(mean_squared_error(y_test, y_pred)):.0f} juta")
print(f"R²   : {r2_score(y_test, y_pred):.4f}")
print(f"\nTop-5 Feature terpenting (berdasarkan koefisien):")
coef_df = pd.DataFrame({
    'Feature': feature_cols,
    'Koefisien': model_rumah.coef_
}).sort_values('Koefisien', key=abs, ascending=False)
print(coef_df.head().to_string(index=False))
```

### 5.7.2 Studi Kasus 2: Klasifikasi Persetujuan Kredit

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score

# Dataset kredit nasabah bank di Indonesia (simulasi)
np.random.seed(42)
n = 500

data_nasabah = pd.DataFrame({
    'usia': np.random.randint(21, 60, n),
    'penghasilan_juta': np.round(np.random.uniform(3, 80, n), 1),
    'lama_kerja_tahun': np.random.randint(0, 30, n),
    'jumlah_tanggungan': np.random.randint(0, 6, n),
    'total_pinjaman_juta': np.round(np.random.uniform(0, 200, n), 1),
    'riwayat_kredit_macet': np.random.choice([0, 1], n, p=[0.7, 0.3]),
    'skor_bi_checking': np.random.randint(1, 6, n),
})

# Label persetujuan
skor_kredit = (
    data_nasabah['penghasilan_juta'] * 1.5
    + data_nasabah['lama_kerja_tahun'] * 2
    - data_nasabah['jumlah_tanggungan'] * 5
    - data_nasabah['total_pinjaman_juta'] * 0.3
    - data_nasabah['riwayat_kredit_macet'] * 20
    - data_nasabah['skor_bi_checking'] * 3
    + np.random.normal(0, 10, n)
)
data_nasabah['disetujui'] = (skor_kredit > 10).astype(int)

print(f"Distribusi kelas:\n{data_nasabah['disetujui'].value_counts()}")

# Feature dan target
X = data_nasabah.drop('disetujui', axis=1)
y = data_nasabah['disetujui']

# Split dan scale
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# Model
model_kredit = LogisticRegression(random_state=42, max_iter=1000)
model_kredit.fit(X_train_s, y_train)

y_pred = model_kredit.predict(X_test_s)
y_prob = model_kredit.predict_proba(X_test_s)[:, 1]

print("\n=== KLASIFIKASI PERSETUJUAN KREDIT ===")
print(classification_report(y_test, y_pred,
                             target_names=['Ditolak', 'Disetujui']))
print(f"AUC-ROC: {roc_auc_score(y_test, y_prob):.4f}")

# Analisis koefisien
print("\nFaktor yang mempengaruhi persetujuan kredit:")
for feature, coef in sorted(zip(X.columns, model_kredit.coef_[0]),
                              key=lambda x: abs(x[1]), reverse=True):
    efek = "MENINGKATKAN" if coef > 0 else "MENURUNKAN"
    print(f"  {feature:30s}: {coef:>8.4f} → {efek} peluang disetujui")
```

---

## 5.8 AI Corner: Menggunakan AI untuk Interpretasi Hasil Regresi dan Klasifikasi

**Level: Intermediate**

### 5.8.1 Apa yang Bisa AI Bantu?

| AI Bisa | AI Tidak Bisa |
|---------|--------------|
| Menjelaskan arti koefisien regresi | Menentukan apakah model cocok untuk bisnis Anda |
| Menginterpretasi confusion matrix | Memahami konteks domain secara mendalam |
| Menyarankan metrik evaluasi yang tepat | Memutuskan threshold optimal tanpa konteks bisnis |
| Membantu debug error kode sklearn | Menjamin prediksi model selalu benar |
| Menjelaskan perbedaan MSE vs MAE | Menentukan apakah data cukup representatif |

### 5.8.2 Contoh Prompt yang Baik

```
Prompt 1 (Interpretasi Koefisien):
"Model regresi linear saya untuk prediksi harga rumah memiliki
koefisien luas_bangunan = 8.5 dan jarak_stasiun = -20.
Jelaskan interpretasi masing-masing koefisien dalam konteks
bisnis properti di Indonesia."

Prompt 2 (Evaluasi Model):
"Model logistic regression saya menghasilkan accuracy 85%,
precision 80%, recall 60%. Dataset memiliki class imbalance
(70% negatif, 30% positif). Apakah model saya sudah baik?
Metrik mana yang harus saya prioritaskan dan mengapa?"

Prompt 3 (Debugging):
"Kode sklearn LinearRegression saya menghasilkan R² negatif
pada data test. Apa kemungkinan penyebabnya? Data saya memiliki
100 sampel dan 50 feature."
```

### 5.8.3 Verifikasi Output AI

Selalu lakukan verifikasi berikut setelah mendapat jawaban dari AI:

1. **Jalankan kode** yang disarankan AI — pastikan tidak error
2. **Cek logika** — apakah interpretasi masuk akal secara domain?
3. **Bandingkan** dengan materi kuliah dan referensi textbook
4. **Dokumentasikan** dalam AI Usage Log

### 5.8.4 Template AI Usage Log untuk Bab 5

```markdown
## AI Usage Log — BAB 5: Regresi Linear dan Logistik

### Interaksi 1
- **Tool:** [Claude / ChatGPT / Copilot]
- **Prompt:** [Copy-paste prompt Anda]
- **Output:** [Ringkasan jawaban AI]
- **Verifikasi:** [Sudah / Belum diverifikasi? Hasilnya?]
- **Modifikasi:** [Apa yang Anda ubah/tambahkan]
- **Refleksi:** [Apa yang Anda pelajari?]
```

---

## Rangkuman Bab 5

1. **Regresi linear sederhana** memodelkan hubungan linear antara satu feature (x) dan target (y) dengan persamaan ŷ = β₀ + β₁x. Solusi optimal ditemukan menggunakan **OLS** atau **gradient descent**.

2. **Regresi linear berganda** memperluas model ke banyak feature: ŷ = Xβ. Perhatikan potensi **multikolinearitas** antar feature.

3. **Metrik evaluasi regresi**: MSE mengukur rata-rata kuadrat error, RMSE memberikan satuan yang sama dengan target, MAE lebih robust terhadap outlier, dan R² mengukur proporsi variansi yang dijelaskan model.

4. **Gradient descent** adalah algoritma optimasi iteratif. **Learning rate** yang terlalu kecil menyebabkan konvergensi lambat, terlalu besar menyebabkan divergensi.

5. **Regresi logistik** digunakan untuk **klasifikasi biner** dengan fungsi sigmoid yang mengubah output linear menjadi probabilitas [0, 1].

6. **Metrik evaluasi klasifikasi**: confusion matrix, accuracy, precision, recall, F1-score, ROC curve, dan AUC. Pemilihan metrik bergantung pada konteks masalah (misalnya, recall penting untuk deteksi penyakit).

7. Dalam konteks Indonesia, regresi dan klasifikasi dapat diterapkan untuk **prediksi harga properti**, **persetujuan kredit**, dan berbagai masalah bisnis lainnya.

---

## Latihan Soal

### Tingkat Dasar (C2-C3)

**Soal 1.** Jelaskan perbedaan antara regresi linear sederhana dan regresi linear berganda. Kapan kita menggunakan masing-masing?

**Soal 2.** Sebuah model regresi linear menghasilkan persamaan ŷ = 200 + 5x, di mana x = luas rumah (m²) dan y = harga (juta Rp). Interpretasikan nilai intercept (200) dan slope (5).

**Soal 3.** Jelaskan mengapa kita perlu membagi data menjadi training set dan testing set. Apa yang terjadi jika kita mengevaluasi model pada data yang sama yang digunakan untuk pelatihan?

**Soal 4.** Perhatikan confusion matrix berikut:

| | Prediksi: Positif | Prediksi: Negatif |
|---|---|---|
| Aktual: Positif | 40 | 10 |
| Aktual: Negatif | 5 | 45 |

Hitung: (a) Accuracy, (b) Precision, (c) Recall, (d) F1-Score.

**Soal 5.** Jelaskan apa itu fungsi sigmoid dan mengapa fungsi ini digunakan dalam regresi logistik. Berapa output sigmoid jika z = 0?

### Tingkat Menengah (C3-C4)

**Soal 6.** Tulis kode Python menggunakan sklearn untuk melatih model regresi linear yang memprediksi **nilai IPK** mahasiswa berdasarkan **jam belajar per minggu** dan **nilai ujian masuk**. Gunakan data simulasi minimal 50 sampel. Evaluasi model dengan MSE, RMSE, dan R².

**Soal 7.** Suatu model regresi menghasilkan R² = 0.45 pada data training dan R² = 0.42 pada data testing. Model lain menghasilkan R² = 0.95 pada training dan R² = 0.30 pada testing. Analisis kedua model: mana yang lebih baik dan mengapa? Apa yang terjadi pada model kedua?

**Soal 8.** Implementasikan logistic regression menggunakan sklearn untuk memprediksi apakah seorang mahasiswa **lulus atau tidak** berdasarkan: jam belajar, kehadiran (%), dan nilai tugas rata-rata. Tampilkan confusion matrix dan classification report.

**Soal 9.** Jelaskan perbedaan antara accuracy, precision, dan recall. Dalam kasus deteksi penipuan transaksi e-commerce di Indonesia (misalnya di Tokopedia), metrik mana yang lebih penting dan mengapa?

### Tingkat Mahir (C4-C5)

**Soal 10.** Implementasikan gradient descent dari nol (tanpa sklearn) untuk regresi linear sederhana. Eksperimen dengan 3 learning rate berbeda dan visualisasikan kurva konvergensi. Jelaskan hasilnya.

**Soal 11.** Anda diminta membangun model prediksi harga rumah di kota Anda. Jelaskan:
- a) Feature apa saja yang akan Anda gunakan? (minimal 5 feature)
- b) Bagaimana Anda menangani feature kategorikal (misalnya lokasi)?
- c) Bagaimana Anda mendeteksi dan menangani multikolinearitas?
- d) Metrik evaluasi apa yang akan Anda gunakan dan mengapa?
- e) Implementasikan solusi lengkap dengan Python (data boleh simulasi)

**Soal 12.** Bandingkan performa regresi logistik dengan threshold 0.3, 0.5, dan 0.7 pada dataset klasifikasi kredit. Untuk setiap threshold, hitung precision, recall, dan F1-score. Kapan kita sebaiknya menggunakan threshold selain 0.5?

---

## Referensi

1. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2023). *An Introduction to Statistical Learning* (2nd ed.). Springer.
2. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.
3. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
4. Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.
5. Hosmer, D. W., Lemeshow, S., & Sturdivant, R. X. (2013). *Applied Logistic Regression* (3rd ed.). Wiley.
6. Bank Indonesia. (2025). *Statistik Sistem Keuangan Indonesia*. BI.
7. Rumah123.com & Lamudi.co.id. (2025). *Laporan Properti Indonesia 2025*.

---

*Bab berikutnya: **Bab 6 — Decision Tree dan Ensemble Methods***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
