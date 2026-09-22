# Minggu 6: Peubah Acak Diskret dan Distribusinya

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 6 |
| **Topik** | Peubah acak diskret, PMF dan CDF, distribusi Bernoulli, Binomial, Poisson, Geometrik |
| **CPL / CPMK** | CPL08 / CPMK081 |
| **Sub-CPMK** | `PS-Sub-CPMK081-1` |
| **Indikator Mingguan** | Memodelkan fenomena diskret dengan distribusi Bernoulli, Binomial, Poisson, dan Geometrik |
| **Level Bloom** | C3 (Menerapkan) |
| **Durasi** | 150 menit tatap muka |
| **Metode** | Kuliah, pemodelan kasus, komputasi `scipy.stats` |

---

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Membedakan** (C2) peubah acak diskret dan kontinu serta menjelaskan PMF dan CDF.
2. **Menerapkan** (C3) distribusi Bernoulli dan Binomial untuk memodelkan percobaan dengan dua hasil.
3. **Menerapkan** (C3) distribusi Poisson untuk memodelkan jumlah kejadian per satuan waktu atau ruang.
4. **Menerapkan** (C3) distribusi Geometrik untuk memodelkan percobaan sampai keberhasilan pertama.
5. **Menentukan** (C4) distribusi yang tepat untuk sebuah fenomena berdasarkan ciri-cirinya.

---

## Materi Pembelajaran

### 1. Peubah Acak

#### 1.1 Definisi

> **Peubah acak** adalah fungsi yang memetakan setiap hasil dalam ruang sampel ke sebuah bilangan real.

```
   Ruang sampel S                    Bilangan real
   ┌──────────────┐                  ─────────────
   │ LLL  LLG     │      X = jumlah        0
   │ LGL  LGG     │  ───  modul gagal ───→ 1
   │ GLL  GLG     │                        2
   │ GGL  GGG     │                        3
   └──────────────┘
```

Peubah acak memungkinkan kita berpindah dari "hasil percobaan" ke "angka yang bisa dihitung rata-rata dan variansnya".

| Jenis | Ciri | Contoh Informatika |
|-------|------|--------------------|
| **Diskret** | Nilai terhitung (bilangan bulat, terbatas atau tak terbatas) | Jumlah bug, jumlah permintaan, jumlah percobaan login |
| **Kontinu** | Nilai dalam selang bilangan real | Waktu respons, ukuran berkas, suhu prosesor |

Minggu ini membahas yang diskret; minggu depan yang kontinu.

#### 1.2 PMF dan CDF

| Fungsi | Lambang | Definisi | Sifat |
|--------|---------|----------|-------|
| **PMF** (*probability mass function*) | p(x) = P(X = x) | Probabilitas X bernilai tepat x | p(x) ≥ 0 dan Σ p(x) = 1 |
| **CDF** (*cumulative distribution function*) | F(x) = P(X ≤ x) | Probabilitas X tidak melebihi x | Tidak turun, dari 0 ke 1 |

```python
import numpy as np
import matplotlib.pyplot as plt

# Contoh: X = jumlah modul gagal dari 3 modul, tiap modul gagal 20%
from scipy import stats

n, p = 3, 0.20
x = np.arange(0, n + 1)
pmf = stats.binom.pmf(x, n, p)
cdf = stats.binom.cdf(x, n, p)

print("x   P(X=x)    P(X≤x)")
for xi, pm, cd in zip(x, pmf, cdf):
    print(f"{xi}   {pm:.4f}    {cd:.4f}")
print(f"\nJumlah seluruh PMF = {pmf.sum():.4f}  (harus 1)")

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].bar(x, pmf, color="steelblue", edgecolor="white")
axes[0].set_title("PMF: P(X = x)")
axes[0].set_xlabel("Jumlah modul gagal")
axes[1].step(x, cdf, where="post", linewidth=2, color="#c0392b")
axes[1].set_title("CDF: P(X ≤ x)")
axes[1].set_xlabel("Jumlah modul gagal")
axes[1].set_ylim(0, 1.05)
plt.tight_layout()
plt.show()
```

---

### 2. Distribusi Bernoulli

**Satu percobaan dengan dua hasil:** berhasil (1) dengan probabilitas p, gagal (0) dengan probabilitas 1−p.

$$P(X = x) = p^x (1-p)^{1-x}, \quad x \in \{0, 1\}$$

$$E[X] = p \qquad \text{Var}(X) = p(1-p)$$

**Contoh Informatika:** satu permintaan HTTP berhasil atau gagal; satu pengguna melakukan konversi atau tidak; satu berkas lolos validasi atau tidak.

> Bernoulli adalah **batu bata dasar**. Distribusi Binomial dan Geometrik dibangun dari rangkaian percobaan Bernoulli.

---

### 3. Distribusi Binomial

