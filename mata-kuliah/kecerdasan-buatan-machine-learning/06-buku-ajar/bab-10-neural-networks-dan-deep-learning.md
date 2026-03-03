# BAB 10: NEURAL NETWORKS DAN DEEP LEARNING DASAR

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| Sub-CPMK 11.1 | Membangun neural network sederhana (MLP) dengan TensorFlow/Keras untuk masalah klasifikasi dan regresi | C3 |
| Sub-CPMK 11.2 | Menjelaskan mekanisme backpropagation, activation functions, dan optimizer dalam neural network serta menerapkan teknik regularisasi untuk meningkatkan generalisasi model | C2-C3 |

**CPMK-5:** Menerapkan arsitektur neural network dan deep learning dasar untuk menyelesaikan masalah klasifikasi dan regresi.

---

## Estimasi Waktu

| Komponen | Durasi |
|----------|--------|
| Membaca materi | 120 menit |
| Praktik kode Python | 90 menit |
| Latihan soal | 60 menit |
| **Total** | **270 menit** |

---

## Prasyarat

- Dasar-dasar aljabar linear: matriks, vektor, dot product (Bab 3)
- Kalkulus dasar: turunan, chain rule (Bab 3)
- Supervised learning: konsep training, evaluasi, overfitting (Bab 5-7)
- Python dan scikit-learn (Bab 2, 5)
- Unsupervised learning dan dimensionality reduction (Bab 8-9)

---

## 10.1 Biological Inspiration: Neuron Biologis ke Neuron Buatan

### 10.1.1 Sistem Saraf Manusia

Otak manusia adalah komputer biologis paling canggih yang diketahui — terdiri dari sekitar **86 miliar neuron** yang terhubung melalui lebih dari **100 triliun sinapsis**. Setiap neuron menerima sinyal elektrokimia dari neuron lain melalui **dendrit**, memproses sinyal tersebut di **soma** (badan sel), dan jika total sinyal melebihi ambang batas (*threshold*), neuron akan "menyala" (*fire*) dan mengirim sinyal melalui **akson** ke neuron berikutnya.

```
Neuron Biologis — Struktur Dasar:

                         Dendrit (penerima sinyal)
                         ┌──────────┐
  sinyal dari        ───→│          │
  neuron lain        ───→│   SOMA   │──→ Akson ──→ Terminal Sinaptik
  (input)            ───→│  (badan  │    (kabel     (pengirim sinyal
                         │   sel)   │    penghantar  ke neuron lain)
                         └──────────┘    sinyal)

  Prinsip kerja:
  1. Dendrit menerima sinyal dari banyak neuron lain
  2. Soma menjumlahkan semua sinyal yang masuk
  3. Jika total sinyal > threshold → neuron "fire" (aktif)
  4. Sinyal diteruskan melalui akson ke neuron berikutnya
  5. Kekuatan koneksi (sinapsis) berubah seiring waktu → BELAJAR
```

> **Wawasan Islami:** Dalam Al-Qur'an, Allah SWT menyebutkan tentang penciptaan manusia dalam bentuk yang paling sempurna (*ahsani taqwim*, QS At-Tin: 4). Kompleksitas otak manusia mencerminkan keagungan ciptaan-Nya. Sebagai ilmuwan Muslim, kita mempelajari neural network bukan untuk menandingi ciptaan Allah, melainkan untuk memahami sebagian kecil dari hikmah penciptaan dan memanfaatkannya untuk kebaikan umat.

### 10.1.2 Dari Neuron Biologis ke Neuron Buatan

**Artificial neural network** (jaringan saraf tiruan / JST) terinspirasi dari neuron biologis, tetapi merupakan penyederhanaan matematis yang sangat signifikan:

| Komponen Biologis | Komponen Buatan | Fungsi |
|-------------------|-----------------|--------|
| Dendrit | Input features ($x_1, x_2, ..., x_n$) | Menerima data/sinyal |
| Sinapsis | Weights ($w_1, w_2, ..., w_n$) | Kekuatan koneksi (dipelajari) |
| Soma | Fungsi penjumlahan ($\sum w_i x_i$) | Menggabungkan sinyal |
| Threshold | Bias ($b$) | Mengatur ambang aktivasi |
| Firing mechanism | Activation function ($f(z)$) | Menentukan apakah neuron aktif |
| Akson | Output ($\hat{y}$) | Mengirim hasil ke layer berikutnya |

```
Perbandingan Visual:

NEURON BIOLOGIS:                    NEURON BUATAN:

  dendrit₁ ──┐                        x₁ ──w₁──┐
  dendrit₂ ──┼→ soma → akson           x₂ ──w₂──┼→ Σ+b → f(z) → ŷ
  dendrit₃ ──┘                        x₃ ──w₃──┘

  sinapsis berubah                    weights di-update
  → learning biologis                 → gradient descent
```

### 10.1.3 Sejarah Singkat Neural Networks

| Tahun | Tonggak | Tokoh |
|-------|---------|-------|
| 1943 | McCulloch-Pitts neuron (model matematika pertama) | McCulloch & Pitts |
| 1958 | Perceptron — neuron yang bisa belajar | Frank Rosenblatt |
| 1969 | "Perceptrons" — menunjukkan keterbatasan perceptron (XOR) | Minsky & Papert |
| 1986 | Backpropagation dipopulerkan | Rumelhart, Hinton, Williams |
| 2006 | Deep Belief Networks — awal era deep learning | Geoffrey Hinton |
| 2012 | AlexNet memenangkan ImageNet — deep learning meledak | Alex Krizhevsky |
| 2017 | Transformer architecture — revolusi NLP | Vaswani et al. |
| 2022+ | Large Language Models (GPT-4, Claude) — AI generatif | OpenAI, Anthropic |

> **Catatan penting:** Neural network artificial **tidak** benar-benar mensimulasikan otak. Analogi biologis berguna untuk membangun intuisi, tetapi realitasnya neural network adalah **model matematika** berbasis optimisasi fungsi.

---

## 10.2 Perceptron dan Multi-Layer Perceptron (MLP)

### 10.2.1 Perceptron: Model Neuron Tunggal

**Perceptron** adalah model neural network paling sederhana — sebuah neuron tunggal yang melakukan klasifikasi biner:

```
    x₁ ──w₁──┐
              │
    x₂ ──w₂──┼──→ z = Σ(wᵢ·xᵢ) + b ──→ f(z) ──→ ŷ (output)
              │
    x₃ ──w₃──┘

Di mana:
  x₁, x₂, x₃  = input (fitur data)
  w₁, w₂, w₃   = weights (bobot, dipelajari dari data)
  b             = bias (dipelajari dari data)
  z             = weighted sum (penjumlahan tertimbang)
  f(z)          = activation function
  ŷ             = prediksi output
```

**Secara matematis:**

$$\hat{y} = f\left(\sum_{i=1}^{n} w_i x_i + b\right) = f(\mathbf{w}^T \mathbf{x} + b)$$

**Perceptron Learning Rule** — mengupdate weights berdasarkan kesalahan:

$$w_i \leftarrow w_i + \alpha \cdot (y - \hat{y}) \cdot x_i$$

di mana $\alpha$ adalah *learning rate*.

