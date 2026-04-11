# Lab 09: Unit Testing dengan pytest dan Jest

## Informasi Praktikum

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Praktikum** | 8 dari 13 (Minggu 9) |
| **Topik** | Unit Testing Backend (pytest) dan Frontend (Jest) |
| **CPMK** | CPMK-5 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 07 (Database Integration & ORM) selesai |
| **Referensi Teori** | IF2205 Minggu 9 — Software Testing |

## Tujuan

1. **Menulis** (C3) unit test untuk Flask API menggunakan pytest
2. **Menulis** (C3) unit test untuk fungsi JavaScript menggunakan Jest
3. **Menjalankan** (C3) test suite dan menganalisis coverage report
4. **Menerapkan** (C3) TDD (Test-Driven Development) untuk fitur baru

## Konsep Singkat

### Apa Itu Unit Testing?

**Unit testing** adalah teknik pengujian perangkat lunak di mana unit terkecil dari kode (fungsi, method, atau class) diuji secara **terisolasi** dari komponen lain. Tujuannya memastikan setiap unit bekerja sesuai spesifikasi sebelum diintegrasikan.

```
Piramida Testing (Testing Pyramid)
===================================

         /\
        /  \         E2E Tests        (sedikit, lambat, mahal)
       /----\
      /      \       Integration      (sedang)
     /--------\      Tests
    /          \
   /------------\    Unit Tests       (banyak, cepat, murah)
  /______________\

Prinsip: Semakin ke bawah, semakin BANYAK dan CEPAT.
         Semakin ke atas, semakin SEDIKIT dan LAMBAT.
```

### Mengapa Unit Testing Penting?

| Manfaat | Penjelasan |
|---------|-----------|
| **Deteksi bug lebih awal** | Bug ditemukan saat development, bukan di production |
| **Dokumentasi hidup** | Test menjelaskan bagaimana kode seharusnya bekerja |
| **Refactoring aman** | Ubah internal tanpa takut merusak behavior |
| **Regresi tercegah** | Perubahan baru tidak merusak fitur lama |
| **Desain lebih baik** | Kode yang mudah di-test = kode yang terstruktur baik |

### Anatomi Unit Test (AAA Pattern)

Setiap unit test mengikuti pola **Arrange-Act-Assert**:

```python
def test_example():
    # Arrange — siapkan data dan kondisi awal
    buku = Buku(judul="Test", pengarang="Ali", tahun=2025)

    # Act — jalankan aksi yang diuji
    result = buku.to_dict()

    # Assert — verifikasi hasilnya sesuai ekspektasi
    assert result['judul'] == "Test"
```

### TDD: Red-Green-Refactor

**Test-Driven Development** membalik urutan: tulis test dulu, baru implementasi.

```
   RED              GREEN            REFACTOR
   (test gagal) --> (test lulus) --> (perbaiki kode)
       |                                  |
       +----------------------------------+
                (ulangi siklus)
```

> **Referensi teori:** Lihat modul IF2205 Minggu 9 — Software Testing untuk pembahasan mendalam tentang strategi testing, white-box vs black-box, dan test case design.

## Persiapan

- Proyek Flask dari Lab 06-07 sudah berjalan
- Install dependencies:
  ```bash
  pip install pytest pytest-cov
  npm install --save-dev jest
  ```
- Buat folder `tests/` di root proyek:
  ```bash
  mkdir -p tests
  touch tests/__init__.py
  ```

**Verifikasi instalasi:**
```bash
pytest --version
npx jest --version
```

**Expected output:**
```
pytest 8.x.x
30.x.x    # versi Jest
```

> **Troubleshooting:** Jika `pytest` tidak ditemukan, pastikan virtual environment aktif (`source venv/bin/activate`). Jika `npx jest` gagal, pastikan `node_modules/` ada dengan `npm install`.

## Langkah-langkah

### Langkah 1: Setup pytest dan Konfigurasi (15 menit)

**Mengapa langkah ini penting?** Konfigurasi yang benar memastikan pytest menemukan dan menjalankan semua test secara konsisten, baik di lokal maupun di CI pipeline.

Buat file konfigurasi pytest:
```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = -v --tb=short
```

