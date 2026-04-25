---
mata_kuliah: Algoritma dan Pemrograman
kode_mk: INF-101
sks: 2 SKS (Teori)
semester: Genap 2025/2026
jenis: UTS
---

# UJIAN TENGAH SEMESTER (UTS)
## Semester Genap Tahun Akademik 2025/2026

### KUNCI JAWABAN, RUBRIK PENSKORAN & PEMETAAN CPMK

> **RAHASIA — HANYA UNTUK DOSEN/ASISTEN PENGAMPU**

> *"Sesungguhnya Allah menyuruh kamu menyampaikan amanat kepada yang berhak menerimanya, dan (menyuruh kamu) apabila menetapkan hukum di antara manusia supaya kamu menetapkan dengan adil."*
> — **QS An-Nisa: 58**

**UNIVERSITAS AL AZHAR INDONESIA**
**Fakultas Sains dan Teknologi — Program Studi Informatika**

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

## BAGIAN I — KUNCI PILIHAN GANDA (40 poin)

### PG No. 1

**Sub-CPMK:** CPMK-1.1 — Mendefinisikan konsep algoritma, sejarah perkembangannya, dan relevansinya dalam kehidupan sehari-hari
**Level Bloom:** C2
**Konteks:** Umum

**Jawaban:** E

**Pembahasan:**
Sifat wajib algoritma klasik (Knuth) meliputi: *finiteness* (berakhir dalam langkah terbatas), *definiteness* (tiap langkah jelas & tidak ambigu), *input* (nol atau lebih), *output* (satu atau lebih), serta *effectiveness* (setiap langkah dapat dieksekusi). *Randomness* **bukan** sifat wajib — banyak algoritma justru deterministik. Distraktor A–D adalah sifat wajib yang benar dan karena itu tidak bisa menjadi jawaban.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 2

**Sub-CPMK:** CPMK-1.2 — Menjelaskan empat pilar computational thinking: dekomposisi, pengenalan pola, abstraksi, dan desain algoritma
**Level Bloom:** C3
**Konteks:** JTBD (manajemen waktu belajar)

**Jawaban:** B

**Pembahasan:**
Membagi aktivitas harian menjadi bagian-bagian kecil yang dapat dijadwalkan satu per satu adalah definisi tepat **dekomposisi** — memecah masalah besar menjadi sub-masalah. Distraktor A (abstraksi) tentang menyembunyikan detail; C (pengenalan pola) tentang menemukan kemiripan; D (desain algoritma) baru muncul setelah dekomposisi. E (evaluasi) bukan pilar CT.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 3

**Sub-CPMK:** CPMK-1.3 — Menjelaskan peran Python dan AI dalam ekosistem pemrograman modern serta hubungan dengan mata kuliah ko-requisite Analisis Data Statistik
**Level Bloom:** C2
**Konteks:** Umum

**Jawaban:** D

**Pembahasan:**
Python justru **bukan** bahasa tercepat — bahasa seperti C/C++/Rust unggul dari sisi raw performance. Keunggulan Python adalah produktivitas dan ekosistem (A, B, C, E), bukan kecepatan mentah. Distraktor B (ekosistem pustaka ilmiah) dan E (TensorFlow/PyTorch) adalah fakta akurat yang tidak bisa menjadi jawaban karena soal meminta pernyataan yang **salah/kecuali**.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 4

**Sub-CPMK:** CPMK-2.1 — Mengidentifikasi dan menggunakan variabel, konstanta, dan aturan penamaan (naming convention) di Python
**Level Bloom:** C2
**Konteks:** Umum

**Jawaban:** C

**Pembahasan:**
PEP 8 merekomendasikan *snake_case* untuk variabel biasa: `total_harga`. Distraktor A (`TotalHarga`) adalah *PascalCase* yang disediakan untuk kelas, bukan variabel. B memakai tanda hubung (`-`) yang ditafsirkan Python sebagai operator minus. D diawali angka (ilegal). E mengandung simbol `@` (ilegal).

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 5

**Sub-CPMK:** CPMK-2.2 — Membedakan tipe data dasar (int, float, str, bool) dan melakukan konversi tipe (type casting)
**Level Bloom:** C3
**Konteks:** Umum

**Jawaban:** B

**Pembahasan:**
`int("10")` menghasilkan `10` (int); `10 + 3` = `13` (int). Jadi `z` bertipe `int` dan bernilai `13`. Distraktor A (`"103"`) akan muncul jika tidak dicasting, yaitu `"10" + "3"` — namun di sini `x` sudah diubah ke `int` dulu. D salah karena setelah penjumlahan int+int tidak menjadi str. C salah karena tidak ada operasi `float`.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 6

**Sub-CPMK:** CPMK-2.2 — Membedakan tipe data dasar (int, float, str, bool) dan melakukan konversi tipe (type casting)
**Level Bloom:** C3
**Konteks:** Umum

