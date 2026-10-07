# Lab 06: Distribusi Diskret dengan scipy.stats

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu** | 6 |
| **Durasi** | 180 menit (mandiri) |
| **Prasyarat** | Lab 05 selesai; materi Minggu 6 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | 1,92% |
| **Berkas data** | `bug_report_harian.csv` |

---

## Tujuan Praktikum

1. Memakai `scipy.stats` untuk menghitung PMF, CDF, kuantil, dan statistik distribusi diskret.
2. Menerapkan distribusi Binomial, Poisson, dan Geometrik pada kasus Informatika.
3. Merencanakan kapasitas sistem berdasarkan kuantil, bukan rata-rata.
4. Memeriksa kecocokan distribusi Poisson pada data nyata.
5. Membuktikan sifat tanpa memori distribusi Geometrik secara empiris.

---

## Persiapan

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(42)
```

**Antarmuka `scipy.stats` yang akan dipakai:**

| Metode | Arti |
|--------|------|
| `.pmf(k)` | P(X = k) — untuk distribusi diskret |
| `.cdf(k)` | P(X ≤ k) |
| `.sf(k)` | P(X > k) — *survival function*, lebih akurat daripada `1 - cdf` |
| `.ppf(q)` | Kuantil: nilai k terkecil dengan P(X ≤ k) ≥ q |
| `.mean()`, `.var()`, `.std()` | Statistik teoretis |
| `.rvs(size=n)` | Membangkitkan n nilai acak |

---

## Langkah-langkah

### Langkah 1: Distribusi Bernoulli dan Binomial

```python
# =============================================
# LANGKAH 1: Binomial — load balancer
# =============================================

# 20 server, masing-masing galat dengan probabilitas 5%, saling bebas
n, p = 20, 0.05
X = stats.binom(n, p)

print("PEMERIKSAAN SYARAT BINS:")
print("  B (Binary)          : ya — server galat atau tidak")
print("  I (Independent)     : diasumsikan ya — perlu diverifikasi di dunia nyata")
print("  N (Number fixed)    : ya — tepat 20 server")
print("  S (Same probability): diasumsikan ya — semua server identik\n")

print(f"E[X]   = {X.mean():.4f}  (= n·p = {n*p})")
print(f"Var(X) = {X.var():.4f}  (= n·p·(1−p) = {n*p*(1-p)})")
print(f"SD(X)  = {X.std():.4f}\n")

print(f"P(X = 0)  = {X.pmf(0):.6f}   (tidak ada yang galat)")
print(f"P(X = 1)  = {X.pmf(1):.6f}")
print(f"P(X = 2)  = {X.pmf(2):.6f}")
print(f"P(X ≤ 2)  = {X.cdf(2):.6f}")
print(f"P(X ≥ 3)  = {X.sf(2):.6f}   (perhatikan: sf(2), bukan sf(3))")
print(f"P(X ≥ 5)  = {X.sf(4):.8f}   (kejadian yang sangat jarang)")

# Verifikasi jumlah PMF = 1
k = np.arange(0, n + 1)
print(f"\nΣ PMF = {X.pmf(k).sum():.10f}  (harus 1)")
```

```python
# Visualisasi pengaruh p terhadap bentuk
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, pp in zip(axes, [0.05, 0.5, 0.9]):
    k = np.arange(0, 21)
    ax.bar(k, stats.binom.pmf(k, 20, pp), color="steelblue", edgecolor="white")
    ax.set_title(f"Binomial(n=20, p={pp})\nmean={20*pp:.1f}, "
                 f"skew={'kanan' if pp<0.5 else 'kiri' if pp>0.5 else 'simetris'}")
    ax.set_xlabel("k")
axes[0].set_ylabel("P(X = k)")
plt.tight_layout()
plt.show()
```

### Langkah 2: Distribusi Poisson dan Perencanaan Kapasitas

```python
# =============================================
# LANGKAH 2: Poisson — perencanaan kapasitas server
# =============================================

lam = 8   # rata-rata 8 permintaan per detik
X = stats.poisson(lam)

print(f"Distribusi Poisson(λ = {lam})")
print(f"  E[X]   = {X.mean():.4f}")
print(f"  Var(X) = {X.var():.4f}")
print(f"  → mean = varians adalah CIRI KHAS Poisson\n")

print(f"P(X = 5)   = {X.pmf(5):.6f}")
print(f"P(X ≤ 8)   = {X.cdf(8):.6f}   (kapasitas rata-rata cukup?)")
print(f"P(X > 15)  = {X.sf(15):.8f}\n")

print("PERENCANAAN KAPASITAS:")
print(f"{'Tingkat layanan':>18}  {'Kapasitas minimum':>19}  {'Rasio thd rata-rata':>20}")
for level in [0.50, 0.90, 0.95, 0.99, 0.999, 0.9999]:
    kap = X.ppf(level)
    print(f"{level*100:>17.2f}%  {kap:>19.0f}  {kap/lam:>19.2f}×")

