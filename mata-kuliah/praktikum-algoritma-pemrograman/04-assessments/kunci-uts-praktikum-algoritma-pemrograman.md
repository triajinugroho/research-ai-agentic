---
mata_kuliah: Praktikum Algoritma dan Pemrograman
kode_mk: INF-102
sks: 1 SKS (Praktikum)
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

| Field             | Nilai                                                                      |
|-------------------|----------------------------------------------------------------------------|
| Mata Kuliah       | Praktikum Algoritma dan Pemrograman                                        |
| Kode MK / SKS     | INF-102 / 1 SKS (Praktikum)                                                |
| Dosen             | Tri Aji Nugroho, S.T., M.T.                                                |
| Kelas             | [......]                                                                   |
| Hari/Tanggal      | [......]                                                                   |
| Waktu             | 60 menit                                                                   |
| Sifat Ujian       | Colab — boleh jalankan Python, tanpa AI tools, tanpa internet/dokumentasi  |

---

## Catatan Umum Penilaian

- Total poin: **100**. Tiap bagian dinilai independen; mahasiswa yang mengerjakan parsial tetap mendapat poin pada aspek yang benar.
- Penilaian dilakukan berbasis **eksekusi nyata** di notebook: jika cell tidak bisa dijalankan, pertimbangkan partial credit berbasis pembacaan kode (maks 60% dari aspek yang tampak benar).
- Semua jawaban ideal di bawah adalah **satu kemungkinan** — variasi implementasi yang memenuhi *acceptance criteria* tetap bernilai penuh.
- Potongan penalti non-fungsional (penamaan, docstring, format output) **tidak boleh** membuat poin bagian menjadi < 0.

---

## KUNCI JAWABAN PER BAGIAN

### Bagian (a) — Setup Notebook (5 poin)

**Sub-CPMK:** 1.1 (Menyiapkan lingkungan kerja Python di Google Colab dan mengkonfigurasi notebook untuk praktikum) & 1.2 (Mendemonstrasikan alur kerja penulisan, eksekusi, dan debugging program Python di Google Colab)
**Level Bloom:** C3
**Konteks:** Islami + JTBD

**Jawaban Ideal:**

