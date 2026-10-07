# BAB 6: DECISION TREE DAN ENSEMBLE METHODS

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| Sub-CPMK 6.1 | Menganalisis proses pembuatan decision tree berdasarkan information gain dan Gini impurity | C4 |
| Sub-CPMK 6.2 | Menganalisis performa ensemble methods (Random Forest) dan membandingkannya dengan single decision tree | C4 |

**CPMK-3:** Menerapkan algoritma supervised learning untuk permasalahan regresi dan klasifikasi.

---

## Estimasi Waktu

| Aktivitas | Durasi |
|-----------|--------|
| Membaca materi | 90 menit |
| Praktik kode Python | 120 menit |
| Mengerjakan latihan soal | 60 menit |
| **Total** | **270 menit (4.5 jam)** |

---

## Prasyarat

- Bab 5: Regresi Linear dan Logistik
- Pemahaman dasar confusion matrix, accuracy, precision, recall
- Kemampuan dasar Python, NumPy, pandas, dan sklearn

---

## 6.1 Decision Tree Concepts (Konsep Decision Tree)

### 6.1.1 How Trees Split: Information Gain

**Decision tree** (pohon keputusan) adalah algoritma machine learning yang membuat keputusan dengan cara **membagi data secara bertahap** berdasarkan pertanyaan-pertanyaan (kondisi) pada feature.

**Analogi:** Bayangkan Anda bermain game "20 Questions" — Anda mengajukan pertanyaan ya/tidak untuk menebak jawaban. Decision tree bekerja dengan cara yang sama.

```
Contoh: Apakah seorang nasabah berisiko kredit macet?

                    [Penghasilan > 10 juta?]
                     /                    \
                   Ya                     Tidak
                  /                         \
        [Lama kerja > 3 tahun?]        [Riwayat macet?]
          /            \                 /           \
        Ya             Tidak           Ya            Tidak
        /                \             /               \
   [Risiko Rendah]  [Risiko Sedang]  [Risiko Tinggi]  [Risiko Sedang]
```

**Information gain** mengukur seberapa baik sebuah feature memisahkan data ke dalam kelas-kelas yang homogen. Feature dengan information gain tertinggi dipilih sebagai node pemisah.

```
Information Gain = Entropy(parent) - Σ (|child_i| / |parent|) × Entropy(child_i)

Semakin tinggi Information Gain → semakin baik feature tersebut memisahkan data
```

### 6.1.2 Entropy and Gini Impurity

**Entropy** mengukur tingkat ketidakteraturan (*impurity*) dalam data. Semakin campuran kelasnya, semakin tinggi entropy.

```
Entropy(S) = -Σ pᵢ × log₂(pᵢ)

di mana pᵢ = proporsi kelas ke-i dalam dataset S

Contoh:
  - Data semua kelas A: Entropy = -1 × log₂(1) = 0 (paling teratur)
  - Data 50% A, 50% B: Entropy = -(0.5 × log₂(0.5)) × 2 = 1 (paling acak)
```

**Gini Impurity** adalah alternatif yang lebih cepat dihitung:

```
Gini(S) = 1 - Σ pᵢ²

Contoh:
  - Data semua kelas A: Gini = 1 - 1² = 0
  - Data 50% A, 50% B: Gini = 1 - (0.5² + 0.5²) = 0.5
```

```python
import numpy as np
import matplotlib.pyplot as plt

# Visualisasi Entropy vs Gini untuk kasus binary classification
p = np.linspace(0.001, 0.999, 200)

# Entropy
entropy = -(p * np.log2(p) + (1-p) * np.log2(1-p))

# Gini Impurity
gini = 2 * p * (1 - p)

# Misclassification Error (untuk perbandingan)
misclass = 1 - np.maximum(p, 1-p)

plt.figure(figsize=(10, 6))
plt.plot(p, entropy, 'b-', linewidth=2, label='Entropy')
plt.plot(p, gini, 'r-', linewidth=2, label='Gini Impurity')
plt.plot(p, misclass, 'g--', linewidth=2, label='Misclassification Error')
plt.xlabel('Proporsi Kelas Positif (p)', fontsize=12)
plt.ylabel('Impurity', fontsize=12)
plt.title('Perbandingan Fungsi Impurity', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 6.1.3 Building a Decision Tree (Membangun Decision Tree)

Algoritma pembangunan decision tree (ID3/C4.5/CART):

```
Algoritma CART (Classification and Regression Trees):
1. Mulai dari root node (seluruh data)
2. Untuk setiap feature, cari split point terbaik
   yang memaksimalkan information gain (atau meminimalkan Gini)
