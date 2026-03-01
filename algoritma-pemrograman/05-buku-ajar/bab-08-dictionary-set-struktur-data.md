# BAB 8: DICTIONARY, SET, DAN PEMILIHAN STRUKTUR DATA

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| CPMK-5.5 | Memahami dictionary sebagai pemetaan key-value | C2 (Memahami) |
| CPMK-5.6 | Menerapkan operasi pada dictionary dan set | C3 (Menerapkan) |
| CPMK-5.7 | Menganalisis kapan menggunakan list vs tuple vs dict vs set | C4 (Menganalisis) |

**Estimasi Waktu:** 3 × 50 menit (3 SKS)

**Prasyarat:** Mahasiswa telah memahami materi Bab 1–7 (termasuk list dan tuple).

---

## 8.1 Dictionary: Pemetaan Key-Value

### 8.1.1 Apa Itu Dictionary?

**Dictionary** (dict) adalah struktur data yang menyimpan pasangan **key-value** (kunci-nilai). Analoginya:

- **Kamus bahasa**: kata (key) → definisi (value)
- **Buku telepon**: nama (key) → nomor (value)
- **KTP**: field (key) → isi (value)

```
┌──────────────────────────────────────────────────┐
│              DICTIONARY: KEY → VALUE              │
├──────────────────────────────────────────────────┤
│                                                  │
│  "nama"    ──────→  "Ahmad Fauzan"               │
│  "nim"     ──────→  "2025001"                    │
│  "prodi"   ──────→  "Informatika"                │
│  "ipk"     ──────→  3.75                         │
│  "aktif"   ──────→  True                         │
│                                                  │
└──────────────────────────────────────────────────┘
```

### 8.1.2 Membuat Dictionary

```python
# Cara 1: Literal {}
mahasiswa = {
    "nama": "Ahmad Fauzan",
    "nim": "2025001",
    "prodi": "Informatika",
    "ipk": 3.75,
    "aktif": True
}

# Cara 2: Fungsi dict()
mahasiswa = dict(nama="Ahmad", nim="2025001", ipk=3.75)

# Cara 3: Dari list of tuples
pairs = [("nama", "Ahmad"), ("nim", "2025001")]
mahasiswa = dict(pairs)

# Dictionary kosong
kosong = {}
juga_kosong = dict()
```

### 8.1.3 Akses, Tambah, Ubah, Hapus (CRUD)

```python
mhs = {"nama": "Ahmad", "nim": "2025001", "ipk": 3.75}

# READ — Akses value
print(mhs["nama"])         # "Ahmad"
print(mhs.get("ipk"))     # 3.75
print(mhs.get("alamat", "Tidak ada"))  # "Tidak ada" (default)
# mhs["alamat"]  # KeyError! (tanpa .get())

# CREATE — Tambah key baru
mhs["prodi"] = "Informatika"
mhs["semester"] = 2
print(mhs)

# UPDATE — Ubah value
mhs["ipk"] = 3.80
print(f"IPK baru: {mhs['ipk']}")

# DELETE — Hapus key
del mhs["semester"]
# atau
ipk = mhs.pop("ipk")  # hapus dan kembalikan value
print(f"IPK dihapus: {ipk}")
```

> **Tips:** Selalu gunakan `.get(key, default)` daripada `dict[key]` jika ada kemungkinan key tidak ada. Ini menghindari `KeyError`.

### 8.1.4 Dictionary Methods

| Method | Deskripsi | Contoh |
|--------|-----------|--------|
| `keys()` | Semua keys | `mhs.keys()` → `dict_keys(['nama', 'nim'])` |
| `values()` | Semua values | `mhs.values()` → `dict_values(['Ahmad', '2025001'])` |
| `items()` | Semua pasangan (key, value) | `mhs.items()` → `dict_items([...])` |
| `get(k, d)` | Value dari key k, default d | `mhs.get('alamat', '-')` → `'-'` |
| `update(d2)` | Gabungkan dict lain | `mhs.update({'kota': 'Jakarta'})` |
| `pop(k)` | Hapus key k, kembalikan value | `mhs.pop('nim')` → `'2025001'` |
| `setdefault(k, v)` | Set value hanya jika key belum ada | `mhs.setdefault('aktif', True)` |
| `clear()` | Kosongkan dict | `mhs.clear()` |
| `copy()` | Salin dict (shallow) | `salinan = mhs.copy()` |

