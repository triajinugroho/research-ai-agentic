# Minggu 8: UTS -- Review dan Ujian Tengah Semester

## Informasi Modul

| Komponen       | Detail                                                              |
|----------------|---------------------------------------------------------------------|
| Mata Kuliah    | Algoritma dan Pemrograman (3 SKS)                                   |
| Minggu         | 8 (Delapan)                                                        |
| Topik          | UTS -- Review dan Ujian Tengah Semester                              |
| CPMK           | CPMK-1 s.d. CPMK-5 (Komprehensif Minggu 1--7)                      |
| Sub-CPMK       | Seluruh Sub-CPMK Phase 1 (Fondasi) dan Phase 2 (Modularitas)        |
| Durasi         | 150 menit (50 menit review + 100 menit ujian)                       |
| Metode         | Review session, tanya jawab, ujian tertulis                          |
| Pengajar       | Tri Aji Nugroho, S.T., M.T.                                        |
| Program Studi  | Informatika, Universitas Al Azhar Indonesia                         |
| Semester       | Genap 2025/2026                                                     |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Mengidentifikasi** konsep kunci dari setiap topik Minggu 1--7 sebagai persiapan UTS.
2. **Menganalisis** potongan kode Python (code tracing) dan menentukan output secara tepat.
3. **Menyelesaikan** soal pemrograman yang mengintegrasikan konsep fondasi dan modularitas.

---

## Materi Pembelajaran

### 8.1 Ringkasan Materi Minggu 1--7

#### Phase 1: Fondasi (Minggu 1--4)

| Minggu | Topik                         | Konsep Kunci                                                  |
|--------|-------------------------------|---------------------------------------------------------------|
| 1      | Pengantar Algoritma & Python  | Algoritma, flowchart, pseudocode, `print()`, `input()`        |
| 2      | Variabel, Tipe Data, Operator | `int`, `float`, `str`, `bool`, operator aritmatika/logika     |
| 3      | Percabangan (Selection)       | `if`, `elif`, `else`, nested if, operator logika              |
| 4      | Perulangan (Iteration)        | `for`, `while`, `range()`, `break`, `continue`, nested loop   |

#### Phase 2: Modularitas (Minggu 5--7)

| Minggu | Topik                         | Konsep Kunci                                                  |
|--------|-------------------------------|---------------------------------------------------------------|
| 5      | Fungsi dan Modularitas        | `def`, parameter, `return`, scope, DRY, docstring             |
| 6      | String dan Pengolahan Teks    | Indexing, slicing, string methods, f-string, file I/O         |
| 7      | List, Tuple, Operasi Koleksi  | List CRUD, list comprehension, tuple, `enumerate`, `zip`      |

### 8.2 Tipe Soal UTS

| Tipe Soal                | Bobot | Jumlah | Deskripsi                                    |
|--------------------------|-------|--------|----------------------------------------------|
| Pilihan Ganda (PG)       | 20%   | 10     | Konsep dasar, terminologi, output sederhana  |
| Code Tracing             | 30%   | 5      | Membaca kode dan menentukan output manual    |
| Tulis Kode               | 30%   | 3      | Menulis fungsi/program sesuai spesifikasi    |
| Essay / Desain Algoritma | 20%   | 2      | Menjelaskan konsep, merancang solusi         |

**Format UTS:** Durasi 100 menit, closed-book, tanpa AI/internet/catatan, ujian tertulis (kertas).

### 8.3 Tips Persiapan UTS

1. **Kuasai Konsep Dasar** -- variabel, tipe data, operator, percabangan, dan perulangan.
2. **Latih Code Tracing** -- baca kode baris per baris, tentukan output tanpa menjalankan program.
3. **Hafal Sintaks Penting** -- `def`, `for`, `while`, `if`, list operations, string methods.
4. **Pahami Fungsi** -- parameter, return value, dan scope sering diujikan.
5. **Kerjakan Latihan** -- ulangi semua latihan Minggu 1--7 dan soal latihan di bawah.
6. **Manajemen Waktu** -- kerjakan soal mudah terlebih dahulu.

### 8.4 Contoh Soal Latihan

**Soal 1 (PG):** Apa output dari kode berikut?
```python
x = 10
y = 3
print(x // y, x % y)
```
(a) 3.33 1 -- (b) **3 1** -- (c) 3.0 1.0 -- (d) 10 3

