# BAB 8: EKSPEKTASI, VARIANS, DAN DISTRIBUSI SAMPLING

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `PS-Sub-CPMK081-1` | Menghitung ekspektasi dan varians serta menerapkan sifat-sifatnya | C3 |
| `PS-Sub-CPMK081-1` | Membedakan sebaran populasi, sebaran sampel, dan distribusi sampling | C2–C4 |
| `PS-Sub-CPMK081-1` | Menganalisis Teorema Limit Pusat dan batas keberlakuannya | C4 |

---

## 8.1 Ekspektasi

### 8.1.1 Definisi

$$E[X] = \sum_x x \cdot p(x) \quad \text{(diskret)} \qquad E[X] = \int_{-\infty}^{\infty} x f(x)\,dx \quad \text{(kontinu)}$$

Ekspektasi adalah **rata-rata jangka panjang** bila percobaan diulang tak hingga kali. Ia **bukan** nilai yang pasti muncul — dan seringkali bukan nilai yang mungkin muncul sama sekali.

### 8.1.2 Contoh: Anggaran Penanganan Insiden

| Keparahan | Probabilitas | Biaya (juta rupiah) |
|-----------|--------------|---------------------|
| Ringan | 0,70 | 2 |
| Sedang | 0,25 | 12 |
| Berat | 0,05 | 80 |

```python
import numpy as np

biaya = np.array([2, 12, 80])
prob = np.array([0.70, 0.25, 0.05])

E = (biaya * prob).sum()
Var = ((biaya - E) ** 2 * prob).sum()

print(f"E[biaya]  = Rp {E:.2f} juta")
print(f"Var(biaya)= {Var:.2f}")
print(f"SD(biaya) = Rp {np.sqrt(Var):.2f} juta")
print(f"\nPerhatikan: Rp {E:.2f} juta BUKAN salah satu nilai yang mungkin.")

# Penerapan: anggaran tahunan untuk 200 insiden
n_insiden = 200
print(f"\nAnggaran untuk {n_insiden} insiden:")
print(f"  Ekspektasi total : Rp {E*n_insiden:,.2f} juta")
print(f"  SD total         : Rp {np.sqrt(Var*n_insiden):,.2f} juta")
print(f"  Cadangan 2 SD    : Rp {2*np.sqrt(Var*n_insiden):,.2f} juta")
```

> **Penerapan langsung.** Anggaran yang wajar adalah 200 × E[biaya]. Tetapi karena simpangan bakunya besar, anggaran itu **harus disertai cadangan** — persis alasan perusahaan menyediakan dana kontingensi.
>
> Perhatikan juga: SD total tumbuh sebesar **√200**, bukan 200. Ini konsekuensi dari sifat varians yang dibahas di §8.2.

### 8.1.3 Sifat Ekspektasi

| Sifat | Rumus | Syarat |
|-------|-------|--------|
| Konstanta | E[c] = c | — |
| Skala | E[aX] = a·E[X] | — |
| Linearitas | E[aX + b] = a·E[X] + b | — |
| **Penjumlahan** | E[X + Y] = E[X] + E[Y] | **Berlaku SELALU**, bahkan bila X dan Y tidak bebas |

> **Linearitas ekspektasi adalah salah satu sifat paling berguna dalam probabilitas**, justru karena ia berlaku tanpa syarat kebebasan.
>
> Banyak persoalan yang tampak rumit menjadi mudah bila dipecah menjadi jumlah peubah acak sederhana. Contohnya: menurunkan E[X] untuk Binomial menjadi sepele bila X dipandang sebagai jumlah n peubah Bernoulli.

---

## 8.2 Varians Peubah Acak

$$\text{Var}(X) = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$

| Sifat | Rumus | Syarat |
|-------|-------|--------|
| Konstanta | Var(c) = 0 | — |
| Skala | Var(aX) = **a²**·Var(X) | Perhatikan kuadratnya |
| Geseran | Var(X + b) = Var(X) | Menggeser tidak mengubah sebaran |
| Penjumlahan | Var(X + Y) = Var(X) + Var(Y) | **Hanya bila X dan Y BEBAS** |