3. Pilih feature + split point dengan information gain tertinggi
4. Bagi data menjadi dua child nodes
5. Ulangi langkah 2-4 untuk setiap child node (rekursif)
6. Berhenti jika:
   - Semua data dalam node sudah satu kelas (pure)
   - Kedalaman maksimum tercapai (max_depth)
   - Jumlah sampel minimum tercapai (min_samples_split)
```

```python
import numpy as np

def hitung_entropy(y):
    """Menghitung entropy dari array label"""
    classes, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)
    entropy = -np.sum(probs * np.log2(probs + 1e-10))
    return entropy

def hitung_gini(y):
    """Menghitung Gini impurity dari array label"""
    classes, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)
    gini = 1 - np.sum(probs ** 2)
    return gini

def hitung_information_gain(y_parent, y_left, y_right, criterion='entropy'):
    """Menghitung information gain dari sebuah split"""
    if criterion == 'entropy':
        func = hitung_entropy
    else:
        func = hitung_gini

    n = len(y_parent)
    n_left = len(y_left)
    n_right = len(y_right)

    # Information Gain = Impurity(parent) - weighted avg Impurity(children)
    ig = func(y_parent) - (
        (n_left / n) * func(y_left) +
        (n_right / n) * func(y_right)
    )
    return ig

# Contoh: data mahasiswa (lulus/tidak)
# Feature: jam_belajar, kehadiran_persen
# Label: 1 = lulus, 0 = tidak lulus
labels = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0])

print(f"Entropy seluruh data: {hitung_entropy(labels):.4f}")
print(f"Gini seluruh data   : {hitung_gini(labels):.4f}")

# Simulasi split: jam_belajar > 10
labels_kiri = np.array([1, 1, 1, 1, 1, 1, 1])   # jam > 10
labels_kanan = np.array([0, 0, 0, 0, 0, 0, 1, 0])  # jam <= 10

ig_entropy = hitung_information_gain(labels, labels_kiri, labels_kanan, 'entropy')
ig_gini = hitung_information_gain(labels, labels_kiri, labels_kanan, 'gini')

print(f"\nSplit: jam_belajar > 10")
print(f"  Information Gain (Entropy): {ig_entropy:.4f}")
print(f"  Information Gain (Gini)   : {ig_gini:.4f}")
```

---

## 6.2 Decision Tree with sklearn

### 6.2.1 DecisionTreeClassifier

```python
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Dataset: prediksi kelulusan mahasiswa UAI
np.random.seed(42)
n = 300

data_mhs = pd.DataFrame({
    'jam_belajar_per_minggu': np.random.randint(2, 30, n),
    'kehadiran_persen': np.random.randint(40, 100, n),
    'nilai_tugas_rata': np.round(np.random.uniform(30, 100, n), 1),
    'nilai_kuis_rata': np.round(np.random.uniform(20, 100, n), 1),
    'aktif_organisasi': np.random.choice([0, 1], n, p=[0.6, 0.4]),
})

# Label lulus berdasarkan kombinasi faktor
skor = (
    data_mhs['jam_belajar_per_minggu'] * 2 +
    data_mhs['kehadiran_persen'] * 0.5 +
    data_mhs['nilai_tugas_rata'] * 0.3 +
    data_mhs['nilai_kuis_rata'] * 0.3 -
    data_mhs['aktif_organisasi'] * 5 +
    np.random.normal(0, 10, n)
)
data_mhs['lulus'] = (skor > 55).astype(int)

print(f"Distribusi kelas:\n{data_mhs['lulus'].value_counts()}")

# Feature dan target
X = data_mhs.drop('lulus', axis=1)
y = data_mhs['lulus']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Latih Decision Tree
dt_model = DecisionTreeClassifier(
    criterion='gini',        # atau 'entropy'
    max_depth=5,             # batas kedalaman
    min_samples_split=10,    # minimum sampel untuk split
    min_samples_leaf=5,      # minimum sampel di leaf
    random_state=42
)
dt_model.fit(X_train, y_train)

