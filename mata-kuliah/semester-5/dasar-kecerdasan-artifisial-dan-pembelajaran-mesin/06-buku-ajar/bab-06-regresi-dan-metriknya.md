# BAB 6: REGRESI DAN METRIKNYA

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK082-1` | Membangun model regresi linear dan berregularisasi | C3 |
| `DAIML-Sub-CPMK082-1` | Menghitung dan menafsirkan MAE, RMSE, R², dan MAPE | C3–C4 |
| `DAIML-Sub-CPMK082-1` | Menganalisis kondisi model melalui tukar-tambah bias–varians | C4 |

---

## 6.1 Regresi Linear

### 6.1.1 Bentuk Model

$$\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_p x_p$$

Pelatihan berarti mencari koefisien $\beta$ yang meminimalkan **jumlah kuadrat residual**:

$$\text{SSR} = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

### 6.1.2 Menafsirkan Koefisien

$$\widehat{\text{harga}} = 120 + 8{,}5\cdot\text{luas} + 45\cdot\text{kamar} - 12\cdot\text{jarak\_pusat}$$

| Koefisien | Tafsir yang benar |
|-----------|-------------------|
| $\beta_{\text{luas}}=8{,}5$ | Setiap penambahan 1 m², dengan fitur lain tetap, **dikaitkan dengan** kenaikan harga 8,5 juta |
| $\beta_{\text{jarak}}=-12$ | Setiap penambahan 1 km jarak, dikaitkan dengan penurunan 12 juta |
| $\beta_0=120$ | Nilai ketika seluruh fitur nol — **sering tanpa makna nyata** |

> **Kata "dikaitkan dengan", bukan "menyebabkan".** Ini bukan kehati-hatian berlebihan: data observasional tidak mendukung klaim sebab-akibat, sebagaimana sudah dipelajari pada Probabilitas dan Statistik. Pada penilaian mata kuliah ini, menulis interpretasi dengan bahasa sebab-akibat pada data observasional dikenai pengurangan nilai.

### 6.1.3 Asumsi dan Pemeriksaannya

| Asumsi | Akibat bila dilanggar | Pemeriksaan |
|--------|-----------------------|-------------|
| Hubungan linear | Model kehilangan pola | Plot residual vs prediksi |
| Residual bebas | Galat baku menyesatkan | Urutan residual |
| Varians residual seragam | Interval prediksi tidak sah | Plot residual — pola corong |
| Residual normal | Uji signifikansi tidak sah | Q-Q plot |
| Tanpa multikolinearitas ekstrem | Koefisien tidak stabil | VIF; matriks korelasi |

---

## 6.2 Regresi Polinomial dan *Overfitting*

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

model = Pipeline([
    ("poli", PolynomialFeatures(degree=3, include_bias=False)),
    ("regresi", LinearRegression()),
])
```

| Derajat | Perilaku | Kondisi |
|---------|----------|---------|
| 1 | Garis lurus | Sering *underfit* pada hubungan melengkung |
| 2–3 | Lengkungan sedang | Biasanya memadai |
| ≥ 5 | Mengikuti setiap titik data | ***Overfit*** |

Tanda pengenalnya: R² data latih mendekati 1,0 sementara R² data uji rendah atau **negatif**.

> R² negatif bukan galat perhitungan. Ia berarti model **lebih buruk daripada sekadar menebak rata-rata** — yaitu lebih buruk daripada *baseline*.

---

## 6.3 Regularisasi

### 6.3.1 Gagasannya

Menambahkan denda atas besarnya koefisien ke dalam fungsi yang diminimalkan:

| Metode | Fungsi objektif | Pengaruh khas |
|--------|-----------------|---------------|
| **Ridge (L2)** | $\text{SSR}+\alpha\sum\beta_j^2$ | Mengecilkan koefisien; **tidak** menolkannya |
| **Lasso (L1)** | $\text{SSR}+\alpha\sum\lvert\beta_j\rvert$ | Dapat menolkan koefisien → **sekaligus memilih fitur** |
| **Elastic Net** | Gabungan L1 dan L2 | Kompromi keduanya |

```python
from sklearn.linear_model import RidgeCV, LassoCV
from sklearn.preprocessing import StandardScaler
import numpy as np

# PENSKALAAN WAJIB — regularisasi mendenda BESARNYA koefisien
model = Pipeline([
    ("skala", StandardScaler()),
    ("ridge", RidgeCV(alphas=np.logspace(-3, 3, 50), cv=5)),
])
model.fit(X_train, y_train)
print("Alpha terpilih:", model.named_steps["ridge"].alpha_)
```

### 6.3.2 Mengapa Penskalaan Wajib

