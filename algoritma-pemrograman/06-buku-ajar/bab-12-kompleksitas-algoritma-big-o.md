# BAB 12: KOMPLEKSITAS ALGORITMA (BIG-O) DAN OPTIMASI

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman --- Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| CPMK-7.1 | Menjelaskan konsep kompleksitas waktu dan ruang | C2 (Memahami) |
| CPMK-7.2 | Mengidentifikasi dan menghitung Big-O dari algoritma sederhana | C3 (Menerapkan) |
| CPMK-7.3 | Membandingkan efisiensi algoritma berdasarkan Big-O | C4 (Menganalisis) |
| CPMK-7.4 | Mengevaluasi trade-off antara waktu dan ruang | C5 (Mengevaluasi) |

**Prasyarat:** Mahasiswa telah memahami konsep loop, fungsi, rekursi (Bab 5--7), serta algoritma sorting dan searching (Bab 10--11).

---

## 12.1 Mengapa Efisiensi Penting?

### 12.1.1 Masalah yang Sama, Performa yang Berbeda Drastis

Bayangkan Anda diminta mencari satu nama dari **1 miliar data penduduk**. Dua programmer menulis solusi masing-masing:

- **Programmer A** menggunakan *linear search* --- memeriksa satu per satu dari awal.
- **Programmer B** menggunakan *binary search* --- data sudah terurut, dan pencarian dilakukan dengan membagi dua secara berulang.

Hasilnya?

| Pendekatan | Jumlah Operasi (Worst Case) | Estimasi Waktu |
|------------|----------------------------|----------------|
| Linear Search | 1.000.000.000 operasi | ~16 menit (pada 1 juta operasi/detik) |
| Binary Search | ~30 perbandingan | < 1 milidetik |

Ya, Anda membacanya dengan benar. **30 perbandingan** versus **1 miliar perbandingan**. Perbedaan ini bukan karena hardware yang lebih cepat atau bahasa pemrograman yang berbeda --- melainkan karena **algoritma yang berbeda**.

### 12.1.2 Ketika Data Tumbuh, Pilihan Algoritma Menentukan Segalanya

Untuk data kecil (misalnya 100 elemen), hampir semua algoritma terasa "cepat". Tetapi ketika data tumbuh --- dari ratusan menjadi jutaan, menjadi miliaran --- perbedaan efisiensi menjadi **sangat dramatis**.

Perhatikan tabel berikut untuk algoritma sorting:

| Jumlah Data (n) | Bubble Sort O(n^2) | Merge Sort O(n log n) | Rasio |
|------------------|--------------------|----------------------|-------|
| 1.000 | 1.000.000 operasi | ~10.000 operasi | 100x |
| 10.000 | 100.000.000 operasi | ~133.000 operasi | 752x |
| 1.000.000 | 1.000.000.000.000 operasi | ~20.000.000 operasi | 50.000x |

Pada 1 juta data, Bubble Sort memerlukan **50.000 kali** lebih banyak operasi dibanding Merge Sort!

### 12.1.3 Konteks Indonesia: Data Besar di Sekitar Kita

Efisiensi algoritma bukan hanya teori akademik. Berikut contoh nyata yang relevan dengan Indonesia:

- **Data Kependudukan Indonesia**: 270+ juta penduduk. Sistem Dukcapil harus mampu mencari, memvalidasi, dan memproses data penduduk dengan efisien.
- **E-commerce (Tokopedia, Shopee)**: Jutaan produk, jutaan transaksi per hari. Algoritma pencarian dan rekomendasi harus merespons dalam milidetik.
- **BPJS Kesehatan**: 200+ juta peserta. Verifikasi data harus real-time ketika pasien datang ke rumah sakit.
- **Pemilu**: 200+ juta pemilih. Sistem tabulasi dan quick count harus memproses data dengan cepat dan akurat.

> **Pesan Utama**: Memahami efisiensi algoritma bukan sekadar lulus ujian --- ini adalah keterampilan fundamental yang menentukan apakah sistem yang Anda bangun bisa melayani jutaan pengguna atau "crash" di hari pertama.

---

## 12.2 Cara Mengukur Efisiensi Algoritma

Ada beberapa pendekatan untuk mengukur efisiensi algoritma. Mari kita bahas dari yang paling sederhana hingga yang paling tepat.

### 12.2.1 Pendekatan 1: Mengukur Waktu Eksekusi (*Wall Clock Time*)

Cara paling intuitif adalah menjalankan program dan mengukur berapa lama waktu yang dibutuhkan.

```python
import time

def linear_search(data, target):
    for item in data:
        if item == target:
            return True
    return False

data = list(range(1_000_000))
target = 999_999

start = time.time()
linear_search(data, target)
end = time.time()

print(f"Waktu eksekusi: {end - start:.4f} detik")
```

**Masalah dengan pendekatan ini:**
- Hasilnya **bervariasi** tergantung hardware (laptop murah vs. server mahal).
- Dipengaruhi oleh proses lain yang berjalan bersamaan di komputer.
- Tidak memberikan gambaran bagaimana performa berubah ketika data bertambah.
- Harus benar-benar menjalankan program --- tidak bisa dianalisis secara teoritis.

**Verdict:** Berguna untuk benchmarking praktis, tetapi **tidak cukup** untuk analisis formal.

### 12.2.2 Pendekatan 2: Menghitung Jumlah Operasi

Pendekatan yang lebih baik adalah menghitung **berapa kali operasi dasar** dilakukan.

```python
def linear_search_counted(data, target):
    operations = 0
    for item in data:
        operations += 1       # hitung perbandingan
        if item == target:
            print(f"Ditemukan setelah {operations} operasi")
            return True
    print(f"Tidak ditemukan setelah {operations} operasi")
    return False
```

**Kelebihan:** Tidak tergantung hardware.
**Kekurangan:** Masih harus menjalankan program dan hasilnya spesifik untuk satu input tertentu.

### 12.2.3 Pendekatan 3: Analisis Asimptotik (*Asymptotic Analysis*)

Pendekatan terbaik adalah menganalisis **bagaimana jumlah operasi tumbuh seiring bertambahnya ukuran input** (n). Inilah yang disebut **analisis asimptotik**.

Alih-alih mengatakan "algoritma ini membutuhkan 3n + 5 operasi", kita menyederhanakannya menjadi "algoritma ini **berskala** O(n)".

Yang kita pedulikan bukan angka pastinya, melainkan **pola pertumbuhannya** (*growth rate*).

| Pendekatan | Presisi | Portabilitas | Skalabilitas |
|------------|---------|--------------|--------------|
| Wall clock time | Tinggi (untuk satu mesin) | Rendah | Rendah |
| Hitung operasi | Tinggi | Tinggi | Sedang |
| Analisis asimptotik | Umum | Sangat tinggi | Sangat tinggi |

> **Analogi**: Jika Anda ingin tahu apakah sebuah kota tumbuh pesat, Anda tidak perlu menghitung jumlah penduduk yang tepat. Cukup tahu apakah pertumbuhannya *linear* (naik stabil), *eksponensial* (meledak), atau *konstan* (stagnan). Itulah inti analisis asimptotik.

