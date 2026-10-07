# Minggu 3: Requirements Engineering dan Analisis Kebutuhan

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 3 dari 16 |
| **Topik** | Requirements Engineering: Elicitation, Analysis, Specification, Validation |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK-2 |
| **Sub-CPMK** | 2.1 (Teknik elicitation), 2.2 (Menyusun SRS IEEE 830) |
| **Durasi** | 150 menit (3 x 50 menit) |
| **Metode** | Ceramah, role-play elicitation, praktik menulis SRS |

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menjelaskan** proses requirements engineering dan pentingnya RE bagi keberhasilan proyek (C2)
2. **Menerapkan** minimal 3 teknik elicitation (interview, observation, prototyping) untuk mengumpulkan kebutuhan (C3)
3. **Membedakan** functional requirements dan non-functional requirements dengan contoh konkret (C2)
4. **Menyusun** dokumen SRS sesuai standar IEEE 830/ISO 29148 (C3)
5. **Menerapkan** teknik validasi requirements menggunakan checklist SMART (C3)

## Materi Pembelajaran

### 3.1 Pengantar Requirements Engineering

#### 3.1.1 Mengapa RE Sangat Penting?

> **Fakta:** 60% kegagalan proyek software disebabkan oleh requirements yang buruk (Standish Group CHAOS Report).

```
┌──────────────────────────────────────────────────────────────┐
│        BIAYA PERBAIKAN REQUIREMENT ERROR                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Fase ditemukan:          Biaya relatif:                     │
│                                                              │
│  Requirements   ██  $1                                       │
│  Design         ████  $5                                     │
│  Construction   ██████████  $10                               │
│  Testing        ████████████████  $20                         │
│  Deployment     ██████████████████████████████████████  $100  │
│                                                              │
│  Kesimpulan: Semakin lambat ditemukan, semakin MAHAL!        │
│  Fix 1 bug di production = fix 100 bug di requirements       │
└──────────────────────────────────────────────────────────────┘
```

#### 3.1.2 Proses Requirements Engineering

```
┌──────────────────────────────────────────────────────────────┐
│              PROSES REQUIREMENTS ENGINEERING                  │
│                                                              │
│  ┌───────────┐   ┌───────────┐   ┌──────────────┐          │
│  │Elicitation│──▶│ Analysis  │──▶│Specification │          │
│  │(Kumpulkan)│   │(Analisis) │   │(Dokumentasi) │          │
│  └───────────┘   └───────────┘   └──────┬───────┘          │
│       ▲                                  │                   │
│       │          ┌───────────┐           │                   │
│       │          │Management │           │                   │
│       └──────────│(Kelola    │◀──────────┘                   │
│                  │perubahan) │                                │
│                  └─────┬─────┘                                │
│                        │                                     │
│                  ┌─────▼─────┐                                │
│                  │Validation │                                │
│                  │(Validasi) │                                │
│                  └───────────┘                                │
│                                                              │
│  Proses ini ITERATIF, bukan sekali jalan!                    │
└──────────────────────────────────────────────────────────────┘
```

### 3.2 Stakeholder Analysis

Sebelum melakukan elicitation, kita harus mengidentifikasi **siapa saja stakeholder**-nya.

```python
# Identifikasi stakeholder untuk Sistem Perpustakaan Kampus

class StakeholderAnalysis:
    """Analisis stakeholder menggunakan Power-Interest Grid."""

    def __init__(self):
        self.stakeholders = []

    def tambah_stakeholder(self, nama, peran, power, interest):
        """
        power: 1-5 (pengaruh terhadap proyek)
        interest: 1-5 (kepentingan terhadap sistem)
        """
        self.stakeholders.append({
            "nama": nama,
            "peran": peran,
            "power": power,
            "interest": interest,
            "strategi": self._tentukan_strategi(power, interest),
        })

    def _tentukan_strategi(self, power, interest):
        if power >= 4 and interest >= 4:
            return "Manage Closely (komunikasi intensif)"
        elif power >= 4 and interest < 4:
            return "Keep Satisfied (update berkala)"
        elif power < 4 and interest >= 4:
            return "Keep Informed (libatkan di review)"
        else:
            return "Monitor (minimal effort)"

    def tampilkan(self):
        print(f"{'Stakeholder':<20} {'Peran':<25} {'P':>3} {'I':>3} {'Strategi'}")
        print("-" * 90)
        for s in self.stakeholders:
            print(f"{s['nama']:<20} {s['peran']:<25} {s['power']:>3} "
                  f"{s['interest']:>3} {s['strategi']}")


# Contoh: Sistem Perpustakaan Kampus UAI
sa = StakeholderAnalysis()
sa.tambah_stakeholder("Kepala Perpustakaan", "Product Owner", 5, 5)
sa.tambah_stakeholder("Pustakawan", "End User (staff)", 3, 5)
sa.tambah_stakeholder("Mahasiswa", "End User (peminjam)", 2, 5)
sa.tambah_stakeholder("Dekan FST", "Sponsor", 5, 3)
sa.tambah_stakeholder("IT UAI", "Technical support", 4, 4)
sa.tambah_stakeholder("Dosen", "Indirect user", 3, 2)

sa.tampilkan()
```

