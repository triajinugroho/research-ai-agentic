# Minggu 10: Algoritma Pencarian (Searching)

## Informasi Modul

| Komponen | Keterangan |
|----------|------------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Kode MK** | IF1101 |
| **SKS** | 3 SKS |
| **Minggu** | 10 (Sepuluh) |
| **Topik** | Algoritma Pencarian (Searching) |
| **CPMK** | CPMK-6: Mampu menerapkan algoritma dasar (pencarian, pengurutan, rekursi) untuk menyelesaikan masalah komputasional |
| **Sub-CPMK** | CPMK-6.1: Menjelaskan pentingnya algoritma pencarian dalam pemrograman |
| | CPMK-6.2: Mengimplementasikan algoritma linear search dan melakukan tracing |
| | CPMK-6.3: Mengimplementasikan algoritma binary search dan melakukan tracing |
| | CPMK-6.4: Membandingkan kompleksitas waktu linear search O(n) dan binary search O(log n) |
| **Durasi** | 150 menit |
| **Metode** | Ceramah, Live Coding, Tracing Exercise, Demonstrasi Performa |
| **Bahasa Pemrograman** | Python |
| **Semester** | Genap 2025/2026 |
| **Pengajar** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Menjelaskan** mengapa algoritma pencarian penting dan di mana penerapannya dalam dunia nyata (C2 — Memahami)
2. **Mengimplementasikan** algoritma linear search dan binary search dalam Python serta melakukan tracing langkah demi langkah (C3 — Menerapkan)
3. **Membandingkan** kompleksitas waktu O(n) dan O(log n) melalui analisis dan pengukuran performa menggunakan modul `time` (C4 — Menganalisis)
4. **Menggunakan** fitur pencarian bawaan Python (`in`, `index()`, `bisect`) secara tepat sesuai kebutuhan (C3 — Menerapkan)

---

## Materi Pembelajaran

### 10.1 Mengapa Pencarian Penting?

Pencarian (searching) adalah operasi fundamental dalam ilmu komputer. Hampir setiap aplikasi memerlukan pencarian data:

- Mencari kontak di ponsel
- Mencari kata di dokumen (Ctrl+F)
- Mesin pencari (Google, Bing)
- Mencari data mahasiswa berdasarkan NIM

**Pertanyaan kunci:** Bagaimana cara paling efisien menemukan data tertentu dari sekumpulan data?

### 10.2 Linear Search (Pencarian Berurutan)

Linear search memeriksa setiap elemen satu per satu dari awal hingga akhir sampai elemen yang dicari ditemukan atau seluruh data telah diperiksa.

#### 10.2.1 Implementasi

```python
def linear_search(data, target):
    """Mencari target dalam list data secara berurutan.
    Mengembalikan index jika ditemukan, -1 jika tidak."""
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# Contoh penggunaan
angka = [34, 7, 23, 32, 5, 62, 14, 8]
hasil = linear_search(angka, 32)
print(f"Ditemukan di index: {hasil}")  # Ditemukan di index: 3
```

#### 10.2.2 Tracing Linear Search

Mencari nilai `23` dalam `[34, 7, 23, 32, 5]`:

| Langkah | Index (i) | data[i] | data[i] == 23? | Aksi |
|---------|-----------|---------|-----------------|------|
| 1 | 0 | 34 | Tidak | Lanjut |
| 2 | 1 | 7 | Tidak | Lanjut |
| 3 | 2 | 23 | **Ya** | Return 2 |

**Jumlah perbandingan:** 3

#### 10.2.3 Analisis Kompleksitas

| Kasus | Perbandingan | Keterangan |
|-------|-------------|------------|
| **Best case** | O(1) | Elemen ditemukan di posisi pertama |
| **Worst case** | O(n) | Elemen di posisi terakhir atau tidak ada |
| **Average case** | O(n/2) = O(n) | Rata-rata setengah data diperiksa |

### 10.3 Binary Search (Pencarian Biner)

Binary search bekerja pada data yang **sudah terurut**. Algoritma ini membagi ruang pencarian menjadi dua bagian pada setiap langkah.

#### 10.3.1 Prasyarat

> **Penting:** Binary search **hanya** bekerja pada data yang sudah terurut (sorted). Jika data belum terurut, harus diurutkan terlebih dahulu.

#### 10.3.2 Implementasi

```python
def binary_search(data, target):
    """Mencari target dalam list data yang sudah terurut.
    Mengembalikan index jika ditemukan, -1 jika tidak."""
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1     # cari di bagian kanan
        else:
            high = mid - 1    # cari di bagian kiri

    return -1

# Contoh penggunaan (data HARUS sudah terurut)
angka = [3, 7, 11, 18, 25, 33, 42, 56, 71, 89]
hasil = binary_search(angka, 33)
print(f"Ditemukan di index: {hasil}")  # Ditemukan di index: 5
```

#### 10.3.3 Tracing Binary Search

Mencari nilai `33` dalam `[3, 7, 11, 18, 25, 33, 42, 56, 71, 89]`:

| Langkah | low | high | mid | data[mid] | Perbandingan | Aksi |
|---------|-----|------|-----|-----------|-------------|------|
| 1 | 0 | 9 | 4 | 25 | 25 < 33 | low = 5 |
| 2 | 5 | 9 | 7 | 56 | 56 > 33 | high = 6 |
| 3 | 5 | 6 | 5 | 33 | 33 == 33 | **Return 5** |

**Jumlah perbandingan:** 3 (dari 10 elemen)

