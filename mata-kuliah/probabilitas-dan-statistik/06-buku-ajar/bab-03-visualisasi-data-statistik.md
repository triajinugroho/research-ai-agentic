# BAB 3: VISUALISASI DATA STATISTIK

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `PS-Sub-CPMK102-1` | Memilih jenis grafik berdasarkan jenis data dan pertanyaan analisis | C3 |
| `PS-Sub-CPMK102-1` | Membuat visualisasi statistik dengan matplotlib dan seaborn | C3 |
| `PS-Sub-CPMK102-1` | Menganalisis grafik untuk mendeteksi teknik penyajian yang menyesatkan | C4 |

---

## 3.1 Kuartet Anscombe: Bukti bahwa Angka Tidak Cukup

Pada 1973, Francis Anscombe menyusun empat kumpulan data yang memiliki **statistik ringkasan nyaris identik**:

| Statistik | Dataset I | II | III | IV |
|-----------|-----------|-----|-----|-----|
| Mean x | 9,0 | 9,0 | 9,0 | 9,0 |
| Varians x | 11,0 | 11,0 | 11,0 | 11,0 |
| Mean y | 7,50 | 7,50 | 7,50 | 7,50 |
| Varians y | 4,12 | 4,13 | 4,12 | 4,12 |
| Korelasi | 0,816 | 0,816 | 0,816 | 0,817 |
| Garis regresi | y = 3 + 0,5x | sama | sama | sama |

Seorang analis yang hanya melihat tabel itu akan menyimpulkan keempatnya "pada dasarnya sama". Tetapi bentuknya:

```
   I: linear wajar       II: melengkung         III: linear + 1 pencilan   IV: satu titik ekstrem
       ·  ·                    ·····                    ·                          ·
     ·  ·                   ··     ··                 ·                            │
   ·  ·                   ·           ·             ·                              │
  ·  ·                  ·                         ·                       ········ ┘
```

- **Dataset I** — hubungan linear yang wajar. Model regresi tepat.
- **Dataset II** — hubungan melengkung. Regresi linear salah model.
- **Dataset III** — linear sempurna kecuali satu pencilan yang menarik garisnya.
- **Dataset IV** — sepuluh titik pada x yang sama, satu titik ekstrem yang menentukan seluruh garis.

```python
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

anscombe = sns.load_dataset("anscombe")

# Buktikan statistiknya nyaris identik
ringkas = anscombe.groupby("dataset").agg(
    mean_x=("x", "mean"), mean_y=("y", "mean"),
    std_x=("x", "std"), std_y=("y", "std"),
).round(3)
ringkas["korelasi"] = anscombe.groupby("dataset").apply(
    lambda g: stats.pearsonr(g["x"], g["y"])[0]
).round(3)
print(ringkas)

sns.lmplot(data=anscombe, x="x", y="y", col="dataset", col_wrap=2,
           height=3, ci=None, scatter_kws={"s": 60, "alpha": 0.8})
plt.suptitle("Kuartet Anscombe: statistik sama, bentuk berbeda", y=1.02)
plt.show()
```

> **Pelajaran yang harus dipegang seumur karier:** statistik ringkasan tidak pernah cukup. **Selalu lihat datanya.**
>
> Dalam alur kerja profesional, visualisasi dilakukan **sebelum** analisis inferensial — bukan sesudahnya sebagai pemanis laporan.

**Pengembangan modern.** Pada 2017, Matejka dan Fitzmaurice membuat *Datasaurus Dozen*: tiga belas kumpulan data dengan statistik identik sampai dua desimal, salah satunya membentuk gambar dinosaurus. Argumennya sama, dengan bukti yang lebih dramatis.

---

## 3.2 Memilih Grafik yang Tepat

### 3.2.1 Pohon Keputusan

