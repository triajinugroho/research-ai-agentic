# BAB 12: PENGANTAR MACHINE LEARNING STATISTIK

**Tri Aji Nugroho, S.T., M.T.**
Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-7.1 | Menjelaskan perbedaan paradigma antara statistik tradisional dan machine learning serta memahami kapan menggunakan masing-masing pendekatan | C2 |
| CPMK-7.2 | Membedakan supervised vs unsupervised learning, serta classification vs regression dalam konteks ML | C4 |
| CPMK-7.3 | Membangun dan mengevaluasi model Decision Tree dan k-Nearest Neighbors menggunakan scikit-learn | C5 |
| CPMK-7.4 | Menerapkan teknik train-test split dan cross-validation untuk evaluasi model yang robust | C5 |
| CPMK-7.5 | Merancang pipeline machine learning end-to-end untuk permasalahan klasifikasi dengan data konteks Indonesia | C5 |

---

## 12.1 Apa Itu Machine Learning?

### 12.1.1 Definisi dari Perspektif Statistik

**Machine Learning (ML)** adalah cabang kecerdasan buatan yang mempelajari cara komputer "belajar" dari data tanpa diprogram secara eksplisit. Dari perspektif statistik, ML adalah **perluasan pemodelan statistik** yang mengutamakan kemampuan prediksi pada data baru.

> "Machine learning is essentially statistics scaled up to large datasets and complex models."
> — Larry Wasserman, *All of Statistics*

Selama 11 bab sebelumnya, kalian telah membangun fondasi statistik yang kuat — mulai dari deskriptif, inferensi, regresi, ANOVA, hingga regresi logistik. Sekarang kita akan melihat bagaimana **fondasi yang sama** melahirkan pendekatan baru yang sangat powerful.

### 12.1.2 Statistik Tradisional vs Machine Learning

| Aspek | Statistik Tradisional | Machine Learning |
|-------|----------------------|------------------|
| **Tujuan utama** | Memahami hubungan antar variabel (*inference*) | Membuat prediksi seakurat mungkin (*prediction*) |
| **Pendekatan** | Model-driven: mulai dari asumsi distribusi | Data-driven: biarkan data "berbicara" |
| **Asumsi** | Banyak (normalitas, homoscedasticity, dll.) | Lebih sedikit, lebih fleksibel |
| **Interpretasi** | Sangat penting (p-value, koefisien) | Kadang dikorbankan demi akurasi (*black box*) |
| **Ukuran data** | Bisa bekerja dengan sampel kecil | Biasanya butuh data besar |
| **Overfitting** | Kurang dibahas eksplisit | *Concern* utama, ada mekanisme pencegahan |
| **Evaluasi** | R-squared, p-value, confidence interval | Accuracy, precision, recall, cross-validation |

### 12.1.3 Dimana Mereka Bertemu?

Penting dipahami bahwa ML **bukan** pengganti statistik. Keduanya saling melengkapi:

```
STATISTIKA KLASIK                    MACHINE LEARNING
──────────────────                   ─────────────────
Regresi Linear          ────→        Linear Regression
Regresi Logistik        ────→        Logistic Regression (Classification)
Analisis Diskriminan    ────→        LDA, QDA
Clustering Hierarki     ────→        K-Means, DBSCAN
Bayesian Inference      ────→        Naive Bayes, Bayesian Networks
Decision Trees          ────→        Random Forest, XGBoost
Kernel Methods          ────→        Support Vector Machines
Reduksi Dimensi         ────→        PCA, t-SNE
```

> **Analogi:** Statistik seperti seorang dokter yang ingin memahami *mengapa* pasien sakit (diagnosis). Machine learning seperti seorang dokter yang ingin memprediksi *siapa* yang akan sakit berikutnya (prediksi). Keduanya butuh pengetahuan kedokteran (fondasi statistik).

Mahasiswa yang menguasai statistika akan memahami **mengapa** model ML bekerja, bukan hanya **bagaimana** menjalankannya.

---

## 12.2 Supervised vs Unsupervised Learning

### 12.2.1 Taksonomi Machine Learning

```
                    MACHINE LEARNING
                         │
          ┌──────────────┼──────────────┐
          │              │              │
   SUPERVISED      UNSUPERVISED    REINFORCEMENT
   (Ada label)    (Tanpa label)   (Reward/penalty)
          │              │
    ┌─────┴─────┐   ┌────┴────┐
    │           │   │         │
CLASSIFICATION REGRESSION CLUSTERING DIMENSIONALITY
(Kategori)   (Numerik) (Kelompok)   REDUCTION
```

### 12.2.2 Supervised Learning

Dalam supervised learning, kita memiliki **data berlabel** — artinya kita tahu "jawaban yang benar" untuk setiap observasi. Algoritma belajar pola dari data berlabel ini, lalu memprediksi label untuk data baru.

**Contoh dalam konteks Indonesia:**
- Email diberi label "spam" atau "bukan spam" di Gmail/Yahoo
- Transaksi GoPay diberi label "fraud" atau "legitimate"
- Ulasan di Tokopedia diberi label "positif", "netral", atau "negatif"
- Data historis pelanggan Telkomsel diberi label "churn" atau "tidak churn"

### 12.2.3 Unsupervised Learning

Dalam unsupervised learning, **tidak ada label**. Algoritma mencari pola atau struktur tersembunyi dalam data.

**Contoh:**
- Mengelompokkan pelanggan Shopee berdasarkan perilaku belanja (*customer segmentation*)
- Menemukan topik tersembunyi dalam kumpulan berita Kompas.com (*topic modeling*)
- Reduksi dimensi untuk visualisasi data transaksi yang memiliki ratusan fitur

> **Catatan:** Dalam bab ini, kita fokus pada **supervised learning** — khususnya klasifikasi.

### 12.2.4 Classification vs Regression

| Aspek | Classification | Regression |
|-------|---------------|------------|
| **Output** | Kategori/label (diskret) | Nilai numerik (kontinu) |
| **Contoh Indonesia** | Spam/bukan spam, churn/tidak churn | Harga rumah di Jakarta, suhu besok |
| **Metrik evaluasi** | Accuracy, precision, recall, F1 | RMSE, MAE, R-squared |
| **Algoritma** | Decision Tree, k-NN, Logistic Regression | Linear Regression, Random Forest Regression |

