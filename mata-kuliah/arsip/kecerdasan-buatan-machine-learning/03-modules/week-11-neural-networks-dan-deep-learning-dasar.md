# Minggu 11: Neural Networks dan Deep Learning Dasar

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 11 |
| **Topik** | Neural Networks dan Deep Learning Dasar |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK-5: Memahami dan menerapkan arsitektur neural network dasar |
| **Sub-CPMK** | 11.1 Menjelaskan arsitektur neural network (perceptron, MLP, activation functions, backpropagation) |
| | 11.2 Menerapkan neural network untuk klasifikasi menggunakan TensorFlow/Keras |
| **Bloom's Taxonomy** | C2-C3 (Memahami-Menerapkan / *Understand-Apply*) |
| **Durasi** | 2 x 100 menit (Teori 100 min + Praktikum 100 min) |
| **Platform** | Google Colab |
| **Metode** | Ceramah interaktif, demonstrasi visual, hands-on coding, diskusi |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** inspirasi biologis di balik neural network (*neuron*, *synapse*, *signal propagation*).
2. **Memahami** cara kerja perceptron sebagai unit dasar neural network, termasuk konsep *weights*, *bias*, dan *activation function*.
3. **Menjelaskan** arsitektur Multi-Layer Perceptron (MLP) termasuk *hidden layers* dan *forward pass*.
4. **Membedakan** fungsi aktivasi (sigmoid, ReLU, softmax) serta kapan menggunakannya.
5. **Menjelaskan** intuisi backpropagation dan proses update gradient.
6. **Memahami** fungsi loss (MSE, cross-entropy) dan optimizers (SGD, Adam).
7. **Mengimplementasikan** neural network classifier menggunakan TensorFlow/Keras Sequential API.
8. **Menerapkan** teknik pencegahan overfitting (dropout, early stopping) pada model neural network.

---

## Materi Pembelajaran

### 1. Inspirasi Biologis: Neuron dan Sinapsis

#### Dari Otak ke Komputer

Neural network terinspirasi dari cara kerja otak manusia. Otak kita terdiri dari sekitar **86 miliar neuron** yang terhubung melalui **sinapsis**. Setiap neuron:

1. Menerima sinyal dari neuron lain melalui **dendrit**
2. Memproses sinyal di **badan sel** (*soma*)
3. Jika sinyal cukup kuat, mengirimkan sinyal melalui **akson** ke neuron berikutnya

```
Neuron Biologis:                  Neuron Buatan:

  Dendrit → Soma → Akson           Input → Σ(w*x + b) → f(z) → Output
     ↑                                ↑                    ↑
  Menerima                        Weighted Sum         Activation
  sinyal                                                Function
```

#### Persamaan dan Perbedaan

| Aspek | Neuron Biologis | Neuron Buatan |
|---|---|---|
| **Input** | Sinyal listrik/kimia dari sinapsis | Angka (fitur data) |
| **Pemrosesan** | Akumulasi di badan sel | Penjumlahan berbobot + bias |
| **Keputusan** | Threshold untuk firing | Activation function |
| **Output** | Sinyal ke neuron lain | Angka (prediksi) |
| **Belajar** | Penguatan/pelemahan sinapsis | Update bobot (weights) |

> **Catatan:** Neural network buatan adalah penyederhanaan besar dari otak biologis. Analogi ini membantu intuisi, tetapi cara kerja sebenarnya sangat berbeda. Otak jauh lebih kompleks!

---

### 2. Perceptron: Single Neuron

#### Model Perceptron

**Perceptron** adalah unit paling sederhana dari neural network — sebuah neuron tunggal. Diperkenalkan oleh Frank Rosenblatt pada tahun 1958.

```
Input           Weight     Sum + Bias    Activation    Output

x₁ ──── w₁ ──→ ┐
                ├──→ z = Σ(wᵢxᵢ) + b ──→ f(z) ──→ ŷ
x₂ ──── w₂ ──→ ┘
                    ↑
                   bias (b)
```

**Formulasi matematika:**

$$z = w_1 x_1 + w_2 x_2 + ... + w_n x_n + b = \mathbf{w}^T \mathbf{x} + b$$

$$\hat{y} = f(z)$$

