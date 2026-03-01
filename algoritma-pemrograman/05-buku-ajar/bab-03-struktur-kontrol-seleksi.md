# BAB 3: STRUKTUR KONTROL: SELEKSI

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman --- Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|:------------:|
| CPMK-3.1 | Menjelaskan konsep percabangan dalam algoritma | C2 --- Memahami |
| CPMK-3.2 | Menerapkan statement `if`, `if-else`, dan `if-elif-else` | C3 --- Menerapkan |
| CPMK-3.3 | Menggunakan operator logika dalam kondisi majemuk | C3 --- Menerapkan |
| CPMK-3.4 | Menerapkan nested if dan conditional expression | C3 --- Menerapkan |

**Prasyarat:** Mahasiswa telah memahami materi Bab 2 (Variabel, Tipe Data, dan Operator), khususnya operator perbandingan (`==`, `!=`, `>`, `<`, `>=`, `<=`) dan tipe data `bool`.

**Durasi:** 2 pertemuan (masing-masing 2x50 menit)

---

## 3.1 Konsep Percabangan

### 3.1.1 Mengapa Perlu Percabangan?

Bayangkan Anda berjalan menuju kampus di pagi hari. Anda melihat langit dan berpikir:

> *"Jika mendung, saya bawa payung. Jika cerah, saya pakai topi."*

Tanpa disadari, Anda baru saja menjalankan sebuah **algoritma percabangan** --- mengambil keputusan berdasarkan suatu kondisi. Dalam kehidupan sehari-hari, kita terus-menerus membuat keputusan seperti ini:

- **Jika** saldo e-money cukup, **maka** tap in di gerbang TransJakarta. **Jika tidak**, isi ulang dulu.
- **Jika** IPK >= 3.5, **maka** eligible untuk beasiswa. **Jika tidak**, coba semester depan.
- **Jika** total belanja di minimarket >= Rp100.000, **maka** dapat diskon 10%.
- **Jika** umur >= 17 tahun, **maka** boleh membuat KTP.
- **Jika** hari ini Sabtu atau Minggu, **maka** kampus libur.

Dalam pemrograman, **percabangan** (*branching* atau *selection*) memungkinkan program untuk mengambil jalur eksekusi yang berbeda berdasarkan kondisi tertentu. Tanpa percabangan, program hanya bisa berjalan secara sekuensial --- baris demi baris dari atas ke bawah --- tanpa kemampuan untuk membuat keputusan.

**[R] Refleksi:** Coba pikirkan 5 keputusan yang Anda buat hari ini yang melibatkan kondisi "jika ... maka ...". Tuliskan dalam bentuk kalimat percabangan.

### 3.1.2 Flowchart Percabangan

Dalam flowchart, percabangan digambarkan menggunakan simbol **belah ketupat** (*diamond*) yang merepresentasikan sebuah **kondisi** yang dievaluasi menjadi `True` atau `False`.

```
Flowchart Percabangan Sederhana:
Contoh: Apakah mahasiswa lulus?

            ┌─────────────┐
            │   MULAI     │
            └──────┬──────┘
                   │
                   v
          ┌────────────────┐
          │ Input: nilai   │
          └───────┬────────┘
                  │
                  v
           ╱            ╲
          ╱   nilai      ╲
         ╱    >= 60?      ╲
         ╲               ╱
          ╲             ╱
           ╲           ╱
        Ya  │         │  Tidak
            v         v
   ┌────────────┐  ┌──────────────┐
   │ Cetak:     │  │ Cetak:       │
   │ "Lulus"    │  │ "Tidak Lulus"│
   └─────┬──────┘  └──────┬───────┘
         │                │
         └───────┬────────┘
                 │
                 v
          ┌─────────────┐
          │   SELESAI   │
          └─────────────┘
```

Perhatikan:
- Simbol **belah ketupat** berisi kondisi/pertanyaan yang hasilnya `True` (Ya) atau `False` (Tidak).
- Terdapat **dua jalur** yang keluar dari simbol belah ketupat.
- Kedua jalur pada akhirnya **bertemu kembali** untuk melanjutkan program.

### 3.1.3 Tiga Struktur Kontrol Fundamental

Menurut **Teorema Bohm-Jacopini** (1966), setiap algoritma dapat ditulis menggunakan tiga struktur kontrol fundamental:

| No. | Struktur | Penjelasan | Keyword Python |
|:---:|----------|------------|----------------|
| 1 | **Sekuensial** | Eksekusi baris per baris dari atas ke bawah | (default) |
| 2 | **Seleksi** | Memilih jalur eksekusi berdasarkan kondisi | `if`, `elif`, `else` |
| 3 | **Perulangan** | Mengulang blok kode selama kondisi terpenuhi | `for`, `while` (Bab 4) |

Bab ini fokus pada struktur kontrol **seleksi**. Perulangan akan dibahas di Bab 4.

---

## 3.2 Statement `if`

### 3.2.1 Sintaks Dasar

Statement `if` adalah bentuk percabangan paling sederhana. Blok kode di dalamnya hanya dijalankan **jika kondisi bernilai `True`**.

```python
if kondisi:
    # blok kode yang dijalankan jika kondisi True
    # perhatikan indentasi (4 spasi)
    # boleh lebih dari satu baris
```

**Hal penting yang perlu diperhatikan:**

1. **Tanda titik dua (`:`)** --- Wajib ada di akhir baris `if`. Lupa menuliskan titik dua adalah salah satu kesalahan paling umum bagi pemula.
2. **Indentasi** --- Python menggunakan **indentasi** (4 spasi) untuk menentukan blok kode, BUKAN kurung kurawal `{}` seperti bahasa C atau Java. Semua baris yang terindentasi di bawah `if` termasuk dalam blok `if`.
3. **Kondisi** --- Ekspresi yang menghasilkan nilai `True` atau `False` (tipe `bool`).

```
Visualisasi Alur Eksekusi if:

    Kode sebelum if
            │
            v
     ╱             ╲
    ╱  kondisi       ╲
    ╲  True?         ╱
     ╲             ╱
      True │    │ False
           v    │
    ┌────────────┐  │
    │ Blok if    │  │
    └─────┬──────┘  │
          │         │
          └────┬────┘
               │
               v
    Kode setelah if
```

### 3.2.2 Contoh-contoh

**Contoh 1: Cek Kelulusan Mahasiswa**

```python
# Cek kelulusan berdasarkan nilai
nilai = int(input("Masukkan nilai akhir: "))

if nilai >= 60:
    print("Selamat! Anda lulus mata kuliah ini.")
    print("Silakan mengambil sertifikat di bagian akademik.")

print("Terima kasih telah mengikuti ujian.")  # Baris ini SELALU dijalankan
```

Perhatikan bahwa baris terakhir (`print("Terima kasih...")`) **tidak terindentasi** di dalam blok `if`, sehingga akan **selalu dijalankan** tanpa memandang nilai kondisi.

**Contoh uji coba:**
| Input | Kondisi `nilai >= 60` | Output |
|:-----:|:---------------------:|--------|
| 85 | `True` | "Selamat! Anda lulus..." + "Silakan mengambil..." + "Terima kasih..." |
| 50 | `False` | "Terima kasih..." |

**Contoh 2: Diskon Belanja di Minimarket**

```python
# Program diskon belanja
total_belanja = float(input("Total belanja: Rp"))

if total_belanja >= 100000:
    diskon = total_belanja * 0.1
    total_bayar = total_belanja - diskon
    print(f"Anda mendapat diskon 10%!")
    print(f"Diskon      : Rp{diskon:,.0f}")
    print(f"Total bayar : Rp{total_bayar:,.0f}")

print(f"Total belanja awal: Rp{total_belanja:,.0f}")
```

**Contoh 3: Peringatan Suhu Tinggi**

```python
# Monitoring suhu ruangan server
suhu = float(input("Masukkan suhu ruangan (Celsius): "))

if suhu > 30:
    print("[PERINGATAN] Suhu ruangan terlalu tinggi!")
    print("Segera cek sistem pendingin.")
    print(f"Suhu saat ini: {suhu}°C (batas normal: 30°C)")
```

