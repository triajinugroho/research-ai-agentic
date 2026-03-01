# Minggu 9: Dictionary, Set, dan Pemilihan Struktur Data

## Informasi Modul

| Komponen | Keterangan |
|----------|------------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Kode MK** | IF1101 |
| **SKS** | 3 SKS |
| **Minggu** | 9 (Sembilan) |
| **Topik** | Dictionary, Set, dan Pemilihan Struktur Data |
| **CPMK** | CPMK-5: Mampu menerapkan struktur data dasar untuk menyimpan dan mengelola data secara efektif |
| **Sub-CPMK** | CPMK-5.5: Membuat dan memanipulasi dictionary (key-value pairs) |
| | CPMK-5.6: Menggunakan set untuk operasi himpunan pada data unik |
| | CPMK-5.7: Memilih struktur data yang tepat berdasarkan kebutuhan masalah |
| **Durasi** | 150 menit |
| **Metode** | Ceramah, Live Coding, Latihan Terbimbing, Diskusi |
| **Bahasa Pemrograman** | Python |
| **Semester** | Genap 2025/2026 |
| **Pengajar** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. **Membuat** dictionary beserta operasi CRUD (Create, Read, Update, Delete) dan menerapkan dictionary comprehension serta nested dictionary (C4 — Menganalisis)
2. **Mengoperasikan** set untuk menyimpan data unik dan melakukan operasi himpunan: union, intersection, dan difference (C3 — Menerapkan)
3. **Mengevaluasi** kelebihan dan kekurangan masing-masing struktur data (list, tuple, dictionary, set) untuk menentukan pilihan yang tepat sesuai kebutuhan masalah (C5 — Mengevaluasi)
4. **Menyusun** proposal proyek akhir yang mengidentifikasi masalah, solusi berbasis pemrograman, dan rencana implementasi (C6 — Mencipta)

---

## Materi Pembelajaran

### 9.1 Dictionary (Key-Value Pairs)

Dictionary adalah struktur data yang menyimpan pasangan **key-value**. Setiap key bersifat unik dan digunakan untuk mengakses value-nya.

#### 9.1.1 Membuat Dictionary

```python
# Dictionary kosong
data_kosong = {}
data_kosong2 = dict()

# Dictionary dengan data awal
mahasiswa = {
    "nama": "Ahmad Fauzi",
    "nim": "2025001",
    "prodi": "Informatika",
    "ipk": 3.75
}

# Dari list of tuples
pasangan = [("a", 1), ("b", 2), ("c", 3)]
dari_tuple = dict(pasangan)
```

#### 9.1.2 Operasi CRUD pada Dictionary

```python
kontak = {"Ali": "081234567890", "Budi": "089876543210"}

# CREATE — menambah entry baru
kontak["Citra"] = "085511223344"

# READ — mengakses value
print(kontak["Ali"])            # "081234567890"
print(kontak.get("Dina", "Tidak ditemukan"))  # aman dari KeyError

# UPDATE — mengubah value
kontak["Ali"] = "081299998888"

# DELETE — menghapus entry
del kontak["Budi"]              # hapus dengan key
nomor = kontak.pop("Citra")     # hapus dan kembalikan value
```

#### 9.1.3 Method Penting Dictionary

| Method | Fungsi | Contoh |
|--------|--------|--------|
| `keys()` | Mengembalikan semua key | `kontak.keys()` |
| `values()` | Mengembalikan semua value | `kontak.values()` |
| `items()` | Mengembalikan pasangan (key, value) | `kontak.items()` |
| `get(key, default)` | Mengakses value dengan default | `kontak.get("X", "-")` |
| `update(dict2)` | Menggabungkan dictionary | `kontak.update(baru)` |
| `pop(key)` | Menghapus dan mengembalikan value | `kontak.pop("Ali")` |

```python
# Iterasi dictionary
nilai_mhs = {"Ahmad": 85, "Budi": 92, "Citra": 78}

for nama, nilai in nilai_mhs.items():
    status = "Lulus" if nilai >= 80 else "Perlu perbaikan"
    print(f"{nama}: {nilai} — {status}")
```

#### 9.1.4 Dictionary Comprehension

```python
# Kuadrat angka 1–5
kuadrat = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter: hanya nilai lulus (>= 75)
semua_nilai = {"Ahmad": 85, "Budi": 60, "Citra": 92, "Dina": 70}
lulus = {k: v for k, v in semua_nilai.items() if v >= 75}
# {"Ahmad": 85, "Citra": 92}
```

#### 9.1.5 Nested Dictionary

```python
kelas = {
    "IF-A": {
        "ketua": "Rina",
        "jumlah": 35,
        "mata_kuliah": ["Algoritma", "Kalkulus", "Fisika"]
    },
    "IF-B": {
        "ketua": "Sandi",
        "jumlah": 33,
        "mata_kuliah": ["Algoritma", "Kalkulus", "Statistika"]
    }
}

# Akses nested
print(kelas["IF-A"]["ketua"])               # "Rina"
print(kelas["IF-B"]["mata_kuliah"][0])       # "Algoritma"
```

### 9.2 Set (Himpunan Data Unik)

Set adalah koleksi **tidak berurutan** yang hanya menyimpan elemen **unik** (tanpa duplikat).

#### 9.2.1 Membuat dan Menggunakan Set