Di mana:
- $x_i$ = input (fitur)
- $w_i$ = weight (bobot) — menentukan pentingnya setiap input
- $b$ = bias — memungkinkan model menggeser keputusan
- $f$ = activation function
- $\hat{y}$ = output (prediksi)

#### Analogi Sederhana

Bayangkan Anda memutuskan apakah akan membeli makanan online:

| Faktor (Input) | Bobot (Weight) | Nilai |
|---|---|---|
| Harga terjangkau? ($x_1$) | $w_1 = 0.4$ | Ya (1) |
| Rating tinggi? ($x_2$) | $w_2 = 0.3$ | Ya (1) |
| Jarak dekat? ($x_3$) | $w_3 = 0.3$ | Tidak (0) |

$$z = 0.4(1) + 0.3(1) + 0.3(0) + (-0.2) = 0.5$$

Jika threshold = 0.5, maka keputusan: **Beli!**

---

### 3. Multi-Layer Perceptron (MLP): Hidden Layers dan Forward Pass

#### Dari Single Neuron ke Network

Satu perceptron hanya bisa menangani masalah yang **linearly separable**. Untuk masalah kompleks, kita menumpuk banyak neuron dalam beberapa lapisan — inilah **Multi-Layer Perceptron (MLP)**.

```
Input Layer      Hidden Layer 1    Hidden Layer 2    Output Layer
(fitur)          (neuron)          (neuron)          (prediksi)

  x₁ ─────────→ ○ ────────────→ ○ ────────────→ ○ → ŷ₁
       ╲       ╱ ╲             ╱ ╲             ╱
        ╲     ╱   ╲           ╱   ╲           ╱
  x₂ ───╲───╱─→ ○ ──╲───────╱─→ ○ ──────────→ ○ → ŷ₂
          ╲ ╱       ╲ ╲     ╱       ╲         ╱
           ╳         ╲ ╲   ╱         ╲       ╱
          ╱ ╲         ╲ ╲ ╱           ╲     ╱
  x₃ ───╱───╲─→ ○ ────╲╱────────→ ○ ──────→ ○ → ŷ₃
       ╱       ╲       ╱╲             ╲
      ╱         ╲     ╱  ╲             ╲
  x₄ ─────────→ ○ ──╱────╲──────→ ○

  4 input       4 neuron     4 neuron       3 output
```

#### Terminologi Penting

| Istilah | Penjelasan |
|---|---|
| **Input Layer** | Menerima data fitur (bukan neuron sebenarnya) |
| **Hidden Layer** | Lapisan neuron yang melakukan komputasi — disebut "hidden" karena tidak terlihat dari luar |
| **Output Layer** | Menghasilkan prediksi akhir |
| **Deep Learning** | Neural network dengan **lebih dari satu hidden layer** |
| **Forward Pass** | Proses menghitung output dari input → hidden → output |

#### Forward Pass

Proses forward pass menghitung prediksi secara bertahap:

```
Input → Hidden Layer 1:  h₁ = f(W₁ · x + b₁)
Hidden 1 → Hidden 2:     h₂ = f(W₂ · h₁ + b₂)
Hidden 2 → Output:       ŷ  = f(W₃ · h₂ + b₃)
```

Setiap koneksi antar neuron memiliki weight-nya sendiri. Network dengan 4 input, 2 hidden layers (masing-masing 4 neuron), dan 3 output memiliki: $(4 \times 4) + (4 \times 4) + (4 \times 3) = 44$ weights + bias.

---

### 4. Activation Functions: Sigmoid, ReLU, Softmax

#### Mengapa Activation Function Diperlukan?

Tanpa activation function, neural network hanyalah **transformasi linear bertingkat** — yang sama saja dengan satu transformasi linear. Activation function memberikan **non-linearitas** sehingga network bisa mempelajari pola kompleks.

#### a) Sigmoid

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

```
Output
1.0 |          ___________
    |        /
0.5 |-------/------------- ← z = 0 → output = 0.5
    |      /
0.0 |_____/
    ──────────────────── z
   -6    -3    0    3    6
```

- **Range:** (0, 1) — cocok untuk probabilitas
- **Kapan digunakan:** Output layer untuk klasifikasi biner
- **Kelemahan:** Vanishing gradient pada nilai ekstrem

#### b) ReLU (Rectified Linear Unit)

$$\text{ReLU}(z) = \max(0, z)$$

