# Minggu 1: Pengantar Rekayasa Perangkat Lunak dan SDLC

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 1 dari 16 |
| **Topik** | Pengantar RPL, SWEBOK v4, Software Crisis, Etika Profesi |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK-1 |
| **Sub-CPMK** | 1.1 (Definisi & prinsip dasar RPL), 1.2 (SWEBOK v4 & etika profesi) |
| **Durasi** | 150 menit (3 x 50 menit) |
| **Metode** | Ceramah interaktif, diskusi kelompok, video |

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menjelaskan** definisi rekayasa perangkat lunak dan perbedaannya dengan programming (C2)
2. **Mengidentifikasi** faktor-faktor yang menyebabkan software crisis dan kebutuhan akan pendekatan SE yang sistematis (C2)
3. **Mendeskripsikan** 15 Knowledge Areas dalam SWEBOK v4 (2024) dan relevansinya dengan mata kuliah ini (C2)
4. **Menjelaskan** Software Development Life Cycle (SDLC) dan fase-fase utamanya (C2)
5. **Menjelaskan** prinsip etika profesi software engineer berdasarkan ACM/IEEE Code of Ethics dan nilai-nilai Islami (C2)

## Materi Pembelajaran

### 1.1 Apa Itu Rekayasa Perangkat Lunak?

#### 1.1.1 Definisi Formal

> **Rekayasa Perangkat Lunak** (*Software Engineering*) adalah penerapan pendekatan yang **sistematis, disiplin, dan terukur** terhadap pengembangan, pengoperasian, dan pemeliharaan perangkat lunak (IEEE, 2024).

Definisi ini mengandung tiga kata kunci penting:

```
┌─────────────────────────────────────────────────────────────┐
│              TIGA PILAR SOFTWARE ENGINEERING                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  SISTEMATIS  │  │   DISIPLIN   │  │   TERUKUR    │     │
│  │              │  │              │  │              │     │
│  │ Mengikuti    │  │ Mengikuti    │  │ Bisa diukur: │     │
│  │ proses yang  │  │ standar dan  │  │ waktu, biaya,│     │
│  │ terstruktur  │  │ best practice│  │ kualitas     │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                             │
│  Contoh: Pembangunan jembatan membutuhkan arsitek,          │
│  insinyur sipil, dan proses konstruksi yang terstandar.     │
│  Begitu juga pembangunan software yang berkualitas.         │
└─────────────────────────────────────────────────────────────┘
```

#### 1.1.2 Software Engineering vs Programming

Banyak mahasiswa mengira bahwa *software engineering* = menulis kode. Padahal, menulis kode (*programming/construction*) hanyalah **satu dari banyak fase** dalam rekayasa perangkat lunak.

```
┌─────────────────────────────────────────────────────────────────┐
│ SOFTWARE ENGINEERING (Lingkup penuh)                             │
│                                                                  │
│  ┌────────────────────────────────────────────────────┐         │
│  │ Requirements → Design → Construction → Testing →   │         │
│  │ Deployment → Maintenance → Evolution               │         │
│  │                                                    │         │
│  │  ┌────────────────────┐                           │         │
│  │  │    PROGRAMMING     │ ← hanya ~20% dari total!  │         │
│  │  │  (menulis kode)    │                           │         │
│  │  └────────────────────┘                           │         │
│  └────────────────────────────────────────────────────┘         │
│                                                                  │
│  + Project Management + Quality Assurance + Ethics               │
│  + Team Collaboration + Process Improvement                      │
└─────────────────────────────────────────────────────────────────┘
```

Perbandingan detail:

| Aspek | Programming | Software Engineering |
|-------|-------------|---------------------|
| **Fokus** | Menulis kode yang berjalan | Membangun sistem yang andal dan maintainable |
| **Skala** | Individu / kecil | Tim / besar (ribuan baris kode) |
| **Proses** | Ad-hoc, "yang penting jalan" | Terstruktur, mengikuti metodologi |
| **Dokumentasi** | Minimal | SRS, UML, API docs, test plan |
| **Testing** | Manual, jika sempat | Otomatis, terstruktur (unit, integration, E2E) |
| **Waktu hidup** | Sekali pakai | Bertahun-tahun, perlu maintenance |
| **Contoh** | Script hitung IPK | Sistem Akademik UAI (ratusan fitur, ribuan user) |

Analogi sederhana:

```
┌──────────────────────────────────────────────────────────┐
│  Membangun Rumah Kecil (Programming)                     │
│  ┌───────────────────────┐                               │
│  │ Satu tukang, sketsa   │                               │
│  │ di kertas, langsung   │                               │
│  │ bangun, selesai.      │                               │
│  └───────────────────────┘                               │
│                                                          │
│  Membangun Gedung 20 Lantai (Software Engineering)       │
│  ┌───────────────────────┐                               │
│  │ Arsitek + insinyur +  │                               │
│  │ tukang + QC + project │                               │
│  │ manager + izin +      │                               │
│  │ blueprint + testing   │                               │
│  │ material + maintenance│                               │
│  └───────────────────────┘                               │
└──────────────────────────────────────────────────────────┘
```

#### 1.1.3 Perangkat Lunak: Bukan Sekadar Kode

Perangkat lunak (*software*) bukan hanya kode program. IEEE mendefinisikan software sebagai:

```
Software = Program + Data + Dokumentasi + Konfigurasi
```

```python
# Contoh: Apa saja "software" dari Sistem Perpustakaan Kampus?

komponen_software = {
    "program": [
        "app.py (Flask backend)",
        "templates/ (HTML frontend)",
        "static/ (CSS, JavaScript)",
    ],
    "data": [
        "perpustakaan.db (database SQLite)",
        "data_buku.csv (data awal)",
    ],
    "dokumentasi": [
        "SRS.md (Software Requirements Specification)",
        "README.md (panduan instalasi)",
        "API_docs.md (dokumentasi API)",
    ],
    "konfigurasi": [
        ".env (environment variables)",
        "Dockerfile (container config)",
        ".github/workflows/ci.yml (CI/CD pipeline)",
    ],
}

# Hitung total komponen
total = sum(len(v) for v in komponen_software.values())
print(f"Total komponen software: {total}")
# Output: Total komponen software: 11
```

### 1.2 Sejarah dan Software Crisis

#### 1.2.1 Timeline Perkembangan Software Engineering

```
1940s-50s     1960s        1968         1970s        1980s-90s    2000s+
  │            │            │            │            │            │
  ▼            ▼            ▼            ▼            ▼            ▼
Kode mesin   Bahasa      NATO         Waterfall   OOP, UML,    Agile,
& assembly   tingkat     Conference   model,      Design       DevOps,
             tinggi      "Software    structured  Patterns     Cloud,
             (FORTRAN,   Engineering" programming              AI-assisted
             COBOL)      lahir!       lahir                    development
```

#### 1.2.2 Konferensi NATO 1968 — Lahirnya Software Engineering

Pada tahun 1968, di Garmisch, Jerman, diadakan **NATO Software Engineering Conference**. Para ahli berkumpul karena kesadaran akan masalah serius dalam pengembangan software:

- Proyek sering **terlambat** dari jadwal
- **Biaya** membengkak jauh melebihi anggaran
- Software yang dihasilkan **penuh bug**
- Produk **tidak sesuai** dengan kebutuhan pengguna

Fenomena ini disebut **Software Crisis** (*Krisis Perangkat Lunak*).

#### 1.2.3 Lima Kasus Kegagalan Software yang Mengubah Dunia

```
┌────────────────────────────────────────────────────────────────┐
│  5 KEGAGALAN SOFTWARE TERKENAL                                 │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  1. Ariane 5 (1996)                                           │
│     Roket meledak 37 detik setelah peluncuran.                │
│     Penyebab: Konversi tipe data 64-bit → 16-bit overflow.   │
│     Kerugian: $370 juta                                       │
│                                                                │
│  2. Therac-25 (1985-1987)                                     │
│     Mesin radioterapi memberikan dosis radiasi berlebihan.    │
│     Penyebab: Race condition di software kontrol.             │
│     Dampak: 6 pasien cedera/meninggal                         │
│                                                                │
│  3. Healthcare.gov (2013)                                      │
│     Website asuransi kesehatan AS crash saat peluncuran.      │
│     Penyebab: Kurangnya testing, integrasi 55 sistem.         │
│     Kerugian: $1.7 miliar untuk perbaikan                     │
│                                                                │
│  4. Boeing 737 MAX MCAS (2018-2019)                           │
│     Dua kecelakaan pesawat fatal.                             │
│     Penyebab: Software MCAS bergantung pada satu sensor.      │
│     Dampak: 346 korban jiwa                                   │
│                                                                │
│  5. Knight Capital (2012)                                      │
│     Bug pada trading software menyebabkan transaksi liar.     │
│     Penyebab: Deployment kode lama yang tidak dihapus.        │
│     Kerugian: $440 juta dalam 45 menit                        │
└────────────────────────────────────────────────────────────────┘
```

