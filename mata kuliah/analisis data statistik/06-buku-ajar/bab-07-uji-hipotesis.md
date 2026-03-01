# BAB 7: UJI HIPOTESIS

**Tri Aji Nugroho, S.T., M.T.**
Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-4.6 | Merumuskan hipotesis null (H0) dan hipotesis alternatif (H1) berdasarkan konteks permasalahan dengan benar | C4 |
| CPMK-4.7 | Memilih dan melaksanakan uji statistik yang tepat (z-test, one-sample t-test, two-sample t-test, paired t-test) menggunakan `scipy.stats` | C4 |
| CPMK-4.8 | Menginterpretasi p-value dengan benar dan menghindari tiga miskonsepsi utama dalam penarikan kesimpulan | C4 |
| CPMK-4.9 | Menganalisis dan membedakan Type I Error, Type II Error, serta menjelaskan konsep Statistical Power | C4 |
| CPMK-4.10 | Menghitung dan menginterpretasi effect size (Cohen's d) sebagai ukuran signifikansi praktis, serta membedakannya dari signifikansi statistik | C4 |

---

## 7.1 Pengantar: Mengapa Perlu Uji Hipotesis?

Pada Bab 6, kita telah mempelajari bagaimana **estimasi** memberikan kita interval kepercayaan untuk parameter populasi. Namun, seringkali pertanyaan dalam dunia nyata bukan sekadar "berapa nilainya?", melainkan **"apakah ada perbedaan yang nyata?"** atau **"apakah klaim ini didukung data?"**.

Inilah wilayah **uji hipotesis** (*hypothesis testing*) — salah satu alat paling fundamental dalam inferensi statistik.

**Contoh pertanyaan yang dijawab uji hipotesis:**
- Apakah rata-rata IPK lulusan Prodi Informatika UAI berbeda dari standar nasional?
- Apakah metode *flipped classroom* menghasilkan nilai ujian lebih tinggi dibanding ceramah tradisional?
- Apakah workshop Python meningkatkan skor *coding test* mahasiswa?
- Apakah aplikasi baru lebih cepat dari versi sebelumnya? (A/B Testing)

> "In God we trust; all others must bring data."
> — W. Edwards Deming

```
                    UJI HIPOTESIS
                         │
         ┌───────────────┼───────────────┐
         │               │               │
   KERANGKA         JENIS UJI      INTERPRETASI
   DASAR                │               │
   ├── H0          ┌────┼────┐      ├── p-value
   ├── H1       z-test  │  t-test   ├── Type I Error
   └── alpha          ┌─┴─┐        ├── Type II Error
                   1-samp  2-samp   ├── Power
                         ┌─┴─┐     └── Effect Size
                    Independent  Paired
```

---

## 7.2 Kerangka Dasar Uji Hipotesis

### 7.2.1 Analogi Pengadilan

Sebelum membahas formula, mari pahami konsep uji hipotesis melalui analogi yang lebih dekat: **sistem peradilan**.

| Pengadilan | Uji Hipotesis |
|------------|---------------|
| Terdakwa dianggap **tidak bersalah** sampai terbukti | H0 dianggap **benar** sampai ada bukti cukup |
| Jaksa harus memberikan **bukti kuat** | Data harus memberikan **bukti kuat** (p-value kecil) |
| "Beyond reasonable doubt" | Significance level (alpha, biasanya 0.05) |
| Verdict: **guilty** | Keputusan: **Tolak H0** |
| Verdict: **not guilty** (bukan "innocent"!) | Keputusan: **Gagal tolak H0** (bukan "H0 terbukti benar"!) |

Analogi ini memperlihatkan prinsip penting: kita **tidak pernah membuktikan H0 benar**. Kita hanya bisa menolak H0 atau gagal menolaknya.

### 7.2.2 Hipotesis Null (H0) dan Alternatif (H1)

**H0 — Hipotesis Null:**
- Representasi *status quo*: tidak ada efek, tidak ada perbedaan, tidak ada perubahan
- Selalu mengandung tanda kesetaraan: `=`, `≤`, atau `≥`
- Sesuatu yang ingin kita **tolak** jika data memberikan cukup bukti

**H1 — Hipotesis Alternatif:**
- Representasi klaim yang ingin dibuktikan: ada efek, ada perbedaan
- Tidak mengandung tanda `=`
- Menentukan apakah uji bersifat **one-tailed** atau **two-tailed**

**Contoh formulasi hipotesis:**

*Skenario:* Dosen menduga rata-rata waktu penyelesaian tugas mahasiswa Informatika UAI berbeda dari standar nasional 120 menit.

$$H_0: \mu = 120 \text{ menit}$$
$$H_1: \mu \neq 120 \text{ menit (two-tailed)}$$

*Skenario:* Tim pengembang aplikasi berharap versi baru lebih cepat dari versi lama (150 ms).

$$H_0: \mu \geq 150 \text{ ms}$$
$$H_1: \mu < 150 \text{ ms (left-tailed)}$$

### 7.2.3 Jenis Uji Berdasarkan H1

| Jenis Uji | H0 | H1 | Kapan Digunakan |
|-----------|----|----|-----------------|
| **Two-tailed** | $\mu = \mu_0$ | $\mu \neq \mu_0$ | Tidak tahu arah perbedaan |
| **Left-tailed** | $\mu \geq \mu_0$ | $\mu < \mu_0$ | Menduga nilai lebih kecil |
| **Right-tailed** | $\mu \leq \mu_0$ | $\mu > \mu_0$ | Menduga nilai lebih besar |

```
  TWO-TAILED              LEFT-TAILED             RIGHT-TAILED
  H1: mu != mu0           H1: mu < mu0            H1: mu > mu0

     /\                       /\                      /\
    /  \                     /  \                    /  \
   /    \                   /    \                  /    \
--/------\--             --/------\--            --/------\--
 |||    |||               |||                              |||
 Tolak  Tolak             Tolak                           Tolak
 H0     H0                H0                              H0
```

### 7.2.4 Significance Level (Alpha)

**Alpha (α)** adalah probabilitas maksimum yang kita toleransi untuk membuat kesalahan menolak H0 padahal H0 sebenarnya benar. Nilai alpha ditentukan **sebelum** pengumpulan data.

| Alpha | Artinya | Kapan Digunakan |
|-------|---------|-----------------|
| 0.10  | 10% toleransi kesalahan | Studi eksplorasi awal |
| **0.05** | **5% toleransi kesalahan** | **Standar paling umum** |
| 0.01  | 1% toleransi kesalahan | Uji kritis (medis, keamanan siber) |

---

## 7.3 Lima Langkah Uji Hipotesis

Semua uji hipotesis — tanpa terkecuali — mengikuti kerangka lima langkah berikut:

```
+---------------------------------------------------------------------------+
|                     LIMA LANGKAH UJI HIPOTESIS                           |
+---------------------------------------------------------------------------+
|                                                                           |
|  Langkah 1: FORMULASI                                                    |
|             Rumuskan H0 dan H1 secara eksplisit                          |
|                          |                                                |
|                          v                                                |
|  Langkah 2: PEMILIHAN UJI                                                |
|             Pilih uji statistik yang tepat, tentukan alpha               |
|                          |                                                |
|                          v                                                |
|  Langkah 3: PERHITUNGAN                                                  |
|             Hitung test statistic (z, t) dan p-value                     |
|                          |                                                |
|                          v                                                |
|  Langkah 4: KEPUTUSAN                                                    |
|             p-value < alpha  --> Tolak H0                                |
|             p-value >= alpha --> Gagal Tolak H0                          |
|                          |                                                |
|                          v                                                |
|  Langkah 5: INTERPRETASI                                                 |
|             Apa arti keputusan dalam konteks masalah nyata?              |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

## 7.4 z-Test

### 7.4.1 Kapan Digunakan?

z-test digunakan ketika **standard deviation populasi (σ) diketahui**. Kondisi ini jarang terjadi di dunia nyata, namun penting sebagai fondasi konseptual sebelum mempelajari t-test.

**Syarat penggunaan:**
- σ populasi diketahui, atau
- Ukuran sampel sangat besar (n ≥ 30) sehingga *s* ≈ σ (berkat Central Limit Theorem)

### 7.4.2 Formula z-Test

$$z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}$$

Di mana:
- $\bar{x}$ = mean sampel
- $\mu_0$ = mean hipotesis (dari H0)
- $\sigma$ = standard deviation **populasi** (diketahui)
- $n$ = ukuran sampel

**Distribusi sampling z mengikuti distribusi Normal standar:** $z \sim N(0, 1)$

### 7.4.3 Contoh: IPK Lulusan UAI vs Standar Nasional

**Konteks:** Data historis menunjukkan bahwa rata-rata IPK lulusan Informatika secara nasional adalah 3.20 dengan σ = 0.35. Apakah IPK lulusan Informatika UAI berbeda dari standar tersebut? (Data: 40 lulusan)

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# ============================================================
# z-TEST: IPK Lulusan UAI vs Standar Nasional
# ============================================================

np.random.seed(42)
ipk_sampel = np.random.normal(loc=3.30, scale=0.35, size=40)

# Langkah 1: Formulasi Hipotesis
mu_0  = 3.20   # standar nasional
sigma = 0.35   # sigma populasi diketahui
alpha = 0.05

print("=" * 55)
print("z-TEST: IPK Lulusan UAI vs Standar Nasional")
print("=" * 55)
print(f"\nLangkah 1: Formulasi Hipotesis")
print(f"  H0: mu = {mu_0} (IPK UAI = standar nasional)")
print(f"  H1: mu != {mu_0} (IPK UAI != standar nasional)")
print(f"  Uji: two-tailed, alpha = {alpha}")

# Langkah 2: Pilih Uji --> z-test (sigma diketahui)
print(f"\nLangkah 2: Pilih Uji")
print(f"  z-test karena sigma populasi diketahui = {sigma}")

# Langkah 3: Hitung
n     = len(ipk_sampel)
x_bar = ipk_sampel.mean()
se    = sigma / np.sqrt(n)
z_stat = (x_bar - mu_0) / se
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))  # two-tailed

print(f"\nLangkah 3: Perhitungan")
print(f"  n      = {n}")
print(f"  x_bar  = {x_bar:.4f}")
print(f"  SE     = sigma / sqrt(n) = {sigma} / {np.sqrt(n):.2f} = {se:.4f}")
print(f"  z      = (x_bar - mu0) / SE = {z_stat:.4f}")
print(f"  p-value = {p_value:.4f}")

# Langkah 4: Keputusan
print(f"\nLangkah 4: Keputusan")
if p_value < alpha:
    print(f"  p-value ({p_value:.4f}) < alpha ({alpha}) --> TOLAK H0")
else:
    print(f"  p-value ({p_value:.4f}) >= alpha ({alpha}) --> GAGAL TOLAK H0")

# Langkah 5: Interpretasi
print(f"\nLangkah 5: Interpretasi")
if p_value < alpha:
    print(f"  Pada tingkat signifikansi 5%, terdapat cukup bukti")
    print(f"  bahwa rata-rata IPK lulusan UAI berbeda dari standar nasional.")
    print(f"  Rata-rata sampel ({x_bar:.3f}) > standar ({mu_0}).")
else:
    print(f"  Pada tingkat signifikansi 5%, tidak cukup bukti")
    print(f"  bahwa IPK lulusan UAI berbeda dari standar nasional.")
```

---

## 7.5 One-Sample t-Test

### 7.5.1 Kapan Digunakan?

Situasi yang **jauh lebih umum** dari z-test: ketika σ populasi **tidak diketahui** dan kita menggunakan *s* (standard deviation sampel) sebagai estimasinya.

**Perbedaan utama dari z-test:**
- Menggunakan **distribusi t** (bukan distribusi Normal)
- Distribusi t lebih "gemuk" di ekor (*heavier tails*) — lebih konservatif
- Semakin besar n, distribusi t makin mendekati distribusi Normal

### 7.5.2 Formula t-Test

$$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}, \quad df = n - 1$$

