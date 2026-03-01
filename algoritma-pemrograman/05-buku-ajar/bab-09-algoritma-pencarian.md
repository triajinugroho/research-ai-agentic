# BAB 9: ALGORITMA PENCARIAN (SEARCHING)

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman --- Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| CPMK-6.1 | Menjelaskan konsep dan pentingnya algoritma pencarian dalam pemrograman | C2 --- Memahami |
| CPMK-6.2 | Mengimplementasikan algoritma Linear Search dalam bahasa Python | C3 --- Menerapkan |
| CPMK-6.3 | Mengimplementasikan algoritma Binary Search (iteratif dan rekursif) dalam bahasa Python | C3 --- Menerapkan |
| CPMK-6.4 | Menganalisis dan membandingkan performa algoritma Linear Search dan Binary Search | C4 --- Menganalisis |

---

## Pendahuluan

> *"Mencari jarum dalam tumpukan jerami adalah masalah pencarian klasik.
> Pertanyaannya: apakah kita harus memeriksa satu per satu, atau adakah cara yang lebih cerdas?"*

Pencarian (*searching*) adalah salah satu operasi paling fundamental dalam ilmu komputer.
Hampir setiap aplikasi yang kita gunakan sehari-hari melibatkan proses pencarian data.
Pada bab ini, kita akan mempelajari dua algoritma pencarian utama --- **Linear Search**
dan **Binary Search** --- beserta analisis performa, implementasi Python, dan studi kasus
yang relevan dengan konteks Indonesia.

---

## 9.1 Mengapa Pencarian Penting?

### 9.1.1 Contoh Pencarian dalam Kehidupan Sehari-hari

Pencarian bukanlah konsep yang asing. Kita melakukannya setiap hari, seringkali
tanpa menyadarinya:

1. **Mencari buku di perpustakaan** --- Apakah kita memeriksa setiap rak satu per satu,
   atau langsung menuju ke bagian yang sesuai berdasarkan kode klasifikasi?
2. **Mencari kontak di HP** --- Ketika kita mengetik nama seseorang di kolom pencarian,
   aplikasi langsung menyaring ribuan kontak dalam hitungan milidetik.
3. **Mencari file di komputer** --- Fitur search di file explorer membantu kita menemukan
   file di antara ribuan dokumen yang tersimpan.
4. **Mencari kata di kamus** --- Kita tidak membuka kamus dari halaman pertama; kita
   langsung membuka bagian tengah dan menyesuaikan arah pencarian.

### 9.1.2 Pencarian dalam Konteks Indonesia

- **Dukcapil (Dinas Kependudukan dan Catatan Sipil)**: Mencari data penduduk berdasarkan
  NIK di antara lebih dari 270 juta data warga negara Indonesia.
- **Tokopedia / Shopee**: Ketika pengguna mengetik "sepatu olahraga", sistem harus mencari
  dan menampilkan jutaan produk yang relevan dalam waktu kurang dari 1 detik.
- **SIAK (Sistem Informasi Akademik)**: Mencari data mahasiswa berdasarkan NIM atau nama
  dari database universitas.
- **e-KTP**: Verifikasi identitas melalui pencarian data biometrik.

### 9.1.3 Pencarian dalam Skala Global

Google memproses lebih dari **8,5 miliar pencarian per hari** (2024). Setiap pencarian
melibatkan algoritma yang sangat kompleks untuk menemukan halaman web yang paling relevan
dari miliaran halaman yang terindeks. Meskipun algoritma Google jauh lebih kompleks dari
yang akan kita pelajari, fondasi dasarnya tetap sama: **bagaimana menemukan data yang
dicari secara efisien**.

### 9.1.4 Definisi Formal

**Masalah Pencarian (Search Problem)**:
- **Input**: Sebuah koleksi data `D` yang terdiri dari `n` elemen, dan sebuah nilai
  target `T` yang dicari.
- **Output**: Lokasi (indeks) dari `T` di dalam `D`, atau indikasi bahwa `T` tidak
  ditemukan.

Dalam konteks pemrograman Python:

```
Input:  data = [15, 23, 4, 42, 8, 16]
        target = 42

Output: 3  (karena data[3] == 42)
```

---

## 9.2 Linear Search (Sequential Search)

### 9.2.1 Konsep Dasar

**Linear Search** (atau **Sequential Search**) adalah algoritma pencarian paling sederhana.
Cara kerjanya sangat intuitif:

> Periksa setiap elemen satu per satu, dari awal hingga akhir, sampai elemen yang
> dicari ditemukan atau seluruh data telah diperiksa.

Analoginya seperti mencari buku tertentu di rak yang belum tersusun rapi --- kita harus
memeriksa setiap buku satu per satu dari kiri ke kanan.

### 9.2.2 Pseudocode

```
ALGORITMA LinearSearch(data, target)
INPUT:  data   = array berisi n elemen
        target = nilai yang dicari
OUTPUT: indeks target jika ditemukan, -1 jika tidak

1. UNTUK i = 0 SAMPAI n-1:
2.     JIKA data[i] == target:
3.         KEMBALIKAN i
4. KEMBALIKAN -1
```

### 9.2.3 Implementasi Python

```python
def linear_search(data, target):
    """Mencari target dalam data secara sequential.

    Args:
        data: List yang akan dicari
        target: Nilai yang dicari

    Returns:
        int: indeks target jika ditemukan, -1 jika tidak
    """
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


# === Contoh Penggunaan ===
nilai = [72, 85, 60, 91, 78, 65, 88, 95, 70, 82]

# Pencarian yang berhasil
hasil = linear_search(nilai, 91)
print(f"Mencari 91: ditemukan di indeks {hasil}")   # Output: 3

# Pencarian yang gagal
hasil = linear_search(nilai, 100)
print(f"Mencari 100: ditemukan di indeks {hasil}")   # Output: -1
```

### 9.2.4 Visualisasi ASCII --- Step by Step

Mari kita telusuri proses pencarian nilai **78** dalam list berikut:

```
data = [72, 85, 60, 91, 78, 65, 88, 95, 70, 82]
target = 78
```

**Langkah 1**: Periksa indeks 0
```
  [72] [85] [60] [91] [78] [65] [88] [95] [70] [82]
   ^
   i=0
   72 == 78? TIDAK --> lanjut
```

**Langkah 2**: Periksa indeks 1
```
  [72] [85] [60] [91] [78] [65] [88] [95] [70] [82]
        ^
        i=1
        85 == 78? TIDAK --> lanjut
```

**Langkah 3**: Periksa indeks 2
```
  [72] [85] [60] [91] [78] [65] [88] [95] [70] [82]
              ^
              i=2
              60 == 78? TIDAK --> lanjut
```

**Langkah 4**: Periksa indeks 3
```
  [72] [85] [60] [91] [78] [65] [88] [95] [70] [82]
                    ^
                    i=3
                    91 == 78? TIDAK --> lanjut
```

**Langkah 5**: Periksa indeks 4
```
  [72] [85] [60] [91] [78] [65] [88] [95] [70] [82]
                          ^
                          i=4
                          78 == 78? YA! --> kembalikan 4
```

**Hasil**: Target 78 ditemukan di **indeks 4** setelah **5 perbandingan**.

### 9.2.5 Trace Table --- Linear Search

Trace table adalah alat yang sangat penting untuk memahami jalannya algoritma secara
detail. Berikut trace table lengkap untuk pencarian di atas:

**Contoh 1**: Mencari target = 78 dalam data = [72, 85, 60, 91, 78, 65, 88, 95, 70, 82]

