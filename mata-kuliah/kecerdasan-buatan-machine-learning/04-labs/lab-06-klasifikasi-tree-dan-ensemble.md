# Lab 06: Klasifikasi dengan Tree dan Ensemble

**Mata Kuliah:** Kecerdasan Buatan dan Machine Learning
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Minggu:** 6
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

- Membangun model DecisionTreeClassifier dan mengevaluasi performanya
- Memvisualisasikan pohon keputusan menggunakan plot_tree
- Menganalisis feature importance dari model decision tree
- Mendemonstrasikan dan memahami fenomena overfitting
- Membangun model RandomForestClassifier sebagai ensemble method
- Membandingkan performa single tree vs random forest
- Melakukan hyperparameter tuning menggunakan GridSearchCV

---

## Persiapan

1. Buka Google Colab dan buat notebook baru
2. Nama file: `Lab06_NamaAnda_NIM.ipynb`
3. Pastikan library pandas, numpy, matplotlib, seaborn, dan scikit-learn sudah tersedia
4. Pahami konsep dasar decision tree dari kuliah teori

---

## Langkah-langkah

### Langkah 1: DecisionTreeClassifier - Fit, Predict, Score

```python
# =============================================
# LANGKAH 1: DecisionTreeClassifier
# =============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Pengaturan tampilan
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)
np.random.seed(42)

print("=" * 60)
print("DECISION TREE - PREDIKSI CHURN NASABAH BANK")
print("=" * 60)

# --- Buat Dataset Simulasi Churn Nasabah Bank Indonesia ---
n = 800

data_bank = {
    'usia': np.random.normal(40, 12, n).clip(18, 70).astype(int),
    'saldo_juta': np.round(np.random.lognormal(mean=2.5, sigma=1.0, size=n), 2),
    'jumlah_produk': np.random.choice([1, 2, 3, 4], n, p=[0.45, 0.35, 0.15, 0.05]),
    'lama_nasabah_tahun': np.random.choice(range(1, 16), n),
    'memiliki_kartu_kredit': np.random.choice([0, 1], n, p=[0.30, 0.70]),
    'nasabah_aktif': np.random.choice([0, 1], n, p=[0.45, 0.55]),
    'gaji_juta': np.round(np.random.lognormal(mean=2.0, sigma=0.7, size=n), 2),
    'kota': np.random.choice(
        ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Semarang'],
        n, p=[0.30, 0.20, 0.20, 0.15, 0.15]
    ),
}

df = pd.DataFrame(data_bank)

# Generate target (churn)
logit = (-2 + 0.02 * df['usia'] - 0.05 * df['saldo_juta']
         + 0.5 * df['jumlah_produk'] - 0.15 * df['lama_nasabah_tahun']
         - 0.8 * df['nasabah_aktif'] + np.random.normal(0, 0.5, n))
prob = 1 / (1 + np.exp(-logit))
df['churn'] = (prob > 0.5).astype(int)

print(f"Dataset Bank: {df.shape[0]} baris x {df.shape[1]} kolom")
print(f"\nDistribusi Churn:")
print(df['churn'].value_counts())
print(f"Rasio churn: {df['churn'].mean()*100:.1f}%")

# --- Encoding dan Persiapan Data ---
le = LabelEncoder()
df['kota_encoded'] = le.fit_transform(df['kota'])

fitur_cols = ['usia', 'saldo_juta', 'jumlah_produk', 'lama_nasabah_tahun',
              'memiliki_kartu_kredit', 'nasabah_aktif', 'gaji_juta', 'kota_encoded']

X = df[fitur_cols].values
y = df['churn'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTraining: {X_train.shape[0]} sampel")
print(f"Testing : {X_test.shape[0]} sampel")

# --- Fit Decision Tree ---
dt_model = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_model.fit(X_train, y_train)

y_pred_dt = dt_model.predict(X_test)
akurasi_dt = accuracy_score(y_test, y_pred_dt)

print(f"\n--- Hasil Decision Tree (max_depth=5) ---")
print(f"Akurasi: {akurasi_dt:.4f} ({akurasi_dt*100:.1f}%)")
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred_dt, target_names=['Tidak Churn', 'Churn']))
```

### Langkah 2: Visualisasi Pohon Keputusan

