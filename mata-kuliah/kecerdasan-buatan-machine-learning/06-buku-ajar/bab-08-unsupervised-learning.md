# BAB 8: UNSUPERVISED LEARNING

**Tri Aji Nugroho, S.T., M.T.**
Kecerdasan Buatan dan Machine Learning — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| Sub-CPMK 9.1 | Menerapkan algoritma clustering (K-Means, Hierarchical, DBSCAN) pada dataset riil menggunakan scikit-learn | C3 |
| Sub-CPMK 9.2 | Menganalisis dan membandingkan hasil berbagai algoritma clustering serta memilih metode yang tepat berdasarkan karakteristik data | C4 |

**CPMK-4:** Menganalisis data menggunakan algoritma unsupervised learning dan teknik reduksi dimensi.

---

## Estimasi Waktu

| Komponen | Durasi |
|----------|--------|
| Membaca materi | 90 menit |
| Praktik kode Python | 60 menit |
| Latihan soal | 45 menit |
| **Total** | **195 menit** |

---

## Prasyarat

- Pemahaman dasar Python dan library scikit-learn (Bab 2)
- Konsep supervised learning: klasifikasi dan regresi (Bab 5-7)
- Dasar-dasar visualisasi data dengan matplotlib dan seaborn (Bab 4)
- Konsep evaluasi model (Bab 5)

---

## 8.1 Supervised vs Unsupervised Learning

### 8.1.1 Perbedaan Mendasar

Dalam supervised learning, kita memiliki data berlabel (*labeled data*) — setiap contoh pelatihan memiliki pasangan input-output. Dalam unsupervised learning, kita hanya memiliki data tanpa label dan bertugas menemukan **pola tersembunyi** dalam data tersebut.

| Aspek | Supervised Learning | Unsupervised Learning |
|-------|--------------------|-----------------------|
| **Data** | Berlabel (X, y) | Tanpa label (X saja) |
| **Tujuan** | Memprediksi output | Menemukan pola/struktur |
| **Contoh algoritma** | Regresi, Decision Tree, SVM | K-Means, DBSCAN, PCA |
| **Evaluasi** | Accuracy, precision, recall | Silhouette score, inertia |
| **Contoh kasus** | Prediksi harga rumah, klasifikasi spam | Segmentasi pelanggan, deteksi anomali |

```
Supervised Learning:
  Input → [Model] → Output (label diketahui)
  "Foto ini adalah kucing" (label sudah ada)

Unsupervised Learning:
  Input → [Model] → Pola/Cluster (label TIDAK diketahui)
  "Data ini terbagi menjadi 3 kelompok alami"
```

### 8.1.2 Kapan Menggunakan Unsupervised Learning?

Unsupervised learning digunakan ketika:

1. **Tidak ada label tersedia** — Data belum dianotasi dan proses pelabelan terlalu mahal
2. **Eksplorasi data** — Ingin memahami struktur natural dalam data
3. **Segmentasi** — Mengelompokkan pelanggan, produk, atau entitas lainnya
4. **Deteksi anomali** — Menemukan data yang tidak biasa (fraud detection)
5. **Preprocessing** — Reduksi dimensi sebelum supervised learning
6. **Generasi fitur baru** — Cluster membership sebagai fitur tambahan

> **Analogi:** Bayangkan Anda diminta mengelompokkan 1.000 buah tanpa diberitahu nama jenis buahnya. Anda akan mengelompokkan berdasarkan warna, ukuran, dan bentuk — inilah unsupervised learning.

---

## 8.2 Clustering Overview

### 8.2.1 Apa itu Clustering?

**Clustering** (pengelompokan) adalah proses membagi data menjadi **kelompok-kelompok** (*clusters*) sedemikian rupa sehingga:
- Data dalam satu cluster **mirip** satu sama lain (*high intra-cluster similarity*)
- Data antar cluster **berbeda** satu sama lain (*low inter-cluster similarity*)

```
Data Awal:                    Setelah Clustering:
  .  .     . .                  o  o     x x
    .  .  .                       o  o  x
  .    .     .                  o    o     x
        . .    .                      x x    +
          .  .                          x  +
             .    .                       +    +
                .  .                        +  +
```

### 8.2.2 Jenis-jenis Clustering

| Metode | Pendekatan | Contoh |
|--------|------------|--------|
| **Partitioning** | Membagi data menjadi K cluster | K-Means, K-Medoids |
| **Hierarchical** | Membangun hierarki cluster | Agglomerative, Divisive |
| **Density-based** | Berdasarkan kepadatan titik data | DBSCAN, OPTICS |
| **Distribution-based** | Berdasarkan distribusi probabilitas | Gaussian Mixture Models |

### 8.2.3 Metrik Jarak

Clustering bergantung pada ukuran **kemiripan** (*similarity*) atau **jarak** (*distance*):

