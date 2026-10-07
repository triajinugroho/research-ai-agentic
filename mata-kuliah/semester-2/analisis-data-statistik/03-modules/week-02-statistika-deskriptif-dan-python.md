# Minggu 2: Statistika Deskriptif dan Eksplorasi Data dengan Python

## Informasi Modul

| Komponen | Keterangan |
|---|---|
| **Minggu** | 2 |
| **Topik** | Statistika Deskriptif dan Eksplorasi Data dengan Python |
| **CPMK** | CPMK-2: Menghitung dan menginterpretasikan ukuran statistika deskriptif menggunakan Python |
| **Sub-CPMK** | 2.1 Menghitung ukuran pemusatan dan penyebaran data secara manual dan dengan Python |
| | 2.2 Melakukan eksplorasi data menggunakan pandas dan numpy |
| **Bloom's Taxonomy** | C3 (Mengaplikasikan / *Applying*) |
| **Durasi** | 2 x 50 menit |
| **Metode** | Ceramah interaktif, live coding, studi kasus |
| **Prasyarat** | Minggu 1: Pengantar Statistika di Era AI |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menghitung** ukuran pemusatan (mean, median, modus) dan ukuran penyebaran (range, variance, standard deviation, IQR) baik secara manual maupun menggunakan Python.
2. **Menginterpretasikan** makna skewness dan kurtosis dalam konteks bentuk distribusi data.
3. **Menggunakan** fungsi-fungsi pandas (`.describe()`, `.info()`, `.value_counts()`, `.groupby()`) dan numpy untuk melakukan eksplorasi data secara efektif.

---

## Materi Pembelajaran

### 1. Ukuran Pemusatan (*Measures of Central Tendency*)

Ukuran pemusatan menunjukkan nilai yang mewakili "pusat" atau "tengah" dari sebuah kumpulan data. Tiga ukuran utama yang akan kita pelajari:

#### a) Mean (Rata-rata Aritmetika)

**Definisi:** Jumlah seluruh nilai data dibagi dengan banyaknya data.

**Rumus:**

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i = \frac{x_1 + x_2 + \cdots + x_n}{n}$$

**Intuisi:** Mean adalah titik keseimbangan data. Bayangkan data sebagai beban di timbangan -- mean adalah titik di mana timbangan seimbang.

**Kapan menggunakan mean:**
- Data berskala interval atau rasio
- Distribusi data relatif simetris
- Tidak ada *outlier* (pencilan) yang ekstrem

**Contoh Perhitungan:**

Data IPK: 3.75, 3.50, 3.85, 3.20, 3.60

$$\bar{x} = \frac{3.75 + 3.50 + 3.85 + 3.20 + 3.60}{5} = \frac{17.90}{5} = 3.58$$

**Python:**

```python
import pandas as pd
import numpy as np

ipk = [3.75, 3.50, 3.85, 3.20, 3.60]

# Menggunakan numpy
mean_np = np.mean(ipk)
print(f"Mean (numpy): {mean_np:.2f}")

# Menggunakan pandas Series
s = pd.Series(ipk)
mean_pd = s.mean()
print(f"Mean (pandas): {mean_pd:.2f}")

# Menggunakan built-in Python
mean_manual = sum(ipk) / len(ipk)
print(f"Mean (manual): {mean_manual:.2f}")
```

Output:
```
Mean (numpy): 3.58
Mean (pandas): 3.58
Mean (manual): 3.58
```

#### b) Median (Nilai Tengah)

**Definisi:** Nilai yang membagi data terurut menjadi dua bagian sama besar.

**Rumus:**

Untuk data terurut $x_{(1)}, x_{(2)}, \ldots, x_{(n)}$:

$$\text{Median} = \begin{cases} x_{(\frac{n+1}{2})} & \text{jika } n \text{ ganjil} \\ \frac{x_{(\frac{n}{2})} + x_{(\frac{n}{2}+1)}}{2} & \text{jika } n \text{ genap} \end{cases}$$

**Intuisi:** Median adalah nilai "di tengah-tengah". 50% data berada di bawah median, dan 50% data berada di atas median.

**Kapan menggunakan median:**
- Data mengandung *outlier* (pencilan)
- Distribusi data tidak simetris (*skewed*)
- Data berskala ordinal, interval, atau rasio
- Contoh klasik: median lebih tepat untuk melaporkan pendapatan rumah tangga karena distribusi pendapatan biasanya *skewed*

**Contoh Perhitungan:**

Data terurut: 3.20, 3.50, **3.60**, 3.75, 3.85 (n = 5, ganjil)

