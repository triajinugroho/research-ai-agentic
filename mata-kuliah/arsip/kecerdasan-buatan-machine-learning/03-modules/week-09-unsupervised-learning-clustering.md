# Minggu 9: Unsupervised Learning — Clustering

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan dan Machine Learning (4 SKS) |
| **Minggu** | 9 |
| **Topik** | Unsupervised Learning — Clustering |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Semester** | Ganjil 2026/2027 |
| **CPMK** | CPMK-4: Menerapkan dan menganalisis algoritma unsupervised learning |
| **Sub-CPMK** | 9.1 Menerapkan algoritma clustering (K-Means, Hierarchical, DBSCAN) pada dataset nyata |
| | 9.2 Menganalisis dan membandingkan hasil clustering menggunakan metrik evaluasi yang tepat |
| **Bloom's Taxonomy** | C3-C4 (Menerapkan-Menganalisis / *Apply-Analyze*) |
| **Durasi** | 2 x 100 menit (Teori 100 min + Praktikum 100 min) |
| **Platform** | Google Colab |
| **Metode** | Ceramah interaktif, demonstrasi, hands-on coding, diskusi kelompok |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Membedakan** paradigma supervised dan unsupervised learning serta mengidentifikasi kapan masing-masing digunakan.
2. **Menjelaskan** konsep clustering dan berbagai algoritma utamanya (K-Means, Hierarchical Clustering, DBSCAN).
3. **Menerapkan** algoritma K-Means Clustering pada dataset nyata menggunakan scikit-learn.
4. **Menganalisis** kualitas clustering menggunakan *elbow method* dan *silhouette score*.
5. **Membandingkan** kelebihan dan kelemahan algoritma clustering yang berbeda berdasarkan karakteristik data.
6. **Mengimplementasikan** segmentasi pelanggan e-commerce Indonesia sebagai studi kasus nyata.

---

## Materi Pembelajaran

### 1. Supervised vs Unsupervised Learning: Perbedaan Utama

#### Paradigma Pembelajaran dalam Machine Learning

Hingga minggu lalu, kita telah mempelajari algoritma **supervised learning** — di mana model belajar dari data berlabel (*labeled data*). Pada unsupervised learning, kita menghadapi tantangan berbeda: **data tidak memiliki label**.

| Aspek | Supervised Learning | Unsupervised Learning |
|---|---|---|
| **Data** | Berlabel (*labeled*) | Tidak berlabel (*unlabeled*) |
| **Tujuan** | Prediksi label/nilai baru | Menemukan pola/struktur tersembunyi |
| **Output** | Kelas (klasifikasi) atau nilai (regresi) | Cluster, dimensi baru, asosiasi |
| **Evaluasi** | Accuracy, precision, recall, MSE | Silhouette score, inertia, visual |
| **Contoh** | Deteksi spam, prediksi harga | Segmentasi pelanggan, deteksi anomali |
| **Algoritma** | KNN, Decision Tree, SVM, Regresi | K-Means, DBSCAN, PCA, Apriori |

```
Supervised Learning:
  Input (X) + Label (y) → Model → Prediksi label baru

Unsupervised Learning:
  Input (X) saja → Model → Pola / Struktur tersembunyi
```

> **Analogi:** Supervised learning seperti belajar dengan guru yang memberikan jawaban benar. Unsupervised learning seperti mengamati pola sendiri tanpa diberi tahu jawabannya — misalnya mengelompokkan buah-buahan berdasarkan warna dan ukuran tanpa diberi tahu nama buahnya.

---

### 2. Clustering: Apa, Mengapa, dan Kapan

#### Apa Itu Clustering?

**Clustering** adalah teknik unsupervised learning yang bertujuan mengelompokkan data menjadi beberapa kelompok (*cluster*) di mana:
- Data dalam satu cluster **mirip** satu sama lain (*high intra-cluster similarity*)
- Data antar cluster **berbeda** satu sama lain (*low inter-cluster similarity*)

#### Mengapa Clustering Penting?

- **Eksplorasi data:** Menemukan pola tersembunyi dalam data besar
- **Segmentasi:** Mengelompokkan pelanggan, produk, atau dokumen
- **Preprocessing:** Sebagai langkah awal sebelum analisis lanjutan
- **Deteksi anomali:** Mengidentifikasi data yang tidak masuk cluster manapun

#### Kapan Menggunakan Clustering?

