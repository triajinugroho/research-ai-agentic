# BAB 14: PROYEK AKHIR — WEB APP END-TO-END

**Oleh: Tri Aji Nugroho, S.T., M.T.**
**Mata Kuliah:** IF2205 Rekayasa Perangkat Lunak
**Program Studi:** Informatika, Universitas Al Azhar Indonesia
**Semester:** Genap 2025/2026

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom | Estimasi Waktu |
|-----------|-----------|-------------|----------------|
| 7.3 | Mengevaluasi tren modern software engineering (supply chain security, green software, platform engineering) dan relevansinya dengan industri Indonesia | C5 (Mengevaluasi) | 75 menit |
| 7.4 | Merancang roadmap pengembangan karir sebagai software engineer berdasarkan kebutuhan industri Indonesia dan global | C6 (Mencipta) | 75 menit |

**Setelah mempelajari bab ini, mahasiswa mampu:**

1. Merancang dan membangun web application end-to-end dalam tim Agile/Scrum yang mengintegrasikan seluruh pengetahuan dari Bab 1-13
2. Menerapkan tech stack lengkap (Flask + JavaScript + SQLite + Docker + GitHub Actions) untuk proyek akhir
3. Melaksanakan Sprint 0-4 dengan deliverables yang terukur dan berkualitas
4. Menyiapkan demo dan presentasi proyek yang profesional
5. Menyusun dokumentasi proyek standar industri (README, API docs, user guide)
6. Mengevaluasi tren modern SE: supply chain security (SBOM), green software, dan platform engineering
7. Merancang personal career roadmap sebagai software engineer di ekosistem teknologi Indonesia

---

## Peta Konsep Bab 14

```
                    ┌──────────────────────────────────────────────┐
                    │  PROYEK AKHIR: WEB APP END-TO-END            │
                    └──────────────────────┬───────────────────────┘
                                           │
        ┌──────────────┬───────────────────┼──────────────┬────────────────┐
        │              │                   │              │                │
        ▼              ▼                   ▼              ▼                ▼
  ┌───────────┐ ┌────────────┐    ┌──────────────┐ ┌───────────┐ ┌──────────────┐
  │ Project   │ │ Sprint     │    │ Tech Stack   │ │ Modern SE │ │ Career       │
  │ Overview  │ │ 0-4        │    │ & Code       │ │ Trends    │ │ Roadmap      │
  │ & Setup   │ │ Walkthrough│    │ Structure    │ │           │ │              │
  └─────┬─────┘ └─────┬──────┘    └──────┬───────┘ └─────┬─────┘ └──────┬───────┘
        │              │                  │              │               │
  ┌─────┴─────┐  ┌─────┴──────┐   ┌──────┴──────┐ ┌────┴──────┐ ┌─────┴────────┐
  │Tujuan &   │  │Sprint 0:   │   │Flask +      │ │SBOM &     │ │Junior →      │
  │Pilihan    │  │ Setup      │   │SQLAlchemy   │ │Supply     │ │Senior →      │
  │Proyek     │  │Sprint 1:   │   │HTML/CSS/JS  │ │Chain      │ │Lead →        │
  │Rubric     │  │ Foundation │   │Docker       │ │Green SW   │ │Architect     │
  │           │  │Sprint 2:   │   │GitHub       │ │Platform   │ │Sertifikasi   │
  │           │  │ Core Dev   │   │Actions      │ │Engineering│ │Indonesia     │
  │           │  │Sprint 3:   │   │SQLite       │ │           │ │Tech Career   │
  │           │  │ Quality    │   │             │ │           │ │              │
  │           │  │Sprint 4:   │   │             │ │           │ │              │
  │           │  │ Deploy     │   │             │ │           │ │              │
  └───────────┘  └────────────┘   └─────────────┘ └───────────┘ └──────────────┘
```

---

## 14.1 Gambaran Proyek Akhir

### 14.1.1 Tujuan Proyek

Proyek akhir mengintegrasikan **seluruh pengetahuan Software Engineering** dari Bab 1-13 ke dalam satu web application yang nyata:

```
┌────────────────────────────────────────────────────────────────────────┐
│                    INTEGRASI PENGETAHUAN SE                             │
│                                                                         │
│  Bab 1-2  : Prinsip SE + Model Proses          → Agile/Scrum          │
│  Bab 3-4  : Requirements Engineering            → SRS + User Stories   │
│  Bab 5-6  : Arsitektur + Desain (UML)           → Arsitektur + UML     │
│  Bab 7    : Construction + Version Control      → Clean Code + Git     │
│  Bab 8-9  : Testing + Quality Assurance         → pytest + TDD         │
│  Bab 10   : DevOps + CI/CD                      → GitHub Actions       │
│  Bab 11   : Maintenance + Evolution             → Refactoring + SemVer │
│  Bab 12   : Project Management + Agile          → Sprint Management    │
│  Bab 13   : AI-Augmented SE                     → AI Pair Programming  │
│                                                                         │
│  SEMUA TERAPLIKASI dalam SATU PROYEK yang functional, tested,          │
│  dan deployed!                                                          │
└────────────────────────────────────────────────────────────────────────┘
```

### 14.1.2 Spesifikasi Proyek

| Aspek | Detail |
|-------|--------|
| **Tipe** | Web Application (full-stack) |
| **Ukuran Tim** | 3-4 mahasiswa |
| **Metodologi** | Agile/Scrum (4 Sprint + Sprint 0) |
| **Tech Stack** | Flask (backend), HTML/CSS/JS (frontend), SQLite (database), Docker, GitHub Actions |
| **Platform Dev** | GitHub Codespaces |
| **Deployment** | Railway / Render (free tier) |
| **Timeline** | Sprint 0 (W5-6) → Sprint 1 (W7+9) → Sprint 2 (W10-11) → Sprint 3 (W12-13) → Sprint 4 (W14) → Demo (W15) |
| **Deliverables** | GitHub repo, SRS, UML, working app, test suite, CI/CD, demo, AI Usage Log |
| **Konteks** | Wajib menggunakan konteks Indonesia (UMKM, layanan publik, pendidikan, dll.) |

### 14.1.3 Pilihan Proyek (Konteks Indonesia)

| # | Proyek | Deskripsi | Kompleksitas | Stakeholder |
|---|--------|-----------|-------------|-------------|
| 1 | **Sistem Informasi Perpustakaan** | Katalog buku, peminjaman, pengembalian, denda, notifikasi | Medium | Pustakawan, anggota, admin |
| 2 | **Aplikasi Manajemen UMKM** | Inventory produk, pencatatan penjualan, laporan keuangan sederhana | Medium | Pemilik UMKM, kasir |
| 3 | **Sistem Antrian Puskesmas** | Pendaftaran online, antrian real-time, rekam medis sederhana | Medium-High | Pasien, petugas loket, dokter |
| 4 | **Platform E-Commerce Produk Lokal** | Katalog produk daerah, cart, checkout, tracking pesanan | Medium-High | Pembeli, penjual, admin |
| 5 | **Aplikasi Pengelolaan Zakat/Infaq** | Pencatatan donasi, distribusi, laporan, data muzakki/mustahik | Medium | Donatur, pengurus, admin |
| 6 | **Sistem Informasi Akademik Mini** | Manajemen mahasiswa, mata kuliah, nilai, jadwal | Medium | Mahasiswa, dosen, admin |

> **Tips pemilihan:** Pilih proyek yang:
> - Memiliki konteks Indonesia yang jelas
> - Tidak terlalu sederhana (minimal 5 entitas, 10 endpoints)
> - Tidak terlalu kompleks (selesai dalam 10 minggu oleh 4 orang)
> - Menarik bagi semua anggota tim

### 14.1.4 Grading Rubric

| Komponen | Bobot | Kriteria Penilaian |
|----------|-------|--------------------|
| **Requirements & Design** | 15% | SRS lengkap, 15+ user stories INVEST, UML (class, sequence, activity), ERD ternormalisasi |
| **Implementation** | 25% | Clean code (PEP 8/ESLint), fitur lengkap sesuai sprint backlog, proper error handling, separation of concerns |
| **Testing** | 15% | Unit tests (coverage >= 70%), integration tests, test quality (meaningful assertions, edge cases) |
| **DevOps** | 10% | CI/CD pipeline (lint + test + deploy), Dockerfile, docker-compose, cloud deployment berjalan |
| **Presentation & Demo** | 10% | Demo live (bukan video), semua Must Have berjalan, komunikasi jelas, Q&A |
| **Teamwork** | 10% | Git log merata, Scrum artifacts (sprint backlog, burndown, retrospective), fair contribution |
| **Documentation** | 10% | README profesional, API docs, user guide, architecture docs |
| **AI Integration** | 5% | AI Usage Log komprehensif, responsible usage, minimal 5 entries per anggota |
| **Total** | **100%** | |

---

## 14.2 Tech Stack Setup

### 14.2.1 Arsitektur Aplikasi

