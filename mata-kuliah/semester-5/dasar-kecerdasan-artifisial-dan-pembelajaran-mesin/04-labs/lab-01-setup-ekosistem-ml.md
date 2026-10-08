# Lab 01: Penyiapan Lingkungan dan Eksplorasi Dataset Pertama

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 1 |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-01 |
| Durasi | 100 menit (45' di kelas + 55' mandiri) |
| Prasyarat | Akun Google; dasar Python |
| Bobot | 1,875% (Observasi, Sub-CPMK082-1) |
| Diuji pada | scikit-learn 1.6 dan 1.9, pandas 2.2 dan 3.0 (Oktober 2026) |

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. Menyiapkan lingkungan kerja Google Colab dan memverifikasi versi pustaka.
2. Memuat dan memeriksa dataset dari berbagai sumber.
3. Mengenali anatomi masalah ML: fitur, target, jenis *task*.
4. Menentukan apakah sebuah masalah memang memerlukan pembelajaran mesin.

---

## Persiapan

1. Buka <https://colab.research.google.com> dan buat notebook baru.
2. Beri nama `NIM_Nama_Lab01.ipynb`.
3. Pastikan dapat menjalankan sel dengan `Shift+Enter`.
4. **Data:** Langkah 2–3 memakai dataset bawaan `scikit-learn` (`load_diabetes`, `load_breast_cancer`). Tabel IPM provinsi pada Langkah 4 adalah **contoh ilustratif** untuk mempelajari struktur data: angkanya sebagian menyerupai rilis IPM BPS dari tahun yang berbeda-beda, **bukan kutipan resmi BPS**, sehingga tidak boleh dikutip sebagai data BPS. Untuk analisis yang dilaporkan (mis. Tantangan 1 atau proyek), unduh tabel IPM dari <https://www.bps.go.id> dan catat nama tabel serta tahunnya — lihat [panduan dataset §1.1](../datasets/README.md#11-data-praktikum-dan-data-proyek-sengaja-berbeda).

---

## Langkah-langkah

### LANGKAH 1: Sel Pembuka Baku

Sel ini akan dipakai pada **setiap** notebook sepanjang semester.

```python
# =============================================
# LANGKAH 1: Sel pembuka baku
# =============================================
import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

# Pencatatan versi — bagian dari reproduksibilitas,
# yang merupakan kriteria penilaian Sub-CPMK082-1
print("Python      :", sys.version.split()[0])
print("NumPy       :", np.__version__)
print("pandas      :", pd.__version__)
print("matplotlib  :", matplotlib.__version__)
print("seaborn     :", sns.__version__)
print("scikit-learn:", sklearn.__version__)

# Pengaturan tampilan
pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 120)
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (9, 5)
plt.rcParams["figure.dpi"] = 110

# Seed — WAJIB agar hasil dapat diulang
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)
print("\nLingkungan siap. RANDOM_STATE =", RANDOM_STATE)
```

### LANGKAH 2: Memuat Dataset Bawaan scikit-learn

```python
# =============================================
# LANGKAH 2: Dataset pertama — diabetes (regresi)
# =============================================
from sklearn.datasets import load_diabetes

data = load_diabetes(as_frame=True)
df_diabetes = data.frame

print("Dimensi:", df_diabetes.shape)
print("\nLima baris pertama:")
display(df_diabetes.head())

print("\nDeskripsi target:")
print(df_diabetes["target"].describe())
```

**Pertanyaan yang harus dijawab di sel Markdown:**
- Apa **targetnya**? Bilangan kontinu atau kategori?
- Jenis *task* apa ini?
- Berapa jumlah fitur?

### LANGKAH 3: Memuat Dataset Klasifikasi

```python
# =============================================
# LANGKAH 3: Dataset kedua — breast cancer (klasifikasi)
# =============================================
from sklearn.datasets import load_breast_cancer

data2 = load_breast_cancer(as_frame=True)
df_kanker = data2.frame

print("Dimensi:", df_kanker.shape)
print("\nSebaran kelas:")
print(df_kanker["target"].value_counts())
print("\nProporsi:")
print(df_kanker["target"].value_counts(normalize=True).round(3))
print("\nNama kelas:", data2.target_names)
```

