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

ML **bukan** pengganti statistik. Keduanya saling melengkapi:

```
STATISTIKA KLASIK                    MACHINE LEARNING
──────────────────                   ─────────────────
Regresi Linear          ────→        Linear Regression
Regresi Logistik        ────→        Logistic Regression (Classification)
Analisis Diskriminan    ────→        LDA, QDA
Clustering Hierarki     ────→        K-Means, DBSCAN
Bayesian Inference      ────→        Naive Bayes, Bayesian Networks
Decision Trees          ────→        Random Forest, XGBoost
```

> **Analogi:** Statistik seperti seorang dokter yang ingin memahami *mengapa* pasien sakit (diagnosis). Machine learning seperti seorang dokter yang ingin memprediksi *siapa* yang akan sakit berikutnya (prediksi). Keduanya butuh pengetahuan kedokteran (fondasi statistik).

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

Dalam supervised learning, kita memiliki **data berlabel** — artinya kita tahu "jawaban yang benar" untuk setiap observasi.

**Contoh dalam konteks Indonesia:**
- Email diberi label "spam" atau "bukan spam"
- Transaksi GoPay diberi label "fraud" atau "legitimate"
- Data pelanggan Telkomsel diberi label "churn" atau "tidak churn"

### 12.2.3 Unsupervised Learning

Dalam unsupervised learning, **tidak ada label**. Algoritma mencari pola tersembunyi dalam data.

**Contoh:** Mengelompokkan pelanggan Shopee berdasarkan perilaku belanja (*customer segmentation*), menemukan topik tersembunyi dalam kumpulan berita Kompas.com (*topic modeling*).

### 12.2.4 Classification vs Regression

| Aspek | Classification | Regression |
|-------|---------------|------------|
| **Output** | Kategori/label (diskret) | Nilai numerik (kontinu) |
| **Contoh Indonesia** | Spam/bukan spam, churn/tidak churn | Harga rumah di Jakarta, suhu besok |
| **Metrik evaluasi** | Accuracy, precision, recall, F1 | RMSE, MAE, R-squared |
| **Algoritma** | Decision Tree, k-NN, Logistic Regression | Linear Regression, Random Forest Regression |

Dalam bab ini, kita akan fokus pada **classification**.

---

## 12.3 Decision Tree: Konsep dan Implementasi

### 12.3.1 Apa Itu Decision Tree?

Decision tree membuat keputusan dengan cara **memecah data berdasarkan pertanyaan berurutan**, mirip seperti flowchart.

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

### 12.3.2 Information Gain dan Entropy

Bagaimana tree memutuskan pertanyaan mana yang ditanyakan pertama? Jawabannya: **Information Gain**.

**Entropy** mengukur "ketidakpastian" dalam data:

$$Entropy(S) = -\sum_{i=1}^{c} p_i \cdot \log_2(p_i)$$

- Jika 100% data satu kelas: Entropy = **0** (pasti)
- Jika 50-50: Entropy = **1.0** (ketidakpastian maksimum)

**Information Gain** = Entropy sebelum split - Entropy setelah split. Tree memilih fitur dengan IG **tertinggi**.

```
ENTROPY: Mengukur Ketidakpastian
─────────────────────────────────
Entropy = 0.0   →  ████████████  Semua satu kelas (pasti)
Entropy = 0.72  →  ██████░░░░░░  Agak tercampur (80:20)
Entropy = 1.0   →  █████░░░░░░░  Tercampur rata 50:50 (paling tidak pasti)
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
print(f"Fitur: {iris.feature_names}")
print(f"Jumlah sampel: {X.shape[0]}, Jumlah kelas: {len(set(y))}")
print(f"Nama kelas: {list(iris.target_names)}")
```

```python
# Bangun model Decision Tree
dt_model = DecisionTreeClassifier(max_depth=3, random_state=42)
dt_model.fit(X, y)

# Visualisasi tree
plt.figure(figsize=(16, 10))
plot_tree(dt_model, feature_names=iris.feature_names,
          class_names=list(iris.target_names),
          filled=True, rounded=True, fontsize=10)
plt.title("Decision Tree untuk Klasifikasi Iris", fontsize=14)
plt.tight_layout()
plt.show()

# Feature Importance
importance = pd.DataFrame({
    'Fitur': iris.feature_names,
    'Importance': dt_model.feature_importances_
}).sort_values('Importance', ascending=False)

print("=== FEATURE IMPORTANCE ===")
for _, row in importance.iterrows():
    bar = '█' * int(row['Importance'] * 40)
    print(f"  {row['Fitur']:25s}: {row['Importance']:.4f} {bar}")
```

