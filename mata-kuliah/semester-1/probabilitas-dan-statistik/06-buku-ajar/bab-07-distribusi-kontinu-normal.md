# BAB 7: DISTRIBUSI KONTINU DAN DISTRIBUSI NORMAL

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `PS-Sub-CPMK081-1` | Menjelaskan PDF dan mengapa P(X = x) = 0 pada peubah kontinu | C2 |
| `PS-Sub-CPMK081-1` | Menerapkan distribusi Uniform, Eksponensial, dan Normal | C3 |
| `PS-Sub-CPMK081-1` | Menghitung probabilitas Normal dengan skor-z dan memeriksa kenormalan data | C3–C4 |

---

## 7.1 Dari Diskret ke Kontinu

### 7.1.1 Mengapa P(X = x) = 0

Pada peubah acak kontinu, probabilitas satu titik tepat adalah **nol**.

> Berapa probabilitas waktu respons **tepat** 100,000000… ms? Nol — karena ada tak hingga banyak nilai yang mungkin antara 99 dan 101 ms, dan satu titik di antaranya tidak punya "lebar".

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
      TINGGI = P(X=x)                 LUAS = P(a≤X≤b)
```

| Aspek | PMF (diskret) | PDF (kontinu) |
|-------|---------------|---------------|
| Notasi | p(x) = P(X = x) | f(x) |
| Nilai | 0 ≤ p(x) ≤ 1 | f(x) ≥ 0, **boleh lebih dari 1** |
| Total | Σ p(x) = 1 | ∫ f(x) dx = 1 |
| P(X = a) | p(a) | **0** |
| Cara membaca | Tinggi batang | **Luas di bawah kurva** |

> **PDF boleh bernilai lebih dari 1.** Yang harus sama dengan 1 adalah **luasnya**, bukan tingginya. Distribusi Normal dengan σ = 0,1 memiliki puncak PDF sekitar 3,99 — dan itu benar.
>
> **Konsekuensi praktis:** karena P(X = a) = 0, maka P(X ≤ a) = P(X < a). Pada kasus kontinu, tanda "sama dengan" tidak berpengaruh — berbeda dari kasus diskret.

---

## 7.2 Distribusi Uniform Kontinu

Semua nilai dalam selang [a, b] sama mungkinnya.

$$f(x) = \frac{1}{b-a}, \quad a \le x \le b \qquad E[X] = \frac{a+b}{2} \qquad \text{Var}(X) = \frac{(b-a)^2}{12}$$

**Contoh Informatika:** *jitter* acak pada strategi *retry*; nilai yang dihasilkan `random.random()`; posisi acak dalam *hash table* yang ideal.

```python
from scipy import stats

a, b = 0, 500                              # jitter 0–500 ms
U = stats.uniform(loc=a, scale=b - a)      # PERHATIKAN: scale = lebar selang

print(f"E[X]             = {U.mean():.2f} ms")
print(f"SD(X)            = {U.std():.2f} ms")
print(f"P(X ≤ 100)       = {U.cdf(100):.4f}")
print(f"P(200 ≤ X ≤ 300) = {U.cdf(300) - U.cdf(200):.4f}")
```

---

## 7.3 Distribusi Eksponensial

### 7.3.1 Hubungan dengan Poisson

Memodelkan **waktu tunggu sampai kejadian berikutnya**, ketika kejadian mengikuti proses Poisson dengan laju λ.

$$f(x) = \lambda e^{-\lambda x}, \quad x \ge 0 \qquad E[X] = \frac{1}{\lambda} \qquad \text{Var}(X) = \frac{1}{\lambda^2}$$

```
   POISSON                        EKSPONENSIAL
   "berapa kejadian               "berapa lama sampai
    per satuan waktu?"             kejadian berikutnya?"

   diskret, λ per detik           kontinu, rata-rata 1/λ detik

           ← dua sisi mata uang yang sama →
```

### 7.3.2 Contoh dan Jebakan Parameter

```python
from scipy import stats

lam = 8                            # 8 permintaan per detik
E = stats.expon(scale=1/lam)       # PERHATIKAN: scale = 1/λ, BUKAN λ

# Verifikasi bahwa parameter sudah benar
print(f"Verifikasi: E[X] = {E.mean():.6f} detik (harus = 1/λ = {1/lam:.6f})\n")

