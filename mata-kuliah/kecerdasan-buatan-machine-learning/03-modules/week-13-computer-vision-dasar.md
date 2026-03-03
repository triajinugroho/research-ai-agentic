# Minggu 13: Computer Vision Dasar

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 13 |
| **Topik** | Computer Vision Dasar |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK-6: Menerapkan dan menganalisis teknik computer vision dasar menggunakan CNN |
| **Sub-CPMK** | 13.1 Menerapkan teknik preprocessing dan augmentasi citra menggunakan OpenCV dan Keras |
| | 13.2 Menganalisis arsitektur CNN dan konsep transfer learning untuk klasifikasi citra |
| **Bloom's Taxonomy** | C3-C4 (Menerapkan-Menganalisis / *Apply-Analyze*) |
| **Durasi** | 2 x 100 menit (Teori 100 min + Praktikum 100 min) |
| **Platform** | Google Colab |
| **Metode** | Ceramah interaktif, demonstrasi visual, hands-on coding, diskusi kelompok |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menjelaskan** konsep dasar computer vision, representasi citra digital, dan aplikasinya di berbagai domain termasuk konteks Indonesia.
2. **Menerapkan** teknik preprocessing citra (resizing, grayscale, filtering) dan augmentasi (rotasi, flip, brightness) menggunakan OpenCV dan Keras.
3. **Menganalisis** arsitektur Convolutional Neural Network (CNN) termasuk lapisan konvolusi, pooling, dan fully connected.
4. **Menerapkan** CNN sederhana untuk klasifikasi citra menggunakan Keras/TensorFlow.
5. **Menganalisis** konsep transfer learning dan kapan menggunakannya untuk menyelesaikan permasalahan klasifikasi citra.

---

## Materi Pembelajaran

### 1. Pengantar Computer Vision

#### Apa itu Computer Vision?

**Computer Vision** (*visi komputer*) adalah cabang kecerdasan buatan yang memungkinkan komputer untuk "melihat" dan memahami konten visual dari dunia nyata -- gambar dan video. Tujuan utamanya adalah mengekstraksi informasi bermakna dari data visual secara otomatis.

#### Mengapa Computer Vision Penting?

Computer vision telah menjadi salah satu bidang AI yang paling berkembang pesat, dengan aplikasi yang menyentuh kehidupan sehari-hari:

| Domain | Aplikasi | Contoh |
|---|---|---|
| **Kesehatan** | Diagnosis medis dari citra | Deteksi kanker dari X-ray, retinopati diabetik |
| **Otomotif** | Kendaraan otonom | Self-driving car, ADAS (*Advanced Driver Assistance*) |
| **Keamanan** | Pengenalan wajah, CCTV cerdas | Face recognition di bandara, deteksi anomali |
| **Pertanian** | Monitoring tanaman | Deteksi penyakit tanaman dari foto daun |
| **Retail** | Visual search, cashierless store | Amazon Go, rekomendasi produk berbasis gambar |

#### Aplikasi Computer Vision di Indonesia

| Aplikasi | Deskripsi |
|---|---|
| **Pengenalan Motif Batik** | Klasifikasi pola batik berdasarkan daerah asal (Solo, Pekalongan, Yogyakarta) |
| **Klasifikasi Makanan Nusantara** | Identifikasi jenis makanan Indonesia dari foto (nasi goreng, rendang, soto) |
| **Deteksi Kondisi Jalan** | Analisis kerusakan jalan raya dari citra drone untuk Kementerian PUPR |
| **Pertanian Presisi** | Deteksi hama pada tanaman padi dan kelapa sawit menggunakan drone |
| **E-KTP Verification** | Verifikasi identitas berbasis pengenalan wajah di layanan perbankan digital |

---

### 2. Representasi Citra Digital

#### Pixel: Unit Terkecil Citra

Sebuah citra digital tersusun dari ribuan titik kecil yang disebut **pixel** (*picture element*). Setiap pixel menyimpan nilai intensitas warna.

```
Citra Digital
├── Grayscale (1 channel)
│   └── Setiap pixel: 0 (hitam) - 255 (putih)
│
└── Berwarna / RGB (3 channels)
    ├── Red (Merah):   0-255
    ├── Green (Hijau):  0-255
    └── Blue (Biru):   0-255
```

#### Resolusi dan Ukuran