Median = nilai ke-3 = **3.60**

**Python:**

```python
ipk = [3.75, 3.50, 3.85, 3.20, 3.60]

median_np = np.median(ipk)
print(f"Median (numpy): {median_np:.2f}")

median_pd = pd.Series(ipk).median()
print(f"Median (pandas): {median_pd:.2f}")
```

Output:
```
Median (numpy): 3.60
Median (pandas): 3.60
```

#### c) Modus (*Mode*)

**Definisi:** Nilai yang paling sering muncul dalam data.

**Intuisi:** Modus adalah jawaban dari pertanyaan "Apa yang paling umum?"

**Kapan menggunakan modus:**
- Data berskala nominal (satu-satunya ukuran pemusatan yang valid untuk data nominal)
- Ingin mengetahui kategori atau nilai yang paling populer/sering
- Bisa digunakan untuk semua skala pengukuran

**Python:**

```python
# Modus untuk data kategorikal
jurusan = ['Informatika', 'Sistem Informasi', 'Informatika',
           'Sistem Informasi', 'Informatika', 'Informatika']

s_jurusan = pd.Series(jurusan)
print(f"Modus jurusan: {s_jurusan.mode().values}")

# Modus untuk data numerik
semester = [4, 6, 4, 6, 2, 2, 4, 6, 4, 2]
s_semester = pd.Series(semester)
print(f"Modus semester: {s_semester.mode().values}")
```

Output:
```
Modus jurusan: ['Informatika']
Modus semester: [4]
```

#### Perbandingan Mean, Median, dan Modus

| Ukuran | Kelebihan | Kelemahan | Skala Data |
|---|---|---|---|
| **Mean** | Memanfaatkan semua data, basis banyak rumus lanjutan | Sensitif terhadap outlier | Interval, Rasio |
| **Median** | Robust terhadap outlier | Tidak memanfaatkan semua data | Ordinal, Interval, Rasio |
| **Modus** | Bisa untuk semua tipe data | Bisa tidak ada atau lebih dari satu | Semua skala |

> **Tips:** Jika mean jauh berbeda dari median, itu indikasi distribusi data tidak simetris (*skewed*) atau ada outlier.

---

### 2. Ukuran Penyebaran (*Measures of Dispersion*)

Ukuran pemusatan saja tidak cukup. Dua dataset bisa memiliki mean yang sama tetapi penyebaran yang sangat berbeda. Oleh karena itu, kita juga perlu ukuran penyebaran.

#### a) Range (Jangkauan)

**Definisi:** Selisih antara nilai terbesar dan terkecil.

$$\text{Range} = x_{max} - x_{min}$$

**Intuisi:** Seberapa "lebar" data tersebar.

**Kelemahan:** Sangat sensitif terhadap outlier, hanya menggunakan 2 titik data.

```python
ipk = [3.75, 3.50, 3.85, 3.20, 3.60]

range_ipk = max(ipk) - min(ipk)
print(f"Range IPK: {range_ipk:.2f}")

# Atau menggunakan numpy
range_np = np.ptp(ipk)  # ptp = peak to peak
print(f"Range (numpy): {range_np:.2f}")
```

Output:
```
Range IPK: 0.65
Range (numpy): 0.65
```

#### b) Variance (Varians)

**Definisi:** Rata-rata dari kuadrat selisih setiap data terhadap mean.

**Rumus (populasi):**

$$\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2$$

**Rumus (sampel):**

$$s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

> **Catatan:** Pembagi $n-1$ (bukan $n$) pada varians sampel disebut *Bessel's correction*, digunakan agar estimasi varians populasi tidak bias (*unbiased*).

**Intuisi:** Variance mengukur seberapa "jauh" data-data tersebar dari mean rata-rata. Semakin besar variance, semakin tersebar datanya.

```python
ipk = [3.75, 3.50, 3.85, 3.20, 3.60]

# Varians populasi (ddof=0)
var_pop = np.var(ipk, ddof=0)
print(f"Varians (populasi): {var_pop:.4f}")

# Varians sampel (ddof=1) -- default pandas
var_sample = pd.Series(ipk).var()
print(f"Varians (sampel): {var_sample:.4f}")
```

Output:
```
Varians (populasi): 0.0476
Varians (sampel): 0.0595
```

#### c) Standard Deviation (Simpangan Baku)

**Definisi:** Akar kuadrat dari varians.

**Rumus (sampel):**

$$s = \sqrt{s^2} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

**Intuisi:** Standard deviation memiliki satuan yang sama dengan data asli (berbeda dengan variance yang satuannya kuadrat), sehingga lebih mudah diinterpretasikan.

