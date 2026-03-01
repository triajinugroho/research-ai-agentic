# BAB 2: VARIABEL, TIPE DATA, DAN OPERATOR

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| CPMK-2.1 | Menjelaskan konsep variabel dan cara penamaan yang baik | C2 (Memahami) |
| CPMK-2.2 | Mengidentifikasi dan menggunakan tipe data dasar Python | C3 (Menerapkan) |
| CPMK-2.3 | Menerapkan operator aritmatika, perbandingan, dan logika | C3 (Menerapkan) |
| CPMK-2.4 | Membuat program sederhana dengan input/output | C3 (Menerapkan) |

**Estimasi Waktu:** 3 x 50 menit (3 SKS)

**Prasyarat:** Mahasiswa telah memahami materi Bab 1 (Pengantar Algoritma dan Pemrograman) dan telah berhasil menginstal Python serta IDE/text editor.

---

## 2.1 Variabel

### 2.1.1 Apa Itu Variabel?

Dalam pemrograman, **variabel** adalah tempat penyimpanan data di dalam memori komputer yang diberi nama (label) agar dapat diakses dan dimanipulasi oleh program. Bayangkan variabel seperti **kotak penyimpanan berlabel** di sebuah gudang:

- Setiap kotak memiliki **label** (nama variabel) yang menjelaskan isinya.
- Setiap kotak dapat **menyimpan satu barang** (nilai/data) pada satu waktu.
- Anda dapat **mengganti isi kotak** kapan saja (menimpa nilai variabel).
- Anda menggunakan **label** untuk menemukan kotak tersebut (mengakses variabel).

**Visualisasi Memori (Sederhana):**

```
Memori Komputer
┌──────────────────────────────────────────────────┐
│                                                  │
│   nama ──────► [ "Ahmad" ]    (alamat: 0x001)    │
│                                                  │
│   umur ──────► [ 19 ]         (alamat: 0x002)    │
│                                                  │
│   ipk  ──────► [ 3.75 ]      (alamat: 0x003)    │
│                                                  │
│   aktif ─────► [ True ]      (alamat: 0x004)    │
│                                                  │
└──────────────────────────────────────────────────┘
```

Dalam ilustrasi di atas, `nama`, `umur`, `ipk`, dan `aktif` adalah label (nama variabel) yang merujuk ke lokasi memori tertentu yang menyimpan nilai masing-masing.

**Python dan Dynamic Typing:**

Salah satu keunggulan Python dibandingkan bahasa seperti C atau Java adalah Python menggunakan **dynamic typing**. Artinya:

1. Anda **tidak perlu mendeklarasikan tipe data** variabel sebelum menggunakannya.
2. Python secara otomatis **mendeteksi tipe data** berdasarkan nilai yang diberikan.
3. Sebuah variabel dapat **berubah tipe datanya** selama program berjalan (meskipun tidak disarankan).

```python
# Di Python, cukup langsung assign nilai:
nama = "Ahmad"       # Python tahu ini string
umur = 19            # Python tahu ini integer
ipk = 3.75           # Python tahu ini float
is_aktif = True      # Python tahu ini boolean

# Bandingkan dengan Java (sebagai perbandingan):
# String nama = "Ahmad";
# int umur = 19;
# double ipk = 3.75;
# boolean isAktif = true;
```

> **Catatan Penting:** Meskipun Python memungkinkan variabel berubah tipe data, **praktik terbaik** adalah menjaga konsistensi tipe data sebuah variabel sepanjang program. Mengubah tipe data variabel secara tiba-tiba (misalnya, dari integer ke string) dapat membuat kode sulit dibaca dan rawan bug.

---

### 2.1.2 Aturan Penamaan Variabel

Python memiliki aturan ketat untuk penamaan variabel. Jika aturan ini dilanggar, program akan menghasilkan **SyntaxError**.

**Aturan Wajib (Mandatory Rules):**

