# BAB 14: PROYEK AKHIR — MEMBANGUN SOLUSI END-TO-END

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

| Sub-CPMK | Deskripsi | Bloom's Level |
|----------|-----------|---------------|
| CPMK-7.9 | Merancang solusi pemrograman end-to-end dari perumusan masalah hingga implementasi | C6 (Mencipta) |
| CPMK-7.10 | Mengintegrasikan seluruh konsep (variabel, kontrol, fungsi, struktur data, algoritma) | C5 (Mengevaluasi) |
| CPMK-7.11 | Mendokumentasikan proses pengembangan termasuk AI Usage Log | C4 (Menganalisis) |
| CPMK-7.12 | Mempresentasikan solusi dengan jelas dan profesional | C5 (Mengevaluasi) |

**Estimasi Waktu:** 3 × 50 menit (3 SKS)

**Prasyarat:** Seluruh materi Bab 1–13.

---

## 14.1 Software Development Life Cycle (SDLC) Sederhana

### 14.1.1 Dari Masalah ke Solusi

Sepanjang 13 bab sebelumnya, Anda telah mempelajari semua komponen dasar pemrograman:

```
BAB 1-4: FONDASI
├── Algoritma & Computational Thinking
├── Variabel, Tipe Data, Operator
├── Seleksi (if/elif/else)
└── Perulangan (for/while)

BAB 5-7: MODULARITAS
├── Fungsi & Dekomposisi
├── String & Pengolahan Teks
└── List, Tuple, Operasi Koleksi

BAB 8-11: STRUKTUR DATA & ALGORITMA
├── Dictionary, Set, Pemilihan Struktur Data
├── Algoritma Pencarian (Searching)
├── Algoritma Pengurutan (Sorting)
└── Rekursi & Pemecahan Masalah

BAB 12-13: FRONTIER
├── Kompleksitas Algoritma (Big-O)
└── AI-Augmented Programming & Code Quality
```

Sekarang saatnya **menyatukan semuanya** dalam satu proyek nyata. Ini adalah bab capstone — di mana Anda menunjukkan bahwa Anda mampu membangun solusi pemrograman dari awal hingga akhir.

### 14.1.2 Fase SDLC Sederhana

Untuk proyek mata kuliah ini, kita menggunakan SDLC sederhana dengan 6 fase:

```
╭───────────╮    ╭───────────╮    ╭──────────────╮
│ 1. ANALISIS│───→│ 2. DESAIN │───→│ 3. IMPLEMENT │
│   MASALAH  │    │           │    │    ASI       │
╰───────────╯    ╰───────────╯    ╰──────┬───────╯
                                         │
╭───────────╮    ╭───────────╮    ╭──────▼───────╮
│6. PRESENT │←───│5. DOKUMEN │←───│ 4. TESTING   │
│   ASI     │    │   TASI    │    │              │
╰───────────╯    ╰───────────╯    ╰──────────────╯
```

### 14.1.3 Timeline Proyek

| Minggu | Milestone | Deliverable |
|--------|-----------|-------------|
| **9** | Proposal | Dokumen proposal (masalah, fitur, rencana) |
| **10-11** | Implementasi Awal | Kode inti (core features) |
| **12** | Progress Report | Demo progress + laporan kemajuan |
| **13-14** | Implementasi Lanjutan | Kode lengkap + testing |
| **15** | Presentasi Final | Source code + Dokumentasi + Presentasi + AI Log |

---

## 14.2 Fase 1: Analisis Masalah

### 14.2.1 Memilih Topik Proyek

Pilih topik yang sesuai dengan kemampuan dan minat Anda. Berikut **10 contoh topik** dengan konteks Indonesia:

| No | Topik | Deskripsi Singkat |
|----|-------|-------------------|
| 1 | Sistem Informasi Perpustakaan Mini | Kelola buku: tambah, cari, pinjam, kembalikan |
| 2 | Aplikasi Kasir Toko/Warung | Input barang, hitung total, cetak struk |
| 3 | Game Tebak Kata Bahasa Indonesia | Hangman dengan kata-kata Bahasa Indonesia |
| 4 | Sistem Antrian Rumah Sakit | Antrian dengan prioritas darurat/lansia |
| 5 | Tool Analisis Teks | Frekuensi kata, sentimen sederhana |
| 6 | Buku Alamat / Kontak Manager | CRUD kontak dengan searching dan sorting |
| 7 | Kalkulator IPK dan Transkrip | Hitung IPK, tampilkan transkrip akademik |
| 8 | Sistem Rekomendasi Menu Kantin | Cari menu berdasarkan budget, kategori |
| 9 | Sistem Voting / E-Polling | Registrasi, voting, tabulasi, hasil |
| 10 | Mini Quiz App | Bank soal, scoring, leaderboard |

### 14.2.2 Problem Statement yang Jelas

Setiap proyek harus dimulai dengan **problem statement** yang jelas:

```
TEMPLATE PROBLEM STATEMENT
═══════════════════════════

Masalah:
[Deskripsi masalah yang ingin diselesaikan, 2-3 kalimat]

Siapa yang terpengaruh:
[Siapa pengguna/stakeholder utama]

Solusi yang diusulkan:
[Deskripsi singkat solusi, 2-3 kalimat]

Fitur utama:
1. [Fitur 1]
2. [Fitur 2]
3. [Fitur 3]
...
```

