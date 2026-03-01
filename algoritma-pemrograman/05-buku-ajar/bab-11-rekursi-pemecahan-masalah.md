# BAB 11: REKURSI DAN PEMECAHAN MASALAH

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| CPMK-6.7 | Memahami konsep rekursi: base case dan recursive case | C2 (Memahami) |
| CPMK-6.8 | Mengimplementasikan solusi rekursif untuk masalah klasik | C3 (Menerapkan) |
| CPMK-6.9 | Menganalisis call stack dan recursion tree | C4 (Menganalisis) |
| CPMK-6.10 | Mengevaluasi kapan menggunakan rekursi vs iterasi | C5 (Mengevaluasi) |

**Estimasi Waktu:** 3 × 50 menit (3 SKS)

**Prasyarat:** Mahasiswa telah memahami materi Bab 1–10, terutama Bab 5 (fungsi) dan Bab 9-10 (searching dan sorting).

---

## 11.1 Apa Itu Rekursi?

### 11.1.1 Definisi

**Rekursi** (recursion) adalah teknik di mana sebuah fungsi **memanggil dirinya sendiri** untuk menyelesaikan sub-masalah yang lebih kecil, hingga mencapai kondisi dasar (base case) yang bisa diselesaikan langsung.

```python
def fungsi_rekursif(parameter):
    if kondisi_berhenti:      # BASE CASE
        return nilai_dasar
    else:                     # RECURSIVE CASE
        return fungsi_rekursif(parameter_lebih_kecil)
```

### 11.1.2 Analogi

- **Boneka Matryoshka**: Buka boneka besar → di dalamnya ada boneka lebih kecil → buka lagi → lebih kecil → sampai boneka terkecil (base case)
- **Cermin berhadapan**: Bayangan di dalam bayangan di dalam bayangan...
- **Antrian**: "Siapa orang ke-100?" → "Orang ke-99 + 1" → "Siapa orang ke-99?" → "Orang ke-98 + 1" → ... → "Orang ke-1" (base case)

### 11.1.3 Dua Komponen Wajib

Setiap fungsi rekursif **HARUS** memiliki dua komponen:

```
┌─────────────────────────────────────────────────────────────┐
│              DUA KOMPONEN REKURSI                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. BASE CASE (Kasus Dasar)                                 │
│     → Kondisi di mana fungsi BERHENTI memanggil dirinya     │
│     → Mengembalikan nilai langsung tanpa rekursi             │
│     → WAJIB ada! Tanpa base case = infinite recursion       │
│                                                             │
│  2. RECURSIVE CASE (Kasus Rekursif)                         │
│     → Fungsi memanggil dirinya sendiri                      │
│     → Parameter HARUS mendekati base case                   │
│     → Masalah diperkecil di setiap pemanggilan               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 11.1.4 Bahaya Infinite Recursion

```python
# BAHAYA! Tidak ada base case!
def hitung_mundur(n):
    print(n)
    hitung_mundur(n - 1)  # tidak pernah berhenti!

# hitung_mundur(5)
# 5, 4, 3, 2, 1, 0, -1, -2, ... → RecursionError!
```

```python
# BENAR — dengan base case
def hitung_mundur(n):
    if n <= 0:         # BASE CASE
        print("Mulai!")
        return
    print(n)
    hitung_mundur(n - 1)  # RECURSIVE CASE

hitung_mundur(5)
# Output: 5, 4, 3, 2, 1, Mulai!
```

---

## 11.2 Call Stack dan Cara Rekursi Bekerja

### 11.2.1 Apa Itu Call Stack?

**Call stack** adalah struktur data (stack/tumpukan) yang digunakan Python untuk melacak pemanggilan fungsi. Setiap kali fungsi dipanggil, sebuah **stack frame** ditambahkan ke atas stack. Ketika fungsi selesai (return), frame tersebut dikeluarkan.

```
CALL STACK untuk hitung_mundur(3):

    ┌─────────────────────┐
    │ hitung_mundur(0)    │ ← return (base case)
    ├─────────────────────┤
    │ hitung_mundur(1)    │ ← menunggu
    ├─────────────────────┤
    │ hitung_mundur(2)    │ ← menunggu
    ├─────────────────────┤
    │ hitung_mundur(3)    │ ← menunggu
    ├─────────────────────┤
    │ main()              │
    └─────────────────────┘
