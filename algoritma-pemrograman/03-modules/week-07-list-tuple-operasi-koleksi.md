# Minggu 7: List, Tuple, dan Operasi Koleksi

## Informasi Modul

| Komponen       | Detail                                                              |
|----------------|---------------------------------------------------------------------|
| Mata Kuliah    | Algoritma dan Pemrograman (3 SKS)                                   |
| Minggu         | 7 (Tujuh)                                                          |
| Topik          | List, Tuple, dan Operasi Koleksi                                    |
| CPMK           | CPMK-5: Mampu menggunakan struktur data koleksi untuk mengelola data |
| Sub-CPMK       | CPMK-5.1, CPMK-5.2, CPMK-5.3, CPMK-5.4                           |
| Durasi         | 150 menit                                                           |
| Metode         | Ceramah, live coding, praktikum                                     |
| Pengajar       | Tri Aji Nugroho, S.T., M.T.                                        |
| Program Studi  | Informatika, Universitas Al Azhar Indonesia                         |
| Semester       | Genap 2025/2026                                                     |
| Bahasa         | Python                                                              |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Memanipulasi** list menggunakan operasi CRUD (Create, Read, Update, Delete), methods bawaan, dan teknik slicing (CPMK-5.1).
2. **Membangun** list comprehension untuk transformasi dan filtering data secara efisien (CPMK-5.2).
3. **Membedakan** karakteristik list dan tuple, serta menerapkan tuple packing/unpacking dalam program (CPMK-5.3).
4. **Menggunakan** fungsi bawaan Python (`len`, `sum`, `min`, `max`, `sorted`, `enumerate`, `zip`) untuk mengolah data koleksi (CPMK-5.4).

---

## Materi Pembelajaran

### 7.1 List: Struktur Data Dinamis

List adalah struktur data yang **mutable** (dapat diubah), terurut, dan dapat menyimpan elemen dengan tipe data campuran.

```python
# Membuat list
nilai = [85, 90, 78, 92, 88]
campuran = ["Ahmad", 20, True, 3.14]
kosong = []

# Operasi CRUD
# Create - menambahkan elemen
nilai.append(95)             # tambah di akhir: [85, 90, 78, 92, 88, 95]
nilai.insert(0, 100)         # sisip di indeks 0: [100, 85, 90, 78, 92, 88, 95]

# Read - mengakses elemen
print(nilai[0])              # 100 (elemen pertama)
print(nilai[-1])             # 95 (elemen terakhir)
print(nilai[1:4])            # [85, 90, 78] (slicing)

# Update - mengubah elemen
nilai[0] = 80                # ubah elemen indeks 0

# Delete - menghapus elemen
nilai.remove(78)             # hapus berdasarkan nilai
del nilai[0]                 # hapus berdasarkan indeks
elemen = nilai.pop()         # hapus dan kembalikan elemen terakhir
```

### 7.2 List Methods

| Method               | Keterangan                                | Contoh                      |
|----------------------|-------------------------------------------|-----------------------------|
| `append(x)`          | Tambah elemen di akhir                    | `lst.append(10)`            |
| `insert(i, x)`       | Sisipkan elemen di indeks `i`             | `lst.insert(0, 5)`          |
| `remove(x)`          | Hapus kemunculan pertama dari `x`         | `lst.remove(10)`            |
| `pop(i)`             | Hapus dan kembalikan elemen di indeks `i` | `lst.pop()`                 |
| `sort()`             | Urutkan list (in-place, ascending)        | `lst.sort()`                |
| `reverse()`          | Balik urutan list (in-place)              | `lst.reverse()`             |
| `index(x)`           | Kembalikan indeks pertama dari `x`        | `lst.index(10)`             |
| `count(x)`           | Hitung kemunculan `x` dalam list          | `lst.count(10)`             |
| `extend(iterable)`   | Tambahkan semua elemen dari iterable      | `lst.extend([1, 2, 3])`    |
| `copy()`             | Buat salinan dangkal (shallow copy)       | `lst2 = lst.copy()`         |

### 7.3 List Comprehension

List comprehension adalah cara ringkas dan Pythonic untuk membuat list baru dari iterable yang ada:

```python
# Sintaks: [ekspresi for item in iterable if kondisi]

# Contoh 1: kuadrat bilangan 1-10
kuadrat = [x**2 for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Contoh 2: filter bilangan genap
genap = [x for x in range(1, 21) if x % 2 == 0]
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Contoh 3: transformasi string
nama_list = ["ahmad", "budi", "citra"]
kapital = [nama.capitalize() for nama in nama_list]
# ['Ahmad', 'Budi', 'Citra']

# Contoh 4: list comprehension dengan kondisi ganda
fizzbuzz = [
    "FizzBuzz" if x % 15 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else x
    for x in range(1, 16)
]
```

### 7.4 Nested List (List 2 Dimensi)

```python
# Matriks 3x3
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Akses elemen: matriks[baris][kolom]
print(matriks[0][0])    # 1 (baris 0, kolom 0)
print(matriks[1][2])    # 6 (baris 1, kolom 2)

# Iterasi seluruh elemen
for baris in matriks:
    for elemen in baris:
        print(elemen, end=" ")
    print()

# Tabel nilai mahasiswa
tabel_nilai = [
    ["Ahmad", 85, 90, 88],
    ["Budi",  78, 82, 80],
    ["Citra", 92, 95, 93]
]

for mhs in tabel_nilai:
    rata_rata = sum(mhs[1:]) / len(mhs[1:])
    print(f"{mhs[0]}: rata-rata = {rata_rata:.1f}")
```

### 7.5 Tuple: Sequence Immutable

Tuple mirip list tetapi bersifat **immutable** — tidak bisa diubah setelah dibuat. Cocok untuk data yang tidak boleh berubah.

