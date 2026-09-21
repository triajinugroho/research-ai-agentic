# Minggu 10: Estimasi Titik dan Interval Kepercayaan

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 10 |
| **Topik** | Estimator, interval kepercayaan rata-rata dan proporsi, distribusi-t, ukuran sampel |
| **CPL / CPMK** | CPL08 / CPMK081 |
| **Sub-CPMK** | `PS-Sub-CPMK081-1` |
| **Indikator Mingguan** | Menyusun estimasi titik dan interval kepercayaan serta menafsirkan maknanya secara tepat |
| **Level Bloom** | C3–C4 (Menerapkan–Menganalisis) |
| **Durasi** | 150 menit tatap muka |
| **Metode** | Kuliah, latihan terbimbing, simulasi cakupan interval |

---

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menjelaskan** (C2) sifat estimator yang baik: tak bias, efisien, dan konsisten.
2. **Menghitung** (C3) interval kepercayaan untuk rata-rata ketika σ diketahui maupun tidak diketahui.
3. **Menghitung** (C3) interval kepercayaan untuk proporsi.
4. **Menafsirkan** (C4) makna "95% kepercayaan" secara benar dan mengenali salah tafsir yang umum.
5. **Menentukan** (C3) ukuran sampel yang diperlukan untuk mencapai presisi tertentu.

---

## Materi Pembelajaran

### 1. Estimasi Titik

#### 1.1 Estimator dan Sifatnya

> **Estimator** adalah aturan untuk menduga parameter populasi dari data sampel. **Estimasi** adalah nilai yang dihasilkannya.

| Parameter | Estimator | Lambang |
|-----------|-----------|---------|
| μ (rata-rata populasi) | Rata-rata sampel | x̄ |
| σ² (varians populasi) | Varians sampel (n−1) | s² |
| p (proporsi populasi) | Proporsi sampel | p̂ |

**Tiga sifat estimator yang baik:**

| Sifat | Arti | Contoh |
|-------|------|--------|
| **Tak bias** | E[estimator] = parameter | E[x̄] = μ; s² dengan n−1 tak bias, dengan n bias |
| **Efisien** | Variansnya kecil | x̄ lebih efisien daripada median untuk populasi Normal |
| **Konsisten** | Makin mendekati parameter seiring n bertambah | x̄ konsisten karena SE = σ/√n → 0 |

```python
import numpy as np

rng = np.random.default_rng(42)
mu_sebenarnya, sigma_sebenarnya = 100, 15

# Menunjukkan bahwa s² dengan penyebut n−1 tak bias, dengan n bias
n, ulangan = 5, 50_000
var_n = np.empty(ulangan)
var_n1 = np.empty(ulangan)

for i in range(ulangan):
    sampel = rng.normal(mu_sebenarnya, sigma_sebenarnya, n)
    var_n[i] = sampel.var(ddof=0)    # penyebut n   → bias
    var_n1[i] = sampel.var(ddof=1)   # penyebut n−1 → tak bias

print(f"Varians populasi sebenarnya : {sigma_sebenarnya**2}")
print(f"Rata-rata s² dengan n       : {var_n.mean():.2f}  ← meremehkan")
print(f"Rata-rata s² dengan n−1     : {var_n1.mean():.2f}  ← tepat")
```

#### 1.2 Keterbatasan Estimasi Titik

Estimasi titik memberi satu angka, tanpa menyatakan seberapa yakin kita padanya.

> "Rata-rata waktu respons adalah 214 ms."

Angka ini **hampir pasti tidak sama persis** dengan μ sebenarnya. Sebuah estimasi tanpa ukuran ketidakpastian adalah informasi yang tidak lengkap — dan dalam konteks pengambilan keputusan, bisa menyesatkan.

---

### 2. Interval Kepercayaan untuk Rata-Rata

#### 2.1 Ketika σ Diketahui (Interval-z)

$$\bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

| Tingkat Kepercayaan | α | z(α/2) |
|---------------------|---|--------|
| 90% | 0,10 | 1,645 |
| 95% | 0,05 | 1,960 |
| 99% | 0,01 | 2,576 |