| Metrik | Formula | Digunakan Untuk |
|--------|---------|-----------------|
| **Euclidean** | $\sqrt{\sum(x_i - y_i)^2}$ | Data numerik kontinu |
| **Manhattan** | $\sum|x_i - y_i|$ | Data dengan outlier |
| **Cosine** | $1 - \frac{x \cdot y}{\|x\| \|y\|}$ | Data teks, sparse |

```python
import numpy as np

# Contoh perhitungan jarak
titik_a = np.array([1, 2])
titik_b = np.array([4, 6])

# Euclidean distance
euclidean = np.sqrt(np.sum((titik_a - titik_b)**2))
print(f"Euclidean distance: {euclidean:.2f}")  # 5.00

# Manhattan distance
manhattan = np.sum(np.abs(titik_a - titik_b))
print(f"Manhattan distance: {manhattan}")       # 7

# Cosine similarity
cosine_sim = np.dot(titik_a, titik_b) / (np.linalg.norm(titik_a) * np.linalg.norm(titik_b))
print(f"Cosine similarity: {cosine_sim:.4f}")   # 0.9839
```

---

## 8.3 K-Means Clustering

### 8.3.1 Algoritma K-Means

K-Means adalah algoritma clustering paling populer dan intuitif. Tujuannya: membagi n data menjadi **K cluster** dengan meminimalkan total jarak data ke centroid masing-masing cluster.

**Langkah-langkah Algoritma:**

```
1. INISIALISASI: Pilih K centroid secara acak
2. ASSIGNMENT:   Setiap titik data di-assign ke centroid terdekat
3. UPDATE:       Hitung ulang posisi centroid (rata-rata anggota cluster)
4. KONVERGENSI:  Ulangi langkah 2-3 sampai centroid tidak berubah
```

**Visualisasi langkah demi langkah:**

```
Langkah 1 (Inisialisasi):     Langkah 2 (Assignment):
  .  C1  .    .                  o  C1  o    x
    .  .   .                       o  o   x
  .     C2    .                  o     C2    x
        .  .    .                      x  x    x
          .   .                          x   x
            C3  .                          C3  +
              .    .                          +    +
                .  .                            +  +

Langkah 3 (Update centroid):   Langkah 4 (Re-assign):
  o  C1' o    x                  o  C1' o    x
    o  o   x                       o  o   x
  o     C2'   x                  o     C2'   x
        x  x    x                      x  x    +
          x   +                          +   +
            C3' +                          C3' +
              +    +                          +    +
                +  +                            +  +
```

**Objective function (inertia):**

$$J = \sum_{i=1}^{K} \sum_{x \in C_i} \|x - \mu_i\|^2$$

di mana $\mu_i$ adalah centroid cluster ke-i.

### 8.3.2 Memilih K: Elbow Method dan Silhouette Score

Salah satu tantangan utama K-Means adalah menentukan **jumlah cluster K** yang optimal.

**Elbow Method:**
- Jalankan K-Means untuk berbagai nilai K (misal K=1 sampai 10)
- Plot inertia (total jarak kuadrat) vs K
- Cari titik "siku" (*elbow*) di mana penurunan inertia mulai melambat

**Silhouette Score:**
- Mengukur seberapa baik setiap titik cocok dengan clusternya
- Nilai berkisar dari -1 (salah cluster) hingga +1 (sangat cocok)
- Rata-rata silhouette score yang tinggi menunjukkan clustering yang baik

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

# Buat data sintetis dengan 4 cluster
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=42)

# Elbow Method
inertias = []
silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X, kmeans.labels_))

# Plot Elbow dan Silhouette
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Elbow plot
axes[0].plot(list(K_range), inertias, 'bo-', linewidth=2)
axes[0].set_xlabel('Jumlah Cluster (K)')
axes[0].set_ylabel('Inertia')
axes[0].set_title('Elbow Method')
axes[0].grid(True, alpha=0.3)

# Silhouette plot
axes[1].plot(list(K_range), silhouette_scores, 'rs-', linewidth=2)
axes[1].set_xlabel('Jumlah Cluster (K)')
axes[1].set_ylabel('Silhouette Score')
axes[1].set_title('Silhouette Score vs K')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('elbow_silhouette.png', dpi=150, bbox_inches='tight')
plt.show()

# Nilai optimal
best_k = list(K_range)[np.argmax(silhouette_scores)]
print(f"K optimal berdasarkan Silhouette Score: {best_k}")
print(f"Silhouette Score terbaik: {max(silhouette_scores):.4f}")
```

### 8.3.3 K-Means dengan scikit-learn

```python
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Buat dataset pelanggan sederhana
np.random.seed(42)
n_pelanggan = 200

