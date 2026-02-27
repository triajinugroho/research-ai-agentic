# BAB 2: STATISTIKA DESKRIPTIF DAN EKSPLORASI DATA DENGAN PYTHON

**Tri Aji Nugroho, S.T., M.T.**
Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-2.1 | Menghitung ukuran pemusatan data (mean, median, modus) secara manual dan dengan Python | C3 |
| CPMK-2.2 | Menghitung ukuran penyebaran data (range, variance, standard deviation, IQR) secara manual dan dengan Python | C3 |
| CPMK-2.3 | Menghitung dan menginterpretasikan ukuran posisi data (quartiles, percentiles) serta five-number summary | C3 |
| CPMK-2.4 | Melakukan eksplorasi data menggunakan pandas dan numpy untuk menghasilkan ringkasan statistik | C3 |
| CPMK-2.5 | Menginterpretasikan hasil statistika deskriptif dalam konteks data riil Indonesia | C3 |

---

## 2.1 Mengapa Statistika Deskriptif?

Pada Bab 1, kita membahas bahwa statistika adalah ilmu belajar dari data. Namun, data mentah dalam jumlah besar tidak bermakna tanpa proses **ringkasan** dan **eksplorasi**. Bayangkan Anda menerima CSV berisi 10.000 baris transaksi Tokopedia — langkah pertama adalah **statistika deskriptif**.

> "You can't understand what you can't summarize."
> — Hadley Wickham, *R for Data Science*

**Statistika deskriptif** bertugas **meringkas**, **mengorganisasi**, dan **menyajikan** data agar mudah dipahami, tanpa menarik kesimpulan tentang populasi.

```
              STATISTIKA DESKRIPTIF
                      │
        ┌─────────────┼─────────────┐
        │             │             │
   PEMUSATAN     PENYEBARAN     POSISI
   (Central      (Dispersion)   (Position)
    Tendency)         │             │
        │        ┌────┼────┐    ┌──┼──┐
     Mean     Range Var  Std  Q1  Percentile
     Median        IQR       Q2  Z-score
     Modus                   Q3
```

Ketiga pilar ini saling melengkapi: pemusatan menunjukkan **di mana** pusat data, penyebaran menunjukkan **seberapa tersebar** data, dan posisi menunjukkan **letak relatif** suatu titik data.

---

## 2.2 Ukuran Pemusatan (*Measures of Central Tendency*)

### 2.2.1 Mean (Rata-rata Aritmetika)

**Rumus sampel:** $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$ | **Rumus populasi:** $\mu = \frac{1}{N} \sum_{i=1}^{N} x_i$

**Intuisi:** Mean adalah titik keseimbangan data, seperti titik tumpu pada papan jungkat-jungkit.

```
Nilai:   2    4    5    5    7    8    11
         *    *    **        *    *         *
  ──┬────┬────┬────┬────┬────┬────┬────┬────┬──
    1    2    3    4    5    6    7    8   ...  11
                              △
                         Mean = 6.0
```

**Contoh perhitungan manual:** Data nilai UTS 5 mahasiswa Informatika UAI: 75, 82, 68, 91, 64

$$\bar{x} = \frac{75 + 82 + 68 + 91 + 64}{5} = \frac{380}{5} = 76.0$$

```python
import numpy as np
import pandas as pd

nilai_uts = [75, 82, 68, 91, 64]

# Tiga cara menghitung mean
print(f"Mean (manual) : {sum(nilai_uts) / len(nilai_uts):.2f}")
print(f"Mean (numpy)  : {np.mean(nilai_uts):.2f}")
print(f"Mean (pandas) : {pd.Series(nilai_uts).mean():.2f}")
```

**Kelemahan Mean — Sensitif terhadap outlier:**

```python
pendapatan = [5, 6, 7, 7, 8, 8, 9, 10]  # juta Rp/bulan
print(f"Mean tanpa outlier : {np.mean(pendapatan):.2f} juta")

pendapatan_outlier = [5, 6, 7, 7, 8, 8, 9, 10, 200]  # + seorang CEO
print(f"Mean dengan outlier: {np.mean(pendapatan_outlier):.2f} juta")
print(f"Median tetap stabil: {np.median(pendapatan_outlier):.2f} juta")
```

