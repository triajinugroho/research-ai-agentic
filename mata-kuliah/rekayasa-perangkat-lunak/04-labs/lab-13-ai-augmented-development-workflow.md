# Lab 13: AI-Augmented Development Workflow

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 12 dari 13 (Minggu 13) |
| **Topik** | AI Tools for Development, Prompt Engineering, AI Usage Log |
| **CPMK** | CPMK-7 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |

## Tujuan

1. **Menggunakan** AI (Claude/Copilot) untuk code generation, testing, review, dan dokumentasi
2. **Mengevaluasi** output AI secara kritis
3. **Mendokumentasikan** penggunaan AI dalam AI Usage Log

## Langkah-langkah

### Langkah 1: AI untuk Code Generation (20 menit)
Gunakan AI untuk generate fitur baru:
```
Prompt: "Buatkan Flask API endpoint untuk fitur perpanjangan peminjaman buku.
Endpoint: PATCH /api/peminjaman/<id>/extend
Rules: Hanya bisa diperpanjang 1x, maksimal 7 hari tambahan.
Gunakan SQLAlchemy, return JSON."
```
Evaluasi: Apakah kode benar? Apa yang perlu dimodifikasi?

### Langkah 2: AI untuk Test Generation (20 menit)
```
Prompt: "Buatkan pytest unit tests untuk endpoint perpanjangan peminjaman.
Cover: happy path, sudah pernah diperpanjang, peminjaman tidak ditemukan."
```
Jalankan tests — berapa yang pass tanpa modifikasi?

### Langkah 3: AI untuk Code Review (20 menit)
```
Prompt: "Review kode berikut dari sisi: correctness, security, performance, readability.
[paste kode dari proyek Anda]"
```
Catat: rekomendasi mana yang valid vs tidak relevan?

### Langkah 4: AI untuk Documentation (15 menit)
```
Prompt: "Buatkan API documentation (Markdown) untuk endpoint berikut:
[paste Flask routes]"
```

### Langkah 5: Isi AI Usage Log (15 menit)

| No | Task | Tool | Prompt (ringkas) | Output | Evaluasi | Modifikasi |
|----|------|------|------------------|--------|----------|------------|
| 1 | Code gen | Claude | "Buat endpoint extend..." | Endpoint code | 4/5 benar | Fix validation |
| 2 | Test gen | Claude | "Buat pytest untuk..." | 3 tests | 2/3 pass | Fix mock |
| 3 | Review | Claude | "Review kode ini..." | 5 suggestions | 3/5 valid | Applied 3 |
| 4 | Docs | Claude | "Buat API docs..." | MD docs | Accurate | Minor edit |

## Tantangan Tambahan

1. Bandingkan output Claude vs ChatGPT untuk task yang sama
2. Coba AI untuk debugging — berikan error message dan minta solusi

## Checklist Penyelesaian

- [ ] AI-generated code untuk 1 fitur baru
- [ ] AI-generated tests (evaluasi accuracy)
- [ ] AI code review (evaluasi relevance)
- [ ] AI-generated documentation
- [ ] AI Usage Log lengkap (4+ entries)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
