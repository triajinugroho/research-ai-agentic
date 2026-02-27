# Minggu 13: Pengantar Machine Learning Statistik

## Mata Kuliah: Analisis Data Statistik
### Prodi Informatika — Universitas Al Azhar Indonesia — Semester Genap 2025/2026

---

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Minggu** | 13 |
| **Topik** | Pengantar Machine Learning Statistik |
| **CPMK** | CPMK-7: Mengevaluasi dan merancang analisis data end-to-end dengan memanfaatkan AI sebagai co-analyst secara bertanggung jawab |
| **Sub-CPMK** | 13.1: Membedakan pendekatan machine learning dan statistik tradisional |
| | 13.2: Membangun model klasifikasi sederhana (decision tree, k-NN) dan mengevaluasi performanya |
| **Bloom's Taxonomy** | C5 (Evaluate) |
| **Durasi** | 100 menit (50 menit teori + 50 menit praktikum) |
| **Prasyarat Modul** | Minggu 9-12 (Regresi, ANOVA, Chi-Square, Logistic Regression) |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Menjelaskan** perbedaan paradigma antara statistik tradisional dan machine learning, serta memahami kapan menggunakan masing-masing pendekatan
2. **Membedakan** supervised vs unsupervised learning, serta classification vs regression dalam konteks ML
3. **Membangun** model Decision Tree dan k-Nearest Neighbors (k-NN) menggunakan scikit-learn
4. **Menerapkan** teknik train-test split dan memahami konsep cross-validation
5. **Mengevaluasi** performa model klasifikasi menggunakan accuracy, precision, recall, F1-score, dan confusion matrix

---

## Materi Pembelajaran

### 1. Dari Statistik ke Machine Learning: Paradigma Berbeda, Fondasi Sama

Selama 12 minggu terakhir, kalian telah belajar statistik — mulai dari deskriptif, inferensi, regresi, hingga ANOVA. Sekarang kita akan melihat bagaimana **fondasi statistik yang sama** melahirkan pendekatan baru yang disebut **machine learning (ML)**.

#### 1.1 Statistik Tradisional vs Machine Learning

| Aspek | Statistik Tradisional | Machine Learning |
|-------|----------------------|------------------|
| **Tujuan utama** | Memahami hubungan antar variabel (inference) | Membuat prediksi seakurat mungkin (prediction) |
| **Pendekatan** | Model-driven: mulai dari asumsi distribusi | Data-driven: biarkan data "berbicara" |
| **Asumsi** | Banyak asumsi (normalitas, homoscedasticity, dll.) | Lebih sedikit asumsi, lebih fleksibel |
| **Interpretasi** | Sangat penting (p-value, coefficient meaning) | Kadang dikorbankan demi akurasi (black box) |
| **Ukuran data** | Bisa bekerja dengan sampel kecil | Biasanya butuh data besar |
| **Overfitting** | Kurang dibahas eksplisit | Concern utama, ada mekanisme pencegahan |
| **Evaluasi** | R-squared, p-value, confidence interval | Accuracy, precision, recall, cross-validation |

#### 1.2 Dimana Mereka Bertemu?

Penting dipahami bahwa ML **bukan** pengganti statistik. Keduanya saling melengkapi:

- **Regresi linear** yang kalian pelajari di Minggu 9-10 adalah salah satu algoritma ML paling dasar
- **Logistic regression** (Minggu 12) digunakan secara luas di ML untuk klasifikasi
- **Asumsi distribusi** tetap penting untuk memahami *mengapa* model bekerja
- **P-value dan confidence interval** tetap relevan saat kita ingin *memahami*, bukan hanya memprediksi

> **Analogi:** Statistik seperti seorang dokter yang ingin memahami *mengapa* pasien sakit (diagnosis). Machine learning seperti seorang dokter yang ingin memprediksi *siapa* yang akan sakit berikutnya (prediksi). Keduanya butuh pengetahuan kedokteran (fondasi statistik).

---

### 2. Supervised vs Unsupervised Learning

#### 2.1 Supervised Learning

Dalam supervised learning, kita memiliki **data berlabel** — artinya kita tahu "jawaban yang benar" untuk setiap observasi.

**Contoh:**
- Email diberi label "spam" atau "bukan spam"
- Bunga iris diberi label spesiesnya (setosa, versicolor, virginica)
- Rumah diberi label harganya

Algoritma belajar pola dari data berlabel ini, lalu memprediksi label untuk data baru.

#### 2.2 Unsupervised Learning