**Contoh:**
```
Masalah:
Perpustakaan kampus UAI masih menggunakan pencatatan manual
untuk meminjam dan mengembalikan buku. Proses pencarian buku
lambat dan riwayat peminjaman sulit dilacak.

Siapa yang terpengaruh:
Mahasiswa dan petugas perpustakaan UAI.

Solusi yang diusulkan:
Membuat aplikasi konsol Python untuk mengelola data buku dan
peminjaman secara digital. Aplikasi mendukung pencarian cepat
dan pencatatan riwayat.

Fitur utama:
1. Tambah dan hapus buku dari katalog
2. Cari buku berdasarkan judul, pengarang, atau kategori
3. Pinjam dan kembalikan buku dengan validasi
4. Tampilkan statistik perpustakaan
5. Simpan data ke file (persistent storage)
```

### 14.2.3 Requirements Analysis

Identifikasi kebutuhan secara detail:

**Functional Requirements** (apa yang harus dilakukan):
- FR-1: Sistem harus bisa menambahkan buku baru
- FR-2: Sistem harus bisa mencari buku berdasarkan judul
- FR-3: Sistem harus bisa memproses peminjaman buku
- ...

**Non-Functional Requirements** (bagaimana sistem bekerja):
- NFR-1: Respons pencarian harus instan (data < 1000 buku)
- NFR-2: Antarmuka konsol harus mudah dipahami
- NFR-3: Data harus tersimpan saat program ditutup

### 14.2.4 Template Proposal Proyek

```markdown
# PROPOSAL PROYEK AKHIR
## Algoritma dan Pemrograman — Semester Genap 2025/2026

### Identitas
- Nama: [Nama Anda]
- NIM: [NIM Anda]
- Tanggal: [Tanggal]

### 1. Judul Proyek
[Judul proyek Anda]

### 2. Latar Belakang Masalah
[2-3 paragraf menjelaskan masalah dan konteks]

### 3. Tujuan
[3-5 tujuan spesifik]

### 4. Fitur yang Akan Dibuat
[List fitur dengan deskripsi singkat]

### 5. Rencana Struktur Data
[Struktur data yang akan digunakan dan alasannya]

### 6. Rencana Algoritma
[Algoritma utama: searching, sorting, dll.]

### 7. Rencana AI Usage
[Bagian mana yang akan menggunakan bantuan AI]

### 8. Timeline
[Rencana mingguan]
```

---

## 14.3 Fase 2: Desain

### 14.3.1 Desain Top-Down

Terapkan prinsip top-down design (Bab 5) untuk memecah program menjadi fungsi-fungsi:

```
              ┌──────────────────────┐
              │    PERPUSTAKAAN      │
              │    (main_menu)       │
              └──────────┬───────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
  ┌─────▼─────┐   ┌─────▼─────┐   ┌─────▼─────┐
  │  KELOLA   │   │  TRANSAKSI│   │  LAPORAN  │
  │  BUKU     │   │           │   │           │
  └─────┬─────┘   └─────┬─────┘   └─────┬─────┘
        │               │               │
   ┌────┼────┐     ┌────┼────┐     ┌────┼────┐
   │    │    │     │    │    │     │    │    │
tambah cari hapus pinjam kembali  stat  riwayat
buku  buku  buku  buku   buku    istik
```

### 14.3.2 Pemilihan Struktur Data

Gunakan pengetahuan dari Bab 7-8 untuk memilih struktur data yang tepat:

| Data | Struktur | Alasan |
|------|----------|--------|
| Katalog buku | `dict` (key=id_buku) | Akses cepat O(1) berdasarkan ID |
| Daftar peminjaman | `list` of `dict` | Perlu iterasi dan pencarian |
| Kategori buku | `set` | Unik, lookup cepat |
| Data buku tunggal | `dict` | Key-value pairs (judul, pengarang, tahun, dll.) |

### 14.3.3 Desain Algoritma

Sketsa pseudocode untuk fitur utama:

```
FUNGSI cari_buku(katalog, keyword, kriteria):
    hasil = list kosong
    UNTUK SETIAP buku DALAM katalog:
        JIKA keyword ADA DI buku[kriteria] (case-insensitive):
            tambahkan buku ke hasil
    JIKA hasil kosong:
        TAMPILKAN "Buku tidak ditemukan"
    JIKA TIDAK:
        urutkan hasil berdasarkan judul (A-Z)
        TAMPILKAN hasil
    RETURN hasil
```

### 14.3.4 Desain User Interface (Console-Based)

Sketsa tampilan program:

```
═══════════════════════════════════════════
       SISTEM PERPUSTAKAAN MINI UAI
         Versi 1.0 — Februari 2026
═══════════════════════════════════════════

╔═══════════ MENU UTAMA ═══════════╗
║                                  ║
║  1. Tambah Buku Baru             ║
║  2. Cari Buku                    ║
║  3. Tampilkan Semua Buku         ║
║  4. Pinjam Buku                  ║
║  5. Kembalikan Buku              ║
║  6. Statistik Perpustakaan       ║
║  7. Keluar                       ║
║                                  ║
╚══════════════════════════════════╝

Pilih menu (1-7): _
```

---

## 14.4 Fase 3: Implementasi

### 14.4.1 Setup Project

Struktur file proyek:

```
perpustakaan-mini/
├── main.py            # Program utama
├── data_buku.txt      # Data buku (file I/O)
├── riwayat.txt        # Riwayat peminjaman
└── README.md          # Dokumentasi proyek
```

### 14.4.2 Implementasi Bertahap

Implementasikan secara **incremental** — satu fitur per satu:

1. Buat menu utama dan loop program
2. Implementasikan CRUD buku (tambah, tampilkan, hapus)
3. Implementasikan pencarian
4. Implementasikan peminjaman/pengembalian
5. Implementasikan statistik
6. Tambahkan file I/O
7. Testing dan perbaikan

### 14.4.3 Kode Inti: Review Konsep dari Semua Bab

Proyek Anda harus mengintegrasikan konsep dari seluruh mata kuliah:

| Konsep | Bab | Contoh Penggunaan di Proyek |
|--------|-----|----------------------------|
| Variabel & tipe data | 2 | Menyimpan data buku, input pengguna |
| Seleksi (if/elif/else) | 3 | Validasi input, pemilihan menu |
| Perulangan (for/while) | 4 | Iterasi katalog, menu loop |
| Fungsi | 5 | Setiap fitur = 1 fungsi |
| String | 6 | Formatting output, pencarian teks |
| List/Tuple | 7 | Menyimpan koleksi data |
| Dictionary/Set | 8 | Katalog buku, data key-value |
| Searching | 9 | Pencarian buku |
| Sorting | 10 | Mengurutkan daftar buku |
| Rekursi | 11 | Opsional (misal: nested menu) |
| Big-O | 12 | Pilih algoritma yang efisien |
| AI Partner | 13 | Bantu coding, dokumentasikan di AI Log |

### 14.4.4 AI sebagai Coding Partner

Gunakan framework CRIDE dari Bab 13:
- Analisis masalah sendiri (JANGAN langsung tanya AI)
- Gunakan AI untuk membantu implementasi bagian repetitif
- SELALU review kode dari AI
- Dokumentasikan SEMUA interaksi di AI Usage Log

---

## 14.5 Fase 4: Testing

### 14.5.1 Manual Testing

Buat **test plan** sederhana:

| No | Test Case | Input | Expected Output | Actual Output | Status |
|----|-----------|-------|-----------------|---------------|--------|
| 1 | Tambah buku | "Laskar Pelangi", "Andrea Hirata", 2005 | Buku berhasil ditambahkan | — | — |
| 2 | Cari buku (ada) | keyword="Laskar" | Menampilkan Laskar Pelangi | — | — |
| 3 | Cari buku (tidak ada) | keyword="xyz" | "Buku tidak ditemukan" | — | — |
| 4 | Pinjam buku | ID buku valid | Status berubah "dipinjam" | — | — |
| 5 | Pinjam buku yang sudah dipinjam | ID buku yang dipinjam | "Buku sedang dipinjam" | — | — |

### 14.5.2 Edge Cases dan Error Handling

```python
# Contoh error handling yang baik
def tambah_buku(katalog, judul, pengarang, tahun):
    """Menambahkan buku ke katalog dengan validasi."""
    # Validasi input kosong
    if not judul or not pengarang:
        print("Error: Judul dan pengarang tidak boleh kosong!")
        return False

    # Validasi tahun
    if not isinstance(tahun, int) or tahun < 0 or tahun > 2026:
        print("Error: Tahun tidak valid!")
        return False

    # Cek duplikat
    for buku in katalog.values():
        if buku['judul'].lower() == judul.lower():
            print(f"Peringatan: Buku '{judul}' sudah ada di katalog.")
            return False

    # Generate ID unik
    id_buku = f"BK-{len(katalog) + 1:04d}"

    katalog[id_buku] = {
        'judul': judul,
        'pengarang': pengarang,
        'tahun': tahun,
        'status': 'tersedia'
    }

    print(f"Buku '{judul}' berhasil ditambahkan dengan ID: {id_buku}")
    return True
```

### 14.5.3 Debugging Strategies

Jika menemukan bug:
1. **Identifikasi**: Baris/fungsi mana yang bermasalah?
2. **Reproduce**: Bisakah bug diulang?
3. **Isolate**: Uji fungsi secara terpisah
4. **Fix**: Perbaiki bug
5. **Verify**: Pastikan fix tidak merusak yang lain

```python
# Teknik debugging sederhana: print statements
def cari_buku(katalog, keyword):
    print(f"DEBUG: mencari '{keyword}' di {len(katalog)} buku")  # hapus setelah fix
    hasil = []
    for id_buku, buku in katalog.items():
        if keyword.lower() in buku['judul'].lower():
            print(f"DEBUG: ditemukan di {id_buku}")  # hapus setelah fix
            hasil.append((id_buku, buku))
    print(f"DEBUG: total hasil = {len(hasil)}")  # hapus setelah fix
    return hasil
```

---

## 14.6 Fase 5: Dokumentasi

### 14.6.1 Dokumentasi Kode

Setiap fungsi harus memiliki docstring:

```python
def pinjam_buku(katalog, id_buku, nama_peminjam):
    """
    Memproses peminjaman buku.

    Parameters:
        katalog (dict): Katalog buku
        id_buku (str): ID buku yang akan dipinjam
        nama_peminjam (str): Nama peminjam

    Returns:
        bool: True jika peminjaman berhasil, False jika gagal
    """
    # ... implementasi
```

### 14.6.2 README Proyek