```
┌─────────────────────────────────────────────────────────────────┐
│                      ARSITEKTUR PROYEK AKHIR                     │
│                                                                   │
│  ┌─────────────────────────┐    ┌─────────────────────────────┐ │
│  │     FRONTEND             │    │         BACKEND              │ │
│  │  ┌───────────────────┐  │    │  ┌───────────────────────┐  │ │
│  │  │  HTML Templates   │  │    │  │    Flask App           │  │ │
│  │  │  (Jinja2)         │  │    │  │    (app factory)       │  │ │
│  │  └───────────────────┘  │    │  └───────────┬───────────┘  │ │
│  │  ┌───────────────────┐  │    │              │               │ │
│  │  │  CSS (styles)     │  │◄───┤  ┌───────────┴───────────┐  │ │
│  │  └───────────────────┘  │    │  │   Blueprints (Routes)  │  │ │
│  │  ┌───────────────────┐  │    │  │   /api/buku            │  │ │
│  │  │  JavaScript       │──┼───►│  │   /api/anggota         │  │ │
│  │  │  (fetch API)      │  │    │  │   /api/peminjaman      │  │ │
│  │  └───────────────────┘  │    │  └───────────┬───────────┘  │ │
│  └─────────────────────────┘    │              │               │ │
│                                  │  ┌───────────┴───────────┐  │ │
│  ┌─────────────────────────┐    │  │   Services (Logic)     │  │ │
│  │     DEVOPS               │    │  └───────────┬───────────┘  │ │
│  │  ┌───────────────────┐  │    │              │               │ │
│  │  │  GitHub Actions   │  │    │  ┌───────────┴───────────┐  │ │
│  │  │  (CI/CD)          │  │    │  │   SQLAlchemy Models    │  │ │
│  │  └───────────────────┘  │    │  └───────────┬───────────┘  │ │
│  │  ┌───────────────────┐  │    │              │               │ │
│  │  │  Docker           │  │    │  ┌───────────┴───────────┐  │ │
│  │  │  (Container)      │  │    │  │   SQLite Database      │  │ │
│  │  └───────────────────┘  │    │  │   (perpustakaan.db)    │  │ │
│  │  ┌───────────────────┐  │    │  └───────────────────────┘  │ │
│  │  │  Railway/Render   │  │    │                              │ │
│  │  │  (Hosting)        │  │    │                              │ │
│  │  └───────────────────┘  │    └─────────────────────────────┘ │
│  └─────────────────────────┘                                     │
└─────────────────────────────────────────────────────────────────┘
```

### 14.2.2 Project Structure Template

```
sistem-perpustakaan/
├── README.md                    # Project overview, setup, API docs
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Container configuration
├── docker-compose.yml           # Multi-container setup
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
├── .flake8                      # Linting configuration
├── run.py                       # Entry point
│
├── .github/
│   ├── workflows/
│   │   └── ci.yml               # CI/CD pipeline
│   └── pull_request_template.md # PR template
│
├── app/
│   ├── __init__.py              # App factory (create_app)
│   ├── config.py                # Configuration classes
│   ├── extensions.py            # Flask extensions (db, login, etc.)
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── buku.py              # Model Buku
│   │   ├── anggota.py           # Model Anggota
│   │   └── peminjaman.py        # Model Peminjaman
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py              # Main routes (home, about)
│   │   ├── auth.py              # Authentication routes
│   │   ├── buku.py              # CRUD buku
│   │   ├── anggota.py           # CRUD anggota
│   │   └── peminjaman.py        # CRUD peminjaman
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── buku_service.py      # Business logic buku
│   │   └── peminjaman_service.py# Business logic peminjaman
│   │
│   ├── templates/
│   │   ├── base.html            # Base template (layout)
│   │   ├── index.html           # Homepage
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── buku/
│   │   │   ├── list.html
│   │   │   ├── detail.html
│   │   │   └── form.html
│   │   └── peminjaman/
│   │       ├── list.html
│   │       └── form.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   └── main.js
│       └── images/
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Shared fixtures
│   ├── test_models.py           # Unit tests: models
│   ├── test_routes.py           # Integration tests: API endpoints
│   └── test_services.py         # Unit tests: business logic
│
├── docs/
│   ├── srs.md                   # Software Requirements Specification
│   ├── api-docs.md              # API Documentation
│   ├── user-guide.md            # User Guide
│   ├── architecture.md          # Architecture Decision Records
│   └── ai-usage-log.md          # AI Usage Log
│
└── migrations/                  # Database migrations (if using Flask-Migrate)
```

### 14.2.3 Kode Setup Awal

**File: `run.py`**

```python
"""Entry point untuk menjalankan aplikasi."""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

**File: `app/__init__.py`**

```python
"""Application factory untuk Sistem Perpustakaan UAI."""
from flask import Flask
from app.config import config
from app.extensions import db, login_manager

def create_app(config_name='development'):
    """Buat dan konfigurasi Flask app instance.
    
    Args:
        config_name: Nama konfigurasi ('development', 'testing', 'production')
    
    Returns:
        Flask app instance yang sudah dikonfigurasi
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Inisialisasi extensions
    db.init_app(app)
    login_manager.init_app(app)
    
    # Register blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.buku import buku_bp
    from app.routes.anggota import anggota_bp
    from app.routes.peminjaman import peminjaman_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(buku_bp, url_prefix='/api/buku')
    app.register_blueprint(anggota_bp, url_prefix='/api/anggota')
    app.register_blueprint(peminjaman_bp, url_prefix='/api/peminjaman')
    
    # Error handlers
    register_error_handlers(app)
    
    # Buat tabel database
    with app.app_context():
        db.create_all()
    
    return app

def register_error_handlers(app):
    """Daftarkan custom error handlers."""
    from flask import jsonify
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Resource tidak ditemukan'}), 404
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'error': 'Request tidak valid'}), 400
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({'error': 'Terjadi kesalahan server'}), 500
```

**File: `app/config.py`**

```python
"""Konfigurasi aplikasi untuk berbagai environment."""
import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-ganti-di-production')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Konfigurasi development."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///perpustakaan_dev.db'

class TestingConfig(Config):
    """Konfigurasi testing."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    """Konfigurasi production."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///perpustakaan.db')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
```

**File: `app/extensions.py`**

```python
"""Flask extensions yang digunakan oleh aplikasi."""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
```

**File: `app/models/buku.py`**

```python
"""Model Buku untuk Sistem Perpustakaan."""
from app.extensions import db
from datetime import datetime

class Buku(db.Model):
    """Representasi buku dalam perpustakaan.
    
    Attributes:
        id: Primary key
        judul: Judul buku
        pengarang: Nama pengarang
        isbn: ISBN (International Standard Book Number)
        tahun_terbit: Tahun terbit
        stok: Jumlah stok tersedia
        kategori: Kategori buku (fiksi, non-fiksi, referensi, dll.)
        created_at: Timestamp pembuatan record
    """
    __tablename__ = 'buku'
    
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(200), nullable=False)
    pengarang = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(13), unique=True)
    tahun_terbit = db.Column(db.Integer)
    stok = db.Column(db.Integer, default=0)
    kategori = db.Column(db.String(50), default='umum')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relasi
    peminjaman = db.relationship('Peminjaman', backref='buku', lazy=True)
    
    def is_available(self):
        """Cek apakah buku tersedia untuk dipinjam."""
        return self.stok > 0
    
    def to_dict(self):
        """Konversi ke dictionary untuk JSON response."""
        return {
            'id': self.id,
            'judul': self.judul,
            'pengarang': self.pengarang,
            'isbn': self.isbn,
            'tahun_terbit': self.tahun_terbit,
            'stok': self.stok,
            'kategori': self.kategori,
            'is_available': self.is_available()
        }
    
    def __repr__(self):
        return f'<Buku {self.judul}>'
```

**File: `tests/conftest.py`**

```python
"""Shared test fixtures untuk pytest."""
import pytest
from app import create_app
from app.extensions import db as _db
from app.models.buku import Buku
from app.models.anggota import Anggota

@pytest.fixture(scope='session')
def app():
    """Buat app instance untuk testing."""
    app = create_app('testing')
    return app

@pytest.fixture(scope='function')
def db(app):
    """Buat fresh database untuk setiap test."""
    with app.app_context():
        _db.create_all()
        yield _db
        _db.session.rollback()
        _db.drop_all()

@pytest.fixture
def client(app):
    """Test client untuk HTTP requests."""
    return app.test_client()

@pytest.fixture
def sample_buku(db):
    """Buku contoh untuk testing."""
    buku_list = [
        Buku(judul="Laskar Pelangi", pengarang="Andrea Hirata",
             isbn="9789793062792", tahun_terbit=2005, stok=5, 
             kategori="fiksi"),
        Buku(judul="Bumi Manusia", pengarang="Pramoedya Ananta Toer",
             isbn="9789799731234", tahun_terbit=1980, stok=3,
             kategori="fiksi"),
        Buku(judul="Filosofi Teras", pengarang="Henry Manampiring",
             isbn="9786020633121", tahun_terbit=2018, stok=7,
             kategori="non-fiksi"),
    ]
    db.session.add_all(buku_list)
    db.session.commit()
    return buku_list
