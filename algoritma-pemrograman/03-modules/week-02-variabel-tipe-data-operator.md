# Minggu 2: Variabel, Tipe Data, dan Operator

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Algoritma dan Pemrograman (3 SKS) |
| **Minggu** | 2 dari 16 |
| **Topik** | Variabel, Tipe Data, dan Operator |
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python |
| **CPMK** | CPMK-2 |
| **Sub-CPMK** | CPMK-2.1, CPMK-2.2, CPMK-2.3, CPMK-2.4 |
| **Durasi** | 150 menit (Teori: 75 menit, Praktik: 75 menit) |
| **Metode** | Ceramah interaktif, Live Coding, Praktik |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Menjelaskan** konsep variabel, aturan penamaan, dan mekanisme penugasan nilai dalam Python (CPMK-2.1)
2. **Membedakan** tipe data dasar (int, float, str, bool) beserta karakteristik dan penggunaannya (CPMK-2.2)
3. **Menerapkan** operator aritmetika, perbandingan, dan logika untuk membangun ekspresi komputasional (CPMK-2.3)
4. **Mengimplementasikan** operasi input/output dan konversi tipe data dalam program Python sederhana (CPMK-2.4)

---

## Materi Pembelajaran

### 1. Variabel dan Aturan Penamaan (CPMK-2.1)

**Variabel** adalah nama yang merujuk pada lokasi di memori tempat data disimpan. Dalam Python, variabel dibuat saat pertama kali diberi nilai (tidak perlu deklarasi eksplisit).

```python
nama = "Ahmad"          # string
usia = 20               # integer
tinggi = 170.5          # float
aktif = True            # boolean
```

**Aturan penamaan variabel:**

| Aturan | Contoh Valid | Contoh Tidak Valid |
|--------|-------------|-------------------|
| Dimulai dengan huruf atau underscore | `nama`, `_total` | `2nama`, `@nilai` |
| Hanya mengandung huruf, angka, underscore | `nilai_1`, `total_harga` | `nilai-1`, `total harga` |
| Bersifat case-sensitive | `Nama` berbeda dengan `nama` | -- |
| Tidak boleh menggunakan keyword Python | `jumlah`, `data` | `for`, `if`, `class` |

**Konvensi penamaan (snake_case):**

```python
# Direkomendasikan (snake_case)
nama_mahasiswa = "Siti Aminah"
nilai_rata_rata = 85.5

# Tidak direkomendasikan
NamaMahasiswa = "Siti Aminah"    # PascalCase (untuk nama class)
nilairatarata = 85.5              # sulit dibaca
```

### 2. Tipe Data Dasar (CPMK-2.2)

Python memiliki empat tipe data dasar yang sering digunakan:

| Tipe Data | Deskripsi | Contoh | Fungsi Pemeriksa |
|-----------|-----------|--------|-----------------|
| `int` | Bilangan bulat (tanpa batas ukuran) | `42`, `-7`, `0` | `type(42)` -> `<class 'int'>` |
| `float` | Bilangan desimal (pecahan) | `3.14`, `-0.5`, `2.0` | `type(3.14)` -> `<class 'float'>` |
| `str` | Teks/string (diapit tanda kutip) | `"Halo"`, `'UAI'` | `type("Halo")` -> `<class 'str'>` |
| `bool` | Nilai logika (benar/salah) | `True`, `False` | `type(True)` -> `<class 'bool'>` |

```python
# Memeriksa tipe data
bilangan = 42
print(type(bilangan))    # <class 'int'>

nama = "Informatika"
print(type(nama))        # <class 'str'>
```

### 3. Operator (CPMK-2.3)

#### a. Operator Aritmetika

| Operator | Fungsi | Contoh | Hasil |
|----------|--------|--------|-------|
| `+` | Penjumlahan | `7 + 3` | `10` |
| `-` | Pengurangan | `7 - 3` | `4` |
| `*` | Perkalian | `7 * 3` | `21` |
| `/` | Pembagian (float) | `7 / 3` | `2.333...` |
| `//` | Pembagian bulat (floor) | `7 // 3` | `2` |
| `%` | Modulo (sisa bagi) | `7 % 3` | `1` |
| `**` | Perpangkatan | `2 ** 3` | `8` |

#### b. Operator Perbandingan

