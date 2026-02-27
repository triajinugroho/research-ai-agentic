# Minggu 11: ANOVA dan Uji Non-Parametrik

## Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

**Semester:** Genap 2025/2026
**CPMK:** CPMK-6 — Menganalisis data menggunakan ANOVA, uji non-parametrik, dan analisis data kategorikal sesuai karakteristik data
**Sub-CPMK:** 11.1 (One-way ANOVA), 11.2 (Uji non-parametrik)
**Bloom's Taxonomy:** C4 (Analyze)
**Durasi:** 100 menit (50 menit teori + 50 menit praktikum)

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Menjelaskan** kapan dan mengapa kita perlu membandingkan lebih dari 2 kelompok sekaligus (Sub-CPMK 11.1)
2. **Melaksanakan** one-way ANOVA dan menginterpretasi F-statistic serta p-value (Sub-CPMK 11.1)
3. **Memeriksa** asumsi ANOVA (normalitas, homogeneity of variance, independence) dan menentukan apakah asumsi terpenuhi (Sub-CPMK 11.1)
4. **Melakukan** post-hoc test (Tukey's HSD) untuk mengetahui kelompok mana yang berbeda (Sub-CPMK 11.1)
5. **Menerapkan** uji non-parametrik (Mann-Whitney U, Kruskal-Wallis) ketika asumsi parametrik tidak terpenuhi (Sub-CPMK 11.2)
6. **Memutuskan** uji mana yang tepat berdasarkan karakteristik data menggunakan decision tree (Sub-CPMK 11.2)

---

## Materi

### 11.1 Membandingkan Lebih dari Dua Kelompok

#### 11.1.1 Kenapa Tidak Pakai Banyak t-Test?

Bayangkan kita ingin membandingkan pengeluaran rumah tangga di **4 wilayah Indonesia**: Jawa, Sumatera, Kalimantan, dan Sulawesi. Kita bisa melakukan t-test berpasangan:
- Jawa vs Sumatera
- Jawa vs Kalimantan
- Jawa vs Sulawesi
- Sumatera vs Kalimantan
- Sumatera vs Sulawesi
- Kalimantan vs Sulawesi

Itu **6 kali t-test** untuk 4 kelompok saja! Dengan 6 kelompok, kita butuh 15 t-test.

**Masalah utama: Inflasi Error Type I**

Setiap t-test memiliki risiko *false positive* sebesar α = 0.05 (5%). Ketika kita melakukan banyak t-test:

```
P(minimal 1 false positive) = 1 - (1 - α)^k

Untuk 6 perbandingan: 1 - (0.95)^6 = 0.265 = 26.5%!
```

Artinya, ada kemungkinan 26.5% kita salah menyimpulkan ada perbedaan padahal tidak ada. Ini jauh dari 5% yang kita inginkan.

**Solusi: ANOVA** — satu uji yang membandingkan semua kelompok sekaligus.

#### 11.1.2 One-Way ANOVA: Konsep

ANOVA (Analysis of Variance) menguji apakah **rata-rata** tiga kelompok atau lebih **berbeda secara signifikan**. Meskipun namanya "Analysis of Variance," yang diuji sebenarnya adalah **perbedaan rata-rata**.

**Hipotesis:**
- **H₀:** μ₁ = μ₂ = μ₃ = ... = μₖ (semua rata-rata kelompok sama)
- **H₁:** Minimal satu rata-rata kelompok berbeda

**Ide dasar ANOVA:**
Membandingkan dua sumber variasi:

1. **Between-group variance (SSB):** Variasi rata-rata antar kelompok — seberapa berbeda kelompok-kelompok tersebut satu sama lain
2. **Within-group variance (SSW):** Variasi data dalam masing-masing kelompok — seberapa tersebar data dalam tiap kelompok

Jika variasi *antar kelompok* jauh lebih besar dari variasi *dalam kelompok*, maka kelompok-kelompok tersebut kemungkinan memang berbeda.

#### 11.1.3 F-Statistic dan F-Distribution

F-statistic mengukur rasio antara variasi antar kelompok dan variasi dalam kelompok:

```
        MSB     SSB / (k - 1)
F = ───── = ─────────────────
        MSW     SSW / (N - k)
```

Di mana:
- **MSB** = Mean Square Between (variasi rata-rata antar kelompok)
- **MSW** = Mean Square Within (variasi rata-rata dalam kelompok)
- **k** = jumlah kelompok
- **N** = jumlah total observasi

**Interpretasi F:**
- F mendekati 1 → variasi antar kelompok hampir sama dengan variasi dalam kelompok → tidak ada perbedaan signifikan
- F jauh lebih besar dari 1 → variasi antar kelompok jauh lebih besar → kemungkinan ada perbedaan signifikan

**Keputusan:** Bandingkan p-value dari F-statistic dengan α (biasanya 0.05):
- p-value < α → **Tolak H₀** → minimal satu kelompok berbeda
- p-value ≥ α → **Gagal tolak H₀** → tidak cukup bukti bahwa ada perbedaan

> **Penting:** ANOVA hanya mengatakan "ada perbedaan." Untuk tahu *kelompok mana* yang berbeda, kita perlu **post-hoc test**.

#### 11.1.4 Asumsi ANOVA

ANOVA valid jika tiga asumsi terpenuhi:

| Asumsi | Penjelasan | Cara Cek | Uji Formal |
|--------|-----------|----------|------------|
| **Normalitas** | Data dalam setiap kelompok berdistribusi normal | Histogram, Q-Q plot | Shapiro-Wilk test per kelompok |
| **Homogeneity of Variance** | Variansi semua kelompok kira-kira sama | Box plot (lebar box mirip) | Levene's test |
| **Independence** | Observasi saling independen | Desain penelitian | — (dipastikan dari pengambilan data) |

**Jika asumsi dilanggar:**
- Normalitas ringan dilanggar + sampel besar → ANOVA masih cukup robust
- Homogeneity dilanggar → Gunakan Welch's ANOVA
- Asumsi dilanggar parah → Gunakan alternatif non-parametrik (Kruskal-Wallis)

#### 11.1.5 Post-Hoc Test: Tukey's HSD

Jika ANOVA menunjukkan perbedaan signifikan (p < 0.05), kita perlu tahu **kelompok mana** yang berbeda. **Tukey's Honestly Significant Difference (HSD)** membandingkan setiap pasangan kelompok sambil mengontrol error Type I.

Tukey's HSD memberikan:
- Perbedaan rata-rata antar setiap pasangan kelompok
- p-value untuk setiap perbandingan (sudah dikoreksi untuk *multiple comparisons*)
- Confidence interval untuk perbedaan

---

### 11.2 Uji Non-Parametrik

#### 11.2.1 Kapan Asumsi Parametrik Dilanggar?

Uji parametrik (seperti t-test dan ANOVA) mengasumsikan data berdistribusi normal (atau mendekati normal). Namun, dalam praktik, kita sering menemui:

- Data sangat **skewed** (misalnya data pendapatan)
- Data memiliki **outlier** ekstrem
- Data berskala **ordinal** (misalnya skala Likert 1-5)
- **Sampel kecil** sehingga normalitas sulit diverifikasi

Dalam kasus-kasus ini, uji **non-parametrik** menjadi alternatif yang lebih tepat.

#### 11.2.2 Mann-Whitney U Test (2 Kelompok)

Mann-Whitney U test adalah alternatif non-parametrik untuk **independent two-sample t-test**. Uji ini membandingkan **distribusi** (bukan rata-rata) dua kelompok independen.

**Cara kerja:**
1. Gabungkan semua data dari kedua kelompok
2. Berikan rank (peringkat) dari yang terkecil ke terbesar
3. Jumlahkan rank untuk masing-masing kelompok
4. Hitung U-statistic dan bandingkan dengan distribusi null

**Hipotesis:**
- H₀: Distribusi kedua kelompok sama
- H₁: Distribusi kedua kelompok berbeda

**Kapan digunakan:**
- Data ordinal
- Data numerik tapi tidak normal
- Sampel kecil
- Ada outlier yang mempengaruhi rata-rata

#### 11.2.3 Kruskal-Wallis Test (>2 Kelompok)

Kruskal-Wallis test adalah alternatif non-parametrik untuk **one-way ANOVA**. Cara kerjanya serupa dengan Mann-Whitney tetapi untuk tiga kelompok atau lebih.

**Hipotesis:**
- H₀: Distribusi semua kelompok sama
- H₁: Minimal satu kelompok berbeda

**Setelah Kruskal-Wallis signifikan:** Gunakan post-hoc test seperti **Dunn's test** (dengan koreksi Bonferroni) untuk mengetahui kelompok mana yang berbeda.

#### 11.2.4 Decision Tree: Parametrik vs Non-Parametrik

Berikut panduan memilih uji yang tepat:

```
Berapa kelompok yang dibandingkan?
│
├── 2 kelompok
│   ├── Data normal + variansi homogen?
│   │   ├── YA → Independent t-test
│   │   └── TIDAK → Mann-Whitney U test
│   └── Data berpasangan?
│       ├── Normal → Paired t-test
│       └── Tidak normal → Wilcoxon Signed-Rank test
│
└── >2 kelompok
    ├── Data normal + variansi homogen?
    │   ├── YA → One-way ANOVA → (jika signifikan) → Tukey's HSD
    │   └── TIDAK (variansi beda) → Welch's ANOVA
    └── Data tidak normal / ordinal?
        └── Kruskal-Wallis → (jika signifikan) → Dunn's test
```

**Ringkasan tabel:**

| Situasi | Parametrik | Non-Parametrik |
|---------|-----------|----------------|
| 2 kelompok independen | Independent t-test | Mann-Whitney U |
| 2 kelompok berpasangan | Paired t-test | Wilcoxon Signed-Rank |
| >2 kelompok independen | One-way ANOVA | Kruskal-Wallis |
| Post-hoc (parametrik) | Tukey's HSD | — |
| Post-hoc (non-parametrik) | — | Dunn's test |

---

## Contoh Kode Python

### Persiapan Data

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Simulasi data: Pengeluaran rumah tangga per bulan (ribu Rp) di 4 wilayah
np.random.seed(2025)

data = pd.DataFrame({
    'wilayah': (
        ['Jawa'] * 40 +
        ['Sumatera'] * 35 +
        ['Kalimantan'] * 30 +
        ['Sulawesi'] * 25
    ),
    'pengeluaran': np.concatenate([
        np.random.normal(4500, 800, 40),    # Jawa
        np.random.normal(3800, 900, 35),    # Sumatera
        np.random.normal(4200, 750, 30),    # Kalimantan
        np.random.normal(3500, 850, 25)     # Sulawesi
    ])
})

print("=== Preview Data ===")
print(data.head(10))
print(f"\nJumlah data per wilayah:")
print(data['wilayah'].value_counts())
print(f"\n=== Statistik per Wilayah ===")
print(data.groupby('wilayah')['pengeluaran'].describe().round(0))
```

### Visualisasi Perbandingan Kelompok

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Box plot
sns.boxplot(data=data, x='wilayah', y='pengeluaran', ax=axes[0],
            palette='Set2', order=['Jawa', 'Sumatera', 'Kalimantan', 'Sulawesi'])
axes[0].set_xlabel('Wilayah', fontsize=11)
axes[0].set_ylabel('Pengeluaran (Ribu Rp/Bulan)', fontsize=11)
axes[0].set_title('Distribusi Pengeluaran per Wilayah', fontsize=13)
axes[0].grid(True, alpha=0.3, axis='y')

# Violin plot (lebih informatif tentang distribusi)
sns.violinplot(data=data, x='wilayah', y='pengeluaran', ax=axes[1],
               palette='Set2', order=['Jawa', 'Sumatera', 'Kalimantan', 'Sulawesi'],
               inner='box')
axes[1].set_xlabel('Wilayah', fontsize=11)
axes[1].set_ylabel('Pengeluaran (Ribu Rp/Bulan)', fontsize=11)
axes[1].set_title('Violin Plot: Distribusi Pengeluaran', fontsize=13)
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()
```

### Cek Asumsi ANOVA

```python
# ============================================================
# LANGKAH 1: Cek Asumsi sebelum ANOVA
# ============================================================

wilayah_list = ['Jawa', 'Sumatera', 'Kalimantan', 'Sulawesi']
kelompok_data = [data[data['wilayah'] == w]['pengeluaran'] for w in wilayah_list]

# Asumsi 1: Normalitas (Shapiro-Wilk test per kelompok)
print("=== Cek Normalitas (Shapiro-Wilk Test) ===")
print(f"{'Wilayah':<15} {'W-stat':<10} {'p-value':<10} {'Normal?'}")
print("─" * 50)
semua_normal = True
for w, d in zip(wilayah_list, kelompok_data):
    stat, p = stats.shapiro(d)
    normal = "Ya" if p > 0.05 else "TIDAK"
    if p <= 0.05:
        semua_normal = False
    print(f"{w:<15} {stat:<10.4f} {p:<10.4f} {normal}")

# Asumsi 2: Homogeneity of Variance (Levene's Test)
print(f"\n=== Cek Homogenitas Variansi (Levene's Test) ===")
stat_lev, p_lev = stats.levene(*kelompok_data)
print(f"Levene's statistic: {stat_lev:.4f}")
print(f"p-value: {p_lev:.4f}")
print(f"Variansi homogen? {'Ya' if p_lev > 0.05 else 'TIDAK'} (α = 0.05)")

# Keputusan: uji mana yang digunakan?
print(f"\n=== Keputusan ===")
if semua_normal and p_lev > 0.05:
    print("Semua asumsi terpenuhi → Gunakan One-way ANOVA")
elif not semua_normal:
    print("Normalitas tidak terpenuhi → Pertimbangkan Kruskal-Wallis")
else:
    print("Variansi tidak homogen → Pertimbangkan Welch's ANOVA atau Kruskal-Wallis")
```

### One-Way ANOVA

```python
# ============================================================
# LANGKAH 2: One-Way ANOVA
# ============================================================

f_stat, p_anova = stats.f_oneway(*kelompok_data)

print("=== One-Way ANOVA ===")
print(f"F-statistic: {f_stat:.4f}")
print(f"p-value: {p_anova:.6f}")
print(f"\nKeputusan (α = 0.05):")
if p_anova < 0.05:
    print(f"  p-value ({p_anova:.6f}) < 0.05 → TOLAK H₀")
    print(f"  Kesimpulan: Ada perbedaan signifikan pengeluaran antar wilayah.")
    print(f"  → Lanjut ke post-hoc test untuk mengetahui wilayah mana yang berbeda.")
else:
    print(f"  p-value ({p_anova:.6f}) >= 0.05 → GAGAL TOLAK H₀")
    print(f"  Kesimpulan: Tidak cukup bukti adanya perbedaan pengeluaran antar wilayah.")
```

### Post-Hoc Test: Tukey's HSD

```python
# ============================================================
# LANGKAH 3: Post-Hoc Test (Tukey's HSD)
# ============================================================

from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Tukey's HSD
tukey = pairwise_tukeyhsd(
    endog=data['pengeluaran'],
    groups=data['wilayah'],
    alpha=0.05
)

print("=== Post-Hoc: Tukey's HSD ===")
print(tukey)

# Visualisasi Tukey's HSD
fig = tukey.plot_simultaneous(figsize=(8, 5))
plt.xlabel('Pengeluaran (Ribu Rp/Bulan)', fontsize=11)
plt.title('Tukey HSD: Confidence Intervals per Wilayah', fontsize=13)
plt.tight_layout()
plt.show()

# Interpretasi
print("\n=== Interpretasi ===")
print("Pasangan dengan 'reject=True' menunjukkan perbedaan signifikan.")
print("Pasangan dengan 'reject=False' tidak berbeda secara signifikan.")
```

### Mann-Whitney U Test (Contoh 2 Kelompok)

```python
# ============================================================
# UJI NON-PARAMETRIK: Mann-Whitney U Test
# ============================================================

# Contoh: membandingkan Jawa vs Sulawesi saja
jawa = data[data['wilayah'] == 'Jawa']['pengeluaran']
sulawesi = data[data['wilayah'] == 'Sulawesi']['pengeluaran']

stat_mw, p_mw = stats.mannwhitneyu(jawa, sulawesi, alternative='two-sided')

print("=== Mann-Whitney U Test: Jawa vs Sulawesi ===")
print(f"U-statistic: {stat_mw:.2f}")
print(f"p-value: {p_mw:.6f}")
if p_mw < 0.05:
    print(f"Kesimpulan: Distribusi pengeluaran Jawa dan Sulawesi berbeda signifikan.")
else:
    print(f"Kesimpulan: Tidak ada perbedaan signifikan distribusi pengeluaran.")

# Bandingkan dengan t-test
stat_t, p_t = stats.ttest_ind(jawa, sulawesi)
print(f"\nPerbandingan: t-test p-value = {p_t:.6f}")
print(f"             Mann-Whitney p-value = {p_mw:.6f}")
print(f"Kedua uji memberikan kesimpulan yang {'sama' if (p_t < 0.05) == (p_mw < 0.05) else 'BERBEDA'}.")
```

### Kruskal-Wallis Test (>2 Kelompok Non-Parametrik)

```python
# ============================================================
# UJI NON-PARAMETRIK: Kruskal-Wallis Test
# ============================================================

stat_kw, p_kw = stats.kruskal(*kelompok_data)

print("=== Kruskal-Wallis Test ===")
print(f"H-statistic: {stat_kw:.4f}")
print(f"p-value: {p_kw:.6f}")
if p_kw < 0.05:
    print(f"Kesimpulan: Ada perbedaan signifikan distribusi pengeluaran antar wilayah.")
    print(f"→ Lanjut ke Dunn's test untuk post-hoc.")
else:
    print(f"Kesimpulan: Tidak cukup bukti adanya perbedaan.")

# Perbandingan ANOVA vs Kruskal-Wallis
print(f"\nPerbandingan:")
print(f"  ANOVA p-value:          {p_anova:.6f}")
print(f"  Kruskal-Wallis p-value: {p_kw:.6f}")
```

### Post-Hoc Dunn's Test (untuk Kruskal-Wallis)

```python
# Install jika belum: pip install scikit-posthocs
# Di Google Colab: !pip install scikit-posthocs

import scikit_posthocs as sp

# Dunn's test dengan koreksi Bonferroni
dunn_result = sp.posthoc_dunn(
    data, val_col='pengeluaran', group_col='wilayah',
    p_adjust='bonferroni'
)

print("=== Post-Hoc: Dunn's Test (Bonferroni correction) ===")
print("P-values:")
print(dunn_result.round(4))

# Visualisasi heatmap p-values
plt.figure(figsize=(7, 5))
sns.heatmap(dunn_result, annot=True, fmt='.4f', cmap='RdYlGn_r',
            vmin=0, vmax=0.1, linewidths=0.5)
plt.title("Dunn's Test P-Values\n(Hijau = Tidak Signifikan, Merah = Signifikan)",
          fontsize=12)
plt.tight_layout()
plt.show()

print("\nPasangan dengan p-value < 0.05 berbeda signifikan.")
```

---

## Studi Kasus: Perbandingan Pengeluaran Rumah Tangga Antar Wilayah Indonesia

### Konteks

Indonesia terdiri dari berbagai wilayah dengan karakteristik ekonomi yang beragam. Apakah pengeluaran rumah tangga per bulan berbeda secara signifikan antar wilayah besar (Jawa, Sumatera, Kalimantan, Sulawesi)? Analisis ini penting untuk perencanaan kebijakan ekonomi dan sosial.

### Analisis Lengkap

```python
# ============================================================
# STUDI KASUS LENGKAP: Pengeluaran Rumah Tangga
# ============================================================

# 1. Deskriptif
print("=" * 60)
print("STUDI KASUS: Perbandingan Pengeluaran Rumah Tangga")
print("=" * 60)

ringkasan = data.groupby('wilayah')['pengeluaran'].agg(
    ['count', 'mean', 'median', 'std', 'min', 'max']
).round(0)
ringkasan.columns = ['N', 'Mean', 'Median', 'Std', 'Min', 'Max']
print("\n1. Statistik Deskriptif (Ribu Rp/Bulan):")
print(ringkasan)

# 2. Cek asumsi
print("\n2. Cek Asumsi:")
asumsi_normal = True
for w in wilayah_list:
    d = data[data['wilayah'] == w]['pengeluaran']
    _, p = stats.shapiro(d)
    status = "Normal" if p > 0.05 else "Tidak Normal"
    print(f"   Normalitas {w}: p = {p:.4f} ({status})")
    if p <= 0.05:
        asumsi_normal = False

_, p_lev = stats.levene(*kelompok_data)
asumsi_homogen = p_lev > 0.05
print(f"   Levene's test: p = {p_lev:.4f} ({'Homogen' if asumsi_homogen else 'Tidak Homogen'})")

# 3. Pilih dan jalankan uji yang tepat
print("\n3. Pengujian:")
if asumsi_normal and asumsi_homogen:
    # Parametrik: ANOVA
    f_val, p_val = stats.f_oneway(*kelompok_data)
    print(f"   Uji: One-Way ANOVA (asumsi terpenuhi)")
    print(f"   F = {f_val:.4f}, p = {p_val:.6f}")
    uji_signifikan = p_val < 0.05
else:
    # Non-parametrik: Kruskal-Wallis
    h_val, p_val = stats.kruskal(*kelompok_data)
    print(f"   Uji: Kruskal-Wallis (asumsi parametrik tidak terpenuhi)")
    print(f"   H = {h_val:.4f}, p = {p_val:.6f}")
    uji_signifikan = p_val < 0.05

print(f"   Signifikan? {'YA' if uji_signifikan else 'TIDAK'} (α = 0.05)")

# 4. Post-hoc (jika signifikan)
if uji_signifikan:
    print("\n4. Post-Hoc Test:")
    if asumsi_normal and asumsi_homogen:
        tukey_result = pairwise_tukeyhsd(data['pengeluaran'], data['wilayah'], 0.05)
        print(tukey_result)
    else:
        dunn = sp.posthoc_dunn(data, val_col='pengeluaran',
                               group_col='wilayah', p_adjust='bonferroni')
        print("   Dunn's test (Bonferroni):")
        print(dunn.round(4))

# 5. Kesimpulan
print("\n5. Kesimpulan:")
if uji_signifikan:
    print("   Terdapat perbedaan signifikan pengeluaran rumah tangga antar wilayah.")
    print("   Analisis post-hoc menunjukkan pasangan wilayah yang berbeda.")
    print("   Informasi ini berguna untuk perencanaan subsidi dan kebijakan ekonomi.")
else:
    print("   Tidak terdapat perbedaan signifikan pengeluaran antar wilayah.")
```

### Diskusi Studi Kasus

1. **Mengapa ada perbedaan?** Perbedaan pengeluaran antar wilayah bisa disebabkan oleh perbedaan biaya hidup, tingkat urbanisasi, struktur ekonomi, dan ketersediaan barang/jasa.
2. **Limitasi:** Data ini simulasi. Data riil dari BPS (Survei Sosial Ekonomi Nasional/Susenas) akan menunjukkan pola yang lebih nuansa.
3. **Implikasi kebijakan:** Jika ada perbedaan signifikan, kebijakan transfer sosial (misalnya BLT, PKH) perlu disesuaikan dengan tingkat pengeluaran lokal.
4. **Pertanyaan lanjutan:** Apakah perbedaan ini tetap signifikan setelah mengontrol variabel seperti pendapatan, pendidikan, dan ukuran keluarga? (Ini memerlukan analisis regresi lebih lanjut.)

---

## AI Corner: AI untuk Memilih Uji Statistik yang Tepat

### Prompt yang Efektif

> "Saya memiliki data pengeluaran rumah tangga dari 4 wilayah di Indonesia. Saya sudah cek asumsi: Shapiro-Wilk test menunjukkan [hasil], Levene's test menunjukkan [hasil]. Uji apa yang paling tepat? Jelaskan reasoning-nya."

### Kapan AI Membantu

- Membantu memilih uji yang tepat berdasarkan karakteristik data
- Menjelaskan cara membaca output Tukey's HSD atau Dunn's test
- Menyusun narasi interpretatif dari hasil uji statistik
- Memeriksa apakah reasoning kita sudah benar dalam memilih uji

### Kapan Harus Kritis terhadap AI

- AI mungkin langsung merekomendasikan ANOVA tanpa mengecek asumsi terlebih dahulu
- AI terkadang tidak menjelaskan bahwa ANOVA hanya mendeteksi "ada perbedaan," bukan "di mana perbedaannya"
- AI mungkin tidak memahami konteks Indonesia (misalnya: perbedaan ekonomi Jawa vs luar Jawa)
- Selalu pastikan AI merekomendasikan post-hoc test ketika ANOVA signifikan

### Contoh Evaluasi Output AI

Jika AI mengatakan: *"Hasil ANOVA signifikan dengan p < 0.05, berarti semua kelompok berbeda satu sama lain"* — ini **salah**. ANOVA signifikan hanya berarti **minimal satu** kelompok berbeda. Untuk tahu **mana** yang berbeda, perlu post-hoc test.

---

## Latihan Mandiri

### Latihan 1: ANOVA Step-by-Step (20 menit)

Simulasikan data nilai ujian mahasiswa dari 3 program studi berbeda (Informatika, Sistem Informasi, Teknik Komputer), masing-masing 30 mahasiswa.

```python
# Template data:
np.random.seed(123)
informatika = np.random.normal(75, 10, 30)
si = np.random.normal(72, 12, 30)
tekkom = np.random.normal(78, 8, 30)
```

a. Buat box plot untuk membandingkan ketiga kelompok secara visual
b. Cek asumsi normalitas (Shapiro-Wilk) dan homogenitas variansi (Levene's)
c. Lakukan One-way ANOVA
d. Jika signifikan, lakukan Tukey's HSD
e. Tulis kesimpulan dalam 2-3 kalimat

### Latihan 2: Non-Parametrik (15 menit)

Gunakan data berikut (skala kepuasan mahasiswa 1-5 di 3 kampus berbeda):

```python
kampus_A = [4, 5, 3, 4, 5, 4, 3, 5, 4, 4]
kampus_B = [3, 2, 3, 4, 2, 3, 2, 3, 3, 2]
kampus_C = [4, 3, 4, 5, 4, 3, 4, 4, 5, 3]
```

a. Mengapa data ini lebih cocok dianalisis dengan uji non-parametrik? (Petunjuk: skala ordinal)
b. Lakukan Kruskal-Wallis test
c. Jika signifikan, lakukan Dunn's test
d. Interpretasikan hasilnya

### Latihan 3: Decision Tree dalam Praktik (15 menit)

Untuk masing-masing skenario berikut, tentukan uji yang paling tepat. Jelaskan alasannya.

a. Membandingkan berat badan antara 2 kelompok diet, data normal, variansi sama
b. Membandingkan skor kepuasan (1-10) di 4 cabang toko, distribusi skewed
c. Membandingkan tekanan darah sebelum dan sesudah minum obat pada 20 pasien yang sama
d. Membandingkan waktu respons website di 3 server berbeda, data tidak normal, ada outlier

### Latihan 4: Analisis Lengkap (20 menit)

Kunjungi [bps.go.id](https://bps.go.id) atau gunakan data simulasi untuk:

a. Ambil atau simulasikan data dengan minimal 3 kelompok
b. Lakukan analisis lengkap:
   - Statistik deskriptif per kelompok
   - Visualisasi (box plot + violin plot)
   - Cek asumsi
   - Pilih dan jalankan uji yang tepat
   - Post-hoc test (jika signifikan)
   - Kesimpulan
c. Dokumentasikan reasoning pemilihan uji

---

## Rangkuman

| Konsep | Poin Kunci |
|--------|-----------|
| ANOVA | Membandingkan rata-rata >2 kelompok sekaligus; menghindari inflasi Type I error |
| F-Statistic | Rasio variasi antar kelompok vs dalam kelompok; F >> 1 → ada perbedaan |
| Asumsi ANOVA | Normalitas, homogeneity of variance, independence |
| Tukey's HSD | Post-hoc test; menunjukkan *kelompok mana* yang berbeda setelah ANOVA signifikan |
| Mann-Whitney U | Non-parametrik untuk 2 kelompok; berbasis rank; alternatif untuk t-test |
| Kruskal-Wallis | Non-parametrik untuk >2 kelompok; berbasis rank; alternatif untuk ANOVA |
| Decision Tree | Pilih uji berdasarkan: jumlah kelompok, normalitas, skala data |

---

## Referensi

1. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics* (4th ed.), Chapter 7: Inference for Numerical Data (ANOVA section).
2. Field, A. (2018). *Discovering Statistics Using IBM SPSS Statistics* (5th ed.), Chapters 12-15.
3. Bruce, P., & Bruce, A. (2020). *Practical Statistics for Data Scientists* (2nd ed.), Chapter 3: Statistical Experiments and Significance Testing.
4. scipy.stats Documentation: [f_oneway](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html), [mannwhitneyu](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html), [kruskal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html)
5. scikit-posthocs Documentation: [scikit-posthocs](https://scikit-posthocs.readthedocs.io/)
6. statsmodels Documentation: [pairwise_tukeyhsd](https://www.statsmodels.org/stable/generated/statsmodels.stats.multicomp.pairwise_tukeyhsd.html)
7. BPS (Badan Pusat Statistik) — Data Susenas: [bps.go.id](https://bps.go.id)

---

*Modul ini adalah bagian dari mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia. Semester Genap 2025/2026.*