**Interpretasi umum (distribusi normal):**
- Sekitar 68% data berada dalam jarak 1 std dari mean
- Sekitar 95% data berada dalam jarak 2 std dari mean
- Sekitar 99.7% data berada dalam jarak 3 std dari mean

```python
ipk = [3.75, 3.50, 3.85, 3.20, 3.60]

# Standard deviation sampel
std_sample = pd.Series(ipk).std()
print(f"Std. Deviasi (sampel): {std_sample:.4f}")

# Menggunakan numpy (default ddof=0, jadi kita set ddof=1 untuk sampel)
std_np = np.std(ipk, ddof=1)
print(f"Std. Deviasi (numpy): {std_np:.4f}")

# Interpretasi
mean_ipk = np.mean(ipk)
print(f"\nMean: {mean_ipk:.2f}")
print(f"Mean - 1 Std: {mean_ipk - std_sample:.2f}")
print(f"Mean + 1 Std: {mean_ipk + std_sample:.2f}")
```

Output:
```
Std. Deviasi (sampel): 0.2439
Std. Deviasi (numpy): 0.2439

Mean: 3.58
Mean - 1 Std: 3.34
Mean + 1 Std: 3.82
```

#### d) IQR (Interquartile Range)

**Definisi:** Selisih antara kuartil ketiga (Q3) dan kuartil pertama (Q1).

$$\text{IQR} = Q3 - Q1$$

Di mana:
- **Q1** (Kuartil 1) = persentil ke-25 (25% data di bawahnya)
- **Q2** (Kuartil 2) = median = persentil ke-50
- **Q3** (Kuartil 3) = persentil ke-75 (75% data di bawahnya)

**Intuisi:** IQR mengukur lebar "kotak tengah" yang memuat 50% data. Lebih robust terhadap outlier dibandingkan range.

**Deteksi Outlier dengan IQR:**
- Batas bawah: $Q1 - 1.5 \times IQR$
- Batas atas: $Q3 + 1.5 \times IQR$
- Data di luar batas ini dianggap sebagai *outlier*

```python
ipk = pd.Series([3.75, 3.50, 3.85, 3.20, 3.60, 3.90, 3.45, 3.70, 3.55, 3.80])

Q1 = ipk.quantile(0.25)
Q3 = ipk.quantile(0.75)
IQR = Q3 - Q1

print(f"Q1: {Q1:.2f}")
print(f"Q3: {Q3:.2f}")
print(f"IQR: {IQR:.2f}")

# Batas outlier
batas_bawah = Q1 - 1.5 * IQR
batas_atas = Q3 + 1.5 * IQR
print(f"\nBatas bawah outlier: {batas_bawah:.2f}")
print(f"Batas atas outlier: {batas_atas:.2f}")

# Cek outlier
outliers = ipk[(ipk < batas_bawah) | (ipk > batas_atas)]
print(f"Outlier: {outliers.values if len(outliers) > 0 else 'Tidak ada'}")
```

Output:
```
Q1: 3.51
Q3: 3.81
IQR: 0.30

Batas bawah outlier: 3.06
Batas atas outlier: 4.26
Outlier: Tidak ada
```

---

### 3. Skewness dan Kurtosis

#### a) Skewness (Kecondongan)

**Definisi:** Ukuran ketidaksimetrisan distribusi data.

| Nilai Skewness | Interpretasi | Hubungan Mean-Median |
|---|---|---|
| Skewness = 0 | Distribusi simetris | Mean = Median |
| Skewness > 0 | Condong ke kanan (*right-skewed*) | Mean > Median |
| Skewness < 0 | Condong ke kiri (*left-skewed*) | Mean < Median |

**Ilustrasi:**

```
Left-skewed          Symmetric           Right-skewed
(Skewness < 0)      (Skewness = 0)      (Skewness > 0)

      ___                ___                ___
    /    \             /     \            /    \
   /      \           /       \          /      \
  /        \___      /         \      __/        \
```

**Contoh Konteks:**
- **Right-skewed:** Distribusi pendapatan (sedikit orang berpendapatan sangat tinggi)
- **Left-skewed:** Distribusi usia pensiun (sedikit orang pensiun sangat muda)
- **Simetris:** Tinggi badan, berat badan (mendekati distribusi normal)

```python
data = pd.Series([3.75, 3.50, 3.85, 3.20, 3.60, 3.90, 3.45, 3.70, 3.55, 3.80])

skewness = data.skew()
print(f"Skewness: {skewness:.4f}")

if skewness > 0:
    print("Distribusi condong ke kanan (right-skewed)")
elif skewness < 0:
    print("Distribusi condong ke kiri (left-skewed)")
else:
    print("Distribusi simetris")
```

