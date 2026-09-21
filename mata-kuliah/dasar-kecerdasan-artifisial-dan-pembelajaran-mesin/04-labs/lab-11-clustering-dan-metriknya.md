# Lab 11: *Clustering* dan Metriknya

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 11 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-10 |
| Durasi | 100 menit |
| Prasyarat | Lab 10 selesai |
| Bobot | 1,9% (Observasi) |

---

## Tujuan Praktikum

1. Menerapkan K-Means, *hierarchical clustering*, dan DBSCAN pada data nyata.
2. Menentukan jumlah klaster dengan *elbow* dan *silhouette*.
3. Menghitung tiga metrik internal dan menafsirkannya.
4. **Memberi nama dan penjelasan substantif** pada setiap klaster.

---

## Ketentuan Khusus Lab Ini

> **Notebook tanpa interpretasi substantif dikembalikan.** Hasil yang hanya dilaporkan sebagai "klaster 0, klaster 1, klaster 2" dinilai belum selesai. Setiap klaster wajib diberi nama, dijelaskan cirinya, dan dikaitkan dengan tindakan yang berbeda.

---

## Langkah-langkah

### LANGKAH 1: Data Indikator Provinsi Indonesia

```python
# =============================================
# LANGKAH 1: Data indikator sosial-ekonomi provinsi
# =============================================
import numpy as np, pandas as pd

# Data berdasarkan struktur publikasi BPS. Pada praktikum sebenarnya,
# unduh data terbaru dari bps.go.id dan unggah ke Colab.
data = {
    "provinsi": ["Aceh","Sumatera Utara","Sumatera Barat","Riau","Jambi",
                 "Sumatera Selatan","Bengkulu","Lampung","Bangka Belitung",
                 "Kepulauan Riau","DKI Jakarta","Jawa Barat","Jawa Tengah",
                 "DI Yogyakarta","Jawa Timur","Banten","Bali",
                 "Nusa Tenggara Barat","Nusa Tenggara Timur","Kalimantan Barat",
                 "Kalimantan Tengah","Kalimantan Selatan","Kalimantan Timur",
                 "Kalimantan Utara","Sulawesi Utara","Sulawesi Tengah",
                 "Sulawesi Selatan","Sulawesi Tenggara","Gorontalo",
                 "Sulawesi Barat","Maluku","Maluku Utara","Papua Barat","Papua"],
    "ipm":  [72.8,73.1,73.3,73.5,72.1,70.9,72.2,70.5,72.2,76.5,82.5,73.7,73.4,
             81.1,72.8,73.3,76.6,70.0,65.9,68.6,71.5,71.8,77.4,72.0,73.8,70.3,
             73.3,72.2,70.2,66.9,70.2,69.9,66.0,62.3],
    "harapan_hidup": [69.9,69.4,69.5,71.7,71.2,69.9,69.5,70.6,70.8,70.1,73.2,
                      73.3,74.5,75.1,71.6,70.1,72.1,66.5,67.4,70.6,69.6,68.9,
                      74.6,72.9,71.6,68.7,70.9,71.2,68.2,65.0,66.1,68.5,66.0,66.0],
    "rata_lama_sekolah": [9.5,9.6,9.1,9.2,8.7,8.4,9.0,8.1,8.2,10.2,11.3,8.8,7.8,
                          9.8,8.0,9.1,9.0,7.6,7.7,7.6,8.8,8.3,9.9,9.3,9.6,8.9,
                          8.7,9.1,7.8,8.1,10.0,9.3,8.2,7.1],
    "pengeluaran_kapita_jt": [10.3,11.5,11.4,11.7,11.2,11.4,11.0,10.2,13.9,14.5,
                              19.0,11.4,11.3,15.0,12.2,12.5,14.2,10.5,8.0,9.4,
                              11.5,12.1,12.5,10.4,11.5,10.3,11.9,10.4,10.4,9.4,
                              9.5,9.1,9.4,7.6],
    "tingkat_pengangguran": [6.0,5.4,6.2,4.4,4.5,4.5,3.4,4.2,4.6,7.5,7.2,7.9,5.4,
                             3.6,5.2,7.5,2.7,2.9,3.0,5.3,4.3,4.5,5.7,4.3,5.5,3.1,
                             4.4,3.4,3.0,2.9,6.1,4.3,5.4,2.8],
    "persen_penduduk_miskin": [14.5,8.1,5.9,6.7,7.6,11.8,14.3,11.1,4.6,5.7,4.4,
                               7.6,10.8,11.0,10.4,6.2,4.3,13.9,19.9,6.7,5.2,4.4,
                               6.1,6.8,7.4,12.3,8.7,11.4,15.2,11.5,16.2,6.3,21.3,26.0],
}
df = pd.DataFrame(data)
print("Dimensi:", df.shape)
display(df.head())
print("\nRingkasan:")
display(df.describe().T.round(2))
```

