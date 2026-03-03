# LAMPIRAN

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Daftar Lampiran

| Lampiran | Judul |
|----------|-------|
| A | Instalasi dan Setup Python / Google Colab |
| B | Daftar Library Python yang Digunakan |
| C | Template AI Usage Log |
| D | Panduan Penggunaan AI secara Bertanggung Jawab |
| E | Glosarium Istilah AI/ML |
| F | Referensi Dataset Indonesia untuk ML |
| G | Cheat Sheet scikit-learn API |
| H | Cheat Sheet Keras API |

---

## Lampiran A: Instalasi dan Setup Python / Google Colab

### A.1 Mengapa Google Colab?

Google Colaboratory (Colab) adalah lingkungan notebook berbasis cloud yang memungkinkan mahasiswa menjalankan kode Python tanpa instalasi apapun. Keunggulan Colab untuk pembelajaran AI/ML:

- **Gratis** — akses GPU/TPU terbatas tersedia tanpa biaya, esensial untuk deep learning
- **Tanpa instalasi** — berjalan langsung di browser
- **Terintegrasi** dengan Google Drive untuk penyimpanan
- **Berbagi mudah** — link notebook dapat dibagikan seperti Google Docs
- **Pre-installed libraries** — NumPy, Pandas, scikit-learn, TensorFlow, Keras sudah tersedia
- **GPU access** — pelatihan model neural network tanpa memerlukan hardware khusus

---

### A.2 Memulai Google Colab

**Langkah 1: Buka Colab**

1. Buka browser dan kunjungi `https://colab.research.google.com`
2. Masuk dengan akun Google Anda
3. Klik **"New notebook"** untuk membuat notebook baru, atau
4. Klik **"File → Open notebook"** untuk membuka file `.ipynb` yang sudah ada

**Langkah 2: Mengenal Antarmuka**

```
┌─────────────────────────────────────────────────────┐
│  File  Edit  View  Insert  Runtime  Tools  Help      │
├─────────────────────────────────────────────────────┤
│  [+ Code]  [+ Text]          RAM ████░░  Disk ██░░  │
├─────────────────────────────────────────────────────┤
│  ▶ [ Sel kode Python di sini...                   ] │
│  ▶ [ Sel teks Markdown di sini...                 ] │
└─────────────────────────────────────────────────────┘
```

- **Sel Code** — tempat menulis dan menjalankan kode Python
- **Sel Text** — tempat menulis penjelasan menggunakan Markdown
- **Runtime** — menu untuk mengelola sesi komputasi

**Langkah 3: Mengaktifkan GPU**

Untuk eksperimen deep learning (TensorFlow, Keras, CNN):

1. Klik **Runtime → Change runtime type**
2. Pilih **Hardware accelerator: GPU** (T4 GPU)
3. Klik **Save**

```python
# Verifikasi GPU tersedia
import tensorflow as tf
print(f"TensorFlow version: {tf.__version__}")
print(f"GPU available: {tf.config.list_physical_devices('GPU')}")

# Jika GPU tersedia, output akan menunjukkan:
# GPU available: [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

**Langkah 4: Menjalankan Kode**

Klik tombol `▶` di sebelah kiri sel, atau tekan `Shift + Enter`.

---

### A.3 Instalasi Lokal (Opsional)

Jika Anda ingin bekerja secara lokal, berikut langkah instalasinya:

**Menggunakan Anaconda (Direkomendasikan):**

```bash
# 1. Download Anaconda dari https://www.anaconda.com/download
# 2. Instal sesuai sistem operasi Anda
# 3. Buat environment baru untuk kursus ini

conda create -n aiml-uai python=3.10
conda activate aiml-uai

# 4. Instal library yang diperlukan
pip install numpy pandas matplotlib seaborn scikit-learn
pip install tensorflow keras
pip install nltk spacy gensim
pip install jupyter notebook

# 5. Jalankan Jupyter Notebook
jupyter notebook
```

**Menggunakan pip langsung:**

```bash
# Pastikan Python 3.10+ sudah terinstal
python --version

# Buat virtual environment
python -m venv aiml-env
source aiml-env/bin/activate  # Linux/Mac
# aiml-env\Scripts\activate   # Windows

# Instal semua library
pip install -r requirements.txt
```

---

### A.4 Menghubungkan Google Drive

```python
# Pasang Google Drive ke Colab
from google.colab import drive
drive.mount('/content/drive')

# Setelah otorisasi, akses file seperti:
import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/data/dataset.csv')
```

---

### A.5 Keyboard Shortcuts Penting

| Shortcut | Fungsi |
|----------|--------|
| `Shift + Enter` | Jalankan sel saat ini, pindah ke sel berikutnya |
| `Ctrl + Enter` | Jalankan sel saat ini, tetap di sel yang sama |
| `Alt + Enter` | Jalankan sel saat ini, buat sel baru di bawah |
| `Ctrl + M + B` | Tambah sel kode di bawah |
| `Ctrl + M + A` | Tambah sel kode di atas |
| `Ctrl + M + D` | Hapus sel saat ini |
| `Ctrl + M + M` | Ubah sel menjadi Markdown |
| `Ctrl + M + Y` | Ubah sel menjadi kode |
| `Ctrl + /` | Komentar/uncomment baris |
| `Ctrl + Z` | Undo |
| `Ctrl + S` | Simpan notebook |
| `Ctrl + F9` | Jalankan semua sel |
| `Ctrl + M + H` | Tampilkan daftar shortcut lengkap |

---

### A.6 Tips Penggunaan Colab untuk AI/ML

**1. Hindari timeout sesi**

Colab akan memutus sesi setelah ~90 menit tidak aktif. Simpan pekerjaan Anda secara berkala ke Google Drive.

```python
# Simpan model ke Drive secara berkala
model.save('/content/drive/MyDrive/models/model_checkpoint.h5')
```

**2. Cek resource yang tersedia**

```python
# Cek GPU yang digunakan
!nvidia-smi