**Jawaban:** B

**Pembahasan:**
`float("7")` → `7.0` (float); `bool(0)` → `False` (tipe `bool`); `str(a)` → `"7.0"` (str). Output: `<class 'float'> <class 'bool'> <class 'str'>`. Distraktor C keliru menyatakan `bool(0)` sebagai `int` — sebenarnya `bool` adalah subclass `int` tetapi `type()` tetap mengembalikan `bool`. D salah karena `a` bertipe `float` bukan `str`.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 7

**Sub-CPMK:** CPMK-2.3 — Menerapkan operator aritmatika, perbandingan, logika, dan assignment dalam ekspresi komputasi
**Level Bloom:** C3
**Konteks:** Umum

**Jawaban:** B

**Pembahasan:**
Urutan presedensi: `**` (16) → `*` & `//` kiri-ke-kanan → `+` & `-` kiri-ke-kanan.
- `4 ** 2 = 16`
- `3 * 16 = 48`, `48 // 5 = 9`
- `2 + 9 = 11`, `11 - 1 = 10` → jawaban **10**.
Distraktor A (9) terjadi jika `- 1` dievaluasi lebih dulu dari `+`. C (11) lupa mengurangi 1. D/E terjadi jika urutan presedensi dilanggar.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 8

**Sub-CPMK:** CPMK-2.3 — Menerapkan operator aritmatika, perbandingan, logika, dan assignment dalam ekspresi komputasi
**Level Bloom:** C4
**Konteks:** Umum

**Jawaban:** A

**Pembahasan:**
Python memakai **short-circuit evaluation**. Pada `x and cek()`: karena `x = False`, operator `and` langsung mengembalikan `False` tanpa memanggil `cek()`. Pada `True or cek()`: karena operand kiri `True`, operator `or` langsung mengembalikan `True` tanpa memanggil `cek()`. Jadi `cek()` tidak pernah dipanggil → 0 kali. Distraktor C (2) adalah jawaban bagi yang tidak memahami short-circuit.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 9

**Sub-CPMK:** CPMK-2.4 — Menerapkan fungsi input/output untuk interaksi program sederhana
**Level Bloom:** C3
**Konteks:** JTBD (form belanja online)

**Jawaban:** B

**Pembahasan:**
`input()` selalu mengembalikan `str`, sehingga `"100" * "2"` akan error (tidak bisa mengalikan dua string). Koreksi yang benar adalah mengkonversi ke `int` lalu mengalikan: `int(harga) * int(jumlah)`. Distraktor D salah karena Python TIDAK otomatis mendeteksi angka dari `input()`. C memperburuk masalah (concatenation str+int error). E tidak menyelesaikan akar masalah perkalian.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 10

**Sub-CPMK:** CPMK-3.1 — Menerapkan struktur seleksi if, elif, else untuk pengambilan keputusan dalam program
**Level Bloom:** C3
**Konteks:** Islami (kalkulasi zakat mal 2,5%)

**Jawaban:** C

**Pembahasan:**
`harta = 90_000_000` dan `nisab = 85_000_000`, sehingga kondisi `harta >= nisab` benar. Zakat = `90_000_000 * 0.025 = 2_250_000.0`. Output: `Wajib zakat: 2250000.0`. Distraktor B (`2125000`) terjadi jika salah hitung `85jt * 0.025`. D (`2500000`) jika harta dibaca sebagai `100_000_000`. E adalah kesalahan desimal tiga digit.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 11

**Sub-CPMK:** CPMK-3.2 — Merancang struktur seleksi bertingkat (nested) dan multi-kondisi untuk kasus yang kompleks
**Level Bloom:** C4
**Konteks:** Indonesia (grade IP UAI)

**Jawaban:** B

**Pembahasan:**
Evaluasi berurutan: `78 >= 85` salah, `78 >= 80` salah, `78 >= 75` **benar** → `grade = "B+"`. Cabang berikutnya tidak dievaluasi karena `elif` sudah terpicu. Distraktor C (`B`) adalah kesalahan umum yang mengabaikan threshold `>= 75` untuk B+. A (`A-`) mengira 78 ≥ 80.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 12

**Sub-CPMK:** CPMK-3.3 — Menerapkan match-case statement (Python 3.10+) sebagai alternatif seleksi
**Level Bloom:** C3
**Konteks:** Umum

**Jawaban:** A

**Pembahasan:**
`hari = "Senin"` cocok dengan pola pertama (`"Senin" | "Selasa" | ... | "Jumat"`) sehingga `kategori = "Hari kerja"`. Distraktor E (`SyntaxError`) keliru — `match-case` valid di Python 3.10+. C (`Tidak dikenal`) hanya terjadi jika string tidak cocok dengan pola mana pun.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 13

