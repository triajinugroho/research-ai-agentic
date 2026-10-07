# BAB 9: SVM, NAIVE BAYES, DAN PEMILIHAN MODEL

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK082-1` | Menerapkan SVM dengan berbagai *kernel* dan Naive Bayes | C3 |
| `DAIML-Sub-CPMK082-1` | Menyetel hiperparameter tanpa menyentuh data uji | C3 |
| `DAIML-Sub-CPMK082-1` | Merancang protokol perbandingan model yang adil | C6 |

---

## 9.1 Support Vector Machine

### 9.1.1 Margin Maksimum

```
        ×  ×            │      ○
     ×     ×      ┊     │    ┊    ○   ○
        ×      ┊        │       ┊   ○
    ×       ┊           │          ┊    ○
          ┊             │             ┊
      ─────┴────────────┴──────────────┴─────
        margin    hiperbidang    margin

    × dan ○ yang MENYENTUH garis putus-putus adalah
    support vector — hanya mereka yang menentukan
    posisi hiperbidang.
```

SVM tidak sekadar mencari pemisah; ia mencari pemisah dengan **jarak terbesar** ke titik terdekat dari kedua kelas. Gagasan ini memberi ketahanan: pemisah berjarak lebar lebih mungkin bertahan pada data baru.

Sifat lain yang menarik: **hanya sebagian kecil titik yang menentukan modelnya**. Menggeser titik yang jauh dari margin tidak mengubah apa pun.

### 9.1.2 *Kernel*

Ketika data tidak terpisahkan secara linear, *kernel* memetakannya ke ruang berdimensi lebih tinggi tempat pemisahan linear menjadi mungkin — **tanpa menghitung pemetaan itu secara eksplisit** (*kernel trick*).

| Kernel | Bentuk | Kapan dipakai |
|--------|--------|---------------|
| `linear` | $x_i^\top x_j$ | Data berdimensi tinggi; teks |
| `rbf` | $\exp(-\gamma\lVert x_i-x_j\rVert^2)$ | **Baku; paling serbaguna** |
| `poly` | $(\gamma x_i^\top x_j+r)^d$ | Hubungan polinomial |

```python
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# PENSKALAAN WAJIB — SVM berbasis jarak
model = Pipeline([
    ("skala", StandardScaler()),
    ("svm", SVC(kernel="rbf", C=1.0, gamma="scale", random_state=42)),
])
```

| Hiperparameter | Pengaruh |
|----------------|----------|
| `C` kecil | Margin lebar, kesalahan lebih ditoleransi → model lebih sederhana |
| `C` besar | Margin sempit, kesalahan ditekan → risiko *overfit* |
| `gamma` kecil | Pengaruh tiap titik meluas → batas keputusan halus |
| `gamma` besar | Pengaruh tiap titik sempit → batas berliku, risiko *overfit* |

> **Keterbatasan penting:** SVM berskala buruk pada data besar (kompleksitas antara $O(n^2)$ dan $O(n^3)$). Pada data di atas puluhan ribu baris, `LinearSVC` atau model lain lebih sesuai.

---

## 9.2 Naive Bayes

### 9.2.1 Dari Teorema Bayes

$$P(y\mid x_1,\dots,x_p)\propto P(y)\prod_{j=1}^{p}P(x_j\mid y)$$

Tanda perkalian itulah asumsi "naif": **seluruh fitur dianggap saling bebas bila kelasnya diketahui**. Asumsi ini hampir selalu salah dalam kenyataan — dan modelnya sering tetap bekerja baik.

Mengapa demikian? Karena untuk **klasifikasi**, yang dibutuhkan hanyalah urutan probabilitas yang benar, bukan nilai probabilitas yang tepat. Asumsi kebebasan sering merusak nilainya tanpa merusak urutannya.

### 9.2.2 Varian

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

> Naive Bayes layak dicoba sebagai **pembanding cepat** sebelum model yang lebih mahal. Bila model kompleks tidak mengungguli Naive Bayes secara bermakna, ada yang perlu diselidiki — biasanya pada fiturnya.

---

## 9.3 Penyetelan Hiperparameter

### 9.3.1 Parameter vs Hiperparameter

| | Parameter | Hiperparameter |
|---|-----------|----------------|
| Ditentukan oleh | Proses pelatihan | Manusia atau pencarian |
| Contoh | Koefisien regresi, struktur pohon | `C`, `max_depth`, `n_neighbors` |
| Kapan ditetapkan | Saat `fit` | **Sebelum** `fit` |

### 9.3.2 *Grid* dan *Random Search*

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from scipy.stats import loguniform

ruang_grid = {
    "svm__C":     [0.1, 1, 10, 100],
    "svm__gamma": [0.001, 0.01, 0.1, "scale"],
}
pencarian = GridSearchCV(model, ruang_grid, cv=5, scoring="f1", n_jobs=-1)

# Random search lebih efisien pada ruang besar
ruang_acak = {"svm__C": loguniform(1e-2, 1e3),
              "svm__gamma": loguniform(1e-4, 1e1)}
pencarian = RandomizedSearchCV(model, ruang_acak, n_iter=50, cv=5,
                               scoring="f1", random_state=42, n_jobs=-1)

pencarian.fit(X_train, y_train)      # HANYA data latih
```

