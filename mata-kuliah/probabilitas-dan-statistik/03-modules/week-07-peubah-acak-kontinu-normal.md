# Minggu 7: Peubah Acak Kontinu dan Distribusi Normal

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 7 |
| **Topik** | PDF, distribusi Uniform, Eksponensial, dan Normal; skor-z; uji kenormalan |
| **CPL / CPMK** | CPL08 / CPMK081 |
| **Sub-CPMK** | `PS-Sub-CPMK081-1` |
| **Indikator Mingguan** | Memodelkan fenomena kontinu dengan distribusi Uniform, Eksponensial, dan Normal |
| **Level Bloom** | C3 (Menerapkan) |
| **Durasi** | 150 menit tatap muka |
| **Metode** | Kuliah, latihan terbimbing, komputasi |

---

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menjelaskan** (C2) perbedaan PMF dan PDF serta mengapa P(X = x) = 0 pada peubah kontinu.
2. **Menerapkan** (C3) distribusi Uniform dan Eksponensial pada kasus computing.
3. **Menghitung** (C3) probabilitas pada distribusi Normal melalui standardisasi (skor-z).
4. **Menerapkan** (C3) aturan empiris 68–95–99,7 untuk menilai kewajaran sebuah nilai.
5. **Memeriksa** (C4) kenormalan sebuah data dengan histogram, Q-Q plot, dan uji formal.

---

## Materi Pembelajaran

### 1. Dari Diskret ke Kontinu

#### 1.1 Mengapa P(X = x) = 0

Pada peubah acak kontinu, probabilitas satu titik tepat adalah **nol**.

> Berapa probabilitas waktu respons tepat 100,000000… ms? Nol — karena ada tak hingga banyak nilai yang mungkin antara 99 dan 101 ms.

Yang bermakna adalah probabilitas pada **selang**:

$$P(a \le X \le b) = \int_a^b f(x)\,dx$$

```
   PMF (diskret)                    PDF (kontinu)
   ────────────                     ─────────────
    │ █                              │    ╭───╮
    │ █  █                           │   ╱     ╲
    │ █  █  █                        │  ╱       ╲
    │ █  █  █  █                     │ ╱  ▓▓▓▓▓  ╲
    └─┴──┴──┴──┴──                   └────────────────
      tinggi = P(X=x)                 LUAS = P(a≤X≤b)
```

| Aspek | PMF (diskret) | PDF (kontinu) |
|-------|---------------|---------------|
| Notasi | p(x) = P(X = x) | f(x) |
| Nilai | 0 ≤ p(x) ≤ 1 | f(x) ≥ 0, **boleh > 1** |
| Total | Σ p(x) = 1 | ∫ f(x) dx = 1 |
| Probabilitas titik | p(x) | **0** |
| Cara baca | Tinggi batang | **Luas di bawah kurva** |

> **Konsekuensi praktis:** karena P(X = a) = 0, maka P(X ≤ a) = P(X < a). Pada kasus kontinu, tanda "sama dengan" tidak berpengaruh — berbeda dari kasus diskret.

---

### 2. Distribusi Uniform Kontinu

Semua nilai dalam selang [a, b] sama mungkinnya.

$$f(x) = \frac{1}{b-a} \text{ untuk } a \le x \le b \qquad E[X] = \frac{a+b}{2} \qquad \text{Var}(X) = \frac{(b-a)^2}{12}$$

**Contoh Informatika:** waktu tunggu acak pada *exponential backoff* dengan *jitter*; nilai yang dihasilkan `random.random()`; posisi acak dalam *hash table* yang ideal.

```python
from scipy import stats

# Jitter acak antara 0 dan 500 ms pada strategi retry
a, b = 0, 500
X = stats.uniform(loc=a, scale=b - a)

print(f"E[X]              = {X.mean():.2f} ms")
print(f"SD(X)             = {X.std():.2f} ms")
print(f"P(X ≤ 100)        = {X.cdf(100):.4f}")
print(f"P(200 ≤ X ≤ 300)  = {X.cdf(300) - X.cdf(200):.4f}")
```

---

### 3. Distribusi Eksponensial

#### 3.1 Kapan Dipakai

Memodelkan **waktu tunggu sampai kejadian berikutnya**, ketika kejadian mengikuti proses Poisson dengan laju λ.

$$f(x) = \lambda e^{-\lambda x}, \quad x \ge 0 \qquad E[X] = \frac{1}{\lambda} \qquad \text{Var}(X) = \frac{1}{\lambda^2}$$