### 8.1.5 Iterasi pada Dictionary

```python
mahasiswa = {
    "nama": "Ahmad Fauzan",
    "nim": "2025001",
    "prodi": "Informatika",
    "ipk": 3.75
}

# Iterasi keys
for key in mahasiswa:
    print(f"  {key}: {mahasiswa[key]}")

# Iterasi key-value pairs (lebih Pythonic)
for key, value in mahasiswa.items():
    print(f"  {key}: {value}")

# Iterasi hanya values
for value in mahasiswa.values():
    print(f"  {value}")
```

### 8.1.6 Nested Dictionary

```python
# Dictionary berisi dictionary
kelas = {
    "2025001": {
        "nama": "Ahmad Fauzan",
        "nilai": {"tugas": 85, "uts": 78, "uas": 82}
    },
    "2025002": {
        "nama": "Siti Aminah",
        "nilai": {"tugas": 92, "uts": 88, "uas": 90}
    },
    "2025003": {
        "nama": "Budi Santoso",
        "nilai": {"tugas": 76, "uts": 80, "uas": 78}
    }
}

# Akses nested
print(kelas["2025001"]["nama"])           # Ahmad Fauzan
print(kelas["2025002"]["nilai"]["uts"])    # 88

# Iterasi nested dict
for nim, data in kelas.items():
    n = data["nilai"]
    rata = (n["tugas"] + n["uts"] + n["uas"]) / 3
    print(f"  {data['nama']} ({nim}): {rata:.1f}")
```

---

## 8.2 Set: Koleksi Unik

### 8.2.1 Apa Itu Set?

**Set** adalah koleksi elemen **unik** (tidak ada duplikat) dan **tidak terurut** (unordered). Set mengikuti konsep himpunan dalam matematika.

```python
# Membuat set
buah = {"apel", "mangga", "durian", "apel"}  # duplikat "apel" dihapus
print(buah)  # {"apel", "mangga", "durian"} (urutan bisa berbeda)

# Dari list (menghapus duplikat)
angka = [1, 2, 3, 2, 1, 4, 3, 5]
unik = set(angka)
print(unik)  # {1, 2, 3, 4, 5}

# Set kosong — HARUS pakai set(), bukan {}
kosong = set()  # {} membuat dict kosong!
```

### 8.2.2 Operasi Himpunan

```
         Set A              Set B
     ┌───────────┐     ┌───────────┐
     │     ┌─────┼─────┼─────┐     │
     │  1  │  3  │     │  3  │  6  │
     │  2  │  4  │     │  4  │  7  │
     │     │  5  │     │  5  │     │
     │     └─────┼─────┼─────┘     │
     └───────────┘     └───────────┘
```

```python
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

# Union (gabungan): A ∪ B — semua elemen dari A dan B
print(A | B)         # {1, 2, 3, 4, 5, 6, 7}
print(A.union(B))    # sama

# Intersection (irisan): A ∩ B — elemen yang ada di keduanya
print(A & B)              # {3, 4, 5}
print(A.intersection(B))  # sama

# Difference (selisih): A - B — elemen A yang tidak ada di B
print(A - B)             # {1, 2}
print(A.difference(B))   # sama

# Symmetric difference: elemen yang ada di A ATAU B, tapi tidak keduanya
print(A ^ B)                        # {1, 2, 6, 7}
print(A.symmetric_difference(B))    # sama
```

### 8.2.3 Set Methods

