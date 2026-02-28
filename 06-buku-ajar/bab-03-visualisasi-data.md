# BAB 3: VISUALISASI DATA DAN DATA STORYTELLING

**Tri Aji Nugroho, S.T., M.T.**
Analisis Data Statistik — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|-----------|-----------|---------|
| CPMK-2.6 | Menjelaskan prinsip desain visualisasi data yang efektif berdasarkan framework Edward Tufte | C2 |
| CPMK-2.7 | Membuat berbagai jenis grafik (line plot, bar chart, scatter plot, histogram, boxplot, heatmap) menggunakan matplotlib dan seaborn | C3 |
| CPMK-2.8 | Memilih jenis visualisasi yang tepat berdasarkan tipe data dan tujuan komunikasi | C3 |
| CPMK-2.9 | Menerapkan prinsip data storytelling (framework Knaflic) untuk mengubah grafik menjadi narasi bermakna | C3 |
| CPMK-2.10 | Mengkustomisasi visualisasi (warna, label, anotasi) dan menghindari common pitfalls | C3 |

---

## 3.1 Prinsip Desain Visualisasi Data

### 3.1.1 Mengapa Visualisasi Penting?

Otak manusia memproses informasi visual **60.000 kali lebih cepat** dibandingkan teks. Sebuah tabel berisi ribuan angka bisa sangat sulit dipahami, tetapi satu grafik yang tepat mampu mengungkap pola, tren, dan anomali dalam sekejap.

> "The greatest value of a picture is when it forces us to notice what we never expected to see."
> — John W. Tukey, *Exploratory Data Analysis* (1977)

Dalam konteks informatika dan data science, visualisasi data berperan untuk:
- **Eksplorasi**: menemukan pola tersembunyi di tahap awal analisis (EDA)
- **Komunikasi**: menyampaikan temuan kepada audiens non-teknis (manajer, stakeholder)
- **Validasi**: memeriksa asumsi statistik sebelum menjalankan uji hipotesis
- **Monitoring**: dashboard real-time untuk performa sistem atau bisnis

### 3.1.2 Prinsip-prinsip Edward Tufte

Edward Tufte, profesor emeritus di Yale University, dikenal sebagai "Leonardo da Vinci of Data" karena kontribusinya terhadap teori visualisasi data. Berikut prinsip utamanya.

**a) Data-Ink Ratio**

> "Above all else, show the data." — Edward Tufte

Data-ink ratio mengukur proporsi elemen visual ("tinta") pada grafik yang benar-benar menyampaikan **informasi data** dibandingkan total elemen visual.

```
Data-Ink Ratio = (Elemen yang menampilkan data) / (Total elemen pada grafik)
```

Prinsipnya: **maksimalkan data-ink ratio**. Setiap piksel pada grafik harus memiliki alasan untuk ada. Hapus elemen yang tidak menambah informasi: grid berlebihan, border tidak perlu, dekorasi kosmetik.

```
  RENDAH Data-Ink Ratio          TINGGI Data-Ink Ratio
  ┌─────────────────────┐        ┌─────────────────────┐
  │░░ JUDUL BESAR ░░░░░ │        │ Penjualan Naik 23%  │
  │╔═══════════════════╗│        │ ████████████  45%    │
  │║ ████ 45%  ░░░░░░░ ║│        │ ████████████████ 60% │
  │║ ██████ 60%  ░░░░░ ║│        │ ████████  30%        │
  │╚═══════════════════╝│        │ Sumber: BPS 2024     │
  │[Logo] [Border] [3D] │        └─────────────────────┘
  └─────────────────────┘         Fokus pada data
   Banyak elemen dekoratif
```

**b) Chartjunk**

Chartjunk adalah elemen visual yang **tidak menambah informasi** dan justru mengalihkan perhatian dari data. Contoh chartjunk yang sering dijumpai:
- Efek 3D pada bar chart (mendistorsi proporsi)
- Background gambar atau gradien yang mengganggu
- Garis grid yang terlalu tebal dan rapat
- Clip art, icon dekoratif, atau ornamen berlebihan

**c) Lie Factor**

Lie factor mengukur seberapa **jujur** sebuah grafik merepresentasikan data.

```
Lie Factor = (Ukuran efek yang ditampilkan di grafik) / (Ukuran efek di data)
```

Lie factor = 1.0 berarti representasi akurat. Nilai > 1.05 atau < 0.95 menandakan **distorsi visual** yang harus dihindari. Contoh umum: memotong sumbu Y agar perbedaan kecil terlihat dramatis.

