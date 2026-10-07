# Lab 13: ANOVA dan Uji Chi-Square

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu** | 13 |
| **Durasi** | 180 menit (mandiri) |
| **Prasyarat** | Lab 12 selesai; materi Minggu 13 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | 1,92% |
| **Berkas data** | `transjakarta_koridor.csv`, `nilai_mahasiswa_if.csv` |

---

## Tujuan Praktikum

1. Menunjukkan inflasi galat Tipe I pada perbandingan ganda.
2. Menjalankan ANOVA satu arah dengan pemeriksaan asumsi lengkap.
3. Menjalankan uji lanjut Tukey dan membacanya dengan benar.
4. Menjalankan uji chi-square kesesuaian dan kebebasan.
5. Menghitung dan menafsirkan ukuran efek η² dan Cramér's V.

---

## Persiapan

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from math import comb

rng = np.random.default_rng(42)
```

---

## Langkah-langkah

### Langkah 1: Inflasi Galat Tipe I

```python
# =============================================
# LANGKAH 1: Mengapa uji-t berulang tidak sahih
# =============================================

print("Peluang sedikitnya satu galat Tipe I (α = 0,05 per uji):\n")
print(f"{'k kelompok':>12}  {'Jumlah uji':>11}  {'α gabungan':>12}")
for k in [2, 3, 4, 5, 6, 8, 10]:
    n_uji = comb(k, 2)
    print(f"{k:>12}  {n_uji:>11}  {1 - 0.95**n_uji:>11.4f}")

# Verifikasi dengan simulasi
def simulasi_inflasi(k, n_per_kelompok=30, ulangan=3000, alpha=0.05):
    """Berapa sering ada temuan palsu bila semua kelompok identik?"""
    palsu = 0
    for _ in range(ulangan):
        kel = [rng.normal(100, 15, n_per_kelompok) for _ in range(k)]
        ada = any(stats.ttest_ind(kel[i], kel[j])[1] < alpha
                  for i in range(k) for j in range(i+1, k))
        palsu += ada
    return palsu / ulangan

print(f"\nVerifikasi simulasi (semua kelompok IDENTIK):")
print(f"{'k':>4}  {'Teoretis':>10}  {'Simulasi':>10}")
for k in [2, 3, 4, 5]:
    teori = 1 - 0.95**comb(k, 2)
    print(f"{k:>4}  {teori:>10.4f}  {simulasi_inflasi(k, ulangan=1500):>10.4f}")
```

### Langkah 2: ANOVA Satu Arah Lengkap

```python
# =============================================
# LANGKAH 2: ANOVA dengan pemeriksaan asumsi
# =============================================

def anova_lengkap(df, kol_nilai, kol_kelompok, alpha=0.05):
    """ANOVA satu arah: asumsi, uji, ukuran efek, uji lanjut."""
    data = df[[kol_nilai, kol_kelompok]].dropna()
    kelompok = [g[kol_nilai].values for _, g in data.groupby(kol_kelompok)]
    nama = sorted(data[kol_kelompok].unique())
    k, N = len(kelompok), len(data)

    print("=" * 68)
    print(f"ANOVA: {kol_nilai} menurut {kol_kelompok}")
    print("=" * 68)
    print(f"{'Kelompok':<26} {'n':>5} {'Mean':>10} {'SD':>10}")
    for nm, g in zip(nama, kelompok):
        print(f"{str(nm):<26} {len(g):>5} {g.mean():>10.3f} {g.std(ddof=1):>10.3f}")

    print(f"\n--- ASUMSI ---")
    _, p_lev = stats.levene(*kelompok)
    homogen = p_lev > alpha
    print(f"Homogenitas ragam (Levene): p = {p_lev:.6f} "
          f"→ {'homogen ✓' if homogen else 'TIDAK homogen ✗'}")
    semua_normal = True
    for nm, g in zip(nama, kelompok):
        if 3 <= len(g) <= 5000:
            _, p_n = stats.shapiro(g)
            if p_n <= alpha and len(g) < 30:
                semua_normal = False
            print(f"Kenormalan {str(nm):<20}: p = {p_n:.6f}")

    print(f"\n--- UJI UTAMA ---")
    F, p = stats.f_oneway(*kelompok)
    print(f"ANOVA klasik : F({k-1}, {N-k}) = {F:.4f}, p = {p:.8f}")

    if not homogen:
        try:
            from scipy.stats import alexandergovern
            ag = alexandergovern(*kelompok)
            print(f"Alexander-Govern (robust): p = {ag.pvalue:.8f}")
        except ImportError:
            pass
    H, p_kw = stats.kruskal(*kelompok)
    print(f"Kruskal-Wallis (nonparametrik): H = {H:.4f}, p = {p_kw:.8f}")

    # Ukuran efek
    grand = np.concatenate(kelompok)
    gm = grand.mean()
    ss_antar = sum(len(g) * (g.mean() - gm)**2 for g in kelompok)
    ss_total = ((grand - gm)**2).sum()
    eta2 = ss_antar / ss_total
    besar = "kecil" if eta2 < 0.06 else "sedang" if eta2 < 0.14 else "besar"

    print(f"\n--- UKURAN EFEK ---")
    print(f"η² = {eta2:.4f}  (efek {besar})")
    print(f"→ {eta2*100:.1f}% keragaman dijelaskan oleh {kol_kelompok}")
    print(f"→ {(1-eta2)*100:.1f}% sisanya oleh faktor lain")

    print(f"\n--- KEPUTUSAN ---")
    if p < alpha:
        print(f"p < {alpha} → TOLAK H₀. Sedikitnya satu kelompok berbeda.")
        print(f"\n--- UJI LANJUT TUKEY HSD ---")
        tukey = pairwise_tukeyhsd(data[kol_nilai], data[kol_kelompok], alpha=alpha)
        print(tukey)
        print("\nCara membaca: bila [lower, upper] MEMUAT NOL,")
        print("pasangan itu tidak berbeda signifikan.")
    else:
        print(f"p ≥ {alpha} → GAGAL MENOLAK H₀.")
        print("Uji lanjut TIDAK dilakukan (akan mengembalikan masalah")
        print("perbandingan ganda yang justru ingin dihindari).")
    return F, p, eta2

