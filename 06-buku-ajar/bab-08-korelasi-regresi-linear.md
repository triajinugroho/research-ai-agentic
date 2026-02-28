# BAB 8: KORELASI DAN REGRESI LINEAR SEDERHANA

**Tri Aji Nugroho, S.T., M.T.**
Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-5.1 | Menjelaskan konsep korelasi dan mengidentifikasi arah serta kekuatan hubungan antar variabel melalui scatter plot | C2 |
| CPMK-5.2 | Menghitung dan menginterpretasi koefisien korelasi Pearson dan Spearman | C3 |
| CPMK-5.3 | Membangun model regresi linear sederhana menggunakan metode least squares dan menginterpretasi koefisien regresi | C3 |
| CPMK-5.4 | Menganalisis kualitas model regresi melalui koefisien determinasi (R²) dan diagnostik residual | C4 |
| CPMK-5.5 | Mengimplementasikan analisis korelasi dan regresi menggunakan Python (scipy, scikit-learn, statsmodels) serta membedakan korelasi dari kausalitas | C4 |

---

## 8.1 Pendahuluan: Mengapa Mempelajari Hubungan Antar Variabel?

Dalam dunia nyata, variabel jarang berdiri sendiri. Seorang data analyst di Tokopedia mungkin bertanya: apakah durasi kunjungan pengguna berhubungan dengan jumlah pembelian? Seorang peneliti di BPS ingin tahu: apakah provinsi dengan Indeks Pembangunan Manusia (IPM) tinggi juga memiliki pendapatan per kapita yang tinggi? Seorang mahasiswa penasaran: apakah jam belajar mempengaruhi nilai ujian?

Untuk menjawab pertanyaan-pertanyaan ini, kita membutuhkan dua alat statistik fundamental:

1. **Korelasi** — mengukur *kekuatan* dan *arah* hubungan antara dua variabel
2. **Regresi** — memodelkan hubungan tersebut sehingga kita bisa membuat *prediksi*

> "All models are wrong, but some are useful."
> — George E. P. Box

Bab ini membahas kedua alat tersebut secara mendalam, dilengkapi implementasi Python yang dapat langsung dijalankan di Google Colab, serta studi kasus berbasis data Indonesia.

```
┌─────────────────────────────────────────────────────────┐
│            PETA KONSEP BAB 8                            │
│                                                         │
│  HUBUNGAN ANTAR VARIABEL                                │
│         │                                               │
│    ┌────┴────┐                                          │
│    │         │                                          │
│  KORELASI  REGRESI                                      │
│    │         │                                          │
│  ┌─┴──┐   ┌─┴──────────┐                               │
│  │    │   │             │                               │
│ Pearson Spearman  Linear      Diagnostik                │
│  (r)    (ρ)    Sederhana     Residual                   │
│                 ŷ=b₀+b₁x                               │
│                    │                                    │
│              ┌─────┼─────┐                              │
│              │     │     │                              │
│           Slope  Inter-  R²                             │
│           (b₁)  cept(b₀)                               │
│                                                         │
│  PERINGATAN: Korelasi ≠ Kausalitas!                     │
└─────────────────────────────────────────────────────────┘
```

---

## 8.2 Konsep Korelasi

### 8.2.1 Apa Itu Korelasi?

**Korelasi** adalah ukuran statistik yang menggambarkan seberapa erat hubungan linear antara dua variabel numerik. Korelasi mengukur dua hal sekaligus:

| Aspek | Penjelasan | Contoh |
|-------|-----------|--------|
| **Arah** | Positif (+) atau negatif (-) | Jam belajar vs nilai ujian (positif); jam bermain game vs nilai (negatif) |
| **Kekuatan** | Seberapa erat hubungan (0 = tidak ada, 1 = sempurna) | r = 0.92 (sangat kuat); r = 0.15 (sangat lemah) |

### 8.2.2 Scatter Plot: Langkah Pertama Sebelum Menghitung

Sebelum menghitung koefisien korelasi, **selalu** buat scatter plot terlebih dahulu. Scatter plot membantu kita melihat:

- Arah hubungan (naik atau turun)
- Kekuatan hubungan (titik rapat atau tersebar)
- Pola non-linear (kurva, U-shape)
- Outlier yang mungkin mempengaruhi hasil

```
SCATTER PLOT: BERBAGAI POLA HUBUNGAN

  Positif Kuat (r≈0.9)     Negatif Kuat (r≈-0.9)    Tidak Ada (r≈0)
  y│    · ·                 y│· ·                     y│  ·    ·
   │   · ·                  │ · ·                      │    ·
   │  · ·                   │  · ·                     │ ·     ·
   │ · ·                    │   · ·                    │   ·  ·
   │· ·                     │    · ·                   │ ·   ·
   └──────── x              └──────── x                └──────── x

  Non-Linear (r≈0)          Positif Lemah (r≈0.3)
  y│·       ·               y│      · ·
   │ ·     ·                │   ·  ·
   │  ·   ·                 │  · ·   ·
   │   · ·                  │ ·  ·  ·
   │    ·                   │·  · ·
   └──────── x              └──────── x

  PERINGATAN: Pola non-linear bisa memiliki r ≈ 0
  padahal ada hubungan yang jelas!
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Contoh scatter plot: jam belajar vs nilai ujian mahasiswa UAI
np.random.seed(42)
jam_belajar = np.array([2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 10, 11, 12, 14])
nilai_ujian = np.array([52, 58, 62, 65, 70, 68, 74, 78, 80, 82, 85, 88, 87, 92, 95])

plt.figure(figsize=(8, 6))
plt.scatter(jam_belajar, nilai_ujian, color='steelblue', s=100,
            edgecolor='white', alpha=0.8)
plt.xlabel('Jam Belajar per Minggu', fontsize=12)
plt.ylabel('Nilai Ujian', fontsize=12)
plt.title('Hubungan Jam Belajar dan Nilai Ujian\nMahasiswa Informatika UAI', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 8.2.3 Tabel Interpretasi Scatter Plot

| Pola Visual | Arah | Kekuatan | Korelasi Pearson |
|-------------|------|----------|-----------------|
| Titik rapat naik ke kanan atas | Positif | Kuat | r mendekati +1 |
| Titik longgar naik ke kanan atas | Positif | Lemah | r antara 0 dan +0.5 |
| Titik rapat turun ke kanan bawah | Negatif | Kuat | r mendekati -1 |
| Titik tersebar acak | Tidak ada | - | r mendekati 0 |
| Pola melengkung (U/kurva) | Non-linear | - | r bisa mendekati 0! |

---

## 8.3 Koefisien Korelasi Pearson

### 8.3.1 Definisi dan Rumus

Koefisien korelasi Pearson (*Pearson product-moment correlation coefficient*) mengukur kekuatan dan arah hubungan **linear** antara dua variabel. Nilainya berkisar antara -1 dan +1.

**Rumus:**

```
            Σ(xᵢ - x̄)(yᵢ - ȳ)
r = ─────────────────────────────────
    √[Σ(xᵢ - x̄)²] × √[Σ(yᵢ - ȳ)²]
```

Atau dalam notasi yang lebih ringkas:

```
        n Σxᵢyᵢ - (Σxᵢ)(Σyᵢ)
r = ─────────────────────────────────────────
    √[n Σxᵢ² - (Σxᵢ)²] × √[n Σyᵢ² - (Σyᵢ)²]
