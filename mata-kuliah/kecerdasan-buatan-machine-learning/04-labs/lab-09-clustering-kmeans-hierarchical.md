# Lab 09: Clustering — K-Means dan Hierarchical

**Mata Kuliah:** Kecerdasan Buatan dan Machine Learning
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Minggu:** 9 (setelah UTS)
**Penilaian:** Dinilai (submit notebook)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

- Menghasilkan data sintetis untuk clustering menggunakan `make_blobs`
- Menerapkan algoritma K-Means dan memvisualisasikan hasil cluster
- Menentukan jumlah cluster optimal dengan metode Elbow dan Silhouette
- Menerapkan Hierarchical Clustering dan membaca dendrogram
- Menerapkan DBSCAN untuk clustering berbasis densitas
- Membandingkan performa tiga metode clustering pada dataset yang sama

---

## Persiapan

1. Buka Google Colab notebook baru
2. Nama file: `Lab09_NamaAnda_NIM.ipynb`
3. Pastikan library `scikit-learn`, `scipy`, `matplotlib`, dan `numpy` sudah bisa diimpor

---

## Langkah-langkah

### Langkah 1: Setup dan Generate Data Clustering

```python
# =============================================
# LANGKAH 1: Setup dan Generate Data
# =============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Set random seed untuk reproducibility
np.random.seed(42)

# Generate data simulasi segmentasi pelanggan e-commerce Indonesia
# Fitur: total_belanja (juta Rp), frekuensi_transaksi (per bulan)
X, y_true = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=[1.0, 1.5, 0.8, 1.2],
    random_state=42
)

# Transformasi agar realistis (belanja & frekuensi)
X[:, 0] = np.abs(X[:, 0]) * 2 + 1    # total belanja (juta Rp)
X[:, 1] = np.abs(X[:, 1]) * 3 + 1    # frekuensi transaksi per bulan

df = pd.DataFrame(X, columns=['total_belanja_juta', 'frekuensi_transaksi'])
df['label_asli'] = y_true

print(f"Dataset: {df.shape[0]} pelanggan e-commerce")
print(f"Fitur: {list(df.columns[:2])}")
print(f"\nStatistik deskriptif:")
print(df[['total_belanja_juta', 'frekuensi_transaksi']].describe().round(2))

# Visualisasi data awal
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c='steelblue', alpha=0.6, s=30)
plt.xlabel('Total Belanja (Juta Rp)')
plt.ylabel('Frekuensi Transaksi per Bulan')
plt.title('Data Pelanggan E-Commerce Indonesia')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 2: K-Means — Fit, Predict, dan Visualisasi

```python
# =============================================
# LANGKAH 2: K-Means Clustering
# =============================================

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Standardisasi fitur (penting untuk clustering)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Terapkan K-Means dengan K=4
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(X_scaled)
labels_kmeans = kmeans.predict(X_scaled)

# Ambil centroid dan transform kembali ke skala asli
centroids_scaled = kmeans.cluster_centers_
centroids_original = scaler.inverse_transform(centroids_scaled)

print("=== HASIL K-MEANS (K=4) ===")
print(f"Inertia (SSE): {kmeans.inertia_:.2f}")
print(f"\nJumlah anggota tiap cluster:")
for i in range(4):
    count = np.sum(labels_kmeans == i)
    print(f"  Cluster {i}: {count} pelanggan")

# Visualisasi hasil clustering
plt.figure(figsize=(10, 7))
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12']
for i in range(4):
    mask = labels_kmeans == i
    plt.scatter(X[mask, 0], X[mask, 1], c=colors[i], label=f'Cluster {i}',
                alpha=0.6, s=40)
plt.scatter(centroids_original[:, 0], centroids_original[:, 1],
            c='black', marker='X', s=200, linewidths=2, label='Centroid')
plt.xlabel('Total Belanja (Juta Rp)')
plt.ylabel('Frekuensi Transaksi per Bulan')
plt.title('Segmentasi Pelanggan E-Commerce — K-Means (K=4)')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 3: Metode Elbow — Menentukan K Optimal

```python
# =============================================
# LANGKAH 3: Metode Elbow
# =============================================

# Hitung inertia untuk berbagai nilai K
inertias = []
K_range = range(2, 11)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

# Plot Elbow
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertias, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Jumlah Cluster (K)')
plt.ylabel('Inertia (Within-Cluster SSE)')
plt.title('Metode Elbow — Menentukan Jumlah Cluster Optimal')
plt.xticks(K_range)
plt.grid(alpha=0.3)

# Tandai titik elbow (K=4)
plt.annotate('Elbow Point (K=4)', xy=(4, inertias[2]),
             xytext=(6, inertias[2] + 50),
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=12, color='red')

plt.tight_layout()
plt.show()

print("Interpretasi: Titik 'siku' (elbow) menunjukkan K optimal.")
print("Setelah titik ini, penambahan K tidak banyak mengurangi inertia.")
```