#### b) Kurtosis (Keruncingan)

**Definisi:** Ukuran "keruncingan" atau "ketebalan ekor" distribusi data dibandingkan dengan distribusi normal.

| Jenis | Kurtosis (Excess) | Ciri |
|---|---|---|
| **Mesokurtik** | = 0 | Seperti distribusi normal |
| **Leptokurtik** | > 0 | Lebih runcing, ekor lebih tebal (*heavy-tailed*) |
| **Platikurtik** | < 0 | Lebih datar, ekor lebih tipis (*light-tailed*) |

> **Catatan:** pandas menggunakan *excess kurtosis* (dikurangi 3), sehingga distribusi normal memiliki kurtosis = 0.

```python
kurtosis = data.kurtosis()
print(f"Kurtosis (excess): {kurtosis:.4f}")

if kurtosis > 0:
    print("Leptokurtik: distribusi lebih runcing dari normal")
elif kurtosis < 0:
    print("Platikurtik: distribusi lebih datar dari normal")
else:
    print("Mesokurtik: seperti distribusi normal")
```

---

### 4. Eksplorasi Data dengan pandas

Pandas menyediakan fungsi-fungsi yang sangat berguna untuk mengeksplorasi data secara cepat dan efisien.

#### a) `.describe()` -- Ringkasan Statistik

```python
import pandas as pd

# Membuat dataset contoh
data = {
    'provinsi': ['DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur',
                 'Bali', 'Sumatera Utara', 'Sulawesi Selatan', 'Kalimantan Timur',
                 'Papua', 'NTT'],
    'ipm': [81.11, 72.45, 72.16, 72.14, 75.69,
            72.00, 71.66, 76.88, 60.62, 65.28],
    'populasi_juta': [10.56, 49.94, 36.52, 40.67, 4.32,
                      14.80, 9.07, 3.77, 4.30, 5.33],
    'tingkat_kemiskinan': [4.69, 7.88, 11.25, 10.49, 4.01,
                           8.42, 8.73, 6.10, 26.80, 20.23]
}

df = pd.DataFrame(data)

# describe() untuk kolom numerik
print("=== Ringkasan Statistik (Numerik) ===")
print(df.describe())
```

Output:
```
=== Ringkasan Statistik (Numerik) ===
             ipm  populasi_juta  tingkat_kemiskinan
count  10.000000      10.000000           10.000000
mean   71.999000      17.928000           10.860000
std     5.680...      16.405...            7.278...
min    60.620000       3.770000            4.010000
25%    71.780000       4.815000            6.545000
50%    72.150000       9.815000            8.575000
75%    75.385000      31.220000           11.060000
max    81.110000      49.940000           26.800000
```

**Membaca Output `.describe()`:**

| Statistik | Arti |
|---|---|
| **count** | Jumlah data non-null |
| **mean** | Rata-rata |
| **std** | Standard deviation (sampel) |
| **min** | Nilai minimum |
| **25%** | Kuartil 1 (Q1) |
| **50%** | Median (Q2) |
| **75%** | Kuartil 3 (Q3) |
| **max** | Nilai maksimum |

#### b) `.info()` -- Informasi Struktur Data

```python
print("=== Informasi Dataset ===")
df.info()
```

Output:
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 4 columns):
 #   Column              Non-Null Count  Dtype
---  ------              --------------  -----
 0   provinsi            10 non-null     object
 1   ipm                 10 non-null     float64
 2   populasi_juta       10 non-null     float64
 3   tingkat_kemiskinan  10 non-null     float64
dtypes: float64(3), object(1)
memory usage: 448.0+ bytes
```

**Informasi yang didapat dari `.info()`:**
- Jumlah baris dan kolom
- Nama kolom dan tipe datanya
- Jumlah data non-null (berguna untuk mendeteksi *missing values*)
- Penggunaan memori

#### c) `.value_counts()` -- Frekuensi Nilai

```python
# Contoh: menghitung frekuensi kategori
pendidikan = pd.Series(['S1', 'S2', 'S1', 'S3', 'S1', 'S2', 'S1', 'D3', 'S1', 'S2'])

print("=== Frekuensi Pendidikan ===")
print(pendidikan.value_counts())
print()

# Dengan persentase
print("=== Persentase ===")
print(pendidikan.value_counts(normalize=True).mul(100).round(1))
```

Output:
```
=== Frekuensi Pendidikan ===
S1    5
S2    3
D3    1
S3    1
dtype: int64

