# Lab 11: Neural Network dengan Keras

**Mata Kuliah:** Kecerdasan Buatan dan Machine Learning
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Minggu:** 11
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

- Membangun perceptron sederhana dari nol menggunakan NumPy
- Menggunakan Keras Sequential API untuk membangun neural network
- Melatih MLP (Multi-Layer Perceptron) untuk klasifikasi dataset Iris
- Memvisualisasikan training history (akurasi dan loss)
- Membangun model untuk klasifikasi digit MNIST
- Mengevaluasi model dengan confusion matrix pada data test
- Melakukan eksperimen arsitektur (jumlah layer, neuron, dropout)
- Menerapkan early stopping untuk mencegah overfitting

---

## Persiapan

1. Buka Google Colab notebook baru
2. Nama file: `Lab11_NamaAnda_NIM.ipynb`
3. Pastikan TensorFlow/Keras sudah tersedia (pre-installed di Google Colab)
4. Verifikasi dengan: `import tensorflow as tf; print(tf.__version__)`

---

## Langkah-langkah

### Langkah 1: Perceptron dari Nol (Pure NumPy)

```python
# =============================================
# LANGKAH 1: Perceptron dari Nol (NumPy)
# =============================================

import numpy as np
import matplotlib.pyplot as plt

# --- Implementasi Perceptron Sederhana ---
class PerceptronSederhana:
    """Perceptron sederhana dengan fungsi aktivasi sigmoid."""

    def __init__(self, n_input):
        # Inisialisasi bobot secara acak
        np.random.seed(42)
        self.weights = np.random.randn(n_input) * 0.01
        self.bias = 0.0

    def sigmoid(self, z):
        """Fungsi aktivasi sigmoid: 1 / (1 + e^(-z))"""
        return 1.0 / (1.0 + np.exp(-np.clip(z, -500, 500)))

    def forward(self, X):
        """Forward pass: hitung output"""
        z = np.dot(X, self.weights) + self.bias
        return self.sigmoid(z)

    def predict(self, X, threshold=0.5):
        """Prediksi kelas (0 atau 1)"""
        return (self.forward(X) >= threshold).astype(int)

    def train(self, X, y, learning_rate=0.1, epochs=100):
        """Latih perceptron dengan gradient descent"""
        losses = []
        for epoch in range(epochs):
            # Forward pass
            output = self.forward(X)

            # Hitung error (binary cross-entropy)
            loss = -np.mean(y * np.log(output + 1e-8) +
                           (1 - y) * np.log(1 - output + 1e-8))
            losses.append(loss)

            # Backward pass (gradient)
            error = output - y
            grad_w = np.dot(X.T, error) / len(y)
            grad_b = np.mean(error)

            # Update bobot
            self.weights -= learning_rate * grad_w
            self.bias -= learning_rate * grad_b

            if (epoch + 1) % 20 == 0:
                acc = np.mean(self.predict(X) == y)
                print(f"Epoch {epoch+1:3d}: Loss = {loss:.4f}, Akurasi = {acc:.4f}")

        return losses

# --- Data: Gerbang logika OR ---
X_or = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_or = np.array([0, 1, 1, 1])

print("=== PERCEPTRON SEDERHANA — Gerbang OR ===\n")
p = PerceptronSederhana(n_input=2)
losses = p.train(X_or, y_or, learning_rate=1.0, epochs=100)

# Hasil prediksi
print("\n--- Hasil Prediksi ---")
for x, y_true in zip(X_or, y_or):
    y_pred = p.predict(x.reshape(1, -1))[0]
    prob = p.forward(x.reshape(1, -1))[0]
    print(f"  Input: {x} -> Prediksi: {y_pred} (prob: {prob:.4f}), Aktual: {y_true}")

# Plot loss
plt.figure(figsize=(8, 4))
plt.plot(losses, color='steelblue', linewidth=2)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss — Perceptron Sederhana')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 2: Pengenalan Keras Sequential API

```python
# =============================================
# LANGKAH 2: Keras Sequential API
# =============================================

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print(f"TensorFlow version: {tf.__version__}")