```markdown
# Sistem Perpustakaan Mini UAI

## Deskripsi
Aplikasi konsol Python untuk mengelola perpustakaan mini.
Dikembangkan sebagai proyek akhir mata kuliah Algoritma
dan Pemrograman — Universitas Al Azhar Indonesia.

## Fitur
- Tambah dan hapus buku dari katalog
- Cari buku berdasarkan judul/pengarang/kategori
- Pinjam dan kembalikan buku
- Statistik perpustakaan
- Data tersimpan di file (persistent)

## Cara Menjalankan
1. Buka Google Colab
2. Upload file main.py
3. Jalankan: `!python main.py`
   Atau copy-paste kode ke cell Colab

## Struktur Data
- Katalog: dictionary (key=id_buku, value=data_buku)
- Setiap buku: dictionary dengan key judul, pengarang, tahun, status

## Algoritma yang Digunakan
- Linear search untuk pencarian buku
- Built-in sort untuk pengurutan katalog

## Identitas
- Nama: [Nama Anda]
- NIM: [NIM Anda]
- Mata Kuliah: Algoritma dan Pemrograman (3 SKS)
- Dosen: Tri Aji Nugroho, S.T., M.T.
- Semester: Genap 2025/2026
```

### 14.6.3 AI Usage Log

**Template lengkap** (dari Bab 13):

```markdown
# AI Usage Log — Proyek Akhir
## Identitas
- Nama: Ahmad Fauzan
- NIM: 2025001
- Proyek: Sistem Perpustakaan Mini
- Tanggal mulai: 1 April 2026
- Tanggal selesai: 25 Mei 2026

## Ringkasan
- AI yang digunakan: Claude
- Persentase kode AI: ~40%
- Persentase kode sendiri: ~60%
- Jumlah interaksi: 12 prompt

## Detail Interaksi

### Interaksi 1 (Minggu 9)
- **Prompt:** "Bantu saya merancang struktur data untuk sistem
  perpustakaan. Saya butuh menyimpan buku, peminjaman, dan anggota."
- **Respons AI:** Menyarankan dict untuk katalog, list untuk riwayat
- **Yang digunakan:** Adopsi saran dict untuk katalog
- **Modifikasi:** Menambahkan field 'kategori' yang tidak disarankan AI
- **Pelajaran:** Dict lebih tepat dari list untuk data yang butuh akses by ID

### Interaksi 2 (Minggu 10)
- **Prompt:** "Implementasikan fungsi cari_buku yang mendukung
  pencarian by judul, pengarang, dan tahun."
- **Respons AI:** Generate fungsi dengan 3 parameter
- **Yang digunakan:** Adaptasi logika pencarian
- **Modifikasi:** Tambah case-insensitive search, perbaiki bug ketika
  kata kunci kosong
- **Pelajaran:** AI lupa handle edge case string kosong

[... dst untuk setiap interaksi ...]

## Refleksi
AI membantu mempercepat implementasi, terutama untuk kode
boilerplate (menu, formatting output). Namun, desain arsitektur
dan penanganan edge cases tetap dilakukan sendiri. Saya
memahami seluruh kode yang dikumpulkan.
```

### 14.6.4 Laporan Teknis Singkat

Struktur laporan (2-3 halaman):
1. Pendahuluan (masalah dan tujuan)
2. Desain (struktur data, algoritma, flowchart)
3. Implementasi (highlight fitur utama)
4. Testing (hasil pengujian)
5. Kesimpulan dan refleksi

---

## 14.7 Fase 6: Presentasi

### 14.7.1 Struktur Presentasi (5-7 Menit)

| Waktu | Bagian | Isi |
|-------|--------|-----|
| 0:00-0:30 | Pembuka | Salam, nama, judul proyek |
| 0:30-1:30 | Masalah & Solusi | Problem statement, mengapa penting |
| 1:30-3:00 | Demo | Live demo fitur utama (3-4 fitur) |
| 3:00-4:30 | Teknis | Struktur data, algoritma, code highlight |
| 4:30-5:30 | AI Usage | Bagaimana AI membantu, apa yang dipelajari |
| 5:30-6:00 | Kesimpulan | Refleksi, rencana pengembangan |
| 6:00-7:00 | Q&A | Pertanyaan dari dosen/teman |

### 14.7.2 Tips Presentasi Teknis

1. **Persiapkan demo** — pastikan program berjalan SEBELUM presentasi
2. **Siapkan data dummy** — jangan bergantung pada input live
3. **Highlight kode penting** — jangan tampilkan semua kode, fokus pada bagian menarik
4. **Ceritakan proses** — lebih menarik dari sekadar menunjukkan hasil
5. **Jujur tentang limitasi** — "Fitur ini belum sempurna karena..." lebih baik dari mengabaikan

### 14.7.3 Live Demo Tips

```python
# Siapkan data demo di awal program
def muat_data_demo():
    """Memuat data contoh untuk demo presentasi."""
    katalog = {
        "BK-0001": {"judul": "Laskar Pelangi", "pengarang": "Andrea Hirata",
                     "tahun": 2005, "kategori": "Novel", "status": "tersedia"},
        "BK-0002": {"judul": "Bumi Manusia", "pengarang": "Pramoedya A.T.",
                     "tahun": 1980, "kategori": "Novel", "status": "dipinjam"},
        "BK-0003": {"judul": "Algoritma dan Pemrograman", "pengarang": "Rinaldi Munir",
                     "tahun": 2021, "kategori": "Textbook", "status": "tersedia"},
        "BK-0004": {"judul": "Think Python", "pengarang": "Allen Downey",
                     "tahun": 2024, "kategori": "Textbook", "status": "tersedia"},
        "BK-0005": {"judul": "Ayat-Ayat Cinta", "pengarang": "Habiburrahman",
                     "tahun": 2004, "kategori": "Novel", "status": "tersedia"},
    }
    return katalog
```

