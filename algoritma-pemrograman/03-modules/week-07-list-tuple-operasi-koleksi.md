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

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Memanipulasi** list menggunakan operasi CRUD, methods bawaan, dan slicing (CPMK-5.1).
2. **Membangun** list comprehension untuk transformasi dan filtering data secara efisien (CPMK-5.2).
3. **Membedakan** list dan tuple serta menerapkan tuple packing/unpacking dalam program (CPMK-5.3).
4. **Menggunakan** fungsi bawaan (`len`, `sum`, `min`, `max`, `sorted`, `enumerate`, `zip`) untuk mengolah koleksi (CPMK-5.4).

---

## Materi Pembelajaran

### 7.1 List: Struktur Data Dinamis

List adalah struktur data **mutable**, terurut, dan dapat menyimpan elemen bertipe campuran.

```python
nilai = [85, 90, 78, 92, 88]

# Create
nilai.append(95)           # tambah di akhir
nilai.insert(0, 100)       # sisip di indeks 0

# Read
print(nilai[0])            # elemen pertama
print(nilai[1:4])          # slicing

# Update
nilai[0] = 80

# Delete
nilai.remove(78)           # hapus berdasarkan nilai
del nilai[0]               # hapus berdasarkan indeks
elemen = nilai.pop()       # hapus & kembalikan elemen terakhir
```

| Method            | Keterangan                            |
|-------------------|---------------------------------------|
| `append(x)`       | Tambah elemen di akhir                |
| `insert(i, x)`    | Sisipkan elemen di indeks `i`         |
| `remove(x)`       | Hapus kemunculan pertama `x`          |
| `pop(i)`          | Hapus & kembalikan elemen indeks `i`  |
| `sort()`          | Urutkan list (in-place)              |
| `reverse()`       | Balik urutan (in-place)              |
| `index(x)`        | Indeks pertama dari `x`              |
| `count(x)`        | Hitung kemunculan `x`                |

### 7.2 List Comprehension

```python
# Sintaks: [ekspresi for item in iterable if kondisi]
kuadrat = [x**2 for x in range(1, 11)]
genap = [x for x in range(1, 21) if x % 2 == 0]
kapital = [nama.capitalize() for nama in ["ahmad", "budi", "citra"]]
```

### 7.3 Nested List (List 2D)

```python
matriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriks[1][2])    # 6 (baris 1, kolom 2)

tabel = [["Ahmad", 85, 90], ["Budi", 78, 82], ["Citra", 92, 95]]
for mhs in tabel:
    rata = sum(mhs[1:]) / len(mhs[1:])
    print(f"{mhs[0]}: {rata:.1f}")
```

### 7.4 Tuple: Sequence Immutable

Tuple mirip list tetapi **immutable** -- cocok untuk data yang tidak boleh berubah.

```python
koordinat = (3, 5)
warna_rgb = (255, 128, 0)

# Packing & unpacking
x, y = koordinat
a, b = 5, 10
a, b = b, a           # swap

# Tuple sebagai return value
def min_max(data):
    return min(data), max(data)
lo, hi = min_max([3, 1, 4, 1, 5])
```

| Aspek       | List                       | Tuple                         |
|-------------|----------------------------|-------------------------------|
| Sintaks     | `[1, 2, 3]`               | `(1, 2, 3)`                  |
| Mutability  | Mutable                    | Immutable                     |
| Kecepatan   | Lebih lambat               | Lebih cepat                   |
| Penggunaan  | Data yang berubah          | Data tetap (konstanta)        |

### 7.5 Fungsi Bawaan untuk Koleksi

```python
data = [45, 78, 23, 91, 56]
print(len(data))          # 5
print(sum(data))          # 293
print(min(data))          # 23
print(max(data))          # 91
print(sorted(data))       # [23, 45, 56, 78, 91]

# enumerate & zip
buah = ["apel", "mangga", "jeruk"]
for i, item in enumerate(buah):
    print(f"{i+1}. {item}")

nama = ["Ahmad", "Budi", "Citra"]
nilai = [85, 90, 78]
for n, v in zip(nama, nilai):
    print(f"{n}: {v}")
```

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Membaca materi modul Minggu 7 tentang list, tuple, dan operasi koleksi.
- Mencoba membuat list dan melakukan 3 operasi berbeda di Google Colab.
- Menyiapkan pertanyaan tentang perbedaan list dan tuple.

### In-class (120 menit)

| Waktu (menit) | Kegiatan                                               | Metode      |
|----------------|-------------------------------------------------------|-------------|
| 0 -- 10        | Review pre-class dan tanya jawab pembuka               | Diskusi     |
| 10 -- 35       | Ceramah: list CRUD, methods, slicing, nested list      | Ceramah     |
| 35 -- 55       | Live coding: data processing -- analisis nilai          | Demonstrasi |
| 55 -- 65       | Istirahat                                              | --          |
| 65 -- 80       | Ceramah: list comprehension, tuple, fungsi bawaan      | Ceramah     |
| 80 -- 105      | Praktikum: latihan list comprehension & pengolahan data | Praktikum   |
| 105 -- 115     | Kuis K2 (15 menit, materi Minggu 5--7)                 | Kuis        |
| 115 -- 120     | Pengantar Tugas T4 dan persiapan UTS                   | Ceramah     |

### Post-class (15 menit)
- Mengerjakan Tugas T4.
- Review materi Minggu 5--7 sebagai persiapan UTS.
- Tantangan tambahan: implementasi matriks sederhana dengan nested list.

---

## Penugasan

### Tugas T4: Data Processing with Collections

| Komponen   | Detail                              |
|------------|--------------------------------------|
| Jenis      | Tugas Individu                       |
| Deadline   | Minggu 8 (sebelum UTS)              |
| Submission | Google Colab notebook via LMS        |

**Deskripsi:** Diberikan dataset berupa list of lists (data penjualan: nama produk, kategori, harga, jumlah terjual). Mahasiswa diminta: (1) hitung total penjualan per kategori, (2) filter produk di atas rata-rata dengan list comprehension, (3) urutkan berdasarkan total penjualan descending, (4) tampilkan laporan ringkasan dengan f-string.

| Kriteria                          | Bobot |
|-----------------------------------|-------|
| Ketepatan logika dan hasil        | 30%   |
| Penggunaan list comprehension     | 25%   |
| Pemanfaatan fungsi bawaan koleksi | 20%   |
| Format output dan keterbacaan     | 15%   |
| Kerapihan dan komentar            | 10%   |

### Kuis K2: Modularitas (Minggu 5--7)

| Komponen | Detail                                            |
|----------|---------------------------------------------------|
| Jenis    | Kuis Individu (di kelas)                          |
| Durasi   | 15 menit                                          |
| Cakupan  | Fungsi, string, list, tuple (Minggu 5--7)          |
| Format   | 5 soal pilihan ganda + 2 soal code tracing        |

---

## Referensi

1. Downey, A. (2015). *Think Python*, 2nd Ed. O'Reilly. -- Ch. 10: Lists, Ch. 12: Tuples.
2. Matthes, E. (2023). *Python Crash Course*, 3rd Ed. No Starch Press. -- Ch. 3-4: Lists.
3. Python Docs. "Data Structures." [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)
4. Sweigart, A. (2019). *Automate the Boring Stuff with Python*, 2nd Ed. -- Ch. 4: Lists.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