```
  Berapa variabel yang ingin ditampilkan?
  │
  ├── SATU variabel
  │   ├── Kategorikal  → bar chart  (bukan pie chart)
  │   └── Numerik      → histogram, boxplot, atau density plot
  │
  ├── DUA variabel
  │   ├── Numerik × Numerik         → scatter plot
  │   ├── Kategorikal × Numerik     → boxplot / violin plot berkelompok
  │   └── Kategorikal × Kategorikal → bar chart bertumpuk / heatmap
  │
  └── TIGA ATAU LEBIH
      ├── Tambahkan dimensi warna, ukuran, atau bentuk
      ├── Pecah menjadi panel kecil (facet)
      └── Matriks korelasi (heatmap)
```

### 3.2.2 Tabel Rujukan Cepat

| Pertanyaan Analisis | Grafik | Yang harus diperhatikan |
|---------------------|--------|-------------------------|
| Bagaimana bentuk sebaran? | Histogram | Lebar bin |
| Adakah pencilan? | Boxplot | Aturan 1,5×IQR terbaca langsung |
| Bagaimana perbandingan antar kelompok? | Boxplot / violin berkelompok | Boxplot menyembunyikan bimodalitas |
| Adakah hubungan dua besaran? | Scatter plot | Pola melengkung dan corong |
| Bagaimana tren sepanjang waktu? | Line chart | Sumbu waktu selalu horizontal |
| Berapa besar tiap kategori? | Bar chart | Urutkan; mulai dari nol |
| Bagaimana korelasi antar banyak variabel? | Heatmap korelasi | Skema warna divergen |

---

## 3.3 Histogram

### 3.3.1 Lebar Bin Mengubah Cerita

Histogram membagi rentang data menjadi selang (*bin*) dan menghitung frekuensinya. **Pilihan lebar bin mengubah kesan yang ditangkap pembaca** — dan inilah titik di mana kejujuran visual paling mudah dilanggar.

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
data = np.concatenate([
    rng.normal(62, 7, 320),     # kelompok nilai rendah
    rng.normal(84, 6, 220),     # kelompok nilai tinggi
])

fig, axes = plt.subplots(1, 4, figsize=(18, 4))
for ax, bins in zip(axes, [4, 12, 35, 140]):
    ax.hist(data, bins=bins, color="steelblue", edgecolor="white")
    ax.set_title(f"bins = {bins}")
    ax.set_xlabel("Nilai")
axes[0].set_ylabel("Frekuensi")
plt.suptitle("Data yang SAMA, kesan yang BERBEDA", y=1.04)
plt.tight_layout()
plt.show()
```

| bins | Yang tampak | Masalahnya |
|------|-------------|------------|
| 4 | Satu gundukan tunggal | **Menyembunyikan** bahwa ada dua kelompok |
| 12 | Dua puncak mulai terlihat | Wajar |
| 35 | Dua puncak jelas | Wajar |
| 140 | Bergerigi dan berisik | Derap acak terbaca sebagai pola |

> **Implikasi etis:** bila Anda ingin menyembunyikan fakta bahwa ada dua kelompok berbeda dalam data — misalnya dua kelompok mahasiswa dengan capaian sangat berbeda — cukup pilih bin yang sedikit. Tidak ada angka yang dipalsukan. Tetapi pembaca tetap tertipu.
>
> Karena itu **menyebutkan jumlah bin yang dipakai** adalah bagian dari transparansi.

### 3.3.2 Aturan Penentuan Bin

| Aturan | Rumus | Kapan dipakai |
|--------|-------|---------------|
| Sturges | ⌈log₂(n) + 1⌉ | Data kecil dan hampir Normal |
| Akar kuadrat | ⌈√n⌉ | Sederhana, bawaan banyak perangkat lunak |
| **Freedman-Diaconis** | lebar = 2·IQR / n^(1/3) | **Paling tahan pencilan** — dianjurkan |

```python
def saran_bin(data):
    """Tiga aturan penentuan jumlah bin."""
    n = len(data)
    sturges = int(np.ceil(np.log2(n) + 1))
    akar = int(np.ceil(np.sqrt(n)))
    q1, q3 = np.percentile(data, [25, 75])
    lebar_fd = 2 * (q3 - q1) / (n ** (1/3))
    fd = int(np.ceil((data.max() - data.min()) / lebar_fd)) if lebar_fd > 0 else akar
    print(f"n = {n}")
    print(f"  Sturges           : {sturges}")
    print(f"  Akar kuadrat      : {akar}")
    print(f"  Freedman-Diaconis : {fd}  ← dianjurkan")
    return fd