```python
import numpy as np

rng = np.random.default_rng(42)
X = rng.normal(100, 15, 200_000)

print(f"Var(X)     = {X.var(ddof=1):>10.2f}")
print(f"Var(3X)    = {(3*X).var(ddof=1):>10.2f}")
print(f"9 × Var(X) = {9*X.var(ddof=1):>10.2f}   ← sesuai a² = 9")
print(f"Var(X+50)  = {(X+50).var(ddof=1):>10.2f}   ← tidak berubah")
```

> **Mengapa ini penting untuk Informatika.** Bila Anda menjumlahkan waktu eksekusi n tahap yang saling bebas, variansnya **bertambah secara linear** — sehingga **simpangan bakunya tumbuh sebesar √n**, bukan n.
>
> Konsekuensinya: sistem dengan banyak tahap memiliki waktu total yang **relatif lebih stabil** daripada tiap tahapnya. Ini fenomena nyata yang disebut *averaging effect*.

---

## 8.3 Distribusi Sampling

### 8.3.1 Tiga Sebaran yang Berbeda

Ini konsep paling penting — sekaligus paling sulit — di seluruh buku ini. Luangkan waktu memahaminya.

```
  1. SEBARAN POPULASI          2. SEBARAN SATU SAMPEL      3. DISTRIBUSI SAMPLING
     seluruh N anggota            n anggota yang diambil       rata-rata dari SEMUA
                                                               sampel berukuran n
                                                               yang mungkin diambil
     ╭──╮  ╭──╮                   ·  ·· ·                          ╭─╮
    ╱    ╲╱    ╲                 · ·  · ··                        ╱   ╲
   ╱            ╲               ·   ·· ·                        ╱       ╲
   bisa berbentuk apa saja      bentuk mirip populasi        SELALU mendekati
                                                              Normal bila n besar
```

> **Distribusi sampling** adalah sebaran sebuah **statistik** (misalnya x̄) bila kita mengambil sampel berukuran n berulang-ulang dari populasi yang sama.

Kita tidak pernah benar-benar melakukan pengambilan berulang itu dalam praktik. **Tetapi mengetahui bentuk distribusi sampling secara teoretis adalah yang memungkinkan kita membuat interval kepercayaan dan uji hipotesis dari satu sampel saja.**

### 8.3.2 Sifat Distribusi Sampling Rata-Rata

Bila sampel acak berukuran n diambil dari populasi dengan rata-rata μ dan simpangan baku σ:

$$E[\bar{X}] = \mu \qquad \text{SD}(\bar{X}) = \frac{\sigma}{\sqrt{n}}$$

Besaran σ/√n disebut **galat baku** (*standard error*, SE).

| Istilah | Lambang | Mengukur apa |
|---------|---------|--------------|
| Simpangan baku | σ atau s | Sebaran **data individual** |
| **Galat baku** | σ/√n | Sebaran **rata-rata sampel** |

> **Membedakan keduanya adalah sumber kebingungan terbesar bagi pemula.** Simpangan baku menjawab "seberapa menyebar datanya"; galat baku menjawab "seberapa menyebar rata-rata sampel di sekitar μ".
>
> Galat baku **selalu lebih kecil** daripada simpangan baku (untuk n > 1), dan mengecil seiring n bertambah.

### 8.3.3 Hukum Akar n

```python
import numpy as np

sigma = 15
print(f"{'n':>7}  {'SE = σ/√n':>12}  {'Rasio thd n=1':>15}")
for n in [1, 4, 16, 64, 256, 1024]:
    print(f"{n:>7}  {sigma/np.sqrt(n):>12.4f}  {'1/' + str(int(np.sqrt(n))):>15}")
```

> **Hukum akar n:** untuk memperkecil galat baku menjadi **separuh**, ukuran sampel harus **dilipatempatkan**.
>
> Inilah alasan survei nasional memakai 1.200–2.400 responden, bukan 100.000 — menambah responden memberi hasil tambahan yang makin kecil dengan biaya yang terus meningkat.
>
> Perhatikan juga bahwa rumus SE **tidak mengandung N** (ukuran populasi). Survei 1.200 orang sama akuratnya untuk populasi 10.000 maupun 280 juta — selama sampelnya acak. Fakta ini sering mengejutkan.

---

## 8.4 Teorema Limit Pusat

### 8.4.1 Pernyataan

> **Teorema Limit Pusat (CLT).** Bila X₁, …, Xₙ adalah sampel acak bebas dari populasi **berbentuk apa pun** dengan rata-rata μ dan simpangan baku σ **berhingga**, maka untuk n yang cukup besar:
>
> $$\bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right)$$

