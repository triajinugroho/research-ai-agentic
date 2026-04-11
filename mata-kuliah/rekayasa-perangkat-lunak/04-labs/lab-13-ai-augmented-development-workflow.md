# Lab 13: AI-Augmented Development Workflow

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 12 dari 13 (Minggu 13) |
| **Topik** | AI Tools untuk Development, Prompt Engineering (CRIDE), AI Code Review, AI Usage Log |
| **CPMK** | CPMK-7 (Merancang dan membangun web application secara end-to-end, memanfaatkan AI sebagai co-developer secara bertanggung jawab) |
| **Sub-CPMK** | Sub-CPMK-7.1, Sub-CPMK-7.2 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces + AI Tools (GitHub Copilot, Claude, ChatGPT) |
| **Prasyarat** | Lab 01-11 selesai, modul Minggu 13, akses ke minimal 1 AI tool |

---

## Tujuan

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. **Menerapkan** (C3) AI tools (Copilot/Claude/ChatGPT) untuk code generation, testing, dan review
2. **Mengevaluasi** (C5) kualitas output AI secara kritis — membedakan output yang valid dari yang salah/berbahaya
3. **Menerapkan** (C3) framework CRIDE untuk prompt engineering yang efektif
4. **Mendokumentasikan** (C3) penggunaan AI secara transparan dalam AI Usage Log

---

## Konsep Singkat

### AI sebagai Co-developer, Bukan Pengganti

AI tools seperti GitHub Copilot, Claude, dan ChatGPT telah mengubah cara software engineer bekerja. Namun, AI adalah **asisten**, bukan pengganti pikiran kritis manusia. AI bisa menghasilkan kode yang terlihat benar tapi secara logika salah, tidak aman, atau tidak sesuai konteks.

```
Peran AI vs Manusia dalam Development:

  AI Bisa:                          Manusia Tetap Harus:
  ┌─────────────────────────┐       ┌──────────────────────────┐
  │ Generate boilerplate    │       │ Memahami requirements    │
  │ Suggest code completion │       │ Mendesain arsitektur     │
  │ Explain error messages  │       │ Mengevaluasi output AI   │
  │ Generate test cases     │       │ Memikirkan edge cases    │
  │ Refactor suggestions    │       │ Memutuskan trade-offs    │
  │ Draft documentation     │       │ Menjamin keamanan        │
  │ Translate kode          │       │ Bertanggung jawab atas   │
  └─────────────────────────┘       │ kode yang di-deploy      │
                                    └──────────────────────────┘
```

### Framework CRIDE untuk Prompt Engineering

CRIDE adalah kerangka kerja untuk membuat prompt yang efektif:

| Komponen | Deskripsi | Contoh |
|----------|-----------|--------|
| **C** — Context | Berikan konteks proyek dan teknologi | "Saya mengembangkan sistem perpustakaan dengan Flask dan SQLAlchemy" |
| **R** — Role | Tentukan peran AI | "Bertindaklah sebagai senior Python developer" |
| **I** — Instruction | Perintah yang spesifik | "Buatkan endpoint REST API untuk perpanjangan peminjaman" |
| **D** — Details | Detail teknis dan constraint | "Gunakan Flask Blueprint, return JSON, handle error 400/404" |
| **E** — Examples | Berikan contoh input/output | "Contoh response sukses: {id: 1, status: 'diperpanjang'}" |

### Kapan AI Membantu vs Menyesatkan?

```
AI BAGUS untuk:                    AI RAWAN SALAH di:
┌─────────────────────────┐       ┌──────────────────────────┐
│ Boilerplate code        │       │ Logika bisnis yang unik  │
│ Standard patterns       │       │ Konteks spesifik proyek  │
│ Syntax yang terlupa     │       │ Security-critical code   │
│ Test case generation    │       │ Angka/fakta/referensi    │
│ Refactoring suggestions │       │ Kode yang sangat baru    │
│ Error explanation       │       │ Arsitektur keseluruhan   │
└─────────────────────────┘       └──────────────────────────┘
```

