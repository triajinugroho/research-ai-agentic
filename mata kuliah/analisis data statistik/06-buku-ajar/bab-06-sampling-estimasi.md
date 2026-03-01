# BAB 6: SAMPLING, ESTIMASI, DAN BOOTSTRAP

**Tri Aji Nugroho, S.T., M.T.**
Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-4.1 | Membedakan teknik-teknik sampling (simple random, stratified, cluster, systematic) dan memilih teknik yang tepat untuk kasus tertentu | C4 |
| CPMK-4.2 | Mengidentifikasi dan menganalisis potensi sampling bias dalam desain survei | C4 |
| CPMK-4.3 | Menghitung dan menginterpretasikan point estimation serta interval estimation (confidence interval) untuk mean dan proporsi | C4 |
| CPMK-4.4 | Menentukan ukuran sampel minimum berdasarkan margin of error dan confidence level yang diinginkan | C4 |
| CPMK-4.5 | Mengimplementasikan bootstrap resampling menggunakan Python untuk mengestimasi confidence interval tanpa asumsi distribusi | C4 |

---

## 6.1 Mengapa Sampling?

Pada bab-bab sebelumnya kita mempelajari cara mendeskripsikan dan memvisualisasikan data yang sudah ada di tangan kita. Namun dalam praktik, seorang analis data jarang sekali memiliki akses ke **seluruh populasi**. Bayangkan skenario berikut:

- BPS ingin mengetahui rata-rata pengeluaran rumah tangga di Indonesia (270 juta penduduk)
- Lembaga survei Litbang Kompas ingin memprediksi hasil Pilpres sebelum hari pemungutan suara
- Tim QA perusahaan e-commerce ingin mengukur waktu respons rata-rata servernya

Tidak mungkin — atau tidak efisien — untuk memeriksa setiap anggota populasi. Solusinya adalah **sampling**: mengambil sebagian kecil yang representatif untuk membuat kesimpulan tentang keseluruhan.

> "The goal of sampling is not to have a perfect miniature copy of the population, but to have one that is good enough to support the inferences we need to make."
> — Andrew Gelman, *Regression and Other Stories*

```
         POPULASI                     SAMPEL
    ┌─────────────────┐          ┌───────────┐
    │  ○ ○ ○ ○ ○ ○ ○  │          │  ○ ○ ○    │
    │  ○ ○ ○ ○ ○ ○ ○  │ ──────►  │  ○ ○ ○    │
    │  ○ ○ ○ ○ ○ ○ ○  │ Sampling │  ○ ○      │
    │  ○ ○ ○ ○ ○ ○ ○  │          └───────────┘
    └─────────────────┘               │
        N = sangat besar         n << N
        Parameter: μ, σ, p            │
                                      ▼
                               Hitung statistik:
                               x̄, s, p̂
                                      │
                                      ▼
                               Buat inferensi
                               tentang populasi
```

### 6.1.1 Populasi vs Sampel: Notasi

| Konsep | Populasi | Sampel |
|--------|----------|--------|
| **Definisi** | Seluruh elemen yang ingin dipelajari | Sebagian elemen yang dipilih dari populasi |
| **Ukuran** | N (biasanya sangat besar) | n (lebih kecil) |
| **Mean** | μ (mu) — **parameter**, biasanya tidak diketahui | x̄ (x-bar) — **statistik**, dihitung dari data |
| **Std Dev** | σ (sigma) — **parameter** | s — **statistik** |
| **Proporsi** | p — **parameter** | p̂ (p-hat) — **statistik** |

**Prinsip utama:** Statistik sampel (x̄, s, p̂) digunakan untuk **mengestimasi** parameter populasi (μ, σ, p) yang tidak diketahui.

### 6.1.2 Alasan Sampling

Sampling diperlukan karena empat alasan utama:

1. **Biaya** — Mewawancarai 270 juta penduduk Indonesia membutuhkan anggaran yang tidak realistis. BPS hanya mampu melakukan sensus penuh setiap 10 tahun sekali.
2. **Waktu** — Pengambilan keputusan sering butuh informasi cepat. Survei 1.000 responden bisa selesai dalam seminggu; sensus butuh bertahun-tahun.
3. **Destruktif** — Menguji ketahanan seluruh batch baterai lithium = tidak ada yang tersisa untuk dijual.
4. **Populasi tak terbatas** — Semua kemungkinan hasil pelemparan koin tidak bisa semuanya diamati.

---

## 6.2 Teknik Sampling

Teknik sampling dibagi menjadi dua kategori besar: **probability sampling** (setiap anggota memiliki peluang terukur untuk terpilih) dan **non-probability sampling** (tidak ada jaminan representasi). Kita fokus pada probability sampling karena hanya metode inilah yang memungkinkan kita membuat inferensi statistik yang valid.

```
TEKNIK SAMPLING
├── PROBABILITY SAMPLING (inferensi valid)
│   ├── Simple Random Sampling (SRS)
│   ├── Stratified Sampling
│   ├── Systematic Sampling
│   └── Cluster Sampling
└── NON-PROBABILITY SAMPLING (inferensi terbatas)
    ├── Convenience Sampling
    ├── Purposive Sampling
    └── Snowball Sampling
```

### 6.2.1 Simple Random Sampling (SRS)

**Definisi:** Setiap anggota populasi memiliki peluang yang **sama dan independen** untuk terpilih.

**Prosedur:**
1. Buat **sampling frame** — daftar lengkap semua anggota populasi
2. Beri nomor setiap anggota (1 sampai N)
3. Gunakan random number generator untuk memilih n nomor tanpa pengembalian

**Ilustrasi ASCII:**

```
Populasi N=10:   [1] [2] [3] [4] [5] [6] [7] [8] [9] [10]
                  ^           ^               ^
Sampel n=3:      [1]         [4]             [7]
(dipilih acak)
```

**Kelebihan:**
- Paling sederhana dan mudah dipahami
- Tidak ada bias seleksi jika sampling frame lengkap
- Analisis statistik paling mudah dan langsung

**Kekurangan:**
- Butuh sampling frame yang lengkap (sering tidak tersedia)
- Bisa tidak representatif untuk subkelompok kecil
- Tidak efisien jika populasi tersebar secara geografis

**Contoh Indonesia:** BPS menggunakan SRS dalam beberapa survei rumah tangga di mana daftar lengkap rumah tangga tersedia dari registrasi kependudukan.

```python
import numpy as np
import pandas as pd

# === SIMPLE RANDOM SAMPLING ===
np.random.seed(42)

# Simulasi: populasi 1000 mahasiswa UAI
populasi = pd.DataFrame({
    'id': range(1, 1001),
    'prodi': np.random.choice(['Informatika', 'Sistem Informasi', 'Teknik Elektro',
                                'Manajemen', 'Akuntansi'], size=1000),
    'ipk': np.random.normal(3.2, 0.4, 1000).clip(1.0, 4.0)
})

# Ambil simple random sample n=50
sampel_srs = populasi.sample(n=50, random_state=42)

print(f"Populasi : N = {len(populasi)}")
print(f"Sampel   : n = {len(sampel_srs)}")
print(f"\nMean IPK Populasi  : {populasi['ipk'].mean():.4f}")
print(f"Mean IPK Sampel SRS: {sampel_srs['ipk'].mean():.4f}")
print(f"Selisih            : {abs(populasi['ipk'].mean() - sampel_srs['ipk'].mean()):.4f}")
```

### 6.2.2 Stratified Sampling

