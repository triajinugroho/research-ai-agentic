# Lab 07: Collections dan Iteration

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Durasi** | 75 menit |
| **Prasyarat** | Lab 06 — String Processing |

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:
- Membuat dan memanipulasi list beserta method-nya
- Menggunakan list comprehension untuk membuat list secara ringkas
- Memahami tuple dan teknik unpacking
- Membangun sistem informasi nilai mahasiswa menggunakan collections

---

## Persiapan

1. Buka Google Colab dan buat notebook baru
2. Beri nama `Lab07_NamaAnda_NIM.ipynb`
3. Pastikan Anda telah memahami fungsi dan string processing

---

## Langkah-langkah

### Langkah 1 — Membuat dan Mengakses List

```python
# Membuat list
mahasiswa = ["Aisyah", "Budi", "Citra", "Dani", "Eka"]
nilai = [85, 92, 78, 65, 88]
campuran = ["Informatika", 2025, 3.75, True]

print(f"Daftar mahasiswa : {mahasiswa}")
print(f"Daftar nilai     : {nilai}")
print(f"List campuran    : {campuran}")

# Indexing
print(f"\nMahasiswa pertama  : {mahasiswa[0]}")
print(f"Mahasiswa terakhir : {mahasiswa[-1]}")

# Slicing
print(f"3 mahasiswa pertama: {mahasiswa[:3]}")
print(f"Urutan terbalik    : {mahasiswa[::-1]}")

# Panjang list
print(f"Jumlah mahasiswa   : {len(mahasiswa)}")
```

### Langkah 2 — Method List

```python
# Demonstrasi method list
kota = ["Jakarta", "Surabaya", "Bandung"]
print(f"Awal    : {kota}")

# append - menambah di akhir
kota.append("Medan")
print(f"append  : {kota}")

# insert - menambah di posisi tertentu
kota.insert(1, "Yogyakarta")
print(f"insert  : {kota}")

# remove - menghapus berdasarkan nilai
kota.remove("Surabaya")
print(f"remove  : {kota}")

# pop - menghapus dan mengembalikan elemen
terakhir = kota.pop()
print(f"pop()   : {kota} (dihapus: {terakhir})")

posisi1 = kota.pop(1)
print(f"pop(1)  : {kota} (dihapus: {posisi1})")

# sort - mengurutkan
angka = [34, 12, 89, 5, 67, 23, 45]
print(f"\nSebelum sort : {angka}")
angka.sort()
print(f"sort()       : {angka}")
angka.sort(reverse=True)
print(f"sort(rev)    : {angka}")

# index dan count
buah = ["apel", "jeruk", "mangga", "apel", "durian", "apel"]
print(f"\nbuah            : {buah}")
print(f"index('mangga') : {buah.index('mangga')}")
print(f"count('apel')   : {buah.count('apel')}")
```

### Langkah 3 — List Comprehension

```python
# List comprehension — cara ringkas membuat list

# Cara biasa
kuadrat_biasa = []
for i in range(1, 11):
    kuadrat_biasa.append(i ** 2)

# Cara list comprehension
kuadrat_lc = [i ** 2 for i in range(1, 11)]
print(f"Kuadrat 1-10 : {kuadrat_lc}")

# Dengan kondisi (filter)
genap = [i for i in range(1, 21) if i % 2 == 0]
print(f"Genap 1-20   : {genap}")

# Manipulasi string
nama_list = ["aisyah", "budi", "citra", "dani"]
nama_kapital = [nama.capitalize() for nama in nama_list]
print(f"Kapital      : {nama_kapital}")

# Konversi suhu: Celcius ke Fahrenheit
celcius = [0, 10, 20, 25, 30, 37, 100]
fahrenheit = [(c * 9/5) + 32 for c in celcius]

print(f"\n{'Celcius':>8} | {'Fahrenheit':>10}")
print("-" * 22)
for c, f in zip(celcius, fahrenheit):
    print(f"{c:>8} | {f:>10.1f}")
```

### Langkah 4 — Tuple dan Unpacking

