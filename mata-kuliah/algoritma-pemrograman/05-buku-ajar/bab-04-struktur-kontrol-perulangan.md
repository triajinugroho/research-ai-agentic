# BAB 4: STRUKTUR KONTROL: PERULANGAN

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's |
|----------|-----------|---------|
| CPMK-3.5 | Menjelaskan konsep perulangan dan jenisnya | C2 |
| CPMK-3.6 | Menerapkan perulangan `for` untuk iterasi tertentu | C3 |
| CPMK-3.7 | Menerapkan perulangan `while` untuk kondisi tertentu | C3 |
| CPMK-3.8 | Mengimplementasikan nested loops dan pola-pola perulangan | C3 |

---

## 4.1 Konsep Perulangan

### 4.1.1 Mengapa Perlu Perulangan?

Bayangkan Anda diminta untuk mencetak angka 1 sampai 100. Tanpa perulangan, kode Anda akan terlihat seperti ini:

```python
# TANPA perulangan — cara yang SANGAT tidak efisien!
print(1)
print(2)
print(3)
print(4)
print(5)
# ... (bayangkan menulis ini sampai 100 baris!)
print(98)
print(99)
print(100)
```

Anda harus menulis **100 baris kode** hanya untuk mencetak angka! Bagaimana jika diminta mencetak sampai 10.000? Atau 1.000.000? Tentu saja hal ini tidak masuk akal.

Dengan perulangan (loop), tugas yang sama bisa diselesaikan dalam **3 baris**:

```python
# DENGAN perulangan — efisien dan elegan
for i in range(1, 101):
    print(i)
```

**Analogi kehidupan sehari-hari:**

Perulangan ada di mana-mana dalam kehidupan kita:
- "Ulangi sholat **5 kali sehari**" — jumlah iterasi diketahui (seperti `for` loop)
- "Cetak **100 sertifikat** untuk peserta seminar" — iterasi tertentu
- "Aduk adonan **sampai mengental**" — iterasi bergantung kondisi (seperti `while` loop)
- "Terus belajar **sampai lulus**" — kondisi akhir belum pasti
- "Ulangi input **sampai benar**" — validasi data

