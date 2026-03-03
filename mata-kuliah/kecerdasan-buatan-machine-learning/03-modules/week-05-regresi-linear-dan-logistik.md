# Minggu 5: Regresi Linear dan Logistik

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 5 |
| **Topik** | Regresi Linear dan Logistik |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK-3: Menerapkan dan menganalisis algoritma supervised learning |
| **Sub-CPMK** | 5.1 Menerapkan regresi linear untuk prediksi variabel kontinu |
| | 5.2 Menganalisis regresi logistik untuk klasifikasi biner |
| **Bloom's Taxonomy** | C3–C4 (Menerapkan–Menganalisis / *Apply–Analyze*) |
| **Durasi** | 2 x 100 menit (Teori 100 min + Praktikum 100 min) |
| **Platform** | Google Colab |
| **Metode** | Ceramah interaktif, live coding, hands-on praktikum |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menerapkan** model regresi linear sederhana (*simple linear regression*) dengan memahami konsep garis terbaik (*best fit line*), cost function (MSE), dan *ordinary least squares*.
2. **Menjelaskan** regresi linear berganda (*multiple linear regression*) dengan representasi matriks dan memahami kontribusi setiap fitur.
3. **Menganalisis** proses *gradient descent* beserta pengaruh *learning rate* terhadap konvergensi model.
4. **Mengevaluasi** performa model regresi menggunakan metrik MSE, RMSE, MAE, dan R² score.
5. **Menerapkan** regresi logistik untuk klasifikasi biner dengan memahami fungsi sigmoid dan *decision boundary*.
6. **Menganalisis** hasil klasifikasi menggunakan *confusion matrix*, akurasi, presisi, recall, dan F1-score.
7. **Mengimplementasikan** `LinearRegression` dan `LogisticRegression` dari scikit-learn pada dataset nyata Indonesia.

---

## Materi Pembelajaran

### 1. Simple Linear Regression

#### Konsep Dasar

Regresi linear sederhana adalah teknik supervised learning yang memodelkan hubungan antara satu variabel independen (fitur) dan satu variabel dependen (target) dalam bentuk garis lurus:

$$y = mx + b$$

Di mana:
- **y** = variabel dependen (target/prediksi)
- **x** = variabel independen (fitur)
- **m** = *slope* (kemiringan garis)
- **b** = *intercept* (titik potong sumbu y)

#### Konteks Indonesia

Bayangkan kita ingin memprediksi **harga rumah di Jakarta Selatan** berdasarkan **luas bangunan**. Semakin besar luas bangunan, semakin tinggi harganya -- hubungan ini dapat dimodelkan dengan regresi linear.

#### Cost Function: Mean Squared Error (MSE)

Untuk menemukan garis terbaik, kita perlu mengukur seberapa jauh prediksi model dari nilai sebenarnya. Kita menggunakan **Mean Squared Error**:

```
MSE = (1/n) * Σ(yᵢ - ŷᵢ)²
```

Di mana `yᵢ` adalah nilai aktual dan `ŷᵢ` adalah nilai prediksi. Tujuan kita: **meminimalkan MSE**.

#### Ordinary Least Squares (OLS)

Metode OLS mencari nilai `m` dan `b` yang meminimalkan jumlah kuadrat residual. Secara analitis:

```
m = Σ((xᵢ - x̄)(yᵢ - ȳ)) / Σ((xᵢ - x̄)²)
b = ȳ - m * x̄
```

Metode ini memberikan solusi *closed-form* yang optimal untuk regresi linear.

---

### 2. Multiple Linear Regression

#### Dari Satu Fitur ke Banyak Fitur

Dalam praktiknya, harga rumah tidak hanya bergantung pada luas bangunan. Faktor lain seperti jumlah kamar tidur, jarak ke stasiun MRT, dan usia bangunan juga berpengaruh. Model regresi linear berganda:

```
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
```

#### Representasi Matriks

Dalam bentuk matriks, model dapat ditulis sebagai:

```
Y = Xβ + ε

Di mana:
Y = vektor target (n x 1)
X = matriks fitur (n x p)
β = vektor koefisien (p x 1)
ε = vektor error (n x 1)
```

Solusi OLS dalam bentuk matriks:

```
β = (XᵀX)⁻¹Xᵀy
```

#### Interpretasi Koefisien