- Ketika data **tidak memiliki label** dan kita ingin menemukan struktur
- Ketika kita ingin **mengelompokkan** entitas serupa
- Ketika kita ingin melakukan **eksplorasi awal** pada dataset baru
- Ketika label terlalu mahal atau sulit didapatkan

#### Contoh Penerapan di Indonesia

| Domain | Contoh Clustering |
|---|---|
| **E-commerce** | Segmentasi pelanggan Tokopedia/Shopee berdasarkan perilaku belanja |
| **Perbankan** | Pengelompokan nasabah berdasarkan profil risiko kredit |
| **Kesehatan** | Klasterisasi puskesmas berdasarkan kinerja layanan |
| **Pendidikan** | Pengelompokan sekolah berdasarkan indikator mutu |
| **Geografi** | Klasterisasi desa berdasarkan indeks pembangunan |

---

### 3. K-Means Clustering: Algoritma, Centroid, dan Iterasi

#### Konsep Dasar K-Means

**K-Means** adalah algoritma clustering paling populer dan intuitif. Ide dasarnya sederhana:

1. Tentukan jumlah cluster **K** yang diinginkan
2. Tempatkan **K centroid** secara acak
3. Setiap data point di-assign ke centroid terdekat
4. Hitung ulang posisi centroid berdasarkan rata-rata anggota cluster
5. Ulangi langkah 3-4 hingga konvergen (centroid tidak berubah lagi)

```
Algoritma K-Means:
1. Inisialisasi K centroid secara acak
2. REPEAT:
   a. Assignment: Setiap data → centroid terdekat
   b. Update: Centroid = rata-rata anggota cluster
3. UNTIL centroid tidak berubah (konvergen)
```

#### Ilustrasi Visual (K=3)

```
Iterasi 0 (Random):     Iterasi 1:              Iterasi Final:
    *                       *                       *
  . . .  X              . . .  X                . . . X
 .   .   .             .   .   .               .   .  .
. . . . .  .          . . . . .  .            . . . . . .
    X                     X                       X
 .  .  .  .            .  .  .  .              .  .  . .
. .  .  . .           . .  .  . .             . .  . . .
      X                     X                       X

*X = centroid, . = data point
```

#### Fungsi Objektif: Inertia (WCSS)

K-Means meminimalkan **Within-Cluster Sum of Squares (WCSS)** atau **inertia**:

$$\text{WCSS} = \sum_{i=1}^{K} \sum_{x \in C_i} ||x - \mu_i||^2$$

Di mana $\mu_i$ adalah centroid cluster $C_i$.

#### Kelebihan dan Keterbatasan K-Means

| Kelebihan | Keterbatasan |
|---|---|
| Sederhana dan mudah dipahami | Harus menentukan K di awal |
| Cepat secara komputasi (O(nKt)) | Sensitif terhadap inisialisasi centroid |
| Scalable untuk data besar | Hanya menemukan cluster berbentuk spherical |
| Hasil mudah diinterpretasi | Sensitif terhadap outlier |

---

### 4. Memilih K: Elbow Method dan Silhouette Score

#### Elbow Method

Elbow method memplot nilai **inertia (WCSS)** untuk berbagai nilai K. Titik di mana penurunan WCSS mulai melandai membentuk "siku" (*elbow*) — itulah K optimal.

```
WCSS
 |
 |*
 | *
 |  *
 |   *
 |    *___________  ← Elbow point (K optimal)
 |         *  *  *
 |__________________ K
 1  2  3  4  5  6  7
```

#### Silhouette Score

**Silhouette score** mengukur seberapa mirip data terhadap clusternya sendiri dibandingkan cluster terdekat:

$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$

Di mana:
- $a(i)$ = rata-rata jarak ke data lain dalam cluster yang sama
- $b(i)$ = rata-rata jarak ke data di cluster terdekat

**Interpretasi:**
- **s = 1:** Data sangat cocok di clusternya
- **s = 0:** Data berada di batas antar cluster
- **s = -1:** Data mungkin salah cluster

---

### 5. Hierarchical Clustering: Agglomerative dan Dendrogram

#### Konsep Hierarchical Clustering

Berbeda dengan K-Means, **Hierarchical Clustering** membangun hierarki cluster secara bertahap. Ada dua pendekatan:

- **Agglomerative (bottom-up):** Mulai dari setiap data sebagai cluster individual, lalu gabungkan yang terdekat secara bertahap
- **Divisive (top-down):** Mulai dari satu cluster besar, lalu bagi secara bertahap

