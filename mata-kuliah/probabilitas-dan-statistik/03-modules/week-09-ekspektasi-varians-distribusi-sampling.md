# Minggu 9: Ekspektasi, Varians, dan Distribusi Sampling

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 9 |
| **Topik** | Ekspektasi dan varians peubah acak, distribusi sampling, galat baku, Teorema Limit Pusat |
| **CPL / CPMK** | CPL08 / CPMK081 |
| **Sub-CPMK** | `PS-Sub-CPMK081-1` |
| **Indikator Mingguan** | Menghitung ekspektasi dan varians, serta menjelaskan distribusi sampling dan Teorema Limit Pusat |
| **Level Bloom** | C3–C4 (Menerapkan–Menganalisis) |
| **Durasi** | 150 menit tatap muka |
| **Metode** | Kuliah, simulasi CLT, diskusi |

---

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menghitung** (C3) ekspektasi dan varians peubah acak diskret maupun kontinu.
2. **Menerapkan** (C3) sifat linearitas ekspektasi dan aturan varians untuk kombinasi peubah acak.
3. **Menjelaskan** (C2) apa itu distribusi sampling dan mengapa ia berbeda dari distribusi populasi.
4. **Menghitung** (C3) galat baku rata-rata dan menjelaskan pengaruh ukuran sampel terhadapnya.
5. **Menganalisis** (C4) Teorema Limit Pusat melalui simulasi dan menjelaskan mengapa ia menjadi tulang punggung inferensi.

---

## Materi Pembelajaran

### 1. Ekspektasi (Nilai Harapan)

#### 1.1 Definisi

$$E[X] = \sum_x x \cdot p(x) \quad \text{(diskret)} \qquad E[X] = \int_{-\infty}^{\infty} x f(x)\,dx \quad \text{(kontinu)}$$

Ekspektasi adalah **rata-rata jangka panjang** bila percobaan diulang tak hingga kali. Ia **bukan** nilai yang pasti muncul — dan seringkali bukan nilai yang mungkin muncul sama sekali.

#### 1.2 Contoh: Biaya Harapan Penanganan Insiden

> Sebuah tim menangani insiden dengan tiga tingkat keparahan. Biaya penanganan dan probabilitasnya:

| Keparahan | Probabilitas | Biaya (juta rupiah) |
|-----------|--------------|---------------------|
| Ringan | 0,70 | 2 |
| Sedang | 0,25 | 12 |
| Berat | 0,05 | 80 |

```python
import numpy as np

biaya = np.array([2, 12, 80])
prob = np.array([0.70, 0.25, 0.05])

ekspektasi = (biaya * prob).sum()
varians = ((biaya - ekspektasi) ** 2 * prob).sum()
simpangan = np.sqrt(varians)

print(f"E[biaya]   = Rp {ekspektasi:.2f} juta")
print(f"Var(biaya) = {varians:.2f}")
print(f"SD(biaya)  = Rp {simpangan:.2f} juta")
print(f"\nPerhatikan: Rp {ekspektasi:.2f} juta BUKAN salah satu nilai yang mungkin.")
print("Ia adalah rata-rata jangka panjang, berguna untuk menganggarkan.")
```

> **Penerapan langsung:** bila tim menangani 200 insiden setahun, anggaran yang wajar adalah 200 × E[biaya]. Tetapi karena simpangan bakunya besar, anggaran itu **harus disertai cadangan** — persis alasan perusahaan menyediakan dana kontingensi.

#### 1.3 Sifat Ekspektasi

| Sifat | Rumus | Catatan |
|-------|-------|---------|
| Konstanta | E[c] = c | |
| Skala | E[aX] = a·E[X] | |
| Linearitas | E[aX + b] = a·E[X] + b | |
| **Penjumlahan** | E[X + Y] = E[X] + E[Y] | **Berlaku selalu**, bahkan bila X dan Y tidak bebas |

> **Linearitas ekspektasi adalah salah satu sifat paling berguna dalam probabilitas** karena berlaku tanpa syarat kebebasan. Banyak persoalan yang tampak rumit menjadi mudah bila dipecah menjadi jumlah peubah acak sederhana.

---

### 2. Varians Peubah Acak

$$\text{Var}(X) = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$

| Sifat | Rumus | Syarat |
|-------|-------|--------|
| Konstanta | Var(c) = 0 | |
| Skala | Var(aX) = a²·Var(X) | Perhatikan **kuadrat** |
| Geseran | Var(X + b) = Var(X) | Menggeser tidak mengubah sebaran |
| Penjumlahan | Var(X + Y) = Var(X) + Var(Y) | **Hanya bila X dan Y bebas** |

