---
mata_kuliah: Praktikum Algoritma dan Pemrograman
kode_mk: INF-102
sks: 1 SKS (Praktikum)
semester: Genap 2025/2026
jenis: UTS
---

# UJIAN TENGAH SEMESTER (UTS)
## Semester Genap Tahun Akademik 2025/2026

**UNIVERSITAS AL AZHAR INDONESIA**
**Fakultas Sains dan Teknologi — Program Studi Informatika**

> *"Bacalah dengan (menyebut) nama Tuhanmu yang menciptakan."*
> — **QS Al-'Alaq: 1**

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

## PETUNJUK PENGERJAAN

1. Bacalah **Basmalah** sebelum memulai ujian.
2. Tuliskan Nama, NIM, dan Kelas di lembar jawaban (dalam cell Markdown pertama notebook).
3. Kerjakan dengan jujur, mandiri, dan bertanggung jawab sesuai nilai integritas akademik dan etika Islami.
4. Dilarang menggunakan AI tools (ChatGPT, Copilot, dll.), kecuali dinyatakan lain pada sifat ujian.
5. **Khusus Praktikum:**
   - Kerjakan di Google Colab (1 notebook baru).
   - Simpan notebook ke Drive dengan nama: `UTS_<NIM>_<NamaLengkap>.ipynb` (contoh: `UTS_2024001_SitiAisyah.ipynb`).
   - Jangan akses dokumentasi online, Stack Overflow, ChatGPT, Copilot, atau alat AI apa pun.
   - Submit link Colab/file `.ipynb` ke folder submission yang disediakan dosen sebelum waktu habis.
   - Penilaian per-bagian bisa independen — kerjakan bagian yang paling Anda kuasai lebih dulu bila mentok pada bagian sebelumnya.
6. Periksa kembali jawaban sebelum dikumpulkan.
7. Akhiri dengan **Hamdalah**.

> *"Sesungguhnya amal-amal itu tergantung pada niatnya."*
> — **HR. Bukhari-Muslim**

---

## SOAL INTEGRATIF — "Sistem Pengelola Donasi Masjid" (100 poin)

Masjid Al-Azhar di kampung Anda ingin membangun sistem pencatat donasi sederhana berbasis Python untuk membantu pengurus mencatat nama donatur, jumlah donasi (dalam Rupiah), dan tujuan donasi (misal: pembangunan, operasional, sosial). Sistem juga harus dapat mengklasifikasikan donatur dan menghasilkan laporan.

Kerjakan 7 bagian (a-g) berikut secara berurutan pada **satu notebook Colab**. Tiap bagian dibuat dalam **cell terpisah** yang diawali cell Markdown berjudul "Bagian (a)", "Bagian (b)", dan seterusnya. Bobot tiap bagian dituliskan di judul; total 100 poin.

---

> **Sub-CPMK 1.1 & 1.2** — Menyiapkan lingkungan kerja Python di Google Colab dan mengkonfigurasi notebook untuk praktikum; Mendemonstrasikan alur kerja penulisan, eksekusi, dan debugging program Python di Google Colab
> *Level Bloom:* C3 · *Konteks:* Islami + JTBD

### Bagian (a) — Setup Notebook (5 poin)

1. Buat **cell Markdown** di paling atas notebook yang berisi:
   - Nama lengkap
   - NIM
   - Kelas
   - Judul "UTS Praktikum Algoritma & Pemrograman — Genap 2025/2026"
2. Buat **cell kode** berikutnya yang mencetak dua baris:
   - Baris pertama: `Bismillahirrahmanirrahim` (huruf Latin)
   - Baris kedua: `Sistem Donasi — Mulai.`
3. Jalankan cell tersebut untuk memverifikasi output muncul di bawah cell.

---

> **Sub-CPMK 2.1, 2.2, 2.4** — Mengimplementasikan deklarasi variabel dengan penamaan sesuai konvensi PEP 8 dalam program interaktif; Mendemonstrasikan penggunaan tipe data dasar (int, float, str, bool) dan melakukan konversi tipe dalam program; Membangun program interaktif menggunakan fungsi input/output dengan validasi sederhana
> *Level Bloom:* C3 · *Konteks:* Islami + JTBD

### Bagian (b) — Data Donatur (15 poin)

Buat variabel berikut dengan penamaan sesuai konvensi PEP 8 (`snake_case`):

