# BAB 10: NEURAL NETWORKS DAN DEEP LEARNING

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| Sub-CPMK 11.1 | Menjelaskan konsep dasar neural network: perceptron, multi-layer perceptron, activation function, dan backpropagation | C2 |
| Sub-CPMK 11.2 | Menerapkan neural network menggunakan Keras/TensorFlow untuk masalah klasifikasi dan regresi | C3 |

**CPMK-5:** Menerapkan neural network dan deep learning untuk masalah prediktif.

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

---

## 10.1 Inspirasi Biologis: Neuron dan Sinapsis

### 10.1.1 Neuron Biologis

Otak manusia terdiri dari sekitar **86 miliar neuron** yang terhubung melalui **sinapsis**. Setiap neuron menerima sinyal dari neuron lain, memproses sinyal tersebut, dan meneruskan hasilnya ke neuron berikutnya.

```
Neuron Biologis:
                    Dendrit (input)
                    ┌──────┐
sinyal masuk ──────→│      │
sinyal masuk ──────→│ Soma │──→ Akson ──→ sinyal keluar
sinyal masuk ──────→│(badan│     (output)
                    │ sel) │
                    └──────┘
                    Jika total sinyal > threshold → neuron "aktif" (fire)
```

### 10.1.2 Dari Biologi ke Matematika

**Artificial neural network** (jaringan saraf tiruan) terinspirasi dari neuron biologis, tetapi **sangat disederhanakan**:

| Biologi | Artificial |
|---------|-----------|
| Dendrit | Input (fitur) |
| Sinapsis | Weights (bobot) |
| Soma | Fungsi penjumlahan + activation |
| Threshold | Bias |
| Akson | Output |

> **Catatan penting:** Neural network artificial **tidak** benar-benar mensimulasikan otak. Analogi biologis berguna untuk intuisi, tetapi realitasnya neural network adalah **model matematika** berbasis optimisasi.

---

## 10.2 Perceptron: Model Neuron Tunggal

### 10.2.1 Weights, Bias, dan Activation

**Perceptron** adalah model neural network paling sederhana — satu neuron tunggal:

```
    x1 ──w1──┐
              │
    x2 ──w2──┼──→ Σ(wi*xi) + b ──→ f(z) ──→ output (ŷ)
              │
    x3 ──w3──┘

Di mana:
  x1, x2, x3  = input (fitur)
  w1, w2, w3   = weights (bobot, dipelajari)
  b            = bias (dipelajari)
  f(z)         = activation function
  z = w1*x1 + w2*x2 + w3*x3 + b
```

**Secara matematis:**

$$\hat{y} = f\left(\sum_{i=1}^{n} w_i x_i + b\right) = f(\mathbf{w}^T \mathbf{x} + b)$$

Untuk klasifikasi biner, perceptron menggunakan **step function**:

$$f(z) = \begin{cases} 1 & \text{jika } z \geq 0 \\ 0 & \text{jika } z < 0 \end{cases}$$

### 10.2.2 Perceptron Learning Rule

Perceptron belajar dengan **mengupdate weights** berdasarkan kesalahan prediksi:

$$w_i \leftarrow w_i + \alpha \cdot (y - \hat{y}) \cdot x_i$$

di mana $\alpha$ adalah *learning rate*.

