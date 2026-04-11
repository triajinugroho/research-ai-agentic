# BAB 13: AI-AUGMENTED SOFTWARE ENGINEERING

**Oleh: Tri Aji Nugroho, S.T., M.T.**
**Mata Kuliah:** IF2205 Rekayasa Perangkat Lunak
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Semester:** Genap 2025/2026

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom | Estimasi Waktu |
|-----------|-----------|-------------|----------------|
| 7.1 | Mengevaluasi peran AI tools (GitHub Copilot, Claude Code, Cursor, ChatGPT) dalam setiap fase SDLC dan memilih tool yang tepat untuk setiap konteks | C5 (Mengevaluasi) | 75 menit |
| 7.2 | Menerapkan prompt engineering dengan CRIDE framework untuk software engineering tasks dan mengelola AI secara bertanggung jawab sesuai prinsip amanah | C3-C5 (Menerapkan-Mengevaluasi) | 75 menit |

**Setelah mempelajari bab ini, mahasiswa mampu:**

1. Memetakan lanskap AI tools untuk software engineering dan membandingkan fitur utamanya
2. Menunjukkan bagaimana AI dapat digunakan di setiap fase SDLC (requirements, design, construction, testing, deployment, maintenance)
3. Menerapkan CRIDE framework (Context, Role, Instructions, Details, Examples) untuk menulis prompt yang efektif
4. Menjelaskan konsep *agentic development* dan perbedaannya dengan AI code completion biasa
5. Mengidentifikasi keterbatasan AI (hallucination, outdated knowledge, security blind spots) dan strategi mitigasinya
6. Merancang AI pair programming workflow yang bertanggung jawab untuk tim development
7. Mendokumentasikan penggunaan AI dengan AI Usage Log yang jujur dan lengkap
8. Menerapkan prinsip amanah dan etika Islam dalam penggunaan AI untuk pengembangan perangkat lunak

---

## Peta Konsep Bab 13

```
                    ┌──────────────────────────────────────────┐
                    │     AI-AUGMENTED SOFTWARE ENGINEERING     │
                    └──────────────────┬───────────────────────┘
                                       │
        ┌──────────────┬───────────────┼───────────────┬───────────────┐
        │              │               │               │               │
        ▼              ▼               ▼               ▼               ▼
  ┌───────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌──────────────┐
  │ AI Tools  │ │ AI di      │ │ CRIDE      │ │ Agentic    │ │ Responsible  │
  │ Landscape │ │ Setiap     │ │ Framework  │ │ Development│ │ AI Usage     │
  │           │ │ Fase SDLC  │ │            │ │            │ │              │
  └─────┬─────┘ └─────┬──────┘ └─────┬──────┘ └─────┬──────┘ └──────┬───────┘
        │              │              │              │               │
  ┌─────┴─────┐  ┌─────┴──────┐ ┌────┴───────┐ ┌────┴──────┐ ┌─────┴───────┐
  │Copilot    │  │Requirements│ │Context     │ │Claude Code│ │AI Usage Log │
  │Claude Code│  │Design      │ │Role        │ │Agent Mode │ │Limitations  │
  │Cursor     │  │Code        │ │Instructions│ │Human-in   │ │Hallucination│
  │ChatGPT    │  │Test        │ │Details     │ │-the-Loop  │ │Etika Islam  │
  │CodeRabbit │  │Deploy      │ │Examples    │ │           │ │Amanah       │
  └───────────┘  │Maintain    │ └────────────┘ └───────────┘ └─────────────┘
                 └────────────┘
```

---

## 13.1 Lanskap AI Tools untuk Software Engineering (2025-2026)

### 13.1.1 Evolusi AI dalam Software Engineering

AI dalam pengembangan perangkat lunak telah berkembang pesat dalam 3 tahun terakhir:

```
Timeline AI untuk Software Engineering:

2021 │ GitHub Copilot (preview) — autocomplete berbasis AI pertama
     │ yang luas diadopsi developer
     │
2022 │ ChatGPT diluncurkan — mengubah cara developer bertanya
     │ dan belajar. Copilot GA (Generally Available)
     │
2023 │ GPT-4 + Claude + Gemini — model multimodal
     │ Copilot Chat, Cursor IDE, AI code review tools
     │
2024 │ Claude 3.5 Sonnet, Claude Code (CLI agent)
     │ Agentic development mulai mainstream
     │ Devin (AI software engineer), SWE-Agent
     │
2025 │ Claude Opus 4 + Claude Code mature
     │ AI pair programming menjadi standar industri
     │ MCP (Model Context Protocol) untuk integrasi tools
     │
2026 │ AI agent mengerjakan task kompleks secara otonom
     │ Human-in-the-loop sebagai quality gate
     │ AI Usage Policy wajib di setiap perusahaan
```

### 13.1.2 Kategori AI Tools

| Kategori | Tools | Fungsi Utama | Model Pricing |
|----------|-------|-------------|---------------|
| **Code Completion** | GitHub Copilot, Codeium, Tabnine | Autocomplete kode real-time di IDE | $10-19/bulan |
| **AI Chat + Code** | Claude (Anthropic), ChatGPT (OpenAI), Gemini (Google) | Diskusi, generate kode, explain code | Freemium |
| **AI-Native IDE** | Cursor, Windsurf, Zed | IDE dengan AI terintegrasi | $20/bulan |
| **Agentic Development** | Claude Code, Devin, SWE-Agent, Cline | AI mengerjakan task secara otonom (baca, tulis, execute) | Varies |
| **Code Review** | CodeRabbit, Sourcery, Codium PR-Agent | Review PR otomatis, suggest perbaikan | Freemium |
| **Testing** | Diffblue Cover, CodiumAI | Generate test otomatis dari kode | Varies |
| **Documentation** | Mintlify, README.ai, Swimm | Generate docs dari kode | Freemium |

### 13.1.3 Perbandingan Detail AI Tools Utama