### 3.1.3 Memilih Jenis Chart yang Tepat

Pemilihan jenis chart bergantung pada **tipe data** dan **tujuan komunikasi**. Berikut panduan praktis:

| Tujuan Komunikasi | Tipe Data | Chart yang Tepat |
|-------------------|-----------|-----------------|
| Perbandingan antar kategori | Kategorikal | Bar chart, grouped bar chart |
| Distribusi satu variabel | Numerik kontinu | Histogram, boxplot, violin plot |
| Hubungan dua variabel | Numerik vs numerik | Scatter plot |
| Tren sepanjang waktu | Time series | Line plot |
| Komposisi / proporsi | Kategorikal (sedikit) | Stacked bar chart, (pie chart — hati-hati!) |
| Korelasi banyak variabel | Numerik multivariat | Heatmap, pairplot |
| Distribusi per kategori | Numerik + kategorikal | Boxplot, violin plot |

**Decision tree** berikut membantu memilih chart yang tepat:

```
                    APA YANG INGIN DITAMPILKAN?
                              │
          ┌───────────┬───────┼───────┬────────────┐
          │           │       │       │            │
      PERBANDINGAN  DISTRIBUSI  HUBUNGAN   TREN       KOMPOSISI
          │           │       │       │            │
     ┌────┴────┐   ┌──┴──┐   │    Line Plot   Stacked Bar
     │         │   │     │   │                 (bukan Pie!)
  Bar Chart  Grouped  Histogram  Scatter
  (≤10 kat)  Bar     Boxplot    Plot
             Chart   Violin
```

> **Tips:** Hindari pie chart jika kategori lebih dari 5, atau jika selisih proporsi antar kategori kecil. Mata manusia lebih baik membandingkan **panjang** (bar chart) daripada **sudut** (pie chart).

---

## 3.2 Matplotlib: Fondasi Visualisasi Python

### 3.2.1 Arsitektur Matplotlib

`matplotlib` adalah library visualisasi paling fundamental di ekosistem Python. Hampir semua library visualisasi Python lainnya (termasuk seaborn, plotly) dibangun di atas matplotlib.

```
            ARSITEKTUR MATPLOTLIB
            =====================

  ┌─────────────────────────────────────┐
  │              Figure                 │  ← Kanvas utama (kertas gambar)
  │  ┌──────────────┐ ┌──────────────┐  │
  │  │   Axes (1)   │ │   Axes (2)   │  │  ← Subplot (area plot individual)
  │  │ ┌──────────┐ │ │ ┌──────────┐ │  │
  │  │ │  Plot    │ │ │ │  Plot    │ │  │  ← Grafik (line, bar, scatter, dll)
  │  │ │ (data)   │ │ │ │ (data)   │ │  │
  │  │ └──────────┘ │ │ └──────────┘ │  │
  │  │ xlabel ylabel│ │ xlabel ylabel│  │  ← Label sumbu
  │  │    title     │ │    title     │  │  ← Judul subplot
  │  └──────────────┘ └──────────────┘  │
  │             suptitle                │  ← Judul utama Figure
  └─────────────────────────────────────┘
```

Konsep utama: **Figure** = wadah keseluruhan (kertas gambar), **Axes** = area individual tempat data diplot.

### 3.2.2 Setup Awal

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline
np.random.seed(42)
```

### 3.2.3 Line Plot — Tren Waktu

Line plot ideal untuk menampilkan **perubahan data sepanjang waktu** (time series).

```python
# Data: Pertumbuhan pengguna internet di Indonesia (juta orang)
tahun = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
pengguna_internet = [171.2, 196.7, 175.4, 202.6, 210.0, 215.6, 221.5]

# Membuat line plot
plt.figure(figsize=(10, 6))
plt.plot(tahun, pengguna_internet, marker='o', color='#2196F3',
         linewidth=2, markersize=8, label='Pengguna Internet')

# Menambahkan label dan judul
plt.title('Pertumbuhan Pengguna Internet di Indonesia',
          fontsize=14, fontweight='bold')
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

### 3.2.4 Bar Chart — Perbandingan Kategori

Bar chart efektif untuk **membandingkan nilai antar kategori diskret**.

```python
sektor = ['E-commerce', 'Fintech', 'Edtech', 'Healthtech', 'Logistics']
jumlah = [2500, 1800, 950, 620, 780]

plt.figure(figsize=(10, 6))
bars = plt.barh(sektor, jumlah,
                color=['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'])
for bar, val in zip(bars, jumlah):
    plt.text(val + 30, bar.get_y() + bar.get_height()/2,
             f'{val:,}', va='center', fontsize=11)
plt.title('Jumlah Startup per Sektor di Indonesia (2024)',
          fontsize=14, fontweight='bold')
plt.xlabel('Jumlah Startup', fontsize=12)
plt.xlim(0, max(jumlah) * 1.15)
plt.tight_layout()
plt.show()
```

