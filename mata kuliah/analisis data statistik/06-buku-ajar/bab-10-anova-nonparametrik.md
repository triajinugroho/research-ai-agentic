# BAB 10: ANOVA DAN UJI NON-PARAMETRIK

**Tri Aji Nugroho, S.T., M.T.**
Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-6.1 | Menjelaskan konsep ANOVA dan mengapa diperlukan untuk membandingkan lebih dari dua kelompok | C2 |
| CPMK-6.2 | Melaksanakan one-way ANOVA, memeriksa asumsi, dan menginterpretasi F-statistic serta p-value | C3 |
| CPMK-6.3 | Melakukan post-hoc test (Tukey HSD, Bonferroni) untuk mengidentifikasi pasangan kelompok yang berbeda | C4 |
| CPMK-6.4 | Menerapkan uji non-parametrik (Mann-Whitney U, Wilcoxon signed-rank, Kruskal-Wallis) ketika asumsi parametrik tidak terpenuhi | C4 |
| CPMK-6.5 | Menganalisis karakteristik data untuk memilih uji statistik yang tepat menggunakan decision tree | C4 |

---

## 10.1 Mengapa Perlu Membandingkan Lebih dari Dua Kelompok?

### 10.1.1 Keterbatasan Multiple t-Test

Di bab sebelumnya, kita telah mempelajari uji-t untuk membandingkan dua kelompok. Namun, bagaimana jika kita ingin membandingkan **tiga kelompok atau lebih** sekaligus?

Misalnya, seorang peneliti di laboratorium Informatika UAI ingin membandingkan waktu eksekusi (*execution time*) dari **3 algoritma sorting**: Bubble Sort, Merge Sort, dan Quick Sort pada dataset berukuran sama. Pendekatan naif adalah melakukan t-test berpasangan:
- Bubble Sort vs Merge Sort
- Bubble Sort vs Quick Sort
- Merge Sort vs Quick Sort

Itu memerlukan **3 kali t-test** untuk 3 kelompok. Secara umum, untuk *k* kelompok diperlukan C(k,2) = k(k-1)/2 perbandingan:

| Jumlah Kelompok (k) | Jumlah t-test | P(min. 1 false positive) |
|---------------------|---------------|--------------------------|
| 3 | 3 | 14.3% |
| 4 | 6 | 26.5% |
| 5 | 10 | 40.1% |
| 6 | 15 | 53.7% |
| 10 | 45 | 90.1% |

**Masalah utama: Inflasi Error Type I**

Setiap t-test memiliki risiko *false positive* sebesar alpha = 0.05 (5%). Ketika kita melakukan banyak t-test secara bersamaan, probabilitas mendapatkan **minimal satu** false positive meningkat drastis:

```
P(minimal 1 false positive) = 1 - (1 - alpha)^k

Untuk 6 perbandingan:
P = 1 - (1 - 0.05)^6 = 1 - (0.95)^6 = 0.265 = 26.5%
```

Artinya, ada kemungkinan **26.5%** kita salah menyimpulkan ada perbedaan padahal sebenarnya tidak ada. Ini jauh dari tingkat 5% yang kita inginkan.

> "Doing multiple t-tests is like rolling a die multiple times — the more you roll, the more likely you'll get a 'lucky' result that means nothing."
> — Andy Field, *Discovering Statistics*

**Solusi: ANOVA** -- satu uji yang membandingkan **semua kelompok sekaligus** sambil mengendalikan error Type I pada level alpha yang ditentukan.

### 10.1.2 Aplikasi dalam Informatika

Situasi perbandingan lebih dari dua kelompok sangat sering dijumpai dalam informatika:

| Konteks | Kelompok yang Dibandingkan | Variabel Dependen |
|---------|---------------------------|-------------------|
| Evaluasi algoritma | 3+ algoritma sorting/searching | Waktu eksekusi (ms) |
| A/B/C testing | 3+ desain UI/UX | Conversion rate, task completion time |
| Perbandingan model ML | 3+ model klasifikasi | Accuracy, F1-score |
| Analisis performa server | 3+ konfigurasi server | Response time, throughput |
| Evaluasi metode pembelajaran | 3+ metode pengajaran | Nilai ujian mahasiswa |

---

## 10.2 One-Way ANOVA: Konsep dan Teori

### 10.2.1 Definisi

**ANOVA** (*Analysis of Variance*) adalah metode statistik yang menguji apakah **rata-rata** dari tiga kelompok atau lebih **berbeda secara signifikan**. Meskipun namanya "Analysis of *Variance*," yang sesungguhnya diuji adalah **perbedaan rata-rata** -- dengan cara menganalisis sumber-sumber variasi dalam data.

**Hipotesis:**
- **H_0:** mu_1 = mu_2 = mu_3 = ... = mu_k (semua rata-rata kelompok sama)
- **H_1:** Minimal satu rata-rata kelompok berbeda dari yang lain

> **Penting:** H_1 tidak menyatakan bahwa *semua* kelompok berbeda. H_1 hanya menyatakan bahwa *setidaknya satu pasang* kelompok memiliki rata-rata yang berbeda.

### 10.2.2 Ide Dasar: Dekomposisi Variansi

Ide kunci ANOVA adalah **memecah total variasi** dalam data menjadi dua komponen:

```
TOTAL VARIASI DALAM DATA
============================================================

  ┌──────────────────────────────────────────────────────┐
  │                  SS_Total (SST)                      │
  │          Total Sum of Squares                        │
  │    Seberapa tersebar seluruh data dari grand mean    │
  └──────────────────────┬───────────────────────────────┘
                         │
            ┌────────────┴────────────┐
            │                         │
  ┌─────────▼──────────┐   ┌─────────▼──────────┐
  │   SS_Between (SSB)  │   │   SS_Within (SSW)   │
  │   Variasi ANTAR     │   │   Variasi DALAM     │
  │   kelompok          │   │   kelompok           │
  │                     │   │                      │
  │   Disebabkan oleh   │   │   Disebabkan oleh    │
  │   perbedaan rata-   │   │   variasi alami      │
  │   rata kelompok     │   │   (random error)     │
  └─────────────────────┘   └──────────────────────┘

  SST = SSB + SSW
```

- **SSB (Sum of Squares Between):** Mengukur seberapa jauh rata-rata tiap kelompok dari rata-rata keseluruhan (*grand mean*). Jika kelompok-kelompok memang berbeda, SSB akan besar.
- **SSW (Sum of Squares Within):** Mengukur seberapa tersebar data di dalam masing-masing kelompok. Ini mewakili variasi acak (noise) yang tidak terkait dengan perbedaan kelompok.

**Analogi sederhana:** Bayangkan kelas A, B, dan C mengikuti ujian yang sama. SSB mengukur perbedaan nilai rata-rata *antar kelas*, sedangkan SSW mengukur variasi nilai *di dalam setiap kelas*. Jika perbedaan antar kelas jauh lebih besar daripada variasi dalam kelas, maka kelas-kelas tersebut memang berbeda.

### 10.2.3 Rumus ANOVA

**Sum of Squares:**

```
SST = Sigma_{i=1}^{k} Sigma_{j=1}^{n_i} (x_{ij} - x_bar_grand)^2

SSB = Sigma_{i=1}^{k} n_i * (x_bar_i - x_bar_grand)^2

SSW = Sigma_{i=1}^{k} Sigma_{j=1}^{n_i} (x_{ij} - x_bar_i)^2
```

Di mana:
- x_{ij} = observasi ke-j dari kelompok ke-i
- x_bar_i = rata-rata kelompok ke-i
- x_bar_grand = rata-rata keseluruhan (grand mean)
- n_i = jumlah observasi dalam kelompok ke-i
- k = jumlah kelompok
- N = jumlah total observasi