Di mana:
- $s$ = standard deviation **sampel** (bukan populasi)
- $df$ = *degrees of freedom* = n − 1

### 7.5.3 Contoh: Waktu Respons IT Helpdesk UAI

**Konteks:** Standar layanan IT helpdesk UAI menetapkan waktu respons = 30 menit. Tim manajemen mencurigai bahwa waktu respons aktual melebihi standar. Diambil sampel 25 tiket layanan.

```python
# ============================================================
# ONE-SAMPLE t-TEST: Waktu Respons IT Helpdesk UAI
# ============================================================

np.random.seed(42)
waktu_respons = np.random.normal(loc=35, scale=8, size=25)  # menit

mu_0  = 30   # standar yang ditetapkan
alpha = 0.05

print("=" * 55)
print("ONE-SAMPLE t-TEST: Waktu Respons IT Helpdesk")
print("=" * 55)

# Langkah 1
print(f"\nLangkah 1: Formulasi Hipotesis")
print(f"  H0: mu = {mu_0} menit (sesuai standar)")
print(f"  H1: mu > {mu_0} menit (melebihi standar) [right-tailed]")

# Langkah 2-3: Hitung menggunakan scipy
t_stat, p_two = stats.ttest_1samp(waktu_respons, popmean=mu_0)
p_value = p_two / 2  # right-tailed: bagi dua jika t > 0

n     = len(waktu_respons)
x_bar = waktu_respons.mean()
s     = waktu_respons.std(ddof=1)
se    = s / np.sqrt(n)

print(f"\nLangkah 3: Statistik Sampel dan Hasil Uji")
print(f"  n        = {n}")
print(f"  x_bar    = {x_bar:.2f} menit")
print(f"  s        = {s:.2f} menit")
print(f"  SE       = s / sqrt(n) = {se:.2f} menit")
print(f"  t        = {t_stat:.4f}")
print(f"  df       = {n - 1}")
print(f"  p-value (right-tailed) = {p_value:.4f}")

# Langkah 4-5
print(f"\nLangkah 4: Keputusan")
if p_value < alpha and t_stat > 0:
    print(f"  p-value ({p_value:.4f}) < alpha ({alpha}) --> TOLAK H0")
    print(f"\nLangkah 5: Interpretasi")
    print(f"  Waktu respons IT helpdesk UAI secara signifikan MELEBIHI")
    print(f"  standar {mu_0} menit. Rata-rata aktual = {x_bar:.1f} menit.")
    print(f"  Perlu tindakan perbaikan layanan.")
else:
    print(f"  GAGAL TOLAK H0")
    print(f"  Tidak cukup bukti bahwa waktu respons melebihi standar.")

# Hitung Confidence Interval (informasi tambahan)
t_crit = stats.t.ppf(1 - alpha / 2, df=n - 1)
ci = (x_bar - t_crit * se, x_bar + t_crit * se)
print(f"\n  95% Confidence Interval: [{ci[0]:.2f}, {ci[1]:.2f}] menit")
```

