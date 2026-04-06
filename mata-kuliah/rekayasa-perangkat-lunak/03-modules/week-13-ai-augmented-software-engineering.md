# Minggu 13: AI-Augmented Software Engineering

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 13 dari 16 |
| **Topik** | AI-Augmented Software Engineering |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK-7: Merancang dan membangun web app end-to-end dalam tim Agile/Scrum dengan AI sebagai co-developer |
| **Sub-CPMK** | 13.1 Mengevaluasi berbagai AI tools dan perannya dalam setiap fase SDLC (C5) |
| | 13.2 Merancang workflow AI-augmented development yang efektif dan bertanggung jawab (C6) |
| | 13.3 Menerapkan prompt engineering (CRIDE) untuk mengoptimalkan output AI (C5) |
| **Durasi** | 150 menit (3 × 50 menit) |
| **Metode** | Ceramah interaktif, hands-on AI pair programming, AI code review exercise |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Mengevaluasi** landscape AI tools untuk software engineering dan memilih tool yang tepat untuk setiap konteks (C5)
2. **Menganalisis** bagaimana AI dapat membantu di setiap fase SDLC: requirements, design, coding, testing, deployment (C4)
3. **Menerapkan** teknik prompt engineering CRIDE untuk mendapatkan output AI yang berkualitas (C5)
4. **Merancang** workflow agentic development menggunakan Claude Code atau Cursor (C6)
5. **Mengevaluasi** aspek etika dan tanggung jawab dalam penggunaan AI untuk pengembangan software (C5)

---

## Materi Pembelajaran

### 13.1 AI Tools Landscape untuk Software Engineering

AI telah mengubah cara software engineer bekerja. Berikut peta tool yang relevan per 2025/2026:

| Kategori | Tool | Kegunaan Utama |
|----------|------|----------------|
| **Code Completion** | GitHub Copilot | Autocomplete kode real-time |
| **Agentic Coding** | Claude Code, Cursor, Windsurf | AI agent yang bisa mengedit file, jalankan terminal |
| **Chat-based** | ChatGPT, Claude.ai, Gemini | Diskusi arsitektur, debugging, code review |
| **Code Review** | CodeRabbit, Greptile | Review PR otomatis |
| **Testing** | Copilot, Claude | Generate test cases |
| **Documentation** | Mintlify, Claude | Generate docs dari kode |

```
Evolusi AI dalam Software Engineering:
┌──────────┐   ┌───────────┐   ┌──────────────┐   ┌─────────────┐
│ Autocomplete│→│ Chat-based│→│  AI Agents    │→│  Autonomous  │
│ (Copilot  │   │ (ChatGPT, │   │ (Claude Code,│   │  SE (future) │
│  2021)    │   │  Claude   │   │  Cursor,     │   │              │
│           │   │  2022-23) │   │  Devin 2024) │   │              │
└──────────┘   └───────────┘   └──────────────┘   └─────────────┘
  Assist          Collaborate      Delegate          (Belum siap)
```

### 13.2 AI di Setiap Fase SDLC

| Fase SDLC | Cara AI Membantu | Contoh Prompt |
|-----------|-----------------|---------------|
| **Requirements** | Analisis user story, identifikasi gap | "Analisis user stories ini dan identifikasi yang ambigu" |
| **Design** | Generate diagram, review arsitektur | "Sarankan arsitektur untuk e-commerce dengan 10K users" |
| **Construction** | Code generation, pair programming | "Implementasikan endpoint REST API untuk manajemen produk" |
| **Testing** | Generate test cases, review coverage | "Generate unit test komprehensif untuk fungsi ini" |
| **Deployment** | Generate Dockerfile, CI/CD config | "Buat GitHub Actions workflow untuk aplikasi Flask" |
| **Maintenance** | Detect code smells, suggest refactoring | "Analisis technical debt dalam file ini" |

### 13.3 Agentic Development — AI sebagai Co-Developer

Agentic development menggunakan AI agent yang dapat:
- Membaca dan memahami codebase secara keseluruhan
- Mengedit multiple files secara koordinasi
- Menjalankan perintah terminal (test, build, deploy)
- Iterasi berdasarkan feedback (error → fix → test → verify)

```
Traditional Coding:
  Developer berpikir → Developer menulis kode → Developer test

AI-Assisted (Copilot):
  Developer berpikir → AI suggest kode → Developer review & edit → Developer test

Agentic Development (Claude Code/Cursor):
  Developer describe intent → AI agent menulis kode + test + fix error
  → Developer review final result → Iterate jika perlu
```

#### Workflow Agentic Development

```
┌──────────────────────────────────────────────┐
│ 1. Developer menjelaskan intent/tugas        │
│    "Buat fitur CRUD produk dengan validasi"  │
│                    │                          │
│ 2. AI Agent:       ▼                          │
│    ├── Baca kode yang sudah ada               │
│    ├── Tulis kode baru (model, route, test)   │
│    ├── Jalankan test                          │
│    ├── Fix error jika ada                     │
│    └── Commit atau present hasil              │
│                    │                          │
│ 3. Developer:      ▼                          │
│    ├── Review perubahan                       │
│    ├── Minta revisi jika perlu                │
│    └── Approve & merge                        │
└──────────────────────────────────────────────┘
```

### 13.4 Prompt Engineering — Framework CRIDE

CRIDE adalah framework untuk menulis prompt yang menghasilkan output AI berkualitas tinggi:

| Elemen | Deskripsi | Contoh |
|--------|-----------|--------|
| **C** — Context | Berikan konteks proyek/kode | "Proyek Flask e-commerce, Python 3.11, PostgreSQL" |
| **R** — Role | Tetapkan peran untuk AI | "Kamu adalah senior backend developer" |
| **I** — Instruction | Perintah yang jelas dan spesifik | "Implementasikan endpoint PUT /api/products/{id}" |
| **D** — Details | Spesifikasi detail dan constraint | "Gunakan SQLAlchemy ORM, validasi input dengan Pydantic" |
| **E** — Examples | Berikan contoh input/output | "Contoh response: {'id': 1, 'nama': 'Batik', ...}" |

#### Contoh Prompt CRIDE Lengkap

```
[Context] Saya sedang mengembangkan API e-commerce UMKM Indonesia
menggunakan Flask + SQLAlchemy. Database PostgreSQL. Saat ini sudah
ada model Product dan endpoint GET /api/products.

[Role] Kamu adalah senior Python backend developer yang berpengalaman
dengan REST API design.

[Instruction] Tambahkan endpoint PUT /api/products/{id} untuk
mengupdate produk yang sudah ada.

[Details]
- Validasi: nama (wajib, max 100 char), harga (wajib, > 0),
  stok (wajib, >= 0)
- Return 404 jika produk tidak ditemukan
- Return 400 jika validasi gagal dengan pesan error yang jelas
- Ikuti pattern yang sudah ada di endpoint GET
- Tambahkan unit test menggunakan pytest

[Examples]
Request: PUT /api/products/1
Body: {"nama": "Batik Tulis Solo", "harga": 350000, "stok": 25}
Response 200: {"id": 1, "nama": "Batik Tulis Solo", ...}
Response 404: {"error": "Produk dengan id 1 tidak ditemukan"}
```

### 13.5 Responsible AI Usage

#### Prinsip Penggunaan AI yang Bertanggung Jawab

1. **Verifikasi selalu** — Jangan percaya output AI tanpa review
2. **Pahami kode yang di-generate** — Kamu bertanggung jawab atas kode yang kamu submit
3. **Transparansi** — Catat penggunaan AI di AI Usage Log
4. **Jangan copy-paste blindly** — AI bisa menghasilkan kode yang bermasalah dari segi keamanan, performa, atau lisensi
5. **AI sebagai partner, bukan pengganti** — Skill fundamental tetap harus dikuasai

#### AI Usage Log

Setiap mahasiswa wajib mencatat penggunaan AI dalam proyek:

```markdown
## AI Usage Log — [Nama Mahasiswa]

| Tanggal | Tool | Tugas | Prompt (ringkas) | Hasil | Modifikasi |
|---------|------|-------|-----------------|-------|------------|
| 15/4/26 | Claude | Generate test | "Buat unit test untuk..." | 8 test cases | Perbaiki 2 assertions |
| 16/4/26 | Copilot | Autocomplete | — (inline) | Route handler | Tambah error handling |
```

> **Nilai Islami — Amanah dan Kejujuran:** Mencatat penggunaan AI adalah bentuk amanah akademik. Islam mengajarkan bahwa kejujuran (*shidq*) adalah fondasi karakter yang baik. Mengklaim kode AI sebagai karya sendiri tanpa transparansi adalah bentuk ketidakjujuran.

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)

- Buat akun Claude.ai (gratis) jika belum punya
- Pastikan GitHub Copilot tersedia di Codespaces (free untuk mahasiswa)
- Refleksi: "Bagaimana AI mengubah profesi software engineer? Apakah SE akan digantikan AI?"

### In-class (120 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-20 menit | AI tools landscape, evolusi AI dalam SE | Ceramah + diskusi |
| 20-35 menit | AI di setiap fase SDLC, agentic development | Ceramah + demo |
| 35-55 menit | Prompt engineering CRIDE — teori dan contoh | Ceramah + latihan |
| 55-60 menit | *Break* | — |
| 60-90 menit | Hands-on AI pair programming: implementasi fitur baru di proyek menggunakan Claude/Copilot | Hands-on |
| 90-110 menit | AI code review exercise: gunakan AI untuk review PR teman, lalu evaluasi kualitas review AI | Exercise kelompok |
| 110-120 menit | Diskusi responsible AI usage, AI Usage Log, wrap-up | Diskusi kelas |

### Post-class (15 menit)

- Mulai isi AI Usage Log untuk semua interaksi AI dalam proyek
- Eksperimen: gunakan CRIDE framework untuk 3 tugas berbeda di proyek kelompok
- Kerjakan tugas T6

---

## Penugasan

### T6 — AI-Augmented Code Review Report

| Komponen | Detail |
|----------|--------|
| **Tipe** | Individual |
| **Deadline** | Minggu 15 |
| **Deliverable** | Laporan markdown (min. 1500 kata) |

**Instruksi:**
1. Pilih satu Pull Request dari proyek kelompok (min. 50 baris perubahan)
2. Lakukan **manual code review** terlebih dahulu — catat temuan
3. Gunakan **AI tool** (Claude/ChatGPT) untuk melakukan code review terhadap PR yang sama
4. **Bandingkan** hasil review manual vs AI — apa yang ditemukan AI tapi terlewat oleh kamu? Dan sebaliknya?
5. Sertakan AI Usage Log, prompt yang digunakan, dan analisis kritis terhadap kualitas review AI
6. Kesimpulan: kapan AI review efektif dan kapan masih butuh human judgment?

---

## Referensi

1. GitHub Copilot documentation. [docs.github.com/copilot](https://docs.github.com/en/copilot)
2. Anthropic. (2025). *Claude Code documentation*. [docs.anthropic.com](https://docs.anthropic.com/)
3. Zhang, T. et al. (2023). "A Survey on Large Language Models for Software Engineering." arXiv.
4. Fan, A. et al. (2023). "Large Language Models for Software Engineering: Survey and Open Problems." arXiv.
5. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering*, 9th ed. Chapter 30.
6. Cursor documentation. [cursor.sh](https://cursor.sh/)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