| Langkah | i | data[i] | data[i] == 78? | Aksi |
|---------|---|---------|----------------|------|
| 1 | 0 | 72 | Tidak | Lanjut ke i+1 |
| 2 | 1 | 85 | Tidak | Lanjut ke i+1 |
| 3 | 2 | 60 | Tidak | Lanjut ke i+1 |
| 4 | 3 | 91 | Tidak | Lanjut ke i+1 |
| 5 | 4 | 78 | **Ya** | **Return 4** |

Total perbandingan: **5**

**Contoh 2**: Mencari target = 50 dalam data = [72, 85, 60, 91, 78, 65, 88, 95, 70, 82]

| Langkah | i | data[i] | data[i] == 50? | Aksi |
|---------|---|---------|----------------|------|
| 1 | 0 | 72 | Tidak | Lanjut ke i+1 |
| 2 | 1 | 85 | Tidak | Lanjut ke i+1 |
| 3 | 2 | 60 | Tidak | Lanjut ke i+1 |
| 4 | 3 | 91 | Tidak | Lanjut ke i+1 |
| 5 | 4 | 78 | Tidak | Lanjut ke i+1 |
| 6 | 5 | 65 | Tidak | Lanjut ke i+1 |
| 7 | 6 | 88 | Tidak | Lanjut ke i+1 |
| 8 | 7 | 95 | Tidak | Lanjut ke i+1 |
| 9 | 8 | 70 | Tidak | Lanjut ke i+1 |
| 10 | 9 | 82 | Tidak | Loop selesai |
| 11 | - | - | - | **Return -1** |

Total perbandingan: **10** (seluruh elemen diperiksa, target tidak ditemukan)

### 9.2.6 Analisis Kompleksitas Linear Search

| Kasus | Kondisi | Jumlah Perbandingan | Big-O |
|-------|---------|---------------------|-------|
| **Best Case** | Target ada di indeks 0 | 1 | O(1) |
| **Worst Case** | Target ada di indeks terakhir atau tidak ada | n | O(n) |
| **Average Case** | Target ada di posisi random | n/2 | O(n) |

**Penjelasan**:
- **Best case O(1)**: Jika target kebetulan berada di elemen pertama, kita hanya perlu
  1 perbandingan. Ini disebut *constant time*.
- **Worst case O(n)**: Jika target berada di elemen terakhir atau tidak ada dalam data,
  kita harus memeriksa seluruh n elemen.
- **Average case O(n/2)**: Secara rata-rata, jika target ada di posisi acak, kita perlu
  memeriksa sekitar setengah dari total elemen. Dalam notasi Big-O, O(n/2) = O(n)
  karena konstanta diabaikan.

### 9.2.7 Kapan Menggunakan Linear Search?

Linear Search cocok digunakan ketika:
- Data **belum terurut** (unsorted)
- Jumlah data **sedikit** (n kecil)
- Pencarian hanya dilakukan **sekali atau jarang**
- Implementasi harus **sesederhana mungkin**

---

## 9.3 Binary Search

### 9.3.1 Konsep Dasar

**Binary Search** adalah algoritma pencarian yang jauh lebih efisien dibandingkan
Linear Search, tetapi memiliki satu prasyarat penting:

> **Data HARUS sudah terurut (sorted) sebelum Binary Search dapat digunakan.**

Ide dasarnya adalah strategi **divide and conquer** (bagi dan taklukkan):

1. Periksa elemen **tengah** dari data.
2. Jika elemen tengah sama dengan target, pencarian selesai.
3. Jika target **lebih kecil** dari elemen tengah, cari di **bagian kiri** (setengah bawah).
4. Jika target **lebih besar** dari elemen tengah, cari di **bagian kanan** (setengah atas).
5. Ulangi proses ini sampai target ditemukan atau ruang pencarian habis.

### 9.3.2 Analogi: Mencari Kata di Kamus

Bayangkan Anda mencari kata **"mangga"** di kamus bahasa Indonesia:

1. Anda **membuka halaman tengah** kamus. Halaman itu menunjukkan kata-kata berawalan "L".
2. "M" ada **setelah** "L", jadi Anda membuang bagian kiri dan **fokus ke bagian kanan**.
3. Anda **membuka tengah** dari bagian kanan. Halaman itu menunjukkan kata berawalan "P".
4. "M" ada **sebelum** "P", jadi Anda membuang bagian kanan dan **fokus ke bagian kiri**.
5. Anda **membuka tengah** lagi dan menemukan kata berawalan "M".
6. Anda terus mempersempit pencarian sampai menemukan kata "mangga".

Setiap langkah **membuang setengah** dari sisa halaman yang harus diperiksa. Inilah
kekuatan Binary Search!

### 9.3.3 Pseudocode

```
ALGORITMA BinarySearch(data, target)
INPUT:  data   = array TERURUT berisi n elemen
        target = nilai yang dicari
OUTPUT: indeks target jika ditemukan, -1 jika tidak

1. low  = 0
2. high = n - 1
3. SELAMA low <= high:
4.     mid = (low + high) // 2
5.     JIKA data[mid] == target:
6.         KEMBALIKAN mid
7.     JIKA data[mid] < target:
8.         low = mid + 1
9.     SELAINNYA:
10.        high = mid - 1
11. KEMBALIKAN -1
```

### 9.3.4 Implementasi Python (Iteratif)

```python
def binary_search(data, target):
    """Binary search pada data yang sudah terurut.

    Args:
        data: List terurut (ascending)
        target: Nilai yang dicari

    Returns:
        int: indeks target jika ditemukan, -1 jika tidak ditemukan
    """
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# === Contoh Penggunaan ===
data_terurut = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

hasil = binary_search(data_terurut, 70)
print(f"Mencari 70: ditemukan di indeks {hasil}")    # Output: 6

hasil = binary_search(data_terurut, 55)
print(f"Mencari 55: ditemukan di indeks {hasil}")    # Output: -1
```

### 9.3.5 Visualisasi ASCII --- Binary Search Step by Step

**Contoh 1**: Mencari target = **70** dalam data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

```
Indeks:  0    1    2    3    4    5    6    7    8    9
Data:  [10] [20] [30] [40] [50] [60] [70] [80] [90] [100]
```

**Langkah 1**: low=0, high=9, mid=(0+9)//2 = 4
```
        [10] [20] [30] [40] [50] [60] [70] [80] [90] [100]
         ^                   ^                          ^
        low                 mid                       high

        data[4] = 50
        50 == 70? TIDAK
        50 <  70? YA --> target di bagian KANAN --> low = mid + 1 = 5
```

**Langkah 2**: low=5, high=9, mid=(5+9)//2 = 7
```
        [10] [20] [30] [40] [50] [60] [70] [80] [90] [100]
                                   ^          ^          ^
                                  low        mid       high

        data[7] = 80
        80 == 70? TIDAK
        80 <  70? TIDAK --> target di bagian KIRI --> high = mid - 1 = 6
```

**Langkah 3**: low=5, high=6, mid=(5+6)//2 = 5
```
        [10] [20] [30] [40] [50] [60] [70] [80] [90] [100]
                                   ^    ^
                               low,mid high

        data[5] = 60
        60 == 70? TIDAK
        60 <  70? YA --> target di bagian KANAN --> low = mid + 1 = 6
```

**Langkah 4**: low=6, high=6, mid=(6+6)//2 = 6
```
        [10] [20] [30] [40] [50] [60] [70] [80] [90] [100]
                                         ^
                                    low,mid,high

        data[6] = 70
        70 == 70? YA! --> DITEMUKAN! Return 6
```

**Hasil**: Target 70 ditemukan di **indeks 6** setelah **4 perbandingan**.
Bandingkan dengan Linear Search yang membutuhkan **7 perbandingan** untuk data ini!

### 9.3.6 Trace Table Detail --- Binary Search

