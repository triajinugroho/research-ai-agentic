# Minggu 4: Pemodelan Requirements — Use Case dan User Story

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 4 dari 16 |
| **Topik** | Use Case Diagram, Use Case Narrative, User Stories, Acceptance Criteria, Product Backlog |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK-2 |
| **Sub-CPMK** | 2.3 (Use Case Diagram & Narrative), 2.4 (User Stories, INVEST, Backlog) |
| **Durasi** | 150 menit (3 x 50 menit) |
| **Metode** | Ceramah, workshop user story writing, backlog prioritization |

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Membuat** Use Case Diagram dengan notasi standar UML untuk memodelkan interaksi aktor dan sistem (C3)
2. **Menyusun** Use Case Narrative yang lengkap mencakup precondition, main flow, alternative flow, dan postcondition (C3)
3. **Menulis** User Stories dengan kriteria INVEST dan format standar "As a... I want... So that..." (C3)
4. **Menulis** Acceptance Criteria dalam format Given-When-Then (Gherkin) untuk setiap User Story (C3)
5. **Menerapkan** teknik prioritisasi MoSCoW dan Story Points untuk mengelola Product Backlog (C3)

---

## Materi Pembelajaran

### 4.1 Use Case Modeling — Fondasi Pemodelan Requirements

#### 4.1.1 Apa Itu Use Case?

Use Case adalah teknik untuk menangkap **requirements fungsional** dari perspektif pengguna (*user-centric*). Teknik ini dikembangkan oleh Ivar Jacobson pada tahun 1992 dan menjadi bagian standar UML.

```
┌─────────────────────────────────────────────────────────────────┐
│                USE CASE MODELING                                 │
│                                                                  │
│  Menjawab pertanyaan fundamental:                               │
│                                                                  │
│  ┌──────────────────┐    ┌──────────────────────────────────┐  │
│  │   SIAPA?          │    │  Actor (pengguna/sistem eksternal)│  │
│  ├──────────────────┤    ├──────────────────────────────────┤  │
│  │   APA?            │    │  Use Case (fungsionalitas sistem) │  │
│  ├──────────────────┤    ├──────────────────────────────────┤  │
│  │   BAGAIMANA?      │    │  Use Case Narrative (alur detail) │  │
│  └──────────────────┘    └──────────────────────────────────┘  │
│                                                                  │
│  Use Case BUKAN diagram alir (flowchart)!                       │
│  Use Case menggambarkan APA yang dilakukan, bukan BAGAIMANA.    │
└─────────────────────────────────────────────────────────────────┘
```

#### 4.1.2 Komponen Use Case Diagram

| Komponen | Simbol | Deskripsi | Contoh |
|----------|--------|-----------|--------|
| **Actor** | Stick figure | Entitas eksternal yang berinteraksi dengan sistem | Mahasiswa, Admin, Sistem Pembayaran |
| **Use Case** | Oval/Ellipse | Fungsionalitas yang disediakan sistem | Daftar Mata Kuliah, Bayar SPP |
| **System Boundary** | Rectangle | Batas sistem yang dimodelkan | Sistem Akademik UAI |
| **Association** | Garis lurus | Hubungan aktor dengan use case | Mahasiswa --- Daftar MK |
| **Include** | `<<include>>` | Use case yang WAJIB dipanggil | Login <<include>> Validasi |
| **Extend** | `<<extend>>` | Use case OPSIONAL | Bayar <<extend>> Cetak Kwitansi |
| **Generalization** | Panah segitiga | Pewarisan antar aktor/use case | Admin --|> User |

#### 4.1.3 Relasi dalam Use Case Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│ RELASI USE CASE                                                  │
│                                                                  │
│ 1. INCLUDE (<<include>>) — Wajib dipanggil                     │
│                                                                  │
│    ┌────────────┐  <<include>>  ┌──────────────┐               │
│    │ Lihat Nilai│─────────────▶│ Login Sistem  │               │
│    └────────────┘              └──────────────┘               │
│    "Untuk melihat nilai, mahasiswa HARUS login terlebih dahulu" │
│                                                                  │
│ 2. EXTEND (<<extend>>) — Opsional, conditional                 │
│                                                                  │
│    ┌────────────┐  <<extend>>  ┌──────────────┐               │
│    │ Cetak PDF  │─ ─ ─ ─ ─ ─▶│ Lihat Nilai  │               │
│    └────────────┘              └──────────────┘               │
│    "Setelah melihat nilai, mahasiswa BISA mencetak PDF"        │
│                                                                  │
│ 3. GENERALIZATION — Pewarisan                                   │
│                                                                  │
│    ┌────────────┐                                               │
│    │   Admin    │                                               │
│    └─────┬──────┘                                               │
│          △                                                       │
│    ┌─────┴──────┐                                               │
│    │   User     │                                               │
│    └────────────┘                                               │
│    "Admin adalah spesialisasi dari User"                        │
└─────────────────────────────────────────────────────────────────┘
```

#### 4.1.4 Contoh: Use Case Diagram Sistem Antrian Puskesmas

```
┌─────────────────────────────────────────────────────────────────┐
│                  SISTEM ANTRIAN PUSKESMAS                         │
│                                                                  │
│                        ┌─────────────────────┐                  │
│   ┌───┐               │  Daftar Antrian      │                  │
│   │ P │──────────────▶│  Online              │                  │
│   │ a │               └─────────────────────┘                  │
│   │ s │                                                         │
│   │ i │               ┌─────────────────────┐                  │
│   │ e │──────────────▶│  Lihat Status        │                  │
│   │ n │               │  Antrian             │                  │
│   └───┘               └─────────────────────┘                  │
│                               │                                  │
│                          <<extend>>                              │
│                               │                                  │
│                        ┌──────┴──────────────┐                  │
│                        │  Terima Notifikasi   │                  │
│                        │  WhatsApp            │                  │
│                        └─────────────────────┘                  │
│                                                                  │
│   ┌───┐               ┌─────────────────────┐                  │
│   │ P │──────────────▶│  Panggil Pasien      │                  │
│   │ e │               └─────────────────────┘                  │
│   │ t │                       │                                  │
│   │ u │                  <<include>>                             │
│   │ g │                       │                                  │
│   │ a │               ┌──────┴──────────────┐                  │
│   │ s │               │  Update Status       │                  │
│   └───┘               │  Antrian             │                  │
│     │                 └─────────────────────┘                  │
│     │                                                           │
│     │                 ┌─────────────────────┐                  │
│     └────────────────▶│  Input Rekam Medis   │                  │
│                        └─────────────────────┘                  │
│                               │                                  │
│                          <<include>>                             │
│                               │                                  │
│   ┌───┐               ┌──────┴──────────────┐                  │
│   │ D │──────────────▶│  Validasi Data       │                  │
│   │ o │               │  Pasien              │                  │
│   │ k │               └─────────────────────┘                  │
│   │ t │                                                         │
│   │ e │               ┌─────────────────────┐                  │
│   │ r │──────────────▶│  Tulis Resep Obat    │                  │
│   └───┘               └─────────────────────┘                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