# Evaluasi
y_pred = dt_model.predict(X_test)
print(f"\n=== DECISION TREE - PREDIKSI KELULUSAN ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"\n{classification_report(y_test, y_pred, target_names=['Tidak Lulus', 'Lulus'])}")
```

### 6.2.2 Visualizing Trees (Visualisasi Pohon)

```python
from sklearn.tree import plot_tree, export_text
import matplotlib.pyplot as plt

# Visualisasi pohon keputusan
plt.figure(figsize=(20, 10))
plot_tree(
    dt_model,
    feature_names=X.columns.tolist(),
    class_names=['Tidak Lulus', 'Lulus'],
    filled=True,
    rounded=True,
    fontsize=8,
    max_depth=3  # tampilkan hanya 3 level pertama
)
plt.title('Decision Tree: Prediksi Kelulusan Mahasiswa', fontsize=16)
plt.tight_layout()
plt.show()

# Tampilkan aturan dalam bentuk teks
print("=== ATURAN DECISION TREE ===")
rules = export_text(dt_model, feature_names=list(X.columns), max_depth=3)
print(rules)
```

### 6.2.3 Feature Importance (Kepentingan Feature)

```python
import pandas as pd
import matplotlib.pyplot as plt

# Feature importance dari model
importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': dt_model.feature_importances_
}).sort_values('Importance', ascending=True)

print("=== FEATURE IMPORTANCE ===")
for _, row in importance_df.iterrows():
    print(f"  {row['Feature']:30s}: {row['Importance']:.4f}")

# Visualisasi
plt.figure(figsize=(10, 5))
plt.barh(importance_df['Feature'], importance_df['Importance'],
         color='steelblue')
plt.xlabel('Importance', fontsize=12)
plt.title('Feature Importance: Decision Tree', fontsize=14)
plt.tight_layout()
plt.show()
```

---

## 6.3 Overfitting in Trees (Overfitting pada Decision Tree)

### 6.3.1 Training vs Testing Accuracy

**Overfitting** terjadi ketika model terlalu "menghafal" data training sehingga performanya buruk pada data baru (testing). Decision tree sangat rentan terhadap overfitting karena dapat terus tumbuh sampai setiap leaf hanya berisi satu sampel.

```python
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Bandingkan performa tree dengan berbagai kedalaman
depths = range(1, 21)
train_accs = []
test_accs = []

for depth in depths:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_train, y_train)

    train_acc = accuracy_score(y_train, dt.predict(X_train))
    test_acc = accuracy_score(y_test, dt.predict(X_test))

    train_accs.append(train_acc)
    test_accs.append(test_acc)