Buat file `tests/conftest.py` — file ini berisi **fixtures** (objek yang disiapkan sebelum test berjalan):
```python
# tests/conftest.py
import pytest
from app import create_app, db

@pytest.fixture
def app():
    """Buat instance aplikasi untuk testing.

    Menggunakan SQLite in-memory agar:
    - Test tidak mengubah database development
    - Setiap test mulai dari database kosong (terisolasi)
    - Test berjalan lebih cepat (tidak ada disk I/O)
    """
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    """Test client untuk HTTP requests.

    Menggantikan browser/Postman — kirim request ke Flask
    tanpa perlu menjalankan server sungguhan.
    """
    return app.test_client()

@pytest.fixture
def sample_buku(app):
    """Fixture untuk buku sample yang sering dipakai di banyak test."""
    from app.models import Buku
    with app.app_context():
        buku = Buku(judul='Algoritma Python', pengarang='Ahmad', tahun=2025)
        db.session.add(buku)
        db.session.commit()
        yield buku
```

**Jalankan untuk verifikasi setup:**
```bash
pytest --co
```

**Expected output:**
```
========================= test session starts ==========================
collected 0 items

========================= no tests ran ============================
```

> Ini normal — kita belum menulis test. Yang penting tidak ada error konfigurasi.

### Langkah 2: Unit Test Backend — Model (20 menit)

**Mengapa langkah ini penting?** Model adalah inti dari domain logic. Test model memastikan data disimpan dan divalidasi dengan benar sebelum kita menguji layer yang lebih tinggi (API).

```python
# tests/test_models.py
from app.models import Buku, User
from app import db

def test_create_buku(app):
    """Test membuat instance Buku."""
    with app.app_context():
        buku = Buku(judul='Algoritma Python', pengarang='Ahmad', tahun=2025)
        db.session.add(buku)
        db.session.commit()

        assert buku.id is not None
        assert buku.judul == 'Algoritma Python'

def test_buku_repr(app):
    """Test representasi string Buku."""
    buku = Buku(judul='Test Book', pengarang='Test', tahun=2025)
    assert 'Test Book' in str(buku)

def test_create_user(app):
    """Test membuat instance User."""
    with app.app_context():
        user = User(username='mahasiswa1', email='mhs@uai.ac.id')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()

        assert user.check_password('password123')
        assert not user.check_password('wrong')

def test_buku_to_dict(app):
    """Test konversi Buku ke dictionary (untuk JSON response)."""
    with app.app_context():
        buku = Buku(judul='Flask Web', pengarang='Budi', tahun=2025)
        db.session.add(buku)
        db.session.commit()

        result = buku.to_dict()
        assert result['judul'] == 'Flask Web'
        assert result['pengarang'] == 'Budi'
        assert 'id' in result

def test_user_password_not_stored_plain(app):
    """Test bahwa password TIDAK disimpan sebagai plain text."""
    with app.app_context():
        user = User(username='test_user', email='test@uai.ac.id')
        user.set_password('rahasia123')
        db.session.add(user)
        db.session.commit()

        # Password hash tidak boleh sama dengan plain text
        assert user.password_hash != 'rahasia123'
```

**Jalankan test:**
```bash
pytest tests/test_models.py -v
```

**Expected output:**
```
========================= test session starts ==========================
tests/test_models.py::test_create_buku PASSED                    [ 20%]
tests/test_models.py::test_buku_repr PASSED                      [ 40%]
tests/test_models.py::test_create_user PASSED                    [ 60%]
tests/test_models.py::test_buku_to_dict PASSED                   [ 80%]
tests/test_models.py::test_user_password_not_stored_plain PASSED  [100%]

========================= 5 passed in 0.42s ============================
```

> **Troubleshooting:** Jika muncul `ModuleNotFoundError: No module named 'app'`, pastikan Anda menjalankan pytest dari root proyek (bukan dari dalam folder `tests/`). Tambahkan file `tests/__init__.py` jika belum ada.

### Langkah 3: Unit Test Backend — API Routes (20 menit)

**Mengapa langkah ini penting?** API routes adalah "kontrak" antara frontend dan backend. Test routes memastikan endpoint mengembalikan response yang benar untuk berbagai skenario (sukses, error, edge case).