```
   POISSON                        EKSPONENSIAL
   "berapa kejadian               "berapa lama sampai
    per satuan waktu?"             kejadian berikutnya?"

   diskret, λ per detik           kontinu, rata-rata 1/λ detik

           ← dua sisi mata uang yang sama →
```

#### 3.2 Contoh Terapan

> Server menerima rata-rata 8 permintaan per detik (Poisson, λ = 8). Waktu antar permintaan mengikuti Eksponensial dengan λ = 8.

```python
from scipy import stats

lam = 8                       # 8 permintaan per detik
X = stats.expon(scale=1/lam)  # perhatikan: scipy memakai scale = 1/λ

print(f"Rata-rata waktu antar permintaan : {X.mean()*1000:.2f} ms")
print(f"P(tunggu < 50 ms)                : {X.cdf(0.050):.4f}")
print(f"P(tunggu > 500 ms)               : {X.sf(0.500):.4f}")
print(f"Persentil ke-95 waktu tunggu     : {X.ppf(0.95)*1000:.2f} ms")

# Sifat tanpa memori, versi kontinu
print(f"\nSifat tanpa memori:")
print(f"  P(X > 0.2)            = {X.sf(0.2):.6f}")
print(f"  P(X > 0.3 | X > 0.1)  = {X.sf(0.3)/X.sf(0.1):.6f}")
print("  → Sama. Sudah menunggu 0,1 detik tidak mengubah apa pun.")
```

> **Jebakan `scipy`:** parameter `scale` pada `stats.expon` adalah **1/λ**, bukan λ. Kesalahan ini sangat umum dan menghasilkan jawaban yang salah secara diam-diam — tidak ada galat, hanya angka yang keliru. Selalu periksa dengan `X.mean()`.

---

### 4. Distribusi Normal (Gaussian)

#### 4.1 Rumus dan Bentuk

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

Dua parameter: μ menentukan **letak** puncak, σ menentukan **lebar** kurva.

```
              μ = pusat
                 │
           ╭─────┼─────╮
         ╱       │       ╲
       ╱         │         ╲
     ╱           │           ╲
   ─────────────────────────────
   μ−3σ  μ−2σ  μ−σ  μ  μ+σ  μ+2σ  μ+3σ
   │      │     │        │     │     │
   0,1%  2,1%  13,6%   34,1%  ...
   ←────── 68,27% ──────→
   ←───────── 95,45% ─────────→
   ←──────────── 99,73% ───────────→
```

#### 4.2 Aturan Empiris 68–95–99,7

| Selang | Proporsi Data |
|--------|---------------|
| μ ± 1σ | ≈ 68,27% |
| μ ± 2σ | ≈ 95,45% |
| μ ± 3σ | ≈ 99,73% |

```python
from scipy import stats

mu, sigma = 0, 1
Z = stats.norm(mu, sigma)

for k in [1, 2, 3]:
    p = Z.cdf(k) - Z.cdf(-k)
    print(f"P(μ − {k}σ ≤ X ≤ μ + {k}σ) = {p:.6f}  ({p*100:.2f}%)")
```

> **Penerapan dalam rekayasa:** istilah "Six Sigma" berasal dari sini. Proses yang cacatnya berada di luar μ ± 6σ menghasilkan sekitar 3,4 cacat per satu juta kesempatan.

#### 4.3 Standardisasi: Skor-z

$$z = \frac{x - \mu}{\sigma}$$

Skor-z menyatakan **berapa simpangan baku sebuah nilai berjarak dari rata-rata**. Ia mengubah distribusi Normal apa pun menjadi Normal baku N(0, 1).

**Contoh.** Nilai UAS berdistribusi Normal dengan μ = 72 dan σ = 11.

```python
from scipy import stats

mu, sigma = 72, 11
X = stats.norm(mu, sigma)

nilai = 88
z = (nilai - mu) / sigma

print(f"Nilai {nilai}:")
print(f"  Skor-z         = {z:.4f}")
print(f"  P(X < {nilai})     = {X.cdf(nilai):.4f}  → peringkat persentil {X.cdf(nilai)*100:.1f}")
print(f"  P(X > {nilai})     = {X.sf(nilai):.4f}")

# Berapa nilai yang diperlukan untuk masuk 10% teratas?
batas = X.ppf(0.90)
print(f"\nBatas 10% teratas : {batas:.2f}")
print(f"Batas 25% terbawah: {X.ppf(0.25):.2f}")

# Membandingkan dua mahasiswa dari dua mata kuliah berbeda
print("\nPerbandingan lintas mata kuliah:")
# Mahasiswa A: nilai 85 di MK dengan μ=75, σ=8
zA = (85 - 75) / 8
# Mahasiswa B: nilai 78 di MK dengan μ=65, σ=6
zB = (78 - 65) / 6
print(f"  A: nilai 85 (μ=75, σ=8)  → z = {zA:.3f}")
print(f"  B: nilai 78 (μ=65, σ=6)  → z = {zB:.3f}")
print(f"  → {'B' if zB > zA else 'A'} berprestasi relatif lebih baik.")
```