# Visualisasi overfitting
plt.figure(figsize=(10, 6))
plt.plot(depths, train_accs, 'b-o', linewidth=2, label='Training Accuracy')
plt.plot(depths, test_accs, 'r-o', linewidth=2, label='Testing Accuracy')
plt.xlabel('Max Depth', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
plt.title('Overfitting: Training vs Testing Accuracy', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xticks(depths)

# Tandai titik optimal
best_depth = depths[np.argmax(test_accs)]
plt.axvline(x=best_depth, color='green', linestyle='--',
            label=f'Best depth = {best_depth}')
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()

print(f"Depth optimal: {best_depth}")
print(f"Test accuracy terbaik: {max(test_accs):.4f}")
```

### 6.3.2 Pruning: max_depth, min_samples_split

**Pruning** (pemangkasan) adalah teknik untuk mengurangi overfitting pada decision tree:

| Parameter | Deskripsi | Efek |
|-----------|-----------|------|
| `max_depth` | Kedalaman maksimum tree | Semakin kecil → model lebih sederhana |
| `min_samples_split` | Minimum sampel untuk melakukan split | Semakin besar → split lebih jarang |
| `min_samples_leaf` | Minimum sampel di setiap leaf | Mencegah leaf dengan sampel sangat sedikit |
| `max_features` | Jumlah feature yang dipertimbangkan untuk split | Menambah randomness |
| `max_leaf_nodes` | Jumlah maksimum leaf nodes | Membatasi kompleksitas tree |

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Bandingkan tree tanpa dan dengan pruning
model_tanpa_pruning = DecisionTreeClassifier(random_state=42)
model_tanpa_pruning.fit(X_train, y_train)

model_dengan_pruning = DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=20,
    min_samples_leaf=10,
    random_state=42
)
model_dengan_pruning.fit(X_train, y_train)

print("=== PERBANDINGAN PRUNING ===")
print(f"\nTanpa Pruning:")
print(f"  Kedalaman tree     : {model_tanpa_pruning.get_depth()}")
print(f"  Jumlah leaf nodes  : {model_tanpa_pruning.get_n_leaves()}")
print(f"  Train accuracy     : {accuracy_score(y_train, model_tanpa_pruning.predict(X_train)):.4f}")
print(f"  Test accuracy      : {accuracy_score(y_test, model_tanpa_pruning.predict(X_test)):.4f}")

print(f"\nDengan Pruning:")
print(f"  Kedalaman tree     : {model_dengan_pruning.get_depth()}")
print(f"  Jumlah leaf nodes  : {model_dengan_pruning.get_n_leaves()}")
print(f"  Train accuracy     : {accuracy_score(y_train, model_dengan_pruning.predict(X_train)):.4f}")
print(f"  Test accuracy      : {accuracy_score(y_test, model_dengan_pruning.predict(X_test)):.4f}")
```

---

## 6.4 Ensemble Methods (Metode Ensemble)

### 6.4.1 Bagging Concept (Konsep Bagging)

**Ensemble methods** adalah teknik yang menggabungkan beberapa model "lemah" untuk membuat model yang lebih kuat. Prinsipnya: **wisdom of the crowd** — keputusan bersama seringkali lebih baik daripada keputusan individu.

**Bagging** (Bootstrap Aggregating):

```
Algoritma Bagging:
1. Ambil B bootstrap samples dari data training
   (sampling dengan pengembalian / with replacement)
2. Latih model independen pada setiap bootstrap sample
3. Gabungkan prediksi:
   - Klasifikasi: voting mayoritas
   - Regresi: rata-rata prediksi

     Data Training
     ┌──────────────┐
     │ x₁ x₂ ... y │
     │ ............ │
     │ ............ │
     └──────────────┘
      │    │    │
      ↓    ↓    ↓      ← Bootstrap Sampling
   ┌────┐┌────┐┌────┐
   │ S₁ ││ S₂ ││ S₃ │  ← B sampel bootstrap
   └──┬─┘└──┬─┘└──┬─┘
      ↓     ↓     ↓     ← Latih model independen
   ┌────┐┌────┐┌────┐
   │ M₁ ││ M₂ ││ M₃ │
   └──┬─┘└──┬─┘└──┬─┘
      ↓     ↓     ↓
      └─────┼─────┘     ← Agregasi (voting/averaging)
            ↓
       Prediksi Akhir
```

### 6.4.2 Random Forest: Multiple Trees, Feature Sampling

**Random Forest** memperluas bagging dengan menambahkan **random feature selection** pada setiap split:

```
Random Forest = Bagging + Random Feature Selection

Pada setiap split node:
  - Decision Tree biasa: pertimbangkan SEMUA feature
  - Random Forest: pertimbangkan hanya SUBSET acak dari feature
    (biasanya √p feature untuk klasifikasi, p/3 untuk regresi,
     di mana p = total jumlah feature)

Manfaat random feature selection:
  - Mengurangi korelasi antar tree
  - Membuat setiap tree melihat "perspektif" berbeda
  - Menghasilkan ensemble yang lebih diverse dan robust
```

### 6.4.3 RandomForestClassifier with sklearn

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt

# Latih Random Forest pada dataset yang sama
rf_model = RandomForestClassifier(
    n_estimators=100,        # jumlah tree
    max_depth=10,            # kedalaman maksimum per tree
    min_samples_split=10,    # minimum sampel untuk split
    max_features='sqrt',     # √p feature pada setiap split
    random_state=42,
    n_jobs=-1                # gunakan semua CPU cores
)
rf_model.fit(X_train, y_train)

# Evaluasi
y_pred_rf = rf_model.predict(X_test)

print("=== RANDOM FOREST - PREDIKSI KELULUSAN ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred_rf):.4f}")
print(f"\n{classification_report(y_test, y_pred_rf, target_names=['Tidak Lulus', 'Lulus'])}")

# Feature importance dari Random Forest
importance_rf = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_model.feature_importances_
}).sort_values('Importance', ascending=True)

plt.figure(figsize=(10, 5))
plt.barh(importance_rf['Feature'], importance_rf['Importance'],
         color='forestgreen')