```
Output
    |            /
    |           /
    |          /
    |         /
0.0 |________/ ← z = 0
    ──────────────────── z
   -6   -3    0    3    6
```

- **Range:** [0, ∞) — tidak dibatasi di atas
- **Kapan digunakan:** Hidden layers (default paling populer)
- **Keunggulan:** Cepat, mengatasi vanishing gradient
- **Kelemahan:** "Dying ReLU" — neuron bisa mati (selalu 0)

#### c) Softmax

$$\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j} e^{z_j}}$$

- **Range:** (0, 1), jumlah semua output = 1
- **Kapan digunakan:** Output layer untuk klasifikasi multi-kelas
- **Hasil:** Distribusi probabilitas atas semua kelas

#### Ringkasan Pemilihan Activation Function

| Lokasi | Masalah | Activation Function |
|---|---|---|
| Hidden layer | Umum | **ReLU** (default) |
| Output layer | Klasifikasi biner | **Sigmoid** |
| Output layer | Klasifikasi multi-kelas | **Softmax** |
| Output layer | Regresi | **Linear** (tanpa activation) |

---

### 5. Backpropagation: Intuisi dan Gradient Update

#### Bagaimana Neural Network Belajar?

Proses belajar neural network terdiri dari dua tahap yang diulang:

```
Forward Pass:  Input → Prediksi (ŷ)
                          ↓
              Hitung Loss: L = loss(y, ŷ)
                          ↓
Backward Pass: Hitung gradient: ∂L/∂w untuk setiap weight
                          ↓
Update:        w_baru = w_lama - learning_rate × ∂L/∂w
```

#### Intuisi Backpropagation

Bayangkan Anda bermain panahan dengan mata tertutup:

1. **Forward pass:** Anda melepas anak panah (membuat prediksi)
2. **Loss:** Seseorang memberitahu seberapa jauh dari target (menghitung error)
3. **Backward pass:** Anda menganalisis apa yang perlu diperbaiki — sudut tangan? Kekuatan tarikan? (menghitung gradient)
4. **Update:** Anda menyesuaikan teknik untuk tembakan berikutnya (update weights)

Proses ini diulang ribuan kali hingga anak panah mendekati target!

#### Chain Rule

Backpropagation menggunakan **chain rule** dari kalkulus untuk menghitung gradient secara efisien dari output kembali ke input:

$$\frac{\partial L}{\partial w_1} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial h_2} \cdot \frac{\partial h_2}{\partial h_1} \cdot \frac{\partial h_1}{\partial w_1}$$

> **Tidak perlu menghitung manual!** TensorFlow/Keras melakukan backpropagation secara otomatis (*automatic differentiation*). Yang penting adalah memahami **intuisinya**.

---

### 6. Loss Functions: MSE dan Cross-Entropy

#### Mengapa Loss Function Penting?

Loss function mengukur **seberapa buruk** prediksi model dibandingkan nilai sebenarnya. Tujuan training adalah **meminimalkan** loss.

#### a) Mean Squared Error (MSE) — Untuk Regresi

$$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

- Mengukur rata-rata kuadrat selisih antara prediksi dan nilai sebenarnya
- Sensitif terhadap outlier (karena dikuadratkan)

#### b) Cross-Entropy Loss — Untuk Klasifikasi

**Binary Cross-Entropy** (2 kelas):

$$L = -\frac{1}{n} \sum_{i=1}^{n} [y_i \log(\hat{y}_i) + (1-y_i) \log(1-\hat{y}_i)]$$

**Categorical Cross-Entropy** (multi-kelas):

$$L = -\frac{1}{n} \sum_{i=1}^{n} \sum_{c=1}^{C} y_{i,c} \log(\hat{y}_{i,c})$$

| Masalah | Loss Function | Output Activation |
|---|---|---|
| Regresi | MSE | Linear |
| Klasifikasi biner | Binary Cross-Entropy | Sigmoid |
| Klasifikasi multi-kelas | Categorical Cross-Entropy | Softmax |

---

### 7. Optimizers: SGD dan Adam

#### Optimizer Menentukan Cara Update Weight

