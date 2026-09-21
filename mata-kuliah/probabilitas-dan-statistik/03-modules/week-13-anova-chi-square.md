# Minggu 13: ANOVA Satu Arah dan Uji Chi-Square

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 13 |
| **Topik** | Masalah perbandingan ganda, ANOVA satu arah, uji lanjut Tukey, chi-square kesesuaian dan kebebasan |
| **CPL / CPMK** | CPL10 / CPMK102 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Indikator Mingguan** | Menerapkan ANOVA satu arah dan uji chi-square, serta menafsirkan hasilnya |
| **Level Bloom** | C3–C4 (Menerapkan–Menganalisis) |
| **Durasi** | 150 menit tatap muka |
| **Metode** | Kuliah, latihan terbimbing, komputasi |

---

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menjelaskan** (C2) masalah perbandingan ganda dan mengapa uji-t berulang tidak sahih.
2. **Melakukan** (C3) ANOVA satu arah dan membaca tabel ANOVA.
3. **Melakukan** (C3) uji lanjut Tukey untuk mengetahui kelompok mana yang berbeda.
4. **Melakukan** (C3) uji chi-square kesesuaian dan uji chi-square kebebasan.
5. **Menghitung** (C3) dan **menafsirkan** (C4) ukuran efek η² dan Cramér's V.

---

## Materi Pembelajaran

### 1. Masalah Perbandingan Ganda

#### 1.1 Mengapa Tidak Boleh Uji-t Berulang

Membandingkan 4 kelompok dengan uji-t berpasangan memerlukan C(4,2) = 6 uji. Bila tiap uji memakai α = 0,05:

$$P(\text{sedikitnya satu galat Tipe I}) = 1 - (1 - 0{,}05)^6 = 0{,}265$$

```python
import numpy as np
from math import comb

print("Peluang galat Tipe I bila menjalankan banyak uji dengan α = 0,05:")
print(f"{'k kelompok':>12}  {'jumlah uji':>11}  {'α gabungan':>12}")
for k in [2, 3, 4, 5, 6, 10]:
    n_uji = comb(k, 2)
    alpha_gab = 1 - (1 - 0.05) ** n_uji
    print(f"{k:>12}  {n_uji:>11}  {alpha_gab:>11.4f}")

print("\n→ Dengan 10 kelompok, hampir PASTI (89%) ada 'temuan' palsu.")
```

> **Inilah alasan ANOVA ada:** ia menjawab pertanyaan "apakah ada perbedaan di antara semua kelompok ini?" dengan **satu uji saja**, sehingga α tetap terkendali.

---

### 2. ANOVA Satu Arah

#### 2.1 Gagasan Dasar

ANOVA membandingkan **dua sumber keragaman**:

```
   Keragaman ANTAR kelompok      vs      Keragaman DALAM kelompok
   (apakah pusat kelompok                (seberapa menyebar data
    berjauhan?)                           di dalam tiap kelompok?)

              F = MS_antar / MS_dalam

   F besar  → kelompok memang berbeda
   F ≈ 1    → perbedaan yang terlihat wajar saja sebagai keragaman acak
```

**Hipotesis:**

$$H_0: \mu_1 = \mu_2 = \cdots = \mu_k \qquad H_1: \text{sedikitnya satu } \mu_i \text{ berbeda}$$

> **Perhatikan H₁:** ANOVA hanya memberi tahu **bahwa ada** perbedaan, bukan **di mana** perbedaannya. Untuk itu diperlukan uji lanjut.

#### 2.2 Tabel ANOVA

| Sumber | df | Jumlah Kuadrat (SS) | Kuadrat Tengah (MS) | F |
|--------|-----|---------------------|---------------------|---|
| Antar kelompok | k − 1 | SS_antar | SS_antar/(k−1) | MS_antar/MS_dalam |
| Dalam kelompok | N − k | SS_dalam | SS_dalam/(N−k) | |
| Total | N − 1 | SS_total | | |

#### 2.3 Asumsi ANOVA

1. **Kebebasan** — pengamatan saling bebas.
2. **Kenormalan** — residual berdistribusi Normal (atau n tiap kelompok memadai).
3. **Homogenitas ragam** — ragam antar kelompok sebanding (uji Levene).

Bila asumsi 3 dilanggar, gunakan **ANOVA Welch**. Bila asumsi 2 dilanggar berat, gunakan **Kruskal-Wallis**.

#### 2.4 Implementasi Lengkap