print(f"Rata-rata jeda    : {E.mean()*1000:.2f} ms")
print(f"P(jeda < 50 ms)   : {E.cdf(0.050):.4f}")
print(f"P(jeda > 500 ms)  : {E.sf(0.500):.6f}")
print(f"Persentil ke-95   : {E.ppf(0.95)*1000:.2f} ms\n")

print("SIFAT TANPA MEMORI (versi kontinu):")
print(f"  P(X > 0.2)           = {E.sf(0.2):.8f}")
print(f"  P(X > 0.3 | X > 0.1) = {E.sf(0.3)/E.sf(0.1):.8f}")
print("  → IDENTIK. Sudah menunggu 0,1 detik tidak mengubah apa pun.")
```

> **Jebakan `scipy` yang sangat sering terjadi.** Parameter `scale` pada `stats.expon` adalah **1/λ**, bukan λ.
>
> Kesalahan ini tidak menghasilkan galat — hanya angka yang keliru secara diam-diam. Biasakan **memverifikasi dengan `.mean()`** setiap kali membuat objek distribusi.

---

## 7.4 Distribusi Normal

### 7.4.1 Rumus dan Bentuk

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

Dua parameter: **μ menentukan letak** puncak, **σ menentukan lebar** kurva.

```
              μ = pusat
                 │
           ╭─────┼─────╮
         ╱       │       ╲
       ╱         │         ╲
     ╱           │           ╲
   ─────────────────────────────
   μ−3σ  μ−2σ  μ−σ  μ  μ+σ  μ+2σ  μ+3σ
              ←── 68,27% ──→
         ←─────── 95,45% ───────→
    ←──────────── 99,73% ────────────→
```

### 7.4.2 Aturan Empiris 68–95–99,7

| Selang | Proporsi Data |
|--------|---------------|
| μ ± 1σ | ≈ 68,27% |
| μ ± 2σ | ≈ 95,45% |
| μ ± 3σ | ≈ 99,73% |

```python
from scipy import stats

Z = stats.norm(0, 1)
for k in [1, 2, 3, 6]:
    p = Z.cdf(k) - Z.cdf(-k)
    print(f"P(μ − {k}σ ≤ X ≤ μ + {k}σ) = {p:.8f}  ({p*100:.4f}%)")
```

> **Asal istilah "Six Sigma".** Proses yang cacatnya berada di luar μ ± 6σ menghasilkan sekitar 3,4 cacat per satu juta kesempatan (setelah memperhitungkan pergeseran proses 1,5σ yang lazim diasumsikan). Istilah manajemen mutu itu berakar langsung pada tabel di atas.

### 7.4.3 Skor-z: Membandingkan yang Tidak Sebanding

$$z = \frac{x - \mu}{\sigma}$$

Skor-z menyatakan **berapa simpangan baku sebuah nilai berjarak dari rata-rata**, dan mengubah distribusi Normal apa pun menjadi Normal baku N(0, 1).

```python
from scipy import stats

mu, sigma = 72, 11
X = stats.norm(mu, sigma)

print(f"NILAI UAS ~ Normal(μ={mu}, σ={sigma})\n")
print(f"{'Nilai':>6} {'z':>8} {'Persentil':>11} {'P(X > nilai)':>14}")
for nilai in [50, 60, 72, 85, 95]:
    z = (nilai - mu) / sigma
    print(f"{nilai:>6} {z:>8.3f} {X.cdf(nilai)*100:>10.1f}% {X.sf(nilai):>14.4f}")

print(f"\nAmbang batas:")
print(f"  10% teratas  : nilai ≥ {X.ppf(0.90):.2f}")
print(f"  25% terbawah : nilai ≤ {X.ppf(0.25):.2f}")
```

**Kegunaan utama skor-z: membandingkan nilai dari dua sebaran berbeda.**

```python
mahasiswa = [
    {"nama": "Ahmad", "mk": "Statistika", "nilai": 85, "mu": 75, "sigma": 8},
    {"nama": "Budi",  "mk": "Kalkulus",   "nilai": 78, "mu": 65, "sigma": 6},
]

print(f"{'Nama':<8} {'Nilai':>6} {'μ':>5} {'σ':>5} {'z':>8} {'Persentil':>10}")
for m in mahasiswa:
    z = (m["nilai"] - m["mu"]) / m["sigma"]
    print(f"{m['nama']:<8} {m['nilai']:>6} {m['mu']:>5} {m['sigma']:>5} "
          f"{z:>8.3f} {stats.norm.cdf(z)*100:>9.1f}%")