| Variabel         | Tipe   | Diperoleh dari                                                                          |
|------------------|--------|-----------------------------------------------------------------------------------------|
| `nama_donatur`   | `str`  | `input("Nama donatur: ")`                                                               |
| `jumlah_donasi`  | `float`| `input("Jumlah donasi (Rp): ")` lalu konversi ke `float`                                |
| `tujuan`         | `str`  | `input("Tujuan donasi: ")`                                                              |
| `is_anonim`      | `bool` | `input("Donasi anonim? (y/n): ")` lalu konversi ke `bool` (y → `True`, selain itu → `False`) |

Ketentuan tambahan:

1. Cetak keempat variabel beserta tipe masing-masing menggunakan `type()` untuk verifikasi.
2. Tangani kasus input non-numerik pada `jumlah_donasi` dengan **validasi sederhana** (tidak perlu `try/except` lengkap). Contoh validasi: cek `input.replace('.', '', 1).isdigit()` sebelum konversi. Jika tidak valid, cetak pesan `"Input jumlah tidak valid — setel ke 0."` dan set `jumlah_donasi = 0.0`.

---

> **Sub-CPMK 2.3 & 3.1** — Mengimplementasikan operator aritmatika, perbandingan, dan logika untuk membangun program kalkulasi; Mengimplementasikan struktur seleksi if, elif, else dalam program pengambilan keputusan
> *Level Bloom:* C3 · *Konteks:* Islami

### Bagian (c) — Klasifikasi Donatur (15 poin)

Gunakan `if/elif/else` dan operator perbandingan/logika untuk mengklasifikasikan `jumlah_donasi` ke dalam empat kategori:

- `jumlah_donasi >= 5_000_000` → kategori `"Mujahid"`
- `jumlah_donasi >= 1_000_000` dan `jumlah_donasi < 5_000_000` → kategori `"Muhsin"`
- `jumlah_donasi < 1_000_000` dan `jumlah_donasi > 0` → kategori `"Mukmin"`
- lainnya (≤ 0 atau tidak valid) → kategori `"Tidak Valid"`

Simpan hasil ke variabel `kategori`. Cetak kalimat akhir dengan f-string:

```
f"{nama_donatur} termasuk kategori {kategori}."
```

---

> **Sub-CPMK 3.2** — Membangun program dengan seleksi bertingkat (nested) dan multi-kondisi untuk menyelesaikan kasus kompleks
> *Level Bloom:* C4 · *Konteks:* Islami

### Bagian (d) — Donasi Anonim (10 poin)

Kembangkan logika pada bagian (c). Jika `is_anonim == True`, nama donatur yang dicetak **harus** diganti menjadi `"Hamba Allah"` — tetapi kategori yang ditampilkan **tetap** sesuai jumlah donasinya. Gunakan pendekatan seleksi bertingkat (nested) atau multi-kondisi dalam satu blok keputusan.

Contoh hasil yang diharapkan:

- Jika `is_anonim=True` dan donasi Rp 2.000.000 → `"Hamba Allah termasuk kategori Muhsin."`
- Jika `is_anonim=False` (misal nama "Siti Aisyah") dan donasi Rp 10.000.000 → `"Siti Aisyah termasuk kategori Mujahid."`

Simpan nama tampil akhir ke variabel `nama_tampil` sebelum dicetak.

---

> **Sub-CPMK 4.1, 4.2, 4.3** — Mengimplementasikan perulangan for dan while untuk menyelesaikan masalah iteratif; Membangun program pencetakan pola (pattern printing) menggunakan perulangan bertingkat; Mengimplementasikan pola akumulator, counter, dan flag dalam program berbasis perulangan
> *Level Bloom:* C3 · *Konteks:* JTBD

### Bagian (e) — Input Banyak Donatur (20 poin)

Modifikasi program agar dapat menerima **minimal 5 donatur**. Ikuti langkah berikut:

1. Siapkan list kosong: `daftar_donasi = []`.
2. Gunakan perulangan `while` dengan pola **sentinel**: jika input nama sama dengan `"selesai"` (case-insensitive), hentikan loop dengan `break`.
3. Dalam loop, jika input nama kosong (string kosong setelah `strip()`), cetak pesan `"Nama tidak boleh kosong."` lalu lanjut iterasi berikutnya (`continue`) **tanpa** menambah data.
4. Untuk tiap iterasi valid, minta input: `nama`, `jumlah` (float), `tujuan`, `anonim` (y/n). Simpan sebagai **dictionary** ke dalam `daftar_donasi`, misal:

   ```python
   {"nama": ..., "jumlah": ..., "tujuan": ..., "anonim": ...}
   ```