```python
import numpy as np
import matplotlib.pyplot as plt

# Implementasi Perceptron dari awal
class PerceptronSederhana:
    def __init__(self, learning_rate=0.1, n_iterasi=100):
        self.lr = learning_rate
        self.n_iter = n_iterasi
        self.weights = None
        self.bias = None
        self.errors = []

    def fit(self, X, y):
        n_sampel, n_fitur = X.shape
        self.weights = np.zeros(n_fitur)
        self.bias = 0

        for epoch in range(self.n_iter):
            total_error = 0
            for xi, yi in zip(X, y):
                # Prediksi
                z = np.dot(xi, self.weights) + self.bias
                y_pred = 1 if z >= 0 else 0

                # Update weights
                error = yi - y_pred
                self.weights += self.lr * error * xi
                self.bias += self.lr * error
                total_error += abs(error)

            self.errors.append(total_error)
            if total_error == 0:
                print(f"Konvergen di epoch {epoch + 1}")
                break

    def predict(self, X):
        z = np.dot(X, self.weights) + self.bias
        return np.where(z >= 0, 1, 0)

# Contoh: AND gate
X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])

# Latih perceptron
p = PerceptronSederhana(learning_rate=0.1, n_iterasi=20)
p.fit(X_and, y_and)

# Prediksi
print("=== PERCEPTRON UNTUK AND GATE ===")
print(f"Weights: {p.weights}")
print(f"Bias: {p.bias}")
for xi, yi in zip(X_and, y_and):
    pred = p.predict(xi.reshape(1, -1))[0]
    print(f"Input: {xi} → Prediksi: {pred} (Target: {yi})")

# Catatan: Perceptron TIDAK BISA mempelajari XOR
# karena XOR tidak linearly separable
X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([0, 1, 1, 0])

p_xor = PerceptronSederhana(learning_rate=0.1, n_iterasi=100)
p_xor.fit(X_xor, y_xor)
print(f"\n=== XOR GATE (perceptron gagal) ===")
for xi, yi in zip(X_xor, y_xor):
    pred = p_xor.predict(xi.reshape(1, -1))[0]
    status = "OK" if pred == yi else "SALAH"
    print(f"Input: {xi} → Prediksi: {pred} (Target: {yi}) [{status}]")
```

> **Keterbatasan perceptron:** Perceptron hanya bisa menyelesaikan masalah yang **linearly separable**. Masalah XOR membutuhkan **hidden layer** — inilah motivasi lahirnya Multi-Layer Perceptron.

---

## 10.3 Multi-Layer Perceptron (MLP)

### 10.3.1 Hidden Layers

**MLP** menambahkan satu atau lebih **hidden layers** di antara input dan output. Ini memungkinkan network mempelajari hubungan **non-linear** yang kompleks.

```
Input Layer    Hidden Layer 1    Hidden Layer 2    Output Layer

  x1 ─────────── h1 ─────────── h4 ──────────── ŷ1
          ╲   ╱        ╲   ╱        ╲   ╱
  x2 ─────────── h2 ─────────── h5 ──────────── ŷ2
          ╱   ╲        ╱   ╲        ╱   ╲
  x3 ─────────── h3 ─────────── h6

 (3 neuron)    (3 neuron)     (3 neuron)    (2 neuron)

Total parameter = (3×3 + 3) + (3×3 + 3) + (3×2 + 2) = 44
```

**Terminologi:**
- **Input layer:** Menerima fitur data (tidak dihitung sebagai layer)
- **Hidden layers:** Layer antara input dan output (melakukan komputasi)
- **Output layer:** Menghasilkan prediksi final
- **Deep learning:** Neural network dengan **>= 2 hidden layers**

### 10.3.2 Forward Pass

Forward pass adalah proses **menghitung output** dari input melalui seluruh layer:

```python
# Forward pass secara manual (untuk pemahaman)
import numpy as np

# Network: 2 input → 3 hidden → 1 output
np.random.seed(42)

# Input
X = np.array([0.5, 0.3])

# Layer 1: Input(2) → Hidden(3)
W1 = np.random.randn(2, 3) * 0.5  # Weights
b1 = np.zeros(3)                    # Bias
z1 = X @ W1 + b1                    # Linear combination
a1 = np.maximum(0, z1)              # ReLU activation

# Layer 2: Hidden(3) → Output(1)
W2 = np.random.randn(3, 1) * 0.5
b2 = np.zeros(1)
z2 = a1 @ W2 + b2
a2 = 1 / (1 + np.exp(-z2))          # Sigmoid activation

print(f"Input: {X}")
print(f"Hidden layer (z1): {z1.round(4)}")
print(f"Hidden layer (a1, setelah ReLU): {a1.round(4)}")
print(f"Output (z2): {z2.round(4)}")
print(f"Output (a2, setelah sigmoid): {a2.round(4)}")
```