**Definisi:** Populasi dibagi ke dalam **strata** (subkelompok yang homogen secara internal), lalu sampel diambil dari setiap stratum secara **proporsional** atau sama rata.

**Prosedur:**
1. Identifikasi variabel strata yang relevan (misal: prodi, jenis kelamin, wilayah)
2. Bagi populasi ke dalam strata yang mutually exclusive dan collectively exhaustive
3. Ambil sampel dari setiap stratum (proporsional: n_k = n × N_k/N)

**Ilustrasi ASCII:**

```
Populasi (N=300)
┌──────────────┬──────────────┬──────────────┐
│  Stratum A   │  Stratum B   │  Stratum C   │
│  (Infor.)    │  (SI)        │  (Teknik)    │
│  N_A = 150   │  N_B = 90    │  N_C = 60    │
│  (50%)       │  (30%)       │  (20%)       │
└──────┬───────┴──────┬───────┴──────┬───────┘
       │Sampel 50%    │Sampel 30%    │Sampel 20%
       ▼              ▼              ▼
    n_A = 25       n_B = 15       n_C = 10
                                         Total n=50
```

**Kelebihan:**
- Menjamin representasi setiap subkelompok (sangat penting jika ada subkelompok kecil)
- Variance estimasi **lebih kecil** dibanding SRS (estimasi lebih presisi)
- Memungkinkan analisis terpisah per stratum

**Kekurangan:**
- Perlu informasi tentang strata sebelum pengambilan sampel
- Lebih kompleks dalam implementasi dan analisis

**Contoh Indonesia:** Survei Sosial Ekonomi Nasional (Susenas) BPS menggunakan stratified sampling berdasarkan provinsi dan daerah perkotaan/perdesaan.

```python
# === STRATIFIED SAMPLING ===

def stratified_sample(df, strata_col, n_total, random_state=42):
    """Ambil sampel proporsional berdasarkan strata."""
    proportions = df[strata_col].value_counts(normalize=True)
    samples = []

    for stratum, prop in proportions.items():
        n_stratum = max(1, round(n_total * prop))
        stratum_data = df[df[strata_col] == stratum]
        sample = stratum_data.sample(
            n=min(n_stratum, len(stratum_data)),
            random_state=random_state
        )
        samples.append(sample)

    return pd.concat(samples).reset_index(drop=True)

sampel_stratified = stratified_sample(populasi, 'prodi', n_total=50)

print("=== PERBANDINGAN PROPORSI PRODI ===")
print(f"\n{'Prodi':<20} {'Populasi':>10} {'Sampel (Strat)':>15}")
print("-" * 47)
pop_prop = populasi['prodi'].value_counts(normalize=True)
samp_prop = sampel_stratified['prodi'].value_counts(normalize=True)
for prodi in pop_prop.index:
    print(f"{prodi:<20} {pop_prop[prodi]:>10.3f} {samp_prop.get(prodi, 0):>15.3f}")

print(f"\nMean IPK Populasi          : {populasi['ipk'].mean():.4f}")
print(f"Mean IPK Sampel Stratified : {sampel_stratified['ipk'].mean():.4f}")
```

### 6.2.3 Systematic Sampling

**Definisi:** Pilih elemen pertama secara acak, lalu pilih setiap elemen ke-**k** dari daftar, dengan k = N/n (interval sampling).

**Prosedur:**
1. Hitung k = N/n (dibulatkan ke bilangan bulat terdekat)
2. Pilih starting point r secara acak dari 1 hingga k
3. Ambil elemen ke r, r+k, r+2k, r+3k, …

**Ilustrasi ASCII:**

```
N=20, n=5, k=4, r=2 (acak)

Indeks : 1  2  3  4 | 5  6  7  8 | 9 10 11 12 |13 14 15 16 |17 18 19 20
         -  *  -  - | -  *  -  - | -  *  -  - | -  *  -  - | -  *  -  -
             ↑              ↑          ↑              ↑          ↑
           r=2           r+k=6     r+2k=10        r+3k=14    r+4k=18
```

**Kelebihan:**
- Sangat mudah dilaksanakan di lapangan
- Tersebar merata di seluruh urutan populasi

**Kekurangan:**
- Bisa menghasilkan bias jika ada **pola periodik** dalam data (periodicitas). Contoh: data penjualan harian dengan pola weekend—weekday.

```python
# === SYSTEMATIC SAMPLING ===

N = len(populasi)
n = 50
k = N // n  # interval sampling = 20

# Pilih starting point acak antara 0 dan k-1
np.random.seed(42)
start = np.random.randint(0, k)

# Ambil setiap elemen ke-k
indices = list(range(start, N, k))[:n]
sampel_systematic = populasi.iloc[indices]

print(f"=== SYSTEMATIC SAMPLING ===")
print(f"Interval k        = {k}")
print(f"Starting index    = {start}")
print(f"Ukuran sampel     = {len(sampel_systematic)}")
print(f"\nMean IPK Populasi           : {populasi['ipk'].mean():.4f}")
print(f"Mean IPK Sampel Systematic  : {sampel_systematic['ipk'].mean():.4f}")
```

### 6.2.4 Cluster Sampling

**Definisi:** Populasi dibagi ke dalam **cluster** (kelompok yang heterogen secara internal, mirip dengan miniatur populasi), beberapa cluster dipilih secara acak, dan **semua** anggota cluster terpilih diteliti.

**Perbedaan kunci dari Stratified:**

```
STRATIFIED: Bagi populasi → strata HOMOGEN → ambil SEBAGIAN dari setiap stratum
CLUSTER:    Bagi populasi → cluster HETEROGEN → pilih BEBERAPA cluster → ambil SEMUA anggotanya
```

**Contoh cluster:** Kelas/rombel, RT/RW, rumah sakit, sekolah.

**Kelebihan:**
- Praktis dan ekonomis (tidak perlu sampling frame lengkap, hanya daftar cluster)
- Efisien jika populasi tersebar geografis (survei desa-desa di Kalimantan)

**Kekurangan:**
- Variance estimasi **lebih besar** dibanding SRS dan stratified
- Cluster yang terpilih bisa tidak mewakili keragaman populasi

**Contoh Indonesia:** Dalam RISKESDAS (Riset Kesehatan Dasar) Kemenkes, cluster sampling digunakan dengan kelurahan/desa sebagai cluster.

```python
# === CLUSTER SAMPLING ===
# Cluster = prodi (masing-masing prodi dianggap sebagai satu cluster)

np.random.seed(42)
semua_cluster = populasi['prodi'].unique()
n_cluster_dipilih = 2

# Pilih 2 cluster (prodi) secara acak
selected_clusters = np.random.choice(semua_cluster, size=n_cluster_dipilih, replace=False)
sampel_cluster = populasi[populasi['prodi'].isin(selected_clusters)]

print(f"=== CLUSTER SAMPLING ===")
print(f"Semua cluster : {list(semua_cluster)}")
print(f"Cluster terpilih: {list(selected_clusters)}")
print(f"Ukuran sampel   : {len(sampel_cluster)}")
print(f"\nMean IPK Populasi        : {populasi['ipk'].mean():.4f}")
print(f"Mean IPK Sampel Cluster  : {sampel_cluster['ipk'].mean():.4f}")
```

### 6.2.5 Ringkasan Perbandingan Teknik Sampling