**Sub-CPMK:** CPMK-4.1 — Menerapkan perulangan for dengan range() dan iterasi koleksi
**Level Bloom:** C3
**Konteks:** Umum

**Jawaban:** B

**Pembahasan:**
`range(2, 20, 3)` menghasilkan `2, 5, 8, 11, 14, 17` — **6 nilai** (stop `20` eksklusif). Rumus jumlah iterasi: `ceil((stop - start) / step) = ceil((20-2)/3) = ceil(6) = 6`. Distraktor A (5) salah menghitung nilai terakhir, C (7) salah memasukkan `20` yang seharusnya eksklusif.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 14

**Sub-CPMK:** CPMK-4.2 — Menerapkan perulangan while dengan kondisi berhenti yang tepat
**Level Bloom:** C4
**Konteks:** Umum

**Jawaban:** C

**Pembahasan:**
`n` dimulai dari 10 dan bertambah 1 tiap iterasi (`n = n + 1`), sehingga kondisi `n > 0` selalu bernilai benar — **infinite loop**. Distraktor A keliru karena asumsi `n` menurun, padahal kode menambahkan. D salah karena Python 3 tidak memiliki batas maksimum integer (int Python arbitrary precision). E salah: `n` dimodifikasi, hanya arahnya salah.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 15

**Sub-CPMK:** CPMK-4.3 — Menggunakan break, continue, dan perulangan bertingkat (nested loop) untuk kontrol alur lanjutan
**Level Bloom:** C4
**Konteks:** Umum

**Jawaban:** C

**Pembahasan:**
Trace eksekusi:
- `i=1`: `j=1` → total += 1*1 = 1; `j=2` → continue; `j=3` → total += 1*3 = 3 → total=4.
- `i=2`: `j=1` → total += 2*1 = 2 → total=6; `j=2` → continue; `j=3` → total += 2*3 = 6 → total=12.
- `i=3`: `j=1` → bukan 2, cek `i==3` → **break** (keluar loop dalam). `i=3` tidak menambah apa-apa.

Total akhir = **12**. Distraktor B (10) terjadi jika salah hitung iterasi `i=2`; D (16) jika `break` diabaikan.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 16

**Sub-CPMK:** CPMK-4.4 — Menerapkan pola akumulator, penghitung (counter), dan flag dalam perulangan
**Level Bloom:** C3
**Konteks:** JTBD (rekap pengeluaran harian — akumulator)

**Jawaban:** B

**Pembahasan:**
Pola akumulator klasik: inisialisasi `total = 0` lalu di tiap iterasi tambahkan elemen ke akumulator (`total = total + x`). Distraktor A hanya meng-*assign* ulang, bukan menjumlahkan. C memakai `total = 1` dan perkalian (ini pola produk, bukan jumlah). D tidak menginisialisasi `total` → `NameError` di iterasi pertama. E inisialisasi `total` sebagai list lalu menambahkan int → `TypeError`.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 17

**Sub-CPMK:** CPMK-5.1 — Mendefinisikan dan memanggil fungsi dengan parameter dan nilai kembalian (return value)
**Level Bloom:** C2
**Konteks:** Umum

**Jawaban:** B

**Pembahasan:**
Istilah resmi: identifier di *signature* fungsi disebut **parameter** (`panjang`, `lebar`), sedangkan nilai yang dilewatkan saat pemanggilan disebut **argument** (`5`, `3`). `5 * 3 = 15` dikembalikan via `return`. Distraktor A membalik definisi; C salah karena `return` bekerja tanpa butuh `print`; D salah karena Python *dynamically typed*; E salah karena `return` tidak tergantung loop.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 18

**Sub-CPMK:** CPMK-5.2 — Menjelaskan konsep scope (lokal vs global) dan lifetime variabel
**Level Bloom:** C4
**Konteks:** Umum

**Jawaban:** C

**Pembahasan:**
Penugasan `x = 5` di dalam `ubah()` membuat variabel **lokal** baru bernama `x` — tidak memengaruhi `x` global. Jadi `dalam: 5` (local), `luar: 10` (global). Distraktor A keliru karena mengira `x` di dalam fungsi otomatis memodifikasi global (harus pakai `global x` eksplisit). E salah karena Python tidak mensyaratkan deklarasi `global` untuk membuat variabel lokal.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 19

**Sub-CPMK:** CPMK-5.3 — Menerapkan fungsi lambda, default parameter, dan variable-length arguments (*args, **kwargs)
**Level Bloom:** C3
**Konteks:** Umum

**Jawaban:** C

**Pembahasan:**
`*angka` menangkap semua positional arguments ke dalam tuple `(1, 2, 3, 4)`. `sum((1,2,3,4)) = 10`. Distraktor D adalah tuple mentah yang belum di-sum. E salah karena lambda **boleh** memakai `*args`.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 20

**Sub-CPMK:** CPMK-5.4 — Menerapkan prinsip modularitas dan code reuse melalui pengorganisasian fungsi
**Level Bloom:** C4
**Konteks:** Umum

