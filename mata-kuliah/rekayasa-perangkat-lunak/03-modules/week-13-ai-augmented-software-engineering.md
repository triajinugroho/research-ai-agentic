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
| **CPMK** | CPMK-7: Merancang dan membangun web app end-to-end dalam tim Agile/Scrum dengan AI sebagai co-developer secara bertanggung jawab |
| **Sub-CPMK** | Sub-CPMK-7.1: Memanfaatkan AI tools (Copilot, Claude Code, Cursor) untuk setiap fase SDLC secara bertanggung jawab (C5) |
| | Sub-CPMK-7.2: Menerapkan prompt engineering (CRIDE framework) untuk software engineering tasks (C3) |
| **Durasi** | 150 menit (3 x 50 menit) |
| **Metode** | Ceramah interaktif, hands-on AI pair programming, AI code review exercise |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Mengevaluasi** landscape AI tools untuk software engineering dan memilih tool yang tepat untuk setiap konteks (C5)
2. **Menganalisis** bagaimana AI dapat membantu di setiap fase SDLC: requirements, design, coding, testing, deployment (C4)
3. **Menerapkan** teknik prompt engineering CRIDE untuk mendapatkan output AI yang berkualitas tinggi (C3)
4. **Merancang** workflow agentic development menggunakan Claude Code atau Cursor (C6)
5. **Mengevaluasi** aspek etika dan tanggung jawab dalam penggunaan AI untuk software development (C5)
6. **Mendokumentasikan** penggunaan AI dalam AI Usage Log secara transparan dan jujur (C3)

---

## Materi Pembelajaran

### 13.1 AI Tools Landscape untuk Software Engineering

AI telah mengubah cara software engineer bekerja secara fundamental. Per 2025/2026, berikut peta tool AI yang relevan:

```
Evolusi AI dalam Software Engineering:
+------------+   +-----------+   +--------------+   +-------------+
| Autocomplete|-->| Chat-based|-->|  AI Agents    |-->|  Autonomous  |
| (Copilot   |   | (ChatGPT, |   | (Claude Code,|   |  SE (future) |
|  2021)     |   |  Claude   |   |  Cursor,     |   |              |
|            |   |  2022-23) |   |  Devin 2024) |   |              |
+------------+   +-----------+   +--------------+   +-------------+
   ASSIST          COLLABORATE      DELEGATE          (Belum siap)
   
Level interaksi dengan developer:
+-- Assist: AI suggest, developer decide
+-- Collaborate: AI diskusi, developer review
+-- Delegate: AI execute, developer supervise
+-- Autonomous: AI end-to-end (masih belum reliable)
```

#### Perbandingan AI Tools untuk SE

| Tool | Kategori | Kegunaan Utama | Kelebihan | Kekurangan |
|------|----------|----------------|-----------|------------|
| **GitHub Copilot** | Code Completion | Autocomplete kode real-time di IDE | Cepat, terintegrasi VS Code | Konteks terbatas, hanya per-file |
| **Claude Code** | Agentic Coding | AI agent: edit file, terminal, multi-file | Konteks besar (200K), agentic | Perlu terminal, learning curve |
| **Cursor** | AI IDE | IDE berbasis VS Code + AI built-in | UX baik, multi-model | Berbayar |
| **ChatGPT** | Chat-based | Diskusi arsitektur, debugging, review | Serbaguna, GPT-4 capable | Tidak bisa akses codebase langsung |
| **Claude.ai** | Chat-based | Analisis kode, review, reasoning | Reasoning kuat, jujur tentang keterbatasan | Tidak bisa edit file langsung |
| **CodeRabbit** | Code Review | Review PR otomatis di GitHub | Terintegrasi GitHub, spesifik | Hanya review, tidak code |
| **Windsurf** | Agentic IDE | IDE + AI agent dengan context flow | Konteks alur kerja | Baru, ekosistem terbatas |