Denda dihitung atas besarnya koefisien. Fitur berskala besar memperoleh koefisien kecil — bukan karena kurang penting, melainkan **semata-mata karena satuannya** — sehingga terdenda lebih ringan. Tanpa penskalaan, regularisasi menghukum fitur secara tidak adil.

### 6.3.3 Pengaruh α

| α | Pengaruh | Risiko |
|---|----------|--------|
| 0 | Sama dengan regresi biasa | *Overfitting* |
| Kecil (0,01–1) | Pengecilan ringan | Biasanya tepat |
| Besar (10–100) | Pengecilan kuat | *Underfitting* |
| Sangat besar | Seluruh koefisien → 0 | Model menjadi konstanta |

**α ditentukan melalui validasi silang, bukan ditebak.** Bila α terbaik berada di tepi rentang yang dicoba, rentangnya perlu diperluas.

---

## 6.4 Metrik Regresi

### 6.4.1 Empat Metrik Pokok

| Metrik | Rumus | Satuan | Sifat |
|--------|-------|--------|-------|
| **MAE** | $\frac{1}{n}\sum\lvert y_i-\hat{y}_i\rvert$ | Sama dengan target | Tahan pencilan; mudah ditafsirkan |
| **RMSE** | $\sqrt{\frac{1}{n}\sum(y_i-\hat{y}_i)^2}$ | Sama dengan target | Menghukum galat besar |
| **R²** | $1-\frac{SS_{res}}{SS_{tot}}$ | Tanpa satuan | Proporsi keragaman terjelaskan |
| **MAPE** | $\frac{100\%}{n}\sum\left\lvert\frac{y_i-\hat{y}_i}{y_i}\right\rvert$ | Persen | Galat relatif; **gagal bila ada $y_i=0$** |

### 6.4.2 Perhitungan Manual

Prediksi harga rumah (juta rupiah):

| Sebenarnya | Prediksi | Galat | \|Galat\| | Galat² | \|Galat\|/y |
|------------|----------|-------|-----------|--------|-------------|
| 800 | 750 | −50 | 50 | 2.500 | 0,0625 |
| 1.200 | 1.150 | −50 | 50 | 2.500 | 0,0417 |
| 600 | 640 | +40 | 40 | 1.600 | 0,0667 |
| 2.000 | 1.400 | −600 | 600 | 360.000 | 0,3000 |
| 900 | 920 | +20 | 20 | 400 | 0,0222 |
| | **Jumlah** | | **760** | **367.000** | **0,4931** |

$$\text{MAE}=\frac{760}{5}=152 \qquad \text{MSE}=\frac{367.000}{5}=73.400 \qquad \text{RMSE}=\sqrt{73.400}\approx 271$$
$$\text{MAPE}=\frac{0{,}4931}{5}\times 100\%\approx 9{,}9\%$$

**Yang harus diperhatikan:** RMSE (271) jauh lebih besar daripada MAE (152). Selisih itu **seluruhnya** berasal dari satu pengamatan — rumah 2.000 juta yang meleset 600 juta.

| Metrik | Kesimpulannya |
|--------|---------------|
| MAE = 152 | "Rata-rata meleset 152 juta" |
| RMSE = 271 | "Ada kesalahan besar yang perlu diperhatikan" |
| MAPE = 9,9% | "Secara relatif cukup baik" |

Ketiganya benar. Yang dipilih bergantung pada **apakah kesalahan besar merugikan secara tidak proporsional**.

### 6.4.3 Rasio RMSE/MAE sebagai Petunjuk

| Rasio | Tafsir |
|-------|--------|
| Mendekati 1,0 | Galat tersebar merata |
| 1,2–1,5 | Ada beberapa galat besar |
| > 2,0 | Sedikit galat sangat besar mendominasi RMSE — **selidiki kasusnya** |

Pada contoh §6.4.2, rasionya 271/152 ≈ 1,78 — petunjuk bahwa ada kasus yang layak diperiksa satu per satu.

### 6.4.4 Memilih Metrik

| Situasi | Metrik | Alasan |
|---------|--------|--------|
| Semua kesalahan setara | **MAE** | Mudah ditafsirkan; tahan pencilan |
| Kesalahan besar jauh lebih buruk | **RMSE** | Menghukum secara kuadratik |
| Perlu perbandingan lintas skala | **R²** | Tanpa satuan |
| Kesalahan relatif yang penting | **MAPE** | Persentase |
| Target memuat nilai nol | **Hindari MAPE** | Pembagian nol |
| Target sangat menceng | **MAE** | RMSE didominasi nilai besar |

