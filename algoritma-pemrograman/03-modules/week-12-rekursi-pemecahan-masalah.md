# Minggu 12: Rekursi dan Pemecahan Masalah

## Informasi Modul

| Komponen | Keterangan |
|----------|------------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Kode MK** | IF1101 |
| **SKS** | 3 SKS |
| **Minggu** | 12 (Dua Belas) |
| **Topik** | Rekursi dan Pemecahan Masalah |
| **CPMK** | CPMK-6: Mampu menerapkan algoritma dasar (pencarian, pengurutan, rekursi) untuk menyelesaikan masalah komputasional |
| **Sub-CPMK** | CPMK-6.9: Menjelaskan konsep rekursi (base case dan recursive case) |
| | CPMK-6.10: Mengimplementasikan fungsi rekursif untuk masalah klasik (faktorial, Fibonacci, Tower of Hanoi) |
| | CPMK-6.11: Memvisualisasikan recursion tree dan call stack |
| | CPMK-6.12: Membandingkan pendekatan rekursif dan iteratif serta menerapkan memoization |
| **Durasi** | 150 menit |
| **Metode** | Ceramah, Live Coding, Call Stack Tracing, Demonstrasi, Kuis |
| **Bahasa Pemrograman** | Python |
| **Semester** | Genap 2025/2026 |
| **Pengajar** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Menjelaskan** konsep rekursi dengan mengidentifikasi base case dan recursive case pada suatu fungsi (C2 — Memahami)
2. **Mengimplementasikan** fungsi rekursif untuk menyelesaikan masalah klasik: faktorial, Fibonacci, dan Tower of Hanoi (C3 — Menerapkan)
3. **Menganalisis** alur eksekusi rekursi melalui recursion tree dan call stack serta menerapkan teknik memoization untuk optimasi (C4 — Menganalisis)
4. **Mengevaluasi** kapan menggunakan pendekatan rekursif vs iteratif berdasarkan efisiensi dan keterbacaan kode (C5 — Mengevaluasi)

---

## Materi Pembelajaran

### 12.1 Apa Itu Rekursi?

Rekursi adalah teknik pemrograman di mana sebuah fungsi **memanggil dirinya sendiri** untuk menyelesaikan masalah yang lebih kecil dari masalah aslinya.

Setiap fungsi rekursif memiliki dua komponen wajib:

1. **Base case** — kondisi berhenti yang mencegah pemanggilan tak terbatas
2. **Recursive case** — pemanggilan fungsi terhadap sub-masalah yang lebih kecil

```python
def hitung_mundur(n):
    """Contoh sederhana rekursi: hitung mundur dari n ke 1."""
    if n <= 0:          # Base case
        print("Selesai!")
        return
    print(n)
    hitung_mundur(n - 1)  # Recursive case

hitung_mundur(5)  # Output: 5, 4, 3, 2, 1, Selesai!
```

> **Peringatan:** Tanpa base case, rekursi akan berjalan tanpa henti hingga Python mengeluarkan `RecursionError: maximum recursion depth exceeded`.

### 12.2 Faktorial

Faktorial dari n (ditulis n!) adalah perkalian semua bilangan bulat positif dari 1 hingga n.

**Definisi matematis:**
- 0! = 1 (base case)
- n! = n x (n-1)! (recursive case)

```python
def faktorial(n):
    """Menghitung n! secara rekursif."""
    if n == 0 or n == 1:    # Base case
        return 1
    return n * faktorial(n - 1)  # Recursive case

print(faktorial(5))  # 120  (5 * 4 * 3 * 2 * 1)
```

#### Tracing Call Stack: `faktorial(4)`

```
faktorial(4)
├── return 4 * faktorial(3)
│   ├── return 3 * faktorial(2)
│   │   ├── return 2 * faktorial(1)
│   │   │   └── return 1          ← base case
│   │   └── return 2 * 1 = 2
│   └── return 3 * 2 = 6
└── return 4 * 6 = 24
```

### 12.3 Fibonacci

Deret Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

**Definisi:**
- F(0) = 0, F(1) = 1 (base cases)
- F(n) = F(n-1) + F(n-2) (recursive case)

#### 12.3.1 Implementasi Naive (Tanpa Optimasi)

```python
def fibonacci(n):
    """Menghitung bilangan Fibonacci ke-n secara rekursif (naive)."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 55
```

**Masalah:** Untuk `fibonacci(30)`, fungsi ini melakukan jutaan pemanggilan karena banyak perhitungan yang **berulang**.

