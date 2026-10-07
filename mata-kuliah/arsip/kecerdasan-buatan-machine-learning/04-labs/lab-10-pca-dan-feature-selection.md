# Lab 10: PCA dan Feature Selection

**Mata Kuliah:** Kecerdasan Buatan dan Machine Learning
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Minggu:** 10
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

- Menerapkan Principal Component Analysis (PCA) untuk reduksi dimensi
- Membuat dan menginterpretasi scree plot dari explained variance
- Memvisualisasikan data berdimensi tinggi dalam 2D menggunakan PCA
- Menggunakan SelectKBest untuk seleksi fitur berbasis statistik
- Menerapkan Recursive Feature Elimination (RFE) untuk seleksi fitur
- Mengekstrak feature importance dari model Random Forest
- Membandingkan akurasi model dengan berbagai strategi seleksi fitur

---

## Persiapan

1. Buka Google Colab notebook baru
2. Nama file: `Lab10_NamaAnda_NIM.ipynb`
3. Pastikan library `scikit-learn`, `matplotlib`, `numpy`, dan `pandas` sudah bisa diimpor

---

## Langkah-langkah

### Langkah 1: PCA pada Dataset Iris

```python
# =============================================
# LANGKAH 1: PCA pada Dataset Iris
# =============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Muat dataset Iris
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

print("=== DATASET IRIS ===")
print(f"Jumlah sampel: {X.shape[0]}")
print(f"Jumlah fitur: {X.shape[1]}")
print(f"Fitur: {feature_names}")
print(f"Kelas: {target_names}")

# Standardisasi data (penting sebelum PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Terapkan PCA — pertahankan semua komponen
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

# Explained Variance Ratio
print("\n=== EXPLAINED VARIANCE RATIO ===")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"  PC{i+1}: {var:.4f} ({var*100:.2f}%)")
print(f"  Total (semua PC): {sum(pca.explained_variance_ratio_)*100:.2f}%")
print(f"  Total (PC1+PC2) : {sum(pca.explained_variance_ratio_[:2])*100:.2f}%")
```

### Langkah 2: Scree Plot

```python
# =============================================
# LANGKAH 2: Scree Plot
# =============================================

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Explained variance per komponen
axes[0].bar(range(1, len(pca.explained_variance_ratio_) + 1),
            pca.explained_variance_ratio_, color='steelblue',
            edgecolor='white', alpha=0.8)
axes[0].set_xlabel('Principal Component')
axes[0].set_ylabel('Explained Variance Ratio')
axes[0].set_title('Scree Plot — Variance per Komponen')
axes[0].set_xticks(range(1, len(pca.explained_variance_ratio_) + 1))
axes[0].grid(axis='y', alpha=0.3)

# Plot 2: Cumulative explained variance
cumulative_var = np.cumsum(pca.explained_variance_ratio_)
axes[1].plot(range(1, len(cumulative_var) + 1), cumulative_var,
             'ro-', linewidth=2, markersize=8)
axes[1].axhline(y=0.95, color='gray', linestyle='--', label='95% threshold')
axes[1].set_xlabel('Jumlah Komponen')
axes[1].set_ylabel('Cumulative Explained Variance')
axes[1].set_title('Cumulative Explained Variance')
axes[1].set_xticks(range(1, len(cumulative_var) + 1))
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Untuk mencapai 95% variance, dibutuhkan minimal "
      f"{np.argmax(cumulative_var >= 0.95) + 1} komponen.")
```

### Langkah 3: Visualisasi 2D dengan PCA

```python
# =============================================
# LANGKAH 3: Visualisasi 2D dengan PCA
# =============================================

# Gunakan 2 komponen utama
pca_2d = PCA(n_components=2)
X_2d = pca_2d.fit_transform(X_scaled)

plt.figure(figsize=(10, 7))
colors = ['#e74c3c', '#3498db', '#2ecc71']

for i, (name, color) in enumerate(zip(target_names, colors)):
    mask = y == i
    plt.scatter(X_2d[mask, 0], X_2d[mask, 1], c=color,
                label=name, alpha=0.7, s=60, edgecolors='white')

plt.xlabel(f'PC1 ({pca_2d.explained_variance_ratio_[0]*100:.1f}% variance)')
plt.ylabel(f'PC2 ({pca_2d.explained_variance_ratio_[1]*100:.1f}% variance)')
plt.title('Iris Dataset — Proyeksi PCA 2D')
plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Tampilkan loading (kontribusi fitur ke setiap PC)
print("=== PCA LOADINGS (Kontribusi Fitur) ===")
loadings = pd.DataFrame(
    pca_2d.components_.T,
    columns=['PC1', 'PC2'],
    index=feature_names
)
print(loadings.round(4))
print("\nInterpretasi: Nilai absolut besar menunjukkan fitur dominan pada PC tersebut.")
```

