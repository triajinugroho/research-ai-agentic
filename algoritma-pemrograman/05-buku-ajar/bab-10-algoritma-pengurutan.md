# BAB 10: ALGORITMA PENGURUTAN (SORTING)

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| CPMK-6.3 | Memahami konsep sorting dan mengapa pengurutan penting | C2 (Memahami) |
| CPMK-6.4 | Mengimplementasikan bubble sort, selection sort, dan insertion sort | C3 (Menerapkan) |
| CPMK-6.5 | Menganalisis dan membandingkan performa algoritma pengurutan | C4 (Menganalisis) |
| CPMK-6.6 | Mengevaluasi pemilihan algoritma sorting berdasarkan konteks | C5 (Mengevaluasi) |

**Estimasi Waktu:** 3 × 50 menit (3 SKS)

**Prasyarat:** Mahasiswa telah memahami materi Bab 1–9 (terutama Bab 7 untuk list dan Bab 9 untuk searching).

---

## 10.1 Mengapa Pengurutan Penting?

### 10.1.1 Pengurutan dalam Kehidupan Sehari-hari

Kita melakukan sorting setiap hari tanpa menyadarinya:
- **Ranking sekolah/universitas** — diurutkan berdasarkan nilai akreditasi
- **Leaderboard game** — diurutkan berdasarkan skor tertinggi
- **Playlist musik** — diurutkan berdasarkan artis/album/tahun
- **E-commerce** — urutkan produk berdasarkan harga, rating, terbaru
- **Hasil Google** — diurutkan berdasarkan relevansi

### 10.1.2 Pengurutan dalam Komputasi

Sorting adalah salah satu operasi paling fundamental dalam computer science:
- **Pencarian lebih cepat** — binary search memerlukan data terurut (Bab 9)
- **Presentasi data** — laporan, tabel, grafik membutuhkan data terurut
- **Eliminasi duplikat** — lebih mudah pada data terurut
- **Analisis data** — median, persentil, ranking memerlukan sorting

> **Fakta:** Diperkirakan 25-50% waktu komputasi di dunia dihabiskan untuk sorting!

---

## 10.2 Bubble Sort

### 10.2.1 Konsep dan Analogi

**Bubble Sort** bekerja dengan membandingkan **dua elemen bersebelahan** dan menukarnya jika urutannya salah. Elemen terbesar "menggelembung" (*bubble*) ke posisi akhir, seperti gelembung udara yang naik ke permukaan air.

### 10.2.2 Algoritma

```
ALGORITMA BubbleSort(A, n):
    UNTUK i ← 0 SAMPAI n-2:
        UNTUK j ← 0 SAMPAI n-2-i:
            JIKA A[j] > A[j+1]:
                tukar A[j] dan A[j+1]
```

### 10.2.3 Trace Table

Data awal: `[64, 34, 25, 12, 22]`

**Pass 1:** (bandingkan dan tukar elemen bersebelahan)

```
[64, 34, 25, 12, 22]  ← bandingkan 64 > 34? Ya → tukar
[34, 64, 25, 12, 22]  ← bandingkan 64 > 25? Ya → tukar
[34, 25, 64, 12, 22]  ← bandingkan 64 > 12? Ya → tukar
[34, 25, 12, 64, 22]  ← bandingkan 64 > 22? Ya → tukar
[34, 25, 12, 22, 64]  ← 64 sudah di posisi benar ✓
```

**Pass 2:**

```
[34, 25, 12, 22, 64]  ← 34 > 25? Ya → tukar
[25, 34, 12, 22, 64]  ← 34 > 12? Ya → tukar
[25, 12, 34, 22, 64]  ← 34 > 22? Ya → tukar
[25, 12, 22, 34, 64]  ← 34 sudah di posisi benar ✓
```

**Pass 3:**

