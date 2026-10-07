# Lab 13: Pengantar Machine Learning — Klasifikasi

**Mata Kuliah:** Statistika — Universitas Al Azhar Indonesia
**Minggu:** 13
**Platform:** Google Colab (Python)

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. Memahami alur kerja (*workflow*) machine learning untuk klasifikasi
2. Membagi data menjadi training dan testing set dengan `train_test_split`
3. Membangun model Decision Tree dan k-Nearest Neighbors (k-NN)
4. Mengevaluasi model: confusion matrix, classification report, accuracy
5. Membandingkan performa beberapa model
6. Melakukan cross-validation untuk evaluasi yang lebih robust

---

## Persiapan

### Library yang Dibutuhkan

```python
# Jalankan cell ini terlebih dahulu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# scikit-learn
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix, classification_report,
    accuracy_score, ConfusionMatrixDisplay
)
from sklearn.datasets import load_iris

# Pengaturan
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("Semua library berhasil dimuat!")
```

### Konsep Singkat: Alur Kerja Machine Learning

```
┌─────────────┐    ┌──────────────┐    ┌──────────────┐
│  1. Data     │───→│  2. Preprocessing │───→│  3. Split    │
│  Collection  │    │  (cleaning,   │    │  Train/Test  │
│              │    │   encoding)   │    │              │
└─────────────┘    └──────────────┘    └──────┬───────┘
                                              │
                   ┌──────────────┐    ┌──────▼───────┐
                   │  5. Evaluate │←───│  4. Train    │
                   │  (accuracy,  │    │  Model       │
                   │   confusion) │    │              │
                   └──────┬───────┘    └──────────────┘
                          │
                   ┌──────▼───────┐
                   │  6. Predict  │
                   │  (new data)  │
                   └──────────────┘
```

---

## Langkah-langkah Praktikum

### Langkah 1: Load dan Eksplorasi Dataset

```python
# Menggunakan dataset Iris dari sklearn
iris = load_iris()

data = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)
data['species'] = iris.target
data['species_name'] = data['species'].map({
    0: 'setosa', 1: 'versicolor', 2: 'virginica'
})

print("=== Dataset Iris ===")
print(f"Jumlah data  : {len(data)}")
print(f"Jumlah fitur : {len(iris.feature_names)}")
print(f"Kelas target : {iris.target_names.tolist()}")
print()
print("5 data pertama:")
data.head()
```

```python
# Statistik deskriptif per kelas
print("=== Statistik Deskriptif per Species ===")
data.groupby('species_name')[iris.feature_names].mean().round(2)
```

```python
# Visualisasi distribusi fitur per kelas
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
for i, col in enumerate(iris.feature_names):
    ax = axes[i // 2, i % 2]
    for species in ['setosa', 'versicolor', 'virginica']:
        subset = data[data['species_name'] == species][col]
        ax.hist(subset, bins=15, alpha=0.5, label=species)
    ax.set_xlabel(col)
    ax.set_ylabel('Frekuensi')
    ax.set_title(f'Distribusi {col}')
    ax.legend()

plt.suptitle('Distribusi Fitur per Species', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

```python
# Scatter plot: 2 fitur utama
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Petal length vs petal width
scatter1 = axes[0].scatter(
    data['petal length (cm)'], data['petal width (cm)'],
    c=data['species'], cmap='Set1', s=60, alpha=0.7
)
axes[0].set_xlabel('Petal Length (cm)')
axes[0].set_ylabel('Petal Width (cm)')
axes[0].set_title('Petal Length vs Petal Width')

# Sepal length vs sepal width
scatter2 = axes[1].scatter(
    data['sepal length (cm)'], data['sepal width (cm)'],
    c=data['species'], cmap='Set1', s=60, alpha=0.7
)
axes[1].set_xlabel('Sepal Length (cm)')
axes[1].set_ylabel('Sepal Width (cm)')
axes[1].set_title('Sepal Length vs Sepal Width')

plt.tight_layout()
plt.show()
```

### Langkah 2: Mempersiapkan Data (Train/Test Split)

```python
# Tentukan fitur (X) dan target (y)
X = data[iris.feature_names]
y = data['species']

# Split data: 70% training, 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print(f"=== Pembagian Data ===")
print(f"Total data    : {len(X)}")
print(f"Data training : {len(X_train)} ({len(X_train)/len(X)*100:.0f}%)")
print(f"Data testing  : {len(X_test)} ({len(X_test)/len(X)*100:.0f}%)")
print()

