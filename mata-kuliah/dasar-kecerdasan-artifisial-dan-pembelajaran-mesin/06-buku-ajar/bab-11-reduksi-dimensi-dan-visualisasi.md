# BAB 11: REDUKSI DIMENSI DAN VISUALISASI KINERJA MODEL

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK102-1` | Menerapkan PCA dan menafsirkan *explained variance* serta *loading* | C3–C4 |
| `DAIML-Sub-CPMK102-1` | Mendiagnosis kondisi model dari kurva pembelajaran | C4 |
| `DAIML-Sub-CPMK102-1` | Menyusun rangkaian visualisasi diagnostik yang lengkap | C3 |

---

## 11.1 *Principal Component Analysis*

### 11.1.1 Gagasannya

PCA mencari sumbu-sumbu baru yang saling tegak lurus, diurutkan menurut **besarnya keragaman data yang dijelaskan**.

```
     x₂                          PC1 = arah keragaman terbesar
      ▲         ● ●              PC2 = tegak lurus PC1
      │      ● ●●●  ╱PC1
      │   ● ●●●  ╱                Data dinyatakan ulang pada
      │  ●●●  ╱                   sumbu PC1-PC2
      │ ● ╱ ╲
      │╱     ╲PC2
      └──────────────► x₁
```

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np

# PENSKALAAN WAJIB — PCA memaksimalkan varians, yang peka satuan
alur = Pipeline([("skala", StandardScaler()), ("pca", PCA(random_state=42))]).fit(X_train)
pca = alur.named_steps["pca"]
kumulatif = np.cumsum(pca.explained_variance_ratio_)

for ambang in [0.80, 0.90, 0.95]:
    k = int(np.searchsorted(kumulatif, ambang) + 1)
    print(f"Komponen untuk {ambang:.0%} varians: {k} dari {X.shape[1]}")
```

### 11.1.2 Apa yang Diperoleh dan Apa yang Hilang

| Diperoleh | Hilang |
|-----------|--------|
| Dimensi berkurang; komputasi lebih cepat | **Keterjelasan** |
| Multikolinearitas hilang (PC saling ortogonal) | Sebagian informasi |
| Derau berkurang | Kemampuan menjelaskan kepada pemangku kepentingan |
| Visualisasi menjadi mungkin | — |

> **PCA bukan pemilihan fitur.** Pemilihan fitur membuang sebagian fitur dan mempertahankan sisanya apa adanya; PCA **mengganti seluruh fitur** dengan kombinasi baru. Setelah PCA, tidak ada lagi kolom bernama "omzet_bulanan" — yang ada adalah "PC1", campuran dari seluruh kolom.
>
> Karena itu, pada bidang yang menuntut penjelasan atas keputusan — kredit, kesehatan, layanan publik — PCA sering **tidak dapat dipakai pada tahap akhir**, meski sangat membantu pada tahap eksplorasi.

### 11.1.3 *Loading*

```python
import pandas as pd

loading = pd.DataFrame(pca.components_[:3].T,
                       columns=["PC1", "PC2", "PC3"], index=X.columns)
print(loading.round(3))
```

*Loading* menunjukkan seberapa besar setiap fitur asli menyumbang pada tiap komponen — **satu-satunya jalan** untuk memberi makna pada PC. Tanpa membaca *loading*, "PC1 menjelaskan 42% varians" adalah pernyataan yang tidak dapat ditindaklanjuti.

---

## 11.2 t-SNE dan UMAP

| Aspek | PCA | t-SNE / UMAP |
|-------|-----|--------------|
| Sifat | Linear | **Non-linear** |
| Tujuan | Mempertahankan varians global | Mempertahankan **struktur lokal** |
| Dapat diterapkan ke data baru | **Ya** (`transform`) | t-SNE: tidak; UMAP: ya |
| Dipakai sebagai prapemrosesan model | **Ya** | **Tidak disarankan** |
| Kegunaan utama | Reduksi dimensi | **Visualisasi** |

### 11.2.1 Tiga Kekeliruan Membaca t-SNE

| Kekeliruan | Yang sebenarnya |
|------------|-----------------|
| "Jarak antarklaster menunjukkan seberapa berbeda" | **Jarak antarklaster tidak bermakna** pada t-SNE |
| "Ukuran klaster menunjukkan jumlah anggotanya" | Ukuran visual tidak mencerminkan kerapatan sebenarnya |
| "Klaster yang terlihat pasti ada" | `perplexity` berbeda dapat menghasilkan klaster berbeda |