data_pelanggan = pd.DataFrame({
    'usia': np.concatenate([
        np.random.normal(25, 3, 70),   # Kelompok muda
        np.random.normal(40, 5, 80),   # Kelompok dewasa
        np.random.normal(55, 4, 50)    # Kelompok senior
    ]),
    'pengeluaran_bulanan_juta': np.concatenate([
        np.random.normal(2, 0.5, 70),  # Pengeluaran rendah
        np.random.normal(5, 1.0, 80),  # Pengeluaran sedang
        np.random.normal(8, 1.5, 50)   # Pengeluaran tinggi
    ])
})

print("=== DATA PELANGGAN (5 baris pertama) ===")
print(data_pelanggan.head())
print(f"\nJumlah data: {len(data_pelanggan)}")
print(f"\nStatistik deskriptif:\n{data_pelanggan.describe().round(2)}")

# Standardisasi data (PENTING untuk K-Means!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(data_pelanggan)

# Terapkan K-Means dengan K=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
data_pelanggan['cluster'] = kmeans.fit_predict(X_scaled)

# Evaluasi
sil_score = silhouette_score(X_scaled, data_pelanggan['cluster'])
print(f"\nSilhouette Score: {sil_score:.4f}")
print(f"Inertia: {kmeans.inertia_:.2f}")

# Profil setiap cluster
print("\n=== PROFIL CLUSTER ===")
profil = data_pelanggan.groupby('cluster').agg({
    'usia': ['mean', 'std', 'count'],
    'pengeluaran_bulanan_juta': ['mean', 'std']
}).round(2)
print(profil)
```

### 8.3.4 Visualisasi Cluster

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 7))

# Plot data per cluster
warna = ['#FF6B6B', '#4ECDC4', '#45B7D1']
label_cluster = ['Muda-Hemat', 'Dewasa-Menengah', 'Senior-Premium']

for i in range(3):
    mask = data_pelanggan['cluster'] == i
    ax.scatter(
        data_pelanggan.loc[mask, 'usia'],
        data_pelanggan.loc[mask, 'pengeluaran_bulanan_juta'],
        c=warna[i], label=label_cluster[i],
        alpha=0.6, edgecolors='w', s=60
    )

# Plot centroid (konversi kembali dari skala standar)
centroids_original = scaler.inverse_transform(kmeans.cluster_centers_)
ax.scatter(
    centroids_original[:, 0], centroids_original[:, 1],
    c='black', marker='X', s=200, linewidths=2,
    edgecolors='gold', label='Centroid', zorder=5
)

ax.set_xlabel('Usia (tahun)', fontsize=12)
ax.set_ylabel('Pengeluaran Bulanan (Juta Rp)', fontsize=12)
ax.set_title('Segmentasi Pelanggan dengan K-Means (K=3)', fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('kmeans_clustering.png', dpi=150, bbox_inches='tight')
plt.show()
```

> **Catatan Penting:** K-Means sangat sensitif terhadap **skala fitur**. Selalu lakukan **standardisasi** (StandardScaler) sebelum menerapkan K-Means, karena fitur dengan skala besar akan mendominasi perhitungan jarak.

---

## 8.4 Hierarchical Clustering

### 8.4.1 Pendekatan Agglomerative

Hierarchical clustering membangun **hierarki cluster** yang dapat divisualisasikan sebagai **dendrogram**. Pendekatan **agglomerative** (*bottom-up*) bekerja sebagai berikut:

```
Langkah-langkah Agglomerative Clustering:
1. Mulai: setiap data = 1 cluster sendiri (N cluster)
2. Gabungkan 2 cluster terdekat menjadi 1
3. Ulangi langkah 2 sampai tersisa 1 cluster
4. "Potong" dendrogram pada tingkat tertentu untuk mendapat K cluster

Contoh dengan 5 data:
Langkah 0: {A} {B} {C} {D} {E}     → 5 cluster
Langkah 1: {A,B} {C} {D} {E}       → 4 cluster (A,B paling dekat)
Langkah 2: {A,B} {C} {D,E}         → 3 cluster (D,E digabung)
Langkah 3: {A,B} {C,D,E}           → 2 cluster
Langkah 4: {A,B,C,D,E}             → 1 cluster
```

**Kelebihan dibanding K-Means:**
- Tidak perlu menentukan K di awal
- Menghasilkan hierarki yang informatif (dendrogram)
- Dapat menangani cluster non-spherical

### 8.4.2 Linkage Methods

Metode **linkage** menentukan bagaimana jarak antar cluster dihitung:

| Linkage | Jarak Antar Cluster | Karakteristik |
|---------|---------------------|---------------|
| **Single** | Jarak minimum antar anggota | Cenderung membentuk rantai panjang (*chaining*) |
| **Complete** | Jarak maksimum antar anggota | Cluster cenderung bulat dan kompak |
| **Average** | Rata-rata jarak antar anggota | Keseimbangan antara single dan complete |
| **Ward** | Peningkatan total variance | Mirip K-Means, cluster kompak dan seimbang |

