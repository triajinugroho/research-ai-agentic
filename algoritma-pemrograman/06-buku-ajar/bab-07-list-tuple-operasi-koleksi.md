# BAB 7: LIST, TUPLE, DAN OPERASI KOLEKSI

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| CPMK-5.1 | Memahami konsep list dan tuple sebagai struktur data linear | C2 (Memahami) |
| CPMK-5.2 | Menerapkan operasi CRUD pada list | C3 (Menerapkan) |
| CPMK-5.3 | Menggunakan list comprehension untuk transformasi data | C3 (Menerapkan) |
| CPMK-5.4 | Membedakan penggunaan list vs tuple berdasarkan konteks | C4 (Menganalisis) |

**Estimasi Waktu:** 3 × 50 menit (3 SKS)

**Prasyarat:** Mahasiswa telah memahami materi Bab 1–6 (variabel, kontrol, fungsi, string).

---

## 7.1 Pengenalan Struktur Data Koleksi

### 7.1.1 Mengapa Butuh Koleksi?

Bayangkan Anda ingin menyimpan nilai 40 mahasiswa dalam satu kelas. Tanpa koleksi:

```python
# TANPA KOLEKSI — 40 variabel berbeda!
nilai_1 = 85
nilai_2 = 92
nilai_3 = 78
# ... sampai ...
nilai_40 = 88
# Bagaimana menghitung rata-rata? Loop tidak mungkin!
```

Dengan koleksi:

```python
# DENGAN LIST — 1 variabel, 40 elemen!
nilai = [85, 92, 78, 95, 88, 76, 91, 83, 87, 90,
         82, 79, 94, 86, 81, 93, 77, 89, 84, 80,
         91, 85, 73, 96, 87, 82, 88, 75, 90, 86,
         84, 92, 79, 81, 93, 78, 85, 87, 91, 88]

rata_rata = sum(nilai) / len(nilai)
print(f"Rata-rata kelas: {rata_rata:.2f}")
```

**Koleksi** (collection) memungkinkan kita menyimpan **banyak data** dalam **satu variabel**, dan memprosesnya secara efisien menggunakan loop.

### 7.1.2 Jenis Koleksi di Python

Python memiliki 4 tipe koleksi built-in:

| Tipe | Ordered | Mutable | Duplikat | Contoh |
|------|---------|---------|----------|--------|
| **List** | Ya | Ya | Ya | `[1, 2, 3]` |
| **Tuple** | Ya | Tidak | Ya | `(1, 2, 3)` |
| **Dict** | Ya* | Ya | Key unik | `{"a": 1}` |
| **Set** | Tidak | Ya | Tidak | `{1, 2, 3}` |

*Dict ordered sejak Python 3.7+

Bab ini fokus pada **List** dan **Tuple**. Dictionary dan Set dibahas di Bab 8.

---

## 7.2 List: Koleksi Dinamis

### 7.2.1 Membuat List

```python
# Cara 1: Literal (langsung)
buah = ["apel", "mangga", "durian", "rambutan"]
nilai = [85, 92, 78, 95, 88]
campuran = ["Ahmad", 20, 3.75, True]  # boleh beda tipe
kosong = []

# Cara 2: Fungsi list()
huruf = list("Python")       # ['P', 'y', 't', 'h', 'o', 'n']
angka = list(range(1, 6))    # [1, 2, 3, 4, 5]
genap = list(range(2, 21, 2))  # [2, 4, 6, ..., 20]

# Cara 3: List repetition
nol = [0] * 10               # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

### 7.2.2 Indexing dan Slicing

List menggunakan **zero-based indexing** — elemen pertama ada di index 0:

```
 Positive index:   0        1        2        3        4
                ┌────────┬────────┬────────┬────────┬────────┐
  buah =        │ "apel" │"mangga"│"durian"│"rambut"│"jambu" │
                └────────┴────────┴────────┴────────┴────────┘
 Negative index:  -5       -4       -3       -2       -1
```

```python
buah = ["apel", "mangga", "durian", "rambutan", "jambu"]

