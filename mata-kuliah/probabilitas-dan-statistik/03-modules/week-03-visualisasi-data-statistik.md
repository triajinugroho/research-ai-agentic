# Minggu 3: Visualisasi Data Statistik

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 3 |
| **Topik** | Pemilihan grafik, histogram, boxplot, scatter plot, prinsip kejujuran visual |
| **CPL / CPMK** | CPL10 / CPMK102 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Indikator Mingguan** | Memilih dan membuat visualisasi statistik yang sesuai dengan jenis data dan pertanyaan analisis |
| **Level Bloom** | C3 (Menerapkan) |
| **Durasi** | 150 menit tatap muka |
| **Metode** | Kuliah, studio visualisasi, kritik grafik |

---

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Memilih** (C3) jenis grafik yang sesuai berdasarkan jenis data dan pertanyaan analisis.
2. **Membuat** (C3) histogram, boxplot, scatter plot, dan bar chart dengan matplotlib dan seaborn.
3. **Menentukan** (C3) lebar bin histogram yang wajar dan menjelaskan dampaknya terhadap kesan sebaran.
4. **Menganalisis** (C4) sebuah grafik untuk mendeteksi teknik penyajian yang menyesatkan.
5. **Menerapkan** (C3) prinsip kejujuran visual pada grafik yang dibuat sendiri.

---

## Materi Pembelajaran

### 1. Mengapa Visualisasi Bukan Hiasan

#### 1.1 Kuartet Anscombe

Empat kumpulan data berikut memiliki **statistik deskriptif yang nyaris identik**: mean x, mean y, varians, korelasi, dan garis regresi semuanya sama.

| Statistik | Dataset I | II | III | IV |
|-----------|-----------|-----|-----|-----|
| Mean x | 9,0 | 9,0 | 9,0 | 9,0 |
| Mean y | 7,50 | 7,50 | 7,50 | 7,50 |
| Korelasi | 0,816 | 0,816 | 0,816 | 0,817 |
| Garis regresi | y = 3 + 0,5x | sama | sama | sama |

Tetapi bentuknya sama sekali berbeda:

```
    I: linear wajar      II: melengkung        III: linear + 1 pencilan   IV: satu titik ekstrem
        ·  ·                   ·····                    ·                        ·
      ·  ·                   ··     ··                ·                          │
    ·  ·                   ·          ·             ·                            │
   ·  ·                  ·                        ·                     ········ ┘
```

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Kuartet Anscombe tersedia langsung di seaborn
anscombe = sns.load_dataset("anscombe")

# Verifikasi bahwa statistiknya nyaris sama
print(anscombe.groupby("dataset").agg(
    mean_x=("x", "mean"), mean_y=("y", "mean"),
    std_x=("x", "std"), std_y=("y", "std")
).round(3))

# Tetapi bentuknya sangat berbeda
sns.lmplot(data=anscombe, x="x", y="y", col="dataset",
           col_wrap=2, height=3, ci=None,
           scatter_kws={"s": 60, "alpha": 0.8})
plt.suptitle("Kuartet Anscombe: statistik sama, bentuk berbeda", y=1.02)
plt.show()
```

> **Pelajarannya:** statistik ringkasan **tidak pernah cukup**. Selalu lihat datanya. Dalam alur kerja profesional, visualisasi dilakukan **sebelum** analisis inferensial, bukan sesudahnya sebagai pemanis laporan.

---

### 2. Memilih Grafik yang Tepat

#### 2.1 Pohon Keputusan

```
  Berapa variabel yang ingin ditampilkan?
  │
  ├── SATU variabel
  │   ├── Kategorikal  → bar chart (bukan pie chart)
  │   └── Numerik      → histogram, boxplot, atau density plot
  │
  ├── DUA variabel
  │   ├── Numerik × Numerik        → scatter plot
  │   ├── Kategorikal × Numerik    → boxplot / violin plot berkelompok
  │   └── Kategorikal × Kategorikal → bar chart bertumpuk / heatmap
  │
  └── TIGA ATAU LEBIH
      ├── Tambah dimensi warna, ukuran, atau bentuk
      ├── Pecah menjadi panel kecil (facet)
      └── Matriks korelasi (heatmap)