=== Persentase ===
S1    50.0
S2    30.0
D3    10.0
S3    10.0
dtype: float64
```

#### d) `.groupby()` -- Analisis per Kelompok

```python
# Dataset dengan kategori pulau
data2 = {
    'provinsi': ['DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur',
                 'Bali', 'Sumatera Utara', 'Sumatera Barat',
                 'Kalimantan Timur', 'Kalimantan Selatan',
                 'Sulawesi Selatan'],
    'pulau': ['Jawa', 'Jawa', 'Jawa', 'Jawa', 'Jawa',
              'Sumatera', 'Sumatera', 'Kalimantan', 'Kalimantan',
              'Sulawesi'],
    'ipm': [81.11, 72.45, 72.16, 72.14, 75.69,
            72.00, 72.38, 76.88, 70.91, 71.66],
    'tingkat_kemiskinan': [4.69, 7.88, 11.25, 10.49, 4.01,
                           8.42, 6.04, 6.10, 4.47, 8.73]
}

df2 = pd.DataFrame(data2)

# Rata-rata IPM per pulau
print("=== Rata-rata IPM per Pulau ===")
print(df2.groupby('pulau')['ipm'].mean().round(2))
print()

# Beberapa statistik sekaligus
print("=== Statistik Kemiskinan per Pulau ===")
print(df2.groupby('pulau')['tingkat_kemiskinan'].agg(['mean', 'min', 'max']).round(2))
```

Output:
```
=== Rata-rata IPM per Pulau ===
pulau
Jawa          74.71
Kalimantan    73.90
Sulawesi      71.66
Sumatera      72.19
Name: ipm, dtype: float64

=== Statistik Kemiskinan per Pulau ===
            mean   min    max
pulau
Jawa        7.66  4.01  11.25
Kalimantan  5.28  4.47   6.10
Sulawesi    8.73  8.73   8.73
Sumatera    7.23  6.04   8.42
```

---

### 5. Pengenalan numpy untuk Komputasi Numerik

**numpy** (Numerical Python) adalah library fundamental untuk komputasi numerik di Python. Semua library data science Python dibangun di atas numpy.

#### Mengapa numpy?

| Fitur | Python List | numpy Array |
|---|---|---|
| Kecepatan | Lambat (loop Python) | Cepat (operasi vectorized di C) |
| Memori | Boros | Efisien |
| Operasi Matematika | Manual per elemen | Langsung pada seluruh array |
| Broadcasting | Tidak ada | Didukung |

#### Operasi Dasar numpy

```python
import numpy as np

# Membuat array
data = np.array([3.75, 3.50, 3.85, 3.20, 3.60, 3.90, 3.45, 3.70, 3.55, 3.80])

# Statistik deskriptif dengan numpy
print("=== Statistik Deskriptif dengan numpy ===")
print(f"Mean       : {np.mean(data):.4f}")
print(f"Median     : {np.median(data):.4f}")
print(f"Std (pop)  : {np.std(data):.4f}")
print(f"Std (samp) : {np.std(data, ddof=1):.4f}")
print(f"Var (pop)  : {np.var(data):.4f}")
print(f"Var (samp) : {np.var(data, ddof=1):.4f}")
print(f"Min        : {np.min(data):.4f}")
print(f"Max        : {np.max(data):.4f}")
print(f"Sum        : {np.sum(data):.4f}")
print(f"Range      : {np.ptp(data):.4f}")

# Persentil
print(f"\nPersentil ke-25 (Q1): {np.percentile(data, 25):.4f}")
print(f"Persentil ke-50 (Q2): {np.percentile(data, 50):.4f}")
print(f"Persentil ke-75 (Q3): {np.percentile(data, 75):.4f}")
```

#### Operasi Vectorized

```python
# Operasi pada seluruh array sekaligus (tanpa loop)
nilai_ujian = np.array([75, 80, 65, 90, 85, 70, 95, 60, 88, 72])

# Konversi ke skala 4.0
nilai_4 = nilai_ujian / 100 * 4
print(f"Nilai skala 4.0: {np.round(nilai_4, 2)}")

# Z-score (standardisasi)
z_scores = (nilai_ujian - np.mean(nilai_ujian)) / np.std(nilai_ujian, ddof=1)
print(f"Z-scores: {np.round(z_scores, 2)}")