> **Perhatikan penamaan `svm__C`.** Dua garis bawah menghubungkan nama langkah dalam `Pipeline` dengan nama parameternya — sehingga parameter prapemrosesan pun dapat disetel dalam pencarian yang sama.

### 9.3.3 Empat Kesalahan Umum

| Kesalahan | Akibat |
|-----------|--------|
| Menyetel pada data uji | Skor uji menjadi optimistis; kebocoran pemilihan |
| Melaporkan `best_score_` sebagai kinerja akhir | Skor itu **sudah dioptimalkan**, sehingga bias ke atas |
| Ruang pencarian terlalu sempit | Nilai optimum berada di tepi ruang — harus diperluas |
| Mengabaikan simpangan antarlipatan | Perbedaan yang dilaporkan bisa tidak bermakna |

Yang benar: setel pada data latih dengan validasi silang; laporkan kinerja akhir pada data uji yang disentuh **sekali**.

### 9.3.4 Validasi Silang Bersarang

Bila penyetelan dan penaksiran kinerja harus dilakukan dari data yang sama:

```python
from sklearn.model_selection import cross_val_score, StratifiedKFold

dalam = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
luar  = StratifiedKFold(n_splits=5, shuffle=True, random_state=7)

pencarian = GridSearchCV(model, ruang_grid, cv=dalam, scoring="f1")
skor = cross_val_score(pencarian, X, y, cv=luar, scoring="f1")
print(f"Taksiran tidak bias: {skor.mean():.3f} ± {skor.std(ddof=1):.3f}")   # ddof=1: SD sampel
```

Lingkar dalam memilih hiperparameter; lingkar luar menaksir kinerja. Karena pemilihan terjadi **di dalam** tiap lipatan luar, taksirannya tidak terkontaminasi oleh proses pemilihan.

---

## 9.4 Merancang Perbandingan yang Adil

### 9.4.1 Lima Syarat

| Syarat | Mengapa |
|--------|---------|
| **Lipatan yang sama** untuk seluruh model | Perbedaan antarlipatan dapat lebih besar daripada perbedaan antarmodel |
| **Prapemrosesan yang sesuai** tiap model | Tidak adil membandingkan SVM tanpa penskalaan dengan *Random Forest* |
| **Anggaran penyetelan yang sebanding** | Model yang disetel 100 kali vs 5 kali bukan perbandingan |
| ***Baseline* disertakan** | Tanpa itu seluruh angka tidak bermakna |
| **Simpangan dan selisih per lipatan dilaporkan** | Selisih rerata 0,01 baru bermakna bila konsisten antarlipatan — diukur dengan selisih berpasangan (§9.4.2), bukan dengan membandingkannya pada simpangan masing-masing model |

### 9.4.2 Membaca Hasil Perbandingan

Karena seluruh model dinilai pada **lipatan yang sama**, skor dua model **berpasangan**: pada lipatan ke-$i$, keduanya diuji pada baris yang persis sama. Sebagian variasi skor berasal dari lipatannya sendiri — ada lipatan yang "mudah" dan ada yang "sulit" — dan dialami kedua model bersama-sama. Selisih per lipatan menghapus variasi bersama itu.