```python
# =============================================
# LANGKAH 2: Visualisasi Pohon Keputusan
# =============================================

# --- Plot Pohon Keputusan ---
fig, ax = plt.subplots(figsize=(24, 10))
plot_tree(dt_model,
          feature_names=fitur_cols,
          class_names=['Tidak Churn', 'Churn'],
          filled=True,
          rounded=True,
          fontsize=8,
          max_depth=3,  # Batasi tampilan agar mudah dibaca
          ax=ax)
ax.set_title('Visualisasi Decision Tree (max_depth=3 ditampilkan)', fontsize=16)
plt.tight_layout()
plt.show()

# --- Pohon keputusan sederhana (depth=2) untuk pemahaman ---
dt_simple = DecisionTreeClassifier(max_depth=2, random_state=42)
dt_simple.fit(X_train, y_train)

fig, ax = plt.subplots(figsize=(16, 6))
plot_tree(dt_simple,
          feature_names=fitur_cols,
          class_names=['Tidak Churn', 'Churn'],
          filled=True,
          rounded=True,
          fontsize=10,
          ax=ax)
ax.set_title('Decision Tree Sederhana (max_depth=2)', fontsize=16)
plt.tight_layout()
plt.show()

print(f"Akurasi tree sederhana (depth=2): {dt_simple.score(X_test, y_test):.4f}")
print(f"Akurasi tree (depth=5)          : {akurasi_dt:.4f}")
```

### Langkah 3: Feature Importance

```python
# =============================================
# LANGKAH 3: Feature Importance
# =============================================

print("=" * 60)
print("FEATURE IMPORTANCE")
print("=" * 60)

importances = dt_model.feature_importances_

# Buat DataFrame importance
df_importance = pd.DataFrame({
    'Fitur': fitur_cols,
    'Importance': importances
}).sort_values('Importance', ascending=True)

print("Feature Importance (Decision Tree):")
for _, row in df_importance.iterrows():
    bar = '#' * int(row['Importance'] * 50)
    print(f"  {row['Fitur']:30s}: {row['Importance']:.4f} {bar}")

# --- Visualisasi ---
fig, ax = plt.subplots(figsize=(10, 6))
colors = plt.cm.RdYlBu_r(np.linspace(0.2, 0.8, len(df_importance)))
df_importance.plot(kind='barh', x='Fitur', y='Importance', ax=ax,
                   color=colors, edgecolor='white', legend=False)
ax.set_xlabel('Importance Score', fontsize=12)
ax.set_title('Feature Importance - Decision Tree', fontsize=14)
ax.grid(axis='x', alpha=0.3)

# Tambahkan nilai di samping bar
for i, (_, row) in enumerate(df_importance.iterrows()):
    ax.text(row['Importance'] + 0.005, i, f'{row["Importance"]:.3f}', va='center', fontsize=10)

plt.tight_layout()
plt.show()

print(f"\nFitur paling penting: {df_importance.iloc[-1]['Fitur']} ({df_importance.iloc[-1]['Importance']:.4f})")
print(f"Fitur paling tidak penting: {df_importance.iloc[0]['Fitur']} ({df_importance.iloc[0]['Importance']:.4f})")
```

### Langkah 4: Demonstrasi Overfitting

```python
# =============================================
# LANGKAH 4: Demonstrasi Overfitting
# =============================================

print("=" * 60)
print("DEMONSTRASI OVERFITTING: VARIASI MAX_DEPTH")
print("=" * 60)

depths = range(1, 21)
train_scores = []
test_scores = []

for depth in depths:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_train, y_train)
    train_scores.append(dt.score(X_train, y_train))
    test_scores.append(dt.score(X_test, y_test))

# Tampilkan tabel
print(f"\n{'Depth':>6} {'Train Acc':>12} {'Test Acc':>12} {'Gap':>10}")
print("-" * 42)
for d, tr, te in zip(depths, train_scores, test_scores):
    gap = tr - te
    marker = " <-- overfitting" if gap > 0.10 else ""
    print(f"{d:>6} {tr:>12.4f} {te:>12.4f} {gap:>10.4f}{marker}")

# --- Visualisasi ---
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(depths, train_scores, 'b-o', linewidth=2, markersize=6, label='Training Accuracy')
ax.plot(depths, test_scores, 'r-o', linewidth=2, markersize=6, label='Testing Accuracy')

# Tandai depth optimal
best_depth = depths[np.argmax(test_scores)]
best_score = max(test_scores)
ax.axvline(x=best_depth, color='green', linestyle='--', alpha=0.5,
           label=f'Best depth = {best_depth} (test acc = {best_score:.3f})')

# Zona overfitting
ax.fill_between(depths, train_scores, test_scores, alpha=0.15, color='red')

ax.set_xlabel('Max Depth', fontsize=12)
ax.set_ylabel('Accuracy', fontsize=12)
ax.set_title('Overfitting: Training vs Testing Accuracy', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_xticks(depths)

plt.tight_layout()
plt.show()

print(f"""
Observasi:
- Depth rendah (1-3): Underfitting - model terlalu sederhana
- Depth optimal ({best_depth}): Keseimbangan bias-variance
- Depth tinggi (>10): Overfitting - training tinggi, testing rendah
- Gap (train-test) membesar seiring depth → tanda overfitting
""")
```

### Langkah 5: RandomForestClassifier

