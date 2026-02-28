# Minggu 5: Fungsi dan Modularitas

## Informasi Modul

| Komponen       | Detail                                                        |
|----------------|---------------------------------------------------------------|
| Mata Kuliah    | Algoritma dan Pemrograman (3 SKS)                             |
| Minggu         | 5 (Lima)                                                      |
| Topik          | Fungsi dan Modularitas                                        |
| CPMK           | CPMK-4: Mampu menerapkan prinsip modularitas dalam pemrograman |
| Sub-CPMK       | CPMK-4.1, CPMK-4.2, CPMK-4.3, CPMK-4.4                     |
| Durasi         | 150 menit                                                     |
| Metode         | Ceramah, live coding, latihan refactoring                     |
| Pengajar       | Tri Aji Nugroho, S.T., M.T.                                  |
| Program Studi  | Informatika, Universitas Al Azhar Indonesia                   |
| Semester       | Genap 2025/2026                                               |
| Bahasa         | Python                                                        |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Mendefinisikan** fungsi menggunakan keyword `def`, parameter, dan `return` untuk memecah program menjadi unit-unit modular (CPMK-4.1).
2. **Membedakan** variabel lokal dan global serta menjelaskan konsep scope dalam konteks fungsi Python (CPMK-4.2).
3. **Menerapkan** prinsip DRY (Don't Repeat Yourself) dan pendekatan top-down design dalam perancangan solusi algoritmik (CPMK-4.3).
4. **Mendokumentasikan** fungsi menggunakan docstring dan memanfaatkan fungsi bawaan `help()` untuk membaca dokumentasi (CPMK-4.4).

---

## Materi Pembelajaran

### 5.1 Pengantar Fungsi

Fungsi adalah blok kode yang dapat digunakan kembali (reusable) untuk melakukan tugas tertentu. Fungsi membantu memecah program besar menjadi bagian-bagian kecil yang lebih mudah dipahami, diuji, dan dipelihara.

**Mengapa Fungsi Penting?**

| Manfaat            | Penjelasan                                                 |
|--------------------|------------------------------------------------------------|
| Reusability        | Kode ditulis sekali, dipanggil berkali-kali                |
| Abstraksi          | Menyembunyikan detail implementasi                         |
| Modularitas        | Memecah masalah besar menjadi sub-masalah kecil            |
| Keterbacaan        | Program lebih mudah dibaca dan dipahami                    |
| Pemeliharaan       | Perubahan cukup dilakukan di satu tempat                   |

### 5.2 Mendefinisikan dan Memanggil Fungsi

```python
# Sintaks dasar fungsi
def nama_fungsi(parameter1, parameter2):
    """Docstring: penjelasan singkat fungsi."""
    # badan fungsi
    hasil = parameter1 + parameter2
    return hasil

# Memanggil fungsi
total = nama_fungsi(10, 20)
print(total)  # Output: 30
```

### 5.3 Parameter dan Argumen

Python mendukung beberapa jenis parameter:

```python
# 1. Positional parameter
def sapa(nama, pesan):
    print(f"{pesan}, {nama}!")

sapa("Andi", "Selamat pagi")

# 2. Default parameter
def hitung_luas_persegi(sisi, satuan="cm"):
    luas = sisi ** 2
    return f"{luas} {satuan}^2"

print(hitung_luas_persegi(5))         # 25 cm^2
print(hitung_luas_persegi(5, "m"))    # 25 m^2

# 3. Keyword argument
def profil(nama, umur, kota):
    print(f"{nama}, {umur} tahun, dari {kota}")

profil(kota="Jakarta", nama="Budi", umur=20)
```

### 5.4 Return Value

Fungsi dapat mengembalikan satu nilai, beberapa nilai (tuple), atau `None` jika tanpa `return`:

```python
# Mengembalikan satu nilai
def kuadrat(x):
    return x ** 2

# Mengembalikan beberapa nilai
def hitung_statistik(data):
    minimum = min(data)
    maksimum = max(data)
    rata_rata = sum(data) / len(data)
    return minimum, maksimum, rata_rata

low, high, avg = hitung_statistik([10, 20, 30, 40, 50])
print(f"Min={low}, Max={high}, Avg={avg}")
```

### 5.5 Scope: Variabel Lokal dan Global

```python
pesan_global = "Halo Dunia"  # variabel global

def demo_scope():
    pesan_lokal = "Halo Lokal"   # variabel lokal
    print(pesan_global)          # bisa akses global
    print(pesan_lokal)           # bisa akses lokal

demo_scope()
# print(pesan_lokal)  # ERROR: variabel lokal tidak bisa diakses di luar fungsi
```

| Aspek              | Variabel Lokal                    | Variabel Global                    |
|--------------------|-----------------------------------|------------------------------------|
| Didefinisikan di   | Dalam fungsi                      | Di luar fungsi (level modul)       |
| Dapat diakses dari | Hanya dalam fungsi tersebut       | Seluruh program                    |
| Masa hidup         | Selama fungsi berjalan            | Selama program berjalan            |
| Best practice      | Gunakan sebanyak mungkin          | Hindari jika memungkinkan          |

> **Catatan:** Penggunaan `global` keyword sebaiknya dihindari karena membuat program sulit di-debug dan dipelihara.

### 5.6 Prinsip DRY dan Top-Down Design

**DRY (Don't Repeat Yourself):** Setiap pengetahuan atau logika harus memiliki representasi tunggal yang tidak ambigu di dalam sistem.

```python
# SEBELUM refactoring (melanggar DRY)
print("=" * 40)
print("LAPORAN NILAI MAHASISWA")
print("=" * 40)
# ... kode lain ...
print("=" * 40)
print("LAPORAN KEHADIRAN")
print("=" * 40)

# SETELAH refactoring (mengikuti DRY)
def cetak_header(judul):
    print("=" * 40)
    print(judul)
    print("=" * 40)

cetak_header("LAPORAN NILAI MAHASISWA")
cetak_header("LAPORAN KEHADIRAN")
```

**Top-Down Design:** Memecah masalah besar menjadi sub-masalah yang lebih kecil, kemudian mengimplementasikan setiap sub-masalah sebagai fungsi.

```python
# Top-down design: Program Kalkulator Nilai
def main():
    nama = input_nama()
    nilai_list = input_nilai()
    rata_rata = hitung_rata_rata(nilai_list)
    grade = tentukan_grade(rata_rata)
    tampilkan_hasil(nama, rata_rata, grade)
```

### 5.7 Docstring

```python
def hitung_bmi(berat_kg, tinggi_m):
    """
    Menghitung Body Mass Index (BMI).

    Parameters:
        berat_kg (float): Berat badan dalam kilogram.
        tinggi_m (float): Tinggi badan dalam meter.

    Returns:
        float: Nilai BMI.
    """
    return berat_kg / (tinggi_m ** 2)

# Membaca docstring
help(hitung_bmi)
print(hitung_bmi.__doc__)
```

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Membaca materi modul Minggu 5 tentang fungsi dan modularitas.
- Menonton video pendek: "Functions in Python — Crash Course" (sumber disediakan di LMS).
- Mencatat minimal 2 pertanyaan tentang konsep fungsi untuk didiskusikan di kelas.

### In-class (120 menit)

| Waktu (menit) | Kegiatan                                              | Metode           |
|----------------|-------------------------------------------------------|------------------|
| 0 -- 10        | Review pre-class dan tanya jawab pembuka               | Diskusi          |
| 10 -- 35       | Ceramah: definisi fungsi, parameter, return, scope     | Ceramah          |
| 35 -- 60       | Live coding: top-down design program kalkulator nilai   | Demonstrasi      |
| 60 -- 70       | Istirahat                                              | —                |
| 70 -- 100      | Latihan refactoring: mengubah kode prosedural menjadi modular | Praktikum   |
| 100 -- 115     | Presentasi hasil refactoring oleh 2-3 kelompok         | Presentasi       |
| 115 -- 120     | Ringkasan dan pengantar tugas T3                       | Ceramah          |

### Post-class (15 menit)
- Menyelesaikan latihan tambahan tentang fungsi di Google Colab.
- Mengerjakan Tugas T3 (lihat bagian Penugasan).
- Membaca materi Minggu 6 tentang String dan Pengolahan Teks sebagai persiapan.

---

## Penugasan

### Tugas T3: Refactoring with Functions

| Komponen         | Detail                                                         |
|------------------|----------------------------------------------------------------|
| Jenis            | Tugas Individu                                                 |
| Bobot            | Sesuai RPS                                                     |
| Deadline         | Minggu 6 (sebelum kelas dimulai)                               |
| Submission       | Google Colab notebook via LMS                                  |

**Deskripsi:**
Diberikan sebuah program prosedural (tanpa fungsi) sepanjang kurang lebih 80 baris yang menghitung statistik nilai mahasiswa. Mahasiswa diminta untuk:

1. Mengidentifikasi bagian kode yang berulang atau dapat dimodularkan.
2. Melakukan refactoring dengan membuat minimal 5 fungsi yang bermakna.
3. Menambahkan docstring pada setiap fungsi.
4. Memastikan program tetap menghasilkan output yang sama sebelum dan sesudah refactoring.

**Kriteria Penilaian:**

| Kriteria                        | Bobot |
|---------------------------------|-------|
| Ketepatan pemecahan fungsi       | 30%   |
| Penggunaan parameter dan return  | 25%   |
| Dokumentasi (docstring)          | 20%   |
| Kode berjalan tanpa error        | 15%   |
| Kerapihan dan penamaan           | 10%   |

---

## Referensi

1. Downey, A. (2015). *Think Python: How to Think Like a Computer Scientist*, 2nd Edition. O'Reilly Media. — Chapter 3: Functions.
2. Matthes, E. (2023). *Python Crash Course*, 3rd Edition. No Starch Press. — Chapter 8: Functions.
3. Python Software Foundation. "Defining Functions." *Python 3 Documentation*. [https://docs.python.org/3/tutorial/controlflow.html#defining-functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
4. Sweigart, A. (2019). *Automate the Boring Stuff with Python*, 2nd Edition. No Starch Press. — Chapter 3: Functions.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