```python
# Membuat tuple
koordinat = (3, 5)
warna_rgb = (255, 128, 0)
singleton = (42,)          # tuple satu elemen perlu koma

# Tuple packing dan unpacking
titik = (10, 20)           # packing
x, y = titik               # unpacking
print(f"x={x}, y={y}")     # x=10, y=20

# Swap menggunakan tuple unpacking
a, b = 5, 10
a, b = b, a                # a=10, b=5

# Tuple sebagai return value fungsi
def min_max(data):
    return min(data), max(data)

lo, hi = min_max([3, 1, 4, 1, 5, 9])
```

| Aspek         | List                      | Tuple                      |
|---------------|---------------------------|----------------------------|
| Sintaks       | `[1, 2, 3]`              | `(1, 2, 3)`               |
| Mutability    | Mutable (bisa diubah)     | Immutable (tidak bisa diubah) |
| Kecepatan     | Lebih lambat              | Lebih cepat                |
| Penggunaan    | Data yang berubah         | Data tetap (konstanta)     |
| Method        | Banyak (append, sort, dll)| Sedikit (count, index)     |

### 7.6 Fungsi Bawaan untuk Koleksi

```python
data = [45, 78, 23, 91, 56, 34, 67]

print(len(data))           # 7 (jumlah elemen)
print(sum(data))           # 394 (total)
print(min(data))           # 23 (minimum)
print(max(data))           # 91 (maksimum)
print(sorted(data))        # [23, 34, 45, 56, 67, 78, 91] (list baru terurut)

# enumerate: iterasi dengan indeks
buah = ["apel", "mangga", "jeruk"]
for i, item in enumerate(buah):
    print(f"{i+1}. {item}")

# zip: menggabungkan dua iterable
nama = ["Ahmad", "Budi", "Citra"]
nilai = [85, 90, 78]
for n, v in zip(nama, nilai):
    print(f"{n}: {v}")
```

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Membaca materi modul Minggu 7 tentang list, tuple, dan operasi koleksi.
- Mencoba membuat list sederhana dan melakukan 3 operasi berbeda di Google Colab.
- Menyiapkan pertanyaan tentang perbedaan list dan tuple.

### In-class (120 menit)

| Waktu (menit) | Kegiatan                                                      | Metode           |
|----------------|--------------------------------------------------------------|------------------|
| 0 -- 10        | Review pre-class dan tanya jawab pembuka                      | Diskusi          |
| 10 -- 35       | Ceramah: list (CRUD, methods, slicing), nested list            | Ceramah          |
| 35 -- 55       | Live coding: data processing — analisis nilai mahasiswa        | Demonstrasi      |
| 55 -- 65       | Istirahat                                                     | —                |
| 65 -- 80       | Ceramah: list comprehension, tuple, fungsi bawaan koleksi      | Ceramah          |
| 80 -- 105      | Praktikum: latihan list comprehension dan pengolahan data      | Praktikum        |
| 105 -- 115     | Kuis K2 (15 menit, mencakup materi Minggu 5--7)               | Kuis             |
| 115 -- 120     | Pengantar Tugas T4 dan persiapan UTS                          | Ceramah          |

### Post-class (15 menit)
- Mengerjakan Tugas T4 (lihat bagian Penugasan).
- Review ulang materi Minggu 5--7 sebagai persiapan UTS.
- Mencoba tantangan tambahan: implementasi matriks sederhana menggunakan nested list.

---

## Penugasan

### Tugas T4: Data Processing with Collections

| Komponen         | Detail                                                         |
|------------------|----------------------------------------------------------------|
| Jenis            | Tugas Individu                                                 |
| Bobot            | Sesuai RPS                                                     |
| Deadline         | Minggu 8 (sebelum UTS)                                        |
| Submission       | Google Colab notebook via LMS                                  |

**Deskripsi:**
Mahasiswa diberikan dataset sederhana berupa list of lists yang berisi data penjualan toko (nama produk, kategori, harga, jumlah terjual). Mahasiswa diminta untuk:

1. Menghitung total penjualan per kategori menggunakan loop dan list.
2. Membuat list comprehension untuk memfilter produk dengan penjualan di atas rata-rata.
3. Mengurutkan data berdasarkan total penjualan (harga x jumlah) secara descending.
4. Menampilkan laporan ringkasan menggunakan f-string formatting yang rapi.

**Kriteria Penilaian:**

| Kriteria                            | Bobot |
|-------------------------------------|-------|
| Ketepatan logika dan hasil          | 30%   |
| Penggunaan list comprehension       | 25%   |
| Pemanfaatan fungsi bawaan koleksi   | 20%   |
| Format output dan keterbacaan kode  | 15%   |
| Kerapihan dan komentar              | 10%   |

### Kuis K2: Modularitas (Minggu 5--7)

| Komponen         | Detail                                                         |
|------------------|----------------------------------------------------------------|
| Jenis            | Kuis Individu (di kelas)                                      |
| Durasi           | 15 menit                                                       |
| Cakupan          | Fungsi, string, list, tuple (Minggu 5--7)                      |
| Format           | 5 soal pilihan ganda + 2 soal code tracing                    |

---

## Referensi

1. Downey, A. (2015). *Think Python: How to Think Like a Computer Scientist*, 2nd Edition. O'Reilly Media. — Chapter 10: Lists, Chapter 12: Tuples.
2. Matthes, E. (2023). *Python Crash Course*, 3rd Edition. No Starch Press. — Chapter 3: Introducing Lists, Chapter 4: Working with Lists.
3. Python Software Foundation. "Data Structures." *Python 3 Documentation*. [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)
4. Sweigart, A. (2019). *Automate the Boring Stuff with Python*, 2nd Edition. No Starch Press. — Chapter 4: Lists.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