Regresi linear yang kalian pelajari di bab sebelumnya adalah contoh **regression** dalam konteks ML. Regresi logistik — meskipun namanya "regresi" — digunakan untuk **classification**. Dalam bab ini, kita akan fokus pada **classification**.

---

## 12.3 Decision Tree: Konsep dan Implementasi

### 12.3.1 Apa Itu Decision Tree?

Decision tree adalah algoritma yang membuat keputusan dengan cara **memecah data berdasarkan pertanyaan-pertanyaan berurutan**, mirip seperti flowchart. Bayangkan kalian bermain game "20 Questions" — kalian bertanya ya/tidak berulang-ulang untuk menebak jawaban. Decision tree bekerja dengan cara yang sama.

```
              [Pengeluaran Bulanan > Rp 5 juta?]
              /                                \
            Ya                                Tidak
            /                                    \
 [Usia > 35 tahun?]                    [Frekuensi Login < 2x/bulan?]
    /           \                          /                  \
  Ya           Tidak                     Ya                  Tidak
  /               \                      /                      \
[Tidak Churn]  [Churn]            [Churn]              [Tidak Churn]
```

*Contoh di atas: decision tree untuk prediksi churn pelanggan telekomunikasi Indonesia.*

### 12.3.2 Information Gain dan Entropy

Bagaimana tree memutuskan pertanyaan mana yang ditanyakan pertama? Jawabannya: **Information Gain** — konsep dari teori informasi yang mengukur seberapa efektif suatu fitur dalam memisahkan kelas.

**Entropy** mengukur "ketidakpastian" dalam data:

$$Entropy(S) = -\sum_{i=1}^{c} p_i \cdot \log_2(p_i)$$

Di mana $p_i$ adalah proporsi data di kelas $i$, dan $c$ adalah jumlah kelas.

**Contoh perhitungan:**
- Jika 100% data adalah spam: Entropy = -1.0 * log2(1.0) = **0** (pasti, tidak ada ketidakpastian)
- Jika 50% spam, 50% bukan spam: Entropy = -0.5 * log2(0.5) - 0.5 * log2(0.5) = **1.0** (ketidakpastian maksimum)
- Jika 80% spam, 20% bukan spam: Entropy = -0.8 * log2(0.8) - 0.2 * log2(0.2) = **0.72**

**Information Gain** mengukur pengurangan entropy setelah data dipecah berdasarkan suatu fitur:

$$IG(S, A) = Entropy(S) - \sum_{v \in values(A)} \frac{|S_v|}{|S|} \cdot Entropy(S_v)$$

Tree memilih fitur dan threshold yang memberikan **information gain tertinggi** di setiap langkah.

```
ENTROPY: Mengukur Ketidakpastian
─────────────────────────────────
Entropy = 0.0   →  ████████████  Semua satu kelas (pasti)
Entropy = 0.72  →  ██████░░░░░░  Agak tercampur
Entropy = 1.0   →  ██████░░░░░░  Tercampur rata 50:50 (paling tidak pasti)

Information Gain = Entropy(sebelum split) - Entropy(setelah split)
                 → Semakin besar, semakin baik split-nya
```

### 12.3.3 Implementasi Decision Tree dengan Python

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

print("=== EKSPLORASI DATASET IRIS ===")
print(f"Fitur yang tersedia: {iris.feature_names}")
print(f"Jumlah sampel: {X.shape[0]}")
print(f"Jumlah kelas: {len(set(y))}")
print(f"Nama kelas: {list(iris.target_names)}")
print(f"\nStatistik deskriptif:")
print(X.describe().round(2))
```

```python
# Bangun model Decision Tree
dt_model = DecisionTreeClassifier(
    max_depth=3,          # Batasi kedalaman agar tidak terlalu kompleks
    random_state=42       # Reproducibility
)
dt_model.fit(X, y)

# Visualisasi tree
plt.figure(figsize=(16, 10))
plot_tree(
    dt_model,
    feature_names=iris.feature_names,
    class_names=list(iris.target_names),
    filled=True,          # Warnai node berdasarkan kelas mayoritas
    rounded=True,
    fontsize=10
)
plt.title("Decision Tree untuk Klasifikasi Iris", fontsize=14)
plt.tight_layout()
plt.show()
```

```python
# Feature Importance — fitur mana yang paling berpengaruh?
importance = pd.DataFrame({
    'Fitur': iris.feature_names,
    'Importance': dt_model.feature_importances_
}).sort_values('Importance', ascending=False)

print("=== FEATURE IMPORTANCE ===")
for _, row in importance.iterrows():
    bar = '█' * int(row['Importance'] * 40)
    print(f"  {row['Fitur']:25s}: {row['Importance']:.4f} {bar}")
```

**Kelebihan Decision Tree:**
- Mudah diinterpretasi (bisa divisualisasikan sebagai flowchart)
- Tidak butuh normalisasi data
- Bisa menangani fitur numerik dan kategorikal

**Kelemahan Decision Tree:**
- Cenderung overfitting jika tidak dibatasi (*pruning*)
- Sensitif terhadap perubahan kecil dalam data
- Batas keputusan selalu berbentuk garis tegak lurus (axis-aligned)

---

## 12.4 k-Nearest Neighbors (k-NN): Klasifikasi Berbasis Jarak

### 12.4.1 Konsep k-NN

k-NN adalah algoritma yang sangat intuitif: untuk mengklasifikasikan data baru, **lihat k tetangga terdekat** dan ambil "suara mayoritas" dari kelas mereka.

> **Analogi:** Jika kalian pindah ke lingkungan baru di Jakarta dan ingin tahu warung makan mana yang enak, kalian bertanya ke 5 tetangga terdekat. Jika 4 dari 5 bilang Warung A, kemungkinan besar Warung A memang enak. Itulah k-NN dengan k=5.

```
CARA KERJA k-NN (k=3)
──────────────────────

    ○ ○       △ △         ○ = Kelas A
      ○    ?    △         △ = Kelas B
         ○   △            ? = Data baru
       ○       △