**Tiga hal yang membuat teorema ini luar biasa:**

1. Berlaku untuk **sebaran populasi apa pun** — menceng, bimodal, uniform, bahkan hanya dua nilai.
2. Menjelaskan mengapa distribusi Normal muncul di mana-mana dalam statistika terapan.
3. Memungkinkan inferensi **tanpa mengetahui bentuk sebaran populasi**.

### 8.4.2 Simulasi

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(42)

def demo_clt(fungsi_populasi, nama, ukuran=(1, 5, 30, 100), ulangan=5000):
    fig, axes = plt.subplots(1, len(ukuran) + 1, figsize=(19, 3.5))
    populasi = fungsi_populasi(50_000)
    axes[0].hist(populasi, bins=50, color="#7f8c8d", edgecolor="white")
    axes[0].set_title(f"POPULASI\n{nama}"); axes[0].set_yticks([])
    for ax, n in zip(axes[1:], ukuran):
        rata = np.array([fungsi_populasi(n).mean() for _ in range(ulangan)])
        _, p = stats.shapiro(rata[:500])
        ax.hist(rata, bins=50, color="steelblue", edgecolor="white")
        ax.set_title(f"n = {n}\nShapiro p = {p:.3f}"); ax.set_yticks([])
    plt.suptitle(f"Teorema Limit Pusat — {nama}", y=1.06)
    plt.tight_layout(); plt.show()

