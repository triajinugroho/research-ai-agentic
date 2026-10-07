# BAB 1: PENGANTAR REKAYASA PERANGKAT LUNAK

**Oleh: Tri Aji Nugroho, S.T., M.T.**
**Mata Kuliah:** IF2205 Rekayasa Perangkat Lunak
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Semester:** Genap 2025/2026

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom | Estimasi Waktu |
|-----------|-----------|-------------|----------------|
| 1.1 | Menjelaskan definisi, sejarah, dan prinsip-prinsip dasar rekayasa perangkat lunak serta perbedaan SE vs programming | C2 (Memahami) | 75 menit |
| 1.2 | Menjelaskan 15 Knowledge Areas SWEBOK v4 dan etika profesi software engineer | C2 (Memahami) | 75 menit |

**Setelah mempelajari bab ini, mahasiswa mampu:**

1. Mendefinisikan rekayasa perangkat lunak (*software engineering*) dan membedakannya dari pemrograman (*programming*)
2. Menelusuri sejarah SE dari Konferensi NATO 1968 hingga era AI-augmented development
3. Mengidentifikasi minimal 10 kasus kegagalan software (*software crisis*) dan pelajaran yang didapat
4. Menjelaskan 15 Knowledge Areas SWEBOK v4 (2024) beserta relevansinya
5. Menerapkan prinsip etika profesi berdasarkan ACM/IEEE Code of Ethics dan nilai-nilai Islam
6. Menghargai warisan peradaban Islam dalam fondasi ilmu komputer

---

## Peta Konsep Bab 1

```
                    ┌─────────────────────────────────┐
                    │  PENGANTAR REKAYASA PERANGKAT    │
                    │         LUNAK (SE)               │
                    └──────────────┬──────────────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
          ▼                        ▼                        ▼
   ┌──────────────┐    ┌───────────────────┐    ┌──────────────────┐
   │  Definisi &  │    │  Sejarah &        │    │  Etika Profesi   │
   │  Prinsip SE  │    │  Software Crisis  │    │  & Nilai Islam   │
   └──────┬───────┘    └────────┬──────────┘    └────────┬─────────┘
          │                     │                        │
   ┌──────┴───────┐    ┌───────┴──────────┐    ┌────────┴─────────┐
   │ SE vs        │    │ NATO 1968 →      │    │ ACM/IEEE Code    │
   │ Programming  │    │ Era AI (2024+)   │    │ of Ethics        │
   │              │    │                  │    │                  │
   │ SWEBOK v4    │    │ 10+ Kasus        │    │ Amanah, Adil,    │
   │ 15 KA        │    │ Kegagalan        │    │ Ihsan            │
   │              │    │                  │    │                  │
   │ Prinsip SE   │    │ Konteks          │    │ Al-Khwarizmi     │
   │ Fundamental  │    │ Indonesia        │    │ Heritage         │
   └──────────────┘    └──────────────────┘    └──────────────────┘
```

---

## 1.1 Apa Itu Rekayasa Perangkat Lunak?

### 1.1.1 Definisi Formal

> **Rekayasa Perangkat Lunak** (*Software Engineering*) adalah penerapan pendekatan yang **sistematis, disiplin, dan terukur** terhadap pengembangan, pengoperasian, dan pemeliharaan perangkat lunak, serta studi tentang pendekatan-pendekatan tersebut.
> — IEEE Standard Glossary of Software Engineering Terminology (IEEE Std 610.12)

Definisi ini menekankan tiga kata kunci:

| Kata Kunci | Makna | Contoh Penerapan |
|------------|-------|------------------|
| **Sistematis** (*Systematic*) | Mengikuti metode dan proses yang terstruktur | Menggunakan Scrum dengan sprint planning, review, retrospective |
| **Disiplin** (*Disciplined*) | Konsisten mengikuti standar dan best practices | Menerapkan coding standards (PEP 8), code review wajib sebelum merge |
| **Terukur** (*Quantifiable*) | Dapat diukur dan dievaluasi secara objektif | Mengukur code coverage > 80%, defect density < 5 per KLOC |

Beberapa definisi lain yang penting:

- **Sommerville (2016):** "Software engineering is an engineering discipline that is concerned with all aspects of software production from the early stages of system specification through to maintaining the system after it has gone into use."
- **Pressman (2020):** "Software engineering encompasses a process, a collection of methods, and an array of tools that allow professionals to build high-quality computer software."
- **Fritz Bauer (NATO 1968):** "The establishment and use of sound engineering principles in order to obtain economically software that is reliable and works efficiently on real machines."

### 1.1.2 Software Engineering vs Programming

Banyak mahasiswa mengira bahwa belajar SE sama dengan belajar programming lebih lanjut. Ini adalah miskonsepsi fundamental. Perhatikan analogi berikut:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ANALOGI: KONSTRUKSI BANGUNAN                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Tukang Batu (≈ Programmer)         Insinyur Sipil (≈ SE)          │
│  ┌─────────────────────┐           ┌──────────────────────────┐    │
│  │ - Memasang bata      │           │ - Survei lahan            │    │
│  │ - Mengaduk semen     │           │ - Analisis struktur       │    │
│  │ - Memasang keramik   │           │ - Desain arsitektur       │    │
│  │                      │           │ - Hitung kekuatan         │    │
│  │ Keterampilan:        │           │ - Kelola kontraktor       │    │
│  │ MEMBANGUN             │           │ - Pastikan standar K3     │    │
│  └─────────────────────┘           │ - Uji kelayakan bangunan  │    │
│                                     │                            │    │
│                                     │ Tanggung jawab:            │    │
│                                     │ SELURUH LIFECYCLE          │    │
│                                     └──────────────────────────┘    │
│                                                                     │
│  Tanpa insinyur sipil, bangunan mungkin berdiri...                  │
│  tapi apakah AMAN? Apakah TAHAN GEMPA? Apakah EFISIEN?             │
└─────────────────────────────────────────────────────────────────────┘
```

**Perbandingan detail:**

| Aspek | Programming | Software Engineering |
|-------|-------------|---------------------|
| **Fokus utama** | Menulis kode yang berfungsi | Seluruh lifecycle perangkat lunak |
| **Skala** | Individu, program kecil | Tim 5-500+ orang, sistem enterprise |
| **Proses** | Ad-hoc, "langsung coding" | Metodologi terstruktur (Agile, Waterfall) |
| **Kualitas** | "Yang penting jalan" | Reliable, maintainable, scalable, secure |
| **Dokumentasi** | Komentar kode (jika ada) | SRS, UML, ADR, API docs, user manual |
| **Requirements** | Sering diasumsikan | Dielisitasi, dianalisis, divalidasi |
| **Testing** | Manual, "coba-coba" | Strategi testing terstruktur (unit, integration, E2E) |
| **Maintenance** | Patch saat error | Planned maintenance, evolution, refactoring |
| **Tim** | Sendiri atau pair | Roles berbeda (PO, SM, Dev, QA, DevOps) |
| **Waktu hidup produk** | Tugas selesai = selesai | 5-20+ tahun dipakai dan dimaintain |

### 1.1.3 Mengapa Software Engineering Penting?

Software telah menjadi infrastruktur kritis kehidupan modern:

```
┌─────────────────────────────────────────────────────────┐
│          SOFTWARE ADA DI MANA-MANA                      │
│                                                         │
│  Transportasi        Kesehatan        Keuangan          │
│  ┌──────────┐       ┌──────────┐    ┌──────────┐       │
│  │ Gojek    │       │ Halodoc  │    │ BCA      │       │
│  │ Grab     │       │ BPJS     │    │ OVO      │       │
│  │ MRT App  │       │ Alodokter│    │ GoPay    │       │
│  └──────────┘       └──────────┘    └──────────┘       │
│                                                         │
│  Pendidikan          Pemerintahan    E-Commerce          │
│  ┌──────────┐       ┌──────────┐    ┌──────────┐       │
│  │ Ruangguru│       │ e-KTP    │    │ Tokopedia│       │
│  │ LMS UAI  │       │ SIPKD    │    │ Shopee   │       │
│  │ Google   │       │ OSS      │    │ Bukalapak│       │
│  │ Classroom│       │ SIAK     │    │          │       │
│  └──────────┘       └──────────┘    └──────────┘       │
└─────────────────────────────────────────────────────────┘
```

**Fakta-fakta penting:**

- **Standish Group CHAOS Report (2020):** Hanya **31% proyek software berhasil** sepenuhnya (*on time, on budget, on target*). 50% "challenged" (terlambat/over-budget), 19% **gagal total**.
- **60% kegagalan** disebabkan oleh requirements yang buruk atau berubah (Wiegers & Beatty, 2013)
- Biaya perbaikan bug meningkat secara eksponensial:

```
Biaya Perbaikan Bug (Relatif)
┌──────────────────────────────────────────────────┐
│                                          ■ $100x │
│                                    ■              │
│                              ■     $30x           │
│                        ■     $10x                 │
│                  ■     $5x                        │
│            ■     $3x                              │
│      ■     $1.5x                                  │
│ ■    $1x                                          │
│ Req  Design  Code  Unit  Integ  System  Release   │
│              Test  Test  Test   Test              │
└──────────────────────────────────────────────────┘
  Semakin lambat ditemukan → semakin MAHAL diperbaiki