### 3.2.5 Scatter Plot — Hubungan Dua Variabel

Scatter plot menunjukkan **hubungan (korelasi) antara dua variabel numerik**.

```python
# Data simulasi: IPK vs Jam Belajar per Minggu
np.random.seed(42)
jam_belajar = np.random.uniform(5, 30, 50)
ipk = 2.0 + 0.06 * jam_belajar + np.random.normal(0, 0.3, 50)
ipk = np.clip(ipk, 2.0, 4.0)

plt.figure(figsize=(10, 6))
plt.scatter(jam_belajar, ipk, alpha=0.7, c='#2196F3',
            edgecolors='white', s=80)

# Garis tren (regresi linear sederhana)
z = np.polyfit(jam_belajar, ipk, 1)
p = np.poly1d(z)
plt.plot(np.linspace(5, 30, 100), p(np.linspace(5, 30, 100)),
         '--', color='red', label=f'Tren: y = {z[0]:.3f}x + {z[1]:.3f}')

plt.title('Hubungan Jam Belajar dan IPK Mahasiswa', fontsize=14, fontweight='bold')
plt.xlabel('Jam Belajar per Minggu', fontsize=12)
plt.ylabel('IPK', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 3.2.6 Histogram — Distribusi Data

Histogram menampilkan **distribusi frekuensi** dari data numerik kontinu. Berbeda dari bar chart, sumbu X pada histogram adalah kontinu (bukan kategorikal).

```python
# Data simulasi: Nilai UTS Statistika (100 mahasiswa)
np.random.seed(42)
nilai_uts = np.random.normal(loc=72, scale=12, size=100)
nilai_uts = np.clip(nilai_uts, 30, 100)

plt.figure(figsize=(10, 6))

# Histogram dengan overlay KDE (Kernel Density Estimation)
counts, bins, patches = plt.hist(nilai_uts, bins=15, color='#36A2EB',
                                  edgecolor='white', alpha=0.7,
                                  density=True, label='Histogram')

# Overlay kurva KDE
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

## 3.3 Seaborn: Visualisasi Statistik Tingkat Tinggi

### 3.3.1 Mengapa Seaborn?

`seaborn` dibangun di atas matplotlib dan menyediakan **antarmuka tingkat tinggi** untuk visualisasi statistik. Kelebihan: styling lebih menarik, integrasi langsung dengan pandas DataFrame, dan pengelompokan data otomatis via parameter `hue`.

```python
import seaborn as sns
sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)

# Memuat dataset contoh bawaan seaborn
tips = sns.load_dataset('tips')
print(tips.head())
print(f"Shape: {tips.shape}, Columns: {list(tips.columns)}")
```

### 3.3.2 Boxplot — Distribusi dan Outlier

Boxplot menampilkan ringkasan lima angka (**minimum, Q1, median, Q3, maximum**) dan mendeteksi outlier secara visual.

```
  ANATOMI BOXPLOT
  ===============
           ──┬──  ← Maximum (atau Q3 + 1.5*IQR)
     ┌───────┴───────┐
     │      Q3       │ ← Kuartil 3 (persentil 75)
     │───────────────│
     │    MEDIAN     │ ← Median (persentil 50)
     │───────────────│
     │      Q1       │ ← Kuartil 1 (persentil 25)
     └───────┬───────┘   IQR = Q3 - Q1
           ──┴──  ← Minimum (atau Q1 - 1.5*IQR)
     o            ← Outlier
```

```python
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='total_bill', hue='sex',
            palette='Set2')

plt.title('Distribusi Total Bill per Hari dan Gender',
          fontsize=14, fontweight='bold')
plt.xlabel('Hari', fontsize=12)
plt.ylabel('Total Bill ($)', fontsize=12)
plt.legend(title='Gender')
plt.tight_layout()
plt.show()
```

### 3.3.3 Violin Plot — Distribusi Detail

Violin plot menggabungkan boxplot dengan KDE. Gunakan `split=True` untuk membandingkan dua kelompok secara berdampingan:

```python
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex',
               split=True, inner='quart', palette='pastel')
```

### 3.3.4 Heatmap — Korelasi Antar Variabel

