# BAB 11: ANALISIS DATA KATEGORIKAL

**Tri Aji Nugroho, S.T., M.T.**
Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-6.6 | Membuat dan membaca tabel frekuensi serta contingency table untuk data kategorikal | C3 |
| CPMK-6.7 | Melaksanakan chi-square test of independence dan goodness of fit serta menginterpretasi hasilnya | C4 |
| CPMK-6.8 | Menghitung dan menginterpretasi odds ratio dan relative risk untuk tabel 2x2 | C4 |
| CPMK-6.9 | Menjelaskan konsep logistic regression untuk outcome biner dan menginterpretasi koefisien melalui odds ratio | C4 |
| CPMK-6.10 | Mengimplementasikan analisis data kategorikal menggunakan Python (scipy, sklearn, statsmodels) pada studi kasus nyata | C4 |

---

## 11.1 Pendahuluan: Mengapa Data Kategorikal Butuh Teknik Khusus?

### 11.1.1 Data Kategorikal dalam Kehidupan Sehari-hari

Pada bab-bab sebelumnya, kita banyak bekerja dengan variabel **numerik** (kontinu maupun diskret) — misalnya IPK, pengeluaran bulanan, atau harga rumah. Namun, banyak data di dunia nyata berbentuk **kategorikal**, yaitu variabel yang nilainya berupa kategori atau label, bukan angka kontinu.

**Contoh variabel kategorikal di Indonesia:**
- Platform e-commerce yang digunakan (Tokopedia / Shopee / Lazada / Bukalapak)
- Metode pembayaran (GoPay / OVO / Dana / Transfer bank / COD)
- Status kelulusan (Lulus / Tidak lulus)
- Tingkat kepuasan pelanggan (Sangat Puas / Puas / Netral / Tidak Puas)
- Jenis kelamin (Laki-laki / Perempuan)
- Provinsi asal (DKI Jakarta / Jawa Barat / Jawa Timur / ...)

> "You cannot take the average of a category. The mean of 'Shopee' and 'Tokopedia' is meaningless."
> — Prinsip dasar analisis data kategorikal

### 11.1.2 Mengapa Teknik Berbeda?

Kita tidak bisa menghitung "rata-rata" dari kategori. Tidak masuk akal mengatakan "rata-rata platform e-commerce mahasiswa adalah 1.47." Untuk data kategorikal, kita bekerja dengan **frekuensi** dan **proporsi**.

```
JENIS ANALISIS BERDASARKAN TIPE VARIABEL
═══════════════════════════════════════════════════════════

Variabel X        Variabel Y        Teknik Analisis
──────────        ──────────        ───────────────
Numerik       vs  Numerik       →   Korelasi, Regresi (Bab 8-9)
Kategorikal   vs  Numerik       →   ANOVA, Kruskal-Wallis (Bab 10)
Kategorikal   vs  Kategorikal   →   Chi-Square (Bab 11)  ← ANDA DI SINI
Numerik/Kat.  →   Biner (0/1)   →   Logistic Regression (Bab 11)
```

### 11.1.3 Alat Analisis Data Kategorikal

| Teknik | Tujuan | Kapan Digunakan |
|--------|--------|-----------------|
| **Tabel frekuensi** | Meringkas distribusi satu variabel | Deskripsi awal data kategorikal |
| **Contingency table** | Melihat hubungan dua variabel kategorikal | Eksplorasi hubungan antar kategori |
| **Chi-square test of independence** | Menguji hubungan dua variabel kategorikal | Inferensi: apakah ada hubungan? |
| **Chi-square goodness of fit** | Menguji apakah distribusi sesuai teori | Apakah data mengikuti distribusi tertentu? |
| **Fisher's exact test** | Alternatif chi-square untuk sampel kecil | Jika expected frequency < 5 |
| **Odds ratio & relative risk** | Mengukur kekuatan hubungan | Kuantifikasi perbedaan antar kelompok |
| **Logistic regression** | Memprediksi outcome biner | Pemodelan dengan banyak prediktor |

---

## 11.2 Tabel Frekuensi dan Contingency Table

### 11.2.1 Tabel Frekuensi Satu Variabel

Tabel frekuensi adalah cara paling sederhana untuk meringkas data kategorikal. Tabel ini menunjukkan berapa kali setiap kategori muncul.

**Contoh:** Survei terhadap 200 mahasiswa tentang platform e-commerce favorit.

```
╔══════════════════╦═══════════╦════════════╗
║ Platform         ║ Frekuensi ║ Proporsi   ║
╠══════════════════╬═══════════╬════════════╣
║ Shopee           ║    82     ║   41.0%    ║
║ Tokopedia        ║    58     ║   29.0%    ║
║ Lazada           ║    35     ║   17.5%    ║
║ Bukalapak        ║    25     ║   12.5%    ║
╠══════════════════╬═══════════╬════════════╣
║ Total            ║   200     ║  100.0%    ║
╚══════════════════╩═══════════╩════════════╝
```

### 11.2.2 Contingency Table (Tabel Kontingensi)

**Contingency table** (tabel kontingensi) adalah tabel silang yang menunjukkan distribusi frekuensi gabungan dari dua variabel kategorikal. Ini adalah langkah pertama sebelum melakukan uji chi-square.

**Contoh:** Hubungan antara gender dan platform e-commerce favorit.

```
CONTINGENCY TABLE: Gender vs Platform E-Commerce
═══════════════════════════════════════════════════════════════
                 Shopee   Tokopedia   Lazada   Bukalapak  Total
───────────────────────────────────────────────────────────────
Laki-laki          30        35        18         12        95
Perempuan          52        23        17         13       105
───────────────────────────────────────────────────────────────
Total              82        58        35         25       200
═══════════════════════════════════════════════════════════════
```

Dari tabel ini, kita bisa bertanya: **Apakah preferensi platform e-commerce berbeda antara mahasiswa laki-laki dan perempuan?**

### 11.2.3 Membuat Contingency Table dengan Python

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Simulasi data survei platform e-commerce mahasiswa
np.random.seed(2025)
n = 200

gender = np.random.choice(['Laki-laki', 'Perempuan'], n, p=[0.475, 0.525])

# Preferensi platform (beri sedikit hubungan dengan gender)
platform = []
for g in gender:
    if g == 'Laki-laki':
        p = np.random.choice(
            ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak'],
            p=[0.30, 0.38, 0.19, 0.13]
        )
    else:
        p = np.random.choice(
            ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak'],
            p=[0.50, 0.22, 0.16, 0.12]
        )
    platform.append(p)

survei = pd.DataFrame({
    'gender': gender,
    'platform': platform
})

# Tabel frekuensi satu variabel
print("=== Tabel Frekuensi: Platform ===")
print(survei['platform'].value_counts())
print(f"\nProporsi:")
print(survei['platform'].value_counts(normalize=True).round(3))

# Contingency table
ct = pd.crosstab(survei['gender'], survei['platform'], margins=True)
print(f"\n=== Contingency Table: Gender vs Platform ===")
print(ct)

# Proporsi per baris (menunjukkan distribusi platform per gender)
ct_pct = pd.crosstab(survei['gender'], survei['platform'], normalize='index')
print(f"\n=== Proporsi per Gender ===")
print(ct_pct.round(3))
```

### 11.2.4 Visualisasi Contingency Table

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Stacked bar chart
ct_pct = pd.crosstab(survei['gender'], survei['platform'], normalize='index')
ct_pct.plot(kind='bar', stacked=True, ax=axes[0], colormap='Set2',
            edgecolor='white')
axes[0].set_xlabel('Gender', fontsize=11)
axes[0].set_ylabel('Proporsi', fontsize=11)
axes[0].set_title('Proporsi Platform E-Commerce per Gender', fontsize=13)
axes[0].legend(title='Platform', bbox_to_anchor=(1.02, 1))
axes[0].tick_params(axis='x', rotation=0)
axes[0].grid(True, alpha=0.3, axis='y')

# Heatmap frekuensi
ct_no_margins = pd.crosstab(survei['gender'], survei['platform'])
sns.heatmap(ct_no_margins, annot=True, fmt='d', cmap='YlOrRd', ax=axes[1])
axes[1].set_title('Heatmap: Gender vs Platform (Frekuensi)', fontsize=13)

plt.tight_layout()
plt.show()
```

