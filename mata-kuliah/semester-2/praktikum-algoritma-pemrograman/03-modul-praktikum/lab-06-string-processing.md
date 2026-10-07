# Lab 06: String Processing

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Durasi** | 75 menit |
| **Prasyarat** | Lab 05 — Functions dan Decomposition |

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:
- Melakukan indexing, slicing, dan iterasi pada string
- Menggunakan method string bawaan Python untuk manipulasi teks
- Menerapkan f-string formatting untuk output yang rapi
- Membangun program pengolahan teks: Word Counter, Caesar Cipher, dan Palindrome Checker

---

## Persiapan

1. Buka Google Colab dan buat notebook baru
2. Beri nama `Lab06_NamaAnda_NIM.ipynb`
3. Pastikan Anda telah memahami fungsi dan loop

---

## Langkah-langkah

### Langkah 1 — Indexing dan Slicing String

```python
# String indexing
kota = "Universitas Al Azhar Indonesia"

print(f"String : '{kota}'")
print(f"Panjang: {len(kota)} karakter")
print()

# Indexing (dimulai dari 0)
print(f"Karakter pertama   : kota[0]  = '{kota[0]}'")
print(f"Karakter kelima    : kota[4]  = '{kota[4]}'")
print(f"Karakter terakhir  : kota[-1] = '{kota[-1]}'")
print(f"Karakter ke-2 dari akhir: kota[-2] = '{kota[-2]}'")

# Slicing [start:stop:step]
print(f"\nSlicing:")
print(f"kota[0:11]   = '{kota[0:11]}'")       # Universitas
print(f"kota[12:20]  = '{kota[12:20]}'")       # Al Azhar
print(f"kota[21:]    = '{kota[21:]}'")          # Indonesia
print(f"kota[::-1]   = '{kota[::-1]}'")         # terbalik
print(f"kota[::2]    = '{kota[::2]}'")          # setiap 2 karakter
```

### Langkah 2 — Method String Umum

```python
# Method string bawaan Python
teks = "  Selamat Datang di Prodi Informatika UAI  "

print(f"Original     : '{teks}'")
print(f"upper()      : '{teks.upper()}'")
print(f"lower()      : '{teks.lower()}'")
print(f"strip()      : '{teks.strip()}'")
print(f"lstrip()     : '{teks.lstrip()}'")
print(f"rstrip()     : '{teks.rstrip()}'")
print(f"title()      : '{teks.strip().title()}'")
print(f"capitalize() : '{teks.strip().capitalize()}'")
print(f"swapcase()   : '{teks.strip().swapcase()}'")

# Find dan count
kalimat = "Belajar Python itu menyenangkan. Python mudah dipelajari."
print(f"\nKalimat: '{kalimat}'")
print(f"find('Python')   : posisi {kalimat.find('Python')}")
print(f"rfind('Python')  : posisi {kalimat.rfind('Python')}")
print(f"count('Python')  : {kalimat.count('Python')} kali")
print(f"count('a')       : {kalimat.count('a')} kali")

# Replace
baru = kalimat.replace("Python", "pemrograman")
print(f"replace()        : '{baru}'")
```

### Langkah 3 — Split dan Join

```python
# Split: memecah string menjadi list
data_csv = "Ahmad,Informatika,2025,3.85"
kolom = data_csv.split(",")
print(f"Data CSV  : '{data_csv}'")
print(f"split(',') : {kolom}")
print(f"Nama      : {kolom[0]}")
print(f"Prodi     : {kolom[1]}")

# Split kalimat menjadi kata-kata
kalimat = "Algoritma dan Pemrograman adalah mata kuliah wajib"
kata_kata = kalimat.split()
print(f"\nKalimat   : '{kalimat}'")
print(f"split()    : {kata_kata}")
print(f"Jumlah kata: {len(kata_kata)}")

# Join: menggabungkan list menjadi string
buah = ["mangga", "jeruk", "apel", "durian", "rambutan"]
gabung_koma = ", ".join(buah)
gabung_strip = " - ".join(buah)
print(f"\nList buah   : {buah}")
print(f"join(', ')  : '{gabung_koma}'")
print(f"join(' - ') : '{gabung_strip}'")
```

### Langkah 4 — Pengecekan String

