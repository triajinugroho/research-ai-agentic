# Lab 13: Image Classification dengan CNN

**Mata Kuliah:** Kecerdasan Buatan dan Machine Learning
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Minggu:** 13
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

- Memuat dataset gambar MNIST menggunakan TensorFlow/Keras
- Melakukan preprocessing gambar: reshape dan normalisasi
- Memvisualisasikan sampel gambar dari dataset
- Membangun arsitektur CNN (Conv2D, MaxPooling2D, Flatten, Dense)
- Melatih dan mengkompilasi model CNN untuk klasifikasi gambar
- Memvisualisasikan training history (akurasi dan loss)
- Mengevaluasi model dengan confusion matrix pada data test
- Memprediksi gambar individual dan memvisualisasikan hasilnya

---

## Persiapan

1. Buka Google Colab notebook baru
2. Nama file: `Lab13_NamaAnda_NIM.ipynb`
3. Pastikan TensorFlow/Keras sudah tersedia (pre-installed di Google Colab)
4. Disarankan menggunakan GPU runtime: Runtime > Change runtime type > GPU

---

## Langkah-langkah

### Langkah 1: Load Dataset MNIST

```python
# =============================================
# LANGKAH 1: Load Dataset MNIST
# =============================================

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print(f"TensorFlow version: {tf.__version__}")

# Muat dataset MNIST
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

print("=== DATASET MNIST ===")
print(f"Training images: {X_train.shape}")
print(f"Training labels: {y_train.shape}")
print(f"Test images: {X_test.shape}")
print(f"Test labels: {y_test.shape}")
print(f"\nUkuran gambar: {X_train.shape[1]}x{X_train.shape[2]} piksel")
print(f"Tipe data: {X_train.dtype}")
print(f"Range nilai piksel: [{X_train.min()}, {X_train.max()}]")
print(f"\nDistribusi kelas (training):")
for digit in range(10):
    count = np.sum(y_train == digit)
    print(f"  Digit {digit}: {count} gambar ({count/len(y_train)*100:.1f}%)")
```

### Langkah 2: Preprocessing Gambar

```python
# =============================================
# LANGKAH 2: Preprocessing Gambar
# =============================================

# 1. Reshape: tambahkan dimensi channel (grayscale = 1 channel)
# Dari (28, 28) menjadi (28, 28, 1) untuk input Conv2D
X_train_reshaped = X_train.reshape(-1, 28, 28, 1)
X_test_reshaped = X_test.reshape(-1, 28, 28, 1)

# 2. Normalisasi: ubah range [0, 255] menjadi [0, 1]
X_train_norm = X_train_reshaped.astype('float32') / 255.0
X_test_norm = X_test_reshaped.astype('float32') / 255.0

# 3. One-hot encoding untuk label
from tensorflow.keras.utils import to_categorical
y_train_onehot = to_categorical(y_train, num_classes=10)
y_test_onehot = to_categorical(y_test, num_classes=10)

print("=== PREPROCESSING SELESAI ===")
print(f"X_train shape: {X_train_norm.shape}")
print(f"X_test shape : {X_test_norm.shape}")
print(f"Range piksel : [{X_train_norm.min()}, {X_train_norm.max()}]")
print(f"y_train shape: {y_train_onehot.shape}")
print(f"\nContoh one-hot label digit 5: {y_train_onehot[y_train == 5][0]}")
```

### Langkah 3: Visualisasi Sampel Gambar

```python
# =============================================
# LANGKAH 3: Visualisasi Sampel
# =============================================

# Tampilkan 20 gambar acak
fig, axes = plt.subplots(2, 10, figsize=(16, 4))
np.random.seed(42)
indices = np.random.choice(len(X_train), 20, replace=False)

for i, (ax, idx) in enumerate(zip(axes.flat, indices)):
    ax.imshow(X_train[idx], cmap='gray')
    ax.set_title(f'{y_train[idx]}', fontsize=11, color='blue')
    ax.axis('off')

plt.suptitle('Sampel Gambar MNIST (20 Digit Acak)', fontsize=14)
plt.tight_layout()
plt.show()

# Tampilkan satu gambar per digit (0-9)
fig, axes = plt.subplots(1, 10, figsize=(16, 2))
for digit in range(10):
    idx = np.where(y_train == digit)[0][0]
    axes[digit].imshow(X_train[idx], cmap='gray')
    axes[digit].set_title(f'Digit {digit}', fontsize=10)
    axes[digit].axis('off')

plt.suptitle('Satu Sampel per Kelas (Digit 0-9)', fontsize=13)
plt.tight_layout()
plt.show()

# Visualisasi distribusi piksel
plt.figure(figsize=(8, 4))
plt.hist(X_train[0].flatten(), bins=50, color='steelblue', edgecolor='white')
plt.xlabel('Nilai Piksel')
plt.ylabel('Frekuensi')
plt.title(f'Distribusi Piksel — Gambar Digit {y_train[0]}')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 4: Membangun Arsitektur CNN

```python
# =============================================
# LANGKAH 4: Arsitektur CNN
# =============================================

