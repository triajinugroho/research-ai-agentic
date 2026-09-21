# Minggu 14: Korelasi dan Pengantar Regresi Linear

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 14 |
| **Topik** | Kovarians, korelasi Pearson dan Spearman, regresi linear sederhana, R², diagnostik residual |
| **CPL / CPMK** | CPL10 / CPMK102 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Indikator Mingguan** | Menganalisis korelasi dan membangun model regresi linear sederhana beserta diagnostiknya |
| **Level Bloom** | C4 (Menganalisis) |
| **Durasi** | 150 menit tatap muka |
| **Metode** | Kuliah, latihan terbimbing, studi kasus korelasi palsu |

---

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menghitung** (C3) dan **menafsirkan** (C4) koefisien korelasi Pearson dan Spearman.
2. **Menjelaskan** (C2) mengapa korelasi tidak menyatakan sebab-akibat dan mengenali tiga penyebab korelasi palsu.
3. **Membangun** (C3) model regresi linear sederhana dengan metode kuadrat terkecil.
4. **Menafsirkan** (C4) koefisien regresi, R², dan *p-value*-nya dalam konteks masalah.
5. **Memeriksa** (C4) asumsi regresi melalui diagnostik residual.

---

## Materi Pembelajaran

### 1. Kovarians dan Korelasi

#### 1.1 Kovarians

$$\text{Cov}(X, Y) = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n - 1}$$

Kovarians menyatakan arah hubungan, tetapi **besarnya bergantung satuan** — sehingga sulit ditafsirkan.

#### 1.2 Korelasi Pearson

$$r = \frac{\text{Cov}(X, Y)}{s_X \cdot s_Y} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \sum(y_i - \bar{y})^2}}$$

Korelasi adalah kovarians yang dinormalisasi, sehingga **selalu berada antara −1 dan +1** dan tidak bergantung satuan.

| \|r\| | Kekuatan Hubungan Linear |
|-------|--------------------------|
| 0,00 – 0,19 | Sangat lemah |
| 0,20 – 0,39 | Lemah |
| 0,40 – 0,59 | Sedang |
| 0,60 – 0,79 | Kuat |
| 0,80 – 1,00 | Sangat kuat |

```python
import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("nilai_mahasiswa_if.csv")

x = df["jam_belajar"].values
y = df["nilai_uas"].values

kovarians = np.cov(x, y, ddof=1)[0, 1]
r_pearson, p_pearson = stats.pearsonr(x, y)
r_spearman, p_spearman = stats.spearmanr(x, y)

print(f"Kovarians          : {kovarians:.4f}  (satuannya jam × poin — sulit ditafsirkan)")
print(f"Korelasi Pearson   : r = {r_pearson:.4f}, p = {p_pearson:.6f}")
print(f"Korelasi Spearman  : ρ = {r_spearman:.4f}, p = {p_spearman:.6f}")
print(f"\nKoefisien determinasi r² = {r_pearson**2:.4f}")
print(f"→ {r_pearson**2*100:.1f}% keragaman nilai UAS berkaitan dengan jam belajar.")
print(f"→ {(1-r_pearson**2)*100:.1f}% sisanya dijelaskan faktor lain.")
```

#### 1.3 Pearson vs Spearman

| Aspek | Pearson | Spearman |
|-------|---------|----------|
| Mengukur | Hubungan **linear** | Hubungan **monoton** (naik/turun konsisten) |
| Bekerja pada | Data interval/rasio | Data ordinal ke atas |
| Tahan pencilan | Tidak | Ya |
| Asumsi | Kedua variabel mendekati Normal | Tidak perlu |

```python
import numpy as np
from scipy import stats

# Hubungan monoton tetapi tidak linear
x = np.arange(1, 31)
y = x ** 3           # naik terus, tetapi melengkung tajam

print(f"Pearson : {stats.pearsonr(x, y)[0]:.4f}  (tidak sempurna, karena tak linear)")
print(f"Spearman: {stats.spearmanr(x, y)[0]:.4f}  (sempurna, karena monoton)")

# Pengaruh satu pencilan
x2 = np.concatenate([np.arange(1, 21), [100]])
y2 = np.concatenate([np.arange(1, 21), [5]])
print(f"\nDengan satu pencilan ekstrem:")
print(f"Pearson : {stats.pearsonr(x2, y2)[0]:.4f}  (terseret)")
print(f"Spearman: {stats.spearmanr(x2, y2)[0]:.4f}  (lebih tahan)")
```