| Metode | Prasyarat | Presisi | Biaya/Kemudahan | Kapan Digunakan |
|--------|-----------|---------|-----------------|-----------------|
| **Simple Random** | Sampling frame lengkap | Baseline | Bisa mahal | Populasi homogen, frame tersedia |
| **Stratified** | Info strata | Terbaik | Sedang | Ada subkelompok penting |
| **Systematic** | Daftar terurut | Baik | Paling mudah | Populasi berurutan, tidak ada periodisitas |
| **Cluster** | Daftar cluster | Terendah | Paling murah | Geografis tersebar, tidak ada frame |

---

## 6.3 Sampling Bias

**Sampling bias** terjadi ketika mekanisme pemilihan sampel secara sistematis menghasilkan sampel yang **tidak representatif** terhadap populasi. Bias bukan soal kesalahan acak — bias adalah kesalahan **sistematis** yang tidak hilang meski ukuran sampel diperbesar.

### 6.3.1 Jenis-Jenis Bias

**1. Selection Bias (Bias Seleksi)**
Terjadi ketika prosedur pemilihan lebih cenderung memilih anggota tertentu.

*Contoh:* Survei kepuasan pengguna yang hanya dikirim via email ke pengguna yang pernah login dalam 30 hari terakhir — pengguna tidak aktif tidak terwakili sama sekali.

**2. Non-Response Bias**
Terjadi ketika responden yang tidak menjawab berbeda secara sistematis dari yang menjawab.

*Contoh Indonesia:* Dalam survei ekonomi, rumah tangga sangat miskin sering tidak bisa dihubungi karena tidak memiliki nomor telepon. Hal ini menyebabkan estimasi pendapatan rata-rata menjadi lebih tinggi dari kenyataan.

**3. Survivorship Bias**
Hanya mengamati yang "selamat" atau berhasil, mengabaikan yang gagal.

*Contoh:* Menganalisis portofolio reksa dana yang saat ini aktif terdaftar di OJK — reksa dana yang sudah dibubarkan karena kinerjanya buruk tidak masuk dalam analisis, sehingga kinerja rata-rata tampak lebih baik dari kenyataannya.

**4. Convenience Sampling Bias**
Memilih responden yang paling mudah dijangkau.

*Contoh:* Mahasiswa yang melakukan penelitian skripsi dan hanya menyebarkan kuesioner ke teman-temannya sendiri — tidak mewakili populasi yang lebih luas.

### 6.3.2 Cara Mengurangi Bias

```
STRATEGI PENGURANGAN BIAS
├── Gunakan probability sampling (bukan convenience sampling)
├── Pastikan sampling frame selengkap mungkin
├── Lakukan follow-up untuk non-responden
├── Terapkan pembobotan (weighting) pasca-survei
└── Transparansi dalam pelaporan: ungkapkan keterbatasan sampling
```

> **Catatan penting:** Ukuran sampel yang besar **tidak menghilangkan bias**. Survei online dengan 1 juta responden yang memilih sendiri (self-selected) masih lebih bias dibanding survei telepon yang proper dengan 1.000 responden terpilih secara acak.

---

## 6.4 Distribusi Sampling dan Standard Error

### 6.4.1 Distribusi Sampling

**Definisi:** Jika kita mengambil **banyak** sampel berukuran n dari populasi yang sama dan menghitung suatu statistik (misalnya: mean) dari setiap sampel, maka distribusi dari semua statistik tersebut disebut **sampling distribution** (distribusi sampling).

Ini adalah konsep teoritis yang sangat penting — dalam praktik kita hanya mengambil **satu** sampel, tetapi kita perlu memahami bagaimana statistik kita akan bervariasi jika kita mengambil banyak sampel.

**Koneksi dengan CLT (dari Bab 5):**

Central Limit Theorem menyatakan bahwa distribusi sampling dari mean akan mendekati **Normal** untuk n yang cukup besar (umumnya n ≥ 30), dengan:
- Mean distribusi sampling = μ (mean populasi)
- Standard deviation distribusi sampling = σ/√n (**Standard Error**)

### 6.4.2 Standard Error (SE)

**Formula:**

$$SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}} \approx \frac{s}{\sqrt{n}}$$

di mana:
- σ = standard deviation populasi (biasanya tidak diketahui, digantikan s)
- s = standard deviation sampel
- n = ukuran sampel

**Interpretasi:** Standard Error mengukur seberapa bervariasi rata-rata sampel antar sampel yang berbeda. SE yang kecil berarti estimasi kita lebih presisi.

**Poin penting yang sering dikacaukan:**

| Konsep | Mengukur Apa | Formula |
|--------|-------------|---------|
| **Standard Deviation (s)** | Sebaran data individual dalam satu sampel | $s = \sqrt{\frac{\sum(x_i-\bar{x})^2}{n-1}}$ |
| **Standard Error (SE)** | Sebaran mean sampel antar sampel berbeda | $SE = s/\sqrt{n}$ |

```python
from scipy import stats
import matplotlib.pyplot as plt

# === DEMONSTRASI STANDARD ERROR ===
np.random.seed(42)

pop_mean = 165    # rata-rata tinggi badan (cm)
pop_std = 8
n_simulations = 3000

sample_sizes = [5, 10, 30, 100]

fig, axes = plt.subplots(1, 4, figsize=(18, 4))

for i, n in enumerate(sample_sizes):
    # Simulasi: ambil 3000 sampel berukuran n, hitung mean tiap sampel
    sample_means = [np.random.normal(pop_mean, pop_std, n).mean()
                    for _ in range(n_simulations)]

    se_teoritis = pop_std / np.sqrt(n)
    se_empiris  = np.std(sample_means)

    axes[i].hist(sample_means, bins=50, density=True,
                 color='steelblue', alpha=0.7, edgecolor='white')
    axes[i].axvline(pop_mean, color='red', linestyle='--', linewidth=2)
    axes[i].set_title(f'n = {n}\nSE teori = {se_teoritis:.2f}\nSE empiris = {se_empiris:.2f}')
    axes[i].set_xlabel('Rata-rata Sampel (cm)')

plt.suptitle('Distribusi Sampling: SE Mengecil Seiring n Bertambah',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Apa yang terlihat dari simulasi:** Semakin besar n, distribusi sampling semakin sempit (SE mengecil), artinya estimasi mean kita semakin mendekati nilai populasi yang sebenarnya.

---

## 6.5 Estimasi: Point vs Interval

### 6.5.1 Point Estimation

**Definisi:** Menggunakan **satu nilai** tunggal sebagai estimasi parameter populasi.

**Contoh:**
- x̄ = 3.25 sebagai estimasi μ (IPK rata-rata populasi)
- s = 0.38 sebagai estimasi σ
- p̂ = 0.62 sebagai estimasi p (proporsi mahasiswa yang puas)

**Sifat estimator yang baik (BLUE):**
1. **Unbiased** — rata-rata estimator = parameter populasi
2. **Consistent** — semakin besar n, estimator semakin mendekati parameter
3. **Efficient** — variance estimator sekecil mungkin

**Keterbatasan:** Point estimation tidak memberikan informasi tentang **ketidakpastian** estimasi. Apakah μ benar-benar tepat 3.25? Atau bisa saja 3.15 atau 3.35?

### 6.5.2 Interval Estimation (Confidence Interval)

**Definisi:** Memberikan **rentang nilai** yang kemungkinan besar mengandung parameter populasi, disertai dengan **tingkat kepercayaan** (confidence level) tertentu.

**Logika dasar Confidence Interval:**

Berdasarkan CLT, distribusi sampling dari x̄ bersifat Normal dengan mean μ dan SE = σ/√n. Oleh karena itu:

$$P\left(\bar{x} - z^* \frac{\sigma}{\sqrt{n}} \leq \mu \leq \bar{x} + z^* \frac{\sigma}{\sqrt{n}}\right) = 1 - \alpha$$

di mana α adalah tingkat signifikansi (1 - confidence level).

---

## 6.6 Confidence Interval untuk Mean

### 6.6.1 Formula

**Kasus 1: σ diketahui (sangat jarang dalam praktik)**

$$CI_{1-\alpha} = \bar{x} \pm z^* \cdot \frac{\sigma}{\sqrt{n}}$$

**Kasus 2: σ tidak diketahui (gunakan distribusi-t)**

$$CI_{1-\alpha} = \bar{x} \pm t^*_{df=n-1} \cdot \frac{s}{\sqrt{n}}$$

**Nilai kritis yang umum:**

| Confidence Level | α | z* (Normal) | t* (df=29) | t* (df=9) |
|-----------------|---|-------------|------------|-----------|
| 90% | 0.10 | 1.645 | 1.699 | 1.833 |
| 95% | 0.05 | 1.960 | 2.045 | 2.262 |
| 99% | 0.01 | 2.576 | 2.756 | 3.250 |

**Catatan:** Gunakan z* hanya jika σ diketahui atau n sangat besar (n > 200). Dalam hampir semua kasus nyata, gunakan t* dengan df = n − 1.

### 6.6.2 Komponen Confidence Interval

```
CI = x̄ ± Margin of Error