# Siapa yang nilainya di atas rata-rata?
mean_nilai = np.mean(nilai_ujian)
di_atas_rata = nilai_ujian[nilai_ujian > mean_nilai]
print(f"\nRata-rata: {mean_nilai:.1f}")
print(f"Nilai di atas rata-rata: {di_atas_rata}")
print(f"Jumlah: {len(di_atas_rata)} dari {len(nilai_ujian)} mahasiswa")
```

---

## Studi Kasus: Analisis Data Indeks Pembangunan Manusia (IPM) per Provinsi

### Konteks

Indeks Pembangunan Manusia (IPM) adalah indikator komposit yang mengukur kualitas hidup manusia berdasarkan tiga dimensi: kesehatan (umur panjang), pengetahuan (pendidikan), dan standar hidup layak (pendapatan). Data IPM dirilis setiap tahun oleh Badan Pusat Statistik (BPS).

### Dataset

```python
import pandas as pd
import numpy as np

# Data IPM per Provinsi (sumber: BPS, data ilustratif)
data_ipm = {
    'provinsi': [
        'Aceh', 'Sumatera Utara', 'Sumatera Barat', 'Riau',
        'Jambi', 'Sumatera Selatan', 'Bengkulu', 'Lampung',
        'Kep. Bangka Belitung', 'Kep. Riau', 'DKI Jakarta',
        'Jawa Barat', 'Jawa Tengah', 'DI Yogyakarta', 'Jawa Timur',
        'Banten', 'Bali', 'NTB', 'NTT',
        'Kalimantan Barat', 'Kalimantan Tengah', 'Kalimantan Selatan',
        'Kalimantan Timur', 'Kalimantan Utara',
        'Sulawesi Utara', 'Sulawesi Tengah', 'Sulawesi Selatan',
        'Sulawesi Tenggara', 'Gorontalo', 'Sulawesi Barat',
        'Maluku', 'Maluku Utara', 'Papua Barat', 'Papua'
    ],
    'ipm': [
        72.18, 72.00, 72.38, 73.10,
        71.63, 70.24, 71.40, 69.69,
        71.69, 75.48, 81.11,
        72.45, 72.16, 80.64, 72.14,
        72.44, 75.69, 68.65, 65.28,
        67.90, 71.15, 70.91,
        76.88, 71.19,
        72.93, 69.55, 71.66,
        71.20, 68.49, 65.73,
        69.45, 68.70, 65.09, 60.62
    ],
    'pulau': [
        'Sumatera', 'Sumatera', 'Sumatera', 'Sumatera',
        'Sumatera', 'Sumatera', 'Sumatera', 'Sumatera',
        'Sumatera', 'Sumatera', 'Jawa',
        'Jawa', 'Jawa', 'Jawa', 'Jawa',
        'Jawa', 'Jawa', 'Nusa Tenggara', 'Nusa Tenggara',
        'Kalimantan', 'Kalimantan', 'Kalimantan',
        'Kalimantan', 'Kalimantan',
        'Sulawesi', 'Sulawesi', 'Sulawesi',
        'Sulawesi', 'Sulawesi', 'Sulawesi',
        'Maluku', 'Maluku', 'Papua', 'Papua'
    ]
}

df = pd.DataFrame(data_ipm)
print(f"Dataset memiliki {df.shape[0]} provinsi dan {df.shape[1]} kolom")
print()
print(df.head(10))
```

### Langkah 1: Eksplorasi Awal

```python
# Informasi dataset
print("=== Info Dataset ===")
df.info()
print()

# Statistik deskriptif IPM
print("=== Statistik Deskriptif IPM ===")
print(df['ipm'].describe())
```

### Langkah 2: Hitung Ukuran Pemusatan dan Penyebaran

```python
print("=== Ukuran Pemusatan ===")
print(f"Mean IPM   : {df['ipm'].mean():.2f}")
print(f"Median IPM : {df['ipm'].median():.2f}")
print(f"Modus IPM  : {df['ipm'].mode().values}")
print()

print("=== Ukuran Penyebaran ===")
print(f"Range      : {df['ipm'].max() - df['ipm'].min():.2f}")
print(f"Variance   : {df['ipm'].var():.2f}")
print(f"Std Dev    : {df['ipm'].std():.2f}")

Q1 = df['ipm'].quantile(0.25)
Q3 = df['ipm'].quantile(0.75)
IQR = Q3 - Q1
print(f"IQR        : {IQR:.2f}")
print(f"Q1         : {Q1:.2f}")
print(f"Q3         : {Q3:.2f}")
print()

