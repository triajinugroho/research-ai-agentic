---
mata_kuliah: Algoritma dan Pemrograman
kode_mk: INF-101
sks: 2 SKS (Teori)
semester: Genap 2025/2026
jenis: UTS
---

# UJIAN TENGAH SEMESTER (UTS)
## Semester Genap Tahun Akademik 2025/2026

**UNIVERSITAS AL AZHAR INDONESIA**
**Fakultas Sains dan Teknologi — Program Studi Informatika**

> *"Bacalah dengan (menyebut) nama Tuhanmu yang menciptakan."*
> — **QS Al-'Alaq: 1**

| Field             | Nilai                                       |
|-------------------|---------------------------------------------|
| Mata Kuliah       | Algoritma dan Pemrograman                   |
| Kode MK / SKS     | INF-101 / 2 SKS (Teori)                     |
| Dosen             | Tri Aji Nugroho, S.T., M.T.                 |
| Kelas             | [......]                                    |
| Hari/Tanggal      | [......]                                    |
| Waktu             | 120 menit                                   |
| Sifat Ujian       | Closed-book, tanpa AI tools                 |

---

## PETUNJUK PENGERJAAN

1. Bacalah **Basmalah** sebelum memulai ujian.
2. Tuliskan Nama, NIM, dan Kelas di lembar jawaban.
3. Kerjakan dengan jujur, mandiri, dan bertanggung jawab sesuai nilai integritas akademik dan etika Islami.
4. Dilarang menggunakan AI tools (ChatGPT, Copilot, dll.), kecuali dinyatakan lain pada sifat ujian.
5. Tulis huruf jawaban Pilihan Ganda (A/B/C/D/E) pada lembar jawaban. Untuk Esai, jelaskan langkah kerja dan tunjukkan proses berpikir — jawaban benar tanpa proses mendapat nilai partial.
6. Periksa kembali jawaban sebelum dikumpulkan.
7. Akhiri dengan **Hamdalah**.

> *"Sesungguhnya amal-amal itu tergantung pada niatnya."*
> — **HR. Bukhari-Muslim**

---

## BAGIAN I — PILIHAN GANDA (40 poin)

*Pilih satu jawaban yang paling tepat. Setiap soal bernilai 2 poin.*

---

> **Sub-CPMK 1.1** — Mendefinisikan konsep algoritma, sejarah perkembangannya, dan relevansinya dalam kehidupan sehari-hari
> *Level Bloom:* C2 · *Konteks:* Umum

**1.** Manakah dari pernyataan berikut yang **bukan** merupakan sifat wajib sebuah algoritma?

A. Finiteness — jumlah langkah terbatas dan berakhir setelah sejumlah langkah tertentu
B. Definiteness — setiap langkah dirumuskan jelas dan tidak ambigu
C. Input — menerima nol atau lebih nilai masukan
D. Output — menghasilkan satu atau lebih keluaran
E. Randomness — setiap langkah harus menggunakan nilai acak untuk menjamin keberhasilan

---

> **Sub-CPMK 1.2** — Menjelaskan empat pilar computational thinking: dekomposisi, pengenalan pola, abstraksi, dan desain algoritma
> *Level Bloom:* C3 · *Konteks:* JTBD (manajemen waktu belajar)

**2.** Seorang mahasiswa ingin mengelola waktu belajarnya dengan lebih baik. Ia membagi aktivitas harian menjadi bagian-bagian kecil seperti "membaca materi", "mengerjakan latihan", dan "review catatan", lalu menjadwalkannya satu per satu. Pilar *computational thinking* yang paling tepat menggambarkan langkah tersebut adalah ...

A. Abstraksi — menyembunyikan detail yang tidak perlu
B. Dekomposisi — memecah masalah besar menjadi sub-masalah yang lebih kecil
C. Pengenalan pola — menemukan kemiripan pada beberapa masalah
D. Desain algoritma — menyusun urutan langkah penyelesaian
E. Evaluasi — menilai hasil akhir dari sebuah proses

---

> **Sub-CPMK 1.3** — Menjelaskan peran Python dan AI dalam ekosistem pemrograman modern serta hubungan dengan mata kuliah ko-requisite Analisis Data Statistik
> *Level Bloom:* C2 · *Konteks:* Umum

**3.** Berikut ini adalah alasan Python banyak dipakai sebagai bahasa utama di ekosistem AI dan data science modern, **kecuali** ...