```
┌────────────────────────────────────────────────────────────────────────┐
│                    PERBANDINGAN AI TOOLS UTAMA                         │
├───────────────┬──────────────┬──────────────┬────────────┬────────────┤
│ Fitur         │ GitHub       │ Claude Code  │ Cursor     │ ChatGPT    │
│               │ Copilot      │ (Anthropic)  │            │ (OpenAI)   │
├───────────────┼──────────────┼──────────────┼────────────┼────────────┤
│ Tipe          │ Code         │ CLI Agent    │ AI-Native  │ Chat +     │
│               │ Completion   │              │ IDE        │ Code Gen   │
├───────────────┼──────────────┼──────────────┼────────────┼────────────┤
│ Interface     │ VS Code      │ Terminal     │ VS Code    │ Web/API    │
│               │ extension    │ (CLI)        │ fork       │            │
├───────────────┼──────────────┼──────────────┼────────────┼────────────┤
│ Inline        │ ✅ Excellent │ ❌ No        │ ✅ Good    │ ❌ No      │
│ Autocomplete  │              │              │            │            │
├───────────────┼──────────────┼──────────────┼────────────┼────────────┤
│ Chat/Discuss  │ ✅ Copilot   │ ✅ Native    │ ✅ Native  │ ✅ Native  │
│               │ Chat         │              │            │            │
├───────────────┼──────────────┼──────────────┼────────────┼────────────┤
│ File Edit     │ Limited      │ ✅ Full      │ ✅ Full    │ ❌ Manual  │
│               │              │ (multi-file) │(multi-file)│ copy-paste │
├───────────────┼──────────────┼──────────────┼────────────┼────────────┤
│ Execute Code  │ ❌ No        │ ✅ Yes       │ Limited    │ ✅ Code    │
│               │              │ (terminal)   │            │ Interpreter│
├───────────────┼──────────────┼──────────────┼────────────┼────────────┤
│ Agentic Mode  │ ✅ Agent     │ ✅ Full      │ ✅ Composer│ ❌ No      │
│               │ (2025)       │ Agent        │            │            │
├───────────────┼──────────────┼──────────────┼────────────┼────────────┤
│ Codebase      │ ✅ Workspace │ ✅ Full      │ ✅ Full    │ ❌ Manual  │
│ Awareness     │              │ codebase     │ codebase   │ context    │
├───────────────┼──────────────┼──────────────┼────────────┼────────────┤
│ Best For      │ Daily coding │ Complex      │ Full-stack │ Learning,  │
│               │ productivity │ tasks,       │ development│ exploring  │
│               │              │ refactoring  │            │ concepts   │
├───────────────┼──────────────┼──────────────┼────────────┼────────────┤
│ Free Tier     │ ✅ Students  │ ✅ Limited   │ ✅ Limited │ ✅ GPT-4o  │
│               │ (via GitHub  │              │            │ mini       │
│               │ Education)   │              │            │            │
└───────────────┴──────────────┴──────────────┴────────────┴────────────┘
```

> **Rekomendasi untuk mahasiswa IF2205:**
> - **GitHub Copilot** untuk daily coding (gratis dengan GitHub Education)
> - **Claude Code** untuk task kompleks dan refactoring
> - **ChatGPT** untuk belajar konsep dan eksplorasi

---

## 13.2 AI di Setiap Fase SDLC

### 13.2.1 Overview: AI sebagai Co-Developer

AI tidak hanya berguna saat menulis kode. AI dapat membantu di **setiap fase** Software Development Life Cycle:

```
┌─────────────────────────────────────────────────────────────────────┐
│                   AI DI SETIAP FASE SDLC                            │
│                                                                      │
│  Requirements ──→ Design ──→ Code ──→ Test ──→ Deploy ──→ Maintain  │
│      🤖              🤖         🤖        🤖        🤖         🤖    │
│                                                                      │
│  AI membantu di SEMUA fase, tapi dengan cara yang berbeda:           │
│                                                                      │
│  Requirements : Analisis, generate user stories, validasi SRS       │
│  Design       : Suggest arsitektur, generate UML, review desain     │
│  Code         : Autocomplete, generate, refactor, explain           │
│  Test         : Generate test cases, edge cases, mutation testing   │
│  Deploy       : CI/CD config, Dockerfile, monitoring setup          │
│  Maintain     : Bug analysis, code explanation, refactoring legacy  │
└─────────────────────────────────────────────────────────────────────┘
```

### 13.2.2 AI untuk Requirements Engineering

```
┌──────────────────────────────────────────────────────────────┐
│  FASE: REQUIREMENTS ENGINEERING                               │
│                                                               │
│  Prompt 1: Generate User Stories                              │
│  ─────────────────────────────────                            │
│  "Saya membangun Sistem Antrian Puskesmas Online.            │
│  Stakeholder: pasien, petugas loket, dokter, admin.          │
│  Buatkan 10 user stories format:                              │
│  'Sebagai [role], saya ingin [action] agar [benefit]'        │
│  dengan acceptance criteria Given-When-Then untuk setiap      │
│  story. Prioritaskan dengan MoSCoW."                         │
│                                                               │
│  Prompt 2: Analisis SRS                                       │
│  ────────────────────────                                     │
│  "Review SRS berikut dari sisi completeness, consistency,     │
│  dan feasibility. Identifikasi requirements yang ambigu,      │
│  conflicting, atau missing. [paste SRS]"                      │
│                                                               │
│  Prompt 3: Non-Functional Requirements                        │
│  ────────────────────────────────────────                     │
│  "Untuk Sistem Antrian Puskesmas Online, identifikasi        │
│  10 non-functional requirements terkait: performance,         │
│  security, usability, reliability, dan scalability.           │
│  Format IEEE 830, dengan measurable criteria."                │
│                                                               │
│  ⚠️ SELALU validasi output AI dengan stakeholder asli!        │
└──────────────────────────────────────────────────────────────┘
```

### 13.2.3 AI untuk Design

```python
# Contoh prompt untuk generate class diagram (PlantUML)
prompt_design = """
Saya membangun Sistem Perpustakaan Online dengan Flask + SQLAlchemy.
Entitas utama: Buku, Anggota, Peminjaman, Kategori, Admin.

Buatkan:
1. Class Diagram dalam format PlantUML
2. Relasi antar class (association, composition, inheritance)
3. Atribut dan method untuk setiap class
4. Pastikan mengikuti prinsip SOLID

Constraints:
- Satu anggota bisa pinjam maks 3 buku
- Durasi peminjaman maks 14 hari
- Denda Rp 1.000/hari keterlambatan
"""

# AI Output (contoh):
plantuml_output = """
@startuml
class Buku {
  - id: int
  - judul: str
  - pengarang: str
  - isbn: str
  - tahun_terbit: int
  - stok: int
  - kategori_id: int
  + is_available(): bool
  + kurangi_stok(): void
  + tambah_stok(): void
}

class Anggota {
  - id: int
  - nama: str
  - nim: str
  - email: str
  - is_active: bool
  + jumlah_pinjaman_aktif(): int
  + bisa_pinjam(): bool
}

class Peminjaman {
  - id: int
  - anggota_id: int
  - buku_id: int
  - tgl_pinjam: date
  - tgl_jatuh_tempo: date
  - tgl_kembali: date
  - status: str
  + hitung_denda(): int
  + kembalikan(): void
  + is_terlambat(): bool
}

Buku "1" -- "0..*" Peminjaman
Anggota "1" -- "0..3" Peminjaman
@enduml
"""

# Evaluasi manusia: 
# ✅ Relasi benar (1-to-many)
# ✅ Constraint 3 buku tercermin
# ⚠️ Perlu tambahkan class Kategori
# ⚠️ Method hitung_denda() perlu detail formula
```

### 13.2.4 AI untuk Construction (Coding)

AI paling banyak digunakan dalam fase construction. Berikut skenario-skenario umum:

**Skenario 1: Generate Boilerplate Code**

```python
# Prompt: "Buatkan Flask app factory dengan SQLAlchemy, 
#          Blueprint, dan error handler untuk Sistem Perpustakaan"

# AI Output:
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name='development'):
    """Application factory pattern."""
    app = Flask(__name__)
    
    # Konfigurasi
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///perpustakaan.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'ganti-dengan-secret-yang-aman'
    
    # Inisialisasi extensions
    db.init_app(app)
    
    # Register Blueprints
    from app.routes.buku import buku_bp
    from app.routes.anggota import anggota_bp
    from app.routes.peminjaman import peminjaman_bp
    
    app.register_blueprint(buku_bp, url_prefix='/api/buku')
    app.register_blueprint(anggota_bp, url_prefix='/api/anggota')
    app.register_blueprint(peminjaman_bp, url_prefix='/api/peminjaman')
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Resource tidak ditemukan'}), 404
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'error': 'Request tidak valid'}), 400
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    return app

# Evaluasi manusia:
# ✅ Struktur benar (app factory pattern)
# ✅ Blueprint terpisah per resource
# ⚠️ SECRET_KEY harus dari environment variable
# ⚠️ Perlu tambah CORS jika frontend terpisah
```

