# Minggu 12: Uji Hipotesis Dua Sampel dan Uji Proporsi

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 12 |
| **Topik** | Uji-t dua sampel bebas dan berpasangan, uji proporsi, pemeriksaan asumsi, uji nonparametrik, A/B testing |
| **CPL / CPMK** | CPL10 / CPMK102 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Indikator Mingguan** | Menguji hipotesis dua sampel dan uji proporsi, serta memeriksa asumsi yang menyertainya |
| **Level Bloom** | C3–C4 (Menerapkan–Menganalisis) |
| **Durasi** | 150 menit tatap muka |
| **Metode** | Kuliah, latihan terbimbing, studi kasus A/B testing |

---

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Membedakan** (C2) rancangan dua sampel bebas dan berpasangan serta memilih uji yang sesuai.
2. **Melakukan** (C3) uji-t dua sampel bebas dan uji-t berpasangan.
3. **Memeriksa** (C4) asumsi kenormalan, homogenitas ragam, dan kebebasan sebelum menjalankan uji.
4. **Melakukan** (C3) uji proporsi satu dan dua sampel.
5. **Menerapkan** (C3) alternatif nonparametrik ketika asumsi dilanggar.
6. **Merancang** (C4) sebuah A/B test sederhana beserta analisisnya.

---

## Materi Pembelajaran

### 1. Memilih Uji yang Tepat

```
  Dua kelompok yang ingin dibandingkan
  │
  ├── BERPASANGAN? (subjek yang sama diukur dua kali,
  │   atau pasangan yang dijodohkan)
  │   │
  │   ├── YA  → selisih Normal?  ── ya ──→ UJI-T BERPASANGAN
  │   │                          └─ tidak → WILCOXON SIGNED-RANK
  │   │
  │   └── TIDAK (kelompok berbeda dan bebas)
  │       │
  │       ├── Data Normal (atau n besar)?
  │       │   ├── Ragam homogen? ── ya ──→ UJI-T (pooled)
  │       │   └──                  tidak → UJI-T WELCH  ← default yang aman
  │       │
  │       └── Tidak Normal dan n kecil → MANN-WHITNEY U
  │
  └── Data berupa PROPORSI → UJI PROPORSI DUA SAMPEL atau CHI-SQUARE
```

> **Anjuran praktis:** untuk dua kelompok bebas, gunakan **uji-t Welch** sebagai pilihan awal. Ia tidak mengandaikan ragam homogen, dan bila ragamnya memang homogen hasilnya hampir sama dengan uji-t *pooled*. Ini yang dipakai `scipy` secara bawaan (`equal_var=True` harus dinyatakan eksplisit untuk *pooled*).

---

### 2. Uji-t Dua Sampel Bebas

#### 2.1 Rumus

**Welch (ragam tidak diandaikan sama) — dianjurkan:**

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

**Pooled (ragam diandaikan sama):**

$$t = \frac{\bar{x}_1 - \bar{x}_2}{s_p\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}, \quad s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}$$

#### 2.2 Implementasi Lengkap dengan Pemeriksaan Asumsi