### 11.2.5 Konsep Mosaic Plot

Mosaic plot adalah visualisasi khusus untuk contingency table di mana luas setiap kotak proporsional terhadap frekuensi sel. Berikut konsep dasarnya dalam bentuk ASCII:

```
MOSAIC PLOT: Gender vs Platform E-Commerce (konseptual)
═══════════════════════════════════════════════════════════

     ┌───────────────┬──────────┬────────┬──────┐
     │               │          │        │      │
     │   Shopee      │Tokopedia │ Lazada │Buka- │
L    │   (30)        │  (35)    │ (18)   │lapak │  ← Laki-laki
     │               │          │        │ (12) │
     ├───────────────┼──────────┼────────┼──────┤
     │               │          │        │      │
     │   Shopee      │Tokopedia │ Lazada │Buka- │
P    │   (52)        │  (23)    │ (17)   │lapak │  ← Perempuan
     │               │          │        │ (13) │
     │               │          │        │      │
     └───────────────┴──────────┴────────┴──────┘

     Lebar tiap kolom ~ proporsi total platform
     Tinggi tiap baris ~ proporsi total gender
     Luas setiap kotak ~ frekuensi sel
```

---

## 11.3 Chi-Square Test of Independence

### 11.3.1 Konsep Dasar

Chi-square test of independence menguji apakah dua variabel kategorikal **berhubungan** (dependen) atau **tidak berhubungan** (independen).

**Hipotesis:**
- **H0:** Kedua variabel independen (tidak berhubungan)
- **H1:** Kedua variabel dependen (ada hubungan)

**Contoh pertanyaan penelitian:**
- Apakah preferensi platform e-commerce berbeda antara mahasiswa laki-laki dan perempuan?
- Apakah ada hubungan antara fakultas dan tingkat kepuasan terhadap layanan kampus?
- Apakah metode pembayaran yang dipilih berkaitan dengan kelompok usia?

### 11.3.2 Expected Frequencies (Frekuensi Harapan)

Jika kedua variabel **benar-benar independen**, berapa frekuensi yang kita *harapkan* di setiap sel? Logikanya: jika gender dan platform tidak berhubungan, maka proporsi pemilih setiap platform harus sama untuk laki-laki dan perempuan.

**Rumus expected frequency:**

```
E_ij = (Row_total_i x Column_total_j) / Grand_total
```

**Contoh perhitungan:** Expected frequency laki-laki yang memilih Shopee:

```
E = (95 x 82) / 200 = 38.95
```

Artinya: jika gender dan platform independen, kita *mengharapkan* sekitar 39 mahasiswa laki-laki memilih Shopee. Jika frekuensi observasi sangat berbeda dari 39, itu indikasi adanya hubungan.

```
PERBANDINGAN OBSERVED vs EXPECTED (ilustrasi)
═══════════════════════════════════════════════════════

     Observed (O)              Expected (E) jika H0 benar
     ─────────────             ──────────────────────────
     Shopee  Toko  Laz  Buka  Shopee  Toko  Laz   Buka
L:    30     35    18   12     38.95  27.55  16.63  11.88
P:    52     23    17   13     43.05  30.45  18.38  13.13

     Perbedaan (O - E) menentukan besar chi-square
```

### 11.3.3 Rumus Chi-Square

Statistik uji chi-square mengukur seberapa jauh frekuensi observasi menyimpang dari frekuensi harapan:

```
         k
chi2 =  SUM  (O_i - E_i)^2 / E_i
        i=1

Di mana:
  O_i = frekuensi observasi di sel ke-i
  E_i = frekuensi harapan di sel ke-i
  k   = jumlah total sel dalam tabel
```

**Derajat kebebasan (degrees of freedom):**

```
df = (r - 1) x (c - 1)

Di mana:
  r = jumlah baris
  c = jumlah kolom
```

Untuk tabel 2x4 (gender vs 4 platform): df = (2-1)(4-1) = 3

**Keputusan:**
- Jika p-value < alpha (0.05): **Tolak H0** — ada hubungan signifikan
- Jika p-value >= alpha (0.05): **Gagal tolak H0** — tidak cukup bukti adanya hubungan

### 11.3.4 Syarat Penggunaan Chi-Square Test

| Syarat | Penjelasan | Jika Tidak Terpenuhi |
|--------|------------|---------------------|
| Expected frequency >= 5 | Setiap sel harus memiliki E >= 5 | Gabungkan kategori atau gunakan Fisher's exact test |
| Observasi independen | Setiap observasi hanya masuk satu sel | Pastikan desain survei benar |
| Data berupa frekuensi | Bukan proporsi atau persentase | Gunakan data mentah (raw counts) |
| Ukuran sampel cukup besar | Aturan umum: n >= 20-30 | Kumpulkan lebih banyak data |

### 11.3.5 Implementasi Chi-Square Test dengan Python

```python
# ============================================================
# CHI-SQUARE TEST OF INDEPENDENCE
# ============================================================

# Membuat contingency table (tanpa margins)
ct_chi = pd.crosstab(survei['gender'], survei['platform'])

# Chi-square test menggunakan scipy
chi2, p_value, dof, expected = stats.chi2_contingency(ct_chi)

print("=== Chi-Square Test of Independence ===")
print(f"H0: Gender dan platform e-commerce independen")
print(f"H1: Gender dan platform e-commerce dependen (ada hubungan)")
print(f"\nChi-square statistic (chi2): {chi2:.4f}")
print(f"Degrees of freedom (df): {dof}")
print(f"P-value: {p_value:.6f}")

# Tampilkan expected frequencies
print(f"\n=== Expected Frequencies (jika H0 benar) ===")
expected_df = pd.DataFrame(
    expected,
    index=ct_chi.index,
    columns=ct_chi.columns
)
print(expected_df.round(2))

# Cek syarat: semua expected >= 5?
print(f"\nMinimum expected frequency: {expected.min():.2f}")
print(f"Semua expected >= 5? {'Ya - syarat terpenuhi' if expected.min() >= 5 else 'TIDAK - pertimbangkan Fisher exact test!'}")

# Perbandingan observed vs expected
print(f"\n=== Observed vs Expected (detail per sel) ===")
for gender in ct_chi.index:
    for plat in ct_chi.columns:
        obs = ct_chi.loc[gender, plat]
        exp = expected_df.loc[gender, plat]
        kontribusi = (obs - exp)**2 / exp
        print(f"  {gender:10s} - {plat:12s}: O = {obs:3d}, E = {exp:5.1f}, "
              f"(O-E)^2/E = {kontribusi:.3f}")

# Keputusan
alpha = 0.05
print(f"\n=== Keputusan (alpha = {alpha}) ===")
if p_value < alpha:
    print(f"p-value ({p_value:.6f}) < {alpha} --> TOLAK H0")
    print("Kesimpulan: Ada hubungan signifikan antara gender dan preferensi platform.")
else:
    print(f"p-value ({p_value:.6f}) >= {alpha} --> GAGAL TOLAK H0")
    print("Kesimpulan: Tidak cukup bukti adanya hubungan antara gender dan "
          "preferensi platform.")
```

### 11.3.6 Effect Size: Cramer's V

Chi-square test hanya memberi tahu ada/tidaknya hubungan, tetapi tidak mengukur **seberapa kuat** hubungan tersebut. Untuk itu, kita gunakan **Cramer's V**:

```
V = sqrt(chi2 / (n x (min(r, c) - 1)))

Di mana:
  chi2     = statistik chi-square
  n        = total observasi
  min(r,c) = minimum dari jumlah baris dan kolom
```

| Cramer's V | Interpretasi |
|------------|-------------|
| < 0.10 | Hubungan sangat lemah (negligible) |
| 0.10 - 0.30 | Hubungan lemah |
| 0.30 - 0.50 | Hubungan sedang |
| > 0.50 | Hubungan kuat |