```
[25, 12, 22, 34, 64]  ← 25 > 12? Ya → tukar
[12, 25, 22, 34, 64]  ← 25 > 22? Ya → tukar
[12, 22, 25, 34, 64]  ← 25 sudah di posisi benar ✓
```

**Pass 4:**

```
[12, 22, 25, 34, 64]  ← 12 > 22? Tidak → tidak tukar
[12, 22, 25, 34, 64]  ← Sudah terurut! ✓
```

### 10.2.4 Implementasi Python

```python
def bubble_sort(arr):
    """
    Mengurutkan list menggunakan Bubble Sort (ascending).

    Parameters:
        arr (list): List yang akan diurutkan

    Returns:
        list: List yang sudah terurut
    """
    n = len(arr)
    data = arr.copy()  # jangan ubah list asli

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data

# Test
nilai = [64, 34, 25, 12, 22]
hasil = bubble_sort(nilai)
print(f"Sebelum: {nilai}")
print(f"Sesudah: {hasil}")
```

### 10.2.5 Optimasi: Flag Swapped

Jika dalam satu pass **tidak ada penukaran**, data sudah terurut — bisa berhenti lebih awal:

```python
def bubble_sort_optimized(arr):
    """Bubble Sort dengan optimasi early termination."""
    n = len(arr)
    data = arr.copy()

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        if not swapped:
            break  # data sudah terurut!

    return data
```

### 10.2.6 Analisis Kompleksitas

| Kasus | Kompleksitas | Penjelasan |
|-------|-------------|------------|
| **Best case** | O(n) | Data sudah terurut (dengan optimasi flag) |
| **Average case** | O(n²) | Data acak |
| **Worst case** | O(n²) | Data terurut terbalik |
| **Space** | O(1) | In-place (hanya butuh variabel temp) |
| **Stable?** | Ya | Elemen yang sama mempertahankan urutan relatif |

---

## 10.3 Selection Sort

### 10.3.1 Konsep dan Analogi

**Selection Sort** bekerja dengan mencari elemen **terkecil** dari bagian yang belum terurut, lalu menempatkannya di posisi yang benar. Analoginya: Anda memilih kartu terkecil dari tangan, letakkan di kiri, lalu cari terkecil berikutnya, dan seterusnya.

### 10.3.2 Algoritma

```
ALGORITMA SelectionSort(A, n):
    UNTUK i ← 0 SAMPAI n-2:
        min_idx ← i
        UNTUK j ← i+1 SAMPAI n-1:
            JIKA A[j] < A[min_idx]:
                min_idx ← j
        tukar A[i] dan A[min_idx]
```

### 10.3.3 Trace Table

Data awal: `[64, 25, 12, 22, 11]`

```
Pass 1: Cari minimum dari index 0-4
  Minimum = 11 (index 4)
  Tukar A[0] dan A[4]: [11, 25, 12, 22, 64]
                         ▲ terurut

Pass 2: Cari minimum dari index 1-4
  Minimum = 12 (index 2)
  Tukar A[1] dan A[2]: [11, 12, 25, 22, 64]
                         ▲───▲ terurut

Pass 3: Cari minimum dari index 2-4
  Minimum = 22 (index 3)
  Tukar A[2] dan A[3]: [11, 12, 22, 25, 64]
                         ▲───▲───▲ terurut

Pass 4: Cari minimum dari index 3-4
  Minimum = 25 (index 3, sudah di posisi benar)
  Tidak ada tukar:      [11, 12, 22, 25, 64]
                         ▲───▲───▲───▲───▲ TERURUT!
```

### 10.3.4 Implementasi Python

```python
def selection_sort(arr):
    """
    Mengurutkan list menggunakan Selection Sort (ascending).

    Parameters:
        arr (list): List yang akan diurutkan

    Returns:
        list: List yang sudah terurut
    """
    n = len(arr)
    data = arr.copy()

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        # Tukar elemen terkecil ke posisi i
        data[i], data[min_idx] = data[min_idx], data[i]

    return data

# Test
nilai = [64, 25, 12, 22, 11]
hasil = selection_sort(nilai)
print(f"Sebelum: {nilai}")
print(f"Sesudah: {hasil}")
```

