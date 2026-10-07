# BAB 13: KORELASI DAN REGRESI LINEAR

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `PS-Sub-CPMK102-1` | Menghitung dan menafsirkan korelasi Pearson dan Spearman | C3–C4 |
| `PS-Sub-CPMK102-1` | Membangun model regresi linear sederhana dan menafsirkan koefisiennya | C3–C4 |
| `PS-Sub-CPMK102-1` | Memeriksa asumsi regresi melalui diagnostik residual | C4 |

---

## 13.1 Kovarians dan Korelasi

### 13.1.1 Kovarians

$$\text{Cov}(X, Y) = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n - 1}$$

Kovarians menyatakan **arah** hubungan, tetapi besarnya bergantung satuan — sehingga sulit ditafsirkan. Kovarians antara luas rumah (m²) dan harga (rupiah) akan bernilai miliaran; angka itu tidak memberi tahu apa pun tentang kekuatan hubungan.

### 13.1.2 Korelasi Pearson

$$r = \frac{\text{Cov}(X, Y)}{s_X \cdot s_Y} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \sum(y_i - \bar{y})^2}}$$

Korelasi adalah kovarians yang dinormalisasi: **selalu antara −1 dan +1**, dan **tidak bergantung satuan**.

| \|r\| | Kekuatan Hubungan Linear |
|-------|--------------------------|
| 0,00 – 0,19 | Sangat lemah |
| 0,20 – 0,39 | Lemah |
| 0,40 – 0,59 | Sedang |
| 0,60 – 0,79 | Kuat |
| 0,80 – 1,00 | Sangat kuat |

**Koefisien determinasi r²** menyatakan proporsi keragaman y yang berkaitan dengan x.

### 13.1.3 Pearson vs Spearman

| Aspek | Pearson | Spearman |
|-------|---------|----------|
| Mengukur | Hubungan **linear** | Hubungan **monoton** |
| Bekerja pada | Interval/rasio | Ordinal ke atas |
| Tahan pencilan | Tidak | Ya |
| Asumsi | Kedua variabel mendekati Normal | Tidak perlu |

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)

def bandingkan(x, y, nama):
    rp, _ = stats.pearsonr(x, y)
    rs, _ = stats.spearmanr(x, y)
    print(f"{nama:<38} r={rp:>7.4f}  ρ={rs:>7.4f}")

x = np.arange(1, 41)
bandingkan(x, 2*x + rng.normal(0, 5, 40), "(a) Linear dengan derap")
bandingkan(x, x**3, "(b) Monoton tetapi melengkung tajam")

x3 = np.concatenate([np.arange(1, 31), [100]])
y3 = np.concatenate([np.arange(1, 31), [5]])
bandingkan(x3, y3, "(c) Dengan satu pencilan ekstrem")

x4 = np.linspace(-10, 10, 60)
bandingkan(x4, x4**2 + rng.normal(0, 4, 60), "(d) Parabola (kuat, tak monoton)")
```

> **Perhatikan kasus (d).** Korelasi Pearson mendekati nol padahal hubungannya jelas kuat — karena parabola simetris bukan hubungan linear maupun monoton.
>
> **Pelajarannya: scatter plot wajib dilihat sebelum mempercayai angka korelasi.** Angka r = 0,02 dapat berarti "tidak ada hubungan" atau "ada hubungan kuat tetapi tidak linear", dan keduanya sangat berbeda konsekuensinya.

---

## 13.2 Korelasi Bukan Sebab-Akibat

### 13.2.1 Tiga Penyebab Korelasi Tanpa Sebab-Akibat

```
   (a) KEBETULAN                (b) VARIABEL PERANCU          (c) ARAH TERBALIK

    X ····? ···· Y                     Z                        X ←──── Y
                                      ╱ ╲
    tidak ada hubungan               ╱   ╲                   yang dianggap sebab
    nyata sama sekali               X     Y                  sebenarnya akibat
```

#### (a) Kebetulan

Dengan cukup banyak variabel yang dibandingkan, korelasi tinggi **pasti** muncul secara acak.

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)
n_var, n_obs = 100, 30
data = rng.normal(0, 1, (n_var, n_obs))

signifikan = [(i, j, stats.pearsonr(data[i], data[j])[0])
              for i in range(n_var) for j in range(i+1, n_var)
              if stats.pearsonr(data[i], data[j])[1] < 0.05]

total = n_var*(n_var-1)//2
print(f"Dari {total:,} pasangan variabel ACAK:")
print(f"  {len(signifikan)} 'signifikan' (harapan teoretis: {total*0.05:.0f})")
terkuat = max(signifikan, key=lambda t: abs(t[2]))
print(f"  Korelasi terkuat: r = {terkuat[2]:.4f}")
print("\n→ Semuanya PALSU.")
```