### Langkah 4: Analisis Silhouette

```python
# =============================================
# LANGKAH 4: Silhouette Analysis
# =============================================

from sklearn.metrics import silhouette_score, silhouette_samples

# Hitung Silhouette Score untuk berbagai K
silhouette_scores = []

for k in range(2, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    silhouette_scores.append(score)
    print(f"K={k}: Silhouette Score = {score:.4f}")

# Plot Silhouette Score vs K
plt.figure(figsize=(8, 5))
plt.plot(range(2, 11), silhouette_scores, 'go-', linewidth=2, markersize=8)
plt.xlabel('Jumlah Cluster (K)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score untuk Berbagai K')
plt.xticks(range(2, 11))
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Silhouette per sampel untuk K=4
km_best = KMeans(n_clusters=4, random_state=42, n_init=10)
labels_best = km_best.fit_predict(X_scaled)
sample_silhouette = silhouette_samples(X_scaled, labels_best)

print(f"\nK=4 — Rata-rata Silhouette Score: {silhouette_score(X_scaled, labels_best):.4f}")
for i in range(4):
    cluster_vals = sample_silhouette[labels_best == i]
    print(f"  Cluster {i}: mean={cluster_vals.mean():.4f}, "
          f"min={cluster_vals.min():.4f}, max={cluster_vals.max():.4f}")
```

### Langkah 5: Hierarchical Clustering (Agglomerative)

```python
# =============================================
# LANGKAH 5: Hierarchical Clustering
# =============================================

from sklearn.cluster import AgglomerativeClustering

# Terapkan Agglomerative Clustering
agg = AgglomerativeClustering(n_clusters=4, linkage='ward')
labels_agg = agg.fit_predict(X_scaled)

print("=== HASIL HIERARCHICAL CLUSTERING ===")
print(f"Linkage: Ward (minimize within-cluster variance)")
print(f"\nJumlah anggota tiap cluster:")
for i in range(4):
    count = np.sum(labels_agg == i)
    print(f"  Cluster {i}: {count} pelanggan")

# Visualisasi
plt.figure(figsize=(10, 7))
for i in range(4):
    mask = labels_agg == i
    plt.scatter(X[mask, 0], X[mask, 1], c=colors[i],
                label=f'Cluster {i}', alpha=0.6, s=40)
plt.xlabel('Total Belanja (Juta Rp)')
plt.ylabel('Frekuensi Transaksi per Bulan')
plt.title('Segmentasi Pelanggan — Hierarchical Clustering (Ward)')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 6: Dendrogram

```python
# =============================================
# LANGKAH 6: Dendrogram
# =============================================

from scipy.cluster.hierarchy import dendrogram, linkage

# Hitung linkage matrix (gunakan subset untuk visualisasi yang jelas)
# Ambil 50 sampel acak agar dendrogram terbaca
np.random.seed(42)
idx_sample = np.random.choice(len(X_scaled), size=50, replace=False)
X_sample = X_scaled[idx_sample]

# Hitung linkage
Z = linkage(X_sample, method='ward', metric='euclidean')

# Plot dendrogram
plt.figure(figsize=(14, 7))
dendrogram(
    Z,
    leaf_rotation=90,
    leaf_font_size=8,
    color_threshold=5.0
)
plt.title('Dendrogram — Hierarchical Clustering (Ward Linkage)')
plt.xlabel('Indeks Sampel')
plt.ylabel('Jarak (Distance)')
plt.axhline(y=5.0, color='red', linestyle='--', label='Threshold (K=4)')
plt.legend()
plt.tight_layout()
plt.show()

print("Interpretasi: Garis horizontal merah menunjukkan threshold")
print("untuk memotong dendrogram menjadi 4 cluster.")
```

### Langkah 7: DBSCAN — Clustering Berbasis Densitas

```python
# =============================================
# LANGKAH 7: DBSCAN
# =============================================

from sklearn.cluster import DBSCAN

# Terapkan DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels_dbscan = dbscan.fit_predict(X_scaled)

n_clusters_dbscan = len(set(labels_dbscan)) - (1 if -1 in labels_dbscan else 0)
n_noise = np.sum(labels_dbscan == -1)

print("=== HASIL DBSCAN ===")
print(f"eps=0.5, min_samples=5")
print(f"Jumlah cluster ditemukan: {n_clusters_dbscan}")
print(f"Jumlah noise points: {n_noise}")

# Visualisasi DBSCAN
plt.figure(figsize=(10, 7))
unique_labels = set(labels_dbscan)
cmap = plt.cm.get_cmap('tab10', len(unique_labels))