```python
import numpy as np
import matplotlib.pyplot as plt

# Implementasi Perceptron dari awal (from scratch)
class PerceptronSederhana:
    """Implementasi perceptron untuk pemahaman konseptual."""

    def __init__(self, learning_rate=0.1, n_iterasi=100):
        self.lr = learning_rate
        self.n_iter = n_iterasi
        self.weights = None
        self.bias = None
        self.errors_per_epoch = []  # Menyimpan jumlah error per epoch

    def fit(self, X, y):
        """Melatih perceptron dengan data X dan label y."""
        n_sampel, n_fitur = X.shape
        self.weights = np.zeros(n_fitur)
        self.bias = 0

        for epoch in range(self.n_iter):
            total_error = 0
            for xi, yi in zip(X, y):
                # Forward pass: hitung prediksi
                z = np.dot(xi, self.weights) + self.bias
                y_pred = 1 if z >= 0 else 0

                # Hitung error dan update weights
                error = yi - y_pred
                self.weights += self.lr * error * xi
                self.bias += self.lr * error
                total_error += abs(error)

            self.errors_per_epoch.append(total_error)
            if total_error == 0:
                print(f"Konvergen di epoch {epoch + 1}")
                break

    def predict(self, X):
        """Prediksi label untuk data baru."""
        z = np.dot(X, self.weights) + self.bias
        return np.where(z >= 0, 1, 0)

# Contoh 1: AND gate (linearly separable → berhasil)
X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])

p_and = PerceptronSederhana(learning_rate=0.1, n_iterasi=20)
p_and.fit(X_and, y_and)

print("=== PERCEPTRON UNTUK AND GATE ===")
print(f"Weights: {p_and.weights}, Bias: {p_and.bias}")
for xi, yi in zip(X_and, y_and):
    pred = p_and.predict(xi.reshape(1, -1))[0]
    print(f"  Input: {xi} → Prediksi: {pred} (Target: {yi}) {'OK' if pred == yi else 'SALAH'}")

# Contoh 2: XOR gate (TIDAK linearly separable → GAGAL)
X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([0, 1, 1, 0])

p_xor = PerceptronSederhana(learning_rate=0.1, n_iterasi=100)
p_xor.fit(X_xor, y_xor)

print("\n=== PERCEPTRON UNTUK XOR GATE (GAGAL!) ===")
for xi, yi in zip(X_xor, y_xor):
    pred = p_xor.predict(xi.reshape(1, -1))[0]
    status = "OK" if pred == yi else "SALAH"
    print(f"  Input: {xi} → Prediksi: {pred} (Target: {yi}) [{status}]")
print("Perceptron tidak bisa menyelesaikan XOR karena tidak linearly separable!")
```

### 10.2.2 Multi-Layer Perceptron (MLP)

Keterbatasan perceptron (hanya bisa menyelesaikan masalah *linearly separable*) diatasi oleh **Multi-Layer Perceptron (MLP)** yang menambahkan satu atau lebih **hidden layer** antara input dan output:

```
Arsitektur MLP — 3 Hidden Layers:

Input Layer     Hidden Layer 1    Hidden Layer 2    Output Layer

  x₁ ─────────── h₁ ─────────── h₄ ──────────── ŷ₁
          ╲   ╱        ╲   ╱        ╲   ╱
  x₂ ─────────── h₂ ─────────── h₅ ──────────── ŷ₂
          ╱   ╲        ╱   ╲        ╱   ╲
  x₃ ─────────── h₃ ─────────── h₆

 (3 neuron)    (3 neuron)     (3 neuron)     (2 neuron)

Setiap garis = 1 weight + 1 bias per neuron
Total koneksi = 3×3 + 3×3 + 3×2 = 27 weights + 8 biases = 35 parameter
```

**Terminologi penting:**

| Istilah | Definisi |
|---------|----------|
| **Input layer** | Menerima fitur data — bukan "layer" sesungguhnya (tidak ada komputasi) |
| **Hidden layer** | Layer antara input dan output — melakukan transformasi non-linear |
| **Output layer** | Menghasilkan prediksi akhir |
| **Deep learning** | Neural network dengan **2 atau lebih hidden layers** |
| **Width** | Jumlah neuron dalam satu layer |
| **Depth** | Jumlah hidden layers |

### 10.2.3 Universal Approximation Theorem

> **Teorema (Cybenko, 1989; Hornik, 1991):** Neural network dengan **satu hidden layer** dan **jumlah neuron yang cukup** dapat mengaproksimasi **fungsi kontinu apapun** dengan akurasi sembarang.

**Implikasi praktis:**
- Secara teori, satu hidden layer sudah cukup untuk memodelkan pola apapun
- Tetapi **dalam praktik**, deep networks (banyak layer, lebih sedikit neuron per layer) lebih **efisien** daripada wide networks (satu layer, sangat banyak neuron)
- Deep learning menangkap **hirarki fitur**: layer awal menangkap pola sederhana, layer dalam menangkap pola kompleks

```
Contoh hierarki fitur pada pengenalan wajah:

Layer 1: Tepi dan garis sederhana      ── / | \ ──
Layer 2: Bentuk geometris dasar        mata, hidung, mulut
Layer 3: Bagian wajah                  setengah wajah
Layer 4: Wajah lengkap                 identifikasi orang
```

---

## 10.3 Fungsi Aktivasi (Sigmoid, ReLU, Softmax)

### 10.3.1 Mengapa Perlu Activation Function?

Tanpa activation function, MLP hanya melakukan **transformasi linear bertingkat** — yang setara dengan satu transformasi linear tunggal. Activation function menambahkan **non-linearitas** yang memungkinkan neural network mempelajari pola kompleks.

```
Tanpa activation:
  Layer 1: z₁ = W₁·x + b₁
  Layer 2: z₂ = W₂·z₁ + b₂ = W₂·(W₁·x + b₁) + b₂ = (W₂W₁)·x + (W₂b₁ + b₂)
  → Setara dengan satu layer linear! (sia-sia menambah layer)

Dengan activation:
  Layer 1: a₁ = f(W₁·x + b₁)    ← non-linear!
  Layer 2: a₂ = f(W₂·a₁ + b₂)   ← non-linear lagi!
  → Network bisa mempelajari fungsi non-linear yang kompleks
```

### 10.3.2 Jenis-jenis Activation Function

| Activation | Formula | Range | Digunakan Di | Kelebihan | Kekurangan |
|-----------|---------|-------|-------------|-----------|------------|
| **Sigmoid** | $\sigma(z) = \frac{1}{1+e^{-z}}$ | (0, 1) | Output klasifikasi biner | Output interpretable sebagai probabilitas | Vanishing gradient |
| **Tanh** | $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$ | (-1, 1) | Hidden layer (jarang) | Zero-centered | Vanishing gradient |
| **ReLU** | $\max(0, z)$ | [0, +inf) | Hidden layer (default) | Komputasi cepat, mitigasi vanishing gradient | "Dead neuron" problem |
| **Leaky ReLU** | $\max(0.01z, z)$ | (-inf, +inf) | Hidden layer (alternatif) | Mengatasi dead neuron | Sedikit lebih lambat |
| **Softmax** | $\frac{e^{z_i}}{\sum_j e^{z_j}}$ | (0, 1), sum=1 | Output multi-kelas | Menghasilkan distribusi probabilitas | Hanya untuk output layer |