# Cek distribusi kelas di training dan testing
print("Distribusi kelas:")
print(f"  Training: {np.bincount(y_train).tolist()}")
print(f"  Testing : {np.bincount(y_test).tolist()}")
print("  (stratify=y memastikan proporsi kelas seimbang)")
```

### Langkah 3: Model 1 — Decision Tree

```python
# Bangun model Decision Tree
dt_model = DecisionTreeClassifier(
    max_depth=3,          # batasi kedalaman agar mudah divisualisasi
    random_state=42
)
dt_model.fit(X_train, y_train)

# Prediksi
y_pred_dt = dt_model.predict(X_test)

# Evaluasi
acc_dt = accuracy_score(y_test, y_pred_dt)
print(f"=== Decision Tree — Hasil ===")
print(f"Akurasi: {acc_dt:.4f} ({acc_dt*100:.1f}%)")
print()
print("Classification Report:")
print(classification_report(y_test, y_pred_dt,
                            target_names=iris.target_names))
```

```python
# Visualisasi Decision Tree
plt.figure(figsize=(18, 10))
plot_tree(
    dt_model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True,
    fontsize=11
)
plt.title('Visualisasi Decision Tree (max_depth=3)', fontsize=14)
plt.tight_layout()
plt.show()
```

```python
# Confusion Matrix — Decision Tree
fig, ax = plt.subplots(figsize=(8, 6))
cm_dt = confusion_matrix(y_test, y_pred_dt)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm_dt,
    display_labels=iris.target_names
)
disp.plot(ax=ax, cmap='Blues')
ax.set_title('Confusion Matrix — Decision Tree')
plt.tight_layout()
plt.show()
```

```python
# Cara membaca Confusion Matrix
print("""
=== Cara Membaca Confusion Matrix ===

                    Prediksi
                 setosa  versi  virgi
Aktual setosa  [  TP   |  FP  |  FP  ]
       versi   [  FN   |  TP  |  FP  ]
       virgi   [  FN   |  FN  |  TP  ]

- Diagonal (TP): prediksi benar
- Di luar diagonal: prediksi salah

Metrik:
- Precision: TP / (TP + FP) — dari yang diprediksi positif, berapa yang benar?
- Recall   : TP / (TP + FN) — dari yang benar positif, berapa yang terdeteksi?
- F1-score : rata-rata harmonis precision dan recall
""")
```

### Langkah 4: Feature Importance — Decision Tree

```python
# Feature importance dari Decision Tree
importance = pd.DataFrame({
    'Fitur': iris.feature_names,
    'Importance': dt_model.feature_importances_
}).sort_values('Importance', ascending=True)

plt.figure(figsize=(10, 5))
plt.barh(importance['Fitur'], importance['Importance'], color='steelblue')
plt.xlabel('Feature Importance')
plt.title('Feature Importance — Decision Tree')
plt.tight_layout()
plt.show()

print("Fitur yang paling penting untuk klasifikasi:")
for _, row in importance.sort_values('Importance', ascending=False).iterrows():
    print(f"  {row['Fitur']:25s}: {row['Importance']:.4f}")
```

### Langkah 5: Model 2 — k-Nearest Neighbors (k-NN)

```python
# Standarisasi fitur (penting untuk k-NN karena berbasis jarak)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("=== Standarisasi Fitur ===")
print("k-NN menggunakan jarak antar titik data.")
print("Tanpa standarisasi, fitur dengan skala besar akan mendominasi.")
print()
print("Sebelum standarisasi (mean, std):")
for col in iris.feature_names:
    print(f"  {col}: mean={X_train[col].mean():.2f}, std={X_train[col].std():.2f}")
print()
print("Setelah standarisasi (mean ≈ 0, std ≈ 1):")
for i, col in enumerate(iris.feature_names):
    print(f"  {col}: mean={X_train_scaled[:, i].mean():.2f}, std={X_train_scaled[:, i].std():.2f}")
```

```python
# k-NN dengan k=5
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_scaled, y_train)

# Prediksi
y_pred_knn = knn_model.predict(X_test_scaled)

# Evaluasi
acc_knn = accuracy_score(y_test, y_pred_knn)
print(f"=== k-NN (k=5) — Hasil ===")
print(f"Akurasi: {acc_knn:.4f} ({acc_knn*100:.1f}%)")
print()
print("Classification Report:")
print(classification_report(y_test, y_pred_knn,
                            target_names=iris.target_names))
```

### Langkah 6: Eksperimen dengan Nilai k Berbeda

```python
# Coba berbagai nilai k
k_values = range(1, 21)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    acc = knn.score(X_test_scaled, y_test)
    accuracies.append(acc)

# Visualisasi
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracies, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Nilai k (jumlah tetangga)')
plt.ylabel('Akurasi')
plt.title('Pengaruh Nilai k terhadap Akurasi k-NN')
plt.xticks(k_values)
plt.grid(True, alpha=0.3)

