# Minggu 6: Regresi dan Metriknya

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 6 dari 16 |
| Topik | Regresi linear, polinomial, regularisasi; MAE, RMSE, R², MAPE; bias–varians |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-06 |
| Bloom | C3 (Menerapkan) → C5 (Mengevaluasi) |
| Durasi | 150 menit |
| Metode | Kuliah · Turunan manual · Praktikum |
| Penilaian | Observasi (Lab 6) |

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Menjelaskan** (C2) cara kerja regresi linear dan makna koefisiennya.
2. **Menerapkan** (C3) regularisasi Ridge dan Lasso serta menjelaskan perbedaan pengaruhnya.
3. **Menghitung** (C3) MAE, RMSE, R², dan MAPE secara manual.
4. **Memilih** (C5) metrik regresi berdasarkan sifat masalah dan dampak kesalahan.
5. **Menganalisis** (C4) kondisi model melalui tukar-tambah bias–varians.

---

## Materi Pembelajaran

### 6.1 Regresi Linear

#### 6.1.1 Bentuk Model

$$\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_p x_p$$

Pelatihan berarti mencari koefisien $\beta$ yang meminimalkan **jumlah kuadrat residual**:

$$\text{SSR} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

#### 6.1.2 Menafsirkan Koefisien

Untuk model harga rumah:

$$\widehat{\text{harga}} = 120 + 8{,}5 \cdot \text{luas} + 45 \cdot \text{kamar} - 12 \cdot \text{jarak\_pusat}$$

| Koefisien | Tafsir yang benar |
|-----------|-------------------|
| $\beta_{\text{luas}} = 8{,}5$ | Setiap penambahan 1 m², dengan fitur lain tetap, **dikaitkan dengan** kenaikan harga 8,5 juta |
| $\beta_{\text{jarak}} = -12$ | Setiap penambahan 1 km jarak dari pusat, dikaitkan dengan penurunan 12 juta |
| $\beta_0 = 120$ | Nilai ketika seluruh fitur nol — **sering tanpa makna nyata** |

> **Kata "dikaitkan dengan", bukan "menyebabkan".** Ini bukan kehati-hatian berlebihan: data observasional tidak mendukung klaim sebab-akibat, sebagaimana dipelajari pada Probabilitas dan Statistik. Pada penilaian mata kuliah ini, penulisan interpretasi dengan bahasa sebab-akibat pada data observasional dikenai pengurangan nilai.

#### 6.1.3 Asumsi dan Batasnya

| Asumsi | Akibat bila dilanggar | Pemeriksaan |
|--------|-----------------------|-------------|
| Hubungan linear | Model kehilangan pola | Plot residual vs prediksi |
| Residual bebas | Galat baku menyesatkan | Urutan residual; Durbin-Watson |
| Varians residual seragam | Interval prediksi tidak sah | Plot residual — pola corong |
| Residual normal | Uji signifikansi tidak sah | Q-Q plot |
| Tidak ada multikolinearitas ekstrem | Koefisien tidak stabil | VIF; matriks korelasi |

---

### 6.2 Regresi Polinomial dan *Overfitting*

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
| ≥ 5 | Mengikuti setiap titik data | ***Overfit*** — bagus pada latih, buruk pada uji |

Tanda pengenal *overfitting* pada regresi polinomial: R² data latih mendekati 1,0 sementara R² data uji rendah atau bahkan **negatif**.

> R² negatif bukan galat perhitungan. Ia berarti model lebih buruk daripada sekadar menebak rata-rata — yaitu lebih buruk daripada *baseline*.

---

### 6.3 Regularisasi

#### 6.3.1 Gagasannya

Menambahkan denda atas besarnya koefisien ke dalam fungsi yang diminimalkan:

| Metode | Fungsi objektif | Pengaruh khas |
|--------|-----------------|---------------|
| **Ridge (L2)** | $\text{SSR} + \alpha \sum \beta_j^2$ | Mengecilkan koefisien; **tidak** membuatnya nol |
| **Lasso (L1)** | $\text{SSR} + \alpha \sum \|\beta_j\|$ | Dapat membuat koefisien **tepat nol** → pemilihan fitur |
| **Elastic Net** | Gabungan L1 dan L2 | Kompromi keduanya |

```python
from sklearn.linear_model import Ridge, Lasso, ElasticNet

# WAJIB: fitur diskalakan lebih dahulu — regularisasi peka satuan
model = Pipeline([
    ("skala", StandardScaler()),
    ("ridge", Ridge(alpha=1.0, random_state=42)),
])
```

