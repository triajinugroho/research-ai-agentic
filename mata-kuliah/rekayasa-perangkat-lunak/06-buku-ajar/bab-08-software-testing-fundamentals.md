# BAB 8: SOFTWARE TESTING FUNDAMENTALS

**Oleh: Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom |
|-----------|-----------|-------------|
| 5.1 | Merancang strategi testing berdasarkan testing levels dan types | C4 (Menganalisis) |
| 5.2 | Mengimplementasikan unit testing dan integration testing dengan pytest | C3 (Menerapkan) |

---

## 8.1 Mengapa Testing Penting?

> "Testing can only show the presence of bugs, not their absence." — Edsger Dijkstra

Meskipun testing tidak bisa membuktikan kode bebas bug, testing tetap krusial:
- **Cost of bugs**: Biaya perbaikan meningkat 100x setelah deployment
- **Confidence**: Testing memberikan kepercayaan bahwa perubahan tidak merusak fitur yang ada
- **Documentation**: Test cases mendokumentasikan expected behavior

### 8.1.1 Testing Pyramid

```
         /\
        /  \          E2E Tests (sedikit, mahal, lambat)
       /    \
      /──────\
     /        \       Integration Tests (sedang)
    /──────────\
   /            \     Unit Tests (banyak, murah, cepat)
  /──────────────\
```

## 8.2 Testing Levels

| Level | Apa yang Ditest | Siapa | Tools |
|-------|----------------|-------|-------|
| **Unit Testing** | Fungsi/method individual | Developer | pytest, Jest |
| **Integration Testing** | Interaksi antar komponen | Developer | pytest, Supertest |
| **System Testing** | Seluruh sistem end-to-end | QA team | Selenium, Playwright |
| **Acceptance Testing** | Kesesuaian dengan requirements | Stakeholder/PO | Manual, Cucumber |

## 8.3 Testing Types

| Type | Fokus | Contoh |
|------|-------|--------|
| **Functional** | Fitur berjalan sesuai requirements | Login berhasil dengan credential valid |
| **Performance** | Kecepatan dan kapasitas | Response time < 3 detik |
| **Security** | Kerentanan keamanan | SQL injection, XSS |
| **Usability** | Kemudahan penggunaan | User bisa checkout dalam < 5 klik |
| **Regression** | Fitur lama tidak rusak setelah perubahan | Re-run semua test setelah bug fix |

## 8.4 Test-Driven Development (TDD)

### 8.4.1 Siklus Red-Green-Refactor

```
  ┌─── RED ─────────────────────┐
  │ Tulis test yang GAGAL        │
  └──────────┬──────────────────┘
             │
  ┌──────────▼──────────────────┐
  │ GREEN                        │
  │ Tulis kode MINIMAL agar pass │
  └──────────┬──────────────────┘
             │
  ┌──────────▼──────────────────┐
  │ REFACTOR                     │
  │ Perbaiki kode tanpa          │
  │ mengubah perilaku            │
  └──────────┬──────────────────┘
             │
             └───── Ulangi ──────▶
```

### 8.4.2 Contoh TDD dengan pytest

```python
# test_buku_service.py — RED: Tulis test dulu
def test_search_buku_by_judul():
    service = BukuService()
    service.tambah(Buku(judul="Algoritma Dasar", penulis="Ahmad"))
    service.tambah(Buku(judul="Struktur Data", penulis="Budi"))
    
    hasil = service.search("Algoritma")
    
    assert len(hasil) == 1
    assert hasil[0].judul == "Algoritma Dasar"

def test_search_buku_tidak_ditemukan():
    service = BukuService()
    hasil = service.search("xyz")
    assert len(hasil) == 0
```

```python
# buku_service.py — GREEN: Implementasi minimal
class BukuService:
    def __init__(self):
        self._buku = []
    
    def tambah(self, buku):
        self._buku.append(buku)
    
    def search(self, keyword):
        return [b for b in self._buku if keyword.lower() in b.judul.lower()]
```

## 8.5 Unit Testing dengan pytest

### 8.5.1 Dasar pytest