---

## 12.3 Notasi Big-O

### 12.3.1 Definisi Formal

**Big-O notation** mendeskripsikan *upper bound* (batas atas) dari laju pertumbuhan suatu fungsi.

Secara formal:

> Sebuah fungsi **f(n) = O(g(n))** jika dan hanya jika terdapat konstanta positif **c** dan **n_0** sedemikian sehingga:
>
> **f(n) <= c . g(n)** untuk semua **n >= n_0**

Artinya: mulai dari suatu titik (n_0), fungsi f(n) **tidak pernah tumbuh lebih cepat** dari g(n) dikalikan suatu konstanta.

### 12.3.2 Definisi Informal (Cara Mahasiswa Mengingat)

> **Big-O menggambarkan skenario terburuk (*worst case*) dari pertumbuhan waktu/ruang algoritma seiring bertambahnya ukuran input.**

Ketika kita mengatakan sebuah algoritma adalah O(n^2), artinya:
- Dalam skenario terburuk, waktu yang dibutuhkan **tumbuh secara kuadratik** terhadap ukuran input.
- Jika input berlipat 2, waktu bisa berlipat **hingga 4 kali**.
- Jika input berlipat 10, waktu bisa berlipat **hingga 100 kali**.

### 12.3.3 Notasi Asimptotik Lainnya (Sekilas)

Selain Big-O, ada notasi lain yang perlu diketahui:

| Notasi | Makna | Digunakan Untuk |
|--------|-------|-----------------|
| O (Big-O) | Upper bound (batas atas) | Worst case --- paling sering digunakan |
| Omega (Big-Omega) | Lower bound (batas bawah) | Best case |
| Theta (Big-Theta) | Tight bound (batas ketat) | Average case (tepat) |

Dalam praktik sehari-hari dan wawancara kerja, **Big-O** adalah yang paling sering digunakan karena kita biasanya ingin tahu **seburuk apa** performa algoritma.

### 12.3.4 Aturan Penyederhanaan Big-O

Ada tiga aturan emas dalam menyederhanakan notasi Big-O:

**Aturan 1: Buang Konstanta**

Konstanta pengali tidak berpengaruh pada laju pertumbuhan.

```
O(3n)     -->  O(n)
O(100n)   -->  O(n)
O(0.5n^2) -->  O(n^2)
O(5)      -->  O(1)
```

*Mengapa?* Karena konstanta hanya menggeser grafik ke atas/bawah, tetapi tidak mengubah **bentuk** pertumbuhannya.

**Aturan 2: Buang Suku Berorde Lebih Rendah**

Ketika n sangat besar, suku dengan orde tertinggi mendominasi.

```
O(n^2 + n)       -->  O(n^2)
O(n^3 + 100n^2)  -->  O(n^3)
O(n + log n)      -->  O(n)
O(2^n + n^5)      -->  O(2^n)
```

*Mengapa?* Untuk n = 1.000.000:
- n^2 = 1.000.000.000.000
- n   = 1.000.000

Suku n menjadi **tidak signifikan** dibanding n^2.

**Aturan 3: Secara Default, Gunakan Worst Case**

Kecuali disebutkan secara eksplisit, Big-O merujuk pada skenario terburuk.

```python
# Best case: O(1) --- target di posisi pertama
# Worst case: O(n) --- target di posisi terakhir atau tidak ada
# Kita katakan: Linear Search adalah O(n)
def linear_search(data, target):
    for item in data:
        if item == target:
            return True
    return False
```

---

## 12.4 Kelas-kelas Kompleksitas Umum

### 12.4.1 Tabel Perbandingan Pertumbuhan

Berikut adalah kelas-kelas kompleksitas yang paling umum ditemui, diurutkan dari yang paling efisien hingga paling tidak efisien:

| Big-O | Nama | Contoh Algoritma | n=10 | n=100 | n=1.000 | n=1.000.000 |
|-------|------|------------------|------|-------|---------|-------------|
| O(1) | Constant | Akses array by index, dict lookup | 1 | 1 | 1 | 1 |
| O(log n) | Logarithmic | Binary search, balanced BST lookup | 3 | 7 | 10 | 20 |
| O(n) | Linear | Linear search, iterasi satu loop | 10 | 100 | 1.000 | 1.000.000 |
| O(n log n) | Linearithmic | Merge sort, Timsort (Python sorted) | 33 | 664 | 9.966 | 19.931.569 |
| O(n^2) | Quadratic | Bubble sort, nested loops | 100 | 10.000 | 1.000.000 | 10^12 |
| O(n^3) | Cubic | Matrix multiplication (naive) | 1.000 | 1.000.000 | 10^9 | 10^18 |
| O(2^n) | Exponential | Fibonacci rekursif naive, brute force | 1.024 | 1,27 x 10^30 | ~ inf | ~ inf |
| O(n!) | Factorial | Permutasi, TSP brute force | 3.628.800 | ~ inf | ~ inf | ~ inf |

> **Catatan**: "~ inf" berarti jumlah operasi begitu besar sehingga tidak akan selesai dalam waktu yang realistis, bahkan dengan superkomputer tercepat di dunia.

### 12.4.2 Visualisasi Pertumbuhan (ASCII Graph)

```
Jumlah Operasi (skala logaritmik)
    |
    |                                              * O(n!)
    |
    |                                         * O(2^n)
    |
    |                                  *
    |                            * O(n^3)
    |
    |                      * O(n^2)
    |
    |                 *
    |            * O(n log n)
    |        *
    |     * O(n)
    |   *
    |  *
    | * O(log n)
    |*
    |* O(1)
    +-------------------------------------------------->
    1     10      100     1000    10000   100000      n
```

### 12.4.3 Penjelasan Setiap Kelas Kompleksitas

**O(1) --- Constant Time**

Waktu eksekusi **tidak berubah** berapapun ukuran input.

```python
# O(1) --- akses elemen array
def get_first(data):
    return data[0]

# O(1) --- dictionary lookup
def cari_mahasiswa(nim_dict, nim):
    return nim_dict.get(nim, "Tidak ditemukan")

# O(1) --- operasi aritmatika
def luas_persegi(sisi):
    return sisi * sisi
```

Tidak peduli apakah list memiliki 10 atau 10 juta elemen, mengakses elemen pertama selalu membutuhkan **satu langkah**.

**O(log n) --- Logarithmic Time**

Waktu eksekusi tumbuh secara **logaritmik**. Setiap kali input berlipat dua, operasi hanya bertambah **satu**.

```python
# O(log n) --- binary search
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
```

| Ukuran Data | Maks. Perbandingan |
|-------------|-------------------|
| 1.000 | 10 |
| 1.000.000 | 20 |
| 1.000.000.000 | 30 |

Algoritma O(log n) sangat efisien karena "membuang" setengah data di setiap langkah.

**O(n) --- Linear Time**

Waktu eksekusi tumbuh **sebanding langsung** dengan ukuran input.

