# Lab 06: Backend Development — Python Flask REST API

## Informasi Praktikum

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Praktikum** | 6 dari 13 (Minggu 6) |
| **Topik** | Backend Development: Flask REST API, Blueprints, Error Handling |
| **CPMK** | CPMK-4 (Mengimplementasikan komponen full-stack) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 05 (Frontend Development) selesai |
| **Sprint** | Sprint 0 — Foundation |

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. **Membangun** (*C6*) Flask application menggunakan factory pattern dengan konfigurasi multi-environment (development, testing, production)
2. **Mengimplementasikan** (*C3*) 5 REST API endpoints untuk resource Buku dengan HTTP methods yang tepat (GET, POST, PUT, DELETE)
3. **Menerapkan** (*C3*) proper HTTP status codes (200, 201, 400, 404, 500), JSON request/response handling, dan error handlers
4. **Menguji** (*C4*) API endpoints menggunakan curl dan memverifikasi response sesuai standar REST

## Konsep Singkat

### REST API dan Arsitektur Backend

Pada kuliah teori IF2205 Minggu 6 (*Desain UML dan Database*), Anda telah mempelajari bagaimana merancang komponen sistem menggunakan UML dan mendesain API. Dalam praktikum ini, kita mengimplementasikan desain tersebut menjadi **REST API** yang nyata menggunakan Flask.

```
┌─────────────────────────────────────────────────────────────┐
│                    REST API Architecture                     │
│                                                             │
│  Client (Browser/Postman/curl)                              │
│       │                                                     │
│       │  HTTP Request                                       │
│       │  GET /api/buku                                      │
│       │  Content-Type: application/json                     │
│       ▼                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────┐ │
│  │   Flask App   │→│  Blueprint    │→│  Route Handler     │ │
│  │  (Factory)    │  │  (books_bp)  │  │  get_all_books()  │ │
│  └──────────────┘  └──────────────┘  └───────────────────┘ │
│       │                                      │              │
│       │  Config (dev/test/prod)               │  JSON        │
│       │                                      ▼              │
│  ┌──────────────┐                   ┌───────────────────┐  │
│  │  config.py    │                   │  HTTP Response     │  │
│  │  SECRET_KEY   │                   │  200 OK            │  │
│  │  DATABASE_URI │                   │  {"buku": [...]}   │  │
│  └──────────────┘                   └───────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**Konsep kunci yang dipraktikkan:**

- **REST (Representational State Transfer)**: Arsitektur API yang menggunakan HTTP methods (GET, POST, PUT, DELETE) untuk operasi CRUD pada resource. Setiap endpoint merepresentasikan sebuah resource (noun), bukan aksi (verb).
- **Blueprint**: Cara Flask mengorganisasi routes ke dalam modul terpisah. Analoginya seperti *package* di Java — mengelompokkan fungsionalitas terkait.
- **Factory Pattern**: `create_app()` memungkinkan pembuatan instance app dengan konfigurasi berbeda (dev vs test vs production). Pattern ini akan krusial saat testing di Lab 09.
- **HTTP Status Codes**: Bahasa universal antara client dan server — `200` (OK), `201` (Created), `400` (Bad Request), `404` (Not Found), `500` (Internal Server Error).

| Method | Endpoint | Aksi | Status Code |
|--------|----------|------|-------------|
| GET | `/api/buku` | Ambil semua buku | 200 |
| GET | `/api/buku/<id>` | Ambil satu buku | 200 / 404 |
| POST | `/api/buku` | Tambah buku baru | 201 / 400 |
| PUT | `/api/buku/<id>` | Update buku | 200 / 404 / 400 |
| DELETE | `/api/buku/<id>` | Hapus buku | 200 / 404 |

> **Referensi Teori:** Modul IF2205 Minggu 6 — [Desain UML dan Database](../../rekayasa-perangkat-lunak/03-modules/week-06-desain-perangkat-lunak-uml-dan-database-design.md)

## Persiapan

1. **Proyek Flask dari Lab 05** sudah berfungsi (app factory, templates, static files)
2. Install dependency tambahan:
   ```bash
   pip install flask-cors
   ```
3. Pastikan sudah membaca modul teori IF2205 Minggu 6
4. Siapkan terminal kedua untuk menjalankan `curl` commands

Struktur proyek yang akan kita **tambahkan** di lab ini (melanjutkan Lab 05):

```
perpustakaan-uai/
├── app/
│   ├── __init__.py          # UPDATE: tambah konfigurasi + error handlers
│   ├── routes/
│   │   ├── main.py          # Dari Lab 05 (halaman web)
│   │   └── books.py         # BARU: REST API endpoints untuk Buku
│   ├── templates/           # Dari Lab 05
│   └── static/              # Dari Lab 05
├── config.py                # BARU: Multi-environment configuration
└── run.py                   # UPDATE: gunakan config
```

---

## Langkah-langkah

### Langkah 1: Buat Konfigurasi Multi-Environment (10 menit)

**Mengapa langkah ini penting?** Aplikasi yang sama perlu perilaku berbeda di lingkungan yang berbeda. Di *development* kita ingin debug mode aktif; di *testing* kita gunakan database terpisah; di *production* kita matikan debug dan gunakan secret key yang kuat. Ini mengikuti prinsip *Twelve-Factor App*.

Buat file `config.py`:

```python
# config.py
"""
Konfigurasi multi-environment untuk Perpustakaan Digital UAI.
Setiap environment (dev, test, prod) memiliki setting yang berbeda.
"""