#### 3.1 Kapan Dipakai

Empat syarat (disingkat **BINS**):

1. **B**inary — tiap percobaan punya tepat dua hasil.
2. **I**ndependent — percobaan saling bebas.
3. **N**umber fixed — jumlah percobaan n ditetapkan di awal.
4. **S**ame probability — probabilitas keberhasilan p sama tiap percobaan.

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

$$E[X] = np \qquad \text{Var}(X) = np(1-p)$$

#### 3.2 Contoh Terapan

> Sebuah *load balancer* meneruskan permintaan ke 20 server. Setiap server punya probabilitas 5% mengembalikan galat, dan kegagalan antar server saling bebas.
>
> (a) Berapa probabilitas tepat 2 server mengembalikan galat?
> (b) Berapa probabilitas **sedikitnya** 3 server galat?
> (c) Berapa rata-rata jumlah server yang galat?

```python
from scipy import stats

n, p = 20, 0.05
X = stats.binom(n, p)

# (a) tepat 2
print(f"(a) P(X = 2)  = {X.pmf(2):.4f}")

# (b) sedikitnya 3  →  1 − P(X ≤ 2)
print(f"(b) P(X ≥ 3)  = {1 - X.cdf(2):.4f}")
#     bisa juga dengan survival function, lebih akurat secara numerik
print(f"    (sf)      = {X.sf(2):.4f}")

# (c) nilai harapan dan varians
print(f"(c) E[X]      = {X.mean():.4f}   (= n·p = {n*p})")
print(f"    Var(X)    = {X.var():.4f}    (= n·p·(1−p) = {n*p*(1-p)})")
print(f"    SD(X)     = {X.std():.4f}")
```

#### 3.3 Bentuk Distribusi dan Pengaruh p

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

n = 20
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for ax, p in zip(axes, [0.1, 0.5, 0.85]):
    x = np.arange(0, n + 1)
    ax.bar(x, stats.binom.pmf(x, n, p), color="steelblue", edgecolor="white")
    ax.set_title(f"Binomial(n={n}, p={p})\nmean = {n*p:.1f}")
    ax.set_xlabel("k")
axes[0].set_ylabel("P(X = k)")
plt.suptitle("p < 0,5 menceng kanan · p = 0,5 simetris · p > 0,5 menceng kiri", y=1.02)
plt.tight_layout()
plt.show()
```

---

### 4. Distribusi Poisson

#### 4.1 Kapan Dipakai

Memodelkan **jumlah kejadian dalam satuan waktu, ruang, atau volume tertentu**, ketika:

1. Kejadian terjadi secara bebas satu sama lain.
2. Laju rata-rata λ (lambda) konstan.
3. Dua kejadian tidak mungkin terjadi pada saat yang persis sama.

$$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \ldots$$

$$E[X] = \lambda \qquad \text{Var}(X) = \lambda$$

> **Ciri khas Poisson:** mean dan varians **sama**. Bila pada data nyata varians jauh lebih besar dari mean (*overdispersion*), Poisson bukan model yang tepat.

#### 4.2 Contoh Terapan

> Sebuah server menerima rata-rata **8 permintaan per detik**.
>
> (a) Berapa probabilitas tepat 5 permintaan dalam satu detik?
> (b) Berapa probabilitas lebih dari 15 permintaan dalam satu detik?
> (c) Berapa kapasitas yang harus disiapkan agar 99% dari waktu tidak kewalahan?

```python
from scipy import stats

lam = 8
X = stats.poisson(lam)

print(f"(a) P(X = 5)   = {X.pmf(5):.4f}")
print(f"(b) P(X > 15)  = {X.sf(15):.6f}")

# (c) kuantil ke-99: kapasitas minimum
kapasitas = X.ppf(0.99)
print(f"(c) Kapasitas 99% = {kapasitas:.0f} permintaan/detik")
print(f"    Verifikasi: P(X ≤ {kapasitas:.0f}) = {X.cdf(kapasitas):.4f}")

# Bandingkan beberapa tingkat layanan
print("\nKapasitas menurut tingkat layanan:")
for level in [0.90, 0.95, 0.99, 0.999]:
    print(f"  {level*100:5.1f}% → {X.ppf(level):.0f} permintaan/detik")
```

> **Wawasan perencanaan kapasitas:** merancang server untuk kapasitas rata-rata (8/detik) berarti sistem kewalahan hampir separuh waktu. Untuk 99% ketersediaan diperlukan kapasitas 15 — hampir dua kali rata-rata. Inilah alasan *over-provisioning* dalam rekayasa sistem bukan pemborosan, melainkan konsekuensi matematis dari variabilitas.

#### 4.3 Poisson Sebagai Hampiran Binomial

Ketika n besar dan p kecil, Binomial(n, p) ≈ Poisson(λ = np).

```python
import numpy as np
from scipy import stats