```python
# Menghitung Cramer's V
def cramers_v(chi2_stat, n_obs, min_dim):
    """Menghitung Cramer's V sebagai ukuran effect size."""
    return np.sqrt(chi2_stat / (n_obs * (min_dim - 1)))

n_obs = ct_chi.values.sum()
min_dim = min(ct_chi.shape)
v = cramers_v(chi2, n_obs, min_dim)

print(f"=== Effect Size: Cramer's V ===")
print(f"Cramer's V = {v:.4f}")
if v < 0.10:
    print("Interpretasi: Hubungan sangat lemah (negligible)")
elif v < 0.30:
    print("Interpretasi: Hubungan lemah")
elif v < 0.50:
    print("Interpretasi: Hubungan sedang")
else:
    print("Interpretasi: Hubungan kuat")
```

---

## 11.4 Chi-Square Goodness of Fit Test

### 11.4.1 Konsep

Berbeda dengan chi-square test of independence yang menguji hubungan dua variabel, **goodness of fit test** menguji apakah distribusi satu variabel kategorikal sesuai dengan distribusi yang diharapkan (teoritis).

**Hipotesis:**
- **H0:** Distribusi data sesuai dengan distribusi yang diharapkan
- **H1:** Distribusi data berbeda dari distribusi yang diharapkan

**Contoh pertanyaan:**
- Apakah distribusi pengguna e-commerce Indonesia merata di antara 4 platform? (masing-masing 25%)
- Apakah distribusi jawaban survei sesuai dengan distribusi populasi yang diketahui?
- Apakah jumlah pengunjung website merata setiap hari dalam seminggu?

### 11.4.2 Rumus

Rumus chi-square goodness of fit sama dengan test of independence:

```
chi2 = SUM (O_i - E_i)^2 / E_i

Derajat kebebasan: df = k - 1
Di mana k = jumlah kategori
```

### 11.4.3 Implementasi Python

```python
# ============================================================
# CHI-SQUARE GOODNESS OF FIT TEST
# ============================================================
# Apakah 4 platform e-commerce memiliki pengguna yang merata?

# Frekuensi observasi dari data survei
observed = survei['platform'].value_counts().sort_index()
print("=== Frekuensi Observasi ===")
print(observed)

# Frekuensi harapan: jika distribusi merata (masing-masing 25%)
n_total = len(survei)
k = len(observed)
expected_gof = np.array([n_total / k] * k)
print(f"\nFrekuensi harapan (merata): {expected_gof}")

# Goodness of fit test
chi2_gof, p_gof = stats.chisquare(observed.values, f_exp=expected_gof)

print(f"\n=== Chi-Square Goodness of Fit Test ===")
print(f"H0: Distribusi pengguna merata di 4 platform")
print(f"H1: Distribusi pengguna TIDAK merata")
print(f"\nChi-square statistic: {chi2_gof:.4f}")
print(f"Degrees of freedom: {k - 1}")
print(f"P-value: {p_gof:.6f}")

alpha = 0.05
if p_gof < alpha:
    print(f"\np-value ({p_gof:.6f}) < {alpha} --> TOLAK H0")
    print("Kesimpulan: Distribusi pengguna TIDAK merata di antara platform.")
else:
    print(f"\np-value ({p_gof:.6f}) >= {alpha} --> GAGAL TOLAK H0")
    print("Kesimpulan: Tidak cukup bukti bahwa distribusi pengguna tidak merata.")
```

```python
# Contoh 2: Goodness of fit dengan distribusi non-uniform
# Apakah distribusi survei kita sesuai dengan market share nasional?

# Market share nasional (hipotesis): Shopee 45%, Tokopedia 25%, Lazada 18%, Bukalapak 12%
market_share = np.array([0.45, 0.25, 0.18, 0.12])
expected_market = n_total * market_share

observed_sorted = survei['platform'].value_counts().reindex(
    ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak']
)

chi2_market, p_market = stats.chisquare(observed_sorted.values, f_exp=expected_market)

print("=== Goodness of Fit: vs Market Share Nasional ===")
print(f"Market share yang diuji: Shopee={market_share[0]:.0%}, "
      f"Tokopedia={market_share[1]:.0%}, Lazada={market_share[2]:.0%}, "
      f"Bukalapak={market_share[3]:.0%}")
print(f"\nChi2 = {chi2_market:.4f}, p-value = {p_market:.6f}")
if p_market < 0.05:
    print("Kesimpulan: Distribusi survei berbeda signifikan dari market share nasional.")
else:
    print("Kesimpulan: Distribusi survei konsisten dengan market share nasional.")
```

---

## 11.5 Fisher's Exact Test

### 11.5.1 Kapan Menggunakan Fisher's Exact Test?

Chi-square test memiliki syarat bahwa semua expected frequencies harus >= 5. Jika syarat ini **tidak terpenuhi** (misalnya karena sampel kecil atau kategori langka), kita menggunakan **Fisher's exact test** sebagai alternatif.

Fisher's exact test menghitung **probabilitas eksak** dari distribusi yang diamati (dan semua distribusi yang lebih ekstrem), tanpa menggunakan pendekatan (approximation) seperti chi-square.

**Keterbatasan:** Dalam implementasi `scipy.stats.fisher_exact`, uji ini hanya tersedia untuk tabel **2x2**.

### 11.5.2 Contoh Kasus: Sampel Kecil

```
CONTOH TABEL 2x2 DENGAN FREKUENSI KECIL
═══════════════════════════════════════════

Apakah ada hubungan antara penggunaan AI tool dan keberhasilan
debugging pada sekelompok kecil mahasiswa?

                  Berhasil    Gagal    Total
────────────────────────────────────────────
Pakai AI             8          2       10
Tidak pakai AI       3          7       10
────────────────────────────────────────────
Total               11          9       20

Expected frequency untuk beberapa sel < 5 → gunakan Fisher's exact test
```

### 11.5.3 Implementasi Python

```python
# ============================================================
# FISHER'S EXACT TEST (untuk tabel 2x2 dengan sampel kecil)
# ============================================================

# Data: penggunaan AI tool vs keberhasilan debugging
tabel_2x2 = np.array([[8, 2],
                       [3, 7]])

# Fisher's exact test
odds_ratio_fisher, p_fisher = stats.fisher_exact(tabel_2x2)

print("=== Fisher's Exact Test ===")
print(f"Tabel 2x2:")
print(f"              Berhasil  Gagal")
print(f"  Pakai AI       {tabel_2x2[0,0]}        {tabel_2x2[0,1]}")
print(f"  Tanpa AI       {tabel_2x2[1,0]}        {tabel_2x2[1,1]}")
print(f"\nOdds Ratio: {odds_ratio_fisher:.4f}")
print(f"P-value: {p_fisher:.6f}")

if p_fisher < 0.05:
    print(f"\nKesimpulan: Ada hubungan signifikan antara penggunaan AI "
          f"dan keberhasilan debugging (p = {p_fisher:.4f}).")
else:
    print(f"\nKesimpulan: Tidak cukup bukti adanya hubungan (p = {p_fisher:.4f}).")

# Bandingkan dengan chi-square (untuk edukasi)
chi2_small, p_small = stats.chi2_contingency(tabel_2x2)[:2]
print(f"\nPerbandingan dengan chi-square test:")
print(f"  Chi-square p-value: {p_small:.6f}")
print(f"  Fisher's   p-value: {p_fisher:.6f}")
print("  Fisher's exact test lebih akurat untuk sampel kecil.")
```

---

## 11.6 Odds Ratio dan Relative Risk

### 11.6.1 Konsep Odds

**Odds** adalah rasio probabilitas suatu kejadian terjadi versus tidak terjadi:

```
                P(event)          P(event)
Odds(event) = ─────────── = ──────────────────
              P(not event)   1 - P(event)
```

**Contoh:** Jika probabilitas mahasiswa memilih Shopee adalah 0.6, maka:
- Odds = 0.6 / 0.4 = 1.5
- Artinya: "Untuk setiap 3 mahasiswa yang tidak memilih Shopee, ada sekitar 4-5 yang memilih Shopee."