# Indexing
print(buah[0])     # "apel" (pertama)
print(buah[2])     # "durian" (ketiga)
print(buah[-1])    # "jambu" (terakhir)
print(buah[-2])    # "rambutan" (kedua dari terakhir)

# Slicing: list[start:stop:step]
print(buah[1:3])   # ["mangga", "durian"] (index 1 dan 2)
print(buah[:3])    # ["apel", "mangga", "durian"] (awal sampai 2)
print(buah[2:])    # ["durian", "rambutan", "jambu"] (index 2 sampai akhir)
print(buah[::2])   # ["apel", "durian", "jambu"] (loncat 2)
print(buah[::-1])  # ["jambu", "rambutan", "durian", "mangga", "apel"] (terbalik)
```

### 7.2.3 Mutability: Mengubah Elemen

Berbeda dengan string (immutable), list bersifat **mutable** — elemennya bisa diubah:

```python
nilai = [85, 92, 78, 95, 88]

# Mengubah satu elemen
nilai[2] = 80
print(nilai)  # [85, 92, 80, 95, 88]

# Mengubah slice (beberapa elemen)
nilai[1:3] = [90, 82]
print(nilai)  # [85, 90, 82, 95, 88]
```

> **Perbandingan:**
> ```python
> teks = "Hello"
> teks[0] = "h"  # ERROR! TypeError — string immutable
>
> data = [1, 2, 3]
> data[0] = 10    # OK — list mutable
> ```

### 7.2.4 List Methods

| Method | Deskripsi | Contoh | Hasil |
|--------|-----------|--------|-------|
| `append(x)` | Tambah x di akhir | `[1,2].append(3)` | `[1,2,3]` |
| `insert(i, x)` | Sisipkan x di posisi i | `[1,3].insert(1, 2)` | `[1,2,3]` |
| `extend(iter)` | Gabungkan iterable | `[1,2].extend([3,4])` | `[1,2,3,4]` |
| `remove(x)` | Hapus x pertama | `[1,2,1].remove(1)` | `[2,1]` |
| `pop(i)` | Hapus & kembalikan index i | `[1,2,3].pop(1)` | return `2` |
| `pop()` | Hapus & kembalikan terakhir | `[1,2,3].pop()` | return `3` |
| `index(x)` | Cari index x pertama | `[1,2,3].index(2)` | `1` |
| `count(x)` | Hitung kemunculan x | `[1,2,1].count(1)` | `2` |
| `sort()` | Urutkan (in-place) | `[3,1,2].sort()` | `[1,2,3]` |
| `reverse()` | Balik urutan (in-place) | `[1,2,3].reverse()` | `[3,2,1]` |
| `copy()` | Salin list (shallow) | `a = [1,2]; b = a.copy()` | `b = [1,2]` |
| `clear()` | Kosongkan list | `[1,2].clear()` | `[]` |

```python
# Demonstrasi methods
mahasiswa = ["Ahmad", "Siti", "Budi"]

# Menambah
mahasiswa.append("Dewi")
print(mahasiswa)  # ["Ahmad", "Siti", "Budi", "Dewi"]

mahasiswa.insert(1, "Fatimah")
print(mahasiswa)  # ["Ahmad", "Fatimah", "Siti", "Budi", "Dewi"]

# Menghapus
mahasiswa.remove("Budi")
print(mahasiswa)  # ["Ahmad", "Fatimah", "Siti", "Dewi"]

terakhir = mahasiswa.pop()
print(f"Dihapus: {terakhir}")  # Dihapus: Dewi

# Mengurutkan
mahasiswa.sort()
print(mahasiswa)  # ["Ahmad", "Fatimah", "Siti"]

# Informasi
posisi = mahasiswa.index("Siti")
print(f"Siti di posisi: {posisi}")  # Siti di posisi: 2
```

### 7.2.5 Operasi pada List

```python
a = [1, 2, 3]
b = [4, 5, 6]

# Concatenation (+)
c = a + b
print(c)  # [1, 2, 3, 4, 5, 6]