n, p = 1000, 0.008
lam = n * p

x = np.arange(0, 25)
binom_pmf = stats.binom.pmf(x, n, p)
pois_pmf = stats.poisson.pmf(x, lam)

print("k   Binomial    Poisson     Selisih")
for k in range(0, 16, 3):
    print(f"{k:2d}  {binom_pmf[k]:.6f}  {pois_pmf[k]:.6f}  "
          f"{abs(binom_pmf[k]-pois_pmf[k]):.2e}")
```

> Hampiran ini berguna ketika n sangat besar sehingga menghitung C(n,k) menjadi mahal — misalnya "berapa probabilitas tepat 3 dari 10 juta permintaan mengalami *race condition*".

---

### 5. Distribusi Geometrik

#### 5.1 Kapan Dipakai

Memodelkan **jumlah percobaan sampai keberhasilan pertama**.

$$P(X = k) = (1-p)^{k-1} p, \quad k = 1, 2, 3, \ldots$$

$$E[X] = \frac{1}{p} \qquad \text{Var}(X) = \frac{1-p}{p^2}$$

#### 5.2 Contoh Terapan

> Sebuah klien mencoba menyambung ke server. Setiap percobaan berhasil dengan probabilitas 0,3 (jaringan tidak stabil).
>
> (a) Berapa probabilitas berhasil tepat pada percobaan ke-4?
> (b) Berapa rata-rata jumlah percobaan sampai berhasil?
> (c) Berapa probabilitas butuh lebih dari 5 percobaan?

```python
from scipy import stats

p = 0.3
X = stats.geom(p)

print(f"(a) P(X = 4)  = {X.pmf(4):.4f}")
print(f"(b) E[X]      = {X.mean():.4f}  (= 1/p = {1/p:.4f})")
print(f"(c) P(X > 5)  = {X.sf(5):.4f}")

# Sifat "tanpa memori": gagal 3 kali tidak membuat percobaan ke-4 lebih mungkin
print(f"\nSifat tanpa memori:")
print(f"  P(X > 5)         = {X.sf(5):.6f}")
print(f"  P(X > 8 | X > 3) = {X.sf(8)/X.sf(3):.6f}")
print("  → Sama. Koin tidak 'ingat' sudah gagal berapa kali.")
```

> **Sifat tanpa memori (*memoryless*)** adalah ciri khas distribusi Geometrik (dan Eksponensial pada kasus kontinu). Sistem *retry* yang dirancang dengan asumsi "sudah gagal banyak, pasti sebentar lagi berhasil" berpijak pada kekeliruan ini — dikenal sebagai *gambler's fallacy*.

---

### 6. Memilih Distribusi yang Tepat

```
  Pertanyaannya apa?
  │
  ├── "Berhasil atau gagal?" (satu kali)          → BERNOULLI
  │
  ├── "Berapa kali berhasil dari n percobaan?"    → BINOMIAL
  │     syarat: n tetap, p sama, saling bebas
  │
  ├── "Berapa kejadian per satuan waktu/ruang?"   → POISSON
  │     syarat: laju λ konstan, kejadian bebas
  │
  └── "Percobaan ke berapa baru berhasil?"        → GEOMETRIK
        syarat: p sama, saling bebas
```

| Distribusi | Parameter | E[X] | Var(X) | Contoh Informatika |
|------------|-----------|------|--------|--------------------|
| Bernoulli | p | p | p(1−p) | Satu permintaan berhasil? |
| Binomial | n, p | np | np(1−p) | Berapa dari 100 pengguna melakukan konversi? |
| Poisson | λ | λ | λ | Berapa permintaan per detik? Berapa bug per hari? |
| Geometrik | p | 1/p | (1−p)/p² | Berapa kali *retry* sampai berhasil? |

#### Latihan Penentuan Distribusi

Untuk tiap kasus, tentukan distribusinya beserta parameternya:

| No | Kasus | Distribusi? |
|----|-------|-------------|
| 1 | Dari 50 *pull request*, berapa yang ditolak bila tingkat penolakan 12%? | |
| 2 | Berapa laporan bug masuk ke sistem tiket besok, bila rata-rata 6 per hari? | |
| 3 | Berapa kali harus me-*refresh* halaman sampai berhasil dimuat, bila 85% berhasil? | |
| 4 | Apakah sebuah berkas unggahan lolos pemindaian virus? | |
| 5 | Berapa pengguna dari 1.000 yang mengalami galat, bila tingkat galat 0,2%? | |

*Kunci dibahas di kelas. Perhatikan nomor 5 — dua jawaban dapat diterima, dan keduanya hampir sama hasilnya.*

---

### 7. Memeriksa Kecocokan Distribusi pada Data Nyata

```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv("bug_report_harian.csv")
jumlah = df["jumlah_bug"].values