```
Kapan menggunakan tool mana:
+---------------------+------------------------------+
| Kebutuhan           | Tool yang Tepat               |
+---------------------+------------------------------+
| Autocomplete cepat  | Copilot (inline suggestion)  |
| Diskusi arsitektur  | ChatGPT / Claude.ai          |
| Implementasi fitur  | Claude Code / Cursor          |
| Review PR           | CodeRabbit + manual review   |
| Generate test       | Copilot / Claude Code         |
| Debug error         | Claude.ai (paste error)      |
| Refactoring besar   | Claude Code (multi-file)     |
+---------------------+------------------------------+
```

#### Ketersediaan untuk Mahasiswa

| Tool | Akses Gratis? | Cara Akses |
|------|--------------|------------|
| **GitHub Copilot** | Ya (GitHub Student Pack) | github.com/education |
| **Claude.ai** | Ya (tier gratis) | claude.ai |
| **ChatGPT** | Ya (GPT-3.5 gratis, GPT-4 limited) | chat.openai.com |
| **Cursor** | Free tier (limited) | cursor.sh |
| **Claude Code** | Perlu API key | Via Anthropic API |

### 13.2 AI di Setiap Fase SDLC

AI bukan hanya untuk *coding* -- AI dapat membantu di **setiap fase** Software Development Life Cycle:

```
AI Across SDLC:
+-----------+    +---------+    +-----------+    +---------+    +--------+
|REQUIREMENTS|-->| DESIGN  |-->|CONSTRUCTION|-->| TESTING |-->| DEPLOY |
|            |    |         |    |           |    |         |    |        |
| AI bantu:  |    | AI bantu|    | AI bantu: |    | AI bantu|    | AI help|
| - Analisis |    | - Arch. |    | - Code gen|    | - Test  |    | - YAML |
|   user     |    |   saran |    | - Pair    |    |   gen   |    |   gen  |
|   story    |    | - UML   |    |   program |    | - Debug |    | - Cfg  |
| - Gap      |    |   draft |    | - Refactor|    | - Cover |    |   gen  |
|   detect   |    | - API   |    |           |    |   anal. |    |        |
+-----------+    +---------+    +-----------+    +---------+    +--------+
                                      |
                                      v
                               +-----------+
                               |MAINTENANCE|
                               | AI bantu: |
                               | - Code    |
                               |   smell   |
                               | - Tech    |
                               |   debt    |
                               | - Deps    |
                               |   audit   |
                               +-----------+
```

#### Contoh Prompt per Fase SDLC

**Fase 1: Requirements**

```python
# Prompt untuk analisis user stories
prompt_requirements = """
Analisis user stories berikut untuk sistem e-commerce UMKM:

1. "Sebagai pembeli, saya ingin mencari produk"
2. "Sebagai penjual, saya ingin mengelola stok"
3. "Sebagai admin, saya ingin melihat laporan"

Untuk setiap user story:
- Apakah sudah memenuhi format INVEST?
- Identifikasi yang ambigu atau tidak lengkap
- Sarankan acceptance criteria (Given-When-Then)
- Estimasi story points (Fibonacci: 1,2,3,5,8,13)
"""
```

**Fase 2: Design**

```python
# Prompt untuk saran arsitektur
prompt_design = """
Saya membangun aplikasi manajemen inventori untuk UMKM batik 
di Solo. Spesifikasi:
- 10-50 pengguna concurrent
- Backend: Python/Flask
- Frontend: HTML/CSS/JS (vanilla)
- Database: PostgreSQL
- Deploy: Railway

Sarankan:
1. Arsitektur yang cocok (MVC/layered/lainnya)
2. Database schema (ERD) untuk: produk, kategori, 
   transaksi, pengguna
3. REST API endpoints utama
4. Pertimbangan keamanan dasar
"""
```

**Fase 3: Construction**

```python
# Prompt untuk implementasi fitur
prompt_construction = """
Konteks: Aplikasi Flask e-commerce UMKM, SQLAlchemy ORM,
PostgreSQL. Model Product sudah ada.

Implementasikan endpoint REST API:
- GET /api/products (dengan pagination dan filter kategori)
- GET /api/products/<id>
- POST /api/products (validasi: nama wajib, harga > 0)
- PUT /api/products/<id>
- DELETE /api/products/<id>

Sertakan:
- Error handling yang konsisten
- Input validation
- Docstring Indonesia
- Unit test dengan pytest (minimal 5 test cases)
"""
```

