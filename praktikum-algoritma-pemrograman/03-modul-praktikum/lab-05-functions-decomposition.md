# Lab 05: Functions dan Decomposition

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Durasi** | 75 menit |
| **Prasyarat** | Lab 04 — Loops dan Patterns |

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:
- Mendefinisikan fungsi dengan `def`, parameter, dan `return`
- Menggunakan parameter default dan memahami *scope* variabel
- Menulis dokumentasi fungsi dengan *docstring*
- Melakukan refactoring kode prosedural menjadi fungsi-fungsi modular

---

## Persiapan

1. Buka Google Colab dan buat notebook baru
2. Beri nama `Lab05_NamaAnda_NIM.ipynb`
3. Pastikan Anda telah memahami loop dan conditional

---

## Langkah-langkah

### Langkah 1 — Mendefinisikan Fungsi Pertama

```python
# Fungsi sederhana tanpa parameter
def salam():
    print("Assalamualaikum Warahmatullahi Wabarakatuh")
    print("Selamat datang di program kami!")

# Memanggil fungsi
salam()
print("---")
salam()  # fungsi bisa dipanggil berulang kali
```

**Penjelasan:**
- `def` digunakan untuk mendefinisikan fungsi
- Nama fungsi mengikuti aturan penamaan variabel
- Blok kode di dalam fungsi diindentasi
- Fungsi baru dijalankan saat **dipanggil**

### Langkah 2 — Fungsi dengan Parameter dan Return

```python
# Fungsi dengan parameter
def hitung_luas_persegi(sisi):
    """Menghitung luas persegi."""
    luas = sisi ** 2
    return luas

def hitung_luas_lingkaran(jari_jari):
    """Menghitung luas lingkaran."""
    pi = 3.14159
    luas = pi * jari_jari ** 2
    return luas

def hitung_luas_segitiga(alas, tinggi):
    """Menghitung luas segitiga."""
    return 0.5 * alas * tinggi

# Menggunakan fungsi
s = 7
print(f"Luas persegi (sisi={s})       : {hitung_luas_persegi(s):.2f}")
print(f"Luas lingkaran (r={5})        : {hitung_luas_lingkaran(5):.2f}")
print(f"Luas segitiga (a=10, t=6)     : {hitung_luas_segitiga(10, 6):.2f}")
```

### Langkah 3 — Parameter Default

```python
# Fungsi dengan parameter default
def hitung_harga(harga, jumlah=1, diskon_persen=0):
    """
    Menghitung total harga setelah diskon.

    Parameters:
        harga (float): Harga satuan barang
        jumlah (int): Jumlah barang (default: 1)
        diskon_persen (float): Persentase diskon (default: 0)

    Returns:
        float: Total harga setelah diskon
    """
    subtotal = harga * jumlah
    diskon = subtotal * diskon_persen / 100
    total = subtotal - diskon
    return total

# Berbagai cara memanggil fungsi
print(f"1 buku Rp25.000               : Rp{hitung_harga(25000):,.0f}")
print(f"3 buku Rp25.000               : Rp{hitung_harga(25000, 3):,.0f}")
print(f"3 buku Rp25.000, diskon 10%   : Rp{hitung_harga(25000, 3, 10):,.0f}")
print(f"5 buku Rp25.000, diskon 15%   : Rp{hitung_harga(25000, jumlah=5, diskon_persen=15):,.0f}")
```

### Langkah 4 — Scope (Lingkup Variabel)

```python
# Demonstrasi scope variabel
pesan_global = "Saya variabel global"

def demonstrasi_scope():
    pesan_lokal = "Saya variabel lokal"
    print(f"  Di dalam fungsi - global : {pesan_global}")
    print(f"  Di dalam fungsi - lokal  : {pesan_lokal}")

demonstrasi_scope()
print(f"Di luar fungsi - global    : {pesan_global}")

# Baris berikut akan ERROR jika di-uncomment:
# print(pesan_lokal)  # NameError: pesan_lokal tidak terdefinisi di luar fungsi

# Variabel lokal vs global dengan nama sama
x = 100  # global

def ubah_x():
    x = 50  # ini variabel LOKAL baru, bukan yang global
    print(f"  x di dalam fungsi: {x}")

ubah_x()
print(f"x di luar fungsi: {x}")  # tetap 100
```