**Jawaban:** B

**Pembahasan:**
Prinsip DRY (*Don't Repeat Yourself*) jelas dilanggar: rumus `3.14 * r * r` ditulis tiga kali, dan konstanta `3.14` tersebar sebagai *magic number*. Solusi modular: bungkus ke fungsi `luas_lingkaran(r)` dan panggil ulang, plus ambil `math.pi` sebagai konstanta. Distraktor A menyangkal adanya duplikasi (salah). C/D/E adalah saran yang justru memperburuk atau tidak relevan.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

## BAGIAN II — KUNCI ESAI (60 poin)

### Esai No. E1

**Sub-CPMK:** CPMK-1.2 — Menjelaskan empat pilar computational thinking: dekomposisi, pengenalan pola, abstraksi, dan desain algoritma
**Level Bloom:** C3
**Konteks:** JTBD (merancang rutinitas belajar efektif)

**Jawaban Ideal:**

**a) Definisi empat pilar:**
1. **Dekomposisi** — memecah masalah besar menjadi sub-masalah yang lebih kecil dan mudah diselesaikan.
2. **Pengenalan pola** — menemukan kemiripan, tren, atau pola berulang antara beberapa masalah atau data.
3. **Abstraksi** — menyaring detail yang penting dan menyembunyikan detail yang tidak relevan untuk menyederhanakan representasi masalah.
4. **Desain algoritma** — menyusun langkah-langkah sistematis yang dapat diikuti untuk menyelesaikan masalah.

**b) Penerapan ke "rutinitas belajar harian efektif":**
1. **Dekomposisi:** Pecah "belajar efektif" menjadi komponen konkret: membaca bahan, mengerjakan latihan, mereview catatan, istirahat, dan evaluasi harian.
2. **Pengenalan pola:** Amati waktu produktif pribadi (misal lebih fokus pagi hari), topik yang sering muncul di tugas, atau pola energi menurun setelah 90 menit.
3. **Abstraksi:** Fokus pada variabel kunci (jam belajar, durasi sesi, jenis aktivitas) dan abaikan detail tidak relevan (misal warna buku).
4. **Desain algoritma:** Susun urutan: (1) mulai pukul 08.00 baca materi 45 menit → (2) latihan 30 menit → (3) istirahat 15 menit → (4) review 20 menit → ulangi siklus.

**Rubrik Penskoran (Total 12 poin):**

| Kriteria | Poin |
|---|---|
| Menyebutkan & mendefinisikan 4 pilar dengan benar (a) | 4 |
| Menerapkan 4 pilar ke kasus "rutinitas belajar" dengan contoh relevan (b) | 4 |
| Koherensi & kejelasan argumentasi (keterkaitan a ke b) | 2 |
| Kedalaman dan kebenaran teknis contoh konkret | 2 |

**Aturan Partial Credit:**
- 3 pilar terdefinisi benar → maksimum 3/4 poin bagian (a).
- 2 pilar terdefinisi benar → maksimum 2/4 poin bagian (a).
- Contoh penerapan tidak relevan dengan pilar (mis. menyebut "pengenalan pola" tapi contohnya dekomposisi) → -1 poin per pilar, maksimum -3 untuk (b).
- Hanya definisi tanpa contoh penerapan → maksimum 6/12 poin total.
- Sekadar menyebut nama pilar tanpa definisi/contoh → maksimum 2/12 poin.

---

### Esai No. E2

**Sub-CPMK:** CPMK-3.1 & 3.2 — Menerapkan struktur seleksi if/elif/else; Merancang struktur seleksi bertingkat (nested) dan multi-kondisi
**Level Bloom:** C3
**Konteks:** Islami (klasifikasi nisab zakat mal)

**Jawaban Ideal:**

```python
# Program klasifikasi zakat mal berdasarkan nisab
harta = float(input("Masukkan jumlah harta (Rp): "))
nisab = float(input("Masukkan nilai nisab (Rp, setara 85 gram emas): "))

if harta < 0:
    # Cabang 1: input tidak valid
    print("Input tidak valid")
elif harta < nisab:
    # Cabang 2: belum mencapai nisab
    print("Belum wajib zakat")
elif harta < 2 * nisab:
    # Cabang 3: kategori standar (nisab <= harta < 2*nisab)
    zakat = harta * 0.025
    print("Wajib zakat (kategori standar)")
    print(f"Jumlah zakat: Rp {zakat:,.2f}")
else:
    # Cabang 4: harta >= 2 * nisab
    zakat = harta * 0.025
    print("Wajib zakat (kategori besar, pertimbangkan zakat tambahan)")
    print(f"Jumlah zakat: Rp {zakat:,.2f}")
```

**Rubrik Penskoran (Total 12 poin):**