Satu outlier (200 juta) membuat mean "tertarik" jauh ke kanan. Inilah mengapa BPS melaporkan **median** pendapatan rumah tangga Indonesia.

### 2.2.2 Median (Nilai Tengah)

**Definisi:** Nilai yang membagi data terurut menjadi dua bagian sama besar (50%-50%).

$$\text{Median} = \begin{cases} x_{\left(\frac{n+1}{2}\right)} & \text{jika } n \text{ ganjil} \\ \frac{x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2}+1\right)}}{2} & \text{jika } n \text{ genap} \end{cases}$$

**Contoh (n ganjil):** Data terurut: 64, 68, **75**, 82, 91 → Median = 75

**Contoh (n genap):** Data terurut: 64, 68, **75, 82**, 88, 91 → Median = (75+82)/2 = 78.5

```python
print(f"Median (n=5): {np.median([75, 82, 68, 91, 64]):.2f}")
print(f"Median (n=6): {np.median([75, 82, 68, 91, 64, 88]):.2f}")
```

**Kapan menggunakan median:** Data mengandung outlier, distribusi skewed, atau data ordinal.

### 2.2.3 Modus (*Mode*)

**Definisi:** Nilai yang paling sering muncul. Satu-satunya ukuran pemusatan yang valid untuk data **nominal**.

```python
metode_bayar = pd.Series(['GoPay', 'OVO', 'GoPay', 'Dana', 'GoPay', 'OVO'])
print(f"Modus: {metode_bayar.mode().values}")   # Output: ['GoPay']

nilai_quiz = pd.Series([80, 85, 85, 90, 75, 85, 80])
print(f"Modus: {nilai_quiz.mode().values}")       # Output: [85]
```

### 2.2.4 Perbandingan dan Hubungan dengan Bentuk Distribusi

| Ukuran | Kelebihan | Kelemahan | Skala Data |
|--------|-----------|-----------|------------|
| **Mean** | Memanfaatkan semua data; basis rumus lanjutan | Sensitif outlier | Interval, Rasio |
| **Median** | Robust terhadap outlier | Tidak memanfaatkan semua data | Ordinal, Interval, Rasio |
| **Modus** | Bisa untuk semua tipe data | Bisa tidak ada / lebih dari satu | Semua (NOIR) |

```
Simetris                  Right-Skewed              Left-Skewed
(Mean = Median = Modus)  (Modus < Median < Mean)  (Mean < Median < Modus)

       ___                     ___                      ___
     /     \                 /    \                    /    \
    /       \               /      \___            __/      \
   /         \             /           \          /           \
──┴─────┬─────┴──       ──┴──┬──────────┴──    ──┴──────────┬──┴──
    Mean=Med=Mod         Mod Med  Mean         Mean  Med  Mod
```

> **Tips:** Jika mean dan median berbeda jauh, distribusi kemungkinan skewed atau terdapat outlier. Median biasanya lebih representatif dalam kasus tersebut.

---

## 2.3 Ukuran Penyebaran (*Measures of Dispersion*)

Dua dataset bisa memiliki mean sama tetapi penyebaran sangat berbeda:

```
Dataset A (std=2):    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     Dataset B (std=15):   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                    ──┬──┬──┬──┬──┬──             ──┬──┬──┬──┬──┬──┬──┬──┬──
                     46 48 50 52 54                 20 30 40 50 60 70 80
                    Penyebaran KECIL               Penyebaran BESAR
```

### 2.3.1 Range (Jangkauan)

$$\text{Range} = x_{\max} - x_{\min}$$

Mudah dihitung, tetapi sangat sensitif terhadap outlier (hanya menggunakan 2 titik data).

```python
response_time = [120, 135, 128, 142, 115, 138, 125, 131, 890, 119]
print(f"Range: {max(response_time) - min(response_time)} ms")  # 775 ms
print(f"Range (numpy): {np.ptp(response_time)} ms")
```

### 2.3.2 Variance (Varians)

**Varians populasi:** $\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2$ | **Varians sampel:** $s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$

> **Bessel's correction:** Pembagi $n-1$ (bukan $n$) pada varians sampel menghasilkan estimator tak bias (*unbiased*). Kita kehilangan satu derajat kebebasan karena $\bar{x}$ dihitung dari data yang sama.