#### 4.1.5 Contoh: Use Case Diagram Sistem Perpustakaan Digital UAI

```
┌─────────────────────────────────────────────────────────────────┐
│              SISTEM PERPUSTAKAAN DIGITAL UAI                     │
│                                                                  │
│  ┌───────────┐      ┌──────────────────────┐                   │
│  │ Mahasiswa │─────▶│ Cari Buku            │                   │
│  └───────────┘      └──────────────────────┘                   │
│       │              ┌──────────────────────┐                   │
│       ├─────────────▶│ Pinjam Buku          │                   │
│       │              └──────────────────────┘                   │
│       │                      │ <<include>>                      │
│       │              ┌───────┴──────────────┐                   │
│       │              │ Cek Ketersediaan     │                   │
│       │              └──────────────────────┘                   │
│       │              ┌──────────────────────┐                   │
│       ├─────────────▶│ Kembalikan Buku      │                   │
│       │              └──────────────────────┘                   │
│       │                      │ <<extend>>                       │
│       │              ┌───────┴──────────────┐                   │
│       │              │ Bayar Denda          │                   │
│       │              └──────────────────────┘                   │
│       │              ┌──────────────────────┐                   │
│       └─────────────▶│ Lihat Riwayat        │                   │
│                      └──────────────────────┘                   │
│                                                                  │
│  ┌───────────┐      ┌──────────────────────┐                   │
│  │ Pustakawan│─────▶│ Kelola Katalog       │                   │
│  └───────────┘      └──────────────────────┘                   │
│       │              ┌──────────────────────┐                   │
│       ├─────────────▶│ Kelola Peminjaman    │                   │
│       │              └──────────────────────┘                   │
│       │              ┌──────────────────────┐                   │
│       └─────────────▶│ Lihat Laporan        │                   │
│                      └──────────────────────┘                   │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Use Case Narrative — Detail Alur Interaksi

#### 4.2.1 Template Use Case Narrative

Use Case Diagram memberikan gambaran tingkat tinggi (*big picture*), sedangkan **Use Case Narrative** memberikan detail langkah-langkah interaksi.

```
┌─────────────────────────────────────────────────────────────────┐
│           HUBUNGAN DIAGRAM dan NARRATIVE                         │
│                                                                  │
│  Use Case Diagram          Use Case Narrative                   │
│  (overview visual)         (detail per use case)                │
│                                                                  │
│  ┌───────┐                 UC-001: Pinjam Buku                  │
│  │ Pinjam│  ──────────▶   - Precondition                       │
│  │ Buku  │                 - Main Flow (step 1-8)               │
│  └───────┘                 - Alternative Flow                   │
│                            - Postcondition                      │
│                            - Business Rules                     │
│                                                                  │
│  Setiap oval di diagram = 1 dokumen narrative                   │
└─────────────────────────────────────────────────────────────────┘
```

#### 4.2.2 Contoh Use Case Narrative: Pinjam Buku

| Elemen | Detail |
|--------|--------|
| **UC-ID** | UC-003 |
| **Nama** | Pinjam Buku |
| **Aktor Primer** | Mahasiswa |
| **Aktor Sekunder** | Sistem Perpustakaan |
| **Deskripsi** | Mahasiswa meminjam buku dari perpustakaan digital |
| **Precondition** | 1. Mahasiswa sudah login ke sistem |
| | 2. Mahasiswa tidak memiliki denda yang belum dibayar |
| | 3. Jumlah peminjaman aktif < 5 buku |
| **Trigger** | Mahasiswa menekan tombol "Pinjam" pada halaman detail buku |

**Main Flow (Alur Utama):**

| Step | Aktor | Sistem |
|------|-------|--------|
| 1 | Mahasiswa memilih buku yang ingin dipinjam | — |
| 2 | — | Sistem menampilkan halaman detail buku (judul, penulis, status) |
| 3 | Mahasiswa menekan tombol "Pinjam Buku" | — |
| 4 | — | Sistem memeriksa ketersediaan buku (stok > 0) |
| 5 | — | Sistem memeriksa kuota peminjaman mahasiswa (< 5 buku) |
| 6 | — | Sistem membuat record peminjaman baru |
| 7 | — | Sistem mengurangi stok buku sebanyak 1 |
| 8 | — | Sistem menampilkan konfirmasi dan tanggal pengembalian (14 hari) |

**Alternative Flows (Alur Alternatif):**

| ID | Kondisi | Aksi |
|----|---------|------|
| AF-1 | Buku tidak tersedia (stok = 0) pada step 4 | Sistem menampilkan pesan "Buku sedang dipinjam semua" dan opsi "Masuk Daftar Tunggu" |
| AF-2 | Kuota peminjaman penuh pada step 5 | Sistem menampilkan pesan "Kuota peminjaman Anda penuh. Kembalikan buku terlebih dahulu." |
| AF-3 | Mahasiswa membatalkan pada step 3 | Sistem kembali ke halaman detail buku |

**Postcondition:**
- Record peminjaman tersimpan di database
- Stok buku berkurang 1
- Tanggal pengembalian terset (hari ini + 14 hari)
- Mahasiswa mendapat notifikasi konfirmasi via email

**Business Rules:**
- Maksimal 5 buku dipinjam secara bersamaan
- Durasi peminjaman: 14 hari kalender
- Denda keterlambatan: Rp 1.000/hari/buku

#### 4.2.3 Contoh Use Case Narrative: Daftar Antrian Puskesmas

| Elemen | Detail |
|--------|--------|
| **UC-ID** | UC-001 |
| **Nama** | Daftar Antrian Online |
| **Aktor Primer** | Pasien |
| **Deskripsi** | Pasien mendaftar antrian puskesmas secara online |
| **Precondition** | Pasien memiliki NIK yang terdaftar |
| **Trigger** | Pasien membuka halaman pendaftaran |

**Main Flow:**

| Step | Aktor | Sistem |
|------|-------|--------|
| 1 | Pasien memasukkan NIK | — |
| 2 | — | Sistem memvalidasi NIK terhadap database kependudukan |
| 3 | — | Sistem menampilkan data pasien (nama, alamat) |
| 4 | Pasien memilih poli tujuan (Umum/Gigi/KIA) | — |
| 5 | Pasien memilih tanggal kunjungan | — |
| 6 | — | Sistem mengecek kuota poli pada tanggal tersebut |
| 7 | — | Sistem membuat nomor antrian |
| 8 | — | Sistem mengirim konfirmasi via WhatsApp |

### 4.3 User Stories — Format Agile untuk Requirements

#### 4.3.1 Apa Itu User Story?

User Story adalah deskripsi **singkat** tentang sebuah fitur dari perspektif **pengguna akhir** (*end user*). User Story menjadi unit kerja dasar dalam Agile/Scrum.

```
┌─────────────────────────────────────────────────────────────────┐
│                    FORMAT USER STORY                              │
│                                                                  │
│    ┌───────────────────────────────────────────────────────┐    │
│    │                                                       │    │
│    │  As a    [ROLE]                                       │    │
│    │  I want  [FEATURE/ACTION]                             │    │
│    │  So that [BENEFIT/VALUE]                              │    │
│    │                                                       │    │
│    └───────────────────────────────────────────────────────┘    │
│                                                                  │
│    Dalam Bahasa Indonesia:                                       │
│    ┌───────────────────────────────────────────────────────┐    │
│    │                                                       │    │
│    │  Sebagai  [PERAN]                                     │    │
│    │  Saya ingin [FITUR/AKSI]                              │    │
│    │  Agar      [MANFAAT/NILAI]                            │    │
│    │                                                       │    │
│    └───────────────────────────────────────────────────────┘    │
│                                                                  │
│  Contoh:                                                         │
│  "As a mahasiswa, I want mencari buku berdasarkan judul,        │
│   so that saya bisa menemukan buku yang dibutuhkan dengan cepat"│
└─────────────────────────────────────────────────────────────────┘
```

#### 4.3.2 Contoh User Stories — Sistem Perpustakaan UAI

```python
# Representasi User Stories dalam Python