```python
import numpy as np
import pandas as pd
from scipy import stats

def uji_dua_sampel_bebas(g1, g2, nama1="Kelompok 1", nama2="Kelompok 2",
                         alpha=0.05):
    """Uji dua sampel bebas lengkap: periksa asumsi, pilih uji, laporkan efek."""
    g1 = np.asarray(g1)[~np.isnan(g1)]
    g2 = np.asarray(g2)[~np.isnan(g2)]
    n1, n2 = len(g1), len(g2)

    print("=" * 62)
    print(f"PERBANDINGAN: {nama1} vs {nama2}")
    print("=" * 62)
    print(f"{nama1:20s}: n={n1:4d}  mean={g1.mean():8.3f}  s={g1.std(ddof=1):7.3f}")
    print(f"{nama2:20s}: n={n2:4d}  mean={g2.mean():8.3f}  s={g2.std(ddof=1):7.3f}")

    # --- Pemeriksaan asumsi ---
    print(f"\n--- PEMERIKSAAN ASUMSI ---")
    _, p_norm1 = stats.shapiro(g1[:5000])
    _, p_norm2 = stats.shapiro(g2[:5000])
    print(f"Kenormalan {nama1:14s}: Shapiro p = {p_norm1:.4f}")
    print(f"Kenormalan {nama2:14s}: Shapiro p = {p_norm2:.4f}")

    # Uji Levene untuk homogenitas ragam (lebih tahan daripada uji-F)
    stat_lev, p_lev = stats.levene(g1, g2)
    print(f"Homogenitas ragam (Levene): p = {p_lev:.4f} "
          f"{'→ ragam homogen' if p_lev > alpha else '→ ragam TIDAK homogen'}")

    normal_ok = (p_norm1 > alpha and p_norm2 > alpha) or (n1 >= 30 and n2 >= 30)
    print(f"\nKesimpulan asumsi: "
          f"{'uji parametrik layak' if normal_ok else 'pertimbangkan uji nonparametrik'}")

    # --- Uji utama ---
    print(f"\n--- HASIL UJI ---")
    t_welch, p_welch = stats.ttest_ind(g1, g2, equal_var=False)
    t_pool, p_pool = stats.ttest_ind(g1, g2, equal_var=True)
    print(f"Uji-t Welch  : t = {t_welch:8.4f}, p = {p_welch:.6f}  ← dianjurkan")
    print(f"Uji-t pooled : t = {t_pool:8.4f}, p = {p_pool:.6f}")

    u_stat, p_mw = stats.mannwhitneyu(g1, g2, alternative="two-sided")
    print(f"Mann-Whitney : U = {u_stat:8.1f}, p = {p_mw:.6f}  (nonparametrik)")

    # --- Ukuran efek Cohen's d ---
    s_pool = np.sqrt(((n1-1)*g1.var(ddof=1) + (n2-1)*g2.var(ddof=1)) / (n1+n2-2))
    d = (g1.mean() - g2.mean()) / s_pool
    besar = ("sangat kecil" if abs(d) < 0.2 else "kecil" if abs(d) < 0.5
             else "sedang" if abs(d) < 0.8 else "besar")

    # --- Interval kepercayaan selisih ---
    se_diff = np.sqrt(g1.var(ddof=1)/n1 + g2.var(ddof=1)/n2)
    df_welch = (se_diff**4) / ((g1.var(ddof=1)/n1)**2/(n1-1) +
                               (g2.var(ddof=1)/n2)**2/(n2-1))
    t_kritis = stats.t.ppf(1 - alpha/2, df_welch)
    selisih = g1.mean() - g2.mean()
    ik = (selisih - t_kritis*se_diff, selisih + t_kritis*se_diff)

    print(f"\n--- UKURAN EFEK DAN PRESISI ---")
    print(f"Selisih rata-rata : {selisih:.4f}")
    print(f"IK {(1-alpha)*100:.0f}% selisih   : [{ik[0]:.4f} , {ik[1]:.4f}]")
    print(f"Cohen's d         : {d:.4f}  (efek {besar})")

    p_pakai = p_welch if normal_ok else p_mw
    uji_pakai = "uji-t Welch" if normal_ok else "Mann-Whitney"
    print(f"\n--- KEPUTUSAN (berdasarkan {uji_pakai}, α = {alpha}) ---")
    if p_pakai < alpha:
        print(f"p = {p_pakai:.6f} < {alpha}  →  TOLAK H₀")
        print(f"Terdapat perbedaan yang signifikan secara statistik.")
        if abs(d) < 0.2:
            print("PERINGATAN: ukuran efeknya sangat kecil — periksa apakah")
            print("perbedaan ini bermakna secara praktis.")
    else:
        print(f"p = {p_pakai:.6f} ≥ {alpha}  →  GAGAL MENOLAK H₀")
        print("Bukti tidak cukup untuk menyatakan ada perbedaan.")
    return {"p": p_pakai, "d": d, "ik": ik}

# Kasus: apakah nilai UAS berbeda antara kelas IF26A dan IF26H?
df = pd.read_csv("nilai_mahasiswa_if.csv")
a = df[df["kelas"] == "IF26A"]["nilai_uas"]
h = df[df["kelas"] == "IF26H"]["nilai_uas"]
uji_dua_sampel_bebas(a, h, "IF26A", "IF26H")
```

---

### 3. Uji-t Berpasangan

#### 3.1 Kapan Dipakai