**Mean Squares dan F-Statistic:**

```
              SSB             SSW
MSB = ─────────────   MSW = ─────────────
           k - 1              N - k

              MSB     Variasi antar kelompok
F-stat = ───────── = ──────────────────────────
              MSW     Variasi dalam kelompok
```

**Interpretasi F-statistic:**
- F mendekati 1 --> variasi antar kelompok sebanding dengan variasi dalam kelompok --> tidak ada perbedaan signifikan
- F jauh lebih besar dari 1 --> variasi antar kelompok jauh melebihi variasi dalam kelompok --> kemungkinan ada perbedaan signifikan

### 10.2.4 Tabel ANOVA

Hasil ANOVA biasanya disajikan dalam tabel standar:

| Sumber Variasi | Sum of Squares (SS) | df | Mean Square (MS) | F | p-value |
|---------------|--------------------|----|------------------|---|---------|
| Between (Antar kelompok) | SSB | k - 1 | MSB = SSB/(k-1) | MSB/MSW | P(F > F_obs) |
| Within (Dalam kelompok) | SSW | N - k | MSW = SSW/(N-k) | | |
| Total | SST | N - 1 | | | |

**Keputusan:**
- Jika p-value < alpha (biasanya 0.05) --> **Tolak H_0** --> minimal satu kelompok berbeda
- Jika p-value >= alpha --> **Gagal tolak H_0** --> tidak cukup bukti adanya perbedaan

### 10.2.5 Asumsi ANOVA

ANOVA valid jika tiga asumsi berikut terpenuhi:

| Asumsi | Penjelasan | Cara Cek Visual | Uji Formal |
|--------|-----------|-----------------|------------|
| **Normalitas** | Data dalam setiap kelompok berdistribusi normal | Histogram, Q-Q plot | Shapiro-Wilk test per kelompok |
| **Homogenitas variansi** | Variansi semua kelompok kira-kira sama | Box plot (lebar box mirip) | Levene's test |
| **Independensi** | Observasi saling independen satu sama lain | Desain penelitian | -- (dipastikan dari cara pengambilan data) |

**Jika asumsi dilanggar:**
- Normalitas dilanggar ringan + sampel besar (n > 30 per kelompok) --> ANOVA masih cukup *robust*
- Homogenitas variansi dilanggar --> Gunakan **Welch's ANOVA**
- Asumsi dilanggar parah --> Gunakan alternatif non-parametrik (**Kruskal-Wallis**)

### 10.2.6 Effect Size: Eta-Squared

Selain p-value, penting untuk melaporkan **effect size** yang mengukur besarnya efek:

```
         SSB
eta^2 = ─────
         SST
```

| Nilai eta^2 | Interpretasi |
|-------------|-------------|
| < 0.01 | Negligible (sangat kecil) |
| 0.01 - 0.06 | Kecil |
| 0.06 - 0.14 | Sedang |
| > 0.14 | Besar |

> **Tips:** p-value hanya memberi tahu *apakah* ada perbedaan, sedangkan effect size memberi tahu *seberapa besar* perbedaannya. Dengan sampel yang sangat besar, perbedaan kecil pun bisa signifikan secara statistik meskipun tidak bermakna secara praktis.

---

## 10.3 Post-Hoc Tests

### 10.3.1 Mengapa Perlu Post-Hoc?

ANOVA hanya menjawab: "Apakah **ada** perbedaan di antara kelompok-kelompok?" Jika hasilnya signifikan, kita masih belum tahu **kelompok mana** yang berbeda dari kelompok mana. Post-hoc test menjawab pertanyaan lanjutan ini.

```
                       ANOVA
                         │
                 ┌───────┴───────┐
                 │               │
          p < 0.05           p >= 0.05
          (Signifikan)       (Tidak Signifikan)
                 │               │
                 ▼               ▼
          POST-HOC TEST      BERHENTI
          (kelompok mana     (tidak ada bukti
           yang berbeda?)     perbedaan)
```

### 10.3.2 Tukey's Honestly Significant Difference (HSD)

**Tukey's HSD** adalah post-hoc test yang paling umum digunakan. Uji ini membandingkan **setiap pasangan kelompok** sambil mengontrol error Type I secara keseluruhan (*family-wise error rate*).

**Kelebihan:**
- Mengontrol family-wise error rate
- Memberikan confidence interval untuk setiap perbedaan
- Cocok jika ingin membandingkan *semua* pasangan kelompok

**Output Tukey's HSD memberikan:**
- Perbedaan rata-rata antar setiap pasangan kelompok
- p-value untuk setiap perbandingan (sudah dikoreksi)
- Confidence interval untuk perbedaan rata-rata
- Keputusan reject/fail to reject untuk setiap pasangan

### 10.3.3 Koreksi Bonferroni

Alternatif yang lebih konservatif adalah **koreksi Bonferroni**, yang membagi tingkat signifikansi alpha dengan jumlah perbandingan:

```
alpha_adjusted = alpha / m

Di mana m = jumlah perbandingan = k(k-1)/2
```

Contoh: Untuk 4 kelompok (6 perbandingan):
```
alpha_adjusted = 0.05 / 6 = 0.0083
```

Setiap perbandingan individual harus memiliki p-value < 0.0083 untuk dianggap signifikan.

| Metode | Kelebihan | Kekurangan |
|--------|-----------|------------|
| **Tukey HSD** | Power lebih tinggi, cocok untuk semua pasangan | Hanya untuk perbandingan semua pasangan |
| **Bonferroni** | Sederhana, fleksibel, cocok untuk subset perbandingan | Sangat konservatif (power rendah) jika banyak perbandingan |

---

## 10.4 Kapan Parametrik vs Non-Parametrik?

### 10.4.1 Uji Parametrik vs Non-Parametrik

**Uji parametrik** (seperti t-test dan ANOVA) mengasumsikan distribusi tertentu (biasanya normal) pada data. **Uji non-parametrik** tidak memerlukan asumsi distribusi tertentu -- uji ini bekerja berdasarkan **rank (peringkat)** data, bukan nilai mentah.

```
┌────────────────────────────────────────────────────────────┐
│              PARAMETRIK vs NON-PARAMETRIK                   │
│                                                             │
│  PARAMETRIK                     NON-PARAMETRIK              │
│  ─────────                      ──────────────              │
│  Asumsi: normalitas             Tidak perlu asumsi          │
│  Bekerja pada: nilai data       Bekerja pada: rank data     │
│  Power: lebih tinggi            Power: lebih rendah          │
│  Cocok: data kontinu, normal    Cocok: ordinal, skewed,     │
│                                   sampel kecil, outlier     │
│                                                             │
│  Contoh:                        Contoh:                     │
│  - t-test                       - Mann-Whitney U            │
│  - Paired t-test                - Wilcoxon signed-rank      │
│  - One-way ANOVA                - Kruskal-Wallis            │
└────────────────────────────────────────────────────────────┘
```

### 10.4.2 Kapan Menggunakan Non-Parametrik?

Gunakan uji non-parametrik ketika:

1. **Data berskala ordinal** -- misalnya skala Likert (1-5), rating kepuasan
2. **Distribusi sangat skewed** -- misalnya data pendapatan, waktu tunggu
3. **Terdapat outlier ekstrem** -- yang dapat memengaruhi rata-rata secara signifikan
4. **Sampel kecil** (n < 15-20 per kelompok) -- sehingga normalitas sulit diverifikasi
5. **Uji normalitas gagal** -- Shapiro-Wilk test menunjukkan p < 0.05

