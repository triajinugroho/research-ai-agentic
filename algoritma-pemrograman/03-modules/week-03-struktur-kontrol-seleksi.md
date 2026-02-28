# Minggu 3: Struktur Kontrol: Seleksi (if/elif/else)

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Algoritma dan Pemrograman (3 SKS) |
| **Minggu** | 3 dari 16 |
| **Topik** | Struktur Kontrol: Seleksi (if/elif/else) |
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python |
| **CPMK** | CPMK-3 |
| **Sub-CPMK** | CPMK-3.1, CPMK-3.2, CPMK-3.3, CPMK-3.4 |
| **Durasi** | 150 menit (Teori: 75 menit, Praktik: 75 menit) |
| **Metode** | Ceramah interaktif, Live Coding, Praktik |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Menjelaskan** konsep percabangan dan peran struktur seleksi dalam mengontrol alur program (CPMK-3.1)
2. **Menerapkan** struktur if, if-else, dan if-elif-else untuk menyelesaikan permasalahan dengan kondisi tunggal maupun majemuk (CPMK-3.2)
3. **Menganalisis** kondisi majemuk menggunakan operator logika (and, or, not) serta tabel kebenaran (CPMK-3.3)
4. **Mengimplementasikan** nested if dan conditional expression untuk menangani kasus percabangan bertingkat (CPMK-3.4)

---

## Materi Pembelajaran

### 1. Konsep Percabangan dan Struktur if (CPMK-3.1)

Struktur seleksi memungkinkan program mengambil keputusan berdasarkan kondisi tertentu. Alur eksekusi tidak lagi linear, melainkan bergantung pada hasil evaluasi kondisi (True atau False).

#### Struktur if Sederhana

```python
# Sintaks dasar if
if kondisi:
    # blok kode dieksekusi jika kondisi bernilai True
    pernyataan

# Contoh: memeriksa bilangan positif
bilangan = int(input("Masukkan bilangan: "))
if bilangan > 0:
    print("Bilangan tersebut adalah bilangan positif")
```

**Catatan penting:** Python menggunakan **indentasi** (4 spasi) untuk menandai blok kode, bukan kurung kurawal seperti bahasa C/Java.

### 2. Struktur if-else dan if-elif-else (CPMK-3.2)

#### Struktur if-else

```python
# Dua kemungkinan: True atau False
nilai = int(input("Masukkan nilai: "))
if nilai >= 60:
    print("LULUS")
else:
    print("TIDAK LULUS")
```

#### Struktur if-elif-else

```python
# Beberapa kemungkinan kondisi
nilai = int(input("Masukkan nilai (0-100): "))

if nilai >= 85:
    huruf = "A"
elif nilai >= 70:
    huruf = "B"
elif nilai >= 55:
    huruf = "C"
elif nilai >= 40:
    huruf = "D"
else:
    huruf = "E"

print(f"Nilai huruf: {huruf}")
```

**Tabel keputusan (Decision Table) untuk konversi nilai:**

| Rentang Nilai | Nilai Huruf | Keterangan |
|---------------|-------------|------------|
| 85 -- 100 | A | Sangat Baik |
| 70 -- 84 | B | Baik |
| 55 -- 69 | C | Cukup |
| 40 -- 54 | D | Kurang |
| 0 -- 39 | E | Sangat Kurang |

### 3. Kondisi Majemuk dan Tabel Kebenaran (CPMK-3.3)

Kondisi majemuk (compound condition) menggabungkan dua atau lebih ekspresi boolean menggunakan operator logika.

```python
# Operator and -- kedua kondisi harus True
usia = 20
memiliki_ktp = True
if usia >= 17 and memiliki_ktp:
    print("Anda berhak memilih dalam pemilu")

# Operator or -- salah satu kondisi True sudah cukup
hari = "Sabtu"
if hari == "Sabtu" or hari == "Minggu":
    print("Hari libur")

# Operator not -- membalik nilai logika
hujan = False
if not hujan:
    print("Cuaca cerah, ayo berolahraga!")
```