Ketika **subjek yang sama** diukur dua kali, atau ketika pasangan dijodohkan.

$$t = \frac{\bar{d}}{s_d/\sqrt{n}}, \quad df = n - 1$$

dengan d = selisih tiap pasangan.

| Rancangan | Contoh Informatika |
|-----------|--------------------|
| Sebelum–sesudah | Waktu eksekusi sebelum dan sesudah optimasi, pada **mesin yang sama** |
| Dua perlakuan pada subjek sama | Setiap pengguna mencoba kedua antarmuka |
| Pasangan dijodohkan | Dua server dengan spesifikasi identik |

> **Mengapa berpasangan lebih kuat:** ia menghilangkan variasi antar subjek. Bila sepuluh mesin memiliki kecepatan yang sangat berbeda, uji dua sampel bebas akan tenggelam dalam variasi itu; uji berpasangan hanya melihat **selisih pada mesin yang sama**.

```python
import numpy as np
from scipy import stats

# Waktu eksekusi (detik) pada 12 mesin yang sama, sebelum dan sesudah optimasi
sebelum = np.array([142, 158, 131, 176, 149, 163, 138, 155, 147, 169, 152, 144])
sesudah = np.array([128, 141, 122, 155, 133, 147, 125, 139, 134, 150, 138, 130])

selisih = sebelum - sesudah

print("Uji-t BERPASANGAN")
t_pair, p_pair = stats.ttest_rel(sebelum, sesudah)
print(f"  Rata-rata penurunan : {selisih.mean():.3f} detik")
print(f"  SD selisih          : {selisih.std(ddof=1):.3f}")
print(f"  t = {t_pair:.4f}, p = {p_pair:.8f}")

print("\nBila KELIRU dianalisis sebagai dua sampel bebas:")
t_ind, p_ind = stats.ttest_ind(sebelum, sesudah, equal_var=False)
print(f"  t = {t_ind:.4f}, p = {p_ind:.8f}")
print("\n→ Uji berpasangan jauh lebih peka karena variasi antar mesin")
print("  sudah dihilangkan. Memakai uji yang salah membuang kuasa uji.")

# Ukuran efek untuk data berpasangan
d_pair = selisih.mean() / selisih.std(ddof=1)
print(f"\nCohen's d (berpasangan): {d_pair:.4f}")

# Alternatif nonparametrik
w_stat, p_w = stats.wilcoxon(sebelum, sesudah)
print(f"Wilcoxon signed-rank   : W = {w_stat:.1f}, p = {p_w:.8f}")
```

---

### 4. Uji Proporsi

#### 4.1 Dua Sampel

$$z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1-\hat{p})\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}}, \quad \hat{p} = \frac{x_1 + x_2}{n_1 + n_2}$$

```python
import numpy as np
from statsmodels.stats.proportion import proportions_ztest, confint_proportions_2indep

# Kasus A/B test: konversi grup kontrol vs grup perlakuan
konversi = np.array([148, 191])     # jumlah konversi
total = np.array([1000, 1000])      # jumlah pengunjung

p1, p2 = konversi / total
z, p_value = proportions_ztest(konversi, total)

print("A/B TEST — Uji proporsi dua sampel")
print(f"Grup A (kontrol)  : {konversi[0]}/{total[0]} = {p1*100:.2f}%")
print(f"Grup B (perlakuan): {konversi[1]}/{total[1]} = {p2*100:.2f}%")
print(f"Selisih absolut   : {(p2-p1)*100:.2f} poin persen")
print(f"Kenaikan relatif  : {(p2-p1)/p1*100:.2f}%")
print(f"\nz = {z:.4f}, p-value = {p_value:.6f}")

bawah, atas = confint_proportions_2indep(konversi[1], total[1],
                                         konversi[0], total[0],
                                         method="wald")
print(f"IK 95% selisih    : [{bawah*100:.2f} , {atas*100:.2f}] poin persen")

if p_value < 0.05:
    print("\n→ Perbedaan signifikan secara statistik.")
    print(f"→ Namun perhatikan IK: kenaikan sebenarnya bisa serendah "
          f"{bawah*100:.2f} poin.")
    print("  Apakah itu cukup untuk membenarkan biaya penerapannya?")
```

#### 4.2 Merancang A/B Test yang Sahih

