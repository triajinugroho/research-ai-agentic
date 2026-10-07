# Lab 01: Setup Google Colab dan Eksplorasi Data Pertama

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu** | 1 |
| **Durasi** | 180 menit (mandiri) |
| **Prasyarat** | Akun Google aktif |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | 1,92% (bagian dari Observasi 25%) |
| **Berkas data** | `nilai_mahasiswa_if.csv` (tersedia di LMS) |

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. Membuat, menjalankan, dan membagikan notebook Google Colab.
2. Memuat dataset CSV ke dalam pandas DataFrame.
3. Melakukan pemeriksaan awal atas sebuah dataset baru.
4. Menentukan skala pengukuran setiap kolom dan menjelaskan konsekuensinya.
5. Menulis interpretasi atas keluaran statistik, bukan sekadar menampilkan angka.

---

## Persiapan

1. Buka <https://colab.research.google.com> dan masuk dengan akun Google.
2. Buat notebook baru: **File → New notebook**.
3. Ganti namanya menjadi `Lab01_NIM_NamaLengkap`.
4. Unduh `nilai_mahasiswa_if.csv` dari LMS UAI.

> **Catatan tentang dataset.** Berkas `nilai_mahasiswa_if.csv` bersifat **sintetis** — dibuat menyerupai sebaran nilai nyata untuk keperluan latihan. Ia **tidak** menggambarkan mahasiswa sesungguhnya. Hal ini dinyatakan terbuka agar Anda terbiasa memeriksa asal-usul data sebelum menarik kesimpulan apa pun.

---

## Langkah-langkah

### Langkah 1: Memeriksa Lingkungan Kerja

```python
# =============================================
# LANGKAH 1: Memeriksa lingkungan kerja
# =============================================

import sys
import numpy as np
import pandas as pd
import matplotlib
import scipy

print("Lingkungan Google Colab")
print("-" * 40)
print(f"Python      : {sys.version.split()[0]}")
print(f"NumPy       : {np.__version__}")
print(f"pandas      : {pd.__version__}")
print(f"matplotlib  : {matplotlib.__version__}")
print(f"SciPy       : {scipy.__version__}")
```

> **Tulis interpretasi:** apakah seluruh pustaka yang dibutuhkan sudah tersedia? Apakah ada yang perlu dipasang sendiri?

### Langkah 2: Mengunggah dan Memuat Data

```python
# =============================================
# LANGKAH 2: Mengunggah berkas data
# =============================================

from google.colab import files

# Akan memunculkan tombol pilih berkas
uploaded = files.upload()
```

```python
import pandas as pd

# Memuat data ke dalam DataFrame
df = pd.read_csv("nilai_mahasiswa_if.csv")

print("Data berhasil dimuat.")
print(f"Ukuran: {df.shape[0]} baris × {df.shape[1]} kolom")
```

### Langkah 3: Tiga Pemeriksaan Wajib pada Dataset Baru

```python
# =============================================
# LANGKAH 3: Pemeriksaan awal
# =============================================

# (a) Bentuk dan ukuran
print("=== UKURAN ===")
print(f"Jumlah baris  : {df.shape[0]}")
print(f"Jumlah kolom  : {df.shape[1]}")
print(f"Nama kolom    : {list(df.columns)}")

# (b) Lima baris pertama dan terakhir
print("\n=== LIMA BARIS PERTAMA ===")
print(df.head())

print("\n=== LIMA BARIS TERAKHIR ===")
print(df.tail())

# (c) Tipe data dan memori
print("\n=== INFORMASI KOLOM ===")
df.info()
```

> **Tulis interpretasi:** apakah jumlah barisnya masuk akal untuk konteks "mahasiswa dua kelas"? Adakah kolom yang tipenya tampak keliru?

### Langkah 4: Memeriksa Kualitas Data

```python
# =============================================
# LANGKAH 4: Pemeriksaan kualitas data
# =============================================

def periksa_kualitas(df):
    """Pemeriksaan kualitas data dasar sebelum analisis."""

    print("=== NILAI HILANG ===")
    hilang = df.isnull().sum()
    persen = (hilang / len(df) * 100).round(2)
    ringkasan = pd.DataFrame({"jumlah_hilang": hilang, "persen": persen})
    print(ringkasan[ringkasan["jumlah_hilang"] > 0]
          if ringkasan["jumlah_hilang"].sum() > 0
          else "Tidak ada nilai hilang.")

    print("\n=== BARIS DUPLIKAT ===")
    print(f"Jumlah duplikat penuh : {df.duplicated().sum()}")

    print("\n=== KARDINALITAS KOLOM KATEGORIKAL ===")
    for kolom in df.select_dtypes(include="object").columns:
        print(f"  {kolom:14s}: {df[kolom].nunique()} nilai unik "
              f"→ {sorted(df[kolom].unique())[:6]}")

    print("\n=== RENTANG KOLOM NUMERIK ===")
    for kolom in df.select_dtypes(include=["int64", "float64"]).columns:
        print(f"  {kolom:14s}: {df[kolom].min()} sampai {df[kolom].max()}")

periksa_kualitas(df)
```