```python
import numpy as np

# Verifikasi Var(aX) = a² Var(X)
rng = np.random.default_rng(42)
X = rng.normal(100, 15, 100_000)
a = 3

print(f"Var(X)        = {X.var(ddof=1):.2f}")
print(f"Var(3X)       = {(a*X).var(ddof=1):.2f}")
print(f"9 × Var(X)    = {9 * X.var(ddof=1):.2f}")

# Verifikasi Var(X + b) = Var(X)
print(f"\nVar(X + 50)   = {(X + 50).var(ddof=1):.2f}   (tidak berubah)")
```

> **Mengapa ini penting untuk Informatika:** bila Anda menjumlahkan waktu eksekusi n tahap yang saling bebas, variansnya bertambah — sehingga **simpangan bakunya tumbuh sebesar √n**, bukan n. Inilah alasan sistem dengan banyak tahap memiliki waktu total yang relatif lebih stabil daripada tiap tahapnya.

---

### 3. Distribusi Sampling

#### 3.1 Gagasan yang Sering Membingungkan

Ini konsep paling penting — sekaligus paling sulit — di seluruh mata kuliah. Luangkan waktu memahaminya.

```
  TIGA SEBARAN YANG BERBEDA:

  1. SEBARAN POPULASI          2. SEBARAN SATU SAMPEL      3. DISTRIBUSI SAMPLING
     seluruh N anggota            n anggota yang diambil       rata-rata dari SEMUA
                                                               sampel berukuran n yang
                                                               mungkin diambil
     ╭──╮  ╭──╮                   ·  ·· ·                          ╭─╮
    ╱    ╲╱    ╲                 · ·  · ··                        ╱   ╲
   ╱            ╲               ·   ·· ·                        ╱       ╲
   bisa berbentuk apa saja      bentuk mirip populasi        SELALU mendekati
                                                              Normal bila n besar
```

> **Distribusi sampling** adalah sebaran sebuah **statistik** (misalnya x̄) bila kita mengambil sampel berukuran n berulang-ulang dari populasi yang sama.

Kita tidak pernah benar-benar melakukan pengambilan berulang itu dalam praktik. Tetapi **mengetahui bentuk distribusi sampling secara teoretis** adalah yang memungkinkan kita membuat interval kepercayaan dan uji hipotesis dari satu sampel saja.

#### 3.2 Sifat Distribusi Sampling Rata-Rata

Bila sampel acak berukuran n diambil dari populasi dengan rata-rata μ dan simpangan baku σ:

$$E[\bar{X}] = \mu \qquad \text{SD}(\bar{X}) = \frac{\sigma}{\sqrt{n}}$$

Besaran σ/√n disebut **galat baku** (*standard error*, SE).

| Istilah | Lambang | Mengukur apa |
|---------|---------|--------------|
| Simpangan baku | σ atau s | Sebaran **data individual** |
| **Galat baku** | σ/√n | Sebaran **rata-rata sampel** |

```python
import numpy as np

sigma = 15   # simpangan baku populasi

print("Pengaruh ukuran sampel terhadap galat baku:")
print(f"{'n':>6}  {'SE = σ/√n':>12}  {'Perbandingan':>14}")
for n in [1, 4, 25, 100, 400, 1600]:
    se = sigma / np.sqrt(n)
    print(f"{n:>6}  {se:>12.4f}  {'1/' + str(int(np.sqrt(n))):>14}")
```

> **Hukum akar n.** Untuk memperkecil galat baku menjadi separuh, ukuran sampel harus **dilipatempatkan**. Inilah alasan survei nasional memakai 1.200–2.400 responden, bukan 100.000 — menambah responden memberi hasil yang makin sedikit dengan biaya yang terus meningkat.

---

### 4. Teorema Limit Pusat (CLT)

#### 4.1 Pernyataan

> **Teorema Limit Pusat.** Bila X₁, X₂, …, Xₙ adalah sampel acak bebas dari populasi **berbentuk apa pun** dengan rata-rata μ dan simpangan baku σ berhingga, maka untuk n yang cukup besar:
>
> $$\bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right)$$

**Tiga hal yang membuat teorema ini luar biasa:**

1. Berlaku untuk **sebaran populasi apa pun** — menceng, bimodal, uniform, bahkan sangat tidak normal.
2. Menjelaskan mengapa distribusi Normal muncul di mana-mana dalam statistika terapan.
3. Memungkinkan inferensi **tanpa mengetahui bentuk sebaran populasi**.

#### 4.2 Simulasi: Membuktikan Sendiri

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