---

## 7.6 Two-Sample t-Test

### 7.6.1 Independent (Unpaired) Two-Sample t-Test

**Kapan digunakan:** Membandingkan mean dari **dua kelompok berbeda** yang tidak saling terkait (independen).

**Contoh konteks:**
- Nilai ujian Kelas A (metode tradisional) vs Kelas B (metode *active learning*)
- Lama loading website sebelum vs sesudah optimasi (dua server berbeda)
- IPK mahasiswa penerima beasiswa vs bukan penerima beasiswa

**Formula (Welch's t-test — lebih aman, tidak mengasumsikan varians sama):**

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}$$

```python
# ============================================================
# INDEPENDENT TWO-SAMPLE t-TEST
# Nilai Ujian: Kelas A (Tradisional) vs Kelas B (Active Learning)
# ============================================================

np.random.seed(42)
kelas_a = np.random.normal(loc=72, scale=9, size=35)   # tradisional
kelas_b = np.random.normal(loc=78, scale=10, size=32)  # active learning

alpha = 0.05

print("=" * 60)
print("INDEPENDENT TWO-SAMPLE t-TEST")
print("Nilai Ujian: Kelas A vs Kelas B")
print("=" * 60)

# Langkah 1: Hipotesis
print(f"\nLangkah 1: Hipotesis")
print(f"  H0: mu_A = mu_B (tidak ada perbedaan nilai antar kelas)")
print(f"  H1: mu_A != mu_B (ada perbedaan nilai) [two-tailed]")

# Langkah 2: Statistik deskriptif
print(f"\nLangkah 2: Statistik Deskriptif")
print(f"  Kelas A (Tradisional):    n={len(kelas_a)}, "
      f"mean={kelas_a.mean():.2f}, std={kelas_a.std(ddof=1):.2f}")
print(f"  Kelas B (Active Learn):   n={len(kelas_b)}, "
      f"mean={kelas_b.mean():.2f}, std={kelas_b.std(ddof=1):.2f}")
print(f"  Perbedaan mean: {kelas_b.mean() - kelas_a.mean():.2f} poin")

# Langkah 3: Periksa homogenitas varians (Levene's Test)
stat_lev, p_lev = stats.levene(kelas_a, kelas_b)
equal_var = p_lev > 0.05
print(f"\nLangkah 3: Uji Varians (Levene's Test)")
print(f"  stat={stat_lev:.4f}, p={p_lev:.4f} "
      f"--> Varians {'SAMA' if equal_var else 'BERBEDA'}")

# Langkah 4: t-test (Welch jika varians berbeda, Student jika sama)
t_stat_ind, p_value_ind = stats.ttest_ind(kelas_a, kelas_b,
                                           equal_var=equal_var)
metode = "Student" if equal_var else "Welch"
print(f"\nLangkah 4: Hasil Uji ({metode}'s t-test)")
print(f"  t-statistic = {t_stat_ind:.4f}")
print(f"  p-value     = {p_value_ind:.4f}")

# Langkah 5
print(f"\nLangkah 5: Keputusan dan Interpretasi")
if p_value_ind < alpha:
    print(f"  p-value ({p_value_ind:.4f}) < alpha ({alpha}) --> TOLAK H0")
    print(f"  Terdapat perbedaan signifikan antara nilai Kelas A dan B.")
else:
    print(f"  GAGAL TOLAK H0 --> Tidak cukup bukti adanya perbedaan.")
```

### 7.6.2 Paired t-Test

**Kapan digunakan:** Membandingkan **dua pengukuran** dari **subjek yang sama**. Pengukuran berpasangan (*paired* atau *dependent*).

**Contoh konteks:**
- Skor *coding test* mahasiswa **sebelum** dan **sesudah** workshop Python
- Waktu pengerjaan soal **sebelum** dan **sesudah** pelatihan
- Kepuasan pengguna **sebelum** dan **sesudah** desain ulang antarmuka (*UI redesign*)

**Inti paired t-test:** Hitung selisih $d_i = x_{2i} - x_{1i}$ untuk setiap pasang, lalu lakukan one-sample t-test pada selisih tersebut terhadap H0: $\mu_d = 0$.

$$t = \frac{\bar{d}}{s_d / \sqrt{n}}, \quad df = n - 1$$