**Contoh 1**: Mencari target = **70** dalam [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

| Langkah | low | high | mid | data[mid] | Perbandingan | Aksi |
|---------|-----|------|-----|-----------|-------------|------|
| 1 | 0 | 9 | 4 | 50 | 50 < 70 | low = 5 |
| 2 | 5 | 9 | 7 | 80 | 80 > 70 | high = 6 |
| 3 | 5 | 6 | 5 | 60 | 60 < 70 | low = 6 |
| 4 | 6 | 6 | 6 | 70 | 70 == 70 | **Return 6** |

Total perbandingan: **4** (dari 10 elemen)

---

**Contoh 2**: Mencari target = **25** dalam [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

| Langkah | low | high | mid | data[mid] | Perbandingan | Aksi |
|---------|-----|------|-----|-----------|-------------|------|
| 1 | 0 | 9 | 4 | 50 | 50 > 25 | high = 3 |
| 2 | 0 | 3 | 1 | 20 | 20 < 25 | low = 2 |
| 3 | 2 | 3 | 2 | 30 | 30 > 25 | high = 1 |
| 4 | 2 | 1 | - | - | low > high | **Return -1** |

Total perbandingan: **3** (target tidak ditemukan)

Visualisasi langkah-langkah:
```
Langkah 1:  [10  20  30  40 |50| 60  70  80  90  100]
              L               M                    H     50 > 25 -> cari kiri

Langkah 2:  [10 |20| 30  40]
              L   M       H                              20 < 25 -> cari kanan

Langkah 3:  [|30| 40]
              L,M  H                                     30 > 25 -> cari kiri

Langkah 4:  low=2 > high=1 --> TIDAK DITEMUKAN
```

---

**Contoh 3**: Mencari target = **10** dalam [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

| Langkah | low | high | mid | data[mid] | Perbandingan | Aksi |
|---------|-----|------|-----|-----------|-------------|------|
| 1 | 0 | 9 | 4 | 50 | 50 > 10 | high = 3 |
| 2 | 0 | 3 | 1 | 20 | 20 > 10 | high = 0 |
| 3 | 0 | 0 | 0 | 10 | 10 == 10 | **Return 0** |

Total perbandingan: **3** (elemen pertama ditemukan dalam 3 langkah, bukan 1!)

> **Catatan Penting**: Pada Binary Search, elemen pertama bukan berarti best case.
> Best case terjadi ketika target kebetulan berada tepat di posisi **mid** pada
> iterasi pertama (yaitu elemen tengah dari data).

### 9.3.7 Mengapa O(log n)? --- Penjelasan Intuitif

Setiap langkah Binary Search **membuang setengah** dari ruang pencarian:

```
Langkah 1: n    elemen  -->  periksa 1, sisa n/2
Langkah 2: n/2  elemen  -->  periksa 1, sisa n/4
Langkah 3: n/4  elemen  -->  periksa 1, sisa n/8
Langkah 4: n/8  elemen  -->  periksa 1, sisa n/16
...
Langkah k: 1    elemen  -->  pencarian selesai
```

Berapa banyak langkah (k) yang diperlukan sampai tersisa 1 elemen?

```
n / 2^k = 1
n = 2^k
k = log2(n)
```

Oleh karena itu, kompleksitas waktu Binary Search adalah **O(log n)**.

**Contoh konkret**: Untuk n = 1.000.000 elemen:
- log2(1.000.000) = 19,93 --> maksimal **20 langkah**!
- Sementara Linear Search membutuhkan hingga **1.000.000 langkah**!

### 9.3.8 Tabel Perbandingan Jumlah Langkah

Tabel berikut menunjukkan betapa dramatisnya perbedaan efisiensi antara Linear Search
dan Binary Search seiring bertambahnya jumlah data:

| Jumlah Data (n) | Linear Search (max) | Binary Search (max) | Rasio |
|------------------|---------------------|---------------------|-------|
| 10 | 10 | 4 | 2,5x |
| 100 | 100 | 7 | 14x |
| 1.000 | 1.000 | 10 | 100x |
| 10.000 | 10.000 | 14 | 714x |
| 100.000 | 100.000 | 17 | 5.882x |
| 1.000.000 | 1.000.000 | 20 | 50.000x |
| 1.000.000.000 | 1.000.000.000 | 30 | 33.333.333x |

> **Bayangkan**: Untuk mencari satu data dari **1 miliar** data, Binary Search hanya
> perlu **30 langkah**. Itulah kekuatan logaritma!

### 9.3.9 Analisis Kompleksitas Binary Search

| Kasus | Kondisi | Big-O |
|-------|---------|-------|
| **Best Case** | Target tepat di posisi mid pertama | O(1) |
| **Worst Case** | Target di ujung atau tidak ada | O(log n) |
| **Average Case** | Target di posisi random | O(log n) |

---

## 9.4 Binary Search Rekursif

### 9.4.1 Konsep

Binary Search dapat juga diimplementasikan secara **rekursif**. Setiap pemanggilan
fungsi memproses setengah dari data, dengan base case ketika `low > high`
(data tidak ditemukan) atau `data[mid] == target` (data ditemukan).

### 9.4.2 Implementasi Python

```python
def binary_search_recursive(data, target, low, high):
    """Binary search secara rekursif pada data terurut.

    Args:
        data: List terurut (ascending)
        target: Nilai yang dicari
        low: Batas bawah pencarian (indeks)
        high: Batas atas pencarian (indeks)

    Returns:
        int: indeks target jika ditemukan, -1 jika tidak ditemukan
    """
    # Base case: ruang pencarian habis
    if low > high:
        return -1

    mid = (low + high) // 2

    if data[mid] == target:
        return mid
    elif data[mid] < target:
        return binary_search_recursive(data, target, mid + 1, high)
    else:
        return binary_search_recursive(data, target, low, mid - 1)


# === Contoh Penggunaan ===
data = [5, 12, 18, 25, 33, 47, 56, 68, 72, 89]

# Panggilan awal: low=0, high=len(data)-1
hasil = binary_search_recursive(data, 47, 0, len(data) - 1)
print(f"Mencari 47: ditemukan di indeks {hasil}")    # Output: 5

hasil = binary_search_recursive(data, 40, 0, len(data) - 1)
print(f"Mencari 40: ditemukan di indeks {hasil}")    # Output: -1
```

### 9.4.3 Trace Pemanggilan Rekursif

Mencari target = **47** dalam data = [5, 12, 18, 25, 33, 47, 56, 68, 72, 89]

```
binary_search_recursive(data, 47, 0, 9)
    mid = 4, data[4] = 33
    33 < 47 --> cari kanan
    |
    +-- binary_search_recursive(data, 47, 5, 9)
            mid = 7, data[7] = 68
            68 > 47 --> cari kiri
            |
            +-- binary_search_recursive(data, 47, 5, 6)
                    mid = 5, data[5] = 47
                    47 == 47 --> DITEMUKAN! Return 5
                    |
                    return 5
            return 5
    return 5
```

### 9.4.4 Perbandingan Iteratif vs Rekursif

| Aspek | Iteratif | Rekursif |
|-------|----------|----------|
| Memori | O(1) --- hanya variabel low, high, mid | O(log n) --- call stack rekursi |
| Kecepatan | Sedikit lebih cepat (tidak ada overhead call stack) | Sedikit lebih lambat |
| Readability | Jelas dan straightforward | Lebih elegan secara konseptual |
| Risiko | Tidak ada risiko stack overflow | Potensi stack overflow untuk data sangat besar |
| Rekomendasi | **Direkomendasikan untuk produksi** | Baik untuk pemahaman konsep |

### 9.4.5 Wrapper Function

Untuk memudahkan penggunaan versi rekursif, kita bisa membuat wrapper function:

```python
def binary_search_rec(data, target):
    """Wrapper untuk binary_search_recursive agar lebih mudah digunakan."""
    return binary_search_recursive(data, target, 0, len(data) - 1)

# Penggunaan menjadi lebih sederhana
hasil = binary_search_rec(data, 47)
```

---

## 9.5 Perbandingan Linear vs Binary Search

### 9.5.1 Tabel Perbandingan Komprehensif

| Aspek | Linear Search | Binary Search |
|-------|--------------|---------------|
| **Prasyarat** | Tidak ada | Data **HARUS** terurut |
| **Strategi** | Sequential (satu per satu) | Divide and conquer (bagi dua) |
| **Best Case** | O(1) | O(1) |
| **Worst Case** | O(n) | O(log n) |
| **Average Case** | O(n) | O(log n) |
| **Memory (iteratif)** | O(1) | O(1) |
| **Memory (rekursif)** | - | O(log n) |
| **Implementasi** | Sangat mudah | Lebih kompleks |
| **Tipe Data** | Semua tipe | Harus *comparable* (bisa dibandingkan) |
| **Efisiensi n besar** | Lambat | Sangat cepat |
| **Biaya persiapan** | Tidak ada | Harus sorting dulu: O(n log n) |
| **Data dinamis** | Cocok | Kurang cocok (harus re-sort) |

### 9.5.2 Kapan Menggunakan Masing-masing?

**Gunakan Linear Search ketika**:
- Data belum terurut dan hanya dicari sekali
- Jumlah data kecil (n < 100)
- Data sering berubah (insert/delete) sehingga menjaga keterurutan mahal
- Kesederhanaan kode lebih penting daripada performa

**Gunakan Binary Search ketika**:
- Data sudah terurut atau akan dicari berkali-kali (sort sekali, search berkali-kali)
- Jumlah data besar (n > 1000)
- Performa pencarian sangat penting (real-time systems)
- Data relatif statis (jarang berubah)

### 9.5.3 Visualisasi Perbandingan

```
Linear Search: Mencari 90 dari 10 elemen
[10] [20] [30] [40] [50] [60] [70] [80] [90] [100]
 (1)  (2)  (3)  (4)  (5)  (6)  (7)  (8)  (9)
                                           ^ FOUND! (9 perbandingan)

Binary Search: Mencari 90 dari 10 elemen
[10] [20] [30] [40] [50] [60] [70] [80] [90] [100]
                      (1)
                                    (2)
                                         (3)
                                           ^ FOUND! (3 perbandingan)

Linear: 9 langkah  vs  Binary: 3 langkah --> Binary 3x lebih cepat
```

---

## 9.6 Python Built-in Search

Python menyediakan beberapa mekanisme pencarian bawaan yang sudah dioptimasi.
Memahami cara kerjanya membantu kita memilih alat yang tepat.

### 9.6.1 Operator `in`

```python
# Operator 'in' untuk memeriksa keberadaan elemen
buah = ["apel", "mangga", "jeruk", "durian", "rambutan"]

if "mangga" in buah:
    print("Mangga tersedia!")    # Output: Mangga tersedia!

if "anggur" not in buah:
    print("Anggur tidak tersedia.")    # Output: Anggur tidak tersedia.
```

> **Catatan**: Untuk `list`, operator `in` menggunakan **Linear Search** di belakang
> layar, sehingga kompleksitasnya **O(n)**. Namun untuk `set` dan `dict`, operator `in`
> menggunakan **hash-based lookup** dengan kompleksitas **O(1)**.

### 9.6.2 Method `list.index()`

```python
buah = ["apel", "mangga", "jeruk", "durian", "rambutan"]

# Mengembalikan indeks elemen
indeks = buah.index("jeruk")
print(f"Jeruk ada di indeks: {indeks}")    # Output: 2

# HATI-HATI: Akan memunculkan ValueError jika tidak ditemukan!
try:
    indeks = buah.index("anggur")
except ValueError:
    print("Anggur tidak ditemukan dalam list")
```

### 9.6.3 Module `bisect` --- Binary Search Bawaan Python

```python
import bisect

# Data HARUS terurut
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# bisect_left: mencari posisi insertion point (cocok untuk search)
pos = bisect.bisect_left(data, 70)
if pos < len(data) and data[pos] == 70:
    print(f"70 ditemukan di indeks {pos}")    # Output: 70 ditemukan di indeks 6
else:
    print("70 tidak ditemukan")

# bisect_left untuk elemen yang tidak ada
pos = bisect.bisect_left(data, 55)
if pos < len(data) and data[pos] == 55:
    print(f"55 ditemukan di indeks {pos}")
else:
    print("55 tidak ditemukan")    # Output: 55 tidak ditemukan


# Fungsi helper untuk binary search dengan bisect
def binary_search_bisect(data, target):
    """Binary search menggunakan module bisect."""
    pos = bisect.bisect_left(data, target)
    if pos < len(data) and data[pos] == target:
        return pos
    return -1
```

### 9.6.4 `dict` dan `set` --- Pencarian O(1)

```python
# Dictionary: pencarian berdasarkan key --> O(1)
mahasiswa = {
    "2024001": "Ahmad",
    "2024002": "Budi",
    "2024003": "Citra",
    "2024004": "Dewi"
}

nim = "2024003"
if nim in mahasiswa:
    print(f"NIM {nim}: {mahasiswa[nim]}")    # Output: NIM 2024003: Citra

# Set: pencarian keanggotaan --> O(1)
nim_aktif = {"2024001", "2024002", "2024003", "2024004"}

if "2024003" in nim_aktif:
    print("Mahasiswa aktif!")    # Output: Mahasiswa aktif!
```

### 9.6.5 Ringkasan Kompleksitas Built-in Python

| Struktur Data | Operasi Pencarian | Kompleksitas |
|--------------|-------------------|-------------|
| `list` | `in`, `.index()` | O(n) |
| `list` (sorted) | `bisect.bisect_left()` | O(log n) |
| `dict` | `in`, `dict[key]` | O(1) average |
| `set` | `in` | O(1) average |
| `tuple` | `in` | O(n) |
| `str` | `in`, `.find()` | O(n*m) |

---

## 9.7 Studi Kasus: Sistem Pencarian Mahasiswa

### 9.7.1 Deskripsi Masalah

Sebuah universitas memiliki database mahasiswa. Sistem harus mendukung:
1. Pencarian berdasarkan **NIM** (unik, terurut) --- menggunakan Binary Search
2. Pencarian berdasarkan **nama** (tidak terurut secara default) --- menggunakan Linear Search

### 9.7.2 Implementasi Lengkap

```python
def binary_search_mahasiswa_nim(daftar, nim_target):
    """Mencari mahasiswa berdasarkan NIM menggunakan Binary Search.

    Prasyarat: daftar sudah terurut berdasarkan NIM.

    Args:
        daftar: List of dict, terurut berdasarkan key 'nim'
        nim_target: NIM yang dicari (string)

    Returns:
        dict atau None: Data mahasiswa jika ditemukan, None jika tidak
    """
    low = 0
    high = len(daftar) - 1

    while low <= high:
        mid = (low + high) // 2

        if daftar[mid]["nim"] == nim_target:
            return daftar[mid]
        elif daftar[mid]["nim"] < nim_target:
            low = mid + 1
        else:
            high = mid - 1

    return None


def linear_search_mahasiswa_nama(daftar, nama_target):
    """Mencari mahasiswa berdasarkan nama menggunakan Linear Search.

    Mendukung pencarian partial (substring matching).

    Args:
        daftar: List of dict
        nama_target: Nama atau bagian nama yang dicari (string)

    Returns:
        list: Daftar mahasiswa yang namanya mengandung nama_target
    """
    hasil = []
    nama_target_lower = nama_target.lower()

    for mhs in daftar:
        if nama_target_lower in mhs["nama"].lower():
            hasil.append(mhs)

    return hasil


# === Database Mahasiswa (terurut berdasarkan NIM) ===
database_mahasiswa = [
    {"nim": "2024001", "nama": "Ahmad Fauzi", "prodi": "Informatika", "ipk": 3.75},
    {"nim": "2024002", "nama": "Budi Santoso", "prodi": "Informatika", "ipk": 3.50},
    {"nim": "2024003", "nama": "Citra Dewi", "prodi": "Informatika", "ipk": 3.85},
    {"nim": "2024004", "nama": "Dewi Lestari", "prodi": "Informatika", "ipk": 3.60},
    {"nim": "2024005", "nama": "Eko Prasetyo", "prodi": "Informatika", "ipk": 3.45},
    {"nim": "2024006", "nama": "Fajar Nugroho", "prodi": "Informatika", "ipk": 3.70},
    {"nim": "2024007", "nama": "Gita Permata", "prodi": "Informatika", "ipk": 3.90},
    {"nim": "2024008", "nama": "Hadi Wijaya", "prodi": "Informatika", "ipk": 3.55},
    {"nim": "2024009", "nama": "Indah Cahyani", "prodi": "Informatika", "ipk": 3.80},
    {"nim": "2024010", "nama": "Joko Widodo", "prodi": "Informatika", "ipk": 3.65},
]


# === Demo Penggunaan ===
print("=" * 60)
print("    SISTEM PENCARIAN DATA MAHASISWA")
print("    Universitas Al Azhar Indonesia")
print("=" * 60)

# Pencarian berdasarkan NIM (Binary Search)
print("\n--- Pencarian berdasarkan NIM (Binary Search) ---")
nim_cari = "2024007"
result = binary_search_mahasiswa_nim(database_mahasiswa, nim_cari)
if result:
    print(f"  NIM     : {result['nim']}")
    print(f"  Nama    : {result['nama']}")
    print(f"  Prodi   : {result['prodi']}")
    print(f"  IPK     : {result['ipk']}")
else:
    print(f"  Mahasiswa dengan NIM {nim_cari} tidak ditemukan.")

# Pencarian berdasarkan nama (Linear Search)
print("\n--- Pencarian berdasarkan Nama (Linear Search) ---")
nama_cari = "dewi"
results = linear_search_mahasiswa_nama(database_mahasiswa, nama_cari)
print(f"  Hasil pencarian nama mengandung '{nama_cari}':")
if results:
    for mhs in results:
        print(f"    - {mhs['nim']} | {mhs['nama']} | IPK: {mhs['ipk']}")
else:
    print(f"  Tidak ada mahasiswa dengan nama mengandung '{nama_cari}'.")
```

**Output yang diharapkan**:

```
============================================================
    SISTEM PENCARIAN DATA MAHASISWA
    Universitas Al Azhar Indonesia
============================================================

--- Pencarian berdasarkan NIM (Binary Search) ---
  NIM     : 2024007
  Nama    : Gita Permata
  Prodi   : Informatika
  IPK     : 3.9

--- Pencarian berdasarkan Nama (Linear Search) ---
  Hasil pencarian nama mengandung 'dewi':
    - 2024003 | Citra Dewi | IPK: 3.85
    - 2024004 | Dewi Lestari | IPK: 3.6
```

---

## 9.8 Studi Kasus: Pencarian Produk E-Commerce

### 9.8.1 Deskripsi Masalah

Simulasi fitur pencarian produk seperti di Tokopedia atau Shopee. Sistem harus
mendukung:
1. Pencarian berdasarkan **nama produk** (substring matching)
2. Pencarian berdasarkan **rentang harga** (price range)
3. Pencarian berdasarkan **kategori**
4. Pencarian produk dengan **harga tertentu** menggunakan Binary Search

### 9.8.2 Implementasi Lengkap

```python
import bisect


# === Database Produk ===
produk_list = [
    {"id": "P001", "nama": "Laptop ASUS VivoBook 14",    "harga": 7500000,  "kategori": "Elektronik", "rating": 4.5},
    {"id": "P002", "nama": "Mouse Logitech M331",        "harga": 250000,   "kategori": "Elektronik", "rating": 4.7},
    {"id": "P003", "nama": "Keyboard Mechanical Rexus",   "harga": 450000,   "kategori": "Elektronik", "rating": 4.3},
    {"id": "P004", "nama": "Sepatu Nike Air Max",         "harga": 1500000,  "kategori": "Fashion",    "rating": 4.6},
    {"id": "P005", "nama": "Buku Algoritma Pemrograman",  "harga": 85000,    "kategori": "Buku",       "rating": 4.8},
    {"id": "P006", "nama": "Tas Ransel Eiger",            "harga": 350000,   "kategori": "Fashion",    "rating": 4.4},
    {"id": "P007", "nama": "Headset Sony WH-1000XM5",     "harga": 4500000,  "kategori": "Elektronik", "rating": 4.9},
    {"id": "P008", "nama": "Buku Python untuk Pemula",    "harga": 95000,    "kategori": "Buku",       "rating": 4.6},
    {"id": "P009", "nama": "Smartphone Samsung Galaxy",   "harga": 5000000,  "kategori": "Elektronik", "rating": 4.5},
    {"id": "P010", "nama": "Sepatu Adidas Ultraboost",    "harga": 2000000,  "kategori": "Fashion",    "rating": 4.7},
]


def cari_produk_nama(daftar_produk, keyword):
    """Mencari produk berdasarkan nama (Linear Search, substring matching)."""
    hasil = []
    keyword_lower = keyword.lower()
    for produk in daftar_produk:
        if keyword_lower in produk["nama"].lower():
            hasil.append(produk)
    return hasil


def cari_produk_harga(daftar_produk, harga_min, harga_max):
    """Mencari produk dalam rentang harga (Linear Search)."""
    hasil = []
    for produk in daftar_produk:
        if harga_min <= produk["harga"] <= harga_max:
            hasil.append(produk)
    return hasil


def cari_produk_kategori(daftar_produk, kategori):
    """Mencari produk berdasarkan kategori (Linear Search)."""
    hasil = []
    for produk in daftar_produk:
        if produk["kategori"].lower() == kategori.lower():
            hasil.append(produk)
    return hasil


def cari_harga_exact_binary(harga_sorted, harga_list_produk, target_harga):
    """Mencari produk dengan harga tepat menggunakan Binary Search.

    Args:
        harga_sorted: List harga yang sudah diurutkan
        harga_list_produk: List produk yang sudah diurutkan berdasarkan harga
        target_harga: Harga yang dicari

    Returns:
        list: Produk dengan harga tersebut
    """
    pos = bisect.bisect_left(harga_sorted, target_harga)
    hasil = []
    while pos < len(harga_sorted) and harga_sorted[pos] == target_harga:
        hasil.append(harga_list_produk[pos])
        pos += 1
    return hasil


def format_harga(harga):
    """Format harga ke format Rupiah."""
    return f"Rp{harga:,.0f}".replace(",", ".")


# === Demo Penggunaan ===
print("=" * 60)
print("    PENCARIAN PRODUK E-COMMERCE")
print("    Simulasi Tokopedia Search")
print("=" * 60)

# 1. Cari berdasarkan nama
print("\n[1] Pencarian: 'sepatu'")
hasil = cari_produk_nama(produk_list, "sepatu")
for p in hasil:
    print(f"    {p['nama']} - {format_harga(p['harga'])} (Rating: {p['rating']})")

# 2. Cari berdasarkan rentang harga
print("\n[2] Produk dengan harga Rp100.000 - Rp500.000:")
hasil = cari_produk_harga(produk_list, 100000, 500000)
for p in hasil:
    print(f"    {p['nama']} - {format_harga(p['harga'])}")

# 3. Cari berdasarkan kategori
print("\n[3] Kategori: 'Buku'")
hasil = cari_produk_kategori(produk_list, "Buku")
for p in hasil:
    print(f"    {p['nama']} - {format_harga(p['harga'])} (Rating: {p['rating']})")

# 4. Cari harga exact dengan Binary Search
produk_sorted = sorted(produk_list, key=lambda x: x["harga"])
harga_sorted = [p["harga"] for p in produk_sorted]

print(f"\n[4] Produk dengan harga tepat {format_harga(450000)} (Binary Search):")
hasil = cari_harga_exact_binary(harga_sorted, produk_sorted, 450000)
for p in hasil:
    print(f"    {p['nama']} - {format_harga(p['harga'])}")
```

**Output yang diharapkan**:

```
============================================================
    PENCARIAN PRODUK E-COMMERCE
    Simulasi Tokopedia Search
============================================================

[1] Pencarian: 'sepatu'
    Sepatu Nike Air Max - Rp1.500.000 (Rating: 4.6)
    Sepatu Adidas Ultraboost - Rp2.000.000 (Rating: 4.7)

[2] Produk dengan harga Rp100.000 - Rp500.000:
    Mouse Logitech M331 - Rp250.000
    Keyboard Mechanical Rexus - Rp450.000
    Tas Ransel Eiger - Rp350.000

[3] Kategori: 'Buku'
    Buku Algoritma Pemrograman - Rp85.000 (Rating: 4.8)
    Buku Python untuk Pemula - Rp95.000 (Rating: 4.6)

[4] Produk dengan harga tepat Rp450.000 (Binary Search):
    Keyboard Mechanical Rexus - Rp450.000
```

---

## 9.9 Pengukuran Performa

### 9.9.1 Mengukur Waktu Eksekusi

Kita dapat mengukur secara empiris perbedaan kecepatan antara Linear Search dan
Binary Search menggunakan modul `time`:

```python
import time


def linear_search(data, target):
    """Linear Search."""
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data, target):
    """Binary Search (data harus terurut)."""
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# === Pengukuran Performa ===
print("=" * 55)
print("  PERBANDINGAN PERFORMA LINEAR vs BINARY SEARCH")
print("=" * 55)

# Data: list terurut 0 sampai 999.999
data = list(range(1_000_000))
target = 999_999    # Worst case untuk linear search

# Mengukur Linear Search
start = time.time()
linear_search(data, target)
linear_time = time.time() - start

# Mengukur Binary Search
start = time.time()
binary_search(data, target)
binary_time = time.time() - start

print(f"\n  Jumlah data    : {len(data):,} elemen")
print(f"  Target         : {target:,} (elemen terakhir)")
print(f"  Linear Search  : {linear_time:.6f} detik")
print(f"  Binary Search  : {binary_time:.6f} detik")

if binary_time > 0:
    print(f"  Rasio          : Binary {linear_time/binary_time:,.0f}x lebih cepat!")
```

**Output yang mungkin (bervariasi tergantung hardware)**:

```
=======================================================
  PERBANDINGAN PERFORMA LINEAR vs BINARY SEARCH
=======================================================

  Jumlah data    : 1,000,000 elemen
  Target         : 999,999 (elemen terakhir)
  Linear Search  : 0.045231 detik
  Binary Search  : 0.000012 detik
  Rasio          : Binary 3,769x lebih cepat!
```

### 9.9.2 Pengukuran dengan Berbagai Ukuran Data

```python
import time


def ukur_performa(ukuran_list):
    """Mengukur performa linear vs binary search untuk berbagai ukuran data."""
    print(f"\n{'Ukuran Data':>15} | {'Linear (detik)':>15} | {'Binary (detik)':>15} | {'Rasio':>10}")
    print("-" * 65)

    for n in ukuran_list:
        data = list(range(n))
        target = n - 1    # Worst case

        # Linear Search
        start = time.time()
        linear_search(data, target)
        t_linear = time.time() - start

        # Binary Search
        start = time.time()
        binary_search(data, target)
        t_binary = time.time() - start

        rasio = t_linear / t_binary if t_binary > 0 else float('inf')
        print(f"{n:>15,} | {t_linear:>15.6f} | {t_binary:>15.6f} | {rasio:>9.0f}x")


# Jalankan pengukuran
ukuran = [1_000, 10_000, 100_000, 1_000_000, 10_000_000]
ukur_performa(ukuran)
```

**Output tipikal**:

```
    Ukuran Data |  Linear (detik) |  Binary (detik) |      Rasio
-----------------------------------------------------------------
          1,000 |        0.000045 |        0.000003 |        15x
         10,000 |        0.000450 |        0.000004 |       113x
        100,000 |        0.004500 |        0.000005 |       900x
      1,000,000 |        0.045000 |        0.000006 |     7,500x
     10,000,000 |        0.450000 |        0.000007 |    64,286x
```

### 9.9.3 Menghitung Jumlah Perbandingan

Selain waktu eksekusi, kita bisa menghitung jumlah perbandingan yang dilakukan:

```python
def linear_search_count(data, target):
    """Linear Search dengan penghitung perbandingan."""
    comparisons = 0
    for i in range(len(data)):
        comparisons += 1
        if data[i] == target:
            return i, comparisons
    return -1, comparisons


def binary_search_count(data, target):
    """Binary Search dengan penghitung perbandingan."""
    comparisons = 0
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if data[mid] == target:
            return mid, comparisons
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


# === Demo ===
data = list(range(1, 101))    # 1 sampai 100
target = 73

idx_l, comp_l = linear_search_count(data, target)
idx_b, comp_b = binary_search_count(data, target)

print(f"Mencari {target} dari {len(data)} elemen:")
print(f"  Linear: ditemukan di indeks {idx_l}, {comp_l} perbandingan")
print(f"  Binary: ditemukan di indeks {idx_b}, {comp_b} perbandingan")
```

---

## 9.10 Common Mistakes (Kesalahan Umum)

### Kesalahan 1: Lupa Mengurutkan Data Sebelum Binary Search

```python
# SALAH: Data tidak terurut, Binary Search tidak bekerja dengan benar!
data = [30, 10, 50, 20, 40]
hasil = binary_search(data, 20)
print(hasil)    # Mungkin -1 (padahal 20 ada di data!)

# BENAR: Urutkan dulu, baru Binary Search
data_sorted = sorted(data)    # [10, 20, 30, 40, 50]
hasil = binary_search(data_sorted, 20)
print(hasil)    # Output: 1
```

> **Aturan Emas**: SELALU pastikan data sudah terurut sebelum menggunakan Binary Search.
> Jika tidak, hasilnya bisa **salah tanpa error** --- ini adalah bug yang sangat
> berbahaya karena sulit dideteksi.

### Kesalahan 2: Off-by-One Error pada low/high/mid

```python
# SALAH: Menggunakan high = len(data) (seharusnya len(data) - 1)
def binary_search_buggy(data, target):
    low = 0
    high = len(data)    # BUG! Seharusnya len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:    # Bisa IndexError!
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# BENAR:
def binary_search_correct(data, target):
    low = 0
    high = len(data) - 1    # Indeks terakhir yang valid
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

### Kesalahan 3: Integer Overflow pada Perhitungan mid

```python
# Dalam bahasa seperti C/Java, perhitungan ini bisa overflow:
# mid = (low + high) / 2    # Jika low + high > MAX_INT --> overflow!

# Solusi yang aman (di semua bahasa):
# mid = low + (high - low) // 2

# Di Python, ini BUKAN masalah karena Python mendukung arbitrary precision integers.
# Namun, penting untuk memahami konsep ini karena:
# 1. Anda mungkin akan menulis Binary Search di bahasa lain (C, Java, dll.)
# 2. Ini adalah pertanyaan klasik dalam wawancara kerja (coding interview)
```

### Kesalahan 4: Infinite Loop Karena low/high Tidak Di-update

```python
# SALAH: Lupa meng-update low dan high
def binary_search_infinite(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid    # BUG! Seharusnya mid + 1 (bisa infinite loop)
        else:
            high = mid   # BUG! Seharusnya mid - 1 (bisa infinite loop)
    return -1

# BENAR: Selalu gunakan mid + 1 dan mid - 1
# low = mid + 1   (buang mid dan elemen sebelumnya)
# high = mid - 1  (buang mid dan elemen sesudahnya)
```

### Kesalahan 5: Tidak Menangani Kasus "Tidak Ditemukan"

```python
# SALAH: Mengabaikan kemungkinan elemen tidak ada
def search_no_check(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    # Tidak ada return statement untuk kasus tidak ditemukan!
    # Fungsi akan mengembalikan None secara implisit

# BENAR: Selalu tangani kasus tidak ditemukan
def search_with_check(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1    # Konvensi: -1 berarti tidak ditemukan

# Dan saat menggunakan hasil pencarian:
hasil = search_with_check(data, target)
if hasil != -1:
    print(f"Ditemukan di indeks {hasil}")
else:
    print("Tidak ditemukan")
```

---

## AI Corner: AI untuk Memahami Algoritma (Level: Lanjut)

### Menggunakan AI sebagai Tutor Algoritma

AI (seperti ChatGPT, Claude, atau Gemini) dapat menjadi alat bantu yang sangat berguna
untuk memahami algoritma pencarian. Berikut beberapa cara memanfaatkannya:

### 1. Meminta AI untuk Trace Algoritma Langkah per Langkah

**Prompt yang efektif**:
```
Tolong trace binary search secara langkah demi langkah untuk mencari
angka 42 dalam array [5, 12, 18, 25, 33, 42, 56, 68, 72, 89].
Tunjukkan nilai low, high, dan mid di setiap langkah.
```

AI akan memberikan trace table yang detail, mirip seperti yang ada di bab ini. Ini
sangat membantu untuk memverifikasi pemahaman Anda.

### 2. Meminta AI Menjelaskan Mengapa Binary Search O(log n)

**Prompt yang efektif**:
```
Jelaskan secara intuitif mengapa Binary Search memiliki kompleksitas O(log n).
Gunakan analogi yang sederhana dan berikan contoh perhitungan konkret.
```

### 3. Meminta AI untuk Generate Test Cases

**Prompt yang efektif**:
```
Buatkan test cases untuk menguji implementasi binary search saya, termasuk:
- Normal case (elemen ada di tengah, awal, akhir)
- Edge case (array kosong, satu elemen, elemen duplikat)
- Case yang sering menyebabkan bug
```

### 4. Meminta AI untuk Review Kode

**Prompt yang efektif**:
```
Review implementasi binary search saya berikut. Apakah ada bug atau
potensi masalah?

[paste kode Anda di sini]
```

### Peringatan Penting

> **PERHATIAN**: AI tidak selalu benar! Beberapa hal yang perlu diperhatikan:
>
> 1. **AI bisa salah menghitung mid**: Periksa kembali semua perhitungan aritmetika
>    yang diberikan AI, terutama pembulatan (floor division).
> 2. **AI mungkin menghasilkan binary search yang buggy**: Bug klasik seperti
>    off-by-one error atau infinite loop kadang muncul dalam kode yang dihasilkan AI.
> 3. **Selalu verifikasi dengan trace manual**: Jangan hanya mengandalkan penjelasan
>    AI. Coba trace sendiri dengan contoh kecil untuk memastikan kode benar.
> 4. **Gunakan AI untuk belajar, bukan untuk menyalin**: Tujuan menggunakan AI adalah
>    memahami konsep, bukan mendapat jawaban instan tanpa pemahaman.

---

## Latihan Soal

### Level 1: Dasar (5 soal)

**Soal 1.1** --- Implementasi Linear Search

Implementasikan fungsi `linear_search_all(data, target)` yang mengembalikan **semua
indeks** di mana `target` ditemukan (bukan hanya indeks pertama).

```python
# Contoh:
data = [5, 3, 7, 3, 9, 3, 1]
hasil = linear_search_all(data, 3)
print(hasil)    # Output: [1, 3, 5]
```

**Soal 1.2** --- Trace Binary Search

Buatlah trace table lengkap untuk pencarian target = **35** dalam data berikut
menggunakan Binary Search:

```
data = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
```

Tuliskan nilai `low`, `high`, `mid`, dan `data[mid]` di setiap langkah.

**Soal 1.3** --- Mencari Nilai Minimum

Implementasikan fungsi `find_min(data)` yang menggunakan **Linear Search** untuk
menemukan elemen **terkecil** dalam sebuah list. Jangan gunakan fungsi `min()` bawaan
Python.

```python
# Contoh:
data = [42, 15, 87, 3, 65, 28]
hasil = find_min(data)
print(hasil)    # Output: 3
```

**Soal 1.4** --- Mencari Nilai Maksimum

Implementasikan fungsi `find_max(data)` yang menggunakan **Linear Search** untuk
menemukan elemen **terbesar** dalam sebuah list. Jangan gunakan fungsi `max()` bawaan
Python.

**Soal 1.5** --- Verifikasi Binary Search

Diberikan data berikut yang **BELUM terurut**:

```
data = [45, 12, 78, 34, 56, 23, 89, 67]
```

Apa yang terjadi jika Anda langsung menjalankan Binary Search pada data ini tanpa
mengurutkannya terlebih dahulu? Jelaskan mengapa hasilnya bisa salah, dan berikan
contoh target yang menghasilkan jawaban yang salah.

---

### Level 2: Menengah (5 soal)

**Soal 2.1** --- Search in List of Dictionaries

Implementasikan fungsi `search_by_field(data_list, field, value)` yang mencari elemen
dalam list of dictionaries berdasarkan field tertentu.

```python
# Contoh:
mahasiswa = [
    {"nim": "001", "nama": "Ali", "ipk": 3.5},
    {"nim": "002", "nama": "Budi", "ipk": 3.8},
    {"nim": "003", "nama": "Cici", "ipk": 3.2},
]

hasil = search_by_field(mahasiswa, "nama", "Budi")
print(hasil)    # Output: {"nim": "002", "nama": "Budi", "ipk": 3.8}
```

**Soal 2.2** --- Search dengan Multiple Criteria

Implementasikan fungsi yang mencari produk berdasarkan **dua kriteria sekaligus**:
kategori DAN rentang harga.

```python
def search_multi_criteria(produk_list, kategori, harga_min, harga_max):
    """Mencari produk berdasarkan kategori dan rentang harga."""
    # Implementasikan di sini
    pass
```

**Soal 2.3** --- Menghitung Jumlah Perbandingan

Modifikasi fungsi `linear_search` dan `binary_search` agar mengembalikan
**jumlah perbandingan** yang dilakukan selain hasil pencarian. Lalu bandingkan
jumlah perbandingan keduanya untuk:
- Target ada di posisi awal
- Target ada di posisi tengah
- Target ada di posisi akhir
- Target tidak ada dalam data

**Soal 2.4** --- Search with Sentinel

Implementasikan **Sentinel Linear Search** --- variasi Linear Search yang menambahkan
target di akhir array sehingga tidak perlu memeriksa batas array di setiap iterasi.

```python
def sentinel_linear_search(data, target):
    """
    Sentinel Linear Search: tambahkan target di akhir array
    sehingga loop pasti berhenti tanpa perlu cek index bounds.
    """
    # Implementasikan di sini
    pass
```

**Soal 2.5** --- Binary Search: First and Last Occurrence

Implementasikan dua fungsi:
- `find_first(data, target)`: Menemukan indeks **pertama** dari target dalam data terurut
  yang mungkin memiliki elemen duplikat.
- `find_last(data, target)`: Menemukan indeks **terakhir** dari target.

```python
# Contoh:
data = [1, 2, 3, 3, 3, 4, 5, 6]
print(find_first(data, 3))    # Output: 2
print(find_last(data, 3))     # Output: 4
```

---

### Level 3: Mahir (3 soal)

**Soal 3.1** --- Interpolation Search

Implementasikan **Interpolation Search** --- variasi Binary Search yang memperkirakan
posisi target berdasarkan nilainya (bukan selalu memilih posisi tengah).

Formula posisi perkiraan:
```
pos = low + ((target - data[low]) * (high - low)) // (data[high] - data[low])
```

Interpolation Search memiliki kompleksitas **O(log log n)** untuk data yang terdistribusi
merata, namun bisa menjadi **O(n)** untuk distribusi tidak merata. Bandingkan
performanya dengan Binary Search untuk data yang:
- Terdistribusi merata (uniform)
- Terdistribusi tidak merata (skewed)

**Soal 3.2** --- Search in Rotated Sorted Array

Sebuah array terurut diputar (rotated) pada suatu titik. Misalnya:

```
Array asli   : [1, 2, 3, 4, 5, 6, 7]
Setelah rotasi: [4, 5, 6, 7, 1, 2, 3]  (rotasi di indeks 3)
```

Implementasikan fungsi yang mencari target dalam rotated sorted array dengan
kompleksitas **O(log n)** (modifikasi Binary Search).

```python
def search_rotated(data, target):
    """
    Binary Search pada sorted array yang sudah di-rotate.
    Kompleksitas: O(log n)
    """
    # Implementasikan di sini
    pass

# Contoh:
data = [4, 5, 6, 7, 1, 2, 3]
print(search_rotated(data, 6))    # Output: 2
print(search_rotated(data, 2))    # Output: 5
```

**Soal 3.3** --- Performance Analysis dengan matplotlib

Buatlah program yang:
1. Mengukur waktu eksekusi Linear Search dan Binary Search untuk berbagai ukuran data
   (n = 100, 500, 1000, 5000, 10000, 50000, 100000)
2. Menghitung jumlah perbandingan aktual untuk setiap ukuran data
3. Membuat **dua grafik** menggunakan matplotlib:
   - Grafik 1: Waktu eksekusi (x: ukuran data, y: waktu dalam detik)
   - Grafik 2: Jumlah perbandingan (x: ukuran data, y: jumlah perbandingan)
4. Simpan grafik sebagai file PNG

```python
import matplotlib.pyplot as plt
import time

# Kerangka program:
ukuran = [100, 500, 1000, 5000, 10000, 50000, 100000]
waktu_linear = []
waktu_binary = []
comp_linear = []
comp_binary = []

# Lengkapi kode untuk mengisi list di atas
# kemudian buat grafik perbandingan
```

---

## Rangkuman

### Poin-poin Penting Bab 9

1. **Pencarian (Searching)** adalah operasi fundamental dalam pemrograman yang digunakan
   untuk menemukan lokasi suatu elemen dalam kumpulan data.

2. **Linear Search** (Sequential Search):
   - Memeriksa elemen satu per satu dari awal hingga akhir
   - Kompleksitas: **O(n)**
   - Kelebihan: sederhana, tidak perlu data terurut
   - Kekurangan: lambat untuk data besar

3. **Binary Search** (Divide and Conquer):
   - Membagi ruang pencarian menjadi dua setiap langkah
   - Kompleksitas: **O(log n)**
   - Kelebihan: sangat cepat untuk data besar
   - Kekurangan: data **harus terurut**

4. **Binary Search Rekursif**:
   - Implementasi alternatif yang lebih elegan secara konseptual
   - Memerlukan memori O(log n) untuk call stack
   - Versi iteratif lebih disarankan untuk produksi

5. **Python Built-in**: Gunakan operator `in` untuk pencarian sederhana, module `bisect`
   untuk binary search, dan `dict`/`set` untuk pencarian O(1).

6. **Perbandingan Performa**:
   - Untuk 1 juta data, Binary Search bisa **50.000x lebih cepat** dari Linear Search
   - Untuk 1 miliar data, Binary Search hanya perlu **30 langkah**

7. **Kesalahan Umum**: lupa mengurutkan data, off-by-one error, infinite loop,
   integer overflow (di bahasa selain Python), dan tidak menangani kasus "tidak ditemukan".

### Diagram Alur Pemilihan Algoritma

```
                    Apakah data TERURUT?
                    /                \
                  Ya                Tidak
                  |                   |
          Apakah n BESAR?      Apakah akan dicari
          /           \        BERKALI-KALI?
        Ya            Tidak    /            \
        |               |    Ya            Tidak
   Binary Search   Linear/   |               |
                  Binary    Sort dulu,    Linear
                  (keduanya  lalu Binary   Search
                   OK)       Search
```

### Formula Penting

| Konsep | Formula |
|--------|---------|
| Indeks tengah | `mid = (low + high) // 2` |
| Indeks tengah (aman dari overflow) | `mid = low + (high - low) // 2` |
| Maks langkah Binary Search | `ceil(log2(n + 1))` |
| Kondisi berhenti Binary Search | `low > high` (tidak ditemukan) |

---

## Referensi

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009).
   *Introduction to Algorithms* (3rd ed.). MIT Press. --- Chapter 2: Getting Started
   (Binary Search discussion).

2. Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley.
   --- Section 3.1: Symbol Tables (searching fundamentals).

3. Gaddis, T. (2018). *Starting Out with Python* (4th ed.). Pearson.
   --- Chapter 9: Searching and Sorting Algorithms.

4. Knuth, D. E. (1998). *The Art of Computer Programming, Volume 3: Sorting and
   Searching* (2nd ed.). Addison-Wesley. --- Definitive reference on search algorithms.

5. Python Documentation. (2024). *bisect --- Array bisection algorithm*.
   https://docs.python.org/3/library/bisect.html

6. Lutz, M. (2013). *Learning Python* (5th ed.). O'Reilly Media.

---

## Glosarium

| Istilah | Definisi |
|---------|----------|
| **Searching** | Proses menemukan lokasi suatu elemen dalam kumpulan data |
| **Linear Search** | Algoritma pencarian yang memeriksa setiap elemen secara berurutan |
| **Binary Search** | Algoritma pencarian yang membagi ruang pencarian menjadi dua (divide and conquer) |
| **Divide and Conquer** | Strategi memecah masalah besar menjadi sub-masalah yang lebih kecil |
| **Big-O Notation** | Notasi matematika untuk menggambarkan batas atas kompleksitas algoritma |
| **O(n)** | Kompleksitas linear --- waktu bertambah proporsional dengan jumlah data |
| **O(log n)** | Kompleksitas logaritmik --- waktu bertambah sangat lambat seiring jumlah data |
| **Sorted** | Data yang sudah terurut (dari kecil ke besar atau sebaliknya) |
| **Index** | Posisi elemen dalam array/list (dimulai dari 0 di Python) |
| **Sentinel** | Nilai khusus yang ditambahkan untuk menyederhanakan logika pencarian |
| **Interpolation Search** | Variasi binary search yang memperkirakan posisi target berdasarkan nilainya |
| **Rotated Array** | Array terurut yang digeser siklis pada suatu titik |

---

*Bab 9 --- Algoritma Pencarian (Searching)*
*Algoritma dan Pemrograman --- Prodi Informatika, Universitas Al Azhar Indonesia*
*Tri Aji Nugroho, S.T., M.T.*
