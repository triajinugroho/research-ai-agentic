# Lab 07: Database Integration dan ORM

## Informasi Praktikum

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Praktikum** | 7 dari 13 (Minggu 7) |
| **Topik** | Database Integration: SQLAlchemy ORM, Migrations, Relationships |
| **CPMK** | CPMK-4 (Mengimplementasikan komponen full-stack) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 06 (Backend Development — Flask API) selesai |
| **Sprint** | Sprint 1 — Core Features |

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. **Merancang** (*C6*) model database menggunakan SQLAlchemy ORM dengan 3 entitas (User, Buku, Peminjaman) dan relasi antar-entitas (one-to-many)
2. **Mengimplementasikan** (*C3*) database migration menggunakan Flask-Migrate (init, migrate, upgrade) untuk version control schema database
3. **Menerapkan** (*C3*) operasi CRUD melalui ORM (create, read, update, delete) menggantikan data in-memory dari Lab 06
4. **Mengintegrasikan** (*C4*) database SQLite dengan REST API endpoints sehingga data persisten antar restart server

## Konsep Singkat

### ORM dan Database dalam Arsitektur Aplikasi

Pada kuliah teori IF2205 Minggu 6 (*Desain UML dan Database*), Anda mempelajari Entity-Relationship Diagram (ERD) dan desain database. Dalam praktikum ini, kita **memetakan ERD menjadi kode Python** menggunakan SQLAlchemy ORM (Object-Relational Mapping).

```
┌──────────────────────────────────────────────────────────────────┐
│                  Dari ERD ke Kode ORM                            │
│                                                                  │
│  ERD (Desain)              SQLAlchemy (Implementasi)             │
│  ┌────────────┐            class User(db.Model):                 │
│  │   User     │                id = db.Column(Integer, PK)       │
│  │ ─────────  │                username = db.Column(String)      │
│  │ id (PK)    │                                                  │
│  │ username   │───── 1:N ─────┐                                  │
│  │ email      │               │                                  │
│  └────────────┘               │                                  │
│                               │                                  │
│  ┌────────────┐            ┌──▼───────────┐                      │
│  │   Buku     │            │  Peminjaman  │                      │
│  │ ─────────  │            │ ───────────  │                      │
│  │ id (PK)    │── 1:N ────▶│ id (PK)      │                      │
│  │ judul      │            │ user_id (FK) │                      │
│  │ pengarang  │            │ buku_id (FK) │                      │
│  └────────────┘            │ tgl_pinjam   │                      │
│                            │ tgl_kembali  │                      │
│                            │ status       │                      │
│                            └──────────────┘                      │
└──────────────────────────────────────────────────────────────────┘
```

**Konsep kunci yang dipraktikkan:**

- **ORM (Object-Relational Mapping)**: Memetakan tabel database ke class Python. Setiap instance class = satu row di tabel. Ini menghilangkan kebutuhan menulis SQL mentah dan membuat kode lebih *Pythonic*.
- **Relationships**: Relasi 1:N (one-to-many) dinyatakan dengan `db.relationship()` di sisi "one" dan `db.ForeignKey()` di sisi "many". Satu User bisa memiliki banyak Peminjaman; satu Buku bisa dipinjam banyak kali.
- **Database Migration**: Seperti version control (Git) untuk schema database. Setiap perubahan model menghasilkan migration file yang bisa di-apply (upgrade) atau di-rollback (downgrade).
- **Seed Data**: Data awal yang di-insert ke database untuk keperluan development dan testing. Memastikan database tidak kosong saat mulai develop.

| Komponen | Tanpa ORM (SQL Mentah) | Dengan ORM (SQLAlchemy) |
|----------|----------------------|------------------------|
| Buat tabel | `CREATE TABLE buku (...)` | `class Buku(db.Model):` |
| Insert | `INSERT INTO buku VALUES (...)` | `db.session.add(buku)` |
| Query | `SELECT * FROM buku WHERE id=1` | `Buku.query.get(1)` |
| Update | `UPDATE buku SET judul=... WHERE id=1` | `buku.judul = "..."; db.session.commit()` |
| Delete | `DELETE FROM buku WHERE id=1` | `db.session.delete(buku)` |
| Migration | Manual ALTER TABLE | `flask db migrate` (otomatis) |

> **Referensi Teori:** Modul IF2205 Minggu 6 — [Desain Perangkat Lunak, UML, dan Database Design](../../rekayasa-perangkat-lunak/03-modules/week-06-desain-perangkat-lunak-uml-dan-database-design.md)

## Persiapan

1. **Proyek Flask dari Lab 05-06** sudah berfungsi (app factory, Blueprint, REST API)
2. Install dependencies baru:
   ```bash
   pip install flask-sqlalchemy flask-migrate
   ```
3. Pastikan sudah membaca modul teori IF2205 Minggu 6
4. Siapkan tool database viewer (opsional): DB Browser for SQLite atau SQLite extension di VS Code

Struktur proyek yang akan kita **tambahkan** di lab ini (melanjutkan Lab 05-06):

```
perpustakaan-uai/
├── app/
│   ├── __init__.py          # UPDATE: tambah SQLAlchemy + Migrate init
│   ├── models.py            # BARU: Model User, Buku, Peminjaman
│   ├── routes/
│   │   ├── main.py          # UPDATE: gunakan database
│   │   └── books.py         # UPDATE: ganti in-memory → SQLAlchemy
│   ├── templates/           # Dari Lab 05
│   └── static/              # Dari Lab 05
├── migrations/              # BARU: auto-generated oleh Flask-Migrate
├── config.py                # Dari Lab 06 (sudah ada DATABASE_URI)
├── seed.py                  # BARU: Script untuk seed data
└── run.py                   # Dari Lab 06
```

---

## Langkah-langkah