**Kelebihan:** Mudah diinterpretasi, tidak butuh normalisasi, menangani fitur numerik dan kategorikal.
**Kelemahan:** Cenderung overfitting jika tidak dibatasi, sensitif terhadap perubahan kecil dalam data.

---

## 12.4 k-Nearest Neighbors (k-NN)

### 12.4.1 Konsep k-NN

k-NN mengklasifikasikan data baru dengan melihat **k tetangga terdekat** dan mengambil "suara mayoritas" dari kelas mereka.

```
CARA KERJA k-NN (k=3)
──────────────────────
    ○ ○       △ △         ○ = Kelas A
      ○    ?    △         △ = Kelas B
         ○   △            ? = Data baru
       ○       △
Langkah: Hitung jarak → Pilih 3 terdekat → Mayoritas = Kelas A → Prediksi: ?=A
```

### 12.4.2 Memilih Nilai k dan Distance Metrics

| k | Karakteristik |
|---|---------------|
| **k kecil** (k=1) | Sensitif terhadap noise, overfitting |
| **k besar** (k=50) | Terlalu smooth, underfitting |
| **Aturan praktis** | Mulai dengan k = sqrt(n), gunakan k ganjil |

**Euclidean Distance** (default): $d(x,y) = \sqrt{\sum (x_i - y_i)^2}$

**Manhattan Distance** (robust terhadap outlier): $d(x,y) = \sum |x_i - y_i|$

> **Penting:** Karena k-NN berbasis jarak, **standardisasi fitur wajib dilakukan**. Fitur berskala besar (misal gaji dalam jutaan) akan mendominasi perhitungan jarak dibanding fitur berskala kecil (misal usia dalam puluhan).