def simulasi_clt(sebaran_populasi, nama, ukuran_sampel=(1, 5, 30, 100),
                 n_ulangan=5000):
    """Menunjukkan CLT bekerja dari sebaran populasi apa pun."""
    fig, axes = plt.subplots(1, len(ukuran_sampel) + 1, figsize=(19, 3.6))

    # Panel pertama: sebaran populasi aslinya
    populasi = sebaran_populasi(50_000)
    axes[0].hist(populasi, bins=50, color="#7f8c8d", edgecolor="white")
    axes[0].set_title(f"POPULASI\n{nama}")
    axes[0].set_yticks([])

    # Panel berikutnya: distribusi sampling rata-rata untuk berbagai n
    for ax, n in zip(axes[1:], ukuran_sampel):
        rata_rata = np.array([sebaran_populasi(n).mean()
                              for _ in range(n_ulangan)])
        ax.hist(rata_rata, bins=50, color="steelblue", edgecolor="white")
        ax.set_title(f"n = {n}\nmean={rata_rata.mean():.2f}, "
                     f"SD={rata_rata.std(ddof=1):.3f}")
        ax.set_yticks([])

    plt.suptitle(f"Teorema Limit Pusat — populasi {nama}", y=1.05)
    plt.tight_layout()
    plt.show()

