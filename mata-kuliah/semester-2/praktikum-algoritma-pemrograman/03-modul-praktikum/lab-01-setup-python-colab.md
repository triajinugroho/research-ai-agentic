# Lab 01: Setup Python dan Google Colab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Durasi** | 75 menit |
| **Prasyarat** | Akun Google aktif, browser modern (Chrome/Firefox) |

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:
- Membuat dan mengelola notebook di Google Colab
- Memahami perbedaan sel kode (*code cell*) dan sel teks (*text cell*)
- Menggunakan fungsi `print()` untuk menampilkan output
- Menggunakan fungsi `input()` untuk menerima masukan dari pengguna

---

## Persiapan

1. Buka browser dan masuk ke akun Google Anda
2. Akses [Google Colab](https://colab.research.google.com/)
3. Klik **New Notebook** untuk membuat notebook baru
4. Ganti nama notebook menjadi `Lab01_NamaAnda_NIM.ipynb`

---

## Langkah-langkah

### Langkah 1 — Mengenal Antarmuka Google Colab

Perhatikan elemen-elemen berikut pada antarmuka Colab:
- **Menu bar**: File, Edit, View, Insert, Runtime, Tools, Help
- **Toolbar**: tombol untuk menambah sel, menjalankan sel, dll.
- **Code cell**: sel untuk menulis dan menjalankan kode Python
- **Text cell**: sel untuk menulis catatan dalam format Markdown

> Tambahkan sebuah **text cell** di bagian paling atas notebook Anda, lalu tulis:
> `# Lab 01 - Nama Anda - NIM`

### Langkah 2 — Menjalankan Sel Kode Pertama

Klik pada *code cell* dan ketik kode berikut, lalu tekan **Shift + Enter** untuk menjalankan:

```python
# Program pertama saya di Google Colab
print("Assalamualaikum, dunia!")
print("Selamat datang di Algoritma dan Pemrograman")
```

**Penjelasan:**
- `print()` adalah fungsi bawaan Python untuk menampilkan teks ke layar
- Teks di dalam tanda kutip disebut **string**
- Baris yang diawali `#` adalah **komentar** dan tidak dieksekusi

### Langkah 3 — Menampilkan Beberapa Baris Output

```python
# Menampilkan informasi diri
print("=================================")
print("   BIODATA MAHASISWA")
print("=================================")
print("Nama  : Ahmad Fauzan")
print("NIM   : 12345678")
print("Prodi : Informatika")
print("Kampus: Universitas Al Azhar Indonesia")
print("=================================")
```

### Langkah 4 — Operasi Aritmetika Sederhana

Python dapat digunakan langsung sebagai kalkulator:

```python
# Python sebagai kalkulator
print("Penjumlahan  : 15 + 27 =", 15 + 27)
print("Pengurangan  : 100 - 35 =", 100 - 35)
print("Perkalian    : 12 * 8 =", 12 * 8)
print("Pembagian    : 45 / 7 =", 45 / 7)
```

**Penjelasan:**
- Python langsung menghitung ekspresi aritmetika di dalam `print()`
- Koma (`,`) pada `print()` memisahkan beberapa nilai yang ingin ditampilkan

### Langkah 5 — Menggunakan Fungsi `input()`

Fungsi `input()` memungkinkan program menerima masukan dari pengguna:

```python
# Menerima input dari pengguna
nama = input("Masukkan nama Anda: ")
print("Halo,", nama, "! Selamat belajar Python.")
```

**Penjelasan:**
- `input()` menampilkan pesan dan menunggu pengguna mengetik sesuatu
- Hasil input disimpan dalam **variabel** bernama `nama`
- Variabel adalah wadah untuk menyimpan data

### Langkah 6 — Input dan Perhitungan

Perhatikan bahwa `input()` selalu mengembalikan tipe **string**. Untuk perhitungan, kita perlu mengonversi ke angka:

```python
# Input angka dari pengguna
bilangan1 = input("Masukkan bilangan pertama: ")
bilangan2 = input("Masukkan bilangan kedua: ")

# Konversi string ke integer
bilangan1 = int(bilangan1)
bilangan2 = int(bilangan2)

# Hitung dan tampilkan hasil
hasil = bilangan1 + bilangan2
print("Hasil penjumlahan:", bilangan1, "+", bilangan2, "=", hasil)
```

### Langkah 7 — Program Interaktif: Perkenalan Diri

Gabungkan semua yang telah dipelajari menjadi satu program utuh:

```python
# ===================================
# Program Perkenalan Diri Interaktif
# ===================================

print("=" * 40)
print("  PROGRAM PERKENALAN DIRI")
print("=" * 40)

# Menerima data dari pengguna
nama = input("Nama lengkap    : ")
nim = input("NIM              : ")
kota = input("Kota asal        : ")
umur = input("Umur (tahun)     : ")

# Konversi umur ke integer dan hitung tahun lahir
umur = int(umur)
tahun_lahir = 2026 - umur

# Menampilkan hasil
print("\n" + "=" * 40)
print("  KARTU IDENTITAS MAHASISWA")
print("=" * 40)
print(f"Nama       : {nama}")
print(f"NIM        : {nim}")
print(f"Kota Asal  : {kota}")
print(f"Umur       : {umur} tahun")
print(f"Tahun Lahir: {tahun_lahir} (perkiraan)")
print("=" * 40)
print("Selamat bergabung di Prodi Informatika UAI!")
```

### Langkah 8 — Kalkulator Sederhana

```python
# ===================================
# Kalkulator Sederhana
# ===================================

print(">> Kalkulator Sederhana <<")
print("-" * 30)

angka1 = float(input("Masukkan angka pertama : "))
angka2 = float(input("Masukkan angka kedua   : "))

print("\n--- Hasil Perhitungan ---")
print(f"{angka1} + {angka2} = {angka1 + angka2}")
print(f"{angka1} - {angka2} = {angka1 - angka2}")
print(f"{angka1} x {angka2} = {angka1 * angka2}")

if angka2 != 0:
    print(f"{angka1} / {angka2} = {angka1 / angka2}")
else:
    print("Pembagian dengan nol tidak diperbolehkan!")
```

---

## Tantangan Tambahan

1. **Konversi Suhu**: Buat program yang menerima input suhu dalam Celcius, lalu menampilkan hasilnya dalam Fahrenheit (`F = C * 9/5 + 32`), Reamur (`R = C * 4/5`), dan Kelvin (`K = C + 273.15`).

2. **Kalkulator Zakat Penghasilan**: Buat program yang menerima input gaji bulanan, lalu menghitung zakat 2.5% jika gaji melebihi nisab (setara 85 gram emas, asumsikan Rp 85.000.000 per tahun). Tampilkan apakah wajib zakat dan berapa nominalnya.

3. **Kartu Nama Digital**: Buat program yang menerima input lengkap (nama, alamat, telepon, email, hobi) lalu menampilkan dalam format kartu nama yang rapi menggunakan border karakter.

---

## Checklist Penyelesaian

- [ ] Berhasil membuat notebook baru di Google Colab
- [ ] Mampu menjalankan sel kode dan sel teks
- [ ] Berhasil menggunakan `print()` dengan berbagai format
- [ ] Berhasil menggunakan `input()` untuk menerima masukan
- [ ] Berhasil mengonversi tipe data input menggunakan `int()` dan `float()`
- [ ] Menyelesaikan Program Perkenalan Diri Interaktif
- [ ] Menyelesaikan Kalkulator Sederhana
- [ ] Mengerjakan minimal 1 tantangan tambahan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
