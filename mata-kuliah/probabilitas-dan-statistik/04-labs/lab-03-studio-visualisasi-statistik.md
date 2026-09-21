# Lab 03: Studio Visualisasi Statistik

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu** | 3 |
| **Durasi** | 180 menit (mandiri) |
| **Prasyarat** | Lab 02 selesai |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | 1,92% |
| **Berkas data** | `nilai_mahasiswa_if.csv`, `waktu_respons_server.csv` |

---

## Tujuan Praktikum

1. Membuat histogram, boxplot, violin plot, scatter plot, dan bar chart dengan matplotlib dan seaborn.
2. Menunjukkan dampak lebar bin terhadap kesan yang ditangkap pembaca.
3. Mengenali dan memperbaiki grafik yang menyesatkan.
4. Menerapkan daftar periksa kejujuran visual pada grafik sendiri.
5. Memilih grafik berdasarkan jenis data dan pertanyaan analisis.

---

## Persiapan

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 110

df = pd.read_csv("nilai_mahasiswa_if.csv")
srv = pd.read_csv("waktu_respons_server.csv")
```

---

## Langkah-langkah

### Langkah 1: Kuartet Anscombe — Mengapa Grafik Wajib

```python
# =============================================
# LANGKAH 1: Statistik sama, bentuk berbeda
# =============================================

anscombe = sns.load_dataset("anscombe")

# Buktikan statistiknya nyaris identik
ringkas = anscombe.groupby("dataset").agg(
    mean_x=("x", "mean"), mean_y=("y", "mean"),
    std_x=("x", "std"), std_y=("y", "std"),
).round(3)
korelasi = anscombe.groupby("dataset").apply(
    lambda g: stats.pearsonr(g["x"], g["y"])[0]
).round(3)
ringkas["korelasi"] = korelasi
print(ringkas)

# Tetapi bentuknya sangat berbeda
sns.lmplot(data=anscombe, x="x", y="y", col="dataset", col_wrap=2,
           height=3, ci=None, scatter_kws={"s": 60, "alpha": 0.8})
plt.suptitle("Kuartet Anscombe", y=1.02)
plt.show()
```

> **Tulis interpretasi:** untuk masing-masing dataset I–IV, jelaskan apa yang terjadi dan mengapa statistik ringkasan gagal menangkapnya.

### Langkah 2: Dampak Lebar Bin

```python
# =============================================
# LANGKAH 2: Lebar bin mengubah cerita
# =============================================

rng = np.random.default_rng(42)
data_bimodal = np.concatenate([
    rng.normal(62, 7, 320),     # kelompok nilai rendah
    rng.normal(84, 6, 220),     # kelompok nilai tinggi
])

fig, axes = plt.subplots(1, 4, figsize=(18, 4))
for ax, bins in zip(axes, [4, 12, 35, 140]):
    ax.hist(data_bimodal, bins=bins, color="steelblue", edgecolor="white")
    ax.set_title(f"bins = {bins}")
    ax.set_xlabel("Nilai")
axes[0].set_ylabel("Frekuensi")
plt.suptitle("Data yang SAMA, kesan yang BERBEDA", y=1.04)
plt.tight_layout()
plt.show()
```

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
    print(f"  Freedman-Diaconis : {fd}  ← paling tahan pencilan")
    return fd

saran_bin(data_bimodal)
```

> **Tulis interpretasi:** dengan bins=4, informasi penting apa yang hilang? Bila Anda ingin menyembunyikan fakta bahwa ada dua kelompok, bin mana yang Anda pilih? Apa implikasi etisnya?

### Langkah 3: Boxplot vs Violin Plot

```python
# =============================================
# LANGKAH 3: Kapan boxplot menyembunyikan sesuatu
# =============================================

rng = np.random.default_rng(0)
sebaran_a = rng.normal(70, 12, 500)
sebaran_b = np.concatenate([rng.normal(55, 5, 250), rng.normal(85, 5, 250)])

fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

axes[0].boxplot([sebaran_a, sebaran_b], labels=["A", "B"])
axes[0].set_title("Boxplot — tampak serupa")

sns.violinplot(data=[sebaran_a, sebaran_b], ax=axes[1], palette="Set2")
axes[1].set_xticklabels(["A", "B"])
axes[1].set_title("Violin — bimodalitas B terungkap")

axes[2].hist(sebaran_a, bins=30, alpha=0.6, label="A", color="steelblue")
axes[2].hist(sebaran_b, bins=30, alpha=0.6, label="B", color="#e67e22")
axes[2].legend()
axes[2].set_title("Histogram — paling jelas")

plt.tight_layout()
plt.show()

# Bandingkan ringkasan lima angkanya
for nama, d in [("A", sebaran_a), ("B", sebaran_b)]:
    q = np.percentile(d, [0, 25, 50, 75, 100])
    print(f"{nama}: min={q[0]:.1f} Q1={q[1]:.1f} med={q[2]:.1f} "
          f"Q3={q[3]:.1f} max={q[4]:.1f}")
```

