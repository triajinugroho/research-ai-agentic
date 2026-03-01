# Minggu 11: Algoritma Pengurutan (Sorting)

## Informasi Modul

| Komponen | Keterangan |
|----------|------------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Kode MK** | IF1101 |
| **SKS** | 3 SKS |
| **Minggu** | 11 (Sebelas) |
| **Topik** | Algoritma Pengurutan (Sorting) |
| **CPMK** | CPMK-6: Mampu menerapkan algoritma dasar (pencarian, pengurutan, rekursi) untuk menyelesaikan masalah komputasional |
| **Sub-CPMK** | CPMK-6.5: Menjelaskan konsep dan pentingnya pengurutan data |
| | CPMK-6.6: Mengimplementasikan bubble sort, selection sort, dan insertion sort |
| | CPMK-6.7: Melakukan tracing langkah demi langkah pada setiap algoritma pengurutan |
| | CPMK-6.8: Membandingkan kompleksitas dan karakteristik ketiga algoritma serta pengurutan bawaan Python |
| **Durasi** | 150 menit |
| **Metode** | Ceramah, Live Coding, Tracing Exercise, Card Sorting Activity |
| **Bahasa Pemrograman** | Python |
| **Semester** | Genap 2025/2026 |
| **Pengajar** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Menjelaskan** konsep pengurutan dan mengapa data yang terurut penting dalam komputasi (C2 — Memahami)
2. **Mengimplementasikan** tiga algoritma pengurutan dasar (bubble sort, selection sort, insertion sort) dalam Python (C3 — Menerapkan)
3. **Menelusuri** (tracing) langkah demi langkah eksekusi setiap algoritma pengurutan pada data contoh (C4 — Menganalisis)
4. **Membandingkan** kompleksitas waktu, stabilitas, dan karakteristik ketiga algoritma serta pengurutan bawaan Python (C5 — Mengevaluasi)

---

## Materi Pembelajaran

### 11.1 Mengapa Pengurutan Penting?

Pengurutan (sorting) adalah proses menyusun data dalam urutan tertentu (ascending/descending). Pengurutan penting karena:

- **Binary search** hanya bekerja pada data terurut
- **Menampilkan data** secara terstruktur (daftar nilai, ranking)
- **Mendeteksi duplikat** lebih mudah pada data terurut
- **Operasi database** sangat bergantung pada pengurutan

### 11.2 Bubble Sort

Bubble sort bekerja dengan membandingkan dua elemen bersebelahan dan menukarnya jika urutannya salah. Proses diulang hingga tidak ada lagi pertukaran.

#### 11.2.1 Implementasi

```python
def bubble_sort(data):
    """Mengurutkan list secara ascending menggunakan bubble sort."""
    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break   # sudah terurut, hentikan lebih awal
    return data
```

#### 11.2.2 Tracing Bubble Sort

Data awal: `[64, 34, 25, 12, 22]`

**Pass 1:**

| Perbandingan | Data | Tukar? |
|-------------|------|--------|
| 64 > 34? Ya | [**34, 64**, 25, 12, 22] | Ya |
| 64 > 25? Ya | [34, **25, 64**, 12, 22] | Ya |
| 64 > 12? Ya | [34, 25, **12, 64**, 22] | Ya |
| 64 > 22? Ya | [34, 25, 12, **22, 64**] | Ya |

**Pass 2:**

| Perbandingan | Data | Tukar? |
|-------------|------|--------|
| 34 > 25? Ya | [**25, 34**, 12, 22, 64] | Ya |
| 34 > 12? Ya | [25, **12, 34**, 22, 64] | Ya |
| 34 > 22? Ya | [25, 12, **22, 34**, 64] | Ya |

Proses berlanjut hingga terurut: `[12, 22, 25, 34, 64]`

### 11.3 Selection Sort

Selection sort mencari elemen terkecil dari bagian yang belum terurut, lalu menukarnya dengan elemen di posisi paling depan bagian yang belum terurut.

#### 11.3.1 Implementasi

```python
def selection_sort(data):
    """Mengurutkan list secara ascending menggunakan selection sort."""
    n = len(data)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
    return data
```

#### 11.3.2 Tracing Selection Sort

Data awal: `[64, 25, 12, 22, 11]`

| Pass | Minimum ditemukan | Tukar dengan posisi | Hasil |
|------|-------------------|---------------------|-------|
| 1 | 11 (index 4) | index 0 | [**11**, 25, 12, 22, 64] |
| 2 | 12 (index 2) | index 1 | [11, **12**, 25, 22, 64] |
| 3 | 22 (index 3) | index 2 | [11, 12, **22**, 25, 64] |
| 4 | 25 (index 3) | index 3 | [11, 12, 22, **25**, 64] |

Hasil akhir: `[11, 12, 22, 25, 64]`

### 11.4 Insertion Sort

Insertion sort membangun list terurut satu elemen pada satu waktu, seperti cara kita mengurutkan kartu di tangan.

#### 11.4.1 Implementasi

```python
def insertion_sort(data):
    """Mengurutkan list secara ascending menggunakan insertion sort."""
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data
```

#### 11.4.2 Tracing Insertion Sort

Data awal: `[64, 34, 25, 12, 22]`

| Pass | Key | Pergeseran | Hasil |
|------|-----|-----------|-------|
| 1 | 34 | 64 geser kanan | [**34, 64**, 25, 12, 22] |
| 2 | 25 | 64, 34 geser kanan | [**25, 34, 64**, 12, 22] |
| 3 | 12 | 64, 34, 25 geser kanan | [**12, 25, 34, 64**, 22] |
| 4 | 22 | 64, 34, 25 geser kanan | [**12, 22, 25, 34, 64**] |