# Repetition (*)
d = a * 3
print(d)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Membership (in / not in)
print(2 in a)      # True
print(7 not in a)  # True

# Fungsi bawaan
print(len(a))    # 3
print(min(a))    # 1
print(max(a))    # 3
print(sum(a))    # 6
```

### 7.2.6 Nested List (List Bersarang)

List bisa berisi list lain, membentuk **matriks** atau tabel:

```python
# Matriks 3x3
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Akses elemen
print(matriks[0])       # [1, 2, 3] (baris pertama)
print(matriks[1][2])    # 6 (baris 1, kolom 2)
print(matriks[2][0])    # 7 (baris 2, kolom 0)

# Iterasi matriks
for baris in matriks:
    for elemen in baris:
        print(f"{elemen:>3}", end="")
    print()  # baris baru

# Output:
#   1  2  3
#   4  5  6
#   7  8  9
```

**Studi kasus: Tabel nilai mahasiswa**

```python
# [nama, tugas, uts, uas]
data_nilai = [
    ["Ahmad",   85, 78, 82],
    ["Siti",    92, 88, 90],
    ["Budi",    76, 80, 78],
    ["Dewi",    95, 92, 88],
    ["Fatimah", 88, 85, 86],
]

print(f"{'Nama':<10} {'Tugas':>5} {'UTS':>5} {'UAS':>5} {'Rata':>6}")
print("-" * 38)

for mhs in data_nilai:
    nama = mhs[0]
    rata = (mhs[1] + mhs[2] + mhs[3]) / 3
    print(f"{nama:<10} {mhs[1]:>5} {mhs[2]:>5} {mhs[3]:>5} {rata:>6.1f}")
```

---

## 7.3 Iterasi pada List

### 7.3.1 For Loop pada List

```python
buah = ["apel", "mangga", "durian", "rambutan"]

# Cara 1: Langsung iterasi elemen
for b in buah:
    print(f"  Saya suka {b}")

# Cara 2: Iterasi dengan index
for i in range(len(buah)):
    print(f"  {i+1}. {buah[i]}")
```

### 7.3.2 While Loop pada List

```python
# Menghapus elemen satu per satu (processing queue)
antrian = ["Pasien A", "Pasien B", "Pasien C", "Pasien D"]

while antrian:
    pasien = antrian.pop(0)
    print(f"  Melayani: {pasien}")
    print(f"  Sisa antrian: {len(antrian)}")
```

### 7.3.3 Enumerate() — Index + Value

```python
mahasiswa = ["Ahmad", "Siti", "Budi", "Dewi", "Fatimah"]

for nomor, nama in enumerate(mahasiswa, start=1):
    print(f"  {nomor}. {nama}")

# Output:
#   1. Ahmad
#   2. Siti
#   3. Budi
#   4. Dewi
#   5. Fatimah
```

### 7.3.4 Zip() — Iterasi Paralel

```python
nama = ["Ahmad", "Siti", "Budi"]
nilai = [85, 92, 78]
kota = ["Jakarta", "Bandung", "Surabaya"]

for n, v, k in zip(nama, nilai, kota):
    print(f"  {n} ({k}): {v}")

# Output:
#   Ahmad (Jakarta): 85
#   Siti (Bandung): 92
#   Budi (Surabaya): 78
```

---

## 7.4 List Comprehension

### 7.4.1 Sintaks Dasar

**List comprehension** adalah cara ringkas untuk membuat list baru dari iterable:

```python
# Sintaks: [ekspresi for variabel in iterable]

# Tanpa list comprehension
kuadrat = []
for x in range(1, 6):
    kuadrat.append(x ** 2)

# Dengan list comprehension — 1 baris!
kuadrat = [x ** 2 for x in range(1, 6)]
print(kuadrat)  # [1, 4, 9, 16, 25]
```

```python
# Contoh lain
nama = ["ahmad", "siti", "budi"]
nama_kapital = [n.title() for n in nama]
print(nama_kapital)  # ["Ahmad", "Siti", "Budi"]