```python
# ============================================================
# PAIRED t-TEST
# Skor Coding Test: Sebelum vs Sesudah Workshop Python
# ============================================================

np.random.seed(42)
n_mahasiswa    = 25
skor_sebelum   = np.random.normal(loc=60, scale=10, size=n_mahasiswa)
peningkatan    = np.random.normal(loc=7, scale=5, size=n_mahasiswa)
skor_sesudah   = skor_sebelum + peningkatan

alpha   = 0.05
selisih = skor_sesudah - skor_sebelum  # d_i

print("=" * 60)
print("PAIRED t-TEST")
print("Skor Coding Test: Sebelum vs Sesudah Workshop Python")
print("=" * 60)

# Langkah 1: Hipotesis
print(f"\nLangkah 1: Hipotesis")
print(f"  H0: mu_d = 0 (workshop tidak meningkatkan skor)")
print(f"  H1: mu_d > 0 (skor meningkat setelah workshop) [right-tailed]")
print(f"  di mana d = sesudah - sebelum")

# Langkah 2: Deskriptif
print(f"\nLangkah 2: Statistik Deskriptif")
print(f"  Sebelum  : mean = {skor_sebelum.mean():.2f}, "
      f"std = {skor_sebelum.std(ddof=1):.2f}")
print(f"  Sesudah  : mean = {skor_sesudah.mean():.2f}, "
      f"std = {skor_sesudah.std(ddof=1):.2f}")
print(f"  Selisih  : mean = {selisih.mean():.2f}, "
      f"std = {selisih.std(ddof=1):.2f}")

# Langkah 3: Hitung
t_stat_p, p_two_p = stats.ttest_rel(skor_sesudah, skor_sebelum)
p_value_p = p_two_p / 2  # one-tailed (right)

print(f"\nLangkah 3: Hasil Uji (Paired t-test, one-tailed)")
print(f"  t-statistic = {t_stat_p:.4f}")
print(f"  df          = {n_mahasiswa - 1}")
print(f"  p-value     = {p_value_p:.4f}")

# Langkah 4-5
print(f"\nLangkah 4: Keputusan")
if p_value_p < alpha and t_stat_p > 0:
    print(f"  p-value ({p_value_p:.4f}) < alpha ({alpha}) --> TOLAK H0")
    print(f"\nLangkah 5: Interpretasi")
    print(f"  Workshop Python SECARA SIGNIFIKAN meningkatkan skor.")
    print(f"  Peningkatan rata-rata: {selisih.mean():.2f} poin.")
    print(f"  (dari {skor_sebelum.mean():.1f} menjadi {skor_sesudah.mean():.1f})")
else:
    print(f"  GAGAL TOLAK H0")

# Visualisasi perubahan individual
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

ax = axes[0]
for i in range(n_mahasiswa):
    warna = 'green' if selisih[i] > 0 else 'red'
    ax.plot([0, 1], [skor_sebelum[i], skor_sesudah[i]],
            'o-', color=warna, alpha=0.4, markersize=4)
ax.set_xticks([0, 1])
ax.set_xticklabels(['Sebelum', 'Sesudah'], fontsize=12)
ax.set_ylabel('Skor Coding Test')
ax.set_title('Perubahan Skor Individual\n(Hijau = naik, Merah = turun)')
ax.grid(alpha=0.3)

ax = axes[1]
ax.hist(selisih, bins=10, color='steelblue', alpha=0.7, edgecolor='black')
ax.axvline(0, color='red', linestyle='--', linewidth=2, label='H0: mu_d = 0')
ax.axvline(selisih.mean(), color='green', linestyle='-', linewidth=2,
           label=f'Mean selisih = {selisih.mean():.2f}')
ax.set_xlabel('Selisih Skor (Sesudah - Sebelum)')
ax.set_ylabel('Frekuensi')
ax.set_title(f'Distribusi Selisih\n(t = {t_stat_p:.2f}, p = {p_value_p:.4f})')
ax.legend()
ax.grid(alpha=0.3)

plt.suptitle('Paired t-Test: Efektivitas Workshop Python di UAI',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()
```

### 7.6.3 Panduan Memilih Jenis Uji

```
Berapa kelompok yang terlibat?
│
├── SATU kelompok vs nilai referensi
│   ├── sigma populasi DIKETAHUI  --> z-test
│   │   scipy: stats.norm.cdf() atau statsmodels ztest
│   └── sigma populasi TIDAK diketahui --> ONE-SAMPLE t-test
│       scipy: stats.ttest_1samp(data, popmean=mu0)
│
└── DUA kelompok
    ├── Subjek SAMA (before-after, pengukuran berulang)
    │   --> PAIRED t-test
    │   scipy: stats.ttest_rel(sesudah, sebelum)
    │
    └── Subjek BERBEDA (dua grup independen)
        --> INDEPENDENT t-test (gunakan Welch, equal_var=False)
        scipy: stats.ttest_ind(grup1, grup2, equal_var=False)

(3+ kelompok --> ANOVA, dibahas di Bab 11)
```

---

## 7.7 Interpretasi p-Value yang Benar

### 7.7.1 Definisi p-Value

> **p-value** adalah probabilitas mendapatkan hasil **seektrem atau lebih ekstrem** dari yang kita amati, **apabila H0 benar**.

Secara intuitif:
- **p-value kecil** → data kita "sangat aneh" jika H0 benar → bukti kuat melawan H0
- **p-value besar** → data kita "wajar saja" jika H0 benar → tidak cukup bukti untuk menolak H0

### 7.7.2 Tiga Miskonsepsi yang Harus Dihindari

| No. | Miskonsepsi (SALAH) | Koreksi (BENAR) |
|-----|---------------------|-----------------|
| 1 | "p = 0.03 berarti ada 3% peluang H0 benar" | p-value **bukan** probabilitas H0 benar. Untuk itu diperlukan Bayesian statistics. p-value = P(data seekstrem ini \| H0 benar), bukan P(H0 benar \| data). |
| 2 | "p = 0.07, maka H0 terbukti benar" | Gagal tolak H0 **tidak berarti** H0 terbukti. Artinya: tidak cukup bukti untuk menolaknya. Seperti vonis "tidak bersalah" — bukan berarti "pasti tidak bersalah". |
| 3 | "p = 0.001 berarti efeknya sangat besar" | p-value kecil hanya menunjukkan **bukti kuat** melawan H0. Dengan n = 1.000.000, perbedaan mean 0.01 pun bisa menghasilkan p < 0.001, padahal efeknya tidak bermakna secara praktis. |

### 7.7.3 Panduan Interpretasi Kekuatan Bukti

| p-value | Kekuatan Bukti Melawan H0 |
|---------|---------------------------|
| > 0.10  | Tidak ada atau sangat lemah |
| 0.05 – 0.10 | Lemah (marginal) |
| 0.01 – 0.05 | Moderat |
| 0.001 – 0.01 | Kuat |
| < 0.001 | Sangat kuat |

**Penting:** Ambang batas 0.05 adalah **konvensi**, bukan aturan absolut. p = 0.049 dan p = 0.051 secara praktis tidak berbeda jauh. Konteks dan ukuran efek jauh lebih penting dari sekadar menyeberangi ambang batas.

---

## 7.8 Type I Error, Type II Error, dan Statistical Power

### 7.8.1 Matriks Keputusan

Dalam uji hipotesis, selalu ada kemungkinan salah. Ada dua jenis kesalahan yang mungkin terjadi:

|  | **H0 Benar** (realita) | **H0 Salah** (realita) |
|--|------------------------|------------------------|
| **Gagal Tolak H0** | Keputusan BENAR ✓ — probabilitas = 1 − α | **Type II Error** (β) |
| **Tolak H0** | **Type I Error** (α) | Keputusan BENAR ✓ — probabilitas = 1 − β = **Power** |

### 7.8.2 Penjelasan Detail

**Type I Error (α) — False Positive:**
- Menolak H0 padahal H0 sebenarnya benar
- Analogi: "menghukum orang yang tidak bersalah"
- Contoh: Menyimpulkan obat baru efektif, padahal sebenarnya tidak
- Dikendalikan langsung oleh pemilihan nilai alpha

**Type II Error (β) — False Negative:**
- Gagal menolak H0 padahal H0 sebenarnya salah
- Analogi: "membebaskan orang yang bersalah"
- Contoh: Menyimpulkan obat tidak efektif, padahal sebenarnya efektif
- Lebih sulit dikendalikan; bergantung pada ukuran sampel dan efek

