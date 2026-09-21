# Minggu 10: SVM, Naive Bayes, dan Pemilihan Model

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 10 dari 16 |
| Topik | SVM dan *kernel*, Naive Bayes, penyetelan hiperparameter, perbandingan model yang adil |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-09 |
| Bloom | C3 (Menerapkan) → C5 (Mengevaluasi) |
| Durasi | 150 menit |
| Metode | Kuliah · Praktikum · Diskusi hasil |
| Penilaian | Observasi (Lab 10) · **Kuis 3** |

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Menjelaskan** (C2) gagasan margin maksimum pada SVM dan peran *kernel*.
2. **Menerapkan** (C3) Naive Bayes dan menjelaskan asumsi kebebasannya.
3. **Menerapkan** (C3) penyetelan hiperparameter dengan `GridSearchCV` dan `RandomizedSearchCV`.
4. **Merancang** (C6) protokol perbandingan model yang adil.
5. **Mengevaluasi** (C5) hasil perbandingan dengan memperhatikan ketidakpastiannya.

---

## Materi Pembelajaran

### 10.1 Support Vector Machine

#### 10.1.1 Margin Maksimum

```
        ×  ×            │      ○
     ×     ×      ┊     │    ┊    ○   ○
        ×      ┊        │       ┊   ○
    ×       ┊           │          ┊    ○
          ┊             │             ┊
      ─────┴────────────┴──────────────┴─────
        margin    hiperbidang    margin
        bawah      pemisah        atas

    × dan ○ yang MENYENTUH garis putus-putus
    adalah support vector — hanya mereka yang
    menentukan posisi hiperbidang.
```

SVM tidak sekadar mencari pemisah; ia mencari pemisah dengan **jarak terbesar** ke titik terdekat dari kedua kelas. Gagasan ini memberi ketahanan: pemisah yang berjarak lebar lebih mungkin bertahan pada data baru.

#### 10.1.2 *Kernel*

Ketika data tidak terpisahkan secara linear, *kernel* memetakannya ke ruang berdimensi lebih tinggi tempat pemisahan linear menjadi mungkin — tanpa menghitung pemetaan itu secara eksplisit (*kernel trick*).

| Kernel | Bentuk | Kapan dipakai |
|--------|--------|---------------|
| `linear` | $x_i^\top x_j$ | Data berdimensi tinggi; teks |
| `rbf` | $\exp(-\gamma\|x_i-x_j\|^2)$ | **Baku; paling serbaguna** |
| `poly` | $(\gamma x_i^\top x_j + r)^d$ | Hubungan polinomial |

```python
from sklearn.svm import SVC

# PENSKALAAN WAJIB — SVM berbasis jarak
model = Pipeline([
    ("skala", StandardScaler()),
    ("svm", SVC(kernel="rbf", C=1.0, gamma="scale", probability=True, random_state=42)),
])
```

| Hiperparameter | Pengaruh |
|----------------|----------|
| `C` kecil | Margin lebar, lebih banyak kesalahan ditoleransi → lebih sederhana |
| `C` besar | Margin sempit, kesalahan ditekan → risiko *overfit* |
| `gamma` kecil | Pengaruh tiap titik meluas → batas keputusan halus |
| `gamma` besar | Pengaruh tiap titik sempit → batas keputusan berliku, risiko *overfit* |

> **Keterbatasan penting:** SVM berskala buruk pada data besar (kompleksitas antara $O(n^2)$ dan $O(n^3)$). Pada data di atas puluhan ribu baris, `LinearSVC` atau model lain lebih sesuai.

---

### 10.2 Naive Bayes

#### 10.2.1 Dari Teorema Bayes

$$P(y \mid x_1,\dots,x_p) \propto P(y) \prod_{j=1}^{p} P(x_j \mid y)$$

Tanda perkalian itulah asumsi "naif": **seluruh fitur dianggap saling bebas bila kelasnya diketahui**. Asumsi ini hampir selalu salah dalam kenyataan — dan modelnya sering tetap bekerja baik.

#### 10.2.2 Varian

| Varian | Untuk data | Contoh |
|--------|------------|--------|
| `GaussianNB` | Numerik kontinu | Pengukuran sensor |
| `MultinomialNB` | Cacahan | **Klasifikasi teks** |
| `BernoulliNB` | Biner | Ada/tidaknya kata |
| `CategoricalNB` | Kategorik | Data survei |

| Kelebihan | Kekurangan |
|-----------|------------|
| Sangat cepat dilatih | Asumsi kebebasan sering dilanggar |
| Bekerja pada data kecil | Probabilitas keluarannya kurang terkalibrasi |
| Baik sebagai *baseline* teks | Kalah oleh model lain pada data tabular |