```
Single linkage:              Complete linkage:
  d(A,B) = min d(ai, bj)      d(A,B) = max d(ai, bj)

  Cluster A    Cluster B      Cluster A    Cluster B
    o o          o o             o o          o o
    o o   ←→   o o             o o   ←→   o o
     ^  jarak terdekat          ^  jarak terjauh
```

### 8.4.3 Dendrogram dengan scipy

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.preprocessing import StandardScaler

# Menggunakan data pelanggan yang sama (ambil subset untuk dendrogram yang jelas)
np.random.seed(42)
sample_idx = np.random.choice(len(data_pelanggan), 30, replace=False)
X_sample = data_pelanggan[['usia', 'pengeluaran_bulanan_juta']].iloc[sample_idx].values

# Standardisasi
scaler = StandardScaler()
X_sample_scaled = scaler.fit_transform(X_sample)

# Hitung linkage matrix dengan Ward method
Z = linkage(X_sample_scaled, method='ward')

# Buat dendrogram
fig, ax = plt.subplots(figsize=(14, 7))
dendrogram(
    Z,
    leaf_rotation=90,
    leaf_font_size=8,
    color_threshold=5,  # Warnai berdasarkan threshold
    ax=ax
)
ax.set_title('Dendrogram Hierarchical Clustering (Ward Linkage)', fontsize=14)
ax.set_xlabel('Indeks Data')
ax.set_ylabel('Jarak (Distance)')
ax.axhline(y=5, color='r', linestyle='--', label='Threshold (K=3)')
ax.legend()
plt.tight_layout()
plt.savefig('dendrogram.png', dpi=150, bbox_inches='tight')
plt.show()

# Potong dendrogram untuk mendapat 3 cluster
cluster_labels = fcluster(Z, t=3, criterion='maxclust')
print(f"Jumlah data per cluster: {np.bincount(cluster_labels)[1:]}")
```

### 8.4.4 AgglomerativeClustering dengan scikit-learn

```python
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

# Terapkan pada dataset lengkap
X_full_scaled = StandardScaler().fit_transform(
    data_pelanggan[['usia', 'pengeluaran_bulanan_juta']]
)

# Bandingkan berbagai linkage
linkage_methods = ['ward', 'complete', 'average', 'single']
results = []

for method in linkage_methods:
    agg = AgglomerativeClustering(n_clusters=3, linkage=method)
    labels = agg.fit_predict(X_full_scaled)
    sil = silhouette_score(X_full_scaled, labels)
    results.append({'Linkage': method, 'Silhouette': round(sil, 4)})

df_results = pd.DataFrame(results)
print("=== PERBANDINGAN LINKAGE METHODS ===")
print(df_results.to_string(index=False))

# Visualisasi hasil terbaik (Ward)
agg_ward = AgglomerativeClustering(n_clusters=3, linkage='ward')
labels_ward = agg_ward.fit_predict(X_full_scaled)

fig, ax = plt.subplots(figsize=(10, 7))
scatter = ax.scatter(
    data_pelanggan['usia'],
    data_pelanggan['pengeluaran_bulanan_juta'],
    c=labels_ward, cmap='viridis', alpha=0.6, edgecolors='w', s=60
)
ax.set_xlabel('Usia (tahun)', fontsize=12)
ax.set_ylabel('Pengeluaran Bulanan (Juta Rp)', fontsize=12)
ax.set_title('Hierarchical Clustering (Ward, K=3)', fontsize=14)
plt.colorbar(scatter, label='Cluster')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('hierarchical_clustering.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## 8.5 DBSCAN: Density-Based Clustering

### 8.5.1 Core Points, Border Points, dan Noise

**DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) mengelompokkan data berdasarkan **kepadatan** (*density*), bukan jarak ke centroid. Ini memungkinkan DBSCAN menemukan cluster dengan **bentuk arbitrary** dan secara otomatis mendeteksi **noise/outlier**.

**Konsep utama:**

| Istilah | Definisi |
|---------|----------|
| **Core point** | Titik yang memiliki >= `min_samples` tetangga dalam radius `eps` |
| **Border point** | Titik yang berada dalam radius `eps` dari core point, tapi bukan core point |
| **Noise** | Titik yang bukan core point maupun border point |

```
Contoh dengan eps=1.0, min_samples=4:

  Core point (C):     Border point (B):     Noise (N):
  >= 4 tetangga       dekat core point      terisolasi
  dalam radius eps    tapi < 4 tetangga

     o o
    o C o              B o o                    N
     o o                o C o
                         o o
```

**Algoritma DBSCAN:**
1. Untuk setiap titik, hitung jumlah tetangga dalam radius `eps`
2. Tandai titik sebagai core/border/noise
3. Hubungkan core points yang berdekatan menjadi cluster
4. Tambahkan border points ke cluster terdekat
5. Noise points tidak termasuk cluster manapun (label = -1)