---

### 2. Korelasi Bukan Sebab-Akibat

#### 2.1 Tiga Penyebab Korelasi Tanpa Sebab-Akibat

```
   (a) KEBETULAN                (b) VARIABEL PERANCU          (c) ARAH TERBALIK
                                     (confounder)

    X ····? ···· Y                     Z                        X ←──── Y
                                      ╱ ╲
    tidak ada hubungan               ╱   ╲                   yang dianggap sebab
    nyata sama sekali               X     Y                  sebenarnya akibat
```

**(a) Kebetulan.** Dengan cukup banyak variabel yang dibandingkan, korelasi tinggi pasti muncul secara acak. Menelusuri 1.000 pasangan variabel pada α = 0,05 menghasilkan sekitar 50 "temuan" palsu.

**(b) Variabel perancu.** Contoh klasik: penjualan es krim berkorelasi dengan jumlah tenggelam. Penyebab sebenarnya: **musim panas** memengaruhi keduanya.

Contoh Informatika: jumlah baris kode berkorelasi dengan jumlah bug. Perancunya: **kompleksitas fitur** memengaruhi keduanya.

**(c) Arah terbalik.** Apakah tim yang banyak rapat menjadi lebih produktif, atau tim yang bermasalah jadi banyak rapat?

#### 2.2 Latihan: Menelaah Klaim

Untuk tiap klaim, tentukan penjelasan alternatifnya:

| Klaim | Penjelasan alternatif? |
|-------|------------------------|
| "Mahasiswa yang punya laptop mahal nilainya lebih tinggi" | |
| "Proyek yang memakai TypeScript punya lebih sedikit bug" | |
| "Pengguna aplikasi kami lebih sehat daripada rata-rata nasional" | |
| "Server dengan uptime tinggi menerima lebih banyak trafik" | |

---

### 3. Regresi Linear Sederhana

#### 3.1 Model

$$y = \beta_0 + \beta_1 x + \varepsilon$$

| Simbol | Makna |
|--------|-------|
| β₀ | Intersep — nilai y ketika x = 0 |
| β₁ | Kemiringan — perubahan y untuk setiap kenaikan satu satuan x |
| ε | Galat acak |

Estimasi dengan **metode kuadrat terkecil** (*least squares*) meminimumkan Σ(yᵢ − ŷᵢ)².

$$\hat{\beta}_1 = r \cdot \frac{s_y}{s_x} \qquad \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$

#### 3.2 Implementasi dengan statsmodels

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_csv("harga_rumah_jabodetabek.csv")

X = df[["luas_bangunan"]]
y = df["harga_juta"]

X_const = sm.add_constant(X)          # menambahkan kolom intersep
model = sm.OLS(y, X_const).fit()

print(model.summary())
```

**Cara membaca keluaran yang penting:**

| Bagian | Artinya |
|--------|---------|
| `coef` intersep | Perkiraan harga ketika luas = 0 (sering tidak bermakna) |
| `coef` luas_bangunan | Tambahan harga per m² tambahan |
| `P>\|t\|` | Apakah koefisien berbeda nyata dari nol |
| `R-squared` | Proporsi keragaman harga yang dijelaskan model |
| `[0.025 0.975]` | Interval kepercayaan koefisien |
| `Durbin-Watson` | Indikasi autokorelasi residual (≈ 2 berarti baik) |

```python
b0, b1 = model.params
r2 = model.rsquared

print(f"\nPersamaan regresi:")
print(f"  harga = {b0:.3f} + {b1:.3f} × luas_bangunan")
print(f"\nTafsir kemiringan:")
print(f"  Setiap tambahan 1 m² luas bangunan dikaitkan dengan")
print(f"  kenaikan harga sekitar Rp {b1:.2f} juta.")
print(f"\nR² = {r2:.4f} → model menjelaskan {r2*100:.1f}% keragaman harga.")
print(f"  Sisanya {(1-r2)*100:.1f}% dijelaskan faktor lain")
print(f"  (lokasi, umur bangunan, akses transportasi, dan sebagainya).")
```

> **Peringatan penting tentang ekstrapolasi.** Model hanya sahih pada rentang data yang dipakai melatihnya. Memakai model ini untuk memperkirakan harga rumah seluas 5.000 m² — jauh di luar rentang data — adalah **ekstrapolasi** dan tidak dapat dipertanggungjawabkan.

---

### 4. Diagnostik Residual

Regresi linear mengandaikan empat hal, disingkat **LINE**:

| Huruf | Asumsi | Cara memeriksa |
|-------|--------|----------------|
| **L** | *Linearity* — hubungan memang linear | Scatter plot residual vs prediksi |
| **I** | *Independence* — residual saling bebas | Durbin-Watson; telaah rancangan |
| **N** | *Normality* — residual berdistribusi Normal | Q-Q plot residual |
| **E** | *Equal variance* (homoskedastisitas) | Residual vs prediksi tidak berbentuk corong |

```python
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats

def diagnostik_regresi(model, X, y):
    """Empat plot diagnostik baku untuk regresi linear."""
    prediksi = model.fittedvalues
    residual = model.resid
    residual_std = residual / residual.std()

    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    # (1) Residual vs prediksi — memeriksa linearitas dan homoskedastisitas
    axes[0, 0].scatter(prediksi, residual, alpha=0.5, s=25)
    axes[0, 0].axhline(0, color="#c0392b", linestyle="--")
    axes[0, 0].set_xlabel("Nilai prediksi")
    axes[0, 0].set_ylabel("Residual")
    axes[0, 0].set_title("Residual vs Prediksi\n(cari pola dan bentuk corong)")

    # (2) Q-Q plot — memeriksa kenormalan residual
    stats.probplot(residual, dist="norm", plot=axes[0, 1])
    axes[0, 1].set_title("Q-Q Plot Residual\n(titik harus di garis)")

    # (3) Histogram residual
    axes[1, 0].hist(residual, bins=30, color="steelblue", edgecolor="white")
    axes[1, 0].set_xlabel("Residual")
    axes[1, 0].set_title("Sebaran Residual\n(idealnya simetris di sekitar 0)")

    # (4) Scale-Location — memeriksa homoskedastisitas
    axes[1, 1].scatter(prediksi, np.sqrt(np.abs(residual_std)), alpha=0.5, s=25)
    axes[1, 1].set_xlabel("Nilai prediksi")
    axes[1, 1].set_ylabel("√|residual terstandardisasi|")
    axes[1, 1].set_title("Scale-Location\n(garis tren harus mendatar)")

    plt.tight_layout()
    plt.show()

    # Uji formal
    print("--- UJI FORMAL ASUMSI ---")
    _, p_shapiro = stats.shapiro(residual[:5000])
    print(f"Kenormalan residual (Shapiro-Wilk): p = {p_shapiro:.6f}")

    from statsmodels.stats.diagnostic import het_breuschpagan
    _, p_bp, _, _ = het_breuschpagan(residual, model.model.exog)
    print(f"Homoskedastisitas (Breusch-Pagan) : p = {p_bp:.6f} "
          f"{'→ ragam homogen' if p_bp > 0.05 else '→ HETEROSKEDASTIS'}")

    from statsmodels.stats.stattools import durbin_watson
    dw = durbin_watson(residual)
    print(f"Durbin-Watson                      : {dw:.4f} "
          f"{'→ tidak ada autokorelasi' if 1.5 < dw < 2.5 else '→ periksa autokorelasi'}")

diagnostik_regresi(model, X_const, y)
```

#### Pola Residual yang Perlu Diwaspadai

```
   BAIK                  MELENGKUNG            CORONG
   (acak di sekitar 0)   (hubungan tak linear) (heteroskedastis)

    ·  · ·  ·  ·          ·      ·              ·
   ──·──·──·──·──        · ·   · ·             ·· ··
    · ·  ·  · ·           ·  ·  ·             ··· ···
                            ···              ····  ····

   asumsi terpenuhi     → coba transformasi   → coba transformasi log
                          atau tambah suku      atau regresi terboboti
                          kuadratik
```

---

### 5. Menutup Fase Inferensial

```
  Yang sudah dipelajari pada Minggu 9–14:

  Minggu 9   CLT — dasar seluruh inferensi
  Minggu 10  Estimasi — "berapa nilainya, dan seberapa yakin?"
  Minggu 11  Uji satu sampel — "apakah berbeda dari nilai acuan?"
  Minggu 12  Uji dua sampel — "apakah dua kelompok berbeda?"
  Minggu 13  ANOVA & chi-square — "apakah banyak kelompok berbeda?"
  Minggu 14  Korelasi & regresi — "apakah dua besaran berhubungan?"

              ↓ semuanya bertemu di ↓

           PROYEK AKHIR (Minggu 15)