### Langkah 4: Grafik untuk Data Nyata

```python
# =============================================
# LANGKAH 4: Visualisasi data kelas
# =============================================

fig, axes = plt.subplots(2, 2, figsize=(14, 9))

# (a) Sebaran nilai UAS dengan garis median
axes[0, 0].hist(df["nilai_uas"], bins=20, color="steelblue", edgecolor="white")
med = df["nilai_uas"].median()
axes[0, 0].axvline(med, color="#c0392b", linestyle="--", linewidth=2,
                   label=f"Median = {med:.1f}")
axes[0, 0].set_title("Sebaran Nilai UAS")
axes[0, 0].set_xlabel("Nilai UAS (0–100)")
axes[0, 0].set_ylabel("Jumlah mahasiswa")
axes[0, 0].legend()

# (b) Boxplot jam belajar per asal sekolah
sns.boxplot(data=df, x="asal_sekolah", y="jam_belajar",
            ax=axes[0, 1], palette="Set2")
axes[0, 1].set_title("Jam Belajar menurut Asal Sekolah")
axes[0, 1].set_xlabel("Asal sekolah")
axes[0, 1].set_ylabel("Jam per minggu")
axes[0, 1].tick_params(axis="x", rotation=15)

# (c) Scatter jam belajar vs nilai UAS
sns.scatterplot(data=df, x="jam_belajar", y="nilai_uas", hue="kelas",
                ax=axes[1, 0], s=55, alpha=0.75)
axes[1, 0].set_title("Jam Belajar vs Nilai UAS")
axes[1, 0].set_xlabel("Jam belajar per minggu")
axes[1, 0].set_ylabel("Nilai UAS")

# (d) Bar chart asal sekolah, diurutkan
frek = df["asal_sekolah"].value_counts().sort_values()
axes[1, 1].barh(frek.index, frek.values, color="#e67e22")
axes[1, 1].set_title("Jumlah Mahasiswa menurut Asal Sekolah")
axes[1, 1].set_xlabel("Jumlah mahasiswa")

plt.suptitle(f"Profil Mahasiswa Probabilitas dan Statistik — n = {len(df)}",
             y=1.01, fontsize=13)
plt.tight_layout()
plt.show()
```

> **Tulis interpretasi untuk setiap panel:** apa yang Anda lihat, dan apa yang **belum bisa** Anda simpulkan dari grafik itu.

### Langkah 5: Empat Teknik Menyesatkan

```python
# =============================================
# LANGKAH 5: Mengenali grafik yang menyesatkan
# =============================================

fig, axes = plt.subplots(2, 2, figsize=(14, 9))

# (a) Sumbu tidak dari nol pada bar chart
kat, nil = ["Produk A", "Produk B"], [98, 100]
axes[0, 0].bar(kat, nil, color=["#c0392b", "#27ae60"])
axes[0, 0].set_ylim(97, 101)
axes[0, 0].set_title("MENYESATKAN: sumbu mulai 97\nB tampak jauh lebih baik")

axes[0, 1].bar(kat, nil, color=["#c0392b", "#27ae60"])
axes[0, 1].set_ylim(0, 110)
axes[0, 1].set_title("JUJUR: sumbu mulai 0\nselisih sebenarnya hanya 2%")

# (b) Pie chart terlalu banyak irisan vs bar chart
bahasa = ["Python", "JavaScript", "Java", "C++", "PHP", "Go", "Rust"]
jumlah = [145, 112, 98, 67, 45, 34, 28]
axes[1, 0].pie(jumlah, labels=bahasa, autopct="%1.1f%%", startangle=90)
axes[1, 0].set_title("SULIT DIBACA: bandingkan Go, Rust, PHP")

urut = sorted(zip(jumlah, bahasa))
axes[1, 1].barh([b for _, b in urut], [j for j, _ in urut], color="steelblue")
axes[1, 1].set_title("MUDAH DIBACA: perbandingan langsung")
axes[1, 1].set_xlabel("Jumlah pengguna")

plt.tight_layout()
plt.show()
```