### 8.5.2 Parameter: eps dan min_samples

| Parameter | Fungsi | Tips Pemilihan |
|-----------|--------|----------------|
| `eps` | Radius pencarian tetangga | Gunakan **k-distance plot** |
| `min_samples` | Minimum tetangga untuk core point | Umumnya >= dimensi data + 1 |

**K-Distance Plot** untuk menentukan `eps`:

```python
from sklearn.neighbors import NearestNeighbors

# Hitung jarak ke tetangga ke-k terdekat
k = 5  # min_samples yang direncanakan
nn = NearestNeighbors(n_neighbors=k)
nn.fit(X_full_scaled)
distances, _ = nn.kneighbors(X_full_scaled)

# Urutkan jarak k-nearest neighbor
k_distances = np.sort(distances[:, k-1])

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(k_distances, 'b-', linewidth=1)
ax.set_xlabel('Titik Data (diurutkan)')
ax.set_ylabel(f'{k}-Distance')
ax.set_title(f'K-Distance Plot (k={k}) untuk Menentukan eps')
ax.grid(True, alpha=0.3)

# Tandai "elbow" (titik eps yang direkomendasikan)
ax.axhline(y=0.5, color='r', linestyle='--', label='eps = 0.5 (kandidat)')
ax.legend()
plt.tight_layout()
plt.savefig('k_distance_plot.png', dpi=150, bbox_inches='tight')
plt.show()
```

### 8.5.3 DBSCAN dengan scikit-learn

```python
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

# Buat data dengan cluster berbentuk non-spherical
from sklearn.datasets import make_moons
X_moons, _ = make_moons(n_samples=300, noise=0.05, random_state=42)

# Bandingkan K-Means vs DBSCAN pada data non-spherical
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# K-Means (gagal pada data non-spherical)
kmeans_moons = KMeans(n_clusters=2, random_state=42, n_init=10)
labels_km = kmeans_moons.fit_predict(X_moons)
axes[0].scatter(X_moons[:, 0], X_moons[:, 1], c=labels_km, cmap='viridis', alpha=0.6, s=40)
axes[0].set_title(f'K-Means (K=2)\nSilhouette: {silhouette_score(X_moons, labels_km):.3f}')

# DBSCAN (berhasil)
dbscan = DBSCAN(eps=0.2, min_samples=5)
labels_db = dbscan.fit_predict(X_moons)
# Hitung silhouette hanya untuk data non-noise
mask = labels_db != -1
if len(set(labels_db[mask])) > 1:
    sil_db = silhouette_score(X_moons[mask], labels_db[mask])
else:
    sil_db = 0.0
axes[1].scatter(X_moons[:, 0], X_moons[:, 1], c=labels_db, cmap='viridis', alpha=0.6, s=40)
axes[1].set_title(f'DBSCAN (eps=0.2, min_samples=5)\nSilhouette: {sil_db:.3f}')

# Data asli
axes[2].scatter(X_moons[:, 0], X_moons[:, 1], c='gray', alpha=0.6, s=40)
axes[2].set_title('Data Asli (make_moons)')

for ax in axes:
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')

plt.tight_layout()
plt.savefig('kmeans_vs_dbscan.png', dpi=150, bbox_inches='tight')
plt.show()

# Detail DBSCAN
n_clusters = len(set(labels_db)) - (1 if -1 in labels_db else 0)
n_noise = list(labels_db).count(-1)
print(f"Jumlah cluster: {n_clusters}")
print(f"Jumlah noise points: {n_noise}")
print(f"Persentase noise: {n_noise/len(labels_db)*100:.1f}%")
```

---

## 8.6 Perbandingan Algoritma Clustering

| Aspek | K-Means | Hierarchical | DBSCAN |
|-------|---------|-------------|--------|
| **Perlu K?** | Ya (harus ditentukan) | Opsional (potong dendrogram) | Tidak (otomatis) |
| **Bentuk cluster** | Spherical (bulat) | Fleksibel | Arbitrary (bebas) |
| **Menangani noise?** | Tidak | Tidak | Ya (label -1) |
| **Kompleksitas** | O(n K t) — cepat | O(n^2 log n) — sedang | O(n log n) — sedang |
| **Skalabilitas** | Baik (data besar) | Kurang (data besar) | Baik |
| **Sensitif terhadap** | Inisialisasi, outlier | Linkage method | Parameter eps, min_samples |
| **Kelebihan utama** | Sederhana, cepat | Dendrogram informatif | Bentuk cluster bebas |
| **Kapan digunakan** | Cluster jelas terpisah | Ingin hierarki | Data dengan noise/outlier |

**Panduan pemilihan algoritma:**