#### 1.2.4 Konteks Indonesia: Tantangan Software Lokal

```python
# Contoh kegagalan/tantangan proyek software di Indonesia

kasus_indonesia = [
    {
        "proyek": "e-KTP (2011-sekarang)",
        "masalah": "Proyek tertunda bertahun-tahun, anggaran membengkak",
        "pelajaran": "Requirements yang tidak jelas + korupsi = kegagalan",
    },
    {
        "proyek": "PeduliLindungi (2020-2022)",
        "masalah": "Performa lambat saat peak usage, isu privasi data",
        "pelajaran": "Scalability & security harus dipikirkan sejak awal",
    },
    {
        "proyek": "Sistem PPDB Online (berbagai daerah)",
        "masalah": "Server down saat pendaftaran, antrian tak terkendali",
        "pelajaran": "Load testing sangat penting sebelum go-live",
    },
    {
        "proyek": "SIPKD (Sistem Informasi Pengelolaan Keuangan Daerah)",
        "masalah": "Sulit di-maintain, versi berbeda di tiap daerah",
        "pelajaran": "Software maintenance & version control itu krusial",
    },
]

for kasus in kasus_indonesia:
    print(f"Proyek : {kasus['proyek']}")
    print(f"Masalah: {kasus['masalah']}")
    print(f"Lesson : {kasus['pelajaran']}")
    print("-" * 50)
```

#### 1.2.5 Statistik Proyek Software — CHAOS Report

```
┌──────────────────────────────────────────────────────┐
│  Standish Group CHAOS Report (2020)                  │
│                                                      │
│  ████████████████████████████████  31% Berhasil      │
│  ██████████████████████████████████████████  52% Challenged │
│  ██████████████  17% Gagal                           │
│                                                      │
│  "Challenged" = terlambat, over-budget, atau         │
│                 fitur tidak lengkap                   │
│                                                      │
│  Faktor sukses utama:                                │
│  1. User involvement (15.9%)                         │
│  2. Executive support (13.9%)                        │
│  3. Clear requirements (13.0%)                       │
│  4. Proper planning (9.6%)                           │
│  5. Realistic expectations (8.2%)                    │
└──────────────────────────────────────────────────────┘
```

### 1.3 SWEBOK v4 (2024) — 15 Knowledge Areas

SWEBOK (*Software Engineering Body of Knowledge*) v4 adalah **panduan resmi IEEE** yang mendefinisikan cakupan ilmu rekayasa perangkat lunak.

```
┌──────────────────────────────────────────────────────────────┐
│                     SWEBOK v4 (2024)                         │
│                  15 Knowledge Areas                          │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─── INTI SE (langsung terkait MK ini) ───────────────┐   │
│  │ 1. Software Requirements      [Minggu 3-4]          │   │
│  │ 2. Software Design            [Minggu 5-6]          │   │
│  │ 3. Software Construction      [Minggu 7]            │   │
│  │ 4. Software Testing           [Minggu 9-10]         │   │
│  │ 5. Software Maintenance       [Minggu 12]           │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─── PENDUKUNG SE ───────────────────────────────────┐    │
│  │ 6. Software Config. Management  [Minggu 7, 11]      │    │
│  │ 7. SE Management                [Minggu 12]         │    │
│  │ 8. SE Process                   [Minggu 2]          │    │
│  │ 9. SE Models & Methods          [Minggu 5-6]        │    │
│  │ 10. Software Quality            [Minggu 9-10]       │    │
│  │ 11. SE Professional Practice    [Minggu 1, 13-14]   │    │
│  │ 12. SE Economics                [Minggu 12]         │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌─── FONDASI ────────────────────────────────────────┐    │
│  │ 13. Computing Foundations       [Prasyarat: AlPro]  │    │
│  │ 14. Mathematical Foundations    [Prasyarat: Matdis] │    │
│  │ 15. Engineering Foundations     [Umum]              │    │
│  └─────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘
```

Detail setiap Knowledge Area:

| No | Knowledge Area | Deskripsi Singkat | Relevansi |
|----|---------------|-------------------|-----------|
| 1 | Software Requirements | Elicitation, analysis, specification, validation | Minggu 3-4 |
| 2 | Software Design | Architecture, detailed design, patterns | Minggu 5-6 |
| 3 | Software Construction | Coding, debugging, code review | Minggu 7 |
| 4 | Software Testing | Levels, techniques, automation | Minggu 9-10 |
| 5 | Software Maintenance | Corrective, adaptive, perfective, preventive | Minggu 12 |
| 6 | Software Configuration Management | Version control, change management | Minggu 7, 11 |
| 7 | Software Engineering Management | Planning, measurement, risk | Minggu 12 |
| 8 | Software Engineering Process | Process models, improvement | Minggu 2 |
| 9 | Software Engineering Models & Methods | Modeling, formal methods | Minggu 5-6 |
| 10 | Software Quality | QA, metrics, standards | Minggu 9-10 |
| 11 | SE Professional Practice | Ethics, economics, teamwork | Minggu 1, 13-14 |
| 12 | Software Engineering Economics | Cost estimation, value analysis | Minggu 12 |
| 13 | Computing Foundations | Algorithms, data structures, OS | Prasyarat |
| 14 | Mathematical Foundations | Logic, discrete math, statistics | Prasyarat |
| 15 | Engineering Foundations | Empirical methods, design basics | Umum |

### 1.4 Software Development Life Cycle (SDLC)

SDLC adalah **kerangka proses** yang mendefinisikan tahapan pengembangan software dari awal hingga akhir.

```
┌─────────────────────────────────────────────────────────────┐
│              SOFTWARE DEVELOPMENT LIFE CYCLE                 │
│                                                              │
│  ┌───────────┐    ┌───────────┐    ┌───────────┐           │
│  │ Planning  │───▶│Requirements│───▶│  Design   │           │
│  │& Analysis │    │ Gathering │    │           │           │
│  └───────────┘    └───────────┘    └─────┬─────┘           │
│                                          │                  │
│                                          ▼                  │
│  ┌───────────┐    ┌───────────┐    ┌───────────┐           │
│  │Maintenance│◀───│ Deployment│◀───│Construction│           │
│  │& Support  │    │& Delivery │    │ & Testing │           │
│  └───────────┘    └───────────┘    └───────────┘           │
│                                                              │
│  Setiap fase menghasilkan deliverable yang menjadi input    │
│  untuk fase berikutnya.                                      │
└─────────────────────────────────────────────────────────────┘
```

```python
# Simulasi SDLC sederhana: fase dan deliverable

sdlc_phases = {
    "1. Planning": {
        "aktivitas": "Analisis kelayakan, estimasi biaya, timeline",
        "deliverable": "Project Charter, Feasibility Study",
        "contoh": "Menentukan apakah Sistem Perpustakaan UAI layak dibangun",
    },
    "2. Requirements": {
        "aktivitas": "Elicitation, analisis, dokumentasi kebutuhan",
        "deliverable": "SRS (Software Requirements Specification)",
        "contoh": "Mahasiswa bisa meminjam buku, pustakawan bisa mengelola stok",
    },
    "3. Design": {
        "aktivitas": "Arsitektur, desain database, UI/UX wireframe",
        "deliverable": "UML Diagrams, ERD, Wireframes",
        "contoh": "Arsitektur MVC dengan Flask + SQLite",
    },
    "4. Construction": {
        "aktivitas": "Coding, unit testing, code review",
        "deliverable": "Source Code, Test Results",
        "contoh": "Implementasi API endpoint /api/buku",
    },
    "5. Testing": {
        "aktivitas": "Integration test, system test, UAT",
        "deliverable": "Test Report, Bug List",
        "contoh": "Test skenario peminjaman buku end-to-end",
    },
    "6. Deployment": {
        "aktivitas": "Release, deployment, training pengguna",
        "deliverable": "Deployed Application, User Manual",
        "contoh": "Deploy ke Railway/Vercel, training pustakawan",
    },
    "7. Maintenance": {
        "aktivitas": "Bug fixing, update fitur, monitoring",
        "deliverable": "Patch, Release Notes",
        "contoh": "Menambah fitur notifikasi keterlambatan",
    },
}

for phase, detail in sdlc_phases.items():
    print(f"\n{phase}")
    for key, val in detail.items():
        print(f"  {key}: {val}")
```

### 1.5 Mengapa Belajar RPL di Era AI?

AI bisa generate code, lalu mengapa perlu belajar Software Engineering?