# Bangun model CNN
model_cnn = keras.Sequential([
    # Blok Konvolusi 1
    layers.Conv2D(32, kernel_size=(3, 3), activation='relu',
                  input_shape=(28, 28, 1), name='conv2d_1'),
    layers.MaxPooling2D(pool_size=(2, 2), name='maxpool_1'),

    # Blok Konvolusi 2
    layers.Conv2D(64, kernel_size=(3, 3), activation='relu', name='conv2d_2'),
    layers.MaxPooling2D(pool_size=(2, 2), name='maxpool_2'),

    # Blok Konvolusi 3
    layers.Conv2D(64, kernel_size=(3, 3), activation='relu', name='conv2d_3'),

    # Flatten dan Dense layers
    layers.Flatten(name='flatten'),
    layers.Dropout(0.3, name='dropout_1'),
    layers.Dense(128, activation='relu', name='dense_1'),
    layers.Dropout(0.3, name='dropout_2'),
    layers.Dense(10, activation='softmax', name='output')
])

# Tampilkan arsitektur
model_cnn.summary()

print("\nPenjelasan Arsitektur:")
print("- Conv2D: Deteksi pola lokal (tepi, sudut, tekstur)")
print("- MaxPooling2D: Reduksi dimensi, pertahankan fitur penting")
print("- Flatten: Ubah feature map 2D menjadi vektor 1D")
print("- Dropout: Regularisasi untuk mencegah overfitting")
print("- Dense + Softmax: Klasifikasi akhir (10 kelas digit)")
```

### Langkah 5: Compile dan Training

```python
# =============================================
# LANGKAH 5: Compile dan Training
# =============================================

from tensorflow.keras.callbacks import EarlyStopping

# Compile model
model_cnn.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Callback early stopping
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)

# Latih model
print("=== TRAINING CNN ===\n")
history = model_cnn.fit(
    X_train_norm, y_train_onehot,
    epochs=20,
    batch_size=128,
    validation_split=0.1,
    callbacks=[early_stop],
    verbose=1
)

actual_epochs = len(history.history['loss'])
print(f"\nTraining selesai setelah {actual_epochs} epoch")
print(f"(Early stopping patience: 3)")
```

### Langkah 6: Plot Training History

```python
# =============================================
# LANGKAH 6: Training History
# =============================================

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot Akurasi
axes[0].plot(history.history['accuracy'], 'b-', label='Training', linewidth=2)
axes[0].plot(history.history['val_accuracy'], 'r-', label='Validation', linewidth=2)
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Accuracy')
axes[0].set_title('Akurasi Training vs Validation')
axes[0].legend()
axes[0].grid(alpha=0.3)

# Plot Loss
axes[1].plot(history.history['loss'], 'b-', label='Training', linewidth=2)
axes[1].plot(history.history['val_loss'], 'r-', label='Validation', linewidth=2)
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Loss')
axes[1].set_title('Loss Training vs Validation')
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.suptitle('Training History — CNN MNIST', fontsize=14)
plt.tight_layout()
plt.show()

# Ringkasan training
final_train_acc = history.history['accuracy'][-1]
final_val_acc = history.history['val_accuracy'][-1]
print(f"Akurasi training akhir : {final_train_acc:.4f}")
print(f"Akurasi validation akhir: {final_val_acc:.4f}")
print(f"Gap: {abs(final_train_acc - final_val_acc):.4f}")
if abs(final_train_acc - final_val_acc) > 0.05:
    print("-> Terdapat indikasi overfitting (gap > 5%)")
