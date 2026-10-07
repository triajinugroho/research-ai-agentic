# BAB 12: COMPUTER VISION DASAR

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| Sub-CPMK 13.1 | Menerapkan teknik preprocessing citra digital menggunakan OpenCV dan PIL | C3 (Menerapkan) |
| Sub-CPMK 13.2 | Menganalisis arsitektur Convolutional Neural Network (CNN) untuk klasifikasi gambar | C4 (Menganalisis) |

**CPMK-6:** Menerapkan dan menganalisis teknik computer vision dasar untuk penyelesaian masalah klasifikasi citra.

**Estimasi Waktu:** 3 × 50 menit (2 SKS)

**Prasyarat:** Mahasiswa telah memahami konsep neural network dasar (Bab 10–11), operasi matriks dengan NumPy, serta dasar-dasar supervised learning.

---

## 12.1 Computer Vision Overview

### 12.1.1 Apa itu Computer Vision?

**Computer Vision** (Visi Komputer) adalah cabang AI yang memungkinkan komputer untuk "melihat" dan memahami konten visual dari dunia nyata — seperti gambar, video, dan data visual lainnya.

> "Computer Vision is the science of making machines see."
> — Fei-Fei Li, Stanford University

Secara sederhana, jika Machine Learning memberikan komputer kemampuan untuk **belajar dari data**, maka Computer Vision memberikan komputer kemampuan untuk **belajar dari data visual**.

```
                    KECERDASAN BUATAN (AI)
                           │
            ┌──────────────┼──────────────┐
            │              │              │
     Machine Learning   Robotics    Expert Systems
            │
    ┌───────┼───────┐
    │       │       │
   NLP   Computer  Speech
         Vision    Recognition
            │
    ┌───────┼───────┐
    │       │       │
  Image   Object   Face
  Classif. Detection Recognition
```

### 12.1.2 Mengapa Computer Vision Penting?

Computer Vision telah menjadi salah satu bidang AI dengan perkembangan paling pesat:

| Aplikasi | Contoh Nyata | Konteks Indonesia |
|----------|-------------|-------------------|
| **Pengenalan Wajah** | Face ID, keamanan bandara | e-KTP biometrik, verifikasi identitas fintech |
| **Kendaraan Otonom** | Tesla Autopilot, Waymo | Riset kendaraan otonom ITB, UI |
| **Medis** | Deteksi kanker dari X-ray | Analisis citra medis RSUP Nasional |
| **Pertanian** | Deteksi penyakit tanaman | Monitoring sawit, padi Indonesia |
| **E-commerce** | Visual search produk | Pencarian visual di Tokopedia, Shopee |
| **Keamanan** | CCTV cerdas | Smart city Jakarta, Surabaya |

### 12.1.3 Tugas Utama Computer Vision

1. **Image Classification** — Mengklasifikasikan gambar ke kategori tertentu (kucing vs anjing)
2. **Object Detection** — Mendeteksi dan melokalisasi objek dalam gambar (bounding box)
3. **Semantic Segmentation** — Memberi label pada setiap piksel gambar
4. **Face Recognition** — Mengidentifikasi atau memverifikasi identitas seseorang
5. **Image Generation** — Membuat gambar baru (DALL-E, Stable Diffusion)

---

## 12.2 Representasi Citra Digital

### 12.2.1 Piksel, Channel (RGB), dan Resolusi

Sebuah **citra digital** (digital image) pada dasarnya adalah sebuah **matriks angka**. Setiap elemen matriks disebut **piksel** (picture element).

```
Gambar Grayscale 4×4:                Gambar RGB 4×4:
┌─────┬─────┬─────┬─────┐           Setiap piksel memiliki 3 nilai:
│  0  │ 128 │ 255 │  64 │           - Red (Merah):   0-255
├─────┼─────┼─────┼─────┤           - Green (Hijau):  0-255
│ 200 │  50 │ 180 │ 100 │           - Blue (Biru):   0-255
├─────┼─────┼─────┼─────┤
│  30 │ 220 │  90 │ 150 │           Contoh: (255, 0, 0) = Merah murni
├─────┼─────┼─────┼─────┤                    (0, 255, 0) = Hijau murni
│ 170 │  80 │ 240 │  10 │                    (0, 0, 255) = Biru murni
└─────┴─────┴─────┴─────┘                    (255, 255, 255) = Putih
```