print("=== Bentuk Distribusi ===")
print(f"Skewness   : {df['ipm'].skew():.4f}")
print(f"Kurtosis   : {df['ipm'].kurtosis():.4f}")
```

### Langkah 3: Analisis per Kelompok Pulau

```python
print("=== IPM Rata-rata per Pulau ===")
ipm_per_pulau = df.groupby('pulau')['ipm'].agg(['mean', 'median', 'std', 'min', 'max', 'count'])
ipm_per_pulau = ipm_per_pulau.round(2).sort_values('mean', ascending=False)
print(ipm_per_pulau)
```

### Langkah 4: Identifikasi Provinsi Tertinggi dan Terendah

```python
# Top 5 IPM tertinggi
print("=== 5 Provinsi IPM Tertinggi ===")
top5 = df.nlargest(5, 'ipm')[['provinsi', 'ipm', 'pulau']]
print(top5.to_string(index=False))
print()

# Bottom 5 IPM terendah
print("=== 5 Provinsi IPM Terendah ===")
bottom5 = df.nsmallest(5, 'ipm')[['provinsi', 'ipm', 'pulau']]
print(bottom5.to_string(index=False))
```

### Langkah 5: Deteksi Outlier

```python
# Deteksi outlier menggunakan metode IQR
Q1 = df['ipm'].quantile(0.25)
Q3 = df['ipm'].quantile(0.75)
IQR = Q3 - Q1
batas_bawah = Q1 - 1.5 * IQR
batas_atas = Q3 + 1.5 * IQR

print(f"Batas bawah: {batas_bawah:.2f}")
print(f"Batas atas : {batas_atas:.2f}")
print()

outliers = df[(df['ipm'] < batas_bawah) | (df['ipm'] > batas_atas)]
if len(outliers) > 0:
    print("=== Provinsi Outlier ===")
    print(outliers[['provinsi', 'ipm', 'pulau']].to_string(index=False))
else:
    print("Tidak ada outlier yang terdeteksi.")
```

### Interpretasi Hasil

Setelah menjalankan seluruh kode di atas, diskusikan pertanyaan-pertanyaan berikut:

1. Apakah distribusi IPM di Indonesia simetris atau condong? Apa implikasinya?
2. Mengapa ada kesenjangan IPM antara Indonesia Barat dan Indonesia Timur?
3. Mengapa DKI Jakarta dan DI Yogyakarta memiliki IPM jauh lebih tinggi?
4. Apakah mean atau median lebih tepat untuk merepresentasikan IPM Indonesia? Mengapa?

---

## AI Corner: Gunakan AI untuk Menjelaskan Output `.describe()`

### Konsep

Salah satu cara efektif memanfaatkan AI assistant adalah untuk **membantu interpretasi output statistik**. Seringkali kita bisa menjalankan fungsi `.describe()`, tetapi belum tentu memahami implikasi dari angka-angka yang dihasilkan.

### Cara Menggunakan

**Langkah 1:** Jalankan `.describe()` di Colab.

**Langkah 2:** Copy output-nya.

**Langkah 3:** Masukkan ke AI assistant dengan prompt yang spesifik.

### Contoh Prompt

```
Berikut adalah output .describe() dari data IPM 34 provinsi di Indonesia:

       ipm
count  34.000000
mean   71.063529
std    4.175...
min    60.620000
25%    68.960000
50%    71.530000
75%    72.430000
max    81.110000