**Contoh perhitungan manual:** Data IPK: 3.75, 3.50, 3.85, 3.20, 3.60 | $\bar{x} = 3.58$

| $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
|--------|-----------------|---------------------|
| 3.75 | 0.17 | 0.0289 |
| 3.50 | -0.08 | 0.0064 |
| 3.85 | 0.27 | 0.0729 |
| 3.20 | -0.38 | 0.1444 |
| 3.60 | 0.02 | 0.0004 |
| **Total** | | **0.2530** |

$s^2 = \frac{0.2530}{4} = 0.0633$

```python
ipk = [3.75, 3.50, 3.85, 3.20, 3.60]
print(f"Var populasi (ddof=0): {np.var(ipk, ddof=0):.4f}")
print(f"Var sampel   (ddof=1): {np.var(ipk, ddof=1):.4f}")  # default pandas
print(f"Var pandas           : {pd.Series(ipk).var():.4f}")
```

> **Hati-hati:** `np.var()` default `ddof=0` (populasi), sedangkan `pd.Series.var()` default `ddof=1` (sampel). Dalam mata kuliah ini, kita selalu menggunakan **varians sampel** (ddof=1).

### 2.3.3 Standard Deviation (Simpangan Baku)

$$s = \sqrt{s^2} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

Standard deviation memiliki **satuan sama** dengan data asli (berbeda dengan variance yang satuannya kuadrat), sehingga lebih mudah diinterpretasikan.

**Aturan Empiris (distribusi mendekati normal):**

```
           68.27%
       ┌─────┴─────┐
       95.45%
   ┌────┴────────────┐
   99.73%
┌──┴──────────────────┐
──┼──┼──┼──┼──┼──┼──┼──
 -3s -2s -1s  μ  +1s +2s +3s
```

### 2.3.4 Coefficient of Variation (CV)

$$CV = \frac{s}{\bar{x}} \times 100\%$$

Berguna untuk membandingkan variabilitas dua dataset dengan satuan atau skala berbeda.

```python
ipk = np.array([3.75, 3.50, 3.85, 3.20, 3.60, 3.90, 3.45, 3.70])
pendapatan = np.array([1.5, 2.0, 1.8, 3.5, 1.2, 2.5, 1.0, 4.0])

cv_ipk = (np.std(ipk, ddof=1) / np.mean(ipk)) * 100
cv_pendapatan = (np.std(pendapatan, ddof=1) / np.mean(pendapatan)) * 100
print(f"CV IPK: {cv_ipk:.2f}% | CV Pendapatan: {cv_pendapatan:.2f}%")
# Pendapatan lebih bervariasi secara relatif
```

### 2.3.5 IQR dan Deteksi Outlier

$$\text{IQR} = Q3 - Q1$$

IQR mengukur lebar "kotak tengah" yang memuat 50% data pusat. Lebih **robust** terhadap outlier dibanding range.

**Aturan deteksi outlier:** Batas bawah = $Q1 - 1.5 \times \text{IQR}$ | Batas atas = $Q3 + 1.5 \times \text{IQR}$

```python
pendapatan = pd.Series([4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0,
                          8.5, 9.0, 10.0, 12.0, 15.0, 45.0, 60.0])
Q1, Q3 = pendapatan.quantile(0.25), pendapatan.quantile(0.75)
IQR = Q3 - Q1
batas_bawah, batas_atas = Q1 - 1.5*IQR, Q3 + 1.5*IQR

print(f"Q1: {Q1:.2f} | Q3: {Q3:.2f} | IQR: {IQR:.2f}")
print(f"Batas: [{batas_bawah:.2f}, {batas_atas:.2f}]")

outliers = pendapatan[(pendapatan < batas_bawah) | (pendapatan > batas_atas)]
print(f"Outlier: {outliers.values}")  # [45. 60.]
```

---

## 2.4 Ukuran Posisi (*Measures of Position*)

### 2.4.1 Kuartil dan Persentil

Kuartil membagi data terurut menjadi **empat bagian** sama besar:

```
 │     25%     │     25%     │     25%     │     25%     │
 Min ──────── Q1 ──────── Q2 ──────── Q3 ──────── Max
                            (Median)
```