Dalam unsupervised learning, **tidak ada label**. Algoritma mencari pola atau struktur tersembunyi dalam data.

**Contoh:**
- Mengelompokkan pelanggan berdasarkan perilaku belanja (clustering)
- Menemukan topik tersembunyi dalam kumpulan dokumen
- Reduksi dimensi untuk visualisasi data berdimensi tinggi

> **Catatan:** Di modul ini, kita fokus pada **supervised learning** — khususnya klasifikasi.

#### 2.3 Classification vs Regression dalam ML

| | Classification | Regression |
|--|---------------|------------|
| **Output** | Kategori/label (diskret) | Nilai numerik (kontinu) |
| **Contoh** | Spam/bukan spam, jenis bunga | Harga rumah, suhu besok |
| **Metrik** | Accuracy, precision, recall | RMSE, MAE, R-squared |
| **Algoritma** | Decision Tree, k-NN, Logistic Regression | Linear Regression, Random Forest Regression |

Regresi linear yang kalian pelajari di Minggu 9-10 adalah contoh **regression** dalam konteks ML. Hari ini kita akan fokus pada **classification**.

---

### 3. Decision Tree: Konsep dan Implementasi

#### 3.1 Apa Itu Decision Tree?

Decision tree adalah algoritma yang membuat keputusan dengan cara **memecah data berdasarkan pertanyaan-pertanyaan berurutan**, mirip seperti flowchart.

**Analogi:** Bayangkan kalian bermain game "20 Questions" — kalian bertanya ya/tidak berulang-ulang untuk menebak jawaban. Decision tree bekerja dengan cara yang sama.

```
                    [Petal Length <= 2.45?]
                    /                     \
                  Ya                      Tidak
                  /                         \
            [Setosa]              [Petal Width <= 1.75?]
                                  /                    \
                                Ya                    Tidak
                                /                        \
                        [Versicolor]                [Virginica]
```

#### 3.2 Information Gain dan Entropy

Bagaimana tree memutuskan pertanyaan mana yang ditanyakan pertama? Jawabannya: **Information Gain**.

**Entropy** mengukur "ketidakpastian" dalam data:

```
Entropy(S) = -sum(p_i * log2(p_i))
```

- Jika semua data dalam satu kelas: Entropy = 0 (pasti, tidak ada ketidakpastian)
- Jika data terbagi rata 50-50: Entropy = 1 (maksimum ketidakpastian)

**Information Gain** = Entropy sebelum split - Entropy setelah split

Tree memilih fitur dan threshold yang memberikan **information gain tertinggi** di setiap langkah.

#### 3.3 Implementasi dengan Python

```python
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load dataset iris
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

print("Fitur yang tersedia:")
print(X.columns.tolist())
print(f"\nJumlah sampel: {X.shape[0]}")
print(f"Jumlah kelas: {len(set(y))}")
print(f"Nama kelas: {iris.target_names}")
```

```python
# Bangun model Decision Tree
dt_model = DecisionTreeClassifier(
    max_depth=3,          # Batasi kedalaman tree agar tidak terlalu kompleks
    random_state=42       # Reproducibility
)
dt_model.fit(X, y)

# Visualisasi tree
plt.figure(figsize=(16, 10))
plot_tree(
    dt_model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,          # Warnai node berdasarkan kelas mayoritas
    rounded=True,
    fontsize=10
)
plt.title("Decision Tree untuk Klasifikasi Iris", fontsize=14)
plt.tight_layout()
plt.show()
```

> **Kelebihan Decision Tree:** Mudah diinterpretasi (bisa divisualisasikan), tidak butuh normalisasi data, bisa handle fitur numerik dan kategorikal.
>
> **Kelemahan:** Cenderung overfitting jika tidak dibatasi (pruning), sensitif terhadap perubahan kecil dalam data.

---

### 4. k-Nearest Neighbors (k-NN): Klasifikasi Berbasis Jarak

#### 4.1 Konsep k-NN

k-NN adalah algoritma yang sangat intuitif: untuk mengklasifikasikan data baru, **lihat k tetangga terdekat** dan ambil "suara mayoritas" dari kelas mereka.

**Analogi:** Jika kalian pindah ke kota baru dan ingin tahu restoran mana yang bagus, kalian bertanya ke 5 tetangga terdekat. Jika 4 dari 5 bilang Restoran A, kemungkinan besar Restoran A memang bagus.

#### 4.2 Memilih Nilai k

Pemilihan k sangat penting:

| k | Karakteristik |
|---|---------------|
| **k kecil** (misal k=1) | Sangat sensitif terhadap noise, batas keputusan tidak halus (overfitting) |
| **k besar** (misal k=50) | Terlalu "smooth", bisa kehilangan pola lokal (underfitting) |
| **Aturan praktis** | Mulai dengan k = sqrt(n), di mana n = jumlah data, lalu eksperimen |

**Tips:** Gunakan k ganjil untuk menghindari "seri" dalam voting (khususnya binary classification).

#### 4.3 Distance Metric

k-NN menggunakan **jarak** untuk menentukan "tetangga terdekat". Jarak yang paling umum:

- **Euclidean Distance:** sqrt(sum((x_i - y_i)^2)) — default di sklearn
- **Manhattan Distance:** sum(|x_i - y_i|) — lebih robust terhadap outlier

> **Penting:** Karena k-NN bergantung pada jarak, **skala fitur sangat berpengaruh**. Fitur dengan range besar akan mendominasi perhitungan jarak. Solusi: **normalisasi/standardisasi** data sebelum menggunakan k-NN.

#### 4.4 Implementasi dengan Python

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Standardisasi fitur (penting untuk k-NN!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Bangun model k-NN
knn_model = KNeighborsClassifier(
    n_neighbors=5,        # k = 5
    metric='euclidean'    # Default distance metric
)
knn_model.fit(X_scaled, y)

print(f"Model k-NN dengan k={knn_model.n_neighbors}")
print(f"Accuracy pada training data: {knn_model.score(X_scaled, y):.4f}")
```

---

### 5. Train-Test Split: Mengapa dan Bagaimana

#### 5.1 Masalah: Overfitting

Jika kita melatih model pada **semua** data, lalu mengevaluasi pada data yang **sama**, hasilnya akan terlalu optimis. Ini seperti ujian di mana soalnya persis sama dengan latihan — nilai tinggi belum tentu berarti paham.

Model yang "menghafal" data training tapi gagal pada data baru disebut **overfitting**.

#### 5.2 Solusi: Train-Test Split

Kita membagi data menjadi dua bagian:
- **Training set** (biasanya 70-80%): digunakan untuk melatih model
- **Test set** (biasanya 20-30%): disimpan dan hanya digunakan untuk evaluasi akhir

```python
from sklearn.model_selection import train_test_split

# Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,        # 20% untuk testing
    random_state=42,      # Reproducibility
    stratify=y            # Pastikan proporsi kelas sama di train dan test
)

print(f"Training set: {X_train.shape[0]} sampel")
print(f"Test set: {X_test.shape[0]} sampel")
print(f"\nProporsi kelas di training set:")
print(pd.Series(y_train).value_counts(normalize=True))
print(f"\nProporsi kelas di test set:")
print(pd.Series(y_test).value_counts(normalize=True))
```

> **Parameter `stratify=y`** memastikan bahwa proporsi kelas di training dan test set sama dengan proporsi di data asli. Sangat penting untuk dataset yang tidak seimbang (imbalanced).

#### 5.3 Cross-Validation: Evaluasi Lebih Robust

Train-test split hanya memberikan **satu estimasi** performa. Bagaimana jika split tersebut "kebetulan" bagus atau buruk?

**K-Fold Cross-Validation** mengatasi masalah ini:

1. Bagi data menjadi K bagian (fold) yang sama besar
2. Untuk setiap fold: gunakan fold tersebut sebagai test, sisanya sebagai training
3. Hitung rata-rata performa dari K percobaan

```
Fold 1: [TEST] [Train] [Train] [Train] [Train]  → Score 1
Fold 2: [Train] [TEST] [Train] [Train] [Train]  → Score 2
Fold 3: [Train] [Train] [TEST] [Train] [Train]  → Score 3
Fold 4: [Train] [Train] [Train] [TEST] [Train]  → Score 4
Fold 5: [Train] [Train] [Train] [Train] [TEST]  → Score 5

Final Score = Rata-rata(Score 1, 2, 3, 4, 5)
```

```python
from sklearn.model_selection import cross_val_score

# 5-Fold Cross-Validation untuk Decision Tree
dt_scores = cross_val_score(
    DecisionTreeClassifier(max_depth=3, random_state=42),
    X, y,
    cv=5,                 # 5-fold
    scoring='accuracy'
)