```python
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def anova_satu_arah(df, kolom_nilai, kolom_kelompok, alpha=0.05):
    """ANOVA satu arah lengkap: asumsi, uji utama, ukuran efek, uji lanjut."""
    kelompok = [g[kolom_nilai].dropna().values
                for _, g in df.groupby(kolom_kelompok)]
    nama = sorted(df[kolom_kelompok].unique())
    k = len(kelompok)
    N = sum(len(g) for g in kelompok)

    print("=" * 64)
    print(f"ANOVA SATU ARAH: {kolom_nilai} menurut {kolom_kelompok}")
    print("=" * 64)
    for nm, g in zip(nama, kelompok):
        print(f"  {str(nm):22s}: n={len(g):4d}  mean={g.mean():8.3f}  "
              f"s={g.std(ddof=1):7.3f}")

    # --- Asumsi ---
    print(f"\n--- PEMERIKSAAN ASUMSI ---")
    stat_lev, p_lev = stats.levene(*kelompok)
    print(f"Homogenitas ragam (Levene): p = {p_lev:.4f} "
          f"{'→ homogen' if p_lev > alpha else '→ TIDAK homogen, gunakan ANOVA Welch'}")
    for nm, g in zip(nama, kelompok):
        if 3 <= len(g) <= 5000:
            _, p_n = stats.shapiro(g)
            print(f"Kenormalan {str(nm):18s}: Shapiro p = {p_n:.4f}")

    # --- Uji utama ---
    f_stat, p_val = stats.f_oneway(*kelompok)
    print(f"\n--- HASIL ANOVA ---")
    print(f"F({k-1}, {N-k}) = {f_stat:.4f}")
    print(f"p-value    = {p_val:.6f}")

    # --- Ukuran efek eta-kuadrat ---
    grand_mean = np.concatenate(kelompok).mean()
    ss_antar = sum(len(g) * (g.mean() - grand_mean)**2 for g in kelompok)
    ss_total = sum(((g - grand_mean)**2).sum() for g in kelompok)
    eta2 = ss_antar / ss_total
    besar = ("kecil" if eta2 < 0.06 else "sedang" if eta2 < 0.14 else "besar")
    print(f"η² (eta-kuadrat) = {eta2:.4f}  (efek {besar})")
    print(f"  → {eta2*100:.1f}% keragaman {kolom_nilai} dijelaskan oleh {kolom_kelompok}")

    # --- Keputusan ---
    print(f"\n--- KEPUTUSAN (α = {alpha}) ---")
    if p_val < alpha:
        print(f"p < {alpha} → TOLAK H₀. Sedikitnya satu kelompok berbeda.")
        print("Lanjut ke uji Tukey untuk mengetahui kelompok mana.\n")
        tukey = pairwise_tukeyhsd(df[kolom_nilai].dropna(),
                                  df[kolom_kelompok][df[kolom_nilai].notna()],
                                  alpha=alpha)
        print(tukey)
    else:
        print(f"p ≥ {alpha} → GAGAL MENOLAK H₀.")
        print("Bukti tidak cukup untuk menyatakan ada perbedaan antar kelompok.")
        print("Uji lanjut TIDAK dilakukan.")
    return f_stat, p_val, eta2

df = pd.read_csv("nilai_mahasiswa_if.csv")
anova_satu_arah(df, "jam_belajar", "asal_sekolah")
```

> **Urutan yang benar:** ANOVA dulu, uji lanjut **hanya bila** ANOVA signifikan. Langsung melompat ke uji Tukey tanpa ANOVA mengembalikan masalah perbandingan ganda yang justru ingin dihindari.

#### 2.5 Uji Lanjut Tukey

Uji Tukey HSD (*Honestly Significant Difference*) membandingkan seluruh pasangan sambil mengendalikan galat Tipe I gabungan.

Keluarannya berupa tabel dengan kolom:
- `meandiff` — selisih rata-rata antar pasangan
- `p-adj` — *p-value* yang sudah disesuaikan
- `lower`, `upper` — interval kepercayaan selisih
- `reject` — apakah H₀ ditolak untuk pasangan itu

> **Cara membaca:** bila interval [lower, upper] **memuat nol**, maka pasangan itu tidak berbeda signifikan.

---

### 3. Uji Chi-Square

#### 3.1 Uji Kesesuaian (*Goodness of Fit*)

Menguji apakah sebaran data teramati cocok dengan sebaran teoretis yang diharapkan.

$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}, \quad df = k - 1 - (\text{jumlah parameter yang ditaksir})$$