Bandingkan: linear search membutuhkan 6 perbandingan untuk menemukan elemen yang sama.

#### 10.3.4 Analisis Kompleksitas

| Kasus | Perbandingan | Keterangan |
|-------|-------------|------------|
| **Best case** | O(1) | Target tepat di tengah |
| **Worst case** | O(log n) | Terus membagi hingga 1 elemen |
| **Average case** | O(log n) | Rata-rata logaritmik |

### 10.4 Perbandingan Linear vs Binary Search

| Aspek | Linear Search | Binary Search |
|-------|--------------|---------------|
| **Prasyarat** | Tidak ada | Data harus terurut |
| **Kompleksitas** | O(n) | O(log n) |
| **n = 1.000** | Maks 1.000 langkah | Maks 10 langkah |
| **n = 1.000.000** | Maks 1.000.000 langkah | Maks 20 langkah |
| **Implementasi** | Sederhana | Lebih kompleks |
| **Kapan dipakai** | Data kecil/tidak terurut | Data besar dan terurut |

### 10.5 Pencarian Bawaan Python

```python
# Operator 'in' — cek keberadaan
angka = [10, 20, 30, 40, 50]
print(30 in angka)       # True
print(35 in angka)       # False

# Method index() — cari posisi (error jika tidak ada)
print(angka.index(30))   # 2

# Modul bisect — binary search pada list terurut
import bisect
data = [10, 20, 30, 40, 50]
pos = bisect.bisect_left(data, 30)
found = pos < len(data) and data[pos] == 30
print(f"Posisi: {pos}, Ditemukan: {found}")  # Posisi: 2, Ditemukan: True
```

### 10.6 Pengukuran Performa dengan Modul `time`

```python
import time
import random

# Buat data besar
data = sorted(random.sample(range(10_000_000), 1_000_000))
target = data[999_999]  # elemen terakhir (worst case linear)

# Ukur linear search
start = time.time()
linear_search(data, target)
waktu_linear = time.time() - start
print(f"Linear search: {waktu_linear:.6f} detik")

# Ukur binary search
start = time.time()
binary_search(data, target)
waktu_binary = time.time() - start
print(f"Binary search: {waktu_binary:.6f} detik")

# Perbandingan
print(f"Binary search {waktu_linear/waktu_binary:.0f}x lebih cepat")
```

---

## Kegiatan Pembelajaran

### Pre-Class (15 menit)

- Membaca konsep dasar algoritma pencarian dari referensi utama
- Mengingat kembali materi list dan pengurutan sederhana
- Memikirkan: di mana saja pencarian digunakan dalam kehidupan sehari-hari?

### In-Class (120 menit)

| Waktu | Aktivitas | Deskripsi |
|-------|-----------|-----------|
| 0–20 menit | Ceramah: Pentingnya Pencarian | Motivasi, contoh dunia nyata, pengantar dua algoritma utama |
| 20–40 menit | Ceramah & Live Coding: Linear Search | Penjelasan konsep, implementasi Python, analisis kompleksitas |
| 40–55 menit | Tracing Exercise | Mahasiswa melakukan tracing linear search secara manual di kertas |
| 55–80 menit | Ceramah & Live Coding: Binary Search | Penjelasan konsep, prasyarat sorted data, implementasi Python |
| 80–95 menit | Tracing Exercise | Mahasiswa melakukan tracing binary search secara manual di kertas |
| 95–110 menit | Live Coding: Perbandingan Performa | Demonstrasi pengukuran waktu eksekusi kedua algoritma pada data besar |
| 110–120 menit | Diskusi & Tanya Jawab | Kapan menggunakan linear vs binary search, fitur bawaan Python |

### Post-Class (15 menit)

- Menyelesaikan Tugas T5 (Implementasi & Perbandingan Algoritma Pencarian)
- Mencoba mengimplementasikan linear search yang mengembalikan semua index kemunculan
- Membaca materi minggu depan: Algoritma Pengurutan

---

## Penugasan

### Tugas T5: Implementasi & Perbandingan Algoritma Pencarian

| Komponen | Keterangan |
|----------|------------|
| **Deskripsi** | Implementasikan linear search dan binary search, lalu bandingkan performanya |
| **Tugas** | 1. Implementasikan fungsi `linear_search(data, target)` |
| | 2. Implementasikan fungsi `binary_search(data, target)` |
| | 3. Buat program yang menghasilkan list acak berukuran 10.000, 100.000, dan 1.000.000 |
| | 4. Ukur dan tampilkan waktu eksekusi kedua algoritma untuk setiap ukuran data |
| | 5. Tulis analisis singkat (5–10 kalimat) tentang hasil perbandingan |
| **Deadline** | Minggu 11, sebelum perkuliahan |
| **Pengumpulan** | LMS, file `.py` dan laporan analisis (PDF) |
| **Penilaian** | Kebenaran implementasi (40%), Pengukuran performa (30%), Analisis (30%) |

---

## Referensi

1. Downey, A. B. (2015). *Think Python: How to Think Like a Computer Scientist* (2nd ed.). O'Reilly Media. — Chapter 3: Functions, Appendix B: Analysis of Algorithms.
2. Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.). MIT Press. — Chapter 12: Searching and Sorting.
3. Cormen, T. H., et al. (2022). *Introduction to Algorithms* (4th ed.). MIT Press. — Chapter 2: Getting Started (Binary Search).
4. Python Software Foundation. (2025). *Python 3.12 Documentation — bisect*. https://docs.python.org/3/library/bisect.html

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