> **Penting:** Odds bukanlah probabilitas! Odds = 1.5 **bukan berarti** probabilitas 1.5 (tidak mungkin). Odds bisa bernilai 0 sampai tak hingga, sedangkan probabilitas hanya 0 sampai 1.

### 11.6.2 Odds Ratio (OR)

**Odds Ratio (OR)** membandingkan odds antara dua kelompok:

```
         Odds kelompok 1     a / b     a x d
OR  =  ──────────────────  = ───── = ─────────
         Odds kelompok 2     c / d     b x c

Di mana (untuk tabel 2x2):
┌─────────────┬──────────┬──────────┐
│             │ Event    │ No Event │
├─────────────┼──────────┼──────────┤
│ Kelompok 1  │    a     │    b     │
│ Kelompok 2  │    c     │    d     │
└─────────────┴──────────┴──────────┘
```

**Interpretasi OR:**

| Nilai OR | Interpretasi |
|----------|-------------|
| OR = 1 | Tidak ada perbedaan odds antara kedua kelompok |
| OR > 1 | Kelompok 1 memiliki odds lebih tinggi mengalami event |
| OR < 1 | Kelompok 1 memiliki odds lebih rendah mengalami event |

### 11.6.3 Relative Risk (RR)

**Relative Risk (RR)** atau **risiko relatif** membandingkan **probabilitas** (bukan odds) antara dua kelompok:

```
         P(event | kelompok 1)     a / (a + b)
RR  =  ──────────────────────── = ─────────────
         P(event | kelompok 2)     c / (c + d)
```

### 11.6.4 Perbandingan OR dan RR

| Aspek | Odds Ratio (OR) | Relative Risk (RR) |
|-------|-----------------|-------------------|
| Mengukur | Rasio **odds** | Rasio **probabilitas** |
| Kapan digunakan | Case-control studies, logistic regression | Cohort studies, RCT |
| Interpretasi | Kurang intuitif | Lebih intuitif |
| Nilai saat event langka | Mendekati RR | (sama) |
| Digunakan dalam | Logistic regression koefisien | Epidemiologi klinis |

> **Tips untuk mahasiswa:** OR lebih penting untuk dipahami karena merupakan output utama dari logistic regression. Setiap kali membaca OR, ingat: **OR berbicara tentang odds, bukan probabilitas**.

### 11.6.5 Implementasi Python: Odds Ratio dan Relative Risk

```python
# ============================================================
# ODDS RATIO DAN RELATIVE RISK
# ============================================================

# Studi kasus: Apakah mahasiswa yang menggunakan AI tool lebih
# mungkin lulus mata kuliah Statistika?
#
# Data (fiktif):
#   - Menggunakan AI: 80 lulus, 20 tidak lulus
#   - Tidak menggunakan AI: 60 lulus, 40 tidak lulus

a, b = 80, 20   # AI: lulus, tidak lulus
c, d = 60, 40   # Non-AI: lulus, tidak lulus

print("=== Tabel 2x2: Penggunaan AI vs Kelulusan ===")
print(f"               Lulus   Tidak Lulus   Total")
print(f"  Pakai AI      {a:3d}      {b:3d}         {a+b}")
print(f"  Tanpa AI      {c:3d}      {d:3d}         {c+d}")
print(f"  Total         {a+c:3d}      {b+d:3d}         {a+b+c+d}")

# Hitung Odds
odds_ai = a / b
odds_non_ai = c / d
print(f"\n=== Perhitungan Odds ===")
print(f"Odds lulus (pakai AI)    = {a}/{b} = {odds_ai:.3f}")
print(f"Odds lulus (tanpa AI)    = {c}/{d} = {odds_non_ai:.3f}")

# Odds Ratio
OR = odds_ai / odds_non_ai
print(f"\n=== Odds Ratio ===")
print(f"OR = {odds_ai:.3f} / {odds_non_ai:.3f} = {OR:.3f}")
print(f"Interpretasi: Odds kelulusan mahasiswa yang menggunakan AI")
print(f"  adalah {OR:.1f} kali odds mahasiswa yang tidak menggunakan AI.")

# Relative Risk
prob_ai = a / (a + b)
prob_non_ai = c / (c + d)
RR = prob_ai / prob_non_ai
print(f"\n=== Relative Risk ===")
print(f"P(lulus | AI)    = {a}/{a+b} = {prob_ai:.3f}")
print(f"P(lulus | no AI) = {c}/{c+d} = {prob_non_ai:.3f}")
print(f"RR = {prob_ai:.3f} / {prob_non_ai:.3f} = {RR:.3f}")
print(f"Interpretasi: Mahasiswa yang menggunakan AI memiliki probabilitas")
print(f"  kelulusan {RR:.2f} kali dibandingkan yang tidak menggunakan AI.")

# Perbandingan
print(f"\n=== Perbandingan OR vs RR ===")
print(f"  OR = {OR:.3f}")
print(f"  RR = {RR:.3f}")
print(f"  OR > RR karena event (lulus) cukup umum (bukan langka).")
print(f"  Jika event langka, OR akan mendekati RR.")
```

---

## 11.7 Pengantar Logistic Regression

### 11.7.1 Dari Linear ke Logistic

Pada bab sebelumnya (Bab 8-9), kita mempelajari **linear regression** untuk variabel dependen numerik (kontinu). Bagaimana jika variabel dependen kita **biner** — yaitu hanya memiliki dua kemungkinan nilai (ya/tidak, lulus/gagal, klik/tidak klik, beli/tidak beli)?

**Masalah jika memaksakan linear regression untuk outcome biner:**
1. Prediksi bisa < 0 atau > 1 (tidak masuk akal untuk probabilitas)
2. Asumsi residual normal dilanggar
3. Hubungannya biasanya non-linear

```
MASALAH LINEAR REGRESSION UNTUK OUTCOME BINER
═══════════════════════════════════════════════

Y (0/1)
  1 ─ ─ ─ ─ ● ─ ─ ● ─ ─ ─ ● ─ ─ ─ ● ● ● ● ● ●
            ●       ●   ●
       ●         ●     ●         Garis regresi
  0 ● ● ● ● ● ─ ─ ─ ─ ─ ─ ─ ─ ─/─ ─ ─ ─ ─ ─ ─ ─
    ● ●    ●              /
                       /          ← Prediksi bisa > 1
              ─ ─ ─/─ ─ ─ ─ ─ ─     atau < 0!
              /
    ──┬──┬──┬──┬──┬──┬──┬──┬──┬──→ X (IPK)
      2.0       3.0       4.0


SOLUSI: LOGISTIC REGRESSION (SIGMOID)
═══════════════════════════════════════

P(Y=1)
  1.0 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ● ● ● ● ●═══
                              ● ●/
                           ●  /
  0.5 ─ ─ ─ ─ ─ ─ ─ ─ ─●/ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
                       /●
                    / ●
  0.0 ═══● ● ● ●/─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
    ──┬──┬──┬──┬──┬──┬──┬──┬──┬──→ X (IPK)
      2.0       3.0       4.0

    Output selalu antara 0 dan 1 → interpretasi sebagai probabilitas!
```

### 11.7.2 Fungsi Sigmoid (Logistic Function)

Logistic regression menggunakan fungsi **sigmoid** untuk memastikan output selalu antara 0 dan 1:

```
                  1
P(Y = 1) = ──────────────
            1 + e^(-z)

di mana z = b0 + b1*x1 + b2*x2 + ... + bk*xk
```

**Sifat fungsi sigmoid:**
- z = 0 maka P = 0.5 (titik tengah, decision boundary)
- z sangat besar (positif) maka P mendekati 1
- z sangat kecil (negatif) maka P mendekati 0
- Kurva berbentuk S (sigmoid = "berbentuk S")

### 11.7.3 Interpretasi Koefisien melalui Odds Ratio

Dalam logistic regression, koefisien **tidak** diinterpretasi langsung seperti linear regression. Kita menggunakan **odds ratio** dari eksponensial koefisien:

```
OR_i = e^(b_i)
```