```

#### 2.2 Tabel Rujukan Cepat

| Pertanyaan Analisis | Grafik | Catatan |
|---------------------|--------|---------|
| Bagaimana bentuk sebaran? | Histogram | Perhatikan lebar bin |
| Apakah ada pencilan? | Boxplot | Aturan 1,5×IQR terbaca langsung |
| Bagaimana perbandingan antar kelompok? | Boxplot berkelompok / violin plot | Boxplot menyembunyikan bimodalitas; violin tidak |
| Adakah hubungan antara dua besaran? | Scatter plot | Tambah garis tren bila perlu |
| Bagaimana tren sepanjang waktu? | Line chart | Sumbu waktu selalu horizontal |
| Berapa besar tiap kategori? | Bar chart | Urutkan dari besar ke kecil bila kategori nominal |
| Bagaimana korelasi antar banyak variabel? | Heatmap korelasi | Gunakan skema warna divergen |

---

### 3. Histogram

#### 3.1 Anatomi dan Lebar Bin

Histogram membagi rentang data menjadi selang (*bin*) dan menghitung frekuensi tiap selang. **Pilihan lebar bin mengubah kesan yang ditangkap pembaca.**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
# Data bimodal: dua kelompok tercampur
data = np.concatenate([
    np.random.normal(65, 8, 300),    # kelompok nilai rendah
    np.random.normal(85, 6, 200),    # kelompok nilai tinggi
])

fig, axes = plt.subplots(1, 4, figsize=(18, 4))
for ax, bins in zip(axes, [5, 15, 40, 150]):
    ax.hist(data, bins=bins, color="steelblue", edgecolor="white")
    ax.set_title(f"bins = {bins}")
    ax.set_xlabel("Nilai")
axes[0].set_ylabel("Frekuensi")
plt.suptitle("Lebar bin mengubah cerita yang tampak", y=1.03)
plt.tight_layout()
plt.show()
```

Apa yang terjadi:

| bins | Yang tampak | Masalah |
|------|-------------|---------|
| 5 | Satu gundukan tunggal | **Menyembunyikan** bahwa ada dua kelompok |
| 15 | Dua puncak mulai terlihat | Wajar |
| 40 | Dua puncak jelas | Wajar |
| 150 | Bergerigi dan berisik | Derap acak terbaca sebagai pola |

#### 3.2 Aturan Penentuan Bin

```python
def saran_jumlah_bin(data):
    """Menghitung saran jumlah bin dengan tiga aturan umum."""
    n = len(data)
    # Aturan Sturges: baik untuk data kecil dan hampir normal
    sturges = int(np.ceil(np.log2(n) + 1))
    # Aturan akar: sederhana, sering dipakai perangkat lunak
    akar = int(np.ceil(np.sqrt(n)))
    # Aturan Freedman-Diaconis: robust, berbasis IQR
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    lebar_fd = 2 * iqr / (n ** (1/3))
    fd = int(np.ceil((data.max() - data.min()) / lebar_fd)) if lebar_fd > 0 else akar

    print(f"n = {n}")
    print(f"  Sturges           : {sturges} bin")
    print(f"  Akar kuadrat      : {akar} bin")
    print(f"  Freedman-Diaconis : {fd} bin  (paling tahan pencilan)")
    return fd

saran_jumlah_bin(data)
```

> **Praktik yang dianjurkan:** coba beberapa lebar bin, lalu pilih yang paling jujur menggambarkan data — bukan yang paling mendukung kesimpulan yang Anda inginkan. Menyebutkan jumlah bin yang dipakai dalam laporan adalah bagian dari transparansi.

---

### 4. Boxplot dan Violin Plot

#### 4.1 Membaca Boxplot