### 11.5 Perbandingan Algoritma Pengurutan

| Aspek | Bubble Sort | Selection Sort | Insertion Sort |
|-------|-------------|---------------|----------------|
| **Best case** | O(n)* | O(n^2) | O(n)* |
| **Average case** | O(n^2) | O(n^2) | O(n^2) |
| **Worst case** | O(n^2) | O(n^2) | O(n^2) |
| **Stabil** | Ya | Tidak | Ya |
| **In-place** | Ya | Ya | Ya |
| **Kapan terbaik** | Data hampir terurut | Data kecil | Data hampir terurut |

*Dengan optimasi early termination.

**Stable vs Unstable Sort:**
- **Stable:** Elemen dengan nilai sama mempertahankan urutan relatif aslinya
- **Unstable:** Urutan relatif elemen bernilai sama bisa berubah

### 11.6 Pengurutan Bawaan Python (Timsort)

```python
# sorted() — mengembalikan list baru (tidak mengubah asli)
angka = [64, 34, 25, 12, 22]
terurut = sorted(angka)
print(angka)     # [64, 34, 25, 12, 22] — tidak berubah
print(terurut)   # [12, 22, 25, 34, 64]

# .sort() — mengubah list secara in-place
angka.sort()
print(angka)     # [12, 22, 25, 34, 64] — berubah

# Descending
print(sorted([3, 1, 4, 1, 5], reverse=True))  # [5, 4, 3, 1, 1]

# Sort berdasarkan kriteria (key function)
mahasiswa = [("Budi", 85), ("Ahmad", 92), ("Citra", 78)]
by_nilai = sorted(mahasiswa, key=lambda x: x[1], reverse=True)
print(by_nilai)  # [("Ahmad", 92), ("Budi", 85), ("Citra", 78)]
```

> **Timsort** (algoritma bawaan Python) adalah hybrid sort yang menggabungkan merge sort dan insertion sort. Kompleksitasnya O(n log n) — jauh lebih efisien dari tiga algoritma dasar di atas untuk data besar.

---

## Kegiatan Pembelajaran

### Pre-Class (15 menit)

- Membaca konsep dasar pengurutan dari referensi utama
- Menonton visualisasi sorting algorithms (contoh: visualgo.net)
- Mengingat kembali konsep perbandingan dan pertukaran elemen list

### In-Class (120 menit)

| Waktu | Aktivitas | Deskripsi |
|-------|-----------|-----------|
| 0–10 menit | Ceramah: Pentingnya Pengurutan | Motivasi, contoh penerapan, pengantar tiga algoritma |
| 10–30 menit | Ceramah & Live Coding: Bubble Sort | Konsep, implementasi, tracing langkah demi langkah |
| 30–50 menit | Ceramah & Live Coding: Selection Sort | Konsep, implementasi, tracing langkah demi langkah |
| 50–70 menit | Ceramah & Live Coding: Insertion Sort | Konsep, implementasi, tracing langkah demi langkah |
| 70–85 menit | Card Sorting Activity | Mahasiswa mengurutkan kartu fisik menggunakan ketiga algoritma secara bergantian |
| 85–100 menit | Perbandingan & Timsort | Tabel perbandingan, konsep stable sort, demo sorted() dan .sort() |
| 100–115 menit | Live Coding: Pengukuran Performa | Membandingkan waktu eksekusi keempat algoritma pada berbagai ukuran data |
| 115–120 menit | Diskusi & Tanya Jawab | Kapan memilih algoritma tertentu, relevansi dengan dunia nyata |

### Post-Class (15 menit)

- Menyelesaikan Tugas T6 (Implementasi & Perbandingan Algoritma Pengurutan)
- Berlatih tracing setiap algoritma pada data contoh baru
- Membaca materi minggu depan: Rekursi dan Pemecahan Masalah

---

## Penugasan

### Tugas T6: Implementasi & Perbandingan Algoritma Pengurutan

| Komponen | Keterangan |
|----------|------------|
| **Deskripsi** | Implementasikan tiga algoritma pengurutan dan bandingkan performanya |
| **Tugas** | 1. Implementasikan `bubble_sort(data)`, `selection_sort(data)`, dan `insertion_sort(data)` |
| | 2. Tambahkan counter untuk menghitung jumlah perbandingan dan pertukaran di setiap algoritma |
| | 3. Uji pada list acak berukuran 1.000, 5.000, dan 10.000 elemen |
| | 4. Uji juga pada data yang sudah terurut dan terurut terbalik |
| | 5. Tampilkan tabel perbandingan (waktu, jumlah perbandingan, jumlah pertukaran) |
| | 6. Tulis analisis singkat (5–10 kalimat) menjelaskan hasil pengamatan |
| **Deadline** | Minggu 12, sebelum perkuliahan |
| **Pengumpulan** | LMS, file `.py` dan laporan analisis (PDF) |
| **Penilaian** | Kebenaran implementasi (35%), Counter & pengukuran (25%), Analisis (25%), Kode bersih & komentar (15%) |

---

## Referensi

1. Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.). MIT Press. — Chapter 12: Searching and Sorting.
2. Cormen, T. H., et al. (2022). *Introduction to Algorithms* (4th ed.). MIT Press. — Chapter 2: Insertion Sort, Chapter 7–8: Sorting.
3. Downey, A. B. (2015). *Think Python: How to Think Like a Computer Scientist* (2nd ed.). O'Reilly Media. — Appendix B: Analysis of Algorithms.
4. VisuAlgo. (2025). *Sorting Visualization*. https://visualgo.net/en/sorting

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