#### (b) Variabel Perancu

Contoh klasik: penjualan es krim berkorelasi dengan jumlah tenggelam. Penyebab sebenarnya: **musim panas** memengaruhi keduanya.

Contoh Informatika: jumlah baris kode berkorelasi dengan jumlah bug. Perancunya: **kompleksitas fitur**.

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(7)
n = 300
kompleksitas = rng.uniform(1, 10, n)                       # perancu
baris_kode = 200*kompleksitas + rng.normal(0, 150, n)
jumlah_bug = 3*kompleksitas + rng.normal(0, 2.5, n)

def korelasi_parsial(x, y, z):
    """Korelasi x dan y setelah pengaruh z dikendalikan."""
    rxy = stats.pearsonr(x, y)[0]
    rxz = stats.pearsonr(x, z)[0]
    ryz = stats.pearsonr(y, z)[0]
    return (rxy - rxz*ryz) / np.sqrt((1-rxz**2)*(1-ryz**2))

print(f"r(baris_kode, bug)          = {stats.pearsonr(baris_kode, jumlah_bug)[0]:.4f}")
print(f"r parsial (kompleksitas dikendalikan) = "
      f"{korelasi_parsial(baris_kode, jumlah_bug, kompleksitas):.4f}")
print("\n→ Korelasinya nyaris hilang. Penyebab sebenarnya KOMPLEKSITAS.")
```

#### (c) Arah Terbalik

Apakah tim yang sering rapat menjadi lebih produktif, atau tim yang bermasalah jadi banyak rapat? Data korelasional **tidak dapat membedakan** keduanya.

### 13.2.2 Apa yang Dapat Membuktikan Sebab-Akibat

| Rancangan | Dapat menyimpulkan sebab-akibat? |
|-----------|----------------------------------|
| Observasional (data yang ada) | **Tidak** |
| Observasional + pengendalian perancu | Lebih kuat, tetapi masih tidak pasti |
| **Eksperimen dengan pengacakan** | **Ya** — pengacakan menyeimbangkan seluruh perancu, yang terukur maupun tidak |
| Deret waktu dengan intervensi | Bergantung rancangan |

> **Inilah alasan A/B testing (Bab 11) begitu berharga:** pengacakan penugasan adalah satu-satunya cara praktis untuk menyimpulkan sebab-akibat dalam sistem perangkat lunak.

---

## 13.3 Regresi Linear Sederhana

### 13.3.1 Model

$$y = \beta_0 + \beta_1 x + \varepsilon$$

| Simbol | Makna |
|--------|-------|
| β₀ | Intersep — nilai y ketika x = 0 |
| β₁ | Kemiringan — perubahan y untuk setiap kenaikan satu satuan x |
| ε | Galat acak |

Estimasi dengan **metode kuadrat terkecil** meminimumkan Σ(yᵢ − ŷᵢ)²:

$$\hat{\beta}_1 = r \cdot \frac{s_y}{s_x} \qquad \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$

### 13.3.2 Implementasi dan Pembacaan Keluaran

```python
import pandas as pd
import statsmodels.api as sm

rumah = pd.read_csv("harga_rumah_jabodetabek.csv")
X = sm.add_constant(rumah[["luas_bangunan"]])
y = rumah["harga_juta"]
model = sm.OLS(y, X).fit()