### 10.3.3 Universal Approximation Theorem (Intuisi)

> **Teorema:** Neural network dengan **satu hidden layer** dan **jumlah neuron yang cukup** dapat mengaproksimasi **fungsi kontinu apapun** dengan akurasi sembarang.

**Artinya secara praktis:**
- Neural network secara teori bisa mempelajari pola apapun
- Tetapi "jumlah neuron yang cukup" bisa sangat besar
- Dalam praktik, **deep networks** (banyak layer) lebih efisien daripada **wide networks** (satu layer banyak neuron)

---

## 10.4 Activation Functions

### 10.4.1 Jenis-jenis Activation Function

Activation function menambahkan **non-linearity** ke neural network. Tanpa activation function, MLP hanya menjadi regresi linear biasa.

| Activation | Formula | Range | Digunakan Di |
|-----------|---------|-------|-------------|
| **Sigmoid** | $\sigma(z) = \frac{1}{1+e^{-z}}$ | (0, 1) | Output klasifikasi biner |
| **Tanh** | $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$ | (-1, 1) | Hidden layer (jarang dipakai) |
| **ReLU** | $\max(0, z)$ | [0, +inf) | Hidden layer (paling populer) |
| **Leaky ReLU** | $\max(0.01z, z)$ | (-inf, +inf) | Hidden layer (varian ReLU) |
| **Softmax** | $\frac{e^{z_i}}{\sum_j e^{z_j}}$ | (0, 1), sum=1 | Output klasifikasi multi-kelas |

```python
import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(-5, 5, 200)

# Hitung semua activation function
aktivasi = {
    'Sigmoid': 1 / (1 + np.exp(-z)),
    'Tanh': np.tanh(z),
    'ReLU': np.maximum(0, z),
    'Leaky ReLU': np.where(z > 0, z, 0.01 * z)
}

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

for ax, (nama, nilai) in zip(axes.flatten(), aktivasi.items()):
    ax.plot(z, nilai, 'b-', linewidth=2)
    ax.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
    ax.axvline(x=0, color='gray', linestyle='-', linewidth=0.5)
    ax.set_title(nama, fontsize=14)
    ax.set_xlabel('z')
    ax.set_ylabel('f(z)')
    ax.grid(True, alpha=0.3)

plt.suptitle('Activation Functions', fontsize=16, y=1.02)
plt.tight_layout()
plt.savefig('activation_functions.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 10.4.2 Kapan Menggunakan Activation Function Tertentu

```
Tipe Masalah                    Output Layer         Hidden Layer
─────────────────────────────────────────────────────────────────
Regresi                         Linear (none)        ReLU
Klasifikasi biner               Sigmoid              ReLU
Klasifikasi multi-kelas         Softmax              ReLU
```

**Mengapa ReLU populer untuk hidden layers?**
1. Komputasi cepat (hanya perbandingan dan perkalian)
2. Mengurangi masalah *vanishing gradient*
3. Menghasilkan sparse activation (banyak output 0) — efisien

---

## 10.5 Backpropagation

### 10.5.1 Intuisi Chain Rule

**Backpropagation** adalah algoritma untuk menghitung **gradien** (turunan parsial) dari loss function terhadap setiap weight di network. Gradien ini digunakan untuk **mengupdate weights** agar prediksi membaik.

**Analogi:**

> Bayangkan Anda melempar bola ke keranjang dan meleset. Anda ingin tahu: "Berapa banyak saya harus menyesuaikan sudut lengan, kekuatan lempar, dan arah?" Backpropagation menjawab pertanyaan ini untuk setiap weight di neural network.

**Chain rule:**

$$\frac{\partial L}{\partial w_1} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z_2} \cdot \frac{\partial z_2}{\partial a_1} \cdot \frac{\partial a_1}{\partial z_1} \cdot \frac{\partial z_1}{\partial w_1}$$

### 10.5.2 Gradient Flow

```
Forward Pass (maju):
Input → [W1] → Hidden → [W2] → Output → Loss
  x    ──→      a1    ──→      ŷ     ──→  L