> **Inilah kegunaan skor-z:** membandingkan nilai dari dua sebaran yang berbeda. Nilai mentah 85 dan 78 tidak bisa dibandingkan langsung; skor-z membuatnya bisa.

#### 4.4 Mengapa Distribusi Normal Muncul Di Mana-Mana

Bukan kebetulan. **Teorema Limit Pusat** (Minggu 9) menjelaskan bahwa jumlah atau rata-rata dari banyak pengaruh acak kecil yang saling bebas akan mendekati Normal — berapa pun bentuk sebaran aslinya.

> **Tetapi hati-hati:** tidak semua hal berdistribusi Normal. Waktu respons, ukuran berkas, penghasilan, dan jumlah pengikut **hampir selalu menceng kanan**, bukan Normal. Mengasumsikan kenormalan tanpa memeriksanya adalah kesalahan yang sering berakibat fatal pada kesimpulan.

---

### 5. Memeriksa Kenormalan

Tiga cara, dari yang paling longgar ke paling ketat.

#### 5.1 Pemeriksaan Visual: Histogram dan Q-Q Plot

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("nilai_mahasiswa_if.csv")
data = df["nilai_uas"].dropna()

fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

# (1) Histogram dengan kurva Normal pembanding
axes[0].hist(data, bins=20, density=True, color="steelblue",
             edgecolor="white", alpha=0.8)
x = np.linspace(data.min(), data.max(), 200)
axes[0].plot(x, stats.norm.pdf(x, data.mean(), data.std(ddof=1)),
             color="#c0392b", linewidth=2, label="Normal teoretis")
axes[0].set_title("Histogram vs kurva Normal")
axes[0].legend()

# (2) Q-Q plot: titik harus mengikuti garis diagonal
stats.probplot(data, dist="norm", plot=axes[1])
axes[1].set_title("Q-Q Plot")

# (3) Boxplot untuk melihat simetri dan pencilan
axes[2].boxplot(data, vert=True)
axes[2].set_title("Boxplot")

plt.tight_layout()
plt.show()
```

**Cara membaca Q-Q plot:**

```
   NORMAL                 EKOR BERAT            MENCENG KANAN
    ·                       ·                       ··
   ··                      ·                      ··
  ··                     ··                     ···
 ··                   ···                    ····
··                 ···                    ···
titik di garis     melengkung S          melengkung ke atas
```

#### 5.2 Statistik Kemencengan dan Kurtosis

```python
from scipy import stats

kemencengan = stats.skew(data)
kurtosis = stats.kurtosis(data)   # kurtosis berlebih: Normal = 0

print(f"Kemencengan : {kemencengan:>7.4f}   (Normal ≈ 0)")
print(f"Kurtosis    : {kurtosis:>7.4f}   (Normal ≈ 0)")

if abs(kemencengan) < 0.5 and abs(kurtosis) < 1:
    print("→ Bentuk mendekati Normal.")
else:
    print("→ Menyimpang dari Normal; periksa lebih lanjut.")
```

#### 5.3 Uji Formal

```python
from scipy import stats

# Shapiro-Wilk: kuat untuk n kecil-menengah (n < 5000)
stat_sw, p_sw = stats.shapiro(data)
print(f"Shapiro-Wilk     : W = {stat_sw:.4f}, p-value = {p_sw:.6f}")

# Kolmogorov-Smirnov terhadap Normal dengan parameter dari data
stat_ks, p_ks = stats.kstest(
    data, "norm", args=(data.mean(), data.std(ddof=1))
)
print(f"Kolmogorov-Smirnov: D = {stat_ks:.4f}, p-value = {p_ks:.6f}")

alpha = 0.05
print(f"\nDengan α = {alpha}:")
if p_sw > alpha:
    print("  Shapiro-Wilk: tidak ada bukti cukup untuk menolak kenormalan.")
else:
    print("  Shapiro-Wilk: data menyimpang signifikan dari Normal.")