```python
# Membuat tuple (immutable — tidak bisa diubah)
koordinat = (6.2088, 106.8456)    # Jakarta
dimensi = (1920, 1080)

print(f"Koordinat Jakarta : {koordinat}")
print(f"Latitude          : {koordinat[0]}")
print(f"Longitude         : {koordinat[1]}")

# Tuple unpacking
lebar, tinggi = dimensi
print(f"\nResolusi: {lebar} x {tinggi}")

# Tuple dalam list — data mahasiswa
data_mhs = [
    ("Aisyah", "20250001", 3.85),
    ("Budi", "20250002", 3.42),
    ("Citra", "20250003", 3.91),
    ("Dani", "20250004", 3.15),
]

print(f"\n{'Nama':<10} {'NIM':<12} {'IPK':>5}")
print("-" * 30)
for nama, nim, ipk in data_mhs:
    print(f"{nama:<10} {nim:<12} {ipk:>5.2f}")
```

### Langkah 5 — Nested List (Matriks 2D)

```python
# Matriks 2D menggunakan nested list
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Matriks 3x3:")
for baris in matriks:
    for elemen in baris:
        print(f"{elemen:>4}", end="")
    print()

# Akses elemen tertentu
print(f"\nElemen baris 1, kolom 2 : matriks[0][1] = {matriks[0][1]}")
print(f"Elemen baris 3, kolom 3 : matriks[2][2] = {matriks[2][2]}")

# Penjumlahan dua matriks
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]

print(f"\nA = {A}")
print(f"B = {B}")
print(f"A + B = {C}")
```

### Langkah 6 — Built-in Functions untuk Collections

```python
# Built-in functions yang berguna
nilai_kelas = [78, 92, 65, 88, 71, 95, 82, 60, 74, 89]

print(f"Nilai kelas : {nilai_kelas}")
print(f"len()       : {len(nilai_kelas)} mahasiswa")
print(f"sum()       : {sum(nilai_kelas)} (total)")
print(f"min()       : {min(nilai_kelas)} (terendah)")
print(f"max()       : {max(nilai_kelas)} (tertinggi)")
print(f"Rata-rata   : {sum(nilai_kelas) / len(nilai_kelas):.2f}")
print(f"sorted()    : {sorted(nilai_kelas)}")
print(f"sorted(rev) : {sorted(nilai_kelas, reverse=True)}")

# enumerate — loop dengan index
print(f"\n--- Daftar dengan Nomor ---")
buah = ["Mangga", "Jeruk", "Apel", "Durian", "Rambutan"]
for i, nama in enumerate(buah, 1):
    print(f"  {i}. {nama}")

# zip — menggabungkan dua list
nama_mhs = ["Aisyah", "Budi", "Citra", "Dani", "Eka"]
nilai_mhs = [85, 92, 78, 65, 88]

print(f"\n--- Tabel Nilai (zip) ---")
print(f"{'No':<4} {'Nama':<10} {'Nilai':>6}")
print("-" * 22)
for i, (nama, nilai) in enumerate(zip(nama_mhs, nilai_mhs), 1):
    print(f"{i:<4} {nama:<10} {nilai:>6}")
```

### Langkah 7 — Mini Project: Sistem Nilai Mahasiswa