import os


class Config:
    """Konfigurasi dasar yang dipakai semua environment."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'kunci-rahasia-default-ganti-di-production')
    # Database URI akan ditambahkan di Lab 07
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///perpustakaan.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Konfigurasi untuk development — debug aktif."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///perpustakaan_dev.db'


class TestingConfig(Config):
    """Konfigurasi untuk testing — database terpisah di memory."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
    """Konfigurasi untuk production — debug mati, key dari env."""
    DEBUG = False


# Dictionary untuk memilih konfigurasi berdasarkan nama
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

Update `run.py` untuk menggunakan konfigurasi:

```python
# run.py
from app import create_app

app = create_app('development')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

**Expected Output:**

```bash
python -c "from config import config; print(list(config.keys()))"
# Output: ['development', 'testing', 'production', 'default']
```

> **Troubleshooting:**
> - `ImportError: cannot import name 'config'` → Pastikan `config.py` ada di root proyek (sejajar dengan `run.py`), bukan di dalam folder `app/`
> - `os.environ.get()` mengembalikan `None` → Itu normal di development; kita gunakan default value sebagai fallback

---

### Langkah 2: Update App Factory dengan Konfigurasi dan Error Handlers (10 menit)

**Mengapa langkah ini penting?** App factory yang menerima parameter konfigurasi memungkinkan kita membuat instance app yang berbeda untuk development dan testing. Error handlers memberikan response JSON yang konsisten saat terjadi kesalahan — bukan halaman HTML error default Flask.

Update file `app/__init__.py`:

```python
# app/__init__.py
from flask import Flask, jsonify
from flask_cors import CORS