```

> **Menuju Analisis Data Statistik (Semester 2).** Regresi linear sederhana yang dipelajari minggu ini akan dikembangkan menjadi **regresi berganda**, analisis data kategorikal, dan pengantar pemodelan. Dan pada Semester 5, regresi ini akan Anda kenali kembali sebagai **model pembelajaran mesin yang paling dasar** — dengan istilah yang berbeda: β menjadi *weights*, kuadrat terkecil menjadi *loss function*, dan R² menjadi salah satu *evaluation metric*.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (Mandiri — 60 menit)

1. Membaca [Bab 13 buku ajar](../06-buku-ajar/bab-13-statistika-dengan-bantuan-ai.md) bagian korelasi–regresi, dan Bab 12.
2. **Mencari satu contoh korelasi palsu** (misalnya dari *Spurious Correlations*) dan menjelaskan penyebabnya.

### Di Kelas (150 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–10' | Pembahasan Kuis 4 |
| 10–40' | Kuliah: kovarians, korelasi Pearson dan Spearman, kapan memakai yang mana |
| 40–65' | **Bedah kasus korelasi palsu:** tiga penyebab; mahasiswa menyajikan contohnya |
| 65–75' | Istirahat |
| 75–110' | Kuliah + latihan: regresi linear sederhana; membaca keluaran statsmodels |
| 110–140' | Studio: diagnostik residual pada data harga rumah |
| 140–150' | Pengarahan presentasi proyek Minggu 15 |

### Setelah Kelas (Mandiri — 180 menit)

1. Mengerjakan [Lab 14](../04-labs/lab-14-korelasi-regresi-linear.md).
2. **Menyelesaikan laporan dan notebook proyek — dikumpulkan minggu ini.**
3. Menyiapkan presentasi proyek.

---

## Penugasan

| Kode | Tugas | Bobot | Batas Waktu |
|------|-------|-------|-------------|
| T-14 | Laporan Lab 14 — Korelasi dan regresi linear | 2,04% | Sebelum kelas Minggu 15 |
| P-01a | **Laporan dan notebook proyek** | (dinilai Minggu 15) | Minggu 14 |

---

## Rangkuman

1. **Kovarians** menunjukkan arah hubungan tetapi bergantung satuan; **korelasi** menormalisasinya ke rentang [−1, +1].
2. **Pearson** mengukur hubungan linear dan peka pencilan; **Spearman** mengukur hubungan monoton dan lebih tahan pencilan.
3. **Korelasi bukan sebab-akibat.** Tiga penyebabnya: kebetulan, variabel perancu, dan arah hubungan yang terbalik.
4. **Regresi linear** memodelkan y sebagai fungsi linear x dengan metode kuadrat terkecil.
5. **Tafsir kemiringan** selalu dalam bentuk "setiap kenaikan satu satuan x **dikaitkan dengan** perubahan sebesar β₁ pada y" — bukan "menyebabkan".
6. **R²** menyatakan proporsi keragaman yang dijelaskan model. R² tinggi tidak menjamin model benar, dan R² rendah tidak berarti model tidak berguna.
7. **Ekstrapolasi di luar rentang data tidak dapat dipertanggungjawabkan.**
8. Asumsi regresi disingkat **LINE**: Linearity, Independence, Normality of residuals, Equal variance. Diagnostik residual **wajib** dilakukan, bukan pilihan.
9. Regresi linear akan Anda temui kembali di Semester 5 sebagai **model pembelajaran mesin paling dasar**, dengan istilah yang berbeda.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 11. Pearson.
2. Montgomery, D. C., Peck, E. A., & Vining, G. G. (2021). *Introduction to Linear Regression Analysis* (6th ed.). Wiley.
3. Vigen, T. (2015). *Spurious Correlations*. Hachette Books.
4. Anscombe, F. J. (1973). Graphs in Statistical Analysis. *The American Statistician*, 27(1), 17–21.
5. Dokumentasi statsmodels — *Linear Regression*. <https://www.statsmodels.org/stable/regression.html>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
