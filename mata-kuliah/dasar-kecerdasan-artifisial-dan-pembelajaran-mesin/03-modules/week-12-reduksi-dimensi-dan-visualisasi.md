# Minggu 12: Reduksi Dimensi dan Visualisasi Kinerja Model

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 12 dari 16 |
| Topik | PCA, t-SNE/UMAP, kurva pembelajaran, kurva validasi, visualisasi diagnostik |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-11 |
| Bloom | C3 (Menerapkan) → C4 (Menganalisis) |
| Durasi | 150 menit |
| Metode | Kuliah · Praktikum visualisasi |
| Penilaian | Observasi (Lab 12) |

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Menerapkan** (C3) PCA dan menafsirkan *explained variance*.
2. **Membedakan** (C4) peran PCA sebagai reduksi dimensi dari t-SNE/UMAP sebagai alat visual.
3. **Membaca** (C4) kurva pembelajaran dan mendiagnosis kondisi model darinya.
4. **Membaca** (C4) kurva validasi untuk menentukan nilai hiperparameter.
5. **Menyusun** (C3) rangkaian visualisasi diagnostik yang lengkap untuk sebuah model.

---

## Materi Pembelajaran

### 12.1 *Principal Component Analysis*

#### 12.1.1 Gagasannya

PCA mencari sumbu-sumbu baru (komponen utama) yang saling tegak lurus, diurutkan menurut **besarnya keragaman data yang dijelaskan**.

```
     x₂                          PC1 = arah keragaman terbesar
      ▲         ● ●              PC2 = tegak lurus PC1
      │      ● ●●●  ╱PC1
      │   ● ●●●  ╱                Data dinyatakan ulang pada
      │  ●●●  ╱                   sumbu PC1-PC2, bukan x₁-x₂
      │ ● ╱ ╲
      │╱     ╲PC2
      └──────────────► x₁
```

```python
from sklearn.decomposition import PCA
import numpy as np

# PENSKALAAN WAJIB — PCA memaksimalkan varians, yang peka satuan
alur = Pipeline([("skala", StandardScaler()), ("pca", PCA())])
alur.fit(X)

pca = alur.named_steps["pca"]
kumulatif = np.cumsum(pca.explained_variance_ratio_)

for i, (rasio, kum) in enumerate(zip(pca.explained_variance_ratio_, kumulatif), 1):
    print(f"PC{i:2d}: {rasio:6.1%}  (kumulatif {kum:6.1%})")
    if kum > 0.95:
        break
```

#### 12.1.2 Menentukan Jumlah Komponen

| Kriteria | Cara |
|----------|------|
| Ambang varians kumulatif | Ambil komponen sampai mencapai 90–95% |
| *Scree plot* | Cari siku pada grafik varians per komponen |
| Kebutuhan visualisasi | 2 atau 3 komponen |
| Otomatis | `PCA(n_components=0.95)` |

```python
# scikit-learn menerima pecahan: ambil komponen secukupnya untuk 95% varians
pca = PCA(n_components=0.95, random_state=42)
```

#### 12.1.3 Apa yang Diperoleh dan Apa yang Hilang

| Diperoleh | Hilang |
|-----------|--------|
| Dimensi berkurang; komputasi lebih cepat | **Keterjelasan** — PC adalah kombinasi linear, bukan fitur asli |
| Multikolinearitas hilang (PC saling ortogonal) | Sebagian informasi (sesuai varians yang dibuang) |
| Derau berkurang | Kemampuan menjelaskan kepada pemangku kepentingan |
| Visualisasi menjadi mungkin | — |

> **PCA bukan pemilihan fitur.** Pemilihan fitur membuang sebagian fitur dan mempertahankan sisanya apa adanya; PCA mengganti seluruh fitur dengan kombinasi baru. Setelah PCA, tidak ada lagi kolom bernama "omzet_bulanan" — yang ada adalah "PC1" yang merupakan campuran dari seluruh kolom.
>
> Karena itu, pada bidang yang menuntut penjelasan atas keputusan, PCA sering **tidak** dapat dipakai pada tahap akhir meski membantu pada tahap eksplorasi.

#### 12.1.4 Membaca *Loading*