| Method | Deskripsi | Contoh |
|--------|-----------|--------|
| `add(x)` | Tambah elemen | `s.add(5)` |
| `remove(x)` | Hapus elemen (error jika tidak ada) | `s.remove(5)` |
| `discard(x)` | Hapus elemen (tidak error jika tidak ada) | `s.discard(5)` |
| `pop()` | Hapus & kembalikan elemen acak | `s.pop()` |
| `clear()` | Kosongkan set | `s.clear()` |
| `union(s2)` | Gabungan | `s.union(s2)` |
| `intersection(s2)` | Irisan | `s.intersection(s2)` |
| `difference(s2)` | Selisih | `s.difference(s2)` |
| `issubset(s2)` | Apakah s ⊂ s2? | `s.issubset(s2)` |
| `issuperset(s2)` | Apakah s ⊃ s2? | `s.issuperset(s2)` |

```python
# Studi kasus: mahasiswa yang mengambil kedua mata kuliah
alpro = {"Ahmad", "Siti", "Budi", "Dewi", "Fatimah"}
statistik = {"Siti", "Budi", "Hasan", "Rina", "Dewi"}

# Mahasiswa yang mengambil keduanya
dua_mk = alpro & statistik
print(f"Mengambil keduanya: {dua_mk}")  # {'Siti', 'Budi', 'Dewi'}

# Hanya mengambil AlPro
hanya_alpro = alpro - statistik
print(f"Hanya AlPro: {hanya_alpro}")  # {'Ahmad', 'Fatimah'}

# Semua mahasiswa (tanpa duplikat)
semua = alpro | statistik
print(f"Semua mahasiswa ({len(semua)}): {semua}")
```

### 8.2.4 Frozen Set

**Frozenset** adalah set yang immutable — tidak bisa diubah setelah dibuat:

```python
fs = frozenset([1, 2, 3, 4])
# fs.add(5)  # AttributeError — tidak bisa diubah

# Frozenset bisa jadi key dictionary (karena hashable)
jadwal = {
    frozenset(["Senin", "Rabu"]): "Algoritma dan Pemrograman",
    frozenset(["Selasa", "Kamis"]): "Kalkulus",
}
```

---

## 8.3 Hashable vs Unhashable

### 8.3.1 Apa Itu Hash?

**Hash** adalah nilai integer tetap yang dihitung dari sebuah objek. Python menggunakan hash untuk:
- **Dictionary keys** — mencari key dengan cepat
- **Set elements** — memeriksa keberadaan elemen dengan cepat

```python
# Tipe hashable (bisa di-hash)
print(hash(42))           # integer → hashable
print(hash("hello"))      # string → hashable
print(hash((1, 2, 3)))    # tuple → hashable

# Tipe unhashable (TIDAK bisa di-hash)
# hash([1, 2, 3])    # TypeError — list unhashable
# hash({1: "a"})     # TypeError — dict unhashable
# hash({1, 2, 3})    # TypeError — set unhashable
```

### 8.3.2 Implikasi Praktis

```python
# Dict key HARUS hashable
valid = {
    "nama": "Ahmad",       # string ✓
    42: "angka",           # int ✓
    (1, 2): "tuple",       # tuple ✓
}

# Ini TIDAK BISA:
# invalid = {[1, 2]: "list"}  # TypeError — list unhashable

# Set elemen HARUS hashable
valid_set = {"apel", 42, (1, 2)}  # ✓
# invalid_set = {[1, 2], "apel"}  # TypeError — list unhashable
```

---

## 8.4 Pemilihan Struktur Data yang Tepat

### 8.4.1 Decision Tree

```
                    Apakah data berpasangan
                    (key-value)?
                   ╱                    ╲
                 Ya                     Tidak
                 │                        │
            ╔════════╗              Apakah urutan
            ║  DICT  ║              penting?
            ╚════════╝             ╱          ╲
                                 Ya           Tidak
                                 │              │
                           Apakah data     ╔════════╗
                           bisa berubah?   ║  SET   ║
                          ╱          ╲     ╚════════╝
                        Ya           Tidak
                        │              │
                   ╔════════╗    ╔════════╗
                   ║  LIST  ║    ║ TUPLE  ║
                   ╚════════╝    ╚════════╝
```

