# Minggu 8: UTS — Review dan Ujian Tengah Semester

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 8 dari 16 |
| **Topik** | Review Minggu 1-7, Ujian Tengah Semester |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **CPMK** | CPMK 1-4 |
| **Sub-CPMK** | Review seluruh Sub-CPMK 1.1 - 4.2 |
| **Durasi** | 150 menit (Review: 50 menit + UTS: 100 menit) |
| **Metode** | Review session interaktif, ujian tertulis |

## Tujuan Pembelajaran

1. **Mengintegrasikan** pemahaman konsep RPL dari Minggu 1-7 dalam kerangka berpikir yang utuh (C4)
2. **Menerapkan** pengetahuan Minggu 1-7 untuk menjawab soal analisis dan problem solving (C3-C4)
3. **Mengevaluasi** kesiapan diri menghadapi UTS melalui latihan soal (C5)

---

## Peta Konsep Minggu 1-7

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PETA KONSEP MINGGU 1-7                                │
│                                                                          │
│  MINGGU 1: FONDASI RPL                                                  │
│  ┌─────────────────────────────────────────────────────────────┐        │
│  │ Definisi SE vs Programming | Software Crisis (NATO 1968)    │        │
│  │ SWEBOK v4 (15 KA) | SDLC Phases | Etika (ACM/IEEE + Islam) │        │
│  └───────────────────────────────┬─────────────────────────────┘        │
│                                  │                                       │
│  MINGGU 2: PROSES & MODEL        │                                       │
│  ┌───────────────────────────────┴─────────────────────────────┐        │
│  │ Waterfall | V-Model | Spiral | Agile Manifesto              │        │
│  │ Scrum (Roles, Events, Artifacts) | Kanban | DevOps           │        │
│  └───────────────────────────────┬─────────────────────────────┘        │
│                                  │                                       │
│  MINGGU 3: REQUIREMENTS ENGINEERING                                     │
│  ┌───────────────────────────────┴─────────────────────────────┐        │
│  │ Elicitation (Interview, Observation, Prototyping)            │        │
│  │ FR vs NFR | SRS (IEEE 830) | Validasi Requirements           │        │
│  └───────────────────────────────┬─────────────────────────────┘        │
│                                  │                                       │
│  MINGGU 4: PEMODELAN REQUIREMENTS                                       │
│  ┌───────────────────────────────┴─────────────────────────────┐        │
│  │ Use Case Diagram & Narrative | User Stories (INVEST)         │        │
│  │ Acceptance Criteria (Given-When-Then) | Product Backlog      │        │
│  │ MoSCoW Prioritization | Story Points (Fibonacci)            │        │
│  └───────────────────────────────┬─────────────────────────────┘        │
│                                  │                                       │
│  MINGGU 5: ARSITEKTUR & DESIGN PATTERNS                                 │
│  ┌───────────────────────────────┴─────────────────────────────┐        │
│  │ 5 Architectural Styles (Monolithic, Layered, MVC,            │        │
│  │   Microservices, Event-Driven) | Quality Attributes          │        │
│  │ SOLID Principles | 4 GoF Patterns (Singleton, Factory,       │        │
│  │   Observer, Strategy) | C4 Model | ADR                       │        │
│  └───────────────────────────────┬─────────────────────────────┘        │
│                                  │                                       │
│  MINGGU 6: DESAIN & DATABASE                                            │
│  ┌───────────────────────────────┴─────────────────────────────┐        │
│  │ UML: Class, Sequence, Activity, State, Component Diagram     │        │
│  │ ERD & Normalisasi (1NF-3NF) | Relasi (1:1, 1:N, N:M)       │        │
│  │ RESTful API (HTTP methods, status codes, versioning)         │        │
│  │ SQLAlchemy | Flask API                                       │        │
│  └───────────────────────────────┬─────────────────────────────┘        │
│                                  │                                       │
│  MINGGU 7: CONSTRUCTION & VERSION CONTROL                               │
│  ┌───────────────────────────────┴─────────────────────────────┐        │
│  │ Clean Code (10 prinsip) | PEP 8 | Code Smells (12 jenis)    │        │
│  │ Refactoring Techniques | Git Flow/GitHub Flow                │        │
│  │ Conventional Commits | PR & Code Review Best Practices       │        │
│  └─────────────────────────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────────────────────────┘
```

## Ringkasan CPMK yang Diujikan

| CPMK | Topik Kunci | Bloom's | Tipe Soal yang Diharapkan |
|------|-------------|---------|---------------------------|
| **CPMK-1** | Definisi SE, SWEBOK v4, software crisis, model proses (Waterfall, Agile, Scrum), Agile Manifesto | C2 | Pilihan ganda, uraian singkat |
| **CPMK-2** | Requirements engineering, elicitation techniques, FR/NFR, SRS, use case, user stories, INVEST, acceptance criteria | C3 | Uraian, studi kasus |
| **CPMK-3** | Architectural styles, quality attributes, SOLID, design patterns, UML diagrams, ERD, normalisasi, REST API | C3-C4 | Diagram, analisis, implementasi |
| **CPMK-4** | Clean code, PEP 8, code smells, refactoring, Git flow, conventional commits, code review | C3-C4 | Analisis kode, uraian |

## Konsep Kunci yang Wajib Dikuasai

### Daftar Istilah dan Definisi Penting

| Istilah | Definisi Singkat |
|---------|-----------------|
| Software Engineering | Pendekatan sistematis, disiplin, dan terukur untuk pengembangan software |
| SWEBOK v4 | Guide to Software Engineering Body of Knowledge — 15 Knowledge Areas |
| SDLC | Software Development Life Cycle — siklus hidup pengembangan software |
| Agile Manifesto | 4 values + 12 principles untuk pengembangan software yang adaptif |
| Scrum | Framework Agile: 3 roles, 5 events, 3 artifacts |
| Functional Requirement | Apa yang harus dilakukan sistem (fitur) |
| Non-Functional Requirement | Bagaimana sistem harus berperilaku (kualitas) |
| SRS | Software Requirements Specification — dokumen kebutuhan software |
| INVEST | Independent, Negotiable, Valuable, Estimable, Small, Testable |
| Given-When-Then | Format acceptance criteria dari BDD |
| MoSCoW | Must, Should, Could, Won't — teknik prioritisasi |
| SOLID | 5 prinsip desain OOP: SRP, OCP, LSP, ISP, DIP |
| Design Pattern | Solusi teruji untuk masalah desain yang sering muncul |
| UML | Unified Modeling Language — bahasa visual untuk modeling |
| ERD | Entity-Relationship Diagram — model data/database |
| Normalisasi | Proses menghilangkan redundansi data (1NF, 2NF, 3NF) |
| REST | Representational State Transfer — arsitektur API |
| Code Smell | Indikasi masalah desain dalam kode (bukan bug) |
| Refactoring | Mengubah struktur internal kode tanpa mengubah perilaku eksternal |
| Conventional Commits | Format standar pesan commit: `type(scope): description` |

### Formula dan Aturan Penting

```
┌─────────────────────────────────────────────────────────────────┐
│              FORMULA & ATURAN YANG PERLU DIINGAT                 │
│                                                                  │
│  1. Story Points: Skala Fibonacci (1, 2, 3, 5, 8, 13, 21)     │
│     Velocity = total story points yang selesai per sprint        │
│                                                                  │
│  2. Scrum:                                                      │
│     Roles: Product Owner, Scrum Master, Dev Team                │
│     Events: Sprint Planning, Daily Standup, Sprint Review,      │
│             Sprint Retrospective, Sprint (2-4 minggu)           │
│     Artifacts: Product Backlog, Sprint Backlog, Increment       │
│                                                                  │
│  3. HTTP Methods:                                               │
│     GET = Read | POST = Create | PUT = Update (full)            │
│     PATCH = Update (partial) | DELETE = Delete                   │
│                                                                  │
│  4. HTTP Status:                                                │
│     2xx = Success | 4xx = Client Error | 5xx = Server Error     │
│     200 OK | 201 Created | 400 Bad Request | 404 Not Found      │
│                                                                  │
│  5. Normalisasi:                                                │
│     1NF = Atomik | 2NF = Full FD pada PK | 3NF = No transitive │
│                                                                  │
│  6. SOLID:                                                      │
│     S = Single Responsibility | O = Open/Closed                 │
│     L = Liskov Substitution  | I = Interface Segregation        │
│     D = Dependency Inversion                                    │
│                                                                  │
│  7. Conventional Commits:                                       │
│     feat: | fix: | docs: | style: | refactor: | test: | chore: │
└─────────────────────────────────────────────────────────────────┘
```

---

## Format UTS

| Komponen | Detail |
|----------|--------|
| **Durasi** | 100 menit |
| **Tipe** | Closed-book, tanpa AI/internet |
| **Bobot** | 20% nilai akhir |
| **Alat tulis** | Pulpen hitam/biru, penggaris (untuk diagram) |

### Struktur Soal

| Bagian | Tipe | Jumlah | Bobot | CPMK |
|--------|------|--------|-------|------|
| A | Pilihan Ganda (PG) | 20 soal | 30 poin | 1-4 |
| B | Essay/Uraian | 3 soal | 30 poin | 1-4 |
| C | Studi Kasus & Diagram | 2 soal | 40 poin | 2-4 |
| **Total** | | **25 soal** | **100 poin** | |

### Distribusi Soal per CPMK

| CPMK | PG | Essay | Studi Kasus | Total Bobot |
|------|----|-------|-------------|-------------|
| CPMK-1 (Fondasi, Proses) | 5 soal | 1 soal | — | 20% |
| CPMK-2 (Requirements) | 5 soal | 1 soal | 1 studi kasus (parsial) | 30% |
| CPMK-3 (Arsitektur, Desain) | 5 soal | — | 1 studi kasus (diagram) | 30% |
| CPMK-4 (Construction) | 5 soal | 1 soal | — | 20% |

---

## Contoh Soal UTS

### Bagian A: Pilihan Ganda (30 poin)

**Soal 1 (CPMK-1, C2):**
Manakah yang BUKAN merupakan Scrum Event?
- a) Sprint Planning
- b) Daily Standup
- c) Code Review
- d) Sprint Retrospective

**Jawaban: c)** — Code Review bukan Scrum Event. Scrum Events: Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective.

---

**Soal 2 (CPMK-1, C2):**
Agile Manifesto menyatakan "Individuals and interactions over processes and tools". Apa makna pernyataan ini?
- a) Proses dan tools tidak penting sama sekali
- b) Komunikasi dan kolaborasi tim lebih bernilai daripada proses rigid
- c) Tidak perlu menggunakan tools apapun
- d) Individual work lebih baik daripada teamwork

**Jawaban: b)** — Agile menghargai kedua sisi, tapi lebih menekankan interaksi manusia.

---

**Soal 3 (CPMK-2, C2):**
Kriteria "V" dalam INVEST untuk user story berarti:
- a) Verifiable — bisa dibuktikan kebenarannya
- b) Valuable — memberikan nilai bagi pengguna
- c) Versatile — bisa digunakan di banyak konteks
- d) Visual — harus digambarkan dalam diagram

**Jawaban: b)** — Valuable: setiap user story harus memberikan nilai bagi pengguna atau bisnis.

---

**Soal 4 (CPMK-3, C2):**
Prinsip SOLID yang menyatakan "class hanya boleh bergantung pada abstraksi, bukan implementasi konkret" adalah:
- a) Single Responsibility Principle
- b) Open/Closed Principle
- c) Interface Segregation Principle
- d) Dependency Inversion Principle

**Jawaban: d)** — DIP: high-level modules depend on abstractions, not concrete implementations.

---

**Soal 5 (CPMK-3, C2):**
HTTP status code 201 digunakan ketika:
- a) Request berhasil dan data dikembalikan
- b) Resource baru berhasil dibuat
- c) Client mengirim request yang tidak valid
- d) Resource tidak ditemukan

**Jawaban: b)** — 201 Created digunakan setelah POST berhasil membuat resource baru.

---

**Soal 6 (CPMK-4, C2):**
Manakah yang merupakan contoh code smell "Magic Number"?
- a) Fungsi dengan 200 baris kode
- b) `if user.status == 3:`
- c) Kode yang tidak pernah dieksekusi
- d) Class dengan 20 methods

**Jawaban: b)** — Angka 3 tanpa konteks adalah magic number. Harus diganti dengan named constant.

---

### Bagian B: Essay/Uraian (30 poin)

**Soal 7 (CPMK-1, C2, 10 poin):**

Jelaskan perbedaan mendasar antara model pengembangan **Waterfall** dan **Agile/Scrum**. Dalam konteks proyek pengembangan aplikasi e-commerce UMKM di Indonesia, model mana yang lebih cocok? Berikan 3 alasan yang mendukung.

**Rubrik:**
- Perbedaan Waterfall vs Agile (4 poin)
- Pilihan model yang tepat untuk konteks (2 poin)
- 3 alasan yang logis dan kontekstual (4 poin)

---

**Soal 8 (CPMK-2, C3, 10 poin):**

Diberikan skenario: Perpustakaan Universitas Al Azhar Indonesia ingin membangun sistem peminjaman buku online.

a) Tulis 3 user stories yang memenuhi kriteria INVEST (3 poin)
b) Untuk salah satu user story, tulis 2 acceptance criteria dalam format Given-When-Then (4 poin)
c) Prioritaskan ketiga user story menggunakan MoSCoW dan berikan alasan (3 poin)

---

**Soal 9 (CPMK-4, C4, 10 poin):**

Identifikasi **4 code smells** dalam kode berikut dan jelaskan teknik refactoring yang tepat untuk setiap smell:

```python
def process(d, u):
    result = []
    for item in d:
        if item['type'] == 'buku':
            if item['stok'] > 0:
                if u.status == 1:
                    if u.pinjam < 5:
                        item['ok'] = True
                        result.append(item)
                        import smtplib
                        s = smtplib.SMTP('smtp.gmail.com', 587)
                        s.sendmail("lib@uai.ac.id", u.email,
                                 f"Buku {item['judul']} ready")
    return result