### 10.3.5 Analisis Kompleksitas

| Kasus | Kompleksitas | Penjelasan |
|-------|-------------|------------|
| **Best case** | O(n²) | Selalu melakukan n(n-1)/2 perbandingan |
| **Average case** | O(n²) | Sama |
| **Worst case** | O(n²) | Sama |
| **Space** | O(1) | In-place |
| **Stable?** | Tidak | Penukaran bisa mengubah urutan relatif |
| **Jumlah swap** | O(n) | Maksimal n-1 swap (lebih sedikit dari Bubble) |

---

## 10.4 Insertion Sort

### 10.4.1 Konsep dan Analogi

**Insertion Sort** bekerja seperti **menyortir kartu di tangan**: Anda mengambil satu kartu baru dari tumpukan dan **menyisipkannya** di posisi yang tepat di antara kartu yang sudah terurut.

### 10.4.2 Algoritma

```
ALGORITMA InsertionSort(A, n):
    UNTUK i ← 1 SAMPAI n-1:
        key ← A[i]
        j ← i - 1
        SELAMA j >= 0 DAN A[j] > key:
            A[j+1] ← A[j]
            j ← j - 1
        A[j+1] ← key
```

### 10.4.3 Trace Table

Data awal: `[12, 11, 13, 5, 6]`

```
                      │ terurut │ belum terurut
                      │         │
Pass 1: key = 11      │   [12]  │ [11, 13, 5, 6]
  11 < 12 → geser 12  │         │
  Sisipkan 11:        │[11, 12] │ [13, 5, 6]
                      │         │
Pass 2: key = 13      │[11, 12] │ [13, 5, 6]
  13 > 12 → sudah ok  │         │
  Sisipkan 13:        │[11,12,13]│ [5, 6]
                      │         │
Pass 3: key = 5       │[11,12,13]│ [5, 6]
  5 < 13 → geser 13   │         │
  5 < 12 → geser 12   │         │
  5 < 11 → geser 11   │         │
  Sisipkan 5:         │[5,11,12,13]│ [6]
                      │         │
Pass 4: key = 6       │[5,11,12,13]│ [6]
  6 < 13 → geser 13   │         │
  6 < 12 → geser 12   │         │
  6 < 11 → geser 11   │         │
  6 > 5 → stop        │         │
  Sisipkan 6:         │[5,6,11,12,13]│ TERURUT!
```

### 10.4.4 Implementasi Python

```python
def insertion_sort(arr):
    """
    Mengurutkan list menggunakan Insertion Sort (ascending).

    Parameters:
        arr (list): List yang akan diurutkan

    Returns:
        list: List yang sudah terurut
    """
    n = len(arr)
    data = arr.copy()

    for i in range(1, n):
        key = data[i]
        j = i - 1

        # Geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        # Sisipkan key di posisi yang tepat
        data[j + 1] = key

    return data

# Test
nilai = [12, 11, 13, 5, 6]
hasil = insertion_sort(nilai)
print(f"Sebelum: {nilai}")
print(f"Sesudah: {hasil}")
```

### 10.4.5 Analisis Kompleksitas

| Kasus | Kompleksitas | Penjelasan |
|-------|-------------|------------|
| **Best case** | O(n) | Data sudah terurut (inner loop tidak jalan) |
| **Average case** | O(n²) | Data acak |
| **Worst case** | O(n²) | Data terurut terbalik |
| **Space** | O(1) | In-place |
| **Stable?** | Ya | Elemen sama mempertahankan urutan relatif |
| **Adaptive?** | Ya | Cepat untuk data yang hampir terurut |

---

## 10.5 Perbandingan Tiga Algoritma

### 10.5.1 Tabel Perbandingan