Untuk $k$ lipatan, hitung selisih per lipatan $d_i = \text{skor}_{A,i} - \text{skor}_{B,i}$, lalu rerata, simpangan baku sampel, dan galat baku (*standard error*) rerata selisih:

$$\bar d=\frac{1}{k}\sum_{i=1}^{k} d_i \qquad s_d=\sqrt{\frac{1}{k-1}\sum_{i=1}^{k}\left(d_i-\bar d\right)^2} \qquad SE=\frac{s_d}{\sqrt{k}}$$

```python
import numpy as np

# skor_a, skor_b: skor per lipatan dari cross_val_score dengan objek CV yang SAMA
d = np.asarray(skor_a) - np.asarray(skor_b)
k = len(d)
d_bar = d.mean()
s_d = d.std(ddof=1)           # simpangan baku SAMPEL (ddof=1), sama dengan pd.Series.std()
se = s_d / np.sqrt(k)
searah = int((np.sign(d) == np.sign(d_bar)).sum())   # lipatan yang searah dengan rerata
bermakna = abs(d_bar) > 2 * se and searah >= 0.8 * k
print(f"rerata selisih = {d_bar:.4f} | s_d = {s_d:.4f} | SE = {se:.4f} | "
      f"searah di {searah} dari {k} lipatan | bermakna: {bermakna}")
```

| Hasil | Tafsir |
|-------|--------|
| $\lvert\bar d\rvert > 2\cdot SE$ **dan** arah selisih konsisten di sebagian besar lipatan (pada 5 lipatan: minimal 4) | Perbedaan kemungkinan nyata |
| $\lvert\bar d\rvert \le 2\cdot SE$, atau arah selisih berganti-ganti antarlipatan | **Tidak dapat disimpulkan mana yang lebih baik** |
| Seluruh model ≈ *baseline* | Fitur tidak memuat sinyal untuk target ini |
| Model sederhana ≈ model kompleks | **Pilih yang sederhana** |

Aturan $|\bar d| > 2\cdot SE$ adalah **aturan praktis mata kuliah** — penyaring kasar, karena skor antarlipatan tidak benar-benar saling bebas (data latihnya tumpang-tindih). Untuk analisis formal, gunakan *corrected resampled t-test* (Nadeau & Bengio, 2003).

> **Jangan pakai "simpangan gabungan" $\sqrt{s_1^2+s_2^2}$.** Rumus itu memperlakukan skor kedua model seolah-olah tidak berpasangan dan memakai simpangan baku (SD) skor masing-masing model, padahal ketidakpastian **rerata selisih** diukur oleh galat baku (SE) dari selisih per lipatan. Akibatnya, selisih yang konsisten di semua lipatan dapat dinyatakan "tidak bermakna" hanya karena kedua model sama-sama naik-turun dari lipatan ke lipatan. Seragamkan pula cara menghitung simpangan baku skor lipatan: selalu **`ddof=1`** — `np.std(x, ddof=1)` atau `pd.Series.std()`; `np.std(x)` dan `skor.std()` pada larik NumPy tanpa argumen memakai `ddof=0`.

> Baris terakhir tabel di atas — *model sederhana ≈ model kompleks* — adalah kaidah yang sering diabaikan. Model yang lebih rumit hanya sepadan bila peningkatannya nyata dan bermakna **secara praktis** — bukan sekadar lebih besar pada angka desimal ketiga. Model yang lebih sederhana lebih mudah dipelihara, lebih cepat dijalankan, lebih mudah dijelaskan, dan lebih jarang rusak.

---

## AI Corner — Tahap *Apply*

### Penyetelan Adalah Tempat Kebocoran Paling Mudah Terjadi

Diminta menuliskan kode penyetelan hiperparameter, model bahasa sangat sering menghasilkan pola berikut:

```python
# Pola yang sering muncul — dan SALAH
pencarian = GridSearchCV(model, ruang, cv=5)
pencarian.fit(X, y)                       # ← seluruh data
print("Skor terbaik:", pencarian.best_score_)
```

