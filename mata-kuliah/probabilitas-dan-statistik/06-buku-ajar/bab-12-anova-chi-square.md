# BAB 12: ANOVA DAN UJI CHI-SQUARE

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `PS-Sub-CPMK102-1` | Menjelaskan masalah perbandingan ganda dan menerapkan ANOVA satu arah | C3–C4 |
| `PS-Sub-CPMK102-1` | Menjalankan uji lanjut Tukey dan menafsirkannya | C3 |
| `PS-Sub-CPMK102-1` | Menerapkan uji chi-square kesesuaian dan kebebasan beserta ukuran efeknya | C3–C4 |

---

## 12.1 Masalah Perbandingan Ganda

### 12.1.1 Mengapa Uji-t Berulang Tidak Sahih

Membandingkan 4 kelompok dengan uji-t berpasangan memerlukan C(4,2) = 6 uji. Bila tiap uji memakai α = 0,05:

$$P(\text{sedikitnya satu galat Tipe I}) = 1 - (1-0{,}05)^6 = 0{,}265$$

```python
from math import comb

print(f"{'k kelompok':>12}  {'Jumlah uji':>11}  {'α gabungan':>12}")
for k in [2, 3, 4, 5, 6, 8, 10]:
    n_uji = comb(k, 2)
    print(f"{k:>12}  {n_uji:>11}  {1 - 0.95**n_uji:>11.4f}")
print("\n→ Dengan 10 kelompok, hampir PASTI (89%) ada temuan palsu.")
```

> **Inilah alasan ANOVA ada.** Ia menjawab pertanyaan "apakah ada perbedaan di antara semua kelompok ini?" dengan **satu uji saja**, sehingga α tetap terkendali pada 0,05.

---

## 12.2 ANOVA Satu Arah

### 12.2.1 Gagasan Dasar

ANOVA membandingkan **dua sumber keragaman**:

```
   Keragaman ANTAR kelompok      vs      Keragaman DALAM kelompok
   (apakah pusat kelompok                (seberapa menyebar data
    berjauhan?)                           di dalam tiap kelompok?)

              F = MS_antar / MS_dalam

   F besar  → kelompok memang berbeda
   F ≈ 1    → perbedaan yang tampak wajar sebagai keragaman acak
```

**Hipotesis:**

$$H_0: \mu_1 = \mu_2 = \cdots = \mu_k \qquad H_1: \text{sedikitnya satu } \mu_i \text{ berbeda}$$

> **Perhatikan H₁ baik-baik.** ANOVA hanya memberi tahu **bahwa ada** perbedaan, bukan **di mana** perbedaannya. H₁ bukan "semua berbeda", melainkan "sedikitnya satu berbeda".

### 12.2.2 Tabel ANOVA

| Sumber | df | Jumlah Kuadrat (SS) | Kuadrat Tengah (MS) | F |
|--------|-----|---------------------|---------------------|---|
| Antar kelompok | k − 1 | SS_antar | SS_antar/(k−1) | MS_antar/MS_dalam |
| Dalam kelompok | N − k | SS_dalam | SS_dalam/(N−k) | |
| **Total** | N − 1 | SS_total | | |

dengan SS_total = SS_antar + SS_dalam.

### 12.2.3 Asumsi dan Alternatifnya

| Asumsi | Uji | Bila dilanggar |
|--------|-----|----------------|
| Kebebasan pengamatan | Telaah rancangan | Tidak ada perbaikan statistik |
| Kenormalan residual | Shapiro-Wilk, Q-Q plot | Kruskal-Wallis |
| **Homogenitas ragam** | Levene | **ANOVA Welch** atau Alexander-Govern |

### 12.2.4 Implementasi Lengkap