plt.xlabel('Importance', fontsize=12)
plt.title('Feature Importance: Random Forest', fontsize=14)
plt.tight_layout()
plt.show()
```

---

## 6.5 Hyperparameter Tuning

### 6.5.1 GridSearchCV

**GridSearchCV** melakukan pencarian exhaustive atas kombinasi hyperparameter yang ditentukan, menggunakan cross-validation untuk mengevaluasi setiap kombinasi.

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Definisikan grid hyperparameter
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10, None],
    'min_samples_split': [2, 5, 10],
    'max_features': ['sqrt', 'log2'],
}

# Hitung total kombinasi
total_kombinasi = 1
for v in param_grid.values():
    total_kombinasi *= len(v)
print(f"Total kombinasi: {total_kombinasi}")
print(f"Dengan 5-fold CV: {total_kombinasi * 5} model dilatih")

# GridSearchCV
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,                    # 5-fold cross-validation
    scoring='accuracy',      # metrik evaluasi
    n_jobs=-1,               # paralelisasi
    verbose=1                # tampilkan progress
)

grid_search.fit(X_train, y_train)

# Hasil terbaik
print(f"\n=== HASIL GRID SEARCH ===")
print(f"Parameter terbaik: {grid_search.best_params_}")
print(f"Accuracy terbaik (CV): {grid_search.best_score_:.4f}")

# Evaluasi pada data test
best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test)
print(f"Accuracy pada data test: {accuracy_score(y_test, y_pred_best):.4f}")

# Top-5 kombinasi
results_df = pd.DataFrame(grid_search.cv_results_)
top5 = results_df.nsmallest(5, 'rank_test_score')[
    ['params', 'mean_test_score', 'std_test_score', 'rank_test_score']
]
print(f"\nTop-5 kombinasi:")
print(top5.to_string(index=False))
```

### 6.5.2 Best Practices (Praktik Terbaik)

| Praktik | Penjelasan |
|---------|-----------|
| Mulai dengan grid kecil | Coba beberapa nilai dulu, lalu perkecil range |
| Gunakan `RandomizedSearchCV` untuk grid besar | Lebih efisien dari grid search untuk banyak parameter |
| Selalu gunakan cross-validation | Hindari evaluasi pada data training |
| Perhatikan `std_test_score` | Standar deviasi tinggi menunjukkan model tidak stabil |
| Jangan overfit hyperparameter | Banyak tuning bisa menyebabkan overfitting pada validation set |
| Evaluasi akhir pada test set | Test set hanya digunakan SEKALI di akhir |

---

## 6.6 Comparing Tree vs Forest (Perbandingan Decision Tree vs Random Forest)

```python
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import time

# Bandingkan berbagai model
models = {
    'Decision Tree (max_depth=3)': DecisionTreeClassifier(max_depth=3, random_state=42),
    'Decision Tree (max_depth=10)': DecisionTreeClassifier(max_depth=10, random_state=42),
    'Decision Tree (no limit)': DecisionTreeClassifier(random_state=42),
    'Random Forest (50 trees)': RandomForestClassifier(n_estimators=50, random_state=42),
    'Random Forest (100 trees)': RandomForestClassifier(n_estimators=100, random_state=42),
    'Random Forest (200 trees)': RandomForestClassifier(n_estimators=200, random_state=42),
}

results = []
for name, model in models.items():
    start = time.time()

    # Cross-validation
    cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')

    # Latih dan evaluasi pada test set
    model.fit(X_train, y_train)
    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))

    elapsed = time.time() - start

    results.append({
        'Model': name,
        'CV Mean': cv_scores.mean(),
        'CV Std': cv_scores.std(),
        'Train Acc': train_acc,
        'Test Acc': test_acc,
        'Time (s)': elapsed
    })

results_df = pd.DataFrame(results)
print("=== PERBANDINGAN MODEL ===")
print(results_df.to_string(index=False))

# Visualisasi perbandingan
fig, ax = plt.subplots(figsize=(12, 6))
x = range(len(results_df))
width = 0.3

bars1 = ax.bar([i - width for i in x], results_df['Train Acc'],
               width, label='Training', color='steelblue', alpha=0.8)
bars2 = ax.bar(x, results_df['Test Acc'],
               width, label='Testing', color='coral', alpha=0.8)
bars3 = ax.bar([i + width for i in x], results_df['CV Mean'],
               width, label='CV Mean', color='forestgreen', alpha=0.8)

ax.set_xlabel('Model', fontsize=12)
ax.set_ylabel('Accuracy', fontsize=12)
ax.set_title('Perbandingan Decision Tree vs Random Forest', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(results_df['Model'], rotation=45, ha='right', fontsize=9)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()
```