---

## 14.8 Proyek Contoh Lengkap: Sistem Informasi Perpustakaan Mini

Berikut implementasi lengkap sebagai referensi:

```python
# ============================================================
# SISTEM INFORMASI PERPUSTAKAAN MINI
# Proyek Akhir — Algoritma dan Pemrograman
# Universitas Al Azhar Indonesia — Semester Genap 2025/2026
# ============================================================

# --- Konstanta ---
SEPARATOR = "=" * 55
GARIS = "-" * 55

# --- Data Global ---
katalog = {}
riwayat_pinjam = []
counter_id = 0

# ===========================
# FUNGSI UTILITAS
# ===========================

def generate_id():
    """Menghasilkan ID buku unik."""
    global counter_id
    counter_id += 1
    return f"BK-{counter_id:04d}"

def input_valid(prompt, tipe="str"):
    """Meminta input dengan validasi tipe data."""
    while True:
        nilai = input(prompt).strip()
        if not nilai:
            print("  Input tidak boleh kosong!")
            continue
        if tipe == "int":
            try:
                return int(nilai)
            except ValueError:
                print("  Masukkan angka yang valid!")
                continue
        return nilai

# ===========================
# FUNGSI CRUD BUKU
# ===========================

def tambah_buku():
    """Menambahkan buku baru ke katalog."""
    print(f"\n{GARIS}")
    print("  TAMBAH BUKU BARU")
    print(GARIS)

    judul = input_valid("  Judul     : ")
    pengarang = input_valid("  Pengarang : ")
    tahun = input_valid("  Tahun     : ", "int")
    kategori = input_valid("  Kategori  : ")

    id_buku = generate_id()
    katalog[id_buku] = {
        'judul': judul,
        'pengarang': pengarang,
        'tahun': tahun,
        'kategori': kategori,
        'status': 'tersedia'
    }

    print(f"\n  Buku '{judul}' berhasil ditambahkan!")
    print(f"  ID Buku: {id_buku}")

def tampilkan_semua():
    """Menampilkan seluruh buku di katalog."""
    if not katalog:
        print("\n  Katalog kosong.")
        return

    print(f"\n{SEPARATOR}")
    print(f"  KATALOG PERPUSTAKAAN ({len(katalog)} buku)")
    print(SEPARATOR)
    print(f"  {'ID':<10} {'Judul':<25} {'Pengarang':<20} {'Thn':>4} {'Status':<10}")
    print(f"  {GARIS}")

    # Urutkan berdasarkan judul
    buku_terurut = sorted(katalog.items(),
                          key=lambda x: x[1]['judul'].lower())

    for id_buku, buku in buku_terurut:
        judul = buku['judul'][:23]
        pengarang = buku['pengarang'][:18]
        print(f"  {id_buku:<10} {judul:<25} {pengarang:<20} "
              f"{buku['tahun']:>4} {buku['status']:<10}")

def hapus_buku():
    """Menghapus buku dari katalog."""
    id_buku = input_valid("\n  Masukkan ID buku yang akan dihapus: ")

    if id_buku not in katalog:
        print(f"  Buku dengan ID '{id_buku}' tidak ditemukan.")
        return

    buku = katalog[id_buku]
    if buku['status'] == 'dipinjam':
        print(f"  Buku '{buku['judul']}' sedang dipinjam. Tidak bisa dihapus.")
        return

    konfirmasi = input(f"  Yakin hapus '{buku['judul']}'? (y/n): ").lower()
    if konfirmasi == 'y':
        del katalog[id_buku]
        print(f"  Buku '{buku['judul']}' berhasil dihapus.")
    else:
        print("  Penghapusan dibatalkan.")

# ===========================
# FUNGSI PENCARIAN
# ===========================

def cari_buku():
    """Mencari buku berdasarkan keyword."""
    print(f"\n{GARIS}")
    print("  CARI BUKU")
    print(f"  Kriteria: 1=Judul, 2=Pengarang, 3=Kategori")
    print(GARIS)

    pilihan = input("  Pilih kriteria (1-3): ").strip()
    kriteria_map = {"1": "judul", "2": "pengarang", "3": "kategori"}

    if pilihan not in kriteria_map:
        print("  Kriteria tidak valid!")
        return

    kriteria = kriteria_map[pilihan]
    keyword = input(f"  Masukkan keyword ({kriteria}): ").strip().lower()

    # Linear search
    hasil = []
    for id_buku, buku in katalog.items():
        if keyword in buku[kriteria].lower():
            hasil.append((id_buku, buku))

    if not hasil:
        print(f"\n  Tidak ditemukan buku dengan {kriteria} '{keyword}'.")
        return

    # Urutkan hasil berdasarkan judul
    hasil.sort(key=lambda x: x[1]['judul'].lower())

    print(f"\n  Ditemukan {len(hasil)} buku:")
    print(f"  {'ID':<10} {'Judul':<25} {'Pengarang':<20} {'Status':<10}")
    print(f"  {GARIS}")
    for id_buku, buku in hasil:
        print(f"  {id_buku:<10} {buku['judul'][:23]:<25} "
              f"{buku['pengarang'][:18]:<20} {buku['status']:<10}")

# ===========================
# FUNGSI PEMINJAMAN
# ===========================

def pinjam_buku():
    """Memproses peminjaman buku."""
    id_buku = input_valid("\n  Masukkan ID buku yang akan dipinjam: ")

    if id_buku not in katalog:
        print(f"  Buku dengan ID '{id_buku}' tidak ditemukan.")
        return

    buku = katalog[id_buku]

    if buku['status'] == 'dipinjam':
        print(f"  Buku '{buku['judul']}' sedang dipinjam orang lain.")
        return

    nama_peminjam = input_valid("  Nama peminjam: ")

    buku['status'] = 'dipinjam'
    buku['peminjam'] = nama_peminjam

    riwayat_pinjam.append({
        'id_buku': id_buku,
        'judul': buku['judul'],
        'peminjam': nama_peminjam,
        'aksi': 'pinjam'
    })

    print(f"\n  Buku '{buku['judul']}' berhasil dipinjam oleh {nama_peminjam}.")

def kembalikan_buku():
    """Memproses pengembalian buku."""
    id_buku = input_valid("\n  Masukkan ID buku yang akan dikembalikan: ")

    if id_buku not in katalog:
        print(f"  Buku dengan ID '{id_buku}' tidak ditemukan.")
        return

    buku = katalog[id_buku]

    if buku['status'] != 'dipinjam':
        print(f"  Buku '{buku['judul']}' tidak sedang dipinjam.")
        return

    peminjam = buku.get('peminjam', 'Unknown')
    buku['status'] = 'tersedia'
    buku.pop('peminjam', None)

    riwayat_pinjam.append({
        'id_buku': id_buku,
        'judul': buku['judul'],
        'peminjam': peminjam,
        'aksi': 'kembali'
    })

    print(f"\n  Buku '{buku['judul']}' berhasil dikembalikan oleh {peminjam}.")

# ===========================
# FUNGSI STATISTIK
# ===========================

def tampilkan_statistik():
    """Menampilkan statistik perpustakaan."""
    total = len(katalog)
    if total == 0:
        print("\n  Katalog kosong — belum ada statistik.")
        return

    tersedia = sum(1 for b in katalog.values() if b['status'] == 'tersedia')
    dipinjam = sum(1 for b in katalog.values() if b['status'] == 'dipinjam')

    # Hitung kategori
    kategori_count = {}
    for buku in katalog.values():
        kat = buku['kategori']
        kategori_count[kat] = kategori_count.get(kat, 0) + 1

    print(f"\n{SEPARATOR}")
    print("  STATISTIK PERPUSTAKAAN")
    print(SEPARATOR)
    print(f"  Total buku      : {total}")
    print(f"  Tersedia         : {tersedia}")
    print(f"  Dipinjam         : {dipinjam}")
    print(f"  Total transaksi  : {len(riwayat_pinjam)}")
    print(f"\n  Buku per Kategori:")

    # Urutkan kategori dari terbanyak
    for kat, jumlah in sorted(kategori_count.items(),
                               key=lambda x: x[1], reverse=True):
        bar = "█" * jumlah
        print(f"    {kat:<15} : {bar} ({jumlah})")

# ===========================
# FUNGSI MENU UTAMA
# ===========================

def tampilkan_header():
    """Menampilkan header program."""
    print(f"\n{SEPARATOR}")
    print("     SISTEM INFORMASI PERPUSTAKAAN MINI UAI")
    print("     Algoritma dan Pemrograman — 2026")
    print(SEPARATOR)

def tampilkan_menu():
    """Menampilkan menu utama."""
    print("\n  ╔═════════════ MENU ═══════════════╗")
    print("  ║  1. Tambah Buku Baru             ║")
    print("  ║  2. Tampilkan Semua Buku          ║")
    print("  ║  3. Cari Buku                     ║")
    print("  ║  4. Pinjam Buku                   ║")
    print("  ║  5. Kembalikan Buku               ║")
    print("  ║  6. Hapus Buku                    ║")
    print("  ║  7. Statistik                     ║")
    print("  ║  8. Keluar                        ║")
    print("  ╚══════════════════════════════════╝")

def main():
    """Fungsi utama program."""
    tampilkan_header()

    # Muat data demo (opsional)
    katalog["BK-0001"] = {"judul": "Laskar Pelangi", "pengarang": "Andrea Hirata",
                          "tahun": 2005, "kategori": "Novel", "status": "tersedia"}
    katalog["BK-0002"] = {"judul": "Bumi Manusia", "pengarang": "Pramoedya A.T.",
                          "tahun": 1980, "kategori": "Novel", "status": "tersedia"}
    katalog["BK-0003"] = {"judul": "Think Python", "pengarang": "Allen Downey",
                          "tahun": 2024, "kategori": "Textbook", "status": "tersedia"}
    global counter_id
    counter_id = 3

    aksi = {
        "1": tambah_buku,
        "2": tampilkan_semua,
        "3": cari_buku,
        "4": pinjam_buku,
        "5": kembalikan_buku,
        "6": hapus_buku,
        "7": tampilkan_statistik,
    }

    while True:
        tampilkan_menu()
        pilihan = input("\n  Pilih menu (1-8): ").strip()

        if pilihan == "8":
            print(f"\n  Terima kasih telah menggunakan sistem ini.")
            print(f"  Wassalamu'alaikum Warahmatullahi Wabarakatuh.\n")
            break

        if pilihan in aksi:
            aksi[pilihan]()
        else:
            print("  Pilihan tidak valid! Silakan coba lagi.")

# Jalankan program
main()
```