**Skenario 2: Implementasi Fitur dari User Story**

```python
# Prompt: "Implementasi user story: 'Sebagai anggota, saya ingin 
#          mencari buku berdasarkan judul atau pengarang'
#          Acceptance criteria:
#          - Given: anggota di halaman katalog
#          - When: mengetik keyword di search box
#          - Then: ditampilkan daftar buku yang cocok (max 20)"

# AI Output:
from flask import Blueprint, request, jsonify
from app.models import Buku
from sqlalchemy import or_

buku_bp = Blueprint('buku', __name__)

@buku_bp.route('/search', methods=['GET'])
def search_buku():
    """Pencarian buku berdasarkan judul atau pengarang.
    
    Query Parameters:
        q (str): Keyword pencarian (minimal 2 karakter)
        page (int): Halaman (default: 1)
        per_page (int): Jumlah per halaman (default: 20, max: 50)
    
    Returns:
        JSON: Daftar buku yang cocok dengan pagination info
    """
    keyword = request.args.get('q', '').strip()
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 20, type=int), 50)
    
    # Validasi input
    if len(keyword) < 2:
        return jsonify({
            'error': 'Keyword minimal 2 karakter'
        }), 400
    
    # Query dengan LIKE (case-insensitive)
    search_filter = or_(
        Buku.judul.ilike(f'%{keyword}%'),
        Buku.pengarang.ilike(f'%{keyword}%')
    )
    
    # Pagination
    result = Buku.query.filter(search_filter)\
        .order_by(Buku.judul)\
        .paginate(page=page, per_page=per_page, error_out=False)
    
    return jsonify({
        'data': [buku.to_dict() for buku in result.items],
        'pagination': {
            'page': result.page,
            'per_page': result.per_page,
            'total': result.total,
            'pages': result.pages
        }
    })

# Evaluasi manusia:
# ✅ Implementasi sesuai acceptance criteria
# ✅ Input validation ada
# ✅ Pagination ada
# ⚠️ Perlu sanitize keyword untuk SQL injection (SQLAlchemy sudah handle)
# ⚠️ Pertimbangkan full-text search jika data besar
```

### 13.2.5 AI untuk Testing

```python
# Prompt: "Generate pytest unit tests untuk endpoint search_buku 
#          di atas. Cover: happy path, edge cases, error handling.
#          Gunakan fixtures dan parametrize."

# AI Output:
import pytest
from app import create_app, db
from app.models import Buku

@pytest.fixture
def app():
    """Buat app instance untuk testing."""
    app = create_app('testing')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        # Seed test data
        buku_data = [
            Buku(judul="Laskar Pelangi", pengarang="Andrea Hirata", 
                 isbn="978-1", tahun_terbit=2005, stok=5),
            Buku(judul="Bumi Manusia", pengarang="Pramoedya Ananta Toer",
                 isbn="978-2", tahun_terbit=1980, stok=3),
            Buku(judul="Filosofi Teras", pengarang="Henry Manampiring",
                 isbn="978-3", tahun_terbit=2018, stok=7),
            Buku(judul="Atomic Habits", pengarang="James Clear",
                 isbn="978-4", tahun_terbit=2018, stok=10),
        ]
        db.session.add_all(buku_data)
        db.session.commit()
        
        yield app
        
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

class TestSearchBuku:
    """Test suite untuk endpoint GET /api/buku/search"""
    
    # Happy path
    def test_search_by_judul(self, client):
        """Cari buku berdasarkan judul."""
        response = client.get('/api/buku/search?q=Laskar')
        assert response.status_code == 200
        data = response.get_json()
        assert len(data['data']) == 1
        assert data['data'][0]['judul'] == 'Laskar Pelangi'
    
    def test_search_by_pengarang(self, client):
        """Cari buku berdasarkan pengarang."""
        response = client.get('/api/buku/search?q=Pramoedya')
        assert response.status_code == 200
        data = response.get_json()
        assert len(data['data']) == 1
    
    def test_search_case_insensitive(self, client):
        """Search harus case-insensitive."""
        response = client.get('/api/buku/search?q=laskar')
        assert response.status_code == 200
        assert len(response.get_json()['data']) == 1
    
    def test_search_multiple_results(self, client):
        """Keyword yang cocok dengan banyak buku."""
        response = client.get('/api/buku/search?q=a')
        # "Laskar Pelangi", "Bumi Manusia", "Atomic Habits" 
        # semuanya mengandung 'a'
        assert response.status_code == 200
        assert len(response.get_json()['data']) >= 3
    
    # Edge cases
    def test_search_no_results(self, client):
        """Keyword yang tidak cocok dengan buku apapun."""
        response = client.get('/api/buku/search?q=xyzabc')
        assert response.status_code == 200
        assert len(response.get_json()['data']) == 0
    
    def test_search_keyword_too_short(self, client):
        """Keyword kurang dari 2 karakter harus error 400."""
        response = client.get('/api/buku/search?q=a')
        # Hmm, ini harusnya 400 tapi 'a' panjangnya 1
        # Fix: keyword minimal 2 karakter
        assert response.status_code == 400
    
    def test_search_empty_keyword(self, client):
        """Keyword kosong harus error 400."""
        response = client.get('/api/buku/search?q=')
        assert response.status_code == 400
    
    # Pagination
    def test_search_pagination(self, client):
        """Pastikan pagination info ada."""
        response = client.get('/api/buku/search?q=buku&page=1&per_page=2')
        data = response.get_json()
        assert 'pagination' in data
        assert data['pagination']['page'] == 1
        assert data['pagination']['per_page'] == 2

# Evaluasi manusia:
# ✅ Happy path tested (judul, pengarang, case-insensitive)
# ✅ Edge cases tested (no results, short keyword)
# ✅ Pagination tested
# ⚠️ test_search_multiple_results: assertion perlu disesuaikan 
#    (keyword 'a' 1 karakter, melanggar validasi min 2)
# ⚠️ Perlu test: special characters di keyword
# ⚠️ Perlu test: SQL injection attempt
```

### 13.2.6 AI untuk Deployment

```yaml
# Prompt: "Buatkan GitHub Actions CI/CD workflow untuk Flask app 
#          dengan pytest, flake8 linting, dan deploy ke Railway.
#          Python 3.11, SQLite."

# AI Output (.github/workflows/ci.yml):
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install flake8
      - run: flake8 app/ tests/ --max-line-length=120

  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pip install pytest pytest-cov
      - run: pytest tests/ -v --cov=app --cov-report=term-missing
      
  deploy:
    runs-on: ubuntu-latest
    needs: test
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to Railway
        uses: bervProject/railway-deploy@main
        with:
          railway_token: ${{ secrets.RAILWAY_TOKEN }}
          service: perpustakaan-app

# Evaluasi manusia:
# ✅ Lint → Test → Deploy flow benar
# ✅ Deploy hanya dari branch main
# ✅ Secrets digunakan untuk token
# ⚠️ Perlu cache pip dependencies untuk speed
# ⚠️ Perlu environment variables untuk test database
```