```
Apakah cluster berbentuk bulat?
├── Ya → Apakah data besar (>100K)?
│   ├── Ya → K-Means (MiniBatchKMeans untuk sangat besar)
│   └── Tidak → K-Means atau Hierarchical
└── Tidak → Apakah ada noise/outlier?
    ├── Ya → DBSCAN
    └── Tidak → Hierarchical (average/complete linkage)
```

---

## 8.7 Studi Kasus Indonesia: Segmentasi Pelanggan E-Commerce

### 8.7.1 Konteks

Sebuah platform e-commerce Indonesia ingin melakukan **segmentasi pelanggan** (*customer segmentation*) berdasarkan perilaku belanja mereka. Segmentasi ini akan digunakan untuk:
- Menyesuaikan strategi pemasaran per segmen
- Personalisasi rekomendasi produk
- Mengidentifikasi pelanggan bernilai tinggi (*high-value customers*)

### 8.7.2 Dataset dan Preprocessing

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Simulasi data pelanggan e-commerce Indonesia
np.random.seed(42)
n = 500

# Segmen 1: Pelanggan baru (aktif rendah)
seg1 = pd.DataFrame({
    'total_transaksi': np.random.poisson(3, 150),
    'total_belanja_juta': np.random.exponential(0.5, 150),
    'rata_rata_rating': np.random.normal(3.5, 0.8, 150).clip(1, 5),
    'jumlah_kategori': np.random.poisson(2, 150).clip(1, 10),
    'hari_sejak_terakhir': np.random.exponential(60, 150),
    'frekuensi_login_bulanan': np.random.poisson(3, 150)
})

# Segmen 2: Pelanggan reguler
seg2 = pd.DataFrame({
    'total_transaksi': np.random.poisson(15, 200),
    'total_belanja_juta': np.random.exponential(2.5, 200),
    'rata_rata_rating': np.random.normal(4.0, 0.5, 200).clip(1, 5),
    'jumlah_kategori': np.random.poisson(5, 200).clip(1, 15),
    'hari_sejak_terakhir': np.random.exponential(15, 200),
    'frekuensi_login_bulanan': np.random.poisson(10, 200)
})

# Segmen 3: Pelanggan premium
seg3 = pd.DataFrame({
    'total_transaksi': np.random.poisson(40, 100),
    'total_belanja_juta': np.random.exponential(8, 100),
    'rata_rata_rating': np.random.normal(4.5, 0.3, 100).clip(1, 5),
    'jumlah_kategori': np.random.poisson(8, 100).clip(1, 20),
    'hari_sejak_terakhir': np.random.exponential(5, 100),
    'frekuensi_login_bulanan': np.random.poisson(20, 100)
})

# Segmen 4: Pelanggan tidak aktif (churned)
seg4 = pd.DataFrame({
    'total_transaksi': np.random.poisson(8, 50),
    'total_belanja_juta': np.random.exponential(1.5, 50),
    'rata_rata_rating': np.random.normal(2.5, 0.8, 50).clip(1, 5),
    'jumlah_kategori': np.random.poisson(3, 50).clip(1, 10),
    'hari_sejak_terakhir': np.random.exponential(120, 50),
    'frekuensi_login_bulanan': np.random.poisson(1, 50)
})

# Gabungkan semua segmen
df = pd.concat([seg1, seg2, seg3, seg4], ignore_index=True)
df['rata_rata_rating'] = df['rata_rata_rating'].round(1)
df['total_belanja_juta'] = df['total_belanja_juta'].round(2)

print("=== DATASET E-COMMERCE ===")
print(f"Jumlah pelanggan: {len(df)}")
print(f"Fitur: {list(df.columns)}")
print(f"\n{df.describe().round(2)}")

# Standardisasi
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)
```

### 8.7.3 Penerapan Clustering dan Evaluasi

```python
# 1. Tentukan K optimal
inertias = []
sil_scores = []
K_range = range(2, 9)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)
    sil_scores.append(silhouette_score(X_scaled, km.labels_))

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].plot(list(K_range), inertias, 'bo-')
axes[0].set_title('Elbow Method')
axes[0].set_xlabel('K')
axes[0].set_ylabel('Inertia')
axes[0].grid(True, alpha=0.3)

axes[1].plot(list(K_range), sil_scores, 'rs-')
axes[1].set_title('Silhouette Score')
axes[1].set_xlabel('K')
axes[1].set_ylabel('Score')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ecommerce_elbow.png', dpi=150, bbox_inches='tight')
plt.show()

# 2. Terapkan K-Means dengan K=4
kmeans_final = KMeans(n_clusters=4, random_state=42, n_init=10)
df['cluster_kmeans'] = kmeans_final.fit_predict(X_scaled)

print("=== PROFIL SEGMEN PELANGGAN ===")
profil_segmen = df.groupby('cluster_kmeans').agg({
    'total_transaksi': 'mean',
    'total_belanja_juta': 'mean',
    'rata_rata_rating': 'mean',
    'jumlah_kategori': 'mean',
    'hari_sejak_terakhir': 'mean',
    'frekuensi_login_bulanan': 'mean'
}).round(2)