Persentil membagi data menjadi **100 bagian**. Persentil ke-*p* berarti *p*% data berada di bawahnya.

```python
# Response time API e-commerce (milidetik)
rt = np.array([45, 52, 48, 55, 61, 43, 58, 47, 51, 49,
               53, 56, 44, 50, 62, 46, 54, 57, 42, 59,
               120, 85, 67, 73, 41, 63, 78, 52, 48, 95])

for p in [50, 75, 90, 95, 99]:
    print(f"P{p:2d}: {np.percentile(rt, p):.1f} ms")

# P99 digunakan perusahaan seperti Gojek/Tokopedia untuk SLA monitoring
```

### 2.4.2 Z-Score (Skor Standar)

$$z = \frac{x - \bar{x}}{s}$$

Z-score menunjukkan berapa standard deviation suatu data berada dari mean, memungkinkan perbandingan lintas distribusi.

```python
# Ahmad mendapat 85 di Statistika (mean=72, std=8)
# Budi mendapat 78 di Kalkulus (mean=60, std=10)
z_ahmad = (85 - 72) / 8   # 1.62
z_budi = (78 - 60) / 10   # 1.80

print(f"Z-score Ahmad: {z_ahmad:.2f} | Budi: {z_budi:.2f}")
print(f"Budi lebih menonjol di kelasnya (z-score lebih tinggi)")
```

---

## 2.5 Five-Number Summary dan Boxplot

### 2.5.1 Five-Number Summary

Lima nilai kunci yang meringkas distribusi data: **Min, Q1, Median (Q2), Q3, Max**.

```python
# Data IPM 10 provinsi (sumber: BPS, data ilustratif)
ipm = pd.Series({
    'DKI Jakarta': 81.11, 'DI Yogyakarta': 80.64,
    'Kaltim': 76.88, 'Bali': 75.69, 'Riau': 73.10,
    'Jabar': 72.45, 'Jateng': 72.16, 'Sulsel': 71.66,
    'NTT': 65.28, 'Papua': 60.62
})

print(f"Min    : {ipm.min():.2f} ({ipm.idxmin()})")
print(f"Q1     : {ipm.quantile(0.25):.2f}")
print(f"Median : {ipm.median():.2f}")
print(f"Q3     : {ipm.quantile(0.75):.2f}")
print(f"Max    : {ipm.max():.2f} ({ipm.idxmax()})")
```

### 2.5.2 Anatomi Boxplot

```
  Outlier                                            Outlier
    o                                                  o
    │       ┌──────────────┬──────────────┐            │
────┼───────│     Q1       │  Q2 (Median) │  Q3 ──────┼──
    │       └──────────────┴──────────────┘            │
  Whisker                "Box"                      Whisker
 (Q1-1.5*IQR)         (IQR = Q3-Q1)             (Q3+1.5*IQR)
              memuat 50% data tengah
```

**Membaca boxplot:** Kotak = 50% data tengah. Garis dalam kotak = median. Kumis = data terluar non-outlier. Titik di luar kumis = outlier.

```python
import matplotlib.pyplot as plt

ipm_jawa = [81.11, 72.45, 72.16, 80.64, 72.14, 72.44, 75.69]
ipm_sumatera = [72.18, 72.00, 72.38, 73.10, 71.63, 70.24, 71.40, 69.69, 71.69, 75.48]
ipm_kalimantan = [67.90, 71.15, 70.91, 76.88, 71.19]
ipm_sulawesi = [72.93, 69.55, 71.66, 71.20, 68.49, 65.73]
ipm_timur = [69.45, 68.70, 65.09, 60.62]

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot([ipm_jawa, ipm_sumatera, ipm_kalimantan, ipm_sulawesi, ipm_timur],
           labels=['Jawa', 'Sumatera', 'Kalimantan', 'Sulawesi', 'Papua &\nMaluku'],
           patch_artist=True,
           boxprops=dict(facecolor='lightblue', color='navy'),
           medianprops=dict(color='red', linewidth=2))
ax.set_title('Perbandingan IPM antar Wilayah Indonesia', fontsize=14)
ax.set_ylabel('Indeks Pembangunan Manusia (IPM)')
ax.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()
```

---