Setiap koefisien βᵢ menunjukkan **perubahan pada y ketika xᵢ bertambah satu unit**, dengan asumsi fitur lain tetap (*ceteris paribus*). Contoh:
- β₁ = 15.000.000 untuk luas bangunan berarti setiap tambahan 1 m² meningkatkan harga Rp15 juta.
- β₂ = -500.000 untuk jarak ke MRT berarti setiap tambahan 1 km dari MRT menurunkan harga Rp500 ribu.

---

### 3. Gradient Descent

#### Intuisi

Bayangkan Anda berada di puncak bukit berkabut dan ingin turun ke titik terendah, tetapi tidak bisa melihat jauh. Strategi: **ambil langkah kecil ke arah yang paling curam ke bawah**. Inilah inti *gradient descent*.

```
Visualisasi Gradient Descent:

Cost (MSE)
  |
  | *
  |  \
  |   \
  |    *
  |     \
  |      \___*___*___*  <- Konvergen
  |________________________
        parameter (m, b)
```

#### Algoritma

1. Inisialisasi parameter `m` dan `b` secara acak
2. Hitung gradien (turunan parsial) dari cost function terhadap setiap parameter
3. Update parameter: `m = m - α * ∂MSE/∂m` dan `b = b - α * ∂MSE/∂b`
4. Ulangi langkah 2-3 hingga konvergen

#### Learning Rate (α)

*Learning rate* mengontrol ukuran langkah pada setiap iterasi:

```
Learning Rate terlalu kecil:    Learning Rate terlalu besar:
  |*                              |       *
  | *                             |  *        *
  |  *                            |      *
  |   *                           |   *     *
  |    *                          |         ← Divergen!
  |     *___*  (Lambat)           |
```

- **Terlalu kecil** (α = 0.0001): konvergensi sangat lambat
- **Terlalu besar** (α = 10): bisa divergen (melompat-lompat)
- **Tepat** (α = 0.01): konvergensi efisien ke minimum

---

### 4. Metrik Evaluasi Regresi

Setelah model dilatih, kita perlu mengukur performanya:

| Metrik | Rumus | Interpretasi |
|---|---|---|
| **MSE** | (1/n) Σ(yᵢ - ŷᵢ)² | Rata-rata kuadrat error; sensitif terhadap outlier |
| **RMSE** | √MSE | Akar dari MSE; satuan sama dengan target |
| **MAE** | (1/n) Σ\|yᵢ - ŷᵢ\| | Rata-rata absolute error; lebih robust terhadap outlier |
| **R² Score** | 1 - (SS_res / SS_tot) | Proporsi variansi yang dijelaskan model (0-1, makin tinggi makin baik) |

#### Kapan Menggunakan Metrik Apa?

- **MSE/RMSE**: ketika error besar harus dihukum lebih berat (misalnya prediksi harga properti -- error besar sangat merugikan)
- **MAE**: ketika semua error sama pentingnya dan ada potensi outlier
- **R²**: untuk membandingkan model secara umum; R² = 0.85 berarti model menjelaskan 85% variansi data

---

### 5. Logistic Regression: Klasifikasi Biner

#### Dari Regresi ke Klasifikasi

Regresi linear memprediksi nilai kontinu. Namun, bagaimana jika kita ingin memprediksi **kategori**? Misalnya: apakah pengajuan kredit **disetujui** atau **ditolak**?

#### Fungsi Sigmoid

Regresi logistik menggunakan **fungsi sigmoid** untuk mengubah output linear menjadi probabilitas (0 hingga 1):

```
σ(z) = 1 / (1 + e⁻ᶻ)

di mana z = β₀ + β₁x₁ + β₂x₂ + ...
```

```
Grafik Fungsi Sigmoid:
  1.0 |              ___________
      |           /
  0.5 |         /    <- Threshold (batas keputusan)
      |       /
  0.0 |______/
      +--------------------------
     -∞           0           +∞
                  z
```

#### Decision Boundary

Dengan *threshold* 0.5:
- Jika σ(z) ≥ 0.5 → kelas 1 (disetujui)
- Jika σ(z) < 0.5 → kelas 0 (ditolak)

#### Contoh Konteks Indonesia