```python
# tests/test_routes.py
import json

def test_get_books_empty(client):
    """Test GET /api/buku saat database kosong."""
    response = client.get('/api/buku')
    assert response.status_code == 200
    assert response.json == []

def test_create_book(client):
    """Test POST /api/buku untuk menambah buku baru."""
    data = {'judul': 'Flask Web Dev', 'pengarang': 'Budi', 'tahun': 2025}
    response = client.post('/api/buku',
                          data=json.dumps(data),
                          content_type='application/json')
    assert response.status_code == 201
    assert response.json['judul'] == 'Flask Web Dev'

def test_get_book_not_found(client):
    """Test GET /api/buku/999 — buku tidak ditemukan."""
    response = client.get('/api/buku/999')
    assert response.status_code == 404

def test_create_book_missing_judul(client):
    """Test POST /api/buku tanpa field judul — harus ditolak."""
    data = {'pengarang': 'Test', 'tahun': 2025}
    response = client.post('/api/buku',
                          data=json.dumps(data),
                          content_type='application/json')
    assert response.status_code == 400

def test_update_book(client):
    """Test PUT /api/buku/<id> untuk update data buku."""
    # Buat buku dulu
    data = {'judul': 'Original', 'pengarang': 'Ali', 'tahun': 2020}
    resp = client.post('/api/buku',
                       data=json.dumps(data),
                       content_type='application/json')
    buku_id = resp.json['id']

    # Update
    update_data = {'judul': 'Updated Title'}
    resp = client.put(f'/api/buku/{buku_id}',
                      data=json.dumps(update_data),
                      content_type='application/json')
    assert resp.status_code == 200
    assert resp.json['judul'] == 'Updated Title'

def test_delete_book(client):
    """Test DELETE /api/buku/<id> untuk menghapus buku."""
    # Buat buku dulu
    data = {'judul': 'To Delete', 'pengarang': 'Test', 'tahun': 2025}
    resp = client.post('/api/buku',
                       data=json.dumps(data),
                       content_type='application/json')
    buku_id = resp.json['id']

    # Hapus
    resp = client.delete(f'/api/buku/{buku_id}')
    assert resp.status_code == 200

    # Pastikan sudah terhapus
    resp = client.get(f'/api/buku/{buku_id}')
    assert resp.status_code == 404
```

**Jalankan test:**
```bash
pytest tests/test_routes.py -v
```

**Expected output:**
```
========================= test session starts ==========================
tests/test_routes.py::test_get_books_empty PASSED                [ 16%]
tests/test_routes.py::test_create_book PASSED                    [ 33%]
tests/test_routes.py::test_get_book_not_found PASSED             [ 50%]
tests/test_routes.py::test_create_book_missing_judul PASSED      [ 66%]
tests/test_routes.py::test_update_book PASSED                    [ 83%]
tests/test_routes.py::test_delete_book PASSED                    [100%]

========================= 6 passed in 0.58s ============================
```

> **Troubleshooting:** Jika test `test_create_book` gagal dengan `405 Method Not Allowed`, periksa apakah route di Flask sudah mendukung method `POST`. Pastikan decorator `@buku_bp.route('/api/buku', methods=['GET', 'POST'])` sudah benar.

### Langkah 4: Unit Test Frontend — Jest (15 menit)

**Mengapa langkah ini penting?** Frontend juga memiliki logic (format tanggal, validasi input, manipulasi string) yang harus diuji. Jest adalah test runner standar untuk JavaScript.

Pastikan `package.json` memiliki konfigurasi Jest:
```json
{
  "scripts": {
    "test": "jest --verbose"
  },
  "jest": {
    "testEnvironment": "node",
    "collectCoverageFrom": ["static/js/**/*.js"]
  }
}
```

Buat file test:
```javascript
// tests/utils.test.js
const { formatDate, validateISBN, truncateText } = require('../static/js/utils');

describe('formatDate', () => {
  test('memformat tanggal dengan benar', () => {
    expect(formatDate('2025-03-15')).toBe('15 Maret 2025');
  });

  test('mengembalikan string kosong untuk input invalid', () => {
    expect(formatDate('')).toBe('');
  });

  test('mengembalikan string kosong untuk null', () => {
    expect(formatDate(null)).toBe('');
  });

  test('memformat tanggal di bulan Desember', () => {
    expect(formatDate('2025-12-01')).toBe('1 Desember 2025');
  });
});

describe('validateISBN', () => {
  test('menerima ISBN-13 valid', () => {
    expect(validateISBN('978-3-16-148410-0')).toBe(true);
  });

  test('menolak ISBN invalid', () => {
    expect(validateISBN('12345')).toBe(false);
  });

  test('menolak string kosong', () => {
    expect(validateISBN('')).toBe(false);
  });

  test('menolak input non-string', () => {
    expect(validateISBN(12345)).toBe(false);
  });
});

describe('truncateText', () => {
  test('memotong teks panjang', () => {
    const text = 'Lorem ipsum dolor sit amet consectetur';
    expect(truncateText(text, 20)).toBe('Lorem ipsum dolor si...');
  });

  test('tidak memotong teks pendek', () => {
    expect(truncateText('Hello', 20)).toBe('Hello');
  });

  test('menangani teks kosong', () => {
    expect(truncateText('', 20)).toBe('');
  });

  test('menangani limit nol', () => {
    expect(truncateText('Hello', 0)).toBe('...');
  });
});
```