df = pd.read_csv("nilai_mahasiswa_if.csv")
anova_lengkap(df, "jam_belajar", "asal_sekolah")
```

### Langkah 3: ANOVA pada Data TransJakarta

```python
# =============================================
# LANGKAH 3: Kasus nyata — koridor TransJakarta
# =============================================

tj = pd.read_csv("transjakarta_koridor.csv")

print(tj.groupby("koridor")["jumlah_penumpang"].describe().round(2))

anova_lengkap(tj, "jumlah_penumpang", "koridor")
```

```python
# Visualisasi
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

import seaborn as sns
sns.boxplot(data=tj, x="koridor", y="jumlah_penumpang", ax=axes[0],
            palette="Set3")
axes[0].set_title("Sebaran penumpang per koridor")
axes[0].tick_params(axis="x", rotation=45)

# Plot rata-rata dengan galat baku
ringkas = tj.groupby("koridor")["jumlah_penumpang"].agg(["mean", "sem"])
axes[1].errorbar(range(len(ringkas)), ringkas["mean"],
                 yerr=1.96*ringkas["sem"], fmt="o", capsize=5,
                 color="steelblue", markersize=7)
axes[1].set_xticks(range(len(ringkas)))
axes[1].set_xticklabels(ringkas.index, rotation=45)
axes[1].set_ylabel("Rata-rata penumpang")
axes[1].set_title("Rata-rata ± IK 95%")
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

> **Tulis interpretasi:** koridor mana yang berbeda dari yang lain menurut uji Tukey? Berapa η²-nya — apakah "koridor" menjelaskan sebagian besar keragaman, atau justru sedikit?

### Langkah 4: Uji Chi-Square Kesesuaian

```python
# =============================================
# LANGKAH 4: Chi-square kesesuaian
# =============================================

hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
teramati = np.array([52, 38, 41, 44, 65])
n = teramati.sum()
diharapkan = np.full(len(hari), n / len(hari))

print("H₀: laporan bug tersebar MERATA sepanjang hari kerja\n")
print(f"{'Hari':>8} {'Teramati':>10} {'Diharapkan':>12} {'(O−E)':>8} {'(O−E)²/E':>10}")
for h, o, e in zip(hari, teramati, diharapkan):
    print(f"{h:>8} {o:>10} {e:>12.1f} {o-e:>8.1f} {(o-e)**2/e:>10.4f}")

chi2, p = stats.chisquare(teramati, diharapkan)
dof = len(hari) - 1

print(f"\nχ² = {chi2:.4f}, df = {dof}, p = {p:.8f}")
print(f"Nilai kritis (α=0,05) = {stats.chi2.ppf(0.95, dof):.4f}")
print(f"\nSyarat semua E ≥ 5? {'ya ✓' if (diharapkan >= 5).all() else 'TIDAK ✗'}")

# Residual terstandardisasi
residual = (teramati - diharapkan) / np.sqrt(diharapkan)
print(f"\nResidual terstandardisasi (|r| > 2 patut diperhatikan):")
for h, r in zip(hari, residual):
    tanda = " ←" if abs(r) > 2 else ""
    print(f"  {h:>8}: {r:>7.3f}{tanda}")

if p < 0.05:
    print("\n→ TOLAK H₀. Sebaran TIDAK merata.")
    print("→ Jumat dan Senin menyumbang paling banyak.")
    print("→ Dugaan penyebab: deployment akhir pekan dan tekanan akhir sprint.")
    print("  (Dugaan ini HIPOTESIS, bukan kesimpulan dari uji ini.)")
```

### Langkah 5: Uji Chi-Square Kebebasan