| Optimizer | Deskripsi | Kapan Digunakan |
|---|---|---|
| **SGD** (Stochastic Gradient Descent) | Update weight setiap batch kecil data | Sederhana, baseline |
| **SGD + Momentum** | SGD dengan "inersia" untuk melewati lokal minimum | Peningkatan dari SGD |
| **Adam** (Adaptive Moment Estimation) | Kombinasi momentum + adaptive learning rate | **Default terbaik** untuk kebanyakan kasus |
| **RMSprop** | Adaptive learning rate | Cocok untuk data non-stationary |

#### Learning Rate

**Learning rate (α)** mengontrol seberapa besar langkah update weight:

```
Learning rate terlalu besar:        Learning rate tepat:         Learning rate terlalu kecil:
     Loss                              Loss                          Loss
      |  *                              |  *                          |  *
      | * *                             | *                           | *
      |*   *                            |  *                          |  *
      |     *  * * *                    |   *                         |   *
      |                                 |    * * * → konvergen        |    *
      +──────────── epoch               +──────────── epoch           |     *
      (oscillate, tidak konvergen)      (konvergen dengan baik)       +──── epoch
                                                                      (sangat lambat)
```

> **Tips:** Gunakan **Adam** sebagai default optimizer. Learning rate default Adam (0.001) biasanya cukup baik untuk memulai.

---

### 8. Membangun Neural Network dengan TensorFlow/Keras

#### Keras Sequential API

**Keras** adalah API tingkat tinggi untuk membangun neural network. **Sequential API** adalah cara paling sederhana — menumpuk layer satu per satu.

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

model = Sequential([
    Dense(128, activation='relu', input_shape=(784,)),  # Hidden layer 1
    Dense(64, activation='relu'),                        # Hidden layer 2
    Dense(10, activation='softmax')                      # Output layer
])
```

#### Langkah Membangun Model

```
1. Definisikan arsitektur (Sequential + Dense layers)
           ↓
2. Compile model (optimizer, loss, metrics)
           ↓
3. Training model (fit dengan data training)
           ↓
4. Evaluasi model (evaluate dengan data test)
           ↓
5. Prediksi (predict pada data baru)
```

---

### 9. Training: Epochs, Batch Size, Validation Split

#### Parameter Training Penting

| Parameter | Deskripsi | Nilai Umum |
|---|---|---|
| **Epochs** | Berapa kali model melihat seluruh dataset | 10-100 |
| **Batch Size** | Jumlah sampel per update weight | 32, 64, 128 |
| **Validation Split** | Proporsi data untuk validasi selama training | 0.1-0.2 (10-20%) |

#### Analogi

- **Epoch** = membaca buku dari awal sampai akhir satu kali
- **Batch** = membaca satu bab pada satu waktu
- **10 epochs, batch size 32** = membaca buku 10 kali, setiap kali membaca 32 halaman sebelum merangkum

---

### 10. Pencegahan Overfitting: Dropout dan Early Stopping

#### Overfitting pada Neural Network

Neural network sangat rentan overfitting karena jumlah parameter yang besar. Tanda-tanda overfitting:

```
Loss                               Accuracy
  |  Training ────────→             |           ──── Training
  |                                 |          /
  |  Validation ─────╲             |         / ──── Validation
  |                    ╲            |        /  ╲
  |                     ╲           |       /    ╲──────
  +─────────────── epoch            +─────────────── epoch
  ↑ Gap semakin besar               ↑ Training naik, Validation turun
    = OVERFITTING                     = OVERFITTING
```

#### a) Dropout

**Dropout** secara acak menonaktifkan sejumlah neuron selama training:

```
Tanpa Dropout:              Dengan Dropout (rate=0.3):
○ ─── ○ ─── ○              ○ ─── ○ ─── ○
○ ─── ○ ─── ○              ○ ─── ╳ ─── ○    ← dimatikan (30%)
○ ─── ○ ─── ○              ╳ ─── ○ ─── ○    ← dimatikan
○ ─── ○ ─── ○              ○ ─── ○ ─── ╳