**Jalankan:**
```bash
npx jest --verbose
```

**Expected output:**
```
 PASS  tests/utils.test.js
  formatDate
    ✓ memformat tanggal dengan benar (3 ms)
    ✓ mengembalikan string kosong untuk input invalid (1 ms)
    ✓ mengembalikan string kosong untuk null (1 ms)
    ✓ memformat tanggal di bulan Desember (1 ms)
  validateISBN
    ✓ menerima ISBN-13 valid (1 ms)
    ✓ menolak ISBN invalid
    ✓ menolak string kosong
    ✓ menolak input non-string (1 ms)
  truncateText
    ✓ memotong teks panjang (1 ms)
    ✓ tidak memotong teks pendek
    ✓ menangani teks kosong
    ✓ menangani limit nol

Tests:       12 passed, 12 total
```

> **Troubleshooting:** Jika muncul `Cannot find module '../static/js/utils'`, pastikan file `static/js/utils.js` ada dan menggunakan `module.exports` untuk mengekspos fungsi.

### Langkah 5: Coverage Report dan Analisis (15 menit)

**Mengapa langkah ini penting?** Coverage report menunjukkan baris kode mana yang sudah dan belum diuji. Ini membantu Anda menemukan "blind spot" — bagian kode yang belum punya test.

```bash
# Backend coverage
pytest tests/ --cov=app --cov-report=html --cov-report=term
```

**Expected output (contoh):**
```
---------- coverage: platform linux, python 3.11.x ----------
Name                    Stmts   Miss  Cover
-------------------------------------------
app/__init__.py            15      2    87%
app/models.py              42      5    88%
app/routes/buku.py         38     12    68%
app/routes/auth.py         25     15    40%
app/routes/health.py        8      0   100%
-------------------------------------------
TOTAL                     128     34    73%
```

**Cara membaca coverage report:**

| Kolom | Arti |
|-------|------|
| **Stmts** | Total baris kode yang bisa dieksekusi |
| **Miss** | Baris yang TIDAK dieksekusi oleh test |
| **Cover** | Persentase baris yang sudah diuji |

**Analisis:**
- `app/routes/auth.py` hanya 40% — banyak path yang belum diuji (misalnya: login gagal, token expired)
- `app/routes/health.py` 100% — endpoint sederhana, mudah di-cover
- **Target minimum: 70%** untuk keseluruhan proyek

```bash
# Buka laporan visual (HTML)
# Di Codespaces, gunakan tab Ports untuk preview htmlcov/index.html

# Frontend coverage
npx jest --coverage
```

**Expected output frontend:**
```
----------|---------|----------|---------|---------|-------------------
File      | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
----------|---------|----------|---------|---------|-------------------
All files |   85.71 |    66.67 |     100 |   85.71 |
 utils.js |   85.71 |    66.67 |     100 |   85.71 | 12,15
----------|---------|----------|---------|---------|-------------------
```

**Interpretasi:** `% Branch` 66.67% berarti ada cabang `if/else` yang belum semua path-nya diuji. Periksa baris 12 dan 15 di `utils.js` — tulis test tambahan untuk menutupi cabang tersebut.

> **Troubleshooting:** Jika coverage 0%, pastikan `--cov=app` mengarah ke folder yang benar (folder yang berisi kode produksi, bukan folder test). Jika muncul `No data to report`, pastikan test benar-benar mengimpor dan menjalankan kode dari folder `app/`.

### Langkah 6: Mini TDD Challenge (15 menit)

**Mengapa langkah ini penting?** TDD memastikan Anda berpikir tentang behavior sebelum implementasi. Ini menghasilkan kode yang lebih fokus dan mudah di-test.