### 12.4.3 Implementasi k-NN

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Standardisasi fitur (penting untuk k-NN!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Bangun model k-NN
knn_model = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn_model.fit(X_scaled, y)

print(f"k-NN (k={knn_model.n_neighbors})")
print(f"Accuracy pada training data: {knn_model.score(X_scaled, y):.4f}")
```

---

## 12.5 Train-Test Split dan Cross-Validation

### 12.5.1 Mengapa Tidak Boleh Evaluasi pada Data Training?

Model yang "menghafal" data training tapi gagal pada data baru disebut **overfitting**.

```
ANALOGI OVERFITTING
────────────────────
Mahasiswa A: Menghafal soal latihan → Latihan: 100 | UAS (soal baru): 40 → OVERFITTING!
Mahasiswa B: Memahami konsep       → Latihan: 85  | UAS (soal baru): 80 → GENERALISASI!
```

### 12.5.2 Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training: {X_train.shape[0]} sampel ({X_train.shape[0]/len(X)*100:.0f}%)")
print(f"Testing : {X_test.shape[0]} sampel ({X_test.shape[0]/len(X)*100:.0f}%)")
```

> **`stratify=y`** memastikan proporsi kelas sama di train dan test set — penting untuk dataset imbalanced.

### 12.5.3 K-Fold Cross-Validation

```
5-FOLD CROSS-VALIDATION
─────────────────────────
Fold 1: [TEST ] [Train] [Train] [Train] [Train]  → Score 1
Fold 2: [Train] [TEST ] [Train] [Train] [Train]  → Score 2
Fold 3: [Train] [Train] [TEST ] [Train] [Train]  → Score 3
Fold 4: [Train] [Train] [Train] [TEST ] [Train]  → Score 4
Fold 5: [Train] [Train] [Train] [Train] [TEST ]  → Score 5

Final Score = Mean(Score 1..5) ± Std
```

```python
from sklearn.model_selection import cross_val_score

dt_scores = cross_val_score(
    DecisionTreeClassifier(max_depth=3, random_state=42),
    X, y, cv=5, scoring='accuracy'
)
print(f"Decision Tree — 5-Fold CV:")
print(f"  Scores: {dt_scores.round(4)}")
print(f"  Mean: {dt_scores.mean():.4f} ± {dt_scores.std():.4f}")
```

---

## 12.6 Evaluation Metrics

### 12.6.1 Confusion Matrix

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
```

### 12.6.2 Metrik Turunan

| Metrik | Formula | Kapan Penting |
|--------|---------|---------------|
| **Accuracy** | (TP+TN) / Total | Data seimbang |
| **Precision** | TP / (TP+FP) | FP mahal (spam filter: email penting jangan masuk spam) |
| **Recall** | TP / (TP+FN) | FN mahal (deteksi fraud: transaksi penipuan jangan lolos) |
| **F1-Score** | 2*(P*R)/(P+R) | Keseimbangan precision dan recall |

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

# Decision Tree
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

print("=== DECISION TREE ===")
print(f"Akurasi: {accuracy_score(y_test, y_pred_dt):.4f}")
print(classification_report(y_test, y_pred_dt, target_names=iris.target_names))

# k-NN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
y_pred_knn = knn.predict(X_test_scaled)

print("=== k-NN (k=5) ===")
print(f"Akurasi: {accuracy_score(y_test, y_pred_knn):.4f}")
print(classification_report(y_test, y_pred_knn, target_names=iris.target_names))

# Confusion matrices
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
for ax, y_pred, title in zip(axes, [y_pred_dt, y_pred_knn],
                              ['Decision Tree', 'k-NN (k=5)']):
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(cm, display_labels=iris.target_names)
    disp.plot(ax=ax, cmap='Blues')
    ax.set_title(f'Confusion Matrix — {title}')
plt.tight_layout()
plt.show()
```

---

## 12.7 Overfitting vs Underfitting: Bias-Variance Tradeoff

### 12.7.1 Konsep

| Kondisi | Ciri-ciri |
|---------|-----------|
| **Underfitting** | Akurasi rendah di training DAN test — model terlalu sederhana |
| **Good fit** | Akurasi tinggi di training DAN test — model menangkap pola umum |
| **Overfitting** | Akurasi tinggi di training, RENDAH di test — model "menghafal" noise |

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
  └──────────────────────→ Kompleksitas Model
       Sederhana      Kompleks
  ← Underfitting →|← Sweet Spot →|← Overfitting →
```

### 12.7.3 Demonstrasi: Efek max_depth pada Decision Tree

```python
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
plt.xlabel('max_depth')
plt.ylabel('Accuracy')
plt.title('Efek max_depth terhadap Overfitting (Decision Tree)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("Training accuracy naik terus; test accuracy naik lalu TURUN → overfitting")
```

---

## 12.8 Pipeline ML End-to-End

### 12.8.1 Alur Kerja

```
┌─────────────┐    ┌────────────────┐    ┌──────────────┐
│  1. Data     │───→│ 2. Preprocessing│───→│  3. Split    │
│  Collection  │    │ (cleaning,      │    │  Train/Test  │
│              │    │  encoding,      │    │              │
│              │    │  scaling)       │    │              │
└─────────────┘    └────────────────┘    └──────┬───────┘
                                                │
                    ┌──────────────┐    ┌────────▼───────┐
                    │ 5. Evaluate  │←───│ 4. Train Model │
                    │ (metrics, CV)│    │                │
                    └──────┬───────┘    └────────────────┘
                           │
                    ┌──────▼───────┐
                    │ 6. Predict   │
                    │ (new data)   │
                    └──────────────┘
```

### 12.8.2 Pipeline dengan sklearn

```python
from sklearn.pipeline import Pipeline

# Pipeline otomatis: standardisasi + k-NN
knn_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=5))
])