mean_data = jumlah.mean()
var_data = jumlah.var(ddof=1)

print(f"Mean data    : {mean_data:.3f}")
print(f"Varians data : {var_data:.3f}")
print(f"Rasio var/mean: {var_data/mean_data:.3f}")

if 0.8 <= var_data / mean_data <= 1.25:
    print("→ Rasio mendekati 1: Poisson masuk akal.")
else:
    print("→ Rasio jauh dari 1: Poisson mungkin tidak cocok (overdispersion).")

# Membandingkan frekuensi teramati dengan yang diharapkan Poisson
lam = mean_data
nilai = np.arange(0, jumlah.max() + 1)
teramati = np.array([(jumlah == k).sum() for k in nilai])
diharapkan = stats.poisson.pmf(nilai, lam) * len(jumlah)

plt.figure(figsize=(10, 5))
lebar = 0.4
plt.bar(nilai - lebar/2, teramati, lebar, label="Teramati", color="steelblue")
plt.bar(nilai + lebar/2, diharapkan, lebar, label=f"Poisson(λ={lam:.2f})",
        color="#e67e22", alpha=0.85)
plt.xlabel("Jumlah bug per hari")
plt.ylabel("Jumlah hari")
plt.title("Kecocokan data laporan bug dengan distribusi Poisson")
plt.legend()
plt.tight_layout()
plt.show()
```

> Pengujian kecocokan secara formal memakai **uji chi-square kesesuaian** — materi Minggu 13. Untuk sekarang, perbandingan visual dan rasio varians/mean sudah memberi petunjuk yang berguna.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (Mandiri — 60 menit)

1. Membaca [Bab 6 buku ajar](../06-buku-ajar/bab-06-peubah-acak-distribusi-diskret.md).
2. Menyegarkan kembali kombinasi C(n,k) dari Minggu 4.
3. Mencatat tiga fenomena dari pengalaman sendiri yang berupa "jumlah kejadian per satuan waktu".

### Di Kelas (150 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–10' | Pembahasan Kuis 2 dan umpan balik proposal proyek |
| 10–30' | Kuliah: peubah acak, PMF, CDF |
| 30–60' | Kuliah + latihan: Bernoulli dan Binomial; syarat BINS |
| 60–70' | Istirahat |
| 70–100' | Kuliah + latihan: Poisson; kasus perencanaan kapasitas server |
| 100–120' | Kuliah: Geometrik dan sifat tanpa memori; diskusi *gambler's fallacy* |
| 120–145' | **Latihan kelas:** menentukan distribusi untuk 5 kasus; studio `scipy.stats` |
| 145–150' | Penutup, penjelasan Lab 06 |

### Setelah Kelas (Mandiri — 180 menit)

1. Mengerjakan [Lab 06](../04-labs/lab-06-distribusi-diskret-scipy.md).
2. Mengerjakan Latihan Soal Bab 6.
3. Mulai mengumpulkan data proyek.

---

## Penugasan

| Kode | Tugas | Bobot | Batas Waktu |
|------|-------|-------|-------------|
| T-06 | Laporan Lab 06 — Distribusi diskret dengan `scipy.stats` | 1,92% | Sebelum kelas Minggu 7 |

---

## Rangkuman

1. **Peubah acak** memetakan hasil percobaan ke bilangan, sehingga bisa dihitung rata-rata dan variansnya.
2. **PMF** memberi P(X = x); **CDF** memberi P(X ≤ x). Jumlah seluruh PMF selalu 1.
3. **Bernoulli** adalah batu bata dasar: satu percobaan, dua hasil.
4. **Binomial** menghitung jumlah keberhasilan dari n percobaan. Syaratnya **BINS**: Binary, Independent, Number fixed, Same probability.
5. **Poisson** menghitung kejadian per satuan waktu/ruang. Cirinya: **mean = varians**. Rasio varians/mean jauh dari 1 menandakan Poisson tidak cocok.
6. **Geometrik** menghitung percobaan sampai keberhasilan pertama, dan bersifat **tanpa memori** — kegagalan masa lalu tidak membuat keberhasilan berikutnya lebih dekat.
7. Merancang kapasitas sistem berdasarkan **rata-rata** berarti kewalahan hampir separuh waktu; kuantil ke-99 memberi angka yang layak.
8. Memilih distribusi dimulai dari **pertanyaan apa yang ingin dijawab**, bukan dari rumus mana yang diingat.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 3, 5. Pearson.
2. Ross, S. M. (2019). *A First Course in Probability* (10th ed.), Bab 4. Pearson.
3. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.), Bab 3. Wiley.
4. Dokumentasi SciPy — *Discrete distributions*. <https://docs.scipy.org/doc/scipy/reference/stats.html#discrete-distributions>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