```python
import numpy as np
import matplotlib.pyplot as plt

# Visualisasi semua activation function
z = np.linspace(-5, 5, 200)

# Definisi activation functions
aktivasi = {
    'Sigmoid': 1 / (1 + np.exp(-z)),
    'Tanh': np.tanh(z),
    'ReLU': np.maximum(0, z),
    'Leaky ReLU (α=0.01)': np.where(z > 0, z, 0.01 * z)
}

# Turunan (derivative) masing-masing
turunan = {
    'Sigmoid': aktivasi['Sigmoid'] * (1 - aktivasi['Sigmoid']),
    'Tanh': 1 - aktivasi['Tanh']**2,
    'ReLU': np.where(z > 0, 1.0, 0.0),
    'Leaky ReLU (α=0.01)': np.where(z > 0, 1.0, 0.01)
}

# Plot activation functions dan turunannya
fig, axes = plt.subplots(2, 4, figsize=(16, 8))

for idx, (nama, nilai) in enumerate(aktivasi.items()):
    # Baris 1: Activation function
    axes[0, idx].plot(z, nilai, 'b-', linewidth=2)
    axes[0, idx].axhline(y=0, color='gray', linewidth=0.5)
    axes[0, idx].axvline(x=0, color='gray', linewidth=0.5)
    axes[0, idx].set_title(f'{nama}', fontsize=11)
    axes[0, idx].set_xlabel('z')
    axes[0, idx].set_ylabel('f(z)')
    axes[0, idx].grid(True, alpha=0.3)

    # Baris 2: Derivative
    axes[1, idx].plot(z, list(turunan.values())[idx], 'r-', linewidth=2)
    axes[1, idx].axhline(y=0, color='gray', linewidth=0.5)
    axes[1, idx].axvline(x=0, color='gray', linewidth=0.5)
    axes[1, idx].set_title(f"Turunan {nama}", fontsize=11)
    axes[1, idx].set_xlabel('z')
    axes[1, idx].set_ylabel("f'(z)")
    axes[1, idx].grid(True, alpha=0.3)

plt.suptitle('Activation Functions dan Turunannya', fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig('activation_functions_lengkap.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 10.3.3 Panduan Pemilihan Activation Function

```
Tipe Masalah                    Output Layer         Hidden Layer
───────────────────────────────────────────────────────────────────
Regresi (nilai kontinu)         Linear (none)        ReLU
Klasifikasi biner (2 kelas)    Sigmoid              ReLU
Klasifikasi multi-kelas         Softmax              ReLU
```

**Mengapa ReLU paling populer untuk hidden layers?**
1. **Komputasi cepat** — hanya operasi max(0, z), tanpa eksponensial
2. **Mengurangi vanishing gradient** — turunan = 1 untuk z > 0
3. **Sparse activation** — banyak output bernilai 0, efisien secara komputasi
4. **Konvergensi cepat** — training lebih cepat dibanding sigmoid/tanh

### 10.3.4 Contoh Softmax untuk Klasifikasi Multi-kelas

```python
import numpy as np

def softmax(z):
    """Hitung softmax secara numerik stabil."""
    z_shifted = z - np.max(z)  # Menghindari overflow eksponensial
    exp_z = np.exp(z_shifted)
    return exp_z / exp_z.sum()

# Contoh: klasifikasi 4 kelas (Kucing, Anjing, Burung, Ikan)
z_output = np.array([2.0, 1.0, 0.1, -1.0])
probabilitas = softmax(z_output)

kelas = ['Kucing', 'Anjing', 'Burung', 'Ikan']
print("=== OUTPUT SOFTMAX ===")
for k, p in zip(kelas, probabilitas):
    print(f"  {k}: {p:.4f} ({p*100:.1f}%)")
print(f"  Total: {probabilitas.sum():.4f}")  # Harus = 1.0
print(f"  Prediksi: {kelas[np.argmax(probabilitas)]}")
```

---

## 10.4 Forward Propagation dan Backpropagation

### 10.4.1 Forward Propagation

**Forward propagation** (propagasi maju) adalah proses menghitung output dari input melalui seluruh layer neural network:

```
Forward Propagation — Langkah demi Langkah:

Input x → [Layer 1] → a₁ → [Layer 2] → a₂ → [Output] → ŷ → Loss(y, ŷ)

Layer k:
  1. Hitung weighted sum: z_k = W_k · a_{k-1} + b_k
  2. Terapkan activation: a_k = f(z_k)
  3. Lanjutkan ke layer berikutnya
```

```python
import numpy as np

# Demonstrasi forward propagation manual
np.random.seed(42)

# Arsitektur: 3 input → 4 hidden → 2 output
# Data input (1 sampel dengan 3 fitur)
X = np.array([0.5, 0.3, 0.8])

# Layer 1: Input(3) → Hidden(4)
W1 = np.random.randn(3, 4) * 0.5  # Weight matrix (3x4)
b1 = np.zeros(4)                    # Bias vector (4,)
z1 = X @ W1 + b1                    # Weighted sum
a1 = np.maximum(0, z1)              # ReLU activation

print("=== FORWARD PROPAGATION MANUAL ===")
print(f"Input X: {X}")
print(f"\n--- Layer 1 (Hidden) ---")
print(f"W1 shape: {W1.shape}, b1 shape: {b1.shape}")
print(f"z1 (sebelum aktivasi): {z1.round(4)}")
print(f"a1 (setelah ReLU):     {a1.round(4)}")

# Layer 2: Hidden(4) → Output(2)
W2 = np.random.randn(4, 2) * 0.5  # Weight matrix (4x2)
b2 = np.zeros(2)                    # Bias vector (2,)
z2 = a1 @ W2 + b2                   # Weighted sum

# Softmax untuk klasifikasi 2 kelas
exp_z2 = np.exp(z2 - np.max(z2))
a2 = exp_z2 / exp_z2.sum()          # Output probabilities

print(f"\n--- Layer 2 (Output) ---")
print(f"W2 shape: {W2.shape}, b2 shape: {b2.shape}")
print(f"z2 (sebelum aktivasi): {z2.round(4)}")
print(f"a2 (setelah softmax):  {a2.round(4)}")
print(f"Prediksi kelas: {np.argmax(a2)}")
```

### 10.4.2 Backpropagation: Intuisi

**Backpropagation** (propagasi mundur) adalah algoritma untuk menghitung **gradien** (turunan parsial) dari loss function terhadap setiap parameter (weight dan bias) di network. Gradien ini kemudian digunakan oleh optimizer untuk mengupdate parameter.

> **Analogi:** Bayangkan Anda bermain panahan dan anak panah meleset 10 cm ke kanan dan 5 cm ke atas dari target. Backpropagation menjawab: "Berapa banyak saya harus mengubah sudut busur dan kekuatan tarikan agar anak panah lebih dekat ke target?" — ia menghitung seberapa besar setiap parameter berkontribusi terhadap kesalahan.

```
Alur Backpropagation:

FORWARD PASS (maju):
  Input → [W₁,b₁] → Hidden → [W₂,b₂] → Output → Loss
   x    ────────→     a₁   ────────→     ŷ     ──→  L

BACKWARD PASS (mundur):
  Input ← [∂L/∂W₁] ← Hidden ← [∂L/∂W₂] ← Output ← ∂L/∂ŷ
           gradien               gradien             gradien

UPDATE PARAMETER:
  W₁_baru = W₁_lama − learning_rate × ∂L/∂W₁
  W₂_baru = W₂_lama − learning_rate × ∂L/∂W₂
  b₁_baru = b₁_lama − learning_rate × ∂L/∂b₁
  b₂_baru = b₂_lama − learning_rate × ∂L/∂b₂
