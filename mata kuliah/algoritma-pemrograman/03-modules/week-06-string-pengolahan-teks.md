# Minggu 6: String dan Pengolahan Teks

## Informasi Modul

| Komponen       | Detail                                                           |
|----------------|------------------------------------------------------------------|
| Mata Kuliah    | Algoritma dan Pemrograman (3 SKS)                                |
| Minggu         | 6 (Enam)                                                        |
| Topik          | String dan Pengolahan Teks                                       |
| CPMK           | CPMK-4: Mampu menerapkan prinsip modularitas dalam pemrograman   |
| Sub-CPMK       | CPMK-4.5, CPMK-4.6, CPMK-4.7, CPMK-4.8                        |
| Durasi         | 150 menit                                                        |
| Metode         | Ceramah, live coding, praktikum                                  |
| Pengajar       | Tri Aji Nugroho, S.T., M.T.                                     |
| Program Studi  | Informatika, Universitas Al Azhar Indonesia                      |
| Semester       | Genap 2025/2026                                                  |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menganalisis** string sebagai sequence dan menerapkan indexing serta slicing untuk memanipulasi karakter (CPMK-4.5).
2. **Menggunakan** string methods bawaan Python untuk pengolahan dan transformasi teks (CPMK-4.6).
3. **Menerapkan** formatting string menggunakan f-string untuk output yang terstruktur (CPMK-4.7).
4. **Mengimplementasikan** file I/O dasar (baca/tulis file teks, CSV sederhana) dengan statement `with` (CPMK-4.8).

---

## Materi Pembelajaran

### 6.1 String sebagai Sequence

String adalah urutan karakter yang bersifat **immutable** (tidak dapat diubah setelah dibuat).

```python
teks = "Informatika"
print(teks[0])      # 'I'       (indexing)
print(teks[-1])     # 'a'       (indeks negatif)
print(teks[0:5])    # 'Infor'   (slicing)
print(teks[::-1])   # 'akitamrofnI' (reverse)
```

| Operasi        | Sintaks           | Contoh                | Hasil      |
|----------------|-------------------|-----------------------|------------|
| Indexing       | `s[i]`            | `"Python"[0]`         | `'P'`      |
| Negative index | `s[-i]`           | `"Python"[-1]`        | `'n'`      |
| Slicing        | `s[start:stop]`   | `"Python"[1:4]`       | `'yth'`    |
| Length          | `len(s)`          | `len("Python")`       | `6`        |
| Membership     | `x in s`          | `'th' in "Python"`    | `True`     |
| Concatenation  | `s1 + s2`         | `"Py" + "thon"`       | `'Python'` |
| Repetition     | `s * n`           | `"Ha" * 3`            | `'HaHaHa'` |

### 6.2 String Methods

```python
kalimat = "  Selamat Datang di UAI  "
print(kalimat.strip())       # hapus spasi awal/akhir
print(kalimat.lower())       # huruf kecil semua
print(kalimat.upper())       # huruf besar semua
print(kalimat.find("UAI"))   # indeks kemunculan pertama
print(kalimat.replace("UAI", "Universitas Al Azhar"))
print(kalimat.split())       # pecah jadi list kata

buah = ["apel", "mangga", "jeruk"]
print(", ".join(buah))       # "apel, mangga, jeruk"

# Validasi
print("12345".isdigit())     # True
print("abc".isalpha())       # True
```

### 6.3 String Formatting dengan f-string

```python
nama = "Ahmad"
nilai = 87.5
print(f"Nama: {nama}, Nilai: {nilai}")

# Format angka
pi = 3.14159265
print(f"Pi = {pi:.2f}")             # Pi = 3.14
print(f"Harga: Rp{50000:,.0f}")     # Harga: Rp50,000

# Alignment dan padding
for item, harga in [("Nasi Goreng", 25000), ("Es Teh", 5000)]:
    print(f"{item:<20} Rp{harga:>10,.0f}")
```

### 6.4 File I/O Dasar

```python
# Menulis file
with open("output.txt", "w") as f:
    f.write("Baris pertama\n")
    f.write("Baris kedua\n")

# Membaca seluruh file
with open("output.txt", "r") as f:
    isi = f.read()
    print(isi)

# Membaca baris per baris
with open("output.txt", "r") as f:
    for baris in f:
        print(baris.strip())
```

| Mode   | Keterangan                                       |
|--------|--------------------------------------------------|
| `"r"`  | Read -- membaca (default, error jika tidak ada)  |
| `"w"`  | Write -- menulis (buat baru / timpa)             |
| `"a"`  | Append -- menambahkan di akhir file              |

> **Penting:** Selalu gunakan statement `with` agar file ditutup otomatis meskipun terjadi error.

### 6.5 CSV Sederhana

```python
# Menulis CSV
data = [["NIM","Nama","Nilai"], ["001","Ahmad","85"], ["002","Budi","90"]]
with open("mahasiswa.csv", "w") as f:
    for baris in data:
        f.write(",".join(baris) + "\n")

# Membaca CSV
with open("mahasiswa.csv", "r") as f:
    for baris in f:
        kolom = baris.strip().split(",")
        print(f"NIM: {kolom[0]}, Nama: {kolom[1]}, Nilai: {kolom[2]}")
```

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Membaca materi modul Minggu 6 tentang string dan file I/O.
- Mencoba eksperimen singkat di Google Colab: buat string, coba 3 method berbeda.
- Menyiapkan file teks sederhana (`.txt`) untuk latihan file I/O.

### In-class (120 menit)

| Waktu (menit) | Kegiatan                                                  | Metode      |
|----------------|----------------------------------------------------------|-------------|
| 0 -- 10        | Review pre-class, pengumpulan Tugas T3, tanya jawab       | Diskusi     |
| 10 -- 35       | Ceramah: string sequence, indexing, slicing, methods       | Ceramah     |
| 35 -- 55       | Live coding: pengolahan teks -- analisis frekuensi kata    | Demonstrasi |
| 55 -- 65       | Istirahat                                                 | --          |
| 65 -- 80       | Ceramah: f-string formatting dan file I/O                 | Ceramah     |
| 80 -- 110      | Praktikum: membaca file teks, memproses data, menulis CSV | Praktikum   |
| 110 -- 120     | Diskusi hasil praktikum dan ringkasan materi              | Diskusi     |

### Post-class (15 menit)
- Menyelesaikan latihan tambahan tentang string methods di Google Colab.
- Eksplorasi mandiri: dokumentasi Python tentang `str` methods.
- Membaca materi Minggu 7 (List, Tuple, dan Operasi Koleksi).

---

## Penugasan

Tidak ada tugas formal pada minggu ini. Mahasiswa diharapkan menyelesaikan latihan praktikum file I/O yang diberikan di kelas dan menyiapkan diri untuk Tugas T4 dan Kuis K2 pada Minggu 7.

---

## Referensi

1. Downey, A. (2015). *Think Python*, 2nd Ed. O'Reilly. -- Ch. 8: Strings, Ch. 14: Files.
2. Matthes, E. (2023). *Python Crash Course*, 3rd Ed. No Starch Press. -- Ch. 6: Strings, Ch. 10: Files.
3. Python Docs. "String Methods." [https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
4. Python Docs. "Reading and Writing Files." [https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