print(model.summary())
```

**Bagian keluaran yang harus dibaca:**

| Bagian | Artinya |
|--------|---------|
| `coef` const | Intersep β₀ |
| `coef` luas_bangunan | Kemiringan β₁ |
| `P>\|t\|` | Apakah koefisien berbeda nyata dari nol |
| `R-squared` | Proporsi keragaman y yang dijelaskan model |
| `Adj. R-squared` | R² terkoreksi jumlah prediktor |
| `[0.025 0.975]` | Interval kepercayaan koefisien |
| `Durbin-Watson` | Indikasi autokorelasi residual (≈2 berarti baik) |
| `Prob(Omnibus)` | Indikasi kenormalan residual |

```python
b0, b1 = model.params
print(f"harga = {b0:.4f} + {b1:.4f} × luas_bangunan\n")
print("TAFSIR:")
print(f"  Setiap tambahan 1 m² luas bangunan DIKAITKAN DENGAN")
print(f"  kenaikan harga sekitar Rp {b1:.2f} juta.")
print(f"\nR² = {model.rsquared:.4f}")
print(f"  → {model.rsquared*100:.1f}% keragaman harga terjelaskan oleh luas.")
print(f"  → {(1-model.rsquared)*100:.1f}% oleh faktor lain: lokasi, umur,")
print("     akses transportasi, kondisi bangunan.")
```

> **Perhatikan pilihan kata: "dikaitkan dengan", bukan "menyebabkan".**
>
> Data harga rumah adalah data observasional. Rumah yang luas mungkin juga berada di lokasi yang lebih baik, lebih baru, atau memiliki fasilitas lebih lengkap. Model tidak dapat memisahkan pengaruh-pengaruh itu.
>
> Dalam mata kuliah ini, menuliskan "menyebabkan" untuk hasil regresi dari data observasional **mengurangi nilai**.

### 13.3.3 Bahaya Ekstrapolasi

```python
prediksi_3000 = model.predict([1, 3000])[0]
print(f"Rentang data: {rumah['luas_bangunan'].min():.0f} – "
      f"{rumah['luas_bangunan'].max():.0f} m²")
print(f"Prediksi untuk 3.000 m²: Rp {prediksi_3000:,.0f} juta")
print("\n→ Angka ini TIDAK dapat dipercaya.")
print("  Model tidak pernah melihat data seukuran itu;")
print("  hubungannya bisa saja tidak lagi linear di luar rentang.")
```

> **Model hanya sahih pada rentang data yang dipakai melatihnya.** Menyatakan batas keberlakuan adalah bagian dari pelaporan yang jujur.

---

## 13.4 Diagnostik Residual: Asumsi LINE

| Huruf | Asumsi | Cara memeriksa | Bila dilanggar |
|-------|--------|----------------|----------------|
| **L** | *Linearity* | Plot residual vs prediksi | Tambah suku kuadratik atau transformasi |
| **I** | *Independence* | Durbin-Watson; telaah rancangan | Model deret waktu |
| **N** | *Normality* residual | Q-Q plot residual | Transformasi; bootstrap |
| **E** | *Equal variance* | Residual vs prediksi tidak berbentuk corong | Transformasi log; regresi terboboti |

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.stattools import durbin_watson

def diagnostik(model):
    pred, res = model.fittedvalues, model.resid
    res_std = res / res.std()

    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    axes[0,0].scatter(pred, res, alpha=0.5, s=25, color="steelblue")
    axes[0,0].axhline(0, color="#c0392b", linestyle="--")
    axes[0,0].set_title("Residual vs Prediksi\n(L: pola · E: corong)")
    stats.probplot(res, dist="norm", plot=axes[0,1])
    axes[0,1].set_title("Q-Q Plot Residual (N)")
    axes[1,0].hist(res, bins=30, color="steelblue", edgecolor="white")
    axes[1,0].set_title("Sebaran Residual")
    axes[1,1].scatter(pred, np.sqrt(np.abs(res_std)), alpha=0.5, s=25,
                      color="steelblue")
    axes[1,1].set_title("Scale-Location (E)")
    plt.tight_layout(); plt.show()

    _, p_sw = stats.shapiro(res[:5000])
    _, p_bp, _, _ = het_breuschpagan(res, model.model.exog)
    dw = durbin_watson(res)
    print(f"N — Kenormalan residual   : p = {p_sw:.6f} {'✓' if p_sw>0.05 else '✗'}")
    print(f"E — Homoskedastisitas     : p = {p_bp:.6f} "
          f"{'✓' if p_bp>0.05 else '✗ HETEROSKEDASTIS'}")
    print(f"I — Durbin-Watson         : {dw:.4f} "
          f"{'✓' if 1.5<dw<2.5 else '✗'}")

diagnostik(model)
```

### Pola Residual yang Perlu Diwaspadai

```
   BAIK                  MELENGKUNG            CORONG
   (acak di sekitar 0)   (hubungan tak linear) (heteroskedastis)

    ·  · ·  ·  ·          ·      ·              ·
   ──·──·──·──·──        · ·   · ·             ·· ··
    · ·  ·  · ·           ·  ·  ·             ··· ···
                            ···              ····  ····

   asumsi terpenuhi     → transformasi atau  → transformasi log
                          suku kuadratik       atau regresi terboboti
```