### Langkah 1: Konfigurasi SQLAlchemy dan Flask-Migrate (10 menit)

**Mengapa langkah ini penting?** SQLAlchemy perlu diinisialisasi bersama Flask app agar bisa mengelola koneksi database. Flask-Migrate menambahkan command `flask db` untuk mengelola perubahan schema. Keduanya harus dikonfigurasi di app factory agar mendukung multi-environment (dev menggunakan file SQLite, testing menggunakan in-memory SQLite).

Update file `app/__init__.py`:

```python
# app/__init__.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inisialisasi extension di level modul (belum terikat ke app)
# Ini memungkinkan import db dari file lain (models, routes)
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name='default'):
    """
    Factory function untuk membuat instance Flask app.

    Args:
        config_name: Nama konfigurasi ('development', 'testing', 'production')

    Returns:
        Flask app instance yang sudah dikonfigurasi
    """
    app = Flask(__name__)

    # Load konfigurasi
    from config import config
    app.config.from_object(config[config_name])

    # Inisialisasi extensions dengan app
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Import models agar dikenali oleh Flask-Migrate
    from app import models  # noqa: F401

    # --- Register Blueprints ---
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    from app.routes.books import books_bp
    app.register_blueprint(books_bp)

    # --- Error Handlers ---
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'error': 'Bad Request',
            'message': str(error.description)
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'error': 'Not Found',
            'message': 'Resource yang diminta tidak ditemukan.'
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()  # Rollback jika ada transaksi gagal
        return jsonify({
            'error': 'Internal Server Error',
            'message': 'Terjadi kesalahan pada server.'
        }), 500

    return app
```

**Expected Output** — Verifikasi konfigurasi:

```bash
cd perpustakaan-uai
python -c "
from app import create_app, db
app = create_app('development')
with app.app_context():
    print('Database URI:', app.config['SQLALCHEMY_DATABASE_URI'])
    print('SQLAlchemy OK:', db is not None)
    print('App created successfully!')
"
```

```
Database URI: sqlite:///perpustakaan_dev.db
SQLAlchemy OK: True
App created successfully!
```

> **Troubleshooting:**
> - `ModuleNotFoundError: No module named 'flask_sqlalchemy'` → Jalankan `pip install flask-sqlalchemy flask-migrate`
> - `RuntimeError: Working outside of application context` → Pastikan kode database dijalankan di dalam `with app.app_context():`
> - `ImportError: cannot import name 'db'` → Pastikan `db = SQLAlchemy()` ada di level modul `__init__.py`, bukan di dalam fungsi

---

### Langkah 2: Definisikan 3 Models dengan Relationships (20 menit)

**Mengapa langkah ini penting?** Models adalah representasi tabel database dalam kode Python. Mendefinisikan relasi (1:N) secara eksplisit memungkinkan ORM menangani JOIN secara otomatis — Anda cukup akses `user.peminjaman` untuk mendapat semua peminjaman milik user tersebut, tanpa menulis SQL JOIN.

Buat file `app/models.py`:

```python
# app/models.py
"""
Database models untuk Perpustakaan Digital UAI.

Entitas:
  - User: pengguna perpustakaan (mahasiswa, dosen, staff)
  - Buku: koleksi buku perpustakaan
  - Peminjaman: transaksi peminjaman buku

Relasi:
  - User 1:N Peminjaman (satu user bisa meminjam banyak buku)
  - Buku 1:N Peminjaman (satu buku bisa dipinjam banyak kali)
"""

from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model):
    """Model untuk pengguna perpustakaan."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    nama_lengkap = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(20), default='mahasiswa')  # mahasiswa, dosen, admin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relasi: satu user bisa memiliki banyak peminjaman
    peminjaman = db.relationship('Peminjaman', backref='peminjam', lazy='dynamic')

    def set_password(self, password):
        """Hash password sebelum disimpan ke database."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifikasi password terhadap hash yang tersimpan."""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Konversi model ke dictionary untuk JSON response."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'nama_lengkap': self.nama_lengkap,
            'role': self.role,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'jumlah_peminjaman': self.peminjaman.count()
        }

    def __repr__(self):
        return f'<User {self.username}>'


class Buku(db.Model):
    """Model untuk koleksi buku perpustakaan."""
    __tablename__ = 'buku'

    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(200), nullable=False)
    pengarang = db.Column(db.String(150), nullable=False)
    tahun = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=True)
    kategori = db.Column(db.String(50), default='Umum')
    stok = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relasi: satu buku bisa memiliki banyak transaksi peminjaman
    peminjaman = db.relationship('Peminjaman', backref='buku', lazy='dynamic')

    def to_dict(self):
        """Konversi model ke dictionary untuk JSON response."""
        return {
            'id': self.id,
            'judul': self.judul,
            'pengarang': self.pengarang,
            'tahun': self.tahun,
            'isbn': self.isbn,
            'kategori': self.kategori,
            'stok': self.stok,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<Buku {self.judul}>'


class Peminjaman(db.Model):
    """
    Model untuk transaksi peminjaman buku.
    Menghubungkan User dan Buku (associative entity / junction table).
    """
    __tablename__ = 'peminjaman'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    buku_id = db.Column(db.Integer, db.ForeignKey('buku.id'), nullable=False)
    tanggal_pinjam = db.Column(db.DateTime, default=datetime.utcnow)
    tanggal_kembali = db.Column(db.DateTime, nullable=True)
    tenggat = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='dipinjam')  # dipinjam, dikembalikan, terlambat

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set tenggat otomatis 14 hari dari tanggal pinjam jika tidak diset
        if not self.tenggat:
            pinjam = self.tanggal_pinjam or datetime.utcnow()
            self.tenggat = pinjam + timedelta(days=14)

    def to_dict(self):
        """Konversi model ke dictionary untuk JSON response."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'buku_id': self.buku_id,
            'peminjam': self.peminjam.nama_lengkap if self.peminjam else None,
            'judul_buku': self.buku.judul if self.buku else None,
            'tanggal_pinjam': self.tanggal_pinjam.isoformat() if self.tanggal_pinjam else None,
            'tanggal_kembali': self.tanggal_kembali.isoformat() if self.tanggal_kembali else None,
            'tenggat': self.tenggat.isoformat() if self.tenggat else None,
            'status': self.status
        }

    def __repr__(self):
        return f'<Peminjaman {self.id}: User {self.user_id} → Buku {self.buku_id}>'
```