Margin of Error (ME) = t* × SE = t* × (s / √n)

┌─────────────────────────────────────────────────┐
│          95% Confidence Interval                │
│                                                 │
│   [──────────────|──────────────]               │
│   ↑              ↑              ↑               │
│ x̄ - ME          x̄           x̄ + ME            │
│                                                 │
│   ←── ME ──→ ←── ME ──→                        │
│        (lebar CI = 2 × ME)                      │
└─────────────────────────────────────────────────┘
```

### 6.6.3 Interpretasi yang Benar

Ini adalah salah satu konsep yang **paling sering disalahartikan** dalam statistik inferensial:

**Interpretasi BENAR:**
> "Prosedur ini, jika diulangi berkali-kali, akan menghasilkan interval yang mengandung parameter populasi sebesar 95% dari semua interval yang dihitung."

**Miskonsepsi yang SALAH:**

| Pernyataan | Mengapa Salah |
|-----------|---------------|
| "Ada 95% peluang bahwa μ berada di interval ini" | μ adalah **konstanta** (nilai tetap yang tidak berubah), bukan variabel acak. Yang acak adalah intervalnya — setiap sampel berbeda akan menghasilkan interval berbeda. |
| "95% data berada di dalam interval ini" | CI berkaitan dengan **mean populasi**, bukan sebaran data individual. |
| "Saya 95% yakin μ = x̄" | CI menyatakan rentang kemungkinan, bukan keyakinan bahwa μ tepat di titik tengah. |

**Visualisasi konsep yang benar:**

```
50 eksperimen mengambil sampel dan menghitung 95% CI:

Eksperimen 1:  [========|========]           ← mengandung μ ✓
Eksperimen 2:      [========|========]       ← mengandung μ ✓
Eksperimen 3:  [======|======]               ← mengandung μ ✓
Eksperimen 4:            [=====|=====]       ← mengandung μ ✓
Eksperimen 5:                    [====|====] ← TIDAK mengandung μ ✗
...dan seterusnya...

Parameter μ:   ─────────────────────────────── (nilai tetap, tidak diketahui)

Rata-rata: ~95% dari 50 interval tersebut mengandung μ
```

### 6.6.4 Implementasi Python

```python
# === MENGHITUNG CONFIDENCE INTERVAL UNTUK MEAN ===

np.random.seed(42)

# Skenario: sampel IPK 40 mahasiswa Informatika UAI
ipk_sampel = np.random.normal(loc=3.25, scale=0.38, size=40).clip(1.0, 4.0)

# Statistik sampel
n      = len(ipk_sampel)
x_bar  = ipk_sampel.mean()
s      = ipk_sampel.std(ddof=1)   # ddof=1 untuk sampel (bukan populasi)
se     = s / np.sqrt(n)

print("=" * 50)
print("STATISTIK SAMPEL")
print("=" * 50)
print(f"n    = {n}")
print(f"x̄   = {x_bar:.4f}")
print(f"s    = {s:.4f}")
print(f"SE   = {se:.4f}")
print()

# --- Cara 1: Hitung manual ---
for conf in [0.90, 0.95, 0.99]:
    alpha   = 1 - conf
    t_crit  = stats.t.ppf(1 - alpha/2, df=n - 1)
    me      = t_crit * se
    ci_lo   = x_bar - me
    ci_hi   = x_bar + me
    print(f"{int(conf*100)}% CI: ({ci_lo:.4f}, {ci_hi:.4f})  "
          f"[t* = {t_crit:.3f}, ME = {me:.4f}, Lebar = {2*me:.4f}]")

print()

# --- Cara 2: Menggunakan scipy.stats (lebih ringkas) ---
ci_95 = stats.t.interval(confidence=0.95, df=n-1, loc=x_bar, scale=se)
print(f"95% CI (scipy): ({ci_95[0]:.4f}, {ci_95[1]:.4f})")
```

**Interpretasi hasil:**
> "Berdasarkan data dari 40 mahasiswa (x̄ = 3.25, s = 0.38), kita dapat menyatakan dengan prosedur 95% bahwa interval tersebut mengandung rata-rata IPK seluruh mahasiswa Informatika UAI. Lebar interval yang cukup sempit menunjukkan estimasi yang cukup presisi."

---

## 6.7 Confidence Interval untuk Proporsi

Dalam banyak survei — terutama survei opini publik dan polling politik — parameter yang ingin diestimasi adalah **proporsi** (persentase), bukan mean.

### 6.7.1 Formula

Misalkan p adalah proporsi populasi dan p̂ adalah proporsi sampel. Maka:

$$SE_{\hat{p}} = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

$$CI_{1-\alpha} = \hat{p} \pm z^* \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

**Syarat penggunaan:** n × p̂ ≥ 10 **dan** n × (1-p̂) ≥ 10 (agar distribusi Normal valid).

### 6.7.2 Contoh: Polling Pilpres Indonesia

```python
# === CONFIDENCE INTERVAL UNTUK PROPORSI ===
# Skenario: Survei elektabilitas calon presiden

# Data survei: 1200 responden, 624 memilih kandidat A
n_responden   = 1200
n_pilih_A     = 624
p_hat         = n_pilih_A / n_responden  # proporsi sampel

# Standard Error untuk proporsi
se_prop = np.sqrt(p_hat * (1 - p_hat) / n_responden)

print("=" * 55)
print("SURVEI ELEKTABILITAS (Simulasi)")
print("=" * 55)
print(f"Jumlah responden : {n_responden}")
print(f"Memilih Kandidat A: {n_pilih_A} ({p_hat*100:.1f}%)")
print(f"SE proporsi      : {se_prop:.4f}")
print()

# CI untuk proporsi (gunakan z*, bukan t*, karena proporsi)
for conf in [0.90, 0.95, 0.99]:
    alpha   = 1 - conf
    z_crit  = stats.norm.ppf(1 - alpha/2)
    me      = z_crit * se_prop
    ci_lo   = p_hat - me
    ci_hi   = p_hat + me
    print(f"{int(conf*100)}% CI: ({ci_lo*100:.1f}%, {ci_hi*100:.1f}%)  "
          f"[ME = ±{me*100:.1f}%]")

