# Minggu 3: Matematika untuk Machine Learning

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 3 |
| **Topik** | Matematika untuk Machine Learning |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK-2: Menerapkan fondasi matematika yang mendasari algoritma machine learning |
| **Sub-CPMK** | 3.1 Menerapkan operasi aljabar linear (vektor, matriks) dan konsep probabilitas dalam konteks ML |
| | 3.2 Menjelaskan intuisi gradient descent sebagai mekanisme pembelajaran model ML |
| **Bloom's Taxonomy** | C3 (Menerapkan / *Applying*) |
| **Durasi** | 2 x 100 menit (Teori 100 min + Praktikum 100 min) |
| **Platform** | Google Colab |
| **Metode** | Ceramah interaktif, live coding, visualisasi, hands-on Google Colab |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menerapkan** operasi aljabar linear dasar (vektor, matriks, dot product, perkalian matriks) menggunakan NumPy.
2. **Menjelaskan** konsep eigenvector dan eigenvalue serta relevansinya untuk teknik PCA (*Principal Component Analysis*).
3. **Menerapkan** konsep probabilitas dasar, conditional probability, dan Bayes Theorem dalam konteks machine learning.
4. **Menjelaskan** intuisi gradient descent — bagaimana model ML "belajar" melalui optimasi cost function.

---

## Materi Pembelajaran

### 1. Aljabar Linear untuk Machine Learning

#### Mengapa Aljabar Linear Penting untuk ML?

**Aljabar linear** (*linear algebra*) adalah bahasa matematika yang digunakan oleh hampir semua algoritma machine learning. Data dalam ML selalu direpresentasikan sebagai **vektor** dan **matriks**:

- Satu baris data (satu sampel) = satu **vektor**
- Seluruh dataset = satu **matriks**
- Operasi model (prediksi, training) = **operasi matriks**

> **Insight:** Ketika model regresi linear melakukan prediksi `y = Xw + b`, itu adalah **perkalian matriks**. Ketika neural network menghitung output, itu juga **perkalian matriks** diikuti fungsi aktivasi.

#### Vektor (*Vector*)

Vektor adalah array satu dimensi yang memiliki **magnitude** (besar) dan **direction** (arah).

```python
import numpy as np

# Vektor sebagai representasi data
# Contoh: fitur seorang mahasiswa [usia, IPK, jumlah_sks]
mahasiswa_1 = np.array([20, 3.75, 120])
mahasiswa_2 = np.array([22, 3.50, 140])

print(f"Vektor mahasiswa 1: {mahasiswa_1}")
print(f"Vektor mahasiswa 2: {mahasiswa_2}")
print(f"Dimensi vektor    : {mahasiswa_1.shape[0]} dimensi")
```

#### Operasi Vektor

```python
# Penjumlahan vektor
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print(f"v1 + v2 = {v1 + v2}")       # [5, 7, 9]
print(f"v1 - v2 = {v1 - v2}")       # [-3, -3, -3]
print(f"v1 * 3  = {v1 * 3}")        # [3, 6, 9] (scalar multiplication)

# Magnitude (panjang) vektor
# ||v|| = sqrt(v1^2 + v2^2 + v3^2)
magnitude = np.linalg.norm(v1)
print(f"\nMagnitude v1 = {magnitude:.4f}")

# Unit vector (vektor dengan panjang 1)
unit_v1 = v1 / magnitude
print(f"Unit vector  = {unit_v1}")
print(f"Panjang unit = {np.linalg.norm(unit_v1):.4f}")  # 1.0
```

#### Dot Product (Perkalian Titik)

Dot product adalah operasi fundamental dalam ML — digunakan dalam regresi linear, cosine similarity, dan neural networks.

```python
# Dot product: a · b = a1*b1 + a2*b2 + ... + an*bn
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Cara 1: np.dot
dot_product = np.dot(a, b)  # 1*4 + 2*5 + 3*6 = 32
print(f"a · b = {dot_product}")

# Cara 2: operator @
dot_product_2 = a @ b
print(f"a @ b = {dot_product_2}")

# Aplikasi ML: Prediksi regresi linear sederhana
# y = w · x + b  (w: weights, x: features, b: bias)
weights = np.array([0.5, 0.3, 0.2])  # Model weights
features = np.array([85, 90, 78])     # Nilai mahasiswa
bias = 10

prediksi = np.dot(weights, features) + bias
print(f"\nContoh prediksi linear:")
print(f"Weights  : {weights}")
print(f"Features : {features}")
print(f"Prediksi : w · x + b = {prediksi}")
```

