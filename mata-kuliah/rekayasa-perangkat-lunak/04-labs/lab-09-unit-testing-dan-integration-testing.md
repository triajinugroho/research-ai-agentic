# Lab 09: Unit Testing dan Integration Testing

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 8 dari 13 (Minggu 9) |
| **Topik** | pytest, Fixtures, Mocking, TDD, Integration Tests |
| **CPMK** | CPMK-5 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |

## Tujuan

1. **Menulis** unit tests dengan pytest (fixtures, parametrize, mock)
2. **Menerapkan** TDD (Red-Green-Refactor)
3. **Menulis** integration tests untuk Flask API endpoints

## Langkah-langkah

### Langkah 1: Setup pytest (10 menit)
```bash
pip install pytest pytest-cov
mkdir tests
touch tests/__init__.py tests/test_buku_service.py
```

### Langkah 2: Unit Tests dengan Fixtures (25 menit)
```python
# tests/test_buku_service.py
import pytest
from app.services.buku_service import BukuService

@pytest.fixture
def service():
    svc = BukuService()
    svc.tambah({"judul": "Clean Code", "penulis": "Martin", "stok": 5})
    svc.tambah({"judul": "Design Patterns", "penulis": "GoF", "stok": 3})
    return svc

def test_search_ditemukan(service):
    hasil = service.search("Clean")
    assert len(hasil) == 1
    assert hasil[0]["judul"] == "Clean Code"

def test_search_tidak_ditemukan(service):
    assert len(service.search("xyz")) == 0

def test_tambah_buku(service):
    service.tambah({"judul": "Buku Baru", "penulis": "Test", "stok": 1})
    assert len(service.get_all()) == 3

@pytest.mark.parametrize("keyword,expected", [
    ("Clean", 1), ("Design", 1), ("Code", 1), ("xyz", 0)
])
def test_search_parametrize(service, keyword, expected):
    assert len(service.search(keyword)) == expected
```

### Langkah 3: TDD — Red-Green-Refactor (20 menit)
```python
# RED: Tulis test yang gagal
def test_hitung_denda():
    assert hitung_denda(3, 1000) == 3000
    assert hitung_denda(0, 1000) == 0

# GREEN: Implementasi minimal
def hitung_denda(hari, tarif):
    return hari * tarif

# REFACTOR: Tambahkan validasi
def hitung_denda(hari, tarif=1000):
    if hari < 0:
        raise ValueError("Hari tidak boleh negatif")
    return hari * tarif
```

### Langkah 4: Integration Tests (25 menit)
```python
# tests/test_api.py
import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app('testing')
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_get_buku_empty(client):
    resp = client.get('/api/buku')
    assert resp.status_code == 200
    assert resp.json == []

def test_create_buku(client):
    resp = client.post('/api/buku', json={
        'judul': 'Test Book', 'penulis': 'Author', 'stok': 5
    })
    assert resp.status_code == 201
```

### Langkah 5: Coverage Report (10 menit)
```bash
pytest tests/ --cov=app --cov-report=term-missing
# Target: ≥ 70%
```

## Tantangan Tambahan

1. Gunakan `unittest.mock.patch` untuk mock external service
2. Capai 80% code coverage

## Checklist Penyelesaian

- [ ] 5+ unit tests berjalan pass
- [ ] Fixtures dan parametrize digunakan
- [ ] TDD: bukti commit test-first → implement
- [ ] 3+ integration tests untuk API
- [ ] Coverage report ≥ 70%

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