else:
    print("-> Model belajar dengan baik (gap kecil)")
```

### Langkah 7: Evaluasi — Akurasi dan Confusion Matrix

```python
# =============================================
# LANGKAH 7: Evaluasi pada Test Set
# =============================================

from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

# Evaluasi pada test set
test_loss, test_acc = model_cnn.evaluate(X_test_norm, y_test_onehot, verbose=0)
print(f"=== EVALUASI TEST SET ===")
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_acc:.4f} ({test_acc*100:.2f}%)")

# Prediksi
y_pred_prob = model_cnn.predict(X_test_norm)
y_pred = np.argmax(y_pred_prob, axis=1)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=range(10), yticklabels=range(10))
plt.xlabel('Prediksi', fontsize=12)
plt.ylabel('Aktual', fontsize=12)
plt.title(f'Confusion Matrix — CNN MNIST (Akurasi: {test_acc:.4f})', fontsize=14)
plt.tight_layout()
plt.show()

# Classification Report
print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, y_pred,
                            target_names=[f'Digit {i}' for i in range(10)]))

# Digit dengan akurasi terendah
per_class_acc = cm.diagonal() / cm.sum(axis=1)
worst_digit = np.argmin(per_class_acc)
best_digit = np.argmax(per_class_acc)
print(f"Digit dengan akurasi tertinggi: {best_digit} ({per_class_acc[best_digit]:.4f})")
print(f"Digit dengan akurasi terendah : {worst_digit} ({per_class_acc[worst_digit]:.4f})")
```

### Langkah 8: Prediksi pada Gambar Individual

```python
# =============================================
# LANGKAH 8: Prediksi Gambar Individual
# =============================================

# Pilih 10 gambar acak dari test set
np.random.seed(123)
random_indices = np.random.choice(len(X_test), 10, replace=False)

fig, axes = plt.subplots(2, 5, figsize=(16, 7))

for i, (ax, idx) in enumerate(zip(axes.flat, random_indices)):
    # Prediksi
    img = X_test_norm[idx].reshape(1, 28, 28, 1)
    pred_prob = model_cnn.predict(img, verbose=0)
    pred_label = np.argmax(pred_prob)
    confidence = np.max(pred_prob)
    actual = y_test[idx]

    # Tampilkan gambar
    ax.imshow(X_test[idx], cmap='gray')
    is_correct = pred_label == actual
    color = 'green' if is_correct else 'red'
    ax.set_title(f'Pred: {pred_label} ({confidence:.2f})\nAktual: {actual}',
                 fontsize=10, color=color)
    ax.axis('off')

plt.suptitle('Prediksi CNN pada Gambar Test (Hijau=Benar, Merah=Salah)',
             fontsize=13)
plt.tight_layout()
plt.show()

# Tampilkan contoh yang salah diklasifikasi
print("=== GAMBAR YANG SALAH DIKLASIFIKASI ===")
wrong_indices = np.where(y_pred != y_test)[0]
print(f"Jumlah salah: {len(wrong_indices)} dari {len(y_test)} "
      f"({len(wrong_indices)/len(y_test)*100:.2f}%)")

if len(wrong_indices) > 0:
    fig, axes = plt.subplots(2, 5, figsize=(16, 7))
    for ax, idx in zip(axes.flat, wrong_indices[:10]):
        ax.imshow(X_test[idx], cmap='gray')
        pred_prob = model_cnn.predict(X_test_norm[idx].reshape(1, 28, 28, 1), verbose=0)
        pred_label = np.argmax(pred_prob)
        confidence = np.max(pred_prob)
        ax.set_title(f'Pred: {pred_label} ({confidence:.2f})\nAktual: {y_test[idx]}',
                     fontsize=10, color='red')
        ax.axis('off')

    plt.suptitle('Sampel Gambar yang Salah Diklasifikasi', fontsize=13)
    plt.tight_layout()
    plt.show()

# Distribusi confidence untuk prediksi benar vs salah
correct_conf = np.max(y_pred_prob[y_pred == y_test], axis=1)
wrong_conf = np.max(y_pred_prob[y_pred != y_test], axis=1) if len(wrong_indices) > 0 else []