```python
# O(n) --- linear search
def cari_linear(data, target):
    for item in data:
        if item == target:
            return True
    return False

# O(n) --- menghitung total
def total(data):
    result = 0
    for x in data:
        result += x
    return result
```

Jika data berlipat dua, waktu juga berlipat dua. Sederhana dan proporsional.

**O(n log n) --- Linearithmic Time**

Sedikit lebih lambat dari linear, tetapi **jauh lebih cepat** dari kuadratik. Ini adalah kompleksitas dari algoritma sorting terbaik berbasis perbandingan.

```python
# O(n log n) --- merge sort
def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**O(n^2) --- Quadratic Time**

Waktu eksekusi tumbuh secara **kuadratik**. Biasanya muncul ketika ada **nested loops** (loop bersarang).

```python
# O(n^2) --- bubble sort
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data
```

Untuk 10.000 data: 10.000 x 10.000 = **100 juta operasi**. Masih oke.
Untuk 1.000.000 data: 1.000.000 x 1.000.000 = **1 triliun operasi**. Tidak realistis!

**O(2^n) --- Exponential Time**

Waktu eksekusi **berlipat dua** setiap kali input bertambah satu. Hampir selalu tidak praktis untuk n > 30.

```python
# O(2^n) --- Fibonacci rekursif naive
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# fibonacci(40) membutuhkan ~1 miliar operasi!
# fibonacci(50) bisa memakan waktu berjam-jam
```

**O(n!) --- Factorial Time**

Tumbuh **sangat sangat cepat**. 20! = 2.432.902.008.176.640.000. Hanya layak untuk n < 15.

```python
# O(n!) --- mencari semua permutasi
def permutations(data):
    if len(data) <= 1:
        return [data]
    result = []
    for i in range(len(data)):
        rest = data[:i] + data[i+1:]
        for perm in permutations(rest):
            result.append([data[i]] + perm)
    return result
```

### 12.4.4 Batas Praktis: Berapa n yang Bisa Ditangani?

Asumsi: komputer mampu melakukan **10^8 operasi per detik** (100 juta operasi/detik).

| Kompleksitas | n Maks dalam 1 Detik | n Maks dalam 1 Menit |
|--------------|----------------------|----------------------|
| O(1) | ~ inf | ~ inf |
| O(log n) | ~ inf | ~ inf |
| O(n) | 10^8 | 6 x 10^9 |
| O(n log n) | ~4 x 10^6 | ~2 x 10^8 |
| O(n^2) | ~10.000 | ~77.000 |
| O(n^3) | ~464 | ~1.817 |
| O(2^n) | ~26 | ~32 |
| O(n!) | ~12 | ~14 |

> **Insight**: Jika soal competitive programming memberikan batas n = 10^5, dan time limit 1 detik, maka Anda membutuhkan solusi yang **paling buruk O(n log n)**. Solusi O(n^2) akan mendapat **TLE** (Time Limit Exceeded).

---

## 12.5 Menghitung Big-O --- Panduan Praktis

### 12.5.1 Langkah-langkah Menghitung Big-O

1. **Identifikasi operasi dasar** (perbandingan, penugasan, aritmatika).
2. **Hitung berapa kali operasi dasar dieksekusi** sebagai fungsi dari n.
3. **Sederhanakan** menggunakan aturan Big-O (buang konstanta dan suku berorde rendah).
4. **Nyatakan hasilnya** dalam notasi Big-O.

### 12.5.2 Contoh 1: Single Loop --- O(n)

```python
# Analisis langkah demi langkah
def hitung_total(data):
    total = 0              # 1 operasi --- O(1)
    for x in data:         # loop dijalankan n kali --- O(n)
        total += x         # 1 operasi per iterasi --- O(1)
    return total           # 1 operasi --- O(1)

# Total = O(1) + O(n) * O(1) + O(1)
#       = O(1) + O(n) + O(1)
#       = O(n)
```

**Kesimpulan: O(n)**

### 12.5.3 Contoh 2: Nested Loops --- O(n^2)

```python
# Cek apakah ada elemen duplikat
def cek_duplikat(data):
    n = len(data)
    for i in range(n):             # O(n) --- outer loop
        for j in range(i + 1, n):  # O(n) --- inner loop
            if data[i] == data[j]: # O(1) --- perbandingan
                return True
    return False

# Outer loop: n iterasi
# Inner loop: (n-1) + (n-2) + ... + 1 = n(n-1)/2 iterasi
# Total = n(n-1)/2 = (n^2 - n) / 2
# Buang konstanta dan suku berorde rendah: O(n^2)
```

**Kesimpulan: O(n^2)**

### 12.5.4 Contoh 3: Loop yang Membagi Dua --- O(log n)

```python
# Berapa kali n bisa dibagi 2 sampai menjadi 1?
def mystery(n):
    count = 0
    while n > 1:       # Loop berjalan sampai n <= 1
        n = n // 2     # n dibagi 2 setiap iterasi
        count += 1
    return count

# n = 16: 16 -> 8 -> 4 -> 2 -> 1 (4 langkah)
# n = 32: 32 -> 16 -> 8 -> 4 -> 2 -> 1 (5 langkah)
# n = 1024: butuh 10 langkah
# Secara umum: log2(n) langkah
```

**Kesimpulan: O(log n)**

### 12.5.5 Contoh 4: Nested Loops dengan Ukuran Berbeda --- O(n x m)

```python
# Matriks: n baris, m kolom
def cetak_matriks(matriks, n, m):
    for i in range(n):       # O(n)
        for j in range(m):   # O(m)
            print(matriks[i][j], end=" ")  # O(1)
        print()

# Total: O(n) * O(m) = O(n * m)
# Jika n == m, maka O(n^2)
# Tapi jika n dan m berbeda, tulis O(n * m)
```

**Kesimpulan: O(n x m)**

### 12.5.6 Contoh 5: Operasi Berurutan --- O(n + m)

```python
# Dua loop terpisah (bukan bersarang)
def proses_dua_list(list_a, list_b):
    # Loop pertama: O(n) di mana n = len(list_a)
    for item in list_a:
        print(item)

    # Loop kedua: O(m) di mana m = len(list_b)
    for item in list_b:
        print(item)

# Total: O(n) + O(m) = O(n + m)
# BUKAN O(n^2)! Karena loop-nya berurutan, bukan bersarang
```

**Kesimpulan: O(n + m)**

> **Peringatan umum**: Banyak mahasiswa mengira dua loop berarti O(n^2). **Tidak!** Dua loop berurutan = O(n + m). Dua loop bersarang = O(n * m).

### 12.5.7 Contoh 6: Fungsi Rekursif

```python
# Fibonacci rekursif
def fib(n):
    if n <= 1:          # Base case
        return n
    return fib(n-1) + fib(n-2)  # Dua pemanggilan rekursif