### Langkah 5 — Docstring dan Fungsi dengan Multiple Return

```python
def analisis_bilangan(n):
    """
    Menganalisis sebuah bilangan bulat.

    Parameters:
        n (int): Bilangan yang akan dianalisis

    Returns:
        tuple: (genap_ganjil, positif_negatif, prima)
    """
    # Cek genap/ganjil
    genap_ganjil = "Genap" if n % 2 == 0 else "Ganjil"

    # Cek positif/negatif/nol
    if n > 0:
        positif_negatif = "Positif"
    elif n < 0:
        positif_negatif = "Negatif"
    else:
        positif_negatif = "Nol"

    # Cek prima
    if n < 2:
        prima = False
    else:
        prima = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                prima = False
                break

    return genap_ganjil, positif_negatif, prima

# Menggunakan fungsi
bilangan = int(input("Masukkan bilangan: "))
gg, pn, pr = analisis_bilangan(bilangan)

print(f"\nAnalisis bilangan {bilangan}:")
print(f"  Genap/Ganjil    : {gg}")
print(f"  Positif/Negatif : {pn}")
print(f"  Bilangan Prima  : {'Ya' if pr else 'Tidak'}")

# Menampilkan docstring
print(f"\nDokumentasi fungsi:\n{analisis_bilangan.__doc__}")
```

### Langkah 6 — Latihan Refactoring

Berikut adalah kode *spaghetti* yang perlu di-refactor menjadi fungsi-fungsi terpisah:

**Kode SEBELUM refactoring (jangan dijalankan, hanya untuk dibaca):**
```python
# KODE SPAGHETTI - JANGAN DITIRU
# nama = input("Nama: ")
# n1 = float(input("Nilai 1: "))
# n2 = float(input("Nilai 2: "))
# n3 = float(input("Nilai 3: "))
# rata = (n1+n2+n3)/3
# if rata >= 85: h = "A"
# elif rata >= 70: h = "B"
# elif rata >= 55: h = "C"
# else: h = "D"
# if h in ["A","B","C"]: s = "LULUS"
# else: s = "TIDAK LULUS"
# print("Nama:", nama, "Rata-rata:", rata, "Huruf:", h, "Status:", s)
```

**Kode SETELAH refactoring:**
```python
def input_data_siswa():
    """Mengambil input data siswa dari pengguna."""
    nama = input("Nama siswa: ")
    nilai1 = float(input("Nilai ke-1: "))
    nilai2 = float(input("Nilai ke-2: "))
    nilai3 = float(input("Nilai ke-3: "))
    return nama, nilai1, nilai2, nilai3

def hitung_rata_rata(n1, n2, n3):
    """Menghitung rata-rata dari tiga nilai."""
    return (n1 + n2 + n3) / 3

def konversi_ke_huruf(rata_rata):
    """Mengonversi nilai rata-rata ke nilai huruf."""
    if rata_rata >= 85:
        return "A"
    elif rata_rata >= 70:
        return "B"
    elif rata_rata >= 55:
        return "C"
    else:
        return "D"

def tentukan_status(huruf):
    """Menentukan status kelulusan berdasarkan nilai huruf."""
    if huruf in ["A", "B", "C"]:
        return "LULUS"
    return "TIDAK LULUS"

def tampilkan_hasil(nama, rata_rata, huruf, status):
    """Menampilkan hasil evaluasi dalam format tabel."""
    print(f"\n{'=' * 35}")
    print(f"  HASIL EVALUASI SISWA")
    print(f"{'=' * 35}")
    print(f"  Nama        : {nama}")
    print(f"  Rata-rata   : {rata_rata:.2f}")
    print(f"  Nilai Huruf : {huruf}")
    print(f"  Status      : {status}")
    print(f"{'=' * 35}")

# Program utama — bersih dan mudah dibaca
nama, n1, n2, n3 = input_data_siswa()
rata = hitung_rata_rata(n1, n2, n3)
huruf = konversi_ke_huruf(rata)
status = tentukan_status(huruf)
tampilkan_hasil(nama, rata, huruf, status)
```