```

### 10.4.3 Chain Rule dalam Backpropagation

**Chain rule** (aturan rantai) adalah fondasi matematis backpropagation — memungkinkan kita menghitung gradien melalui komposisi fungsi:

$$\frac{\partial L}{\partial w_1} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z_2} \cdot \frac{\partial z_2}{\partial a_1} \cdot \frac{\partial a_1}{\partial z_1} \cdot \frac{\partial z_1}{\partial w_1}$$

Setiap faktor dalam rantai mudah dihitung secara individual — backpropagation menggabungkan semuanya secara efisien.

### 10.4.4 Vanishing dan Exploding Gradients

| Masalah | Penyebab | Dampak | Solusi |
|---------|----------|--------|--------|
| **Vanishing gradient** | Sigmoid/tanh: turunan maksimal 0.25 | Gradien mendekati 0 di layer awal — layer awal tidak belajar | ReLU, Batch Normalization, skip connections |
| **Exploding gradient** | Weights besar, gradient dikalikan berulang | Gradien membesar tak terkendali — training diverge | Gradient clipping, proper initialization |

```python
import numpy as np

# Demonstrasi vanishing gradient dengan sigmoid vs ReLU
print("=== DAMPAK VANISHING GRADIENT ===")
print("\nSigmoid: turunan maksimal = 0.25")
for n_layer in [3, 5, 10, 20]:
    # Gradien yang sampai ke layer pertama (asumsi turunan maksimal)
    gradien_sigmoid = 0.25 ** n_layer
    gradien_relu = 1.0 ** n_layer  # ReLU: turunan = 1 untuk z > 0
    print(f"  {n_layer} layers: sigmoid gradient = {gradien_sigmoid:.2e}, "
          f"ReLU gradient = {gradien_relu:.2e}")

print("\nKesimpulan: Dengan 10 layer sigmoid, gradien tinggal ~0.000001!")
print("Ini menyebabkan layer awal hampir tidak belajar sama sekali.")
print("Solusi: gunakan ReLU sebagai activation function di hidden layers.")
```

---

## 10.5 Training Neural Network: Loss Function, Optimizer, Epochs

### 10.5.1 Loss Function (Fungsi Rugi)

Loss function mengukur **seberapa buruk** prediksi model dibandingkan target. Tujuan training: **meminimalkan loss**.

| Loss Function | Formula | Digunakan Untuk | Keras Name |
|---------------|---------|-----------------|------------|
| **MSE** | $\frac{1}{n}\sum(y_i - \hat{y}_i)^2$ | Regresi | `'mse'` |
| **MAE** | $\frac{1}{n}\sum|y_i - \hat{y}_i|$ | Regresi (robust terhadap outlier) | `'mae'` |
| **Binary Cross-Entropy** | $-\frac{1}{n}\sum[y\log\hat{y} + (1-y)\log(1-\hat{y})]$ | Klasifikasi biner | `'binary_crossentropy'` |
| **Categorical Cross-Entropy** | $-\frac{1}{n}\sum\sum y_{ij}\log\hat{y}_{ij}$ | Multi-kelas (one-hot) | `'categorical_crossentropy'` |
| **Sparse Categorical CE** | Sama, tapi label berupa integer | Multi-kelas (integer) | `'sparse_categorical_crossentropy'` |

```python
import numpy as np

# Contoh perhitungan loss secara manual
print("=== CONTOH PERHITUNGAN LOSS ===")

# Binary Cross-Entropy
y_true_bin = np.array([1, 0, 1, 1, 0])
y_pred_bin = np.array([0.9, 0.1, 0.8, 0.7, 0.3])
bce = -np.mean(y_true_bin * np.log(y_pred_bin) +
               (1 - y_true_bin) * np.log(1 - y_pred_bin))
print(f"Binary Cross-Entropy: {bce:.4f}")

# MSE untuk regresi (contoh: prediksi harga rumah Jakarta dalam miliar Rp)
harga_aktual = np.array([1.5, 2.8, 3.2, 5.0, 7.5])   # Miliar Rp
harga_prediksi = np.array([1.4, 3.0, 3.1, 4.8, 7.8])  # Prediksi model
mse = np.mean((harga_aktual - harga_prediksi) ** 2)
print(f"MSE (harga rumah): {mse:.4f} miliar Rp²")
print(f"RMSE: {np.sqrt(mse):.4f} miliar Rp")
```

### 10.5.2 Optimizer

Optimizer menentukan **bagaimana weights di-update** berdasarkan gradien yang dihitung oleh backpropagation.

| Optimizer | Cara Kerja | Kelebihan | Kekurangan |
|-----------|-----------|-----------|------------|
| **SGD** | Update per mini-batch, fixed learning rate | Sederhana, generalisasi baik | Konvergensi lambat, sensitif terhadap lr |
| **SGD + Momentum** | Menambahkan "inersia" dari update sebelumnya | Lebih cepat dari SGD biasa | Perlu tuning momentum |
| **RMSprop** | Adaptive lr berdasarkan running average gradien² | Baik untuk landscape bergelombang | Kurang populer dari Adam |
| **Adam** | Menggabungkan momentum + adaptive lr | Cepat konvergen, robust, minim tuning | Bisa overfit, memori lebih besar |

```
Perbandingan cara kerja:

SGD:       w = w − lr × ∂L/∂w                    (langsung turun)
Momentum:  v = β·v + ∂L/∂w; w = w − lr × v        (ada inersia)
Adam:      m = β₁·m + (1−β₁)·g                    (first moment)
           v = β₂·v + (1−β₂)·g²                   (second moment)
           w = w − lr × m̂ / (√v̂ + ε)              (adaptive)
```

**Panduan praktis:**
- **Mulai dengan Adam** (learning rate = 0.001) — biasanya cukup baik
- Jika overfit → coba **SGD + Momentum** (lr = 0.01, momentum = 0.9)
- Jika model tidak konvergen → turunkan learning rate

### 10.5.3 Epoch, Batch, dan Iteration

| Istilah | Definisi | Contoh (1000 data, batch_size=100) |
|---------|----------|-------------------------------------|
| **Epoch** | Satu kali seluruh training data diproses | 1 epoch |
| **Batch** | Subset data yang diproses sekaligus | 100 data per batch |
| **Iteration** | Satu kali update weights (= 1 batch diproses) | 10 iterations per epoch |

```
Training process dengan 1000 data, batch_size=100:

Epoch 1:  [batch 1] → update → [batch 2] → update → ... → [batch 10] → update
          ←──────────── 10 iterations = 1 epoch ────────────→

Epoch 2:  [batch 1] → update → [batch 2] → update → ... → [batch 10] → update

... (total 50 epochs = 500 iterations)
```

```python
# Cheat sheet kompilasi Keras
"""
Masalah                 Loss                          Output Activation    Metrics
─────────────────────────────────────────────────────────────────────────────────────
Regresi                 'mse' atau 'mae'              'linear' (none)      'mae', 'mse'
Klasifikasi biner       'binary_crossentropy'         'sigmoid'            'accuracy'
Multi-kelas (one-hot)   'categorical_crossentropy'    'softmax'            'accuracy'
Multi-kelas (integer)   'sparse_categorical_crossentropy' 'softmax'       'accuracy'
"""
```

---

## 10.6 Implementasi dengan TensorFlow/Keras (Google Colab)

### 10.6.1 Instalasi dan Setup

```python
# Di Google Colab, TensorFlow sudah terinstall
# Jika belum: !pip install tensorflow

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt

print(f"TensorFlow versi: {tf.__version__}")
print(f"GPU tersedia: {tf.config.list_physical_devices('GPU')}")
```

### 10.6.2 Membangun Model dengan Sequential API

```python
from tensorflow import keras
from tensorflow.keras import layers