**Fase 4: Testing**

```python
# Prompt untuk generate test cases
prompt_testing = """
Berikut fungsi yang perlu ditest:

def hitung_total_belanja(items, kode_voucher=None):
    subtotal = sum(i['harga'] * i['qty'] for i in items)
    diskon = 0
    if kode_voucher == "MERDEKA79":
        diskon = subtotal * 0.17  # Diskon 17 Agustus
    elif kode_voucher == "WELCOME10":
        diskon = min(subtotal * 0.10, 50000)  # Max 50rb
    total = subtotal - diskon
    ppn = total * 0.11
    return {"subtotal": subtotal, "diskon": diskon,
            "ppn": ppn, "total": total + ppn}

Generate unit test komprehensif menggunakan pytest:
- Test normal case (tanpa voucher)
- Test setiap voucher
- Test edge case (keranjang kosong, qty 0)
- Test boundary values (diskon pas di batas max)
- Gunakan parametrize untuk variasi input
"""
```

**Fase 5: Deployment & Maintenance**

```python
# Prompt untuk generate CI/CD config
prompt_deploy = """
Generate GitHub Actions workflow untuk:
- Python 3.11 Flask app
- Lint: flake8
- Test: pytest dengan coverage > 70%
- Build: Docker image
- Deploy: Railway (hanya branch main)

Include: caching, secrets management, status badge
"""

# Prompt untuk analisis technical debt
prompt_maintenance = """
Analisis kode berikut dan identifikasi:
1. Code smells (dengan severity level)
2. Technical debt items
3. Saran refactoring (prioritized)
4. Estimasi effort untuk setiap perbaikan

[paste kode yang akan dianalisis]
"""
```

### 13.3 Agentic Development -- AI sebagai Co-Developer

Agentic development adalah paradigma baru di mana AI **bukan hanya menjawab pertanyaan**, tetapi bisa:
- Membaca dan memahami codebase secara keseluruhan
- Mengedit multiple files secara terkoordinasi
- Menjalankan perintah terminal (test, build, deploy)
- Iterasi berdasarkan feedback (error -> fix -> test -> verify)

```
Perbandingan Paradigma Development:

Traditional Coding:
  Developer berpikir --> Developer menulis kode --> Developer test
  [100% effort developer]

AI-Assisted (Copilot):
  Developer berpikir --> AI suggest kode --> Developer review & edit
  --> Developer test
  [70% effort developer, 30% AI assist]

Agentic Development (Claude Code/Cursor):
  Developer describe intent --> AI agent menulis kode + test + fix
  --> Developer review final result --> Iterate jika perlu
  [30% effort developer (review), 70% AI execute]

PENTING: Developer tetap bertanggung jawab 100% atas hasil akhir!
```

#### Workflow Agentic Development

```
+----------------------------------------------+
| 1. Developer menjelaskan intent/tugas        |
|    "Buat fitur CRUD produk dengan validasi"  |
|                    |                          |
| 2. AI Agent:       v                          |
|    +-- Baca kode yang sudah ada               |
|    +-- Tulis kode baru (model, route, test)   |
|    +-- Jalankan test                          |
|    +-- Fix error jika ada                     |
|    +-- Present hasil untuk review             |
|                    |                          |
| 3. Developer:      v                          |
|    +-- Review setiap perubahan                |
|    +-- Minta revisi jika perlu                |
|    +-- Verifikasi test coverage               |
|    +-- Approve & merge                        |
+----------------------------------------------+
```

