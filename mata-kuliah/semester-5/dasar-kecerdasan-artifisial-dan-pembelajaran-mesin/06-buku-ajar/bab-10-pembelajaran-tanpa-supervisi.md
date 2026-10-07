# BAB 10: PEMBELAJARAN TANPA SUPERVISI

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK082-1` | Menerapkan K-Means, *hierarchical clustering*, dan DBSCAN | C3 |
| `DAIML-Sub-CPMK082-1` | Menentukan jumlah klaster dan menilai hasilnya dengan metrik yang sesuai | C5 |
| `DAIML-Sub-CPMK082-1` | Menafsirkan hasil *clustering* secara substantif | C4 |

---

## 10.1 Kesulitan Pokok

Pada pembelajaran terbimbing, ada jawaban benar untuk dibandingkan. Di sini tidak ada.

| Persoalan | Konsekuensi |
|-----------|-------------|
| Tidak ada "benar" atau "salah" | Evaluasi bergantung pada ukuran tak langsung **dan** penilaian manusia |
| Hasil bergantung pilihan jarak dan penskalaan | Keputusan teknis mengubah struktur yang ditemukan |
| Jumlah klaster harus ditentukan | Biasanya tidak diketahui sebelumnya |
| Klaster yang ditemukan mungkin tidak bermakna | **Interpretasi substantif wajib** |

> **Kaidah buku ini:** hasil *clustering* yang hanya dilaporkan sebagai "klaster 0, klaster 1, klaster 2" tanpa penafsiran substantif **belum selesai**. Pekerjaan *clustering* selesai ketika setiap klaster dapat diberi nama, dijelaskan cirinya, dan dikaitkan dengan tindakan yang berbeda.

---

## 10.2 K-Means

### 10.2.1 Algoritmanya

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
model = Pipeline([("skala", StandardScaler()),
                  ("kmeans", KMeans(n_clusters=4, n_init=20, random_state=42))])
label = model.fit_predict(X)
```

| Parameter | Peran |
|-----------|-------|
| `n_clusters` | **Wajib ditentukan** |
| `n_init` | Berapa kali diulang dengan pusat awal berbeda; hasil terbaik dipilih |
| `init="k-means++"` | Penempatan pusat awal yang cerdas (baku) |

### 10.2.2 Asumsi dan Batasnya

| Asumsi K-Means | Akibat bila dilanggar |
|----------------|-----------------------|
| Klaster berbentuk bulat | Klaster memanjang atau melengkung terpotong salah |
| Klaster berukuran sebanding | Klaster kecil terserap ke klaster besar |
| Kerapatan sebanding | Daerah renggang terbagi sembarang |
| Tanpa pencilan berat | Pusat tertarik ke pencilan |

Untuk data yang melanggar asumsi ini, DBSCAN atau *hierarchical clustering* lebih sesuai.

---

## 10.3 Menentukan Jumlah Klaster

### 10.3.1 Metode *Elbow*

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

> **Keterbatasan:** siku sering tidak tegas. Metode ini memberi **petunjuk**, bukan jawaban.

### 10.3.2 *Silhouette*

Untuk setiap titik $i$:

$$s(i)=\frac{b(i)-a(i)}{\max\{a(i),\,b(i)\}}$$

di mana $a(i)$ = rata-rata jarak ke anggota klaster sendiri, $b(i)$ = rata-rata jarak ke anggota klaster terdekat berikutnya.

| $s(i)$ | Makna |
|--------|-------|
| Mendekati +1 | Penempatan baik |
| Sekitar 0 | Titik di perbatasan |
| Negatif | **Kemungkinan salah ditempatkan** |

### 10.3.3 Kriteria Ketiga yang Paling Menentukan

Setelah *elbow* dan *silhouette*, ada kriteria ketiga yang tidak dapat dihitung: **apakah jumlah klaster itu bermakna bagi persoalannya?**

Dinas sosial yang harus merancang program intervensi mungkin hanya sanggup mengelola empat jenis program. Menemukan sembilan klaster yang "optimal secara *silhouette*" tidak berguna baginya. Sebaliknya, membagi menjadi dua klaster ketika struktur datanya jelas menunjukkan lima akan menyembunyikan perbedaan yang penting.

Kriteria ini menuntut percakapan dengan pemangku kepentingan — dan itulah sebabnya *clustering* jarang dapat diselesaikan sendirian di depan komputer.