Yang paling umum digunakan adalah pendekatan **agglomerative**.

#### Linkage Methods

Bagaimana mengukur jarak antar cluster?

| Metode | Deskripsi |
|---|---|
| **Single Linkage** | Jarak minimum antar anggota dua cluster |
| **Complete Linkage** | Jarak maksimum antar anggota dua cluster |
| **Average Linkage** | Rata-rata jarak antar semua pasangan anggota |
| **Ward's Linkage** | Meminimalkan peningkatan variance setelah penggabungan |

#### Dendrogram

**Dendrogram** adalah visualisasi hierarki penggabungan cluster. Sumbu vertikal menunjukkan jarak (*distance*) saat penggabungan terjadi.

```
Jarak
  |     ┌───────┐
  |   ┌─┤       ├─┐
  |   │ └─┐   ┌─┘ │
  |   │   │   │   │
  | ┌─┤ ┌─┤ ┌─┤   │
  | │ │ │ │ │ │   │
  ──A─B─C─D─E─F───G─── Data points

→ Memotong dendrogram di ketinggian tertentu menentukan jumlah cluster
```

#### Kelebihan Hierarchical Clustering

- **Tidak perlu menentukan K** di awal
- Menghasilkan **visualisasi dendrogram** yang informatif
- Cocok untuk data dengan **hierarki alami**

---

### 6. DBSCAN: Density-Based Clustering

#### Konsep DBSCAN

**DBSCAN** (*Density-Based Spatial Clustering of Applications with Noise*) mengelompokkan data berdasarkan **kepadatan** (*density*), bukan jarak ke centroid.

#### Parameter Utama

- **eps (ε):** Radius lingkaran di sekitar data point
- **min_samples:** Jumlah minimum data point dalam radius eps untuk membentuk *core point*

#### Klasifikasi Data Point

```
Legend: ● Core point  ○ Border point  × Noise

   ○ ● ● ○
   ● ● ●          ← Cluster 1
   ○ ● ○

       ×           ← Noise (outlier)

      ● ● ○
      ● ● ●       ← Cluster 2
      ○ ● ○
```

- **Core point:** Memiliki ≥ min_samples titik dalam radius eps
- **Border point:** Dalam radius eps dari core point, tapi sendiri tidak memenuhi syarat core
- **Noise:** Tidak termasuk cluster manapun

#### Kelebihan DBSCAN

| Kelebihan | Keterbatasan |
|---|---|
| Tidak perlu menentukan K | Sensitif terhadap eps dan min_samples |
| Bisa menemukan cluster bentuk bebas | Sulit untuk data dengan kepadatan bervariasi |
| Mendeteksi outlier otomatis | Kurang efektif di ruang dimensi tinggi |
| Robust terhadap outlier | |

---

### 7. Perbandingan Algoritma Clustering

| Aspek | K-Means | Hierarchical | DBSCAN |
|---|---|---|---|
| **Jumlah K** | Harus ditentukan | Ditentukan setelah | Otomatis |
| **Bentuk Cluster** | Spherical | Bebas (tergantung linkage) | Bebas |
| **Outlier** | Sensitif | Tergantung metode | Mendeteksi otomatis |
| **Skalabilitas** | Sangat baik | Buruk (O(n³)) | Baik |
| **Interpretabilitas** | Tinggi (centroid) | Tinggi (dendrogram) | Sedang |
| **Kapan Digunakan** | Data besar, cluster bulat | Perlu hierarki, data kecil | Cluster bentuk bebas, ada noise |

> **Tips Praktis:** Mulailah dengan K-Means karena cepat dan mudah. Jika hasilnya kurang baik (cluster tidak bulat, banyak noise), coba DBSCAN. Gunakan Hierarchical Clustering jika ingin memahami struktur hierarki data.

---

### 8. Konteks Indonesia: Segmentasi Pelanggan E-Commerce

#### Studi Kasus: Segmentasi Pelanggan

Dalam industri e-commerce Indonesia yang berkembang pesat (Tokopedia, Shopee, Bukalapak, Lazada), segmentasi pelanggan sangat penting untuk:

- **Personalisasi marketing:** Mengirim promosi yang tepat ke segmen yang tepat
- **Alokasi resources:** Fokus pada segmen pelanggan paling bernilai
- **Product development:** Memahami kebutuhan berbeda tiap segmen
- **Retention strategy:** Strategi retensi berbeda untuk setiap segmen

#### RFM Analysis