> **Ketentuan mata kuliah ini:** laporkan sekurang-kurangnya MAE dan RMSE bersama-sama. Keduanya menceritakan hal yang berbeda, dan **selisihnya sendiri adalah informasi**.

---

## 6.5 Tukar-Tambah Bias dan Varians

### 6.5.1 Uraian Galat

$$\text{Galat} = \text{Bias}^2 + \text{Varians} + \text{Galat tak tereduksi}$$

| Komponen | Makna | Penyebab |
|----------|-------|----------|
| **Bias** | Kekeliruan sistematis | Model terlalu sederhana untuk pola yang ada |
| **Varians** | Kepekaan terhadap data latih | Model terlalu kompleks |
| **Tak tereduksi** | Derau dalam data | Tidak dapat dihilangkan model apa pun |

```
   Galat
     ▲
     │  ╲                                   ╱
     │   ╲        Galat total             ╱
     │    ╲                             ╱
     │     ╲___                      ╱
     │         ╲___             ___╱      ← Varians
     │             ╲________ ___╱
     │   Bias²  ╲___________╱
     │              ╲___________________
     └──────────────────┬──────────────────────► Kompleksitas
                    optimum
      UNDERFIT                         OVERFIT
```

### 6.5.2 Mengenali Kondisi Model

| Kondisi | Galat latih | Galat validasi | Tindakan |
|---------|-------------|----------------|----------|
| ***Underfit*** | Tinggi | Tinggi | Tambah kompleksitas; tambah fitur; kurangi regularisasi |
| **Pas** | Rendah | Rendah | — |
| ***Overfit*** | **Sangat rendah** | Tinggi | Tambah data; kurangi fitur; **tambah regularisasi**; sederhanakan model |

Diagnosis melalui kurva pembelajaran dibahas pada Bab 11.

---

## AI Corner — Tahap *Apply*

### Memakai AI untuk Kode, Bukan untuk Pemilihan Metrik

Pada bab ini bantuan AI menjadi sangat praktis: sintaks `RidgeCV`, cara membuat plot residual, cara membaca `coef_` dari `Pipeline`. Semua itu adalah pekerjaan sintaksis yang tepat diserahkan.

Yang **tidak** boleh diserahkan adalah pemilihan metrik — dan alasannya dapat ditunjukkan dengan contoh.

Diminta "metrik apa untuk masalah regresi ini?", model bahasa hampir selalu menjawab RMSE atau R². Jawaban itu lazim dalam teks yang melatihnya, dan ia keliru pada sejumlah kasus nyata:

| Kasus | Jawaban khas AI | Yang sebenarnya tepat |
|-------|-----------------|-----------------------|
| Perkiraan lama antrean puskesmas | RMSE | **MAE** — "meleset 7 menit" dapat dipahami petugas |
| Perkiraan kebutuhan stok obat, dengan sebagian item bernilai 0 | MAPE | **MAE** — MAPE gagal pada nol |
| Perkiraan harga properti, kesalahan besar sangat mahal | R² | **RMSE** — R² tidak menunjukkan besaran galat |

Pemilihan yang tepat menuntut jawaban atas pertanyaan yang tidak ada dalam prompt: **berapa biaya sebuah kesalahan, dan apakah biaya itu tumbuh sebanding atau lebih cepat daripada besarnya kesalahan?**

### Pemakaian yang Wajar

```
Saya memprediksi lama antrean puskesmas dalam menit. Rentangnya
5–120 menit, dengan beberapa kasus ekstrem di atas 180 menit yang
SAH (bukan kesalahan pencatatan).

Keputusan saya: memakai MAE sebagai metrik utama, karena keluarannya
akan dibaca petugas sebagai "perkiraan meleset sekian menit", dan
karena kasus ekstrem yang sah tidak seharusnya mendominasi ukuran.

Saya tetap melaporkan RMSE sebagai pendamping.

Tolong periksa penalaran ini — apa yang mungkin saya lewatkan?
```

---

## Latihan Soal

### Tingkat Dasar

1. Tafsirkan koefisien berikut dengan bahasa yang benar: model memperkirakan IPM kabupaten, dan $\beta_{\text{rata\_lama\_sekolah}} = 2{,}4$.

2. Sebuah model memperoleh R² latih 0,98 dan R² uji −0,12.
   (a) Kondisi apa ini?
   (b) Apa arti R² negatif?
   (c) Sebutkan dua tindakan yang tepat.

3. Jelaskan perbedaan Ridge dan Lasso, dan sebutkan satu keadaan ketika masing-masing lebih disukai.

4. Mengapa penskalaan wajib dilakukan sebelum regularisasi? Jelaskan dalam dua kalimat.

### Tingkat Menengah