---

## 10.4 *Hierarchical Clustering*

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

| *Linkage* | Jarak antarklaster | Kecenderungan |
|-----------|--------------------|---------------|
| `ward` | Minimalkan penambahan varians | **Klaster seimbang** — paling sering dipakai |
| `complete` | Jarak terjauh | Klaster padat |
| `average` | Rata-rata jarak | Kompromi |
| `single` | Jarak terdekat | Klaster memanjang; peka derau |

**Kelebihan:** dendrogram memperlihatkan struktur pada **berbagai tingkat sekaligus** — sering lebih informatif daripada satu penetapan k.
**Kekurangan:** kompleksitas $O(n^2)$ hingga $O(n^3)$; tidak sesuai untuk data besar.

---

## 10.5 DBSCAN

Mengelompokkan berdasarkan **kerapatan**, bukan jarak ke pusat.

```python
from sklearn.cluster import DBSCAN

db = DBSCAN(eps=0.5, min_samples=5)
label = db.fit_predict(X_skala)
# Label -1 berarti derau/pencilan
```

| Kelebihan | Kekurangan |
|-----------|------------|
| **Jumlah klaster tidak perlu ditentukan** | Sangat peka terhadap `eps` |
| Menemukan klaster berbentuk sembarang | Kesulitan bila kerapatan antarklaster berbeda |
| **Mengenali pencilan secara eksplisit** | Sulit pada dimensi tinggi |

### 10.5.1 Perbandingan Ketiga Metode

| Aspek | K-Means | Hierarchical | DBSCAN |
|-------|---------|--------------|--------|
| k ditentukan di awal | Ya | Tidak (dipotong kemudian) | **Tidak** |
| Bentuk klaster | Bulat | Fleksibel | **Sembarang** |
| Pencilan | Dipaksa masuk | Dipaksa masuk | **Ditandai sebagai derau** |
| Skala data besar | **Baik** | Buruk | Sedang |
| Kestabilan | Bergantung pusat awal | Deterministik | Deterministik |

---

## 10.6 Metrik Evaluasi

### 10.6.1 Tanpa Label Sebenarnya (*Internal*)

| Metrik | Rentang | Arah baik | Yang diukur |
|--------|---------|-----------|-------------|
| **Silhouette** | [−1, 1] | Makin tinggi | Kerapatan dalam vs pemisahan antarklaster |
| **Davies-Bouldin** | [0, ∞) | **Makin rendah** | Rasio sebaran dalam terhadap jarak antarklaster |
| **Calinski-Harabasz** | [0, ∞) | Makin tinggi | Rasio varians antar terhadap dalam klaster |

### 10.6.2 Metrik Tidak Menggantikan Penilaian Manusia

> Skor *silhouette* tinggi berarti klaster terpisah dengan baik **secara geometris**. Ia sama sekali tidak menjamin klaster itu **bermakna**. Data dapat terbagi rapi menjadi lima kelompok yang tidak berarti apa pun bagi persoalan yang sedang ditangani.

Evaluasi *clustering* karena itu selalu berjalan dua lapis:

1. **Lapis teknis:** metrik internal menunjukkan pemisahan yang layak.
2. **Lapis substantif:** setiap klaster dapat diberi nama, dijelaskan cirinya, dan dikaitkan dengan tindakan yang berbeda.

Lapis kedua tidak dapat diotomatiskan.

---

## 10.7 Menafsirkan Klaster

```python
import pandas as pd

# Ciri tiap klaster: rata-rata fitur ASLI (bukan yang sudah diskalakan)
profil = X.assign(klaster=label).groupby("klaster").mean().round(2)
profil["n"] = pd.Series(label).value_counts().sort_index()
print(profil.T)
```

**Contoh hasil segmentasi provinsi Indonesia berdasarkan indikator BPS:**

| Klaster | n | IPM | Kepadatan | % Pertanian | **Nama yang diberikan** |
|---------|---|-----|-----------|-------------|-------------------------|
| 0 | 6 | 76,2 | Tinggi | Rendah | **Perkotaan padat industri** |
| 1 | 14 | 71,4 | Sedang | Sedang | **Transisi agraris-industri** |
| 2 | 11 | 68,1 | Rendah | Tinggi | **Agraris berkembang** |
| 3 | 7 | 65,3 | Sangat rendah | Tinggi | **Terpencil dengan tantangan akses** |

