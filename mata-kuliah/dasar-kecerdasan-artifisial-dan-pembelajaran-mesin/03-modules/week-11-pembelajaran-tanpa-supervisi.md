# Minggu 11: Pembelajaran Tanpa Supervisi

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 11 dari 16 |
| Topik | K-Means, *hierarchical clustering*, DBSCAN, metrik *clustering*, deteksi anomali |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-10 |
| Bloom | C3 (Menerapkan) → C4 (Menganalisis) |
| Durasi | 150 menit |
| Metode | Kuliah · Praktikum · Interpretasi kelompok |
| Penilaian | Observasi (Lab 11) · **Milestone proyek 2 (P-02)** |

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Menerapkan** (C3) K-Means, *hierarchical clustering*, dan DBSCAN pada data nyata.
2. **Menentukan** (C5) jumlah klaster dengan metode *elbow* dan *silhouette*.
3. **Menghitung** (C3) dan **menafsirkan** (C4) metrik *silhouette*, Davies-Bouldin, dan Calinski-Harabasz.
4. **Menafsirkan** (C4) hasil *clustering* secara substantif, bukan sekadar sebagai nomor klaster.
5. **Menerapkan** (C3) deteksi anomali untuk pengamatan yang tak lazim.

---

## Materi Pembelajaran

### 11.1 Kesulitan Pokok Pembelajaran Tanpa Supervisi

Pada pembelajaran terbimbing, ada jawaban benar untuk dibandingkan. Di sini tidak ada. Akibatnya:

| Persoalan | Konsekuensi |
|-----------|-------------|
| Tidak ada "benar" atau "salah" | Evaluasi bergantung pada ukuran tak langsung dan penilaian manusia |
| Hasil bergantung pada pilihan jarak dan penskalaan | Keputusan teknis mengubah struktur yang ditemukan |
| Jumlah klaster harus ditentukan | Biasanya tidak diketahui sebelumnya |
| Klaster yang ditemukan mungkin tidak bermakna | **Interpretasi substantif wajib** |

> **Kaidah mata kuliah ini:** hasil *clustering* yang hanya dilaporkan sebagai "klaster 0, klaster 1, klaster 2" tanpa penafsiran substantif dinilai belum selesai. Pekerjaan *clustering* baru selesai ketika setiap klaster dapat diberi nama dan dijelaskan artinya.

---

### 11.2 K-Means

#### 11.2.1 Algoritmanya

```
  1. Tentukan k; tempatkan k pusat awal (k-means++)
  2. ULANGI sampai stabil:
       a. Tetapkan setiap titik ke pusat terdekat
       b. Pindahkan setiap pusat ke rata-rata anggotanya
  3. Selesai ketika penetapan tidak lagi berubah
```

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# PENSKALAAN WAJIB — K-Means berbasis jarak Euclidean
model = Pipeline([
    ("skala", StandardScaler()),
    ("kmeans", KMeans(n_clusters=4, n_init=10, random_state=42)),
])
label = model.fit_predict(X)
```

| Parameter | Peran |
|-----------|-------|
| `n_clusters` | Jumlah klaster — **wajib ditentukan** |
| `n_init` | Berapa kali diulang dengan pusat awal berbeda; ambil yang terbaik |
| `init="k-means++"` | Penempatan pusat awal yang cerdas (baku) |

#### 11.2.2 Asumsi dan Batasnya

| Asumsi K-Means | Akibat bila dilanggar |
|----------------|-----------------------|
| Klaster berbentuk bulat | Klaster memanjang atau melengkung terpotong salah |
| Klaster berukuran sebanding | Klaster kecil terserap ke klaster besar |
| Kerapatan sebanding | Daerah renggang terbagi sembarang |
| Tidak ada pencilan berat | Pusat tertarik ke pencilan |

Untuk data yang melanggar asumsi ini, DBSCAN atau *hierarchical clustering* lebih sesuai.

---

### 11.3 Menentukan Jumlah Klaster

#### 11.3.1 Metode *Elbow*

```python
import matplotlib.pyplot as plt

inersia = []
rentang_k = range(2, 11)
for k in rentang_k:
    km = Pipeline([("skala", StandardScaler()),
                   ("kmeans", KMeans(n_clusters=k, n_init=10, random_state=42))])
    km.fit(X)
    inersia.append(km.named_steps["kmeans"].inertia_)