Langkah 1: Hitung jarak dari ? ke semua data
Langkah 2: Pilih 3 tetangga terdekat
Langkah 3: Mayoritas tetangga = Kelas A (2 dari 3)
Langkah 4: Prediksi: ? → Kelas A
```

### 12.4.2 Memilih Nilai k

Pemilihan k sangat penting dan mempengaruhi perilaku model:

| k | Karakteristik |
|---|---------------|
| **k kecil** (misal k=1) | Sangat sensitif terhadap noise, batas keputusan tidak halus (overfitting) |
| **k besar** (misal k=50) | Terlalu "smooth", bisa kehilangan pola lokal (underfitting) |
| **Aturan praktis** | Mulai dengan k = sqrt(n), di mana n = jumlah data, lalu eksperimen |

**Tips:** Gunakan k ganjil untuk menghindari "seri" dalam voting (khususnya pada binary classification).

### 12.4.3 Distance Metrics

k-NN menggunakan **jarak** untuk menentukan "tetangga terdekat". Dua metrik jarak yang paling umum:

**Euclidean Distance** (default di scikit-learn):

$$d(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}$$

**Manhattan Distance** (lebih robust terhadap outlier):

$$d(x, y) = \sum_{i=1}^{n} |x_i - y_i|$$

> **Penting:** Karena k-NN bergantung pada jarak, **skala fitur sangat berpengaruh**. Fitur dengan range besar akan mendominasi perhitungan jarak. Contoh: jika satu fitur berupa "gaji" (jutaan) dan fitur lain berupa "usia" (puluhan), maka gaji akan mendominasi jarak. **Solusi: normalisasi/standardisasi data sebelum menggunakan k-NN.**

### 12.4.4 Implementasi k-NN dengan Python

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Standardisasi fitur (penting untuk k-NN!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("=== EFEK STANDARDISASI ===")
print("Sebelum standardisasi:")
for col in iris.feature_names:
    print(f"  {col}: mean={X[col].mean():.2f}, std={X[col].std():.2f}")
print("\nSetelah standardisasi (mean ≈ 0, std ≈ 1):")
for i, col in enumerate(iris.feature_names):
    print(f"  {col}: mean={X_scaled[:, i].mean():.2f}, std={X_scaled[:, i].std():.2f}")
```

```python
# Bangun model k-NN
knn_model = KNeighborsClassifier(
    n_neighbors=5,        # k = 5
    metric='euclidean'    # Default distance metric
)
knn_model.fit(X_scaled, y)

print(f"\nModel k-NN dengan k={knn_model.n_neighbors}")
print(f"Accuracy pada training data: {knn_model.score(X_scaled, y):.4f}")
```

---

## 12.5 Train-Test Split dan Cross-Validation

### 12.5.1 Masalah: Mengapa Tidak Boleh Evaluasi pada Data Training?

Jika kita melatih model pada **semua** data, lalu mengevaluasi pada data yang **sama**, hasilnya akan terlalu optimis. Ini seperti ujian di mana soalnya persis sama dengan latihan — nilai tinggi belum tentu berarti paham.

Model yang "menghafal" data training tapi gagal pada data baru disebut **overfitting**.

```
ANALOGI OVERFITTING
────────────────────

Mahasiswa A: Menghafal seluruh soal latihan tanpa memahami konsep
             → Nilai latihan: 100  |  Nilai UAS (soal baru): 40
             → OVERFITTING!

Mahasiswa B: Memahami konsep dan berlatih soal yang bervariasi
             → Nilai latihan: 85   |  Nilai UAS (soal baru): 80
             → GENERALISASI BAIK!
```

### 12.5.2 Solusi: Train-Test Split

Kita membagi data menjadi dua bagian:
- **Training set** (biasanya 70-80%): digunakan untuk melatih model
- **Test set** (biasanya 20-30%): disimpan dan **hanya** digunakan untuk evaluasi akhir

```python
from sklearn.model_selection import train_test_split

# Split data: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,        # 20% untuk testing
    random_state=42,      # Reproducibility
    stratify=y            # Pastikan proporsi kelas sama di train dan test
)

print(f"=== PEMBAGIAN DATA ===")
print(f"Total data    : {len(X)}")
print(f"Data training : {X_train.shape[0]} ({X_train.shape[0]/len(X)*100:.0f}%)")
print(f"Data testing  : {X_test.shape[0]} ({X_test.shape[0]/len(X)*100:.0f}%)")
print(f"\nProporsi kelas di training set:")
print(pd.Series(y_train).value_counts(normalize=True).sort_index())
print(f"\nProporsi kelas di test set:")
print(pd.Series(y_test).value_counts(normalize=True).sort_index())
```

> **Parameter `stratify=y`** memastikan bahwa proporsi kelas di training dan test set sama dengan proporsi di data asli. Sangat penting untuk dataset yang tidak seimbang (*imbalanced*).

### 12.5.3 Cross-Validation: Evaluasi Lebih Robust

Train-test split hanya memberikan **satu estimasi** performa. Bagaimana jika split tersebut "kebetulan" bagus atau buruk? **K-Fold Cross-Validation** mengatasi masalah ini:

```
5-FOLD CROSS-VALIDATION
─────────────────────────

Fold 1: [TEST ] [Train] [Train] [Train] [Train]  → Score 1
Fold 2: [Train] [TEST ] [Train] [Train] [Train]  → Score 2
Fold 3: [Train] [Train] [TEST ] [Train] [Train]  → Score 3
Fold 4: [Train] [Train] [Train] [TEST ] [Train]  → Score 4
Fold 5: [Train] [Train] [Train] [Train] [TEST ]  → Score 5

Final Score = Mean(Score 1, 2, 3, 4, 5) ± Std
```

Setiap data menjadi test set tepat **satu kali**, sehingga evaluasi lebih adil dan stabil.

```python
from sklearn.model_selection import cross_val_score

# 5-Fold Cross-Validation untuk Decision Tree
dt_scores = cross_val_score(
    DecisionTreeClassifier(max_depth=3, random_state=42),
    X, y,
    cv=5,                 # 5-fold
    scoring='accuracy'
)

print("=== 5-FOLD CROSS-VALIDATION ===")
print(f"Decision Tree:")
print(f"  Scores per fold : {dt_scores.round(4)}")
print(f"  Mean Accuracy   : {dt_scores.mean():.4f}")
print(f"  Std Deviation   : {dt_scores.std():.4f}")
```

