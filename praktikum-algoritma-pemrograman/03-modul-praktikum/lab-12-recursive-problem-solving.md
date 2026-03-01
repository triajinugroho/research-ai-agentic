# Lab 12: Pemecahan Masalah Rekursif

## Informasi Praktikum

| Komponen | Keterangan |
|----------|------------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Kode MK** | INF-101 |
| **Semester** | Genap 2025/2026 |
| **Praktikum** | Lab 12 — Pemecahan Masalah Rekursif |
| **Durasi** | 75 menit |
| **Prasyarat** | Lab 10 (Algoritma Pencarian), Lab 11 (Algoritma Pengurutan), Modul Minggu 12 |
| **Platform** | Google Colab |
| **Pengajar** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. **Mengimplementasikan** fungsi rekursif untuk menyelesaikan masalah klasik (faktorial, Fibonacci, Tower of Hanoi)
2. **Menelusuri** (tracing) call stack dari pemanggilan rekursif untuk memahami alur eksekusi
3. **Menerapkan** teknik memoization untuk mengoptimalkan rekursi
4. **Membangun** Recursive Art — pola ASCII rekursif sebagai penerapan kreatif konsep rekursi

---

## Persiapan

- Buka Google Colab di browser: [colab.research.google.com](https://colab.research.google.com)
- Buat notebook baru dengan nama: `Lab12_NIM_NamaLengkap.ipynb`
- Pastikan sudah memahami konsep fungsi (Lab 05) dan algoritma pencarian (Lab 10)

---

## Langkah-langkah Praktikum

### Langkah 1: Fungsi Rekursif — Faktorial (10 menit)

Fungsi rekursif adalah fungsi yang memanggil dirinya sendiri. Setiap fungsi rekursif memiliki **base case** (kondisi berhenti) dan **recursive case** (pemanggilan diri).

```python
def faktorial(n, kedalaman=0):
    """
    Menghitung n! secara rekursif.
    Menampilkan call stack untuk pemahaman.
    """
    indent = "  " * kedalaman
    print(f"{indent}→ faktorial({n}) dipanggil")

    # Base case
    if n == 0 or n == 1:
        print(f"{indent}← faktorial({n}) = 1 (base case)")
        return 1

    # Recursive case
    hasil = n * faktorial(n - 1, kedalaman + 1)
    print(f"{indent}← faktorial({n}) = {n} × {hasil // n} = {hasil}")
    return hasil

# Uji coba
print("=== TRACING FAKTORIAL ===\n")
hasil = faktorial(5)
print(f"\nHasil akhir: 5! = {hasil}")

# Verifikasi
import math
print(f"Verifikasi math.factorial(5) = {math.factorial(5)}")
```

### Langkah 2: Fibonacci — Naive dan Memoization (15 menit)

Deret Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

```python
import time

# === FIBONACCI NAIVE (LAMBAT) ===
panggilan_naive = 0

def fibonacci_naive(n):
    """Fibonacci rekursif tanpa optimasi — sangat lambat untuk n besar."""
    global panggilan_naive
    panggilan_naive += 1

    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

# === FIBONACCI DENGAN MEMOIZATION (CEPAT) ===
panggilan_memo = 0

def fibonacci_memo(n, cache={}):
    """Fibonacci rekursif dengan memoization — jauh lebih cepat."""
    global panggilan_memo
    panggilan_memo += 1

    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n in cache:
        return cache[n]

    cache[n] = fibonacci_memo(n - 1, cache) + fibonacci_memo(n - 2, cache)
    return cache[n]

# === PERBANDINGAN ===
print("=== PERBANDINGAN FIBONACCI ===\n")
print(f"{'n':<5} {'Hasil':<12} {'Naive (panggilan)':<20} {'Memo (panggilan)':<20}")
print("-" * 55)

for n in [5, 10, 15, 20, 25, 30]:
    panggilan_naive = 0
    panggilan_memo = 0

    start = time.time()
    hasil_naive = fibonacci_naive(n)
    waktu_naive = time.time() - start

    start = time.time()
    fibonacci_memo.cache = {}  # reset cache
    hasil_memo = fibonacci_memo(n, {})
    waktu_memo = time.time() - start

    print(f"{n:<5} {hasil_naive:<12} {panggilan_naive:<20,} {panggilan_memo:<20,}")

print("\nPerhatikan: Jumlah panggilan naive bertumbuh eksponensial!")
print("Memoization mengurangi panggilan secara drastis dengan menyimpan hasil yang sudah dihitung.")

# Menampilkan 15 angka Fibonacci pertama
print("\n15 angka Fibonacci pertama:")
fib_list = [fibonacci_memo(i, {}) for i in range(15)]
print(fib_list)
```

### Langkah 3: Tower of Hanoi (10 menit)

Masalah klasik: pindahkan n piringan dari tiang sumber ke tiang tujuan menggunakan tiang bantu.

```python
langkah_hanoi = 0

def tower_of_hanoi(n, sumber='A', tujuan='C', bantu='B', kedalaman=0):
    """
    Menyelesaikan Tower of Hanoi secara rekursif.
    n piringan dipindahkan dari tiang sumber ke tiang tujuan.
    """
    global langkah_hanoi

    if n == 1:
        langkah_hanoi += 1
        indent = "  " * kedalaman
        print(f"{indent}Langkah {langkah_hanoi}: Pindahkan piringan 1 "
              f"dari {sumber} ke {tujuan}")
        return

    # Pindahkan n-1 piringan dari sumber ke bantu
    tower_of_hanoi(n - 1, sumber, bantu, tujuan, kedalaman + 1)

    # Pindahkan piringan terbesar dari sumber ke tujuan
    langkah_hanoi += 1
    indent = "  " * kedalaman
    print(f"{indent}Langkah {langkah_hanoi}: Pindahkan piringan {n} "
          f"dari {sumber} ke {tujuan}")

    # Pindahkan n-1 piringan dari bantu ke tujuan
    tower_of_hanoi(n - 1, bantu, tujuan, sumber, kedalaman + 1)

# Uji coba dengan 3 piringan
print("=== TOWER OF HANOI (3 piringan) ===\n")
langkah_hanoi = 0
tower_of_hanoi(3)
print(f"\nTotal langkah: {langkah_hanoi}")
print(f"Rumus: 2^n - 1 = 2^3 - 1 = {2**3 - 1}")

# Verifikasi rumus untuk berbagai n
print("\n--- Verifikasi Rumus ---")
for n in range(1, 8):
    langkah_hanoi = 0
    tower_of_hanoi(n, 'A', 'C', 'B', 0)  # Jalankan tapi tanpa print
    # Kita hitung ulang langkah tanpa print
    print(f"  n={n}: langkah = {2**n - 1}")
```

### Langkah 4: Binary Search Rekursif (10 menit)

Implementasi Binary Search secara rekursif, bandingkan dengan versi iteratif dari Lab 10.

```python
def binary_search_rekursif(data, target, left, right, langkah=0):
    """
    Binary Search secara rekursif.
    Mengembalikan (index, langkah) atau (-1, langkah) jika tidak ditemukan.
    """
    langkah += 1
    if left > right:
        return -1, langkah

    mid = (left + right) // 2
    print(f"  Langkah {langkah}: left={left}, right={right}, mid={mid}, "
          f"data[mid]={data[mid]}")

    if data[mid] == target:
        print(f"  → DITEMUKAN di index {mid}!")
        return mid, langkah
    elif data[mid] < target:
        return binary_search_rekursif(data, target, mid + 1, right, langkah)
    else:
        return binary_search_rekursif(data, target, left, mid - 1, langkah)

# Uji coba
data_terurut = [4, 8, 15, 19, 23, 31, 42, 55, 67, 88]
print("=== BINARY SEARCH REKURSIF ===\n")
print(f"Data: {data_terurut}")

target = 42
print(f"\nMencari: {target}")
index, langkah = binary_search_rekursif(data_terurut, target, 0, len(data_terurut) - 1)
print(f"Hasil: index={index}, langkah={langkah}")

target = 50
print(f"\nMencari: {target}")
index, langkah = binary_search_rekursif(data_terurut, target, 0, len(data_terurut) - 1)
print(f"Hasil: index={index} (tidak ditemukan), langkah={langkah}")
```

### Langkah 5: Perbandingan Rekursif vs Iteratif (5 menit)

```python
import time

# Faktorial iteratif
def faktorial_iteratif(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

# Perbandingan waktu
print("=== REKURSIF vs ITERATIF ===\n")
print(f"{'n':<8} {'Rekursif (detik)':<20} {'Iteratif (detik)':<20} {'Hasil sama?'}")
print("-" * 58)

for n in [10, 50, 100, 500, 900]:
    start = time.time()
    r1 = faktorial(n) if n <= 100 else None  # rekursi dibatasi
    t_rekursif = time.time() - start

    start = time.time()
    r2 = faktorial_iteratif(n)
    t_iteratif = time.time() - start

    sama = "Ya" if r1 == r2 else "N/A" if r1 is None else "Tidak"
    print(f"{n:<8} {t_rekursif:<20.6f} {t_iteratif:<20.6f} {sama}")

print("\nCatatan: Python memiliki batas kedalaman rekursi (default: 1000).")
print(f"Batas saat ini: {__import__('sys').getrecursionlimit()}")
```

### Langkah 6: Mini Project — Recursive Art (15 menit)

Buat pola ASCII rekursif — segitiga Sierpinski dalam bentuk teks.

```python
def segitiga_sierpinski(n):
    """
    Menghasilkan segitiga Sierpinski level n menggunakan ASCII.
    Menggunakan teknik rekursif: segitiga besar terdiri dari 3 segitiga kecil.
    """
    if n == 0:
        return ["*"]

    # Dapatkan segitiga level sebelumnya
    sebelumnya = segitiga_sierpinski(n - 1)
    tinggi = len(sebelumnya)
    lebar = len(sebelumnya[-1])

    # Bagian atas: segitiga kecil di tengah
    atas = [" " * (lebar + 1) + baris + " " * (lebar + 1) for baris in sebelumnya]

    # Bagian bawah: dua segitiga kecil berdampingan
    bawah = [sebelumnya[i] + " " + sebelumnya[i] for i in range(tinggi)]

    return atas + bawah

def tampilkan_sierpinski(level):
    """Menampilkan segitiga Sierpinski level tertentu."""
    print(f"\n=== SEGITIGA SIERPINSKI (Level {level}) ===\n")
    pola = segitiga_sierpinski(level)
    for baris in pola:
        print(baris)

# Tampilkan level 0 hingga 4
for level in range(5):
    tampilkan_sierpinski(level)

# === POHON REKURSIF (ASCII) ===
def pohon_rekursif(tinggi, offset=0):
    """Menggambar pohon ASCII secara rekursif."""
    if tinggi <= 0:
        return []

    baris = []
    # Bagian daun (segitiga)
    for i in range(tinggi):
        spasi = " " * (tinggi - i - 1 + offset)
        daun = "*" * (2 * i + 1)
        baris.append(spasi + daun)

    # Rekursi: pohon lebih kecil di atas
    if tinggi > 2:
        sub_pohon = pohon_rekursif(tinggi - 1, offset + 1)
        baris = sub_pohon + baris

    return baris

print("\n=== POHON REKURSIF (tinggi=5) ===\n")
pohon = pohon_rekursif(5)
for baris in pohon:
    print(baris)

# Batang pohon
lebar_max = len(pohon[-1])
for _ in range(3):
    print(" " * (lebar_max // 2 - 1) + "|||")
```

---

## Tantangan Tambahan

1. **Sum of Digits:** Buat fungsi rekursif `jumlah_digit(n)` yang menghitung jumlah digit sebuah bilangan (contoh: `jumlah_digit(1234)` = 10).
2. **Palindrome Checker:** Buat fungsi rekursif `cek_palindrom(teks)` yang memeriksa apakah sebuah string adalah palindrom.
3. **Flood Fill:** Implementasikan algoritma flood fill secara rekursif pada grid 2D (seperti fitur "paint bucket" di editor gambar).

---

## Checklist Penyelesaian

- [ ] Mampu mengimplementasikan faktorial secara rekursif dengan tracing call stack
- [ ] Mampu mengimplementasikan Fibonacci naive dan dengan memoization
- [ ] Mampu menyelesaikan Tower of Hanoi secara rekursif
- [ ] Mampu mengimplementasikan Binary Search secara rekursif
- [ ] Memahami perbandingan performa rekursif vs iteratif
- [ ] Menyelesaikan mini project Recursive Art (Sierpinski/Pohon)
- [ ] Notebook disimpan dengan nama `Lab12_NIM_NamaLengkap.ipynb`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