user_stories = [
    {
        "id": "US-001",
        "role": "mahasiswa",
        "want": "mencari buku berdasarkan judul, penulis, atau ISBN",
        "benefit": "saya bisa menemukan buku yang dibutuhkan dengan cepat",
        "priority": "Must",
        "points": 3
    },
    {
        "id": "US-002",
        "role": "mahasiswa",
        "want": "melihat status ketersediaan buku secara real-time",
        "benefit": "saya tidak perlu datang ke perpustakaan untuk mengecek",
        "priority": "Must",
        "points": 2
    },
    {
        "id": "US-003",
        "role": "mahasiswa",
        "want": "meminjam buku secara online",
        "benefit": "saya bisa reservasi buku dari mana saja",
        "priority": "Must",
        "points": 5
    },
    {
        "id": "US-004",
        "role": "pustakawan",
        "want": "melihat daftar peminjaman yang terlambat",
        "benefit": "saya bisa mengirim reminder ke mahasiswa",
        "priority": "Should",
        "points": 3
    },
    {
        "id": "US-005",
        "role": "pustakawan",
        "want": "menambah dan mengupdate data buku baru",
        "benefit": "katalog perpustakaan selalu terbaru",
        "priority": "Must",
        "points": 3
    },
]

# Format output yang rapi
for story in user_stories:
    print(f"[{story['id']}] ({story['priority']}, {story['points']} pts)")
    print(f"  As a {story['role']},")
    print(f"  I want {story['want']},")
    print(f"  So that {story['benefit']}.")
    print()