# Tiga sebaran populasi yang sangat tidak Normal
simulasi_clt(lambda n: rng.exponential(2, n), "Eksponensial (menceng kanan)")
simulasi_clt(lambda n: rng.uniform(0, 10, n), "Uniform (datar)")
simulasi_clt(lambda n: np.concatenate([rng.normal(2, 0.5, n//2),
                                       rng.normal(8, 0.5, n - n//2)]),
             "Bimodal (dua puncak)")
```

**Yang akan Anda amati:**

| n | Bentuk distribusi sampling |
|---|----------------------------|
| 1 | Sama persis dengan populasi |
| 5 | Mulai menggumpal di tengah |
| 30 | Sudah cukup mirip Normal |
| 100 | Sangat mendekati Normal, dan jauh lebih sempit |

#### 4.3 Berapa n yang "Cukup Besar"?

| Bentuk Populasi | n Minimum |
|-----------------|-----------|
| Normal | n = 1 (langsung Normal) |
| Simetris tanpa pencilan | n ≥ 15 |
| Agak menceng | n ≥ 30 |
| Sangat menceng atau banyak pencilan | n ≥ 50, kadang lebih |

> **Aturan praktis n ≥ 30** banyak dikutip, tetapi bukan hukum. Untuk sebaran yang sangat menceng — dan waktu respons sering demikian — n = 30 belum tentu cukup. Periksa dengan simulasi bila ragu.

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(7)

def kapan_clt_cukup(fungsi_populasi, nama, n_ulangan=3000):
    """Menguji kenormalan distribusi sampling pada berbagai ukuran sampel."""
    print(f"\n{nama}")
    print(f"{'n':>5}  {'p-value Shapiro':>16}  Kesimpulan")
    for n in [5, 10, 20, 30, 50, 100]:
        rata = np.array([fungsi_populasi(n).mean() for _ in range(n_ulangan)])
        # Shapiro-Wilk pada subsampel agar tidak terlalu sensitif
        _, p = stats.shapiro(rata[:500])
        status = "mendekati Normal" if p > 0.05 else "belum Normal"
        print(f"{n:>5}  {p:>16.4f}  {status}")

kapan_clt_cukup(lambda n: rng.exponential(2, n), "Populasi Eksponensial")
kapan_clt_cukup(lambda n: rng.lognormal(0, 1.5, n), "Populasi Lognormal (sangat menceng)")
```

#### 4.4 Mengapa CLT Menjadi Tulang Punggung Inferensi

```
  Kita hanya punya SATU sampel.
              │
              ▼
  CLT memberi tahu: "bila kamu mengambil banyak sampel,
  rata-ratanya akan tersebar Normal di sekitar μ
  dengan galat baku σ/√n"
              │
              ▼
  Maka dari satu sampel kita bisa berkata:
  "μ kemungkinan besar berada dalam x̄ ± (nilai kritis × SE)"
              │
              ▼
  INTERVAL KEPERCAYAAN (Minggu 10)
  UJI HIPOTESIS (Minggu 11–13)
```

Tanpa CLT, seluruh bangunan statistika inferensial klasik runtuh.

---

### 5. Penerapan: Berapa Sampel yang Saya Butuhkan?

```python
import numpy as np
from scipy import stats

def ukuran_sampel_untuk_presisi(sigma, margin_error, kepercayaan=0.95):
    """Menghitung n minimum agar margin galat tidak melebihi nilai tertentu."""
    z = stats.norm.ppf(1 - (1 - kepercayaan) / 2)
    n = (z * sigma / margin_error) ** 2
    return int(np.ceil(n))

# Kasus: mengukur rata-rata waktu respons API
# Dari data pendahuluan, simpangan baku ≈ 35 ms
sigma = 35

print("Sampel yang dibutuhkan untuk berbagai tingkat presisi:")
print(f"{'Margin galat':>14}  {'n (95%)':>10}  {'n (99%)':>10}")
for me in [20, 10, 5, 2, 1]:
    n95 = ukuran_sampel_untuk_presisi(sigma, me, 0.95)
    n99 = ukuran_sampel_untuk_presisi(sigma, me, 0.99)
    print(f"{me:>11} ms  {n95:>10}  {n99:>10}")
```

> Perhatikan pertumbuhannya: memperkecil margin galat dari 10 ms ke 5 ms memerlukan **empat kali lipat** sampel. Ini konsekuensi langsung dari hukum akar n.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (Mandiri — 60 menit)

1. Membaca [Bab 8 buku ajar](../06-buku-ajar/bab-08-ekspektasi-varians-sampling.md).
2. Menjawab: *"Bila populasi berbentuk sangat menceng, apakah rata-rata dari sampel berukuran 50 juga akan menceng?"* Tuliskan dugaan Anda sebelum kelas.

### Di Kelas (150 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–15' | Pembahasan soal UTS dan kesalahan yang paling sering muncul |
| 15–45' | Kuliah: ekspektasi, varians, dan sifat-sifatnya; kasus anggaran insiden |
| 45–60' | Kuliah: tiga sebaran yang berbeda — populasi, sampel, distribusi sampling |
| 60–70' | Istirahat |
| 70–105' | **Simulasi CLT bersama-sama** dari tiga sebaran populasi yang tidak Normal |
| 105–125' | Kuliah: galat baku, hukum akar n, dan implikasi praktisnya |
| 125–145' | Latihan: perencanaan ukuran sampel |
| 145–150' | Penutup, penjelasan Lab 09 |

#### Diskusi Kelas

1. Mengapa survei nasional cukup memakai 1.200 responden untuk populasi 280 juta jiwa, sedangkan survei kelas 40 mahasiswa terasa "terlalu sedikit"? (Petunjuk: perhatikan bahwa rumus SE **tidak mengandung N**.)
2. Sebuah tim ingin memperkecil ketidakpastian estimasi waktu respons menjadi separuhnya. Berapa kali lipat data yang harus dikumpulkan?
3. Kapan CLT **tidak** menolong? (Petunjuk: populasi dengan varians tak hingga, atau sampel yang tidak bebas.)

### Setelah Kelas (Mandiri — 180 menit)

1. Mengerjakan [Lab 09](../04-labs/lab-09-simulasi-teorema-limit-pusat.md).
2. Mengerjakan Latihan Soal Bab 8.
3. **Proyek:** menyelesaikan pembersihan data dan memulai analisis deskriptif.

---

## Penugasan

| Kode | Tugas | Bobot | Batas Waktu |
|------|-------|-------|-------------|
| T-09 | Laporan Lab 09 — Simulasi Teorema Limit Pusat | 1,92% | Sebelum kelas Minggu 10 |

---

## Rangkuman

1. **Ekspektasi** adalah rata-rata jangka panjang — berguna untuk menganggarkan, meskipun sering bukan nilai yang mungkin muncul.
2. **Linearitas ekspektasi** E[X+Y] = E[X]+E[Y] berlaku **selalu**, bahkan tanpa kebebasan. Varians hanya dapat dijumlahkan bila peubahnya **bebas**.
3. Ada **tiga sebaran yang berbeda**: sebaran populasi, sebaran satu sampel, dan **distribusi sampling**. Mencampuradukkannya adalah sumber kebingungan terbesar dalam statistika.
4. **Galat baku** SE = σ/√n mengukur sebaran **rata-rata sampel**, bukan sebaran data.
5. **Hukum akar n:** memperkecil SE menjadi separuh memerlukan empat kali lipat sampel. Ini menjelaskan mengapa survei besar tidak perlu sebesar yang diduga orang.
6. **Teorema Limit Pusat** menyatakan rata-rata sampel mendekati Normal untuk n besar, **berapa pun bentuk populasinya**.
7. Aturan n ≥ 30 adalah panduan, bukan hukum. Untuk populasi yang sangat menceng, n yang diperlukan lebih besar.
8. **Tanpa CLT, inferensi statistika klasik tidak mungkin dilakukan.** Semua yang akan dipelajari Minggu 10–14 berpijak pada teorema ini.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 4, 8. Pearson.
2. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.), Bab 7. Wiley.
3. Downey, A. B. (2014). *Think Stats* (2nd ed.), Bab 8. O'Reilly Media.
4. Ross, S. M. (2019). *A First Course in Probability* (10th ed.), Bab 8. Pearson.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