> **Referensi:** Materi lengkap tersedia di modul Minggu 13 (`week-13`) dan Bab 13 Buku Ajar.

---

## Persiapan

| Kebutuhan | Detail |
|-----------|--------|
| Repository | Repository proyek tim (dari Lab 01-11) |
| AI Tools | Minimal 1: GitHub Copilot (gratis via Student Pack), Claude (claude.ai), atau ChatGPT |
| Codespace | Aktif dengan Python, Flask, pytest terinstal |
| Template AI Usage Log | Sudah familiar dari modul sebelumnya |

---

## Langkah-langkah

### Langkah 1: Setup dan Eksplorasi AI Tools (10 menit)

**Mengapa:** Sebelum menggunakan AI secara efektif, mahasiswa perlu memahami kemampuan dan batasan masing-masing tool.

**Instruksi:**

Pastikan Anda memiliki akses ke minimal 1 AI tool:

```
AI Tools yang Bisa Digunakan:

  ┌─────────────────────────────────────────────────────────┐
  │ Tool              │ Cara Akses           │ Kelebihan    │
  ├─────────────────────────────────────────────────────────┤
  │ GitHub Copilot    │ VS Code extension    │ Inline code  │
  │                   │ (gratis via Student  │ completion,  │
  │                   │  Developer Pack)     │ IDE-native   │
  ├─────────────────────────────────────────────────────────┤
  │ Claude (Anthropic)│ claude.ai            │ Analisis     │
  │                   │ claude.ai/code       │ panjang,     │
  │                   │                      │ reasoning    │
  ├─────────────────────────────────────────────────────────┤
  │ ChatGPT (OpenAI)  │ chat.openai.com      │ General      │
  │                   │                      │ purpose,     │
  │                   │                      │ widely known │
  └─────────────────────────────────────────────────────────┘
```

**Aktivitas pemanasan (5 menit):** Coba prompt sederhana berikut di AI tool pilihan Anda:

```
Jelaskan perbedaan antara Flask Blueprint dan Django App dalam 3 kalimat.
Gunakan bahasa Indonesia.
```

Evaluasi: Apakah jawabannya akurat? Apakah ada hal yang terlewat?

**Estimasi waktu:** 10 menit

---

### Langkah 2: AI untuk Requirements Brainstorming dengan CRIDE (15 menit)

**Mengapa:** AI bisa membantu brainstorming requirements dan user stories lebih cepat, terutama untuk mengidentifikasi skenario yang mungkin terlewat oleh manusia.

**Instruksi:**

Gunakan framework **CRIDE** untuk membuat prompt brainstorming. Coba prompt berikut:

```
[CRIDE Prompt untuk Requirements]

Context: Saya sedang mengembangkan Sistem Perpustakaan Digital untuk
Universitas Al Azhar Indonesia menggunakan Flask + SQLAlchemy + SQLite.
Pengguna utama: mahasiswa (meminjam buku) dan pustakawan (mengelola katalog).

Role: Bertindaklah sebagai Business Analyst yang berpengalaman dalam
sistem informasi perpustakaan di Indonesia.

Instruction: Identifikasi 5 user stories yang mungkin TERLEWAT dari
fitur dasar CRUD peminjaman buku. Fokus pada edge cases dan skenario
yang sering dilupakan developer.

Details:
- Format: "As a [role], I want [feature], so that [benefit]"
- Sertakan Acceptance Criteria dalam format Given-When-Then
- Pertimbangkan konteks perpustakaan universitas Indonesia

Example:
As a mahasiswa, I want melihat riwayat peminjaman saya,
so that saya bisa melacak buku yang pernah saya pinjam.
Given: mahasiswa sudah login
When: mahasiswa membuka halaman /riwayat
Then: sistem menampilkan daftar peminjaman (judul, tanggal, status)
```