# Membangun model MLP dengan Sequential API
model = keras.Sequential([
    # Hidden layer 1: 64 neuron, ReLU activation
    layers.Dense(64, activation='relu', input_shape=(10,),
                 name='hidden_1'),

    # Hidden layer 2: 32 neuron, ReLU activation
    layers.Dense(32, activation='relu', name='hidden_2'),

    # Output layer: 1 neuron, Sigmoid untuk klasifikasi biner
    layers.Dense(1, activation='sigmoid', name='output')
])

# Tampilkan ringkasan arsitektur
model.summary()

# Penjelasan output:
# Layer (type)               Output Shape     Param #
# hidden_1 (Dense)           (None, 64)       704      ← (10+1)×64 = 704
# hidden_2 (Dense)           (None, 32)       2080     ← (64+1)×32 = 2080
# output (Dense)             (None, 1)        33       ← (32+1)×1 = 33
# Total params: 2,817
```

### 10.6.3 Contoh Lengkap: Klasifikasi Kanker Payudara

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# 1. Muat dan persiapkan data
cancer = load_breast_cancer()
X = cancer.data   # 569 sampel, 30 fitur
y = cancer.target  # 0 = malignant, 1 = benign

# Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Standardisasi fitur (WAJIB untuk neural network!)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Gunakan parameter dari training

print(f"Training: {X_train_scaled.shape}, Testing: {X_test_scaled.shape}")

# 2. Bangun arsitektur model
model_cancer = keras.Sequential([
    layers.Dense(64, activation='relu',
                 input_shape=(X_train_scaled.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(16, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Klasifikasi biner
])

# 3. Kompilasi model
model_cancer.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model_cancer.summary()

# 4. Training model
history = model_cancer.fit(
    X_train_scaled, y_train,
    epochs=100,              # Maksimum 100 epoch
    batch_size=32,           # 32 sampel per batch
    validation_split=0.2,    # 20% training data untuk validasi
    verbose=1
)

# 5. Evaluasi pada test set
test_loss, test_acc = model_cancer.evaluate(X_test_scaled, y_test, verbose=0)
print(f"\n=== HASIL EVALUASI ===")
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_acc:.4f} ({test_acc*100:.1f}%)")
```

### 10.6.4 Visualisasi Training History

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot Loss
axes[0].plot(history.history['loss'], label='Training Loss', linewidth=2)
axes[0].plot(history.history['val_loss'], label='Validation Loss', linewidth=2)
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Loss')
axes[0].set_title('Training vs Validation Loss')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Plot Accuracy
axes[1].plot(history.history['accuracy'], label='Training Accuracy', linewidth=2)
axes[1].plot(history.history['val_accuracy'], label='Validation Accuracy', linewidth=2)
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Accuracy')
axes[1].set_title('Training vs Validation Accuracy')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('training_history.png', dpi=150, bbox_inches='tight')
plt.show()

# Interpretasi:
# - Jika val_loss naik sementara train_loss turun → OVERFITTING
# - Jika keduanya masih menurun → masih bisa ditambah epoch (UNDERFITTING)
# - Jika keduanya stabil → model sudah konvergen
```

### 10.6.5 Contoh Regresi: Prediksi Harga Rumah Jakarta

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Simulasi dataset harga rumah Jakarta
np.random.seed(42)
n = 1000

# Fitur-fitur rumah
data_rumah = pd.DataFrame({
    'luas_tanah_m2': np.random.uniform(60, 500, n),
    'luas_bangunan_m2': np.random.uniform(40, 400, n),
    'jumlah_kamar': np.random.randint(1, 8, n),
    'jumlah_kamar_mandi': np.random.randint(1, 5, n),
    'jarak_ke_pusat_km': np.random.uniform(1, 40, n),
    'tahun_dibangun': np.random.randint(1980, 2024, n),
    'ada_garasi': np.random.choice([0, 1], n, p=[0.3, 0.7]),
})

# Harga ditentukan oleh kombinasi fitur (dengan noise)
data_rumah['harga_miliar'] = (
    0.008 * data_rumah['luas_tanah_m2'] +
    0.005 * data_rumah['luas_bangunan_m2'] +
    0.2 * data_rumah['jumlah_kamar'] +
    0.15 * data_rumah['jumlah_kamar_mandi'] -
    0.05 * data_rumah['jarak_ke_pusat_km'] +
    0.01 * (data_rumah['tahun_dibangun'] - 1980) +
    0.3 * data_rumah['ada_garasi'] +
    np.random.normal(0, 0.5, n)  # Noise
).clip(0.5)  # Minimum 500 juta

print("=== DATASET HARGA RUMAH JAKARTA ===")
print(f"Jumlah data: {len(data_rumah)}")
print(f"\n{data_rumah.describe().round(2)}")

# Persiapan data
X = data_rumah.drop('harga_miliar', axis=1).values
y = data_rumah['harga_miliar'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Bangun model regresi
model_rumah = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='linear')  # Output linear untuk regresi!
])

model_rumah.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='mse',
    metrics=['mae']
)

# Training dengan early stopping
early_stop = keras.callbacks.EarlyStopping(
    monitor='val_loss', patience=15, restore_best_weights=True
)

history_rumah = model_rumah.fit(
    X_train_scaled, y_train,
    epochs=200,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=0
)

print(f"Training selesai di epoch {len(history_rumah.history['loss'])}")

# Evaluasi
from sklearn.metrics import mean_absolute_error, r2_score

y_pred = model_rumah.predict(X_test_scaled, verbose=0).flatten()
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n=== EVALUASI MODEL HARGA RUMAH ===")
print(f"MAE: Rp {mae:.2f} miliar (error rata-rata {mae*1000:.0f} juta)")
print(f"R² Score: {r2:.4f}")

# Visualisasi prediksi vs aktual
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(y_test, y_pred, alpha=0.5, s=30, edgecolors='w')
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
        'r--', linewidth=2, label='Prediksi Sempurna')
ax.set_xlabel('Harga Aktual (Miliar Rp)', fontsize=12)
ax.set_ylabel('Harga Prediksi (Miliar Rp)', fontsize=12)
ax.set_title(f'Prediksi Harga Rumah Jakarta\nMAE={mae:.3f}M, R²={r2:.4f}',
             fontsize=14)
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('prediksi_harga_rumah.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## 10.7 Regularisasi: Dropout, Early Stopping, Batch Normalization

### 10.7.1 Mengapa Regularisasi Diperlukan?

Neural network memiliki **banyak parameter** yang membuat mereka sangat rentan terhadap **overfitting** — model terlalu menghafal training data dan gagal melakukan generalisasi pada data baru.

```
Underfitting          Just Right           Overfitting
(model terlalu       (model seimbang)     (model terlalu
sederhana)                                kompleks)

  |  * *  *           |  * *  *           |  * *  *
  | *   *  *          | *   *  *          | *   *  *
  |  *  *  *          |  *  *  *          |  *  *  *
  |__________         |___/\___/___       |__/\/\/\__
   garis lurus        kurva halus          kurva zig-zag

  Train error: tinggi  Train error: rendah  Train error: SANGAT rendah
  Val error: tinggi    Val error: rendah    Val error: TINGGI ← masalah!