Backward Pass (mundur):
Input ← [∂L/∂W1] ← Hidden ← [∂L/∂W2] ← Output ← ∂L/∂ŷ
         gradien              gradien

Update:
W1_baru = W1_lama - learning_rate × ∂L/∂W1
W2_baru = W2_lama - learning_rate × ∂L/∂W2
```

### 10.5.3 Vanishing dan Exploding Gradients

| Masalah | Penyebab | Dampak | Solusi |
|---------|----------|--------|--------|
| **Vanishing gradient** | Sigmoid/tanh memiliki turunan kecil | Gradien mendekati 0, layer awal tidak belajar | ReLU, skip connections, Batch Norm |
| **Exploding gradient** | Weights terlalu besar | Gradien meledak, training tidak stabil | Gradient clipping, proper initialization |

```python
# Demonstrasi vanishing gradient dengan sigmoid
import numpy as np

z = np.linspace(-5, 5, 100)
sigmoid = 1 / (1 + np.exp(-z))
sigmoid_deriv = sigmoid * (1 - sigmoid)

print(f"Sigmoid derivative:")
print(f"  Maksimum: {sigmoid_deriv.max():.4f}")  # 0.25
print(f"  Jika 5 layer: 0.25^5 = {0.25**5:.6f}")  # Gradien sangat kecil!
print(f"  Jika 10 layer: 0.25^10 = {0.25**10:.10f}")

# Bandingkan dengan ReLU
relu_deriv = np.where(z > 0, 1, 0).astype(float)
print(f"\nReLU derivative:")
print(f"  Untuk z > 0: selalu 1 (gradien mengalir tanpa menyusut)")
```

---

## 10.6 Loss Functions

Loss function mengukur **seberapa buruk** prediksi model. Tujuan training: **meminimalkan loss**.

| Loss Function | Formula | Digunakan Untuk |
|---------------|---------|-----------------|
| **MSE** (Mean Squared Error) | $\frac{1}{n}\sum(y_i - \hat{y}_i)^2$ | Regresi |
| **Binary Cross-Entropy** | $-\frac{1}{n}\sum[y\log\hat{y} + (1-y)\log(1-\hat{y})]$ | Klasifikasi biner |
| **Categorical Cross-Entropy** | $-\frac{1}{n}\sum\sum y_{ij}\log\hat{y}_{ij}$ | Klasifikasi multi-kelas |

```python
import numpy as np

# Contoh perhitungan loss
y_true = np.array([1, 0, 1, 1, 0])
y_pred = np.array([0.9, 0.1, 0.8, 0.7, 0.3])

# Binary Cross-Entropy
bce = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
print(f"Binary Cross-Entropy: {bce:.4f}")

# MSE (untuk regresi)
y_true_reg = np.array([3.0, 5.0, 7.0, 9.0])
y_pred_reg = np.array([2.8, 5.2, 6.9, 9.1])
mse = np.mean((y_true_reg - y_pred_reg)**2)
print(f"MSE: {mse:.4f}")
```

---

## 10.7 Optimizers

Optimizer menentukan **bagaimana weights di-update** berdasarkan gradien.

| Optimizer | Cara Kerja | Kelebihan | Kekurangan |
|-----------|-----------|-----------|------------|
| **SGD** | Update per mini-batch | Sederhana, generalisasi baik | Konvergensi lambat |
| **Adam** | Adaptive learning rate per parameter | Cepat konvergen, robust | Bisa overfit |
| **RMSprop** | Adaptive learning rate berdasarkan running average | Baik untuk RNN | Kurang populer dari Adam |

```
SGD:      w = w - lr × g                    (sederhana)
Momentum: w = w - lr × g - momentum × v     (+ inersia)
Adam:     w = w - lr × m̂/(√v̂ + ε)          (adaptive)

