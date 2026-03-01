# BAB 5: FUNGSI DAN MODULARITAS

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|:------------:|
| CPMK-4.1 | Mendefinisikan fungsi dengan parameter dan return value | C3 (Menerapkan) |
| CPMK-4.2 | Menerapkan prinsip DRY dan dekomposisi top-down | C3 (Menerapkan) |
| CPMK-4.3 | Menjelaskan konsep scope (local vs global) | C2 (Memahami) |
| CPMK-4.4 | Menggunakan docstring dan dokumentasi fungsi | C3 (Menerapkan) |

**Estimasi Waktu:** 2 pertemuan (masing-masing 2 × 50 menit)

**Prasyarat:** Mahasiswa telah memahami materi Bab 1–4 (Pengantar Algoritma, Variabel & Tipe Data, Seleksi, dan Perulangan).

---

## 5.1 Konsep Fungsi

### 5.1.1 Mengapa Perlu Fungsi?

Bayangkan Anda memiliki program yang perlu menghitung luas lingkaran di banyak tempat berbeda. Tanpa fungsi, kode Anda akan terlihat seperti ini:

```python
# TANPA fungsi — kode berulang dan rawan kesalahan!
import math

# Hitung luas lingkaran pertama
jari_jari_1 = 7
luas_1 = math.pi * jari_jari_1 ** 2
print(f"Luas lingkaran 1: {luas_1:.2f}")

# Hitung luas lingkaran kedua
jari_jari_2 = 14
luas_2 = math.pi * jari_jari_2 ** 2
print(f"Luas lingkaran 2: {luas_2:.2f}")

# Hitung luas lingkaran ketiga
jari_jari_3 = 21
luas_3 = math.pi * jari_jari_3 ** 2
print(f"Luas lingkaran 3: {luas_3:.2f}")
```

Perhatikan bahwa rumus `math.pi * jari_jari ** 2` diulang **tiga kali**. Bagaimana jika ada kesalahan rumus? Anda harus memperbaikinya di tiga tempat! Bagaimana jika perlu menghitung untuk 100 lingkaran?

Dengan fungsi, kode menjadi jauh lebih rapi:

```python
import math

def hitung_luas_lingkaran(jari_jari):
    """Menghitung luas lingkaran berdasarkan jari-jari."""
    return math.pi * jari_jari ** 2

# Tinggal panggil fungsi — rapi dan mudah diubah
print(f"Luas lingkaran 1: {hitung_luas_lingkaran(7):.2f}")
print(f"Luas lingkaran 2: {hitung_luas_lingkaran(14):.2f}")
print(f"Luas lingkaran 3: {hitung_luas_lingkaran(21):.2f}")
```

**Analogi kehidupan sehari-hari:**

Fungsi seperti **resep masakan**:
- **Nama resep** = nama fungsi (misalnya `buat_nasi_goreng`)
- **Bahan-bahan** = parameter (nasi, telur, kecap, bumbu)
- **Langkah-langkah** = body fungsi (instruksi memasak)
- **Hasil masakan** = return value (nasi goreng yang siap dimakan)

Anda menulis resep **satu kali**, lalu bisa menggunakannya **berulang kali** tanpa harus mengingat ulang langkah-langkahnya.

### 5.1.2 Apa Itu Fungsi?

**Fungsi** adalah blok kode yang diberi nama, dirancang untuk melakukan **satu tugas tertentu**, dan dapat dipanggil (digunakan) berulang kali dari bagian program manapun.

```
┌─────────────────────────────────────────┐
│           DEFINISI FUNGSI               │
│                                         │
│   def nama_fungsi(parameter):           │
│       """Docstring penjelasan"""         │
│       # instruksi-instruksi             │
│       return hasil                      │
│                                         │
├─────────────────────────────────────────┤
│           PEMANGGILAN FUNGSI            │
│                                         │
│   hasil = nama_fungsi(argumen)          │
│                                         │
└─────────────────────────────────────────┘
```

**Istilah penting:**

| Istilah | Penjelasan | Contoh |
|---------|------------|--------|
| **Definisi** (`def`) | Membuat/mendaftarkan fungsi | `def sapa(nama):` |
| **Parameter** | Variabel di definisi fungsi | `nama` dalam `def sapa(nama):` |
| **Argumen** | Nilai yang dikirim saat memanggil | `"Ahmad"` dalam `sapa("Ahmad")` |
| **Body** | Isi/instruksi dalam fungsi | Kode yang di-indent |
| **Return value** | Nilai yang dikembalikan fungsi | `return hasil` |
| **Pemanggilan** (call) | Mengeksekusi fungsi | `sapa("Ahmad")` |

### 5.1.3 Keuntungan Menggunakan Fungsi

| Keuntungan | Penjelasan |
|------------|------------|
| **Reusability** (Dapat digunakan ulang) | Tulis sekali, gunakan berkali-kali |
| **Readability** (Mudah dibaca) | Nama fungsi menjelaskan apa yang dilakukan |
| **Maintainability** (Mudah dipelihara) | Perubahan cukup di satu tempat |
| **Testability** (Mudah diuji) | Setiap fungsi bisa diuji secara terpisah |
| **Abstraksi** | Menyembunyikan detail implementasi |

---

## 5.2 Mendefinisikan dan Memanggil Fungsi

### 5.2.1 Sintaks Dasar

```python
def nama_fungsi():
    """Docstring: penjelasan singkat fungsi."""
    # body fungsi
    pass
```

**Aturan penamaan fungsi (sama dengan variabel):**
- Gunakan huruf kecil dan underscore: `hitung_luas`, `cek_prima`
- Nama harus deskriptif: `hitung_rata_rata` lebih baik dari `hr`
- Diawali huruf atau underscore, tidak boleh dimulai angka
- Tidak boleh menggunakan kata kunci Python (`def`, `if`, `while`, dll.)