```

**Output:**
```
[US-001] (Must, 3 pts)
  As a mahasiswa,
  I want mencari buku berdasarkan judul, penulis, atau ISBN,
  So that saya bisa menemukan buku yang dibutuhkan dengan cepat.

[US-002] (Must, 2 pts)
  As a mahasiswa,
  I want melihat status ketersediaan buku secara real-time,
  So that saya tidak perlu datang ke perpustakaan untuk mengecek.

[US-003] (Must, 5 pts)
  As a mahasiswa,
  I want meminjam buku secara online,
  So that saya bisa reservasi buku dari mana saja.

[US-004] (Should, 3 pts)
  As a pustakawan,
  I want melihat daftar peminjaman yang terlambat,
  So that saya bisa mengirim reminder ke mahasiswa.

[US-005] (Must, 3 pts)
  As a pustakawan,
  I want menambah dan mengupdate data buku baru,
  So that katalog perpustakaan selalu terbaru.
```

#### 4.3.3 Contoh User Stories — Sistem E-Commerce UMKM Batik

```python
# User Stories untuk platform e-commerce batik UMKM Yogyakarta

umkm_stories = [
    {
        "id": "US-E01",
        "story": "As a pembeli, I want melihat katalog batik berdasarkan motif daerah, "
                 "so that saya bisa menemukan batik khas daerah yang dicari",
        "priority": "Must",
        "points": 3
    },
    {
        "id": "US-E02",
        "story": "As a pembeli, I want membayar menggunakan QRIS, "
                 "so that saya bisa bayar dari e-wallet manapun",
        "priority": "Must",
        "points": 8
    },
    {
        "id": "US-E03",
        "story": "As a penjual UMKM, I want mengupload foto produk dengan auto-compress, "
                 "so that foto tetap bagus meskipun koneksi internet lambat",
        "priority": "Should",
        "points": 5
    },
    {
        "id": "US-E04",
        "story": "As a penjual UMKM, I want melihat laporan penjualan bulanan, "
                 "so that saya bisa memantau perkembangan bisnis",
        "priority": "Should",
        "points": 5
    },
    {
        "id": "US-E05",
        "story": "As a admin, I want memverifikasi identitas penjual UMKM, "
                 "so that hanya penjual terverifikasi yang bisa berjualan",
        "priority": "Must",
        "points": 5
    },
]
```

### 4.4 INVEST Criteria — Standar Kualitas User Story

#### 4.4.1 Penjelasan Detail INVEST

```
┌─────────────────────────────────────────────────────────────────┐
│                     INVEST CRITERIA                              │
│                                                                  │
│  ┌─── I ─── Independent ────────────────────────────────────┐   │
│  │  Story tidak bergantung pada story lain.                  │   │
│  │  Bisa dikerjakan dalam urutan apapun.                     │   │
│  │                                                           │   │
│  │  Buruk: "As a user, I want login" lalu "As a user,       │   │
│  │     I want lihat profil" (tightly coupled)                │   │
│  │  Baik: Pisahkan sehingga masing-masing berdiri sendiri    │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌─── N ─── Negotiable ────────────────────────────────────┐   │
│  │  Bukan kontrak tetap — bisa didiskusikan antara          │   │
│  │  developer dan product owner.                             │   │
│  │                                                           │   │
│  │  Buruk: "Gunakan dropdown dengan warna biru #0066CC"      │   │
│  │  Baik: "User bisa memilih kategori buku"                  │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌─── V ─── Valuable ──────────────────────────────────────┐   │
│  │  Memberikan nilai nyata bagi pengguna atau bisnis.        │   │
│  │                                                           │   │
│  │  Buruk: "Refactor database schema" (teknis, bukan value)  │   │
│  │  Baik: "As a mahasiswa, I want ... so that ..."           │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌─── E ─── Estimable ─────────────────────────────────────┐   │
│  │  Tim bisa memperkirakan effort yang dibutuhkan.           │   │
│  │                                                           │   │
│  │  Buruk: "Buat sistem yang cepat" (terlalu abstrak)        │   │
│  │  Baik: "Pencarian buku merespon dalam < 2 detik"          │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌─── S ─── Small ─────────────────────────────────────────┐   │
│  │  Cukup kecil untuk diselesaikan dalam 1 sprint.           │   │
│  │                                                           │   │
│  │  Buruk: "Buat seluruh fitur pembayaran" (epic)            │   │
│  │  Baik: "Integrasi pembayaran via QRIS" (1 sprint)         │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌─── T ─── Testable ──────────────────────────────────────┐   │
│  │  Bisa diverifikasi bahwa story sudah selesai.             │   │
│  │                                                           │   │
│  │  Buruk: "Sistem harus user-friendly" (subjektif)          │   │
│  │  Baik: "Pencarian menampilkan hasil dalam 2 detik"        │   │
│  └───────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

#### 4.4.2 Validasi INVEST dengan Python