# Contoh sederhana: membangun model Sequential
model_demo = keras.Sequential([
    layers.Dense(8, activation='relu', input_shape=(2,), name='hidden_1'),
    layers.Dense(4, activation='relu', name='hidden_2'),
    layers.Dense(1, activation='sigmoid', name='output')
])

# Tampilkan arsitektur model
model_demo.summary()

print("\nPenjelasan:")
print("- Dense: layer fully-connected (setiap neuron terhubung ke semua input)")
print("- activation='relu': fungsi aktivasi ReLU (max(0, x))")
print("- activation='sigmoid': output antara 0 dan 1 (untuk klasifikasi biner)")
print("- input_shape=(2,): model menerima 2 fitur sebagai input")
```

### Langkah 3: MLP untuk Klasifikasi Iris

```python
# =============================================
# LANGKAH 3: MLP — Klasifikasi Iris
# =============================================

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import to_categorical

# Muat dan persiapkan data Iris
iris = load_iris()
X = iris.data
y = iris.target

# Standardisasi fitur
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

# One-hot encoding untuk label (3 kelas)
y_train_onehot = to_categorical(y_train, num_classes=3)
y_test_onehot = to_categorical(y_test, num_classes=3)

print(f"Training set: {X_train.shape[0]} sampel")
print(f"Test set: {X_test.shape[0]} sampel")
print(f"Shape y_train_onehot: {y_train_onehot.shape}")

# Bangun model MLP
model_iris = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(4,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(3, activation='softmax')  # 3 kelas output
])

# Compile model
model_iris.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model_iris.summary()

# Latih model
print("\n=== TRAINING ===")
history = model_iris.fit(
    X_train, y_train_onehot,
    epochs=100,
    batch_size=16,
    validation_split=0.2,
    verbose=1
)

# Evaluasi pada test set
test_loss, test_acc = model_iris.evaluate(X_test, y_test_onehot, verbose=0)
print(f"\n=== EVALUASI TEST SET ===")
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_acc:.4f}")
```

### Langkah 4: Plot Training History

```python
# =============================================
# LANGKAH 4: Visualisasi Training History
# =============================================

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot Akurasi
axes[0].plot(history.history['accuracy'], label='Training', linewidth=2)
axes[0].plot(history.history['val_accuracy'], label='Validation', linewidth=2)
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Accuracy')
axes[0].set_title('Akurasi Training vs Validation')
axes[0].legend()
axes[0].grid(alpha=0.3)

# Plot Loss
axes[1].plot(history.history['loss'], label='Training', linewidth=2)
axes[1].plot(history.history['val_loss'], label='Validation', linewidth=2)
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Loss')
axes[1].set_title('Loss Training vs Validation')
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.suptitle('Training History — MLP Iris Classification', fontsize=14)
plt.tight_layout()
plt.show()

print("Interpretasi:")
print("- Jika val_loss naik sementara loss turun -> overfitting")
print("- Jika keduanya turun dan konvergen -> model belajar dengan baik")
print("- Gap besar antara training dan validation -> overfitting")
```

### Langkah 5: Klasifikasi Digit MNIST

```python
# =============================================
# LANGKAH 5: Klasifikasi Digit MNIST
# =============================================

# Muat dataset MNIST
(X_train_mnist, y_train_mnist), (X_test_mnist, y_test_mnist) = \
    keras.datasets.mnist.load_data()

print("=== DATASET MNIST ===")
print(f"Training: {X_train_mnist.shape}")
print(f"Test: {X_test_mnist.shape}")
print(f"Kelas: digit 0-9")

# Preprocessing
# Normalisasi pixel (0-255) menjadi (0-1)
X_train_norm = X_train_mnist.astype('float32') / 255.0
X_test_norm = X_test_mnist.astype('float32') / 255.0

# Reshape: (28, 28) -> (28, 28, 1) untuk input model
X_train_reshaped = X_train_norm.reshape(-1, 28, 28, 1)
X_test_reshaped = X_test_norm.reshape(-1, 28, 28, 1)

# One-hot encoding label
y_train_cat = to_categorical(y_train_mnist, 10)
y_test_cat = to_categorical(y_test_mnist, 10)

