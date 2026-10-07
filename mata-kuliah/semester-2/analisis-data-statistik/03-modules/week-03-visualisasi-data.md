# MODUL MINGGU 3: VISUALISASI DATA DAN STORYTELLING

## UNIVERSITAS AL AZHAR INDONESIA
### Fakultas Sains dan Teknologi — Program Studi Informatika
### Mata Kuliah: Analisis Data Statistik (IF2XXX)

---

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Minggu** | 3 |
| **Topik** | Visualisasi Data dan Storytelling |
| **CPMK** | CPMK-2: Menerapkan teknik statistika deskriptif dan visualisasi data untuk eksplorasi dan komunikasi temuan menggunakan Python |
| **Sub-CPMK** | 3.1: Membuat visualisasi data yang efektif menggunakan matplotlib dan seaborn |
| | 3.2: Menerapkan prinsip storytelling with data untuk komunikasi temuan |
| **Bloom's Taxonomy** | C3 (Apply) |
| **Durasi** | 100 menit (50 menit teori + 50 menit praktikum) |
| **Tools** | Google Colab, Python 3.x, matplotlib, seaborn, pandas |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Menjelaskan** prinsip-prinsip visualisasi data yang efektif berdasarkan framework Edward Tufte
2. **Membuat** berbagai jenis grafik (line plot, bar chart, scatter plot, histogram, boxplot, heatmap) menggunakan matplotlib dan seaborn
3. **Memilih** jenis visualisasi yang tepat berdasarkan tipe data dan tujuan komunikasi
4. **Menerapkan** prinsip storytelling with data (framework Knaflic) untuk mengubah grafik menjadi narasi yang bermakna
5. **Mengidentifikasi** dan menghindari common pitfalls dalam visualisasi data

---

## Materi Pembelajaran

### 1. Prinsip Visualisasi Data yang Efektif

Visualisasi data bukan sekadar "membuat grafik yang cantik" — melainkan **mengomunikasikan informasi secara jelas dan jujur**. Edward Tufte, salah satu pakar terkemuka di bidang ini, merumuskan beberapa prinsip fundamental.

#### 1.1 Prinsip-prinsip Tufte

**a) Data-Ink Ratio**

> "Above all else, show the data." — Edward Tufte

Data-ink ratio adalah proporsi tinta (atau piksel) pada grafik yang digunakan untuk menampilkan **data aktual** dibandingkan dengan total tinta pada grafik.

```
Data-Ink Ratio = (Tinta yang menampilkan data) / (Total tinta pada grafik)
```

Prinsipnya: **maksimalkan data-ink ratio**. Hapus elemen yang tidak menyampaikan informasi (grid berlebihan, border yang tidak perlu, dekorasi yang mengganggu).

**b) Chartjunk**

Chartjunk adalah elemen visual yang **tidak menambah informasi** tetapi justru mengalihkan perhatian dari data. Contoh chartjunk:
- Efek 3D yang tidak perlu pada bar chart
- Background gambar yang mengganggu
- Garis grid yang terlalu banyak dan tebal
- Dekorasi berlebihan (clip art, icon dekoratif)

**c) Lie Factor**

Lie factor mengukur seberapa jujur sebuah grafik merepresentasikan data.

```
Lie Factor = (Ukuran efek yang ditampilkan di grafik) / (Ukuran efek di data)
```

Lie factor = 1 berarti grafik merepresentasikan data secara akurat. Lie factor > 1.05 atau < 0.95 menandakan distorsi yang perlu dihindari.

#### 1.2 Memilih Jenis Chart yang Tepat

Pemilihan jenis chart bergantung pada **tipe data** dan **tujuan komunikasi**:

| Tujuan | Tipe Data | Chart yang Tepat |
|--------|-----------|-----------------|
| Perbandingan antar kategori | Kategorikal | Bar chart, grouped bar chart |
| Distribusi satu variabel | Numerik kontinu | Histogram, boxplot, violin plot |
| Hubungan dua variabel | Numerik vs numerik | Scatter plot |
| Tren waktu | Time series | Line plot |
| Komposisi/proporsi | Kategorikal (sedikit) | Stacked bar chart, (pie chart — hati-hati!) |
| Korelasi banyak variabel | Numerik multivariat | Heatmap, pairplot |
| Distribusi per kategori | Numerik + kategorikal | Boxplot, violin plot, countplot |