---

## 13.5 Menuju Pembelajaran Mesin

```
  Yang Anda pelajari di bab ini         Namanya di Semester 5
  ───────────────────────────────       ─────────────────────
  Koefisien β                      →    weights
  Metode kuadrat terkecil          →    loss function (MSE)
  R²                               →    salah satu evaluation metric
  Residual                         →    error / loss
  Ekstrapolasi                     →    out-of-distribution prediction
  Regresi berganda                 →    multiple features
```

> Regresi linear adalah **model pembelajaran mesin yang paling dasar**. Ketika Anda kelak memanggil `sklearn.linear_model.LinearRegression`, Anda memanggil persis apa yang dipelajari di bab ini — dengan istilah yang berbeda.
>
> Dan yang paling penting: **asumsi LINE tetap berlaku di sana**, meskipun banyak praktisi melupakannya.

---

## AI Corner — Tingkat Mahir

### Wilayah Paling Rawan: Kata "Menyebabkan"

Diberi hasil regresi, sebagian AI akan menulis kalimat interpretasi yang mengandung klaim kausal:

> *"Model menunjukkan bahwa menambah luas bangunan akan meningkatkan harga rumah."*

Kata "akan meningkatkan" adalah klaim sebab-akibat yang tidak didukung data observasional.

**Percobaan:** berikan hasil regresi kepada sebuah AI dan minta interpretasi. Hitung berapa kali muncul kata kausal ("menyebabkan", "meningkatkan", "berdampak pada", "mempengaruhi").

Lalu tanyakan:

> *"Apakah data ini observasional atau eksperimental? Bila observasional, apakah kalimat interpretasimu tadi dapat dipertanggungjawabkan?"*

### Tanggung Jawab yang Tidak Dapat Didelegasikan

| Yang dapat dibantu AI | Yang **tidak** dapat didelegasikan |
|-----------------------|-------------------------------------|
| Menulis kode statsmodels | Menilai apakah asumsi LINE terpenuhi |
| Menghasilkan plot diagnostik | Membaca plot itu dan memutuskan tindakan |
| Menjelaskan arti R² | Menilai apakah R² 0,35 "cukup baik" untuk masalah Anda |
| Menyarankan transformasi | Memutuskan apakah transformasi itu masuk akal secara substantif |
| Menyusun kalimat laporan | **Memastikan kalimat itu tidak melampaui data** |

Baris terakhir adalah tanggung jawab yang melekat pada Anda sebagai penulis laporan. Bila laporan Anda memuat klaim yang salah, **Anda** yang bertanggung jawab — bukan alat yang Anda pakai.

### Daftar Periksa Interpretasi Regresi

Sebelum memasukkan interpretasi hasil regresi ke laporan:

- [ ] Apakah saya memakai "dikaitkan dengan", bukan "menyebabkan"?
- [ ] Apakah saya menyebutkan rentang keberlakuan model?
- [ ] Apakah saya melaporkan R² **dan** apa yang tidak dijelaskannya?
- [ ] Apakah saya menampilkan hasil diagnostik residual?
- [ ] Apakah saya menyebutkan variabel perancu yang mungkin?
- [ ] Bila ada bagian yang dibantu AI, apakah sudah saya catat di AI Usage Log?

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan perbedaan kovarians dan korelasi. Mengapa korelasi lebih mudah ditafsirkan?

2. Kapan memakai Spearman alih-alih Pearson? Beri dua situasi.

3. Sebuah regresi menghasilkan ŷ = 45 + 2,3x dengan R² = 0,62. Tafsirkan ketiga angka itu.

4. Sebutkan keempat asumsi LINE dan cara memeriksa masing-masing.

5. Jelaskan mengapa ekstrapolasi berbahaya, dengan satu contoh.

### Tingkat Menengah

6. Untuk tiap klaim, sebutkan penjelasan alternatif selain sebab-akibat langsung:
   (a) "Mahasiswa yang punya laptop mahal nilainya lebih tinggi."
   (b) "Proyek yang memakai TypeScript punya lebih sedikit bug."
   (c) "Server dengan uptime tinggi menerima lebih banyak trafik."
   (d) "Tim yang memakai code review menghasilkan kode lebih berkualitas."

7. Sebuah scatter plot menunjukkan pola melengkung, tetapi r = 0,12.
   (a) Apakah berarti tidak ada hubungan?
   (b) Apa yang diukur r, dan apa yang tidak diukurnya?
   (c) Hitung apa yang akan diberikan Spearman untuk pola parabola simetris.
   (d) Apa yang harus dilakukan analis?