Di mana: g = gradien, m̂ = first moment, v̂ = second moment
```

**Panduan pemilihan optimizer:**

```
Mulai dengan Adam (lr=0.001) → biasanya cukup baik
Jika overfit → coba SGD + momentum (lr=0.01, momentum=0.9)
Jika underfitting → naikkan learning rate atau arsitektur
```

---

## 10.8 Membangun Neural Network dengan Keras

### 10.8.1 Sequential API

**Keras** adalah high-level API untuk TensorFlow yang memudahkan pembuatan neural network.

```python
# Instalasi (jika belum ada di Colab)
# !pip install tensorflow

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

print(f"TensorFlow versi: {tf.__version__}")

# Buat model sederhana dengan Sequential API
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(10,)),  # Hidden layer 1
    layers.Dense(32, activation='relu'),                      # Hidden layer 2
    layers.Dense(1, activation='sigmoid')                     # Output layer
])

# Ringkasan arsitektur
model.summary()

# Output:
# Layer (type)               Output Shape     Param #
# dense (Dense)              (None, 64)       704      ← 10×64 + 64 = 704
# dense_1 (Dense)            (None, 32)       2080     ← 64×32 + 32 = 2080
# dense_2 (Dense)            (None, 1)        33       ← 32×1 + 1 = 33
# Total params: 2,817
```

### 10.8.2 Model Compilation

```python
# Kompilasi model — menentukan optimizer, loss, dan metrik
model.compile(
    optimizer='adam',                    # Optimizer
    loss='binary_crossentropy',         # Loss function
    metrics=['accuracy']                # Metrik evaluasi
)

# Konfigurasi lebih detail:
model_detail = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(10,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model_detail.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['accuracy', keras.metrics.AUC(name='auc')]
)
```

**Cheat sheet kompilasi:**

```
Masalah                 Loss                    Output Activation   Metrics
─────────────────────────────────────────────────────────────────────────────
Regresi                 'mse'                   'linear' (none)     'mae'
Klasifikasi biner       'binary_crossentropy'   'sigmoid'           'accuracy'
Multi-kelas             'categorical_crossentropy' 'softmax'        'accuracy'
Multi-kelas (integer)   'sparse_categorical_crossentropy' 'softmax' 'accuracy'
```

### 10.8.3 Model Training

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Muat data
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# Split dan standardisasi
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Buat model
model_cancer = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(16, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model_cancer.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Training
history = model_cancer.fit(
    X_train_scaled, y_train,
    epochs=100,                    # Jumlah iterasi penuh atas training data
    batch_size=32,                 # Jumlah sampel per update
    validation_split=0.2,          # 20% training data untuk validasi
    verbose=1                      # Tampilkan progress
)

# Evaluasi pada test set
test_loss, test_acc = model_cancer.evaluate(X_test_scaled, y_test, verbose=0)
print(f"\nTest Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_acc:.4f}")
```

### 10.8.4 Visualisasi Training History

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot Loss
axes[0].plot(history.history['loss'], label='Training Loss')
axes[0].plot(history.history['val_loss'], label='Validation Loss')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Loss')
axes[0].set_title('Training vs Validation Loss')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Plot Accuracy
axes[1].plot(history.history['accuracy'], label='Training Accuracy')
axes[1].plot(history.history['val_accuracy'], label='Validation Accuracy')
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
# - Jika keduanya masih menurun → UNDERFITTING (tambah epoch)
# - Jika keduanya stabil → model sudah konvergen
```

---

## 10.9 Regularization Techniques

### Dropout

```python
# Dropout: matikan neuron secara acak saat training
model_dropout = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    layers.Dropout(0.3),       # 30% neuron dimatikan saat training
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),       # 20% neuron dimatikan
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model_dropout.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

### Early Stopping