A. Sintaks yang mudah dibaca mirip bahasa Inggris alami
B. Ekosistem pustaka ilmiah yang matang (NumPy, pandas, scikit-learn)
C. Dukungan kuat komunitas open source dan integrasi Jupyter/Colab
D. Performa eksekusi paling cepat di antara seluruh bahasa pemrograman
E. Interoperabilitas dengan framework AI seperti TensorFlow dan PyTorch

---

> **Sub-CPMK 2.1** — Mengidentifikasi dan menggunakan variabel, konstanta, dan aturan penamaan (naming convention) di Python
> *Level Bloom:* C2 · *Konteks:* Umum

**4.** Manakah nama variabel berikut yang **paling sesuai** konvensi penamaan PEP 8 untuk variabel biasa di Python?

A. `TotalHarga`
B. `total-harga`
C. `total_harga`
D. `2total_harga`
E. `totalHarga@`

---

> **Sub-CPMK 2.2** — Membedakan tipe data dasar (int, float, str, bool) dan melakukan konversi tipe (type casting)
> *Level Bloom:* C3 · *Konteks:* Umum

**5.** Perhatikan potongan kode berikut:

```python
x = "10"
y = 3
z = int(x) + y
```

Tipe data dan nilai dari `z` setelah eksekusi adalah ...

A. `str` dengan nilai `"103"`
B. `int` dengan nilai `13`
C. `float` dengan nilai `13.0`
D. `str` dengan nilai `"13"`
E. Terjadi `TypeError` karena tipe tidak kompatibel

---

> **Sub-CPMK 2.2** — Membedakan tipe data dasar (int, float, str, bool) dan melakukan konversi tipe (type casting)
> *Level Bloom:* C3 · *Konteks:* Umum

**6.** Perhatikan potongan kode berikut:

```python
a = float("7")
b = bool(0)
c = str(a)
print(type(a), type(b), type(c))
```

Output yang tepat adalah ...

A. `<class 'int'> <class 'int'> <class 'str'>`
B. `<class 'float'> <class 'bool'> <class 'str'>`
C. `<class 'float'> <class 'int'> <class 'str'>`
D. `<class 'str'> <class 'bool'> <class 'str'>`
E. `<class 'float'> <class 'bool'> <class 'float'>`

---

> **Sub-CPMK 2.3** — Menerapkan operator aritmatika, perbandingan, logika, dan assignment dalam ekspresi komputasi
> *Level Bloom:* C3 · *Konteks:* Umum

**7.** Perhatikan ekspresi berikut:

```python
hasil = 2 + 3 * 4 ** 2 // 5 - 1
```

Nilai `hasil` setelah dievaluasi adalah ...

A. 9
B. 10
C. 11
D. 30
E. 31

---

> **Sub-CPMK 2.3** — Menerapkan operator aritmatika, perbandingan, logika, dan assignment dalam ekspresi komputasi
> *Level Bloom:* C4 · *Konteks:* Umum

**8.** Perhatikan potongan kode berikut:

```python
def cek():
    print("dipanggil")
    return True

x = False
y = x and cek()
z = True or cek()
```

Berapa kali kata "dipanggil" akan tercetak ke layar?

A. 0 kali
B. 1 kali
C. 2 kali
D. 3 kali
E. Tidak bisa ditentukan tanpa menjalankan program

---

> **Sub-CPMK 2.4** — Menerapkan fungsi input/output untuk interaksi program sederhana
> *Level Bloom:* C3 · *Konteks:* JTBD (form belanja online)

**9.** Pada sebuah form belanja online, pengguna memasukkan harga satuan dan jumlah barang. Potongan kode berikut digunakan untuk menghitung total belanja:

```python
harga = input("Harga satuan: ")
jumlah = input("Jumlah barang: ")
total = harga * jumlah
print("Total:", total)
```

Manakah koreksi yang **paling tepat** agar perhitungan total berjalan benar?

A. Ganti `input()` dengan `print()` pada baris 1 dan 2
B. Gunakan `total = int(harga) * int(jumlah)` agar tipe data menjadi numerik
C. Ganti `print("Total:", total)` menjadi `print("Total:" + total)`
D. Tidak perlu diubah, Python otomatis mengenali tipe numerik dari `input()`
E. Tambahkan `total = str(total)` sebelum `print`