8. Diagnostik residual menunjukkan pola corong melebar.
   (a) Asumsi mana yang dilanggar?
   (b) Apa dampaknya pada interval kepercayaan koefisien?
   (c) Sebutkan dua cara mengatasinya.
   (d) Setelah transformasi log, bagaimana cara menafsirkan koefisiennya?

9. Sebuah model regresi memiliki R² = 0,18.
   (a) Apakah model ini "buruk"? Jelaskan.
   (b) Dalam bidang apa R² = 0,18 dapat dianggap baik?
   (c) Dalam bidang apa R² = 0,90 masih dianggap kurang?
   (d) Apa yang lebih penting daripada R² dalam menilai sebuah model?

### Tingkat Mahir

10. Lakukan analisis regresi lengkap pada data nyata.
    (a) Pilih dataset dengan sekurang-kurangnya dua variabel numerik.
    (b) Buat scatter plot dan hitung korelasi Pearson serta Spearman.
    (c) Bangun model regresi linear sederhana.
    (d) Jalankan seluruh diagnostik LINE.
    (e) Bila ada asumsi yang dilanggar, lakukan perbaikan dan bandingkan.
    (f) Tuliskan interpretasi lengkap: persamaan, tafsir koefisien, R², rentang keberlakuan, dan apa yang **tidak** dapat disimpulkan.

11. Demonstrasikan variabel perancu secara simulasi.
    (a) Bangkitkan variabel perancu Z.
    (b) Bangkitkan X dan Y yang keduanya bergantung pada Z, tetapi **tidak saling bergantung**.
    (c) Hitung korelasi X–Y. Apakah signifikan?
    (d) Hitung korelasi parsial setelah Z dikendalikan.
    (e) Jalankan regresi Y ~ X, lalu Y ~ X + Z. Bandingkan koefisien X.
    (f) Jelaskan apa yang terjadi dan apa pelajarannya bagi analisis data nyata.

12. Tulislah pedoman (satu halaman) berjudul *"Menulis Interpretasi Regresi yang Jujur"*. Sertakan: kata-kata yang boleh dan tidak boleh dipakai, unsur wajib dalam setiap interpretasi, cara menyatakan rentang keberlakuan, dan tiga contoh kalimat sebelum-sesudah perbaikan.

---

## Rangkuman

1. **Kovarians** menunjukkan arah tetapi bergantung satuan; **korelasi** menormalisasinya ke [−1, +1].
2. **Pearson** mengukur hubungan linear dan peka pencilan; **Spearman** mengukur hubungan monoton dan lebih tahan.
3. **Scatter plot wajib dilihat sebelum mempercayai angka korelasi.** r mendekati nol dapat berarti "tidak ada hubungan" atau "hubungan kuat tetapi tidak linear".
4. **Korelasi bukan sebab-akibat.** Tiga penyebabnya: kebetulan, variabel perancu, dan arah terbalik.
5. Hanya **eksperimen dengan pengacakan** yang dapat menyimpulkan sebab-akibat secara meyakinkan.
6. **Regresi linear** memodelkan y sebagai fungsi linear x dengan metode kuadrat terkecil.
7. **Tafsir kemiringan** selalu "setiap kenaikan satu satuan x **dikaitkan dengan** perubahan β₁ pada y".
8. **R²** menyatakan proporsi keragaman yang dijelaskan. R² tinggi tidak menjamin model benar; R² rendah tidak berarti tak berguna.
9. **Ekstrapolasi di luar rentang data tidak dapat dipertanggungjawabkan.**
10. Asumsi **LINE** wajib diperiksa melalui diagnostik residual.
11. Regresi linear adalah **model pembelajaran mesin paling dasar** — dan asumsinya tetap berlaku di sana.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 11. Pearson.
2. Montgomery, D. C., Peck, E. A., & Vining, G. G. (2021). *Introduction to Linear Regression Analysis* (6th ed.). Wiley.
3. Vigen, T. (2015). *Spurious Correlations*. Hachette Books.
4. Pearl, J., & Mackenzie, D. (2018). *The Book of Why: The New Science of Cause and Effect*. Basic Books.
5. Anscombe, F. J. (1973). Graphs in Statistical Analysis. *The American Statistician*, 27(1), 17–21.
6. Dokumentasi statsmodels — *Linear Regression*. <https://www.statsmodels.org/stable/regression.html>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