```python
import pandas as pd

loading = pd.DataFrame(
    pca.components_[:3].T,
    columns=["PC1", "PC2", "PC3"],
    index=X.columns,
)
print(loading.round(3))
```

*Loading* menunjukkan seberapa besar setiap fitur asli menyumbang pada tiap komponen — satu-satunya jalan untuk memberi makna pada PC.

---

### 12.2 t-SNE dan UMAP

| Aspek | PCA | t-SNE / UMAP |
|-------|-----|--------------|
| Sifat | Linear | **Non-linear** |
| Tujuan | Mempertahankan varians global | Mempertahankan **struktur lokal** |
| Dapat diterapkan ke data baru | **Ya** (`transform`) | t-SNE: tidak; UMAP: ya |
| Dapat dipakai sebagai prapemrosesan model | **Ya** | **Tidak disarankan** |
| Kegunaan utama | Reduksi dimensi | **Visualisasi** |

```python
from sklearn.manifold import TSNE

# Untuk VISUALISASI saja — bukan untuk prapemrosesan model
tsne = TSNE(n_components=2, perplexity=30, random_state=42, init="pca")
X_2d = tsne.fit_transform(X_scaled)
```

#### 12.2.1 Tiga Kekeliruan Membaca t-SNE

| Kekeliruan | Yang sebenarnya |
|------------|-----------------|
| "Jarak antarklaster pada plot menunjukkan seberapa berbeda" | **Jarak antarklaster tidak bermakna** pada t-SNE |
| "Ukuran klaster menunjukkan jumlah anggotanya" | Ukuran visual tidak mencerminkan kerapatan sebenarnya |
| "Klaster yang terlihat pasti ada" | `perplexity` yang berbeda dapat menghasilkan klaster yang berbeda |

> t-SNE adalah alat untuk **melihat**, bukan alat untuk **menyimpulkan**. Setiap klaster yang terlihat padanya harus diverifikasi dengan cara lain sebelum dijadikan temuan.

---

### 12.3 Kurva Pembelajaran

Menunjukkan bagaimana kinerja berubah seiring bertambahnya data latih — alat diagnosis paling informatif dalam mata kuliah ini.

```python
from sklearn.model_selection import learning_curve
import numpy as np, matplotlib.pyplot as plt

ukuran, skor_latih, skor_val = learning_curve(
    model, X_train, y_train,
    train_sizes=np.linspace(0.1, 1.0, 10),
    cv=5, scoring="f1", n_jobs=-1, random_state=42,
)

plt.plot(ukuran, skor_latih.mean(axis=1), "o-", label="Latih")
plt.plot(ukuran, skor_val.mean(axis=1), "o-", label="Validasi")
plt.fill_between(ukuran, skor_val.mean(axis=1) - skor_val.std(axis=1),
                 skor_val.mean(axis=1) + skor_val.std(axis=1), alpha=0.15)
plt.xlabel("Jumlah data latih"); plt.ylabel("F1"); plt.legend()
```

#### 12.3.1 Tiga Pola dan Diagnosisnya

```
  (a) UNDERFIT                (b) OVERFIT               (c) PAS
  Skor                        Skor                      Skor
   ▲                           ▲  ●●●●●●●●●●            ▲  ●●●●●●●●●
   │                           │                        │ ○○○○○○○○○
   │ ●●●●●●●●●●●               │                        │
   │ ○○○○○○○○○○○               │      ○○○○○○○           │
   │                           │  ○○○○                  │
   └──────────────►            └──────────────►         └──────────────►
     Keduanya rendah             Selisih besar            Keduanya tinggi,
     dan berdekatan              dan menetap              selisih kecil

   ● latih   ○ validasi
```

| Pola | Diagnosis | Tindakan |
|------|-----------|----------|
| Keduanya rendah, berdekatan, mendatar | ***Underfit*** | Tambah kompleksitas model; tambah fitur; kurangi regularisasi |
| Latih tinggi, validasi rendah, selisih menetap | ***Overfit*** | **Tambah data**; kurangi fitur; tambah regularisasi; sederhanakan model |
| Selisih mengecil tetapi belum mendatar | Kurang data | **Menambah data akan membantu** |
| Keduanya tinggi, selisih kecil, mendatar | Pas | Menambah data tidak akan banyak membantu |