cv_knn = cross_val_score(knn_pipeline, X, y, cv=5, scoring='accuracy')
print(f"k-NN Pipeline — 5-Fold CV: {cv_knn.mean():.4f} ± {cv_knn.std():.4f}")
```

---

## 12.9 Studi Kasus: Klasifikasi dengan Konteks Indonesia

### 12.9.1 Studi Kasus 1: Prediksi Churn Pelanggan Telekomunikasi

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score

# Simulasi data churn pelanggan provider Indonesia
np.random.seed(123)
data_churn = pd.DataFrame({
    'durasi_langganan_bulan': np.concatenate([
        np.random.normal(8, 4, 120),
        np.random.normal(24, 10, 180)
    ]).clip(1, 60),
    'pengeluaran_bulanan_ribu': np.concatenate([
        np.random.normal(45, 15, 120),
        np.random.normal(85, 25, 180)
    ]).clip(10, 200),
    'jumlah_keluhan': np.concatenate([
        np.random.poisson(4, 120),
        np.random.poisson(1, 180)
    ]),
    'frekuensi_login_app': np.concatenate([
        np.random.poisson(2, 120),
        np.random.poisson(8, 180)
    ]),
    'punya_paket_bundling': np.concatenate([
        np.random.binomial(1, 0.20, 120),
        np.random.binomial(1, 0.65, 180)
    ]),
    'churn': [1] * 120 + [0] * 180
})

print("=== DATASET CHURN PELANGGAN ===")
print(f"Jumlah data: {len(data_churn)}")
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

sc = StandardScaler()
X_tr_sc = sc.fit_transform(X_tr)
X_te_sc = sc.transform(X_te)

# Eksperimen beberapa model
models = {
    'Decision Tree (depth=3)': (DecisionTreeClassifier(max_depth=3, random_state=42), False),
    'Decision Tree (depth=5)': (DecisionTreeClassifier(max_depth=5, random_state=42), False),
    'k-NN (k=3)': (KNeighborsClassifier(n_neighbors=3), True),
    'k-NN (k=5)': (KNeighborsClassifier(n_neighbors=5), True),
    'k-NN (k=7)': (KNeighborsClassifier(n_neighbors=7), True),
}

print("=== PERBANDINGAN MODEL — PREDIKSI CHURN ===")
print(f"{'Model':<28} {'Acc':>7} {'Prec':>7} {'Rec':>7} {'F1':>7}")
print("-" * 58)

for name, (model, use_scaled) in models.items():
    if use_scaled:
        model.fit(X_tr_sc, y_tr)
        preds = model.predict(X_te_sc)
    else:
        model.fit(X_tr, y_tr)
        preds = model.predict(X_te)

    print(f"{name:<28} {accuracy_score(y_te, preds):>7.4f} "
          f"{precision_score(y_te, preds):>7.4f} "
          f"{recall_score(y_te, preds):>7.4f} "
          f"{f1_score(y_te, preds):>7.4f}")
```

### 12.9.2 Studi Kasus 2: Klasifikasi Spam SMS

```python
# Simulasi fitur yang diekstrak dari SMS Indonesia
np.random.seed(42)
data_sms = pd.DataFrame({
    'panjang_pesan': np.concatenate([
        np.random.normal(120, 30, 100),    # Spam lebih panjang
        np.random.normal(45, 20, 100)      # Bukan spam lebih pendek
    ]),
    'jumlah_angka': np.concatenate([
        np.random.poisson(8, 100),         # Spam banyak angka (nomor HP, harga)
        np.random.poisson(1, 100)
    ]),
    'jumlah_huruf_besar': np.concatenate([
        np.random.poisson(12, 100),        # Spam banyak kapital (GRATIS, MENANG)
        np.random.poisson(2, 100)
    ]),
    'ada_kata_promo': np.concatenate([
        np.random.binomial(1, 0.85, 100),
        np.random.binomial(1, 0.05, 100)
    ]),
    'label': [1] * 100 + [0] * 100        # 1=spam, 0=bukan spam
})

X_sms = data_sms.drop('label', axis=1)
y_sms = data_sms['label']

X_tr_s, X_te_s, y_tr_s, y_te_s = train_test_split(
    X_sms, y_sms, test_size=0.2, random_state=42, stratify=y_sms
)

dt_spam = DecisionTreeClassifier(max_depth=4, random_state=42)
dt_spam.fit(X_tr_s, y_tr_s)
print("=== KLASIFIKASI SPAM SMS ===")
print(classification_report(y_te_s, dt_spam.predict(X_te_s),
                            target_names=['Bukan Spam', 'Spam']))
```

### 12.9.3 Eksperimen Pemilihan Nilai k

