# BAB 5: FUNGSI DAN MODULARITAS

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| CPMK-4.1 | Mendefinisikan fungsi dengan parameter dan return value | C3 (Menerapkan) |
| CPMK-4.2 | Menerapkan prinsip DRY dan dekomposisi top-down | C3 (Menerapkan) |
| CPMK-4.3 | Menjelaskan konsep scope (local vs global) | C2 (Memahami) |
| CPMK-4.4 | Menggunakan docstring dan dokumentasi fungsi | C3 (Menerapkan) |

**Estimasi Waktu:** 3 × 50 menit (3 SKS)

**Prasyarat:** Mahasiswa telah memahami materi Bab 1–4 (variabel, tipe data, seleksi, perulangan).

---

## 5.1 Apa Itu Fungsi?

### 5.1.1 Definisi dan Analogi

**Fungsi** dalam pemrograman adalah blok kode yang diberi nama, melakukan tugas tertentu, dan dapat dipanggil berulang kali kapan pun dibutuhkan.

**Analogi: Fungsi = Resep Masakan**

Bayangkan Anda seorang koki di restoran Padang. Setiap hari, Anda memasak rendang, gulai, dan sambal. Alih-alih mengingat langkah-langkah dari awal setiap kali, Anda memiliki **resep** (fungsi) yang tinggal diikuti:

```
┌─────────────────────────────────────────────────────┐
│  RESEP RENDANG (= fungsi)                           │
│                                                     │
│  Bahan (= parameter):                               │
│    - daging 1 kg                                     │
│    - santan 1 liter                                  │
│    - bumbu halus                                     │
│                                                     │
│  Langkah-langkah (= body fungsi):                   │
│    1. Panaskan santan                                │
│    2. Tumis bumbu                                    │
│    3. Masukkan daging                                │
│    4. Masak hingga kering                            │
│                                                     │
│  Hasil (= return value):                             │
│    → Rendang siap saji                               │
└─────────────────────────────────────────────────────┘
```

Kunci dari analogi ini:
- **Nama resep** = nama fungsi → agar bisa dipanggil kapan saja
- **Bahan** = parameter → input yang dibutuhkan
- **Langkah** = body fungsi → proses yang dilakukan
- **Hasil** = return value → output yang dikembalikan

### 5.1.2 Mengapa Fungsi Penting?

```
┌─────────────────────────────────────────────────────────────┐
│              4 ALASAN FUNGSI PENTING                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. MODULARITY (Modularitas)                                │
│     Program dipecah menjadi bagian-bagian kecil             │
│     yang mudah dikelola dan dipahami                        │
│                                                             │
│  2. REUSABILITY (Dapat Digunakan Ulang)                     │
│     Tulis sekali, panggil berkali-kali                      │
│     Tidak perlu copy-paste kode yang sama                   │
│                                                             │
│  3. READABILITY (Keterbacaan)                               │
│     Program utama menjadi ringkas dan jelas                 │
│     hitung_total() lebih mudah dibaca dari 20 baris kode    │
│                                                             │
│  4. MAINTAINABILITY (Kemudahan Pemeliharaan)                │
│     Jika ada bug, cukup perbaiki di satu fungsi             │
│     Perubahan otomatis berlaku di semua pemanggilan          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Contoh tanpa fungsi (kode "spageti"):**
```python
# Menghitung luas persegi panjang — 3 kali copy-paste!
panjang1 = 10
lebar1 = 5
luas1 = panjang1 * lebar1
print(f"Luas 1: {luas1}")

panjang2 = 7
lebar2 = 3
luas2 = panjang2 * lebar2
print(f"Luas 2: {luas2}")