> Baris ketiga adalah kegunaan praktis terbesar kurva pembelajaran: ia menjawab pertanyaan **"apakah mengumpulkan lebih banyak data akan membantu?"** — pertanyaan yang berdampak langsung pada anggaran proyek nyata. Bila kurva validasi sudah mendatar, tidak ada gunanya mengumpulkan data lagi.

---

### 12.4 Kurva Validasi

Menunjukkan pengaruh **satu hiperparameter** terhadap kinerja.

```python
from sklearn.model_selection import validation_curve

rentang = np.logspace(-3, 3, 13)
skor_latih, skor_val = validation_curve(
    model, X_train, y_train,
    param_name="ridge__alpha", param_range=rentang,
    cv=5, scoring="r2", n_jobs=-1,
)

plt.semilogx(rentang, skor_latih.mean(axis=1), "o-", label="Latih")
plt.semilogx(rentang, skor_val.mean(axis=1), "o-", label="Validasi")
plt.xlabel("alpha"); plt.ylabel("R²"); plt.legend()
```

```
  Skor
    ▲
    │ ●●●●●●●●●●                      ← latih: turun seiring regularisasi menguat
    │          ●●●●
    │      ○○○○○○○●●●●
    │   ○○○         ●●●●●
    │ ○○               ○○○○
    │                      ○○○
    └──────┬───────────────────────► alpha (log)
        optimum
```

Titik optimum adalah nilai hiperparameter yang memberi **skor validasi tertinggi** — bukan skor latih tertinggi.

---

### 12.5 Rangkaian Visualisasi Diagnostik

Lima grafik yang wajib ada pada laporan proyek:

| # | Grafik | Menjawab pertanyaan |
|---|--------|---------------------|
| 1 | **Matriks konfusi ternormalisasi** | Kelas mana yang paling sering tertukar? |
| 2 | **Kurva ROC** (dan PR bila tak seimbang) | Seberapa baik model memisahkan kelas pada berbagai ambang? |
| 3 | **Kurva pembelajaran** | *Underfit*, *overfit*, atau kurang data? |
| 4 | **Kepentingan fitur** | Fitur mana yang paling berpengaruh pada prediksi? |
| 5 | **Distribusi kesalahan** | Kasus seperti apa yang paling sering salah? |

```python
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Ternormalisasi per baris — menunjukkan recall per kelas
ConfusionMatrixDisplay.from_estimator(
    model, X_test, y_test, normalize="true", cmap="Blues", ax=ax[0])
ax[0].set_title("Matriks Konfusi (ternormalisasi per kelas aktual)")

RocCurveDisplay.from_estimator(model, X_test, y_test, ax=ax[1])
ax[1].plot([0, 1], [0, 1], "k--", lw=1)
ax[1].set_title("Kurva ROC")
plt.tight_layout()
```

#### 12.5.1 Grafik Kelima: Analisis Kesalahan

Yang paling sering dilewati dan paling berguna:

```python
salah = X_test[model.predict(X_test) != y_test].copy()
benar = X_test[model.predict(X_test) == y_test].copy()

# Adakah pola pada kasus yang salah?
perbandingan = pd.DataFrame({
    "Salah": salah.mean(),
    "Benar": benar.mean(),
})
perbandingan["Selisih"] = perbandingan["Salah"] - perbandingan["Benar"]
print(perbandingan.sort_values("Selisih", key=abs, ascending=False).round(3))
```

Bila kasus yang salah ternyata terpusat pada kelompok tertentu — satu wilayah, satu rentang nilai, satu kategori — itu adalah temuan penting yang mengarah langsung pada bahasan *fairness* Minggu 14.

---

### 12.6 Kejujuran dalam Visualisasi

| Praktik yang menyesatkan | Perbaikan |
|--------------------------|-----------|
| Sumbu-y dipotong agar selisih tampak besar | Mulai dari nol, atau nyatakan pemotongannya dengan jelas |
| Menampilkan hanya lipatan terbaik | Tampilkan rerata dengan pita simpangan |
| Matriks konfusi tanpa normalisasi pada data tak seimbang | Normalisasi per kelas aktual |
| Grafik tanpa n dan tanpa sumber | Cantumkan keduanya |
| Skala warna berurutan untuk data kategorik | Gunakan skala kategorik |