> t-SNE adalah alat untuk **melihat**, bukan alat untuk **menyimpulkan**. Setiap klaster yang terlihat padanya harus diverifikasi dengan cara lain sebelum dijadikan temuan.

---

## 11.3 Kurva Pembelajaran

Menunjukkan bagaimana kinerja berubah seiring bertambahnya data latih — alat diagnosis paling informatif dalam buku ini.

```python
from sklearn.model_selection import learning_curve
import numpy as np, matplotlib.pyplot as plt

ukuran, s_latih, s_val = learning_curve(
    model, X_train, y_train, train_sizes=np.linspace(0.1, 1.0, 10),
    cv=5, scoring="f1", n_jobs=-1, random_state=42)

plt.plot(ukuran, s_latih.mean(axis=1), "o-", label="Latih")
plt.plot(ukuran, s_val.mean(axis=1), "s-", label="Validasi")
plt.fill_between(ukuran, s_val.mean(axis=1)-s_val.std(axis=1),
                 s_val.mean(axis=1)+s_val.std(axis=1), alpha=0.15)
plt.xlabel("Jumlah data latih"); plt.ylabel("F1"); plt.legend()
```

### 11.3.1 Tiga Pola dan Diagnosisnya

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
| Keduanya rendah, berdekatan, mendatar | ***Underfit*** | Tambah kompleksitas; tambah fitur; kurangi regularisasi |
| Latih tinggi, validasi rendah, selisih menetap | ***Overfit*** | **Tambah data**; kurangi fitur; tambah regularisasi |
| Selisih mengecil tetapi belum mendatar | **Kurang data** | **Menambah data akan membantu** |
| Keduanya tinggi, selisih kecil, mendatar | Pas | Menambah data tidak akan banyak membantu |

### 11.3.2 Pertanyaan Berbiaya Nyata

Baris ketiga adalah kegunaan praktis terbesar kurva pembelajaran. Ia menjawab pertanyaan yang berdampak langsung pada anggaran proyek:

> **"Apakah mengumpulkan lebih banyak data akan membantu?"**

Bila kurva validasi sudah mendatar, tidak ada gunanya mengumpulkan data lagi — perhatian harus dialihkan ke fitur atau model. Bila masih menanjak, pengumpulan data adalah investasi yang paling menguntungkan.

Menjawab pertanyaan ini dengan bukti, alih-alih dengan dugaan, adalah salah satu sumbangan paling konkret seorang insinyur ML pada keputusan organisasinya.

---

## 11.4 Kurva Validasi

Menunjukkan pengaruh **satu hiperparameter** terhadap kinerja.

```python
from sklearn.model_selection import validation_curve

rentang = np.logspace(-3, 3, 13)
s_latih, s_val = validation_curve(
    model, X_train, y_train, param_name="ridge__alpha",
    param_range=rentang, cv=5, scoring="r2", n_jobs=-1)
```

```
  Skor
    ▲
    │ ●●●●●●●●●●                      ← latih: turun seiring regularisasi menguat
    │          ●●●●
    │      ○○○○○○○●●●●
    │   ○○○         ●●●●●
    │ ○○               ○○○○
    └──────┬───────────────────────► alpha (log)
        optimum
```

Titik optimum dibaca dari **skor validasi**, bukan skor latih.

---

## 11.5 Rangkaian Visualisasi Diagnostik

Lima grafik yang wajib ada pada laporan proyek:

| # | Grafik | Menjawab pertanyaan |
|---|--------|---------------------|
| 1 | **Matriks konfusi ternormalisasi** | Kelas mana yang paling sering tertukar? |
| 2 | **Kurva ROC** (dan PR bila timpang) | Seberapa baik model memisahkan kelas pada berbagai ambang? |
| 3 | **Kurva pembelajaran** | *Underfit*, *overfit*, atau kurang data? |
| 4 | **Kepentingan fitur** | Fitur mana yang paling berpengaruh? |
| 5 | **Distribusi kesalahan** | Kasus seperti apa yang paling sering salah? |

### 11.5.1 Grafik Kelima: Analisis Kesalahan

Yang paling sering dilewati dan paling berguna.

