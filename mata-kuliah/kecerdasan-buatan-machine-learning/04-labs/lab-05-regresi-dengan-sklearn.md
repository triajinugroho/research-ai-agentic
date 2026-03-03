# Lab 05: Regresi dengan scikit-learn

**Mata Kuliah:** Kecerdasan Buatan dan Machine Learning
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Minggu:** 5
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

- Membangun model Linear Regression dan mengevaluasi dengan MSE, RMSE, dan R-squared
- Memvisualisasikan garis regresi pada scatter plot
- Menerapkan Multiple Linear Regression dengan beberapa fitur
- Melakukan analisis residual untuk mengevaluasi asumsi model
- Membangun model Logistic Regression untuk klasifikasi biner
- Membuat confusion matrix dan classification report
- Membuat ROC curve dan menghitung AUC

---

## Persiapan

1. Buka Google Colab dan buat notebook baru
2. Nama file: `Lab05_NamaAnda_NIM.ipynb`
3. Pastikan library pandas, numpy, matplotlib, seaborn, dan scikit-learn sudah tersedia
4. Pahami konsep regresi linear dari kuliah teori

---

## Langkah-langkah

### Langkah 1: Linear Regression - Fit, Predict, Evaluate

```python
# =============================================
# LANGKAH 1: Linear Regression
# =============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler

# Pengaturan tampilan
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
np.random.seed(42)

print("=" * 60)
print("LINEAR REGRESSION - PREDIKSI HARGA RUMAH")
print("=" * 60)

# --- Buat Dataset Simulasi Harga Rumah di Indonesia ---
n = 400

luas_bangunan = np.random.uniform(30, 300, size=n)  # m2
noise = np.random.normal(0, 80, size=n)
harga_juta = 50 + 3.5 * luas_bangunan + noise  # Model sederhana

df = pd.DataFrame({
    'luas_bangunan_m2': luas_bangunan,
    'harga_juta': harga_juta
})

print(f"Dataset: {df.shape[0]} baris")
print(df.describe().round(2))

# --- Persiapan Data ---
X = df[['luas_bangunan_m2']].values
y = df['harga_juta'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTraining: {X_train.shape[0]} sampel")
print(f"Testing : {X_test.shape[0]} sampel")

# --- Fit Model ---
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)

print(f"\nKoefisien (slope)  : {model_lr.coef_[0]:.4f}")
print(f"Intercept (bias)   : {model_lr.intercept_:.4f}")
print(f"Persamaan: harga = {model_lr.intercept_:.2f} + {model_lr.coef_[0]:.2f} * luas_bangunan")

# --- Predict ---
y_pred_train = model_lr.predict(X_train)
y_pred_test = model_lr.predict(X_test)

# --- Evaluate ---
mse = mean_squared_error(y_test, y_pred_test)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred_test)
r2 = r2_score(y_test, y_pred_test)

print(f"\n--- Evaluasi Model ---")
print(f"MSE  (Mean Squared Error)    : {mse:.2f}")
print(f"RMSE (Root Mean Squared Error): {rmse:.2f}")
print(f"MAE  (Mean Absolute Error)   : {mae:.2f}")
print(f"R²   (Coefficient of Determ) : {r2:.4f}")
print(f"\nInterpretasi R²: Model menjelaskan {r2*100:.1f}% variasi harga")
```

### Langkah 2: Visualisasi Garis Regresi

```python
# =============================================
# LANGKAH 2: Visualisasi Garis Regresi
# =============================================

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# --- Plot 1: Scatter Plot dengan Garis Regresi ---
ax = axes[0]
ax.scatter(X_train, y_train, alpha=0.5, s=20, color='steelblue', label='Training data')
ax.scatter(X_test, y_test, alpha=0.5, s=20, color='coral', label='Testing data')

# Garis regresi
x_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_line = model_lr.predict(x_line)
ax.plot(x_line, y_line, 'r-', linewidth=2.5, label=f'Regresi (R²={r2:.3f})')

ax.set_xlabel('Luas Bangunan (m²)', fontsize=12)
ax.set_ylabel('Harga (Juta Rp)', fontsize=12)
ax.set_title('Linear Regression: Prediksi Harga Rumah', fontsize=13)
ax.legend(fontsize=10)

# --- Plot 2: Prediksi vs Aktual ---
ax = axes[1]
ax.scatter(y_test, y_pred_test, alpha=0.6, s=30, color='steelblue', edgecolors='white')
# Garis diagonal sempurna
min_val = min(y_test.min(), y_pred_test.min())
max_val = max(y_test.max(), y_pred_test.max())
ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Prediksi Sempurna')

ax.set_xlabel('Harga Aktual (Juta Rp)', fontsize=12)
ax.set_ylabel('Harga Prediksi (Juta Rp)', fontsize=12)
ax.set_title('Prediksi vs Aktual', fontsize=13)
ax.legend()

plt.tight_layout()
plt.show()
```