plt.plot(rentang_k, inersia, "o-")
plt.xlabel("Jumlah klaster (k)"); plt.ylabel("Inersia (WCSS)")
plt.title("Metode Elbow")
```

```
  Inersia
     ▲
     │ ●
     │  ╲
     │   ●
     │    ╲
     │     ●      ← "siku": penambahan k setelah ini
     │      ╲___     memberi perbaikan yang kecil
     │          ●───●───●───●
     └──────────┴────────────────► k
                3
```

> **Keterbatasan:** siku sering tidak tegas. Metode *elbow* memberi petunjuk, bukan jawaban. Ia harus dipadukan dengan *silhouette* dan — yang paling menentukan — dengan pertimbangan apakah jumlah klaster itu **bermakna** bagi persoalannya.

#### 11.3.2 Analisis *Silhouette*

Untuk setiap titik $i$:

$$s(i) = \frac{b(i) - a(i)}{\max\{a(i),\, b(i)\}}$$

di mana $a(i)$ = rata-rata jarak ke anggota klasternya sendiri, dan $b(i)$ = rata-rata jarak ke anggota klaster terdekat berikutnya.

| $s(i)$ | Makna |
|--------|-------|
| Mendekati +1 | Titik jauh lebih dekat ke klasternya sendiri — penempatan baik |
| Sekitar 0 | Titik berada di perbatasan |
| Negatif | **Titik kemungkinan salah ditempatkan** |

```python
from sklearn.metrics import silhouette_score

for k in range(2, 11):
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    label = km.fit_predict(X_scaled)
    print(f"k={k}: silhouette = {silhouette_score(X_scaled, label):.3f}")
```

---

### 11.4 *Hierarchical Clustering*

Membangun hierarki klaster tanpa menetapkan k di awal.

```
   Jarak
     │        ┌─────────────┐
     │        │             │
     │    ┌───┴───┐     ┌───┴───┐
     │    │       │     │       │
     │  ┌─┴─┐   ┌─┴─┐ ┌─┴─┐   ┌─┴─┐
     │  A   B   C   D E   F   G   H
     └──────────────────────────────►
         Pemotongan pada ketinggian tertentu
         menentukan jumlah klaster
```

```python
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

hc = AgglomerativeClustering(n_clusters=4, linkage="ward")
label = hc.fit_predict(X_scaled)

# Dendrogram untuk melihat strukturnya
Z = linkage(X_scaled, method="ward")
dendrogram(Z, truncate_mode="lastp", p=20)
```

| *Linkage* | Jarak antarklaster | Kecenderungan |
|-----------|--------------------|---------------|
| `ward` | Minimalkan penambahan varians | **Klaster seimbang** — paling sering dipakai |
| `complete` | Jarak terjauh | Klaster padat |
| `average` | Rata-rata jarak | Kompromi |
| `single` | Jarak terdekat | Klaster memanjang; peka derau |

**Kelebihan:** dendrogram memperlihatkan struktur pada berbagai tingkat sekaligus — sering lebih informatif daripada satu penetapan k.
**Kekurangan:** kompleksitas $O(n^2)$ hingga $O(n^3)$; tidak sesuai untuk data besar.

---

### 11.5 DBSCAN

Mengelompokkan berdasarkan **kerapatan**, bukan jarak ke pusat.

```python
from sklearn.cluster import DBSCAN

db = DBSCAN(eps=0.5, min_samples=5)
label = db.fit_predict(X_scaled)

