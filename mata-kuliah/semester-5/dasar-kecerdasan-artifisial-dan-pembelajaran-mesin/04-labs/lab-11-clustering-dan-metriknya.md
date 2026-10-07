# Lab 11: *Clustering* dan Metriknya

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 11 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-10 |
| Durasi | 100 menit |
| Prasyarat | Lab 10 selesai |
| Bobot | 1,875% (Observasi, Sub-CPMK082-1) |
| Diuji pada | scikit-learn 1.6 dan 1.9, pandas 2.2 dan 3.0 (Oktober 2026) |

---

## Tujuan Praktikum

1. Menerapkan K-Means, *hierarchical clustering*, dan DBSCAN pada data indikator sosial-ekonomi provinsi Indonesia.
2. Menentukan jumlah klaster dengan *elbow* dan *silhouette*.
3. Menghitung tiga metrik internal dan menafsirkannya.
4. **Memberi nama dan penjelasan substantif** pada setiap klaster.

---

## Ketentuan Khusus Lab Ini

> **Notebook tanpa interpretasi substantif dikembalikan.** Hasil yang hanya dilaporkan sebagai "klaster 0, klaster 1, klaster 2" dinilai belum selesai. Setiap klaster wajib diberi nama, dijelaskan cirinya, dan dikaitkan dengan tindakan yang berbeda.

---

## Persiapan