> **Tulis interpretasi:** adakah nilai yang mustahil? Misalnya nilai ujian negatif, atau jam belajar lebih dari 168 jam per minggu?

### Langkah 5: Menentukan Skala Pengukuran

Ini langkah yang paling penting — dan yang paling sering dilewati pemula.

```python
# =============================================
# LANGKAH 5: Menentukan skala pengukuran
# =============================================

# Isi sendiri berdasarkan pemahaman Anda dari Minggu 1
skala_kolom = {
    "nim":          "nominal",    # identitas, bukan besaran
    "kelas":        "nominal",
    "nilai_uts":    "interval",
    "nilai_uas":    "interval",
    "jam_belajar":  "rasio",
    "asal_sekolah": "nominal",
}

operasi_sah = {
    "nominal":  ["frekuensi", "modus", "proporsi"],
    "ordinal":  ["frekuensi", "modus", "median", "kuartil"],
    "interval": ["frekuensi", "modus", "median", "mean", "simpangan baku"],
    "rasio":    ["frekuensi", "modus", "median", "mean", "simpangan baku",
                 "koefisien variasi", "rasio antar nilai"],
}

print(f"{'Kolom':16s} {'Tipe Python':14s} {'Skala':12s} Operasi yang sah")
print("-" * 92)
for kolom, skala in skala_kolom.items():
    tipe_py = str(df[kolom].dtype)
    print(f"{kolom:16s} {tipe_py:14s} {skala:12s} "
          f"{', '.join(operasi_sah[skala][:4])}")
```

> **Tulis interpretasi:** perhatikan kolom `nim`. Tipenya `int64`, tetapi skalanya nominal. Apa yang terjadi bila seseorang menghitung rata-rata NIM? Mengapa Python tidak mencegahnya?

### Langkah 6: Ringkasan Statistik Awal

```python
# =============================================
# LANGKAH 6: Ringkasan statistik
# =============================================

# Ringkasan numerik — PERHATIKAN kolom mana yang sebenarnya tidak layak
print("=== RINGKASAN NUMERIK (apa adanya dari pandas) ===")
print(df.describe().T.round(2))

# Ringkasan yang BENAR: hanya kolom yang skalanya sesuai
kolom_layak = [k for k, s in skala_kolom.items() if s in ("interval", "rasio")]
print(f"\n=== RINGKASAN YANG BENAR (hanya {kolom_layak}) ===")
print(df[kolom_layak].describe().T.round(2))

# Ringkasan kategorikal
print("\n=== DISTRIBUSI KOLOM KATEGORIKAL ===")
for kolom in ["kelas", "asal_sekolah"]:
    print(f"\n{kolom}:")
    frek = df[kolom].value_counts()
    prop = df[kolom].value_counts(normalize=True) * 100
    print(pd.DataFrame({"frekuensi": frek, "persen": prop.round(2)}))
```

> **Tulis interpretasi:** `df.describe()` menghitung rata-rata NIM. Jelaskan mengapa angka itu tidak bermakna, dan apa pelajarannya tentang hubungan antara tipe data komputer dan skala pengukuran statistik.

### Langkah 7: Visualisasi Pertama

```python
# =============================================
# LANGKAH 7: Visualisasi awal
# =============================================

import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

# Histogram nilai UAS
axes[0].hist(df["nilai_uas"], bins=20, color="steelblue", edgecolor="white")
axes[0].set_title("Sebaran Nilai UAS")
axes[0].set_xlabel("Nilai UAS (0–100)")
axes[0].set_ylabel("Jumlah mahasiswa")

# Histogram jam belajar
axes[1].hist(df["jam_belajar"], bins=20, color="#27ae60", edgecolor="white")
axes[1].set_title("Sebaran Jam Belajar per Minggu")
axes[1].set_xlabel("Jam per minggu")

# Bar chart asal sekolah
frek = df["asal_sekolah"].value_counts()
axes[2].bar(frek.index, frek.values, color="#e67e22")
axes[2].set_title("Asal Sekolah")
axes[2].set_ylabel("Jumlah mahasiswa")
axes[2].tick_params(axis="x", rotation=20)

plt.suptitle(f"Eksplorasi awal — n = {len(df)} mahasiswa", y=1.03)
plt.tight_layout()
plt.show()
```

> **Tulis interpretasi:** untuk setiap grafik, tuliskan satu kalimat tentang apa yang Anda lihat. Apakah sebarannya simetris? Adakah nilai yang tampak menyendiri?

### Langkah 8: Menyimpan dan Membagikan

