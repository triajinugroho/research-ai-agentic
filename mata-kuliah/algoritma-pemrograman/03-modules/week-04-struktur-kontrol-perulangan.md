# Minggu 4: Struktur Kontrol: Perulangan (for/while)

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Algoritma dan Pemrograman (3 SKS) |
| **Minggu** | 4 dari 16 |
| **Topik** | Struktur Kontrol: Perulangan (for/while) |
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python |
| **CPMK** | CPMK-3 |
| **Sub-CPMK** | CPMK-3.5, CPMK-3.6, CPMK-3.7, CPMK-3.8 |
| **Durasi** | 150 menit (Teori: 75 menit, Praktik: 75 menit) |
| **Metode** | Ceramah interaktif, Live Coding, Praktik |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Menerapkan** perulangan `for` dengan fungsi `range()` untuk iterasi dengan jumlah pengulangan yang diketahui (CPMK-3.5)
2. **Menerapkan** perulangan `while` untuk iterasi dengan kondisi berhenti tertentu (CPMK-3.6)
3. **Menggunakan** pernyataan `break`, `continue`, dan klausa `else` pada loop untuk mengontrol alur perulangan (CPMK-3.7)
4. **Menganalisis** nested loop menggunakan loop trace table dan mengimplementasikannya untuk mencetak pola (CPMK-3.8)

---

## Materi Pembelajaran

### 1. Perulangan for dan Fungsi range() (CPMK-3.5)

Perulangan `for` digunakan ketika jumlah iterasi sudah diketahui sebelumnya.

| Bentuk range() | Deskripsi | Contoh | Hasil |
|----------------|-----------|--------|-------|
| `range(stop)` | 0 sampai stop-1 | `range(5)` | 0, 1, 2, 3, 4 |
| `range(start, stop)` | start sampai stop-1 | `range(2, 6)` | 2, 3, 4, 5 |
| `range(start, stop, step)` | start sampai stop-1 dengan langkah step | `range(1, 10, 2)` | 1, 3, 5, 7, 9 |

```python
# Menghitung jumlah 1 sampai 10
total = 0
for i in range(1, 11):
    total += i
print(f"Jumlah 1 sampai 10 = {total}")  # 55

# Hitung mundur
for i in range(10, 0, -1):
    print(i, end=" ")
print("Mulai!")  # 10 9 8 7 6 5 4 3 2 1 Mulai!

# Iterasi pada string
for huruf in "PYTHON":
    print(huruf, end="-")  # P-Y-T-H-O-N-
```

### 2. Perulangan while (CPMK-3.6)

Perulangan `while` digunakan ketika jumlah iterasi belum diketahui dan bergantung pada suatu kondisi.

```python
# Contoh: tebak angka sederhana
import random
angka_rahasia = random.randint(1, 10)
tebakan = 0
while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka (1-10): "))
    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
print("Selamat! Tebakan Anda benar!")
```

**Perhatian -- Infinite Loop:** Pastikan kondisi `while` akan bernilai `False` pada suatu titik agar loop berhenti. Selalu sertakan mekanisme pengubah kondisi di dalam blok while.

### 3. Pernyataan break, continue, dan else pada Loop (CPMK-3.7)

```python
# break -- menghentikan loop secara paksa
for i in range(1, 100):
    if i * i > 50:
        print(f"Bilangan pertama yang kuadratnya > 50: {i}")
        break  # keluar dari loop

# continue -- melewati iterasi saat ini
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")  # 1 2 4 5 7 8 10

# else pada loop -- dieksekusi jika loop selesai tanpa break
bilangan = 17
for i in range(2, bilangan):
    if bilangan % i == 0:
        print(f"{bilangan} bukan bilangan prima")
        break
else:
    print(f"{bilangan} adalah bilangan prima")
```

### 4. Nested Loop dan Loop Trace Table (CPMK-3.8)

```python
for i in range(1, 6):          # Tabel perkalian 1-5
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()
```

**Loop Trace Table** -- melacak nilai variabel di setiap iterasi. Contoh: `total = 0; for i in range(1,4): for j in range(1,3): total += i*j`

