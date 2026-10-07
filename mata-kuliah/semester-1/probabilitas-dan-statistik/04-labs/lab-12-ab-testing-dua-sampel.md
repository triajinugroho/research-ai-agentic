# Lab 12: A/B Testing dan Uji Dua Sampel

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu** | 12 |
| **Durasi** | 180 menit (mandiri) |
| **Prasyarat** | Lab 11 selesai; materi Minggu 12 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | 1,92% |
| **Berkas data** | `ab_test_fitur_checkout.csv`, `nilai_mahasiswa_if.csv` |

---

## Tujuan Praktikum

1. Memilih uji yang tepat: bebas vs berpasangan, parametrik vs nonparametrik.
2. Menjalankan uji-t dua sampel (Welch dan pooled) dengan pemeriksaan asumsi.
3. Menjalankan uji-t berpasangan dan menunjukkan keunggulan kuasanya.
4. Menganalisis A/B test proporsi lengkap dengan interval kepercayaan.
5. Mendemonstrasikan bahaya *peeking* pada A/B test.

---

## Persiapan

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, confint_proportions_2indep

rng = np.random.default_rng(42)
```

---

## Langkah-langkah

### Langkah 1: Uji Dua Sampel Bebas Lengkap

```python
# =============================================
# LANGKAH 1: Uji dua sampel bebas
# =============================================

def uji_dua_sampel(g1, g2, nama1="Kelompok 1", nama2="Kelompok 2", alpha=0.05):
    """Uji dua sampel bebas: asumsi, tiga uji, ukuran efek, interval."""
    g1 = np.asarray(g1, dtype=float); g1 = g1[~np.isnan(g1)]
    g2 = np.asarray(g2, dtype=float); g2 = g2[~np.isnan(g2)]
    n1, n2 = len(g1), len(g2)

    print("=" * 64)
    print(f"{nama1} vs {nama2}")
    print("=" * 64)
    print(f"{nama1:>22}: n={n1:>4}  mean={g1.mean():>9.4f}  s={g1.std(ddof=1):>8.4f}")
    print(f"{nama2:>22}: n={n2:>4}  mean={g2.mean():>9.4f}  s={g2.std(ddof=1):>8.4f}")

    print(f"\n--- PEMERIKSAAN ASUMSI ---")
    _, p1 = stats.shapiro(g1[:5000])
    _, p2 = stats.shapiro(g2[:5000])
    print(f"Kenormalan {nama1:>16}: p = {p1:.6f}")
    print(f"Kenormalan {nama2:>16}: p = {p2:.6f}")
    _, p_lev = stats.levene(g1, g2)
    print(f"Homogenitas ragam (Levene) : p = {p_lev:.6f} "
          f"→ {'homogen' if p_lev > alpha else 'TIDAK homogen'}")
    normal_ok = (p1 > alpha and p2 > alpha) or (n1 >= 30 and n2 >= 30)
    print(f"Kesimpulan: {'uji parametrik layak' if normal_ok else 'pertimbangkan nonparametrik'}")

    print(f"\n--- HASIL TIGA UJI ---")
    tw, pw = stats.ttest_ind(g1, g2, equal_var=False)
    tp, pp = stats.ttest_ind(g1, g2, equal_var=True)
    u, pu = stats.mannwhitneyu(g1, g2, alternative="two-sided")
    print(f"Uji-t Welch   : t = {tw:>9.4f}  p = {pw:.8f}  ← dianjurkan")
    print(f"Uji-t pooled  : t = {tp:>9.4f}  p = {pp:.8f}")
    print(f"Mann-Whitney  : U = {u:>9.1f}  p = {pu:.8f}")

    s_pool = np.sqrt(((n1-1)*g1.var(ddof=1) + (n2-1)*g2.var(ddof=1)) / (n1+n2-2))
    d = (g1.mean() - g2.mean()) / s_pool
    besar = ("sangat kecil" if abs(d) < 0.2 else "kecil" if abs(d) < 0.5
             else "sedang" if abs(d) < 0.8 else "besar")

    se = np.sqrt(g1.var(ddof=1)/n1 + g2.var(ddof=1)/n2)
    dfw = se**4 / ((g1.var(ddof=1)/n1)**2/(n1-1) + (g2.var(ddof=1)/n2)**2/(n2-1))
    tc = stats.t.ppf(1 - alpha/2, dfw)
    selisih = g1.mean() - g2.mean()

    print(f"\n--- UKURAN EFEK DAN PRESISI ---")
    print(f"Selisih rata-rata : {selisih:.4f}")
    print(f"IK {(1-alpha)*100:.0f}% selisih   : [{selisih-tc*se:.4f} , {selisih+tc*se:.4f}]")
    print(f"Cohen's d         : {d:.4f}  (efek {besar})")

    p_pakai = pw if normal_ok else pu
    print(f"\n--- KEPUTUSAN ---")
    if p_pakai < alpha:
        print(f"p = {p_pakai:.8f} < {alpha} → TOLAK H₀: ada perbedaan signifikan.")
        if abs(d) < 0.2:
            print("PERINGATAN: efeknya sangat kecil — periksa kebermaknaan praktisnya.")
    else:
        print(f"p = {p_pakai:.8f} ≥ {alpha} → GAGAL MENOLAK H₀.")
    return {"p": p_pakai, "d": d}