```python
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def anova_lengkap(df, kol_nilai, kol_kelompok, alpha=0.05):
    data = df[[kol_nilai, kol_kelompok]].dropna()
    kelompok = [g[kol_nilai].values for _, g in data.groupby(kol_kelompok)]
    nama = sorted(data[kol_kelompok].unique())
    k, N = len(kelompok), len(data)

    print(f"{'Kelompok':<26} {'n':>5} {'Mean':>10} {'SD':>10}")
    for nm, g in zip(nama, kelompok):
        print(f"{str(nm):<26} {len(g):>5} {g.mean():>10.3f} {g.std(ddof=1):>10.3f}")

    print("\n--- ASUMSI ---")
    _, p_lev = stats.levene(*kelompok)
    print(f"Homogenitas ragam (Levene): p = {p_lev:.6f} "
          f"→ {'homogen ✓' if p_lev > alpha else 'TIDAK homogen ✗'}")

    print("\n--- UJI UTAMA ---")
    F, p = stats.f_oneway(*kelompok)
    H, p_kw = stats.kruskal(*kelompok)
    print(f"ANOVA klasik   : F({k-1}, {N-k}) = {F:.4f}, p = {p:.8f}")
    print(f"Kruskal-Wallis : H = {H:.4f}, p = {p_kw:.8f}")

    grand = np.concatenate(kelompok); gm = grand.mean()
    ss_antar = sum(len(g)*(g.mean()-gm)**2 for g in kelompok)
    ss_total = ((grand - gm)**2).sum()
    eta2 = ss_antar/ss_total
    besar = "kecil" if eta2 < 0.06 else "sedang" if eta2 < 0.14 else "besar"

    print(f"\nη² = {eta2:.4f} (efek {besar})")
    print(f"→ {eta2*100:.1f}% keragaman dijelaskan oleh {kol_kelompok}")
    print(f"→ {(1-eta2)*100:.1f}% oleh faktor lain")

    if p < alpha:
        print(f"\np < {alpha} → TOLAK H₀. Lanjut uji Tukey:\n")
        print(pairwise_tukeyhsd(data[kol_nilai], data[kol_kelompok], alpha=alpha))
        print("\nCara membaca: bila [lower, upper] MEMUAT NOL,")
        print("pasangan itu tidak berbeda signifikan.")
    else:
        print(f"\np ≥ {alpha} → GAGAL MENOLAK H₀.")
        print("Uji lanjut TIDAK dilakukan.")
    return F, p, eta2

df = pd.read_csv("nilai_mahasiswa_if.csv")
anova_lengkap(df, "jam_belajar", "asal_sekolah")
```

> **Urutan yang benar: ANOVA dulu, uji lanjut hanya bila ANOVA signifikan.**
>
> Melompat langsung ke uji Tukey tanpa ANOVA mengembalikan masalah perbandingan ganda yang justru ingin dihindari.

### 12.2.5 Uji Lanjut Tukey HSD

Uji Tukey (*Honestly Significant Difference*) membandingkan seluruh pasangan sambil mengendalikan galat Tipe I gabungan pada tingkat α.

Keluarannya berisi kolom:

| Kolom | Arti |
|-------|------|
| `meandiff` | Selisih rata-rata antar pasangan |
| `p-adj` | *p-value* yang sudah disesuaikan untuk perbandingan ganda |
| `lower`, `upper` | Interval kepercayaan selisih |
| `reject` | Apakah H₀ ditolak untuk pasangan itu |

---

## 12.3 Uji Chi-Square

### 12.3.1 Uji Kesesuaian (*Goodness of Fit*)

Menguji apakah sebaran data teramati cocok dengan sebaran teoretis yang diharapkan.

$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}, \quad df = k - 1 - m$$

dengan m = jumlah parameter yang ditaksir dari data.

```python
import numpy as np
from scipy import stats

hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
teramati = np.array([52, 38, 41, 44, 65])
n = teramati.sum()
diharapkan = np.full(len(hari), n/len(hari))

print("H₀: laporan bug tersebar MERATA sepanjang hari kerja\n")
print(f"{'Hari':>8} {'O':>6} {'E':>8} {'(O−E)²/E':>10}")
for h, o, e in zip(hari, teramati, diharapkan):
    print(f"{h:>8} {o:>6} {e:>8.1f} {(o-e)**2/e:>10.4f}")

chi2, p = stats.chisquare(teramati, diharapkan)
dof = len(hari) - 1
print(f"\nχ² = {chi2:.4f}, df = {dof}, p = {p:.8f}")
print(f"Nilai kritis (α=0,05) = {stats.chi2.ppf(0.95, dof):.4f}")
print(f"Syarat semua E ≥ 5? {'ya ✓' if (diharapkan >= 5).all() else 'TIDAK ✗'}")

residual = (teramati - diharapkan)/np.sqrt(diharapkan)
print("\nResidual terstandardisasi (|r| > 2 patut diperhatikan):")
for h, r in zip(hari, residual):
    print(f"  {h:>8}: {r:>7.3f}{'  ←' if abs(r) > 2 else ''}")
```