### 13.2.7 AI untuk Maintenance

```
Prompt untuk Debug:
"Error berikut muncul saat POST /api/peminjaman:

Traceback (most recent call last):
  File "app/routes/peminjaman.py", line 45, in create_peminjaman
    buku = Buku.query.get(data['buku_id'])
  ...
  AttributeError: 'NoneType' object has no attribute 'stok'

Request body: {"anggota_id": 1, "buku_id": 999}

Jelaskan penyebab error dan berikan fix yang proper dengan 
error handling yang baik."
```

```
Prompt untuk Refactoring Legacy Code:
"Refactor fungsi berikut yang memiliki code smells 
(long method, magic numbers, no error handling):

[paste kode legacy]

Terapkan:
1. Extract method
2. Replace magic numbers with constants
3. Proper error handling
4. Type hints
5. Docstrings
Jelaskan setiap perubahan yang kamu buat."
```

---

## 13.3 CRIDE Framework untuk Prompt Engineering

### 13.3.1 Apa Itu CRIDE?

CRIDE adalah framework untuk menulis prompt yang efektif dan menghasilkan output AI yang akurat. CRIDE memastikan AI mendapatkan informasi yang cukup untuk memberikan jawaban yang relevan.

```
┌──────────────────────────────────────────────────────────────────┐
│                      CRIDE FRAMEWORK                              │
│                                                                   │
│  C ─ Context     │ Berikan latar belakang: proyek, teknologi,    │
│                   │ posisi Anda, situasi saat ini                  │
│                   │                                                │
│  R ─ Role        │ Tentukan peran AI: "Kamu adalah senior Flask   │
│                   │ developer", "Kamu adalah QA engineer"          │
│                   │                                                │
│  I ─ Instructions│ Tugas spesifik: apa yang harus dilakukan AI    │
│                   │ "Buatkan...", "Review...", "Refactor..."       │
│                   │                                                │
│  D ─ Details     │ Constraint dan spesifikasi: format output,     │
│                   │ library yang digunakan, batasan                │
│                   │                                                │
│  E ─ Examples    │ Contoh input-output yang diharapkan (few-shot) │
│                   │ atau referensi kode yang sudah ada             │
│                                                                   │
│  Tidak semua elemen wajib — tapi semakin lengkap, semakin baik.  │
│  Minimal: Context + Instructions + Details                        │
└──────────────────────────────────────────────────────────────────┘
```

### 13.3.2 Worked Example 1: Generate API Endpoint

**Prompt (tanpa CRIDE):**
```
Buatkan API untuk pinjam buku.
```

**Prompt (dengan CRIDE):**
```
[C] Saya membangun Sistem Perpustakaan Online untuk proyek akhir 
    IF2205. Tech stack: Flask + SQLAlchemy + SQLite. Saat ini sudah 
    ada model Buku dan Anggota yang berjalan.

[R] Kamu adalah senior Flask developer yang berpengalaman dengan 
    RESTful API design.

[I] Buatkan API endpoint POST /api/peminjaman untuk proses 
    peminjaman buku. Endpoint harus:
    1. Menerima JSON body dengan anggota_id dan buku_id
    2. Validasi: anggota ada, buku ada, stok > 0, anggota belum 
       pinjam 3 buku
    3. Buat record peminjaman dengan tgl_jatuh_tempo = 14 hari
    4. Kurangi stok buku
    5. Return JSON response yang informatif

[D] - Gunakan Flask Blueprint (peminjaman_bp sudah ada)
    - Error handling: return JSON error message + HTTP status code
    - Jangan gunakan raw SQL, gunakan SQLAlchemy ORM
    - Ikuti PEP 8 dan tambahkan docstrings
    - Status peminjaman: 'aktif', 'dikembalikan', 'terlambat'

[E] Response sukses yang diharapkan:
    {
      "message": "Peminjaman berhasil",
      "data": {
        "id": 1,
        "anggota": "Ahmad",
        "buku": "Laskar Pelangi",
        "tgl_pinjam": "2026-04-01",
        "tgl_jatuh_tempo": "2026-04-15"
      }
    }
```

**Perbedaan output:**

| Aspek | Tanpa CRIDE | Dengan CRIDE |
|-------|-------------|--------------|
| Akurasi | ~40% sesuai kebutuhan | ~85% sesuai kebutuhan |
| Validasi | Mungkin tidak ada | Lengkap sesuai spec |
| Error handling | Basic atau tidak ada | Proper HTTP status codes |
| Kode style | Inconsistent | Sesuai PEP 8 + docstrings |
| Integrasi | Mungkin tidak cocok | Cocok dengan codebase |

### 13.3.3 Worked Example 2: Code Review

```
[C] Saya anggota tim 4 mahasiswa yang mengerjakan proyek akhir 
    Sistem Perpustakaan. Berikut adalah PR dari rekan tim saya 
    untuk fitur "kembalikan buku".

[R] Kamu adalah senior software engineer yang melakukan code review.

[I] Review kode berikut dari 5 aspek:
    1. Correctness: Apakah logika benar?
    2. Security: Apakah ada vulnerability?
    3. Performance: Apakah ada bottleneck?
    4. Readability: Apakah kode mudah dipahami?
    5. Test coverage: Apakah perlu test tambahan?

[D] Berikan feedback dalam format:
    - 🔴 MUST FIX: masalah kritis
    - 🟡 SHOULD FIX: improvement penting
    - 🟢 NICE TO HAVE: improvement opsional
    Sertakan contoh kode perbaikan untuk setiap feedback.

[E] [paste kode yang akan di-review]
```

### 13.3.4 Worked Example 3: Generate Documentation

```
[C] Proyek Flask Sistem Perpustakaan sudah memiliki 12 API 
    endpoints di folder app/routes/. Kami perlu API documentation 
    untuk sprint review dan submission proyek akhir.

[R] Kamu adalah technical writer yang paham REST API documentation.

[I] Buatkan API documentation lengkap dalam format Markdown untuk
    semua endpoints. Setiap endpoint harus mencakup:
    1. HTTP method + URL
    2. Deskripsi singkat
    3. Request parameters / body
    4. Response format (success + error)
    5. Contoh request (curl)
    6. Contoh response

[D] - Format: Markdown table untuk overview, detail per endpoint
    - Group by resource (Buku, Anggota, Peminjaman)
    - Include authentication requirements
    - Bahasa Indonesia untuk deskripsi, English untuk technical terms

[E] Contoh format yang diharapkan:
    ### POST /api/peminjaman
    **Deskripsi:** Membuat peminjaman buku baru
    **Auth:** Required (Bearer token)
    **Body:** `{"anggota_id": 1, "buku_id": 5}`
    **Response 201:** `{"message": "Peminjaman berhasil", ...}`
    **Response 400:** `{"error": "Stok buku habis"}`
```

### 13.3.5 Worked Example 4: Debugging dengan CRIDE