## 2.6 Eksplorasi Data dengan pandas dan numpy

### 2.6.1 Fungsi Kunci pandas untuk EDA

| Fungsi | Kegunaan |
|--------|----------|
| `.describe()` | Ringkasan statistik otomatis (count, mean, std, min, Q1, median, Q3, max) |
| `.info()` | Struktur dataset: tipe data, jumlah non-null, penggunaan memori |
| `.value_counts()` | Frekuensi setiap nilai (untuk data kategorikal) |
| `.groupby()` | Analisis statistik per kelompok/kategori |

### 2.6.2 Contoh Eksplorasi Dataset

```python
import numpy as np, pandas as pd
np.random.seed(42)
n = 200

df = pd.DataFrame({
    'provinsi': np.random.choice(
        ['DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur', 'Banten'],
        size=n, p=[0.25, 0.25, 0.20, 0.20, 0.10]),
    'jenis_kelamin': np.random.choice(['Laki-laki', 'Perempuan'], size=n),
    'usia': np.random.normal(35, 12, size=n).astype(int).clip(18, 65),
    'pendidikan': np.random.choice(
        ['SD', 'SMP', 'SMA', 'D3', 'S1', 'S2'],
        size=n, p=[0.10, 0.15, 0.30, 0.15, 0.25, 0.05]),
    'pendapatan_juta': np.round(np.random.lognormal(1.5, 0.7, n), 2),
    'status_pekerjaan': np.random.choice(
        ['PNS', 'Swasta', 'Wiraswasta', 'Freelance', 'Tidak Bekerja'],
        size=n, p=[0.15, 0.35, 0.25, 0.15, 0.10]),
})
df['pengeluaran_juta'] = np.round(
    df['pendapatan_juta'] * np.random.uniform(0.60, 0.90, n), 2)

# --- Eksplorasi ---
print("=== RINGKASAN STATISTIK ===")
print(df.describe().round(2))

print("\n=== DISTRIBUSI PER PROVINSI ===")
print(df['provinsi'].value_counts())

print("\n=== PENDAPATAN PER PROVINSI ===")
print(df.groupby('provinsi')['pendapatan_juta'].agg(
    ['count', 'mean', 'median', 'std']).round(2))
```

### 2.6.3 Tabel Distribusi Frekuensi

```python
bins = [0, 2, 4, 6, 8, 10, 15, 20, 100]
labels = ['0-2', '2-4', '4-6', '6-8', '8-10', '10-15', '15-20', '>20']
df['kelas_pendapatan'] = pd.cut(df['pendapatan_juta'], bins=bins, labels=labels, right=False)

freq = df['kelas_pendapatan'].value_counts().sort_index().reset_index()
freq.columns = ['Kelas (Juta Rp)', 'Frekuensi']
freq['Frek. Relatif (%)'] = (freq['Frekuensi'] / len(df) * 100).round(1)
freq['Frek. Kumulatif'] = freq['Frekuensi'].cumsum()
print(freq.to_string(index=False))
```

### 2.6.4 Skewness dan Kurtosis

| Skewness | Interpretasi | Hubungan Mean-Median |
|----------|-------------|---------------------|
| = 0 | Simetris | Mean = Median |
| > 0 | Right-skewed (ekor kanan panjang) | Mean > Median |
| < 0 | Left-skewed (ekor kiri panjang) | Mean < Median |

| Kurtosis (Excess) | Jenis | Ciri |
|-------------------|-------|------|
| = 0 | Mesokurtik | Seperti distribusi normal |
| > 0 | Leptokurtik | Lebih runcing, ekor tebal |
| < 0 | Platikurtik | Lebih datar, ekor tipis |

```python
pend = df['pendapatan_juta']
print(f"Skewness: {pend.skew():.4f} | Kurtosis: {pend.kurtosis():.4f}")
print(f"Mean: {pend.mean():.2f} | Median: {pend.median():.2f}")
# Mean > Median → right-skewed (tipikal data pendapatan Indonesia)
```

---

## 2.7 Studi Kasus: Analisis Data Sosial Ekonomi Indonesia

### 2.7.1 Konteks

Dalam studi kasus ini, kita mempraktikkan seluruh teknik statistika deskriptif pada data simulasi yang menyerupai data survei BPS. Kita akan melakukan analisis end-to-end: dari eksplorasi awal hingga interpretasi temuan.