**Aktivitas:**
1. Salin prompt di atas ke AI tool
2. Baca output AI — evaluasi setiap user story: apakah realistis? Apakah bisa diimplementasikan?
3. Pilih 2-3 user stories terbaik dari output AI
4. Modifikasi jika perlu (AI mungkin terlalu generik atau terlalu ambisius)

**Expected Output** (contoh output AI yang mungkin muncul):

```
1. As a pustakawan, I want menerima notifikasi otomatis saat buku jatuh tempo,
   so that saya bisa mengirim reminder ke mahasiswa.
   Given: ada peminjaman yang jatuh tempo hari ini
   When: sistem menjalankan cron job harian
   Then: email dikirim ke mahasiswa terkait

2. As a mahasiswa, I want mereservasi buku yang stoknya habis,
   so that saya mendapat prioritas saat buku dikembalikan.
   Given: stok buku = 0
   When: mahasiswa klik "Reservasi"
   Then: mahasiswa masuk ke antrian reservasi

3. As a pustakawan, I want melihat laporan buku paling populer per bulan,
   so that saya bisa merencanakan pengadaan buku baru.
```

**Diskusi (3 menit):**
- Apakah ada user story dari AI yang terlalu ambisius untuk proyek ini?
- Apakah AI bisa menggantikan proses interview stakeholder? Mengapa/mengapa tidak?

**Estimasi waktu:** 15 menit

---

### Langkah 3: AI untuk Code Generation (20 menit)

**Mengapa:** Code generation adalah use case AI yang paling umum. Namun, kode yang dihasilkan AI **tidak selalu benar** — mahasiswa harus mampu mengevaluasi, memodifikasi, dan memastikan kode bekerja sesuai spesifikasi.

**Instruksi:**

Gunakan CRIDE prompt berikut untuk generate fitur baru:

```
[CRIDE Prompt untuk Code Generation]

Context: Sistem Perpustakaan Digital UAI, Flask + SQLAlchemy, Python 3.x.
Model Peminjaman sudah ada dengan atribut: id, user_id, buku_id,
tanggal_pinjam, tanggal_jatuh_tempo, status ('dipinjam'/'dikembalikan').

Role: Bertindaklah sebagai senior Flask developer.

Instruction: Buatkan Flask endpoint untuk fitur perpanjangan peminjaman buku.

Details:
- Endpoint: PATCH /api/peminjaman/<id>/extend
- Rules: Hanya bisa diperpanjang 1x (tambah kolom extended: bool)
- Perpanjangan menambah 7 hari dari tanggal_jatuh_tempo
- Hanya peminjaman aktif (status='dipinjam') yang bisa diperpanjang
- Return JSON response
- Handle error: 404 (tidak ditemukan), 400 (sudah diperpanjang / sudah dikembalikan)

Example response sukses:
{
    "status": "success",
    "data": {
        "id": 5,
        "tanggal_jatuh_tempo": "2026-05-02",
        "extended": true
    }
}
```

**Aktivitas:**
1. Kirim prompt ke AI tool
2. Salin output AI ke file baru (jangan langsung paste ke proyek)
3. **Evaluasi kritis** — jawab pertanyaan berikut:

```
Checklist Evaluasi Output AI:

□ Apakah kode bisa berjalan tanpa error syntax?
□ Apakah semua edge cases ditangani (not found, already extended, dll)?
□ Apakah ada security issue (SQL injection, unauthorized access)?
□ Apakah kode mengikuti pattern yang sudah ada di proyek kita (MVC)?
□ Apakah variable naming konsisten dengan konvensi proyek?
□ Apakah response format konsisten dengan endpoint lain?
□ Apakah ada import yang kurang?
□ Apakah transaction database ditangani dengan benar (commit/rollback)?
```

4. Modifikasi kode AI jika ada yang perlu diperbaiki
5. Test kode yang sudah dimodifikasi

**Contoh evaluasi (output AI vs yang perlu diubah):**