**Resolusi** menentukan ukuran citra:
- Gambar 1920×1080 (Full HD) = 2.073.600 piksel
- Gambar 224×224 (standar input CNN) = 50.176 piksel
- Gambar 28×28 (MNIST) = 784 piksel

### 12.2.2 Citra sebagai Array NumPy

Dalam Python, citra direpresentasikan sebagai array NumPy:

```python
import numpy as np

# Membuat citra grayscale 4x4 (contoh)
gambar_gray = np.array([
    [0, 128, 255, 64],
    [200, 50, 180, 100],
    [30, 220, 90, 150],
    [170, 80, 240, 10]
], dtype=np.uint8)

print(f"Bentuk (shape): {gambar_gray.shape}")   # (4, 4)
print(f"Tipe data: {gambar_gray.dtype}")         # uint8
print(f"Nilai minimum: {gambar_gray.min()}")     # 0
print(f"Nilai maksimum: {gambar_gray.max()}")    # 255

# Membuat citra RGB 4x4x3
gambar_rgb = np.zeros((4, 4, 3), dtype=np.uint8)
gambar_rgb[0, 0] = [255, 0, 0]    # Piksel (0,0) = Merah
gambar_rgb[0, 1] = [0, 255, 0]    # Piksel (0,1) = Hijau
gambar_rgb[0, 2] = [0, 0, 255]    # Piksel (0,2) = Biru
gambar_rgb[0, 3] = [255, 255, 0]  # Piksel (0,3) = Kuning

print(f"Bentuk RGB: {gambar_rgb.shape}")  # (4, 4, 3)
```

### 12.2.3 Image I/O dengan OpenCV dan PIL

```python
# Instalasi di Google Colab (sudah tersedia secara default)
# !pip install opencv-python Pillow

# === Menggunakan OpenCV ===
import cv2
from google.colab import files
import matplotlib.pyplot as plt

# Upload gambar di Colab
# uploaded = files.upload()

# Membaca gambar dengan OpenCV (format BGR)
gambar_cv = cv2.imread('contoh.jpg')
print(f"Shape OpenCV: {gambar_cv.shape}")  # (tinggi, lebar, channel)

# OpenCV menggunakan BGR, konversi ke RGB untuk matplotlib
gambar_rgb = cv2.cvtColor(gambar_cv, cv2.COLOR_BGR2RGB)

# Menampilkan gambar
plt.figure(figsize=(8, 6))
plt.imshow(gambar_rgb)
plt.title('Gambar Contoh')
plt.axis('off')
plt.show()

# === Menggunakan PIL (Pillow) ===
from PIL import Image

# Membaca gambar dengan PIL (format RGB)
gambar_pil = Image.open('contoh.jpg')
print(f"Ukuran PIL: {gambar_pil.size}")    # (lebar, tinggi)
print(f"Mode: {gambar_pil.mode}")          # RGB

# Konversi PIL ke NumPy array
gambar_array = np.array(gambar_pil)
print(f"Shape array: {gambar_array.shape}")
```

> **Catatan Penting:** OpenCV membaca gambar dalam format **BGR** (Blue-Green-Red), sedangkan PIL dan matplotlib menggunakan format **RGB**. Selalu konversi format saat berpindah antar library.

---

## 12.3 Image Preprocessing

### 12.3.1 Resizing dan Konversi Grayscale

Preprocessing adalah langkah penting sebelum memasukkan gambar ke model ML:

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar
gambar = cv2.imread('makanan_indonesia.jpg')
gambar_rgb = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)

# --- Resizing ---
# Resize ke ukuran standar CNN (224×224)
gambar_resized = cv2.resize(gambar_rgb, (224, 224))
print(f"Ukuran asli: {gambar_rgb.shape}")
print(f"Ukuran resize: {gambar_resized.shape}")

# --- Konversi ke Grayscale ---
gambar_gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
print(f"Shape grayscale: {gambar_gray.shape}")  # (tinggi, lebar)

# Visualisasi perbandingan
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(gambar_rgb)
axes[0].set_title('Original')
axes[1].imshow(gambar_resized)
axes[1].set_title('Resized (224×224)')
axes[2].imshow(gambar_gray, cmap='gray')
axes[2].set_title('Grayscale')
for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