```

Setelah base case tercapai, stack **unwind** (mengempis kembali):

```
Step 1: hitung_mundur(3) → print(3), panggil hitung_mundur(2)
Step 2: hitung_mundur(2) → print(2), panggil hitung_mundur(1)
Step 3: hitung_mundur(1) → print(1), panggil hitung_mundur(0)
Step 4: hitung_mundur(0) → print("Mulai!"), return  ← BASE CASE
Step 5: hitung_mundur(1) → return (selesai)
Step 6: hitung_mundur(2) → return (selesai)
Step 7: hitung_mundur(3) → return (selesai)
```

### 11.2.2 Stack Overflow

Python memiliki batas kedalaman rekursi (default: 1000):

```python
import sys
print(sys.getrecursionlimit())  # 1000

# Jika melebihi batas:
# RecursionError: maximum recursion depth exceeded

# Bisa diubah (HATI-HATI!):
# sys.setrecursionlimit(5000)
```

---

## 11.3 Contoh Klasik Rekursi

### 11.3.1 Factorial (n!)

**Definisi:** n! = n × (n-1) × (n-2) × ... × 2 × 1, dan 0! = 1

**Secara rekursif:**
- Base case: 0! = 1
- Recursive case: n! = n × (n-1)!

```python
def factorial(n):
    """Menghitung n! secara rekursif."""
    if n == 0:           # BASE CASE
        return 1
    return n * factorial(n - 1)  # RECURSIVE CASE

print(factorial(5))  # 120
```

**Trace call stack untuk factorial(4):**

```
factorial(4) = 4 * factorial(3)
                   factorial(3) = 3 * factorial(2)
                                      factorial(2) = 2 * factorial(1)
                                                         factorial(1) = 1 * factorial(0)
                                                                            factorial(0) = 1  ← BASE
                                                         factorial(1) = 1 * 1 = 1
                                      factorial(2) = 2 * 1 = 2
                   factorial(3) = 3 * 2 = 6
factorial(4) = 4 * 6 = 24
```

### 11.3.2 Fibonacci

**Definisi:** F(0)=0, F(1)=1, F(n) = F(n-1) + F(n-2)

Deret: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

```python
def fibonacci(n):
    """Menghitung bilangan Fibonacci ke-n secara rekursif."""
    if n <= 0:           # BASE CASE 1
        return 0
    if n == 1:           # BASE CASE 2
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # RECURSIVE CASE

for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
```

> **Peringatan:** Fibonacci rekursif naif sangat lambat! F(30) memerlukan jutaan pemanggilan fungsi. Kita akan membahas solusinya di bagian Memoization (11.8).

**Recursion Tree untuk fibonacci(4):**

```
                    fib(4)
                  /        \
              fib(3)       fib(2)
             /     \       /    \
         fib(2)  fib(1)  fib(1) fib(0)
         /    \    |       |      |
     fib(1) fib(0) 1       1      0
       |      |
       1      0
```

Perhatikan: `fib(2)` dihitung **2 kali** — pemborosan!

### 11.3.3 Sum of List (Jumlah Elemen List)

```python
def sum_list(data):
    """Menghitung jumlah seluruh elemen list secara rekursif."""
    if not data:        # BASE CASE: list kosong
        return 0
    return data[0] + sum_list(data[1:])  # RECURSIVE CASE