```
                    pencilan
                       ●
                       │
        ┌──────────────┤  ← batas atas (Q3 + 1,5×IQR)
        │              │
        │   ┌──────┐   │  ← Q3
        │   │──────│   │  ← median (Q2)
        │   └──────┘   │  ← Q1
        │              │
        └──────────────┤  ← batas bawah (Q1 − 1,5×IQR)
```

Boxplot menampilkan lima angka sekaligus (min wajar, Q1, median, Q3, maks wajar) plus pencilan — dan memungkinkan perbandingan banyak kelompok dalam satu gambar.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("nilai_mahasiswa_if.csv")

plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x="asal_sekolah", y="jam_belajar", palette="Set2")
plt.title("Jam belajar per minggu menurut asal sekolah")
plt.xlabel("Asal sekolah")
plt.ylabel("Jam belajar per minggu")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
```

#### 4.2 Keterbatasan Boxplot: Bimodalitas Tersembunyi

Boxplot hanya menampilkan ringkasan lima angka. Dua sebaran yang sangat berbeda bisa menghasilkan boxplot yang mirip.

```python
np.random.seed(0)
# Sebaran A: satu gundukan
a = np.random.normal(70, 12, 500)
# Sebaran B: dua gundukan, tetapi ringkasan lima angkanya mirip
b = np.concatenate([np.random.normal(55, 5, 250), np.random.normal(85, 5, 250)])

fig, axes = plt.subplots(1, 2, figsize=(13, 4))

# Boxplot: terlihat mirip
axes[0].boxplot([a, b], labels=["Sebaran A", "Sebaran B"])
axes[0].set_title("Boxplot: tampak serupa")

# Violin plot: perbedaannya terlihat
sns.violinplot(data=[a, b], ax=axes[1], palette="Set2")
axes[1].set_xticklabels(["Sebaran A", "Sebaran B"])
axes[1].set_title("Violin plot: bimodalitas B terungkap")

plt.tight_layout()
plt.show()
```

> **Kapan memakai violin plot:** ketika Anda menduga sebaran tidak bergundukan tunggal, atau ketika jumlah data memadai (≥ 50 per kelompok). Untuk data kecil, boxplot atau bahkan *strip plot* (menampilkan tiap titik) lebih jujur.

---

### 5. Scatter Plot

```python
plt.figure(figsize=(9, 6))
sns.scatterplot(data=df, x="jam_belajar", y="nilai_uas",
                hue="asal_sekolah", style="kelas", s=70, alpha=0.75)