| Iterasi | i | j | i * j | total |
|---------|---|---|-------|-------|
| 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 2 | 3 |
| 3 | 2 | 1 | 2 | 5 |
| 4 | 2 | 2 | 4 | 9 |
| 5 | 3 | 1 | 3 | 12 |
| 6 | 3 | 2 | 6 | 18 |

**Mencetak pola dengan nested loop:**

```python
# Segitiga rata kiri                    # Segitiga rata kanan
n = 5                                    # n = 5
for i in range(1, n + 1):               # for i in range(1, n + 1):
    print("*" * i)                       #     print(" " * (n - i) + "*" * i)
```

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)

1. Membaca materi tentang perulangan dari referensi utama -- Bab 4 (10 menit)
2. Mengulang konsep operator perbandingan dan logika sebagai dasar kondisi loop (5 menit)

### In-class (120 menit)

| Waktu | Kegiatan | Metode |
|-------|----------|--------|
| 0--20 menit | Ceramah: Konsep perulangan for dan fungsi range() | Ceramah interaktif |
| 20--35 menit | Live coding: Contoh for loop (penjumlahan, hitung mundur, iterasi string) | Live coding |
| 35--55 menit | Ceramah dan live coding: Perulangan while dan penanganan infinite loop | Ceramah dan live coding |
| 55--70 menit | Ceramah: break, continue, else pada loop beserta contoh kasus | Ceramah interaktif |
| 70--90 menit | Live coding: Nested loop dan pattern printing (segitiga bintang) | Live coding |
| 90--105 menit | Latihan: Mengisi loop trace table untuk 2 program yang diberikan | Praktik terbimbing |
| 105--120 menit | Praktik mandiri: Mencetak 2 pola menggunakan nested loop | Praktik mandiri |

### Post-class (15 menit)

1. Mengerjakan Tugas T2 -- Pattern Printing (10 menit persiapan awal)
2. Mempersiapkan diri untuk Kuis K1 dengan mereview materi Minggu 1--4 (5 menit perencanaan belajar)

---

## Penugasan

### Tugas T2: Pattern Printing

| Komponen | Detail |
|----------|--------|
| **Jenis** | Tugas Individu |
| **Bobot** | Sesuai ketentuan RPS |
| **Deadline** | Minggu 5 (sebelum perkuliahan) |

**Deskripsi:** Buatlah program Python yang mencetak 3 pola berikut berdasarkan input N dari pengguna: (1) Pola Segitiga Angka -- baris ke-i menampilkan angka 1 sampai i, (2) Pola Diamond (Belah Ketupat) -- pola bintang berbentuk belah ketupat, (3) Pola Piramida Terbalik -- pola bintang piramida dari lebar ke sempit.

**Kriteria penilaian:** Ketepatan pola (50%), Penggunaan nested loop yang efisien (25%), Kualitas kode dan komentar (15%), Penanganan input tidak valid (10%).

### Kuis K1: Fondasi Algoritma dan Pemrograman

| Komponen | Detail |
|----------|--------|
| **Jenis** | Kuis Individu |
| **Cakupan** | Minggu 1--4 (Algoritma, Variabel, Seleksi, Perulangan) |
| **Durasi** | 30 menit (dilaksanakan di awal perkuliahan Minggu 5) |
| **Format** | 10 soal pilihan ganda, 3 soal tracing/trace table, 2 soal menulis kode singkat |

---

## Referensi

1. Gaddis, T. (2021). *Starting Out with Python*, 5th Edition. Pearson. -- Bab 4: Repetition Structures.
2. Zelle, J. (2016). *Python Programming: An Introduction to Computer Science*, 3rd Edition. -- Bab 8.
3. Dokumentasi resmi Python -- for Statements: [https://docs.python.org/3/tutorial/controlflow.html#for-statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
4. Dokumentasi resmi Python -- range(): [https://docs.python.org/3/library/stdtypes.html#range](https://docs.python.org/3/library/stdtypes.html#range)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