**Soal 2 (Code Tracing):** Tentukan output:
```python
def misteri(n):
    hasil = ""
    for i in range(n, 0, -1):
        hasil += str(i)
    return hasil

print(misteri(5), type(misteri(5)).__name__)
```
**Jawaban:** `54321 str`

**Soal 3 (Code Tracing):** Tentukan output:
```python
data = [10, 20, 30, 40, 50]
hasil = [x * 2 for x in data if x % 20 == 0]
print(hasil)
print(sum(hasil))
```
**Jawaban:** `[40, 80]` dan `120`

**Soal 4 (Tulis Kode):** Buat fungsi `hitung_huruf_vokal(teks)` yang mengembalikan jumlah huruf vokal.
```python
def hitung_huruf_vokal(teks):
    """Menghitung jumlah huruf vokal dalam teks."""
    return sum(1 for h in teks.lower() if h in "aiueo")
```

**Soal 5 (Code Tracing):** Tentukan output:
```python
def proses(data):
    return [x**2 if x > 0 else abs(x) for x in data]

print(proses([-3, 4, -1, 5, 0, -2]))
```
**Jawaban:** `[3, 16, 1, 25, 0, 2]`

**Soal 6 (Essay):** Jelaskan perbedaan variabel lokal dan global. Berikan contoh kasus di mana variabel global menyebabkan bug dan cara mengatasinya dengan parameter/return.

**Soal 7 (Tulis Kode):** Buat fungsi `ringkasan_data(angka_list)` yang mengembalikan tuple `(rata_rata, max, min, jumlah_genap)`.
```python
def ringkasan_data(angka_list):
    """Menghitung ringkasan statistik dari list angka."""
    rata = sum(angka_list) / len(angka_list)
    return rata, max(angka_list), min(angka_list), sum(1 for x in angka_list if x % 2 == 0)
```

**Soal 8 (PG):** Tipe data **immutable** di Python?
(a) list -- (b) dictionary -- (c) **tuple** -- (d) set

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Membaca ringkasan materi Minggu 1--7 pada modul ini.
- Menyiapkan daftar topik yang masih belum dipahami untuk sesi review.
- Mengerjakan 2--3 soal latihan secara mandiri.

### In-class (150 menit)

| Waktu (menit) | Kegiatan                                                | Metode           |
|----------------|---------------------------------------------------------|------------------|
| 0 -- 5         | Pembukaan dan penjelasan agenda                          | Ceramah          |
| 5 -- 20        | Review Phase 1: Fondasi (Minggu 1--4)                    | Ceramah & Diskusi|
| 20 -- 35       | Review Phase 2: Modularitas (Minggu 5--7)                | Ceramah & Diskusi|
| 35 -- 50       | Tanya jawab terbuka dan pembahasan soal latihan          | Diskusi          |
| 50 -- 55       | Persiapan ujian: distribusi soal, penjelasan aturan      | --               |
| 55 -- 155      | **Ujian Tengah Semester (UTS) -- 100 menit**              | Ujian Tertulis   |

> **Catatan:** Jika UTS dijadwalkan pada sesi terpisah sesuai kebijakan universitas, seluruh 150 menit digunakan untuk review, latihan, dan tanya jawab.

### Post-class (15 menit)
- Refleksi mandiri terhadap performa UTS.
- Membaca materi Minggu 9 sebagai persiapan Phase 3.

---

## Penugasan

Tidak ada tugas formal pada minggu ini. Mahasiswa diharapkan:

1. Mengumpulkan **Tugas T4** sebelum UTS dimulai.
2. Mempersiapkan diri dengan mengerjakan soal-soal latihan di atas.
3. Mereview seluruh catatan dan tugas dari Minggu 1--7.

---

## Referensi

1. Downey, A. (2015). *Think Python*, 2nd Ed. O'Reilly. -- Ch. 1--12.
2. Matthes, E. (2023). *Python Crash Course*, 3rd Ed. No Starch Press. -- Ch. 1--10.
3. Python Docs. *The Python Tutorial*. [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
4. Sweigart, A. (2019). *Automate the Boring Stuff with Python*, 2nd Ed. -- Ch. 1--6.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