---

> **Sub-CPMK 3.1** — Menerapkan struktur seleksi if, elif, else untuk pengambilan keputusan dalam program
> *Level Bloom:* C3 · *Konteks:* Islami (kalkulasi zakat mal 2,5%)

**10.** Perhatikan potongan kode berikut untuk menghitung zakat mal:

```python
harta = 90_000_000
nisab = 85_000_000

if harta >= nisab:
    zakat = harta * 0.025
    print("Wajib zakat:", zakat)
else:
    print("Belum wajib zakat")
```

Output yang tepat dari program di atas adalah ...

A. `Belum wajib zakat`
B. `Wajib zakat: 2125000.0`
C. `Wajib zakat: 2250000.0`
D. `Wajib zakat: 2500000.0`
E. `Wajib zakat: 22500.0`

---

> **Sub-CPMK 3.2** — Merancang struktur seleksi bertingkat (nested) dan multi-kondisi untuk kasus yang kompleks
> *Level Bloom:* C4 · *Konteks:* Indonesia (grade IP UAI)

**11.** Perhatikan potongan kode konversi nilai akhir ke huruf mutu sesuai standar UAI:

```python
nilai = 78

if nilai >= 85:
    grade = "A"
elif nilai >= 80:
    grade = "A-"
elif nilai >= 75:
    grade = "B+"
elif nilai >= 70:
    grade = "B"
elif nilai >= 65:
    grade = "B-"
elif nilai >= 55:
    grade = "C"
elif nilai >= 45:
    grade = "D"
else:
    grade = "E"
print(grade)
```

Huruf mutu yang dicetak untuk `nilai = 78` adalah ...

A. `A-`
B. `B+`
C. `B`
D. `B-`
E. `C`

---

> **Sub-CPMK 3.3** — Menerapkan match-case statement (Python 3.10+) sebagai alternatif seleksi
> *Level Bloom:* C3 · *Konteks:* Umum

**12.** Perhatikan potongan kode berikut:

```python
hari = "Senin"
match hari:
    case "Senin" | "Selasa" | "Rabu" | "Kamis" | "Jumat":
        kategori = "Hari kerja"
    case "Sabtu" | "Minggu":
        kategori = "Akhir pekan"
    case _:
        kategori = "Tidak dikenal"
print(kategori)
```

Output program di atas adalah ...

A. `Hari kerja`
B. `Akhir pekan`
C. `Tidak dikenal`
D. `Senin`
E. Terjadi `SyntaxError`

---

> **Sub-CPMK 4.1** — Menerapkan perulangan for dengan range() dan iterasi koleksi
> *Level Bloom:* C3 · *Konteks:* Umum

**13.** Berapa kali badan perulangan (`body`) pada potongan kode berikut dieksekusi?

```python
for i in range(2, 20, 3):
    body  # representasi satu baris eksekusi
```

A. 5 kali
B. 6 kali
C. 7 kali
D. 18 kali
E. 20 kali

---

> **Sub-CPMK 4.2** — Menerapkan perulangan while dengan kondisi berhenti yang tepat
> *Level Bloom:* C4 · *Konteks:* Umum

**14.** Perhatikan potongan kode berikut:

```python
n = 10
while n > 0:
    print(n)
    n = n + 1
```

Pernyataan yang **paling tepat** tentang perulangan di atas adalah ...

A. Mencetak `10 9 8 7 6 5 4 3 2 1` lalu berhenti
B. Tidak pernah masuk ke badan perulangan karena kondisi awal salah
C. Akan berjalan selamanya (infinite loop) karena `n` terus bertambah sehingga `n > 0` selalu benar
D. Berhenti ketika `n` mencapai batas maksimum integer Python
E. Mencetak angka 10 saja lalu berhenti karena `n` tidak dimodifikasi

---

> **Sub-CPMK 4.3** — Menggunakan break, continue, dan perulangan bertingkat (nested loop) untuk kontrol alur lanjutan
> *Level Bloom:* C4 · *Konteks:* Umum

**15.** Perhatikan potongan kode berikut:

```python
total = 0
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        if i == 3:
            break
        total = total + (i * j)
print(total)
```

Nilai `total` yang dicetak adalah ...

A. 0
B. 10
C. 12
D. 16
E. 18

---