```
┌──────────────────────────────────────────────────────────┐
│            POWER-INTEREST GRID                            │
│                                                          │
│  High   │ Keep Satisfied    │ Manage Closely             │
│  Power  │ (Dekan FST)       │ (Kepala Perpustakaan,     │
│         │                    │  IT UAI)                   │
│         ├────────────────────┼────────────────────────────│
│  Low    │ Monitor           │ Keep Informed              │
│  Power  │ (Dosen)           │ (Pustakawan, Mahasiswa)    │
│         │                    │                            │
│         └────────────────────┴────────────────────────────│
│              Low Interest         High Interest           │
└──────────────────────────────────────────────────────────┘
```

### 3.3 Teknik Elicitation (6 Teknik)

#### 3.3.1 Ringkasan 6 Teknik

| No | Teknik | Deskripsi | Kapan Digunakan | Kelebihan | Kekurangan |
|----|--------|-----------|-----------------|-----------|------------|
| 1 | **Interview** | Tanya jawab langsung | Awal proyek, requirements inti | Mendalam, bisa klarifikasi | Memakan waktu, bias interviewer |
| 2 | **Questionnaire** | Survey tertulis | Banyak stakeholder | Efisien untuk banyak orang | Tidak bisa follow-up langsung |
| 3 | **Observation** | Mengamati pengguna | Proses bisnis kompleks | Melihat kebutuhan nyata | Observer effect, memakan waktu |
| 4 | **Prototyping** | Membuat mock-up | UI/UX, requirements ambigu | Feedback konkret dan cepat | Bisa misleading soal effort |
| 5 | **Brainstorming** | Diskusi terbuka | Inovasi, fase awal | Banyak ide, kreatif | Bisa didominasi, tidak fokus |
| 6 | **Document Analysis** | Analisis dokumen existing | Penggantian sistem | Memahami proses existing | Dokumen bisa outdated |

#### 3.3.2 Teknik Interview — Detail

```
┌──────────────────────────────────────────────────────────────┐
│               TEKNIK INTERVIEW REQUIREMENTS                  │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  PERSIAPAN:                                                  │
│  1. Identifikasi stakeholder target                          │
│  2. Siapkan daftar pertanyaan (open-ended + closed)          │
│  3. Jadwalkan waktu (30-60 menit ideal)                      │
│  4. Siapkan alat rekam (dengan izin)                         │
│                                                              │
│  JENIS PERTANYAAN:                                           │
│                                                              │
│  Open-ended (eksplorasi):                                    │
│  "Ceritakan proses peminjaman buku saat ini."                │
│  "Apa kesulitan terbesar yang Anda alami?"                   │
│  "Jika bisa mengubah satu hal, apa itu?"                     │
│                                                              │
│  Closed (konfirmasi):                                        │
│  "Berapa rata-rata peminjaman per hari?"                     │
│  "Apakah diperlukan fitur notifikasi?"                       │
│  "Apakah sistem harus mendukung mobile?"                     │
│                                                              │
│  TIPS:                                                       │
│  - Mulai dari umum ke spesifik                               │
│  - Dengarkan lebih banyak, bicara lebih sedikit              │
│  - Catat SEMUA kebutuhan, filter nanti                       │
│  - Konfirmasi pemahaman: "Jadi maksud Bapak/Ibu..."         │
└──────────────────────────────────────────────────────────────┘
```