**Contoh fungsi sederhana tanpa parameter dan tanpa return:**

```python
def sapa_selamat_datang():
    """Menampilkan pesan selamat datang."""
    print("=" * 40)
    print("  SELAMAT DATANG DI PROGRAM KAMI")
    print("  Universitas Al Azhar Indonesia")
    print("=" * 40)

# Memanggil fungsi
sapa_selamat_datang()
```

Output:
```
========================================
  SELAMAT DATANG DI PROGRAM KAMI
  Universitas Al Azhar Indonesia
========================================
```

### 5.2.2 Fungsi dengan Parameter

Parameter memungkinkan fungsi menerima **input** dari luar sehingga fungsi menjadi lebih fleksibel.

```python
def sapa(nama):
    """Menyapa seseorang berdasarkan nama."""
    print(f"Assalamu'alaikum, {nama}!")
    print(f"Selamat datang di Prodi Informatika.")

# Memanggil dengan argumen berbeda
sapa("Ahmad")
sapa("Siti")
sapa("Budi")
```

Output:
```
Assalamu'alaikum, Ahmad!
Selamat datang di Prodi Informatika.
Assalamu'alaikum, Siti!
Selamat datang di Prodi Informatika.
Assalamu'alaikum, Budi!
Selamat datang di Prodi Informatika.
```

**Fungsi dengan beberapa parameter:**

```python
def perkenalan(nama, umur, prodi):
    """Menampilkan data perkenalan mahasiswa."""
    print(f"Nama  : {nama}")
    print(f"Umur  : {umur} tahun")
    print(f"Prodi : {prodi}")
    print("-" * 30)

perkenalan("Ahmad", 19, "Informatika")
perkenalan("Siti", 20, "Sistem Informasi")
```

### 5.2.3 Fungsi dengan Return Value

Fungsi yang mengembalikan nilai menggunakan kata kunci `return`. Ini memungkinkan hasil perhitungan digunakan di bagian lain program.

```python
def hitung_luas_persegi(sisi):
    """Menghitung luas persegi."""
    luas = sisi * sisi
    return luas

def hitung_keliling_persegi(sisi):
    """Menghitung keliling persegi."""
    return 4 * sisi

# Menggunakan return value
sisi = 5
luas = hitung_luas_persegi(sisi)
keliling = hitung_keliling_persegi(sisi)
print(f"Persegi dengan sisi {sisi}:")
print(f"  Luas     = {luas}")
print(f"  Keliling = {keliling}")
```

Output:
```
Persegi dengan sisi 5:
  Luas     = 25
  Keliling = 20
```

**Perbedaan `print` vs `return`:**

Ini adalah salah satu konsep yang sering membingungkan pemula:

```python
# Fungsi dengan print — hanya MENAMPILKAN, tidak mengembalikan nilai
def tambah_print(a, b):
    print(a + b)

# Fungsi dengan return — MENGEMBALIKAN nilai yang bisa digunakan lagi
def tambah_return(a, b):
    return a + b

# Perhatikan perbedaannya:
hasil_print = tambah_print(3, 4)    # Menampilkan: 7
print(f"hasil_print = {hasil_print}")  # Output: hasil_print = None

hasil_return = tambah_return(3, 4)  # Tidak menampilkan apa-apa
print(f"hasil_return = {hasil_return}")  # Output: hasil_return = 7

# Return value bisa digunakan dalam perhitungan lanjutan
total = tambah_return(3, 4) + tambah_return(5, 6)
print(f"Total: {total}")  # Output: Total: 18
```

> **Tips Penting:** Gunakan `return` jika Anda ingin **menggunakan hasil** fungsi di tempat lain. Gunakan `print` hanya jika Anda ingin **menampilkan** sesuatu ke layar. Dalam banyak kasus, `return` lebih baik karena membuat fungsi lebih fleksibel.

### 5.2.4 Fungsi dengan Multiple Return Values

Python memungkinkan fungsi mengembalikan **lebih dari satu nilai** menggunakan tuple:

```python
def hitung_statistik(angka_list):
    """Menghitung nilai minimum, maksimum, dan rata-rata dari list."""
    nilai_min = min(angka_list)
    nilai_max = max(angka_list)
    rata_rata = sum(angka_list) / len(angka_list)
    return nilai_min, nilai_max, rata_rata

# Menggunakan multiple return values
nilai = [85, 90, 78, 92, 88, 76, 95]
minimum, maksimum, rerata = hitung_statistik(nilai)

print(f"Nilai minimum : {minimum}")
print(f"Nilai maksimum: {maksimum}")
print(f"Rata-rata     : {rerata:.2f}")
```

Output:
```
Nilai minimum : 76
Nilai maksimum: 95
Rata-rata     : 86.29
```

### 5.2.5 Flowchart Pemanggilan Fungsi

Berikut visualisasi alur eksekusi ketika sebuah fungsi dipanggil:

```
Program Utama              Fungsi hitung_luas(p, l)
─────────────              ─────────────────────────
     │
     │  x = 10
     │  y = 5
     │
     │  luas = hitung_luas(x, y)
     │────────────────────────►  p = 10, l = 5
     │                           │
     │                           │  hasil = p * l
     │                           │  hasil = 50
     │                           │
     │  luas = 50  ◄─────────────│  return hasil
     │
     │  print(luas) → 50
     │
     ▼
```

---

## 5.3 Jenis-Jenis Parameter

### 5.3.1 Positional Parameter

Parameter yang diisi berdasarkan **urutan posisi** saat pemanggilan:

```python
def buat_email(nama, domain):
    """Membuat alamat email dari nama dan domain."""
    # Nama diubah ke lowercase dan spasi diganti titik
    username = nama.lower().replace(" ", ".")
    return f"{username}@{domain}"

# Urutan argumen HARUS sesuai urutan parameter
email = buat_email("Ahmad Fadillah", "uai.ac.id")
print(email)  # Output: ahmad.fadillah@uai.ac.id

# SALAH — urutan tertukar!
email_salah = buat_email("uai.ac.id", "Ahmad Fadillah")
print(email_salah)  # Output: uai.ac.id@Ahmad Fadillah (tidak masuk akal!)
```

### 5.3.2 Default Parameter

Parameter yang memiliki **nilai bawaan** (default) jika tidak diisi saat pemanggilan:

```python
def sapa_mahasiswa(nama, prodi="Informatika", tahun=2024):
    """Menyapa mahasiswa dengan data default."""
    print(f"Halo {nama}!")
    print(f"Prodi: {prodi}, Angkatan: {tahun}")
    print()

# Tanpa default — menggunakan nilai default
sapa_mahasiswa("Ahmad")
# Output:
# Halo Ahmad!
# Prodi: Informatika, Angkatan: 2024

# Mengubah satu default
sapa_mahasiswa("Siti", "Sistem Informasi")
# Output:
# Halo Siti!
# Prodi: Sistem Informasi, Angkatan: 2024

# Mengubah semua default
sapa_mahasiswa("Budi", "Teknik Elektro", 2023)
# Output:
# Halo Budi!
# Prodi: Teknik Elektro, Angkatan: 2023
```

> **Aturan Penting:** Parameter dengan default value harus ditempatkan **setelah** parameter tanpa default. `def fungsi(a, b=10)` benar, tetapi `def fungsi(a=10, b)` akan menghasilkan `SyntaxError`.

### 5.3.3 Keyword Argument

Saat memanggil fungsi, argumen bisa dikirim menggunakan **nama parameter** sehingga urutan tidak penting:

```python
def daftar_matakuliah(nama_mk, sks, semester, dosen):
    """Menampilkan informasi mata kuliah."""
    print(f"Mata Kuliah : {nama_mk}")
    print(f"SKS         : {sks}")
    print(f"Semester    : {semester}")
    print(f"Dosen       : {dosen}")
    print()

# Dengan keyword argument — urutan bebas
daftar_matakuliah(
    dosen="Tri Aji Nugroho",
    nama_mk="Algoritma dan Pemrograman",
    semester=1,
    sks=3
)

# Campuran positional dan keyword
daftar_matakuliah(
    "Struktur Data",  # positional (nama_mk)
    3,                 # positional (sks)
    semester=2,        # keyword
    dosen="Dr. Ahmad"  # keyword
)
```

### 5.3.4 Arbitrary Arguments (*args dan **kwargs)

Untuk fungsi yang menerima **jumlah argumen tidak tentu**:

```python
# *args — menerima argumen positional tak terbatas (sebagai tuple)
def hitung_rata_rata(*nilai):
    """Menghitung rata-rata dari sejumlah nilai."""
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)

print(hitung_rata_rata(85, 90, 78))         # Output: 84.33...
print(hitung_rata_rata(90, 85, 92, 88, 76)) # Output: 86.2

# **kwargs — menerima keyword argument tak terbatas (sebagai dictionary)
def cetak_profil(**data):
    """Mencetak profil berdasarkan data yang diberikan."""
    print("=== PROFIL ===")
    for kunci, nilai in data.items():
        print(f"  {kunci}: {nilai}")
    print()

cetak_profil(nama="Ahmad", umur=19, prodi="Informatika", hobi="Coding")
```

Output:
```
=== PROFIL ===
  nama: Ahmad
  umur: 19
  prodi: Informatika
  hobi: Coding
```

---

## 5.4 Scope (Ruang Lingkup Variabel)

### 5.4.1 Local Scope vs Global Scope

**Scope** menentukan di mana sebuah variabel bisa diakses. Ini adalah konsep fundamental yang harus dipahami agar terhindar dari bug yang sulit dilacak.

```python
# Variabel GLOBAL — didefinisikan di luar fungsi
nama_universitas = "Universitas Al Azhar Indonesia"

def tampilkan_info():
    # Variabel LOCAL — didefinisikan di dalam fungsi
    nama_prodi = "Informatika"
    print(f"Universitas: {nama_universitas}")  # Bisa akses global
    print(f"Prodi: {nama_prodi}")              # Bisa akses local

tampilkan_info()
# print(nama_prodi)  # ERROR! nama_prodi tidak dikenal di luar fungsi
```

**Visualisasi Scope:**

```
┌──────────────────────────────────────────────┐
│                GLOBAL SCOPE                   │
│                                               │
│   nama_universitas = "UAI"                    │
│                                               │
│   ┌──────────────────────────────────────┐   │
│   │          LOCAL SCOPE                  │   │
│   │       (fungsi tampilkan_info)         │   │
│   │                                       │   │
│   │   nama_prodi = "Informatika"          │   │
│   │                                       │   │
│   │   ✓ Bisa akses nama_universitas      │   │
│   │   ✓ Bisa akses nama_prodi            │   │
│   │                                       │   │
│   └──────────────────────────────────────┘   │
│                                               │
│   ✓ Bisa akses nama_universitas              │
│   ✗ TIDAK bisa akses nama_prodi              │
│                                               │
└──────────────────────────────────────────────┘
```

### 5.4.2 Variabel Local Menyembunyikan Variabel Global

Ketika variabel local memiliki nama yang sama dengan variabel global, variabel local **menyembunyikan** (shadowing) variabel global:

```python
x = 100  # variabel global

def ubah_x():
    x = 50  # variabel LOCAL baru — BUKAN mengubah global!
    print(f"Di dalam fungsi: x = {x}")  # Output: 50

ubah_x()
print(f"Di luar fungsi: x = {x}")  # Output: 100 (tidak berubah!)
```

> **Perhatian:** Ini adalah sumber bug yang sangat umum bagi pemula! Variabel di dalam fungsi yang memiliki nama sama dengan variabel global adalah variabel **baru** yang terpisah.

### 5.4.3 Kata Kunci `global`

Jika Anda **benar-benar perlu** mengubah variabel global dari dalam fungsi, gunakan kata kunci `global`:

```python
skor_total = 0

def tambah_skor(poin):
    global skor_total  # Deklarasi: kita akan mengubah variabel global
    skor_total += poin

tambah_skor(10)
print(f"Skor: {skor_total}")  # Output: 10
tambah_skor(25)
print(f"Skor: {skor_total}")  # Output: 35
```

> **Peringatan:** Penggunaan `global` sebaiknya **dihindari** sebisa mungkin. Fungsi yang mengubah variabel global membuat program sulit diprediksi dan di-debug. Lebih baik gunakan parameter dan return value. Ini disebut prinsip **pure function** — fungsi yang hanya bergantung pada inputnya dan tidak memiliki efek samping.

**Cara yang lebih baik (tanpa `global`):**

```python
def tambah_skor(skor_saat_ini, poin):
    """Mengembalikan skor baru tanpa mengubah variabel global."""
    return skor_saat_ini + poin

skor = 0
skor = tambah_skor(skor, 10)
print(f"Skor: {skor}")  # Output: 10
skor = tambah_skor(skor, 25)
print(f"Skor: {skor}")  # Output: 35
```

### 5.4.4 Aturan LEGB (Resolusi Scope Python)

Python mencari variabel dengan urutan **LEGB**:

```
L — Local      : Di dalam fungsi saat ini
E — Enclosing  : Di fungsi pembungkus (nested function)
G — Global     : Di level modul (file)
B — Built-in   : Di namespace Python bawaan (print, len, dll.)
```

```python
x = "global"  # G — Global

def luar():
    x = "enclosing"  # E — Enclosing

    def dalam():
        x = "local"  # L — Local
        print(x)     # Mencari: Local → ditemukan!

    dalam()
    print(x)  # Mencari: Local (tidak ada) → Enclosing → ditemukan!

luar()
print(x)  # Mencari: Local (tidak ada) → Enclosing (tidak ada) → Global → ditemukan!
```

Output:
```
local
enclosing
global
```

---

## 5.5 Prinsip DRY dan Dekomposisi

### 5.5.1 Prinsip DRY (Don't Repeat Yourself)

Prinsip DRY menyatakan: **setiap bagian pengetahuan harus memiliki satu representasi tunggal** dalam sistem. Jika Anda melihat kode yang sama diulang, itu adalah sinyal untuk membuat fungsi.

**Contoh pelanggaran DRY dan perbaikannya:**

```python
# SEBELUM (MELANGGAR DRY) — kode sama diulang 3 kali
print("=" * 50)
print("LAPORAN NILAI MAHASISWA")
print("Universitas Al Azhar Indonesia")
print("=" * 50)

# ... kode lainnya ...

print("=" * 50)
print("LAPORAN KEHADIRAN MAHASISWA")
print("Universitas Al Azhar Indonesia")
print("=" * 50)

# ... kode lainnya ...

print("=" * 50)
print("LAPORAN AKTIVITAS MAHASISWA")
print("Universitas Al Azhar Indonesia")
print("=" * 50)
```

```python
# SESUDAH (MENERAPKAN DRY) — fungsi menghilangkan duplikasi
def cetak_header(judul):
    """Mencetak header laporan dengan format standar."""
    print("=" * 50)
    print(judul)
    print("Universitas Al Azhar Indonesia")
    print("=" * 50)

cetak_header("LAPORAN NILAI MAHASISWA")
# ... kode lainnya ...
cetak_header("LAPORAN KEHADIRAN MAHASISWA")
# ... kode lainnya ...
cetak_header("LAPORAN AKTIVITAS MAHASISWA")
```

### 5.5.2 Dekomposisi Top-Down

**Dekomposisi top-down** adalah teknik memecah masalah besar menjadi sub-masalah yang lebih kecil dan lebih mudah dikelola. Setiap sub-masalah diimplementasikan sebagai fungsi terpisah.

**Contoh: Program Manajemen Nilai Mahasiswa**

Langkah 1 — Identifikasi masalah utama:
```
Program Manajemen Nilai
├── Input data mahasiswa
├── Hitung nilai akhir
├── Tentukan grade huruf
└── Tampilkan hasil
```

Langkah 2 — Implementasi masing-masing fungsi:

