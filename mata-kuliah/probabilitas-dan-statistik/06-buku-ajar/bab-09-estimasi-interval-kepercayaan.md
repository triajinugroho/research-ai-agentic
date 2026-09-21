# BAB 9: ESTIMASI DAN INTERVAL KEPERCAYAAN

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `PS-Sub-CPMK081-1` | Menjelaskan sifat estimator yang baik | C2 |
| `PS-Sub-CPMK081-1` | Menghitung interval kepercayaan rata-rata dan proporsi | C3 |
| `PS-Sub-CPMK081-1` | Menafsirkan tingkat kepercayaan dengan benar dan mengenali salah tafsir | C4 |

---

## 9.1 Estimasi Titik

### 9.1.1 Estimator dan Sifatnya

> **Estimator** adalah aturan untuk menduga parameter populasi dari data sampel. **Estimasi** adalah nilai yang dihasilkannya.

| Parameter | Estimator | Lambang |
|-----------|-----------|---------|
| μ | Rata-rata sampel | x̄ |
| σ² | Varians sampel (penyebut n−1) | s² |
| p | Proporsi sampel | p̂ |

**Tiga sifat estimator yang baik:**

| Sifat | Arti | Contoh |
|-------|------|--------|
| **Tak bias** | E[estimator] = parameter | E[x̄] = μ; s² dengan n−1 tak bias |
| **Efisien** | Variansnya kecil di antara estimator tak bias | x̄ lebih efisien dari median untuk populasi Normal |
| **Konsisten** | Makin mendekati parameter seiring n bertambah | x̄ konsisten karena SE = σ/√n → 0 |

```python
import numpy as np

rng = np.random.default_rng(42)
MU, SIGMA = 100, 15

print(f"Varians populasi sebenarnya: {SIGMA**2}\n")
print(f"{'n':>5}  {'E[s² dgn n]':>13}  {'E[s² dgn n−1]':>15}  {'Bias (n)':>10}")
for n in [3, 5, 10, 30, 100]:
    vn, vn1 = [], []
    for _ in range(20_000):
        s = rng.normal(MU, SIGMA, n)
        vn.append(s.var(ddof=0)); vn1.append(s.var(ddof=1))
    print(f"{n:>5}  {np.mean(vn):>13.2f}  {np.mean(vn1):>15.2f}  "
          f"{np.mean(vn) - SIGMA**2:>10.2f}")
```

> Perhatikan bahwa biasnya paling parah pada n kecil dan mengecil seiring n bertambah. Untuk n = 100, selisihnya sudah hampir tak berarti — tetapi untuk n = 3, penyebut n meremehkan varians sepertiga bagian.

### 9.1.2 Keterbatasan Estimasi Titik

> "Rata-rata waktu respons adalah 214 ms."

Angka ini **hampir pasti tidak sama persis** dengan μ sebenarnya. Sebuah estimasi tanpa ukuran ketidakpastian adalah informasi yang tidak lengkap — dan dalam konteks pengambilan keputusan, bisa menyesatkan.

Interval kepercayaan mengatasi ini dengan menyatakan: **berapa nilainya, dan seberapa yakin kita.**

---

## 9.2 Interval Kepercayaan Rata-Rata

### 9.2.1 Ketika σ Diketahui (Interval-z)

$$\bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

| Tingkat Kepercayaan | α | z(α/2) |
|---------------------|---|--------|
| 90% | 0,10 | 1,645 |
| 95% | 0,05 | 1,960 |
| 99% | 0,01 | 2,576 |

### 9.2.2 Ketika σ Tidak Diketahui (Interval-t)

Dalam praktik σ hampir **tidak pernah** diketahui. Kita menggantinya dengan s, dan sebagai konsekuensinya memakai **distribusi-t** dengan derajat bebas df = n − 1.

$$\bar{x} \pm t_{\alpha/2,\,n-1} \cdot \frac{s}{\sqrt{n}}$$

```
   Distribusi-t vs Normal baku

        Normal ──╮   ╭── t dengan df kecil
                 │   │   (ekor lebih tebal,
              ╭──┴───┴──╮   puncak lebih rendah)
            ╱             ╲
          ╱                 ╲
       ─────────────────────────
       Makin besar df, makin mirip Normal.
```