| Tahap | Yang Harus Dilakukan | Kesalahan Umum |
|-------|----------------------|----------------|
| 1. Tetapkan metrik | Satu metrik utama yang ditentukan di muka | Memilih metrik setelah melihat hasil |
| 2. Hitung ukuran sampel | Berdasarkan efek minimum yang bermakna | Menjalankan tes tanpa perhitungan |
| 3. Acak penugasan | Setiap pengguna diacak ke satu grup | Membagi berdasarkan waktu atau lokasi |
| 4. Jalankan sampai selesai | Tidak mengintip dan berhenti saat signifikan | ***Peeking*** — penyebab utama hasil palsu |
| 5. Analisis satu kali | Uji sesuai rencana | Mencoba banyak segmen sampai ada yang signifikan |
| 6. Laporkan lengkap | Efek, IK, dan keterbatasan | Hanya melaporkan *p-value* |

```python
import numpy as np
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

def ukuran_sampel_ab_test(p_dasar, kenaikan_minimum, alpha=0.05, kuasa=0.80):
    """Menghitung n per grup untuk A/B test proporsi."""
    p_baru = p_dasar + kenaikan_minimum
    efek = proportion_effectsize(p_baru, p_dasar)
    analisis = NormalIndPower()
    n = analisis.solve_power(effect_size=efek, alpha=alpha,
                             power=kuasa, ratio=1.0)
    return int(np.ceil(n))

p_dasar = 0.15    # konversi saat ini 15%

print("Ukuran sampel per grup untuk A/B test (α=0,05, kuasa=0,80):")
print(f"{'Kenaikan minimum':>18}  {'n per grup':>12}")
for kenaikan in [0.05, 0.03, 0.02, 0.01, 0.005]:
    n = ukuran_sampel_ab_test(p_dasar, kenaikan)
    print(f"{kenaikan*100:>15.1f} pp  {n:>12,}")

print("\n→ Mendeteksi kenaikan 0,5 poin persen memerlukan puluhan ribu")
print("  pengguna per grup. Tetapkan efek minimum yang BERMAKNA lebih dulu.")
```

> **Bahaya *peeking*.** Bila Anda memeriksa hasil A/B test setiap hari dan berhenti begitu p < 0,05, tingkat galat Tipe I yang sebenarnya bisa melonjak dari 5% ke lebih dari 25%. Tetapkan ukuran sampel di muka, jalankan sampai selesai, lalu analisis **satu kali**.

---

### 5. Uji Nonparametrik

Dipakai ketika asumsi kenormalan tidak terpenuhi dan n kecil.

| Uji Parametrik | Padanan Nonparametrik | Yang Dibandingkan |
|----------------|-----------------------|-------------------|
| Uji-t satu sampel | Wilcoxon signed-rank | Median |
| Uji-t dua sampel bebas | Mann-Whitney U | Sebaran/median |
| Uji-t berpasangan | Wilcoxon signed-rank | Median selisih |
| ANOVA satu arah | Kruskal-Wallis | Sebaran/median |

| Aspek | Parametrik | Nonparametrik |
|-------|------------|---------------|
| Asumsi | Lebih ketat | Lebih longgar |
| Kuasa bila asumsi terpenuhi | Lebih tinggi | Sedikit lebih rendah |
| Tahan pencilan | Tidak | Ya |
| Yang dibandingkan | Rata-rata | Median/sebaran |

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(42)

# Data dengan pencilan ekstrem
g1 = np.concatenate([rng.normal(100, 10, 28), [350, 400]])
g2 = rng.normal(108, 10, 30)

print("Data dengan pencilan ekstrem pada kelompok 1:")
print(f"  g1: mean={g1.mean():.2f}, median={np.median(g1):.2f}")
print(f"  g2: mean={g2.mean():.2f}, median={np.median(g2):.2f}")

t, p_t = stats.ttest_ind(g1, g2, equal_var=False)
u, p_u = stats.mannwhitneyu(g1, g2, alternative="two-sided")