panjang3 = 15
lebar3 = 8
luas3 = panjang3 * lebar3
print(f"Luas 3: {luas3}")
```

**Contoh dengan fungsi (clean code):**
```python
def hitung_luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang."""
    return panjang * lebar

# Panggil 3 kali — ringkas dan jelas!
print(f"Luas 1: {hitung_luas_persegi_panjang(10, 5)}")
print(f"Luas 2: {hitung_luas_persegi_panjang(7, 3)}")
print(f"Luas 3: {hitung_luas_persegi_panjang(15, 8)}")
```

### 5.1.3 Fungsi Built-in Python

Python sudah menyediakan banyak fungsi bawaan yang sering kita gunakan:

| Fungsi | Deskripsi | Contoh |
|--------|-----------|--------|
| `print()` | Menampilkan output ke layar | `print("Halo")` |
| `input()` | Menerima input dari pengguna | `nama = input("Nama: ")` |
| `len()` | Menghitung panjang | `len("Python")` → 6 |
| `type()` | Mengetahui tipe data | `type(42)` → `<class 'int'>` |
| `int()` | Konversi ke integer | `int("10")` → 10 |
| `float()` | Konversi ke float | `float("3.14")` → 3.14 |
| `str()` | Konversi ke string | `str(42)` → "42" |
| `range()` | Menghasilkan urutan angka | `range(1, 6)` → 1,2,3,4,5 |
| `abs()` | Nilai absolut | `abs(-5)` → 5 |
| `round()` | Pembulatan | `round(3.7)` → 4 |
| `max()` | Nilai terbesar | `max(3, 7, 1)` → 7 |
| `min()` | Nilai terkecil | `min(3, 7, 1)` → 1 |
| `sum()` | Total penjumlahan | `sum([1,2,3])` → 6 |
| `sorted()` | Mengurutkan | `sorted([3,1,2])` → [1,2,3] |

> **Catatan:** Semua fungsi built-in ini dibuat oleh developer Python. Di bab ini, kita akan belajar **membuat fungsi sendiri** (user-defined functions).

---

## 5.2 Mendefinisikan Fungsi (`def`)

### 5.2.1 Sintaks Dasar

```python
def nama_fungsi(parameter1, parameter2, ...):
    """Docstring: penjelasan singkat fungsi."""
    # Body fungsi — kode yang dijalankan
    # ...
    return nilai_kembali  # opsional
```

```
┌─────────────────────────────────────────────────────────────┐
│                    ANATOMI FUNGSI PYTHON                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  def hitung_diskon(harga, persen_diskon):                   │
│  ▲   ▲              ▲                                       │
│  │   │              └── Parameter (input)                   │
│  │   └── Nama fungsi (snake_case)                           │
│  └── Keyword 'def' (define)                                 │
│                                                             │
│      """Menghitung harga setelah diskon."""  ← Docstring    │
│      potongan = harga * persen_diskon / 100 ← Body         │
│      harga_akhir = harga - potongan         ← Body         │
│      return harga_akhir                     ← Return value │
│             ▲                                               │
│             └── Nilai yang dikembalikan ke pemanggil        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 5.2.2 Fungsi Tanpa Parameter

Fungsi paling sederhana: tidak menerima input dan tidak mengembalikan nilai.

```python
def salam():
    """Menampilkan salam pembuka."""
    print("Assalamu'alaikum Warahmatullahi Wabarakatuh")
    print("Selamat datang di Sistem Informasi Mahasiswa")
    print("Universitas Al Azhar Indonesia")
    print("-" * 45)

# Panggil fungsi
salam()
salam()  # bisa dipanggil berulang kali
```

### 5.2.3 Fungsi Dengan Parameter

Parameter membuat fungsi lebih fleksibel — bisa menerima input yang berbeda-beda.

```python
def salam_personal(nama, prodi):
    """Menampilkan salam personal kepada mahasiswa."""
    print(f"Assalamu'alaikum, {nama}!")
    print(f"Selamat datang di Program Studi {prodi}")

# Panggil dengan argumen berbeda
salam_personal("Ahmad", "Informatika")
salam_personal("Fatimah", "Sistem Informasi")
```

**Perbedaan Parameter vs Argumen:**
- **Parameter**: variabel di definisi fungsi → `nama`, `prodi`
- **Argumen**: nilai aktual saat pemanggilan → `"Ahmad"`, `"Informatika"`

### 5.2.4 Fungsi Dengan Return Value

`return` mengembalikan nilai dari fungsi ke pemanggil.

```python
def hitung_ipk(total_mutu, total_sks):
    """
    Menghitung IPK mahasiswa.

    Parameters:
        total_mutu (float): Total nilai mutu (bobot × sks)
        total_sks (int): Total SKS yang ditempuh

    Returns:
        float: IPK (0.00 - 4.00)
    """
    if total_sks == 0:
        return 0.0
    ipk = total_mutu / total_sks
    return round(ipk, 2)

# Panggil dan simpan hasil
ipk_ahmad = hitung_ipk(135.5, 40)
print(f"IPK Ahmad: {ipk_ahmad}")  # IPK Ahmad: 3.39

ipk_siti = hitung_ipk(148.0, 40)
print(f"IPK Siti: {ipk_siti}")    # IPK Siti: 3.70
```

> **Penting:** Ketika fungsi mencapai `return`, eksekusi fungsi **langsung berhenti**. Kode setelah `return` tidak akan dijalankan.

```python
def cek_kelulusan(ipk):
    """Menentukan status kelulusan berdasarkan IPK."""
    if ipk >= 3.5:
        return "Cum Laude"
    elif ipk >= 3.0:
        return "Sangat Memuaskan"
    elif ipk >= 2.5:
        return "Memuaskan"
    elif ipk >= 2.0:
        return "Cukup"
    else:
        return "Tidak Lulus"
    # Kode di sini TIDAK AKAN dijalankan
    print("Ini tidak akan pernah tampil")

print(cek_kelulusan(3.7))  # Cum Laude
print(cek_kelulusan(2.3))  # Cukup
```

### 5.2.5 Multiple Return Values

Python memungkinkan fungsi mengembalikan lebih dari satu nilai menggunakan tuple:

```python
def statistik_nilai(daftar_nilai):
    """
    Menghitung statistik dasar dari daftar nilai.

    Returns:
        tuple: (rata_rata, nilai_min, nilai_max)
    """
    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    nilai_min = min(daftar_nilai)
    nilai_max = max(daftar_nilai)
    return rata_rata, nilai_min, nilai_max

# Panggil dan unpack hasilnya
nilai = [85, 92, 78, 95, 88, 76, 91]
rata, minimum, maksimum = statistik_nilai(nilai)

print(f"Rata-rata: {rata:.2f}")  # Rata-rata: 86.43
print(f"Minimum  : {minimum}")   # Minimum  : 76
print(f"Maksimum : {maksimum}")  # Maksimum : 95
```

---

## 5.3 Parameter dan Argumen

### 5.3.1 Positional Arguments

Argumen dicocokkan berdasarkan **posisi** (urutan).

```python
def buat_biodata(nama, umur, kota):
    """Membuat string biodata."""
    return f"{nama}, {umur} tahun, dari {kota}"

# Urutan harus sesuai!
print(buat_biodata("Ahmad", 19, "Jakarta"))
# Output: Ahmad, 19 tahun, dari Jakarta

# Salah urutan → hasil aneh:
print(buat_biodata(19, "Jakarta", "Ahmad"))
# Output: 19, Jakarta tahun, dari Ahmad  ← SALAH!
```

### 5.3.2 Keyword Arguments

Argumen dicocokkan berdasarkan **nama parameter**.

```python
# Urutan bebas jika pakai keyword arguments
print(buat_biodata(kota="Bandung", nama="Siti", umur=20))
# Output: Siti, 20 tahun, dari Bandung

# Bisa campur: positional dulu, lalu keyword
print(buat_biodata("Budi", kota="Surabaya", umur=21))
# Output: Budi, 21 tahun, dari Surabaya
```

### 5.3.3 Default Parameters

Memberikan nilai default pada parameter — jika tidak diisi, nilai default yang dipakai.

```python
def hitung_harga(harga_satuan, jumlah, diskon=0):
    """
    Menghitung total harga dengan diskon opsional.

    Parameters:
        harga_satuan (int): Harga per item dalam Rupiah
        jumlah (int): Jumlah item
        diskon (float): Persentase diskon (default: 0)

    Returns:
        int: Total harga setelah diskon
    """
    subtotal = harga_satuan * jumlah
    potongan = subtotal * diskon / 100
    return int(subtotal - potongan)

# Tanpa diskon (default=0)
print(hitung_harga(15000, 3))          # 45000

# Dengan diskon 10%
print(hitung_harga(15000, 3, 10))      # 40500

# Dengan keyword argument
print(hitung_harga(15000, 3, diskon=20))  # 36000
```

> **Aturan:** Parameter dengan default value HARUS diletakkan **setelah** parameter tanpa default.
> ```python
> def fungsi(a, b, c=10):    # ✓ Benar
> def fungsi(a, b=10, c):    # ✗ SyntaxError!
> ```

### 5.3.4 *args dan **kwargs (Pengenalan)

Untuk menerima **jumlah argumen yang tidak tetap**:

```python
def hitung_total(*harga_barang):
    """Menghitung total dari sejumlah harga barang."""
    total = sum(harga_barang)
    return total

# Bisa dipanggil dengan berapapun argumen
print(hitung_total(15000, 25000))                    # 40000
print(hitung_total(15000, 25000, 8000))              # 48000
print(hitung_total(15000, 25000, 8000, 32000, 5000)) # 85000
```

```python
def cetak_info(**info):
    """Mencetak informasi dalam format key-value."""
    for kunci, nilai in info.items():
        print(f"  {kunci}: {nilai}")

cetak_info(nama="Ahmad", nim="2025001", prodi="Informatika")
# Output:
#   nama: Ahmad
#   nim: 2025001
#   prodi: Informatika
```

> **Catatan:** `*args` dan `**kwargs` adalah fitur lanjutan. Untuk mata kuliah ini, cukup memahami konsep dasarnya. Anda akan memperdalam ini di mata kuliah lanjutan.

---

## 5.4 Scope: Variabel Lokal vs Global

### 5.4.1 Local Scope

Variabel yang didefinisikan **di dalam fungsi** hanya bisa diakses di dalam fungsi tersebut:

```python
def hitung_luas():
    panjang = 10  # variabel lokal
    lebar = 5     # variabel lokal
    luas = panjang * lebar
    print(f"Di dalam fungsi: luas = {luas}")

hitung_luas()
# print(panjang)  # ERROR! NameError: name 'panjang' is not defined
```

### 5.4.2 Global Scope

Variabel yang didefinisikan **di luar fungsi** bisa diakses dari mana saja:

```python
nama_universitas = "Universitas Al Azhar Indonesia"  # variabel global

def tampilkan_info():
    print(f"Universitas: {nama_universitas}")  # bisa akses global

tampilkan_info()  # Output: Universitas: Universitas Al Azhar Indonesia
print(nama_universitas)  # Juga bisa diakses di luar fungsi
```

> **Penting:** Fungsi bisa **membaca** variabel global, tetapi tidak bisa **mengubah** variabel global secara langsung (kecuali menggunakan keyword `global`, yang **tidak disarankan**).

```python
counter = 0

def tambah_counter():
    # counter += 1  # ERROR! UnboundLocalError
    # Gunakan parameter dan return sebagai gantinya:
    pass

# Cara yang BENAR:
def tambah(nilai):
    """Menambahkan 1 ke nilai."""
    return nilai + 1

counter = tambah(counter)
print(counter)  # 1
```

### 5.4.3 Aturan LEGB

Python mencari variabel menggunakan aturan **LEGB** (dari dalam ke luar):

```
┌─────────────────────────────────────────────────┐
│  B — Built-in                                    │
│  ┌─────────────────────────────────────────────┐ │
│  │  G — Global                                  │ │
│  │  ┌─────────────────────────────────────────┐ │ │
│  │  │  E — Enclosing (fungsi pembungkus)      │ │ │
│  │  │  ┌─────────────────────────────────────┐ │ │ │
│  │  │  │  L — Local (fungsi saat ini)        │ │ │ │
│  │  │  │                                     │ │ │ │
│  │  │  │  Python mencari dari SINI dulu      │ │ │ │
│  │  │  └─────────────────────────────────────┘ │ │ │
│  │  └─────────────────────────────────────────┘ │ │
│  └─────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
```

| Level | Penjelasan | Contoh |
|-------|-----------|--------|
| **L** (Local) | Variabel di dalam fungsi saat ini | `x = 10` di dalam `def f():` |
| **E** (Enclosing) | Variabel di fungsi pembungkus (nested function) | Fungsi di dalam fungsi |
| **G** (Global) | Variabel di level modul/file | `x = 10` di luar semua fungsi |
| **B** (Built-in) | Nama bawaan Python | `print`, `len`, `range` |

```python
x = "global"  # G

def fungsi_luar():
    x = "enclosing"  # E

    def fungsi_dalam():
        x = "local"  # L
        print(x)  # Menampilkan "local" (L ditemukan dulu)

    fungsi_dalam()
    print(x)  # Menampilkan "enclosing" (E)

fungsi_luar()
print(x)  # Menampilkan "global" (G)
```

> **Best Practice:** Hindari penggunaan variabel global. Gunakan **parameter** untuk memasukkan data ke fungsi dan **return** untuk mengeluarkan hasil. Ini membuat kode lebih mudah dipahami dan di-debug.

---

## 5.5 Desain Top-Down dan Dekomposisi

### 5.5.1 Prinsip DRY (Don't Repeat Yourself)

**DRY** adalah salah satu prinsip terpenting dalam pemrograman:

> *"Every piece of knowledge must have a single, unambiguous, authoritative representation within a system."*

**Contoh pelanggaran DRY:**
```python
# Kode TIDAK DRY — menghitung diskon berulang kali
harga1 = 100000
diskon1 = harga1 * 10 / 100
total1 = harga1 - diskon1
print(f"Total 1: Rp {total1:,.0f}")

harga2 = 250000
diskon2 = harga2 * 10 / 100
total2 = harga2 - diskon2
print(f"Total 2: Rp {total2:,.0f}")

harga3 = 75000
diskon3 = harga3 * 10 / 100
total3 = harga3 - diskon3
print(f"Total 3: Rp {total3:,.0f}")
```

**Contoh DRY:**
```python
def hitung_setelah_diskon(harga, persen=10):
    """Menghitung harga setelah diskon."""
    potongan = harga * persen / 100
    return harga - potongan

# Ringkas, jelas, dan mudah diubah!
for harga in [100000, 250000, 75000]:
    total = hitung_setelah_diskon(harga)
    print(f"Harga: Rp {harga:>10,.0f} → Total: Rp {total:>10,.0f}")
```

### 5.5.2 Diagram Top-Down Design

**Top-down design** adalah pendekatan memecah program besar menjadi fungsi-fungsi kecil, dari yang paling umum (atas) ke yang paling spesifik (bawah):

```
                    ┌────────────────────┐
                    │   PROGRAM UTAMA    │
                    │   (main)           │
                    └────────┬───────────┘
                             │
            ┌────────────────┼─────────────────┐
            │                │                 │
     ┌──────▼──────┐  ┌─────▼──────┐  ┌──────▼──────┐
     │   INPUT     │  │  PROSES    │  │   OUTPUT    │
     │  (baca_data)│  │(hitung)    │  │(tampilkan)  │
     └──────┬──────┘  └─────┬──────┘  └──────┬──────┘
            │               │                │
       ┌────▼────┐     ┌────▼─────┐    ┌─────▼─────┐
       │validasi │     │hitung_   │    │cetak_     │
       │_input() │     │subtotal()│    │struk()    │
       └─────────┘     │hitung_   │    │cetak_     │
                       │diskon()  │    │ringkasan()│
                       │hitung_   │    └───────────┘
                       │pajak()   │
                       └──────────┘
```

### 5.5.3 Studi Kasus: Refactoring Program Kalkulator

**SEBELUM (kode spageti tanpa fungsi):**

```python
print("=== KALKULATOR SEDERHANA ===")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
pilihan = input("Pilih operasi (1-4): ")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
if pilihan == "1":
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
elif pilihan == "2":
    hasil = angka1 - angka2
    print(f"{angka1} - {angka2} = {hasil}")
elif pilihan == "3":
    hasil = angka1 * angka2
    print(f"{angka1} * {angka2} = {hasil}")
elif pilihan == "4":
    if angka2 == 0:
        print("Error: Tidak bisa membagi dengan nol!")
    else:
        hasil = angka1 / angka2
        print(f"{angka1} / {angka2} = {hasil}")
else:
    print("Pilihan tidak valid!")
```

**SESUDAH (modular dengan fungsi):**

```python
def tampilkan_menu():
    """Menampilkan menu operasi kalkulator."""
    print("\n=== KALKULATOR SEDERHANA ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

def baca_angka(prompt):
    """Membaca dan memvalidasi input angka dari pengguna."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Masukkan angka yang valid!")

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
    """Membagi dua bilangan dengan validasi pembagian nol."""
    if b == 0:
        return None  # tidak bisa bagi nol
    return a / b