saran_bin(data)
```

---

## 3.4 Boxplot dan Violin Plot

### 3.4.1 Membaca Boxplot

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

Boxplot menampilkan lima angka ringkasan sekaligus plus pencilan, dan memungkinkan perbandingan banyak kelompok dalam satu gambar. Ia sangat efisien.

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

### 3.4.2 Keterbatasan Boxplot: Bimodalitas Tersembunyi

Boxplot hanya menampilkan lima angka. **Dua sebaran yang sangat berbeda dapat menghasilkan boxplot yang nyaris sama.**

```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
a = rng.normal(70, 12, 500)                                      # satu gundukan
b = np.concatenate([rng.normal(55, 5, 250),
                    rng.normal(85, 5, 250)])                     # dua gundukan

fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

axes[0].boxplot([a, b], labels=["A", "B"])
axes[0].set_title("Boxplot — tampak serupa")

sns.violinplot(data=[a, b], ax=axes[1], palette="Set2")
axes[1].set_xticklabels(["A", "B"])
axes[1].set_title("Violin — bimodalitas B terungkap")

axes[2].hist(a, bins=30, alpha=0.6, label="A", color="steelblue")
axes[2].hist(b, bins=30, alpha=0.6, label="B", color="#e67e22")
axes[2].legend()
axes[2].set_title("Histogram — paling jelas")

plt.tight_layout()
plt.show()
```

| Grafik | Kapan dipakai |
|--------|---------------|
| **Boxplot** | Membandingkan banyak kelompok; data cukup; sebaran diduga bergundukan tunggal |
| **Violin plot** | Menduga sebaran tidak bergundukan tunggal; n ≥ 50 per kelompok |
| **Strip plot / swarm plot** | n kecil (< 30); menampilkan setiap titik data secara jujur |
| **Histogram** | Satu kelompok, ingin melihat bentuk sedetail mungkin |

---

## 3.5 Scatter Plot

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

### Yang Harus Dicari pada Scatter Plot

| Ciri | Artinya | Dibahas di |
|------|---------|------------|
| Pola naik/turun | Ada hubungan linear | Bab 13 |
| Pola melengkung | Hubungan tidak linear — regresi linear tidak cocok | Bab 13 |
| Titik menyebar acak | Tidak ada hubungan linear | Bab 13 |
| Kelompok terpisah | Mungkin ada subpopulasi | Bab 2 |
| Titik jauh terpisah | Kandidat pencilan | Bab 2 |
| **Corong melebar** | Ragam tidak homogen — melanggar asumsi regresi | Bab 13 |

> **Ingat selalu:** pola pada scatter plot menunjukkan **asosiasi**, bukan **sebab-akibat**. Bab 13 membahas ini secara khusus.

---

## 3.6 Kejujuran Visual

### 3.6.1 Empat Teknik Menyesatkan yang Paling Umum

#### (a) Sumbu vertikal tidak dimulai dari nol pada bar chart

```python
kategori, nilai = ["Produk A", "Produk B"], [98, 100]

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].bar(kategori, nilai, color=["#c0392b", "#27ae60"])
axes[0].set_ylim(97, 101)
axes[0].set_title("MENYESATKAN\nB tampak 3× lebih baik")