**Yang perlu diperhatikan:** periksa apakah kelasnya seimbang. Ketidakseimbangan menentukan metrik yang akan dipakai — bahasan Minggu 7.

### LANGKAH 4: Contoh Struktur Data IPM Provinsi (ilustratif)

> **Contoh ilustratif**, bukan kutipan resmi BPS — lihat Persiapan butir 4.

```python
# =============================================
# LANGKAH 4: Contoh struktur data IPM provinsi (ILUSTRATIF)
# =============================================
# Angka ilustratif: sebagian menyerupai rilis IPM BPS dari tahun yang
# berbeda-beda; BUKAN kutipan resmi BPS. Untuk analisis yang dilaporkan,
# unduh tabel IPM dari bps.go.id (catat nama tabel dan tahunnya),
# lalu unggah melalui panel Files di Colab.
data_ipm = pd.DataFrame({
    "provinsi": ["DKI Jakarta", "Jawa Barat", "Jawa Tengah", "DI Yogyakarta",
                 "Jawa Timur", "Sumatera Utara", "Sulawesi Selatan",
                 "Kalimantan Timur", "Bali", "Papua"],
    "ipm":              [82.46, 73.74, 73.39, 81.07, 72.75,
                         73.13, 73.26, 77.44, 76.61, 62.25],
    "harapan_hidup":    [73.2, 73.3, 74.5, 75.1, 71.6,
                         69.6, 70.9, 74.6, 72.1, 66.0],
    "rata_lama_sekolah":[11.3, 8.8, 7.8, 9.8, 8.0,
                         9.6, 8.7, 9.9, 9.0, 7.1],
    "pengeluaran_kapita":[19.0, 11.4, 11.3, 15.0, 12.2,
                          11.5, 11.9, 12.5, 14.2, 7.6],
})

print("Dimensi:", data_ipm.shape)
display(data_ipm)

# Tujuh perintah pembuka — akan dipakai setiap kali menerima data baru
print("\n--- Info ---")
data_ipm.info()
print("\n--- Ringkasan numerik ---")
display(data_ipm.describe().T.round(2))
print("\n--- Nilai hilang (%) ---")
print((data_ipm.isna().mean() * 100).round(2))
print("\n--- Duplikat ---")
print(data_ipm.duplicated().sum())
```

### LANGKAH 5: Mengenali Anatomi Masalah ML

```python
# =============================================
# LANGKAH 5: Anatomi masalah ML
# =============================================
# Untuk setiap dataset, isi tabel berikut di sel Markdown.

# Contoh untuk data IPM:
#
# | Aspek              | Jawaban                                      |
# |--------------------|----------------------------------------------|
# | Target             | ipm (kontinu)                                |
# | Fitur              | harapan_hidup, rata_lama_sekolah, ...        |
# | Jenis task         | Regresi                                      |
# | Jumlah baris       | 10                                           |
# | Apakah perlu ML?   | TIDAK — IPM dihitung dengan RUMUS BAKU BPS   |
#                        dari komponennya: umur harapan hidup, harapan
#                        lama sekolah, rata-rata lama sekolah, dan
#                        pengeluaran per kapita. Rumusnya diketahui
#                        dan pasti. Membangun model ML untuk ini
#                        menghasilkan hampiran yang lebih buruk
#                        daripada rumus aslinya.

# Periksa dugaan tersebut: seberapa erat tiap komponen berkaitan dengan IPM?
korelasi = data_ipm.select_dtypes(include="number").corr()["ipm"].sort_values(ascending=False)
print("Korelasi terhadap IPM:")
print(korelasi.round(3))

# Kesimpulan DIHITUNG dari hasil, bukan teks tetap
komponen = korelasi.drop("ipm")
print(f"\nKorelasi ketiga komponen dengan IPM: {komponen.min():.2f}–{komponen.max():.2f}.")
if komponen.min() >= 0.7:
    print("Semuanya tinggi: IPM memang dibangun dari komponen-komponen ini. "
          "Tidak satu pun sempurna, karena IPM menggabungkan beberapa komponen —\n"
          "dan tabel ilustratif ini tidak memuat harapan lama sekolah.")
else:
    print("Ada komponen yang korelasinya rendah — periksa kembali isi data_ipm.")
```