def jalankan_kalkulator():
    """Fungsi utama yang menjalankan loop kalkulator."""
    operasi = {
        "1": ("+", tambah),
        "2": ("-", kurang),
        "3": ("*", kali),
        "4": ("/", bagi),
    }

    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi (1-5): ").strip()

        if pilihan == "5":
            print("Terima kasih! Sampai jumpa.")
            break

        if pilihan not in operasi:
            print("Pilihan tidak valid!")
            continue

        simbol, fungsi_operasi = operasi[pilihan]
        a = baca_angka("Masukkan angka pertama : ")
        b = baca_angka("Masukkan angka kedua   : ")

        hasil = fungsi_operasi(a, b)

        if hasil is None:
            print("Error: Tidak bisa membagi dengan nol!")
        else:
            print(f"\n  {a} {simbol} {b} = {hasil}")

# Jalankan program
jalankan_kalkulator()
```

**Perbandingan:**

| Aspek | Sebelum | Sesudah |
|-------|---------|---------|
| Jumlah fungsi | 0 | 7 |
| Kemudahan dibaca | Sulit | Mudah |
| Menambah operasi baru | Ubah banyak kode | Tambah 1 fungsi + 1 baris di dict |
| Validasi input | Tidak ada | Ada (baca_angka) |
| Loop (ulang tanpa restart) | Tidak | Ya |

---

## 5.6 Dokumentasi Fungsi

### 5.6.1 Docstrings

**Docstring** adalah string dokumentasi yang ditulis tepat di baris pertama body fungsi:

```python
def hitung_bmi(berat_kg, tinggi_cm):
    """
    Menghitung Body Mass Index (BMI).

    Parameters:
        berat_kg (float): Berat badan dalam kilogram
        tinggi_cm (float): Tinggi badan dalam sentimeter

    Returns:
        float: Nilai BMI

    Example:
        >>> hitung_bmi(70, 175)
        22.86
    """
    tinggi_m = tinggi_cm / 100
    bmi = berat_kg / (tinggi_m ** 2)
    return round(bmi, 2)