```python
# Template interview guide

class InterviewGuide:
    """Template panduan interview untuk requirements elicitation."""

    def __init__(self, proyek, stakeholder):
        self.proyek = proyek
        self.stakeholder = stakeholder
        self.pertanyaan = []
        self.catatan = []

    def tambah_pertanyaan(self, kategori, pertanyaan):
        self.pertanyaan.append({"kategori": kategori, "pertanyaan": pertanyaan})

    def generate_default_questions(self):
        """Generate pertanyaan standar untuk interview."""
        default = [
            ("Konteks", "Ceritakan proses kerja Anda sehari-hari terkait sistem ini."),
            ("Masalah", "Apa masalah terbesar yang Anda hadapi dengan proses saat ini?"),
            ("Harapan", "Fitur apa yang paling Anda butuhkan dari sistem baru?"),
            ("Pengguna", "Siapa saja yang akan menggunakan sistem ini?"),
            ("Data", "Data apa saja yang perlu dikelola oleh sistem?"),
            ("Performa", "Berapa pengguna yang akan mengakses sistem bersamaan?"),
            ("Keamanan", "Apakah ada data sensitif yang perlu dilindungi?"),
            ("Integrasi", "Apakah sistem perlu terhubung dengan sistem lain?"),
            ("Prioritas", "Dari semua kebutuhan tadi, mana 3 yang paling penting?"),
            ("Timeline", "Kapan sistem ini diharapkan sudah bisa digunakan?"),
        ]
        for kategori, pertanyaan in default:
            self.tambah_pertanyaan(kategori, pertanyaan)

    def cetak(self):
        print(f"INTERVIEW GUIDE")
        print(f"Proyek     : {self.proyek}")
        print(f"Stakeholder: {self.stakeholder}")
        print(f"{'='*60}")
        for i, q in enumerate(self.pertanyaan, 1):
            print(f"  {i}. [{q['kategori']}] {q['pertanyaan']}")


# Contoh penggunaan
guide = InterviewGuide("Sistem Perpustakaan UAI", "Kepala Perpustakaan")
guide.generate_default_questions()
guide.cetak()
```

#### 3.3.3 Teknik Prototyping

```
┌──────────────────────────────────────────────────────────────┐
│           JENIS PROTOTYPE UNTUK REQUIREMENTS                 │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  LOW-FIDELITY                                                │
│  ┌─────────────────────────┐                                 │
│  │ Paper Prototype          │  Sketsa di kertas / whiteboard │
│  │ Wireframe               │  Figma / Balsamiq wireframe    │
│  │ ┌───────────────────┐   │                                 │
│  │ │ [Logo]  [Search]  │   │  Cepat dibuat (< 1 jam)       │
│  │ │ ┌─────┐ ┌─────┐   │   │  Fokus pada layout & flow     │
│  │ │ │Buku1│ │Buku2│   │   │  Murah untuk dibuang & redo   │
│  │ │ └─────┘ └─────┘   │   │                                 │
│  │ │ [Pinjam] [Detail] │   │                                 │
│  │ └───────────────────┘   │                                 │
│  └─────────────────────────┘                                 │
│                                                              │
│  HIGH-FIDELITY                                               │
│  ┌─────────────────────────┐                                 │
│  │ Interactive Prototype    │  Figma interactive / HTML mock │
│  │ Clickable Mockup        │  Bisa diklik, navigasi nyata   │
│  │                         │  Lebih mahal tapi feedback     │
│  │ Tampilan mirip produk   │  lebih akurat dari stakeholder │
│  │ akhir tapi tanpa        │                                 │
│  │ backend logic            │                                 │
│  └─────────────────────────┘                                 │
│                                                              │
│  THROWAWAY vs EVOLUTIONARY:                                  │
│  - Throwaway: Dibuang setelah requirements clear             │
│  - Evolutionary: Diiterasi menjadi produk akhir              │
└──────────────────────────────────────────────────────────────┘
```

### 3.4 Functional vs Non-Functional Requirements

#### 3.4.1 Functional Requirements (FR)

Mendefinisikan **APA** yang sistem harus lakukan — perilaku dan fungsi spesifik.