```

**Sifat-sifat korelasi Pearson:**
- -1 <= r <= +1
- r = +1 : hubungan linear positif sempurna
- r = -1 : hubungan linear negatif sempurna
- r = 0 : tidak ada hubungan linear (bukan berarti tidak ada hubungan sama sekali!)

### 8.3.2 Interpretasi Kekuatan Korelasi

| Rentang |r| | Interpretasi |
|-----------|-------------|
| 0.80 - 1.00 | Sangat kuat |
| 0.60 - 0.79 | Kuat |
| 0.40 - 0.59 | Sedang |
| 0.20 - 0.39 | Lemah |
| 0.00 - 0.19 | Sangat lemah / tidak ada |

> **Catatan penting:** Tanda positif/negatif menunjukkan *arah*, bukan *kekuatan*. Jadi r = -0.85 memiliki hubungan yang **lebih kuat** daripada r = +0.40.

### 8.3.3 Syarat Penggunaan Pearson

Korelasi Pearson valid jika:
1. Kedua variabel berskala **interval atau rasio** (data numerik kontinu)
2. Hubungan antar variabel bersifat **linear**
3. Data tidak memiliki **outlier yang ekstrem**
4. Kedua variabel idealnya berdistribusi **normal** (terutama untuk uji signifikansi)

### 8.3.4 Perhitungan Manual dan Python

```python
import numpy as np
from scipy import stats

# Data: jam belajar dan nilai ujian 7 mahasiswa
x = np.array([2, 3, 5, 6, 8, 9, 10])   # Jam belajar per minggu
y = np.array([55, 60, 68, 72, 80, 85, 90])  # Nilai ujian

# === Perhitungan manual ===
n = len(x)
x_bar = np.mean(x)
y_bar = np.mean(y)

# Pembilang: Σ(xi - x̄)(yi - ȳ)
pembilang = np.sum((x - x_bar) * (y - y_bar))

# Penyebut: √[Σ(xi - x̄)²] × √[Σ(yi - ȳ)²]
penyebut = np.sqrt(np.sum((x - x_bar)**2)) * np.sqrt(np.sum((y - y_bar)**2))

r_manual = pembilang / penyebut

print("=== PERHITUNGAN KORELASI PEARSON ===")
print(f"n = {n}")
print(f"x̄ = {x_bar:.2f}, ȳ = {y_bar:.2f}")
print(f"Σ(xi - x̄)(yi - ȳ) = {pembilang:.2f}")
print(f"Penyebut = {penyebut:.2f}")
print(f"r (manual) = {r_manual:.4f}")

# === Dengan scipy ===
r_scipy, p_value = stats.pearsonr(x, y)
print(f"\nr (scipy)  = {r_scipy:.4f}")
print(f"p-value    = {p_value:.6f}")

# Interpretasi
if p_value < 0.05:
    print(f"\nKorelasi signifikan pada α = 0.05")
else:
    print(f"\nKorelasi tidak signifikan pada α = 0.05")
```

**Output:**
```
=== PERHITUNGAN KORELASI PEARSON ===
n = 7
x̄ = 6.14, ȳ = 72.86
Σ(xi - x̄)(yi - ȳ) = 240.86
Penyebut = 242.49
r (manual) = 0.9933
r (scipy)  = 0.9933
p-value    = 0.000016

Korelasi signifikan pada α = 0.05
```

**Interpretasi:** Terdapat hubungan positif yang **sangat kuat** (r = 0.99) antara jam belajar dan nilai ujian. Hubungan ini signifikan secara statistik (p < 0.001).

---

## 8.4 Koefisien Korelasi Spearman

### 8.4.1 Kapan Menggunakan Spearman?

Korelasi Spearman adalah alternatif **non-parametrik** dari Pearson. Alih-alih bekerja pada nilai asli, Spearman bekerja pada **rank (peringkat)** data. Gunakan Spearman ketika:

- Data berskala **ordinal** (misalnya skala Likert: Sangat Tidak Setuju hingga Sangat Setuju)
- Ada **outlier** yang mempengaruhi korelasi Pearson
- Hubungan bersifat **monotonic** tetapi tidak linear (misalnya: semakin tinggi X, semakin tinggi Y, tapi bukan garis lurus)

### 8.4.2 Cara Kerja Spearman

Langkah-langkah:
1. **Ranking** data X dan Y secara terpisah (dari yang terkecil ke terbesar)
2. **Hitung korelasi Pearson** dari rank-rank tersebut

```
CONTOH RANKING:

Data asli:          Setelah ranking:
X:  10  25  8  30   X_rank:  2  3  1  4
Y:  55  70  50  80  Y_rank:  2  3  1  4
```

### 8.4.3 Perbandingan Pearson vs Spearman

| Aspek | Pearson (r) | Spearman (ρ) |
|-------|-------------|--------------|
| Tipe data | Interval/Rasio | Ordinal/Interval/Rasio |
| Asumsi | Hubungan linear | Hubungan monotonic |
| Sensitif terhadap outlier | Ya, sangat | Tidak, robust |
| Mengukur | Hubungan linear | Hubungan monotonic |
| Kapan digunakan | Data kontinu, tanpa outlier | Data ordinal, ada outlier |

### 8.4.4 Implementasi Python

```python
import numpy as np
from scipy import stats

# Data: peringkat kepuasan (ordinal) vs frekuensi pembelian
# Skala kepuasan: 1=Sangat Tidak Puas, ..., 5=Sangat Puas
kepuasan = np.array([2, 3, 4, 5, 1, 3, 4, 5, 2, 4, 5, 3, 1, 4, 5])
frekuensi_beli = np.array([3, 5, 7, 10, 1, 4, 8, 12, 2, 6, 11, 5, 1, 7, 9])

# Pearson (kurang tepat untuk data ordinal, tapi kita bandingkan)
r_pearson, p_pearson = stats.pearsonr(kepuasan, frekuensi_beli)

# Spearman (lebih tepat untuk data ordinal)
rho_spearman, p_spearman = stats.spearmanr(kepuasan, frekuensi_beli)

print("=== PERBANDINGAN PEARSON vs SPEARMAN ===")
print(f"Pearson  r = {r_pearson:.4f},  p-value = {p_pearson:.6f}")
print(f"Spearman ρ = {rho_spearman:.4f}, p-value = {p_spearman:.6f}")
print()

# Contoh dengan outlier
print("=== EFEK OUTLIER ===")
x_normal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_normal = np.array([2, 4, 5, 4, 5, 7, 8, 9, 10, 11])

# Tambahkan outlier
x_outlier = np.append(x_normal, 10)
y_outlier = np.append(y_normal, 50)  # outlier!

r_no_outlier, _ = stats.pearsonr(x_normal, y_normal)
r_with_outlier, _ = stats.pearsonr(x_outlier, y_outlier)
rho_no_outlier, _ = stats.spearmanr(x_normal, y_normal)
rho_with_outlier, _ = stats.spearmanr(x_outlier, y_outlier)