---

## 12.6 Evaluation Metrics: Mengukur Performa Klasifikasi

### 12.6.1 Confusion Matrix

Confusion matrix adalah tabel yang menunjukkan jumlah prediksi benar dan salah per kelas:

```
CONFUSION MATRIX (Binary Classification)
──────────────────────────────────────────

                      Prediksi Model
                   Positive    Negative
                ┌────────────┬────────────┐
Actual Positive │     TP     │     FN     │
                │ (Benar!)   │ (Lolos!)   │
                ├────────────┼────────────┤
Actual Negative │     FP     │     TN     │
                │ (Salah!)   │ (Benar!)   │
                └────────────┴────────────┘

TP = True Positive   → Benar diprediksi positif
TN = True Negative   → Benar diprediksi negatif
FP = False Positive  → Salah diprediksi positif  (Type I Error)
FN = False Negative  → Salah diprediksi negatif  (Type II Error)
```

### 12.6.2 Metrik Turunan dari Confusion Matrix

| Metrik | Formula | Arti | Kapan Penting |
|--------|---------|------|---------------|
| **Accuracy** | (TP + TN) / Total | Seberapa sering model benar secara keseluruhan | Data seimbang |
| **Precision** | TP / (TP + FP) | Dari yang diprediksi positif, berapa yang benar? | Ketika FP mahal (spam filter) |
| **Recall** | TP / (TP + FN) | Dari yang sebenarnya positif, berapa yang terdeteksi? | Ketika FN mahal (deteksi penyakit) |
| **F1-Score** | 2 * (P * R) / (P + R) | Harmonic mean precision dan recall | Keseimbangan P dan R |

**Contoh nyata di Indonesia:**
- **Deteksi fraud transaksi OVO:** Recall lebih penting — kita tidak ingin melewatkan transaksi penipuan (FN berbahaya bagi pengguna)
- **Filter spam email kampus:** Precision lebih penting — kita tidak ingin email penting dari dosen masuk ke folder spam (FP mengganggu aktivitas akademik)
- **Klasifikasi berita hoaks:** F1-score penting — keseimbangan antara tidak meloloskan hoaks (recall) dan tidak salah memblokir berita benar (precision)

### 12.6.3 Implementasi Evaluasi Lengkap

```python
from sklearn.metrics import (
    confusion_matrix, classification_report,
    accuracy_score, ConfusionMatrixDisplay
)

# Standardisasi untuk k-NN
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --- Model 1: Decision Tree ---
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

print("=== DECISION TREE — EVALUASI ===")
print(f"Akurasi: {accuracy_score(y_test, y_pred_dt):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_dt, target_names=iris.target_names))

# Confusion Matrix
cm_dt = confusion_matrix(y_test, y_pred_dt)
fig, ax = plt.subplots(figsize=(8, 6))
disp = ConfusionMatrixDisplay(confusion_matrix=cm_dt, display_labels=iris.target_names)
disp.plot(ax=ax, cmap='Blues')
plt.title("Confusion Matrix — Decision Tree", fontsize=14)
plt.tight_layout()
plt.show()
```

```python
# --- Model 2: k-NN ---
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
y_pred_knn = knn.predict(X_test_scaled)

print("=== k-NN (k=5) — EVALUASI ===")
print(f"Akurasi: {accuracy_score(y_test, y_pred_knn):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_knn, target_names=iris.target_names))
```

---

## 12.7 Overfitting vs Underfitting: Bias-Variance Tradeoff

### 12.7.1 Konsep

Salah satu masalah paling fundamental dalam machine learning adalah menemukan keseimbangan antara model yang terlalu sederhana dan terlalu kompleks.

| Kondisi | Definisi | Ciri-ciri |
|---------|----------|-----------|
| **Underfitting** | Model terlalu sederhana, tidak mampu menangkap pola dalam data | Akurasi rendah di training DAN test |
| **Good fit** | Model menangkap pola umum tanpa menghafal detail noise | Akurasi tinggi di training DAN test |
| **Overfitting** | Model terlalu kompleks, "menghafal" data training termasuk noise-nya | Akurasi tinggi di training, RENDAH di test |

### 12.7.2 Bias-Variance Tradeoff

```
BIAS-VARIANCE TRADEOFF
────────────────────────

Error
  ^
  │  \                    /
  │   \    Total Error   /
  │    \      ___       /
  │     \    /   \     /
  │      \  /     \   /
  │       \/       \_/_____ Bias (underfitting)
  │       /\
  │      /  \______________ Variance (overfitting)
  │     /
  │    /
  └──────────────────────→ Kompleksitas Model
       Sederhana      Kompleks

  ← Underfitting →|← Sweet Spot →|← Overfitting →
```

- **Bias** (kesalahan sistematis): Model terlalu sederhana sehingga tidak mampu menangkap pola. High bias = underfitting.
- **Variance** (ketidakstabilan): Model terlalu sensitif terhadap data training tertentu. High variance = overfitting.
- **Sweet spot**: Keseimbangan optimal antara bias dan variance.

### 12.7.3 Demonstrasi: Efek max_depth pada Decision Tree

```python
# Eksperimen: bagaimana max_depth mempengaruhi overfitting?
train_scores = []
test_scores = []
depths = range(1, 16)

for depth in depths:
    dt_temp = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt_temp.fit(X_train, y_train)
    train_scores.append(dt_temp.score(X_train, y_train))
    test_scores.append(dt_temp.score(X_test, y_test))

plt.figure(figsize=(10, 6))
plt.plot(depths, train_scores, 'b-o', label='Training Accuracy', linewidth=2)
plt.plot(depths, test_scores, 'r-s', label='Test Accuracy', linewidth=2)
plt.xlabel('max_depth', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
plt.title('Efek max_depth terhadap Overfitting (Decision Tree)', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

# Anotasi
plt.axvline(x=3, color='green', linestyle='--', alpha=0.5, label='Sweet spot (max_depth=3)')
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()

print("Interpretasi:")
print("- Training accuracy terus naik seiring max_depth bertambah")
print("- Test accuracy naik lalu TURUN → tanda overfitting")
print("- Sweet spot: max_depth sekitar 3-4 untuk dataset ini")
```

