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

## Tujuan

1. **Menulis** unit test untuk Flask API menggunakan pytest
2. **Menulis** unit test untuk fungsi JavaScript menggunakan Jest
3. **Menjalankan** test suite dan menganalisis coverage report
4. **Menerapkan** TDD (Test-Driven Development) untuk fitur baru

## Persiapan

- Proyek Flask dari Lab 06-07 sudah berjalan
- Install dependencies: `pip install pytest pytest-cov` dan `npm install --save-dev jest`
- Buat folder `tests/` di root proyek

## Langkah-langkah

### Langkah 1: Setup pytest (15 menit)

Buat file konfigurasi pytest:
```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
```

Buat file `tests/conftest.py`:
```python
import pytest
from app import create_app, db

@pytest.fixture
def app():
    """Buat instance aplikasi untuk testing."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    """Test client untuk HTTP requests."""
    return app.test_client()
```

### Langkah 2: Unit Test Backend — Model (20 menit)

```python
# tests/test_models.py
from app.models import Buku, User

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
```

Jalankan: `pytest tests/test_models.py -v`

### Langkah 3: Unit Test Backend — API Routes (20 menit)

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
```

### Langkah 4: Unit Test Frontend — Jest (15 menit)

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
});

describe('validateISBN', () => {
  test('menerima ISBN-13 valid', () => {
    expect(validateISBN('978-3-16-148410-0')).toBe(true);
  });

  test('menolak ISBN invalid', () => {
    expect(validateISBN('12345')).toBe(false);
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
});
```

Jalankan: `npx jest --verbose`

### Langkah 5: Coverage Report (15 menit)

```bash
# Backend coverage
pytest tests/ --cov=app --cov-report=html --cov-report=term
# Buka htmlcov/index.html untuk laporan visual

# Frontend coverage
npx jest --coverage
```

Analisis:
- Identifikasi file/fungsi dengan coverage rendah
- Tulis test tambahan untuk meningkatkan coverage ≥ 70%

### Langkah 6: Mini TDD Challenge (15 menit)

Implementasikan fitur "search buku" dengan TDD:

1. **Red** — Tulis test dulu (akan gagal):
```python
def test_search_books(client):
    # Tambah data dulu
    client.post('/api/buku', data=json.dumps(
        {'judul': 'Python Dasar', 'pengarang': 'Ali', 'tahun': 2025}
    ), content_type='application/json')

    # Test search
    response = client.get('/api/buku/search?q=Python')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['judul'] == 'Python Dasar'
```

2. **Green** — Implementasi minimal:
```python
@buku_bp.route('/api/buku/search')
def search_buku():
    query = request.args.get('q', '')
    results = Buku.query.filter(Buku.judul.ilike(f'%{query}%')).all()
    return jsonify([b.to_dict() for b in results])
```

3. **Refactor** — Perbaiki jika perlu (validasi input, pagination)

## Tantangan Tambahan

1. Tulis test untuk edge cases: input kosong, karakter spesial, SQL injection attempt
2. Capai coverage ≥ 80% untuk seluruh proyek
3. Implementasikan fitur "filter by tahun" menggunakan TDD

## Checklist Penyelesaian

- [ ] `conftest.py` dengan fixtures (app, client) berfungsi
- [ ] Minimal 3 unit test model (pytest) — PASS
- [ ] Minimal 3 unit test API route (pytest) — PASS
- [ ] Minimal 3 unit test frontend (Jest) — PASS
- [ ] Coverage report dihasilkan (≥ 70%)
- [ ] 1 fitur baru diimplementasi dengan TDD (Red-Green-Refactor)
- [ ] AI Usage Log diisi untuk sesi ini

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