```python
def validate_invest(story: dict) -> dict:
    """Validasi apakah user story memenuhi kriteria INVEST."""
    
    results = {}
    
    # Independent: cek apakah ada dependency
    results['Independent'] = len(story.get('dependencies', [])) == 0
    
    # Negotiable: cek apakah tidak terlalu teknis/spesifik
    technical_keywords = ['database', 'SQL', 'API endpoint', 'CSS color']
    results['Negotiable'] = not any(
        kw.lower() in story.get('want', '').lower() 
        for kw in technical_keywords
    )
    
    # Valuable: cek apakah ada benefit
    results['Valuable'] = len(story.get('benefit', '')) > 10
    
    # Estimable: cek apakah ada story points
    results['Estimable'] = story.get('points', 0) > 0
    
    # Small: cek apakah story points tidak terlalu besar (> 13)
    results['Small'] = 0 < story.get('points', 0) <= 13
    
    # Testable: cek apakah ada acceptance criteria
    results['Testable'] = len(story.get('acceptance_criteria', [])) > 0
    
    return results

# Contoh penggunaan
story_bagus = {
    "id": "US-001",
    "role": "mahasiswa",
    "want": "mencari buku berdasarkan judul",
    "benefit": "saya bisa menemukan buku yang dibutuhkan dengan cepat",
    "dependencies": [],
    "points": 3,
    "acceptance_criteria": [
        "Given mahasiswa di halaman pencarian, "
        "When memasukkan keyword 'algoritma', "
        "Then sistem menampilkan buku yang mengandung kata 'algoritma'"
    ]
}

hasil = validate_invest(story_bagus)
for kriteria, status in hasil.items():
    icon = "PASS" if status else "FAIL"
    print(f"  [{icon}] {kriteria}")

# Output:
#   [PASS] Independent
#   [PASS] Negotiable
#   [PASS] Valuable
#   [PASS] Estimable
#   [PASS] Small
#   [PASS] Testable
```

### 4.5 Acceptance Criteria — Format Given-When-Then (Gherkin)

#### 4.5.1 Struktur Gherkin

Acceptance Criteria mendefinisikan **kapan** sebuah User Story dianggap **selesai** (*Definition of Done*). Format Given-When-Then (GWT) berasal dari Behaviour-Driven Development (BDD).

```
┌─────────────────────────────────────────────────────────────────┐
│              FORMAT GIVEN-WHEN-THEN                              │
│                                                                  │
│  GIVEN  [konteks/kondisi awal]                                  │
│  WHEN   [aksi yang dilakukan pengguna]                          │
│  THEN   [hasil yang diharapkan]                                 │
│  AND    [hasil tambahan] (opsional)                             │
│                                                                  │
│  Analogi kehidupan sehari-hari:                                  │
│  GIVEN  saya berada di halte TransJakarta Harmoni               │
│  WHEN   saya tap kartu Flazz di mesin                           │
│  THEN   gerbang terbuka dan saldo berkurang Rp 3.500            │
│  AND    layar menampilkan sisa saldo                            │
└─────────────────────────────────────────────────────────────────┘
```

#### 4.5.2 Contoh Acceptance Criteria — Sistem Perpustakaan

```gherkin
# AC-001: Pencarian Buku (Happy Path)
Feature: Pencarian Buku Perpustakaan

  Scenario: Pencarian buku berdasarkan judul
    Given mahasiswa sudah login ke sistem perpustakaan
    And mahasiswa berada di halaman pencarian
    When mahasiswa memasukkan keyword "algoritma" di kolom pencarian
    And mahasiswa menekan tombol "Cari"
    Then sistem menampilkan daftar buku yang mengandung kata "algoritma"
    And setiap buku menampilkan judul, penulis, dan status ketersediaan
    And jumlah hasil pencarian ditampilkan di atas daftar
    And hasil diurutkan berdasarkan relevansi

  Scenario: Pencarian buku tanpa hasil
    Given mahasiswa sudah login ke sistem perpustakaan
    When mahasiswa mencari buku dengan keyword "xyzabc123"
    Then sistem menampilkan pesan "Tidak ditemukan buku dengan keyword tersebut"
    And sistem menampilkan saran: "Coba gunakan keyword yang berbeda"
```

```gherkin
# AC-002: Peminjaman Buku (Happy Path + Edge Cases)
Feature: Peminjaman Buku

  Scenario: Peminjaman buku berhasil
    Given mahasiswa sudah login dan memiliki 2 peminjaman aktif
    And buku "Clean Code" memiliki stok 3
    When mahasiswa menekan tombol "Pinjam" pada buku "Clean Code"
    Then sistem membuat record peminjaman baru
    And stok buku "Clean Code" berkurang menjadi 2
    And tanggal pengembalian ditetapkan 14 hari dari sekarang
    And mahasiswa menerima konfirmasi via email

  Scenario: Peminjaman gagal karena kuota penuh
    Given mahasiswa sudah login dan memiliki 5 peminjaman aktif
    When mahasiswa menekan tombol "Pinjam" pada buku apapun
    Then sistem menampilkan pesan "Kuota peminjaman Anda penuh (5/5)"
    And tombol "Pinjam" menjadi disabled
```

#### 4.5.3 Contoh Acceptance Criteria — Sistem Antrian Puskesmas

```gherkin
Feature: Pendaftaran Antrian Online Puskesmas

  Scenario: Pendaftaran antrian berhasil
    Given pasien memiliki NIK yang valid
    And poli Umum masih memiliki kuota pada tanggal yang dipilih
    When pasien mengisi form pendaftaran dengan NIK dan memilih poli Umum
    And pasien memilih tanggal kunjungan besok
    Then sistem membuat nomor antrian (format: U-001)
    And sistem mengirim konfirmasi via WhatsApp
    And pesan berisi nomor antrian, tanggal, dan estimasi waktu

  Scenario: Kuota poli sudah penuh
    Given kuota poli Gigi pada tanggal 15 April 2026 sudah penuh (30/30)
    When pasien memilih poli Gigi pada tanggal 15 April 2026
    Then sistem menampilkan pesan "Kuota poli Gigi tanggal 15 April sudah penuh"
    And sistem menawarkan tanggal alternatif terdekat yang masih tersedia
```