```python
# Contoh Functional Requirements untuk Sistem Perpustakaan

functional_requirements = [
    {
        "id": "FR-01",
        "deskripsi": "Sistem harus memungkinkan mahasiswa mendaftar dengan NIM dan email UAI",
        "prioritas": "Must",
        "aktor": "Mahasiswa",
    },
    {
        "id": "FR-02",
        "deskripsi": "Sistem harus memungkinkan pengguna login menggunakan NIM dan password",
        "prioritas": "Must",
        "aktor": "Semua pengguna",
    },
    {
        "id": "FR-03",
        "deskripsi": "Sistem harus menampilkan daftar buku yang tersedia dengan pencarian",
        "prioritas": "Must",
        "aktor": "Semua pengguna",
    },
    {
        "id": "FR-04",
        "deskripsi": "Sistem harus memungkinkan mahasiswa meminjam maksimal 3 buku",
        "prioritas": "Must",
        "aktor": "Mahasiswa",
    },
    {
        "id": "FR-05",
        "deskripsi": "Sistem harus mengirim notifikasi H-1 sebelum tenggat pengembalian",
        "prioritas": "Should",
        "aktor": "Sistem (otomatis)",
    },
    {
        "id": "FR-06",
        "deskripsi": "Pustakawan harus bisa menambah, edit, dan hapus data buku",
        "prioritas": "Must",
        "aktor": "Pustakawan",
    },
]

# Tampilkan sebagai tabel
print(f"{'ID':<8} {'Prioritas':<10} {'Aktor':<15} {'Deskripsi'}")
print("-" * 80)
for fr in functional_requirements:
    print(f"{fr['id']:<8} {fr['prioritas']:<10} {fr['aktor']:<15} {fr['deskripsi'][:45]}...")
```

#### 3.4.2 Non-Functional Requirements (NFR)

Mendefinisikan **BAGAIMANA** sistem harus bekerja — kualitas dan constraint.

```
┌──────────────────────────────────────────────────────────────┐
│        KATEGORI NON-FUNCTIONAL REQUIREMENTS                  │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  PERFORMANCE                                                 │
│  NFR-01: Halaman harus loading < 3 detik pada koneksi 4G    │
│  NFR-02: Pencarian harus mengembalikan hasil < 1 detik      │
│                                                              │
│  SCALABILITY                                                 │
│  NFR-03: Sistem harus mendukung 1000 pengguna bersamaan     │
│  NFR-04: Database harus menampung 100.000+ data buku        │
│                                                              │
│  SECURITY                                                    │
│  NFR-05: Password harus di-hash menggunakan bcrypt          │
│  NFR-06: API endpoint harus dilindungi dengan JWT token     │
│                                                              │
│  USABILITY                                                   │
│  NFR-07: Pengguna baru harus bisa melakukan peminjaman      │
│          dalam 3 langkah atau kurang                         │
│                                                              │
│  RELIABILITY                                                 │
│  NFR-08: Sistem harus memiliki uptime 99.5%                 │
│  NFR-09: Backup database otomatis setiap 24 jam             │
│                                                              │
│  COMPATIBILITY                                               │
│  NFR-10: Sistem harus berjalan di Chrome, Firefox, Safari   │
│                                                              │
│  Ingat: NFR yang BAIK harus TERUKUR (measurable)!           │
│  Buruk : "Sistem harus cepat"                               │
│  Baik  : "Response time < 3 detik untuk 95% request"        │
└──────────────────────────────────────────────────────────────┘
```

```python
# Validasi NFR: harus measurable (SMART)

class RequirementValidator:
    """Validasi apakah requirement memenuhi kriteria SMART."""

    @staticmethod
    def validate_smart(requirement):
        """
        S = Specific (spesifik, tidak ambigu)
        M = Measurable (terukur)
        A = Achievable (bisa dicapai)
        R = Relevant (relevan dengan kebutuhan)
        T = Testable (bisa diuji)
        """
        checks = {
            "specific": not any(word in requirement.lower()
                                for word in ["cepat", "baik", "mudah", "bagus"]),
            "measurable": any(char.isdigit() for char in requirement)
                         or any(word in requirement.lower()
                                for word in ["kurang dari", "maksimal", "minimal", "<", ">"]),
            "testable": True,  # assumed if measurable
        }
        score = sum(checks.values()) / len(checks) * 100
        return checks, score


validator = RequirementValidator()

# Test requirements
reqs = [
    "Sistem harus cepat",                              # BURUK
    "Halaman harus loading dalam < 3 detik",           # BAIK
    "Sistem harus mudah digunakan",                    # BURUK
    "Pengguna baru bisa meminjam dalam 3 langkah",     # BAIK
]

for req in reqs:
    checks, score = validator.validate_smart(req)
    status = "BAIK" if score >= 66 else "PERLU PERBAIKAN"
    print(f"[{status}] \"{req}\"")
    print(f"         Checks: {checks}\n")
```