```
[C] Proyek Flask Sistem Perpustakaan, Python 3.11, SQLAlchemy 2.0,
    SQLite. Fitur peminjaman buku sudah berjalan kemarin, 
    tapi tiba-tiba error hari ini setelah merge PR #15.

[R] Kamu adalah debugging expert yang berpengalaman menyelesaikan 
    production issues.

[I] Diagnosa error berikut dan berikan:
    1. Root cause analysis
    2. Langkah-langkah fix
    3. Preventive measures agar tidak terulang

[D] Error traceback:
    IntegrityError: UNIQUE constraint failed: peminjaman.id
    Terjadi saat POST /api/peminjaman
    PR #15 berisi: migrasi database untuk tambah kolom 'denda'

[E] Saya sudah coba:
    - Restart server → masih error
    - Delete database → error hilang, tapi data hilang juga
    Saya butuh solusi yang tidak menghapus data existing.
```

### 13.3.6 Worked Example 5: Arsitektur Decision

```
[C] Tim kami akan membangun fitur real-time notification untuk 
    Sistem Perpustakaan (notif buku tersedia, reminder deadline).
    Saat ini stack: Flask + SQLite + vanilla JS. Tim 4 mahasiswa,
    deadline 2 minggu.

[R] Kamu adalah solution architect yang berpengalaman dengan 
    web applications.

[I] Rekomendasikan pendekatan teknis untuk real-time notification.
    Bandingkan minimal 3 opsi dengan pro/cons.

[D] Constraint:
    - Tim belum pernah pakai WebSocket
    - Deploy di Railway (free tier)
    - Tidak boleh terlalu kompleks (proyek mahasiswa)
    - SQLite sebagai database (tidak ada Redis)
    Format: tabel perbandingan + rekomendasi dengan alasan

[E] Opsi yang saya tahu: polling, SSE, WebSocket. 
    Apakah ada opsi lain yang lebih sederhana?
```

---

## 13.4 Agentic Development

### 13.4.1 Apa Itu Agentic Development?

**Agentic development** adalah paradigma di mana AI agent secara **otonom** menyelesaikan task development — bukan hanya menjawab pertanyaan atau melengkapi kode, tapi mengeksekusi serangkaian langkah secara mandiri:

```
┌────────────────────────────────────────────────────────────────────┐
│              SPEKTRUM AI ASSISTANCE                                  │
│                                                                      │
│  Code Completion ──→ Chat Assistant ──→ Agentic Development          │
│  (pasif)              (interaktif)       (otonom)                     │
│                                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐       │
│  │ Copilot:     │  │ ChatGPT:     │  │ Claude Code (agent): │       │
│  │ Suggest next │  │ "Bagaimana   │  │ 1. Baca codebase     │       │
│  │ line of code │  │  caranya...?"│  │ 2. Plan approach     │       │
│  │              │  │              │  │ 3. Write code        │       │
│  │ Developer    │  │ Developer    │  │ 4. Run tests         │       │
│  │ decides &    │  │ copy-pastes  │  │ 5. Fix errors        │       │
│  │ types        │  │ & adapts     │  │ 6. Iterate until     │       │
│  │              │  │              │  │    tests pass        │       │
│  │ Control:     │  │ Control:     │  │                      │       │
│  │ 100% human   │  │ 80% human   │  │ Control: 30% human   │       │
│  │              │  │              │  │ (review & approve)   │       │
│  └──────────────┘  └──────────────┘  └──────────────────────┘       │
└────────────────────────────────────────────────────────────────────┘
```

### 13.4.2 Claude Code sebagai AI Agent

Claude Code adalah CLI tool dari Anthropic yang dapat:

```bash
# Contoh interaksi dengan Claude Code

$ claude "Implement fitur pencarian buku untuk Sistem Perpustakaan"

# Claude Code akan:
# 1. Membaca codebase (app/models/, app/routes/, tests/)
# 2. Memahami struktur yang sudah ada
# 3. Membuat file baru: app/routes/search.py
# 4. Mengedit file yang relevan: app/__init__.py (register blueprint)
# 5. Membuat test: tests/test_search.py
# 6. Menjalankan tests
# 7. Fix jika ada error
# 8. Menampilkan summary perubahan

# Contoh task yang cocok untuk agentic mode:
$ claude "Tambahkan authentication dengan Flask-Login"
$ claude "Refactor semua routes untuk pakai error handling yang konsisten"
$ claude "Fix bug: pagination tidak bekerja di halaman katalog"
$ claude "Tambahkan Dockerfile dan docker-compose.yml"
```

### 13.4.3 Human-in-the-Loop

Meskipun AI agent powerful, engineer **tetap harus** menjadi quality gate:

```
┌────────────────────────────────────────────────────────────────────┐
│              HUMAN-IN-THE-LOOP WORKFLOW                              │
│                                                                      │
│  Developer ──→ AI Agent ──→ Developer Review ──→ Merge/Reject       │
│  (task)        (execute)    (quality gate)       (decision)          │
│                                                                      │
│  ┌────────────────────────────────────────────────────────────┐     │
│  │ Developer HARUS:                                           │     │
│  │                                                            │     │
│  │ ✅ REVIEW setiap perubahan AI — baca line by line          │     │
│  │ ✅ TEST output AI — jalankan, coba edge cases              │     │
│  │ ✅ UNDERSTAND kode — bisa jelaskan jika ditanya            │     │
│  │ ✅ APPROVE sebelum merge — jangan auto-merge               │     │
│  │ ✅ GUIDE AI — berikan context yang tepat                   │     │
│  │ ✅ REJECT output yang salah — jangan kompromi quality      │     │
│  │                                                            │     │
│  │ Developer TIDAK BOLEH:                                     │     │
│  │                                                            │     │
│  │ ❌ Merge tanpa review ("AI pasti benar")                   │     │
│  │ ❌ Submit kode yang tidak dipahami                         │     │
│  │ ❌ Mengabaikan warning atau test failure                   │     │
│  │ ❌ Bergantung 100% pada AI tanpa verifikasi                │     │
│  └────────────────────────────────────────────────────────────┘     │
└────────────────────────────────────────────────────────────────────┘
```

### 13.4.4 AI Pair Programming Workflow

```
Workflow yang direkomendasikan untuk proyek IF2205:

┌────────────────────────────────────────────┐
│ 1. PLAN (Developer memimpin)               │
│    - Pilih user story dari sprint backlog   │
│    - Pahami acceptance criteria              │
│    - Tentukan pendekatan teknis              │
├────────────────────────────────────────────┤
│ 2. SCAFFOLD (AI membantu)                  │
│    - Generate boilerplate code               │
│    - Buat file structure                     │
│    - Generate model/schema awal              │
├────────────────────────────────────────────┤
│ 3. IMPLEMENT (Kolaborasi)                  │
│    - Developer tulis business logic          │
│    - AI bantu routine code & boilerplate     │
│    - Developer review setiap output AI       │
├────────────────────────────────────────────┤
│ 4. TEST (AI generate, Developer review)    │
│    - AI generate test cases                  │
│    - Developer tambah edge cases             │
│    - Developer jalankan & evaluasi coverage  │
├────────────────────────────────────────────┤
│ 5. REVIEW (Developer memimpin)             │
│    - AI bantu code review awal               │
│    - Developer/peer final review             │
│    - Fix issues sebelum merge                │
├────────────────────────────────────────────┤
│ 6. DOCUMENT (AI generate, Developer edit)  │
│    - AI generate API docs & README           │
│    - Developer verify accuracy               │
│    - Update AI Usage Log                     │
└────────────────────────────────────────────┘
```