# Tandai k terbaik
best_k = k_values[np.argmax(accuracies)]
best_acc = max(accuracies)
plt.axvline(x=best_k, color='red', linestyle='--', alpha=0.7,
            label=f'k terbaik = {best_k} (akurasi = {best_acc:.3f})')
plt.legend()
plt.tight_layout()
plt.show()

print(f"Nilai k terbaik: {best_k} dengan akurasi: {best_acc:.4f}")
```

```python
# Confusion Matrix — k-NN terbaik
knn_best = KNeighborsClassifier(n_neighbors=best_k)
knn_best.fit(X_train_scaled, y_train)
y_pred_knn_best = knn_best.predict(X_test_scaled)

fig, ax = plt.subplots(figsize=(8, 6))
cm_knn = confusion_matrix(y_test, y_pred_knn_best)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm_knn,
    display_labels=iris.target_names
)
disp.plot(ax=ax, cmap='Greens')
ax.set_title(f'Confusion Matrix — k-NN (k={best_k})')
plt.tight_layout()
plt.show()
```

### Langkah 7: Perbandingan Model

```python
# Tabel perbandingan
from sklearn.metrics import precision_score, recall_score, f1_score

models = {
    'Decision Tree': (y_pred_dt, acc_dt),
    f'k-NN (k={best_k})': (y_pred_knn_best, accuracy_score(y_test, y_pred_knn_best))
}

print("=== Perbandingan Model ===")
print(f"{'Model':<20} {'Accuracy':>10} {'Precision':>10} {'Recall':>10} {'F1-Score':>10}")
print("-" * 62)

for name, (preds, acc) in models.items():
    prec = precision_score(y_test, preds, average='weighted')
    rec = recall_score(y_test, preds, average='weighted')
    f1 = f1_score(y_test, preds, average='weighted')
    print(f"{name:<20} {acc:>10.4f} {prec:>10.4f} {rec:>10.4f} {f1:>10.4f}")
```

```python
# Visualisasi perbandingan
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
dt_scores = [
    acc_dt,
    precision_score(y_test, y_pred_dt, average='weighted'),
    recall_score(y_test, y_pred_dt, average='weighted'),
    f1_score(y_test, y_pred_dt, average='weighted')
]
knn_scores = [
    accuracy_score(y_test, y_pred_knn_best),
    precision_score(y_test, y_pred_knn_best, average='weighted'),
    recall_score(y_test, y_pred_knn_best, average='weighted'),
    f1_score(y_test, y_pred_knn_best, average='weighted')
]

x = np.arange(len(metrics))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, dt_scores, width, label='Decision Tree', color='steelblue')
bars2 = ax.bar(x + width/2, knn_scores, width, label=f'k-NN (k={best_k})', color='coral')

ax.set_xlabel('Metrik')
ax.set_ylabel('Skor')
ax.set_title('Perbandingan Performa: Decision Tree vs k-NN')
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()
ax.set_ylim(0, 1.1)

# Tambahkan label nilai
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.01,
            f'{bar.get_height():.3f}', ha='center', va='bottom', fontsize=9)
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.01,
            f'{bar.get_height():.3f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()
```

### Langkah 8: Cross-Validation

```python
# Cross-validation: evaluasi yang lebih robust
print("=== Cross-Validation (5-Fold) ===")
print()
print("Cross-validation membagi data menjadi k bagian (fold),")
print("melatih model pada k-1 fold dan menguji pada 1 fold sisanya,")
print("diulang k kali sehingga setiap fold menjadi test set tepat sekali.")
print()

# Decision Tree
cv_dt = cross_val_score(
    DecisionTreeClassifier(max_depth=3, random_state=42),
    X, y, cv=5, scoring='accuracy'
)

# k-NN (perlu standarisasi dalam pipeline)
from sklearn.pipeline import Pipeline

knn_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=best_k))
])
cv_knn = cross_val_score(knn_pipeline, X, y, cv=5, scoring='accuracy')

print(f"Decision Tree:")
print(f"  Skor per fold: {cv_dt.round(4)}")
print(f"  Mean ± Std   : {cv_dt.mean():.4f} ± {cv_dt.std():.4f}")
print()
print(f"k-NN (k={best_k}):")
print(f"  Skor per fold: {cv_knn.round(4)}")
print(f"  Mean ± Std   : {cv_knn.mean():.4f} ± {cv_knn.std():.4f}")
```

```python
# Visualisasi cross-validation
fig, ax = plt.subplots(figsize=(10, 6))

positions_dt = np.arange(1, 6) - 0.15
positions_knn = np.arange(1, 6) + 0.15

