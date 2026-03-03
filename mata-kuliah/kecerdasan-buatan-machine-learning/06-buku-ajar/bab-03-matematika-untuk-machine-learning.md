# BAB 3: MATEMATIKA UNTUK MACHINE LEARNING

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-3.1 | Menerapkan konsep aljabar linear (vektor, matriks, eigenvalue) dalam konteks machine learning | C3 |
| CPMK-3.2 | Menerapkan konsep probabilitas dan kalkulus (Bayes' Theorem, gradient descent) untuk memahami cara kerja algoritma ML | C3 |

---

## Estimasi Waktu

| Aktivitas | Durasi |
|-----------|--------|
| Membaca materi | 120 menit |
| Praktik kode NumPy | 90 menit |
| Mengerjakan latihan soal | 60 menit |
| Eksplorasi AI Corner | 30 menit |
| **Total** | **5 jam** |

---

## Prasyarat

- Bab 1: Pengantar Kecerdasan Buatan
- Bab 2: Python untuk AI dan Machine Learning (terutama NumPy)
- Pemahaman dasar matematika SMA (aljabar, probabilitas dasar)

---

## 3.1 Aljabar Linear untuk Machine Learning

### 3.1.1 Vektor dan Operasi Vektor

**Vektor** adalah daftar bilangan yang terurut. Dalam ML, vektor merepresentasikan **fitur** suatu data point.

```
Contoh: Mahasiswa direpresentasikan sebagai vektor fitur
─────────────────────────────────────────────────────
mahasiswa = [IPK, jam_belajar, kehadiran, tugas_selesai]
         = [3.45,    4.0,        85,         10      ]

Setiap mahasiswa adalah satu VEKTOR di ruang 4-dimensi.
Seluruh dataset adalah kumpulan vektor → MATRIKS.
```

```python
import numpy as np

# === VEKTOR ===
# Vektor fitur mahasiswa: [ipk, jam_belajar, kehadiran_persen, tugas_selesai]
v1 = np.array([3.45, 4.0, 85, 10])  # Mahasiswa 1
v2 = np.array([3.12, 2.5, 70, 7])   # Mahasiswa 2

print(f"Vektor mahasiswa 1: {v1}")
print(f"Vektor mahasiswa 2: {v2}")
print(f"Dimensi vektor: {v1.shape[0]}")

# === OPERASI VEKTOR ===
# 1. Penjumlahan dan pengurangan
print(f"\nv1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")

# 2. Perkalian skalar
print(f"2 * v1 = {2 * v1}")

# 3. Dot product (perkalian titik)
# Mengukur "kesamaan arah" dua vektor
dot = np.dot(v1, v2)
print(f"\nDot product v1 · v2 = {dot:.2f}")

# 4. Norma (magnitude/panjang vektor)
# Euclidean norm (L2 norm)
norma_v1 = np.linalg.norm(v1)
print(f"||v1|| = {norma_v1:.2f}")

# 5. Jarak Euclidean antara dua vektor
jarak = np.linalg.norm(v1 - v2)
print(f"Jarak Euclidean v1-v2 = {jarak:.2f}")

# 6. Cosine Similarity
cos_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
print(f"Cosine Similarity = {cos_sim:.4f}")
```

**Mengapa vektor penting di ML?**

| Konsep ML | Peran Vektor |
|-----------|-------------|
| **kNN** | Menghitung jarak Euclidean antar vektor fitur |
| **SVM** | Mencari hyperplane yang memisahkan vektor fitur |
| **Word Embedding** | Kata direpresentasikan sebagai vektor (Word2Vec, GloVe) |
| **Neural Network** | Input, weight, bias, output — semua adalah vektor |
| **PCA** | Menemukan arah vektor dengan variansi terbesar |

### 3.1.2 Matriks dan Operasi Matriks

**Matriks** adalah array 2D dari bilangan — di ML, matriks adalah **dataset** itu sendiri.

```
Dataset sebagai Matriks X (m × n):
- m baris = jumlah sampel data
- n kolom = jumlah fitur

     fitur_1  fitur_2  fitur_3  fitur_4
X = ┌                                  ┐
    │  3.45    4.0     85       10     │  ← sampel 1
    │  3.12    2.5     70        7     │  ← sampel 2
    │  3.78    5.0     92       12     │  ← sampel 3
    │  3.21    3.0     75        8     │  ← sampel 4
    │  3.55    4.5     88       11     │  ← sampel 5
    └                                  ┘
                5 × 4 matrix
```

```python
import numpy as np

# === MATRIKS ===
# Dataset: 5 mahasiswa × 4 fitur
X = np.array([
    [3.45, 4.0, 85, 10],
    [3.12, 2.5, 70,  7],
    [3.78, 5.0, 92, 12],
    [3.21, 3.0, 75,  8],
    [3.55, 4.5, 88, 11],
])

print(f"Matriks X:\n{X}")
print(f"Shape: {X.shape}")  # (5, 4) = 5 baris, 4 kolom

# === OPERASI MATRIKS ===
# 1. Transpose
X_T = X.T
print(f"\nTranspose X^T:\n{X_T}")
print(f"Shape transpose: {X_T.shape}")  # (4, 5)

# 2. Perkalian matriks (matrix multiplication)
# X^T X menghasilkan matriks kovariansi (penting untuk PCA)
XTX = X.T @ X  # atau np.dot(X.T, X)
print(f"\nX^T × X:\n{XTX.round(2)}")
print(f"Shape: {XTX.shape}")  # (4, 4)

# 3. Matriks identitas
I = np.eye(4)
print(f"\nMatriks Identitas 4×4:\n{I}")

# 4. Determinan
A = np.array([[3, 1], [2, 4]])
det_A = np.linalg.det(A)
print(f"\nMatriks A:\n{A}")
print(f"Determinan A: {det_A:.2f}")

# 5. Invers matriks
A_inv = np.linalg.inv(A)
print(f"Invers A:\n{A_inv.round(4)}")

# Verifikasi: A × A^(-1) = I
print(f"A × A^(-1):\n{(A @ A_inv).round(2)}")

# 6. Menyelesaikan sistem persamaan linear: Ax = b
# 3x + y = 9
# 2x + 4y = 16
# Solusi: x = A^(-1) × b
b = np.array([9, 16])
x = np.linalg.solve(A, b)
print(f"\nSistem persamaan Ax = b:")
print(f"Solusi x = {x}")  # [2, 3] → x=2, y=3
```

### 3.1.3 Eigenvalue dan Eigenvector (Preview untuk PCA)

**Eigenvalue** dan **eigenvector** adalah konsep fundamental yang digunakan dalam **PCA** (Principal Component Analysis) — teknik reduksi dimensi yang sangat penting di ML.

```
INTUISI EIGENVALUE & EIGENVECTOR
════════════════════════════════════════════════
Jika A adalah transformasi linear, maka eigenvector v
adalah vektor yang TIDAK BERUBAH ARAH setelah transformasi,
hanya berubah PANJANG (diskalakan oleh eigenvalue λ).

A × v = λ × v

Dimana:
  A = matriks transformasi
  v = eigenvector (arah)
  λ = eigenvalue (skala / besaran)
════════════════════════════════════════════════
```

```python
import numpy as np

# Matriks kovariansi (contoh sederhana 2D)
# Kovariansi antara 2 fitur: IPK dan jam_belajar
cov_matrix = np.array([
    [0.25, 0.15],   # var(IPK), cov(IPK, jam_belajar)
    [0.15, 0.36]    # cov(jam_belajar, IPK), var(jam_belajar)
])

# Hitung eigenvalue dan eigenvector
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print(f"Matriks Kovariansi:\n{cov_matrix}")
print(f"\nEigenvalues: {eigenvalues.round(4)}")
print(f"\nEigenvectors:\n{eigenvectors.round(4)}")

# Interpretasi untuk PCA:
# - Eigenvalue terbesar → menunjukkan arah variansi terbesar (PC1)
# - Eigenvalue terkecil → arah variansi terkecil (PC2)
total_var = np.sum(eigenvalues)
print(f"\nVariansi yang dijelaskan oleh PC1: {eigenvalues[0]/total_var*100:.1f}%")
print(f"Variansi yang dijelaskan oleh PC2: {eigenvalues[1]/total_var*100:.1f}%")

# Verifikasi: A × v = λ × v
for i in range(len(eigenvalues)):
    Av = cov_matrix @ eigenvectors[:, i]
    lv = eigenvalues[i] * eigenvectors[:, i]
    print(f"\nVerifikasi eigenvector {i+1}:")
    print(f"  A × v = {Av.round(6)}")
    print(f"  λ × v = {lv.round(6)}")
    print(f"  Sama? {np.allclose(Av, lv)}")
```

**Hubungan dengan PCA:**

| Konsep | Peran dalam PCA |
|--------|----------------|
| Matriks kovariansi | Mengukur hubungan antar fitur |
| Eigenvector | Arah komponen utama (principal components) |
| Eigenvalue | Besarnya variansi yang ditangkap oleh setiap PC |
| Eigenvalue terbesar | Komponen yang paling informatif |

> **Catatan:** Di Bab selanjutnya, kita akan mengimplementasikan PCA secara lengkap menggunakan `sklearn.decomposition.PCA`. Di sini, kita membangun intuisi matematisnya.

---

## 3.2 Probabilitas untuk Machine Learning

### 3.2.1 Review: Probabilitas Kondisional

Probabilitas kondisional (*conditional probability*) adalah probabilitas suatu kejadian **given** kejadian lain sudah terjadi.

```
P(A|B) = P(A ∩ B) / P(B)

"Probabilitas A terjadi, DIBERIKAN B sudah terjadi"
```

```python
import numpy as np

# Contoh: Data mahasiswa UAI
# 100 mahasiswa, dengan data kelulusan dan kehadiran
np.random.seed(42)

n = 1000
kehadiran_tinggi = np.random.choice([True, False], n, p=[0.6, 0.4])
# Jika kehadiran tinggi, peluang lulus lebih besar
lulus = np.array([
    np.random.choice([True, False], p=[0.85, 0.15]) if k
    else np.random.choice([True, False], p=[0.40, 0.60])
    for k in kehadiran_tinggi
])

# Hitung probabilitas
P_lulus = np.mean(lulus)
P_kehadiran_tinggi = np.mean(kehadiran_tinggi)
P_lulus_dan_kehadiran = np.mean(lulus & kehadiran_tinggi)

# Probabilitas kondisional
P_lulus_given_kehadiran = P_lulus_dan_kehadiran / P_kehadiran_tinggi

print(f"=== PROBABILITAS ===")
print(f"P(Lulus) = {P_lulus:.3f}")
print(f"P(Kehadiran Tinggi) = {P_kehadiran_tinggi:.3f}")
print(f"P(Lulus ∩ Kehadiran Tinggi) = {P_lulus_dan_kehadiran:.3f}")
print(f"P(Lulus | Kehadiran Tinggi) = {P_lulus_given_kehadiran:.3f}")

# Bandingkan: P(Lulus | Kehadiran Rendah)
P_kehadiran_rendah = 1 - P_kehadiran_tinggi
P_lulus_dan_kehadiran_rendah = np.mean(lulus & ~kehadiran_tinggi)
P_lulus_given_kehadiran_rendah = P_lulus_dan_kehadiran_rendah / P_kehadiran_rendah

print(f"P(Lulus | Kehadiran Rendah) = {P_lulus_given_kehadiran_rendah:.3f}")
print(f"\nKesimpulan: Kehadiran tinggi meningkatkan peluang lulus secara signifikan!")
```

### 3.2.2 Bayes' Theorem dan Perannya dalam ML

**Bayes' Theorem** adalah fondasi untuk banyak algoritma ML, terutama **Naive Bayes Classifier**.

```
                    P(B|A) × P(A)
P(A|B) = ─────────────────────────
                    P(B)

Dimana:
  P(A|B) = POSTERIOR  — probabilitas A setelah melihat evidence B
  P(A)   = PRIOR      — probabilitas A sebelum melihat evidence
  P(B|A) = LIKELIHOOD — probabilitas melihat B jika A benar
  P(B)   = EVIDENCE   — probabilitas B secara keseluruhan
```

```
INTUISI BAYES' THEOREM
═══════════════════════════════════════════════════
Contoh: Deteksi email spam

PRIOR:       P(Spam) = 30% email adalah spam
LIKELIHOOD:  P("gratis"|Spam) = 80% spam mengandung kata "gratis"
EVIDENCE:    P("gratis") = 35% email mengandung kata "gratis"

POSTERIOR:   P(Spam|"gratis") = (0.80 × 0.30) / 0.35
                               = 0.686 ≈ 69%

→ Jika email mengandung kata "gratis",
  probabilitas spam meningkat dari 30% menjadi 69%
═══════════════════════════════════════════════════
```

```python
import numpy as np

# === BAYES' THEOREM: Deteksi Spam ===
# Prior probabilities
P_spam = 0.30
P_not_spam = 0.70

# Likelihood: P(kata|kelas)
P_gratis_given_spam = 0.80
P_gratis_given_not_spam = 0.10

# Evidence: P(gratis) = P(gratis|spam)P(spam) + P(gratis|not_spam)P(not_spam)
P_gratis = P_gratis_given_spam * P_spam + P_gratis_given_not_spam * P_not_spam

# Posterior: P(spam|gratis)
P_spam_given_gratis = (P_gratis_given_spam * P_spam) / P_gratis

print(f"=== BAYES' THEOREM: DETEKSI SPAM ===")
print(f"Prior P(Spam) = {P_spam:.2f}")
print(f"Likelihood P('gratis'|Spam) = {P_gratis_given_spam:.2f}")
print(f"Evidence P('gratis') = {P_gratis:.2f}")
print(f"Posterior P(Spam|'gratis') = {P_spam_given_gratis:.4f}")
print(f"\nKesimpulan: Email dengan kata 'gratis' → {P_spam_given_gratis*100:.1f}% kemungkinan spam")

# === NAIVE BAYES dengan multiple kata ===
# Asumsi "naive": kata-kata independen satu sama lain
kata_email = ['gratis', 'hadiah', 'klik']
P_kata_given_spam = {'gratis': 0.80, 'hadiah': 0.60, 'klik': 0.70}
P_kata_given_not_spam = {'gratis': 0.10, 'hadiah': 0.05, 'klik': 0.15}

# Hitung P(spam|kata1, kata2, kata3)
likelihood_spam = np.prod([P_kata_given_spam[k] for k in kata_email])
likelihood_not_spam = np.prod([P_kata_given_not_spam[k] for k in kata_email])

P_spam_posterior = (likelihood_spam * P_spam) / (
    likelihood_spam * P_spam + likelihood_not_spam * P_not_spam
)

print(f"\n=== NAIVE BAYES: Multiple Kata ===")
print(f"Kata dalam email: {kata_email}")
print(f"P(Spam|kata) = {P_spam_posterior:.6f}")
print(f"→ {P_spam_posterior*100:.2f}% kemungkinan spam")
```

### 3.2.3 Distribusi Probabilitas yang Relevan untuk ML

| Distribusi | Tipe | Digunakan di |
|-----------|------|-------------|
| **Bernoulli** | Diskret (0/1) | Naive Bayes, binary classification |
| **Multinomial** | Diskret (multi-kelas) | Text classification, Naive Bayes |
| **Normal (Gaussian)** | Kontinu | Gaussian Naive Bayes, asumsi banyak model |
| **Uniform** | Kontinu | Random initialization, random search |
| **Poisson** | Diskret (count) | Count prediction, arrival rate |

```python
import numpy as np
import matplotlib.pyplot as plt

# Visualisasi distribusi Normal (Gaussian)
np.random.seed(42)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 1. Normal Distribution
x_normal = np.random.normal(loc=75, scale=10, size=1000)
axes[0].hist(x_normal, bins=30, density=True, alpha=0.7, color='steelblue')
axes[0].set_title('Distribusi Normal\n(μ=75, σ=10)')
axes[0].set_xlabel('Nilai')

# 2. Uniform Distribution
x_uniform = np.random.uniform(low=50, high=100, size=1000)
axes[1].hist(x_uniform, bins=30, density=True, alpha=0.7, color='green')
axes[1].set_title('Distribusi Uniform\n(50-100)')
axes[1].set_xlabel('Nilai')

# 3. Poisson Distribution
x_poisson = np.random.poisson(lam=5, size=1000)
axes[2].hist(x_poisson, bins=range(15), density=True, alpha=0.7, color='coral')
axes[2].set_title('Distribusi Poisson\n(λ=5)')
axes[2].set_xlabel('Jumlah kejadian')

plt.tight_layout()
plt.savefig('distribusi_probabilitas.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## 3.3 Kalkulus untuk Machine Learning

### 3.3.1 Turunan (Derivatives) dan Gradien

**Turunan** (*derivative*) mengukur **laju perubahan** suatu fungsi. Dalam ML, turunan digunakan untuk **mengoptimasi** model — menemukan parameter yang meminimalkan error.

```
INTUISI TURUNAN DALAM ML
═══════════════════════════════════════════════
Bayangkan Anda berdiri di lereng gunung dalam kegelapan.
Anda ingin turun ke lembah (titik terendah).

Turunan (gradient) memberitahu Anda:
  → ARAH mana yang menurun (tanda: + atau -)
  → SEBERAPA CURAM lerengnya (besaran)

Anda melangkah ke arah yang menurun → GRADIENT DESCENT!
═══════════════════════════════════════════════
```

```python
import numpy as np

# === TURUNAN NUMERIK ===
# Definisi: f'(x) ≈ (f(x+h) - f(x-h)) / (2h)

def f(x):
    """Fungsi contoh: f(x) = x^2 + 3x + 2"""
    return x**2 + 3*x + 2

def turunan_numerik(func, x, h=1e-7):
    """Hitung turunan numerik menggunakan central difference"""
    return (func(x + h) - func(x - h)) / (2 * h)

# Turunan f(x) = x^2 + 3x + 2 → f'(x) = 2x + 3
x_values = np.array([-2, -1, 0, 1, 2, 3])
print("=== TURUNAN NUMERIK ===")
print("f(x) = x² + 3x + 2")
print("f'(x) = 2x + 3 (analitik)")
print(f"{'x':>5} {'f(x)':>8} {'f\'(x) numerik':>15} {'f\'(x) analitik':>16}")
for x in x_values:
    num = turunan_numerik(f, x)
    analitik = 2*x + 3
    print(f"{x:5.1f} {f(x):8.2f} {num:15.6f} {analitik:16.1f}")

# === GRADIEN (Multi-variabel) ===
# Untuk fungsi multi-variabel, gradien adalah vektor turunan parsial
def cost_function(w, X, y):
    """Mean Squared Error: L(w) = (1/n) Σ(y - Xw)²"""
    predictions = X @ w
    errors = y - predictions
    return np.mean(errors**2)

def gradient(w, X, y):
    """Gradien MSE: ∇L = -(2/n) X^T (y - Xw)"""
    n = len(y)
    predictions = X @ w
    errors = y - predictions
    return -(2/n) * X.T @ errors

# Contoh
np.random.seed(42)
X = np.column_stack([np.ones(10), np.random.randn(10)])  # dengan bias
y = 3 + 2 * X[:, 1] + np.random.randn(10) * 0.5  # y = 3 + 2x + noise
w = np.array([0.0, 0.0])  # inisialisasi

print(f"\n=== GRADIEN MSE ===")
print(f"Weight awal: {w}")
print(f"Cost awal: {cost_function(w, X, y):.4f}")
print(f"Gradien awal: {gradient(w, X, y).round(4)}")
```

### 3.3.2 Gradient Descent: Cost Function, Learning Rate, Convergence

**Gradient Descent** adalah algoritma optimasi yang digunakan hampir di **semua** model ML untuk menemukan parameter optimal.

```
GRADIENT DESCENT
═══════════════════════════════════════════════
Langkah-langkah:
1. Inisialisasi parameter w secara acak
2. Hitung gradien (arah kemiringan cost function)
3. Update parameter: w_baru = w_lama - α × gradien
4. Ulangi sampai konvergen (gradien ≈ 0)

α (alpha) = LEARNING RATE
  → Terlalu besar: melompat-lompat, tidak konvergen
  → Terlalu kecil: konvergen sangat lambat
  → Tepat: konvergen dengan efisien
═══════════════════════════════════════════════
```

```python
import numpy as np

# === GRADIENT DESCENT: Linear Regression ===
np.random.seed(42)

# Generate data: y = 3 + 2x + noise
n = 50
X_raw = np.random.uniform(0, 10, n)
y = 3 + 2 * X_raw + np.random.randn(n) * 2

# Tambahkan kolom bias (intercept)
X = np.column_stack([np.ones(n), X_raw])

# Fungsi cost (MSE)
def mse_cost(w, X, y):
    predictions = X @ w
    return np.mean((y - predictions)**2)

# Fungsi gradien
def mse_gradient(w, X, y):
    n_samples = len(y)
    predictions = X @ w
    return -(2/n_samples) * X.T @ (y - predictions)

# === GRADIENT DESCENT ===
learning_rate = 0.01
n_iterations = 1000
w = np.array([0.0, 0.0])  # [intercept, slope]

# Simpan history untuk visualisasi
history_cost = []
history_w = []

for i in range(n_iterations):
    # Hitung gradien
    grad = mse_gradient(w, X, y)

    # Update parameter
    w = w - learning_rate * grad

    # Simpan history
    cost = mse_cost(w, X, y)
    history_cost.append(cost)
    history_w.append(w.copy())

    # Print setiap 200 iterasi
    if i % 200 == 0:
        print(f"Iterasi {i:4d}: Cost = {cost:.4f}, w = [{w[0]:.4f}, {w[1]:.4f}]")

print(f"\n=== HASIL AKHIR ===")
print(f"Intercept (w0) = {w[0]:.4f}  (target: 3.0)")
print(f"Slope (w1)     = {w[1]:.4f}  (target: 2.0)")
print(f"Final Cost     = {history_cost[-1]:.4f}")

# Bandingkan dengan solusi analitik (Normal Equation)
w_analitik = np.linalg.inv(X.T @ X) @ X.T @ y
print(f"\nSolusi Analitik: w = [{w_analitik[0]:.4f}, {w_analitik[1]:.4f}]")
```

### 3.3.3 Visualisasi Gradient Descent

```python
import numpy as np
import matplotlib.pyplot as plt

# Menggunakan data dan history dari kode sebelumnya
# Visualisasi proses konvergensi

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: Cost function vs Iterasi
axes[0].plot(history_cost, color='red', linewidth=1.5)
axes[0].set_title('Konvergensi Cost Function', fontsize=12)
axes[0].set_xlabel('Iterasi')
axes[0].set_ylabel('MSE (Cost)')
axes[0].set_yscale('log')
axes[0].grid(True, alpha=0.3)
axes[0].axhline(y=history_cost[-1], color='green', linestyle='--', alpha=0.5,
                label=f'Final: {history_cost[-1]:.2f}')
axes[0].legend()

# Plot 2: Data dan garis regresi hasil gradient descent
axes[1].scatter(X_raw, y, alpha=0.6, label='Data', color='steelblue')
x_line = np.linspace(0, 10, 100)
y_line = w[0] + w[1] * x_line
axes[1].plot(x_line, y_line, 'r-', linewidth=2, label=f'y = {w[0]:.2f} + {w[1]:.2f}x')
axes[1].set_title('Hasil Regresi Linear', fontsize=12)
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# Plot 3: Perubahan parameter w selama training
w0_history = [w_pair[0] for w_pair in history_w]
w1_history = [w_pair[1] for w_pair in history_w]
axes[2].plot(w0_history, label='w0 (intercept)', color='blue')
axes[2].plot(w1_history, label='w1 (slope)', color='orange')
axes[2].set_title('Evolusi Parameter', fontsize=12)
axes[2].set_xlabel('Iterasi')
axes[2].set_ylabel('Nilai Parameter')
axes[2].legend()
axes[2].grid(True, alpha=0.3)
axes[2].axhline(y=3, color='blue', linestyle=':', alpha=0.3)
axes[2].axhline(y=2, color='orange', linestyle=':', alpha=0.3)

plt.tight_layout()
plt.savefig('gradient_descent_visualization.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 3.3.4 Efek Learning Rate

```python
import numpy as np

# Demonstrasi efek learning rate yang berbeda
np.random.seed(42)
n = 50
X_raw = np.random.uniform(0, 10, n)
y = 3 + 2 * X_raw + np.random.randn(n) * 2
X = np.column_stack([np.ones(n), X_raw])

learning_rates = [0.001, 0.01, 0.05, 0.1]

print("=== EFEK LEARNING RATE ===")
print(f"{'Learning Rate':>15} {'Iterasi 100 Cost':>18} {'Iterasi 500 Cost':>18} {'Final Cost (1000)':>18}")

for lr in learning_rates:
    w = np.array([0.0, 0.0])
    costs = []
    for i in range(1000):
        grad = -(2/n) * X.T @ (y - X @ w)
        w = w - lr * grad
        costs.append(np.mean((y - X @ w)**2))

    if not np.isnan(costs[-1]) and costs[-1] < 1e10:
        print(f"{lr:>15.3f} {costs[99]:>18.4f} {costs[499]:>18.4f} {costs[-1]:>18.4f}")
    else:
        print(f"{lr:>15.3f} {'DIVERGEN':>18} {'DIVERGEN':>18} {'DIVERGEN':>18}")
```

```
TIPS MEMILIH LEARNING RATE
═══════════════════════════════════════
α terlalu kecil → Konvergen LAMBAT (butuh ribuan iterasi)
α terlalu besar → DIVERGEN (cost meningkat, bukan menurun)
α tepat         → Konvergen CEPAT dan STABIL

Praktik umum:
1. Mulai dari α = 0.01
2. Jika divergen → kurangi (÷10)
3. Jika terlalu lambat → tingkatkan (×3)
4. Gunakan learning rate scheduling (menurun seiring waktu)
═══════════════════════════════════════
```

---

## 3.4 Mengapa Matematika Penting: Koneksi ke Algoritma ML

### 3.4.1 Peta Konsep Matematika ↔ ML

```
MATEMATIKA                              ALGORITMA ML
═══════════════                         ═══════════════
LINEAR ALGEBRA
  Vektor & jarak          ─────→        kNN, clustering
  Perkalian matriks       ─────→        Neural Networks
  Eigenvalue/Eigenvector  ─────→        PCA
  Matriks invers          ─────→        Linear Regression (Normal Equation)

PROBABILITAS
  Bayes' Theorem          ─────→        Naive Bayes Classifier
  Distribusi Gaussian     ─────→        Gaussian Naive Bayes, GMM
  Probabilitas kondisional ────→        Decision Tree (information gain)
  Maximum Likelihood      ─────→        Logistic Regression

KALKULUS
  Turunan & gradien       ─────→        Gradient Descent (semua model)
  Chain rule              ─────→        Backpropagation (Neural Networks)
  Optimasi                ─────→        Loss function minimization
```

### 3.4.2 Contoh: Matematika di Balik Linear Regression

```python
import numpy as np

# Linear Regression — dua pendekatan:
# 1. Normal Equation (aljabar linear)
# 2. Gradient Descent (kalkulus)

np.random.seed(42)
n = 100
X_raw = np.random.uniform(1, 10, n)
y = 5 + 3 * X_raw + np.random.randn(n) * 2
X = np.column_stack([np.ones(n), X_raw])

# PENDEKATAN 1: Normal Equation
# w* = (X^T X)^(-1) X^T y
w_normal = np.linalg.inv(X.T @ X) @ X.T @ y
print(f"=== NORMAL EQUATION ===")
print(f"w = [{w_normal[0]:.4f}, {w_normal[1]:.4f}]")
print(f"MSE = {np.mean((y - X @ w_normal)**2):.4f}")

# PENDEKATAN 2: Gradient Descent
w_gd = np.array([0.0, 0.0])
lr = 0.01
for _ in range(2000):
    grad = -(2/n) * X.T @ (y - X @ w_gd)
    w_gd = w_gd - lr * grad
print(f"\n=== GRADIENT DESCENT ===")
print(f"w = [{w_gd[0]:.4f}, {w_gd[1]:.4f}]")
print(f"MSE = {np.mean((y - X @ w_gd)**2):.4f}")

# PENDEKATAN 3: scikit-learn
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_raw.reshape(-1, 1), y)
print(f"\n=== SCIKIT-LEARN ===")
print(f"w = [{model.intercept_:.4f}, {model.coef_[0]:.4f}]")

print(f"\n→ Ketiga pendekatan menghasilkan parameter yang SAMA!")
print(f"→ Target sebenarnya: w = [5.0, 3.0]")
```

### 3.4.3 Pesan untuk Mahasiswa

```
┌─────────────────────────────────────────────────────┐
│         MENGAPA MAHASISWA PERLU MATEMATIKA?           │
│                                                       │
│  1. MEMAHAMI vs MENGHAFAL                             │
│     Tanpa matematika → hanya "tukang ketik sklearn"   │
│     Dengan matematika → memahami MENGAPA model kerja  │
│                                                       │
│  2. DEBUGGING                                         │
│     Jika model tidak bekerja, pemahaman matematika    │
│     membantu mendiagnosis masalah                     │
│                                                       │
│  3. INOVASI                                           │
│     Untuk menciptakan algoritma baru atau modifikasi, │
│     fondasi matematika adalah keharusan                │
│                                                       │
│  4. INTERVIEW                                         │
│     Perusahaan top menanyakan matematika di balik ML   │
│     di interview Data Scientist / ML Engineer         │
│                                                       │
│  "You don't need to be a math expert,                 │
│   but you need math intuition." — Andrew Ng           │
└─────────────────────────────────────────────────────┘
```

---

## 3.5 AI Corner: Menggunakan AI untuk Memahami Matematika

### 3.5.1 AI sebagai Tutor Matematika

Level: **Basic**

| AI Bisa | AI Tidak Bisa |
|---------|--------------|
| Menjelaskan konsep math dengan analogi | Menggantikan latihan soal (Anda harus mengerjakan sendiri) |
| Menunjukkan langkah-langkah derivasi | Memberikan intuisi yang mendalam tanpa Anda berpikir |
| Memvisualisasikan konsep (deskripsi) | Menjamin penjelasan selalu benar (verifikasi!) |
| Memberikan contoh numerik | Membuat Anda otomatis paham tanpa usaha |

### 3.5.2 Contoh Prompt untuk Belajar Matematika ML

**Prompt yang Baik:**
```
Saya mahasiswa informatika belajar machine learning.
Jelaskan gradient descent menggunakan analogi mendaki gunung
di Gunung Bromo. Sertakan:
1. Apa itu cost function (analoginya apa?)
2. Apa itu learning rate (analoginya apa?)
3. Apa yang terjadi jika learning rate terlalu besar/kecil?
4. Berikan contoh numerik sederhana (1 variabel)
```

**Prompt yang Kurang Baik:**
```
Jelaskan gradient descent
```

### 3.5.3 Aktivitas: Eksplorasi Matematika dengan AI

1. Minta AI menjelaskan **eigenvalue** menggunakan analogi dari kehidupan sehari-hari
2. Verifikasi penjelasan AI dengan menghitung eigenvalue menggunakan NumPy
3. Minta AI menjelaskan **mengapa** Bayes' Theorem penting untuk Naive Bayes
4. Bandingkan penjelasan AI dengan materi bab ini
5. Dokumentasikan dalam AI Usage Log

---

## Rangkuman Bab 3

1. **Aljabar Linear** adalah fondasi ML: vektor merepresentasikan data, matriks merepresentasikan dataset, dan operasi matriks adalah inti komputasi ML.
2. **Dot product** mengukur kesamaan dua vektor, **jarak Euclidean** mengukur perbedaan — keduanya fundamental untuk algoritma seperti kNN dan clustering.
3. **Eigenvalue dan eigenvector** digunakan dalam PCA untuk reduksi dimensi — eigenvalue menunjukkan besarnya variansi yang ditangkap.
4. **Bayes' Theorem** adalah dasar Naive Bayes Classifier: menghitung probabilitas posterior dari prior, likelihood, dan evidence.
5. **Gradient descent** adalah algoritma optimasi universal di ML: iteratif mengupdate parameter ke arah yang meminimalkan cost function.
6. **Learning rate** menentukan ukuran langkah gradient descent — terlalu besar → divergen, terlalu kecil → lambat.
7. Linear Regression bisa diselesaikan dengan **Normal Equation** (aljabar linear) atau **Gradient Descent** (kalkulus) — keduanya menghasilkan solusi yang sama.
8. Memahami matematika di balik ML membedakan **praktisi** yang memahami dari **operator** yang hanya menjalankan kode.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Diberikan dua vektor:
- v1 = [3, 4, 1]
- v2 = [1, 2, 5]

Hitung secara manual (kemudian verifikasi dengan NumPy):
- a) v1 + v2
- b) v1 - v2
- c) Dot product v1 · v2
- d) Norma (panjang) v1 dan v2
- e) Jarak Euclidean antara v1 dan v2