# Konversi suhu (Celsius → Fahrenheit)
celsius = [0, 10, 20, 30, 40]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]
```

### 7.4.2 Conditional Comprehension

```python
# Sintaks: [ekspresi for variabel in iterable if kondisi]

nilai = [85, 62, 78, 95, 58, 88, 72, 45, 91, 80]

# Filter: hanya yang lulus (>= 60)
lulus = [n for n in nilai if n >= 60]
print(f"Lulus: {lulus}")  # [85, 62, 78, 95, 88, 72, 91, 80]

# Filter + transformasi
nilai_huruf = ["Lulus" if n >= 60 else "Tidak Lulus" for n in nilai]
print(nilai_huruf)

# Bilangan genap dari 1-20
genap = [x for x in range(1, 21) if x % 2 == 0]
print(genap)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

### 7.4.3 Nested Comprehension

```python
# Tabel perkalian 3x3
tabel = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(tabel)  # [[1,2,3], [2,4,6], [3,6,9]]

# Flatten nested list
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = [x for sub in nested for x in sub]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 7.4.4 Perbandingan: Loop vs Comprehension

| Aspek | Loop Tradisional | List Comprehension |
|-------|------------------|--------------------|
| Baris kode | 3-4 baris | 1 baris |
| Readability (sederhana) | Baik | Sangat baik |
| Readability (kompleks) | Lebih jelas | Bisa sulit dibaca |
| Performa | Sedikit lebih lambat | Sedikit lebih cepat |
| Kapan digunakan | Logika kompleks | Transformasi sederhana |

> **Best Practice:** Gunakan list comprehension untuk operasi **sederhana** (1 kondisi, 1 transformasi). Untuk logika yang kompleks, gunakan loop biasa — keterbacaan lebih penting daripada keringkasan.

---

## 7.5 Tuple: Koleksi Immutable

### 7.5.1 Membuat Tuple

```python
# Tuple menggunakan tanda kurung ()
koordinat = (3, 5)
warna_rgb = (255, 128, 0)
mahasiswa = ("Ahmad", "2025001", "Informatika")
singleton = (42,)  # tuple 1 elemen — WAJIB ada koma!
kosong = ()

# Tanpa kurung juga bisa (tuple packing)
titik = 3, 5
print(type(titik))  # <class 'tuple'>
```

### 7.5.2 Immutability

Tuple **tidak bisa diubah** setelah dibuat:

```python
buah = ("apel", "mangga", "durian")

# TIDAK BISA mengubah elemen
# buah[0] = "jeruk"  # TypeError: 'tuple' does not support item assignment

# TIDAK BISA menambah/menghapus
# buah.append("jeruk")  # AttributeError: 'tuple' has no attribute 'append'

# TAPI BISA mengakses dan slicing (read-only)
print(buah[0])     # "apel"
print(buah[1:])    # ("mangga", "durian")
print(len(buah))   # 3
```

### 7.5.3 Kapan Menggunakan Tuple vs List

| Kriteria | List | Tuple |
|----------|------|-------|
| **Data berubah?** | Ya — gunakan list | Tidak — gunakan tuple |
| **Contoh** | Daftar mahasiswa (bisa tambah/hapus) | Koordinat (x, y) |
| **Performa** | Sedikit lebih lambat | Sedikit lebih cepat |
| **Memory** | Lebih besar | Lebih kecil |
| **Hashable** | Tidak (tidak bisa jadi dict key) | Ya (bisa jadi dict key) |
| **Keamanan** | Data bisa diubah | Data aman dari perubahan |

**Aturan praktis:**
- Gunakan **tuple** untuk data yang **tetap** (fixed): koordinat, konfigurasi, return value fungsi
- Gunakan **list** untuk data yang **berubah** (dynamic): daftar mahasiswa, antrian, keranjang belanja

### 7.5.4 Tuple Unpacking

```python
# Tuple unpacking — assign ke beberapa variabel sekaligus
koordinat = (3, 5)
x, y = koordinat
print(f"x = {x}, y = {y}")  # x = 3, y = 5