```python
# =============================================
# LANGKAH 8: Menyimpan hasil
# =============================================

# Menyimpan ringkasan ke berkas CSV
ringkasan = df[kolom_layak].describe().T.round(2)
ringkasan.to_csv("ringkasan_lab01.csv")
print("Ringkasan disimpan.")

# Mengunduh ke komputer
from google.colab import files
files.download("ringkasan_lab01.csv")
```

**Membagikan notebook:**
1. **Share** → **Change to anyone with the link** → **Viewer**.
2. Salin tautannya.
3. Unduh juga sebagai `.ipynb`: **File → Download → Download .ipynb**.

---

## Tantangan Tambahan

### Tantangan 1: Menemukan Nilai yang Mustahil

Tulis fungsi yang memeriksa nilai mustahil pada setiap kolom numerik, berdasarkan pengetahuan konteks (bukan statistik).

```python
def periksa_nilai_mustahil(df):
    """Memeriksa nilai yang mustahil berdasarkan konteks domain."""
    masalah = []

    # Contoh aturan — lengkapi sendiri
    if (df["nilai_uts"] < 0).any() or (df["nilai_uts"] > 100).any():
        masalah.append("nilai_uts di luar rentang 0–100")

    # TUGAS ANDA: tambahkan sekurang-kurangnya 3 aturan lagi
    # Petunjuk: jam belajar tidak mungkin negatif; tidak mungkin
    # melebihi 168 jam (jumlah jam dalam seminggu); NIM harus
    # punya jumlah digit yang konsisten

    return masalah if masalah else ["Tidak ditemukan nilai mustahil."]

for m in periksa_nilai_mustahil(df):
    print("•", m)
```

### Tantangan 2: Perbandingan Dua Kelas

Buat tabel yang membandingkan IF26A dan IF26H pada seluruh kolom numerik. Gunakan `groupby`.

```python
# TUGAS ANDA
perbandingan = df.groupby("kelas")[kolom_layak].agg(
    ["count", "mean", "median", "std", "min", "max"]
).round(2)
print(perbandingan)
```

**Pertanyaan yang harus dijawab dalam interpretasi:**
Bila rata-rata salah satu kelas lebih tinggi, bolehkah Anda menyimpulkan kelas itu "lebih baik"? Jelaskan mengapa tidak — dan sebutkan materi minggu ke berapa yang akan menjawab pertanyaan itu secara benar.

### Tantangan 3: Memuat Data dari Sumber Nyata

Unduh satu tabel dari BPS (<https://www.bps.go.id>) atau Satu Data Indonesia (<https://data.go.id>), muat ke Colab, dan jalankan pemeriksaan kualitas yang sama.

```python
# TUGAS ANDA
# Petunjuk untuk berkas Excel BPS yang punya baris judul ganda:
# df_bps = pd.read_excel("berkas_bps.xlsx", skiprows=3, skipfooter=2,
#                        engine="openpyxl")
```

Laporkan: berapa baris, berapa kolom, masalah apa yang Anda temui saat memuatnya, dan bagaimana Anda mengatasinya.

---

## Refleksi

Tulis 3–5 kalimat menjawab:

1. Apa hal paling baru yang Anda pelajari dari lab ini?
2. Bagian mana yang masih membingungkan?
3. Mengapa menentukan skala pengukuran perlu dilakukan **sebelum** menghitung apa pun?

---

## AI Usage Log

Wajib diisi pada sel terakhir notebook.

| No | Tanggal | Alat AI | Untuk apa | Prompt (ringkas) | Apa yang saya ubah/verifikasi |
|----|---------|---------|-----------|------------------|-------------------------------|
| 1 | | | | | |

**Pernyataan:**

> *Saya menyatakan bahwa seluruh perhitungan statistik, pemilihan metode, dan interpretasi hasil dalam pekerjaan ini adalah hasil pemahaman saya sendiri. Penggunaan AI telah saya catat seluruhnya pada tabel di atas. Saya bersedia menjelaskan setiap bagian pekerjaan ini apabila diminta.*
>
> Nama: ______________  NIM: ______________

---

## Checklist Penyelesaian

- [ ] Notebook dinamai `Lab01_NIM_NamaLengkap.ipynb`
- [ ] Seluruh sel dapat dijalankan ulang dari atas ke bawah tanpa galat
- [ ] Langkah 1–8 selesai dikerjakan
- [ ] **Setiap keluaran statistik disertai kalimat interpretasi**
- [ ] Ketiga tantangan tambahan dikerjakan
- [ ] Bagian Refleksi terisi (3–5 kalimat)
- [ ] AI Usage Log terisi dan pernyataan ditandatangani
- [ ] Berkas `.ipynb` diunggah ke LMS
- [ ] Tautan Colab dibagikan dengan akses *Viewer*

---

## Kriteria Penilaian

| Aspek | Bobot |
|-------|-------|
| Ketepatan prosedur | 30% |
| Kesesuaian grafik | 20% |
| Validitas interpretasi | 30% |
| Tantangan tambahan | 10% |
| Kerapian dan AI Usage Log | 10% |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