# Cek RAM tersedia
import psutil
ram = psutil.virtual_memory()
print(f"RAM Total: {ram.total / (1024**3):.1f} GB")
print(f"RAM Used:  {ram.used / (1024**3):.1f} GB")
print(f"RAM Free:  {ram.available / (1024**3):.1f} GB")
```

**3. Template impor standar untuk AI/ML**

Selalu mulai notebook dengan sel ini:

```python
# === Import Standar AI/ML ===
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Machine Learning
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import mean_squared_error, r2_score

# Deep Learning
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Pengaturan tampilan grafik
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
sns.set_style('whitegrid')
sns.set_palette('husl')

print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"scikit-learn: {__import__('sklearn').__version__}")
print(f"TensorFlow: {tf.__version__}")
print("Setup selesai!")
```

---

## Lampiran B: Daftar Library Python yang Digunakan

Berikut adalah daftar lengkap library Python yang digunakan sepanjang buku ajar ini, dikelompokkan berdasarkan fungsi.

### B.1 Library Inti (Sudah Tersedia di Colab)

| Library | Fungsi Utama | Import Standar | Versi Minimum |
|---------|-------------|----------------|---------------|
| `numpy` | Komputasi numerik, array, aljabar linear | `import numpy as np` | 1.23+ |
| `pandas` | Manipulasi data tabular, DataFrame | `import pandas as pd` | 1.5+ |
| `matplotlib` | Visualisasi dasar, plotting | `import matplotlib.pyplot as plt` | 3.6+ |
| `seaborn` | Visualisasi statistik lanjut | `import seaborn as sns` | 0.12+ |
| `scipy` | Komputasi ilmiah, statistik | `from scipy import stats` | 1.9+ |
| `scikit-learn` | Machine learning klasik | `from sklearn import ...` | 1.2+ |
| `tensorflow` | Deep learning, neural networks | `import tensorflow as tf` | 2.12+ |
| `keras` | High-level API untuk neural networks | `from tensorflow import keras` | (termasuk di TF) |

### B.2 Library Tambahan (Perlu Instalasi)

```python
# NLP (Natural Language Processing)
!pip install nltk spacy gensim
!pip install transformers  # Hugging Face Transformers
!python -m spacy download id_core_news_sm  # Model bahasa Indonesia

# Visualisasi interaktif
!pip install plotly

# Evaluasi model lanjut
!pip install shap lime  # Explainable AI

# Gradient Boosting
!pip install xgboost lightgbm catboost

# Computer Vision
!pip install opencv-python-headless  # OpenCV
!pip install Pillow  # Image processing

# Utilitas
!pip install tqdm  # Progress bar
!pip install joblib  # Parallel processing
!pip install imbalanced-learn  # Handling imbalanced data
```

### B.3 Deskripsi Library Tambahan

| Library | Fungsi Utama | Bab yang Menggunakan |
|---------|-------------|---------------------|
| `nltk` | Tokenisasi, stemming, NLP klasik | Bab 11 |
| `spacy` | NLP modern, NER, POS tagging | Bab 11 |
| `gensim` | Word embeddings (Word2Vec, FastText) | Bab 11 |
| `transformers` | Pre-trained models (BERT, GPT) | Bab 11, 13 |
| `xgboost` | Gradient boosting yang efisien | Bab 7 |
| `lightgbm` | Gradient boosting ringan | Bab 7 |
| `opencv` | Computer vision, image processing | Bab 12 |
| `shap` | Explainable AI (SHAP values) | Bab 10, 13 |
| `lime` | Local Interpretable Model Explanations | Bab 10, 13 |
| `plotly` | Visualisasi interaktif | Bab 3, 8 |
| `imbalanced-learn` | Teknik handling data tidak seimbang | Bab 6, 7 |

---

## Lampiran C: Template AI Usage Log

### C.1 Mengapa AI Usage Log?

AI Usage Log adalah catatan transparan tentang bagaimana mahasiswa menggunakan AI (ChatGPT, Claude, Copilot, dll.) dalam proses belajar dan pengerjaan tugas. Log ini bertujuan untuk:

1. **Transparansi** — Menunjukkan bahwa AI digunakan sebagai alat bantu belajar, bukan pengganti pemikiran
2. **Refleksi** — Membantu mahasiswa merefleksikan seberapa efektif interaksi mereka dengan AI
3. **Integritas akademik** — Memastikan penggunaan AI sesuai dengan kebijakan akademik
4. **Portofolio keterampilan** — Menunjukkan kemampuan prompt engineering dan critical evaluation

### C.2 Template Log

```
╔══════════════════════════════════════════════════════════════╗
║                    AI USAGE LOG                              ║
║         Kecerdasan Buatan dan Machine Learning               ║
║         Program Studi Informatika — UAI                      ║
╠══════════════════════════════════════════════════════════════╣
║ Nama Mahasiswa  : ______________________________________     ║
║ NIM             : ______________________________________     ║
║ Tugas/Bab       : ______________________________________     ║
║ Tanggal         : ______________________________________     ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║ ENTRI LOG #___                                               ║
║                                                              ║
║ AI Tool yang Digunakan: [ ] ChatGPT  [ ] Claude             ║
║                         [ ] Copilot  [ ] Lainnya: _____      ║
║                                                              ║
║ Tujuan Penggunaan:                                           ║
║ [ ] Memahami konsep                                          ║
║ [ ] Debugging kode                                           ║
║ [ ] Membantu menulis kode                                    ║
║ [ ] Membandingkan algoritma                                  ║
║ [ ] Interpretasi hasil/output                                ║
║ [ ] Review kode / best practices                             ║
║ [ ] Lainnya: ___________________________________             ║
║                                                              ║
║ Prompt yang Diberikan:                                       ║
║ ____________________________________________________________ ║
║ ____________________________________________________________ ║
║ ____________________________________________________________ ║
║                                                              ║
║ Ringkasan Respons AI:                                        ║
║ ____________________________________________________________ ║
║ ____________________________________________________________ ║
║ ____________________________________________________________ ║
║                                                              ║
║ Evaluasi Kritis:                                             ║
║ - Apakah respons AI benar?      [ ] Ya  [ ] Sebagian  [ ] Tidak ║
║ - Apakah perlu modifikasi?      [ ] Ya  [ ] Tidak            ║
║ - Apa yang saya pelajari?                                    ║
║   __________________________________________________________ ║
║ - Apa yang harus saya verifikasi sendiri?                    ║
║   __________________________________________________________ ║
║                                                              ║
║ Level Kontribusi AI: (lingkari satu)                         ║
║ 1 — Minimal (hanya klarifikasi konsep)                       ║
║ 2 — Moderat (membantu sebagian kode/analisis)                ║
║ 3 — Signifikan (membantu sebagian besar kode/analisis)       ║
║                                                              ║
║ Refleksi: Apa yang akan saya lakukan berbeda di lain waktu?  ║
║ ____________________________________________________________ ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

