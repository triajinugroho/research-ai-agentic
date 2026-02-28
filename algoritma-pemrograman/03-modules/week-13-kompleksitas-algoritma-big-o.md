# Minggu 13: Kompleksitas Algoritma (Big-O) dan Optimasi

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Algoritma dan Pemrograman (3 SKS) |
| **Minggu** | 13 dari 16 |
| **Topik** | Kompleksitas Algoritma (Big-O) dan Optimasi |
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python |
| **CPMK** | CPMK-7 |
| **Sub-CPMK** | CPMK-7.1, CPMK-7.2, CPMK-7.3, CPMK-7.4 |
| **Durasi** | 150 menit (Teori: 75 menit, Praktik: 75 menit) |
| **Metode** | Ceramah interaktif, Analisis kode, Eksperimen performa, Diskusi |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Menjelaskan** konsep efisiensi algoritma dan mengapa analisis kompleksitas penting dalam pengembangan perangkat lunak (CPMK-7.1)
2. **Menganalisis** kompleksitas waktu (time complexity) dari potongan kode Python menggunakan notasi Big-O (CPMK-7.2)
3. **Membedakan** kelas-kelas kompleksitas umum (O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n)) serta implikasinya terhadap skalabilitas program (CPMK-7.3)
4. **Mengevaluasi** trade-off antara kompleksitas waktu dan ruang (space complexity) serta menerapkan strategi optimasi pada kode yang sudah ada (CPMK-7.4)

---

## Materi Pembelajaran

### 1. Mengapa Efisiensi Algoritma Penting? (CPMK-7.1)

Dua program yang menghasilkan output identik bisa memiliki waktu eksekusi yang sangat berbeda. Pada data kecil, perbedaannya tidak terasa. Namun ketika data tumbuh menjadi jutaan atau miliaran, algoritma yang tidak efisien bisa memakan waktu berjam-jam, sedangkan algoritma efisien selesai dalam hitungan detik.

**Ilustrasi dampak pertumbuhan data:**

| Ukuran Input (n) | O(n) | O(n^2) | O(2^n) |
|-------------------|------|--------|--------|
| 10 | 10 operasi | 100 operasi | 1.024 operasi |
| 100 | 100 operasi | 10.000 operasi | ~10^30 operasi |
| 1.000 | 1.000 operasi | 1.000.000 operasi | Tidak terhitung |
| 1.000.000 | 1.000.000 operasi | 10^12 operasi | Tidak terhitung |

> **Refleksi:** Jika satu operasi memakan 1 mikrodetik, O(n^2) dengan n=1.000.000 membutuhkan sekitar 11,5 hari. Algoritma O(n log n) hanya membutuhkan sekitar 20 detik.

### 2. Notasi Big-O: Definisi dan Aturan (CPMK-7.2)

**Definisi formal:** f(n) = O(g(n)) jika terdapat konstanta positif c dan n0 sedemikian hingga f(n) <= c * g(n) untuk semua n >= n0.

**Definisi informal:** Big-O menggambarkan *batas atas* laju pertumbuhan suatu fungsi ketika input mendekati tak hingga. Kita hanya peduli pada suku dominan dan mengabaikan konstanta.

**Aturan praktis menghitung Big-O:**

1. **Abaikan konstanta** -- 5n menjadi O(n), 100n^2 menjadi O(n^2)
2. **Ambil suku dominan** -- n^2 + 3n + 7 menjadi O(n^2)
3. **Loop berurutan dijumlahkan** -- O(n) + O(n) = O(n)
4. **Loop bersarang dikalikan** -- O(n) * O(n) = O(n^2)

### 3. Kelas-kelas Kompleksitas Umum (CPMK-7.3)

| Kelas | Nama | Contoh Algoritma | Pertumbuhan |
|-------|------|------------------|-------------|
| O(1) | Konstan | Akses elemen list via indeks | Tetap sama |
| O(log n) | Logaritmik | Binary search | Sangat lambat naik |
| O(n) | Linear | Linear search, traversal list | Sebanding input |
| O(n log n) | Linearitmik | Merge sort, Tim sort | Sedikit di atas linear |
| O(n^2) | Kuadratik | Bubble sort, Selection sort | Naik cepat |
| O(2^n) | Eksponensial | Brute-force subset | Meledak sangat cepat |

**Contoh kode untuk setiap kelas:**

```python
# O(1) -- Konstan
def akses_elemen(data, indeks):
    return data[indeks]  # Selalu 1 operasi

# O(log n) -- Logaritmik
def binary_search(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# O(n) -- Linear
def cari_maksimum(data):
    maks = data[0]
    for elemen in data:  # Loop n kali
        if elemen > maks:
            maks = elemen
    return maks

# O(n^2) -- Kuadratik
def bubble_sort(data):
    n = len(data)
    for i in range(n):            # Loop luar: n kali
        for j in range(n - 1 - i):  # Loop dalam: n kali
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data
```

### 4. Menghitung Big-O dari Kode (CPMK-7.2)

**Latihan analisis -- tentukan Big-O:**

```python
# Soal 1: Berapa kompleksitasnya?
def mystery_a(n):
    total = 0           # O(1)
    for i in range(n):  # O(n)
        total += i      # O(1)
    return total         # O(1)
# Jawaban: O(n)

# Soal 2: Berapa kompleksitasnya?
def mystery_b(data):
    n = len(data)
    for i in range(n):          # O(n)
        for j in range(n):      # O(n)
            print(data[i], data[j])  # O(1)
# Jawaban: O(n^2)

# Soal 3: Berapa kompleksitasnya?
def mystery_c(n):
    i = n
    while i > 1:   # Berapa kali loop berjalan?
        i = i // 2
# Jawaban: O(log n) -- karena i dibagi 2 setiap iterasi
```