### 3.5 Software Requirements Specification (SRS)

#### 3.5.1 Struktur SRS (IEEE 830/ISO 29148)

```
┌──────────────────────────────────────────────────────────────┐
│           STRUKTUR SRS — IEEE 830 / ISO 29148                │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  1. PENDAHULUAN                                              │
│     1.1 Tujuan Dokumen                                       │
│     1.2 Ruang Lingkup Produk                                 │
│     1.3 Definisi, Akronim, Singkatan                         │
│     1.4 Referensi                                            │
│     1.5 Gambaran Umum Dokumen                                │
│                                                              │
│  2. DESKRIPSI UMUM                                           │
│     2.1 Perspektif Produk                                    │
│     2.2 Fungsi Produk (ringkasan)                            │
│     2.3 Karakteristik Pengguna                               │
│     2.4 Batasan (Constraints)                                │
│     2.5 Asumsi dan Dependensi                                │
│                                                              │
│  3. KEBUTUHAN SPESIFIK                                       │
│     3.1 Functional Requirements                              │
│         3.1.1 FR-01: [Deskripsi]                             │
│         3.1.2 FR-02: [Deskripsi]                             │
│         ...                                                  │
│     3.2 Non-Functional Requirements                          │
│         3.2.1 Performance Requirements                       │
│         3.2.2 Security Requirements                          │
│         3.2.3 Usability Requirements                         │
│     3.3 External Interface Requirements                      │
│         3.3.1 User Interface                                 │
│         3.3.2 Hardware Interface                             │
│         3.3.3 Software Interface                             │
│                                                              │
│  4. LAMPIRAN (Use Case, Wireframe, dll.)                     │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

#### 3.5.2 Contoh SRS Mini: Sistem Perpustakaan Kampus UAI

```python
# Template SRS dalam format terstruktur (Python dict → Markdown)

srs_perpustakaan = {
    "judul": "Software Requirements Specification",
    "proyek": "Sistem Informasi Perpustakaan Kampus UAI",
    "versi": "1.0",
    "pendahuluan": {
        "tujuan": "Dokumen ini mendeskripsikan kebutuhan fungsional dan "
                  "non-fungsional untuk Sistem Informasi Perpustakaan Kampus UAI.",
        "ruang_lingkup": "Sistem berbasis web untuk mengelola peminjaman buku, "
                         "pencarian katalog, dan administrasi perpustakaan.",
        "pengguna_target": ["Mahasiswa", "Pustakawan", "Admin IT"],
    },
    "deskripsi_umum": {
        "perspektif": "Sistem standalone berbasis web (Flask + SQLite), "
                      "diakses via browser, di-deploy menggunakan Docker.",
        "fungsi_utama": [
            "Pencarian dan browsing katalog buku",
            "Peminjaman dan pengembalian buku",
            "Manajemen data buku (CRUD)",
            "Notifikasi keterlambatan",
            "Laporan statistik peminjaman",
        ],
        "batasan": [
            "Hanya untuk perpustakaan kampus UAI",
            "Bahasa antarmuka: Indonesia",
            "Koneksi internet diperlukan",
        ],
    },
    "functional_requirements": [
        {"id": "FR-01", "deskripsi": "Registrasi mahasiswa dengan NIM", "prioritas": "Must"},
        {"id": "FR-02", "deskripsi": "Login dengan NIM dan password", "prioritas": "Must"},
        {"id": "FR-03", "deskripsi": "Pencarian buku berdasarkan judul/penulis/ISBN", "prioritas": "Must"},
        {"id": "FR-04", "deskripsi": "Peminjaman buku (maks 3 per mahasiswa)", "prioritas": "Must"},
        {"id": "FR-05", "deskripsi": "Pengembalian buku dengan scan barcode", "prioritas": "Should"},
        {"id": "FR-06", "deskripsi": "Notifikasi email H-1 pengembalian", "prioritas": "Should"},
        {"id": "FR-07", "deskripsi": "Denda otomatis keterlambatan (Rp 1.000/hari)", "prioritas": "Could"},
        {"id": "FR-08", "deskripsi": "CRUD data buku oleh pustakawan", "prioritas": "Must"},
        {"id": "FR-09", "deskripsi": "Dashboard statistik peminjaman", "prioritas": "Should"},
        {"id": "FR-10", "deskripsi": "Export laporan ke PDF/Excel", "prioritas": "Could"},
    ],
    "nonfunctional_requirements": [
        {"id": "NFR-01", "kategori": "Performance", "deskripsi": "Response time < 3 detik"},
        {"id": "NFR-02", "kategori": "Scalability", "deskripsi": "Mendukung 500 user bersamaan"},
        {"id": "NFR-03", "kategori": "Security", "deskripsi": "Password hashed (bcrypt)"},
        {"id": "NFR-04", "kategori": "Usability", "deskripsi": "Peminjaman < 3 klik"},
        {"id": "NFR-05", "kategori": "Reliability", "deskripsi": "Uptime 99%"},
    ],
}