Bank di Indonesia menggunakan model serupa untuk menentukan kelayakan kredit nasabah. Fitur yang dipertimbangkan:
- Pendapatan bulanan
- Riwayat kredit (skor BI Checking)
- Rasio utang terhadap pendapatan (*debt-to-income ratio*)
- Lama bekerja
- Status kepemilikan rumah

---

### 6. Evaluasi Klasifikasi

#### Confusion Matrix

```
                    Prediksi
                  Positif  Negatif
Aktual  Positif [  TP   |   FN   ]
        Negatif [  FP   |   TN   ]

TP = True Positive   (benar positif)
FP = False Positive  (salah positif / Type I Error)
FN = False Negative  (salah negatif / Type II Error)
TN = True Negative   (benar negatif)
```

#### Metrik Klasifikasi

| Metrik | Rumus | Interpretasi |
|---|---|---|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Proporsi prediksi benar secara keseluruhan |
| **Precision** | TP / (TP + FP) | Dari semua prediksi positif, berapa yang benar? |
| **Recall** | TP / (TP + FN) | Dari semua data positif, berapa yang terdeteksi? |
| **F1-Score** | 2 × (Precision × Recall) / (Precision + Recall) | Harmonic mean dari precision dan recall |

#### Kapan Precision vs Recall Lebih Penting?

- **Precision tinggi**: Ketika *false positive* mahal. Contoh: filter spam email -- kita tidak ingin email penting masuk ke spam.
- **Recall tinggi**: Ketika *false negative* berbahaya. Contoh: deteksi penyakit -- kita tidak ingin pasien sakit lolos tanpa terdeteksi.
- **F1-Score**: Ketika kita butuh keseimbangan antara keduanya.

---

### 7. Implementasi dengan scikit-learn

Scikit-learn menyediakan API yang konsisten untuk berbagai algoritma ML:

```python
from sklearn.linear_model import LinearRegression, LogisticRegression

# Regresi Linear
model_reg = LinearRegression()
model_reg.fit(X_train, y_train)
y_pred = model_reg.predict(X_test)

# Regresi Logistik
model_clf = LogisticRegression()
model_clf.fit(X_train, y_train)
y_pred = model_clf.predict(X_test)
```

Kedua model mengikuti pola yang sama: `fit()` untuk melatih, `predict()` untuk memprediksi. Perbedaannya ada pada tipe target:
- **LinearRegression**: target kontinu (harga, suhu, pendapatan)
- **LogisticRegression**: target kategorikal biner (ya/tidak, lulus/gagal)

---

## Aktivitas Kelas

### Sesi 1: Teori dan Diskusi (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Review & Pembukaan | Review materi minggu 4, pengantar regresi |
| 20 menit | Ceramah Interaktif | Simple & Multiple Linear Regression: konsep, OLS, MSE |
| 15 menit | Demonstrasi Visual | Gradient descent: simulasi interaktif, pengaruh learning rate |
| 15 menit | Ceramah Interaktif | Logistic Regression: sigmoid, decision boundary |
| 15 menit | Diskusi Kelompok | Studi kasus: kapan menggunakan regresi vs klasifikasi? Berikan contoh dari konteks Indonesia |
| 15 menit | Metrik Evaluasi | Penjelasan metrik regresi (MSE, R²) dan klasifikasi (confusion matrix, F1) |
| 10 menit | Tanya Jawab | Klarifikasi konsep sebelum masuk praktikum |

### Sesi 2: Praktikum Hands-on (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Setup & Data Loading | Buka Google Colab, import library, load dataset |
| 25 menit | Hands-on Regresi Linear | Prediksi harga rumah dengan LinearRegression |
| 20 menit | Hands-on Gradient Descent | Implementasi manual gradient descent, visualisasi konvergensi |
| 25 menit | Hands-on Regresi Logistik | Klasifikasi persetujuan kredit dengan LogisticRegression |
| 15 menit | Evaluasi & Interpretasi | Hitung metrik, analisis confusion matrix |
| 5 menit | Wrap-up & Preview | Rangkuman, pengenalan Decision Tree minggu depan |

---

## Hands-on: Prediksi Harga Rumah dan Klasifikasi Kredit

### Langkah 1: Import Library

```python
# Import library yang dibutuhkan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (mean_squared_error, mean_absolute_error,
                             r2_score, confusion_matrix, classification_report,
                             accuracy_score)
from sklearn.preprocessing import StandardScaler

print("Semua library berhasil di-import!")
```

