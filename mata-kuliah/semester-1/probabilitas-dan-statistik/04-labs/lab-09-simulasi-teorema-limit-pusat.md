# Lab 09: Simulasi Teorema Limit Pusat

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu** | 9 |
| **Durasi** | 180 menit (mandiri) |
| **Prasyarat** | Lab 07 selesai; UTS; materi Minggu 9 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | 1,92% |
| **Berkas data** | `waktu_respons_server.csv` |

---

## Tujuan Praktikum

1. Membedakan sebaran populasi, sebaran satu sampel, dan distribusi sampling.
2. Membuktikan Teorema Limit Pusat secara empiris dari berbagai bentuk populasi.
3. Menghitung galat baku dan menunjukkan hukum akar n.
4. Menentukan n minimum agar CLT berlaku untuk sebuah populasi.
5. Merencanakan ukuran sampel untuk mencapai presisi tertentu.

---

## Persiapan

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(42)
```

---

## Langkah-langkah

### Langkah 1: Tiga Sebaran yang Berbeda

```python
# =============================================
# LANGKAH 1: Membedakan tiga sebaran
# =============================================

# Populasi: sangat menceng (mirip waktu respons nyata)
POPULASI = rng.exponential(scale=200, size=200_000)

n = 40
satu_sampel = rng.choice(POPULASI, size=n, replace=False)
rata_rata_banyak_sampel = np.array([
    rng.choice(POPULASI, size=n, replace=False).mean() for _ in range(5000)
])

fig, axes = plt.subplots(1, 3, figsize=(16, 4.2))

axes[0].hist(POPULASI, bins=60, color="#7f8c8d", edgecolor="white")
axes[0].set_title(f"1. SEBARAN POPULASI\nN={len(POPULASI):,}, "
                  f"μ={POPULASI.mean():.1f}, σ={POPULASI.std():.1f}")
axes[0].set_xlim(0, 1200)

axes[1].hist(satu_sampel, bins=15, color="#e67e22", edgecolor="white")
axes[1].set_title(f"2. SEBARAN SATU SAMPEL\nn={n}, "
                  f"x̄={satu_sampel.mean():.1f}")
axes[1].set_xlim(0, 1200)

axes[2].hist(rata_rata_banyak_sampel, bins=50, color="steelblue",
             edgecolor="white")
axes[2].set_title(f"3. DISTRIBUSI SAMPLING x̄\n"
                  f"mean={rata_rata_banyak_sampel.mean():.1f}, "
                  f"SD={rata_rata_banyak_sampel.std(ddof=1):.1f}")

plt.tight_layout()
plt.show()

print("PERBANDINGAN:")
print(f"  μ populasi           : {POPULASI.mean():.4f}")
print(f"  Mean distribusi x̄    : {rata_rata_banyak_sampel.mean():.4f}")
print(f"  → Hampir identik. E[x̄] = μ (estimator tak bias).\n")
print(f"  σ populasi           : {POPULASI.std():.4f}")
print(f"  SD distribusi x̄      : {rata_rata_banyak_sampel.std(ddof=1):.4f}")
print(f"  σ/√n teoretis        : {POPULASI.std()/np.sqrt(n):.4f}")
print(f"  → Sesuai. SD(x̄) = σ/√n, jauh lebih kecil dari σ.")
```

> **Tulis interpretasi:** mengapa panel 3 jauh lebih sempit daripada panel 1? Apa artinya bagi keyakinan kita terhadap sebuah rata-rata sampel?

### Langkah 2: CLT dari Berbagai Bentuk Populasi

```python
# =============================================
# LANGKAH 2: CLT bekerja dari bentuk apa pun
# =============================================

def demo_clt(fungsi_populasi, nama, ukuran=(1, 5, 30, 100), ulangan=5000):
    """Menunjukkan CLT dari sebuah sebaran populasi."""
    fig, axes = plt.subplots(1, len(ukuran) + 1, figsize=(19, 3.5))

    populasi = fungsi_populasi(50_000)
    axes[0].hist(populasi, bins=50, color="#7f8c8d", edgecolor="white")
    axes[0].set_title(f"POPULASI\n{nama}")
    axes[0].set_yticks([])

    for ax, n in zip(axes[1:], ukuran):
        rata = np.array([fungsi_populasi(n).mean() for _ in range(ulangan)])
        _, p_norm = stats.shapiro(rata[:500])
        ax.hist(rata, bins=50, color="steelblue", edgecolor="white")
        ax.set_title(f"n = {n}\nShapiro p = {p_norm:.3f}")
        ax.set_yticks([])

    plt.suptitle(f"Teorema Limit Pusat — {nama}", y=1.06)
    plt.tight_layout()
    plt.show()

