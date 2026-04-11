# Lab 13: AI Pair Programming dan Code Review

## Informasi Praktikum

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Praktikum** | 12 dari 13 (Minggu 13) |
| **Topik** | AI sebagai Pair Programmer, AI-Assisted Code Review |
| **CPMK** | CPMK-7 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 12 (Docker & Deployment) selesai |
| **Referensi Teori** | IF2205 Minggu 13 — AI-Augmented Software Engineering |

## Tujuan

1. **Menggunakan** (C3) AI (Claude/Copilot) sebagai pair programmer untuk fitur baru
2. **Mengevaluasi** (C5) kualitas kode yang dihasilkan AI secara kritis
3. **Melakukan** (C4) AI-assisted code review pada kode tim
4. **Mendokumentasikan** (C3) penggunaan AI dalam AI Usage Log secara transparan

## Konsep Singkat

### AI dalam Software Engineering

AI tools telah mengubah cara developer bekerja. Namun, AI adalah **asisten, bukan pengganti** — mahasiswa tetap harus memahami kode yang dihasilkan dan bertanggung jawab atas kualitasnya.

```
Peran AI dalam SE
=================

  Developer (Anda)              AI Tool
  ================              =======
  - Menentukan APA yang         - Menyarankan BAGAIMANA
    dibutuhkan                    mengimplementasikan
  - Mengevaluasi output         - Generate kode boilerplate
  - Membuat keputusan desain    - Menemukan bug potensial
  - Bertanggung jawab atas      - Menulis test cases
    kualitas akhir              - Generate dokumentasi

  Prinsip: AI mempercepat, ANDA yang memastikan kualitas.
```

### AI Usage Spectrum

| Level | Penggunaan AI | Contoh | Etika |
|-------|--------------|--------|-------|
| **0 — Tanpa AI** | Semua kode ditulis manual | UTS/UAS, coding interview | Wajib untuk penilaian individu |
| **1 — AI sebagai referensi** | Membaca penjelasan AI, menulis kode sendiri | Belajar konsep baru | Harus dicatat di AI Usage Log |
| **2 — AI sebagai pair programmer** | Diskusi bolak-balik dengan AI, modifikasi output | Lab dan tugas | Harus dicatat + dievaluasi |
| **3 — AI generate, manusia review** | AI menulis, Anda review dan perbaiki | Boilerplate, test cases | Harus dicatat + dimodifikasi |
| **4 — Copy-paste tanpa review** | Langsung pakai output AI | **TIDAK DIPERBOLEHKAN** | Melanggar prinsip *amanah* |

### Framework CRIDE untuk AI Prompting

**CRIDE** adalah framework untuk menulis prompt yang efektif ke AI tools:

| Komponen | Penjelasan | Contoh |
|----------|-----------|--------|
| **C** — Context | Berikan konteks proyek dan teknologi | "Saya membangun API perpustakaan dengan Flask + SQLAlchemy" |
| **R** — Role | Tentukan peran AI | "Bertindak sebagai senior Python developer" |
| **I** — Instructions | Tugas spesifik yang diminta | "Buatkan endpoint untuk fitur notifikasi keterlambatan" |
| **D** — Details | Spesifikasi teknis dan constraints | "Gunakan Blueprint, return JSON, sertakan error handling" |
| **E** — Examples | Contoh output yang diinginkan | "Format response mirip endpoint GET /api/buku yang sudah ada" |

```
Prompt BURUK:                       Prompt BAIK (CRIDE):
============                        ====================

"Buatkan kode notifikasi"          "Context: Aplikasi perpustakaan Flask +
                                    SQLAlchemy. Model: Buku, User, Peminjaman.
(Terlalu vague, AI tidak            Role: Bertindak sebagai Python developer.
 tahu konteks, teknologi,           Instructions: Buatkan endpoint API untuk
 atau format yang diinginkan)       notifikasi keterlambatan pengembalian buku.
                                    Details: GET /api/peminjaman/overdue, return
                                    JSON, Flask Blueprint, error handling.
                                    Examples: Format mirip endpoint GET /api/buku."
```

> **Referensi teori:** Lihat modul IF2205 Minggu 13 — AI-Augmented Software Engineering untuk pembahasan mendalam tentang AI tools landscape, prompt engineering, dan responsible AI usage.

## Persiapan

- Akses ke AI tool: Claude (claude.ai), ChatGPT (chatgpt.com), atau GitHub Copilot
- Proyek tim sudah ter-deploy (Lab 12)
- Siapkan template AI Usage Log (tersedia di langkah terakhir)
- Buka proyek di GitHub Codespaces

## Langkah-langkah

### Langkah 1: AI untuk Code Generation dengan CRIDE (25 menit)