# Cetak ringkasan SRS
print(f"SRS: {srs_perpustakaan['proyek']} v{srs_perpustakaan['versi']}")
print(f"\nFunctional Requirements ({len(srs_perpustakaan['functional_requirements'])}):")
for fr in srs_perpustakaan['functional_requirements']:
    print(f"  {fr['id']} [{fr['prioritas']}] {fr['deskripsi']}")
print(f"\nNon-Functional Requirements ({len(srs_perpustakaan['nonfunctional_requirements'])}):")
for nfr in srs_perpustakaan['nonfunctional_requirements']:
    print(f"  {nfr['id']} [{nfr['kategori']}] {nfr['deskripsi']}")
```

### 3.6 Validasi Requirements

Validasi memastikan bahwa requirements yang didokumentasikan **benar, lengkap, dan konsisten**.

#### 3.6.1 Teknik Validasi

```
┌──────────────────────────────────────────────────────────────┐
│            TEKNIK VALIDASI REQUIREMENTS                      │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  1. REQUIREMENTS REVIEW                                      │
│     Tim dan stakeholder membaca SRS bersama-sama             │
│     dan memberikan feedback.                                 │
│                                                              │
│  2. PROTOTYPING                                              │
│     Buat prototype dan minta stakeholder mencoba.            │
│     "Apakah ini yang Anda maksud?"                           │
│                                                              │
│  3. TEST CASE GENERATION                                     │
│     Jika tidak bisa dibuat test case-nya,                    │
│     berarti requirement tidak testable!                       │
│                                                              │
│  4. CHECKLIST VALIDATION                                     │
│     Gunakan checklist standar untuk memeriksa setiap         │
│     requirement.                                              │
│                                                              │
│  5. TRACEABILITY MATRIX                                      │
│     Pastikan setiap requirement bisa dilacak ke              │
│     source (stakeholder) dan ke test case.                    │
└──────────────────────────────────────────────────────────────┘
```

#### 3.6.2 Checklist Validasi

```python
# Checklist validasi requirement

def validasi_requirement(req_id, deskripsi):
    """Validasi satu requirement menggunakan checklist."""

    checklist = {
        "Jelas (tidak ambigu)": True,
        "Testable (bisa diuji)": True,
        "Konsisten (tidak bertentangan)": True,
        "Complete (lengkap)": True,
        "Feasible (bisa diimplementasi)": True,
        "Traceable (bisa dilacak sumbernya)": True,
        "Prioritized (ada prioritas)": True,
    }

    # Heuristik sederhana: cek ambiguitas
    kata_ambigu = ["cepat", "baik", "mudah", "banyak", "sedikit", "secukupnya"]
    for kata in kata_ambigu:
        if kata in deskripsi.lower():
            checklist["Jelas (tidak ambigu)"] = False
            break

    # Cek testability
    if not any(char.isdigit() for char in deskripsi):
        if not any(word in deskripsi.lower() for word in ["harus", "wajib", "mampu"]):
            checklist["Testable (bisa diuji)"] = False

    passed = sum(checklist.values())
    total = len(checklist)

    print(f"\nValidasi {req_id}: \"{deskripsi[:50]}...\"")
    for item, status in checklist.items():
        mark = "PASS" if status else "FAIL"
        print(f"  [{mark}] {item}")
    print(f"  Skor: {passed}/{total} ({passed/total*100:.0f}%)")

    return passed == total