```python
import numpy as np
from scipy import stats

def interval_kepercayaan_z(x_bar, sigma, n, kepercayaan=0.95):
    """Interval kepercayaan rata-rata ketika σ populasi diketahui."""
    alpha = 1 - kepercayaan
    z = stats.norm.ppf(1 - alpha/2)
    se = sigma / np.sqrt(n)
    margin = z * se
    return x_bar - margin, x_bar + margin, margin, se

x_bar, sigma, n = 214, 35, 100
bawah, atas, margin, se = interval_kepercayaan_z(x_bar, sigma, n)

print(f"Rata-rata sampel : {x_bar} ms")
print(f"Galat baku       : {se:.3f} ms")
print(f"Margin galat     : {margin:.3f} ms")
print(f"IK 95%           : [{bawah:.2f} , {atas:.2f}] ms")
```

#### 2.2 Ketika σ Tidak Diketahui (Interval-t)

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
       Pada df ≈ 30, keduanya hampir tidak terbedakan.
```

```python
from scipy import stats

print(f"{'df':>5}  {'t(0,025)':>10}  {'z(0,025)':>10}  {'selisih':>9}")
z = stats.norm.ppf(0.975)
for df in [2, 5, 10, 20, 30, 50, 100, 1000]:
    t = stats.t.ppf(0.975, df)
    print(f"{df:>5}  {t:>10.4f}  {z:>10.4f}  {t-z:>9.4f}")
```

```python
import numpy as np
import pandas as pd
from scipy import stats

def interval_kepercayaan_t(data, kepercayaan=0.95):
    """Interval kepercayaan rata-rata ketika σ tidak diketahui (kasus umum)."""
    data = np.asarray(data)
    n = len(data)
    x_bar = data.mean()
    s = data.std(ddof=1)
    se = s / np.sqrt(n)
    t_kritis = stats.t.ppf(1 - (1 - kepercayaan)/2, df=n - 1)
    margin = t_kritis * se
    return {
        "n": n, "mean": x_bar, "s": s, "se": se,
        "df": n - 1, "t_kritis": t_kritis, "margin": margin,
        "bawah": x_bar - margin, "atas": x_bar + margin,
    }

df_data = pd.read_csv("nilai_mahasiswa_if.csv")
hasil = interval_kepercayaan_t(df_data["jam_belajar"].dropna())

for k, v in hasil.items():
    print(f"{k:>10}: {v:.4f}" if isinstance(v, float) else f"{k:>10}: {v}")

print(f"\nIK 95% untuk rata-rata jam belajar: "
      f"[{hasil['bawah']:.2f} , {hasil['atas']:.2f}] jam/minggu")
```

> **Aturan praktis:** gunakan interval-t hampir selalu. Interval-z hanya sah bila σ populasi benar-benar diketahui dari sumber lain — situasi yang sangat jarang di luar soal ujian.

---

### 3. Menafsirkan "95% Kepercayaan" dengan Benar

#### 3.1 Tafsir yang Salah dan yang Benar

> ❌ **SALAH:** "Ada 95% probabilitas bahwa μ berada antara 13,1 dan 15,3."
>
> Mengapa salah: μ adalah **konstanta tetap** (meski nilainya tidak kita ketahui). Ia tidak "punya probabilitas" berada di mana-mana. Setelah interval dihitung, μ entah ada di dalamnya atau tidak — tidak ada peluang lagi.

> ❌ **SALAH:** "95% dari data berada dalam interval ini."
>
> Mengapa salah: interval kepercayaan tentang **rata-rata**, bukan tentang sebaran data individual. Interval kepercayaan jauh lebih sempit daripada sebaran data.

> ✅ **BENAR:** "Bila prosedur ini diulang pada banyak sampel, 95% dari interval yang dihasilkan akan memuat μ sebenarnya."
>
> Yang punya sifat "95%" adalah **prosedurnya**, bukan interval yang satu ini.

> ✅ **BENAR (untuk pembaca awam):** "Kami memperkirakan rata-rata sebenarnya berada antara 13,1 dan 15,3 jam per minggu, dengan tingkat kepercayaan 95%."

#### 3.2 Membuktikannya dengan Simulasi

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(42)
MU_SEBENARNYA, SIGMA = 100, 15
n, n_interval = 30, 100

plt.figure(figsize=(11, 7))
memuat = 0

for i in range(n_interval):
    sampel = rng.normal(MU_SEBENARNYA, SIGMA, n)
    x_bar = sampel.mean()
    se = sampel.std(ddof=1) / np.sqrt(n)
    t = stats.t.ppf(0.975, df=n-1)
    bawah, atas = x_bar - t*se, x_bar + t*se

    cocok = bawah <= MU_SEBENARNYA <= atas
    memuat += cocok
    warna = "#2980b9" if cocok else "#c0392b"
    plt.plot([bawah, atas], [i, i], color=warna, linewidth=1.6)
    plt.plot(x_bar, i, "o", color=warna, markersize=3)

plt.axvline(MU_SEBENARNYA, color="black", linestyle="--", linewidth=2,
            label=f"μ sebenarnya = {MU_SEBENARNYA}")
plt.xlabel("Nilai")
plt.ylabel("Ulangan ke-")
plt.title(f"100 interval kepercayaan 95% dari populasi yang sama\n"
          f"{memuat} interval memuat μ, {n_interval - memuat} tidak "
          f"(merah = meleset)")
plt.legend()
plt.tight_layout()
plt.show()

print(f"Cakupan empiris: {memuat}/{n_interval} = {memuat/n_interval*100:.1f}%")
print("→ Mendekati 95%, sesuai janji prosedurnya.")
```

