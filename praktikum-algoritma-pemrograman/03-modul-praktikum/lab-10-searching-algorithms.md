# Lab 10: Algoritma Pencarian

## Informasi Praktikum

| Komponen | Keterangan |
|----------|------------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Kode MK** | INF-101 |
| **Semester** | Genap 2025/2026 |
| **Praktikum** | Lab 10 — Algoritma Pencarian |
| **Durasi** | 75 menit |
| **Prasyarat** | Lab 09 (Pemilihan Struktur Data), Modul Minggu 10 |
| **Platform** | Google Colab |
| **Pengajar** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. **Mengimplementasikan** algoritma Linear Search dan Binary Search dalam Python
2. **Menelusuri** (tracing) langkah-langkah pencarian secara manual untuk memahami mekanisme kerja algoritma
3. **Membandingkan** performa kedua algoritma pada dataset dengan ukuran berbeda menggunakan modul `time`
4. **Membangun** Sistem Pencarian Mahasiswa yang menggunakan kedua algoritma secara tepat

---

## Persiapan

- Buka Google Colab di browser: [colab.research.google.com](https://colab.research.google.com)
- Buat notebook baru dengan nama: `Lab10_NIM_NamaLengkap.ipynb`
- Pastikan sudah memahami konsep list dan perbandingan elemen

---

## Langkah-langkah Praktikum

### Langkah 1: Implementasi Linear Search (10 menit)

Linear Search memeriksa setiap elemen satu per satu dari awal hingga akhir.

```python
def linear_search(data, target):
    """
    Mencari target dalam data secara linear (sequential).
    Mengembalikan index jika ditemukan, -1 jika tidak.
    """
    langkah = 0
    for i in range(len(data)):
        langkah += 1
        print(f"  Langkah {langkah}: Periksa index [{i}] = {data[i]}", end="")
        if data[i] == target:
            print(f"  ← DITEMUKAN!")
            return i, langkah
        print()
    return -1, langkah

# Uji coba
angka = [15, 42, 8, 23, 67, 31, 55, 4, 19, 88]
print(f"Data: {angka}")
print(f"Mencari: 31\n")

index, langkah = linear_search(angka, 31)
if index != -1:
    print(f"\nHasil: Ditemukan di index {index} dalam {langkah} langkah")
else:
    print(f"\nHasil: Tidak ditemukan setelah {langkah} langkah")
```

### Langkah 2: Implementasi Binary Search (15 menit)

Binary Search bekerja pada data **yang sudah terurut**. Setiap langkah memotong ruang pencarian menjadi setengah.

```python
def binary_search(data, target):
    """
    Mencari target dalam data terurut secara binary (iteratif).
    Mengembalikan index jika ditemukan, -1 jika tidak.
    """
    left = 0
    right = len(data) - 1
    langkah = 0

    while left <= right:
        langkah += 1
        mid = (left + right) // 2
        print(f"  Langkah {langkah}: left={left}, right={right}, mid={mid}, "
              f"data[mid]={data[mid]}", end="")

        if data[mid] == target:
            print(f"  ← DITEMUKAN!")
            return mid, langkah
        elif data[mid] < target:
            print(f"  → target lebih besar, geser left")
            left = mid + 1
        else:
            print(f"  → target lebih kecil, geser right")
            right = mid - 1

    return -1, langkah

# Uji coba — data HARUS terurut
angka_terurut = [4, 8, 15, 19, 23, 31, 42, 55, 67, 88]
print(f"Data (terurut): {angka_terurut}")
print(f"Mencari: 31\n")

index, langkah = binary_search(angka_terurut, 31)
if index != -1:
    print(f"\nHasil: Ditemukan di index {index} dalam {langkah} langkah")
else:
    print(f"\nHasil: Tidak ditemukan setelah {langkah} langkah")
```

### Langkah 3: Latihan Tracing (10 menit)

Isi tabel tracing berikut secara manual, lalu verifikasi dengan menjalankan kode.

**Soal:** Gunakan Binary Search untuk mencari **67** dalam data `[4, 8, 15, 19, 23, 31, 42, 55, 67, 88]`.

```python
# Isi tabel tracing ini sebelum menjalankan kode:
print("=== TABEL TRACING BINARY SEARCH ===")
print(f"{'Langkah':<8} {'Left':<6} {'Right':<7} {'Mid':<5} {'data[mid]':<10} {'Aksi'}")
print("-" * 50)
# Contoh format output — isi secara manual dulu di kertas/komentar:
# Langkah 1: left=0, right=9, mid=4, data[4]=23, target>23 → left=5
# Langkah 2: ...
# Langkah 3: ...

print("\n=== VERIFIKASI DENGAN KODE ===")
data_trace = [4, 8, 15, 19, 23, 31, 42, 55, 67, 88]
index, langkah = binary_search(data_trace, 67)
print(f"\nJawaban: index={index}, langkah={langkah}")
```

**Latihan mandiri:** Trace pencarian angka **10** (tidak ada dalam data). Berapa langkah yang dibutuhkan?

### Langkah 4: Perbandingan Performa (15 menit)

Bandingkan kecepatan kedua algoritma pada dataset besar.

```python
import time
import random

def linear_search_silent(data, target):
    """Linear search tanpa print (untuk pengukuran waktu)."""
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

def binary_search_silent(data, target):
    """Binary search tanpa print (untuk pengukuran waktu)."""
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# === PERBANDINGAN PERFORMA ===
ukuran_data = [1_000, 10_000, 100_000, 1_000_000]

print(f"{'Ukuran Data':<15} {'Linear (detik)':<18} {'Binary (detik)':<18} {'Rasio'}")
print("=" * 65)

for n in ukuran_data:
    data = list(range(n))  # data sudah terurut
    target = n - 1          # worst case: elemen terakhir

    # Waktu Linear Search
    start = time.time()
    linear_search_silent(data, target)
    waktu_linear = time.time() - start

    # Waktu Binary Search
    start = time.time()
    binary_search_silent(data, target)
    waktu_binary = time.time() - start

    rasio = waktu_linear / waktu_binary if waktu_binary > 0 else float('inf')
    print(f"{n:<15,} {waktu_linear:<18.6f} {waktu_binary:<18.6f} {rasio:,.0f}x")

print("\nKesimpulan: Binary Search jauh lebih cepat, tetapi membutuhkan data terurut!")
```

### Langkah 5: Mini Project — Sistem Pencarian Mahasiswa (25 menit)

Bangun sistem pencarian data mahasiswa yang menggunakan Binary Search untuk NIM (terurut) dan Linear Search untuk nama.

```python
import time

# === DATA MAHASISWA (sudah terurut berdasarkan NIM) ===
daftar_mahasiswa = [
    {"nim": "2025001", "nama": "Ahmad Fauzi", "prodi": "Informatika", "ipk": 3.75},
    {"nim": "2025008", "nama": "Budi Santoso", "prodi": "Informatika", "ipk": 3.50},
    {"nim": "2025015", "nama": "Citra Dewi", "prodi": "Informatika", "ipk": 3.92},
    {"nim": "2025023", "nama": "Diana Putri", "prodi": "Informatika", "ipk": 3.68},
    {"nim": "2025031", "nama": "Eka Prasetya", "prodi": "Informatika", "ipk": 3.45},
    {"nim": "2025042", "nama": "Farhan Rizki", "prodi": "Informatika", "ipk": 3.81},
    {"nim": "2025055", "nama": "Gita Nuraini", "prodi": "Informatika", "ipk": 3.60},
    {"nim": "2025063", "nama": "Hadi Wijaya", "prodi": "Informatika", "ipk": 3.33},
    {"nim": "2025078", "nama": "Indah Permata", "prodi": "Informatika", "ipk": 3.95},
    {"nim": "2025089", "nama": "Joko Susanto", "prodi": "Informatika", "ipk": 3.72},
]

def cari_nim_binary(daftar, target_nim):
    """Mencari mahasiswa berdasarkan NIM menggunakan Binary Search."""
    left, right = 0, len(daftar) - 1
    langkah = 0
    while left <= right:
        langkah += 1
        mid = (left + right) // 2
        nim_mid = daftar[mid]["nim"]
        print(f"  Langkah {langkah}: Periksa NIM {nim_mid}", end="")
        if nim_mid == target_nim:
            print(" ← DITEMUKAN!")
            return daftar[mid], langkah
        elif nim_mid < target_nim:
            print(" → cari di kanan")
            left = mid + 1
        else:
            print(" → cari di kiri")
            right = mid - 1
    return None, langkah

def cari_nama_linear(daftar, query_nama):
    """Mencari mahasiswa berdasarkan nama menggunakan Linear Search (partial match)."""
    hasil = []
    langkah = 0
    for mhs in daftar:
        langkah += 1
        if query_nama.lower() in mhs["nama"].lower():
            hasil.append(mhs)
            print(f"  Langkah {langkah}: {mhs['nama']} ← COCOK!")
        else:
            print(f"  Langkah {langkah}: {mhs['nama']}")
    return hasil, langkah

def tampilkan_mahasiswa(mhs):
    """Menampilkan data satu mahasiswa dalam format rapi."""
    print(f"    NIM   : {mhs['nim']}")
    print(f"    Nama  : {mhs['nama']}")
    print(f"    Prodi : {mhs['prodi']}")
    print(f"    IPK   : {mhs['ipk']:.2f}")

# === PROGRAM UTAMA ===
print("=" * 50)
print("  SISTEM PENCARIAN DATA MAHASISWA")
print("  Informatika — Universitas Al Azhar Indonesia")
print("=" * 50)

while True:
    print("\n  1. Cari berdasarkan NIM (Binary Search)")
    print("  2. Cari berdasarkan Nama (Linear Search)")
    print("  3. Tampilkan semua mahasiswa")
    print("  0. Keluar")

    pilihan = input("\nPilih menu: ").strip()

    if pilihan == '1':
        nim = input("Masukkan NIM: ").strip()
        print(f"\nMencari NIM '{nim}' dengan Binary Search:")
        start = time.time()
        hasil, langkah = cari_nim_binary(daftar_mahasiswa, nim)
        waktu = time.time() - start
        if hasil:
            print(f"\n  Data Mahasiswa Ditemukan ({langkah} langkah, {waktu:.6f} detik):")
            tampilkan_mahasiswa(hasil)
        else:
            print(f"\n  NIM '{nim}' tidak ditemukan ({langkah} langkah).")

    elif pilihan == '2':
        nama = input("Masukkan nama (atau sebagian nama): ").strip()
        print(f"\nMencari nama '{nama}' dengan Linear Search:")
        start = time.time()
        hasil, langkah = cari_nama_linear(daftar_mahasiswa, nama)
        waktu = time.time() - start
        if hasil:
            print(f"\n  Ditemukan {len(hasil)} mahasiswa ({langkah} langkah, {waktu:.6f} detik):")
            for mhs in hasil:
                tampilkan_mahasiswa(mhs)
                print()
        else:
            print(f"\n  Nama '{nama}' tidak ditemukan ({langkah} langkah).")

    elif pilihan == '3':
        print(f"\n  {'No':<4} {'NIM':<10} {'Nama':<20} {'IPK':<6}")
        print("  " + "-" * 40)
        for i, mhs in enumerate(daftar_mahasiswa, 1):
            print(f"  {i:<4} {mhs['nim']:<10} {mhs['nama']:<20} {mhs['ipk']:<6.2f}")

    elif pilihan == '0':
        print("\nTerima kasih! Sampai jumpa.")
        break
    else:
        print("  Pilihan tidak valid.")
```

---

## Tantangan Tambahan

1. **Pencarian Multi-Kriteria:** Tambahkan fitur pencarian berdasarkan rentang IPK (misalnya, semua mahasiswa dengan IPK 3.5-3.8).
2. **Hitung Perbandingan:** Modifikasi program agar menampilkan jumlah perbandingan yang dilakukan, bukan hanya waktu.
3. **Interpolation Search:** Implementasikan algoritma Interpolation Search dan bandingkan dengan Binary Search pada data numerik yang terdistribusi merata.

---

## Checklist Penyelesaian

- [ ] Mampu mengimplementasikan Linear Search dengan visualisasi langkah
- [ ] Mampu mengimplementasikan Binary Search (iteratif) dengan visualisasi langkah
- [ ] Menyelesaikan latihan tracing secara manual dan memverifikasi dengan kode
- [ ] Berhasil membandingkan performa kedua algoritma pada berbagai ukuran data
- [ ] Menyelesaikan mini project Sistem Pencarian Mahasiswa
- [ ] Notebook disimpan dengan nama `Lab10_NIM_NamaLengkap.ipynb`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
