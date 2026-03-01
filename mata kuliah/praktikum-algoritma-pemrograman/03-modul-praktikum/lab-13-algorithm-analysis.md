# Lab 13: Analisis Algoritma

## Informasi Praktikum

| Komponen | Keterangan |
|----------|------------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Kode MK** | INF-101 |
| **Semester** | Genap 2025/2026 |
| **Praktikum** | Lab 13 — Analisis Algoritma |
| **Durasi** | 75 menit |
| **Prasyarat** | Lab 10 (Pencarian), Lab 11 (Pengurutan), Lab 12 (Rekursi), Modul Minggu 13 |
| **Platform** | Google Colab |
| **Pengajar** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. **Mengukur** waktu eksekusi kode Python menggunakan modul `time` secara konsisten dan akurat
2. **Memplot** kurva pertumbuhan waktu eksekusi terhadap ukuran input menggunakan `matplotlib`
3. **Mengidentifikasi** kompleksitas Big-O dari potongan kode yang diberikan
4. **Membangun** Algorithm Benchmark Tool yang membandingkan berbagai algoritma secara otomatis

---

## Persiapan

- Buka Google Colab di browser: [colab.research.google.com](https://colab.research.google.com)
- Buat notebook baru dengan nama: `Lab13_NIM_NamaLengkap.ipynb`
- Google Colab sudah menyediakan `matplotlib` secara bawaan — tidak perlu instalasi tambahan

---

## Langkah-langkah Praktikum

### Langkah 1: Mengukur Waktu Eksekusi (10 menit)

Pelajari cara mengukur waktu eksekusi dengan benar menggunakan `time.perf_counter()`.

```python
import time

def ukur_waktu(fungsi, *args, ulang=5):
    """
    Mengukur waktu rata-rata eksekusi sebuah fungsi.
    Menjalankan fungsi beberapa kali untuk hasil yang konsisten.
    """
    waktu_list = []
    for _ in range(ulang):
        start = time.perf_counter()
        hasil = fungsi(*args)
        elapsed = time.perf_counter() - start
        waktu_list.append(elapsed)
    rata_rata = sum(waktu_list) / len(waktu_list)
    return rata_rata, hasil

# Contoh: mengukur waktu penjumlahan
def jumlah_loop(n):
    """Menghitung 1 + 2 + ... + n menggunakan loop — O(n)."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def jumlah_rumus(n):
    """Menghitung 1 + 2 + ... + n menggunakan rumus Gauss — O(1)."""
    return n * (n + 1) // 2

# Perbandingan
print("=== PENGUKURAN WAKTU ===\n")
print(f"{'n':<12} {'Loop O(n)':<18} {'Rumus O(1)':<18} {'Rasio'}")
print("-" * 55)

for n in [1_000, 10_000, 100_000, 1_000_000, 10_000_000]:
    t_loop, _ = ukur_waktu(jumlah_loop, n)
    t_rumus, _ = ukur_waktu(jumlah_rumus, n)
    rasio = t_loop / t_rumus if t_rumus > 0 else float('inf')
    print(f"{n:<12,} {t_loop:<18.6f} {t_rumus:<18.8f} {rasio:,.0f}x")

print("\nO(1) tetap konstan, O(n) bertumbuh linear seiring ukuran input.")
```

### Langkah 2: Memplot Kurva Pertumbuhan (15 menit)

Visualisasikan bagaimana waktu eksekusi bertumbuh seiring ukuran input.

```python
import time
import matplotlib.pyplot as plt

# === ALGORITMA YANG AKAN DIBANDINGKAN ===
def cari_linear(data, target):
    for item in data:
        if item == target:
            return True
    return False

def cari_binary(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def cek_duplikat_n2(data):
    """Mengecek apakah ada duplikat — O(n^2)."""
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                return True
    return False

def cek_duplikat_n(data):
    """Mengecek apakah ada duplikat — O(n) dengan set."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False

# === PENGUKURAN DAN PLOTTING ===
ukuran = [100, 500, 1000, 2000, 3000, 5000]
waktu_linear = []
waktu_binary = []
waktu_n2 = []
waktu_n = []

for n in ukuran:
    data = list(range(n))
    target = n + 1  # target tidak ada — worst case

    # Linear Search
    start = time.perf_counter()
    for _ in range(10):
        cari_linear(data, target)
    waktu_linear.append((time.perf_counter() - start) / 10)

    # Binary Search
    start = time.perf_counter()
    for _ in range(10):
        cari_binary(data, target)
    waktu_binary.append((time.perf_counter() - start) / 10)

    # Cek duplikat O(n^2)
    start = time.perf_counter()
    cek_duplikat_n2(data)
    waktu_n2.append(time.perf_counter() - start)

    # Cek duplikat O(n)
    start = time.perf_counter()
    cek_duplikat_n(data)
    waktu_n.append(time.perf_counter() - start)

# Plot grafik
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Grafik 1: Pencarian
axes[0].plot(ukuran, waktu_linear, 'o-', label='Linear Search — O(n)', color='red')
axes[0].plot(ukuran, waktu_binary, 's-', label='Binary Search — O(log n)', color='green')
axes[0].set_xlabel('Ukuran Data (n)')
axes[0].set_ylabel('Waktu (detik)')
axes[0].set_title('Perbandingan Algoritma Pencarian')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Grafik 2: Cek Duplikat
axes[1].plot(ukuran, waktu_n2, 'o-', label='Nested Loop — O(n²)', color='red')
axes[1].plot(ukuran, waktu_n, 's-', label='Dengan Set — O(n)', color='green')
axes[1].set_xlabel('Ukuran Data (n)')
axes[1].set_ylabel('Waktu (detik)')
axes[1].set_title('Perbandingan Cek Duplikat')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('perbandingan_algoritma.png', dpi=100, bbox_inches='tight')
plt.show()
print("Grafik disimpan sebagai 'perbandingan_algoritma.png'")
```

### Langkah 3: Identifikasi Big-O dari Kode (15 menit)

Analisis kompleksitas waktu dari potongan kode berikut. Tentukan Big-O masing-masing.

```python
# === LATIHAN: Tentukan Big-O setiap fungsi ===

# Fungsi A
def fungsi_a(n):
    total = 0
    for i in range(n):
        total += i
    return total
# Big-O: ??? (isi jawabanmu)

# Fungsi B
def fungsi_b(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total
# Big-O: ??? (isi jawabanmu)

# Fungsi C
def fungsi_c(data):
    return data[0] + data[-1]
# Big-O: ??? (isi jawabanmu)

# Fungsi D
def fungsi_d(n):
    if n <= 1:
        return 1
    return n + fungsi_d(n // 2)
# Big-O: ??? (isi jawabanmu)

# Fungsi E
def fungsi_e(n):
    total = 0
    for i in range(n):
        for j in range(i):
            total += 1
    return total
# Big-O: ??? (isi jawabanmu)

# === VERIFIKASI DENGAN PENGUKURAN ===
print("=== VERIFIKASI BIG-O ===\n")
print(f"{'n':<10} {'A':<14} {'B':<14} {'C':<14} {'D':<14} {'E':<14}")
print("-" * 70)

for n in [100, 500, 1000, 2000, 5000]:
    data = list(range(n))
    ta, _ = ukur_waktu(fungsi_a, n, ulang=3)
    tb, _ = ukur_waktu(fungsi_b, n, ulang=3) if n <= 2000 else (float('nan'), 0)
    tc, _ = ukur_waktu(fungsi_c, data, ulang=3)
    td, _ = ukur_waktu(fungsi_d, n, ulang=3)
    te, _ = ukur_waktu(fungsi_e, n, ulang=3) if n <= 5000 else (float('nan'), 0)
    print(f"{n:<10} {ta:<14.6f} {tb:<14.6f} {tc:<14.8f} {td:<14.8f} {te:<14.6f}")

# Jawaban
print("\n=== JAWABAN ===")
print("Fungsi A: O(n)      — satu loop dari 0 sampai n")
print("Fungsi B: O(n²)     — dua nested loop, masing-masing n iterasi")
print("Fungsi C: O(1)      — akses langsung ke index, tidak tergantung ukuran data")
print("Fungsi D: O(log n)  — n dibagi 2 setiap pemanggilan rekursif")
print("Fungsi E: O(n²)     — loop dalam: 0+1+2+...+(n-1) = n(n-1)/2")
```

### Langkah 4: Optimasi — Dari O(n^2) ke O(n) (10 menit)

Latihan mengoptimalkan kode yang lambat menggunakan struktur data yang tepat.

```python
import time
import random

# === SOAL 1: Cari elemen yang muncul di kedua list ===

# Versi lambat — O(n^2)
def irisan_lambat(list_a, list_b):
    hasil = []
    for item in list_a:
        for item_b in list_b:
            if item == item_b and item not in hasil:
                hasil.append(item)
    return hasil

# Versi cepat — O(n) menggunakan set
def irisan_cepat(list_a, list_b):
    return list(set(list_a) & set(list_b))

# === SOAL 2: Cari pasangan yang berjumlah target ===

# Versi lambat — O(n^2)
def cari_pasangan_lambat(data, target):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == target:
                return (data[i], data[j])
    return None

# Versi cepat — O(n) menggunakan set
def cari_pasangan_cepat(data, target):
    sudah_dilihat = set()
    for angka in data:
        komplemen = target - angka
        if komplemen in sudah_dilihat:
            return (komplemen, angka)
        sudah_dilihat.add(angka)
    return None

# === PERBANDINGAN ===
n = 5000
list_a = random.sample(range(n * 10), n)
list_b = random.sample(range(n * 10), n)
data = random.sample(range(n * 10), n)
target = data[100] + data[200]

print("=== OPTIMASI O(n²) → O(n) ===\n")

# Irisan
start = time.perf_counter()
r1 = irisan_lambat(list_a, list_b)
t1 = time.perf_counter() - start

start = time.perf_counter()
r2 = irisan_cepat(list_a, list_b)
t2 = time.perf_counter() - start

print(f"Irisan dua list (n={n}):")
print(f"  O(n²) : {t1:.4f} detik — ditemukan {len(r1)} elemen")
print(f"  O(n)  : {t2:.6f} detik — ditemukan {len(r2)} elemen")
print(f"  Speedup: {t1/t2:,.0f}x lebih cepat\n")

# Cari pasangan
start = time.perf_counter()
p1 = cari_pasangan_lambat(data, target)
t1 = time.perf_counter() - start

start = time.perf_counter()
p2 = cari_pasangan_cepat(data, target)
t2 = time.perf_counter() - start

print(f"Cari pasangan berjumlah {target} (n={n}):")
print(f"  O(n²) : {t1:.6f} detik — {p1}")
print(f"  O(n)  : {t2:.6f} detik — {p2}")
print(f"  Speedup: {t1/t2:,.0f}x lebih cepat")
```

### Langkah 5: Mini Project — Algorithm Benchmark Tool (15 menit)

Bangun tool otomatis untuk membandingkan berbagai algoritma pencarian dan pengurutan.

```python
import time
import random

# === ALGORITMA PENCARIAN ===
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

def binary_search(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# === ALGORITMA PENGURUTAN ===
def bubble_sort(data):
    arr = data.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(data):
    arr = data.copy()
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(data):
    arr = data.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def python_sorted(data):
    return sorted(data)

# === BENCHMARK TOOL ===
def benchmark_pencarian(ukuran_list):
    """Benchmark otomatis untuk algoritma pencarian."""
    print("\n" + "=" * 65)
    print("  BENCHMARK ALGORITMA PENCARIAN")
    print("=" * 65)
    print(f"  {'Ukuran':<10} {'Linear (dtk)':<16} {'Binary (dtk)':<16} {'Rasio'}")
    print("  " + "-" * 55)

    for n in ukuran_list:
        data = list(range(n))
        target = n - 1  # worst case

        start = time.perf_counter()
        for _ in range(10):
            linear_search(data, target)
        t_linear = (time.perf_counter() - start) / 10

        start = time.perf_counter()
        for _ in range(10):
            binary_search(data, target)
        t_binary = (time.perf_counter() - start) / 10

        rasio = t_linear / t_binary if t_binary > 0 else float('inf')
        print(f"  {n:<10,} {t_linear:<16.6f} {t_binary:<16.8f} {rasio:>8,.0f}x")

def benchmark_pengurutan(ukuran_list):
    """Benchmark otomatis untuk algoritma pengurutan."""
    print("\n" + "=" * 75)
    print("  BENCHMARK ALGORITMA PENGURUTAN")
    print("=" * 75)
    print(f"  {'Ukuran':<8} {'Bubble':<12} {'Selection':<12} {'Insertion':<12} {'sorted()':<12}")
    print("  " + "-" * 55)

    for n in ukuran_list:
        data = random.sample(range(n * 10), n)

        start = time.perf_counter()
        bubble_sort(data)
        t_bubble = time.perf_counter() - start

        start = time.perf_counter()
        selection_sort(data)
        t_selection = time.perf_counter() - start

        start = time.perf_counter()
        insertion_sort(data)
        t_insertion = time.perf_counter() - start

        start = time.perf_counter()
        python_sorted(data)
        t_sorted = time.perf_counter() - start

        print(f"  {n:<8} {t_bubble:<12.4f} {t_selection:<12.4f} "
              f"{t_insertion:<12.4f} {t_sorted:<12.6f}")

    print("\n  Catatan: sorted() menggunakan Timsort — O(n log n)")
    print("  Bubble, Selection, Insertion — O(n²)")

# === JALANKAN BENCHMARK ===
print("ALGORITHM BENCHMARK TOOL")
print("Algoritma dan Pemrograman — Universitas Al Azhar Indonesia")

benchmark_pencarian([1_000, 10_000, 100_000, 500_000])
benchmark_pengurutan([500, 1000, 2000, 3000])

print("\n" + "=" * 65)
print("  Benchmark selesai!")
print("=" * 65)
```

---

## Tantangan Tambahan

1. **Benchmark Custom:** Tambahkan algoritma lain ke benchmark tool (misalnya: Merge Sort atau Quick Sort dari pustaka) dan bandingkan hasilnya.
2. **Best/Worst/Average Case:** Modifikasi benchmark untuk menguji setiap algoritma pada 3 kasus: data sudah terurut (best), data terurut terbalik (worst), dan data acak (average).
3. **Memory Profiling:** Gunakan `sys.getsizeof()` untuk membandingkan penggunaan memori antara list, set, dan dictionary pada ukuran data yang sama.

---

## Checklist Penyelesaian

- [ ] Mampu mengukur waktu eksekusi menggunakan `time.perf_counter()` dengan pengulangan
- [ ] Berhasil memplot kurva pertumbuhan waktu eksekusi menggunakan `matplotlib`
- [ ] Mampu mengidentifikasi Big-O dari potongan kode (5 latihan)
- [ ] Berhasil mengoptimalkan kode O(n^2) menjadi O(n) menggunakan set/dict
- [ ] Menyelesaikan mini project Algorithm Benchmark Tool
- [ ] Notebook disimpan dengan nama `Lab13_NIM_NamaLengkap.ipynb`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