#### 12.3.2 Recursion Tree untuk fibonacci(5)

```
                    fib(5)
                   /      \
              fib(4)       fib(3)
             /     \       /    \
          fib(3)  fib(2) fib(2) fib(1)
         /    \   /   \   /   \
      fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
      /   \
   fib(1) fib(0)
```

Perhatikan `fib(3)` dihitung 2 kali, `fib(2)` dihitung 3 kali — sangat tidak efisien!

#### 12.3.3 Fibonacci dengan Memoization

Memoization menyimpan hasil perhitungan yang sudah pernah dilakukan agar tidak perlu dihitung ulang.

```python
def fibonacci_memo(n, memo={}):
    """Fibonacci dengan memoization — jauh lebih efisien."""
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print(fibonacci_memo(50))  # 12586269025 (instan!)
```

```python
# Alternatif: menggunakan decorator @lru_cache dari functools
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cache(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)

print(fibonacci_cache(100))  # 354224848179261915075
```

### 12.4 Tower of Hanoi

Tower of Hanoi adalah masalah klasik: pindahkan n piringan dari tiang A ke tiang C menggunakan tiang B sebagai perantara, dengan aturan:
- Hanya satu piringan yang boleh dipindahkan pada satu waktu
- Piringan besar tidak boleh diletakkan di atas piringan kecil

```python
def tower_of_hanoi(n, sumber, tujuan, perantara):
    """Menyelesaikan Tower of Hanoi untuk n piringan."""
    if n == 1:  # Base case
        print(f"Pindahkan piringan 1 dari {sumber} ke {tujuan}")
        return
    # Pindahkan n-1 piringan dari sumber ke perantara
    tower_of_hanoi(n - 1, sumber, perantara, tujuan)
    # Pindahkan piringan terbesar ke tujuan
    print(f"Pindahkan piringan {n} dari {sumber} ke {tujuan}")
    # Pindahkan n-1 piringan dari perantara ke tujuan
    tower_of_hanoi(n - 1, perantara, tujuan, sumber)

print("Tower of Hanoi dengan 3 piringan:")
tower_of_hanoi(3, "A", "C", "B")
```

**Output:**
```
Pindahkan piringan 1 dari A ke C
Pindahkan piringan 2 dari A ke B
Pindahkan piringan 1 dari C ke B
Pindahkan piringan 3 dari A ke C
Pindahkan piringan 1 dari B ke A
Pindahkan piringan 2 dari B ke C
Pindahkan piringan 1 dari A ke C
```

Total langkah untuk n piringan: **2^n - 1** (untuk 3 piringan = 7 langkah).

### 12.5 Binary Search Rekursif

```python
def binary_search_recursive(data, target, low, high):
    """Binary search menggunakan rekursi."""
    if low > high:              # Base case: tidak ditemukan
        return -1

    mid = (low + high) // 2

    if data[mid] == target:     # Base case: ditemukan
        return mid
    elif data[mid] < target:
        return binary_search_recursive(data, target, mid + 1, high)
    else:
        return binary_search_recursive(data, target, low, mid - 1)

data = [3, 7, 11, 18, 25, 33, 42, 56, 71, 89]
hasil = binary_search_recursive(data, 42, 0, len(data) - 1)
print(f"Ditemukan di index: {hasil}")  # Ditemukan di index: 6
```

### 12.6 Rekursif vs Iteratif

| Aspek | Rekursif | Iteratif |
|-------|----------|----------|
| **Keterbacaan** | Lebih elegan untuk masalah rekursif alami | Lebih mudah untuk masalah sekuensial |
| **Memori** | Menggunakan call stack (risiko stack overflow) | Memori konstan (biasanya) |
| **Performa** | Overhead pemanggilan fungsi | Umumnya lebih cepat |
| **Debugging** | Lebih sulit (call stack dalam) | Lebih mudah |
| **Kapan dipakai** | Struktur rekursif: tree, divide & conquer | Loop sederhana, iterasi data |

```python
# Perbandingan: Faktorial rekursif vs iteratif

def faktorial_iteratif(n):
    """Faktorial menggunakan loop (iteratif)."""
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

# Keduanya menghasilkan output yang sama
print(faktorial(10))            # 3628800 (rekursif)
print(faktorial_iteratif(10))   # 3628800 (iteratif)
```

### 12.7 Visualisasi Call Stack