### Langkah 4: Feature Selection dengan SelectKBest

```python
# =============================================
# LANGKAH 4: SelectKBest (f_classif & chi2)
# =============================================

from sklearn.feature_selection import SelectKBest, f_classif, chi2

# --- Metode 1: f_classif (ANOVA F-value) ---
selector_f = SelectKBest(score_func=f_classif, k='all')
selector_f.fit(X_scaled, y)

print("=== FEATURE SELECTION: f_classif (ANOVA) ===")
f_scores = pd.DataFrame({
    'Fitur': feature_names,
    'F-Score': selector_f.scores_,
    'p-value': selector_f.pvalues_
}).sort_values('F-Score', ascending=False)
print(f_scores.to_string(index=False))

# --- Metode 2: chi2 (hanya untuk data non-negatif) ---
from sklearn.preprocessing import MinMaxScaler
X_minmax = MinMaxScaler().fit_transform(X)  # chi2 butuh non-negatif

selector_chi = SelectKBest(score_func=chi2, k='all')
selector_chi.fit(X_minmax, y)

print("\n=== FEATURE SELECTION: chi2 ===")
chi_scores = pd.DataFrame({
    'Fitur': feature_names,
    'Chi2-Score': selector_chi.scores_,
    'p-value': selector_chi.pvalues_
}).sort_values('Chi2-Score', ascending=False)
print(chi_scores.to_string(index=False))

# Visualisasi perbandingan skor
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].barh(f_scores['Fitur'], f_scores['F-Score'], color='steelblue')
axes[0].set_xlabel('F-Score')
axes[0].set_title('Feature Ranking — ANOVA F-test')

axes[1].barh(chi_scores['Fitur'], chi_scores['Chi2-Score'], color='coral')
axes[1].set_xlabel('Chi2 Score')
axes[1].set_title('Feature Ranking — Chi-Square Test')

plt.tight_layout()
plt.show()
```

### Langkah 5: Recursive Feature Elimination (RFE)

```python
# =============================================
# LANGKAH 5: Recursive Feature Elimination (RFE)
# =============================================

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

# Gunakan Random Forest sebagai estimator
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# RFE: pilih 2 fitur terbaik
rfe = RFE(estimator=rf, n_features_to_select=2, step=1)
rfe.fit(X_scaled, y)

print("=== RECURSIVE FEATURE ELIMINATION (RFE) ===")
print(f"Estimator: Random Forest")
print(f"Jumlah fitur yang dipilih: 2\n")

rfe_result = pd.DataFrame({
    'Fitur': feature_names,
    'Terpilih': rfe.support_,
    'Ranking': rfe.ranking_
}).sort_values('Ranking')
print(rfe_result.to_string(index=False))

print(f"\nFitur terpilih: {[f for f, s in zip(feature_names, rfe.support_) if s]}")
```

### Langkah 6: Feature Importance dari Random Forest

```python
# =============================================
# LANGKAH 6: Feature Importance (Random Forest)
# =============================================

# Latih Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_scaled, y)

# Ambil feature importance
importances = rf_model.feature_importances_
indices = np.argsort(importances)[::-1]

print("=== FEATURE IMPORTANCE (Random Forest) ===")
for i, idx in enumerate(indices):
    print(f"  {i+1}. {feature_names[idx]}: {importances[idx]:.4f}")

# Visualisasi
plt.figure(figsize=(8, 5))
plt.bar(range(len(importances)), importances[indices],
        color='steelblue', edgecolor='white')
plt.xticks(range(len(importances)),
           [feature_names[i] for i in indices], rotation=45, ha='right')
plt.ylabel('Importance')
plt.title('Feature Importance — Random Forest')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# Ringkasan semua metode
print("\n=== RINGKASAN RANKING FITUR ===")
summary = pd.DataFrame({
    'Fitur': feature_names,
    'ANOVA Rank': f_scores.reset_index(drop=True).index + 1,
    'Chi2 Rank': chi_scores.reset_index(drop=True).index + 1,
    'RFE Rank': rfe.ranking_,
    'RF Importance': importances
})
# Urutkan fitur berdasarkan nama agar konsisten
summary = summary.sort_values('Fitur')
print(summary.to_string(index=False))
```

### Langkah 7: Perbandingan Akurasi Model