axes[1].bar(kategori, nilai, color=["#c0392b", "#27ae60"])
axes[1].set_ylim(0, 110)
axes[1].set_title("JUJUR\nselisih sebenarnya 2%")
plt.tight_layout(); plt.show()
```

> **Aturan:** bar chart **wajib** dimulai dari nol, karena **panjang batang adalah representasi nilai**. Memotong sumbu berarti memalsukan perbandingan panjang.
>
> Line chart untuk tren **boleh** tidak dimulai dari nol — karena yang dibaca adalah kemiringan, bukan panjang — asalkan skalanya jelas tercantum.

#### (b) Skala ganda yang memaksakan kesan hubungan

Dua sumbu-y dengan skala berbeda dapat membuat dua deret apa pun tampak "berkorelasi". Dengan mengatur skalanya, penjualan es krim dapat dibuat tampak mengikuti angka kriminalitas.

Hindari, kecuali benar-benar perlu, dan selalu jelaskan skalanya.

#### (c) Memotong rentang data

Menampilkan hanya bagian data yang mendukung argumen. Misalnya menampilkan tren tiga bulan terakhir yang naik, padahal tren setahun menurun.

#### (d) Pie chart dengan banyak irisan

Mata manusia buruk dalam membandingkan sudut, tetapi baik dalam membandingkan panjang. Pie chart dengan lebih dari 4–5 irisan sulit dibaca.

```python
bahasa = ["Python", "JavaScript", "Java", "C++", "PHP", "Go", "Rust"]
jumlah = [145, 112, 98, 67, 45, 34, 28]

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
axes[0].pie(jumlah, labels=bahasa, autopct="%1.1f%%", startangle=90)
axes[0].set_title("SULIT: bandingkan Go, Rust, PHP")

urut = sorted(zip(jumlah, bahasa))
axes[1].barh([b for _, b in urut], [j for j, _ in urut], color="steelblue")
axes[1].set_title("MUDAH: perbandingan langsung")
axes[1].set_xlabel("Jumlah pengguna")
plt.tight_layout(); plt.show()
```

### 3.6.2 Daftar Periksa Grafik yang Jujur

Sebelum memasukkan grafik ke laporan:

- [ ] Judul menjelaskan **apa** yang ditampilkan, bukan sekadar nama variabel
- [ ] Kedua sumbu berlabel lengkap **beserta satuannya**
- [ ] Sumbu-y bar chart dimulai dari nol
- [ ] Jumlah bin histogram disebutkan atau wajar
- [ ] **Sumber data dicantumkan**
- [ ] **Ukuran sampel (n) terlihat**
- [ ] Warna terbaca dalam hitam-putih dan oleh pembaca buta warna
- [ ] Tidak ada elemen dekoratif tanpa informasi (bayangan, efek 3D)
- [ ] Skala tidak dipotong tanpa penjelasan

### 3.6.3 Template Grafik yang Memenuhi Daftar Periksa

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))

n_bin = 20
ax.hist(df["nilai_uas"], bins=n_bin, color="steelblue",
        edgecolor="white", alpha=0.85)

med = df["nilai_uas"].median()
ax.axvline(med, color="#c0392b", linestyle="--", linewidth=2,
           label=f"Median = {med:.1f}")

ax.set_title("Sebaran Nilai UAS Probabilitas dan Statistik\n"
             "Prodi Informatika UAI, Semester Ganjil 2026/2027",
             fontsize=12, pad=12)
ax.set_xlabel("Nilai UAS (skala 0–100)")
ax.set_ylabel("Jumlah mahasiswa")
ax.legend()

ax.text(0.99, -0.13,
        f"n = {len(df)} mahasiswa · {n_bin} bin · Sumber: kelas IF26A dan IF26H",
        transform=ax.transAxes, ha="right", fontsize=8, color="gray")

plt.tight_layout()
plt.show()
```

### 3.6.4 Rasio Tinta-Data

Edward Tufte memperkenalkan gagasan ***data-ink ratio***: proporsi tinta yang benar-benar membawa informasi dibanding total tinta pada grafik.

> **Prinsipnya:** maksimalkan tinta-data, minimalkan tinta-hias.

| Buang | Alasan |
|-------|--------|
| Efek 3D pada bar chart | Membuat perbandingan panjang menjadi sulit |
| Bayangan dan gradien | Tidak membawa informasi |
| Garis kisi yang tebal | Bersaing dengan data |
| Bingkai ganda | Tidak perlu |
| Legenda untuk satu seri | Cukup ditulis di judul |