**Interpretasi:** "Setiap kenaikan 1 unit x_i, **odds** dari Y=1 berubah sebesar faktor e^(b_i), dengan asumsi variabel lain tetap (ceteris paribus)."

**Contoh:**
- Jika b_IPK = 1.2, maka OR = e^1.2 = 3.32
- "Setiap kenaikan 1 poin IPK, odds kelulusan meningkat **3.32 kali lipat**."
- Jika b_jam = 0.3, maka OR = e^0.3 = 1.35
- "Setiap tambahan 1 jam belajar, odds kelulusan meningkat **35%**."

### 11.7.4 Kapan Chi-Square vs Logistic Regression?

| Aspek | Chi-Square Test | Logistic Regression |
|-------|----------------|-------------------|
| **Tujuan** | Menguji hubungan 2 variabel kategorikal | Memprediksi outcome biner dari satu/banyak prediktor |
| **Variabel** | Kedua variabel kategorikal | Dependen biner, independen bisa numerik/kategorikal |
| **Output** | p-value (ada/tidak hubungan) | Koefisien, odds ratio, prediksi probabilitas |
| **Kekuatan** | Sederhana, cepat, mudah dipahami | Bisa mengontrol banyak variabel, prediktif |
| **Kelemahan** | Tidak bisa mengontrol confounders | Lebih kompleks, butuh sampel lebih besar |
| **Kapan pakai** | Eksplorasi awal hubungan | Analisis mendalam dan prediksi |

**Aturan praktis:**
- Ingin tahu "apakah ada hubungan?" → gunakan **Chi-square**
- Ingin "memprediksi" atau "mengontrol variabel lain" → gunakan **Logistic regression**
- **Idealnya:** gunakan keduanya — chi-square untuk eksplorasi, logistic regression untuk pemodelan

---

## 11.8 Implementasi Logistic Regression dengan Python

### 11.8.1 Menyiapkan Data

```python
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Simulasi data: prediksi kepuasan mahasiswa terhadap e-commerce
np.random.seed(2025)
n = 200

ipk = np.random.normal(3.2, 0.4, n).clip(2.0, 4.0).round(2)
jam_belanja_online = np.random.uniform(1, 10, n).round(1)
frekuensi_komplain = np.random.poisson(2, n)

# Outcome biner: puas (1) vs tidak puas (0) terhadap layanan e-commerce
z = -4 + 0.8 * ipk + 0.15 * jam_belanja_online - 0.4 * frekuensi_komplain
z += np.random.normal(0, 0.5, n)
prob_puas = 1 / (1 + np.exp(-z))
puas = (np.random.random(n) < prob_puas).astype(int)

data_ecommerce = pd.DataFrame({
    'ipk': ipk,
    'jam_belanja_online': jam_belanja_online,
    'frekuensi_komplain': frekuensi_komplain,
    'puas': puas
})

print("=== Preview Data ===")
print(data_ecommerce.head(10))
print(f"\nDistribusi kepuasan:")
print(f"  Puas (1): {puas.sum()} ({puas.mean()*100:.1f}%)")
print(f"  Tidak Puas (0): {(1-puas).sum()} ({(1-puas.mean())*100:.1f}%)")
```

### 11.8.2 Logistic Regression dengan scikit-learn

```python
# ============================================================
# LOGISTIC REGRESSION DENGAN SCIKIT-LEARN
# ============================================================

X = data_ecommerce[['ipk', 'jam_belanja_online', 'frekuensi_komplain']]
y = data_ecommerce['puas']

# Fit model
log_model = LogisticRegression(random_state=42)
log_model.fit(X, y)

print("=== Logistic Regression (sklearn) ===")
print(f"Intercept (b0): {log_model.intercept_[0]:.4f}")
print(f"\nKoefisien dan Odds Ratio:")
print(f"  {'Variabel':<25} {'Beta':<10} {'OR (e^beta)':<12}")
print(f"  {'-'*47}")
for nama, koef in zip(X.columns, log_model.coef_[0]):
    or_val = np.exp(koef)
    print(f"  {nama:<25} {koef:<10.4f} {or_val:<12.4f}")

# Prediksi dan evaluasi
y_pred = log_model.predict(X)
print(f"\n=== Evaluasi Model ===")
print(f"Akurasi: {log_model.score(X, y):.4f}")
print(f"\nConfusion Matrix:")
cm = confusion_matrix(y, y_pred)
print(f"  Prediksi →       Tidak Puas   Puas")
print(f"  Aktual Tidak Puas   {cm[0,0]:5d}      {cm[0,1]:5d}")
print(f"  Aktual Puas         {cm[1,0]:5d}      {cm[1,1]:5d}")
```

### 11.8.3 Logistic Regression dengan statsmodels (Output Lengkap)

```python
# ============================================================
# LOGISTIC REGRESSION DENGAN STATSMODELS (untuk p-value dan CI)
# ============================================================

X_sm = sm.add_constant(data_ecommerce[['ipk', 'jam_belanja_online',
                                        'frekuensi_komplain']])
y_sm = data_ecommerce['puas']

logit_model = sm.Logit(y_sm, X_sm).fit()
print(logit_model.summary())

# Odds Ratio dengan confidence interval
print("\n=== Odds Ratio dengan 95% Confidence Interval ===")
params = logit_model.params
conf = logit_model.conf_int()
or_table = pd.DataFrame({
    'OR': np.exp(params),
    'CI_Lower': np.exp(conf[0]),
    'CI_Upper': np.exp(conf[1]),
    'p_value': logit_model.pvalues
})
print(or_table.round(4))

print("\n=== Interpretasi ===")
for var in ['ipk', 'jam_belanja_online', 'frekuensi_komplain']:
    or_val = np.exp(params[var])
    p_val = logit_model.pvalues[var]
    sig = "signifikan" if p_val < 0.05 else "tidak signifikan"
    if or_val > 1:
        print(f"  {var}: OR = {or_val:.2f} (p = {p_val:.4f}, {sig})")
        print(f"    -> Setiap kenaikan 1 unit, odds kepuasan meningkat "
              f"{(or_val-1)*100:.1f}%.")
    else:
        print(f"  {var}: OR = {or_val:.2f} (p = {p_val:.4f}, {sig})")
        print(f"    -> Setiap kenaikan 1 unit, odds kepuasan menurun "
              f"{(1-or_val)*100:.1f}%.")
```

### 11.8.4 Visualisasi Logistic Regression

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Fungsi sigmoid
z_range = np.linspace(-6, 6, 200)
sigmoid = 1 / (1 + np.exp(-z_range))

axes[0].plot(z_range, sigmoid, 'b-', linewidth=2)
axes[0].axhline(y=0.5, color='red', linestyle='--', alpha=0.5, label='P = 0.5')
axes[0].axvline(x=0, color='gray', linestyle='--', alpha=0.3)
axes[0].set_xlabel('z = b0 + b1*x1 + b2*x2 + ...', fontsize=11)
axes[0].set_ylabel('P(Y = 1)', fontsize=11)
axes[0].set_title('Fungsi Sigmoid (Logistic Function)', fontsize=13)
axes[0].legend(fontsize=10)
axes[0].grid(True, alpha=0.3)
axes[0].set_ylim(-0.05, 1.05)

# Plot 2: Scatter plot IPK vs Kepuasan + probability curve
ipk_sorted = np.sort(data_ecommerce['ipk'].values)
ipk_pred = np.column_stack([
    ipk_sorted,
    np.full(len(ipk_sorted), data_ecommerce['jam_belanja_online'].mean()),
    np.full(len(ipk_sorted), data_ecommerce['frekuensi_komplain'].mean())
])
prob_pred = log_model.predict_proba(ipk_pred)[:, 1]

axes[1].scatter(data_ecommerce['ipk'], data_ecommerce['puas'],
                alpha=0.3, color='steelblue', label='Data observasi')
axes[1].plot(ipk_sorted, prob_pred, 'r-', linewidth=2,
             label='P(Puas) predicted')
axes[1].axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
axes[1].set_xlabel('IPK', fontsize=11)
axes[1].set_ylabel('Kepuasan (0/1) atau P(Puas)', fontsize=11)
axes[1].set_title('Logistic Regression: IPK vs Kepuasan\n'
                  '(variabel lain = rata-rata)', fontsize=13)