#### 6.3.2 Pengaruh α

| α | Pengaruh | Risiko |
|---|----------|--------|
| 0 | Sama dengan regresi biasa | *Overfitting* |
| Kecil (0,01–1) | Pengecilan ringan | Biasanya tepat |
| Besar (10–100) | Pengecilan kuat | *Underfitting* |
| Sangat besar | Seluruh koefisien → 0 | Model menjadi konstanta |

α ditentukan melalui validasi silang, **bukan** ditebak:

```python
from sklearn.linear_model import RidgeCV
import numpy as np

model = RidgeCV(alphas=np.logspace(-3, 3, 50), cv=5)
model.fit(X_train, y_train)
print("Alpha terpilih:", model.alpha_)
```

> **Mengapa penskalaan wajib sebelum regularisasi:** denda dihitung atas besarnya koefisien. Fitur berskala besar memperoleh koefisien kecil, sehingga terdenda ringan — bukan karena kurang penting, melainkan semata-mata karena satuannya.

---

### 6.4 Metrik Regresi

#### 6.4.1 Empat Metrik Pokok

| Metrik | Rumus | Satuan | Sifat |
|--------|-------|--------|-------|
| **MAE** | $\frac{1}{n}\sum \|y_i - \hat{y}_i\|$ | Sama dengan target | Tahan pencilan; mudah ditafsirkan |
| **MSE** | $\frac{1}{n}\sum (y_i - \hat{y}_i)^2$ | Kuadrat target | Menghukum galat besar |
| **RMSE** | $\sqrt{\text{MSE}}$ | Sama dengan target | Menghukum galat besar; dapat ditafsirkan |
| **R²** | $1 - \frac{SS_{res}}{SS_{tot}}$ | Tanpa satuan | Proporsi keragaman terjelaskan |
| **MAPE** | $\frac{100\%}{n}\sum \left\|\frac{y_i - \hat{y}_i}{y_i}\right\|$ | Persen | Galat relatif; **gagal bila ada $y_i = 0$** |

#### 6.4.2 Perhitungan Manual

Data prediksi harga rumah (dalam juta rupiah):

| Sebenarnya | Prediksi | Galat | \|Galat\| | Galat² | \|Galat\|/y |
|------------|----------|-------|-----------|--------|-------------|
| 800 | 750 | −50 | 50 | 2.500 | 0,0625 |
| 1.200 | 1.150 | −50 | 50 | 2.500 | 0,0417 |
| 600 | 640 | +40 | 40 | 1.600 | 0,0667 |
| 2.000 | 1.400 | −600 | 600 | 360.000 | 0,3000 |
| 900 | 920 | +20 | 20 | 400 | 0,0222 |
| | **Jumlah** | | **760** | **367.000** | **0,4931** |

$$\text{MAE} = \frac{760}{5} = 152 \text{ juta}$$
$$\text{MSE} = \frac{367.000}{5} = 73.400 \qquad \text{RMSE} = \sqrt{73.400} \approx 271 \text{ juta}$$
$$\text{MAPE} = \frac{0{,}4931}{5} \times 100\% \approx 9{,}9\%$$

**Yang harus diperhatikan:** RMSE (271) jauh lebih besar daripada MAE (152). Selisih itu seluruhnya berasal dari satu pengamatan — rumah 2.000 juta yang meleset 600 juta.

| Metrik | Kesimpulannya |
|--------|---------------|
| MAE = 152 | "Rata-rata meleset 152 juta" |
| RMSE = 271 | "Ada kesalahan besar yang perlu diperhatikan" |
| MAPE = 9,9% | "Secara relatif cukup baik" |

Ketiganya benar. Yang dipilih bergantung pada **apakah kesalahan besar lebih merugikan secara tidak proporsional**.

#### 6.4.3 Memilih Metrik

| Situasi | Metrik | Alasan |
|---------|--------|--------|
| Semua kesalahan setara | **MAE** | Mudah ditafsirkan; tahan pencilan |
| Kesalahan besar jauh lebih buruk | **RMSE** | Menghukum galat besar secara kuadratik |
| Perlu perbandingan lintas skala | **R²** | Tanpa satuan |
| Kesalahan relatif yang penting | **MAPE** | Persentase |
| Target memuat nilai nol | **Hindari MAPE** | Pembagian nol |
| Target sangat menceng | **MAE atau RMSLE** | RMSE didominasi nilai besar |