```

**File: `requirements.txt`**

```
Flask==3.1.0
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
python-dotenv==1.0.1
gunicorn==22.0.0
```

**File: `Dockerfile`**

```dockerfile
# Dockerfile untuk Sistem Perpustakaan
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements dan install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 5000

# Jalankan aplikasi dengan gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
```

**File: `docker-compose.yml`**

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - SECRET_KEY=${SECRET_KEY:-super-secret-key}
    volumes:
      - ./instance:/app/instance  # Persist SQLite database
    restart: unless-stopped
```

**File: `.github/workflows/ci.yml`**

```yaml
name: CI Pipeline

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
      - name: Install linting tools
        run: pip install flake8
      - name: Run flake8
        run: flake8 app/ tests/ --max-line-length=120 --exclude=__pycache__

  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - name: Run tests with coverage
        run: pytest tests/ -v --cov=app --cov-report=term-missing --cov-fail-under=70
      
  deploy:
    runs-on: ubuntu-latest
    needs: test
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to Railway
        uses: bervProject/railway-deploy@main
        with:
          railway_token: ${{ secrets.RAILWAY_TOKEN }}
          service: perpustakaan-app
```

---

## 14.3 Sprint Walkthrough

### 14.3.1 Sprint 0: Project Setup (Minggu 5-6)

**Sprint Goal:** "Tim terbentuk, repository siap, dan requirements terdefinisi."

Sprint 0 bukan sprint Scrum resmi, melainkan fase persiapan sebelum development dimulai:

```
┌────────────────────────────────────────────────────────────────────┐
│                       SPRINT 0: SETUP                               │
│  Durasi: 2 minggu (Minggu 5-6)                                     │
│                                                                      │
│  Minggu 5:                                                           │
│  ┌────────────────────────────────────────────────────────────┐     │
│  │ ☐ Bentuk tim (3-4 orang), tentukan nama tim                │     │
│  │ ☐ Pilih proyek dari daftar (atau propose sendiri)          │     │
│  │ ☐ Setup GitHub repository (README, .gitignore, LICENSE)    │     │
│  │ ☐ Setup GitHub Codespaces                                  │     │
│  │ ☐ Buat team agreement (komunikasi, git workflow, standar)  │     │
│  │ ☐ Bagi peran: PO, SM (bergilir), Developer, QA/DevOps     │     │
│  └────────────────────────────────────────────────────────────┘     │
│                                                                      │
│  Minggu 6:                                                           │
│  ┌────────────────────────────────────────────────────────────┐     │
│  │ ☐ Requirements elicitation (diskusi stakeholder)            │     │
│  │ ☐ Tulis 15+ user stories (INVEST criteria)                 │     │
│  │ ☐ Prioritasi backlog (MoSCoW)                              │     │
│  │ ☐ Buat SRS draft (overview, functional & non-functional)   │     │
│  │ ☐ Design: UML diagrams (class, sequence)                   │     │
│  │ ☐ Design: ERD + SQL schema                                 │     │
│  │ ☐ Design: REST API endpoint list                           │     │
│  │ ☐ Setup project structure (app factory, config, models)    │     │
│  │ ☐ Setup branch protection rules                            │     │
│  └────────────────────────────────────────────────────────────┘     │
│                                                                      │
│  Deliverables:                                                       │
│  ✅ GitHub repo dengan structure lengkap                             │
│  ✅ README.md dengan project description & setup guide               │
│  ✅ 15+ user stories dengan acceptance criteria                      │
│  ✅ Product Backlog (MoSCoW prioritized)                             │
│  ✅ UML diagrams (Class, Sequence, Activity)                         │
│  ✅ ERD + REST API endpoint list                                     │
│  ✅ SRS draft (docs/srs.md)                                         │
│  ✅ Team agreement                                                   │
└────────────────────────────────────────────────────────────────────┘
```

**Contoh User Stories (Sistem Perpustakaan):**

```python
# Product Backlog — Sistem Perpustakaan UAI
product_backlog = [
    # Must Have (M)
    {"id": "US-01", "priority": "M", "points": 5,
     "story": "Sebagai admin, saya ingin menambahkan buku baru ke katalog "
              "agar koleksi perpustakaan selalu up-to-date",
     "acceptance": [
         "Given: admin di halaman tambah buku",
         "When: mengisi form (judul, pengarang, ISBN, stok) dan submit",
         "Then: buku tersimpan dan muncul di katalog"
     ]},
    {"id": "US-02", "priority": "M", "points": 3,
     "story": "Sebagai anggota, saya ingin mencari buku berdasarkan "
              "judul atau pengarang agar bisa menemukan buku dengan cepat",
     "acceptance": [
         "Given: anggota di halaman katalog",
         "When: mengetik keyword di search box",
         "Then: ditampilkan daftar buku yang cocok (max 20 per halaman)"
     ]},
    {"id": "US-03", "priority": "M", "points": 8,
     "story": "Sebagai anggota, saya ingin meminjam buku secara online "
              "agar tidak perlu antri di counter",
     "acceptance": [
         "Given: anggota sudah login, buku tersedia (stok > 0)",
         "When: klik tombol 'Pinjam' di halaman detail buku",
         "Then: peminjaman tercatat, stok berkurang, jatuh tempo 14 hari"
     ]},
    {"id": "US-04", "priority": "M", "points": 5,
     "story": "Sebagai anggota, saya ingin login ke sistem "
              "agar bisa mengakses fitur peminjaman",
     "acceptance": [
         "Given: anggota di halaman login",
         "When: memasukkan email dan password yang benar",
         "Then: redirect ke dashboard dengan nama anggota ditampilkan"
     ]},
    {"id": "US-05", "priority": "M", "points": 3,
     "story": "Sebagai anggota, saya ingin melihat daftar buku yang "
              "sedang saya pinjam agar bisa tracking jatuh tempo",
     "acceptance": [
         "Given: anggota sudah login",
         "When: mengakses halaman 'Peminjaman Saya'",
         "Then: ditampilkan daftar buku yang dipinjam dengan status & jatuh tempo"
     ]},
    
    # Should Have (S)
    {"id": "US-06", "priority": "S", "points": 5,
     "story": "Sebagai anggota, saya ingin mengembalikan buku secara "
              "online agar proses lebih cepat"},
    {"id": "US-07", "priority": "S", "points": 5,
     "story": "Sebagai admin, saya ingin melihat laporan peminjaman "
              "per bulan agar bisa analisis tren"},
    {"id": "US-08", "priority": "S", "points": 3,
     "story": "Sebagai anggota, saya ingin mendaftar akun baru "
              "agar bisa menjadi anggota perpustakaan"},
    
    # Could Have (C)
    {"id": "US-09", "priority": "C", "points": 5,
     "story": "Sebagai anggota, saya ingin menerima notifikasi email "
              "saat jatuh tempo mendekat"},
    {"id": "US-10", "priority": "C", "points": 8,
     "story": "Sebagai admin, saya ingin mengelola denda keterlambatan "
              "secara otomatis"},
]
```

### 14.3.2 Sprint 1: Foundation (Minggu 7 + 9)

> **Catatan:** Minggu 8 = UTS, tidak ada aktivitas sprint.

**Sprint Goal:** "Backend API inti dan halaman utama berjalan end-to-end."

```
┌────────────────────────────────────────────────────────────────────┐
│                     SPRINT 1: FOUNDATION                            │
│  Durasi: 2 minggu efektif (W7 + W9, minus UTS W8)                 │
│  Velocity target: 15-20 story points (sprint pertama)              │
│                                                                      │
│  Sprint Backlog:                                                     │
│  ┌──────┬────────────────────────────────────┬──────┬──────────┐    │
│  │ ID   │ Story                              │ Pts  │ Assignee │    │
│  ├──────┼────────────────────────────────────┼──────┼──────────┤    │
│  │ US-04│ Login & Authentication             │  5   │ Budi     │    │
│  │ US-08│ Registrasi anggota baru            │  3   │ Budi     │    │
│  │ US-01│ CRUD Buku (tambah, edit, hapus)    │  5   │ Citra    │    │
│  │ US-02│ Pencarian buku                     │  3   │ Citra    │    │
│  │ T-01 │ Setup base template & navigation   │  2   │ Aisyah   │    │
│  │ T-02 │ Setup database & seed data         │  2   │ Dimas    │    │
│  ├──────┼────────────────────────────────────┼──────┼──────────┤    │
│  │      │ TOTAL                              │ 20   │          │    │
│  └──────┴────────────────────────────────────┴──────┴──────────┘    │
│                                                                      │
│  Definition of Done (DoD):                                           │
│  ☐ Kode di-push ke branch feature/*                                 │
│  ☐ PR dibuat dengan deskripsi yang jelas                            │
│  ☐ Minimal 1 code reviewer approve                                 │
│  ☐ Unit test ada (minimal happy path)                               │
│  ☐ Tidak ada error flake8                                           │
│  ☐ PR merged ke develop                                             │
│                                                                      │
│  Deliverables Sprint 1:                                              │
│  ✅ Login/Register berfungsi                                        │
│  ✅ CRUD Buku berfungsi (admin)                                     │
│  ✅ Pencarian buku berfungsi                                        │
│  ✅ Base template dengan navigation                                 │
│  ✅ Database dengan seed data                                       │
└────────────────────────────────────────────────────────────────────┘
```