### 12.7.4 Strategi Mengatasi Overfitting

| Strategi | Decision Tree | k-NN |
|----------|--------------|------|
| **Regularisasi** | Batasi `max_depth`, `min_samples_split`, `min_samples_leaf` | Pilih k lebih besar |
| **Lebih banyak data** | Berlaku untuk keduanya | Berlaku untuk keduanya |
| **Feature selection** | Gunakan fitur yang paling relevan | Kurangi dimensi data |
| **Cross-validation** | Evaluasi lebih robust | Evaluasi lebih robust |

---

## 12.8 Pipeline ML Sederhana End-to-End

### 12.8.1 Alur Kerja Machine Learning

```
┌─────────────┐    ┌──────────────────┐    ┌──────────────┐
│  1. Data     │───→│  2. Preprocessing │───→│  3. Split    │
│  Collection  │    │  (cleaning,       │    │  Train/Test  │
│              │    │   encoding,       │    │              │
│              │    │   scaling)        │    │              │
└─────────────┘    └──────────────────┘    └──────┬───────┘
                                                   │
                    ┌──────────────┐    ┌───────────▼──────┐
                    │  5. Evaluate │←───│  4. Train        │
                    │  (metrics,   │    │  Model           │
                    │   CV)        │    │                  │
                    └──────┬───────┘    └──────────────────┘
                           │
                    ┌──────▼───────┐
                    │  6. Predict  │
                    │  (new data)  │
                    └──────────────┘
```

### 12.8.2 Implementasi Pipeline Lengkap dengan sklearn

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# Pipeline untuk k-NN (otomatis standardisasi + model)
knn_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=5))
])

# Cross-validation dengan pipeline
cv_knn = cross_val_score(knn_pipeline, X, y, cv=5, scoring='accuracy')
print(f"k-NN Pipeline — 5-Fold CV: {cv_knn.mean():.4f} (+/- {cv_knn.std():.4f})")

# Perbandingan dengan Decision Tree
cv_dt = cross_val_score(
    DecisionTreeClassifier(max_depth=3, random_state=42),
    X, y, cv=5, scoring='accuracy'
)
print(f"Decision Tree — 5-Fold CV: {cv_dt.mean():.4f} (+/- {cv_dt.std():.4f})")
```

---

## 12.9 Studi Kasus: Klasifikasi dengan Konteks Indonesia

### 12.9.1 Studi Kasus 1: Klasifikasi Spam SMS Bahasa Indonesia

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

# Simulasi dataset SMS spam Indonesia
# (Dalam proyek nyata, gunakan dataset publik seperti SMS Spam Collection)
np.random.seed(42)
n = 200

# Fitur yang diekstrak dari SMS
data_sms = pd.DataFrame({
    'panjang_pesan': np.concatenate([
        np.random.normal(120, 30, 100),    # Spam cenderung lebih panjang
        np.random.normal(45, 20, 100)      # Bukan spam lebih pendek
    ]),
    'jumlah_angka': np.concatenate([
        np.random.poisson(8, 100),         # Spam banyak angka (nomor HP, harga)
        np.random.poisson(1, 100)          # Bukan spam sedikit angka
    ]),
    'jumlah_huruf_besar': np.concatenate([
        np.random.poisson(12, 100),        # Spam banyak kapital (GRATIS, MENANG)
        np.random.poisson(2, 100)          # Bukan spam sedikit kapital
    ]),
    'ada_kata_promo': np.concatenate([
        np.random.binomial(1, 0.85, 100),  # 85% spam ada kata promo
        np.random.binomial(1, 0.05, 100)   # 5% bukan spam ada kata promo
    ]),
    'ada_url': np.concatenate([
        np.random.binomial(1, 0.70, 100),  # 70% spam ada URL
        np.random.binomial(1, 0.15, 100)   # 15% bukan spam ada URL
    ]),
    'label': ['spam'] * 100 + ['bukan_spam'] * 100
})

print("=== DATASET SMS SPAM INDONESIA ===")
print(f"Jumlah data: {len(data_sms)}")
print(f"\nDistribusi label:")
print(data_sms['label'].value_counts())
print(f"\nStatistik per kelas:")
print(data_sms.groupby('label').mean().round(2))
```

```python
# Persiapan data
X_sms = data_sms.drop('label', axis=1)
y_sms = (data_sms['label'] == 'spam').astype(int)  # 1 = spam, 0 = bukan spam

X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_sms, y_sms, test_size=0.2, random_state=42, stratify=y_sms
)

# Model 1: Decision Tree
dt_spam = DecisionTreeClassifier(max_depth=4, random_state=42)
dt_spam.fit(X_train_s, y_train_s)
y_pred_spam_dt = dt_spam.predict(X_test_s)

print("=== DECISION TREE — KLASIFIKASI SPAM ===")
print(classification_report(y_test_s, y_pred_spam_dt,
                            target_names=['Bukan Spam', 'Spam']))

# Model 2: k-NN
scaler_sms = StandardScaler()
X_train_s_scaled = scaler_sms.fit_transform(X_train_s)
X_test_s_scaled = scaler_sms.transform(X_test_s)

knn_spam = KNeighborsClassifier(n_neighbors=5)
knn_spam.fit(X_train_s_scaled, y_train_s)
y_pred_spam_knn = knn_spam.predict(X_test_s_scaled)

print("=== k-NN — KLASIFIKASI SPAM ===")
print(classification_report(y_test_s, y_pred_spam_knn,
                            target_names=['Bukan Spam', 'Spam']))
```

### 12.9.2 Studi Kasus 2: Prediksi Churn Pelanggan Telekomunikasi