# Verifikasi syarat Normal
print(f"\nCek syarat Normal:")
print(f"n × p̂     = {n_responden * p_hat:.0f} (harus ≥ 10) → {'OK' if n_responden*p_hat >= 10 else 'TIDAK OK'}")
print(f"n × (1-p̂) = {n_responden * (1-p_hat):.0f} (harus ≥ 10) → {'OK' if n_responden*(1-p_hat) >= 10 else 'TIDAK OK'}")
```

**Interpretasi:** Jika 95% CI adalah (49.2%, 54.8%), maka kita tidak bisa menyimpulkan kandidat A unggul secara statistik, karena interval masih mencakup 50%. Ini adalah makna nyata dari "margin of error" yang sering disebut dalam berita.

---

## 6.8 Margin of Error dan Ukuran Sampel

### 6.8.1 Margin of Error (ME)

**Margin of Error** adalah setengah dari lebar confidence interval:

$$ME = z^* \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \quad \text{(untuk proporsi)}$$

$$ME = t^* \cdot \frac{s}{\sqrt{n}} \quad \text{(untuk mean)}$$

Ketika media melaporkan "survei ini memiliki margin of error ±3% dengan tingkat kepercayaan 95%", artinya CI mereka memiliki lebar total 6% (±3% dari point estimate).

### 6.8.2 Menentukan Ukuran Sampel Minimum

Sering kali kita ingin menentukan **berapa besar n** yang dibutuhkan untuk mencapai ME tertentu. Balik rumus ME:

**Untuk proporsi (kasus terburuk: p = 0.5):**

$$n \geq \left(\frac{z^*}{ME}\right)^2 \cdot p(1-p) = \left(\frac{z^*}{ME}\right)^2 \cdot 0.25$$

**Untuk mean:**

$$n \geq \left(\frac{z^* \cdot \sigma}{ME}\right)^2$$

```python
# === PENENTUAN UKURAN SAMPEL MINIMUM ===

print("=" * 60)
print("TABEL UKURAN SAMPEL MINIMUM UNTUK PROPORSI")
print("(Kasus terburuk: p = 0.5, Confidence Level = 95%)")
print("=" * 60)

z_star = 1.960  # 95% confidence

print(f"\n{'Margin of Error':>18} | {'n minimum':>12} | {'Contoh Survei'}")
print("-" * 55)

for me_pct in [1, 2, 3, 4, 5, 10]:
    me = me_pct / 100
    n_min = int(np.ceil((z_star / me) ** 2 * 0.25))
    contoh = {1: "Pilpres nasional", 2: "Survei nasional", 3: "Survei provinsi",
              4: "Survei kota", 5: "Akademik/skripsi", 10: "Studi awal"}
    print(f"     ±{me_pct}% ({me:.2f})   | {n_min:>12,} | {contoh.get(me_pct, '')}")

print()
print("PENGARUH CONFIDENCE LEVEL (ME = ±3%)")
print("-" * 55)
for conf, z in [(0.90, 1.645), (0.95, 1.960), (0.99, 2.576)]:
    n_min = int(np.ceil((z / 0.03) ** 2 * 0.25))
    print(f"Confidence {int(conf*100)}%: z* = {z:.3f} → n ≥ {n_min:,}")
```

**Implikasi praktis:**

```
Ukuran Sampel dan Margin of Error (95% CI, proporsi):

n = 100  → ME = ±9.8%   (sangat kasar)
n = 400  → ME = ±4.9%   (survei kelas menengah)
n = 600  → ME = ±4.0%   (survei Litbang Kompas)
n = 1067 → ME = ±3.0%   (survei standar Pilpres)
n = 2401 → ME = ±2.0%   (survei presisi tinggi)
n = 9604 → ME = ±1.0%   (sangat presisi, mahal)
```

---

## 6.9 Bootstrap Resampling

### 6.9.1 Motivasi: Ketika Formula Tidak Cukup

Formula CI berbasis distribusi-t bekerja dengan baik ketika:
- Data mendekati Normal **atau** n cukup besar (CLT berlaku)
- Kita mengestimasi **mean** atau **proporsi**

Tetapi bagaimana jika:
- Kita ingin CI untuk **median**? Tidak ada rumus sederhana.
- Data sangat **skewed** dan n kecil?
- Kita ingin CI untuk **korelasi**, **rasio**, atau statistik yang kompleks?

Jawaban: **Bootstrap**.

### 6.9.2 Prinsip Bootstrap

**Ide inti:** Jika kita tidak tahu distribusi populasi, gunakan **sampel yang kita punya** sebagai proxy populasi. Lakukan resampling dari sampel tersebut berkali-kali **dengan pengembalian** (with replacement).

**Analogi:** Anggap sampel Anda adalah "populasi kecil". Sama seperti kita mengambil banyak sampel dari populasi untuk membangun distribusi sampling, kita mengambil banyak **bootstrap samples** dari sampel kita.

**Prosedur bootstrap:**

```
DATA ASLI (n=30):
  [x₁, x₂, x₃, ..., x₃₀]
         │
         ▼ Resample WITH replacement (B kali)
         │
Bootstrap Sample 1: [x₅, x₅, x₁₂, x₃, x₅, ...] → hitung statistik θ̂₁*
Bootstrap Sample 2: [x₁₉, x₄, x₄, x₂₇, x₁, ...] → hitung statistik θ̂₂*
Bootstrap Sample 3: [x₇, x₃₀, x₃, x₁₅, x₇, ...] → hitung statistik θ̂₃*
...
Bootstrap Sample B: [...]                           → hitung statistik θ̂ᵦ*
         │
         ▼
Bootstrap Distribution: [θ̂₁*, θ̂₂*, ..., θ̂ᵦ*]
         │
         ▼ Ambil percentile ke-2.5 dan 97.5
         │
95% Bootstrap CI: (percentile_2.5, percentile_97.5)
```

### 6.9.3 Implementasi Bootstrap dari Nol

```python
# === BOOTSTRAP CONFIDENCE INTERVAL ===

np.random.seed(42)

# Data sampel: waktu respons API (milidetik) — distribusi skewed
data_respons = np.array([
    120, 135, 142, 128, 155, 162, 138, 145, 131, 148,
    160, 125, 140, 133, 152, 167, 129, 143, 137, 158,
    172, 119, 146, 136, 150, 155, 141, 134, 163, 127
])

n = len(data_respons)
print("=" * 55)
print("DATA WAKTU RESPONS SERVER (ms)")
print("=" * 55)
print(f"n       = {n}")
print(f"Mean    = {data_respons.mean():.2f} ms")
print(f"Median  = {np.median(data_respons):.2f} ms")
print(f"Std Dev = {data_respons.std(ddof=1):.2f} ms")


def bootstrap_ci(data, stat_func, n_bootstrap=10_000,
                 confidence=0.95, seed=42):
    """
    Hitung Bootstrap Confidence Interval (Metode Percentile).

    Parameters:
    -----------
    data         : array data sampel asli
    stat_func    : fungsi statistik (np.mean, np.median, dll.)
    n_bootstrap  : jumlah bootstrap resamples (default 10.000)
    confidence   : tingkat kepercayaan (default 0.95)
    seed         : random seed untuk reproducibility

    Returns:
    --------
    tuple: (ci_lower, ci_upper, bootstrap_statistics)
    """
    np.random.seed(seed)
    n = len(data)

    bootstrap_stats = np.array([
        stat_func(np.random.choice(data, size=n, replace=True))
        for _ in range(n_bootstrap)
    ])

    alpha   = 1 - confidence
    ci_lo   = np.percentile(bootstrap_stats, 100 * alpha / 2)
    ci_hi   = np.percentile(bootstrap_stats, 100 * (1 - alpha / 2))

    return ci_lo, ci_hi, bootstrap_stats