```python
# =============================================
# LANGKAH 5: Random Forest Classifier
# =============================================

print("=" * 60)
print("RANDOM FOREST CLASSIFIER")
print("=" * 60)

# --- Fit Random Forest ---
rf_model = RandomForestClassifier(
    n_estimators=100,      # Jumlah pohon
    max_depth=7,           # Kedalaman maksimal tiap pohon
    random_state=42,
    n_jobs=-1              # Gunakan semua CPU
)
rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)
akurasi_rf = accuracy_score(y_test, y_pred_rf)

print(f"Random Forest (100 trees, max_depth=7)")
print(f"Akurasi: {akurasi_rf:.4f} ({akurasi_rf*100:.1f}%)")
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred_rf, target_names=['Tidak Churn', 'Churn']))

# --- Feature Importance dari Random Forest ---
rf_importances = rf_model.feature_importances_
df_rf_imp = pd.DataFrame({
    'Fitur': fitur_cols,
    'DT_Importance': importances,
    'RF_Importance': rf_importances
}).sort_values('RF_Importance', ascending=True)

print("\nPerbandingan Feature Importance:")
print(df_rf_imp.round(4))

# --- Visualisasi Feature Importance: DT vs RF ---
fig, ax = plt.subplots(figsize=(12, 6))

x_pos = np.arange(len(fitur_cols))
width = 0.35

bars1 = ax.barh(x_pos - width/2, df_rf_imp['DT_Importance'], width,
                label='Decision Tree', color='steelblue', edgecolor='white')
bars2 = ax.barh(x_pos + width/2, df_rf_imp['RF_Importance'], width,
                label='Random Forest', color='coral', edgecolor='white')

ax.set_yticks(x_pos)
ax.set_yticklabels(df_rf_imp['Fitur'])
ax.set_xlabel('Importance Score', fontsize=12)
ax.set_title('Feature Importance: Decision Tree vs Random Forest', fontsize=14)
ax.legend(fontsize=11)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.show()
```

### Langkah 6: Perbandingan Single Tree vs Random Forest

```python
# =============================================
# LANGKAH 6: Perbandingan DT vs RF
# =============================================

print("=" * 60)
print("PERBANDINGAN: SINGLE TREE vs RANDOM FOREST")
print("=" * 60)

# Cross-validation untuk perbandingan yang lebih fair
from sklearn.model_selection import cross_val_score

dt_cv = cross_val_score(
    DecisionTreeClassifier(max_depth=5, random_state=42),
    X, y, cv=5, scoring='accuracy'
)

rf_cv = cross_val_score(
    RandomForestClassifier(n_estimators=100, max_depth=7, random_state=42),
    X, y, cv=5, scoring='accuracy'
)

print(f"Decision Tree (5-fold CV):")
print(f"  Scores  : {dt_cv.round(4)}")
print(f"  Mean    : {dt_cv.mean():.4f} +/- {dt_cv.std():.4f}")

print(f"\nRandom Forest (5-fold CV):")
print(f"  Scores  : {rf_cv.round(4)}")
print(f"  Mean    : {rf_cv.mean():.4f} +/- {rf_cv.std():.4f}")

print(f"\nPeningkatan RF vs DT: +{(rf_cv.mean() - dt_cv.mean())*100:.2f}%")

# --- Efek jumlah pohon pada Random Forest ---
n_trees_list = [1, 5, 10, 25, 50, 100, 200, 300]
rf_scores_train = []
rf_scores_test = []

for n_trees in n_trees_list:
    rf = RandomForestClassifier(n_estimators=n_trees, max_depth=7, random_state=42)
    rf.fit(X_train, y_train)
    rf_scores_train.append(rf.score(X_train, y_train))
    rf_scores_test.append(rf.score(X_test, y_test))

# --- Visualisasi ---
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Perbandingan CV scores
ax = axes[0]
models = ['Decision\nTree', 'Random\nForest']
means = [dt_cv.mean(), rf_cv.mean()]
stds = [dt_cv.std(), rf_cv.std()]
colors = ['steelblue', 'coral']

bars = ax.bar(models, means, yerr=stds, capsize=10, color=colors,
              edgecolor='white', alpha=0.8)
for bar, mean in zip(bars, means):
    ax.text(bar.get_x() + bar.get_width()/2., mean + 0.005,
            f'{mean:.3f}', ha='center', va='bottom', fontsize=12, fontweight='bold')

ax.set_ylabel('Accuracy', fontsize=12)
ax.set_title('Cross-Validation Accuracy', fontsize=13)
ax.set_ylim(0.5, 1.0)
ax.grid(axis='y', alpha=0.3)

# Plot 2: Efek jumlah pohon
ax = axes[1]
ax.plot(n_trees_list, rf_scores_train, 'b-o', label='Training', linewidth=2)
ax.plot(n_trees_list, rf_scores_test, 'r-o', label='Testing', linewidth=2)
ax.set_xlabel('Jumlah Pohon (n_estimators)', fontsize=12)
ax.set_ylabel('Accuracy', fontsize=12)
ax.set_title('Efek Jumlah Pohon pada Random Forest', fontsize=13)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### Langkah 7: Hyperparameter Tuning dengan GridSearchCV

```python
# =============================================
# LANGKAH 7: Hyperparameter Tuning (GridSearchCV)
# =============================================