```python
from scipy import stats

z = stats.norm.ppf(0.975)
print(f"{'df':>6}  {'t(0,025)':>10}  {'z(0,025)':>10}  {'Selisih':>9}")
for df in [1, 2, 5, 10, 20, 30, 50, 100, 500]:
    t = stats.t.ppf(0.975, df)
    print(f"{df:>6}  {t:>10.4f}  {z:>10.4f}  {t - z:>9.4f}")
print("\n→ Pada df ≈ 30, keduanya hampir tidak terbedakan.")
```

```python
import numpy as np
import pandas as pd
from scipy import stats

def ik_rata_rata(data, kepercayaan=0.95):
    """Interval kepercayaan rata-rata dengan distribusi-t."""
    data = np.asarray(data, dtype=float)
    data = data[~np.isnan(data)]
    n = len(data)
    x_bar, s = data.mean(), data.std(ddof=1)
    se = s / np.sqrt(n)
    t_kritis = stats.t.ppf(1 - (1 - kepercayaan)/2, df=n-1)
    margin = t_kritis * se
    return {"n": n, "mean": x_bar, "s": s, "se": se, "df": n-1,
            "t": t_kritis, "margin": margin,
            "bawah": x_bar - margin, "atas": x_bar + margin}

df = pd.read_csv("nilai_mahasiswa_if.csv")
h = ik_rata_rata(df["jam_belajar"].dropna())
for k, v in h.items():
    print(f"  {k:>7}: {v:.4f}" if isinstance(v, float) else f"  {k:>7}: {v}")
print(f"\nIK 95%: [{h['bawah']:.3f} , {h['atas']:.3f}] jam/minggu")
```

> **Aturan praktis:** gunakan interval-t hampir selalu. Interval-z hanya sah bila σ populasi benar-benar diketahui dari sumber lain — situasi yang sangat jarang di luar soal ujian.

### 9.2.3 Pertukaran antara Kepastian dan Presisi

```python
for kep in [0.80, 0.90, 0.95, 0.99, 0.999]:
    h = ik_rata_rata(df["jam_belajar"].dropna(), kepercayaan=kep)
    print(f"{kep*100:>6.1f}%  margin ±{h['margin']:.4f}  "
          f"[{h['bawah']:.3f} , {h['atas']:.3f}]")
```

> Makin tinggi tingkat kepercayaan, makin **lebar** intervalnya. **Kepastian dan presisi saling berlawanan.**
>
> Interval 100% selalu benar tetapi tidak berguna: "rata-rata waktu respons antara 0 dan tak hingga". Memilih tingkat kepercayaan adalah memilih titik keseimbangan.

---

## 9.3 Menafsirkan "95% Kepercayaan"

### 9.3.1 Tafsir yang Salah

> ❌ **"Ada 95% probabilitas bahwa μ berada antara 13,1 dan 15,3."**
>
> **Mengapa salah:** μ adalah **konstanta tetap** (meski nilainya tidak diketahui). Ia tidak "punya probabilitas" berada di mana-mana. Setelah interval dihitung, μ entah ada di dalamnya atau tidak — tidak ada peluang lagi.

> ❌ **"95% dari data berada dalam interval ini."**
>
> **Mengapa salah:** interval kepercayaan adalah tentang **rata-rata**, bukan tentang sebaran data individual. Interval kepercayaan jauh lebih sempit daripada sebaran data.

> ❌ **"Bila penelitian diulang, 95% hasilnya akan jatuh dalam interval ini."**
>
> **Mengapa salah:** itu deskripsi *prediction interval*, bukan *confidence interval*.

### 9.3.2 Tafsir yang Benar

> ✅ **"Bila prosedur ini diulang pada banyak sampel, 95% dari interval yang dihasilkan akan memuat μ sebenarnya."**
>
> Yang memiliki sifat "95%" adalah **prosedurnya**, bukan interval yang satu ini.

> ✅ **Untuk pembaca awam:** "Kami memperkirakan rata-rata sebenarnya berada antara 13,1 dan 15,3 jam per minggu, dengan tingkat kepercayaan 95%."

### 9.3.3 Membuktikannya dengan Simulasi

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(42)
MU, SIGMA, n = 100, 15, 30

plt.figure(figsize=(11, 8))
memuat = 0
for i in range(100):
    s = rng.normal(MU, SIGMA, n)
    se = s.std(ddof=1) / np.sqrt(n)
    t = stats.t.ppf(0.975, n-1)
    bawah, atas = s.mean() - t*se, s.mean() + t*se
    cocok = bawah <= MU <= atas
    memuat += cocok
    plt.plot([bawah, atas], [i, i],
             color="#2980b9" if cocok else "#c0392b", linewidth=1.5)