Cell Markdown (cell #1):

```markdown
# UTS Praktikum Algoritma & Pemrograman — Genap 2025/2026
- Nama: Siti Aisyah
- NIM:  2024001
- Kelas: INF-A
```

Cell kode (cell #2):

```python
print("Bismillahirrahmanirrahim")
print("Sistem Donasi — Mulai.")
```

**Output yang diharapkan saat dijalankan:**

```
Bismillahirrahmanirrahim
Sistem Donasi — Mulai.
```

**Rubrik Penskoran:**

| Aspek                                                         | Poin |
|---------------------------------------------------------------|------|
| Cell Markdown identitas lengkap (Nama, NIM, Kelas, Judul UTS) | 2    |
| Cell kode mencetak "Bismillahirrahmanirrahim" (baris 1)       | 1    |
| Cell kode mencetak "Sistem Donasi — Mulai." (baris 2)         | 1    |
| Cell dijalankan & output tampil (bukan hanya ditulis)         | 1    |

**Acceptance Criteria:** Terdapat 2 cell (Markdown + kode) dan saat cell kode dijalankan, kedua baris output muncul tanpa error.

**Aturan Partial Credit:**
- Identitas tidak lengkap (≤ 2 dari 4 item) → skor cell Markdown = 1.
- Cell kode ada tetapi belum dijalankan (tidak ada output) → potongan 1 poin.
- Kesalahan ejaan "Bismillahirrahmanirrahim" → tetap diterima jika substansinya sama (toleransi 1 huruf).

---

### Bagian (b) — Data Donatur (15 poin)

**Sub-CPMK:** 2.1 (Mengimplementasikan deklarasi variabel dengan penamaan sesuai konvensi PEP 8 dalam program interaktif), 2.2 (Mendemonstrasikan penggunaan tipe data dasar dan melakukan konversi tipe dalam program), 2.4 (Membangun program interaktif menggunakan fungsi input/output dengan validasi sederhana)
**Level Bloom:** C3
**Konteks:** Islami + JTBD

**Jawaban Ideal (kode Python):**

```python
nama_donatur = input("Nama donatur: ")

jumlah_input = input("Jumlah donasi (Rp): ")
if jumlah_input.replace('.', '', 1).isdigit():
    jumlah_donasi = float(jumlah_input)
else:
    print("Input jumlah tidak valid — setel ke 0.")
    jumlah_donasi = 0.0

tujuan = input("Tujuan donasi: ")

anonim_input = input("Donasi anonim? (y/n): ").strip().lower()
is_anonim = (anonim_input == 'y')

# Verifikasi nilai & tipe
print(nama_donatur, type(nama_donatur))
print(jumlah_donasi, type(jumlah_donasi))
print(tujuan, type(tujuan))
print(is_anonim, type(is_anonim))
```

**Contoh output (input nama="Ahmad", jumlah="2500000", tujuan="pembangunan", anonim="n"):**

```
Ahmad <class 'str'>
2500000.0 <class 'float'>
pembangunan <class 'str'>
False <class 'bool'>
```

**Rubrik Penskoran:**

| Aspek                                                                 | Poin |
|-----------------------------------------------------------------------|------|
| 4 variabel dideklarasi dengan nama sesuai PEP 8 (snake_case)          | 4    |
| Tipe data tepat (`str`, `float`, `str`, `bool`)                       | 4    |
| Input interaktif `input()` digunakan untuk keempat variabel           | 3    |
| Validasi & konversi `jumlah_donasi` bekerja (pesan error + fallback 0)| 4    |

**Acceptance Criteria:** Program berjalan tanpa error untuk input valid (misal "2500000") dan tidak crash untuk input tidak valid (misal "abc" → setel ke 0.0 dengan pesan error).

**Aturan Partial Credit:**
- Nama variabel tidak PEP 8 (misal `NamaDonatur`, `Jumlah`) → kurangi 1 poin per variabel (maks 4).
- Tipe salah (misal `jumlah_donasi` tetap `str`) → kurangi 2 poin per variabel.
- Tidak ada validasi input jumlah → kurangi 4 poin (seluruh aspek validasi).
- Tidak mencetak `type()` untuk verifikasi → kurangi 2 poin (setengah dari aspek "Tipe data tepat").

---

### Bagian (c) — Klasifikasi Donatur (15 poin)

**Sub-CPMK:** 2.3 (Mengimplementasikan operator aritmatika, perbandingan, dan logika untuk membangun program kalkulasi) & 3.1 (Mengimplementasikan struktur seleksi if, elif, else dalam program pengambilan keputusan)
**Level Bloom:** C3
**Konteks:** Islami

**Jawaban Ideal (kode Python):**

```python
if jumlah_donasi >= 5_000_000:
    kategori = "Mujahid"
elif jumlah_donasi >= 1_000_000:        # otomatis < 5_000_000 di cabang ini
    kategori = "Muhsin"
elif jumlah_donasi > 0:                  # otomatis < 1_000_000 di cabang ini
    kategori = "Mukmin"
else:
    kategori = "Tidak Valid"

print(f"{nama_donatur} termasuk kategori {kategori}.")
```

**Contoh hasil eksekusi:**

| `jumlah_donasi` | `kategori`     | Output                                      |
|-----------------|----------------|---------------------------------------------|
| 8_000_000       | Mujahid        | `Ahmad termasuk kategori Mujahid.`          |
| 2_500_000       | Muhsin         | `Ahmad termasuk kategori Muhsin.`           |
| 300_000         | Mukmin         | `Ahmad termasuk kategori Mukmin.`           |
| 0 / -100        | Tidak Valid    | `Ahmad termasuk kategori Tidak Valid.`      |

**Rubrik Penskoran:**

| Aspek                                                                | Poin |
|----------------------------------------------------------------------|------|
| Struktur `if/elif/else` lengkap 4 cabang                             | 4    |
| Batas ambang benar (5jt, 1jt, 0)                                     | 4    |
| Operator perbandingan tepat (`>=`, `<`, `>`)                         | 3    |
| Output f-string sesuai format `{nama} termasuk kategori {kategori}.` | 4    |

**Acceptance Criteria:** Untuk nilai uji 8_000_000 / 2_500_000 / 300_000 / 0, kategori yang dihasilkan berturut-turut Mujahid / Muhsin / Mukmin / Tidak Valid.

**Aturan Partial Credit:**
- Hanya 3 cabang (lupa kasus "Tidak Valid") → kurangi 3 poin.
- Batas ambang salah (misal ≥ 5jt → "Muhsin") → kurangi 4 poin.
- Pakai `if` beruntun tanpa `elif` tetapi hasil akhir benar → kurangi 2 poin (kurang efisien).
- Output tidak f-string tetapi isi benar (pakai `+` concat) → kurangi 1 poin.

---

### Bagian (d) — Donasi Anonim (10 poin)

**Sub-CPMK:** 3.2 (Membangun program dengan seleksi bertingkat (nested) dan multi-kondisi untuk menyelesaikan kasus kompleks)
**Level Bloom:** C4
**Konteks:** Islami

**Jawaban Ideal (kode Python):**

```python
# Tentukan kategori dulu (atau reuse dari bagian c)
if jumlah_donasi >= 5_000_000:
    kategori = "Mujahid"
elif jumlah_donasi >= 1_000_000:
    kategori = "Muhsin"
elif jumlah_donasi > 0:
    kategori = "Mukmin"
else:
    kategori = "Tidak Valid"

# Seleksi bertingkat anonim
if is_anonim:
    if kategori == "Tidak Valid":
        nama_tampil = "Hamba Allah"   # tetap Hamba Allah meski tidak valid
    else:
        nama_tampil = "Hamba Allah"
else:
    nama_tampil = nama_donatur

print(f"{nama_tampil} termasuk kategori {kategori}.")
```

**Contoh hasil eksekusi:**

| `is_anonim` | `nama_donatur` | `jumlah_donasi` | Output                                      |
|-------------|----------------|-----------------|---------------------------------------------|
| True        | Ahmad          | 2_000_000       | `Hamba Allah termasuk kategori Muhsin.`     |
| False       | Siti Aisyah    | 10_000_000      | `Siti Aisyah termasuk kategori Mujahid.`    |
| True        | Budi           | 500_000         | `Hamba Allah termasuk kategori Mukmin.`     |

**Rubrik Penskoran:**

| Aspek                                                                          | Poin |
|--------------------------------------------------------------------------------|------|
| Cek `is_anonim` untuk memilih `nama_tampil`                                    | 3    |
| Kategori tetap dihitung berdasarkan `jumlah_donasi` (tidak tergantung anonim)  | 3    |
| Struktur nested/multi-kondisi tampak jelas (bukan satu baris tanpa struktur)   | 2    |
| Output f-string memuat `nama_tampil` & `kategori` dengan format benar          | 2    |

**Acceptance Criteria:** Untuk input (`is_anonim=True`, `jumlah=2_000_000`), output memuat "Hamba Allah" dan "Muhsin". Untuk input (`is_anonim=False`, `jumlah=10_000_000`), output memuat nama asli dan "Mujahid".

**Aturan Partial Credit:**
- Lupa ganti nama ketika anonim (tetap pakai nama asli) → kurangi 3 poin.
- Kategori ikut berubah saat anonim (misal anonim → otomatis "Hamba Allah" tanpa kategori benar) → kurangi 3 poin.
- Tidak menggunakan struktur nested/terpisah (cuma 1 if flat yang kebetulan benar) → kurangi 2 poin.

---

### Bagian (e) — Input Banyak Donatur (20 poin)

**Sub-CPMK:** 4.1 (Mengimplementasikan perulangan for dan while untuk menyelesaikan masalah iteratif), 4.2 (Membangun program pencetakan pola menggunakan perulangan bertingkat), 4.3 (Mengimplementasikan pola akumulator, counter, dan flag dalam program berbasis perulangan)
**Level Bloom:** C3
**Konteks:** JTBD

**Jawaban Ideal (kode Python):**

```python
daftar_donasi = []

while True:
    nama = input("Nama donatur (ketik 'selesai' untuk berhenti): ").strip()

    # Sentinel: berhenti jika input = 'selesai' (case-insensitive)
    if nama.lower() == "selesai":
        break

    # Flag/continue: skip jika nama kosong
    if nama == "":
        print("Nama tidak boleh kosong.")
        continue

    # Input field lain
    jumlah_input = input("  Jumlah donasi (Rp): ").strip()
    if jumlah_input.replace('.', '', 1).isdigit():
        jumlah = float(jumlah_input)
    else:
        print("  Jumlah tidak valid — setel ke 0.")
        jumlah = 0.0

    tujuan_item = input("  Tujuan donasi: ").strip()
    anonim = (input("  Donasi anonim? (y/n): ").strip().lower() == 'y')

    daftar_donasi.append({
        "nama": nama,
        "jumlah": jumlah,
        "tujuan": tujuan_item,
        "anonim": anonim,
    })

# Peringatan jika data kurang dari 5
if len(daftar_donasi) < 5:
    print(f"Peringatan: data donatur kurang dari 5. (Terkumpul: {len(daftar_donasi)})")
else:
    print(f"Data donatur terkumpul: {len(daftar_donasi)} entri.")
```

**Contoh jalur eksekusi (5 donatur):**

Input berturut-turut: `Ahmad, 5000000, pembangunan, n` → `Budi, 1500000, sosial, n` → `` (kosong, di-continue) → `Siti, 3000000, pembangunan, y` → `Fatimah, 800000, operasional, n` → `Umar, 2000000, sosial, n` → `selesai`.

Output akhir: `Data donatur terkumpul: 5 entri.`

**Rubrik Penskoran:**

| Aspek                                                                       | Poin |
|-----------------------------------------------------------------------------|------|
| Inisialisasi `daftar_donasi = []` (list kosong)                             | 2    |
| Loop `while` dengan sentinel `"selesai"` (case-insensitive) + `break`       | 5    |
| Penanganan nama kosong dengan `continue` + pesan `"Nama tidak boleh kosong."` | 4    |
| Dictionary dengan 4 field (nama, jumlah, tujuan, anonim) di-`append`        | 5    |
| Pengecekan len < 5 & pesan peringatan setelah loop                          | 4    |

**Acceptance Criteria:** Loop dapat dijalankan hingga sentinel "selesai" tanpa crash, `daftar_donasi` terisi dictionary, input kosong tidak menambah elemen, peringatan tampil bila < 5 entri.

**Aturan Partial Credit:**
- Sentinel case-sensitive saja (`"selesai"` beda dengan `"Selesai"`) → kurangi 2 poin.
- Tidak pakai `continue` untuk nama kosong, melainkan tetap append dengan nama kosong → kurangi 4 poin.
- Simpan sebagai list of list (bukan dict) tetapi 4 field semua tersimpan → kurangi 2 poin.
- Tidak ada peringatan < 5 → kurangi 4 poin.
- Pakai `for` dengan batas tetap (bukan `while` sentinel) → kurangi 5 poin (inti pola sentinel tidak terpenuhi).

---

### Bagian (f) — Fungsi Agregasi (20 poin)

**Sub-CPMK:** 4.3 (Mengimplementasikan pola akumulator, counter, dan flag dalam program berbasis perulangan), 5.1 (Mengimplementasikan fungsi dengan parameter dan return value untuk memecah program menjadi modul), 5.2 (Melakukan refactoring kode prosedural menjadi kode modular berbasis fungsi)
**Level Bloom:** C4
**Konteks:** JTBD

**Jawaban Ideal (kode Python):**

```python
def hitung_total(daftar_donasi: list) -> float:
    """Mengembalikan total jumlah donasi dari daftar (pola akumulator)."""
    total = 0.0
    for item in daftar_donasi:
        total += item["jumlah"]
    return total


def cari_donatur_terbesar(daftar_donasi: list) -> dict:
    """Mengembalikan dictionary donatur dengan jumlah donasi terbesar (running max)."""
    if not daftar_donasi:
        return None

    terbesar = daftar_donasi[0]
    for item in daftar_donasi[1:]:
        if item["jumlah"] > terbesar["jumlah"]:
            terbesar = item
    return terbesar


# Pemanggilan & cetak hasil
total = hitung_total(daftar_donasi)
donatur_top = cari_donatur_terbesar(daftar_donasi)

print(f"Total donasi: Rp {total:,.0f}".replace(",", "."))
if donatur_top is not None:
    print(f"Donatur terbesar: {donatur_top['nama']} — Rp {donatur_top['jumlah']:,.0f}".replace(",", "."))
else:
    print("Donatur terbesar: (tidak ada data)")
```

**Verifikasi manual dengan data uji:**

Data: `[{"nama":"Ahmad","jumlah":5_000_000,...}, {"nama":"Budi","jumlah":1_500_000,...}, {"nama":"Siti","jumlah":3_000_000,...}, {"nama":"Fatimah","jumlah":800_000,...}, {"nama":"Umar","jumlah":2_000_000,...}]`

- `hitung_total(...)` → `5_000_000 + 1_500_000 + 3_000_000 + 800_000 + 2_000_000 = 12_300_000.0` ✓
- `cari_donatur_terbesar(...)` → `{"nama":"Ahmad","jumlah":5_000_000,...}` ✓

Output:

```
Total donasi: Rp 12.300.000
Donatur terbesar: Ahmad — Rp 5.000.000
```

**Rubrik Penskoran:**

| Aspek                                                                         | Poin |
|-------------------------------------------------------------------------------|------|
| `hitung_total` didefinisikan dengan parameter & return, pola akumulator tepat | 5    |
| `cari_donatur_terbesar` didefinisikan dengan parameter & return, running max  | 5    |
| Penanganan list kosong (return 0.0 / None) di kedua fungsi                    | 3    |
| Pemanggilan kedua fungsi pada `daftar_donasi` & hasil dicetak                 | 4    |
| Format output rapi (Rupiah & nama donatur terbesar)                           | 3    |

**Acceptance Criteria:** Kedua fungsi dapat dipanggil terhadap `daftar_donasi` bagian (e) tanpa error; nilai `hitung_total` = jumlah `item["jumlah"]`; `cari_donatur_terbesar` menghasilkan item dengan `jumlah` maksimum; untuk list kosong kedua fungsi mengembalikan nilai default tanpa error.

**Aturan Partial Credit:**
- Logika akumulator ditulis di scope global (bukan di dalam fungsi) → kurangi 5 poin (fungsi tidak memenuhi modularitas).
- `hitung_total` pakai `sum([item["jumlah"] for item in daftar])` — diterima penuh (pola akumulator tersirat).
- `cari_donatur_terbesar` pakai `max(daftar, key=lambda d: d["jumlah"])` — diterima penuh.
- Tidak menangani list kosong (crash `IndexError`) → kurangi 3 poin.
- Tidak ada return (hanya `print` di dalam fungsi) → kurangi 5 poin (bukan fungsi dengan return value sesuai spec).
- Format output tanpa "Rp" atau tanpa pemisah ribuan → kurangi 1 poin.

---

### Bagian (g) — Refactor ke Program Utama (15 poin)

**Sub-CPMK:** 5.3 (Mendemonstrasikan penggunaan lambda, default parameter, dan *args/**kwargs dalam program)
**Level Bloom:** C5
**Konteks:** JTBD

**Jawaban Ideal (kode Python lengkap siap dijalankan):**

```python
def hitung_total(daftar_donasi: list) -> float:
    """Mengembalikan total jumlah donasi dari daftar."""
    total = 0.0
    for item in daftar_donasi:
        total += item["jumlah"]
    return total


def cari_donatur_terbesar(daftar_donasi: list) -> dict:
    """Mengembalikan dictionary donatur dengan jumlah donasi terbesar."""
    if not daftar_donasi:
        return None
    terbesar = daftar_donasi[0]
    for item in daftar_donasi[1:]:
        if item["jumlah"] > terbesar["jumlah"]:
            terbesar = item
    return terbesar


def format_rupiah(nilai: float) -> str:
    """Format angka ke string Rupiah dengan pemisah ribuan titik."""
    return f"Rp {nilai:,.0f}".replace(",", ".")


def jalankan_sistem():
    """Program utama Sistem Pengelola Donasi Masjid.

    Tujuan:
        Mencatat donasi jamaah masjid, mengklasifikasikan donatur,
        lalu menghasilkan laporan total dan daftar terurut.

    Input (interaktif via `input()`):
        - nama donatur (str), jumlah donasi (float Rp), tujuan (str),
          status anonim (y/n) — diulang hingga pengguna mengetik "selesai".

    Output (print ke stdout):
        - Klasifikasi per donatur (Mujahid/Muhsin/Mukmin/Tidak Valid),
          total donasi, donatur terbesar, dan daftar terurut terbesar → kecil.
    """
    daftar_donasi = []

    print("=" * 40)
    print("   SISTEM PENGELOLA DONASI MASJID")
    print("=" * 40)

    # --- Bagian (e): loop input dengan sentinel "selesai" ---
    while True:
        nama = input("Nama donatur (ketik 'selesai' untuk berhenti): ").strip()

        if nama.lower() == "selesai":
            break
        if nama == "":
            print("Nama tidak boleh kosong.")
            continue

        jumlah_input = input("  Jumlah donasi (Rp): ").strip()
        if jumlah_input.replace('.', '', 1).isdigit():
            jumlah = float(jumlah_input)
        else:
            print("  Jumlah tidak valid — setel ke 0.")
            jumlah = 0.0

        tujuan_item = input("  Tujuan donasi: ").strip()
        anonim = (input("  Donasi anonim? (y/n): ").strip().lower() == 'y')

        # --- Bagian (c) & (d): klasifikasi + anonim ---
        if jumlah >= 5_000_000:
            kategori = "Mujahid"
        elif jumlah >= 1_000_000:
            kategori = "Muhsin"
        elif jumlah > 0:
            kategori = "Mukmin"
        else:
            kategori = "Tidak Valid"

        nama_tampil = "Hamba Allah" if anonim else nama
        print(f"  -> {nama_tampil} termasuk kategori {kategori}.")

        daftar_donasi.append({
            "nama": nama_tampil,
            "jumlah": jumlah,
            "tujuan": tujuan_item,
            "anonim": anonim,
            "kategori": kategori,
        })

    # --- Peringatan jumlah minimum ---
    if len(daftar_donasi) < 5:
        print(f"\nPeringatan: data donatur kurang dari 5. (Terkumpul: {len(daftar_donasi)})")
    else:
        print(f"\nData donatur terkumpul: {len(daftar_donasi)} entri.")

    # --- Bagian (f) + sorting lambda ---
    total = hitung_total(daftar_donasi)
    terbesar = cari_donatur_terbesar(daftar_donasi)
    daftar_terurut = sorted(daftar_donasi, key=lambda d: d["jumlah"], reverse=True)

    # --- Laporan akhir ---
    print()
    print("=" * 40)
    print("       LAPORAN DONASI MASJID")
    print("=" * 40)
    print(f"Total donasi    : {format_rupiah(total)}")
    if terbesar is not None:
        print(f"Donatur terbesar: {terbesar['nama']} — {format_rupiah(terbesar['jumlah'])}")
    else:
        print("Donatur terbesar: (tidak ada data)")
    print("-" * 40)
    print("Daftar (urut terbesar → terkecil):")
    for i, d in enumerate(daftar_terurut, start=1):
        print(f"  {i}. {d['nama']:<15s} — {format_rupiah(d['jumlah'])}  ({d['tujuan']})")
    print("=" * 40)


# Entry point
jalankan_sistem()
```

**Verifikasi manual (data uji yang sama dengan bagian f):**

Dengan 5 donatur input: Ahmad/5jt/pembangunan/n, Budi/1.5jt/sosial/n, Siti/3jt/pembangunan/y, Fatimah/800rb/operasional/n, Umar/2jt/sosial/n → `selesai`.

Sorted (desc) seharusnya: Ahmad (5jt) → Siti anonim="Hamba Allah" (3jt) → Umar (2jt) → Budi (1.5jt) → Fatimah (800rb).

Laporan:

```
========================================
       LAPORAN DONASI MASJID
========================================
Total donasi    : Rp 12.300.000
Donatur terbesar: Ahmad — Rp 5.000.000
----------------------------------------
Daftar (urut terbesar → terkecil):
  1. Ahmad           — Rp 5.000.000  (pembangunan)
  2. Hamba Allah     — Rp 3.000.000  (pembangunan)
  3. Umar            — Rp 2.000.000  (sosial)
  4. Budi            — Rp 1.500.000  (sosial)
  5. Fatimah         — Rp 800.000  (operasional)
========================================
```

**Rubrik Penskoran:**

| Aspek                                                                 | Poin |
|-----------------------------------------------------------------------|------|
| Alur b-f terbungkus di dalam `jalankan_sistem()` (tanpa kode di scope global untuk alur utama) | 4    |
| Docstring `jalankan_sistem` menjelaskan tujuan, input, dan output     | 2    |
| Minimal satu penggunaan `lambda` (sorting/filtering yang benar)       | 3    |
| Laporan akhir memuat total, donatur terbesar, dan daftar terurut      | 4    |
| `jalankan_sistem()` dipanggil sebagai entry point di cell terakhir    | 2    |

**Acceptance Criteria:** `jalankan_sistem()` dapat dipanggil sekali, mencakup alur input → klasifikasi → agregasi → laporan, menghasilkan output laporan yang memuat total donasi + donatur terbesar + daftar terurut dari terbesar; penggunaan `lambda` pada `sorted(..., key=lambda d: d["jumlah"], reverse=True)` atau yang setara.

**Aturan Partial Credit:**
- Tidak membungkus alur ke dalam fungsi `jalankan_sistem` (masih prosedural di global) → kurangi 4 poin.
- Docstring ada tetapi hanya 1 baris tanpa penjelasan input/output → kurangi 1 poin.
- Pakai `sorted(..., key=itemgetter("jumlah"), reverse=True)` tanpa lambda → kurangi 3 poin (spec meminta lambda).
- Laporan tidak urut dari terbesar → kurangi 2 poin.
- `jalankan_sistem()` didefinisikan tapi tidak dipanggil → kurangi 2 poin.

---

## RINGKASAN DISTRIBUSI

### Tabel A — Pemetaan Sub-CPMK → Bagian → Poin

| Sub-CPMK | Deskripsi singkat                                    | Bagian    | Total Poin |
|----------|------------------------------------------------------|-----------|------------|
| 1.1      | Menyiapkan lingkungan Python di Google Colab         | (a)       | 2,5        |
| 1.2      | Alur kerja penulisan, eksekusi, debugging di Colab   | (a)       | 2,5        |
| 2.1      | Deklarasi variabel sesuai PEP 8                      | (b)       | 5          |
| 2.2      | Tipe data dasar & konversi tipe                      | (b)       | 5          |
| 2.4      | Program interaktif input/output dengan validasi      | (b)       | 5          |
| 2.3      | Operator aritmatika, perbandingan, logika            | (c)       | 7          |
| 3.1      | Seleksi if/elif/else                                 | (c)       | 8          |
| 3.2      | Seleksi bertingkat (nested) & multi-kondisi          | (d)       | 10         |
| 4.1      | Perulangan for dan while                             | (e)       | 7          |
| 4.2      | Perulangan bertingkat (loop kontrol break/continue)  | (e)       | 6          |
| 4.3      | Akumulator, counter, flag dalam loop                 | (e), (f)  | 12         |
| 5.1      | Fungsi dengan parameter & return value               | (f)       | 8          |
| 5.2      | Refactoring prosedural → modular berbasis fungsi     | (f)       | 7          |
| 5.3      | Lambda, default parameter, *args/**kwargs            | (g)       | 15         |
| **Total**|                                                      |           | **100**    |

*Catatan:* Poin pada bagian yang mencakup beberapa sub-CPMK didistribusikan proporsional (contoh: bagian (b) 15 poin dibagi rata 5/5/5 ke 3 sub-CPMK; bagian (e) 20 poin dibagi 7/6/7 ke sub-CPMK 4.1/4.2/4.3, lalu 5 poin sisa dari 4.3 bergabung dengan bagian (f)).

### Tabel B — Distribusi Level Bloom (per bobot poin)

| Level | Bagian                   | Total Poin | Persen Poin |
|-------|--------------------------|------------|-------------|
| C3    | (a) 5, (b) 15, (c) 15, (e) 20 | 55         | 55%         |
| C4    | (d) 10, (f) 20           | 30         | 30%         |
| C5    | (g) 15                   | 15         | 15%         |
| **Total** |                     | **100**    | **100%**    |

*Catatan:* Karena praktikum merupakan 1 soal integratif, bobot Bloom dihitung per poin bagian, bukan per jumlah soal. Level C2 tidak direpresentasikan karena karakter praktikum fokus pada aplikasi (C3+) sesuai RPS.

### Tabel C — Distribusi Konteks

| Konteks            | Bagian                   | Total Poin |
|--------------------|--------------------------|------------|
| Islami             | (c), (d)                 | 25         |
| Islami + JTBD      | (a), (b)                 | 20         |
| JTBD               | (e), (f), (g)            | 55         |
| **Total**          |                          | **100**    |

*Catatan:* Seluruh bagian diikat pada tema tunggal "Sistem Pengelola Donasi Masjid" — konteks Islami muncul di nomenklatur kategori (Mujahid/Muhsin/Mukmin), kasus donasi anonim ("Hamba Allah"), dan salam pembuka ("Bismillahirrahmanirrahim"); konteks JTBD personal muncul di pencatatan donasi, akumulasi, dan laporan keuangan pribadi masjid (Rupiah).

---

**~ Barakallahu fiikum — Selamat Mengoreksi ~**