# Bootstrap CI untuk MEAN
ci_lo_mean, ci_hi_mean, boot_means = bootstrap_ci(data_respons, np.mean)
print(f"\nBootstrap 95% CI (Mean)   : ({ci_lo_mean:.2f}, {ci_hi_mean:.2f}) ms")

# Bootstrap CI untuk MEDIAN (tidak ada formula sederhana untuk ini!)
ci_lo_med, ci_hi_med, boot_meds = bootstrap_ci(data_respons, np.median)
print(f"Bootstrap 95% CI (Median) : ({ci_lo_med:.2f}, {ci_hi_med:.2f}) ms")

# Formula-based CI (t-interval) untuk perbandingan
se     = data_respons.std(ddof=1) / np.sqrt(n)
t_ci   = stats.t.interval(confidence=0.95, df=n-1, loc=data_respons.mean(), scale=se)
print(f"Formula t-based 95% CI    : ({t_ci[0]:.2f}, {t_ci[1]:.2f}) ms")
```

### 6.9.4 Bootstrap untuk Berbagai Statistik

Kekuatan utama bootstrap adalah kemampuannya menghitung CI untuk **statistik apapun**, termasuk yang tidak memiliki formula closed-form.

```python
# === BOOTSTRAP UNTUK BERBAGAI STATISTIK ===

np.random.seed(42)
# Data penghasilan bulanan (Juta Rp) — distribusi log-normal (skewed)
data_penghasilan = np.array([
    4.2, 6.8, 3.1, 12.5, 5.5, 7.3, 4.9, 8.1, 3.7, 15.2,
    5.0, 6.2, 4.5, 9.8, 3.3, 7.1, 5.8, 22.0, 4.1, 6.5,
    3.9, 8.4, 5.2, 11.3, 4.6, 7.8, 6.0, 3.5, 9.1, 5.4
])

statistik_dict = {
    'Mean'      : np.mean,
    'Median'    : np.median,
    'Std Dev'   : lambda x: np.std(x, ddof=1),
    'IQR'       : lambda x: np.percentile(x, 75) - np.percentile(x, 25),
    'Maks/Min'  : lambda x: x.max() / x.min(),
}

print("=" * 65)
print("BOOTSTRAP 95% CI UNTUK BERBAGAI STATISTIK")
print("(Data: Penghasilan Bulanan, n=30)")
print("=" * 65)
print(f"\n{'Statistik':<12} {'Nilai Sampel':>14} {'CI Lower':>10} {'CI Upper':>10}")
print("-" * 50)

for nama, func in statistik_dict.items():
    nilai_asli = func(data_penghasilan)
    ci_lo, ci_hi, _ = bootstrap_ci(data_penghasilan, func)
    print(f"{nama:<12} {nilai_asli:>14.3f} {ci_lo:>10.3f} {ci_hi:>10.3f}")
```

### 6.9.5 Perbandingan Bootstrap vs Formula-Based CI

| Aspek | Formula (t-interval) | Bootstrap |
|-------|---------------------|-----------|
| **Asumsi distribusi** | Normal atau n besar | Minimal |
| **Statistik yang bisa diestimasi** | Terutama mean | Statistik apapun |
| **Implementasi** | Rumus langsung | Simulasi komputer |
| **Kecepatan** | Sangat cepat | Lebih lambat (tapi tetap cepat) |
| **n kecil, distribusi skewed** | Bisa tidak akurat | Lebih andal |
| **Kapan digunakan** | n ≥ 30, data mendekati Normal | Selalu, terutama jika asumsi tidak terpenuhi |

**Kesimpulan praktis:** Ketika ada keraguan tentang normalitas atau ketika mengestimasi statistik selain mean, gunakan bootstrap. Ketika data Normal dan kita mengestimasi mean, kedua metode memberikan hasil yang hampir identik.

---

## 6.10 Studi Kasus: Survei di Indonesia

### 6.10.1 Kasus 1 — Survei BPS: Rata-rata Pengeluaran Rumah Tangga

BPS secara rutin melakukan survei pengeluaran rumah tangga melalui SUSENAS. Data pengeluaran cenderung **right-skewed** (karena beberapa rumah tangga kaya dengan pengeluaran sangat tinggi). Kita akan mensimulasikan situasi ini dan membandingkan estimasi formula vs bootstrap.

```python
# === STUDI KASUS 1: SIMULASI SURVEI SUSENAS ===
np.random.seed(42)

# Populasi pengeluaran rumah tangga (Juta Rp/bulan), distribusi log-normal
N_pop = 50_000
populasi_pengeluaran = np.random.lognormal(mean=1.6, sigma=0.7, size=N_pop)

mu_pop    = populasi_pengeluaran.mean()
med_pop   = np.median(populasi_pengeluaran)

print("=" * 55)
print("PARAMETER POPULASI (Sesungguhnya tidak diketahui BPS)")
print("=" * 55)
print(f"N     = {N_pop:,}")
print(f"Mean  = Rp {mu_pop:.3f} juta/bulan")
print(f"Median= Rp {med_pop:.3f} juta/bulan")
print(f"Std   = Rp {populasi_pengeluaran.std():.3f} juta/bulan")

# BPS mengambil sampel n=300 (disederhanakan)
sampel_bps = np.random.choice(populasi_pengeluaran, size=300, replace=False)

print(f"\n{'='*55}")
print("HASIL SAMPEL (n=300)")
print(f"{'='*55}")
print(f"Mean sampel  : Rp {sampel_bps.mean():.3f} juta/bulan")
print(f"Median sampel: Rp {np.median(sampel_bps):.3f} juta/bulan")

# CI formula untuk mean
n    = len(sampel_bps)
se   = sampel_bps.std(ddof=1) / np.sqrt(n)
ci_f = stats.t.interval(0.95, df=n-1, loc=sampel_bps.mean(), scale=se)
print(f"\n95% CI Mean (Formula) : (Rp {ci_f[0]:.3f}, Rp {ci_f[1]:.3f}) juta")

# Bootstrap CI untuk mean dan median
ci_lo_m, ci_hi_m, _ = bootstrap_ci(sampel_bps, np.mean, seed=42)
ci_lo_med2, ci_hi_med2, _ = bootstrap_ci(sampel_bps, np.median, seed=42)
print(f"95% CI Mean (Bootstrap): (Rp {ci_lo_m:.3f}, Rp {ci_hi_m:.3f}) juta")
print(f"95% CI Median (Bootstrap): (Rp {ci_lo_med2:.3f}, Rp {ci_hi_med2:.3f}) juta")

print(f"\nApakah CI formula menangkap μ? {ci_f[0] <= mu_pop <= ci_f[1]}")
print(f"Apakah CI bootstrap (mean) menangkap μ? {ci_lo_m <= mu_pop <= ci_hi_m}")
print(f"Apakah CI bootstrap (median) menangkap median pop? {ci_lo_med2 <= med_pop <= ci_hi_med2}")
```

### 6.10.2 Kasus 2 — Polling Politik: Elektabilitas dengan Margin of Error

```python
# === STUDI KASUS 2: POLLING PILKADA ===

# Survei elektabilitas Pilkada Gubernur
# 800 responden, 3 kandidat

np.random.seed(42)
n_poll = 800

# Proporsi "sebenarnya" di populasi (tidak diketahui)
p_true_A = 0.42
p_true_B = 0.35
p_true_C = 0.23

