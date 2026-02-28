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
| Bahasa         | Python                                                              |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Mengidentifikasi** konsep-konsep kunci dari setiap topik yang telah dipelajari pada Minggu 1--7 sebagai persiapan UTS.
2. **Menganalisis** potongan kode Python (code tracing) dan menentukan output yang dihasilkan secara tepat.
3. **Menyelesaikan** soal-soal pemrograman yang mengintegrasikan berbagai konsep fondasi dan modularitas.

---

## Materi Pembelajaran

### 8.1 Ringkasan Materi Minggu 1--7

#### Phase 1: Fondasi (Minggu 1--4)

| Minggu | Topik                              | Konsep Kunci                                                    |
|--------|------------------------------------|-----------------------------------------------------------------|
| 1      | Pengantar Algoritma & Python       | Definisi algoritma, flowchart, pseudocode, Google Colab, `print()`, `input()` |
| 2      | Variabel, Tipe Data, Operator      | Variabel, `int`, `float`, `str`, `bool`, operator aritmatika, perbandingan, logika, type casting |
| 3      | Percabangan (Selection)            | `if`, `elif`, `else`, nested if, operator logika dalam kondisi  |
| 4      | Perulangan (Iteration)             | `for`, `while`, `range()`, `break`, `continue`, nested loop, akumulator pattern |

#### Phase 2: Modularitas (Minggu 5--7)

| Minggu | Topik                              | Konsep Kunci                                                    |
|--------|------------------------------------|-----------------------------------------------------------------|
| 5      | Fungsi dan Modularitas             | `def`, parameter, `return`, scope (lokal/global), DRY, top-down design, docstring |
| 6      | String dan Pengolahan Teks         | Indexing, slicing, string methods, f-string, file I/O, `with` statement |
| 7      | List, Tuple, dan Operasi Koleksi   | List CRUD, list comprehension, nested list, tuple, `len`, `sum`, `min`, `max`, `sorted`, `enumerate`, `zip` |

### 8.2 Tipe Soal UTS

| Tipe Soal                   | Bobot | Jumlah | Deskripsi                                                      |
|-----------------------------|-------|--------|----------------------------------------------------------------|
| Pilihan Ganda (PG)          | 20%   | 10     | Konsep dasar, terminologi, output sederhana                    |
| Code Tracing                | 30%   | 5      | Membaca kode dan menentukan output secara manual               |
| Tulis Kode                  | 30%   | 3      | Menulis fungsi/program sesuai spesifikasi yang diberikan       |
| Essay / Desain Algoritma    | 20%   | 2      | Menjelaskan konsep dan merancang solusi algoritmik             |

**Format UTS:**
- Durasi: **100 menit**
- Sifat: **Closed-book** (buku tertutup)
- Alat bantu: **Tidak diperkenankan** menggunakan AI, internet, atau catatan
- Media: Kertas (ujian tertulis)

### 8.3 Tips Persiapan UTS

1. **Kuasai Konsep Dasar:** Pastikan memahami variabel, tipe data, operator, dan alur kontrol (percabangan & perulangan) secara mendalam.
2. **Latih Code Tracing:** Biasakan membaca kode baris per baris dan menentukan output secara manual tanpa menjalankan program.
3. **Hafal Sintaks Penting:** Pastikan dapat menulis `def`, `for`, `while`, `if`, list operations, dan string methods tanpa bantuan auto-complete.
4. **Pahami Fungsi:** Kuasai konsep parameter, return value, dan scope. Ini adalah topik yang sering diujikan.
5. **Kerjakan Latihan:** Ulangi semua latihan dari Minggu 1--7 dan coba soal-soal latihan di bawah ini.
6. **Manajemen Waktu:** Kerjakan soal yang mudah terlebih dahulu, baru kembali ke soal yang sulit.

### 8.4 Contoh Soal Latihan

#### Soal 1: Pilihan Ganda
Apa output dari kode berikut?
```python
x = 10
y = 3
print(x // y, x % y)
```
- (a) 3.33 1
- (b) 3 1
- (c) 3.0 1.0
- (d) 10 3

**Jawaban:** (b) — operator `//` adalah floor division, `%` adalah modulo.

#### Soal 2: Code Tracing
Tentukan output dari kode berikut:
```python
def misteri(n):
    hasil = ""
    for i in range(n, 0, -1):
        hasil += str(i)
    return hasil

x = misteri(5)
print(x, type(x).__name__)
```

**Jawaban:** `54321 str` — fungsi menggabungkan angka dari n sampai 1 menjadi string.

#### Soal 3: Code Tracing
Tentukan output dari kode berikut:
```python
data = [10, 20, 30, 40, 50]
hasil = []
for i in range(len(data)):
    if data[i] % 20 == 0:
        hasil.append(data[i] * 2)

print(hasil)
print(sum(hasil))
```

**Jawaban:** `[40, 80]` dan `120` — hanya elemen yang habis dibagi 20 (yaitu 20 dan 40) yang diproses.

#### Soal 4: Tulis Kode
Buatlah fungsi `hitung_huruf_vokal(teks)` yang menerima sebuah string dan mengembalikan jumlah huruf vokal (a, i, u, e, o) dalam string tersebut. Huruf besar dan kecil dihitung sama.