```

### 1.1.4 Prinsip-Prinsip Dasar SE

David Hooker (1996) merumuskan **7 Prinsip SE** yang tetap relevan:

1. **The Reason It All Exists** — Software ada untuk memberikan nilai kepada pengguna. Jika tidak memberikan nilai, jangan bangun.
2. **KISS (Keep It Simple, Stupid!)** — Desain sesederhana mungkin, tapi tidak lebih sederhana dari yang dibutuhkan.
3. **Maintain the Vision** — Visi arsitektur yang jelas mencegah "design by committee" yang kacau.
4. **What You Produce, Others Will Consume** — Kode Anda akan dibaca dan dimaintain orang lain. Tulis untuk mereka, bukan hanya untuk diri sendiri.
5. **Be Open to the Future** — Sistem harus bisa diadaptasi. Jangan hard-code hal yang mungkin berubah.
6. **Plan Ahead for Reuse** — Desain komponen agar bisa digunakan ulang di proyek lain.
7. **Think!** — Berpikir jernih sebelum bertindak menghasilkan hasil yang lebih baik daripada langsung coding.

> **Tips Praktis:** Prinsip #4 sangat penting dalam kolaborasi tim. Ketika Anda menulis kode di proyek akhir kuliah ini, bayangkan teman satu tim Anda harus membaca dan melanjutkan kode tersebut besok pagi.

---

## 1.2 Sejarah Rekayasa Perangkat Lunak

### 1.2.1 Timeline: Dari NATO 1968 hingga Era AI

```
1950s        1960s        1968         1970s        1980s
  │            │            │            │            │
  ▼            ▼            ▼            ▼            ▼
Assembly   Software    NATO Conf.   Waterfall    OOP, C++
Language   Crisis      Garmisch     (Royce)      Spiral Model
           dimulai     "Software    Structured   (Boehm)
                       Engineering" Programming
                       coined       SE sebagai    CMM (SEI)
                                    disiplin

1990s        2001         2010s        2020s        2024+
  │            │            │            │            │
  ▼            ▼            ▼            ▼            ▼
Internet   Agile        DevOps       AI-Augmented  SWEBOK v4
Era        Manifesto    Cloud        GitHub        AI Agents
UML, Java  Scrum Guide  Microservs   Copilot       Agentic Dev
SWEBOK v1  XP, Kanban   Docker       ChatGPT       Claude Code
                        CI/CD        Claude        Cursor
```

### 1.2.2 Era Awal (1950s-1960s): Kelahiran Masalah

Pada era ini, software dikembangkan secara **ad hoc** — programmer menulis kode langsung tanpa desain atau dokumentasi. Proyeknya kecil dan dikerjakan individu. Namun seiring komputer semakin powerful, software menjadi semakin kompleks:

- **1960s:** Proyek OS/360 IBM — salah satu proyek software terbesar saat itu. Fred Brooks (yang terlibat langsung) kemudian menulis **"The Mythical Man-Month" (1975)** yang menjadi klasik SE. Hukum Brooks: *"Adding manpower to a late software project makes it later."*
- **Software Crisis** mulai terasa: proyek terlambat, over-budget, tidak memenuhi kebutuhan.

### 1.2.3 Era Formalisasi (1968-1980s): SE Lahir sebagai Disiplin

- **1968: Konferensi NATO di Garmisch, Jerman** — Pertama kalinya istilah "Software Engineering" digunakan secara resmi. Para ilmuwan menyadari bahwa pendekatan engineering diperlukan untuk membangun software.
- **1970: Winston Royce** mempublikasikan paper yang (ironisnya) sering disalahpahami sebagai "penemu Waterfall" — padahal Royce justru menunjukkan kelemahannya dan merekomendasikan iterasi.
- **1976: Barry Boehm** memperkenalkan Software Economics dan cost estimation (COCOMO).
- **1986: Boehm** mengusulkan Spiral Model yang menggabungkan iterasi dengan risk analysis.
- **1987: SEI (Software Engineering Institute)** di Carnegie Mellon memperkenalkan CMM (Capability Maturity Model) untuk mengukur kematangan proses.

### 1.2.4 Era Modern (1990s-2000s): Internet dan Agile

- **1990s:** Internet mengubah segalanya — software harus bisa di-deploy cepat, di-update sering, dan accessible via browser.
- **1995:** Ken Schwaber dan Jeff Sutherland memperkenalkan **Scrum**.
- **1996:** Kent Beck memperkenalkan **Extreme Programming (XP)**.
- **1997:** UML (Unified Modeling Language) distandarisasi oleh OMG.
- **2001:** 17 software developers bertemu di Snowbird, Utah dan melahirkan **Agile Manifesto** — revolusi dalam cara kita membangun software.
- **2004:** SWEBOK v2 diterbitkan oleh IEEE.

### 1.2.5 Era DevOps dan Cloud (2010s)

- **2009:** Patrick Debois menyelenggarakan **DevOpsDays** pertama — istilah "DevOps" lahir.
- **2013:** Docker membuat containerization accessible untuk semua developer.
- **2014:** Microservices menjadi architectural style dominan (dipopulerkan oleh Netflix, Amazon).
- **2015:** CI/CD menjadi standar industri — code commit otomatis di-build, test, dan deploy.

### 1.2.6 Era AI-Augmented (2020s-sekarang)

- **2021:** GitHub Copilot diluncurkan — AI bisa suggest code secara real-time.
- **2022:** ChatGPT (OpenAI) merevolusi cara developer berinteraksi dengan AI.
- **2023:** Claude (Anthropic), Cursor IDE, dan berbagai AI coding tools bermunculan.
- **2024:** SWEBOK v4 diterbitkan — menambahkan Knowledge Areas baru termasuk AI/ML foundations. Era **agentic development** dimulai — AI tidak hanya suggest code, tapi bisa menjalankan perintah, membuat file, dan mengelola proyek.
- **2025-2026:** Claude Code, GitHub Copilot Workspace, dan AI agent tools menjadi bagian dari workflow SE sehari-hari.

> **Refleksi:** Dalam kurang dari 60 tahun, SE berkembang dari "menulis kode tanpa aturan" menjadi disiplin ilmu yang melibatkan AI sebagai partner. Namun prinsip dasarnya tetap: **membangun software yang reliable, maintainable, dan memberikan nilai kepada pengguna.**

---

## 1.3 Software Crisis: Belajar dari Kegagalan

### 1.3.1 Apa Itu Software Crisis?

**Software crisis** adalah istilah yang diperkenalkan pada Konferensi NATO 1968 untuk menggambarkan fenomena sistemik di mana proyek software secara konsisten:

- Terlambat dari jadwal (*schedule overrun*)
- Melebihi anggaran (*cost overrun*)
- Penuh bug dan tidak reliable
- Tidak sesuai dengan kebutuhan pengguna
- Sulit dimaintain dan dievoluasi

Meskipun istilah "crisis" berasal dari tahun 1960-an, kegagalan software terus terjadi hingga hari ini. Berikut adalah 12 kasus penting yang wajib diketahui setiap software engineer:

### 1.3.2 Katalog Kegagalan Software: 12 Kasus Penting

#### Kasus 1: Therac-25 (1985-1987) — Ketika Software Membunuh

**Apa yang terjadi:** Therac-25 adalah mesin terapi radiasi yang dikendalikan software. Akibat **race condition** dan penghapusan hardware safety interlock, mesin memberikan dosis radiasi **100x lipat** dari yang seharusnya. Enam pasien menerima overdosis masif; tiga di antaranya meninggal dunia.

**Pelajaran SE:**
- Jangan menggantikan hardware safety dengan software safety saja
- Race condition adalah bug yang sangat berbahaya di sistem safety-critical
- Testing harus mencakup semua skenario, termasuk edge cases

#### Kasus 2: Morris Worm (1988) — Internet Worm Pertama

**Apa yang terjadi:** Robert Tappan Morris, mahasiswa Cornell, menulis worm yang mengeksploitasi buffer overflow di program `fingerd` Unix. Worm ini menginfeksi **~6.000 komputer** (sekitar 10% dari seluruh internet saat itu) dan menyebabkan kerugian jutaan dolar.

**Pelajaran SE:**
- Buffer overflow adalah vulnerability klasik yang masih relevan
- Input validation wajib dilakukan di setiap entry point
- Security harus menjadi bagian dari desain, bukan afterthought

#### Kasus 3: Ariane 5 Flight 501 (1996) — Roket Rp 5 Triliun Meledak

**Apa yang terjadi:** Roket Ariane 5 Eropa meledak 37 detik setelah peluncuran. Penyebabnya: **integer overflow** — konversi dari 64-bit floating point ke 16-bit signed integer pada Inertial Reference System (SRI). Kode tersebut di-reuse dari Ariane 4 tanpa testing ulang.

**Pelajaran SE:**
- Reuse kode tanpa re-validasi sangat berbahaya
- Type checking dan range checking sangat penting
- Software testing harus mencakup kondisi operasional baru

```python
# Simulasi sederhana integer overflow (konsep)
import struct