### 8.4.2 Perbandingan Performa

| Operasi | List | Tuple | Dict | Set |
|---------|------|-------|------|-----|
| Akses by index | O(1) | O(1) | — | — |
| Akses by key | — | — | O(1) | — |
| Cari elemen (`in`) | O(n) | O(n) | O(1) | O(1) |
| Tambah elemen | O(1)* | — | O(1) | O(1) |
| Hapus elemen | O(n) | — | O(1) | O(1) |
| Sort | O(n log n) | — | — | — |

*O(1) amortized untuk append

> **Insight:** Jika sering melakukan pencarian (`in`), gunakan **set** atau **dict** (O(1)) daripada **list** (O(n)).

### 8.4.3 Common Patterns

**Counting (menghitung frekuensi):**
```python
teks = "algoritma dan pemrograman di era ai"
kata_list = teks.split()

# Pattern: counting with dict
frekuensi = {}
for kata in kata_list:
    frekuensi[kata] = frekuensi.get(kata, 0) + 1

print(frekuensi)
# {'algoritma': 1, 'dan': 1, 'pemrograman': 1, 'di': 1, 'era': 1, 'ai': 1}
```

**Deduplication (menghapus duplikat):**
```python
data = [1, 5, 2, 3, 5, 1, 4, 2, 3, 5]
unik = list(set(data))  # menghapus duplikat
print(unik)  # [1, 2, 3, 4, 5] (urutan bisa berbeda)

# Jika urutan asli penting:
seen = set()
unik_ordered = []
for x in data:
    if x not in seen:
        seen.add(x)
        unik_ordered.append(x)
print(unik_ordered)  # [1, 5, 2, 3, 4]
```

**Grouping (mengelompokkan):**
```python
mahasiswa = [
    ("Ahmad", "Informatika"),
    ("Siti", "Sistem Informasi"),
    ("Budi", "Informatika"),
    ("Dewi", "Sistem Informasi"),
    ("Fatimah", "Informatika"),
]

# Group by prodi
per_prodi = {}
for nama, prodi in mahasiswa:
    if prodi not in per_prodi:
        per_prodi[prodi] = []
    per_prodi[prodi].append(nama)

for prodi, daftar_nama in per_prodi.items():
    print(f"  {prodi}: {daftar_nama}")
```

---

## 8.5 Dictionary Comprehension dan Set Comprehension

```python
# Dictionary comprehension
# {key_expr: value_expr for var in iterable if condition}

nama = ["Ahmad", "Siti", "Budi"]
nilai = [85, 92, 78]

# Dict dari dua list
data = {n: v for n, v in zip(nama, nilai)}
print(data)  # {'Ahmad': 85, 'Siti': 92, 'Budi': 78}

# Filter: hanya yang lulus
lulus = {n: v for n, v in data.items() if v >= 80}
print(lulus)  # {'Ahmad': 85, 'Siti': 92}

# Transformasi: kuadrat angka 1-5
kuadrat = {x: x**2 for x in range(1, 6)}
print(kuadrat)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```python
# Set comprehension
# {expr for var in iterable if condition}

kalimat = "algoritma dan pemrograman dengan python"
huruf_vokal = {c for c in kalimat if c in "aiueo"}
print(huruf_vokal)  # {'a', 'i', 'o', 'e', 'u'}
```

---

## 8.6 Studi Kasus

### 8.6.1 Aplikasi Buku Telepon

```python
def buku_telepon():
    """Aplikasi buku telepon sederhana menggunakan dictionary."""
    kontak = {}

    while True:
        print("\n--- BUKU TELEPON ---")
        print("1. Tambah kontak")
        print("2. Cari kontak")
        print("3. Tampilkan semua")
        print("4. Hapus kontak")
        print("5. Keluar")

        pilihan = input("Pilih (1-5): ")

        if pilihan == "1":
            nama = input("Nama : ")
            nomor = input("Nomor: ")
            kontak[nama] = nomor
            print(f"Kontak '{nama}' disimpan.")

        elif pilihan == "2":
            nama = input("Cari nama: ")
            nomor = kontak.get(nama)
            if nomor:
                print(f"  {nama}: {nomor}")
            else:
                print(f"  '{nama}' tidak ditemukan.")

        elif pilihan == "3":
            if not kontak:
                print("  Buku telepon kosong.")
            else:
                for nama in sorted(kontak):
                    print(f"  {nama}: {kontak[nama]}")

        elif pilihan == "4":
            nama = input("Nama yang dihapus: ")
            if kontak.pop(nama, None):
                print(f"  '{nama}' dihapus.")
            else:
                print(f"  '{nama}' tidak ditemukan.")

        elif pilihan == "5":
            print("Sampai jumpa!")
            break