### 5. Space Complexity dan Trade-off (CPMK-7.4)

**Space complexity** mengukur jumlah memori tambahan yang digunakan algoritma relatif terhadap ukuran input.

| Algoritma | Time Complexity | Space Complexity | Trade-off |
|-----------|----------------|-----------------|-----------|
| Bubble Sort | O(n^2) | O(1) | Lambat, hemat memori |
| Merge Sort | O(n log n) | O(n) | Cepat, butuh memori ekstra |
| Memoization Fibonacci | O(n) | O(n) | Cepat, butuh cache |
| Recursive Fibonacci | O(2^n) | O(n) | Sangat lambat, stack depth |

**Contoh optimasi dengan memoization:**

```python
# Tanpa optimasi: O(2^n) -- sangat lambat
def fib_rekursif(n):
    if n <= 1:
        return n
    return fib_rekursif(n - 1) + fib_rekursif(n - 2)

# Dengan memoization: O(n) -- jauh lebih cepat
def fib_memo(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]
```

### 6. Review Kompleksitas Algoritma Sepanjang Semester (CPMK-7.3)

| Minggu | Algoritma/Operasi | Time Complexity | Space Complexity |
|--------|-------------------|----------------|-----------------|
| 5 | Linear Search | O(n) | O(1) |
| 5 | Binary Search | O(log n) | O(1) |
| 9 | Bubble Sort | O(n^2) | O(1) |
| 9 | Selection Sort | O(n^2) | O(1) |
| 10 | Merge Sort | O(n log n) | O(n) |
| 10 | Quick Sort | O(n log n) avg | O(log n) |
| 11 | Stack push/pop | O(1) | O(n) |
| 11 | Queue enqueue/dequeue | O(1) | O(n) |
| 12 | Dictionary lookup | O(1) avg | O(n) |

### 7. Contoh Optimasi Kode (CPMK-7.4)

```python
import time

# Versi lambat: O(n^2) -- cek duplikat dengan nested loop
def cek_duplikat_lambat(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return True
    return False

# Versi cepat: O(n) -- cek duplikat dengan set
def cek_duplikat_cepat(data):
    return len(data) != len(set(data))

# Pengukuran waktu
data_besar = list(range(10000)) + [0]  # Duplikat di akhir
start = time.time()
cek_duplikat_lambat(data_besar)
print(f"Lambat: {time.time() - start:.4f} detik")

start = time.time()
cek_duplikat_cepat(data_besar)
print(f"Cepat: {time.time() - start:.6f} detik")
```

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)

1. Menonton video "Big-O Notation in 5 Minutes" dan mencatat 3 poin utama (8 menit)
2. Membaca ringkasan tentang mengapa performa algoritma penting dalam industri software (7 menit)

### In-class (120 menit)

| Waktu | Kegiatan | Metode |
|-------|----------|--------|
| 0--25 menit | Ceramah: Mengapa efisiensi penting, notasi Big-O formal dan informal, aturan perhitungan | Ceramah interaktif dengan visualisasi kurva pertumbuhan |
| 25--45 menit | Ceramah: Kelas-kelas kompleksitas umum dengan contoh kode Python | Ceramah dan demonstrasi kode |
| 45--65 menit | Latihan: Menganalisis potongan kode dan menentukan Big-O (6 soal bertingkat) | Praktik terbimbing |
| 65--80 menit | Ceramah: Space complexity, trade-off waktu vs ruang, memoization | Ceramah interaktif |
| 80--100 menit | Lab: Pengukuran waktu eksekusi -- membandingkan linear search vs binary search, bubble sort vs merge sort pada berbagai ukuran data | Eksperimen performa (praktik mandiri) |
| 100--120 menit | Tantangan optimasi: Diberikan 3 kode tidak efisien, mahasiswa mengoptimasi dan mengukur peningkatan performa | Tantangan kelompok |

### Post-class (15 menit)

1. Mengerjakan 5 soal analisis Big-O dari kode Python yang diberikan di LMS (10 menit)
2. Menuliskan ringkasan pribadi: tabel kompleksitas semua algoritma yang dipelajari semester ini (5 menit)

---

## Penugasan

**Tugas Minggu 13: Analisis dan Optimasi Kompleksitas**

1. Tentukan Big-O (time dan space) dari 5 potongan kode yang diberikan, sertakan penjelasan langkah demi langkah
2. Diberikan sebuah fungsi Python yang tidak efisien, tuliskan versi optimal-nya dan ukur perbedaan waktu eksekusi menggunakan modul `time`
3. Buat tabel ringkasan seluruh algoritma yang dipelajari dari Minggu 1--13 beserta kompleksitasnya

**Deadline:** Sebelum pertemuan Minggu 14.

---

## Referensi

1. Gaddis, T. (2021). *Starting Out with Python*, 5th Edition. Pearson. -- Bab 12 (Recursion) dan Appendix tentang Algorithm Analysis.
2. Cormen, T. H., et al. (2022). *Introduction to Algorithms*, 4th Edition. MIT Press. -- Bab 3: Growth of Functions.
3. Zelle, J. (2016). *Python Programming: An Introduction to Computer Science*, 3rd Edition. Franklin, Beedle & Associates. -- Bab 13.
4. Sweigart, A. (2020). *Beyond the Basic Stuff with Python*. No Starch Press. -- Bab 13: Big-O.
5. Big-O Cheat Sheet: [https://www.bigocheatsheet.com/](https://www.bigocheatsheet.com/)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