```python
from sklearn.pipeline import Pipeline

k_values = range(1, 21)
cv_means = []

for k in k_values:
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('knn', KNeighborsClassifier(n_neighbors=k))
    ])
    scores = cross_val_score(pipeline, X, y, cv=5, scoring='accuracy')
    cv_means.append(scores.mean())

plt.figure(figsize=(10, 6))
plt.plot(k_values, cv_means, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Nilai k')
plt.ylabel('Cross-Validation Accuracy')
plt.title('Pengaruh Nilai k terhadap Akurasi k-NN (5-Fold CV)')
plt.xticks(k_values)
plt.grid(True, alpha=0.3)

best_k = list(k_values)[np.argmax(cv_means)]
plt.axvline(x=best_k, color='red', linestyle='--', alpha=0.7,
            label=f'k terbaik = {best_k}, Acc = {max(cv_means):.4f}')
plt.legend()
plt.tight_layout()
plt.show()
```

---

## AI Corner: AI sebagai Asisten dalam Workflow ML

### Bagaimana AI Tools Membantu

| Tahap ML | Bantuan AI | Tetap Tanggung Jawab Manusia |
|----------|-----------|------------------------------|
| **Data Understanding** | Generate kode EDA otomatis | Interpretasi pola dan konteks domain |
| **Preprocessing** | Sarankan teknik encoding/scaling | Memilih strategi yang tepat |
| **Model Selection** | Sarankan algoritma yang sesuai | Memahami asumsi dan batasan |
| **Evaluation** | Hitung metrik otomatis | Memilih metrik yang tepat untuk kasus |
| **Interpretation** | Jelaskan confusion matrix | Membuat keputusan bisnis dari hasil |

### Contoh Prompt Efektif

**Baik:**
```
Saya punya dataset 500 pelanggan telekomunikasi Indonesia dengan fitur:
durasi_langganan, pengeluaran_bulanan, jumlah_keluhan. Target: churn (binary).
Dataset imbalanced: 70% tidak churn, 30% churn.
Algoritma apa yang cocok? Metrik evaluasi mana yang tepat?
Berikan kode Python dengan sklearn.
```

**Kurang baik:** `Buatkan model machine learning untuk data saya`

### Prinsip Penting

Selalu verifikasi output AI — jalankan kodenya, cek hasilnya, pahami metriknya. AI mempercepat proses, tetapi **pemahaman konseptual** tentang bias-variance, overfitting, dan pemilihan metrik tetap harus dikuasai. Seorang data scientist yang hanya mengandalkan AI tanpa pemahaman statistik ibarat pengemudi yang tidak tahu cara kerja mesin — bisa jalan, tapi tidak tahu apa yang salah ketika mogok.

---

## Rangkuman Bab 12

1. **Machine Learning** adalah perluasan pemodelan statistik yang mengutamakan kemampuan prediksi. ML dan statistik tradisional saling melengkapi, bukan saling menggantikan.

2. **Supervised learning** menggunakan data berlabel (classification untuk output kategorikal, regression untuk output numerik), sedangkan **unsupervised learning** mencari pola tanpa label.

3. **Decision Tree** bekerja dengan memecah data melalui pertanyaan berurutan berdasarkan **information gain**. Mudah diinterpretasi tetapi rentan overfitting.

4. **k-Nearest Neighbors** mengklasifikasikan berdasarkan tetangga terdekat. Membutuhkan **standardisasi fitur** karena berbasis jarak.

5. **Train-test split** mencegah overfitting; **cross-validation** memberikan estimasi performa lebih robust dengan merotasi data test.

6. **Evaluation metrics** — accuracy, precision, recall, F1-score — memiliki kegunaan berbeda tergantung konteks. **Confusion matrix** adalah fondasi semua metrik ini.

7. **Bias-variance tradeoff** adalah prinsip fundamental: underfitting (high bias) vs overfitting (high variance). Tujuannya menemukan *sweet spot*.

8. **Pipeline ML end-to-end** — dari data collection hingga prediksi — merupakan keterampilan esensial bagi praktisi data di Indonesia.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan utama antara tujuan statistik tradisional dan machine learning. Berikan masing-masing satu contoh dalam konteks bisnis digital Indonesia.

**Soal 2.** Klasifikasikan masalah berikut sebagai supervised/unsupervised DAN classification/regression:
- a) Memprediksi apakah nasabah BCA akan gagal bayar kredit
- b) Mengelompokkan pelanggan Tokopedia berdasarkan pola belanja
- c) Memprediksi harga properti di BSD Tangerang
- d) Mendeteksi email spam di layanan kampus

**Soal 3.** Jelaskan apa yang dimaksud entropy dalam konteks decision tree. Mengapa entropy = 0 menunjukkan kondisi "pasti"?