### 2.7.2 Analisis Lengkap

```python
import numpy as np, pandas as pd, matplotlib.pyplot as plt
np.random.seed(42)
n = 200

# --- Buat Dataset ---
df = pd.DataFrame({
    'id': range(1, n+1),
    'provinsi': np.random.choice(
        ['DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur', 'Banten'],
        n, p=[0.25, 0.25, 0.20, 0.20, 0.10]),
    'jenis_kelamin': np.random.choice(['Laki-laki', 'Perempuan'], n),
    'usia': np.random.normal(35, 12, n).astype(int).clip(18, 65),
    'pendapatan_juta': np.round(np.random.lognormal(1.5, 0.7, n), 2),
    'status_pekerjaan': np.random.choice(
        ['PNS', 'Swasta', 'Wiraswasta', 'Freelance', 'Tidak Bekerja'],
        n, p=[0.15, 0.35, 0.25, 0.15, 0.10]),
})
df['pengeluaran_juta'] = np.round(
    df['pendapatan_juta'] * np.random.uniform(0.6, 0.9, n), 2)

# Tambahkan outlier
df.loc[5, 'pendapatan_juta'] = 85.0
df.loc[15, 'pendapatan_juta'] = 92.5

# --- Statistik Deskriptif ---
pend = df['pendapatan_juta']
Q1, Q3 = pend.quantile(0.25), pend.quantile(0.75)
IQR = Q3 - Q1

print("=" * 55)
print("  ANALISIS DESKRIPTIF: PENDAPATAN RESPONDEN")
print("=" * 55)
print(f"\nMean: {pend.mean():.2f} | Median: {pend.median():.2f} juta")
print(f"Std: {pend.std():.2f} | IQR: {IQR:.2f} | CV: {pend.std()/pend.mean()*100:.1f}%")
print(f"Skewness: {pend.skew():.4f} | Kurtosis: {pend.kurtosis():.4f}")

# --- Deteksi Outlier ---
batas_bawah, batas_atas = Q1 - 1.5*IQR, Q3 + 1.5*IQR
outliers = df[(pend < batas_bawah) | (pend > batas_atas)]
print(f"\nOutlier: {len(outliers)} data (batas: [{batas_bawah:.2f}, {batas_atas:.2f}])")

# --- Analisis per Kelompok ---
print("\n=== PENDAPATAN PER PROVINSI ===")
print(df.groupby('provinsi')['pendapatan_juta'].agg(
    ['count', 'mean', 'median', 'std']).round(2).sort_values('mean', ascending=False))

# --- Visualisasi Boxplot ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].boxplot(pend, vert=True, patch_artist=True,
                boxprops=dict(facecolor='lightblue'))
axes[0].set_title('Boxplot Pendapatan (Juta Rp)')
axes[0].axhline(y=batas_atas, color='red', linestyle='--',
                label=f'Batas atas: {batas_atas:.1f}')
axes[0].legend()

data_prov = [df[df['provinsi']==p]['pendapatan_juta'].values
              for p in sorted(df['provinsi'].unique())]
axes[1].boxplot(data_prov, labels=sorted(df['provinsi'].unique()),
                patch_artist=True)
axes[1].set_title('Pendapatan per Provinsi')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
```

### 2.7.3 Interpretasi Temuan

Dari analisis di atas, beberapa insight penting:

1. **Distribusi right-skewed:** Mean lebih besar dari median, menunjukkan sebagian besar responden berpendapatan rendah-menengah dengan sedikit orang berpendapatan sangat tinggi — pola khas distribusi pendapatan Indonesia.

2. **Outlier terdeteksi:** Metode IQR mengidentifikasi beberapa pendapatan ekstrem yang perlu diselidiki lebih lanjut — apakah data entry error atau memang valid.

3. **Median lebih representatif:** Untuk data skewed seperti ini, median (bukan mean) lebih tepat sebagai ukuran "pendapatan tipikal".

4. **Variasi antar provinsi:** Analisis groupby menunjukkan perbedaan pendapatan antar provinsi, dengan DKI Jakarta cenderung lebih tinggi.

---