---

## AI Corner — Tingkat Dasar

### AI dan Visualisasi: Kuat pada Sintaksis, Lemah pada Pilihan

AI sangat membantu menuliskan kode matplotlib dan seaborn. Sintaksis kedua pustaka itu rumit dan mudah lupa; meminta bantuan AI untuk itu **wajar dan diizinkan** (dengan pencatatan di AI Usage Log).

Tetapi perhatikan apa yang **tidak** bisa dilakukan AI:

| AI bisa | AI tidak bisa |
|---------|---------------|
| Menulis kode histogram | Mengetahui bahwa data Anda bimodal sehingga bin kecil menyesatkan |
| Membuat boxplot berkelompok | Menilai apakah boxplot menyembunyikan sesuatu pada data Anda |
| Memilih palet warna | Mengetahui bahwa pembaca laporan Anda akan mencetaknya hitam-putih |
| Membuat grafik yang rapi | Menilai apakah grafik itu **jujur** untuk kesimpulan yang Anda tarik |

### Percobaan

Berikan sebuah AI data bimodal dan mintalah histogram, tanpa menyebutkan bahwa datanya bimodal:

> *"Buatkan histogram untuk data ini: [data bimodal]"*

Perhatikan berapa bin yang dipilihnya. Sebagian besar akan memakai nilai bawaan (10 bin pada matplotlib) — yang mungkin **menyembunyikan bimodalitas**.

Lalu tanyakan:

> *"Apakah jumlah bin yang kamu pilih menyembunyikan struktur dalam data ini?"*

Sekarang ia akan memeriksa dan mungkin merevisi. **Informasi itu ada dalam modelnya — tetapi tidak muncul sampai Anda tahu harus menanyakannya.**

### Pemakaian yang Dianjurkan

```
PROMPT YANG BAIK:
"Saya punya data waktu respons yang menceng kanan (skewness 2,3) dengan
 beberapa pencilan ekstrem. Saya ingin menampilkan sebarannya secara jujur
 kepada manajemen. Grafik apa yang Anda sarankan, dan apa kelebihan-kekurangan
 masing-masing pilihan?"

Mengapa baik: Anda sudah memeriksa datanya sendiri, sudah tahu bentuknya,
dan meminta pertimbangan — bukan jawaban jadi.
```

---

## Latihan Soal

### Tingkat Dasar

1. Untuk setiap pertanyaan analisis, tentukan grafik yang paling tepat:
   (a) Bagaimana sebaran nilai UAS?
   (b) Apakah jam belajar berbeda antar asal sekolah?
   (c) Adakah hubungan antara jam belajar dan nilai?
   (d) Berapa proporsi mahasiswa dari tiap asal sekolah?
   (e) Bagaimana tren jumlah pengguna sepanjang 12 bulan?

2. Sebutkan lima unsur wajib sebuah grafik yang jujur.

3. Jelaskan apa yang ditampilkan boxplot: sebutkan kelima angka ringkasannya dan bagaimana pencilan ditandai.

4. Mengapa bar chart wajib dimulai dari nol, sedangkan line chart boleh tidak?

5. Sebutkan dua kelemahan pie chart dibanding bar chart.

### Tingkat Menengah

6. Sebuah histogram dibuat dengan 5 bin dan tampak bergundukan tunggal. Dengan 30 bin, tampak dua gundukan.
   (a) Mana yang menggambarkan data dengan lebih jujur?
   (b) Bagaimana cara memutuskannya secara objektif?
   (c) Hitung saran Freedman-Diaconis bila n = 540, IQR = 18, rentang = 62.

7. Jelaskan mengapa boxplot dapat menyembunyikan bimodalitas. Rancang sebuah contoh data (boleh dalam bentuk kode pembangkit) yang mendemonstrasikannya.