# Test
validasi_requirement("FR-01", "Sistem harus memungkinkan mahasiswa mendaftar dengan NIM")
validasi_requirement("NFR-01", "Sistem harus cepat dan mudah digunakan")  # akan gagal
```

### 3.7 Studi Kasus: BPJS Kesehatan — Complexity of Requirements

```
┌──────────────────────────────────────────────────────────────┐
│  STUDI KASUS: REQUIREMENTS BPJS KESEHATAN                    │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  STAKEHOLDERS (sangat banyak!):                              │
│  - 200+ juta peserta                                        │
│  - 23.000+ fasilitas kesehatan (faskes)                     │
│  - Kemenkes (regulator)                                      │
│  - Pemerintah daerah                                         │
│  - RS swasta dan pemerintah                                  │
│  - Apotek dan lab klinik                                     │
│                                                              │
│  TANTANGAN REQUIREMENTS:                                     │
│  1. Requirements berubah dengan regulasi pemerintah          │
│  2. Integrasi 55+ sistem yang berbeda                        │
│  3. Performance: jutaan transaksi per hari                   │
│  4. Security: data medis sangat sensitif                     │
│  5. Usability: pengguna dari beragam latar belakang          │
│                                                              │
│  PELAJARAN:                                                  │
│  - RE yang buruk = sistem yang tidak bisa memenuhi semua     │
│    kebutuhan stakeholder                                     │
│  - Teknik elicitation harus beragam (interview + observation │
│    + document analysis + prototype)                          │
│  - Validasi requirements WAJIB dilakukan sebelum coding      │
│  - Requirements management penting karena perubahan sering   │
└──────────────────────────────────────────────────────────────┘
```

```python
# Analisis kompleksitas requirements BPJS vs Perpustakaan

def analisis_kompleksitas(proyek, jumlah_stakeholder, jumlah_fr,
                          jumlah_integrasi, regulasi):
    """Hitung skor kompleksitas requirements."""
    skor = 0
    skor += min(jumlah_stakeholder / 10, 10)  # maks 10
    skor += min(jumlah_fr / 20, 10)           # maks 10
    skor += min(jumlah_integrasi * 2, 10)     # maks 10
    skor += 5 if regulasi else 0              # 0 atau 5

    level = "Rendah" if skor < 10 else "Sedang" if skor < 20 else "Tinggi"

    print(f"Proyek: {proyek}")
    print(f"  Stakeholders   : {jumlah_stakeholder}")
    print(f"  Functional Reqs: {jumlah_fr}")
    print(f"  Integrasi      : {jumlah_integrasi} sistem")
    print(f"  Regulasi ketat : {'Ya' if regulasi else 'Tidak'}")
    print(f"  Skor Kompleksitas: {skor:.1f}/35 ({level})")
    print()