> **Ketentuan mata kuliah ini:** laporkan sekurang-kurangnya MAE dan RMSE bersama-sama. Keduanya menceritakan hal yang berbeda, dan selisihnya sendiri adalah informasi.

---

### 6.5 Tukar-Tambah Bias dan Varians

#### 6.5.1 Uraian Galat

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
     └──────────────────┬──────────────────────► Kompleksitas model
                    optimum
      UNDERFIT                         OVERFIT
```

#### 6.5.2 Mengenali Kondisi Model

| Kondisi | Galat latih | Galat validasi | Ciri |
|---------|-------------|----------------|------|
| ***Underfit*** | Tinggi | Tinggi | Keduanya buruk dan berdekatan |
| **Pas** | Rendah | Rendah | Keduanya baik; selisih kecil |
| ***Overfit*** | **Sangat rendah** | Tinggi | Selisih besar |

| Kondisi | Yang harus dilakukan |
|---------|----------------------|
| *Underfit* | Tambah kompleksitas; tambah fitur; kurangi regularisasi |
| *Overfit* | Tambah data; kurangi fitur; **tambah regularisasi**; sederhanakan model |

Diagnosis melalui kurva pembelajaran dibahas pada Minggu 12.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 6 buku ajar](../06-buku-ajar/bab-06-regresi-dan-metriknya.md).
- Meninjau kembali materi regresi linear dari Probabilitas dan Statistik (Bab 13).

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | Tinjauan; pembahasan T-05 dan proposal |
| Konsep | 35' | Regresi linear; interpretasi koefisien; asumsi |
| Latihan | 20' | **Perhitungan manual MAE, RMSE, R², MAPE** pada data §6.4.2 |
| Konsep | 30' | Regularisasi; pengaruh α; mengapa penskalaan wajib |
| Demonstrasi | 35' | Membandingkan Linear, Ridge, dan Lasso pada data properti; menunjukkan koefisien yang dinolkan Lasso |
| Penutup | 20' | Bias–varians; mengenali kondisi model; penugasan |

**Latihan manual wajib dikerjakan tanpa komputer**, karena inilah bentuk soal yang muncul pada UTS dan UAS.

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 6](../04-labs/lab-06-model-regresi-dan-metrik.md).
- Mengerjakan Milestone 1 proyek (jatuh tempo Minggu 7).

---

## Penugasan

**T-06 — Model Regresi dan Metriknya**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook Colab |
| Isi | (a) *Baseline* `DummyRegressor`; (b) Regresi linear, Ridge, dan Lasso dalam `Pipeline`; (c) α ditentukan dengan validasi silang; (d) MAE, RMSE, R², MAPE untuk seluruh model; (e) **Penjelasan mengapa metrik-metrik itu memberi kesimpulan berbeda**; (f) Koefisien yang dinolkan Lasso dan tafsirnya |
| Tenggat | Awal pertemuan Minggu 7 |
| Bobot | 1,9% (Observasi) |

---

## Rangkuman

1. Regresi linear mencari koefisien yang meminimalkan **jumlah kuadrat residual**.
2. Koefisien ditafsirkan dengan **"dikaitkan dengan"**, bukan "menyebabkan".
3. Polinomial derajat tinggi ***overfit***; R² uji negatif berarti lebih buruk daripada *baseline*.
4. **Ridge mengecilkan; Lasso dapat menolkan** → Lasso sekaligus memilih fitur.
5. **Penskalaan wajib sebelum regularisasi**, karena denda dihitung atas besarnya koefisien.
6. α ditentukan lewat **validasi silang**, bukan ditebak.
7. **MAE tahan pencilan; RMSE menghukum galat besar.** Selisih keduanya sendiri adalah informasi.
8. **MAPE gagal bila target memuat nol.**
9. Galat = **bias² + varians + galat tak tereduksi**.
10. *Underfit*: keduanya buruk. *Overfit*: latih sangat baik, validasi buruk.

---

## Referensi

1. James, G., et al. (2023). *An Introduction to Statistical Learning with Python*, Bab 3 dan 6. Springer.
2. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 4. O'Reilly.
3. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*, Bab 3. Springer.
4. Dokumentasi scikit-learn — *Linear Models*. <https://scikit-learn.org/stable/modules/linear_model.html>
5. Dokumentasi scikit-learn — *Metrics for regression*. <https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