| Aspek | Bubble Sort | Selection Sort | Insertion Sort |
|-------|-------------|---------------|----------------|
| **Best case** | O(n)* | O(n²) | O(n) |
| **Average case** | O(n²) | O(n²) | O(n²) |
| **Worst case** | O(n²) | O(n²) | O(n²) |
| **Space** | O(1) | O(1) | O(1) |
| **Stable** | Ya | Tidak | Ya |
| **Adaptive** | Ya* | Tidak | Ya |
| **Jumlah swap** | Banyak | Sedikit (≤ n-1) | Sedikit |
| **Cocok untuk** | Edukasi | Data kecil | Data hampir terurut |

*Dengan optimasi flag swapped

### 10.5.2 Kapan Menggunakan Masing-masing

- **Bubble Sort**: Untuk pemahaman konsep dasar sorting. Jarang digunakan di produksi.
- **Selection Sort**: Ketika jumlah swap harus minimal (misal: menulis ke media yang lambat).
- **Insertion Sort**: Untuk data kecil atau data yang hampir terurut. Sering digunakan sebagai bagian dari algoritma sorting yang lebih kompleks (Timsort).

### 10.5.3 Pengukuran Waktu Eksekusi

```python
import time
import random

def ukur_waktu(fungsi_sort, data):
    """Mengukur waktu eksekusi fungsi sorting."""
    start = time.time()
    fungsi_sort(data)
    end = time.time()
    return end - start

# Generate data acak
ukuran = [100, 500, 1000, 2000]

print(f"{'n':>6} {'Bubble':>10} {'Selection':>10} {'Insertion':>10}")
print("-" * 40)

for n in ukuran:
    data = [random.randint(1, 10000) for _ in range(n)]

    t_bubble = ukur_waktu(bubble_sort, data)
    t_selection = ukur_waktu(selection_sort, data)
    t_insertion = ukur_waktu(insertion_sort, data)

    print(f"{n:>6} {t_bubble:>10.4f}s {t_selection:>10.4f}s {t_insertion:>10.4f}s")
```

---

## 10.6 Built-in Sorting Python

### 10.6.1 sorted() dan .sort()

```python
nilai = [85, 62, 78, 95, 58, 88]

# sorted() — mengembalikan list baru (original tidak berubah)
terurut = sorted(nilai)
print(f"Original: {nilai}")     # [85, 62, 78, 95, 58, 88]
print(f"Terurut:  {terurut}")   # [58, 62, 78, 85, 88, 95]

# .sort() — mengubah list asli (in-place)
nilai.sort()
print(f"Setelah .sort(): {nilai}")  # [58, 62, 78, 85, 88, 95]
```

### 10.6.2 Parameter key dan reverse

```python
# Urutkan descending (terbesar ke terkecil)
nilai = [85, 62, 78, 95, 58]
print(sorted(nilai, reverse=True))  # [95, 88, 85, 78, 62, 58]

# Urutkan string berdasarkan panjang
kata = ["Python", "AI", "Algoritma", "Data", "Pemrograman"]
print(sorted(kata, key=len))
# ['AI', 'Data', 'Python', 'Algoritma', 'Pemrograman']

# Urutkan case-insensitive
nama = ["ahmad", "Siti", "BUDI", "dewi"]
print(sorted(nama, key=str.lower))
# ['ahmad', 'BUDI', 'dewi', 'Siti']
```

### 10.6.3 Sorting Objek Kompleks

```python
# List of tuples
mahasiswa = [
    ("Ahmad", 85),
    ("Siti", 92),
    ("Budi", 78),
    ("Dewi", 95),
    ("Fatimah", 88),
]

# Urutkan berdasarkan nilai (elemen index 1)
by_nilai = sorted(mahasiswa, key=lambda x: x[1], reverse=True)
for nama, nilai in by_nilai:
    print(f"  {nama}: {nilai}")

# List of dicts
produk = [
    {"nama": "Indomie", "harga": 3500},
    {"nama": "Aqua", "harga": 4000},
    {"nama": "Chitato", "harga": 10000},
    {"nama": "Teh Botol", "harga": 5000},
]

by_harga = sorted(produk, key=lambda x: x["harga"])
for p in by_harga:
    print(f"  {p['nama']}: Rp {p['harga']:,}")
```

