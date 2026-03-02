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

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Mendefinisikan** fungsi menggunakan keyword `def`, parameter, dan `return` untuk memecah program menjadi unit modular (CPMK-4.1).
2. **Membedakan** variabel lokal dan global serta menjelaskan konsep scope dalam konteks fungsi (CPMK-4.2).
3. **Menerapkan** prinsip DRY dan pendekatan top-down design dalam perancangan solusi algoritmik (CPMK-4.3).
4. **Mendokumentasikan** fungsi menggunakan docstring dan memanfaatkan `help()` untuk membaca dokumentasi (CPMK-4.4).

---

## Materi Pembelajaran

### 5.1 Pengantar Fungsi

Fungsi adalah blok kode reusable untuk melakukan tugas tertentu, membantu memecah program besar menjadi bagian kecil yang mudah dipahami dan dipelihara.

| Manfaat       | Penjelasan                                     |
|---------------|-------------------------------------------------|
| Reusability   | Kode ditulis sekali, dipanggil berkali-kali     |
| Abstraksi     | Menyembunyikan detail implementasi              |
| Modularitas   | Memecah masalah besar menjadi sub-masalah kecil |
| Keterbacaan   | Program lebih mudah dibaca dan dipahami         |

### 5.2 Mendefinisikan dan Memanggil Fungsi

```python
def nama_fungsi(parameter1, parameter2):
    """Docstring: penjelasan singkat fungsi."""
    hasil = parameter1 + parameter2
    return hasil

total = nama_fungsi(10, 20)
print(total)  # Output: 30
```

### 5.3 Parameter dan Argumen

```python
# Positional parameter
def sapa(nama, pesan):
    print(f"{pesan}, {nama}!")

# Default parameter
def hitung_luas(sisi, satuan="cm"):
    return f"{sisi ** 2} {satuan}^2"

print(hitung_luas(5))       # 25 cm^2
print(hitung_luas(5, "m"))  # 25 m^2

# Keyword argument
def profil(nama, umur, kota):
    print(f"{nama}, {umur} tahun, dari {kota}")

profil(kota="Jakarta", nama="Budi", umur=20)
```

### 5.4 Return Value

```python
def hitung_statistik(data):
    return min(data), max(data), sum(data) / len(data)

low, high, avg = hitung_statistik([10, 20, 30, 40, 50])
print(f"Min={low}, Max={high}, Avg={avg}")
```

### 5.5 Scope: Variabel Lokal dan Global

```python
pesan_global = "Halo Dunia"       # variabel global

def demo_scope():
    pesan_lokal = "Halo Lokal"    # variabel lokal
    print(pesan_global)           # bisa akses global
    print(pesan_lokal)

demo_scope()
# print(pesan_lokal)  # ERROR: tidak bisa diakses di luar fungsi
```

| Aspek            | Variabel Lokal              | Variabel Global                |
|------------------|-----------------------------|--------------------------------|
| Didefinisikan di | Dalam fungsi                | Di luar fungsi (level modul)   |
| Dapat diakses    | Hanya dalam fungsi tersebut | Seluruh program                |
| Best practice    | Gunakan sebanyak mungkin    | Hindari jika memungkinkan      |

### 5.6 Prinsip DRY dan Top-Down Design

```python
# SEBELUM (melanggar DRY)            # SETELAH (mengikuti DRY)
print("=" * 40)                       def cetak_header(judul):
print("LAPORAN NILAI")                    print("=" * 40)
print("=" * 40)                            print(judul)
# ...                                     print("=" * 40)
print("=" * 40)
print("LAPORAN KEHADIRAN")            cetak_header("LAPORAN NILAI")
print("=" * 40)                       cetak_header("LAPORAN KEHADIRAN")
```

**Top-Down Design** -- memecah masalah besar menjadi sub-fungsi:

```python
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

help(hitung_bmi)
```

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Membaca materi modul Minggu 5 tentang fungsi dan modularitas.
- Menonton video pendek: "Functions in Python" (disediakan di LMS).
- Mencatat minimal 2 pertanyaan tentang konsep fungsi.

### In-class (120 menit)

| Waktu (menit) | Kegiatan                                           | Metode      |
|----------------|---------------------------------------------------|-------------|
| 0 -- 10        | Review pre-class dan tanya jawab pembuka           | Diskusi     |
| 10 -- 35       | Ceramah: definisi fungsi, parameter, return, scope | Ceramah     |
| 35 -- 60       | Live coding: top-down design kalkulator nilai      | Demonstrasi |
| 60 -- 70       | Istirahat                                          | --          |
| 70 -- 100      | Latihan refactoring: prosedural menjadi modular    | Praktikum   |
| 100 -- 115     | Presentasi hasil refactoring (2-3 kelompok)        | Presentasi  |
| 115 -- 120     | Ringkasan dan pengantar Tugas T3                   | Ceramah     |

### Post-class (15 menit)
- Menyelesaikan latihan tambahan tentang fungsi di Google Colab.
- Mengerjakan Tugas T3.
- Membaca materi Minggu 6 (String dan Pengolahan Teks).

---

## Penugasan

### Tugas T3: Refactoring with Functions

| Komponen   | Detail                                   |
|------------|------------------------------------------|
| Jenis      | Tugas Individu                           |
| Deadline   | Minggu 6 (sebelum kelas dimulai)         |
| Submission | Google Colab notebook via LMS            |

**Deskripsi:** Diberikan program prosedural (~80 baris) yang menghitung statistik nilai mahasiswa. Mahasiswa diminta: (1) mengidentifikasi bagian kode yang berulang, (2) melakukan refactoring dengan minimal 5 fungsi, (3) menambahkan docstring pada setiap fungsi, (4) memastikan output tetap sama.

| Kriteria                       | Bobot |
|--------------------------------|-------|
| Ketepatan pemecahan fungsi     | 30%   |
| Penggunaan parameter & return  | 25%   |
| Dokumentasi (docstring)        | 20%   |
| Kode berjalan tanpa error      | 15%   |
| Kerapihan dan penamaan         | 10%   |

---

## Referensi

1. Downey, A. (2015). *Think Python*, 2nd Ed. O'Reilly. -- Ch. 3: Functions.
2. Matthes, E. (2023). *Python Crash Course*, 3rd Ed. No Starch Press. -- Ch. 8: Functions.
3. Python Docs. "Defining Functions." [https://docs.python.org/3/tutorial/controlflow.html#defining-functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
4. Sweigart, A. (2019). *Automate the Boring Stuff with Python*, 2nd Ed. -- Ch. 3: Functions.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