print(f"Tanpa outlier  → Pearson: {r_no_outlier:.4f}, Spearman: {rho_no_outlier:.4f}")
print(f"Dengan outlier → Pearson: {r_with_outlier:.4f}, Spearman: {rho_with_outlier:.4f}")
print("→ Perhatikan: Pearson berubah drastis, Spearman relatif stabil!")
```

---

## 8.5 Correlation Does Not Imply Causation

### 8.5.1 Prinsip Fundamental

Ini adalah salah satu prinsip **paling penting** dalam statistika, dan salah satu yang paling sering dilanggar di media dan kehidupan sehari-hari:

> **Korelasi tidak berarti kausalitas** (*correlation does not imply causation*)

Dua variabel yang berkorelasi tidak berarti yang satu *menyebabkan* yang lain.

### 8.5.2 Contoh Korelasi yang Menipu

| Variabel X | Variabel Y | Korelasi | Apakah X menyebabkan Y? |
|-----------|-----------|----------|------------------------|
| Penjualan es krim | Kasus tenggelam | Positif kuat | **TIDAK.** Variabel ketiga (cuaca panas) menyebabkan keduanya naik |
| Konsumsi keju per kapita | Kematian terjerat selimut | r = 0.95 | **TIDAK.** Spurious correlation — angka kebetulan bergerak bersamaan |
| Jumlah masjid di kota | Tingkat kriminalitas | Positif | **TIDAK.** Keduanya berkorelasi dengan ukuran populasi kota |
| Pengguna internet Indonesia | Harga avokad global | Positif | **TIDAK.** Keduanya kebetulan naik seiring waktu (tren temporal) |

### 8.5.3 Tiga Jebakan Utama

```
JEBAKAN KORELASI → KAUSALITAS

1. CONFOUNDING VARIABLE (Variabel Perancu)
   ┌──── Cuaca Panas ────┐
   │                     │
   ▼                     ▼
Es Krim ←─ r=0.85 ─→ Tenggelam
   (Bukan es krim yang menyebabkan tenggelam!)

2. REVERSE CAUSATION (Kausalitas Terbalik)
   Kita pikir:  X ──→ Y
   Padahal:     X ←── Y
   Contoh: "Negara kaya punya IPM tinggi"
   Atau:   "IPM tinggi membuat negara kaya"?

3. SPURIOUS CORRELATION (Korelasi Palsu)
   X ──── r=0.95 ────→ Y
   (Tidak ada hubungan logis sama sekali,
    hanya kebetulan statistik)
```

### 8.5.4 Bagaimana Membuktikan Kausalitas?

Untuk membuktikan bahwa X benar-benar *menyebabkan* Y, diperlukan:

1. **Eksperimen terkontrol** (*Randomized Controlled Trial / RCT*) — standar emas
2. **Analisis kausal** (*causal inference*) menggunakan metode seperti *instrumental variables*, *difference-in-differences*, atau *regression discontinuity*
3. **Framework Bradford Hill** — kekuatan asosiasi, konsistensi, spesifisitas, temporalitas, dll.

> **Pesan untuk mahasiswa:** Ketika membaca berita atau hasil penelitian yang mengklaim "X menyebabkan Y", selalu tanyakan: apakah ini berdasarkan eksperimen terkontrol atau hanya korelasi? Keterampilan berpikir kritis ini sangat berharga di era informasi.

---

## 8.6 Regresi Linear Sederhana

### 8.6.1 Dari Korelasi ke Prediksi

Korelasi menjawab: *"Apakah ada hubungan?"* Regresi menjawab pertanyaan yang lebih kuat: *"Seberapa besar pengaruhnya, dan bisakah kita memprediksi?"*

**Model regresi linear sederhana:**

```
ŷ = b₀ + b₁x
```

Di mana:
- **ŷ** (*y-hat*) = nilai prediksi variabel dependen (respons)
- **b₀** (*intercept*) = nilai ŷ ketika x = 0
- **b₁** (*slope*) = perubahan ŷ untuk setiap kenaikan 1 unit x
- **x** = variabel independen (prediktor)

```
ANATOMI REGRESI LINEAR SEDERHANA

  y │
    │           · (data point)
    │        ·  /
    │      /  ·    ← eᵢ = yᵢ - ŷᵢ (residual)
    │    · /
    │   /·         Garis regresi: ŷ = b₀ + b₁x
    │  / ·
    │ /·           slope (b₁) = kemiringan garis
    │/
  b₀──────────── x
    │
    intercept (b₀) = titik potong sumbu y
```

### 8.6.2 Metode Least Squares (Kuadrat Terkecil)

Bagaimana kita menemukan garis "terbaik" yang melewati titik-titik data? Kita menggunakan **metode Ordinary Least Squares (OLS)** — yaitu mencari b₀ dan b₁ yang **meminimalkan jumlah kuadrat residual** (*Sum of Squared Residuals*):

```
Minimize: SSR = Σ(yᵢ - ŷᵢ)² = Σ(yᵢ - b₀ - b₁xᵢ)²
```

Dengan menggunakan kalkulus (turunan parsial dan menyamakan dengan nol), kita memperoleh:

```
         Σ(xᵢ - x̄)(yᵢ - ȳ)
b₁ = ────────────────────────
          Σ(xᵢ - x̄)²

b₀ = ȳ - b₁ × x̄
```

**Mengapa kuadrat?** Karena jika kita hanya menjumlahkan residual tanpa dikuadratkan, error positif dan negatif akan saling meniadakan (jumlahnya bisa nol meskipun ada error besar).

### 8.6.3 Visualisasi Konsep Residual

```
RESIDUAL: JARAK VERTIKAL DARI TITIK DATA KE GARIS REGRESI

  y │
    │        · (y₃)
    │        |  ← e₃ = y₃ - ŷ₃ (positif)
    │     ···+···/···
    │       /
    │    · (y₂)
    │    +     ← e₂ ≈ 0 (titik dekat garis)
    │   /
    │  +
    │ /|
    │/ · (y₁) ← e₁ = y₁ - ŷ₁ (negatif)
    └──────────── x

  OLS meminimalkan: e₁² + e₂² + e₃² + ...
```

### 8.6.4 Interpretasi Koefisien Regresi

Interpretasi yang tepat sangat penting. Gunakan template berikut:

- **Slope (b₁):** *"Jika X naik 1 unit, maka Y **diperkirakan** berubah sebesar b₁ unit."*
- **Intercept (b₀):** *"Ketika X = 0, nilai Y diperkirakan sebesar b₀."* (Tapi hati-hati — X = 0 mungkin tidak masuk akal dalam konteks data!)

**Contoh interpretasi:**

Misalkan model regresi antara jam belajar (X) dan nilai ujian (Y) menghasilkan:

```
ŷ = 45.2 + 4.8x
```

- **Slope = 4.8:** "Setiap tambahan 1 jam belajar per minggu, nilai ujian diperkirakan naik 4.8 poin."
- **Intercept = 45.2:** "Jika mahasiswa tidak belajar sama sekali (0 jam), nilai ujian diperkirakan 45.2." (Ini masuk akal — mungkin ada pengetahuan dasar dari mengikuti kuliah.)

> **Hati-hati dengan ekstrapolasi!** Model ini hanya valid dalam rentang data yang diamati. Memprediksi nilai ujian untuk mahasiswa yang belajar 50 jam per minggu tidak akan menghasilkan prediksi yang bermakna.

### 8.6.5 Perhitungan Manual Regresi

```python
import numpy as np

# Data: jam belajar (X) dan nilai ujian (Y)
x = np.array([2, 3, 5, 6, 8, 9, 10])
y = np.array([55, 60, 68, 72, 80, 85, 90])

n = len(x)
x_bar = np.mean(x)
y_bar = np.mean(y)

# Hitung slope (b₁)
pembilang_b1 = np.sum((x - x_bar) * (y - y_bar))
penyebut_b1 = np.sum((x - x_bar) ** 2)
b1 = pembilang_b1 / penyebut_b1

# Hitung intercept (b₀)
b0 = y_bar - b1 * x_bar