```python
import numpy as np
from scipy import stats

# Kasus: apakah laporan bug tersebar merata sepanjang hari kerja?
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
teramati = np.array([52, 38, 41, 44, 65])
n = teramati.sum()
diharapkan = np.full(5, n / 5)     # hipotesis: merata

chi2, p = stats.chisquare(teramati, diharapkan)

print("UJI CHI-SQUARE KESESUAIAN")
print("H₀: laporan bug tersebar merata sepanjang hari kerja\n")
print(f"{'Hari':>8}  {'Teramati':>9}  {'Diharapkan':>11}  {'(O−E)²/E':>10}")
for h, o, e in zip(hari, teramati, diharapkan):
    print(f"{h:>8}  {o:>9}  {e:>11.1f}  {(o-e)**2/e:>10.4f}")

print(f"\nχ² = {chi2:.4f}, df = {len(hari)-1}, p = {p:.6f}")

# Syarat kelayakan
print(f"\nSyarat: semua E ≥ 5? {'ya' if (diharapkan >= 5).all() else 'TIDAK'}")

if p < 0.05:
    print("\n→ TOLAK H₀. Sebaran tidak merata.")
    print("  Senin dan Jumat menyumbang laporan lebih banyak.")
    print("  Kemungkinan penyebab: deployment akhir pekan dan tekanan akhir sprint.")
```

#### 3.2 Uji Kebebasan

Menguji apakah dua variabel kategorikal saling bebas.

$$\chi^2 = \sum_{i}\sum_{j} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}, \quad E_{ij} = \frac{(\text{total baris } i)(\text{total kolom } j)}{N}$$

$$df = (r-1)(c-1)$$

```python
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("nilai_mahasiswa_if.csv")
df["kategori_nilai"] = pd.cut(df["nilai_uas"],
                              bins=[0, 60, 75, 100],
                              labels=["Rendah", "Sedang", "Tinggi"])

tabel = pd.crosstab(df["asal_sekolah"], df["kategori_nilai"])
print("Tabel kontingensi (teramati):")
print(tabel)

chi2, p, dof, diharapkan = stats.chi2_contingency(tabel)

print(f"\nFrekuensi yang diharapkan bila kedua variabel bebas:")
print(pd.DataFrame(diharapkan, index=tabel.index,
                   columns=tabel.columns).round(2))

print(f"\nχ² = {chi2:.4f}")
print(f"df = {dof}")
print(f"p-value = {p:.6f}")

# Syarat kelayakan: semua E ≥ 5, atau sedikitnya 80% sel punya E ≥ 5
proporsi_ok = (diharapkan >= 5).mean()
print(f"\nSyarat kelayakan: {proporsi_ok*100:.1f}% sel memiliki E ≥ 5")
if proporsi_ok < 0.8:
    print("  → Syarat TIDAK terpenuhi. Gabungkan kategori atau gunakan uji Fisher.")

# Ukuran efek Cramér's V
n = tabel.values.sum()
min_dim = min(tabel.shape) - 1
cramers_v = np.sqrt(chi2 / (n * min_dim))
besar = ("kecil" if cramers_v < 0.3 else
         "sedang" if cramers_v < 0.5 else "besar")
print(f"\nCramér's V = {cramers_v:.4f}  (asosiasi {besar})")

if p < 0.05:
    print("\n→ TOLAK H₀. Terdapat asosiasi antara asal sekolah dan kategori nilai.")
    print("  CATATAN: asosiasi BUKAN sebab-akibat. Bisa jadi ada variabel")
    print("  ketiga (misalnya akses fasilitas belajar) yang menjelaskan keduanya.")
else:
    print("\n→ GAGAL MENOLAK H₀. Tidak cukup bukti adanya asosiasi.")
```

#### 3.3 Menelaah Residual Terstandardisasi

Ketika chi-square signifikan, residual terstandardisasi menunjukkan **sel mana** yang menyumbang paling besar.

```python
residual = (tabel.values - diharapkan) / np.sqrt(diharapkan)
print("Residual terstandardisasi (|nilai| > 2 patut diperhatikan):")
print(pd.DataFrame(residual, index=tabel.index,
                   columns=tabel.columns).round(2))
```

---

### 4. Ringkasan Pemilihan Uji

| Situasi | Uji | Ukuran Efek |
|---------|-----|-------------|
| 3+ kelompok, data numerik, ragam homogen | ANOVA satu arah | η² |
| 3+ kelompok, ragam tidak homogen | ANOVA Welch | η² |
| 3+ kelompok, tidak Normal | Kruskal-Wallis | ε² |
| ANOVA signifikan, ingin tahu pasangan mana | Tukey HSD | selisih + IK |
| Satu variabel kategorikal vs sebaran teoretis | Chi-square kesesuaian | — |
| Dua variabel kategorikal | Chi-square kebebasan | Cramér's V |
| Chi-square dengan sel harapan < 5 | Uji eksak Fisher | *odds ratio* |