# Pohon rekursi: setiap pemanggilan menghasilkan 2 pemanggilan baru
# Level 0: 1 pemanggilan
# Level 1: 2 pemanggilan
# Level 2: 4 pemanggilan
# ...
# Level n: 2^n pemanggilan
# Total: 1 + 2 + 4 + ... + 2^n = 2^(n+1) - 1
# Big-O: O(2^n)
```

**Kesimpulan: O(2^n)**

Bandingkan dengan versi iteratif:

```python
# Fibonacci iteratif --- O(n)
def fib_iteratif(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

Perbedaan dari O(2^n) ke O(n) adalah **perbedaan yang sangat besar** --- fib(50) membutuhkan ~1 kuadriliun operasi secara rekursif, tetapi hanya 50 operasi secara iteratif!

### 12.5.8 Cheat Sheet: Pola Umum

| Pola Kode | Kompleksitas |
|-----------|-------------|
| Tidak ada loop | O(1) |
| Satu loop 0..n | O(n) |
| Dua loop bersarang, masing-masing 0..n | O(n^2) |
| Tiga loop bersarang | O(n^3) |
| Loop yang membagi/mengalikan 2 | O(log n) |
| Satu loop x loop yang membagi 2 | O(n log n) |
| Dua loop berurutan (terpisah) | O(n + m) |
| Rekursi yang memanggil diri sendiri 2x | O(2^n) |
| Mencari semua permutasi | O(n!) |

---

## 12.6 Space Complexity (Kompleksitas Ruang)

### 12.6.1 Apa itu Space Complexity?

Selain waktu, kita juga perlu memperhatikan **berapa banyak memori tambahan** yang digunakan algoritma. Ini disebut **space complexity** atau **kompleksitas ruang**.

> **Space complexity** mengukur jumlah memori *tambahan* (auxiliary space) yang dibutuhkan algoritma, relatif terhadap ukuran input.

**Catatan penting:** Yang dihitung adalah memori **tambahan** --- bukan memori yang digunakan untuk menyimpan input itu sendiri.

### 12.6.2 Contoh Space Complexity

**O(1) --- Constant Space** (In-place)

```python
# Bubble sort --- hanya butuh variabel temp
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]  # swap in-place
    return data

# Memori tambahan: hanya variabel i, j, n (konstan)
# Space complexity: O(1)
```

**O(n) --- Linear Space**

```python
# Membuat salinan list yang sudah difilter
def filter_genap(data):
    result = []             # list baru
    for x in data:
        if x % 2 == 0:
            result.append(x)
    return result

# Dalam worst case, semua elemen genap, sehingga result berukuran n
# Space complexity: O(n)
```

**O(n^2) --- Quadratic Space**

```python
# Membuat matriks n x n
def buat_matriks(n):
    matriks = []
    for i in range(n):
        baris = [0] * n    # n elemen per baris
        matriks.append(baris)
    return matriks

# Total sel: n * n = n^2
# Space complexity: O(n^2)
```

**O(n) --- Rekursi (Call Stack)**

```python
# Rekursi linear --- setiap panggilan menambah stack frame
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Kedalaman rekursi: n
# Setiap call frame memakan memori
# Space complexity: O(n) karena call stack
```

### 12.6.3 Trade-off: Waktu vs. Ruang

Seringkali ada **trade-off** antara waktu dan ruang. Dengan menggunakan lebih banyak memori, kita bisa mendapatkan waktu yang lebih cepat. Sebaliknya, menghemat memori bisa berarti waktu yang lebih lama.

**Contoh: Memoization pada Fibonacci**

```python
# Tanpa memoization: O(2^n) waktu, O(n) ruang (call stack)
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# Dengan memoization: O(n) waktu, O(n) ruang (cache + call stack)
def fib_memo(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]
```

| Pendekatan | Time Complexity | Space Complexity |
|------------|----------------|-----------------|
| Rekursif naive | O(2^n) | O(n) |
| Dengan memoization | O(n) | O(n) |
| Iteratif | O(n) | O(1) |

Memoization mengorbankan **ruang** (O(n) untuk cache) demi **waktu** yang jauh lebih baik (dari O(2^n) ke O(n)). Versi iteratif adalah yang terbaik --- O(n) waktu dan O(1) ruang.

> **Prinsip**: Dalam banyak kasus praktis, **waktu lebih berharga dari ruang**. Memori relatif murah dan berlimpah, sedangkan pengguna tidak suka menunggu.

---

## 12.7 Analisis Algoritma yang Sudah Dipelajari

Berikut rangkuman kompleksitas dari algoritma-algoritma yang sudah dipelajari di bab-bab sebelumnya:

### 12.7.1 Tabel Ringkasan Kompleksitas

| Algoritma | Time (Best) | Time (Average) | Time (Worst) | Space | Stabil? |
|-----------|-------------|----------------|--------------|-------|---------|
| **Searching** | | | | | |
| Linear Search | O(1) | O(n) | O(n) | O(1) | --- |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) | --- |
| **Sorting** | | | | | |
| Bubble Sort | O(n) | O(n^2) | O(n^2) | O(1) | Ya |
| Selection Sort | O(n^2) | O(n^2) | O(n^2) | O(1) | Tidak |
| Insertion Sort | O(n) | O(n^2) | O(n^2) | O(1) | Ya |
| Python sorted() / Timsort | O(n) | O(n log n) | O(n log n) | O(n) | Ya |
| **Data Structures** | | | | | |
| List --- akses by index | O(1) | O(1) | O(1) | --- | --- |
| List --- search (in) | O(1) | O(n) | O(n) | --- | --- |
| List --- append | O(1)* | O(1)* | O(1)* | --- | --- |
| Dict --- lookup | O(1) | O(1) | O(n)** | O(n) | --- |
| Dict --- insert | O(1) | O(1) | O(n)** | O(n) | --- |
| Set --- membership (in) | O(1) | O(1) | O(n)** | O(n) | --- |

> \* Amortized --- lihat Bagian 12.10
> \** Worst case O(n) karena hash collision, tetapi sangat jarang dalam praktik

### 12.7.2 Kapan Menggunakan Apa?

```python
# Skenario: mencari apakah suatu NIM ada dalam daftar

# Pendekatan 1: List + Linear Search --- O(n)
daftar_nim = ["2301001", "2301002", "2301003", ...]
nim_dicari = "2301999"
if nim_dicari in daftar_nim:  # O(n)
    print("Ditemukan")

# Pendekatan 2: Set + Hash Lookup --- O(1) average
set_nim = {"2301001", "2301002", "2301003", ...}
if nim_dicari in set_nim:  # O(1) average
    print("Ditemukan")

# Pendekatan 3: Sorted List + Binary Search --- O(log n)
import bisect
sorted_nim = sorted(daftar_nim)  # O(n log n) sekali saja
idx = bisect.bisect_left(sorted_nim, nim_dicari)
if idx < len(sorted_nim) and sorted_nim[idx] == nim_dicari:  # O(log n)
    print("Ditemukan")
```

**Rekomendasi:**
- Jika data sering berubah dan sering dicari: **gunakan Set atau Dict** (O(1) lookup).
- Jika data statis dan sudah terurut: **gunakan Binary Search** (O(log n)).
- Jika data sangat kecil (< 100 elemen): **tidak masalah** --- semua pendekatan cepat.

---

## 12.8 Optimasi: Contoh Praktis

### 12.8.1 Contoh 1: Menghapus Duplikat

