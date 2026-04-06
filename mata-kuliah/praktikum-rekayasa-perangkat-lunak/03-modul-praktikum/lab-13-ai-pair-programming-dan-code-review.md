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

## Tujuan

1. **Menggunakan** AI (Claude/Copilot) sebagai pair programmer untuk fitur baru
2. **Mengevaluasi** kualitas kode yang dihasilkan AI secara kritis
3. **Melakukan** AI-assisted code review pada kode tim
4. **Mendokumentasikan** penggunaan AI dalam AI Usage Log

## Persiapan

- Akses ke AI tool (Claude, ChatGPT, atau GitHub Copilot)
- Proyek tim sudah ter-deploy (Lab 12)
- Siapkan template AI Usage Log

## Langkah-langkah

### Langkah 1: AI untuk Code Generation (25 menit)

Pilih salah satu fitur baru untuk proyek tim. Gunakan AI untuk generate kode:

**Contoh Prompt:**
```
Konteks: Saya membangun aplikasi perpustakaan kampus dengan Flask + SQLAlchemy.
Model yang sudah ada: Buku (judul, pengarang, tahun, isbn), User (username, email),
Peminjaman (user_id, buku_id, tanggal_pinjam, tanggal_kembali, status).

Task: Buatkan endpoint API untuk fitur notifikasi keterlambatan pengembalian buku.
- GET /api/peminjaman/overdue — daftar peminjaman yang melewati batas waktu (14 hari)
- POST /api/notifikasi/send — kirim reminder ke user yang terlambat
- Gunakan Flask Blueprint, return JSON
- Sertakan error handling dan docstring
```

**Evaluasi output AI:**

| Kriteria | Skor (1-5) | Catatan |
|----------|-----------|---------|
| Correctness — apakah kode benar? | | |
| Completeness — apakah semua requirement terpenuhi? | | |
| Security — ada vulnerability? | | |
| Code style — sesuai coding standards tim? | | |
| Testability — mudah di-test? | | |

**Modifikasi yang diperlukan:**
1. ___ (catat apa yang perlu diubah)
2. ___
3. ___

### Langkah 2: AI untuk Test Generation (20 menit)

Gunakan AI untuk generate test:

```
Buatkan pytest test untuk endpoint berikut:
[paste kode dari Langkah 1]

Cover test cases:
1. Happy path — ada peminjaman overdue
2. Tidak ada peminjaman overdue
3. User tidak terautentikasi
4. Edge case — peminjaman tepat 14 hari (batas)
```

Jalankan test yang di-generate AI:
```bash
pytest tests/test_overdue.py -v
```

Catat: berapa test yang langsung PASS tanpa modifikasi?

### Langkah 3: AI-Assisted Code Review (20 menit)

Ambil kode dari anggota tim, minta AI melakukan review:

```
Review kode Python berikut dari aspek:
1. Correctness — apakah logic benar?
2. Security — ada SQL injection, XSS, atau vulnerability lain?
3. Performance — ada N+1 query atau bottleneck?
4. Readability — mudah dipahami? Naming convention baik?
5. Best practices — ikuti Flask/Python best practices?

[paste kode anggota tim]
```

**Evaluasi rekomendasi AI:**

| No | Rekomendasi AI | Valid? | Diterapkan? | Alasan |
|----|---------------|--------|-------------|--------|
| 1 | | Ya/Tidak | Ya/Tidak | |
| 2 | | Ya/Tidak | Ya/Tidak | |
| 3 | | Ya/Tidak | Ya/Tidak | |
| 4 | | Ya/Tidak | Ya/Tidak | |
| 5 | | Ya/Tidak | Ya/Tidak | |

### Langkah 4: AI untuk Documentation (15 menit)

Gunakan AI untuk generate API documentation:

```
Buatkan API documentation dalam format Markdown untuk endpoint berikut:
[paste semua Flask routes dari proyek]

Format per endpoint:
- HTTP Method + URL
- Deskripsi
- Request parameters/body (dengan contoh)
- Response (sukses + error, dengan contoh JSON)
- Authentication requirement
```

Evaluasi: apakah dokumentasi akurat? Apa yang perlu diedit?

### Langkah 5: Lengkapi AI Usage Log (20 menit)

Isi AI Usage Log untuk seluruh sesi:

| No | Task | AI Tool | Prompt (ringkas) | Output Quality (1-5) | Modifikasi yang Diperlukan | Waktu Hemat (estimasi) |
|----|------|---------|------------------|----------------------|---------------------------|------------------------|
| 1 | Code gen | | | | | |
| 2 | Test gen | | | | | |
| 3 | Code review | | | | | |
| 4 | Documentation | | | | | |

**Refleksi:**
1. Untuk task mana AI paling membantu? Mengapa?
2. Untuk task mana AI kurang akurat? Mengapa?
3. Apa yang Anda pelajari tentang bekerja dengan AI?
4. Bagaimana prinsip amanah (kejujuran) diterapkan saat menggunakan AI?

## Tantangan Tambahan

1. Bandingkan output 2 AI tools berbeda (Claude vs ChatGPT) untuk task yang sama
2. Gunakan AI untuk refactoring — minta perbaikan kode yang sudah ada
3. Coba prompt chaining: output dari task 1 menjadi input task 2

## Checklist Penyelesaian

- [ ] AI-generated code untuk 1 fitur baru — dievaluasi dan dimodifikasi
- [ ] AI-generated tests — dievaluasi accuracy (berapa yang langsung pass?)
- [ ] AI code review — dievaluasi relevance (berapa rekomendasi yang valid?)
- [ ] AI-generated documentation — dievaluasi accuracy
- [ ] AI Usage Log lengkap (4+ entries)
- [ ] Refleksi tertulis tentang penggunaan AI
- [ ] Semua kode dan test sudah di-commit ke repository

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