```python
def input_nilai():
    """Meminta input nilai dari pengguna."""
    nama = input("Nama mahasiswa: ")
    tugas = float(input("Nilai tugas (0-100): "))
    uts = float(input("Nilai UTS (0-100): "))
    uas = float(input("Nilai UAS (0-100): "))
    return nama, tugas, uts, uas

def hitung_nilai_akhir(tugas, uts, uas):
    """Menghitung nilai akhir dengan bobot tertentu.

    Bobot: Tugas 30%, UTS 30%, UAS 40%
    """
    return tugas * 0.30 + uts * 0.30 + uas * 0.40

def tentukan_grade(nilai_akhir):
    """Menentukan grade huruf berdasarkan nilai akhir."""
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 55:
        return "C"
    elif nilai_akhir >= 40:
        return "D"
    else:
        return "E"

def tampilkan_hasil(nama, tugas, uts, uas, nilai_akhir, grade):
    """Menampilkan hasil penilaian dalam format tabel."""
    print("\n" + "=" * 40)
    print("     HASIL PENILAIAN MAHASISWA")
    print("=" * 40)
    print(f"  Nama        : {nama}")
    print(f"  Tugas       : {tugas:.1f}")
    print(f"  UTS         : {uts:.1f}")
    print(f"  UAS         : {uas:.1f}")
    print(f"  Nilai Akhir : {nilai_akhir:.2f}")
    print(f"  Grade       : {grade}")
    print("=" * 40)

# Program utama — mudah dibaca karena terdekomposisi
def main():
    """Fungsi utama program manajemen nilai."""
    nama, tugas, uts, uas = input_nilai()
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    grade = tentukan_grade(nilai_akhir)
    tampilkan_hasil(nama, tugas, uts, uas, nilai_akhir, grade)

main()
```

> **Perhatikan** bagaimana fungsi `main()` menjadi sangat **mudah dibaca** — Anda bisa memahami alur program hanya dari nama-nama fungsi tanpa perlu membaca detail implementasinya.

### 5.5.3 Prinsip Single Responsibility

Setiap fungsi seharusnya hanya bertanggung jawab atas **satu tugas** saja. Jika sebuah fungsi melakukan terlalu banyak hal, pecah menjadi beberapa fungsi yang lebih kecil.

```python
# BURUK — satu fungsi melakukan terlalu banyak hal
def proses_semua(data):
    # Input, validasi, perhitungan, dan output semua di satu tempat
    # ... sangat panjang dan sulit di-debug ...
    pass

# BAIK — setiap fungsi punya satu tanggung jawab
def validasi_input(data):
    """Hanya memvalidasi data input."""
    pass

def hitung_hasil(data_valid):
    """Hanya menghitung hasil."""
    pass

def format_output(hasil):
    """Hanya memformat output."""
    pass
```

---

## 5.6 Docstring dan Dokumentasi Fungsi

### 5.6.1 Apa Itu Docstring?

**Docstring** (documentation string) adalah string yang ditempatkan sebagai **baris pertama** di dalam fungsi untuk mendokumentasikan apa yang dilakukan fungsi tersebut.

```python
def hitung_bmi(berat_kg, tinggi_m):
    """Menghitung Body Mass Index (BMI).

    BMI dihitung dengan rumus: berat / tinggi^2

    Parameters:
        berat_kg (float): Berat badan dalam kilogram
        tinggi_m (float): Tinggi badan dalam meter

    Returns:
        float: Nilai BMI

    Example:
        >>> hitung_bmi(70, 1.75)
        22.857142857142858
    """
    return berat_kg / (tinggi_m ** 2)
```

**Mengakses docstring:**

```python
# Cara melihat docstring sebuah fungsi
print(hitung_bmi.__doc__)

# Atau menggunakan help()
help(hitung_bmi)
```

### 5.6.2 Format Docstring

**One-line docstring** — untuk fungsi sederhana:
```python
def kuadrat(n):
    """Mengembalikan kuadrat dari n."""
    return n ** 2
```

**Multi-line docstring** — untuk fungsi yang lebih kompleks:
```python
def cari_mahasiswa(daftar, nim):
    """Mencari mahasiswa berdasarkan NIM.

    Melakukan pencarian linear pada daftar mahasiswa.
    Mengembalikan data mahasiswa jika ditemukan.

    Parameters:
        daftar (list): Daftar dictionary berisi data mahasiswa
        nim (str): Nomor Induk Mahasiswa yang dicari

    Returns:
        dict: Data mahasiswa jika ditemukan
        None: Jika mahasiswa tidak ditemukan
    """
    for mhs in daftar:
        if mhs["nim"] == nim:
            return mhs
    return None
```

### 5.6.3 Mengapa Docstring Penting?

1. **Membantu orang lain (dan diri Anda di masa depan)** memahami kode
2. **IDE dan editor** menampilkan docstring sebagai tooltip/hint
3. **Alat dokumentasi otomatis** (seperti Sphinx) menggunakannya untuk membuat dokumentasi
4. **Melatih kebiasaan baik** dalam pengembangan perangkat lunak profesional

---

## 5.7 Fungsi sebagai Abstraksi

### 5.7.1 Konsep Abstraksi

**Abstraksi** adalah proses menyembunyikan detail implementasi dan hanya menampilkan **antarmuka** (interface) yang relevan. Fungsi adalah alat utama untuk mencapai abstraksi dalam pemrograman.

```python
# Pengguna fungsi TIDAK PERLU tahu cara kerjanya di dalam
# Cukup tahu: input apa, output apa
hasil = sorted([3, 1, 4, 1, 5, 9, 2, 6])
# Kita tidak perlu tahu algoritma sorting yang dipakai!
# Cukup tahu: sorted() menerima list, mengembalikan list terurut
```

**Analogi:**

Anda tidak perlu tahu cara mesin ATM bekerja di dalam untuk bisa mengambil uang. Yang Anda perlu tahu adalah:
- **Input:** Kartu ATM + PIN + jumlah penarikan
- **Output:** Uang tunai + struk

### 5.7.2 Contoh: Membangun Library Fungsi Matematika