#### Cosine Similarity

Mengukur kemiripan arah antara dua vektor — banyak digunakan dalam NLP dan recommendation systems.

```python
# Cosine Similarity: cos(θ) = (a · b) / (||a|| * ||b||)
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Contoh: Kemiripan preferensi pengguna e-commerce
# Fitur: [elektronik, fashion, makanan, buku, olahraga]
user_ahmad = np.array([5, 1, 3, 4, 2])  # Ahmad suka elektronik dan buku
user_budi  = np.array([4, 2, 2, 5, 1])  # Budi juga suka elektronik dan buku
user_citra = np.array([1, 5, 4, 1, 3])  # Citra suka fashion dan makanan

sim_ab = cosine_similarity(user_ahmad, user_budi)
sim_ac = cosine_similarity(user_ahmad, user_citra)

print("=== Cosine Similarity (Recommendation System) ===")
print(f"Similarity Ahmad-Budi  : {sim_ab:.4f}")
print(f"Similarity Ahmad-Citra : {sim_ac:.4f}")
print(f"\nAhmad lebih mirip dengan {'Budi' if sim_ab > sim_ac else 'Citra'}")
print("(Ini adalah dasar dari collaborative filtering di Tokopedia!)")
```

---

### 2. Matriks dan Operasi Matriks

#### Matriks sebagai Dataset

```python
# Matriks = kumpulan vektor = dataset
# Setiap baris = satu sampel, setiap kolom = satu fitur

# Dataset: 5 mahasiswa, 3 fitur [usia, IPK, jumlah_SKS]
X = np.array([
    [20, 3.75, 120],
    [22, 3.50, 140],
    [21, 3.85, 130],
    [23, 3.20, 150],
    [20, 3.90, 110]
])

print("=== Dataset sebagai Matriks ===")
print(f"Shape: {X.shape} ({X.shape[0]} sampel, {X.shape[1]} fitur)")
print(f"\nMatriks X:\n{X}")
```

#### Perkalian Matriks (*Matrix Multiplication*)

```python
# Perkalian matriks: C = A @ B
# Syarat: kolom A = baris B
# Hasil: (m x n) @ (n x p) = (m x p)

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])  # 3x2

B = np.array([[7, 8, 9],
              [10, 11, 12]])  # 2x3

C = A @ B  # 3x3
print("A (3x2):")
print(A)
print("\nB (2x3):")
print(B)
print("\nC = A @ B (3x3):")
print(C)

# Aplikasi ML: Forward pass di neural network
# output = activation(W @ x + b)
print("\n=== Aplikasi: Forward Pass Neural Network ===")
W = np.array([[0.1, 0.2, 0.3],
              [0.4, 0.5, 0.6]])  # Weight matrix 2x3

x = np.array([1.0, 2.0, 3.0])   # Input vector
b = np.array([0.1, 0.2])         # Bias vector

output = W @ x + b
print(f"W @ x + b = {output}")
```

#### Transpose dan Inverse

```python
# Transpose: menukar baris dan kolom
A = np.array([[1, 2, 3],
              [4, 5, 6]])

print(f"A (2x3):\n{A}")
print(f"\nA transpose (3x2):\n{A.T}")

# Inverse: A^(-1) sehingga A @ A^(-1) = I (identitas)
# Hanya untuk matriks persegi dan non-singular
B = np.array([[2, 1],
              [5, 3]])

B_inv = np.linalg.inv(B)
print(f"\nB:\n{B}")
print(f"\nB inverse:\n{B_inv}")
print(f"\nB @ B_inv (harus identitas):\n{(B @ B_inv).round(10)}")
```

---

### 3. Eigenvectors dan Eigenvalues (Preview untuk PCA)

#### Konsep Intuitif

**Eigenvector** adalah vektor yang **tidak berubah arahnya** ketika dikalikan dengan matriks — hanya berubah panjangnya. Faktor perubahan panjang disebut **eigenvalue**.