# Visualisasi sampel digit
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_train_mnist[i], cmap='gray')
    ax.set_title(f'Label: {y_train_mnist[i]}', fontsize=11)
    ax.axis('off')
plt.suptitle('Sampel Digit MNIST', fontsize=14)
plt.tight_layout()
plt.show()

# Bangun model (MLP dengan Flatten)
model_mnist = keras.Sequential([
    layers.Flatten(input_shape=(28, 28, 1)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

model_mnist.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model_mnist.summary()

# Latih model
print("\n=== TRAINING MNIST ===")
history_mnist = model_mnist.fit(
    X_train_reshaped, y_train_cat,
    epochs=15,
    batch_size=128,
    validation_split=0.1,
    verbose=1
)
```

### Langkah 6: Evaluasi pada Test Set

```python
# =============================================
# LANGKAH 6: Evaluasi Model MNIST
# =============================================

from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

# Evaluasi
test_loss, test_acc = model_mnist.evaluate(X_test_reshaped, y_test_cat, verbose=0)
print(f"=== EVALUASI MNIST TEST SET ===")
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_acc:.4f}")

# Prediksi
y_pred_prob = model_mnist.predict(X_test_reshaped)
y_pred = np.argmax(y_pred_prob, axis=1)

# Confusion Matrix
cm = confusion_matrix(y_test_mnist, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=range(10), yticklabels=range(10))
plt.xlabel('Prediksi')
plt.ylabel('Aktual')
plt.title(f'Confusion Matrix — MNIST (Akurasi: {test_acc:.4f})')
plt.tight_layout()
plt.show()

# Classification Report
print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test_mnist, y_pred,
                            target_names=[f'Digit {i}' for i in range(10)]))
```

### Langkah 7: Eksperimen Arsitektur

```python
# =============================================
# LANGKAH 7: Eksperimen Arsitektur
# =============================================

print("=" * 60)
print("EKSPERIMEN ARSITEKTUR NEURAL NETWORK")
print("=" * 60)

# Definisikan beberapa arsitektur untuk dibandingkan
architectures = {
    'Shallow (1 layer, 64 neuron)': [64],
    'Medium (2 layer, 128-64)': [128, 64],
    'Deep (3 layer, 256-128-64)': [256, 128, 64],
    'Wide (1 layer, 512 neuron)': [512],
}

results = {}

for name, hidden_layers in architectures.items():
    print(f"\n--- {name} ---")

    # Bangun model secara dinamis
    model_exp = keras.Sequential()
    model_exp.add(layers.Flatten(input_shape=(28, 28, 1)))

    for units in hidden_layers:
        model_exp.add(layers.Dense(units, activation='relu'))
        model_exp.add(layers.Dropout(0.2))

    model_exp.add(layers.Dense(10, activation='softmax'))

    model_exp.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

    # Latih (epochs lebih sedikit untuk kecepatan)
    hist = model_exp.fit(
        X_train_reshaped, y_train_cat,
        epochs=10, batch_size=128,
        validation_split=0.1, verbose=0
    )

    # Evaluasi
    loss, acc = model_exp.evaluate(X_test_reshaped, y_test_cat, verbose=0)
    n_params = model_exp.count_params()
    results[name] = {'accuracy': acc, 'loss': loss, 'params': n_params}
    print(f"  Test Accuracy: {acc:.4f}, Parameters: {n_params:,}")

# Tabel ringkasan
print("\n=== RINGKASAN EKSPERIMEN ===")
print(f"{'Arsitektur':<35} {'Akurasi':>8} {'Loss':>8} {'Parameter':>12}")
print("-" * 65)
for name, r in results.items():
    print(f"{name:<35} {r['accuracy']:>8.4f} {r['loss']:>8.4f} {r['params']:>12,}")
```

### Langkah 8: Early Stopping Callback

```python
# =============================================
# LANGKAH 8: Early Stopping
# =============================================

from tensorflow.keras.callbacks import EarlyStopping

