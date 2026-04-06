# Lab 10: Integration Testing dan API Testing

## Informasi Praktikum

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Praktikum** | 9 dari 13 (Minggu 10) |
| **Topik** | Integration Testing, API Testing, Test Automation |
| **CPMK** | CPMK-5 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 09 (Unit Testing) selesai |

## Tujuan

1. **Menulis** integration test yang menguji interaksi antar komponen
2. **Menguji** API endpoint secara end-to-end dengan data realistis
3. **Menggunakan** fixture dan factory pattern untuk test data
4. **Mengotomatisasi** test execution dengan script

## Persiapan

- Proyek Flask dengan unit test dari Lab 09
- pytest dan pytest-cov terinstall
- Database test (SQLite in-memory) terkonfigurasi

## Langkah-langkah

### Langkah 1: Test Data Factory (15 menit)

Buat factory untuk generate test data secara konsisten:

```python
# tests/factories.py
from app.models import Buku, User, Peminjaman
from app import db
from datetime import datetime, timedelta

class BukuFactory:
    """Factory untuk membuat data buku test."""
    _counter = 0

    @classmethod
    def create(cls, **kwargs):
        cls._counter += 1
        defaults = {
            'judul': f'Buku Test {cls._counter}',
            'pengarang': f'Pengarang {cls._counter}',
            'tahun': 2025,
            'isbn': f'978-000-000-{cls._counter:04d}'
        }
        defaults.update(kwargs)
        buku = Buku(**defaults)
        db.session.add(buku)
        db.session.commit()
        return buku

class UserFactory:
    """Factory untuk membuat data user test."""
    _counter = 0

    @classmethod
    def create(cls, **kwargs):
        cls._counter += 1
        defaults = {
            'username': f'user_test_{cls._counter}',
            'email': f'user{cls._counter}@uai.ac.id'
        }
        defaults.update(kwargs)
        user = User(**defaults)
        user.set_password('testpass123')
        db.session.add(user)
        db.session.commit()
        return user
```

### Langkah 2: Integration Test — Alur Peminjaman (25 menit)

```python
# tests/test_integration_peminjaman.py
import json
from tests.factories import BukuFactory, UserFactory

def test_full_peminjaman_flow(client, app):
    """Test alur lengkap: login → pinjam → lihat → kembalikan."""
    with app.app_context():
        # Setup: buat user dan buku
        user = UserFactory.create(username='mahasiswa_test')
        buku = BukuFactory.create(judul='Algoritma Python')

        # Step 1: Login
        resp = client.post('/api/auth/login', data=json.dumps({
            'username': 'mahasiswa_test',
            'password': 'testpass123'
        }), content_type='application/json')
        assert resp.status_code == 200

        # Step 2: Pinjam buku
        resp = client.post('/api/peminjaman', data=json.dumps({
            'buku_id': buku.id
        }), content_type='application/json')
        assert resp.status_code == 201
        peminjaman_id = resp.json['id']

        # Step 3: Lihat daftar peminjaman
        resp = client.get('/api/peminjaman')
        assert resp.status_code == 200
        assert len(resp.json) == 1
        assert resp.json[0]['buku']['judul'] == 'Algoritma Python'

        # Step 4: Kembalikan buku
        resp = client.patch(f'/api/peminjaman/{peminjaman_id}/return')
        assert resp.status_code == 200
        assert resp.json['status'] == 'dikembalikan'

def test_peminjaman_buku_tidak_tersedia(client, app):
    """Test pinjam buku yang sedang dipinjam orang lain."""
    with app.app_context():
        user1 = UserFactory.create(username='mhs1')
        user2 = UserFactory.create(username='mhs2')
        buku = BukuFactory.create(judul='Flask Web', stok=1)

        # User 1 pinjam
        client.post('/api/auth/login', data=json.dumps({
            'username': 'mhs1', 'password': 'testpass123'
        }), content_type='application/json')
        client.post('/api/peminjaman', data=json.dumps({
            'buku_id': buku.id
        }), content_type='application/json')

        # User 2 coba pinjam — harus gagal
        client.post('/api/auth/login', data=json.dumps({
            'username': 'mhs2', 'password': 'testpass123'
        }), content_type='application/json')
        resp = client.post('/api/peminjaman', data=json.dumps({
            'buku_id': buku.id
        }), content_type='application/json')
        assert resp.status_code == 400

def test_peminjaman_tanpa_login(client):
    """Test akses API peminjaman tanpa autentikasi."""
    resp = client.get('/api/peminjaman')
    assert resp.status_code == 401
```