**[T] Tips:** Biasakan memberikan informasi yang jelas dalam pesan output. Alih-alih hanya mencetak "Error", berikan konteks: apa yang salah, apa batas normalnya, dan apa yang harus dilakukan.

---

## 3.3 Statement `if-else`

### 3.3.1 Sintaks

Statement `if-else` menyediakan **dua jalur alternatif**: satu untuk kondisi `True`, satu lagi untuk kondisi `False`.

```python
if kondisi:
    # blok kode jika kondisi True
else:
    # blok kode jika kondisi False
```

```
Visualisasi Alur Eksekusi if-else:

    Kode sebelum if
            │
            v
     ╱             ╲
    ╱  kondisi       ╲
    ╲  True?         ╱
     ╲             ╱
   True │       │ False
        v       v
 ┌──────────┐ ┌──────────┐
 │ Blok if  │ │ Blok     │
 │          │ │ else     │
 └────┬─────┘ └────┬─────┘
      │             │
      └──────┬──────┘
             │
             v
    Kode setelah if-else
```

### 3.3.2 Contoh-contoh

**Contoh 1: Cek Ganjil atau Genap**

```python
# Cek bilangan ganjil atau genap
bilangan = int(input("Masukkan sebuah bilangan bulat: "))

if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan GENAP")
else:
    print(f"{bilangan} adalah bilangan GANJIL")
```

**Penjelasan:** Operator modulo (`%`) menghasilkan sisa pembagian. Jika `bilangan % 2 == 0`, maka bilangan tersebut habis dibagi 2 (genap).

**Contoh 2: Tarif Parkir**

```python
# Sistem tarif parkir
jenis_kendaraan = input("Jenis kendaraan (motor/mobil): ").lower()

if jenis_kendaraan == "motor":
    tarif = 2000
    print(f"Tarif parkir motor: Rp{tarif:,}")
else:
    tarif = 5000
    print(f"Tarif parkir mobil: Rp{tarif:,}")

print(f"Silakan ambil karcis Anda.")
```

**Contoh 3: Syarat Membuat KTP (Voter Eligibility)**

```python
# Cek apakah warga bisa membuat KTP
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))

if umur >= 17:
    print(f"Halo {nama}! Anda BERHAK membuat KTP.")
    print("Silakan datang ke kantor kelurahan dengan membawa:")
    print("1. Surat pengantar RT/RW")
    print("2. Kartu Keluarga")
    print("3. Akta kelahiran")
else:
    selisih = 17 - umur
    print(f"Maaf {nama}, Anda BELUM berhak membuat KTP.")
    print(f"Anda perlu menunggu {selisih} tahun lagi.")
```

**Contoh 4: Cek Tahun Kabisat (Sederhana)**

```python
# Cek tahun kabisat (versi sederhana)
tahun = int(input("Masukkan tahun: "))

if tahun % 4 == 0:
    print(f"Tahun {tahun} adalah tahun kabisat.")
else:
    print(f"Tahun {tahun} bukan tahun kabisat.")
```

**[!] Peringatan:** Versi di atas adalah penyederhanaan. Aturan tahun kabisat yang lengkap lebih kompleks dan akan dibahas di bagian latihan soal (harus habis dibagi 4, kecuali habis dibagi 100, kecuali habis dibagi 400).

---

## 3.4 Statement `if-elif-else`

### 3.4.1 Sintaks

Ketika terdapat **lebih dari dua kemungkinan** jalur, kita menggunakan `if-elif-else`. Kata `elif` adalah kependekan dari *else if*.

```python
if kondisi_1:
    # blok kode jika kondisi_1 True
elif kondisi_2:
    # blok kode jika kondisi_2 True
elif kondisi_3:
    # blok kode jika kondisi_3 True
else:
    # blok kode jika SEMUA kondisi di atas False (default)
```

**Cara kerja:**
1. Python mengevaluasi `kondisi_1` terlebih dahulu.
2. Jika `True`, jalankan blok kode pertama, lalu **lewati seluruh blok `elif` dan `else`**.
3. Jika `False`, lanjut evaluasi `kondisi_2`.
4. Proses berlanjut hingga ditemukan kondisi yang `True`, atau hingga mencapai `else`.
5. Blok `else` bersifat **opsional** tetapi **sangat disarankan** sebagai penanganan kasus default.

```
Visualisasi Alur if-elif-else:

     ╱             ╲
    ╱  kondisi_1     ╲──True──> Blok 1
    ╲                ╱
     ╲              ╱
         │ False
         v
     ╱             ╲
    ╱  kondisi_2     ╲──True──> Blok 2
    ╲                ╱
     ╲              ╱
         │ False
         v
     ╱             ╲
    ╱  kondisi_3     ╲──True──> Blok 3
    ╲                ╱
     ╲              ╱
         │ False
         v
      Blok else
```

### 3.4.2 Contoh Lengkap: Konversi Nilai ke Huruf (Sistem Penilaian UAI)

```python
# ============================================
# Sistem Konversi Nilai - Universitas Al Azhar Indonesia
# ============================================

nilai = float(input("Masukkan nilai akhir (0-100): "))

# Validasi input
if nilai < 0 or nilai > 100:
    print("Error: Nilai harus antara 0-100!")
else:
    # Konversi nilai angka ke huruf berdasarkan pedoman UAI
    if nilai >= 85:
        huruf = "A"
        angka = 4.0
        keterangan = "Sangat Baik"
    elif nilai >= 80:
        huruf = "A-"
        angka = 3.7
        keterangan = "Sangat Baik"
    elif nilai >= 75:
        huruf = "B+"
        angka = 3.3
        keterangan = "Baik"
    elif nilai >= 70:
        huruf = "B"
        angka = 3.0
        keterangan = "Baik"
    elif nilai >= 65:
        huruf = "B-"
        angka = 2.7
        keterangan = "Cukup Baik"
    elif nilai >= 60:
        huruf = "C+"
        angka = 2.3
        keterangan = "Cukup"
    elif nilai >= 55:
        huruf = "C"
        angka = 2.0
        keterangan = "Cukup"
    elif nilai >= 40:
        huruf = "D"
        angka = 1.0
        keterangan = "Kurang"
    else:
        huruf = "E"
        angka = 0.0
        keterangan = "Sangat Kurang"

    # Tampilkan hasil
    print("\n" + "=" * 40)
    print("      HASIL KONVERSI NILAI")
    print("=" * 40)
    print(f"  Nilai Angka  : {nilai}")
    print(f"  Nilai Huruf  : {huruf}")
    print(f"  Bobot        : {angka}")
    print(f"  Keterangan   : {keterangan}")
    print("=" * 40)

    # Tentukan status kelulusan
    if angka >= 2.0:
        print("  Status       : LULUS")
    else:
        print("  Status       : TIDAK LULUS")
    print("=" * 40)
```

**[!] Peringatan:** Perhatikan bahwa urutan kondisi **sangat penting** dalam `if-elif-else`. Karena Python mengevaluasi dari atas ke bawah dan berhenti pada kondisi pertama yang `True`, kita harus menyusun kondisi dari nilai **tertinggi ke terendah**. Jika kita menulis `if nilai >= 40` di awal, maka nilai 90 juga akan masuk ke blok tersebut!

### 3.4.3 Contoh: Tarif TransJakarta