#### 4.5.4 Contoh Acceptance Criteria — Aplikasi Ruangguru

```gherkin
Feature: Pencarian Tutor Online

  Scenario: Filter tutor berdasarkan mata pelajaran
    Given siswa sudah login ke aplikasi Ruangguru
    When siswa memilih filter mata pelajaran "Matematika SMA"
    And siswa memilih filter rating minimal 4.5
    Then sistem menampilkan daftar tutor Matematika SMA dengan rating >= 4.5
    And setiap tutor menampilkan nama, rating, jumlah sesi, dan harga per sesi
    And daftar diurutkan berdasarkan rating tertinggi
```

#### 4.5.5 Implementasi Acceptance Criteria sebagai Test (Python)

```python
# Acceptance Criteria bisa langsung diterjemahkan menjadi automated test

import pytest

class TestPencarianBuku:
    """Test berdasarkan AC-001: Pencarian Buku."""
    
    def test_pencarian_berdasarkan_judul(self, client, sample_books):
        """
        GIVEN mahasiswa sudah login
        WHEN mahasiswa mencari buku dengan keyword 'algoritma'
        THEN sistem menampilkan buku yang mengandung kata 'algoritma'
        """
        # Given
        client.login(username="mahasiswa01", password="pass123")
        
        # When
        response = client.get("/api/buku?q=algoritma")
        
        # Then
        assert response.status_code == 200
        data = response.get_json()
        assert len(data['results']) > 0
        for buku in data['results']:
            assert 'algoritma' in buku['judul'].lower()
            assert 'penulis' in buku
            assert 'status' in buku
    
    def test_pencarian_tanpa_hasil(self, client):
        """
        GIVEN mahasiswa sudah login
        WHEN mahasiswa mencari buku dengan keyword yang tidak ada
        THEN sistem menampilkan pesan tidak ditemukan
        """
        client.login(username="mahasiswa01", password="pass123")
        response = client.get("/api/buku?q=xyzabc123")
        
        assert response.status_code == 200
        data = response.get_json()
        assert len(data['results']) == 0
        assert 'Tidak ditemukan' in data['message']
```

### 4.6 Product Backlog dan Prioritisasi

#### 4.6.1 Apa Itu Product Backlog?

Product Backlog adalah **daftar semua fitur, perbaikan, dan pekerjaan** yang perlu dilakukan pada produk, diurutkan berdasarkan prioritas.

```
┌─────────────────────────────────────────────────────────────────┐
│                     PRODUCT BACKLOG                               │
│                                                                  │
│  Prioritas tinggi (atas) ke rendah (bawah)                      │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  SPRINT 1  │  US-001: Pencarian buku (3 pts)    [Must]   │   │
│  │            │  US-003: Pinjam buku online (5 pts) [Must]   │   │
│  │            │  US-005: Kelola katalog (3 pts)     [Must]   │   │
│  ├────────────┼──────────────────────────────────────────────┤   │
│  │  SPRINT 2  │  US-002: Status real-time (2 pts)   [Must]   │   │
│  │            │  US-004: Daftar terlambat (3 pts)   [Should] │   │
│  │            │  US-006: Notifikasi email (3 pts)   [Should] │   │
│  ├────────────┼──────────────────────────────────────────────┤   │
│  │  SPRINT 3  │  US-007: Rekomendasi buku (5 pts)   [Could]  │   │
│  │            │  US-008: Export laporan PDF (3 pts)  [Could]  │   │
│  ├────────────┼──────────────────────────────────────────────┤   │
│  │  BACKLOG   │  US-009: Mobile app (13 pts)        [Won't]  │   │
│  │            │  US-010: AI recommendation (8 pts)   [Won't]  │   │
│  └────────────┴──────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

#### 4.6.2 MoSCoW Method — Teknik Prioritisasi

| Prioritas | Deskripsi | Persentase | Contoh (Perpustakaan) |
|-----------|-----------|------------|----------------------|
| **Must** have | Wajib ada, sistem tidak bisa berjalan tanpa ini | ~60% | Login, pencarian buku, peminjaman, pengembalian |
| **Should** have | Penting tapi tidak kritis untuk rilis pertama | ~20% | Filter pencarian, notifikasi, laporan keterlambatan |
| **Could** have | Nice to have, meningkatkan user experience | ~15% | Dark mode, export PDF, rating buku |
| **Won't** have (now) | Tidak untuk rilis ini, mungkin rilis selanjutnya | ~5% | Mobile app, AI recommendation, integrasi OPAC nasional |

#### 4.6.3 Story Points — Estimasi Effort

Story Points menggunakan skala Fibonacci karena ketidakpastian meningkat seiring kompleksitas:

```
┌────────────────────────────────────────────────────────────────┐
│  FIBONACCI STORY POINTS                                         │
│                                                                  │
│  1    2    3    5    8    13    21                               │
│  │    │    │    │    │     │     │                               │
│  ▼    ▼    ▼    ▼    ▼     ▼     ▼                               │
│ Sangat  Kecil  Sedang  Besar  Sangat  Epic!   Pecah            │
│ kecil                         besar           jadi              │
│                                               story             │
│                                               lebih kecil       │
│                                                                  │
│  Contoh:                                                        │
│  1 pt  = Ubah label tombol                                      │
│  2 pts = Tambah field di form                                   │
│  3 pts = CRUD sederhana (satu tabel)                            │
│  5 pts = Fitur dengan validasi dan relasi antar tabel           │
│  8 pts = Integrasi API eksternal (payment gateway)              │
│  13 pts = Fitur kompleks (real-time notification system)        │
│  21+ pts = Terlalu besar! Perlu dipecah (split)                 │
└────────────────────────────────────────────────────────────────┘
```

#### 4.6.4 Implementasi Product Backlog dengan Python

```python
class UserStory:
    """Representasi sebuah User Story dalam Product Backlog."""
    
    MOSCOW_ORDER = {"Must": 1, "Should": 2, "Could": 3, "Won't": 4}
    
    def __init__(self, story_id, role, want, benefit, priority, points):
        self.story_id = story_id
        self.role = role
        self.want = want
        self.benefit = benefit
        self.priority = priority  # MoSCoW
        self.points = points      # Story Points (Fibonacci)
        self.status = "To Do"
    
    def __repr__(self):
        return f"[{self.story_id}] ({self.priority}, {self.points}pts) {self.want}"