Salah satu pendekatan populer untuk segmentasi pelanggan adalah **RFM Analysis**:

| Dimensi | Deskripsi | Interpretasi |
|---|---|---|
| **Recency (R)** | Berapa lama sejak transaksi terakhir | Semakin baru = semakin baik |
| **Frequency (F)** | Berapa kali bertransaksi | Semakin sering = semakin loyal |
| **Monetary (M)** | Total nilai transaksi | Semakin besar = semakin bernilai |

Dengan melakukan K-Means clustering pada fitur RFM, kita bisa mengidentifikasi segmen seperti:
- **Champions:** Recency tinggi, Frequency tinggi, Monetary tinggi
- **Loyal Customers:** Frequency tinggi tapi Monetary sedang
- **At Risk:** Recency rendah (lama tidak transaksi) tapi pernah aktif
- **Hibernating:** Sudah lama tidak aktif

---

## Aktivitas Kelas

### Sesi 1: Teori dan Diskusi (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Pembukaan & Review | Review supervised learning, transisi ke unsupervised |
| 15 menit | Ceramah: Supervised vs Unsupervised | Perbedaan paradigma, kapan digunakan |
| 20 menit | Ceramah: K-Means Clustering | Algoritma, centroid, iterasi, demo visual |
| 15 menit | Ceramah: Memilih K | Elbow method, silhouette score, interpretasi |
| 15 menit | Ceramah: Hierarchical & DBSCAN | Dendrogram, density-based, perbandingan |
| 15 menit | Diskusi Kelompok | Studi kasus segmentasi pelanggan e-commerce Indonesia |
| 10 menit | Rangkuman & Transisi | Key takeaways, persiapan hands-on |

### Sesi 2: Hands-on Praktikum (100 menit)

| Waktu | Aktivitas | Deskripsi |
|---|---|---|
| 10 menit | Setup & Load Data | Buka Google Colab, import libraries, load dataset |
| 25 menit | K-Means Clustering | Implementasi K-Means, elbow method, silhouette |
| 20 menit | Hierarchical Clustering | Dendrogram, agglomerative clustering |
| 20 menit | DBSCAN | Implementasi DBSCAN, deteksi noise |
| 15 menit | Perbandingan Visual | Membandingkan hasil tiga algoritma |
| 10 menit | Wrap-up & Preview | Rangkuman, penjelasan tugas, preview minggu depan |

---

## Hands-on: Clustering pada Data Pelanggan E-Commerce Indonesia

### Langkah 1: Import Library dan Persiapan Data

```python
# Import library yang diperlukan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage
import warnings
warnings.filterwarnings('ignore')

# Mengatur style visualisasi
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
print("Library berhasil di-import!")
```

### Langkah 2: Membuat Dataset Pelanggan E-Commerce Indonesia

```python
# Simulasi data pelanggan e-commerce Indonesia (RFM)
np.random.seed(42)
n_customers = 200

# Membuat segmen pelanggan secara simulasi
data = {
    'customer_id': [f'CUST-{i:04d}' for i in range(1, n_customers + 1)],
    'kota': np.random.choice(
        ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Semarang',
         'Makassar', 'Yogyakarta', 'Palembang', 'Denpasar', 'Malang'],
        n_customers
    ),
}

# Segmen 1: Champions (pembelian baru, sering, nilai tinggi)
seg1 = 50
# Segmen 2: Loyal (cukup sering, nilai sedang)
seg2 = 60
# Segmen 3: At Risk (sudah lama, jarang, nilai rendah-sedang)
seg3 = 50
# Segmen 4: New/Casual (baru tapi jarang, nilai rendah)
seg4 = 40

recency = np.concatenate([
    np.random.randint(1, 15, seg1),     # Champions: baru-baru ini
    np.random.randint(10, 40, seg2),    # Loyal: cukup baru
    np.random.randint(60, 120, seg3),   # At Risk: sudah lama
    np.random.randint(5, 30, seg4)      # New/Casual: relatif baru
])

frequency = np.concatenate([
    np.random.randint(15, 40, seg1),    # Champions: sangat sering
    np.random.randint(8, 20, seg2),     # Loyal: cukup sering
    np.random.randint(2, 8, seg3),      # At Risk: jarang
    np.random.randint(1, 5, seg4)       # New/Casual: sangat jarang
])

monetary = np.concatenate([
    np.random.randint(2000000, 10000000, seg1),   # Champions: tinggi
    np.random.randint(500000, 3000000, seg2),     # Loyal: sedang
    np.random.randint(200000, 1500000, seg3),     # At Risk: rendah-sedang
    np.random.randint(50000, 500000, seg4)        # New/Casual: rendah
])

data['recency_days'] = recency
data['frequency'] = frequency
data['monetary_rp'] = monetary

df = pd.DataFrame(data)
print(f"Dataset: {df.shape[0]} pelanggan, {df.shape[1]} kolom")
print("\n=== 5 Data Pertama ===")
print(df.head())
print("\n=== Statistik Deskriptif (RFM) ===")
print(df[['recency_days', 'frequency', 'monetary_rp']].describe())
```