df = pd.read_csv("nilai_mahasiswa_if.csv")
uji_dua_sampel(df[df.kelas=="IF26A"]["nilai_uas"],
               df[df.kelas=="IF26H"]["nilai_uas"], "IF26A", "IF26H")
```

### Langkah 2: Uji Berpasangan dan Kuasa yang Terbuang

```python
# =============================================
# LANGKAH 2: Berpasangan vs bebas
# =============================================

# Waktu eksekusi (detik) pada 12 mesin yang SAMA
sebelum = np.array([142, 158, 131, 176, 149, 163, 138, 155, 147, 169, 152, 144])
sesudah = np.array([128, 141, 122, 155, 133, 147, 125, 139, 134, 150, 138, 130])
selisih = sebelum - sesudah

print("Data: 12 mesin, diukur SEBELUM dan SESUDAH optimasi.\n")
print(f"{'Mesin':>6} {'Sebelum':>9} {'Sesudah':>9} {'Selisih':>9}")
for i, (a, b, d) in enumerate(zip(sebelum, sesudah, selisih), 1):
    print(f"{i:>6} {a:>9} {b:>9} {d:>9}")

print(f"\nRata-rata selisih : {selisih.mean():.4f} detik")
print(f"SD selisih        : {selisih.std(ddof=1):.4f}")

print("\n--- UJI BERPASANGAN (BENAR) ---")
tp, pp = stats.ttest_rel(sebelum, sesudah)
print(f"t = {tp:.4f}, p = {pp:.10f}")
d_pair = selisih.mean() / selisih.std(ddof=1)
print(f"Cohen's d = {d_pair:.4f}")

print("\n--- UJI DUA SAMPEL BEBAS (KELIRU untuk data ini) ---")
ti, pi = stats.ttest_ind(sebelum, sesudah, equal_var=False)
print(f"t = {ti:.4f}, p = {pi:.10f}")

print(f"\n→ p berpasangan {pp:.2e} vs p bebas {pi:.2e}")
print(f"→ Rasio: {pi/pp:.0f}× lebih besar")
print("→ Memakai uji yang salah MEMBUANG kuasa uji karena variasi")
print("  antar mesin tidak dihilangkan.")

# Nonparametrik untuk berpasangan
w, pwx = stats.wilcoxon(sebelum, sesudah)
print(f"\nWilcoxon signed-rank: W = {w:.1f}, p = {pwx:.10f}")
```

### Langkah 3: A/B Test Proporsi

```python
# =============================================
# LANGKAH 3: A/B test proporsi lengkap
# =============================================

ab = pd.read_csv("ab_test_fitur_checkout.csv")