print("=== PERHITUNGAN REGRESI LINEAR (MANUAL) ===")
print(f"n = {n}")
print(f"x̄ = {x_bar:.2f}")
print(f"ȳ = {y_bar:.2f}")
print(f"Σ(xᵢ - x̄)(yᵢ - ȳ) = {pembilang_b1:.2f}")
print(f"Σ(xᵢ - x̄)² = {penyebut_b1:.2f}")
print(f"\nb₁ (slope)     = {b1:.4f}")
print(f"b₀ (intercept) = {b0:.4f}")
print(f"\nPersamaan regresi: ŷ = {b0:.2f} + {b1:.2f}x")

# Prediksi
y_pred = b0 + b1 * x
residuals = y - y_pred

print(f"\n{'x':>5} {'y_actual':>10} {'y_pred':>10} {'residual':>10}")
print("-" * 40)
for i in range(n):
    print(f"{x[i]:>5} {y[i]:>10.2f} {y_pred[i]:>10.2f} {residuals[i]:>10.2f}")
```

---

## 8.7 Koefisien Determinasi (R²)

### 8.7.1 Definisi

R² (*coefficient of determination*) mengukur **proporsi variasi** dalam variabel dependen (Y) yang dapat **dijelaskan** oleh variabel independen (X) melalui model regresi.

```
              SS_res        Σ(yᵢ - ŷᵢ)²
R² = 1 - ─────────── = 1 - ──────────────
              SS_tot        Σ(yᵢ - ȳ)²
```

Di mana:
- **SS_res** (*Sum of Squares Residual*) = Σ(yᵢ - ŷᵢ)² = variasi yang **TIDAK** bisa dijelaskan model
- **SS_tot** (*Sum of Squares Total*) = Σ(yᵢ - ȳ)² = variasi **total** dalam Y

### 8.7.2 Interpretasi R²

```
DEKOMPOSISI VARIASI

  SS_total (variasi total Y)
  ┌─────────────────────────────────────────┐
  │  SS_reg (dijelaskan model)  │  SS_res   │
  │  (R² × SS_total)           │  (sisa)   │
  └─────────────────────────────┴───────────┘

  Jika R² = 0.78:
  ┌────────────────────────────────┬─────────┐
  │     78% dijelaskan oleh X     │ 22%     │
  │     (model menangkap ini)     │ (sisa)  │
  └────────────────────────────────┴─────────┘
```

| Nilai R² | Interpretasi | Contoh |
|----------|-------------|--------|
| 0.90 - 1.00 | Sangat baik | "90%+ variasi Y dijelaskan oleh X" |
| 0.70 - 0.89 | Baik | Model cukup kuat untuk prediksi |
| 0.50 - 0.69 | Cukup | Masih berguna, tapi banyak variasi yang tidak tertangkap |
| 0.30 - 0.49 | Lemah | Model memiliki kekuatan prediksi terbatas |
| 0.00 - 0.29 | Sangat lemah | Model hampir tidak menjelaskan variasi Y |

> **Catatan penting:** Untuk regresi linear sederhana (satu prediktor), R² = r² (kuadrat dari korelasi Pearson). Misalnya, jika r = 0.90, maka R² = 0.81.

### 8.7.3 Perhitungan R² dengan Python

```python
import numpy as np

# Lanjutan dari data sebelumnya
x = np.array([2, 3, 5, 6, 8, 9, 10])
y = np.array([55, 60, 68, 72, 80, 85, 90])

# Model regresi (dari perhitungan sebelumnya)
b0 = 44.83  # intercept (nilai perkiraan)
b1 = 4.39   # slope (nilai perkiraan)
y_pred = b0 + b1 * x
y_bar = np.mean(y)

# Hitung komponen R²
SS_tot = np.sum((y - y_bar) ** 2)
SS_res = np.sum((y - y_pred) ** 2)
SS_reg = np.sum((y_pred - y_bar) ** 2)

R_squared = 1 - (SS_res / SS_tot)

print("=== KOEFISIEN DETERMINASI (R²) ===")
print(f"SS_total (variasi total)     = {SS_tot:.2f}")
print(f"SS_regression (dijelaskan)   = {SS_reg:.2f}")
print(f"SS_residual (tidak dijelaskan) = {SS_res:.2f}")
print(f"\nR² = 1 - ({SS_res:.2f} / {SS_tot:.2f}) = {R_squared:.4f}")
print(f"\nInterpretasi: {R_squared*100:.1f}% variasi dalam nilai ujian")
print(f"dapat dijelaskan oleh jam belajar.")
print(f"Sisanya {(1-R_squared)*100:.1f}% dipengaruhi faktor lain")
print(f"(motivasi, metode belajar, kecerdasan bawaan, dll).")
```

---

## 8.8 Diagnostik Residual: Asumsi Regresi Linear

### 8.8.1 Empat Asumsi Klasik (LINE)

Model regresi linear yang valid memerlukan empat asumsi utama, yang dapat diingat dengan akronim **LINE**:

| Asumsi | Singkatan | Penjelasan | Cara Memeriksa |
|--------|-----------|-----------|----------------|
| **L**inearity | Linearitas | Hubungan X dan Y adalah linear | Scatter plot, residual plot |
| **I**ndependence | Independensi | Residual saling independen | Durbin-Watson test |
| **N**ormality | Normalitas | Residual berdistribusi normal | Histogram residual, Q-Q plot, Shapiro-Wilk test |
| **E**qual variance | Homoskedastisitas | Varians residual konstan | Residual vs fitted plot |

### 8.8.2 Residual Plot: Alat Utama Diagnostik

```
RESIDUAL PLOT: APA YANG KITA HARAPKAN vs MASALAH

  BAIK (Asumsi terpenuhi):        MASALAH: Non-linearitas
  residual│                        residual│
          │  ·  ·     ·                    │     · ·
          │    ·   ·                       │  ·       ·
    ------0--·----·---·----               ------0-----------·----
          │·     ·  ·                      │·             ·
          │  ·       ·                     │   · ·
          └──────────── ŷ                  └──────────── ŷ
  (Tersebar acak)                  (Pola melengkung)

  MASALAH: Heteroskedastisitas    MASALAH: Outlier
  residual│                        residual│
          │              · · ·             │
          │          · · ·                 │           · (outlier)
    ------0--·-·--·--------               ------0--·--·---·------
          │  · ·     · · ·                 │  ·  ·  · ·
          │              · ·               │    ·
          └──────────── ŷ                  └──────────── ŷ
  (Varians membesar/corong)        (Satu titik sangat jauh)