```
┌────────────────────────────────────────────────────────────┐
│           AI vs SOFTWARE ENGINEER — Siapa Ngapain?         │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  AI BISA:                    SE TETAP PERLU:               │
│  ┌──────────────┐           ┌────────────────────────┐    │
│  │ Generate code│           │ Memahami kebutuhan     │    │
│  │ dari prompt  │           │ stakeholder yang ambigu │    │
│  ├──────────────┤           ├────────────────────────┤    │
│  │ Suggest code │           │ Merancang arsitektur   │    │
│  │ completion   │           │ scalable & maintainable│    │
│  ├──────────────┤           ├────────────────────────┤    │
│  │ Find bugs    │           │ Memutuskan trade-off   │    │
│  │ dalam kode   │           │ (security vs performa) │    │
│  ├──────────────┤           ├────────────────────────┤    │
│  │ Generate     │           │ Memastikan software    │    │
│  │ unit tests   │           │ memenuhi kebutuhan     │    │
│  ├──────────────┤           ├────────────────────────┤    │
│  │ Explain &    │           │ Mengelola tim, proses, │    │
│  │ refactor code│           │ dan etika pengembangan │    │
│  └──────────────┘           └────────────────────────┘    │
│                                                            │
│  Kesimpulan: AI adalah ALAT, SE adalah PROFESI             │
│  AI tanpa SE = kode tanpa arah                             │
│  SE tanpa AI = bekerja kurang efisien                      │
└────────────────────────────────────────────────────────────┘
```

```python
# Analogi: AI sebagai asisten, SE sebagai arsitek

class SoftwareEngineer:
    """SE menentukan APA yang dibangun dan MENGAPA."""

    def __init__(self, nama):
        self.nama = nama
        self.keahlian = [
            "requirements_analysis",
            "architecture_design",
            "quality_assurance",
            "team_leadership",
            "ethical_judgment",
        ]

    def tentukan_arsitektur(self, proyek):
        """AI tidak bisa memutuskan arsitektur yang tepat."""
        if proyek["skala"] == "startup":
            return "Monolith (sederhana, cepat develop)"
        elif proyek["skala"] == "enterprise":
            return "Microservices (scalable, independent deploy)"

    def evaluasi_output_ai(self, kode_dari_ai):
        """SE harus memvalidasi setiap output AI."""
        checks = ["security", "performance", "maintainability", "correctness"]
        return {check: "perlu_review_manusia" for check in checks}


class AIAssistant:
    """AI membantu BAGAIMANA implementasinya."""

    def generate_code(self, prompt):
        return "# Kode yang di-generate AI — perlu review SE!"

    def suggest_test(self, kode):
        return "# Test case dari AI — perlu validasi SE!"


# Kolaborasi SE + AI
engineer = SoftwareEngineer("Budi")
ai = AIAssistant()

arsitektur = engineer.tentukan_arsitektur({"skala": "startup"})
kode = ai.generate_code("Buat endpoint login")
review = engineer.evaluasi_output_ai(kode)

print(f"Arsitektur: {arsitektur}")
print(f"Review AI output: {review}")
```

### 1.6 Warisan Muslim dalam Ilmu Komputer

```
┌────────────────────────────────────────────────────────────┐
│         KONTRIBUSI ILMUWAN MUSLIM UNTUK COMPUTING          │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  AL-KHWARIZMI (780-850 M)                                 │
│  "Bapak Algoritma"                                        │
│  Kata "algorithm" berasal dari nama beliau.                │
│  Kitab "Al-Jabr" menjadi dasar aljabar.                   │
│  Pendekatan sistematis dalam problem-solving =             │
│  fondasi computational thinking.                           │
│                                                            │
│  AL-JAZARI (1136-1206 M)                                  │
│  "Bapak Robotika"                                         │
│  Merancang automata dan mesin otomatis.                    │
│  Cikal bakal konsep automation yang menjadi inti DevOps.   │
│                                                            │
│  IBN AL-HAYTHAM (965-1040 M)                              │
│  "Bapak Scientific Method"                                │
│  Pendekatan empiris: hipotesis → eksperimen → validasi.   │
│  Metode ini menjadi dasar software testing.                │
│                                                            │
│  Nilai: Islam mendorong pencarian ilmu (iqra'),            │
│  pendekatan sistematis, dan tanggung jawab (amanah)        │
│  dalam setiap karya.                                       │
└────────────────────────────────────────────────────────────┘
```