> Prinsip yang sama dengan mata kuliah Probabilitas dan Statistik: grafik adalah **argumen**, dan argumen yang tidak jujur tetap tidak jujur meskipun dibuat dengan pustaka yang baik.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 11 buku ajar](../06-buku-ajar/bab-11-reduksi-dimensi-dan-visualisasi.md).
- Menyiapkan hasil model proyek untuk dipakai sebagai bahan praktik.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | Tinjauan; pembahasan T-11 |
| Konsep | 30' | PCA; *explained variance*; *loading*; apa yang hilang |
| Konsep | 20' | t-SNE dan UMAP; tiga kekeliruan membacanya |
| **Diagnosis** | 40' | **Kegiatan inti:** enam kurva pembelajaran ditampilkan tanpa keterangan — mahasiswa mendiagnosis dan mengusulkan tindakan |
| Demonstrasi | 35' | Menyusun lima grafik diagnostik lengkap untuk satu model |
| Penutup | 15' | Kejujuran visualisasi; penugasan |

**Kegiatan inti — enam kurva:** tiap kurva mewakili satu kondisi (*underfit* berat, *underfit* ringan, *overfit* berat, *overfit* ringan, kurang data, pas). Mahasiswa mendiagnosis secara perorangan, lalu dibahas bersama. Bentuk soal ini muncul pada UAS.

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 12](../04-labs/lab-12-pca-dan-visualisasi-model.md).
- Menyiapkan laporan akhir proyek (jatuh tempo Minggu 14).

---

## Penugasan

**T-12 — PCA dan Visualisasi Kinerja Model**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook Colab |
| Isi | (a) PCA dengan *scree plot*, varians kumulatif, dan tabel *loading*; (b) Visualisasi t-SNE beserta catatan keterbatasannya; (c) **Lima grafik diagnostik** §12.5; (d) **Diagnosis tertulis** kondisi model berdasarkan kurva pembelajaran; (e) Analisis kesalahan: adakah pola pada kasus yang salah |
| Tenggat | Awal pertemuan Minggu 13 |
| Bobot | 1,9% (Observasi) |

---

## Rangkuman

1. **PCA wajib didahului penskalaan**; ia mencari sumbu dengan keragaman terbesar.
2. **PCA bukan pemilihan fitur** — ia mengganti fitur dengan kombinasi linear, dan **keterjelasan hilang**.
3. *Loading* adalah satu-satunya jalan memberi makna pada komponen utama.
4. **t-SNE untuk melihat, bukan untuk menyimpulkan.** Jarak antarklaster padanya tidak bermakna.
5. t-SNE **tidak dipakai sebagai prapemrosesan model**.
6. **Kurva pembelajaran** mendiagnosis *underfit*, *overfit*, dan kekurangan data.
7. Kurva pembelajaran menjawab pertanyaan berbiaya nyata: **"apakah menambah data akan membantu?"**
8. **Kurva validasi** menunjukkan pengaruh satu hiperparameter; optimum dibaca dari skor **validasi**.
9. Lima grafik diagnostik wajib: matriks konfusi, ROC/PR, kurva pembelajaran, kepentingan fitur, **distribusi kesalahan**.
10. Kesalahan yang terpusat pada kelompok tertentu adalah temuan *fairness*, bukan sekadar temuan teknis.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 8. O'Reilly.
2. James, G., et al. (2023). *An Introduction to Statistical Learning with Python*, Bab 12. Springer.
3. Wattenberg, M., Viégas, F., & Johnson, I. (2016). How to Use t-SNE Effectively. *Distill*. <https://distill.pub/2016/misread-tsne/>
4. McInnes, L., Healy, J., & Melville, J. (2018). UMAP: Uniform Manifold Approximation and Projection. *arXiv:1802.03426*.
5. Dokumentasi scikit-learn — *Decomposition*. <https://scikit-learn.org/stable/modules/decomposition.html>
6. Dokumentasi scikit-learn — *Validation curves*. <https://scikit-learn.org/stable/modules/learning_curve.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