### Langkah 3: Preprocessing — Standardisasi Fitur

```python
# Pilih fitur RFM untuk clustering
fitur_rfm = ['recency_days', 'frequency', 'monetary_rp']
X = df[fitur_rfm].values

# Standardisasi fitur (penting untuk clustering!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("=== Sebelum Standardisasi ===")
print(f"Mean: {X.mean(axis=0)}")
print(f"Std:  {X.std(axis=0)}")
print()
print("=== Sesudah Standardisasi ===")
print(f"Mean: {X_scaled.mean(axis=0).round(4)}")
print(f"Std:  {X_scaled.std(axis=0).round(4)}")
print()
print("Catatan: Setelah standardisasi, semua fitur memiliki skala yang sama")
print("(mean ≈ 0, std ≈ 1). Ini penting agar fitur dengan skala besar")
print("(seperti monetary dalam jutaan) tidak mendominasi clustering.")
```

### Langkah 4: K-Means — Elbow Method untuk Menentukan K

```python
# Elbow Method: mencari K optimal
inertias = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

# Visualisasi Elbow Method
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(K_range, inertias, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Jumlah Cluster (K)', fontsize=12)
plt.ylabel('Inertia (WCSS)', fontsize=12)
plt.title('Elbow Method', fontsize=14)
plt.xticks(K_range)
plt.grid(True, alpha=0.3)

# Silhouette Score untuk berbagai K
silhouette_scores = []
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    silhouette_scores.append(score)

plt.subplot(1, 2, 2)
plt.plot(K_range, silhouette_scores, 'ro-', linewidth=2, markersize=8)
plt.xlabel('Jumlah Cluster (K)', fontsize=12)
plt.ylabel('Silhouette Score', fontsize=12)
plt.title('Silhouette Score per K', fontsize=14)
plt.xticks(K_range)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.suptitle('Menentukan Jumlah Cluster Optimal', fontsize=14, y=1.02)
plt.show()

# Tampilkan nilai numerik
print("\n=== Silhouette Score per K ===")
for k, score in zip(K_range, silhouette_scores):
    marker = " ← terbaik" if score == max(silhouette_scores) else ""
    print(f"K={k}: {score:.4f}{marker}")
```

### Langkah 5: K-Means Clustering dengan K Optimal

```python
# Implementasi K-Means dengan K=4
K_OPTIMAL = 4
kmeans = KMeans(n_clusters=K_OPTIMAL, random_state=42, n_init=10)
df['cluster_kmeans'] = kmeans.fit_predict(X_scaled)

# Analisis setiap cluster
print("=== Profil Setiap Cluster (K-Means) ===\n")
for i in range(K_OPTIMAL):
    cluster_data = df[df['cluster_kmeans'] == i]
    print(f"--- Cluster {i} ({len(cluster_data)} pelanggan) ---")
    print(f"  Recency  : {cluster_data['recency_days'].mean():.1f} hari (rata-rata)")
    print(f"  Frequency: {cluster_data['frequency'].mean():.1f} kali")
    print(f"  Monetary : Rp {cluster_data['monetary_rp'].mean():,.0f}")
    print(f"  Kota terbanyak: {cluster_data['kota'].value_counts().index[0]}")
    print()

# Visualisasi hasil clustering (2D: Frequency vs Monetary)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
scatter = plt.scatter(df['frequency'], df['monetary_rp'] / 1_000_000,
                       c=df['cluster_kmeans'], cmap='viridis',
                       alpha=0.6, edgecolors='black', linewidth=0.5)
plt.xlabel('Frequency (jumlah transaksi)', fontsize=12)
plt.ylabel('Monetary (juta Rp)', fontsize=12)
plt.title('K-Means: Frequency vs Monetary', fontsize=13)
plt.colorbar(scatter, label='Cluster')

plt.subplot(1, 2, 2)
scatter = plt.scatter(df['recency_days'], df['frequency'],
                       c=df['cluster_kmeans'], cmap='viridis',
                       alpha=0.6, edgecolors='black', linewidth=0.5)
plt.xlabel('Recency (hari sejak transaksi terakhir)', fontsize=12)
plt.ylabel('Frequency (jumlah transaksi)', fontsize=12)
plt.title('K-Means: Recency vs Frequency', fontsize=13)
plt.colorbar(scatter, label='Cluster')

plt.tight_layout()
plt.show()
```