> **Inilah makna sebenarnya dari tingkat kepercayaan.** Sekitar 5 dari 100 interval **memang meleset** — dan itu bukan kesalahan, melainkan konsekuensi yang sudah diperhitungkan. Kita tidak pernah tahu interval mana yang meleset.

---

### 4. Interval Kepercayaan untuk Proporsi

$$\hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

**Syarat kelayakan:** n·p̂ ≥ 10 dan n(1−p̂) ≥ 10.

```python
import numpy as np
from scipy import stats

def interval_kepercayaan_proporsi(berhasil, n, kepercayaan=0.95):
    """Interval kepercayaan proporsi dengan pemeriksaan syarat kelayakan."""
    p_hat = berhasil / n
    # Pemeriksaan syarat
    layak = (n * p_hat >= 10) and (n * (1 - p_hat) >= 10)
    z = stats.norm.ppf(1 - (1 - kepercayaan)/2)
    se = np.sqrt(p_hat * (1 - p_hat) / n)
    margin = z * se
    return {
        "p_hat": p_hat, "se": se, "margin": margin,
        "bawah": max(0, p_hat - margin), "atas": min(1, p_hat + margin),
        "layak": layak,
        "np": n * p_hat, "n(1-p)": n * (1 - p_hat),
    }

# Kasus: dari 400 pengguna yang mencoba fitur baru, 148 melakukan konversi
hasil = interval_kepercayaan_proporsi(148, 400)

print(f"Proporsi sampel  : {hasil['p_hat']:.4f}  ({hasil['p_hat']*100:.2f}%)")
print(f"Syarat kelayakan : n·p̂ = {hasil['np']:.1f}, n(1−p̂) = {hasil['n(1-p)']:.1f}")
print(f"  → {'terpenuhi' if hasil['layak'] else 'TIDAK terpenuhi, gunakan metode eksak'}")
print(f"Margin galat     : ±{hasil['margin']*100:.2f} poin persen")
print(f"IK 95%           : [{hasil['bawah']*100:.2f}% , {hasil['atas']*100:.2f}%]")
```

> **Ketika syarat tidak terpenuhi** (proporsi sangat kecil atau sampel kecil), gunakan interval Wilson atau Clopper-Pearson:

```python
from statsmodels.stats.proportion import proportion_confint

# Kasus sulit: hanya 3 dari 200 pengguna mengalami galat
for metode in ["normal", "wilson", "beta"]:
    bawah, atas = proportion_confint(3, 200, alpha=0.05, method=metode)
    print(f"{metode:>8}: [{bawah*100:6.3f}% , {atas*100:6.3f}%]")
print("\n→ Metode 'normal' bisa memberi batas bawah negatif; Wilson lebih aman.")
```

---

### 5. Menentukan Ukuran Sampel

$$n = \left(\frac{z_{\alpha/2} \cdot \sigma}{E}\right)^2 \quad\text{(rata-rata)} \qquad n = \frac{z_{\alpha/2}^2 \cdot p(1-p)}{E^2} \quad\text{(proporsi)}$$

dengan E = margin galat yang diinginkan.

```python
import numpy as np
from scipy import stats

def n_untuk_rata_rata(sigma, margin, kepercayaan=0.95):
    z = stats.norm.ppf(1 - (1 - kepercayaan)/2)
    return int(np.ceil((z * sigma / margin) ** 2))

def n_untuk_proporsi(margin, p_dugaan=0.5, kepercayaan=0.95):
    """p_dugaan=0.5 memberi n terbesar (kasus paling aman)."""
    z = stats.norm.ppf(1 - (1 - kepercayaan)/2)
    return int(np.ceil(z**2 * p_dugaan * (1 - p_dugaan) / margin**2))

print("Survei kepuasan pengguna (proporsi):")
for me in [0.10, 0.05, 0.03, 0.02, 0.01]:
    print(f"  Margin ±{me*100:4.1f} poin → n = {n_untuk_proporsi(me):>6}")

print("\n→ Inilah alasan survei nasional memakai sekitar 1.100 responden")
print("  untuk margin ±3%, bukan puluhan ribu.")
```