**Mengapa langkah ini penting?** Kemampuan menulis prompt yang efektif adalah skill kunci di era AI. Prompt yang baik menghasilkan kode yang lebih akurat dan mengurangi waktu modifikasi.

Pilih salah satu fitur baru untuk proyek Perpustakaan Digital UAI. Gunakan AI untuk generate kode.

**Worked Example 1 — Requirements ke Code:**

Prompt (menggunakan CRIDE):
```
Context: Saya membangun aplikasi Perpustakaan Digital UAI dengan Flask + SQLAlchemy.
Model yang sudah ada:
- Buku (id, judul, pengarang, tahun, isbn, stok)
- User (id, username, email, password_hash)
- Peminjaman (id, user_id, buku_id, tanggal_pinjam, tanggal_kembali, status)

Role: Bertindak sebagai senior Python/Flask developer.

Instructions: Buatkan endpoint API untuk fitur notifikasi keterlambatan pengembalian buku.
- GET /api/peminjaman/overdue — daftar peminjaman yang melewati batas waktu (14 hari)
- POST /api/notifikasi/send — kirim reminder ke user yang terlambat

Details:
- Gunakan Flask Blueprint
- Return JSON dengan format konsisten: {"data": [...], "count": N}
- Sertakan error handling dan docstring
- Batas waktu peminjaman: 14 hari dari tanggal_pinjam
- Hanya user terautentikasi yang bisa akses

Examples: Format response mirip endpoint GET /api/buku yang sudah ada.
```

**Evaluasi output AI (isi tabel ini):**

| Kriteria | Skor (1-5) | Catatan |
|----------|-----------|---------|
| Correctness — apakah kode benar secara logic? | | |
| Completeness — apakah semua requirement terpenuhi? | | |
| Security — ada vulnerability (SQL injection, auth bypass)? | | |
| Code style — sesuai coding standards tim (PEP 8)? | | |
| Testability — apakah fungsi mudah di-unit-test? | | |

**Modifikasi yang diperlukan (catat):**
1. ___
2. ___
3. ___

**Worked Example 2 — Refactoring Code:**

Prompt:
```
Context: Kode berikut adalah endpoint pencarian buku di Flask. Saya ingin memperbaikinya.

[paste kode search endpoint dari Lab 09]

Role: Bertindak sebagai code reviewer senior.

Instructions: Refactor kode ini untuk:
1. Menambah search by pengarang (selain judul)
2. Menambah pagination
3. Menambah sorting (by judul atau tahun)
4. Memastikan query aman dari SQL injection

Details: Gunakan SQLAlchemy query builder, bukan raw SQL.
```

### Langkah 2: AI untuk Test Generation (20 menit)

**Mengapa langkah ini penting?** AI sangat baik untuk generate test cases — termasuk edge cases yang mungkin tidak terpikirkan manusia. Tapi Anda harus mengevaluasi apakah test yang dihasilkan benar-benar berguna.

**Worked Example 3 — Code ke Test:**

Prompt:
```
Context: Endpoint Flask berikut menangani peminjaman overdue:

[paste kode dari Langkah 1]

Instructions: Buatkan pytest test yang komprehensif.

Details: Cover test cases berikut:
1. Happy path — ada 3 peminjaman, 1 overdue (> 14 hari)
2. Tidak ada peminjaman overdue (semua masih dalam batas waktu)
3. User tidak terautentikasi (expect 401)
4. Edge case — peminjaman tepat 14 hari (hari ke-14, belum overdue)
5. Edge case — peminjaman 15 hari (hari ke-15, sudah overdue)

Gunakan conftest.py fixtures (app, client) yang sudah ada.
Gunakan BukuFactory dan UserFactory dari tests/factories.py.
```

Jalankan test yang di-generate AI:
```bash
pytest tests/test_overdue.py -v
```

**Catat hasil:**

| Metrik | Nilai |
|--------|-------|
| Total test yang di-generate AI | ___ |
| Test yang langsung PASS tanpa modifikasi | ___ |
| Test yang perlu dimodifikasi | ___ |
| Test yang salah total (harus ditulis ulang) | ___ |
| Persentase akurasi AI | ___% |

> **Insight:** Biasanya AI menghasilkan ~60-80% test yang langsung PASS. Test yang gagal biasanya karena AI tidak tahu detail implementasi spesifik Anda (nama fixture, format response exact, dsb).

### Langkah 3: Manual vs AI Code Review — Perbandingan (20 menit)

**Mengapa langkah ini penting?** Code review adalah gatekeeper kualitas kode. Membandingkan review manual vs AI membantu Anda memahami kekuatan dan kelemahan masing-masing.

**Latihan: Review kode anggota tim**

**Bagian A — Review manual Anda sendiri (10 menit):**

Ambil kode dari anggota tim (satu file, misalnya satu route endpoint). Review berdasarkan checklist ini:

```markdown
## Manual Code Review Checklist
- [ ] Correctness: Apakah logic benar untuk semua skenario?
- [ ] Security: Ada SQL injection, XSS, atau hardcoded secrets?
- [ ] Error handling: Semua error ditangani? Pesan error informatif?
- [ ] Performance: Ada N+1 query? Loop tidak perlu?
- [ ] Readability: Naming baik? Komentar cukup? Fungsi tidak terlalu panjang?
- [ ] Testing: Apakah ada test untuk fungsi ini?
```

Catat temuan Anda: ___ (minimal 3 poin)

**Bagian B — Review oleh AI (10 menit):**

Prompt:
```
Review kode Python berikut dari aspek:
1. Correctness — apakah logic benar?
2. Security — ada SQL injection, XSS, atau vulnerability lain?
3. Performance — ada N+1 query atau bottleneck?
4. Readability — mudah dipahami? Naming convention baik?
5. Best practices — ikuti Flask/Python best practices?

Untuk setiap temuan, berikan severity (Critical/Major/Minor) dan saran perbaikan.

[paste kode anggota tim]
```

**Evaluasi rekomendasi AI:**

| No | Rekomendasi AI | Severity | Valid? | Diterapkan? | Alasan |
|----|---------------|----------|--------|-------------|--------|
| 1 | | | Ya/Tidak | Ya/Tidak | |
| 2 | | | Ya/Tidak | Ya/Tidak | |
| 3 | | | Ya/Tidak | Ya/Tidak | |
| 4 | | | Ya/Tidak | Ya/Tidak | |
| 5 | | | Ya/Tidak | Ya/Tidak | |

**Bagian C — Perbandingan (isi tabel ini):**

| Aspek | Review Manual | Review AI |
|-------|--------------|-----------|
| Temuan total | ___ | ___ |
| Temuan valid | ___ | ___ |
| Temuan yang overlap | ___ | ___ |
| Temuan unik (hanya ditemukan oleh) | ___ | ___ |
| Waktu yang diperlukan | ___ menit | ___ menit |
| Kekuatan utama | | |
| Kelemahan utama | | |

> **Insight umum:** AI baik menemukan pattern-level issues (naming, best practices, common vulnerabilities). Manusia lebih baik menemukan context-level issues (business logic error, arsitektur yang tidak cocok dengan requirements).

### Langkah 4: AI untuk Documentation (15 menit)

**Mengapa langkah ini penting?** Dokumentasi sering terabaikan karena developer lebih suka coding. AI bisa mempercepat pembuatan dokumentasi secara signifikan.

Prompt:
```
Context: Berikut adalah semua Flask route endpoints dari proyek Perpustakaan Digital UAI:

[paste semua Flask routes dari proyek]

Instructions: Buatkan API documentation dalam format Markdown.

Details — Format per endpoint:
- HTTP Method + URL
- Deskripsi singkat
- Request: headers, parameters/body (dengan contoh JSON)
- Response: sukses (200/201) + error (400/401/404), masing-masing dengan contoh JSON
- Authentication: required/not required

Tambahkan section "Getting Started" di awal dengan base URL dan authentication flow.
```

**Evaluasi dokumentasi AI:**
- Apakah semua endpoint tercakup? (cek jumlah endpoint di kode vs di dokumentasi)
- Apakah contoh request/response akurat? (coba jalankan contoh request via curl)
- Apakah status code dan error response sesuai implementasi?
- Apa yang perlu diedit atau ditambahkan?

**Contoh output yang diharapkan dari AI (ringkasan API docs):**
```markdown
## API Documentation — Perpustakaan Digital UAI

### Base URL
`https://your-app.up.railway.app`

### Authentication
POST `/api/auth/login` dengan body `{"username": "...", "password": "..."}`.
Response: `{"token": "JWT_TOKEN_HERE"}`.
Sertakan header `Authorization: Bearer JWT_TOKEN_HERE` untuk endpoint yang membutuhkan autentikasi.

### Endpoints

#### GET /api/buku
Daftar semua buku.
- Auth: Tidak diperlukan
- Query params: `page` (int), `per_page` (int), `q` (string, search)
- Response 200: `{"data": [{"id": 1, "judul": "...", ...}], "total": 15}`