```python
# OUTPUT AI (mungkin seperti ini):
@bp.route('/api/peminjaman/<int:id>/extend', methods=['PATCH'])
def extend_peminjaman(id):
    peminjaman = Peminjaman.query.get(id)        # AI biasanya benar
    if not peminjaman:
        return jsonify({"error": "Not found"}), 404
    # ... dst

# YANG PERLU DIEVALUASI:
# 1. Apakah ada @login_required? (AI sering lupa auth)
# 2. Apakah user yang request = user yang meminjam? (authorization)
# 3. Apakah ada db.session.commit()? (AI kadang lupa)
# 4. Apakah pesan error dalam bahasa Indonesia? (konsistensi proyek)
```

**Catat hasil evaluasi untuk AI Usage Log di Langkah 6.**

**Estimasi waktu:** 20 menit

---

### Langkah 4: AI untuk Code Review — Manual vs AI (15 menit)

**Mengapa:** Membandingkan hasil review manusia dengan review AI membantu memahami kekuatan dan kelemahan masing-masing. AI bagus untuk mendeteksi pattern, tapi manusia lebih baik memahami konteks bisnis.

**Instruksi:**

Ambil kode dari proyek Anda (atau dari refactoring di Lab 07) dan minta AI untuk mereview:

```
[CRIDE Prompt untuk Code Review]

Context: Kode ini adalah bagian dari Sistem Perpustakaan UAI (Flask + SQLAlchemy).

Role: Bertindaklah sebagai senior developer yang melakukan code review.

Instruction: Review kode berikut dari 5 aspek:
1. Correctness — apakah logika benar?
2. Security — ada vulnerability?
3. Performance — ada bottleneck?
4. Readability — mudah dipahami?
5. Best Practices — mengikuti Python/Flask conventions?

Details: Berikan rating 1-5 per aspek dan suggestion spesifik.

[PASTE KODE ANDA DI SINI]
```

**Aktivitas:**
1. Pilih satu modul/file dari proyek tim (50-100 baris)
2. Review sendiri dulu (manual, 5 menit) — catat temuanmu
3. Minta AI review (kirim prompt + kode, 3 menit)
4. Bandingkan temuan manual vs AI:

```
Perbandingan Review Manual vs AI:

| Aspek            | Review Manual (Anda)    | Review AI              |
|------------------|-------------------------|------------------------|
| Correctness      | (temuan Anda)           | (temuan AI)            |
| Security         | (temuan Anda)           | (temuan AI)            |
| Performance      | (temuan Anda)           | (temuan AI)            |
| Readability      | (temuan Anda)           | (temuan AI)            |
| Temuan unik      | (yang tidak ditemukan AI)| (yang tidak Anda temukan)|
| Rekomendasi valid| X dari Y                | X dari Y               |
```

**Diskusi (5 menit):**
- Temuan apa yang HANYA ditemukan oleh manusia? (biasanya: konteks bisnis, arsitektur, naming convention proyek)
- Temuan apa yang HANYA ditemukan oleh AI? (biasanya: edge case, security pattern, library-specific issues)
- Apakah AI bisa menggantikan human code review sepenuhnya? (Jawab: Tidak — AI bagus sebagai *first pass*, tapi keputusan tetap di tangan manusia)

**Estimasi waktu:** 15 menit

---

### Langkah 5: AI untuk Test Generation (15 menit)

**Mengapa:** AI bisa generate test cases dengan cepat, termasuk edge cases yang mungkin tidak terpikirkan. Namun, test yang dihasilkan AI perlu diverifikasi — AI kadang membuat test yang selalu pass (useless) atau test yang asumsinya salah.

**Instruksi:**

Gunakan prompt berikut untuk generate test:

```
[CRIDE Prompt untuk Test Generation]

Context: Flask app dengan endpoint PATCH /api/peminjaman/<id>/extend.
Menggunakan pytest dan Flask test client. Model Peminjaman punya atribut:
id, user_id, buku_id, tanggal_jatuh_tempo, status, extended (bool).

Role: Bertindaklah sebagai QA engineer.

Instruction: Buatkan 5 pytest test cases untuk endpoint perpanjangan
peminjaman dengan coverage berikut:

Details:
1. Happy path: perpanjangan berhasil
2. Error: peminjaman tidak ditemukan (404)
3. Error: sudah pernah diperpanjang (400)
4. Error: peminjaman sudah dikembalikan (400)
5. Edge case: perpanjangan mengubah tanggal_jatuh_tempo tepat +7 hari

Example test format:
def test_extend_success(client, sample_peminjaman):
    resp = client.patch(f'/api/peminjaman/{sample_peminjaman.id}/extend')
    assert resp.status_code == 200
    assert resp.json['data']['extended'] == True
```

**Aktivitas:**
1. Kirim prompt ke AI
2. Salin test cases ke file `tests/test_extend.py`
3. Evaluasi setiap test:

```
Evaluasi Test dari AI:

| Test | Deskripsi | Bisa Run? | Asumsi Benar? | Perlu Modifikasi? |
|------|-----------|-----------|---------------|-------------------|
| 1    | Happy path| Ya/Tidak  | Ya/Tidak      | (detail)          |
| 2    | Not found | Ya/Tidak  | Ya/Tidak      | (detail)          |
| 3    | Already   | Ya/Tidak  | Ya/Tidak      | (detail)          |
| 4    | Returned  | Ya/Tidak  | Ya/Tidak      | (detail)          |
| 5    | +7 days   | Ya/Tidak  | Ya/Tidak      | (detail)          |
```

4. Jalankan test (setelah modifikasi): `python -m pytest tests/test_extend.py -v`
5. Catat: berapa test yang pass TANPA modifikasi? Berapa yang perlu diubah?

**Expected Output** (setelah modifikasi):

```
tests/test_extend.py::test_extend_success PASSED
tests/test_extend.py::test_extend_not_found PASSED
tests/test_extend.py::test_extend_already_extended PASSED
tests/test_extend.py::test_extend_already_returned PASSED
tests/test_extend.py::test_extend_adds_7_days PASSED

5 passed in 0.15s
```

**Estimasi waktu:** 15 menit

---

### Langkah 6: Mengisi AI Usage Log dan Refleksi (25 menit)

**Mengapa:** AI Usage Log adalah bagian integral dari integritas akademik dan refleksi pembelajaran. Mendokumentasikan penggunaan AI membantu mahasiswa memahami kapan AI membantu dan kapan justru menyesatkan.

**Instruksi:**

Isi AI Usage Log lengkap untuk semua aktivitas AI yang dilakukan hari ini:

```markdown
# AI Usage Log — Lab 13

Nama: _______________
NIM: _______________
Tanggal: _______________

## Log Penggunaan AI

| No | Task | AI Tool | Prompt (ringkas) | Output (ringkas) | Evaluasi (1-5) | Modifikasi yang Dilakukan |
|----|------|---------|------------------|------------------|-----------------|--------------------------|
| 1 | Requirements brainstorming | Claude/ChatGPT | CRIDE: identifikasi 5 user stories terlewat | 5 user stories + AC | 4/5 — 4 realistis, 1 terlalu ambisius | Hapus 1 story, ubah AC yang kurang spesifik |
| 2 | Code generation (extend endpoint) | Copilot/Claude | CRIDE: buat PATCH endpoint extend | Flask route + logic | 3/5 — lupa auth dan error bahasa | Tambah @login_required, ubah pesan ke Indonesia |
| 3 | Code review | Claude/ChatGPT | Review kode dari 5 aspek | Rating + 6 suggestions | 4/5 — 4 valid, 2 kurang relevan | Apply 4 suggestions, abaikan 2 |
| 4 | Test generation | Claude/ChatGPT | Buat 5 pytest test cases | 5 test functions | 3/5 — 3 langsung pass, 2 perlu fix mock | Fix fixture dan assertion 2 test |

## Ringkasan Statistik
- Total prompt: ___
- Output yang langsung bisa dipakai (tanpa modifikasi): ___ dari ___
- Output yang perlu modifikasi minor: ___ dari ___
- Output yang salah/tidak relevan: ___ dari ___

## Refleksi
```