```python
# Method untuk memeriksa isi string
contoh = [
    "12345",
    "abcde",
    "abc123",
    "Hello World",
    "   ",
    "HURUF BESAR",
    "huruf kecil",
]

print(f"{'String':<15} {'isdigit':>8} {'isalpha':>8} {'isalnum':>8} {'isspace':>8} {'isupper':>8} {'islower':>8}")
print("-" * 70)

for s in contoh:
    print(f"'{s}'".ljust(15), end="")
    print(f"{str(s.isdigit()):>8}", end="")
    print(f"{str(s.isalpha()):>8}", end="")
    print(f"{str(s.isalnum()):>8}", end="")
    print(f"{str(s.isspace()):>8}", end="")
    print(f"{str(s.isupper()):>8}", end="")
    print(f"{str(s.islower()):>8}")
```

### Langkah 5 — f-String Formatting Lanjutan

```python
# Format angka dan alignment
barang = [
    ("Buku Tulis", 5, 4500),
    ("Pensil 2B", 12, 2000),
    ("Penghapus", 3, 3500),
    ("Penggaris 30cm", 2, 8000),
    ("Tas Ransel", 1, 175000),
]

print("=" * 50)
print(f"{'NOTA BELANJA TOKO SINAR ILMU':^50}")
print("=" * 50)
print(f"{'Barang':<18} {'Qty':>4} {'Harga':>10} {'Subtotal':>12}")
print("-" * 50)

total = 0
for nama, qty, harga in barang:
    sub = qty * harga
    total += sub
    print(f"{nama:<18} {qty:>4} {harga:>10,} {sub:>12,}")

print("-" * 50)
print(f"{'TOTAL':<18} {'':>4} {'':>10} {total:>12,}")
print("=" * 50)
```

### Langkah 6 — File I/O (Baca dan Tulis File)

```python
# Menulis file teks
nama_file = "catatan_mahasiswa.txt"

with open(nama_file, "w") as f:
    f.write("=== CATATAN MAHASISWA ===\n")
    f.write("Nama     : Dewi Sartika\n")
    f.write("NIM      : 20250042\n")
    f.write("Prodi    : Informatika\n")
    f.write("Semester : 2\n")
    f.write("\nMata Kuliah:\n")
    f.write("1. Algoritma dan Pemrograman\n")
    f.write("2. Kalkulus II\n")
    f.write("3. Basis Data\n")

print(f"File '{nama_file}' berhasil ditulis!")

# Membaca file teks
print("\n--- Isi File ---")
with open(nama_file, "r") as f:
    isi = f.read()
    print(isi)

# Membaca baris per baris
print("--- Baris per Baris ---")
with open(nama_file, "r") as f:
    for nomor, baris in enumerate(f, 1):
        print(f"Baris {nomor:>2}: {baris.rstrip()}")
```

### Langkah 7 — Mini Project: Word Counter

```python
# =============================================
# MINI PROJECT 1: Word Counter
# =============================================

def hitung_statistik_teks(teks):
    """Menghitung berbagai statistik dari sebuah teks."""
    jumlah_karakter = len(teks)
    jumlah_karakter_tanpa_spasi = len(teks.replace(" ", ""))
    kata_kata = teks.split()
    jumlah_kata = len(kata_kata)
    kalimat = [s.strip() for s in teks.split(".") if s.strip()]
    jumlah_kalimat = len(kalimat)

    # Hitung frekuensi setiap kata
    frekuensi = {}
    for kata in kata_kata:
        kata_bersih = kata.lower().strip(".,!?;:'\"")
        if kata_bersih:
            frekuensi[kata_bersih] = frekuensi.get(kata_bersih, 0) + 1

    return {
        "karakter": jumlah_karakter,
        "karakter_tanpa_spasi": jumlah_karakter_tanpa_spasi,
        "kata": jumlah_kata,
        "kalimat": jumlah_kalimat,
        "frekuensi": frekuensi,
    }

# Teks contoh
teks_input = """Indonesia adalah negara kepulauan terbesar di dunia.
Indonesia memiliki lebih dari tujuh belas ribu pulau.
Ibukota Indonesia adalah Jakarta. Indonesia memiliki
keberagaman budaya yang sangat kaya dan indah."""

print("=" * 50)
print(f"{'WORD COUNTER':^50}")
print("=" * 50)
print(f"\nTeks:\n{teks_input}")

hasil = hitung_statistik_teks(teks_input)

print(f"\n--- Statistik ---")
print(f"Jumlah karakter           : {hasil['karakter']}")
print(f"Karakter (tanpa spasi)    : {hasil['karakter_tanpa_spasi']}")
print(f"Jumlah kata               : {hasil['kata']}")
print(f"Jumlah kalimat            : {hasil['kalimat']}")

print(f"\n--- Frekuensi Kata (Top 10) ---")
freq_sorted = sorted(hasil["frekuensi"].items(), key=lambda x: x[1], reverse=True)
for i, (kata, jumlah) in enumerate(freq_sorted[:10], 1):
    bar = "#" * jumlah
    print(f"  {i:>2}. {kata:<15} : {jumlah} {bar}")
```