print(f"\n→ Merancang untuk rata-rata ({lam}) berarti kewalahan "
      f"{(1 - X.cdf(lam))*100:.1f}% waktu.")
print("→ Untuk 99,9% ketersediaan, kapasitas harus ~2,4× rata-rata.")
print("→ Inilah alasan matematis di balik 'over-provisioning'.")
```

### Langkah 3: Memeriksa Kecocokan Poisson pada Data Nyata

```python
# =============================================
# LANGKAH 3: Apakah data bug mengikuti Poisson?
# =============================================

df = pd.read_csv("bug_report_harian.csv")
jumlah = df["jumlah_bug"].values

mean_data = jumlah.mean()
var_data = jumlah.var(ddof=1)
rasio = var_data / mean_data

print(f"n hari         : {len(jumlah)}")
print(f"Mean           : {mean_data:.4f}")
print(f"Varians        : {var_data:.4f}")
print(f"Rasio var/mean : {rasio:.4f}")
print()
if 0.8 <= rasio <= 1.25:
    print("→ Rasio mendekati 1: Poisson MASUK AKAL.")
elif rasio > 1.25:
    print("→ Rasio > 1: OVERDISPERSION. Poisson mungkin tidak cocok.")
    print("  Kemungkinan penyebab: laju λ tidak konstan (ada hari sibuk),")
    print("  atau kejadian tidak saling bebas (satu bug memicu bug lain).")
else:
    print("→ Rasio < 1: UNDERDISPERSION. Data lebih teratur dari Poisson.")
```

```python
# Perbandingan visual: teramati vs diharapkan
lam_taksiran = mean_data
nilai = np.arange(0, jumlah.max() + 1)
teramati = np.array([(jumlah == k).sum() for k in nilai])
diharapkan = stats.poisson.pmf(nilai, lam_taksiran) * len(jumlah)

fig, axes = plt.subplots(1, 2, figsize=(14, 4.5))

lebar = 0.4
axes[0].bar(nilai - lebar/2, teramati, lebar, label="Teramati",
            color="steelblue")
axes[0].bar(nilai + lebar/2, diharapkan, lebar,
            label=f"Poisson(λ={lam_taksiran:.2f})", color="#e67e22", alpha=0.85)
axes[0].set_xlabel("Jumlah bug per hari")
axes[0].set_ylabel("Jumlah hari")
axes[0].set_title(f"Kecocokan dengan Poisson (n = {len(jumlah)} hari)")
axes[0].legend()

# Q-Q plot diskret
teori = stats.poisson.ppf(np.linspace(0.01, 0.99, len(jumlah)), lam_taksiran)
axes[1].scatter(np.sort(teori), np.sort(jumlah), alpha=0.5, s=20)
lims = [0, max(jumlah.max(), teori.max())]
axes[1].plot(lims, lims, "r--", linewidth=1.5)
axes[1].set_xlabel("Kuantil teoretis Poisson")
axes[1].set_ylabel("Kuantil data teramati")
axes[1].set_title("Q-Q Plot")

plt.tight_layout()
plt.show()
```

> **Tulis interpretasi:** berdasarkan rasio varians/mean dan perbandingan visual, apakah Poisson model yang masuk akal untuk data ini? Uji formalnya (chi-square kesesuaian) akan dipelajari Minggu 13.

### Langkah 4: Distribusi Geometrik dan Sifat Tanpa Memori

```python
# =============================================
# LANGKAH 4: Geometrik — strategi retry
# =============================================

p = 0.3   # setiap percobaan sambung berhasil dengan probabilitas 0,3
X = stats.geom(p)

print(f"Distribusi Geometrik(p = {p})")
print(f"  E[X]   = {X.mean():.4f}  (= 1/p = {1/p:.4f})")
print(f"  Var(X) = {X.var():.4f}\n")

print(f"P(berhasil pada percobaan ke-1) = {X.pmf(1):.4f}")
print(f"P(berhasil pada percobaan ke-4) = {X.pmf(4):.4f}")
print(f"P(butuh lebih dari 5 percobaan) = {X.sf(5):.4f}")
print(f"P(butuh lebih dari 10 percobaan)= {X.sf(10):.4f}\n")

# Membuktikan sifat tanpa memori
print("BUKTI SIFAT TANPA MEMORI:")
print(f"  P(X > 5)          = {X.sf(5):.8f}")
print(f"  P(X > 8 | X > 3)  = {X.sf(8)/X.sf(3):.8f}")
print(f"  Selisih           = {abs(X.sf(5) - X.sf(8)/X.sf(3)):.2e}")
print("\n→ IDENTIK. Sudah gagal 3 kali TIDAK membuat percobaan")
print("  berikutnya lebih mungkin berhasil.")
print("  Keyakinan sebaliknya disebut GAMBLER'S FALLACY.")
```

```python
# Verifikasi empiris dengan simulasi
ulangan = 200_000
sampel = X.rvs(size=ulangan, random_state=42)