- **Resolusi** menentukan jumlah pixel (misal: 224 x 224, 1920 x 1080)
- **Channel** menentukan kedalaman warna (1 = grayscale, 3 = RGB, 4 = RGBA)
- Sebuah citra RGB 224x224 memiliki total: 224 x 224 x 3 = **150.528 nilai**

> **Insight:** Bagi komputer, sebuah gambar hanyalah matriks angka (array multidimensi). Inilah mengapa NumPy dan operasi matriks sangat penting dalam computer vision.

---

### 3. Preprocessing Citra dengan OpenCV

#### Apa itu OpenCV?

**OpenCV** (*Open Source Computer Vision Library*) adalah library paling populer untuk pemrosesan citra. Di Python, kita menggunakan `cv2` (OpenCV-Python).

#### Operasi Preprocessing Dasar

| Operasi | Fungsi | Tujuan |
|---|---|---|
| **Reading** | `cv2.imread()` | Membaca file gambar ke array NumPy |
| **Resizing** | `cv2.resize()` | Mengubah ukuran agar seragam untuk input model |
| **Grayscale** | `cv2.cvtColor()` | Mengurangi kompleksitas (3 channel -> 1 channel) |
| **Filtering** | `cv2.GaussianBlur()` | Mengurangi noise pada gambar |
| **Thresholding** | `cv2.threshold()` | Mengubah gambar menjadi biner (hitam-putih) |
| **Edge Detection** | `cv2.Canny()` | Mendeteksi tepi objek dalam gambar |

---

### 4. Augmentasi Citra (*Image Augmentation*)

#### Mengapa Augmentasi Diperlukan?

Augmentasi citra adalah teknik untuk **memperbanyak data training secara artifisial** dengan menerapkan transformasi pada gambar yang sudah ada. Ini sangat penting ketika dataset terbatas.

#### Teknik Augmentasi Umum

| Teknik | Deskripsi | Contoh Penggunaan |
|---|---|---|
| **Rotasi** | Memutar gambar beberapa derajat | Objek bisa muncul dalam orientasi berbeda |
| **Flipping** | Membalik gambar horizontal/vertikal | Simetri objek |
| **Brightness** | Mengubah kecerahan gambar | Variasi pencahayaan |
| **Zooming** | Memperbesar/memperkecil area gambar | Skala objek bervariasi |
| **Shifting** | Menggeser posisi gambar | Objek tidak selalu di tengah |

#### Augmentasi di Keras

Keras menyediakan `ImageDataGenerator` untuk augmentasi secara otomatis saat training:

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=20,       # Rotasi hingga 20 derajat
    width_shift_range=0.2,   # Geser horizontal 20%
    height_shift_range=0.2,  # Geser vertikal 20%
    horizontal_flip=True,    # Flip horizontal
    brightness_range=[0.8, 1.2],  # Variasi kecerahan
    zoom_range=0.2           # Zoom 20%
)
```

> **Analogi:** Augmentasi seperti mengajari anak mengenali kucing -- kita tunjukkan kucing dari berbagai sudut, jarak, dan pencahayaan agar ia bisa mengenali kucing dalam kondisi apapun.

---

### 5. Convolutional Neural Networks (CNN)

#### Apa itu CNN?

**Convolutional Neural Network** (CNN) adalah arsitektur neural network yang dirancang khusus untuk memproses data berbentuk grid, terutama citra. CNN secara otomatis belajar mendeteksi fitur-fitur visual (*feature learning*) tanpa perlu ekstraksi fitur manual.

#### Komponen Utama CNN

```
Input Image → [Conv2D → ReLU → MaxPool] × N → Flatten → Dense → Output
              ├── Feature Extraction ──────┤  ├── Classification ──┤