**Statistical Power (1 − β):**
- Probabilitas **mendeteksi efek nyata** ketika efek itu memang ada
- Target power yang baik: ≥ 0.80 (80%)
- Digunakan dalam **power analysis** sebelum penelitian untuk menentukan ukuran sampel minimum

### 7.8.3 Faktor yang Mempengaruhi Power

```
Power meningkat jika:
├── Ukuran sampel (n) lebih BESAR         --> Pengumpulan data lebih banyak
├── Effect size lebih BESAR               --> Perbedaan nyata lebih mudah terdeteksi
├── Significance level (alpha) lebih BESAR --> Trade-off dengan Type I Error!
└── Variabilitas data lebih KECIL         --> Kontrol kondisi eksperimen
```

```python
# ============================================================
# VISUALISASI: Type I Error, Type II Error, dan Power
# ============================================================

fig, ax = plt.subplots(figsize=(12, 6))

x = np.linspace(-4, 8, 1000)
h0_dist = stats.norm(loc=0, scale=1)   # distribusi jika H0 benar
h1_dist = stats.norm(loc=3, scale=1)   # distribusi jika H1 benar (efek = 3)

# Plot kedua distribusi
ax.plot(x, h0_dist.pdf(x), 'b-', linewidth=2,
        label='Distribusi jika H0 benar (mu = 0)')
ax.plot(x, h1_dist.pdf(x), 'r-', linewidth=2,
        label='Distribusi jika H1 benar (mu = 3)')

# Critical value (alpha = 0.05, one-tailed)
z_crit = stats.norm.ppf(0.95)

# Warnai tiga area
x_alpha = np.linspace(z_crit, 5.5, 200)
x_beta  = np.linspace(-4, z_crit, 200)
x_power = np.linspace(z_crit, 8, 200)

ax.fill_between(x_alpha, h0_dist.pdf(x_alpha), color='blue', alpha=0.35,
                label=f'Type I Error (alpha = {1-h0_dist.cdf(z_crit):.3f})')
ax.fill_between(x_beta, h1_dist.pdf(x_beta), color='red', alpha=0.35,
                label=f'Type II Error (beta = {h1_dist.cdf(z_crit):.3f})')
ax.fill_between(x_power, h1_dist.pdf(x_power), color='green', alpha=0.35,
                label=f'Power (1-beta = {1-h1_dist.cdf(z_crit):.3f})')

ax.axvline(z_crit, color='black', linestyle='--', linewidth=1.5,
           label=f'Critical value = {z_crit:.2f}')

ax.set_xlabel('Test Statistic', fontsize=12)
ax.set_ylabel('Density', fontsize=12)
ax.set_title('Visualisasi Type I Error, Type II Error, dan Power',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=9, loc='upper right')
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 7.9 Effect Size: Cohen's d

### 7.9.1 Mengapa Effect Size Penting?

**Masalah dengan signifikansi statistik semata:**

Dengan ukuran sampel yang sangat besar, perbedaan yang secara praktis tidak berarti pun bisa menghasilkan p-value kecil. Sebaliknya, dengan sampel kecil, efek yang secara praktis besar mungkin tidak "signifikan" secara statistik.

| Skenario | Signifikan Statistik? | Effect Size | Bermakna Praktis? |
|----------|----------------------|-------------|-------------------|
| n = 500.000, perbedaan mean 0.5 poin | Ya (p < 0.001) | d = 0.04 (sangat kecil) | **Tidak** |
| n = 20, perbedaan mean 15 poin | Mungkin tidak (p = 0.08) | d = 0.80 (besar) | **Ya!** |
| n = 60, perbedaan mean 8 poin | Ya (p = 0.02) | d = 0.55 (sedang) | **Ya** |

**Pesan utama:** Selalu laporkan **keduanya** — p-value DAN effect size!

### 7.9.2 Formula Cohen's d

**Untuk one-sample t-test:**

$$d = \frac{\bar{x} - \mu_0}{s}$$

**Untuk independent two-sample t-test:**

$$d = \frac{\bar{x}_1 - \bar{x}_2}{s_{\text{pooled}}}, \quad s_{\text{pooled}} = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}$$

**Untuk paired t-test:**

$$d = \frac{\bar{d}}{s_d}$$

### 7.9.3 Interpretasi Cohen's d

| |d| | Interpretasi |
|-----|-------------|
| < 0.2 | Negligible — sangat kecil, hampir tidak terdeteksi |
| 0.2 – 0.49 | Small — kecil |
| 0.5 – 0.79 | Medium — sedang |
| ≥ 0.8 | Large — besar |
| ≥ 1.0 | Very Large — sangat besar |

### 7.9.4 Implementasi Python

```python
# ============================================================
# EFFECT SIZE: Cohen's d
# ============================================================

def cohens_d_one_sample(data, mu_0):
    """Cohen's d untuk one-sample t-test."""
    return (data.mean() - mu_0) / data.std(ddof=1)

def cohens_d_independent(group1, group2):
    """Cohen's d untuk independent t-test (pooled std)."""
    n1, n2 = len(group1), len(group2)
    s1, s2 = group1.std(ddof=1), group2.std(ddof=1)
    s_pooled = np.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
    return (group1.mean() - group2.mean()) / s_pooled

def cohens_d_paired(before, after):
    """Cohen's d untuk paired t-test."""
    diff = after - before
    return diff.mean() / diff.std(ddof=1)

def interpretasi_d(d):
    """Interpretasi nilai Cohen's d."""
    d_abs = abs(d)
    if d_abs < 0.2:
        return "Negligible (sangat kecil)"
    elif d_abs < 0.5:
        return "Small (kecil)"
    elif d_abs < 0.8:
        return "Medium (sedang)"
    else:
        return "Large (besar)"

# Contoh: Kelas A vs Kelas B
d_ind = cohens_d_independent(kelas_a, kelas_b)
print(f"Cohen's d (Kelas B vs Kelas A) = {abs(d_ind):.3f}")
print(f"Interpretasi: Efek {interpretasi_d(d_ind)}")
print()

# Laporan lengkap (format APA-like)
print("Laporan Lengkap (APA Style):")
print(f"  t({len(kelas_a) + len(kelas_b) - 2}) = {t_stat_ind:.2f}, "
      f"p = {p_value_ind:.4f}, d = {abs(d_ind):.2f}")
print(f"  Kelas A: M = {kelas_a.mean():.1f}, SD = {kelas_a.std(ddof=1):.1f}")
print(f"  Kelas B: M = {kelas_b.mean():.1f}, SD = {kelas_b.std(ddof=1):.1f}")
print(f"  Perbedaan mean = {kelas_b.mean() - kelas_a.mean():.1f} poin "
      f"(efek {interpretasi_d(d_ind).lower()})")