Heatmap sangat berguna untuk memvisualisasikan **matriks korelasi** antar variabel numerik.

```python
# Menghitung matriks korelasi
tips_numeric = tips.select_dtypes(include=[np.number])
korelasi = tips_numeric.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(korelasi, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, square=True, linewidths=1,
            cbar_kws={'label': 'Koefisien Korelasi'})

plt.title('Heatmap Korelasi — Dataset Tips',
          fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

Cara membaca: nilai mendekati +1 (merah) = korelasi positif kuat, -1 (biru) = negatif kuat, 0 (putih) = tidak ada korelasi.

### 3.3.5 Pairplot — Eksplorasi Multivariat

Pairplot membuat **matriks scatter plot** untuk semua pasangan variabel numerik. Sangat berguna untuk EDA pada dataset baru.

```python
iris = sns.load_dataset('iris')
sns.pairplot(iris, hue='species', palette='Dark2',
             diag_kind='kde', height=2.5,
             plot_kws={'alpha': 0.6, 's': 50, 'edgecolor': 'white'})
plt.suptitle('Pairplot — Dataset Iris', fontsize=16, fontweight='bold', y=1.02)
plt.show()
```

### 3.3.6 Countplot — Frekuensi Kategori

Countplot menampilkan **jumlah observasi per kategori**, cocok untuk variabel kategorikal.

```python
sns.countplot(data=tips, x='day', hue='time',
              palette='viridis', order=['Thur', 'Fri', 'Sat', 'Sun'])
plt.title('Jumlah Transaksi per Hari dan Waktu', fontsize=14, fontweight='bold')
plt.show()
```

---

## 3.4 Data Storytelling: Dari Chart ke Insight ke Narasi

### 3.4.1 Mengapa Storytelling Penting?

Membuat grafik yang secara teknis benar saja **tidak cukup**. Seorang data analyst harus mampu **bercerita dengan data** agar audiens memahami pesan dan mengambil tindakan.

> "Numbers have an important story to tell. They rely on you to give them a clear and convincing voice."
> — Stephen Few

### 3.4.2 Framework Knaflic

Cole Nussbaumer Knaflic, dalam bukunya *Storytelling with Data* (2015), merumuskan framework tiga elemen:

```
  FRAMEWORK DATA STORYTELLING (KNAFLIC)
  ======================================
  ┌────────────────┐
  │  1. CONTEXT    │ → Siapa audiens? Apa tujuan?
  └───────┬────────┘
  ┌───────▼────────┐
  │  2. VISUAL     │ → Chart tepat, hilangkan clutter, warna strategis
  └───────┬────────┘
  ┌───────▼────────┐
  │  3. STORY      │ → Setup → Conflict → Resolution
  └────────────────┘
```

**Elemen 1: Context** — Siapa audiens? Apa yang ingin mereka ketahui/lakukan? Bagaimana data mendukung pesan?

**Elemen 2: Visual** — Pilih chart yang tepat, hilangkan clutter, gunakan warna strategis (*preattentive attributes*), terapkan prinsip Gestalt (proximity, similarity, enclosure).

**Elemen 3: Story** — Gunakan struktur **Setup -- Conflict -- Resolution**. Judul chart harus berupa **insight**, bukan deskripsi:
- Buruk: "Grafik Penjualan 2020-2024"
- Baik: "Penjualan Melonjak 150% Setelah Transformasi Digital"

### 3.4.3 Contoh Penerapan: Sebelum dan Sesudah Storytelling

```python
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
tahun = ['2020', '2021', '2022', '2023', '2024']
umkm_digital = [13, 19, 24, 30, 36]
persen = [d/65*100 for d in umkm_digital]  # 65 juta = total UMKM

# SEBELUM: tanpa storytelling
axes[0].bar(tahun, umkm_digital, color='blue')
axes[0].set_title('UMKM Digital')
axes[0].set_ylabel('Juta')

# SESUDAH: dengan storytelling
colors = ['#D3D3D3'] * 4 + ['#FF6B35']  # highlight tahun terkini
axes[1].bar(tahun, persen, color=colors, edgecolor='white')
axes[1].set_title('UMKM Go-Digital Naik 2x Lipat dalam 4 Tahun,\n'
    'Tapi Masih 55% yang Tertinggal', fontsize=13, fontweight='bold')
axes[1].set_ylabel('% UMKM yang Go-Digital')
axes[1].annotate(f'{persen[-1]:.0f}%', xy=(4, persen[-1]),
    xytext=(0, 8), textcoords='offset points',
    fontsize=14, fontweight='bold', color='#FF6B35', ha='center')
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