```python
# File: matematika.py — Library fungsi matematika kustom

def faktorial(n):
    """Menghitung faktorial dari n (n!).

    Parameters:
        n (int): Bilangan bulat non-negatif

    Returns:
        int: Hasil n!
    """
    if n < 0:
        return None  # Faktorial tidak terdefinisi untuk negatif
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

def is_prima(n):
    """Memeriksa apakah n adalah bilangan prima.

    Parameters:
        n (int): Bilangan bulat positif

    Returns:
        bool: True jika prima, False jika bukan
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """Menghasilkan n bilangan Fibonacci pertama.

    Parameters:
        n (int): Jumlah bilangan yang diinginkan

    Returns:
        list: Daftar bilangan Fibonacci
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def pangkat(basis, eksponen):
    """Menghitung basis pangkat eksponen.

    Parameters:
        basis (float): Bilangan basis
        eksponen (int): Bilangan pangkat

    Returns:
        float: Hasil basis^eksponen
    """
    return basis ** eksponen

# Penggunaan library
print(f"5! = {faktorial(5)}")           # Output: 5! = 120
print(f"7 prima? {is_prima(7)}")        # Output: 7 prima? True
print(f"10 prima? {is_prima(10)}")      # Output: 10 prima? False
print(f"Fibonacci(8) = {fibonacci(8)}") # Output: Fibonacci(8) = [0, 1, 1, 2, 3, 5, 8, 13]
print(f"2^10 = {pangkat(2, 10)}")       # Output: 2^10 = 1024
```

---

## 5.8 Studi Kasus

### Studi Kasus 1: Kalkulator IPK Semester

```python
def input_matakuliah():
    """Meminta input data satu mata kuliah."""
    nama = input("Nama Mata Kuliah: ")
    sks = int(input("Jumlah SKS: "))
    nilai_huruf = input("Nilai Huruf (A/B/C/D/E): ").upper()
    return nama, sks, nilai_huruf

def konversi_nilai(huruf):
    """Mengkonversi nilai huruf ke angka (bobot).

    Skala: A=4, B=3, C=2, D=1, E=0
    """
    konversi = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "E": 0.0}
    return konversi.get(huruf, 0.0)

def hitung_ipk(daftar_mk):
    """Menghitung IPK dari daftar mata kuliah.

    IPK = Σ(SKS × Bobot) / Σ(SKS)

    Parameters:
        daftar_mk (list): List of tuples (nama, sks, nilai_huruf)

    Returns:
        tuple: (ipk, total_sks)
    """
    total_bobot = 0
    total_sks = 0

    for nama, sks, huruf in daftar_mk:
        bobot = konversi_nilai(huruf)
        total_bobot += sks * bobot
        total_sks += sks

    if total_sks == 0:
        return 0.0, 0

    ipk = total_bobot / total_sks
    return ipk, total_sks

def tampilkan_transkrip(daftar_mk, ipk, total_sks):
    """Menampilkan transkrip nilai lengkap."""
    print("\n" + "=" * 55)
    print("         TRANSKRIP NILAI SEMESTER")
    print("     Universitas Al Azhar Indonesia")
    print("=" * 55)
    print(f"{'No':<4}{'Mata Kuliah':<25}{'SKS':<6}{'Nilai':<8}{'Bobot':<6}")
    print("-" * 55)

    for i, (nama, sks, huruf) in enumerate(daftar_mk, 1):
        bobot = konversi_nilai(huruf)
        print(f"{i:<4}{nama:<25}{sks:<6}{huruf:<8}{bobot:<6.1f}")

    print("-" * 55)
    print(f"{'Total SKS:':<35}{total_sks}")
    print(f"{'IPK Semester:':<35}{ipk:.2f}")
    print("=" * 55)

def main():
    """Program utama kalkulator IPK."""
    print("=== KALKULATOR IPK SEMESTER ===\n")

    jumlah = int(input("Berapa mata kuliah? "))
    daftar_mk = []

    for i in range(jumlah):
        print(f"\n--- Mata Kuliah ke-{i + 1} ---")
        nama, sks, huruf = input_matakuliah()
        daftar_mk.append((nama, sks, huruf))

    ipk, total_sks = hitung_ipk(daftar_mk)
    tampilkan_transkrip(daftar_mk, ipk, total_sks)

main()
```

### Studi Kasus 2: Validasi Data dengan Fungsi

```python
def validasi_nim(nim):
    """Memvalidasi format NIM mahasiswa.

    Format valid: 10 digit angka, diawali '2024' (untuk angkatan 2024).
    Contoh: 2024040001

    Parameters:
        nim (str): NIM yang akan divalidasi

    Returns:
        tuple: (bool, str) — (valid/tidak, pesan)
    """
    if not nim.isdigit():
        return False, "NIM harus berisi angka saja"
    if len(nim) != 10:
        return False, "NIM harus 10 digit"
    if not nim.startswith("2024"):
        return False, "NIM harus diawali '2024'"
    return True, "NIM valid"

def validasi_nilai(nilai_str):
    """Memvalidasi input nilai (harus angka 0-100).

    Parameters:
        nilai_str (str): String yang akan divalidasi

    Returns:
        tuple: (bool, float/None, str) — (valid, nilai, pesan)
    """
    try:
        nilai = float(nilai_str)
    except ValueError:
        return False, None, "Input harus berupa angka"

    if nilai < 0 or nilai > 100:
        return False, None, "Nilai harus antara 0-100"

    return True, nilai, "Nilai valid"

def input_dengan_validasi(prompt, fungsi_validasi):
    """Input yang diulang sampai valid.

    Parameters:
        prompt (str): Pesan yang ditampilkan ke pengguna
        fungsi_validasi (function): Fungsi untuk memvalidasi input

    Returns:
        str: Input yang sudah valid
    """
    while True:
        data = input(prompt)
        hasil = fungsi_validasi(data)

        # Cek apakah valid (elemen pertama dari tuple)
        if hasil[0]:
            print(f"  ✓ {hasil[-1]}")
            return data
        else:
            print(f"  ✗ {hasil[-1]}. Silakan coba lagi.")

# Penggunaan
nim = input_dengan_validasi("Masukkan NIM: ", validasi_nim)
print(f"NIM yang dimasukkan: {nim}")
```

