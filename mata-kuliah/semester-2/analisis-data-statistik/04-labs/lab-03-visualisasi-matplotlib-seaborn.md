# Lab 03: Visualisasi Data dengan matplotlib & seaborn

**Mata Kuliah:** Statistika dan Probabilitas
**Program Studi:** Universitas Al Azhar Indonesia
**Minggu:** 3
**Penilaian:** Dinilai (submit notebook dengan narasi)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. Membuat berbagai jenis visualisasi menggunakan matplotlib (histogram, bar chart, scatter plot)
2. Membuat visualisasi lanjutan menggunakan seaborn (boxplot, heatmap, pairplot)
3. Mengkustomisasi tampilan grafik (judul, label, warna, ukuran)
4. Menyusun "data story" -- narasi analisis yang didukung 5+ visualisasi

---

## Persiapan

- Google Colab notebook baru
- Nama file: `Lab03_NamaAnda_NIM.ipynb`
- Library yang digunakan: matplotlib, seaborn, pandas, numpy

---

## Langkah-langkah

### Langkah 1: Setup dan Persiapan Data

```python
# =============================================
# LANGKAH 1: Setup
# =============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi tampilan
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 11
sns.set_style("whitegrid")

np.random.seed(42)

# Generate dataset simulasi: Data Kesehatan Masyarakat
n = 300

data = {
    'usia': np.random.normal(40, 15, n).astype(int).clip(18, 75),
    'berat_badan': np.random.normal(65, 12, n).round(1).clip(40, 120),
    'tinggi_badan': np.random.normal(165, 10, n).round(1).clip(140, 195),
    'tekanan_sistolik': np.random.normal(125, 18, n).astype(int).clip(90, 200),
    'gula_darah': np.random.lognormal(4.7, 0.3, n).round(1).clip(60, 350),
    'kolesterol': np.random.normal(200, 40, n).round(1).clip(100, 380),
    'jam_olahraga_minggu': np.random.exponential(3, n).round(1).clip(0, 20),
    'jenis_kelamin': np.random.choice(['Laki-laki', 'Perempuan'], n),
    'wilayah': np.random.choice(['Kota', 'Pinggiran', 'Pedesaan'], n,
                                 p=[0.40, 0.35, 0.25]),
    'merokok': np.random.choice(['Ya', 'Tidak'], n, p=[0.30, 0.70]),
}

df = pd.DataFrame(data)

# Hitung BMI
df['bmi'] = (df['berat_badan'] / ((df['tinggi_badan']/100) ** 2)).round(1)

# Kategori BMI
def kategori_bmi(bmi):
    if bmi < 18.5: return 'Underweight'
    elif bmi < 25: return 'Normal'
    elif bmi < 30: return 'Overweight'
    else: return 'Obese'

df['kategori_bmi'] = df['bmi'].apply(kategori_bmi)

print(f"Dataset: {df.shape[0]} baris x {df.shape[1]} kolom")
print(f"Kolom: {list(df.columns)}")
df.head()
```

### Langkah 2: Histogram (matplotlib)