## 2.8 AI Corner: Menggunakan AI untuk Statistika Deskriptif

### 2.8.1 Contoh Prompt yang Efektif

**Prompt 1 — Interpretasi Output:**
```
Berikut output .describe() dari data pendapatan 200 responden:
       pendapatan_juta
count        200.00
mean           6.42
std           10.15
min            0.15
25%            2.45
50%            4.18
75%            7.30
max           92.50

Jelaskan: (1) Apa artinya std > mean? (2) Bandingkan mean vs median.
(3) Adakah indikasi outlier dari five-number summary ini?
```

**Prompt 2 — Generate Kode:**
```
Saya punya DataFrame df dengan kolom 'pendapatan_juta' dan 'provinsi'.
Buatkan kode Python untuk five-number summary per provinsi, deteksi
outlier per provinsi dengan metode IQR, dan boxplot perbandingan.
```

### 2.8.2 Verifikasi Output AI

```
┌──────────────────────────────────────────────────────┐
│  AI BISA SALAH — SELALU VERIFIKASI!                  │
│                                                      │
│  1. Jalankan kode yang digenerate di Google Colab     │
│  2. Cocokkan interpretasi dengan materi kuliah        │
│  3. Periksa apakah ddof=0 atau ddof=1 yang dipakai   │
│  4. Pastikan kesimpulan logis dan didukung data       │
└──────────────────────────────────────────────────────┘
```

---

## Rangkuman Bab 2

1. **Statistika deskriptif** meringkas data melalui tiga pilar: ukuran pemusatan, penyebaran, dan posisi.

2. **Ukuran pemusatan:** mean (sensitif outlier, untuk interval/rasio), median (robust, untuk data skewed), modus (satu-satunya untuk data nominal).

3. **Ukuran penyebaran:** range (sederhana tapi sensitif outlier), variance dan standard deviation (basis teori statistik), CV (membandingkan variabilitas beda satuan), IQR (robust terhadap outlier).

4. **Ukuran posisi:** quartiles, percentiles, dan z-score menunjukkan letak relatif data dalam distribusi. P99 digunakan industri teknologi untuk monitoring performa.

5. **Five-number summary** (Min, Q1, Median, Q3, Max) dan **boxplot** memberikan ringkasan visual yang efektif, termasuk deteksi outlier.

6. **pandas** menyediakan fungsi EDA: `.describe()`, `.info()`, `.value_counts()`, dan `.groupby()`. **numpy** menyediakan operasi vectorized untuk komputasi statistik.

7. **Skewness** mengukur ketidaksimetrisan distribusi, **kurtosis** mengukur keruncingan. Data pendapatan Indonesia biasanya right-skewed.

8. Untuk data skewed atau mengandung outlier, **median dan IQR** lebih representatif daripada mean dan standard deviation.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan perbedaan antara mean, median, dan modus. Berikan masing-masing satu contoh situasi di mana ukuran tersebut paling tepat digunakan dalam konteks data Indonesia.

**Soal 2.** Perhatikan data jumlah pesanan harian sebuah toko online di Tokopedia selama 10 hari:
`15, 22, 18, 25, 20, 17, 23, 19, 21, 16`
Hitung secara manual: (a) Mean, (b) Median, (c) Range.

**Soal 3.** Jelaskan mengapa standard deviation lebih sering digunakan daripada variance untuk melaporkan penyebaran data.

**Soal 4.** Perhatikan output `.describe()` berikut:
```
       harga_properti_juta
count        500.00
mean         850.25
std          620.40
min           95.00
25%          425.00
50%          680.00
75%         1050.00
max         4500.00
```
(a) Berapa median harga properti? (b) Apakah distribusi harga simetris, skewed kiri, atau skewed kanan? Jelaskan. (c) Hitung IQR.

**Soal 5.** Apa yang dimaksud dengan Bessel's correction? Mengapa varians sampel menggunakan pembagi $(n-1)$?

### Tingkat Menengah (C2-C3)

**Soal 6.** Diberikan data pengeluaran bulanan (juta Rp) 12 mahasiswa:
`1.5, 2.0, 1.8, 2.5, 1.2, 3.0, 2.2, 1.7, 2.8, 15.0, 1.9, 2.3`
(a) Hitung mean dan median secara manual. (b) Buktikan bahwa 15.0 adalah outlier dengan metode IQR. (c) Hitung ulang mean dan median tanpa outlier. (d) Ukuran mana yang lebih representatif? Jelaskan.