p_teoretis = X.sf(5)
p_empiris = (sampel > 5).mean()

# P(X > 8 | X > 3) secara empiris
subset = sampel[sampel > 3]
p_bersyarat_empiris = (subset > 8).mean()

print(f"\nVerifikasi empiris ({ulangan:,} simulasi):")
print(f"  P(X > 5) teoretis : {p_teoretis:.6f}")
print(f"  P(X > 5) empiris  : {p_empiris:.6f}")
print(f"  P(X > 8 | X > 3)  : {p_bersyarat_empiris:.6f}")
```

### Langkah 5: Memilih Distribusi yang Tepat

```python
# =============================================
# LANGKAH 5: Latihan pemilihan distribusi
# =============================================

kasus = [
    {
        "deskripsi": "Dari 50 pull request, berapa yang ditolak? Tingkat penolakan 12%.",
        "distribusi": "Binomial(n=50, p=0.12)",
        "hitung": lambda: stats.binom(50, 0.12),
    },
    {
        "deskripsi": "Berapa laporan bug masuk besok? Rata-rata 6 per hari.",
        "distribusi": "Poisson(λ=6)",
        "hitung": lambda: stats.poisson(6),
    },
    {
        "deskripsi": "Berapa kali refresh sampai halaman termuat? Berhasil 85%.",
        "distribusi": "Geometrik(p=0.85)",
        "hitung": lambda: stats.geom(0.85),
    },
]

for i, k in enumerate(kasus, 1):
    X = k["hitung"]()
    print(f"{i}. {k['deskripsi']}")
    print(f"   Distribusi : {k['distribusi']}")
    print(f"   E[X]       : {X.mean():.4f}")
    print(f"   SD(X)      : {X.std():.4f}")
    print(f"   P(X ≤ E[X]): {X.cdf(X.mean()):.4f}\n")
```

---

## Tantangan Tambahan

### Tantangan 1: Binomial vs Poisson sebagai Hampiran

Bandingkan Binomial(n, p) dengan Poisson(λ = np) untuk beberapa nilai n dan p.

```python
# TUGAS ANDA
# Untuk pasangan (n, p) berikut, hitung selisih maksimum PMF-nya:
#   (100, 0.5), (100, 0.05), (1000, 0.005), (10000, 0.0008)
# Simpulkan: kapan hampiran Poisson cukup baik?
```

### Tantangan 2: Perencanaan Kapasitas Nyata

Sebuah API Sistem Informasi Akademik UAI menerima permintaan dengan pola berikut:

| Periode | Rata-rata permintaan/detik |
|---------|---------------------------|
| Jam biasa | 12 |
| Jam sibuk (pengisian KRS) | 95 |
| Puncak (hari pertama KRS) | 340 |

```python
# TUGAS ANDA
# Untuk setiap periode, hitung kapasitas minimum agar sistem
# tidak kewalahan pada tingkat layanan 99% dan 99,9%.
# Sajikan dalam tabel dan buat rekomendasi autoscaling.
```

**Pertanyaan:** apakah masuk akal menyiapkan kapasitas puncak sepanjang waktu? Apa alternatifnya?

### Tantangan 3: Menguji Asumsi Kebebasan

Distribusi Binomial dan Poisson **mengandaikan kejadian saling bebas**. Dalam kenyataan, kegagalan sering berkorelasi.

```python
# TUGAS ANDA
# Simulasikan dua skenario dengan 20 server:
#   (a) Kegagalan BEBAS: tiap server gagal dengan p=0.05 secara mandiri
#   (b) Kegagalan BERKORELASI: dengan probabilitas 0.02 terjadi gangguan
#       pusat data yang membuat SEMUA server gagal bersamaan; selain itu
#       tiap server gagal mandiri dengan p=0.03
#
# Bandingkan sebaran jumlah server gagal pada kedua skenario.
# Hitung P(X ≥ 10) untuk keduanya.
```

**Pertanyaan:** berapa kali lipat lebih besar risiko kegagalan massal pada skenario berkorelasi? Apa pelajarannya bagi arsitektur sistem yang mengandalkan replika?

---

## Refleksi

1. Mengapa merancang kapasitas berdasarkan rata-rata adalah kesalahan?
2. Apa tanda-tanda bahwa Poisson **tidak** cocok untuk sebuah data?
3. Bagaimana *gambler's fallacy* bisa muncul dalam perancangan sistem *retry*?

---

## AI Usage Log

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |

> Nama: ______________  NIM: ______________

---

## Checklist Penyelesaian

- [ ] Notebook dinamai `Lab06_NIM_NamaLengkap.ipynb`
- [ ] Langkah 1–5 selesai
- [ ] Syarat BINS diperiksa secara eksplisit pada Langkah 1
- [ ] Setiap keluaran disertai interpretasi
- [ ] Ketiga tantangan dikerjakan
- [ ] Refleksi terisi
- [ ] AI Usage Log terisi
- [ ] Diunggah ke LMS

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