---

## 6.7 Studi Kasus Indonesia: Customer Churn Prediction (Prediksi Churn Pelanggan)

### 6.7.1 Konteks

**Churn** adalah kondisi ketika pelanggan berhenti menggunakan layanan. Di Indonesia, persaingan antar penyedia layanan telekomunikasi dan e-commerce sangat ketat, sehingga prediksi churn menjadi sangat penting.

```python
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Dataset churn pelanggan telekomunikasi Indonesia (simulasi)
np.random.seed(42)
n = 500

data_churn = pd.DataFrame({
    'lama_berlangganan_bulan': np.random.randint(1, 72, n),
    'tagihan_bulanan_ribu': np.round(np.random.uniform(30, 300, n), 0),
    'jumlah_keluhan': np.random.poisson(2, n),
    'penggunaan_data_gb': np.round(np.random.uniform(0.5, 50, n), 1),
    'kontrak': np.random.choice(['Bulanan', 'Tahunan', '2-Tahun'], n,
                                 p=[0.5, 0.3, 0.2]),
    'metode_pembayaran': np.random.choice(
        ['Transfer Bank', 'E-Wallet', 'Kartu Kredit', 'Potong Pulsa'], n
    ),
    'layanan_tambahan': np.random.randint(0, 5, n),
})

# Encode variabel kategorikal
le_kontrak = LabelEncoder()
data_churn['kontrak_encoded'] = le_kontrak.fit_transform(data_churn['kontrak'])
le_bayar = LabelEncoder()
data_churn['bayar_encoded'] = le_bayar.fit_transform(data_churn['metode_pembayaran'])

# Label churn (faktor: lama berlangganan rendah, keluhan tinggi, bulanan)
skor_churn = (
    -data_churn['lama_berlangganan_bulan'] * 0.5
    + data_churn['jumlah_keluhan'] * 8
    + data_churn['tagihan_bulanan_ribu'] * 0.05
    - data_churn['layanan_tambahan'] * 5
    + (data_churn['kontrak'] == 'Bulanan').astype(int) * 15
    + np.random.normal(0, 10, n)
)
data_churn['churn'] = (skor_churn > 10).astype(int)

print(f"Distribusi churn:\n{data_churn['churn'].value_counts()}")
print(f"Churn rate: {data_churn['churn'].mean():.2%}")

# Feature numerik
feature_cols = ['lama_berlangganan_bulan', 'tagihan_bulanan_ribu',
                'jumlah_keluhan', 'penggunaan_data_gb',
                'kontrak_encoded', 'bayar_encoded', 'layanan_tambahan']
X = data_churn[feature_cols]
y = data_churn['churn']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# --- Model 1: Decision Tree ---
dt_churn = DecisionTreeClassifier(max_depth=5, min_samples_leaf=10,
                                   random_state=42)
dt_churn.fit(X_train, y_train)
y_pred_dt = dt_churn.predict(X_test)
y_prob_dt = dt_churn.predict_proba(X_test)[:, 1]

# --- Model 2: Random Forest ---
rf_churn = RandomForestClassifier(n_estimators=100, max_depth=10,
                                   random_state=42, n_jobs=-1)
rf_churn.fit(X_train, y_train)
y_pred_rf = rf_churn.predict(X_test)
y_prob_rf = rf_churn.predict_proba(X_test)[:, 1]

# Perbandingan
print("\n=== PERBANDINGAN MODEL: PREDIKSI CHURN ===")
print(f"\n--- Decision Tree ---")
print(classification_report(y_test, y_pred_dt, target_names=['Tidak Churn', 'Churn']))
print(f"AUC-ROC: {roc_auc_score(y_test, y_prob_dt):.4f}")

print(f"\n--- Random Forest ---")
print(classification_report(y_test, y_pred_rf, target_names=['Tidak Churn', 'Churn']))
print(f"AUC-ROC: {roc_auc_score(y_test, y_prob_rf):.4f}")

# Feature importance perbandingan
fig, axes = plt.subplots(1, 2, figsize=(16, 5))

for ax, model, title, color in zip(
    axes,
    [dt_churn, rf_churn],
    ['Decision Tree', 'Random Forest'],
    ['steelblue', 'forestgreen']
):
    imp_df = pd.DataFrame({
        'Feature': feature_cols,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=True)

    ax.barh(imp_df['Feature'], imp_df['Importance'], color=color)
    ax.set_xlabel('Importance')
    ax.set_title(f'Feature Importance: {title}')

plt.suptitle('Prediksi Customer Churn - Telekomunikasi Indonesia', fontsize=14)
plt.tight_layout()
plt.show()

# Insight bisnis
print("\n=== INSIGHT BISNIS ===")
print("Faktor utama yang mendorong churn:")
imp_rf = pd.DataFrame({
    'Feature': feature_cols,
    'Importance': rf_churn.feature_importances_
}).sort_values('Importance', ascending=False)

for _, row in imp_rf.head(3).iterrows():
    print(f"  - {row['Feature']}: importance = {row['Importance']:.4f}")
print("\nRekomendasi:")
print("  1. Berikan insentif perpanjangan kontrak tahunan")
print("  2. Tangani keluhan pelanggan dengan cepat (SLA < 24 jam)")
print("  3. Tawarkan paket bundling untuk meningkatkan layanan tambahan")
```