### Langkah 7 — Mini Project: Sistem Kalkulator Modular

```python
# =============================================
# MINI PROJECT: Sistem Kalkulator Modular
# =============================================

def tambah(a, b):
    """Menjumlahkan dua bilangan."""
    return a + b

def kurang(a, b):
    """Mengurangkan dua bilangan."""
    return a - b

def kali(a, b):
    """Mengalikan dua bilangan."""
    return a * b

def bagi(a, b):
    """Membagi dua bilangan dengan pengecekan pembagian nol."""
    if b == 0:
        return "Error: Pembagian dengan nol!"
    return a / b

def pangkat(a, b):
    """Menghitung a pangkat b."""
    return a ** b

def modulus(a, b):
    """Menghitung sisa pembagian a mod b."""
    if b == 0:
        return "Error: Pembagian dengan nol!"
    return a % b

def tampilkan_menu():
    """Menampilkan menu utama kalkulator."""
    print("\n" + "=" * 35)
    print("   KALKULATOR MODULAR")
    print("=" * 35)
    print("  1. Penjumlahan (+)")
    print("  2. Pengurangan (-)")
    print("  3. Perkalian   (x)")
    print("  4. Pembagian   (/)")
    print("  5. Pangkat     (^)")
    print("  6. Modulus     (%)")
    print("  0. Keluar")
    print("-" * 35)

def input_dua_bilangan():
    """Meminta input dua bilangan dari pengguna."""
    a = float(input("Bilangan pertama : "))
    b = float(input("Bilangan kedua   : "))
    return a, b

def proses_operasi(pilihan, a, b):
    """Memproses operasi berdasarkan pilihan menu."""
    operasi = {
        "1": ("Penjumlahan", "+", tambah),
        "2": ("Pengurangan", "-", kurang),
        "3": ("Perkalian", "x", kali),
        "4": ("Pembagian", "/", bagi),
        "5": ("Pangkat", "^", pangkat),
        "6": ("Modulus", "%", modulus),
    }

    if pilihan in operasi:
        nama_op, simbol, fungsi = operasi[pilihan]
        hasil = fungsi(a, b)
        print(f"\n  {nama_op}: {a} {simbol} {b} = {hasil}")
    else:
        print("  Pilihan tidak valid!")

# === Program Utama ===
print("Selamat datang di Kalkulator Modular!")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (0-6): ")

    if pilihan == "0":
        print("\nTerima kasih! Sampai jumpa.")
        break

    if pilihan in ["1", "2", "3", "4", "5", "6"]:
        a, b = input_dua_bilangan()
        proses_operasi(pilihan, a, b)
    else:
        print("Menu tidak valid, silakan coba lagi.")
```

---

## Tantangan Tambahan

1. **Kalkulator Konversi Satuan**: Tambahkan modul konversi satuan ke kalkulator (suhu, panjang, berat). Setiap konversi adalah fungsi terpisah.

2. **Fungsi Rekursif Faktorial dan Fibonacci**: Buat fungsi rekursif untuk menghitung faktorial (`n!`) dan bilangan Fibonacci ke-n. Bandingkan hasilnya dengan versi iteratif (loop).

3. **Sistem Login Sederhana**: Buat program dengan fungsi `daftar_akun()`, `login()`, dan `tampilkan_profil()`. Simpan data akun dalam dictionary. Program berjalan dalam loop menu utama.

---

## Checklist Penyelesaian

- [ ] Mampu mendefinisikan dan memanggil fungsi
- [ ] Mampu menggunakan parameter, return, dan parameter default
- [ ] Memahami perbedaan scope lokal dan global
- [ ] Mampu menulis docstring pada fungsi
- [ ] Menyelesaikan latihan refactoring (spaghetti code menjadi modular)
- [ ] Menyelesaikan Mini Project: Sistem Kalkulator Modular
- [ ] Mengerjakan minimal 1 tantangan tambahan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