```python
# =============================================
# MINI PROJECT: Sistem Nilai Mahasiswa
# =============================================

def input_data():
    """Mengambil input data mahasiswa."""
    data = []
    jumlah = int(input("Jumlah mahasiswa: "))

    for i in range(1, jumlah + 1):
        print(f"\n--- Mahasiswa ke-{i} ---")
        nama = input("  Nama  : ")
        nim = input("  NIM   : ")
        tugas = float(input("  Tugas : "))
        uts = float(input("  UTS   : "))
        uas = float(input("  UAS   : "))
        data.append((nama, nim, tugas, uts, uas))

    return data

def hitung_nilai_akhir(tugas, uts, uas):
    """Menghitung nilai akhir: Tugas 30%, UTS 30%, UAS 40%."""
    return tugas * 0.3 + uts * 0.3 + uas * 0.4

def konversi_huruf(na):
    """Mengonversi nilai akhir ke huruf."""
    if na >= 85: return "A"
    elif na >= 75: return "B"
    elif na >= 60: return "C"
    elif na >= 45: return "D"
    else: return "E"

def proses_data(data):
    """Memproses seluruh data mahasiswa."""
    hasil = []
    for nama, nim, tugas, uts, uas in data:
        na = hitung_nilai_akhir(tugas, uts, uas)
        huruf = konversi_huruf(na)
        status = "Lulus" if huruf in ["A", "B", "C"] else "Tidak Lulus"
        hasil.append((nama, nim, tugas, uts, uas, na, huruf, status))
    return hasil

def hitung_statistik(hasil):
    """Menghitung statistik kelas."""
    semua_na = [row[5] for row in hasil]
    jumlah_lulus = sum(1 for row in hasil if row[7] == "Lulus")
    jumlah_tidak = len(hasil) - jumlah_lulus

    return {
        "total": len(hasil),
        "rata_rata": sum(semua_na) / len(semua_na),
        "tertinggi": max(semua_na),
        "terendah": min(semua_na),
        "lulus": jumlah_lulus,
        "tidak_lulus": jumlah_tidak,
    }

def tampilkan_tabel(hasil):
    """Menampilkan tabel nilai mahasiswa."""
    # Urutkan berdasarkan nilai akhir (descending)
    hasil_sorted = sorted(hasil, key=lambda x: x[5], reverse=True)

    print("\n" + "=" * 78)
    print(f"{'DAFTAR NILAI MAHASISWA':^78}")
    print(f"{'Algoritma dan Pemrograman — Semester Genap 2025/2026':^78}")
    print("=" * 78)
    print(f"{'No':<4} {'Nama':<14} {'NIM':<12} {'Tugas':>6} {'UTS':>6} {'UAS':>6} {'NA':>7} {'Huruf':>6} {'Status':<12}")
    print("-" * 78)

    for i, (nama, nim, tgs, uts, uas, na, huruf, status) in enumerate(hasil_sorted, 1):
        print(f"{i:<4} {nama:<14} {nim:<12} {tgs:>6.1f} {uts:>6.1f} {uas:>6.1f} {na:>7.2f} {huruf:>6} {status:<12}")

    print("-" * 78)

def tampilkan_statistik(stats):
    """Menampilkan statistik kelas."""
    print(f"\n{'=' * 40}")
    print(f"{'STATISTIK KELAS':^40}")
    print(f"{'=' * 40}")
    print(f"  Jumlah mahasiswa  : {stats['total']}")
    print(f"  Rata-rata kelas   : {stats['rata_rata']:.2f}")
    print(f"  Nilai tertinggi   : {stats['tertinggi']:.2f}")
    print(f"  Nilai terendah    : {stats['terendah']:.2f}")
    print(f"  Jumlah lulus      : {stats['lulus']}")
    print(f"  Jumlah tidak lulus: {stats['tidak_lulus']}")
    persen_lulus = stats['lulus'] / stats['total'] * 100
    print(f"  Tingkat kelulusan : {persen_lulus:.1f}%")
    print(f"{'=' * 40}")

# === Program Utama ===
print("=" * 50)
print(f"{'SISTEM NILAI MAHASISWA':^50}")
print(f"{'Informatika — UAI':^50}")
print("=" * 50)

data = input_data()
hasil = proses_data(data)
tampilkan_tabel(hasil)
stats = hitung_statistik(hasil)
tampilkan_statistik(stats)
```

---

## Tantangan Tambahan

1. **Inventory Toko**: Buat program pengelolaan stok barang menggunakan list of tuples. Fitur: tambah barang, hapus barang, cari barang, tampilkan stok yang hampir habis (< 5), dan total nilai inventory.

2. **Matriks Transpose dan Perkalian**: Buat fungsi untuk melakukan transpose matriks dan perkalian dua matriks menggunakan nested list. Tampilkan matriks input dan hasilnya dalam format yang rapi.

3. **Analisis Data Cuaca**: Buat program yang menyimpan data suhu harian selama satu minggu (7 hari) dalam list. Hitung rata-rata, suhu tertinggi dan terendah, hari terpanas dan terdingin, serta tampilkan grafik batang sederhana menggunakan karakter `#`.

---

## Checklist Penyelesaian

- [ ] Mampu membuat dan memanipulasi list (append, insert, remove, pop, sort)
- [ ] Mampu menggunakan list comprehension
- [ ] Memahami tuple dan teknik unpacking
- [ ] Mampu bekerja dengan nested list (matriks 2D)
- [ ] Menguasai built-in functions: `len`, `sum`, `min`, `max`, `sorted`, `enumerate`, `zip`
- [ ] Menyelesaikan Mini Project: Sistem Nilai Mahasiswa
- [ ] Mengerjakan minimal 1 tantangan tambahan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