print("Decision Tree - 5-Fold Cross-Validation:")
print(f"  Scores per fold: {dt_scores}")
print(f"  Mean Accuracy: {dt_scores.mean():.4f}")
print(f"  Std Deviation: {dt_scores.std():.4f}")
```

---

### 6. Evaluation Metrics: Mengukur Performa Klasifikasi

#### 6.1 Confusion Matrix

Confusion matrix adalah tabel yang menunjukkan jumlah prediksi benar dan salah per kelas:

```
                    Predicted
                 Positive  Negative
Actual Positive    TP        FN
       Negative    FP        TN

TP = True Positive   → Benar diprediksi positif
TN = True Negative   → Benar diprediksi negatif
FP = False Positive  → Salah diprediksi positif (Type I Error)
FN = False Negative  → Salah diprediksi negatif (Type II Error)
```

#### 6.2 Metrik dari Confusion Matrix

| Metrik | Formula | Arti | Kapan Penting |
|--------|---------|------|---------------|
| **Accuracy** | (TP + TN) / Total | Seberapa sering model benar secara keseluruhan | Data seimbang |
| **Precision** | TP / (TP + FP) | Dari yang diprediksi positif, berapa yang benar | Ketika FP mahal (spam filter) |
| **Recall** | TP / (TP + FN) | Dari yang sebenarnya positif, berapa yang terdeteksi | Ketika FN mahal (deteksi penyakit) |
| **F1-Score** | 2 * (P * R) / (P + R) | Harmonic mean precision & recall | Keseimbangan P dan R |

> **Contoh nyata:**
> - **Deteksi kanker:** Recall lebih penting — kita tidak ingin melewatkan pasien yang sakit (FN)
> - **Spam filter:** Precision lebih penting — kita tidak ingin email penting masuk ke spam (FP)

#### 6.3 Implementasi Evaluasi Lengkap

```python
from sklearn.metrics import (
    confusion_matrix, classification_report,
    accuracy_score, ConfusionMatrixDisplay
)

# Train model pada training set
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)

# Prediksi pada test set
y_pred = dt.predict(X_test)

# Confusion Matrix
print("=== Confusion Matrix ===")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Visualisasi Confusion Matrix
fig, ax = plt.subplots(figsize=(8, 6))
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)
disp.plot(ax=ax, cmap='Blues')
plt.title("Confusion Matrix — Decision Tree", fontsize=14)
plt.tight_layout()
plt.show()

# Classification Report
print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
```

**Output classification_report akan terlihat seperti:**

```
              precision    recall  f1-score   support

      setosa       1.00      1.00      1.00        10
  versicolor       1.00      1.00      1.00        10
   virginica       1.00      1.00      1.00        10

    accuracy                           1.00        30
   macro avg       1.00      1.00      1.00        30
weighted avg       1.00      1.00      1.00        30
```

---

## Studi Kasus: Klasifikasi Dataset Iris — End-to-End

Sekarang kita akan menggabungkan semua konsep dalam satu alur analisis lengkap.

```python
# ============================================
# STUDI KASUS: Klasifikasi Iris End-to-End
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

# --- Langkah 1: Load dan Eksplorasi Data ---
print("=" * 50)
print("LANGKAH 1: EKSPLORASI DATA")
print("=" * 50)

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