### 14.3.3 Sprint 2: Core Development (Minggu 10-11)

**Sprint Goal:** "Fitur utama (Must Have) berfungsi end-to-end."

```
Sprint Backlog:
┌──────┬────────────────────────────────────┬──────┬──────────┐
│ ID   │ Story                              │ Pts  │ Assignee │
├──────┼────────────────────────────────────┼──────┼──────────┤
│ US-03│ Proses peminjaman buku online      │  8   │ Budi     │
│ US-05│ Daftar buku yang sedang dipinjam   │  3   │ Aisyah   │
│ US-06│ Pengembalian buku online           │  5   │ Citra    │
│ T-03 │ Dashboard halaman utama            │  3   │ Aisyah   │
│ T-04 │ Error handling & validation        │  2   │ Dimas    │
├──────┼────────────────────────────────────┼──────┼──────────┤
│      │ TOTAL                              │ 21   │          │
└──────┴────────────────────────────────────┴──────┴──────────┘
```

**Contoh implementasi fitur inti (peminjaman):**

```python
# app/services/peminjaman_service.py
"""Business logic untuk peminjaman buku."""
from datetime import datetime, timedelta
from app.extensions import db
from app.models.buku import Buku
from app.models.anggota import Anggota
from app.models.peminjaman import Peminjaman

# Konstanta bisnis
MAX_PEMINJAMAN_AKTIF = 3
DURASI_PINJAM_HARI = 14
DENDA_PER_HARI = 1000  # Rp 1.000 per hari keterlambatan

class PeminjamanService:
    """Service class untuk operasi peminjaman buku."""
    
    @staticmethod
    def pinjam_buku(anggota_id, buku_id):
        """Proses peminjaman buku.
        
        Args:
            anggota_id: ID anggota yang meminjam
            buku_id: ID buku yang dipinjam
            
        Returns:
            dict: Data peminjaman jika berhasil
            
        Raises:
            ValueError: Jika validasi gagal
        """
        # Validasi anggota
        anggota = Anggota.query.get(anggota_id)
        if not anggota:
            raise ValueError("Anggota tidak ditemukan")
        
        # Validasi buku
        buku = Buku.query.get(buku_id)
        if not buku:
            raise ValueError("Buku tidak ditemukan")
        
        if not buku.is_available():
            raise ValueError(f"Stok buku '{buku.judul}' habis")
        
        # Cek jumlah peminjaman aktif
        pinjaman_aktif = Peminjaman.query.filter_by(
            anggota_id=anggota_id, 
            status='aktif'
        ).count()
        
        if pinjaman_aktif >= MAX_PEMINJAMAN_AKTIF:
            raise ValueError(
                f"Sudah meminjam {MAX_PEMINJAMAN_AKTIF} buku. "
                "Kembalikan dulu sebelum meminjam yang baru."
            )
        
        # Cek apakah sudah pinjam buku yang sama
        sudah_pinjam = Peminjaman.query.filter_by(
            anggota_id=anggota_id,
            buku_id=buku_id,
            status='aktif'
        ).first()
        
        if sudah_pinjam:
            raise ValueError(f"Buku '{buku.judul}' sudah Anda pinjam")
        
        # Buat peminjaman
        peminjaman = Peminjaman(
            anggota_id=anggota_id,
            buku_id=buku_id,
            tgl_pinjam=datetime.utcnow(),
            tgl_jatuh_tempo=datetime.utcnow() + timedelta(days=DURASI_PINJAM_HARI),
            status='aktif'
        )
        
        # Kurangi stok
        buku.stok -= 1
        
        db.session.add(peminjaman)
        db.session.commit()
        
        return peminjaman.to_dict()
    
    @staticmethod
    def kembalikan_buku(peminjaman_id):
        """Proses pengembalian buku.
        
        Returns:
            dict: Data peminjaman yang diupdate, termasuk denda jika ada
        """
        peminjaman = Peminjaman.query.get(peminjaman_id)
        if not peminjaman:
            raise ValueError("Peminjaman tidak ditemukan")
        
        if peminjaman.status != 'aktif':
            raise ValueError("Buku sudah dikembalikan")
        
        # Update status
        peminjaman.tgl_kembali = datetime.utcnow()
        peminjaman.status = 'dikembalikan'
        
        # Hitung denda jika terlambat
        denda = 0
        if peminjaman.tgl_kembali > peminjaman.tgl_jatuh_tempo:
            hari_terlambat = (peminjaman.tgl_kembali - peminjaman.tgl_jatuh_tempo).days
            denda = hari_terlambat * DENDA_PER_HARI
            peminjaman.denda = denda
        
        # Kembalikan stok
        peminjaman.buku.stok += 1
        
        db.session.commit()
        
        result = peminjaman.to_dict()
        result['denda'] = denda
        result['denda_formatted'] = f"Rp {denda:,.0f}"
        return result
```

### 14.3.4 Sprint 3: Quality (Minggu 12-13)

**Sprint Goal:** "Kode tested, CI/CD pipeline berjalan, dan Docker siap."

```
Sprint Backlog:
┌──────┬────────────────────────────────────┬──────┬──────────┐
│ ID   │ Task                               │ Pts  │ Assignee │
├──────┼────────────────────────────────────┼──────┼──────────┤
│ T-05 │ Unit tests model (coverage >= 70%) │  5   │ Dimas    │
│ T-06 │ Integration tests API endpoints    │  5   │ Citra    │
│ T-07 │ GitHub Actions CI pipeline         │  3   │ Dimas    │
│ T-08 │ Dockerfile & docker-compose        │  3   │ Dimas    │
│ US-07│ Laporan peminjaman per bulan       │  5   │ Budi     │
│ T-09 │ Code review & refactoring          │  2   │ All      │
├──────┼────────────────────────────────────┼──────┼──────────┤
│      │ TOTAL                              │ 23   │          │
└──────┴────────────────────────────────────┴──────┴──────────┘
```

**Contoh test yang bermakna:**

```python
# tests/test_services.py
"""Unit tests untuk PeminjamanService."""
import pytest
from datetime import datetime, timedelta
from app.services.peminjaman_service import PeminjamanService

class TestPeminjamanService:
    """Test suite untuk business logic peminjaman."""
    
    def test_pinjam_buku_sukses(self, db, sample_buku, sample_anggota):
        """Happy path: peminjaman berhasil."""
        result = PeminjamanService.pinjam_buku(
            anggota_id=sample_anggota.id,
            buku_id=sample_buku[0].id
        )
        
        assert result['status'] == 'aktif'
        assert result['buku']['judul'] == 'Laskar Pelangi'
        
        # Verifikasi stok berkurang
        buku = sample_buku[0]
        assert buku.stok == 4  # dari 5 menjadi 4
    
    def test_pinjam_buku_stok_habis(self, db, sample_anggota):
        """Edge case: buku dengan stok 0."""
        from app.models.buku import Buku
        buku_habis = Buku(judul="Habis", pengarang="Test", stok=0)
        db.session.add(buku_habis)
        db.session.commit()
        
        with pytest.raises(ValueError, match="Stok buku.*habis"):
            PeminjamanService.pinjam_buku(
                anggota_id=sample_anggota.id,
                buku_id=buku_habis.id
            )
    
    def test_pinjam_melebihi_batas(self, db, sample_buku, sample_anggota):
        """Edge case: anggota sudah pinjam 3 buku (max)."""
        # Pinjam 3 buku
        for i in range(3):
            PeminjamanService.pinjam_buku(
                anggota_id=sample_anggota.id,
                buku_id=sample_buku[i].id
            )
        
        # Pinjam buku ke-4 harus gagal
        from app.models.buku import Buku
        buku_ke4 = Buku(judul="Buku 4", pengarang="Test", stok=1)
        db.session.add(buku_ke4)
        db.session.commit()
        
        with pytest.raises(ValueError, match="Sudah meminjam 3 buku"):
            PeminjamanService.pinjam_buku(
                anggota_id=sample_anggota.id,
                buku_id=buku_ke4.id
            )
    
    def test_kembalikan_buku_tepat_waktu(self, db, sample_buku, sample_anggota):
        """Happy path: kembalikan buku tanpa denda."""
        result = PeminjamanService.pinjam_buku(
            anggota_id=sample_anggota.id,
            buku_id=sample_buku[0].id
        )
        
        kembalikan = PeminjamanService.kembalikan_buku(result['id'])
        
        assert kembalikan['status'] == 'dikembalikan'
        assert kembalikan['denda'] == 0
        assert sample_buku[0].stok == 5  # stok kembali
    
    def test_kembalikan_buku_terlambat(self, db, sample_buku, sample_anggota):
        """Edge case: kembalikan buku terlambat, ada denda."""
        from app.models.peminjaman import Peminjaman
        
        # Buat peminjaman yang sudah jatuh tempo 3 hari lalu
        peminjaman = Peminjaman(
            anggota_id=sample_anggota.id,
            buku_id=sample_buku[0].id,
            tgl_pinjam=datetime.utcnow() - timedelta(days=17),
            tgl_jatuh_tempo=datetime.utcnow() - timedelta(days=3),
            status='aktif'
        )
        sample_buku[0].stok -= 1
        db.session.add(peminjaman)
        db.session.commit()
        
        result = PeminjamanService.kembalikan_buku(peminjaman.id)
        
        assert result['status'] == 'dikembalikan'
        assert result['denda'] >= 3000  # minimal 3 hari x Rp 1.000
```

