# Lab 11: Algoritma Pengurutan

## Informasi Praktikum

| Komponen | Keterangan |
|----------|------------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Kode MK** | INF-101 |
| **Semester** | Genap 2025/2026 |
| **Praktikum** | Lab 11 — Algoritma Pengurutan |
| **Durasi** | 75 menit |
| **Prasyarat** | Lab 10 (Algoritma Pencarian), Modul Minggu 11 |
| **Platform** | Google Colab |
| **Pengajar** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. **Mengimplementasikan** tiga algoritma pengurutan dasar: Bubble Sort, Selection Sort, dan Insertion Sort
2. **Memvisualisasikan** proses pengurutan pada setiap pass untuk memahami mekanisme kerja algoritma
3. **Membandingkan** jumlah operasi dan waktu eksekusi ketiga algoritma pada berbagai ukuran data
4. **Membangun** program pengurutan data mahasiswa berdasarkan berbagai kriteria

---

## Persiapan

- Buka Google Colab di browser: [colab.research.google.com](https://colab.research.google.com)
- Buat notebook baru dengan nama: `Lab11_NIM_NamaLengkap.ipynb`
- Pastikan sudah memahami konsep perbandingan dan pertukaran (swap) elemen

---

## Langkah-langkah Praktikum

### Langkah 1: Bubble Sort dengan Visualisasi (15 menit)

Bubble Sort membandingkan elemen bersebelahan dan menukar jika urutannya salah. Elemen terbesar "menggelembung" ke akhir di setiap pass.

```python
def bubble_sort(data):
    """
    Mengurutkan data menggunakan Bubble Sort.
    Menampilkan proses setiap pass dan menghitung jumlah swap.
    """
    arr = data.copy()
    n = len(arr)
    total_swap = 0
    total_perbandingan = 0

    print(f"Data awal: {arr}\n")

    for i in range(n - 1):
        swap_pass = 0
        for j in range(n - 1 - i):
            total_perbandingan += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_pass += 1
                total_swap += 1
        print(f"  Pass {i+1}: {arr}  (swap: {swap_pass})")
        if swap_pass == 0:
            print("  → Tidak ada swap, data sudah terurut!")
            break

    print(f"\nHasil   : {arr}")
    print(f"Total perbandingan: {total_perbandingan}")
    print(f"Total swap        : {total_swap}")
    return arr

# Uji coba
nilai = [64, 34, 25, 12, 22, 11, 90]
print("=== BUBBLE SORT ===")
hasil = bubble_sort(nilai)
```

### Langkah 2: Selection Sort dengan Visualisasi (15 menit)

Selection Sort menemukan elemen terkecil di sisa array, lalu menempatkannya di posisi yang benar.

```python
def selection_sort(data):
    """
    Mengurutkan data menggunakan Selection Sort.
    Menampilkan proses setiap pass.
    """
    arr = data.copy()
    n = len(arr)
    total_swap = 0
    total_perbandingan = 0

    print(f"Data awal: {arr}\n")

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            total_perbandingan += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            total_swap += 1
            print(f"  Pass {i+1}: Tukar arr[{i}]={arr[min_idx]} dengan "
                  f"min={arr[i]} di index [{min_idx}] → {arr}")
        else:
            print(f"  Pass {i+1}: Elemen arr[{i}]={arr[i]} sudah di posisi benar → {arr}")

    print(f"\nHasil   : {arr}")
    print(f"Total perbandingan: {total_perbandingan}")
    print(f"Total swap        : {total_swap}")
    return arr

# Uji coba
nilai = [64, 34, 25, 12, 22, 11, 90]
print("=== SELECTION SORT ===")
hasil = selection_sort(nilai)
```

### Langkah 3: Insertion Sort dengan Visualisasi (10 menit)

Insertion Sort membangun array terurut satu elemen pada satu waktu, seperti menyusun kartu di tangan.

```python
def insertion_sort(data):
    """
    Mengurutkan data menggunakan Insertion Sort.
    Menampilkan proses setiap langkah penyisipan.
    """
    arr = data.copy()
    n = len(arr)
    total_pergeseran = 0
    total_perbandingan = 0

    print(f"Data awal: {arr}\n")

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        geser_count = 0

        while j >= 0 and arr[j] > key:
            total_perbandingan += 1
            arr[j + 1] = arr[j]
            j -= 1
            geser_count += 1
            total_pergeseran += 1

        if j >= 0:
            total_perbandingan += 1  # perbandingan terakhir yang gagal

        arr[j + 1] = key
        print(f"  Sisipkan {key:>2} di index [{j+1}] "
              f"(geser {geser_count} elemen) → {arr}")

    print(f"\nHasil   : {arr}")
    print(f"Total perbandingan: {total_perbandingan}")
    print(f"Total pergeseran  : {total_pergeseran}")
    return arr

# Uji coba
nilai = [64, 34, 25, 12, 22, 11, 90]
print("=== INSERTION SORT ===")
hasil = insertion_sort(nilai)
```

### Langkah 4: Perbandingan Ketiga Algoritma (10 menit)

Bandingkan waktu eksekusi dan jumlah operasi dari ketiga algoritma.

```python
import time
import random

def bubble_sort_count(data):
    """Bubble Sort — mengembalikan (hasil, perbandingan, swap)."""
    arr = data.copy()
    n = len(arr)
    perbandingan, swap = 0, 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            perbandingan += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap += 1
    return arr, perbandingan, swap

def selection_sort_count(data):
    """Selection Sort — mengembalikan (hasil, perbandingan, swap)."""
    arr = data.copy()
    n = len(arr)
    perbandingan, swap = 0, 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            perbandingan += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swap += 1
    return arr, perbandingan, swap

def insertion_sort_count(data):
    """Insertion Sort — mengembalikan (hasil, perbandingan, pergeseran)."""
    arr = data.copy()
    n = len(arr)
    perbandingan, pergeseran = 0, 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            perbandingan += 1
            arr[j + 1] = arr[j]
            j -= 1
            pergeseran += 1
        if j >= 0:
            perbandingan += 1
        arr[j + 1] = key
    return arr, perbandingan, pergeseran

# === PERBANDINGAN PERFORMA ===
ukuran_list = [100, 500, 1000, 3000]

print(f"{'Ukuran':<8} {'Bubble (dtk)':<14} {'Selection (dtk)':<17} {'Insertion (dtk)'}")
print("=" * 55)

for n in ukuran_list:
    data_acak = random.sample(range(n * 10), n)

    start = time.time()
    bubble_sort_count(data_acak)
    t_bubble = time.time() - start

    start = time.time()
    selection_sort_count(data_acak)
    t_selection = time.time() - start

    start = time.time()
    insertion_sort_count(data_acak)
    t_insertion = time.time() - start

    print(f"{n:<8} {t_bubble:<14.4f} {t_selection:<17.4f} {t_insertion:.4f}")

print("\n--- Perbandingan Jumlah Operasi (n=1000) ---")
data_1000 = random.sample(range(10000), 1000)
_, bp, bs = bubble_sort_count(data_1000)
_, sp, ss = selection_sort_count(data_1000)
_, ip, ig = insertion_sort_count(data_1000)
print(f"  Bubble Sort    : {bp:>10,} perbandingan, {bs:>10,} swap")
print(f"  Selection Sort : {sp:>10,} perbandingan, {ss:>10,} swap")
print(f"  Insertion Sort : {ip:>10,} perbandingan, {ig:>10,} pergeseran")
```

### Langkah 5: sorted() dan list.sort() bawaan Python (5 menit)

Python memiliki algoritma pengurutan bawaan (Timsort) yang sangat efisien.

```python
# === PENGURUTAN BAWAAN PYTHON ===
nama_kota = ["Surabaya", "Jakarta", "Bandung", "Yogyakarta", "Medan", "Semarang"]

# sorted() — mengembalikan list baru, data asli tidak berubah
kota_terurut = sorted(nama_kota)
print(f"Asli     : {nama_kota}")
print(f"sorted() : {kota_terurut}")

# list.sort() — mengurutkan di tempat (in-place), mengubah list asli
nama_kota.sort(reverse=True)
print(f"sort(rev): {nama_kota}")

# Custom key — urutkan berdasarkan panjang nama
kota_by_len = sorted(kota_terurut, key=len)
print(f"By length: {kota_by_len}")

# Perbandingan kecepatan: Timsort vs implementasi kita
import time
data_besar = random.sample(range(100_000), 10_000)

start = time.time()
_ = sorted(data_besar)
waktu_timsort = time.time() - start
print(f"\nTimsort (n=10000): {waktu_timsort:.6f} detik ← sangat cepat!")
```

### Langkah 6: Mini Project — Mengurutkan Data Mahasiswa (20 menit)

Bangun program untuk mengurutkan data mahasiswa berdasarkan berbagai kriteria.

```python
# === DATA MAHASISWA ===
mahasiswa = [
    {"nim": "2025042", "nama": "Farhan Rizki", "ipk": 3.81},
    {"nim": "2025001", "nama": "Ahmad Fauzi", "ipk": 3.75},
    {"nim": "2025078", "nama": "Indah Permata", "ipk": 3.95},
    {"nim": "2025015", "nama": "Citra Dewi", "ipk": 3.92},
    {"nim": "2025031", "nama": "Eka Prasetya", "ipk": 3.45},
    {"nim": "2025008", "nama": "Budi Santoso", "ipk": 3.50},
    {"nim": "2025089", "nama": "Joko Susanto", "ipk": 3.72},
    {"nim": "2025063", "nama": "Hadi Wijaya", "ipk": 3.33},
    {"nim": "2025055", "nama": "Gita Nuraini", "ipk": 3.60},
    {"nim": "2025023", "nama": "Diana Putri", "ipk": 3.68},
]

def tampilkan_tabel(daftar, judul="Daftar Mahasiswa"):
    """Menampilkan data mahasiswa dalam format tabel."""
    print(f"\n{'=' * 50}")
    print(f"  {judul}")
    print(f"{'=' * 50}")
    print(f"  {'No':<4} {'NIM':<10} {'Nama':<20} {'IPK':<6}")
    print(f"  {'-' * 44}")
    for i, mhs in enumerate(daftar, 1):
        print(f"  {i:<4} {mhs['nim']:<10} {mhs['nama']:<20} {mhs['ipk']:<6.2f}")
    print(f"{'=' * 50}")

def insertion_sort_mahasiswa(data, key_field, reverse=False):
    """
    Mengurutkan data mahasiswa menggunakan Insertion Sort.
    key_field: 'nim', 'nama', atau 'ipk'
    reverse: True untuk urutan menurun
    """
    arr = data.copy()
    n = len(arr)
    for i in range(1, n):
        key_item = arr[i]
        key_val = key_item[key_field]
        j = i - 1
        while j >= 0 and (
            (arr[j][key_field] > key_val) if not reverse
            else (arr[j][key_field] < key_val)
        ):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

# === PROGRAM UTAMA ===
print("SISTEM PENGURUTAN DATA MAHASISWA")
print("Informatika — Universitas Al Azhar Indonesia\n")

tampilkan_tabel(mahasiswa, "Data Awal (Belum Terurut)")

while True:
    print("\nUrutkan berdasarkan:")
    print("  1. NIM (ascending)")
    print("  2. Nama (A-Z)")
    print("  3. IPK (tertinggi ke terendah)")
    print("  4. IPK (terendah ke tertinggi)")
    print("  0. Keluar")

    pilihan = input("\nPilih: ").strip()

    if pilihan == '1':
        hasil = insertion_sort_mahasiswa(mahasiswa, "nim")
        tampilkan_tabel(hasil, "Diurutkan berdasarkan NIM")
    elif pilihan == '2':
        hasil = insertion_sort_mahasiswa(mahasiswa, "nama")
        tampilkan_tabel(hasil, "Diurutkan berdasarkan Nama (A-Z)")
    elif pilihan == '3':
        hasil = insertion_sort_mahasiswa(mahasiswa, "ipk", reverse=True)
        tampilkan_tabel(hasil, "Diurutkan berdasarkan IPK (Tertinggi)")
    elif pilihan == '4':
        hasil = insertion_sort_mahasiswa(mahasiswa, "ipk")
        tampilkan_tabel(hasil, "Diurutkan berdasarkan IPK (Terendah)")
    elif pilihan == '0':
        print("\nTerima kasih!")
        break
    else:
        print("  Pilihan tidak valid.")
```

---

## Tantangan Tambahan

1. **Visualisasi Bar Chart:** Buat fungsi yang menampilkan array sebagai bar chart ASCII di setiap langkah sorting (contoh: `[3,1,4]` menjadi `### # ####`).
2. **Cocktail Shaker Sort:** Implementasikan variasi Bubble Sort yang bergerak bolak-balik (bidirectional). Bandingkan dengan Bubble Sort biasa.
3. **Stabilitas:** Buktikan bahwa Insertion Sort bersifat *stable* (elemen dengan nilai sama tetap mempertahankan urutan asli) sementara Selection Sort tidak.

---

## Checklist Penyelesaian

- [ ] Mampu mengimplementasikan Bubble Sort dengan visualisasi per pass
- [ ] Mampu mengimplementasikan Selection Sort dengan visualisasi per pass
- [ ] Mampu mengimplementasikan Insertion Sort dengan visualisasi per langkah
- [ ] Berhasil membandingkan performa ketiga algoritma (waktu dan jumlah operasi)
- [ ] Memahami penggunaan `sorted()` dan `list.sort()` bawaan Python
- [ ] Menyelesaikan mini project Mengurutkan Data Mahasiswa
- [ ] Notebook disimpan dengan nama `Lab11_NIM_NamaLengkap.ipynb`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