### C.3 Contoh Pengisian

| Komponen | Contoh |
|----------|--------|
| **Tugas/Bab** | Bab 7 — Latihan Menengah #3: Random Forest untuk Klasifikasi |
| **AI Tool** | Claude |
| **Tujuan** | Debugging kode — model Random Forest menghasilkan accuracy 100% pada training set |
| **Prompt** | "Model RandomForestClassifier saya mendapatkan accuracy 100% di training set tapi hanya 65% di test set. Kode saya: [kode]. Apa yang salah dan bagaimana cara memperbaikinya?" |
| **Ringkasan Respons** | AI menjelaskan bahwa model overfitting karena tidak ada pembatasan max_depth dan min_samples_leaf. Disarankan menambah regularisasi dan menggunakan cross-validation. |
| **Evaluasi** | Benar — setelah menambah max_depth=10 dan min_samples_leaf=5, gap antara train dan test accuracy berkurang signifikan. Saya juga belajar membaca learning curve untuk mendiagnosis overfitting. |
| **Level** | 2 — Moderat |

---

## Lampiran D: Panduan Penggunaan AI secara Bertanggung Jawab

### D.1 Prinsip Dasar

Penggunaan AI dalam pembelajaran AI/ML di Universitas Al Azhar Indonesia didasarkan pada prinsip berikut:

```
┌─────────────────────────────────────────────────────────────┐
│              PRINSIP PENGGUNAAN AI di UAI                    │
│                                                              │
│  1. AI sebagai MITRA BELAJAR, bukan pengganti berpikir      │
│  2. TRANSPARANSI — selalu dokumentasikan penggunaan AI       │
│  3. VERIFIKASI — selalu validasi output AI secara kritis     │
│  4. PEMAHAMAN — pastikan Anda memahami apa yang AI hasilkan  │
│  5. INTEGRITAS — jujur tentang kontribusi AI dalam tugas     │
└─────────────────────────────────────────────────────────────┘
```

### D.2 Yang BOLEH Dilakukan

| Aktivitas | Contoh | Catatan |
|-----------|--------|---------|
| Meminta penjelasan konsep | "Jelaskan intuisi di balik gradient descent" | Bandingkan dengan penjelasan di buku |
| Debugging kode | "Mengapa kode KNN saya menghasilkan error ini?" | Pahami penyebab error, bukan hanya perbaikannya |
| Membandingkan pendekatan | "Kapan saya harus menggunakan Random Forest vs SVM?" | Verifikasi dengan eksperimen sendiri |
| Menulis boilerplate code | "Tuliskan template kode untuk cross-validation di scikit-learn" | Modifikasi sesuai kebutuhan spesifik |
| Review kode | "Apakah ada cara yang lebih efisien untuk melakukan feature engineering ini?" | Pahami mengapa cara tersebut lebih efisien |
| Interpretasi output | "Bagaimana cara menginterpretasi confusion matrix ini?" | Latih kemampuan interpretasi sendiri |

### D.3 Yang TIDAK BOLEH Dilakukan

| Aktivitas | Mengapa Dilarang |
|-----------|-----------------|
| Copy-paste seluruh jawaban tugas dari AI tanpa pemahaman | Melanggar integritas akademik; tidak ada pembelajaran yang terjadi |
| Menggunakan AI saat UTS/UAS | Ujian adalah closed-book dan tanpa AI |
| Menyembunyikan penggunaan AI | Melanggar prinsip transparansi dan amanah |
| Mengandalkan AI tanpa verifikasi | AI dapat menghasilkan output yang salah (*hallucination*) |
| Meminta AI menyelesaikan seluruh proyek akhir | Proyek akhir adalah demonstrasi kemampuan Anda, bukan AI |

### D.4 Tingkat Penggunaan AI per Jenis Tugas

| Jenis Tugas | Tingkat AI yang Diperbolehkan |
|-------------|------------------------------|
| **Latihan Soal Dasar** | Minimal — kerjakan sendiri, gunakan AI hanya untuk klarifikasi setelah mencoba |
| **Latihan Soal Menengah** | Moderat — boleh berdiskusi dengan AI, tetapi solusi harus dari pemahaman sendiri |
| **Latihan Soal Mahir** | Moderat — boleh menggunakan AI untuk debugging dan eksplorasi pendekatan |
| **Tugas Mingguan** | Moderat — dokumentasikan semua penggunaan AI dalam AI Usage Log |
| **Proyek Akhir** | Moderat — AI sebagai coding assistant, tetapi desain dan analisis dari Anda |
| **UTS / UAS** | Tidak diperbolehkan — ujian closed-book tanpa akses AI |
| **Kuis** | Tidak diperbolehkan — kuis menguji pemahaman individual |

### D.5 Etika AI dari Perspektif Islam

Sebagai mahasiswa di Universitas Al Azhar Indonesia, penggunaan AI harus sejalan dengan nilai-nilai Islami:

- **Amanah** — Jujur tentang kontribusi AI dalam pekerjaan Anda. Menyembunyikan penggunaan AI sama dengan ketidakjujuran.
- **Tawadhu (Kerendahan Hati)** — Akui keterbatasan pemahaman Anda dan gunakan AI untuk belajar, bukan untuk tampak lebih mampu dari yang sebenarnya.
- **Itqan (Kesempurnaan dalam Bekerja)** — Gunakan AI untuk meningkatkan kualitas pekerjaan, bukan untuk mengambil jalan pintas.
- **Istiqamah (Konsistensi)** — Disiplin dalam mendokumentasikan penggunaan AI di setiap tugas.

---

## Lampiran E: Glosarium Istilah AI/ML

Istilah-istilah kecerdasan buatan dan machine learning yang digunakan dalam buku ajar ini, disusun secara alfabetis. Format: **Istilah** — Definisi *(English equivalent)*.

---

**Activation Function (Fungsi Aktivasi)** — Fungsi non-linear yang diterapkan pada output setiap neuron dalam neural network, memungkinkan model mempelajari pola yang kompleks. Contoh: ReLU, Sigmoid, Tanh. *(Activation function)*

**Akurasi (Accuracy)** — Proporsi prediksi yang benar dari total prediksi model klasifikasi; $\text{Accuracy} = (TP + TN) / (TP + TN + FP + FN)$. *(Accuracy)*

**Algoritma (Algorithm)** — Serangkaian langkah terstruktur untuk menyelesaikan masalah atau mencapai tujuan tertentu. Dalam ML, algoritma adalah prosedur yang belajar dari data. *(Algorithm)*

**Artificial Intelligence (Kecerdasan Buatan)** — Bidang ilmu komputer yang berfokus pada pembuatan sistem yang dapat melakukan tugas yang biasanya memerlukan kecerdasan manusia, seperti pengenalan pola, pengambilan keputusan, dan pemahaman bahasa. *(Artificial Intelligence / AI)*

**Backpropagation** — Algoritma untuk menghitung gradien loss function terhadap setiap weight dalam neural network, digunakan bersama gradient descent untuk melatih model. *(Backpropagation)*

**Batch Size** — Jumlah sampel data yang diproses sebelum model memperbarui parameter internalnya selama pelatihan. *(Batch size)*

**Bias (Model)** — Kesalahan sistematis yang muncul dari asumsi yang terlalu sederhana dalam algoritma pembelajaran, menyebabkan underfitting. *(Bias)*

**Bias (Sosial/Algoritmik)** — Ketidakadilan sistematis dalam keputusan model ML yang merugikan kelompok tertentu, sering kali berasal dari data pelatihan yang tidak representatif. *(Algorithmic bias)*

**Bias-Variance Tradeoff** — Dilema fundamental dalam ML: model yang terlalu sederhana memiliki bias tinggi (underfitting), sementara model yang terlalu kompleks memiliki variance tinggi (overfitting). *(Bias-variance tradeoff)*

**Classification (Klasifikasi)** — Tugas supervised learning di mana model memprediksi label kategorikal (diskrit) untuk input yang diberikan. *(Classification)*

**Clustering** — Tugas unsupervised learning yang mengelompokkan data berdasarkan kesamaan tanpa label yang telah ditentukan sebelumnya. *(Clustering)*

**CNN (Convolutional Neural Network)** — Arsitektur neural network yang dirancang khusus untuk memproses data grid-like (seperti gambar), menggunakan operasi konvolusi untuk mengekstrak fitur. *(Convolutional Neural Network)*

**Confusion Matrix (Matriks Konfusi)** — Tabel yang merangkum performa model klasifikasi dengan menampilkan True Positives (TP), True Negatives (TN), False Positives (FP), dan False Negatives (FN). *(Confusion matrix)*

**Cross-Validation** — Teknik evaluasi model dengan membagi data menjadi beberapa lipatan (fold) untuk melatih dan menguji secara bergantian, mengurangi overfitting pada evaluasi. *(Cross-validation)*

**Data Augmentation** — Teknik memperbanyak data pelatihan dengan menerapkan transformasi (rotasi, flip, crop pada gambar) untuk meningkatkan robustness model. *(Data augmentation)*

**Decision Boundary** — Batas dalam feature space yang memisahkan kelas-kelas berbeda menurut model klasifikasi. *(Decision boundary)*

**Decision Tree (Pohon Keputusan)** — Model ML yang membuat keputusan dengan membagi data secara rekursif berdasarkan fitur, membentuk struktur seperti pohon. *(Decision tree)*

**Deep Learning** — Sub-bidang ML yang menggunakan neural networks dengan banyak lapisan (deep) untuk mempelajari representasi data yang semakin abstrak. *(Deep learning)*

**Dimensionality Reduction (Reduksi Dimensi)** — Teknik untuk mengurangi jumlah fitur dalam dataset sambil mempertahankan informasi penting. Contoh: PCA, t-SNE. *(Dimensionality reduction)*

**Dropout** — Teknik regularisasi dalam neural networks yang secara acak menonaktifkan sebagian neuron selama pelatihan untuk mencegah overfitting. *(Dropout)*

**Embedding** — Representasi numerik berdimensi rendah dari data berdimensi tinggi (seperti kata atau kategori), yang menangkap hubungan semantik. *(Embedding)*

**Ensemble Methods (Metode Ensemble)** — Teknik yang menggabungkan beberapa model untuk menghasilkan prediksi yang lebih baik. Contoh: Bagging, Boosting, Stacking. *(Ensemble methods)*

**Epoch** — Satu kali iterasi lengkap melalui seluruh dataset pelatihan selama proses training neural network. *(Epoch)*

**Explainability (Kemamputerangan)** — Kemampuan untuk memahami dan menjelaskan bagaimana model ML membuat keputusan. *(Explainability / Interpretability)*

**F1-Score** — Rata-rata harmonik antara presisi dan recall; $F_1 = 2 \cdot \frac{Precision \times Recall}{Precision + Recall}$. *(F1-score)*

**Feature (Fitur)** — Variabel input atau atribut yang digunakan model ML untuk membuat prediksi. *(Feature)*

**Feature Engineering** — Proses membuat fitur baru atau memodifikasi fitur yang ada untuk meningkatkan performa model ML. *(Feature engineering)*