> **Sub-CPMK 4.4** — Menerapkan pola akumulator, penghitung (counter), dan flag dalam perulangan
> *Level Bloom:* C3 · *Konteks:* JTBD (rekap pengeluaran harian — akumulator)

**16.** Anda ingin merekap total pengeluaran harian Anda selama seminggu dari list `pengeluaran`. Pola yang **paling tepat** digunakan adalah ...

```python
pengeluaran = [25000, 40000, 15000, 60000, 20000, 55000, 30000]
```

A.
```python
total = 0
for x in pengeluaran:
    total = x
```
B.
```python
total = 0
for x in pengeluaran:
    total = total + x
```
C.
```python
total = 1
for x in pengeluaran:
    total = total * x
```
D.
```python
for x in pengeluaran:
    total = total + x
```
E.
```python
total = pengeluaran
for x in pengeluaran:
    total = total + 1
```

---

> **Sub-CPMK 5.1** — Mendefinisikan dan memanggil fungsi dengan parameter dan nilai kembalian (return value)
> *Level Bloom:* C2 · *Konteks:* Umum

**17.** Perhatikan definisi fungsi berikut:

```python
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

hasil = luas_persegi_panjang(5, 3)
```

Pernyataan yang **paling tepat** adalah ...

A. `panjang` dan `lebar` disebut *argument*, sedangkan `5` dan `3` disebut *parameter*
B. `panjang` dan `lebar` disebut *parameter*, sedangkan `5` dan `3` disebut *argument*; fungsi mengembalikan nilai `15`
C. Fungsi tidak mengembalikan apa pun karena tidak ada `print` di dalamnya
D. Fungsi akan error karena parameter belum didefinisikan secara eksplisit tipenya
E. `hasil` akan bernilai `None` karena `return` hanya berlaku di dalam loop

---

> **Sub-CPMK 5.2** — Menjelaskan konsep scope (lokal vs global) dan lifetime variabel
> *Level Bloom:* C4 · *Konteks:* Umum

**18.** Perhatikan potongan kode berikut:

```python
x = 10

def ubah():
    x = 5
    print("dalam:", x)

ubah()
print("luar:", x)
```

Output yang tepat adalah ...

A. `dalam: 5` lalu `luar: 5`
B. `dalam: 10` lalu `luar: 10`
C. `dalam: 5` lalu `luar: 10`
D. `dalam: 10` lalu `luar: 5`
E. Terjadi `NameError` karena `x` di dalam fungsi tidak dideklarasi global

---

> **Sub-CPMK 5.3** — Menerapkan fungsi lambda, default parameter, dan variable-length arguments (*args, **kwargs)
> *Level Bloom:* C3 · *Konteks:* Umum

**19.** Perhatikan potongan kode berikut:

```python
total = lambda *angka: sum(angka)
print(total(1, 2, 3, 4))
```

Output yang tepat adalah ...

A. `1`
B. `4`
C. `10`
D. `(1, 2, 3, 4)`
E. Terjadi `TypeError` karena lambda tidak boleh memakai `*args`

---

> **Sub-CPMK 5.4** — Menerapkan prinsip modularitas dan code reuse melalui pengorganisasian fungsi
> *Level Bloom:* C4 · *Konteks:* Umum

**20.** Perhatikan potongan kode berikut:

```python
# Hitung luas lingkaran 1
r1 = 7
luas1 = 3.14 * r1 * r1

# Hitung luas lingkaran 2
r2 = 10
luas2 = 3.14 * r2 * r2

# Hitung luas lingkaran 3
r3 = 4
luas3 = 3.14 * r3 * r3
```

