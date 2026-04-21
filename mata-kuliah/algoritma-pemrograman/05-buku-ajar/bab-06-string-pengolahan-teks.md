# BAB 6: STRING DAN PENGOLAHAN TEKS

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|-----------|-----------|---------------|
| CPMK-4.5 | Memahami string sebagai sequence dan operasinya | C2 (Memahami) |
| CPMK-4.6 | Menerapkan string methods untuk pengolahan teks | C3 (Menerapkan) |
| CPMK-4.7 | Mengimplementasikan program pengolahan teks dengan fungsi | C3-C4 (Menerapkan-Menganalisis) |

**Estimasi Waktu:** 3 x 50 menit (3 SKS)

**Prasyarat:** Mahasiswa telah memahami materi Bab 1-5 (Pengantar, Variabel & Tipe Data, Seleksi, Perulangan, dan Fungsi).

---

## 6.1 String: Lebih dari Sekadar Teks

### 6.1.1 String sebagai Sequence

Dalam Python, **string** (`str`) adalah tipe data yang merepresentasikan urutan (sequence) karakter. Setiap karakter dalam string memiliki posisi (indeks) tertentu, mirip seperti deretan kotak yang masing-masing berisi satu huruf.

**Analogi kehidupan sehari-hari:**

Bayangkan sebuah **tasbih digital** dengan 33 butir. Setiap butir memiliki nomor urut (0, 1, 2, ..., 32) dan menyimpan satu karakter. Anda bisa mengakses butir tertentu berdasarkan nomor urutnya, namun Anda **tidak bisa mengganti** butir yang sudah ada — Anda hanya bisa membuat tasbih baru jika ingin perubahan.

```python
# String adalah sequence (urutan) karakter
nama = "Informatika"

# Setiap karakter memiliki indeks (posisi)
print(nama[0])   # Output: I
print(nama[1])   # Output: n
print(nama[10])  # Output: a

# String memiliki panjang (jumlah karakter)
print(len(nama)) # Output: 11
```

**Sifat Immutable (Tidak Dapat Diubah):**

String di Python bersifat **immutable** — artinya setelah string dibuat, isinya **tidak bisa diubah**. Ini berbeda dari list yang bersifat mutable.

```python
nama = "Informatika"

# SALAH: mencoba mengubah karakter string
# nama[0] = "i"  # TypeError: 'str' object does not support item assignment

# BENAR: buat string baru
nama_baru = "i" + nama[1:]
print(nama_baru)  # Output: informatika

# String asli tidak berubah
print(nama)        # Output: Informatika
```

> **Catatan Penting:** Immutability bukan kelemahan, melainkan fitur keamanan. Dalam pemrograman, data yang tidak bisa diubah secara tak terduga membuat program lebih mudah diprediksi dan di-debug. Ini sejalan dengan prinsip **transparansi** — kode yang perilakunya jelas dan dapat diprediksi.

**Visualisasi String di Memori:**

```
String: "UAI"

Memori:
┌──────────────────────────────────────┐
│                                      │
│   nama ──────► [ "U" | "A" | "I" ]  │
│                  [0]   [1]   [2]     │
│                                      │
│   Immutable: karakter tidak bisa     │
│   diubah setelah string dibuat       │
│                                      │
└──────────────────────────────────────┘
```

### 6.1.2 Pembuatan String

Python menyediakan beberapa cara untuk membuat string:

**1. Single Quote (Kutip Tunggal)**

```python
nama = 'Ahmad Fadillah'
prodi = 'Informatika'
print(nama)   # Output: Ahmad Fadillah
print(prodi)  # Output: Informatika
```

**2. Double Quote (Kutip Ganda)**

```python
nama = "Siti Aisyah"
universitas = "Universitas Al Azhar Indonesia"
print(nama)         # Output: Siti Aisyah
print(universitas)  # Output: Universitas Al Azhar Indonesia
```

**3. Kapan Menggunakan Single vs Double Quote?**

```python
# Gunakan double quote jika string mengandung apostrof
pesan = "It's a beautiful day"
print(pesan)  # Output: It's a beautiful day

# Gunakan single quote jika string mengandung kutip ganda
html = '<div class="container">Hello</div>'
print(html)   # Output: <div class="container">Hello</div>

# Atau gunakan escape character
pesan2 = 'It\'s a beautiful day'
html2 = "<div class=\"container\">Hello</div>"
```

**4. Triple Quote (Kutip Tiga) — untuk String Multi-baris**

```python
# Triple quote memungkinkan string multi-baris
puisi = """Iqra! Bacalah!
Dengan menyebut nama Tuhanmu yang menciptakan.
Dia telah menciptakan manusia dari segumpal darah.
Bacalah, dan Tuhanmulah Yang Maha Pemurah."""

print(puisi)
```

Output:
```
Iqra! Bacalah!
Dengan menyebut nama Tuhanmu yang menciptakan.
Dia telah menciptakan manusia dari segumpal darah.
Bacalah, dan Tuhanmulah Yang Maha Pemurah.
```

```python
# Triple quote juga berguna untuk docstring (dokumentasi fungsi)
def hitung_ipk(total_mutu, total_sks):
    """
    Menghitung IPK mahasiswa.

    Parameters:
        total_mutu (float): Total nilai mutu
        total_sks (int): Total SKS yang diambil

    Returns:
        float: Nilai IPK (0.00 - 4.00)
    """
    if total_sks == 0:
        return 0.0
    return total_mutu / total_sks
```

### 6.1.3 Escape Characters