### 10.4.3 Tabel Padanan Uji Parametrik dan Non-Parametrik

| Situasi | Uji Parametrik | Uji Non-Parametrik | Yang Dibandingkan |
|---------|---------------|--------------------|--------------------|
| 2 kelompok independen | Independent t-test | **Mann-Whitney U** | Rata-rata / Distribusi |
| 2 kelompok berpasangan | Paired t-test | **Wilcoxon signed-rank** | Rata-rata selisih / Distribusi selisih |
| >2 kelompok independen | One-way ANOVA | **Kruskal-Wallis** | Rata-rata / Distribusi |
| Post-hoc parametrik | Tukey HSD | -- | Pasangan kelompok |
| Post-hoc non-parametrik | -- | **Dunn's test** | Pasangan kelompok |

---

## 10.5 Mann-Whitney U Test

### 10.5.1 Konsep

**Mann-Whitney U test** (juga dikenal sebagai *Wilcoxon rank-sum test*) adalah alternatif non-parametrik untuk **independent two-sample t-test**. Uji ini membandingkan **distribusi** dua kelompok independen berdasarkan peringkat (*rank*).

**Hipotesis:**
- **H_0:** Distribusi kedua kelompok sama
- **H_1:** Distribusi kedua kelompok berbeda

### 10.5.2 Cara Kerja

Langkah-langkah Mann-Whitney U test:

1. **Gabungkan** semua data dari kedua kelompok
2. **Berikan rank** (peringkat) dari yang terkecil ke terbesar
3. **Jumlahkan rank** untuk masing-masing kelompok (R_1 dan R_2)
4. **Hitung U-statistic:**

```
U_1 = n_1 * n_2 + n_1(n_1 + 1)/2 - R_1
U_2 = n_1 * n_2 + n_2(n_2 + 1)/2 - R_2

U = min(U_1, U_2)
```

5. Bandingkan U dengan distribusi null untuk mendapatkan p-value

**Contoh sederhana:**

```
Kelompok A (waktu respons server lama, ms): 120, 150, 180, 200
Kelompok B (waktu respons server baru, ms): 80, 95, 110, 130

Gabungan dan rank:
Nilai:  80  95  110  120  130  150  180  200
Rank:    1   2    3    4    5    6    7    8
Grup:    B   B    B    A    B    A    A    A

R_A = 4 + 6 + 7 + 8 = 25
R_B = 1 + 2 + 3 + 5 = 11

U_A = 4*4 + 4*5/2 - 25 = 16 + 10 - 25 = 1
U_B = 4*4 + 4*5/2 - 11 = 16 + 10 - 11 = 15

U = min(1, 15) = 1  (U kecil --> distribusi berbeda)
```

### 10.5.3 Kapan Menggunakan Mann-Whitney U?

- Data ordinal (misalnya skala Likert)
- Data numerik tetapi **tidak berdistribusi normal**
- Terdapat **outlier** yang memengaruhi rata-rata
- **Sampel kecil** sehingga normalitas sulit diverifikasi
- Sebagai **robustness check** terhadap hasil t-test

---

## 10.6 Wilcoxon Signed-Rank Test

### 10.6.1 Konsep

**Wilcoxon signed-rank test** adalah alternatif non-parametrik untuk **paired t-test**. Uji ini digunakan ketika kita memiliki dua pengukuran dari subjek yang **sama** (data berpasangan), tetapi asumsi normalitas tidak terpenuhi.

**Hipotesis:**
- **H_0:** Median selisih berpasangan = 0 (tidak ada perbedaan)
- **H_1:** Median selisih berpasangan != 0 (ada perbedaan)

### 10.6.2 Cara Kerja

1. Hitung **selisih** (d_i) untuk setiap pasangan
2. Ambil **nilai absolut** selisih |d_i| dan buang yang bernilai 0
3. Berikan **rank** pada |d_i|
4. Berikan **tanda** (+/-) pada rank sesuai tanda selisih asli
5. Jumlahkan rank positif (W+) dan rank negatif (W-)
6. W = min(W+, W-), bandingkan dengan distribusi null

**Contoh penggunaan:** Membandingkan waktu respons mahasiswa sebelum dan sesudah mengikuti pelatihan typing, mengukur kepuasan pengguna sebelum dan sesudah update aplikasi, atau mengevaluasi performa model sebelum dan sesudah fine-tuning.

---

## 10.7 Kruskal-Wallis Test

### 10.7.1 Konsep

**Kruskal-Wallis test** adalah alternatif non-parametrik untuk **one-way ANOVA**. Uji ini membandingkan distribusi dari **tiga kelompok atau lebih** menggunakan peringkat data.

**Hipotesis:**
- **H_0:** Distribusi semua kelompok sama
- **H_1:** Minimal satu kelompok memiliki distribusi yang berbeda

### 10.7.2 Cara Kerja

Kruskal-Wallis menghitung H-statistic:

```
          12            k    R_i^2
H = ──────────── * ( Sigma ─────── ) - 3(N + 1)
     N(N + 1)         i=1    n_i
```

Di mana:
- R_i = jumlah rank dalam kelompok ke-i
- n_i = jumlah observasi dalam kelompok ke-i
- N = jumlah total observasi
- k = jumlah kelompok

H-statistic mengikuti distribusi chi-square dengan df = k - 1 (untuk sampel besar).

### 10.7.3 Post-Hoc Setelah Kruskal-Wallis

Jika Kruskal-Wallis signifikan, gunakan **Dunn's test** (dengan koreksi Bonferroni atau koreksi lainnya) untuk mengetahui kelompok mana yang berbeda:

```python
# Menggunakan library scikit-posthocs
import scikit_posthocs as sp
dunn_result = sp.posthoc_dunn(data, val_col='nilai', group_col='kelompok',
                               p_adjust='bonferroni')
```

---

## 10.8 Decision Tree: Memilih Uji yang Tepat

### 10.8.1 Flowchart Pemilihan Uji Statistik

Memilih uji yang tepat adalah keterampilan penting. Berikut decision tree yang komprehensif:

```
MEMILIH UJI STATISTIK UNTUK PERBANDINGAN KELOMPOK
===================================================

Berapa kelompok yang dibandingkan?
│
├── 2 KELOMPOK
│   │
│   ├── Data BERPASANGAN (subjek sama)?
│   │   │
│   │   ├── YA (paired)
│   │   │   ├── Data normal?
│   │   │   │   ├── YA ──→ Paired t-test
│   │   │   │   └── TIDAK ──→ Wilcoxon Signed-Rank Test
│   │   │   │
│   │   └── TIDAK (independen)
│   │       ├── Data normal + variansi homogen?
│   │       │   ├── YA ──→ Independent t-test
│   │       │   ├── Normal tapi variansi beda ──→ Welch's t-test
│   │       │   └── TIDAK normal ──→ Mann-Whitney U Test
│   │
├── 3+ KELOMPOK
│   │
│   ├── Data BERPASANGAN (repeated measures)?
│   │   ├── YA
│   │   │   ├── Data normal ──→ Repeated Measures ANOVA
│   │   │   └── TIDAK normal ──→ Friedman Test
│   │   │
│   └── TIDAK (independen)
│       ├── Data normal + variansi homogen?
│       │   ├── YA ──→ One-Way ANOVA
│       │   │          (jika signifikan ──→ Tukey HSD)
│       │   ├── Normal tapi variansi beda ──→ Welch's ANOVA
│       │   └── TIDAK normal / ordinal ──→ Kruskal-Wallis
│       │                                  (jika signifikan ──→ Dunn's Test)
```

### 10.8.2 Checklist Sebelum Memilih Uji

Sebelum menjalankan uji statistik, jawab pertanyaan berikut:

| No | Pertanyaan | Implikasi |
|----|-----------|-----------|
| 1 | Berapa jumlah kelompok? | 2: t-test/Mann-Whitney; 3+: ANOVA/Kruskal-Wallis |
| 2 | Apakah data berpasangan atau independen? | Berpasangan: paired test; Independen: independent test |
| 3 | Apa skala pengukuran data? | Nominal/Ordinal: non-parametrik; Interval/Rasio: bisa parametrik |
| 4 | Apakah data berdistribusi normal? | Ya: parametrik; Tidak: non-parametrik |
| 5 | Apakah variansi antar kelompok homogen? | Ya: ANOVA standar; Tidak: Welch's atau non-parametrik |
| 6 | Berapa besar sampel per kelompok? | Kecil (n < 20): hati-hati asumsi; Besar: CLT membantu |

---

## 10.9 Implementasi Python

### 10.9.1 Persiapan dan Import Library

```python
# Library yang dibutuhkan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Pengaturan tampilan
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
np.random.seed(2025)

print("Library berhasil dimuat!")
```

### 10.9.2 One-Way ANOVA Lengkap: Perbandingan Algoritma Sorting

```python
# ============================================================
# STUDI KASUS 1: Perbandingan Waktu Eksekusi 3 Algoritma Sorting
# ============================================================

np.random.seed(2025)

# Simulasi waktu eksekusi (milidetik) untuk 10.000 elemen
bubble_sort = np.random.normal(450, 50, 30)    # Bubble Sort: lambat
merge_sort  = np.random.normal(120, 20, 30)    # Merge Sort: cepat
quick_sort  = np.random.normal(100, 25, 30)    # Quick Sort: paling cepat

# Gabungkan ke DataFrame
data_sorting = pd.DataFrame({
    'waktu_ms': np.concatenate([bubble_sort, merge_sort, quick_sort]),
    'algoritma': (['Bubble Sort'] * 30 +
                  ['Merge Sort'] * 30 +
                  ['Quick Sort'] * 30)
})

# Statistik deskriptif per kelompok
print("=" * 60)
print("STUDI KASUS: Perbandingan Algoritma Sorting")
print("=" * 60)
print("\n1. Statistik Deskriptif (waktu eksekusi dalam ms):")
ringkasan = data_sorting.groupby('algoritma')['waktu_ms'].agg(
    ['count', 'mean', 'median', 'std', 'min', 'max']
).round(2)
ringkasan.columns = ['N', 'Mean', 'Median', 'Std', 'Min', 'Max']
print(ringkasan)
```

```python
# Visualisasi
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Box plot
sns.boxplot(data=data_sorting, x='algoritma', y='waktu_ms', ax=axes[0],
            palette='Set2', order=['Bubble Sort', 'Merge Sort', 'Quick Sort'])
axes[0].set_xlabel('Algoritma')
axes[0].set_ylabel('Waktu Eksekusi (ms)')
axes[0].set_title('Box Plot: Waktu Eksekusi per Algoritma')
axes[0].grid(True, alpha=0.3, axis='y')

# Violin plot
sns.violinplot(data=data_sorting, x='algoritma', y='waktu_ms', ax=axes[1],
               palette='Set2', order=['Bubble Sort', 'Merge Sort', 'Quick Sort'],
               inner='box')
axes[1].set_xlabel('Algoritma')
axes[1].set_ylabel('Waktu Eksekusi (ms)')
axes[1].set_title('Violin Plot: Distribusi Waktu Eksekusi')
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()
```

```python
# ============================================================
# LANGKAH 1: Cek Asumsi
# ============================================================

algo_list = ['Bubble Sort', 'Merge Sort', 'Quick Sort']
kelompok = [data_sorting[data_sorting['algoritma'] == a]['waktu_ms']
            for a in algo_list]

# Asumsi 1: Normalitas (Shapiro-Wilk test)
print("\n2. Cek Asumsi:")
print("   a) Normalitas (Shapiro-Wilk Test):")
semua_normal = True
for a, d in zip(algo_list, kelompok):
    stat, p = stats.shapiro(d)
    normal = "Normal" if p > 0.05 else "TIDAK Normal"
    if p <= 0.05:
        semua_normal = False
    print(f"      {a:15s}: W = {stat:.4f}, p = {p:.4f} --> {normal}")

# Asumsi 2: Homogenitas variansi (Levene's Test)
stat_lev, p_lev = stats.levene(*kelompok)
print(f"\n   b) Homogenitas Variansi (Levene's Test):")
print(f"      Levene's statistic = {stat_lev:.4f}")
print(f"      p-value = {p_lev:.4f}")
print(f"      Variansi homogen? {'Ya' if p_lev > 0.05 else 'TIDAK'}")

# Keputusan
print(f"\n   Keputusan:")
if semua_normal and p_lev > 0.05:
    print("   --> Semua asumsi terpenuhi. Gunakan One-Way ANOVA.")
elif not semua_normal:
    print("   --> Normalitas tidak terpenuhi. Pertimbangkan Kruskal-Wallis.")
else:
    print("   --> Variansi tidak homogen. Pertimbangkan Welch's ANOVA.")
```

```python
# ============================================================
# LANGKAH 2: One-Way ANOVA
# ============================================================

f_stat, p_anova = stats.f_oneway(*kelompok)

print("\n3. One-Way ANOVA:")
print(f"   F-statistic = {f_stat:.4f}")
print(f"   p-value     = {p_anova:.8f}")

if p_anova < 0.05:
    print(f"   Keputusan: TOLAK H_0 (p < 0.05)")
    print(f"   Kesimpulan: Ada perbedaan signifikan waktu eksekusi antar algoritma.")
    print(f"   --> Lanjut ke post-hoc test.")
else:
    print(f"   Keputusan: GAGAL TOLAK H_0 (p >= 0.05)")
    print(f"   Kesimpulan: Tidak cukup bukti adanya perbedaan.")

# Effect size (Eta-squared)
grand_mean = data_sorting['waktu_ms'].mean()
ss_between = sum(len(g) * (g.mean() - grand_mean)**2 for g in kelompok)
ss_total = sum((data_sorting['waktu_ms'] - grand_mean)**2)
eta_sq = ss_between / ss_total

print(f"\n   Effect size (eta^2) = {eta_sq:.4f}")
if eta_sq < 0.06:
    print("   Interpretasi: Effect size kecil")
elif eta_sq < 0.14:
    print("   Interpretasi: Effect size sedang")
else:
    print("   Interpretasi: Effect size besar")
```

```python
# ============================================================
# LANGKAH 3: Post-Hoc Test (Tukey's HSD)
# ============================================================

tukey = pairwise_tukeyhsd(
    endog=data_sorting['waktu_ms'],
    groups=data_sorting['algoritma'],
    alpha=0.05
)

print("\n4. Post-Hoc: Tukey's HSD:")
print(tukey)

# Visualisasi Tukey's HSD
fig = tukey.plot_simultaneous(figsize=(8, 5))
plt.xlabel('Waktu Eksekusi (ms)')
plt.title('Tukey HSD: Confidence Intervals per Algoritma')
plt.tight_layout()
plt.show()

# Interpretasi
print("\nInterpretasi:")
print("- Pasangan dengan 'reject=True': perbedaan signifikan.")
print("- Pasangan dengan 'reject=False': tidak berbeda signifikan.")
```

### 10.9.3 Mann-Whitney U Test