1. Buat notebook baru bernama `NIM_Nama_Lab11.ipynb`.
2. Jalankan **sel pembuka baku** di [Lampiran D](../06-buku-ajar/lampiran.md#lampiran-d-sel-pembuka-baku) — mengimpor pustaka, mencatat versi, dan menetapkan `RANDOM_STATE = 42`. Seluruh langkah di bawah mengandaikan sel itu sudah dijalankan.
3. **Data:** tabel di Langkah 1 adalah **data ilustratif (semi-sintetis)** yang disusun mengikuti pola dan kisaran indikator sosial-ekonomi BPS (IPM, umur harapan hidup, rata-rata lama sekolah, pengeluaran per kapita, tingkat pengangguran terbuka, persentase penduduk miskin). Sumber tabel dan tahun publikasinya **tidak terdokumentasi**, sehingga angka-angka ini **bukan data resmi BPS** dan tidak boleh dikutip sebagai data BPS. Tabel memakai susunan **34 provinsi** (sebelum pemekaran Papua); sejak 2022 Indonesia memiliki **38 provinsi** (bertambah Papua Selatan, Papua Tengah, Papua Pegunungan, dan Papua Barat Daya). Bila hasil *clustering* hendak dilaporkan di luar latihan ini (mis. untuk proyek), unduh data resmi terbaru 38 provinsi dari <https://www.bps.go.id> dan catat nama tabel serta tahunnya; angka dan pengelompokan di lab ini akan berubah.

---

## Langkah-langkah

### LANGKAH 1: Data Indikator Provinsi Indonesia (Ilustratif)

> **Data ilustratif (semi-sintetis)** berpola indikator BPS, 34 provinsi (susunan sebelum 2022); bukan data resmi BPS — lihat Persiapan butir 3.

```python
# =============================================
# LANGKAH 1: Data indikator sosial-ekonomi provinsi
#            (ILUSTRATIF — berpola indikator BPS, bukan data resmi BPS)
# =============================================
import numpy as np, pandas as pd

# Angka ilustratif: mengikuti pola dan kisaran indikator BPS, tetapi sumber dan
# tahunnya tidak terdokumentasi. Susunan 34 provinsi (sebelum pemekaran Papua);
# sejak 2022 Indonesia memiliki 38 provinsi. Untuk analisis yang dilaporkan,
# unduh data resmi terbaru dari bps.go.id dan unggah ke Colab.
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
print(df.head().to_string())
print("\nRingkasan:")
print(df.describe().T.round(2).to_string())
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

# Sumbangan rata-rata tiap fitur pada jarak Euclidean KUADRAT sebanding dengan
# variansnya: fitur bervarians besar "menguasai" jarak bila tidak diskalakan
porsi_jarak = pd.Series(X.var(axis=0), index=fitur) / X.var(axis=0).sum()
print("\nPorsi sumbangan pada jarak kuadrat — TANPA penskalaan:")
print(porsi_jarak.sort_values(ascending=False).map("{:.1%}".format).to_string())

print("\nSetelah penskalaan — rata-rata ~0, simpangan ~1:")
print(pd.DataFrame(X_skala, columns=fitur).agg(["mean","std"]).round(3).T.to_string())
```

> **Tanpa penskalaan**, fitur dengan sebaran terbesar menguasai jarak Euclidean semata-mata karena satuan dan sebarannya: pada data ini `persen_penduduk_miskin` (simpangan baku ≈ 5,2; rentang 4,3–26,0) menyumbang ≈ 48% jarak kuadrat dan `ipm` (≈ 3,9; rentang 62,3–82,5) ≈ 27%, sedangkan `rata_lama_sekolah` (≈ 0,9) hanya ≈ 1,4%. Setelah penskalaan, keenam fitur menyumbang sama besar. Simpangan yang tercetak 1,015 — bukan tepat 1 — karena `pandas` membagi dengan n − 1, sedangkan `StandardScaler` membagi dengan n: √(34/33) ≈ 1,015.

**Pemeriksaan otomatis.** Sel berikut harus lulus tanpa `AssertionError`; bila gagal, pesannya menunjukkan apa yang perlu diperiksa.

```python
# =============================================
# Pemeriksaan otomatis — Langkah 2 (penskalaan)
# =============================================
assert np.allclose(X_skala.mean(axis=0), 0, atol=1e-9), (
    "Rata-rata tiap fitur terskala harus ≈ 0 — pastikan StandardScaler di-fit pada X")
assert np.allclose(X_skala.std(axis=0), 1), (
    "Simpangan baku (pembagi n) tiap fitur terskala harus ≈ 1 — periksa StandardScaler")
assert porsi_jarak.max() > 2 / len(fitur), (
    "Tanpa penskalaan, satu fitur seharusnya menyumbang jauh lebih dari porsi adilnya (1/6)")
print("Pemeriksaan otomatis lulus.")
```

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

> `K = 4` hanyalah nilai awal agar seluruh sel dapat dijalankan. Pada data ini, k = 4 **tidak** menjadi pilihan terbaik menurut satu pun dari ketiga metrik di Langkah 3 — jadi keputusan Anda harus bersandar pada Langkah 3 **dan** kebermaknaan bagi kebijakan, lalu dijelaskan. Angka-angka pembahasan di Langkah 9 berlaku untuk `K = 4`.

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

Sesuaikan jumlah baris dengan nilai `K` yang Anda pilih. Nama yang baik menggambarkan **ciri**, bukan sekadar peringkat. "Perkotaan padat dengan IPM tinggi dan pengangguran tinggi" lebih baik daripada "Klaster terbaik".

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
    ax[i].set_title(f"{judul} — n={len(df)}, data ilustratif berpola BPS")
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
from scipy.optimize import linear_sum_assignment
from sklearn.metrics import adjusted_rand_score

# ARI tidak bergantung pada penomoran klaster — aman dihitung langsung
ari = adjusted_rand_score(df["klaster_kmeans"], df["klaster_hc"])
print(f"Kesepakatan K-Means vs Hierarchical (ARI): {ari:.4f}")

silang = pd.crosstab(df["klaster_kmeans"], df["klaster_hc"],
                     rownames=["K-Means"], colnames=["Hierarchical"])
print("\nTabel silang (nomor klaster MENTAH):")
print(silang.to_string())

# PERANGKAP: nomor klaster hanyalah nama sembarang. "Klaster 0" K-Means tidak
# ada hubungannya dengan "klaster 0" hierarchical, sehingga membandingkan nomor
# mentah membesar-besarkan perbedaan.
beda_mentah = int((df["klaster_kmeans"] != df["klaster_hc"]).sum())

# Penyelarasan label (label alignment): pasangkan tiap klaster hierarchical dengan
# satu klaster K-Means sehingga jumlah provinsi yang cocok MAKSIMUM.
# linear_sum_assignment (algoritma Hungaria) meminimalkan biaya -> pakai tanda minus.
idx_baris, idx_kolom = linear_sum_assignment(-silang.values)
peta = dict(sorted((int(silang.columns[j]), int(silang.index[i]))
                  for i, j in zip(idx_baris, idx_kolom)))
df["klaster_hc_selaras"] = df["klaster_hc"].map(peta)
print("\nPemetaan nomor Hierarchical -> K-Means:", peta)

silang_selaras = pd.crosstab(df["klaster_kmeans"], df["klaster_hc_selaras"],
                             rownames=["K-Means"],
                             colnames=["Hierarchical (diselaraskan)"])
print("\nTabel silang SETELAH penyelarasan (kesepakatan ada di diagonal):")
print(silang_selaras.to_string())

beda = df.loc[df["klaster_kmeans"] != df["klaster_hc_selaras"], "provinsi"].tolist()
print(f"\n'Berbeda' bila nomor MENTAH dibandingkan : {beda_mentah} dari {len(df)} provinsi (cara yang KELIRU)")
print(f"Berbeda SETELAH label diselaraskan        : {len(beda)} dari {len(df)} provinsi")
print(" ", ", ".join(beda) if beda else "(tidak ada)")

# Kesimpulan DIHITUNG dari hasil — patokan kasar lab ini untuk ARI
if ari >= 0.9:
    tingkat = "hampir identik"
elif ari >= 0.5:
    tingkat = "sepakat pada struktur besar, tetapi berbeda pada sebagian provinsi"
else:
    tingkat = "hanya sepakat lemah — struktur klaster tidak stabil antarmetode"
print(f"\nKesimpulan: ARI = {ari:.2f} -> kedua metode {tingkat}; "
      f"{len(beda)} provinsi ({len(beda) / len(df):.0%}) ditempatkan berbeda.")
```

**Pemeriksaan otomatis.** Sel berikut mengunci pelajaran utama langkah ini: perbandingan nomor klaster mentah menyesatkan, sedangkan ARI tidak terpengaruh penomoran.

```python
# =============================================
# Pemeriksaan otomatis — Langkah 9 (penyelarasan label)
# =============================================
assert len(beda) <= beda_mentah, (
    "Penyelarasan tidak boleh MENAMBAH jumlah provinsi yang berbeda — periksa pemetaan label")
if K == 4:   # nilai baku lab ini; pada K lain nomor mentah bisa kebetulan sudah selaras
    assert len(beda) < beda_mentah, (
        f"Dengan K = 4, jumlah beda setelah penyelarasan ({len(beda)}) seharusnya lebih kecil "
        f"daripada perbandingan nomor mentah ({beda_mentah}) — periksa linear_sum_assignment")
assert np.isclose(adjusted_rand_score(df["klaster_kmeans"], df["klaster_hc_selaras"]), ari), (
    "ARI seharusnya TIDAK berubah oleh penomoran ulang klaster — periksa kolom klaster_hc_selaras")
print("Pemeriksaan otomatis lulus.")
```

> Pada data ini dengan `K = 4` (diuji pada scikit-learn 1.6 dan 1.9), perbandingan nomor mentah mencetak **30 dari 34** provinsi "berbeda", padahal setelah label diselaraskan hanya **6** provinsi yang benar-benar ditempatkan berbeda (ARI ≈ 0,57). Selisih itu sepenuhnya akibat penomoran sembarang — bukan perbedaan pengelompokan.

**Tulis pembahasan:** provinsi mana yang penempatannya tidak stabil antarmetode (daftar **setelah** penyelarasan)? Apa artinya — apakah provinsi itu berada di perbatasan antarkelompok? Mengapa ARI dapat dihitung tanpa penyelarasan, sedangkan daftar provinsi yang berbeda tidak? Untuk DBSCAN, bandingkan secara kualitatif: jalankan ulang dengan `eps` pilihan Anda dari Langkah 6, lalu periksa provinsi mana yang ditandai derau (label −1) — apakah termasuk provinsi yang penempatannya berbeda antara K-Means dan *hierarchical*?

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