> Naive Bayes layak dicoba sebagai **pembanding cepat** sebelum model yang lebih mahal. Bila model kompleks tidak mengungguli Naive Bayes, ada yang perlu diselidiki.

---

### 10.3 Penyetelan Hiperparameter

#### 10.3.1 Parameter vs Hiperparameter

| | Parameter | Hiperparameter |
|---|-----------|----------------|
| Ditentukan oleh | Proses pelatihan | Manusia atau pencarian |
| Contoh | Koefisien regresi, struktur pohon | `C`, `max_depth`, `n_neighbors` |
| Kapan ditetapkan | Saat `fit` | Sebelum `fit` |

#### 10.3.2 *Grid Search* vs *Random Search*

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from scipy.stats import loguniform

# Grid search — mencoba seluruh kombinasi
ruang_grid = {
    "svm__C": [0.1, 1, 10, 100],
    "svm__gamma": [0.001, 0.01, 0.1, 1],
    "svm__kernel": ["rbf", "linear"],
}
pencarian = GridSearchCV(model, ruang_grid, cv=5, scoring="f1", n_jobs=-1)

# Random search — mencoba n kombinasi acak; lebih efisien pada ruang besar
ruang_acak = {
    "svm__C": loguniform(1e-2, 1e3),
    "svm__gamma": loguniform(1e-4, 1e1),
}
pencarian = RandomizedSearchCV(model, ruang_acak, n_iter=50, cv=5,
                               scoring="f1", random_state=42, n_jobs=-1)

pencarian.fit(X_train, y_train)          # HANYA data latih
print("Terbaik:", pencarian.best_params_)
print("Skor CV:", pencarian.best_score_)
```

> **Perhatikan penamaan `svm__C`.** Dua garis bawah menghubungkan nama langkah dalam `Pipeline` dengan nama parameternya. Dengan begitu parameter prapemrosesan pun dapat disetel dalam pencarian yang sama.

#### 10.3.3 Kesalahan Paling Umum dalam Penyetelan

| Kesalahan | Akibat |
|-----------|--------|
| Menyetel pada data uji | Skor uji menjadi optimistis; kebocoran pemilihan |
| Melaporkan `best_score_` sebagai kinerja akhir | Skor itu sudah dioptimalkan, sehingga bias ke atas |
| Ruang pencarian terlalu sempit | Nilai optimum berada di tepi ruang — perluas |
| Mengabaikan simpangan antarlipatan | Perbedaan yang dilaporkan bisa tidak bermakna |

**Yang benar:** setel pada data latih dengan validasi silang; laporkan kinerja akhir pada data uji yang disentuh **sekali**.

#### 10.3.4 Validasi Silang Bersarang

Bila penyetelan dan penaksiran kinerja harus dilakukan dari data yang sama:

```python
from sklearn.model_selection import cross_val_score, KFold

# Lingkar dalam: memilih hiperparameter
# Lingkar luar: menaksir kinerja
lingkar_dalam = KFold(n_splits=5, shuffle=True, random_state=42)
lingkar_luar  = KFold(n_splits=5, shuffle=True, random_state=7)

pencarian = GridSearchCV(model, ruang_grid, cv=lingkar_dalam, scoring="f1")
skor = cross_val_score(pencarian, X, y, cv=lingkar_luar, scoring="f1")

print(f"Taksiran kinerja yang tidak bias: {skor.mean():.3f} ± {skor.std():.3f}")
```

---

### 10.4 Merancang Perbandingan Model yang Adil

#### 10.4.1 Lima Syarat

| Syarat | Mengapa |
|--------|---------|
| **Lipatan yang sama** untuk seluruh model | Perbedaan lipatan dapat lebih besar daripada perbedaan model |
| **Prapemrosesan yang sesuai** tiap model | Tidak adil membandingkan SVM tanpa penskalaan dengan RF |
| **Anggaran penyetelan yang sebanding** | Model yang disetel 100 kali vs 5 kali bukan perbandingan |
| ***Baseline* disertakan** | Tanpa itu, seluruh angka tidak bermakna |
| **Simpangan dilaporkan** | Selisih 0,01 dengan simpangan 0,05 bukan perbedaan |

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score
import pandas as pd

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)   # SAMA untuk semua

kandidat = {
    "Baseline":       pipeline_dummy,
    "Regresi Logistik": pipeline_logreg,
    "k-NN":           pipeline_knn,
    "SVM (RBF)":      pipeline_svm,
    "Random Forest":  pipeline_rf,
    "Grad. Boosting": pipeline_gb,
}

baris = []
for nama, pipa in kandidat.items():
    skor = cross_val_score(pipa, X_train, y_train, cv=cv, scoring="f1")
    baris.append({"Model": nama, "F1 rerata": skor.mean(),
                  "Simpangan": skor.std(), "Min": skor.min(), "Maks": skor.max()})

tabel = pd.DataFrame(baris).sort_values("F1 rerata", ascending=False)
print(tabel.round(3).to_string(index=False))
```