demo_clt(lambda n: rng.exponential(2, n), "Eksponensial (menceng kanan)")
demo_clt(lambda n: rng.uniform(0, 10, n), "Uniform (datar)")
demo_clt(lambda n: rng.binomial(1, 0.15, n), "Bernoulli p=0,15 (dua nilai saja)")
demo_clt(lambda n: np.concatenate([rng.normal(2, 0.4, n//2),
                                   rng.normal(9, 0.4, n - n//2)]),
         "Bimodal (dua puncak)")
```

> **Tulis interpretasi:** untuk masing-masing populasi, pada n berapa distribusi sampling mulai tampak Normal? Populasi mana yang memerlukan n paling besar?

### Langkah 3: Menentukan n Minimum untuk CLT

```python
# =============================================
# LANGKAH 3: Berapa n yang "cukup besar"?
# =============================================

def n_minimum_clt(fungsi_populasi, nama, ulangan=2000, ambang_p=0.05):
    """Mencari n terkecil agar distribusi sampling lolos uji kenormalan."""
    print(f"\n{nama}")
    print(f"{'n':>5}  {'Shapiro p':>12}  {'Skew x̄':>9}  Status")
    n_lolos = None
    for n in [2, 5, 10, 15, 20, 30, 50, 80, 120, 200]:
        rata = np.array([fungsi_populasi(n).mean() for _ in range(ulangan)])
        _, p = stats.shapiro(rata[:500])
        sk = stats.skew(rata)
        status = "Normal" if p > ambang_p else "belum"
        if p > ambang_p and n_lolos is None:
            n_lolos = n
            status += "  ← n minimum"
        print(f"{n:>5}  {p:>12.4f}  {sk:>9.4f}  {status}")
    return n_lolos

n_minimum_clt(lambda n: rng.exponential(2, n), "Eksponensial")
n_minimum_clt(lambda n: rng.lognormal(0, 1.6, n), "Lognormal (sangat menceng)")
n_minimum_clt(lambda n: rng.uniform(0, 1, n), "Uniform")
```

> **Tulis interpretasi:** apakah aturan praktis "n ≥ 30" berlaku untuk semua kasus di atas? Untuk populasi mana aturan itu **tidak** memadai?

### Langkah 4: Hukum Akar n

```python
# =============================================
# LANGKAH 4: Galat baku dan hukum akar n
# =============================================

sigma = POPULASI.std()

print(f"σ populasi = {sigma:.4f}\n")
print(f"{'n':>7}  {'SE teoretis':>13}  {'SE empiris':>13}  {'Rasio thd n=1':>15}")
for n in [1, 4, 16, 64, 256, 1024]:
    se_teori = sigma / np.sqrt(n)
    rata = np.array([rng.choice(POPULASI, n, replace=False).mean()
                     for _ in range(3000)])
    se_empiris = rata.std(ddof=1)
    print(f"{n:>7}  {se_teori:>13.4f}  {se_empiris:>13.4f}  "
          f"{'1/' + str(int(np.sqrt(n))):>15}")

print("\n→ Melipatempatkan n hanya MEMBAGI DUA galat baku.")
print("→ Inilah alasan survei nasional memakai ~1.200 responden,")
print("  bukan 100.000 — hasil tambahannya makin kecil.")
```

```python
# Visualisasi kurva penurunan
n_range = np.arange(1, 1001)
se_range = sigma / np.sqrt(n_range)

fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
axes[0].plot(n_range, se_range, linewidth=2, color="steelblue")
axes[0].set_xlabel("Ukuran sampel (n)")
axes[0].set_ylabel("Galat baku σ/√n")
axes[0].set_title("Penurunan galat baku")
axes[0].grid(alpha=0.3)

axes[1].plot(n_range, se_range, linewidth=2, color="steelblue")
axes[1].set_xscale("log")
axes[1].set_yscale("log")
axes[1].set_xlabel("Ukuran sampel (skala log)")
axes[1].set_ylabel("Galat baku (skala log)")
axes[1].set_title("Skala log-log: garis lurus dengan kemiringan −0,5")
axes[1].grid(alpha=0.3, which="both")

plt.tight_layout()
plt.show()
```

### Langkah 5: Perencanaan Ukuran Sampel

```python
# =============================================
# LANGKAH 5: Berapa data yang saya butuhkan?
# =============================================

def n_untuk_presisi(sigma, margin, kepercayaan=0.95):
    """n minimum agar margin galat tidak melebihi nilai tertentu."""
    z = stats.norm.ppf(1 - (1 - kepercayaan) / 2)
    return int(np.ceil((z * sigma / margin) ** 2))

srv = pd.read_csv("waktu_respons_server.csv")
sigma_taksiran = srv["waktu_ms"].std(ddof=1)

print(f"Dari data pendahuluan: s = {sigma_taksiran:.2f} ms\n")
print(f"{'Margin galat':>14}  {'n (90%)':>9}  {'n (95%)':>9}  {'n (99%)':>9}")
for me in [100, 50, 20, 10, 5]:
    print(f"{me:>11} ms  "
          f"{n_untuk_presisi(sigma_taksiran, me, 0.90):>9,}  "
          f"{n_untuk_presisi(sigma_taksiran, me, 0.95):>9,}  "
          f"{n_untuk_presisi(sigma_taksiran, me, 0.99):>9,}")

print("\n→ Memperkecil margin galat menjadi separuh")
print("  memerlukan EMPAT KALI LIPAT data.")
```

---

## Tantangan Tambahan

### Tantangan 1: CLT untuk Proporsi

CLT juga berlaku untuk proporsi sampel p̂.

```python
# TUGAS ANDA
# 1. Bangkitkan populasi Bernoulli dengan p = 0,15
# 2. Untuk n = 5, 20, 50, 100, 500: ambil 5000 sampel, hitung p̂ tiap sampel
# 3. Buat histogram distribusi sampling p̂
# 4. Bandingkan SD empiris dengan rumus teoretis √(p(1−p)/n)
# 5. Pada n berapa distribusi p̂ mulai tampak Normal?
#
# Pertanyaan: syarat umum adalah n·p ≥ 10 DAN n(1−p) ≥ 10.
# Apakah hasil simulasi Anda sesuai dengan syarat itu?
```

### Tantangan 2: Ketika CLT Gagal

CLT mensyaratkan populasi memiliki **varians berhingga**. Distribusi Cauchy tidak memenuhinya.

```python
# TUGAS ANDA
# 1. Bangkitkan sampel dari distribusi Cauchy: rng.standard_cauchy(n)
# 2. Ulangi proses CLT untuk n = 1, 10, 100, 1000
# 3. Amati: apakah distribusi sampling menyempit seiring n bertambah?
# 4. Bandingkan dengan Normal
#
# Pertanyaan: mengapa rata-rata sampel dari Cauchy tidak pernah
# "menstabil"? Apa pelajarannya tentang batas keberlakuan CLT?
```

### Tantangan 3: Simulasi Bootstrap

Bootstrap adalah cara mendapatkan distribusi sampling **tanpa** mengambil sampel baru — cukup mengambil ulang dari sampel yang ada.

```python
# TUGAS ANDA
# 1. Ambil satu sampel berukuran 60 dari waktu_respons_server.csv
# 2. Lakukan 10.000 pengambilan ulang (dengan pengembalian) dari sampel itu
# 3. Hitung rata-rata tiap pengambilan ulang → distribusi bootstrap
# 4. Bandingkan SD distribusi bootstrap dengan s/√n
# 5. Bandingkan interval persentil bootstrap [2,5%, 97,5%] dengan
#    interval kepercayaan-t biasa
#
# Pertanyaan: kapan bootstrap lebih berguna daripada rumus analitis?
```

---

## Refleksi

1. Jelaskan dengan kalimat sendiri perbedaan σ dan σ/√n.
2. Mengapa CLT disebut "tulang punggung inferensi statistika"?
3. Apa risiko memakai aturan "n ≥ 30" tanpa memeriksa bentuk populasinya?

---

## AI Usage Log

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |

> Nama: ______________  NIM: ______________

---

## Checklist Penyelesaian

- [ ] Notebook dinamai `Lab09_NIM_NamaLengkap.ipynb`
- [ ] *Seed* ditetapkan di awal
- [ ] Langkah 1–5 selesai
- [ ] Setiap simulasi disertai interpretasi
- [ ] Ketiga tantangan dikerjakan
- [ ] Refleksi terisi
- [ ] AI Usage Log terisi
- [ ] Diunggah ke LMS

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