### Studi Kasus 3: Program Konversi Suhu Modular

```python
def celsius_ke_fahrenheit(celsius):
    """Konversi Celsius ke Fahrenheit: F = C × 9/5 + 32"""
    return celsius * 9 / 5 + 32

def celsius_ke_kelvin(celsius):
    """Konversi Celsius ke Kelvin: K = C + 273.15"""
    return celsius + 273.15

def fahrenheit_ke_celsius(fahrenheit):
    """Konversi Fahrenheit ke Celsius: C = (F - 32) × 5/9"""
    return (fahrenheit - 32) * 5 / 9

def fahrenheit_ke_kelvin(fahrenheit):
    """Konversi Fahrenheit ke Kelvin melalui Celsius."""
    celsius = fahrenheit_ke_celsius(fahrenheit)
    return celsius_ke_kelvin(celsius)

def kelvin_ke_celsius(kelvin):
    """Konversi Kelvin ke Celsius: C = K - 273.15"""
    return kelvin - 273.15

def kelvin_ke_fahrenheit(kelvin):
    """Konversi Kelvin ke Fahrenheit melalui Celsius."""
    celsius = kelvin_ke_celsius(kelvin)
    return celsius_ke_fahrenheit(celsius)

def tampilkan_menu():
    """Menampilkan menu konversi."""
    print("\n=== KONVERSI SUHU ===")
    print("1. Celsius    → Fahrenheit")
    print("2. Celsius    → Kelvin")
    print("3. Fahrenheit → Celsius")
    print("4. Fahrenheit → Kelvin")
    print("5. Kelvin     → Celsius")
    print("6. Kelvin     → Fahrenheit")
    print("0. Keluar")

def proses_konversi(pilihan, nilai):
    """Melakukan konversi berdasarkan pilihan menu.

    Returns:
        tuple: (hasil, satuan_asal, satuan_tujuan)
    """
    konversi = {
        "1": (celsius_ke_fahrenheit, "°C", "°F"),
        "2": (celsius_ke_kelvin, "°C", "K"),
        "3": (fahrenheit_ke_celsius, "°F", "°C"),
        "4": (fahrenheit_ke_kelvin, "°F", "K"),
        "5": (kelvin_ke_celsius, "K", "°C"),
        "6": (kelvin_ke_fahrenheit, "K", "°F"),
    }

    if pilihan in konversi:
        fungsi, satuan_asal, satuan_tujuan = konversi[pilihan]
        hasil = fungsi(nilai)
        return hasil, satuan_asal, satuan_tujuan
    return None, None, None

def main():
    """Program utama konversi suhu."""
    print("PROGRAM KONVERSI SUHU")
    print("Universitas Al Azhar Indonesia\n")

    while True:
        tampilkan_menu()
        pilihan = input("\nPilihan Anda: ")

        if pilihan == "0":
            print("Terima kasih! Sampai jumpa.")
            break

        if pilihan not in "123456" or len(pilihan) != 1:
            print("Pilihan tidak valid!")
            continue

        try:
            nilai = float(input("Masukkan suhu: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        hasil, satuan_asal, satuan_tujuan = proses_konversi(pilihan, nilai)
        if hasil is not None:
            print(f"\n  {nilai:.2f} {satuan_asal} = {hasil:.2f} {satuan_tujuan}")

main()
```

---

## 5.9 Kesalahan Umum dan Tips

### 5.9.1 Kesalahan Umum

**1. Lupa memanggil fungsi (hanya menyebutkan namanya):**

```python
def sapa():
    print("Halo!")

# SALAH — hanya mereferensikan fungsi, bukan memanggilnya
sapa       # Tidak terjadi apa-apa!

# BENAR — memanggil fungsi dengan tanda kurung
sapa()     # Output: Halo!
```

**2. Menggunakan `print` padahal seharusnya `return`:**

```python
# SALAH — fungsi ini "menampilkan" tapi tidak bisa digunakan lagi
def luas_segitiga_salah(alas, tinggi):
    print(0.5 * alas * tinggi)

hasil = luas_segitiga_salah(10, 5)  # Menampilkan 25.0
print(hasil * 2)  # ERROR: None * 2 tidak bisa!

# BENAR — fungsi ini mengembalikan nilai yang bisa diproses
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

hasil = luas_segitiga(10, 5)
print(hasil * 2)  # Output: 50.0
```

**3. Memodifikasi mutable default parameter:**

```python
# BAHAYA! Default parameter mutable dishare antar pemanggilan!
def tambah_item_salah(item, daftar=[]):
    daftar.append(item)
    return daftar

print(tambah_item_salah("apel"))     # Output: ['apel']
print(tambah_item_salah("jeruk"))    # Output: ['apel', 'jeruk'] — BUG!

# BENAR — gunakan None sebagai default
def tambah_item(item, daftar=None):
    if daftar is None:
        daftar = []
    daftar.append(item)
    return daftar

print(tambah_item("apel"))     # Output: ['apel']
print(tambah_item("jeruk"))    # Output: ['jeruk'] — Benar!
```

**4. Lupa `return` (fungsi mengembalikan `None`):**

```python
# SALAH — tidak ada return, hasilnya None
def hitung_diskon(harga, persen):
    diskon = harga * persen / 100
    harga_akhir = harga - diskon
    # Oops, lupa return!

hasil = hitung_diskon(100000, 20)
print(hasil)  # Output: None

# BENAR
def hitung_diskon(harga, persen):
    diskon = harga * persen / 100
    harga_akhir = harga - diskon
    return harga_akhir

hasil = hitung_diskon(100000, 20)
print(hasil)  # Output: 80000.0
```