### Langkah 3: Multiple Linear Regression

```python
# =============================================
# LANGKAH 3: Multiple Linear Regression
# =============================================

print("=" * 60)
print("MULTIPLE LINEAR REGRESSION")
print("=" * 60)

# --- Buat Dataset dengan Multiple Features ---
np.random.seed(42)
n = 400

kota_list = ['Jakarta', 'Bandung', 'Surabaya', 'Yogyakarta', 'Semarang']
kota_premium = {'Jakarta': 2.5, 'Bandung': 1.0, 'Surabaya': 1.3, 'Yogyakarta': 0.8, 'Semarang': 0.9}

data_rumah = {
    'luas_bangunan_m2': np.random.uniform(30, 300, n),
    'jumlah_kamar': np.random.choice([1, 2, 3, 4, 5], n, p=[0.05, 0.20, 0.35, 0.25, 0.15]),
    'jarak_pusat_kota_km': np.random.uniform(1, 30, n),
    'tahun_dibangun': np.random.choice(range(1990, 2026), n),
    'kota': np.random.choice(kota_list, n),
}

df_multi = pd.DataFrame(data_rumah)
df_multi['usia_bangunan'] = 2026 - df_multi['tahun_dibangun']
df_multi['faktor_kota'] = df_multi['kota'].map(kota_premium)

# Harga = fungsi dari semua fitur
noise = np.random.normal(0, 100, n)
df_multi['harga_juta'] = (
    50 +
    3.0 * df_multi['luas_bangunan_m2'] +
    80 * df_multi['jumlah_kamar'] -
    15 * df_multi['jarak_pusat_kota_km'] -
    5 * df_multi['usia_bangunan'] +
    200 * df_multi['faktor_kota'] +
    noise
)

# Pilih fitur numerik
fitur_cols = ['luas_bangunan_m2', 'jumlah_kamar', 'jarak_pusat_kota_km', 'usia_bangunan', 'faktor_kota']
X_multi = df_multi[fitur_cols].values
y_multi = df_multi['harga_juta'].values

X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
    X_multi, y_multi, test_size=0.2, random_state=42
)

# --- Fit Model ---
model_multi = LinearRegression()
model_multi.fit(X_train_m, y_train_m)

y_pred_m = model_multi.predict(X_test_m)

# --- Evaluasi ---
r2_multi = r2_score(y_test_m, y_pred_m)
rmse_multi = np.sqrt(mean_squared_error(y_test_m, y_pred_m))

print(f"R² (Multiple)  : {r2_multi:.4f}")
print(f"RMSE (Multiple): {rmse_multi:.2f}")

# --- Koefisien Model ---
print(f"\n--- Koefisien Model ---")
for fitur, coef in zip(fitur_cols, model_multi.coef_):
    print(f"  {fitur:25s}: {coef:+.4f}")
print(f"  {'Intercept':25s}: {model_multi.intercept_:+.4f}")

# Perbandingan model sederhana vs multiple
print(f"\n--- Perbandingan ---")
print(f"Simple Linear Regression R² : {r2:.4f}")
print(f"Multiple Linear Regression R²: {r2_multi:.4f}")
print(f"Peningkatan: +{(r2_multi - r2)*100:.1f}%")
```

### Langkah 4: Analisis Residual