### 14.3.5 Sprint 4: Polish & Deploy (Minggu 14)

**Sprint Goal:** "Aplikasi deployed dan siap demo."

```
Sprint Backlog:
┌──────┬────────────────────────────────────┬──────┬──────────┐
│ ID   │ Task                               │ Pts  │ Assignee │
├──────┼────────────────────────────────────┼──────┼──────────┤
│ T-10 │ Deploy ke Railway/Render           │  3   │ Dimas    │
│ T-11 │ Final bug fixes & polish           │  5   │ All      │
│ T-12 │ API documentation (docs/api-docs)  │  3   │ Citra    │
│ T-13 │ User guide (docs/user-guide)       │  3   │ Aisyah   │
│ T-14 │ README profesional                 │  2   │ Budi     │
│ T-15 │ Presentation slides                │  2   │ All      │
│ T-16 │ AI Usage Log finalization          │  2   │ All      │
├──────┼────────────────────────────────────┼──────┼──────────┤
│      │ TOTAL                              │ 20   │          │
└──────┴────────────────────────────────────┴──────┴──────────┘
```

---

## 14.4 Documentation Standards

### 14.4.1 README Profesional

Setiap proyek akhir **wajib** memiliki README.md yang profesional:

```markdown
# Sistem Perpustakaan UAI

> Aplikasi manajemen perpustakaan berbasis web untuk Universitas 
> Al Azhar Indonesia. Proyek akhir IF2205 Rekayasa Perangkat Lunak.

![CI Status](https://github.com/username/repo/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Flask](https://img.shields.io/badge/flask-3.1-green)

## Fitur Utama
- Katalog buku dengan pencarian
- Peminjaman & pengembalian buku online
- Dashboard admin dengan laporan
- Sistem denda otomatis
- Authentication (login/register)

## Tech Stack
| Layer | Technology |
|-------|-----------|
| Backend | Flask 3.1, SQLAlchemy |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |
| CI/CD | GitHub Actions |
| Container | Docker |
| Hosting | Railway |

## Quick Start

### Prerequisites
- Python 3.11+
- Git

### Setup Lokal
\```bash
# Clone repository
git clone https://github.com/username/sistem-perpustakaan.git
cd sistem-perpustakaan

# Buat virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
python run.py
# Buka http://localhost:5000
\```

### Docker
\```bash
docker-compose up --build
# Buka http://localhost:5000
\```

## Tim
| Nama | Peran | GitHub |
|------|-------|--------|
| Aisyah | Product Owner, Frontend | @aisyah |
| Budi | Scrum Master, Backend | @budi |
| Citra | Lead Developer | @citra |
| Dimas | QA & DevOps | @dimas |

## Dokumentasi
- [SRS](docs/srs.md)
- [API Docs](docs/api-docs.md)
- [User Guide](docs/user-guide.md)
- [AI Usage Log](docs/ai-usage-log.md)
```

### 14.4.2 API Documentation

```markdown
# API Documentation — Sistem Perpustakaan UAI

Base URL: `https://perpustakaan-app.up.railway.app/api`

## Overview

| Method | Endpoint | Deskripsi | Auth |
|--------|----------|-----------|------|
| POST | /auth/login | Login | No |
| POST | /auth/register | Register | No |
| GET | /buku | Daftar semua buku | No |
| GET | /buku/search?q=keyword | Cari buku | No |
| GET | /buku/:id | Detail buku | No |
| POST | /buku | Tambah buku baru | Admin |
| PUT | /buku/:id | Edit buku | Admin |
| DELETE | /buku/:id | Hapus buku | Admin |
| GET | /peminjaman | Daftar peminjaman saya | User |
| POST | /peminjaman | Pinjam buku | User |
| PUT | /peminjaman/:id/kembalikan | Kembalikan buku | User |

## Detail Endpoint

### POST /api/peminjaman
**Deskripsi:** Proses peminjaman buku baru.

**Request Body:**
\```json
{
  "buku_id": 5
}
\```

**Response 201 (Success):**
\```json
{
  "message": "Peminjaman berhasil",
  "data": {
    "id": 1,
    "buku": {"id": 5, "judul": "Laskar Pelangi"},
    "tgl_pinjam": "2026-04-01",
    "tgl_jatuh_tempo": "2026-04-15",
    "status": "aktif"
  }
}
\```

**Response 400 (Error):**
\```json
{"error": "Stok buku 'Laskar Pelangi' habis"}
\```
\```json
{"error": "Sudah meminjam 3 buku. Kembalikan dulu sebelum meminjam yang baru."}
\```
```

---

## 14.5 Demo dan Presentasi

### 14.5.1 Demo Preparation Guide

```
┌────────────────────────────────────────────────────────────────────┐
│                    DEMO PREPARATION CHECKLIST                       │
│                                                                      │
│  H-3 (3 hari sebelum demo):                                        │
│  ☐ Aplikasi deployed dan bisa diakses via URL publik               │
│  ☐ Semua fitur Must Have berjalan                                  │
│  ☐ Database sudah ada seed data yang realistis                     │
│  ☐ CI/CD pipeline green (semua test pass)                          │
│                                                                      │
│  H-1 (1 hari sebelum demo):                                        │
│  ☐ Rehearsal demo minimal 2 kali                                   │
│  ☐ Persiapkan demo script (urutan fitur yang akan ditunjukkan)     │
│  ☐ Siapkan backup: video recording demo (jika internet bermasalah)│
│  ☐ Test di browser yang berbeda                                    │
│  ☐ Slides presentasi sudah selesai                                 │
│                                                                      │
│  Saat Demo:                                                          │
│  ☐ Login sebagai user yang sudah disiapkan (bukan register baru)   │
│  ☐ Demo fitur sesuai script, jangan improvisasi                    │
│  ☐ Tunjukkan CI/CD pipeline (GitHub Actions — green build)         │
│  ☐ Tunjukkan test results & coverage                               │
│  ☐ Siap untuk pertanyaan teknis dari dosen                         │
│                                                                      │
│  ⚠️  Yang Harus DIHINDARI saat demo:                                │
│  ✗ "Ini harusnya berjalan, tapi..." (sudah test sebelumnya!)      │
│  ✗ Menunjukkan halaman error tanpa penjelasan                      │
│  ✗ Demo di localhost (harus deployed!)                              │
│  ✗ Terlalu banyak waktu di setup, kurang di demo fitur             │
└────────────────────────────────────────────────────────────────────┘
```

### 14.5.2 Struktur Presentasi (15 menit/tim)

| Bagian | Durasi | Konten | Presenter |
|--------|--------|--------|-----------|
| **Intro** | 2 menit | Tim, project overview, problem statement, konteks Indonesia | PO |
| **Architecture** | 3 menit | Tech stack, arsitektur (diagram), UML key diagrams, database design | Lead Dev |
| **Live Demo** | 5 menit | Demo semua fitur Must Have, tunjukkan error handling, responsiveness | Semua |
| **Engineering** | 3 menit | Testing (coverage), CI/CD (GitHub Actions), Docker, deployment | QA/DevOps |
| **Lessons Learned** | 2 menit | Apa yang berjalan baik, tantangan, refleksi AI usage | SM |

### 14.5.3 Tips Presentasi Profesional

```
Struktur Demo Script (5 menit):

1. [0:00] "Selamat datang di Sistem Perpustakaan UAI"
   → Tunjukkan halaman utama (deployed URL)

2. [0:30] "Saya login sebagai anggota perpustakaan"
   → Login → Dashboard → tunjukkan sidebar menu

3. [1:00] "Fitur pencarian buku"
   → Ketik keyword → hasil muncul → klik detail buku

4. [1:30] "Proses peminjaman"
   → Klik "Pinjam" → konfirmasi → status aktif

5. [2:30] "Daftar peminjaman saya"
   → Tunjukkan daftar + jatuh tempo + tombol kembalikan

6. [3:00] "Pengembalian buku"
   → Klik "Kembalikan" → status berubah → stok kembali

7. [3:30] "Login sebagai admin — laporan"
   → Laporan peminjaman bulanan → chart

8. [4:00] "CI/CD Pipeline"
   → Buka GitHub Actions → tunjukkan green build
   → Tunjukkan test coverage report

9. [4:30] "Deployment"
   → Tunjukkan Railway dashboard → URL publik

10. [5:00] Selesai. "Ada pertanyaan?"
```