### Langkah 2: Dataset Harga Rumah Indonesia (Regresi Linear)

```python
# Membuat dataset harga rumah di Jakarta (simulasi)
np.random.seed(42)
n = 200

luas_bangunan = np.random.uniform(30, 200, n)  # m²
jumlah_kamar = np.random.randint(1, 6, n)
jarak_mrt = np.random.uniform(0.5, 15, n)  # km
usia_bangunan = np.random.randint(0, 30, n)  # tahun

# Harga dalam jutaan rupiah (dengan sedikit noise)
harga = (15 * luas_bangunan
         + 50 * jumlah_kamar
         - 20 * jarak_mrt
         - 5 * usia_bangunan
         + 200
         + np.random.normal(0, 100, n))

df_rumah = pd.DataFrame({
    'luas_bangunan_m2': luas_bangunan,
    'jumlah_kamar': jumlah_kamar,
    'jarak_mrt_km': jarak_mrt,
    'usia_bangunan_tahun': usia_bangunan,
    'harga_juta_rp': harga
})

print("Dataset Harga Rumah Jakarta:")
print(df_rumah.head())
print(f"\nJumlah data: {len(df_rumah)}")
print(f"\nStatistik deskriptif:")
print(df_rumah.describe().round(2))
```

### Langkah 3: Simple Linear Regression

```python
# Simple Linear Regression: Harga vs Luas Bangunan
X_simple = df_rumah[['luas_bangunan_m2']]
y = df_rumah['harga_juta_rp']

# Split data
X_train_s, X_test_s, y_train, y_test = train_test_split(
    X_simple, y, test_size=0.2, random_state=42
)

# Latih model
model_simple = LinearRegression()
model_simple.fit(X_train_s, y_train)

# Koefisien
print(f"Slope (m): {model_simple.coef_[0]:.2f}")
print(f"Intercept (b): {model_simple.intercept_:.2f}")
print(f"\nInterpretasi: Setiap tambahan 1 m² luas bangunan,")
print(f"harga rumah naik sekitar Rp{model_simple.coef_[0]:.2f} juta")

# Visualisasi
plt.figure(figsize=(10, 6))
plt.scatter(X_test_s, y_test, alpha=0.6, label='Data Aktual')
plt.plot(X_test_s.sort_values('luas_bangunan_m2'),
         model_simple.predict(X_test_s.sort_values('luas_bangunan_m2')),
         color='red', linewidth=2, label='Garis Regresi')
plt.xlabel('Luas Bangunan (m²)')
plt.ylabel('Harga (Juta Rp)')
plt.title('Simple Linear Regression: Harga Rumah vs Luas Bangunan')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 4: Multiple Linear Regression

```python
# Multiple Linear Regression: semua fitur
X_multi = df_rumah[['luas_bangunan_m2', 'jumlah_kamar',
                     'jarak_mrt_km', 'usia_bangunan_tahun']]
y = df_rumah['harga_juta_rp']

X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
    X_multi, y, test_size=0.2, random_state=42
)

# Latih model
model_multi = LinearRegression()
model_multi.fit(X_train_m, y_train_m)
y_pred_m = model_multi.predict(X_test_m)

# Koefisien
print("=== Koefisien Multiple Linear Regression ===")
for nama, koef in zip(X_multi.columns, model_multi.coef_):
    print(f"  {nama}: {koef:.2f}")
print(f"  Intercept: {model_multi.intercept_:.2f}")

# Metrik evaluasi
mse = mean_squared_error(y_test_m, y_pred_m)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test_m, y_pred_m)
r2 = r2_score(y_test_m, y_pred_m)

print(f"\n=== Metrik Evaluasi ===")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f} juta Rp")
print(f"MAE  : {mae:.2f} juta Rp")
print(f"R²   : {r2:.4f}")
print(f"\nModel menjelaskan {r2*100:.1f}% variansi harga rumah.")