Dua kekeliruan sekaligus: penyetelan memakai seluruh data (termasuk yang seharusnya menjadi uji), dan `best_score_` dilaporkan sebagai kinerja akhir.

Kekeliruan ini lolos dengan mudah karena kodenya berjalan tanpa galat dan menghasilkan angka yang masuk akal. Ia hanya dapat dikenali oleh seseorang yang memahami mengapa `best_score_` bias ke atas.

### Memeriksa, Bukan Menyerahkan

```
Saya menjalankan GridSearchCV pada X_train saja, dengan cv=5,
lalu melaporkan skor pada X_test yang belum pernah disentuh.

Nilai C terbaik yang ditemukan adalah nilai terbesar pada rentang
yang saya coba (C=100 dari [0.1, 1, 10, 100]).

Pertanyaan saya: apa artinya optimum berada di tepi rentang, dan
apa yang sebaiknya saya lakukan?
```

Prompt ini menunjukkan bahwa prosedurnya sudah benar, dan yang ditanyakan adalah penafsiran atas gejala — pemakaian yang tepat.

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan apa yang dimaksud *support vector*, dan mengapa hanya sebagian kecil titik menentukan model SVM.

2. Mengapa SVM wajib diskalakan sementara *Random Forest* tidak?

3. Jelaskan asumsi "naif" pada Naive Bayes, dan mengapa modelnya sering tetap berguna meski asumsi itu dilanggar.

4. Sebutkan lima syarat perbandingan model yang adil.

### Tingkat Menengah

5. Sebuah `GridSearchCV` melaporkan `best_score_` 0,872, sementara skor pada data uji adalah 0,841.
   (a) Mengapa keduanya berbeda?
   (b) Mana yang harus dilaporkan sebagai kinerja akhir?
   (c) Apakah selisih 0,031 mengkhawatirkan? Faktor apa yang menentukannya?
   (d) Bagaimana cara memperoleh taksiran yang tidak bias tanpa data uji terpisah?

6. Parameter terbaik yang ditemukan adalah `C=100` dan `gamma=0.001`, keduanya di ujung rentang yang dicoba.
   (a) Apa yang ditunjukkan hal ini?
   (b) Apa yang harus dilakukan?
   (c) Bila setelah perluasan, `C=10000` menjadi yang terbaik, apa yang Anda simpulkan tentang datanya?
   (d) Risiko apa yang menyertai `C` yang sangat besar?

7. Sebuah tim menyetel *Random Forest* dengan 6 kombinasi dan SVM dengan 96 kombinasi, lalu menyimpulkan SVM lebih baik.
   (a) Apakah perbandingan ini adil? Jelaskan.
   (b) Apa yang harus diperbaiki?
   (c) Selain jumlah kombinasi, apa lagi yang harus disetarakan?
   (d) Bagaimana bila menyetarakan anggaran tidak memungkinkan karena keterbatasan waktu?

8. Dua model dinilai dengan validasi silang 5 lipatan pada **lipatan yang sama**. F1 per lipatan:

   | Lipatan | 1 | 2 | 3 | 4 | 5 |
   |---------|---|---|---|---|---|
   | Model A | 0,832 | 0,871 | 0,845 | 0,889 | 0,868 |
   | Model B | 0,847 | 0,865 | 0,857 | 0,885 | 0,886 |

   (a) Hitung selisih per lipatan $d_i$ = B − A, lalu $\bar d$, $s_d$ (`ddof=1`), dan $SE$.
   (b) Apakah selisihnya bermakna menurut aturan praktis mata kuliah (§9.4.2)? Periksa juga arah selisih di tiap lipatan.
   (c) Bila Model A jauh lebih cepat dan lebih mudah dijelaskan, apa rekomendasi Anda?
   (d) Bagaimana Anda menuliskan kesimpulan ini dalam laporan?

### Tingkat Mahir