# Beri label segmen
label_segmen = {0: 'Baru', 1: 'Reguler', 2: 'Premium', 3: 'Churned'}
profil_segmen.index = profil_segmen.index.map(
    lambda x: f"Segmen {x}: {label_segmen.get(x, 'Unknown')}"
)
print(profil_segmen)

# Jumlah pelanggan per segmen
print(f"\nDistribusi segmen:\n{df['cluster_kmeans'].value_counts().sort_index()}")
```

### 8.7.4 Visualisasi dan Interpretasi

```python
# Visualisasi profil segmen dengan radar chart
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fitur_list = df.columns[:-1]  # Semua fitur kecuali cluster

for idx, fitur in enumerate(fitur_list):
    ax = axes[idx // 3, idx % 3]
    df.boxplot(column=fitur, by='cluster_kmeans', ax=ax)
    ax.set_title(fitur.replace('_', ' ').title())
    ax.set_xlabel('Cluster')

plt.suptitle('Distribusi Fitur per Cluster', fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig('ecommerce_cluster_profiles.png', dpi=150, bbox_inches='tight')
plt.show()

# Heatmap profil cluster (normalized)
profil_norm = df.groupby('cluster_kmeans')[fitur_list].mean()
profil_norm = (profil_norm - profil_norm.min()) / (profil_norm.max() - profil_norm.min())

fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(profil_norm, annot=True, fmt='.2f', cmap='YlOrRd',
            xticklabels=[f.replace('_', '\n') for f in fitur_list],
            yticklabels=['Segmen 0', 'Segmen 1', 'Segmen 2', 'Segmen 3'],
            ax=ax)
ax.set_title('Profil Segmen Pelanggan (Normalized)', fontsize=14)
plt.tight_layout()
plt.savefig('ecommerce_heatmap.png', dpi=150, bbox_inches='tight')
plt.show()

# Rekomendasi bisnis per segmen
print("\n=== REKOMENDASI STRATEGI PER SEGMEN ===")
rekomendasi = {
    'Segmen 0 (Baru)': 'Onboarding campaign, voucher pembelian pertama, edukasi fitur',
    'Segmen 1 (Reguler)': 'Loyalty program, cross-selling berdasarkan kategori favorit',
    'Segmen 2 (Premium)': 'VIP program, early access promo, dedicated customer service',
    'Segmen 3 (Churned)': 'Win-back campaign, survei kepuasan, penawaran khusus re-activation'
}
for segmen, strategi in rekomendasi.items():
    print(f"  {segmen}: {strategi}")
```

---

## 8.8 AI Corner: Menggunakan AI untuk Interpretasi Clustering

### Level: Intermediate-Advanced

| Kemampuan AI | Contoh Penggunaan |
|-------------|-------------------|
| Interpretasi cluster | Meminta AI menganalisis profil cluster dan memberikan label bermakna |
| Debugging kode clustering | Meminta AI memeriksa parameter dan preprocessing |
| Saran visualisasi | Meminta AI merekomendasikan cara visualisasi terbaik |
| Validasi bisnis | Mendiskusikan apakah segmen yang ditemukan masuk akal secara bisnis |

### Contoh Prompt yang Baik

```
Saya melakukan K-Means clustering pada data pelanggan e-commerce dengan 6 fitur:
total_transaksi, total_belanja, rating, jumlah_kategori, hari_sejak_terakhir,
frekuensi_login.

Hasil K=4 menghasilkan profil cluster berikut:
[paste tabel profil cluster]

1. Berikan label yang bermakna untuk setiap cluster
2. Apakah segmen ini masuk akal secara bisnis?
3. Strategi apa yang tepat untuk masing-masing segmen?
4. Apakah ada fitur yang mungkin redundan?
```

### Contoh Prompt yang Kurang Baik

```
Cluster data saya
```

### Yang Perlu Diingat

1. **AI tidak melihat data Anda** — selalu sertakan statistik deskriptif atau profil cluster
2. **Verifikasi interpretasi AI** — AI mungkin memberi label yang tidak sesuai konteks Indonesia
3. **Domain knowledge tetap penting** — Anda lebih memahami konteks bisnis daripada AI
4. **Dokumentasikan penggunaan AI** — Catat prompt dan modifikasi dalam AI Usage Log

### Template AI Usage Log untuk Clustering

```markdown
## AI Usage Documentation — Bab 8
### Tool: [Claude / ChatGPT / Copilot]
### Prompt: "Interpretasikan profil 4 cluster dari data e-commerce..."
### Output: [Ringkasan interpretasi AI]
### Modifikasi: [Label cluster disesuaikan dengan konteks Indonesia]
### Refleksi: [Apa yang saya pelajari tentang interpretasi cluster?]
```

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan utama antara supervised learning dan unsupervised learning. Berikan masing-masing dua contoh kasus penggunaan di Indonesia.

**Soal 2.** Sebutkan dan jelaskan 3 jenis titik data dalam algoritma DBSCAN (core point, border point, noise point).

**Soal 3.** Apa yang dimaksud dengan *inertia* dalam K-Means? Mengapa kita tidak bisa memilih K yang paling kecil inertia-nya?

**Soal 4.** Jelaskan perbedaan antara 4 linkage methods (single, complete, average, Ward) dalam hierarchical clustering. Kapan Ward linkage paling tepat digunakan?

**Soal 5.** Mengapa standardisasi data (StandardScaler) penting sebelum melakukan clustering? Berikan contoh kasus di mana tanpa standardisasi akan menghasilkan cluster yang salah.

### Tingkat Menengah (C3)

**Soal 6.** Tulis kode Python untuk menerapkan K-Means clustering pada dataset berikut:
- Buat 300 data acak dengan 3 fitur: `penghasilan`, `usia`, `skor_kredit`
- Tentukan K optimal menggunakan elbow method
- Terapkan K-Means dengan K optimal
- Visualisasikan hasil dalam scatter plot

**Soal 7.** Diberikan dataset berikut (5 titik 2D):
```
A(1,2), B(1.5,1.8), C(5,8), D(8,8), E(1,0.6)
```
Lakukan hierarchical clustering dengan single linkage secara manual (tunjukkan langkah per langkah). Gambar dendrogramnya.

**Soal 8.** Bandingkan hasil K-Means (K=3) dan DBSCAN pada dataset `make_moons` dari sklearn. Algoritma mana yang lebih baik dan mengapa?

### Tingkat Mahir (C4)

**Soal 9.** Sebuah rumah sakit di Jakarta ingin mengelompokkan pasien berdasarkan riwayat kesehatan untuk personalisasi layanan. Dataset memiliki fitur: usia, jumlah_kunjungan, total_biaya, jumlah_diagnosa, lama_rawat.
- a) Jelaskan langkah-langkah lengkap (preprocessing hingga interpretasi) untuk melakukan customer segmentation.
- b) Algoritma clustering mana yang paling tepat? Jelaskan alasan Anda.
- c) Bagaimana Anda mengevaluasi kualitas clustering tanpa label?
- d) Tulis kode Python lengkap untuk implementasi.

**Soal 10.** Anda diminta melakukan segmentasi UMKM di Indonesia berdasarkan data BPS: jumlah_karyawan, omzet_tahunan, umur_usaha, jumlah_produk, dan wilayah (kode provinsi).
- a) Apakah variabel `wilayah` bisa langsung digunakan dalam K-Means? Jelaskan.
- b) Bagaimana menangani fitur campuran (numerik + kategorikal)?
- c) Implementasikan clustering dan berikan rekomendasi kebijakan per segmen.

---

## Rangkuman

1. **Unsupervised learning** menemukan pola tersembunyi dalam data tanpa label, berbeda dengan supervised learning yang membutuhkan data berlabel.
2. **K-Means** membagi data menjadi K cluster berdasarkan jarak ke centroid. Gunakan elbow method dan silhouette score untuk memilih K optimal. Selalu lakukan standardisasi data terlebih dahulu.
3. **Hierarchical clustering** membangun hierarki cluster yang divisualisasikan sebagai dendrogram. Ward linkage umumnya menghasilkan cluster paling kompak dan seimbang.
4. **DBSCAN** mengelompokkan data berdasarkan kepadatan, mampu menemukan cluster berbentuk arbitrary dan secara otomatis mendeteksi noise/outlier.
5. **Pemilihan algoritma** bergantung pada bentuk cluster, keberadaan noise, dan ukuran data. Tidak ada satu algoritma yang terbaik untuk semua kasus.
6. **Evaluasi clustering** menggunakan metrik internal (silhouette score, inertia) karena tidak ada label ground truth.
7. Dalam konteks bisnis Indonesia (e-commerce, perbankan, kesehatan), clustering digunakan untuk **segmentasi** yang mendorong strategi yang lebih personal dan efektif.

---

## Referensi

1. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.
2. Geron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
3. scikit-learn documentation. (2026). *Clustering*. Retrieved from https://scikit-learn.org/stable/modules/clustering.html
4. Ester, M., Kriegel, H. P., Sander, J., & Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. *KDD-96 Proceedings*.
5. Raschka, S., & Mirjalili, V. (2022). *Python Machine Learning* (4th ed.). Packt Publishing.
6. BPS. (2025). *Statistik E-Commerce Indonesia*. Badan Pusat Statistik.

---

*Bab berikutnya: **Bab 9 — Dimensionality Reduction dan Feature Selection***

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