# Label -1 berarti derau/pencilan
print("Jumlah klaster:", len(set(label)) - (1 if -1 in label else 0))
print("Titik derau   :", (label == -1).sum())
```

| Parameter | Makna |
|-----------|-------|
| `eps` | Radius ketetanggaan |
| `min_samples` | Jumlah minimum titik agar suatu daerah disebut rapat |

| Kelebihan | Kekurangan |
|-----------|------------|
| **Jumlah klaster tidak perlu ditentukan** | Sangat peka terhadap `eps` |
| Menemukan klaster berbentuk sembarang | Kesulitan bila kerapatan antarklaster berbeda |
| **Mengenali pencilan secara eksplisit** | Sulit pada dimensi tinggi |

#### 11.5.1 Perbandingan Ketiga Metode

| Aspek | K-Means | Hierarchical | DBSCAN |
|-------|---------|--------------|--------|
| k ditentukan di awal | Ya | Tidak (dipotong kemudian) | **Tidak** |
| Bentuk klaster | Bulat | Fleksibel | **Sembarang** |
| Pencilan | Dipaksa masuk klaster | Dipaksa masuk klaster | **Ditandai sebagai derau** |
| Skala data besar | **Baik** | Buruk | Sedang |
| Kestabilan | Bergantung pusat awal | Deterministik | Deterministik |

---

### 11.6 Metrik Evaluasi *Clustering*

#### 11.6.1 Tanpa Label Sebenarnya (*Internal*)

| Metrik | Rentang | Arah baik | Yang diukur |
|--------|---------|-----------|-------------|
| **Silhouette** | [−1, 1] | Makin tinggi | Kerapatan dalam klaster vs pemisahan antarklaster |
| **Davies-Bouldin** | [0, ∞) | **Makin rendah** | Rasio sebaran dalam terhadap jarak antarklaster |
| **Calinski-Harabasz** | [0, ∞) | Makin tinggi | Rasio varians antarklaster terhadap dalam klaster |

```python
from sklearn.metrics import (silhouette_score, davies_bouldin_score,
                             calinski_harabasz_score)

print("Silhouette       :", silhouette_score(X_scaled, label).round(3))
print("Davies-Bouldin   :", davies_bouldin_score(X_scaled, label).round(3))
print("Calinski-Harabasz:", calinski_harabasz_score(X_scaled, label).round(1))
```

#### 11.6.2 Bila Label Sebenarnya Tersedia (*External*)

Dipakai untuk pengujian dan pembelajaran, bukan pada penerapan nyata:

| Metrik | Rentang |
|--------|---------|
| *Adjusted Rand Index* (ARI) | [−1, 1]; 0 = setara acak |
| *Normalized Mutual Information* (NMI) | [0, 1] |

#### 11.6.3 Metrik Tidak Menggantikan Penilaian Manusia

> Skor *silhouette* tinggi berarti klaster terpisah dengan baik **secara geometris**. Ia sama sekali tidak menjamin klaster itu **bermakna**. Data dapat terbagi rapi menjadi lima kelompok yang tidak berarti apa pun bagi persoalan yang sedang ditangani.

Karena itu evaluasi *clustering* selalu berjalan dua lapis:

1. **Lapis teknis:** metrik internal menunjukkan pemisahan yang layak.
2. **Lapis substantif:** setiap klaster dapat diberi nama, dijelaskan cirinya, dan dikaitkan dengan tindakan yang berbeda.

---

### 11.7 Menafsirkan Klaster

```python
# Ciri tiap klaster: rata-rata fitur asli (bukan yang sudah diskalakan)
profil = X.assign(klaster=label).groupby("klaster").mean().round(2)
print(profil.T)

# Ukuran tiap klaster
print(pd.Series(label).value_counts().sort_index())
```

**Contoh hasil segmentasi provinsi Indonesia berdasarkan indikator BPS:**

| Klaster | n | IPM | Kepadatan | % Pertanian | **Nama yang diberikan** |
|---------|---|-----|-----------|-------------|-------------------------|
| 0 | 6 | 76,2 | Tinggi | Rendah | **Perkotaan padat industri** |
| 1 | 14 | 71,4 | Sedang | Sedang | **Transisi agraris-industri** |
| 2 | 11 | 68,1 | Rendah | Tinggi | **Agraris berkembang** |
| 3 | 7 | 65,3 | Sangat rendah | Tinggi | **Terpencil dengan tantangan akses** |

Kolom terakhir adalah luaran yang dinilai. Tanpa kolom itu, pekerjaan belum selesai.

---

### 11.8 Deteksi Anomali

```python
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

# Isolation Forest — mengisolasi titik yang mudah dipisahkan
iso = IsolationForest(contamination=0.05, random_state=42)
anomali = iso.fit_predict(X_scaled)        # -1 = anomali