1. **Harus diawali** dengan huruf (a-z, A-Z) atau underscore (`_`).
2. **Tidak boleh diawali** dengan angka.
3. **Hanya boleh mengandung** huruf, angka, dan underscore (alfanumerik + `_`).
4. **Tidak boleh mengandung spasi** atau karakter khusus (-, !, @, #, $, dll.).
5. **Tidak boleh menggunakan kata kunci** (reserved words) Python.
6. **Case-sensitive:** `nama`, `Nama`, dan `NAMA` adalah tiga variabel yang berbeda.

**Contoh Nama Variabel yang Valid dan Tidak Valid:**

```python
# VALID
nama = "Ahmad"
_nama = "Budi"
nama2 = "Citra"
nama_mahasiswa = "Dina"
totalHarga = 50000      # camelCase (valid tapi bukan standar Python)
MAKS_NILAI = 100        # konstanta (konvensi: huruf besar semua)

# TIDAK VALID — akan menghasilkan SyntaxError
# 2nama = "Error"        # Diawali angka
# nama mahasiswa = "Err" # Mengandung spasi
# nama-mahasiswa = "Err" # Mengandung tanda hubung
# class = "Informatika"  # Menggunakan kata kunci Python
# harga$ = 1000          # Mengandung karakter khusus
```

**Daftar Kata Kunci (Reserved Words) Python 3:**

```
False    await    else      import    pass
None     break    except    in        raise
True     class    finally   is        return
and      continue for       lambda    try
as       def      from      nonlocal  while
assert   del      global    not       with
async    elif     if        or        yield
```

> **Tip:** Untuk melihat daftar kata kunci Python di interpreter, jalankan:
> ```python
> import keyword
> print(keyword.kwlist)
> ```

**Konvensi Penamaan Python (PEP 8):**

PEP 8 adalah panduan gaya penulisan kode Python yang diterima secara luas oleh komunitas Python. Untuk variabel, PEP 8 merekomendasikan **snake_case**:

- Semua huruf kecil.
- Kata-kata dipisahkan dengan underscore (`_`).

```python
# snake_case (DIREKOMENDASIKAN di Python)
nama_mahasiswa = "Ahmad"
total_harga = 150000
jumlah_item = 5
is_lulus = True

# camelCase (umum di Java/JavaScript, TIDAK direkomendasikan di Python)
namaMahasiswa = "Ahmad"
totalHarga = 150000

# UPPER_SNAKE_CASE (untuk konstanta)
MAKS_MAHASISWA = 40
PI = 3.14159
TARIF_PAJAK = 0.11
```

**Tabel Perbandingan Nama Variabel Baik vs Buruk:**

| Baik | Buruk | Alasan |
|------|-------|--------|
| `nama_mahasiswa` | `nm` | Deskriptif, mudah dipahami |
| `total_harga` | `x` | Bermakna, menjelaskan isi data |
| `jumlah_item` | `j` | Jelas, tidak ambigu |
| `is_lulus` | `flag1` | Menunjukkan bahwa ini adalah boolean |
| `suhu_celsius` | `s` | Menjelaskan satuan dan konteks |
| `indeks_baris` | `i2` | Lebih deskriptif daripada singkatan |
| `nomor_telepon` | `ntelp` | Lebih mudah dibaca |
| `tanggal_lahir` | `tgl` | Tidak membingungkan pembaca kode |

> **Prinsip Utama:** Kode lebih sering **dibaca** daripada **ditulis**. Nama variabel yang deskriptif membuat kode Anda lebih mudah dipahami oleh orang lain (dan oleh diri Anda sendiri di masa depan).

---

### 2.1.3 Assignment (Penugasan)

**Assignment** adalah proses memberikan nilai kepada variabel menggunakan operator `=` (tanda sama dengan). Dalam Python, operator `=` berarti "berikan nilai di sebelah kanan ke variabel di sebelah kiri."

> **Perhatian:** Operator `=` dalam pemrograman **bukan** berarti "sama dengan" secara matematis. Untuk perbandingan kesamaan, Python menggunakan `==`.

**Assignment Dasar:**

```python
# Assignment dasar — nilai di kanan disimpan ke variabel di kiri
nama = "Ahmad"          # String
umur = 19               # Integer
ipk = 3.75              # Float
is_aktif = True         # Boolean
alamat = None           # NoneType (belum memiliki nilai)
```

**Multiple Assignment (Penugasan Ganda):**

Python memungkinkan Anda memberikan nilai ke beberapa variabel sekaligus dalam satu baris:

```python
# Multiple assignment — satu baris, beberapa variabel
x, y, z = 1, 2, 3
print(x)  # Output: 1
print(y)  # Output: 2
print(z)  # Output: 3

# Berguna untuk data yang saling terkait
nama, nim, angkatan = "Ahmad", "2024001", 2024
print(f"Mahasiswa: {nama}, NIM: {nim}, Angkatan: {angkatan}")

# Memberikan nilai yang sama ke beberapa variabel
a = b = c = 0
print(a, b, c)  # Output: 0 0 0
```

**Swap Values (Menukar Nilai):**

Dalam banyak bahasa pemrograman, menukar nilai dua variabel memerlukan variabel sementara (temporary variable). Python memiliki cara yang lebih **elegan**:

```python
# Cara klasik (menggunakan variabel sementara)
x = 10
y = 20
temp = x
x = y
y = temp
print(x, y)  # Output: 20 10

# Cara Python (elegan dan singkat!)
x = 10
y = 20
x, y = y, x
print(x, y)  # Output: 20 10
```

> **Mengapa ini bekerja?** Python mengevaluasi **semua ekspresi di sisi kanan** terlebih dahulu sebelum melakukan assignment ke sisi kiri. Jadi `y, x` dievaluasi menjadi `(20, 10)` terlebih dahulu, kemudian di-assign ke `x, y`.

**Augmented Assignment (Assignment Gabungan):**

```python
# Augmented assignment — operasi + assignment dalam satu langkah
saldo = 1000000

saldo += 500000     # sama dengan: saldo = saldo + 500000
print(saldo)        # Output: 1500000

saldo -= 200000     # sama dengan: saldo = saldo - 200000
print(saldo)        # Output: 1300000

# Lebih banyak contoh akan dibahas di Subbab 2.3.4
```

---

## 2.2 Tipe Data Dasar

Tipe data menentukan **jenis nilai** yang dapat disimpan dalam variabel dan **operasi apa** yang dapat dilakukan terhadap nilai tersebut. Python memiliki beberapa tipe data bawaan (*built-in types*) yang paling sering digunakan:

```
Tipe Data Dasar Python
├── Numerik
│   ├── int    (bilangan bulat)
│   └── float  (bilangan desimal)
├── Teks
│   └── str    (string / teks)
├── Boolean
│   └── bool   (True / False)
└── Null
    └── NoneType (None)
```

---

### 2.2.1 Integer (int)

**Integer** adalah tipe data untuk menyimpan **bilangan bulat**, baik positif, negatif, maupun nol.

```python
# Contoh integer
jumlah_mahasiswa = 150
suhu_minus = -5
nol = 0
tahun_masuk = 2024
harga_barang = 25000
nomor_lantai = -2       # basement lantai 2
```

**Keunggulan Python:** Tidak seperti bahasa C/Java yang membatasi ukuran integer (misalnya, `int` di Java maksimal ~2.1 miliar), Python **tidak memiliki batasan ukuran** integer. Python dapat menangani bilangan bulat sebesar apa pun selama memori komputer mencukupi.

```python
# Python dapat menangani bilangan yang sangat besar
bilangan_besar = 99999999999999999999999999999999999999
print(bilangan_besar)
print(type(bilangan_besar))  # <class 'int'>

# Perhitungan dengan bilangan besar juga valid
faktorial_30 = 265252859812191058636308480000000
print(faktorial_30)
```

**Operasi pada Integer:**

```python
# Operasi dasar
a = 17
b = 5

print(a + b)     # 22 (penjumlahan)
print(a - b)     # 12 (pengurangan)
print(a * b)     # 85 (perkalian)
print(a / b)     # 3.4 (pembagian — hasilnya SELALU float!)
print(a // b)    # 3 (pembagian bulat)
print(a % b)     # 2 (sisa bagi / modulo)
print(a ** b)    # 1419857 (pangkat: 17^5)
```

**Representasi Integer dalam Berbagai Basis:**

```python
# Desimal (basis 10) — default
angka = 255

# Biner (basis 2) — awalan 0b
biner = 0b11111111      # 255 dalam biner
print(biner)            # Output: 255

# Oktal (basis 8) — awalan 0o
oktal = 0o377           # 255 dalam oktal
print(oktal)            # Output: 255

# Heksadesimal (basis 16) — awalan 0x
heksa = 0xFF            # 255 dalam heksadesimal
print(heksa)            # Output: 255

# Konversi ke representasi string berbagai basis
print(bin(255))         # '0b11111111'
print(oct(255))         # '0o377'
print(hex(255))         # '0xff'
```

**Contoh dengan Konteks Indonesia:**

```python
# Jumlah penduduk Indonesia (estimasi)
populasi_indonesia = 275000000

# Harga barang dalam Rupiah
harga_laptop = 12500000
harga_buku = 85000

# Nomor induk (perhatikan: ini sebaiknya string jika diawali 0)
# nim = 2024001  # OK sebagai integer jika tidak diawali 0
```

> **Peringatan:** Untuk data seperti nomor telepon, NIK, atau NIM yang mungkin diawali angka 0, gunakan **string**, bukan integer. Integer akan menghilangkan angka 0 di depan.

---

### 2.2.2 Float (Floating-Point)

**Float** adalah tipe data untuk menyimpan **bilangan desimal** (bilangan berkoma). Nama "floating-point" merujuk pada cara bilangan ini disimpan di memori komputer menggunakan standar **IEEE 754**.

```python
# Contoh float
ipk = 3.75
suhu = 36.5
pi = 3.14159265358979
harga_dollar = 15750.50
koordinat_lat = -6.2088      # Latitude Jakarta
koordinat_lon = 106.8456     # Longitude Jakarta
```

**Notasi Ilmiah (Scientific Notation):**

```python
# Notasi ilmiah untuk bilangan yang sangat besar atau sangat kecil
jarak_matahari = 1.496e8     # 1.496 x 10^8 km = 149,600,000 km
massa_elektron = 9.109e-31   # 9.109 x 10^-31 kg

print(jarak_matahari)        # 149600000.0
print(massa_elektron)        # 9.109e-31
```

**Masalah Presisi Float (Floating-Point Precision):**

Ini adalah salah satu hal yang paling penting untuk dipahami tentang float. Karena cara bilangan desimal disimpan dalam format biner, **beberapa bilangan desimal tidak dapat direpresentasikan secara tepat**:

```python
# Masalah presisi yang terkenal
print(0.1 + 0.2)            # 0.30000000000000004 (BUKAN 0.3!)
print(0.1 + 0.2 == 0.3)     # False!

# Mengapa ini terjadi?
# 0.1 dalam biner = 0.0001100110011... (berulang tak hingga)
# Komputer menyimpan pendekatan (approximation), bukan nilai tepat.

# Solusi 1: Pembulatan
print(round(0.1 + 0.2, 1))          # 0.3
print(round(0.1 + 0.2, 1) == 0.3)   # True

# Solusi 2: Modul decimal (untuk aplikasi keuangan)
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # 0.3 (tepat!)
```

> **Aturan Praktis:** Untuk **aplikasi keuangan** (perhitungan uang, pajak, bunga), gunakan modul `Decimal` daripada float biasa. Untuk keperluan umum (fisika, grafik, statistik), float biasa cukup memadai.

**Konversi Integer ke Float dan Sebaliknya:**

```python
# Integer ke float
x = 10
y = float(x)
print(y)           # 10.0
print(type(y))     # <class 'float'>

# Float ke integer (MEMBUANG desimal, bukan membulatkan!)
a = 3.7
b = int(a)
print(b)           # 3 (bukan 4!)

a = -3.7
b = int(a)
print(b)           # -3 (bukan -4!)

# Untuk membulatkan, gunakan round()
print(round(3.7))  # 4
print(round(3.2))  # 3
print(round(3.5))  # 4 (banker's rounding untuk .5)
```

**Contoh dengan Konteks Indonesia:**

```python
# IPK mahasiswa
ipk_semester = 3.67

# Suhu rata-rata Jakarta
suhu_rata_rata = 27.5  # derajat Celsius

# Kurs dollar
kurs_usd = 15750.00

# Tinggi badan dalam meter
tinggi_badan = 1.72
```

---

### 2.2.3 String (str)

**String** adalah tipe data untuk menyimpan **teks** — urutan karakter yang bisa berupa huruf, angka, simbol, spasi, dan karakter khusus lainnya. String di Python diapit oleh tanda kutip tunggal (`'...'`), ganda (`"..."`), atau tiga tanda kutip (`'''...'''` atau `"""..."""`).

```python
# Kutip tunggal
nama = 'Ahmad'

# Kutip ganda
nim = "2024001"

# Kutip tiga (untuk string multi-baris)
alamat = """Jl. Sisingamangaraja
Kebayoran Baru
Jakarta Selatan 12110"""

# String kosong
kosong = ""
juga_kosong = ''
```

**Kapan Menggunakan Kutip Tunggal vs Ganda?**

```python
# Gunakan kutip ganda jika string mengandung kutip tunggal
pesan = "It's a beautiful day"

# Gunakan kutip tunggal jika string mengandung kutip ganda
html = '<a href="https://uai.ac.id">UAI</a>'

# Atau gunakan escape character
pesan2 = 'It\'s a beautiful day'
html2 = "<a href=\"https://uai.ac.id\">UAI</a>"
```

**Escape Characters (Karakter Escape):**

Escape character digunakan untuk menyisipkan karakter khusus ke dalam string:

| Escape | Fungsi | Contoh |
|--------|--------|--------|
| `\n` | Baris baru (newline) | `"Baris 1\nBaris 2"` |
| `\t` | Tab | `"Nama\t: Ahmad"` |
| `\\` | Backslash literal | `"C:\\Users\\Ahmad"` |
| `\'` | Kutip tunggal | `'It\'s OK'` |
| `\"` | Kutip ganda | `"Dia berkata \"Halo\""` |

```python
# Contoh penggunaan escape character
print("Nama\t: Ahmad")
print("NIM\t: 2024001")
print("Prodi\t: Informatika")
# Output:
# Nama    : Ahmad
# NIM     : 2024001
# Prodi   : Informatika

print("Baris pertama\nBaris kedua\nBaris ketiga")
# Output:
# Baris pertama
# Baris kedua
# Baris ketiga

# Raw string (mengabaikan escape character)
path = r"C:\Users\Ahmad\Documents"
print(path)  # C:\Users\Ahmad\Documents
```

**F-String (Formatted String Literal) — Python 3.6+:**

F-string adalah cara **paling modern dan direkomendasikan** untuk memformat string di Python:

```python
# F-string dasar
nama = "Ahmad"
umur = 19
print(f"Halo, nama saya {nama} dan umur saya {umur} tahun.")
# Output: Halo, nama saya Ahmad dan umur saya 19 tahun.

# F-string dengan ekspresi
panjang = 5
lebar = 3
print(f"Luas persegi panjang: {panjang * lebar}")
# Output: Luas persegi panjang: 15

# F-string dengan format angka
ipk = 3.6789
print(f"IPK Anda: {ipk:.2f}")    # 2 digit desimal
# Output: IPK Anda: 3.68

harga = 15500000
print(f"Harga: Rp{harga:,}")     # Pemisah ribuan
# Output: Harga: Rp15,500,000

print(f"Harga: Rp{harga:,.0f}")  # Pemisah ribuan tanpa desimal
# Output: Harga: Rp15,500,000
```

**String Indexing (Pengindeksan String) — Preview:**

Setiap karakter dalam string memiliki indeks (posisi). Indeks dimulai dari 0:

```python
teks = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5    (indeks positif)
#      -6 -5 -4 -3 -2 -1   (indeks negatif)

print(teks[0])     # 'P'
print(teks[1])     # 'y'
print(teks[-1])    # 'n' (karakter terakhir)
print(teks[-2])    # 'o' (karakter kedua dari belakang)
```

> **Catatan:** Topik string akan dibahas lebih mendalam di bab tersendiri (manipulasi string, slicing, method string, dll.).

**Contoh dengan Konteks Indonesia:**

```python
# Data mahasiswa
nama_lengkap = "Ahmad Fauzi"
nim = "20240010015"     # NIM sebagai string (bisa diawali 0)
program_studi = "Informatika"
universitas = "Universitas Al Azhar Indonesia"

# Alamat
alamat = "Jl. Sisingamangaraja No. 2, Kebayoran Baru, Jakarta Selatan"

# Pesan terformat
print(f"Mahasiswa: {nama_lengkap}")
print(f"NIM: {nim}")
print(f"Prodi: {program_studi}, {universitas}")
```

---

### 2.2.4 Boolean (bool)

**Boolean** adalah tipe data yang hanya memiliki dua nilai: **`True`** (benar) dan **`False`** (salah). Boolean sangat penting dalam logika pemrograman, terutama untuk pengambilan keputusan (yang akan dibahas lebih dalam di Bab 3).

```python
# Nilai boolean langsung
is_lulus = True
has_paid = False
is_student = True
sudah_makan = False

# Boolean dari hasil perbandingan
umur = 19
print(umur >= 17)      # True
print(umur == 20)      # False
print(umur != 19)      # False

# Boolean dari operator logika
nilai = 85
kehadiran = 80
lulus = nilai >= 60 and kehadiran >= 75
print(lulus)            # True
```

**Truthy dan Falsy Values:**

Di Python, setiap nilai memiliki "kebenaran" bawaan. Beberapa nilai dianggap **falsy** (dievaluasi sebagai `False`), dan sisanya dianggap **truthy** (dievaluasi sebagai `True`):

| Falsy (Dianggap False) | Truthy (Dianggap True) |
|------------------------|----------------------|
| `False` | `True` |
| `0` (integer nol) | Angka selain 0 (`1`, `-5`, `3.14`) |
| `0.0` (float nol) | Angka selain 0.0 |
| `""` (string kosong) | String tidak kosong (`"Hello"`, `" "`) |
| `None` | Objek apa pun yang bukan None |
| `[]` (list kosong) | List tidak kosong (`[1, 2, 3]`) |
| `{}` (dictionary kosong) | Dictionary tidak kosong |

```python
# Demonstrasi truthy/falsy
print(bool(1))        # True
print(bool(0))        # False
print(bool("Hello"))  # True
print(bool(""))       # False
print(bool(None))     # False
print(bool(42))       # True
print(bool(-1))       # True (semua angka selain 0 adalah truthy)
```

**Contoh dengan Konteks Indonesia:**

```python
# Status akademik
is_lulus = True
is_cuti = False
has_bayar_ukt = True
sudah_ta = False

# Evaluasi kelulusan
nilai_akhir = 72
kehadiran_persen = 82
is_lulus_mk = nilai_akhir >= 55 and kehadiran_persen >= 75
print(f"Lulus mata kuliah: {is_lulus_mk}")  # Lulus mata kuliah: True
```

---

### 2.2.5 NoneType

**`None`** adalah nilai khusus di Python yang merepresentasikan **ketiadaan nilai** atau **"tidak ada data"**. `None` memiliki tipe data `NoneType` dan merupakan satu-satunya nilai dari tipe ini.

```python
# Deklarasi variabel tanpa nilai awal
hasil_pencarian = None
data_mahasiswa = None

# Cek apakah variabel bernilai None
if hasil_pencarian is None:
    print("Belum ada hasil pencarian.")

# None sering digunakan sebagai nilai default
def cari_mahasiswa(nim):
    # Jika tidak ditemukan, return None
    return None

# None berbeda dengan string kosong, nol, atau False
print(None == 0)       # False
print(None == "")      # False
print(None == False)   # False
print(None is None)    # True
```

> **Kapan Menggunakan None?**
> - Saat sebuah variabel belum memiliki nilai yang ditentukan.
> - Sebagai nilai kembalian (*return value*) fungsi yang tidak menemukan hasil.
> - Sebagai nilai default parameter fungsi.

---

### 2.2.6 Type Checking dan Type Conversion

**Type Checking (Pengecekan Tipe):**

Fungsi `type()` digunakan untuk mengetahui tipe data sebuah variabel atau nilai:

```python
# Type checking menggunakan type()
x = 42
print(type(x))           # <class 'int'>

y = 3.14
print(type(y))           # <class 'float'>

nama = "Ahmad"
print(type(nama))        # <class 'str'>

aktif = True
print(type(aktif))       # <class 'bool'>

kosong = None
print(type(kosong))      # <class 'NoneType'>
```

Fungsi `isinstance()` digunakan untuk mengecek apakah sebuah variabel memiliki tipe data tertentu:

```python
# isinstance() — lebih fleksibel dari type()
x = 42
print(isinstance(x, int))      # True
print(isinstance(x, float))    # False
print(isinstance(x, (int, float)))  # True (cek beberapa tipe sekaligus)
```

**Type Conversion (Konversi Tipe Data / Casting):**

Python menyediakan fungsi bawaan untuk mengonversi antar tipe data:

```python
# String ke Integer
angka_str = "100"
angka_int = int(angka_str)
print(angka_int)          # 100
print(type(angka_int))    # <class 'int'>

# String ke Float
ipk_str = "3.75"
ipk_float = float(ipk_str)
print(ipk_float)          # 3.75
print(type(ipk_float))    # <class 'float'>

# Integer ke Float
bilangan = 10
desimal = float(bilangan)
print(desimal)            # 10.0

# Float ke Integer (membuang desimal, BUKAN membulatkan)
suhu = 36.8
suhu_bulat = int(suhu)
print(suhu_bulat)         # 36 (bukan 37!)

# Integer/Float ke String
umur = 19
umur_str = str(umur)
print(umur_str)           # "19"
print(type(umur_str))     # <class 'str'>

harga = 15000.50
harga_str = str(harga)
print(harga_str)          # "15000.5"

# Integer ke Boolean
print(bool(0))            # False
print(bool(1))            # True
print(bool(-5))           # True

# Boolean ke Integer
print(int(True))          # 1
print(int(False))         # 0
```

**Error pada Konversi yang Tidak Valid:**

```python
# Konversi yang akan GAGAL (menghasilkan error)

# String non-numerik ke integer
# int("hello")       # ValueError: invalid literal for int()

# String non-numerik ke float
# float("abc")       # ValueError: could not convert string to float

# String float ke integer (harus dua tahap)
# int("3.14")        # ValueError!
# Solusi: int(float("3.14"))  → 3

# Cara aman: menggunakan try-except (akan dipelajari nanti)
teks = "bukan_angka"
try:
    angka = int(teks)
except ValueError:
    print(f"'{teks}' tidak bisa dikonversi ke integer!")
# Output: 'bukan_angka' tidak bisa dikonversi ke integer!
```

---

## 2.3 Operator

**Operator** adalah simbol khusus yang digunakan untuk melakukan operasi terhadap satu atau lebih nilai (operan). Python mendukung berbagai jenis operator.

---

### 2.3.1 Operator Aritmatika

Operator aritmatika digunakan untuk melakukan operasi matematika:

| Operator | Nama | Contoh | Hasil | Keterangan |
|----------|------|--------|-------|------------|
| `+` | Penjumlahan | `7 + 3` | `10` | Menjumlahkan dua nilai |
| `-` | Pengurangan | `7 - 3` | `4` | Mengurangi nilai |
| `*` | Perkalian | `7 * 3` | `21` | Mengalikan dua nilai |
| `/` | Pembagian | `7 / 3` | `2.333...` | Hasil **selalu float** |
| `//` | Pembagian Bulat | `7 // 3` | `2` | Membuang sisa desimal |
| `%` | Modulo | `7 % 3` | `1` | Sisa hasil bagi |
| `**` | Pangkat | `7 ** 3` | `343` | 7 pangkat 3 |

```python
# Demonstrasi lengkap operator aritmatika
a = 17
b = 5

print(f"{a} + {b} = {a + b}")    # 17 + 5 = 22
print(f"{a} - {b} = {a - b}")    # 17 - 5 = 12
print(f"{a} * {b} = {a * b}")    # 17 * 5 = 85
print(f"{a} / {b} = {a / b}")    # 17 / 5 = 3.4
print(f"{a} // {b} = {a // b}")  # 17 // 5 = 3
print(f"{a} % {b} = {a % b}")    # 17 % 5 = 2
print(f"{a} ** {b} = {a ** b}")  # 17 ** 5 = 1419857
```

**Perbedaan `/` dan `//`:**

```python
# Pembagian biasa (/) selalu menghasilkan float
print(10 / 3)      # 3.3333333333333335
print(10 / 2)      # 5.0 (tetap float meskipun habis dibagi!)

# Pembagian bulat (//) membuang desimal (floor division)
print(10 // 3)     # 3
print(10 // 2)     # 5 (integer)
print(-10 // 3)    # -4 (BUKAN -3! Floor = pembulatan ke bawah)
```

**Operator Modulo (%) — Sangat Berguna!:**

```python
# Cek bilangan genap atau ganjil
angka = 7
if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap")
else:
    print(f"{angka} adalah bilangan ganjil")
# Output: 7 adalah bilangan ganjil

# Konversi detik ke menit:detik
total_detik = 185
menit = total_detik // 60    # 3 menit
detik = total_detik % 60     # 5 detik
print(f"{total_detik} detik = {menit} menit {detik} detik")
# Output: 185 detik = 3 menit 5 detik
```

**Prioritas Operator (Precedence) — PEMDAS:**

Seperti dalam matematika, Python memiliki aturan prioritas operasi. Urutan dari prioritas **tertinggi ke terendah**:

| Prioritas | Operator | Keterangan |
|-----------|----------|------------|
| 1 (Tertinggi) | `()` | Tanda kurung |
| 2 | `**` | Pangkat |
| 3 | `+x`, `-x` | Positif/negatif unary |
| 4 | `*`, `/`, `//`, `%` | Perkalian, pembagian, modulo |
| 5 (Terendah) | `+`, `-` | Penjumlahan, pengurangan |

```python
# Tanpa tanda kurung — mengikuti prioritas
hasil = 2 + 3 * 4        # 2 + 12 = 14 (bukan 20!)
print(hasil)              # 14

# Dengan tanda kurung — mengubah urutan
hasil = (2 + 3) * 4      # 5 * 4 = 20
print(hasil)              # 20

# Contoh lebih kompleks
hasil = 2 ** 3 + 4 * 2 - 1
# Langkah: 8 + 8 - 1 = 15
print(hasil)              # 15

# Selalu gunakan tanda kurung jika ragu!
hasil = (2 ** 3) + (4 * 2) - 1
print(hasil)              # 15 (lebih jelas)
```

**Contoh Studi Kasus: Hitung Total Belanja**

```python
# Menghitung total belanja dengan diskon dan pajak
harga_satuan = 25000
jumlah = 3
diskon_persen = 10
pajak_persen = 11   # PPN 11%

subtotal = harga_satuan * jumlah
diskon = subtotal * diskon_persen / 100
setelah_diskon = subtotal - diskon
pajak = setelah_diskon * pajak_persen / 100
total = setelah_diskon + pajak

print(f"Subtotal     : Rp{subtotal:,.0f}")
print(f"Diskon ({diskon_persen}%) : Rp{diskon:,.0f}")
print(f"Setelah Diskon: Rp{setelah_diskon:,.0f}")
print(f"PPN ({pajak_persen}%)    : Rp{pajak:,.0f}")
print(f"Total Bayar  : Rp{total:,.0f}")
```

---

### 2.3.2 Operator Perbandingan

Operator perbandingan digunakan untuk membandingkan dua nilai. Hasilnya selalu **boolean** (`True` atau `False`):

| Operator | Nama | Contoh | Hasil |
|----------|------|--------|-------|
| `==` | Sama dengan | `5 == 5` | `True` |
| `!=` | Tidak sama dengan | `5 != 3` | `True` |
| `>` | Lebih besar | `5 > 3` | `True` |
| `<` | Lebih kecil | `5 < 3` | `False` |
| `>=` | Lebih besar atau sama | `5 >= 5` | `True` |
| `<=` | Lebih kecil atau sama | `5 <= 3` | `False` |

```python
# Contoh operator perbandingan
nilai = 75
print(nilai == 75)     # True
print(nilai != 80)     # True
print(nilai > 60)      # True
print(nilai < 60)      # False
print(nilai >= 75)     # True
print(nilai <= 70)     # False

# Perbandingan string (berdasarkan urutan leksikografis / alfabet)
print("Ahmad" == "Ahmad")    # True
print("Ahmad" == "ahmad")    # False (case-sensitive!)
print("Ahmad" < "Budi")      # True ('A' < 'B' secara ASCII)
print("apel" > "jeruk")      # False ('a' < 'j')

# Chained comparison (perbandingan berantai) — fitur unik Python!
umur = 19
print(17 <= umur <= 25)      # True (apakah umur antara 17 dan 25?)
# Setara dengan: umur >= 17 and umur <= 25

nilai_akhir = 72
print(55 <= nilai_akhir < 70)    # False (apakah nilai antara 55 dan 69?)
```

> **Peringatan Umum:** Jangan bingung antara `=` (assignment) dan `==` (perbandingan). Ini adalah salah satu kesalahan paling sering ditemui oleh pemula!

```python
x = 5      # Assignment: memberikan nilai 5 ke x
x == 5     # Perbandingan: apakah x sama dengan 5? (True)
```

---

### 2.3.3 Operator Logika

Operator logika digunakan untuk menggabungkan beberapa kondisi boolean:

| Operator | Deskripsi | Contoh | Hasil |
|----------|-----------|--------|-------|
| `and` | Benar jika **kedua** operan benar | `True and True` | `True` |
| `or` | Benar jika **salah satu** operan benar | `True or False` | `True` |
| `not` | Membalikkan nilai boolean | `not True` | `False` |

**Tabel Kebenaran (Truth Table) `and`:**

| A | B | A and B |
|---|---|---------|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

**Tabel Kebenaran `or`:**

| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

**Tabel Kebenaran `not`:**

| A | not A |
|---|-------|
| True | False |
| False | True |

```python
# Contoh penggunaan operator logika

# Syarat kelulusan mata kuliah
nilai = 72
kehadiran = 80

lulus = nilai >= 55 and kehadiran >= 75
print(f"Lulus: {lulus}")  # True (kedua syarat terpenuhi)

# Syarat mendapat remedial
is_remedial = nilai < 55 or kehadiran < 75
print(f"Remedial: {is_remedial}")  # False

# Syarat diskualifikasi
is_curang = False
tidak_diskualifikasi = not is_curang
print(f"Tidak diskualifikasi: {tidak_diskualifikasi}")  # True

# Kombinasi kompleks: syarat beasiswa
ipk = 3.5
semester = 3
is_aktif_organisasi = True
penerima_beasiswa = (ipk >= 3.25 and semester >= 2
                     and is_aktif_organisasi
                     and not is_curang)
print(f"Penerima beasiswa: {penerima_beasiswa}")  # True
```

**Short-Circuit Evaluation:**

Python menggunakan evaluasi "pendek" (*short-circuit*) untuk operator `and` dan `or`:

```python
# Dengan 'and': jika operan pertama False, operan kedua TIDAK dievaluasi
# (karena hasilnya pasti False)
x = 0
# x != 0 adalah False, jadi 10/x tidak pernah dihitung (menghindari error!)
hasil = x != 0 and 10 / x > 2
print(hasil)  # False (tidak terjadi ZeroDivisionError)

# Dengan 'or': jika operan pertama True, operan kedua TIDAK dievaluasi
# (karena hasilnya pasti True)
```

---

### 2.3.4 Operator Assignment (Penugasan)

Selain operator `=` dasar, Python menyediakan **augmented assignment operators** yang menggabungkan operasi aritmatika dengan assignment:

| Operator | Contoh | Setara Dengan | Keterangan |
|----------|--------|---------------|------------|
| `=` | `x = 5` | — | Assignment dasar |
| `+=` | `x += 3` | `x = x + 3` | Tambah dan simpan |
| `-=` | `x -= 3` | `x = x - 3` | Kurang dan simpan |
| `*=` | `x *= 3` | `x = x * 3` | Kali dan simpan |
| `/=` | `x /= 3` | `x = x / 3` | Bagi dan simpan |
| `//=` | `x //= 3` | `x = x // 3` | Bagi bulat dan simpan |
| `%=` | `x %= 3` | `x = x % 3` | Modulo dan simpan |
| `**=` | `x **= 3` | `x = x ** 3` | Pangkat dan simpan |

```python
# Demonstrasi augmented assignment
saldo = 1000000
print(f"Saldo awal: Rp{saldo:,}")

saldo += 500000    # Menerima transfer
print(f"Setelah terima transfer: Rp{saldo:,}")

saldo -= 200000    # Membayar tagihan
print(f"Setelah bayar tagihan: Rp{saldo:,}")

saldo *= 2         # Bonus double!
print(f"Setelah bonus: Rp{saldo:,}")

# Output:
# Saldo awal: Rp1,000,000
# Setelah terima transfer: Rp1,500,000
# Setelah bayar tagihan: Rp1,300,000
# Setelah bonus: Rp2,600,000
```

---

### 2.3.5 Operator Prioritas (Precedence) — Tabel Lengkap

Berikut tabel prioritas operator Python dari **tertinggi** ke **terendah**:

| Prioritas | Operator | Deskripsi |
|-----------|----------|-----------|
| 1 (Tertinggi) | `()` | Pengelompokan (tanda kurung) |
| 2 | `**` | Pangkat |
| 3 | `+x`, `-x`, `~x` | Unary plus, unary minus, bitwise NOT |
| 4 | `*`, `/`, `//`, `%` | Perkalian, pembagian, floor div, modulo |
| 5 | `+`, `-` | Penjumlahan, pengurangan |
| 6 | `<<`, `>>` | Bitwise shift |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `\|` | Bitwise OR |
| 10 | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `in` | Perbandingan, identitas, keanggotaan |
| 11 | `not` | Logika NOT |
| 12 | `and` | Logika AND |
| 13 (Terendah) | `or` | Logika OR |

```python
# Contoh prioritas operator dalam satu ekspresi
hasil = 2 + 3 * 4 > 10 and not False or True
# Langkah evaluasi:
# 1. 3 * 4 = 12          (perkalian dulu)
# 2. 2 + 12 = 14         (penjumlahan)
# 3. 14 > 10 = True      (perbandingan)
# 4. not False = True     (not)
# 5. True and True = True (and)
# 6. True or True = True  (or)
print(hasil)  # True

# Tips: selalu gunakan tanda kurung untuk kejelasan!
hasil = ((2 + (3 * 4)) > 10) and (not False) or True
print(hasil)  # True (sama, tapi lebih jelas)
```

---

## 2.4 Input dan Output

Program yang berguna biasanya perlu **berinteraksi** dengan pengguna — menerima data masukan (*input*) dan menampilkan hasil (*output*).

---

### 2.4.1 Output: print()

Fungsi `print()` digunakan untuk menampilkan informasi ke layar (konsol/terminal).

**Penggunaan Dasar:**

```python
# Print string
print("Halo, Dunia!")
print('Selamat datang di Python')

# Print variabel
nama = "Ahmad"
print(nama)

# Print beberapa nilai sekaligus
nama = "Ahmad"
umur = 19
print("Nama:", nama, "| Umur:", umur)
# Output: Nama: Ahmad | Umur: 19
```

**Parameter `sep` (Separator):**

```python
# Default separator adalah spasi
print("A", "B", "C")
# Output: A B C

# Mengubah separator
print("A", "B", "C", sep="-")
# Output: A-B-C

print("A", "B", "C", sep=" | ")
# Output: A | B | C

print("192", "168", "1", "1", sep=".")
# Output: 192.168.1.1

# Tanpa separator
print("A", "B", "C", sep="")
# Output: ABC
```

**Parameter `end` (Karakter Akhir):**

```python
# Default end adalah newline (\n) — pindah baris
print("Baris 1")
print("Baris 2")
# Output:
# Baris 1
# Baris 2

# Mengubah end (tidak pindah baris)
print("Loading", end="")
print("...", end="")
print(" Selesai!")
# Output: Loading... Selesai!

# Menggunakan end untuk dekorasi
print("*" * 20, end="\n\n")
print("Halo!")
# Output:
# ********************
#
# Halo!
```

**F-String untuk Output Terformat (Direkomendasikan!):**

```python
# Format angka desimal
pi = 3.14159265358979
print(f"Pi = {pi:.2f}")          # Pi = 3.14
print(f"Pi = {pi:.4f}")          # Pi = 3.1416
print(f"Pi = {pi:.0f}")          # Pi = 3

# Format angka dengan pemisah ribuan
populasi = 275000000
print(f"Populasi: {populasi:,}")         # Populasi: 275,000,000
print(f"Populasi: {populasi:,.0f}")      # Populasi: 275,000,000

# Format lebar kolom (alignment)
print(f"{'Nama':<20}{'NIM':>15}")
print(f"{'Ahmad Fauzi':<20}{'20240010015':>15}")
print(f"{'Budi Santoso':<20}{'20240010023':>15}")
# Output:
# Nama                            NIM
# Ahmad Fauzi              20240010015
# Budi Santoso             20240010023

# Format persentase
rasio = 0.856
print(f"Kehadiran: {rasio:.1%}")         # Kehadiran: 85.6%

# Padding dengan nol
nomor = 7
print(f"Nomor urut: {nomor:04d}")        # Nomor urut: 0007
```

**Contoh: Menampilkan Harga Terformat**

```python
harga = 15000
qty = 3
total = harga * qty
print(f"Total belanja: Rp{total:,}")
# Output: Total belanja: Rp45,000

# Lebih detail
print(f"Harga satuan : Rp{harga:>12,}")
print(f"Jumlah       : {qty:>12}")
print(f"{'─' * 27}")
print(f"Total        : Rp{total:>12,}")
```

---

### 2.4.2 Input: input()

Fungsi `input()` digunakan untuk menerima data dari pengguna melalui keyboard.

**Aturan Penting:** Fungsi `input()` **selalu mengembalikan string!** Jika Anda membutuhkan angka, Anda **harus mengonversinya** secara eksplisit.

```python
# Input string (langsung digunakan)
nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}!")

# Input integer (harus dikonversi!)
umur = int(input("Masukkan umur Anda: "))
print(f"Tahun depan umur Anda {umur + 1} tahun.")

# Input float (harus dikonversi!)
ipk = float(input("Masukkan IPK Anda: "))
print(f"IPK Anda: {ipk:.2f}")

# KESALAHAN UMUM:
# umur = input("Masukkan umur: ")
# print(umur + 1)  # TypeError! (string + integer)
```

**Contoh Program Interaktif:**

```python
# Biodata mahasiswa interaktif
print("=" * 40)
print("    FORMULIR DATA MAHASISWA")
print("=" * 40)

nama = input("Nama lengkap  : ")
nim = input("NIM           : ")
umur = int(input("Umur          : "))
ipk = float(input("IPK           : "))
prodi = input("Program studi : ")

print()
print("=" * 40)
print("    KARTU IDENTITAS MAHASISWA")
print("=" * 40)
print(f"Nama  : {nama}")
print(f"NIM   : {nim}")
print(f"Umur  : {umur} tahun")
print(f"IPK   : {ipk:.2f}")
print(f"Prodi : {prodi}")
print("=" * 40)
```

**Menangani Kesalahan Input:**

```python
# Apa yang terjadi jika user memasukkan huruf saat diminta angka?
# int("abc")  --> ValueError!

# Cara aman (akan dipelajari lebih detail di bab error handling):
try:
    umur = int(input("Masukkan umur Anda: "))
    print(f"Umur Anda: {umur}")
except ValueError:
    print("Error: Masukkan angka yang valid!")
```

---

## 2.5 Studi Kasus: Kalkulator Harga Warung

Berikut adalah contoh program lengkap yang mengintegrasikan semua konsep yang telah dipelajari di bab ini: variabel, tipe data, operator, input, dan output.

```python
# ============================================================
# Kalkulator Harga Warung Makan Sederhana
# Konteks: Warung makan di dekat kampus UAI
# ============================================================

print("=" * 50)
print("        WARUNG MAKAN PAK AHMAD")
print("     Jl. Sisingamangaraja, Jakarta")
print("=" * 50)
print()

# ---- DAFTAR HARGA ----
HARGA_NASI_GORENG = 15000
HARGA_MIE_GORENG = 13000
HARGA_AYAM_GEPREK = 18000
HARGA_ES_TEH = 5000
HARGA_ES_JERUK = 7000

# ---- MENAMPILKAN MENU ----
print("MENU:")
print(f"  1. Nasi Goreng   Rp{HARGA_NASI_GORENG:,}")
print(f"  2. Mie Goreng    Rp{HARGA_MIE_GORENG:,}")
print(f"  3. Ayam Geprek   Rp{HARGA_AYAM_GEPREK:,}")
print(f"  4. Es Teh        Rp{HARGA_ES_TEH:,}")
print(f"  5. Es Jeruk      Rp{HARGA_ES_JERUK:,}")
print("-" * 50)
print()

# ---- INPUT PESANAN ----
print("Masukkan jumlah pesanan (0 jika tidak pesan):")
qty_nasi_goreng = int(input("  Nasi Goreng  : "))
qty_mie_goreng = int(input("  Mie Goreng   : "))
qty_ayam_geprek = int(input("  Ayam Geprek  : "))
qty_es_teh = int(input("  Es Teh       : "))
qty_es_jeruk = int(input("  Es Jeruk     : "))

# ---- HITUNG SUBTOTAL PER ITEM ----
sub_nasi_goreng = HARGA_NASI_GORENG * qty_nasi_goreng
sub_mie_goreng = HARGA_MIE_GORENG * qty_mie_goreng
sub_ayam_geprek = HARGA_AYAM_GEPREK * qty_ayam_geprek
sub_es_teh = HARGA_ES_TEH * qty_es_teh
sub_es_jeruk = HARGA_ES_JERUK * qty_es_jeruk

# ---- HITUNG TOTAL ----
subtotal = (sub_nasi_goreng + sub_mie_goreng + sub_ayam_geprek
            + sub_es_teh + sub_es_jeruk)
pajak_persen = 10   # Pajak restoran 10%
pajak = subtotal * pajak_persen / 100
total = subtotal + pajak

# ---- CETAK STRUK ----
print()
print("=" * 50)
print("              STRUK PEMBAYARAN")
print("         WARUNG MAKAN PAK AHMAD")
print("=" * 50)

if qty_nasi_goreng > 0:
    print(f"  Nasi Goreng  x{qty_nasi_goreng:>3}    Rp{sub_nasi_goreng:>12,}")
if qty_mie_goreng > 0:
    print(f"  Mie Goreng   x{qty_mie_goreng:>3}    Rp{sub_mie_goreng:>12,}")
if qty_ayam_geprek > 0:
    print(f"  Ayam Geprek  x{qty_ayam_geprek:>3}    Rp{sub_ayam_geprek:>12,}")
if qty_es_teh > 0:
    print(f"  Es Teh       x{qty_es_teh:>3}    Rp{sub_es_teh:>12,}")
if qty_es_jeruk > 0:
    print(f"  Es Jeruk     x{qty_es_jeruk:>3}    Rp{sub_es_jeruk:>12,}")

print("-" * 50)
print(f"  Subtotal              Rp{subtotal:>12,}")
print(f"  Pajak ({pajak_persen}%)            Rp{pajak:>12,.0f}")
print("-" * 50)
print(f"  TOTAL BAYAR           Rp{total:>12,.0f}")
print("=" * 50)
print()
print("  Terima kasih atas kunjungan Anda!")
print("  Selamat menikmati hidangan.")
print("=" * 50)
```

**Contoh Output:**

```
==================================================
        WARUNG MAKAN PAK AHMAD
     Jl. Sisingamangaraja, Jakarta
==================================================

MENU:
  1. Nasi Goreng   Rp15,000
  2. Mie Goreng    Rp13,000
  3. Ayam Geprek   Rp18,000
  4. Es Teh        Rp5,000
  5. Es Jeruk      Rp7,000
--------------------------------------------------

Masukkan jumlah pesanan (0 jika tidak pesan):
  Nasi Goreng  : 2
  Mie Goreng   : 0
  Ayam Geprek  : 1
  Es Teh       : 3
  Es Jeruk     : 0

==================================================
              STRUK PEMBAYARAN
         WARUNG MAKAN PAK AHMAD
==================================================
  Nasi Goreng  x  2    Rp      30,000
  Ayam Geprek  x  1    Rp      18,000
  Es Teh       x  3    Rp      15,000
--------------------------------------------------
  Subtotal              Rp      63,000
  Pajak (10%)           Rp       6,300
--------------------------------------------------
  TOTAL BAYAR           Rp      69,300
==================================================

  Terima kasih atas kunjungan Anda!
  Selamat menikmati hidangan.
==================================================
```

---

## 2.6 Studi Kasus: Konversi Suhu

Program ini mengonversi suhu dari Celsius ke Fahrenheit dan Kelvin, menggunakan rumus fisika dasar.

**Rumus Konversi:**
- Fahrenheit = (Celsius x 9/5) + 32
- Kelvin = Celsius + 273.15

```python
# ============================================================
# Program Konversi Suhu
# Mengonversi Celsius ke Fahrenheit dan Kelvin
# ============================================================

print("=" * 40)
print("    KONVERSI SUHU")
print("=" * 40)
print()

# Input suhu dalam Celsius
celsius = float(input("Masukkan suhu dalam Celsius: "))

# Konversi
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

# Output hasil
print()
print("Hasil Konversi:")
print(f"  {celsius:.2f} °C = {fahrenheit:.2f} °F")
print(f"  {celsius:.2f} °C = {kelvin:.2f} K")
print()

# Interpretasi suhu
print("Interpretasi:")
if celsius < 0:
    print("  Suhu di bawah titik beku air.")
elif celsius == 0:
    print("  Suhu tepat di titik beku air.")
elif celsius < 30:
    print("  Suhu nyaman / sejuk.")
elif celsius < 40:
    print("  Suhu hangat / panas.")
elif celsius == 100:
    print("  Suhu tepat di titik didih air.")
else:
    print("  Suhu sangat panas!")
```

**Contoh Output:**

```
========================================
    KONVERSI SUHU
========================================

Masukkan suhu dalam Celsius: 36.5

Hasil Konversi:
  36.50 °C = 97.70 °F
  36.50 °C = 309.65 K

Interpretasi:
  Suhu hangat / panas.
```

---

## AI Corner: AI untuk Belajar Sintaks (Level: Dasar)

Dalam bab ini, kita memperkenalkan bagaimana **Kecerdasan Buatan (AI)** seperti ChatGPT, Claude, atau Gemini dapat membantu Anda memahami sintaks Python dengan lebih baik. Ini bukan pengganti belajar, tetapi alat bantu yang efektif jika digunakan dengan benar.

### Cara Menggunakan AI untuk Belajar Sintaks

**1. Meminta Penjelasan Konsep:**

```
Prompt yang baik:
"Jelaskan perbedaan operator / dan // di Python, berikan 3 contoh
masing-masing dengan output-nya."

Prompt yang kurang baik:
"Apa itu / di Python?"
```

> **Tips:** Semakin spesifik pertanyaan Anda, semakin baik jawaban yang Anda dapatkan. Sebutkan bahasa pemrograman (Python), minta contoh kode, dan minta penjelasan output.

**2. Meminta Contoh Kode:**

```
Prompt yang baik:
"Buatkan contoh program Python sederhana yang menggunakan f-string
untuk menampilkan data mahasiswa (nama, NIM, IPK) dalam format tabel.
Jelaskan setiap baris kodenya."

Prompt yang kurang baik:
"Buat program Python"
```

**3. Debugging dengan AI:**

```
Prompt yang baik:
"Saya mendapat error 'TypeError: can only concatenate str (not "int")
to str' pada kode berikut. Jelaskan mengapa error ini terjadi dan
bagaimana cara memperbaikinya:

umur = input('Masukkan umur: ')
print('Tahun depan umur Anda ' + umur + 1)
"
```

### Cara Memverifikasi Jawaban AI

AI tidak selalu benar. Berikut cara memverifikasi jawabannya:

1. **Jalankan kode yang diberikan AI** di interpreter Python Anda.
2. **Bandingkan output** aktual dengan yang diklaim AI.
3. **Cek dokumentasi resmi** Python di [docs.python.org](https://docs.python.org/3/).
4. **Uji edge cases** — coba input yang tidak biasa (angka negatif, nol, string kosong).

### Peringatan Penting

- AI mungkin memberikan **sintaks yang sudah usang** (outdated) — misalnya menggunakan `%` formatting alih-alih f-string.
- AI mungkin memberikan **jawaban yang terlihat benar tapi salah secara teknis** (hallucination).
- **Jangan hanya menyalin kode dari AI** tanpa memahaminya. Pastikan Anda memahami setiap baris sebelum menggunakannya.
- Gunakan AI sebagai **tutor**, bukan sebagai **joki** — tujuannya adalah agar Anda **belajar**, bukan sekadar menyelesaikan tugas.

> **Etika Akademik:** Menyerahkan kode hasil AI mentah-mentah sebagai tugas kuliah tanpa pemahaman dan modifikasi sendiri adalah bentuk ketidakjujuran akademik. Gunakan AI sebagai alat bantu belajar, bukan alat curang.

---

## Latihan Soal

### Tingkat Dasar

**Soal 1: Kartu Identitas Mahasiswa**

Buat program yang menerima input nama dan NIM dari pengguna, kemudian menampilkan kartu identitas mahasiswa dalam format yang rapi.

Contoh output yang diharapkan:
```
===================================
      KARTU IDENTITAS MAHASISWA
   Universitas Al Azhar Indonesia
===================================
  Nama  : Ahmad Fauzi
  NIM   : 20240010015
  Prodi : Informatika
===================================
```

**Soal 2: Kalkulator Sederhana**

Buat program yang menerima dua angka dari pengguna, kemudian menampilkan hasil dari keempat operasi aritmatika dasar (penjumlahan, pengurangan, perkalian, pembagian).

Contoh output:
```
Masukkan angka pertama: 12
Masukkan angka kedua: 5
Hasil:
  12 + 5 = 17
  12 - 5 = 7
  12 * 5 = 60
  12 / 5 = 2.40
```

**Soal 3: Tebak Tipe Data**

Tentukan tipe data dari setiap literal berikut (jawab tanpa menjalankan kode):

```python
a = 42                  # Tipe: ?
b = 3.14                # Tipe: ?
c = "Hello"             # Tipe: ?
d = True                # Tipe: ?
e = None                # Tipe: ?
f = "42"                # Tipe: ?
g = 0                   # Tipe: ?
h = 0.0                 # Tipe: ?
i = ""                  # Tipe: ?
j = False               # Tipe: ?
```

Verifikasi jawaban Anda menggunakan `type()`.

**Soal 4: Lingkaran**

Buat program yang menerima input jari-jari lingkaran, kemudian menghitung dan menampilkan luas dan keliling lingkaran.

Rumus:
- Luas = pi x r^2
- Keliling = 2 x pi x r
- Gunakan pi = 3.14159

**Soal 5: Konversi Mata Uang**

Buat program konversi mata uang dari IDR (Rupiah) ke USD (Dollar AS). Gunakan kurs `1 USD = Rp15.750`.

Contoh output:
```
Masukkan jumlah Rupiah: 5000000
Rp5,000,000 = $317.46 USD
```

---

### Tingkat Menengah

**Soal 1: Nota Minimarket**

Buat program nota pembelian minimarket yang menerima input minimal 3 item (nama, harga satuan, jumlah). Program harus menghitung:
- Subtotal per item
- Total sebelum diskon
- Diskon 5% untuk pembelian di atas Rp100.000
- PPN 11%
- Total akhir yang harus dibayar

Tampilkan nota dalam format yang rapi dan profesional.

**Soal 2: Kalkulator BMI**

Buat program yang menghitung Body Mass Index (BMI) dari input berat badan (kg) dan tinggi badan (cm).

Rumus: BMI = berat / (tinggi_m)^2

Tampilkan kategori:
- BMI < 18.5 : Berat badan kurang
- 18.5 <= BMI < 25.0 : Berat badan normal
- 25.0 <= BMI < 30.0 : Berat badan berlebih
- BMI >= 30.0 : Obesitas

**Soal 3: Konversi Waktu**

Buat program yang mengonversi total detik menjadi format jam:menit:detik.

Contoh:
- Input: 3661 detik
- Output: 1 jam, 1 menit, 1 detik

Gunakan operator `//` dan `%` untuk konversi ini.

**Soal 4: Biaya Parkir**

Buat program perhitungan biaya parkir dengan ketentuan:
- Motor: Rp2.000 per jam (pembulatan ke atas)
- Mobil: Rp5.000 per jam (pembulatan ke atas)
- Input: jenis kendaraan, jam masuk, jam keluar
- Hitung durasi dan total biaya

**Soal 5: Representasi Biner**

Buat program yang menerima input bilangan bulat positif dan menampilkan representasinya dalam format:
- Desimal
- Biner (tanpa awalan 0b)
- Oktal (tanpa awalan 0o)
- Heksadesimal (tanpa awalan 0x)
- Jumlah bit yang diperlukan untuk menyimpan bilangan tersebut

---

### Tingkat Mahir

**Soal 1: Kalkulator Investasi (Compound Interest)**

Buat program kalkulator investasi yang menghitung pertumbuhan uang dengan bunga majemuk.

Rumus: A = P x (1 + r/n)^(n*t)

Di mana:
- A = jumlah akhir
- P = modal awal (principal)
- r = suku bunga tahunan (annual rate)
- n = frekuensi penggabungan bunga per tahun (compounding frequency)
- t = jangka waktu dalam tahun

Program harus:
- Menerima input semua variabel di atas
- Menampilkan pertumbuhan per tahun
- Menampilkan total bunga yang diperoleh

**Soal 2: Split Bill Restoran**

Buat program untuk membagi tagihan restoran. Program harus:
- Menerima input total tagihan makanan
- Menambahkan pajak restoran (10%)
- Menerima input persentase tip (opsional, default 0%)
- Menerima input jumlah orang yang membagi
- Menampilkan rincian: subtotal, pajak, tip, total, dan bayar per orang
- Semua angka diformat dalam Rupiah

**Soal 3: Tantangan — Tukar Dua Variabel (3 Cara)**

Tanpa menggunakan variabel ketiga (temporary variable), tukar nilai dua variabel `a` dan `b` menggunakan **3 cara berbeda**:

1. Cara Pythonic (tuple unpacking)
2. Cara aritmatika (penjumlahan dan pengurangan)
3. Cara bitwise (XOR) — untuk integer saja

Jelaskan langkah-langkah setiap cara dan buktikan hasilnya.

> **Hint untuk cara 2:**
> ```
> a = a + b
> b = a - b
> a = a - b
> ```

> **Hint untuk cara 3:**
> ```
> a = a ^ b
> b = a ^ b
> a = a ^ b
> ```

---

## Rangkuman

Berikut adalah poin-poin utama yang telah dibahas dalam bab ini:

1. **Variabel** adalah tempat penyimpanan data di memori yang diberi nama. Python menggunakan dynamic typing, sehingga tipe data variabel ditentukan secara otomatis berdasarkan nilai yang diberikan.

2. **Penamaan variabel** harus mengikuti aturan: diawali huruf atau underscore, tidak menggunakan kata kunci Python, dan bersifat case-sensitive. Konvensi Python (PEP 8) merekomendasikan `snake_case`.

3. **Assignment** menggunakan operator `=` untuk memberikan nilai ke variabel. Python mendukung multiple assignment (`x, y = 1, 2`) dan swap elegan (`x, y = y, x`).

4. **Tipe data dasar Python** meliputi:
   - `int` — bilangan bulat (tanpa batas ukuran)
   - `float` — bilangan desimal (perhatikan masalah presisi)
   - `str` — teks (mendukung single, double, dan triple quotes)
   - `bool` — nilai logika (`True` / `False`)
   - `NoneType` — ketiadaan nilai (`None`)

5. **Type checking** menggunakan `type()` dan `isinstance()`. **Type conversion** menggunakan `int()`, `float()`, `str()`, dan `bool()`.

6. **Operator aritmatika** (`+`, `-`, `*`, `/`, `//`, `%`, `**`) digunakan untuk perhitungan matematika. Perhatikan perbedaan `/` (selalu float) dan `//` (floor division).

7. **Operator perbandingan** (`==`, `!=`, `>`, `<`, `>=`, `<=`) menghasilkan boolean. Python mendukung chained comparison (`17 <= umur <= 25`).

8. **Operator logika** (`and`, `or`, `not`) digunakan untuk menggabungkan kondisi. Pahami short-circuit evaluation untuk efisiensi dan keamanan kode.

9. **Operator assignment gabungan** (`+=`, `-=`, `*=`, dll.) menggabungkan operasi aritmatika dengan assignment dalam satu langkah.

10. **Prioritas operator** mengikuti aturan hierarki (PEMDAS). Selalu gunakan tanda kurung `()` jika ragu tentang urutan evaluasi.

11. **Output** menggunakan `print()` dengan dukungan f-string untuk format yang elegan. Perhatikan parameter `sep` dan `end` untuk kontrol tambahan.

12. **Input** menggunakan `input()` yang **selalu mengembalikan string**. Konversi eksplisit (`int()`, `float()`) diperlukan untuk input numerik.

13. **AI dapat membantu** belajar sintaks Python, tetapi selalu verifikasi jawabannya dan pastikan Anda memahami kode sebelum menggunakannya.

---

## Referensi

1. Downey, A. B. (2015). *Think Python: How to Think Like a Computer Scientist* (2nd ed.). O'Reilly Media. [https://greenteapress.com/thinkpython2/](https://greenteapress.com/thinkpython2/)

2. Lutz, M. (2013). *Learning Python* (5th ed.). O'Reilly Media.

3. Matthes, E. (2019). *Python Crash Course: A Hands-On, Project-Based Introduction to Programming* (2nd ed.). No Starch Press.

4. Python Software Foundation. (n.d.). *The Python Tutorial*. [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)

5. Python Software Foundation. (n.d.). *PEP 8 — Style Guide for Python Code*. [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)

6. Python Software Foundation. (n.d.). *Built-in Types*. [https://docs.python.org/3/library/stdtypes.html](https://docs.python.org/3/library/stdtypes.html)

7. Severance, C. (2016). *Python for Everybody: Exploring Data in Python 3*. [https://www.py4e.com/book](https://www.py4e.com/book)

8. Sweigart, A. (2019). *Automate the Boring Stuff with Python* (2nd ed.). No Starch Press. [https://automatetheboringstuff.com/](https://automatetheboringstuff.com/)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