# Simulasi hasil survei
hasil_survei = np.random.choice(['A', 'B', 'C'],
                                 size=n_poll,
                                 p=[p_true_A, p_true_B, p_true_C])

# Hitung proporsi sampel
unique, counts = np.unique(hasil_survei, return_counts=True)
prop_dict = dict(zip(unique, counts / n_poll))

print("=" * 60)
print(f"HASIL POLLING PILKADA (n = {n_poll} responden)")
print("=" * 60)
print(f"\n{'Kandidat':>10} | {'Jumlah':>8} | {'Proporsi':>10} | {'95% CI':>22}")
print("-" * 57)

for kandidat in ['A', 'B', 'C']:
    p_hat  = prop_dict[kandidat]
    se_p   = np.sqrt(p_hat * (1 - p_hat) / n_poll)
    me     = 1.960 * se_p
    ci_lo  = p_hat - me
    ci_hi  = p_hat + me
    jumlah = int(p_hat * n_poll)
    print(f"{'Kandidat ' + kandidat:>10} | {jumlah:>8} | "
          f"{p_hat*100:>8.1f}%  | ({ci_lo*100:.1f}%, {ci_hi*100:.1f}%)")

print(f"\nMargin of Error keseluruhan: ±{1.960 * np.sqrt(0.5*0.5/n_poll)*100:.1f}%")
print()
print("INTERPRETASI:")
print("- Kandidat A unggul, tetapi CI perlu diperiksa apakah")
print("  selisihnya signifikan dibanding B.")
print("- Jika CI Kandidat A dan B tumpang tindih, perbedaan")
print("  tidak dapat dinyatakan signifikan secara statistik.")
```

### 6.10.3 Desain Sampling BPS dalam Praktik

```
CONTOH DESAIN SAMPLING SUSENAS BPS:

Level 1 (Cluster): Pilih kabupaten/kota secara acak
      │
      ▼
Level 2 (Cluster): Pilih kecamatan dari kab/kota terpilih
      │
      ▼
Level 3 (Cluster): Pilih desa/kelurahan dari kecamatan terpilih
      │
      ▼
Level 4 (Stratified): Pilih rumah tangga secara stratified
      │              (perkotaan vs perdesaan)
      ▼
Level 5 (SRS): Ambil sampel akhir dari setiap blok sensus

Ini disebut: Multi-Stage Cluster Sampling
Digunakan karena: Tidak ada daftar lengkap rumah tangga Indonesia
```

---

## AI Corner

### Menggunakan AI untuk Sampling dan Estimasi

Kecerdasan buatan dapat menjadi asisten yang berguna dalam belajar statistik, tetapi perlu digunakan dengan kritis dan bijak.

**Prompt 1 — Memilih Teknik Sampling:**
> "Saya akan melakukan penelitian skripsi tentang tingkat literasi digital mahasiswa di Universitas Al Azhar Indonesia. Ada 5 fakultas dengan jumlah mahasiswa yang sangat berbeda (terbesar 2.000 mahasiswa, terkecil 300 mahasiswa). Saya hanya punya waktu dan dana untuk mewawancarai 150 mahasiswa. Teknik sampling apa yang paling tepat? Jelaskan langkah-langkahnya."

**Prompt 2 — Interpretasi Confidence Interval:**
> "Dari survei saya terhadap 120 mahasiswa, diperoleh rata-rata waktu belajar per minggu = 18.5 jam dengan SD = 6.2 jam. Hitung 95% confidence interval dan berikan interpretasi yang benar. Koreksi saya jika interpretasi berikut salah: 'Ada 95% kemungkinan bahwa rata-rata waktu belajar mahasiswa UAI berada di antara nilai CI yang saya hitung.'"

**Prompt 3 — Kapan Pakai Bootstrap:**
> "Saya memiliki data pendapatan 25 wirausahawan muda Indonesia yang sangat skewed ke kanan (beberapa orang pendapatannya jauh di atas rata-rata). Saya ingin membuat confidence interval untuk rata-rata dan median pendapatan. Haruskah saya menggunakan formula t-interval atau bootstrap? Berikan kode Python untuk keduanya."

**Prompt 4 — Debug Kode:**
> "Kode Python bootstrap saya menghasilkan CI yang aneh (lower > upper). Bantu saya menemukan kesalahan. [Tempelkan kode]"

**Hal yang perlu diingat saat menggunakan AI:**
- AI dapat menjelaskan konsep dengan baik, tetapi **selalu verifikasi rumus** dengan buku teks
- Kode yang dihasilkan AI tidak selalu benar — selalu **jalankan sendiri** dan periksa hasilnya
- Untuk interpretasi statistik, AI sering memberikan **miskonsepsi umum** — selalu bandingkan dengan definisi formal
- AI sangat berguna untuk: brainstorming, penjelasan ulang dengan bahasa berbeda, dan debugging kode

---

## Rangkuman Bab 6

**Poin-poin utama yang harus dikuasai:**

1. **Sampling adalah dasar inferensi statistik.** Kita menggunakan statistik sampel (x̄, s, p̂) untuk mengestimasi parameter populasi (μ, σ, p) yang tidak diketahui. Kualitas inferensi sangat bergantung pada **kualitas sampling**, bukan hanya ukuran sampel.

2. **Empat teknik probability sampling** memiliki trade-off masing-masing: SRS (sederhana, butuh frame lengkap), Stratified (presisi terbaik, butuh info strata), Systematic (mudah dilaksanakan, awas periodisitas), Cluster (murah dan praktis, variance terbesar).

3. **Sampling bias adalah musuh utama.** Bias tidak bisa diatasi dengan menambah n — hanya prosedur sampling yang benar yang bisa mencegahnya. Kenali dan hindari: selection bias, non-response bias, dan survivorship bias.

4. **Standard Error (SE = s/√n)** mengukur variabilitas estimasi, bukan variabilitas data. SE mengecil proporsional terhadap √n — untuk mempersempit CI dua kali lipat, ukuran sampel harus diperbesar **empat kali lipat**.

5. **Confidence Interval adalah rentang, bukan pernyataan tentang probabilitas suatu nilai.** Interpretasi yang benar: "Prosedur ini menghasilkan interval yang mengandung parameter populasi sebesar X% dari semua pengulangan." Parameter adalah konstanta — bukan variabel acak yang "berada di suatu tempat dengan probabilitas tertentu."

6. **Margin of error berbanding terbalik dengan √n.** Untuk survei Pilpres nasional (ME ≤ 3%), dibutuhkan minimal 1.067 responden. Untuk skripsi (ME ≤ 5%), cukup 385 responden (dengan asumsi proporsi).

7. **Bootstrap adalah teknik resampling yang powerful** karena tidak memerlukan asumsi distribusi dan dapat digunakan untuk statistik apapun — median, IQR, korelasi, rasio, dll. Prinsipnya: resample dari sampel dengan pengembalian sebanyak B kali (B = 10.000), hitung statistik setiap resample, ambil percentile 2.5% dan 97.5% sebagai batas CI.

8. **Dalam praktik Indonesia:** Survei BPS (SUSENAS, Sakernas, RISKESDAS) menggunakan multi-stage cluster sampling karena tidak ada sampling frame lengkap seluruh penduduk. Lembaga survei politik (Litbang Kompas, LSI) umumnya menggunakan stratified random sampling dengan n sekitar 1.000–1.200 responden.

---

## Latihan Soal

### A. Dasar (C1–C2)

**1.** Jelaskan perbedaan antara **parameter** dan **statistik**. Berikan dua contoh masing-masing dalam konteks survei mahasiswa.

**2.** Sebuah peneliti ingin mengetahui rata-rata jam tidur mahasiswa Indonesia. Beri label masing-masing sebagai **Populasi** atau **Sampel**:
   - a) 270 mahasiswa Universitas Al Azhar Indonesia
   - b) 50 mahasiswa yang disurvei via Google Form
   - c) Seluruh mahasiswa aktif di Indonesia
   - d) Rata-rata jam tidur dari 50 mahasiswa tersebut

**3.** Sebutkan **empat teknik probability sampling** dan satu contoh penggunaannya di Indonesia untuk masing-masing teknik.

**4.** Dalam konteks confidence interval 95%, manakah pernyataan yang **BENAR**?
   - a) Ada 95% kemungkinan μ berada dalam interval
   - b) 95% data berada dalam interval
   - c) Prosedur ini menghasilkan interval yang mengandung μ pada 95% pengulangan
   - d) μ pasti berada dalam interval ini

**5.** Hitung **Standard Error** dari sampel berikut: n = 64, s = 16.
   Jelaskan apa artinya nilai SE yang Anda hitung.

**6.** Sebuah polling dengan n = 400 responden mendapatkan p̂ = 0.55.
   Hitunglah **Margin of Error** untuk confidence level 95%.

### B. Menengah (C2–C3)

**7.** Data IPK sampel 25 mahasiswa Informatika UAI memiliki rata-rata x̄ = 3.42 dan standard deviation s = 0.31. Hitunglah:
   - a) Standard Error
   - b) 90% Confidence Interval
   - c) 95% Confidence Interval
   - d) 99% Confidence Interval
   - e) Jelaskan pola yang Anda amati pada lebar CI saat confidence level meningkat

**8.** Sebuah lembaga survei melakukan polling Pilkada dengan hasil: dari 1.500 responden, 720 memilih Kandidat X.
   - a) Hitung proporsi sampel p̂
   - b) Verifikasi apakah syarat penggunaan CI berbasis Normal terpenuhi
   - c) Hitung 95% CI untuk proporsi populasi
   - d) Apakah Kandidat X dapat dinyatakan unggul secara statistik? Jelaskan.

**9.** Seorang peneliti ingin mendesain survei kepuasan pelanggan dengan ketentuan: ME ≤ 4%, confidence level 95%, dan tidak ada informasi awal tentang proporsi.
   - a) Berapa ukuran sampel minimum yang dibutuhkan?
   - b) Jika peneliti hanya memiliki dana untuk 250 responden, berapa ME yang akan didapatkan?

**10.** Identifikasi jenis bias sampling yang terjadi dalam skenario berikut, dan jelaskan mengapa itu bermasalah:
   - a) Survei kepuasan aplikasi mobile yang hanya dikirim ke pengguna aktif (login dalam 7 hari terakhir)
   - b) Peneliti mengestimasi pendapatan rata-rata pengusaha sukses dari wawancara di majalah Forbes Indonesia
   - c) Kuesioner skripsi yang hanya disebarkan kepada teman-teman mahasiswa peneliti di grup WhatsApp

### C. Mahir (C3–C4)

**11.** Perhatikan tabel berikut tentang distribusi mahasiswa UAI berdasarkan fakultas:

| Fakultas | Jumlah Mahasiswa |
|----------|-----------------|
| Teknologi Informasi | 850 |
| Ekonomi dan Bisnis | 1.200 |
| Ilmu Sosial | 650 |
| Teknik | 500 |
| Kesehatan | 300 |

Anda ingin melakukan survei kepuasan akademik dengan n = 200 responden total menggunakan **stratified proportional sampling**.

   a) Tentukan jumlah sampel dari masing-masing fakultas
   b) Tuliskan kode Python untuk mengimplementasikan stratified sampling ini
   c) Mengapa stratified sampling lebih tepat dibanding SRS dalam kasus ini?
   d) Jika Anda menggunakan SRS dan secara kebetulan tidak ada satupun mahasiswa Kesehatan yang terpilih, apa konsekuensinya bagi validitas hasil survei?

**12.** Data berikut adalah waktu penyelesaian tugas (menit) dari sampel 20 mahasiswa dalam sebuah praktikum:

```
[45, 52, 38, 67, 41, 59, 73, 48, 55, 62,
 44, 71, 39, 58, 65, 47, 53, 69, 42, 56]