→ Model tidak bergantung pada neuron tertentu
→ Memaksa model belajar fitur yang lebih robust
```

```python
model.add(Dropout(0.3))  # Matikan 30% neuron secara acak saat training
```

#### b) Early Stopping

**Early stopping** menghentikan training ketika performa validasi mulai menurun:

```python
from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(
    monitor='val_loss',    # Pantau validation loss
    patience=5,            # Tunggu 5 epoch tanpa perbaikan
    restore_best_weights=True  # Kembalikan bobot terbaik
)
```

---

## Aktivitas Kelas

### Sesi 1: Teori dan Diskusi (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Pembukaan & Review | Review unsupervised learning, transisi ke neural networks |
| 15 menit | Ceramah: Inspirasi Biologis & Perceptron | Neuron, weights, bias, activation — demo interaktif |
| 15 menit | Ceramah: MLP & Forward Pass | Hidden layers, arsitektur, forward propagation |
| 15 menit | Ceramah: Activation Functions | Sigmoid, ReLU, softmax — visualisasi dan perbandingan |
| 15 menit | Ceramah: Backpropagation & Loss | Intuisi gradient descent, MSE, cross-entropy |
| 10 menit | Ceramah: Optimizer & Overfitting | SGD, Adam, dropout, early stopping |
| 10 menit | Diskusi: Kapan Deep Learning? | Diskusi tentang kapan deep learning diperlukan vs ML tradisional |
| 10 menit | Rangkuman & Transisi | Key takeaways, persiapan hands-on |

### Sesi 2: Hands-on Praktikum (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Setup & Install | Google Colab, install TensorFlow, load MNIST |
| 25 menit | Membangun Model | Arsitektur MLP, compile, summary |
| 25 menit | Training & Evaluasi | Fit model, plot loss/accuracy, evaluasi |
| 20 menit | Eksperimen | Variasi arsitektur, dropout, early stopping |
| 10 menit | Visualisasi & Interpretasi | Confusion matrix, prediksi salah |
| 10 menit | Wrap-up & Preview | Rangkuman, penjelasan tugas, preview minggu depan |

---

## Hands-on: Neural Network Classifier untuk MNIST Digits

### Langkah 1: Import Library dan Setup

```python
# Import library yang diperlukan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, classification_report
import warnings
warnings.filterwarnings('ignore')

# Cek versi TensorFlow
print(f"TensorFlow versi: {tf.__version__}")
print(f"GPU tersedia: {tf.config.list_physical_devices('GPU')}")

# Mengatur style visualisasi
plt.style.use('seaborn-v0_8')
```

### Langkah 2: Load dan Eksplorasi Dataset MNIST

```python
# Load MNIST dataset (sudah tersedia di Keras)
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

print("=== Informasi Dataset MNIST ===")
print(f"Training set: {X_train.shape[0]} gambar, ukuran {X_train.shape[1]}x{X_train.shape[2]}")
print(f"Test set: {X_test.shape[0]} gambar")
print(f"Kelas: digit 0-9")
print(f"Nilai pixel: {X_train.min()} - {X_train.max()}")

# Visualisasi contoh digit
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_train[i], cmap='gray')
    ax.set_title(f'Label: {y_train[i]}', fontsize=12)
    ax.axis('off')
plt.suptitle('Contoh Gambar Digit MNIST', fontsize=14)
plt.tight_layout()
plt.show()

# Distribusi kelas
print("\n=== Distribusi Kelas (Training) ===")
unique, counts = np.unique(y_train, return_counts=True)
for digit, count in zip(unique, counts):
    print(f"  Digit {digit}: {count} gambar ({count/len(y_train)*100:.1f}%)")
```

### Langkah 3: Preprocessing Data

```python
# Preprocessing MNIST untuk neural network

# 1. Reshape: dari 28x28 gambar ke vektor 784 dimensi
X_train_flat = X_train.reshape(X_train.shape[0], -1)  # (60000, 784)
X_test_flat = X_test.reshape(X_test.shape[0], -1)      # (10000, 784)

# 2. Normalisasi: skala pixel dari [0, 255] ke [0, 1]
X_train_norm = X_train_flat.astype('float32') / 255.0
X_test_norm = X_test_flat.astype('float32') / 255.0

# 3. One-hot encoding untuk label (diperlukan untuk categorical cross-entropy)
y_train_onehot = to_categorical(y_train, num_classes=10)
y_test_onehot = to_categorical(y_test, num_classes=10)