**Feature Scaling** — Teknik menormalisasi atau menstandarisasi range nilai fitur agar algoritma ML dapat bekerja optimal. *(Feature scaling)*

**Fine-tuning** — Proses melatih ulang model pre-trained pada dataset baru yang lebih spesifik untuk menyesuaikan dengan tugas tertentu. *(Fine-tuning)*

**Gradient Boosting** — Teknik ensemble yang membangun model secara sekuensial, di mana setiap model baru berfokus pada memperbaiki kesalahan model sebelumnya. *(Gradient boosting)*

**Gradient Descent** — Algoritma optimisasi iteratif yang meminimalkan loss function dengan mengikuti arah gradien negatif. *(Gradient descent)*

**Hallucination** — Fenomena di mana model AI (terutama LLM) menghasilkan output yang terdengar meyakinkan tetapi faktanya salah atau tidak berdasar. *(Hallucination)*

**Hyperparameter** — Parameter model yang ditentukan sebelum pelatihan dimulai, bukan dipelajari dari data. Contoh: learning rate, jumlah hidden layers. *(Hyperparameter)*

**K-Means** — Algoritma clustering yang membagi data menjadi K kelompok berdasarkan jarak ke centroid terdekat. *(K-Means)*

**K-Nearest Neighbors (KNN)** — Algoritma klasifikasi/regresi yang membuat prediksi berdasarkan K tetangga terdekat dalam feature space. *(K-Nearest Neighbors)*

**Kernel** — Fungsi yang memetakan data ke dimensi yang lebih tinggi, digunakan dalam SVM dan CNN. Dalam CNN, kernel adalah filter yang mengekstrak fitur dari gambar. *(Kernel)*

**Label** — Nilai target atau output yang benar dalam supervised learning, digunakan untuk melatih dan mengevaluasi model. *(Label)*

**Large Language Model (LLM)** — Model deep learning berskala besar yang dilatih pada corpus teks masif untuk memahami dan menghasilkan bahasa manusia. Contoh: GPT, Claude, LLaMA. *(Large Language Model)*

**Learning Rate** — Hyperparameter yang mengontrol seberapa besar langkah update parameter pada setiap iterasi gradient descent. *(Learning rate)*

**Linear Regression (Regresi Linear)** — Model supervised learning yang memprediksi nilai kontinu menggunakan hubungan linear antara fitur dan target. *(Linear regression)*

**Logistic Regression (Regresi Logistik)** — Model klasifikasi yang memprediksi probabilitas kelas menggunakan fungsi sigmoid. *(Logistic regression)*

**Loss Function (Fungsi Loss)** — Fungsi yang mengukur seberapa jauh prediksi model dari nilai aktual; tujuan pelatihan adalah meminimalkan loss. *(Loss function)*

**Machine Learning (Pembelajaran Mesin)** — Sub-bidang AI di mana sistem belajar dari data untuk membuat prediksi atau keputusan tanpa diprogram secara eksplisit. *(Machine learning)*

**Max Pooling** — Operasi dalam CNN yang mengurangi dimensi spasial feature map dengan mengambil nilai maksimum dari setiap region. *(Max pooling)*

**Model** — Representasi matematis yang dipelajari dari data, digunakan untuk membuat prediksi pada data baru. *(Model)*

**Naive Bayes** — Algoritma klasifikasi probabilistik yang mengasumsikan independensi antar fitur, berdasarkan Teorema Bayes. *(Naive Bayes)*

**Natural Language Processing (NLP)** — Cabang AI yang berfokus pada interaksi antara komputer dan bahasa manusia. *(Natural Language Processing)*

**Neural Network (Jaringan Saraf Tiruan)** — Model komputasi yang terinspirasi dari jaringan saraf biologis, terdiri dari lapisan-lapisan neuron yang saling terhubung. *(Neural network)*

**Normalization (Normalisasi)** — Proses mengubah skala fitur ke rentang tertentu (biasanya 0-1) agar setiap fitur berkontribusi secara proporsional. *(Normalization)*

**Overfitting** — Kondisi di mana model terlalu cocok dengan data pelatihan sehingga kurang mampu menggeneralisasi ke data baru. *(Overfitting)*

**PCA (Principal Component Analysis)** — Teknik reduksi dimensi yang mentransformasi data ke komponen-komponen utama yang menangkap varians terbesar. *(Principal Component Analysis)*

**Perceptron** — Unit dasar neural network; model linear sederhana yang mengambil input berbobot, menjumlahkannya, dan menerapkan fungsi aktivasi. *(Perceptron)*

**Pipeline** — Urutan langkah pemrosesan data dan pemodelan yang dijalankan secara berurutan, memastikan konsistensi dan reproducibility. *(Pipeline)*

**Precision (Presisi)** — Proporsi prediksi positif yang memang positif; $Precision = TP / (TP + FP)$. *(Precision)*

**Preprocessing** — Langkah persiapan data sebelum digunakan untuk melatih model ML, termasuk pembersihan, transformasi, dan encoding. *(Preprocessing)*

**Random Forest** — Metode ensemble yang menggabungkan banyak decision tree yang dilatih pada subset data acak, menghasilkan prediksi yang lebih robust. *(Random Forest)*

**Recall (Sensitivitas)** — Proporsi kasus positif aktual yang berhasil dideteksi model; $Recall = TP / (TP + FN)$. *(Recall, Sensitivity)*

**Regularization (Regularisasi)** — Teknik untuk mencegah overfitting dengan menambahkan penalti pada kompleksitas model. Contoh: L1 (Lasso), L2 (Ridge). *(Regularization)*

**Reinforcement Learning** — Paradigma ML di mana agent belajar melalui interaksi dengan environment, menerima reward atau penalty berdasarkan aksinya. *(Reinforcement learning)*

**ReLU (Rectified Linear Unit)** — Fungsi aktivasi yang menghasilkan 0 untuk input negatif dan input itu sendiri untuk input positif; $f(x) = \max(0, x)$. *(ReLU)*