### 12.3.2 Uji Kebebasan

Menguji apakah dua variabel kategorikal saling bebas.

$$\chi^2 = \sum_i\sum_j \frac{(O_{ij}-E_{ij})^2}{E_{ij}}, \quad E_{ij} = \frac{(\text{total baris }i)(\text{total kolom }j)}{N}, \quad df = (r-1)(c-1)$$

```python
import pandas as pd
import numpy as np
from scipy import stats

df["kategori_nilai"] = pd.cut(df["nilai_uas"], bins=[0, 60, 75, 100],
                              labels=["Rendah", "Sedang", "Tinggi"])
tabel = pd.crosstab(df["asal_sekolah"], df["kategori_nilai"])
print("TABEL KONTINGENSI:"); print(tabel)

chi2, p, dof, diharapkan = stats.chi2_contingency(tabel)
print("\nFREKUENSI DIHARAPKAN (bila bebas):")
print(pd.DataFrame(diharapkan, index=tabel.index,
                   columns=tabel.columns).round(2))

print(f"\nχ² = {chi2:.4f}, df = {dof}, p = {p:.8f}")

prop_ok = (diharapkan >= 5).mean()
print(f"Syarat: {prop_ok*100:.1f}% sel punya E ≥ 5 "
      f"({'terpenuhi ✓' if prop_ok >= 0.8 else 'TIDAK ✗'})")

n_total = tabel.values.sum()
v = np.sqrt(chi2 / (n_total * (min(tabel.shape) - 1)))
besar = "kecil" if v < 0.3 else "sedang" if v < 0.5 else "besar"
print(f"\nCramér's V = {v:.4f} (asosiasi {besar})")

res = (tabel.values - diharapkan)/np.sqrt(diharapkan)
print("\nResidual terstandardisasi:")
print(pd.DataFrame(res, index=tabel.index, columns=tabel.columns).round(2))
```

### 12.3.3 Syarat Kelayakan dan Alternatifnya

> **Syarat chi-square:** semua frekuensi **harapan** ≥ 5, atau sedikitnya 80% sel memenuhinya dengan minimum 1.
>
> Perhatikan: syaratnya pada frekuensi **harapan**, bukan teramati. Sel dengan 0 pengamatan boleh saja, asalkan harapannya ≥ 5.

Bila syarat tidak terpenuhi:
1. **Gabungkan kategori** yang secara substantif masuk akal digabung.
2. Gunakan **uji eksak Fisher** (untuk tabel 2×2 atau dengan `scipy.stats.fisher_exact`).
3. Gunakan simulasi Monte Carlo untuk memperoleh *p-value*.

### 12.3.4 Peringatan Interpretasi

> **Chi-square signifikan berarti ada asosiasi — bukan sebab-akibat, dan bukan penjelasan.**
>
> Bila ditemukan asosiasi antara asal sekolah dan kategori nilai, itu **tidak** berarti asal sekolah "menyebabkan" nilai. Bisa jadi ada variabel ketiga — akses fasilitas belajar, latar ekonomi, motivasi — yang menjelaskan keduanya sekaligus.
>
> **Residual terstandardisasi** membantu menemukan sel mana yang menyimpang, tetapi tetap tidak menjelaskan mengapa.

---

## 12.4 Ringkasan Pemilihan Uji

| Situasi | Uji | Ukuran Efek |
|---------|-----|-------------|
| 3+ kelompok, numerik, ragam homogen | ANOVA satu arah | η² |
| 3+ kelompok, ragam tidak homogen | ANOVA Welch / Alexander-Govern | η² |
| 3+ kelompok, sangat tidak Normal | Kruskal-Wallis | ε² |
| ANOVA signifikan, ingin tahu pasangan mana | Tukey HSD | selisih + IK |
| Satu variabel kategorikal vs sebaran teoretis | Chi-square kesesuaian | — |
| Dua variabel kategorikal | Chi-square kebebasan | Cramér's V |
| Sel harapan < 5 | Uji eksak Fisher | *odds ratio* |