**Pendekatan Naive --- O(n^2):**

```python
def hapus_duplikat_naive(data):
    """Menghapus elemen duplikat --- O(n^2)"""
    result = []
    for item in data:           # O(n)
        if item not in result:  # O(n) --- linear search di list
            result.append(item)
    return result
```

Mengapa O(n^2)? Karena `item not in result` melakukan linear search pada list `result`, yang bisa berukuran hingga n. Sehingga: O(n) * O(n) = O(n^2).

**Pendekatan Optimal --- O(n):**

```python
def hapus_duplikat_optimal(data):
    """Menghapus elemen duplikat --- O(n)"""
    seen = set()            # Set untuk tracking O(1) lookup
    result = []
    for item in data:       # O(n)
        if item not in seen: # O(1) --- hash lookup
            seen.add(item)   # O(1)
            result.append(item)
    return result
```

Atau lebih sederhana (jika urutan tidak penting):

```python
def hapus_duplikat_simple(data):
    return list(set(data))  # O(n)
```

### 12.8.2 Contoh 2: Two-Sum (Mencari Pasangan dengan Jumlah Tertentu)

**Soal:** Diberikan list angka dan target. Cari dua angka yang jika dijumlahkan sama dengan target.

**Pendekatan Naive --- O(n^2):**

```python
def two_sum_naive(data, target):
    """Cari pasangan yang jumlahnya = target --- O(n^2)"""
    n = len(data)
    for i in range(n):                  # O(n)
        for j in range(i + 1, n):       # O(n)
            if data[i] + data[j] == target:
                return (i, j)
    return None

# Contoh:
# two_sum_naive([2, 7, 11, 15], 9) --> (0, 1) karena 2 + 7 = 9
```

**Pendekatan Optimal --- O(n):**

```python
def two_sum_optimal(data, target):
    """Cari pasangan yang jumlahnya = target --- O(n)"""
    seen = {}               # dict: nilai -> index
    for i, num in enumerate(data):   # O(n)
        complement = target - num
        if complement in seen:       # O(1) dict lookup
            return (seen[complement], i)
        seen[num] = i                # O(1) dict insert
    return None

# Logika: untuk setiap angka x, kita cek apakah (target - x) sudah pernah dilihat
```

| Pendekatan | Time | Space |
|------------|------|-------|
| Naive (nested loops) | O(n^2) | O(1) |
| Optimal (hash map) | O(n) | O(n) |

Trade-off yang klasik: mengorbankan O(n) space untuk mendapatkan waktu dari O(n^2) ke O(n).

### 12.8.3 Contoh 3: Pengecekan Anagram

**Soal:** Dua string dikatakan anagram jika mengandung huruf-huruf yang sama dengan frekuensi yang sama (contoh: "listen" dan "silent").

**Pendekatan 1 --- O(n log n) dengan Sorting:**

```python
def is_anagram_sort(s1, s2):
    """Cek anagram dengan sorting --- O(n log n)"""
    return sorted(s1) == sorted(s2)
```

**Pendekatan 2 --- O(n) dengan Frequency Counter:**

```python
def is_anagram_counter(s1, s2):
    """Cek anagram dengan frequency counter --- O(n)"""
    if len(s1) != len(s2):
        return False

    freq = {}
    for char in s1:           # O(n)
        freq[char] = freq.get(char, 0) + 1

    for char in s2:           # O(n)
        if char not in freq or freq[char] == 0:
            return False
        freq[char] -= 1

    return True
```

Atau menggunakan `collections.Counter`:

```python
from collections import Counter

def is_anagram_pythonic(s1, s2):
    """Cek anagram --- Pythonic way --- O(n)"""
    return Counter(s1) == Counter(s2)
```

### 12.8.4 Contoh 4: Frekuensi Kata Terbanyak

**Soal:** Dari sebuah teks, temukan kata yang paling sering muncul.

**Pendekatan Naive --- O(n^2):**

```python
def kata_terbanyak_naive(teks):
    """Cari kata yang paling sering muncul --- O(n^2)"""
    kata_list = teks.lower().split()
    max_count = 0
    max_kata = ""
    for kata in kata_list:                       # O(n)
        count = kata_list.count(kata)            # O(n) --- menghitung dari awal
        if count > max_count:
            max_count = count
            max_kata = kata
    return max_kata, max_count
```

**Pendekatan Optimal --- O(n):**

```python
def kata_terbanyak_optimal(teks):
    """Cari kata yang paling sering muncul --- O(n)"""
    kata_list = teks.lower().split()
    freq = {}
    for kata in kata_list:             # O(n)
        freq[kata] = freq.get(kata, 0) + 1  # O(1)

    max_kata = max(freq, key=freq.get) # O(k) di mana k = jumlah kata unik
    return max_kata, freq[max_kata]
```

---

## 12.9 Studi Kasus: Perbandingan Performa dengan Timing

Berikut program lengkap yang membandingkan waktu eksekusi berbagai pendekatan:

```python
"""
Studi Kasus: Perbandingan Performa Algoritma
Mata Kuliah: Algoritma dan Pemrograman
Universitas Al Azhar Indonesia
"""

import time
import random

# ============================================================
# FUNGSI UTILITAS
# ============================================================

def ukur_waktu(func, *args):
    """Mengukur waktu eksekusi sebuah fungsi."""
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start


# ============================================================
# STUDI KASUS 1: MENGHAPUS DUPLIKAT
# ============================================================

def hapus_duplikat_naive(data):
    """O(n^2) --- menggunakan list"""
    result = []
    for item in data:
        if item not in result:
            result.append(item)
    return result

def hapus_duplikat_set(data):
    """O(n) --- menggunakan set"""
    seen = set()
    result = []
    for item in data:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# ============================================================
# STUDI KASUS 2: SEARCHING
# ============================================================

def linear_search(data, target):
    """O(n) --- linear search"""
    for i, item in enumerate(data):
        if item == target:
            return i
    return -1

def binary_search(data, target):
    """O(log n) --- binary search (data harus terurut)"""
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


# ============================================================
# MAIN: BENCHMARKING
# ============================================================

def main():
    sizes = [1_000, 5_000, 10_000, 50_000]

    print("=" * 65)
    print("BENCHMARK: HAPUS DUPLIKAT")
    print("=" * 65)
    print(f"{'n':>10} | {'Naive O(n^2)':>15} | {'Set O(n)':>15} | {'Speedup':>10}")
    print("-" * 65)

    for n in sizes:
        data = [random.randint(0, n // 2) for _ in range(n)]

        _, time_naive = ukur_waktu(hapus_duplikat_naive, data)
        _, time_set = ukur_waktu(hapus_duplikat_set, data)

        speedup = time_naive / time_set if time_set > 0 else float('inf')
        print(f"{n:>10,} | {time_naive:>13.4f} s | {time_set:>13.4f} s | {speedup:>8.1f}x")

    print()
    print("=" * 65)
    print("BENCHMARK: SEARCHING")
    print("=" * 65)
    sizes_search = [100_000, 1_000_000, 10_000_000]
    print(f"{'n':>12} | {'Linear O(n)':>15} | {'Binary O(log n)':>18} | {'Speedup':>10}")
    print("-" * 65)

    for n in sizes_search:
        data = list(range(n))
        target = n - 1  # worst case: elemen terakhir

        _, time_linear = ukur_waktu(linear_search, data, target)
        _, time_binary = ukur_waktu(binary_search, data, target)

        speedup = time_linear / time_binary if time_binary > 0 else float('inf')
        print(f"{n:>12,} | {time_linear:>13.4f} s | {time_binary:>16.6f} s | {speedup:>8.0f}x")

    print()
    print("Eksperimen selesai!")


if __name__ == "__main__":
    main()
```