```

---

## 7.10 Studi Kasus: A/B Testing Antarmuka Aplikasi Akademik UAI

### 7.10.1 Konteks

Tim pengembang Sistem Informasi Akademik (SIAKAD) UAI merancang ulang antarmuka (*UI redesign*). Untuk mengevaluasi efektivitas desain baru, mereka melakukan **A/B Testing**:

- **Versi A (Kontrol):** Antarmuka lama
- **Versi B (Treatment):** Antarmuka baru dengan desain yang lebih modern

Metrik yang diukur: **waktu yang dibutuhkan mahasiswa untuk menyelesaikan tugas tertentu** (dalam detik), dan **skor kepuasan** pada skala 1–10.

### 7.10.2 Analisis Lengkap

```python
# ============================================================
# STUDI KASUS: A/B Testing SIAKAD UAI
# ============================================================

np.random.seed(2024)

# Data A/B Testing
# Waktu penyelesaian tugas (detik) -- lebih rendah = lebih baik
versi_a_waktu = np.array([85, 92, 78, 105, 88, 76, 95, 83, 90, 87,
                           102, 79, 91, 84, 96, 80, 88, 93, 77, 86,
                           99, 81, 94, 89, 82, 97, 75, 90, 85, 93])  # n=30
versi_b_waktu = np.array([72, 68, 75, 80, 65, 71, 77, 69, 74, 70,
                           83, 66, 73, 67, 78, 64, 71, 76, 68, 73,
                           81, 65, 74, 70, 67, 79, 63, 72, 69, 75])  # n=30

# Skor kepuasan pengguna (1-10)
skor_a = np.array([6, 7, 5, 6, 8, 6, 7, 5, 7, 6,
                   5, 7, 6, 8, 5, 7, 6, 5, 7, 6,
                   7, 6, 5, 8, 6, 7, 5, 6, 7, 6])   # n=30
skor_b = np.array([8, 9, 7, 8, 9, 8, 9, 8, 9, 7,
                   8, 9, 8, 9, 7, 8, 9, 8, 9, 8,
                   8, 9, 7, 9, 8, 8, 9, 7, 8, 9])   # n=30

alpha = 0.05

print("=" * 65)
print("A/B TESTING: SIAKAD UAI — Antarmuka Lama vs Antarmuka Baru")
print("=" * 65)

# ---- UJI 1: Waktu Penyelesaian Tugas ----
print("\n--- UJI 1: Waktu Penyelesaian Tugas (detik) ---")
print(f"Versi A (Lama): M = {versi_a_waktu.mean():.2f}, "
      f"SD = {versi_a_waktu.std(ddof=1):.2f}")
print(f"Versi B (Baru): M = {versi_b_waktu.mean():.2f}, "
      f"SD = {versi_b_waktu.std(ddof=1):.2f}")

# Hipotesis: Apakah versi B lebih cepat? (left-tailed: mu_B < mu_A)
print(f"\nH0: mu_A <= mu_B (versi baru tidak lebih cepat)")
print(f"H1: mu_A > mu_B  (versi lama lebih lambat) [right-tailed A - B]")

t_w, p_w_two = stats.ttest_ind(versi_a_waktu, versi_b_waktu,
                                equal_var=False)
# H1: A lebih besar dari B --> right-tailed pada (A - B)
p_w = p_w_two / 2 if t_w > 0 else 1

d_w = cohens_d_independent(versi_a_waktu, versi_b_waktu)

print(f"\nHasil: t = {t_w:.4f}, p = {p_w:.4f}, d = {abs(d_w):.3f}")
print(f"Efek: {interpretasi_d(d_w)}")
if p_w < alpha and t_w > 0:
    print(f"--> TOLAK H0: Versi B (baru) SECARA SIGNIFIKAN lebih cepat.")
    print(f"    Penghematan waktu rata-rata: "
          f"{versi_a_waktu.mean() - versi_b_waktu.mean():.1f} detik.")
else:
    print(f"--> GAGAL TOLAK H0")

# ---- UJI 2: Skor Kepuasan Pengguna ----
print("\n--- UJI 2: Skor Kepuasan Pengguna (1-10) ---")
print(f"Versi A (Lama): M = {skor_a.mean():.2f}, "
      f"SD = {skor_a.std(ddof=1):.2f}")
print(f"Versi B (Baru): M = {skor_b.mean():.2f}, "
      f"SD = {skor_b.std(ddof=1):.2f}")

t_s, p_s = stats.ttest_ind(skor_b, skor_a, equal_var=False)
d_s = cohens_d_independent(skor_b, skor_a)

print(f"\nH0: mu_B = mu_A (kepuasan sama)")
print(f"H1: mu_B > mu_A (versi baru lebih memuaskan) [right-tailed]")

p_s_one = p_s / 2 if t_s > 0 else 1
print(f"\nHasil: t = {t_s:.4f}, p = {p_s_one:.4f}, d = {d_s:.3f}")
print(f"Efek: {interpretasi_d(d_s)}")
if p_s_one < alpha and t_s > 0:
    print(f"--> TOLAK H0: Kepuasan pengguna SECARA SIGNIFIKAN lebih tinggi")
    print(f"    pada antarmuka baru (M = {skor_b.mean():.2f} vs M = {skor_a.mean():.2f}).")
else:
    print(f"--> GAGAL TOLAK H0")

# ---- Visualisasi ----
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Waktu penyelesaian
ax = axes[0]
ax.boxplot([versi_a_waktu, versi_b_waktu],
           labels=['Versi A\n(Lama)', 'Versi B\n(Baru)'],
           patch_artist=True,
           boxprops=dict(facecolor='lightblue', alpha=0.7))
ax.set_ylabel('Waktu Penyelesaian (detik)', fontsize=11)
ax.set_title(f'Waktu Penyelesaian Tugas\n'
             f'(t = {t_w:.2f}, p = {p_w:.4f}, d = {abs(d_w):.2f})',
             fontsize=11, fontweight='bold')
ax.grid(alpha=0.3)

# Plot 2: Skor kepuasan
ax = axes[1]
ax.hist(skor_a, bins=8, alpha=0.6, label=f'Versi A (M={skor_a.mean():.1f})',
        color='coral', edgecolor='black')
ax.hist(skor_b, bins=8, alpha=0.6, label=f'Versi B (M={skor_b.mean():.1f})',
        color='steelblue', edgecolor='black')
ax.axvline(skor_a.mean(), color='coral', linestyle='--', linewidth=2)
ax.axvline(skor_b.mean(), color='steelblue', linestyle='--', linewidth=2)
ax.set_xlabel('Skor Kepuasan (1-10)', fontsize=11)
ax.set_ylabel('Frekuensi', fontsize=11)
ax.set_title(f'Skor Kepuasan Pengguna\n'
             f'(t = {t_s:.2f}, p = {p_s_one:.4f}, d = {d_s:.2f})',
             fontsize=11, fontweight='bold')
ax.legend()
ax.grid(alpha=0.3)

