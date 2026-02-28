# Minggu 6: String dan Pengolahan Teks

## Informasi Modul

| Komponen       | Detail                                                           |
|----------------|------------------------------------------------------------------|
| Mata Kuliah    | Algoritma dan Pemrograman (3 SKS)                                |
| Minggu         | 6 (Enam)                                                        |
| Topik          | String dan Pengolahan Teks                                       |
| CPMK           | CPMK-4: Mampu menerapkan prinsip modularitas dalam pemrograman   |
| Sub-CPMK       | CPMK-4.5, CPMK-4.6, CPMK-4.7, CPMK-4.8                        |
| Durasi         | 150 menit                                                        |
| Metode         | Ceramah, live coding, praktikum                                  |
| Pengajar       | Tri Aji Nugroho, S.T., M.T.                                     |
| Program Studi  | Informatika, Universitas Al Azhar Indonesia                      |
| Semester       | Genap 2025/2026                                                  |
| Bahasa         | Python                                                           |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menganalisis** string sebagai sequence dan menerapkan operasi indexing serta slicing untuk mengakses dan memanipulasi karakter (CPMK-4.5).
2. **Menggunakan** berbagai string methods bawaan Python untuk pengolahan dan transformasi teks (CPMK-4.6).
3. **Menerapkan** teknik formatting string menggunakan f-string untuk menghasilkan output yang terstruktur (CPMK-4.7).
4. **Mengimplementasikan** operasi file I/O dasar (baca dan tulis file teks, CSV sederhana) menggunakan statement `with` (CPMK-4.8).

---

## Materi Pembelajaran

### 6.1 String sebagai Sequence

String di Python adalah urutan (sequence) karakter yang bersifat **immutable** — tidak dapat diubah setelah dibuat.

```python
teks = "Informatika"

# Indexing (mulai dari 0)
print(teks[0])     # 'I'
print(teks[-1])    # 'a' (indeks negatif dari belakang)

# Slicing [start:stop:step]
print(teks[0:5])   # 'Infor'
print(teks[5:])    # 'matika'
print(teks[::-1])  # 'akitamrofnI' (reverse)
```

| Operasi          | Sintaks            | Contoh                  | Hasil         |
|------------------|--------------------|-------------------------|---------------|
| Indexing         | `s[i]`             | `"Python"[0]`           | `'P'`         |
| Negative index   | `s[-i]`            | `"Python"[-1]`          | `'n'`         |
| Slicing          | `s[start:stop]`    | `"Python"[1:4]`         | `'yth'`       |
| Step slicing     | `s[::step]`        | `"Python"[::2]`         | `'Pto'`       |
| Length            | `len(s)`           | `len("Python")`         | `6`           |
| Membership       | `x in s`           | `'th' in "Python"`      | `True`        |
| Concatenation    | `s1 + s2`          | `"Py" + "thon"`         | `'Python'`    |
| Repetition       | `s * n`            | `"Ha" * 3`              | `'HaHaHa'`   |

### 6.2 String Methods

Python menyediakan banyak method bawaan untuk memanipulasi string:

```python
kalimat = "  Selamat Datang di Universitas Al Azhar Indonesia  "

# Transformasi
print(kalimat.strip())          # hapus spasi di awal dan akhir
print(kalimat.lower())          # semua huruf kecil
print(kalimat.upper())          # semua huruf besar
print(kalimat.title())          # huruf kapital di awal kata

# Pencarian
print(kalimat.find("Azhar"))    # 35 (indeks kemunculan pertama)
print(kalimat.count("a"))       # jumlah kemunculan karakter 'a'

# Penggantian dan pemisahan
print(kalimat.replace("Indonesia", "Jakarta"))
kata_list = kalimat.split()     # memecah berdasarkan spasi
print(kata_list)

# Penggabungan
buah = ["apel", "mangga", "jeruk"]
print(", ".join(buah))          # "apel, mangga, jeruk"

# Validasi
print("12345".isdigit())        # True
print("abc".isalpha())          # True
print("abc123".isalnum())       # True
```

### 6.3 String Formatting dengan f-string

f-string (formatted string literal) adalah cara modern dan efisien untuk menyisipkan ekspresi ke dalam string:

```python
nama = "Ahmad"
nilai = 87.5
grade = "A"

# f-string dasar
print(f"Nama: {nama}, Nilai: {nilai}, Grade: {grade}")

# Format angka
pi = 3.14159265
print(f"Pi = {pi:.2f}")            # Pi = 3.14
print(f"Harga: Rp{50000:,.0f}")    # Harga: Rp50,000

# Alignment dan padding
for item, harga in [("Nasi Goreng", 25000), ("Es Teh", 5000), ("Bakso", 20000)]:
    print(f"{item:<20} Rp{harga:>10,.0f}")
# Output:
# Nasi Goreng          Rp    25,000
# Es Teh               Rp     5,000
# Bakso                Rp    20,000

# Ekspresi dalam f-string
print(f"10 + 20 = {10 + 20}")
print(f"{'python'.upper()}")
```

### 6.4 File I/O Dasar

Operasi file memungkinkan program membaca dan menulis data ke file eksternal:

```python
# Menulis file teks
with open("output.txt", "w") as f:
    f.write("Baris pertama\n")
    f.write("Baris kedua\n")
    f.write("Baris ketiga\n")

# Membaca seluruh file
with open("output.txt", "r") as f:
    isi = f.read()
    print(isi)

# Membaca baris per baris
with open("output.txt", "r") as f:
    for baris in f:
        print(baris.strip())

# Menambahkan ke file (append)
with open("output.txt", "a") as f:
    f.write("Baris tambahan\n")
```

| Mode   | Keterangan                                  |
|--------|---------------------------------------------|
| `"r"`  | Read — membaca (default, error jika tidak ada) |
| `"w"`  | Write — menulis (buat baru / timpa)          |
| `"a"`  | Append — menambahkan di akhir file           |
| `"r+"` | Read + Write                                 |

> **Penting:** Selalu gunakan statement `with` untuk membuka file. Statement ini menjamin file ditutup otomatis meskipun terjadi error.

### 6.5 Membaca dan Menulis CSV Sederhana

```python
# Menulis CSV sederhana
mahasiswa = [
    ["NIM", "Nama", "Nilai"],
    ["001", "Ahmad", "85"],
    ["002", "Budi", "90"],
    ["003", "Citra", "78"]
]

with open("mahasiswa.csv", "w") as f:
    for baris in mahasiswa:
        f.write(",".join(baris) + "\n")

# Membaca CSV sederhana
with open("mahasiswa.csv", "r") as f:
    for baris in f:
        kolom = baris.strip().split(",")
        print(f"NIM: {kolom[0]}, Nama: {kolom[1]}, Nilai: {kolom[2]}")
```

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Membaca materi modul Minggu 6 tentang string dan file I/O.
- Mencoba eksperimen singkat di Google Colab: buat string, coba 3 method berbeda.
- Menyiapkan file teks sederhana (`.txt`) di komputer untuk latihan file I/O.

### In-class (120 menit)

| Waktu (menit) | Kegiatan                                                   | Metode           |
|----------------|-----------------------------------------------------------|------------------|
| 0 -- 10        | Review pre-class, pengumpulan Tugas T3, tanya jawab        | Diskusi          |
| 10 -- 35       | Ceramah: string sebagai sequence, indexing, slicing, methods | Ceramah         |
| 35 -- 55       | Live coding: pengolahan teks — analisis frekuensi kata      | Demonstrasi      |
| 55 -- 65       | Istirahat                                                  | —                |
| 65 -- 80       | Ceramah: f-string formatting dan file I/O                  | Ceramah          |
| 80 -- 110      | Praktikum: membaca file teks, memproses data, menulis CSV   | Praktikum        |
| 110 -- 120     | Diskusi hasil praktikum dan ringkasan materi                | Diskusi          |

### Post-class (15 menit)
- Menyelesaikan latihan tambahan tentang string methods di Google Colab.
- Eksplorasi mandiri: membaca dokumentasi Python tentang `str` methods.
- Membaca materi Minggu 7 tentang List, Tuple, dan Operasi Koleksi sebagai persiapan.

---

## Penugasan

Tidak ada tugas formal pada minggu ini. Mahasiswa diharapkan menyelesaikan latihan praktikum file I/O yang diberikan di kelas dan menyiapkan diri untuk Tugas T4 dan Kuis K2 pada Minggu 7.

---

## Referensi

1. Downey, A. (2015). *Think Python: How to Think Like a Computer Scientist*, 2nd Edition. O'Reilly Media. — Chapter 8: Strings, Chapter 14: Files.
2. Matthes, E. (2023). *Python Crash Course*, 3rd Edition. No Starch Press. — Chapter 6: Strings, Chapter 10: Files and Exceptions.
3. Python Software Foundation. "String Methods." *Python 3 Documentation*. [https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
4. Python Software Foundation. "Reading and Writing Files." *Python 3 Documentation*. [https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