buku_telepon()
```

### 8.6.2 Analisis Frekuensi Kata

```python
def analisis_frekuensi(teks):
    """Menganalisis frekuensi kata dalam teks."""
    # Bersihkan dan pecah teks
    kata_list = teks.lower().split()

    # Hitung frekuensi dengan dict
    frekuensi = {}
    for kata in kata_list:
        # Bersihkan tanda baca
        kata = kata.strip(".,!?;:")
        if kata:
            frekuensi[kata] = frekuensi.get(kata, 0) + 1

    return frekuensi

def tampilkan_frekuensi(frekuensi, top_n=10):
    """Menampilkan kata dengan frekuensi tertinggi."""
    # Urutkan berdasarkan frekuensi (descending)
    terurut = sorted(frekuensi.items(), key=lambda x: x[1], reverse=True)

    print(f"\n{'Kata':<20} {'Frekuensi':>9} {'Grafik'}")
    print("-" * 45)
    for kata, jumlah in terurut[:top_n]:
        bar = "█" * jumlah
        print(f"{kata:<20} {jumlah:>9} {bar}")

# Contoh penggunaan
teks_pancasila = """
Ketuhanan Yang Maha Esa. Kemanusiaan yang adil dan beradab.
Persatuan Indonesia. Kerakyatan yang dipimpin oleh hikmat
kebijaksanaan dalam permusyawaratan perwakilan. Keadilan
sosial bagi seluruh rakyat Indonesia.
"""

frek = analisis_frekuensi(teks_pancasila)
tampilkan_frekuensi(frek)

# Statistik unik
total_kata = sum(frek.values())
kata_unik = len(frek)
print(f"\nTotal kata: {total_kata}")
print(f"Kata unik: {kata_unik}")
```

### 8.6.3 Sistem Inventaris Toko

```python
def sistem_inventaris():
    """Sistem inventaris toko menggunakan dict + set."""
    inventaris = {
        "Indomie Goreng": {"harga": 3500, "stok": 100, "kategori": "Makanan"},
        "Aqua 600ml": {"harga": 4000, "stok": 50, "kategori": "Minuman"},
        "Teh Botol 450ml": {"harga": 5000, "stok": 30, "kategori": "Minuman"},
        "Chitato 68g": {"harga": 10000, "stok": 25, "kategori": "Snack"},
    }

    # Set untuk kategori unik
    kategori = {v["kategori"] for v in inventaris.values()}
    print(f"Kategori: {kategori}")

    # Total nilai inventaris
    total = sum(v["harga"] * v["stok"] for v in inventaris.values())
    print(f"Total nilai inventaris: Rp {total:,.0f}")

    # Tampilkan per kategori
    for kat in sorted(kategori):
        print(f"\n[{kat}]")
        for nama, data in inventaris.items():
            if data["kategori"] == kat:
                print(f"  {nama}: Rp {data['harga']:,} × {data['stok']} = "
                      f"Rp {data['harga'] * data['stok']:,}")