```python
# ============================================================
# UJI NON-PARAMETRIK: Mann-Whitney U Test
# ============================================================

# Contoh: Membandingkan response time dua desain UI
# Data tidak normal (skewed) karena beberapa user sangat lambat (outlier)

np.random.seed(42)
ui_lama = np.random.exponential(scale=5.0, size=25) + 3   # Skewed
ui_baru = np.random.exponential(scale=3.5, size=25) + 2   # Skewed

print("=" * 60)
print("Mann-Whitney U Test: Response Time Dua Desain UI")
print("=" * 60)

# Cek normalitas
_, p_lama = stats.shapiro(ui_lama)
_, p_baru = stats.shapiro(ui_baru)
print(f"\nNormalitas UI Lama: p = {p_lama:.4f} --> {'Normal' if p_lama > 0.05 else 'TIDAK Normal'}")
print(f"Normalitas UI Baru: p = {p_baru:.4f} --> {'Normal' if p_baru > 0.05 else 'TIDAK Normal'}")
print("Data tidak normal --> Gunakan Mann-Whitney U test")

# Mann-Whitney U Test
stat_mw, p_mw = stats.mannwhitneyu(ui_lama, ui_baru, alternative='two-sided')

print(f"\nHasil Mann-Whitney U Test:")
print(f"   U-statistic = {stat_mw:.2f}")
print(f"   p-value     = {p_mw:.4f}")

if p_mw < 0.05:
    print(f"   Kesimpulan: Distribusi response time berbeda signifikan.")
    print(f"   Median UI Lama: {np.median(ui_lama):.2f}s")
    print(f"   Median UI Baru: {np.median(ui_baru):.2f}s")
    print(f"   --> UI baru memberikan response time yang lebih baik.")
else:
    print(f"   Kesimpulan: Tidak ada perbedaan signifikan.")
```

### 10.9.4 Wilcoxon Signed-Rank Test

```python
# ============================================================
# UJI NON-PARAMETRIK: Wilcoxon Signed-Rank Test
# ============================================================

# Contoh: Membandingkan kecepatan mengetik (WPM) mahasiswa
# sebelum dan sesudah pelatihan typing

np.random.seed(123)
n_mahasiswa = 20
wpm_sebelum = np.random.normal(45, 10, n_mahasiswa).astype(int)
# Sesudah pelatihan: sebagian besar meningkat, tapi tidak semua
peningkatan = np.random.exponential(scale=8, size=n_mahasiswa)
wpm_sesudah = (wpm_sebelum + peningkatan).astype(int)

print("=" * 60)
print("Wilcoxon Signed-Rank Test: Efektivitas Pelatihan Typing")
print("=" * 60)

# Tampilkan sebagian data
df_typing = pd.DataFrame({
    'Mahasiswa': [f'Mhs-{i+1:02d}' for i in range(n_mahasiswa)],
    'WPM_Sebelum': wpm_sebelum,
    'WPM_Sesudah': wpm_sesudah,
    'Selisih': wpm_sesudah - wpm_sebelum
})
print("\nData (5 pertama):")
print(df_typing.head().to_string(index=False))

# Cek normalitas selisih
selisih = wpm_sesudah - wpm_sebelum
_, p_norm = stats.shapiro(selisih)
print(f"\nNormalitas selisih: p = {p_norm:.4f} --> {'Normal' if p_norm > 0.05 else 'TIDAK Normal'}")

# Wilcoxon Signed-Rank Test
stat_w, p_w = stats.wilcoxon(wpm_sebelum, wpm_sesudah, alternative='two-sided')

print(f"\nHasil Wilcoxon Signed-Rank Test:")
print(f"   W-statistic = {stat_w:.2f}")
print(f"   p-value     = {p_w:.4f}")

if p_w < 0.05:
    print(f"   Kesimpulan: Terdapat perbedaan signifikan WPM sebelum dan sesudah pelatihan.")
    print(f"   Median sebelum: {np.median(wpm_sebelum):.0f} WPM")
    print(f"   Median sesudah: {np.median(wpm_sesudah):.0f} WPM")
else:
    print(f"   Kesimpulan: Tidak ada perbedaan signifikan.")
```

### 10.9.5 Kruskal-Wallis Test

```python
# ============================================================
# UJI NON-PARAMETRIK: Kruskal-Wallis Test
# ============================================================

# Contoh: Membandingkan rating kepuasan mahasiswa (skala 1-5)
# terhadap 3 platform LMS berbeda

np.random.seed(99)
# Data ordinal (skala Likert), tidak cocok untuk ANOVA
lms_moodle   = np.random.choice([1, 2, 3, 4, 5], size=25,
               p=[0.05, 0.10, 0.25, 0.35, 0.25])  # Cenderung puas
lms_canvas   = np.random.choice([1, 2, 3, 4, 5], size=25,
               p=[0.02, 0.08, 0.20, 0.40, 0.30])  # Lebih puas
lms_lokal    = np.random.choice([1, 2, 3, 4, 5], size=25,
               p=[0.15, 0.25, 0.30, 0.20, 0.10])  # Kurang puas

data_lms = pd.DataFrame({
    'rating': np.concatenate([lms_moodle, lms_canvas, lms_lokal]),
    'platform': (['Moodle'] * 25 + ['Canvas'] * 25 + ['LMS Lokal'] * 25)
})

print("=" * 60)
print("Kruskal-Wallis Test: Kepuasan Mahasiswa terhadap LMS")
print("=" * 60)

# Statistik deskriptif
print("\nDistribusi Rating per Platform:")
for platform in ['Moodle', 'Canvas', 'LMS Lokal']:
    subset = data_lms[data_lms['platform'] == platform]['rating']
    print(f"  {platform:10s}: Median = {np.median(subset):.0f}, "
          f"Mean = {np.mean(subset):.2f}, N = {len(subset)}")

# Kruskal-Wallis Test
grup_lms = [data_lms[data_lms['platform'] == p]['rating']
            for p in ['Moodle', 'Canvas', 'LMS Lokal']]

stat_kw, p_kw = stats.kruskal(*grup_lms)

print(f"\nHasil Kruskal-Wallis Test:")
print(f"   H-statistic = {stat_kw:.4f}")
print(f"   p-value     = {p_kw:.4f}")

if p_kw < 0.05:
    print(f"   Kesimpulan: Terdapat perbedaan signifikan kepuasan antar platform.")
    print(f"   --> Lanjut ke Dunn's test untuk post-hoc.")
else:
    print(f"   Kesimpulan: Tidak ada perbedaan signifikan.")
```

```python
# Post-Hoc: Dunn's Test
# Install jika belum: !pip install scikit-posthocs

import scikit_posthocs as sp

dunn_result = sp.posthoc_dunn(
    data_lms, val_col='rating', group_col='platform',
    p_adjust='bonferroni'
)

print("\nPost-Hoc: Dunn's Test (koreksi Bonferroni):")
print(dunn_result.round(4))

# Visualisasi heatmap p-values
plt.figure(figsize=(7, 5))
sns.heatmap(dunn_result, annot=True, fmt='.4f', cmap='RdYlGn_r',
            vmin=0, vmax=0.1, linewidths=0.5)
plt.title("Dunn's Test P-Values\n(Hijau = Tidak Signifikan, Merah = Signifikan)")
plt.tight_layout()
plt.show()

print("\nPasangan dengan p-value < 0.05 berbeda signifikan.")
```

### 10.9.6 Fungsi Decision Flowchart Otomatis