### Langkah 3: API Testing dengan Request Validation (20 menit)

```python
# tests/test_api_validation.py
import json

def test_create_buku_missing_fields(client, app):
    """Test POST /api/buku dengan field yang hilang."""
    with app.app_context():
        # Tanpa judul
        resp = client.post('/api/buku', data=json.dumps({
            'pengarang': 'Test'
        }), content_type='application/json')
        assert resp.status_code == 400
        assert 'judul' in resp.json.get('error', '').lower()

def test_create_buku_invalid_tahun(client, app):
    """Test POST /api/buku dengan tahun invalid."""
    with app.app_context():
        resp = client.post('/api/buku', data=json.dumps({
            'judul': 'Test', 'pengarang': 'Test', 'tahun': -1
        }), content_type='application/json')
        assert resp.status_code == 400

def test_pagination(client, app):
    """Test pagination pada endpoint GET /api/buku."""
    with app.app_context():
        # Buat 15 buku
        for i in range(15):
            BukuFactory.create(judul=f'Buku {i+1}')

        # Page 1 (default 10 per page)
        resp = client.get('/api/buku?page=1&per_page=10')
        assert resp.status_code == 200
        assert len(resp.json['data']) == 10

        # Page 2
        resp = client.get('/api/buku?page=2&per_page=10')
        assert len(resp.json['data']) == 5

def test_content_type_json_required(client):
    """Test bahwa API menolak request tanpa Content-Type JSON."""
    resp = client.post('/api/buku', data='not json')
    assert resp.status_code in [400, 415]
```

### Langkah 4: Test Runner Script (15 menit)

```bash
#!/bin/bash
# scripts/run_tests.sh
echo "=== Running All Tests ==="
echo ""

echo "--- Unit Tests ---"
pytest tests/test_models.py tests/test_routes.py -v
UNIT_EXIT=$?

echo ""
echo "--- Integration Tests ---"
pytest tests/test_integration_peminjaman.py -v
INT_EXIT=$?

echo ""
echo "--- API Validation Tests ---"
pytest tests/test_api_validation.py -v
API_EXIT=$?

echo ""
echo "--- Coverage Report ---"
pytest tests/ --cov=app --cov-report=term --cov-fail-under=70
COV_EXIT=$?

echo ""
echo "=== Summary ==="
[ $UNIT_EXIT -eq 0 ] && echo "✓ Unit tests PASSED" || echo "✗ Unit tests FAILED"
[ $INT_EXIT -eq 0 ] && echo "✓ Integration tests PASSED" || echo "✗ Integration tests FAILED"
[ $API_EXIT -eq 0 ] && echo "✓ API tests PASSED" || echo "✗ API tests FAILED"
[ $COV_EXIT -eq 0 ] && echo "✓ Coverage ≥ 70%" || echo "✗ Coverage < 70%"
```

```bash
chmod +x scripts/run_tests.sh
./scripts/run_tests.sh
```

### Langkah 5: Analisis dan Dokumentasi (15 menit)

1. **Identifikasi gap**: Endpoint mana yang belum ter-cover?
2. **Tulis test tambahan** untuk endpoint yang belum diuji
3. **Isi AI Usage Log** — catat jika menggunakan AI untuk generate test

## Tantangan Tambahan

1. Tulis integration test untuk fitur search + pagination secara bersamaan
2. Gunakan AI untuk generate test cases — evaluasi kualitasnya
3. Implementasikan test untuk concurrent access (2 user pinjam buku yang sama)

## Checklist Penyelesaian

- [ ] Test data factory (`factories.py`) berfungsi
- [ ] Minimal 3 integration test — PASS
- [ ] Minimal 3 API validation test — PASS
- [ ] Test runner script berjalan
- [ ] Coverage report ≥ 70%
- [ ] Gap analysis terdokumentasi
- [ ] AI Usage Log diisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