---

## 14.9 Rubrik Penilaian Proyek

### 14.9.1 8 Komponen Penilaian

| No | Komponen | Bobot | Deskripsi |
|----|----------|-------|-----------|
| 1 | Perumusan Masalah & Desain | 10% | Problem statement, requirements, desain top-down |
| 2 | Implementasi Kode & Fungsi | 20% | Kode berjalan, modular (minimal 5 fungsi), Python style |
| 3 | Penggunaan Struktur Data & Algoritma | 15% | Pemilihan tepat, minimal 1 searching/sorting |
| 4 | Penanganan Error & Edge Cases | 10% | Input validation, error handling, edge cases |
| 5 | Dokumentasi Kode | 10% | Docstrings, komentar, README, kode terbaca |
| 6 | Dokumentasi AI Usage | 15% | AI Usage Log lengkap dan jujur |
| 7 | Presentasi & Demo | 15% | Komunikasi jelas, demo berjalan, Q&A |
| 8 | Etika & Integritas | 5% | Kejujuran, orisinalitas, transparansi |
| | **TOTAL** | **100%** | |

### 14.9.2 Contoh Penilaian

**Nilai A (85-100):**
- Program berjalan sempurna tanpa error
- Minimal 7 fungsi dengan docstrings
- Menggunakan dict + list + searching + sorting
- Semua edge cases ditangani
- AI Usage Log detail dan reflektif
- Presentasi profesional dengan demo lancar