# Bangun model baru
model_es = keras.Sequential([
    layers.Flatten(input_shape=(28, 28, 1)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')
])

model_es.compile(optimizer='adam',
                 loss='categorical_crossentropy',
                 metrics=['accuracy'])

# Definisikan callback early stopping
early_stop = EarlyStopping(
    monitor='val_loss',       # Pantau validation loss
    patience=5,               # Berhenti jika 5 epoch tidak membaik
    restore_best_weights=True # Kembalikan bobot terbaik
)

print("=== TRAINING DENGAN EARLY STOPPING ===")
print("Monitor: val_loss, Patience: 5 epochs\n")

history_es = model_es.fit(
    X_train_reshaped, y_train_cat,
    epochs=100,              # Set banyak, early stopping akan menghentikan
    batch_size=128,
    validation_split=0.1,
    callbacks=[early_stop],
    verbose=1
)

# Berapa epoch yang dijalankan?
actual_epochs = len(history_es.history['loss'])
print(f"\nTraining berhenti pada epoch: {actual_epochs}")

# Evaluasi
loss_es, acc_es = model_es.evaluate(X_test_reshaped, y_test_cat, verbose=0)
print(f"Test Accuracy: {acc_es:.4f}")

# Plot perbandingan
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(history_es.history['accuracy'], label='Training')
axes[0].plot(history_es.history['val_accuracy'], label='Validation')
axes[0].axvline(x=actual_epochs - 5, color='red', linestyle='--',
                alpha=0.7, label=f'Best epoch (~{actual_epochs-5})')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Accuracy')
axes[0].set_title('Akurasi dengan Early Stopping')
axes[0].legend()
axes[0].grid(alpha=0.3)

axes[1].plot(history_es.history['loss'], label='Training')
axes[1].plot(history_es.history['val_loss'], label='Validation')
axes[1].axvline(x=actual_epochs - 5, color='red', linestyle='--',
                alpha=0.7, label=f'Best epoch (~{actual_epochs-5})')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Loss')
axes[1].set_title('Loss dengan Early Stopping')
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.suptitle('Training History dengan Early Stopping', fontsize=14)
plt.tight_layout()
plt.show()

print("\nKesimpulan:")
print("- Early stopping mencegah overfitting dengan menghentikan training otomatis")
print("- restore_best_weights=True memastikan model terbaik yang digunakan")
print("- Patience=5 berarti model diberi 5 epoch untuk memperbaiki performa")
```

---

## Tantangan Tambahan

1. **Perceptron XOR:** Modifikasi perceptron di Langkah 1 untuk menyelesaikan gerbang XOR. Apakah berhasil? Jelaskan mengapa perceptron single-layer tidak bisa menyelesaikan XOR (problem non-linearly separable). Tambahkan hidden layer secara manual untuk menyelesaikannya.

2. **Fashion MNIST:** Ganti MNIST digit dengan Fashion MNIST (`keras.datasets.fashion_mnist`). Bangun model MLP dan catat akurasinya. Bandingkan: apakah klasifikasi pakaian lebih sulit daripada digit? Visualisasikan sampel yang salah diklasifikasi.

3. **Learning Rate Experiment:** Latih model MNIST dengan learning rate berbeda (0.0001, 0.001, 0.01, 0.1). Plot training curve untuk setiap learning rate dalam satu grafik. Analisis dampak learning rate terhadap konvergensi dan stabilitas.

---

## Checklist Penyelesaian

- [ ] Langkah 1: Perceptron dari nol berhasil mempelajari gerbang OR
- [ ] Langkah 2: Keras Sequential API berhasil dijalankan
- [ ] Langkah 3: MLP Iris berhasil dilatih dengan akurasi > 90%
- [ ] Langkah 4: Training history (akurasi dan loss) berhasil divisualisasi
- [ ] Langkah 5: Model MNIST berhasil dilatih
- [ ] Langkah 6: Confusion matrix dan classification report berhasil dibuat
- [ ] Langkah 7: Eksperimen arsitektur berhasil membandingkan 4 konfigurasi
- [ ] Langkah 8: Early stopping berhasil menghentikan training secara otomatis
- [ ] Semua kode berjalan tanpa error di Google Colab
- [ ] Notebook disimpan dengan format `Lab11_NamaAnda_NIM.ipynb`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