---

### 2. matplotlib Basics

`matplotlib` adalah library visualisasi paling fundamental di Python. Hampir semua library visualisasi Python lainnya (termasuk seaborn) dibangun di atas matplotlib.

#### 2.1 Setup Awal

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Agar grafik tampil di notebook
%matplotlib inline

# Membuat data contoh
np.random.seed(42)
```

#### 2.2 Line Plot — Tren Waktu

Line plot ideal untuk menampilkan **perubahan data sepanjang waktu**.

```python
# Data: Pertumbuhan pengguna internet di Indonesia (juta orang)
tahun = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
pengguna_internet = [171.2, 196.7, 175.4, 202.6, 210.0, 215.6, 221.5]

# Membuat line plot
plt.figure(figsize=(10, 6))
plt.plot(tahun, pengguna_internet, marker='o', color='#2196F3',
         linewidth=2, markersize=8, label='Pengguna Internet')

# Menambahkan label dan judul
plt.title('Pertumbuhan Pengguna Internet di Indonesia', fontsize=14, fontweight='bold')
plt.xlabel('Tahun', fontsize=12)
plt.ylabel('Jumlah Pengguna (Juta)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)

# Anotasi titik tertinggi
plt.annotate(f'{max(pengguna_internet)} juta',
             xy=(tahun[pengguna_internet.index(max(pengguna_internet))],
                 max(pengguna_internet)),
             xytext=(10, 10), textcoords='offset points',
             fontsize=10, color='red',
             arrowprops=dict(arrowstyle='->', color='red'))

plt.tight_layout()
plt.show()
```

#### 2.3 Bar Chart — Perbandingan Kategori

Bar chart efektif untuk **membandingkan nilai antar kategori**.

```python
# Data: Jumlah startup per sektor di Indonesia
sektor = ['E-commerce', 'Fintech', 'Edtech', 'Healthtech', 'Logistics']
jumlah = [2500, 1800, 950, 620, 780]

# Membuat bar chart horizontal (lebih mudah dibaca untuk label panjang)
plt.figure(figsize=(10, 6))
bars = plt.barh(sektor, jumlah, color=['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'])

# Menambahkan nilai di ujung bar
for bar, val in zip(bars, jumlah):
    plt.text(val + 30, bar.get_y() + bar.get_height()/2,
             f'{val:,}', va='center', fontsize=11)

plt.title('Jumlah Startup per Sektor di Indonesia (2024)', fontsize=14, fontweight='bold')
plt.xlabel('Jumlah Startup', fontsize=12)
plt.xlim(0, max(jumlah) * 1.15)  # Ruang untuk label
plt.tight_layout()
plt.show()
```

#### 2.4 Scatter Plot — Hubungan Dua Variabel

Scatter plot menunjukkan **hubungan (korelasi) antara dua variabel numerik**.

```python
# Data simulasi: IPK vs Jam Belajar per Minggu
np.random.seed(42)
jam_belajar = np.random.uniform(5, 30, 50)
ipk = 2.0 + 0.06 * jam_belajar + np.random.normal(0, 0.3, 50)
ipk = np.clip(ipk, 2.0, 4.0)  # IPK antara 2.0 - 4.0

plt.figure(figsize=(10, 6))
plt.scatter(jam_belajar, ipk, alpha=0.7, c='#2196F3', edgecolors='white',
            s=80, linewidth=0.5)

# Menambahkan garis tren (regresi linear sederhana)
z = np.polyfit(jam_belajar, ipk, 1)
p = np.poly1d(z)
x_line = np.linspace(5, 30, 100)
plt.plot(x_line, p(x_line), '--', color='red', alpha=0.8,
         label=f'Tren: y = {z[0]:.3f}x + {z[1]:.3f}')

plt.title('Hubungan Jam Belajar dan IPK Mahasiswa', fontsize=14, fontweight='bold')
plt.xlabel('Jam Belajar per Minggu', fontsize=12)
plt.ylabel('IPK', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

#### 2.5 Histogram — Distribusi Data

Histogram menampilkan **distribusi frekuensi** dari data numerik kontinu.

```python
# Data simulasi: Nilai UTS Statistika (100 mahasiswa)
np.random.seed(42)
nilai_uts = np.random.normal(loc=72, scale=12, size=100)
nilai_uts = np.clip(nilai_uts, 30, 100)

plt.figure(figsize=(10, 6))

# Histogram dengan KDE (Kernel Density Estimation) overlay
counts, bins, patches = plt.hist(nilai_uts, bins=15, color='#36A2EB',
                                  edgecolor='white', alpha=0.7, density=True,
                                  label='Histogram')

# Overlay KDE
from scipy import stats
x_kde = np.linspace(30, 100, 200)
kde = stats.gaussian_kde(nilai_uts)
plt.plot(x_kde, kde(x_kde), color='red', linewidth=2, label='KDE')

# Garis mean dan median
plt.axvline(np.mean(nilai_uts), color='green', linestyle='--',
            linewidth=2, label=f'Mean = {np.mean(nilai_uts):.1f}')
plt.axvline(np.median(nilai_uts), color='orange', linestyle='-.',
            linewidth=2, label=f'Median = {np.median(nilai_uts):.1f}')

plt.title('Distribusi Nilai UTS Statistika', fontsize=14, fontweight='bold')
plt.xlabel('Nilai', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()
```

---

### 3. seaborn: Statistical Visualization

`seaborn` dibangun di atas matplotlib dan menyediakan **antarmuka tingkat tinggi** untuk membuat visualisasi statistik yang informatif dan estetis.

#### 3.1 Setup seaborn

```python
import seaborn as sns

# Mengatur tema default seaborn
sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)

# Memuat dataset contoh (tips dataset bawaan seaborn)
tips = sns.load_dataset('tips')
print(tips.head())
print(f"\nShape: {tips.shape}")
print(f"Columns: {list(tips.columns)}")
```

#### 3.2 Boxplot — Distribusi dan Outlier

Boxplot menampilkan ringkasan lima angka (minimum, Q1, median, Q3, maximum) dan **mendeteksi outlier**.

```python
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='total_bill', hue='sex',
            palette='Set2')

plt.title('Distribusi Total Bill per Hari dan Gender', fontsize=14, fontweight='bold')
plt.xlabel('Hari', fontsize=12)
plt.ylabel('Total Bill ($)', fontsize=12)
plt.legend(title='Gender')
plt.tight_layout()
plt.show()
```

#### 3.3 Violin Plot — Distribusi Detail

Violin plot menggabungkan boxplot dengan KDE, memberikan gambaran **distribusi data yang lebih lengkap**.

```python
plt.figure(figsize=(10, 6))
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex',
               split=True, inner='quart', palette='pastel')

plt.title('Distribusi Total Bill: Violin Plot', fontsize=14, fontweight='bold')
plt.xlabel('Hari', fontsize=12)
plt.ylabel('Total Bill ($)', fontsize=12)
plt.tight_layout()
plt.show()
```

#### 3.4 Heatmap — Korelasi Antar Variabel

Heatmap sangat berguna untuk memvisualisasikan **matriks korelasi** antar variabel numerik.

```python
# Menghitung korelasi
tips_numeric = tips.select_dtypes(include=[np.number])
korelasi = tips_numeric.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(korelasi, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, square=True, linewidths=1,
            cbar_kws={'label': 'Koefisien Korelasi'})

plt.title('Heatmap Korelasi — Dataset Tips', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

#### 3.5 Pairplot — Eksplorasi Multivariat

Pairplot membuat **matriks scatter plot** untuk semua pasangan variabel numerik sekaligus.

```python
# Memuat dataset iris untuk pairplot
iris = sns.load_dataset('iris')

sns.pairplot(iris, hue='species', palette='Dark2',
             diag_kind='kde', height=2.5,
             plot_kws={'alpha': 0.6, 's': 50, 'edgecolor': 'white'})

plt.suptitle('Pairplot — Dataset Iris', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

#### 3.6 Countplot — Frekuensi Kategori

Countplot menampilkan **jumlah observasi per kategori** (seperti bar chart untuk frekuensi).

```python
plt.figure(figsize=(10, 6))
sns.countplot(data=tips, x='day', hue='time',
              palette='viridis', order=['Thur', 'Fri', 'Sat', 'Sun'])

plt.title('Jumlah Transaksi per Hari dan Waktu', fontsize=14, fontweight='bold')
plt.xlabel('Hari', fontsize=12)
plt.ylabel('Jumlah Transaksi', fontsize=12)
plt.legend(title='Waktu Makan')
plt.tight_layout()
plt.show()
```

---

### 4. Storytelling with Data: Dari Chart ke Insight ke Narasi

Membuat grafik yang bagus saja tidak cukup. Kita perlu **bercerita dengan data** agar audiens memahami pesan yang ingin disampaikan. Cole Nussbaumer Knaflic, dalam bukunya *Storytelling with Data*, merumuskan framework yang terdiri dari tiga elemen utama.

#### 4.1 Framework Knaflic

**Elemen 1: Context (Konteks)**
- **Siapa** audiens Anda? (manajer, investor, publik umum?)
- **Apa** yang Anda ingin mereka ketahui atau lakukan?
- **Bagaimana** data mendukung pesan Anda?

**Elemen 2: Visual (Visualisasi yang Tepat)**
- Pilih jenis chart yang paling efektif
- Hilangkan clutter (elemen yang tidak perlu)
- Gunakan warna secara strategis untuk mengarahkan perhatian (*preattentive attributes*)
- Terapkan prinsip Gestalt (proximity, similarity, enclosure)

**Elemen 3: Story (Narasi)**
- Gunakan struktur **setup → conflict → resolution**:
  - **Setup**: "Indonesia memiliki pertumbuhan ekonomi digital tercepat di Asia Tenggara..."
  - **Conflict**: "...namun 60% UMKM belum go digital..."
  - **Resolution**: "...investasi di edukasi digital dapat menutup gap ini."
- Gunakan judul chart sebagai **insight**, bukan deskripsi
  - Buruk: "Grafik penjualan 2020-2024"
  - Baik: "Penjualan melonjak 150% setelah transformasi digital"

#### 4.2 Contoh Penerapan: Sebelum dan Sesudah

```python
# === SEBELUM: Grafik tanpa storytelling ===
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Data
tahun = ['2020', '2021', '2022', '2023', '2024']
umkm_digital = [13, 19, 24, 30, 36]
umkm_total = [65, 65, 65, 65, 65]  # dalam juta

# SEBELUM: Grafik biasa
axes[0].bar(tahun, umkm_digital, color='blue')
axes[0].set_title('UMKM Digital')
axes[0].set_ylabel('Juta')

# === SESUDAH: Grafik dengan storytelling ===
persen_digital = [d/t*100 for d, t in zip(umkm_digital, umkm_total)]

# Warna: abu-abu untuk tahun lalu, highlight tahun terkini
colors = ['#D3D3D3'] * 4 + ['#FF6B35']

axes[1].bar(tahun, persen_digital, color=colors, edgecolor='white', linewidth=1.5)

# Judul = insight, bukan deskripsi
axes[1].set_title('UMKM Go-Digital Naik 2x Lipat dalam 4 Tahun,\nTapi Masih 55% yang Tertinggal',
                   fontsize=13, fontweight='bold', pad=15)
axes[1].set_ylabel('% UMKM yang Go-Digital', fontsize=11)

# Anotasi pada bar terakhir
axes[1].annotate(f'{persen_digital[-1]:.0f}%',
                  xy=(4, persen_digital[-1]),
                  xytext=(0, 8), textcoords='offset points',
                  fontsize=14, fontweight='bold', color='#FF6B35',
                  ha='center')

# Hilangkan elemen yang tidak perlu (clutter)
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)
axes[1].set_ylim(0, 70)

plt.suptitle('Sebelum vs Sesudah Storytelling', fontsize=15,
             fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

---

### 5. Common Pitfalls dalam Visualisasi Data

Visualisasi data yang buruk dapat **menyesatkan** pembaca. Berikut adalah kesalahan umum yang harus dihindari.

#### 5.1 Misleading Axes / Truncated Y-Axis

**Masalah:** Memotong sumbu Y agar perbedaan kecil terlihat besar.

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Data: Rating approval
bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei']
approval = [62, 61, 60, 59, 58]

# MENYESATKAN: Y-axis dimulai dari 57 (perbedaan terlihat dramatis)
axes[0].plot(bulan, approval, 'ro-', linewidth=2, markersize=8)
axes[0].set_ylim(57, 63)
axes[0].set_title('MENYESATKAN: "Approval Rating Jatuh!"',
                   fontsize=12, color='red', fontweight='bold')
axes[0].set_ylabel('Approval Rating (%)')
axes[0].fill_between(range(5), approval, 57, alpha=0.2, color='red')

# JUJUR: Y-axis dimulai dari 0
axes[1].plot(bulan, approval, 'bo-', linewidth=2, markersize=8)
axes[1].set_ylim(0, 100)
axes[1].set_title('JUJUR: "Approval Rating Relatif Stabil"',
                   fontsize=12, color='green', fontweight='bold')
axes[1].set_ylabel('Approval Rating (%)')
axes[1].fill_between(range(5), approval, 0, alpha=0.1, color='blue')

plt.suptitle('Bahaya Truncated Y-Axis', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

#### 5.2 Pie Chart Overuse

Pie chart **sulit dibandingkan** ketika ada banyak kategori atau selisih proporsi kecil. Alternatif yang lebih baik: bar chart.

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Data
kategori = ['E-commerce', 'Fintech', 'Edtech', 'Healthtech', 'Logistics',
            'Agritech', 'Proptech', 'Others']
nilai = [32, 24, 12, 9, 8, 6, 5, 4]

# KURANG EFEKTIF: Pie chart dengan banyak kategori
axes[0].pie(nilai, labels=kategori, autopct='%1.0f%%', startangle=90,
            textprops={'fontsize': 8})
axes[0].set_title('KURANG EFEKTIF: Pie Chart\n(sulit membandingkan)', fontsize=11,
                   color='red', fontweight='bold')

# LEBIH BAIK: Horizontal bar chart
y_pos = range(len(kategori))
axes[1].barh(y_pos, nilai, color='#36A2EB', edgecolor='white')
axes[1].set_yticks(y_pos)
axes[1].set_yticklabels(kategori)
axes[1].set_xlabel('Persentase (%)')
axes[1].set_title('LEBIH BAIK: Bar Chart\n(mudah dibandingkan)', fontsize=11,
                   color='green', fontweight='bold')
axes[1].invert_yaxis()  # Kategori terbesar di atas
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

# Tambahkan nilai di ujung bar
for i, v in enumerate(nilai):
    axes[1].text(v + 0.5, i, f'{v}%', va='center', fontsize=10)

plt.tight_layout()
plt.show()
```

#### 5.3 Color Blindness Considerations

Sekitar **8% pria dan 0.5% wanita** memiliki buta warna. Tips:
- Hindari kombinasi merah-hijau
- Gunakan palette yang *colorblind-friendly* (contoh: `viridis`, `cividis`)
- Gunakan pattern/shape sebagai pembeda selain warna

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

data = np.random.rand(5, 3)
labels = ['Kategori A', 'Kategori B', 'Kategori C']

# KURANG AKSESIBEL: Merah-hijau
axes[0].bar(range(5), data[:, 0], color='red', label=labels[0])
axes[0].bar(range(5), data[:, 1], bottom=data[:, 0], color='green', label=labels[1])
axes[0].bar(range(5), data[:, 2], bottom=data[:, 0]+data[:, 1], color='#888888', label=labels[2])
axes[0].set_title('KURANG AKSESIBEL\n(merah-hijau)', color='red', fontweight='bold')
axes[0].legend()

# LEBIH AKSESIBEL: Palette colorblind-friendly
colors_cb = ['#0072B2', '#E69F00', '#56B4E9']  # Blue, Orange, Light Blue
axes[1].bar(range(5), data[:, 0], color=colors_cb[0], label=labels[0])
axes[1].bar(range(5), data[:, 1], bottom=data[:, 0], color=colors_cb[1], label=labels[1])
axes[1].bar(range(5), data[:, 2], bottom=data[:, 0]+data[:, 1], color=colors_cb[2], label=labels[2])
axes[1].set_title('LEBIH AKSESIBEL\n(colorblind-friendly)', color='green', fontweight='bold')
axes[1].legend()

plt.suptitle('Pertimbangan Color Blindness', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

## Studi Kasus: Membuat "Data Story" tentang Ekonomi Digital Indonesia

### Konteks

Anda adalah data analyst di sebuah lembaga riset. Tugas Anda: membuat **presentasi visual** tentang perkembangan ekonomi digital Indonesia untuk pihak kementerian. Gunakan framework Knaflic untuk membangun narasi.

### Dataset

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data Ekonomi Digital Indonesia (dalam miliar USD)
data_ekonomi = pd.DataFrame({
    'Tahun': [2019, 2020, 2021, 2022, 2023, 2024],
    'E-commerce': [21, 32, 47, 59, 62, 65],
    'Transport_Food': [8, 6, 8, 11, 13, 15],
    'Travel': [10, 4, 5, 9, 12, 15],
    'Fintech': [2, 4, 8, 14, 18, 22],
    'Media': [3, 4, 5, 6, 7, 8]
})

data_ekonomi['Total'] = data_ekonomi[['E-commerce', 'Transport_Food',
                                       'Travel', 'Fintech', 'Media']].sum(axis=1)

print(data_ekonomi)
```

### Visualisasi 1: Tren Pertumbuhan

```python
# Storytelling: Judul = Insight
plt.figure(figsize=(12, 7))

# Area chart untuk komposisi
sektor = ['E-commerce', 'Fintech', 'Transport_Food', 'Travel', 'Media']
colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF']

plt.stackplot(data_ekonomi['Tahun'],
              [data_ekonomi[s] for s in sektor],
              labels=sektor, colors=colors, alpha=0.8)

# Judul sebagai insight
plt.title('Ekonomi Digital Indonesia Menembus $125 Miliar:\nFintech Jadi Bintang dengan Pertumbuhan 11x Lipat',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Tahun', fontsize=12)
plt.ylabel('Nilai (Miliar USD)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, alpha=0.2)

# Hilangkan clutter
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
```

### Visualisasi 2: Perbandingan Growth Rate

```python
# Menghitung growth rate 2019-2024
growth_data = pd.DataFrame({
    'Sektor': sektor,
    'Nilai_2019': [data_ekonomi[s].iloc[0] for s in sektor],
    'Nilai_2024': [data_ekonomi[s].iloc[-1] for s in sektor],
})
growth_data['Growth_Persen'] = ((growth_data['Nilai_2024'] - growth_data['Nilai_2019'])
                                 / growth_data['Nilai_2019'] * 100)
growth_data = growth_data.sort_values('Growth_Persen', ascending=True)

plt.figure(figsize=(10, 6))
colors_bar = ['#D3D3D3'] * (len(growth_data) - 1) + ['#FF6B35']
bars = plt.barh(growth_data['Sektor'], growth_data['Growth_Persen'], color=colors_bar)

for bar, val in zip(bars, growth_data['Growth_Persen']):
    plt.text(val + 15, bar.get_y() + bar.get_height()/2,
             f'{val:.0f}%', va='center', fontsize=12, fontweight='bold')

plt.title('Fintech: Sektor dengan Pertumbuhan Tercepat\ndalam Ekonomi Digital Indonesia (2019-2024)',
          fontsize=14, fontweight='bold')
plt.xlabel('Pertumbuhan (%)', fontsize=12)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.show()
```

### Narasi (Story)

> **Setup:** "Ekonomi digital Indonesia tumbuh pesat, mencapai $125 miliar pada 2024, menjadikannya yang terbesar di Asia Tenggara."
>
> **Conflict:** "Namun, pertumbuhan ini tidak merata. Sementara Fintech tumbuh 1000%, sektor Travel baru pulih ke level pra-pandemi."
>
> **Resolution:** "Investasi di infrastruktur digital dan literasi keuangan digital perlu diprioritaskan untuk memastikan pertumbuhan yang inklusif di semua sektor."

---

## AI Corner: Minta AI Merekomendasikan Jenis Visualisasi yang Tepat

### Cara Menggunakan AI untuk Visualisasi

Anda dapat meminta AI (seperti ChatGPT, Claude, atau Gemini) untuk membantu:

1. **Memilih jenis visualisasi** berdasarkan data Anda
2. **Mereview** grafik yang sudah dibuat
3. **Memperbaiki** kode matplotlib/seaborn
4. **Menulis narasi** untuk data story

### Contoh Prompt

**Prompt 1 — Rekomendasi chart:**
```
Saya memiliki dataset dengan kolom berikut:
- provinsi (33 kategori)
- tahun (2019-2024)
- jumlah_umkm (numerik)
- sektor (5 kategori: kuliner, fashion, kerajinan, jasa, teknologi)

Saya ingin menunjukkan tren pertumbuhan UMKM per sektor dari waktu ke waktu.
Jenis visualisasi apa yang paling tepat? Berikan kode Python-nya.
```

**Prompt 2 — Review grafik:**
```
Berikut kode grafik saya: [paste kode].
Apakah ada pelanggaran prinsip Tufte? Bagaimana cara memperbaikinya?
Apakah grafik ini accessible untuk penderita buta warna?
```

### Catatan Penting

- **Selalu verifikasi** rekomendasi AI — AI bisa salah memilih chart type
- **Jangan copy-paste** kode AI tanpa memahaminya
- **Gunakan AI sebagai asisten**, bukan pengganti pemahaman Anda tentang data
- Pastikan narasi yang dihasilkan AI **sesuai dengan data asli** Anda

---

## Latihan Mandiri

### Latihan 1: Eksplorasi Visual (Sub-CPMK 3.1)

Gunakan dataset `tips` dari seaborn (`sns.load_dataset('tips')`) untuk membuat:
1. Histogram distribusi `total_bill` dengan overlay KDE
2. Scatter plot `total_bill` vs `tip` dengan warna berdasarkan `time` (Lunch/Dinner)
3. Boxplot `tip` per `day` dengan highlight hari Sabtu

### Latihan 2: Data Storytelling (Sub-CPMK 3.2)

Buatlah **minimal 3 visualisasi** yang membentuk satu "data story" tentang topik pilihan berikut:
- Tren penggunaan media sosial di Indonesia
- Perbandingan biaya hidup di kota-kota besar Indonesia
- Perkembangan e-commerce di Asia Tenggara

Untuk setiap visualisasi:
- Judul harus berupa **insight** (bukan deskripsi)
- Terapkan minimal 2 prinsip Tufte
- Tulis narasi setup → conflict → resolution

### Latihan 3: Perbaiki Grafik (Critical Thinking)

Berikut kode grafik yang mengandung beberapa masalah. Identifikasi masalahnya dan perbaiki:

```python
# Kode bermasalah — perbaiki ini!
plt.figure(figsize=(6, 6))
kategori = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
nilai = [23, 22, 21, 20, 19, 18, 17, 16, 15, 14]
plt.pie(nilai, labels=kategori, autopct='%1.1f%%')
plt.title('Data')
plt.show()
```

**Pertanyaan:**
1. Apa masalah dari grafik di atas? (minimal 3 masalah)
2. Bagaimana Anda memperbaikinya? Tuliskan kode yang sudah diperbaiki.

---

## Referensi

1. Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press.
2. Knaflic, C. N. (2015). *Storytelling with Data: A Data Visualization Guide for Business Professionals*. Wiley.
3. Matplotlib Documentation. https://matplotlib.org/stable/
4. Seaborn Documentation. https://seaborn.pydata.org/
5. Wilke, C. O. (2019). *Fundamentals of Data Visualization*. O'Reilly Media. https://clauswilke.com/dataviz/
6. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media. — Chapter 9: Plotting and Visualization.
7. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media. — Chapter 4: Visualization with Matplotlib.

---

*Modul ini adalah bagian dari mata kuliah Analisis Data Statistik, Program Studi Informatika, Universitas Al Azhar Indonesia. Semester Genap 2025/2026.*