axes[1].legend(fontsize=10)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## 11.9 Studi Kasus: Analisis Preferensi Platform E-Commerce Indonesia

### 11.9.1 Konteks

Sebuah tim riset dari Universitas Al Azhar Indonesia melakukan survei terhadap 300 mahasiswa dari berbagai fakultas untuk mengetahui: (1) Apakah preferensi platform e-commerce berbeda berdasarkan gender? (2) Faktor apa yang mempengaruhi kepuasan mahasiswa terhadap layanan e-commerce?

### 11.9.2 Analisis Lengkap

```python
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# STUDI KASUS: Survei Preferensi Platform E-Commerce
# ============================================================

np.random.seed(2025)
n = 300

# Generate data survei
gender = np.random.choice(['Laki-laki', 'Perempuan'], n, p=[0.45, 0.55])
usia = np.random.choice(['18-20', '21-23', '24+'], n, p=[0.40, 0.45, 0.15])

platform = []
for g in gender:
    if g == 'Laki-laki':
        p = np.random.choice(
            ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak'],
            p=[0.30, 0.40, 0.18, 0.12]
        )
    else:
        p = np.random.choice(
            ['Shopee', 'Tokopedia', 'Lazada', 'Bukalapak'],
            p=[0.52, 0.22, 0.15, 0.11]
        )
    platform.append(p)

# Variabel tambahan untuk logistic regression
frekuensi_belanja = np.random.poisson(4, n)  # kali per bulan
rating_layanan = np.random.uniform(1, 5, n).round(1)

# Outcome biner: puas (1) vs tidak puas (0)
z = -3 + 0.5 * rating_layanan + 0.2 * frekuensi_belanja
z += np.random.normal(0, 0.8, n)
prob = 1 / (1 + np.exp(-z))
puas = (np.random.random(n) < prob).astype(int)

data_survei = pd.DataFrame({
    'gender': gender,
    'usia': usia,
    'platform': platform,
    'frekuensi_belanja': frekuensi_belanja,
    'rating_layanan': rating_layanan,
    'puas': puas
})

print("=" * 60)
print("STUDI KASUS: Preferensi Platform E-Commerce Mahasiswa")
print("=" * 60)
print(f"\nJumlah responden: {n}")
print(f"\nDistribusi variabel:")
for col in ['gender', 'usia', 'platform']:
    print(f"\n  {col}:")
    for val, cnt in data_survei[col].value_counts().items():
        print(f"    {val}: {cnt} ({cnt/n*100:.1f}%)")

# ─────────────────────────────────────────────────────
# BAGIAN A: Chi-Square — Gender vs Platform
# ─────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("BAGIAN A: Hubungan Gender dan Preferensi Platform")
print("=" * 60)

# A1. Contingency table
ct = pd.crosstab(data_survei['gender'], data_survei['platform'], margins=True)
print(f"\n1. Tabel Kontingensi:")
print(ct)

ct_pct = pd.crosstab(data_survei['gender'], data_survei['platform'],
                      normalize='index')
print(f"\n   Proporsi per Gender:")
print(ct_pct.round(3))

# A2. Chi-square test
ct_test = pd.crosstab(data_survei['gender'], data_survei['platform'])
chi2, p, dof, exp = stats.chi2_contingency(ct_test)

print(f"\n2. Chi-Square Test of Independence:")
print(f"   chi2 = {chi2:.4f}, df = {dof}, p = {p:.6f}")
print(f"   Min expected frequency = {exp.min():.1f}")

if p < 0.05:
    print(f"   Keputusan: TOLAK H0 — ada hubungan signifikan.")
else:
    print(f"   Keputusan: Gagal tolak H0 — tidak ada hubungan signifikan.")

# A3. Cramer's V
v = np.sqrt(chi2 / (n * (min(ct_test.shape) - 1)))
print(f"\n3. Effect Size (Cramer's V): {v:.4f}")

# ─────────────────────────────────────────────────────
# BAGIAN B: Logistic Regression — Prediksi Kepuasan
# ─────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("BAGIAN B: Faktor yang Mempengaruhi Kepuasan E-Commerce")
print("=" * 60)

# B1. Deskriptif
print(f"\n1. Distribusi kepuasan:")
print(f"   Puas (1): {data_survei['puas'].sum()} "
      f"({data_survei['puas'].mean()*100:.1f}%)")
print(f"   Tidak Puas (0): {(1-data_survei['puas']).sum()} "
      f"({(1-data_survei['puas'].mean())*100:.1f}%)")

# B2. Logistic regression dengan statsmodels
X_case = sm.add_constant(data_survei[['rating_layanan', 'frekuensi_belanja']])
logit_case = sm.Logit(data_survei['puas'], X_case).fit(disp=0)

print(f"\n2. Model Logistic Regression:")
print(f"   Log-Likelihood: {logit_case.llf:.2f}")
print(f"   Pseudo R-squared: {logit_case.prsquared:.4f}")
print(f"   AIC: {logit_case.aic:.2f}")

print(f"\n3. Koefisien dan Odds Ratio:")
print(f"   {'Variabel':<22} {'Beta':<10} {'OR':<10} {'p-value':<10} {'Sig?'}")
print(f"   {'-'*52}")
for var in X_case.columns:
    beta = logit_case.params[var]
    or_val = np.exp(beta)
    pval = logit_case.pvalues[var]
    sig = ("Ya ***" if pval < 0.001 else "Ya **" if pval < 0.01
           else "Ya *" if pval < 0.05 else "Tidak")
    print(f"   {var:<22} {beta:<10.4f} {or_val:<10.4f} {pval:<10.4f} {sig}")

# B3. Prediksi contoh
print(f"\n4. Prediksi Contoh:")
contoh = pd.DataFrame({
    'const': [1, 1, 1],
    'rating_layanan': [2.0, 3.5, 4.5],
    'frekuensi_belanja': [1, 4, 8]
})
for _, row in contoh.iterrows():
    prob = logit_case.predict(row)[0]
    label = "Kemungkinan Puas" if prob > 0.5 else "Kemungkinan Tidak Puas"
    print(f"   Rating {row['rating_layanan']}, Belanja {int(row['frekuensi_belanja'])}x/bln"
          f" -> P(Puas) = {prob:.3f} ({label})")

# Kesimpulan
print(f"\n{'='*60}")
print("KESIMPULAN STUDI KASUS:")
print(f"{'='*60}")
print("1. Analisis chi-square menunjukkan bahwa preferensi platform")
if p < 0.05:
    print(f"   e-commerce berhubungan dengan gender (p = {p:.4f}, V = {v:.3f}).")
    print("   Perempuan cenderung lebih memilih Shopee, sementara laki-laki")
    print("   lebih merata ke Tokopedia dan platform lainnya.")
else:
    print(f"   e-commerce tidak berhubungan signifikan dengan gender (p = {p:.4f}).")
print("2. Model logistic regression menunjukkan bahwa rating layanan")
print("   dan frekuensi belanja berpengaruh terhadap kepuasan.")
print("3. Implikasi: platform e-commerce perlu mempertahankan kualitas")
print("   layanan untuk meningkatkan kepuasan pengguna.")
```

### 11.9.3 Studi Kasus 2: Survei Kepuasan Pelanggan