---

## 14.6 Tren Modern Software Engineering

### 14.6.1 Software Supply Chain Security & SBOM

**Supply chain attack** adalah serangan yang menargetkan dependency (library) yang digunakan oleh aplikasi, bukan aplikasi itu sendiri. Ini menjadi perhatian serius setelah beberapa insiden besar:

```
┌────────────────────────────────────────────────────────────────────┐
│              SOFTWARE SUPPLY CHAIN SECURITY                         │
│                                                                      │
│  Insiden Besar:                                                      │
│  • SolarWinds (2020): Malware diinjeksi ke update software resmi    │
│  • Log4Shell (2021): Vulnerability di Log4j, dipakai jutaan app     │
│  • event-stream (2018): npm package populer disusupi cryptominer    │
│  • Colors.js (2022): Maintainer sengaja merusak package sendiri     │
│                                                                      │
│  SBOM (Software Bill of Materials):                                  │
│  Daftar lengkap semua komponen/library yang digunakan aplikasi      │
│                                                                      │
│  Aplikasi Anda                                                       │
│  ├── Flask 3.1.0                                                     │
│  │   ├── Werkzeug 3.1.3                                              │
│  │   ├── Jinja2 3.1.4                                                │
│  │   └── click 8.1.7                                                 │
│  ├── SQLAlchemy 2.0.36                                               │
│  ├── Flask-Login 0.6.3                                               │
│  └── gunicorn 22.0.0                                                 │
│                                                                      │
│  Pertanyaan: Apakah Anda tahu SEMUA library yang dipakai?           │
│  Apakah ada yang memiliki known vulnerability?                       │
│                                                                      │
│  Tools: GitHub Dependabot, pip-audit, safety, Snyk                  │
└────────────────────────────────────────────────────────────────────┘
```

**Praktik untuk proyek akhir:**

```bash
# Cek vulnerability di dependencies Python
pip install pip-audit
pip-audit

# Output:
# Found 0 known vulnerabilities in 8 packages
# ✅ Aman!

# Atau jika ada vulnerability:
# flask-sqlalchemy  3.0.2  CVE-2024-XXXX  High
# Recommendation: Upgrade to >= 3.1.0
```

### 14.6.2 Green Software Engineering

**Green Software** adalah praktik membangun perangkat lunak yang mengonsumsi lebih sedikit energi dan menghasilkan lebih sedikit emisi karbon:

| Prinsip | Penjelasan | Contoh Penerapan |
|---------|------------|------------------|
| **Energy Efficiency** | Kode yang efisien mengonsumsi lebih sedikit listrik | Optimasi query database, hindari N+1 queries |
| **Carbon Awareness** | Jalankan workload saat grid listrik lebih hijau | Schedule CI/CD builds di waktu off-peak |
| **Hardware Efficiency** | Maksimalkan penggunaan hardware | Container sizing yang tepat, auto-scaling |
| **Measurement** | Ukur carbon footprint software | Green Software Foundation SCI metric |

```
Dampak Software terhadap Lingkungan:

Data Center Global mengonsumsi ~1-2% listrik dunia
    └── Setara emisi industri penerbangan!

┌────────────────────────────────────────┐
│ Yang bisa developer lakukan:           │
│                                         │
│ 1. Optimasi query (reduce compute)      │
│ 2. Compress assets (reduce bandwidth)   │
│ 3. Lazy loading (reduce unnecessary)    │
│ 4. Cache effectively (reduce repeat)    │
│ 5. Right-size containers (reduce waste) │
│ 6. Delete dead code (reduce storage)    │
└────────────────────────────────────────┘
```

### 14.6.3 Platform Engineering

**Platform Engineering** adalah disiplin membangun dan mengelola **Internal Developer Platform (IDP)** — infrastruktur yang memudahkan developer lain untuk build, test, dan deploy:

```
Evolusi Developer Experience:

Era 1: "Setiap tim setup sendiri" (chaos)
  Developer → manual setup → deploy manual → monitoring manual

Era 2: DevOps (2010-2020)
  Developer → CI/CD → container → cloud
  (Setiap tim buat pipeline sendiri)

Era 3: Platform Engineering (2020+)
  ┌──────────────────────────────────────────┐
  │        Internal Developer Platform        │
  │                                           │
  │  Developer:                               │
  │  "Saya butuh: web app + database + CI/CD" │
  │                                           │
  │  Platform:                                │
  │  "Ini template-nya. 1-click deploy."      │
  │  ┌─────────────────────────────────────┐  │
  │  │ ✅ Git repo created                 │  │
  │  │ ✅ CI/CD pipeline configured        │  │
  │  │ ✅ Database provisioned             │  │
  │  │ ✅ Monitoring & logging setup       │  │
  │  │ ✅ Security scanning enabled        │  │
  │  └─────────────────────────────────────┘  │
  └──────────────────────────────────────────┘
  
  Contoh: GitHub Codespaces, Vercel, Railway
  → Anda sudah menggunakan platform engineering!
```

**Relevansi untuk Indonesia:**

Perusahaan besar Indonesia (GoTo, Traveloka, Bukalapak) sudah mulai membangun IDP internal:
- **GoTo:** Internal platform "GoCloud" untuk standardisasi deployment
- **Traveloka:** Platform team yang menyediakan template dan tooling
- **Bukalapak:** "Bukaengine" sebagai internal developer platform

---

## 14.7 Career Roadmap Software Engineer di Indonesia

### 14.7.1 Jenjang Karir SE

```
┌────────────────────────────────────────────────────────────────────┐
│               CAREER ROADMAP SOFTWARE ENGINEER                      │
│                                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │
│  │  Junior   │→│  Mid-     │→│  Senior   │→│  Staff/Principal  │   │
│  │  Engineer │  │  Level    │  │  Engineer │  │  Engineer         │   │
│  │  (0-2 th) │  │  (2-5 th)│  │  (5-8 th)│  │  (8+ tahun)       │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────────┘   │
│        │              │             │                │              │
│  Fokus:         Fokus:        Fokus:          Fokus:               │
│  - Belajar      - Deliver     - Mentor        - Technical vision   │
│  - Coding       - Design      - Architecture  - Org-wide impact    │
│  - Tasks        - Lead        - Strategy      - Innovation         │
│                   features                                          │
│                                                                      │
│  Alternative Tracks (setelah Senior):                                │
│                                                                      │
│  Individual Contributor (IC):   Management:                          │
│  Staff → Principal →            Engineering Manager →                │
│  Distinguished Engineer         Director of Engineering →            │
│                                 VP Engineering → CTO                 │
└────────────────────────────────────────────────────────────────────┘
```

### 14.7.2 Detail per Level

| Level | Tahun Exp | Skill Ekspektasi | Salary Range (2026, Jakarta) | Tanggung Jawab |
|-------|-----------|------------------|------------------------------|----------------|
| **Junior** | 0-2 | Coding, debugging, basic Git, 1 framework | Rp 5-10 juta/bulan | Mengerjakan task yang diberikan, belajar codebase |
| **Mid-Level** | 2-5 | System design, code review, testing, mentoring junior | Rp 10-20 juta/bulan | Deliver fitur end-to-end, review kode orang lain |
| **Senior** | 5-8 | Architecture, leadership, cross-team collaboration | Rp 20-40 juta/bulan | Design system, mentor tim, technical decision |
| **Staff** | 8+ | Org-wide impact, technical vision, complex problem solving | Rp 40-80 juta/bulan | Define technical strategy, solve hardest problems |
| **Lead/Manager** | 5+ | People management, project planning, stakeholder mgmt | Rp 25-60 juta/bulan | Manage team, hire, career development |

> **Catatan:** Range salary sangat bervariasi tergantung perusahaan (startup vs corporate vs multinational), lokasi, dan negosiasi. Angka di atas adalah estimasi untuk Jakarta, 2026.

### 14.7.3 Ekosistem Teknologi Indonesia