plt.suptitle('Sebelum vs Sesudah Storytelling', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

## 3.5 Kustomisasi Plot: Warna, Label, dan Anotasi

### 3.5.1 Sistem Warna yang Efektif

Warna bukan sekadar estetika — warna adalah **alat komunikasi**. Gunakan warna secara strategis:

| Strategi | Penjelasan | Contoh |
|----------|-----------|--------|
| **Highlight** | Satu warna mencolok di antara warna netral | Satu bar oranye, sisanya abu-abu |
| **Sequential** | Gradasi satu warna untuk data berurutan | Ringan → gelap untuk nilai rendah → tinggi |
| **Diverging** | Dua warna berlawanan untuk data berpusat | Biru (negatif) ← putih → merah (positif) |
| **Categorical** | Warna berbeda untuk kategori berbeda | Set warna viridis, Set2, Dark2 |

**Pertimbangan aksesibilitas (color blindness):** Sekitar 8% pria dan 0.5% wanita memiliki kondisi buta warna. Tips:
- Hindari kombinasi **merah-hijau** sebagai satu-satunya pembeda
- Gunakan palette *colorblind-friendly*: `viridis`, `cividis`, `colorblind` (seaborn)
- Gunakan pattern/shape sebagai pembeda tambahan selain warna

```python
# Palette colorblind-friendly yang direkomendasikan
# (Okabe-Ito palette, sumber: https://jfly.uni-koeln.de/color/)
palette_cb = ['#0072B2', '#E69F00', '#56B4E9', '#009E73',
              '#F0E442', '#CC79A7', '#D55E00', '#000000']

# Contoh penggunaan di seaborn
sns.set_palette(palette_cb)
# atau gunakan palette bawaan: sns.set_palette('colorblind')
```

### 3.5.2 Anotasi dan Label yang Informatif

Anotasi membantu audiens memahami **titik-titik penting** pada grafik tanpa harus membaca angka dari sumbu. Fungsi-fungsi utama matplotlib untuk anotasi:

```python
# plt.annotate() — teks dengan panah penunjuk ke titik data
plt.annotate('Pandemi COVID-19\nmempercepat digitalisasi',
             xy=(2020, 32),           # titik yang ditunjuk
             xytext=(2020.5, 50),     # posisi teks
             fontsize=10, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
             bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))

# plt.text() — teks sederhana di posisi tertentu
plt.text(2024, 65, '$65B', ha='center', fontsize=10, fontweight='bold')

# plt.axhline() / plt.axvline() — garis referensi horizontal/vertikal
plt.axhline(y=50, color='red', linestyle='--', alpha=0.5, label='Target')
```

---

## 3.6 Common Pitfalls dalam Visualisasi Data

### 3.6.1 Truncated Y-Axis (Sumbu Y Terpotong)

Memotong sumbu Y agar perbedaan kecil terlihat dramatis adalah bentuk **misleading visualization** yang paling umum.

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei']
approval = [62, 61, 60, 59, 58]

# MENYESATKAN: Y-axis dimulai dari 57
axes[0].plot(bulan, approval, 'ro-', linewidth=2, markersize=8)
axes[0].set_ylim(57, 63)
axes[0].set_title('MENYESATKAN: "Approval Jatuh!"', color='red', fontweight='bold')

# JUJUR: Y-axis dimulai dari 0
axes[1].plot(bulan, approval, 'bo-', linewidth=2, markersize=8)
axes[1].set_ylim(0, 100)
axes[1].set_title('JUJUR: "Approval Relatif Stabil"', color='green', fontweight='bold')

plt.suptitle('Bahaya Truncated Y-Axis', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### 3.6.2 Pie Chart Overuse

Pie chart **sulit dibandingkan** ketika ada banyak kategori (>5) atau selisih proporsi kecil. Mata manusia lebih baik membandingkan **panjang** (bar chart) daripada **sudut** (pie chart). Selalu pertimbangkan horizontal bar chart sebagai alternatif yang lebih efektif.

### 3.6.3 Ringkasan Pitfalls

```
  COMMON PITFALLS VISUALISASI DATA
  =================================

  1. Truncated Y-Axis     → Selalu mulai dari 0 (kecuali ada alasan kuat)
  2. Pie Chart Overuse     → Gunakan bar chart jika kategori > 5
  3. Efek 3D               → Hindari! Mendistorsi proporsi
  4. Dual Y-Axis           → Sering menyesatkan, gunakan dua panel terpisah
  5. Merah-Hijau           → Tidak aksesibel untuk penderita buta warna
  6. Judul Deskriptif      → Ganti dengan judul berisi insight
  7. Overplotting           → Gunakan alpha, jitter, atau heatmap
  8. Missing Context       → Selalu sertakan sumber data dan satuan
```

---

## 3.7 Studi Kasus: Visualisasi Data Ekonomi Digital Indonesia

### 3.7.1 Konteks

Anda adalah data analyst di sebuah lembaga riset. Tugas Anda: membuat **presentasi visual** tentang perkembangan ekonomi digital Indonesia untuk kementerian. Gunakan framework Knaflic untuk membangun narasi yang persuasif.

### 3.7.2 Membangun Dataset

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

### 3.7.3 Visualisasi 1: Tren Pertumbuhan (Area Chart)

```python
sektor = ['E-commerce', 'Fintech', 'Transport_Food', 'Travel', 'Media']
colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF']

plt.figure(figsize=(12, 7))
plt.stackplot(data_ekonomi['Tahun'],
              [data_ekonomi[s] for s in sektor],
              labels=sektor, colors=colors, alpha=0.8)
plt.title('Ekonomi Digital Indonesia Menembus $125 Miliar:\n'
          'Fintech Jadi Bintang dengan Pertumbuhan 11x Lipat',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Tahun', fontsize=12)
plt.ylabel('Nilai (Miliar USD)', fontsize=12)
plt.legend(loc='upper left')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.show()
```

### 3.7.4 Visualisasi 2: Perbandingan Growth Rate

```python
# Menghitung growth rate 2019-2024 per sektor
growth = {s: (data_ekonomi[s].iloc[-1] / data_ekonomi[s].iloc[0] - 1) * 100
          for s in sektor}
growth_sorted = dict(sorted(growth.items(), key=lambda x: x[1]))

plt.figure(figsize=(10, 6))
colors_bar = ['#D3D3D3'] * (len(growth_sorted) - 1) + ['#FF6B35']
bars = plt.barh(list(growth_sorted.keys()), list(growth_sorted.values()),
                color=colors_bar)
for bar, val in zip(bars, growth_sorted.values()):
    plt.text(val + 15, bar.get_y() + bar.get_height()/2,
             f'{val:.0f}%', va='center', fontsize=12, fontweight='bold')
plt.title('Fintech: Sektor dengan Pertumbuhan Tercepat\n'
          'dalam Ekonomi Digital Indonesia (2019-2024)',
          fontsize=14, fontweight='bold')
plt.xlabel('Pertumbuhan (%)', fontsize=12)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.show()
```

### 3.7.5 Narasi Data Story

Dengan dua visualisasi di atas, kita membangun narasi menggunakan struktur Setup-Conflict-Resolution:

> **Setup:** "Ekonomi digital Indonesia tumbuh pesat, mencapai $125 miliar pada 2024, menjadikannya yang terbesar di Asia Tenggara."
>
> **Conflict:** "Namun, pertumbuhan ini tidak merata. Sementara Fintech tumbuh 1000%, sektor Travel baru pulih ke level pra-pandemi."
>
> **Resolution:** "Investasi di infrastruktur digital dan literasi keuangan digital perlu diprioritaskan untuk memastikan pertumbuhan yang inklusif di semua sektor."

---

## AI Corner: Menggunakan AI untuk Visualisasi Data

### Cara Memanfaatkan AI

AI generatif (ChatGPT, Claude, Gemini) dapat menjadi **asisten** yang produktif untuk visualisasi data:

| AI Bisa Membantu | Yang Tetap Tugas Anda |
|------------------|-----------------------|
| Merekomendasikan jenis chart berdasarkan data | Memahami konteks dan tujuan komunikasi |
| Menulis kode matplotlib/seaborn | Memastikan grafik merepresentasikan data dengan jujur |
| Memperbaiki error di kode visualisasi | Memvalidasi apakah insight yang muncul masuk akal |
| Menyarankan perbaikan berdasarkan prinsip Tufte | Menentukan narasi dan rekomendasi berdasarkan domain knowledge |
| Menulis template narasi data story | Menyesuaikan narasi dengan konteks audiens |

### Contoh Prompt yang Efektif

**Prompt 1 — Rekomendasi chart:**
```
Saya memiliki dataset dengan kolom berikut:
- provinsi (33 kategori)
- tahun (2019-2024)
- jumlah_umkm (numerik)
- sektor (5 kategori: kuliner, fashion, kerajinan, jasa, teknologi)

Saya ingin menunjukkan tren pertumbuhan UMKM per sektor dari waktu ke waktu.
Jenis visualisasi apa yang paling tepat? Berikan kode Python-nya
menggunakan matplotlib dan seaborn.
```

**Prompt 2 — Review grafik:**
```
Berikut kode matplotlib saya: [paste kode].
Tolong review berdasarkan prinsip Tufte:
1. Apakah data-ink ratio sudah optimal?
2. Ada chartjunk yang perlu dihapus?
3. Apakah grafik ini accessible untuk penderita buta warna?
4. Saran perbaikan spesifik apa yang bisa diterapkan?
```

**Prompt 3 — Data storytelling:**
```
Saya punya data: pengguna internet Indonesia naik dari 171 juta (2018)
ke 221 juta (2024), tapi pertumbuhan melambat dari 14%/tahun menjadi 3%/tahun.
Bantu saya menulis narasi data story (setup-conflict-resolution)
untuk audiens pemerintah.
```

### Etika dan Batasan

- **Selalu verifikasi** rekomendasi AI — AI bisa memilih chart yang kurang tepat
- **Jangan copy-paste** kode AI tanpa memahami cara kerjanya
- **Gunakan AI sebagai asisten**, bukan pengganti pemahaman Anda
- Dokumentasikan penggunaan AI dalam AI Usage Log sesuai kebijakan mata kuliah

---

## Rangkuman Bab 3

1. **Visualisasi data** bukan sekadar grafik yang menarik, melainkan **komunikasi informasi yang jelas, jujur, dan efektif**.

2. **Prinsip Tufte**: maksimalkan *data-ink ratio*, hindari *chartjunk*, jaga *lie factor* mendekati 1.0.

3. **Matplotlib** adalah fondasi visualisasi Python (arsitektur Figure-Axes): `plot()`, `bar()`, `scatter()`, `hist()`.

4. **Seaborn** menyediakan antarmuka tingkat tinggi untuk visualisasi statistik: `boxplot()`, `violinplot()`, `heatmap()`, `pairplot()`, `countplot()`.

5. **Pemilihan chart** bergantung pada tipe data dan tujuan: line plot (tren), bar chart (perbandingan), scatter plot (hubungan), histogram (distribusi), boxplot (distribusi per kelompok), heatmap (korelasi).

6. **Data storytelling** (framework Knaflic): Context -- Visual -- Story, dengan struktur narasi setup-conflict-resolution.

7. **Kustomisasi**: warna strategis, anotasi titik penting, label informatif, aksesibilitas (color blindness).

8. **Pitfalls**: truncated Y-axis, pie chart berlebihan, efek 3D, kombinasi merah-hijau, judul deskriptif.

---

## Latihan Soal

### Tingkat Dasar (C1-C2)

**Soal 1.** Jelaskan apa yang dimaksud dengan *data-ink ratio* menurut Edward Tufte. Mengapa prinsip ini penting dalam membuat visualisasi data?

**Soal 2.** Perhatikan daftar elemen visual berikut pada sebuah bar chart. Klasifikasikan mana yang termasuk "data ink" dan mana yang termasuk "chartjunk":
- a) Tinggi bar yang merepresentasikan nilai data
- b) Efek bayangan 3D pada setiap bar
- c) Label angka di ujung setiap bar
- d) Background bergambar peta Indonesia
- e) Judul chart
- f) Grid horizontal tipis (alpha=0.3)
- g) Border tebal mengelilingi area plot