---

## 6.8 AI Corner: Menggunakan AI untuk Menjelaskan Keputusan Tree kepada Stakeholder

**Level: Intermediate**

### 6.8.1 Apa yang Bisa AI Bantu?

| AI Bisa | AI Tidak Bisa |
|---------|--------------|
| Menerjemahkan aturan tree ke bahasa bisnis | Menentukan aturan bisnis yang optimal |
| Membuat visualisasi tree lebih informatif | Menjamin tree rules berlaku di masa depan |
| Menjelaskan konsep entropy/Gini secara sederhana | Menggantikan keahlian domain expert |
| Menyarankan hyperparameter yang tepat | Menentukan apakah tree model cocok untuk masalah Anda |
| Membantu interpretasi feature importance | Menentukan kausalitas dari korelasi |

### 6.8.2 Contoh Prompt yang Baik

```
Prompt 1 (Interpretasi Rule):
"Decision tree saya menghasilkan rule: jika jumlah_keluhan > 3
AND kontrak = 'Bulanan' THEN churn = 1 (confidence 85%).
Jelaskan rule ini dalam bahasa yang mudah dipahami oleh
manajer pemasaran yang tidak paham ML."

Prompt 2 (Perbandingan Model):
"Model Decision Tree saya accuracy 82% dan Random Forest 88%
pada dataset customer churn. Feature importance berubah
signifikan antara kedua model. Apa yang menyebabkan perbedaan
ini dan kapan saya harus memilih DT vs RF?"

Prompt 3 (Tuning):
"Random Forest saya memiliki 20 feature dan 5000 sampel.
Berapa n_estimators dan max_depth yang sebaiknya saya coba?
Berikan range yang masuk akal untuk GridSearchCV."
```

### 6.8.3 Template AI Usage Log untuk Bab 6

```markdown
## AI Usage Log — BAB 6: Decision Tree dan Ensemble Methods

### Interaksi 1
- **Tool:** [Claude / ChatGPT / Copilot]
- **Prompt:** [Copy-paste prompt Anda]
- **Output:** [Ringkasan jawaban AI]
- **Verifikasi:** [Sudah / Belum diverifikasi? Hasilnya?]
- **Modifikasi:** [Apa yang Anda ubah/tambahkan]
- **Refleksi:** [Apa yang Anda pelajari?]
```

---

## Rangkuman Bab 6

1. **Decision tree** membuat keputusan klasifikasi/regresi melalui serangkaian pertanyaan biner yang membagi data secara rekursif. Setiap split dipilih berdasarkan **information gain** (entropy) atau **Gini impurity**.

2. **Entropy** mengukur ketidakteraturan data (0 = murni, 1 = maksimum untuk binary). **Gini impurity** adalah alternatif yang lebih cepat dihitung.

3. Decision tree mudah diinterpretasi dan divisualisasikan, tetapi sangat rentan terhadap **overfitting**. **Pruning** (max_depth, min_samples_split, dll.) membantu mengontrol kompleksitas model.

4. **Ensemble methods** menggabungkan banyak model lemah menjadi model yang kuat. **Bagging** melatih model pada bootstrap samples.