print("\n→ Nilai mentah 85 dan 78 tidak bisa dibandingkan langsung.")
print("  Skor-z membuatnya bisa.")
```

### 7.4.4 Mengapa Normal Muncul Di Mana-Mana — dan Kapan Tidak

Bukan kebetulan. **Teorema Limit Pusat** (Bab 8) menjelaskan bahwa jumlah atau rata-rata dari banyak pengaruh acak kecil yang saling bebas akan mendekati Normal — berapa pun bentuk sebaran aslinya.

> **Tetapi hati-hati: tidak semua hal berdistribusi Normal.**
>
> Waktu respons, ukuran berkas, penghasilan, jumlah pengikut — semuanya **menceng kanan**, bukan Normal. Mengasumsikan kenormalan tanpa memeriksanya adalah kesalahan yang sering berakibat fatal pada kesimpulan.

---

## 7.5 Memeriksa Kenormalan

### 7.5.1 Tiga Pendekatan

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def periksa_kenormalan(data, nama):
    """Pemeriksaan kenormalan: visual, statistik bentuk, dan uji formal."""
    data = np.asarray(data)
    data = data[~np.isnan(data)]
    n = len(data)

    fig, axes = plt.subplots(1, 3, figsize=(16, 4.2))

    axes[0].hist(data, bins=30, density=True, color="steelblue",
                 edgecolor="white", alpha=0.85)
    x = np.linspace(data.min(), data.max(), 300)
    axes[0].plot(x, stats.norm.pdf(x, data.mean(), data.std(ddof=1)),
                 color="#c0392b", linewidth=2, label="Normal teoretis")
    axes[0].set_title(f"{nama}\nHistogram vs Normal"); axes[0].legend()

    stats.probplot(data, dist="norm", plot=axes[1])
    axes[1].set_title("Q-Q Plot")

    axes[2].boxplot(data)
    axes[2].set_title("Boxplot")
    plt.tight_layout(); plt.show()

    sk, ku = stats.skew(data), stats.kurtosis(data)
    print(f"=== {nama} (n = {n}) ===")
    print(f"  Kemencengan : {sk:>8.4f}   (Normal ≈ 0)")
    print(f"  Kurtosis    : {ku:>8.4f}   (Normal ≈ 0)")

    sub = data if n <= 5000 else np.random.default_rng(42).choice(data, 5000, replace=False)
    w, p_sw = stats.shapiro(sub)
    print(f"  Shapiro-Wilk: W = {w:.4f}, p = {p_sw:.8f}")

    if abs(sk) < 0.5 and abs(ku) < 1:
        print("  → Bentuk mendekati Normal secara praktis.")
    else:
        print("  → Menyimpang. Telaah Q-Q plot untuk menilai seberapa jauh.")
```

### 7.5.2 Cara Membaca Q-Q Plot

```
   NORMAL                 EKOR BERAT            MENCENG KANAN
    ·                       ·                       ··
   ··                      ·                      ··
  ··                     ··                     ···
 ··                   ···                    ····
··                 ···                    ···
titik di garis     melengkung S          melengkung ke atas
```

### 7.5.3 Mengapa Uji Formal Menyesatkan pada Sampel Besar

```python
from scipy import stats

print("Data hampir Normal (kemencengan sangat kecil):")
print(f"{'n':>8}  {'Shapiro p':>14}  Kesimpulan uji")
for n in [30, 100, 500, 2000, 5000]:
    s = stats.skewnorm.rvs(a=0.35, size=n, random_state=42)
    _, p = stats.shapiro(s)
    print(f"{n:>8}  {p:>14.8f}  "
          f"{'tidak menolak' if p > 0.05 else 'MENOLAK kenormalan'}")
```

> **Peringatan penting.** Pada sampel besar, uji kenormalan formal hampir **selalu** menolak — karena penyimpangan sekecil apa pun menjadi "signifikan". Pada sampel kecil, uji itu lemah dan jarang menolak apa pun.
>
> Karena itu **pemeriksaan visual (Q-Q plot) sering lebih informatif** daripada nilai p.
>
> Pertanyaan yang tepat bukan *"apakah data ini persis Normal?"* (jawabannya hampir selalu tidak) melainkan **"apakah penyimpangannya cukup kecil sehingga metode yang mengandaikan kenormalan masih layak dipakai?"**
>
> Pertanyaan ini akan kembali pada Bab 10 ketika membahas asumsi uji-t.