```python
# test_calculator.py
def test_tambah():
    assert tambah(2, 3) == 5

def test_tambah_negatif():
    assert tambah(-1, 1) == 0

def test_bagi_nol():
    import pytest
    with pytest.raises(ZeroDivisionError):
        bagi(10, 0)
```

### 8.5.2 Fixtures

```python
import pytest

@pytest.fixture
def sample_buku():
    return Buku(judul="Clean Code", penulis="Robert Martin", stok=5)

@pytest.fixture
def buku_service():
    service = BukuService()
    service.tambah(Buku(judul="Clean Code", penulis="Martin"))
    service.tambah(Buku(judul="Design Patterns", penulis="GoF"))
    return service

def test_search_with_fixture(buku_service):
    hasil = buku_service.search("Clean")
    assert len(hasil) == 1

def test_stok_buku(sample_buku):
    assert sample_buku.stok == 5
```

### 8.5.3 Mocking

```python
from unittest.mock import patch, MagicMock

def test_kirim_notifikasi():
    with patch('services.email_service.send') as mock_send:
        mock_send.return_value = True
        
        result = proses_peminjaman(user_id=1, buku_id=1)
        
        assert result == True
        mock_send.assert_called_once()
```

### 8.5.4 Code Coverage

```bash
# Jalankan test dengan coverage
pytest --cov=app --cov-report=html tests/

# Hasil: htmlcov/index.html
# Target: minimum 80% coverage
```

## 8.6 Integration Testing Flask API

```python
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

def test_get_semua_buku(client):
    response = client.get('/api/buku')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_tambah_buku(client):
    response = client.post('/api/buku', json={
        'judul': 'Clean Code',
        'penulis': 'Robert Martin',
        'stok': 5
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Buku berhasil ditambahkan'

def test_buku_tidak_ditemukan(client):
    response = client.get('/api/buku/999')
    assert response.status_code == 404
```

---

## AI Corner: AI untuk Testing (Level: Advanced)

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| Generate test cases | "Buatkan pytest unit tests untuk class BukuService dengan method search, tambah, hapus" | Review edge cases — AI sering miss boundary conditions |
| Test coverage gaps | "Analisis kode ini dan identifikasi test cases yang belum di-cover: [paste]" | Gunakan bersama coverage report |
| TDD guidance | "Tulis test-first untuk fitur 'mahasiswa bisa memperpanjang peminjaman 1x'" | Pastikan test benar-benar gagal sebelum implementasi |

---

## Latihan Soal

### Level Dasar (C1-C2)
1. Jelaskan testing pyramid dan 4 testing levels.
2. Apa perbedaan black-box dan white-box testing?
3. Jelaskan siklus TDD Red-Green-Refactor.

### Level Menengah (C3-C4)
4. Tulis 5 unit tests untuk fungsi `validate_email(email)` menggunakan pytest.
5. Implementasikan TDD untuk fitur "checkout pesanan" — tulis test dulu, lalu implementasi.
6. Buatlah integration test untuk endpoint POST `/api/peminjaman`.

### Level Mahir (C5-C6)
7. Rancang strategi testing komprehensif untuk Sistem Antrian Puskesmas — cover semua testing levels.
8. Evaluasi: apakah 100% code coverage menjamin software bebas bug? Jelaskan.

---

## Rangkuman

1. **Testing pyramid**: banyak unit test (cepat, murah), sedikit E2E test (lambat, mahal).
2. **Testing levels**: Unit → Integration → System → Acceptance.
3. **TDD** (Red-Green-Refactor) menghasilkan kode yang testable by design.
4. **pytest** adalah framework testing Python — fixtures, parametrize, mocking, coverage.
5. **Integration testing** Flask menggunakan test client untuk menguji API endpoints.
6. **Code coverage** adalah metrik, bukan jaminan — target 80% tapi fokus pada critical paths.

---

## Referensi

1. Myers, G. J. et al. (2011). *The Art of Software Testing* (3rd ed.). Wiley.
2. Beck, K. (2003). *Test Driven Development: By Example*. Addison-Wesley.
3. pytest documentation. (2024). *pytest: helps you write better programs*. docs.pytest.org.
4. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 8. Pearson.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
