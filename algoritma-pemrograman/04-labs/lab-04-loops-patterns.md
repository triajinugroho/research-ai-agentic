# Lab 04: Loops dan Patterns

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Durasi** | 75 menit |
| **Prasyarat** | Lab 03 — Conditional Logic |

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:
- Menggunakan `for` loop dengan `range()` dan `while` loop
- Mengontrol alur perulangan dengan `break` dan `continue`
- Membuat pola (*patterns*) menggunakan perulangan bersarang
- Membangun program tabel perkalian dan game tebak angka

---

## Persiapan

1. Buka Google Colab dan buat notebook baru
2. Beri nama `Lab04_NamaAnda_NIM.ipynb`
3. Pastikan Anda telah memahami percabangan (`if-elif-else`)

---

## Langkah-langkah

### Langkah 1 — `for` Loop dengan `range()`

```python
# Menampilkan nama-nama hari
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

print("=== Daftar Hari ===")
for h in hari:
    print(f"  - {h}")

# Menggunakan range()
print("\n=== Bilangan 1-10 ===")
for i in range(1, 11):
    print(i, end=" ")
print()  # baris baru

# range(start, stop, step)
print("\n=== Bilangan Genap 2-20 ===")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# Hitung mundur
print("\n=== Hitung Mundur ===")
for i in range(10, 0, -1):
    print(i, end="... ")
print("LIFTOFF!")
```

### Langkah 2 — `while` Loop

```python
# While loop: hitung total belanja
print("=== KASIR MINIMARKET ===")
print("(Ketik 0 untuk selesai)")
print()

total = 0
item_ke = 1

while True:
    harga = float(input(f"Harga item ke-{item_ke}: Rp"))
    if harga == 0:
        break
    total += harga
    print(f"  Subtotal: Rp{total:,.0f}")
    item_ke += 1

print(f"\n{'=' * 30}")
print(f"Total belanja : Rp{total:,.0f}")
print(f"Jumlah item   : {item_ke - 1}")
```

### Langkah 3 — `break` dan `continue`

```python
# Contoh break: cari bilangan prima pertama setelah N
n = int(input("Cari bilangan prima pertama setelah: "))
calon = n + 1

while True:
    prima = True
    for i in range(2, int(calon ** 0.5) + 1):
        if calon % i == 0:
            prima = False
            break
    if prima:
        print(f"Bilangan prima pertama setelah {n} adalah {calon}")
        break
    calon += 1

# Contoh continue: cetak hanya bilangan ganjil
print("\nBilangan ganjil 1-20:")
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()
```

### Langkah 4 — Akumulasi dengan Loop

```python
# Menghitung rata-rata nilai kelas
print("=== RATA-RATA NILAI KELAS ===")
jumlah_siswa = int(input("Jumlah siswa: "))

total_nilai = 0
nilai_tertinggi = 0
nilai_terendah = 100

for i in range(1, jumlah_siswa + 1):
    nilai = float(input(f"Nilai siswa ke-{i}: "))
    total_nilai += nilai
    if nilai > nilai_tertinggi:
        nilai_tertinggi = nilai
    if nilai < nilai_terendah:
        nilai_terendah = nilai

rata_rata = total_nilai / jumlah_siswa

print(f"\n--- Statistik Kelas ---")
print(f"Jumlah siswa     : {jumlah_siswa}")
print(f"Total nilai      : {total_nilai:.1f}")
print(f"Rata-rata        : {rata_rata:.2f}")
print(f"Nilai tertinggi  : {nilai_tertinggi:.1f}")
print(f"Nilai terendah   : {nilai_terendah:.1f}")
```

### Langkah 5 — Nested Loops: Pola Bintang

```python
# === POLA 1: Segitiga Siku-Siku Kanan ===
n = 5
print("Pola 1: Segitiga Siku-Siku Kanan")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# === POLA 2: Segitiga Terbalik ===
print("\nPola 2: Segitiga Terbalik")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# === POLA 3: Piramida ===
print("\nPola 3: Piramida")
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)

# === POLA 4: Diamond (Belah Ketupat) ===
print("\nPola 4: Diamond")
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)

# === POLA 5: Segitiga Angka ===
print("\nPola 5: Segitiga Angka")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

### Langkah 6 — Mini Project: Tabel Perkalian 1-10

```python
# =============================================
# MINI PROJECT 1: Tabel Perkalian 1-10
# =============================================

print("=" * 67)
print("                    TABEL PERKALIAN 1-10")
print("=" * 67)

# Header kolom
print(f"{'X':>4}", end="")
for j in range(1, 11):
    print(f"{j:>6}", end="")
print()
print("-" * 67)

# Isi tabel
for i in range(1, 11):
    print(f"{i:>4}", end="")
    for j in range(1, 11):
        print(f"{i * j:>6}", end="")
    print()

print("-" * 67)
```

### Langkah 7 — Mini Project: Game Tebak Angka

```python
# =============================================
# MINI PROJECT 2: Game Tebak Angka
# =============================================
import random

print("=" * 40)
print("     GAME TEBAK ANGKA")
print("=" * 40)
print("Komputer memilih angka antara 1-100.")
print("Anda punya 7 kesempatan untuk menebak!")
print()

angka_rahasia = random.randint(1, 100)
maksimal_tebakan = 7
berhasil = False

for percobaan in range(1, maksimal_tebakan + 1):
    sisa = maksimal_tebakan - percobaan
    tebakan = int(input(f"Tebakan ke-{percobaan} (sisa {sisa + 1}): "))

    if tebakan == angka_rahasia:
        print(f"\nSELAMAT! Anda menebak dengan benar!")
        print(f"Angka rahasia: {angka_rahasia}")
        print(f"Jumlah percobaan: {percobaan}")

        if percobaan <= 3:
            print("Peringkat: LUAR BIASA!")
        elif percobaan <= 5:
            print("Peringkat: BAGUS!")
        else:
            print("Peringkat: CUKUP BAIK!")

        berhasil = True
        break
    elif tebakan < angka_rahasia:
        print("   >> Terlalu KECIL! Coba lebih besar.")
    else:
        print("   >> Terlalu BESAR! Coba lebih kecil.")

if not berhasil:
    print(f"\nMaaf, kesempatan habis!")
    print(f"Angka rahasia adalah: {angka_rahasia}")
    print("Coba lagi lain waktu!")

print("\nTerima kasih sudah bermain!")
```

---

## Tantangan Tambahan

1. **Deret Fibonacci**: Buat program yang menampilkan N bilangan pertama dalam deret Fibonacci (0, 1, 1, 2, 3, 5, 8, ...) menggunakan loop. Tampilkan juga jumlah total deret.

2. **Pola Jam Pasir**: Buat pola jam pasir (*hourglass*) dari bintang dengan ukuran N yang diinput pengguna. Contoh untuk N=5:
   ```
   * * * * *
    * * * *
     * * *
      * *
       *
      * *
     * * *
    * * * *
   * * * * *
   ```

3. **Faktor Prima**: Buat program yang meminta input bilangan bulat positif, lalu menampilkan semua faktor primanya. Contoh: 60 = 2 x 2 x 3 x 5.

---

## Checklist Penyelesaian

- [ ] Mampu menggunakan `for` loop dengan `range()`
- [ ] Mampu menggunakan `while` loop
- [ ] Memahami dan menggunakan `break` dan `continue`
- [ ] Mampu membuat minimal 3 pola bintang berbeda
- [ ] Menyelesaikan Mini Project: Tabel Perkalian 1-10
- [ ] Menyelesaikan Mini Project: Game Tebak Angka
- [ ] Mengerjakan minimal 1 tantangan tambahan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