---

## Kegiatan Pembelajaran

### Sebelum Kelas (Mandiri — 60 menit)

1. Membaca [Bab 9 buku ajar](../06-buku-ajar/bab-09-estimasi-interval-kepercayaan.md).
2. Menuliskan dalam kalimat sendiri: apa arti "interval kepercayaan 95%"? (Akan diperiksa dan dikoreksi di kelas.)

### Di Kelas (150 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–10' | Pembahasan Lab 09 |
| 10–35' | Kuliah: estimator dan sifatnya; demonstrasi bias penyebut n vs n−1 |
| 35–65' | Kuliah + latihan: interval kepercayaan rata-rata; kapan z, kapan t |
| 65–75' | Istirahat |
| 75–105' | **Simulasi cakupan:** 100 interval dari populasi yang sama; memeriksa tafsir yang benar |
| 105–125' | Kuliah + latihan: interval proporsi dan syarat kelayakannya |
| 125–145' | Latihan: perencanaan ukuran sampel untuk survei proyek |
| 145–150' | **Kuis 3** (Minggu 9–10) |

> **Catatan:** Kuis 3 dilaksanakan pada pertemuan ini, bobot 3,75%.

#### Kegiatan Koreksi Tafsir

Dosen mengumpulkan kalimat tafsir yang ditulis mahasiswa sebelum kelas, lalu membahas 4–5 contoh secara anonim: mana yang benar, mana yang keliru, dan mengapa. Kegiatan ini penting karena **salah tafsir interval kepercayaan adalah salah satu kekeliruan paling umum bahkan di kalangan peneliti**.

### Setelah Kelas (Mandiri — 180 menit)

1. Mengerjakan [Lab 10](../04-labs/lab-10-interval-kepercayaan-cakupan.md).
2. Mengerjakan Latihan Soal Bab 9.
3. **Proyek:** menyelesaikan analisis deskriptif dan visualisasi.

---

## Penugasan

| Kode | Tugas | Bobot | Batas Waktu |
|------|-------|-------|-------------|
| T-10 | Laporan Lab 10 — Interval kepercayaan dan simulasi cakupan | 1,92% | Sebelum kelas Minggu 11 |
| K-03 | Kuis 3 — Minggu 9–10 | 3,75% | Di kelas Minggu 10 |

---

## Rangkuman

1. **Estimator yang baik** bersifat tak bias, efisien, dan konsisten. Penyebut n−1 pada s² adalah yang membuatnya tak bias.
2. **Estimasi titik tanpa ukuran ketidakpastian adalah informasi yang tidak lengkap.**
3. Gunakan **interval-t** hampir selalu; interval-z hanya sah bila σ benar-benar diketahui.
4. Distribusi-t berekor lebih tebal daripada Normal; perbedaannya mengecil seiring bertambahnya df dan hampir hilang pada df ≈ 30.
5. **Tafsir yang benar:** yang memiliki sifat "95%" adalah **prosedurnya**, bukan interval tunggal yang sudah dihitung. μ adalah konstanta, bukan peubah acak.
6. Interval kepercayaan adalah tentang **rata-rata**, bukan tentang sebaran data individual.
7. Interval proporsi memerlukan syarat n·p̂ ≥ 10 dan n(1−p̂) ≥ 10; bila tidak terpenuhi gunakan Wilson atau Clopper-Pearson.
8. **Ukuran sampel tumbuh kuadratik** terhadap presisi yang diinginkan — memperkecil margin galat menjadi separuh memerlukan empat kali lipat data.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 9. Pearson.
2. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.), Bab 8. Wiley.
3. Hoekstra, R., et al. (2014). Robust misinterpretation of confidence intervals. *Psychonomic Bulletin & Review*, 21(5), 1157–1164.
4. Brown, L. D., Cai, T. T., & DasGupta, A. (2001). Interval Estimation for a Binomial Proportion. *Statistical Science*, 16(2), 101–133.
5. Dokumentasi statsmodels — `proportion_confint`. <https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportion_confint.html>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