**Expected Output** — Verifikasi model:

```bash
python -c "
from app import create_app, db
from app.models import User, Buku, Peminjaman

app = create_app('development')
with app.app_context():
    print('Models loaded:')
    print('  User columns:', [c.name for c in User.__table__.columns])
    print('  Buku columns:', [c.name for c in Buku.__table__.columns])
    print('  Peminjaman columns:', [c.name for c in Peminjaman.__table__.columns])
"
```

```
Models loaded:
  User columns: ['id', 'username', 'email', 'password_hash', 'nama_lengkap', 'role', 'created_at']
  Buku columns: ['id', 'judul', 'pengarang', 'tahun', 'isbn', 'kategori', 'stok', 'created_at']
  Peminjaman columns: ['id', 'user_id', 'buku_id', 'tanggal_pinjam', 'tanggal_kembali', 'tenggat', 'status']
```

> **Troubleshooting:**
> - `ImportError: cannot import name 'db' from 'app'` → Pastikan `db = SQLAlchemy()` ada di `app/__init__.py` sebelum `create_app()`
> - `sqlalchemy.exc.InvalidRequestError` → Biasanya karena nama `__tablename__` duplikat atau circular import
> - `werkzeug.security not found` → Werkzeug sudah terinstal bersama Flask; jika tidak: `pip install werkzeug`

---

### Langkah 3: Jalankan Database Migration (10 menit)

**Mengapa langkah ini penting?** Migration adalah *version control* untuk database schema. Sama seperti Git menyimpan riwayat perubahan kode, Flask-Migrate menyimpan riwayat perubahan struktur tabel. Ini memungkinkan seluruh tim menerapkan perubahan database secara konsisten.

Set environment variable agar Flask mengenali app:

```bash
export FLASK_APP=run.py
```

Jalankan migration:

```bash
# Langkah 1: Inisialisasi folder migrations (hanya sekali)
flask db init
```

**Expected Output:**

```
  Creating directory /workspaces/.../perpustakaan-uai/migrations ...  done
  Creating directory /workspaces/.../perpustakaan-uai/migrations/versions ...  done
  Generating /workspaces/.../perpustakaan-uai/migrations/env.py ...  done
  Generating /workspaces/.../perpustakaan-uai/migrations/alembic.ini ...  done
  Generating /workspaces/.../perpustakaan-uai/migrations/script.py.mako ...  done
  Please edit configuration/connection/logging settings in '.../alembic.ini' before proceeding.
```

```bash
# Langkah 2: Generate migration script dari model definitions
flask db migrate -m "create user buku peminjaman tables"
```

**Expected Output:**

```
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'buku'
INFO  [alembic.autogenerate.compare] Detected added table 'users'
INFO  [alembic.autogenerate.compare] Detected added table 'peminjaman'
  Generating .../migrations/versions/xxxx_create_user_buku_peminjaman_tables.py ...  done
```

```bash
# Langkah 3: Apply migration ke database (buat tabel)
flask db upgrade
```

**Expected Output:**

```
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> xxxx, create user buku peminjaman tables
```

Verifikasi tabel sudah dibuat:

```bash
python -c "
from app import create_app, db
app = create_app('development')
with app.app_context():
    # Cek tabel yang ada di database
    inspector = db.inspect(db.engine)
    tables = inspector.get_table_names()
    print('Tables in database:', tables)
    for table in tables:
        if table != 'alembic_version':
            columns = [col['name'] for col in inspector.get_columns(table)]
            print(f'  {table}: {columns}')
"
```

**Expected Output:**

```
Tables in database: ['alembic_version', 'buku', 'peminjaman', 'users']
  buku: ['id', 'judul', 'pengarang', 'tahun', 'isbn', 'kategori', 'stok', 'created_at']
  peminjaman: ['id', 'user_id', 'buku_id', 'tanggal_pinjam', 'tanggal_kembali', 'tenggat', 'status']
  users: ['id', 'username', 'email', 'password_hash', 'nama_lengkap', 'role', 'created_at']
```

> **Troubleshooting:**
> - `Error: Could not locate a Flask application` → Pastikan `export FLASK_APP=run.py` sudah dijalankan
> - `alembic.util.exc.CommandError: Target database is not up to date` → Jalankan `flask db upgrade` dulu sebelum `flask db migrate`
> - `No changes detected` saat migrate → Pastikan `from app import models` ada di `create_app()` agar Alembic mengenali models
> - File `instance/perpustakaan_dev.db` muncul → Itu normal, itu file SQLite database Anda

---

### Langkah 4: Buat Seed Data Script (10 menit)

**Mengapa langkah ini penting?** Seed data memberi data awal yang realistis untuk development dan testing. Tanpa seed data, Anda harus membuat data manual setiap kali database di-reset — membuang waktu dan tidak konsisten.

Buat file `seed.py`:

```python
# seed.py
"""
Script untuk mengisi database dengan data awal (seed data).
Jalankan: python seed.py

Data seed:
  - 5 Users (1 admin, 2 dosen, 2 mahasiswa)
  - 10 Buku (berbagai kategori)
  - 3 Peminjaman aktif
"""

from datetime import datetime, timedelta
from app import create_app, db
from app.models import User, Buku, Peminjaman


def seed_database():
    """Mengisi database dengan data awal."""
    app = create_app('development')

    with app.app_context():
        # Hapus data lama (hati-hati di production!)
        print("Menghapus data lama...")
        Peminjaman.query.delete()
        Buku.query.delete()
        User.query.delete()
        db.session.commit()

        # ===== Seed Users =====
        print("Membuat users...")
        users = []

        admin = User(
            username='admin',
            email='admin@uai.ac.id',
            nama_lengkap='Administrator Perpustakaan',
            role='admin'
        )
        admin.set_password('admin123')
        users.append(admin)

        dosen1 = User(
            username='ahmad.fauzi',
            email='ahmad.fauzi@uai.ac.id',
            nama_lengkap='Dr. Ahmad Fauzi, M.Kom.',
            role='dosen'
        )
        dosen1.set_password('dosen123')
        users.append(dosen1)

        dosen2 = User(
            username='siti.nurhaliza',
            email='siti.nurhaliza@uai.ac.id',
            nama_lengkap='Siti Nurhaliza, S.T., M.T.',
            role='dosen'
        )
        dosen2.set_password('dosen123')
        users.append(dosen2)

        mhs1 = User(
            username='budi.santoso',
            email='budi.santoso@students.uai.ac.id',
            nama_lengkap='Budi Santoso',
            role='mahasiswa'
        )
        mhs1.set_password('mahasiswa123')
        users.append(mhs1)

        mhs2 = User(
            username='citra.dewi',
            email='citra.dewi@students.uai.ac.id',
            nama_lengkap='Citra Dewi Lestari',
            role='mahasiswa'
        )
        mhs2.set_password('mahasiswa123')
        users.append(mhs2)

        for user in users:
            db.session.add(user)
        db.session.commit()
        print(f"  {len(users)} users dibuat.")

        # ===== Seed Buku =====
        print("Membuat buku...")
        buku_list = [
            Buku(judul='Algoritma dan Pemrograman Python', pengarang='Ahmad Fauzi',
                 tahun=2024, isbn='978-602-001-001', kategori='Pemrograman', stok=3),
            Buku(judul='Rekayasa Perangkat Lunak Modern', pengarang='Budi Santoso',
                 tahun=2023, isbn='978-602-001-002', kategori='Software Engineering', stok=2),
            Buku(judul='Basis Data: Konsep dan Implementasi', pengarang='Citra Dewi',
                 tahun=2024, isbn='978-602-001-003', kategori='Database', stok=4),
            Buku(judul='Jaringan Komputer dan Internet', pengarang='Dimas Pratama',
                 tahun=2022, isbn='978-602-001-004', kategori='Jaringan', stok=2),
            Buku(judul='Kecerdasan Buatan: Teori dan Praktik', pengarang='Eka Putri',
                 tahun=2025, isbn='978-602-001-005', kategori='AI', stok=3),
            Buku(judul='Struktur Data dengan Python', pengarang='Fajar Hidayat',
                 tahun=2023, isbn='978-602-001-006', kategori='Pemrograman', stok=2),
            Buku(judul='Keamanan Sistem Informasi', pengarang='Gita Puspita',
                 tahun=2024, isbn='978-602-001-007', kategori='Keamanan', stok=1),
            Buku(judul='Machine Learning untuk Pemula', pengarang='Hendra Wijaya',
                 tahun=2025, isbn='978-602-001-008', kategori='AI', stok=3),
            Buku(judul='Pemrograman Web dengan Flask', pengarang='Indra Gunawan',
                 tahun=2024, isbn='978-602-001-009', kategori='Pemrograman', stok=2),
            Buku(judul='Matematika Diskrit untuk Informatika', pengarang='Joko Widodo',
                 tahun=2023, isbn='978-602-001-010', kategori='Matematika', stok=5),
        ]

        for buku in buku_list:
            db.session.add(buku)
        db.session.commit()
        print(f"  {len(buku_list)} buku dibuat.")

        # ===== Seed Peminjaman =====
        print("Membuat peminjaman...")

        # Ambil user dan buku yang sudah disimpan
        budi = User.query.filter_by(username='budi.santoso').first()
        citra = User.query.filter_by(username='citra.dewi').first()
        dosen = User.query.filter_by(username='ahmad.fauzi').first()

        buku1 = Buku.query.filter_by(isbn='978-602-001-001').first()
        buku3 = Buku.query.filter_by(isbn='978-602-001-003').first()
        buku5 = Buku.query.filter_by(isbn='978-602-001-005').first()

        peminjaman_list = [
            Peminjaman(
                user_id=budi.id,
                buku_id=buku1.id,
                tanggal_pinjam=datetime.utcnow() - timedelta(days=7),
                status='dipinjam'
            ),
            Peminjaman(
                user_id=citra.id,
                buku_id=buku3.id,
                tanggal_pinjam=datetime.utcnow() - timedelta(days=3),
                status='dipinjam'
            ),
            Peminjaman(
                user_id=dosen.id,
                buku_id=buku5.id,
                tanggal_pinjam=datetime.utcnow() - timedelta(days=20),
                tanggal_kembali=datetime.utcnow() - timedelta(days=6),
                status='dikembalikan'
            ),
        ]

        for p in peminjaman_list:
            db.session.add(p)
        db.session.commit()
        print(f"  {len(peminjaman_list)} peminjaman dibuat.")

        # ===== Verifikasi =====
        print("\n=== Verifikasi Seed Data ===")
        print(f"Total Users:      {User.query.count()}")
        print(f"Total Buku:       {Buku.query.count()}")
        print(f"Total Peminjaman: {Peminjaman.query.count()}")

        print("\nDaftar Users:")
        for u in User.query.all():
            print(f"  - {u.username} ({u.role}) — {u.email}")

        print("\nDaftar Buku:")
        for b in Buku.query.all():
            print(f"  - [{b.id}] {b.judul} ({b.pengarang}, {b.tahun}) — stok: {b.stok}")

        print("\nDaftar Peminjaman:")
        for p in Peminjaman.query.all():
            print(f"  - {p.peminjam.nama_lengkap} meminjam '{p.buku.judul}' — status: {p.status}")

        print("\n✓ Seed data berhasil!")


if __name__ == '__main__':
    seed_database()
```