### Langkah 6: Hierarchical Clustering dan Dendrogram

```python
# Dendrogram untuk melihat hierarki clustering
plt.figure(figsize=(14, 6))

# Menghitung linkage matrix
linked = linkage(X_scaled, method='ward')

# Membuat dendrogram
dendrogram(linked,
           truncate_mode='lastp',
           p=30,  # Tampilkan 30 node terakhir
           leaf_font_size=8,
           show_contracted=True)

plt.title('Dendrogram — Hierarchical Clustering (Ward Linkage)', fontsize=14)
plt.xlabel('Data Points', fontsize=12)
plt.ylabel('Jarak (Distance)', fontsize=12)
plt.axhline(y=8, color='r', linestyle='--', label='Cut-off untuk 4 cluster')
plt.legend()
plt.tight_layout()
plt.show()

# Agglomerative Clustering dengan 4 cluster
agg_clustering = AgglomerativeClustering(n_clusters=4, linkage='ward')
df['cluster_hierarchical'] = agg_clustering.fit_predict(X_scaled)

print("\n=== Perbandingan Ukuran Cluster ===")
print("\nK-Means:")
print(df['cluster_kmeans'].value_counts().sort_index())
print("\nHierarchical:")
print(df['cluster_hierarchical'].value_counts().sort_index())
```

### Langkah 7: DBSCAN Clustering

```python
# DBSCAN Clustering
dbscan = DBSCAN(eps=0.8, min_samples=5)
df['cluster_dbscan'] = dbscan.fit_predict(X_scaled)

# Cluster -1 berarti noise (outlier)
n_clusters = len(set(df['cluster_dbscan'])) - (1 if -1 in df['cluster_dbscan'].values else 0)
n_noise = list(df['cluster_dbscan']).count(-1)

print(f"=== Hasil DBSCAN ===")
print(f"Jumlah cluster ditemukan: {n_clusters}")
print(f"Jumlah noise points: {n_noise}")
print(f"\nDistribusi cluster:")
print(df['cluster_dbscan'].value_counts().sort_index())
```

### Langkah 8: Perbandingan Visual Tiga Algoritma

```python
# Perbandingan visual hasil tiga algoritma
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# K-Means
axes[0].scatter(df['frequency'], df['monetary_rp'] / 1_000_000,
                c=df['cluster_kmeans'], cmap='viridis',
                alpha=0.6, edgecolors='black', linewidth=0.5)
axes[0].set_title('K-Means (K=4)', fontsize=13)
axes[0].set_xlabel('Frequency')
axes[0].set_ylabel('Monetary (juta Rp)')

# Hierarchical
axes[1].scatter(df['frequency'], df['monetary_rp'] / 1_000_000,
                c=df['cluster_hierarchical'], cmap='viridis',
                alpha=0.6, edgecolors='black', linewidth=0.5)
axes[1].set_title('Hierarchical (Ward, K=4)', fontsize=13)
axes[1].set_xlabel('Frequency')
axes[1].set_ylabel('Monetary (juta Rp)')

# DBSCAN
colors = df['cluster_dbscan'].copy()
axes[2].scatter(df['frequency'], df['monetary_rp'] / 1_000_000,
                c=colors, cmap='viridis',
                alpha=0.6, edgecolors='black', linewidth=0.5)
axes[2].set_title(f'DBSCAN (eps=0.8, min_samples=5)', fontsize=13)
axes[2].set_xlabel('Frequency')
axes[2].set_ylabel('Monetary (juta Rp)')

plt.suptitle('Perbandingan Hasil Clustering pada Data E-Commerce', fontsize=15, y=1.02)
plt.tight_layout()
plt.show()

# Silhouette score perbandingan (hanya untuk K-Means dan Hierarchical)
sil_kmeans = silhouette_score(X_scaled, df['cluster_kmeans'])
sil_hier = silhouette_score(X_scaled, df['cluster_hierarchical'])

# DBSCAN: hanya hitung jika ada lebih dari 1 cluster dan tidak semua noise
valid_mask = df['cluster_dbscan'] != -1
if len(set(df.loc[valid_mask, 'cluster_dbscan'])) > 1:
    sil_dbscan = silhouette_score(X_scaled[valid_mask], df.loc[valid_mask, 'cluster_dbscan'])
else:
    sil_dbscan = float('nan')

print("\n=== Silhouette Score Perbandingan ===")
print(f"K-Means:      {sil_kmeans:.4f}")
print(f"Hierarchical: {sil_hier:.4f}")
print(f"DBSCAN:       {sil_dbscan:.4f}")
```