```

**Rubrik:**
- Identifikasi 4 code smells (4 poin)
- Penjelasan refactoring yang tepat untuk masing-masing (4 poin)
- Contoh kode setelah refactoring (2 poin bonus)

---

### Bagian C: Studi Kasus & Diagram (40 poin)

**Soal 10 (CPMK-2 + CPMK-3, C3-C4, 20 poin):**

Sebuah startup transportasi di Surabaya ingin membangun aplikasi "AngkotKu" untuk mempermudah penumpang menemukan dan membayar angkot. Tim terdiri dari 5 developer, menggunakan Scrum, deadline MVP 3 bulan.

a) Buatlah **Use Case Diagram** untuk fitur utama: penumpang mencari rute, pesan angkot, bayar online, sopir terima pesanan (6 poin)

b) Tulis **Use Case Narrative** lengkap untuk "Pesan Angkot" meliputi: aktor, precondition, main flow (min 5 step), 2 alternative flows, postcondition (6 poin)

c) Gambarkan **Class Diagram** minimal 4 class (User, Penumpang, Sopir, Pesanan) dengan atribut, method, dan relasi (4 poin)

d) Arsitektur apa yang paling cocok untuk aplikasi ini? Gambarkan **arsitektur high-level** dan berikan alasan pemilihan (4 poin)

---

**Soal 11 (CPMK-3 + CPMK-4, C3-C4, 20 poin):**

Berdasarkan skenario "AngkotKu" di soal 10:

a) Desain **ERD** untuk sistem ini dengan minimal 4 entitas. Tunjukkan primary key, foreign key, dan kardinalitas. Pastikan desain memenuhi 3NF (6 poin)

b) Desain **5 REST API endpoint** untuk fitur pemesanan angkot. Sertakan HTTP method, URL, deskripsi, contoh request body (jika ada), dan status code (6 poin)

c) Gambarkan **Sequence Diagram** untuk alur: penumpang pesan angkot -> sistem cari sopir terdekat -> sopir menerima pesanan -> penumpang mendapat konfirmasi (4 poin)

d) Identifikasi **design pattern** yang cocok untuk fitur notifikasi ke penumpang dan sopir. Jelaskan mengapa pattern tersebut cocok dan berikan skeleton kode Python-nya (4 poin)

---

## Tips Persiapan UTS

```
┌─────────────────────────────────────────────────────────────────┐
│                    STRATEGI BELAJAR UTS                           │
│                                                                  │
│  1. REVIEW PETA KONSEP                                          │
│     Pastikan bisa menjelaskan hubungan antar topik:             │
│     Requirements -> Use Case -> User Story -> Backlog           │
│     Arsitektur -> SOLID -> Design Pattern -> UML                │
│                                                                  │
│  2. LATIHAN DIAGRAM                                             │
│     UTS banyak soal diagram — latih menggambar:                 │
│     Use Case, Class, Sequence, ERD, Architecture                │
│     Gunakan kertas dan pensil, bukan tools!                     │
│                                                                  │
│  3. PAHAMI KONSEP, BUKAN HAFAL                                  │
│     "Mengapa SOLID penting?" lebih penting dari                 │
│     "Sebutkan 5 prinsip SOLID"                                  │
│                                                                  │
│  4. LATIH ANALISIS KODE                                         │
│     Soal code smell dan refactoring butuh latihan               │
│     Identifikasi masalah, jelaskan solusi                       │
│                                                                  │
│  5. KONTEKS INDONESIA                                           │
│     Contoh dan studi kasus menggunakan konteks Indonesia        │
│     Pikirkan: Gojek, Tokopedia, BPJS, TransJakarta, UAI        │
│                                                                  │
│  6. KELOLA WAKTU                                                │
│     PG (30 menit) -> Essay (30 menit) -> Studi Kasus (40 menit)│
│     Jangan terlalu lama di satu soal!                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## Kegiatan Pembelajaran