```python
buah = {"apel", "mangga", "jeruk", "apel"}  # duplikat otomatis dihapus
print(buah)  # {"apel", "mangga", "jeruk"}

# Dari list (menghilangkan duplikat)
angka = [1, 2, 3, 2, 4, 3, 5]
unik = set(angka)  # {1, 2, 3, 4, 5}

# Menambah dan menghapus elemen
buah.add("durian")
buah.discard("jeruk")   # aman jika tidak ada
```

#### 9.2.2 Operasi Himpunan

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union (gabungan)
print(A | B)        # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))

# Intersection (irisan)
print(A & B)            # {4, 5}
print(A.intersection(B))

# Difference (selisih)
print(A - B)            # {1, 2, 3}
print(A.difference(B))

# Symmetric difference (elemen yang tidak di keduanya)
print(A ^ B)                    # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))
```

#### 9.2.3 Kasus Penggunaan Set

```python
# Menghitung kata unik dalam teks
teks = "saya belajar python karena python itu mudah dan saya suka python"
kata_list = teks.split()
kata_unik = set(kata_list)
print(f"Total kata: {len(kata_list)}, Kata unik: {len(kata_unik)}")

# Cek keanggotaan (sangat cepat pada set)
email_terdaftar = {"ali@uai.ac.id", "budi@uai.ac.id", "citra@uai.ac.id"}
cek = "ali@uai.ac.id"
print(cek in email_terdaftar)  # True
```

### 9.3 Pemilihan Struktur Data

| Kriteria | List | Tuple | Dictionary | Set |
|----------|------|-------|------------|-----|
| **Urutan** | Terurut (index) | Terurut (index) | Tidak terurut* | Tidak terurut |
| **Mutable** | Ya | Tidak | Ya | Ya |
| **Duplikat** | Boleh | Boleh | Key unik | Tidak boleh |
| **Akses** | Index `[i]` | Index `[i]` | Key `[k]` | Tidak bisa index |
| **Kapan dipakai** | Koleksi data terurut | Data tetap/konstan | Pasangan key-value | Data unik, operasi himpunan |

*Sejak Python 3.7, dictionary mempertahankan urutan penyisipan.

**Framework Pemilihan:**

```
Apakah data perlu pasangan key-value?
├── Ya → Dictionary
└── Tidak
    ├── Apakah data harus unik, tanpa urutan?
    │   ├── Ya → Set
    │   └── Tidak
    │       ├── Apakah data tidak boleh berubah?
    │       │   ├── Ya → Tuple
    │       │   └── Tidak → List
```

---

## Kegiatan Pembelajaran

### Pre-Class (15 menit)

- Membaca materi dictionary dan set dari referensi utama
- Menonton video singkat tentang perbedaan struktur data Python
- Menyiapkan pertanyaan tentang kapan menggunakan dictionary vs list

### In-Class (120 menit)

| Waktu | Aktivitas | Deskripsi |
|-------|-----------|-----------|
| 0–25 menit | Ceramah: Dictionary | Penjelasan konsep key-value, CRUD, methods, comprehension, dan nested dictionary |
| 25–45 menit | Live Coding: Contact Book | Membangun aplikasi buku kontak sederhana menggunakan dictionary |
| 45–65 menit | Ceramah: Set | Penjelasan set, operasi himpunan, dan kasus penggunaan |
| 65–85 menit | Ceramah: Pemilihan Struktur Data | Perbandingan list vs tuple vs dictionary vs set dengan decision framework |
| 85–110 menit | Latihan Terbimbing | Mahasiswa mengerjakan latihan pemilihan struktur data yang tepat untuk berbagai skenario |
| 110–120 menit | Pengumpulan Proposal Proyek Akhir | Mahasiswa mengumpulkan proposal proyek akhir (1 halaman) |

### Post-Class (15 menit)

- Menyelesaikan latihan pemilihan struktur data yang belum selesai
- Merevisi proposal proyek akhir berdasarkan masukan dosen (jika ada)
- Membaca materi minggu depan: Algoritma Pencarian

---

## Penugasan

### Proyek Akhir — Proposal (Deadline: Minggu 9)

| Komponen | Keterangan |
|----------|------------|
| **Format** | 1 halaman (A4), PDF |
| **Isi** | 1. Identifikasi masalah yang akan diselesaikan |
| | 2. Solusi berbasis pemrograman Python yang diusulkan |
| | 3. Rencana implementasi (fitur utama, struktur data yang digunakan, timeline) |
| **Pengumpulan** | LMS, akhir pertemuan Minggu 9 |
| **Penilaian** | Kejelasan masalah (30%), Relevansi solusi (40%), Kelayakan rencana (30%) |

---

## Referensi

1. Downey, A. B. (2015). *Think Python: How to Think Like a Computer Scientist* (2nd ed.). O'Reilly Media. — Chapter 11: Dictionaries, Chapter 19: The Goodies.
2. Matthes, E. (2019). *Python Crash Course* (2nd ed.). No Starch Press. — Chapter 6: Dictionaries.
3. Python Software Foundation. (2025). *Python 3.12 Documentation — Data Structures*. https://docs.python.org/3/tutorial/datastructures.html
4. Lutz, M. (2013). *Learning Python* (5th ed.). O'Reilly Media. — Part II: Types and Operations.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