| Kriteria | Poin |
|---|---|
| Input `harta` & `nisab` dengan konversi tipe `float`/`int` yang tepat | 2 |
| Keempat cabang (`<0`, `<nisab`, `<2*nisab`, `>=2*nisab`) tercakup semua | 4 |
| Urutan `if/elif/else` logis (tidak ada cabang tertutup oleh cabang sebelumnya) | 2 |
| Perhitungan `zakat = harta * 0.025` benar & tercetak di dua cabang wajib | 2 |
| Pesan output sesuai spesifikasi (kata persis atau padanan jelas) | 1 |
| Komentar singkat di tiap cabang | 1 |

**Aturan Partial Credit:**
- Kurang satu cabang (misal tidak menangani `harta < 0`) → -1 poin.
- Operator perbandingan salah (`>` bukan `>=` di threshold nisab sehingga `harta == nisab` masuk cabang keliru) → -1 poin.
- Menghitung zakat dengan persentase salah (mis. 2% atau 25%) → -2 poin di kriteria perhitungan.
- Memakai `if` berturut-turut tanpa `elif` sehingga beberapa cabang dobel terpicu → -2 poin di kriteria urutan logis.
- Tidak ada komentar → -1 poin; tidak ada `input()` (nilai di-*hardcode*) → -2 poin.
- Sintaks Python tidak valid (program tidak bisa dijalankan) → maksimum 8/12.

---

### Esai No. E3

**Sub-CPMK:** CPMK-4.1 & 4.4 — Menerapkan perulangan for dengan range(); Menerapkan pola akumulator, penghitung, dan flag
**Level Bloom:** C4
**Konteks:** Indonesia (data jumlah penduduk per provinsi)

**Jawaban Ideal (output baris per baris):**

State awal: `total=0`, `terbanyak=10_600_000`, `nama_terbanyak="DKI Jakarta"`.

- **Iterasi i=0** (DKI Jakarta, 10.600.000):
  - `total = 0 + 10_600_000 = 10_600_000`
  - `10_600_000 > 10_600_000`? Tidak → `terbanyak` & `nama_terbanyak` tidak berubah.
  - Output: `Iterasi 0: total sementara = 10600000, sementara terbanyak = DKI Jakarta`
- **Iterasi i=1** (Jawa Barat, 48.200.000):
  - `total = 10_600_000 + 48_200_000 = 58_800_000`
  - `48_200_000 > 10_600_000`? Ya → `terbanyak = 48_200_000`, `nama_terbanyak = "Jawa Barat"`.
  - Output: `Iterasi 1: total sementara = 58800000, sementara terbanyak = Jawa Barat`
- **Iterasi i=2** (Jawa Tengah, 36.500.000):
  - `total = 58_800_000 + 36_500_000 = 95_300_000`
  - `36_500_000 > 48_200_000`? Tidak → tidak berubah.
  - Output: `Iterasi 2: total sementara = 95300000, sementara terbanyak = Jawa Barat`
- **Iterasi i=3** (DI Yogyakarta, 3.700.000):
  - `total = 95_300_000 + 3_700_000 = 99_000_000`
  - `3_700_000 > 48_200_000`? Tidak → tidak berubah.
  - Output: `Iterasi 3: total sementara = 99000000, sementara terbanyak = Jawa Barat`
- **Iterasi i=4** (Banten, 11.900.000):
  - `total = 99_000_000 + 11_900_000 = 110_900_000`
  - `11_900_000 > 48_200_000`? Tidak → tidak berubah.
  - Output: `Iterasi 4: total sementara = 110900000, sementara terbanyak = Jawa Barat`

Setelah loop: `rata_rata = 110_900_000 / 5 = 22_180_000.0`.

**Output final (3 baris terakhir):**
```
Total penduduk = 110900000
Rata-rata = 22180000.0
Provinsi terbanyak = Jawa Barat (48200000 jiwa)
```

**Rubrik Penskoran (Total 12 poin):**

| Kriteria | Poin |
|---|---|
| 5 baris output iterasi dengan nilai `total` akumulatif benar | 5 |
| Identifikasi `nama_terbanyak` yang tepat di tiap iterasi | 3 |
| Tiga baris output final (total, rata-rata, provinsi terbanyak) benar | 3 |
| Urutan dan format output sesuai (nilai bulat, urut iterasi 0→4) | 1 |

**Aturan Partial Credit:**
- Total akumulatif salah di satu iterasi tetapi iterasi berikutnya konsisten dengan kesalahan tersebut → hanya -1 poin.
- Lupa bahwa iterasi dimulai dari `i=0` (menulis `Iterasi 1..5`) → -1 poin.
- Nilai `rata_rata` dihitung tapi pembagi salah (mis. bagi 4) → -1 poin.
- Lupa bahwa `>` bukan `>=` sehingga saat nilai sama `terbanyak` berubah → -2 poin.
- Hanya menuliskan output akhir tanpa trace iterasi → maksimum 4/12 poin.