plt.axvline(MU, color="black", linestyle="--", linewidth=2,
            label=f"μ sebenarnya = {MU}")
plt.title(f"100 interval kepercayaan 95% dari populasi yang SAMA\n"
          f"{memuat} memuat μ · {100-memuat} MELESET (merah)")
plt.legend(); plt.tight_layout(); plt.show()

print(f"Cakupan empiris: {memuat}/100 = {memuat}%")
```

> **Inilah makna sebenarnya.** Sekitar 5 dari 100 interval **memang meleset** — dan itu bukan kesalahan, melainkan konsekuensi yang sudah diperhitungkan sejak awal.
>
> Yang tidak pernah kita ketahui: **interval mana yang meleset**. Interval yang ada di tangan Anda mungkin salah satunya.

### 9.3.4 Mengapa Salah Tafsir Ini Penting

Penelitian Hoekstra dkk. (2014) menunjukkan bahwa **mayoritas peneliti profesional** — bukan hanya mahasiswa — salah menafsirkan interval kepercayaan. Ini bukan kesalahan sepele:

- Pengambil keputusan yang mengira "95% probabilitas μ di sini" akan **terlalu percaya diri**.
- Mereka tidak menyadari bahwa 1 dari 20 studi menghasilkan interval yang meleset sepenuhnya.
- Konsekuensinya: kebijakan yang dibangun di atas satu studi tunggal.

---

## 9.4 Interval Kepercayaan Proporsi

$$\hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

**Syarat kelayakan:** n·p̂ ≥ 10 **dan** n(1−p̂) ≥ 10.

```python
from statsmodels.stats.proportion import proportion_confint

def ik_proporsi(berhasil, n, kepercayaan=0.95):
    p_hat = berhasil / n
    np_, nq_ = n*p_hat, n*(1-p_hat)
    print(f"Data: {berhasil}/{n} = {p_hat:.4f} ({p_hat*100:.2f}%)")
    print(f"Syarat: n·p̂={np_:.1f}, n(1−p̂)={nq_:.1f} → "
          f"{'TERPENUHI' if np_>=10 and nq_>=10 else 'TIDAK TERPENUHI'}\n")
    print(f"{'Metode':>12}  {'Bawah':>10}  {'Atas':>10}  {'Lebar':>8}")
    for m, label in [("normal","Wald"), ("wilson","Wilson"), ("beta","Clopper-P")]:
        b, a = proportion_confint(berhasil, n, alpha=1-kepercayaan, method=m)
        print(f"{label:>12}  {b*100:>9.3f}%  {a*100:>9.3f}%  {(a-b)*100:>7.3f}")

print("KASUS 1 — syarat terpenuhi:"); ik_proporsi(148, 400)
print("\nKASUS 2 — proporsi sangat kecil:"); ik_proporsi(3, 200)
print("\nKASUS 3 — nol keberhasilan:"); ik_proporsi(0, 150)
```

> **Perhatikan Kasus 3.** Metode Wald memberi interval [0, 0] — menyatakan dengan "kepercayaan 95%" bahwa proporsinya **pasti nol**. Jelas keliru: tidak mengamati kejadian dalam 150 percobaan tidak membuktikan kejadian itu mustahil.
>
> Metode **Wilson** dan **Clopper-Pearson** memberi batas atas yang masuk akal (sekitar 2,4%). Gunakan keduanya ketika syarat Wald tidak terpenuhi.

---

## 9.5 Menentukan Ukuran Sampel

$$n = \left(\frac{z_{\alpha/2} \cdot \sigma}{E}\right)^2 \qquad n = \frac{z_{\alpha/2}^2 \cdot p(1-p)}{E^2}$$

```python
import numpy as np
from scipy import stats

def n_proporsi(margin, p_dugaan=0.5, kepercayaan=0.95):
    """p_dugaan=0.5 memberi n terbesar — paling aman bila tidak ada dugaan."""
    z = stats.norm.ppf(1 - (1 - kepercayaan)/2)
    return int(np.ceil(z**2 * p_dugaan * (1 - p_dugaan) / margin**2))