### 12.3.2 Filtering: Blur dan Edge Detection

```python
# --- Gaussian Blur (Penghalusan) ---
# Berguna untuk mengurangi noise pada gambar
gambar_blur = cv2.GaussianBlur(gambar_gray, (5, 5), 0)

# --- Edge Detection (Deteksi Tepi) ---
# Menggunakan algoritma Canny
tepi = cv2.Canny(gambar_gray, threshold1=50, threshold2=150)

# --- Sobel Filter ---
sobel_x = cv2.Sobel(gambar_gray, cv2.CV_64F, 1, 0, ksize=3)  # Tepi horizontal
sobel_y = cv2.Sobel(gambar_gray, cv2.CV_64F, 0, 1, ksize=3)  # Tepi vertikal

# Visualisasi
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].imshow(gambar_gray, cmap='gray')
axes[0, 0].set_title('Original Grayscale')
axes[0, 1].imshow(gambar_blur, cmap='gray')
axes[0, 1].set_title('Gaussian Blur')
axes[1, 0].imshow(tepi, cmap='gray')
axes[1, 0].set_title('Canny Edge Detection')
axes[1, 1].imshow(np.abs(sobel_x) + np.abs(sobel_y), cmap='gray')
axes[1, 1].set_title('Sobel Filter (X + Y)')
for ax in axes.flat:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

### 12.3.3 Thresholding

Thresholding mengubah gambar grayscale menjadi gambar biner (hitam-putih):

```python
# Thresholding sederhana
_, thresh_binary = cv2.threshold(gambar_gray, 127, 255, cv2.THRESH_BINARY)
_, thresh_otsu = cv2.threshold(gambar_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Adaptive thresholding — lebih baik untuk pencahayaan tidak merata
thresh_adaptive = cv2.adaptiveThreshold(
    gambar_gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 11, 2
)

# Visualisasi
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(thresh_binary, cmap='gray')
axes[0].set_title('Binary Threshold (127)')
axes[1].imshow(thresh_otsu, cmap='gray')
axes[1].set_title('Otsu Threshold')
axes[2].imshow(thresh_adaptive, cmap='gray')
axes[2].set_title('Adaptive Threshold')
for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

### 12.3.4 Image Augmentation (Augmentasi Gambar)

Augmentasi gambar digunakan untuk memperbanyak data training secara artifisial:

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np

# Konfigurasi augmentasi
augmentasi = ImageDataGenerator(
    rotation_range=30,         # Rotasi acak 0-30 derajat
    horizontal_flip=True,      # Flip horizontal
    brightness_range=[0.7, 1.3], # Variasi kecerahan
    zoom_range=0.2,            # Zoom acak 0-20%
    width_shift_range=0.1,     # Geser horizontal
    height_shift_range=0.1     # Geser vertikal
)

# Contoh augmentasi pada satu gambar
gambar_contoh = gambar_resized.reshape(1, 224, 224, 3)  # Tambah dimensi batch

# Tampilkan 6 variasi augmentasi
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes[0, 0].imshow(gambar_resized)
axes[0, 0].set_title('Original')

for i, ax in enumerate(axes.flat[1:]):
    batch = next(augmentasi.flow(gambar_contoh, batch_size=1))
    gambar_aug = batch[0].astype(np.uint8)
    ax.imshow(gambar_aug)
    ax.set_title(f'Augmentasi {i+1}')

for ax in axes.flat:
    ax.axis('off')
plt.suptitle('Contoh Augmentasi Gambar', fontsize=14)
plt.tight_layout()
plt.show()
```

---

## 12.4 Convolutional Neural Networks (CNN)

### 12.4.1 Operasi Konvolusi

**Konvolusi** adalah operasi inti dari CNN. Sebuah **filter** (kernel) kecil digeser di atas gambar untuk menghasilkan **feature map**.

```
Input (5×5)          Filter (3×3)         Output (3×3)
┌───┬───┬───┬───┬───┐   ┌───┬───┬───┐   ┌───┬───┬───┐
│ 1 │ 0 │ 1 │ 0 │ 1 │   │ 1 │ 0 │ 1 │   │ 4 │ 3 │ 4 │
├───┼───┼───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
│ 0 │ 1 │ 0 │ 1 │ 0 │   │ 0 │ 1 │ 0 │   │ 2 │ 4 │ 3 │
├───┼───┼───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
│ 1 │ 0 │ 1 │ 0 │ 1 │   │ 1 │ 0 │ 1 │   │ 4 │ 3 │ 4 │
├───┼───┼───┼───┼───┤   └───┴───┴───┘   └───┴───┴───┘
│ 0 │ 1 │ 0 │ 1 │ 0 │
├───┼───┼───┼───┼───┤   Perhitungan sudut kiri atas:
│ 1 │ 0 │ 1 │ 0 │ 1 │   (1×1)+(0×0)+(1×1)+(0×0)+
└───┴───┴───┴───┴───┘   (1×1)+(0×0)+(1×1)+(0×0)+
                         (1×1) = 4
```

```python
import numpy as np

# Demonstrasi konvolusi manual
def konvolusi_2d(gambar, kernel):
    """Implementasi konvolusi 2D sederhana."""
    h_gambar, w_gambar = gambar.shape
    h_kernel, w_kernel = kernel.shape
    h_output = h_gambar - h_kernel + 1
    w_output = w_gambar - w_kernel + 1
    output = np.zeros((h_output, w_output))

    for i in range(h_output):
        for j in range(w_output):
            # Ambil bagian gambar seukuran kernel
            bagian = gambar[i:i+h_kernel, j:j+w_kernel]
            # Kalikan elemen per elemen, lalu jumlahkan
            output[i, j] = np.sum(bagian * kernel)

    return output

# Contoh penggunaan
gambar = np.array([
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1]
], dtype=np.float32)