**Nilai B (70-84):**
- Program berjalan dengan minor bug
- Minimal 5 fungsi dengan dokumentasi cukup
- Menggunakan struktur data tepat
- Sebagian edge cases ditangani
- AI Usage Log ada tapi kurang detail
- Presentasi cukup baik

**Nilai C (55-69):**
- Program berjalan untuk fitur dasar
- Minimal 3 fungsi
- Struktur data sederhana (list saja)
- Error handling minimal
- AI Usage Log singkat
- Presentasi cukup

**Nilai D/E (<55):**
- Program tidak berjalan / banyak error
- Sedikit/tanpa fungsi
- Tidak ada AI Usage Log
- Tidak ada presentasi

---

## 14.10 10 Ide Proyek dengan Deskripsi Detail

### 1. Sistem Informasi Perpustakaan Mini
- **Fitur wajib:** CRUD buku, cari, pinjam, kembalikan, statistik
- **Struktur data:** dict (katalog), list (riwayat)
- **Algoritma:** linear search, sorted()

### 2. Aplikasi Kasir Toko/Warung
- **Fitur wajib:** Input barang, hitung total, diskon, cetak struk, laporan harian
- **Struktur data:** dict (inventory), list (transaksi)
- **Algoritma:** pencarian produk, pengurutan laporan

### 3. Game Tebak Kata Bahasa Indonesia
- **Fitur wajib:** Bank kata, hangman display, scoring, leaderboard
- **Struktur data:** list (kata), dict (skor), set (huruf tebakan)
- **Algoritma:** random selection, string matching

### 4. Sistem Antrian Rumah Sakit
- **Fitur wajib:** Daftar pasien, prioritas, panggil, statistik
- **Struktur data:** list (antrian), dict (pasien)
- **Algoritma:** priority insertion, FIFO

### 5. Tool Analisis Teks
- **Fitur wajib:** Word count, frekuensi kata, kata terpanjang, sentimen sederhana
- **Struktur data:** dict (frekuensi), list (kata), set (stopwords)
- **Algoritma:** string processing, sorting frekuensi

### 6. Buku Alamat / Kontak Manager
- **Fitur wajib:** CRUD kontak, cari by nama/nomor, grup kontak, export
- **Struktur data:** dict (kontak), set (grup)
- **Algoritma:** searching, sorting by nama

### 7. Kalkulator IPK dan Transkrip
- **Fitur wajib:** Input mata kuliah, hitung IPK, transkrip, simulasi
- **Struktur data:** list (mata kuliah), dict (bobot mutu)
- **Algoritma:** perhitungan rata-rata berbobot, sorting

### 8. Sistem Rekomendasi Menu Kantin
- **Fitur wajib:** Database menu, filter by budget/kategori, rekomendasi acak
- **Struktur data:** dict (menu), list (rekomendasi)
- **Algoritma:** filtering, sorting by harga

### 9. Sistem Voting / E-Polling
- **Fitur wajib:** Registrasi voter, voting, tabulasi, hasil + grafik ASCII
- **Struktur data:** dict (kandidat, voter), list (suara)
- **Algoritma:** counting, sorting hasil

### 10. Mini Quiz App
- **Fitur wajib:** Bank soal, quiz random, scoring, leaderboard, review jawaban
- **Struktur data:** list (soal), dict (skor pengguna)
- **Algoritma:** random selection, sorting leaderboard

---

## AI Corner: Mahir — AI sebagai Partner Proyek