| Operator | Fungsi | Contoh | Hasil |
|----------|--------|--------|-------|
| `==` | Sama dengan | `5 == 5` | `True` |
| `!=` | Tidak sama dengan | `5 != 3` | `True` |
| `>` | Lebih besar | `5 > 3` | `True` |
| `<` | Lebih kecil | `5 < 3` | `False` |
| `>=` | Lebih besar atau sama | `5 >= 5` | `True` |
| `<=` | Lebih kecil atau sama | `3 <= 5` | `True` |

#### c. Operator Logika

| Operator | Fungsi | Contoh | Hasil |
|----------|--------|--------|-------|
| `and` | DAN -- True jika keduanya True | `True and False` | `False` |
| `or` | ATAU -- True jika salah satu True | `True or False` | `True` |
| `not` | NEGASI -- membalik nilai logika | `not True` | `False` |

### 4. Input/Output dan Konversi Tipe Data (CPMK-2.4)

#### Input dari Pengguna

```python
# input() selalu mengembalikan string
nama = input("Masukkan nama Anda: ")
usia = int(input("Masukkan usia Anda: "))
tinggi = float(input("Masukkan tinggi badan (cm): "))
```

#### Output ke Layar

```python
# Berbagai cara menampilkan output
nama = "Ahmad"
nilai = 90

print("Nama:", nama)                          # concatenation dengan koma
print("Nama: " + nama)                        # string concatenation
print(f"Nama: {nama}, Nilai: {nilai}")         # f-string (direkomendasikan)
print("Nama: {}, Nilai: {}".format(nama, nilai))  # method format
```

#### Konversi Tipe Data (Type Casting)

```python
# String ke integer/float
angka_str = "42"
angka_int = int(angka_str)      # 42
angka_float = float(angka_str)  # 42.0

# Integer/float ke string
nilai = 85
nilai_str = str(nilai)          # "85"

# Float ke integer (membuang desimal)
pi = 3.14
pi_int = int(pi)                # 3
```

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)

1. Membaca materi tentang variabel dan tipe data dari referensi utama -- Bab 2 (10 menit)
2. Mencoba menjalankan Google Colab dan menulis `print("Siap belajar!")` untuk memastikan lingkungan siap (5 menit)

### In-class (120 menit)

| Waktu | Kegiatan | Metode |
|-------|----------|--------|
| 0--25 menit | Ceramah: Konsep variabel, aturan penamaan, dan mekanisme assignment | Ceramah interaktif |
| 25--45 menit | Ceramah: Tipe data dasar (int, float, str, bool) dan fungsi `type()` | Ceramah dan demonstrasi |
| 45--70 menit | Live coding: Operator aritmetika, perbandingan, dan logika dengan berbagai contoh | Live coding |
| 70--90 menit | Live coding: Input/output dan konversi tipe data | Live coding |
| 90--120 menit | Praktik mandiri: Latihan soal variabel, tipe data, operator, dan input/output | Praktik terbimbing |

### Post-class (15 menit)

1. Menyelesaikan latihan tambahan: menulis program yang menghitung konversi suhu (Celsius ke Fahrenheit) (10 menit)
2. Memulai pengerjaan Tugas T1 -- Kalkulator Sederhana (5 menit persiapan)

---

## Penugasan

### Tugas T1: Kalkulator Sederhana

| Komponen | Detail |
|----------|--------|
| **Jenis** | Tugas Individu |
| **Bobot** | Sesuai ketentuan RPS |
| **Deadline** | Minggu 3 (sebelum perkuliahan) |

**Deskripsi:**
Buatlah program Python "Kalkulator Sederhana" yang:

1. Meminta pengguna memasukkan dua bilangan (bisa desimal)
2. Meminta pengguna memilih operasi: penjumlahan, pengurangan, perkalian, atau pembagian
3. Menampilkan hasil perhitungan dengan format yang rapi
4. Menangani kasus pembagian dengan nol (menampilkan pesan kesalahan)

**Kriteria penilaian:** Ketepatan logika (40%), Kualitas kode dan penamaan variabel (30%), Penanganan kasus khusus (20%), Kerapian output (10%).

---

## Referensi

1. Gaddis, T. (2021). *Starting Out with Python*, 5th Edition. Pearson. -- Bab 2.
2. Zelle, J. (2016). *Python Programming: An Introduction to Computer Science*, 3rd Edition. -- Bab 2.
3. Dokumentasi resmi Python -- Built-in Types: [https://docs.python.org/3/library/stdtypes.html](https://docs.python.org/3/library/stdtypes.html)
4. Python Tutorial -- An Informal Introduction: [https://docs.python.org/3/tutorial/introduction.html](https://docs.python.org/3/tutorial/introduction.html)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
