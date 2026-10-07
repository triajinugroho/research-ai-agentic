# Lab 02: Variabel dan Ekspresi

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Durasi** | 75 menit |
| **Prasyarat** | Lab 01 — Setup Python dan Google Colab |

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:
- Membuat variabel dengan berbagai tipe data dan memeriksa tipenya
- Melakukan konversi tipe data (*type casting*)
- Menggunakan operator aritmetika, perbandingan, dan logika
- Membangun program kalkulator harga sederhana dengan format output rapi

---

## Persiapan

1. Buka Google Colab dan buat notebook baru
2. Beri nama `Lab02_NamaAnda_NIM.ipynb`
3. Pastikan Anda telah menyelesaikan Lab 01

---

## Langkah-langkah

### Langkah 1 — Membuat Variabel Berbagai Tipe

```python
# Variabel dengan berbagai tipe data
nama_mahasiswa = "Siti Aisyah"          # str (string)
nim = "20250001"                         # str
usia = 19                                # int (integer)
ipk = 3.75                              # float
sudah_lulus = False                      # bool (boolean)
mata_kuliah_favorit = None               # NoneType

# Menampilkan nilai setiap variabel
print("Nama      :", nama_mahasiswa)
print("NIM       :", nim)
print("Usia      :", usia)
print("IPK       :", ipk)
print("Sudah Lulus:", sudah_lulus)
print("MK Favorit:", mata_kuliah_favorit)
```

### Langkah 2 — Memeriksa Tipe Data dengan `type()`

```python
# Memeriksa tipe data setiap variabel
print("Tipe nama_mahasiswa     :", type(nama_mahasiswa))
print("Tipe nim                :", type(nim))
print("Tipe usia               :", type(usia))
print("Tipe ipk                :", type(ipk))
print("Tipe sudah_lulus        :", type(sudah_lulus))
print("Tipe mata_kuliah_favorit:", type(mata_kuliah_favorit))
```

**Penjelasan:**
- `type()` mengembalikan tipe data dari suatu variabel
- Python adalah bahasa *dynamically typed* — tipe ditentukan otomatis saat pemberian nilai

### Langkah 3 — Konversi Tipe Data (*Type Casting*)

```python
# Konversi tipe data
angka_str = "2025"
angka_int = int(angka_str)       # str → int
angka_float = float(angka_str)   # str → float

print(f"'{angka_str}' (str) → {angka_int} (int) → {angka_float} (float)")

# Konversi balik
nilai = 87.5
nilai_int = int(nilai)           # float → int (membuang desimal)
nilai_str = str(nilai)           # float → str

print(f"{nilai} (float) → {nilai_int} (int) → '{nilai_str}' (str)")

# Boolean casting
print(f"\nbool(1)     = {bool(1)}")      # True
print(f"bool(0)     = {bool(0)}")        # False
print(f"bool('')    = {bool('')}")        # False (string kosong)
print(f"bool('Hai') = {bool('Hai')}")    # True (string tidak kosong)
```

### Langkah 4 — Operator Aritmetika (7 Operator)

```python
# Tujuh operator aritmetika Python
a = 25
b = 7

print(f"a = {a}, b = {b}")
print("-" * 35)
print(f"Penjumlahan   : a + b  = {a + b}")
print(f"Pengurangan   : a - b  = {a - b}")
print(f"Perkalian     : a * b  = {a * b}")
print(f"Pembagian     : a / b  = {a / b:.4f}")
print(f"Pembagian bulat: a // b = {a // b}")
print(f"Modulus (sisa): a %% b  = {a % b}")
print(f"Pangkat       : a ** b = {a ** b}")
```

**Penjelasan:**
| Operator | Fungsi | Contoh |
|----------|--------|--------|
| `+` | Penjumlahan | `25 + 7 = 32` |
| `-` | Pengurangan | `25 - 7 = 18` |
| `*` | Perkalian | `25 * 7 = 175` |
| `/` | Pembagian (desimal) | `25 / 7 = 3.5714` |
| `//` | Pembagian bulat | `25 // 7 = 3` |
| `%` | Modulus (sisa bagi) | `25 % 7 = 4` |
| `**` | Pangkat | `25 ** 2 = 625` |

### Langkah 5 — Operator Perbandingan dan Logika

```python
# Operator perbandingan
nilai_uts = 78
nilai_uas = 85
kkm = 70

print("=== Operator Perbandingan ===")
print(f"nilai_uts == nilai_uas : {nilai_uts == nilai_uas}")
print(f"nilai_uts != nilai_uas : {nilai_uts != nilai_uas}")
print(f"nilai_uts > kkm        : {nilai_uts > kkm}")
print(f"nilai_uas >= 85        : {nilai_uas >= 85}")
print(f"nilai_uts < nilai_uas  : {nilai_uts < nilai_uas}")

# Operator logika
print("\n=== Operator Logika ===")
lulus_uts = nilai_uts >= kkm
lulus_uas = nilai_uas >= kkm

print(f"Lulus UTS: {lulus_uts}, Lulus UAS: {lulus_uas}")
print(f"Lulus UTS AND Lulus UAS : {lulus_uts and lulus_uas}")
print(f"Lulus UTS OR  Lulus UAS : {lulus_uts or lulus_uas}")
print(f"NOT Lulus UTS           : {not lulus_uts}")
```