```python
import pandas as pd

pred = model.predict(X_test)
salah = pred != y_test

perbandingan = pd.DataFrame({
    "Rata-rata (salah)": X_test[salah].mean(),
    "Rata-rata (benar)": X_test[~salah].mean(),
})
perbandingan["Selisih baku"] = ((perbandingan["Rata-rata (salah)"]
                                 - perbandingan["Rata-rata (benar)"]) / X_test.std())
print(perbandingan.reindex(perbandingan["Selisih baku"].abs()
                           .nlargest(5).index).round(3))
```

Bila kasus yang salah terpusat pada kelompok tertentu — satu wilayah, satu rentang nilai, satu kategori — itu adalah **temuan penting** yang mengarah langsung pada bahasan *fairness* Bab 13.

---

## 11.6 Kejujuran dalam Visualisasi

| Praktik yang menyesatkan | Perbaikan |
|--------------------------|-----------|
| Sumbu-y dipotong agar selisih tampak besar | Mulai dari nol, atau nyatakan pemotongannya |
| Menampilkan hanya lipatan terbaik | Tampilkan rerata dengan pita simpangan |
| Matriks konfusi tanpa normalisasi pada data timpang | Normalisasi per kelas aktual |
| Grafik tanpa n dan tanpa sumber | Cantumkan keduanya |
| Skala warna berurutan untuk data kategorik | Gunakan skala kategorik |

> Prinsip yang sama dengan Probabilitas dan Statistik: **grafik adalah argumen**, dan argumen yang tidak jujur tetap tidak jujur meskipun dibuat dengan pustaka yang baik.

---

## AI Corner — Tahap *Apply → Create*

### Diagnosis Adalah Keterampilan yang Tidak Dapat Dialihkan

Membaca kurva pembelajaran menuntut dua hal: mengenali polanya, dan memutuskan tindakan yang tepat. Yang pertama dapat dijelaskan AI dengan baik; yang kedua bergantung pada keadaan proyek yang tidak diketahuinya.

Diberi kurva yang menunjukkan *overfitting*, AI akan menyarankan "tambah data atau tambah regularisasi". Saran itu benar secara umum. Yang tidak diketahuinya:

| Pertanyaan | Hanya diketahui oleh pengelola proyek |
|------------|---------------------------------------|
| Apakah data tambahan tersedia? | Ada atau tidaknya sumber data lain |
| Berapa biayanya? | Anggaran dan waktu yang tersisa |
| Apakah menyederhanakan model dapat diterima? | Kebutuhan kinerja minimum |
| Apakah keterjelasan dituntut? | Konteks regulasi dan pengguna |

Diagnosis yang berguna adalah yang berujung pada **tindakan yang dapat dijalankan**, dan itu selalu menuntut pengetahuan tentang batas-batas nyata proyek.

### Memakai AI untuk Membuat, Bukan Membaca

```
Bagaimana cara membuat kurva pembelajaran dengan pita simpangan
di matplotlib, dengan sumbu-x jumlah data latih?
```

Ini pemakaian yang tepat. Yang berikut tidak:

```
Ini kurva pembelajaran saya [gambar]. Apa diagnosisnya dan apa
yang harus saya lakukan?
```

Yang kedua menyerahkan keterampilan yang justru diuji pada UAS — dan yang, pada pekerjaan nyata, tidak dapat diserahkan karena keputusannya bergantung pada keadaan yang tidak ada dalam gambar.

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan mengapa PCA wajib didahului penskalaan.

2. Jelaskan perbedaan pemilihan fitur dan PCA dalam hal apa yang tersisa setelahnya.

3. Untuk masing-masing pola kurva pembelajaran, tentukan diagnosis dan satu tindakan:
   (a) Latih 0,98; validasi 0,62; selisih menetap.
   (b) Latih 0,64; validasi 0,61; keduanya mendatar.
   (c) Latih 0,89; validasi 0,84; validasi masih menanjak.

4. Sebutkan tiga kekeliruan membaca plot t-SNE.

### Tingkat Menengah

5. Sebuah PCA menunjukkan PC1 menjelaskan 38% varians, PC2 22%, PC3 11%.
   (a) Berapa varians kumulatif tiga komponen pertama?
   (b) Apakah cukup untuk visualisasi 2 dimensi? Jelaskan.
   (c) Berapa komponen yang dibutuhkan untuk 95%, bila komponen berikutnya masing-masing sekitar 5%?
   (d) Apa yang harus dibaca untuk mengetahui **arti** PC1?