Implementasikan fitur "search buku" dengan TDD:

**1. RED — Tulis test dulu (akan gagal):**
```python
# tests/test_search.py
import json

def test_search_books(client):
    """Test pencarian buku berdasarkan judul."""
    # Arrange — tambah data dulu
    client.post('/api/buku', data=json.dumps(
        {'judul': 'Python Dasar', 'pengarang': 'Ali', 'tahun': 2025}
    ), content_type='application/json')
    client.post('/api/buku', data=json.dumps(
        {'judul': 'Java Enterprise', 'pengarang': 'Budi', 'tahun': 2024}
    ), content_type='application/json')

    # Act — search
    response = client.get('/api/buku/search?q=Python')

    # Assert
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['judul'] == 'Python Dasar'

def test_search_books_no_results(client):
    """Test pencarian tanpa hasil."""
    response = client.get('/api/buku/search?q=NonExistentBook')
    assert response.status_code == 200
    assert len(response.json) == 0

def test_search_books_empty_query(client):
    """Test pencarian dengan query kosong — kembalikan semua."""
    client.post('/api/buku', data=json.dumps(
        {'judul': 'Buku A', 'pengarang': 'X', 'tahun': 2025}
    ), content_type='application/json')

    response = client.get('/api/buku/search?q=')
    assert response.status_code == 200
    assert len(response.json) >= 1
```

Jalankan — test akan **GAGAL** (RED):
```bash
pytest tests/test_search.py -v
```

**Expected output:**
```
tests/test_search.py::test_search_books FAILED                   [ 33%]
tests/test_search.py::test_search_books_no_results FAILED        [ 66%]
tests/test_search.py::test_search_books_empty_query FAILED       [100%]

========================= 3 failed in 0.35s ============================
```

**2. GREEN — Implementasi minimal:**
```python
# app/routes/buku.py (tambahkan route baru)
@buku_bp.route('/api/buku/search')
def search_buku():
    """Cari buku berdasarkan judul (case-insensitive)."""
    query = request.args.get('q', '')
    if query:
        results = Buku.query.filter(Buku.judul.ilike(f'%{query}%')).all()
    else:
        results = Buku.query.all()
    return jsonify([b.to_dict() for b in results])
```

Jalankan lagi — test harus **LULUS** (GREEN):
```bash
pytest tests/test_search.py -v
```

**Expected output:**
```
tests/test_search.py::test_search_books PASSED                   [ 33%]
tests/test_search.py::test_search_books_no_results PASSED        [ 66%]
tests/test_search.py::test_search_books_empty_query PASSED       [100%]

========================= 3 passed in 0.41s ============================
```

**3. REFACTOR — Perbaiki jika perlu:**
- Tambahkan validasi input (batas panjang query)
- Tambahkan pagination pada hasil search
- Tambahkan search by pengarang juga

### Langkah 7: Edge Case Testing (Bonus, jika waktu tersisa)

**Mengapa langkah ini penting?** Edge case sering menjadi sumber bug di production. Test yang baik mencakup bukan hanya "happy path" tapi juga input tak terduga.