```

### 10.7.2 Dropout

**Dropout** secara acak "mematikan" sebagian neuron saat training (menjadikan outputnya 0), memaksa network untuk tidak bergantung pada neuron tertentu:

```
Training (Dropout=0.3):              Prediksi (tanpa dropout):

  x₁ ── h₁ ── h₄ ── ŷ              x₁ ── h₁ ── h₄ ── ŷ
        ╲ X ╱   ╲╱                         ╲╱     ╲╱
  x₂ ── X  ── h₅ ── ŷ              x₂ ── h₂ ── h₅ ── ŷ
        ╱╲   ╱ X                           ╱╲     ╱╲
  x₃ ── h₃ ── X  ── ŷ              x₃ ── h₃ ── h₆ ── ŷ

  X = neuron dimatikan (30%)         Semua neuron aktif
  Setiap batch, neuron yang           (output di-scale otomatis)
  dimatikan berbeda-beda
```

```python
from tensorflow import keras
from tensorflow.keras import layers

# Model dengan Dropout
model_dropout = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(30,)),
    layers.Dropout(0.3),   # 30% neuron dimatikan saat training
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),   # 20% neuron dimatikan
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model_dropout.compile(optimizer='adam', loss='binary_crossentropy',
                      metrics=['accuracy'])
print("Model dengan Dropout:")
model_dropout.summary()
```

### 10.7.3 Early Stopping

**Early stopping** menghentikan training ketika validation loss berhenti membaik — mencegah model terus menghafal training data:

```
Loss
  │
  │╲         Training Loss
  │ ╲ ╲
  │  ╲  ╲
  │   ╲   ╲─────────────── (terus turun)
  │    ╲
  │     ╲  ╱──────────── Validation Loss (mulai naik = overfit!)
  │      ╲╱
  │       * ← TITIK OPTIMAL (early stopping berhenti di sini)
  │
  └────────────────────── Epoch
           ↑
      Best epoch
```

```python
from tensorflow import keras

# Callback Early Stopping
early_stop = keras.callbacks.EarlyStopping(
    monitor='val_loss',          # Pantau validation loss
    patience=10,                 # Tunggu 10 epoch tanpa improvement
    restore_best_weights=True,   # Kembalikan ke weights terbaik
    min_delta=0.001              # Improvement minimum dianggap bermakna
)

# Callback ReduceLROnPlateau — kurangi learning rate jika val_loss stagnan
reduce_lr = keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,       # Kurangi lr menjadi setengahnya
    patience=5,       # Tunggu 5 epoch sebelum mengurangi
    min_lr=1e-6       # Learning rate minimum
)

# Gunakan callbacks saat training
history = model_dropout.fit(
    X_train_scaled, y_train,
    epochs=200,             # Set tinggi — early stopping akan hentikan
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop, reduce_lr],
    verbose=0
)

print(f"Training berhenti di epoch {len(history.history['loss'])}")
```

### 10.7.4 Batch Normalization

**Batch Normalization** menormalisasi output setiap layer sehingga memiliki mean mendekati 0 dan variance mendekati 1. Ini menstabilkan dan mempercepat training.

```python
from tensorflow import keras
from tensorflow.keras import layers