5. Setelah loop berhenti, **jika jumlah data kurang dari 5**, cetak peringatan: `"Peringatan: data donatur kurang dari 5."`. Jika sudah ≥ 5, cetak: `"Data donatur terkumpul: <n> entri."`.

---

> **Sub-CPMK 4.3, 5.1, 5.2** — Mengimplementasikan pola akumulator, counter, dan flag dalam program berbasis perulangan; Mengimplementasikan fungsi dengan parameter dan return value untuk memecah program menjadi modul; Melakukan refactoring kode prosedural menjadi kode modular berbasis fungsi
> *Level Bloom:* C4 · *Konteks:* JTBD

### Bagian (f) — Fungsi Agregasi (20 poin)

Buat **dua fungsi** berikut (semua logika akumulator harus berada di dalam fungsi, bukan di scope global):

```python
def hitung_total(daftar_donasi: list) -> float:
    """Mengembalikan total jumlah donasi dari daftar."""
    # TODO: gunakan pola akumulator
    pass


def cari_donatur_terbesar(daftar_donasi: list) -> dict:
    """Mengembalikan dictionary donatur dengan jumlah donasi terbesar."""
    # TODO: gunakan pola "running maximum"
    pass
```

Ketentuan:

1. `hitung_total` menggunakan pola **akumulator** (inisialisasi `total = 0.0` lalu iterasi `+=`).
2. `cari_donatur_terbesar` menggunakan pola **running maximum** (inisialisasi dengan elemen pertama, lalu bandingkan dengan elemen lain).
3. Kedua fungsi harus **robust**: jika `daftar_donasi` kosong, `hitung_total` mengembalikan `0.0` dan `cari_donatur_terbesar` mengembalikan `None` (atau dict kosong).
4. Panggil kedua fungsi pada `daftar_donasi` dari bagian (e) dan cetak hasilnya dalam format rapi, contoh:
   - `Total donasi: Rp 12.500.000`
   - `Donatur terbesar: Ahmad — Rp 5.000.000`

---

> **Sub-CPMK 5.3** — Mendemonstrasikan penggunaan lambda, default parameter, dan *args/**kwargs dalam program
> *Level Bloom:* C5 · *Konteks:* JTBD

### Bagian (g) — Refactor ke Program Utama (15 poin)

1. Bungkus seluruh alur interaktif (bagian b-f) ke dalam **fungsi utama** bernama `jalankan_sistem()`. Fungsi ini tidak menerima argumen dan tidak mengembalikan nilai (hanya side effect `print` dan interaksi input).
2. Tambahkan **docstring** di `jalankan_sistem` yang menjelaskan: tujuan fungsi, input yang diminta, dan output yang dihasilkan.
3. Gunakan **minimal satu fungsi lambda** untuk keperluan sorting atau filtering daftar donasi, contoh:

   ```python
   daftar_terurut = sorted(daftar_donasi, key=lambda d: d["jumlah"], reverse=True)
   ```

4. Tampilkan **laporan akhir** dengan isi berikut, rapi dengan pemisah `=` atau `-`:
   - Total donasi (Rupiah)
   - Donatur terbesar (nama + jumlah)
   - Daftar donatur terurut dari terbesar (nama, jumlah, tujuan)
5. Eksekusi `jalankan_sistem()` sebagai **entry point** di cell terakhir notebook.

Contoh format laporan:

```
========================================
       LAPORAN DONASI MASJID
========================================
Total donasi    : Rp 12.500.000
Donatur terbesar: Ahmad — Rp 5.000.000
----------------------------------------
Daftar (urut terbesar → terkecil):
  1. Ahmad         — Rp 5.000.000  (pembangunan)
  2. Hamba Allah   — Rp 3.000.000  (sosial)
  ...
========================================
```

---

## Penutup

> *"Barang siapa menempuh suatu jalan untuk mencari ilmu, niscaya Allah akan memudahkan baginya jalan menuju surga."*
> — **HR. Muslim**

**"Man jadda wajada"** — Siapa bersungguh-sungguh, pasti berhasil.

**~ Selamat Mengerjakan — Jazakumullahu khairan ~**