# Filter deteksi tepi vertikal
kernel_tepi = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
], dtype=np.float32)

hasil = konvolusi_2d(gambar, kernel_tepi)
print("Hasil konvolusi:")
print(hasil)
```

### 12.4.2 Feature Maps dan Filters

Dalam CNN, filter dipelajari secara otomatis selama training:

- **Layer awal** mendeteksi fitur sederhana: tepi, garis, warna
- **Layer tengah** mendeteksi fitur kompleks: tekstur, bentuk
- **Layer akhir** mendeteksi fitur abstrak: wajah, objek

```
Input Image → [Conv Layer 1] → [Conv Layer 2] → [Conv Layer 3]
              Tepi, Garis      Tekstur, Bentuk   Objek, Pola
              (Low-level)      (Mid-level)       (High-level)
```

### 12.4.3 Pooling Layers

**Pooling** mengurangi dimensi feature map sambil mempertahankan informasi penting:

```
Max Pooling (2×2, stride=2):

Input (4×4)              Output (2×2)
┌────┬────┬────┬────┐    ┌────┬────┐
│  1 │  3 │  2 │  1 │    │  5 │  7 │  ← max(1,3,0,5)=5, max(2,1,6,7)=7
├────┼────┼────┼────┤    ├────┼────┤
│  0 │  5 │  6 │  7 │    │  8 │  4 │  ← max(2,8,1,3)=8, max(0,4,2,1)=4
├────┼────┼────┼────┤    └────┴────┘
│  2 │  8 │  0 │  4 │
├────┼────┼────┼────┤
│  1 │  3 │  2 │  1 │
└────┴────┴────┴────┘
```

**Keuntungan Pooling:**
1. Mengurangi jumlah parameter (mencegah overfitting)
2. Mengurangi waktu komputasi
3. Membuat model lebih robust terhadap posisi objek (*translation invariance*)

### 12.4.4 Arsitektur CNN: Conv2D → MaxPooling2D → Flatten → Dense

```
Arsitektur CNN untuk Klasifikasi Gambar:

Input (28×28×1)
    │
    ▼
[Conv2D: 32 filter, 3×3, ReLU]  → (26×26×32)
    │
    ▼
[MaxPooling2D: 2×2]              → (13×13×32)
    │
    ▼
[Conv2D: 64 filter, 3×3, ReLU]  → (11×11×64)
    │
    ▼
[MaxPooling2D: 2×2]              → (5×5×64)
    │
    ▼
[Flatten]                         → (1600)
    │
    ▼
[Dense: 128, ReLU]               → (128)
    │
    ▼
