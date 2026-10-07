# Lab 10: Interval Kepercayaan dan Simulasi Cakupan

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu** | 10 |
| **Durasi** | 180 menit (mandiri) |
| **Prasyarat** | Lab 09 selesai; materi Minggu 10 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | 1,92% |
| **Berkas data** | `nilai_mahasiswa_if.csv`, `ispu_jakarta_2025.csv` |

---

## Tujuan Praktikum

1. Menghitung interval kepercayaan rata-rata (z dan t) dan proporsi.
2. Membuktikan makna "95% kepercayaan" melalui simulasi cakupan.
3. Menunjukkan bahwa tafsir "probabilitas μ berada di interval" keliru.
4. Membandingkan metode interval proporsi ketika syarat tidak terpenuhi.
5. Merencanakan ukuran sampel survei.

---

## Persiapan

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.proportion import proportion_confint

rng = np.random.default_rng(42)
```

---

## Langkah-langkah

### Langkah 1: Estimator Tak Bias — Membuktikan Koreksi Bessel

```python
# =============================================
# LANGKAH 1: Mengapa penyebut n−1
# =============================================

MU, SIGMA = 100, 15
ulangan = 100_000

print(f"Varians populasi sebenarnya: σ² = {SIGMA**2}\n")
print(f"{'n':>5}  {'E[s² dgn n]':>13}  {'E[s² dgn n−1]':>15}  {'Bias (n)':>10}")