```python
# ============================================
# Sistem Tarif TransJakarta
# ============================================

print("=== SISTEM TARIF TRANSJAKARTA ===")
print()

# Input jenis penumpang
print("Jenis kartu:")
print("1. Kartu Reguler")
print("2. Kartu Pelajar/Mahasiswa")
print("3. Kartu Lansia/Disabilitas")
print("4. Tanpa Kartu (Single Trip)")

pilihan = int(input("\nPilih jenis kartu (1-4): "))

# Input jarak
jarak = input("Jarak perjalanan (dekat/jauh): ").lower()

# Tentukan tarif berdasarkan jenis kartu dan jarak
if pilihan == 1:
    jenis = "Reguler"
    if jarak == "jauh":
        tarif = 3500
    else:
        tarif = 3500  # TransJakarta tarif flat
elif pilihan == 2:
    jenis = "Pelajar/Mahasiswa"
    tarif = 2000  # subsidi pelajar
elif pilihan == 3:
    jenis = "Lansia/Disabilitas"
    tarif = 0  # gratis untuk lansia dan disabilitas
elif pilihan == 4:
    jenis = "Single Trip"
    tarif = 5000  # lebih mahal karena tanpa kartu
else:
    jenis = "Tidak Dikenal"
    tarif = -1

# Tampilkan hasil
print("\n" + "-" * 35)
if tarif >= 0:
    print(f"  Jenis Kartu : {jenis}")
    print(f"  Tarif       : Rp{tarif:,}")
    if tarif == 0:
        print("  (Gratis untuk lansia/disabilitas)")
    print("-" * 35)
    print("  Selamat menikmati perjalanan!")
else:
    print("  Pilihan tidak valid!")
print("-" * 35)
```

### 3.4.4 Contoh: Kategori Usia

```python
# Kategorisasi berdasarkan usia
umur = int(input("Masukkan usia Anda: "))

if umur < 0:
    print("Error: Usia tidak boleh negatif!")
elif umur <= 2:
    kategori = "Bayi"
elif umur <= 5:
    kategori = "Balita"
elif umur <= 12:
    kategori = "Anak-anak"
elif umur <= 17:
    kategori = "Remaja"
elif umur <= 59:
    kategori = "Dewasa"
elif umur <= 120:
    kategori = "Lansia"
else:
    print("Error: Usia tidak realistis!")
    kategori = None

if umur >= 0 and umur <= 120:
    print(f"Usia {umur} tahun termasuk kategori: {kategori}")
```

---

## 3.5 Kondisi Majemuk (Compound Conditions)

Seringkali, keputusan tidak hanya bergantung pada satu kondisi saja, melainkan **kombinasi beberapa kondisi**. Python menyediakan tiga operator logika untuk menggabungkan kondisi: `and`, `or`, dan `not`.

### 3.5.1 Operator `and`

Operator `and` menghasilkan `True` **hanya jika kedua kondisi** bernilai `True`.

```python
# Syarat beasiswa: IPK >= 3.0 DAN penghasilan ortu <= 5 juta
ipk = float(input("Masukkan IPK Anda: "))
penghasilan_ortu = float(input("Penghasilan orang tua per bulan: Rp"))

if ipk >= 3.0 and penghasilan_ortu <= 5000000:
    print("Selamat! Anda ELIGIBLE untuk mendaftar beasiswa.")
    print("Silakan lengkapi berkas pendaftaran di BAK.")
else:
    print("Maaf, Anda belum memenuhi syarat beasiswa.")
    if ipk < 3.0:
        print(f"  - IPK Anda ({ipk}) belum memenuhi minimum (3.0)")
    if penghasilan_ortu > 5000000:
        print(f"  - Penghasilan ortu (Rp{penghasilan_ortu:,.0f}) melebihi batas")
```

### 3.5.2 Operator `or`

Operator `or` menghasilkan `True` **jika setidaknya salah satu kondisi** bernilai `True`.

```python
# Cek hari libur kampus
hari = input("Masukkan nama hari: ").capitalize()

if hari == "Sabtu" or hari == "Minggu":
    print(f"{hari} adalah hari libur. Kampus tutup.")
    print("Silakan datang kembali di hari kerja (Senin-Jumat).")
else:
    print(f"{hari} adalah hari kerja. Kampus buka pukul 07.00-17.00 WIB.")
```

```python
# Syarat masuk wahana permainan
tinggi = int(input("Tinggi badan (cm): "))
umur = int(input("Umur: "))

if tinggi < 120 or umur < 8:
    print("Maaf, Anda belum memenuhi syarat untuk wahana ini.")
    print("Syarat: Tinggi minimal 120 cm DAN umur minimal 8 tahun.")
else:
    print("Silakan masuk dan nikmati wahana!")
```

### 3.5.3 Operator `not`

Operator `not` membalikkan (*negate*) nilai boolean: `True` menjadi `False`, dan sebaliknya.

```python
# Cek status registrasi
is_terdaftar = True  # Misalnya dari database

if not is_terdaftar:
    print("Anda belum terdaftar. Silakan registrasi terlebih dahulu.")
    print("Kunjungi: https://siakad.uai.ac.id/registrasi")
else:
    print("Selamat datang kembali!")
```

```python
# Validasi input: bukan string kosong
nama = input("Masukkan nama Anda: ")

if not nama:
    print("Error: Nama tidak boleh kosong!")
else:
    print(f"Halo, {nama}! Selamat datang.")
```

**[T] Tips:** Dalam Python, string kosong `""`, angka `0`, `None`, dan koleksi kosong (`[]`, `{}`) dianggap sebagai **falsy** (bernilai `False` jika dievaluasi sebagai boolean). Sebaliknya, string berisi karakter, angka selain nol, dan koleksi berisi elemen dianggap **truthy** (bernilai `True`).

### 3.5.4 Truth Table (Tabel Kebenaran)

Tabel kebenaran menunjukkan hasil dari setiap kombinasi nilai input untuk operator logika.

**Tabel Kebenaran `and`:**

| A | B | A `and` B |
|:---:|:---:|:---:|
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

**Tabel Kebenaran `or`:**

| A | B | A `or` B |
|:---:|:---:|:---:|
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

**Tabel Kebenaran `not`:**

| A | `not` A |
|:---:|:---:|
| `True` | `False` |
| `False` | `True` |

**Contoh Kombinasi Operator Logika:**

```python
# Menggabungkan and, or, dan not
umur = 20
memiliki_sim = True
memiliki_kendaraan = False

# Boleh mengemudi jika: umur >= 17 DAN punya SIM DAN punya kendaraan
if umur >= 17 and memiliki_sim and memiliki_kendaraan:
    print("Anda boleh mengemudi.")
elif umur >= 17 and memiliki_sim and not memiliki_kendaraan:
    print("Anda boleh mengemudi, tetapi perlu kendaraan.")
elif umur >= 17 and not memiliki_sim:
    print("Anda perlu membuat SIM terlebih dahulu.")
else:
    print("Anda belum cukup umur untuk mengemudi.")
```

### 3.5.5 Prioritas Operator (Precedence)

Ketika menggabungkan beberapa operator logika, Python mengikuti urutan prioritas berikut (dari yang tertinggi ke terendah):

| Prioritas | Operator | Contoh |
|:---------:|----------|--------|
| 1 (tertinggi) | `not` | `not True` -> `False` |
| 2 | `and` | `True and False` -> `False` |
| 3 (terendah) | `or` | `False or True` -> `True` |

**[T] Tips:** Gunakan **tanda kurung `()`** untuk memperjelas urutan evaluasi dan meningkatkan keterbacaan kode, meskipun secara teknis tidak diperlukan.

```python
# Tanpa kurung --- bisa membingungkan
if umur >= 17 and memiliki_sim or is_sopir_darurat:
    print("Boleh mengemudi")

# Dengan kurung --- lebih jelas maksudnya
if (umur >= 17 and memiliki_sim) or is_sopir_darurat:
    print("Boleh mengemudi")
```

### 3.5.6 Short-Circuit Evaluation

Python menggunakan **evaluasi hubung singkat** (*short-circuit evaluation*) saat mengevaluasi operator logika:

- **`and`:** Jika operand pertama bernilai `False`, Python **tidak akan mengevaluasi** operand kedua (karena hasilnya pasti `False`).
- **`or`:** Jika operand pertama bernilai `True`, Python **tidak akan mengevaluasi** operand kedua (karena hasilnya pasti `True`).

```python
# Demonstrasi short-circuit evaluation

# Contoh 1: and --- operand kedua tidak dievaluasi jika pertama False
x = 0
if x != 0 and 10 / x > 2:  # 10/x TIDAK dievaluasi karena x != 0 sudah False
    print("Kondisi terpenuhi")
else:
    print("Aman dari ZeroDivisionError!")

# Contoh 2: or --- operand kedua tidak dievaluasi jika pertama True
is_admin = True
if is_admin or cek_password_rumit():  # cek_password_rumit() TIDAK dipanggil
    print("Akses diberikan")
```