```
A @ v = λ * v
```
- `A` = matriks
- `v` = eigenvector
- `λ` (lambda) = eigenvalue

#### Implementasi dengan NumPy

```python
# Menghitung eigenvectors dan eigenvalues
A = np.array([[4, 2],
              [1, 3]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("=== Eigenvectors & Eigenvalues ===")
print(f"Matriks A:\n{A}")
print(f"\nEigenvalues : {eigenvalues}")
print(f"\nEigenvectors:\n{eigenvectors}")

# Verifikasi: A @ v = λ * v
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    lmbda = eigenvalues[i]
    Av = A @ v
    lv = lmbda * v
    print(f"\nEigenpair {i+1}: λ = {lmbda:.2f}")
    print(f"  A @ v     = {Av}")
    print(f"  λ * v     = {lv}")
    print(f"  Sama? {np.allclose(Av, lv)}")
```

#### Relevansi untuk PCA

```python
# Preview: Bagaimana eigenvectors digunakan di PCA
# PCA menemukan arah (eigenvector) yang menangkap variasi terbesar dalam data

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load data
iris = load_iris()
X = iris.data

# PCA: reduksi dari 4 fitur ke 2 komponen utama
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print("=== Preview PCA (akan dipelajari lebih lanjut) ===")
print(f"Data asli     : {X.shape} (4 fitur)")
print(f"Setelah PCA   : {X_pca.shape} (2 komponen)")
print(f"Variance ratio: {pca.explained_variance_ratio_}")
print(f"Total variance: {sum(pca.explained_variance_ratio_)*100:.1f}%")
print("\nDengan hanya 2 komponen, PCA menangkap ~95% informasi!")
print("Eigenvectors menentukan ARAH komponen utama.")
print("Eigenvalues menentukan PENTINGNYA setiap komponen.")
```

---

### 4. Probabilitas untuk Machine Learning

#### Review Probabilitas Dasar

Probabilitas adalah fondasi dari banyak algoritma ML, terutama untuk klasifikasi, generative models, dan Bayesian methods.

```python
# Contoh: Probabilitas dari data mahasiswa
import pandas as pd

data = {
    'mahasiswa': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],
    'jurusan': ['IF', 'IF', 'IF', 'IF', 'IF', 'IF', 'IF', 'IF', 'IF', 'IF',
                'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI'],
    'lulus_tepat_waktu': ['Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak',
                          'Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak']
}
df = pd.DataFrame(data)

# Probabilitas dasar
total = len(df)
p_if = len(df[df['jurusan'] == 'IF']) / total
p_lulus = len(df[df['lulus_tepat_waktu'] == 'Ya']) / total

print("=== Probabilitas Dasar ===")
print(f"P(Informatika)     = {p_if:.2f}")
print(f"P(Lulus Tepat Waktu) = {p_lulus:.2f}")
```

#### Conditional Probability (Probabilitas Bersyarat)

```python
# P(A|B) = P(A ∩ B) / P(B)
# P(Lulus | Informatika) = P(Lulus ∩ Informatika) / P(Informatika)

mahasiswa_if = df[df['jurusan'] == 'IF']
p_lulus_given_if = len(mahasiswa_if[mahasiswa_if['lulus_tepat_waktu'] == 'Ya']) / len(mahasiswa_if)

mahasiswa_si = df[df['jurusan'] == 'SI']
p_lulus_given_si = len(mahasiswa_si[mahasiswa_si['lulus_tepat_waktu'] == 'Ya']) / len(mahasiswa_si)

print("=== Conditional Probability ===")
print(f"P(Lulus | Informatika) = {p_lulus_given_if:.2f}")
print(f"P(Lulus | Sistem Info) = {p_lulus_given_si:.2f}")

# Dalam ML: classifier menghitung P(kelas | fitur)
print("\nDalam ML, kita menghitung: P(kelas | fitur-fitur)")
print("Contoh: P(Lulus Tepat Waktu | IPK=3.5, SKS=20, Aktif=Ya)")
```

#### Bayes Theorem

Teorema Bayes adalah dasar dari **Naive Bayes classifier** — salah satu algoritma ML yang paling sederhana namun efektif.