5. Sebuah model regresi menghasilkan MAE 12,4 dan RMSE 31,8 pada data uji.
   (a) Hitung rasio RMSE/MAE.
   (b) Apa yang ditunjukkan rasio ini?
   (c) Apa yang akan Anda periksa selanjutnya?
   (d) Bila ternyata ada tiga kasus dengan galat sangat besar, apa dua kemungkinan penjelasannya?

6. Sebuah tim melaporkan MAPE 8% untuk model perkiraan kebutuhan stok obat. Sebagian item memiliki kebutuhan aktual 0 pada beberapa periode.
   (a) Masalah apa yang timbul?
   (b) Apa yang mungkin dilakukan tim itu terhadap baris bernilai nol?
   (c) Mengapa tindakan itu membuat MAPE menyesatkan?
   (d) Metrik apa yang sebaiknya dipakai?

7. `LassoCV` menolkan 7 dari 20 koefisien.
   (a) Apa artinya bagi ketujuh fitur itu?
   (b) Apakah berarti ketujuhnya "tidak berguna"? Jelaskan.
   (c) Apa yang terjadi bila dua fitur berkorelasi sangat kuat?
   (d) Bagaimana cara memeriksa apakah penolkan itu stabil?

8. Alpha terbaik yang ditemukan `RidgeCV` adalah 1000, yaitu nilai terbesar pada rentang `np.logspace(-3, 3, 50)`.
   (a) Apa yang ditunjukkan hal ini?
   (b) Apa yang harus dilakukan?
   (c) Apa yang mungkin terjadi pada model bila α benar-benar harus sebesar itu?
   (d) Apa dugaan Anda tentang data tersebut?

### Tingkat Mahir

9. Bandingkan tiga model regresi secara lengkap pada data nyata.
   (a) Pilih dataset harga atau indikator berkonteks Indonesia.
   (b) Bangun *baseline* `DummyRegressor`.
   (c) Latih regresi linear, Ridge, dan Lasso dalam `Pipeline` berpenskalaan.
   (d) Tentukan α dengan validasi silang; periksa apakah berada di tepi rentang.
   (e) Laporkan MAE, RMSE, R², MAPE untuk seluruhnya.
   (f) Jelaskan mengapa peringkat model berbeda antarmetrik — atau mengapa tidak.

10. Selidiki pengaruh transformasi target.
    (a) Latih model pada target asli, catat metriknya.
    (b) Latih pada $\log(\text{target})$, kembalikan prediksinya dengan $\exp$, catat metriknya.
    (c) Bandingkan MAE, RMSE, dan MAPE keduanya.
    (d) Jelaskan mengapa transformasi memengaruhi ketiganya secara berbeda.
    (e) Untuk masalah itu, mana yang sebaiknya dipakai dan mengapa?

11. Demonstrasikan tukar-tambah bias–varians secara empiris.
    (a) Bangkitkan data dengan hubungan melengkung dan derau yang diketahui.
    (b) Latih regresi polinomial derajat 1 sampai 12.
    (c) Catat galat latih dan galat uji untuk masing-masing.
    (d) Buat grafik keduanya terhadap derajat.
    (e) Tandai titik optimum, dan tunjukkan daerah *underfit* serta *overfit*.
    (f) Ulangi dengan regularisasi Ridge dan jelaskan bagaimana kurvanya berubah.

---

## Rangkuman

1. Regresi linear mencari koefisien yang meminimalkan **jumlah kuadrat residual**.
2. Koefisien ditafsirkan dengan **"dikaitkan dengan"**, bukan "menyebabkan".
3. **R² uji negatif berarti lebih buruk daripada *baseline***.
4. **Ridge mengecilkan; Lasso dapat menolkan** → Lasso sekaligus memilih fitur.
5. **Penskalaan wajib sebelum regularisasi**, karena denda dihitung atas besarnya koefisien.
6. α ditentukan lewat **validasi silang**; α optimum di tepi rentang berarti rentangnya perlu diperluas.
7. **MAE tahan pencilan; RMSE menghukum galat besar.** Selisih keduanya sendiri adalah informasi.
8. **Rasio RMSE/MAE** menunjukkan apakah ada sedikit galat yang mendominasi.
9. **MAPE gagal bila target memuat nol.**
10. Galat = **bias² + varians + galat tak tereduksi**; *underfit* dan *overfit* dikenali dari selisih galat latih dan validasi.

---

## Referensi

1. James, G., et al. (2023). *An Introduction to Statistical Learning with Python*, Bab 3 dan 6. Springer.
2. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 4. O'Reilly.
3. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*, Bab 3. Springer.
4. Dokumentasi scikit-learn — *Linear Models*. <https://scikit-learn.org/stable/modules/linear_model.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