```python
# =============================================
# LANGKAH 4: Analisis Residual
# =============================================

print("=" * 60)
print("ANALISIS RESIDUAL")
print("=" * 60)

residuals = y_test_m - y_pred_m

print(f"Mean residual     : {residuals.mean():.4f} (harus mendekati 0)")
print(f"Std residual      : {residuals.std():.4f}")
print(f"Min residual      : {residuals.min():.4f}")
print(f"Max residual      : {residuals.max():.4f}")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Residual vs Predicted
ax = axes[0, 0]
ax.scatter(y_pred_m, residuals, alpha=0.5, s=20, color='steelblue')
ax.axhline(y=0, color='red', linestyle='--', linewidth=1.5)
ax.set_xlabel('Predicted Values', fontsize=11)
ax.set_ylabel('Residuals', fontsize=11)
ax.set_title('Residual vs Predicted', fontsize=13)

# Plot 2: Histogram Residual (uji normalitas)
ax = axes[0, 1]
ax.hist(residuals, bins=30, color='steelblue', edgecolor='white', alpha=0.7, density=True)
from scipy.stats import norm
x_norm = np.linspace(residuals.min(), residuals.max(), 100)
ax.plot(x_norm, norm.pdf(x_norm, residuals.mean(), residuals.std()), 'r-', linewidth=2)
ax.set_xlabel('Residuals', fontsize=11)
ax.set_ylabel('Density', fontsize=11)
ax.set_title('Distribusi Residual', fontsize=13)

# Plot 3: Q-Q Plot
ax = axes[1, 0]
from scipy import stats
stats.probplot(residuals, dist="norm", plot=ax)
ax.set_title('Q-Q Plot Residual', fontsize=13)

# Plot 4: Residual vs Setiap Fitur
ax = axes[1, 1]
ax.scatter(X_test_m[:, 0], residuals, alpha=0.5, s=20, color='coral')
ax.axhline(y=0, color='red', linestyle='--', linewidth=1.5)
ax.set_xlabel('Luas Bangunan (m²)', fontsize=11)
ax.set_ylabel('Residuals', fontsize=11)
ax.set_title('Residual vs Luas Bangunan', fontsize=13)

plt.suptitle('Analisis Residual - Multiple Regression', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.show()

print(f"""
Asumsi Linear Regression yang diperiksa:
1. Linearitas      : Residual vs Predicted → pola acak (OK jika tidak ada pola)
2. Normalitas      : Histogram & Q-Q Plot → residual mendekati distribusi normal
3. Homoskedastisitas: Residual vs Predicted → variance konstan (tidak menyebar/menyempit)
4. Independensi    : Tidak ada autokorelasi antar residual
""")
```

### Langkah 5: Logistic Regression - Klasifikasi Biner

```python
# =============================================
# LANGKAH 5: Logistic Regression
# =============================================

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print("=" * 60)
print("LOGISTIC REGRESSION - KLASIFIKASI KREDIT")
print("=" * 60)

# --- Dataset Simulasi Persetujuan Kredit ---
np.random.seed(42)
n = 600

pendapatan_juta = np.random.lognormal(mean=2.0, sigma=0.5, size=n)
usia = np.random.normal(35, 10, size=n).clip(21, 60).astype(int)
jumlah_tanggungan = np.random.choice([0, 1, 2, 3, 4, 5], n, p=[0.15, 0.20, 0.25, 0.20, 0.15, 0.05])
riwayat_kredit = np.random.choice([0, 1], n, p=[0.30, 0.70])  # 0=buruk, 1=baik

# Probabilitas disetujui
logit = (-3 + 0.15 * pendapatan_juta + 0.02 * usia - 0.3 * jumlah_tanggungan
         + 2.0 * riwayat_kredit + np.random.normal(0, 0.5, n))
prob = 1 / (1 + np.exp(-logit))
disetujui = (prob > 0.5).astype(int)

df_kredit = pd.DataFrame({
    'pendapatan_juta': np.round(pendapatan_juta, 2),
    'usia': usia,
    'jumlah_tanggungan': jumlah_tanggungan,
    'riwayat_kredit': riwayat_kredit,
    'disetujui': disetujui
})

print(f"Dataset Kredit: {df_kredit.shape}")
print(f"Distribusi target:\n{df_kredit['disetujui'].value_counts()}")

# --- Persiapan Data ---
fitur = ['pendapatan_juta', 'usia', 'jumlah_tanggungan', 'riwayat_kredit']
X_kredit = df_kredit[fitur].values
y_kredit = df_kredit['disetujui'].values

X_train_k, X_test_k, y_train_k, y_test_k = train_test_split(
    X_kredit, y_kredit, test_size=0.2, random_state=42, stratify=y_kredit
)

# Scaling
scaler = StandardScaler()
X_train_ks = scaler.fit_transform(X_train_k)
X_test_ks = scaler.transform(X_test_k)

# --- Fit Model ---
model_logistic = LogisticRegression(random_state=42, max_iter=1000)
model_logistic.fit(X_train_ks, y_train_k)

y_pred_k = model_logistic.predict(X_test_ks)
y_prob_k = model_logistic.predict_proba(X_test_ks)[:, 1]  # Probabilitas kelas 1

akurasi = accuracy_score(y_test_k, y_pred_k)
print(f"\nAkurasi: {akurasi:.4f} ({akurasi*100:.1f}%)")

# --- Koefisien ---
print(f"\n--- Koefisien Logistic Regression ---")
for fitur_name, coef in zip(fitur, model_logistic.coef_[0]):
    print(f"  {fitur_name:25s}: {coef:+.4f}")
print(f"  {'Intercept':25s}: {model_logistic.intercept_[0]:+.4f}")
```