### Langkah 6 — Input/Output dengan Formatting

```python
# Berbagai cara memformat output
nama = "Budi Santoso"
nilai = 92.567
semester = 3

# Cara 1: Concatenation
print("Nama: " + nama + ", Semester: " + str(semester))

# Cara 2: Koma pada print
print("Nama:", nama, "| Semester:", semester)

# Cara 3: format()
print("Nama: {}, Semester: {}".format(nama, semester))

# Cara 4: f-string (DIREKOMENDASIKAN)
print(f"Nama: {nama}, Semester: {semester}")

# Format angka desimal
print(f"Nilai (2 desimal)  : {nilai:.2f}")
print(f"Nilai (tanpa desimal): {nilai:.0f}")

# Format rata kanan dengan lebar tertentu
print(f"{'Mata Kuliah':<20} {'Nilai':>6}")
print(f"{'Algoritma':<20} {85:>6}")
print(f"{'Basis Data':<20} {92:>6}")
print(f"{'Jaringan Komputer':<20} {78:>6}")
```

### Langkah 7 — Mini Project: Kalkulator Harga Warung

```python
# ================================================
# MINI PROJECT: Kalkulator Harga Warung Makan
# ================================================

print("=" * 45)
print("   WARUNG MAKAN BAROKAH - NOTA PEMBAYARAN")
print("=" * 45)

# Input data pesanan
nama_pelanggan = input("Nama pelanggan: ")
nasi_goreng = int(input("Jumlah Nasi Goreng (@ Rp15.000) : "))
es_teh = int(input("Jumlah Es Teh      (@ Rp5.000)  : "))
bakso = int(input("Jumlah Bakso       (@ Rp12.000) : "))

# Harga satuan
harga_nasi = 15000
harga_teh = 5000
harga_bakso = 12000

# Hitung subtotal per item
sub_nasi = nasi_goreng * harga_nasi
sub_teh = es_teh * harga_teh
sub_bakso = bakso * harga_bakso

# Hitung total
subtotal = sub_nasi + sub_teh + sub_bakso

# Diskon 10% jika subtotal >= 50000
if subtotal >= 50000:
    diskon_persen = 10
else:
    diskon_persen = 0

diskon = subtotal * diskon_persen / 100

# Pajak restoran 5%
pajak_persen = 5
pajak = (subtotal - diskon) * pajak_persen / 100

# Total bayar
total_bayar = subtotal - diskon + pajak

# Tampilkan nota
print("\n" + "=" * 45)
print(f"  Pelanggan: {nama_pelanggan}")
print("-" * 45)
print(f"{'Item':<22} {'Qty':>3} {'Harga':>8} {'Subtotal':>10}")
print("-" * 45)

if nasi_goreng > 0:
    print(f"{'Nasi Goreng':<22} {nasi_goreng:>3} {harga_nasi:>8,} {sub_nasi:>10,}")
if es_teh > 0:
    print(f"{'Es Teh':<22} {es_teh:>3} {harga_teh:>8,} {sub_teh:>10,}")
if bakso > 0:
    print(f"{'Bakso':<22} {bakso:>3} {harga_bakso:>8,} {sub_bakso:>10,}")

print("-" * 45)
print(f"{'Subtotal':<35} Rp{subtotal:>10,}")
print(f"{'Diskon (' + str(diskon_persen) + '%)':<35} Rp{diskon:>10,.0f}")
print(f"{'Pajak (' + str(pajak_persen) + '%)':<35} Rp{pajak:>10,.0f}")
print("=" * 45)
print(f"{'TOTAL BAYAR':<35} Rp{total_bayar:>10,.0f}")
print("=" * 45)
print("Terima kasih sudah makan di Warung Barokah!")
```

---

## Tantangan Tambahan

1. **Konverter Mata Uang**: Buat program yang mengonversi Rupiah ke 3 mata uang asing (USD, EUR, MYR) berdasarkan kurs yang diinput pengguna. Tampilkan hasilnya dengan format 2 desimal.

2. **Kalkulator Cicilan**: Buat program menghitung cicilan bulanan untuk pembelian laptop. Input: harga laptop, uang muka, jumlah bulan cicilan, dan bunga per tahun. Tampilkan tabel rincian cicilan per bulan.

3. **Kalkulator Bangun Datar**: Buat program yang menghitung luas dan keliling persegi, persegi panjang, dan lingkaran. Masing-masing bangun meminta input dimensi yang sesuai.

---

## Checklist Penyelesaian

- [ ] Mampu membuat variabel dengan tipe `str`, `int`, `float`, `bool`
- [ ] Mampu memeriksa tipe data dengan `type()`
- [ ] Mampu melakukan konversi tipe data (`int()`, `float()`, `str()`)
- [ ] Memahami dan menggunakan 7 operator aritmetika
- [ ] Memahami operator perbandingan dan logika
- [ ] Mampu memformat output menggunakan f-string
- [ ] Menyelesaikan Mini Project: Kalkulator Harga Warung
- [ ] Mengerjakan minimal 1 tantangan tambahan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