**Expected Output:**

```bash
python seed.py
```

```
Menghapus data lama...
Membuat users...
  5 users dibuat.
Membuat buku...
  10 buku dibuat.
Membuat peminjaman...
  3 peminjaman dibuat.

=== Verifikasi Seed Data ===
Total Users:      5
Total Buku:       10
Total Peminjaman: 3

Daftar Users:
  - admin (admin) — admin@uai.ac.id
  - ahmad.fauzi (dosen) — ahmad.fauzi@uai.ac.id
  - siti.nurhaliza (dosen) — siti.nurhaliza@uai.ac.id
  - budi.santoso (mahasiswa) — budi.santoso@students.uai.ac.id
  - citra.dewi (mahasiswa) — citra.dewi@students.uai.ac.id

Daftar Buku:
  - [1] Algoritma dan Pemrograman Python (Ahmad Fauzi, 2024) — stok: 3
  - [2] Rekayasa Perangkat Lunak Modern (Budi Santoso, 2023) — stok: 2
  ...

Daftar Peminjaman:
  - Budi Santoso meminjam 'Algoritma dan Pemrograman Python' — status: dipinjam
  - Citra Dewi Lestari meminjam 'Basis Data: Konsep dan Implementasi' — status: dipinjam
  - Dr. Ahmad Fauzi, M.Kom. meminjam 'Kecerdasan Buatan: Teori dan Praktik' — status: dikembalikan

✓ Seed data berhasil!
```

> **Troubleshooting:**
> - `sqlalchemy.exc.OperationalError: no such table` → Pastikan `flask db upgrade` sudah dijalankan sebelum seed
> - `IntegrityError: UNIQUE constraint failed` → Jalankan seed ulang; script sudah menghapus data lama
> - `AttributeError: 'NoneType' object has no attribute 'id'` → User/buku tidak ditemukan; pastikan seed users dan buku di-commit sebelum membuat peminjaman

---

### Langkah 5: Update API Endpoints — Ganti In-Memory dengan Database (20 menit)

**Mengapa langkah ini penting?** Ini adalah langkah transformatif — API yang tadinya menggunakan list Python (data hilang saat restart) sekarang menggunakan database persisten. Pola operasi ORM (query, add, commit, delete) menggantikan operasi list.

Update file `app/routes/books.py`:

```python
# app/routes/books.py
"""
REST API Blueprint untuk resource Buku.
UPDATED di Lab 07: Menggunakan SQLAlchemy ORM (menggantikan data in-memory Lab 06).

Endpoint:
  GET    /api/buku            → Ambil semua buku (dengan pagination)
  GET    /api/buku/<id>       → Ambil satu buku
  POST   /api/buku            → Tambah buku baru
  PUT    /api/buku/<id>       → Update buku
  DELETE /api/buku/<id>       → Hapus buku
"""

from flask import Blueprint, jsonify, request
from app import db
from app.models import Buku

books_bp = Blueprint('books', __name__)


def _validate_buku_data(data, is_update=False):
    """
    Validasi input data buku.
    Args:
        data: Dictionary dari request JSON
        is_update: True jika ini operasi update (field tidak wajib semua ada)
    Returns:
        tuple (is_valid, error_message)
    """
    if not is_update:
        required_fields = ['judul', 'pengarang', 'tahun']
        missing = [f for f in required_fields if f not in data or not data[f]]
        if missing:
            return False, f"Field berikut wajib diisi: {', '.join(missing)}"

    # Validasi tahun jika ada
    if 'tahun' in data:
        try:
            tahun = int(data['tahun'])
            if tahun < 1900 or tahun > 2030:
                return False, "Tahun harus antara 1900 dan 2030"
        except (ValueError, TypeError):
            return False, "Tahun harus berupa angka"

    # Validasi judul jika ada
    if 'judul' in data and len(str(data['judul']).strip()) < 3:
        return False, "Judul minimal 3 karakter"

    # Validasi stok jika ada
    if 'stok' in data:
        try:
            stok = int(data['stok'])
            if stok < 0:
                return False, "Stok tidak boleh negatif"
        except (ValueError, TypeError):
            return False, "Stok harus berupa angka"

    return True, ""


# ----- GET /api/buku — Ambil semua buku (dengan pagination) -----
@books_bp.route('/api/buku', methods=['GET'])
def get_all_buku():
    """
    Mengambil daftar buku dengan pagination.
    Query params: page (default=1), per_page (default=10)
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    # Batasi per_page maksimal 50
    per_page = min(per_page, 50)

    # Query dengan pagination
    pagination = Buku.query.order_by(Buku.id).paginate(
        page=page, per_page=per_page, error_out=False
    )

    buku_list = [buku.to_dict() for buku in pagination.items]

    return jsonify({
        'status': 'success',
        'count': len(buku_list),
        'data': buku_list,
        'pagination': {
            'page': pagination.page,
            'per_page': pagination.per_page,
            'total': pagination.total,
            'total_pages': pagination.pages,
            'has_next': pagination.has_next,
            'has_prev': pagination.has_prev
        }
    }), 200


# ----- GET /api/buku/<id> — Ambil satu buku -----
@books_bp.route('/api/buku/<int:buku_id>', methods=['GET'])
def get_buku(buku_id):
    """Mengambil satu buku berdasarkan ID."""
    buku = db.session.get(Buku, buku_id)

    if buku is None:
        return jsonify({
            'status': 'error',
            'message': f'Buku dengan ID {buku_id} tidak ditemukan'
        }), 404

    return jsonify({
        'status': 'success',
        'data': buku.to_dict()
    }), 200


# ----- POST /api/buku — Tambah buku baru -----
@books_bp.route('/api/buku', methods=['POST'])
def create_buku():
    """Menambahkan buku baru ke database."""
    if not request.is_json:
        return jsonify({
            'status': 'error',
            'message': 'Content-Type harus application/json'
        }), 400

    data = request.get_json()

    # Validasi input
    is_valid, error_msg = _validate_buku_data(data)
    if not is_valid:
        return jsonify({
            'status': 'error',
            'message': error_msg
        }), 400

    # Cek duplikasi ISBN jika disertakan
    isbn = data.get('isbn')
    if isbn:
        existing = Buku.query.filter_by(isbn=isbn).first()
        if existing:
            return jsonify({
                'status': 'error',
                'message': f'Buku dengan ISBN {isbn} sudah ada'
            }), 400

    # Buat instance Buku baru
    buku_baru = Buku(
        judul=str(data['judul']).strip(),
        pengarang=str(data['pengarang']).strip(),
        tahun=int(data['tahun']),
        isbn=isbn,
        kategori=data.get('kategori', 'Umum'),
        stok=int(data.get('stok', 1))
    )

    db.session.add(buku_baru)
    db.session.commit()

    return jsonify({
        'status': 'success',
        'message': 'Buku berhasil ditambahkan',
        'data': buku_baru.to_dict()
    }), 201


# ----- PUT /api/buku/<id> — Update buku -----
@books_bp.route('/api/buku/<int:buku_id>', methods=['PUT'])
def update_buku(buku_id):
    """Mengupdate data buku yang sudah ada."""
    buku = db.session.get(Buku, buku_id)

    if buku is None:
        return jsonify({
            'status': 'error',
            'message': f'Buku dengan ID {buku_id} tidak ditemukan'
        }), 404

    if not request.is_json:
        return jsonify({
            'status': 'error',
            'message': 'Content-Type harus application/json'
        }), 400

    data = request.get_json()

    # Validasi
    updatable_fields = ['judul', 'pengarang', 'tahun', 'isbn', 'kategori', 'stok']
    has_update = any(f in data for f in updatable_fields)

    if not has_update:
        return jsonify({
            'status': 'error',
            'message': f'Minimal satu field harus diupdate: {", ".join(updatable_fields)}'
        }), 400

    is_valid, error_msg = _validate_buku_data(data, is_update=True)
    if not is_valid:
        return jsonify({
            'status': 'error',
            'message': error_msg
        }), 400

    # Update field yang diberikan
    if 'judul' in data:
        buku.judul = str(data['judul']).strip()
    if 'pengarang' in data:
        buku.pengarang = str(data['pengarang']).strip()
    if 'tahun' in data:
        buku.tahun = int(data['tahun'])
    if 'isbn' in data:
        buku.isbn = data['isbn']
    if 'kategori' in data:
        buku.kategori = str(data['kategori']).strip()
    if 'stok' in data:
        buku.stok = int(data['stok'])

    db.session.commit()

    return jsonify({
        'status': 'success',
        'message': 'Buku berhasil diupdate',
        'data': buku.to_dict()
    }), 200


# ----- DELETE /api/buku/<id> — Hapus buku -----
@books_bp.route('/api/buku/<int:buku_id>', methods=['DELETE'])
def delete_buku(buku_id):
    """Menghapus buku dari database."""
    buku = db.session.get(Buku, buku_id)

    if buku is None:
        return jsonify({
            'status': 'error',
            'message': f'Buku dengan ID {buku_id} tidak ditemukan'
        }), 404

    # Cek apakah buku sedang dipinjam
    aktif = buku.peminjaman.filter_by(status='dipinjam').count()
    if aktif > 0:
        return jsonify({
            'status': 'error',
            'message': f'Buku "{buku.judul}" sedang dipinjam oleh {aktif} orang. Tidak bisa dihapus.'
        }), 400

    judul = buku.judul
    db.session.delete(buku)
    db.session.commit()

    return jsonify({
        'status': 'success',
        'message': f'Buku "{judul}" berhasil dihapus'
    }), 200
```

**Expected Output** — Jalankan server dan test:

```bash
python run.py &

# GET semua buku (dengan pagination)
curl -s "http://127.0.0.1:5000/api/buku?page=1&per_page=5" | python -m json.tool
```

```json
{
    "status": "success",
    "count": 5,
    "data": [
        {
            "id": 1,
            "judul": "Algoritma dan Pemrograman Python",
            "pengarang": "Ahmad Fauzi",
            "tahun": 2024,
            "isbn": "978-602-001-001",
            "kategori": "Pemrograman",
            "stok": 3,
            "created_at": "2026-04-11T..."
        },
        ...
    ],
    "pagination": {
        "page": 1,
        "per_page": 5,
        "total": 10,
        "total_pages": 2,
        "has_next": true,
        "has_prev": false
    }
}
```

```bash
# Test pagination halaman 2
curl -s "http://127.0.0.1:5000/api/buku?page=2&per_page=5" | python -m json.tool
```

Expected: 5 buku berikutnya, `has_prev: true`, `has_next: false`.

> **Troubleshooting:**
> - `OperationalError: no such table: buku` → Jalankan `flask db upgrade` dan `python seed.py`
> - `DetachedInstanceError` → Pastikan semua akses ke model terjadi di dalam application context
> - Data lama dari Lab 06 masih muncul → Pastikan tidak ada variabel `_buku_data` di file routes yang baru

---

### Langkah 6: Update Route Frontend untuk Menggunakan Database (10 menit)