---

## 13.5 AI Limitations dan Hallucinations

### 13.5.1 Jenis-Jenis Keterbatasan AI

| Limitasi | Deskripsi | Dampak | Mitigasi |
|----------|-----------|--------|----------|
| **Hallucination** | AI "mengkarang" API, library, atau fungsi yang tidak ada | Kode error saat runtime | Verifikasi di docs resmi |
| **Outdated knowledge** | Training data ada batas waktu (knowledge cutoff) | Gunakan API/syntax yang sudah deprecated | Cek changelog library |
| **Context window limit** | Tidak bisa memproses codebase yang sangat besar | Output tidak konsisten dengan kode lain | Berikan konteks yang relevan saja |
| **Security blind spots** | Bisa generate kode yang rentan (SQL injection, XSS) | Vulnerability di production | Manual security review wajib |
| **Business logic gap** | Tidak memahami domain bisnis spesifik | Kode tidak sesuai kebutuhan pengguna | Engineer specify requirements jelas |
| **Non-deterministic** | Output berbeda untuk prompt yang sama | Sulit reproduce dan debug | Simpan prompt + output untuk referensi |
| **Over-engineering** | AI sering menghasilkan solusi yang terlalu kompleks | Kode sulit dimaintain | Request solusi sederhana, KISS principle |

### 13.5.2 Contoh Hallucination yang Umum

```python
# ❌ HALLUCINATION 1: Library yang tidak ada
from flask_awesome_validator import validate_json  
# Library "flask_awesome_validator" TIDAK ADA!

# ✅ Yang benar:
from marshmallow import Schema, fields, validate
# atau
from wtforms.validators import DataRequired, Email

# ─────────────────────────────────────────────────────

# ❌ HALLUCINATION 2: API yang tidak ada
import requests
response = requests.get("https://api.perpustakaan.go.id/buku")
# Endpoint ini TIDAK ADA — AI mengkarangnya

# ✅ Mitigasi: selalu verifikasi URL API sebelum menggunakan

# ─────────────────────────────────────────────────────

# ❌ HALLUCINATION 3: Method yang tidak ada di versi terbaru
from sqlalchemy import select
# AI mungkin suggest syntax SQLAlchemy 1.x padahal Anda pakai 2.0
result = db.session.query(Buku).filter_by(id=1).first()
# Syntax ini masih works di 2.0 tapi deprecated

# ✅ SQLAlchemy 2.0 style:
stmt = select(Buku).where(Buku.id == 1)
result = db.session.execute(stmt).scalar_one_or_none()

# ─────────────────────────────────────────────────────

# ❌ HALLUCINATION 4: Parameter yang tidak ada
app.run(debug=True, auto_reload=True, hot_swap=True)
# Parameter "hot_swap" TIDAK ADA di Flask

# ✅ Yang benar:
app.run(debug=True, use_reloader=True)
```

### 13.5.3 Kapan TIDAK Menggunakan AI

```
┌────────────────────────────────────────────────────────────────┐
│            KAPAN TIDAK MENGGUNAKAN AI                           │
│                                                                 │
│  ❌ Ujian (UTS/UAS/Kuis) — academic dishonesty                 │
│                                                                 │
│  ❌ Security-critical code (authentication, encryption)         │
│     tanpa review manual — AI bisa miss vulnerability            │
│                                                                 │
│  ❌ Memahami konsep baru untuk pertama kali                     │
│     → Belajar manual dulu, AI untuk mempercepat setelah paham  │
│                                                                 │
│  ❌ Keputusan arsitektur besar tanpa diskusi tim                │
│     → AI sebagai input, tim yang memutuskan                    │
│                                                                 │
│  ❌ Kode yang melibatkan data sensitif (password, PII)          │
│     → Jangan paste data asli ke AI                             │
│                                                                 │
│  ❌ Ketika Anda tidak bisa menjelaskan output AI                │
│     → Jika ditanya dosen dan tidak bisa jelaskan = masalah     │
│                                                                 │
│  ⚠️  PRINSIP: Jika Anda tidak bisa menulis kode tersebut       │
│     tanpa AI (walaupun lebih lambat), maka Anda BELUM PAHAM.  │
│     Gunakan AI untuk mempercepat, bukan menggantikan belajar. │
└────────────────────────────────────────────────────────────────┘
```

---

## 13.6 Responsible AI Usage

### 13.6.1 AI Usage Log Template

Setiap penggunaan AI dalam proyek **wajib** didokumentasikan dalam AI Usage Log:

```markdown
# AI Usage Log — Tim Pustaka Digital

## Sprint 2, Minggu 9

### Entry 1
- **Tanggal:** 2026-03-15
- **Developer:** Budi
- **Task:** Implementasi endpoint POST /api/peminjaman
- **AI Tool:** Claude Code
- **Prompt:** (ringkasan) "Implement peminjaman endpoint dengan 
  validasi stok, max 3 buku per anggota, jatuh tempo 14 hari"
- **Output AI:** Endpoint lengkap dengan validasi (45 baris)
- **Modifikasi Manusia:**
  - Tambah error message dalam Bahasa Indonesia
  - Fix: formula jatuh tempo pakai timedelta bukan string
  - Tambah logging untuk audit trail
- **Evaluasi:** 80% output bisa dipakai langsung. Logika bisnis 
  benar, tapi perlu penyesuaian detail.
- **Waktu hemat:** ~30 menit (vs tulis dari scratch)

### Entry 2
- **Tanggal:** 2026-03-16
- **Developer:** Citra
- **Task:** Generate unit tests untuk model Peminjaman
- **AI Tool:** GitHub Copilot
- **Prompt:** (autocomplete saat menulis test file)
- **Output AI:** 8 test cases
- **Modifikasi Manusia:**
  - 2 test cases salah (assertion tidak sesuai business logic)
  - Tambah 3 edge cases yang AI miss
  - Fix fixture setup
- **Evaluasi:** 6/8 test cases benar. AI miss edge case: 
  pinjam buku yang sudah dipinjam anggota yang sama.
- **Pelajaran:** AI kurang paham business rules spesifik.
```

### 13.6.2 Prinsip AI Bertanggung Jawab

```
┌────────────────────────────────────────────────────────────────┐
│           5 PRINSIP RESPONSIBLE AI USAGE                        │
│                                                                  │
│  1. TRANSPARANSI (Transparency)                                  │
│     → Dokumentasikan semua penggunaan AI (AI Usage Log)          │
│     → Jangan sembunyikan bahwa AI digunakan                      │
│                                                                  │
│  2. VERIFIKASI (Verification)                                    │
│     → Selalu review dan test output AI                           │
│     → Jangan trust blindly — AI bisa salah                       │
│                                                                  │
│  3. PEMAHAMAN (Understanding)                                    │
│     → Jangan submit kode yang tidak Anda pahami                  │
│     → Harus bisa jelaskan setiap baris jika ditanya              │
│                                                                  │
│  4. ATRIBUSI (Attribution)                                       │
│     → Jangan klaim AI output sebagai karya 100% sendiri          │
│     → AI Usage Log adalah bentuk atribusi yang jujur             │
│                                                                  │
│  5. AMANAH (Trustworthiness)                                     │
│     → Gunakan AI untuk belajar, bukan menghindari belajar        │
│     → Jujur dalam pelaporan — amanah akademik                    │
└────────────────────────────────────────────────────────────────┘
```