print("=== Setelah Preprocessing ===")
print(f"X_train shape: {X_train_norm.shape}")
print(f"X_test shape: {X_test_norm.shape}")
print(f"y_train (one-hot) shape: {y_train_onehot.shape}")
print(f"Contoh one-hot digit 5: {y_train_onehot[0]}")
print(f"Nilai pixel setelah normalisasi: [{X_train_norm.min():.1f}, {X_train_norm.max():.1f}]")
```

### Langkah 4: Membangun Arsitektur Neural Network

```python
# Membangun model neural network dengan Sequential API
model = Sequential([
    # Input layer + Hidden layer 1: 128 neuron, ReLU
    Dense(128, activation='relu', input_shape=(784,), name='hidden_1'),
    Dropout(0.2, name='dropout_1'),  # Dropout 20% untuk mencegah overfitting

    # Hidden layer 2: 64 neuron, ReLU
    Dense(64, activation='relu', name='hidden_2'),
    Dropout(0.2, name='dropout_2'),

    # Output layer: 10 neuron (digit 0-9), Softmax
    Dense(10, activation='softmax', name='output')
])

# Tampilkan arsitektur model
print("=== Arsitektur Model ===")
model.summary()

# Hitung total parameter
total_params = model.count_params()
print(f"\nTotal parameter yang harus dipelajari: {total_params:,}")
print("Ini berarti neural network harus menemukan {total_params:,} nilai optimal!")
```

### Langkah 5: Compile dan Training Model

```python
# Compile model
model.compile(
    optimizer='adam',                        # Optimizer: Adam
    loss='categorical_crossentropy',         # Loss: Categorical Cross-Entropy
    metrics=['accuracy']                     # Metrik: Accuracy
)

# Early stopping callback
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True,
    verbose=1
)

# Training model
print("=== Memulai Training ===\n")
history = model.fit(
    X_train_norm, y_train_onehot,
    epochs=30,
    batch_size=64,
    validation_split=0.15,      # 15% data training untuk validasi
    callbacks=[early_stop],
    verbose=1
)

print("\nTraining selesai!")
```

### Langkah 6: Visualisasi Proses Training

```python
# Plot training history
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Loss
axes[0].plot(history.history['loss'], label='Training Loss', linewidth=2)
axes[0].plot(history.history['val_loss'], label='Validation Loss', linewidth=2)
axes[0].set_xlabel('Epoch', fontsize=12)
axes[0].set_ylabel('Loss', fontsize=12)
axes[0].set_title('Loss selama Training', fontsize=14)
axes[0].legend(fontsize=11)
axes[0].grid(True, alpha=0.3)

# Accuracy
axes[1].plot(history.history['accuracy'], label='Training Accuracy', linewidth=2)
axes[1].plot(history.history['val_accuracy'], label='Validation Accuracy', linewidth=2)
axes[1].set_xlabel('Epoch', fontsize=12)
axes[1].set_ylabel('Accuracy', fontsize=12)
axes[1].set_title('Accuracy selama Training', fontsize=14)
axes[1].legend(fontsize=11)
axes[1].grid(True, alpha=0.3)

plt.suptitle('Training History — Neural Network MNIST', fontsize=15, y=1.02)
plt.tight_layout()
plt.show()

# Menampilkan best epoch
best_epoch = np.argmin(history.history['val_loss']) + 1
print(f"Best epoch: {best_epoch}")
print(f"Best validation loss: {min(history.history['val_loss']):.4f}")
print(f"Best validation accuracy: {history.history['val_accuracy'][best_epoch-1]:.4f}")
```

### Langkah 7: Evaluasi Model pada Test Set

```python
# Evaluasi pada test set
test_loss, test_accuracy = model.evaluate(X_test_norm, y_test_onehot, verbose=0)

print(f"=== Evaluasi pada Test Set ===")
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")

# Prediksi
y_pred_proba = model.predict(X_test_norm, verbose=0)
y_pred = np.argmax(y_pred_proba, axis=1)

