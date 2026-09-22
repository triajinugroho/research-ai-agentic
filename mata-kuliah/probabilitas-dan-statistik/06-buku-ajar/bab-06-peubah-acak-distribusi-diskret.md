# BAB 6: PEUBAH ACAK DAN DISTRIBUSI DISKRET

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `PS-Sub-CPMK081-1` | Menjelaskan peubah acak, PMF, dan CDF | C2 |
| `PS-Sub-CPMK081-1` | Menerapkan distribusi Bernoulli, Binomial, Poisson, dan Geometrik | C3 |
| `PS-Sub-CPMK081-1` | Menentukan distribusi yang tepat untuk sebuah fenomena beserta asumsinya | C4 |

---

## 6.1 Peubah Acak

### 6.1.1 Definisi

> **Peubah acak** adalah fungsi yang memetakan setiap hasil dalam ruang sampel ke sebuah bilangan real.

```
   Ruang sampel S                     Bilangan real
   ┌──────────────┐                   ─────────────
   │ LLL  LLG     │      X = jumlah         0
   │ LGL  LGG     │  ───  modul gagal ───→  1
   │ GLL  GLG     │                         2
   │ GGL  GGG     │                         3
   └──────────────┘
```

Peubah acak memungkinkan kita berpindah dari "hasil percobaan" — yang bisa berupa apa saja — ke **angka yang dapat dihitung rata-rata dan variansnya**.

| Jenis | Ciri | Contoh Informatika |
|-------|------|--------------------|
| **Diskret** | Nilai terhitung (bilangan bulat) | Jumlah bug, jumlah permintaan, jumlah percobaan login |
| **Kontinu** | Nilai dalam selang bilangan real | Waktu respons, ukuran berkas, suhu prosesor |

### 6.1.2 PMF dan CDF

| Fungsi | Lambang | Definisi | Sifat |
|--------|---------|----------|-------|
| **PMF** (*probability mass function*) | p(x) = P(X = x) | Probabilitas X bernilai tepat x | 0 ≤ p(x) ≤ 1 dan Σ p(x) = 1 |
| **CDF** (*cumulative distribution function*) | F(x) = P(X ≤ x) | Probabilitas X tidak melebihi x | Tidak turun, dari 0 ke 1 |

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

n, p = 3, 0.20          # 3 modul, tiap modul gagal 20%
x = np.arange(0, n + 1)
pmf = stats.binom.pmf(x, n, p)
cdf = stats.binom.cdf(x, n, p)

print(f"{'x':>3} {'P(X=x)':>10} {'P(X≤x)':>10}")
for xi, pm, cd in zip(x, pmf, cdf):
    print(f"{xi:>3} {pm:>10.6f} {cd:>10.6f}")
print(f"\nΣ PMF = {pmf.sum():.10f}  (harus 1)")

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].bar(x, pmf, color="steelblue", edgecolor="white")
axes[0].set_title("PMF: P(X = x)"); axes[0].set_xlabel("Jumlah modul gagal")
axes[1].step(x, cdf, where="post", linewidth=2, color="#c0392b")
axes[1].set_title("CDF: P(X ≤ x)"); axes[1].set_ylim(0, 1.05)
plt.tight_layout(); plt.show()
```

---

## 6.2 Distribusi Bernoulli

**Satu percobaan dengan dua hasil:** berhasil (1) dengan probabilitas p, gagal (0) dengan probabilitas 1−p.

$$P(X = x) = p^x (1-p)^{1-x}, \quad x \in \{0, 1\}$$

$$E[X] = p \qquad \text{Var}(X) = p(1-p)$$

**Contoh Informatika:** satu permintaan HTTP berhasil atau gagal; satu pengguna melakukan konversi atau tidak; satu berkas lolos validasi atau tidak.

> Bernoulli adalah **batu bata dasar**. Binomial dan Geometrik dibangun dari rangkaian percobaan Bernoulli.

**Catatan menarik:** Var(X) = p(1−p) mencapai maksimum pada p = 0,5 (nilainya 0,25) dan mendekati nol ketika p mendekati 0 atau 1. Artinya **ketidakpastian terbesar terjadi ketika peluangnya seimbang** — sesuai intuisi.

---

## 6.3 Distribusi Binomial

### 6.3.1 Syarat BINS

Sebelum memakai Binomial, **periksa empat syarat**:

| Huruf | Syarat | Pertanyaan pemeriksaan |
|-------|--------|------------------------|
| **B** | *Binary* | Apakah tiap percobaan punya tepat dua hasil? |
| **I** | *Independent* | Apakah percobaan saling bebas? |
| **N** | *Number fixed* | Apakah jumlah percobaan n ditetapkan di awal? |
| **S** | *Same probability* | Apakah p sama untuk tiap percobaan? |

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

$$E[X] = np \qquad \text{Var}(X) = np(1-p)$$

> **Syarat I adalah yang paling sering dilanggar dalam praktik Informatika.** Bila 20 server berada di satu rak dan rak itu kehilangan daya, kegagalan mereka **tidak bebas**. Binomial akan memberi jawaban yang terlalu optimistis.

### 6.3.2 Contoh Terapan

> Sebuah *load balancer* meneruskan permintaan ke 20 server. Tiap server mengembalikan galat dengan probabilitas 5%, dan kegagalan antar server saling bebas.

```python
from scipy import stats