**Contoh Output yang Diharapkan (bervariasi tergantung hardware):**

```
=================================================================
BENCHMARK: HAPUS DUPLIKAT
=================================================================
         n |   Naive O(n^2) |          Set O(n) |    Speedup
-----------------------------------------------------------------
     1,000 |        0.0081 s |        0.0001 s |     81.0x
     5,000 |        0.1834 s |        0.0005 s |    366.8x
    10,000 |        0.7215 s |        0.0010 s |    721.5x
    50,000 |       18.3421 s |        0.0049 s |   3743.3x

=================================================================
BENCHMARK: SEARCHING
=================================================================
           n |     Linear O(n) |    Binary O(log n) |    Speedup
-----------------------------------------------------------------
     100,000 |        0.0082 s |         0.000004 s |     2050x
   1,000,000 |        0.0814 s |         0.000005 s |    16280x
  10,000,000 |        0.8247 s |         0.000006 s |   137450x
```

> **Perhatikan** bagaimana speedup semakin besar seiring bertambahnya n. Inilah kekuatan analisis Big-O --- perbedaan yang kecil pada data kecil menjadi **sangat besar** pada data besar.

### 12.9.1 Visualisasi Opsional dengan Matplotlib

```python
# Opsional: jika matplotlib tersedia
try:
    import matplotlib.pyplot as plt
    import math

    n_values = list(range(1, 101))

    complexities = {
        'O(1)':        [1 for _ in n_values],
        'O(log n)':    [math.log2(n) if n > 0 else 0 for n in n_values],
        'O(n)':        n_values,
        'O(n log n)':  [n * math.log2(n) if n > 0 else 0 for n in n_values],
        'O(n^2)':      [n ** 2 for n in n_values],
    }

    plt.figure(figsize=(10, 6))
    for label, values in complexities.items():
        plt.plot(n_values, values, label=label, linewidth=2)

    plt.xlabel('Ukuran Input (n)')
    plt.ylabel('Jumlah Operasi')
    plt.title('Perbandingan Kelas Kompleksitas')
    plt.legend()
    plt.ylim(0, 500)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('kompleksitas_perbandingan.png', dpi=150)
    plt.show()
    print("Grafik berhasil disimpan!")
except ImportError:
    print("matplotlib tidak tersedia. Install dengan: pip install matplotlib")
```

---

## 12.10 Amortized Analysis (Analisis Amortisasi) --- Pengantar Singkat

### 12.10.1 Apa itu Amortized Analysis?

Kadang-kadang, satu operasi individual bisa **mahal**, tetapi jika dilihat secara rata-rata atas banyak operasi, biayanya menjadi **murah**. Analisis ini disebut **amortized analysis**.

### 12.10.2 Contoh: list.append() di Python

`list.append()` di Python memiliki kompleksitas **O(1) amortized**, bukan O(1) strict.

Mengapa? Karena Python list menggunakan **dynamic array**:

1. Saat list masih punya kapasitas tersisa, `append()` adalah O(1).
2. Saat list penuh, Python harus **mengalokasikan array baru yang lebih besar** dan **menyalin semua elemen**. Ini O(n).
3. Tetapi event "menyalin" ini terjadi **sangat jarang** (kapasitas berlipat dua setiap kali).

Ilustrasi:

```
Operasi append ke-1:   [x]            --- O(1)
Operasi append ke-2:   [x, x]         --- O(1)
Operasi append ke-3:   [x, x, x, _]   --- O(n) resize! tapi n masih kecil
Operasi append ke-4:   [x, x, x, x]   --- O(1)
Operasi append ke-5:   [x, x, x, x, x, _, _, _]  --- O(n) resize!
Operasi append ke-6:   [x, x, x, x, x, x, _, _]  --- O(1)
Operasi append ke-7:   O(1)
Operasi append ke-8:   O(1)
Operasi append ke-9:   O(n) resize!
...
```

Jika kita menghitung total biaya dari n operasi append dan membaginya dengan n:

```
Total biaya = n + (1 + 2 + 4 + 8 + ... + n)   [biaya resize]
            = n + 2n - 1
            = 3n - 1
Biaya amortisasi per operasi = (3n - 1) / n ≈ 3 = O(1)
```

> **Kesimpulan**: Meskipun sesekali `append()` membutuhkan O(n) untuk resize, rata-rata per operasi tetap **O(1) amortized**. Inilah mengapa kita aman menggunakan `list.append()` dalam loop tanpa khawatir performa.

### 12.10.3 Mengapa Ini Penting?

Amortized analysis menjelaskan mengapa operasi berikut dianggap efisien dalam praktik:

| Operasi | Worst Case (Satu Operasi) | Amortized |
|---------|--------------------------|-----------|
| list.append() | O(n) | O(1) |
| Dict insert | O(n) (rehashing) | O(1) |
| Set add | O(n) (rehashing) | O(1) |

Anda tidak perlu menghafal analisis formalnya di tahap ini, tetapi penting untuk **memahami konsepnya**: rata-rata dari banyak operasi bisa jauh lebih baik dari worst case satu operasi.

---

## 12.11 Common Mistakes (Kesalahan Umum)

### Kesalahan 1: Mengira O(1) Berarti "Cepat"

O(1) berarti **waktu konstan** --- tidak berubah seiring bertambahnya n. Tetapi "konstan" bisa berarti 1 milidetik atau 10 menit.

```python
# O(1) tapi lambat
def proses_berat():
    time.sleep(10)      # Tidur 10 detik --- tetap O(1)!
    return 42

# O(n) tapi cepat untuk n kecil
def loop_kecil(data):
    for x in data:
        pass
```

Jika n = 5, maka `loop_kecil` jauh lebih cepat meskipun O(n). Big-O menggambarkan **growth rate**, bukan **kecepatan absolut**.

### Kesalahan 2: Mengabaikan Konstanta untuk n Kecil

```python
# Algoritma A: O(100n) --- secara teknis O(n)
# Algoritma B: O(n^2)
#
# Untuk n < 100: Algoritma B sebenarnya lebih cepat!
# 100 * 50 = 5000  vs  50^2 = 2500
#
# Untuk n > 100: Algoritma A mulai menang
# 100 * 200 = 20000  vs  200^2 = 40000
```

> **Insight**: Big-O paling bermakna untuk **n yang besar**. Untuk n kecil (< 100), konstanta masih berpengaruh dan kadang algoritma "lebih buruk" secara Big-O justru **lebih cepat** dalam praktik.