**Manfaat short-circuit:**
- Menghindari error (misalnya division by zero).
- Meningkatkan performa (menghindari evaluasi yang tidak perlu).
- Memungkinkan penulisan kode yang ringkas namun aman.

---

## 3.6 Decision Table

### 3.6.1 Apa Itu Decision Table?

**Decision Table** (Tabel Keputusan) adalah alat bantu yang menyajikan logika kondisional secara terstruktur dalam bentuk tabel. Decision table sangat berguna ketika:

- Terdapat **banyak kombinasi kondisi** yang harus dipertimbangkan.
- Logika percabangan menjadi **terlalu kompleks** untuk dipahami hanya dengan membaca kode.
- Kita ingin **memvalidasi** bahwa semua kemungkinan sudah ditangani.

### 3.6.2 Contoh: Penentuan Tarif Pengiriman

Sebuah jasa pengiriman menentukan tarif berdasarkan tiga faktor: **berat paket**, **jarak pengiriman**, dan **jenis layanan**.

**Decision Table:**

| No. | Berat | Jarak | Layanan | Tarif (Rp) |
|:---:|:-----:|:-----:|:-------:|:----------:|
| 1 | <= 1 kg | <= 50 km | Reguler | 10.000 |
| 2 | <= 1 kg | <= 50 km | Express | 20.000 |
| 3 | <= 1 kg | > 50 km | Reguler | 15.000 |
| 4 | <= 1 kg | > 50 km | Express | 30.000 |
| 5 | > 1 kg | <= 50 km | Reguler | 20.000 |
| 6 | > 1 kg | <= 50 km | Express | 35.000 |
| 7 | > 1 kg | > 50 km | Reguler | 30.000 |
| 8 | > 1 kg | > 50 km | Express | 50.000 |

**Implementasi dalam Python:**

```python
# ============================================
# Sistem Tarif Pengiriman Paket
# ============================================

print("=== KALKULATOR TARIF PENGIRIMAN ===")
print()

berat = float(input("Berat paket (kg): "))
jarak = float(input("Jarak pengiriman (km): "))
layanan = input("Jenis layanan (reguler/express): ").lower()

# Validasi input
if berat <= 0 or jarak <= 0:
    print("Error: Berat dan jarak harus positif!")
elif layanan not in ["reguler", "express"]:
    print("Error: Layanan harus 'reguler' atau 'express'!")
else:
    # Tentukan tarif berdasarkan decision table
    if berat <= 1:
        if jarak <= 50:
            tarif = 10000 if layanan == "reguler" else 20000
        else:
            tarif = 15000 if layanan == "reguler" else 30000
    else:
        if jarak <= 50:
            tarif = 20000 if layanan == "reguler" else 35000
        else:
            tarif = 30000 if layanan == "reguler" else 50000

    # Tampilkan hasil
    print("\n" + "=" * 35)
    print("  RINCIAN PENGIRIMAN")
    print("=" * 35)
    print(f"  Berat    : {berat} kg")
    print(f"  Jarak    : {jarak} km")
    print(f"  Layanan  : {layanan.capitalize()}")
    print(f"  Tarif    : Rp{tarif:,}")
    print("=" * 35)
```

---

## 3.7 Nested `if` (if Bersarang)

### 3.7.1 Konsep

**Nested if** adalah statement `if` yang berada di **dalam** blok `if` lain. Ini digunakan ketika kita perlu membuat keputusan bertingkat --- keputusan kedua bergantung pada hasil keputusan pertama.

```python
if kondisi_luar:
    # kode untuk kondisi_luar True
    if kondisi_dalam:
        # kode untuk kondisi_luar True DAN kondisi_dalam True
    else:
        # kode untuk kondisi_luar True DAN kondisi_dalam False
else:
    # kode untuk kondisi_luar False
```

### 3.7.2 Contoh: Sistem Login dengan Akses Level

```python
# ============================================
# Sistem Login Sederhana dengan Akses Level
# ============================================

print("=== SISTEM LOGIN SIAKAD UAI ===")
print()

username = input("Username : ")
password = input("Password : ")

if username == "admin":
    if password == "admin2026":
        print("\nLogin berhasil!")
        print("Selamat datang, Administrator.")
        print("Akses: Kelola data mahasiswa, dosen, dan mata kuliah.")
    else:
        print("\nLogin gagal!")
        print("Password salah untuk akun admin.")
elif username == "dosen":
    if password == "dosen2026":
        print("\nLogin berhasil!")
        print("Selamat datang, Dosen.")
        print("Akses: Input nilai, lihat jadwal mengajar.")
    else:
        print("\nLogin gagal!")
        print("Password salah untuk akun dosen.")
else:
    # Asumsikan mahasiswa
    if password == "mhs2026":
        print(f"\nLogin berhasil!")
        print(f"Selamat datang, Mahasiswa ({username}).")
        print("Akses: Lihat nilai, lihat jadwal kuliah, KRS online.")
    else:
        print("\nLogin gagal!")
        print("Username atau password tidak dikenali.")
```

### 3.7.3 Kapan Menggunakan Nested if vs Compound Condition?

Tidak semua situasi memerlukan nested if. Terkadang, **compound condition** (kondisi majemuk) menghasilkan kode yang lebih ringkas dan mudah dibaca.

**Perbandingan:**

```python
# === Versi Nested If ===
if umur >= 17:
    if memiliki_sim:
        print("Boleh mengemudi")

# === Versi Compound Condition (lebih ringkas) ===
if umur >= 17 and memiliki_sim:
    print("Boleh mengemudi")
```

**Kapan nested if lebih tepat:**
- Ketika ada **aksi berbeda** untuk setiap level keputusan.
- Ketika keputusan kedua **hanya relevan** jika keputusan pertama bernilai `True`.
- Ketika kode menjadi **lebih mudah dibaca** dalam bentuk bertingkat.

**Kapan compound condition lebih tepat:**
- Ketika semua kondisi harus `True` secara **bersamaan** untuk satu aksi.
- Ketika tidak ada aksi terpisah untuk setiap kondisi individual.
- Ketika jumlah level nesting **tidak lebih dari 2**.

**[!] Peringatan:** Hindari nesting yang terlalu dalam (lebih dari 3 level). Kode yang terlalu nested menjadi sulit dibaca dan di-debug. Jika nesting sudah lebih dari 3 level, pertimbangkan untuk **merestrukturisasi** logika menggunakan compound condition, fungsi terpisah, atau early return.

```python
# BURUK: Terlalu banyak nesting (4 level)
if kondisi_a:
    if kondisi_b:
        if kondisi_c:
            if kondisi_d:
                print("Semua terpenuhi")

# BAIK: Gunakan compound condition
if kondisi_a and kondisi_b and kondisi_c and kondisi_d:
    print("Semua terpenuhi")
```

---

## 3.8 Conditional Expression (Ternary Operator)

### 3.8.1 Sintaks

Python menyediakan cara singkat untuk menulis `if-else` sederhana dalam satu baris, yang disebut **conditional expression** atau **ternary operator**.

```python
# Sintaks:
variabel = nilai_jika_true if kondisi else nilai_jika_false
```

### 3.8.2 Contoh-contoh

```python
# Contoh 1: Menentukan status kelulusan
nilai = 75
status = "Lulus" if nilai >= 60 else "Tidak Lulus"
print(f"Status: {status}")  # Output: Status: Lulus

# Contoh 2: Biaya layanan berdasarkan membership
is_member = True
biaya = 0 if is_member else 10000
print(f"Biaya layanan: Rp{biaya:,}")  # Output: Biaya layanan: Rp0

# Contoh 3: Menentukan paritas bilangan
bilangan = 7
paritas = "Genap" if bilangan % 2 == 0 else "Ganjil"
print(f"{bilangan} adalah bilangan {paritas}")  # Output: 7 adalah bilangan Ganjil

# Contoh 4: Sapaan berdasarkan waktu
jam = 14
sapaan = "Selamat pagi" if jam < 12 else "Selamat siang"
print(sapaan)  # Output: Selamat siang

# Contoh 5: Nilai absolut (tanpa fungsi abs)
x = -5
nilai_absolut = x if x >= 0 else -x
print(f"|{x}| = {nilai_absolut}")  # Output: |-5| = 5
```