n, p = 20, 0.05
X = stats.binom(n, p)

print(f"E[X]   = {X.mean():.4f}  (= np = {n*p})")
print(f"Var(X) = {X.var():.4f}  (= np(1−p) = {n*p*(1-p)})")
print(f"SD(X)  = {X.std():.4f}\n")

print(f"P(X = 0)  = {X.pmf(0):.6f}   (tidak ada yang galat)")
print(f"P(X = 2)  = {X.pmf(2):.6f}")
print(f"P(X ≤ 2)  = {X.cdf(2):.6f}")
print(f"P(X ≥ 3)  = {X.sf(2):.6f}    ← perhatikan sf(2), bukan sf(3)")
print(f"P(X ≥ 5)  = {X.sf(4):.8f}    (kejadian sangat jarang)")
```

> **Jebakan `scipy` yang sering menjatuhkan:** `sf(k)` menghitung P(X > k), bukan P(X ≥ k). Untuk P(X ≥ 3) pada distribusi diskret, gunakan `sf(2)`.

### 6.3.3 Bentuk Distribusi

| p | Bentuk |
|---|--------|
| p < 0,5 | Menceng kanan |
| p = 0,5 | Simetris |
| p > 0,5 | Menceng kiri |

Seiring n bertambah, bentuknya makin mendekati Normal — konsekuensi Teorema Limit Pusat yang dibahas di Bab 8.

---

## 6.4 Distribusi Poisson

### 6.4.1 Kapan Dipakai

Memodelkan **jumlah kejadian dalam satuan waktu, ruang, atau volume tertentu**, dengan tiga syarat:

1. Kejadian terjadi secara **bebas** satu sama lain.
2. Laju rata-rata **λ konstan**.
3. Dua kejadian tidak mungkin terjadi pada saat yang persis sama.

$$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \ldots$$

$$E[X] = \lambda \qquad \text{Var}(X) = \lambda$$

> **Ciri khas Poisson yang harus diingat: mean dan varians SAMA.**
>
> Bila pada data nyata varians jauh lebih besar dari mean (*overdispersion*), Poisson **bukan** model yang tepat. Biasanya penyebabnya: laju λ tidak benar-benar konstan (ada jam sibuk dan jam sepi), atau kejadian tidak saling bebas (satu bug memicu bug lain).

### 6.4.2 Perencanaan Kapasitas

> Sebuah server menerima rata-rata **8 permintaan per detik**.

```python
from scipy import stats

lam = 8
X = stats.poisson(lam)

print(f"E[X] = Var(X) = {lam}  ← ciri khas Poisson\n")
print(f"P(X = 5)  = {X.pmf(5):.6f}")
print(f"P(X ≤ 8)  = {X.cdf(8):.6f}   ← kapasitas rata-rata cukup?")
print(f"P(X > 15) = {X.sf(15):.8f}\n")

print("PERENCANAAN KAPASITAS:")
print(f"{'Tingkat layanan':>17}  {'Kapasitas':>10}  {'Rasio thd rata-rata':>20}")
for level in [0.50, 0.90, 0.95, 0.99, 0.999]:
    kap = X.ppf(level)
    print(f"{level*100:>16.1f}%  {kap:>10.0f}  {kap/lam:>19.2f}×")