**Pertanyaan refleksi (jawab di file yang sama):**

1. **Kekuatan AI:** Di task mana AI paling membantu? Mengapa?
2. **Kelemahan AI:** Di task mana AI paling mengecewakan? Apa yang salah?
3. **Efisiensi:** Apakah menggunakan AI membuat Anda lebih cepat? Berapa estimasi waktu yang dihemat?
4. **Risiko:** Apa yang bisa terjadi jika mahasiswa langsung copy-paste output AI tanpa evaluasi?
5. **Etika:** Menurut Anda, apakah menggunakan AI untuk tugas kuliah "curang"? Apa batasannya?
6. **Amanah:** Bagaimana prinsip *amanah* (kepercayaan) dalam Islam berkaitan dengan penggunaan AI secara jujur dan transparan?

**Diskusi kelas (5 menit):**
- Sharing: siapa yang menemukan output AI yang "terlihat benar tapi sebenarnya salah"? Contohnya?
- Bagaimana cara membangun skill mengevaluasi output AI? (Jawab: perlu pemahaman fundamental yang kuat — AI tidak bisa menggantikan pemahaman dasar)

Commit:

```bash
git add docs/ai-usage-log-lab13.md
git commit -m "docs: tambah AI Usage Log untuk Lab 13

- Dokumentasi 4+ penggunaan AI (brainstorm, code gen, review, test)
- Evaluasi kualitas output AI per task
- Refleksi kekuatan dan kelemahan AI"
git push origin main
```

**Estimasi waktu:** 25 menit

---

## Tantangan Tambahan

### Tantangan 1: Dasar
Bandingkan output **2 AI tools berbeda** (misal Claude vs ChatGPT) untuk task yang sama (code generation). Dokumentasikan perbedaan: mana yang lebih akurat? Mana yang lebih verbose? Mana yang lebih mengikuti best practices?

### Tantangan 2: Menengah
Gunakan AI untuk **debugging** — berikan error message dari proyek Anda ke AI dan minta solusi. Evaluasi apakah solusi AI langsung menyelesaikan masalah atau justru memperkenalkan masalah baru. Dokumentasikan minimal 3 sesi debugging.

### Tantangan 3: Lanjutan
Rancang **panduan penggunaan AI** untuk tim Anda (1 halaman). Tentukan: (1) task apa yang boleh menggunakan AI, (2) task apa yang harus dikerjakan manual, (3) bagaimana mendokumentasikan AI usage, (4) bagaimana mengevaluasi output. Simpan di `docs/ai-guidelines.md`.

---

## Refleksi & AI Usage Log

AI Usage Log sudah diisi di Langkah 6 di atas. Pastikan log Anda mencakup:

- Minimal **4 entries** (satu per langkah yang menggunakan AI)
- Evaluasi dengan rating 1-5 per entry
- Kolom "Modifikasi" yang menjelaskan apa yang Anda ubah dari output AI
- Refleksi personal tentang kekuatan dan kelemahan AI

---

## Checklist Penyelesaian

- [ ] Minimal 1 AI tool berhasil diakses dan dicoba
- [ ] Prompt CRIDE untuk requirements brainstorming dijalankan dan dievaluasi
- [ ] AI-generated code untuk 1 fitur baru (extend peminjaman), dievaluasi dengan checklist
- [ ] Perbandingan code review manual vs AI terdokumentasi
- [ ] AI-generated test cases (5 test), dievaluasi dan dimodifikasi
- [ ] AI Usage Log lengkap (4+ entries) dengan evaluasi per entry
- [ ] Refleksi personal tertulis (6 pertanyaan dijawab)
- [ ] Semua dokumentasi di-commit ke repository

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