### Langkah 8 — Mini Project: Caesar Cipher

```python
# =============================================
# MINI PROJECT 2: Caesar Cipher
# =============================================

def caesar_enkripsi(teks, kunci):
    """Mengenkripsi teks menggunakan Caesar Cipher."""
    hasil = ""
    for char in teks:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            hasil += chr((ord(char) - base + kunci) % 26 + base)
        else:
            hasil += char
    return hasil

def caesar_dekripsi(teks, kunci):
    """Mendekripsi teks yang dienkripsi dengan Caesar Cipher."""
    return caesar_enkripsi(teks, -kunci)

print("=" * 45)
print(f"{'CAESAR CIPHER':^45}")
print("=" * 45)

pesan = input("Masukkan pesan: ")
kunci = int(input("Masukkan kunci (1-25): "))

pesan_enkripsi = caesar_enkripsi(pesan, kunci)
pesan_dekripsi = caesar_dekripsi(pesan_enkripsi, kunci)

print(f"\nPesan asli     : {pesan}")
print(f"Kunci          : {kunci}")
print(f"Hasil enkripsi : {pesan_enkripsi}")
print(f"Hasil dekripsi : {pesan_dekripsi}")

# Brute force: coba semua kunci
print(f"\n--- Brute Force Dekripsi ---")
for k in range(1, 26):
    print(f"  Kunci {k:>2}: {caesar_dekripsi(pesan_enkripsi, k)}")
```

### Langkah 9 — Mini Project: Palindrome Checker

```python
# =============================================
# MINI PROJECT 3: Palindrome Checker
# =============================================

def cek_palindrome(teks):
    """Mengecek apakah suatu teks adalah palindrome."""
    bersih = ""
    for char in teks.lower():
        if char.isalnum():
            bersih += char
    return bersih == bersih[::-1], bersih

print("=" * 45)
print(f"{'PALINDROME CHECKER':^45}")
print("=" * 45)

daftar_uji = [
    "katak",
    "racecar",
    "Kasur rusak",
    "python",
    "Malam",
    "Taat",
    "Ibu Ratna antar ubi",
]

print(f"\n{'Teks':<25} {'Bersih':<20} {'Palindrome?':>12}")
print("-" * 60)

for teks in daftar_uji:
    hasil, bersih = cek_palindrome(teks)
    status = "YA" if hasil else "TIDAK"
    print(f"{teks:<25} {bersih:<20} {status:>12}")
```

---

## Tantangan Tambahan

1. **Validator Email**: Buat fungsi yang memvalidasi format email (harus ada `@`, domain valid, tidak ada spasi, dll.). Uji dengan berbagai contoh email valid dan tidak valid.

2. **Text Analyzer Lanjutan**: Buat program yang membaca sebuah teks lalu menampilkan: jumlah huruf vokal dan konsonan, kata terpanjang dan terpendek, serta rata-rata panjang kata.

3. **Pig Latin Translator**: Buat program yang menerjemahkan kalimat bahasa Inggris ke Pig Latin. Aturan: pindahkan konsonan awal ke akhir kata dan tambahkan "ay". Contoh: "hello" menjadi "ellohay".

---

## Checklist Penyelesaian

- [ ] Mampu melakukan indexing dan slicing pada string
- [ ] Menguasai method string: `upper`, `lower`, `split`, `join`, `replace`, `find`, `count`, `strip`
- [ ] Mampu menggunakan f-string untuk formatting output
- [ ] Mampu membaca dan menulis file teks
- [ ] Menyelesaikan Mini Project: Word Counter
- [ ] Menyelesaikan Mini Project: Caesar Cipher
- [ ] Menyelesaikan Mini Project: Palindrome Checker
- [ ] Mengerjakan minimal 1 tantangan tambahan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