analisis_kompleksitas("Perpustakaan UAI", 6, 15, 1, False)
analisis_kompleksitas("BPJS Kesehatan", 200, 500, 55, True)
analisis_kompleksitas("Startup E-commerce", 10, 50, 5, False)
```

### 3.8 Requirements Management — Mengelola Perubahan

```
┌──────────────────────────────────────────────────────────────┐
│          PROSES CHANGE MANAGEMENT REQUIREMENTS               │
│                                                              │
│  ┌───────────────┐                                           │
│  │ Change Request │                                          │
│  │ (dari PO/user) │                                          │
│  └───────┬───────┘                                           │
│          ▼                                                   │
│  ┌───────────────┐                                           │
│  │ Impact Analysis│  ← Apa dampak ke fitur lain?            │
│  │ (oleh tim dev) │    Berapa effort tambahan?               │
│  └───────┬───────┘                                           │
│          ▼                                                   │
│  ┌───────────────┐                                           │
│  │ Review &       │  ← PO, tim, stakeholder                 │
│  │ Approve/Reject │    evaluasi cost vs benefit              │
│  └───────┬───────┘                                           │
│       ╱     ╲                                                │
│  Approve   Reject                                            │
│      │        │                                              │
│      ▼        ▼                                              │
│  [Update   [Documented                                       │
│   SRS &     & archived]                                      │
│   Backlog]                                                   │
└──────────────────────────────────────────────────────────────┘
```

## Kegiatan Pembelajaran

### Pre-class (20 menit)
- Membaca template SRS di lampiran buku ajar atau contoh SRS di internet
- Pikirkan: "Apa saja kebutuhan sistem perpustakaan kampus yang saya gunakan?"
- Siapkan daftar 5 pertanyaan yang akan Anda ajukan jika mewawancarai pustakawan

### In-class (110 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-20 menit | Pengantar RE, stakeholder analysis, biaya kesalahan requirements | Ceramah interaktif |
| 20-45 menit | 6 teknik elicitation: detail & contoh | Ceramah + demo |
| 45-65 menit | **Role-play Elicitation**: mahasiswa interview "pustakawan" (dosen berperan) | Role-play kelompok |
| 65-85 menit | FR vs NFR, struktur SRS IEEE 830, contoh SRS mini | Ceramah + contoh |
| 85-105 menit | **Hands-on**: Mulai menulis SRS untuk Sistem Perpustakaan Kampus | Praktik individu |
| 105-110 menit | Validasi requirements, checklist, preview T1 | Diskusi |

### Post-class (20 menit)
- Lanjutkan menulis SRS untuk Tugas T1
- Review kembali 6 teknik elicitation — pilih 2 yang paling tepat untuk proyek Anda
- Baca tentang Use Case dan User Story untuk persiapan minggu depan

## Latihan dan Diskusi

### Soal 1 — Pemahaman Konsep (C2)
Jelaskan mengapa biaya memperbaiki requirement error meningkat secara eksponensial seiring fase pengembangan berlanjut. Berikan contoh konkret menggunakan Sistem Perpustakaan Kampus.

### Soal 2 — Elicitation (C3)
Anda ditugaskan untuk mengumpulkan requirements Sistem Informasi Kantin Kampus. Tentukan:
a) Siapa saja stakeholder-nya (minimal 5)?
b) Teknik elicitation apa yang paling tepat untuk masing-masing stakeholder?
c) Tuliskan 5 pertanyaan interview yang akan Anda ajukan ke pengelola kantin.

### Soal 3 — FR vs NFR (C3)
Tuliskan 5 Functional Requirements dan 5 Non-Functional Requirements untuk aplikasi TransJakarta (pembelian tiket, tracking bus, rute). Pastikan setiap NFR memenuhi kriteria SMART (terukur).

### Soal 4 — Validasi (C4)
Berikut beberapa requirements. Identifikasi mana yang BAIK dan mana yang PERLU DIPERBAIKI. Untuk yang perlu diperbaikan, tuliskan versi perbaikannya.
- "Sistem harus cepat"
- "Response time pencarian < 2 detik untuk 95% request"
- "Sistem harus user-friendly"
- "Pengguna baru mampu menyelesaikan peminjaman dalam 3 langkah tanpa bantuan"
- "Sistem harus mendukung banyak pengguna"

### Soal 5 — Studi Kasus (C4)
Sebuah UMKM batik di Solo ingin membangun toko online. Pemilik UMKM tidak familiar dengan teknologi. Jelaskan:
a) Bagaimana Anda akan melakukan stakeholder analysis?
b) Teknik elicitation apa yang paling cocok? (pilih 3, jelaskan alasan)
c) Tuliskan 3 FR dan 3 NFR untuk toko online batik tersebut.

## Penugasan

**T1: Menulis SRS untuk Sistem Informasi Perpustakaan Kampus** (2.5% nilai akhir)
- **Deadline:** Minggu 4 (sebelum kelas)
- **Format:** Markdown, submit via LMS
- **Minimum:** 10 functional requirements, 5 non-functional requirements, stakeholder analysis
- **Struktur:** Mengikuti template IEEE 830 yang dibahas di kelas
- **AI Policy:** AI diizinkan + wajib AI Usage Log (prompt, output, modifikasi, refleksi)

## Referensi

1. Wiegers, K. E., & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press.
2. IEEE Std 830-1998. *Recommended Practice for Software Requirements Specifications*.
3. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 4-5. Pearson.
4. ISO/IEC/IEEE 29148:2018. *Systems and Software Engineering — Life Cycle Processes — Requirements Engineering*.
5. Robertson, S., & Robertson, J. (2012). *Mastering the Requirements Process* (3rd ed.). Addison-Wesley.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