```

##### a) Lapisan Konvolusi (*Convolution Layer*)

Lapisan konvolusi menggunakan **filter** (kernel) berukuran kecil (misal 3x3) yang "bergeser" di atas gambar untuk mendeteksi fitur tertentu:

- Filter awal: mendeteksi **tepi** (edges), **garis** (lines)
- Filter tengah: mendeteksi **tekstur**, **pola**
- Filter akhir: mendeteksi **bagian objek**, **bentuk kompleks**

```
Input (5x5)          Filter (3x3)         Output (Feature Map)
┌─────────────┐      ┌─────────┐          ┌─────────┐
│ 1  0  1  0  1│      │ 1  0  1 │          │ 4  3  4 │
│ 0  1  0  1  0│  *   │ 0  1  0 │    =     │ 2  4  3 │
│ 1  0  1  0  1│      │ 1  0  1 │          │ 4  3  4 │
│ 0  1  0  1  0│      └─────────┘          └─────────┘
│ 1  0  1  0  1│
└─────────────┘
```

##### b) Lapisan Pooling (*Pooling Layer*)

Pooling **mengurangi dimensi** feature map dengan mengambil nilai representatif dari setiap region:

- **Max Pooling**: mengambil nilai **maksimum** (paling umum digunakan)
- **Average Pooling**: mengambil nilai **rata-rata**

```
Input (4x4)              Max Pooling (2x2)      Output (2x2)
┌───┬───┬───┬───┐        stride = 2              ┌───┬───┐
│ 1 │ 3 │ 2 │ 1 │                                │ 4 │ 6 │
├───┼───┼───┼───┤        ──────────────>          ├───┼───┤
│ 4 │ 2 │ 6 │ 1 │                                │ 8 │ 4 │
├───┼───┼───┼───┤                                └───┴───┘
│ 1 │ 5 │ 3 │ 2 │
├───┼───┼───┼───┤
│ 8 │ 1 │ 4 │ 3 │
└───┴───┴───┴───┘
```

##### c) Flatten dan Dense Layer

- **Flatten**: mengubah feature map 2D menjadi vektor 1D
- **Dense** (Fully Connected): lapisan klasifikasi biasa seperti pada neural network standar

---

### 6. Arsitektur CNN dengan Keras

#### Struktur Khas CNN untuk Klasifikasi Citra

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

model = Sequential([
    # Blok Konvolusi 1
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),

    # Blok Konvolusi 2
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),

    # Blok Klasifikasi
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),   # Regularisasi untuk mencegah overfitting
    Dense(10, activation='softmax')  # 10 kelas output
])
```

#### Penjelasan Parameter

| Parameter | Keterangan |
|---|---|
| `Conv2D(32, (3,3))` | 32 filter berukuran 3x3 |
| `activation='relu'` | Fungsi aktivasi ReLU: f(x) = max(0, x) |
| `input_shape=(28,28,1)` | Ukuran input: 28x28 pixel, 1 channel (grayscale) |
| `MaxPooling2D((2,2))` | Pooling dengan window 2x2, mengurangi dimensi 50% |
| `Dropout(0.5)` | Mematikan 50% neuron secara acak saat training |
| `Dense(10, softmax)` | 10 output dengan probabilitas (multi-class classification) |

---

### 7. Transfer Learning

#### Apa itu Transfer Learning?

**Transfer learning** adalah teknik menggunakan model yang sudah dilatih (*pre-trained model*) pada dataset besar (seperti ImageNet -- 1.2 juta gambar, 1000 kelas) sebagai titik awal untuk tugas baru.

#### Mengapa Transfer Learning?

| Keuntungan | Penjelasan |
|---|---|
| **Hemat data** | Tidak perlu jutaan gambar untuk training |
| **Hemat waktu** | Tidak perlu training dari awal (nol) |
| **Performa lebih baik** | Model sudah belajar fitur-fitur visual umum |
| **GPU minimal** | Bisa dilakukan di Google Colab gratis |

#### Model Pre-trained Populer

| Model | Tahun | Parameter | Top-5 Accuracy (ImageNet) |
|---|---|---|---|
| **VGG16** | 2014 | 138M | 92.7% |
| **ResNet50** | 2015 | 25M | 93.3% |
| **InceptionV3** | 2015 | 24M | 93.7% |
| **MobileNetV2** | 2018 | 3.4M | 90.1% |
| **EfficientNetB0** | 2019 | 5.3M | 93.3% |

> **Tips:** Untuk tugas di Google Colab dengan GPU terbatas, **MobileNetV2** adalah pilihan yang baik karena ringan namun tetap akurat.

#### Dua Strategi Transfer Learning

1. **Feature Extraction**: Bekukan (*freeze*) semua lapisan model pre-trained, hanya latih lapisan klasifikasi baru
2. **Fine-tuning**: Bekukan sebagian besar lapisan, buka beberapa lapisan terakhir untuk disesuaikan dengan data baru

---

### 8. Konteks Indonesia: Pengenalan Pola Batik dan Klasifikasi Makanan

#### Pengenalan Motif Batik