**Pemeriksaan otomatis.** Sel berikut harus lulus tanpa `AssertionError`; bila gagal, pesannya menunjukkan apa yang perlu diperiksa.

```python
# =============================================
# Pemeriksaan otomatis — Langkah 2 sampai 5
# =============================================
assert df_diabetes.shape == (442, 11), (
    "Dataset diabetes seharusnya 442 baris x 11 kolom (10 fitur + target)")
assert set(df_kanker["target"].unique()) == {0, 1}, (
    "Dataset breast cancer seharusnya berlabel biner 0/1")
assert data_ipm.isna().sum().sum() == 0, "Tabel contoh IPM seharusnya tanpa nilai hilang"
assert komponen.min() >= 0.7, (
    "Ketiga komponen seharusnya berkorelasi tinggi (>= 0,7) dengan IPM — "
    "periksa angka pada data_ipm di Langkah 4")
print("Pemeriksaan otomatis lulus.")
```

> **Ini adalah pelajaran utama Lab 1.** Korelasi yang sangat tinggi antara fitur dan target dapat berarti dua hal: (a) fitur memang sangat informatif, atau (b) **target adalah turunan langsung dari fitur** — yaitu kasus ketika ML tidak diperlukan sama sekali, atau bahkan merupakan bentuk kebocoran.

### LANGKAH 6: Uji Kelayakan Enam Pertanyaan

```python
# =============================================
# LANGKAH 6: Uji kelayakan ML
# =============================================
# Untuk KETIGA dataset, jawab enam pertanyaan berikut
# di sel Markdown:
#
# 1. Apakah ada POLA yang harus dipelajari, atau aturannya
#    sudah diketahui?
# 2. Apakah DATA tersedia dalam jumlah dan mutu memadai?
# 3. Apakah KESALAHAN dapat ditoleransi, dan berapa biayanya?
# 4. Apakah prediksi akan BENAR-BENAR DIPAKAI untuk keputusan?
# 5. Apakah ada PEMBANDING sederhana yang harus dikalahkan?
# 6. Apakah KONSEKUENSI kesalahan sudah dipahami, termasuk
#    siapa yang dirugikan?
```

### LANGKAH 7: Visualisasi Awal

```python
# =============================================
# LANGKAH 7: Melihat data sebelum apa pun
# =============================================
fig, ax = plt.subplots(1, 2, figsize=(13, 4.5))

# Sebaran target regresi
ax[0].hist(df_diabetes["target"], bins=25, edgecolor="white")
ax[0].set_xlabel("Target (perkembangan penyakit)")
ax[0].set_ylabel("Frekuensi")
ax[0].set_title(f"Sebaran target — regresi (n={len(df_diabetes)})")

# Sebaran kelas klasifikasi
df_kanker["target"].value_counts().sort_index().plot(kind="bar", ax=ax[1])
ax[1].set_xlabel("Kelas")
ax[1].set_ylabel("Jumlah")
ax[1].set_title(f"Sebaran kelas — klasifikasi (n={len(df_kanker)})")
ax[1].tick_params(axis="x", rotation=0)

plt.tight_layout()
plt.show()
```

> **Kaidah yang berlaku sepanjang semester:** setiap grafik wajib memiliki judul yang bermakna, label sumbu, dan keterangan **n**.

### LANGKAH 8: AI Usage Log