### 3.8.3 Kapan Menggunakan Conditional Expression?

**Gunakan** conditional expression ketika:
- Logikanya **sederhana** (hanya satu kondisi, dua kemungkinan nilai).
- Kodenya menjadi **lebih ringkas tanpa mengorbankan keterbacaan**.
- Digunakan untuk **assign nilai** ke variabel.

**Jangan gunakan** conditional expression ketika:
- Logikanya **kompleks** atau melibatkan banyak kondisi.
- Blok kode memiliki **banyak statement** (lebih dari satu baris).
- Keterbacaan menjadi **menurun**.

```python
# BAIK: Sederhana dan jelas
status = "Lulus" if nilai >= 60 else "Tidak Lulus"

# BURUK: Terlalu kompleks untuk satu baris
# Hindari chained ternary yang sulit dibaca
grade = "A" if n >= 85 else "B" if n >= 70 else "C" if n >= 55 else "D"
# Lebih baik gunakan if-elif-else biasa untuk kasus ini
```

---

## 3.9 Match-Case (Python 3.10+)

### 3.9.1 Pengenalan Structural Pattern Matching

Mulai Python 3.10, tersedia fitur baru bernama **match-case** (*structural pattern matching*) yang memberikan cara elegan untuk mencocokkan nilai dengan beberapa pola (*pattern*).

```python
match variabel:
    case pola_1:
        # aksi untuk pola_1
    case pola_2:
        # aksi untuk pola_2
    case _:
        # aksi default (wildcard)
```

**[T] Tips:** Simbol `_` dalam `case _:` berfungsi sebagai **wildcard** --- menangkap semua nilai yang tidak cocok dengan pola sebelumnya, mirip dengan `else` pada `if-elif-else`.

### 3.9.2 Contoh: Hari Kerja vs Hari Libur

```python
# Cek hari kerja atau hari libur menggunakan match-case
hari = input("Masukkan nama hari: ").capitalize()

match hari:
    case "Senin" | "Selasa" | "Rabu" | "Kamis" | "Jumat":
        print(f"{hari} adalah hari kerja.")
        print("Jam operasional kampus: 07.00-17.00 WIB")
    case "Sabtu":
        print(f"{hari} adalah hari libur (setengah hari).")
        print("Beberapa kegiatan UKM mungkin berlangsung.")
    case "Minggu":
        print(f"{hari} adalah hari libur.")
        print("Kampus tutup.")
    case _:
        print(f"'{hari}' bukan nama hari yang valid!")
```

### 3.9.3 Contoh: Kalkulator Sederhana

```python
# Kalkulator sederhana menggunakan match-case
angka1 = float(input("Angka pertama: "))
operator = input("Operator (+, -, *, /): ")
angka2 = float(input("Angka kedua: "))

match operator:
    case "+":
        hasil = angka1 + angka2
    case "-":
        hasil = angka1 - angka2
    case "*":
        hasil = angka1 * angka2
    case "/":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            print("Error: Tidak bisa membagi dengan nol!")
            hasil = None
    case _:
        print(f"Operator '{operator}' tidak dikenali!")
        hasil = None

if hasil is not None:
    print(f"{angka1} {operator} {angka2} = {hasil}")
```

**[!] Peringatan:** Fitur `match-case` hanya tersedia di **Python 3.10 ke atas**. Jika menggunakan versi Python yang lebih lama, gunakan `if-elif-else` sebagai alternatif. Di Google Colab, Python yang tersedia umumnya sudah mendukung fitur ini.

---

## 3.10 Studi Kasus Lengkap: Sistem Pemesanan Tiket KRL Jabodetabek

Berikut adalah program lengkap yang menggabungkan berbagai konsep percabangan yang telah dipelajari. Program ini mensimulasikan sistem pemesanan tiket **KRL Commuter Line Jabodetabek**.

```python
# ================================================================
# STUDI KASUS: SISTEM PEMESANAN TIKET KRL JABODETABEK
# ================================================================
# Program ini mensimulasikan pemesanan tiket KRL dengan:
# - Pemilihan stasiun asal dan tujuan
# - Jenis penumpang (umum, mahasiswa, lansia)
# - Perhitungan tarif berdasarkan jarak
# - Diskon untuk kartu multi-trip
# ================================================================

print("=" * 55)
print("     SISTEM PEMESANAN TIKET KRL JABODETABEK")
print("        PT Kereta Commuter Indonesia")
print("=" * 55)
print()

# --- Data Stasiun dan Jarak (dalam km dari Jakarta Kota) ---
stasiun_data = {
    "Jakarta Kota": 0,
    "Manggarai": 5,
    "Tanah Abang": 7,
    "Sudirman": 4,
    "Bogor": 54,
    "Depok": 33,
    "Bekasi": 18,
    "Tangerang": 29,
}

# Tampilkan daftar stasiun
print("Daftar Stasiun Tersedia:")
print("-" * 30)
nomor = 1
daftar_stasiun = list(stasiun_data.keys())
for nama_stasiun in daftar_stasiun:
    print(f"  {nomor}. {nama_stasiun}")
    nomor += 1
print("-" * 30)
print()

# --- Input Stasiun ---
asal_idx = int(input("Pilih stasiun asal (nomor): ")) - 1
tujuan_idx = int(input("Pilih stasiun tujuan (nomor): ")) - 1

# Validasi input stasiun
if asal_idx < 0 or asal_idx >= len(daftar_stasiun):
    print("Error: Nomor stasiun asal tidak valid!")
elif tujuan_idx < 0 or tujuan_idx >= len(daftar_stasiun):
    print("Error: Nomor stasiun tujuan tidak valid!")
elif asal_idx == tujuan_idx:
    print("Error: Stasiun asal dan tujuan tidak boleh sama!")
else:
    stasiun_asal = daftar_stasiun[asal_idx]
    stasiun_tujuan = daftar_stasiun[tujuan_idx]

    # Hitung jarak
    jarak = abs(stasiun_data[stasiun_asal] - stasiun_data[stasiun_tujuan])

    # --- Input Jenis Penumpang ---
    print()
    print("Jenis Penumpang:")
    print("  1. Umum")
    print("  2. Mahasiswa (dengan KTM)")
    print("  3. Lansia (60 tahun ke atas)")
    jenis_penumpang = int(input("Pilih jenis penumpang (1-3): "))

    # --- Input Jenis Kartu ---
    print()
    print("Jenis Pembayaran:")
    print("  1. Kartu Multi-Trip (KMT)")
    print("  2. Tiket Harian Berjaminan (THB)")
    jenis_kartu = int(input("Pilih jenis pembayaran (1-2): "))

    # --- Input Jumlah Tiket ---
    jumlah = int(input("Jumlah tiket: "))

    if jumlah <= 0:
        print("Error: Jumlah tiket harus minimal 1!")
    elif jenis_penumpang < 1 or jenis_penumpang > 3:
        print("Error: Jenis penumpang tidak valid!")
    elif jenis_kartu < 1 or jenis_kartu > 2:
        print("Error: Jenis pembayaran tidak valid!")
    else:
        # --- Perhitungan Tarif ---

        # Tarif dasar berdasarkan jarak (Rp per km)
        if jarak <= 10:
            tarif_dasar = 3000
        elif jarak <= 25:
            tarif_dasar = 3000 + (jarak - 10) * 200
        elif jarak <= 50:
            tarif_dasar = 6000 + (jarak - 25) * 150
        else:
            tarif_dasar = 9750 + (jarak - 50) * 100

        # Diskon berdasarkan jenis penumpang
        if jenis_penumpang == 1:
            label_penumpang = "Umum"
            diskon_penumpang = 0
        elif jenis_penumpang == 2:
            label_penumpang = "Mahasiswa"
            diskon_penumpang = 0.20  # Diskon 20% untuk mahasiswa
        else:
            label_penumpang = "Lansia"
            diskon_penumpang = 0.50  # Diskon 50% untuk lansia

        # Diskon tambahan untuk kartu multi-trip
        if jenis_kartu == 1:
            label_kartu = "Kartu Multi-Trip (KMT)"
            diskon_kartu = 0.05  # Diskon 5% tambahan
        else:
            label_kartu = "Tiket Harian Berjaminan (THB)"
            diskon_kartu = 0

        # Hitung tarif akhir per tiket
        potongan_penumpang = tarif_dasar * diskon_penumpang
        tarif_setelah_penumpang = tarif_dasar - potongan_penumpang
        potongan_kartu = tarif_setelah_penumpang * diskon_kartu
        tarif_per_tiket = tarif_setelah_penumpang - potongan_kartu

        # Bulatkan ke ratusan terdekat
        tarif_per_tiket = round(tarif_per_tiket / 100) * 100

        # Total pembayaran
        total_bayar = tarif_per_tiket * jumlah

        # --- Tampilkan Struk ---
        print()
        print("=" * 55)
        print("           STRUK PEMESANAN TIKET KRL")
        print("         PT Kereta Commuter Indonesia")
        print("=" * 55)
        print(f"  Stasiun Asal    : {stasiun_asal}")
        print(f"  Stasiun Tujuan  : {stasiun_tujuan}")
        print(f"  Jarak Tempuh    : {jarak} km")
        print("-" * 55)
        print(f"  Jenis Penumpang : {label_penumpang}")
        print(f"  Jenis Pembayaran: {label_kartu}")
        print(f"  Jumlah Tiket    : {jumlah}")
        print("-" * 55)
        print(f"  Tarif Dasar     : Rp{tarif_dasar:>10,}")
        if diskon_penumpang > 0:
            print(f"  Diskon {label_penumpang:10s}: -Rp{potongan_penumpang:>9,.0f} ({int(diskon_penumpang*100)}%)")
        if diskon_kartu > 0:
            print(f"  Diskon KMT      : -Rp{potongan_kartu:>9,.0f} ({int(diskon_kartu*100)}%)")
        print(f"  Tarif per Tiket : Rp{tarif_per_tiket:>10,}")
        print("-" * 55)
        print(f"  TOTAL BAYAR     : Rp{total_bayar:>10,}")
        print("=" * 55)
        print()

        # Pesan tambahan berdasarkan jarak
        if jarak > 40:
            print("  [Info] Perjalanan jauh. Estimasi waktu: ~90 menit.")
            print("  Pastikan membawa bekal dan charger HP.")
        elif jarak > 20:
            print("  [Info] Estimasi waktu perjalanan: ~45 menit.")
        else:
            print("  [Info] Perjalanan dekat. Estimasi waktu: ~20 menit.")

        print()
        print("  Selamat menikmati perjalanan Anda!")
        print("  Terima kasih telah menggunakan KRL Commuter Line.")
        print("=" * 55)
```