plt.suptitle('A/B Testing: SIAKAD UAI — Antarmuka Lama vs Baru',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()

# ---- Kesimpulan Managerial ----
print("\n" + "=" * 65)
print("REKOMENDASI UNTUK TIM PENGEMBANG:")
print("=" * 65)
print("""
Berdasarkan A/B Testing dengan 30 pengguna per versi:

1. WAKTU PENYELESAIAN: Versi B (baru) secara signifikan lebih cepat.
   Rata-rata penghematan waktu nyata secara praktis (effect size besar).

2. KEPUASAN PENGGUNA: Versi B mendapat skor kepuasan lebih tinggi
   dengan effect size yang sangat besar.

REKOMENDASI: Luncurkan Versi B (antarmuka baru) ke semua pengguna.
""")
```

---

## 7.11 Memeriksa Asumsi: Uji Normalitas

Semua uji t mengasumsikan data mendekati distribusi normal (atau n cukup besar untuk mengandalkan Central Limit Theorem). Sebelum uji hipotesis, periksa asumsi ini.

```python
# ============================================================
# UJI NORMALITAS: Shapiro-Wilk Test + QQ-Plot
# ============================================================

print("UJI NORMALITAS (Shapiro-Wilk)")
print("H0: Data berdistribusi normal")
print("H1: Data TIDAK berdistribusi normal")
print("-" * 50)

datasets_uji = {
    'Waktu Respons Helpdesk'  : waktu_respons,
    'Nilai Kelas A'           : kelas_a,
    'Nilai Kelas B'           : kelas_b,
    'Skor Sebelum Workshop'   : skor_sebelum,
    'Skor Sesudah Workshop'   : skor_sesudah,
    'Selisih Skor Workshop'   : selisih,
}

for nama, data in datasets_uji.items():
    stat_sw, p_sw = stats.shapiro(data)
    status = "Normal" if p_sw > 0.05 else "TIDAK Normal"
    print(f"  {nama:<30}: W = {stat_sw:.4f}, p = {p_sw:.4f} --> {status}")

print("\nCatatan:")
print("  - Jika p > 0.05: asumsi normalitas terpenuhi")
print("  - Jika p <= 0.05: asumsi normalitas dilanggar")
print("  - Untuk n >= 30, t-test cukup robust terhadap pelanggaran")
print("    normalitas ringan (berkat Central Limit Theorem)")
print("  - Jika normalitas sangat tidak terpenuhi, gunakan uji non-parametrik")
print("    (Wilcoxon rank-sum, Mann-Whitney U) -- dibahas di Bab 12")

# QQ-Plot visual
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
for idx, (nama, data) in enumerate(datasets_uji.items()):
    ax = axes[idx // 3, idx % 3]
    stats.probplot(data, dist='norm', plot=ax)
    ax.set_title(f'QQ-Plot: {nama}', fontsize=10, fontweight='bold')

plt.suptitle('QQ-Plot untuk Pemeriksaan Normalitas',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

## 7.12 AI Corner

### Menggunakan AI untuk Uji Hipotesis

Kecerdasan buatan generatif (seperti ChatGPT, Claude, Gemini) dapat sangat membantu dalam uji hipotesis — dari formulasi hingga interpretasi. Namun, AI juga memiliki kelemahan khas dalam topik ini.

**Prompt yang Efektif — Formulasi Hipotesis:**
> "Saya ingin meneliti apakah mahasiswa yang menggunakan aplikasi belajar berbasis AI mendapat IPK lebih tinggi dibanding yang tidak. Bantu saya merumuskan H0 dan H1, pilih uji statistik yang tepat, dan tentukan alpha yang sesuai."

**Prompt yang Efektif — Interpretasi Hasil:**
> "Hasil uji statistik saya: t(58) = 2.34, p = 0.023, Cohen's d = 0.48. Tolong bantu saya menginterpretasi hasil ini. Apakah hasilnya signifikan secara statistik? Apakah efeknya bermakna secara praktis?"

**Prompt yang Efektif — Debugging Miskonsepsi:**
> "Rekan saya berargumen: 'p-value = 0.03 berarti ada 3% kemungkinan hipotesis null kita benar.' Apakah pernyataan ini benar? Kalau salah, apa interpretasi yang tepat?"

**Prompt yang Efektif — Kode Python:**
> "Bantu saya menulis kode Python menggunakan scipy.stats untuk melakukan paired t-test pada data sebelum-sesudah pelatihan. Sertakan pemeriksaan asumsi normalitas dengan Shapiro-Wilk dan hitung Cohen's d."

### Peringatan: Kelemahan AI dalam Uji Hipotesis

Berdasarkan berbagai penelitian tentang LLM dan statistika, AI cenderung membuat kesalahan pada:

1. **Interpretasi p-value** — AI sering mengartikan p-value sebagai probabilitas H0 benar (miskonsepsi #1). Selalu verifikasi interpretasi AI.
2. **Pemilihan one-tailed vs two-tailed** — AI kadang tidak konsisten dalam memberikan rekomendasi.
3. **Asumsi yang terlupakan** — AI sering langsung menjalankan t-test tanpa memeriksa asumsi normalitas dan homogenitas varians.
4. **Konteks praktis** — AI baik di statistik, tapi kurang memahami konteks domain spesifik (misalnya pendidikan, kesehatan).

**Praktik terbaik:** Gunakan AI sebagai *thought partner* dan untuk menghasilkan kode awal, namun selalu verifikasi output dengan pemahaman konseptual Anda.

---

## Rangkuman Bab 7

| Konsep | Poin Utama |
|--------|-----------|
| **H0 dan H1** | H0 = status quo (selalu ada tanda =). H1 = klaim yang ingin dibuktikan. Kita tidak pernah "membuktikan H0 benar", hanya "tolak" atau "gagal tolak" H0. |
| **Lima Langkah** | Formulasi → Pilih uji → Hitung → Keputusan (p < α → tolak H0) → Interpretasi kontekstual |
| **z-test vs t-test** | z-test: σ populasi diketahui (jarang). t-test: σ tidak diketahui, gunakan s sampel. Distribusi t lebih konservatif (ekor lebih tebal). |
| **Jenis t-test** | One-sample (1 grup vs nilai referensi), Independent (2 grup berbeda), Paired (subjek yang sama, before-after) |
| **p-value** | P(data seekstrem ini \| H0 benar) — BUKAN probabilitas H0 benar. p kecil = bukti kuat melawan H0. p > 0.05 bukan berarti H0 terbukti. |
| **Type I & Type II Error** | Type I (α): menolak H0 yang benar. Type II (β): gagal menolak H0 yang salah. Power = 1−β: kemampuan mendeteksi efek nyata. |
| **Cohen's d** | Ukuran besar efek: d < 0.2 (negligible), 0.2–0.5 (small), 0.5–0.8 (medium), ≥ 0.8 (large). Selalu laporkan bersamaan dengan p-value. |
| **Signifikansi Statistik vs Praktis** | p kecil ≠ efek besar. Dengan n sangat besar, perbedaan kecil pun bisa "signifikan" secara statistik. Effect size mengukur makna praktis. |

---

## Latihan Soal

### Soal Dasar (C1–C2)

**1.** Jelaskan perbedaan antara H0 (hipotesis null) dan H1 (hipotesis alternatif). Mengapa kita tidak pernah "menerima H0" tetapi hanya "gagal menolak H0"?

**2.** Sebuah penelitian menghasilkan p-value = 0.03 dengan alpha = 0.05. Manakah pernyataan yang BENAR?
   - a) Ada 3% kemungkinan H0 benar
   - b) Tolak H0 karena p < alpha
   - c) H1 terbukti benar dengan 97% kepastian
   - d) Tidak ada cukup bukti untuk menolak H0