Batik Indonesia memiliki beragam motif yang khas berdasarkan daerah:

| Daerah | Contoh Motif | Karakteristik Visual |
|---|---|---|
| **Solo** | Parang, Sidomukti | Garis diagonal, pola geometris teratur |
| **Pekalongan** | Jlamprang, Buketan | Warna cerah, motif bunga, pengaruh Tionghoa |
| **Yogyakarta** | Kawung, Truntum | Pola simetris, warna sogan (cokelat-krem) |
| **Cirebon** | Mega Mendung | Motif awan bergelombang, warna biru gradasi |

Computer vision dapat membantu mengklasifikasikan dan melestarikan warisan budaya batik Indonesia secara digital.

#### Klasifikasi Makanan Nusantara

Dataset makanan Indonesia bisa mencakup kelas-kelas seperti:
- Nasi Goreng, Rendang, Soto Ayam, Gado-gado
- Sate, Bakso, Rawon, Pempek
- Gudeg, Nasi Padang, Mie Ayam, Rujak

> **Refleksi:** Pengembangan dataset citra lokal Indonesia berkontribusi pada kemajuan riset AI di Indonesia dan melestarikan kekayaan budaya Nusantara. Ini adalah bentuk **amanah** sebagai akademisi dan teknolog Muslim.

---

## Aktivitas Kelas

### Sesi 1: Teori dan Demonstrasi (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 15 menit | Pembukaan & Review | Review neural network (Minggu 11-12), motivasi computer vision |
| 20 menit | Ceramah: Konsep CV & Representasi Citra | Penjelasan pixel, channel, resolusi, format gambar |
| 15 menit | Demonstrasi: Preprocessing OpenCV | Live demo resizing, grayscale, filtering di Colab |
| 15 menit | Ceramah: Arsitektur CNN | Konvolusi, pooling, feature maps, visualisasi |
| 15 menit | Diskusi: Transfer Learning | Kapan dan mengapa menggunakan pre-trained model |
| 10 menit | Studi Kasus Indonesia | Batik recognition, food classification |
| 10 menit | Q&A & Transisi Praktikum | Pertanyaan, persiapan hands-on |

### Sesi 2: Praktikum Hands-on (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Setup Environment | Install OpenCV, import library, akses dataset |
| 20 menit | Preprocessing Citra | Latihan baca, resize, grayscale, filter gambar |
| 10 menit | Augmentasi Citra | Implementasi ImageDataGenerator |
| 30 menit | Build CNN | Bangun dan latih CNN untuk klasifikasi MNIST |
| 15 menit | Evaluasi Model | Analisis accuracy, confusion matrix, visualisasi prediksi |
| 10 menit | Eksplorasi Transfer Learning | Demo singkat menggunakan MobileNetV2 |
| 5 menit | Wrap-up & Preview | Rangkuman, preview Minggu 14: AI-Augmented Development |

---

## Hands-on: Computer Vision dengan Python

### Langkah 1: Setup dan Import Library

```python
# Install library tambahan jika diperlukan
!pip install opencv-python-headless -q

# Import library yang dibutuhkan
import numpy as np
import matplotlib.pyplot as plt
import cv2
from google.colab import files

# TensorFlow dan Keras
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator

print(f"TensorFlow versi: {tf.__version__}")
print(f"OpenCV versi: {cv2.__version__}")
print("Semua library berhasil di-import!")
```

### Langkah 2: Memahami Representasi Citra

```python
# Membuat citra sederhana secara manual untuk memahami representasi pixel
# Citra grayscale 5x5
gambar_gray = np.array([
    [0,   50,  100, 150, 200],
    [50,  100, 150, 200, 255],
    [100, 150, 200, 255, 200],
    [150, 200, 255, 200, 150],
    [200, 255, 200, 150, 100]
], dtype=np.uint8)

# Citra RGB 3x3 (Merah-Putih seperti bendera Indonesia)
gambar_rgb = np.zeros((6, 6, 3), dtype=np.uint8)
gambar_rgb[:3, :, 0] = 255    # Baris atas: merah (R=255)
gambar_rgb[3:, :, :] = 255    # Baris bawah: putih (semua 255)

# Visualisasi
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].imshow(gambar_gray, cmap='gray')
axes[0].set_title('Citra Grayscale (1 Channel)')
axes[0].set_xlabel(f'Shape: {gambar_gray.shape}')

axes[1].imshow(gambar_rgb)
axes[1].set_title('Citra RGB (3 Channels)')
axes[1].set_xlabel(f'Shape: {gambar_rgb.shape}')

plt.tight_layout()
plt.show()

print(f"Nilai pixel grayscale:\n{gambar_gray}")
print(f"\nNilai pixel RGB (channel merah):\n{gambar_rgb[:,:,0]}")
```