demo_clt(lambda n: rng.exponential(2, n), "Eksponensial (menceng kanan)")
demo_clt(lambda n: rng.binomial(1, 0.15, n), "Bernoulli p=0,15 (dua nilai saja)")
demo_clt(lambda n: np.concatenate([rng.normal(2, 0.4, n//2),
                                   rng.normal(9, 0.4, n - n//2)]), "Bimodal")
```

### 8.4.3 Berapa n yang "Cukup Besar"?

| Bentuk Populasi | n Minimum |
|-----------------|-----------|
| Normal | n = 1 (langsung Normal) |
| Simetris tanpa pencilan | n ≥ 15 |
| Agak menceng | n ≥ 30 |
| Sangat menceng atau banyak pencilan | n ≥ 50, kadang jauh lebih |

> **Aturan praktis n ≥ 30 banyak dikutip, tetapi bukan hukum.** Untuk sebaran yang sangat menceng — dan waktu respons sering demikian — n = 30 belum tentu cukup. Periksa dengan simulasi bila ragu.

### 8.4.4 Kapan CLT Tidak Berlaku

CLT mensyaratkan populasi memiliki **varians berhingga**. Distribusi Cauchy tidak memenuhinya.

```python
import numpy as np

rng = np.random.default_rng(0)
print(f"{'n':>7}  {'SD rata-rata Normal':>21}  {'SD rata-rata Cauchy':>21}")
for n in [1, 10, 100, 1000]:
    r_norm = np.array([rng.normal(0, 1, n).mean() for _ in range(3000)])
    r_cauchy = np.array([rng.standard_cauchy(n).mean() for _ in range(3000)])
    print(f"{n:>7}  {r_norm.std():>21.4f}  {r_cauchy.std():>21.4f}")
print("\n→ Rata-rata Normal MENYEMPIT seiring n; Cauchy TIDAK PERNAH stabil.")
```

Dalam praktik Informatika, sebaran berekor sangat berat (*heavy-tailed*) — seperti ukuran berkas atau durasi sesi pada sebagian sistem — dapat mendekati perilaku ini, sehingga CLT berlaku jauh lebih lambat dari yang diharapkan.

### 8.4.5 Mengapa CLT Menjadi Tulang Punggung Inferensi

```
  Kita hanya punya SATU sampel.
              │
              ▼
  CLT memberi tahu: "bila kamu mengambil banyak sampel,
  rata-ratanya akan tersebar Normal di sekitar μ
  dengan galat baku σ/√n"
              │
              ▼
  Maka dari SATU sampel kita bisa berkata:
  "μ kemungkinan besar berada dalam x̄ ± (nilai kritis × SE)"
              │
              ▼
  INTERVAL KEPERCAYAAN (Bab 9)
  UJI HIPOTESIS (Bab 10–12)
```

**Tanpa CLT, seluruh bangunan statistika inferensial klasik runtuh.**

---

## 8.5 Perencanaan Ukuran Sampel

```python
import numpy as np
from scipy import stats

def n_untuk_presisi(sigma, margin, kepercayaan=0.95):
    z = stats.norm.ppf(1 - (1 - kepercayaan)/2)
    return int(np.ceil((z * sigma / margin) ** 2))

sigma = 35     # dari data pendahuluan waktu respons
print(f"{'Margin galat':>14}  {'n (90%)':>9}  {'n (95%)':>9}  {'n (99%)':>9}")
for me in [20, 10, 5, 2, 1]:
    print(f"{me:>11} ms  "
          f"{n_untuk_presisi(sigma, me, 0.90):>9,}  "
          f"{n_untuk_presisi(sigma, me, 0.95):>9,}  "
          f"{n_untuk_presisi(sigma, me, 0.99):>9,}")
```

---

## AI Corner — Tingkat Lanjut

### Konsep yang Paling Sering Dikacaukan AI

Perbedaan antara **simpangan baku** dan **galat baku** adalah salah satu kesalahan paling umum — dan AI pun sering keliru, terutama bila pertanyaan diajukan dengan bahasa yang ambigu.

**Percobaan:**

> *"Saya punya 100 pengukuran waktu respons dengan simpangan baku 35 ms. Berapa simpangan baku dari rata-ratanya?"*

Jawaban benar: 35/√100 = 3,5 ms.

Sebagian model menjawab 35 ms — tidak membedakan sebaran data dari sebaran rata-rata.

### Mengapa Ini Berbahaya

Salah membedakan keduanya akan membuat **interval kepercayaan Anda sepuluh kali terlalu lebar** (Bab 9) dan **uji hipotesis Anda kehilangan seluruh kuasanya** (Bab 10).

Ini bukan kesalahan kosmetik — ia mengubah kesimpulan.

### Latihan Memeriksa

Ketika AI memberi jawaban yang melibatkan "simpangan baku", tanyakan:

> *"Yang kamu maksud simpangan baku data atau galat baku rata-rata? Tuliskan rumusnya."*

Bila jawabannya mengandung √n di penyebut, ia berbicara tentang galat baku.

### Pemakaian yang Dianjurkan

```
PROMPT YANG BAIK:
"Saya punya sampel n=64 dengan s=40 ms. Saya menghitung SE = 40/√64 = 5 ms.
 Apakah benar bahwa SE inilah yang saya pakai untuk interval kepercayaan
 rata-rata, bukan s? Tolong jelaskan alasannya."

Mengapa baik: Anda sudah menghitung, sudah punya dugaan tentang mana
yang dipakai, dan meminta AI memeriksa PEMAHAMAN — bukan memberi angka.
```

---

## Latihan Soal

### Tingkat Dasar

1. Sebuah peubah acak X memiliki nilai 0, 1, 2 dengan probabilitas 0,5; 0,3; 0,2. Hitung E[X] dan Var(X).

2. Jelaskan perbedaan simpangan baku dan galat baku dengan kalimat Anda sendiri.

3. Populasi memiliki σ = 20. Hitung galat baku untuk n = 4, 25, 100, 400.

4. Nyatakan Teorema Limit Pusat dengan kalimat Anda sendiri. Sebutkan syaratnya.

5. Mengapa Var(X + Y) = Var(X) + Var(Y) memerlukan syarat kebebasan, sedangkan E[X + Y] = E[X] + E[Y] tidak?

### Tingkat Menengah

6. Sebuah tim menangani insiden dengan biaya: ringan (p=0,6; Rp 3 juta), sedang (p=0,3; Rp 15 juta), berat (p=0,1; Rp 60 juta).
   (a) Hitung E[biaya] dan SD(biaya).
   (b) Berapa anggaran untuk 150 insiden setahun?
   (c) Berapa SD untuk total 150 insiden? (Petunjuk: tumbuh sebesar √150.)
   (d) Berapa cadangan yang Anda sarankan agar aman pada tingkat 2 SD?

7. Sebuah survei ingin memperkirakan rata-rata waktu belajar mahasiswa dengan margin galat ±0,5 jam pada tingkat kepercayaan 95%. Dari studi pendahuluan, σ ≈ 4,5 jam.
   (a) Berapa ukuran sampel yang diperlukan?
   (b) Berapa bila margin diperketat menjadi ±0,25 jam?
   (c) Berapa rasio (b) terhadap (a)? Jelaskan dengan hukum akar n.
   (d) Apakah ukuran populasi memengaruhi jawaban? Jelaskan.

8. Jelaskan mengapa survei nasional dengan 1.200 responden dapat memberikan margin galat ±3%, sedangkan survei kelas dengan 40 mahasiswa terasa "terlalu sedikit".
   (a) Hitung margin galat untuk kedua kasus (proporsi, p̂ = 0,5).
   (b) Apakah selisihnya sebesar yang diduga orang?
   (c) Jelaskan peran ukuran populasi dalam rumus SE.

9. Rancang simulasi untuk menunjukkan CLT dari sebuah populasi bimodal.
   (a) Bangkitkan populasi dari campuran dua Normal yang terpisah jauh.
   (b) Ambil sampel berukuran n = 2, 10, 30, 100 dan hitung rata-ratanya (5.000 kali).
   (c) Pada n berapa distribusi sampling mulai tampak Normal?
   (d) Bandingkan dengan populasi Eksponensial. Mana yang memerlukan n lebih besar?

### Tingkat Mahir

10. Turunkan E[X] dan Var(X) untuk distribusi Binomial dengan memandang X sebagai jumlah n peubah Bernoulli yang saling bebas.
    (a) Gunakan linearitas ekspektasi untuk E[X].
    (b) Gunakan sifat penjumlahan varians untuk Var(X) — sebutkan mengapa syarat kebebasan diperlukan.
    (c) Apa yang terjadi pada Var(X) bila percobaan **tidak** bebas? Beri contoh.

11. Distribusi Cauchy melanggar syarat CLT karena variansnya tak hingga.
    (a) Simulasikan rata-rata sampel dari Cauchy untuk n = 1, 10, 100, 1.000, 10.000.
    (b) Buat grafik SD rata-rata terhadap n. Bandingkan dengan Normal.
    (c) Jelaskan mengapa rata-rata Cauchy tidak pernah "menstabil".
    (d) Adakah besaran dalam sistem komputasi yang berperilaku menyerupai ini? Beri contoh dan jelaskan implikasinya bagi pelaporan kinerja.

12. Tulislah penjelasan (400–500 kata) untuk seorang manajer non-teknis yang bertanya: *"Mengapa kita perlu mengukur 400 permintaan, bukan cukup 20 saja? Bukankah rata-ratanya akan sama?"* Sertakan: peran galat baku, hukum akar n, dan mengapa presisi berbiaya.

---

## Rangkuman

1. **Ekspektasi** adalah rata-rata jangka panjang — berguna untuk menganggarkan, meskipun sering bukan nilai yang mungkin muncul.
2. **Linearitas ekspektasi** E[X+Y] = E[X]+E[Y] berlaku **selalu**; varians hanya dapat dijumlahkan bila peubahnya **bebas**.
3. Var(aX) = **a²**Var(X) — perhatikan kuadratnya. Var(X+b) = Var(X).
4. Menjumlahkan n tahap bebas membuat SD tumbuh sebesar **√n**, bukan n.
5. Ada **tiga sebaran yang berbeda**: populasi, satu sampel, dan **distribusi sampling**. Mencampuradukkannya adalah sumber kebingungan terbesar.
6. **Galat baku** SE = σ/√n mengukur sebaran **rata-rata sampel**, bukan sebaran data.
7. **Hukum akar n:** memperkecil SE menjadi separuh memerlukan empat kali lipat sampel.
8. Rumus SE **tidak mengandung ukuran populasi** — survei 1.200 orang sama akuratnya untuk 10.000 maupun 280 juta jiwa.
9. **CLT** menyatakan rata-rata sampel mendekati Normal untuk n besar, berapa pun bentuk populasinya — **asalkan variansnya berhingga**.
10. Aturan n ≥ 30 adalah panduan, bukan hukum.
11. **Tanpa CLT, inferensi statistika klasik tidak mungkin dilakukan.**

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 4, 8. Pearson.
2. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.), Bab 7. Wiley.
3. Ross, S. M. (2019). *A First Course in Probability* (10th ed.), Bab 8. Pearson.
4. Downey, A. B. (2014). *Think Stats* (2nd ed.), Bab 8. O'Reilly Media.
5. Taleb, N. N. (2020). *Statistical Consequences of Fat Tails*. STEM Academic Press.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