```
P(A|B) = P(B|A) * P(A) / P(B)
```

```python
# Contoh Bayes Theorem: Deteksi Email Spam
# P(Spam | kata "gratis") = ?

# Data yang diketahui:
p_spam = 0.30                    # 30% email adalah spam
p_not_spam = 0.70                # 70% email bukan spam
p_gratis_given_spam = 0.80       # 80% email spam mengandung kata "gratis"
p_gratis_given_not_spam = 0.10   # 10% email non-spam mengandung kata "gratis"

# P(gratis) = P(gratis|spam)*P(spam) + P(gratis|not_spam)*P(not_spam)
p_gratis = (p_gratis_given_spam * p_spam +
            p_gratis_given_not_spam * p_not_spam)

# Bayes Theorem
p_spam_given_gratis = (p_gratis_given_spam * p_spam) / p_gratis

print("=== Bayes Theorem: Deteksi Spam ===")
print(f"P(Spam)                    = {p_spam:.2f}")
print(f"P('gratis' | Spam)         = {p_gratis_given_spam:.2f}")
print(f"P('gratis' | Not Spam)     = {p_gratis_given_not_spam:.2f}")
print(f"P('gratis')                = {p_gratis:.2f}")
print(f"\nP(Spam | 'gratis')         = {p_spam_given_gratis:.4f}")
print(f"\nJika email mengandung kata 'gratis',")
print(f"probabilitas email tersebut spam = {p_spam_given_gratis*100:.1f}%")
```

---

### 5. Gradient Descent: Bagaimana Model ML "Belajar"

#### Intuisi Gradient Descent

Bayangkan Anda berada di puncak gunung dalam **kegelapan total** dan ingin turun ke lembah terendah. Anda tidak bisa melihat seluruh gunung, tapi bisa merasakan **kemiringan tanah** di bawah kaki Anda. Strategi terbaik:

1. Rasakan arah paling **curam ke bawah** (gradien)
2. Ambil **langkah kecil** ke arah tersebut (learning rate)
3. Ulangi sampai mencapai titik terendah (konvergensi)

Inilah **gradient descent** — cara model ML menemukan parameter terbaik.

```
┌──────────────────────────────────────┐
│    Cost Function J(w)                │
│                                      │
│    *                                 │
│     \                      *         │
│      \                    /          │
│       \                  /           │
│        \    ___         /            │
│         \  /   \       /             │
│          \/     \     /              │
│                  \___/               │
│           ▲                          │
│    Minimum (target)                  │
│                                      │
│  Gradient Descent: ikuti kemiringan  │
│  menuju titik minimum               │
└──────────────────────────────────────┘
```

#### Cost Function (Fungsi Biaya)

Cost function mengukur **seberapa buruk** prediksi model dibandingkan dengan nilai sebenarnya.

Untuk regresi linear, cost function yang umum adalah **Mean Squared Error (MSE)**:

```
MSE = (1/n) * Σ(y_actual - y_predicted)²
```

```python
# Implementasi cost function MSE
def mse(y_actual, y_predicted):
    """Menghitung Mean Squared Error"""
    return np.mean((y_actual - y_predicted) ** 2)

# Contoh
y_actual = np.array([100, 150, 200, 250, 300])
y_pred_good = np.array([105, 148, 195, 255, 298])   # Prediksi bagus
y_pred_bad = np.array([80, 180, 150, 300, 250])      # Prediksi buruk

print("=== Cost Function (MSE) ===")
print(f"MSE prediksi bagus : {mse(y_actual, y_pred_good):.2f}")
print(f"MSE prediksi buruk : {mse(y_actual, y_pred_bad):.2f}")
print("\nModel dengan MSE lebih kecil = prediksi lebih akurat!")
```

#### Learning Rate

**Learning rate** (α) menentukan seberapa besar langkah yang diambil pada setiap iterasi:

- **Terlalu besar** — model "melompat-lompat" dan tidak konvergen
- **Terlalu kecil** — model konvergen tapi sangat lambat
- **Tepat** — model konvergen dengan efisien

#### Implementasi Gradient Descent Sederhana