```

> **Wawasan rekayasa yang penting.** Merancang server untuk kapasitas **rata-rata** (8/detik) berarti sistem kewalahan hampir separuh waktu — karena separuh waktu beban berada di atas rata-rata.
>
> Untuk 99,9% ketersediaan diperlukan kapasitas sekitar 2,4× rata-rata. Inilah alasan matematis di balik praktik *over-provisioning*: ia **bukan pemborosan**, melainkan konsekuensi langsung dari variabilitas.

### 6.4.3 Poisson sebagai Hampiran Binomial

Ketika n besar dan p kecil, Binomial(n, p) ≈ Poisson(λ = np).

```python
import numpy as np
from scipy import stats

print(f"{'(n, p)':>18}  {'Selisih maks PMF':>18}")
for n, p in [(100, 0.5), (100, 0.05), (1000, 0.005), (10000, 0.0008)]:
    k = np.arange(0, 40)
    selisih = np.abs(stats.binom.pmf(k, n, p) - stats.poisson.pmf(k, n*p)).max()
    print(f"{f'({n}, {p})':>18}  {selisih:>18.2e}")
print("\n→ Hampiran makin baik ketika n besar DAN p kecil.")
```

Berguna ketika n sangat besar sehingga menghitung C(n,k) menjadi mahal — misalnya "berapa probabilitas tepat 3 dari 10 juta permintaan mengalami *race condition*".

---

## 6.5 Distribusi Geometrik

### 6.5.1 Rumus

Memodelkan **jumlah percobaan sampai keberhasilan pertama**.

$$P(X = k) = (1-p)^{k-1} p, \quad k = 1, 2, 3, \ldots$$

$$E[X] = \frac{1}{p} \qquad \text{Var}(X) = \frac{1-p}{p^2}$$

### 6.5.2 Contoh dan Sifat Tanpa Memori

```python
from scipy import stats

p = 0.3
X = stats.geom(p)

print(f"E[X] = {X.mean():.4f}  (= 1/p = {1/p:.4f})")
print(f"P(berhasil percobaan ke-1) = {X.pmf(1):.4f}")
print(f"P(berhasil percobaan ke-4) = {X.pmf(4):.4f}")
print(f"P(butuh > 5 percobaan)     = {X.sf(5):.6f}\n")

print("SIFAT TANPA MEMORI:")
print(f"  P(X > 5)         = {X.sf(5):.8f}")
print(f"  P(X > 8 | X > 3) = {X.sf(8)/X.sf(3):.8f}")
print("  → IDENTIK.")
```

> **Sifat tanpa memori (*memoryless*)** berarti: sudah gagal 3 kali **tidak** membuat percobaan ke-4 lebih mungkin berhasil. Koin tidak "ingat" berapa kali ia sudah jatuh di sisi yang sama.
>
> Keyakinan sebaliknya disebut ***gambler's fallacy***, dan muncul dalam perancangan sistem ketika seseorang berpikir "sudah gagal banyak, pasti sebentar lagi berhasil" — lalu merancang strategi *retry* dengan asumsi keliru itu.
>
> Strategi *retry* yang benar justru berangkat dari kesadaran bahwa peluangnya tidak berubah: karena itu dipakai *exponential backoff* untuk mengurangi beban, bukan untuk "menunggu giliran keberuntungan".

---

## 6.6 Memilih Distribusi yang Tepat

```
  Pertanyaannya apa?
  │
  ├── "Berhasil atau gagal?" (satu kali)          → BERNOULLI
  │
  ├── "Berapa kali berhasil dari n percobaan?"    → BINOMIAL
  │     periksa: BINS
  │
  ├── "Berapa kejadian per satuan waktu/ruang?"   → POISSON
  │     periksa: λ konstan, kejadian bebas, mean ≈ varians
  │
  └── "Percobaan ke berapa baru berhasil?"        → GEOMETRIK
        periksa: p sama, saling bebas
```

| Distribusi | Parameter | E[X] | Var(X) | Contoh |
|------------|-----------|------|--------|--------|
| Bernoulli | p | p | p(1−p) | Satu permintaan berhasil? |
| Binomial | n, p | np | np(1−p) | Berapa dari 100 pengguna konversi? |
| Poisson | λ | λ | λ | Berapa permintaan per detik? |
| Geometrik | p | 1/p | (1−p)/p² | Berapa *retry* sampai berhasil? |

---

## 6.7 Memeriksa Kecocokan pada Data Nyata

```python
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("bug_report_harian.csv")
jumlah = df["jumlah_bug"].values