Pelanggaran prinsip modularitas/*DRY* yang paling tepat pada kode di atas adalah ...

A. Tidak ada pelanggaran, kode sudah modular karena tiap perhitungan ditulis eksplisit
B. Rumus luas lingkaran `3.14 * r * r` diulang tiga kali dan nilai `3.14` tersebar sebagai *magic number* — seharusnya dibungkus dalam satu fungsi `luas_lingkaran(r)` yang dipanggil ulang
C. Variabel `r1`, `r2`, `r3` seharusnya digabung menjadi satu string panjang
D. Kode harus diubah menjadi satu baris panjang untuk efisiensi memori
E. Perhitungan lingkaran tidak boleh memakai konstanta `3.14`, harus memakai bilangan bulat saja

---

## BAGIAN II — ESAI (60 poin)

*Kerjakan kelima soal berikut. Tuliskan langkah berpikir dan justifikasi — jawaban benar tanpa proses mendapat nilai partial.*

---

> **Sub-CPMK 1.2** — Menjelaskan empat pilar computational thinking: dekomposisi, pengenalan pola, abstraksi, dan desain algoritma
> *Level Bloom:* C3 · *Konteks:* JTBD (merancang rutinitas belajar efektif)

**E1. (12 poin)** Sebagai mahasiswa baru Informatika UAI, Anda ingin merancang rutinitas belajar harian yang efektif agar target akademik tercapai tanpa kelelahan berlebihan.

a) Jelaskan secara singkat definisi dari **empat pilar *computational thinking***: (1) dekomposisi, (2) pengenalan pola, (3) abstraksi, dan (4) desain algoritma. Satu kalimat per pilar. **(4 poin)**

b) Terapkan keempat pilar tersebut untuk memecahkan kasus "merancang rutinitas belajar harian yang efektif". Untuk setiap pilar, tuliskan **minimal satu kalimat penerapan konkret** yang relevan dengan kasus (misalnya apa yang didekomposisi, pola apa yang dikenali, detail apa yang diabstraksi, dan bagaimana urutan langkahnya). **(8 poin)**

---

> **Sub-CPMK 3.1 & 3.2** — Menerapkan struktur seleksi if, elif, else; Merancang struktur seleksi bertingkat (nested) dan multi-kondisi
> *Level Bloom:* C3 · *Konteks:* Islami (klasifikasi nisab zakat mal)

**E2. (12 poin)** Anda diminta menulis program klasifikasi zakat mal berdasarkan spesifikasi berikut:

- Input: `harta` (dalam Rupiah) dan `nisab` (nilai setara 85 gram emas, dalam Rupiah).
- Aturan klasifikasi:
  1. Jika `harta < 0` → cetak `"Input tidak valid"`.
  2. Jika `0 <= harta < nisab` → cetak `"Belum wajib zakat"`.
  3. Jika `nisab <= harta < 2 * nisab` → cetak `"Wajib zakat (kategori standar)"` dan hitung `zakat = harta * 0.025`.
  4. Jika `harta >= 2 * nisab` → cetak `"Wajib zakat (kategori besar, pertimbangkan zakat tambahan)"` dan hitung `zakat = harta * 0.025`.

**Tugas Anda:** Tulis kode Python lengkap menggunakan `if/elif/else` yang memenuhi seluruh spesifikasi di atas. Gunakan `input()` untuk menerima nilai `harta` dan `nisab`, dan `print()` untuk menampilkan hasil klasifikasi beserta nilai `zakat` (jika wajib). Beri komentar singkat pada tiap cabang.

---

> **Sub-CPMK 4.1 & 4.4** — Menerapkan perulangan for dengan range() dan iterasi koleksi; Menerapkan pola akumulator, penghitung (counter), dan flag
> *Level Bloom:* C4 · *Konteks:* Indonesia (data jumlah penduduk per provinsi)

**E3. (12 poin)** Diberikan data jumlah penduduk (dalam jiwa, angka dummy) lima provinsi di Indonesia:

```python
provinsi = ["DKI Jakarta", "Jawa Barat", "Jawa Tengah", "DI Yogyakarta", "Banten"]
penduduk = [10_600_000, 48_200_000, 36_500_000, 3_700_000, 11_900_000]
```

Perhatikan kode berikut:

```python
total = 0
terbanyak = penduduk[0]
nama_terbanyak = provinsi[0]

for i in range(len(provinsi)):
    total = total + penduduk[i]
    if penduduk[i] > terbanyak:
        terbanyak = penduduk[i]
        nama_terbanyak = provinsi[i]
    print(f"Iterasi {i}: total sementara = {total}, sementara terbanyak = {nama_terbanyak}")

rata_rata = total / len(provinsi)
print(f"Total penduduk = {total}")
print(f"Rata-rata = {rata_rata}")
print(f"Provinsi terbanyak = {nama_terbanyak} ({terbanyak} jiwa)")
```

**Tugas Anda:** Trace (telusuri) eksekusi program di atas dan tuliskan **seluruh output baris per baris** sesuai urutan kemunculannya. Tuliskan nilai `total`, `terbanyak`, dan `nama_terbanyak` tepat setelah tiap iterasi selesai.

---

> **Sub-CPMK 5.1 & 5.4** — Mendefinisikan dan memanggil fungsi dengan parameter dan nilai kembalian; Menerapkan prinsip modularitas dan code reuse
> *Level Bloom:* C5 · *Konteks:* JTBD (kalkulator BMI & kebutuhan kalori)

**E4. (12 poin)** Perhatikan kode prosedural berikut untuk menghitung BMI dan kebutuhan kalori harian:

```python
# Program kalkulator kesehatan pribadi
berat = float(input("Berat (kg): "))
tinggi_cm = float(input("Tinggi (cm): "))
usia = int(input("Usia: "))
jk = input("Jenis kelamin (L/P): ")

tinggi_m = tinggi_cm / 100
bmi = berat / (tinggi_m * tinggi_m)

if bmi < 18.5:
    status = "Kurus"
elif bmi < 25:
    status = "Normal"
elif bmi < 30:
    status = "Gemuk"
else:
    status = "Obesitas"

if jk.upper() == "L":
    bmr = 66 + (13.7 * berat) + (5 * tinggi_cm) - (6.8 * usia)
else:
    bmr = 655 + (9.6 * berat) + (1.8 * tinggi_cm) - (4.7 * usia)

kalori = bmr * 1.55  # aktivitas sedang

print(f"BMI: {bmi:.2f} ({status})")
print(f"Kebutuhan kalori harian: {kalori:.0f} kkal")
```

**Tugas Anda:** Refactor kode prosedural di atas menjadi kode **modular berbasis fungsi**. Minimum harus ada **tiga fungsi** berikut dengan parameter dan return value yang jelas:

1. `hitung_bmi(berat, tinggi_cm) -> float` — mengembalikan nilai BMI.
2. `klasifikasi_bmi(bmi) -> str` — mengembalikan status ("Kurus"/"Normal"/"Gemuk"/"Obesitas").
3. `hitung_kalori(berat, tinggi_cm, usia, jk, faktor_aktivitas=1.55) -> float` — mengembalikan kebutuhan kalori harian (gunakan default parameter untuk faktor aktivitas).

Tuliskan kode hasil refactor **secara utuh** (termasuk pemanggilan fungsi di blok utama yang memproses input dan mencetak hasil), lalu jelaskan **singkat (2-3 kalimat)** manfaat modularitas yang Anda capai dibandingkan versi prosedural.

---

> **Sub-CPMK 2.x s/d 5.x (integratif)** — Integrasi variabel, seleksi, perulangan, dan fungsi pada kasus realistis
> *Level Bloom:* C5 · *Konteks:* Indonesia (sistem antrean puskesmas)

**E5. (12 poin)** Anda diminta merancang *sistem antrean puskesmas* sederhana dengan aturan berikut:

- Pasien mendaftar dengan memasukkan **nama** dan **kategori prioritas** (`"lansia"`, `"hamil"`, `"anak"`, atau `"umum"`).
- Pasien berkategori `"lansia"`, `"hamil"`, atau `"anak"` masuk ke **antrean prioritas**; pasien `"umum"` masuk ke **antrean reguler**.
- Sistem dapat **memanggil pasien berikutnya** — selalu prioritaskan antrean prioritas sampai kosong, baru panggil reguler.
- Sistem menerima perintah berulang dari petugas: `daftar`, `panggil`, atau `selesai` (menghentikan sistem).

**Tugas Anda:**

a) Tuliskan **pseudocode** algoritma utamanya (bahasa Indonesia semi-formal, minimal 10 langkah). **(4 poin)**

b) Tuliskan implementasi **Python** yang memenuhi spesifikasi, mencakup minimal: (i) deklarasi variabel/struktur data yang tepat, (ii) struktur seleksi (`if/elif/else`) untuk klasifikasi prioritas, (iii) perulangan (`while`) untuk menerima perintah petugas, dan (iv) minimal **dua fungsi** dengan parameter & return (misal `daftar_pasien()` dan `panggil_berikutnya()`). **(8 poin)**

---

## Penutup

> *"Barang siapa menempuh suatu jalan untuk mencari ilmu, niscaya Allah akan memudahkan baginya jalan menuju surga."*
> — **HR. Muslim**

**"Man jadda wajada"** — Siapa bersungguh-sungguh, pasti berhasil.

**~ Selamat Mengerjakan — Jazakumullahu khairan ~**