---

## AI Corner — Tingkat Mahir

### Yang Paling Sering Dilewatkan AI di Bab Ini

Ketika diminta membandingkan beberapa kelompok, AI biasanya langsung menjalankan ANOVA dengan benar. Tetapi tiga hal hampir selalu terlewat kecuali ditanya:

1. **Pemeriksaan homogenitas ragam** — ia jarang menjalankan uji Levene lebih dulu.
2. **Ukuran efek η²** — hampir selalu hanya melaporkan F dan *p*.
3. **Peringatan bahwa uji lanjut hanya dilakukan bila ANOVA signifikan.**

### Percobaan

Berikan data tiga kelompok dengan ragam yang sangat berbeda (SD 5, 15, dan 40) dan minta AI membandingkannya.

Perhatikan apakah ia:
- Memeriksa homogenitas ragam?
- Memakai ANOVA klasik atau Welch?
- Memperingatkan bahwa asumsi dilanggar?

Lalu tanyakan:

> *"Apakah asumsi homogenitas ragam terpenuhi di sini? Bila tidak, apa dampaknya pada hasil ANOVA klasik, dan apa alternatifnya?"*

### Batas AI dalam Interpretasi Chi-Square

Ini wilayah di mana AI paling rawan melampaui data. Diberi hasil chi-square signifikan, sebagian model akan menulis kalimat seperti:

> *"Hasil ini menunjukkan bahwa asal sekolah memengaruhi prestasi mahasiswa."*

Kata **"memengaruhi"** adalah klaim sebab-akibat yang tidak didukung data observasional.

> **Tanggung jawab Anda sebagai analis:** memeriksa setiap kalimat interpretasi yang dihasilkan AI, dan mengganti kata-kata kausal dengan kata-kata asosiatif ("berkaitan dengan", "berasosiasi dengan") kecuali rancangan penelitiannya memang eksperimental.
>
> Dalam mata kuliah ini, klaim sebab-akibat dari data observasional **mengurangi nilai** pada aspek validitas interpretasi.

---

## Latihan Soal

### Tingkat Dasar

1. Hitung peluang sedikitnya satu galat Tipe I bila membandingkan 6 kelompok dengan uji-t berpasangan pada α = 0,05.

2. Jelaskan apa yang dibandingkan ANOVA: keragaman antar kelompok dengan apa?

3. Lengkapi tabel ANOVA berikut:

   | Sumber | df | SS | MS | F |
   |--------|-----|-----|-----|---|
   | Antar (k=4) | ? | 240 | ? | ? |
   | Dalam (N=44) | ? | 600 | ? | |
   | Total | ? | ? | | |

4. Sebutkan tiga asumsi ANOVA dan uji untuk memeriksa masing-masing.

5. Dari tabel kontingensi 3×2 dengan N = 200 dan χ² = 12,5, hitung df dan Cramér's V.

### Tingkat Menengah

6. Sebuah ANOVA menghasilkan F = 4,82 dengan p = 0,003 untuk 4 kelompok.
   (a) Apa kesimpulannya?
   (b) Apakah berarti keempat kelompok saling berbeda? Jelaskan.
   (c) Apa langkah selanjutnya?
   (d) η² = 0,08. Apa artinya, dan bagaimana Anda melaporkannya kepada pembaca non-teknis?

7. Uji Levene menghasilkan p = 0,002 untuk tiga kelompok yang akan dibandingkan.
   (a) Apa artinya?
   (b) Apakah ANOVA klasik masih layak dipakai?
   (c) Sebutkan dua alternatif dan kapan masing-masing dipilih.
   (d) Apa yang terjadi pada galat Tipe I bila ANOVA klasik tetap dipakai dengan ukuran kelompok tidak seimbang?

8. Sebuah tabel kontingensi 4×3 memiliki beberapa sel dengan frekuensi harapan 2,3 dan 3,8.
   (a) Apakah syarat chi-square terpenuhi?
   (b) Sebutkan tiga cara mengatasinya.
   (c) Bila Anda menggabungkan kategori, atas dasar apa penggabungan itu harus dilakukan?