def simulasi_overflow():
    """
    Demonstrasi konsep integer overflow
    yang menyebabkan kegagalan Ariane 5
    """
    # Nilai asli (64-bit float)
    nilai_sensor = 32768.5  # Melebihi range 16-bit signed int

    # Range 16-bit signed integer: -32768 s.d. 32767
    MAX_INT16 = 32767
    MIN_INT16 = -32768

    if nilai_sensor > MAX_INT16 or nilai_sensor < MIN_INT16:
        print(f"PERINGATAN: Nilai {nilai_sensor} melebihi range int16!")
        print(f"Range int16: {MIN_INT16} s.d. {MAX_INT16}")
        print("Ini yang terjadi pada Ariane 5 — overflow menyebabkan crash")
    else:
        nilai_konversi = int(nilai_sensor)
        print(f"Konversi berhasil: {nilai_konversi}")

simulasi_overflow()
```

**Output yang diharapkan:**
```
PERINGATAN: Nilai 32768.5 melebihi range int16!
Range int16: -32768 s.d. 32767
Ini yang terjadi pada Ariane 5 — overflow menyebabkan crash
```

#### Kasus 4: Mars Climate Orbiter (1999) — Satuan Imperial vs Metrik

**Apa yang terjadi:** NASA kehilangan orbiter senilai $125 juta karena satu tim menggunakan **satuan imperial** (pound-force seconds) sementara tim lain menggunakan **satuan metrik** (newton-seconds). Tidak ada validasi konsistensi antar modul.

**Pelajaran SE:**
- Interface contract antar tim/modul harus didefinisikan dengan jelas
- Integration testing wajib mencakup kompatibilitas data antar komponen
- Dokumentasi teknis harus eksplisit, tidak boleh ambigu

#### Kasus 5: Knight Capital (2012) — $440 Juta Hilang dalam 45 Menit

**Apa yang terjadi:** Knight Capital Group, perusahaan trading terbesar di AS, kehilangan **$440 juta dalam 45 menit** akibat deployment kode lama yang tidak seharusnya aktif. Seorang teknisi lupa meng-update kode di satu dari delapan server. Kode lama mengirim jutaan order yang tidak diinginkan ke pasar saham.

**Pelajaran SE:**
- Deployment harus otomatis dan konsisten (CI/CD)
- Feature flags dan rollback mechanism wajib ada
- Kode mati (*dead code*) harus dihapus, bukan dibiarkan

#### Kasus 6: Healthcare.gov (2013) — Peluncuran Gagal di Depan 300 Juta Warga

**Apa yang terjadi:** Website asuransi kesehatan AS gagal total saat diluncurkan. Dari jutaan pengunjung di hari pertama, hanya **6 orang yang berhasil mendaftar**. Masalah: arsitektur tidak scalable, 55 kontraktor tanpa koordinasi yang jelas, testing hanya 2 minggu sebelum launch.

**Pelajaran SE:**
- Load testing dan performance testing wajib untuk sistem publik
- Arsitektur harus didesain untuk scale
- Koordinasi antar tim adalah tantangan SE, bukan hanya tantangan teknis

#### Kasus 7: Boeing 737 MAX MCAS (2018-2019) — 346 Nyawa

**Apa yang terjadi:** Sistem MCAS (Maneuvering Characteristics Augmentation System) pada Boeing 737 MAX bergantung pada **satu sensor sudut serang** (bukan redundant). Ketika sensor gagal, MCAS mendorong hidung pesawat turun berulang kali. Dua kecelakaan fatal: Lion Air JT610 (189 korban) dan Ethiopian Airlines ET302 (157 korban).

**Pelajaran SE:**
- Single point of failure di sistem safety-critical tidak boleh ada
- Redundancy dan fail-safe mechanism wajib
- Ethical responsibility: keselamatan manusia di atas profit dan timeline
- Transparent communication dengan pengguna (pilot) tentang sistem baru

#### Kasus 8: Volkswagen Dieselgate (2015) — Software sebagai Alat Penipuan

**Apa yang terjadi:** VW memprogram ECU (Engine Control Unit) agar mendeteksi kapan mobil sedang diuji emisi, lalu mengubah perilaku mesin untuk lulus tes. Dalam penggunaan normal, emisi NOx hingga **40x lipat** di atas batas. Skandal ini melibatkan 11 juta kendaraan dan denda miliaran dolar.

**Pelajaran SE:**
- Software engineering bukan hanya soal teknis — ada dimensi **etika**
- Engineer yang diminta menulis "cheat code" harus berani menolak
- Professional responsibility melampaui kepatuhan pada atasan

#### Kasus 9: Crowdstrike Update Incident (2024) — Blue Screen Global

**Apa yang terjadi:** Update rutin Crowdstrike Falcon Sensor menyebabkan **Blue Screen of Death (BSOD)** pada jutaan komputer Windows di seluruh dunia. Bandara, bank, rumah sakit, dan berbagai layanan kritis terdampak selama berjam-jam.

**Pelajaran SE:**
- Update pada sistem yang berjalan di kernel level memerlukan testing ekstra ketat
- Canary deployment dan staged rollout sangat penting
- Disaster recovery plan harus selalu siap

#### Kasus 10: Log4Shell / Log4j (2021) — Vulnerability di Mana-Mana

**Apa yang terjadi:** Vulnerability kritis (CVE-2021-44228) ditemukan di library logging Java yang sangat populer, Log4j. Karena hampir semua aplikasi Java menggunakan library ini, **ratusan juta sistem** di seluruh dunia menjadi vulnerable.

**Pelajaran SE:**
- Dependency management dan Software Bill of Materials (SBOM) sangat penting
- Open source tidak berarti "pasti aman" — perlu audit
- Supply chain security menjadi concern utama SE modern

### 1.3.3 Kegagalan dan Keberhasilan Software di Indonesia

#### Kasus Tantangan di Indonesia

| Kasus | Tahun | Masalah | Status |
|-------|-------|---------|--------|
| **Proyek e-KTP** | 2011-2017 | Anggaran Rp 5.9 triliun, terlibat korupsi, data belum terintegrasi sempurna | Berjalan dengan perbaikan terus-menerus |
| **Sistem BPJS Kesehatan** | 2014-sekarang | Overload pada awal peluncuran, integrasi data rumah sakit sulit, antrean panjang | Terus diperbaiki, belum optimal |
| **SIPKD (Sistem Informasi Pengelolaan Keuangan Daerah)** | 2008-sekarang | Implementasi berbeda di setiap daerah, kurang standarisasi, sulit dimaintain | Bervariasi per daerah |

#### Keberhasilan di Indonesia

| Kasus | Pelajaran SE |
|-------|-------------|
| **Gojek/GoTo** | Dari startup kecil menjadi super-app. Kunci: arsitektur microservices yang scalable, Agile development, engineering culture yang kuat |
| **Tokopedia** | E-commerce platform yang mampu menangani jutaan transaksi. Kunci: CI/CD pipeline matang, A/B testing, data-driven engineering |
| **Traveloka** | Platform travel yang reliable. Kunci: API design yang baik, payment integration yang secure, performance optimization |
| **PeduliLindungi (2020-2022)** | Dibangun cepat saat pandemi untuk contact tracing dan vaksinasi. Kunci: rapid development, scalable architecture untuk ratusan juta pengguna |

> **Konteks Indonesia:** Menurut laporan McKinsey (2023), Indonesia membutuhkan **9 juta talenta digital** tambahan hingga 2030. Software engineer yang memahami prinsip SE — bukan sekadar bisa coding — sangat dibutuhkan untuk membangun infrastruktur digital Indonesia yang reliable dan aman.

```python
# Visualisasi statistik kegagalan proyek software
def tampilkan_statistik_chaos():
    """
    Data dari Standish Group CHAOS Report 2020
    Menampilkan statistik keberhasilan proyek software
    """
    kategori = {
        "Berhasil (on time, on budget, on target)": 31,
        "Challenged (terlambat/over-budget)": 50,
        "Gagal Total (dibatalkan)": 19
    }

    print("=" * 60)
    print("STATISTIK KEBERHASILAN PROYEK SOFTWARE")
    print("Sumber: Standish Group CHAOS Report 2020")
    print("=" * 60)

    for kat, persen in kategori.items():
        bar = "█" * (persen // 2)
        print(f"\n{kat}")
        print(f"  {bar} {persen}%")

    print("\n" + "-" * 60)
    print("Kesimpulan: 69% proyek TIDAK berhasil sepenuhnya!")
    print("Inilah mengapa Software Engineering diperlukan.")

tampilkan_statistik_chaos()
```

**Output yang diharapkan:**
```
============================================================
STATISTIK KEBERHASILAN PROYEK SOFTWARE
Sumber: Standish Group CHAOS Report 2020
============================================================

Berhasil (on time, on budget, on target)
  ███████████████ 31%

Challenged (terlambat/over-budget)
  █████████████████████████ 50%

Gagal Total (dibatalkan)
  █████████ 19%

------------------------------------------------------------
Kesimpulan: 69% proyek TIDAK berhasil sepenuhnya!
Inilah mengapa Software Engineering diperlukan.
```

---

## 1.4 SWEBOK v4 (2024): Body of Knowledge SE

### 1.4.1 Apa Itu SWEBOK?

**SWEBOK** (*Software Engineering Body of Knowledge*) adalah dokumen referensi yang diterbitkan oleh **IEEE Computer Society** untuk mendefinisikan pengetahuan yang harus dikuasai oleh seorang software engineer profesional. SWEBOK berfungsi sebagai:

- **Panduan kurikulum** bagi universitas yang mengajarkan SE
- **Framework sertifikasi** untuk ujian profesional (CSEP — Certified Software Engineering Professional)
- **Referensi** bagi praktisi untuk memahami cakupan profesi SE

### 1.4.2 Sejarah SWEBOK

| Versi | Tahun | Highlight |
|-------|-------|-----------|
| SWEBOK v1 | 2001 | Draft pertama, 10 Knowledge Areas |
| SWEBOK v2 | 2004 | Resmi diterbitkan IEEE, 10 KA |
| SWEBOK v3 | 2014 | Diperluas menjadi 15 KA, ditambah foundations |
| **SWEBOK v4** | **2024** | Update signifikan: AI/ML foundations, modern practices, security emphasis |

### 1.4.3 15 Knowledge Areas SWEBOK v4

SWEBOK v4 mendefinisikan **15 Knowledge Areas (KA)** yang dikelompokkan menjadi tiga kategori:

```
┌──────────────────────────────────────────────────────────────┐
│                    SWEBOK v4 — 15 KNOWLEDGE AREAS            │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─── SOFTWARE ENGINEERING PRACTICE (KA 1-7) ────────────┐  │
│  │ 1. Software Requirements                               │  │
│  │ 2. Software Design                                     │  │
│  │ 3. Software Construction                               │  │
│  │ 4. Software Testing                                    │  │
│  │ 5. Software Maintenance                                │  │
│  │ 6. Software Configuration Management                   │  │
│  │ 7. Software Engineering Management                     │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌─── SE EDUCATION & PROFESSIONAL PRACTICE (KA 8-12) ───┐  │
│  │ 8. Software Engineering Process                        │  │
│  │ 9. Software Engineering Models and Methods             │  │
│  │ 10. Software Quality                                   │  │
│  │ 11. Software Engineering Professional Practice         │  │
│  │ 12. Software Engineering Economics                     │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌─── FOUNDATIONS (KA 13-15) ────────────────────────────┐  │
│  │ 13. Computing Foundations                              │  │
│  │ 14. Mathematical Foundations                           │  │
│  │ 15. Engineering Foundations                            │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Deskripsi detail setiap Knowledge Area:**

| No | Knowledge Area | Deskripsi | Topik Utama | Relevansi Kuliah Ini |
|----|---------------|-----------|-------------|---------------------|
| 1 | **Software Requirements** | Proses menentukan kebutuhan dan batasan perangkat lunak | Elicitation, analysis, specification, validation, management | Bab 3-4 (Minggu 3-4) |
| 2 | **Software Design** | Proses mendefinisikan arsitektur, komponen, interface, dan karakteristik lain dari sistem | Architectural design, detailed design, design patterns, UI design | Bab 5-6 (Minggu 5-6) |
| 3 | **Software Construction** | Implementasi desain menjadi kode yang executable | Coding practices, construction planning, construction testing | Bab 7 (Minggu 7) |
| 4 | **Software Testing** | Proses mengevaluasi software untuk menemukan defect | Test levels, test techniques, test automation, TDD | Bab 8-9 (Minggu 9-10) |
| 5 | **Software Maintenance** | Modifikasi software setelah delivery untuk memperbaiki fault, meningkatkan performa, atau adaptasi | Corrective, adaptive, perfective, preventive maintenance | Bab 11 (Minggu 12) |
| 6 | **Software Configuration Management (SCM)** | Mengelola dan mengendalikan perubahan pada software | Version control, change management, release management, build management | Bab 7 (Minggu 7) |
| 7 | **SE Management** | Perencanaan, pengelolaan, dan pengukuran proyek software | Project planning, risk management, measurement, personnel management | Bab 12 (Minggu 12) |
| 8 | **SE Process** | Definisi, implementasi, pengukuran, dan perbaikan proses SE | Process models, process assessment, process improvement (CMMI, SPICE) | Bab 2 (Minggu 2) |
| 9 | **SE Models and Methods** | Model dan metode yang digunakan dalam SE | Formal methods, modeling languages (UML), agile methods | Bab 5-6 (Minggu 5-6) |
| 10 | **Software Quality** | Kualitas software sebagai totalitas karakteristik yang memenuhi kebutuhan | Quality models (ISO 25010), quality assurance, metrics, reviews | Bab 9 (Minggu 10) |
| 11 | **SE Professional Practice** | Pengetahuan, keterampilan, dan sikap yang harus dimiliki SE profesional | Ethics, professional conduct, communication, teamwork | Bab 1 (Minggu 1), Bab 14 |
| 12 | **SE Economics** | Pengambilan keputusan berbasis ekonomi dalam SE | Cost estimation (COCOMO), value-based SE, ROI analysis | Bab 12 (Minggu 12) |
| 13 | **Computing Foundations** | Pengetahuan dasar computing yang menjadi prasyarat | Algorithms, data structures, programming languages, OS, networks | Prasyarat (INF-101/102) |
| 14 | **Mathematical Foundations** | Pengetahuan matematika yang diperlukan SE | Logic, sets, relations, functions, graphs, probability, statistics | Prasyarat |
| 15 | **Engineering Foundations** | Prinsip engineering umum yang berlaku di SE | Empirical methods, statistical analysis, measurement, design principles | Sepanjang semester |

### 1.4.4 Pemetaan SWEBOK v4 ke Kurikulum IF2205

```python
# Pemetaan SWEBOK v4 Knowledge Areas ke Minggu Kuliah
swebok_mapping = {
    "KA 1: Software Requirements":      ["Minggu 3", "Minggu 4"],
    "KA 2: Software Design":            ["Minggu 5", "Minggu 6"],
    "KA 3: Software Construction":       ["Minggu 7"],
    "KA 4: Software Testing":           ["Minggu 9", "Minggu 10"],
    "KA 5: Software Maintenance":        ["Minggu 12"],
    "KA 6: SW Configuration Mgmt":       ["Minggu 7"],
    "KA 7: SE Management":              ["Minggu 12"],
    "KA 8: SE Process":                 ["Minggu 2"],
    "KA 9: SE Models and Methods":       ["Minggu 5", "Minggu 6"],
    "KA 10: Software Quality":          ["Minggu 9", "Minggu 10"],
    "KA 11: SE Professional Practice":   ["Minggu 1", "Minggu 14"],
    "KA 12: SE Economics":              ["Minggu 12"],
    "KA 13: Computing Foundations":      ["Prasyarat (INF-101/102)"],
    "KA 14: Mathematical Foundations":   ["Prasyarat"],
    "KA 15: Engineering Foundations":    ["Sepanjang semester"],
}

print("=" * 65)
print("PEMETAAN SWEBOK v4 KE KURIKULUM IF2205")
print("=" * 65)
for ka, minggu_list in swebok_mapping.items():
    minggu_str = ", ".join(minggu_list)
    print(f"\n{ka}")
    print(f"  → {minggu_str}")
```

---

## 1.5 Mengapa Belajar SE di Era AI?

### 1.5.1 AI sebagai Tool, Bukan Pengganti

AI generatif (ChatGPT, Claude, GitHub Copilot) telah mengubah cara developer bekerja. Namun penting untuk memahami batasan AI:

```
┌──────────────────────────────────────────────────────────────┐
│           AI BISA                  │    SE TETAP DIBUTUHKAN  │
├────────────────────────────────────┼─────────────────────────┤
│ Generate code dari prompt          │ Memahami kebutuhan      │
│                                    │ stakeholder yang ambigu  │
│ Suggest code completion            │ Merancang arsitektur     │
│                                    │ yang scalable            │
│ Detect bugs dalam code             │ Memutuskan trade-off     │
│                                    │ design (security vs UX)  │
│ Generate unit tests                │ Memastikan software      │
│                                    │ memenuhi kebutuhan bisnis│
│ Explain & refactor code            │ Mengelola tim dan proses │
│                                    │ pengembangan             │
│ Translate antar bahasa             │ Bertanggung jawab atas   │
│ pemrograman                        │ kualitas dan ETIKA       │
│                                    │ software                 │
│ Menulis dokumentasi                │ Komunikasi dengan        │
│                                    │ stakeholder non-teknis   │
└────────────────────────────────────┴─────────────────────────┘
```

### 1.5.2 Peran SE di Era AI: Bergeser, Bukan Hilang

```
┌─────────────────────────────────────────────────────────┐
│  EVOLUSI PERAN SOFTWARE ENGINEER                        │
│                                                         │
│  Era Pre-AI (sebelum 2021):                             │
│  ┌─────────────────────────────────────────────┐       │
│  │ Menulis code 60% │ Design 20% │ Lainnya 20% │       │
│  └─────────────────────────────────────────────┘       │
│                                                         │
│  Era AI-Augmented (2024+):                              │
│  ┌─────────────────────────────────────────────┐       │
│  │ Arch+Design 30% │ Review 25% │ AI Collab 25%│ 20%  │
│  └─────────────────────────────────────────────┘       │
│                            Menulis code berkurang,      │
│                            tapi thinking meningkat!     │
└─────────────────────────────────────────────────────────┘
```

**Kesimpulan:** AI adalah **tool yang powerful**, bukan pengganti engineer. Software engineer yang mahir menggunakan AI akan jauh lebih produktif — tetapi mereka **tetap perlu memahami** fondasi SE: requirements, design, architecture, testing, ethics.

> **Analogi Islami:** Seperti kalkulator tidak menghilangkan kebutuhan memahami matematika, AI tidak menghilangkan kebutuhan memahami prinsip-prinsip SE. Seorang insinyur yang **amanah** harus menguasai ilmunya, bukan bergantung pada alat tanpa pemahaman.

---

## 1.6 Warisan Peradaban Islam dalam Ilmu Komputer

Sebagai mahasiswa di universitas Islam, penting mengetahui dan menghargai kontribusi peradaban Islam terhadap fondasi ilmu komputer modern:

### 1.6.1 Al-Khwarizmi (780-850 M) — Bapak Algoritma

**Muhammad ibn Musa al-Khwarizmi** adalah matematikawan dan astronom dari Khawarezm (Uzbekistan modern) yang bekerja di Bayt al-Hikmah (House of Wisdom) Baghdad.

- Kata **"algorithm"** berasal dari latinisasi namanya: "Algoritmi" → "Algorithm"
- Kata **"algebra"** berasal dari bukunya: *Kitab al-Jabr wa al-Muqabala* (Buku Pemulihan dan Perbandingan)
- Beliau mengembangkan prosedur langkah-demi-langkah yang sistematis untuk menyelesaikan persamaan — inilah esensi **algorithmic thinking** yang menjadi fondasi pemrograman

```
┌──────────────────────────────────────────────────────────┐
│  AL-KHWARIZMI → ALGORITHM → SOFTWARE ENGINEERING         │
│                                                          │
│  Kitab al-Jabr (820 M)                                   │
│       │                                                  │
│       ▼                                                  │
│  Prosedur sistematis untuk menyelesaikan masalah          │
│       │                                                  │
│       ▼                                                  │
│  Algorithmic thinking (abad 20)                           │
│       │                                                  │
│       ▼                                                  │
│  Programming & Software Engineering (abad 21)             │
└──────────────────────────────────────────────────────────┘
```

### 1.6.2 Ilmuwan Muslim Lain yang Berkontribusi

| Ilmuwan | Periode | Kontribusi | Relevansi SE Modern |
|---------|---------|-----------|-------------------|
| **Al-Kindi** (801-873 M) | Abad 9 | Kriptanalisis, frequency analysis | Fondasi cryptography dan security |
| **Ibn al-Haytham** (965-1040 M) | Abad 10-11 | Scientific method, eksperimen empiris | Fondasi software testing dan empirical SE |
| **Al-Jazari** (1136-1206 M) | Abad 12-13 | Automata, mesin mekanik programmable | Fondasi automation dan DevOps |
| **Banu Musa** (abad 9) | Abad 9 | Book of Ingenious Devices — 100 perangkat mekanik otomatis | Konsep control flow dan automation |

> **Refleksi:** Tradisi keilmuan Islam menekankan **pencarian ilmu yang sistematis dan bermanfaat**. Al-Khwarizmi tidak sekadar menemukan solusi — beliau mendokumentasikannya secara **terstruktur dan reproducible**. Inilah esensi software engineering: membangun solusi yang **sistematis, terdokumentasi, dan bisa dipelihara**.

---

## 1.7 Etika Profesi Software Engineer

### 1.7.1 Mengapa Etika Penting dalam SE?

Software saat ini mengendalikan:
- **Kehidupan manusia** — sistem kontrol pesawat, alat medis, kendaraan otonom
- **Data pribadi** — informasi kesehatan, keuangan, lokasi
- **Keputusan penting** — seleksi karyawan, kredit scoring, penegakan hukum
- **Infrastruktur kritis** — listrik, air, telekomunikasi

Ketika software engineer membuat keputusan teknis, mereka juga membuat keputusan **etis**.

### 1.7.2 ACM/IEEE Software Engineering Code of Ethics

ACM dan IEEE bersama menerbitkan **Software Engineering Code of Ethics and Professional Practice** dengan **8 prinsip utama**:

```
┌─────────────────────────────────────────────────────────────┐
│     ACM/IEEE SOFTWARE ENGINEERING CODE OF ETHICS            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. PUBLIC        Bertindak sesuai kepentingan publik       │
│                                                             │
│  2. CLIENT &      Bertindak demi kepentingan klien          │
│     EMPLOYER      dengan tetap menjaga kepentingan publik   │
│                                                             │
│  3. PRODUCT       Memastikan produk memenuhi standar        │
│                   profesional tertinggi                     │
│                                                             │
│  4. JUDGMENT      Menjaga integritas dan independensi       │
│                   profesional                               │
│                                                             │
│  5. MANAGEMENT    Mengelola pengembangan secara etis        │
│                                                             │
│  6. PROFESSION    Memajukan integritas dan reputasi profesi │
│                                                             │
│  7. COLLEAGUES    Berlaku adil dan mendukung rekan sejawat  │
│                                                             │
│  8. SELF          Terus belajar dan mengembangkan diri      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 1.7.3 Perspektif Islam dalam Etika SE

Nilai-nilai Islam memberikan kerangka etis tambahan yang memperkuat kode etik profesional:

| Nilai Islam | Bahasa Arab | Penerapan dalam SE |
|-------------|-------------|-------------------|
| **Amanah** (Trustworthiness) | الأمانة | Kode yang ditulis harus jujur — tidak menyembunyikan bug, tidak memanipulasi data pengguna, menjaga kepercayaan stakeholder. Contoh: melaporkan vulnerability meskipun berisiko menunda release. |
| **Keadilan (Al-'Adl)** | العدل | Software harus accessible dan fair untuk semua pengguna — tidak diskriminatif, memperhatikan inclusivity, tidak bias terhadap kelompok tertentu. Contoh: memastikan AI hiring tool tidak bias gender. |
| **Ihsan** (Excellence) | الإحسان | Berusaha menulis kode yang excellent — clean code sebagai bentuk ihsan, memberikan yang terbaik meskipun tidak diminta. Contoh: menambahkan unit test meskipun tidak diwajibkan. |
| **Itqan** (Perfection in Work) | الإتقان | Hadis: "Sesungguhnya Allah mencintai jika salah seorang dari kalian mengerjakan suatu pekerjaan, ia mengerjakannya dengan itqan (sempurna)." — Menyelesaikan setiap fase SDLC dengan teliti dan tuntas. |
| **Ilmu yang Bermanfaat** | العلم النافع | Software harus memberikan manfaat nyata bagi masyarakat — bukan sekadar menghasilkan profit, tapi memberikan value yang genuine. |

### 1.7.4 Studi Kasus Etika

**Kasus 1: Algoritma Diskriminatif**

Sebuah perusahaan teknologi mengembangkan sistem AI untuk seleksi karyawan. Setelah beberapa bulan, ditemukan bahwa sistem secara sistematis menolak kandidat perempuan karena data training didominasi profil karyawan laki-laki.

**Analisis berdasarkan kode etik:**
- **ACM Prinsip 1 (PUBLIC):** Sistem merugikan kepentingan publik (diskriminasi)
- **ACM Prinsip 3 (PRODUCT):** Produk tidak memenuhi standar profesional tertinggi
- **Amanah:** Engineer harus melaporkan bias meskipun hasilnya "terlihat bagus" secara statistik
- **Keadilan (Al-'Adl):** Software harus adil untuk semua kandidat tanpa memandang gender

**Bagaimana seharusnya engineer merespons:**
1. Segera melaporkan temuan ke manajemen
2. Mengusulkan audit data training dan evaluasi fairness
3. Menolak deploy sistem sebelum bias diperbaiki
4. Mendokumentasikan proses dan keputusan

**Kasus 2: Privasi Data Pengguna — Konteks Indonesia**

Sebuah startup kesehatan di Indonesia diminta oleh investor untuk menjual data riwayat kesehatan pengguna ke perusahaan asuransi. Data ini bisa digunakan untuk menolak klaim asuransi pengguna.

**Analisis:**
- **UU PDP (Perlindungan Data Pribadi) 2022:** Menjual data kesehatan tanpa persetujuan eksplisit melanggar hukum Indonesia
- **ACM Prinsip 2:** Kepentingan klien (investor) tidak boleh melanggar kepentingan publik (privasi pengguna)
- **Amanah:** Pengguna mempercayakan data kesehatannya — menjual tanpa izin adalah pengkhianatan amanah

```python
# Contoh implementasi privacy-by-design sederhana
class UserHealthData:
    """
    Contoh class yang menerapkan prinsip privacy-by-design.
    Data kesehatan pengguna dilindungi secara default.
    """

    def __init__(self, user_id, data_kesehatan):
        self._user_id = user_id
        self._data_kesehatan = data_kesehatan
        self._consent_log = {}  # Log persetujuan pengguna

    def get_data(self, requester, purpose):
        """
        Data hanya bisa diakses jika ada persetujuan eksplisit.
        Sesuai prinsip Amanah dan UU PDP 2022.
        """
        if purpose not in self._consent_log:
            print(f"DITOLAK: Belum ada persetujuan untuk tujuan '{purpose}'")
            print("Sesuai UU PDP 2022, persetujuan eksplisit diperlukan.")
            return None

        if self._consent_log[purpose] != True:
            print(f"DITOLAK: Pengguna menolak akses untuk '{purpose}'")
            return None

        print(f"DIIZINKAN: Akses data untuk '{purpose}' oleh '{requester}'")
        self._log_akses(requester, purpose)
        return self._data_kesehatan

    def set_consent(self, purpose, consent):
        """Mencatat persetujuan pengguna untuk tujuan tertentu."""
        self._consent_log[purpose] = consent
        print(f"Consent '{purpose}': {'Setuju' if consent else 'Menolak'}")

    def _log_akses(self, requester, purpose):
        """Mencatat setiap akses data (audit trail)."""
        from datetime import datetime
        print(f"  [LOG] {datetime.now()} - {requester} - {purpose}")


# Demonstrasi
user = UserHealthData("USR-001", {"tekanan_darah": "120/80"})

# Tanpa consent — ditolak
user.get_data("PT Asuransi X", "penentuan_premi")

print()

# Dengan consent eksplisit
user.set_consent("pengobatan", True)
user.get_data("RS Al Azhar", "pengobatan")
```

**Output yang diharapkan:**
```
DITOLAK: Belum ada persetujuan untuk tujuan 'penentuan_premi'
Sesuai UU PDP 2022, persetujuan eksplisit diperlukan.

Consent 'pengobatan': Setuju
DIIZINKAN: Akses data untuk 'pengobatan' oleh 'RS Al Azhar'
  [LOG] 2026-04-11 10:30:00 - RS Al Azhar - pengobatan
```

---

## 1.8 Studi Kasus Komprehensif: Analisis Kegagalan Proyek e-Government Indonesia

### Konteks

Pemerintah Indonesia telah menginvestasikan triliunan rupiah dalam proyek e-Government (e-KTP, SIPKD, OSS, berbagai sistem informasi daerah). Beberapa berhasil, banyak yang bermasalah. Mari analisis dari perspektif SE.

### Masalah Umum e-Government Indonesia

```
┌────────────────────────────────────────────────────────────┐
│        FAKTOR KEGAGALAN PROYEK e-GOVERNMENT INDONESIA      │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  1. REQUIREMENTS (50% masalah)                             │
│     ├── Kebutuhan tidak jelas dari awal                    │
│     ├── Setiap daerah memiliki kebutuhan berbeda           │
│     └── Regulasi berubah di tengah proyek                  │
│                                                            │
│  2. MANAJEMEN PROYEK (25% masalah)                         │
│     ├── Kontraktor menang tender tapi kurang kompeten      │
│     ├── Timeline tidak realistis (sesuai tahun anggaran)   │
│     └── Koordinasi antar K/L (Kementerian/Lembaga) lemah   │
│                                                            │
│  3. TEKNIS (15% masalah)                                   │
│     ├── Arsitektur monolitik, sulit discale                │
│     ├── Integrasi antar sistem tidak terstandarisasi       │
│     └── Testing dan QA tidak memadai                       │
│                                                            │
│  4. MAINTENANCE (10% masalah)                              │
│     ├── Setelah proyek selesai, tidak ada tim maintenance   │
│     ├── Dokumentasi teknis minim                           │
│     └── Vendor lock-in                                     │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### Analisis dengan SWEBOK

| Knowledge Area | Masalah yang Ditemukan | Rekomendasi Perbaikan |
|---------------|----------------------|----------------------|
| KA 1: Requirements | Elicitation tidak melibatkan pengguna akhir (petugas kelurahan, warga) | Gunakan teknik elicitation yang tepat: interview, observation, prototyping |
| KA 2: Design | Monolithic architecture, tidak modular | Gunakan microservices, API-first design |
| KA 4: Testing | Testing minim sebelum go-live | Mandatory testing: unit, integration, load testing |
| KA 5: Maintenance | Tidak ada rencana maintenance | Sediakan tim maintenance dan alokasi anggaran tahunan |
| KA 8: Process | Waterfall rigid tanpa iterasi | Adopsi Agile dengan feedback loop pendek |

> **Pelajaran untuk Mahasiswa:** Ketika Anda nanti berkarir — baik di startup, korporasi, atau pemerintahan — prinsip-prinsip SE yang dipelajari di kuliah ini akan membantu Anda menghindari kesalahan yang sama. Bukan hanya soal teknis coding, tapi **proses, manajemen, requirements, dan etika**.

---

## AI Corner: Pengenalan AI untuk SE (Level: Basic)

### 1. Memahami Konsep SE dengan Bantuan AI

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| Memahami definisi | "Jelaskan perbedaan software engineering dan programming dengan analogi konstruksi bangunan" | Bandingkan jawaban AI dengan materi kuliah ini |
| Eksplorasi SWEBOK | "Sebutkan 15 Knowledge Areas SWEBOK v4 dan berikan contoh praktis masing-masing" | Verifikasi dengan dokumen resmi IEEE |

### 2. Eksplorasi Software Crisis dengan AI

**Prompt:**
```
Berikan timeline 10 kegagalan software terkenal dari 1985 hingga 2024,
beserta penyebab teknis dan pelajaran SE yang bisa dipetik dari
masing-masing kasus. Format sebagai tabel.
```

**Evaluasi output AI:**
- Apakah fakta dan tahunnya akurat? (AI bisa salah — verifikasi!)
- Apakah analisis penyebab teknis masuk akal?
- Adakah kasus yang terlewat?

### 3. Diskusi Etika dengan AI

**Prompt:**
```
Saya seorang software engineer di startup Indonesia. CTO meminta saya
menambahkan fitur yang secara diam-diam melacak lokasi pengguna tanpa
persetujuan untuk tujuan marketing. Berdasarkan ACM Code of Ethics
dan UU PDP Indonesia 2022, apa yang harus saya lakukan? Berikan
langkah-langkah konkret.
```

**Catatan:** AI bisa memberikan perspektif, tetapi **keputusan etis tetap di tangan engineer**. Gunakan AI sebagai sparring partner untuk berpikir, bukan sebagai oracle yang selalu benar.

### 4. Latihan Prompt Engineering untuk SE

Coba bandingkan respons dari prompt berikut:

| Prompt A (Kurang Baik) | Prompt B (Lebih Baik) |
|-------------------------|----------------------|
| "Apa itu software engineering?" | "Jelaskan software engineering untuk mahasiswa Informatika semester 4 yang sudah bisa programming Python. Fokus pada apa yang berbeda dari programming, berikan 3 contoh konkret, dan jelaskan mengapa SE penting di era AI." |

**Mengapa Prompt B lebih baik?**
- Menentukan **audiens** (mahasiswa semester 4)
- Menentukan **konteks** (sudah bisa Python)
- Menentukan **fokus** (perbedaan dengan programming)
- Menentukan **format** (3 contoh konkret)
- Menentukan **perspektif** (era AI)

### 5. Hands-on: Evaluasi AI tentang SWEBOK

**Tugas:**
1. Minta AI menjelaskan salah satu Knowledge Area SWEBOK v4 (misalnya KA 10: Software Quality)
2. Bandingkan dengan penjelasan di dokumen resmi SWEBOK v4
3. Catat perbedaan atau kesalahan yang ditemukan
4. Tulis refleksi: apakah AI bisa menggantikan membaca dokumen asli?

### Aturan AI di Kuliah Ini

```
┌─────────────────────────────────────────────────────────────┐
│              KEBIJAKAN PENGGUNAAN AI — IF2205               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ✓ DIIZINKAN (dengan AI Usage Log):                        │
│    - Tugas mingguan (T1-T6)                                │
│    - Proyek akhir (sebagai coding partner)                  │
│    - Latihan dan eksplorasi materi                          │
│                                                             │
│  ✗ TIDAK DIIZINKAN:                                        │
│    - Kuis (K1-K3) — closed-book                            │
│    - UTS — closed-book                                      │
│    - UAS — closed-book + 1 lembar catatan A4               │
│                                                             │
│  ⚠ PRINSIP UTAMA:                                          │
│    AI adalah coding partner, BUKAN pengganti pemikiran      │
│    kritis. Anda WAJIB memahami dan mampu menjelaskan        │
│    setiap output AI yang digunakan.                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Latihan Soal

### Level Dasar (C1-C2) — 7 Soal

1. Jelaskan definisi rekayasa perangkat lunak (*software engineering*) menurut IEEE. Apa tiga kata kunci yang menjadi ciri utama pendekatan SE?

2. Sebutkan **7 perbedaan** antara programming dan software engineering. Berikan contoh konkret untuk masing-masing.

3. Apa yang dimaksud dengan "software crisis"? Sebutkan empat gejala utamanya.

4. Jelaskan secara singkat **5 kasus kegagalan software** yang Anda anggap paling penting, beserta pelajaran utama dari masing-masing.

5. Sebutkan **15 Knowledge Areas** dalam SWEBOK v4 dan kelompokkan ke dalam tiga kategori utamanya.

6. Sebutkan **8 prinsip** ACM/IEEE Software Engineering Code of Ethics.

7. Siapakah Al-Khwarizmi dan apa kontribusinya terhadap ilmu komputer? Jelaskan hubungan antara nama beliau dan kata "algorithm".

### Level Menengah (C3-C4) — 7 Soal

8. Mengapa pendekatan yang sistematis (*systematic*) diperlukan dalam pengembangan software berskala besar? Berikan analogi dengan disiplin engineering lain (misalnya teknik sipil atau teknik mesin).

9. Analisis kasus **Boeing 737 MAX MCAS** dari perspektif SWEBOK v4 — Knowledge Area mana saja yang relevan, dan apa yang seharusnya dilakukan berbeda di setiap KA tersebut?

10. Bandingkan peran software engineer **sebelum era AI** (pre-2021) dan **di era AI** (2024+). Aspek apa yang berubah dan aspek apa yang tetap?

11. Analisis **satu proyek e-Government Indonesia** (pilih: e-KTP, BPJS, SIPKD, atau lainnya) menggunakan framework SWEBOK v4. KA mana yang paling bermasalah?

12. Bagaimana nilai **Amanah** (الأمانة) dapat diterapkan secara konkret dalam setiap fase SDLC? Berikan contoh untuk fase: Requirements, Design, Construction, Testing, dan Deployment.

13. Jelaskan mengapa **biaya perbaikan bug meningkat secara eksponensial** seiring tahap SDLC. Berikan contoh skenario konkret.

14. Bandingkan pendekatan SE Indonesia (startup seperti Gojek/Tokopedia) dengan tantangan SE di pemerintahan (proyek e-KTP, SIPKD). Apa perbedaan dan persamaan masalahnya?

### Level Mahir (C5-C6) — 6 Soal

15. Seorang klien meminta Anda membangun fitur yang menurut analisis Anda akan melanggar privasi pengguna (mengumpulkan data lokasi tanpa consent). Bagaimana Anda merespons? Jawab berdasarkan:
    - ACM Code of Ethics (prinsip mana yang relevan?)
    - UU PDP Indonesia 2022
    - Nilai Islam (Amanah, Keadilan)

16. Kasus Volkswagen Dieselgate menunjukkan bahwa software bisa digunakan sebagai **alat penipuan**. Rancang sebuah **framework audit etika** untuk software engineering yang mengintegrasikan kode etik ACM/IEEE dan nilai-nilai Islam. Framework harus mencakup minimal 5 checkpoint dalam SDLC.

17. Rancang proposal singkat bagaimana **SWEBOK v4** bisa dijadikan framework untuk mengaudit kualitas proyek software di pemerintahan Indonesia. Sebutkan minimal 5 KA yang paling relevan dan bagaimana cara mengauditnya.

18. Evaluasi dampak AI generatif terhadap **masa depan profesi software engineer di Indonesia**. Pekerjaan SE apa yang paling terdampak? Skill apa yang menjadi semakin penting?

19. Desain sebuah **kurikulum pelatihan SE** untuk developer junior di startup Indonesia yang mengintegrasikan penggunaan AI tools. Apa yang harus diajarkan terlebih dahulu: programming skills atau SE principles? Jelaskan alasannya.

20. Refleksi kritis: Apakah istilah "software crisis" masih relevan di tahun 2026? Berikan argumentasi **pro** dan **kontra** dengan bukti dari kasus-kasus terkini (2020-2025).

---

## Rangkuman

1. **Rekayasa Perangkat Lunak** (*Software Engineering*) adalah pendekatan yang **sistematis, disiplin, dan terukur** terhadap seluruh lifecycle software — bukan sekadar programming.

2. **Sejarah SE** dimulai dari Konferensi NATO 1968 di Garmisch, Jerman, dan terus berkembang melalui era Waterfall (1970s), OOP (1980s), Agile (2001), DevOps (2010s), hingga AI-Augmented (2020s).

3. **Software crisis** bukan hanya fenomena historis — kegagalan software terus terjadi (Crowdstrike 2024, Log4Shell 2021, Boeing 737 MAX 2018). Diperlukan pendekatan SE yang profesional untuk mencegahnya.

4. **SWEBOK v4** (2024) mendefinisikan **15 Knowledge Areas** yang menjadi body of knowledge profesi SE, dikelompokkan ke dalam Practice (1-7), Education & Professional Practice (8-12), dan Foundations (13-15).

5. Di **era AI**, peran SE **bergeser** — dari fokus menulis kode ke fokus pada arsitektur, review, dan kolaborasi dengan AI — tetapi fondasi SE (requirements, design, testing, ethics) tetap krusial.

6. **Al-Khwarizmi** dan ilmuwan Muslim lainnya memberikan kontribusi fundamental pada fondasi ilmu komputer — tradisi keilmuan Islam menekankan pendekatan yang sistematis dan bermanfaat.

7. **Etika profesi** berdasarkan ACM/IEEE Code of Ethics dan nilai Islam (Amanah, Keadilan, Ihsan, Itqan) menjadi fondasi praktik SE yang bertanggung jawab.

8. **Konteks Indonesia:** Baik startup (Gojek, Tokopedia) maupun proyek pemerintah (e-KTP, BPJS) menunjukkan bahwa keberhasilan software ditentukan bukan hanya oleh kemampuan coding, tapi oleh penerapan prinsip SE secara menyeluruh.

---

## Referensi

1. IEEE Computer Society. (2024). *SWEBOK v4: Guide to the Software Engineering Body of Knowledge*. IEEE.
2. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 1. Pearson.
3. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). Chapter 1. McGraw-Hill.
4. ACM/IEEE. (1999). *Software Engineering Code of Ethics and Professional Practice*. ACM/IEEE Joint Task Force.
5. Standish Group. (2020). *CHAOS Report 2020*. The Standish Group International.
6. Brooks, F. P. (1975). *The Mythical Man-Month: Essays on Software Engineering*. Addison-Wesley.
7. Leveson, N. G. & Turner, C. S. (1993). "An Investigation of the Therac-25 Accidents." *IEEE Computer*, 26(7).
8. Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP).

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