```python
# Contoh session agentic development -- simulasi alur kerja

class AgenticWorkflow:
    """Simulasi workflow agentic development."""
    
    def __init__(self, intent: str):
        self.intent = intent
        self.steps = []
        self.status = "planning"
    
    def plan(self) -> list:
        """AI membuat rencana implementasi."""
        self.steps = [
            "1. Analisis kode existing (models, routes)",
            "2. Buat model Product jika belum ada",
            "3. Implementasi CRUD routes dengan validasi",
            "4. Tulis unit test (min 8 test cases)",
            "5. Jalankan test, fix jika error",
            "6. Update dokumentasi API"
        ]
        self.status = "implementing"
        return self.steps
    
    def execute_step(self, step_num: int) -> dict:
        """AI menjalankan satu langkah."""
        return {
            "step": step_num,
            "action": self.steps[step_num - 1],
            "files_changed": ["src/models.py", "src/routes.py", 
                              "tests/test_api.py"],
            "tests_passed": True,
            "status": "completed"
        }
    
    def review_checkpoint(self) -> str:
        """Developer diminta review sebelum lanjut."""
        return (
            f"Intent: {self.intent}\n"
            f"Status: {self.status}\n"
            f"Files changed: 3\n"
            f"Tests: 8/8 passing\n"
            f"Coverage: 85%\n"
            f"\nApakah Anda ingin approve atau request revisi?"
        )

# Contoh penggunaan
workflow = AgenticWorkflow("Buat fitur CRUD produk UMKM")
plan = workflow.plan()
for step in plan:
    print(step)
print("\n" + workflow.review_checkpoint())
```

### 13.4 Prompt Engineering -- Framework CRIDE

CRIDE adalah framework untuk menulis prompt yang menghasilkan output AI berkualitas tinggi. Prompt yang baik = output yang baik.

```
Framework CRIDE:
+----------+--------------------------------------------+
| Elemen   | Deskripsi                                  |
+----------+--------------------------------------------+
| C-ontext | Berikan konteks proyek, teknologi, state   |
| R-ole    | Tetapkan peran/expertise untuk AI           |
| I-nstruct| Perintah yang jelas dan spesifik           |
| D-etails | Spesifikasi detail, constraint, format     |
| E-xamples| Berikan contoh input/output yang diharapkan|
+----------+--------------------------------------------+
```

#### Perbandingan: Prompt Buruk vs Prompt CRIDE

```
PROMPT BURUK:
"Buatkan API untuk toko online"

Masalah: Tidak ada konteks, tidak spesifik, tidak ada constraint

PROMPT CRIDE (BAIK):
[C] Saya mengembangkan API e-commerce UMKM Indonesia 
    menggunakan Flask + SQLAlchemy. Database PostgreSQL.
    Saat ini sudah ada model Product dan endpoint GET.

[R] Kamu adalah senior Python backend developer yang 
    berpengalaman dengan REST API design dan security.

[I] Tambahkan endpoint PUT /api/products/{id} untuk 
    mengupdate produk yang sudah ada.

[D] - Validasi: nama (wajib, max 100 char), harga 
      (wajib, > 0), stok (wajib, >= 0)
    - Return 404 jika produk tidak ditemukan
    - Return 400 jika validasi gagal dengan pesan jelas
    - Ikuti pattern yang sudah ada di endpoint GET
    - Tambahkan unit test menggunakan pytest
    - Gunakan Bahasa Indonesia untuk docstring

[E] Request: PUT /api/products/1
    Body: {"nama": "Batik Tulis Solo", "harga": 350000}
    Response 200: {"id": 1, "nama": "Batik Tulis Solo", ...}
    Response 404: {"error": "Produk tidak ditemukan"}
```

#### Contoh CRIDE untuk Berbagai Tugas SE

```python
# CRIDE untuk Code Review
prompt_review = """
[Context] PR #42 di proyek Flask e-commerce UMKM. 
Perubahan: 3 file, 150 baris tambahan. Fitur: endpoint 
checkout dengan integrasi pembayaran Midtrans.

[Role] Kamu adalah senior code reviewer yang fokus pada 
security, performance, dan maintainability.

[Instruction] Review kode berikut dan berikan feedback 
terstruktur.

[Details]
- Fokus: SQL injection, input validation, error handling
- Format: severity (critical/major/minor/suggestion)
- Sertakan contoh kode perbaikan untuk setiap issue
- Perhatikan compliance PCI-DSS untuk data pembayaran

[Examples]
Format feedback:
- [CRITICAL] Baris 45: SQL injection vulnerability
  Sebelum: f"SELECT * FROM users WHERE id = {user_id}"
  Sesudah: db.session.execute(text("SELECT ..."), {"id": id})
"""
```