# Perbandingan simple vs multiple
y_pred_s = model_simple.predict(X_test_s)
r2_simple = r2_score(y_test, y_pred_s)
print(f"\n=== Perbandingan R² ===")
print(f"Simple LR  : {r2_simple:.4f}")
print(f"Multiple LR: {r2:.4f}")
print(f"Peningkatan: {(r2 - r2_simple)*100:.2f}%")
```

### Langkah 5: Gradient Descent Manual

```python
# Implementasi Gradient Descent sederhana untuk 1 fitur
def gradient_descent(X, y, learning_rate=0.01, n_iterations=100):
    """Gradient descent untuk simple linear regression."""
    m = 0  # slope awal
    b = 0  # intercept awal
    n = len(X)
    history = []

    for i in range(n_iterations):
        y_pred = m * X + b
        mse = np.mean((y - y_pred) ** 2)
        history.append(mse)

        # Hitung gradien
        dm = (-2/n) * np.sum(X * (y - y_pred))
        db = (-2/n) * np.sum(y - y_pred)

        # Update parameter
        m = m - learning_rate * dm
        b = b - learning_rate * db

    return m, b, history

# Normalisasi data untuk gradient descent
X_norm = (df_rumah['luas_bangunan_m2'].values - df_rumah['luas_bangunan_m2'].mean()) / df_rumah['luas_bangunan_m2'].std()
y_norm = (df_rumah['harga_juta_rp'].values - df_rumah['harga_juta_rp'].mean()) / df_rumah['harga_juta_rp'].std()

# Jalankan gradient descent
m_gd, b_gd, history = gradient_descent(X_norm, y_norm, learning_rate=0.01, n_iterations=200)

# Visualisasi konvergensi
plt.figure(figsize=(10, 5))
plt.plot(history, linewidth=2)
plt.xlabel('Iterasi')
plt.ylabel('MSE (Cost)')
plt.title('Konvergensi Gradient Descent')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"Parameter akhir: m = {m_gd:.4f}, b = {b_gd:.4f}")
print(f"MSE awal : {history[0]:.4f}")
print(f"MSE akhir: {history[-1]:.4f}")

# Perbandingan learning rate
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, lr in zip(axes, [0.001, 0.01, 0.1]):
    _, _, hist = gradient_descent(X_norm, y_norm, learning_rate=lr, n_iterations=200)
    ax.plot(hist, linewidth=2)
    ax.set_title(f'Learning Rate = {lr}')
    ax.set_xlabel('Iterasi')
    ax.set_ylabel('MSE')
    ax.grid(True, alpha=0.3)
plt.suptitle('Pengaruh Learning Rate pada Konvergensi', fontsize=14)
plt.tight_layout()
plt.show()
```

### Langkah 6: Logistic Regression -- Klasifikasi Kredit

```python
# Dataset persetujuan kredit (simulasi konteks Indonesia)
np.random.seed(42)
n = 300

pendapatan = np.random.uniform(3, 50, n)  # juta Rp/bulan
skor_bi_checking = np.random.randint(1, 6, n)  # 1=sangat baik, 5=sangat buruk
rasio_utang = np.random.uniform(0, 0.8, n)
lama_kerja = np.random.uniform(0, 25, n)  # tahun

# Probabilitas disetujui (logistic)
z = (0.1 * pendapatan - 0.8 * skor_bi_checking
     - 3 * rasio_utang + 0.1 * lama_kerja + 1)
prob = 1 / (1 + np.exp(-z))
disetujui = (prob > 0.5).astype(int)

df_kredit = pd.DataFrame({
    'pendapatan_juta': pendapatan.round(1),
    'skor_bi_checking': skor_bi_checking,
    'rasio_utang': rasio_utang.round(3),
    'lama_kerja_tahun': lama_kerja.round(1),
    'disetujui': disetujui
})

print("Dataset Persetujuan Kredit:")
print(df_kredit.head(10))
print(f"\nDistribusi target:")
print(df_kredit['disetujui'].value_counts())
print(f"Rasio persetujuan: {df_kredit['disetujui'].mean()*100:.1f}%")
```

### Langkah 7: Melatih dan Mengevaluasi Model Logistik

```python
# Persiapan data
X_kredit = df_kredit[['pendapatan_juta', 'skor_bi_checking',
                       'rasio_utang', 'lama_kerja_tahun']]
y_kredit = df_kredit['disetujui']

X_train_k, X_test_k, y_train_k, y_test_k = train_test_split(
    X_kredit, y_kredit, test_size=0.2, random_state=42, stratify=y_kredit
)

# Standardisasi fitur
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_k)
X_test_scaled = scaler.transform(X_test_k)

# Latih model logistic regression
model_logistic = LogisticRegression(random_state=42)
model_logistic.fit(X_train_scaled, y_train_k)