**Responsible AI (AI Bertanggung Jawab)** — Prinsip dan praktik pengembangan AI yang memperhatikan fairness, accountability, transparency, dan safety. *(Responsible AI)*

**ROC Curve** — Grafik yang menunjukkan trade-off antara True Positive Rate dan False Positive Rate pada berbagai threshold klasifikasi. *(ROC Curve)*

**Sigmoid** — Fungsi aktivasi yang memetakan input ke rentang (0, 1); $\sigma(x) = 1 / (1 + e^{-x})$. Digunakan dalam logistic regression dan neural networks. *(Sigmoid function)*

**Standardization (Standarisasi)** — Proses mengubah skala fitur agar memiliki mean 0 dan standard deviation 1; $z = (x - \mu) / \sigma$. *(Standardization)*

**Supervised Learning (Pembelajaran Terawasi)** — Paradigma ML di mana model belajar dari data berlabel — input dipasangkan dengan output yang benar. *(Supervised learning)*

**SVM (Support Vector Machine)** — Algoritma klasifikasi yang mencari hyperplane optimal untuk memisahkan kelas-kelas data dengan margin maksimum. *(Support Vector Machine)*

**TF-IDF (Term Frequency-Inverse Document Frequency)** — Metode representasi teks yang mengukur pentingnya suatu kata dalam dokumen relatif terhadap koleksi dokumen. *(TF-IDF)*

**Training Set** — Subset data yang digunakan untuk melatih model ML. *(Training set)*

**Transfer Learning** — Teknik menggunakan model yang telah dilatih pada tugas/dataset besar sebagai titik awal untuk tugas baru yang berbeda. *(Transfer learning)*

**Transformer** — Arsitektur neural network yang menggunakan mekanisme self-attention, menjadi fondasi LLM modern seperti GPT dan BERT. *(Transformer)*

**Test Set** — Subset data yang digunakan untuk mengevaluasi performa akhir model ML setelah pelatihan selesai. *(Test set)*

**Underfitting** — Kondisi di mana model terlalu sederhana sehingga tidak mampu menangkap pola dalam data pelatihan maupun data baru. *(Underfitting)*

**Unsupervised Learning (Pembelajaran Tidak Terawasi)** — Paradigma ML di mana model belajar dari data tanpa label, mencari pola dan struktur tersembunyi. *(Unsupervised learning)*

**Validation Set** — Subset data yang digunakan untuk mengevaluasi performa model selama proses pelatihan dan tuning hyperparameter. *(Validation set)*

**Variance (Model)** — Sensitivitas model terhadap fluktuasi kecil dalam data pelatihan; variance tinggi menyebabkan overfitting. *(Variance)*

**Weight (Bobot)** — Parameter dalam model ML/neural network yang dipelajari selama pelatihan; menentukan kekuatan koneksi antar neuron. *(Weight)*

**Word Embedding** — Representasi vektor berdimensi rendah untuk kata-kata, di mana kata-kata dengan makna serupa memiliki representasi yang dekat. Contoh: Word2Vec, GloVe. *(Word embedding)*

**XGBoost** — Implementasi gradient boosting yang sangat efisien dan populer, sering memenangkan kompetisi ML. Singkatan dari *eXtreme Gradient Boosting*. *(XGBoost)*

---

## Lampiran F: Referensi Dataset Indonesia untuk ML

Berikut adalah daftar sumber dataset Indonesia yang dapat digunakan untuk proyek machine learning.

### F.1 Sumber Data Pemerintah

| Sumber | URL | Jenis Data | Contoh Penggunaan ML |
|--------|-----|-----------|---------------------|
| **BPS (Badan Pusat Statistik)** | https://www.bps.go.id | Statistik sosial, ekonomi, demografi per provinsi | Prediksi kemiskinan, klasifikasi wilayah, clustering provinsi |
| **Open Data Jakarta** | https://data.jakarta.go.id | Data DKI Jakarta (transportasi, lingkungan, kesehatan) | Prediksi kualitas udara, deteksi anomali banjir, optimasi transportasi |
| **Satu Data Indonesia** | https://data.go.id | Agregasi data pemerintah pusat dan daerah | Berbagai proyek ML dengan data publik Indonesia |
| **Bank Indonesia** | https://www.bi.go.id/id/statistik | Data moneter, perbankan, sistem pembayaran | Prediksi inflasi, analisis time series ekonomi |
| **Kemenkes RI** | https://www.kemkes.go.id | Data kesehatan nasional | Prediksi penyebaran penyakit, klasifikasi risiko kesehatan |

### F.2 Sumber Data Akademik dan Komunitas

| Sumber | URL | Jenis Data | Contoh Penggunaan ML |
|--------|-----|-----------|---------------------|
| **Kaggle Indonesia** | https://www.kaggle.com/search?q=indonesia | Beragam dataset Indonesia di Kaggle | Kompetisi dan proyek ML |
| **UCI ML Repository** | https://archive.ics.uci.edu/ml | Dataset klasik ML | Benchmark algoritma |
| **IndoNLU** | https://github.com/indobenchmark | Dataset NLP Bahasa Indonesia | Sentiment analysis, NER, text classification dalam Bahasa Indonesia |
| **Indonesian NLP** | https://github.com/indonesian-nlp | Kumpulan resource NLP Indonesia | Word embeddings, pre-trained models untuk Bahasa Indonesia |

### F.3 Dataset Spesifik per Bab

| Bab | Dataset yang Direkomendasikan | Sumber | Tugas ML |
|-----|------------------------------|--------|----------|
| 3 | Data Kualitas Udara DKI Jakarta | Open Data Jakarta | Preprocessing, EDA |
| 5 | Data Harga Properti Jabodetabek | Kaggle Indonesia | Regresi (prediksi harga) |
| 6 | Data Sentimen Review E-commerce | IndoNLU | Klasifikasi sentimen |
| 7 | Data Kredit Perbankan Indonesia | Simulasi berdasarkan BPS | Klasifikasi risiko kredit |
| 8 | Data Pelanggan E-commerce | Kaggle Indonesia | Clustering segmentasi pelanggan |
| 9 | Data MNIST / Fashion-MNIST | TensorFlow Datasets | Klasifikasi gambar (benchmark) |
| 11 | Data Berita Bahasa Indonesia | Indonesian NLP | Text classification, NER |
| 12 | Data Batik Indonesia | Kaggle Indonesia | Klasifikasi gambar batik |
| 14 | Data End-to-End Pilihan Mahasiswa | Berbagai sumber | Proyek akhir ML |