### LANGKAH 2: Penskalaan — Wajib

```python
# =============================================
# LANGKAH 2: Penskalaan
# =============================================
from sklearn.preprocessing import StandardScaler

fitur = ["ipm", "harapan_hidup", "rata_lama_sekolah",
         "pengeluaran_kapita_jt", "tingkat_pengangguran",
         "persen_penduduk_miskin"]

X = df[fitur].values
scaler = StandardScaler()
X_skala = scaler.fit_transform(X)

print("Sebelum penskalaan — rentang tiap fitur:")
print(pd.DataFrame(X, columns=fitur).agg(["min","max"]).round(2).T.to_string())
print("\nSetelah penskalaan — rata-rata ~0, simpangan ~1:")
print(pd.DataFrame(X_skala, columns=fitur).agg(["mean","std"]).round(3).T.to_string())
```

> **Tanpa penskalaan**, `pengeluaran_kapita_jt` (rentang 7,6–19,0) dan `ipm` (62–82) akan mendominasi jarak Euclidean semata-mata karena satuannya.

### LANGKAH 3: Menentukan Jumlah Klaster

```python
# =============================================
# LANGKAH 3: Elbow dan silhouette
# =============================================
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import (silhouette_score, davies_bouldin_score,
                             calinski_harabasz_score)

rentang_k = range(2, 9)
inersia, sil, db, ch = [], [], [], []

for k in rentang_k:
    km = KMeans(n_clusters=k, n_init=20, random_state=RANDOM_STATE)
    label = km.fit_predict(X_skala)
    inersia.append(km.inertia_)
    sil.append(silhouette_score(X_skala, label))
    db.append(davies_bouldin_score(X_skala, label))
    ch.append(calinski_harabasz_score(X_skala, label))

ringkas = pd.DataFrame({"k": list(rentang_k), "Inersia": inersia,
                        "Silhouette": sil, "Davies-Bouldin": db,
                        "Calinski-Harabasz": ch})
print(ringkas.round(3).to_string(index=False))

fig, ax = plt.subplots(1, 3, figsize=(15, 4.2))
ax[0].plot(rentang_k, inersia, "o-"); ax[0].set_xlabel("k")
ax[0].set_ylabel("Inersia (WCSS)"); ax[0].set_title("Metode Elbow")
ax[1].plot(rentang_k, sil, "o-", color="tab:green"); ax[1].set_xlabel("k")
ax[1].set_ylabel("Silhouette"); ax[1].set_title("Silhouette (makin tinggi makin baik)")
ax[2].plot(rentang_k, db, "o-", color="tab:red"); ax[2].set_xlabel("k")
ax[2].set_ylabel("Davies-Bouldin"); ax[2].set_title("Davies-Bouldin (makin RENDAH makin baik)")
plt.tight_layout(); plt.show()
```

**Tulis di sel Markdown:** apakah ketiga kriteria menunjuk k yang sama? Bila berbeda, kriteria mana yang Anda pilih dan mengapa? Pertimbangkan pula apakah jumlah klaster itu **bermakna** untuk kebijakan.

### LANGKAH 4: K-Means

```python
# =============================================
# LANGKAH 4: K-Means dengan k terpilih
# =============================================
K = 4      # ganti sesuai kesimpulan Langkah 3, dan JELASKAN alasannya

km = KMeans(n_clusters=K, n_init=50, random_state=RANDOM_STATE)
df["klaster_kmeans"] = km.fit_predict(X_skala)

print("Ukuran tiap klaster:")
print(df["klaster_kmeans"].value_counts().sort_index().to_string())
print(f"\nSilhouette: {silhouette_score(X_skala, df['klaster_kmeans']):.4f}")
print(f"Davies-Bouldin: {davies_bouldin_score(X_skala, df['klaster_kmeans']):.4f}")
```

### LANGKAH 5: *Hierarchical Clustering* dan Dendrogram