plt.title("Hubungan jam belajar dan nilai UAS")
plt.xlabel("Jam belajar per minggu")
plt.ylabel("Nilai UAS")
plt.legend(title="Asal sekolah", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.show()
```

Yang dicari pada scatter plot:

| Ciri | Artinya |
|------|---------|
| Pola naik/turun | Ada hubungan (Minggu 14) |
| Pola melengkung | Hubungan tidak linear — regresi linear tidak cocok |
| Titik menyebar acak | Tidak ada hubungan linear |
| Kelompok terpisah | Mungkin ada subpopulasi |
| Titik jauh terpisah | Kandidat pencilan |
| Corong melebar | Ragam tidak homogen — penting untuk Minggu 14 |

> **Ingat selalu:** pola pada scatter plot menunjukkan **asosiasi**, bukan **sebab-akibat**. Kita akan membahas ini secara khusus di Minggu 14.

---

### 6. Prinsip Kejujuran Visual

#### 6.1 Empat Teknik Menyesatkan yang Paling Sering Dipakai

**(a) Sumbu vertikal tidak dimulai dari nol pada bar chart**

```python
kategori = ["Produk A", "Produk B"]
nilai = [98, 100]

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# MENYESATKAN: sumbu dimulai dari 97
axes[0].bar(kategori, nilai, color=["#c0392b", "#27ae60"])
axes[0].set_ylim(97, 101)
axes[0].set_title("MENYESATKAN\nB tampak 3x lebih baik")

# JUJUR: sumbu dimulai dari 0
axes[1].bar(kategori, nilai, color=["#c0392b", "#27ae60"])
axes[1].set_ylim(0, 110)
axes[1].set_title("JUJUR\nselisihnya sebenarnya 2%")

plt.tight_layout()
plt.show()
```

> **Aturan:** bar chart **wajib** dimulai dari nol, karena panjang batang adalah representasi nilai. Line chart untuk tren **boleh** tidak dari nol, asal skalanya dicantumkan jelas.

**(b) Skala ganda yang memaksakan kesan hubungan**

Dua sumbu-y dengan skala berbeda dapat membuat dua deret apa pun tampak "berkorelasi". Hindari, kecuali benar-benar perlu dan dijelaskan.

**(c) Memotong rentang data**

Menampilkan hanya bagian data yang mendukung argumen. Selalu tampilkan rentang penuh atau nyatakan secara jelas bahwa data dipotong.

**(d) Pie chart dengan banyak irisan**

Mata manusia buruk dalam membandingkan sudut. Pie chart dengan lebih dari 4–5 irisan sulit dibaca.

```python
bahasa = ["Python", "Java", "JavaScript", "C++", "Go", "Rust", "PHP"]
jumlah = [145, 98, 112, 67, 34, 28, 45]

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

axes[0].pie(jumlah, labels=bahasa, autopct="%1.1f%%", startangle=90)
axes[0].set_title("Pie chart: sulit membandingkan Go, Rust, PHP")

urut = sorted(zip(jumlah, bahasa), reverse=True)
axes[1].barh([b for _, b in urut][::-1], [j for j, _ in urut][::-1],
             color="steelblue")
axes[1].set_title("Bar chart: perbandingan langsung terbaca")
axes[1].set_xlabel("Jumlah pengguna")

plt.tight_layout()
plt.show()
```

#### 6.2 Daftar Periksa Grafik yang Jujur

Sebelum memasukkan grafik ke laporan, periksa:

- [ ] Judul menjelaskan **apa** yang ditampilkan, bukan sekadar nama variabel.
- [ ] Kedua sumbu diberi label lengkap **beserta satuannya**.
- [ ] Sumbu-y bar chart dimulai dari nol.
- [ ] Jumlah bin histogram disebutkan atau wajar.
- [ ] Sumber data dicantumkan.
- [ ] Ukuran sampel (n) terlihat.
- [ ] Warna masih terbaca bila dicetak hitam-putih atau oleh pembaca buta warna.
- [ ] Tidak ada elemen dekoratif yang tidak membawa informasi (bayangan, efek 3D).
- [ ] Skala tidak dipotong tanpa penjelasan.

```python
# Template grafik yang memenuhi daftar periksa
fig, ax = plt.subplots(figsize=(9, 5.5))

ax.hist(df["nilai_uas"], bins=20, color="steelblue",
        edgecolor="white", alpha=0.85)

ax.set_title("Sebaran Nilai UAS Probabilitas dan Statistik\n"
             "Prodi Informatika UAI, Semester Ganjil 2026/2027",
             fontsize=12, pad=12)
ax.set_xlabel("Nilai UAS (skala 0–100)")
ax.set_ylabel("Jumlah mahasiswa")

# Menambahkan garis median sebagai acuan
median = df["nilai_uas"].median()
ax.axvline(median, color="#c0392b", linestyle="--", linewidth=1.8,
           label=f"Median = {median:.1f}")
ax.legend()

# Keterangan sumber dan ukuran sampel
ax.text(0.99, -0.14, f"n = {len(df)} mahasiswa · Sumber: data kelas IF26A dan IF26H",
        transform=ax.transAxes, ha="right", fontsize=8, color="gray")

plt.tight_layout()
plt.show()
```

---

## Kegiatan Pembelajaran

### Sebelum Kelas (Mandiri — 60 menit)

1. Membaca [Bab 3 buku ajar](../06-buku-ajar/bab-03-visualisasi-data-statistik.md).
2. **Mencari satu grafik menyesatkan** dari media daring Indonesia (berita, media sosial, laporan perusahaan). Simpan tangkapan layarnya.
3. Menuliskan dugaan: teknik menyesatkan apa yang dipakai?

### Di Kelas (150 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–15' | Kuartet Anscombe: mengapa statistik saja tidak cukup |
| 15–40' | Kuliah: pohon keputusan pemilihan grafik; histogram dan lebar bin |
| 40–60' | **Studio:** membuat histogram dengan 4 lebar bin berbeda, mendiskusikan mana yang jujur |
| 60–70' | Istirahat |
| 70–95' | Kuliah: boxplot, violin plot, scatter plot, dan apa yang harus dicari |
| 95–120' | **Kritik grafik:** mahasiswa mempresentasikan grafik menyesatkan yang ditemukannya |
| 120–145' | Studio: memperbaiki satu grafik menyesatkan menjadi jujur |
| 145–150' | **Kuis 1** dibagikan (Minggu 1–3) — dikerjakan 20 menit terakhir |

> **Catatan jadwal:** Kuis 1 dilaksanakan pada pertemuan ini, mencakup materi Minggu 1–3. Bobot 3,75% dari nilai akhir, menelusuri ke `PS-Sub-CPMK081-1`.

#### Kritik Grafik: Panduan Presentasi

Setiap mahasiswa menyampaikan dalam 2 menit:
1. Tampilkan grafiknya.
2. Sebutkan teknik menyesatkan yang dipakai.
3. Jelaskan kesan salah apa yang ditimbulkan.
4. Usulkan perbaikannya.

### Setelah Kelas (Mandiri — 180 menit)

1. Mengerjakan [Lab 03](../04-labs/lab-03-studio-visualisasi-statistik.md).
2. Mengerjakan Latihan Soal Bab 3.
3. **Mulai menyusun proposal proyek** — batas waktu Minggu 6.

---

## Penugasan

| Kode | Tugas | Bobot | Batas Waktu |
|------|-------|-------|-------------|
| T-03 | Laporan Lab 03 — Studio visualisasi statistik | 1,92% | Sebelum kelas Minggu 4 |
| K-01 | Kuis 1 — Minggu 1–3 | 3,75% | Di kelas Minggu 3 |

---

## Rangkuman

1. **Kuartet Anscombe** membuktikan bahwa statistik ringkasan tidak pernah cukup — selalu lihat datanya lebih dulu.
2. Pemilihan grafik ditentukan oleh **jenis data** dan **pertanyaan analisis**, bukan oleh selera.
3. **Lebar bin histogram mengubah cerita.** Bin terlalu sedikit menyembunyikan struktur; terlalu banyak menampilkan derap sebagai pola. Aturan Freedman-Diaconis paling tahan pencilan.
4. **Boxplot** efisien untuk membandingkan banyak kelompok, tetapi **menyembunyikan bimodalitas**. Violin plot mengungkapnya.
5. **Scatter plot** menunjukkan asosiasi, bukan sebab-akibat. Pola melengkung dan corong melebar adalah peringatan dini untuk analisis regresi.
6. Empat teknik menyesatkan yang paling umum: sumbu tidak dari nol, skala ganda, pemotongan rentang, dan pie chart beririsan banyak.
7. **Bar chart wajib dimulai dari nol.** Panjang batang adalah representasi nilai.
8. Grafik yang jujur menyebutkan **sumber data dan ukuran sampel** — ini bagian dari amanah dalam pelaporan.

---

## Referensi

1. Anscombe, F. J. (1973). Graphs in Statistical Analysis. *The American Statistician*, 27(1), 17–21.
2. Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.), Bab 2. Graphics Press.
3. Cairo, A. (2019). *How Charts Lie: Getting Smarter about Visual Information*. W. W. Norton.
4. Freedman, D., & Diaconis, P. (1981). On the histogram as a density estimator. *Probability Theory and Related Fields*, 57(4), 453–476.
5. Dokumentasi seaborn — <https://seaborn.pydata.org/tutorial.html>
6. Dokumentasi matplotlib — <https://matplotlib.org/stable/tutorials/index.html>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