### Kesalahan 3: Mengira Dua Loop Berurutan = O(n^2)

```python
# INI O(n), BUKAN O(n^2)
for x in data:      # O(n)
    print(x)
for x in data:      # O(n)
    print(x * 2)
# Total: O(n) + O(n) = O(2n) = O(n)

# INI yang O(n^2) --- loop BERSARANG
for x in data:           # O(n)
    for y in data:       # O(n)
        print(x, y)
# Total: O(n) * O(n) = O(n^2)
```

**Kunci:** Berurutan (sequential) = **dijumlahkan**. Bersarang (nested) = **dikalikan**.

### Kesalahan 4: Tidak Memperhitungkan Space Complexity

```python
# Banyak mahasiswa hanya fokus pada time complexity

# Time: O(n), Space: O(1) --- efisien di kedua metrik
def sum_data(data):
    total = 0
    for x in data:
        total += x
    return total

# Time: O(n), Space: O(n) --- time efisien, tapi butuh memori ekstra
def double_data(data):
    return [x * 2 for x in data]  # membuat list baru berukuran n
```

Untuk data besar (misal 10 GB), membuat salinan bisa menyebabkan **out of memory**. Selalu pertimbangkan space complexity!

### Kesalahan 5: Premature Optimization

Kutipan terkenal dari **Donald Knuth**:

> *"Premature optimization is the root of all evil."*

Artinya: **jangan mengoptimasi sebelum waktunya**.

Urutan yang benar:
1. **Make it work** --- buat program yang berfungsi dengan benar.
2. **Make it right** --- buat program yang bersih dan mudah dibaca.
3. **Make it fast** --- optimasi hanya jika diperlukan dan setelah profiling.

```python
# JANGAN lakukan ini sejak awal:
# "Saya harus pakai bit manipulation agar lebih cepat 0.001%"

# LAKUKAN ini:
# 1. Tulis solusi yang benar dan jelas
# 2. Test apakah sudah benar
# 3. Jika lambat, ukur di mana bottleneck-nya
# 4. Optimasi bagian yang lambat saja
```

---

## AI Corner: AI untuk Analisis Kompleksitas (Level: Mahir)

### Menggunakan AI untuk Menganalisis Big-O

AI generatif seperti ChatGPT, Claude, atau GitHub Copilot sangat baik dalam menganalisis kompleksitas algoritma. Berikut cara memanfaatkannya secara produktif:

### Prompt 1: Analisis Kompleksitas Kode

```
Prompt ke AI:
"Analisis time dan space complexity dari fungsi Python berikut.
Jelaskan langkah demi langkah.

def mystery(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(n):
            if arr[i] + arr[j] not in result:
                result.append(arr[i] + arr[j])
    return result
"
```

**Respons AI yang diharapkan:**
- Time: O(n^3) --- dua loop bersarang O(n^2), dan `not in result` melakukan linear search O(n)
- Space: O(n^2) --- result bisa berisi hingga n^2 elemen unik
- Saran optimasi: gunakan set untuk O(1) lookup

### Prompt 2: Minta AI Mengoptimasi

```
Prompt ke AI:
"Fungsi berikut memiliki time complexity O(n^2).
Bisakah kamu mengoptimasi menjadi O(n) atau O(n log n)?
Jelaskan pendekatan dan trade-off-nya.

def cari_duplikat_pertama(data):
    for i in range(len(data)):
        for j in range(i):
            if data[i] == data[j]:
                return data[i]
    return None
"
```

### Prompt 3: Verifikasi Analisis Anda

```
Prompt ke AI:
"Saya menganalisis bahwa fungsi berikut memiliki time complexity O(n log n).
Apakah analisis saya benar? Jika salah, apa yang sebenarnya?

def proses(data):
    data.sort()                    # Saya tahu ini O(n log n)
    for item in data:              # O(n)
        print(item)
    return data
"
```

### Tips Kritis dalam Menggunakan AI

1. **Selalu verifikasi** --- AI bisa salah, terutama untuk algoritma yang kompleks.
2. **Minta penjelasan langkah demi langkah** --- jangan terima jawaban tanpa reasoning.
3. **Uji dengan contoh** --- jika AI bilang O(n log n), coba jalankan dengan berbagai ukuran n dan verifikasi polanya.
4. **Jangan hanya copy-paste** --- pastikan Anda **memahami** mengapa suatu algoritma memiliki kompleksitas tertentu.

> **Peringatan**: Dalam ujian dan wawancara kerja, Anda harus bisa menganalisis Big-O **tanpa bantuan AI**. Gunakan AI sebagai **alat belajar**, bukan sebagai pengganti pemahaman.

---

## Latihan Soal

### Level Dasar (5 Soal)

**Soal 1.** Tentukan Big-O dari setiap potongan kode berikut:

```python
# (a)
def func_a(n):
    total = 0
    for i in range(n):
        total += i
    return total

# (b)
def func_b(n):
    for i in range(100):
        print(i)

# (c)
def func_c(data):
    return data[0] + data[-1]

# (d)
def func_d(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# (e)
def func_e(n):
    i = n
    while i > 0:
        print(i)
        i = i // 3
```

**Soal 2.** Urutkan kelas kompleksitas berikut dari yang paling efisien ke paling tidak efisien:

`O(n!), O(1), O(n log n), O(2^n), O(n), O(n^2), O(log n), O(n^3)`

**Soal 3.** Sederhanakan ekspresi Big-O berikut:
- (a) O(5n + 3)
- (b) O(n^2 + 1000n + 500)
- (c) O(3n^3 + 2n^2 + n)
- (d) O(log n + n)
- (e) O(2^n + n^5)

**Soal 4.** Sebuah algoritma membutuhkan n^2 operasi. Jika untuk n = 1.000 dibutuhkan waktu 1 detik, berapa estimasi waktu untuk n = 10.000?

**Soal 5.** Jelaskan mengapa Binary Search membutuhkan data yang **sudah terurut** untuk bisa bekerja, dan mengapa kompleksitasnya O(log n).

---

### Level Menengah (5 Soal)

**Soal 6.** Analisis time dan space complexity dari fungsi berikut:

```python
def mystery_1(data):
    n = len(data)
    result = {}
    for i in range(n):
        for j in range(i, n):
            key = (data[i], data[j])
            result[key] = result.get(key, 0) + 1
    return result
```

**Soal 7.** Optimasi kode berikut dari O(n^2) menjadi O(n):

```python
def ada_pasangan_berurutan(data):
    """Cek apakah ada dua elemen berurutan yang sama."""
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j and abs(i - j) == 1 and data[i] == data[j]:
                return True
    return False
```

**Soal 8.** Diberikan dua fungsi berikut:
- Fungsi A: `f(n) = 100n`
- Fungsi B: `g(n) = n^2`

(a) Untuk nilai n berapa Fungsi A lebih cepat dari Fungsi B?
(b) Untuk nilai n berapa Fungsi B lebih cepat dari Fungsi A?
(c) Apa Big-O masing-masing? Mana yang "lebih baik" secara asimptotik?