---

## Kegiatan Pembelajaran

### Sebelum Kelas (Mandiri — 60 menit)

1. Membaca [Bab 12 buku ajar](../06-buku-ajar/bab-12-anova-chi-square.md).
2. Menghitung: bila 5 kelompok dibandingkan dengan uji-t berpasangan pada α = 0,05, berapa peluang sedikitnya satu galat Tipe I?

### Di Kelas (150 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–10' | Pembahasan Lab 12 |
| 10–30' | Kuliah: masalah perbandingan ganda; demonstrasi inflasi α |
| 30–65' | Kuliah + latihan: ANOVA satu arah; membaca tabel ANOVA; asumsi |
| 65–75' | Istirahat |
| 75–95' | Kuliah + latihan: uji lanjut Tukey dan cara membacanya |
| 95–125' | Kuliah + latihan: chi-square kesesuaian dan kebebasan; Cramér's V |
| 125–145' | Studio: analisis data TransJakarta dengan ANOVA |
| 145–150' | **Kuis 4** (Minggu 11–13) |

> **Catatan:** Kuis 4 dilaksanakan pada pertemuan ini, bobot 3,75%.

#### Studio: Perbandingan Koridor TransJakarta

Menggunakan `transjakarta_koridor.csv`:

1. Apakah jumlah penumpang berbeda antar koridor? (ANOVA)
2. Periksa asumsi lebih dulu — apakah ragamnya homogen?
3. Bila signifikan, koridor mana yang berbeda? (Tukey)
4. Hitung η² — seberapa besar peran koridor dalam menjelaskan keragaman?
5. Apakah kategori cuaca berasosiasi dengan tingkat kepadatan? (Chi-square)

### Setelah Kelas (Mandiri — 180 menit)

1. Mengerjakan [Lab 13](../04-labs/lab-13-anova-chi-square.md).
2. Mengerjakan Latihan Soal Bab 12.
3. **Proyek:** menyelesaikan analisis inferensial, mulai menyusun laporan.

---

## Penugasan

| Kode | Tugas | Bobot | Batas Waktu |
|------|-------|-------|-------------|
| T-13 | Laporan Lab 13 — ANOVA dan chi-square | 1,92% | Sebelum kelas Minggu 14 |
| K-04 | Kuis 4 — Minggu 11–13 | 3,75% | Di kelas Minggu 13 |

---

## Rangkuman

1. **Uji-t berulang pada banyak kelompok menggelembungkan galat Tipe I.** Dengan 4 kelompok, α yang sebenarnya menjadi 26,5%, bukan 5%.
2. **ANOVA** menjawab "adakah perbedaan?" dengan satu uji, membandingkan keragaman antar kelompok terhadap keragaman dalam kelompok.
3. ANOVA hanya memberi tahu **bahwa ada** perbedaan, **bukan di mana**. Uji lanjut Tukey menjawab yang kedua.
4. **Uji lanjut hanya dilakukan bila ANOVA signifikan.** Melompat langsung ke Tukey mengembalikan masalah perbandingan ganda.
5. **Asumsi ANOVA**: kebebasan, kenormalan residual, homogenitas ragam. Bila ragam tidak homogen gunakan ANOVA Welch; bila sangat tidak Normal gunakan Kruskal-Wallis.
6. **η²** menyatakan berapa persen keragaman dijelaskan oleh faktor kelompok — ukuran efek yang wajib dilaporkan bersama F dan *p-value*.
7. **Chi-square kesesuaian** menguji kecocokan dengan sebaran teoretis; **chi-square kebebasan** menguji asosiasi dua variabel kategorikal.
8. Syarat chi-square: **semua frekuensi harapan ≥ 5** (atau sedikitnya 80% sel). Bila tidak terpenuhi, gabungkan kategori atau gunakan uji eksak Fisher.
9. **Asosiasi bukan sebab-akibat.** Chi-square signifikan tidak menjelaskan mengapa asosiasi itu ada.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 10.13, 13. Pearson.
2. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.), Bab 9, 13. Wiley.
3. Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum.
4. Dokumentasi statsmodels — `pairwise_tukeyhsd`, `anova_lm`. <https://www.statsmodels.org/stable/anova.html>
5. Dokumentasi SciPy — `f_oneway`, `chi2_contingency`, `chisquare`.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