**Analisis Studi Kasus:**

Program di atas mendemonstrasikan:
1. **if-elif-else** --- untuk menentukan tarif berdasarkan jarak, jenis penumpang, dan jenis kartu.
2. **Nested if** --- validasi input dilakukan bertingkat.
3. **Compound conditions** --- validasi rentang input menggunakan operator `or`.
4. **Conditional expression** --- tidak digunakan secara eksplisit agar kode tetap mudah dibaca untuk pemula.
5. **Formatted output** --- penggunaan f-string untuk menampilkan struk yang rapi.

---

## 3.11 Common Mistakes (Kesalahan Umum)

Berikut adalah kesalahan-kesalahan umum yang sering dilakukan mahasiswa saat menulis kode percabangan dalam Python.

### Kesalahan 1: Lupa Tanda Titik Dua (`:`)

```python
# SALAH - SyntaxError: expected ':'
if nilai >= 60
    print("Lulus")

# BENAR
if nilai >= 60:
    print("Lulus")
```

### Kesalahan 2: Indentation Error

```python
# SALAH - IndentationError: expected an indented block
if nilai >= 60:
print("Lulus")

# SALAH - IndentationError: unexpected indent (mix tabs dan spaces)
if nilai >= 60:
    print("Lulus")  # menggunakan 4 spasi
	print("Selamat")  # menggunakan tab --- JANGAN CAMPUR!

# BENAR - konsisten menggunakan 4 spasi
if nilai >= 60:
    print("Lulus")
    print("Selamat")
```

**[T] Tips:** Di Google Colab dan kebanyakan editor modern, gunakan **4 spasi** untuk indentasi. Jangan pernah mencampur tab dan spasi.

### Kesalahan 3: Menggunakan `=` Alih-alih `==`

```python
# SALAH - ini assignment, bukan perbandingan!
if nilai = 60:
    print("Lulus")

# BENAR - gunakan == untuk perbandingan
if nilai == 60:
    print("Nilai tepat 60")
```

**Penjelasan:**
- `=` adalah operator **assignment** (penugasan): `nilai = 60` berarti "simpan 60 ke variabel `nilai`".
- `==` adalah operator **perbandingan** (kesamaan): `nilai == 60` berarti "apakah `nilai` sama dengan 60?".

### Kesalahan 4: Kondisi Redundan

```python
# SALAH - redundan, is_lulus sudah boolean
if is_lulus == True:
    print("Selamat!")

# BENAR - langsung gunakan variabel boolean
if is_lulus:
    print("Selamat!")

# SALAH - redundan
if is_lulus == False:
    print("Belum lulus")

# BENAR
if not is_lulus:
    print("Belum lulus")
```

### Kesalahan 5: Unreachable Code (Kode Tak Terjangkau)

```python
# SALAH - elif kedua tidak akan pernah dijalankan
if nilai >= 60:
    print("Lulus")
elif nilai >= 80:        # <-- TIDAK PERNAH TERCAPAI!
    print("Lulus dengan baik")  # Karena nilai >= 80 juga >= 60, sudah ditangkap di atas
else:
    print("Tidak lulus")

# BENAR - urutkan dari kondisi paling spesifik (tertinggi) ke paling umum
if nilai >= 80:
    print("Lulus dengan baik")
elif nilai >= 60:
    print("Lulus")
else:
    print("Tidak lulus")
```

### Kesalahan 6: Lupa `else` sebagai Safety Net

```python
# KURANG BAIK - tidak ada penanganan kasus default
bulan = int(input("Masukkan bulan (1-12): "))
if bulan == 1:
    print("Januari")
elif bulan == 2:
    print("Februari")
# ... bagaimana jika user memasukkan 13 atau -5?

# LEBIH BAIK - selalu sediakan else sebagai safety net
bulan = int(input("Masukkan bulan (1-12): "))
if bulan == 1:
    print("Januari")
elif bulan == 2:
    print("Februari")
# ... (bulan lainnya)
else:
    print("Bulan tidak valid!")
```

### Kesalahan 7: Salah Menggunakan `or` dalam Perbandingan Ganda

```python
# SALAH - ini tidak bekerja seperti yang diharapkan!
hari = "Senin"
if hari == "Sabtu" or "Minggu":  # "Minggu" selalu truthy!
    print("Libur")  # Akan selalu mencetak "Libur"!

# BENAR
if hari == "Sabtu" or hari == "Minggu":
    print("Libur")

# ALTERNATIF (lebih Pythonic)
if hari in ["Sabtu", "Minggu"]:
    print("Libur")
```

**Penjelasan:** `if hari == "Sabtu" or "Minggu"` dievaluasi sebagai `if (hari == "Sabtu") or ("Minggu")`. Karena string "Minggu" bukan string kosong, ia bersifat **truthy**, sehingga kondisi selalu `True`.

---

## AI Corner: AI untuk Debugging Conditional Logic

**Level: Dasar**

Pada AI Corner bab ini, kita akan belajar bagaimana memanfaatkan AI (seperti ChatGPT, Claude, atau Gemini) untuk membantu memahami dan men-debug logika percabangan.