```python
# =============================================
# LANGKAH 5: Hierarchical dan dendrogram
# =============================================
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

hc = AgglomerativeClustering(n_clusters=K, linkage="ward")
df["klaster_hc"] = hc.fit_predict(X_skala)

Z = linkage(X_skala, method="ward")
fig, ax = plt.subplots(figsize=(15, 6))
dendrogram(Z, labels=df["provinsi"].values, leaf_rotation=90,
           leaf_font_size=8, ax=ax)
ax.set_ylabel("Jarak (Ward)")
ax.set_title(f"Dendrogram provinsi Indonesia (n={len(df)})")
plt.tight_layout(); plt.show()

print(f"Silhouette hierarchical: {silhouette_score(X_skala, df['klaster_hc']):.4f}")
```

> Dendrogram memperlihatkan struktur pada berbagai tingkat sekaligus. Perhatikan provinsi mana yang bergabung paling awal — itu yang paling mirip menurut indikator yang dipakai.

### LANGKAH 6: DBSCAN

```python
# =============================================
# LANGKAH 6: DBSCAN — tidak memerlukan k
# =============================================
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors

# Menentukan eps dengan grafik k-distance
nn = NearestNeighbors(n_neighbors=4).fit(X_skala)
jarak, _ = nn.kneighbors(X_skala)
jarak_urut = np.sort(jarak[:, -1])

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(jarak_urut, "o-")
ax.set_xlabel("Titik (terurut)"); ax.set_ylabel("Jarak ke tetangga ke-4")
ax.set_title("Grafik k-distance untuk menentukan eps")
plt.tight_layout(); plt.show()

for eps in [1.0, 1.5, 2.0, 2.5]:
    db_model = DBSCAN(eps=eps, min_samples=3)
    lbl = db_model.fit_predict(X_skala)
    n_klaster = len(set(lbl)) - (1 if -1 in lbl else 0)
    n_derau = int((lbl == -1).sum())
    sil_txt = (f"{silhouette_score(X_skala[lbl != -1], lbl[lbl != -1]):.4f}"
               if n_klaster > 1 and (lbl != -1).sum() > n_klaster else "—")
    print(f"eps={eps:.1f}: {n_klaster} klaster, {n_derau} derau, silhouette={sil_txt}")
```

### LANGKAH 7: Interpretasi Substantif — Bagian yang Dinilai

```python
# =============================================
# LANGKAH 7: Profil dan PENAMAAN klaster
# =============================================
profil = df.groupby("klaster_kmeans")[fitur].mean().round(2)
profil["n"] = df["klaster_kmeans"].value_counts().sort_index()
print("Profil tiap klaster (rata-rata fitur ASLI, bukan terskala):")
print(profil.to_string())

print("\nAnggota tiap klaster:")
for k in sorted(df["klaster_kmeans"].unique()):
    anggota = df.loc[df["klaster_kmeans"] == k, "provinsi"].tolist()
    print(f"\n  Klaster {k} ({len(anggota)} provinsi):")
    print("   ", ", ".join(anggota))
```

**Yang WAJIB ditulis di sel Markdown — tabel interpretasi:**

```markdown
| Klaster | n | Ciri pokok | **Nama yang diberikan** | Usulan tindakan kebijakan |
|---------|---|------------|-------------------------|---------------------------|
| 0       |   |            |                         |                           |
| 1       |   |            |                         |                           |
| 2       |   |            |                         |                           |
| 3       |   |            |                         |                           |
```

Nama yang baik menggambarkan **ciri**, bukan sekadar peringkat. "Perkotaan padat dengan IPM tinggi dan pengangguran tinggi" lebih baik daripada "Klaster terbaik".

### LANGKAH 8: Visualisasi dengan PCA