**Soal 2.** Diberikan matriks:
```
A = [[2, 1],    B = [[1, 3],
     [3, 4]]         [2, 0]]
```
Hitung secara manual (kemudian verifikasi dengan NumPy):
- a) A + B
- b) A × B (perkalian matriks)
- c) A^T (transpose A)
- d) Determinan A

**Soal 3.** Jelaskan dengan kata-kata Anda sendiri (tanpa rumus):
- a) Apa itu eigenvalue dan eigenvector?
- b) Mengapa eigenvalue penting untuk PCA?
- c) Apa hubungan antara eigenvalue terbesar dan variansi data?

**Soal 4.** Jelaskan Bayes' Theorem dengan contoh dari kehidupan sehari-hari di Indonesia (bukan contoh spam email).

**Soal 5.** Apa yang dimaksud dengan gradient descent? Jelaskan menggunakan analogi yang mudah dipahami.

### Tingkat Menengah (C2-C3)

**Soal 6.** Tulis kode Python (NumPy) untuk:
- a) Membuat matriks data 10x3 (10 mahasiswa, 3 fitur)
- b) Menghitung matriks kovariansi
- c) Menghitung eigenvalue dan eigenvector dari matriks kovariansi
- d) Menentukan komponen utama (eigenvector dengan eigenvalue terbesar)
- e) Interpretasikan hasilnya