9. Sebuah laporan menyatakan: *"Uji chi-square menunjukkan bahwa jenis perangkat memengaruhi tingkat konversi (χ²=18,4; p<0,001)."*
   (a) Apa yang salah dengan kata "memengaruhi"?
   (b) Tuliskan ulang kalimat itu secara tepat.
   (c) Informasi apa yang hilang dari laporan itu?
   (d) Sebutkan dua penjelasan alternatif untuk asosiasi itu.

### Tingkat Mahir

10. Bandingkan keandalan tiga uji ketika asumsi dilanggar.
    (a) Simulasikan tiga kelompok dengan SD = 5, 15, 40 dan n = 10, 50, 200 (tidak seimbang).
    (b) Dengan H₀ **benar**, jalankan ANOVA klasik, Alexander-Govern, dan Kruskal-Wallis, 2.000 kali.
    (c) Hitung galat Tipe I empiris masing-masing.
    (d) Ulangi dengan H₀ **salah** dan bandingkan kuasanya.
    (e) Uji mana yang Anda anjurkan sebagai bawaan, dan mengapa?

11. Lakukan analisis lengkap data kategorikal nyata.
    (a) Pilih dua variabel kategorikal dari data BPS atau Satu Data Indonesia.
    (b) Buat tabel kontingensi dan periksa syarat kelayakannya.
    (c) Jalankan uji kebebasan dan hitung Cramér's V.
    (d) Telaah residual terstandardisasi dan buat *heatmap*-nya.
    (e) Tuliskan interpretasi yang **tidak** mengklaim sebab-akibat.
    (f) Sebutkan tiga variabel perancu yang mungkin menjelaskan asosiasi itu.

12. Tulislah panduan (satu halaman) berjudul *"Membandingkan Lebih dari Dua Kelompok: Prosedur dan Jebakannya"*. Sertakan: pohon keputusan pemilihan uji, urutan langkah wajib, kapan uji lanjut boleh dilakukan, ukuran efek yang harus dilaporkan, dan kesalahan interpretasi yang harus dihindari.

---

## Rangkuman

1. **Uji-t berulang menggelembungkan galat Tipe I.** Dengan 4 kelompok, α sebenarnya menjadi 26,5%.
2. **ANOVA** menjawab "adakah perbedaan?" dengan satu uji, membandingkan keragaman antar kelompok terhadap keragaman dalam kelompok.
3. ANOVA hanya memberi tahu **bahwa ada** perbedaan, **bukan di mana**. Uji lanjut Tukey menjawab yang kedua.
4. **Uji lanjut hanya dilakukan bila ANOVA signifikan.**
5. **Asumsi ANOVA**: kebebasan, kenormalan residual, homogenitas ragam. Bila ragam tidak homogen gunakan **Welch**; bila sangat tidak Normal gunakan **Kruskal-Wallis**.
6. **η²** menyatakan berapa persen keragaman dijelaskan faktor kelompok — wajib dilaporkan bersama F dan *p*.
7. **Chi-square kesesuaian** menguji kecocokan dengan sebaran teoretis; **kebebasan** menguji asosiasi dua variabel kategorikal.
8. Syarat chi-square: **frekuensi HARAPAN ≥ 5** (sedikitnya 80% sel). Bila tidak terpenuhi, gabungkan kategori atau gunakan uji Fisher.
9. **Residual terstandardisasi** menunjukkan sel mana yang menyimpang.
10. **Asosiasi bukan sebab-akibat.** Ganti kata kausal dengan kata asosiatif kecuali rancangannya eksperimental.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 10.13, 13. Pearson.
2. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.), Bab 9, 13. Wiley.
3. Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum.
4. Tukey, J. W. (1949). Comparing Individual Means in the Analysis of Variance. *Biometrics*, 5(2), 99–114.
5. Agresti, A. (2018). *An Introduction to Categorical Data Analysis* (3rd ed.). Wiley.
6. Dokumentasi statsmodels — *ANOVA*. <https://www.statsmodels.org/stable/anova.html>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