### Langkah 6: Template Grafik yang Memenuhi Daftar Periksa

```python
# =============================================
# LANGKAH 6: Grafik yang jujur dan lengkap
# =============================================

fig, ax = plt.subplots(figsize=(10, 6))

n_bin = 20
ax.hist(srv["waktu_ms"], bins=n_bin, color="steelblue",
        edgecolor="white", alpha=0.85)

med = srv["waktu_ms"].median()
p95 = srv["waktu_ms"].quantile(0.95)
ax.axvline(med, color="#27ae60", linestyle="--", linewidth=2,
           label=f"Median (p50) = {med:.0f} ms")
ax.axvline(p95, color="#c0392b", linestyle="--", linewidth=2,
           label=f"p95 = {p95:.0f} ms")

ax.set_title("Sebaran Waktu Respons API\n"
             "Sistem Informasi Akademik UAI, September 2026",
             fontsize=12, pad=12)
ax.set_xlabel("Waktu respons (milidetik)")
ax.set_ylabel("Jumlah permintaan")
ax.legend()

ax.text(0.99, -0.13,
        f"n = {len(srv):,} permintaan · {n_bin} bin · "
        f"Sumber: log server SIA UAI",
        transform=ax.transAxes, ha="right", fontsize=8, color="gray")

plt.tight_layout()
plt.show()
```

**Daftar periksa yang harus dipenuhi setiap grafik Anda:**

- [ ] Judul menjelaskan **apa** yang ditampilkan, bukan sekadar nama variabel
- [ ] Kedua sumbu berlabel **beserta satuannya**
- [ ] Sumbu-y bar chart dimulai dari nol
- [ ] Jumlah bin disebutkan atau wajar
- [ ] Sumber data dicantumkan
- [ ] Ukuran sampel (n) terlihat
- [ ] Warna masih terbaca dalam hitam-putih
- [ ] Tidak ada elemen dekoratif tanpa informasi
- [ ] Skala tidak dipotong tanpa penjelasan

---

## Tantangan Tambahan

### Tantangan 1: Memperbaiki Grafik Menyesatkan

Gunakan grafik menyesatkan yang Anda temukan sebelum kelas (tugas pra-kelas Minggu 3).

1. Tampilkan tangkapan layarnya di notebook (gunakan sel Markdown dengan gambar).
2. Identifikasi teknik menyesatkan yang dipakai.
3. **Buat ulang** grafik itu secara jujur dengan matplotlib, dengan data yang sama.
4. Jelaskan bagaimana kesan pembaca berubah.

### Tantangan 2: Heatmap Korelasi

```python
# TUGAS ANDA: buat heatmap korelasi untuk kolom numerik di df
# Ketentuan:
#   - gunakan skema warna DIVERGEN (misalnya 'RdBu_r' atau 'coolwarm')
#   - pusatkan pada nol (center=0)
#   - tampilkan nilainya (annot=True)
#   - beri judul dan keterangan n
# Petunjuk: sns.heatmap(df[kolom_numerik].corr(), ...)
```

**Pertanyaan:** mengapa skema warna divergen lebih tepat daripada skema sekuensial untuk korelasi?

### Tantangan 3: Grafik untuk Data Anda Sendiri

Gunakan dataset proyek kelompok Anda (atau data BPS pilihan Anda).

Buat **tiga grafik** yang menjawab tiga pertanyaan berbeda, masing-masing memenuhi seluruh daftar periksa kejujuran visual. Untuk tiap grafik tuliskan:

1. Pertanyaan analisis yang dijawab.
2. Mengapa jenis grafik itu yang dipilih.
3. Apa yang terlihat.
4. Apa yang **tidak boleh** disimpulkan dari grafik itu.

---

## Refleksi

1. Grafik mana yang paling sering Anda lihat dipakai secara menyesatkan di media?
2. Apa perbedaan antara "menyederhanakan grafik" dan "menyembunyikan informasi"?
3. Bagaimana prinsip **amanah** berlaku dalam pembuatan grafik?

---

## AI Usage Log

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |

> Nama: ______________  NIM: ______________

---

## Checklist Penyelesaian

- [ ] Notebook dinamai `Lab03_NIM_NamaLengkap.ipynb`
- [ ] Langkah 1–6 selesai
- [ ] Setiap grafik disertai interpretasi
- [ ] Setiap grafik buatan sendiri memenuhi daftar periksa kejujuran visual
- [ ] Ketiga tantangan dikerjakan
- [ ] Refleksi terisi
- [ ] AI Usage Log terisi
- [ ] Diunggah ke LMS

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