[Dense: 10, Softmax]             → (10) ← Probabilitas per kelas
```

---

## 12.5 Membangun CNN dengan Keras

### 12.5.1 Klasifikasi Fashion-MNIST

Fashion-MNIST berisi 70.000 gambar grayscale (28×28 piksel) dari 10 kategori pakaian:

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import numpy as np

# Memuat dataset Fashion-MNIST
(X_train, y_train), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()

# Nama kategori
nama_kelas = ['T-shirt/top', 'Celana', 'Pullover', 'Dress', 'Mantel',
              'Sandal', 'Kemeja', 'Sepatu kets', 'Tas', 'Ankle boot']

print(f"Data training: {X_train.shape}")   # (60000, 28, 28)
print(f"Data testing: {X_test.shape}")     # (10000, 28, 28)
print(f"Jumlah kelas: {len(nama_kelas)}")

# Visualisasi sampel data
fig, axes = plt.subplots(2, 5, figsize=(15, 6))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_train[i], cmap='gray')
    ax.set_title(nama_kelas[y_train[i]])
    ax.axis('off')
plt.suptitle('Sampel Data Fashion-MNIST', fontsize=14)
plt.tight_layout()
plt.show()

# Preprocessing: normalisasi dan reshape
X_train = X_train.astype('float32') / 255.0  # Normalisasi ke [0, 1]
X_test = X_test.astype('float32') / 255.0

# Tambah dimensi channel (grayscale = 1 channel)
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

print(f"Shape setelah reshape: {X_train.shape}")  # (60000, 28, 28, 1)
```

### 12.5.2 Arsitektur Model, Compile, dan Fit

```python
# Membangun model CNN
model = keras.Sequential([
    # Blok Konvolusi 1
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),

    # Blok Konvolusi 2
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Blok Konvolusi 3
    layers.Conv2D(64, (3, 3), activation='relu'),

    # Klasifikasi
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),  # Regularisasi: mencegah overfitting
    layers.Dense(10, activation='softmax')  # 10 kelas output
])

# Ringkasan arsitektur
model.summary()

# Kompilasi model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Melatih model
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=64,
    validation_split=0.2,  # 20% data training untuk validasi
    verbose=1
)
```

### 12.5.3 Visualisasi Training

```python
# Visualisasi akurasi dan loss selama training
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot Akurasi
axes[0].plot(history.history['accuracy'], label='Training', linewidth=2)
axes[0].plot(history.history['val_accuracy'], label='Validasi', linewidth=2)
axes[0].set_title('Akurasi Model')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Akurasi')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Plot Loss
axes[1].plot(history.history['loss'], label='Training', linewidth=2)
axes[1].plot(history.history['val_loss'], label='Validasi', linewidth=2)
axes[1].set_title('Loss Model')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Loss')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.suptitle('Riwayat Training CNN Fashion-MNIST', fontsize=14)
plt.tight_layout()
plt.show()
```

### 12.5.4 Evaluasi Model

```python
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# Evaluasi pada data testing
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Akurasi Testing: {test_accuracy:.4f}")
print(f"Loss Testing: {test_loss:.4f}")

# Prediksi
y_pred = model.predict(X_test)
y_pred_kelas = np.argmax(y_pred, axis=1)

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred_kelas, target_names=nama_kelas))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred_kelas)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=nama_kelas, yticklabels=nama_kelas)
plt.title('Confusion Matrix — Fashion-MNIST CNN')
plt.xlabel('Prediksi')
plt.ylabel('Aktual')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Visualisasi prediksi (benar dan salah)
fig, axes = plt.subplots(2, 5, figsize=(15, 6))
salah_idx = np.where(y_pred_kelas != y_test)[0]

for i, ax in enumerate(axes.flat[:5]):
    ax.imshow(X_test[i].reshape(28, 28), cmap='gray')
    warna = 'green' if y_pred_kelas[i] == y_test[i] else 'red'
    ax.set_title(f'Pred: {nama_kelas[y_pred_kelas[i]]}', color=warna)
    ax.axis('off')

for i, ax in enumerate(axes.flat[5:]):
    idx = salah_idx[i] if i < len(salah_idx) else 0
    ax.imshow(X_test[idx].reshape(28, 28), cmap='gray')
    ax.set_title(f'Pred: {nama_kelas[y_pred_kelas[idx]]}\n'
                 f'Actual: {nama_kelas[y_test[idx]]}', color='red')
    ax.axis('off')

plt.suptitle('Contoh Prediksi (Hijau = Benar, Merah = Salah)', fontsize=14)
plt.tight_layout()
plt.show()
```