class ProductBacklog:
    """Mengelola Product Backlog yang terurut berdasarkan prioritas."""
    
    def __init__(self):
        self.stories = []
    
    def add_story(self, story: UserStory):
        self.stories.append(story)
        self._sort()
    
    def _sort(self):
        """Urutkan: MoSCoW priority dulu, lalu story points (kecil dulu)."""
        self.stories.sort(
            key=lambda s: (UserStory.MOSCOW_ORDER[s.priority], s.points)
        )
    
    def get_sprint_candidates(self, velocity: int) -> list:
        """Ambil stories yang muat dalam sprint berdasarkan velocity."""
        candidates = []
        total_points = 0
        for story in self.stories:
            if story.status == "To Do" and total_points + story.points <= velocity:
                candidates.append(story)
                total_points += story.points
        return candidates
    
    def display(self):
        """Tampilkan seluruh backlog."""
        print("=" * 60)
        print("PRODUCT BACKLOG")
        print("=" * 60)
        for story in self.stories:
            print(f"  {story}")
        total = sum(s.points for s in self.stories)
        print(f"\nTotal: {len(self.stories)} stories, {total} points")


# Contoh penggunaan
backlog = ProductBacklog()
backlog.add_story(UserStory("US-001", "mahasiswa", "mencari buku", "cepat menemukan", "Must", 3))
backlog.add_story(UserStory("US-002", "mahasiswa", "lihat status buku", "tidak perlu ke perpus", "Must", 2))
backlog.add_story(UserStory("US-003", "mahasiswa", "pinjam buku online", "reservasi dari mana saja", "Must", 5))
backlog.add_story(UserStory("US-004", "pustakawan", "lihat daftar terlambat", "kirim reminder", "Should", 3))
backlog.add_story(UserStory("US-005", "pustakawan", "kelola katalog", "data selalu update", "Must", 3))
backlog.add_story(UserStory("US-006", "mahasiswa", "rekomendasi buku", "temukan buku relevan", "Could", 5))

backlog.display()

# Sprint Planning: velocity = 10 points
print("\n--- Sprint 1 (velocity: 10 pts) ---")
sprint_1 = backlog.get_sprint_candidates(velocity=10)
for s in sprint_1:
    print(f"  {s}")
```

**Output:**
```
============================================================
PRODUCT BACKLOG
============================================================
  [US-002] (Must, 2pts) lihat status buku
  [US-001] (Must, 3pts) mencari buku
  [US-005] (Must, 3pts) kelola katalog
  [US-003] (Must, 5pts) pinjam buku online
  [US-004] (Should, 3pts) lihat daftar terlambat
  [US-006] (Could, 5pts) rekomendasi buku

Total: 6 stories, 21 points

--- Sprint 1 (velocity: 10 pts) ---
  [US-002] (Must, 2pts) lihat status buku
  [US-001] (Must, 3pts) mencari buku
  [US-005] (Must, 3pts) kelola katalog