```python
# CRIDE untuk Generate Documentation
prompt_docs = """
[Context] Aplikasi Toko UMKM (Flask + PostgreSQL). 
API sudah lengkap: 12 endpoints, autentikasi JWT.

[Role] Kamu adalah technical writer yang menulis 
dokumentasi API untuk developer Indonesia.

[Instruction] Generate dokumentasi API dalam format 
Markdown untuk endpoint berikut:
POST /api/auth/login
POST /api/auth/register
GET /api/products
POST /api/orders

[Details]
- Bahasa: Indonesia (istilah teknis bilingual)
- Format: method, URL, headers, request body, response, 
  error codes
- Sertakan contoh curl command
- Tambahkan catatan keamanan di setiap endpoint

[Examples]
## POST /api/auth/login
**Deskripsi:** Autentikasi pengguna dan dapatkan JWT token.
**Request Body:**
{
  "email": "user@example.com", 
  "password": "s3cur3p@ss"
}
"""
```

#### Tips Prompt Engineering Lanjutan

| Teknik | Deskripsi | Contoh |
|--------|-----------|--------|
| **Chain of Thought** | Minta AI berpikir step-by-step | "Pikirkan langkah-langkah, lalu implementasi" |
| **Few-Shot** | Berikan 2-3 contoh output yang diinginkan | "Contoh 1: ... Contoh 2: ... Sekarang buatkan..." |
| **Negative Examples** | Tunjukkan apa yang TIDAK diinginkan | "Jangan gunakan global variables" |
| **Iterative Refinement** | Perbaiki prompt berdasarkan output | "Output tadi kurang X, tambahkan Y" |
| **Constraint Setting** | Batasi scope output | "Maksimal 50 baris, gunakan hanya stdlib" |

### 13.5 Responsible AI Usage

```
Spectrum Penggunaan AI:
+-------+----------+-----------+----------+--------+
| BAIK  |          |           |          | BURUK  |
+-------+----------+-----------+----------+--------+
| AI    | AI bantu | AI draft, | AI       | Copy-  |
| bantu | debug &  | developer | generate | paste  |
| cari  | explain  | review &  | semua,   | tanpa  |
| ref.  | error    | modify    | tidak    | review |
|       |          |           | review   |        |
+-------+----------+-----------+----------+--------+
 TOOL    ASSISTANT   PARTNER    SHORTCUT   CHEATING
```

#### Prinsip Penggunaan AI yang Bertanggung Jawab

| # | Prinsip | Penjelasan | Contoh |
|---|---------|------------|--------|
| 1 | **Verifikasi selalu** | Jangan percaya output AI tanpa review | Jalankan test, baca kode line by line |
| 2 | **Pahami kode** | Kamu bertanggung jawab atas kode yang di-submit | Bisa jelaskan di demo/interview |
| 3 | **Transparansi** | Catat penggunaan AI di AI Usage Log | Log setiap interaksi signifikan |
| 4 | **Jangan blind copy** | AI bisa generate kode bermasalah | Cek security, license, performance |
| 5 | **AI = partner** | Skill fundamental tetap harus dikuasai | Bisa coding tanpa AI juga |
| 6 | **Bias awareness** | AI punya bias dari training data | Review output untuk fairness |

#### Kapan AI TIDAK Boleh Digunakan

```
TIDAK BOLEH menggunakan AI untuk:
+-- UTS dan UAS (closed-book, tanpa AI)
+-- Kuis K1, K2, K3 (closed-book)
+-- Mengklaim kode AI sebagai karya sendiri tanpa log
+-- Bypass code review ("AI sudah generate, pasti benar")

WAJIB menggunakan AI Usage Log untuk:
+-- Tugas T1-T6 (documented AI usage)
+-- Proyek akhir (10% rubrik = AI Usage Log)
+-- Lab praktikum (documented)
```