### Langkah 9: Interpretasi Bisnis — Penamaan Segmen

```python
# Interpretasi bisnis: beri nama segmen berdasarkan profil RFM
print("=== Interpretasi Segmen Pelanggan (K-Means) ===\n")

for i in range(K_OPTIMAL):
    cluster_data = df[df['cluster_kmeans'] == i]
    avg_r = cluster_data['recency_days'].mean()
    avg_f = cluster_data['frequency'].mean()
    avg_m = cluster_data['monetary_rp'].mean()

    # Beri label berdasarkan profil RFM
    if avg_r < 20 and avg_f > 15 and avg_m > 2_000_000:
        label = "Champions (Pelanggan Setia)"
        strategy = "Berikan reward eksklusif, program loyalty premium"
    elif avg_f > 8 and avg_m > 500_000:
        label = "Loyal Customers (Pelanggan Loyal)"
        strategy = "Upselling, cross-selling, diskon khusus"
    elif avg_r > 50:
        label = "At Risk (Berisiko Churn)"
        strategy = "Win-back campaign, diskon besar, survey kepuasan"
    else:
        label = "New/Casual (Pelanggan Baru/Kasual)"
        strategy = "Onboarding, welcome offer, edukasi produk"

    print(f"Cluster {i}: {label}")
    print(f"  Jumlah: {len(cluster_data)} pelanggan")
    print(f"  Avg Recency: {avg_r:.0f} hari | Freq: {avg_f:.0f} kali | "
          f"Monetary: Rp {avg_m:,.0f}")
    print(f"  Strategi: {strategy}")
    print()
```

---

## AI Corner: Menggunakan AI untuk Menginterpretasi Hasil Clustering

> **Level: Intermediate-Advanced** — Pada minggu ini, kita menggunakan AI tidak hanya untuk coding, tetapi juga untuk **menginterpretasi** hasil analisis.

### Skenario Penggunaan AI dalam Clustering

| Skenario | Contoh Prompt ke AI |
|---|---|
| Memilih algoritma | *"Saya punya data pelanggan 10.000 baris dengan fitur RFM. Algoritma clustering mana yang paling cocok dan mengapa?"* |
| Menentukan K | *"Berikut plot elbow method saya [paste]. Menurut kamu K berapa yang optimal? Jelaskan alasannya."* |
| Interpretasi cluster | *"Berikut profil 4 cluster pelanggan saya [paste profil]. Berikan nama dan strategi bisnis untuk setiap segmen."* |
| Debugging | *"DBSCAN saya menghasilkan semua data sebagai noise. Parameter eps=0.5, min_samples=10. Apa yang salah?"* |
| Visualisasi | *"Buatkan kode Python untuk visualisasi 3D dari hasil K-Means clustering dengan matplotlib."* |

### Contoh Prompt untuk Interpretasi Cluster

```
Saya melakukan K-Means clustering (K=4) pada data pelanggan e-commerce Indonesia
dengan fitur RFM (Recency, Frequency, Monetary). Berikut profil setiap cluster:

Cluster 0: Recency 8 hari, Frequency 25 kali, Monetary Rp 5.500.000
Cluster 1: Recency 25 hari, Frequency 13 kali, Monetary Rp 1.200.000
Cluster 2: Recency 85 hari, Frequency 4 kali, Monetary Rp 750.000
Cluster 3: Recency 15 hari, Frequency 3 kali, Monetary Rp 250.000

Tolong:
1. Berikan nama bisnis yang tepat untuk setiap segmen
2. Jelaskan karakteristik masing-masing segmen
3. Rekomendasikan strategi marketing untuk setiap segmen
4. Segmen mana yang perlu perhatian khusus?
```

### Tips Penting