```python
# ============================================================
# STUDI KASUS 2: Survei Kepuasan Pelanggan berdasarkan Fakultas
# ============================================================

np.random.seed(2024)
n2 = 300

fakultas = np.random.choice(
    ['Teknik', 'Ekonomi', 'Hukum', 'FKIP', 'Sains'],
    size=n2, p=[0.25, 0.25, 0.20, 0.15, 0.15]
)

# Kepuasan dipengaruhi oleh fakultas
kepuasan = []
for f in fakultas:
    if f == 'Teknik':
        k = np.random.choice(['Puas', 'Netral', 'Tidak Puas'], p=[0.5, 0.3, 0.2])
    elif f == 'Ekonomi':
        k = np.random.choice(['Puas', 'Netral', 'Tidak Puas'], p=[0.6, 0.25, 0.15])
    elif f == 'Hukum':
        k = np.random.choice(['Puas', 'Netral', 'Tidak Puas'], p=[0.35, 0.35, 0.3])
    elif f == 'FKIP':
        k = np.random.choice(['Puas', 'Netral', 'Tidak Puas'], p=[0.45, 0.30, 0.25])
    else:
        k = np.random.choice(['Puas', 'Netral', 'Tidak Puas'], p=[0.55, 0.25, 0.20])
    kepuasan.append(k)

data_kepuasan = pd.DataFrame({'fakultas': fakultas, 'kepuasan': kepuasan})

# Chi-square test
ct_kep = pd.crosstab(data_kepuasan['fakultas'], data_kepuasan['kepuasan'])
chi2_kep, p_kep, dof_kep, exp_kep = stats.chi2_contingency(ct_kep)

print("=== Chi-Square: Fakultas vs Kepuasan Layanan Kampus ===")
print(f"\nTabel Kontingensi:")
print(pd.crosstab(data_kepuasan['fakultas'], data_kepuasan['kepuasan'],
                   margins=True))
print(f"\nChi2 = {chi2_kep:.4f}, df = {dof_kep}, p-value = {p_kep:.4f}")
print(f"Min expected freq = {exp_kep.min():.1f}")

if p_kep < 0.05:
    print("Kesimpulan: Ada hubungan signifikan antara fakultas dan kepuasan.")
else:
    print("Kesimpulan: Tidak ada hubungan signifikan antara fakultas dan kepuasan.")

# Visualisasi
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

tabel_persen = pd.crosstab(data_kepuasan['fakultas'],
                            data_kepuasan['kepuasan'], normalize='index') * 100
tabel_persen.plot(kind='bar', stacked=True, ax=axes[0],
                  color=['#27ae60', '#f39c12', '#e74c3c'])
axes[0].set_title('Kepuasan per Fakultas (%)', fontsize=13)
axes[0].set_xlabel('Fakultas')
axes[0].set_ylabel('Persentase')
axes[0].legend(title='Kepuasan')
axes[0].tick_params(axis='x', rotation=45)

sns.heatmap(ct_kep, annot=True, fmt='d', cmap='YlOrRd', ax=axes[1])
axes[1].set_title('Heatmap: Fakultas vs Kepuasan', fontsize=13)

plt.tight_layout()
plt.show()
```

---

## 11.10 AI Corner: Menggunakan AI untuk Analisis Data Kategorikal

### 11.10.1 Apa yang Bisa AI Bantu?

| AI Bisa Membantu | AI Tidak Bisa Menggantikan |
|-------------------|---------------------------|
| Generate kode chi-square test dan logistic regression | Memahami konteks bisnis/domain survei |
| Menjelaskan perbedaan odds ratio vs relative risk | Memutuskan apakah hasil masuk akal secara praktis |
| Menyarankan visualisasi yang tepat untuk data kategorikal | Menjamin bahwa asumsi statistik terpenuhi |
| Menginterpretasi output statsmodels secara teknis | Menentukan implikasi kebijakan dari hasil |
| Membantu debugging kode analisis | Menggantikan pemikiran kritis tentang data |

### 11.10.2 Contoh Prompt yang Efektif

**Prompt yang Baik:**

```
Saya punya data survei 300 mahasiswa dengan variabel:
- gender (Laki-laki / Perempuan)
- platform e-commerce favorit (Shopee / Tokopedia / Lazada / Bukalapak)

Saya sudah membuat contingency table dan ingin menguji apakah ada
hubungan antara gender dan preferensi platform.

1. Tuliskan kode Python untuk chi-square test of independence
2. Bagaimana cara mengecek apakah syarat expected frequency >= 5 terpenuhi?
3. Jika signifikan, bagaimana mengukur effect size-nya?
```

**Prompt yang Kurang Baik:**

```
Analisis data survei saya.
```

### 11.10.3 Kapan Harus Kritis terhadap AI

1. **Odds vs Probabilitas:** AI sering mencampuradukkan odds dan probabilitas. Jika AI mengatakan "OR = 2.5 berarti 2.5 kali lebih mungkin" — ini kurang tepat. Yang benar: "**Odds**-nya 2.5 kali lebih tinggi." Odds bukan probabilitas.

2. **Syarat chi-square:** AI mungkin tidak mengingatkan bahwa expected frequency harus >= 5. Selalu cek sendiri.

3. **Konteks Indonesia:** Pola penggunaan e-commerce, metode pembayaran, dan perilaku belanja online di Indonesia memiliki karakteristik unik yang mungkin tidak dipahami AI secara mendalam.

4. **Kausalitas:** Chi-square hanya menunjukkan **asosiasi** (hubungan), bukan **kausalitas** (sebab-akibat). AI mungkin menggunakan bahasa kausal yang tidak tepat.

### 11.10.4 Template Evaluasi Output AI

Sebelum menerima output AI, jawab pertanyaan berikut:

```
CHECKLIST EVALUASI OUTPUT AI UNTUK ANALISIS KATEGORIKAL
═══════════════════════════════════════════════════════════
[ ] Apakah AI menggunakan uji yang tepat untuk jenis data saya?
[ ] Apakah syarat expected frequency >= 5 sudah dicek?
[ ] Apakah interpretasi OR menggunakan kata "odds" (bukan "probabilitas")?
[ ] Apakah AI menyebutkan bahwa ini asosiasi, bukan kausalitas?
[ ] Apakah kode Python bisa berjalan tanpa error?
[ ] Apakah konteks Indonesia sudah dipertimbangkan?
[ ] Apakah saya sudah memverifikasi perhitungan secara manual?
```

---

## Rangkuman Bab 11

1. **Data kategorikal** adalah variabel yang nilainya berupa kategori atau label. Analisis data kategorikal menggunakan **frekuensi dan proporsi**, bukan rata-rata. Contingency table (tabel kontingensi) adalah langkah pertama untuk mengeksplorasi hubungan dua variabel kategorikal.

2. **Chi-square test of independence** menguji apakah dua variabel kategorikal berhubungan atau independen. Statistik uji dihitung dari perbedaan antara frekuensi observasi (O) dan frekuensi harapan (E) dengan rumus chi2 = SUM (O-E)^2/E, dan derajat kebebasan df = (r-1)(c-1).

3. **Chi-square goodness of fit test** menguji apakah distribusi satu variabel kategorikal sesuai dengan distribusi teoritis yang diharapkan, misalnya menguji apakah distribusi pengguna merata di antara beberapa platform.

4. **Fisher's exact test** adalah alternatif chi-square untuk tabel 2x2 ketika expected frequency < 5 (sampel kecil). Fisher's exact test menghitung probabilitas eksak tanpa menggunakan pendekatan distribusi chi-square.

5. **Odds ratio (OR)** membandingkan odds antara dua kelompok, sedangkan **relative risk (RR)** membandingkan probabilitas. OR digunakan dalam logistic regression dan case-control studies; RR lebih intuitif dan digunakan dalam cohort studies. Ketika event langka, OR mendekati RR.

6. **Logistic regression** digunakan untuk memprediksi outcome biner (0/1) menggunakan fungsi sigmoid yang memastikan output selalu antara 0 dan 1. Koefisien diinterpretasi melalui odds ratio (OR = e^b), yang menyatakan perubahan odds untuk setiap kenaikan satu unit prediktor.

7. **Chi-square vs logistic regression:** Chi-square cocok untuk eksplorasi hubungan dua variabel kategorikal, sedangkan logistic regression cocok untuk pemodelan prediktif dengan banyak variabel dan kontrol terhadap confounders.

8. Dalam implementasi Python, gunakan `scipy.stats.chi2_contingency` untuk chi-square test, `scipy.stats.fisher_exact` untuk Fisher's exact test, `sklearn.linear_model.LogisticRegression` untuk prediksi, dan `statsmodels.api.Logit` untuk output statistik lengkap (p-value, confidence interval).

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan antara data kategorikal dan data numerik. Berikan masing-masing tiga contoh variabel dalam konteks e-commerce Indonesia.

