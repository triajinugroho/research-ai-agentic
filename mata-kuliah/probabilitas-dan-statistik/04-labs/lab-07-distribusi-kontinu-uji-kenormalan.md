# Lab 07: Distribusi Kontinu dan Uji Kenormalan

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu** | 7 |
| **Durasi** | 180 menit (mandiri) |
| **Prasyarat** | Lab 06 selesai; materi Minggu 7 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | 1,92% |
| **Berkas data** | `nilai_mahasiswa_if.csv`, `waktu_respons_server.csv`, `ispu_jakarta_2025.csv` |

---

## Tujuan Praktikum

1. Memakai distribusi Uniform, Eksponensial, dan Normal dengan `scipy.stats`.
2. Menghitung probabilitas Normal dengan skor-z, manual maupun komputasional.
3. Memeriksa kenormalan dengan histogram, Q-Q plot, dan uji formal.
4. Menjelaskan mengapa uji kenormalan formal menyesatkan pada sampel besar.
5. Mengenali data yang **tidak** Normal dan memilih penanganannya.

---

## Persiapan

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(42)
```

> **Jebakan parameter `scipy`.** Perhatikan baik-baik:
> - `stats.norm(loc=μ, scale=σ)` — `scale` adalah **simpangan baku**, bukan varians.
> - `stats.expon(scale=1/λ)` — `scale` adalah **1/λ**, bukan λ.
> - `stats.uniform(loc=a, scale=b−a)` — `scale` adalah **lebar selang**, bukan batas atas.
>
> Kesalahan ini tidak menghasilkan galat — hanya angka yang keliru secara diam-diam. Selalu verifikasi dengan `.mean()`.

---

## Langkah-langkah

### Langkah 1: PDF vs PMF

```python
# =============================================
# LANGKAH 1: Mengapa P(X = x) = 0 pada kontinu
# =============================================

X = stats.norm(loc=100, scale=15)

print("Pada peubah acak KONTINU:")
print(f"  P(X = 100) secara teoretis = 0")
print(f"  pdf(100) = {X.pdf(100):.6f}  ← ini BUKAN probabilitas!")
print(f"\nYang bermakna adalah probabilitas pada SELANG:")
print(f"  P(99 < X < 101)     = {X.cdf(101) - X.cdf(99):.6f}")
print(f"  P(99.9 < X < 100.1) = {X.cdf(100.1) - X.cdf(99.9):.6f}")
print(f"  P(99.99 < X < 100.01) = {X.cdf(100.01) - X.cdf(99.99):.8f}")
print("\n→ Makin sempit selangnya, makin mendekati nol.")

# Membuktikan PDF boleh > 1
Y = stats.norm(loc=0, scale=0.1)
print(f"\nPDF boleh lebih dari 1:")
print(f"  Normal(μ=0, σ=0.1), pdf(0) = {Y.pdf(0):.4f}")
print(f"  Tetapi luas totalnya tetap = {Y.cdf(np.inf) - Y.cdf(-np.inf):.6f}")
```

### Langkah 2: Distribusi Uniform dan Eksponensial

```python
# =============================================
# LANGKAH 2: Uniform dan Eksponensial
# =============================================

# Uniform: jitter acak 0–500 ms pada strategi retry
a, b = 0, 500
U = stats.uniform(loc=a, scale=b - a)

print("UNIFORM(0, 500) — jitter retry")
print(f"  E[X]  = {U.mean():.2f} ms   (= (a+b)/2 = {(a+b)/2})")
print(f"  SD(X) = {U.std():.2f} ms")
print(f"  P(X ≤ 100)       = {U.cdf(100):.4f}")
print(f"  P(200 ≤ X ≤ 300) = {U.cdf(300) - U.cdf(200):.4f}")

# Eksponensial: waktu antar permintaan
lam = 8   # 8 permintaan per detik
E = stats.expon(scale=1/lam)      # PERHATIKAN: scale = 1/λ

print(f"\nEKSPONENSIAL(λ = {lam}) — waktu antar permintaan")
print(f"  Verifikasi scale benar: E[X] = {E.mean():.6f} detik "
      f"(harus = 1/λ = {1/lam:.6f})")
print(f"  Rata-rata jeda   = {E.mean()*1000:.2f} ms")
print(f"  P(jeda < 50 ms)  = {E.cdf(0.050):.4f}")
print(f"  P(jeda > 500 ms) = {E.sf(0.500):.6f}")
print(f"  Persentil ke-95  = {E.ppf(0.95)*1000:.2f} ms")