# Multiple return values dari fungsi (sebenarnya tuple!)
def hitung_statistik(data):
    return min(data), max(data), sum(data) / len(data)

minimum, maksimum, rata = hitung_statistik([85, 92, 78, 95, 88])
print(f"Min: {minimum}, Max: {maksimum}, Rata: {rata:.1f}")

# Swap variabel — Python style!
a, b = 10, 20
a, b = b, a
print(f"a = {a}, b = {b}")  # a = 20, b = 10

# Unpacking dengan * (rest)
pertama, *sisanya = [1, 2, 3, 4, 5]
print(pertama)  # 1
print(sisanya)  # [2, 3, 4, 5]
```

### 7.5.5 Named Tuple (Pengenalan)

Untuk tuple yang lebih deskriptif:

```python
from collections import namedtuple

# Definisikan named tuple
Mahasiswa = namedtuple('Mahasiswa', ['nama', 'nim', 'ipk'])

# Buat instance
mhs1 = Mahasiswa("Ahmad", "2025001", 3.75)
mhs2 = Mahasiswa("Siti", "2025002", 3.90)

# Akses via nama field (lebih jelas dari index)
print(mhs1.nama)  # "Ahmad"
print(mhs2.ipk)   # 3.90

# Tetap bisa akses via index
print(mhs1[0])    # "Ahmad"
```

---

## 7.6 Pola-pola Umum dengan Koleksi

### 7.6.1 Filtering (Menyaring Data)

```python
nilai = [85, 62, 78, 95, 58, 88, 72, 45, 91, 80]

# Pola: buat list baru berdasarkan kondisi
lulus = [n for n in nilai if n >= 60]
tidak_lulus = [n for n in nilai if n < 60]

print(f"Lulus ({len(lulus)}): {lulus}")
print(f"Tidak lulus ({len(tidak_lulus)}): {tidak_lulus}")
```

### 7.6.2 Mapping (Transformasi Data)

```python
harga = [15000, 25000, 8000, 32000, 12000]

# Semua harga naik 10%
harga_baru = [h * 1.1 for h in harga]
print(harga_baru)  # [16500.0, 27500.0, ...]

# Format ke Rupiah
harga_rp = [f"Rp {h:,.0f}" for h in harga]
print(harga_rp)  # ['Rp 15,000', 'Rp 25,000', ...]
```

### 7.6.3 Reducing / Accumulating

```python
nilai = [85, 92, 78, 95, 88]

# Pola akumulator — menghitung total
total = 0
for n in nilai:
    total += n
rata_rata = total / len(nilai)

# Atau langsung: sum() dan len()
rata_rata = sum(nilai) / len(nilai)
print(f"Rata-rata: {rata_rata:.2f}")

# Mencari minimum manual (tanpa min())
minimum = nilai[0]
for n in nilai[1:]:
    if n < minimum:
        minimum = n
print(f"Minimum: {minimum}")
```

### 7.6.4 Searching dalam List

```python
mahasiswa = ["Ahmad", "Siti", "Budi", "Dewi", "Fatimah"]

# Linear search — cari nama
target = "Dewi"
ditemukan = False
for i, nama in enumerate(mahasiswa):
    if nama == target:
        print(f"{target} ditemukan di posisi {i}")
        ditemukan = True
        break

if not ditemukan:
    print(f"{target} tidak ditemukan")

# Cara Pythonic: operator 'in'
if "Dewi" in mahasiswa:
    posisi = mahasiswa.index("Dewi")
    print(f"Dewi ada di posisi {posisi}")
```

---

## 7.7 Studi Kasus: Sistem Nilai Mahasiswa

```python
# ============================================================
# SISTEM PENGELOLAAN NILAI MAHASISWA
# Algoritma dan Pemrograman — UAI
# ============================================================

def input_data_mahasiswa(n):
    """Meminta input data n mahasiswa."""
    data = []
    for i in range(n):
        print(f"\nMahasiswa ke-{i+1}:")
        nama = input("  Nama  : ")
        nim = input("  NIM   : ")
        nilai = float(input("  Nilai : "))
        data.append((nama, nim, nilai))
    return data