**Soal 7.** Tulis kode Python (runnable di Google Colab) untuk: (a) Membuat numpy array 30 data acak bilangan bulat 50-100 (seed=42). (b) Menghitung mean, median, std, Q1, Q3, IQR. (c) Mendeteksi outlier dengan metode IQR. (d) Menghitung z-score setiap data. (e) Menampilkan semua hasil dengan format rapi.

**Soal 8.** Seorang analyst di Gojek membandingkan waktu tunggu GoRide di dua kota: Jakarta (mean=4.5, std=2.1) dan Surabaya (mean=3.2, std=1.8).
(a) Hitung CV masing-masing kota. (b) Kota mana yang lebih konsisten? (c) Jika penumpang Jakarta menunggu 8 menit, berapa z-score-nya? Apakah wajar?

**Soal 9.** Jelaskan perbedaan: (a) `np.var(data)` vs `np.var(data, ddof=1)` — default dan kapan harus hati-hati. (b) Persentil ke-90 (P90) vs kuartil ke-3 (Q3). (c) Kapan menggunakan mean vs median.

### Tingkat Mahir (C3-C4)

**Soal 10.** Buat kode Python lengkap untuk analisis deskriptif IPM 34 provinsi Indonesia: (a) DataFrame dengan kolom provinsi, ipm, pulau. (b) Five-number summary. (c) Skewness dan kurtosis. (d) Deteksi outlier (IQR). (e) Groupby per pulau. (f) Boxplot perbandingan antar pulau. (g) Interpretasi minimal 1 paragraf.

**Soal 11.** Data transaksi harian e-commerce menunjukkan: Mean=1.250, Median=980, Skewness=1.85, Kurtosis=4.20.
(a) Sketsa bentuk distribusi. (b) Interpretasikan skewness dan kurtosis dalam konteks bisnis. (c) Mengapa median lebih tepat sebagai "transaksi harian tipikal"? (d) Apa implikasi kurtosis tinggi bagi perencanaan kapasitas server?

**Soal 12.** Data gaji bulanan (juta Rp) di startup teknologi:
```
Engineering: 12, 15, 14, 18, 25, 13, 16, 22, 14, 17
Marketing  :  8, 10,  9, 11, 35,  9, 10, 12,  8, 10
Operations :  7,  8,  7,  9,  8,  7, 10,  8,  7,  9
```
Tulis kode Python untuk: (a) Mean, median, std, CV per tim. (b) Tim dengan variabilitas tertinggi (gunakan CV). (c) Deteksi outlier per tim. (d) Boxplot perbandingan. (e) Interpretasi: tim mana dengan kesenjangan gaji terbesar dan kemungkinan penyebabnya.

**Soal 13.** Data response time API fintech: P50=120ms, P75=180ms, P90=350ms, P95=520ms, P99=1.200ms.
(a) Interpretasikan setiap persentil dalam bahasa non-teknis. (b) Jika SLA menetapkan P99 < 1.000ms, apakah memenuhi? (c) Mengapa perusahaan memonitor P99, bukan mean? (d) Tulis prompt AI yang efektif untuk menganalisis data ini lebih lanjut.

---

## Referensi

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability & Statistics for Engineers & Scientists* (9th ed.). Pearson.
2. Moore, D. S., McCabe, G. P., & Craig, B. A. (2021). *Introduction to the Practice of Statistics* (10th ed.). W. H. Freeman.
3. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
4. Bruce, P., Bruce, A., & Gedeck, P. (2020). *Practical Statistics for Data Scientists* (2nd ed.). O'Reilly Media.
5. BPS. (2024). *Indeks Pembangunan Manusia per Provinsi*. https://www.bps.go.id
6. pandas Documentation. *Descriptive Statistics*. https://pandas.pydata.org/docs/user_guide/basics.html
7. NumPy Documentation. *Statistics*. https://numpy.org/doc/stable/reference/routines.statistics.html

---

*Bab berikutnya: **Bab 3 — Visualisasi Data dengan matplotlib dan seaborn***