print(df.head())
print(f"\nShape: {df.shape}")
print(f"\nDistribusi kelas:")
print(df['species'].value_counts())
print(f"\nStatistik deskriptif:")
print(df.describe())
```

```python
# --- Langkah 2: Visualisasi Data ---
print("\n" + "=" * 50)
print("LANGKAH 2: VISUALISASI DATA")
print("=" * 50)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Pairplot menggunakan 2 fitur terpenting
for i, feature in enumerate(iris.feature_names):
    ax = axes[i // 2, i % 2]
    for species_idx, species_name in enumerate(iris.target_names):
        mask = iris.target == species_idx
        ax.hist(df[feature][mask], alpha=0.6, label=species_name, bins=15)
    ax.set_xlabel(feature)
    ax.set_ylabel('Frekuensi')
    ax.legend()
    ax.set_title(f'Distribusi {feature}')

plt.suptitle("Distribusi Fitur per Spesies Iris", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

```python
# --- Langkah 3: Persiapan Data ---
print("\n" + "=" * 50)
print("LANGKAH 3: TRAIN-TEST SPLIT")
print("=" * 50)

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Standardisasi (untuk k-NN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Training: {X_train.shape[0]} sampel")
print(f"Testing: {X_test.shape[0]} sampel")
```

```python
# --- Langkah 4: Model Decision Tree ---
print("\n" + "=" * 50)
print("LANGKAH 4: DECISION TREE")
print("=" * 50)

dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

print("Classification Report — Decision Tree:")
print(classification_report(y_test, y_pred_dt, target_names=iris.target_names))

# Cross-validation
dt_cv = cross_val_score(dt, X, y, cv=5, scoring='accuracy')
print(f"5-Fold CV Accuracy: {dt_cv.mean():.4f} (+/- {dt_cv.std():.4f})")
```

```python
# --- Langkah 5: Model k-NN ---
print("\n" + "=" * 50)
print("LANGKAH 5: k-NEAREST NEIGHBORS")
print("=" * 50)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
y_pred_knn = knn.predict(X_test_scaled)

print("Classification Report — k-NN (k=5):")
print(classification_report(y_test, y_pred_knn, target_names=iris.target_names))

# Cross-validation
knn_cv = cross_val_score(knn, scaler.fit_transform(X), y, cv=5, scoring='accuracy')
print(f"5-Fold CV Accuracy: {knn_cv.mean():.4f} (+/- {knn_cv.std():.4f})")
```

```python
# --- Langkah 6: Perbandingan dan Eksperimen k ---
print("\n" + "=" * 50)
print("LANGKAH 6: EKSPERIMEN NILAI k")
print("=" * 50)

k_values = range(1, 21)
cv_scores = []

for k in k_values:
    knn_temp = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn_temp, scaler.fit_transform(X), y, cv=5)
    cv_scores.append(scores.mean())

plt.figure(figsize=(10, 6))
plt.plot(k_values, cv_scores, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Nilai k', fontsize=12)
plt.ylabel('Cross-Validation Accuracy', fontsize=12)
plt.title('Pengaruh Nilai k terhadap Akurasi k-NN', fontsize=14)
plt.xticks(k_values)
plt.grid(True, alpha=0.3)
plt.axhline(y=max(cv_scores), color='r', linestyle='--', alpha=0.5,
            label=f'Best: k={list(k_values)[cv_scores.index(max(cv_scores))]}, '
                  f'Acc={max(cv_scores):.4f}')
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()
```

```python
# --- Langkah 7: Perbandingan Model ---
print("\n" + "=" * 50)
print("LANGKAH 7: PERBANDINGAN AKHIR")
print("=" * 50)

results = pd.DataFrame({
    'Model': ['Decision Tree', 'k-NN (k=5)'],
    'Test Accuracy': [
        accuracy_score(y_test, y_pred_dt),
        accuracy_score(y_test, y_pred_knn)
    ],
    'CV Mean Accuracy': [dt_cv.mean(), knn_cv.mean()],
    'CV Std': [dt_cv.std(), knn_cv.std()]
})
print(results.to_string(index=False))

# Confusion matrices side by side
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax, y_pred, title in zip(
    axes,
    [y_pred_dt, y_pred_knn],
    ['Decision Tree', 'k-NN (k=5)']
):
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(cm, display_labels=iris.target_names)
    disp.plot(ax=ax, cmap='Blues')
    ax.set_title(f'Confusion Matrix — {title}', fontsize=12)

plt.suptitle("Perbandingan Model Klasifikasi", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

## AI Corner: ML vs Traditional Statistics — Kapan Pakai yang Mana?

### Gunakan Statistik Tradisional Ketika:

- Kalian ingin **memahami hubungan** kausal antara variabel
- Ukuran sampel **kecil** (n < 100)
- Kalian perlu **interpretasi** yang jelas untuk stakeholder non-teknis
- Domain membutuhkan **p-value dan confidence interval** (riset akademik, uji klinis)
- Kalian ingin **menguji teori** atau hipotesis spesifik

### Gunakan Machine Learning Ketika:

- Tujuan utama adalah **prediksi** pada data baru
- Data **besar** dan berdimensi tinggi
- Hubungan antar variabel **non-linear** dan kompleks
- Interpretabilitas **bukan** prioritas utama
- Kalian memiliki **banyak fitur** dan tidak yakin mana yang penting

### Dalam Praktik: Keduanya Sering Digunakan Bersama

```
Alur kerja yang umum di industri:

1. Eksplorasi → Statistik deskriptif & visualisasi
2. Pemahaman → Inferensi statistik, uji hipotesis
3. Prediksi → Machine learning model
4. Evaluasi → Metrik ML + interpretasi statistik
5. Komunikasi → Storytelling dengan bahasa statistik
```

> **Prompt untuk dicoba dengan AI:**
> "Saya memiliki dataset tentang kepuasan pelanggan dengan 500 sampel dan 10 fitur. Tujuan saya adalah memahami faktor apa yang paling mempengaruhi kepuasan sekaligus memprediksi kepuasan pelanggan baru. Pendekatan apa yang kamu sarankan — statistik tradisional, machine learning, atau keduanya? Jelaskan alasannya."

---

## Latihan Mandiri

### Latihan 1: Konsep Dasar (10 menit)

Jawab pertanyaan berikut:

1. Sebutkan 3 perbedaan utama antara pendekatan statistik tradisional dan machine learning.
2. Jelaskan mengapa standardisasi fitur penting untuk k-NN tapi tidak untuk Decision Tree.
3. Jika Anda membangun model untuk mendeteksi penipuan transaksi bank (fraud detection), metrik mana yang lebih penting — precision atau recall? Mengapa?

### Latihan 2: Koding (30 menit)

Gunakan dataset `wine` dari sklearn:

```python
from sklearn.datasets import load_wine

wine = load_wine()
X_wine = wine.data
y_wine = wine.target
print(f"Fitur: {wine.feature_names}")
print(f"Kelas: {wine.target_names}")
print(f"Shape: {X_wine.shape}")
```

**Tugas:**
1. Lakukan train-test split (80-20) dengan `stratify=y`
2. Bangun model Decision Tree (coba `max_depth` = 2, 3, 5, None) dan bandingkan hasilnya
3. Bangun model k-NN (coba k = 3, 5, 7, 9) — jangan lupa standardisasi!
4. Buat classification report untuk model terbaik dari masing-masing algoritma
5. Mana yang lebih baik untuk dataset wine — Decision Tree atau k-NN? Jelaskan berdasarkan metrik.

### Latihan 3: Refleksi (10 menit)

1. Apa hubungan antara `max_depth` pada Decision Tree dengan overfitting/underfitting?
2. Mengapa cross-validation memberikan estimasi performa yang lebih reliable dibandingkan single train-test split?
3. Dalam proyek akhir kalian, apakah ada peluang untuk menggunakan teknik ML? Jika ya, jelaskan.

---

## Rangkuman Modul

| Konsep | Poin Penting |
|--------|-------------|
| **Statistik vs ML** | Tujuan berbeda (inferensi vs prediksi), fondasi sama |
| **Supervised Learning** | Belajar dari data berlabel, termasuk classification dan regression |
| **Decision Tree** | Membuat keputusan dengan pertanyaan berurutan, information gain memilih split terbaik |
| **k-NN** | Klasifikasi berdasarkan tetangga terdekat, perlu standardisasi, pilih k hati-hati |
| **Train-Test Split** | Pisahkan data agar evaluasi realistis, hindari overfitting |
| **Cross-Validation** | Evaluasi lebih robust dengan K-fold, rata-rata dari beberapa percobaan |
| **Evaluation Metrics** | Accuracy untuk keseluruhan, precision/recall untuk kasus spesifik, F1 untuk keseimbangan |

---

## Referensi

### Referensi Utama
1. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning with Applications in Python (ISLP)*. Springer. — Chapter 2 (Statistical Learning) & Chapter 4 (Classification).
2. Muller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*. O'Reilly Media. — Chapter 2 (Supervised Learning).

### Referensi Pendukung
3. scikit-learn Documentation — [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/tree.html)
4. scikit-learn Documentation — [KNeighborsClassifier](https://scikit-learn.org/stable/modules/neighbors.html)
5. scikit-learn Documentation — [Model Evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)

### Bacaan Lanjutan
6. Breiman, L. (2001). "Statistical Modeling: The Two Cultures." *Statistical Science*, 16(3), 199-231. — Artikel klasik tentang perbedaan paradigma statistik dan ML.

---

## Persiapan Minggu Depan

Minggu 14 akan membahas **AI-Augmented Data Analysis** — bagaimana menggunakan AI (seperti ChatGPT, Claude) sebagai co-analyst untuk analisis data. Persiapkan:

1. **Akses ke AI assistant** (Claude, ChatGPT, atau lainnya) — pastikan kalian sudah punya akun
2. **Review proyek akhir** kalian — kita akan berlatih menggunakan AI untuk membantu analisis
3. **Pikirkan:** Selama semester ini, kapan saja kalian sudah menggunakan AI? Pengalaman apa yang positif dan negatif?

---

*Modul ini merupakan bagian dari mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia. Semester Genap 2025/2026.*