### 13.6.3 Perspektif Islam tentang AI

Penggunaan AI dalam konteks akademik dan profesional dapat dilihat melalui beberapa prinsip Islam:

| Prinsip Islam | Aplikasi dalam AI Usage | Contoh |
|---------------|------------------------|--------|
| **Amanah** (Kepercayaan) | Menggunakan AI dengan jujur, melaporkan penggunaannya | Mengisi AI Usage Log dengan lengkap dan jujur |
| **Ikhtiar** (Usaha) | AI sebagai alat untuk memaksimalkan usaha, bukan menggantikan usaha | Belajar konsep dulu, lalu gunakan AI untuk mempercepat implementasi |
| **Ilmu** (Pengetahuan) | Mencari ilmu adalah kewajiban — AI memperluas akses ke ilmu | Gunakan AI untuk memahami konsep baru dari berbagai perspektif |
| **Itqan** (Kesempurnaan kerja) | AI membantu menghasilkan karya yang lebih berkualitas | Code review dengan AI + manual untuk kualitas maksimal |
| **Jujur** (Kejujuran) | Tidak menyalin output AI tanpa pemahaman dan modifikasi | "Saya menggunakan AI untuk generate boilerplate, lalu memodifikasi business logic sendiri" |
| **Adil** (Keadilan) | Kontribusi yang fair dalam tim, AI bukan shortcut | Semua anggota tim berkontribusi, bukan hanya satu orang + AI |

> **Hadits relevan:** *"Sesungguhnya Allah menyukai jika seseorang mengerjakan suatu pekerjaan, ia mengerjakannya dengan itqan (sempurna/profesional)."* (HR Thabrani)
>
> AI membantu kita mencapai *itqan* — kode yang lebih bersih, test yang lebih komprehensif, dokumentasi yang lebih lengkap. Tapi fondasi pemahaman tetap harus dari ikhtiar kita sendiri.

### 13.6.4 AI Adoption di Industri Teknologi Indonesia

Perusahaan-perusahaan teknologi Indonesia sudah mulai mengadopsi AI tools:

| Perusahaan | AI Usage | Policy |
|------------|----------|--------|
| **Gojek/GoTo** | Copilot untuk engineering team, AI code review | AI Policy internal, code review tetap wajib |
| **Tokopedia** | AI untuk test generation dan documentation | AI Usage tracking di sprint retrospective |
| **Traveloka** | Copilot + internal AI tools untuk productivity | Mandatory human review untuk semua AI-generated code |
| **Bukalapak** | ChatGPT/Claude untuk requirements analysis | AI sebagai brainstorming tool, keputusan oleh manusia |
| **Startup Indonesia** | Cursor/Claude Code untuk rapid prototyping | Tim kecil leverage AI untuk kecepatan development |

> **Tren:** Perusahaan Indonesia tidak menolak AI, tapi menerapkan prinsip **"AI as co-pilot, human as pilot"**. AI mempercepat, manusia memutuskan.

---

## Studi Kasus Komprehensif: Membangun Fitur dengan AI Pair Programming

**Skenario:** Tim Pustaka Digital ingin mengimplementasi fitur "Laporan Peminjaman Bulanan" menggunakan AI pair programming.

**User Story:** "Sebagai admin perpustakaan, saya ingin melihat laporan peminjaman per bulan agar bisa mengetahui tren peminjaman."

**Langkah-langkah AI Pair Programming:**

```
Langkah 1: Developer PLAN (tanpa AI)
- Pahami acceptance criteria
- Tentukan approach: API endpoint + chart di frontend
- Identifikasi data yang diperlukan

Langkah 2: SCAFFOLD dengan AI
Prompt: [C] Flask + SQLAlchemy, model Peminjaman sudah ada
        [R] Senior Flask developer
        [I] Buatkan API endpoint GET /api/laporan/bulanan
            yang return data peminjaman per bulan (12 bulan terakhir)
        [D] Format: {bulan: "2026-03", jumlah: 45}
            Include: total, rata-rata, bulan tertinggi

Langkah 3: IMPLEMENT (kolaborasi developer + AI)
- AI generate endpoint skeleton → developer review
- Developer tulis query yang sesuai dengan model yang ada
- AI bantu generate Chart.js code untuk frontend
- Developer sesuaikan styling dan label

Langkah 4: TEST (AI generate, developer review)
Prompt: Generate pytest tests untuk endpoint laporan bulanan
        Cover: data kosong, 1 bulan, 12 bulan, filter tahun

Langkah 5: REVIEW dan DOCUMENT
- Developer review semua kode AI
- Fix 2 issues: timezone handling, aggregate query optimization
- Update AI Usage Log
```

**Hasil:** Fitur selesai dalam 3 jam (estimasi tanpa AI: 6-8 jam). 70% kode dari AI, 100% di-review dan dimodifikasi oleh developer.

---

## AI Corner: AI Integration Comprehensive (Level: Expert)

Bab ini **adalah** bab AI — jadi AI Corner fokus pada teknik lanjutan.

### 1. Prompt Chaining (Multi-Step Prompts)

```
Step 1: "Analisis requirements berikut dan identifikasi 
         entity dan relasi: [paste SRS]"
         
Step 2: "Berdasarkan entity di atas, buatkan ERD dalam 
         format PlantUML dengan cardinality"
         
Step 3: "Berdasarkan ERD di atas, generate SQLAlchemy 
         models untuk Flask app"
         
Step 4: "Berdasarkan models di atas, buatkan CRUD 
         API endpoints dengan Flask Blueprint"
         
Step 5: "Generate pytest tests untuk semua endpoints 
         di atas, termasuk edge cases"

Setiap step menggunakan output step sebelumnya sebagai context.
Ini disebut "prompt chaining" — lebih efektif dari satu 
prompt besar.
```

### 2. AI untuk Refactoring Patterns

```
Prompt:
"Kode berikut memiliki code smells: long method, magic 
numbers, duplicate code. Refactor menggunakan:
1. Extract Method
2. Replace Magic Number with Named Constant
3. Extract Class (jika perlu)

Jelaskan setiap perubahan dan alasannya.
Pertahankan semua existing behavior (no behavior change).

[paste kode yang perlu di-refactor]"
```

### 3. AI untuk Architecture Decision Records (ADR)

```
Prompt:
"Kami harus memilih antara:
a) Server-side rendering (Flask Jinja2 templates)
b) Client-side SPA (React + Flask API)
c) Hybrid (Flask templates + HTMX)

Konteks: proyek akhir mahasiswa, tim 4 orang, 10 minggu,
1 anggota pernah pakai React, semua familiar Python.

Buatkan ADR (Architecture Decision Record) dengan format:
- Title
- Status
- Context
- Decision
- Consequences (pro/con)
- Alternatives Considered"
```

### 4. AI untuk Automated Code Review Checklist

```
Prompt:
"Buatkan code review checklist otomatis untuk proyek Flask.
Untuk setiap file yang di-review, cek:

1. Security: SQL injection, XSS, CSRF, hardcoded secrets
2. Performance: N+1 query, missing index, large response
3. Reliability: error handling, edge cases, null checks
4. Maintainability: naming, docstrings, complexity
5. Testing: test coverage, missing test scenarios

Format: checklist Markdown yang bisa di-copy ke PR template."
```