### 7.5.4 Transformasi untuk Data Menceng

```python
import numpy as np
from scipy import stats

waktu = np.array([...])          # data waktu respons, menceng kanan
waktu = waktu[waktu > 0]

for nama, d in [("Asli", waktu), ("log(x)", np.log(waktu)),
                ("√x", np.sqrt(waktu))]:
    print(f"{nama:>8}: kemencengan = {stats.skew(d):>8.4f}")
```

> Transformasi log sering efektif untuk data menceng kanan. **Tetapi setelah transformasi, kesimpulan berlaku pada skala yang ditransformasi.** Menafsirkannya kembali ke skala asli memerlukan kehati-hatian, karena mean dari log **bukan** log dari mean.

---

## AI Corner — Tingkat Menengah

### Kesalahan Parameter: Wilayah Rawan AI

Pustaka statistik memiliki konvensi parameter yang tidak seragam, dan AI sering keliru di sini:

| Distribusi | `scipy` mengharapkan | Kekeliruan yang sering terjadi |
|------------|----------------------|--------------------------------|
| `norm(loc, scale)` | scale = **σ** | Memberikan varians σ² |
| `expon(scale)` | scale = **1/λ** | Memberikan λ |
| `uniform(loc, scale)` | scale = **b − a** | Memberikan b |
| `gamma(a, scale)` | scale = **1/rate** | Memberikan rate |

**Cara memeriksa yang selalu berhasil:**

```python
X = stats.expon(scale=1/8)
print(X.mean())     # harus = 1/8 = 0.125
```

Bila `.mean()` tidak sesuai harapan teoretis Anda, parameternya salah.

### Percobaan

Mintalah AI menghitung: *"Waktu antar permintaan mengikuti Eksponensial dengan laju 8 permintaan per detik. Berapa P(waktu tunggu > 0,5 detik)?"*

Jawaban benar: e^(−8×0,5) = e^(−4) = 0,0183.

Bila AI memakai `stats.expon(scale=8)` alih-alih `scale=1/8`, ia akan menjawab 0,9394 — **lima puluh kali lipat lebih besar**, tanpa galat apa pun.

> **Pelajaran:** kesalahan parameter tidak menghasilkan pesan galat. Satu-satunya pertahanan adalah **memeriksa apakah hasilnya masuk akal** — dan itu menuntut Anda tahu berapa jawaban yang wajar.

### Daftar Periksa

- [ ] Apakah parameter distribusi sudah benar? Verifikasi dengan `.mean()`.
- [ ] Apakah hasilnya berada antara 0 dan 1?
- [ ] Apakah besarannya masuk akal? (P(waktu tunggu > 0,5 detik) mendekati 1 untuk laju 8/detik jelas keliru.)
- [ ] Apakah AI memeriksa asumsi kenormalan, atau langsung mengandaikannya?

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan mengapa P(X = x) = 0 pada peubah acak kontinu, dan apa konsekuensinya bagi penulisan P(X ≤ a) dan P(X < a).

2. Mengapa PDF boleh bernilai lebih dari 1, sedangkan PMF tidak?

3. Untuk Normal(μ=100, σ=15), hitung dengan tabel: (a) P(X < 120), (b) P(X > 85), (c) P(90 < X < 110), (d) nilai x dengan P(X < x) = 0,90.

4. Waktu antar kedatangan permintaan mengikuti Eksponensial dengan λ = 5 per detik. Hitung: (a) rata-rata jeda, (b) P(jeda < 0,1 detik), (c) P(jeda > 1 detik).

5. Nilai ujian berdistribusi Normal(μ=68, σ=12). Hitung skor-z untuk nilai 80 dan tafsirkan artinya.

### Tingkat Menengah

6. Waktu kompilasi proyek ~ Normal(μ = 45 detik, σ = 8 detik). Hitung **secara manual dengan tabel**, lalu verifikasi dengan Python:
   (a) P(X < 50), (b) P(X > 60), (c) P(38 < X < 52),
   (d) waktu yang hanya dilampaui 5% kompilasi terlambat,
   (e) skor-z untuk kompilasi 70 detik — apakah wajar?