#### AI Hallucination dan Cara Mengatasinya

```python
# AI bisa "berhalusinasi" -- generate kode yang terlihat benar tapi salah

# Contoh hallucination: AI menyarankan library yang tidak ada
# "Gunakan flask-autovalidate untuk validasi otomatis"
# --> Library ini TIDAK ADA! AI mengarangnya

# Cara mengatasi:
# 1. Selalu verifikasi library di PyPI (pypi.org) atau npmjs.com
# 2. Baca dokumentasi resmi, bukan hanya output AI
# 3. Jalankan test untuk memverifikasi kode AI
# 4. Cross-check dengan sumber kedua

# Contoh lain: AI generate kode yang "terlihat benar" tapi buggy
# AI output:
def is_palindrome_bad(text):
    return text == text[::-1]  # Bug: case-sensitive!

# Masalah: "Racecar" bukan palindrome menurut kode ini
# Seharusnya:
def is_palindrome(text: str) -> bool:
    """Cek apakah text adalah palindrome (case-insensitive)."""
    cleaned = text.lower().strip()
    return cleaned == cleaned[::-1]

# SELALU test output AI
assert is_palindrome("Racecar") == True
assert is_palindrome("hello") == False
assert is_palindrome("  Kasur Rusak  ") == True
```

```python
# Contoh AI hallucination dalam konteks Indonesia
# AI mungkin menyarankan:
# "Gunakan library pajak_indonesia untuk menghitung PPN"
# --> Library ini TIDAK ADA

# Solusi: tulis sendiri logika bisnis Indonesia
TARIF_PPN = 0.11  # PPN Indonesia per 2025

def hitung_ppn(harga_dasar: float) -> dict:
    """Hitung PPN 11% sesuai regulasi Indonesia."""
    ppn = harga_dasar * TARIF_PPN
    return {
        "harga_dasar": harga_dasar,
        "ppn": ppn,
        "total": harga_dasar + ppn,
        "keterangan": f"PPN {TARIF_PPN*100:.0f}% berdasarkan UU HPP"
    }

print(hitung_ppn(100_000))
# {'harga_dasar': 100000, 'ppn': 11000.0, 'total': 111000.0, ...}
```

### 13.6 AI Usage Log

Setiap mahasiswa **wajib** mencatat penggunaan AI dalam proyek sebagai bentuk transparansi akademik:

```markdown
## AI Usage Log -- [Nama Mahasiswa]
### Proyek: Toko UMKM Online

| # | Tanggal | Tool | Fase SDLC | Tugas | Prompt (ringkas) | Hasil | Modifikasi | Waktu Hemat |
|---|---------|------|-----------|-------|-----------------|-------|------------|-------------|
| 1 | 15/4/26 | Claude | Testing | Generate test | "Buat pytest untuk checkout" | 8 test cases | Fix 2 assertions | ~30 menit |
| 2 | 16/4/26 | Copilot | Code | Autocomplete | (inline) | Route handler | + error handling | ~15 menit |
| 3 | 17/4/26 | ChatGPT | Design | Arsitektur | "Sarankan arsitektur..." | ERD + API | Sesuaikan req | ~45 menit |
| 4 | 18/4/26 | Claude Code | Code | Fitur baru | "Implementasi search" | 3 file baru | Fix 1 bug | ~60 menit |

### Refleksi:
- AI paling membantu untuk: generate boilerplate code dan test cases
- AI kurang baik untuk: keputusan arsitektur (butuh pemahaman bisnis)
- Yang saya pelajari: pentingnya prompt yang spesifik (CRIDE)
```