ringkas = ab.groupby("grup").agg(
    pengunjung=("user_id", "count"),
    konversi=("konversi", "sum"),
).assign(tingkat=lambda d: d["konversi"] / d["pengunjung"])

print(ringkas.round(4))

konv = ringkas["konversi"].values
tot = ringkas["pengunjung"].values
p1, p2 = konv / tot

z, p_value = proportions_ztest(konv, tot)
bawah, atas = confint_proportions_2indep(konv[1], tot[1], konv[0], tot[0],
                                         method="wald")

print(f"\n--- HASIL ---")
print(f"Grup A : {p1*100:.3f}%")
print(f"Grup B : {p2*100:.3f}%")
print(f"Selisih absolut  : {(p2-p1)*100:+.3f} poin persen")
print(f"Kenaikan relatif : {(p2-p1)/p1*100:+.2f}%")
print(f"\nz = {z:.4f}, p-value = {p_value:.8f}")
print(f"IK 95% selisih   : [{bawah*100:+.3f} , {atas*100:+.3f}] poin persen")

print(f"\n--- INTERPRETASI BISNIS ---")
if p_value < 0.05:
    print("Perbedaan signifikan secara statistik.")
    print(f"Namun kenaikan sebenarnya bisa serendah {bawah*100:.2f} pp")
    print(f"atau setinggi {atas*100:.2f} pp.")
    print("Pertanyaan yang harus dijawab tim produk:")
    print(f"  Apakah kenaikan {bawah*100:.2f} pp (skenario terburuk)")
    print("  masih membenarkan biaya penerapan fitur ini?")
else:
    print("Bukti tidak cukup untuk menyatakan ada perbedaan.")
```

### Langkah 4: Merancang A/B Test — Ukuran Sampel

```python
# =============================================
# LANGKAH 4: Perencanaan ukuran sampel A/B test
# =============================================

from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

def n_ab_test(p_dasar, kenaikan_min, alpha=0.05, kuasa=0.80):
    efek = proportion_effectsize(p_dasar + kenaikan_min, p_dasar)
    return int(np.ceil(NormalIndPower().solve_power(
        effect_size=efek, alpha=alpha, power=kuasa, ratio=1.0)))

p_dasar = p1
print(f"Tingkat konversi saat ini: {p_dasar*100:.2f}%\n")
print(f"{'Kenaikan minimum':>18}  {'n per grup':>12}  {'Total':>12}")
for kn in [0.05, 0.03, 0.02, 0.01, 0.005]:
    n = n_ab_test(p_dasar, kn)
    print(f"{kn*100:>15.1f} pp  {n:>12,}  {n*2:>12,}")

print("\n→ Tetapkan 'kenaikan minimum yang bermakna' LEBIH DULU,")
print("  berdasarkan pertimbangan bisnis, bukan berdasarkan hasil.")
```

### Langkah 5: Bahaya *Peeking*

```python
# =============================================
# LANGKAH 5: Mengapa tidak boleh mengintip hasil
# =============================================

def simulasi_peeking(n_maks=4000, n_intip=20, alpha=0.05, ulangan=2000):
    """Berapa galat Tipe I sebenarnya bila mengintip berkali-kali?"""
    titik_intip = np.linspace(200, n_maks, n_intip).astype(int)
    p_sama = 0.15   # H₀ BENAR: kedua grup identik

    salah_sekali, salah_akhir = 0, 0
    for _ in range(ulangan):
        a = rng.random(n_maks) < p_sama
        b = rng.random(n_maks) < p_sama
        berhenti_dini = False
        for n in titik_intip:
            _, p = proportions_ztest([a[:n].sum(), b[:n].sum()], [n, n])
            if p < alpha:
                berhenti_dini = True
                break
        if berhenti_dini:
            salah_sekali += 1
        _, p_akhir = proportions_ztest([a.sum(), b.sum()], [n_maks, n_maks])
        if p_akhir < alpha:
            salah_akhir += 1

    return salah_sekali/ulangan, salah_akhir/ulangan