print(sum_list([1, 2, 3, 4, 5]))  # 15
```

**Trace:**
```
sum_list([1,2,3,4,5]) = 1 + sum_list([2,3,4,5])
                         = 1 + 2 + sum_list([3,4,5])
                         = 1 + 2 + 3 + sum_list([4,5])
                         = 1 + 2 + 3 + 4 + sum_list([5])
                         = 1 + 2 + 3 + 4 + 5 + sum_list([])
                         = 1 + 2 + 3 + 4 + 5 + 0
                         = 15
```

### 11.3.4 String Reversal (Membalik String)

```python
def reverse_string(s):
    """Membalik string secara rekursif."""
    if len(s) <= 1:    # BASE CASE
        return s
    return reverse_string(s[1:]) + s[0]  # RECURSIVE CASE

print(reverse_string("Python"))   # "nohtyP"
print(reverse_string("Indonesia")) # "aisenodnI"
```

### 11.3.5 Power (Pangkat: x^n)

```python
def power(x, n):
    """Menghitung x pangkat n secara rekursif."""
    if n == 0:          # BASE CASE
        return 1
    return x * power(x, n - 1)  # RECURSIVE CASE

print(power(2, 10))   # 1024
print(power(3, 4))    # 81
```

**Versi lebih efisien (fast exponentiation):**

```python
def fast_power(x, n):
    """Menghitung x^n dengan O(log n) — fast exponentiation."""
    if n == 0:
        return 1
    if n % 2 == 0:
        half = fast_power(x, n // 2)
        return half * half
    else:
        return x * fast_power(x, n - 1)
```

---

## 11.4 Recursion Tree: Visualisasi Rekursi

### 11.4.1 Apa Itu Recursion Tree

**Recursion tree** adalah diagram pohon yang menggambarkan semua pemanggilan fungsi rekursif. Setiap node merepresentasikan satu pemanggilan fungsi.

### 11.4.2 Recursion Tree untuk Fibonacci

```
fibonacci(5):
                           fib(5) = 5
                         /            \
                   fib(4) = 3        fib(3) = 2
                  /        \         /        \
            fib(3)=2    fib(2)=1  fib(2)=1  fib(1)=1
            /     \      /    \    /    \
       fib(2)=1 fib(1) fib(1) fib(0) fib(1) fib(0)
       /    \    =1     =1     =0     =1     =0
   fib(1) fib(0)
    =1     =0

Total pemanggilan: 15 (untuk n=5!)
```

Untuk n=5, ada **15 pemanggilan**. Untuk n=30, ada **~2.7 juta** pemanggilan. Inilah mengapa Fibonacci rekursif naif sangat lambat — **O(2^n)**!

### 11.4.3 Recursion Tree untuk Binary Search

```
binary_search([1,3,5,7,9,11,13], target=5)

   search(arr, 0, 6)           → mid=3, arr[3]=7, target<7
         |
   search(arr, 0, 2)           → mid=1, arr[1]=3, target>3
         |
   search(arr, 2, 2)           → mid=2, arr[2]=5, target==5 ✓
```

Binary search rekursif hanya membuat **O(log n)** pemanggilan — sangat efisien!

---

## 11.5 Tower of Hanoi

### 11.5.1 Sejarah dan Aturan

**Tower of Hanoi** adalah teka-teki matematika klasik:

- Ada 3 tiang: **Sumber (A)**, **Bantuan (B)**, **Tujuan (C)**
- Ada n piringan (disk) dengan ukuran berbeda, tersusun di tiang A (terbesar di bawah)
- **Tujuan**: pindahkan semua piringan dari A ke C
- **Aturan**:
  1. Hanya boleh memindahkan 1 piringan per langkah
  2. Piringan yang lebih besar **tidak boleh** diletakkan di atas piringan yang lebih kecil

```
Keadaan awal:           Keadaan akhir:
    |        |   |          |   |        |
   [=]       |   |          |   |       [=]
  [===]      |   |          |   |      [===]
 [=====]     |   |          |   |     [=====]
───A─────────B───────C──   ──A──────B──────C──
```

### 11.5.2 Solusi Rekursif

**Ide kunci:** Untuk memindahkan n piringan dari A ke C:
1. Pindahkan n-1 piringan dari A ke B (menggunakan C sebagai bantuan)
2. Pindahkan piringan terbesar dari A ke C
3. Pindahkan n-1 piringan dari B ke C (menggunakan A sebagai bantuan)

### 11.5.3 Implementasi Python

```python
def hanoi(n, sumber, tujuan, bantuan):
    """
    Menyelesaikan Tower of Hanoi secara rekursif.

    Parameters:
        n: jumlah piringan
        sumber: tiang asal
        tujuan: tiang tujuan
        bantuan: tiang bantuan
    """
    if n == 1:  # BASE CASE
        print(f"  Pindahkan piringan 1 dari {sumber} ke {tujuan}")
        return

    # Pindahkan n-1 piringan dari sumber ke bantuan
    hanoi(n - 1, sumber, bantuan, tujuan)

    # Pindahkan piringan terbesar
    print(f"  Pindahkan piringan {n} dari {sumber} ke {tujuan}")

    # Pindahkan n-1 piringan dari bantuan ke tujuan
    hanoi(n - 1, bantuan, tujuan, sumber)

# Contoh: 3 piringan
print("Tower of Hanoi (3 piringan):")
hanoi(3, "A", "C", "B")
```

**Output:**
```
Tower of Hanoi (3 piringan):
  Pindahkan piringan 1 dari A ke C
  Pindahkan piringan 2 dari A ke B
  Pindahkan piringan 1 dari C ke B
  Pindahkan piringan 3 dari A ke C
  Pindahkan piringan 1 dari B ke A
  Pindahkan piringan 2 dari B ke C
  Pindahkan piringan 1 dari A ke C
```

### 11.5.4 Analisis

Jumlah langkah untuk n piringan: **2^n - 1**

| n | Langkah |
|---|---------|
| 1 | 1 |
| 2 | 3 |
| 3 | 7 |
| 4 | 15 |
| 10 | 1,023 |
| 20 | 1,048,575 |
| 64 | ~1.8 × 10^19 |

> **Legenda:** Menurut legenda, ada 64 piringan emas di kuil Benares. Jika dipindahkan 1 piringan per detik, butuh waktu **585 miliar tahun** untuk menyelesaikannya — lebih lama dari usia alam semesta!

---

## 11.6 Binary Search Rekursif

### 11.6.1 Versi Iteratif vs Rekursif

```python
# ITERATIF (dari Bab 9)
def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# REKURSIF
def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:              # BASE CASE: tidak ditemukan
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:      # BASE CASE: ditemukan
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Test
data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search_recursive(data, 23))   # 5
print(binary_search_recursive(data, 50))   # -1
```

---

## 11.7 Rekursi vs Iterasi

### 11.7.1 Kapan Menggunakan Rekursi

Rekursi cocok ketika:
- Masalah secara alami bersifat rekursif (pohon, graf, fraktal)
- Solusi rekursif lebih mudah dibaca dan dipahami
- Kedalaman rekursi terbatas dan terkontrol
- Contoh: traversal pohon, Tower of Hanoi, divide-and-conquer

### 11.7.2 Kapan Menggunakan Iterasi

Iterasi lebih cocok ketika:
- Masalah bersifat linear (perulangan sederhana)
- Performa dan memory sangat penting
- Kedalaman bisa sangat besar
- Contoh: penjumlahan, pencarian linear, sorting sederhana

### 11.7.3 Tabel Perbandingan

| Aspek | Rekursi | Iterasi |
|-------|---------|---------|
| **Readability** | Lebih intuitif untuk masalah rekursif | Lebih jelas untuk perulangan biasa |
| **Memory** | O(n) stack space | O(1) biasanya |
| **Performance** | Overhead fungsi call | Lebih cepat |
| **Stack overflow** | Mungkin (jika terlalu dalam) | Tidak |
| **Debugging** | Lebih sulit di-trace | Lebih mudah |
| **Cocok untuk** | Tree, graph, divide-and-conquer | Loop, counting, accumulating |

### 11.7.4 Contoh: Factorial Rekursif vs Iteratif

```python
# Rekursif
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