#### POST /api/buku
Tambah buku baru.
- Auth: Diperlukan (admin)
- Body: `{"judul": "...", "pengarang": "...", "tahun": 2025}`
- Response 201: `{"id": 1, "judul": "...", ...}`
- Response 400: `{"error": "Judul wajib diisi"}`
```

### Langkah 5: Lengkapi AI Usage Log (20 menit)

**Mengapa langkah ini penting?** AI Usage Log bukan sekadar formalitas — ini adalah dokumentasi proses belajar Anda. Log yang jujur menunjukkan *amanah* (kejujuran akademik) dan membantu Anda memahami kapan AI benar-benar membantu vs kapan Anda perlu belajar sendiri.

**Contoh AI Usage Log yang Sudah Diisi:**

| No | Task | AI Tool | Prompt (ringkas) | Output Quality (1-5) | Modifikasi yang Diperlukan | Waktu Hemat |
|----|------|---------|------------------|----------------------|---------------------------|-------------|
| 1 | Code gen: endpoint overdue | Claude | CRIDE prompt untuk GET /api/peminjaman/overdue + POST /api/notifikasi/send | 4 | Perbaiki format response, tambah auth decorator, fix import yang salah | ~30 menit |
| 2 | Test gen: test overdue | Claude | Generate pytest test 5 cases untuk endpoint overdue | 3 | 3 dari 5 test PASS langsung. 2 test perlu fix fixture dan expected response format | ~20 menit |
| 3 | Code review | ChatGPT | Review kode routes/buku.py dari aspek security, performance, readability | 4 | 4 dari 5 rekomendasi valid. 1 rekomendasi (ganti ORM ke raw SQL) tidak sesuai arsitektur | ~15 menit |
| 4 | API documentation | Claude | Generate API docs dari semua routes | 3 | Beberapa response example tidak akurat, perlu fix status codes, tambah auth section | ~25 menit |

**Isi AI Usage Log Anda untuk seluruh sesi lab ini:**

| No | Task | AI Tool | Prompt (ringkas) | Output Quality (1-5) | Modifikasi yang Diperlukan | Waktu Hemat |
|----|------|---------|------------------|----------------------|---------------------------|-------------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |

**Refleksi Etis:**

1. Untuk task mana AI paling membantu? Mengapa?
2. Untuk task mana AI kurang akurat? Mengapa?
3. Apa yang Anda pelajari tentang bekerja dengan AI sebagai pair programmer?
4. Bagaimana prinsip **amanah** (kejujuran dan tanggung jawab) diterapkan saat menggunakan AI?
   - Apakah Anda memahami setiap baris kode yang di-generate AI?
   - Apakah Anda bisa menjelaskan kode tersebut tanpa bantuan AI?
   - Apakah Anda mencantumkan penggunaan AI di AI Usage Log secara jujur?
5. Jika Anda menjadi dosen, apa aturan penggunaan AI yang akan Anda terapkan di kelas?

## Troubleshooting Umum

| Masalah | Penyebab | Solusi |
|---------|----------|--------|
| AI menghasilkan kode dengan library yang tidak dipakai di proyek | Prompt kurang spesifik tentang tech stack | Tambahkan detail tech stack di bagian Context (CRIDE) |
| AI test gagal semua | AI tidak tahu struktur project Anda | Sertakan contoh test yang sudah ada sebagai referensi di prompt |
| AI code review terlalu generik | Prompt terlalu pendek | Minta review spesifik per aspek (security, performance, dsb) |
| Output AI berbeda setiap kali | AI bersifat non-deterministic | Gunakan temperature rendah jika tersedia, atau minta format output yang lebih strict |
| AI menyarankan deprecated library/pattern | Training data AI mungkin outdated | Selalu verifikasi rekomendasi AI dengan dokumentasi resmi terbaru |

## Tantangan Tambahan

1. **Basic:** Bandingkan output 2 AI tools berbeda (Claude vs ChatGPT) untuk task yang sama — mana yang lebih akurat untuk kode Python/Flask? Dokumentasikan perbandingannya
2. **Intermediate:** Gunakan AI untuk refactoring — ambil satu file yang paling "berantakan" di proyek Anda, minta AI untuk refactor, evaluasi hasilnya, dan terapkan perbaikan yang valid
3. **Advanced:** Coba prompt chaining — output dari task 1 (code gen) menjadi input task 2 (test gen), lalu output task 2 menjadi input task 3 (code review). Dokumentasikan bagaimana kualitas output berubah di setiap chain

## Checklist Penyelesaian

- [ ] AI-generated code untuk 1 fitur baru — dievaluasi dengan tabel kriteria (5 aspek)
- [ ] AI-generated tests — dievaluasi accuracy (berapa yang langsung PASS vs perlu modifikasi)
- [ ] Manual vs AI code review — perbandingan terdokumentasi dalam tabel
- [ ] AI-generated documentation — dievaluasi accuracy dan completeness
- [ ] AI Usage Log lengkap (4+ entries) dengan contoh prompt yang digunakan
- [ ] Refleksi etis tertulis (5 pertanyaan dijawab)
- [ ] Memahami framework CRIDE dan bisa menerapkannya
- [ ] Semua kode dan test sudah di-commit ke repository

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