def hitung_statistik(data):
    """Menghitung statistik kelas."""
    semua_nilai = [mhs[2] for mhs in data]
    return {
        'rata_rata': sum(semua_nilai) / len(semua_nilai),
        'tertinggi': max(semua_nilai),
        'terendah': min(semua_nilai),
        'jumlah_lulus': sum(1 for n in semua_nilai if n >= 60),
        'jumlah_tidak_lulus': sum(1 for n in semua_nilai if n < 60),
    }

def urutkan_nilai(data, descending=True):
    """Mengurutkan data berdasarkan nilai."""
    return sorted(data, key=lambda x: x[2], reverse=descending)

def konversi_huruf(nilai):
    """Konversi nilai angka ke huruf."""
    if nilai >= 85: return "A"
    elif nilai >= 80: return "A-"
    elif nilai >= 75: return "B+"
    elif nilai >= 70: return "B"
    elif nilai >= 65: return "B-"
    elif nilai >= 60: return "C+"
    elif nilai >= 55: return "C"
    elif nilai >= 50: return "D"
    else: return "E"

def tampilkan_tabel(data):
    """Menampilkan data dalam format tabel."""
    print(f"\n{'No':>3} {'Nama':<15} {'NIM':<12} {'Nilai':>5} {'Huruf':>5}")
    print("-" * 45)
    for i, (nama, nim, nilai) in enumerate(data, 1):
        huruf = konversi_huruf(nilai)
        print(f"{i:>3} {nama:<15} {nim:<12} {nilai:>5.1f} {huruf:>5}")

def tampilkan_statistik(stat):
    """Menampilkan statistik kelas."""
    print(f"\n{'='*35}")
    print(f"  STATISTIK KELAS")
    print(f"{'='*35}")
    print(f"  Rata-rata      : {stat['rata_rata']:.2f}")
    print(f"  Nilai tertinggi: {stat['tertinggi']:.1f}")
    print(f"  Nilai terendah : {stat['terendah']:.1f}")
    print(f"  Jumlah lulus   : {stat['jumlah_lulus']}")
    print(f"  Tidak lulus    : {stat['jumlah_tidak_lulus']}")

def main():
    """Fungsi utama."""
    # Data contoh (hardcoded untuk demo)
    data = [
        ("Ahmad",   "2025001", 85),
        ("Siti",    "2025002", 92),
        ("Budi",    "2025003", 68),
        ("Dewi",    "2025004", 95),
        ("Fatimah", "2025005", 78),
        ("Hasan",   "2025006", 55),
        ("Rina",    "2025007", 88),
        ("Umar",    "2025008", 72),
    ]

    print("SISTEM PENGELOLAAN NILAI MAHASISWA")
    print("Mata Kuliah: Algoritma dan Pemrograman\n")

    # Tampilkan tabel (urut berdasarkan nilai tertinggi)
    data_terurut = urutkan_nilai(data)
    tampilkan_tabel(data_terurut)

    # Statistik
    stat = hitung_statistik(data)
    tampilkan_statistik(stat)

    # Filter: mahasiswa dengan predikat A
    top_students = [(n, nim, v) for n, nim, v in data if v >= 85]
    print(f"\nMahasiswa predikat A: {[m[0] for m in top_students]}")