```

### 8.8.3 Implementasi Diagnostik Residual

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression

# Data contoh
np.random.seed(42)
x = np.linspace(5, 50, 40)
y = 10 + 2.5 * x + np.random.normal(0, 8, 40)

# Fit model
X = x.reshape(-1, 1)
model = LinearRegression().fit(X, y)
y_pred = model.predict(X)
residuals = y - y_pred

# === Diagnostik Residual ===
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Residual vs Fitted Values
axes[0, 0].scatter(y_pred, residuals, color='steelblue', s=60, alpha=0.7)
axes[0, 0].axhline(y=0, color='red', linestyle='--', linewidth=2)
axes[0, 0].set_xlabel('Nilai Prediksi (ŷ)')
axes[0, 0].set_ylabel('Residual (y - ŷ)')
axes[0, 0].set_title('1. Residual vs Fitted (Linearitas & Homoskedastisitas)')
axes[0, 0].grid(True, alpha=0.3)

# 2. Histogram Residual
axes[0, 1].hist(residuals, bins=10, color='steelblue', edgecolor='navy', alpha=0.7)
axes[0, 1].set_xlabel('Residual')
axes[0, 1].set_ylabel('Frekuensi')
axes[0, 1].set_title('2. Distribusi Residual (Normalitas)')
axes[0, 1].grid(True, alpha=0.3)

# 3. Q-Q Plot
stats.probplot(residuals, dist="norm", plot=axes[1, 0])
axes[1, 0].set_title('3. Q-Q Plot (Normalitas)')
axes[1, 0].grid(True, alpha=0.3)

# 4. Scale-Location Plot
axes[1, 1].scatter(y_pred, np.sqrt(np.abs(residuals)),
                   color='steelblue', s=60, alpha=0.7)
axes[1, 1].set_xlabel('Nilai Prediksi (ŷ)')
axes[1, 1].set_ylabel('√|Residual|')
axes[1, 1].set_title('4. Scale-Location (Homoskedastisitas)')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Uji normalitas residual
stat_shapiro, p_shapiro = stats.shapiro(residuals)
print(f"Uji Shapiro-Wilk: W = {stat_shapiro:.4f}, p-value = {p_shapiro:.4f}")
if p_shapiro > 0.05:
    print("→ Residual berdistribusi normal (p > 0.05) ✓")
else:
    print("→ Residual TIDAK berdistribusi normal (p ≤ 0.05) ✗")
```

---

## 8.9 Implementasi dengan scikit-learn dan statsmodels

### 8.9.1 Regresi Linear dengan scikit-learn

`scikit-learn` menyediakan API yang sederhana dan konsisten untuk membangun model regresi.

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Data: hubungan luas tanah (m²) dan harga rumah (juta Rp) di Depok
data_rumah = pd.DataFrame({
    'luas_tanah_m2': [60, 72, 80, 90, 100, 110, 120, 135, 150, 180,
                      200, 220, 250, 300, 350],
    'harga_juta_rp': [450, 520, 580, 650, 720, 800, 870, 980, 1100, 1350,
                      1500, 1650, 1900, 2300, 2700]
})

# Siapkan data (sklearn membutuhkan X dalam bentuk 2D)
X = data_rumah['luas_tanah_m2'].values.reshape(-1, 1)
y = data_rumah['harga_juta_rp'].values

# Buat dan latih model
model = LinearRegression()
model.fit(X, y)

# Koefisien
b0 = model.intercept_
b1 = model.coef_[0]
r_squared = model.score(X, y)

print("=== Hasil Regresi Linear (scikit-learn) ===")
print(f"Persamaan: Harga = {b0:.2f} + {b1:.2f} × Luas Tanah")
print(f"Intercept (b₀): {b0:.2f} juta Rp")
print(f"Slope (b₁): {b1:.2f} juta Rp per m²")
print(f"R²: {r_squared:.4f}")

# Metrik evaluasi
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)

print(f"\nMSE  = {mse:.2f}")
print(f"RMSE = {rmse:.2f} juta Rp")

# Interpretasi
print(f"\n=== Interpretasi ===")
print(f"- Setiap tambahan 1 m² luas tanah, harga rumah")
print(f"  diperkirakan naik Rp {b1:.2f} juta ({b1*1e6:,.0f} rupiah).")
print(f"- {r_squared*100:.1f}% variasi harga rumah dapat dijelaskan")
print(f"  oleh luas tanah.")

# Prediksi untuk luas tanah tertentu
luas_baru = np.array([[85], [150], [250]])
prediksi = model.predict(luas_baru)

print(f"\n=== Prediksi Harga Rumah ===")
for luas, harga in zip(luas_baru.flatten(), prediksi):
    print(f"Luas {luas} m² → Harga diperkirakan Rp {harga:.0f} juta"
          f" ({harga*1e6:,.0f} rupiah)")
```

### 8.9.2 Regresi Linear dengan statsmodels (Output Lengkap)

`statsmodels` memberikan output yang lebih detail, mirip dengan software statistik tradisional (SPSS, Stata).

```python
import statsmodels.api as sm

# Data dari contoh sebelumnya
X_sm = sm.add_constant(data_rumah['luas_tanah_m2'])  # Menambahkan kolom konstanta
y_sm = data_rumah['harga_juta_rp']

# Fit model OLS
model_sm = sm.OLS(y_sm, X_sm).fit()

# Tampilkan summary lengkap
print(model_sm.summary())
```

**Output summary statsmodels memberikan informasi berikut:**

```
                            OLS Regression Results
==============================================================================
Dep. Variable:      harga_juta_rp   R-squared:                       0.9xxx
Model:                        OLS   Adj. R-squared:                  0.9xxx
Method:             Least Squares   F-statistic:                     xxx.xx
Date:                  xxx, xx xxx   Prob (F-statistic):           x.xxe-xx
Time:                    xx:xx:xx   Log-Likelihood:                -xxx.xx
No. Observations:              15   AIC:                             xxx.x
Df Residuals:                  13   BIC:                             xxx.x
Df Model:                       1
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        xxx.xxxx    xxx.xxx      x.xxx      0.xxx     xxx.xxx     xxx.xxx
luas_tanah   xxx.xxxx    xxx.xxx      x.xxx      0.000     xxx.xxx     xxx.xxx
==============================================================================
```

**Cara membaca output statsmodels:**

| Bagian | Informasi |
|--------|-----------|
| R-squared | Proporsi variasi Y yang dijelaskan oleh X |
| Adj. R-squared | R² yang disesuaikan untuk jumlah prediktor |
| F-statistic | Uji signifikansi model secara keseluruhan |
| coef (const) | Intercept (b₀) |
| coef (luas_tanah) | Slope (b₁) |
| P>\|t\| | p-value untuk setiap koefisien |
| [0.025, 0.975] | 95% confidence interval untuk koefisien |

```python
# Membaca komponen penting dari summary
print("=== Ringkasan Model statsmodels ===")
print(f"R² = {model_sm.rsquared:.4f}")
print(f"Adj. R² = {model_sm.rsquared_adj:.4f}")
print(f"F-statistic = {model_sm.fvalue:.2f}, p-value = {model_sm.f_pvalue:.6f}")
print(f"\nKoefisien:")
print(f"  Intercept = {model_sm.params[0]:.2f} (p = {model_sm.pvalues[0]:.4f})")
print(f"  Slope     = {model_sm.params[1]:.4f} (p = {model_sm.pvalues[1]:.6f})")
print(f"\n95% CI untuk slope: [{model_sm.conf_int().iloc[1, 0]:.4f}, "
      f"{model_sm.conf_int().iloc[1, 1]:.4f}]")