```python
# Script untuk generate AI Usage Log template
from datetime import datetime

def generate_ai_log_template(nama_mahasiswa: str, nama_proyek: str) -> str:
    """Generate template AI Usage Log dalam format Markdown."""
    template = f"""# AI Usage Log

**Mahasiswa:** {nama_mahasiswa}
**Proyek:** {nama_proyek}
**Periode:** Sprint 1-4 ({datetime.now().strftime('%B %Y')})

## Log Penggunaan AI

| # | Tanggal | Tool | Fase SDLC | Tugas | Prompt | Hasil | Modifikasi | Waktu |
|---|---------|------|-----------|-------|--------|-------|------------|-------|
| 1 | | | | | | | | |

## Statistik Penggunaan
- Total interaksi AI: ___
- Tool paling sering: ___
- Fase SDLC paling terbantu: ___
- Estimasi total waktu dihemat: ___ jam

## Refleksi
- AI paling membantu untuk: ___
- AI kurang baik untuk: ___
- Yang saya pelajari: ___
- Komitmen etika: Saya bertanggung jawab penuh atas semua
  kode yang saya submit, termasuk yang dibantu oleh AI.
"""
    return template

# Generate template
log = generate_ai_log_template("Ahmad Fauzi", "Toko Batik Online")
print(log)
```

> **Nilai Islami -- Amanah dan Kejujuran:** Mencatat penggunaan AI adalah bentuk amanah akademik. Islam mengajarkan bahwa kejujuran (*shidq*) adalah fondasi karakter yang baik. Rasulullah SAW bersabda: "Sesungguhnya kejujuran itu menunjukkan kepada kebaikan" (HR. Bukhari-Muslim). Mengklaim kode AI sebagai karya sendiri tanpa transparansi adalah bentuk ketidakjujuran yang bertentangan dengan prinsip ini. Sebaliknya, mendokumentasikan penggunaan AI dengan jujur menunjukkan integritas dan profesionalisme -- kualitas yang dihargai baik dalam Islam maupun di dunia industri.

---

## Kegiatan Pembelajaran

### Pre-class (20 menit)

- Buat akun Claude.ai (gratis) jika belum punya: [claude.ai](https://claude.ai)
- Pastikan GitHub Copilot tersedia di Codespaces (free untuk mahasiswa via GitHub Education Pack)
- Siapkan satu file kode dari proyek kelompok yang ingin di-review oleh AI
- Refleksi tertulis (3-5 kalimat): "Bagaimana AI mengubah profesi software engineer? Apakah SE akan digantikan AI?"

### In-class (110 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-20 menit | AI tools landscape, evolusi AI dalam SE, demo perbandingan tools | Ceramah + demo |
| 20-35 menit | AI di setiap fase SDLC, agentic development workflow | Ceramah + diskusi |
| 35-55 menit | Prompt engineering CRIDE -- teori, contoh, latihan menulis prompt | Ceramah + latihan |
| 55-60 menit | *Break* | -- |
| 60-85 menit | Hands-on AI pair programming: implementasi fitur baru di proyek menggunakan Claude/Copilot + catat AI Usage Log | Hands-on |
| 85-105 menit | AI code review exercise: gunakan AI untuk review PR teman, lalu evaluasi kualitas review AI vs manual | Exercise kelompok |
| 105-110 menit | Diskusi responsible AI usage, AI hallucination awareness, wrap-up | Diskusi kelas |

### Post-class (20 menit)

- Mulai isi AI Usage Log untuk semua interaksi AI dalam proyek (retroaktif + ke depan)
- Eksperimen: gunakan CRIDE framework untuk 3 tugas berbeda di proyek kelompok
- Kerjakan tugas T6 (AI-Augmented Code Review Report)
- Lanjutkan Sprint 3 proyek kelompok

---

## Latihan & Diskusi

### Soal 1 (C2 -- Memahami)
Jelaskan perbedaan antara AI-assisted development (Copilot) dan agentic development (Claude Code/Cursor). Dalam konteks proyek kelompok Anda (tim 3-4 orang, Flask + PostgreSQL), kapan sebaiknya menggunakan masing-masing?

### Soal 2 (C3 -- Menerapkan)
Tulis prompt menggunakan framework CRIDE untuk tugas berikut:
a) Generate unit test untuk fungsi `hitung_ongkir(berat, tujuan, metode)` yang menghitung ongkos kirim UMKM
b) Review kode endpoint POST /api/orders untuk menemukan security vulnerabilities
c) Refactor file `views.py` yang memiliki 500 baris menjadi modular