# Classification report
print(f"\n=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=[str(i) for i in range(10)]))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=range(10), yticklabels=range(10))
plt.xlabel('Prediksi', fontsize=12)
plt.ylabel('Label Sebenarnya', fontsize=12)
plt.title('Confusion Matrix — MNIST Neural Network', fontsize=14)
plt.tight_layout()
plt.show()
```

### Langkah 8: Visualisasi Prediksi Salah

```python
# Temukan prediksi yang salah
wrong_indices = np.where(y_pred != y_test)[0]
print(f"Jumlah prediksi salah: {len(wrong_indices)} dari {len(y_test)} "
      f"({len(wrong_indices)/len(y_test)*100:.2f}%)")

# Visualisasi beberapa prediksi salah
n_show = 10
fig, axes = plt.subplots(2, 5, figsize=(15, 6))
for i, ax in enumerate(axes.flat):
    if i < len(wrong_indices):
        idx = wrong_indices[i]
        ax.imshow(X_test[idx], cmap='gray')
        ax.set_title(
            f'True: {y_test[idx]}, Pred: {y_pred[idx]}\n'
            f'Conf: {y_pred_proba[idx][y_pred[idx]]:.2%}',
            fontsize=10, color='red'
        )
    ax.axis('off')
plt.suptitle('Contoh Prediksi SALAH', fontsize=14, color='red')
plt.tight_layout()
plt.show()

print("\nRefleksi: Perhatikan digit mana yang sering salah diprediksi.")
print("Biasanya digit 3-5, 4-9, 7-1 sering tertukar karena mirip secara visual.")
```

### Langkah 9: Eksperimen — Variasi Arsitektur

```python
# Eksperimen: bandingkan arsitektur berbeda
def build_model(hidden_layers, dropout_rate=0.2):
    """Membuat model dengan arsitektur tertentu"""
    model = Sequential()
    model.add(Dense(hidden_layers[0], activation='relu', input_shape=(784,)))
    model.add(Dropout(dropout_rate))

    for units in hidden_layers[1:]:
        model.add(Dense(units, activation='relu'))
        model.add(Dropout(dropout_rate))

    model.add(Dense(10, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Eksperimen dengan 3 arsitektur berbeda
architectures = {
    'Kecil (64)': [64],
    'Sedang (128-64)': [128, 64],
    'Besar (256-128-64)': [256, 128, 64]
}

print("=== Eksperimen Arsitektur ===\n")
for name, layers in architectures.items():
    model_exp = build_model(layers)
    history_exp = model_exp.fit(
        X_train_norm, y_train_onehot,
        epochs=15, batch_size=64,
        validation_split=0.15, verbose=0
    )
    _, acc = model_exp.evaluate(X_test_norm, y_test_onehot, verbose=0)
    n_params = model_exp.count_params()
    print(f"  {name:25s}: Accuracy = {acc:.4f}, Parameters = {n_params:,}")
```

---

## AI Corner: Menggunakan AI untuk Debug Arsitektur Neural Network

> **Level: Advanced** — Pada minggu ini, kita menggunakan AI untuk membantu mendesain dan men-debug arsitektur neural network.

### Skenario Penggunaan AI

| Skenario | Contoh Prompt ke AI |
|---|---|
| Desain arsitektur | *"Saya ingin membangun neural network untuk klasifikasi gambar 28x28 grayscale ke 10 kelas. Sarankan arsitektur MLP yang tepat."* |
| Memilih hyperparameter | *"Model saya overfitting pada epoch 10. Training accuracy 99% tapi validation 92%. Apa yang harus saya lakukan?"* |
| Debugging error | *"Error: shapes (None, 784) and (None, 28, 28) are not compatible. Bagaimana cara memperbaiki?"* |
| Interpretasi hasil | *"Confusion matrix saya menunjukkan digit 3 dan 5 sering tertukar. Mengapa dan bagaimana solusinya?"* |
| Optimasi | *"Model saya hanya 95% accuracy pada MNIST. Apa yang bisa saya lakukan untuk meningkatkannya tanpa CNN?"* |

### Contoh Prompt Minggu Ini

```
Saya membangun neural network pertama saya untuk MNIST digit classification
menggunakan Keras Sequential API. Berikut arsitektur saya:
- Input: 784 (28x28 flattened)
- Hidden 1: Dense(128, relu) + Dropout(0.2)
- Hidden 2: Dense(64, relu) + Dropout(0.2)
- Output: Dense(10, softmax)

Training accuracy: 98%, Validation accuracy: 97%, Test accuracy: 97%

Pertanyaan:
1. Apakah arsitektur ini sudah baik untuk MNIST?
2. Bagaimana cara meningkatkan akurasi ke >99%?
3. Apa bedanya menggunakan MLP vs CNN untuk masalah ini?
4. Kapan saya harus menambah layer vs menambah neuron?
```

### Tips Penting

1. **Mulai sederhana** — jangan langsung membuat network yang sangat dalam.
2. **AI sangat membantu** untuk debugging error shape dan dimensi.
3. **Selalu validasi** saran arsitektur AI dengan eksperimen.
4. **Pahami konsep** sebelum copy-paste kode dari AI.

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai bahan refleksi:

1. **Inspirasi Biologis:** Seberapa mirip neural network buatan dengan otak manusia? Apa batasan utama analogi ini?

2. **Kapan Deep Learning?** Tidak semua masalah membutuhkan deep learning. Berikan contoh masalah di Indonesia di mana (a) deep learning diperlukan dan (b) model ML tradisional sudah cukup.

3. **Overfitting:** Jelaskan dengan kata-kata Anda sendiri mengapa dropout bisa mencegah overfitting. Gunakan analogi jika membantu.

4. **Etika AI:** Neural network sering disebut "black box" karena sulit diinterpretasi. Bagaimana ini bisa menjadi masalah etika, misalnya jika digunakan untuk keputusan kredit atau rekrutmen di Indonesia?

5. **Computational Cost:** Melatih neural network besar membutuhkan energi listrik yang signifikan. Dari perspektif tanggung jawab lingkungan dan nilai Islam tentang menjaga bumi (*khalifah fil ardh*), bagaimana seharusnya kita menyikapi ini?

---

## Tugas Mandiri — T6: Neural Network untuk Klasifikasi (Keras)

### Deskripsi Tugas

Bangun sebuah neural network classifier menggunakan TensorFlow/Keras dengan ketentuan berikut:

1. **Dataset:** Pilih salah satu:
   - MNIST Fashion (`tensorflow.keras.datasets.fashion_mnist`) — klasifikasi pakaian
   - CIFAR-10 (`tensorflow.keras.datasets.cifar10`) — klasifikasi objek (lebih menantang)

2. **Preprocessing:**
   - Reshape dan normalisasi data gambar
   - One-hot encoding untuk label
   - Split training dan validation

3. **Model:**
   - Bangun arsitektur MLP dengan minimal 2 hidden layers
   - Gunakan activation function yang tepat
   - Terapkan dropout untuk mencegah overfitting

4. **Training:**
   - Gunakan optimizer Adam
   - Terapkan early stopping
   - Catat training history (loss dan accuracy)

5. **Evaluasi & Analisis:**
   - Plot training/validation loss dan accuracy
   - Buat confusion matrix
   - Analisis digit/kelas mana yang paling sulit diklasifikasikan
   - Eksperimen dengan minimal 2 arsitektur berbeda dan bandingkan hasilnya

6. **Bonus:** Coba tingkatkan akurasi melalui eksperimen hyperparameter tuning

### Ketentuan Pengumpulan

- **Format:** Notebook Google Colab (.ipynb)
- **Deadline:** Minggu 12 (sebelum perkuliahan)
- **Bobot:** Bagian dari komponen Tugas Individu
- **AI Policy:** Penggunaan AI diizinkan dengan mencantumkan log penggunaan AI. Mahasiswa wajib bisa menjelaskan setiap bagian kode.

---

## Referensi

### Buku Teks

1. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media. — Chapter 10: Introduction to Artificial Neural Networks with Keras.
2. Chollet, F. (2021). *Deep Learning with Python* (2nd ed.). Manning Publications. — Chapter 2-4.
3. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press. — Chapter 6: Deep Feedforward Networks.

### Sumber Online

4. [TensorFlow Tutorials](https://www.tensorflow.org/tutorials) — Tutorial resmi TensorFlow.
5. [Keras Documentation](https://keras.io/) — Dokumentasi resmi Keras API.
6. [3Blue1Brown: Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — Seri video visual yang sangat bagus tentang neural network.
7. [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) — Kursus gratis dari Google.

### Referensi Indonesia

8. [Dicoding: Belajar Machine Learning](https://www.dicoding.com/academies/184) — Platform belajar ML berbahasa Indonesia.

---

> **Preview Minggu Depan:** Kita akan membahas **Natural Language Processing (NLP) Dasar** — memproses teks, tokenization, TF-IDF, dan membangun sistem sentiment analysis untuk teks bahasa Indonesia.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