```python
def pilih_uji_statistik(data, kolom_nilai, kolom_grup, alpha=0.05):
    """
    Decision flowchart otomatis untuk memilih dan menjalankan
    uji statistik yang tepat.

    Parameters:
    -----------
    data : pd.DataFrame
    kolom_nilai : str -- nama kolom variabel dependen
    kolom_grup : str -- nama kolom variabel grup
    alpha : float -- level signifikansi (default 0.05)
    """
    print("=" * 60)
    print("DECISION FLOWCHART: Memilih Uji Statistik")
    print("=" * 60)

    grup_unik = data[kolom_grup].unique()
    n_grup = len(grup_unik)
    print(f"\nJumlah kelompok: {n_grup}")

    if n_grup < 2:
        print("Error: Minimal 2 kelompok diperlukan.")
        return

    # Cek normalitas semua grup
    normal = True
    print(f"\nCek Normalitas (Shapiro-Wilk, alpha = {alpha}):")
    for g in grup_unik:
        subset = data[data[kolom_grup] == g][kolom_nilai]
        stat, p = stats.shapiro(subset)
        status = "Normal" if p > alpha else "TIDAK Normal"
        if p <= alpha:
            normal = False
        print(f"  {g}: W = {stat:.4f}, p = {p:.4f} --> {status}")

    groups = [data[data[kolom_grup] == g][kolom_nilai] for g in grup_unik]

    # Cek homogenitas
    lev_stat, lev_p = stats.levene(*groups)
    homogen = lev_p > alpha
    print(f"\nCek Homogenitas (Levene's Test):")
    print(f"  Levene stat = {lev_stat:.4f}, p = {lev_p:.4f} --> "
          f"{'Homogen' if homogen else 'TIDAK Homogen'}")

    # Pilih uji
    print(f"\nUji yang Dipilih:")
    if n_grup == 2:
        if normal and homogen:
            print("  --> Independent t-test (normal + homogen)")
            stat, p = stats.ttest_ind(*groups)
            print(f"  t = {stat:.4f}, p = {p:.4f}")
        elif normal and not homogen:
            print("  --> Welch's t-test (normal + tidak homogen)")
            stat, p = stats.ttest_ind(*groups, equal_var=False)
            print(f"  t = {stat:.4f}, p = {p:.4f}")
        else:
            print("  --> Mann-Whitney U (tidak normal)")
            stat, p = stats.mannwhitneyu(*groups, alternative='two-sided')
            print(f"  U = {stat:.4f}, p = {p:.4f}")
    else:
        if normal and homogen:
            print("  --> One-Way ANOVA (normal + homogen)")
            stat, p = stats.f_oneway(*groups)
            print(f"  F = {stat:.4f}, p = {p:.4f}")
            if p < alpha:
                print("  --> Signifikan! Lanjut: Tukey HSD")
                tukey = pairwise_tukeyhsd(data[kolom_nilai],
                                          data[kolom_grup], alpha)
                print(tukey)
        elif normal and not homogen:
            print("  --> Welch's ANOVA / Kruskal-Wallis (tidak homogen)")
            stat, p = stats.kruskal(*groups)
            print(f"  H = {stat:.4f}, p = {p:.4f}")
        else:
            print("  --> Kruskal-Wallis (tidak normal)")
            stat, p = stats.kruskal(*groups)
            print(f"  H = {stat:.4f}, p = {p:.4f}")
            if p < alpha:
                print("  --> Signifikan! Lanjut: Dunn's test")

    print(f"\nHasil Akhir:")
    if p < alpha:
        print(f"  SIGNIFIKAN (p = {p:.4f} < {alpha})")
    else:
        print(f"  TIDAK SIGNIFIKAN (p = {p:.4f} >= {alpha})")
    print("=" * 60)

# Contoh penggunaan
pilih_uji_statistik(data_sorting, 'waktu_ms', 'algoritma')
```

---

## 10.10 Studi Kasus

### 10.10.1 Studi Kasus 1: Perbandingan Performa 3 Algoritma Sorting

**Konteks:** Tim pengembang di sebuah startup e-commerce Indonesia ingin memilih algoritma sorting terbaik untuk mengurutkan produk berdasarkan harga. Mereka menguji tiga algoritma (Bubble Sort, Merge Sort, Quick Sort) masing-masing 30 kali pada dataset berisi 10.000 produk.

```python
# ============================================================
# STUDI KASUS 1: Analisis Lengkap Algoritma Sorting
# ============================================================

np.random.seed(2025)

# Data waktu eksekusi (ms)
data_algo = pd.DataFrame({
    'waktu_ms': np.concatenate([
        np.random.normal(450, 50, 30),    # Bubble Sort
        np.random.normal(120, 20, 30),    # Merge Sort
        np.random.normal(100, 25, 30)     # Quick Sort
    ]),
    'algoritma': (['Bubble Sort'] * 30 +
                  ['Merge Sort'] * 30 +
                  ['Quick Sort'] * 30)
})

# Analisis lengkap menggunakan fungsi decision flowchart
pilih_uji_statistik(data_algo, 'waktu_ms', 'algoritma')

print("\n--- INTERPRETASI BISNIS ---")
print("Quick Sort memiliki waktu eksekusi tercepat (rata-rata ~100ms),")
print("diikuti Merge Sort (~120ms), dan Bubble Sort paling lambat (~450ms).")
print("Perbedaan ini sangat signifikan secara statistik (p << 0.05)")
print("dengan effect size besar (eta^2 > 0.14).")
print("\nRekomendasi: Gunakan Quick Sort untuk sorting produk,")
print("dengan Merge Sort sebagai fallback untuk worst-case scenarios.")
```

### 10.10.2 Studi Kasus 2: Evaluasi 3 Desain UI Aplikasi

**Konteks:** Tim UX di sebuah perusahaan fintech Indonesia (misalnya GoPay) ingin mengevaluasi tiga desain antarmuka untuk fitur transfer uang. Mereka mengukur **task completion time** (detik) dari 25 pengguna per desain.

```python
# ============================================================
# STUDI KASUS 2: Evaluasi 3 Desain UI
# ============================================================

np.random.seed(77)

# Task completion time (detik) -- sengaja dibuat skewed
desain_a = np.random.exponential(scale=8, size=25) + 10  # Desain lama
desain_b = np.random.exponential(scale=5, size=25) + 8   # Desain baru 1
desain_c = np.random.exponential(scale=6, size=25) + 7   # Desain baru 2

data_ui = pd.DataFrame({
    'waktu_detik': np.concatenate([desain_a, desain_b, desain_c]),
    'desain': (['Desain A (Lama)'] * 25 +
               ['Desain B (Baru 1)'] * 25 +
               ['Desain C (Baru 2)'] * 25)
})

print("=" * 60)
print("STUDI KASUS 2: Evaluasi Desain UI Fitur Transfer")
print("=" * 60)

# 1. Deskriptif
print("\n1. Statistik Deskriptif:")
for desain in ['Desain A (Lama)', 'Desain B (Baru 1)', 'Desain C (Baru 2)']:
    subset = data_ui[data_ui['desain'] == desain]['waktu_detik']
    print(f"   {desain}: Mean={subset.mean():.1f}s, "
          f"Median={subset.median():.1f}s, Std={subset.std():.1f}s")

# 2. Visualisasi
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.boxplot(data=data_ui, x='desain', y='waktu_detik', ax=axes[0],
            palette='pastel')
axes[0].set_title('Box Plot: Task Completion Time')
axes[0].set_xlabel('Desain UI')
axes[0].set_ylabel('Waktu (detik)')
axes[0].tick_params(axis='x', rotation=15)

sns.violinplot(data=data_ui, x='desain', y='waktu_detik', ax=axes[1],
               palette='pastel', inner='box')
axes[1].set_title('Violin Plot: Distribusi Waktu')
axes[1].set_xlabel('Desain UI')
axes[1].set_ylabel('Waktu (detik)')
axes[1].tick_params(axis='x', rotation=15)

plt.tight_layout()
plt.show()

# 3. Cek normalitas -- data exponential, kemungkinan tidak normal
print("\n2. Cek Normalitas:")
for desain in data_ui['desain'].unique():
    subset = data_ui[data_ui['desain'] == desain]['waktu_detik']
    _, p = stats.shapiro(subset)
    print(f"   {desain}: p = {p:.4f} --> {'Normal' if p > 0.05 else 'TIDAK Normal'}")

# 4. Karena data tidak normal, gunakan Kruskal-Wallis
print("\n3. Data tidak normal --> Gunakan Kruskal-Wallis Test")
grup_ui = [data_ui[data_ui['desain'] == d]['waktu_detik']
           for d in data_ui['desain'].unique()]

stat_kw, p_kw = stats.kruskal(*grup_ui)
print(f"   H-statistic = {stat_kw:.4f}")
print(f"   p-value     = {p_kw:.4f}")

if p_kw < 0.05:
    print("   Kesimpulan: Ada perbedaan signifikan task completion time antar desain.")

    # Post-hoc Dunn's test
    print("\n4. Post-Hoc: Dunn's Test:")
    dunn = sp.posthoc_dunn(data_ui, val_col='waktu_detik',
                           group_col='desain', p_adjust='bonferroni')
    print(dunn.round(4))
else:
    print("   Kesimpulan: Tidak ada perbedaan signifikan.")

print("\n--- REKOMENDASI UX ---")
print("Berdasarkan analisis, desain dengan median waktu terendah")
print("adalah kandidat terbaik untuk meningkatkan user experience.")
print("Pertimbangkan juga faktor kualitatif (kepuasan, kemudahan).")
```