```
┌────────────────────────────────────────────────────────────────────┐
│            EKOSISTEM KARIR TECH DI INDONESIA                        │
│                                                                      │
│  ┌────────────────┐  ┌──────────────────┐  ┌───────────────────┐   │
│  │  TECH UNICORNS  │  │  FINTECH/BANKS   │  │  GOVERNMENT/BUMN  │   │
│  ├────────────────┤  ├──────────────────┤  ├───────────────────┤   │
│  │ • GoTo (Gojek)  │  │ • OVO / GoPay    │  │ • Telkom (digital)│   │
│  │ • Tokopedia     │  │ • DANA           │  │ • LKPP (e-proc)   │   │
│  │ • Traveloka     │  │ • Bank Jago      │  │ • Kominfo          │   │
│  │ • Bukalapak     │  │ • BCA Digital    │  │ • BPJS             │   │
│  │ • Blibli        │  │ • Bank Mandiri   │  │ • Pajak Online     │   │
│  │                  │  │   Livin'         │  │                    │   │
│  │ Kultur: Agile,   │  │ Kultur: Regulasi │  │ Kultur: Structured,│   │
│  │ fast-paced,      │  │ OJK/BI ketat,    │  │ waterfall, job     │   │
│  │ startup mindset  │  │ security-first   │  │ security           │   │
│  └────────────────┘  └──────────────────┘  └───────────────────┘   │
│                                                                      │
│  ┌────────────────┐  ┌──────────────────┐  ┌───────────────────┐   │
│  │  STARTUP       │  │  MULTINATIONAL   │  │  FREELANCE/       │   │
│  │  (Early Stage) │  │  (MNC di Indo)   │  │  REMOTE           │   │
│  ├────────────────┤  ├──────────────────┤  ├───────────────────┤   │
│  │ • SaaS Indo     │  │ • Google Indo    │  │ • Upwork          │   │
│  │ • EduTech       │  │ • AWS Indo       │  │ • Toptal          │   │
│  │ • HealthTech    │  │ • Microsoft Indo │  │ • Turing          │   │
│  │ • AgriTech      │  │ • Shopee         │  │ • Open source     │   │
│  │ • UMKM SaaS     │  │ • Grab           │  │                    │   │
│  │                  │  │                  │  │ Salary: USD-based │   │
│  │ Kultur: Wear     │  │ Kultur: Global   │  │ Rp 20-100 juta+   │   │
│  │ many hats,       │  │ standards,       │  │ /bulan             │   │
│  │ equity upside    │  │ good benefits    │  │                    │   │
│  └────────────────┘  └──────────────────┘  └───────────────────┘   │
└────────────────────────────────────────────────────────────────────┘
```

### 14.7.4 Sertifikasi dan Pengembangan Skill

| Sertifikasi | Fokus | Level | Biaya (est.) | Relevansi |
|-------------|-------|-------|-------------|-----------|
| **AWS Cloud Practitioner** | Cloud fundamentals | Pemula | $100 (ujian) | Sangat tinggi — cloud standard industri |
| **AWS Solutions Architect** | Cloud architecture | Menengah | $150 (ujian) | Tinggi untuk backend/devops engineer |
| **PSM I (Professional Scrum Master)** | Scrum framework | Pemula | $150 | Tinggi untuk Scrum Master / PM role |
| **PSPO I (Professional Scrum Product Owner)** | Product management | Pemula | $200 | Tinggi untuk Product Owner role |
| **Google Cloud Digital Leader** | Cloud overview | Pemula | $99 | Sedang — alternatif AWS |
| **Certified Kubernetes Administrator** | Container orchestration | Mahir | $395 | Tinggi untuk DevOps/SRE |
| **GitHub Foundations** | Git & GitHub | Pemula | Gratis | Bagus untuk portofolio awal |

**Rekomendasi untuk mahasiswa semester 4:**

```
Roadmap Pengembangan Skill (2 tahun ke depan):

Semester 4 (sekarang):
├── ✅ Python + Flask (sudah di IF2205)
├── ✅ Git + GitHub (sudah di IF2205)
├── ✅ Testing + CI/CD (sudah di IF2205)
└── 🎯 GitHub Foundations certification (gratis)

Semester 5-6:
├── 📚 JavaScript/TypeScript mendalam
├── 📚 React atau Vue.js (frontend framework)
├── 📚 PostgreSQL (production database)
├── 📚 REST API + GraphQL
└── 🎯 AWS Cloud Practitioner certification

Semester 7 (menjelang lulus):
├── 📚 System design fundamentals
├── 📚 Docker + Kubernetes basics
├── 📚 Microservices concepts
├── 💼 Internship / freelance project
└── 🎯 PSM I atau AWS Solutions Architect

Pasca lulus (tahun pertama kerja):
├── 💼 Junior developer role
├── 📚 Deep dive di domain (fintech, e-commerce, dll.)
├── 📚 Advanced testing & monitoring
└── 📚 Soft skills: komunikasi, presentasi, teamwork
```

### 14.7.5 Membangun Portofolio

Proyek akhir IF2205 bisa menjadi **portfolio piece pertama** yang kuat:

```
┌────────────────────────────────────────────────────────────────────┐
│              PORTFOLIO BUILDING TIPS                                 │
│                                                                      │
│  1. README Profesional                                               │
│     ├── Screenshots / GIF demo                                      │
│     ├── Tech stack badges (shields.io)                              │
│     ├── Setup instructions yang jelas                               │
│     └── Architecture diagram                                        │
│                                                                      │
│  2. Clean Git History                                                │
│     ├── Conventional commits (feat:, fix:, docs:)                   │
│     ├── Meaningful PR descriptions                                  │
│     ├── Branch strategy yang konsisten                              │
│     └── Hindari: "fix bug", "update", "asdf"                       │
│                                                                      │
│  3. Live Demo URL                                                    │
│     ├── Deployed dan bisa diakses                                   │
│     ├── Seed data yang realistis                                    │
│     └── Responsive (mobile-friendly)                                │
│                                                                      │
│  4. Documentation                                                    │
│     ├── API docs yang lengkap                                       │
│     ├── Architecture decision records                               │
│     └── AI Usage Log (tunjukkan responsible AI usage)               │
│                                                                      │
│  5. Online Presence                                                  │
│     ├── GitHub profile dengan pinned repos                          │
│     ├── LinkedIn dengan project highlights                          │
│     └── Blog post tentang lessons learned (opsional)                │
│                                                                      │
│  ⭐ Satu proyek yang komprehensif > 10 proyek setengah jadi        │
└────────────────────────────────────────────────────────────────────┘
```

---

## 14.8 Refleksi Pembelajaran

### 14.8.1 Pertanyaan Refleksi

Sebelum menyerahkan proyek akhir, setiap anggota tim wajib menjawab pertanyaan refleksi berikut:

1. **Skill SE:** Apa skill software engineering yang paling berharga yang Anda pelajari dari proyek ini? Mengapa?
2. **AI Usage:** Bagaimana AI membantu (dan tidak membantu) dalam development? Berikan contoh spesifik.
3. **Teamwork:** Bagaimana pengalaman bekerja dalam tim Agile? Apa tantangan terbesar?
4. **Improvement:** Apa yang akan Anda lakukan berbeda jika mengulang proyek dari awal?
5. **Career:** Bagaimana proyek ini memengaruhi rencana karir Anda sebagai software engineer?
6. **Nilai Islam:** Bagaimana prinsip amanah dan itqan terwujud (atau belum terwujud) dalam proyek Anda?

### 14.8.2 Retrospective Final

```
Format: 4Ls — Liked, Learned, Lacked, Longed For

❤️ LIKED (Yang disukai):
- Pair programming ternyata seru dan produktif
- Merasa bangga melihat app berjalan di cloud
- Proses code review meningkatkan kualitas kode
- Daily standup menjaga semua tetap sinkron

📚 LEARNED (Yang dipelajari):
- Docker ternyata tidak seseram yang dibayangkan
- Menulis test membutuhkan effort tapi worth it
- Estimasi sprint pertama selalu meleset — wajar!
- AI sangat membantu untuk boilerplate tapi perlu review

🔍 LACKED (Yang kurang):
- Waktu untuk explorasi fitur Should Have
- Pengalaman deployment ke production
- UI/UX design skills
- Otomatisasi test yang lebih comprehensive

🌟 LONGED FOR (Yang diinginkan):
- Lebih banyak waktu untuk proyek
- Mentoring dari praktisi industri
- Pengalaman dengan database production (PostgreSQL)
- Belajar frontend framework (React/Vue)
```

---

## Studi Kasus Komprehensif: Membangun Karir SE dari Proyek Akhir hingga Industri

**Profil:** Rani, lulusan Informatika UAI 2025, sekarang Junior Software Engineer di sebuah startup fintech di Jakarta.

**Timeline karir Rani:**

| Waktu | Aktivitas | Skill Acquired |
|-------|-----------|---------------|
| **Semester 4** (IF2205) | Proyek akhir: Sistem Antrian Puskesmas | Flask, Git, Scrum, Testing, CI/CD |
| **Semester 5** | Internship di startup edtech (3 bulan) | React, PostgreSQL, real-world Agile |
| **Semester 6** | Freelance project: UMKM inventory app | Full-stack, client communication |
| **Semester 7** | AWS Cloud Practitioner + PSM I certification | Cloud, Scrum framework |
| **Lulus** | Apply ke 15 perusahaan, interview di 8, offer dari 3 | Interview skills, system design basics |
| **Tahun 1** | Junior SE di fintech startup | Payment systems, microservices, monitoring |
| **Tahun 2** | Promosi ke Mid-Level SE | Code review, mentoring intern, feature ownership |

**Apa yang membuat portofolio Rani menonjol?**
1. Proyek IF2205 di-deploy dan bisa diakses live
2. README profesional dengan screenshots dan architecture diagram
3. AI Usage Log yang menunjukkan responsible AI usage
4. Clean git history dengan conventional commits
5. Blog post tentang "Lessons Learned Building a Health App with Flask"

