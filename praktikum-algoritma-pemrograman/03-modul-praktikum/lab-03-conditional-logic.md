# Lab 03: Conditional Logic

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Algoritma dan Pemrograman |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Durasi** | 75 menit |
| **Prasyarat** | Lab 02 — Variabel dan Ekspresi |

---

## Tujuan Praktikum

Setelah menyelesaikan lab ini, mahasiswa mampu:
- Menggunakan pernyataan `if`, `if-else`, dan `if-elif-else`
- Menggabungkan kondisi dengan operator logika (`and`, `or`, `not`)
- Menerapkan percabangan bersarang (*nested if*)
- Membangun program Kalkulator BMI dan Konverter Nilai

---

## Persiapan

1. Buka Google Colab dan buat notebook baru
2. Beri nama `Lab03_NamaAnda_NIM.ipynb`
3. Pastikan Anda telah memahami variabel, tipe data, dan operator

---

## Langkah-langkah

### Langkah 1 — Pernyataan `if` Sederhana

```python
# Pernyataan if sederhana
saldo = 150000

print(f"Saldo Anda: Rp{saldo:,}")

if saldo > 100000:
    print("Saldo Anda mencukupi untuk transaksi.")

if saldo < 50000:
    print("Peringatan: saldo Anda hampir habis!")

print("Program selesai.")
```

**Penjelasan:**
- Blok kode di bawah `if` hanya dijalankan jika kondisi bernilai `True`
- Perhatikan penggunaan **indentasi** (4 spasi) — ini wajib di Python
- Jika kondisi `False`, blok tersebut dilewati

### Langkah 2 — Pernyataan `if-else`

```python
# Cek apakah bilangan genap atau ganjil
bilangan = int(input("Masukkan sebuah bilangan bulat: "))

if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan GENAP")
else:
    print(f"{bilangan} adalah bilangan GANJIL")
```

### Langkah 3 — Pernyataan `if-elif-else`

```python
# Menentukan tarif parkir berdasarkan jenis kendaraan
print("=== SISTEM PARKIR MALL ===")
print("Jenis kendaraan:")
print("1. Motor")
print("2. Mobil")
print("3. Truk")

jenis = input("Pilih jenis kendaraan (1/2/3): ")
jam = int(input("Lama parkir (jam): "))

if jenis == "1":
    kendaraan = "Motor"
    tarif_per_jam = 2000
elif jenis == "2":
    kendaraan = "Mobil"
    tarif_per_jam = 5000
elif jenis == "3":
    kendaraan = "Truk"
    tarif_per_jam = 10000
else:
    kendaraan = "Tidak dikenal"
    tarif_per_jam = 0

if tarif_per_jam > 0:
    total = tarif_per_jam * jam
    print(f"\nKendaraan : {kendaraan}")
    print(f"Durasi    : {jam} jam")
    print(f"Tarif/jam : Rp{tarif_per_jam:,}")
    print(f"Total     : Rp{total:,}")
else:
    print("Jenis kendaraan tidak valid!")
```

### Langkah 4 — Kondisi Majemuk (`and`, `or`, `not`)

```python
# Sistem penentuan kelulusan mata kuliah
nama = input("Nama mahasiswa: ")
nilai_uts = float(input("Nilai UTS (0-100): "))
nilai_uas = float(input("Nilai UAS (0-100): "))
kehadiran = float(input("Persentase kehadiran (%): "))

nilai_akhir = (nilai_uts * 0.4) + (nilai_uas * 0.6)

print(f"\n--- Hasil Evaluasi: {nama} ---")
print(f"Nilai UTS      : {nilai_uts}")
print(f"Nilai UAS      : {nilai_uas}")
print(f"Nilai Akhir    : {nilai_akhir:.1f}")
print(f"Kehadiran      : {kehadiran}%")

# Syarat lulus: nilai >= 60 DAN kehadiran >= 75%
if nilai_akhir >= 60 and kehadiran >= 75:
    print("Status         : LULUS")
elif nilai_akhir >= 60 and kehadiran < 75:
    print("Status         : TIDAK LULUS (kehadiran kurang)")
elif nilai_akhir < 60 and kehadiran >= 75:
    print("Status         : TIDAK LULUS (nilai kurang)")
else:
    print("Status         : TIDAK LULUS (nilai dan kehadiran kurang)")
```

### Langkah 5 — Percabangan Bersarang (*Nested If*)

```python
# Sistem tiket bioskop dengan diskon
print("=== BIOSKOP CITRA XXI ===")
hari = input("Hari (Senin-Minggu): ").capitalize()
umur = int(input("Umur penonton: "))
punya_kartu_member = input("Punya kartu member? (ya/tidak): ").lower()

# Harga dasar tiket
if hari in ["Sabtu", "Minggu"]:
    harga_dasar = 50000
    kategori_hari = "Weekend"
else:
    harga_dasar = 35000
    kategori_hari = "Weekday"

# Diskon berdasarkan umur
if umur < 12:
    diskon_umur = 50   # anak-anak diskon 50%
    kategori_umur = "Anak-anak"
elif umur >= 60:
    diskon_umur = 30   # lansia diskon 30%
    kategori_umur = "Lansia"
else:
    diskon_umur = 0
    kategori_umur = "Dewasa"

# Diskon tambahan member
if punya_kartu_member == "ya":
    diskon_member = 10
else:
    diskon_member = 0

# Perhitungan
total_diskon = diskon_umur + diskon_member
potongan = harga_dasar * total_diskon / 100
harga_final = harga_dasar - potongan

print(f"\n--- Rincian Tiket ---")
print(f"Hari          : {hari} ({kategori_hari})")
print(f"Kategori      : {kategori_umur}")
print(f"Harga dasar   : Rp{harga_dasar:,}")
print(f"Diskon umur   : {diskon_umur}%")
print(f"Diskon member : {diskon_member}%")
print(f"Total diskon  : {total_diskon}%  (-Rp{potongan:,.0f})")
print(f"Harga bayar   : Rp{harga_final:,.0f}")
```