### Skenario 1: Meminta AI Menjelaskan Alur Kode

Ketika Anda memiliki kode percabangan yang tidak berperilaku sesuai harapan, Anda bisa meminta AI untuk **menelusuri alur eksekusi** (trace execution).

**Contoh Prompt:**

> "Tolong trace kode Python berikut jika input nilai = 75. Jelaskan langkah demi langkah kondisi mana yang dievaluasi dan apa hasilnya."

```python
# Kode yang ingin di-trace
nilai = 75
if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 55:
    grade = "C"
else:
    grade = "D"
print(grade)
```

AI akan memberikan penjelasan langkah demi langkah:
1. Evaluasi `nilai >= 85` (75 >= 85) -> `False`, lanjut ke `elif`
2. Evaluasi `nilai >= 70` (75 >= 70) -> `True`, eksekusi `grade = "B"`
3. Lewati semua `elif` dan `else` berikutnya
4. Output: `B`

### Skenario 2: Meminta AI Menemukan Bug Logika

**Contoh Prompt:**

> "Kode berikut seharusnya memberikan diskon 10% jika belanja >= 100rb ATAU member, dan diskon 15% jika keduanya. Tetapi hasilnya selalu salah. Di mana bugnya?"

```python
# Kode bermasalah
total = 150000
is_member = True

if total >= 100000 or is_member:
    diskon = 0.10
if total >= 100000 and is_member:
    diskon = 0.15

# Masalah: jika total < 100000 dan is_member True,
# diskon 0.10 terpasang, lalu if kedua menimpa
```

AI akan menjelaskan bahwa **dua `if` terpisah** bukan `if-elif-else`, sehingga kedua blok bisa dieksekusi. AI kemungkinan akan menyarankan perbaikan:

```python
# Perbaikan: gunakan if-elif-else dan urutkan dari kondisi paling spesifik
total = 150000
is_member = True

if total >= 100000 and is_member:
    diskon = 0.15  # Diskon terbesar dulu
elif total >= 100000 or is_member:
    diskon = 0.10
else:
    diskon = 0
```

### Skenario 3: Validasi Saran AI

**Penting:** Jangan langsung menerima saran AI tanpa verifikasi. Langkah-langkah validasi:

1. **Pahami penjelasan AI** --- Apakah penjelasannya logis?
2. **Trace manual** --- Coba trace kode perbaikan AI dengan beberapa input test.
3. **Uji di Google Colab** --- Jalankan kode asli dan kode perbaikan untuk membandingkan.
4. **Cek edge cases** --- Apakah AI memperhitungkan kasus-kasus batas (misalnya nilai = 0, nilai negatif)?

**[!] Peringatan:** AI terkadang "memperbaiki" kode dengan **mengubah logika program** secara keseluruhan, bukan hanya memperbaiki bug. Selalu pastikan bahwa **tujuan awal program** tidak berubah setelah "perbaikan" dari AI.

### Contoh Prompt yang Baik vs Kurang Baik

| Prompt Kurang Baik | Prompt yang Baik |
|---------------------|------------------|
| "Kode saya error, tolong perbaiki" | "Kode berikut seharusnya mencetak 'Lulus' jika nilai >= 60, tapi selalu mencetak 'Tidak Lulus'. Input yang saya coba: 75. Di mana bugnya?" |
| "Buatkan kode if-else" | "Tolong jelaskan alur eksekusi kode if-elif-else berikut jika input = 42. Saya ingin memahami mengapa hasilnya 'C' bukan 'B'." |
| "Fix this" | "Kode berikut memiliki bug pada baris ke-5. Saya menduga masalahnya ada di kondisi `or`. Bisakah Anda menjelaskan apa yang salah dan bagaimana memperbaikinya?" |

**[R] Refleksi:** Coba buat satu contoh kode percabangan yang bermasalah, lalu minta AI menjelaskan bugnya. Bandingkan jawaban AI dengan analisis Anda sendiri. Apakah AI memberikan penjelasan yang akurat?

---

## Latihan Soal

### Tingkat Dasar

**Soal 1: Cek Bilangan Positif, Negatif, atau Nol**

Buat program yang menerima input sebuah bilangan bulat dan menentukan apakah bilangan tersebut positif, negatif, atau nol.

Contoh output:
```
Masukkan bilangan: -7
Bilangan -7 adalah bilangan NEGATIF.
```

---

**Soal 2: Konversi Nilai Angka ke Huruf**

Buat program konversi nilai angka (0-100) ke nilai huruf dengan ketentuan:
- A: 85-100
- B: 70-84
- C: 55-69
- D: 40-54
- E: 0-39

Program harus menampilkan pesan error jika nilai di luar rentang 0-100.

---

**Soal 3: Cek Tahun Kabisat (Lengkap)**

Buat program yang menentukan apakah suatu tahun adalah tahun kabisat dengan aturan lengkap:
- Tahun kabisat jika habis dibagi 400, ATAU
- Habis dibagi 4 tetapi TIDAK habis dibagi 100.

Contoh:
- 2000 -> kabisat (habis dibagi 400)
- 1900 -> bukan kabisat (habis dibagi 100 tapi tidak habis dibagi 400)
- 2024 -> kabisat (habis dibagi 4, tidak habis dibagi 100)
- 2023 -> bukan kabisat

---

**Soal 4: Tarif Listrik berdasarkan Daya**

Buat program yang menentukan tarif listrik per kWh berdasarkan daya terpasang:

| Daya | Tarif per kWh | Subsidi |
|------|:-------------:|:-------:|
| 450 VA | Rp415 | Ya |
| 900 VA | Rp605 | Ya |
| 1.300 VA | Rp1.444,70 | Tidak |
| 2.200 VA | Rp1.444,70 | Tidak |

Input: daya dan jumlah pemakaian (kWh). Output: total tagihan.

---

**Soal 5: Bilangan Terbesar dari Tiga Bilangan**

Buat program yang menerima input tiga bilangan bulat dan menentukan bilangan yang terbesar. Program harus menangani kasus ketika ada bilangan yang bernilai sama.

Contoh output:
```
Masukkan bilangan pertama: 15
Masukkan bilangan kedua: 42
Masukkan bilangan ketiga: 28
Bilangan terbesar adalah 42.
```

---

### Tingkat Menengah

**Soal 6: Kalkulator BMI (Body Mass Index)**

Buat program kalkulator BMI dengan rumus:
```
BMI = berat (kg) / tinggi (m)^2
```

Kategori berdasarkan WHO (disesuaikan untuk Asia):

| BMI | Kategori |
|-----|----------|
| < 18.5 | Berat badan kurang (Underweight) |
| 18.5 - 22.9 | Normal |
| 23.0 - 24.9 | Berat badan berlebih (Overweight) |
| 25.0 - 29.9 | Obesitas Tingkat I |
| >= 30.0 | Obesitas Tingkat II |

Tampilkan BMI (2 desimal), kategori, dan saran kesehatan singkat.

---

**Soal 7: Tarif Pajak Progresif PPh 21**

Buat program yang menghitung Pajak Penghasilan (PPh 21) berdasarkan tarif progresif Indonesia:

| Penghasilan Kena Pajak (PKP) | Tarif |
|------------------------------|:-----:|
| s.d. Rp60.000.000 | 5% |
| > Rp60.000.000 s.d. Rp250.000.000 | 15% |
| > Rp250.000.000 s.d. Rp500.000.000 | 25% |
| > Rp500.000.000 s.d. Rp5.000.000.000 | 30% |
| > Rp5.000.000.000 | 35% |

Input: penghasilan bruto per tahun dan status PTKP (TK/0, K/0, K/1, K/2, K/3). Hitung PKP dan total pajak.

---

**Soal 8: Cek Segitiga**

Buat program yang menerima input tiga sisi segitiga dan menentukan:
1. Apakah tiga sisi tersebut bisa membentuk segitiga (valid/tidak). Syarat: jumlah dua sisi harus lebih besar dari sisi ketiga.
2. Jika valid, tentukan jenisnya:
   - Sama sisi: ketiga sisi sama panjang
   - Sama kaki: dua sisi sama panjang
   - Sembarang: tidak ada sisi yang sama panjang