# Sifat tanpa memori versi kontinu
print(f"\n  Sifat tanpa memori:")
print(f"    P(X > 0.2)           = {E.sf(0.2):.8f}")
print(f"    P(X > 0.3 | X > 0.1) = {E.sf(0.3)/E.sf(0.1):.8f}")
```

```python
# Visualisasi hubungan Poisson–Eksponensial
fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))

k = np.arange(0, 22)
axes[0].bar(k, stats.poisson.pmf(k, lam), color="steelblue", edgecolor="white")
axes[0].set_title(f"POISSON(λ={lam})\n'berapa kejadian per detik?'")
axes[0].set_xlabel("Jumlah kejadian")

x = np.linspace(0, 0.8, 400)
axes[1].plot(x * 1000, E.pdf(x) / 1000, linewidth=2, color="#e67e22")
axes[1].fill_between(x * 1000, E.pdf(x) / 1000, alpha=0.3, color="#e67e22")
axes[1].set_title(f"EKSPONENSIAL(λ={lam})\n'berapa lama sampai kejadian berikutnya?'")
axes[1].set_xlabel("Waktu tunggu (ms)")

plt.suptitle("Dua sisi mata uang yang sama", y=1.03)
plt.tight_layout()
plt.show()
```

### Langkah 3: Distribusi Normal dan Skor-z

```python
# =============================================
# LANGKAH 3: Normal, aturan empiris, skor-z
# =============================================

Z = stats.norm(0, 1)

print("ATURAN EMPIRIS 68–95–99,7:")
for k in [1, 2, 3]:
    p = Z.cdf(k) - Z.cdf(-k)
    print(f"  μ ± {k}σ : {p:.6f}  ({p*100:.2f}%)")

# Kasus nilai UAS
mu, sigma = 72, 11
X = stats.norm(mu, sigma)

print(f"\nNILAI UAS ~ Normal(μ={mu}, σ={sigma})")
for nilai in [50, 60, 72, 85, 95]:
    z = (nilai - mu) / sigma
    print(f"  Nilai {nilai:>3}: z = {z:>6.3f}, "
          f"persentil = {X.cdf(nilai)*100:>5.1f}, "
          f"P(X > {nilai}) = {X.sf(nilai):.4f}")

print(f"\nAmbang batas:")
print(f"  10% teratas  : nilai ≥ {X.ppf(0.90):.2f}")
print(f"  25% teratas  : nilai ≥ {X.ppf(0.75):.2f}")
print(f"  25% terbawah : nilai ≤ {X.ppf(0.25):.2f}")
```

```python
# Membandingkan prestasi lintas mata kuliah dengan skor-z
mahasiswa = [
    {"nama": "Ahmad", "mk": "Statistika", "nilai": 85, "mu": 75, "sigma": 8},
    {"nama": "Budi",  "mk": "Kalkulus",   "nilai": 78, "mu": 65, "sigma": 6},
    {"nama": "Citra", "mk": "Dasprog",    "nilai": 90, "mu": 82, "sigma": 12},
]

print("\nPERBANDINGAN PRESTASI LINTAS MATA KULIAH:")
print(f"{'Nama':<8} {'MK':<12} {'Nilai':>6} {'μ':>5} {'σ':>5} {'z':>8} {'Persentil':>10}")
print("-" * 60)
for m in mahasiswa:
    z = (m["nilai"] - m["mu"]) / m["sigma"]
    pers = stats.norm.cdf(z) * 100
    print(f"{m['nama']:<8} {m['mk']:<12} {m['nilai']:>6} {m['mu']:>5} "
          f"{m['sigma']:>5} {z:>8.3f} {pers:>9.1f}%")

terbaik = max(mahasiswa, key=lambda m: (m["nilai"]-m["mu"])/m["sigma"])
print(f"\n→ Prestasi relatif terbaik: {terbaik['nama']}")
print("  Nilai mentah tidak bisa dibandingkan; skor-z bisa.")
```

### Langkah 4: Memeriksa Kenormalan — Tiga Cara

```python
# =============================================
# LANGKAH 4: Pemeriksaan kenormalan
# =============================================