---

### Esai No. E4

**Sub-CPMK:** CPMK-5.1 & 5.4 — Mendefinisikan dan memanggil fungsi dengan parameter & return; Menerapkan prinsip modularitas dan code reuse
**Level Bloom:** C5
**Konteks:** JTBD (kalkulator BMI & kebutuhan kalori)

**Jawaban Ideal:**

```python
def hitung_bmi(berat: float, tinggi_cm: float) -> float:
    """Mengembalikan nilai BMI dari berat (kg) & tinggi (cm)."""
    tinggi_m = tinggi_cm / 100
    return berat / (tinggi_m * tinggi_m)

def klasifikasi_bmi(bmi: float) -> str:
    """Mengembalikan status BMI: Kurus / Normal / Gemuk / Obesitas."""
    if bmi < 18.5:
        return "Kurus"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Gemuk"
    else:
        return "Obesitas"

def hitung_kalori(berat: float, tinggi_cm: float, usia: int, jk: str,
                  faktor_aktivitas: float = 1.55) -> float:
    """Mengembalikan kebutuhan kalori harian (kkal) berdasarkan BMR Harris-Benedict
    dikalikan faktor aktivitas (default 1.55 = aktivitas sedang)."""
    if jk.upper() == "L":
        bmr = 66 + (13.7 * berat) + (5 * tinggi_cm) - (6.8 * usia)
    else:
        bmr = 655 + (9.6 * berat) + (1.8 * tinggi_cm) - (4.7 * usia)
    return bmr * faktor_aktivitas

# Blok utama
def main():
    berat = float(input("Berat (kg): "))
    tinggi_cm = float(input("Tinggi (cm): "))
    usia = int(input("Usia: "))
    jk = input("Jenis kelamin (L/P): ")

    bmi = hitung_bmi(berat, tinggi_cm)
    status = klasifikasi_bmi(bmi)
    kalori = hitung_kalori(berat, tinggi_cm, usia, jk)

    print(f"BMI: {bmi:.2f} ({status})")
    print(f"Kebutuhan kalori harian: {kalori:.0f} kkal")

main()
```

**Manfaat modularitas (2-3 kalimat):**
Dengan fungsi, tiap perhitungan dapat diuji dan dipanggil kembali tanpa duplikasi kode (prinsip DRY). Jika rumus BMR berubah, modifikasi cukup dilakukan di satu tempat — lebih mudah dipelihara. Selain itu, default parameter `faktor_aktivitas=1.55` memungkinkan penggunaan kembali untuk level aktivitas berbeda (1.2 ringan, 1.75 berat) tanpa menulis ulang logika.

**Rubrik Penskoran (Total 12 poin):**

| Kriteria | Poin |
|---|---|
| `hitung_bmi(berat, tinggi_cm)` benar, mengembalikan `float` | 2 |
| `klasifikasi_bmi(bmi)` benar, mengembalikan string sesuai rentang | 2 |
| `hitung_kalori(...)` benar, mencakup cabang L/P & default parameter | 3 |
| Pemanggilan fungsi di blok utama dengan input & output yang tepat | 2 |
| Kode hasil refactor dapat dijalankan tanpa error (sintaks valid) | 2 |
| Penjelasan manfaat modularitas (jelas, 2-3 kalimat) | 1 |

**Aturan Partial Credit:**
- Kurang satu fungsi dari tiga yang diwajibkan → -3 poin.
- Fungsi tidak memakai `return` (pakai `print` di dalam fungsi) → -1 per fungsi, maksimum -3.
- Tidak memakai default parameter untuk `faktor_aktivitas` → -1 poin.
- Logika klasifikasi BMI salah (threshold tertukar) → -1 poin di kriteria klasifikasi.
- Tidak ada penjelasan manfaat modularitas → -1 poin.
- Kode tidak bisa dijalankan karena `SyntaxError` → maksimum 8/12.

---

### Esai No. E5

**Sub-CPMK:** CPMK-2.x s/d 5.x (integratif) — Integrasi variabel, seleksi, perulangan, dan fungsi pada kasus realistis (*merujuk ke sub-CPMK 2.1, 2.3, 2.4, 3.1, 4.2, 5.1*)
**Level Bloom:** C5
**Konteks:** Indonesia (sistem antrean puskesmas)

**Jawaban Ideal:**

**a) Pseudocode (minimal 10 langkah):**