Jelaskan mengapa setiap elemen CRIDE penting dalam prompt Anda.

### Soal 3 (C4 -- Menganalisis)
AI code assistant Anda menyarankan kode berikut untuk autentikasi:

```python
@app.route("/login", methods=["POST"])
def login():
    user = User.query.filter_by(
        email=request.json["email"],
        password=request.json["password"]
    ).first()
    if user:
        return {"token": generate_token(user.id)}
    return {"error": "Invalid"}, 401
```

Analisis minimal 4 masalah keamanan dan fungsional dalam kode ini. Tulis versi yang diperbaiki. Bagaimana hal ini menunjukkan pentingnya "verify always"?

### Soal 4 (C5 -- Mengevaluasi)
Seorang mahasiswa menggunakan AI untuk menyelesaikan seluruh tugas T4 (testing) tanpa memahami kode yang di-generate. Saat ditanya di demo, dia tidak bisa menjelaskan mengapa test tertentu ditulis. Evaluasi dari perspektif: (a) etika akademik, (b) kebijakan AI IF2205, (c) dampak ke kompetensi profesional, (d) prinsip amanah dalam Islam.

### Soal 5 (C5 -- Mengevaluasi)
Bandingkan output dari dua prompt berikut untuk tugas yang sama:

**Prompt A:** "Buatkan API untuk produk"

**Prompt B:** "[Context] Flask + SQLAlchemy, PostgreSQL. [Role] Senior backend dev. [Instruction] Buat GET /api/products dengan pagination. [Details] Page size 10, filter kategori, sort harga. [Example] GET /api/products?page=1&kategori=batik"

Evaluasi perbedaan kualitas output dan jelaskan mengapa CRIDE menghasilkan output lebih baik.

---

## Penugasan

### T6 -- AI-Augmented Code Review Report

| Komponen | Detail |
|----------|--------|
| **Tipe** | Individual |
| **Bobot** | 2.5% dari nilai akhir |
| **Deadline** | Minggu 15 |
| **Deliverable** | Laporan markdown (min. 1500 kata) + AI Usage Log |
| **CPMK** | CPMK-7 |

**Instruksi:**
1. Pilih satu Pull Request dari proyek kelompok (min. 50 baris perubahan)
2. Lakukan **manual code review** -- catat temuan (minimal 5 item)
3. Gunakan **AI tool** (Claude/ChatGPT) dengan prompt CRIDE untuk review PR yang sama
4. **Bandingkan** hasil review manual vs AI:
   - Apa yang ditemukan AI tapi terlewat oleh Anda?
   - Apa yang Anda temukan tapi AI tidak mendeteksi?
   - Kualitas saran perbaikan: mana yang lebih actionable?
5. Sertakan AI Usage Log lengkap, screenshot PR, dan analisis kritis
6. **Kesimpulan:** Kapan AI review efektif dan kapan masih butuh human judgment?

**Kriteria Penilaian:**

| Kriteria | Bobot |
|----------|-------|
| Kualitas manual review (depth, specificity) | 25% |
| Kualitas prompt CRIDE untuk AI review | 20% |
| Analisis perbandingan manual vs AI (insight) | 25% |
| AI Usage Log lengkap dan jujur | 15% |
| Kesimpulan dan refleksi kritis | 15% |

---

## Referensi

1. GitHub Copilot documentation. [docs.github.com/copilot](https://docs.github.com/en/copilot)
2. Anthropic. (2025). *Claude Code documentation*. [docs.anthropic.com](https://docs.anthropic.com/)
3. Zhang, T. et al. (2023). "A Survey on Large Language Models for Software Engineering." arXiv.
4. Fan, A. et al. (2023). "Large Language Models for Software Engineering: Survey and Open Problems." arXiv.
5. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering*, 9th ed. Chapter 30.
6. Cursor documentation. [cursor.sh](https://cursor.sh/)
7. Sommerville, I. (2016). *Software Engineering*, 10th ed. Pearson. Chapter 23.
8. ACM Code of Ethics and Professional Conduct. [acm.org/code-of-ethics](https://www.acm.org/code-of-ethics)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