def periksa_kenormalan(data, nama):
    """Pemeriksaan kenormalan dengan tiga pendekatan."""
    data = np.asarray(data)
    data = data[~np.isnan(data)]
    n = len(data)

    fig, axes = plt.subplots(1, 3, figsize=(16, 4.2))

    # (1) Histogram dengan kurva Normal
    axes[0].hist(data, bins=30, density=True, color="steelblue",
                 edgecolor="white", alpha=0.85)
    x = np.linspace(data.min(), data.max(), 300)
    axes[0].plot(x, stats.norm.pdf(x, data.mean(), data.std(ddof=1)),
                 color="#c0392b", linewidth=2, label="Normal teoretis")
    axes[0].set_title(f"{nama}\nHistogram vs Normal")
    axes[0].legend()

    # (2) Q-Q plot
    stats.probplot(data, dist="norm", plot=axes[1])
    axes[1].set_title("Q-Q Plot\n(titik harus di garis)")

    # (3) Boxplot
    axes[2].boxplot(data, vert=True)
    axes[2].set_title("Boxplot\n(simetri dan pencilan)")

    plt.tight_layout()
    plt.show()

    # Statistik bentuk
    kemencengan = stats.skew(data)
    kurtosis = stats.kurtosis(data)
    print(f"=== {nama} (n = {n}) ===")
    print(f"  Kemencengan : {kemencengan:>8.4f}   (Normal ≈ 0)")
    print(f"  Kurtosis    : {kurtosis:>8.4f}   (Normal ≈ 0)")

    # Uji formal
    if 3 <= n <= 5000:
        w, p_sw = stats.shapiro(data)
        print(f"  Shapiro-Wilk: W = {w:.4f}, p = {p_sw:.8f}")
    else:
        sub = rng.choice(data, 5000, replace=False)
        w, p_sw = stats.shapiro(sub)
        print(f"  Shapiro-Wilk (subsampel 5000): W = {w:.4f}, p = {p_sw:.8f}")

    d, p_ks = stats.kstest(data, "norm", args=(data.mean(), data.std(ddof=1)))
    print(f"  Kolmogorov-S: D = {d:.4f}, p = {p_ks:.8f}")

    # Kesimpulan yang bijak
    if abs(kemencengan) < 0.5 and abs(kurtosis) < 1:
        print("  → Bentuk mendekati Normal secara praktis.")
    else:
        print("  → Menyimpang dari Normal. Periksa Q-Q plot untuk menilai seberapa jauh.")
    print()

df = pd.read_csv("nilai_mahasiswa_if.csv")
srv = pd.read_csv("waktu_respons_server.csv")

periksa_kenormalan(df["nilai_uas"], "Nilai UAS")
periksa_kenormalan(srv["waktu_ms"], "Waktu Respons Server")
```

> **Tulis interpretasi:** bandingkan Q-Q plot kedua data. Yang mana yang mendekati Normal? Bagaimana bentuk Q-Q plot data yang menceng kanan?

### Langkah 5: Mengapa Uji Formal Menyesatkan pada Sampel Besar

```python
# =============================================
# LANGKAH 5: Keterbatasan uji kenormalan formal
# =============================================

# Data yang HAMPIR Normal, tetapi tidak persis
# (Normal dengan sedikit kemencengan)
print("Data hampir Normal (kemencengan sangat kecil):")
print(f"{'n':>8}  {'Shapiro p-value':>17}  {'Kesimpulan uji':>18}")

for n in [30, 100, 500, 2000, 5000]:
    sampel = stats.skewnorm.rvs(a=0.35, size=n, random_state=42)
    _, p = stats.shapiro(sampel)
    kesimpulan = "tidak menolak" if p > 0.05 else "MENOLAK kenormalan"
    print(f"{n:>8}  {p:>17.8f}  {kesimpulan:>18}")

print("\n→ Data yang SAMA bentuknya ditolak kenormalannya begitu n besar.")
print("→ Ini bukan karena datanya berubah, tetapi karena uji formal")
print("  makin peka terhadap penyimpangan sekecil apa pun.")
print("\n→ PERTANYAAN YANG TEPAT bukan 'apakah persis Normal?'")
print("  melainkan 'apakah penyimpangannya cukup kecil sehingga")
print("  metode yang mengandaikan kenormalan masih layak dipakai?'")
print("→ Q-Q plot lebih informatif daripada nilai p.")
```

### Langkah 6: Menangani Data yang Tidak Normal

```python
# =============================================
# LANGKAH 6: Transformasi data menceng
# =============================================