def create_app(config_name='default'):
    """
    Factory function untuk membuat instance Flask app.

    Args:
        config_name: Nama konfigurasi ('development', 'testing', 'production')

    Returns:
        Flask app instance yang sudah dikonfigurasi
    """
    app = Flask(__name__)

    # Load konfigurasi dari config.py
    from config import config
    app.config.from_object(config[config_name])

    # Enable CORS untuk semua route API
    # Ini memungkinkan frontend di domain berbeda mengakses API
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # --- Register Blueprints ---
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    from app.routes.books import books_bp
    app.register_blueprint(books_bp)

    # --- Error Handlers (JSON response) ---
    @app.errorhandler(400)
    def bad_request(error):
        """Handler untuk request yang tidak valid."""
        return jsonify({
            'error': 'Bad Request',
            'message': str(error.description)
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        """Handler untuk resource yang tidak ditemukan."""
        return jsonify({
            'error': 'Not Found',
            'message': 'Resource yang diminta tidak ditemukan.'
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        """Handler untuk kesalahan internal server."""
        return jsonify({
            'error': 'Internal Server Error',
            'message': 'Terjadi kesalahan pada server. Silakan coba lagi.'
        }), 500

    return app
```

**Expected Output** — Test error handler:

```bash
python run.py &
curl -s http://127.0.0.1:5000/api/halaman-tidak-ada | python -m json.tool
```

```json
{
    "error": "Not Found",
    "message": "Resource yang diminta tidak ditemukan."
}
```

> **Troubleshooting:**
> - `ModuleNotFoundError: No module named 'flask_cors'` → Jalankan `pip install flask-cors`
> - Error handler tidak bekerja untuk route API → Pastikan route yang gagal mengembalikan response, bukan raise exception tanpa handler
> - `ImportError: cannot import name 'books_bp'` → File `app/routes/books.py` belum dibuat; buat dulu di Langkah 3

---

### Langkah 3: Buat Blueprint REST API untuk Buku (20 menit)

**Mengapa langkah ini penting?** Ini adalah inti dari lab ini — mengimplementasikan 5 REST endpoints yang mengikuti konvensi standar. Setiap endpoint menangani satu operasi CRUD dan mengembalikan response JSON dengan status code yang tepat.

Buat file `app/routes/books.py`:

```python
# app/routes/books.py
"""
REST API Blueprint untuk resource Buku.
Endpoint mengikuti konvensi RESTful:
  GET    /api/buku       → Ambil semua buku
  GET    /api/buku/<id>  → Ambil satu buku
  POST   /api/buku       → Tambah buku baru
  PUT    /api/buku/<id>  → Update buku
  DELETE /api/buku/<id>  → Hapus buku
"""

from flask import Blueprint, jsonify, request, abort

books_bp = Blueprint('books', __name__)

# Data in-memory (akan diganti dengan database di Lab 07)
_buku_data = [
    {
        'id': 1,
        'judul': 'Algoritma dan Pemrograman Python',
        'pengarang': 'Ahmad Fauzi',
        'tahun': 2024,
        'isbn': '978-602-001-001',
        'kategori': 'Pemrograman'
    },
    {
        'id': 2,
        'judul': 'Rekayasa Perangkat Lunak Modern',
        'pengarang': 'Budi Santoso',
        'tahun': 2023,
        'isbn': '978-602-001-002',
        'kategori': 'Software Engineering'
    },
    {
        'id': 3,
        'judul': 'Basis Data: Konsep dan Implementasi',
        'pengarang': 'Citra Dewi',
        'tahun': 2024,
        'isbn': '978-602-001-003',
        'kategori': 'Database'
    },
    {
        'id': 4,
        'judul': 'Jaringan Komputer dan Internet',
        'pengarang': 'Dimas Pratama',
        'tahun': 2022,
        'isbn': '978-602-001-004',
        'kategori': 'Jaringan'
    },
    {
        'id': 5,
        'judul': 'Kecerdasan Buatan: Teori dan Praktik',
        'pengarang': 'Eka Putri',
        'tahun': 2025,
        'isbn': '978-602-001-005',
        'kategori': 'AI'
    },
]

_next_id = 6  # ID berikutnya untuk buku baru


def _validate_buku_data(data):
    """
    Validasi input data buku.
    Mengembalikan tuple (is_valid, error_message).
    """
    required_fields = ['judul', 'pengarang', 'tahun']

    # Cek field yang wajib ada
    missing = [f for f in required_fields if f not in data or not data[f]]
    if missing:
        return False, f"Field berikut wajib diisi: {', '.join(missing)}"

    # Validasi tahun (harus integer, antara 1900-2030)
    try:
        tahun = int(data['tahun'])
        if tahun < 1900 or tahun > 2030:
            return False, "Tahun harus antara 1900 dan 2030"
    except (ValueError, TypeError):
        return False, "Tahun harus berupa angka"

    # Validasi panjang judul
    if len(str(data['judul']).strip()) < 3:
        return False, "Judul minimal 3 karakter"

    return True, ""


# ----- Endpoint 1: GET /api/buku — Ambil semua buku -----
@books_bp.route('/api/buku', methods=['GET'])
def get_all_buku():
    """
    Mengambil daftar semua buku.
    Response: JSON array dari semua buku dengan status 200.
    """
    return jsonify({
        'status': 'success',
        'count': len(_buku_data),
        'data': _buku_data
    }), 200


# ----- Endpoint 2: GET /api/buku/<id> — Ambil satu buku -----
@books_bp.route('/api/buku/<int:buku_id>', methods=['GET'])
def get_buku(buku_id):
    """
    Mengambil satu buku berdasarkan ID.
    Response: JSON object buku (200) atau error (404).
    """
    buku = next((b for b in _buku_data if b['id'] == buku_id), None)

    if buku is None:
        return jsonify({
            'status': 'error',
            'message': f'Buku dengan ID {buku_id} tidak ditemukan'
        }), 404

    return jsonify({
        'status': 'success',
        'data': buku
    }), 200


# ----- Endpoint 3: POST /api/buku — Tambah buku baru -----
@books_bp.route('/api/buku', methods=['POST'])
def create_buku():
    """
    Menambahkan buku baru ke koleksi.
    Request body: JSON dengan field judul, pengarang, tahun (wajib),
                  isbn dan kategori (opsional).
    Response: JSON buku yang dibuat (201) atau error validasi (400).
    """
    global _next_id

    # Pastikan request berisi JSON
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

    # Buat buku baru
    buku_baru = {
        'id': _next_id,
        'judul': str(data['judul']).strip(),
        'pengarang': str(data['pengarang']).strip(),
        'tahun': int(data['tahun']),
        'isbn': data.get('isbn', ''),
        'kategori': data.get('kategori', 'Umum')
    }

    _buku_data.append(buku_baru)
    _next_id += 1

    return jsonify({
        'status': 'success',
        'message': 'Buku berhasil ditambahkan',
        'data': buku_baru
    }), 201


# ----- Endpoint 4: PUT /api/buku/<id> — Update buku -----
@books_bp.route('/api/buku/<int:buku_id>', methods=['PUT'])
def update_buku(buku_id):
    """
    Mengupdate data buku yang sudah ada.
    Request body: JSON dengan field yang ingin diupdate.
    Response: JSON buku yang diupdate (200), not found (404), atau error (400).
    """
    buku = next((b for b in _buku_data if b['id'] == buku_id), None)

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

    # Validasi: minimal satu field harus diupdate
    updatable_fields = ['judul', 'pengarang', 'tahun', 'isbn', 'kategori']
    has_update = any(f in data for f in updatable_fields)

    if not has_update:
        return jsonify({
            'status': 'error',
            'message': f'Minimal satu field harus diupdate: {", ".join(updatable_fields)}'
        }), 400

    # Validasi tahun jika disertakan
    if 'tahun' in data:
        try:
            tahun = int(data['tahun'])
            if tahun < 1900 or tahun > 2030:
                return jsonify({
                    'status': 'error',
                    'message': 'Tahun harus antara 1900 dan 2030'
                }), 400
        except (ValueError, TypeError):
            return jsonify({
                'status': 'error',
                'message': 'Tahun harus berupa angka'
            }), 400

    # Update field yang diberikan
    for field in updatable_fields:
        if field in data:
            if field == 'tahun':
                buku[field] = int(data[field])
            else:
                buku[field] = str(data[field]).strip()

    return jsonify({
        'status': 'success',
        'message': 'Buku berhasil diupdate',
        'data': buku
    }), 200


# ----- Endpoint 5: DELETE /api/buku/<id> — Hapus buku -----
@books_bp.route('/api/buku/<int:buku_id>', methods=['DELETE'])
def delete_buku(buku_id):
    """
    Menghapus buku dari koleksi.
    Response: Pesan sukses (200) atau not found (404).
    """
    buku = next((b for b in _buku_data if b['id'] == buku_id), None)

    if buku is None:
        return jsonify({
            'status': 'error',
            'message': f'Buku dengan ID {buku_id} tidak ditemukan'
        }), 404

    _buku_data.remove(buku)

    return jsonify({
        'status': 'success',
        'message': f'Buku "{buku["judul"]}" berhasil dihapus'
    }), 200
```

**Expected Output** — Jalankan server dan test endpoint pertama:

```bash
python run.py &
curl -s http://127.0.0.1:5000/api/buku | python -m json.tool
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
            "kategori": "Pemrograman"
        },
        ...
    ]
}
```

> **Troubleshooting:**
> - `404` saat akses `/api/buku` → Pastikan Blueprint sudah di-register di `__init__.py` (`app.register_blueprint(books_bp)`)
> - `ImportError: cannot import name 'books_bp'` → Pastikan file `app/routes/books.py` ada dan `books_bp` didefinisikan di level modul
> - `TypeError: Object of type ... is not JSON serializable` → Pastikan semua value di dictionary adalah tipe dasar Python (str, int, list, dict)

---

### Langkah 4: Test Semua 5 Endpoints dengan curl (20 menit)

**Mengapa langkah ini penting?** Menguji setiap endpoint secara manual memastikan API berfungsi sesuai spesifikasi sebelum digunakan oleh frontend atau diuji secara otomatis (Lab 09). `curl` adalah tool standar untuk testing API di command line.

Pastikan server masih berjalan, lalu jalankan setiap perintah berikut:

**Test 1: GET semua buku**

```bash
curl -s http://127.0.0.1:5000/api/buku | python -m json.tool
```

Expected: Status 200, array berisi 5 buku.

**Test 2: GET satu buku (berhasil)**

```bash
curl -s http://127.0.0.1:5000/api/buku/1 | python -m json.tool
```

Expected output:

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "judul": "Algoritma dan Pemrograman Python",
        "pengarang": "Ahmad Fauzi",
        "tahun": 2024,
        "isbn": "978-602-001-001",
        "kategori": "Pemrograman"
    }
}
```

**Test 3: GET buku yang tidak ada (404)**

```bash
curl -s http://127.0.0.1:5000/api/buku/999 | python -m json.tool
```

Expected output:

```json
{
    "status": "error",
    "message": "Buku dengan ID 999 tidak ditemukan"
}
```

**Test 4: POST buku baru (berhasil)**

```bash
curl -s -X POST http://127.0.0.1:5000/api/buku \
  -H "Content-Type: application/json" \
  -d '{"judul": "Struktur Data dengan Java", "pengarang": "Fajar Hidayat", "tahun": 2024, "isbn": "978-602-001-006", "kategori": "Pemrograman"}' \
  | python -m json.tool
```

Expected output:

```json
{
    "status": "success",
    "message": "Buku berhasil ditambahkan",
    "data": {
        "id": 6,
        "judul": "Struktur Data dengan Java",
        "pengarang": "Fajar Hidayat",
        "tahun": 2024,
        "isbn": "978-602-001-006",
        "kategori": "Pemrograman"
    }
}
```

HTTP status: **201 Created**

**Test 5: POST dengan data tidak valid (400)**

```bash
curl -s -X POST http://127.0.0.1:5000/api/buku \
  -H "Content-Type: application/json" \
  -d '{"judul": "AB"}' \
  | python -m json.tool
```

Expected output:

```json
{
    "status": "error",
    "message": "Field berikut wajib diisi: pengarang, tahun"
}
```

HTTP status: **400 Bad Request**

**Test 6: PUT update buku (berhasil)**

```bash
curl -s -X PUT http://127.0.0.1:5000/api/buku/1 \
  -H "Content-Type: application/json" \
  -d '{"tahun": 2025, "kategori": "Pemrograman Python"}' \
  | python -m json.tool
```

Expected output:

```json
{
    "status": "success",
    "message": "Buku berhasil diupdate",
    "data": {
        "id": 1,
        "judul": "Algoritma dan Pemrograman Python",
        "pengarang": "Ahmad Fauzi",
        "tahun": 2025,
        "isbn": "978-602-001-001",
        "kategori": "Pemrograman Python"
    }
}
```

**Test 7: DELETE buku (berhasil)**

```bash
curl -s -X DELETE http://127.0.0.1:5000/api/buku/5 | python -m json.tool
```

Expected output:

```json
{
    "status": "success",
    "message": "Buku \"Kecerdasan Buatan: Teori dan Praktik\" berhasil dihapus"
}
```

**Test 8: DELETE buku yang tidak ada (404)**

```bash
curl -s -X DELETE http://127.0.0.1:5000/api/buku/999 | python -m json.tool
```

Expected output:

```json
{
    "status": "error",
    "message": "Buku dengan ID 999 tidak ditemukan"
}
```

**Verifikasi: GET semua buku setelah operasi**

```bash
curl -s http://127.0.0.1:5000/api/buku | python -m json.tool
```

Expected: Buku ID 5 sudah tidak ada, buku ID 6 (baru) sudah ada, buku ID 1 tahunnya berubah ke 2025.

> **Troubleshooting:**
> - `curl: command not found` → Di Codespaces, curl biasanya sudah terinstal. Jika tidak: `sudo apt install curl`
> - Response kosong atau HTML bukannya JSON → Pastikan URL-nya benar (`/api/buku`, bukan `/buku`)
> - `405 Method Not Allowed` → Pastikan parameter `methods=` di decorator route sudah benar
> - Di Windows/PowerShell, gunakan double quotes di `-d` dan escape inner quotes, atau gunakan Git Bash

---

### Langkah 5: Tambahkan Input Validation yang Robust (10 menit)

**Mengapa langkah ini penting?** Validasi input mencegah data kotor masuk ke sistem dan melindungi dari serangan seperti injection. API yang baik selalu memvalidasi semua input dari client — prinsip *"Never trust user input"*.

Fungsi `_validate_buku_data()` sudah dibuat di Langkah 3. Sekarang kita tambahkan validasi tambahan dan test edge cases:

```bash
# Test: POST tanpa Content-Type header
curl -s -X POST http://127.0.0.1:5000/api/buku \
  -d '{"judul": "Test"}' \
  | python -m json.tool
```

Expected:

```json
{
    "status": "error",
    "message": "Content-Type harus application/json"
}
```

```bash
# Test: POST dengan tahun tidak valid
curl -s -X POST http://127.0.0.1:5000/api/buku \
  -H "Content-Type: application/json" \
  -d '{"judul": "Test Buku", "pengarang": "Test", "tahun": "bukan-angka"}' \
  | python -m json.tool
```

Expected:

```json
{
    "status": "error",
    "message": "Tahun harus berupa angka"
}
```

```bash
# Test: POST dengan judul terlalu pendek
curl -s -X POST http://127.0.0.1:5000/api/buku \
  -H "Content-Type: application/json" \
  -d '{"judul": "AB", "pengarang": "Test", "tahun": 2024}' \
  | python -m json.tool
```

Expected:

```json
{
    "status": "error",
    "message": "Judul minimal 3 karakter"
}
```

```bash
# Test: PUT tanpa field yang valid
curl -s -X PUT http://127.0.0.1:5000/api/buku/1 \
  -H "Content-Type: application/json" \
  -d '{"field_tidak_dikenal": "value"}' \
  | python -m json.tool
```

Expected:

```json
{
    "status": "error",
    "message": "Minimal satu field harus diupdate: judul, pengarang, tahun, isbn, kategori"
}
```

> **Troubleshooting:**
> - Validasi tidak bekerja → Pastikan `request.get_json()` dipanggil setelah cek `request.is_json`
> - Data tetap diterima walau tidak valid → Cek urutan validasi di `_validate_buku_data()` — pastikan semua cek dilakukan sebelum data disimpan

---

### Langkah 6: Verifikasi CORS dan Integrasi dengan Frontend (10 menit)

**Mengapa langkah ini penting?** CORS (Cross-Origin Resource Sharing) diperlukan agar frontend di domain/port berbeda bisa mengakses API. Tanpa CORS, browser akan memblokir request dari frontend ke backend jika mereka berjalan di origin yang berbeda.

Verifikasi CORS sudah aktif:

```bash
# Cek CORS headers
curl -s -I -X OPTIONS http://127.0.0.1:5000/api/buku \
  -H "Origin: http://localhost:3000" \
  -H "Access-Control-Request-Method: GET"
```

Expected: Response headers mengandung:

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: ...
```

Sekarang, hubungkan API dengan frontend dari Lab 05. Tambahkan fungsi fetch API di `app/static/js/main.js` (tambahkan di akhir file, di dalam `DOMContentLoaded`):

```javascript
    // --- 6. Fetch API Integration (untuk koneksi ke backend) ---
    // Fungsi helper untuk memanggil REST API
    window.PerpustakaanAPI = {
        baseUrl: '/api',

        // GET semua buku
        getAllBuku: async function () {
            const response = await fetch(this.baseUrl + '/buku');
            const result = await response.json();
            return result;
        },

        // GET satu buku
        getBuku: async function (id) {
            const response = await fetch(this.baseUrl + '/buku/' + id);
            if (!response.ok) {
                throw new Error('Buku tidak ditemukan');
            }
            return await response.json();
        },

        // POST buku baru
        createBuku: async function (data) {
            const response = await fetch(this.baseUrl + '/buku', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            return await response.json();
        },

        // DELETE buku
        deleteBuku: async function (id) {
            const response = await fetch(this.baseUrl + '/buku/' + id, {
                method: 'DELETE'
            });
            return await response.json();
        }
    };

    // Test koneksi API (buka Console browser untuk melihat output)
    if (window.location.pathname === '/books') {
        window.PerpustakaanAPI.getAllBuku().then(function (result) {
            console.log('API Response:', result);
            console.log('Jumlah buku dari API:', result.count);
        }).catch(function (error) {
            console.error('API Error:', error);
        });
    }
```

**Expected Output** — Buka halaman `/books` di browser, buka Console (F12):

```
API Response: {status: "success", count: 5, data: Array(5)}
Jumlah buku dari API: 5
```

> **Troubleshooting:**
> - `CORS error` di Console → Pastikan `CORS(app, resources={r"/api/*": {"origins": "*"}})` ada di `__init__.py`
> - `Failed to fetch` → Pastikan server Flask sedang berjalan
> - Data di API berbeda dengan data di template → Karena ada dua sumber data (BUKU_DATA di main.py dan _buku_data di books.py); ini akan diselesaikan di Lab 07 saat kedua route menggunakan database yang sama

---

### Langkah 7: Ringkasan dan Commit (10 menit)

**Mengapa langkah ini penting?** Merangkum apa yang sudah dibangun dan menyimpan progress ke Git memastikan pekerjaan terdokumentasi dan bisa di-review oleh tim.

**Ringkasan arsitektur backend yang dibangun:**

```
HTTP Request
    │
    ▼
Flask App (create_app)
    │
    ├── Config (dev/test/prod)
    │
    ├── CORS Middleware
    │
    ├── Blueprint: main_bp (halaman web — dari Lab 05)
    │   ├── GET /         → index.html
    │   ├── GET /books    → books.html
    │   └── GET|POST /login → login.html
    │
    ├── Blueprint: books_bp (REST API — Lab 06)
    │   ├── GET    /api/buku       → 200 + daftar buku
    │   ├── GET    /api/buku/<id>  → 200 + buku | 404
    │   ├── POST   /api/buku       → 201 + buku baru | 400
    │   ├── PUT    /api/buku/<id>  → 200 + buku updated | 404 | 400
    │   └── DELETE /api/buku/<id>  → 200 + pesan sukses | 404
    │
    └── Error Handlers
        ├── 400 → Bad Request (JSON)
        ├── 404 → Not Found (JSON)
        └── 500 → Internal Server Error (JSON)
```

**Commit ke Git:**

```bash
git add .
git commit -m "feat(api): implement REST API endpoints for Buku resource

- Add multi-environment config (dev/test/prod)
- Add Blueprint books_bp with 5 CRUD endpoints
- Add input validation for create and update operations
- Add error handlers (400, 404, 500) with JSON responses
- Add Flask-CORS for cross-origin requests
- Add JavaScript fetch API helper in frontend"
```

**Verifikasi final — test semua endpoints:**

```bash
# Jalankan script test sederhana
echo "=== Test GET /api/buku ==="
curl -s -o /dev/null -w "Status: %{http_code}\n" http://127.0.0.1:5000/api/buku

echo "=== Test GET /api/buku/1 ==="
curl -s -o /dev/null -w "Status: %{http_code}\n" http://127.0.0.1:5000/api/buku/1

echo "=== Test GET /api/buku/999 (not found) ==="
curl -s -o /dev/null -w "Status: %{http_code}\n" http://127.0.0.1:5000/api/buku/999

echo "=== Test POST /api/buku ==="
curl -s -o /dev/null -w "Status: %{http_code}\n" -X POST http://127.0.0.1:5000/api/buku \
  -H "Content-Type: application/json" \
  -d '{"judul": "Test Book", "pengarang": "Tester", "tahun": 2024}'

echo "=== Test POST /api/buku (invalid) ==="
curl -s -o /dev/null -w "Status: %{http_code}\n" -X POST http://127.0.0.1:5000/api/buku \
  -H "Content-Type: application/json" \
  -d '{"judul": "AB"}'

echo "=== Test PUT /api/buku/1 ==="
curl -s -o /dev/null -w "Status: %{http_code}\n" -X PUT http://127.0.0.1:5000/api/buku/1 \
  -H "Content-Type: application/json" \
  -d '{"tahun": 2026}'

echo "=== Test DELETE /api/buku/1 ==="
curl -s -o /dev/null -w "Status: %{http_code}\n" -X DELETE http://127.0.0.1:5000/api/buku/1
```

**Expected Output:**

```
=== Test GET /api/buku ===
Status: 200
=== Test GET /api/buku/1 ===
Status: 200
=== Test GET /api/buku/999 (not found) ===
Status: 404
=== Test POST /api/buku ===
Status: 201
=== Test POST /api/buku (invalid) ===
Status: 400
=== Test PUT /api/buku/1 ===
Status: 200
=== Test DELETE /api/buku/1 ===
Status: 200
```

---

## Tantangan Tambahan

### Level 1 — Basic
Tambahkan endpoint **GET `/api/buku/search?q=<keyword>`** yang mencari buku berdasarkan judul atau pengarang. Gunakan `request.args.get('q')` untuk mengambil query parameter. Kembalikan daftar buku yang cocok (case-insensitive).

### Level 2 — Intermediate
Implementasikan **pagination** pada endpoint GET `/api/buku`. Terima query parameter `page` (default: 1) dan `per_page` (default: 10). Response harus menyertakan metadata pagination:
```json
{
    "status": "success",
    "data": [...],
    "pagination": {
        "page": 1,
        "per_page": 10,
        "total": 25,
        "total_pages": 3,
        "has_next": true,
        "has_prev": false
    }
}
```

### Level 3 — Advanced
Buat **Blueprint kedua** untuk resource `User` (`/api/users`) dengan 5 endpoints CRUD. Tambahkan validasi email format dan password hashing menggunakan `werkzeug.security.generate_password_hash()`. Pastikan password tidak pernah dikembalikan dalam response JSON.

---

## Refleksi & AI Usage Log

Setelah menyelesaikan praktikum, jawab pertanyaan refleksi berikut:

1. Apa perbedaan antara status code 200, 201, dan 400? Kapan masing-masing digunakan?
2. Mengapa kita perlu validasi input di server-side meskipun sudah ada validasi di client-side (JavaScript)?
3. Apa keuntungan menggunakan Blueprint dibanding mendefinisikan semua route di satu file?
4. Bagaimana factory pattern (`create_app`) membantu proses testing nantinya (Lab 09)?

### AI Usage Log

| No | Prompt/Pertanyaan ke AI | Tool | Output yang Digunakan | Modifikasi yang Dilakukan | Pemahaman (1-5) |
|----|-------------------------|------|----------------------|---------------------------|-----------------|
| 1  | Contoh: "Bagaimana cara menangani JSON request di Flask?" | ChatGPT | Contoh `request.get_json()` | Menambahkan validasi `request.is_json` | 4 |
| 2  | | | | | |
| 3  | | | | | |

> **Catatan:** Penggunaan AI sebagai *learning partner* diperbolehkan. Yang **tidak** diperbolehkan adalah meng-copy seluruh kode tanpa memahami logikanya. Tulis refleksi jujur tentang kontribusi AI vs pemahaman mandiri Anda.

---

## Checklist Penyelesaian

- [ ] `config.py` dengan 3 konfigurasi (development, testing, production) berfungsi
- [ ] App factory `create_app(config_name)` menerima parameter konfigurasi
- [ ] Blueprint `books_bp` terdaftar dan route berfungsi
- [ ] Endpoint GET `/api/buku` mengembalikan semua buku (200)
- [ ] Endpoint GET `/api/buku/<id>` mengembalikan satu buku (200) atau error (404)
- [ ] Endpoint POST `/api/buku` membuat buku baru (201) atau error validasi (400)
- [ ] Endpoint PUT `/api/buku/<id>` mengupdate buku (200) atau error (404/400)
- [ ] Endpoint DELETE `/api/buku/<id>` menghapus buku (200) atau error (404)
- [ ] Input validation berfungsi (field wajib, format tahun, panjang judul)
- [ ] Error handlers (400, 404, 500) mengembalikan JSON
- [ ] Flask-CORS dikonfigurasi untuk route `/api/*`
- [ ] Semua 5 endpoints sudah ditest dengan curl dan menghasilkan response yang benar
- [ ] Kode di-commit ke Git dengan pesan commit yang deskriptif
- [ ] AI Usage Log diisi untuk sesi ini

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