**Soal 3.** Untuk setiap skenario berikut, tentukan jenis chart yang paling tepat dan jelaskan alasannya:
- a) Membandingkan jumlah mahasiswa di 6 fakultas UAI
- b) Menampilkan distribusi nilai UAS 200 mahasiswa
- c) Menunjukkan hubungan antara jam belajar dan IPK
- d) Menampilkan tren jumlah pengguna internet Indonesia dari 2018-2024
- e) Memvisualisasikan korelasi antara 5 variabel numerik

**Soal 4.** Jelaskan perbedaan antara histogram dan bar chart. Kapan masing-masing digunakan?

### Tingkat Menengah (C2-C3)

**Soal 5.** Tulis kode Python menggunakan matplotlib untuk membuat line plot yang menampilkan data berikut (pertumbuhan pengguna e-wallet di Indonesia):

| Tahun | GoPay (juta) | OVO (juta) | DANA (juta) |
|-------|-------------|-----------|------------|
| 2020 | 38 | 32 | 28 |
| 2021 | 45 | 38 | 35 |
| 2022 | 55 | 44 | 42 |
| 2023 | 62 | 50 | 48 |
| 2024 | 70 | 56 | 55 |

Pastikan grafik memiliki: judul berupa insight (bukan deskripsi), label sumbu, legend, grid, dan minimal satu anotasi pada titik penting.