waktu = srv["waktu_ms"].values
waktu = waktu[waktu > 0]

fig, axes = plt.subplots(2, 3, figsize=(16, 8))

transformasi = [
    ("Asli", waktu),
    ("log(x)", np.log(waktu)),
    ("√x", np.sqrt(waktu)),
]

for kol, (nama, data_t) in enumerate(transformasi):
    axes[0, kol].hist(data_t, bins=40, color="steelblue", edgecolor="white")
    axes[0, kol].set_title(f"{nama}\nskew = {stats.skew(data_t):.3f}")
    stats.probplot(data_t, dist="norm", plot=axes[1, kol])
    axes[1, kol].set_title(f"Q-Q Plot — {nama}")

plt.tight_layout()
plt.show()

print("Kemencengan setelah transformasi:")
for nama, data_t in transformasi:
    print(f"  {nama:>8}: {stats.skew(data_t):>8.4f}")
print("\n→ Transformasi log sering efektif untuk data menceng kanan.")
print("→ TETAPI: setelah transformasi, kesimpulan berlaku pada skala")
print("  yang ditransformasi. Menafsirkannya kembali ke skala asli")
print("  memerlukan kehati-hatian (mean log ≠ log mean).")
```

---

## Tantangan Tambahan

### Tantangan 1: Membaca Tabel Normal Secara Manual

UTS bersifat *closed book* tanpa komputer. Latih keterampilan membaca tabel.

Waktu kompilasi proyek ~ Normal(μ = 45 detik, σ = 8 detik). Hitung **secara manual dengan tabel** lalu verifikasi dengan Python:

1. P(X < 50)
2. P(X > 60)
3. P(38 < X < 52)
4. Waktu yang hanya dilampaui 5% kompilasi terlambat
5. Skor-z untuk kompilasi 70 detik — wajar atau tidak?

```python
# TUGAS ANDA: verifikasi kelima jawaban manual Anda
X = stats.norm(45, 8)
# ...
```

**Laporkan:** tabel perbandingan jawaban manual vs Python, dan selisihnya. Jelaskan sumber selisih (pembulatan tabel).

### Tantangan 2: Analisis Kualitas Udara Jakarta

Muat `ispu_jakarta_2025.csv` dan analisis kolom `pm25`:

```python
# TUGAS ANDA
# 1. Periksa kenormalan dengan ketiga pendekatan
# 2. Bila tidak Normal, coba transformasi log dan akar
# 3. Hitung: berapa persen hari melampaui ambang PM2.5 = 55 µg/m³?
# 4. Berapa nilai PM2.5 pada persentil ke-95?
# 5. Bandingkan antar stasiun pemantauan
```

**Pertanyaan:** untuk melaporkan "kualitas udara tipikal Jakarta", ukuran mana yang Anda pilih — mean atau median? Jelaskan berdasarkan bentuk sebarannya.

### Tantangan 3: Simulasi Kenormalan Data Gabungan

```python
# TUGAS ANDA
# Bangkitkan data dari gabungan dua Normal dengan mean berbeda:
#   50% dari Normal(60, 8) dan 50% dari Normal(85, 8)
#
# 1. Buat histogram dan Q-Q plot
# 2. Jalankan Shapiro-Wilk — apakah ditolak?
# 3. Hitung kemencengan dan kurtosis
# 4. Apa yang terjadi bila jarak kedua mean diperkecil menjadi 5?
#
# Pertanyaan: mengapa boxplot bisa gagal mendeteksi bimodalitas
# sementara histogram berhasil?
```

---

## Refleksi

1. Mengapa Q-Q plot lebih berguna daripada nilai p pada sampel besar?
2. Jenis data Informatika apa saja yang biasanya **tidak** Normal? Mengapa?
3. Apa risiko dari mengasumsikan kenormalan tanpa memeriksanya?

---

## AI Usage Log

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |

> Nama: ______________  NIM: ______________

---

## Checklist Penyelesaian

- [ ] Notebook dinamai `Lab07_NIM_NamaLengkap.ipynb`
- [ ] Langkah 1–6 selesai
- [ ] Tantangan 1 dikerjakan **manual dulu**, tabel perbandingan disertakan
- [ ] Setiap Q-Q plot disertai interpretasi bentuknya
- [ ] Ketiga tantangan dikerjakan
- [ ] Refleksi terisi
- [ ] AI Usage Log terisi
- [ ] Diunggah ke LMS

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