### 10.6.4 Timsort: Algoritma di Balik Python Sort

Python menggunakan **Timsort** — algoritma hybrid yang menggabungkan **merge sort** dan **insertion sort**:

| Aspek | Timsort |
|-------|---------|
| **Diciptakan oleh** | Tim Peters (2002, untuk Python) |
| **Kompleksitas** | O(n log n) average dan worst case |
| **Best case** | O(n) (data hampir terurut) |
| **Space** | O(n) |
| **Stable** | Ya |

> Timsort sangat efisien untuk data dunia nyata yang sering memiliki "runs" (bagian yang sudah terurut). Ini jauh lebih cepat dari bubble/selection/insertion sort untuk data besar.

---

## 10.7 Studi Kasus

### 10.7.1 Mengurutkan Data Mahasiswa berdasarkan IPK

```python
def ranking_mahasiswa(data):
    """Membuat ranking mahasiswa berdasarkan IPK (tertinggi)."""
    # Sorting menggunakan built-in sorted
    ranking = sorted(data, key=lambda x: x["ipk"], reverse=True)

    print(f"\n{'Rank':>4} {'Nama':<20} {'NIM':<12} {'IPK':>5}")
    print("-" * 45)
    for i, mhs in enumerate(ranking, 1):
        print(f"{i:>4} {mhs['nama']:<20} {mhs['nim']:<12} {mhs['ipk']:>5.2f}")

data_mahasiswa = [
    {"nama": "Ahmad Fauzan", "nim": "2025001", "ipk": 3.75},
    {"nama": "Siti Aminah", "nim": "2025002", "ipk": 3.90},
    {"nama": "Budi Santoso", "nim": "2025003", "ipk": 3.45},
    {"nama": "Dewi Kartika", "nim": "2025004", "ipk": 3.95},
    {"nama": "Fatimah Zahra", "nim": "2025005", "ipk": 3.80},
]

ranking_mahasiswa(data_mahasiswa)
```

### 10.7.2 Sorting dengan Visualisasi Step-by-Step

```python
def bubble_sort_visual(arr):
    """Bubble Sort dengan visualisasi setiap langkah."""
    n = len(arr)
    data = arr.copy()
    print(f"Data awal: {data}\n")

    for i in range(n - 1):
        print(f"--- Pass {i + 1} ---")
        swapped = False
        for j in range(n - 1 - i):
            # Tampilkan perbandingan
            simbol = ">" if data[j] > data[j+1] else "≤"
            aksi = "TUKAR" if data[j] > data[j+1] else "ok"
            print(f"  {data[j]} {simbol} {data[j+1]} → {aksi}")

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        print(f"  Hasil: {data}")
        if not swapped:
            print("  (Tidak ada pertukaran — selesai!)")
            break

    print(f"\nHasil akhir: {data}")
    return data

bubble_sort_visual([5, 3, 8, 1, 2])
```

---

## AI Corner: AI untuk Memahami Algoritma Sorting

**Level: Lanjut**

### Meminta AI Menjelaskan Trace Step-by-Step

```
Prompt: "Jelaskan step-by-step bagaimana insertion sort
mengurutkan data [38, 27, 43, 3, 9, 82, 10].
Tunjukkan keadaan array setelah setiap pass."
```

### Meminta AI Membandingkan Algoritma

```
Prompt: "Bandingkan bubble sort, selection sort, dan
insertion sort. Buat tabel perbandingan time complexity,
space complexity, stability, dan kapan masing-masing
paling cocok digunakan."
```

### Memvalidasi Implementasi