**Prinsip DRY (Don't Repeat Yourself):**

Dalam pemrograman, salah satu prinsip terpenting adalah **DRY** — jangan mengulang diri sendiri. Perulangan adalah alat utama untuk menerapkan prinsip ini. Kode yang berulang rentan terhadap kesalahan: jika Anda perlu mengubah sesuatu, Anda harus mengubahnya di banyak tempat. Dengan loop, perubahan cukup dilakukan di satu tempat.

### 4.1.2 Jenis Perulangan dalam Python

Python menyediakan dua jenis perulangan utama:

| Jenis | Nama | Digunakan Ketika | Contoh Situasi |
|-------|------|-------------------|----------------|
| `for` | Counted Loop | Jumlah iterasi **diketahui** atau iterasi atas koleksi | Cetak 1-100, proses setiap item dalam list |
| `while` | Conditional Loop | Iterasi bergantung pada **kondisi** | Input validation, game loop |

**Kapan menggunakan `for`:**
- Anda tahu berapa kali harus mengulang
- Anda ingin mengiterasi setiap elemen dalam koleksi (list, string, tuple, dll.)

**Kapan menggunakan `while`:**
- Anda tidak tahu berapa kali harus mengulang
- Perulangan berhenti ketika suatu kondisi terpenuhi (atau tidak terpenuhi)

### 4.1.3 Flowchart Perulangan

Secara umum, flowchart perulangan memiliki struktur sebagai berikut:

```
        ┌─────────────┐
        │    START     │
        └──────┬──────┘
               │
               ▼
        ┌─────────────┐
        │ Inisialisasi │
        │  variabel    │
        └──────┬──────┘
               │
               ▼
          ┌─────────┐      Tidak
          │ Kondisi  │─────────────┐
          │ terpenuhi│             │
          │    ?     │             │
          └────┬─────┘             │
               │ Ya                │
               ▼                   │
        ┌─────────────┐            │
        │   Proses /   │            │
        │  Blok Kode   │            │
        └──────┬──────┘            │
               │                   │
               ▼                   │
        ┌─────────────┐            │
        │   Update     │            │
        │  variabel    │            │
        └──────┬──────┘            │
               │                   │
               └───────┐           │
                       │           │
               (kembali ke         │
                kondisi)           │
                                   │
                                   ▼
                            ┌─────────────┐
                            │     END      │
                            └─────────────┘
```

Perhatikan bahwa loop selalu memiliki tiga komponen penting:
1. **Inisialisasi** — menyiapkan variabel kontrol
2. **Kondisi** — menentukan apakah loop terus berjalan
3. **Update** — mengubah variabel kontrol agar loop akhirnya berhenti

---

## 4.2 Perulangan `for`

### 4.2.1 Sintaks Dasar

Perulangan `for` di Python digunakan untuk mengiterasi (mengulangi) setiap elemen dalam suatu *sequence* (urutan). Sintaksnya adalah:

```python
for variabel in sequence:
    # blok kode yang diulang
    # HARUS di-indent (4 spasi)
```

Cara kerja:
1. Python mengambil elemen pertama dari `sequence` dan memasukkannya ke `variabel`
2. Blok kode di dalam `for` dijalankan
3. Python mengambil elemen berikutnya dan memasukkannya ke `variabel`
4. Blok kode dijalankan lagi
5. Proses berulang sampai semua elemen dalam `sequence` telah diproses

Contoh paling sederhana:

```python
# Cetak angka 0 sampai 4
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

### 4.2.2 Fungsi `range()`

Fungsi `range()` adalah "sahabat" dari `for` loop di Python. Fungsi ini menghasilkan deretan angka sesuai parameter yang diberikan.

**Tiga bentuk `range()`:**

```python
range(stop)                # Mulai dari 0, naik 1, berhenti SEBELUM stop
range(start, stop)         # Mulai dari start, naik 1, berhenti SEBELUM stop
range(start, stop, step)   # Mulai dari start, naik step, berhenti SEBELUM stop
```

**Tabel contoh penggunaan `range()`:**

| Ekspresi | Menghasilkan | Penjelasan |
|----------|-------------|------------|
| `range(5)` | 0, 1, 2, 3, 4 | 5 angka mulai dari 0 |
| `range(1, 6)` | 1, 2, 3, 4, 5 | Mulai dari 1, berhenti sebelum 6 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 | Bilangan genap 0-9 |
| `range(1, 10, 2)` | 1, 3, 5, 7, 9 | Bilangan ganjil 1-9 |
| `range(10, 0, -1)` | 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 | Hitung mundur |
| `range(10, 0, -2)` | 10, 8, 6, 4, 2 | Hitung mundur loncat 2 |
| `range(5, 5)` | *(kosong)* | Start == stop, tidak ada elemen |
| `range(5, 1)` | *(kosong)* | Start > stop tanpa step negatif |

**Contoh kode untuk setiap variasi:**

```python
# range(stop) — mulai dari 0
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()  # Output: 0 1 2 3 4

# range(start, stop) — mulai dari start
print("range(1, 6):")
for i in range(1, 6):
    print(i, end=" ")
print()  # Output: 1 2 3 4 5

# range(start, stop, step) — dengan loncatan
print("range(0, 10, 2) - bilangan genap:")
for i in range(0, 10, 2):
    print(i, end=" ")
print()  # Output: 0 2 4 6 8

# range dengan step negatif — hitung mundur
print("range(10, 0, -1) - hitung mundur:")
for i in range(10, 0, -1):
    print(i, end=" ")
print()  # Output: 10 9 8 7 6 5 4 3 2 1

# range mundur loncat 2
print("range(10, 0, -2):")
for i in range(10, 0, -2):
    print(i, end=" ")
print()  # Output: 10 8 6 4 2
```

> **Catatan Penting:** `range()` berhenti **SEBELUM** nilai `stop`. Ini adalah sumber kesalahan umum bagi pemula! Jika Anda ingin angka 1 sampai 10, gunakan `range(1, 11)`, bukan `range(1, 10)`.

### 4.2.3 Iterasi atas Sequence

Selain `range()`, `for` loop dapat mengiterasi langsung atas berbagai tipe data sequence.

**Iterasi atas string:**

```python
# Setiap karakter dalam string adalah elemen
nama = "INFORMATIKA"
for huruf in nama:
    print(huruf, end=" ")
print()
# Output: I N F O R M A T I K A
```

**Iterasi atas list:**

```python
# Iterasi langsung atas elemen list
buah = ["Mangga", "Jeruk", "Apel", "Durian", "Rambutan"]
for item in buah:
    print(f"Saya suka {item}")
```

Output:
```
Saya suka Mangga
Saya suka Jeruk
Saya suka Apel
Saya suka Durian
Saya suka Rambutan
```

**Iterasi dengan `enumerate()` — mendapatkan index dan nilai:**

```python
# enumerate() memberikan index dan nilai sekaligus
menu = ["Nasi Goreng", "Mie Ayam", "Soto Betawi", "Gado-gado"]
for i, makanan in enumerate(menu, 1):
    print(f"{i}. {makanan}")
```

Output:
```
1. Nasi Goreng
2. Mie Ayam
3. Soto Betawi
4. Gado-gado
```

> **Catatan:** Parameter kedua pada `enumerate(menu, 1)` berarti penomoran dimulai dari 1, bukan dari 0.

**Iterasi atas dictionary:**

```python
# Iterasi atas key-value pairs
mahasiswa = {
    "Ahmad": 85,
    "Budi": 92,
    "Citra": 78,
    "Dewi": 95
}

for nama, nilai in mahasiswa.items():
    print(f"{nama}: {nilai}")
```

Output:
```
Ahmad: 85
Budi: 92
Citra: 78
Dewi: 95
```

### 4.2.4 Contoh-contoh Praktis

**Contoh 1: Hitung total belanja dari list harga**

```python
# Daftar harga belanjaan
harga_belanja = [15000, 25000, 8500, 32000, 12500, 45000]

total = 0
print("=== RINCIAN BELANJA ===")
for i, harga in enumerate(harga_belanja, 1):
    print(f"Item {i}: Rp {harga:,}")
    total += harga

print(f"{'='*25}")
print(f"TOTAL   : Rp {total:,}")
```

Output:
```
=== RINCIAN BELANJA ===
Item 1: Rp 15,000
Item 2: Rp 25,000
Item 3: Rp 8,500
Item 4: Rp 32,000
Item 5: Rp 12,500
Item 6: Rp 45,000
=========================
TOTAL   : Rp 138,000
```

**Contoh 2: Cetak tabel perkalian**

```python
# Tabel perkalian 7
angka = 7
print(f"=== Tabel Perkalian {angka} ===")
for i in range(1, 11):
    hasil = angka * i
    print(f"{angka} x {i:2d} = {hasil:3d}")
```

Output:
```
=== Tabel Perkalian 7 ===
7 x  1 =   7
7 x  2 =  14
7 x  3 =  21
7 x  4 =  28
7 x  5 =  35
7 x  6 =  42
7 x  7 =  49
7 x  8 =  56
7 x  9 =  63
7 x 10 =  70
```

**Contoh 3: Hitung rata-rata nilai mahasiswa**

```python
# Data nilai mahasiswa
nilai_mahasiswa = [85, 90, 78, 92, 88, 76, 95, 83, 70, 91]

total = 0
tertinggi = nilai_mahasiswa[0]
terendah = nilai_mahasiswa[0]

for nilai in nilai_mahasiswa:
    total += nilai
    if nilai > tertinggi:
        tertinggi = nilai
    if nilai < terendah:
        terendah = nilai

rata_rata = total / len(nilai_mahasiswa)

print(f"Jumlah mahasiswa : {len(nilai_mahasiswa)}")
print(f"Total nilai      : {total}")
print(f"Rata-rata        : {rata_rata:.2f}")
print(f"Nilai tertinggi  : {tertinggi}")
print(f"Nilai terendah   : {terendah}")
```

Output:
```
Jumlah mahasiswa : 10
Total nilai      : 848
Rata-rata        : 84.80
Nilai tertinggi  : 95
Nilai terendah   : 70
```

**Contoh 4: Hitung mundur (countdown)**

```python
# Countdown peluncuran roket
import time

print("Persiapan peluncuran...")
for i in range(10, 0, -1):
    print(f"  {i}...")
    # time.sleep(1)  # Uncomment untuk jeda 1 detik per hitungan
print("LIFTOFF!")
```

Output:
```
Persiapan peluncuran...
  10...
  9...
  8...
  7...
  6...
  5...
  4...
  3...
  2...
  1...
LIFTOFF!
```

---

## 4.3 Perulangan `while`

### 4.3.1 Sintaks Dasar

Perulangan `while` menjalankan blok kode **selama kondisi bernilai `True`**. Begitu kondisi bernilai `False`, loop berhenti.

```python
while kondisi:
    # blok kode yang diulang
    # PENTING: harus ada pernyataan yang mengubah kondisi
    # agar loop tidak berjalan selamanya (infinite loop)!
```

Struktur dasar `while` loop:

```python
# 1. Inisialisasi variabel kontrol
counter = 0

# 2. Kondisi dicek SEBELUM setiap iterasi
while counter < 5:
    # 3. Blok kode dijalankan
    print(f"Iterasi ke-{counter}")
    # 4. Update variabel kontrol
    counter += 1

print("Loop selesai!")
```

Output:
```
Iterasi ke-0
Iterasi ke-1
Iterasi ke-2
Iterasi ke-3
Iterasi ke-4
Loop selesai!
```

### 4.3.2 Contoh-contoh

**Contoh 1: Hitung mundur peluncuran roket**

```python
hitungan = 10
while hitungan > 0:
    print(f"{hitungan}...")
    hitungan -= 1
print("LIFTOFF!")
```

Output:
```
10...
9...
8...
7...
6...
5...
4...
3...
2...
1...
LIFTOFF!
```

**Contoh 2: Input validation loop**

```python
# Loop terus berjalan sampai user memasukkan input yang valid
while True:
    try:
        umur = int(input("Masukkan umur (1-120): "))
        if 1 <= umur <= 120:
            break
        print("Umur tidak valid! Harus antara 1-120. Coba lagi.")
    except ValueError:
        print("Input harus berupa angka! Coba lagi.")

print(f"Umur Anda: {umur} tahun")
```

Contoh interaksi:
```
Masukkan umur (1-120): -5
Umur tidak valid! Harus antara 1-120. Coba lagi.
Masukkan umur (1-120): abc
Input harus berupa angka! Coba lagi.
Masukkan umur (1-120): 150
Umur tidak valid! Harus antara 1-120. Coba lagi.
Masukkan umur (1-120): 21
Umur Anda: 21 tahun
```

**Contoh 3: Game tebak angka**

```python
import random

angka_rahasia = random.randint(1, 100)
tebakan = 0
percobaan = 0

print("=== GAME TEBAK ANGKA ===")
print("Saya memikirkan angka antara 1-100.")
print("Coba tebak!")
print()

while tebakan != angka_rahasia:
    tebakan = int(input("Tebakan Anda: "))
    percobaan += 1

    if tebakan < angka_rahasia:
        print("Terlalu kecil! Coba lagi.")
    elif tebakan > angka_rahasia:
        print("Terlalu besar! Coba lagi.")

print(f"\nBenar! Angkanya adalah {angka_rahasia}.")
print(f"Anda menebak dalam {percobaan} percobaan.")

if percobaan <= 5:
    print("Luar biasa!")
elif percobaan <= 10:
    print("Bagus!")
else:
    print("Terus berlatih!")
```

**Contoh 4: Menghitung digit suatu bilangan**

```python
bilangan = 123456789
bilangan_asli = bilangan
jumlah_digit = 0
total_digit = 0

while bilangan > 0:
    digit = bilangan % 10        # Ambil digit terakhir
    total_digit += digit          # Tambahkan ke total
    jumlah_digit += 1             # Hitung jumlah digit
    bilangan = bilangan // 10     # Hapus digit terakhir

print(f"Bilangan       : {bilangan_asli}")
print(f"Jumlah digit   : {jumlah_digit}")
print(f"Total semua digit: {total_digit}")
```

Output:
```
Bilangan       : 123456789
Jumlah digit   : 9
Total semua digit: 45
```

### 4.3.3 Bahaya Infinite Loop

**Infinite loop** terjadi ketika kondisi `while` **tidak pernah** menjadi `False`. Ini menyebabkan program berjalan tanpa henti.

**Penyebab umum:**

```python
# BAHAYA! Infinite loop — variabel 'i' tidak pernah berubah
i = 0
while i < 5:
    print(i)
    # Lupa: i += 1  <-- TIDAK ADA update!

# BAHAYA! Kondisi selalu True
while True:
    print("Loop ini tidak pernah berhenti!")
    # Tidak ada break statement
```

**Cara menghentikan infinite loop:**
- Di terminal/command prompt: tekan **Ctrl+C**
- Di Google Colab: klik tombol **Stop** (ikon kotak) di samping cell
- Di Jupyter Notebook: klik **Interrupt Kernel**

**Strategi pencegahan:**

1. **Selalu pastikan ada update pada variabel kondisi:**
```python
# BENAR
counter = 0
while counter < 10:
    print(counter)
    counter += 1  # Variabel kontrol di-update
```

2. **Gunakan variabel sentinel (pembatas):**
```python
# BENAR — ada batas maksimum iterasi
max_percobaan = 100
percobaan = 0
while percobaan < max_percobaan:
    # lakukan sesuatu
    percobaan += 1
    if kondisi_terpenuhi:
        break
```

3. **Gunakan `while True` dengan `break` yang jelas:**
```python
# BENAR — ada jalur keluar yang jelas
while True:
    jawaban = input("Lanjut? (y/n): ")
    if jawaban.lower() == 'n':
        break  # Jalur keluar yang jelas
```

---

## 4.4 `break`, `continue`, dan `else`

### 4.4.1 `break` — Keluar dari Loop

Statement `break` menghentikan loop secara **langsung**, bahkan jika kondisi loop masih `True` atau masih ada elemen yang belum diproses.

```python
# Cari bilangan prima pertama yang lebih besar dari 100
angka = 101
while True:
    is_prima = True
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            is_prima = False
            break  # Keluar dari for loop (tidak perlu cek lagi)
    if is_prima:
        print(f"Bilangan prima pertama > 100: {angka}")
        break  # Keluar dari while loop
    angka += 1
```

Output:
```
Bilangan prima pertama > 100: 101
```

**Contoh lain — cari item dalam list:**

```python
# Cari nama mahasiswa
daftar = ["Ahmad", "Budi", "Citra", "Dewi", "Eka", "Fani"]
cari = "Citra"

for i, nama in enumerate(daftar):
    if nama == cari:
        print(f"Ditemukan '{cari}' pada indeks {i}")
        break
else:
    print(f"'{cari}' tidak ditemukan")
```

Output:
```
Ditemukan 'Citra' pada indeks 2
```

### 4.4.2 `continue` — Lewati Iterasi

Statement `continue` melewatkan sisa kode dalam iterasi **saat ini** dan langsung melanjutkan ke iterasi **berikutnya**.

```python
# Cetak bilangan ganjil 1-20 (skip bilangan genap)
print("Bilangan ganjil 1-20:")
for i in range(1, 21):
    if i % 2 == 0:
        continue  # Lewati bilangan genap
    print(i, end=" ")
print()
```

Output:
```
Bilangan ganjil 1-20:
1 3 5 7 9 11 13 15 17 19
```

**Contoh lain — proses data, skip yang tidak valid:**

```python
# Proses nilai, skip yang negatif (dianggap tidak valid)
data_nilai = [85, -1, 90, 78, -5, 92, 88, -3, 95]

total = 0
count = 0

for nilai in data_nilai:
    if nilai < 0:
        print(f"  [SKIP] Nilai {nilai} tidak valid")
        continue
    total += nilai
    count += 1
    print(f"  Proses nilai: {nilai}")

rata_rata = total / count
print(f"\nRata-rata (tanpa data invalid): {rata_rata:.2f}")
```

Output:
```
  Proses nilai: 85
  [SKIP] Nilai -1 tidak valid
  Proses nilai: 90
  Proses nilai: 78
  [SKIP] Nilai -5 tidak valid
  Proses nilai: 92
  Proses nilai: 88
  [SKIP] Nilai -3 tidak valid
  Proses nilai: 95

Rata-rata (tanpa data invalid): 88.00
```

### 4.4.3 `else` pada Loop

Fitur unik Python: Anda bisa menambahkan `else` pada loop. Blok `else` dijalankan **hanya jika** loop selesai secara normal (tanpa `break`).

```python
# Cek apakah bilangan n adalah bilangan prima
n = 29

for i in range(2, n):
    if n % i == 0:
        print(f"{n} bukan bilangan prima (habis dibagi {i})")
        break
else:
    # Blok ini HANYA dijalankan jika for loop selesai TANPA break
    print(f"{n} adalah bilangan prima")
```

Output:
```
29 adalah bilangan prima
```

**Penjelasan cara kerja `for-else`:**
- Jika `break` dieksekusi di dalam loop, blok `else` **dilewati**
- Jika loop selesai secara normal (semua iterasi selesai), blok `else` **dijalankan**

```python
# Contoh ketika break dieksekusi (else TIDAK dijalankan)
n = 24

for i in range(2, n):
    if n % i == 0:
        print(f"{n} bukan bilangan prima (habis dibagi {i})")
        break
else:
    print(f"{n} adalah bilangan prima")
# Output: 24 bukan bilangan prima (habis dibagi 2)
```

**`while-else` juga berlaku:**

```python
# while-else
angka = 1
while angka <= 5:
    print(angka, end=" ")
    angka += 1
else:
    print("\nLoop selesai secara normal (tanpa break)")
```

Output:
```
1 2 3 4 5
Loop selesai secara normal (tanpa break)
```

---

## 4.5 Loop Trace Table (Tabel Pelacakan)

### 4.5.1 Apa Itu Trace Table?

**Trace table** (tabel pelacakan) adalah metode untuk menelusuri eksekusi loop **langkah demi langkah** secara manual. Ini sangat berguna untuk:

- **Memahami** bagaimana loop bekerja
- **Men-debug** kode yang tidak menghasilkan output yang diharapkan
- **Memprediksi** output dari suatu loop tanpa menjalankan kode

Cara membuat trace table:
1. Buat kolom untuk setiap variabel yang berubah
2. Buat baris untuk setiap iterasi
3. Isi nilai variabel di setiap langkah

### 4.5.2 Contoh Trace Table

**Contoh 1: Akumulasi sederhana**

```python
total = 0
for i in range(1, 6):
    total += i
print(total)
```

| Langkah | `i` | `total` (sebelum) | `total += i` | `total` (sesudah) |
|---------|-----|-------------------|--------------|-------------------|
| 1 | 1 | 0 | 0 + 1 | 1 |
| 2 | 2 | 1 | 1 + 2 | 3 |
| 3 | 3 | 3 | 3 + 3 | 6 |
| 4 | 4 | 6 | 6 + 4 | 10 |
| 5 | 5 | 10 | 10 + 5 | 15 |

**Output: `15`**

**Contoh 2: Perkalian bertahap (faktorial)**

```python
hasil = 1
n = 5
for i in range(1, n + 1):
    hasil *= i
print(f"{n}! = {hasil}")
```

| Langkah | `i` | `hasil` (sebelum) | `hasil *= i` | `hasil` (sesudah) |
|---------|-----|-------------------|--------------|-------------------|
| 1 | 1 | 1 | 1 * 1 | 1 |
| 2 | 2 | 1 | 1 * 2 | 2 |
| 3 | 3 | 2 | 2 * 3 | 6 |
| 4 | 4 | 6 | 6 * 4 | 24 |
| 5 | 5 | 24 | 24 * 5 | 120 |

**Output: `5! = 120`**

**Contoh 3: While loop dengan kondisi kompleks**

```python
x = 100
count = 0
while x > 1:
    x = x // 2
    count += 1
print(f"count = {count}")
```

| Langkah | `x` (sebelum) | `x > 1`? | `x = x // 2` | `count` |
|---------|---------------|----------|---------------|---------|
| 1 | 100 | True | 50 | 1 |
| 2 | 50 | True | 25 | 2 |
| 3 | 25 | True | 12 | 3 |
| 4 | 12 | True | 6 | 4 |
| 5 | 6 | True | 3 | 5 |
| 6 | 3 | True | 1 | 6 |
| 7 | 1 | False | *(tidak dieksekusi)* | — |

**Output: `count = 6`**

> **Tips:** Trace table sangat berguna saat ujian! Banyak soal ujian meminta mahasiswa menelusuri output dari suatu loop. Latih diri Anda membuat trace table secara rutin.

---

## 4.6 Nested Loops (Loop Bersarang)

### 4.6.1 Konsep

**Nested loop** adalah loop di dalam loop. Setiap kali outer loop (loop luar) menjalankan satu iterasi, inner loop (loop dalam) menjalankan **semua** iterasinya.

Jika outer loop beriterasi **m** kali dan inner loop beriterasi **n** kali, total eksekusi blok kode terdalam adalah **m x n** kali.

```python
# Konsep dasar nested loop
for baris in range(3):       # Outer loop — mengontrol baris
    for kolom in range(4):   # Inner loop — mengontrol kolom
        print(f"({baris},{kolom})", end=" ")
    print()  # Pindah baris setelah inner loop selesai
```

Output:
```
(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
```

### 4.6.2 Pattern Printing — Pola-Pola

Salah satu latihan terbaik untuk memahami nested loop adalah membuat pola-pola (pattern). Berikut beberapa pola populer beserta kodenya.

**Pola 1: Rectangle (Persegi Panjang)**

```
*****
*****
*****
```

```python
baris = 3
kolom = 5

for i in range(baris):
    for j in range(kolom):
        print("*", end="")
    print()
```

Penjelasan: Outer loop mengulang 3 kali (3 baris). Setiap iterasi outer loop, inner loop mencetak 5 bintang. Setelah inner loop selesai, `print()` memindahkan kursor ke baris baru.

**Pola 2: Right Triangle (Segitiga Siku-siku)**

```
*
**
***
****
*****
```

```python
tinggi = 5

for i in range(1, tinggi + 1):
    for j in range(i):
        print("*", end="")
    print()
```

Penjelasan: Pada baris ke-`i`, inner loop mencetak `i` bintang. Baris 1 = 1 bintang, baris 2 = 2 bintang, dst.

**Pola 3: Inverted Triangle (Segitiga Terbalik)**

```
*****
****
***
**
*
```

```python
tinggi = 5

for i in range(tinggi, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
```

Penjelasan: Dimulai dari `tinggi` bintang, berkurang 1 setiap baris.

**Pola 4: Pyramid (Piramida)**

```
    *
   ***
  *****
 *******
*********
```

```python
tinggi = 5

for i in range(1, tinggi + 1):
    # Cetak spasi di kiri
    for j in range(tinggi - i):
        print(" ", end="")
    # Cetak bintang
    for j in range(2 * i - 1):
        print("*", end="")
    print()
```

Penjelasan:
- Baris ke-`i` memiliki `(tinggi - i)` spasi di kiri dan `(2*i - 1)` bintang
- Baris 1: 4 spasi + 1 bintang
- Baris 2: 3 spasi + 3 bintang
- Baris 3: 2 spasi + 5 bintang
- Baris 4: 1 spasi + 7 bintang
- Baris 5: 0 spasi + 9 bintang

**Pola 5: Diamond (Berlian)**

```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

```python
tinggi = 5

# Bagian atas (termasuk baris tengah)
for i in range(1, tinggi + 1):
    print(" " * (tinggi - i) + "*" * (2 * i - 1))

# Bagian bawah
for i in range(tinggi - 1, 0, -1):
    print(" " * (tinggi - i) + "*" * (2 * i - 1))
```

Penjelasan: Diamond adalah kombinasi piramida (atas) dan piramida terbalik (bawah). Baris tengah hanya dicetak sekali.

**Pola 6: Number Triangle (Segitiga Angka)**

```
1
12
123
1234
12345
```

```python
tinggi = 5

for i in range(1, tinggi + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

Penjelasan: Pada baris ke-`i`, cetak angka dari 1 sampai `i`.

**Pola 7: Segitiga Angka Terbalik**

```
12345
1234
123
12
1
```

```python
tinggi = 5

for i in range(tinggi, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

### 4.6.3 Tabel Perkalian

Salah satu contoh klasik nested loop adalah mencetak tabel perkalian:

```python
# Tabel perkalian 1-10
# Cetak header
print("    ", end="")
for j in range(1, 11):
    print(f"{j:4d}", end="")
print()
print("-" * 44)

# Cetak isi tabel
for i in range(1, 11):
    print(f"{i:2d} |", end="")
    for j in range(1, 11):
        print(f"{i*j:4d}", end="")
    print()
```

Output:
```
       1   2   3   4   5   6   7   8   9  10
--------------------------------------------
 1 |   1   2   3   4   5   6   7   8   9  10
 2 |   2   4   6   8  10  12  14  16  18  20
 3 |   3   6   9  12  15  18  21  24  27  30
 4 |   4   8  12  16  20  24  28  32  36  40
 5 |   5  10  15  20  25  30  35  40  45  50
 6 |   6  12  18  24  30  36  42  48  54  60
 7 |   7  14  21  28  35  42  49  56  63  70
 8 |   8  16  24  32  40  48  56  64  72  80
 9 |   9  18  27  36  45  54  63  72  81  90
10 |  10  20  30  40  50  60  70  80  90 100
```

---

## 4.7 Pola-pola Umum Perulangan (Common Loop Patterns)

Dalam pemrograman, ada beberapa **pola perulangan** yang sangat sering digunakan. Memahami pola-pola ini akan membantu Anda menyelesaikan berbagai jenis masalah.

### 4.7.1 Counter Pattern (Pola Penghitung)

Menghitung berapa kali suatu kejadian terjadi.

```python
# Hitung berapa mahasiswa yang lulus (nilai >= 60)
nilai_uas = [85, 45, 90, 55, 78, 32, 92, 68, 40, 88]

lulus = 0
tidak_lulus = 0

for nilai in nilai_uas:
    if nilai >= 60:
        lulus += 1
    else:
        tidak_lulus += 1

print(f"Jumlah lulus      : {lulus} mahasiswa")
print(f"Jumlah tidak lulus: {tidak_lulus} mahasiswa")
print(f"Persentase lulus  : {lulus / len(nilai_uas) * 100:.1f}%")
```

Output:
```
Jumlah lulus      : 6 mahasiswa
Jumlah tidak lulus: 4 mahasiswa
Persentase lulus  : 60.0%
```

### 4.7.2 Accumulator Pattern (Pola Akumulator)

Mengumpulkan (menjumlahkan, mengalikan, atau menggabungkan) nilai selama iterasi.

```python
# Hitung total pendapatan warung per hari
penjualan = [
    ("Nasi Goreng", 5, 15000),   # (menu, jumlah, harga satuan)
    ("Mie Ayam", 8, 12000),
    ("Es Teh", 15, 5000),
    ("Soto Betawi", 3, 20000),
    ("Gado-gado", 4, 13000),
]

total_pendapatan = 0
total_porsi = 0

print("=== LAPORAN PENJUALAN HARIAN ===")
print(f"{'Menu':<15} {'Qty':>4} {'Harga':>10} {'Subtotal':>12}")
print("-" * 45)

for menu, qty, harga in penjualan:
    subtotal = qty * harga
    total_pendapatan += subtotal
    total_porsi += qty
    print(f"{menu:<15} {qty:>4} {harga:>10,} {subtotal:>12,}")

print("-" * 45)
print(f"{'TOTAL':<15} {total_porsi:>4} {'':>10} {total_pendapatan:>12,}")
```

### 4.7.3 Sentinel Value Pattern (Pola Nilai Pembatas)

Loop berjalan sampai menemukan nilai khusus (sentinel) yang menandakan akhir input.

```python
# Input nilai mahasiswa sampai user memasukkan -1
print("Masukkan nilai mahasiswa (ketik -1 untuk selesai):")

daftar_nilai = []

while True:
    nilai = int(input("Nilai: "))
    if nilai == -1:  # Sentinel value
        break
    if 0 <= nilai <= 100:
        daftar_nilai.append(nilai)
    else:
        print("Nilai harus 0-100!")

if daftar_nilai:
    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    print(f"\nJumlah data  : {len(daftar_nilai)}")
    print(f"Rata-rata    : {rata_rata:.2f}")
    print(f"Nilai maks   : {max(daftar_nilai)}")
    print(f"Nilai min    : {min(daftar_nilai)}")
else:
    print("Tidak ada data yang dimasukkan.")
```

### 4.7.4 Flag Pattern (Pola Bendera)

Menggunakan variabel boolean sebagai "bendera" untuk mengontrol alur program.

```python
# Cek apakah suatu bilangan adalah bilangan sempurna
# (bilangan yang sama dengan jumlah faktor-faktornya selain dirinya sendiri)
# Contoh: 6 = 1 + 2 + 3

bilangan = 28
jumlah_faktor = 0
is_sempurna = False  # Flag

for i in range(1, bilangan):
    if bilangan % i == 0:
        jumlah_faktor += i

if jumlah_faktor == bilangan:
    is_sempurna = True

if is_sempurna:
    print(f"{bilangan} adalah bilangan sempurna")
    # Tampilkan faktor-faktornya
    faktor = []
    for i in range(1, bilangan):
        if bilangan % i == 0:
            faktor.append(str(i))
    print(f"Faktor: {' + '.join(faktor)} = {bilangan}")
else:
    print(f"{bilangan} bukan bilangan sempurna")
```

Output:
```
28 adalah bilangan sempurna
Faktor: 1 + 2 + 4 + 7 + 14 = 28
```

### 4.7.5 Min/Max Pattern (Pola Minimum/Maksimum)

Mencari nilai terkecil atau terbesar dalam sebuah kumpulan data.

```python
# Cari suhu tertinggi dan terendah selama seminggu
suhu_harian = [31.5, 33.2, 29.8, 34.1, 32.0, 30.5, 28.7]
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

suhu_max = suhu_harian[0]
suhu_min = suhu_harian[0]
hari_max = hari[0]
hari_min = hari[0]

for i in range(1, len(suhu_harian)):
    if suhu_harian[i] > suhu_max:
        suhu_max = suhu_harian[i]
        hari_max = hari[i]
    if suhu_harian[i] < suhu_min:
        suhu_min = suhu_harian[i]
        hari_min = hari[i]

print("=== LAPORAN SUHU MINGGUAN ===")
for i in range(len(hari)):
    print(f"  {hari[i]:<8}: {suhu_harian[i]}°C")
print(f"\nSuhu tertinggi: {suhu_max}°C (hari {hari_max})")
print(f"Suhu terendah : {suhu_min}°C (hari {hari_min})")
print(f"Rata-rata     : {sum(suhu_harian)/len(suhu_harian):.1f}°C")
```

Output:
```
=== LAPORAN SUHU MINGGUAN ===
  Senin   : 31.5°C
  Selasa  : 33.2°C
  Rabu    : 29.8°C
  Kamis   : 34.1°C
  Jumat   : 32.0°C
  Sabtu   : 30.5°C
  Minggu  : 28.7°C

Suhu tertinggi: 34.1°C (hari Kamis)
Suhu terendah : 28.7°C (hari Minggu)
Rata-rata     : 31.4°C
```

---

## 4.8 Perbandingan `for` vs `while`

Kapan menggunakan `for` dan kapan menggunakan `while`? Berikut panduan pengambilan keputusan:

| Situasi | Gunakan | Alasan |
|---------|---------|--------|
| Iterasi dengan jumlah pasti | `for` | `range()` membatasi jumlah iterasi |
| Iterasi sampai kondisi terpenuhi | `while` | Fleksibel, berhenti sesuai kondisi |
| Iterasi atas koleksi (list, string, dll.) | `for` | Lebih *Pythonic* dan mudah dibaca |
| Input validation | `while True` + `break` | Belum tahu berapa kali user salah input |
| Game loop | `while` | Berjalan sampai menang/kalah |
| Membaca file baris per baris | `for` | File adalah iterable |
| Menu program interaktif | `while` | Terus berjalan sampai user memilih keluar |
| Mengolah setiap elemen array/list | `for` | Langsung iterasi tanpa index manual |

**Aturan praktis:** Jika Anda **tahu** berapa kali loop harus berjalan, gunakan `for`. Jika Anda **tidak tahu**, gunakan `while`.

**Contoh konversi antara keduanya:**

```python
# Menggunakan for
for i in range(5):
    print(i)

# Ekuivalen menggunakan while
i = 0
while i < 5:
    print(i)
    i += 1
```

Keduanya menghasilkan output yang sama, tetapi versi `for` lebih ringkas dan lebih *Pythonic*.

---

## 4.9 Studi Kasus Lengkap: Sistem Kasir Minimarket

Berikut adalah program lengkap yang menggabungkan berbagai konsep perulangan yang telah dipelajari.

```python
# =============================================
# SISTEM KASIR MINIMARKET SEDERHANA
# Studi Kasus Bab 4 - Perulangan
# =============================================

# Daftar produk dan harga
katalog = {
    "A01": {"nama": "Indomie Goreng", "harga": 3500},
    "A02": {"nama": "Teh Botol Sosro 450ml", "harga": 5000},
    "A03": {"nama": "Roti Tawar Sari Roti", "harga": 15000},
    "A04": {"nama": "Beras 5kg Premium", "harga": 65000},
    "A05": {"nama": "Minyak Goreng 1L", "harga": 18000},
    "A06": {"nama": "Gula Pasir 1kg", "harga": 14000},
    "A07": {"nama": "Kopi Kapal Api 165g", "harga": 9500},
    "A08": {"nama": "Sabun Mandi Lifebuoy", "harga": 3500},
    "A09": {"nama": "Susu Ultra 1L", "harga": 17000},
    "A10": {"nama": "Telur 1kg", "harga": 28000},
}

# Daftar belanjaan
keranjang = []
total_belanja = 0

print("=" * 50)
print("    MINIMARKET AL AZHAR MART")
print("    Sistem Kasir v1.0")
print("=" * 50)

# Tampilkan katalog produk
print("\n--- DAFTAR PRODUK ---")
print(f"{'Kode':<6} {'Nama Produk':<25} {'Harga':>10}")
print("-" * 43)
for kode, info in katalog.items():
    print(f"{kode:<6} {info['nama']:<25} Rp {info['harga']:>7,}")

print("-" * 43)
print()

# Loop utama: input belanjaan
while True:
    kode_input = input("Masukkan kode produk (atau 'selesai'): ").strip().upper()

    if kode_input == "SELESAI":
        break

    if kode_input not in katalog:
        print("Kode produk tidak ditemukan! Coba lagi.\n")
        continue

    # Input jumlah
    while True:
        try:
            jumlah = int(input(f"Jumlah {katalog[kode_input]['nama']}: "))
            if jumlah > 0:
                break
            print("Jumlah harus lebih dari 0!")
        except ValueError:
            print("Input harus berupa angka!")

    # Tambahkan ke keranjang
    subtotal = katalog[kode_input]["harga"] * jumlah
    keranjang.append({
        "nama": katalog[kode_input]["nama"],
        "harga": katalog[kode_input]["harga"],
        "jumlah": jumlah,
        "subtotal": subtotal
    })
    total_belanja += subtotal
    print(f"  >> {katalog[kode_input]['nama']} x{jumlah} = Rp {subtotal:,}")
    print()

# Cek apakah ada belanjaan
if not keranjang:
    print("Tidak ada barang yang dibeli. Terima kasih!")
else:
    # Hitung diskon
    diskon = 0
    if total_belanja >= 200000:
        diskon = 0.10  # Diskon 10% untuk belanja >= 200rb
        pesan_diskon = "Diskon 10% (belanja >= Rp 200,000)"
    elif total_belanja >= 100000:
        diskon = 0.05  # Diskon 5% untuk belanja >= 100rb
        pesan_diskon = "Diskon 5% (belanja >= Rp 100,000)"

    nilai_diskon = int(total_belanja * diskon)
    total_bayar = total_belanja - nilai_diskon

    # Cetak struk
    print()
    print("=" * 50)
    print("           STRUK PEMBAYARAN")
    print("       MINIMARKET AL AZHAR MART")
    print("=" * 50)
    print(f"{'No':<3} {'Item':<22} {'Qty':>3} {'Subtotal':>12}")
    print("-" * 50)

    for i, item in enumerate(keranjang, 1):
        print(f"{i:<3} {item['nama']:<22} {item['jumlah']:>3} Rp {item['subtotal']:>8,}")

    print("-" * 50)
    print(f"{'Subtotal':>30} Rp {total_belanja:>8,}")

    if diskon > 0:
        print(f"{'':>30} {pesan_diskon}")
        print(f"{'Diskon':>30} Rp {nilai_diskon:>8,}")

    print(f"{'TOTAL BAYAR':>30} Rp {total_bayar:>8,}")
    print("=" * 50)

    # Input pembayaran
    while True:
        try:
            bayar = int(input(f"\nJumlah bayar: Rp "))
            if bayar >= total_bayar:
                break
            print(f"Uang kurang! Minimal Rp {total_bayar:,}")
        except ValueError:
            print("Input harus berupa angka!")

    kembalian = bayar - total_bayar
    print(f"Kembalian   : Rp {kembalian:,}")
    print()
    print("Terima kasih telah berbelanja!")
    print("Selamat datang kembali.")
    print("=" * 50)
```

**Konsep yang digunakan dalam studi kasus ini:**
1. **`while True` + `break`** — loop utama untuk input belanjaan
2. **`continue`** — skip jika kode produk tidak valid
3. **Nested `while` loop** — validasi input jumlah dan pembayaran
4. **`for` loop dengan `enumerate()`** — mencetak struk
5. **Counter pattern** — menghitung total
6. **Accumulator pattern** — akumulasi total belanja
7. **Sentinel value** — kata "selesai" sebagai penanda akhir input

---

## 4.10 Common Mistakes (Kesalahan Umum)

### Kesalahan 1: Off-by-one Error

`range()` berhenti **SEBELUM** nilai `stop`. Ini sering menyebabkan kesalahan.

```python
# SALAH: ingin cetak 1-10, tapi hanya cetak 1-9
for i in range(1, 10):
    print(i, end=" ")
# Output: 1 2 3 4 5 6 7 8 9  (10 tidak tercetak!)
```

```python
# BENAR: gunakan range(1, 11) untuk mendapatkan 1-10
for i in range(1, 11):
    print(i, end=" ")
# Output: 1 2 3 4 5 6 7 8 9 10
```

### Kesalahan 2: Infinite Loop (Lupa Update Variabel)

```python
# SALAH: variabel 'i' tidak pernah di-update
i = 0
while i < 5:
    print(i)
    # Seharusnya ada: i += 1
# Program tidak pernah berhenti!
```

```python
# BENAR: selalu update variabel kontrol
i = 0
while i < 5:
    print(i)
    i += 1  # PENTING: update variabel
```

### Kesalahan 3: Memodifikasi List Saat Iterasi

```python
# SALAH: menghapus elemen list saat sedang di-iterasi
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for a in angka:
    if a % 2 == 0:
        angka.remove(a)  # BAHAYA! Mengubah list saat iterasi
print(angka)
# Output: [1, 3, 5, 7, 9]? SALAH! Hasilnya mungkin: [1, 3, 5, 7, 9] atau tidak terduga
```

```python
# BENAR: buat list baru dengan list comprehension
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
angka_ganjil = [a for a in angka if a % 2 != 0]
print(angka_ganjil)
# Output: [1, 3, 5, 7, 9]

# BENAR alternatif: iterasi atas copy dari list
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for a in angka[:]:  # angka[:] membuat copy
    if a % 2 == 0:
        angka.remove(a)
print(angka)
# Output: [1, 3, 5, 7, 9]
```

### Kesalahan 4: Menggunakan Tipe Loop yang Salah

```python
# KURANG TEPAT: menggunakan while untuk iterasi list
buah = ["Mangga", "Jeruk", "Apel"]
i = 0
while i < len(buah):
    print(buah[i])
    i += 1
```

```python
# LEBIH BAIK: gunakan for loop (lebih Pythonic)
buah = ["Mangga", "Jeruk", "Apel"]
for b in buah:
    print(b)
```

### Kesalahan 5: Indentation Error pada Nested Loops

```python
# SALAH: print() di tempat yang salah
for i in range(3):
    for j in range(3):
        print("*", end="")
        print()  # SALAH! Ini di dalam inner loop
# Output yang tidak diharapkan — setiap bintang di baris baru
```

```python
# BENAR: print() harus di luar inner loop, di dalam outer loop
for i in range(3):
    for j in range(3):
        print("*", end="")
    print()  # BENAR! Pindah baris setelah inner loop selesai
# Output:
# ***
# ***
# ***
```

---

## AI Corner: AI untuk Memahami Loop Patterns

**Level: Dasar**

AI (seperti ChatGPT, Gemini, atau Claude) dapat menjadi alat bantu yang sangat berguna untuk memahami konsep perulangan. Berikut beberapa cara memanfaatkannya:

### Gunakan AI untuk Trace Loop

Anda bisa meminta AI menelusuri eksekusi loop langkah demi langkah:

> **Contoh prompt:**
> "Trace this nested loop step by step and show the output at each iteration:"
> ```python
> for i in range(3):
>     for j in range(i + 1):
>         print("*", end="")
>     print()
> ```

AI akan memberikan penjelasan langkah demi langkah, membantu Anda memahami bagaimana nested loop bekerja.

### Gunakan AI untuk Generate Pattern

Anda bisa meminta AI membuat pola tertentu:

> **Contoh prompt:**
> "Buatkan kode Python untuk mencetak pola huruf 'A' menggunakan bintang (*) dengan tinggi 7 baris."

### Gunakan AI untuk Debug Loop

Jika loop Anda tidak menghasilkan output yang diharapkan:

> **Contoh prompt:**
> "Kode saya seharusnya mencetak bilangan prima 1-50, tapi outputnya salah. Bantu saya debug: [paste kode]"

### Penting: Verifikasi Sendiri!

AI tidak selalu memberikan jawaban yang benar. **Selalu verifikasi** output AI dengan:

1. **Jalankan kode** di Google Colab atau Python IDE
2. **Buat trace table** sendiri untuk memverifikasi logika
3. **Ubah input** dan cek apakah kode masih bekerja dengan benar
4. **Pahami** kode yang diberikan AI, jangan hanya copy-paste

> **Ingat:** Tujuan kuliah ini bukan menghasilkan kode yang benar, tetapi **memahami** bagaimana dan mengapa kode bekerja. AI adalah alat bantu, bukan pengganti proses belajar Anda.

---

## Latihan Soal

### Tingkat Dasar

**Soal 1: Bilangan Kelipatan 3**

Buatlah program yang mencetak semua bilangan dari 1 sampai 100 yang habis dibagi 3.

Contoh output (sebagian):
```
3 6 9 12 15 18 21 ... 96 99
```

**Soal 2: Faktorial**

Buatlah program yang menghitung faktorial dari bilangan `n` yang diinput user. Faktorial `n!` = 1 x 2 x 3 x ... x n.

Contoh:
```
Masukkan n: 5
5! = 1 x 2 x 3 x 4 x 5 = 120
```

**Soal 3: Segitiga Bintang**

Buatlah program yang mencetak pola segitiga siku-siku (right triangle) dengan tinggi `n` yang diinput user.

Contoh (n=5):
```
*
**
***
****
*****
```

**Soal 4: Jumlah Digit**

Buatlah program yang menghitung jumlah digit dari suatu bilangan yang diinput user (tanpa menggunakan `str()` atau `len()`). Gunakan `while` loop dengan operasi `// 10`.

Contoh:
```
Masukkan bilangan: 123456
Jumlah digit: 6
Total digit : 21
```

**Soal 5: FizzBuzz**

Buatlah program FizzBuzz klasik untuk bilangan 1 sampai 100:
- Jika habis dibagi 3 DAN 5: cetak "FizzBuzz"
- Jika habis dibagi 3 saja: cetak "Fizz"
- Jika habis dibagi 5 saja: cetak "Buzz"
- Selain itu: cetak bilangannya

Contoh output (sebagian):
```
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 ...
```

### Tingkat Menengah

**Soal 1: Deret Fibonacci**

Buatlah program yang mencetak deret Fibonacci sampai `n` suku. Deret Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Contoh:
```
Masukkan jumlah suku: 10
Deret Fibonacci: 0 1 1 2 3 5 8 13 21 34
```

**Soal 2: Cek Bilangan Prima**

Buatlah program yang memeriksa apakah suatu bilangan adalah bilangan prima. Tampilkan juga semua bilangan prima dari 2 sampai bilangan tersebut.

Contoh:
```
Masukkan bilangan: 30
Bilangan prima dari 2-30:
2 3 5 7 11 13 17 19 23 29
Jumlah bilangan prima: 10
```

**Soal 3: Pola Diamond**

Buatlah program yang mencetak pola diamond (berlian) dengan tinggi `n` yang diinput user (n harus ganjil).

Contoh (n=7):
```
   *
  ***
 *****
*******
 *****
  ***
   *
```

**Soal 4: ATM Sederhana**

Buatlah program simulasi ATM sederhana menggunakan `while` loop dengan menu:
1. Cek Saldo
2. Tarik Tunai
3. Setor Tunai
4. Keluar

Saldo awal: Rp 1.000.000. Validasi input dan saldo.

**Soal 5: Aproksimasi Pi (Deret Leibniz)**

Hitung nilai pendekatan pi menggunakan deret Leibniz:

pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...

Buatlah program yang menghitung aproksimasi pi menggunakan `n` suku (input dari user) dan bandingkan dengan `math.pi`.

Contoh:
```
Masukkan jumlah suku: 1000000
Aproksimasi pi : 3.14159165...
math.pi        : 3.14159265...
Selisih        : 0.00000100...
```

### Tingkat Mahir

**Soal 1: Segitiga Pascal**

Buatlah program yang mencetak Segitiga Pascal sebanyak 7 baris dengan format rata tengah.

Contoh output:
```
            1
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1
  1   5  10  10   5   1
1   6  15  20  15   6   1
```

**Soal 2: Collatz Conjecture**

Buatlah program yang mengimplementasikan Collatz Conjecture:
- Input bilangan `n`
- Jika `n` genap: `n = n / 2`
- Jika `n` ganjil: `n = 3*n + 1`
- Ulangi sampai `n = 1`
- Hitung dan tampilkan jumlah langkah serta semua nilai yang dilalui

Contoh:
```
Masukkan n: 27
27 -> 82 -> 41 -> 124 -> 62 -> 31 -> ... -> 4 -> 2 -> 1
Jumlah langkah: 111
Nilai maksimum yang dicapai: 9232
```

**Soal 3: Tantangan ASCII Art "UAI"**

Buatlah program yang mencetak tulisan "UAI" dalam bentuk ASCII art menggunakan nested loops dan conditional. Setiap huruf memiliki tinggi 7 baris.

Contoh output:
```
U   U     A     IIIII
U   U    A A      I
U   U   A   A     I
U   U  AAAAA A    I
U   U  A     A    I
U   U  A     A    I
 UUU   A     A  IIIII
```

Petunjuk: Gunakan nested loop. Outer loop untuk baris, inner loop untuk kolom. Gunakan kondisi untuk menentukan apakah posisi tertentu harus berisi karakter atau spasi.

---

## Rangkuman

Berikut ringkasan materi yang telah dipelajari dalam bab ini:

1. **Perulangan (loop)** adalah struktur kontrol yang memungkinkan eksekusi blok kode secara berulang, menerapkan prinsip DRY (Don't Repeat Yourself).

2. **`for` loop** digunakan ketika jumlah iterasi diketahui atau saat mengiterasi elemen dalam sequence (list, string, tuple, dictionary).

3. **Fungsi `range()`** menghasilkan deretan angka dan memiliki tiga bentuk: `range(stop)`, `range(start, stop)`, dan `range(start, stop, step)`. Ingat bahwa `range()` berhenti **sebelum** nilai `stop`.

4. **`while` loop** digunakan ketika perulangan bergantung pada kondisi tertentu dan jumlah iterasi belum diketahui.

5. **Infinite loop** terjadi ketika kondisi `while` tidak pernah menjadi `False`. Pencegahan utama: selalu pastikan ada mekanisme update pada variabel kondisi atau gunakan `break`.

6. **`break`** menghentikan loop secara langsung, **`continue`** melewati sisa iterasi saat ini dan langsung ke iterasi berikutnya.

7. **`else` pada loop** adalah fitur unik Python: blok `else` dijalankan hanya jika loop selesai tanpa `break`.

8. **Trace table** (tabel pelacakan) adalah metode manual untuk menelusuri eksekusi loop langkah demi langkah, sangat berguna untuk debugging dan memahami alur program.

9. **Nested loop** (loop bersarang) digunakan untuk masalah dua dimensi seperti tabel dan pola. Jika outer loop beriterasi m kali dan inner loop n kali, total eksekusi terdalam = m x n.

10. **Lima pola umum perulangan**: Counter (penghitung), Accumulator (akumulator), Sentinel Value (nilai pembatas), Flag (bendera), dan Min/Max (minimum/maksimum).

11. **Pemilihan `for` vs `while`**: Gunakan `for` jika jumlah iterasi diketahui atau iterasi atas koleksi. Gunakan `while` jika iterasi bergantung kondisi yang belum pasti.

12. **Kesalahan umum** yang harus dihindari: off-by-one error pada `range()`, infinite loop karena lupa update variabel, memodifikasi list saat iterasi, salah penempatan indentasi pada nested loop.

---

## Referensi

1. Downey, A. B. (2015). *Think Python: How to Think Like a Computer Scientist* (2nd ed.). O'Reilly Media. Tersedia gratis di [https://greenteapress.com/wp/think-python-2e/](https://greenteapress.com/wp/think-python-2e/)

2. Lutz, M. (2013). *Learning Python* (5th ed.). O'Reilly Media.

3. Matthes, E. (2019). *Python Crash Course: A Hands-On, Project-Based Introduction to Programming* (2nd ed.). No Starch Press.

4. Severance, C. R. (2016). *Python for Everybody: Exploring Data in Python 3*. Tersedia gratis di [https://www.py4e.com/book](https://www.py4e.com/book)

5. Sweigart, A. (2019). *Automate the Boring Stuff with Python* (2nd ed.). No Starch Press. Tersedia gratis di [https://automatetheboringstuff.com/](https://automatetheboringstuff.com/)

6. Python Software Foundation. (2024). *The Python Tutorial — More Control Flow Tools*. [https://docs.python.org/3/tutorial/controlflow.html](https://docs.python.org/3/tutorial/controlflow.html)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