**Soal 7.** Implementasikan Bayes' Theorem untuk kasus berikut:
- Sebuah tes COVID memiliki sensitivitas 95% (P(positif|sakit) = 0.95)
- Spesifisitas 90% (P(negatif|sehat) = 0.90)
- Prevalensi COVID di populasi adalah 2% (P(sakit) = 0.02)
- Pertanyaan: Jika seseorang tes positif, berapa probabilitas dia benar-benar sakit?
- Tulis kode Python untuk menghitungnya

**Soal 8.** Implementasikan gradient descent untuk menyelesaikan regresi linear pada data berikut:

```python
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2.1, 4.3, 5.8, 8.2, 10.1, 11.9, 14.2, 16.0, 17.8, 20.1])
```

- a) Temukan parameter optimal (intercept dan slope)
- b) Bandingkan dengan solusi sklearn
- c) Plot kurva konvergensi cost function

### Tingkat Mahir (C3-C4)

**Soal 9.** Eksperimen Learning Rate:
- Implementasikan gradient descent dengan learning rate: 0.001, 0.01, 0.05, 0.1, dan 0.5
- Plot kurva konvergensi cost function untuk semua learning rate dalam satu grafik
- Analisis: mana yang konvergen paling cepat? Mana yang divergen?
- Hubungkan dengan konsep matematika: mengapa learning rate terlalu besar menyebabkan divergensi?