```
1.  Inisialisasi antrean_prioritas = [] dan antrean_reguler = []
2.  Cetak menu: "daftar / panggil / selesai"
3.  WHILE perintah != "selesai":
4.      BACA perintah dari petugas
5.      IF perintah == "daftar":
6.          BACA nama pasien
7.          BACA kategori (lansia / hamil / anak / umum)
8.          JIKA kategori IN {lansia, hamil, anak}: tambahkan ke antrean_prioritas
9.          SELAIN ITU: tambahkan ke antrean_reguler
10.     ELSE IF perintah == "panggil":
11.         JIKA antrean_prioritas tidak kosong: panggil elemen pertama dari antrean_prioritas
12.         ELSE JIKA antrean_reguler tidak kosong: panggil elemen pertama dari antrean_reguler
13.         ELSE: cetak "Antrean kosong"
14.     ELSE IF perintah == "selesai": hentikan loop
15.     ELSE: cetak "Perintah tidak dikenal"
16. Cetak ringkasan sisa antrean sebelum program berakhir
```

**b) Implementasi Python:**

```python
# Sistem antrean puskesmas sederhana
antrean_prioritas = []
antrean_reguler = []

def daftar_pasien(nama: str, kategori: str) -> str:
    """Menambahkan pasien ke antrean sesuai kategori. Mengembalikan pesan status."""
    kategori = kategori.lower().strip()
    if kategori in ("lansia", "hamil", "anak"):
        antrean_prioritas.append(nama)
        return f"{nama} ({kategori}) masuk ANTREAN PRIORITAS."
    elif kategori == "umum":
        antrean_reguler.append(nama)
        return f"{nama} masuk ANTREAN REGULER."
    else:
        return "Kategori tidak dikenal — pendaftaran dibatalkan."

def panggil_berikutnya() -> str:
    """Memanggil pasien berikutnya, prioritas dulu. Mengembalikan pesan panggilan."""
    if len(antrean_prioritas) > 0:
        pasien = antrean_prioritas.pop(0)
        return f"Panggil (PRIORITAS): {pasien}"
    elif len(antrean_reguler) > 0:
        pasien = antrean_reguler.pop(0)
        return f"Panggil (REGULER): {pasien}"
    else:
        return "Antrean kosong."

# Loop utama petugas
print("Sistem Antrean Puskesmas — perintah: daftar / panggil / selesai")
while True:
    perintah = input("Perintah: ").lower().strip()
    if perintah == "daftar":
        nama = input("Nama pasien: ")
        kategori = input("Kategori (lansia/hamil/anak/umum): ")
        print(daftar_pasien(nama, kategori))
    elif perintah == "panggil":
        print(panggil_berikutnya())
    elif perintah == "selesai":
        print("Sistem berhenti. Sisa prioritas:", antrean_prioritas,
              "| Sisa reguler:", antrean_reguler)
        break
    else:
        print("Perintah tidak dikenal.")
```

**Rubrik Penskoran (Total 12 poin):**

| Kriteria | Poin |
|---|---|
| (a) Pseudocode minimal 10 langkah, logika lengkap (daftar, panggil, stop) | 4 |
| (b.i) Variabel/struktur data tepat (dua list terpisah atau setara) | 1 |
| (b.ii) Struktur seleksi `if/elif/else` untuk klasifikasi prioritas | 2 |
| (b.iii) Perulangan `while` menerima perintah berulang dengan kondisi berhenti | 2 |
| (b.iv) Minimal dua fungsi dengan parameter & return yang valid | 2 |
| Kode Python konsisten dengan pseudocode & dapat dijalankan | 1 |

**Aturan Partial Credit:**
- Pseudocode < 10 langkah → -1 poin per 2 langkah yang kurang, maksimum -3.
- Hanya satu fungsi (bukan dua) → -1 poin; nol fungsi (semua di *main scope*) → -2 poin.
- Antrean prioritas & reguler digabung dalam satu list tanpa mekanisme prioritas → -2 poin (b.i/b.ii).
- Tidak ada kondisi berhenti `while` (infinite loop) → -1 poin di (b.iii).
- Kode hanya mengimplementasi `daftar` tanpa `panggil` (atau sebaliknya) → -2 poin.
- `SyntaxError` serius yang menghalangi eksekusi → maksimum 8/12.
- Hanya menulis pseudocode tanpa kode Python → maksimum 6/12 (penilaian penuh hanya pada bagian a).

---

## RINGKASAN DISTRIBUSI

### Tabel A — Pemetaan Sub-CPMK → No. Soal → Poin