### Langkah 6: Confusion Matrix dan Classification Report

```python
# =============================================
# LANGKAH 6: Confusion Matrix & Classification Report
# =============================================

from sklearn.metrics import ConfusionMatrixDisplay

print("=" * 60)
print("CONFUSION MATRIX & CLASSIFICATION REPORT")
print("=" * 60)

# --- Confusion Matrix ---
cm = confusion_matrix(y_test_k, y_pred_k)
print(f"\nConfusion Matrix:")
print(f"  [[TN={cm[0,0]:3d}  FP={cm[0,1]:3d}]")
print(f"   [FN={cm[1,0]:3d}  TP={cm[1,1]:3d}]]")

print(f"""
Interpretasi:
- True Negative (TN) = {cm[0,0]}: Ditolak, prediksi benar
- False Positive (FP) = {cm[0,1]}: Ditolak tapi diprediksi disetujui
- False Negative (FN) = {cm[1,0]}: Disetujui tapi diprediksi ditolak
- True Positive (TP) = {cm[1,1]}: Disetujui, prediksi benar
""")

# --- Classification Report ---
print("--- Classification Report ---")
print(classification_report(y_test_k, y_pred_k, target_names=['Ditolak', 'Disetujui']))

# --- Visualisasi Confusion Matrix ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Confusion matrix heatmap
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0],
            xticklabels=['Ditolak', 'Disetujui'],
            yticklabels=['Ditolak', 'Disetujui'])
axes[0].set_xlabel('Prediksi', fontsize=12)
axes[0].set_ylabel('Aktual', fontsize=12)
axes[0].set_title('Confusion Matrix', fontsize=13)

# Distribusi probabilitas prediksi
axes[1].hist(y_prob_k[y_test_k == 0], bins=20, alpha=0.7, color='coral', label='Ditolak (Aktual)', density=True)
axes[1].hist(y_prob_k[y_test_k == 1], bins=20, alpha=0.7, color='steelblue', label='Disetujui (Aktual)', density=True)
axes[1].axvline(x=0.5, color='red', linestyle='--', label='Threshold = 0.5')
axes[1].set_xlabel('Probabilitas Prediksi', fontsize=12)
axes[1].set_ylabel('Density', fontsize=12)
axes[1].set_title('Distribusi Probabilitas Prediksi', fontsize=13)
axes[1].legend()

plt.tight_layout()
plt.show()
```

### Langkah 7: ROC Curve dan AUC