---

**Soal 9: Sistem Diskon Supermarket**

Buat program sistem diskon supermarket dengan ketentuan:
- Member mendapat diskon **10%**
- Belanja di atas Rp200.000 mendapat diskon **5%**
- Member yang belanja di atas Rp200.000 mendapat diskon **15%** (bukan 10%+5%)
- Jika hari Jumat, semua diskon ditambah **2%** (Jumat Berkah)

Input: total belanja, status member (ya/tidak), dan nama hari. Output: rincian diskon dan total bayar.

---

**Soal 10: Konversi Angka ke Kata (1-99)**

Buat program yang mengkonversi angka bulat (1-99) menjadi kata dalam Bahasa Indonesia.

Contoh:
- 1 -> "satu"
- 11 -> "sebelas"
- 15 -> "lima belas"
- 25 -> "dua puluh lima"
- 99 -> "sembilan puluh sembilan"

*Petunjuk:* Perhatikan kasus khusus: 10 ("sepuluh"), 11 ("sebelas"), dan angka belasan (12-19: "dua belas", "tiga belas", dst.).

---

### Tingkat Mahir

**Soal 11: Penentu Zodiak**

Buat program yang menentukan zodiak berdasarkan tanggal lahir (bulan dan hari).

| Zodiak | Rentang Tanggal |
|--------|:---------------:|
| Capricorn | 22 Des - 19 Jan |
| Aquarius | 20 Jan - 18 Feb |
| Pisces | 19 Feb - 20 Mar |
| Aries | 21 Mar - 19 Apr |
| Taurus | 20 Apr - 20 Mei |
| Gemini | 21 Mei - 20 Jun |
| Cancer | 21 Jun - 22 Jul |
| Leo | 23 Jul - 22 Agu |
| Virgo | 23 Agu - 22 Sep |
| Libra | 23 Sep - 22 Okt |
| Scorpio | 23 Okt - 21 Nov |
| Sagittarius | 22 Nov - 21 Des |

Input: bulan (1-12) dan hari (1-31). Lakukan validasi input (pastikan hari valid untuk bulan yang dipilih).

---

**Soal 12: Sistem Antrian Prioritas Rumah Sakit**

Buat program simulasi antrian rumah sakit dengan sistem prioritas:

**Prioritas Utama:**
1. **IGD (Instalasi Gawat Darurat)** --- prioritas tertinggi
2. **Lansia (>= 60 tahun)** --- prioritas kedua
3. **Umum** --- prioritas terendah

**Sub-prioritas dalam setiap kategori:**
- Pasien yang sudah mendaftar lebih dulu mendapat nomor antrian lebih kecil.
- Pasien dengan rujukan dari klinik mendapat prioritas +1 dalam kategorinya.

Input: nama pasien, umur, jenis kunjungan (IGD/biasa), memiliki rujukan (ya/tidak).
Output: nomor antrian dengan format: `[KATEGORI]-[NOMOR]` (contoh: `IGD-001`, `LANSIA-005`, `UMUM-023`).

---

**Soal 13: Tantangan --- Grade Tanpa `if-elif-else`**

Tanpa menggunakan `if-elif-else`, buat program yang menentukan grade nilai (A, B, C, D, E) menggunakan **dictionary mapping** dan operasi matematika.

*Petunjuk:* Manfaatkan pembagian integer (`//`) untuk memetakan rentang nilai ke index, kemudian gunakan dictionary atau list untuk mendapatkan grade-nya.

```python
# Contoh pendekatan (lengkapi sendiri):
# nilai 85-100 -> index 4 -> "A"
# nilai 70-84  -> index 3 -> "B"
# ...
```

---

## Rangkuman

Berikut adalah poin-poin kunci yang telah dipelajari dalam Bab 3:

1. **Percabangan (selection)** adalah struktur kontrol yang memungkinkan program mengambil jalur eksekusi berbeda berdasarkan kondisi tertentu. Ini adalah salah satu dari tiga struktur kontrol fundamental dalam pemrograman.

2. **Statement `if`** menjalankan blok kode **hanya jika** kondisi bernilai `True`. Blok kode ditandai dengan **indentasi** (4 spasi) dan baris `if` diakhiri dengan **titik dua (`:`)**.

3. **Statement `if-else`** menyediakan **dua jalur alternatif**: satu untuk kondisi `True` dan satu untuk kondisi `False`. Selalu ada tepat satu jalur yang dieksekusi.

4. **Statement `if-elif-else`** menangani **lebih dari dua kemungkinan**. Python mengevaluasi kondisi **dari atas ke bawah** dan menjalankan blok pertama yang kondisinya `True`. Urutan kondisi sangat penting --- letakkan kondisi paling spesifik di atas.

5. **Operator logika** (`and`, `or`, `not`) digunakan untuk membuat **kondisi majemuk** (*compound conditions*). Operator `and` memerlukan kedua kondisi `True`, operator `or` memerlukan minimal satu kondisi `True`, dan operator `not` membalikkan nilai boolean.

6. **Short-circuit evaluation** --- Python menghentikan evaluasi ekspresi logika lebih awal jika hasilnya sudah bisa ditentukan. Ini berguna untuk menghindari error dan meningkatkan performa.

7. **Decision table** adalah alat bantu untuk memetakan kombinasi kondisi ke aksi/hasil secara terstruktur. Sangat berguna untuk memastikan semua kemungkinan telah ditangani sebelum menulis kode.

8. **Nested if** (if bersarang) digunakan untuk keputusan bertingkat. Namun, hindari nesting yang terlalu dalam (lebih dari 3 level) karena mengurangi keterbacaan kode.

9. **Conditional expression** (ternary operator) menyediakan cara ringkas untuk menulis `if-else` sederhana dalam satu baris: `nilai = x if kondisi else y`. Gunakan hanya untuk kasus sederhana.

10. **Match-case** (Python 3.10+) adalah fitur *structural pattern matching* yang menyediakan cara elegan untuk mencocokkan nilai dengan beberapa pola, mirip dengan `switch-case` di bahasa lain.

11. **Kesalahan umum** yang harus dihindari: lupa titik dua, indentation error, menggunakan `=` alih-alih `==`, kondisi redundan, unreachable code, dan salah menggunakan `or` dalam perbandingan ganda.

12. **AI dapat membantu** men-debug logika percabangan dengan cara menelusuri alur eksekusi (trace), menemukan bug logika, dan menyarankan perbaikan. Namun, selalu **validasi saran AI** secara manual sebelum menerimanya.

---

## Referensi

1. **Downey, A.** (2024). *Think Python: How to Think Like a Computer Scientist* (3rd ed.). O'Reilly Media. Bab 5: Conditionals and Recursion.

2. **Lutz, M.** (2023). *Learning Python* (6th ed.). O'Reilly Media. Part II: Statements and Syntax --- Chapter 12: if Tests and Syntax Rules.

3. **Matthes, E.** (2023). *Python Crash Course* (3rd ed.). No Starch Press. Chapter 5: if Statements.

4. **Python Software Foundation.** (2024). *The Python Tutorial --- More Control Flow Tools*. Diakses dari https://docs.python.org/3/tutorial/controlflow.html

5. **Python Software Foundation.** (2024). *PEP 634 --- Structural Pattern Matching: Specification*. Diakses dari https://peps.python.org/pep-0634/

6. **Gaddis, T.** (2021). *Starting Out with Python* (5th ed.). Pearson. Chapter 3: Decision Structures and Boolean Logic.

7. **Zelle, J.** (2016). *Python Programming: An Introduction to Computer Science* (3rd ed.). Franklin, Beedle & Associates. Chapter 7: Decision Structures.

8. **Bohm, C. & Jacopini, G.** (1966). Flow Diagrams, Turing Machines and Languages with Only Two Formation Rules. *Communications of the ACM*, 9(5), 366-371.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* --- Program Studi Informatika, Universitas Al Azhar Indonesia