**Soal 9.** Hitung berapa operasi (secara tepat) yang dilakukan oleh kode berikut, lalu nyatakan dalam Big-O:

```python
def compute(n):
    count = 0
    for i in range(n):
        for j in range(i):
            count += 1
    return count
```

*Hint*: Hitung jumlah iterasi inner loop untuk setiap nilai i.

**Soal 10.** Jelaskan trade-off waktu vs. ruang dalam konteks berikut:
Anda memiliki list berisi 10 juta NIM mahasiswa. Anda perlu menjawab 100.000 pertanyaan "apakah NIM X ada dalam list?".
- Pendekatan A: Gunakan list dan linear search untuk setiap pertanyaan.
- Pendekatan B: Konversi list menjadi set terlebih dahulu, lalu gunakan set lookup.

Hitung total operasi masing-masing pendekatan.

---

### Level Mahir (3 Soal)

**Soal 11.** Buktikan bahwa `f(n) = 3n^2 + 7n + 4` adalah `O(n^2)` menggunakan definisi formal Big-O. Tentukan nilai c dan n_0 yang memenuhi.

*Hint*: Tunjukkan bahwa 3n^2 + 7n + 4 <= c * n^2 untuk n >= n_0 tertentu.

**Soal 12.** Desain algoritma O(n) untuk menyelesaikan masalah berikut:

> Diberikan sebuah list bilangan bulat `data` berukuran n. Temukan apakah ada **tiga elemen** (pada posisi berbeda) a, b, c sedemikian sehingga `a + b + c = 0`.
>
> Catatan: Solusi naive (tiga nested loops) adalah O(n^3). Solusi O(n^2) menggunakan two-pointer (setelah sorting) sudah sangat baik. *Apakah bisa O(n)?*

*Petunjuk*: Pikirkan tentang batasan nilai elemen (misalnya, jika nilai dibatasi antara -1000 sampai 1000).

**Soal 13. (Amortized Analysis)**
Sebuah stack mendukung operasi `push(x)` dan `multi_pop(k)`:
- `push(x)` memasukkan satu elemen --- biaya 1 operasi.
- `multi_pop(k)` mengeluarkan k elemen (atau semua elemen jika kurang dari k) --- biaya k operasi.

Jika dimulai dari stack kosong dan dilakukan **n** operasi (campuran push dan multi_pop):
(a) Berapa biaya worst case dari satu operasi multi_pop?
(b) Berapa biaya total terburuk dari n operasi?
(c) Berapa biaya amortisasi per operasi?

*Hint*: Setiap elemen hanya bisa di-pop jika sebelumnya di-push. Total push paling banyak n kali.

---

## Rangkuman

### Poin-poin Utama Bab 12

1. **Efisiensi algoritma** sangat penting, terutama ketika data berskala besar. Pilihan algoritma yang tepat bisa berarti perbedaan antara milidetik dan berjam-jam.

2. **Analisis asimptotik** (khususnya Big-O) adalah cara terbaik untuk mengukur efisiensi karena tidak bergantung pada hardware dan menggambarkan perilaku untuk n yang besar.

3. **Notasi Big-O** mendeskripsikan batas atas (*upper bound*) dari laju pertumbuhan. Aturan utama: buang konstanta, buang suku berorde rendah, dan gunakan worst case secara default.

4. **Kelas kompleksitas umum** (dari efisien ke tidak efisien):
   `O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)`

5. **Space complexity** sama pentingnya dengan time complexity. Sering ada trade-off: lebih banyak memori untuk waktu yang lebih cepat (contoh: memoization, hash tables).

6. **Pola umum**: satu loop = O(n), loop bersarang = O(n^2), loop yang membagi dua = O(log n), dua loop berurutan = O(n + m).

7. **Optimasi praktis** sering melibatkan penggantian linear search O(n) dengan hash lookup O(1) menggunakan set atau dict.

8. **Amortized analysis** menjelaskan mengapa operasi yang sesekali mahal (seperti list resize) tetap efisien secara rata-rata.

9. **Common mistakes**: O(1) bukan berarti cepat, konstanta penting untuk n kecil, dua loop berurutan bukan O(n^2), dan jangan lupa space complexity.

10. **Premature optimization** harus dihindari. Prioritaskan: **benar --> bersih --> cepat**.

### Hubungan dengan Bab Selanjutnya

Di Bab 13, kita akan mempelajari **File Handling dan Exception Handling**, di mana pemahaman tentang efisiensi akan membantu dalam memilih strategi yang tepat untuk memproses file berukuran besar.

---

## Referensi

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press. --- Bab 3: Growth of Functions.

2. Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2013). *Data Structures and Algorithms in Python*. Wiley. --- Bab 3: Algorithm Analysis.

3. Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley. --- Bab 1.4: Analysis of Algorithms.

4. Gaddis, T. (2021). *Starting Out with Python* (5th ed.). Pearson. --- Appendix: Algorithm Analysis.

5. Python Wiki. (2024). "Time Complexity." [https://wiki.python.org/moin/TimeComplexity](https://wiki.python.org/moin/TimeComplexity)

6. Big-O Cheat Sheet. [https://www.bigocheatsheet.com/](https://www.bigocheatsheet.com/)

---

## Glosarium

| Istilah | Definisi |
|---------|----------|
| **Asymptotic Analysis** | Analisis perilaku algoritma ketika ukuran input mendekati tak hingga |
| **Big-O Notation** | Notasi untuk mendeskripsikan batas atas laju pertumbuhan fungsi |
| **Time Complexity** | Ukuran jumlah operasi yang dibutuhkan algoritma sebagai fungsi dari ukuran input |
| **Space Complexity** | Ukuran jumlah memori tambahan yang dibutuhkan algoritma sebagai fungsi dari ukuran input |
| **Amortized Analysis** | Analisis biaya rata-rata per operasi atas serangkaian operasi |
| **Constant Time** | O(1) --- waktu tidak bergantung pada ukuran input |
| **Linear Time** | O(n) --- waktu berbanding lurus dengan ukuran input |
| **Logarithmic Time** | O(log n) --- waktu tumbuh secara logaritmik terhadap ukuran input |
| **Quadratic Time** | O(n^2) --- waktu tumbuh secara kuadratik terhadap ukuran input |
| **Exponential Time** | O(2^n) --- waktu berlipat dua setiap input bertambah satu |
| **Worst Case** | Skenario input yang menghasilkan jumlah operasi terbanyak |
| **Best Case** | Skenario input yang menghasilkan jumlah operasi paling sedikit |
| **Average Case** | Rata-rata jumlah operasi atas semua kemungkinan input |
| **In-place** | Algoritma yang hanya menggunakan memori tambahan konstan O(1) |
| **Trade-off** | Pertukaran antara dua aspek (misalnya waktu vs. ruang) |

---

*Bab 12 --- Kompleksitas Algoritma (Big-O) dan Optimasi*
*Algoritma dan Pemrograman --- Prodi Informatika, Universitas Al Azhar Indonesia*
*Tri Aji Nugroho, S.T., M.T.*
*Edisi Pertama, 2026*