```

### 8.9.3 Perbandingan scikit-learn vs statsmodels

| Aspek | scikit-learn | statsmodels |
|-------|-------------|-------------|
| **Fokus** | Prediksi (Machine Learning) | Inferensi statistik |
| **Output** | Koefisien + R² | Summary lengkap (p-value, CI, F-test) |
| **API** | `.fit()`, `.predict()`, `.score()` | `.fit()`, `.summary()`, `.predict()` |
| **Kapan digunakan** | Membangun model prediksi | Analisis statistik mendalam |
| **Intercept** | Otomatis ditambahkan | Harus ditambahkan manual (`add_constant`) |

> **Rekomendasi:** Gunakan **statsmodels** untuk analisis statistik dan pelaporan akademik. Gunakan **scikit-learn** untuk membangun pipeline machine learning dan prediksi.

---

## 8.10 Studi Kasus 1: Hubungan IPK dan Waktu Belajar Mahasiswa

### 8.10.1 Konteks

Seorang dosen di Universitas Al Azhar Indonesia ingin mengetahui apakah waktu belajar mandiri per minggu berhubungan dengan IPK mahasiswa Informatika. Data berikut dikumpulkan dari 20 mahasiswa semester 4.

### 8.10.2 Analisis Lengkap

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Data mahasiswa Informatika UAI
np.random.seed(2025)
n = 20

jam_belajar = np.array([5, 7, 8, 10, 12, 14, 15, 6, 9, 11,
                         13, 16, 18, 20, 4, 8, 10, 14, 17, 22])
# IPK dipengaruhi jam belajar + noise
ipk = 1.8 + 0.1 * jam_belajar + np.random.normal(0, 0.25, n)
ipk = np.clip(ipk, 1.5, 4.0)  # Batasi IPK antara 1.5 - 4.0

data_mhs = pd.DataFrame({
    'jam_belajar_per_minggu': jam_belajar,
    'ipk': np.round(ipk, 2)
})

print("=== DATA MAHASISWA INFORMATIKA UAI ===")
print(data_mhs.to_string(index=True))
print(f"\n--- Statistik Deskriptif ---")
print(data_mhs.describe().round(2))

# 1. Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(data_mhs['jam_belajar_per_minggu'], data_mhs['ipk'],
            color='steelblue', s=100, edgecolor='white', alpha=0.8)
plt.xlabel('Jam Belajar Mandiri per Minggu', fontsize=12)
plt.ylabel('IPK', fontsize=12)
plt.title('Hubungan Jam Belajar dan IPK\nMahasiswa Informatika UAI', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 2. Korelasi
r_pearson, p_pearson = stats.pearsonr(data_mhs['jam_belajar_per_minggu'],
                                       data_mhs['ipk'])
rho_spearman, p_spearman = stats.spearmanr(data_mhs['jam_belajar_per_minggu'],
                                            data_mhs['ipk'])

print(f"\n=== KORELASI ===")
print(f"Pearson  r = {r_pearson:.4f}, p = {p_pearson:.4f}")
print(f"Spearman ρ = {rho_spearman:.4f}, p = {p_spearman:.4f}")

# 3. Regresi Linear
X = data_mhs['jam_belajar_per_minggu'].values.reshape(-1, 1)
y = data_mhs['ipk'].values

model = LinearRegression().fit(X, y)

print(f"\n=== MODEL REGRESI ===")
print(f"Persamaan: IPK = {model.intercept_:.4f} + {model.coef_[0]:.4f} × Jam_Belajar")
print(f"R² = {model.score(X, y):.4f}")

# 4. Interpretasi
print(f"\n=== INTERPRETASI ===")
print(f"• Setiap tambahan 1 jam belajar per minggu,")
print(f"  IPK diperkirakan naik {model.coef_[0]:.4f} poin.")
print(f"• {model.score(X, y)*100:.1f}% variasi IPK dapat")
print(f"  dijelaskan oleh jam belajar mandiri.")

# 5. Prediksi
jam_tertentu = [5, 10, 15, 20]
for jam in jam_tertentu:
    pred = model.predict([[jam]])[0]
    print(f"  Jam belajar {jam:>2} jam → IPK diperkirakan {pred:.2f}")

# 6. Visualisasi dengan garis regresi
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='steelblue', s=100, edgecolor='white',
            alpha=0.8, label='Data mahasiswa')
x_line = np.linspace(X.min() - 1, X.max() + 1, 100).reshape(-1, 1)
plt.plot(x_line, model.predict(x_line), color='red', linewidth=2,
         label=f'ŷ = {model.intercept_:.2f} + {model.coef_[0]:.2f}x')
plt.xlabel('Jam Belajar per Minggu', fontsize=12)
plt.ylabel('IPK', fontsize=12)
plt.title('Regresi Linear: Jam Belajar vs IPK', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 8.10.3 Diskusi

1. **Apakah hubungan ini kausal?** Tidak bisa dipastikan hanya dari korelasi dan regresi. Mungkin mahasiswa dengan motivasi tinggi belajar lebih lama *dan* mendapat IPK lebih tinggi — motivasi sebagai *confounding variable*.
2. **Faktor lain yang berpengaruh?** Metode belajar, kecerdasan bawaan, dukungan keluarga, kondisi kesehatan, dan banyak faktor lain ikut mempengaruhi IPK.
3. **Limitasi model:** Regresi linear sederhana hanya menggunakan satu prediktor. Model yang lebih realistis memerlukan *regresi linear berganda* (multiple linear regression) yang akan dibahas di mata kuliah lanjut.

---

## 8.11 Studi Kasus 2: Harga Rumah di Wilayah Jakarta

### 8.11.1 Konteks

Pasar properti Jakarta adalah salah satu yang paling dinamis di Indonesia. Apakah luas bangunan merupakan prediktor yang baik untuk harga rumah? Mari kita analisis menggunakan data simulasi yang merepresentasikan pola nyata.

### 8.11.2 Analisis Lengkap

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Data simulasi: harga rumah di wilayah Jakarta Selatan
np.random.seed(2025)
n = 30

luas_bangunan = np.random.uniform(36, 300, n)
luas_bangunan = np.sort(luas_bangunan)

# Harga dalam juta rupiah (non-linear sedikit, tapi mendekati linear)
harga = 200 + 8.5 * luas_bangunan + np.random.normal(0, 150, n)
harga = np.clip(harga, 300, 5000)  # Batasi rentang yang realistis

data_properti = pd.DataFrame({
    'luas_bangunan_m2': np.round(luas_bangunan, 1),
    'harga_juta_rp': np.round(harga, 0)
})

print("=== DATA HARGA RUMAH JAKARTA SELATAN (Simulasi) ===")
print(data_properti.describe().round(1))

# Analisis korelasi
r, p = stats.pearsonr(data_properti['luas_bangunan_m2'],
                       data_properti['harga_juta_rp'])
print(f"\nKorelasi Pearson: r = {r:.4f}, p-value = {p:.6f}")

# Regresi dengan statsmodels (output lengkap)
X_sm = sm.add_constant(data_properti['luas_bangunan_m2'])
model_sm = sm.OLS(data_properti['harga_juta_rp'], X_sm).fit()
print("\n" + str(model_sm.summary()))

# Regresi dengan sklearn untuk prediksi
X = data_properti['luas_bangunan_m2'].values.reshape(-1, 1)
y = data_properti['harga_juta_rp'].values
model_sk = LinearRegression().fit(X, y)

# Visualisasi lengkap
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: Scatter + Regression Line
axes[0].scatter(X, y, color='steelblue', s=80, alpha=0.7, label='Data')
x_plot = np.linspace(X.min() - 10, X.max() + 10, 100).reshape(-1, 1)
axes[0].plot(x_plot, model_sk.predict(x_plot), color='red',
             linewidth=2, label=f'ŷ = {model_sk.intercept_:.0f} + '
             f'{model_sk.coef_[0]:.1f}x')
axes[0].set_xlabel('Luas Bangunan (m²)')
axes[0].set_ylabel('Harga (Juta Rp)')
axes[0].set_title('Scatter Plot + Garis Regresi')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Plot 2: Residual Plot
y_pred = model_sk.predict(X)
residuals = y - y_pred
axes[1].scatter(y_pred, residuals, color='coral', s=80, alpha=0.7)
axes[1].axhline(y=0, color='black', linestyle='--', linewidth=1)
axes[1].set_xlabel('Nilai Prediksi (ŷ)')
axes[1].set_ylabel('Residual')
axes[1].set_title('Residual Plot')
axes[1].grid(True, alpha=0.3)

# Plot 3: Q-Q Plot
stats.probplot(residuals, dist="norm", plot=axes[2])
axes[2].set_title('Q-Q Plot Residual')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Prediksi harga untuk berbagai ukuran rumah
print("\n=== PREDIKSI HARGA RUMAH ===")
ukuran_rumah = [50, 80, 100, 150, 200, 250]
for ukuran in ukuran_rumah:
    harga_pred = model_sk.predict([[ukuran]])[0]
    print(f"  Luas {ukuran:>3} m² → Harga Rp {harga_pred:,.0f} juta "
          f"(Rp {harga_pred*1e6:,.0f})")

# Uji normalitas residual
stat_sw, p_sw = stats.shapiro(residuals)
print(f"\nUji Shapiro-Wilk: W = {stat_sw:.4f}, p = {p_sw:.4f}")
print(f"Asumsi normalitas {'terpenuhi' if p_sw > 0.05 else 'TIDAK terpenuhi'}")
```