mean_d, var_d = jumlah.mean(), jumlah.var(ddof=1)
rasio = var_d / mean_d

print(f"Mean            : {mean_d:.4f}")
print(f"Varians         : {var_d:.4f}")
print(f"Rasio var/mean  : {rasio:.4f}\n")

if 0.8 <= rasio <= 1.25:
    print("→ Rasio mendekati 1: Poisson masuk akal.")
elif rasio > 1.25:
    print("→ OVERDISPERSION. Poisson mungkin tidak cocok.")
    print("  Periksa: apakah λ konstan? Apakah kejadian bebas?")
else:
    print("→ UNDERDISPERSION. Data lebih teratur dari Poisson.")
```

Uji formalnya adalah **chi-square kesesuaian** — Bab 12.

---

## AI Corner — Tingkat Menengah

### Yang AI Lakukan dengan Baik

Menghitung probabilitas dari distribusi yang sudah ditentukan. Bila Anda berkata "hitung P(X=3) untuk Binomial(20, 0.05)", hampir semua model akan benar.

### Yang AI Lakukan dengan Buruk

**Memilih distribusi yang tepat** — karena itu memerlukan pemahaman konteks data Anda, dan terutama **pemeriksaan asumsi**.

### Percobaan: Uji Pemeriksaan Asumsi

Ajukan soal ini:

> *"Sebuah rak berisi 20 server. Tiap server gagal dengan probabilitas 5%. Berapa probabilitas tepat 2 server gagal?"*

Hampir semua AI akan menjawab dengan Binomial: 0,1887.

Sekarang tanyakan:

> *"Apakah asumsi Binomial terpenuhi di sini, mengingat kedua puluh server berada di satu rak dengan satu sumber daya listrik?"*

Model yang baik akan menyadari bahwa **asumsi kebebasan dilanggar** — kegagalan listrik rak akan menjatuhkan semuanya bersamaan. Tetapi ia **tidak menyampaikannya sampai ditanya**.

> **Pola yang berulang di seluruh buku ini:** AI menjawab pertanyaan yang Anda ajukan. Pemeriksaan asumsi hampir tidak pernah muncul secara spontan — karena secara teknis, pertanyaan Anda sudah terjawab.
>
> Yang mengetahui bahwa asumsi perlu diperiksa, hanya Anda.

### Daftar Periksa Sebelum Menerima Jawaban AI

Ketika AI memberi jawaban probabilitas, tanyakan pada diri sendiri:

- [ ] Distribusi apa yang ia pakai, dan mengapa?
- [ ] Apakah syarat distribusi itu terpenuhi pada data saya?
- [ ] Apakah ia memakai `sf(k)` atau `1 - cdf(k)` dengan benar untuk kasus diskret?
- [ ] Apakah hasilnya masuk akal secara besaran? (Probabilitas 1,3 berarti salah.)
- [ ] Apakah ada asumsi tersembunyi yang tidak ia sebutkan?

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan perbedaan PMF dan CDF. Mengapa Σ PMF harus sama dengan 1?

2. Sebutkan empat syarat BINS dan beri satu contoh pelanggaran untuk masing-masing.

3. Untuk Binomial(n=15, p=0,2), hitung: (a) E[X], (b) Var(X), (c) P(X=3), (d) P(X≤2), (e) P(X≥4).

4. Sebuah server menerima rata-rata 4 permintaan per detik (Poisson). Hitung: (a) P(X=0), (b) P(X=4), (c) P(X>8).

5. Untuk Geometrik dengan p=0,25, hitung: (a) E[X], (b) P(X=3), (c) P(X>6).

### Tingkat Menengah

6. Untuk setiap kasus, tentukan distribusi yang tepat, parameternya, dan **asumsi yang harus dipenuhi**:
   (a) Dari 60 *pull request*, berapa yang ditolak bila tingkat penolakan 15%?
   (b) Berapa laporan gangguan masuk besok, bila rata-rata 9 per hari?
   (c) Berapa kali *refresh* sampai halaman termuat, bila 80% berhasil?
   (d) Apakah sebuah unggahan lolos pemindaian virus?
   (e) Berapa dari 5.000 pengguna mengalami galat, bila tingkat galat 0,06%?

7. Sebuah API menerima rata-rata 25 permintaan per detik.
   (a) Hitung kapasitas minimum untuk tingkat layanan 95%, 99%, dan 99,9%.
   (b) Berapa rasio masing-masing terhadap rata-rata?
   (c) Bila biaya server sebanding dengan kapasitas, berapa kali lipat biaya untuk naik dari 95% ke 99,9%?
   (d) Berikan rekomendasi Anda kepada tim dengan mempertimbangkan biaya dan pengalaman pengguna.

8. Data jumlah insiden harian selama 200 hari memiliki mean 3,2 dan varians 9,8.
   (a) Hitung rasio varians/mean.
   (b) Apakah Poisson model yang tepat? Jelaskan.
   (c) Sebutkan dua kemungkinan penyebab hasil itu.
   (d) Apa yang akan Anda periksa selanjutnya?

9. Jelaskan sifat tanpa memori distribusi Geometrik.
   (a) Buktikan secara aljabar bahwa P(X > m+n | X > m) = P(X > n).
   (b) Jelaskan mengapa *gambler's fallacy* adalah pelanggaran terhadap sifat ini.
   (c) Bila *retry* bersifat tanpa memori, mengapa *exponential backoff* tetap berguna?

### Tingkat Mahir

10. Bandingkan skenario kegagalan **bebas** dan **berkorelasi** pada 20 server.
    (a) Skenario A: tiap server gagal mandiri dengan p=0,05.
    (b) Skenario B: dengan probabilitas 0,02 terjadi gangguan rak yang menjatuhkan **semua** server; selain itu tiap server gagal mandiri dengan p=0,03.
    (c) Simulasikan keduanya dan bandingkan sebaran jumlah server gagal.
    (d) Hitung P(X ≥ 10) untuk keduanya. Berapa kali lipat perbedaannya?
    (e) Apa pelajarannya bagi arsitektur sistem yang mengandalkan replika?

11. Turunkan E[X] dan Var(X) untuk distribusi Binomial dari sifat linearitas ekspektasi.
    (Petunjuk: X = Σ Bᵢ dengan Bᵢ ~ Bernoulli(p) saling bebas.)

12. Sebuah tim mengukur jumlah *deployment* gagal per minggu selama 2 tahun (104 minggu). Datanya memiliki mean 2,1 dan varians 2,3.
    (a) Apakah Poisson masuk akal?
    (b) Berdasarkan model Poisson, berapa probabilitas sebuah minggu mengalami 0 kegagalan?
    (c) Dari 104 minggu, berapa minggu yang diharapkan mengalami 0 kegagalan?
    (d) Rancang prosedur untuk menguji kecocokan model ini secara formal (uraikan langkahnya; uji formalnya dibahas di Bab 12).
    (e) Bila tim ingin menurunkan rata-rata kegagalan menjadi 1 per minggu, berapa probabilitas minggu tanpa kegagalan setelah perbaikan?

---

## Rangkuman

1. **Peubah acak** memetakan hasil percobaan ke bilangan, sehingga dapat dihitung rata-rata dan variansnya.
2. **PMF** memberi P(X = x); **CDF** memberi P(X ≤ x). Jumlah seluruh PMF selalu 1.
3. **Bernoulli** adalah batu bata dasar. Variansnya maksimum pada p = 0,5.
4. **Binomial** menghitung keberhasilan dari n percobaan. Periksa **BINS** — terutama syarat kebebasan.
5. **Poisson** menghitung kejadian per satuan waktu/ruang. Cirinya **mean = varians**; rasio jauh dari 1 menandakan model tidak cocok.
6. **Merancang kapasitas berdasarkan rata-rata berarti kewalahan separuh waktu.** Kuantil ke-99 memberi angka yang layak.
7. **Geometrik** menghitung percobaan sampai berhasil, dan bersifat **tanpa memori**.
8. *Gambler's fallacy* adalah pelanggaran terhadap sifat tanpa memori.
9. Memilih distribusi dimulai dari **pertanyaan apa yang ingin dijawab**, bukan dari rumus mana yang diingat.
10. **Asumsi distribusi wajib diperiksa** — AI tidak akan memeriksanya untuk Anda.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 3, 5. Pearson.
2. Ross, S. M. (2019). *A First Course in Probability* (10th ed.), Bab 4. Pearson.
3. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.), Bab 3. Wiley.
4. Gallager, R. G. (2013). *Stochastic Processes: Theory for Applications*, Bab 2. Cambridge University Press.
5. Dokumentasi SciPy — *Discrete distributions*. <https://docs.scipy.org/doc/scipy/reference/stats.html>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