# Docstring bisa diakses dengan help()
help(hitung_bmi)

# Atau dengan __doc__
print(hitung_bmi.__doc__)
```

### 5.6.2 Type Hints (Pengenalan)

Python 3.5+ mendukung **type hints** — anotasi tipe data pada parameter dan return value:

```python
def hitung_diskon(harga: int, persen: float = 10.0) -> int:
    """Menghitung harga setelah diskon."""
    potongan = harga * persen / 100
    return int(harga - potongan)

# Type hints TIDAK memaksa tipe data (hanya dokumentasi)
# tetapi membantu IDE dan pembaca kode memahami fungsi
```

### 5.6.3 Best Practices Penamaan Fungsi

| Aturan | Contoh Baik | Contoh Buruk |
|--------|-------------|-------------|
| Gunakan snake_case | `hitung_rata_rata()` | `hitungRataRata()` |
| Gunakan kata kerja | `hitung_total()` | `total()` |
| Nama deskriptif | `validasi_input_nim()` | `cek()` |
| Singkat tapi jelas | `cari_mahasiswa()` | `fungsi_untuk_mencari_data_mahasiswa_berdasarkan_nim()` |
| Boolean: awali is/has | `is_lulus()`, `has_prasyarat()` | `lulus()`, `prasyarat()` |

---

## 5.7 Studi Kasus: Sistem Penilaian Mahasiswa

Program lengkap yang mendemonstrasikan semua konsep fungsi dalam konteks universitas Indonesia:

```python
# ============================================================
# SISTEM PENILAIAN MAHASISWA SEDERHANA
# Mata Kuliah: Algoritma dan Pemrograman — UAI
# ============================================================