### Pre-class (20 menit)

- Review seluruh materi Minggu 1-7 menggunakan peta konsep di atas
- Kerjakan contoh soal secara mandiri (tanpa melihat jawaban)
- Siapkan pertanyaan untuk sesi review

### In-class (150 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-15 menit | Review peta konsep: koneksi antar topik Minggu 1-7 | Ceramah interaktif |
| 15-35 menit | Tanya jawab: mahasiswa mengajukan pertanyaan | Diskusi terbuka |
| 35-50 menit | Review contoh soal studi kasus dan diagram | Latihan bersama |
| 50-150 menit | **UTS**: Ujian Tengah Semester (100 menit) | Ujian tertulis |

### Post-class

- Refleksi: Identifikasi area yang perlu diperkuat untuk paruh semester kedua
- Preview: Software Testing & QA di Minggu 9
- Proyek akhir: Sprint 1 tetap berjalan (Minggu 7+9) — tidak ada aktivitas sprint di Minggu 8

---

## Referensi

Seluruh referensi Minggu 1-7 berlaku untuk persiapan UTS:

1. Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson.
2. IEEE Computer Society. (2024). *SWEBOK v4*. IEEE.
3. Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide*. Scrum.org.
4. Cohn, M. (2004). *User Stories Applied*. Addison-Wesley.
5. Gamma, E. et al. (1994). *Design Patterns*. Addison-Wesley.
6. Martin, R. C. (2009). *Clean Code*. Prentice Hall.
7. Fowler, M. (2003). *UML Distilled* (3rd ed.). Addison-Wesley.
8. Fowler, M. (2019). *Refactoring* (2nd ed.). Addison-Wesley.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