```python
# tests/test_edge_cases.py
import json

def test_create_buku_tahun_negatif(client):
    """Tahun negatif harus ditolak."""
    data = {'judul': 'Test', 'pengarang': 'Test', 'tahun': -100}
    resp = client.post('/api/buku',
                       data=json.dumps(data),
                       content_type='application/json')
    assert resp.status_code == 400

def test_create_buku_judul_sangat_panjang(client):
    """Judul > 500 karakter harus ditolak atau di-truncate."""
    data = {'judul': 'A' * 501, 'pengarang': 'Test', 'tahun': 2025}
    resp = client.post('/api/buku',
                       data=json.dumps(data),
                       content_type='application/json')
    assert resp.status_code in [400, 201]  # Tergantung implementasi

def test_create_buku_html_injection(client):
    """Coba menyisipkan HTML — harus di-sanitize atau ditolak."""
    data = {'judul': '<script>alert("xss")</script>', 'pengarang': 'Test', 'tahun': 2025}
    resp = client.post('/api/buku',
                       data=json.dumps(data),
                       content_type='application/json')
    if resp.status_code == 201:
        # Jika diterima, pastikan HTML di-escape
        assert '<script>' not in resp.json.get('judul', '')

def test_create_buku_sql_injection_attempt(client):
    """SQL injection via judul — ORM harus mencegah ini."""
    data = {'judul': "'; DROP TABLE buku; --", 'pengarang': 'Test', 'tahun': 2025}
    resp = client.post('/api/buku',
                       data=json.dumps(data),
                       content_type='application/json')
    # Request mungkin sukses (ORM meng-escape), tapi table harus tetap ada
    resp2 = client.get('/api/buku')
    assert resp2.status_code == 200  # Table masih ada, tidak terhapus

def test_concurrent_create_unique_isbn(client):
    """Dua buku dengan ISBN sama harus ditolak yang kedua."""
    data1 = {'judul': 'Buku A', 'pengarang': 'X', 'tahun': 2025, 'isbn': '978-000-111'}
    data2 = {'judul': 'Buku B', 'pengarang': 'Y', 'tahun': 2025, 'isbn': '978-000-111'}

    resp1 = client.post('/api/buku', data=json.dumps(data1),
                        content_type='application/json')
    resp2 = client.post('/api/buku', data=json.dumps(data2),
                        content_type='application/json')

    assert resp1.status_code == 201
    assert resp2.status_code in [400, 409]  # Conflict atau Bad Request
```

## Troubleshooting Umum

| Error | Penyebab | Solusi |
|-------|----------|--------|
| `ModuleNotFoundError: No module named 'app'` | Pytest tidak menemukan package app | Jalankan pytest dari root proyek, pastikan `__init__.py` ada |
| `fixture 'app' not found` | conftest.py tidak di-load | Pastikan `conftest.py` ada di folder `tests/` |
| `AssertionError: 500 != 200` | Server error di endpoint | Periksa Flask error log, biasanya bug di kode route |
| `FAILED ... assert [] == [expected]` | Database kosong di test | Pastikan test menambah data (Arrange) sebelum query |
| `jest: command not found` | Jest belum terinstall | Jalankan `npm install --save-dev jest` |
| `Coverage 0%` | `--cov` mengarah ke folder salah | Pastikan `--cov=app` sesuai nama folder kode produksi |

## Tantangan Tambahan

1. **Basic:** Tulis test untuk edge cases tambahan — input kosong, karakter spesial (emoji, Unicode Arab), nilai batas (tahun = 0, tahun = 9999)
2. **Intermediate:** Capai coverage >= 80% untuk seluruh proyek. Identifikasi baris yang belum ter-cover dari HTML report dan tulis test yang spesifik untuk baris tersebut
3. **Advanced:** Implementasikan fitur "filter by tahun" dan "sort by judul" menggunakan TDD penuh (Red-Green-Refactor). Tulis minimal 5 test cases sebelum menulis satu baris kode implementasi

## Refleksi dan AI Usage Log

### Pertanyaan Refleksi
1. Apakah menulis test *sebelum* implementasi (TDD) mengubah cara Anda berpikir tentang kode?
2. Test mana yang paling sulit ditulis? Mengapa?
3. Bagaimana unit testing berkaitan dengan prinsip *amanah* (trustworthiness) dalam pengembangan perangkat lunak?

### Template AI Usage Log

| No | Task | AI Tool | Prompt (ringkas) | Output Quality (1-5) | Modifikasi yang Diperlukan | Waktu Hemat |
|----|------|---------|------------------|----------------------|---------------------------|-------------|
| 1 | | | | | | |
| 2 | | | | | | |

> Isi log ini dengan jujur. Penggunaan AI diperbolehkan dan didorong — yang penting adalah **transparansi** dan **evaluasi kritis** terhadap output AI.

## Checklist Penyelesaian

- [ ] `pytest.ini` dan `conftest.py` dengan fixtures (app, client) berfungsi
- [ ] Minimal 5 unit test model (pytest) — PASS
- [ ] Minimal 5 unit test API route (pytest) — PASS
- [ ] Minimal 8 unit test frontend (Jest) — PASS
- [ ] Coverage report dihasilkan dan dianalisis (≥ 70%)
- [ ] Mampu menginterpretasi baris mana yang belum ter-cover
- [ ] 1 fitur baru diimplementasi dengan TDD (Red-Green-Refactor)
- [ ] Minimal 2 edge case test ditulis
- [ ] AI Usage Log diisi untuk sesi ini
- [ ] Kode dan test di-commit ke repository

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