Setelah AI generate kode sorting:
1. Trace manual dengan data kecil (5 elemen)
2. Test dengan data terurut (best case)
3. Test dengan data terbalik (worst case)
4. Test dengan data yang sama semua
5. Bandingkan output dengan `sorted()`

---

## Latihan Soal

### Tingkat Dasar

1. Trace bubble sort step-by-step untuk data `[5, 1, 4, 2, 8]`. Tunjukkan keadaan array setelah setiap pass.

2. Trace selection sort untuk data `[29, 10, 14, 37, 13]`. Tunjukkan minimum yang ditemukan dan penukaran di setiap pass.

3. Trace insertion sort untuk data `[7, 3, 5, 1, 9, 2]`. Tunjukkan key dan posisi penyisipan di setiap pass.

4. Berapa jumlah perbandingan dan penukaran untuk bubble sort pada data `[4, 3, 2, 1]` (worst case)?

5. Gunakan `sorted()` untuk mengurutkan list `["Dewi", "ahmad", "BUDI", "siti"]` secara case-insensitive.

### Tingkat Menengah

1. Implementasikan bubble sort yang bisa mengurutkan ascending atau descending berdasarkan parameter.

2. Implementasikan selection sort yang menampilkan trace (keadaan array setiap pass).

3. Buatlah program yang mengurutkan list of tuples `[(nama, nilai)]` berdasarkan nilai tertinggi menggunakan insertion sort yang Anda implementasikan sendiri.

4. Bandingkan waktu eksekusi bubble, selection, dan insertion sort untuk data acak ukuran 500, 1000, dan 2000 elemen. Tampilkan hasilnya dalam tabel.

5. Implementasikan fungsi `is_sorted(arr)` yang mengembalikan `True` jika list sudah terurut (ascending). Gunakan fungsi ini untuk memverifikasi implementasi sorting Anda.

### Tingkat Mahir

1. Implementasikan **cocktail shaker sort** (variasi bubble sort yang bekerja dari dua arah). Bandingkan jumlah pass-nya dengan bubble sort biasa.

2. Buatlah program ranking mahasiswa lengkap: input data (nama, NIM, nilai UTS, UAS), hitung rata-rata, urutkan berdasarkan rata-rata (descending), tampilkan ranking dengan format tabel. Implementasikan menggunakan insertion sort manual DAN built-in sorted, bandingkan hasilnya.

3. Buatlah **visualisasi sorting** menggunakan karakter ASCII: setiap elemen direpresentasikan sebagai bar (█) dengan panjang sesuai nilainya. Tampilkan visualisasi setelah setiap pass untuk bubble sort.

---

## Rangkuman

- **Sorting** adalah proses mengurutkan data berdasarkan kriteria tertentu.
- **Bubble Sort**: bandingkan elemen bersebelahan dan tukar. Best O(n), Worst O(n²). Stable.
- **Selection Sort**: cari minimum, tempatkan di posisi benar. Always O(n²). Jumlah swap minimal.
- **Insertion Sort**: sisipkan elemen ke posisi yang tepat. Best O(n), Worst O(n²). Cocok untuk data hampir terurut.
- Semua tiga algoritma memiliki **space complexity O(1)** (in-place).
- Python built-in `sorted()` dan `.sort()` menggunakan **Timsort** — O(n log n).
- Parameter `key` pada sorted/sort memungkinkan sorting berdasarkan kriteria kustom.
- Parameter `reverse=True` untuk urutan descending.
- Pilihan algoritma bergantung pada **ukuran data**, **kondisi data**, dan **kebutuhan stabilitas**.

---

## Referensi

1. Cormen, T. H. et al. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
2. Sedgewick, R. & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley.
3. Bhargava, A. (2016). *Grokking Algorithms*. Manning Publications.
4. Python Software Foundation. (2026). Sorting HOW TO. https://docs.python.org/3/howto/sorting.html
5. Downey, A. B. (2024). *Think Python* (3rd ed.). O'Reilly Media.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