**3.** Tentukan jenis uji (one-tailed kiri, one-tailed kanan, atau two-tailed) untuk masing-masing H1 berikut:
   - a) H1: μ ≠ 75
   - b) H1: μ > 80
   - c) H1: μ < 3.5

**4.** Sebutkan tiga faktor yang dapat meningkatkan *statistical power*. Jelaskan mengapa masing-masing faktor tersebut berpengaruh.

**5.** Jelaskan perbedaan antara Type I Error dan Type II Error dengan menggunakan analogi di bidang keamanan siber (misal: sistem deteksi intrusi).

**6.** Kapan sebaiknya menggunakan paired t-test dan kapan menggunakan independent two-sample t-test? Berikan masing-masing satu contoh konteks di bidang informatika.

### Soal Menengah (C2–C3)

**7.** Data waktu respons server (dalam ms) diambil dari 20 pengujian: rata-rata = 245 ms, standard deviation = 32 ms. Standar SLA perusahaan menetapkan waktu respons ≤ 240 ms. Dengan alpha = 0.05:
   - a) Rumuskan H0 dan H1 dengan jelas (tentukan arah uji)
   - b) Hitung t-statistic dan p-value secara manual
   - c) Buat keputusan dan interpretasikan hasilnya
   - d) Hitung Cohen's d dan interpretasikan signifikansi praktis

**8.** Seorang mahasiswa melakukan penelitian tentang efektivitas belajar. Ia mengukur skor kuis (0–100) dari 15 mahasiswa sebelum dan sesudah menggunakan *flashcard* digital selama 2 minggu:

   Sebelum: 62, 55, 70, 58, 65, 72, 48, 60, 68, 53, 75, 61, 57, 64, 69
   Sesudah: 70, 62, 75, 65, 71, 79, 55, 68, 74, 61, 80, 68, 63, 72, 76

   - a) Uji apakah flashcard digital meningkatkan skor (alpha = 0.05)
   - b) Hitung effect size Cohen's d
   - c) Interpretasikan hasil secara menyeluruh (statistik DAN praktis)

**9.** Dua tim pengembang (Tim A: n = 25, Tim B: n = 28) menyelesaikan sprint menggunakan metodologi berbeda. Rata-rata bug per sprint: Tim A = 12.4 (SD = 3.2), Tim B = 10.8 (SD = 2.9). Apakah perbedaan ini signifikan (alpha = 0.05)? Hitung juga Cohen's d.

**10.** Jelaskan mengapa pernyataan berikut salah, dan berikan interpretasi yang benar:
   > "Hasil uji kami menunjukkan p = 0.08. Karena p > 0.05, kami menyimpulkan bahwa tidak ada perbedaan antara kedua metode pembelajaran."

### Soal Mahir (C3–C4)

**11. [Python]** Dataset nilai mahasiswa dua angkatan tersedia dalam dua array berikut. Lakukan analisis hipotesis **lengkap** menggunakan Python:

```python
angkatan_2022 = [75, 80, 68, 85, 72, 78, 82, 70, 76, 83,
                 69, 77, 81, 74, 79, 73, 86, 71, 84, 78]
angkatan_2023 = [82, 87, 75, 91, 79, 85, 89, 77, 83, 90,
                 76, 84, 88, 81, 86, 80, 93, 78, 91, 85]
```

   Analisis harus mencakup:
   - a) Formulasi H0 dan H1 yang tepat
   - b) Uji normalitas (Shapiro-Wilk + QQ-plot)
   - c) Uji kesamaan varians (Levene's test) dan pilih Student atau Welch t-test
   - d) Lakukan uji hipotesis dan buat keputusan
   - e) Hitung Cohen's d dan interpretasikan
   - f) Buat visualisasi: boxplot perbandingan + distribusi t dengan rejection region
   - g) Tulis paragraf kesimpulan dalam konteks akademik

**12. [Python — Analisis Kritis]** Tunjukkan fenomena "p-hacking" dengan simulasi berikut: Bangkitkan dua kelompok data dari distribusi normal yang **identik** (H0 benar: tidak ada perbedaan). Ulangi uji t sebanyak 1.000 kali. Berapa kali H0 ditolak (p < 0.05)? Apa implikasi temuan ini terhadap praktik riset yang baik? Visualisasikan distribusi p-value yang dihasilkan.

**13. [Analisis Integratif]** Sebuah startup teknologi di Jakarta melakukan A/B Testing untuk dua versi antarmuka aplikasi mereka:
   - Versi A (lama): 50 pengguna, rata-rata waktu sesi = 12.3 menit (SD = 2.8)
   - Versi B (baru): 50 pengguna, rata-rata waktu sesi = 13.1 menit (SD = 3.1)

   a) Uji apakah perbedaan waktu sesi signifikan (alpha = 0.05)
   b) Hitung Cohen's d. Apakah efeknya bermakna secara praktis?
   c) Meskipun hasilnya "signifikan" (jika p < 0.05), apa pertimbangan bisnis lain yang harus diperhatikan sebelum memutuskan meluncurkan Versi B ke semua pengguna?
   d) Berapa ukuran sampel minimum yang dibutuhkan untuk mendeteksi effect size d = 0.5 dengan power 80% dan alpha = 0.05?

---

## Referensi

1. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics* (4th ed.). OpenIntro, Inc. Chapters 5–6. Tersedia gratis di: openintro.org

2. Downey, A. B. (2021). *Think Stats: Exploratory Data Analysis* (2nd ed.). O'Reilly Media. Chapter 9. Tersedia gratis di: greenteapress.com

3. Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum Associates.

4. Wasserstein, R. L., & Lazar, N. A. (2016). The ASA Statement on p-Values: Context, Process, and Purpose. *The American Statistician*, 70(2), 129–133. https://doi.org/10.1080/00031305.2016.1154108

5. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media. Chapter 5. Tersedia gratis di: jakevdp.github.io/PythonDataScienceHandbook

6. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.

7. Scipy documentation — scipy.stats: https://docs.scipy.org/doc/scipy/reference/stats.html

---

*Bab ini merupakan bagian dari mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia.*
*Penulis: Tri Aji Nugroho, S.T., M.T. | CPMK-4 (C4 — Analyze)*