```python
# Early Stopping: hentikan training jika val_loss tidak membaik
early_stop = keras.callbacks.EarlyStopping(
    monitor='val_loss',     # Pantau validation loss
    patience=10,            # Tunggu 10 epoch tanpa improvement
    restore_best_weights=True  # Kembalikan ke weights terbaik
)

history_es = model_dropout.fit(
    X_train_scaled, y_train,
    epochs=200,             # Set tinggi, early stopping akan menghentikan
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=0
)

print(f"Training berhenti di epoch {len(history_es.history['loss'])}")
test_loss, test_acc = model_dropout.evaluate(X_test_scaled, y_test, verbose=0)
print(f"Test Accuracy (dengan Dropout + Early Stopping): {test_acc:.4f}")
```

### Batch Normalization

```python
# Batch Normalization: normalisasi output setiap layer
model_bn = keras.Sequential([
    layers.Dense(128, input_shape=(X_train_scaled.shape[1],)),
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

model_bn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model_bn.summary()
```

**Ringkasan teknik regularization:**

| Teknik | Cara Kerja | Kapan Digunakan |
|--------|-----------|-----------------|
| **Dropout** | Matikan neuron secara acak | Selalu (default 0.2-0.5) |
| **Early Stopping** | Hentikan training saat val_loss naik | Selalu |
| **Batch Normalization** | Normalisasi output layer | Network dalam (deep) |
| **L1/L2 Regularization** | Penalti pada weights besar | Jika masih overfit |

---

## 10.10 Contoh Lengkap: Klasifikasi Digit MNIST

### 10.10.1 Memuat dan Memahami Dataset

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt

# Muat dataset MNIST
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

print(f"Training set: {X_train.shape}")    # (60000, 28, 28)
print(f"Test set: {X_test.shape}")         # (10000, 28, 28)
print(f"Label unik: {np.unique(y_train)}")  # [0, 1, 2, ..., 9]

# Visualisasi beberapa contoh
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flatten()):
    ax.imshow(X_train[i], cmap='gray')
    ax.set_title(f'Label: {y_train[i]}', fontsize=11)
    ax.axis('off')