```python
# Simulasi data churn pelanggan provider Indonesia
np.random.seed(123)
n_cust = 300

data_churn = pd.DataFrame({
    'durasi_langganan_bulan': np.concatenate([
        np.random.normal(8, 4, 120),        # Churn: langganan lebih pendek
        np.random.normal(24, 10, 180)        # Tidak churn: lebih lama
    ]).clip(1, 60),
    'pengeluaran_bulanan_ribu': np.concatenate([
        np.random.normal(45, 15, 120),       # Churn: pengeluaran lebih rendah
        np.random.normal(85, 25, 180)        # Tidak churn: pengeluaran lebih tinggi
    ]).clip(10, 200),
    'jumlah_keluhan': np.concatenate([
        np.random.poisson(4, 120),           # Churn: lebih banyak keluhan
        np.random.poisson(1, 180)            # Tidak churn: sedikit keluhan
    ]),
    'frekuensi_login_app': np.concatenate([
        np.random.poisson(2, 120),           # Churn: jarang login
        np.random.poisson(8, 180)            # Tidak churn: sering login
    ]),
    'punya_paket_bundling': np.concatenate([
        np.random.binomial(1, 0.20, 120),    # Churn: jarang paket bundling
        np.random.binomial(1, 0.65, 180)     # Tidak churn: sering bundling
    ]),
    'churn': [1] * 120 + [0] * 180
})

print("=== DATASET CHURN PELANGGAN ===")
print(f"Jumlah data: {len(data_churn)}")
print(f"\nDistribusi churn:")
print(data_churn['churn'].value_counts().rename({1: 'Churn', 0: 'Tidak Churn'}))
print(f"\nRata-rata fitur per kelompok:")
print(data_churn.groupby('churn').mean().round(2))
```

```python
# Pipeline end-to-end
X_churn = data_churn.drop('churn', axis=1)
y_churn = data_churn['churn']

X_tr, X_te, y_tr, y_te = train_test_split(
    X_churn, y_churn, test_size=0.2, random_state=42, stratify=y_churn
)

# Standardisasi
sc = StandardScaler()
X_tr_sc = sc.fit_transform(X_tr)
X_te_sc = sc.transform(X_te)

# Eksperimen beberapa model
models = {
    'Decision Tree (depth=3)': DecisionTreeClassifier(max_depth=3, random_state=42),
    'Decision Tree (depth=5)': DecisionTreeClassifier(max_depth=5, random_state=42),
    'k-NN (k=3)': KNeighborsClassifier(n_neighbors=3),
    'k-NN (k=5)': KNeighborsClassifier(n_neighbors=5),
    'k-NN (k=7)': KNeighborsClassifier(n_neighbors=7),
}

print("=== PERBANDINGAN MODEL — PREDIKSI CHURN ===")
print(f"{'Model':<30} {'Accuracy':>10} {'Precision':>10} {'Recall':>10} {'F1':>10}")
print("-" * 72)

from sklearn.metrics import precision_score, recall_score, f1_score

for name, model in models.items():
    if 'k-NN' in name:
        model.fit(X_tr_sc, y_tr)
        preds = model.predict(X_te_sc)
    else:
        model.fit(X_tr, y_tr)
        preds = model.predict(X_te)

    acc = accuracy_score(y_te, preds)
    prec = precision_score(y_te, preds)
    rec = recall_score(y_te, preds)
    f1 = f1_score(y_te, preds)
    print(f"{name:<30} {acc:>10.4f} {prec:>10.4f} {rec:>10.4f} {f1:>10.4f}")
```

```python
# Confusion matrix model terbaik
best_model = DecisionTreeClassifier(max_depth=5, random_state=42)
best_model.fit(X_tr, y_tr)
y_pred_churn = best_model.predict(X_te)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Confusion matrix
cm_churn = confusion_matrix(y_te, y_pred_churn)
disp_churn = ConfusionMatrixDisplay(cm_churn, display_labels=['Tidak Churn', 'Churn'])
disp_churn.plot(ax=axes[0], cmap='Oranges')
axes[0].set_title('Confusion Matrix — Prediksi Churn', fontsize=12)

# Feature importance
importance_churn = pd.DataFrame({
    'Fitur': X_churn.columns,
    'Importance': best_model.feature_importances_
}).sort_values('Importance', ascending=True)

axes[1].barh(importance_churn['Fitur'], importance_churn['Importance'], color='coral')
axes[1].set_xlabel('Feature Importance')
axes[1].set_title('Fitur Paling Berpengaruh terhadap Churn', fontsize=12)

plt.tight_layout()
plt.show()

print("\nInterpretasi bisnis:")
print("- Fitur dengan importance tertinggi = faktor utama penyebab churn")
print("- Insight ini dapat digunakan untuk merancang program retensi pelanggan")
```

---

## 12.10 Eksperimen Pemilihan Nilai k pada k-NN

Memilih hyperparameter yang tepat adalah bagian penting dari proses ML. Berikut demonstrasi bagaimana memilih k optimal:

```python
# Eksperimen nilai k pada dataset Iris
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline

k_values = range(1, 21)
cv_means = []
cv_stds = []

for k in k_values:
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('knn', KNeighborsClassifier(n_neighbors=k))
    ])
    scores = cross_val_score(pipeline, X, y, cv=5, scoring='accuracy')
    cv_means.append(scores.mean())
    cv_stds.append(scores.std())

# Visualisasi
plt.figure(figsize=(10, 6))
plt.errorbar(k_values, cv_means, yerr=cv_stds, fmt='bo-',
             linewidth=2, markersize=8, capsize=4)
plt.xlabel('Nilai k (jumlah tetangga)', fontsize=12)
plt.ylabel('Cross-Validation Accuracy', fontsize=12)
plt.title('Pengaruh Nilai k terhadap Akurasi k-NN (5-Fold CV)', fontsize=14)
plt.xticks(k_values)
plt.grid(True, alpha=0.3)

best_k = list(k_values)[np.argmax(cv_means)]
plt.axvline(x=best_k, color='red', linestyle='--', alpha=0.7,
            label=f'k terbaik = {best_k}, Accuracy = {max(cv_means):.4f}')
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()

print(f"Nilai k terbaik: {best_k}")
print(f"Accuracy terbaik: {max(cv_means):.4f}")
```

---

## AI Corner: AI sebagai Asisten dalam Workflow Machine Learning

### Bagaimana AI Tools Membantu Workflow ML

Di era 2025-2026, AI tools seperti ChatGPT, Claude, dan GitHub Copilot dapat mempercepat berbagai tahap workflow ML. Namun, pemahaman statistik tetap menjadi tanggung jawab manusia.