```python
# Gradient Descent untuk regresi linear sederhana: y = w*x + b
# Kita akan menemukan w dan b terbaik

np.random.seed(42)

# Generate data: y = 3x + 5 + noise
X = np.random.rand(50) * 10
y = 3 * X + 5 + np.random.randn(50) * 2

# Inisialisasi parameter random
w = np.random.randn()  # Weight
b = np.random.randn()  # Bias
learning_rate = 0.01
epochs = 100

# Simpan history untuk visualisasi
history = {'epoch': [], 'loss': [], 'w': [], 'b': []}

print("=== Gradient Descent ===")
print(f"Target: y = 3x + 5")
print(f"Initial: w = {w:.4f}, b = {b:.4f}")
print("-" * 50)

for epoch in range(epochs):
    # Forward pass: prediksi
    y_pred = w * X + b

    # Hitung loss (MSE)
    loss = np.mean((y - y_pred) ** 2)

    # Hitung gradien
    dw = -2 * np.mean(X * (y - y_pred))  # dL/dw
    db = -2 * np.mean(y - y_pred)         # dL/db

    # Update parameter
    w = w - learning_rate * dw
    b = b - learning_rate * db

    # Simpan history
    history['epoch'].append(epoch)
    history['loss'].append(loss)
    history['w'].append(w)
    history['b'].append(b)

    # Print setiap 20 epoch
    if epoch % 20 == 0:
        print(f"Epoch {epoch:3d}: Loss = {loss:.4f}, w = {w:.4f}, b = {b:.4f}")

print("-" * 50)
print(f"Final   : w = {w:.4f}, b = {b:.4f}")
print(f"Target  : w = 3.0000, b = 5.0000")
```