main()
```

---

## AI Corner: AI untuk Operasi Data

**Level: Menengah**

### Meminta AI Generate List Comprehension

```
Prompt: "Konversikan loop berikut menjadi list comprehension:
hasil = []
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        hasil.append(x)
"
```

### Debugging Operasi Koleksi dengan AI

```
Prompt: "Kode saya menghasilkan IndexError:
data = [1, 2, 3]
print(data[3])
Jelaskan mengapa dan bagaimana memperbaikinya."
```

### Validasi Output AI

Selalu verifikasi kode list comprehension dari AI:
1. Bandingkan output dengan loop tradisional
2. Test dengan data kosong `[]`
3. Test dengan data 1 elemen
4. Pastikan logika filter benar

---

## Latihan Soal

### Tingkat Dasar

1. Buatlah list berisi nama 5 kota di Indonesia, lalu tampilkan elemen pertama, terakhir, dan 3 elemen tengah menggunakan slicing.

2. Buatlah program yang meminta input 5 angka dari pengguna, simpan dalam list, lalu tampilkan total, rata-rata, minimum, dan maksimum.

3. Buatlah list berisi angka 1-20. Gunakan list comprehension untuk membuat list baru berisi hanya bilangan ganjil.

4. Jelaskan perbedaan antara `append()` dan `extend()`. Berikan contoh masing-masing.

5. Buatlah tuple berisi 3 mata kuliah favorit Anda. Coba ubah salah satu elemennya — apa yang terjadi? Jelaskan.

### Tingkat Menengah

1. Buatlah program yang menyimpan data 5 barang di warung (nama, harga) dalam list of tuples. Tampilkan daftar barang, hitung total belanja, dan tampilkan barang termahal dan termurah.

2. Diberikan matriks 3×3 sebagai nested list, buatlah fungsi yang menghitung jumlah setiap baris, setiap kolom, dan diagonal.

3. Buatlah program yang menerima sebuah kalimat, memecahnya menjadi list kata, lalu urutkan secara alfabet menggunakan `sorted()`. Tampilkan 3 kata pertama dan 3 kata terakhir.

4. Gunakan `zip()` untuk menggabungkan dua list: `nama = ["Ahmad", "Siti", "Budi"]` dan `nilai = [85, 92, 78]` menjadi list of tuples. Lalu urutkan berdasarkan nilai (tertinggi ke terendah).

5. Buatlah fungsi `flatten(nested_list)` yang mengubah nested list menjadi flat list. Contoh: `[[1,2],[3,4,5],[6]]` → `[1,2,3,4,5,6]`.

### Tingkat Mahir

1. Buatlah program manajemen nilai mahasiswa lengkap: (a) Input data n mahasiswa (nama, NIM, 3 komponen nilai), (b) Hitung rata-rata dan grade per mahasiswa, (c) Urutkan berdasarkan rata-rata (descending), (d) Tampilkan statistik kelas, (e) Ekspor dalam format tabel rapi.

2. Implementasikan Matrix Multiplication untuk dua matriks 2×2 menggunakan nested list. Tunjukkan langkah perhitungan.

3. Buatlah program yang mensimulasikan **antrian kasir** di minimarket: pelanggan bisa masuk antrian (append), dilayani (pop dari depan), dan status antrian ditampilkan. Gunakan list sebagai queue.

---

## Rangkuman

- **List** adalah koleksi **mutable**, ordered, dan bisa berisi duplikat. Dibuat dengan `[]`.
- **Tuple** adalah koleksi **immutable**, ordered, lebih aman dan sedikit lebih cepat. Dibuat dengan `()`.
- List mendukung operasi CRUD: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`.
- **Indexing** dimulai dari 0; negative indexing dimulai dari -1.
- **Slicing** dengan sintaks `list[start:stop:step]`.
- **List comprehension** `[expr for x in iter if cond]` adalah cara ringkas membuat list baru.
- **Enumerate** memberikan index + value; **zip** iterasi paralel beberapa list.
- **Tuple unpacking** memungkinkan assignment ke beberapa variabel: `x, y = (3, 5)`.
- **Nested list** digunakan untuk data tabular/matriks.
- Gunakan **list** untuk data yang berubah, **tuple** untuk data yang tetap.

---

## Referensi

1. Downey, A. B. (2024). *Think Python* (3rd ed.). O'Reilly Media. Bab tentang Lists dan Tuples.
2. Python Software Foundation. (2026). Data Structures. https://docs.python.org/3/tutorial/datastructures.html
3. Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.). MIT Press.
4. Lutz, M. (2023). *Learning Python* (6th ed.). O'Reilly Media.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