```

> **Peringatan penting tentang uji kenormalan.** Pada sampel yang sangat besar, uji formal hampir selalu menolak kenormalan — karena penyimpangan sekecil apa pun menjadi "signifikan". Sebaliknya, pada sampel kecil uji ini lemah dan jarang menolak apa pun.
>
> Karena itu **pemeriksaan visual (Q-Q plot) sering lebih informatif** daripada nilai p. Pertanyaan yang tepat bukan "apakah data ini persis Normal?" (jawabannya hampir selalu tidak) melainkan **"apakah penyimpangannya cukup kecil sehingga metode yang mengandaikan kenormalan masih layak dipakai?"**
>
> Kita akan kembali ke pertanyaan ini pada Minggu 11–12 ketika membahas asumsi uji-t.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (Mandiri — 60 menit)

1. Membaca [Bab 7 buku ajar](../06-buku-ajar/bab-07-distribusi-kontinu-normal.md).
2. Menyiapkan tabel distribusi Normal baku (dibagikan di LMS) — akan dipakai saat UTS.
3. Mencatat: mengapa luas di bawah kurva PDF harus sama dengan 1?

### Di Kelas (150 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–10' | Pembahasan Lab 06 |
| 10–35' | Kuliah: PDF vs PMF; mengapa P(X = x) = 0 |
| 35–55' | Kuliah + latihan: distribusi Uniform dan Eksponensial; hubungan Poisson–Eksponensial |
| 55–65' | Istirahat |
| 65–100' | Kuliah + latihan: distribusi Normal, aturan empiris, standardisasi skor-z |
| 100–120' | **Latihan terbimbing:** membaca tabel Normal secara manual (persiapan UTS) |
| 120–140' | Studio: memeriksa kenormalan data nyata dengan Q-Q plot dan Shapiro-Wilk |
| 140–150' | **Kisi-kisi UTS** dan strategi belajar |

#### Latihan Terbimbing: Membaca Tabel Normal

Karena UTS bersifat *closed book* tanpa komputer, mahasiswa harus terampil membaca tabel Normal baku.

Waktu kompilasi proyek berdistribusi Normal dengan μ = 45 detik dan σ = 8 detik. Hitung **secara manual** menggunakan tabel:

1. P(X < 50)
2. P(X > 60)
3. P(38 < X < 52)
4. Berapa waktu yang dilampaui hanya oleh 5% kompilasi terlambat?
5. Bila sebuah kompilasi memakan 70 detik, berapa skor-z-nya? Apakah itu wajar?

Setelah selesai manual, verifikasi seluruhnya dengan Python.

### Setelah Kelas (Mandiri — 180 menit)

1. Mengerjakan [Lab 07](../04-labs/lab-07-distribusi-kontinu-uji-kenormalan.md).
2. Mengerjakan Latihan Soal Bab 7.
3. **Mulai persiapan UTS** — pelajari [kisi-kisi](../05-assessments/kisi-kisi-uts.md).

---

## Penugasan

| Kode | Tugas | Bobot | Batas Waktu |
|------|-------|-------|-------------|
| T-07 | Laporan Lab 07 — Distribusi kontinu dan uji kenormalan | 1,92% | Sebelum kelas Minggu 8 |

---

## Rangkuman

1. Pada peubah acak kontinu, **P(X = x) = 0**; yang bermakna adalah probabilitas pada selang, dihitung sebagai **luas di bawah PDF**.
2. **PDF boleh bernilai lebih dari 1** — yang harus sama dengan 1 adalah luas totalnya, bukan tingginya.
3. **Uniform** untuk nilai yang sama mungkinnya; **Eksponensial** untuk waktu tunggu antar kejadian Poisson.
4. Eksponensial bersifat **tanpa memori**, sama seperti Geometrik pada kasus diskret.
5. Pada `scipy.stats.expon`, parameter `scale` adalah **1/λ**, bukan λ. Selalu periksa dengan `.mean()`.
6. **Aturan empiris 68–95–99,7** memberi cara cepat menilai kewajaran sebuah nilai pada sebaran Normal.
7. **Skor-z** memungkinkan perbandingan nilai dari dua sebaran berbeda.
8. **Tidak semua data Normal.** Waktu respons, ukuran berkas, dan penghasilan hampir selalu menceng kanan. Periksa dengan **Q-Q plot**, bukan hanya dengan uji formal — pada sampel besar uji formal hampir selalu menolak kenormalan.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 4, 6. Pearson.
2. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.), Bab 4. Wiley.
3. Ghasemi, A., & Zahediasl, S. (2012). Normality tests for statistical analysis. *International Journal of Endocrinology and Metabolism*, 10(2), 486–489.
4. Dokumentasi SciPy — *Continuous distributions*. <https://docs.scipy.org/doc/scipy/reference/stats.html#continuous-distributions>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