| Tahap ML | Bantuan AI | Tetap Tanggung Jawab Manusia |
|----------|-----------|------------------------------|
| **Data Understanding** | Generate kode EDA otomatis | Interpretasi pola dan konteks domain |
| **Preprocessing** | Sarankan teknik encoding/scaling | Memilih strategi yang tepat untuk masalah |
| **Model Selection** | Sarankan algoritma yang sesuai | Memahami asumsi dan batasan setiap model |
| **Hyperparameter Tuning** | Generate kode grid search | Interpretasi kenapa parameter tertentu lebih baik |
| **Evaluation** | Hitung metrik otomatis | Memilih metrik yang tepat (precision vs recall?) |
| **Interpretation** | Jelaskan confusion matrix secara teknis | Membuat keputusan bisnis berdasarkan hasil |

### Contoh Prompt yang Efektif untuk ML

**Prompt yang baik:**
```
Saya memiliki dataset 500 pelanggan telekomunikasi Indonesia dengan fitur:
durasi_langganan, pengeluaran_bulanan, jumlah_keluhan, frekuensi_login.
Target: prediksi churn (binary classification).
Dataset imbalanced: 70% tidak churn, 30% churn.

1. Algoritma klasifikasi apa yang cocok untuk kasus ini?
2. Metrik evaluasi mana yang paling tepat, mengapa?
3. Bagaimana menangani class imbalance?
Berikan kode Python dengan sklearn.
```

**Prompt yang kurang baik:**
```
Buatkan model machine learning untuk data saya
```

### Prinsip Penting

**Selalu verifikasi output AI:**
- Jalankan kode yang diberikan AI dan cek hasilnya
- Pastikan metrik evaluasi yang digunakan sesuai dengan masalah
- Jangan langsung percaya interpretasi AI tanpa memahami sendiri
- Dokumentasikan penggunaan AI dalam AI Usage Log

> **Ingat:** AI mempercepat proses, tetapi **pemahaman konseptual** tentang bias-variance, overfitting, dan pemilihan metrik tetap harus dikuasai oleh praktisi data. Seorang data scientist yang hanya mengandalkan AI tanpa pemahaman statistik ibarat pengemudi yang tidak tahu cara kerja mesin — bisa jalan, tapi tidak tahu apa yang salah ketika mogok.

---

## Rangkuman Bab 12

1. **Machine Learning** adalah perluasan pemodelan statistik yang mengutamakan kemampuan prediksi. ML dan statistik tradisional saling melengkapi, bukan saling menggantikan.

2. **Supervised learning** menggunakan data berlabel (classification untuk output kategorikal, regression untuk output numerik), sedangkan **unsupervised learning** mencari pola tanpa label.

3. **Decision Tree** bekerja dengan memecah data melalui pertanyaan berurutan berdasarkan **information gain** (pengurangan entropy). Mudah diinterpretasi tetapi rentan overfitting.

4. **k-Nearest Neighbors (k-NN)** mengklasifikasikan data berdasarkan "suara mayoritas" dari k tetangga terdekat. Membutuhkan **standardisasi fitur** karena berbasis jarak.

5. **Train-test split** memisahkan data untuk pelatihan dan evaluasi agar terhindar dari overfitting. **Cross-validation** memberikan estimasi performa yang lebih robust dengan merotasi data test.

6. **Evaluation metrics** — accuracy, precision, recall, F1-score — memiliki kegunaan berbeda tergantung konteks masalah. **Confusion matrix** adalah fondasi untuk memahami semua metrik ini.

7. **Bias-variance tradeoff** adalah prinsip fundamental: model terlalu sederhana (high bias/underfitting) vs model terlalu kompleks (high variance/overfitting). Tujuannya menemukan *sweet spot* di antaranya.

8. **Pipeline ML end-to-end** — dari pengumpulan data, preprocessing, split, pelatihan, evaluasi, hingga prediksi — merupakan keterampilan esensial bagi praktisi data di era digital Indonesia.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan utama antara tujuan statistik tradisional dan machine learning. Berikan masing-masing satu contoh dalam konteks bisnis digital Indonesia.

**Soal 2.** Klasifikasikan masalah-masalah berikut sebagai supervised/unsupervised DAN classification/regression (jika supervised):
- a) Memprediksi apakah nasabah bank BCA akan gagal bayar kredit
- b) Mengelompokkan pelanggan Tokopedia berdasarkan pola belanja
- c) Memprediksi harga properti di kawasan BSD Tangerang
- d) Mendeteksi email spam di layanan Biznet
- e) Menemukan topik-topik utama dari kumpulan ulasan di Google Play Store

**Soal 3.** Jelaskan dengan kata-kata sendiri apa yang dimaksud dengan entropy dalam konteks decision tree. Mengapa entropy = 0 menunjukkan kondisi "pasti"?

**Soal 4.** Mengapa standardisasi fitur penting untuk k-NN tetapi **tidak** diperlukan untuk Decision Tree? Jelaskan dengan analogi yang mudah dipahami.

**Soal 5.** Perhatikan confusion matrix berikut untuk model deteksi fraud transaksi:

```
                Prediksi
              Fraud   Legit
Actual Fraud [  80  |  20  ]
       Legit [  15  | 885  ]
```

Hitung: (a) Accuracy, (b) Precision, (c) Recall, (d) F1-Score untuk kelas "Fraud". Interpretasikan setiap metrik dalam konteks bisnis.

### Tingkat Menengah (C2-C3)

**Soal 6.** Seorang data scientist di Gojek membangun model untuk memprediksi apakah seorang penumpang akan memberikan rating 4-5 (puas) atau 1-3 (tidak puas). Model menghasilkan:
- Training accuracy: 98%
- Test accuracy: 65%

Apa yang terjadi? Jelaskan fenomena ini dan sebutkan 3 strategi untuk mengatasinya.

**Soal 7.** Tulis kode Python lengkap untuk:
- a) Memuat dataset `load_wine` dari sklearn
- b) Melakukan train-test split (80:20) dengan stratify
- c) Membangun model Decision Tree dengan `max_depth=3`
- d) Menampilkan classification report dan confusion matrix
- e) Melakukan 5-fold cross-validation dan menampilkan hasilnya