1. **Selalu validasi** interpretasi AI dengan domain knowledge Anda.
2. **Jangan langsung percaya** rekomendasi AI tanpa memahami konteks bisnis.
3. **AI sangat baik** untuk brainstorming nama segmen dan strategi, tapi keputusan akhir tetap di tangan analis.
4. **Dokumentasikan** prompt dan respons AI yang Anda gunakan.

---

## Refleksi dan Diskusi

Jawab pertanyaan-pertanyaan berikut sebagai bahan refleksi:

1. **Supervised vs Unsupervised:** Dalam skenario apa Anda akan memilih unsupervised learning dibanding supervised learning? Berikan contoh nyata dari konteks Indonesia.

2. **Pemilihan Algoritma:** Jika Anda memiliki data pelanggan GoTo (Gojek + Tokopedia) dengan jutaan baris, algoritma clustering mana yang akan Anda pilih? Mengapa?

3. **Etika Segmentasi:** Segmentasi pelanggan dapat digunakan untuk memberikan harga berbeda (*price discrimination*). Bagaimana menurut Anda dari perspektif etika dan nilai keadilan (al-'adl)?

4. **Interpretasi vs Algoritma:** Mengapa interpretasi bisnis dari hasil clustering sama pentingnya — bahkan mungkin lebih penting — daripada algoritma yang digunakan?

5. **Noise dan Outlier:** DBSCAN mengklasifikasikan beberapa data sebagai noise. Dalam konteks bisnis, apakah noise selalu buruk? Mungkinkah noise justru pelanggan yang menarik?

---

## Tugas Mandiri — T5: Clustering pada Dataset E-Commerce Indonesia

### Deskripsi Tugas

Lakukan analisis clustering pada dataset e-commerce Indonesia dengan langkah-langkah berikut:

1. **Dataset:** Gunakan dataset yang disediakan di Google Colab (atau buat simulasi data e-commerce Indonesia dengan minimal 300 baris dan 5 fitur numerik).

2. **Preprocessing:**
   - Lakukan eksplorasi data awal (statistik deskriptif, distribusi)
   - Tangani missing values dan outlier jika ada
   - Standardisasi fitur menggunakan StandardScaler

3. **Clustering:**
   - Terapkan K-Means dengan elbow method dan silhouette score
   - Terapkan Hierarchical Clustering dengan dendrogram
   - Terapkan DBSCAN dengan parameter yang tepat

4. **Evaluasi & Perbandingan:**
   - Bandingkan hasil ketiga algoritma
   - Hitung silhouette score untuk masing-masing
   - Buat visualisasi perbandingan

5. **Interpretasi Bisnis:**
   - Berikan nama segmen untuk setiap cluster
   - Rekomendasikan strategi bisnis untuk setiap segmen
   - Jelaskan segmen mana yang paling bernilai dan mengapa

### Ketentuan Pengumpulan

- **Format:** Notebook Google Colab (.ipynb)
- **Deadline:** Minggu 10 (sebelum perkuliahan)
- **Bobot:** Bagian dari komponen Tugas Individu
- **AI Policy:** Penggunaan AI diizinkan dengan mencantumkan log penggunaan AI

---

## Referensi

### Buku Teks

1. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media. — Chapter 9: Unsupervised Learning Techniques.
2. Müller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*. O'Reilly Media. — Chapter 3: Unsupervised Learning.
3. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2nd ed.). Springer. — Chapter 12: Unsupervised Learning.

### Sumber Online

4. [scikit-learn: Clustering](https://scikit-learn.org/stable/modules/clustering.html) — Dokumentasi resmi algoritma clustering di scikit-learn.
5. [Google Developers: Clustering](https://developers.google.com/machine-learning/clustering) — Tutorial interaktif clustering dari Google.
6. [Towards Data Science: Customer Segmentation](https://towardsdatascience.com/customer-segmentation-using-k-means-clustering-d33964f238c3) — Tutorial segmentasi pelanggan dengan K-Means.

### Referensi Indonesia

7. Data BPS — Badan Pusat Statistik Indonesia. [https://www.bps.go.id/](https://www.bps.go.id/)
8. iPrice Group — Laporan E-Commerce Indonesia. [https://iprice.co.id/](https://iprice.co.id/)

---

> **Preview Minggu Depan:** Kita akan membahas **Dimensionality Reduction dan Feature Selection** — mempelajari PCA untuk mereduksi dimensi data, serta teknik seleksi fitur untuk meningkatkan performa model.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