```python
def faktorial_trace(n, depth=0):
    """Faktorial dengan visualisasi call stack."""
    indent = "  " * depth
    print(f"{indent}faktorial({n}) dipanggil")

    if n == 0 or n == 1:
        print(f"{indent}faktorial({n}) mengembalikan 1")
        return 1

    result = n * faktorial_trace(n - 1, depth + 1)
    print(f"{indent}faktorial({n}) mengembalikan {result}")
    return result

faktorial_trace(4)
```

**Output:**
```
faktorial(4) dipanggil
  faktorial(3) dipanggil
    faktorial(2) dipanggil
      faktorial(1) dipanggil
      faktorial(1) mengembalikan 1
    faktorial(2) mengembalikan 2
  faktorial(3) mengembalikan 6
faktorial(4) mengembalikan 24
```

---

## Kegiatan Pembelajaran

### Pre-Class (15 menit)

- Membaca konsep dasar rekursi dari referensi utama
- Menonton video singkat tentang recursion dan call stack
- Mempersiapkan diri untuk Kuis K3 (materi Minggu 9–12)

### In-Class (120 menit)

| Waktu | Aktivitas | Deskripsi |
|-------|-----------|-----------|
| 0–25 menit | Ceramah: Konsep Rekursi | Base case, recursive case, call stack, contoh sederhana (hitung mundur, faktorial) |
| 25–45 menit | Live Coding: Fibonacci | Implementasi naive, visualisasi recursion tree, masalah performa, solusi memoization |
| 45–60 menit | Demonstrasi: Tower of Hanoi | Penjelasan masalah, demonstrasi fisik/visual, implementasi Python |
| 60–75 menit | Live Coding: Binary Search Rekursif | Membandingkan versi iteratif (minggu 10) dengan versi rekursif |
| 75–90 menit | Call Stack Tracing Exercise | Mahasiswa menelusuri call stack secara manual untuk fungsi rekursif yang diberikan |
| 90–105 menit | Diskusi: Rekursif vs Iteratif | Perbandingan, kapan memakai masing-masing pendekatan |
| 105–120 menit | **Kuis K3** | Kuis tertulis mencakup materi Minggu 9–12 (dictionary, set, searching, sorting, rekursi) |

### Post-Class (15 menit)

- Mengerjakan Progress Report proyek akhir (demo 50%+ kode berjalan)
- Berlatih menulis fungsi rekursif tambahan (sum of list, reverse string)
- Membaca materi minggu depan

---

## Penugasan

### Kuis K3: Algoritma (Minggu 9–12)

| Komponen | Keterangan |
|----------|------------|
| **Cakupan** | Dictionary, Set, Pemilihan Struktur Data, Linear Search, Binary Search, Bubble Sort, Selection Sort, Insertion Sort, Rekursi |
| **Format** | Tertulis, 15 menit (di akhir pertemuan) |
| **Jumlah Soal** | 10 soal (pilihan ganda, tracing, dan isian singkat) |
| **Bobot** | Sesuai ketentuan dalam RPS |

### Proyek Akhir — Progress Report (Deadline: Minggu 12)

| Komponen | Keterangan |
|----------|------------|
| **Deskripsi** | Menunjukkan kemajuan proyek akhir dengan minimal 50% kode berjalan |
| **Format** | Demo langsung atau video screen recording (maks 3 menit) + file kode (.py) |
| **Isi** | 1. Demonstrasi fitur yang sudah berfungsi |
| | 2. Penjelasan singkat struktur kode dan pendekatan yang digunakan |
| | 3. Rencana penyelesaian fitur yang tersisa |
| **Pengumpulan** | LMS, sebelum perkuliahan Minggu 13 |
| **Penilaian** | Fungsionalitas kode (50%), Kesesuaian dengan proposal (25%), Kualitas kode (25%) |

---

## Referensi

1. Downey, A. B. (2015). *Think Python: How to Think Like a Computer Scientist* (2nd ed.). O'Reilly Media. — Chapter 5: Conditionals and Recursion, Chapter 6: Fruitful Functions.
2. Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.). MIT Press. — Chapter 6: Recursion and Global Variables.
3. Cormen, T. H., et al. (2022). *Introduction to Algorithms* (4th ed.). MIT Press. — Chapter 4: Divide-and-Conquer.
4. Python Software Foundation. (2025). *Python 3.12 Documentation — functools.lru_cache*. https://docs.python.org/3/library/functools.html#functools.lru_cache

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
