# Lab 09: Pemilihan Struktur Data

## Informasi Praktikum

| Komponen | Keterangan |
|----------|------------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Kode MK** | INF-101 |
| **Semester** | Genap 2025/2026 |
| **Praktikum** | Lab 09 — Pemilihan Struktur Data |
| **Durasi** | 75 menit |
| **Prasyarat** | Lab 07 (List dan Tuple), Modul Minggu 9 |
| **Platform** | Google Colab |
| **Pengajar** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. **Membuat** dan memanipulasi dictionary dengan operasi CRUD (Create, Read, Update, Delete) serta dictionary comprehension
2. **Menggunakan** set untuk menyimpan data unik dan melakukan operasi himpunan (union, intersection, difference)
3. **Mengevaluasi** kapan menggunakan list, tuple, dictionary, atau set berdasarkan kebutuhan masalah
4. **Membangun** aplikasi Buku Telepon sederhana menggunakan dictionary sebagai struktur data utama

---

## Persiapan

- Buka Google Colab di browser: [colab.research.google.com](https://colab.research.google.com)
- Buat notebook baru dengan nama: `Lab09_NIM_NamaLengkap.ipynb`
- Pastikan sudah memahami materi list dan tuple dari Lab 07

---

## Langkah-langkah Praktikum

### Langkah 1: Operasi Dasar Dictionary (15 menit)

Dictionary menyimpan data dalam pasangan **key-value**. Setiap key bersifat unik.

```python
# === MEMBUAT DICTIONARY ===
mahasiswa = {
    "nama": "Siti Aisyah",
    "nim": "2025001",
    "prodi": "Informatika",
    "ipk": 3.82
}
print("Data mahasiswa:", mahasiswa)

# === READ — Mengakses nilai ===
print("\nNama:", mahasiswa["nama"])
print("IPK:", mahasiswa.get("ipk", 0.0))
print("Alamat:", mahasiswa.get("alamat", "Tidak tersedia"))

# === UPDATE — Mengubah nilai ===
mahasiswa["ipk"] = 3.85
mahasiswa["alamat"] = "Jakarta Selatan"
print("\nSetelah update:", mahasiswa)

# === DELETE — Menghapus entry ===
alamat = mahasiswa.pop("alamat")
print(f"\nAlamat '{alamat}' dihapus.")
print("Data sekarang:", mahasiswa)

# === ITERASI ===
print("\n--- Iterasi Dictionary ---")
for key, value in mahasiswa.items():
    print(f"  {key:10s}: {value}")

print("\nSemua key:", list(mahasiswa.keys()))
print("Semua value:", list(mahasiswa.values()))
```

Jalankan kode di atas dan perhatikan hasilnya. Method `.get()` lebih aman karena tidak error jika key tidak ditemukan.

### Langkah 2: Dictionary Comprehension dan Nested Dictionary (10 menit)

```python
# === DICTIONARY COMPREHENSION ===
# Kuadrat bilangan 1-10
kuadrat = {x: x**2 for x in range(1, 11)}
print("Kuadrat:", kuadrat)

# Filter: hanya bilangan genap
kuadrat_genap = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print("Kuadrat genap:", kuadrat_genap)

# === NESTED DICTIONARY ===
kelas_alpro = {
    "2025001": {"nama": "Ahmad Fauzi", "nilai": 85},
    "2025002": {"nama": "Budi Santoso", "nilai": 92},
    "2025003": {"nama": "Citra Dewi", "nilai": 78},
    "2025004": {"nama": "Diana Putri", "nilai": 95},
}

print("\n--- Daftar Mahasiswa ---")
for nim, data in kelas_alpro.items():
    print(f"  NIM {nim}: {data['nama']} — Nilai: {data['nilai']}")

# Hitung rata-rata nilai
rata_rata = sum(m["nilai"] for m in kelas_alpro.values()) / len(kelas_alpro)
print(f"\nRata-rata kelas: {rata_rata:.2f}")

# Cari mahasiswa dengan nilai tertinggi
nim_terbaik = max(kelas_alpro, key=lambda k: kelas_alpro[k]["nilai"])
print(f"Nilai tertinggi: {kelas_alpro[nim_terbaik]['nama']} ({kelas_alpro[nim_terbaik]['nilai']})")
```

### Langkah 3: Operasi Set (15 menit)

Set menyimpan elemen **unik** tanpa urutan tertentu. Sangat efisien untuk operasi himpunan.

```python
# === MEMBUAT SET ===
buah = {"apel", "jeruk", "mangga", "apel", "jeruk"}  # duplikat otomatis hilang
print("Set buah:", buah)
print("Jumlah elemen:", len(buah))

# === MENAMBAH DAN MENGHAPUS ===
buah.add("durian")
buah.add("rambutan")
buah.discard("apel")  # aman — tidak error jika tidak ada
print("Setelah modifikasi:", buah)

# === OPERASI HIMPUNAN ===
matkul_aisyah = {"Alpro", "Kalkulus", "Fisika", "Statistik"}
matkul_budi = {"Alpro", "Statistik", "Basis Data", "Jaringan"}

print("\n--- Operasi Himpunan ---")
print("Mata kuliah Aisyah:", matkul_aisyah)
print("Mata kuliah Budi  :", matkul_budi)

# Union — semua mata kuliah
gabungan = matkul_aisyah | matkul_budi
print(f"\nUnion (semua)        : {gabungan}")

# Intersection — mata kuliah yang sama
irisan = matkul_aisyah & matkul_budi
print(f"Intersection (sama)  : {irisan}")

# Difference — hanya milik Aisyah
hanya_aisyah = matkul_aisyah - matkul_budi
print(f"Hanya Aisyah         : {hanya_aisyah}")

# Symmetric difference — yang tidak sama
beda_simetris = matkul_aisyah ^ matkul_budi
print(f"Symmetric difference : {beda_simetris}")

# === SET UNTUK MENGHAPUS DUPLIKAT ===
nilai_ujian = [85, 90, 78, 85, 92, 78, 90, 95, 85]
nilai_unik = sorted(set(nilai_ujian))
print(f"\nNilai asli : {nilai_ujian}")
print(f"Nilai unik : {nilai_unik}")
```

### Langkah 4: Framework Pemilihan Struktur Data (10 menit)

Kapan menggunakan masing-masing struktur data? Pelajari tabel berikut, lalu jalankan kode perbandingan.

| Kebutuhan | Struktur Data | Alasan |
|-----------|---------------|--------|
| Urutan data yang bisa diubah | `list` | Mutable, ordered, indexed |
| Urutan data yang tetap | `tuple` | Immutable, lebih cepat |
| Akses data via key | `dict` | Key-value lookup O(1) |
| Kumpulan data unik | `set` | Otomatis hapus duplikat, operasi himpunan |

```python
import time

# Perbandingan kecepatan pencarian: list vs set vs dict
data_list = list(range(1_000_000))
data_set = set(range(1_000_000))
data_dict = {i: True for i in range(1_000_000)}

target = 999_999  # elemen terakhir (worst case untuk list)

# Cari di list
start = time.time()
_ = target in data_list
waktu_list = time.time() - start

# Cari di set
start = time.time()
_ = target in data_set
waktu_set = time.time() - start

# Cari di dict
start = time.time()
_ = target in data_dict
waktu_dict = time.time() - start

print("=== Perbandingan Kecepatan Pencarian ===")
print(f"  List : {waktu_list:.6f} detik")
print(f"  Set  : {waktu_set:.6f} detik")
print(f"  Dict : {waktu_dict:.6f} detik")
print(f"\nSet {waktu_list/waktu_set:.0f}x lebih cepat dari list untuk pencarian!")
```

### Langkah 5: Mini Project — Aplikasi Buku Telepon (25 menit)

Bangun aplikasi buku telepon interaktif menggunakan dictionary.

```python
def tampilkan_menu():
    """Menampilkan menu utama aplikasi."""
    print("\n" + "=" * 40)
    print("   APLIKASI BUKU TELEPON")
    print("=" * 40)
    print("  1. Tambah Kontak")
    print("  2. Cari Kontak")
    print("  3. Hapus Kontak")
    print("  4. Tampilkan Semua Kontak")
    print("  5. Simpan ke File")
    print("  6. Muat dari File")
    print("  0. Keluar")
    print("-" * 40)

def tambah_kontak(buku_telepon):
    """Menambahkan kontak baru ke buku telepon."""
    nama = input("Masukkan nama: ").strip().title()
    if nama in buku_telepon:
        print(f"  Kontak '{nama}' sudah ada. Nomor lama: {buku_telepon[nama]}")
        konfirmasi = input("  Ganti nomor? (y/n): ").lower()
        if konfirmasi != 'y':
            return
    nomor = input("Masukkan nomor telepon: ").strip()
    buku_telepon[nama] = nomor
    print(f"  Kontak '{nama}' berhasil disimpan.")

def cari_kontak(buku_telepon):
    """Mencari kontak berdasarkan nama (partial match)."""
    query = input("Masukkan nama yang dicari: ").strip().lower()
    hasil = {k: v for k, v in buku_telepon.items() if query in k.lower()}
    if hasil:
        print(f"\n  Ditemukan {len(hasil)} kontak:")
        for nama, nomor in hasil.items():
            print(f"    {nama}: {nomor}")
    else:
        print("  Kontak tidak ditemukan.")

def hapus_kontak(buku_telepon):
    """Menghapus kontak dari buku telepon."""
    nama = input("Masukkan nama kontak yang akan dihapus: ").strip().title()
    if nama in buku_telepon:
        nomor = buku_telepon.pop(nama)
        print(f"  Kontak '{nama}' ({nomor}) berhasil dihapus.")
    else:
        print(f"  Kontak '{nama}' tidak ditemukan.")

def tampilkan_semua(buku_telepon):
    """Menampilkan semua kontak secara terurut."""
    if not buku_telepon:
        print("  Buku telepon kosong.")
        return
    print(f"\n  {'No':<4} {'Nama':<25} {'Nomor Telepon':<15}")
    print("  " + "-" * 44)
    for i, (nama, nomor) in enumerate(sorted(buku_telepon.items()), 1):
        print(f"  {i:<4} {nama:<25} {nomor:<15}")
    print(f"\n  Total: {len(buku_telepon)} kontak")

def simpan_ke_file(buku_telepon, nama_file="buku_telepon.txt"):
    """Menyimpan buku telepon ke file teks."""
    with open(nama_file, 'w') as f:
        for nama, nomor in sorted(buku_telepon.items()):
            f.write(f"{nama},{nomor}\n")
    print(f"  {len(buku_telepon)} kontak berhasil disimpan ke '{nama_file}'.")

def muat_dari_file(nama_file="buku_telepon.txt"):
    """Memuat buku telepon dari file teks."""
    buku_telepon = {}
    try:
        with open(nama_file, 'r') as f:
            for baris in f:
                baris = baris.strip()
                if ',' in baris:
                    nama, nomor = baris.split(',', 1)
                    buku_telepon[nama] = nomor
        print(f"  {len(buku_telepon)} kontak berhasil dimuat dari '{nama_file}'.")
    except FileNotFoundError:
        print(f"  File '{nama_file}' tidak ditemukan. Mulai dengan buku telepon kosong.")
    return buku_telepon

# === PROGRAM UTAMA ===
buku_telepon = {
    "Ahmad Fauzi": "081234567890",
    "Budi Santoso": "085678901234",
    "Citra Dewi": "087890123456",
}

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (0-6): ").strip()

    if pilihan == '1':
        tambah_kontak(buku_telepon)
    elif pilihan == '2':
        cari_kontak(buku_telepon)
    elif pilihan == '3':
        hapus_kontak(buku_telepon)
    elif pilihan == '4':
        tampilkan_semua(buku_telepon)
    elif pilihan == '5':
        simpan_ke_file(buku_telepon)
    elif pilihan == '6':
        buku_telepon = muat_dari_file()
    elif pilihan == '0':
        print("\nTerima kasih! Sampai jumpa.")
        break
    else:
        print("  Pilihan tidak valid. Silakan coba lagi.")
```

> **Catatan Colab:** Karena Google Colab tidak mendukung `input()` dalam loop tak terbatas dengan baik, Anda bisa menguji setiap fungsi secara terpisah di cell berbeda, atau batasi loop dengan jumlah iterasi tertentu untuk pengujian.

---

## Tantangan Tambahan

1. **Statistik Kontak:** Tambahkan fitur yang menampilkan jumlah kontak per huruf awal nama (gunakan dictionary comprehension).
2. **Multi-Nomor:** Modifikasi buku telepon agar setiap kontak bisa memiliki lebih dari satu nomor telepon (gunakan list sebagai value).
3. **Export CSV:** Tambahkan fitur export ke format CSV yang bisa dibuka di spreadsheet.

---

## Checklist Penyelesaian

- [ ] Mampu membuat dictionary dan melakukan operasi CRUD
- [ ] Mampu menggunakan dictionary comprehension dan nested dictionary
- [ ] Mampu membuat set dan melakukan operasi himpunan (union, intersection, difference)
- [ ] Memahami kapan menggunakan list, tuple, dict, atau set
- [ ] Berhasil menjalankan perbandingan kecepatan pencarian
- [ ] Menyelesaikan mini project Aplikasi Buku Telepon
- [ ] Notebook disimpan dengan nama `Lab09_NIM_NamaLengkap.ipynb`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