**Soal 2.** Perhatikan contingency table berikut dari survei 200 mahasiswa:

|  | Shopee | Tokopedia | Lazada | Total |
|--|:---:|:---:|:---:|:---:|
| **Laki-laki** | 30 | 40 | 20 | **90** |
| **Perempuan** | 55 | 25 | 30 | **110** |
| **Total** | **85** | **65** | **50** | **200** |

- a) Berapa proporsi perempuan yang memilih Shopee?
- b) Berapa proporsi pengguna Tokopedia yang laki-laki?
- c) Jika gender dan platform independen, berapa expected frequency untuk sel "Laki-laki, Shopee"?

**Soal 3.** Sebutkan empat syarat penggunaan chi-square test of independence. Apa yang harus dilakukan jika salah satu syarat tidak terpenuhi?

**Soal 4.** Jelaskan perbedaan antara chi-square test of independence dan chi-square goodness of fit test. Berikan contoh pertanyaan penelitian untuk masing-masing.

### Tingkat Menengah (C2-C3)

**Soal 5.** Dari tabel pada Soal 2:
- a) Hitung expected frequency untuk **setiap sel** dalam tabel.
- b) Hitung derajat kebebasan (df).
- c) Hitung statistik chi-square secara manual.
- d) Verifikasi jawaban Anda menggunakan `scipy.stats.chi2_contingency`.

**Soal 6.** Sebuah startup fintech melakukan survei terhadap 300 pengguna tentang metode pembayaran favorit:

|  | Transfer Bank | E-Wallet | COD | Total |
|--|:---:|:---:|:---:|:---:|
| **Gen Z (18-25)** | 25 | 80 | 15 | **120** |
| **Milenial (26-35)** | 45 | 55 | 20 | **120** |
| **Gen X (36-50)** | 40 | 10 | 10 | **60** |
| **Total** | **110** | **145** | **45** | **300** |

- a) Lakukan chi-square test of independence menggunakan Python.
- b) Cek apakah syarat expected frequency >= 5 terpenuhi.
- c) Hitung Cramer's V dan interpretasikan.
- d) Buat visualisasi stacked bar chart.
- e) Tulis kesimpulan dalam 2-3 kalimat.

**Soal 7.** Dari data berikut tentang penggunaan AI tool dan keberhasilan proyek akhir:

|  | Berhasil | Gagal | Total |
|--|:---:|:---:|:---:|
| **Pakai AI** | 75 | 25 | **100** |
| **Tanpa AI** | 50 | 50 | **100** |
| **Total** | **125** | **75** | **200** |

- a) Hitung odds keberhasilan untuk kelompok yang menggunakan AI.
- b) Hitung odds keberhasilan untuk kelompok yang tidak menggunakan AI.
- c) Hitung Odds Ratio dan interpretasikan.
- d) Hitung Relative Risk dan bandingkan dengan OR.
- e) Mengapa OR dan RR berbeda nilainya? Kapan keduanya akan mendekati?

**Soal 8.** Tulis kode Python yang melakukan hal berikut:
- a) Membuat contingency table dari data survei menggunakan `pd.crosstab`.
- b) Menampilkan tabel dalam bentuk frekuensi dan persentase per baris.
- c) Melakukan chi-square test dan menampilkan chi2, df, dan p-value.
- d) Membuat heatmap dari contingency table menggunakan seaborn.

### Tingkat Mahir (C3-C4+)

**Soal 9.** Sebuah perusahaan e-commerce ingin mengetahui faktor yang mempengaruhi apakah pengguna akan melakukan pembelian ulang (repeat purchase). Data yang tersedia:
- `repeat_purchase`: 1 (ya) / 0 (tidak) — variabel dependen
- `rating_layanan`: skala 1.0-5.0
- `waktu_pengiriman_hari`: 1-14 hari
- `jumlah_komplain`: 0-5 kali

Tulis kode Python yang:
- a) Membuat data simulasi (n=500) dengan hubungan logistik yang masuk akal.
- b) Membangun model logistic regression menggunakan sklearn dan statsmodels.
- c) Menghitung odds ratio untuk setiap prediktor dan interpretasikan.
- d) Membuat prediksi untuk 3 skenario pengguna yang berbeda.
- e) Visualisasikan fungsi sigmoid dan kurva probabilitas untuk salah satu prediktor.

**Soal 10.** Sebuah rumah sakit ingin mengetahui apakah ada hubungan antara golongan darah (A, B, AB, O) dan kerentanan terhadap suatu penyakit. Dari 80 pasien:

|  | Sakit | Tidak Sakit | Total |
|--|:---:|:---:|:---:|
| **A** | 12 | 8 | **20** |
| **B** | 8 | 12 | **20** |
| **AB** | 3 | 7 | **10** |
| **O** | 7 | 23 | **30** |
| **Total** | **30** | **50** | **80** |

- a) Lakukan chi-square test. Apakah ada sel dengan expected frequency < 5?
- b) Jika ada, lakukan langkah perbaikan yang sesuai (misalnya menggabungkan kategori).
- c) Bandingkan hasil sebelum dan sesudah perbaikan.
- d) Untuk golongan darah A vs O, hitung odds ratio kerentanan penyakit.

**Soal 11.** Sebuah platform e-learning ingin memprediksi apakah mahasiswa akan menyelesaikan kursus online (1) atau tidak (0). Faktor yang tersedia: jumlah login per minggu, durasi menonton video (jam), jumlah tugas yang dikumpulkan, dan forum post.

- a) Jelaskan mengapa logistic regression lebih tepat daripada linear regression untuk masalah ini.
- b) Bangun model logistic regression menggunakan data simulasi.
- c) Variabel mana yang paling berpengaruh? Gunakan odds ratio untuk menjelaskan.
- d) Jika seorang mahasiswa login 5 kali/minggu, menonton 8 jam video, mengumpulkan 3 tugas, dan membuat 2 forum post, berapa probabilitas dia menyelesaikan kursus?

**Soal 12.** Lakukan analisis kategorikal lengkap untuk skenario berikut:

Sebuah survei terhadap 400 pengguna transportasi online di Jakarta mencatat:
- Jenis transportasi: GrabBike / GoRide / Maxim / Konvensional
- Wilayah: Jakarta Pusat / Jakarta Selatan / Jakarta Timur / Jakarta Barat / Jakarta Utara
- Kepuasan: Puas (1) / Tidak Puas (0)

Lakukan:
1. Buat data simulasi yang realistis.
2. Contingency table + visualisasi (stacked bar chart dan heatmap).
3. Chi-square test of independence: jenis transportasi vs wilayah.
4. Odds ratio: GrabBike vs GoRide untuk kepuasan.
5. Logistic regression: prediksi kepuasan berdasarkan variabel yang tersedia.
6. Tulis laporan singkat (5-8 kalimat) yang merangkum temuan Anda.

---

## Referensi

1. Agresti, A. (2018). *An Introduction to Categorical Data Analysis* (3rd ed.). Wiley. Chapters 1-3.
2. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics* (4th ed.). Chapter 6: Inference for Categorical Data.
3. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning with Applications in Python (ISLP)*. Chapter 4: Classification (Logistic Regression).
4. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability & Statistics for Engineers & Scientists* (9th ed.). Pearson.
5. Moore, D. S., McCabe, G. P., & Craig, B. A. (2021). *Introduction to the Practice of Statistics* (10th ed.). W. H. Freeman.
6. SciPy Documentation. `chi2_contingency`: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html
7. SciPy Documentation. `fisher_exact`: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisher_exact.html
8. scikit-learn Documentation. `LogisticRegression`: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
9. statsmodels Documentation. `Logit`: https://www.statsmodels.org/stable/generated/statsmodels.discrete.discrete_model.Logit.html
10. APJII. (2024). *Profil Internet Indonesia 2024*. Asosiasi Penyelenggara Jasa Internet Indonesia.

---

*Bab berikutnya: **Bab 12 — Pengantar Machine Learning dan Supervised Learning***