def input_nilai_mahasiswa():
    """Meminta input nilai komponen dari pengguna."""
    print("\nMasukkan nilai komponen (0-100):")
    tugas = float(input("  Tugas Mingguan  : "))
    kuis = float(input("  Kuis            : "))
    uts = float(input("  UTS             : "))
    proyek = float(input("  Proyek Akhir    : "))
    uas = float(input("  UAS             : "))
    partisipasi = float(input("  Partisipasi     : "))
    return tugas, kuis, uts, proyek, uas, partisipasi

def hitung_nilai_akhir(tugas, kuis, uts, proyek, uas, partisipasi):
    """
    Menghitung nilai akhir berdasarkan bobot.

    Bobot: Tugas 15%, Kuis 10%, UTS 20%, Proyek 25%, UAS 25%, Partisipasi 5%
    """
    nilai_akhir = (
        tugas * 0.15 +
        kuis * 0.10 +
        uts * 0.20 +
        proyek * 0.25 +
        uas * 0.25 +
        partisipasi * 0.05
    )
    return round(nilai_akhir, 2)

def konversi_huruf(nilai_akhir):
    """Mengkonversi nilai angka ke huruf (standar UAI)."""
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 80:
        return "A-"
    elif nilai_akhir >= 75:
        return "B+"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 65:
        return "B-"
    elif nilai_akhir >= 60:
        return "C+"
    elif nilai_akhir >= 55:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"