**Level: Mahir**

### Workflow Lengkap Proyek dengan AI

```
FASE 1: BRAINSTORM (AI = Sparring Partner)
├── Prompt: "Saya ingin membuat [X]. Bantu brainstorm fitur."
├── Anda: Pilih dan prioritaskan fitur
└── AI TIDAK membuat keputusan final

FASE 2: DESAIN (AI = Consultant)
├── Prompt: "Rekomendasi struktur data untuk [fitur]?"
├── Anda: Evaluasi saran berdasarkan Bab 7-8
└── AI TIDAK mendesain arsitektur final

FASE 3: IMPLEMENTASI (AI = Junior Coder)
├── Prompt CRIDE untuk setiap fungsi
├── Anda: Review, test, modifikasi SETIAP kode
└── AI TIDAK submit kode tanpa review Anda

FASE 4: DEBUGGING (AI = Debugger)
├── Prompt: "Kode ini error [X]. Analisis?"
├── Anda: Pahami penjelasan, perbaiki sendiri
└── AI TIDAK di-copy-paste tanpa pemahaman

FASE 5: DOKUMENTASI (AI = Editor)
├── Prompt: "Bantu tulis README untuk proyek ini"
├── Anda: Edit, pastikan akurat, tambahkan AI Log
└── AI TIDAK menulis refleksi Anda
```

### Kapan TIDAK Boleh Menggunakan AI

- Saat UTS/UAS (closed book)
- Untuk seluruh proposal tanpa analisis sendiri
- Untuk menulis refleksi dan AI Usage Log
- Jika Anda tidak memahami kode yang dihasilkan

---

## Checklist Kesiapan Proyek

Sebelum submit, pastikan semua item terpenuhi:

```
CHECKLIST PRE-SUBMISSION
════════════════════════

Program:
□ Program berjalan tanpa error di Google Colab
□ Semua fitur utama berfungsi
□ Input validation untuk semua input pengguna
□ Minimal 5 fungsi yang modular
□ Minimal 1 penggunaan searching atau sorting
□ Menggunakan minimal 2 jenis struktur data

Dokumentasi:
□ Setiap fungsi memiliki docstring
□ Komentar pada bagian yang kompleks
□ README proyek lengkap

AI Usage:
□ AI Usage Log lengkap dan jujur
□ Setiap interaksi didokumentasikan
□ Refleksi pribadi tertulis
□ Persentase kode AI vs sendiri tertulis

Presentasi:
□ Slide/catatan presentasi siap
□ Demo sudah dicoba sebelumnya
□ Data demo tersedia
□ Siap menjawab pertanyaan tentang kode
□ Timer: 5-7 menit

Etika:
□ Tidak ada plagiarisme
□ Semua bantuan AI terdokumentasi
□ Kode yang dikumpulkan dipahami 100%
```

---

## Rangkuman

Bab 14 adalah **puncak perjalanan** Anda di mata kuliah Algoritma dan Pemrograman:

- **SDLC sederhana** (6 fase): Analisis → Desain → Implementasi → Testing → Dokumentasi → Presentasi.
- **Analisis masalah** dimulai dengan problem statement yang jelas dan requirements analysis.
- **Desain** menggunakan top-down design, pemilihan struktur data (Bab 7-8), dan sketsa algoritma.
- **Implementasi** dilakukan secara bertahap (incremental), mengintegrasikan konsep dari **seluruh Bab 1-13**.
- **Testing** mencakup manual testing, edge cases, dan debugging strategies.
- **Dokumentasi** wajib: docstrings, README, AI Usage Log, dan laporan teknis.
- **Presentasi** selama 5-7 menit: demo, penjelasan teknis, refleksi AI usage.
- **Rubrik** terdiri dari 8 komponen: masalah/desain (10%), implementasi (20%), struktur data/algoritma (15%), error handling (10%), dokumentasi kode (10%), AI Log (15%), presentasi (15%), etika (5%).
- **AI adalah partner**, bukan pengganti — semua penggunaan AI **wajib didokumentasikan** dengan jujur dan transparan.
- Proyek ini adalah bukti bahwa Anda telah menguasai **fondasi computational thinking** dan siap untuk mata kuliah lanjutan.

> **Pesan terakhir:** Proyek akhir bukan hanya tentang membuat program yang berjalan — ini tentang menunjukkan bahwa Anda bisa **berpikir seperti seorang programmer**: menganalisis masalah, merancang solusi, mengimplementasikan dengan kode, dan mendokumentasikan dengan profesional. Ini adalah awal perjalanan Anda sebagai *Problem Solver in Digital*. Semoga Allah SWT memberkahi ilmu yang Anda peroleh. *Bismillah!*

---

## Referensi

1. Downey, A. B. (2024). *Think Python* (3rd ed.). O'Reilly Media.
2. Martin, R. C. (2008). *Clean Code*. Pearson Education.
3. Guttag, J. V. (2021). *Introduction to Computation and Programming Using Python* (3rd ed.). MIT Press.
4. McConnell, S. (2004). *Code Complete* (2nd ed.). Microsoft Press.
5. Python Software Foundation. (2026). Python 3.x Documentation. https://docs.python.org/3/
6. IEEE/ACM. (2023). *Computer Science Curricula 2023*. ACM/IEEE.
7. Denny, P. et al. (2024). "Computing Education in the Era of Generative AI." *Communications of the ACM*.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