7. Dua mahasiswa dari mata kuliah berbeda:

   | Mahasiswa | Nilai | μ kelas | σ kelas |
   |-----------|-------|---------|---------|
   | A | 82 | 70 | 10 |
   | B | 75 | 60 | 7 |

   (a) Hitung skor-z masing-masing.
   (b) Siapa yang berprestasi relatif lebih baik?
   (c) Berapa persentil masing-masing?
   (d) Jelaskan mengapa nilai mentah tidak dapat dibandingkan langsung.

8. Sebuah data waktu respons memiliki n = 3.000, kemencengan 2,8, dan Shapiro-Wilk p < 0,0001.
   (a) Apakah data ini Normal?
   (b) Apakah kesimpulan itu berasal dari uji formal atau statistik bentuk? Mana yang lebih Anda percayai, dan mengapa?
   (c) Usulkan dua cara menangani data ini untuk analisis lanjutan.

9. Jelaskan hubungan antara distribusi Poisson dan Eksponensial. Beri satu contoh konkret dari sistem komputasi di mana keduanya muncul bersamaan.

### Tingkat Mahir

10. Sebuah tim melaporkan waktu respons API dengan asumsi Normal, lalu menghitung bahwa 99,7% permintaan selesai di bawah μ + 3σ = 480 ms. Data sebenarnya: p99,7 = 4.200 ms.
    (a) Apa yang salah dengan asumsi tim itu?
    (b) Bagaimana bentuk sebaran yang sebenarnya?
    (c) Rancang prosedur pemeriksaan yang seharusnya mereka lakukan.
    (d) Usulkan cara pelaporan yang jujur tanpa mengandaikan kenormalan.

11. Simulasikan dan bandingkan tiga distribusi kontinu (Uniform, Eksponensial, Normal) dengan mean yang sama.
    (a) Bangkitkan 10.000 nilai dari masing-masing dengan mean = 100.
    (b) Bandingkan simpangan baku, kemencengan, dan kurtosisnya.
    (c) Buat Q-Q plot masing-masing terhadap Normal.
    (d) Untuk tiap distribusi, hitung P(X > 200) dan bandingkan.
    (e) Jelaskan: mengapa dua sebaran dengan mean sama dapat memberi risiko ekor yang sangat berbeda?

12. Tulislah panduan praktis (satu halaman) berjudul *"Memeriksa Kenormalan: Prosedur dan Jebakannya"* untuk tim analis data. Sertakan: langkah pemeriksaan berurutan, kapan uji formal berguna dan kapan menyesatkan, cara membaca Q-Q plot, dan apa yang harus dilakukan bila data tidak Normal.

---

## Rangkuman

1. Pada peubah kontinu, **P(X = x) = 0**; yang bermakna adalah probabilitas pada selang, dihitung sebagai **luas di bawah PDF**.
2. **PDF boleh lebih dari 1** — yang harus sama dengan 1 adalah luasnya.
3. **Uniform** untuk nilai yang sama mungkinnya; **Eksponensial** untuk waktu tunggu antar kejadian Poisson.
4. Eksponensial bersifat **tanpa memori**, seperti Geometrik pada kasus diskret.
5. Pada `scipy.stats.expon`, parameter `scale` adalah **1/λ**. **Selalu verifikasi dengan `.mean()`.**
6. **Aturan empiris 68–95–99,7** memberi cara cepat menilai kewajaran sebuah nilai.
7. **Skor-z** memungkinkan perbandingan nilai dari dua sebaran berbeda.
8. **Tidak semua data Normal.** Data Informatika hampir selalu menceng kanan.
9. Periksa kenormalan dengan **Q-Q plot**, bukan hanya uji formal — pada sampel besar uji formal hampir selalu menolak.
10. Pertanyaan yang tepat bukan "apakah persis Normal", melainkan **"apakah penyimpangannya cukup kecil untuk metode yang akan dipakai"**.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 4, 6. Pearson.
2. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.), Bab 4. Wiley.
3. Ghasemi, A., & Zahediasl, S. (2012). Normality tests for statistical analysis. *International Journal of Endocrinology and Metabolism*, 10(2), 486–489.
4. Dean, J., & Barroso, L. A. (2013). The Tail at Scale. *Communications of the ACM*, 56(2), 74–80.
5. Dokumentasi SciPy — *Continuous distributions*. <https://docs.scipy.org/doc/scipy/reference/stats.html>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