def bobot_mutu(huruf):
    """Mengembalikan bobot mutu dari nilai huruf."""
    tabel = {
        "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0,
        "B-": 2.7, "C+": 2.3, "C": 2.0, "D": 1.0, "E": 0.0
    }
    return tabel.get(huruf, 0.0)

def is_lulus(huruf):
    """Menentukan apakah mahasiswa lulus (minimal C)."""
    return huruf not in ("D", "E")

def cetak_hasil(nama, nim, nilai_akhir, huruf):
    """Mencetak hasil penilaian dalam format rapi."""
    print("\n" + "=" * 45)
    print("       HASIL PENILAIAN MATA KULIAH")
    print("    Algoritma dan Pemrograman — 3 SKS")
    print("=" * 45)
    print(f"  Nama        : {nama}")
    print(f"  NIM         : {nim}")
    print(f"  Nilai Akhir : {nilai_akhir}")
    print(f"  Nilai Huruf : {huruf}")
    print(f"  Bobot Mutu  : {bobot_mutu(huruf)}")
    print(f"  Status      : {'LULUS' if is_lulus(huruf) else 'TIDAK LULUS'}")
    print("=" * 45)

# --- Program Utama ---
def main():
    """Fungsi utama program."""
    print("SISTEM PENILAIAN MAHASISWA")
    print("Mata Kuliah: Algoritma dan Pemrograman")
    print("-" * 40)

    nama = input("Nama Mahasiswa : ")
    nim = input("NIM            : ")

    komponen = input_nilai_mahasiswa()
    nilai_akhir = hitung_nilai_akhir(*komponen)
    huruf = konversi_huruf(nilai_akhir)

    cetak_hasil(nama, nim, nilai_akhir, huruf)