### 5. AI untuk Learning dan Skill Gap Analysis

```
Prompt:
"Saya mahasiswa semester 4 Informatika. Skill saya saat ini:
- Python: intermediate (bisa Flask, SQLAlchemy)
- JavaScript: beginner (DOM manipulation, fetch API)
- Git: intermediate (branch, PR, merge)
- Testing: beginner (baru belajar pytest)
- Docker: tidak ada pengalaman
- CI/CD: tidak ada pengalaman

Untuk proyek akhir RPL (web app end-to-end), buatkan:
1. Skill gap analysis
2. Learning roadmap 10 minggu
3. Resources untuk setiap skill (gratis)
4. Milestone mingguan yang realistis"
```

### 6. Ethical AI Scenarios untuk Diskusi

| Skenario | Pertanyaan Etis | Perspektif |
|----------|-----------------|------------|
| Mahasiswa A menggunakan AI untuk seluruh kode proyek tanpa memahaminya | Apakah ini melanggar amanah akademik? | Amanah: ya, karena tujuan proyek adalah belajar |
| Tim B menggunakan AI untuk generate test cases dan menemukan bug yang sebelumnya tidak terdeteksi | Apakah ini penggunaan AI yang baik? | Itqan: ya, AI membantu kualitas |
| Mahasiswa C copy-paste kode AI tanpa mengisi AI Usage Log | Apakah ini plagiarism? | Jujur: tidak mengisi log = tidak transparan |
| Tim D menggunakan AI untuk semua code review tanpa review manual | Apakah ini cukup? | Ikhtiar: tidak, AI review perlu dilengkapi human review |

---

## Latihan Soal

### Level Dasar (C1-C2)

1. Sebutkan dan jelaskan 5 kategori AI tools untuk software engineering beserta contoh tool-nya.
2. Jelaskan apa itu AI hallucination dan berikan 3 contoh spesifik dalam konteks pengembangan perangkat lunak.
3. Apa perbedaan antara AI code completion (seperti Copilot) dan agentic development (seperti Claude Code)?
4. Sebutkan 5 prinsip responsible AI usage dan jelaskan masing-masing secara singkat.
5. Jelaskan framework CRIDE untuk prompt engineering dan fungsi setiap elemennya.

### Level Menengah (C3-C4)

6. Tuliskan prompt CRIDE lengkap untuk task berikut: "Generate Flask API endpoint untuk sistem registrasi anggota perpustakaan." Sertakan semua 5 elemen CRIDE.
7. Gunakan AI untuk generate 5 unit tests untuk endpoint yang Anda buat di proyek. Dokumentasikan: prompt yang digunakan, output AI, evaluasi Anda (berapa yang benar, apa yang dimodifikasi).
8. Tuliskan 3 prompt dengan teknik berbeda (persona, few-shot, constraint) untuk task yang sama: "Generate Flask API endpoint untuk pengembalian buku." Bandingkan hasilnya.
9. Isi AI Usage Log untuk 1 minggu penggunaan AI dalam proyek tim. Minimal 5 entries dengan format lengkap.
10. Analisis kelebihan dan kekurangan menggunakan AI untuk masing-masing fase SDLC. Buat tabel perbandingan.
11. Berikan contoh 3 skenario di mana penggunaan AI **tidak tepat** dan jelaskan alasannya.

### Level Mahir (C5-C6)

12. Evaluasi pernyataan: "AI developer tools akan menggantikan software engineer dalam 10 tahun." Berikan argumen pro dan kontra berdasarkan bukti dan tren saat ini.
13. Rancang AI integration workflow lengkap untuk tim development 4 orang — kapan AI digunakan, kapan tidak, bagaimana memastikan kualitas, dan bagaimana mendokumentasikan penggunaan. Sertakan flowchart.
14. Kritisi output AI berikut: [berikan kode AI yang mengandung 3+ masalah]. Identifikasi semua masalah, jelaskan mengapa bermasalah, dan berikan perbaikan.
15. Desain kebijakan AI usage untuk sebuah startup Indonesia yang bergerak di fintech. Pertimbangkan: keamanan data, compliance (OJK), kualitas kode, dan produktivitas developer.
16. Tuliskan esai 500 kata: "Amanah dan AI: Bagaimana Prinsip Islam Membimbing Penggunaan AI yang Bertanggung Jawab dalam Software Engineering." Sertakan minimal 3 contoh konkret.

---

## Rangkuman

1. **AI tools** hadir di setiap fase SDLC — dari requirements engineering hingga maintenance — dengan tools yang semakin mature dan terintegrasi.
2. **Lanskap AI tools** mencakup code completion (Copilot), AI chat (Claude, ChatGPT), AI-native IDE (Cursor), dan agentic development (Claude Code) dengan fitur dan use case yang berbeda.
3. **CRIDE framework** (Context, Role, Instructions, Details, Examples) adalah panduan untuk menulis prompt yang menghasilkan output AI berkualitas tinggi dan sesuai kebutuhan.
4. **Agentic development** memungkinkan AI agent menyelesaikan task secara otonom (baca, tulis, execute, iterate), tapi tetap memerlukan human-in-the-loop sebagai quality gate.
5. **AI limitations** (hallucination, outdated knowledge, security blind spots, non-deterministic) harus dipahami dan dimitigasi — AI adalah alat yang powerful tapi tidak sempurna.
6. **Responsible AI usage** memerlukan transparansi (AI Usage Log), verifikasi (review + test), pemahaman (bisa jelaskan), atribusi (jujur), dan amanah.
7. **AI Usage Log** adalah dokumentasi wajib yang mencatat prompt, output, modifikasi, dan evaluasi untuk setiap penggunaan AI dalam proyek.
8. **Perspektif Islam**: AI adalah alat untuk ikhtiar dan mencapai itqan — gunakan dengan amanah, kejujuran, dan niat belajar, bukan menggantikan belajar.
9. **Tren industri Indonesia**: Perusahaan teknologi Indonesia mengadopsi AI dengan prinsip "AI as co-pilot, human as pilot" — AI mempercepat, manusia memutuskan.
10. **Prinsip utama**: AI adalah *coding partner*, bukan pengganti pemikiran kritis. Mahasiswa wajib memahami dan mampu menjelaskan setiap output AI yang digunakan.

---

## Referensi

1. GitHub. (2025). *GitHub Copilot Documentation*. docs.github.com/copilot.
2. Anthropic. (2025). *Claude Code Documentation*. docs.anthropic.com/claude-code.
3. Cursor. (2025). *Cursor IDE Documentation*. docs.cursor.com.
4. Poldrack, R. A. et al. (2023). "AI-assisted coding: Experiments with GPT-4." *arXiv preprint arXiv:2304.13187*.
5. Vaithilingam, P. et al. (2022). "Expectation vs Experience: Evaluating the Usability of Code Generation Tools." *CHI 2022*.
6. Dakhel, A. M. et al. (2023). "GitHub Copilot AI pair programmer: Asset or Liability?" *Journal of Systems and Software*, 203.
7. Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson.
8. ACM Code of Ethics and Professional Conduct. (2018). acm.org/code-of-ethics.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