```

   a) Hitung 95% CI menggunakan formula t-interval (manual dan Python)
   b) Implementasikan bootstrap dengan B = 10.000 untuk menghitung 95% CI
   c) Bandingkan lebar CI dari kedua metode. Apakah hasilnya konsisten? Mengapa?
   d) Hitung juga bootstrap 95% CI untuk **median** waktu penyelesaian. Apakah ada formula sederhana untuk CI median? Jelaskan mengapa bootstrap berguna di sini.
   e) Jika standar kelulusan praktikum adalah "rata-rata harus < 60 menit", apakah data mendukung bahwa rata-rata populasi di bawah 60 menit? Gunakan CI untuk mendukung argumen Anda.

**13.** (Analisis Kritis) Sebuah berita online menulis:
   > "Survei terhadap 10.000 pengguna media sosial menunjukkan bahwa 73% remaja Indonesia mengalami kecemasan akibat media sosial, dengan margin of error hanya ±0.9%. Survei dilakukan melalui pop-up di aplikasi media sosial terpopuler."

   a) Hitung sendiri apakah klaim margin of error ±0.9% konsisten dengan n = 10.000 dan confidence level 95%.
   b) Meskipun n sangat besar, identifikasi minimal **dua jenis bias** yang mungkin membuat hasil survei ini tidak valid.
   c) Jelaskan mengapa "ukuran sampel besar ≠ hasil yang tidak bias."
   d) Desain ulang survei ini agar lebih valid secara metodologis. Apa teknik sampling yang lebih tepat?

---

## Referensi

1. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics* (4th ed.). OpenIntro. Bab 5: Inference for Numerical Data. Tersedia gratis di: https://www.openintro.org/book/os/

2. Bruce, P., & Bruce, A. (2020). *Practical Statistics for Data Scientists* (2nd ed.). O'Reilly Media. Bab 2: Data and Sampling Distributions; Bab 3: Statistical Experiments and Significance Testing.

3. Efron, B., & Tibshirani, R. J. (1993). *An Introduction to the Bootstrap*. Chapman and Hall/CRC. [Referensi klasik untuk metode bootstrap]

4. Lohr, S. L. (2019). *Sampling: Design and Analysis* (3rd ed.). CRC Press. [Referensi komprehensif untuk teknik sampling]

5. Badan Pusat Statistik Indonesia. (2024). *Metodologi Survei Sosial Ekonomi Nasional (SUSENAS)*. BPS RI. https://www.bps.go.id/

6. Wickham, H., & Grolemund, G. (2023). *R for Data Science* (2nd ed.). O'Reilly Media. Bab tentang data import dan tidy data (untuk konteks data riil). Tersedia gratis di: https://r4ds.hadley.nz/

7. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media. Bab 4-5 tentang NumPy dan statistik dengan Python. Tersedia gratis di: https://jakevdp.github.io/PythonDataScienceHandbook/

8. Gelman, A., Hill, J., & Vehtari, A. (2020). *Regression and Other Stories*. Cambridge University Press. Bab 2: Data Collection.

---

*Bab ini merupakan bagian dari buku ajar Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia. Hak cipta dilindungi.*