# Iteratif
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Keduanya menghasilkan hasil yang sama
print(factorial_recursive(10))  # 3628800
print(factorial_iterative(10))  # 3628800
```

---

## 11.8 Pengenalan Memoization

### 11.8.1 Masalah Fibonacci yang Lambat

```python
import time

def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)

# Ukur waktu
start = time.time()
print(fibonacci_naive(30))  # 832040
print(f"Waktu: {time.time() - start:.3f}s")  # Lambat!
```

### 11.8.2 Solusi: Memoization (Dictionary Cache)

**Memoization** adalah teknik menyimpan hasil perhitungan yang sudah dilakukan agar tidak perlu dihitung ulang:

```python
def fibonacci_memo(n, cache={}):
    """Fibonacci dengan memoization menggunakan dictionary."""
    if n in cache:       # Sudah pernah dihitung?
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci_memo(n-1, cache) + fibonacci_memo(n-2, cache)
    return cache[n]

start = time.time()
print(fibonacci_memo(30))  # 832040
print(f"Waktu: {time.time() - start:.6f}s")  # Sangat cepat!
```

**Perbandingan:**

| n | Tanpa Memo | Dengan Memo |
|---|-----------|-------------|
| 20 | ~0.003s | ~0.000001s |
| 30 | ~0.3s | ~0.000001s |
| 40 | ~30s | ~0.000001s |
| 50 | ~5400s (1.5 jam!) | ~0.000001s |

### 11.8.3 functools.lru_cache

Python menyediakan decorator bawaan untuk memoization:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_lru(n):
    """Fibonacci dengan lru_cache — otomatis memoization!"""
    if n <= 1:
        return n
    return fibonacci_lru(n-1) + fibonacci_lru(n-2)

print(fibonacci_lru(100))  # 354224848179261915075 (instan!)
```