8. Temukan satu grafik dari media daring Indonesia yang menurut Anda menyesatkan.
   (a) Identifikasi teknik yang dipakai.
   (b) Jelaskan kesan salah yang ditimbulkannya.
   (c) Buat ulang grafik itu secara jujur dengan matplotlib.
   (d) Bandingkan kesan yang ditimbulkan kedua versi.

9. Sebuah grafik menampilkan pertumbuhan pengguna aplikasi dari 10.200 menjadi 10.450 dalam setahun, dengan sumbu-y dimulai dari 10.150.
   (a) Berapa persen pertumbuhan sebenarnya?
   (b) Bagaimana kesan yang ditimbulkan grafik itu?
   (c) Apakah ini kebohongan atau penyesatan? Jelaskan perbedaannya.
   (d) Bagaimana seharusnya grafik itu dibuat?

### Tingkat Mahir

10. Kuartet Anscombe menunjukkan empat pola berbeda dengan statistik identik.
    (a) Untuk masing-masing dataset, jelaskan mengapa model regresi linear tepat atau tidak tepat.
    (b) Bila Anda seorang analis dan hanya diberi tabel statistik (tanpa grafik), kesalahan apa yang akan Anda buat pada dataset II dan IV?
    (c) Rancang prosedur pemeriksaan minimum yang harus dilalui **sebelum** menerapkan regresi linear.

11. Rancang sebuah *dashboard* satu halaman untuk melaporkan kinerja sebuah API kepada manajemen non-teknis.
    (a) Tentukan 3–4 grafik yang akan ditampilkan dan alasan pemilihannya.
    (b) Jelaskan bagaimana Anda menampilkan p50, p95, dan p99 secara jelas bagi pembaca awam.
    (c) Bagaimana Anda menghindari kesan bahwa "rata-rata sudah cukup"?
    (d) Tuliskan daftar periksa kejujuran visual khusus untuk *dashboard* itu.

12. Tulislah pedoman ringkas (satu halaman) berjudul *"Standar Visualisasi Data untuk Laporan Prodi Informatika UAI"*. Sertakan: aturan wajib, aturan yang dianjurkan, hal yang dilarang, dan contoh sebelum-sesudah.

---

## Rangkuman

1. **Kuartet Anscombe** membuktikan bahwa statistik ringkasan tidak pernah cukup — selalu lihat datanya lebih dulu.
2. Pemilihan grafik ditentukan oleh **jenis data** dan **pertanyaan analisis**.
3. **Lebar bin histogram mengubah cerita.** Bin sedikit menyembunyikan struktur; bin banyak menampilkan derap sebagai pola. Aturan Freedman-Diaconis paling tahan pencilan.
4. **Boxplot** efisien untuk membandingkan banyak kelompok, tetapi **menyembunyikan bimodalitas**. Violin plot mengungkapnya.
5. **Scatter plot** menunjukkan asosiasi, bukan sebab-akibat. Pola melengkung dan corong adalah peringatan dini untuk analisis regresi.
6. Empat teknik menyesatkan: sumbu tidak dari nol, skala ganda, pemotongan rentang, dan pie chart beririsan banyak.
7. **Bar chart wajib dimulai dari nol** karena panjang batang adalah representasi nilai.
8. Grafik jujur menyebutkan **sumber data dan ukuran sampel** — ini bagian dari amanah dalam pelaporan.
9. **Rasio tinta-data:** maksimalkan tinta yang membawa informasi, minimalkan hiasan.

---

## Referensi

1. Anscombe, F. J. (1973). Graphs in Statistical Analysis. *The American Statistician*, 27(1), 17–21.
2. Matejka, J., & Fitzmaurice, G. (2017). Same Stats, Different Graphs. *Proceedings of CHI '17*, 1290–1294.
3. Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press.
4. Cairo, A. (2019). *How Charts Lie: Getting Smarter about Visual Information*. W. W. Norton.
5. Freedman, D., & Diaconis, P. (1981). On the histogram as a density estimator. *Probability Theory and Related Fields*, 57(4), 453–476.
6. Dokumentasi seaborn — <https://seaborn.pydata.org/tutorial.html>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