for n in [3, 5, 10, 30, 100]:
    var_n, var_n1 = [], []
    for _ in range(ulangan // n):
        s = rng.normal(MU, SIGMA, n)
        var_n.append(s.var(ddof=0))
        var_n1.append(s.var(ddof=1))
    e_n, e_n1 = np.mean(var_n), np.mean(var_n1)
    print(f"{n:>5}  {e_n:>13.2f}  {e_n1:>15.2f}  {e_n - SIGMA**2:>10.2f}")

print(f"\n→ Penyebut n selalu MEREMEHKAN varians populasi.")
print(f"→ Biasnya paling parah pada n kecil, dan mengecil seiring n bertambah.")
```

### Langkah 2: Interval Kepercayaan Rata-Rata

```python
# =============================================
# LANGKAH 2: IK rata-rata — z vs t
# =============================================

def ik_rata_rata(data, kepercayaan=0.95, sigma_diketahui=None):
    """Interval kepercayaan rata-rata. Memakai z bila σ diketahui, t bila tidak."""
    data = np.asarray(data)
    data = data[~np.isnan(data)]
    n = len(data)
    x_bar = data.mean()
    alpha = 1 - kepercayaan

    if sigma_diketahui is not None:
        se = sigma_diketahui / np.sqrt(n)
        kritis = stats.norm.ppf(1 - alpha/2)
        metode, df = "z", None
    else:
        s = data.std(ddof=1)
        se = s / np.sqrt(n)
        kritis = stats.t.ppf(1 - alpha/2, df=n-1)
        metode, df = "t", n - 1

    margin = kritis * se
    return {
        "metode": metode, "n": n, "df": df, "mean": x_bar,
        "se": se, "kritis": kritis, "margin": margin,
        "bawah": x_bar - margin, "atas": x_bar + margin,
    }

df = pd.read_csv("nilai_mahasiswa_if.csv")
jam = df["jam_belajar"].dropna()

hasil_t = ik_rata_rata(jam)
print("INTERVAL KEPERCAYAAN 95% — jam belajar per minggu")
for k, v in hasil_t.items():
    print(f"  {k:>8}: {v}" if not isinstance(v, float) else f"  {k:>8}: {v:.4f}")

print(f"\n  IK 95%: [{hasil_t['bawah']:.3f} , {hasil_t['atas']:.3f}] jam/minggu")

# Membandingkan beberapa tingkat kepercayaan
print(f"\n{'Kepercayaan':>12}  {'Nilai kritis':>13}  {'Margin':>9}  Interval")
for kep in [0.80, 0.90, 0.95, 0.99, 0.999]:
    h = ik_rata_rata(jam, kepercayaan=kep)
    print(f"{kep*100:>11.1f}%  {h['kritis']:>13.4f}  {h['margin']:>9.4f}  "
          f"[{h['bawah']:.3f} , {h['atas']:.3f}]")

print("\n→ Makin tinggi kepercayaan, makin LEBAR intervalnya.")
print("  Kepastian dan presisi saling berlawanan.")
```

```python
# Perbandingan nilai kritis t dan z
print(f"\n{'df':>6}  {'t(0,025)':>10}  {'z(0,025)':>10}  {'Selisih':>9}")
z = stats.norm.ppf(0.975)
for d in [1, 2, 5, 10, 20, 30, 50, 100, 500]:
    t = stats.t.ppf(0.975, d)
    print(f"{d:>6}  {t:>10.4f}  {z:>10.4f}  {t - z:>9.4f}")
print("\n→ Pada df ≈ 30, keduanya hampir tidak terbedakan.")
```

### Langkah 3: Simulasi Cakupan — Membuktikan Tafsir yang Benar

```python
# =============================================
# LANGKAH 3: Apa arti sebenarnya "95% kepercayaan"
# =============================================

MU_SEBENARNYA, SIGMA = 100, 15
n, n_interval = 30, 100

plt.figure(figsize=(11, 8))
memuat = 0

for i in range(n_interval):
    sampel = rng.normal(MU_SEBENARNYA, SIGMA, n)
    h = ik_rata_rata(sampel)
    cocok = h["bawah"] <= MU_SEBENARNYA <= h["atas"]
    memuat += cocok
    warna = "#2980b9" if cocok else "#c0392b"
    plt.plot([h["bawah"], h["atas"]], [i, i], color=warna, linewidth=1.5)
    plt.plot(h["mean"], i, "o", color=warna, markersize=2.5)

plt.axvline(MU_SEBENARNYA, color="black", linestyle="--", linewidth=2,
            label=f"μ sebenarnya = {MU_SEBENARNYA}")
plt.xlabel("Nilai")
plt.ylabel("Ulangan ke-")
plt.title(f"100 interval kepercayaan 95% dari populasi yang SAMA\n"
          f"{memuat} memuat μ · {n_interval-memuat} MELESET (merah)")
plt.legend()
plt.tight_layout()
plt.show()

print(f"Cakupan empiris: {memuat}/{n_interval} = {memuat/n_interval*100:.1f}%")
```

```python
# Cakupan pada skala besar
def uji_cakupan(n, kepercayaan=0.95, ulangan=10_000):
    memuat = 0
    for _ in range(ulangan):
        s = rng.normal(MU_SEBENARNYA, SIGMA, n)
        h = ik_rata_rata(s, kepercayaan)
        if h["bawah"] <= MU_SEBENARNYA <= h["atas"]:
            memuat += 1
    return memuat / ulangan

print(f"\n{'n':>6}  {'Target':>8}  {'Cakupan empiris':>17}")
for n_ in [5, 10, 30, 100]:
    for kep in [0.90, 0.95, 0.99]:
        c = uji_cakupan(n_, kep, 5000)
        print(f"{n_:>6}  {kep*100:>7.0f}%  {c*100:>16.2f}%")
```

> **Tulis interpretasi:** tuliskan dengan kalimat sendiri apa arti "95% kepercayaan" berdasarkan simulasi ini. Lalu tuliskan juga **tiga tafsir yang SALAH** dan jelaskan mengapa masing-masing salah.

### Langkah 4: Interval Kepercayaan Proporsi

```python
# =============================================
# LANGKAH 4: IK proporsi dan syarat kelayakannya
# =============================================

def ik_proporsi(berhasil, n, kepercayaan=0.95):
    """IK proporsi dengan tiga metode, plus pemeriksaan syarat."""
    p_hat = berhasil / n
    np_ = n * p_hat
    nq_ = n * (1 - p_hat)
    layak = np_ >= 10 and nq_ >= 10

    print(f"Data: {berhasil}/{n} = {p_hat:.4f} ({p_hat*100:.2f}%)")
    print(f"Syarat: n·p̂ = {np_:.1f}, n(1−p̂) = {nq_:.1f} "
          f"→ {'TERPENUHI' if layak else 'TIDAK TERPENUHI'}\n")
    print(f"{'Metode':>12}  {'Batas bawah':>13}  {'Batas atas':>12}  {'Lebar':>8}")
    for metode, label in [("normal", "Wald"), ("wilson", "Wilson"),
                          ("beta", "Clopper-P")]:
        b, a = proportion_confint(berhasil, n, alpha=1-kepercayaan, method=metode)
        print(f"{label:>12}  {b*100:>12.3f}%  {a*100:>11.3f}%  {(a-b)*100:>7.3f}")
    if not layak:
        print("\n→ Syarat tidak terpenuhi. Metode Wald tidak andal;")
        print("  gunakan Wilson atau Clopper-Pearson.")

print("KASUS 1 — syarat terpenuhi:")
ik_proporsi(148, 400)

print("\nKASUS 2 — proporsi sangat kecil:")
ik_proporsi(3, 200)

print("\nKASUS 3 — proporsi ekstrem:")
ik_proporsi(0, 150)
```

> **Tulis interpretasi:** pada Kasus 3 (nol keberhasilan), apa yang dihasilkan metode Wald? Mengapa hasil itu tidak masuk akal? Metode mana yang memberi jawaban yang layak?

### Langkah 5: Perencanaan Ukuran Sampel Survei

```python
# =============================================
# LANGKAH 5: Perencanaan survei
# =============================================

def n_survei_proporsi(margin, p_dugaan=0.5, kepercayaan=0.95):
    """p_dugaan=0.5 memberi n terbesar (paling konservatif)."""
    z = stats.norm.ppf(1 - (1 - kepercayaan)/2)
    return int(np.ceil(z**2 * p_dugaan * (1 - p_dugaan) / margin**2))

print("SURVEI KEPUASAN MAHASISWA")
print(f"{'Margin galat':>14}  {'n (90%)':>9}  {'n (95%)':>9}  {'n (99%)':>9}")
for me in [0.10, 0.05, 0.03, 0.02, 0.01]:
    print(f"{me*100:>11.1f} pp  "
          f"{n_survei_proporsi(me, kepercayaan=0.90):>9,}  "
          f"{n_survei_proporsi(me, kepercayaan=0.95):>9,}  "
          f"{n_survei_proporsi(me, kepercayaan=0.99):>9,}")

print("\nPengaruh dugaan awal p:")
print(f"{'p dugaan':>10}  {'n untuk margin ±3%':>20}")
for p in [0.05, 0.10, 0.25, 0.50, 0.75, 0.90]:
    print(f"{p:>10.2f}  {n_survei_proporsi(0.03, p):>20,}")
print("\n→ p = 0,50 memberi n TERBESAR. Bila tidak ada dugaan awal,")
print("  pakai 0,50 agar aman.")
```

---

## Tantangan Tambahan

### Tantangan 1: Cakupan pada Populasi Tidak Normal

```python
# TUGAS ANDA
# Ulangi simulasi cakupan (Langkah 3), tetapi dengan populasi:
#   (a) Eksponensial(scale=100)
#   (b) Lognormal(0, 1.5)
# untuk n = 5, 15, 30, 100.
#
# Pertanyaan: pada n berapa cakupan empiris mendekati 95%?
# Apakah IK-t tetap andal untuk populasi yang sangat menceng?
```

### Tantangan 2: Interval Kepercayaan Kualitas Udara

```python
# TUGAS ANDA
# Muat ispu_jakarta_2025.csv
# 1. Hitung IK 95% untuk rata-rata PM2.5 secara keseluruhan
# 2. Hitung IK 95% terpisah untuk tiap stasiun pemantauan
# 3. Buat grafik "forest plot": titik = rata-rata, garis = IK
# 4. Apakah ada stasiun yang intervalnya TIDAK bertumpang tindih
#    dengan stasiun lain?
#
# Pertanyaan: bila dua interval tidak bertumpang tindih, bolehkah
# langsung disimpulkan keduanya berbeda signifikan? (Petunjuk: tidak
# selalu — ini akan dijawab tuntas di Minggu 12.)
```

### Tantangan 3: Interval Bootstrap

```python
# TUGAS ANDA
# 1. Ambil sampel 50 nilai dari jam_belajar
# 2. Lakukan 10.000 bootstrap, hitung rata-rata tiap kali
# 3. Interval persentil bootstrap: [2,5%, 97,5%]
# 4. Bandingkan dengan IK-t biasa
# 5. Ulangi untuk MEDIAN — mengapa IK-t tidak bisa dipakai untuk median?
#
# Pertanyaan: apa keunggulan bootstrap untuk statistik yang tidak
# punya rumus interval analitis?
```

---

## Refleksi

1. Mengapa mengatakan "ada 95% probabilitas μ di interval ini" keliru?
2. Mengapa interval yang lebih lebar justru lebih "aman"?
3. Dalam laporan kepada pihak non-teknis, bagaimana Anda menjelaskan interval kepercayaan?

---

## AI Usage Log

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |

> Nama: ______________  NIM: ______________

---

## Checklist Penyelesaian

- [ ] Notebook dinamai `Lab10_NIM_NamaLengkap.ipynb`
- [ ] Langkah 1–5 selesai
- [ ] Langkah 3 memuat tafsir yang benar **dan** tiga tafsir yang salah
- [ ] Ketiga tantangan dikerjakan
- [ ] Refleksi terisi
- [ ] AI Usage Log terisi
- [ ] Diunggah ke LMS

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