```python
# =============================================
# LANGKAH 2: Histogram
# =============================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Histogram 1: Usia
axes[0, 0].hist(df['usia'], bins=20, color='#3498db', edgecolor='white', alpha=0.85)
axes[0, 0].set_title('Distribusi Usia Responden', fontsize=13, fontweight='bold')
axes[0, 0].set_xlabel('Usia (tahun)')
axes[0, 0].set_ylabel('Frekuensi')
axes[0, 0].axvline(df['usia'].mean(), color='red', linestyle='--',
                    label=f"Mean: {df['usia'].mean():.1f}")
axes[0, 0].axvline(df['usia'].median(), color='green', linestyle='--',
                    label=f"Median: {df['usia'].median():.1f}")
axes[0, 0].legend()

# Histogram 2: BMI
axes[0, 1].hist(df['bmi'], bins=25, color='#e74c3c', edgecolor='white', alpha=0.85)
axes[0, 1].set_title('Distribusi BMI', fontsize=13, fontweight='bold')
axes[0, 1].set_xlabel('BMI (kg/m²)')
axes[0, 1].set_ylabel('Frekuensi')

# Histogram 3: Gula darah
axes[1, 0].hist(df['gula_darah'], bins=30, color='#2ecc71', edgecolor='white', alpha=0.85)
axes[1, 0].set_title('Distribusi Gula Darah', fontsize=13, fontweight='bold')
axes[1, 0].set_xlabel('Gula Darah (mg/dL)')
axes[1, 0].set_ylabel('Frekuensi')

# Histogram 4: Jam olahraga (stacked by gender)
for gender, color in [('Laki-laki', '#3498db'), ('Perempuan', '#e74c3c')]:
    subset = df[df['jenis_kelamin'] == gender]['jam_olahraga_minggu']
    axes[1, 1].hist(subset, bins=20, alpha=0.6, color=color, edgecolor='white', label=gender)
axes[1, 1].set_title('Distribusi Jam Olahraga per Minggu', fontsize=13, fontweight='bold')
axes[1, 1].set_xlabel('Jam Olahraga / Minggu')
axes[1, 1].set_ylabel('Frekuensi')
axes[1, 1].legend()

plt.suptitle('HISTOGRAM - Data Kesehatan Masyarakat', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

### Langkah 3: Bar Chart (matplotlib)

```python
# =============================================
# LANGKAH 3: Bar Chart
# =============================================

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Bar chart 1: Jumlah per kategori BMI
bmi_counts = df['kategori_bmi'].value_counts().reindex(['Underweight', 'Normal', 'Overweight', 'Obese'])
colors_bmi = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
axes[0].bar(bmi_counts.index, bmi_counts.values, color=colors_bmi, edgecolor='white')
axes[0].set_title('Jumlah Responden per Kategori BMI', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Jumlah')
for i, v in enumerate(bmi_counts.values):
    axes[0].text(i, v + 2, str(v), ha='center', fontweight='bold')

# Bar chart 2: Rata-rata tekanan darah per wilayah (horizontal)
mean_tekanan = df.groupby('wilayah')['tekanan_sistolik'].mean().sort_values()
axes[1].barh(mean_tekanan.index, mean_tekanan.values, color=['#1abc9c', '#9b59b6', '#e67e22'])
axes[1].set_title('Rata-rata Tekanan Sistolik per Wilayah', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Tekanan Sistolik (mmHg)')
for i, v in enumerate(mean_tekanan.values):
    axes[1].text(v + 0.5, i, f'{v:.1f}', va='center', fontweight='bold')

# Bar chart 3: Grouped bar chart - merokok per wilayah
smoke_region = pd.crosstab(df['wilayah'], df['merokok'])
smoke_region.plot(kind='bar', ax=axes[2], color=['#2ecc71', '#e74c3c'], edgecolor='white')
axes[2].set_title('Status Merokok per Wilayah', fontsize=12, fontweight='bold')
axes[2].set_ylabel('Jumlah')
axes[2].set_xticklabels(axes[2].get_xticklabels(), rotation=0)
axes[2].legend(title='Merokok')

plt.tight_layout()
plt.show()
```

### Langkah 4: Scatter Plot (matplotlib)

```python
# =============================================
# LANGKAH 4: Scatter Plot
# =============================================

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Scatter 1: Berat badan vs Tekanan sistolik
colors_gender = {'Laki-laki': '#3498db', 'Perempuan': '#e74c3c'}
for gender in df['jenis_kelamin'].unique():
    subset = df[df['jenis_kelamin'] == gender]
    axes[0].scatter(subset['berat_badan'], subset['tekanan_sistolik'],
                    c=colors_gender[gender], label=gender, alpha=0.5, s=30)

axes[0].set_title('Berat Badan vs Tekanan Sistolik', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Berat Badan (kg)')
axes[0].set_ylabel('Tekanan Sistolik (mmHg)')
axes[0].legend()

# Tambahkan garis tren
z = np.polyfit(df['berat_badan'], df['tekanan_sistolik'], 1)
p = np.poly1d(z)
x_line = np.linspace(df['berat_badan'].min(), df['berat_badan'].max(), 100)
axes[0].plot(x_line, p(x_line), 'k--', alpha=0.5, label=f'Tren (slope={z[0]:.2f})')
axes[0].legend()

# Scatter 2: BMI vs Kolesterol (warna = usia)
sc = axes[1].scatter(df['bmi'], df['kolesterol'], c=df['usia'],
                     cmap='RdYlGn_r', alpha=0.6, s=30, edgecolors='gray', linewidths=0.3)
axes[1].set_title('BMI vs Kolesterol (warna = Usia)', fontsize=13, fontweight='bold')
axes[1].set_xlabel('BMI (kg/m²)')
axes[1].set_ylabel('Kolesterol (mg/dL)')
plt.colorbar(sc, ax=axes[1], label='Usia (tahun)')

plt.tight_layout()
plt.show()
```

### Langkah 5: Boxplot (seaborn)

```python
# =============================================
# LANGKAH 5: Boxplot dengan seaborn
# =============================================

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Boxplot 1: BMI per kategori
sns.boxplot(data=df, x='kategori_bmi', y='bmi',
            order=['Underweight', 'Normal', 'Overweight', 'Obese'],
            palette='Set2', ax=axes[0])
axes[0].set_title('Distribusi BMI per Kategori', fontsize=12, fontweight='bold')

# Boxplot 2: Tekanan sistolik per wilayah dan jenis kelamin
sns.boxplot(data=df, x='wilayah', y='tekanan_sistolik',
            hue='jenis_kelamin', palette='Set1', ax=axes[1])
axes[1].set_title('Tekanan Sistolik per Wilayah & Gender', fontsize=12, fontweight='bold')
axes[1].legend(title='Gender', fontsize=9)

# Boxplot 3: Gula darah per status merokok
sns.boxplot(data=df, x='merokok', y='gula_darah',
            palette=['#2ecc71', '#e74c3c'], ax=axes[2])
axes[2].set_title('Gula Darah per Status Merokok', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()
```

### Langkah 6: Heatmap Korelasi (seaborn)

```python
# =============================================
# LANGKAH 6: Heatmap Korelasi
# =============================================

# Pilih kolom numerik
numeric_cols = ['usia', 'berat_badan', 'tinggi_badan', 'tekanan_sistolik',
                'gula_darah', 'kolesterol', 'jam_olahraga_minggu', 'bmi']
corr_matrix = df[numeric_cols].corr()

# Heatmap
plt.figure(figsize=(10, 8))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))  # mask segitiga atas
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f',
            cmap='RdBu_r', center=0, vmin=-1, vmax=1,
            square=True, linewidths=1, linecolor='white',
            cbar_kws={'label': 'Koefisien Korelasi'})
plt.title('Heatmap Korelasi Antar Variabel Numerik', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Interpretasi
print("=== INTERPRETASI KORELASI ===")
print(f"Korelasi berat_badan vs bmi: {corr_matrix.loc['berat_badan', 'bmi']:.3f} (sangat kuat)")
print(f"Korelasi usia vs tekanan_sistolik: {corr_matrix.loc['usia', 'tekanan_sistolik']:.3f}")
print(f"Korelasi bmi vs kolesterol: {corr_matrix.loc['bmi', 'kolesterol']:.3f}")
```

### Langkah 7: Pairplot (seaborn)

```python
# =============================================
# LANGKAH 7: Pairplot
# =============================================

# Pilih subset kolom agar tidak terlalu besar
cols_pairplot = ['usia', 'bmi', 'tekanan_sistolik', 'kolesterol', 'jenis_kelamin']

g = sns.pairplot(df[cols_pairplot], hue='jenis_kelamin',
                 palette='Set1', diag_kind='kde',
                 plot_kws={'alpha': 0.4, 's': 20},
                 height=2.5)
g.fig.suptitle('Pairplot: Variabel Kesehatan per Gender', fontsize=14,
               fontweight='bold', y=1.02)
plt.show()
```

### Langkah 8: Kustomisasi Lanjutan

```python
# =============================================
# LANGKAH 8: Kustomisasi Grafik
# =============================================

fig, ax = plt.subplots(figsize=(10, 6))

# Violin plot + strip plot (gabungan)
sns.violinplot(data=df, x='wilayah', y='kolesterol', hue='jenis_kelamin',
               split=True, inner='quart', palette='pastel', ax=ax)

ax.set_title('Distribusi Kolesterol per Wilayah dan Gender\n(Violin Plot)',
             fontsize=14, fontweight='bold')
ax.set_xlabel('Wilayah', fontsize=12)
ax.set_ylabel('Kolesterol (mg/dL)', fontsize=12)
ax.legend(title='Gender', fontsize=10)

# Tambahkan garis referensi
ax.axhline(y=200, color='red', linestyle='--', alpha=0.5, label='Batas Normal (200)')
ax.axhline(y=240, color='darkred', linestyle='--', alpha=0.5, label='Batas Tinggi (240)')

# Anotasi
ax.annotate('Batas Normal (200 mg/dL)', xy=(2.3, 200), fontsize=9,
            color='red', alpha=0.7)
ax.annotate('Batas Tinggi (240 mg/dL)', xy=(2.3, 240), fontsize=9,
            color='darkred', alpha=0.7)

plt.tight_layout()
plt.show()
```

### Langkah 9: Menyusun "Data Story"

Buat minimal 5 visualisasi yang membentuk narasi (cerita data) yang koheren. Berikut adalah contoh kerangkanya:

```python
# =============================================
# LANGKAH 9: DATA STORY - Potret Kesehatan Masyarakat
# =============================================

fig = plt.figure(figsize=(16, 20))

# --- CHART 1: Komposisi Demografi ---
ax1 = fig.add_subplot(3, 2, 1)
demografi = df['wilayah'].value_counts()
ax1.pie(demografi, labels=demografi.index, autopct='%1.1f%%',
        colors=['#3498db', '#2ecc71', '#f39c12'], startangle=90)
ax1.set_title('1. Komposisi Wilayah Responden', fontsize=12, fontweight='bold')

# --- CHART 2: Distribusi Usia ---
ax2 = fig.add_subplot(3, 2, 2)
sns.histplot(data=df, x='usia', hue='jenis_kelamin', kde=True,
             palette='Set1', alpha=0.5, ax=ax2)
ax2.set_title('2. Distribusi Usia per Gender', fontsize=12, fontweight='bold')

# --- CHART 3: BMI per Wilayah ---
ax3 = fig.add_subplot(3, 2, 3)
sns.boxplot(data=df, x='wilayah', y='bmi', palette='Set2', ax=ax3)
ax3.axhline(y=25, color='red', linestyle='--', alpha=0.5)
ax3.set_title('3. BMI per Wilayah (garis merah = batas overweight)',
              fontsize=12, fontweight='bold')

# --- CHART 4: Tekanan Darah vs Usia ---
ax4 = fig.add_subplot(3, 2, 4)
sns.scatterplot(data=df, x='usia', y='tekanan_sistolik', hue='merokok',
                palette={'Ya': 'red', 'Tidak': 'green'}, alpha=0.5, ax=ax4)
ax4.axhline(y=140, color='red', linestyle='--', alpha=0.3)
ax4.set_title('4. Tekanan Darah vs Usia (per Status Merokok)',
              fontsize=12, fontweight='bold')

# --- CHART 5: Rata-rata Indikator per Wilayah ---
ax5 = fig.add_subplot(3, 2, 5)
mean_by_region = df.groupby('wilayah')[['tekanan_sistolik', 'gula_darah', 'kolesterol']].mean()
mean_by_region.plot(kind='bar', ax=ax5, color=['#3498db', '#e74c3c', '#f39c12'])
ax5.set_title('5. Rata-rata Indikator Kesehatan per Wilayah',
              fontsize=12, fontweight='bold')
ax5.set_xticklabels(ax5.get_xticklabels(), rotation=0)
ax5.legend(fontsize=9)

# --- CHART 6: Korelasi Olahraga vs BMI ---
ax6 = fig.add_subplot(3, 2, 6)
sns.regplot(data=df, x='jam_olahraga_minggu', y='bmi',
            scatter_kws={'alpha': 0.3, 's': 20}, line_kws={'color': 'red'},
            ax=ax6)
ax6.set_title('6. Hubungan Jam Olahraga dengan BMI',
              fontsize=12, fontweight='bold')
ax6.set_xlabel('Jam Olahraga per Minggu')
ax6.set_ylabel('BMI')

plt.suptitle('DATA STORY: Potret Kesehatan Masyarakat\n(n=300 responden)',
             fontsize=16, fontweight='bold', y=1.01)
plt.tight_layout()
plt.show()
```

```markdown
### Narasi Data Story (Contoh)

**Pendahuluan:** Dataset ini berisi data kesehatan 300 responden dari tiga wilayah
(kota, pinggiran, pedesaan). Kita akan mengeksplorasi pola kesehatan masyarakat.

**Temuan 1:** Distribusi usia relatif merata antara laki-laki dan perempuan di
semua wilayah (Chart 1 & 2).

**Temuan 2:** BMI di wilayah kota cenderung lebih tinggi dibandingkan pedesaan,
kemungkinan terkait pola makan dan aktivitas fisik (Chart 3).

**Temuan 3:** Tekanan darah meningkat seiring usia, dan perokok menunjukkan
kecenderungan tekanan darah lebih tinggi (Chart 4).

**Temuan 4:** Terdapat variasi indikator kesehatan antar wilayah yang perlu
perhatian khusus (Chart 5).

**Kesimpulan:** Perlu program kesehatan yang disesuaikan per wilayah dengan fokus
pada pencegahan penyakit tidak menular.
```

---

## Tugas yang Harus Dikumpulkan

Kumpulkan notebook (.ipynb) yang berisi:

1. **Semua kode** dari Langkah 1-8 yang sudah dijalankan (tanpa error)
2. **Data Story Anda sendiri** (Langkah 9) yang mencakup:
   - Minimal **5 visualisasi** berbeda
   - **Narasi tertulis** dalam text cell (minimal 3 paragraf) yang menghubungkan temuan dari setiap chart
   - Setiap chart harus memiliki judul, label sumbu, dan legenda yang sesuai
3. **Satu visualisasi kreatif** tambahan yang belum diajarkan (cari referensi sendiri di dokumentasi matplotlib/seaborn)

---

## Rubrik Singkat

| Kriteria | Bobot | Keterangan |
|----------|-------|------------|
| Kelengkapan kode (Langkah 1-8) | 25% | Semua chart berjalan tanpa error |
| Data Story (5+ chart + narasi) | 35% | Visualisasi beragam, narasi koheren dan insightful |
| Kustomisasi grafik | 20% | Judul, label, warna, ukuran sesuai; chart mudah dibaca |
| Visualisasi kreatif tambahan | 10% | Mencoba chart type baru dengan referensi |
| Kerapian notebook | 10% | Terstruktur rapi dengan text cell penjelasan |

---

## Challenge / Bonus

```python
# =============================================
# CHALLENGE: Subplot Mosaic dan Annotasi Lanjutan
# =============================================

# Gunakan subplot_mosaic untuk layout fleksibel
fig, axes = plt.subplot_mosaic(
    [['hist', 'hist', 'box'],
     ['scatter', 'scatter', 'box']],
    figsize=(14, 8)
)

# Panel kiri atas: Histogram
sns.histplot(data=df, x='bmi', hue='kategori_bmi', multiple='stack',
             palette='RdYlGn_r', ax=axes['hist'])
axes['hist'].set_title('Distribusi BMI per Kategori', fontweight='bold')

# Panel kanan: Boxplot (vertikal panjang)
sns.boxplot(data=df, y='bmi', x='wilayah', palette='Set2', ax=axes['box'])
axes['box'].set_title('BMI per Wilayah', fontweight='bold')

# Panel kiri bawah: Scatter dengan anotasi
sns.scatterplot(data=df, x='usia', y='bmi', hue='kategori_bmi',
                palette='RdYlGn_r', alpha=0.5, ax=axes['scatter'])
axes['scatter'].set_title('Usia vs BMI', fontweight='bold')

# Anotasi titik ekstrem
idx_max_bmi = df['bmi'].idxmax()
axes['scatter'].annotate(
    f"BMI tertinggi: {df.loc[idx_max_bmi, 'bmi']:.1f}",
    xy=(df.loc[idx_max_bmi, 'usia'], df.loc[idx_max_bmi, 'bmi']),
    xytext=(10, 10), textcoords='offset points',
    arrowprops=dict(arrowstyle='->', color='red'),
    fontsize=10, color='red', fontweight='bold'
)

plt.suptitle('Dashboard BMI Masyarakat', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

> **Referensi:**
> - [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
> - [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
> - [Python Graph Gallery](https://python-graph-gallery.com/)