**Contoh jawaban:**
```python
def hitung_huruf_vokal(teks):
    """Menghitung jumlah huruf vokal dalam teks."""
    vokal = "aiueoAIUEO"
    jumlah = 0
    for huruf in teks:
        if huruf in vokal:
            jumlah += 1
    return jumlah

# Alternatif menggunakan list comprehension:
def hitung_huruf_vokal(teks):
    """Menghitung jumlah huruf vokal dalam teks."""
    return sum(1 for h in teks.lower() if h in "aiueo")
```

#### Soal 5: Code Tracing
Tentukan output dari kode berikut:
```python
def proses(data):
    hasil = []
    for item in data:
        if item > 0:
            hasil.append(item ** 2)
        else:
            hasil.append(abs(item))
    return hasil

angka = [-3, 4, -1, 5, 0, -2]
print(proses(angka))
```

**Jawaban:** `[3, 16, 1, 25, 0, 2]` — angka positif dikuadratkan, angka negatif/nol diambil nilai absolutnya.

#### Soal 6: Essay / Desain Algoritma
Jelaskan perbedaan antara variabel lokal dan variabel global dalam Python. Berikan contoh kasus di mana penggunaan variabel global dapat menyebabkan bug, dan bagaimana cara mengatasinya menggunakan parameter dan return value.

#### Soal 7: Tulis Kode
Buatlah fungsi `ringkasan_data(angka_list)` yang menerima list bilangan bulat dan mengembalikan tuple berisi `(rata_rata, nilai_max, nilai_min, jumlah_genap)`.

**Contoh jawaban:**
```python
def ringkasan_data(angka_list):
    """Menghitung ringkasan statistik dari list angka."""
    rata_rata = sum(angka_list) / len(angka_list)
    nilai_max = max(angka_list)
    nilai_min = min(angka_list)
    jumlah_genap = sum(1 for x in angka_list if x % 2 == 0)
    return rata_rata, nilai_max, nilai_min, jumlah_genap

# Penggunaan
avg, hi, lo, genap = ringkasan_data([10, 23, 44, 7, 36, 15])
print(f"Rata-rata: {avg:.1f}, Max: {hi}, Min: {lo}, Genap: {genap}")
```

#### Soal 8: Pilihan Ganda
Manakah yang merupakan tipe data **immutable** di Python?
- (a) list
- (b) dictionary
- (c) tuple
- (d) set

**Jawaban:** (c) — tuple bersifat immutable, tidak dapat diubah setelah dibuat.

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Membaca ringkasan materi Minggu 1--7 pada modul ini.
- Menyiapkan daftar topik atau konsep yang masih belum dipahami untuk ditanyakan saat sesi review.
- Mengerjakan 2--3 soal latihan secara mandiri sebelum kelas.

### In-class (150 menit)

| Waktu (menit)  | Kegiatan                                                      | Metode           |
|----------------|---------------------------------------------------------------|------------------|
| 0 -- 5         | Pembukaan dan penjelasan agenda hari ini                       | Ceramah          |
| 5 -- 20        | Review Phase 1: Fondasi (Minggu 1--4)                          | Ceramah & Diskusi|
| 20 -- 35       | Review Phase 2: Modularitas (Minggu 5--7)                      | Ceramah & Diskusi|
| 35 -- 50       | Tanya jawab terbuka dan pembahasan soal latihan                | Diskusi          |
| 50 -- 55       | Persiapan ujian: distribusi soal, penjelasan aturan            | —                |
| 55 -- 155      | **Ujian Tengah Semester (UTS) — 100 menit**                    | Ujian Tertulis   |

> **Catatan:** Jika jadwal UTS dilaksanakan pada sesi terpisah sesuai kebijakan universitas, maka sesi in-class 150 menit seluruhnya digunakan untuk review, latihan soal, dan tanya jawab. Ujian dilaksanakan sesuai jadwal UTS resmi.

### Post-class (15 menit)
- Refleksi mandiri terhadap performa UTS: identifikasi topik yang masih perlu diperkuat.
- Membaca materi Minggu 9 tentang topik Phase 3 berikutnya sebagai persiapan.

---

## Penugasan

Tidak ada tugas formal pada minggu ini. Mahasiswa diharapkan:

1. Mengumpulkan **Tugas T4** (Data Processing with Collections) sebelum UTS dimulai.
2. Mempersiapkan diri untuk UTS dengan mengerjakan soal-soal latihan di atas.
3. Mereview seluruh catatan, latihan, dan tugas dari Minggu 1--7.

---

## Referensi

1. Downey, A. (2015). *Think Python: How to Think Like a Computer Scientist*, 2nd Edition. O'Reilly Media. — Chapters 1--12 (seluruh materi yang relevan).
2. Matthes, E. (2023). *Python Crash Course*, 3rd Edition. No Starch Press. — Chapters 1--10 (seluruh materi yang relevan).
3. Python Software Foundation. *The Python Tutorial*. [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
4. Sweigart, A. (2019). *Automate the Boring Stuff with Python*, 2nd Edition. No Starch Press. — Chapters 1--6 (seluruh materi yang relevan).

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