---

## 10.11 AI Corner: Menggunakan AI untuk ANOVA dan Uji Non-Parametrik

### 10.11.1 Apa yang Bisa Dilakukan AI?

| AI Bisa | AI Tidak Bisa |
|---------|--------------|
| Membantu memilih uji statistik berdasarkan deskripsi data | Menentukan apakah hasilnya bermakna secara *praktis* |
| Men-generate kode Python untuk ANOVA dan post-hoc | Memahami konteks domain spesifik (UX, algoritma, bisnis) |
| Menjelaskan output statistik secara teknis | Menjamin bahwa rekomendasi uji selalu benar |
| Membantu mengecek asumsi dan menginterpretasi uji asumsi | Menggantikan pemikiran kritis tentang desain eksperimen |
| Menyusun narasi hasil analisis | Memutuskan tindakan lanjutan berdasarkan hasil |

### 10.11.2 Contoh Prompt yang Efektif

**Prompt yang Baik:**
```
Saya memiliki data waktu eksekusi dari 3 algoritma sorting,
masing-masing 30 observasi. Hasil Shapiro-Wilk: semua kelompok
p > 0.05 (normal). Levene's test: p = 0.12 (homogen).
Uji apa yang tepat? Berikan kode Python dan jelaskan interpretasinya.
```

**Prompt yang Kurang Baik:**
```
Bandingkan 3 kelompok data saya
```

**Mengapa prompt pertama lebih baik?**
1. Menyebutkan jumlah kelompok dan ukuran sampel
2. Melaporkan hasil pengecekan asumsi
3. Meminta penjelasan (bukan hanya kode)
4. Konteks yang spesifik (algoritma sorting)

### 10.11.3 Kapan Harus Kritis terhadap AI

Waspadai kesalahan umum berikut dari AI:

1. **AI langsung merekomendasikan ANOVA tanpa mengecek asumsi** -- Selalu cek normalitas dan homogenitas variansi terlebih dahulu.

2. **AI mengklaim "ANOVA signifikan berarti semua kelompok berbeda"** -- Ini **salah**. ANOVA signifikan hanya berarti *minimal satu* kelompok berbeda. Perlu post-hoc test untuk mengetahui *mana* yang berbeda.

3. **AI tidak mempertimbangkan effect size** -- p-value kecil dengan sampel besar bisa berarti perbedaan yang sangat kecil (tidak bermakna secara praktis).

4. **AI mengabaikan konteks Indonesia** -- Misalnya, perbedaan ekonomi antara Jawa dan luar Jawa memerlukan interpretasi yang kontekstual.

### 10.11.4 Contoh Evaluasi Output AI

Jika AI mengatakan:

> *"Hasil ANOVA menunjukkan F = 45.23, p < 0.001. Karena p < 0.05, kita menyimpulkan bahwa ketiga algoritma sorting memiliki kecepatan yang berbeda satu sama lain."*

**Evaluasi kritis:**
- Benar bahwa F signifikan dan ada perbedaan
- **Salah** bahwa "ketiga algoritma berbeda *satu sama lain*" -- ini hanya berarti *minimal satu pasangan* berbeda
- Perlu post-hoc test (Tukey HSD) untuk melihat pasangan mana yang signifikan
- Perlu melaporkan effect size untuk konteks praktis

---

## Rangkuman Bab 10

1. **ANOVA** membandingkan rata-rata tiga kelompok atau lebih sekaligus, menghindari inflasi error Type I yang terjadi jika melakukan multiple t-test. ANOVA menghasilkan F-statistic yang merupakan rasio variasi antar kelompok terhadap variasi dalam kelompok.

2. **Asumsi ANOVA** meliputi normalitas distribusi setiap kelompok, homogenitas variansi antar kelompok, dan independensi observasi. Pelanggaran asumsi mengarahkan kita pada uji alternatif (Welch's ANOVA atau Kruskal-Wallis).

3. **Post-hoc test** (Tukey HSD, Bonferroni) diperlukan setelah ANOVA signifikan untuk menentukan *pasangan kelompok mana* yang berbeda secara signifikan. ANOVA hanya mendeteksi *ada* perbedaan, bukan *di mana* perbedaannya.

4. **Uji non-parametrik** (Mann-Whitney U, Wilcoxon signed-rank, Kruskal-Wallis) adalah alternatif yang bekerja berdasarkan rank data dan tidak memerlukan asumsi normalitas. Cocok untuk data ordinal, data sangat skewed, sampel kecil, atau data dengan outlier ekstrem.

5. **Decision tree** untuk memilih uji yang tepat mempertimbangkan: jumlah kelompok, apakah data berpasangan, skala pengukuran, normalitas distribusi, dan homogenitas variansi.

6. **Effect size** (eta-squared) penting dilaporkan bersama p-value karena signifikansi statistik belum tentu berarti signifikansi praktis, terutama pada sampel besar.

7. **Implementasi Python** menggunakan `scipy.stats` (f_oneway, mannwhitneyu, wilcoxon, kruskal), `statsmodels` (pairwise_tukeyhsd), dan `scikit-posthocs` (posthoc_dunn) memungkinkan analisis yang lengkap dan reproducible.

8. **Alur analisis lengkap:** statistik deskriptif --> visualisasi --> cek asumsi --> pilih uji yang tepat --> jalankan uji --> post-hoc (jika signifikan) --> interpretasi dan rekomendasi.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan mengapa melakukan banyak t-test secara berulang untuk membandingkan beberapa kelompok bukan pendekatan yang tepat. Apa masalah utama yang muncul?

**Soal 2.** Perhatikan tabel ANOVA berikut:

| Sumber | SS | df | MS | F | p-value |
|--------|-----|-----|------|-------|---------|
| Between | 240 | 2 | ? | ? | 0.003 |
| Within | 360 | 27 | ? | | |
| Total | 600 | 29 | | | |

- a) Lengkapi nilai MS_Between dan MS_Within.
- b) Hitung nilai F-statistic.
- c) Berapa jumlah kelompok dan jumlah total observasi?
- d) Apa kesimpulan dari uji ini pada alpha = 0.05?