```python
# =============================================
# LANGKAH 8: AI Usage Log (WAJIB, sel terakhir)
# =============================================
# Salin format berikut ke sel Markdown terakhir dan isi:
#
# ## AI Usage Log
#
# | No | Bagian | Alat | Permintaan | Dipakai? | Verifikasi |
# |----|--------|------|------------|----------|------------|
# | 1  |        |      |            |          |            |
#
# Daftar larangan AI (RPS §K.1) — kegiatan yang TIDAK BOLEH dibantu AI:
# L1. Memformulasikan masalah menjadi task ML
# L2. Memilih model dan hiperparameter
# L3. Memilih dan menafsirkan metrik
# L4. Menganalisis kesalahan model
# L5. Menulis model card dan analisis keterbatasan
# L6. Selama kuis, UTS, dan UAS (tidak boleh sama sekali)
#
# Butir L1–L5 WAJIB muncul di log sebagai "dikerjakan sendiri",
# satu baris per butir; L6 berlaku di ruang kuis dan ujian.
#
# **Pernyataan:** ...
# Nama: __________  NIM: __________  Tanggal: __________
```

Butir L1–L6 di atas adalah daftar larangan AI pada [RPS §K.1](../01-rps/rps-dasar-kecerdasan-artifisial-pembelajaran-mesin.md#k1-kebijakan-kecerdasan-artifisial), dengan rumusan yang sama (bila berbeda, RPS yang berlaku). Contoh log lengkap — termasuk lima baris L1–L5 dan teks pernyataannya — ada pada [RTM §I](../02-rtm/rtm-dasar-kecerdasan-artifisial-pembelajaran-mesin.md#i-ai-usage-log--format-wajib).

---

## Tantangan Tambahan

### Tantangan 1 — Dataset Pilihan Sendiri

Unduh satu dataset nyata dari BPS, Satu Data Indonesia, atau Jakarta Open Data. Jalankan tujuh perintah pembuka, lalu isi tabel anatomi masalah dan uji kelayakan enam pertanyaan.

### Tantangan 2 — Mencari Contoh "ML Tidak Diperlukan"

Temukan satu kasus nyata (dari berita, aplikasi yang Anda pakai, atau lingkungan kampus) yang **diiklankan memakai AI** tetapi sebenarnya dapat diselesaikan dengan aturan biasa. Jelaskan alasannya dalam satu paragraf.

### Tantangan 3 — Memeriksa Reproduksibilitas

Jalankan ulang seluruh notebook dari sel pertama (`Runtime → Restart and run all`). Pastikan tidak ada galat dan seluruh keluaran muncul kembali. Bila ada perbedaan hasil, temukan penyebabnya.

---

## Checklist Penyelesaian

- [ ] Sel pembuka baku memuat versi seluruh pustaka
- [ ] `RANDOM_STATE` ditetapkan
- [ ] Ketiga dataset dimuat dan diperiksa dengan tujuh perintah pembuka
- [ ] Tabel anatomi masalah diisi untuk ketiga dataset
- [ ] Uji kelayakan enam pertanyaan dijawab untuk ketiga dataset
- [ ] **Alasan tertulis** mengapa data IPM tidak memerlukan ML
- [ ] Minimal dua grafik dengan judul, label sumbu, dan n
- [ ] Setiap keluaran disertai kalimat penafsiran
- [ ] Notebook berjalan ulang dari sel pertama tanpa galat dan pemeriksaan otomatis lulus
- [ ] AI Usage Log lengkap dan ditandatangani
- [ ] Berkas dinamai `NIM_Nama_Lab01.ipynb`

---

## Referensi

1. [Modul Minggu 1](../03-modules/week-01-lanskap-kecerdasan-artifisial.md)
2. [Bab 1 buku ajar](../06-buku-ajar/bab-01-lanskap-kecerdasan-artifisial.md)
3. Dokumentasi scikit-learn — *Toy datasets*. <https://scikit-learn.org/stable/datasets/toy_dataset.html>
4. [Panduan dataset](../datasets/README.md)
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