# Prediksi
y_pred_k = model_logistic.predict(X_test_scaled)

# Evaluasi
print("=== Classification Report ===")
print(classification_report(y_test_k, y_pred_k,
      target_names=['Ditolak', 'Disetujui']))

print(f"Akurasi: {accuracy_score(y_test_k, y_pred_k)*100:.1f}%")

# Koefisien (pentingnya fitur)
print("\n=== Koefisien Model ===")
for nama, koef in zip(X_kredit.columns, model_logistic.coef_[0]):
    arah = "meningkatkan" if koef > 0 else "menurunkan"
    print(f"  {nama}: {koef:.3f} ({arah} peluang disetujui)")
```

### Langkah 8: Visualisasi Confusion Matrix

```python
# Confusion Matrix
cm = confusion_matrix(y_test_k, y_pred_k)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Ditolak', 'Disetujui'],
            yticklabels=['Ditolak', 'Disetujui'])
plt.xlabel('Prediksi')
plt.ylabel('Aktual')
plt.title('Confusion Matrix - Persetujuan Kredit')
plt.tight_layout()
plt.show()

# Interpretasi
TP, FP, FN, TN = cm[1][1], cm[0][1], cm[1][0], cm[0][0]
print(f"True Positive  (benar disetujui) : {TP}")
print(f"True Negative  (benar ditolak)   : {TN}")
print(f"False Positive (salah disetujui) : {FP}")
print(f"False Negative (salah ditolak)   : {FN}")
print(f"\nPrecision: {TP/(TP+FP):.3f}")
print(f"Recall   : {TP/(TP+FN):.3f}")
print(f"F1-Score : {2*TP/(2*TP+FP+FN):.3f}")
```

### Langkah 9: Visualisasi Aktual vs Prediksi (Regresi)

```python
# Scatter plot aktual vs prediksi untuk regresi
plt.figure(figsize=(10, 6))
plt.scatter(y_test_m, y_pred_m, alpha=0.6, edgecolors='k', linewidth=0.5)
plt.plot([y_test_m.min(), y_test_m.max()],
         [y_test_m.min(), y_test_m.max()],
         'r--', linewidth=2, label='Prediksi Sempurna')
plt.xlabel('Harga Aktual (Juta Rp)')
plt.ylabel('Harga Prediksi (Juta Rp)')
plt.title(f'Aktual vs Prediksi - Multiple Linear Regression (R² = {r2:.4f})')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## AI Corner: Menggunakan AI untuk Menginterpretasi Hasil Regresi

> **Level: Intermediate** -- Anda sudah memahami dasar-dasar AI assistant dan sekarang belajar menggunakannya untuk interpretasi hasil analisis.

### Cara AI Bisa Membantu

| Skenario | Contoh Prompt ke AI |
|---|---|
| Interpretasi koefisien | *"Model regresi saya memiliki koefisien luas_bangunan = 15.2 dan jarak_mrt = -20.5. Jelaskan artinya dalam konteks harga rumah"* |
| Evaluasi metrik | *"Model saya punya R² = 0.85 dan RMSE = 150 juta Rp. Apakah ini bagus untuk prediksi harga rumah?"* |
| Diagnosis masalah | *"Confusion matrix saya menunjukkan recall rendah (0.6) tapi precision tinggi (0.9). Apa artinya dan bagaimana memperbaikinya?"* |
| Feature engineering | *"Fitur apa saja yang relevan untuk memprediksi harga rumah di Indonesia selain luas dan lokasi?"* |
| Debugging kode | *"Kode LogisticRegression saya error: [paste error]. Bagaimana memperbaikinya?"* |

### Tips Penting

1. **Selalu sertakan konteks** saat bertanya ke AI -- jelaskan dataset dan tujuan analisis Anda.
2. **Verifikasi saran AI** dengan menjalankan kode dan memeriksa hasilnya.
3. **Jangan hanya menerima angka** -- pastikan Anda memahami *mengapa* metrik menunjukkan nilai tertentu.
4. **Dokumentasikan** interaksi AI Anda dalam AI Usage Log.

### Contoh Prompt Minggu Ini

Coba masukkan prompt berikut ke ChatGPT atau Claude:

```
Saya membangun model regresi linear untuk prediksi harga rumah di Jakarta.
Hasilnya: R² = 0.85, RMSE = 120 juta Rp, MAE = 90 juta Rp.
Fitur yang digunakan: luas bangunan, jumlah kamar, jarak ke MRT, usia bangunan.

1. Apakah performa model ini cukup baik? Jelaskan.
2. Apa kelemahan potensial model regresi linear untuk kasus ini?
3. Sarankan 3 fitur tambahan yang mungkin meningkatkan performa.
```

Bandingkan jawaban AI dengan pemahaman Anda dari modul ini.

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai bahan refleksi:

1. **Regresi vs Klasifikasi:** Dalam konteks perbankan Indonesia, berikan masing-masing dua contoh permasalahan yang membutuhkan regresi linear dan regresi logistik. Jelaskan perbedaan target variabelnya.

2. **Interpretasi Koefisien:** Jika model regresi menunjukkan koefisien negatif untuk fitur "jarak ke pusat kota", apa makna praktisnya? Mengapa hal ini masuk akal?

3. **Overfitting vs Underfitting:** Jika R² pada data training = 0.99 tetapi R² pada data testing = 0.50, apa yang terjadi? Bagaimana mengatasinya?

4. **Etika AI dalam Kredit:** Bayangkan model kredit Anda memiliki bias -- menolak lebih banyak pengajuan dari kelompok tertentu. Bagaimana Anda menerapkan prinsip keadilan (*Al-'Adl*) dalam mengatasi masalah ini?

5. **Precision vs Recall:** Untuk deteksi penipuan transaksi bank, mana yang lebih penting: precision tinggi atau recall tinggi? Berikan argumentasi.

---

## Tugas Mandiri: T3 -- Regresi pada Data Riil Indonesia

### Deskripsi Tugas

Pilih **salah satu** skenario berikut dan bangun model regresi menggunakan data konteks Indonesia:

**Opsi A: Regresi Linear**
- Cari atau buat dataset harga properti, kendaraan bekas, atau komoditas di Indonesia.
- Bangun model regresi linear dengan minimal 3 fitur.
- Evaluasi dengan MSE, RMSE, MAE, dan R².
- Visualisasikan hasil dan interpretasikan koefisien.

**Opsi B: Regresi Logistik**
- Cari atau buat dataset klasifikasi biner konteks Indonesia (misal: kelulusan, persetujuan kredit, prediksi churn).
- Bangun model logistic regression.
- Buat confusion matrix dan hitung accuracy, precision, recall, F1-score.
- Interpretasikan hasil dalam konteks bisnis/sosial Indonesia.

### Kriteria Penilaian

| Komponen | Bobot |
|---|---|
| Relevansi dataset (konteks Indonesia) | 20% |
| Kebenaran implementasi model | 30% |
| Evaluasi dan interpretasi metrik | 25% |
| Visualisasi dan presentasi | 15% |
| AI Usage Log (jika menggunakan AI) | 10% |

### Format Pengumpulan

- File: Google Colab notebook (.ipynb)
- Deadline: Minggu 6
- Naming: `T3_NIM_NamaLengkap.ipynb`

---

## Referensi

### Buku Teks

1. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer.
2. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
3. Raschka, S., & Mirjalili, V. (2022). *Python Machine Learning* (4th ed.). Packt Publishing.

### Sumber Online

4. [scikit-learn: Linear Models](https://scikit-learn.org/stable/modules/linear_model.html) -- Dokumentasi resmi Linear & Logistic Regression.
5. [Google Machine Learning Crash Course: Linear Regression](https://developers.google.com/machine-learning/crash-course/linear-regression) -- Tutorial interaktif dari Google.
6. [Towards Data Science: Gradient Descent Explained](https://towardsdatascience.com/gradient-descent-explained-9b953fc0d2c) -- Visualisasi gradient descent.

### Referensi Konteks Indonesia

7. Otoritas Jasa Keuangan (OJK). Peraturan tentang Penilaian Kredit dan BI Checking.
8. Data Properti Indonesia -- [rumah123.com](https://www.rumah123.com/) dan [lamudi.co.id](https://www.lamudi.co.id/).

---

> **Preview Minggu Depan:** Kita akan membahas **Decision Tree dan Random Forest** -- algoritma yang memecah keputusan menjadi serangkaian aturan sederhana, serta teknik ensemble yang menggabungkan banyak model untuk prediksi yang lebih akurat.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