### 1.7 Etika Profesi Software Engineer

#### 1.7.1 ACM/IEEE Code of Ethics — 8 Prinsip Utama

```
┌─────────────────────────────────────────────────────────┐
│          ACM/IEEE SOFTWARE ENGINEERING CODE OF ETHICS     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  1. PUBLIC       Bertindak sesuai kepentingan publik     │
│  2. CLIENT       Bertindak sesuai kepentingan klien      │
│  3. PRODUCT      Memastikan produk memenuhi standar      │
│  4. JUDGMENT     Menjaga integritas profesional          │
│  5. MANAGEMENT   Mengelola pengembangan secara etis      │
│  6. PROFESSION   Memajukan reputasi profesi              │
│  7. COLLEAGUES   Berlaku adil, mendukung rekan           │
│  8. SELF         Terus belajar dan berkembang            │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

#### 1.7.2 Perspektif Islam dalam Software Engineering

| Nilai Islam | Penerapan dalam SE | Contoh Konkret |
|-------------|-------------------|----------------|
| **Amanah** (Trustworthiness) | Kode harus jujur, tidak menyembunyikan bug | Tidak memanipulasi data pengguna untuk keuntungan |
| **Al-'Adl** (Keadilan) | Software harus accessible dan fair | Desain UI yang ramah disabilitas, pricing yang adil |
| **Ihsan** (Excellence) | Menulis kode yang excellent | Clean code, proper testing, dokumentasi lengkap |
| **Ilmu** (Pengetahuan) | Terus belajar teknologi baru | Mengikuti perkembangan AI, cloud, security |
| **Syura** (Musyawarah) | Kolaborasi tim yang baik | Code review, Sprint Retrospective, pair programming |

```python
# Contoh kasus etika: Privacy vs Fitur

class EtikaSoftwareEngineer:
    """Dilema etika yang sering dihadapi SE."""

    @staticmethod
    def kasus_1_privasi():
        """
        Kasus: Startup e-commerce diminta menambah tracking
        lokasi pengguna 24/7 untuk 'personalisasi'.

        Perspektif etika:
        - ACM Prinsip 1 (PUBLIC): Apakah ini melindungi publik?
        - Islam (Amanah): Apakah pengguna tahu dan setuju?
        """
        keputusan = {
            "tracking_24_7": False,  # Melanggar privasi
            "tracking_saat_checkout": True,  # Sesuai kebutuhan
            "consent_dialog": True,  # Wajib minta izin
            "data_encryption": True,  # Lindungi data
        }
        return keputusan

    @staticmethod
    def kasus_2_bias_algoritma():
        """
        Kasus: Algoritma penilaian kredit ternyata diskriminatif
        terhadap kelompok tertentu.

        Perspektif:
        - ACM Prinsip 1 (PUBLIC): Software harus adil
        - Islam (Al-'Adl): Keadilan untuk semua
        """
        langkah_perbaikan = [
            "1. Audit dataset untuk bias",
            "2. Uji fairness metrics",
            "3. Libatkan diverse stakeholders",
            "4. Transparansi algoritma",
        ]
        return langkah_perbaikan


etika = EtikaSoftwareEngineer()
print("Kasus 1 - Tracking:")
print(etika.kasus_1_privasi())
print("\nKasus 2 - Bias Algoritma:")
for langkah in etika.kasus_2_bias_algoritma():
    print(f"  {langkah}")
```

### 1.8 Studi Kasus Mini: Software di Sekitar Kita

```python
# Software yang kita gunakan setiap hari di Indonesia

software_indonesia = {
    "Gojek/GoTo": {
        "pengguna": "190+ juta download",
        "kompleksitas": "Ride-hailing, payment, food delivery, streaming",
        "SE_diperlukan": "Microservices, real-time tracking, payment security",
    },
    "Tokopedia": {
        "pengguna": "100+ juta pengguna",
        "kompleksitas": "Marketplace, logistik, payment gateway",
        "SE_diperlukan": "High availability, scalability, fraud detection",
    },
    "BPJS Kesehatan": {
        "pengguna": "200+ juta peserta",
        "kompleksitas": "Klaim, rujukan, antrean, integrasi RS",
        "SE_diperlukan": "Data integrity, interoperability, performance",
    },
    "Sistem Akademik UAI": {
        "pengguna": "Ribuan mahasiswa + dosen",
        "kompleksitas": "KRS, KHS, jadwal, absensi, pembayaran",
        "SE_diperlukan": "Reliability, usability, data consistency",
    },
}