5. **Random Forest** menggabungkan bagging dengan random feature selection pada setiap split, menghasilkan model yang lebih robust dan akurat dibandingkan single decision tree.

6. **GridSearchCV** membantu menemukan kombinasi hyperparameter optimal melalui pencarian exhaustive dengan cross-validation.

7. Dalam konteks bisnis Indonesia, decision tree dan random forest sangat berguna untuk **prediksi churn pelanggan**, **credit scoring**, dan masalah klasifikasi lain yang membutuhkan interpretabilitas.

---

## Latihan Soal

### Tingkat Dasar (C2-C3)

**Soal 1.** Jelaskan konsep decision tree menggunakan analogi kehidupan sehari-hari. Berikan contoh bagaimana Anda menggunakan "pohon keputusan" tanpa sadar dalam memilih transportasi (GoRide vs TransJakarta vs jalan kaki).

**Soal 2.** Hitung entropy untuk dataset berikut:
- Dataset A: 10 sampel kelas Positif, 0 sampel kelas Negatif
- Dataset B: 5 sampel kelas Positif, 5 sampel kelas Negatif
- Dataset C: 7 sampel kelas Positif, 3 sampel kelas Negatif

Interpretasikan hasilnya.

**Soal 3.** Jelaskan perbedaan antara entropy dan Gini impurity. Kapan kita menggunakan masing-masing?

**Soal 4.** Apa yang dimaksud dengan overfitting pada decision tree? Jelaskan mengapa tree tanpa batasan kedalaman cenderung overfit.

**Soal 5.** Jelaskan konsep bagging dengan analogi sederhana. Mengapa menggabungkan banyak model bisa menghasilkan model yang lebih baik?

### Tingkat Menengah (C3-C4)

**Soal 6.** Tulis kode Python menggunakan sklearn untuk melatih `DecisionTreeClassifier` pada dataset prediksi apakah mahasiswa akan mendapatkan **IPK di atas 3.0** berdasarkan jam belajar, kehadiran, dan nilai tugas. Gunakan data simulasi minimal 200 sampel. Tampilkan:
- a) Visualisasi tree (max_depth=3)
- b) Feature importance
- c) Classification report

**Soal 7.** Bandingkan `DecisionTreeClassifier` dengan `RandomForestClassifier` pada dataset yang sama dari Soal 6. Gunakan 5-fold cross-validation. Model mana yang lebih baik dan mengapa?

**Soal 8.** Jelaskan perbedaan antara decision tree biasa dan random forest dalam hal:
- a) Cara memilih feature pada setiap split
- b) Kecenderungan overfitting
- c) Interpretabilitas
- d) Waktu komputasi

**Soal 9.** Implementasikan `GridSearchCV` untuk mencari hyperparameter optimal Random Forest pada dataset dari Soal 6. Gunakan parameter grid:
- `n_estimators`: [50, 100, 200]
- `max_depth`: [3, 5, 10]
- `min_samples_split`: [2, 5, 10]

### Tingkat Mahir (C4-C5)

**Soal 10.** Implementasikan perhitungan information gain secara manual (tanpa sklearn) untuk dataset kecil. Tentukan feature dan split point terbaik. Bandingkan hasilnya dengan `DecisionTreeClassifier`.

**Soal 11.** Anda diminta membangun model prediksi churn untuk perusahaan e-commerce Indonesia. Dataset memiliki class imbalance (90% tidak churn, 10% churn). Jelaskan:
- a) Mengapa accuracy bukan metrik yang tepat?
- b) Metrik apa yang harus digunakan?
- c) Teknik apa yang bisa menangani class imbalance?
- d) Implementasikan solusi lengkap dengan Python

**Soal 12.** Lakukan analisis: bagaimana jumlah `n_estimators` pada Random Forest mempengaruhi accuracy dan waktu komputasi? Buat plot n_estimators (dari 10 sampai 500) vs accuracy dan n_estimators vs training time.

---

## Referensi

1. Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5-32.
2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2023). *An Introduction to Statistical Learning* (2nd ed.). Springer.
3. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
4. Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.
5. Quinlan, J. R. (1986). Induction of Decision Trees. *Machine Learning*, 1(1), 81-106.
6. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.

---

*Bab berikutnya: **Bab 7 — Support Vector Machine dan K-Nearest Neighbors***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