### F.4 Tips Menggunakan Data Indonesia

1. **Perhatikan format tanggal** — Format Indonesia (DD/MM/YYYY) berbeda dari format internasional (MM/DD/YYYY atau YYYY-MM-DD)
2. **Encoding karakter** — Gunakan `encoding='utf-8'` atau `encoding='latin-1'` saat membaca CSV
3. **Separator desimal** — Beberapa data Indonesia menggunakan koma (`,`) sebagai separator desimal
4. **Missing values** — Perhatikan representasi missing values yang bervariasi: `-`, `N/A`, `kosong`, `0`
5. **Privasi data** — Selalu anonimkan data personal sebelum digunakan dalam proyek ML

```python
# Contoh membaca dataset Indonesia dengan pandas
import pandas as pd

# Dataset BPS dengan separator titik koma
df = pd.read_csv('data_bps.csv', sep=';', encoding='utf-8')

# Konversi format tanggal Indonesia
df['tanggal'] = pd.to_datetime(df['tanggal'], format='%d/%m/%Y')

# Handling separator desimal koma
df['nilai'] = df['nilai'].str.replace(',', '.').astype(float)

print(f"Dataset: {df.shape[0]} baris, {df.shape[1]} kolom")
df.head()
```

---

## Lampiran G: Cheat Sheet scikit-learn API

### G.1 Workflow Umum scikit-learn

```python
# === WORKFLOW STANDAR scikit-learn ===

# 1. Import library
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# 2. Siapkan data
X = df.drop('target', axis=1)   # Fitur
y = df['target']                 # Label

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Preprocessing (scaling)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # HANYA transform, BUKAN fit_transform!

# 5. Buat dan latih model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# 6. Prediksi dan evaluasi
y_pred = model.predict(X_test_scaled)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred))
```

### G.2 Algoritma Supervised Learning

```python
# === REGRESI ===

# Linear Regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Ridge Regression (L2 regularization)
from sklearn.linear_model import Ridge
model = Ridge(alpha=1.0)

# Lasso Regression (L1 regularization)
from sklearn.linear_model import Lasso
model = Lasso(alpha=0.1)

# Elastic Net
from sklearn.linear_model import ElasticNet
model = ElasticNet(alpha=0.1, l1_ratio=0.5)

# Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# === KLASIFIKASI ===

# Logistic Regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000)

# K-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)

# Naive Bayes
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()

# Support Vector Machine
from sklearn.svm import SVC
model = SVC(kernel='rbf', C=1.0)

# Decision Tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth=5)

# Random Forest
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, max_depth=10)

# Gradient Boosting
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
```

### G.3 Algoritma Unsupervised Learning

```python
# === CLUSTERING ===

# K-Means
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X_scaled)

# DBSCAN
from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X_scaled)

# Hierarchical Clustering
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=3)
labels = hc.fit_predict(X_scaled)

# === REDUKSI DIMENSI ===

# PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print(f"Explained variance ratio: {pca.explained_variance_ratio_}")

# t-SNE (untuk visualisasi)
from sklearn.manifold import TSNE
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X_scaled)
```

### G.4 Preprocessing

```python
# === SCALING ===
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# StandardScaler: mean=0, std=1
scaler = StandardScaler()

# MinMaxScaler: range [0, 1]
scaler = MinMaxScaler()

# RobustScaler: robust terhadap outlier
scaler = RobustScaler()

# === ENCODING ===
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Label Encoding (ordinal)
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# One-Hot Encoding
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse_output=False, drop='first')
X_encoded = ohe.fit_transform(X_categorical)

# === HANDLING MISSING VALUES ===
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')  # atau 'median', 'most_frequent'
X_imputed = imputer.fit_transform(X)
```

### G.5 Evaluasi Model

```python
# === METRIK KLASIFIKASI ===
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                              f1_score, confusion_matrix, classification_report,
                              roc_auc_score, roc_curve)

print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.4f}")
print(f"Recall:    {recall_score(y_test, y_pred, average='weighted'):.4f}")
print(f"F1-Score:  {f1_score(y_test, y_pred, average='weighted'):.4f}")
print(classification_report(y_test, y_pred))

# === METRIK REGRESI ===
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

print(f"MSE:  {mean_squared_error(y_test, y_pred):.4f}")
print(f"RMSE: {mean_squared_error(y_test, y_pred, squared=False):.4f}")
print(f"MAE:  {mean_absolute_error(y_test, y_pred):.4f}")
print(f"R2:   {r2_score(y_test, y_pred):.4f}")

# === CROSS-VALIDATION ===
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"CV Accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")
```

### G.6 Hyperparameter Tuning

```python
# Grid Search
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10]
}
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)
print(f"Best params: {grid_search.best_params_}")
print(f"Best score:  {grid_search.best_score_:.4f}")

# Random Search
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

param_dist = {
    'n_estimators': randint(50, 300),
    'max_depth': randint(3, 20),
}
random_search = RandomizedSearchCV(model, param_dist, n_iter=50, cv=5,
                                    scoring='accuracy', random_state=42)
random_search.fit(X_train, y_train)
```

### G.7 Pipeline

```python
from sklearn.pipeline import Pipeline

# Pipeline lengkap: preprocessing + model
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier(n_estimators=100))
])

# Latih dan evaluasi pipeline
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(f"Pipeline Accuracy: {accuracy_score(y_test, y_pred):.4f}")
```

---

## Lampiran H: Cheat Sheet Keras API

### H.1 Membangun Model Sequential

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# === MODEL SEQUENTIAL DASAR ===
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(n_features,)),
    layers.Dropout(0.3),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(32, activation='relu'),
    layers.Dense(n_classes, activation='softmax')  # Klasifikasi multi-kelas
])