for label in unique_labels:
    mask = labels_dbscan == label
    if label == -1:
        plt.scatter(X[mask, 0], X[mask, 1], c='gray', marker='x',
                    s=30, alpha=0.5, label='Noise')
    else:
        plt.scatter(X[mask, 0], X[mask, 1], c=[cmap(label)],
                    label=f'Cluster {label}', alpha=0.6, s=40)

plt.xlabel('Total Belanja (Juta Rp)')
plt.ylabel('Frekuensi Transaksi per Bulan')
plt.title('Segmentasi Pelanggan — DBSCAN')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 8: Perbandingan Tiga Metode Clustering

```python
# =============================================
# LANGKAH 8: Perbandingan Metode
# =============================================

from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score

print("=" * 60)
print("PERBANDINGAN TIGA METODE CLUSTERING")
print("=" * 60)

# Hitung metrik evaluasi (terhadap label asli)
methods = {
    'K-Means': labels_kmeans,
    'Hierarchical': labels_agg,
    'DBSCAN': labels_dbscan
}

print(f"\n{'Metode':<15} {'ARI':>8} {'NMI':>8} {'Silhouette':>12}")
print("-" * 45)

for name, labels in methods.items():
    ari = adjusted_rand_score(y_true, labels)
    nmi = normalized_mutual_info_score(y_true, labels)
    # Silhouette hanya untuk label yang valid (bukan noise)
    valid = labels != -1
    if np.sum(valid) > 1 and len(set(labels[valid])) > 1:
        sil = silhouette_score(X_scaled[valid], labels[valid])
    else:
        sil = float('nan')
    print(f"{name:<15} {ari:>8.4f} {nmi:>8.4f} {sil:>12.4f}")

# Visualisasi side-by-side
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
titles = ['K-Means (K=4)', 'Hierarchical (Ward)', 'DBSCAN']
all_labels = [labels_kmeans, labels_agg, labels_dbscan]

for ax, title, labels in zip(axes, titles, all_labels):
    scatter = ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='tab10',
                         alpha=0.6, s=30)
    ax.set_xlabel('Total Belanja (Juta Rp)')
    ax.set_ylabel('Frekuensi Transaksi')
    ax.set_title(title)
    ax.grid(alpha=0.3)

plt.suptitle('Perbandingan Metode Clustering — Segmentasi Pelanggan', fontsize=14)
plt.tight_layout()
plt.show()

print("\nKesimpulan:")
print("- K-Means: baik untuk cluster berbentuk spherical, perlu tentukan K")
print("- Hierarchical: memberikan hierarki cluster, cocok untuk analisis dendogram")
print("- DBSCAN: otomatis menemukan K, bisa deteksi noise/outlier")
```

---

## Tantangan Tambahan

1. **Eksperimen Parameter DBSCAN:** Coba variasikan nilai `eps` (0.3, 0.5, 0.8, 1.0) dan `min_samples` (3, 5, 10). Buat tabel yang menunjukkan jumlah cluster dan noise point untuk setiap kombinasi. Analisis dampaknya terhadap hasil segmentasi pelanggan.

2. **Segmentasi dengan 3 Fitur:** Tambahkan fitur ketiga (misalnya `rata_rata_rating` produk) ke dataset. Terapkan K-Means dan Hierarchical Clustering pada data 3 dimensi. Visualisasikan hasilnya dengan 3D scatter plot menggunakan `mpl_toolkits.mplot3d`.

3. **Profiling Cluster:** Untuk hasil K-Means terbaik, buat profil deskriptif setiap cluster (misalnya: "Cluster 0 = Pelanggan Premium: belanja tinggi, frekuensi tinggi"). Sajikan dalam bentuk tabel ringkasan dengan rata-rata setiap fitur per cluster.

---

## Checklist Penyelesaian

- [ ] Langkah 1: Data clustering berhasil di-generate dan divisualisasi
- [ ] Langkah 2: K-Means berhasil diterapkan dan hasil cluster divisualisasi
- [ ] Langkah 3: Elbow method berhasil diploting dan K optimal teridentifikasi
- [ ] Langkah 4: Silhouette Score dihitung untuk berbagai K
- [ ] Langkah 5: Hierarchical Clustering berhasil diterapkan
- [ ] Langkah 6: Dendrogram berhasil divisualisasi
- [ ] Langkah 7: DBSCAN berhasil diterapkan, noise points teridentifikasi
- [ ] Langkah 8: Perbandingan tiga metode dengan metrik evaluasi
- [ ] Semua kode berjalan tanpa error di Google Colab
- [ ] Notebook disimpan dengan format `Lab09_NamaAnda_NIM.ipynb`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