ax.bar(positions_dt, cv_dt, width=0.25, label='Decision Tree', color='steelblue', alpha=0.8)
ax.bar(positions_knn, cv_knn, width=0.25, label=f'k-NN (k={best_k})', color='coral', alpha=0.8)

ax.axhline(y=cv_dt.mean(), color='steelblue', linestyle='--', alpha=0.5,
           label=f'DT mean = {cv_dt.mean():.3f}')
ax.axhline(y=cv_knn.mean(), color='coral', linestyle='--', alpha=0.5,
           label=f'k-NN mean = {cv_knn.mean():.3f}')

ax.set_xlabel('Fold')
ax.set_ylabel('Akurasi')
ax.set_title('Cross-Validation: Akurasi per Fold')
ax.set_xticks(range(1, 6))
ax.legend()
ax.set_ylim(0.8, 1.05)

plt.tight_layout()
plt.show()
```

### Langkah 9: Ringkasan dan Refleksi

```python
print("""
=== Ringkasan Lab 13 ===

1. ALUR KERJA ML:
   Data → Preprocessing → Split → Train → Evaluate → Predict

2. DECISION TREE:
   + Mudah diinterpretasi (bisa divisualisasi)
   + Tidak perlu standarisasi fitur
   - Rentan overfitting jika tidak dibatasi (max_depth)

3. k-NN:
   + Sederhana, mudah dipahami
   + Tidak ada fase "training" yang kompleks
   - Perlu standarisasi fitur (berbasis jarak)
   - Lambat untuk dataset besar

4. EVALUASI MODEL:
   - Accuracy: proporsi prediksi benar secara keseluruhan
   - Precision: dari yang diprediksi positif, berapa yang benar?
   - Recall: dari yang benar positif, berapa yang terdeteksi?
   - F1-Score: rata-rata harmonis precision dan recall
   - Cross-validation: evaluasi lebih stabil (mengurangi bias dari satu kali split)

5. TIPS MEMILIH MODEL:
   - Tidak ada model "terbaik" untuk semua kasus
   - Selalu bandingkan beberapa model
   - Gunakan cross-validation untuk evaluasi yang fair
   - Pertimbangkan trade-off antara akurasi dan interpretabilitas
""")
```

---

## Tugas yang Harus Dikumpulkan

Buat notebook Google Colab yang berisi:

1. **Load Dataset** (10 poin)
   - Gunakan dataset dari `sklearn.datasets` (contoh: `load_wine`, `load_breast_cancer`) atau dataset lain
   - Tampilkan eksplorasi data (statistik deskriptif, visualisasi)

2. **Preprocessing dan Split** (15 poin)
   - Lakukan `train_test_split` dengan `stratify`
   - Jelaskan mengapa `stratify` penting

3. **Decision Tree** (20 poin)
   - Bangun model Decision Tree
   - Visualisasikan tree dengan `plot_tree`
   - Tampilkan feature importance

4. **k-NN** (20 poin)
   - Bangun model k-NN (jangan lupa standarisasi)
   - Eksperimen dengan minimal 5 nilai k berbeda
   - Visualisasikan pengaruh k terhadap akurasi

5. **Evaluasi dan Perbandingan** (25 poin)
   - Tampilkan confusion matrix dan classification report untuk kedua model
   - Bandingkan performa dengan tabel dan grafik
   - Lakukan 5-fold cross-validation
   - Model mana yang lebih baik untuk dataset Anda? Mengapa?

6. **Kesimpulan** (10 poin)
   - Tuliskan kesimpulan dan refleksi

**Format:** File `.ipynb` diunggah ke Google Classroom
**Deadline:** Satu minggu setelah pertemuan praktikum

---

## Challenge / Bonus

1. **Tambahkan model ketiga**: Coba `GaussianNB` (Naive Bayes) dari sklearn dan bandingkan dengan Decision Tree dan k-NN.

2. **Hyperparameter tuning**: Gunakan `GridSearchCV` untuk menemukan kombinasi hyperparameter terbaik:
   ```python
   from sklearn.model_selection import GridSearchCV

   param_grid = {
       'max_depth': [2, 3, 4, 5, None],
       'min_samples_split': [2, 5, 10],
       'min_samples_leaf': [1, 2, 4]
   }
   grid_search = GridSearchCV(DecisionTreeClassifier(random_state=42),
                               param_grid, cv=5, scoring='accuracy')
   grid_search.fit(X_train, y_train)
   print(f"Best params: {grid_search.best_params_}")
   print(f"Best score: {grid_search.best_score_:.4f}")
   ```

3. **Decision Boundary Plot**: Buat visualisasi decision boundary menggunakan 2 fitur terbaik untuk membandingkan bagaimana Decision Tree dan k-NN memisahkan kelas.