print("SURVEI KEPUASAN — n yang diperlukan:")
print(f"{'Margin':>10}  {'n (90%)':>9}  {'n (95%)':>9}  {'n (99%)':>9}")
for me in [0.10, 0.05, 0.03, 0.02, 0.01]:
    print(f"{me*100:>7.1f} pp  "
          f"{n_proporsi(me, kepercayaan=0.90):>9,}  "
          f"{n_proporsi(me, kepercayaan=0.95):>9,}  "
          f"{n_proporsi(me, kepercayaan=0.99):>9,}")

print("\nPengaruh dugaan awal p (margin ±3%):")
for p in [0.05, 0.25, 0.50, 0.75, 0.95]:
    print(f"  p = {p:.2f} → n = {n_proporsi(0.03, p):>6,}")
print("→ p = 0,50 memberi n TERBESAR. Bila tidak ada dugaan, pakai 0,50.")
```

---

## AI Corner — Tingkat Lanjut

### Salah Tafsir yang Diwariskan

Karena mayoritas teks di internet salah menafsirkan interval kepercayaan, **model bahasa pun mewarisinya**. Anda akan sering menemukan AI menjawab:

> *"Interval ini berarti ada 95% probabilitas bahwa nilai sebenarnya berada di dalamnya."*

Ini salah. Dan yang membuatnya berbahaya: kalimat itu terdengar **sangat meyakinkan**, dan muncul dalam banyak buku teks populer.

### Cara Memeriksa

Ajukan pertanyaan lanjutan:

> *"Apakah μ adalah peubah acak atau konstanta? Bila konstanta, bagaimana ia bisa 'punya probabilitas' berada dalam sebuah interval?"*

Model yang baik akan memperbaiki jawabannya dan menjelaskan bahwa yang berperilaku acak adalah **intervalnya**, bukan μ.

### Batas Kemampuan AI di Bab Ini

| AI bisa | AI tidak bisa |
|---------|---------------|
| Menghitung interval dari x̄, s, n | Menilai apakah sampel Anda acak dan representatif |
| Memilih t atau z berdasarkan informasi yang Anda beri | Mengetahui apakah σ benar-benar diketahui pada kasus Anda |
| Menghitung ukuran sampel | Menentukan margin galat yang **bermakna** untuk masalah Anda |
| Menjelaskan rumus Wilson | Memutuskan tingkat kepercayaan yang tepat untuk konteks keputusan Anda |

Kolom kanan seluruhnya berisi **keputusan**, bukan perhitungan. Dan keputusan memerlukan konteks yang hanya Anda miliki.

### Pemakaian yang Dianjurkan

```
PROMPT YANG BAIK:
"Saya menulis: 'IK 95% untuk rata-rata waktu respons adalah [205, 223] ms,
 artinya kami 95% yakin rata-rata sebenarnya ada di rentang itu.'
 Apakah kalimat saya secara teknis tepat? Bila kurang tepat, bagaimana
 seharusnya, dan bagaimana menuliskannya agar tetap mudah dipahami
 pembaca non-teknis?"