# Model dengan Batch Normalization
model_bn = keras.Sequential([
    # Pola: Dense → BatchNorm → Activation → Dropout
    layers.Dense(128, input_shape=(30,)),
    layers.BatchNormalization(),
    layers.Activation('relu'),
    layers.Dropout(0.3),

    layers.Dense(64),
    layers.BatchNormalization(),
    layers.Activation('relu'),
    layers.Dropout(0.2),

    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model_bn.compile(optimizer='adam', loss='binary_crossentropy',
                 metrics=['accuracy'])
print("Model dengan Batch Normalization:")
model_bn.summary()
```

### 10.7.5 Ringkasan Teknik Regularisasi

| Teknik | Cara Kerja | Kapan Digunakan | Hyperparameter |
|--------|-----------|-----------------|----------------|
| **Dropout** | Matikan neuron secara acak saat training | Hampir selalu | rate: 0.1-0.5 |
| **Early Stopping** | Hentikan training saat val_loss naik | Selalu | patience: 5-20 |
| **Batch Normalization** | Normalisasi output setiap layer | Network deep (>3 layers) | — |
| **L1/L2 Regularization** | Penalti pada weights besar | Jika masih overfit | lambda: 1e-4 s/d 1e-2 |
| **Data Augmentation** | Perbanyak variasi training data | Dataset kecil | — |

**Best practice — Kombinasi regularisasi yang direkomendasikan:**

```python
from tensorflow import keras
from tensorflow.keras import layers

# Template model "production-ready" dengan semua regularisasi
def buat_model_robust(input_dim, n_kelas=2):
    """Membuat model neural network dengan regularisasi lengkap."""
    model = keras.Sequential([
        # Layer 1
        layers.Dense(128, kernel_regularizer=keras.regularizers.l2(1e-4),
                     input_shape=(input_dim,)),
        layers.BatchNormalization(),
        layers.Activation('relu'),
        layers.Dropout(0.3),

        # Layer 2
        layers.Dense(64, kernel_regularizer=keras.regularizers.l2(1e-4)),
        layers.BatchNormalization(),
        layers.Activation('relu'),
        layers.Dropout(0.2),

        # Layer 3
        layers.Dense(32, activation='relu'),

        # Output
        layers.Dense(1 if n_kelas == 2 else n_kelas,
                     activation='sigmoid' if n_kelas == 2 else 'softmax')
    ])
    return model

# Contoh penggunaan
model_robust = buat_model_robust(input_dim=30, n_kelas=2)
model_robust.compile(optimizer='adam', loss='binary_crossentropy',
                     metrics=['accuracy'])
model_robust.summary()
```

---

## 10.8 Studi Kasus: Klasifikasi MNIST dan Dataset Indonesia

### 10.8.1 Klasifikasi Digit MNIST

MNIST adalah dataset benchmark klasik berisi 70.000 gambar digit tulisan tangan (0-9), berukuran 28x28 piksel.

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt

# 1. Muat dataset MNIST
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

print(f"Training set: {X_train.shape}")     # (60000, 28, 28)
print(f"Test set: {X_test.shape}")          # (10000, 28, 28)
print(f"Label unik: {np.unique(y_train)}")  # [0, 1, 2, ..., 9]

# Visualisasi beberapa contoh
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flatten()):
    ax.imshow(X_train[i], cmap='gray')
    ax.set_title(f'Label: {y_train[i]}', fontsize=11)
    ax.axis('off')
plt.suptitle('Contoh Data MNIST — Digit Tulisan Tangan', fontsize=14)
plt.tight_layout()
plt.savefig('mnist_samples.png', dpi=150, bbox_inches='tight')
plt.show()
```

```python
# 2. Preprocessing
# Normalisasi pixel: 0-255 → 0.0-1.0
X_train_norm = X_train.astype('float32') / 255.0
X_test_norm = X_test.astype('float32') / 255.0

# Flatten: 28x28 → 784 (untuk MLP/Dense layers)
X_train_flat = X_train_norm.reshape(-1, 784)
X_test_flat = X_test_norm.reshape(-1, 784)

print(f"Shape setelah flatten: {X_train_flat.shape}")  # (60000, 784)
```

```python
# 3. Bangun model MLP untuk 10 kelas
model_mnist = keras.Sequential([
    layers.Dense(256, activation='relu', input_shape=(784,)),
    layers.BatchNormalization(),
    layers.Dropout(0.3),

    layers.Dense(128, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.2),

    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 kelas digit (0-9)
])

model_mnist.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',  # Label berupa integer
    metrics=['accuracy']
)

model_mnist.summary()

# 4. Training dengan callbacks
callbacks_list = [
    keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=5, restore_best_weights=True
    ),
    keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6
    )
]

history_mnist = model_mnist.fit(
    X_train_flat, y_train,
    epochs=50,
    batch_size=128,
    validation_split=0.1,
    callbacks=callbacks_list,
    verbose=1
)
```

```python
# 5. Evaluasi lengkap
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

test_loss, test_acc = model_mnist.evaluate(X_test_flat, y_test, verbose=0)
print(f"Test Accuracy: {test_acc:.4f} ({test_acc*100:.1f}%)")

# Prediksi
y_pred = model_mnist.predict(X_test_flat, verbose=0).argmax(axis=1)

# Classification report
print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, y_pred, digits=4))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=range(10), yticklabels=range(10), ax=ax)
ax.set_xlabel('Prediksi', fontsize=12)
ax.set_ylabel('Aktual', fontsize=12)
ax.set_title(f'Confusion Matrix — MNIST (Accuracy: {test_acc:.4f})', fontsize=14)
plt.tight_layout()
plt.savefig('mnist_confusion_matrix.png', dpi=150, bbox_inches='tight')
plt.show()

# Visualisasi prediksi yang salah
salah_idx = np.where(y_pred != y_test)[0]
print(f"\nJumlah prediksi salah: {len(salah_idx)} dari {len(y_test)}")

fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flatten()):
    if i < len(salah_idx):
        idx = salah_idx[i]
        ax.imshow(X_test[idx], cmap='gray')
        ax.set_title(f'Pred:{y_pred[idx]} True:{y_test[idx]}',
                     fontsize=10, color='red')
    ax.axis('off')
plt.suptitle('Contoh Prediksi yang Salah', fontsize=14)
plt.tight_layout()
plt.savefig('mnist_errors.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 10.8.2 Studi Kasus Indonesia: Klasifikasi Sentimen Review Produk

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Simulasi dataset: prediksi kategori produk berdasarkan fitur transaksi
# Konteks: e-commerce Indonesia (Tokopedia, Shopee, Bukalapak)
np.random.seed(42)
n = 2000

# Fitur transaksi
data_produk = pd.DataFrame({
    'harga_ribu': np.concatenate([
        np.random.normal(50, 20, 500),     # Kategori 0: Aksesoris
        np.random.normal(200, 80, 500),    # Kategori 1: Pakaian
        np.random.normal(1500, 500, 500),  # Kategori 2: Elektronik
        np.random.normal(5000, 1500, 500)  # Kategori 3: Gadget
    ]).clip(10),
    'berat_gram': np.concatenate([
        np.random.normal(50, 20, 500),
        np.random.normal(300, 100, 500),
        np.random.normal(1000, 400, 500),
        np.random.normal(300, 100, 500)
    ]).clip(10),
    'jumlah_review': np.concatenate([
        np.random.poisson(50, 500),
        np.random.poisson(100, 500),
        np.random.poisson(30, 500),
        np.random.poisson(200, 500)
    ]),
    'rating_rata2': np.concatenate([
        np.random.normal(4.2, 0.5, 500),
        np.random.normal(4.0, 0.6, 500),
        np.random.normal(4.3, 0.4, 500),
        np.random.normal(4.5, 0.3, 500)
    ]).clip(1, 5),
    'jumlah_terjual': np.concatenate([
        np.random.poisson(200, 500),
        np.random.poisson(500, 500),
        np.random.poisson(50, 500),
        np.random.poisson(100, 500)
    ]),
    'kategori': np.repeat([0, 1, 2, 3], 500)
})

nama_kategori = ['Aksesoris', 'Pakaian', 'Elektronik', 'Gadget']
print("=== DATASET PRODUK E-COMMERCE INDONESIA ===")
print(f"Jumlah data: {len(data_produk)}")
print(f"Distribusi kategori:")
for i, nama in enumerate(nama_kategori):
    print(f"  {nama}: {(data_produk['kategori'] == i).sum()}")

# Persiapan data
X = data_produk.drop('kategori', axis=1).values
y = data_produk['kategori'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Bangun model klasifikasi multi-kelas
model_produk = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    layers.Dense(32, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(4, activation='softmax')  # 4 kategori produk
])

model_produk.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Training
early_stop = keras.callbacks.EarlyStopping(
    monitor='val_loss', patience=10, restore_best_weights=True
)

history_produk = model_produk.fit(
    X_train_scaled, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=0
)

# Evaluasi
test_loss, test_acc = model_produk.evaluate(X_test_scaled, y_test, verbose=0)
print(f"\n=== EVALUASI KLASIFIKASI PRODUK ===")
print(f"Test Accuracy: {test_acc:.4f} ({test_acc*100:.1f}%)")

from sklearn.metrics import classification_report
y_pred_produk = model_produk.predict(X_test_scaled, verbose=0).argmax(axis=1)
print(classification_report(y_test, y_pred_produk,
                            target_names=nama_kategori, digits=4))
```

---

## 10.9 AI Corner: Menggunakan AI untuk Deep Learning

### Level: Advanced

| Kemampuan AI | Contoh Penggunaan |
|-------------|-------------------|
| Debug arsitektur | Meminta AI memeriksa apakah arsitektur sesuai dengan masalah |
| Tuning hyperparameter | Meminta AI menyarankan learning rate, batch size, jumlah layer |
| Diagnosa training | Meminta AI menganalisis training history (overfit/underfit) |
| Menjelaskan error | Meminta AI menjelaskan error TensorFlow/Keras yang sulit dipahami |
| Review kode | Meminta AI memeriksa pipeline ML untuk kesalahan umum |

### Contoh Prompt yang Baik

```
Model neural network saya untuk klasifikasi produk e-commerce 4 kelas:
- Input: 5 fitur (harga, berat, review, rating, terjual)
- Arsitektur: Dense(64,relu) → BN → Dropout(0.3) → Dense(32,relu) →
  Dropout(0.2) → Dense(4,softmax)
- Optimizer: Adam (lr=0.001)
- Loss: sparse_categorical_crossentropy

Training history (50 epoch):
- Training accuracy: 92.5%, Validation accuracy: 88.1%
- Training loss: 0.21, Validation loss: 0.35

1. Apakah model ini overfit? Jika ya, seberapa parah?
2. Apa yang bisa saya lakukan untuk mengurangi gap train-val?
3. Apakah arsitektur ini sudah tepat untuk 2000 data x 5 fitur?
4. Apakah perlu menambah data atau cukup regularisasi?
```

### Contoh Prompt yang Kurang Baik

```
Neural network saya error, tolong perbaiki
```
*(Terlalu umum — tidak menyertakan arsitektur, data, atau pesan error)*

### Yang Perlu Diingat

1. **AI tidak melihat data Anda** — selalu sertakan deskripsi dataset (ukuran, fitur, distribusi kelas)
2. **Verifikasi saran AI secara empiris** — dalam deep learning, eksperimen > teori
3. **AI bisa menyarankan arsitektur**, tetapi Anda yang memahami batasan komputasi (memory, waktu)
4. **Dokumentasikan penggunaan AI** — catat prompt, output, dan modifikasi di AI Usage Log
5. **Jangan copy-paste tanpa memahami** — pahami mengapa setiap parameter dipilih

### Template AI Usage Log untuk Bab 10

```markdown
## AI Usage Documentation — Bab 10: Neural Networks
### Tool: [Claude / ChatGPT / Copilot]
### Prompt: "Model neural network saya overfit, ini training history-nya..."
### Output: [Saran AI: tambah dropout, kurangi jumlah layer, gunakan early stopping]
### Modifikasi: [Menambahkan Dropout(0.3) dan Early Stopping(patience=10)]
### Hasil: [Gap train-val berkurang dari 4.4% ke 1.2%]
### Refleksi: [Dropout sangat efektif untuk model dengan >100K parameter]
```

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan antara perceptron, multi-layer perceptron (MLP), dan deep learning. Sertakan diagram arsitektur sederhana untuk masing-masing.

**Soal 2.** Sebutkan dan jelaskan 5 activation function yang umum digunakan (Sigmoid, Tanh, ReLU, Leaky ReLU, Softmax). Untuk masing-masing, tuliskan range output dan kapan activation function tersebut digunakan.

**Soal 3.** Apa itu backpropagation? Jelaskan secara intuitif (menggunakan analogi sehari-hari) bagaimana neural network "belajar" dari kesalahan prediksi.

**Soal 4.** Jelaskan perbedaan antara:
- a) Loss function dan optimizer — apa peran masing-masing dalam training?
- b) Epoch, batch, dan iteration — berapa iteration per epoch jika data = 5000 dan batch_size = 50?
- c) Overfitting dan underfitting pada neural network — bagaimana mendeteksinya dari training history?
- d) Dropout dan early stopping — mekanisme kerja masing-masing

