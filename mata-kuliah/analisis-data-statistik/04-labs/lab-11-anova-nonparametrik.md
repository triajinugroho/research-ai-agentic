# Lab 11: ANOVA dan Uji Non-Parametrik

**Mata Kuliah:** Statistika — Universitas Al Azhar Indonesia
**Minggu:** 11
**Platform:** Google Colab (Python)

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. Melaksanakan One-Way ANOVA menggunakan `scipy.stats`
2. Memeriksa asumsi ANOVA: normalitas (Shapiro-Wilk) dan homogenitas varians (Levene's test)
3. Melakukan uji post-hoc Tukey's HSD dengan `statsmodels`
4. Menggunakan alternatif non-parametrik (Kruskal-Wallis) jika asumsi dilanggar
5. Memilih uji statistik yang tepat berdasarkan decision flowchart

---

## Persiapan

### Library yang Dibutuhkan

```python
# Jalankan cell ini terlebih dahulu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Pengaturan
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("Semua library berhasil dimuat!")
```

### Konsep Singkat

**ANOVA (Analysis of Variance)** menguji apakah terdapat perbedaan rata-rata yang signifikan antara 3 atau lebih kelompok.

- **H₀**: μ₁ = μ₂ = μ₃ = ... = μₖ (semua rata-rata sama)
- **H₁**: minimal satu rata-rata berbeda

**Asumsi ANOVA:**
1. Data berdistribusi normal di setiap kelompok
2. Homogenitas varians (varians antar kelompok sama)
3. Observasi independen

Jika asumsi dilanggar, gunakan **Kruskal-Wallis** (alternatif non-parametrik).

---

## Langkah-langkah Praktikum

### Langkah 1: Membuat Dataset

```python
# Studi kasus: Pengaruh metode belajar terhadap nilai ujian
np.random.seed(42)

# Tiga metode belajar
metode_a = np.random.normal(75, 8, 30)    # Metode Ceramah
metode_b = np.random.normal(80, 7, 30)    # Metode Diskusi
metode_c = np.random.normal(82, 9, 30)    # Metode Praktikum
metode_d = np.random.normal(78, 10, 30)   # Metode Daring

# Gabungkan ke DataFrame
data = pd.DataFrame({
    'nilai': np.concatenate([metode_a, metode_b, metode_c, metode_d]),
    'metode': (['Ceramah'] * 30 + ['Diskusi'] * 30 +
               ['Praktikum'] * 30 + ['Daring'] * 30)
})

data['nilai'] = np.round(data['nilai'], 1)

print("=== Dataset: Pengaruh Metode Belajar terhadap Nilai Ujian ===")
print(f"Jumlah total data: {len(data)}")
print(f"Kelompok: {data['metode'].unique().tolist()}")
print(f"Jumlah per kelompok: {data['metode'].value_counts().to_dict()}")
print()
data.head()
```

### Langkah 2: Eksplorasi Data per Kelompok

```python
# Statistik deskriptif per kelompok
print("=== Statistik Deskriptif per Metode Belajar ===")
ringkasan = data.groupby('metode')['nilai'].agg(
    ['count', 'mean', 'std', 'min', 'max']
).round(2)
ringkasan.columns = ['N', 'Rata-rata', 'Std Dev', 'Min', 'Max']
print(ringkasan)
```

```python
# Visualisasi: Box plot dan violin plot
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Box plot
data.boxplot(column='nilai', by='metode', ax=axes[0])
axes[0].set_title('Box Plot Nilai per Metode Belajar')
axes[0].set_xlabel('Metode Belajar')
axes[0].set_ylabel('Nilai Ujian')
plt.sca(axes[0])
plt.xticks(rotation=0)

# Violin plot
sns.violinplot(data=data, x='metode', y='nilai', ax=axes[1],
               palette='Set2', inner='box')
axes[1].set_title('Violin Plot Nilai per Metode Belajar')
axes[1].set_xlabel('Metode Belajar')
axes[1].set_ylabel('Nilai Ujian')

plt.suptitle('')  # Hapus judul otomatis dari boxplot
plt.tight_layout()
plt.show()
```

### Langkah 3: Cek Asumsi — Normalitas (Shapiro-Wilk)

```python
# Uji normalitas Shapiro-Wilk untuk setiap kelompok
print("=== Uji Normalitas: Shapiro-Wilk ===")
print("H₀: Data berdistribusi normal")
print("H₁: Data TIDAK berdistribusi normal")
print("Tolak H₀ jika p-value < 0.05")
print()

alpha = 0.05
semua_normal = True

for metode in data['metode'].unique():
    subset = data[data['metode'] == metode]['nilai']
    stat, p_val = stats.shapiro(subset)
    hasil = "Normal" if p_val > alpha else "TIDAK Normal"
    if p_val <= alpha:
        semua_normal = False
    print(f"  {metode:12s}: W = {stat:.4f}, p = {p_val:.4f} → {hasil}")

print()
if semua_normal:
    print("Kesimpulan: Semua kelompok berdistribusi normal. Asumsi terpenuhi.")
else:
    print("Kesimpulan: Ada kelompok yang tidak normal. Pertimbangkan uji non-parametrik.")
```

### Langkah 4: Cek Asumsi — Homogenitas Varians (Levene's Test)

```python
# Uji Levene untuk homogenitas varians
print("=== Uji Homogenitas Varians: Levene's Test ===")
print("H₀: Varians semua kelompok sama (homogen)")
print("H₁: Varians kelompok TIDAK sama (heterogen)")
print()

grup = [data[data['metode'] == m]['nilai'] for m in data['metode'].unique()]
levene_stat, levene_p = stats.levene(*grup)

print(f"Statistik Levene = {levene_stat:.4f}")
print(f"p-value           = {levene_p:.4f}")
print()

if levene_p > 0.05:
    print("Kesimpulan: Varians homogen (p > 0.05). Asumsi terpenuhi.")
    homogen = True
else:
    print("Kesimpulan: Varians TIDAK homogen (p ≤ 0.05). Asumsi dilanggar.")
    homogen = False
```

### Langkah 5: One-Way ANOVA

```python
# One-Way ANOVA
print("=== One-Way ANOVA ===")
print("H₀: μ_ceramah = μ_diskusi = μ_praktikum = μ_daring")
print("H₁: Minimal satu rata-rata berbeda")
print()

f_stat, anova_p = stats.f_oneway(*grup)

print(f"F-statistic = {f_stat:.4f}")
print(f"p-value     = {anova_p:.4f}")
print()

if anova_p < 0.05:
    print("Kesimpulan: Tolak H₀ (p < 0.05)")
    print("Terdapat perbedaan rata-rata yang signifikan antar metode belajar.")
    print("→ Lanjutkan dengan uji post-hoc untuk mengetahui kelompok mana yang berbeda.")
else:
    print("Kesimpulan: Gagal tolak H₀ (p ≥ 0.05)")
    print("Tidak ada perbedaan rata-rata yang signifikan antar metode belajar.")
```

```python
# Hitung effect size (Eta-squared)
# η² = SS_between / SS_total
grand_mean = data['nilai'].mean()
ss_between = sum(len(g) * (g.mean() - grand_mean)**2 for g in grup)
ss_total = sum((data['nilai'] - grand_mean)**2)
eta_squared = ss_between / ss_total

print(f"\nEffect Size (η²) = {eta_squared:.4f}")
if eta_squared < 0.01:
    print("Interpretasi: Effect size kecil (negligible)")
elif eta_squared < 0.06:
    print("Interpretasi: Effect size kecil")
elif eta_squared < 0.14:
    print("Interpretasi: Effect size sedang")
else:
    print("Interpretasi: Effect size besar")
```

### Langkah 6: Uji Post-Hoc — Tukey's HSD

```python
# Tukey's HSD: menguji perbedaan antar setiap pasangan kelompok
print("=== Uji Post-Hoc: Tukey's HSD ===")
print("Menguji perbedaan rata-rata antar setiap pasangan kelompok")
print()

tukey_result = pairwise_tukeyhsd(data['nilai'], data['metode'], alpha=0.05)
print(tukey_result)
```

```python
# Visualisasi hasil Tukey
fig, ax = plt.subplots(figsize=(10, 6))
tukey_result.plot_simultaneous(ax=ax)
ax.set_xlabel('Rata-rata Nilai Ujian')
ax.set_title('Tukey HSD: Confidence Interval per Metode\n(Overlap = tidak berbeda signifikan)')
plt.tight_layout()
plt.show()
```

```python
# Interpretasi otomatis
print("=== Interpretasi Hasil Post-Hoc ===")
tukey_df = pd.DataFrame(data=tukey_result._results_table.data[1:],
                         columns=tukey_result._results_table.data[0])
for _, row in tukey_df.iterrows():
    g1, g2 = row['group1'], row['group2']
    reject = row['reject']
    meandiff = float(row['meandiff'])
    if reject:
        arah = "lebih tinggi" if meandiff > 0 else "lebih rendah"
        print(f"  {g1} vs {g2}: Berbeda signifikan ({g2} {arah} sebesar {abs(meandiff):.2f})")
    else:
        print(f"  {g1} vs {g2}: Tidak berbeda signifikan")
```

### Langkah 7: Alternatif Non-Parametrik — Kruskal-Wallis

```python
# Kruskal-Wallis: digunakan ketika asumsi ANOVA dilanggar
# (non-normal atau varians tidak homogen)
print("=== Uji Kruskal-Wallis (Non-Parametrik) ===")
print("Alternatif ANOVA ketika asumsi tidak terpenuhi")
print("H₀: Distribusi semua kelompok sama")
print("H₁: Minimal satu distribusi berbeda")
print()

kw_stat, kw_p = stats.kruskal(*grup)

print(f"H-statistic = {kw_stat:.4f}")
print(f"p-value     = {kw_p:.4f}")
print()

if kw_p < 0.05:
    print("Kesimpulan: Tolak H₀ — Terdapat perbedaan signifikan antar kelompok.")
else:
    print("Kesimpulan: Gagal tolak H₀ — Tidak ada perbedaan signifikan.")
```

```python
# Post-hoc non-parametrik: Mann-Whitney U berpasangan dengan koreksi Bonferroni
from itertools import combinations

print("=== Post-Hoc: Mann-Whitney U dengan Koreksi Bonferroni ===")
metode_list = data['metode'].unique()
n_comparisons = len(list(combinations(metode_list, 2)))
bonferroni_alpha = 0.05 / n_comparisons

print(f"Jumlah perbandingan: {n_comparisons}")
print(f"Alpha terkoreksi (Bonferroni): {bonferroni_alpha:.4f}")
print()

for m1, m2 in combinations(metode_list, 2):
    g1 = data[data['metode'] == m1]['nilai']
    g2 = data[data['metode'] == m2]['nilai']
    u_stat, u_p = stats.mannwhitneyu(g1, g2, alternative='two-sided')
    sig = "Signifikan" if u_p < bonferroni_alpha else "Tidak Signifikan"
    print(f"  {m1:12s} vs {m2:12s}: U = {u_stat:.1f}, p = {u_p:.4f} → {sig}")
```

### Langkah 8: Decision Flowchart — Memilih Uji yang Tepat

```python
# Fungsi decision flowchart
def pilih_uji_statistik(data, kolom_nilai, kolom_grup, alpha=0.05):
    """
    Decision flowchart untuk memilih uji statistik yang tepat.

    Parameters:
    -----------
    data : pd.DataFrame
    kolom_nilai : str — nama kolom variabel dependen
    kolom_grup : str — nama kolom variabel grup
    alpha : float — level signifikansi (default 0.05)
    """
    print("=" * 60)
    print("DECISION FLOWCHART: Memilih Uji Statistik")
    print("=" * 60)

    grup_unik = data[kolom_grup].unique()
    n_grup = len(grup_unik)
    print(f"\nJumlah kelompok: {n_grup}")

    if n_grup < 2:
        print("Error: Minimal 2 kelompok diperlukan.")
        return

    if n_grup == 2:
        print("→ Dua kelompok terdeteksi")
        # Cek normalitas
        normal = True
        for g in grup_unik:
            subset = data[data[kolom_grup] == g][kolom_nilai]
            _, p = stats.shapiro(subset)
            if p < alpha:
                normal = False
                break

        if normal:
            # Cek homogenitas
            g1 = data[data[kolom_grup] == grup_unik[0]][kolom_nilai]
            g2 = data[data[kolom_grup] == grup_unik[1]][kolom_nilai]
            _, lev_p = stats.levene(g1, g2)
            if lev_p > alpha:
                print("→ Normal + Homogen → Independent t-test")
                stat, p = stats.ttest_ind(g1, g2)
                print(f"  t = {stat:.4f}, p = {p:.4f}")
            else:
                print("→ Normal + Tidak Homogen → Welch's t-test")
                stat, p = stats.ttest_ind(g1, g2, equal_var=False)
                print(f"  t = {stat:.4f}, p = {p:.4f}")
        else:
            print("→ Tidak Normal → Mann-Whitney U")
            g1 = data[data[kolom_grup] == grup_unik[0]][kolom_nilai]
            g2 = data[data[kolom_grup] == grup_unik[1]][kolom_nilai]
            stat, p = stats.mannwhitneyu(g1, g2, alternative='two-sided')
            print(f"  U = {stat:.4f}, p = {p:.4f}")

    else:
        print(f"→ {n_grup} kelompok terdeteksi (≥3)")
        # Cek normalitas semua grup
        normal = True
        for g in grup_unik:
            subset = data[data[kolom_grup] == g][kolom_nilai]
            _, p = stats.shapiro(subset)
            if p < alpha:
                normal = False
                break

        groups = [data[data[kolom_grup] == g][kolom_nilai] for g in grup_unik]

        if normal:
            _, lev_p = stats.levene(*groups)
            if lev_p > alpha:
                print("→ Normal + Homogen → One-Way ANOVA")
                stat, p = stats.f_oneway(*groups)
                print(f"  F = {stat:.4f}, p = {p:.4f}")
                if p < alpha:
                    print("  → Signifikan! Lanjut Post-Hoc: Tukey HSD")
            else:
                print("→ Normal + Tidak Homogen → Welch's ANOVA")
                # scipy tidak punya Welch ANOVA langsung, gunakan Kruskal sebagai alternatif
                stat, p = stats.kruskal(*groups)
                print(f"  H = {stat:.4f}, p = {p:.4f}")
        else:
            print("→ Tidak Normal → Kruskal-Wallis")
            stat, p = stats.kruskal(*groups)
            print(f"  H = {stat:.4f}, p = {p:.4f}")
            if p < alpha:
                print("  → Signifikan! Lanjut Post-Hoc: Mann-Whitney berpasangan")

    print()
    if p < alpha:
        print(f"Hasil: SIGNIFIKAN (p = {p:.4f} < {alpha})")
    else:
        print(f"Hasil: TIDAK SIGNIFIKAN (p = {p:.4f} ≥ {alpha})")
    print("=" * 60)

# Jalankan flowchart
pilih_uji_statistik(data, 'nilai', 'metode')
```

### Langkah 9: Latihan Tambahan — Data Non-Normal

```python
# Buat data yang sengaja tidak normal (skewed)
np.random.seed(99)

grup_x = np.random.exponential(scale=10, size=25)   # Positively skewed
grup_y = np.random.exponential(scale=12, size=25)
grup_z = np.random.exponential(scale=15, size=25)

data_skew = pd.DataFrame({
    'nilai': np.concatenate([grup_x, grup_y, grup_z]),
    'kelompok': ['X'] * 25 + ['Y'] * 25 + ['Z'] * 25
})

print("=== Data Non-Normal (Skewed) ===")
# Cek normalitas
for kel in ['X', 'Y', 'Z']:
    subset = data_skew[data_skew['kelompok'] == kel]['nilai']
    _, p = stats.shapiro(subset)
    print(f"  Kelompok {kel}: Shapiro p = {p:.4f} → {'Normal' if p > 0.05 else 'Tidak Normal'}")

print()
print("Karena data tidak normal, gunakan Kruskal-Wallis:")
pilih_uji_statistik(data_skew, 'nilai', 'kelompok')
```

---

## Tugas yang Harus Dikumpulkan

Buat notebook Google Colab yang berisi:

1. **Buat Dataset Sendiri** (15 poin)
   - Buat dataset dengan minimal 3 kelompok yang relevan dengan bidang studi Anda
   - Contoh: perbandingan nilai antar kelas, waktu tempuh antar rute, dll.
   - Tampilkan statistik deskriptif per kelompok

2. **Cek Asumsi** (20 poin)
   - Lakukan uji Shapiro-Wilk per kelompok
   - Lakukan Levene's test
   - Tuliskan kesimpulan: apakah asumsi terpenuhi?

3. **Uji Statistik** (25 poin)
   - Jika asumsi terpenuhi: lakukan ANOVA dan interpretasikan
   - Jika asumsi dilanggar: lakukan Kruskal-Wallis dan jelaskan alasannya

4. **Post-Hoc** (20 poin)
   - Jika hasil signifikan, lakukan uji post-hoc (Tukey atau Mann-Whitney)
   - Kelompok mana saja yang berbeda signifikan?

5. **Visualisasi dan Kesimpulan** (20 poin)
   - Buat box plot atau violin plot yang informatif
   - Tulis kesimpulan dalam bahasa yang mudah dipahami

**Format:** File `.ipynb` diunggah ke Google Classroom
**Deadline:** Satu minggu setelah pertemuan praktikum

---

## Challenge / Bonus

1. **Two-Way ANOVA**: Tambahkan faktor kedua (misalnya gender) dan lakukan Two-Way ANOVA menggunakan `statsmodels`:
   ```python
   import statsmodels.api as sm
   from statsmodels.formula.api import ols
   model = ols('nilai ~ C(metode) * C(gender)', data=data).fit()
   sm.stats.anova_lm(model, typ=2)
   ```

2. **Buat fungsi Python lengkap** yang menerima DataFrame dan secara otomatis: (a) mengecek asumsi, (b) memilih uji yang tepat, (c) melakukan post-hoc jika diperlukan, (d) membuat visualisasi.

3. **Repeated Measures**: Cari tahu bagaimana melakukan Friedman test (non-parametrik untuk repeated measures) dengan `scipy.stats.friedmanchisquare`.