```

---

## Latihan Soal

### Tingkat Dasar

1. Sebutkan tiga sifat estimator yang baik dan jelaskan masing-masing.

2. Dari sampel n = 36 diperoleh x̄ = 120 dan s = 18. Hitung interval kepercayaan 95% untuk μ.

3. Untuk data soal 2, hitung juga interval 90% dan 99%. Bandingkan lebarnya.

4. Dari 500 pengguna, 85 melakukan konversi. Hitung interval kepercayaan 95% untuk proporsi konversi, setelah memeriksa syarat kelayakannya.

5. Tuliskan tafsir yang benar dari "interval kepercayaan 95%" dengan kalimat Anda sendiri.

### Tingkat Menengah

6. Sebuah tim melaporkan: *"IK 95% untuk rata-rata waktu respons adalah [205, 223] ms. Jadi ada 95% kemungkinan rata-rata sebenarnya ada di rentang ini."*
   (a) Apa yang salah dengan kalimat kedua?
   (b) Tuliskan versi yang benar secara teknis.
   (c) Tuliskan versi yang benar **dan** mudah dipahami manajer non-teknis.
   (d) Jelaskan mengapa perbedaan ini bukan sekadar soal kata-kata.

7. Dari 200 permintaan, 3 mengalami galat.
   (a) Hitung p̂ dan periksa syarat kelayakan interval Wald.
   (b) Hitung interval Wald, Wilson, dan Clopper-Pearson.
   (c) Metode mana yang Anda laporkan? Mengapa?
   (d) Apa yang terjadi pada interval Wald bila **nol** galat yang diamati? Mengapa hasilnya tidak masuk akal?

8. Sebuah survei ingin margin galat ±2 poin persen pada tingkat kepercayaan 95%.
   (a) Berapa n yang diperlukan bila tidak ada dugaan awal tentang p?
   (b) Berapa bila dari studi sebelumnya diperkirakan p ≈ 0,15?
   (c) Berapa penghematan sampelnya?
   (d) Apa risiko memakai dugaan awal yang keliru?

9. Rancang dan jalankan simulasi cakupan untuk interval kepercayaan 90% dan 99%.
   (a) Apakah cakupan empirisnya sesuai target?
   (b) Ulangi untuk n = 5 dan n = 50. Apakah ada perbedaan?
   (c) Ulangi dengan populasi Eksponensial. Apakah cakupan tetap sesuai?

### Tingkat Mahir

10. Bandingkan cakupan empiris interval-t pada populasi yang sangat menceng.
    (a) Simulasikan dengan populasi Lognormal(0, 1,5) untuk n = 5, 15, 30, 100.
    (b) Hitung cakupan empiris interval 95% pada masing-masing n.
    (c) Pada n berapa cakupan mendekati 95%?
    (d) Apa implikasinya bagi analisis waktu respons yang menceng kanan?
    (e) Usulkan dua alternatif bila n tidak dapat diperbesar.

11. Implementasikan interval kepercayaan **bootstrap** dan bandingkan dengan interval-t.
    (a) Ambil sampel n = 50 dari data yang menceng.
    (b) Lakukan 10.000 pengambilan ulang dengan pengembalian.
    (c) Hitung interval persentil bootstrap [2,5%, 97,5%].
    (d) Bandingkan dengan interval-t.
    (e) Ulangi untuk **median** — mengapa interval-t tidak dapat dipakai untuk median?
    (f) Kapan bootstrap lebih berguna daripada rumus analitis?

12. Tulislah panduan satu halaman berjudul *"Melaporkan Ketidakpastian: Pedoman untuk Analis Data"*. Sertakan: mengapa estimasi titik saja tidak cukup, cara menuliskan interval kepercayaan secara jujur untuk pembaca teknis dan non-teknis, kesalahan tafsir yang harus dihindari, dan contoh kalimat baku yang dapat dipakai.

---

## Rangkuman

1. **Estimator yang baik** bersifat tak bias, efisien, dan konsisten. Penyebut n−1 membuat s² tak bias.
2. **Estimasi titik tanpa ukuran ketidakpastian adalah informasi yang tidak lengkap.**
3. Gunakan **interval-t** hampir selalu; interval-z hanya sah bila σ benar-benar diketahui.
4. Distribusi-t berekor lebih tebal daripada Normal; perbedaannya hampir hilang pada df ≈ 30.
5. **Kepastian dan presisi saling berlawanan.** Interval yang lebih lebar lebih aman tetapi kurang informatif.
6. **Tafsir yang benar:** yang memiliki sifat "95%" adalah **prosedurnya**, bukan interval tunggal yang sudah dihitung. μ adalah konstanta, bukan peubah acak.
7. Interval kepercayaan adalah tentang **rata-rata**, bukan tentang sebaran data individual.
8. Salah tafsir interval kepercayaan **lazim terjadi bahkan di kalangan peneliti profesional** — dan diwariskan ke model bahasa.
9. Interval proporsi memerlukan n·p̂ ≥ 10 dan n(1−p̂) ≥ 10; bila tidak terpenuhi gunakan **Wilson** atau **Clopper-Pearson**.
10. **Ukuran sampel tumbuh kuadratik** terhadap presisi yang diinginkan.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 9. Pearson.
2. Hoekstra, R., Morey, R. D., Rouder, J. N., & Wagenmakers, E.-J. (2014). Robust misinterpretation of confidence intervals. *Psychonomic Bulletin & Review*, 21(5), 1157–1164.
3. Brown, L. D., Cai, T. T., & DasGupta, A. (2001). Interval Estimation for a Binomial Proportion. *Statistical Science*, 16(2), 101–133.
4. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.), Bab 8. Wiley.
5. Efron, B., & Tibshirani, R. J. (1994). *An Introduction to the Bootstrap*. Chapman & Hall.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