**Soal 6.** Gunakan seaborn dan dataset `tips` (`sns.load_dataset('tips')`) untuk membuat:
- a) Boxplot distribusi `total_bill` per `day`, dengan warna berbeda berdasarkan `time` (Lunch/Dinner)
- b) Scatter plot `total_bill` vs `tip` dengan warna berdasarkan `size` menggunakan colormap `viridis`
- c) Heatmap korelasi untuk semua kolom numerik

**Soal 7.** Perhatikan kode berikut yang mengandung beberapa masalah visualisasi. Identifikasi minimal 3 masalah dan tulis kode yang sudah diperbaiki.

```python
plt.figure(figsize=(6, 6))
kategori = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
nilai = [23, 22, 21, 20, 19, 18, 17, 16, 15, 14]
plt.pie(nilai, labels=kategori, autopct='%1.1f%%')
plt.title('Data')
plt.show()
```

**Soal 8.** Jelaskan framework data storytelling dari Cole Nussbaumer Knaflic. Kemudian, buatlah narasi singkat (setup-conflict-resolution) berdasarkan data berikut:
- Rata-rata IPK mahasiswa Informatika UAI: 3.2 (2022), 3.3 (2023), 3.4 (2024)
- Rata-rata IPK mahasiswa yang aktif di organisasi: 3.5
- Rata-rata IPK mahasiswa yang tidak aktif: 3.1