# Jalankan
main()
```

---

## AI Corner: AI sebagai Asisten Refactoring

**Level: Menengah**

### Cara Meminta AI Membantu Menulis Fungsi

```
Prompt: "Saya memiliki kode Python berikut yang menghitung
total belanja. Tolong buatkan fungsi-fungsi yang terpisah
untuk setiap operasi. Kode saat ini:
[tempel kode Anda]"
```

### Cara Meminta AI Melakukan Refactoring

```
Prompt: "Refactor kode berikut menjadi fungsi-fungsi modular.
Terapkan prinsip DRY dan top-down design.
Pastikan setiap fungsi memiliki docstring.
[tempel kode Anda]"
```

### Memvalidasi Saran AI tentang Dekomposisi

Ketika AI menyarankan pembagian fungsi, tanyakan pada diri sendiri:
1. Apakah setiap fungsi melakukan **satu tugas** saja?
2. Apakah nama fungsi **menjelaskan** apa yang dilakukannya?
3. Apakah fungsi bisa **digunakan ulang** di tempat lain?
4. Apakah **jumlah parameter** tidak terlalu banyak (ideal ≤ 3)?

> **Ingat:** AI adalah asisten, bukan guru. Selalu verifikasi saran AI dengan pemahaman Anda sendiri tentang prinsip-prinsip yang dipelajari di bab ini.

---

## Latihan Soal

### Tingkat Dasar

1. **Fungsi Sederhana:** Buatlah fungsi `luas_segitiga(alas, tinggi)` yang menghitung dan mengembalikan luas segitiga. Panggil fungsi tersebut untuk 3 segitiga berbeda.

2. **Fungsi Salam:** Buatlah fungsi `salam_islami(nama, waktu="pagi")` yang menampilkan salam berdasarkan waktu. Default waktu adalah "pagi". Jika waktu "pagi" → "Selamat pagi", "siang" → "Selamat siang", dst.

3. **Fungsi Konversi:** Buatlah fungsi `rupiah_ke_dollar(rupiah, kurs=15500)` yang mengkonversi Rupiah ke Dollar AS. Parameter kurs memiliki default value.

4. **Identifikasi Scope:** Perhatikan kode berikut. Apa output dari setiap perintah `print()`? Jelaskan mengapa.
   ```python
   x = 10
   def ubah():
       x = 20
       print(x)
   ubah()
   print(x)
   ```

5. **Multiple Return:** Buatlah fungsi `info_lingkaran(jari_jari)` yang mengembalikan **dua nilai**: luas dan keliling lingkaran. (π = 3.14159)

### Tingkat Menengah

1. **Validasi Input:** Buatlah fungsi `input_bilangan_positif(prompt)` yang terus meminta input hingga pengguna memasukkan bilangan positif. Gunakan fungsi ini dalam program yang menghitung rata-rata dari n bilangan.

2. **Fungsi Rekap Nilai:** Buatlah program dengan fungsi-fungsi berikut:
   - `input_nilai(n)` — meminta n nilai dari pengguna
   - `hitung_rata_rata(daftar)` — menghitung rata-rata
   - `hitung_tertinggi(daftar)` — mencari nilai tertinggi
   - `hitung_terendah(daftar)` — mencari nilai terendah
   - `cetak_rekap(rata, maks, min)` — menampilkan rekap

3. **Refactoring:** Kode berikut menghitung harga di 3 toko berbeda dengan cara yang sama. Refactor menggunakan fungsi!
   ```python
   harga1 = 50000
   pajak1 = harga1 * 0.11
   total1 = harga1 + pajak1
   print(f"Toko 1: Rp {total1:,.0f}")

   harga2 = 75000
   pajak2 = harga2 * 0.11
   total2 = harga2 + pajak2
   print(f"Toko 2: Rp {total2:,.0f}")

   harga3 = 120000
   pajak3 = harga3 * 0.11
   total3 = harga3 + pajak3
   print(f"Toko 3: Rp {total3:,.0f}")
   ```

4. **Top-Down Design:** Gambarkan diagram top-down untuk program "Sistem Pemesanan Tiket Bioskop" dan implementasikan setiap fungsi dalam diagram.

5. **Fungsi Validator:** Buatlah fungsi `validasi_nim(nim)` yang mengembalikan `True` jika NIM valid (format: 4 digit tahun + 3 digit kode prodi + 3 digit nomor urut, total 10 digit), `False` jika tidak valid.

### Tingkat Mahir

1. **Kalkulator Lengkap:** Buatlah program kalkulator ilmiah dengan fungsi-fungsi: tambah, kurang, kali, bagi, pangkat, akar kuadrat, faktorial. Program harus memiliki menu, validasi input, dan bisa diulang.

2. **Sistem Kasir:** Rancang dan implementasikan program kasir warung sederhana menggunakan top-down design. Minimal 6 fungsi: tampilkan_menu, tambah_barang, hapus_barang, hitung_total, cetak_struk, main. Semua harga dalam Rupiah.

3. **Analisis Fungsi:** Diberikan sebuah fungsi Python dari AI. Analisis: (a) apa yang dilakukan fungsi ini, (b) identifikasi minimal 2 bug atau masalah, (c) perbaiki, (d) tambahkan docstring dan type hints.
   ```python
   def proses(data, x):
       r = []
       for i in data:
           if i > x:
               r.append(i)
       if len(r) == 0:
           return -1
       t = 0
       for j in r:
           t += j
       return t / len(r)
   ```

---

## Rangkuman

- **Fungsi** adalah blok kode bernama yang melakukan tugas tertentu dan dapat dipanggil berulang kali.
- Fungsi didefinisikan dengan keyword `def`, bisa menerima **parameter**, dan mengembalikan nilai dengan `return`.
- **Parameter** bisa berupa: positional, keyword, default, `*args`, dan `**kwargs`.
- **Scope** menentukan di mana variabel bisa diakses: **Local → Enclosing → Global → Built-in (LEGB)**.
- Prinsip **DRY** (Don't Repeat Yourself): hindari duplikasi kode, buat fungsi.
- **Top-down design**: pecah program besar menjadi fungsi-fungsi kecil dari umum ke spesifik.
- **Docstring** mendokumentasikan fungsi: apa yang dilakukan, parameter, dan return value.
- **Type hints** membantu keterbacaan: `def f(x: int) -> str:`.
- Penamaan fungsi: gunakan **snake_case**, awali dengan **kata kerja**, nama harus deskriptif.
- Fungsi yang baik: **satu tugas**, parameter tidak terlalu banyak, ada dokumentasi.

---

## Referensi

1. Downey, A. B. (2024). *Think Python* (3rd ed.). O'Reilly Media. Bab tentang Functions.
2. Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.). MIT Press.
3. Python Software Foundation. (2026). Python 3.x Documentation — Defining Functions. https://docs.python.org/3/tutorial/controlflow.html#defining-functions
4. van Rossum, G. et al. (2001). "PEP 8 — Style Guide for Python Code."
5. van Rossum, G. et al. (2014). "PEP 484 — Type Hints."
6. Martin, R. C. (2008). *Clean Code*. Pearson Education.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