**Soal 4.** Mengapa standardisasi fitur penting untuk k-NN tetapi tidak diperlukan untuk Decision Tree?

**Soal 5.** Perhatikan confusion matrix berikut (deteksi fraud transaksi):
```
              Prediksi
              Fraud   Legit
Actual Fraud [  80  |  20  ]
       Legit [  15  | 885  ]
```
Hitung: (a) Accuracy, (b) Precision, (c) Recall, (d) F1-Score untuk kelas "Fraud".

### Tingkat Menengah (C2-C3)

**Soal 6.** Model prediksi rating Gojek menghasilkan training accuracy 98% dan test accuracy 65%. Apa fenomena ini? Sebutkan 3 strategi mengatasinya.

**Soal 7.** Tulis kode Python lengkap untuk:
- a) Memuat dataset `load_wine` dari sklearn
- b) Train-test split (80:20) dengan stratify
- c) Decision Tree (`max_depth=3`) + classification report
- d) 5-fold cross-validation

**Soal 8.** Jelaskan perbedaan Euclidean dan Manhattan distance. Kapan Manhattan lebih disarankan? Berikan contoh numerik 2D.

**Soal 9.** Untuk dataset imbalanced (99% legitimate, 1% fraud):
- a) Apakah accuracy metrik yang tepat? Mengapa?
- b) Metrik apa yang lebih informatif?

### Tingkat Mahir (C3-C5)

**Soal 10.** Implementasikan pipeline ML end-to-end untuk `load_breast_cancer`:
- a) EDA dan split data
- b) Bandingkan Decision Tree (`max_depth`: 2, 3, 5, None) dan k-NN (k: 3, 5, 7, 9) dengan 5-fold CV
- c) Untuk konteks medis, metrik mana yang paling penting? Mengapa?

**Soal 11.** Perusahaan e-commerce Indonesia memiliki data pelanggan dengan fitur: durasi_langganan, total_transaksi, rata_rata_belanja, jumlah_keluhan, platform (iOS/Android/Web), kota.
- a) Bagaimana menangani fitur kategorikal?
- b) Tulis kode pipeline ML lengkap untuk prediksi churn
- c) Metrik evaluasi apa yang paling tepat untuk kasus churn?

**Soal 12.** Jelaskan mengapa cross-validation lebih reliable dibanding single train-test split. Seorang kolega mendapat CV accuracy 99.5% pada dataset 95% kelas mayoritas — apakah model ini bagus? Jelaskan dan beri saran perbaikan.

**Soal 13.** Buat tabel perbandingan Decision Tree vs k-NN mencakup: kecepatan training, kecepatan prediksi, interpretabilitas, kebutuhan preprocessing, dan sensitivitas terhadap outlier. Untuk setiap skenario berikut, rekomendasi mana yang lebih cocok dan mengapa:
- Klasifikasi kelayakan kredit (harus bisa menjelaskan ke nasabah)
- Dataset kecil (50 sampel) dengan fitur terstandarisasi
- Dataset berdimensi sangat tinggi (1000 fitur)

**Soal 14.** Refleksi: Sebutkan minimal 4 kaitan antara konsep statistik bab-bab sebelumnya (deskriptif, inferensi, regresi) dengan machine learning di bab ini. Jika Anda membangun model ML untuk proyek nyata di Indonesia (pilih: prediksi banjir Jakarta, deteksi berita hoaks, atau rekomendasi UMKM), jelaskan pipeline lengkapnya.

---

## Referensi

1. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning with Applications in Python (ISLP)*. Springer. — Chapter 2 & 4.
2. Muller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*. O'Reilly Media. — Chapter 2.
3. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.
4. scikit-learn Documentation — [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/tree.html).
5. scikit-learn Documentation — [KNeighborsClassifier](https://scikit-learn.org/stable/modules/neighbors.html).
6. scikit-learn Documentation — [Model Evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html).
7. Breiman, L. (2001). "Statistical Modeling: The Two Cultures." *Statistical Science*, 16(3), 199-231.
8. Provost, F., & Fawcett, T. (2013). *Data Science for Business*. O'Reilly Media.
9. Raschka, S., & Mirjalili, V. (2022). *Python Machine Learning* (4th ed.). Packt Publishing.

---

*Bab berikutnya: **Bab 13 — AI-Augmented Data Analysis***