---

## 12.6 Transfer Learning

### 12.6.1 Konsep Pre-trained Models

**Transfer Learning** adalah teknik menggunakan model yang sudah dilatih pada dataset besar (misalnya ImageNet dengan 14 juta gambar) sebagai titik awal untuk tugas baru.

```
Transfer Learning:

Model Pre-trained (ImageNet)          Model Baru (Tugas Kita)
┌────────────────────┐               ┌────────────────────┐
│ Conv Layers        │ ──TRANSFER──→ │ Conv Layers        │ ← Bobot dibekukan
│ (fitur universal)  │               │ (fitur universal)  │   (frozen)
├────────────────────┤               ├────────────────────┤
│ Dense Layers       │               │ Dense Layers BARU  │ ← Dilatih ulang
│ (1000 kelas)       │               │ (kelas kita)       │
└────────────────────┘               └────────────────────┘
```

**Mengapa Transfer Learning?**
1. Dataset kita mungkin kecil — pre-trained model sudah belajar fitur visual umum
2. Menghemat waktu training secara signifikan
3. Performa lebih baik dibanding melatih dari nol (*from scratch*)

### 12.6.2 VGG16 dan ResNet (Ringkasan)

| Model | Kedalaman | Parameter | Ukuran | Fitur Utama |
|-------|-----------|-----------|--------|-------------|
| **VGG16** | 16 layer | 138 juta | 528 MB | Sederhana, filter 3×3 konsisten |
| **ResNet50** | 50 layer | 25.6 juta | 98 MB | Skip connections, lebih efisien |
| **MobileNetV2** | 53 layer | 3.4 juta | 14 MB | Ringan, cocok untuk mobile |

### 12.6.3 Konsep Fine-Tuning

```python
from tensorflow.keras.applications import VGG16
from tensorflow.keras import layers, Model

# Memuat VGG16 tanpa top layers, dengan bobot ImageNet
base_model = VGG16(
    weights='imagenet',
    include_top=False,       # Hapus dense layers terakhir
    input_shape=(224, 224, 3)
)

# Bekukan (freeze) semua layer base model
base_model.trainable = False

# Tambahkan layer klasifikasi baru
x = base_model.output
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dense(256, activation='relu')(x)
x = layers.Dropout(0.5)(x)
output = layers.Dense(5, activation='softmax')(x)  # Contoh: 5 kelas makanan

# Bangun model baru
model_transfer = Model(inputs=base_model.input, outputs=output)

# Compile
model_transfer.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print(f"Total parameter: {model_transfer.count_params():,}")
print(f"Parameter trainable: {sum(p.numpy().size for p in model_transfer.trainable_weights):,}")
```

---

## 12.7 Konteks Indonesia: Pengenalan Pola Batik dan Klasifikasi Makanan Indonesia

### 12.7.1 Pengenalan Pola Batik

Batik merupakan warisan budaya Indonesia yang diakui UNESCO. Computer Vision dapat digunakan untuk mengklasifikasikan motif batik secara otomatis:

```python
# Contoh konseptual: klasifikasi motif batik
# Dataset batik bisa dikumpulkan dari berbagai sumber

motif_batik = [
    'Parang',       # Motif diagonal — Yogyakarta
    'Kawung',       # Motif geometris bulat — Solo
    'Mega Mendung', # Motif awan — Cirebon
    'Truntum',      # Motif bunga kecil — Solo
    'Sekar Jagad',  # Motif peta — berbagai daerah
]

# Arsitektur CNN untuk klasifikasi batik
model_batik = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(len(motif_batik), activation='softmax')
])

print("Model klasifikasi motif batik:")
model_batik.summary()
```

### 12.7.2 Klasifikasi Makanan Indonesia