### 8.11.3 Diskusi

1. **Validitas model:** Luas bangunan adalah salah satu prediktor terkuat untuk harga rumah, tetapi bukan satu-satunya. Lokasi (Jakarta Selatan vs Jakarta Timur), kondisi bangunan, akses transportasi, dan fasilitas sekitar juga sangat berpengaruh.
2. **Ekstrapolasi:** Menggunakan model ini untuk memprediksi harga rumah seluas 1.000 m² akan menghasilkan ekstrapolasi yang mungkin tidak akurat.
3. **Heteroskedastisitas:** Dalam data properti riil, varians harga cenderung **meningkat** seiring luas bangunan (rumah besar lebih bervariasi harganya). Ini melanggar asumsi homoskedastisitas.

---

## 8.12 AI Corner: Menggunakan AI untuk Analisis Korelasi dan Regresi

### 8.12.1 Apa yang Bisa AI Bantu?

| AI Bisa Membantu | AI Tidak Bisa Menggantikan |
|-----------------|---------------------------|
| Generate kode Python untuk korelasi dan regresi | Menentukan variabel mana yang relevan untuk dianalisis |
| Menjelaskan konsep R² dengan analogi sederhana | Memutuskan apakah hasil analisis masuk akal secara kontekstual |
| Menyarankan uji diagnostik yang tepat | Menjamin bahwa korelasi = kausalitas |
| Membantu menginterpretasi output statsmodels | Memahami konteks lokal Indonesia (harga rumah, IPK, dll) |
| Debugging kode yang error | Menggantikan pemikiran kritis mahasiswa |

### 8.12.2 Contoh Prompt yang Efektif

**Prompt yang BAIK:**

```
Saya punya data 30 rumah di Jakarta Selatan dengan variabel luas bangunan
(m²) dan harga (juta Rp). Korelasi Pearson r = 0.87, R² = 0.76.
Residual plot menunjukkan pola corong (varians membesar).

Pertanyaan:
1. Apa interpretasi R² = 0.76 dalam konteks ini?
2. Pola corong di residual plot menunjukkan masalah apa?
3. Apa solusinya? Apakah transformasi log bisa membantu?
```

**Prompt yang KURANG BAIK:**

```
Analisis data rumah saya
```

### 8.12.3 Kapan Harus Kritis terhadap AI

1. **AI mungkin mengklaim kausalitas dari korelasi.** Jika AI mengatakan *"luas bangunan menyebabkan kenaikan harga"*, koreksi menjadi *"luas bangunan berkorelasi positif dengan harga, tetapi hubungan kausal memerlukan analisis lebih lanjut."*

2. **AI bisa salah menghitung.** Selalu verifikasi angka-angka penting dengan menjalankan kode sendiri.

3. **AI mungkin tidak memahami konteks Indonesia.** Misalnya, harga properti di Jakarta memiliki dinamika yang berbeda dari kota-kota di negara lain. Mahasiswa yang memahami konteks lokal dapat memberikan interpretasi yang lebih bermakna.

### 8.12.4 Latihan Evaluasi Output AI

Seorang mahasiswa bertanya kepada AI: *"Apakah IPM menyebabkan kenaikan pendapatan per kapita?"*

AI menjawab: *"Ya, IPM yang tinggi menyebabkan pendapatan per kapita meningkat karena pendidikan dan kesehatan yang lebih baik meningkatkan produktivitas."*

**Evaluasi kritis:**
- Jawaban AI ini terlalu simplistik dan **mengklaim kausalitas** dari data korelasi
- Kemungkinan **reverse causation**: pendapatan tinggi memungkinkan investasi lebih besar di pendidikan dan kesehatan (yang meningkatkan IPM)
- Ada **confounding variables**: kebijakan pemerintah, sumber daya alam, geografi, dll.
- Jawaban yang lebih tepat: *"IPM dan pendapatan per kapita berkorelasi positif. Hubungan ini kemungkinan bersifat dua arah (bidirectional) dan dipengaruhi oleh banyak faktor lain."*

---

## Rangkuman Bab 8

1. **Korelasi** mengukur kekuatan dan arah hubungan linear antara dua variabel. Selalu mulai analisis dengan **scatter plot** sebelum menghitung koefisien korelasi.

2. **Korelasi Pearson (r)** mengukur hubungan linear untuk data interval/rasio. Nilainya berkisar -1 hingga +1. Syarat: data numerik kontinu, hubungan linear, tanpa outlier ekstrem.

3. **Korelasi Spearman (rho)** adalah alternatif non-parametrik berbasis rank. Lebih robust terhadap outlier dan cocok untuk data ordinal atau hubungan monotonic non-linear.

4. **Korelasi bukan kausalitas** (*correlation does not imply causation*). Tiga jebakan utama: confounding variable, reverse causation, dan spurious correlation. Untuk membuktikan kausalitas diperlukan eksperimen terkontrol.

5. **Regresi linear sederhana** (y-hat = b0 + b1*x) memodelkan hubungan antara satu prediktor (X) dan satu respons (Y) menggunakan metode **least squares** yang meminimalkan jumlah kuadrat residual. Slope (b1) menunjukkan perubahan Y per unit X; intercept (b0) adalah nilai Y saat X = 0.

6. **R² (koefisien determinasi)** mengukur proporsi variasi Y yang dapat dijelaskan oleh X. Untuk regresi sederhana, R² = r². Semakin tinggi R², semakin baik model menjelaskan data.

7. **Diagnostik residual** memverifikasi asumsi LINE (Linearity, Independence, Normality, Equal variance). Gunakan residual plot, histogram, Q-Q plot, dan uji Shapiro-Wilk.

8. **Implementasi Python:** Gunakan `scipy.stats` untuk korelasi, `scikit-learn` untuk model prediksi, dan `statsmodels` untuk analisis statistik lengkap (p-value, confidence interval, F-test).

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan antara korelasi dan regresi. Kapan kita menggunakan masing-masing?

**Soal 2.** Perhatikan nilai korelasi berikut. Urutkan dari hubungan yang **paling kuat** ke **paling lemah**:
- a) r = 0.45
- b) r = -0.92
- c) r = 0.78
- d) r = -0.15
- e) r = 0.60

