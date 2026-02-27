# Lab 01: Setup Python dan Google Colab

**Mata Kuliah:** Statistika dan Probabilitas
**Program Studi:** Universitas Al Azhar Indonesia
**Minggu:** 1
**Penilaian:** Tidak dinilai (checklist completion)

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. Mengakses dan menavigasi Google Colab
2. Membuat dan menjalankan notebook baru
3. Menulis kode Python dasar (variabel, print, list, dictionary)
4. Menginstal dan mengimpor library data science (pandas, numpy, matplotlib)
5. Memuat dataset dari URL dan melakukan eksplorasi awal

---

## Persiapan

- Akun Google (Gmail) yang aktif
- Browser modern (Chrome, Firefox, atau Edge)
- Koneksi internet yang stabil
- Tidak perlu instalasi software apapun di komputer lokal

---

## Langkah-langkah

### Langkah 1: Membuka Google Colab

1. Buka browser dan kunjungi [https://colab.research.google.com](https://colab.research.google.com)
2. Login dengan akun Google Anda
3. Klik **"New Notebook"** atau **"Notebook Baru"**
4. Ganti nama notebook menjadi: `Lab01_NamaAnda_NIM.ipynb`

> **Catatan:** Google Colab menyimpan file secara otomatis di Google Drive Anda.

### Langkah 2: Mengenal Cell di Colab

Ada dua jenis cell di Google Colab:
- **Code cell**: untuk menulis dan menjalankan kode Python
- **Text cell**: untuk menulis catatan dalam format Markdown

Coba buat satu text cell dengan isi:

```markdown
# Lab 01: Setup Python dan Google Colab
**Nama:** [Nama Anda]
**NIM:** [NIM Anda]
**Tanggal:** [Tanggal Hari Ini]
```

### Langkah 3: Python Dasar - Variabel dan Print

Jalankan kode berikut di code cell baru:

```python
# =============================================
# LANGKAH 3: Variabel dan Print
# =============================================

# Variabel string
nama = "Universitas Al Azhar Indonesia"
prodi = "Statistika dan Probabilitas"

# Variabel numerik
jumlah_mahasiswa = 35
rata_rata_ipk = 3.45

# Print sederhana
print("Selamat datang di", nama)
print(f"Mata Kuliah: {prodi}")
print(f"Jumlah Mahasiswa: {jumlah_mahasiswa}")
print(f"Rata-rata IPK: {rata_rata_ipk:.2f}")

# Operasi aritmatika dasar
a = 10
b = 3
print(f"\n--- Operasi Aritmatika ---")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.4f}")
print(f"{a} ** {b} = {a ** b}")
print(f"{a} % {b} = {a % b}")
```

### Langkah 4: Struktur Data Python

```python
# =============================================
# LANGKAH 4: List, Tuple, dan Dictionary
# =============================================

# List - koleksi data yang bisa diubah
nilai_uts = [78, 85, 92, 67, 73, 88, 95, 81, 76, 90]
print("Nilai UTS:", nilai_uts)
print(f"Jumlah data: {len(nilai_uts)}")
print(f"Nilai pertama: {nilai_uts[0]}")
print(f"Nilai terakhir: {nilai_uts[-1]}")
print(f"3 nilai tertinggi: {sorted(nilai_uts, reverse=True)[:3]}")

# Dictionary - pasangan key-value
mahasiswa = {
    "nama": "Ahmad Fauzi",
    "nim": "2024001",
    "ipk": 3.67,
    "semester": 3
}
print(f"\nData Mahasiswa:")
for key, value in mahasiswa.items():
    print(f"  {key}: {value}")

# List of dictionaries (seperti tabel)
data_kelas = [
    {"nama": "Andi", "nilai": 85},
    {"nama": "Budi", "nilai": 78},
    {"nama": "Citra", "nilai": 92},
    {"nama": "Dewi", "nilai": 88},
]

print("\nDaftar Nilai Kelas:")
for i, mhs in enumerate(data_kelas, 1):
    print(f"  {i}. {mhs['nama']}: {mhs['nilai']}")
```

### Langkah 5: Fungsi Dasar Python

```python
# =============================================
# LANGKAH 5: Fungsi (Function)
# =============================================

# Fungsi sederhana untuk menghitung rata-rata
def hitung_rata_rata(data):
    """Menghitung rata-rata dari sebuah list angka."""
    return sum(data) / len(data)

# Fungsi untuk menentukan grade
def tentukan_grade(nilai):
    """Menentukan grade berdasarkan nilai."""
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 55:
        return "C"
    elif nilai >= 40:
        return "D"
    else:
        return "E"

# Gunakan fungsi
nilai_uts = [78, 85, 92, 67, 73, 88, 95, 81, 76, 90]
rata_rata = hitung_rata_rata(nilai_uts)
print(f"Rata-rata UTS: {rata_rata:.2f}")
print(f"Grade rata-rata: {tentukan_grade(rata_rata)}")

print("\nGrade masing-masing:")
for i, n in enumerate(nilai_uts):
    print(f"  Mahasiswa {i+1}: {n} -> Grade {tentukan_grade(n)}")
```

### Langkah 6: Install dan Import Library

```python
# =============================================
# LANGKAH 6: Library untuk Data Science
# =============================================

# Library ini sudah terinstal di Google Colab
# Jika perlu install library tambahan, gunakan:
# !pip install nama_library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Verifikasi versi library
print(f"NumPy version: {np.__version__}")
print(f"Pandas version: {pd.__version__}")
import matplotlib
print(f"Matplotlib version: {matplotlib.__version__}")

print("\nSemua library berhasil diimpor!")
```

### Langkah 7: Pengenalan NumPy

```python
# =============================================
# LANGKAH 7: NumPy Dasar
# =============================================

# Membuat array dari list
nilai = np.array([78, 85, 92, 67, 73, 88, 95, 81, 76, 90])
print(f"Array: {nilai}")
print(f"Tipe data: {nilai.dtype}")
print(f"Dimensi: {nilai.ndim}")
print(f"Shape: {nilai.shape}")

# Fungsi statistik dasar NumPy
print(f"\n--- Statistik Dasar ---")
print(f"Mean: {np.mean(nilai):.2f}")
print(f"Median: {np.median(nilai):.2f}")
print(f"Std Deviasi: {np.std(nilai):.2f}")
print(f"Minimum: {np.min(nilai)}")
print(f"Maksimum: {np.max(nilai)}")

# Membuat array dengan fungsi NumPy
bilangan = np.arange(1, 11)
print(f"\nBilangan 1-10: {bilangan}")

acak = np.random.randint(1, 100, size=5)
print(f"5 bilangan acak (1-100): {acak}")
```

### Langkah 8: Memuat Dataset dari URL

```python
# =============================================
# LANGKAH 8: Memuat dan Mengeksplorasi Dataset
# =============================================

# Memuat dataset langsung dari URL
# Dataset: Iris (dataset klasik untuk belajar data science)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Tampilkan 5 baris pertama
print("=== 5 Baris Pertama ===")
print(df.head())

# Tampilkan 5 baris terakhir
print("\n=== 5 Baris Terakhir ===")
print(df.tail())

# Informasi dataset
print("\n=== Informasi Dataset ===")
print(df.info())

# Statistik deskriptif
print("\n=== Statistik Deskriptif ===")
print(df.describe())

# Jumlah data per species
print("\n=== Jumlah per Species ===")
print(df['species'].value_counts())
```

### Langkah 9: Visualisasi Sederhana

```python
# =============================================
# LANGKAH 9: Grafik Sederhana
# =============================================

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['sepal_length'], bins=15, color='steelblue', edgecolor='white')
plt.title('Distribusi Panjang Sepal (Iris Dataset)', fontsize=14)
plt.xlabel('Panjang Sepal (cm)')
plt.ylabel('Frekuensi')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# Scatter plot
plt.figure(figsize=(8, 5))
colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal_length'], subset['sepal_width'],
                label=species, c=colors[species], alpha=0.7)

plt.title('Sepal Length vs Sepal Width', fontsize=14)
plt.xlabel('Panjang Sepal (cm)')
plt.ylabel('Lebar Sepal (cm)')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Langkah 10: Menyimpan Notebook

1. Notebook otomatis tersimpan di Google Drive
2. Untuk download: **File > Download > Download .ipynb**
3. Untuk share: **Share** (pojok kanan atas) > masukkan email dosen

---

## Checklist Penyelesaian

Tandai setiap langkah yang sudah Anda selesaikan:

| No | Langkah | Selesai? |
|----|---------|----------|
| 1 | Membuat notebook baru di Google Colab | [ ] |
| 2 | Menulis text cell dengan nama dan NIM | [ ] |
| 3 | Menjalankan kode variabel dan print | [ ] |
| 4 | Menjalankan kode list dan dictionary | [ ] |
| 5 | Menjalankan kode fungsi Python | [ ] |
| 6 | Mengimpor numpy, pandas, matplotlib | [ ] |
| 7 | Menjalankan operasi NumPy dasar | [ ] |
| 8 | Memuat dataset dari URL dengan pandas | [ ] |
| 9 | Membuat histogram dan scatter plot | [ ] |
| 10 | Menyimpan dan menamai notebook | [ ] |

---

## Tugas yang Harus Dikumpulkan

Lab ini **tidak dinilai**, tetapi Anda harus menyelesaikan seluruh checklist di atas sebagai persiapan untuk lab-lab berikutnya. Pastikan semua cell berjalan tanpa error.

---

## Rubrik Singkat

| Kriteria | Keterangan |
|----------|------------|
| **Lengkap** | Semua 10 langkah selesai, semua cell berjalan tanpa error |
| **Sebagian** | 5-9 langkah selesai |
| **Belum Lengkap** | Kurang dari 5 langkah selesai |

---

## Challenge / Bonus

Bagi yang ingin tantangan lebih:

```python
# =============================================
# CHALLENGE: Eksplorasi Dataset Sendiri
# =============================================

# 1. Muat dataset tips dari seaborn
url_tips = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df_tips = pd.read_csv(url_tips)

# 2. Jawab pertanyaan berikut menggunakan kode Python:
# a. Berapa jumlah total baris dan kolom?
print(f"Jumlah baris: {df_tips.shape[0]}, Kolom: {df_tips.shape[1]}")

# b. Berapa rata-rata tip (uang tip)?
print(f"Rata-rata tip: ${df_tips['tip'].mean():.2f}")

# c. Hari apa yang paling banyak pengunjung?
print(f"Hari tersibuk: {df_tips['day'].value_counts().index[0]}")

# d. Buat satu visualisasi menarik dari dataset ini
plt.figure(figsize=(8, 5))
plt.scatter(df_tips['total_bill'], df_tips['tip'],
            alpha=0.6, c='coral', edgecolors='gray')
plt.title('Total Bill vs Tip', fontsize=14)
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---

> **Tips:** Jika mengalami error, baca pesan error dengan teliti. Biasanya pesan error memberikan petunjuk yang cukup jelas tentang masalahnya. Jangan ragu bertanya kepada dosen atau asisten lab.