sistem_inventaris()
```

---

## AI Corner: AI untuk Pemilihan Struktur Data

**Level: Menengah**

### Meminta AI Merekomendasikan Struktur Data

```
Prompt: "Saya membuat program untuk menyimpan data mahasiswa
yang harus bisa: (1) dicari by NIM, (2) diurutkan by nama,
(3) dihitung rata-rata nilai per kelas. Struktur data apa
yang paling tepat di Python dan mengapa?"
```

### Validasi Rekomendasi AI

Tanyakan pada diri sendiri:
1. Apakah operasi utama sesuai dengan kelebihan struktur data?
2. Apakah Big-O operasi kunci sudah optimal?
3. Apakah ada alternatif yang lebih sederhana?

---

## Latihan Soal

### Tingkat Dasar

1. Buatlah dictionary `profil` berisi: nama, nim, prodi, semester, ipk. Tampilkan semua informasi menggunakan loop.

2. Buatlah set dari list `[1, 2, 3, 2, 4, 3, 5, 1]`. Berapa jumlah elemen unik?

3. Diberikan `A = {1,2,3,4,5}` dan `B = {4,5,6,7,8}`. Hitung union, intersection, dan difference.

4. Buatlah dictionary yang memetakan nama hari (Senin-Minggu) ke angka (1-7). Minta user input nama hari, tampilkan angkanya.

5. Jelaskan mengapa list tidak bisa dipakai sebagai key dictionary. Tipe data apa yang bisa?

### Tingkat Menengah

1. Buatlah program frekuensi huruf: input kalimat, output frekuensi setiap huruf (dict), diurutkan dari frekuensi tertinggi.

2. Buatlah dictionary comprehension yang memetakan angka 1-10 ke statusnya: "genap" atau "ganjil".

3. Diberikan dua dict `nilai_uts = {"Ahmad": 85, "Siti": 90}` dan `nilai_uas = {"Ahmad": 80, "Siti": 95, "Budi": 78}`. Gabungkan dan hitung rata-rata UTS+UAS per mahasiswa.

4. Implementasikan program sederhana untuk menghitung berapa banyak item unik yang dibeli pelanggan (gunakan set) dan total belanja (gunakan dict untuk harga).

5. Buat decision tree (pseudocode) untuk memilih antara list, tuple, dict, dan set berdasarkan kebutuhan. Uji dengan 3 skenario berbeda.

### Tingkat Mahir

1. Buatlah sistem inventaris toko dengan fitur lengkap: CRUD barang, cari barang, filter per kategori (set), dan laporan stok (dict). Gunakan nested dictionary.

2. Buatlah program yang membaca paragraf teks dan menghasilkan: (a) frekuensi kata (dict), (b) kata unik (set), (c) 5 kata terbanyak (sorted dict), (d) kata yang muncul tepat 1 kali (filtering).

3. Bandingkan performa pencarian `in` pada list vs set untuk 10.000 elemen. Gunakan modul `time` untuk mengukur. Buat tabel perbandingan dan jelaskan perbedaannya menggunakan konsep hash.

---

## Rangkuman

- **Dictionary** menyimpan pasangan **key-value**. Key harus unik dan hashable. Akses by key adalah O(1).
- Operasi dict: `dict[key]`, `.get()`, `.keys()`, `.values()`, `.items()`, `.update()`, `.pop()`.
- **Set** menyimpan elemen **unik** dan mendukung operasi himpunan: union (`|`), intersection (`&`), difference (`-`).
- **Hashable** types (bisa jadi dict key/set element): int, float, str, tuple, frozenset.
- **Unhashable** types: list, dict, set.
- **Pemilihan struktur data**: dict untuk key-value, set untuk keunikan, list untuk data berubah terurut, tuple untuk data tetap.
- **Dict comprehension**: `{k: v for k, v in iterable}`.
- **Set comprehension**: `{expr for x in iterable}`.
- Common patterns: **counting** (dict), **deduplication** (set), **grouping** (dict of lists).

---

## Referensi

1. Downey, A. B. (2024). *Think Python* (3rd ed.). O'Reilly Media.
2. Python Software Foundation. (2026). Data Structures. https://docs.python.org/3/tutorial/datastructures.html
3. Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.). MIT Press.
4. Lutz, M. (2023). *Learning Python* (6th ed.). O'Reilly Media.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