plt.figure(figsize=(8, 5))
plt.hist(correct_conf, bins=30, alpha=0.7, color='green', label='Benar', density=True)
if len(wrong_conf) > 0:
    plt.hist(wrong_conf, bins=15, alpha=0.7, color='red', label='Salah', density=True)
plt.xlabel('Confidence (Probabilitas Maksimum)')
plt.ylabel('Density')
plt.title('Distribusi Confidence — Prediksi Benar vs Salah')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 9: (Opsional) Konsep Transfer Learning

```python
# =============================================
# LANGKAH 9: Konsep Transfer Learning (Opsional)
# =============================================

print("=" * 60)
print("KONSEP TRANSFER LEARNING")
print("=" * 60)

print("""
Transfer Learning adalah teknik menggunakan model yang sudah
dilatih pada dataset besar (pre-trained model) untuk tugas baru.

Keuntungan:
- Tidak perlu melatih dari nol (hemat waktu & komputasi)
- Bekerja baik meskipun dataset baru berukuran kecil
- Memanfaatkan fitur yang sudah dipelajari model

Contoh model pre-trained populer:
- VGG16/VGG19: klasifikasi gambar dasar
- ResNet50: arsitektur residual, sangat dalam
- MobileNetV2: ringan, cocok untuk mobile/edge
- InceptionV3: multi-scale feature extraction
""")

# Demonstrasi: Load MobileNetV2 (tanpa melatih ulang)
from tensorflow.keras.applications import MobileNetV2

# Load model pre-trained (tanpa top layer)
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,           # Hapus layer klasifikasi asli
    input_shape=(224, 224, 3)    # Input standar ImageNet
)

print(f"=== MobileNetV2 Pre-trained ===")
print(f"Jumlah layer: {len(base_model.layers)}")
print(f"Total parameter: {base_model.count_params():,}")
print(f"Input shape: {base_model.input_shape}")
print(f"Output shape: {base_model.output_shape}")

# Contoh arsitektur transfer learning (tidak dilatih)
model_transfer = keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')  # 10 kelas baru
])

# Freeze base model (tidak update bobot pre-trained)
base_model.trainable = False

model_transfer.compile(optimizer='adam',
                       loss='categorical_crossentropy',
                       metrics=['accuracy'])

model_transfer.summary()

print("\nCatatan: Transfer learning efektif untuk:")
print("- Dataset gambar kecil (ratusan-ribuan gambar)")
print("- Tugas klasifikasi gambar spesifik (batik, makanan, dll)")
print("- Mengurangi waktu training secara signifikan")
```

---

## Tantangan Tambahan

1. **Fashion MNIST:** Ganti dataset MNIST digit dengan Fashion MNIST (`keras.datasets.fashion_mnist`). Bangun CNN yang sama dan bandingkan akurasinya. Kelas mana yang paling sulit diklasifikasi? (misalnya: Shirt vs Coat vs Pullover)

2. **Augmentasi Data:** Terapkan data augmentation menggunakan `keras.preprocessing.image.ImageDataGenerator` (rotasi, zoom, shift). Latih ulang CNN dan bandingkan apakah augmentasi meningkatkan akurasi pada test set.

3. **Arsitektur CNN Lebih Dalam:** Eksperimen dengan arsitektur CNN yang lebih dalam (4-5 blok konvolusi) dengan BatchNormalization. Bandingkan akurasi, jumlah parameter, dan waktu training dengan arsitektur dasar.

---

## Checklist Penyelesaian

- [ ] Langkah 1: Dataset MNIST berhasil dimuat dan dieksplorasi
- [ ] Langkah 2: Gambar berhasil di-reshape dan dinormalisasi
- [ ] Langkah 3: Sampel gambar berhasil divisualisasi
- [ ] Langkah 4: Arsitektur CNN berhasil dibangun (Conv2D, MaxPooling, Dense)
- [ ] Langkah 5: Model berhasil di-compile dan dilatih
- [ ] Langkah 6: Training history berhasil divisualisasi
- [ ] Langkah 7: Confusion matrix dan classification report berhasil dibuat
- [ ] Langkah 8: Prediksi pada gambar individual berhasil divisualisasi
- [ ] Langkah 9: (Opsional) Konsep transfer learning dipahami
- [ ] Semua kode berjalan tanpa error di Google Colab
- [ ] Notebook disimpan dengan format `Lab13_NamaAnda_NIM.ipynb`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