### Langkah 3: Preprocessing Citra dengan OpenCV

```python
# Membuat citra contoh yang lebih kompleks
# (Dalam praktik nyata, kita akan membaca file gambar)
np.random.seed(42)
gambar_asli = np.random.randint(50, 200, (100, 100, 3), dtype=np.uint8)

# Menambahkan pola sederhana (kotak di tengah)
gambar_asli[30:70, 30:70, 0] = 200  # Kotak merah
gambar_asli[30:70, 30:70, 1] = 50
gambar_asli[30:70, 30:70, 2] = 50

# 1. Resize gambar
gambar_resize = cv2.resize(gambar_asli, (50, 50))

# 2. Konversi ke grayscale
gambar_gray = cv2.cvtColor(gambar_asli, cv2.COLOR_BGR2GRAY)

# 3. Gaussian blur (mengurangi noise)
gambar_blur = cv2.GaussianBlur(gambar_asli, (7, 7), 0)

# 4. Edge detection (deteksi tepi)
gambar_edges = cv2.Canny(gambar_gray, 50, 150)

# Visualisasi hasil preprocessing
fig, axes = plt.subplots(1, 4, figsize=(16, 4))
judul = ['Asli (100x100)', 'Resize (50x50)', 'Grayscale', 'Edge Detection']
gambar_list = [gambar_asli, gambar_resize, gambar_gray, gambar_edges]
cmaps = [None, None, 'gray', 'gray']

for ax, img, title, cmap in zip(axes, gambar_list, judul, cmaps):
    ax.imshow(img, cmap=cmap)
    ax.set_title(title)
    ax.axis('off')

plt.suptitle('Hasil Preprocessing Citra dengan OpenCV', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

print("Preprocessing berhasil!")
print(f"Ukuran asli: {gambar_asli.shape}")
print(f"Ukuran setelah resize: {gambar_resize.shape}")
print(f"Ukuran grayscale: {gambar_gray.shape}")
```

### Langkah 4: Load Dataset MNIST

```python
# Load dataset MNIST (angka tulisan tangan 0-9)
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print(f"Ukuran data training: {X_train.shape}")
print(f"Ukuran data testing: {X_test.shape}")
print(f"Jumlah kelas: {len(np.unique(y_train))}")
print(f"Kelas: {np.unique(y_train)}")

# Visualisasi contoh gambar MNIST
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_train[i], cmap='gray')
    ax.set_title(f'Label: {y_train[i]}', fontsize=12)
    ax.axis('off')

plt.suptitle('Contoh Gambar MNIST (Angka Tulisan Tangan)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Langkah 5: Preprocessing Data untuk CNN

```python
# Reshape data: tambahkan dimensi channel (grayscale = 1 channel)
X_train_cnn = X_train.reshape(-1, 28, 28, 1).astype('float32')
X_test_cnn = X_test.reshape(-1, 28, 28, 1).astype('float32')

# Normalisasi pixel dari 0-255 menjadi 0-1
X_train_cnn = X_train_cnn / 255.0
X_test_cnn = X_test_cnn / 255.0

# One-hot encoding label
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

print(f"Shape X_train setelah reshape: {X_train_cnn.shape}")
print(f"Shape y_train setelah one-hot: {y_train_cat.shape}")
print(f"Contoh one-hot label untuk angka {y_train[0]}: {y_train_cat[0]}")
print(f"Range pixel: [{X_train_cnn.min()}, {X_train_cnn.max()}]")
```

### Langkah 6: Membangun Model CNN

```python
# Membangun arsitektur CNN
model = Sequential([
    # Blok Konvolusi 1
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),

    # Blok Konvolusi 2
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),

    # Blok Klasifikasi
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Tampilkan ringkasan arsitektur
model.summary()
```

### Langkah 7: Training Model CNN

```python
# Training model (gunakan subset untuk menghemat waktu di Colab)
history = model.fit(
    X_train_cnn, y_train_cat,
    epochs=5,
    batch_size=128,
    validation_split=0.2,
    verbose=1
)