6. Kurva pembelajaran menunjukkan skor validasi masih menanjak pada ukuran data penuh.
   (a) Apa diagnosisnya?
   (b) Apa rekomendasi Anda kepada pengelola proyek?
   (c) Informasi apa yang dibutuhkan sebelum rekomendasi itu dapat dijalankan?
   (d) Bila data tambahan tidak tersedia, apa alternatifnya?

7. Analisis kesalahan menunjukkan bahwa 70% kasus yang salah berasal dari satu provinsi yang hanya menyumbang 8% data.
   (a) Apa yang ditunjukkan temuan ini?
   (b) Sebutkan dua kemungkinan penyebabnya.
   (c) Apa yang harus dilaporkan dalam *model card*?
   (d) Tindakan apa yang dapat dipertimbangkan?

8. Sebuah laporan menampilkan grafik perbandingan model dengan sumbu-y dari 0,84 sampai 0,87.
   (a) Apa yang dilakukan pemotongan sumbu itu pada persepsi pembaca?
   (b) Kapan pemotongan sumbu dapat dibenarkan?
   (c) Apa yang harus disertakan bila sumbu dipotong?
   (d) Informasi apa yang lebih penting daripada selisih rerata pada grafik semacam itu?

### Tingkat Mahir

9. Bangun rangkaian diagnostik lengkap untuk satu model.
   (a) Latih model pada data nyata.
   (b) Buat kelima grafik §11.5.
   (c) Tuliskan diagnosis tertulis untuk masing-masing.
   (d) Lakukan analisis kesalahan dengan pencarian pola.
   (e) Susun ringkasan satu halaman: kondisi model, penyebabnya, dan tiga tindakan berurutan prioritas.

10. Selidiki kapan PCA membantu dan kapan merugikan.
    (a) Terapkan PCA dengan 2, 5, 10, 20 komponen, dan tanpa PCA.
    (b) Ukur kinerja model pada masing-masing dengan validasi silang.
    (c) Ukur pula waktu latihnya.
    (d) Buat grafik kinerja dan waktu terhadap jumlah komponen.
    (e) Tentukan titik terbaik, dan jelaskan apa yang dikorbankan di titik itu.
    (f) Untuk masalah yang menuntut keterjelasan, apakah titik itu tetap dapat dipilih? Jelaskan.

11. Buat panduan diagnosis satu halaman berjudul *"Membaca Kurva Pembelajaran"*. Sertakan: keempat pola beserta gambarnya, diagnosis dan tindakan untuk masing-masing, tiga pola yang tidak khas beserta kemungkinan sebabnya, dan daftar pertanyaan yang harus dijawab sebelum tindakan dipilih.

---

## Rangkuman

1. **PCA wajib didahului penskalaan**; ia mencari sumbu dengan keragaman terbesar.
2. **PCA bukan pemilihan fitur** — ia mengganti fitur dengan kombinasi linear, dan **keterjelasan hilang**.
3. *Loading* adalah **satu-satunya jalan** memberi makna pada komponen utama.
4. **t-SNE untuk melihat, bukan untuk menyimpulkan.** Jarak antarklaster padanya tidak bermakna.
5. t-SNE **tidak dipakai sebagai prapemrosesan model**.
6. **Kurva pembelajaran** mendiagnosis *underfit*, *overfit*, dan kekurangan data.
7. Ia menjawab pertanyaan berbiaya nyata: **"apakah menambah data akan membantu?"**
8. **Kurva validasi** menunjukkan pengaruh satu hiperparameter; optimum dibaca dari skor **validasi**.
9. Lima grafik diagnostik wajib, dengan **distribusi kesalahan** sebagai yang paling sering dilewati.
10. Kesalahan yang terpusat pada kelompok tertentu adalah **temuan *fairness***, bukan sekadar temuan teknis.
11. **Grafik adalah argumen** — dan argumen yang tidak jujur tetap tidak jujur.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 8. O'Reilly.
2. James, G., et al. (2023). *An Introduction to Statistical Learning with Python*, Bab 12. Springer.
3. Wattenberg, M., Viégas, F., & Johnson, I. (2016). How to Use t-SNE Effectively. *Distill*. <https://distill.pub/2016/misread-tsne/>
4. McInnes, L., Healy, J., & Melville, J. (2018). UMAP. *arXiv:1802.03426*.
5. Dokumentasi scikit-learn — *Validation curves*. <https://scikit-learn.org/stable/modules/learning_curve.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