**Soal 3.** Pasangkan setiap uji parametrik dengan alternatif non-parametriknya:

| Uji Parametrik | Alternatif Non-Parametrik |
|---------------|--------------------------|
| Independent t-test | ? |
| Paired t-test | ? |
| One-way ANOVA | ? |

**Soal 4.** Sebutkan tiga asumsi yang harus dipenuhi agar one-way ANOVA valid. Untuk masing-masing asumsi, tuliskan uji formal yang dapat digunakan untuk memeriksanya.

**Soal 5.** Seorang peneliti membandingkan rata-rata waktu login di tiga browser (Chrome, Firefox, Edge) dan mendapatkan hasil ANOVA: F = 8.42, p = 0.001. Dia menyimpulkan bahwa "Chrome lebih cepat daripada Firefox dan Edge." Apakah kesimpulan ini tepat? Jelaskan mengapa ya atau mengapa tidak.

### Tingkat Menengah (C2-C3)

**Soal 6.** Tiga dosen Informatika UAI ingin membandingkan efektivitas metode pengajaran mereka. Dosen A menggunakan ceramah, Dosen B menggunakan diskusi, dan Dosen C menggunakan praktikum. Tulis kode Python lengkap untuk:
- a) Membuat data simulasi (30 mahasiswa per kelompok)
- b) Menghitung statistik deskriptif per kelompok
- c) Membuat box plot perbandingan
- d) Mengecek asumsi normalitas dan homogenitas variansi
- e) Menjalankan ANOVA dan menginterpretasi hasilnya

**Soal 7.** Jelaskan perbedaan antara Tukey HSD dan koreksi Bonferroni sebagai post-hoc test. Kapan sebaiknya menggunakan masing-masing? Berikan contoh situasi di bidang informatika.

**Soal 8.** Perhatikan data kepuasan mahasiswa (skala 1-5) terhadap tiga LMS berikut:

```python
moodle = [4, 5, 3, 4, 5, 4, 3, 5, 4, 4, 3, 5]
canvas = [3, 2, 3, 4, 2, 3, 2, 3, 3, 2, 4, 3]
google_classroom = [4, 3, 4, 5, 4, 3, 4, 4, 5, 3, 4, 4]
```

- a) Mengapa uji non-parametrik lebih tepat daripada ANOVA untuk data ini?
- b) Tulis kode Python untuk menjalankan Kruskal-Wallis test.
- c) Jika hasilnya signifikan, lakukan post-hoc Dunn's test.
- d) Tuliskan kesimpulan dalam konteks rekomendasi untuk kampus.

**Soal 9.** Sebuah perusahaan e-commerce mengukur waktu loading halaman (detik) dari 4 konfigurasi server. Data menunjukkan bahwa distribusi sangat *right-skewed* karena beberapa halaman membutuhkan waktu sangat lama (outlier). Jelaskan langkah demi langkah analisis yang akan Anda lakukan, termasuk uji yang dipilih dan alasannya.

### Tingkat Mahir (C3-C4+)

**Soal 10.** Anda diminta membandingkan akurasi klasifikasi dari 4 model machine learning (Logistic Regression, Random Forest, SVM, Neural Network) yang diuji pada 5 dataset berbeda. Setiap model dijalankan di setiap dataset.

- a) Apakah data ini berpasangan atau independen? Jelaskan.
- b) Uji apa yang paling tepat?
- c) Tulis kode Python untuk melakukan analisis lengkap.
- d) Bagaimana Anda akan memutuskan model mana yang terbaik berdasarkan hasil analisis?

**Soal 11.** Tulis fungsi Python bernama `analisis_perbandingan_kelompok(data, kolom_nilai, kolom_grup)` yang secara otomatis:
- a) Menampilkan statistik deskriptif per kelompok
- b) Membuat visualisasi (box plot dan violin plot)
- c) Mengecek asumsi normalitas dan homogenitas variansi
- d) Memilih dan menjalankan uji yang tepat (t-test/Mann-Whitney atau ANOVA/Kruskal-Wallis)
- e) Melakukan post-hoc test jika hasilnya signifikan
- f) Menghitung effect size
- g) Menghasilkan ringkasan kesimpulan dalam bahasa Indonesia

Uji fungsi Anda dengan minimal dua dataset yang berbeda (satu memenuhi asumsi parametrik, satu tidak).

**Soal 12.** Rancang sebuah studi eksperimental untuk membandingkan waktu penyelesaian tugas pemrograman menggunakan 3 IDE berbeda (VS Code, PyCharm, Jupyter Notebook) oleh mahasiswa Informatika. Jelaskan:
- a) Variabel independen, dependen, dan kontrol
- b) Desain eksperimen (between-subjects atau within-subjects? Mengapa?)
- c) Berapa sampel yang dibutuhkan dan bagaimana cara menghitungnya (power analysis)?
- d) Uji statistik yang akan digunakan dan alasannya
- e) Potensi confounding variables dan cara mengatasinya
- f) Bagaimana Anda akan melaporkan hasilnya (termasuk effect size dan confidence interval)?

**Soal 13.** Analisis kritis berikut. Seorang mahasiswa melakukan ANOVA pada data berikut dan mendapat F = 0.85, p = 0.44. Dia menyimpulkan bahwa "tidak ada perbedaan antara ketiga kelompok."

```python
grup_1 = [10, 20, 30, 40, 50]     # Mean = 30, Std = 15.81
grup_2 = [28, 29, 30, 31, 32]     # Mean = 30, Std = 1.58
grup_3 = [5, 15, 30, 45, 55]      # Mean = 30, Std = 20.00
```

- a) Mengapa ANOVA tidak signifikan meskipun data terlihat berbeda?
- b) Asumsi ANOVA mana yang dilanggar?
- c) Apakah kesimpulan mahasiswa tersebut tepat? Jelaskan.
- d) Uji atau pendekatan alternatif apa yang seharusnya digunakan?

**Soal 14.** Bandingkan hasil ANOVA dan Kruskal-Wallis pada data yang sama. Kapan kedua uji ini memberikan kesimpulan yang berbeda? Buatlah contoh data di Python di mana:
- a) Keduanya signifikan
- b) ANOVA signifikan tetapi Kruskal-Wallis tidak (atau sebaliknya)
- c) Jelaskan mengapa perbedaan ini terjadi

---

## Referensi

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability & Statistics for Engineers & Scientists* (9th ed.). Pearson.
2. Field, A. (2018). *Discovering Statistics Using IBM SPSS Statistics* (5th ed.), Chapters 12-15. Sage Publications.
3. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics* (4th ed.), Chapter 7: Inference for Numerical Data (ANOVA section).
4. Bruce, P., & Bruce, A. (2020). *Practical Statistics for Data Scientists* (2nd ed.), Chapter 3: Statistical Experiments and Significance Testing. O'Reilly Media.
5. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
6. SciPy Documentation: [scipy.stats.f_oneway](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html), [scipy.stats.mannwhitneyu](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html), [scipy.stats.wilcoxon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html), [scipy.stats.kruskal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html).
7. Statsmodels Documentation: [pairwise_tukeyhsd](https://www.statsmodels.org/stable/generated/statsmodels.stats.multicomp.pairwise_tukeyhsd.html).
8. scikit-posthocs Documentation: [scikit-posthocs](https://scikit-posthocs.readthedocs.io/).
9. BPS (Badan Pusat Statistik). *Survei Sosial Ekonomi Nasional (Susenas)*. [bps.go.id](https://bps.go.id).

---

*Bab berikutnya: **Bab 11 — Analisis Data Kategorikal dan Uji Chi-Square***