```python
# Contoh: klasifikasi makanan Indonesia
makanan_indonesia = [
    'Nasi Goreng',
    'Rendang',
    'Sate Ayam',
    'Gado-gado',
    'Bakso',
    'Soto Ayam',
    'Rawon',
    'Pempek',
    'Gudeg',
    'Nasi Padang'
]

# Menggunakan Transfer Learning untuk klasifikasi makanan
from tensorflow.keras.applications import MobileNetV2

# MobileNetV2 — cocok untuk aplikasi mobile
base_model_food = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)
base_model_food.trainable = False

model_makanan = keras.Sequential([
    base_model_food,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.4),
    layers.Dense(len(makanan_indonesia), activation='softmax')
])

model_makanan.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print(f"\nModel klasifikasi makanan Indonesia:")
print(f"Jumlah kelas: {len(makanan_indonesia)}")
print(f"Total parameter: {model_makanan.count_params():,}")
```

> **Ide Proyek:** Bangun aplikasi mobile yang dapat mengenali makanan Indonesia dari foto — berguna untuk wisatawan asing, dokumentasi kuliner, atau estimasi kalori.

---

## AI Corner — Level: Advanced

### AI untuk Computer Vision: Kemampuan dan Masa Depan

| Aspek | Deskripsi |
|-------|-----------|
| **Level** | Advanced — Gunakan AI sebagai partner analisis dan debugging |
| **Tools** | ChatGPT, Claude, GitHub Copilot |
| **Fokus** | Arsitektur CNN, debugging model, interpretasi hasil |

### Prompt yang Efektif untuk Computer Vision

**Contoh prompt yang BAIK:**
```
"Saya membangun CNN untuk klasifikasi 10 jenis makanan Indonesia
menggunakan gambar 224×224 RGB. Model saya mengalami overfitting
(training accuracy 98%, validation accuracy 72%). Arsitektur saya:
Conv2D(32) → MaxPool → Conv2D(64) → MaxPool → Dense(512) → Dense(10).
Apa yang bisa saya perbaiki?"
```

**Contoh prompt yang KURANG BAIK:**
```
"Buat model computer vision yang bagus"
```

### Cara AI Membantu dalam Computer Vision

1. **Memilih arsitektur** — Minta AI merekomendasikan arsitektur CNN berdasarkan ukuran dataset dan kompleksitas tugas
2. **Debugging error** — Jelaskan error yang muncul beserta shape data
3. **Interpretasi hasil** — Minta AI menjelaskan confusion matrix atau classification report
4. **Augmentasi data** — Minta saran teknik augmentasi yang sesuai

### Kebijakan Penggunaan AI

| Aktivitas | Kebijakan |
|-----------|-----------|
| **Tugas Mingguan** | AI BOLEH digunakan, WAJIB didokumentasikan dalam AI Usage Log |
| **Kuis** | AI TIDAK BOLEH digunakan (closed-book, di kelas) |
| **UTS** | AI TIDAK BOLEH digunakan (closed-book) |
| **Proyek Akhir** | AI BOLEH digunakan, WAJIB didokumentasikan dalam AI Usage Log |
| **UAS** | AI TIDAK BOLEH digunakan (closed-book) |

---

## Rangkuman Bab 12

1. **Computer Vision** adalah cabang AI yang memungkinkan komputer memahami dan memproses data visual — gambar dan video.
2. **Citra digital** direpresentasikan sebagai array NumPy: grayscale (H×W), RGB (H×W×3). Nilai piksel berkisar 0-255 (uint8).
3. **Image preprocessing** meliputi resizing, konversi grayscale, filtering (blur, edge detection), thresholding, dan augmentasi — semua penting untuk performa model.
4. **CNN** menggunakan operasi konvolusi untuk mengekstrak fitur dari gambar secara hierarkis: tepi → tekstur → objek.
5. Arsitektur CNN dasar: **Conv2D → MaxPooling2D → Flatten → Dense** — dengan Softmax untuk output klasifikasi.
6. **Transfer Learning** memungkinkan kita menggunakan model pre-trained (VGG16, ResNet, MobileNet) untuk tugas baru dengan dataset kecil.
7. Konteks Indonesia: CV dapat diterapkan untuk **pengenalan motif batik** dan **klasifikasi makanan Indonesia** — mendukung pelestarian budaya dan inovasi teknologi.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan antara gambar grayscale dan gambar RGB dalam hal representasi array NumPy. Sebutkan shape masing-masing untuk gambar berukuran 100×100.