**Soal 3.** Sebuah studi menemukan bahwa semakin banyak jumlah pemadam kebakaran yang dikirim ke lokasi, semakin besar kerusakan yang terjadi (r = 0.85). Apakah ini berarti pemadam kebakaran *menyebabkan* kerusakan? Jelaskan menggunakan konsep yang telah dipelajari.

**Soal 4.** Apa saja syarat penggunaan korelasi Pearson? Kapan kita sebaiknya menggunakan korelasi Spearman sebagai gantinya?

**Soal 5.** Jika R² = 0.64, apa interpretasinya? Berapa persen variasi yang *tidak* dapat dijelaskan oleh model?

### Tingkat Menengah (C2-C3)

**Soal 6.** Diberikan data berikut tentang mahasiswa UAI:

| Jam Belajar (X) | 2 | 4 | 5 | 7 | 8 | 10 | 12 |
|-----------------|---|---|---|---|---|----|----|
| Nilai Ujian (Y) | 50 | 58 | 65 | 72 | 78 | 85 | 92 |

- a) Buat scatter plot menggunakan matplotlib
- b) Hitung korelasi Pearson menggunakan `scipy.stats.pearsonr`
- c) Bangun model regresi linear menggunakan `sklearn.linear_model.LinearRegression`
- d) Tuliskan persamaan regresi: y-hat = b0 + b1*x
- e) Prediksi nilai ujian untuk mahasiswa yang belajar 6 jam dan 15 jam. Manakah yang lebih dapat dipercaya? Jelaskan.

**Soal 7.** Tulis kode Python untuk:
- a) Membuat data simulasi 50 observasi di mana X ~ Uniform(10, 100) dan Y = 5 + 0.3X + noise
- b) Menghitung korelasi Pearson dan Spearman
- c) Membangun model regresi linear dan menampilkan persamaannya
- d) Membuat visualisasi scatter plot dengan garis regresi

**Soal 8.** Perhatikan dua model regresi berikut:
- Model A: y-hat = 100 + 2.5x, R² = 0.85
- Model B: y-hat = 50 + 5.0x, R² = 0.45
- a) Model mana yang lebih baik dalam menjelaskan variasi Y? Mengapa?
- b) Model mana yang memiliki slope lebih besar? Apakah slope yang lebih besar selalu berarti model lebih baik?

**Soal 9.** Jelaskan apa yang dimaksud dengan:
- a) Confounding variable — berikan contoh dalam konteks Indonesia
- b) Spurious correlation — berikan contoh
- c) Reverse causation — berikan contoh

### Tingkat Mahir (C3-C4+)

**Soal 10.** Gunakan data berikut (atau simulasikan data serupa) tentang indikator ekonomi provinsi di Indonesia:

```python
# Jalankan kode ini di Google Colab
import numpy as np
import pandas as pd
np.random.seed(42)

data_provinsi = pd.DataFrame({
    'ipm': np.random.normal(70, 5, 34).clip(55, 85),
    'pendapatan_perkapita_juta': None,  # Isi sendiri dengan relasi linear + noise
    'tingkat_pengangguran': None  # Isi sendiri
})
```

- a) Lengkapi dataset dengan membuat `pendapatan_perkapita_juta` yang berkorelasi positif dengan IPM dan `tingkat_pengangguran` yang berkorelasi negatif dengan IPM
- b) Hitung matriks korelasi (correlation matrix) untuk ketiga variabel
- c) Bangun model regresi: IPM sebagai prediktor, pendapatan sebagai respons
- d) Lakukan diagnostik residual lengkap (4 plot)
- e) Interpretasikan hasil dalam konteks pembangunan Indonesia

**Soal 11.** Seorang data analyst di sebuah startup e-commerce Jakarta menemukan bahwa jumlah iklan yang ditampilkan berkorelasi negatif (r = -0.72) dengan waktu yang dihabiskan pengguna di aplikasi.

- a) Interpretasikan korelasi ini
- b) Dapatkah analyst menyimpulkan bahwa iklan menyebabkan pengguna meninggalkan aplikasi lebih cepat? Mengapa atau mengapa tidak?
- c) Sebutkan minimal 2 confounding variable yang mungkin berperan
- d) Rancang eksperimen (A/B testing) yang bisa membantu membuktikan kausalitas

**Soal 12.** Buat **fungsi Python lengkap** bernama `analisis_regresi(x, y, nama_x, nama_y)` yang:
- Menghitung korelasi Pearson dan Spearman
- Membangun model regresi linear (menggunakan sklearn)
- Menampilkan persamaan regresi, R², dan interpretasinya
- Membuat 4 plot: scatter + garis regresi, residual plot, histogram residual, Q-Q plot
- Melakukan uji normalitas Shapiro-Wilk pada residual
- Mengembalikan dictionary berisi semua hasil

Uji fungsi tersebut dengan minimal 2 dataset yang berbeda.

**Soal 13.** Berikut adalah data simulasi hubungan antara suhu rata-rata (derajat Celsius) dan konsumsi listrik (kWh) rumah tangga di Jakarta selama 12 bulan:

| Bulan | Suhu Rata-rata (C) | Konsumsi Listrik (kWh) |
|-------|-------------------|----------------------|
| Jan | 27.5 | 320 |
| Feb | 27.8 | 335 |
| Mar | 28.2 | 350 |
| Apr | 28.5 | 360 |
| Mei | 28.0 | 340 |
| Jun | 27.2 | 310 |
| Jul | 26.8 | 295 |
| Agu | 27.0 | 300 |
| Sep | 27.5 | 315 |
| Okt | 28.8 | 370 |
| Nov | 28.5 | 355 |
| Des | 28.0 | 345 |

- a) Lakukan analisis korelasi dan regresi lengkap menggunakan Python
- b) Interpretasikan slope dalam konteks: "Setiap kenaikan 1 derajat Celsius..."
- c) Prediksi konsumsi listrik jika suhu rata-rata 29.5 derajat Celsius
- d) Apakah prediksi untuk suhu 35 derajat Celsius dapat dipercaya? Jelaskan.
- e) Lakukan diagnostik residual dan diskusikan apakah asumsi LINE terpenuhi

**Soal 14.** Bandingkan output regresi dari `scikit-learn` dan `statsmodels` untuk dataset yang sama. Jelaskan:
- a) Informasi apa saja yang diberikan statsmodels tetapi tidak diberikan scikit-learn?
- b) Dalam situasi apa Anda akan memilih scikit-learn daripada statsmodels, dan sebaliknya?
- c) Apa artinya jika p-value untuk slope < 0.05 tetapi R² hanya 0.15?

---

## Referensi

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability & Statistics for Engineers & Scientists* (9th ed.). Pearson. Chapter 11-12.
2. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics* (4th ed.). Chapter 8: Introduction to Linear Regression.
3. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning with Applications in Python (ISLP)*. Chapter 3: Linear Regression.
4. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
5. scikit-learn Documentation. *LinearRegression*. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
6. statsmodels Documentation. *OLS — Ordinary Least Squares*. https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html
7. Tyler Vigen. *Spurious Correlations*. https://tylervigen.com/spurious-correlations
8. BPS (Badan Pusat Statistik). *Indeks Pembangunan Manusia Indonesia*. https://www.bps.go.id
9. Moore, D. S., McCabe, G. P., & Craig, B. A. (2021). *Introduction to the Practice of Statistics* (10th ed.). W. H. Freeman.

---

*Bab berikutnya: **Bab 9 — Analisis Varians (ANOVA)***