#### Visualisasi Gradient Descent

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: Loss curve
axes[0].plot(history['epoch'], history['loss'], 'b-', linewidth=2)
axes[0].set_xlabel('Epoch', fontsize=12)
axes[0].set_ylabel('Loss (MSE)', fontsize=12)
axes[0].set_title('Loss Curve\n(Semakin kecil = semakin baik)', fontsize=13, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Plot 2: Konvergensi w dan b
axes[1].plot(history['epoch'], history['w'], 'r-', label=f'w (final={w:.2f})', linewidth=2)
axes[1].plot(history['epoch'], history['b'], 'g-', label=f'b (final={b:.2f})', linewidth=2)
axes[1].axhline(y=3.0, color='r', linestyle='--', alpha=0.5, label='w target=3.0')
axes[1].axhline(y=5.0, color='g', linestyle='--', alpha=0.5, label='b target=5.0')
axes[1].set_xlabel('Epoch', fontsize=12)
axes[1].set_ylabel('Nilai Parameter', fontsize=12)
axes[1].set_title('Konvergensi Parameter\n(Menuju nilai target)', fontsize=13, fontweight='bold')
axes[1].legend(fontsize=9)
axes[1].grid(True, alpha=0.3)

# Plot 3: Hasil akhir regresi
axes[2].scatter(X, y, alpha=0.6, color='blue', label='Data asli')
X_plot = np.linspace(0, 10, 100)
axes[2].plot(X_plot, w * X_plot + b, 'r-', linewidth=2,
             label=f'Model: y = {w:.2f}x + {b:.2f}')
axes[2].plot(X_plot, 3 * X_plot + 5, 'g--', linewidth=1.5,
             label='Target: y = 3x + 5', alpha=0.7)
axes[2].set_xlabel('X', fontsize=12)
axes[2].set_ylabel('y', fontsize=12)
axes[2].set_title('Hasil Gradient Descent\n(Garis merah = model yang dipelajari)', fontsize=13, fontweight='bold')
axes[2].legend(fontsize=9)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\nGradient descent berhasil 'belajar' mendekati target!")
print("Inilah cara SEMUA model ML belajar dari data.")
```

---

### 6. Mengapa Matematika Penting untuk ML: Rangkuman Koneksi

| Konsep Matematika | Digunakan di Algoritma ML | Penjelasan |
|---|---|---|
| **Dot Product** | Regresi Linear, Neural Networks | Prediksi: `y = w · x + b` |
| **Perkalian Matriks** | Neural Networks, PCA | Forward pass, transformasi data |
| **Eigenvectors** | PCA, Spectral Clustering | Menemukan arah variasi data terbesar |
| **Probabilitas** | Naive Bayes, Bayesian Networks | Klasifikasi berdasarkan probabilitas |
| **Bayes Theorem** | Naive Bayes, Bayesian Optimization | Memperbarui keyakinan berdasarkan data |
| **Gradient** | Semua model ML yang di-train | Arah untuk memperbarui parameter |
| **Cost Function** | Semua model supervised | Mengukur error prediksi |
| **Learning Rate** | Gradient descent | Mengontrol kecepatan pembelajaran |

> **Pesan Penting:** Anda tidak perlu menjadi matematikawan untuk menggunakan ML. Tapi memahami **intuisi** di balik matematikanya akan membantu Anda membuat keputusan yang lebih baik — kapan menggunakan algoritma tertentu, bagaimana men-debug model, dan bagaimana menginterpretasi hasil.

---

## Aktivitas Kelas

### Sesi 1: Teori dan Demonstrasi (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 5 menit | Pembukaan & Review | Review Minggu 2 (preprocessing), preview hari ini |
| 25 menit | Ceramah: Aljabar Linear | Vektor, matriks, dot product, matrix multiplication, cosine similarity |
| 10 menit | Diskusi Singkat | "Di mana Anda menjumpai vektor dan matriks sebelumnya?" |
| 15 menit | Ceramah: Eigenvalues | Eigenvectors, eigenvalues, preview PCA |
| 20 menit | Ceramah: Probabilitas | Probabilitas bersyarat, Bayes theorem, contoh spam detection |
| 20 menit | Ceramah: Gradient Descent | Intuisi, cost function, learning rate, konvergensi |
| 5 menit | Transisi ke Praktikum | Persiapan hands-on |

### Sesi 2: Hands-on Praktikum (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Setup Notebook | Buka Google Colab, import library |
| 25 menit | NumPy Matrix Operations | Latihan vektor, matriks, dot product, cosine similarity |
| 15 menit | Probabilitas dengan Python | Implementasi Bayes theorem |
| 30 menit | Visualisasi Gradient Descent | Implementasi gradient descent sederhana dan visualisasinya |
| 15 menit | Eksplorasi: Learning Rate | Eksperimen dengan berbagai nilai learning rate |
| 5 menit | Wrap-up & Preview | Rangkuman, preview minggu depan |

---

## Hands-on: Eksperimen Learning Rate

### Melihat Efek Learning Rate pada Gradient Descent

```python
# ============================================================
# Minggu 3: Eksperimen Learning Rate
# Mata Kuliah: Kecerdasan Buatan dan Machine Learning
# Universitas Al Azhar Indonesia
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# Generate data
np.random.seed(42)
X = np.random.rand(50) * 10
y = 3 * X + 5 + np.random.randn(50) * 2

def run_gradient_descent(X, y, learning_rate, epochs=100):
    """Menjalankan gradient descent dan mengembalikan history"""
    w, b = np.random.RandomState(42).randn(), np.random.RandomState(42).randn()
    losses = []

    for _ in range(epochs):
        y_pred = w * X + b
        loss = np.mean((y - y_pred) ** 2)
        losses.append(loss)

        dw = -2 * np.mean(X * (y - y_pred))
        db = -2 * np.mean(y - y_pred)

        w -= learning_rate * dw
        b -= learning_rate * db

    return losses, w, b

# Eksperimen dengan berbagai learning rate
learning_rates = [0.0001, 0.001, 0.01, 0.1]
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

for idx, lr in enumerate(learning_rates):
    ax = axes[idx // 2][idx % 2]
    losses, w_final, b_final = run_gradient_descent(X, y, lr, epochs=200)

    ax.plot(losses, linewidth=2)
    ax.set_title(f'Learning Rate = {lr}\n(w={w_final:.2f}, b={b_final:.2f})',
                 fontsize=12, fontweight='bold')
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Loss (MSE)')
    ax.grid(True, alpha=0.3)

    if losses[-1] > 1e6:
        ax.set_ylim(0, losses[0] * 2)
        ax.text(0.5, 0.5, 'DIVERGEN!', transform=ax.transAxes,
                fontsize=20, color='red', ha='center', fontweight='bold')

plt.suptitle('Efek Learning Rate pada Gradient Descent\n'
             '(Target: y = 3x + 5)',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()

print("Kesimpulan:")
print("- LR terlalu kecil (0.0001): konvergen tapi LAMBAT")
print("- LR tepat (0.001-0.01)    : konvergen dengan baik")
print("- LR terlalu besar (0.1)   : bisa DIVERGEN (loss membesar)")
```

### Visualisasi 3D Cost Function (Opsional)

```python
# Visualisasi bagaimana gradient descent mencari minimum
# pada cost function 2D (w dan b)

from mpl_toolkits.mplot3d import Axes3D

# Hitung loss untuk berbagai kombinasi w dan b
w_range = np.linspace(-2, 8, 100)
b_range = np.linspace(-5, 15, 100)
W, B = np.meshgrid(w_range, b_range)

# Cost function surface
Loss_surface = np.zeros_like(W)
for i in range(W.shape[0]):
    for j in range(W.shape[1]):
        y_pred = W[i, j] * X + B[i, j]
        Loss_surface[i, j] = np.mean((y - y_pred) ** 2)

# Plot 3D surface
fig = plt.figure(figsize=(12, 5))

# 3D surface
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(W, B, Loss_surface, cmap='viridis', alpha=0.7)
ax1.set_xlabel('w (weight)')
ax1.set_ylabel('b (bias)')
ax1.set_zlabel('Loss (MSE)')
ax1.set_title('Cost Function Surface', fontweight='bold')

# Contour plot dengan path gradient descent
ax2 = fig.add_subplot(122)
contour = ax2.contour(W, B, Loss_surface, levels=30, cmap='viridis')
ax2.clabel(contour, inline=True, fontsize=8)

# Jalankan gradient descent dan plot path-nya
losses_path, _, _ = run_gradient_descent(X, y, 0.01, epochs=100)
w_init, b_init = np.random.RandomState(42).randn(), np.random.RandomState(42).randn()
w_path, b_path = [w_init], [b_init]
w_curr, b_curr = w_init, b_init
for _ in range(100):
    y_pred = w_curr * X + b_curr
    dw = -2 * np.mean(X * (y - y_pred))
    db = -2 * np.mean(y - y_pred)
    w_curr -= 0.01 * dw
    b_curr -= 0.01 * db
    w_path.append(w_curr)
    b_path.append(b_curr)

ax2.plot(w_path, b_path, 'r.-', markersize=3, linewidth=1, label='GD path')
ax2.plot(w_path[0], b_path[0], 'ro', markersize=10, label='Start')
ax2.plot(w_path[-1], b_path[-1], 'r*', markersize=15, label='End')
ax2.set_xlabel('w (weight)')
ax2.set_ylabel('b (bias)')
ax2.set_title('Contour Plot + Gradient Descent Path', fontweight='bold')
ax2.legend()

plt.tight_layout()
plt.show()

print("Gradient descent 'berjalan' menuruni surface menuju titik minimum!")
```

---

## AI Corner: Menggunakan AI untuk Memahami Konsep Matematika

> **Level: Basic** — Menggunakan AI sebagai tutor matematika untuk ML.

### Cara AI Bisa Membantu Anda

| Skenario | Contoh Prompt ke AI |
|---|---|
| Memahami konsep | *"Jelaskan dot product dengan analogi sederhana. Mengapa dot product penting di ML?"* |
| Visualisasi mental | *"Bantu saya memvisualisasikan apa yang terjadi saat matriks dikalikan. Beri contoh sederhana 2x2."* |
| Bayes theorem | *"Jelaskan Bayes theorem step-by-step dengan contoh deteksi penyakit di Indonesia."* |
| Gradient descent | *"Jelaskan gradient descent seperti saya anak SMA. Gunakan analogi kehidupan nyata."* |
| Verifikasi perhitungan | *"Apakah perhitungan eigenvalue saya benar? [paste perhitungan]"* |

### Tips Penting

1. **Minta analogi** — konsep matematika lebih mudah dipahami dengan analogi kehidupan nyata.
2. **Minta step-by-step** — jangan langsung minta jawaban, minta penjelasan bertahap.
3. **Verifikasi dengan kode** — setelah AI menjelaskan, implementasikan di Python untuk memastikan.
4. **Dokumentasikan** penggunaan AI di AI Usage Log.

### Contoh Prompt Minggu Ini

```
Saya mahasiswa yang belajar machine learning.
Jelaskan dengan bahasa sederhana dan analogi:
1. Mengapa gradient descent bisa menemukan parameter terbaik?
2. Apa yang terjadi jika learning rate terlalu besar?
3. Apa hubungan antara eigenvector dan PCA?
Berikan contoh perhitungan sederhana untuk masing-masing.
```

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai bahan refleksi:

1. **Matematika dan ML:** Sebelum modul ini, apakah Anda mengira ML memerlukan banyak matematika? Setelah melihat koneksinya, apakah pandangan Anda berubah?

2. **Cosine Similarity:** Jika Anda membangun sistem rekomendasi untuk toko online Indonesia, fitur apa saja yang akan Anda gunakan untuk merepresentasikan preferensi pengguna? Bagaimana cosine similarity bisa membantu?

3. **Bayes Theorem di Kehidupan Nyata:** Berikan contoh penggunaan Bayes theorem dalam konteks Indonesia (misalnya di bidang kesehatan, keamanan, atau keuangan).

4. **Learning Rate Analogy:** Bandingkan learning rate dalam gradient descent dengan proses belajar manusia. Apa yang terjadi jika seseorang "belajar terlalu cepat" (learning rate tinggi) atau "terlalu lambat" (learning rate rendah)?

5. **Al-Khawarizmi dan Algoritma:** Bagaimana Anda melihat hubungan antara tradisi ilmiah Islam (Al-Khawarizmi, Al-Jabr) dengan perkembangan machine learning modern?

---

## Tugas Mandiri Minggu 3

1. **NumPy Practice:** Implementasikan fungsi-fungsi berikut menggunakan NumPy (tanpa menggunakan fungsi bawaan np.linalg):
   - Perhitungan dot product manual
   - Perhitungan magnitude vektor manual
   - Perhitungan cosine similarity manual

2. **Bayes Theorem:** Kerjakan soal berikut:
   - Di sebuah kota di Indonesia, 2% penduduk terinfeksi penyakit X. Tes untuk penyakit X memiliki sensitivitas 95% (benar mendeteksi positif jika sakit) dan spesifisitas 90% (benar mendeteksi negatif jika sehat). Jika seseorang dites positif, berapa probabilitas dia benar-benar sakit? Implementasikan dengan Python.

3. **Gradient Descent Exploration:** Modifikasi kode gradient descent di modul ini untuk menemukan parameter dari `y = 2x² + 3x + 1`. Visualisasikan hasilnya. (Hint: Anda perlu menambahkan fitur x² sebagai input.)

---

## Referensi

### Buku Teks

1. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media. Chapter 4: Training Models.
2. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press. Chapter 2: Linear Algebra, Chapter 3: Probability.
3. Deisenroth, M. P., Faisal, A. A., & Ong, C. S. (2020). *Mathematics for Machine Learning*. Cambridge University Press.

### Sumber Online

4. [3Blue1Brown: Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) — Seri video visualisasi aljabar linear yang sangat intuitif.
5. [3Blue1Brown: Neural Networks](https://www.3blue1brown.com/topics/neural-networks) — Visualisasi gradient descent dan backpropagation.
6. [Khan Academy: Linear Algebra](https://www.khanacademy.org/math/linear-algebra) — Kursus gratis aljabar linear.
7. [StatQuest: Gradient Descent](https://www.youtube.com/watch?v=sDv4f4s2SB8) — Penjelasan gradient descent yang mudah dipahami.

### Referensi Sejarah Islam

8. Al-Khawarizmi, M. I. M. (830 M). *Al-Kitab al-Mukhtasar fi Hisab al-Jabr wal-Muqabala*. (Sumber asal kata "algoritma" dan "aljabar")

---

> **Preview Minggu Depan:** Kita akan membahas **Eksplorasi Data dan Feature Engineering** — EDA (*Exploratory Data Analysis*), visualisasi untuk ML, teknik feature engineering, dan data quality checklist. Siapkan dataset Indonesia Anda!

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