**Soal 8.** Jelaskan perbedaan antara Euclidean distance dan Manhattan distance. Dalam situasi apa Manhattan distance lebih disarankan daripada Euclidean? Berikan contoh numerik sederhana dengan 2 dimensi.

**Soal 9.** Perhatikan skenario berikut:
- Dataset A: 10.000 email, 50% spam dan 50% bukan spam
- Dataset B: 10.000 transaksi bank, 99% legitimate dan 1% fraud

Untuk masing-masing dataset:
- a) Apakah accuracy merupakan metrik yang tepat? Mengapa?
- b) Metrik apa yang lebih informatif?
- c) Apa yang dimaksud dengan class imbalance dan bagaimana pengaruhnya?

### Tingkat Mahir (C3-C5)

**Soal 10.** Desain dan implementasikan pipeline ML end-to-end untuk dataset `load_breast_cancer` dari sklearn:
- a) Lakukan EDA (distribusi fitur, korelasi)
- b) Split data dengan stratify
- c) Bandingkan Decision Tree (variasikan `max_depth`: 2, 3, 5, 10, None) dan k-NN (variasikan k: 3, 5, 7, 9, 11) menggunakan 5-fold CV
- d) Pilih model terbaik dan jelaskan alasannya
- e) Untuk konteks medis (deteksi kanker), metrik mana yang paling penting? Mengapa?

**Soal 11.** Sebuah perusahaan e-commerce Indonesia ingin membangun model prediksi churn pelanggan. Data yang tersedia:

| Fitur | Tipe | Deskripsi |
|-------|------|-----------|
| durasi_langganan | Numerik | Bulan sejak mendaftar |
| total_transaksi | Numerik | Total transaksi 6 bulan terakhir |
| rata_rata_belanja | Numerik | Rata-rata nilai belanja (Rp) |
| jumlah_keluhan | Numerik | Keluhan dalam 3 bulan terakhir |
| platform | Kategorikal | iOS / Android / Web |
| kota | Kategorikal | Jakarta / Surabaya / Bandung / Lainnya |
| churn | Binary | 1 = churn, 0 = tidak churn |

- a) Bagaimana Anda menangani fitur kategorikal agar bisa digunakan oleh Decision Tree dan k-NN?
- b) Tulis pseudocode (atau kode Python) untuk pipeline ML lengkap
- c) Metrik evaluasi apa yang paling penting untuk kasus churn? Jelaskan alasannya
- d) Bagaimana Anda akan mengkomunikasikan hasil model kepada tim bisnis yang non-teknis?

**Soal 12.** Analisis kritis:
- a) Jelaskan mengapa cross-validation memberikan estimasi performa yang lebih reliable dibandingkan single train-test split. Gunakan contoh numerik.
- b) Apa kelemahan dari 5-fold cross-validation? Kapan kita mungkin memilih 10-fold atau leave-one-out cross-validation?
- c) Seorang kolega melaporkan bahwa model Decision Tree-nya mendapat akurasi CV 99.5% pada dataset imbalanced (95% kelas mayoritas). Apakah model ini benar-benar bagus? Jelaskan dan berikan saran perbaikan.

**Soal 13.** Bandingkan Decision Tree dan k-NN secara komprehensif:
- a) Buatlah tabel perbandingan mencakup: kecepatan training, kecepatan prediksi, interpretabilitas, kebutuhan preprocessing, sensitivitas terhadap outlier, dan penanganan missing values
- b) Untuk setiap skenario berikut, rekomendasi algoritma mana yang lebih cocok dan mengapa:
  - Klasifikasi gambar hasil scan medis (ribuan fitur)
  - Klasifikasi kelayakan kredit dengan 5 fitur (harus bisa menjelaskan ke nasabah mengapa ditolak)
  - Dataset kecil (50 sampel) dengan fitur yang sudah terstandarisasi

**Soal 14.** Implementasikan eksperimen berikut dalam Google Colab:
- a) Buat dataset sintetik menggunakan `sklearn.datasets.make_classification` dengan 1000 sampel, 10 fitur, dan 2 kelas
- b) Tambahkan 5 fitur noise (random) ke dataset — total 15 fitur
- c) Bandingkan akurasi Decision Tree dan k-NN dengan dan tanpa fitur noise
- d) Apa kesimpulan Anda tentang pengaruh fitur yang tidak relevan terhadap masing-masing algoritma?

**Soal 15.** Refleksi dan evaluasi:
- a) Selama bab ini, di bagian mana konsep statistik dari bab-bab sebelumnya (deskriptif, inferensi, regresi) muncul kembali? Sebutkan minimal 4 kaitan.
- b) Jika Anda diminta membangun model ML untuk proyek nyata di Indonesia (pilih salah satu: prediksi banjir Jakarta, deteksi berita hoaks, rekomendasi UMKM), jelaskan pipeline lengkap yang akan Anda gunakan — dari pengumpulan data hingga evaluasi.
- c) Tuliskan 3 pertanyaan yang masih ingin Anda pelajari lebih lanjut tentang machine learning setelah menyelesaikan bab ini.

---

## Referensi

### Referensi Utama

1. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning with Applications in Python (ISLP)*. Springer. — Chapter 2 (Statistical Learning) & Chapter 4 (Classification).
2. Muller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*. O'Reilly Media. — Chapter 2 (Supervised Learning).
3. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.

### Referensi Pendukung

4. scikit-learn Documentation — [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/tree.html).
5. scikit-learn Documentation — [KNeighborsClassifier](https://scikit-learn.org/stable/modules/neighbors.html).
6. scikit-learn Documentation — [Model Evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html).
7. Breiman, L. (2001). "Statistical Modeling: The Two Cultures." *Statistical Science*, 16(3), 199-231.

### Bacaan Lanjutan

8. Provost, F., & Fawcett, T. (2013). *Data Science for Business*. O'Reilly Media. — Chapter 7-8 (Classification, Evaluation).
9. Raschka, S., & Mirjalili, V. (2022). *Python Machine Learning* (4th ed.). Packt Publishing.

---

*Bab berikutnya: **Bab 13 — AI-Augmented Data Analysis dan Proyek Akhir***