# Visualisasi training history
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot accuracy
axes[0].plot(history.history['accuracy'], label='Training', marker='o')
axes[0].plot(history.history['val_accuracy'], label='Validation', marker='s')
axes[0].set_title('Akurasi Model CNN per Epoch')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Akurasi')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Plot loss
axes[1].plot(history.history['loss'], label='Training', marker='o')
axes[1].plot(history.history['val_loss'], label='Validation', marker='s')
axes[1].set_title('Loss Model CNN per Epoch')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Loss')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### Langkah 8: Evaluasi Model

```python
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# Evaluasi pada data test
test_loss, test_accuracy = model.evaluate(X_test_cnn, y_test_cat, verbose=0)
print(f"Akurasi pada data test: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")
print(f"Loss pada data test: {test_loss:.4f}")

# Prediksi
y_pred = model.predict(X_test_cnn)
y_pred_classes = np.argmax(y_pred, axis=1)

# Classification report
print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred_classes))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred_classes)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=range(10), yticklabels=range(10))
plt.title('Confusion Matrix - CNN MNIST')
plt.xlabel('Prediksi')
plt.ylabel('Aktual')
plt.tight_layout()
plt.show()

# Visualisasi beberapa prediksi
fig, axes = plt.subplots(2, 5, figsize=(14, 6))
indices = np.random.choice(len(X_test), 10, replace=False)

for i, ax in enumerate(axes.flat):
    idx = indices[i]
    ax.imshow(X_test[idx], cmap='gray')
    warna = 'green' if y_pred_classes[idx] == y_test[idx] else 'red'
    ax.set_title(f'Pred: {y_pred_classes[idx]} | Aktual: {y_test[idx]}',
                 color=warna, fontsize=10)
    ax.axis('off')

plt.suptitle('Hasil Prediksi CNN (Hijau=Benar, Merah=Salah)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### Langkah 9: Demo Transfer Learning (MobileNetV2)

```python
# Demo konsep transfer learning dengan MobileNetV2
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D

# Load model pre-trained (tanpa lapisan klasifikasi atas)
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(96, 96, 3)
)

# Bekukan semua lapisan base model
base_model.trainable = False

# Bangun model baru dengan base model + klasifikasi kustom
model_transfer = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(5, activation='softmax')  # Misal 5 kelas makanan Indonesia
])

