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
| **Metode** | Ceramah interaktif, Visualisasi, Analisis kode, Praktik |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Menjelaskan** mengapa efisiensi algoritma penting dan bagaimana notasi Big-O digunakan untuk mengukur kompleksitas waktu dan ruang (CPMK-7.1)
2. **Mengklasifikasikan** algoritma ke dalam kelas kompleksitas yang sesuai: O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n) (CPMK-7.2)
3. **Menganalisis** potongan kode Python untuk menentukan kompleksitas Big-O secara sistematis (CPMK-7.3)
4. **Mengevaluasi** trade-off antara kompleksitas waktu dan ruang serta menerapkan teknik optimasi pada algoritma yang telah dipelajari (CPMK-7.4)

---

## Materi Pembelajaran

### 1. Mengapa Efisiensi Algoritma Penting? (CPMK-7.1)

Dua algoritma yang menghasilkan output benar bisa memiliki kinerja yang sangat berbeda. Bayangkan mencari nama di buku telepon 1 juta entri:

- **Linear Search** -- periksa satu per satu: hingga 1.000.000 langkah
- **Binary Search** -- bagi dua berulang: maksimal 20 langkah

Perbedaan ini semakin dramatis seiring bertambahnya ukuran data. Di dunia nyata, aplikasi yang lambat kehilangan pengguna, server yang tidak efisien membuang energi, dan sistem kritis bisa gagal memenuhi tenggat waktu.

**Pengukuran efisiensi:**

- **Kompleksitas Waktu (Time Complexity)** -- berapa banyak operasi dasar yang diperlukan relatif terhadap ukuran input *n*
- **Kompleksitas Ruang (Space Complexity)** -- berapa banyak memori tambahan yang diperlukan relatif terhadap ukuran input *n*
- Fokus pada **worst-case** (kasus terburuk) sebagai jaminan performa

### 2. Notasi Big-O: Definisi Formal dan Informal (CPMK-7.1)

**Definisi informal:** Big-O menggambarkan laju pertumbuhan jumlah operasi seiring bertambahnya ukuran input. Kita mengabaikan konstanta dan suku-suku yang lebih kecil.

**Definisi formal:** f(n) = O(g(n)) jika terdapat konstanta positif *c* dan *n0* sedemikian hingga f(n) <= c * g(n) untuk semua n >= n0.

**Aturan penyederhanaan:**

- Abaikan konstanta pengali: 5n -> O(n)
- Ambil suku dominan: n^2 + 3n + 7 -> O(n^2)
- Operasi berurutan dijumlahkan: O(n) + O(n^2) -> O(n^2)
- Operasi bersarang dikalikan: loop O(n) di dalam loop O(n) -> O(n^2)

### 3. Kelas Kompleksitas Umum (CPMK-7.2)

| Notasi | Nama | Contoh Algoritma | n=10 | n=1.000 | n=1.000.000 |
|--------|------|------------------|------|---------|-------------|
| O(1) | Konstan | Akses indeks list | 1 | 1 | 1 |
| O(log n) | Logaritmik | Binary Search | 3 | 10 | 20 |
| O(n) | Linear | Linear Search | 10 | 1.000 | 1.000.000 |
| O(n log n) | Linearitmik | Merge Sort, Timsort | 33 | 10.000 | 20.000.000 |
| O(n^2) | Kuadratik | Bubble Sort, Selection Sort | 100 | 1.000.000 | 10^12 |
| O(2^n) | Eksponensial | Brute-force subset | 1.024 | ~10^301 | -- |

**Urutan dari tercepat ke terlambat:**

O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n)

### 4. Menghitung Big-O dari Kode Python (CPMK-7.3)

**Contoh 1 -- O(1): Akses langsung**

```python
def ambil_elemen(data, index):
    return data[index]  # Satu operasi, tidak tergantung ukuran data
```

**Contoh 2 -- O(n): Satu loop**

```python
def cari_linear(data, target):
    for item in data:       # Loop n kali
        if item == target:  # O(1) per iterasi
            return True
    return False
# Total: O(n)
```

**Contoh 3 -- O(n^2): Loop bersarang**

```python
def bubble_sort(data):
    n = len(data)
    for i in range(n):              # Loop luar: n kali
        for j in range(n - 1 - i):  # Loop dalam: ~n kali
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
# Total: O(n) * O(n) = O(n^2)
```

**Contoh 4 -- O(log n): Pembagian berulang**

```python
def binary_search(data, target):
    low, high = 0, len(data) - 1
    while low <= high:                  # Setiap iterasi membagi ruang pencarian menjadi setengah
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
# Total: O(log n)
```

### 5. Kompleksitas Ruang (Space Complexity) (CPMK-7.3)

Selain waktu, kita juga menganalisis memori tambahan yang digunakan:

```python
# O(1) space -- in-place
def tukar(data, i, j):
    data[i], data[j] = data[j], data[i]

# O(n) space -- membuat list baru
def duplikat(data):
    hasil = []
    for item in data:
        hasil.append(item)
        hasil.append(item)
    return hasil
```

### 6. Trade-off Waktu vs Ruang (CPMK-7.4)

Seringkali kita bisa mempercepat waktu dengan mengorbankan memori, atau sebaliknya:

| Pendekatan | Waktu | Ruang | Contoh |
|------------|-------|-------|--------|
| Brute-force cek duplikat | O(n^2) | O(1) | Dua loop bersarang |
| Menggunakan set | O(n) | O(n) | Simpan elemen di set |
| Sorting dulu, lalu cek tetangga | O(n log n) | O(1)* | Sort in-place, cek berdampingan |

```python
# Pendekatan 1: O(n^2) waktu, O(1) ruang
def ada_duplikat_v1(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return True
    return False

# Pendekatan 2: O(n) waktu, O(n) ruang
def ada_duplikat_v2(data):
    dilihat = set()
    for item in data:
        if item in dilihat:
            return True
        dilihat.add(item)
    return False
```

### 7. Review Kompleksitas Algoritma yang Telah Dipelajari (CPMK-7.4)

| Algoritma | Waktu (Best) | Waktu (Worst) | Ruang | Minggu |
|-----------|-------------|---------------|-------|--------|
| Linear Search | O(1) | O(n) | O(1) | 9 |
| Binary Search | O(1) | O(log n) | O(1) | 9 |
| Bubble Sort | O(n) | O(n^2) | O(1) | 10 |
| Selection Sort | O(n^2) | O(n^2) | O(1) | 10 |
| Insertion Sort | O(n) | O(n^2) | O(1) | 10 |
| Merge Sort | O(n log n) | O(n log n) | O(n) | 10 |
| Stack (push/pop) | O(1) | O(1) | O(n) | 11 |
| Queue (enqueue/dequeue) | O(1) | O(1) | O(n) | 11 |

### 8. Teknik Optimasi dan Contoh (CPMK-7.4)

**Mengukur waktu eksekusi di Python:**

```python
import time

def ukur_waktu(fungsi, *args):
    mulai = time.time()
    hasil = fungsi(*args)
    selesai = time.time()
    print(f"Waktu: {selesai - mulai:.6f} detik")
    return hasil

# Contoh: bandingkan dua pendekatan cari duplikat
import random
data_besar = random.sample(range(100_000), 50_000)
ukur_waktu(ada_duplikat_v1, data_besar)  # Lambat (O(n^2))
ukur_waktu(ada_duplikat_v2, data_besar)  # Cepat (O(n))
```

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)

1. Menonton video "Big-O Notation in 5 Minutes" dan mencatat poin-poin kunci (8 menit)
2. Membaca ringkasan tabel kelas kompleksitas dan mencoba menghafal urutannya dari tercepat ke terlambat (7 menit)

### In-class (120 menit)

| Waktu | Kegiatan | Metode |
|-------|----------|--------|
| 0--25 menit | Ceramah: Mengapa efisiensi penting, definisi Big-O formal dan informal, aturan penyederhanaan | Ceramah interaktif dengan visualisasi kurva pertumbuhan |
| 25--45 menit | Ceramah: Kelas kompleksitas umum dengan tabel perbandingan dan contoh algoritma nyata | Ceramah dengan tabel dan grafik |
| 45--70 menit | Latihan terbimbing: Menganalisis 6 potongan kode Python untuk menentukan Big-O masing-masing | Analisis kode bersama |
| 70--80 menit | Diskusi: Trade-off waktu vs ruang -- kapan mengorbankan memori untuk kecepatan? | Diskusi kelas |
| 80--100 menit | Hands-on: Performance timing lab -- mengukur waktu eksekusi berbagai algoritma sorting dan searching pada data berbagai ukuran | Praktik mandiri |
| 100--120 menit | Optimization challenge: Diberikan kode O(n^2), mahasiswa mengoptimasi menjadi O(n) atau O(n log n) | Praktik dan presentasi solusi |

### Post-class (15 menit)

1. Menyelesaikan tabel review kompleksitas untuk semua algoritma yang telah dipelajari di Minggu 9--12 (8 menit)
2. Mengerjakan 3 soal latihan analisis Big-O dari potongan kode yang diberikan di Google Classroom (7 menit)

---

## Penugasan

**Tugas 13: Analisis dan Optimasi Algoritma**

1. Analisis Big-O dari 5 potongan kode yang diberikan (sertakan langkah-langkah penalaran)
2. Diberikan sebuah fungsi Python yang berjalan O(n^2), tulis versi optimasi yang berjalan O(n) dan jelaskan trade-off yang terjadi
3. Jalankan eksperimen timing untuk membandingkan Bubble Sort vs built-in `sorted()` pada data ukuran 1.000, 5.000, dan 10.000 -- sajikan hasil dalam tabel

**Deadline:** Sebelum pertemuan Minggu 14

---

## Referensi

1. Gaddis, T. (2021). *Starting Out with Python*, 5th Edition. Pearson. -- Bab 12 (Recursion) dan Appendix tentang Algorithm Analysis.
2. Zelle, J. (2016). *Python Programming: An Introduction to Computer Science*, 3rd Edition. Franklin, Beedle & Associates. -- Bab 13.
3. Cormen, T. H., et al. (2009). *Introduction to Algorithms*, 3rd Edition. MIT Press. -- Bab 1--3 (Growth of Functions).
4. Big-O Cheat Sheet: [https://www.bigocheatsheet.com/](https://www.bigocheatsheet.com/)
5. Python Time Complexity Wiki: [https://wiki.python.org/moin/TimeComplexity](https://wiki.python.org/moin/TimeComplexity)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