**Soal 10.** Mini-project: Implementasikan Naive Bayes Classifier dari nol (tanpa sklearn) untuk klasifikasi sederhana:
- Buat dataset: 50 email dengan fitur word count untuk 5 kata (gratis, promo, harga, meeting, laporan)
- Label: spam (1) atau bukan (0)
- Implementasikan Bayes' Theorem untuk menghitung P(spam|kata1, kata2, ..., kata5)
- Bandingkan akurasi dengan `sklearn.naive_bayes.GaussianNB`

---

## Daftar Pustaka Bab 3

1. Strang, G. (2019). *Linear Algebra and Its Applications* (6th ed.). Cengage Learning.
2. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning* — Chapter 2: Linear Algebra, Chapter 3: Probability. MIT Press.
3. Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
4. Ng, A. (2018). *Machine Learning Yearning*. deeplearning.ai.
5. Deisenroth, M. P., Faisal, A. A., & Ong, C. S. (2020). *Mathematics for Machine Learning*. Cambridge University Press.
6. 3Blue1Brown. (2016-2024). *Essence of Linear Algebra* [Video series]. YouTube.
7. StatQuest with Josh Starmer. (2020-2024). *Machine Learning* [Video series]. YouTube.

---

*Bab berikutnya: **Bab 4 — Eksplorasi Data dan Feature Engineering***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
