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
2. **Menelusuri** (tracing) call stack rekursif secara manual untuk memahami alur eksekusi
3. **Mengoptimalkan** fungsi rekursif menggunakan teknik memoization
4. **Membangun** program seni rekursif (Recursive Art) menggunakan pola ASCII

---

## Persiapan

- Buka Google Colab di browser: [colab.research.google.com](https://colab.research.google.com)
- Buat notebook baru dengan nama: `Lab12_NIM_NamaLengkap.ipynb`
- Pastikan sudah memahami konsep fungsi dan parameter dari Lab sebelumnya

---

## Langkah-langkah Praktikum

### Langkah 1: Faktorial Rekursif (10 menit)

Rekursi adalah teknik di mana fungsi memanggil dirinya sendiri. Setiap fungsi rekursif membutuhkan **base case** (kondisi berhenti) dan **recursive case**.

```python
def faktorial(n, depth=0):
    """
    Menghitung n! secara rekursif dengan visualisasi call stack.
    """
    indent = "  " * depth
    print(f"{indent}→ faktorial({n}) dipanggil")

    # Base case
    if n == 0 or n == 1:
        print(f"{indent}← faktorial({n}) = 1  [base case]")
        return 1

    # Recursive case
    hasil = n * faktorial(n - 1, depth + 1)
    print(f"{indent}← faktorial({n}) = {n} × {hasil // n} = {hasil}")
    return hasil

# Uji coba
print("=== FAKTORIAL REKURSIF ===\n")
n = 5
hasil = faktorial(n)
print(f"\n{n}! = {hasil}")
```

**Latihan tracing:** Gambar call stack untuk `faktorial(4)` di kertas sebelum menjalankan kode.

### Langkah 2: Fibonacci — Naive vs Memoization (15 menit)

Deret Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

```python
import time

# === FIBONACCI NAIVE (tanpa optimasi) ===
call_count_naive = 0

def fibonacci_naive(n):
    """Fibonacci rekursif tanpa optimasi — sangat lambat untuk n besar."""
    global call_count_naive
    call_count_naive += 1

    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

# === FIBONACCI DENGAN MEMOIZATION ===
call_count_memo = 0

def fibonacci_memo(n, memo={}):
    """Fibonacci rekursif dengan memoization — jauh lebih cepat."""
    global call_count_memo
    call_count_memo += 1

    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# === PERBANDINGAN ===
print("=== FIBONACCI: NAIVE vs MEMOIZATION ===\n")

for n in [10, 20, 30, 35]:
    call_count_naive = 0
    call_count_memo = 0

    start = time.time()
    hasil_naive = fibonacci_naive(n)
    waktu_naive = time.time() - start

    start = time.time()
    hasil_memo = fibonacci_memo(n, {})  # reset memo setiap kali
    waktu_memo = time.time() - start

    print(f"fibonacci({n}) = {hasil_naive}")
    print(f"  Naive : {call_count_naive:>12,} panggilan, {waktu_naive:.6f} detik")
    print(f"  Memo  : {call_count_memo:>12,} panggilan, {waktu_memo:.6f} detik")
    if waktu_naive > 0:
        print(f"  Speedup: {waktu_naive / max(waktu_memo, 1e-9):,.0f}x lebih cepat")
    print()
```

### Langkah 3: Tower of Hanoi (10 menit)

Pindahkan n piringan dari tiang A ke tiang C menggunakan tiang B sebagai perantara.

```python
def tower_of_hanoi(n, sumber, tujuan, perantara, langkah_counter=[0]):
    """
    Menyelesaikan Tower of Hanoi secara rekursif.
    Aturan: hanya boleh memindahkan 1 piringan, piringan besar tidak boleh
    di atas piringan kecil.
    """
    if n == 1:
        langkah_counter[0] += 1
        print(f"  Langkah {langkah_counter[0]:>2}: "
              f"Pindahkan piringan 1 dari {sumber} ke {tujuan}")
        return

    tower_of_hanoi(n - 1, sumber, perantara, tujuan, langkah_counter)
    langkah_counter[0] += 1
    print(f"  Langkah {langkah_counter[0]:>2}: "
          f"Pindahkan piringan {n} dari {sumber} ke {tujuan}")
    tower_of_hanoi(n - 1, perantara, tujuan, sumber, langkah_counter)

# Uji coba
print("=== TOWER OF HANOI ===\n")
for jumlah_piringan in [3, 4]:
    print(f"--- {jumlah_piringan} Piringan ---")
    langkah = [0]
    tower_of_hanoi(jumlah_piringan, "A", "C", "B", langkah)
    print(f"  Total langkah: {langkah[0]} (2^{jumlah_piringan} - 1 = {2**jumlah_piringan - 1})\n")
```

### Langkah 4: Binary Search Rekursif (10 menit)

Versi rekursif dari Binary Search yang sudah dipelajari di Lab 10.

```python
def binary_search_rekursif(data, target, left, right, depth=0):
    """
    Binary Search versi rekursif dengan visualisasi call stack.
    """
    indent = "  " * depth
    print(f"{indent}→ search(left={left}, right={right})", end="")

    if left > right:
        print(f" — TIDAK DITEMUKAN")
        return -1

    mid = (left + right) // 2
    print(f", mid={mid}, data[mid]={data[mid]}", end="")

    if data[mid] == target:
        print(f" ← DITEMUKAN!")
        return mid
    elif data[mid] < target:
        print(f" → cari kanan")
        return binary_search_rekursif(data, target, mid + 1, right, depth + 1)
    else:
        print(f" → cari kiri")
        return binary_search_rekursif(data, target, left, mid - 1, depth + 1)

# Uji coba
data = [4, 8, 15, 19, 23, 31, 42, 55, 67, 88]
print("=== BINARY SEARCH REKURSIF ===")
print(f"Data: {data}\n")

for target in [31, 10]:
    print(f"Mencari {target}:")
    hasil = binary_search_rekursif(data, target, 0, len(data) - 1)
    if hasil != -1:
        print(f"Hasil: ditemukan di index {hasil}\n")
    else:
        print(f"Hasil: tidak ditemukan\n")
```

### Langkah 5: Perbandingan Rekursif vs Iteratif (5 menit)

```python
import time

# === FAKTORIAL ITERATIF ===
def faktorial_iteratif(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

# === PERBANDINGAN ===
def faktorial_rekursif_simple(n):
    if n <= 1:
        return 1
    return n * faktorial_rekursif_simple(n - 1)

print("=== REKURSIF vs ITERATIF ===\n")
print(f"{'n':<8} {'Rekursif (dtk)':<18} {'Iteratif (dtk)':<18} {'Hasil sama?'}")
print("-" * 55)

for n in [100, 500, 900]:
    start = time.time()
    r1 = faktorial_rekursif_simple(n)
    t_rekursif = time.time() - start

    start = time.time()
    r2 = faktorial_iteratif(n)
    t_iteratif = time.time() - start

    print(f"{n:<8} {t_rekursif:<18.6f} {t_iteratif:<18.6f} {r1 == r2}")

print("\nCatatan: Python memiliki batas kedalaman rekursi (~1000 secara default).")
print(f"Batas rekursi saat ini: {__import__('sys').getrecursionlimit()}")
```

### Langkah 6: Mini Project — Recursive Art (15 menit)

Buat pola ASCII rekursif. Pilih salah satu: Segitiga Sierpinski atau Pohon Rekursif.

```python
# === SEGITIGA SIERPINSKI (ASCII) ===
def sierpinski(n):
    """
    Menghasilkan Segitiga Sierpinski level n dalam bentuk ASCII.
    """
    if n == 0:
        return ["*"]

    segitiga_kecil = sierpinski(n - 1)
    lebar = len(segitiga_kecil[-1])

    # Bagian atas: satu segitiga kecil di tengah
    atas = [baris.center(lebar * 2 + 1) for baris in segitiga_kecil]

    # Bagian bawah: dua segitiga kecil berdampingan
    bawah = [baris + " " + baris for baris in segitiga_kecil]

    return atas + bawah

print("=== SEGITIGA SIERPINSKI ===\n")
for level in range(5):
    print(f"--- Level {level} ---")
    pola = sierpinski(level)
    for baris in pola:
        print(baris)
    print()

# === POHON REKURSIF (ASCII) ===
def pohon_rekursif(tinggi, prefix="", is_last=True, label="Akar"):
    """
    Menggambar pohon rekursif dalam bentuk ASCII tree.
    Setiap node memiliki dua cabang sampai tinggi = 0.
    """
    connector = "└── " if is_last else "├── "
    print(f"{prefix}{connector}{label}")

    if tinggi <= 0:
        return

    extension = "    " if is_last else "│   "
    new_prefix = prefix + extension

    pohon_rekursif(tinggi - 1, new_prefix, False, f"Cabang Kiri (h={tinggi-1})")
    pohon_rekursif(tinggi - 1, new_prefix, True, f"Cabang Kanan (h={tinggi-1})")

print("\n=== POHON REKURSIF (ASCII) ===\n")
pohon_rekursif(3, "", True, "Akar (h=3)")
```

---

## Tantangan Tambahan

1. **Sum of Digits:** Buat fungsi rekursif `jumlah_digit(n)` yang menghitung jumlah digit suatu bilangan (contoh: `jumlah_digit(1234)` = 10). Tampilkan call stack-nya.
2. **Palindrome Check:** Buat fungsi rekursif `is_palindrome(s)` yang mengecek apakah string s adalah palindrom. Uji dengan kata-kata bahasa Indonesia seperti "katak", "level", "malam".
3. **Flood Fill:** Implementasikan algoritma Flood Fill rekursif pada grid 2D (seperti bucket fill pada program menggambar). Tampilkan grid sebelum dan sesudah.

---

## Checklist Penyelesaian

- [ ] Mampu mengimplementasikan faktorial rekursif dengan visualisasi call stack
- [ ] Mampu mengimplementasikan Fibonacci naive dan versi memoization, memahami perbedaan performanya
- [ ] Mampu menyelesaikan Tower of Hanoi secara rekursif
- [ ] Mampu mengimplementasikan Binary Search versi rekursif
- [ ] Memahami perbandingan performa rekursif vs iteratif
- [ ] Menyelesaikan mini project Recursive Art (Sierpinski atau Pohon Rekursif)
- [ ] Notebook disimpan dengan nama `Lab12_NIM_NamaLengkap.ipynb`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