**Mengapa langkah ini penting?** Halaman web (dari Lab 05) juga perlu mengambil data dari database, bukan dari list Python. Ini memastikan data yang ditampilkan di frontend konsisten dengan yang dikembalikan oleh API.

Update file `app/routes/main.py`:

```python
# app/routes/main.py
"""
Route handlers untuk halaman web (frontend views).
UPDATED di Lab 07: Menggunakan database queries.
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db
from app.models import User, Buku

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Halaman utama Perpustakaan Digital UAI."""
    jumlah_buku = Buku.query.count()
    buku_terbaru = Buku.query.order_by(Buku.tahun.desc()).limit(3).all()

    # Hitung jumlah kategori unik
    kategori = db.session.query(Buku.kategori).distinct().count()

    return render_template('index.html',
                           jumlah_buku=jumlah_buku,
                           jumlah_kategori=kategori,
                           buku_terbaru=buku_terbaru)


@main_bp.route('/books')
def books():
    """Halaman daftar semua buku."""
    buku_list = Buku.query.order_by(Buku.id).all()
    return render_template('books.html', buku_list=buku_list)


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Halaman login pengguna."""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            flash('Username dan password harus diisi!', 'error')
        else:
            # Cek di database (bukan hardcoded lagi!)
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                flash(f'Selamat datang, {user.nama_lengkap}!', 'success')
                return redirect(url_for('main.index'))
            else:
                flash('Username atau password salah!', 'error')

    return render_template('login.html')
```

Perlu juga update sedikit `app/templates/index.html` untuk menggunakan data dari database (karena sekarang `buku_terbaru` adalah model object, bukan dictionary):

Update bagian stats di `index.html` — ganti `5` dengan `{{ jumlah_kategori }}`:

```html
<!-- Di section stats index.html, ganti angka hardcoded: -->
<div class="stat-card">
    <h3>{{ jumlah_kategori }}</h3>
    <p>Kategori</p>
</div>
```

Dan update bagian card karena sekarang objek Buku (bukan dict):

```html
<!-- Di section buku terbaru index.html, akses atribut langsung: -->
{% for buku in buku_terbaru %}
<div class="card">
    <div class="card-body">
        <h3 class="card-title">{{ buku.judul }}</h3>
        <p class="card-text">Pengarang: {{ buku.pengarang }}</p>
        <p class="card-text">Tahun: {{ buku.tahun }}</p>
        <span class="badge">{{ buku.kategori }}</span>
    </div>
</div>
{% endfor %}
```

**Expected Output** — Buka `http://127.0.0.1:5000/`:

- Statistik menampilkan: Total Buku: **10**, Kategori: **7** (dari database)
- Buku terbaru: 3 buku dengan tahun terbesar
- Login dengan `admin` / `admin123` → "Selamat datang, Administrator Perpustakaan!"
- Login dengan `budi.santoso` / `mahasiswa123` → "Selamat datang, Budi Santoso!"

> **Troubleshooting:**
> - `jinja2.exceptions.UndefinedError: 'dict object' has no attribute...` → Anda masih menggunakan template Lab 05 yang mengakses data sebagai dictionary; model objects diakses dengan dot notation (`buku.judul`), bukan bracket (`buku['judul']`)
> - Data berbeda antara halaman web dan API → Pastikan keduanya mengambil dari model yang sama (`Buku.query...`)

---

### Langkah 7: Test Integrasi Database dan Commit (10 menit)

**Mengapa langkah ini penting?** Verifikasi menyeluruh memastikan database terintegrasi dengan benar ke semua komponen (API endpoints, halaman web, relasi antar model).

**Test relasi antar model:**

```bash
python -c "
from app import create_app, db
from app.models import User, Buku, Peminjaman

app = create_app('development')
with app.app_context():
    # Test relasi: User → Peminjaman
    budi = User.query.filter_by(username='budi.santoso').first()
    print(f'User: {budi.nama_lengkap}')
    print(f'Jumlah peminjaman: {budi.peminjaman.count()}')
    for p in budi.peminjaman.all():
        print(f'  Meminjam: {p.buku.judul} (status: {p.status})')

    print()

    # Test relasi: Buku → Peminjaman
    buku = Buku.query.first()
    print(f'Buku: {buku.judul}')
    print(f'Jumlah kali dipinjam: {buku.peminjaman.count()}')

    print()

    # Test query: buku berdasarkan kategori
    pemrograman = Buku.query.filter_by(kategori='Pemrograman').all()
    print(f'Buku kategori Pemrograman: {len(pemrograman)}')
    for b in pemrograman:
        print(f'  - {b.judul} ({b.tahun})')
"
```

**Expected Output:**

```
User: Budi Santoso
Jumlah peminjaman: 1
  Meminjam: Algoritma dan Pemrograman Python (status: dipinjam)

Buku: Algoritma dan Pemrograman Python
Jumlah kali dipinjam: 1

Buku kategori Pemrograman: 3
  - Algoritma dan Pemrograman Python (2024)
  - Struktur Data dengan Python (2023)
  - Pemrograman Web dengan Flask (2024)
```

**Test API endpoints dengan data dari database:**

```bash
# Test CRUD lengkap
echo "=== GET semua buku ==="
curl -s "http://127.0.0.1:5000/api/buku" | python -m json.tool | head -5

echo "=== POST buku baru ==="
curl -s -X POST http://127.0.0.1:5000/api/buku \
  -H "Content-Type: application/json" \
  -d '{"judul": "Cloud Computing Fundamentals", "pengarang": "Rani Kusuma", "tahun": 2025, "isbn": "978-602-001-011", "kategori": "Cloud", "stok": 2}' \
  | python -m json.tool

echo "=== GET buku baru (ID 11) ==="
curl -s http://127.0.0.1:5000/api/buku/11 | python -m json.tool

echo "=== PUT update stok ==="
curl -s -X PUT http://127.0.0.1:5000/api/buku/11 \
  -H "Content-Type: application/json" \
  -d '{"stok": 5}' \
  | python -m json.tool

echo "=== DELETE buku 11 ==="
curl -s -X DELETE http://127.0.0.1:5000/api/buku/11 | python -m json.tool

echo "=== DELETE buku yang sedang dipinjam (harus gagal) ==="
curl -s -X DELETE http://127.0.0.1:5000/api/buku/1 | python -m json.tool
```