```python
# =============================================
# LANGKAH 7: Perbandingan Akurasi
# =============================================

from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

print("=" * 60)
print("PERBANDINGAN AKURASI: Semua Fitur vs Seleksi vs PCA")
print("=" * 60)

model = SVC(kernel='rbf', random_state=42)

# 1. Semua fitur (4 fitur)
scores_all = cross_val_score(model, X_scaled, y, cv=5, scoring='accuracy')
print(f"\n1. Semua fitur (4 fitur):")
print(f"   Akurasi: {scores_all.mean():.4f} (+/- {scores_all.std():.4f})")

# 2. SelectKBest — 2 fitur terbaik (f_classif)
selector_2 = SelectKBest(score_func=f_classif, k=2)
X_selected = selector_2.fit_transform(X_scaled, y)
selected_names = [feature_names[i] for i in selector_2.get_support(indices=True)]
scores_selected = cross_val_score(model, X_selected, y, cv=5, scoring='accuracy')
print(f"\n2. SelectKBest — 2 fitur ({', '.join(selected_names)}):")
print(f"   Akurasi: {scores_selected.mean():.4f} (+/- {scores_selected.std():.4f})")

# 3. RFE — 2 fitur terbaik
X_rfe = X_scaled[:, rfe.support_]
rfe_names = [f for f, s in zip(feature_names, rfe.support_) if s]
scores_rfe = cross_val_score(model, X_rfe, y, cv=5, scoring='accuracy')
print(f"\n3. RFE — 2 fitur ({', '.join(rfe_names)}):")
print(f"   Akurasi: {scores_rfe.mean():.4f} (+/- {scores_rfe.std():.4f})")

# 4. PCA — 2 komponen
X_pca_2 = PCA(n_components=2).fit_transform(X_scaled)
scores_pca = cross_val_score(model, X_pca_2, y, cv=5, scoring='accuracy')
print(f"\n4. PCA — 2 komponen:")
print(f"   Akurasi: {scores_pca.mean():.4f} (+/- {scores_pca.std():.4f})")

# Visualisasi perbandingan
methods = ['Semua Fitur\n(4)', 'SelectKBest\n(2)', 'RFE\n(2)', 'PCA\n(2)']
means = [scores_all.mean(), scores_selected.mean(),
         scores_rfe.mean(), scores_pca.mean()]
stds = [scores_all.std(), scores_selected.std(),
        scores_rfe.std(), scores_pca.std()]

plt.figure(figsize=(8, 5))
bars = plt.bar(methods, means, yerr=stds, capsize=5,
               color=['steelblue', '#2ecc71', '#e74c3c', '#f39c12'],
               edgecolor='white')
plt.ylabel('Akurasi (5-Fold CV)')
plt.title('Perbandingan Akurasi — Semua Fitur vs Seleksi vs PCA')
plt.ylim(0.85, 1.01)
plt.grid(axis='y', alpha=0.3)

# Tambahkan label nilai
for bar, mean in zip(bars, means):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
             f'{mean:.3f}', ha='center', fontsize=11)

plt.tight_layout()
plt.show()

print("\nKesimpulan:")
print("- Reduksi dimensi (PCA/seleksi fitur) dapat mempertahankan akurasi")
print("- Dengan lebih sedikit fitur, model lebih cepat dan mengurangi overfitting")
print("- PCA menghasilkan komponen baru, sementara seleksi fitur mempertahankan fitur asli")
```

---

## Tantangan Tambahan

1. **PCA pada Dataset Lebih Besar:** Gunakan dataset `wine` dari scikit-learn (13 fitur). Terapkan PCA dan tentukan berapa komponen yang diperlukan untuk menangkap 95% variance. Bandingkan visualisasi 2D PCA dengan t-SNE (`sklearn.manifold.TSNE`).

2. **Feature Selection pada Dataset Diabetes:** Muat dataset `diabetes` dari scikit-learn. Bandingkan 3 metode seleksi fitur (SelectKBest, RFE, dan feature importance) untuk regresi (gunakan `f_regression` sebagai pengganti `f_classif`). Fitur mana yang konsisten penting di semua metode?

3. **Pengaruh Jumlah Fitur terhadap Akurasi:** Untuk dataset iris, buat plot akurasi (sumbu-y) vs jumlah fitur yang dipilih (sumbu-x, dari 1 sampai 4) menggunakan SelectKBest. Apakah selalu lebih banyak fitur = lebih baik?

---

## Checklist Penyelesaian

- [ ] Langkah 1: PCA diterapkan pada Iris, explained variance ratio dihitung
- [ ] Langkah 2: Scree plot dan cumulative variance plot berhasil dibuat
- [ ] Langkah 3: Visualisasi 2D PCA berhasil menunjukkan pemisahan kelas
- [ ] Langkah 4: SelectKBest dengan f_classif dan chi2 berhasil diterapkan
- [ ] Langkah 5: RFE berhasil mengidentifikasi 2 fitur terbaik
- [ ] Langkah 6: Feature importance dari Random Forest berhasil divisualisasi
- [ ] Langkah 7: Perbandingan akurasi empat strategi berhasil dilakukan
- [ ] Semua kode berjalan tanpa error di Google Colab
- [ ] Notebook disimpan dengan format `Lab10_NamaAnda_NIM.ipynb`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