print("=" * 60)
print("HYPERPARAMETER TUNING - GridSearchCV")
print("=" * 60)

# --- Parameter Grid untuk Random Forest ---
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
}

total_kombinasi = 1
for values in param_grid.values():
    total_kombinasi *= len(values)
print(f"Total kombinasi parameter: {total_kombinasi}")
print(f"Dengan 5-fold CV: {total_kombinasi * 5} model dilatih")

# --- Jalankan GridSearchCV ---
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=0
)

print("\nMenjalankan GridSearchCV...")
grid_search.fit(X_train, y_train)

# --- Hasil ---
print(f"\nBest Parameters: {grid_search.best_params_}")
print(f"Best CV Score  : {grid_search.best_score_:.4f}")

best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test)
akurasi_best = accuracy_score(y_test, y_pred_best)

print(f"Test Accuracy  : {akurasi_best:.4f}")

# --- Perbandingan Semua Model ---
print(f"\n{'=' * 60}")
print(f"RINGKASAN PERBANDINGAN MODEL")
print(f"{'=' * 60}")

print(f"{'Model':<35} {'Accuracy':>10}")
print(f"{'-'*45}")
print(f"{'Decision Tree (depth=5)':<35} {accuracy_score(y_test, y_pred_dt):>10.4f}")
print(f"{'Random Forest (default)':<35} {akurasi_rf:>10.4f}")
print(f"{'Random Forest (tuned)':<35} {akurasi_best:>10.4f}")

# --- Top 10 kombinasi parameter ---
results = pd.DataFrame(grid_search.cv_results_)
top10 = results.nsmallest(10, 'rank_test_score')[
    ['params', 'mean_test_score', 'std_test_score', 'rank_test_score']
]
print(f"\nTop 10 Kombinasi Parameter:")
for _, row in top10.iterrows():
    print(f"  Rank {row['rank_test_score']:.0f}: {row['mean_test_score']:.4f} +/- {row['std_test_score']:.4f} | {row['params']}")

# --- Confusion Matrix Model Terbaik ---
cm_best = confusion_matrix(y_test, y_pred_best)

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(cm_best, annot=True, fmt='d', cmap='Blues', ax=ax,
            xticklabels=['Tidak Churn', 'Churn'],
            yticklabels=['Tidak Churn', 'Churn'])
ax.set_xlabel('Prediksi', fontsize=12)
ax.set_ylabel('Aktual', fontsize=12)
ax.set_title(f'Confusion Matrix - Best Random Forest\nAkurasi: {akurasi_best:.2%}', fontsize=14)
plt.tight_layout()
plt.show()

print(f"\nClassification Report (Best Model):")
print(classification_report(y_test, y_pred_best, target_names=['Tidak Churn', 'Churn']))
```

---

## Tantangan Tambahan

1. **Dataset Performa Mahasiswa:** Buat dataset simulasi performa mahasiswa UAI (IPK, kehadiran, tugas, ujian) dan prediksi apakah mahasiswa akan lulus tepat waktu. Gunakan Decision Tree dan Random Forest, lalu bandingkan hasilnya.

2. **Gradient Boosting:** Implementasikan `GradientBoostingClassifier` dari sklearn pada dataset churn nasabah. Bandingkan performanya dengan Random Forest. Eksperimen dengan `learning_rate` dan `n_estimators`.

3. **Pruning Manual:** Buat Decision Tree tanpa batasan depth. Kemudian lakukan cost complexity pruning menggunakan `ccp_alpha`. Plot performa training dan testing untuk berbagai nilai `ccp_alpha` dan temukan nilai optimal.

---

## Checklist Penyelesaian

- [ ] DecisionTreeClassifier berhasil dibangun dan dievaluasi
- [ ] Pohon keputusan berhasil divisualisasikan dengan plot_tree
- [ ] Feature importance berhasil dihitung dan divisualisasikan
- [ ] Overfitting berhasil didemonstrasikan dengan variasi max_depth
- [ ] RandomForestClassifier berhasil dibangun dan dievaluasi
- [ ] Perbandingan single tree vs random forest berhasil dilakukan
- [ ] Hyperparameter tuning dengan GridSearchCV berhasil dijalankan
- [ ] Notebook disimpan dengan nama `Lab06_NamaAnda_NIM.ipynb`
- [ ] Minimal 1 tantangan tambahan diselesaikan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