**Soal 2.** Apa fungsi dari operasi berikut dalam preprocessing gambar?
- a) Resizing
- b) Normalisasi (membagi dengan 255)
- c) Gaussian Blur
- d) Edge Detection

**Soal 3.** Sebutkan tiga keuntungan menggunakan pooling layer dalam arsitektur CNN.

**Soal 4.** Apa perbedaan antara OpenCV dan PIL dalam hal format warna saat membaca gambar?

**Soal 5.** Jelaskan mengapa augmentasi gambar penting dalam deep learning, terutama ketika dataset kecil.

### Tingkat Menengah (C3-C4)

**Soal 6.** Tulis kode Python menggunakan OpenCV untuk:
- a) Membaca sebuah gambar
- b) Mengubah ukurannya menjadi 224×224
- c) Mengkonversi ke grayscale
- d) Menerapkan Canny edge detection
- e) Menampilkan gambar asli dan hasil edge detection secara berdampingan

**Soal 7.** Diberikan arsitektur CNN berikut:
```
Input: 32×32×3
Conv2D: 16 filter, 3×3, padding='valid'
MaxPooling2D: 2×2
Conv2D: 32 filter, 3×3, padding='valid'
MaxPooling2D: 2×2
Flatten
Dense: 64
Dense: 10
```
Hitunglah output shape setelah setiap layer.

**Soal 8.** Jelaskan bagaimana proses konvolusi bekerja. Gunakan contoh input 4×4 dengan kernel 2×2 dan tunjukkan perhitungan langkah demi langkah untuk menghasilkan satu nilai output.

**Soal 9.** Perhatikan confusion matrix berikut untuk klasifikasi 3 jenis makanan Indonesia:

|          | Pred: Rendang | Pred: Sate | Pred: Bakso |
|----------|:---:|:---:|:---:|
| **Actual: Rendang** | 45 | 3 | 2 |
| **Actual: Sate** | 5 | 40 | 5 |
| **Actual: Bakso** | 1 | 4 | 45 |

Hitunglah: a) Akurasi keseluruhan, b) Precision dan Recall untuk kelas "Sate", c) Kelas mana yang paling sering salah diklasifikasikan?

### Tingkat Mahir (C4-C5)

**Soal 10.** Anda diminta membangun model CNN untuk mengklasifikasikan 5 motif batik Indonesia. Dataset Anda hanya berisi 500 gambar (100 per kelas). Jelaskan:
- a) Strategi apa yang akan Anda gunakan untuk mengatasi keterbatasan data?
- b) Apakah Anda akan membangun CNN dari nol atau menggunakan transfer learning? Berikan alasan.
- c) Pre-trained model mana yang akan Anda pilih dan mengapa?

**Soal 11.** Bandingkan arsitektur VGG16, ResNet50, dan MobileNetV2 dari segi:
- a) Jumlah parameter
- b) Kedalaman network
- c) Keunggulan masing-masing
- d) Kapan masing-masing sebaiknya digunakan

**Soal 12.** Model CNN Anda untuk klasifikasi gambar mencapai training accuracy 99% tetapi validation accuracy hanya 65%. Analisis:
- a) Apa masalah yang terjadi?
- b) Sebutkan minimal 3 teknik untuk mengatasi masalah tersebut
- c) Tulis kode Python yang mengimplementasikan salah satu solusi tersebut

---

## Daftar Pustaka Bab 12

1. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
2. Chollet, F. (2021). *Deep Learning with Python* (2nd ed.). Manning Publications.
3. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
4. OpenCV Documentation. (2025). *OpenCV-Python Tutorials*. Retrieved from https://docs.opencv.org
5. Szeliski, R. (2022). *Computer Vision: Algorithms and Applications* (2nd ed.). Springer.
6. He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep Residual Learning for Image Recognition. *Proceedings of CVPR 2016*.
7. Howard, A. G., et al. (2017). MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications. *arXiv:1704.04861*.
8. Simonyan, K., & Zisserman, A. (2015). Very Deep Convolutional Networks for Large-Scale Image Recognition. *Proceedings of ICLR 2015*.

---

*Bab berikutnya: **Bab 13 — AI-Augmented Development dan MLOps***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