```python
# =============================================
# LANGKAH 5: Chi-square kebebasan
# =============================================

df["kategori_nilai"] = pd.cut(df["nilai_uas"], bins=[0, 60, 75, 100],
                              labels=["Rendah", "Sedang", "Tinggi"])
tabel = pd.crosstab(df["asal_sekolah"], df["kategori_nilai"])

print("TABEL KONTINGENSI (teramati):")
print(tabel)
print(f"\nTotal: {tabel.values.sum()}")

chi2, p, dof, diharapkan = stats.chi2_contingency(tabel)

print("\nFREKUENSI DIHARAPKAN (bila kedua variabel bebas):")
print(pd.DataFrame(diharapkan, index=tabel.index,
                   columns=tabel.columns).round(2))

print(f"\nχ² = {chi2:.4f}, df = {dof}, p = {p:.8f}")

prop_ok = (diharapkan >= 5).mean()
print(f"\nSyarat kelayakan: {prop_ok*100:.1f}% sel punya E ≥ 5 "
      f"({'terpenuhi ✓' if prop_ok >= 0.8 else 'TIDAK terpenuhi ✗'})")
if prop_ok < 0.8:
    print("→ Gabungkan kategori atau gunakan uji eksak Fisher.")

# Cramér's V
n_total = tabel.values.sum()
v = np.sqrt(chi2 / (n_total * (min(tabel.shape) - 1)))
besar = "kecil" if v < 0.3 else "sedang" if v < 0.5 else "besar"
print(f"\nCramér's V = {v:.4f}  (asosiasi {besar})")

# Residual terstandardisasi
res = (tabel.values - diharapkan) / np.sqrt(diharapkan)
print("\nResidual terstandardisasi:")
print(pd.DataFrame(res, index=tabel.index, columns=tabel.columns).round(2))

print("\n" + "="*60)
if p < 0.05:
    print("→ TOLAK H₀: terdapat asosiasi antara asal sekolah dan kategori nilai.")
else:
    print("→ GAGAL MENOLAK H₀: bukti tidak cukup adanya asosiasi.")
print("\nPERINGATAN PENTING:")
print("Asosiasi BUKAN sebab-akibat. Bisa jadi ada variabel ketiga")
print("(akses fasilitas belajar, latar ekonomi, motivasi) yang")
print("menjelaskan keduanya sekaligus.")
```

---

## Tantangan Tambahan

### Tantangan 1: ANOVA Dua Arah

```python
# TUGAS ANDA
# Gunakan statsmodels untuk ANOVA dua arah:
#   nilai_uas ~ kelas + asal_sekolah + kelas:asal_sekolah
#
# import statsmodels.api as sm
# from statsmodels.formula.api import ols
# model = ols('nilai_uas ~ C(kelas) + C(asal_sekolah) + C(kelas):C(asal_sekolah)',
#             data=df).fit()
# print(sm.stats.anova_lm(model, typ=2))
#
# Pertanyaan:
# 1. Apakah ada efek interaksi? Apa artinya bila ada?
# 2. Bagaimana cara memvisualisasikan interaksi? (Petunjuk: interaction plot)
```

### Tantangan 2: Ketika Asumsi ANOVA Dilanggar

```python
# TUGAS ANDA
# Simulasikan tiga kelompok dengan:
#   (a) Ragam sangat berbeda: SD = 5, 15, 40
#   (b) Ukuran sangat tidak seimbang: n = 10, 50, 200
#
# 1. Jalankan ANOVA klasik, Alexander-Govern, dan Kruskal-Wallis
# 2. Ulangi 2000 kali dengan H₀ BENAR
# 3. Hitung galat Tipe I empiris tiap uji
#
# Pertanyaan: uji mana yang paling andal ketika ragam tidak homogen
# DAN ukuran kelompok tidak seimbang?
```

### Tantangan 3: Analisis Data Kategorikal Nyata

```python
# TUGAS ANDA
# Gunakan kolom 'cuaca' dan buat kategori kepadatan dari
# jumlah_penumpang pada transjakarta_koridor.csv.
#
# 1. Buat tabel kontingensi cuaca × kategori kepadatan
# 2. Periksa syarat kelayakan chi-square
# 3. Jalankan uji kebebasan
# 4. Hitung Cramér's V
# 5. Telaah residual terstandardisasi — sel mana yang menyimpang?
# 6. Buat heatmap residual
#
# Pertanyaan: bila ditemukan asosiasi, apa saja penjelasan alternatif
# selain "cuaca menyebabkan perubahan jumlah penumpang"?
```

---

## Refleksi

1. Mengapa uji lanjut hanya dilakukan setelah ANOVA signifikan?
2. Apa yang diberitahukan η² yang tidak diberitahukan *p-value*?
3. Mengapa chi-square signifikan tidak menjelaskan **mengapa** asosiasi itu ada?

---

## AI Usage Log

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |

> Nama: ______________  NIM: ______________

---

## Checklist Penyelesaian

- [ ] Notebook dinamai `Lab13_NIM_NamaLengkap.ipynb`
- [ ] Langkah 1–5 selesai
- [ ] Asumsi ANOVA diperiksa sebelum uji dijalankan
- [ ] Ukuran efek (η², Cramér's V) dilaporkan
- [ ] Ketiga tantangan dikerjakan
- [ ] Refleksi terisi
- [ ] AI Usage Log terisi
- [ ] Diunggah ke LMS

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