Kolom terakhir adalah luaran yang dinilai. Tanpa kolom itu, pekerjaan belum selesai.

### 10.7.1 Nama yang Baik dan yang Buruk

| Buruk | Mengapa | Baik |
|-------|---------|------|
| "Klaster terbaik" | Menyiratkan peringkat yang tidak ada | "Perkotaan padat industri" |
| "Kelompok 1" | Tidak menyampaikan apa pun | "Agraris berkembang" |
| "Provinsi maju" | Nilai yang dipaksakan | "IPM tinggi, pengangguran tinggi" |

*Clustering* menemukan **kelompok**, bukan **peringkat**. Penamaan yang menyiratkan peringkat memasukkan penilaian yang tidak berasal dari data.

---

## 10.8 Deteksi Anomali

```python
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

iso = IsolationForest(contamination=0.05, random_state=42)
anomali = iso.fit_predict(X_skala)        # -1 = anomali

lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
anomali_lof = lof.fit_predict(X_skala)
```

| Penerapan di Indonesia | Yang dicari |
|------------------------|-------------|
| Pemantauan konsumsi listrik | Pola pemakaian janggal |
| Pemeriksaan transaksi keuangan | Transaksi di luar kebiasaan |
| Pemantauan kualitas udara | Pembacaan sensor yang keliru |
| Audit data survei | Isian yang tidak wajar |

> **Peringatan penting:** parameter `contamination` menetapkan **berapa persen data yang akan ditandai** sebagai anomali. Menetapkannya 0,05 **menjamin** 5% data ditandai — apakah anomali itu benar-benar ada atau tidak. Angka ini harus berasal dari pengetahuan domain (misalnya "dari audit sebelumnya, sekitar 2% transaksi memang janggal"), bukan dari nilai bawaan.

---

## AI Corner — Tahap *Apply → Create*

### Interpretasi Klaster Tidak Dapat Diserahkan

Ini adalah bab di mana batas kemampuan AI paling jelas terlihat.

Diberi tabel profil klaster, model bahasa akan menghasilkan nama dan deskripsi yang terdengar meyakinkan. Masalahnya: nama itu dibuat dari **pola angka**, bukan dari pemahaman tentang apa arti angka itu di Indonesia.

| Contoh keluaran AI | Mengapa bermasalah |
|--------------------|--------------------|
| "Klaster 3: daerah tertinggal" | Istilah "daerah tertinggal" memiliki definisi resmi yang mungkin tidak sesuai dengan klaster ini |
| "Klaster 0: wilayah makmur" | Menyiratkan penilaian yang tidak berasal dari data |
| "Klaster 2: cocok untuk program bantuan" | Rekomendasi kebijakan tanpa dasar |

Penamaan klaster adalah tindakan yang berkonsekuensi: nama yang diberikan akan dipakai orang lain untuk memikirkan kelompok itu. Nama "daerah tertinggal" dan "wilayah dengan tantangan akses geografis" menggambarkan data yang sama dan mengarahkan kebijakan yang berbeda.

### Pemakaian yang Wajar

Untuk kode dan teknik: sepenuhnya boleh.

```
Bagaimana cara membuat dendrogram dengan scipy dan memotongnya
pada jumlah klaster tertentu?
```

Untuk penafsiran: berikan konteks, minta pemeriksaan.

```
Saya memperoleh 4 klaster provinsi dengan profil berikut: [tabel].
Saya memberinya nama: [nama yang saya pilih] dengan alasan [alasan].

Tolong periksa: apakah ada nama yang menyiratkan penilaian yang
tidak berasal dari data, atau yang berbenturan dengan istilah
resmi pemerintah Indonesia yang memiliki definisi berbeda?
```

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan mengapa penskalaan wajib sebelum K-Means, dengan satu contoh konkret.

2. Sebutkan empat asumsi K-Means dan satu akibat bila masing-masing dilanggar.

3. Jelaskan apa arti nilai *silhouette* yang negatif untuk sebuah titik.

4. Sebutkan satu kelebihan dan satu kekurangan DBSCAN dibandingkan K-Means.

### Tingkat Menengah