```

### 4.7 User Story Mapping — Visualisasi Keseluruhan Produk

#### 4.7.1 Konsep User Story Mapping

User Story Mapping (Jeff Patton, 2014) menyusun stories dalam peta 2D:
- **Horizontal**: Urutan aktivitas pengguna (*user journey*)
- **Vertikal**: Detail/prioritas (atas = penting, bawah = nice-to-have)

```
┌──────────────────────────────────────────────────────────────────────┐
│                    USER STORY MAP — Perpustakaan UAI                  │
│                                                                      │
│  Backbone (User Activities):                                         │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │Registrasi│ │ Pencarian│ │Peminjaman│ │Pengembalian│ │  Laporan │ │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘ │
│       │            │            │            │            │          │
│  ─────┼────────────┼────────────┼────────────┼────────────┼───── R1  │
│  Must │ Register   │ Cari judul │ Pinjam     │ Kembalikan │ Lihat    │
│       │ Login      │ Lihat stok │ Konfirmasi │ Bayar denda│ riwayat  │
│  ─────┼────────────┼────────────┼────────────┼────────────┼───── R2  │
│  Should│Reset pass │ Filter     │ Daftar     │ Perpanjang │ Statistik│
│       │           │ kategori   │ tunggu     │            │          │
│  ─────┼────────────┼────────────┼────────────┼────────────┼───── R3  │
│  Could│ OAuth     │ Rekomendasi│ Bookmark   │ Rating     │ Export   │
│       │ Google    │ AI         │ buku       │ buku       │ PDF      │
└──────────────────────────────────────────────────────────────────────┘
```

### 4.8 Perbandingan Use Case vs User Story

| Aspek | Use Case | User Story |
|-------|----------|------------|
| **Asal** | UML (Jacobson, 1992) | Agile/XP (Beck, 1999) |
| **Detail** | Sangat detail (narrative lengkap) | Ringkas (1-2 kalimat) |
| **Format** | UC Diagram + Narrative | As a/I want/So that |
| **Kapan dipakai** | Proyek besar, formal, regulated | Proyek Agile, iteratif |
| **Verifikasi** | Precondition/Postcondition | Acceptance Criteria (GWT) |
| **Maintenance** | Sulit — dokumen panjang | Mudah — kartu kecil |
| **Cocok untuk** | Sistem perbankan, pemerintah | Startup, aplikasi web/mobile |
| **Contoh Indonesia** | Sistem BPJS Kesehatan | Aplikasi Gojek, Tokopedia |

---

## Kegiatan Pembelajaran

### Pre-class (20 menit)

- Review hasil T1 (SRS) dan feedback dari dosen
- Baca materi tentang User Stories dan INVEST criteria di buku Cohn (2004) Chapter 2
- Siapkan konteks proyek kelompok: domain apa yang dipilih?

### In-class (110 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-25 menit | Use Case Diagram: komponen, notasi, relasi (include/extend/generalization) | Ceramah + contoh Puskesmas |
| 25-40 menit | Use Case Narrative: template dan contoh lengkap | Ceramah + demo |
| 40-55 menit | User Stories: format, INVEST criteria, contoh Indonesia | Ceramah + diskusi |
| 55-70 menit | Acceptance Criteria: format Given-When-Then, 5 contoh | Ceramah + demo |
| 70-90 menit | **Workshop**: Tulis 15 user stories + AC untuk proyek kelompok | Workshop kelompok |
| 90-105 menit | Product Backlog: MoSCoW prioritization + Story Points | Praktik kelompok |
| 105-110 menit | Wrap-up: preview Kuis K1 dan recap | Diskusi |

### Post-class (20 menit)

- Selesaikan T2: User Story Mapping & Acceptance Criteria
- Persiapan Kuis K1 (cakupan Minggu 1-4)
- Review: pastikan setiap user story memenuhi INVEST dan memiliki minimal 1 AC

---

## Latihan & Diskusi

### Soal 1 (C2 — Memahami)

Jelaskan perbedaan antara relasi `<<include>>` dan `<<extend>>` dalam Use Case Diagram. Berikan masing-masing satu contoh dalam konteks Sistem Informasi Akademik UAI.

### Soal 2 (C3 — Menerapkan)

Evaluasi user story berikut menggunakan kriteria INVEST. Identifikasi kriteria mana yang TIDAK terpenuhi dan perbaiki story-nya:

> "As a user, I want the system to use PostgreSQL database with proper indexing on all tables, so that queries are fast."

### Soal 3 (C3 — Menerapkan)

Buatlah 3 Acceptance Criteria dalam format Given-When-Then untuk User Story berikut:

> "As a mahasiswa UAI, I want melihat jadwal kuliah semester ini, so that saya bisa merencanakan kegiatan mingguan saya."

### Soal 4 (C4 — Menganalisis)

Sebuah startup ride-hailing di Surabaya membangun aplikasi "OjekKu". Tim terdiri dari 4 developer dan menggunakan Scrum.

a) Tulis 5 user stories yang memenuhi INVEST untuk fitur utama
b) Prioritaskan menggunakan MoSCoW
c) Estimasi Story Points (skala Fibonacci)
d) Tentukan stories mana yang masuk Sprint 1 (velocity: 15 points)

### Soal 5 (C3 — Menerapkan)

Buatlah Use Case Narrative lengkap (dengan Precondition, Main Flow, Alternative Flow, dan Postcondition) untuk Use Case "Pesan Ojek" pada aplikasi OjekKu di soal 4.

---

## Penugasan

### T2: User Story Mapping & Acceptance Criteria (2.5% nilai akhir)

| Komponen | Detail |
|----------|--------|
| **Deliverable** | 15 user stories (memenuhi INVEST) + acceptance criteria (format GWT) + product backlog yang diprioritaskan (MoSCoW + Story Points) + User Story Map |
| **Format** | Markdown di GitHub repository proyek kelompok |
| **Konteks** | Menggunakan domain proyek akhir kelompok (konteks Indonesia) |
| **Rubrik** | Kualitas INVEST (30%), AC GWT (30%), Prioritisasi (20%), Story Map (20%) |
| **AI Policy** | AI diizinkan sebagai brainstorming partner + wajib AI Usage Log |
| **Deadline** | Sebelum perkuliahan Minggu 5 |

### K1: Kuis Fondasi RPL & Requirements (4% nilai akhir)

| Komponen | Detail |
|----------|--------|
| **Cakupan** | Minggu 1-4 (SWEBOK, SDLC, Proses, Requirements, Use Case, User Story) |
| **Durasi** | 30 menit |
| **Format** | 15 Pilihan Ganda + 2 Uraian Singkat |
| **Sifat** | Closed-book, tanpa AI/internet |

---

## Referensi

1. Cohn, M. (2004). *User Stories Applied: For Agile Software Development*. Addison-Wesley.
2. Cockburn, A. (2001). *Writing Effective Use Cases*. Addison-Wesley.
3. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 4: Requirements Engineering. Pearson.
4. Patton, J. (2014). *User Story Mapping*. O'Reilly Media.
5. Wiegers, K. E., & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