### 5.9.2 Tips dan Best Practices

| Tips | Penjelasan |
|------|------------|
| Nama fungsi harus deskriptif | `hitung_luas_lingkaran()` lebih baik dari `hl()` |
| Satu fungsi, satu tugas | Jangan membuat fungsi yang melakukan terlalu banyak hal |
| Tulis docstring | Dokumentasikan parameter, return value, dan tujuan fungsi |
| Hindari variabel global | Gunakan parameter dan return value |
| Gunakan default parameter bijak | Jangan gunakan mutable object (list, dict) sebagai default |
| Batasi jumlah parameter | Jika lebih dari 4-5, pertimbangkan menggunakan dictionary |
| Test fungsi secara terpisah | Pastikan setiap fungsi bekerja dengan benar secara independen |

---

## 5.10 Latihan

### Latihan Mandiri

**Latihan 5.1 — Fungsi Dasar:**
Buatlah fungsi-fungsi berikut:
1. `luas_lingkaran(r)` — menghitung luas lingkaran
2. `keliling_lingkaran(r)` — menghitung keliling lingkaran
3. `volume_tabung(r, t)` — menghitung volume tabung (gunakan `luas_lingkaran`)

**Latihan 5.2 — Validasi dengan Fungsi:**
Buatlah fungsi `validasi_password(password)` yang mengembalikan `True` jika password memenuhi syarat:
- Minimal 8 karakter
- Mengandung minimal 1 huruf besar
- Mengandung minimal 1 huruf kecil
- Mengandung minimal 1 angka

**Latihan 5.3 — Dekomposisi:**
Buatlah program **Kalkulator Zakat Penghasilan** yang terdekomposisi menjadi fungsi-fungsi:
- `input_penghasilan()` — meminta input gaji bulanan
- `hitung_zakat_tahunan(gaji_bulanan)` — menghitung zakat jika penghasilan tahunan melebihi nisab (85 gram emas × harga emas saat ini), zakat = 2.5% dari penghasilan
- `tampilkan_hasil(gaji, zakat)` — menampilkan hasil perhitungan

**Latihan 5.4 — Library Fungsi:**
Buatlah kumpulan fungsi konversi satuan:
- `km_ke_mil(km)` dan `mil_ke_km(mil)`
- `kg_ke_pound(kg)` dan `pound_ke_kg(pound)`
- `celsius_ke_fahrenheit(c)` dan `fahrenheit_ke_celsius(f)`

### Latihan Kelompok

**Latihan 5.5 — Program Kuis Interaktif:**

Buatlah program kuis dengan fungsi-fungsi berikut:
- `buat_soal(pertanyaan, jawaban_benar)` — menyimpan soal
- `tampilkan_soal(nomor, soal)` — menampilkan soal ke layar
- `cek_jawaban(jawaban_user, jawaban_benar)` — mengecek jawaban
- `hitung_skor(benar, total)` — menghitung persentase skor
- `tampilkan_hasil_kuis(nama, skor, total)` — menampilkan hasil akhir

Program harus memiliki minimal 5 soal tentang materi Bab 1-4.

---

## 5.11 Rangkuman

| Konsep | Penjelasan |
|--------|------------|
| **Fungsi** | Blok kode bernama yang melakukan satu tugas tertentu dan dapat dipanggil berulang kali |
| **Parameter** | Variabel yang menerima input pada definisi fungsi |
| **Argumen** | Nilai yang dikirim saat memanggil fungsi |
| **Return value** | Nilai yang dikembalikan fungsi ke pemanggil |
| **Scope** | Ruang lingkup di mana variabel dapat diakses (local, enclosing, global, built-in) |
| **DRY** | Don't Repeat Yourself — hindari duplikasi kode |
| **Dekomposisi** | Memecah masalah besar menjadi sub-masalah yang lebih kecil |
| **Docstring** | Dokumentasi yang menjelaskan fungsi, parameter, dan return value |
| **Abstraksi** | Menyembunyikan detail implementasi, hanya menampilkan antarmuka |
| **Default parameter** | Parameter yang memiliki nilai bawaan jika tidak diisi |
| **`*args` / `**kwargs`** | Menerima jumlah argumen tidak tentu |

**Peta Konsep Bab 5:**

```
                    ┌──────────────┐
                    │    FUNGSI    │
                    └──────┬───────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
    ┌─────▼─────┐   ┌─────▼─────┐   ┌──────▼──────┐
    │ Definisi  │   │  Scope    │   │  Prinsip    │
    │ & Sintaks │   │           │   │  Desain     │
    └─────┬─────┘   └─────┬─────┘   └──────┬──────┘
          │               │                │
     ┌────┼────┐     ┌────┼────┐      ┌────┼────┐
     │    │    │     │    │    │      │    │    │
    def param return L   E   G     DRY SRP Abstraksi
         │              │    │
       positional    enclosing global
       default       (nested)
       *args/**kwargs
```

---

## Referensi

1. Downey, A. (2015). *Think Python: How to Think Like a Computer Scientist*. 2nd Edition. O'Reilly Media. — Chapter 3: Functions
2. Matthes, E. (2023). *Python Crash Course*. 3rd Edition. No Starch Press. — Chapter 8: Functions
3. Dokumentasi Python: [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
4. Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. — Chapter 3: Functions

---

*Bab selanjutnya: **Bab 6 — String dan Pengolahan Teks** — Anda akan belajar memanipulasi teks menggunakan fungsi-fungsi string bawaan Python, serta mengkombinasikannya dengan fungsi yang Anda buat sendiri.*