plt.suptitle('Contoh Data MNIST', fontsize=14)
plt.tight_layout()
plt.savefig('mnist_samples.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 10.10.2 Preprocessing

```python
# Normalisasi pixel (0-255 → 0-1)
X_train_norm = X_train.astype('float32') / 255.0
X_test_norm = X_test.astype('float32') / 255.0

# Flatten: 28x28 → 784 (untuk Dense/MLP)
X_train_flat = X_train_norm.reshape(-1, 784)
X_test_flat = X_test_norm.reshape(-1, 784)

print(f"Shape setelah normalisasi dan flatten: {X_train_flat.shape}")
```

### 10.10.3 Membangun dan Melatih Model

```python
# Bangun model MLP untuk klasifikasi 10 digit
model_mnist = keras.Sequential([
    layers.Dense(256, activation='relu', input_shape=(784,)),
    layers.BatchNormalization(),
    layers.Dropout(0.3),

    layers.Dense(128, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.2),

    layers.Dense(64, activation='relu'),

    layers.Dense(10, activation='softmax')  # 10 kelas (digit 0-9)
])

model_mnist.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',  # Label berupa integer
    metrics=['accuracy']
)

model_mnist.summary()

# Callbacks
callbacks_list = [
    keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=5, restore_best_weights=True
    ),
    keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6
    )
]

# Training
history_mnist = model_mnist.fit(
    X_train_flat, y_train,
    epochs=50,
    batch_size=128,
    validation_split=0.1,
    callbacks=callbacks_list,
    verbose=1
)
```

### 10.10.4 Evaluasi dan Visualisasi

```python
# Evaluasi pada test set
test_loss, test_acc = model_mnist.evaluate(X_test_flat, y_test, verbose=0)
print(f"Test Accuracy: {test_acc:.4f}")
print(f"Test Loss: {test_loss:.4f}")

# Confusion matrix
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

y_pred = model_mnist.predict(X_test_flat).argmax(axis=1)

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
        ax.set_title(f'Pred: {y_pred[idx]}, True: {y_test[idx]}',
                    fontsize=10, color='red')
    ax.axis('off')
plt.suptitle('Contoh Prediksi Salah', fontsize=14)
plt.tight_layout()
plt.savefig('mnist_errors.png', dpi=150, bbox_inches='tight')
plt.show()

# Training history
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(history_mnist.history['loss'], label='Training')
axes[0].plot(history_mnist.history['val_loss'], label='Validation')
axes[0].set_title('Loss')
axes[0].set_xlabel('Epoch')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(history_mnist.history['accuracy'], label='Training')
axes[1].plot(history_mnist.history['val_accuracy'], label='Validation')
axes[1].set_title('Accuracy')
axes[1].set_xlabel('Epoch')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('mnist_training_history.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## 10.11 AI Corner: Menggunakan AI untuk Debug Neural Network

### Level: Advanced

| Kemampuan AI | Contoh Penggunaan |
|-------------|-------------------|
| Debug arsitektur | Meminta AI memeriksa apakah arsitektur network sesuai dengan masalah |
| Tuning hyperparameter | Meminta AI menyarankan learning rate, batch size, jumlah layer |
| Diagnosa training | Meminta AI menganalisis training history (overfit/underfit) |
| Menjelaskan error | Meminta AI menjelaskan error TensorFlow/Keras |

### Contoh Prompt yang Baik

```
Model neural network saya untuk klasifikasi gambar 10 kelas:
- Input: 784 fitur (28x28 piksel)
- Hidden: Dense(256, relu) → Dense(128, relu) → Dense(64, relu)
- Output: Dense(10, softmax)
- Optimizer: Adam(lr=0.001)
- Loss: sparse_categorical_crossentropy

Training history menunjukkan:
- Training accuracy: 99.5%
- Validation accuracy: 97.2%
- Training selesai di epoch 25

1. Apakah model ini overfit?
2. Apa yang bisa saya lakukan untuk meningkatkan validation accuracy?
3. Apakah arsitekturnya sudah tepat untuk masalah ini?
```

### Contoh Prompt yang Kurang Baik

```
Neural network saya error, tolong perbaiki
```

### Yang Perlu Diingat

1. **AI bisa membantu arsitektur**, tapi hanya Anda yang tahu kendala spesifik (memory, waktu training)
2. **Selalu verifikasi saran AI** — coba semua perubahan secara empiris
3. **AI tidak melihat data Anda** — sertakan informasi tentang dataset (ukuran, tipe, distribusi kelas)
4. **Eksperimen > teori** — dalam deep learning, coba dan ukur lebih efektif dari teori

### Template AI Usage Log

```markdown
## AI Usage Documentation — Bab 10
### Tool: [Claude / ChatGPT / Copilot]
### Prompt: "Model neural network saya overfit, ini training history-nya..."
### Output: [Saran AI: tambah dropout, kurangi layer, gunakan early stopping]
### Modifikasi: [Menambahkan Dropout(0.3) dan Early Stopping, hasilnya...]
### Refleksi: [Dropout efektif mengurangi gap train-val dari 3% ke 1%]
```

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan antara perceptron, multi-layer perceptron (MLP), dan deep learning. Gambarkan arsitektur masing-masing.

**Soal 2.** Sebutkan 5 activation function yang umum digunakan. Untuk masing-masing, jelaskan range output dan kapan digunakan.

**Soal 3.** Apa itu backpropagation? Jelaskan secara intuitif (tanpa rumus) bagaimana neural network "belajar" dari kesalahan prediksi.

**Soal 4.** Jelaskan perbedaan antara:
- a) Loss function dan optimizer
- b) Epoch dan batch
- c) Overfitting dan underfitting pada neural network
- d) Dropout dan early stopping

**Soal 5.** Mengapa perceptron tidak bisa menyelesaikan masalah XOR? Apa solusinya?

### Tingkat Menengah (C3)

**Soal 6.** Tulis kode Keras untuk membangun MLP yang mengklasifikasikan dataset Iris (4 fitur, 3 kelas). Gunakan:
- 2 hidden layers (32 dan 16 neuron)
- ReLU activation di hidden layers
- Softmax di output layer
- Adam optimizer, categorical_crossentropy loss
- Tampilkan training history

**Soal 7.** Hitung secara manual jumlah parameter (weights + biases) untuk model berikut:
- Input: 20 fitur
- Hidden 1: 64 neuron
- Hidden 2: 32 neuron
- Output: 5 neuron (5 kelas)

**Soal 8.** Diberikan training history berikut:
```
Epoch 10: train_loss=0.12, val_loss=0.15
Epoch 20: train_loss=0.05, val_loss=0.18
Epoch 30: train_loss=0.02, val_loss=0.25
```
- a) Apakah model overfit atau underfit? Jelaskan.
- b) Teknik apa yang sebaiknya diterapkan?
- c) Tulis kode Keras yang menerapkan teknik tersebut.

### Tingkat Mahir (C4)

**Soal 9.** Bangun neural network untuk memprediksi harga rumah di Jakarta (masalah regresi). Gunakan dataset sintetis dengan fitur: luas_tanah, luas_bangunan, jumlah_kamar, jarak_ke_pusat, tahun_dibangun. Implementasikan:
- Preprocessing (standardisasi)
- Arsitektur MLP yang tepat untuk regresi
- Early stopping dan learning rate scheduling
- Evaluasi dengan MAE dan R-squared
- Visualisasi prediksi vs aktual

**Soal 10.** Bandingkan performa 3 konfigurasi neural network pada dataset MNIST:
- Model A: 1 hidden layer (128 neuron), tanpa regularization
- Model B: 3 hidden layers (256-128-64), dengan Dropout(0.3)
- Model C: 3 hidden layers (256-128-64), dengan BatchNorm + Dropout + Early Stopping
Buat tabel perbandingan (accuracy, jumlah parameter, waktu training). Analisis trade-off antara kompleksitas dan performa.

---

## Rangkuman

1. **Neural network** terinspirasi dari neuron biologis, terdiri dari layer input, hidden, dan output. Setiap neuron menghitung weighted sum + bias, lalu menerapkan activation function.
2. **Perceptron** adalah neuron tunggal yang hanya bisa menyelesaikan masalah linearly separable. **MLP** menambahkan hidden layers untuk mengatasi keterbatasan ini.
3. **Activation function** menambahkan non-linearity. **ReLU** paling populer untuk hidden layers; **sigmoid** untuk output biner; **softmax** untuk output multi-kelas.
4. **Backpropagation** menghitung gradien loss terhadap setiap weight menggunakan chain rule. **Optimizer** (Adam, SGD) menggunakan gradien ini untuk mengupdate weights.
5. **Keras** memudahkan pembuatan neural network dengan Sequential API. Proses: build model, compile (optimizer + loss), fit (training), evaluate.
6. **Regularization** (Dropout, Early Stopping, Batch Normalization) mencegah overfitting dan meningkatkan generalisasi model.
7. Neural network sangat powerful untuk masalah kompleks (klasifikasi gambar, NLP), tetapi membutuhkan **data yang banyak** dan **tuning yang hati-hati**.

---

## Referensi

1. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press. Retrieved from https://www.deeplearningbook.org
2. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
3. Chollet, F. (2021). *Deep Learning with Python* (2nd ed.). Manning Publications.
4. TensorFlow documentation. (2026). *Keras API Reference*. Retrieved from https://www.tensorflow.org/api_docs/python/tf/keras
5. LeCun, Y., Bottou, L., Bengio, Y., & Haffner, P. (1998). Gradient-based learning applied to document recognition. *Proceedings of the IEEE*, 86(11), 2278-2324.
6. Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors. *Nature*, 323, 533-536.

---

*Bab berikutnya: **Bab 11 — Natural Language Processing Dasar***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