### Langkah 6 — Mini Project: Kalkulator BMI

```python
# =============================================
# MINI PROJECT 1: Kalkulator BMI (Body Mass Index)
# =============================================

print("=" * 40)
print("    KALKULATOR BMI (Body Mass Index)")
print("=" * 40)

nama = input("Nama Anda: ")
berat = float(input("Berat badan (kg): "))
tinggi_cm = float(input("Tinggi badan (cm): "))

# Konversi tinggi ke meter
tinggi_m = tinggi_cm / 100

# Hitung BMI
bmi = berat / (tinggi_m ** 2)

# Tentukan kategori BMI (standar Asia)
if bmi < 18.5:
    kategori = "Berat Badan Kurang"
    saran = "Perbanyak asupan nutrisi dan konsultasi dokter."
elif bmi < 23.0:
    kategori = "Berat Badan Normal"
    saran = "Pertahankan pola makan sehat dan olahraga teratur."
elif bmi < 25.0:
    kategori = "Kelebihan Berat Badan"
    saran = "Kurangi makanan berlemak, perbanyak olahraga."
elif bmi < 30.0:
    kategori = "Obesitas Tingkat 1"
    saran = "Segera atur pola makan dan rutin berolahraga."
else:
    kategori = "Obesitas Tingkat 2"
    saran = "Konsultasi dengan dokter untuk program penurunan berat badan."

print(f"\n--- Hasil BMI: {nama} ---")
print(f"Berat badan  : {berat} kg")
print(f"Tinggi badan : {tinggi_cm} cm ({tinggi_m:.2f} m)")
print(f"Nilai BMI    : {bmi:.1f}")
print(f"Kategori     : {kategori}")
print(f"Saran        : {saran}")
```

### Langkah 7 — Mini Project: Konverter Nilai

```python
# =============================================
# MINI PROJECT 2: Konverter Nilai (Angka → Huruf)
# =============================================

print("=" * 40)
print("   KONVERTER NILAI AKADEMIK")
print("=" * 40)

nama = input("Nama mahasiswa : ")
mk = input("Mata kuliah    : ")
tugas = float(input("Nilai Tugas    (0-100): "))
uts = float(input("Nilai UTS      (0-100): "))
uas = float(input("Nilai UAS      (0-100): "))

# Bobot: Tugas 30%, UTS 30%, UAS 40%
nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

# Konversi ke huruf
if nilai_akhir >= 85:
    huruf = "A"
    bobot = 4.0
elif nilai_akhir >= 80:
    huruf = "A-"
    bobot = 3.7
elif nilai_akhir >= 75:
    huruf = "B+"
    bobot = 3.3
elif nilai_akhir >= 70:
    huruf = "B"
    bobot = 3.0
elif nilai_akhir >= 65:
    huruf = "B-"
    bobot = 2.7
elif nilai_akhir >= 60:
    huruf = "C+"
    bobot = 2.3
elif nilai_akhir >= 55:
    huruf = "C"
    bobot = 2.0
elif nilai_akhir >= 40:
    huruf = "D"
    bobot = 1.0
else:
    huruf = "E"
    bobot = 0.0

# Status kelulusan
if huruf in ["A", "A-", "B+", "B", "B-", "C+", "C"]:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

print(f"\n{'=' * 40}")
print(f"  TRANSKRIP NILAI")
print(f"{'=' * 40}")
print(f"Nama         : {nama}")
print(f"Mata Kuliah  : {mk}")
print(f"Tugas (30%)  : {tugas:.1f}")
print(f"UTS   (30%)  : {uts:.1f}")
print(f"UAS   (40%)  : {uas:.1f}")
print(f"{'-' * 40}")
print(f"Nilai Akhir  : {nilai_akhir:.2f}")
print(f"Nilai Huruf  : {huruf} ({bobot:.1f})")
print(f"Status       : {status}")
print(f"{'=' * 40}")
```

---

## Tantangan Tambahan

1. **Kalkulator Tarif Listrik**: Buat program yang menghitung tagihan listrik bulanan berdasarkan golongan (R1/450VA, R1/900VA, R1/1300VA) dan jumlah kWh yang digunakan. Setiap golongan memiliki tarif per kWh yang berbeda.

2. **Sistem Antrian Rumah Sakit**: Buat program yang menentukan prioritas pasien berdasarkan input umur, jenis kelamin (ibu hamil), dan tingkat kegawatan (ringan/sedang/darurat). Tampilkan nomor antrian dan estimasi waktu tunggu.

3. **Rekomendasi Paket Internet**: Buat program yang merekomendasikan paket internet berdasarkan input kebutuhan pengguna (jumlah pengguna, kegiatan utama: streaming/gaming/browsing, budget per bulan).

---

## Checklist Penyelesaian

- [ ] Mampu menggunakan pernyataan `if` sederhana
- [ ] Mampu menggunakan `if-else` dan `if-elif-else`
- [ ] Mampu menggunakan operator logika `and`, `or`, `not`
- [ ] Mampu menggunakan percabangan bersarang (*nested if*)
- [ ] Menyelesaikan Mini Project: Kalkulator BMI
- [ ] Menyelesaikan Mini Project: Konverter Nilai
- [ ] Mengerjakan minimal 1 tantangan tambahan

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"*