**Expected Output untuk delete buku yang sedang dipinjam:**

```json
{
    "status": "error",
    "message": "Buku \"Algoritma dan Pemrograman Python\" sedang dipinjam oleh 1 orang. Tidak bisa dihapus."
}
```

**Commit ke Git:**

```bash
git add .
git commit -m "feat(database): integrate SQLAlchemy ORM with Flask API

- Add 3 models: User, Buku, Peminjaman with 1:N relationships
- Add Flask-Migrate for database version control
- Add seed.py with 5 users, 10 books, 3 loans
- Update API endpoints to use SQLAlchemy queries (replace in-memory)
- Add pagination support (page, per_page) to GET /api/buku
- Add ISBN uniqueness check and active loan protection on delete
- Update frontend routes to query database"
```

---

## Tantangan Tambahan

### Level 1 — Basic
Tambahkan endpoint **GET `/api/buku/search?q=<keyword>`** yang mencari buku berdasarkan judul atau pengarang menggunakan SQLAlchemy `ilike()`. Kembalikan hasil dengan pagination.

```python
# Hint:
results = Buku.query.filter(
    db.or_(
        Buku.judul.ilike(f'%{query}%'),
        Buku.pengarang.ilike(f'%{query}%')
    )
).paginate(page=page, per_page=per_page)
```

### Level 2 — Intermediate
Buat **Blueprint baru** untuk endpoint Peminjaman (`/api/peminjaman`) dengan minimal 3 endpoints:
- `POST /api/peminjaman` — Buat peminjaman baru (kurangi stok buku)
- `PUT /api/peminjaman/<id>/kembalikan` — Kembalikan buku (update status, set tanggal_kembali, tambah stok)
- `GET /api/peminjaman?user_id=<id>` — Lihat peminjaman user tertentu

### Level 3 — Advanced
Implementasikan **eager loading** menggunakan `joinedload` untuk menghindari N+1 query problem. Buat endpoint `GET /api/peminjaman/detail` yang mengembalikan data peminjaman beserta detail user dan buku dalam satu query, lalu bandingkan jumlah SQL query sebelum dan sesudah optimisasi menggunakan `SQLALCHEMY_ECHO = True`.

```python
# Hint:
from sqlalchemy.orm import joinedload

peminjaman = Peminjaman.query.options(
    joinedload(Peminjaman.peminjam),
    joinedload(Peminjaman.buku)
).all()
```

---

## Refleksi & AI Usage Log

Setelah menyelesaikan praktikum, jawab pertanyaan refleksi berikut:

1. Apa keuntungan menggunakan ORM dibanding menulis SQL mentah? Apakah ada kekurangannya?
2. Mengapa migration penting dalam pengembangan tim? Apa yang terjadi jika setiap developer mengubah schema langsung tanpa migration?
3. Bagaimana relasi 1:N antara User dan Peminjaman memudahkan query data?
4. Bagaimana perubahan dari data in-memory (Lab 06) ke database (Lab 07) mempengaruhi persistensi dan reliabilitas data?

### AI Usage Log

| No | Prompt/Pertanyaan ke AI | Tool | Output yang Digunakan | Modifikasi yang Dilakukan | Pemahaman (1-5) |
|----|-------------------------|------|----------------------|---------------------------|-----------------|
| 1  | Contoh: "Cara membuat relasi one-to-many di SQLAlchemy" | Claude | Contoh `db.relationship()` + `ForeignKey` | Menyesuaikan nama kolom dan backref | 4 |
| 2  | | | | | |
| 3  | | | | | |

> **Catatan:** Penggunaan AI sebagai *learning partner* diperbolehkan. Yang **tidak** diperbolehkan adalah meng-copy seluruh kode tanpa memahami logikanya. Tulis refleksi jujur tentang kontribusi AI vs pemahaman mandiri Anda.

---

## Checklist Penyelesaian

- [ ] Flask-SQLAlchemy dan Flask-Migrate terinstal dan terkonfigurasi di app factory
- [ ] Model `User` dengan field (username, email, password_hash, nama_lengkap, role) dan method `set_password()`, `check_password()`
- [ ] Model `Buku` dengan field (judul, pengarang, tahun, isbn, kategori, stok) dan method `to_dict()`
- [ ] Model `Peminjaman` dengan foreign keys (user_id, buku_id) dan field status
- [ ] Relasi 1:N: User → Peminjaman dan Buku → Peminjaman berfungsi
- [ ] Migration berhasil: `flask db init`, `flask db migrate`, `flask db upgrade` tanpa error
- [ ] `seed.py` berjalan dan mengisi database dengan 5 users, 10 buku, 3 peminjaman
- [ ] API GET `/api/buku` mengembalikan data dari database dengan pagination
- [ ] API POST `/api/buku` menyimpan buku baru ke database secara persisten
- [ ] API PUT `/api/buku/<id>` mengupdate data di database
- [ ] API DELETE `/api/buku/<id>` menghapus dari database (dengan proteksi buku yang sedang dipinjam)
- [ ] Halaman web (frontend) menampilkan data dari database
- [ ] Login menggunakan data user dari database (bukan hardcoded)
- [ ] Kode di-commit ke Git dengan pesan commit yang deskriptif
- [ ] AI Usage Log diisi untuk sesi ini

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