# Untuk klasifikasi biner, gunakan:
# layers.Dense(1, activation='sigmoid')

# Untuk regresi, gunakan:
# layers.Dense(1, activation='linear')  # atau tanpa aktivasi
```

### H.2 Kompilasi Model

```python
# === KLASIFIKASI MULTI-KELAS ===
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',  # jika label integer
    # loss='categorical_crossentropy',       # jika label one-hot encoded
    metrics=['accuracy']
)

# === KLASIFIKASI BINER ===
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# === REGRESI ===
model.compile(
    optimizer='adam',
    loss='mse',      # Mean Squared Error
    metrics=['mae']   # Mean Absolute Error
)

# === OPTIMIZER CUSTOM ===
optimizer = keras.optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='mse', metrics=['mae'])
```

### H.3 Melatih Model

```python
# === TRAINING DASAR ===
history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,      # 20% data training untuk validasi
    # atau validation_data=(X_val, y_val),
    verbose=1
)

# === TRAINING DENGAN CALLBACKS ===
callbacks = [
    # Hentikan pelatihan jika val_loss tidak membaik selama 10 epoch
    keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=10,
        restore_best_weights=True
    ),
    # Simpan model terbaik
    keras.callbacks.ModelCheckpoint(
        'best_model.h5',
        monitor='val_loss',
        save_best_only=True
    ),
    # Kurangi learning rate jika val_loss stagnan
    keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.5,
        patience=5,
        min_lr=1e-6
    )
]

history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=callbacks,
    verbose=1
)
```

### H.4 Evaluasi dan Prediksi

```python
# Evaluasi pada test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Loss:     {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")

# Prediksi
predictions = model.predict(X_test)

# Untuk klasifikasi: ambil kelas dengan probabilitas tertinggi
predicted_classes = predictions.argmax(axis=1)

# Untuk klasifikasi biner: gunakan threshold 0.5
predicted_classes = (predictions > 0.5).astype(int)
```

### H.5 Visualisasi Training History

```python
import matplotlib.pyplot as plt

# Plot Loss
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(history.history['loss'], label='Training Loss')
axes[0].plot(history.history['val_loss'], label='Validation Loss')
axes[0].set_title('Loss per Epoch')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Loss')
axes[0].legend()

# Plot Accuracy
axes[1].plot(history.history['accuracy'], label='Training Accuracy')
axes[1].plot(history.history['val_accuracy'], label='Validation Accuracy')
axes[1].set_title('Accuracy per Epoch')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Accuracy')
axes[1].legend()

plt.tight_layout()
plt.show()
```

### H.6 Convolutional Neural Network (CNN)

```python
# === CNN UNTUK KLASIFIKASI GAMBAR ===
model = keras.Sequential([
    # Blok Konvolusi 1
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, channels)),
    layers.MaxPooling2D((2, 2)),

    # Blok Konvolusi 2
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Blok Konvolusi 3
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Flatten dan Dense layers
    layers.Flatten(),
    layers.Dropout(0.5),
    layers.Dense(128, activation='relu'),
    layers.Dense(n_classes, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()
```

### H.7 Transfer Learning

```python
# === TRANSFER LEARNING DENGAN MobileNetV2 ===

# 1. Load model pre-trained (tanpa top layer)
base_model = keras.applications.MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

# 2. Freeze base model
base_model.trainable = False

# 3. Tambah custom layers di atas
model = keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.3),
    layers.Dense(128, activation='relu'),
    layers.Dense(n_classes, activation='softmax')
])

# 4. Kompilasi dan latih
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 5. Fine-tuning (opsional — setelah initial training)
base_model.trainable = True
# Freeze semua layer kecuali 20 layer terakhir
for layer in base_model.layers[:-20]:
    layer.trainable = False

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-5),  # learning rate kecil!
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

### H.8 Simpan dan Muat Model

```python
# Simpan seluruh model
model.save('model_lengkap.h5')
# atau format SavedModel
model.save('model_directory/')

# Muat model
loaded_model = keras.models.load_model('model_lengkap.h5')

# Simpan hanya weights
model.save_weights('model_weights.h5')

# Muat weights ke arsitektur yang sama
model.load_weights('model_weights.h5')

# Simpan ke Google Drive (di Colab)
model.save('/content/drive/MyDrive/models/model_final.h5')
```

### H.9 Ringkasan Fungsi Aktivasi

| Fungsi | Formula | Digunakan Untuk | Catatan |
|--------|---------|-----------------|---------|
| `relu` | $\max(0, x)$ | Hidden layers (default) | Cepat, efisien, standar |
| `sigmoid` | $1 / (1 + e^{-x})$ | Output klasifikasi biner | Range (0, 1) |
| `softmax` | $e^{x_i} / \sum e^{x_j}$ | Output klasifikasi multi-kelas | Menghasilkan probabilitas |
| `tanh` | $(e^x - e^{-x}) / (e^x + e^{-x})$ | Hidden layers, RNN | Range (-1, 1) |
| `linear` | $x$ | Output regresi | Tanpa transformasi |

### H.10 Ringkasan Loss Functions

| Loss Function | Digunakan Untuk | Kode Keras |
|--------------|-----------------|------------|
| MSE | Regresi | `'mse'` |
| MAE | Regresi (robust terhadap outlier) | `'mae'` |
| Binary Crossentropy | Klasifikasi biner | `'binary_crossentropy'` |
| Categorical Crossentropy | Multi-kelas (label one-hot) | `'categorical_crossentropy'` |
| Sparse Categorical Crossentropy | Multi-kelas (label integer) | `'sparse_categorical_crossentropy'` |

---

*Lampiran ini merupakan bagian dari buku ajar "Kecerdasan Buatan dan Machine Learning" untuk Program Studi Informatika, Universitas Al Azhar Indonesia.*

*Penulis: Tri Aji Nugroho, S.T., M.T.*

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
— Program Studi Informatika, Universitas Al Azhar Indonesia