### Tingkat Mahir (C3-C4)

**Soal 9.** Buatlah **dashboard mini** (4 subplot, 2x2) dari data kesehatan 200 responden (usia, BMI, tekanan darah, kolesterol, wilayah Kota/Desa). Generate data menggunakan `np.random`. Setiap subplot harus menggunakan jenis chart **berbeda**, judul berupa insight, dan terapkan minimal 3 prinsip Tufte.

**Soal 10.** Buatlah 2 visualisasi berbeda dari data kesenjangan digital Indonesia (DKI Jakarta: penetrasi internet 89%, Papua: 35%, NTT: 38%) menggunakan Python. Tulis narasi data story (setup-conflict-resolution) dan jelaskan pilihan desain berdasarkan prinsip Tufte.

**Soal 11.** Perhatikan dua grafik berikut dan analisis secara kritis:

*Grafik A:* Bar chart 3D dengan 15 kategori, warna pelangi, background bergradien, tanpa label sumbu Y, judul "Data Penjualan".

*Grafik B:* Horizontal bar chart 2D dengan 15 kategori diurutkan dari besar ke kecil, warna abu-abu dengan highlight pada 3 kategori teratas, label nilai di ujung bar, judul "Elektronik Mendominasi 45% Total Penjualan".

- a) Identifikasi pelanggaran prinsip Tufte pada masing-masing grafik
- b) Hitung estimasi data-ink ratio relatif (rendah/sedang/tinggi) untuk masing-masing
- c) Grafik mana yang lebih efektif untuk presentasi bisnis? Jelaskan alasannya.

**Soal 12.** Cari referensi di dokumentasi matplotlib/seaborn, lalu buatlah satu visualisasi kreatif yang belum dibahas di bab ini (misalnya: radar chart, waffle chart, bubble chart, atau subplot mosaic). Gunakan data konteks Indonesia dan jelaskan mengapa jenis chart tersebut tepat.

---

## Referensi

1. Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press.
2. Knaflic, C. N. (2015). *Storytelling with Data: A Data Visualization Guide for Business Professionals*. Wiley.
3. Wilke, C. O. (2019). *Fundamentals of Data Visualization*. O'Reilly Media. https://clauswilke.com/dataviz/
4. Matplotlib Documentation. https://matplotlib.org/stable/
5. Seaborn Documentation. https://seaborn.pydata.org/
6. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media. — Chapter 9: Plotting and Visualization.
7. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media. — Chapter 4: Visualization with Matplotlib.
8. Few, S. (2012). *Show Me the Numbers: Designing Tables and Graphs to Enlighten* (2nd ed.). Analytics Press.
9. BPS. (2024). *Statistik Indonesia 2024*. Badan Pusat Statistik.
10. Google, Temasek, & Bain. (2024). *e-Conomy SEA 2024*. Retrieved from https://economysea.withgoogle.com

---

*Bab berikutnya: **Bab 4 — Probabilitas dan Distribusi***