**Soal 5.** Mengapa perceptron tidak bisa menyelesaikan masalah XOR? Apa solusinya dan mengapa solusi tersebut berhasil?

### Tingkat Menengah (C3)

**Soal 6.** Tulis kode Keras/TensorFlow untuk membangun MLP yang mengklasifikasikan dataset Iris (4 fitur, 3 kelas). Gunakan:
- 2 hidden layers (32 dan 16 neuron, ReLU)
- BatchNormalization setelah setiap hidden layer
- Dropout(0.2) setelah hidden layer pertama
- Softmax di output layer
- Adam optimizer, sparse_categorical_crossentropy loss
- Early stopping dengan patience=10
- Tampilkan training history (loss dan accuracy) dalam 2 subplot

**Soal 7.** Hitung secara manual jumlah parameter (weights + biases) untuk arsitektur berikut:
- Input: 20 fitur
- Hidden 1: 64 neuron (ReLU)
- BatchNormalization (berapa parameter tambahan?)
- Hidden 2: 32 neuron (ReLU)
- Output: 5 neuron (Softmax)
Tunjukkan perhitungan langkah demi langkah.

**Soal 8.** Diberikan training history berikut, analisis dan berikan solusi:
```
Epoch 10: train_loss=0.12, val_loss=0.15, train_acc=96%, val_acc=94%
Epoch 20: train_loss=0.05, val_loss=0.18, train_acc=98%, val_acc=93%
Epoch 30: train_loss=0.02, val_loss=0.25, train_acc=99%, val_acc=91%
```
- a) Apakah model overfit, underfit, atau seimbang? Jelaskan buktinya.
- b) Teknik regularisasi apa yang sebaiknya diterapkan? Jelaskan alasannya.
- c) Tulis kode Keras lengkap yang menerapkan minimal 3 teknik regularisasi.

### Tingkat Mahir (C4)

**Soal 9.** Bangun neural network untuk **memprediksi harga rumah di Jakarta** (masalah regresi). Buat dataset sintetis dengan fitur: luas_tanah, luas_bangunan, jumlah_kamar, jarak_ke_pusat, tahun_dibangun, ada_garasi. Implementasikan:
- Preprocessing lengkap (StandardScaler, handling outlier)
- Arsitektur MLP yang tepat untuk regresi
- Minimal 3 teknik regularisasi (Dropout, Early Stopping, BatchNorm)
- Learning rate scheduling (ReduceLROnPlateau)
- Evaluasi dengan MAE, RMSE, dan R-squared
- Visualisasi: (a) prediksi vs aktual, (b) training history, (c) residual plot

**Soal 10.** Bandingkan performa 4 konfigurasi neural network pada dataset MNIST:
- Model A: 1 hidden layer (128 neuron), tanpa regularisasi
- Model B: 3 hidden layers (256-128-64), tanpa regularisasi
- Model C: 3 hidden layers (256-128-64), dengan Dropout(0.3)
- Model D: 3 hidden layers (256-128-64), dengan BatchNorm + Dropout + Early Stopping

Untuk setiap model, catat: test accuracy, jumlah parameter, waktu training, dan epoch terbaik. Buat tabel perbandingan dan analisis:
- a) Apakah model yang lebih deep selalu lebih baik?
- b) Seberapa besar dampak regularisasi terhadap generalisasi?
- c) Model mana yang Anda rekomendasikan dan mengapa?

---

## Rangkuman

1. **Neural network** terinspirasi dari neuron biologis, terdiri dari layer input, hidden, dan output. Setiap neuron menghitung *weighted sum* + *bias*, lalu menerapkan *activation function* untuk menambah non-linearitas.

2. **Perceptron** adalah model neuron tunggal yang hanya mampu menyelesaikan masalah *linearly separable*. **Multi-Layer Perceptron (MLP)** menambahkan hidden layers untuk mengatasi keterbatasan ini, memungkinkan pembelajaran pola non-linear.

3. **Activation function** menambahkan non-linearitas esensial ke neural network. **ReLU** paling populer untuk hidden layers; **Sigmoid** untuk output klasifikasi biner; **Softmax** untuk output klasifikasi multi-kelas.

4. **Forward propagation** menghitung output dari input melalui seluruh layer. **Backpropagation** menghitung gradien loss terhadap setiap parameter menggunakan *chain rule*, memungkinkan **optimizer** (Adam, SGD) mengupdate weights secara efisien.

5. **Loss function** mengukur seberapa buruk prediksi model (MSE untuk regresi, cross-entropy untuk klasifikasi). **Optimizer** menentukan bagaimana weights di-update berdasarkan gradien. **Adam** adalah pilihan default yang robust.

6. **TensorFlow/Keras** memudahkan implementasi neural network: `Sequential API` untuk arsitektur sederhana, `compile()` untuk konfigurasi training, `fit()` untuk training, dan `evaluate()` untuk evaluasi.

7. **Regularisasi** (Dropout, Early Stopping, Batch Normalization, L2) mencegah overfitting dan meningkatkan generalisasi model. Kombinasi beberapa teknik regularisasi umumnya memberikan hasil terbaik.

8. Neural network sangat powerful untuk masalah kompleks (klasifikasi, regresi), tetapi membutuhkan **data yang cukup**, **preprocessing yang benar** (standardisasi!), dan **tuning hyperparameter** yang cermat.

---

## Referensi

1. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press. Retrieved from https://www.deeplearningbook.org
2. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
3. Chollet, F. (2021). *Deep Learning with Python* (2nd ed.). Manning Publications.
4. TensorFlow documentation. (2026). *Keras API Reference*. Retrieved from https://www.tensorflow.org/api_docs/python/tf/keras
5. LeCun, Y., Bottou, L., Bengio, Y., & Haffner, P. (1998). Gradient-based learning applied to document recognition. *Proceedings of the IEEE*, 86(11), 2278-2324.
6. Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors. *Nature*, 323, 533-536.
7. Kingma, D. P., & Ba, J. (2015). Adam: A method for stochastic optimization. *ICLR 2015*.
8. Srivastava, N., Hinton, G., Krizhevsky, A., et al. (2014). Dropout: A simple way to prevent neural networks from overfitting. *JMLR*, 15(1), 1929-1958.

---

*Bab berikutnya: **Bab 11 — Natural Language Processing Dasar***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