| Sub-CPMK | Deskripsi Singkat                                                   | Nomor Soal          | Total Poin |
|----------|----------------------------------------------------------------------|---------------------|------------|
| CPMK-1.1 | Definisi algoritma & sejarah                                         | PG #1               | 2          |
| CPMK-1.2 | Empat pilar computational thinking                                   | PG #2, E1           | 14         |
| CPMK-1.3 | Peran Python & AI dalam ekosistem modern                             | PG #3               | 2          |
| CPMK-2.1 | Variabel, konstanta, naming convention PEP 8                         | PG #4, E5 (bagian)  | 2          |
| CPMK-2.2 | Tipe data dasar & type casting                                       | PG #5, PG #6        | 4          |
| CPMK-2.3 | Operator aritmatika/logika/perbandingan                              | PG #7, PG #8, E5    | 4          |
| CPMK-2.4 | Input/output interaktif                                              | PG #9, E5 (bagian)  | 2          |
| CPMK-3.1 | if/elif/else untuk pengambilan keputusan                             | PG #10, E2, E5      | 14         |
| CPMK-3.2 | Nested & multi-kondisi                                               | PG #11, E2          | 2          |
| CPMK-3.3 | match-case statement                                                 | PG #12              | 2          |
| CPMK-4.1 | for dengan range() & iterasi koleksi                                 | PG #13, E3          | 14         |
| CPMK-4.2 | while & kondisi berhenti                                             | PG #14, E5 (bagian) | 2          |
| CPMK-4.3 | break/continue & nested loop                                         | PG #15              | 2          |
| CPMK-4.4 | Pola akumulator/counter/flag                                         | PG #16, E3          | 2          |
| CPMK-5.1 | Fungsi, parameter, return value                                      | PG #17, E4, E5      | 14         |
| CPMK-5.2 | Scope lokal vs global                                                | PG #18              | 2          |
| CPMK-5.3 | Lambda, default parameter, *args/**kwargs                            | PG #19              | 2          |
| CPMK-5.4 | Modularitas & code reuse                                             | PG #20, E4          | 14         |
| **TOTAL**|                                                                      |                     | **100**    |

*Catatan: Poin Esai dialokasikan ke sub-CPMK "anchor" primernya untuk menghindari double-counting. E1 (12) → CPMK-1.2; E2 (12) → CPMK-3.1; E3 (12) → CPMK-4.1; E4 (12) → CPMK-5.4; E5 (12) → CPMK-5.1. Kolom "Nomor Soal" tetap menyebut seluruh sub-CPMK yang ikut terukur dalam soal tersebut.*

### Tabel B — Distribusi Level Bloom

| Level | Jumlah Soal | Bobot Poin | Persen Poin |
|-------|-------------|------------|-------------|
| C2    | 4           | 8          | 8%          |
| C3    | 12          | 44         | 44%         |
| C4    | 7           | 24         | 24%         |
| C5    | 2           | 24         | 24%         |
| **TOTAL** | **25**  | **100**    | **100%**    |

**Rincian per soal:**
- **C2 (4 soal, 8 poin):** PG #1, PG #3, PG #4, PG #17 (4 × 2 pt = 8 pt).
- **C3 (12 soal, 44 poin):** PG #2, PG #5, PG #6, PG #7, PG #9, PG #10, PG #12, PG #13, PG #16, PG #19 (10 × 2 pt = 20 pt) + E1 (12 pt) + E2 (12 pt) = 44 pt.
- **C4 (7 soal, 24 poin):** PG #8, PG #11, PG #14, PG #15, PG #18, PG #20 (6 × 2 pt = 12 pt) + E3 (12 pt) = 24 pt.
- **C5 (2 soal, 24 poin):** E4 (12 pt) + E5 (12 pt) = 24 pt.

*Catatan: Distribusi soal mengikuti blueprint spec §5.1 — target C2=4, C3≈11, C4≈8, C5=2 dengan toleransi ±1 soal per level. Persen poin berbeda dari persen jumlah soal karena Esai (@12 pt) lebih berat dari PG (@2 pt).*

### Tabel C — Distribusi Konteks

| Konteks           | Jumlah Soal | Bobot Poin | Nomor Soal                                                                 |
|-------------------|-------------|------------|----------------------------------------------------------------------------|
| Umum              | 15          | 30         | PG #1, #3, #4, #5, #6, #7, #8, #12, #13, #14, #15, #17, #18, #19, #20     |
| Indonesia         | 3           | 26         | PG #11, E3, E5                                                             |
| JTBD personal     | 5           | 30         | PG #2, PG #9, PG #16, E1, E4                                               |
| Islami            | 2           | 14         | PG #10, E2                                                                 |
| **TOTAL**         | **25**      | **100**    |                                                                            |

*Catatan: Klasifikasi memakai konteks dominan per soal. Distribusi konteks mengikuti prinsip "campuran Umum + Indonesia + JTBD + Islami" sesuai spec §2. Konteks Islami muncul eksplisit pada kasus zakat mal (PG #10, E2). Konteks Indonesia pada grade IP UAI (PG #11), data penduduk provinsi (E3), dan sistem antrean puskesmas (E5).*

---

## Penutup

> *"Barang siapa menempuh suatu jalan untuk mencari ilmu, niscaya Allah akan memudahkan baginya jalan menuju surga."*
> — **HR. Muslim**

**"Man jadda wajada"** — Siapa bersungguh-sungguh, pasti berhasil.

**~ Jazakumullahu khairan — Semoga berkah dalam penilaian ~**