**Tabel Kebenaran (Truth Table):**

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

**Prioritas operator logika:** `not` (tertinggi) > `and` > `or` (terendah).

```python
# Contoh prioritas operator
# not True or False and True
# -> (not True) or (False and True)
# -> False or False
# -> False
```

### 4. Nested if dan Conditional Expression (CPMK-3.4)

#### Nested if (Percabangan Bertingkat)

```python
# Contoh: menentukan kategori dan harga tiket
usia = int(input("Masukkan usia: "))
hari = input("Hari (weekday/weekend): ")

if usia < 12:
    print("Kategori: Anak-anak")
    if hari == "weekend":
        print("Harga tiket: Rp 25.000")
    else:
        print("Harga tiket: Rp 15.000")
elif usia < 60:
    print("Kategori: Dewasa")
    if hari == "weekend":
        print("Harga tiket: Rp 50.000")
    else:
        print("Harga tiket: Rp 35.000")
else:
    print("Kategori: Lansia")
    print("Harga tiket: Rp 10.000 (semua hari)")
```

#### Conditional Expression (Ternary Operator)

```python
# Sintaks: nilai_jika_true if kondisi else nilai_jika_false
usia = 20
status = "Dewasa" if usia >= 17 else "Anak-anak"
print(status)  # Dewasa

# Contoh: menentukan ganjil/genap
bilangan = 7
jenis = "Genap" if bilangan % 2 == 0 else "Ganjil"
print(f"{bilangan} adalah bilangan {jenis}")  # 7 adalah bilangan Ganjil
```

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)

1. Membaca materi tentang struktur keputusan dari referensi utama -- Bab 3 (10 menit)
2. Menyelesaikan dan mengumpulkan Tugas T1 -- Kalkulator Sederhana (5 menit pengecekan akhir)

### In-class (120 menit)

| Waktu | Kegiatan | Metode |
|-------|----------|--------|
| 0--10 menit | Review Tugas T1 dan pembahasan singkat solusi kalkulator | Diskusi kelas |
| 10--30 menit | Ceramah: Konsep percabangan, struktur if dan if-else | Ceramah interaktif |
| 30--50 menit | Live coding: Konversi nilai huruf menggunakan if-elif-else dan decision table | Live coding |
| 50--70 menit | Ceramah: Kondisi majemuk, operator logika, dan tabel kebenaran | Ceramah dan diskusi |
| 70--85 menit | Live coding: Nested if (studi kasus tiket bioskop) dan conditional expression | Live coding |
| 85--120 menit | Praktik mandiri: Menyelesaikan 3--4 soal latihan percabangan bertingkat | Praktik terbimbing |

### Post-class (15 menit)

1. Mengerjakan latihan tambahan: program menentukan jenis segitiga berdasarkan panjang ketiga sisinya (10 menit)
2. Membuat decision table untuk studi kasus penentuan tarif parkir berdasarkan jenis kendaraan dan durasi (5 menit)

---

## Penugasan

Tidak ada tugas baru pada minggu ini. Mahasiswa fokus pada:
- Pengumpulan Tugas T1 (Kalkulator Sederhana) di awal perkuliahan
- Penyelesaian latihan post-class sebagai persiapan Minggu 4

---

## Referensi

1. Gaddis, T. (2021). *Starting Out with Python*, 5th Edition. Pearson. -- Bab 3: Decision Structures and Boolean Logic.
2. Zelle, J. (2016). *Python Programming: An Introduction to Computer Science*, 3rd Edition. -- Bab 7.
3. Dokumentasi resmi Python -- Compound Statements (if): [https://docs.python.org/3/reference/compound_stmts.html#if](https://docs.python.org/3/reference/compound_stmts.html#if)
4. Dokumentasi resmi Python -- Truth Value Testing: [https://docs.python.org/3/library/stdtypes.html#truth-value-testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