```python
# =============================================
# LANGKAH 8: Memproyeksikan ke 2 dimensi
# =============================================
from sklearn.decomposition import PCA

pca = PCA(n_components=2, random_state=RANDOM_STATE)
X_2d = pca.fit_transform(X_skala)

fig, ax = plt.subplots(1, 2, figsize=(15, 6))
for i, (kol, judul) in enumerate([("klaster_kmeans", "K-Means"),
                                  ("klaster_hc", "Hierarchical (Ward)")]):
    sc = ax[i].scatter(X_2d[:, 0], X_2d[:, 1], c=df[kol], cmap="viridis", s=90)
    for j, prov in enumerate(df["provinsi"]):
        ax[i].annotate(prov, (X_2d[j, 0], X_2d[j, 1]), fontsize=6,
                       xytext=(3, 3), textcoords="offset points")
    ax[i].set_xlabel(f"PC1 ({pca.explained_variance_ratio_[0]:.1%} varians)")
    ax[i].set_ylabel(f"PC2 ({pca.explained_variance_ratio_[1]:.1%} varians)")
    ax[i].set_title(f"{judul} — n={len(df)}, sumber: struktur data BPS")
plt.tight_layout(); plt.show()

print("Varians terjelaskan oleh 2 komponen:",
      f"{pca.explained_variance_ratio_.sum():.1%}")

# Loading: apa arti PC1 dan PC2?
loading = pd.DataFrame(pca.components_.T, columns=["PC1", "PC2"], index=fitur)
print("\nLoading:")
print(loading.round(3).to_string())
```

### LANGKAH 9: Membandingkan Ketiga Metode

```python
# =============================================
# LANGKAH 9: Apakah ketiganya sepakat?
# =============================================
from sklearn.metrics import adjusted_rand_score

print("Kesepakatan K-Means vs Hierarchical (ARI):",
      round(adjusted_rand_score(df["klaster_kmeans"], df["klaster_hc"]), 4))

silang = pd.crosstab(df["klaster_kmeans"], df["klaster_hc"],
                     rownames=["K-Means"], colnames=["Hierarchical"])
print("\nTabel silang:")
print(silang.to_string())

beda = df[df["klaster_kmeans"] != df["klaster_hc"]]["provinsi"].tolist()
print(f"\nProvinsi yang penempatannya berbeda antar metode ({len(beda)}):")
print(" ", ", ".join(beda) if beda else "  (tidak ada)")
```

**Tulis pembahasan:** provinsi mana yang penempatannya tidak stabil antarmetode? Apa artinya — apakah provinsi itu berada di perbatasan antarkelompok?

---

## Tantangan Tambahan

### Tantangan 1 — Deteksi Anomali

Terapkan `IsolationForest(contamination=0.1)` pada data yang sama. Provinsi mana yang ditandai sebagai anomali? Apakah sesuai dengan dugaan Anda? Bahas pula mengapa parameter `contamination` **menjamin** 10% data ditandai apa pun kenyataannya.

### Tantangan 2 — Pengaruh Pemilihan Fitur

Ulangi *clustering* dengan hanya tiga fitur (ipm, pengeluaran_kapita_jt, persen_penduduk_miskin). Apakah pengelompokannya berubah? Apa artinya bagi keandalan kesimpulan *clustering*?

### Tantangan 3 — *Linkage* yang Berbeda

Bandingkan `ward`, `complete`, `average`, dan `single` pada *hierarchical clustering*. Bandingkan dendrogram dan skor *silhouette* masing-masing. Mengapa `single` cenderung menghasilkan klaster memanjang?

---

## Checklist Penyelesaian

- [ ] Penskalaan diterapkan dan dampaknya ditunjukkan
- [ ] Jumlah klaster ditentukan dengan *elbow* **dan** *silhouette*
- [ ] Pemilihan k dijelaskan alasannya, termasuk pertimbangan kebermaknaan
- [ ] Ketiga metode (K-Means, *hierarchical*, DBSCAN) dijalankan
- [ ] Dendrogram ditampilkan dan dibaca
- [ ] Tiga metrik internal dilaporkan untuk tiap metode
- [ ] **Tabel profil klaster dengan nama dan penjelasan substantif**
- [ ] **Usulan tindakan kebijakan berbeda untuk tiap klaster**
- [ ] Visualisasi PCA dengan *loading* yang ditafsirkan
- [ ] Ketiga metode dibandingkan dan perbedaannya dibahas
- [ ] Notebook berjalan ulang tanpa galat
- [ ] AI Usage Log lengkap

---

## Referensi

1. [Modul Minggu 11](../03-modules/week-11-pembelajaran-tanpa-supervisi.md)
2. [Bab 10 buku ajar](../06-buku-ajar/bab-10-pembelajaran-tanpa-supervisi.md)
3. Rousseeuw, P. J. (1987). Silhouettes. *J. Comput. Appl. Math.*, 20, 53–65.
4. Badan Pusat Statistik. *Indeks Pembangunan Manusia*. <https://www.bps.go.id>
5. Dokumentasi scikit-learn — *Clustering*. <https://scikit-learn.org/stable/modules/clustering.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