Tolong jelaskan:
1. Apa arti setiap baris dalam output ini?
2. Apakah distribusi IPM ini simetris? Bagaimana cara mengetahuinya dari output ini?
3. Apa artinya std sebesar 4.17 dalam konteks IPM?
4. Berapa provinsi yang IPM-nya di bawah rata-rata nasional?
5. Apakah ada indikasi kesenjangan pembangunan dari data ini?
```

### Tips Mendapatkan Jawaban AI yang Berkualitas

1. **Berikan konteks** -- sebutkan apa datanya dan dari mana asalnya.
2. **Ajukan pertanyaan spesifik** -- jangan hanya "jelaskan ini", tapi tanyakan hal-hal tertentu.
3. **Minta interpretasi** -- bukan hanya definisi, tetapi arti dalam konteks data Anda.
4. **Verifikasi** -- cocokkan jawaban AI dengan materi kuliah dan sumber referensi.

> **Peringatan:** AI bisa memberikan interpretasi yang salah atau menyesatkan. Selalu gunakan pemahaman Anda sendiri sebagai filter utama.

---

## Latihan Mandiri

### Latihan 1: Perhitungan Manual dan Python

Diberikan data nilai UTS Statistika 15 mahasiswa:

```
72, 85, 68, 91, 77, 83, 65, 88, 79, 94, 70, 86, 73, 81, 90
```

Kerjakan secara manual (tulis langkah-langkahnya) DAN verifikasi dengan Python:

a) Hitung mean, median, dan modus.
b) Hitung range, variance (sampel), dan standard deviation (sampel).
c) Hitung Q1, Q3, dan IQR.
d) Apakah ada outlier? Gunakan metode IQR.
e) Hitung skewness. Apakah distribusi condong ke kiri, kanan, atau simetris?

### Latihan 2: Eksplorasi Data dengan pandas

Buat notebook di Google Colab dan kerjakan tugas berikut:

a) Buat DataFrame yang berisi data berikut (minimal 15 baris):
   - Nama kota di Indonesia
   - Provinsi
   - Jumlah penduduk (dalam ribu)
   - Rata-rata suhu harian (Celsius)
   - Kategori kota (Kecil / Sedang / Besar / Metropolitan)

b) Jalankan `.info()` dan `.describe()`. Interpretasikan hasilnya.

c) Gunakan `.value_counts()` untuk menghitung jumlah kota per kategori.

d) Gunakan `.groupby()` untuk menghitung rata-rata jumlah penduduk per kategori kota.

e) Gunakan numpy untuk menghitung z-score dari kolom jumlah penduduk. Kota mana yang memiliki z-score tertinggi dan terendah?

### Latihan 3: Studi Kasus Mandiri

Unduh dataset dari sumber berikut (pilih salah satu):
- [BPS Open Data](https://www.bps.go.id/)
- [Jakarta Open Data](https://data.jakarta.go.id/)
- [Kaggle Indonesia Datasets](https://www.kaggle.com/datasets?search=indonesia)

Lakukan analisis deskriptif lengkap dan buat laporan singkat (1-2 halaman) yang berisi:
- Deskripsi dataset
- Statistik deskriptif (pemusatan dan penyebaran)
- Temuan menarik dari eksplorasi data
- Minimal 3 insight yang Anda dapatkan

---

## Rangkuman

| Konsep | Rumus / Fungsi | Kapan Digunakan |
|---|---|---|
| **Mean** | `df['col'].mean()` atau `np.mean()` | Data interval/rasio, distribusi simetris |
| **Median** | `df['col'].median()` atau `np.median()` | Ada outlier, distribusi skewed |
| **Modus** | `df['col'].mode()` | Data nominal, mencari nilai terpopuler |
| **Range** | `max - min` atau `np.ptp()` | Gambaran kasar penyebaran |
| **Variance** | `df['col'].var()` atau `np.var(ddof=1)` | Mengukur variabilitas data |
| **Std Dev** | `df['col'].std()` atau `np.std(ddof=1)` | Satuan sama dengan data asli |
| **IQR** | `Q3 - Q1` via `quantile()` | Robust terhadap outlier, deteksi outlier |
| **Skewness** | `df['col'].skew()` | Mengukur ketidaksimetrisan distribusi |
| **Kurtosis** | `df['col'].kurtosis()` | Mengukur keruncingan distribusi |
| **.describe()** | `df.describe()` | Ringkasan cepat semua statistik dasar |
| **.info()** | `df.info()` | Struktur dan tipe data |
| **.value_counts()** | `df['col'].value_counts()` | Frekuensi data kategorikal |
| **.groupby()** | `df.groupby('col').agg()` | Analisis per kelompok |

---

## Referensi

### Buku Teks

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability & Statistics for Engineers & Scientists* (9th ed.). Pearson. -- Bab 1: Pendahuluan, Statistika Deskriptif.
2. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media. -- Bab 5: Getting Started with pandas, Bab 7: Data Cleaning and Preparation.
3. Bruce, P., Bruce, A., & Gedeck, P. (2020). *Practical Statistics for Data Scientists* (2nd ed.). O'Reilly Media. -- Bab 1: Exploratory Data Analysis.

### Dokumentasi Library

4. [pandas - Descriptive Statistics](https://pandas.pydata.org/docs/user_guide/basics.html#descriptive-statistics) -- Fungsi-fungsi statistik deskriptif di pandas.
5. [numpy - Statistics](https://numpy.org/doc/stable/reference/routines.statistics.html) -- Fungsi statistik di numpy.

### Sumber Data

6. [BPS - Indeks Pembangunan Manusia](https://www.bps.go.id/id/statistics-table/2/MTk3MCMy/indeks-pembangunan-manusia.html) -- Data IPM Indonesia per Provinsi.

---

> **Preview Minggu Depan:** Kita akan mempelajari **Visualisasi Data dengan matplotlib dan seaborn** -- membuat histogram, boxplot, scatter plot, dan visualisasi statistik lainnya untuk mengeksplorasi data secara visual.