#### 10.4.2 Membaca Hasil Perbandingan

| Hasil | Tafsir |
|-------|--------|
| Selisih ≫ simpangan | Perbedaan kemungkinan nyata |
| Selisih ≈ simpangan | **Tidak dapat disimpulkan mana yang lebih baik** |
| Seluruh model ≈ *baseline* | Fitur tidak memuat sinyal untuk target ini |
| Model sederhana ≈ model kompleks | **Pilih yang sederhana** — lebih mudah dipelihara dan dijelaskan |

> Baris terakhir adalah kaidah yang sering diabaikan. Model yang lebih rumit hanya sepadan bila peningkatannya nyata dan bermakna secara praktis, bukan sekadar lebih besar pada angka desimal ketiga.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 9 buku ajar](../06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md).
- Meninjau kembali Teorema Bayes dari Probabilitas dan Statistik (Bab 5).

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | Tinjauan; pembahasan T-09 |
| **Kuis 3** | 20' | Protokol eksperimen dan penyetelan |
| Konsep | 30' | SVM dan margin; *kernel*; Naive Bayes |
| Konsep | 25' | Penyetelan hiperparameter; kesalahan umum; CV bersarang |
| Demonstrasi | 40' | **Kegiatan inti:** membangun tabel perbandingan enam model dengan protokol yang adil |
| Penutup | 25' | Membaca hasil; kapan memilih model sederhana; penugasan |

**Diskusi yang wajib muncul:** pada tabel perbandingan, tunjukkan kasus ketika model terbaik hanya unggul 0,004 dari model kedua dengan simpangan 0,03. Tanyakan: model mana yang sebaiknya dipakai, dan mengapa? Jawaban yang diharapkan mempertimbangkan kemudahan pemeliharaan dan keterjelasan, bukan hanya angka.

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 10](../04-labs/lab-10-svm-naive-bayes-penyetelan.md).
- Menyelesaikan Milestone 2 proyek (jatuh tempo Minggu 11).

---

## Penugasan

**T-10 — SVM, Naive Bayes, dan Penyetelan**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook Colab |
| Isi | (a) SVM dengan tiga *kernel*, dalam `Pipeline` berpenskalaan; (b) Naive Bayes sebagai pembanding cepat; (c) `GridSearchCV` **pada data latih saja**; (d) Tabel perbandingan lima model dengan lipatan yang sama, memuat rerata, simpangan, min, dan maks; (e) **Kesimpulan yang memperhatikan simpangan**, bukan hanya rerata |
| Tenggat | Awal pertemuan Minggu 11 |
| Bobot | 1,9% (Observasi) |

---

## Rangkuman

1. SVM mencari pemisah dengan **margin terbesar**; hanya *support vector* yang menentukannya.
2. ***Kernel*** memungkinkan pemisahan non-linear tanpa menghitung pemetaannya secara eksplisit.
3. **SVM wajib diskalakan** dan berskala buruk pada data besar.
4. Naive Bayes mengandaikan **kebebasan antarfitur** — hampir selalu salah, sering tetap berguna.
5. **Hiperparameter disetel sebelum `fit`**; penyetelan dilakukan **hanya pada data latih**.
6. `best_score_` **bukan** kinerja akhir — ia sudah dioptimalkan.
7. Nilai optimum di tepi ruang pencarian berarti ruangnya perlu diperluas.
8. **Validasi silang bersarang** memberi taksiran kinerja yang tidak bias.
9. Perbandingan yang adil menuntut **lipatan sama, anggaran setara, *baseline*, dan pelaporan simpangan**.
10. **Selisih yang lebih kecil daripada simpangan bukan perbedaan.** Bila setara, pilih yang sederhana.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 5. O'Reilly.
2. James, G., et al. (2023). *An Introduction to Statistical Learning with Python*, Bab 9. Springer.
3. Cortes, C., & Vapnik, V. (1995). Support-Vector Networks. *Machine Learning*, 20(3), 273–297.
4. Bergstra, J., & Bengio, Y. (2012). Random Search for Hyper-Parameter Optimization. *JMLR*, 13, 281–305.
5. Cawley, G. C., & Talbot, N. L. C. (2010). On Over-fitting in Model Selection and Subsequent Selection Bias. *JMLR*, 11, 2079–2107.
6. Dokumentasi scikit-learn — *Tuning the hyper-parameters*. <https://scikit-learn.org/stable/modules/grid_search.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