```python
# =============================================
# LANGKAH 7: ROC Curve dan AUC
# =============================================

from sklearn.metrics import roc_curve, auc, roc_auc_score

print("=" * 60)
print("ROC CURVE DAN AUC")
print("=" * 60)

# --- Hitung ROC Curve ---
fpr, tpr, thresholds = roc_curve(y_test_k, y_prob_k)
roc_auc = auc(fpr, tpr)

print(f"AUC (Area Under Curve): {roc_auc:.4f}")
print(f"\nInterpretasi AUC:")
print(f"  0.5       = Model random (tidak berguna)")
print(f"  0.7-0.8   = Model cukup baik")
print(f"  0.8-0.9   = Model baik")
print(f"  0.9-1.0   = Model sangat baik")
print(f"  Model kita: {roc_auc:.4f} -> {'Sangat Baik' if roc_auc >= 0.9 else 'Baik' if roc_auc >= 0.8 else 'Cukup Baik' if roc_auc >= 0.7 else 'Perlu Perbaikan'}")

# --- Visualisasi ROC Curve ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ROC Curve
ax = axes[0]
ax.plot(fpr, tpr, 'b-', linewidth=2, label=f'Logistic Regression (AUC = {roc_auc:.3f})')
ax.plot([0, 1], [0, 1], 'r--', linewidth=1, label='Random Classifier (AUC = 0.500)')
ax.fill_between(fpr, tpr, alpha=0.2, color='blue')
ax.set_xlabel('False Positive Rate (FPR)', fontsize=12)
ax.set_ylabel('True Positive Rate (TPR)', fontsize=12)
ax.set_title('ROC Curve - Persetujuan Kredit', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Precision-Recall vs Threshold
ax = axes[1]
from sklearn.metrics import precision_recall_curve
precision, recall, thresholds_pr = precision_recall_curve(y_test_k, y_prob_k)

ax.plot(thresholds_pr, precision[:-1], 'b-', label='Precision', linewidth=2)
ax.plot(thresholds_pr, recall[:-1], 'r-', label='Recall', linewidth=2)
ax.axvline(x=0.5, color='gray', linestyle='--', alpha=0.5, label='Threshold = 0.5')
ax.set_xlabel('Threshold', fontsize=12)
ax.set_ylabel('Score', fontsize=12)
ax.set_title('Precision & Recall vs Threshold', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

plt.suptitle('Evaluasi Model Logistic Regression', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.show()

# --- Ringkasan ---
print(f"""
{'=' * 60}
RINGKASAN LAB REGRESI
{'=' * 60}

1. LINEAR REGRESSION (Prediksi Harga Rumah):
   - Simple LR  R² = {r2:.4f}
   - Multiple LR R² = {r2_multi:.4f}
   - Multiple regression lebih baik karena lebih banyak fitur

2. LOGISTIC REGRESSION (Persetujuan Kredit):
   - Akurasi = {akurasi:.4f}
   - AUC     = {roc_auc:.4f}
   - Riwayat kredit adalah prediktor paling kuat

Perbedaan utama:
- Linear Regression  → prediksi nilai kontinu (harga)
- Logistic Regression → prediksi kelas biner (ya/tidak)
""")
```

---

## Tantangan Tambahan

1. **Regularisasi:** Bandingkan performa `LinearRegression`, `Ridge`, dan `Lasso` pada dataset harga rumah. Variasikan parameter alpha dan plot perbandingan koefisien serta R-squared.

2. **Threshold Optimization:** Untuk model logistic regression persetujuan kredit, eksperimen dengan threshold selain 0.5. Buat plot precision, recall, dan F1-score vs threshold. Temukan threshold optimal untuk memaksimalkan F1-score.

3. **Feature Importance:** Buat visualisasi yang menunjukkan pentingnya setiap fitur pada model multiple linear regression dan logistic regression. Gunakan koefisien model (setelah normalisasi) sebagai ukuran importance.

---

## Checklist Penyelesaian

- [ ] Linear Regression berhasil dibangun dan dievaluasi (MSE, RMSE, R²)
- [ ] Garis regresi berhasil divisualisasikan pada scatter plot
- [ ] Multiple Linear Regression berhasil diterapkan
- [ ] Analisis residual berhasil dilakukan (4 plot diagnostik)
- [ ] Logistic Regression berhasil dibangun untuk klasifikasi biner
- [ ] Confusion matrix dan classification report berhasil dibuat
- [ ] ROC curve dan AUC berhasil divisualisasikan
- [ ] Notebook disimpan dengan nama `Lab05_NamaAnda_NIM.ipynb`
- [ ] Minimal 1 tantangan tambahan diselesaikan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