print("H₀ BENAR (kedua grup identik). Berapa sering kita salah menolaknya?\n")
print(f"{'Jumlah intipan':>16}  {'Galat Tipe I':>14}")
for k in [1, 5, 10, 20]:
    tipe1, _ = simulasi_peeking(n_intip=k, ulangan=500)
    print(f"{k:>16}  {tipe1*100:>13.2f}%")

print("\n→ Dengan 20 kali intipan, galat Tipe I melonjak dari 5%")
print("  menjadi lebih dari 20%.")
print("→ ATURAN: tetapkan n di muka, jalankan sampai selesai,")
print("  analisis SATU KALI.")
```

---

## Tantangan Tambahan

### Tantangan 1: A/B Test dengan Metrik Kontinu

```python
# TUGAS ANDA
# Gunakan kolom durasi_detik pada ab_test_fitur_checkout.csv
# 1. Bandingkan durasi antara grup A dan B
# 2. Periksa kenormalan — apakah durasi menceng?
# 3. Jalankan uji-t Welch DAN Mann-Whitney
# 4. Bandingkan kesimpulannya
# 5. Bila berbeda, mana yang Anda laporkan dan mengapa?
#
# Pertanyaan: untuk metrik durasi yang menceng kanan, apakah
# membandingkan MEAN adalah pilihan yang tepat? Apa alternatifnya?
```

### Tantangan 2: Koreksi Perbandingan Ganda

```python
# TUGAS ANDA
# Sebuah A/B test dianalisis pada 8 segmen pengguna berbeda
# (mahasiswa baru, mahasiswa lama, pengguna mobile, desktop, dst).
#
# 1. Simulasikan 8 uji dengan H₀ BENAR untuk semuanya
# 2. Hitung berapa persen menghasilkan sedikitnya satu p < 0,05
# 3. Terapkan koreksi Bonferroni (α/k) — hitung ulang
# 4. Terapkan koreksi Benjamini-Hochberg (statsmodels: multipletests)
# 5. Bandingkan ketiganya
#
# Pertanyaan: mengapa "menggali segmen sampai ketemu yang signifikan"
# adalah praktik yang tidak sahih?
```

### Tantangan 3: Rancangan A/B Test Kampus

Rancang A/B test lengkap untuk salah satu skenario:

1. Menambahkan tombol "Daftar Cepat" pada halaman KRS daring.
2. Mengubah tata letak beranda aplikasi perpustakaan.
3. Notifikasi pengingat tugas via aplikasi vs surel.

Dokumen rancangan harus memuat:

| Bagian | Isi |
|--------|-----|
| Hipotesis | H₀ dan H₁ eksplisit |
| Metrik utama | Satu saja, ditetapkan di muka |
| Metrik penjaga | Metrik yang tidak boleh memburuk |
| Efek minimum bermakna | Beserta alasan bisnisnya |
| Ukuran sampel | Hasil perhitungan, bukan tebakan |
| Cara pengacakan | Bagaimana pengguna ditugaskan ke grup |
| Durasi | Berapa lama dan mengapa |
| Rencana analisis | Uji apa, asumsi apa, kapan dianalisis |
| Aturan berhenti | Kapan tes dihentikan (dan kapan TIDAK) |

---

## Refleksi

1. Mengapa uji berpasangan lebih berkuasa ketika rancangannya memang berpasangan?
2. Apa yang salah dengan "menjalankan tes sampai signifikan"?
3. Mengapa interval kepercayaan selisih lebih berguna bagi pengambil keputusan daripada *p-value*?

---

## AI Usage Log

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |

> Nama: ______________  NIM: ______________

---

## Checklist Penyelesaian

- [ ] Notebook dinamai `Lab12_NIM_NamaLengkap.ipynb`
- [ ] Langkah 1–5 selesai
- [ ] Asumsi diperiksa pada setiap uji
- [ ] Interval kepercayaan selisih dilaporkan
- [ ] Ketiga tantangan dikerjakan
- [ ] Tantangan 3 memuat seluruh bagian dokumen rancangan
- [ ] Refleksi terisi
- [ ] AI Usage Log terisi
- [ ] Diunggah ke LMS

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