model_transfer.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Tampilkan ringkasan
print("=== Arsitektur Transfer Learning ===")
print(f"Total parameter: {model_transfer.count_params():,}")
print(f"Trainable parameter: {sum(tf.keras.backend.count_params(w) for w in model_transfer.trainable_weights):,}")
print(f"Non-trainable parameter: {sum(tf.keras.backend.count_params(w) for w in model_transfer.non_trainable_weights):,}")
print("\nModel siap untuk dilatih pada dataset makanan Indonesia!")
print("Kelas contoh: ['Nasi Goreng', 'Rendang', 'Soto', 'Sate', 'Gado-gado']")
```

---

## AI Corner: AI untuk Computer Vision -- Kapabilitas Terkini

> **Level: Advanced** -- Minggu ini kita mengeksplorasi kemampuan AI modern dalam domain computer vision.

### Kemampuan AI Terkini dalam Computer Vision

| Kemampuan | Deskripsi | Contoh Tools/Model |
|---|---|---|
| **Image Classification** | Mengklasifikasikan gambar ke kategori | ResNet, EfficientNet, ViT |
| **Object Detection** | Mendeteksi dan melokalisasi objek | YOLO, Faster R-CNN |
| **Image Segmentation** | Segmentasi pixel-level | U-Net, Mask R-CNN |
| **Image Generation** | Membuat gambar baru dari teks | DALL-E, Stable Diffusion, Midjourney |
| **OCR** | Mengekstraksi teks dari gambar | Tesseract, Google Vision API |

### Cara AI Membantu Belajar Computer Vision

| Skenario | Contoh Prompt ke AI |
|---|---|
| Memahami arsitektur | *"Jelaskan cara kerja konvolusi di CNN dengan analogi sederhana"* |
| Debugging model | *"Model CNN saya overfitting, akurasi training 99% tapi validation 60%. Bagaimana cara mengatasinya?"* |
| Pilih arsitektur | *"Saya punya 500 gambar batik, model apa yang cocok? Build from scratch atau transfer learning?"* |
| Optimasi performa | *"Bagaimana cara meningkatkan akurasi model klasifikasi gambar dari 85% ke 95%?"* |

### Contoh Prompt Minggu Ini

```
Saya sedang belajar CNN untuk klasifikasi gambar.
1. Jelaskan perbedaan antara Conv2D dan Dense layer.
2. Mengapa kita perlu MaxPooling setelah Convolution?
3. Kapan sebaiknya menggunakan transfer learning vs training dari awal?
4. Berikan tips agar model CNN tidak overfitting.
Gunakan bahasa sederhana dan contoh visual jika memungkinkan.
```

### Tips Penggunaan AI untuk Computer Vision

1. **Gunakan AI untuk memahami error** -- paste error message dan minta penjelasan
2. **Minta rekomendasi arsitektur** -- jelaskan dataset dan tujuan Anda, minta saran model
3. **Jangan langsung copy-paste** -- pahami setiap lapisan dan parameternya
4. **Verifikasi output AI** -- jalankan kode dan periksa apakah hasilnya masuk akal

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai bahan refleksi:

1. **Representasi Visual:** Bagaimana pemahaman bahwa gambar adalah matriks angka mengubah cara pandang Anda tentang "komputer yang bisa melihat"? Apakah komputer benar-benar "melihat" seperti manusia?

2. **CNN vs Neural Network Biasa:** Mengapa CNN lebih efektif untuk data citra dibandingkan neural network fully connected biasa? Apa keuntungan operasi konvolusi?

3. **Transfer Learning di Indonesia:** Sebutkan dua contoh aplikasi transfer learning yang bermanfaat untuk Indonesia. Mengapa transfer learning cocok untuk kondisi di mana dataset lokal masih terbatas?

4. **Etika Computer Vision:** Teknologi pengenalan wajah (*face recognition*) menuai kontroversi di banyak negara. Bagaimana menurut Anda, dari perspektif nilai-nilai Islam (amanah, keadilan, tidak merugikan), batasan penggunaan teknologi ini yang seharusnya diterapkan?

5. **Warisan Budaya Digital:** Bagaimana computer vision dapat membantu melestarikan warisan budaya Indonesia (seperti batik, wayang, arsitektur tradisional)? Apa tantangan teknisnya?

---

## Tugas Mandiri Minggu 13

1. **Preprocessing Citra:** Ambil 5 foto makanan Indonesia dari internet, lalu terapkan preprocessing berikut di Google Colab menggunakan OpenCV: resize ke 224x224, konversi ke grayscale, terapkan Gaussian blur, dan deteksi tepi. Tampilkan hasilnya dalam grid visualisasi.

2. **Modifikasi CNN:** Modifikasi arsitektur CNN dari hands-on (tambahkan 1 blok konvolusi lagi atau ubah jumlah filter), lalu bandingkan akurasinya. Buat tabel perbandingan minimal 3 variasi arsitektur.

3. **Laporan Singkat Transfer Learning:** Tulis laporan singkat (1 halaman) yang membandingkan transfer learning vs training dari awal. Sertakan diagram alur (*flowchart*) yang menunjukkan kapan memilih masing-masing pendekatan.

---

## Referensi

### Buku Teks

1. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press. (Chapter 9: Convolutional Networks)
2. Chollet, F. (2021). *Deep Learning with Python* (2nd ed.). Manning Publications.
3. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.

### Sumber Online

4. [TensorFlow CNN Tutorial](https://www.tensorflow.org/tutorials/images/cnn) -- Tutorial resmi TensorFlow untuk CNN.
5. [Keras Applications](https://keras.io/api/applications/) -- Daftar model pre-trained di Keras.
6. [OpenCV Python Tutorial](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) -- Dokumentasi resmi OpenCV-Python.

### Referensi Indonesia

7. Nurhaida, I., et al. (2015). Automatic Indonesian's Batik Pattern Recognition Using SIFT Approach. *Procedia Computer Science*, 59, 567-576.
8. [Indonesia AI](https://indonesiaai.org/) -- Komunitas dan riset AI di Indonesia.

---

> **Preview Minggu Depan:** Kita akan membahas **AI-Augmented Development dan MLOps** -- bagaimana menggunakan AI sebagai co-developer dalam membangun pipeline ML, serta konsep dasar deployment dan monitoring model.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