5. Metode *elbow* menunjukkan siku pada k=3, sementara *silhouette* tertinggi pada k=6.
   (a) Apa yang Anda lakukan?
   (b) Informasi apa yang dibutuhkan untuk memutuskan?
   (c) Siapa yang harus dilibatkan dalam keputusan itu?
   (d) Bagaimana Anda menyatakan ketidakpastian ini dalam laporan?

6. Hasil DBSCAN dengan `eps=0.5` menandai 40% data sebagai derau.
   (a) Apa yang ditunjukkan hal ini?
   (b) Bagaimana cara menentukan `eps` yang lebih sesuai?
   (c) Apa risikonya bila `eps` dinaikkan terlalu besar?
   (d) Kapan proporsi derau yang tinggi justru merupakan temuan yang bermakna?

7. Sebuah *clustering* memperoleh *silhouette* 0,72, tetapi profil klasternya menunjukkan bahwa perbedaan utama antarklaster hanya pada satu fitur.
   (a) Apakah *clustering* ini berhasil?
   (b) Apa yang mungkin terjadi?
   (c) Apa yang akan Anda periksa?
   (d) Apakah hasil ini layak dilaporkan? Bagaimana?

8. Sebuah tim menerapkan `IsolationForest(contamination=0.1)` pada data transaksi, dan melaporkan "ditemukan 10% transaksi anomali".
   (a) Apa yang salah dengan pernyataan itu?
   (b) Dari mana angka 10% sebenarnya berasal?
   (c) Bagaimana seharusnya `contamination` ditentukan?
   (d) Bagaimana kalimat laporan yang benar?

### Tingkat Mahir

9. Lakukan segmentasi lengkap pada data nyata Indonesia.
   (a) Unduh data indikator provinsi atau kabupaten dari BPS.
   (b) Terapkan ketiga metode dengan penskalaan yang benar.
   (c) Tentukan k dengan *elbow*, *silhouette*, **dan** pertimbangan kebermaknaan.
   (d) Laporkan ketiga metrik internal untuk tiap metode.
   (e) Susun tabel profil dengan **nama dan penjelasan substantif** tiap klaster.
   (f) Usulkan tindakan yang berbeda untuk tiap klaster, dan jelaskan dasarnya.

10. Selidiki kestabilan hasil *clustering*.
    (a) Jalankan K-Means dengan sepuluh *seed* berbeda.
    (b) Hitung *Adjusted Rand Index* antarpasangan hasil.
    (c) Identifikasi titik data yang penempatannya paling sering berubah.
    (d) Apa ciri titik-titik itu?
    (e) Apa implikasinya bagi cara melaporkan hasil *clustering*?

11. Tulislah pedoman satu halaman berjudul *"Menamai Kelompok Tanpa Memberi Cap"*. Sertakan: mengapa penamaan klaster berkonsekuensi sosial, kata-kata yang sebaiknya dihindari beserta alasannya, cara menyusun nama yang deskriptif alih-alih evaluatif, dan tiga contoh sebelum-sesudah perbaikan pada konteks data Indonesia.

---

## Rangkuman

1. Pembelajaran tanpa supervisi **tidak memiliki jawaban benar** — evaluasi menuntut ukuran tak langsung **dan** penilaian manusia.
2. **K-Means wajib diskalakan**; ia mengandaikan klaster bulat, berukuran dan berkerapatan sebanding.
3. Metode ***elbow*** memberi petunjuk, bukan jawaban.
4. Kriteria ketiga yang paling menentukan: **apakah jumlah klaster itu bermakna bagi persoalannya?**
5. *Silhouette* negatif menandai titik yang **kemungkinan salah ditempatkan**.
6. **Dendrogram** memperlihatkan struktur pada berbagai tingkat sekaligus.
7. **DBSCAN tidak memerlukan k** dan mengenali pencilan, tetapi sangat peka terhadap `eps`.
8. Tiga metrik internal: *silhouette* (tinggi baik), **Davies-Bouldin (rendah baik)**, Calinski-Harabasz (tinggi baik).
9. **Metrik tinggi tidak menjamin klaster bermakna.** Interpretasi substantif wajib.
10. *Clustering* menemukan **kelompok, bukan peringkat** — penamaan tidak boleh menyiratkan penilaian.
11. Parameter `contamination` **menjamin** sekian persen ditandai; ia harus berasal dari pengetahuan domain.

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