> **Catatan:** `@lru_cache` adalah fitur lanjutan Python. Cukup ketahui bahwa ini ada — Anda akan memperdalam di mata kuliah lanjutan.

---

## 11.9 Studi Kasus

### 11.9.1 Palindrome Checker Rekursif

```python
def is_palindrome(s):
    """Mengecek apakah string palindrome secara rekursif."""
    # Bersihkan: huruf kecil, hanya alfanumerik
    s = ''.join(c.lower() for c in s if c.isalnum())

    # BASE CASE
    if len(s) <= 1:
        return True

    # RECURSIVE CASE
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Test
print(is_palindrome("racecar"))     # True
print(is_palindrome("Kasur rusak")) # True
print(is_palindrome("Python"))      # False
print(is_palindrome("Kodok"))       # True
```

### 11.9.2 Flatten Nested List

```python
def flatten(nested):
    """Meratakan nested list secara rekursif."""
    result = []
    for item in nested:
        if isinstance(item, list):  # RECURSIVE CASE
            result.extend(flatten(item))
        else:                       # BASE CASE
            result.append(item)
    return result

data = [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10]]]]
print(flatten(data))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

## AI Corner: AI untuk Memahami Rekursi

**Level: Lanjut**

### Meminta AI Menggambar Recursion Tree

```
Prompt: "Gambarkan recursion tree untuk fibonacci(5)
menggunakan ASCII art. Tunjukkan nilai setiap node
dan tandai perhitungan yang duplikat."
```

### Debugging Rekursi dengan AI

```
Prompt: "Fungsi rekursif saya menghasilkan RecursionError.
Ini kodenya: [tempel kode]. Bantu saya identifikasi
mengapa base case tidak tercapai."
```

### Convert Iterasi ↔ Rekursi

```
Prompt: "Konversikan fungsi iteratif berikut menjadi
versi rekursif: [tempel fungsi iteratif]"
```

---

## Latihan Soal

### Tingkat Dasar

1. Trace call stack untuk `factorial(5)`. Tunjukkan setiap frame dan return value.

2. Buatlah fungsi rekursif `jumlah_digit(n)` yang menghitung jumlah digit bilangan positif. Contoh: `jumlah_digit(1234)` → 10 (1+2+3+4).

3. Buatlah fungsi rekursif `pangkat(x, n)` yang menghitung x^n tanpa menggunakan operator `**`.

4. Jelaskan apa yang terjadi jika fungsi rekursif tidak memiliki base case. Berikan contoh.

5. Trace recursion tree untuk `fibonacci(5)`. Berapa total pemanggilan fungsi?

### Tingkat Menengah

1. Implementasikan binary search secara rekursif. Trace untuk data `[3, 7, 11, 15, 19, 23, 27]` dengan target 15.

2. Buatlah fungsi rekursif `gcd(a, b)` yang menghitung FPB (Faktor Persekutuan Terbesar) menggunakan algoritma Euclid: `gcd(a, b) = gcd(b, a % b)`, base case: `gcd(a, 0) = a`.

3. Implementasikan Tower of Hanoi untuk 4 piringan. Hitung jumlah langkah dan verifikasi bahwa hasilnya = 2^4 - 1 = 15.

4. Bandingkan waktu eksekusi Fibonacci rekursif naif vs Fibonacci dengan memoization untuk n = 20, 25, 30, 35. Tampilkan dalam tabel.

5. Buatlah fungsi rekursif dan iteratif untuk menghitung sum of list. Bandingkan: mana yang lebih cepat? Mana yang lebih mudah dibaca?

### Tingkat Mahir

1. Implementasikan **merge sort** secara rekursif: (a) bagi list menjadi dua, (b) sort masing-masing secara rekursif, (c) gabungkan (merge) dua list terurut. Bandingkan performanya dengan insertion sort untuk 1000 elemen.

2. Buatlah fungsi rekursif `permutations(s)` yang menghasilkan semua permutasi string. Contoh: `permutations("abc")` → `["abc", "acb", "bac", "bca", "cab", "cba"]`.

3. **Sierpinski Triangle**: Buat fungsi rekursif yang menggambar segitiga Sierpinski menggunakan karakter ASCII. Contoh level 2:
   ```
       *
      * *
     *   *
    * * * *
   ```

---

## Rangkuman

- **Rekursi** adalah fungsi yang memanggil dirinya sendiri. WAJIB memiliki **base case** dan **recursive case**.
- **Call stack** melacak setiap pemanggilan fungsi. Terlalu dalam → **RecursionError** (stack overflow).
- **Contoh klasik**: factorial (n!), Fibonacci, power, Tower of Hanoi.
- **Recursion tree** memvisualisasikan semua pemanggilan — berguna untuk analisis efisiensi.
- **Tower of Hanoi** memerlukan 2^n - 1 langkah — menunjukkan pertumbuhan eksponensial.
- **Binary search rekursif** membagi masalah menjadi setengah → O(log n).
- **Rekursi vs iterasi**: rekursi lebih intuitif untuk masalah rekursif alami, tetapi iterasi lebih hemat memori.
- **Memoization** menghilangkan perhitungan duplikat — mengubah Fibonacci dari O(2^n) menjadi O(n).
- `functools.lru_cache` menyediakan memoization otomatis di Python.

---

## Referensi

1. Cormen, T. H. et al. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
2. Bhargava, A. (2016). *Grokking Algorithms*. Manning Publications. Bab tentang Recursion.
3. Downey, A. B. (2024). *Think Python* (3rd ed.). O'Reilly Media.
4. Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.). MIT Press.
5. Python Software Foundation. (2026). functools — Higher-order functions. https://docs.python.org/3/library/functools.html

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