print(f"\nUji-t Welch  : p = {p_t:.6f}  ← terseret pencilan")
print(f"Mann-Whitney : p = {p_u:.6f}  ← lebih tahan")
print("\n→ Kesimpulan kedua uji bisa berbeda. Laporkan keduanya bila ragu,")
print("  dan jelaskan mengapa Anda memilih salah satunya.")
```

---

## Kegiatan Pembelajaran

### Sebelum Kelas (Mandiri — 60 menit)

1. Membaca [Bab 11 buku ajar](../06-buku-ajar/bab-11-uji-hipotesis-dua-sampel.md).
2. Menjawab: apa bedanya "dua sampel bebas" dan "berpasangan"? Beri satu contoh masing-masing dari konteks Informatika.

### Di Kelas (150 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–10' | Pembahasan Lab 11 |
| 10–35' | Kuliah: pohon keputusan memilih uji; bebas vs berpasangan |
| 35–65' | Kuliah + latihan: uji-t dua sampel; Welch vs pooled; uji Levene |
| 65–75' | Istirahat |
| 75–95' | Kuliah + latihan: uji-t berpasangan; demonstrasi kuasa yang hilang bila salah uji |
| 95–120' | **Studio A/B testing:** merancang A/B test untuk fitur aplikasi kampus |
| 120–140' | Kuliah singkat: uji nonparametrik dan kapan dipakai |
| 140–150' | Penutup, penjelasan Lab 12 |

#### Studio: Merancang A/B Test

Dalam kelompok, rancang A/B test untuk salah satu skenario:

1. Menambahkan tombol "Daftar Cepat" pada halaman KRS daring.
2. Mengubah tata letak beranda aplikasi perpustakaan kampus.
3. Mengirim pengingat tugas via notifikasi vs surel.

Setiap kelompok harus menetapkan:
- Metrik utama (satu saja).
- Efek minimum yang dianggap bermakna, beserta alasannya.
- Ukuran sampel per grup.
- Cara pengacakan.
- Berapa lama tes dijalankan.
- Uji statistik yang akan dipakai.

### Setelah Kelas (Mandiri — 180 menit)

1. Mengerjakan [Lab 12](../04-labs/lab-12-ab-testing-dua-sampel.md).
2. Mengerjakan Latihan Soal Bab 11.
3. **Proyek:** menjalankan analisis inferensial.

---

## Penugasan

| Kode | Tugas | Bobot | Batas Waktu |
|------|-------|-------|-------------|
| T-12 | Laporan Lab 12 — A/B testing dua sampel | 1,92% | Sebelum kelas Minggu 13 |

---

## Rangkuman

1. Langkah pertama selalu **memilih uji yang tepat**: berpasangan atau bebas, parametrik atau nonparametrik.
2. Untuk dua kelompok bebas, **uji-t Welch adalah pilihan awal yang aman** — ia tidak mengandaikan ragam homogen.
3. **Uji berpasangan jauh lebih peka** ketika rancangannya memang berpasangan, karena variasi antar subjek dihilangkan. Memakai uji bebas pada data berpasangan membuang kuasa uji.
4. **Asumsi wajib diperiksa**: kenormalan (Shapiro-Wilk, Q-Q plot), homogenitas ragam (Levene), dan kebebasan (telaah rancangan).
5. Uji proporsi dua sampel adalah tulang punggung **A/B testing**.
6. **Ukuran sampel A/B test harus dihitung di muka** berdasarkan efek minimum yang bermakna — bukan ditentukan saat hasilnya sudah terlihat.
7. ***Peeking*** — menghentikan tes begitu p < 0,05 — dapat melonjakkan galat Tipe I dari 5% ke lebih dari 25%.
8. Uji **nonparametrik** lebih tahan pencilan tetapi sedikit kurang berkuasa. Bila kesimpulan kedua jenis uji berbeda, laporkan keduanya dan jelaskan pilihan Anda.

---

## Referensi

1. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 10. Pearson.
2. Kohavi, R., Tang, D., & Xu, Y. (2020). *Trustworthy Online Controlled Experiments*. Cambridge University Press, Bab 2, 17.
3. Delacre, M., Lakens, D., & Leys, C. (2017). Why Psychologists Should by Default Use Welch's t-test. *International Review of Social Psychology*, 30(1), 92–101.
4. Johari, R., et al. (2017). Peeking at A/B Tests. *Proceedings of KDD '17*.
5. Dokumentasi SciPy — *Statistical tests*. <https://docs.scipy.org/doc/scipy/reference/stats.html#hypothesis-tests>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