print("=" * 60)
print("SOFTWARE INDONESIA YANG MEMBUTUHKAN SE PROFESIONAL")
print("=" * 60)

for nama, info in software_indonesia.items():
    print(f"\n{nama}")
    print(f"  Pengguna     : {info['pengguna']}")
    print(f"  Kompleksitas : {info['kompleksitas']}")
    print(f"  SE Diperlukan: {info['SE_diperlukan']}")
```

## Kegiatan Pembelajaran

### Pre-class (20 menit)
- Membaca overview SWEBOK v4 di [swebok.org](https://www.computer.org/education/bodies-of-knowledge/software-engineering)
- Menonton video "What is Software Engineering?" (10 menit)
- Tulis 3 software yang sering digunakan sehari-hari dan pikirkan: "Berapa banyak orang yang terlibat membuatnya?"

### In-class (110 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-25 menit | Pengantar RPL: definisi, SE vs Programming, sejarah, software crisis | Ceramah interaktif |
| 25-45 menit | SWEBOK v4: 15 Knowledge Areas, relevansi tiap KA | Ceramah + diagram |
| 45-65 menit | SDLC overview, fase-fase utama, deliverables | Ceramah + contoh |
| 65-85 menit | Diskusi kelompok: "Mengapa SE masih relevan di era AI?" + Presentasi | Diskusi kelompok |
| 85-100 menit | Etika profesi SE: ACM/IEEE + perspektif Islam | Ceramah + refleksi |
| 100-110 menit | Studi kasus mini: software Indonesia + Q&A | Studi kasus + tanya jawab |

### Post-class (20 menit)
- Refleksi tertulis: "Tuliskan 3 hal baru yang dipelajari tentang SE dan 1 hal yang ingin digali lebih dalam"
- Preview: Baca pengantar model proses pengembangan software (Waterfall, Agile, Scrum)
- Eksplorasi: Kunjungi website [Gojek Engineering Blog](https://www.gojek.io/blog/tag/engineering) dan baca 1 artikel

## Latihan dan Diskusi

### Soal 1 — Pemahaman Konsep (C2)
Jelaskan dengan kata-kata sendiri mengapa software engineering berbeda dari programming. Berikan analogi dari kehidupan sehari-hari (selain analogi konstruksi bangunan yang sudah dibahas di kelas).

### Soal 2 — Analisis Kasus (C4)
Sebuah UMKM di Yogyakarta ingin membuat aplikasi pemesanan batik online. Tim hanya terdiri dari 2 orang dan deadline 3 bulan. Apakah mereka membutuhkan pendekatan software engineering yang lengkap, atau cukup dengan programming saja? Argumentasikan jawaban Anda dengan merujuk pada konsep yang dipelajari hari ini.

### Soal 3 — Koneksi SWEBOK (C2)
Dari 15 Knowledge Areas SWEBOK v4, pilih 5 yang menurut Anda paling krusial untuk pengembangan Sistem Informasi Perpustakaan Kampus. Jelaskan alasan pemilihan masing-masing.

### Soal 4 — Etika dan Nilai Islam (C3)
Sebuah startup fintech diminta oleh investor untuk menambahkan fitur "dark pattern" yang membuat pengguna secara tidak sadar berlangganan layanan premium. Analisis situasi ini dari perspektif:
a) ACM/IEEE Code of Ethics (sebutkan prinsip yang relevan)
b) Nilai-nilai Islam (amanah, al-'adl, ihsan)

### Soal 5 — Diskusi Kelompok (C5)
"Di masa depan, AI akan menggantikan software engineer sepenuhnya." Apakah Anda setuju atau tidak setuju? Berikan minimal 3 argumen yang didukung oleh konsep dari perkuliahan hari ini.

## Referensi

1. IEEE Computer Society. (2024). *Guide to the Software Engineering Body of Knowledge (SWEBOK) v4*. IEEE.
2. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 1. Pearson.
3. Pressman, R. S., & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). Chapter 1. McGraw-Hill.
4. ACM/IEEE. (2015). *Software Engineering Code of Ethics and Professional Practice*.
5. Standish Group. (2020). *CHAOS Report 2020*.
6. Brooks, F. P. (1995). *The Mythical Man-Month* (Anniversary ed.). Addison-Wesley.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