**Tips dari Rani:**
> "Proyek akhir RPL adalah fondasi portofolio saya. Recruiter pertama yang meng-interview saya bilang: 'Saya lihat proyek kamu di GitHub, bagus dokumentasinya.' Itu yang membedakan saya dari kandidat lain."

---

## AI Corner: AI untuk Proyek Akhir dan Karir (Level: Expert)

### 1. AI untuk Project Scaffolding

```
Prompt:
"Saya akan membangun Sistem Perpustakaan Online dengan:
- Backend: Flask + SQLAlchemy + SQLite
- Frontend: HTML/CSS/JS (Jinja2 templates)
- Testing: pytest
- CI/CD: GitHub Actions
- Container: Docker

Buatkan project scaffold lengkap:
1. Directory structure dengan penjelasan setiap folder
2. requirements.txt dengan versi spesifik
3. app/__init__.py (app factory pattern)
4. app/config.py (development, testing, production)
5. Dockerfile + docker-compose.yml
6. .github/workflows/ci.yml
7. .gitignore untuk Python/Flask project
8. README.md template

Pastikan semua file bisa langsung dijalankan di GitHub Codespaces."
```

### 2. AI untuk Sprint Planning Assistance

```
Prompt:
"Tim 4 mahasiswa, Sprint 2 (2 minggu), velocity sprint 1: 15 pts.
Product Backlog (belum di-sprint):
- [M] Proses peminjaman buku (estimasi: 8 pts)
- [M] Daftar peminjaman anggota (3 pts)
- [S] Pengembalian buku (5 pts)
- [S] Dashboard admin (5 pts)
- [C] Notifikasi email (5 pts)
- [C] Laporan bulanan (5 pts)

Bantu plan Sprint 2:
1. Sprint Backlog recommendation (sesuai velocity 15-18 pts)
2. Task breakdown untuk setiap story
3. Dependency analysis
4. Risk assessment
5. Definition of Done untuk sprint ini"
```

### 3. AI untuk Code Review Comprehensive

```
Prompt:
"Review Pull Request berikut untuk proyek akhir IF2205.
Cek dari aspek:
1. Correctness (logic errors, edge cases)
2. Security (SQL injection, XSS, CSRF, auth bypass)
3. Performance (N+1 queries, missing pagination)
4. Maintainability (naming, complexity, DRY, SOLID)
5. Testing (coverage, meaningful assertions)

Format output:
🔴 MUST FIX: [issue] → [suggested fix]
🟡 SHOULD FIX: [issue] → [suggested fix]
🟢 NICE TO HAVE: [improvement]

[paste PR diff]"
```

### 4. AI untuk Career Guidance

```
Prompt:
"Saya mahasiswa semester 4 Informatika di Indonesia. 
Skill saat ini: Python (Flask), Git, basic testing.
Interest: backend development, cloud.

Buatkan personal career roadmap 5 tahun:
1. Skill acquisition timeline
2. Sertifikasi yang disarankan (dengan urutan)
3. Tipe perusahaan yang cocok di setiap level
4. Salary expectation realistic (Jakarta, 2026-2031)
5. Portfolio building strategy
6. Networking tips khusus Indonesia

Format: timeline per tahun dengan milestones."
```

### 5. AI untuk Interview Preparation

```
Prompt:
"Saya akan interview untuk posisi Junior Software Engineer 
di startup fintech Jakarta. Tech stack: Python, Flask, PostgreSQL.

Buatkan:
1. 10 pertanyaan teknis yang umum ditanyakan (dengan jawaban)
2. 5 pertanyaan system design level junior (dengan approach)
3. 5 pertanyaan behavioral (STAR format)
4. 3 coding challenge yang sering muncul (dengan solusi Python)
5. Pertanyaan yang harus saya tanyakan ke interviewer

Konteks Indonesia: termasuk pertanyaan tentang kultur kerja,
remote vs WFO, dan career growth."
```

---

## Latihan Soal

### Level Dasar (C1-C2)

1. Sebutkan 4 sprint dan deliverable masing-masing dalam proyek akhir IF2205.
2. Jelaskan 8 komponen grading rubric proyek akhir beserta bobotnya.
3. Apa yang dimaksud dengan SBOM (Software Bill of Materials) dan mengapa penting?
4. Sebutkan 5 jenjang karir software engineer dan skill utama di setiap level.
5. Jelaskan apa itu Green Software Engineering dan berikan 3 contoh penerapannya.

### Level Menengah (C3-C4)

6. Buatlah Sprint 1 Backlog lengkap untuk proyek "Sistem Antrian Puskesmas Online" dengan minimal 6 items, story points, dan assignee.
7. Buatlah project structure (directory tree) untuk proyek tim Anda. Jelaskan fungsi setiap folder dan file utama.
8. Tulis 5 unit test yang bermakna untuk fitur utama proyek Anda menggunakan pytest. Sertakan happy path dan edge cases.
9. Buatlah Dockerfile dan docker-compose.yml untuk proyek Anda. Jelaskan setiap instruksi.
10. Bandingkan 3 tren modern SE (supply chain security, green software, platform engineering). Mana yang paling relevan untuk Indonesia saat ini? Berikan alasan.
11. Buatlah API documentation untuk 5 endpoint utama proyek Anda dengan format yang profesional.
12. Analisis ekosistem karir tech di Indonesia: bandingkan kelebihan dan kekurangan bekerja di startup vs corporate vs freelance.

### Level Mahir (C5-C6)

13. Rancang rencana proyek lengkap dari Sprint 0-4 untuk "Platform E-Commerce Produk Lokal Indonesia" — termasuk user stories (15+), arsitektur, sprint backlog per sprint, risk register, dan definition of done.
14. Evaluasi proyek akhir tim Anda: apa yang berjalan baik, apa yang tidak, dan apa 5 improvement utama jika mengulang proyek? Gunakan data (velocity, coverage, burndown) untuk mendukung evaluasi.
15. Rancang personal career roadmap 5 tahun sebagai software engineer. Sertakan: skill acquisition timeline, sertifikasi target, tipe perusahaan per tahap, dan strategi networking khusus Indonesia.
16. Evaluasi pernyataan: "Platform engineering akan menggantikan kebutuhan DevOps engineer." Berikan argumen pro dan kontra berdasarkan tren industri.
17. Desain demo script profesional untuk proyek tim Anda (15 menit). Jelaskan pembagian waktu, siapa yang presentasi apa, fitur yang ditunjukkan, dan backup plan jika terjadi masalah teknis.
18. Tulis esai refleksi (300 kata): "Bagaimana Proyek Akhir IF2205 Mempersiapkan Saya Menjadi Software Engineer yang Beretika dan Profesional." Hubungkan dengan nilai amanah, itqan, dan career readiness.

---

## Rangkuman

1. **Proyek akhir** mengintegrasikan seluruh pengetahuan SE dari Bab 1-13 (requirements, design, code, test, deploy, manage) ke dalam satu web application yang functional dan deployed.
2. **Tech stack** yang digunakan (Flask + JS + SQLite + Docker + GitHub Actions) merepresentasikan tools yang dipakai di industri, memberikan pengalaman praktis yang relevan.
3. **Sprint 0-4** memberikan struktur Agile/Scrum yang nyata: dari setup (Sprint 0) → foundation (Sprint 1) → core development (Sprint 2) → quality assurance (Sprint 3) → deploy dan polish (Sprint 4).
4. **Documentation standards** (README profesional, API docs, user guide) adalah skill penting yang membedakan developer amatir dari profesional.
5. **Demo dan presentasi** melatih kemampuan komunikasi teknis — skill yang sama pentingnya dengan coding skill di industri.
6. **Supply chain security** (SBOM, Dependabot) menjadi semakin kritis karena serangan terhadap dependency semakin sering.
7. **Green software engineering** mendorong developer untuk mempertimbangkan dampak lingkungan dari kode yang ditulis.
8. **Platform engineering** menyederhanakan developer experience — dan tools seperti GitHub Codespaces dan Railway sudah memberikan taste-nya.
9. **Career roadmap** di Indonesia menawarkan banyak jalur: startup, corporate, fintech, government, freelance/remote — masing-masing dengan kelebihan dan trade-off.
10. **Portofolio** yang dibangun dari proyek akhir ini bisa menjadi aset karir pertama yang nyata — README profesional, clean git history, dan live demo URL lebih bernilai dari sertifikat semata.

---

## Referensi

1. Cohn, M. (2005). *Agile Estimating and Planning*. Prentice Hall.
2. Humble, J. & Farley, D. (2010). *Continuous Delivery*. Addison-Wesley.
3. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill.
4. GitHub Docs. (2025). *Building a portfolio with GitHub*. docs.github.com.
5. Green Software Foundation. (2024). *Software Carbon Intensity (SCI) Specification*. greensoftware.foundation.
6. OWASP Foundation. (2024). *Software Component Verification Standard (SCVS)*. owasp.org.
7. Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson. Chapter 22-24.
8. GoTo Engineering Blog. (2023). *Engineering Career Framework at GoTo*. engineering.gotocompany.com.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