9. Rancang dan jalankan perbandingan enam model yang adil.
   (a) Pilih masalah klasifikasi pada data nyata.
   (b) Sertakan *baseline*, satu model linear, satu berbasis jarak, dua berbasis pohon, dan Naive Bayes.
   (c) Pakai lipatan yang sama dan anggaran penyetelan yang sebanding.
   (d) Laporkan rerata, simpangan baku sampel (`ddof=1`), min, maks, dan waktu latih.
   (e) Hitung selisih berpasangan per lipatan antara peringkat 1 dan 2, lalu terapkan aturan praktis $|\bar d| > 2\cdot SE$ beserta pemeriksaan arah selisih.
   (f) Tuliskan rekomendasi yang mempertimbangkan kinerja, waktu, keterjelasan, dan kemudahan pemeliharaan.

10. Selidiki batas skala SVM.
    (a) Jalankan SVM pada data berukuran 500, 1.000, 2.000, 5.000, dan 10.000 baris.
    (b) Catat waktu latih masing-masing.
    (c) Buat grafik waktu terhadap jumlah baris pada skala log-log.
    (d) Taksir pangkat kompleksitasnya dari kemiringan garis.
    (e) Bandingkan dengan `LinearSVC` dan `SGDClassifier` pada ukuran yang sama.
    (f) Pada ukuran berapa SVM menjadi tidak praktis untuk kerja sehari-hari?

11. Bandingkan validasi silang biasa dan bersarang secara empiris.
    (a) Jalankan `GridSearchCV` dengan ruang pencarian besar; catat `best_score_`.
    (b) Jalankan validasi silang bersarang pada data yang sama; catat hasilnya.
    (c) Ulangi keduanya dengan ruang pencarian yang jauh lebih kecil.
    (d) Bandingkan selisih antara `best_score_` dan taksiran bersarang pada kedua ukuran ruang.
    (e) Jelaskan mengapa selisihnya berbeda, dan apa artinya bagi praktik pelaporan.

---

## Rangkuman

1. SVM mencari pemisah dengan **margin terbesar**; hanya *support vector* yang menentukannya.
2. ***Kernel*** memungkinkan pemisahan non-linear tanpa menghitung pemetaannya secara eksplisit.
3. **SVM wajib diskalakan** dan berskala buruk pada data besar.
4. Naive Bayes mengandaikan **kebebasan antarfitur** — hampir selalu salah, sering tetap berguna, karena klasifikasi hanya membutuhkan urutan yang benar.
5. **Hiperparameter ditetapkan sebelum `fit`**; penyetelan dilakukan **hanya pada data latih**.
6. `best_score_` **bukan** kinerja akhir — ia sudah dioptimalkan atas ruang pencarian.
7. Nilai optimum di tepi ruang berarti ruangnya **perlu diperluas**.
8. **Validasi silang bersarang** memberi taksiran kinerja yang tidak bias.
9. Perbandingan adil menuntut **lipatan sama, anggaran setara, *baseline*, dan pelaporan simpangan**.
10. Karena lipatannya sama, skor dua model **berpasangan**: bandingkan dengan **selisih per lipatan** — $\bar d$, $s_d$ (`ddof=1`), $SE = s_d/\sqrt{k}$. Selisih dianggap bermakna bila $|\bar d| > 2\cdot SE$ dan arahnya konsisten; bukan dengan "simpangan gabungan" $\sqrt{s_1^2+s_2^2}$. Bila setara, **pilih yang sederhana**.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 5. O'Reilly.
2. James, G., et al. (2023). *An Introduction to Statistical Learning with Python*, Bab 9. Springer.
3. Cortes, C., & Vapnik, V. (1995). Support-Vector Networks. *Machine Learning*, 20(3), 273–297.
4. Bergstra, J., & Bengio, Y. (2012). Random Search for Hyper-Parameter Optimization. *JMLR*, 13, 281–305.
5. Cawley, G. C., & Talbot, N. L. C. (2010). On Over-fitting in Model Selection and Subsequent Selection Bias. *JMLR*, 11, 2079–2107.
6. Dokumentasi scikit-learn — *Tuning the hyper-parameters*. <https://scikit-learn.org/stable/modules/grid_search.html>
7. Nadeau, C., & Bengio, Y. (2003). Inference for the Generalization Error. *Machine Learning*, 52(3), 239–281.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