Escape characters adalah karakter khusus yang diawali dengan backslash (`\`) untuk merepresentasikan karakter yang tidak bisa diketik langsung.

| Escape Character | Deskripsi | Contoh Output |
|-----------------|-----------|---------------|
| `\n` | Baris baru (newline) | Baris 1↵Baris 2 |
| `\t` | Tab (horizontal) | Kolom1→Kolom2 |
| `\\` | Backslash literal | C:\Users\ |
| `\'` | Kutip tunggal | It's |
| `\"` | Kutip ganda | Dia berkata "Halo" |
| `\0` | Null character | (karakter kosong) |

```python
# Contoh penggunaan escape characters
print("Nama\t: Ahmad Fadillah")
print("NIM\t: 2024001001")
print("Prodi\t: Informatika")
```

Output:
```
Nama    : Ahmad Fadillah
NIM     : 2024001001
Prodi   : Informatika
```

```python
# Newline untuk membuat baris baru
print("Baris pertama\nBaris kedua\nBaris ketiga")
```

Output:
```
Baris pertama
Baris kedua
Baris ketiga
```

```python
# Backslash dalam path Windows
path = "C:\\Users\\Ahmad\\Documents\\tugas.py"
print(path)  # Output: C:\Users\Ahmad\Documents\tugas.py

# Atau gunakan raw string (awalan r) untuk menghindari escape
path_raw = r"C:\Users\Ahmad\Documents\tugas.py"
print(path_raw)  # Output: C:\Users\Ahmad\Documents\tugas.py
```

> **Tips:** Raw string (awalan `r`) sangat berguna ketika bekerja dengan path file Windows atau regular expressions, karena backslash diperlakukan sebagai karakter literal.

---

## 6.2 Operasi Dasar String

### 6.2.1 Indexing dan Negative Indexing

Setiap karakter dalam string memiliki dua jenis indeks:
- **Positive index**: dimulai dari 0 (dari kiri ke kanan)
- **Negative index**: dimulai dari -1 (dari kanan ke kiri)

```
String: "INFORMATIKA"

Positive Index:
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│  I  │  N  │  F  │  O  │  R  │  M  │  A  │  T  │  I  │  K  │  A  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│  0  │  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │  9  │ 10  │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘

Negative Index:
┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│  I  │  N  │  F  │  O  │  R  │  M  │  A  │  T  │  I  │  K  │  A  │
├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ -11 │ -10 │ -9  │ -8  │ -7  │ -6  │ -5  │ -4  │ -3  │ -2  │ -1  │
└─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
```

```python
teks = "INFORMATIKA"

# Positive indexing (dari kiri, mulai 0)
print(teks[0])   # Output: I  (karakter pertama)
print(teks[5])   # Output: M
print(teks[10])  # Output: A  (karakter terakhir)

# Negative indexing (dari kanan, mulai -1)
print(teks[-1])  # Output: A  (karakter terakhir)
print(teks[-2])  # Output: K
print(teks[-11]) # Output: I  (karakter pertama)

# IndexError jika indeks di luar jangkauan
# print(teks[11])  # IndexError: string index out of range
# print(teks[-12]) # IndexError: string index out of range
```

> **Mengapa indeks dimulai dari 0?**
> Ini adalah konvensi yang berasal dari bahasa C, di mana indeks merepresentasikan *offset* (jarak) dari awal memori. Elemen pertama memiliki offset 0 dari awal, sehingga indeksnya 0.

### 6.2.2 Slicing

**Slicing** memungkinkan kita mengambil bagian (substring) dari string menggunakan notasi `[start:stop:step]`.

**Sintaks:** `string[start:stop:step]`
- `start`: indeks awal (inklusif, default 0)
- `stop`: indeks akhir (eksklusif, TIDAK termasuk)
- `step`: langkah/lompatan (default 1)

```
Aturan Slicing: start <= indeks < stop

Contoh: teks[2:7]

    I   N   F   O   R   M   A   T   I   K   A
    0   1   2   3   4   5   6   7   8   9   10
            ^───────────────^
              start=2         stop=7 (tidak termasuk)

    Hasil: "FORMA" (indeks 2, 3, 4, 5, 6)
```

```python
teks = "INFORMATIKA"

# Slicing dasar [start:stop]
print(teks[0:4])    # Output: INFO (indeks 0,1,2,3)
print(teks[2:7])    # Output: FORMA (indeks 2,3,4,5,6)
print(teks[7:11])   # Output: TIKA (indeks 7,8,9,10)

# Mengabaikan start atau stop
print(teks[:4])     # Output: INFO (dari awal sampai indeks 3)
print(teks[7:])     # Output: TIKA (dari indeks 7 sampai akhir)
print(teks[:])      # Output: INFORMATIKA (seluruh string — copy)

# Slicing dengan step
print(teks[0:11:2]) # Output: IFRAIT (setiap 2 langkah)
print(teks[::2])    # Output: IFRAIT (sama — seluruh string, step 2)
print(teks[::3])    # Output: IOMIA (setiap 3 langkah)

# Negative step (membalik arah)
print(teks[::-1])   # Output: AKITAMROFNI (string terbalik!)
print(teks[::-2])   # Output: AIMONI (terbalik, setiap 2 langkah)

# Slicing dengan negative index
print(teks[-4:])    # Output: TIKA (4 karakter terakhir)
print(teks[-7:-3])  # Output: RMAT (indeks -7 sampai -4)
print(teks[:-3])    # Output: INFORMAT (dari awal, tanpa 3 terakhir)
```

**Slicing tidak pernah menghasilkan IndexError:**

```python
teks = "INFORMATIKA"

# Slicing aman meskipun indeks di luar jangkauan
print(teks[0:100])  # Output: INFORMATIKA (tidak error!)
print(teks[50:100]) # Output: "" (string kosong, tidak error!)
print(teks[-100:3]) # Output: INF (Python menyesuaikan otomatis)
```

> **Perbedaan penting:** Indexing (`teks[11]`) menghasilkan `IndexError` jika di luar jangkauan, tetapi slicing (`teks[0:100]`) **tidak** menghasilkan error — Python otomatis menyesuaikan ke batas string.

### 6.2.3 Concatenation dan Repetition

**Concatenation** (penggabungan) menggunakan operator `+`:

```python
# Concatenation: menggabungkan dua string
nama_depan = "Ahmad"
nama_belakang = "Fadillah"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)  # Output: Ahmad Fadillah

# Hati-hati: concatenation hanya untuk string + string
umur = 20
# print("Umur: " + umur)  # TypeError: can only concatenate str to str
print("Umur: " + str(umur))  # Output: Umur: 20

# Lebih baik gunakan f-string (akan dibahas di 6.4)
print(f"Umur: {umur}")       # Output: Umur: 20
```

**Repetition** (pengulangan) menggunakan operator `*`:

```python
# Repetition: mengulang string
garis = "=" * 50
print(garis)  # Output: ==================================================

# Berguna untuk dekorasi output
print("=" * 40)
print("   UNIVERSITAS AL AZHAR INDONESIA")
print("=" * 40)

# Membuat padding
spasi = " " * 10
print(spasi + "Teks terindentasi")  # Output:           Teks terindentasi
```

### 6.2.4 Operator `in` dan `not in`

Operator `in` memeriksa apakah suatu substring terdapat di dalam string. Hasilnya berupa boolean (`True` atau `False`).

```python
kalimat = "Selamat datang di Universitas Al Azhar Indonesia"

# Operator in
print("Azhar" in kalimat)        # Output: True
print("azhar" in kalimat)        # Output: False (case-sensitive!)
print("Universitas" in kalimat)  # Output: True
print("ITB" in kalimat)          # Output: False

# Operator not in
print("ITB" not in kalimat)      # Output: True
print("Azhar" not in kalimat)    # Output: False
```

```python
# Aplikasi praktis: validasi input
email = input("Masukkan email: ")  # Misal: ahmad@uai.ac.id

if "@" in email and "." in email:
    print("Format email valid")
else:
    print("Format email tidak valid!")

# Cek domain email UAI
if email.endswith("@uai.ac.id"):
    print("Email resmi UAI")
```

### 6.2.5 Fungsi `len()`

Fungsi `len()` mengembalikan jumlah karakter dalam string, termasuk spasi dan karakter khusus.

```python
teks1 = "Informatika"
teks2 = "Al Azhar"
teks3 = ""           # String kosong
teks4 = "   "        # 3 spasi (bukan kosong!)
teks5 = "Baris 1\nBaris 2"  # Berisi newline

print(len(teks1))  # Output: 11
print(len(teks2))  # Output: 8  (spasi dihitung!)
print(len(teks3))  # Output: 0
print(len(teks4))  # Output: 3  (spasi dihitung!)
print(len(teks5))  # Output: 15 (\n dihitung sebagai 1 karakter)
```

```python
# Aplikasi: validasi panjang input
password = input("Masukkan password: ")

if len(password) < 8:
    print("Password terlalu pendek! Minimal 8 karakter.")
elif len(password) > 20:
    print("Password terlalu panjang! Maksimal 20 karakter.")
else:
    print(f"Password diterima ({len(password)} karakter)")
```

---

## 6.3 String Methods

String di Python memiliki banyak **methods** (fungsi bawaan) yang sangat berguna untuk pengolahan teks. Methods dipanggil menggunakan notasi titik: `string.method()`.

> **Ingat:** Karena string bersifat immutable, semua string methods **mengembalikan string baru** — string asli tidak berubah.

### 6.3.1 Case Methods (Pengubahan Huruf Besar/Kecil)

```python
teks = "universitas al azhar indonesia"

# upper() — semua huruf besar
print(teks.upper())
# Output: UNIVERSITAS AL AZHAR INDONESIA

# lower() — semua huruf kecil
print("INFORMATIKA UAI".lower())
# Output: informatika uai

# title() — huruf pertama setiap kata kapital
print(teks.title())
# Output: Universitas Al Azhar Indonesia

# capitalize() — hanya huruf pertama string yang kapital
print(teks.capitalize())
# Output: Universitas al azhar indonesia

# swapcase() — tukar besar/kecil
print("Informatika UAI".swapcase())
# Output: iNFORMATIKA uai
```

```python
# Aplikasi: case-insensitive comparison
jawaban = input("Apakah Anda setuju? (ya/tidak): ")

# Tanpa normalisasi — banyak kemungkinan yang harus dicek
# if jawaban == "ya" or jawaban == "Ya" or jawaban == "YA" or jawaban == "yA":

# Dengan normalisasi — cukup satu pengecekan
if jawaban.lower() == "ya":
    print("Terima kasih atas persetujuannya!")
else:
    print("Baik, dicatat.")
```

### 6.3.2 Search Methods (Pencarian dalam String)

```python
teks = "Bismillahirrahmanirrahim, dengan nama Allah yang Maha Pengasih lagi Maha Penyayang"

# find(sub) — cari posisi pertama substring, return -1 jika tidak ada
print(teks.find("Allah"))     # Output: 36
print(teks.find("allah"))     # Output: -1 (case-sensitive)
print(teks.find("xyz"))       # Output: -1

# find(sub, start, end) — cari di range tertentu
print(teks.find("Maha", 0))   # Output: 47 (Maha pertama)
print(teks.find("Maha", 48))  # Output: 67 (Maha kedua)

# index(sub) — sama seperti find, tapi menghasilkan ValueError jika tidak ada
print(teks.index("Allah"))    # Output: 36
# print(teks.index("xyz"))    # ValueError: substring not found

# count(sub) — hitung kemunculan substring
print(teks.count("Maha"))     # Output: 2
print(teks.count("a"))        # Output: 12

# startswith(prefix) — cek apakah string diawali dengan prefix
print(teks.startswith("Bismillah"))  # Output: True
print(teks.startswith("bismillah"))  # Output: False

# endswith(suffix) — cek apakah string diakhiri dengan suffix
print(teks.endswith("Penyayang"))   # Output: True
print(teks.endswith("."))           # Output: False
```

```python
# Aplikasi: mencari semua kemunculan substring
teks = "Python adalah bahasa pemrograman. Python mudah dipelajari. Python sangat populer."

kata = "Python"
posisi = 0
kemunculan = []

while True:
    posisi = teks.find(kata, posisi)
    if posisi == -1:
        break
    kemunculan.append(posisi)
    posisi += 1  # Lanjut cari dari posisi berikutnya

print(f"'{kata}' ditemukan di posisi: {kemunculan}")
# Output: 'Python' ditemukan di posisi: [0, 33, 59]
print(f"Total kemunculan: {len(kemunculan)}")
# Output: Total kemunculan: 3
```

### 6.3.3 Modification Methods (Modifikasi String)

```python
# replace(old, new) — ganti substring
teks = "Saya suka Java. Java itu bagus."
teks_baru = teks.replace("Java", "Python")
print(teks_baru)
# Output: Saya suka Python. Python itu bagus.

# replace dengan limit (jumlah penggantian maksimum)
teks_baru2 = teks.replace("Java", "Python", 1)  # Ganti hanya yang pertama
print(teks_baru2)
# Output: Saya suka Python. Java itu bagus.
```

```python
# strip() — hapus whitespace di awal dan akhir
data = "   Ahmad Fadillah   "
print(f"'{data}'")            # Output: '   Ahmad Fadillah   '
print(f"'{data.strip()}'")    # Output: 'Ahmad Fadillah'

# lstrip() — hapus whitespace di kiri saja
print(f"'{data.lstrip()}'")   # Output: 'Ahmad Fadillah   '

# rstrip() — hapus whitespace di kanan saja
print(f"'{data.rstrip()}'")   # Output: '   Ahmad Fadillah'

# strip dengan karakter tertentu
nomor = "---001234---"
print(nomor.strip("-"))        # Output: 001234
```

```python
# split() — pecah string menjadi list
kalimat = "Informatika adalah prodi terbaik"
kata_kata = kalimat.split()    # Split by whitespace (default)
print(kata_kata)
# Output: ['Informatika', 'adalah', 'prodi', 'terbaik']

# split dengan delimiter tertentu
data_csv = "Ahmad,20,Informatika,3.85"
kolom = data_csv.split(",")
print(kolom)
# Output: ['Ahmad', '20', 'Informatika', '3.85']

# split dengan maxsplit
teks = "satu-dua-tiga-empat-lima"
print(teks.split("-", 2))     # Split maksimal 2 kali
# Output: ['satu', 'dua', 'tiga-empat-lima']
```

```python
# join() — gabungkan list menjadi string (kebalikan split)
kata_kata = ['Informatika', 'adalah', 'prodi', 'terbaik']
kalimat = " ".join(kata_kata)
print(kalimat)
# Output: Informatika adalah prodi terbaik

# join dengan delimiter berbeda
data = ['Ahmad', '20', 'Informatika']
csv_line = ",".join(data)
print(csv_line)
# Output: Ahmad,20,Informatika

# join untuk membuat path
bagian_path = ["home", "user", "documents", "tugas.py"]
path = "/".join(bagian_path)
print(path)
# Output: home/user/documents/tugas.py
```

### 6.3.4 Validation Methods (Validasi Karakter)

```python
# isalpha() — True jika semua karakter adalah huruf
print("Informatika".isalpha())    # Output: True
print("Informatika UAI".isalpha()) # Output: False (ada spasi)
print("Info123".isalpha())         # Output: False (ada angka)
print("".isalpha())                # Output: False (string kosong)

# isdigit() — True jika semua karakter adalah digit
print("12345".isdigit())           # Output: True
print("123.45".isdigit())          # Output: False (ada titik)
print("12 34".isdigit())           # Output: False (ada spasi)

# isalnum() — True jika semua karakter adalah huruf ATAU digit
print("Info123".isalnum())         # Output: True
print("Info 123".isalnum())        # Output: False (ada spasi)

# isspace() — True jika semua karakter adalah whitespace
print("   ".isspace())             # Output: True
print(" \t\n".isspace())           # Output: True
print("  a  ".isspace())           # Output: False
```

```python
# Aplikasi: validasi input
nim = input("Masukkan NIM: ")

if not nim.isdigit():
    print("NIM harus berupa angka!")
elif len(nim) != 10:
    print("NIM harus 10 digit!")
else:
    print(f"NIM {nim} valid.")
```

### Tabel Ringkasan String Methods

Berikut adalah ringkasan seluruh string methods yang telah dibahas:

```
┌─────────────────┬───────────────────────────────────────────────────────┐
│ Kategori        │ Method dan Penjelasan Singkat                        │
├─────────────────┼───────────────────────────────────────────────────────┤
│                 │ upper()      → Semua huruf besar                     │
│ Case            │ lower()      → Semua huruf kecil                     │
│ Methods         │ title()      → Kapital tiap kata                     │
│                 │ capitalize() → Kapital huruf pertama saja            │
│                 │ swapcase()   → Tukar besar/kecil                     │
├─────────────────┼───────────────────────────────────────────────────────┤
│                 │ find()       → Cari posisi substring (-1 jika tak    │
│ Search          │                ada)                                  │
│ Methods         │ index()      → Cari posisi (error jika tak ada)      │
│                 │ count()      → Hitung jumlah kemunculan              │
│                 │ startswith() → Cek awalan string                     │
│                 │ endswith()   → Cek akhiran string                    │
├─────────────────┼───────────────────────────────────────────────────────┤
│                 │ replace()    → Ganti substring                       │
│ Modification    │ strip()      → Hapus whitespace awal/akhir           │
│ Methods         │ lstrip()     → Hapus whitespace kiri                 │
│                 │ rstrip()     → Hapus whitespace kanan                │
│                 │ split()      → Pecah string → list                   │
│                 │ join()       → Gabung list → string                  │
├─────────────────┼───────────────────────────────────────────────────────┤
│                 │ isalpha()    → True jika semua huruf                 │
│ Validation      │ isdigit()    → True jika semua digit                 │
│ Methods         │ isalnum()    → True jika huruf/digit                 │
│                 │ isspace()    → True jika whitespace                  │
│                 │ isupper()    → True jika semua huruf besar           │
│                 │ islower()    → True jika semua huruf kecil           │
└─────────────────┴───────────────────────────────────────────────────────┘
```

---

## 6.4 String Formatting

String formatting adalah teknik untuk menyisipkan nilai variabel ke dalam string. Python menyediakan tiga cara utama, dengan **f-string** sebagai cara yang paling modern dan direkomendasikan.

### 6.4.1 f-strings (Format Terbaru dan Direkomendasikan)

f-string (formatted string literal) diperkenalkan di Python 3.6. Diawali dengan huruf `f` sebelum tanda kutip, dan ekspresi Python ditempatkan di dalam kurung kurawal `{}`.

```python
nama = "Ahmad"
umur = 20
ipk = 3.85

# f-string dasar
print(f"Nama: {nama}")
print(f"Umur: {umur} tahun")
print(f"IPK: {ipk}")
```

Output:
```
Nama: Ahmad
Umur: 20 tahun
IPK: 3.85
```

```python
# f-string dengan ekspresi
panjang = 5
lebar = 3
print(f"Luas persegi panjang: {panjang * lebar} cm²")
# Output: Luas persegi panjang: 15 cm²

# f-string dengan method call
nama = "ahmad fadillah"
print(f"Nama: {nama.title()}")
# Output: Nama: Ahmad Fadillah

# f-string dengan conditional expression
nilai = 85
print(f"Status: {'Lulus' if nilai >= 60 else 'Tidak Lulus'}")
# Output: Status: Lulus
```

```python
# f-string multi-baris
nama = "Siti Aisyah"
nim = "2024001042"
prodi = "Informatika"

kartu = f"""
╔══════════════════════════════════╗
║   KARTU MAHASISWA UAI            ║
║──────────────────────────────────║
║   Nama  : {nama:<20}  ║
║   NIM   : {nim:<20}  ║
║   Prodi : {prodi:<20}  ║
╚══════════════════════════════════╝
"""
print(kartu)
```

### 6.4.2 Method `.format()`

Method `.format()` tersedia sejak Python 2.7/3.0 dan masih banyak digunakan di kode yang sudah ada.

```python
# .format() dasar
print("Nama: {}, Umur: {}".format("Ahmad", 20))
# Output: Nama: Ahmad, Umur: 20

# .format() dengan index
print("{0} belajar {1}. {0} suka {1}.".format("Ahmad", "Python"))
# Output: Ahmad belajar Python. Ahmad suka Python.

# .format() dengan named arguments
print("Nama: {nama}, Prodi: {prodi}".format(nama="Ahmad", prodi="Informatika"))
# Output: Nama: Ahmad, Prodi: Informatika
```

### 6.4.3 %-formatting (Format Lama)

Cara ini berasal dari bahasa C dan masih bisa ditemukan di kode Python lama. **Tidak direkomendasikan** untuk kode baru.

```python
# %-formatting (cara lama)
nama = "Ahmad"
umur = 20
ipk = 3.85

print("Nama: %s" % nama)             # %s = string
print("Umur: %d tahun" % umur)       # %d = integer
print("IPK: %.2f" % ipk)             # %.2f = float 2 desimal
print("Nama: %s, Umur: %d" % (nama, umur))  # Multiple values

# Output:
# Nama: Ahmad
# Umur: 20 tahun
# IPK: 3.85
# Nama: Ahmad, Umur: 20
```

> **Rekomendasi:** Gunakan **f-string** untuk semua kode baru. f-string lebih mudah dibaca, lebih cepat, dan lebih fleksibel. Ketahui `%`-formatting dan `.format()` hanya untuk membaca kode lama.

### 6.4.4 Format Specifiers (Spesifikasi Format)

Format specifiers mengontrol bagaimana nilai ditampilkan (lebar, alignment, presisi, dsb.).

**Sintaks:** `{value:format_spec}`

```
Format spec: [[fill]align][sign][#][0][width][grouping_option][.precision][type]

Alignment:
  <  : rata kiri (default untuk string)
  >  : rata kanan (default untuk angka)
  ^  : rata tengah

Type:
  s  : string (default)
  d  : integer
  f  : float
  e  : scientific notation
  %  : persentase
  ,  : pemisah ribuan
```

```python
# Padding dan alignment
nama = "Ahmad"
print(f"|{nama:<20}|")  # Rata kiri, lebar 20
print(f"|{nama:>20}|")  # Rata kanan, lebar 20
print(f"|{nama:^20}|")  # Rata tengah, lebar 20
print(f"|{nama:*^20}|") # Rata tengah, fill dengan *
```

Output:
```
|Ahmad               |
|               Ahmad|
|       Ahmad        |
|*******Ahmad********|
```

```python
# Number formatting
angka = 1234567.89

print(f"Default     : {angka}")
print(f"2 desimal   : {angka:.2f}")
print(f"Ribuan      : {angka:,.2f}")
print(f"Lebar 20    : {angka:>20,.2f}")
print(f"Leading 0   : {42:05d}")
print(f"Persentase  : {0.856:.1%}")
print(f"Scientific  : {angka:.2e}")
```

Output:
```
Default     : 1234567.89
2 desimal   : 1234567.89
Ribuan      : 1,234,567.89
Lebar 20    :        1,234,567.89
Leading 0   : 00042
Persentase  : 85.6%
Scientific  : 1.23e+06
```

```python
# Aplikasi: tabel laporan akademik
mahasiswa = [
    ("Ahmad Fadillah", "2024001001", 3.85),
    ("Siti Aisyah", "2024001042", 3.92),
    ("Budi Santoso", "2024001015", 3.45),
    ("Dewi Lestari", "2024001028", 3.78),
]

print("=" * 55)
print(f"{'DAFTAR MAHASISWA INFORMATIKA UAI':^55}")
print("=" * 55)
print(f"{'No':<4} {'Nama':<20} {'NIM':<14} {'IPK':>6}")
print("-" * 55)

for i, (nama, nim, ipk) in enumerate(mahasiswa, 1):
    print(f"{i:<4} {nama:<20} {nim:<14} {ipk:>6.2f}")

print("-" * 55)
rata_ipk = sum(m[2] for m in mahasiswa) / len(mahasiswa)
print(f"{'Rata-rata IPK':>38} {rata_ipk:>6.2f}")
print("=" * 55)
```

Output:
```
=======================================================
         DAFTAR MAHASISWA INFORMATIKA UAI
=======================================================
No   Nama                 NIM            IPK
-------------------------------------------------------
1    Ahmad Fadillah       2024001001       3.85
2    Siti Aisyah          2024001042       3.92
3    Budi Santoso         2024001015       3.45
4    Dewi Lestari         2024001028       3.78
-------------------------------------------------------
                          Rata-rata IPK    3.75
=======================================================
```

---

## 6.5 Iterasi pada String

### 6.5.1 Loop pada String

Karena string adalah sequence, kita bisa mengiterasinya menggunakan `for` loop — setiap iterasi mengambil satu karakter.

```python
# Iterasi karakter per karakter
nama = "UAI"
for karakter in nama:
    print(karakter)

# Output:
# U
# A
# I
```

```python
# Iterasi menggunakan indeks
nama = "INFORMATIKA"
for i in range(len(nama)):
    print(f"Indeks {i:>2}: '{nama[i]}'")

# Output:
# Indeks  0: 'I'
# Indeks  1: 'N'
# Indeks  2: 'F'
# ...
# Indeks 10: 'A'
```

### 6.5.2 Enumerate

Fungsi `enumerate()` memberikan akses ke indeks dan karakter secara bersamaan — cara yang lebih *Pythonic* dibandingkan `range(len(...))`.

```python
nama = "INFORMATIKA"
for indeks, karakter in enumerate(nama):
    print(f"[{indeks:>2}] {karakter}")

# Output:
# [ 0] I
# [ 1] N
# [ 2] F
# [ 3] O
# [ 4] R
# [ 5] M
# [ 6] A
# [ 7] T
# [ 8] I
# [ 9] K
# [10] A
```

```python
# enumerate() dengan start parameter
kalimat = "Python"
for nomor, huruf in enumerate(kalimat, start=1):
    print(f"Huruf ke-{nomor}: {huruf}")

# Output:
# Huruf ke-1: P
# Huruf ke-2: y
# Huruf ke-3: t
# Huruf ke-4: h
# Huruf ke-5: o
# Huruf ke-6: n
```

### 6.5.3 Pola-pola Umum Pengolahan String

**Pola 1: Menghitung Karakter Tertentu**

```python
def hitung_vokal(teks):
    """Menghitung jumlah huruf vokal dalam teks."""
    vokal = "aiueoAIUEO"
    jumlah = 0
    for karakter in teks:
        if karakter in vokal:
            jumlah += 1
    return jumlah

kalimat = "Universitas Al Azhar Indonesia"
print(f"Jumlah vokal: {hitung_vokal(kalimat)}")
# Output: Jumlah vokal: 15
```

**Pola 2: Membangun String Baru**

```python
def hapus_vokal(teks):
    """Menghapus semua huruf vokal dari teks."""
    vokal = "aiueoAIUEO"
    hasil = ""
    for karakter in teks:
        if karakter not in vokal:
            hasil += karakter
    return hasil

print(hapus_vokal("Informatika"))
# Output: nfrmtk
```

**Pola 3: Membalik String (Reverse)**

```python
# Cara 1: Slicing (paling sederhana)
teks = "Python"
print(teks[::-1])  # Output: nohtyP

# Cara 2: Loop
def balik_string(teks):
    """Membalik string menggunakan loop."""
    hasil = ""
    for karakter in teks:
        hasil = karakter + hasil  # Tambahkan di depan
    return hasil

print(balik_string("Python"))  # Output: nohtyP

# Cara 3: Menggunakan reversed() dan join()
print("".join(reversed("Python")))  # Output: nohtyP
```

**Pola 4: Cek Palindrome**

Palindrome adalah string yang sama jika dibaca dari depan maupun belakang (contoh: "katak", "level").

```python
def is_palindrome(teks):
    """
    Memeriksa apakah teks adalah palindrome.
    Mengabaikan spasi dan huruf besar/kecil.
    """
    # Normalisasi: hapus spasi, ubah ke huruf kecil
    teks_bersih = teks.replace(" ", "").lower()
    return teks_bersih == teks_bersih[::-1]

# Pengujian
kata_kata = ["katak", "level", "racecar", "python", "kodok", "malam"]
for kata in kata_kata:
    status = "palindrome" if is_palindrome(kata) else "bukan palindrome"
    print(f"  '{kata}' → {status}")
```

Output:
```
  'katak' → palindrome
  'level' → palindrome
  'racecar' → palindrome
  'python' → bukan palindrome
  'kodok' → bukan palindrome
  'malam' → palindrome
```

**Pola 5: Menghitung Frekuensi Karakter**

```python
def frekuensi_karakter(teks):
    """Menghitung frekuensi setiap karakter dalam teks."""
    freq = {}
    for karakter in teks.lower():
        if karakter.isalpha():  # Hanya huruf
            if karakter in freq:
                freq[karakter] += 1
            else:
                freq[karakter] = 1
    return freq

teks = "Universitas Al Azhar Indonesia"
freq = frekuensi_karakter(teks)

# Urutkan berdasarkan frekuensi (terbanyak dulu)
freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("Frekuensi karakter:")
for huruf, jumlah in freq_sorted:
    bar = "█" * jumlah
    print(f"  '{huruf}': {jumlah:>2} {bar}")
```

Output:
```
Frekuensi karakter:
  'a': 5 █████
  'i': 4 ████
  'n': 3 ███
  's': 3 ███
  'r': 2 ██
  'e': 2 ██
  'u': 1 █
  'v': 1 █
  't': 1 █
  'l': 1 █
  'z': 1 █
  'h': 1 █
  'd': 1 █
  'o': 1 █
```

---

## 6.6 Studi Kasus Pengolahan Teks

### 6.6.1 Word Counter Bahasa Indonesia

Program ini menghitung statistik teks dalam bahasa Indonesia: jumlah kata, kalimat, karakter, dan kata yang paling sering muncul.

```python
# =============================================
# WORD COUNTER BAHASA INDONESIA
# Studi Kasus Bab 6 - String
# =============================================

def hitung_kata(teks):
    """Menghitung jumlah kata dalam teks."""
    kata_kata = teks.split()
    return len(kata_kata)

def hitung_kalimat(teks):
    """Menghitung jumlah kalimat (berdasarkan tanda titik, tanya, seru)."""
    jumlah = 0
    for karakter in teks:
        if karakter in ".?!":
            jumlah += 1
    return max(jumlah, 1)  # Minimal 1 kalimat

def hitung_karakter(teks, termasuk_spasi=True):
    """Menghitung jumlah karakter."""
    if termasuk_spasi:
        return len(teks)
    else:
        return len(teks.replace(" ", ""))

def kata_terbanyak(teks, top_n=5):
    """Mencari kata yang paling sering muncul."""
    # Bersihkan tanda baca
    teks_bersih = ""
    for karakter in teks.lower():
        if karakter.isalnum() or karakter == " ":
            teks_bersih += karakter

    kata_kata = teks_bersih.split()

    # Hitung frekuensi (tanpa menggunakan collections.Counter)
    frekuensi = {}
    for kata in kata_kata:
        if kata in frekuensi:
            frekuensi[kata] += 1
        else:
            frekuensi[kata] = 1

    # Urutkan berdasarkan frekuensi
    sorted_freq = sorted(frekuensi.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq[:top_n]

def word_counter(teks):
    """Fungsi utama Word Counter."""
    print("=" * 50)
    print(f"{'WORD COUNTER BAHASA INDONESIA':^50}")
    print("=" * 50)

    jml_kata = hitung_kata(teks)
    jml_kalimat = hitung_kalimat(teks)
    jml_karakter = hitung_karakter(teks)
    jml_karakter_no_space = hitung_karakter(teks, False)
    rata_kata_per_kalimat = jml_kata / jml_kalimat

    print(f"\n{'Statistik Teks':}")
    print(f"  Jumlah kata           : {jml_kata}")
    print(f"  Jumlah kalimat        : {jml_kalimat}")
    print(f"  Jumlah karakter       : {jml_karakter}")
    print(f"  Karakter (tanpa spasi): {jml_karakter_no_space}")
    print(f"  Rata-rata kata/kalimat: {rata_kata_per_kalimat:.1f}")

    print(f"\n{'Top 5 Kata Terbanyak':}")
    top_kata = kata_terbanyak(teks)
    for i, (kata, freq) in enumerate(top_kata, 1):
        bar = "█" * freq
        print(f"  {i}. '{kata}' → {freq}x {bar}")

    print("=" * 50)

# Pengujian
paragraf = """Universitas Al Azhar Indonesia adalah universitas swasta yang terletak
di Jakarta Selatan. Universitas ini memiliki berbagai program studi unggulan.
Program studi Informatika adalah salah satu program studi yang diminati
oleh banyak mahasiswa. Mahasiswa Informatika belajar algoritma dan pemrograman
sebagai fondasi utama. Algoritma adalah langkah-langkah sistematis untuk
menyelesaikan masalah."""

word_counter(paragraf)
```

Output:
```
==================================================
         WORD COUNTER BAHASA INDONESIA
==================================================

Statistik Teks:
  Jumlah kata           : 46
  Jumlah kalimat        : 5
  Jumlah karakter       : 342
  Karakter (tanpa spasi): 297
  Rata-rata kata/kalimat: 9.2

Top 5 Kata Terbanyak:
  1. 'program' → 3x ███
  2. 'studi' → 3x ███
  3. 'adalah' → 3x ███
  4. 'universitas' → 2x ██
  5. 'informatika' → 2x ██
==================================================
```

### 6.6.2 Caesar Cipher Sederhana

Caesar Cipher adalah teknik enkripsi paling sederhana, di mana setiap huruf digeser sejumlah posisi tertentu dalam alfabet. Teknik ini dinamai dari Julius Caesar yang menggunakannya untuk komunikasi militer.

```
Contoh Caesar Cipher dengan pergeseran (shift) = 3:

Alfabet asli    : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Alfabet cipher  : D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

"PYTHON" → "SBWKRQ"
```

```python
# =============================================
# CAESAR CIPHER SEDERHANA
# Studi Kasus Bab 6 - String
# =============================================

def caesar_encrypt(teks, shift):
    """
    Mengenkripsi teks menggunakan Caesar Cipher.

    Parameters:
        teks (str): Teks yang akan dienkripsi
        shift (int): Jumlah pergeseran (1-25)

    Returns:
        str: Teks terenkripsi
    """
    hasil = ""

    for karakter in teks:
        if karakter.isalpha():
            # Tentukan basis ASCII (A=65 untuk huruf besar, a=97 untuk kecil)
            basis = ord('A') if karakter.isupper() else ord('a')

            # Geser karakter dan wrap around menggunakan modulo
            posisi_asli = ord(karakter) - basis
            posisi_baru = (posisi_asli + shift) % 26
            karakter_baru = chr(basis + posisi_baru)

            hasil += karakter_baru
        else:
            # Karakter non-huruf tidak diubah
            hasil += karakter

    return hasil

def caesar_decrypt(teks, shift):
    """
    Mendekripsi teks Caesar Cipher.
    Dekripsi = enkripsi dengan shift negatif.
    """
    return caesar_encrypt(teks, -shift)

# Pengujian
print("=" * 50)
print(f"{'CAESAR CIPHER':^50}")
print("=" * 50)

pesan_asli = "Informatika UAI adalah yang terbaik!"
shift = 7

pesan_enkripsi = caesar_encrypt(pesan_asli, shift)
pesan_dekripsi = caesar_decrypt(pesan_enkripsi, shift)

print(f"\nShift        : {shift}")
print(f"Pesan asli   : {pesan_asli}")
print(f"Terenkripsi  : {pesan_enkripsi}")
print(f"Terdekripsi  : {pesan_dekripsi}")
print(f"Cocok?       : {pesan_asli == pesan_dekripsi}")
print("=" * 50)

# Demonstrasi brute force (mencoba semua kemungkinan shift)
print(f"\n{'BRUTE FORCE DECRYPTION':^50}")
print("-" * 50)
cipher = "Pumvythapbh"
for s in range(1, 26):
    hasil = caesar_decrypt(cipher, s)
    # Tandai jika hasilnya mengandung kata yang dikenal
    marker = " <<<" if "informatika" in hasil.lower() else ""
    print(f"  Shift {s:>2}: {hasil}{marker}")
```

### 6.6.3 Validator NIK (Nomor Induk Kependudukan)

NIK (Nomor Induk Kependudukan) adalah nomor identitas 16 digit yang dimiliki setiap warga negara Indonesia. Struktur NIK mengandung informasi penting tentang domisili dan tanggal lahir pemiliknya.

```
Struktur NIK (16 digit):
┌──┬──┬──┬──────┬──┬──┬──┬──────────────┐
│PP│KK│KC│DDMMYY│SS│SS│SS│SSSS          │
├──┴──┴──┼──────┼──┴──┴──┴──────────────┤
│        │      │                        │
│ Kode   │Tgl   │ Nomor urut             │
│ Wilayah│Lahir │ registrasi             │
│(6 dig) │(6dig)│ (4 digit)              │
└────────┴──────┴────────────────────────┘

PP = Kode Provinsi (2 digit)
KK = Kode Kabupaten/Kota (2 digit)
KC = Kode Kecamatan (2 digit)
DD = Tanggal lahir (01-31, +40 untuk perempuan: 41-71)
MM = Bulan lahir (01-12)
YY = Tahun lahir (2 digit terakhir)
```

```python
# =============================================
# VALIDATOR NIK
# Studi Kasus Bab 6 - String
# =============================================

def validasi_nik(nik):
    """
    Memvalidasi format NIK dan mengekstrak informasi.

    Parameters:
        nik (str): Nomor Induk Kependudukan (16 digit)

    Returns:
        dict: Informasi hasil validasi
    """
    hasil = {
        "valid": True,
        "pesan": [],
        "info": {}
    }

    # 1. Cek panjang
    if len(nik) != 16:
        hasil["valid"] = False
        hasil["pesan"].append(f"Panjang NIK harus 16 digit (ditemukan: {len(nik)} digit)")
        return hasil

    # 2. Cek apakah semua digit
    if not nik.isdigit():
        hasil["valid"] = False
        hasil["pesan"].append("NIK harus berisi angka saja")
        return hasil

    # 3. Ekstrak komponen NIK menggunakan slicing
    kode_provinsi = nik[0:2]
    kode_kabupaten = nik[2:4]
    kode_kecamatan = nik[4:6]
    tanggal_lahir = int(nik[6:8])
    bulan_lahir = int(nik[8:10])
    tahun_lahir = nik[10:12]
    nomor_urut = nik[12:16]

    # 4. Tentukan jenis kelamin dari tanggal
    if tanggal_lahir > 40:
        jenis_kelamin = "Perempuan"
        tanggal_lahir -= 40  # Kurangi 40 untuk mendapatkan tanggal asli
    else:
        jenis_kelamin = "Laki-laki"

    # 5. Validasi tanggal lahir
    if tanggal_lahir < 1 or tanggal_lahir > 31:
        hasil["valid"] = False
        hasil["pesan"].append(f"Tanggal lahir tidak valid: {tanggal_lahir}")

    # 6. Validasi bulan lahir
    if bulan_lahir < 1 or bulan_lahir > 12:
        hasil["valid"] = False
        hasil["pesan"].append(f"Bulan lahir tidak valid: {bulan_lahir}")

    # 7. Daftar provinsi (sebagian)
    daftar_provinsi = {
        "11": "Aceh", "12": "Sumatera Utara", "13": "Sumatera Barat",
        "14": "Riau", "15": "Jambi", "16": "Sumatera Selatan",
        "17": "Bengkulu", "18": "Lampung", "19": "Bangka Belitung",
        "21": "Kepulauan Riau",
        "31": "DKI Jakarta", "32": "Jawa Barat", "33": "Jawa Tengah",
        "34": "DI Yogyakarta", "35": "Jawa Timur", "36": "Banten",
        "51": "Bali", "52": "NTB", "53": "NTT",
        "61": "Kalimantan Barat", "62": "Kalimantan Tengah",
        "63": "Kalimantan Selatan", "64": "Kalimantan Timur",
        "71": "Sulawesi Utara", "72": "Sulawesi Tengah",
        "73": "Sulawesi Selatan", "74": "Sulawesi Tenggara",
        "81": "Maluku", "82": "Maluku Utara",
        "91": "Papua", "92": "Papua Barat",
    }

    nama_provinsi = daftar_provinsi.get(kode_provinsi, "Tidak diketahui")
    if nama_provinsi == "Tidak diketahui":
        hasil["pesan"].append(f"Kode provinsi '{kode_provinsi}' tidak dikenal")

    # Nama bulan
    nama_bulan = ["", "Januari", "Februari", "Maret", "April", "Mei",
                  "Juni", "Juli", "Agustus", "September", "Oktober",
                  "November", "Desember"]

    # Simpan informasi
    hasil["info"] = {
        "nik": nik,
        "provinsi": f"{nama_provinsi} ({kode_provinsi})",
        "kab_kota": kode_kabupaten,
        "kecamatan": kode_kecamatan,
        "tanggal_lahir": f"{tanggal_lahir:02d} {nama_bulan[bulan_lahir]} 19{tahun_lahir}/20{tahun_lahir}",
        "jenis_kelamin": jenis_kelamin,
        "nomor_urut": nomor_urut,
    }

    return hasil


# Pengujian
print("=" * 50)
print(f"{'VALIDATOR NIK':^50}")
print("=" * 50)

daftar_nik = [
    "3175014501990003",  # Contoh NIK wanita DKI Jakarta
    "3201011505020001",  # Contoh NIK pria Jawa Barat
    "123",               # NIK terlalu pendek
    "31750145019900AB",  # NIK mengandung huruf
]

for nik in daftar_nik:
    print(f"\nNIK: {nik}")
    print("-" * 40)
    result = validasi_nik(nik)

    if result["valid"]:
        info = result["info"]
        print(f"  Status       : VALID")
        print(f"  Provinsi     : {info['provinsi']}")
        print(f"  Jenis Kelamin: {info['jenis_kelamin']}")
        print(f"  Tanggal Lahir: {info['tanggal_lahir']}")
        print(f"  No. Urut     : {info['nomor_urut']}")
    else:
        print(f"  Status       : TIDAK VALID")
        for pesan in result["pesan"]:
            print(f"  Alasan       : {pesan}")
```

### 6.6.4 Text Formatter

Program yang membersihkan dan memformat teks: menghapus spasi berlebih, memperbaiki kapitalisasi kalimat, dan menormalisasi whitespace.

```python
# =============================================
# TEXT FORMATTER
# Studi Kasus Bab 6 - String
# =============================================

def hapus_spasi_berlebih(teks):
    """Menghapus spasi berlebih (multiple spaces → single space)."""
    kata_kata = teks.split()  # split() otomatis memecah berdasarkan whitespace
    return " ".join(kata_kata)

def kapitalisasi_kalimat(teks):
    """
    Mengkapitalkan huruf pertama setiap kalimat.
    Kalimat dipisahkan oleh '.', '?', atau '!'.
    """
    hasil = ""
    kapitalkan_berikutnya = True

    for karakter in teks:
        if kapitalkan_berikutnya and karakter.isalpha():
            hasil += karakter.upper()
            kapitalkan_berikutnya = False
        else:
            hasil += karakter

        if karakter in ".?!":
            kapitalkan_berikutnya = True

    return hasil

def normalisasi_tanda_baca(teks):
    """Memastikan ada spasi setelah tanda baca, dan tidak ada spasi sebelumnya."""
    tanda_baca = ".,:;!?"

    hasil = ""
    for i, karakter in enumerate(teks):
        if karakter in tanda_baca:
            # Hapus spasi sebelum tanda baca
            hasil = hasil.rstrip()
            hasil += karakter
            # Pastikan ada spasi setelah tanda baca (kecuali akhir teks)
            if i + 1 < len(teks) and teks[i + 1] not in " \n":
                hasil += " "
        else:
            hasil += karakter

    return hasil

def format_teks(teks):
    """Fungsi utama: memformat teks."""
    print("=" * 60)
    print(f"{'TEXT FORMATTER':^60}")
    print("=" * 60)
    print(f"\nTEKS ASLI:")
    print(f'  "{teks}"')

    # Langkah 1: Hapus spasi berlebih
    teks = hapus_spasi_berlebih(teks)

    # Langkah 2: Normalisasi tanda baca
    teks = normalisasi_tanda_baca(teks)

    # Langkah 3: Kapitalisasi kalimat
    teks = kapitalisasi_kalimat(teks)

    print(f"\nTEKS TERFORMAT:")
    print(f'  "{teks}"')
    print("=" * 60)
    return teks


# Pengujian
teks_berantakan = "  halo   ,selamat    datang di   universitas al azhar indonesia .  kami   senang  menyambut   anda!   semoga  belajar   dengan    baik .  "

format_teks(teks_berantakan)
```

Output:
```
============================================================
                      TEXT FORMATTER
============================================================

TEKS ASLI:
  "  halo   ,selamat    datang di   universitas al azhar indonesia .  kami   senang  menyambut   anda!   semoga  belajar   dengan    baik .  "

TEKS TERFORMAT:
  "Halo, selamat datang di universitas al azhar indonesia. Kami senang menyambut anda! Semoga belajar dengan baik."
============================================================
```

---

## AI Corner: AI untuk Pengolahan Teks

**Level: Menengah**

AI (seperti ChatGPT, Gemini, atau Claude) dapat menjadi alat bantu yang sangat berguna untuk pengolahan teks. Pada level ini, kita akan memanfaatkan AI untuk tugas-tugas yang lebih kompleks dibandingkan bab-bab sebelumnya.

### Meminta AI Membantu Regex Patterns

Regular expressions (regex) adalah topik lanjutan yang sangat berguna untuk pengolahan teks. AI dapat membantu Anda memahami dan membuat regex patterns:

> **Contoh prompt:**
> "Buatkan saya regex pattern Python untuk memvalidasi format email mahasiswa UAI (harus berakhiran @uai.ac.id). Jelaskan setiap bagian dari pattern tersebut."

AI mungkin memberikan jawaban seperti:

```python
import re

pattern = r'^[a-zA-Z0-9._%+-]+@uai\.ac\.id$'

# Penjelasan:
# ^                → awal string
# [a-zA-Z0-9._%+-]+ → satu atau lebih karakter valid untuk username
# @                → karakter @ literal
# uai\.ac\.id      → domain uai.ac.id (titik di-escape)
# $                → akhir string

email_list = [
    "ahmad@uai.ac.id",
    "siti.aisyah@uai.ac.id",
    "budi@gmail.com",
    "invalid@uai.ac.id.xyz",
]

for email in email_list:
    if re.match(pattern, email):
        print(f"  {email} → VALID")
    else:
        print(f"  {email} → INVALID")
```

### Menggunakan AI untuk Debugging String Operations

Ketika operasi string Anda tidak menghasilkan output yang diharapkan, AI bisa membantu debugging:

> **Contoh prompt:**
> "Kode berikut seharusnya menghapus semua karakter duplikat berturutan dari string, tapi hasilnya tidak sesuai. Bantu saya debug:
> ```python
> def hapus_duplikat(s):
>     hasil = s[0]
>     for i in range(len(s)):
>         if s[i] != s[i-1]:
>             hasil += s[i]
>     return hasil
>
> print(hapus_duplikat("aabbccdd"))
> # Expected: "abcd"
> # Actual: "aabcd"
> ```"

AI akan menjelaskan bahwa bug-nya ada pada range yang dimulai dari 0, bukan 1, sehingga karakter pertama ditambahkan dua kali.

### Validasi Output AI pada Text Processing

**Penting:** Selalu verifikasi output AI sebelum menggunakannya!

Langkah-langkah validasi:

1. **Jalankan kode** di Google Colab dengan berbagai input, termasuk edge cases:
   - String kosong: `""`
   - String satu karakter: `"a"`
   - String dengan spasi: `"   "`
   - String dengan karakter khusus: `"@#$%"`

2. **Periksa edge cases** yang mungkin tidak dipertimbangkan AI:
   - Bagaimana jika input `None`?
   - Bagaimana jika string sangat panjang?
   - Bagaimana jika input mengandung karakter Unicode (emoji, aksara non-Latin)?

3. **Bandingkan dengan implementasi manual** — trace kode langkah demi langkah untuk memastikan logikanya benar.

4. **Cek efisiensi** — apakah kode AI menggunakan pendekatan yang efisien? Concatenation string berulang (`hasil += karakter`) bisa lambat untuk string sangat panjang. Pendekatan list + `join()` lebih efisien.

> **Prinsip Islami dalam penggunaan AI:** Jujurlah tentang penggunaan AI. Memahami kode yang diberikan AI adalah **kewajiban akademik** Anda. Copy-paste tanpa pemahaman adalah bentuk **ketidakjujuran intelektual**. Gunakan AI sebagai *guru* yang membantu Anda belajar, bukan sebagai *pengganti* proses belajar Anda.

---

## Latihan Soal

### Tingkat Dasar

**Soal 1: Hitung Konsonan**

Buatlah fungsi `hitung_konsonan(teks)` yang menghitung jumlah huruf konsonan dalam string. Huruf konsonan adalah huruf yang bukan vokal (a, i, u, e, o).

Contoh:
```
Input : "Informatika"
Output: Jumlah konsonan: 6 (n, f, r, m, t, k)
```

**Soal 2: Inisial Nama**

Buatlah fungsi `buat_inisial(nama_lengkap)` yang menghasilkan inisial dari nama lengkap.

Contoh:
```
Input : "Ahmad Fadillah Nugroho"
Output: "A.F.N."

Input : "siti aisyah"
Output: "S.A."
```

**Soal 3: Censor Kata**

Buatlah fungsi `sensor(teks, kata_sensor)` yang mengganti kata tertentu dengan tanda bintang (`*`) sebanyak panjang kata tersebut.

Contoh:
```
Input : sensor("Saya suka makan nasi goreng", "nasi")
Output: "Saya suka makan **** goreng"
```

**Soal 4: Hitung Kata**

Buatlah fungsi `hitung_kata(kalimat)` yang menghitung jumlah kata dalam kalimat. Kata dipisahkan oleh satu atau lebih spasi.

Contoh:
```
Input : "  Ini   adalah   teks   dengan  spasi   berlebih  "
Output: 6 kata
```

**Soal 5: String Zigzag**

Buatlah fungsi `zigzag(teks)` yang mengubah string menjadi pattern zigzag (huruf besar-kecil bergantian).

Contoh:
```
Input : "informatika"
Output: "InFoRmAtIkA"
```

### Tingkat Menengah

**Soal 1: ROT13 Cipher**

Implementasikan ROT13 (Caesar Cipher dengan shift 13). ROT13 bersifat *self-inverse* — mengenkripsi dua kali menghasilkan teks asli.

Contoh:
```
Enkripsi : "Hello World" → "Uryyb Jbeyq"
Dekripsi : "Uryyb Jbeyq" → "Hello World" (ROT13 lagi)
```

**Soal 2: Validasi Password**

Buatlah fungsi `validasi_password(password)` yang memeriksa kekuatan password berdasarkan kriteria:
- Minimal 8 karakter
- Mengandung huruf besar
- Mengandung huruf kecil
- Mengandung angka
- Mengandung karakter khusus (!@#$%^&*)

Tampilkan skor kekuatan: Lemah (1-2 kriteria), Sedang (3 kriteria), Kuat (4 kriteria), Sangat Kuat (5 kriteria).

**Soal 3: Run-Length Encoding**

Implementasikan kompresi Run-Length Encoding (RLE): karakter berturutan yang sama digantikan dengan karakter diikuti jumlahnya.

Contoh:
```
Encode: "AAABBBCCDDDDDD" → "A3B3C2D6"
Decode: "A3B3C2D6" → "AAABBBCCDDDDDD"
```

**Soal 4: Pig Latin**

Implementasikan konversi teks ke Pig Latin (versi sederhana):
- Jika kata dimulai dengan vokal: tambahkan "yay" di akhir
- Jika kata dimulai dengan konsonan: pindahkan konsonan awal ke akhir, tambahkan "ay"

Contoh:
```
"hello" → "ellohay"
"apple" → "appleyay"
"python is fun" → "ythonpay isyay unfay"
```

**Soal 5: Detektor Anagram**

Buatlah fungsi `is_anagram(kata1, kata2)` yang memeriksa apakah dua kata adalah anagram (tersusun dari huruf yang sama).

Contoh:
```
"listen" dan "silent" → Anagram
"hello" dan "world" → Bukan anagram
"dormitory" dan "dirty room" → Anagram (abaikan spasi)
```

### Tingkat Mahir

**Soal 1: Markdown ke Plain Text**

Buatlah fungsi yang mengkonversi teks Markdown sederhana ke plain text:
- Hapus header (`#`, `##`, `###`)
- Hapus bold (`**teks**` → `teks`)
- Hapus italic (`*teks*` → `teks`)
- Hapus inline code (`` `kode` `` → `kode`)
- Ubah link `[teks](url)` → `teks (url)`

Contoh:
```
Input : "# Judul\n**Bold** dan *italic*\nKunjungi [UAI](https://uai.ac.id)"
Output: "Judul\nBold dan italic\nKunjungi UAI (https://uai.ac.id)"
```

**Soal 2: Spell Checker Sederhana**

Buatlah spell checker sederhana untuk bahasa Indonesia yang:
- Memiliki kamus kecil (50-100 kata umum bahasa Indonesia)
- Mendeteksi kata yang tidak ada dalam kamus
- Memberikan saran koreksi berdasarkan kemiripan (misalnya, beda 1 huruf)
- Tampilkan kata yang salah dan sarannya

**Soal 3: Parser Format Sederhana**

Buatlah mini template engine yang bisa menggantikan placeholder `{{nama_variabel}}` dengan nilai dari dictionary.

Contoh:
```python
template = "Halo {{nama}}, selamat datang di {{universitas}}! NIM Anda: {{nim}}."
data = {"nama": "Ahmad", "universitas": "UAI", "nim": "2024001001"}

# Output: "Halo Ahmad, selamat datang di UAI! NIM Anda: 2024001001."
```

Tangani juga kasus:
- Placeholder yang tidak ada di dictionary → biarkan apa adanya
- Dictionary yang memiliki key yang tidak dipakai → abaikan
- Nested braces → tangani dengan baik

---

## Rangkuman

Berikut ringkasan materi yang telah dipelajari dalam bab ini:

1. **String** adalah tipe data sequence yang merepresentasikan urutan karakter. String bersifat **immutable** — tidak bisa diubah setelah dibuat. Setiap operasi yang "mengubah" string sebenarnya membuat string baru.

2. **Pembuatan string** bisa menggunakan single quote (`'...'`), double quote (`"..."`), atau triple quote (`'''...'''` / `"""..."""`). Triple quote memungkinkan string multi-baris dan sering digunakan untuk docstring.

3. **Escape characters** (`\n`, `\t`, `\\`, `\'`, `\"`) digunakan untuk merepresentasikan karakter khusus. Raw string (awalan `r`) menonaktifkan escape.

4. **Indexing** mengakses karakter individual: positif dari kiri (`[0]`), negatif dari kanan (`[-1]`). **Slicing** (`[start:stop:step]`) mengambil bagian string — ingat bahwa `stop` bersifat eksklusif.

5. **Operasi dasar**: concatenation (`+`), repetition (`*`), membership (`in`/`not in`), dan `len()` untuk panjang string.

6. **String methods** mengembalikan string baru (bukan mengubah aslinya):
   - **Case**: `upper()`, `lower()`, `title()`, `capitalize()`, `swapcase()`
   - **Search**: `find()`, `index()`, `count()`, `startswith()`, `endswith()`
   - **Modification**: `replace()`, `strip()`, `split()`, `join()`
   - **Validation**: `isalpha()`, `isdigit()`, `isalnum()`, `isspace()`

7. **String formatting** memiliki tiga cara: **f-string** (direkomendasikan), `.format()`, dan `%`-formatting (lama). f-string mendukung ekspresi Python langsung di dalam `{}`.

8. **Format specifiers** mengontrol tampilan: alignment (`<`, `>`, `^`), padding, presisi desimal (`.2f`), pemisah ribuan (`,`), dan persentase (`%`).

9. **Iterasi string** menggunakan `for` loop dan `enumerate()`. Pola umum meliputi: penghitungan karakter, pembangunan string baru, pembalikan string, dan pengecekan palindrome.

10. **Studi kasus** pengolahan teks menunjukkan aplikasi nyata: Word Counter untuk analisis teks, Caesar Cipher untuk enkripsi dasar, Validator NIK untuk validasi format data Indonesia, dan Text Formatter untuk pembersihan teks.

11. **AI sebagai alat bantu** pengolahan teks: berguna untuk memahami regex, debugging string operations, dan eksplorasi. Namun, selalu **verifikasi** output AI secara mandiri dan **pahami** kode yang diberikan.

---

## Referensi

1. Downey, A. B. (2015). *Think Python: How to Think Like a Computer Scientist* (2nd ed.). O'Reilly Media. Tersedia gratis di [https://greenteapress.com/wp/think-python-2e/](https://greenteapress.com/wp/think-python-2e/)

2. Lutz, M. (2013). *Learning Python* (5th ed.). O'Reilly Media.

3. Matthes, E. (2019). *Python Crash Course: A Hands-On, Project-Based Introduction to Programming* (2nd ed.). No Starch Press.

4. Severance, C. R. (2016). *Python for Everybody: Exploring Data in Python 3*. Tersedia gratis di [https://www.py4e.com/book](https://www.py4e.com/book)

5. Sweigart, A. (2019). *Automate the Boring Stuff with Python* (2nd ed.). No Starch Press. Tersedia gratis di [https://automatetheboringstuff.com/](https://automatetheboringstuff.com/)

6. Python Software Foundation. (2024). *The Python Tutorial — Text Sequence Type (str)*. [https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

7. Python Software Foundation. (2024). *String Methods*. [https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

8. Python Software Foundation. (2024). *Format String Syntax*. [https://docs.python.org/3/library/string.html#formatstrings](https://docs.python.org/3/library/string.html#formatstrings)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