# Local Outlier Factor — berdasarkan kerapatan lokal
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
anomali_lof = lof.fit_predict(X_scaled)
```

| Penerapan di Indonesia | Yang dicari |
|------------------------|-------------|
| Pemantauan konsumsi listrik | Pola pemakaian janggal |
| Pemeriksaan transaksi keuangan | Transaksi di luar kebiasaan |
| Pemantauan kualitas udara | Pembacaan sensor yang keliru |
| Audit data survei | Isian yang tidak wajar |

> **Peringatan:** parameter `contamination` menetapkan *berapa persen* data yang akan ditandai sebagai anomali. Menetapkannya 0,05 **menjamin** 5% data ditandai — apakah anomali itu benar-benar ada atau tidak. Angka ini harus berasal dari pengetahuan domain, bukan dari kebiasaan.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 10 buku ajar](../06-buku-ajar/bab-10-pembelajaran-tanpa-supervisi.md).
- Menyiapkan Milestone 2 proyek — **dikumpulkan hari ini**.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | **Pengumpulan P-02**; tinjauan |
| Konsep | 35' | K-Means; asumsi dan batasnya; penentuan k |
| Konsep | 25' | *Hierarchical*; DBSCAN; perbandingan ketiganya |
| Demonstrasi | 35' | Segmentasi provinsi Indonesia dengan data BPS; ketiga metode dibandingkan |
| **Interpretasi** | 30' | **Kegiatan inti:** berkelompok, memberi nama dan penjelasan pada tiap klaster hasil demonstrasi |
| Penutup | 15' | Metrik *clustering*; deteksi anomali; penugasan |

**Kegiatan inti — interpretasi klaster:** setiap kelompok menerima profil klaster berupa tabel rata-rata fitur, lalu harus (a) memberi nama tiap klaster, (b) menjelaskan cirinya dalam satu kalimat, dan (c) mengusulkan tindakan kebijakan yang berbeda untuk tiap klaster. Hasilnya dibandingkan antarkelompok — perbedaan penamaan sendiri menjadi bahan diskusi tentang sifat subjektif interpretasi.

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 11](../04-labs/lab-11-clustering-dan-metriknya.md).
- Melanjutkan proyek menuju laporan akhir (Minggu 14).

---

## Penugasan

**T-11 — *Clustering* dan Metriknya**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook Colab + tabel interpretasi klaster |
| Isi | (a) Segmentasi data BPS dengan K-Means, *hierarchical*, dan DBSCAN; (b) Penentuan k dengan *elbow* **dan** *silhouette*; (c) Ketiga metrik internal untuk tiap metode; (d) Dendrogram; (e) **Tabel profil klaster beserta nama dan penjelasan substantif**; (f) Perbandingan hasil ketiga metode dan pembahasan mengapa berbeda |
| Ketentuan khusus | Notebook tanpa interpretasi substantif dikembalikan |
| Tenggat | Awal pertemuan Minggu 12 |
| Bobot | 1,9% (Observasi) |

---

## Rangkuman

1. Pembelajaran tanpa supervisi **tidak memiliki jawaban benar** — evaluasi bergantung pada ukuran tak langsung dan penilaian manusia.
2. **K-Means wajib diskalakan**; ia mengandaikan klaster bulat, berukuran sebanding, dan berkerapatan sebanding.
3. Metode ***elbow*** memberi petunjuk, bukan jawaban; padukan dengan *silhouette* dan kebermaknaan.
4. *Silhouette* negatif menandai titik yang **kemungkinan salah ditempatkan**.
5. **Dendrogram** memperlihatkan struktur pada berbagai tingkat sekaligus.
6. **DBSCAN tidak memerlukan k** dan mengenali pencilan secara eksplisit, tetapi sangat peka terhadap `eps`.
7. Tiga metrik internal: *silhouette* (tinggi baik), **Davies-Bouldin (rendah baik)**, Calinski-Harabasz (tinggi baik).
8. **Metrik tinggi tidak menjamin klaster bermakna.** Interpretasi substantif wajib.
9. Pekerjaan *clustering* selesai ketika setiap klaster dapat **diberi nama dan dijelaskan**.
10. Parameter `contamination` pada deteksi anomali **menjamin** sekian persen ditandai — harus berasal dari pengetahuan domain.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 9. O'Reilly.
2. James, G., et al. (2023). *An Introduction to Statistical Learning with Python*, Bab 12. Springer.
3. Rousseeuw, P. J. (1987). Silhouettes: A Graphical Aid to the Interpretation and Validation of Cluster Analysis. *J. Comput. Appl. Math.*, 20, 53–65.
4. Ester, M., et al. (1996). A Density-Based Algorithm for Discovering Clusters. *KDD*.
5. Dokumentasi scikit-learn — *Clustering*. <https://scikit-learn.org/stable/modules/clustering.html>
6. Badan Pusat Statistik. *Indeks Pembangunan Manusia*. <https://www.bps.go.id>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
