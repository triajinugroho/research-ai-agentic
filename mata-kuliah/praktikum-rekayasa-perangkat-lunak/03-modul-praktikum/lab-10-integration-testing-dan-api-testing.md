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
| **Referensi Teori** | IF2205 Minggu 10 — Advanced Testing |

## Tujuan

1. **Menulis** (C3) integration test yang menguji interaksi antar komponen
2. **Menguji** (C4) API endpoint secara end-to-end dengan data realistis
3. **Menggunakan** (C3) fixture dan factory pattern untuk test data
4. **Mengotomatisasi** (C3) test execution dengan script

## Konsep Singkat

### Unit Test vs Integration Test

Pada Lab 09, kita menguji komponen **secara terisolasi** (unit test). Pada lab ini, kita menguji bagaimana komponen-komponen **bekerja bersama** (integration test).

```
Unit Test                          Integration Test
===========                        ================
   [Model]  ← test sendiri         [Route] → [Model] → [Database]
   [Route]  ← test sendiri              ↓
   [Utils]  ← test sendiri         Test seluruh alur sekaligus
```

| Aspek | Unit Test | Integration Test |
|-------|-----------|-----------------|
| **Scope** | Satu fungsi/method | Beberapa komponen bersama |
| **Database** | Mock atau in-memory | Database test (nyata/in-memory) |
| **Kecepatan** | Sangat cepat (ms) | Lebih lambat (detik) |
| **Isolasi** | Tinggi | Rendah — test bisa saling mempengaruhi |
| **Bug yang ditemukan** | Logic error di satu fungsi | Masalah integrasi, konfigurasi, data flow |

### Test Database Isolation

Prinsip penting: **setiap test harus mulai dari state yang bersih**. Jika test A menambah data, test B tidak boleh terganggu olehnya.

Strategi isolasi:
1. **SQLite in-memory** (dipakai di lab ini) — database dibuat baru setiap test session
2. **Transaction rollback** — setiap test berjalan dalam transaksi yang di-rollback setelah selesai
3. **Separate test database** — database PostgreSQL terpisah khusus testing

```
Alur Isolasi Test Database:
===========================

  Test 1                  Test 2                  Test 3
  ------                  ------                  ------
  db.create_all()         db.create_all()         db.create_all()
  [insert data]           [insert data]           [insert data]
  [assertions]            [assertions]            [assertions]
  db.drop_all()           db.drop_all()           db.drop_all()

  Setiap test punya database bersih — tidak ada "data bocor" antar test.
```

### Mock vs Real Database

| Pendekatan | Kelebihan | Kekurangan | Kapan Digunakan |
|-----------|-----------|------------|-----------------|
| **Mock (unittest.mock)** | Sangat cepat, terisolasi sempurna | Tidak menguji query SQL sebenarnya | Unit test logic murni |
| **SQLite in-memory** | Cepat, mudah setup, terisolasi per session | Behavior berbeda dari PostgreSQL | Test cepat di CI |
| **PostgreSQL test DB** | Behavior identik dengan production | Lebih lambat, perlu setup DB | Test akhir sebelum deploy |

> **Referensi teori:** Lihat modul IF2205 Minggu 10 — Advanced Testing untuk pembahasan mendalam tentang integration testing strategy, test doubles, dan test automation.

## Persiapan

- Proyek Flask dengan unit test dari Lab 09
- pytest dan pytest-cov terinstall
- Database test (SQLite in-memory) terkonfigurasi di `conftest.py`
- Install httpx untuk API testing (opsional):
  ```bash
  pip install httpx
  ```

## Langkah-langkah

### Langkah 1: Test Data Factory (15 menit)

**Mengapa langkah ini penting?** Factory pattern menghilangkan duplikasi pembuatan data test. Tanpa factory, setiap test harus membuat data dari nol — kode jadi repetitif dan sulit di-maintain.

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
        user.set_password(kwargs.get('password', 'testpass123'))
        db.session.add(user)
        db.session.commit()
        return user

class PeminjamanFactory:
    """Factory untuk membuat data peminjaman test."""

    @classmethod
    def create(cls, user, buku, **kwargs):
        defaults = {
            'user_id': user.id,
            'buku_id': buku.id,
            'tanggal_pinjam': datetime.utcnow(),
            'status': 'dipinjam'
        }
        defaults.update(kwargs)
        peminjaman = Peminjaman(**defaults)
        db.session.add(peminjaman)
        db.session.commit()
        return peminjaman
```

**Verifikasi factory berfungsi:**
```bash
pytest tests/ -v -k "test_create_buku" --tb=short
```

> **Troubleshooting:** Jika `_counter` tidak reset antar test session, tambahkan reset di `conftest.py`:
> ```python
> @pytest.fixture(autouse=True)
> def reset_factories():
>     BukuFactory._counter = 0
>     UserFactory._counter = 0
>     yield
> ```

### Langkah 2: Integration Test — Alur Peminjaman End-to-End (25 menit)

**Mengapa langkah ini penting?** Ini adalah skenario bisnis inti dari Sistem Perpustakaan Digital UAI: mahasiswa register, login, pinjam buku, lihat daftar pinjaman, kembalikan buku. Jika alur ini gagal, aplikasi tidak berguna.

```python
# tests/test_integration_peminjaman.py
import json
from tests.factories import BukuFactory, UserFactory

def test_full_peminjaman_flow(client, app):
    """Test alur lengkap: login -> pinjam -> lihat -> kembalikan.

    Skenario end-to-end:
    1. Mahasiswa login ke sistem
    2. Mahasiswa meminjam buku "Algoritma Python"
    3. Mahasiswa melihat daftar peminjamannya
    4. Mahasiswa mengembalikan buku
    5. Status berubah menjadi "dikembalikan"
    """
    with app.app_context():
        # Setup: buat user dan buku
        user = UserFactory.create(username='mahasiswa_test')
        buku = BukuFactory.create(judul='Algoritma Python')

        # Step 1: Login
        resp = client.post('/api/auth/login', data=json.dumps({
            'username': 'mahasiswa_test',
            'password': 'testpass123'
        }), content_type='application/json')
        assert resp.status_code == 200, f"Login gagal: {resp.json}"
        token = resp.json.get('token')  # Simpan token jika pakai JWT

        # Step 2: Pinjam buku
        headers = {'Content-Type': 'application/json'}
        if token:
            headers['Authorization'] = f'Bearer {token}'

        resp = client.post('/api/peminjaman', data=json.dumps({
            'buku_id': buku.id
        }), headers=headers)
        assert resp.status_code == 201, f"Pinjam gagal: {resp.json}"
        peminjaman_id = resp.json['id']

        # Step 3: Lihat daftar peminjaman
        resp = client.get('/api/peminjaman', headers=headers)
        assert resp.status_code == 200
        assert len(resp.json) == 1
        assert resp.json[0]['buku']['judul'] == 'Algoritma Python'
        assert resp.json[0]['status'] == 'dipinjam'

        # Step 4: Kembalikan buku
        resp = client.patch(f'/api/peminjaman/{peminjaman_id}/return',
                           headers=headers)
        assert resp.status_code == 200
        assert resp.json['status'] == 'dikembalikan'

        # Step 5: Verifikasi — daftar peminjaman aktif kosong
        resp = client.get('/api/peminjaman?status=dipinjam', headers=headers)
        assert resp.status_code == 200
        assert len(resp.json) == 0

def test_register_then_login_then_borrow(client, app):
    """Test alur lengkap mulai dari registrasi user baru.

    Skenario: mahasiswa baru register -> login -> pinjam buku.
    """
    with app.app_context():
        buku = BukuFactory.create(judul='Flask Web Development')

        # Step 1: Register
        resp = client.post('/api/auth/register', data=json.dumps({
            'username': 'mhs_baru',
            'email': 'mhsbaru@uai.ac.id',
            'password': 'SecurePass123!'
        }), content_type='application/json')
        assert resp.status_code == 201, f"Register gagal: {resp.json}"

        # Step 2: Login
        resp = client.post('/api/auth/login', data=json.dumps({
            'username': 'mhs_baru',
            'password': 'SecurePass123!'
        }), content_type='application/json')
        assert resp.status_code == 200

        # Step 3: Pinjam buku
        resp = client.post('/api/peminjaman', data=json.dumps({
            'buku_id': buku.id
        }), content_type='application/json')
        assert resp.status_code == 201

def test_peminjaman_buku_tidak_tersedia(client, app):
    """Test pinjam buku yang sedang dipinjam orang lain (stok habis)."""
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

        # User 2 coba pinjam — harus gagal (stok habis)
        client.post('/api/auth/login', data=json.dumps({
            'username': 'mhs2', 'password': 'testpass123'
        }), content_type='application/json')
        resp = client.post('/api/peminjaman', data=json.dumps({
            'buku_id': buku.id
        }), content_type='application/json')
        assert resp.status_code == 400
        assert 'stok' in resp.json.get('error', '').lower() or \
               'tersedia' in resp.json.get('error', '').lower()

def test_peminjaman_tanpa_login(client):
    """Test akses API peminjaman tanpa autentikasi — harus 401."""
    resp = client.get('/api/peminjaman')
    assert resp.status_code == 401
```

**Jalankan:**
```bash
pytest tests/test_integration_peminjaman.py -v
```

**Expected output:**
```
========================= test session starts ==========================
tests/test_integration_peminjaman.py::test_full_peminjaman_flow PASSED        [ 25%]
tests/test_integration_peminjaman.py::test_register_then_login_then_borrow PASSED [ 50%]
tests/test_integration_peminjaman.py::test_peminjaman_buku_tidak_tersedia PASSED  [ 75%]
tests/test_integration_peminjaman.py::test_peminjaman_tanpa_login PASSED       [100%]

========================= 4 passed in 1.23s ============================
```

> **Troubleshooting:** Jika `test_full_peminjaman_flow` gagal di Step 2 dengan `401`, pastikan mekanisme autentikasi (session/JWT) diterapkan dengan benar. Jika menggunakan Flask session, `client` akan menyimpan session cookie secara otomatis.

### Langkah 3: API Testing dengan httpx/requests (20 menit)

**Mengapa langkah ini penting?** Selain menggunakan Flask test client, kita juga perlu menguji API menggunakan HTTP client sesungguhnya. Ini mensimulasikan bagaimana frontend atau client lain akan memanggil API kita.

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

def test_create_buku_tahun_masa_depan(client, app):
    """Test POST /api/buku dengan tahun di masa depan."""
    with app.app_context():
        resp = client.post('/api/buku', data=json.dumps({
            'judul': 'Test', 'pengarang': 'Test', 'tahun': 2099
        }), content_type='application/json')
        # Tergantung kebijakan: boleh atau tidak?
        assert resp.status_code in [201, 400]

def test_pagination(client, app):
    """Test pagination pada endpoint GET /api/buku."""
    with app.app_context():
        from tests.factories import BukuFactory
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

def test_pagination_invalid_page(client, app):
    """Test pagination dengan page negatif atau nol."""
    with app.app_context():
        resp = client.get('/api/buku?page=0')
        assert resp.status_code in [400, 200]  # Harus handle gracefully

        resp = client.get('/api/buku?page=-1')
        assert resp.status_code in [400, 200]

def test_content_type_json_required(client):
    """Test bahwa API menolak request tanpa Content-Type JSON."""
    resp = client.post('/api/buku', data='not json')
    assert resp.status_code in [400, 415]

def test_method_not_allowed(client):
    """Test method yang tidak didukung endpoint."""
    resp = client.patch('/api/buku')  # PATCH tidak didukung di /api/buku
    assert resp.status_code == 405
```

**Testing dengan httpx (opsional — untuk testing server yang berjalan):**
```python
# tests/test_api_httpx.py
"""
Test ini membutuhkan server Flask yang berjalan di background.
Jalankan: flask run --port 5001 &
Lalu: pytest tests/test_api_httpx.py -v
"""
import httpx
import pytest

BASE_URL = "http://localhost:5001"

@pytest.mark.skipif(
    not is_server_running(),
    reason="Flask server tidak berjalan di port 5001"
)
class TestAPIWithHttpx:
    def test_health_check(self):
        """Test health endpoint via HTTP request sesungguhnya."""
        resp = httpx.get(f"{BASE_URL}/health")
        assert resp.status_code == 200
        data = resp.json()
        assert data['status'] == 'healthy'

    def test_get_buku_list(self):
        """Test GET /api/buku mengembalikan list."""
        resp = httpx.get(f"{BASE_URL}/api/buku")
        assert resp.status_code == 200
        assert isinstance(resp.json(), (list, dict))

    def test_create_and_retrieve_buku(self):
        """Test POST lalu GET — pastikan data tersimpan."""
        # Create
        resp = httpx.post(f"{BASE_URL}/api/buku", json={
            'judul': 'httpx Test Book',
            'pengarang': 'Tester',
            'tahun': 2025
        })
        assert resp.status_code == 201
        buku_id = resp.json()['id']

        # Retrieve
        resp = httpx.get(f"{BASE_URL}/api/buku/{buku_id}")
        assert resp.status_code == 200
        assert resp.json()['judul'] == 'httpx Test Book'
```

**Jalankan validation tests:**
```bash
pytest tests/test_api_validation.py -v
```

**Expected output:**
```
========================= test session starts ==========================
tests/test_api_validation.py::test_create_buku_missing_fields PASSED     [ 14%]
tests/test_api_validation.py::test_create_buku_invalid_tahun PASSED      [ 28%]
tests/test_api_validation.py::test_create_buku_tahun_masa_depan PASSED   [ 42%]
tests/test_api_validation.py::test_pagination PASSED                     [ 57%]
tests/test_api_validation.py::test_pagination_invalid_page PASSED        [ 71%]
tests/test_api_validation.py::test_content_type_json_required PASSED     [ 85%]
tests/test_api_validation.py::test_method_not_allowed PASSED             [100%]

========================= 7 passed in 0.82s ============================
```

> **Troubleshooting:** Jika `test_pagination` gagal dengan `KeyError: 'data'`, periksa apakah endpoint GET `/api/buku` mengembalikan format `{"data": [...], "total": N, "page": N}` saat menerima parameter `page`. Jika belum ada pagination, implementasikan dulu di `app/routes/buku.py`.

### Langkah 4: Test Runner Script (10 menit)

**Mengapa langkah ini penting?** Script otomatis memudahkan menjalankan semua jenis test dalam satu perintah. Ini juga menjadi dasar untuk CI pipeline di Lab 11.

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
[ $UNIT_EXIT -eq 0 ] && echo "[PASS] Unit tests" || echo "[FAIL] Unit tests"
[ $INT_EXIT -eq 0 ] && echo "[PASS] Integration tests" || echo "[FAIL] Integration tests"
[ $API_EXIT -eq 0 ] && echo "[PASS] API tests" || echo "[FAIL] API tests"
[ $COV_EXIT -eq 0 ] && echo "[PASS] Coverage >= 70%" || echo "[FAIL] Coverage < 70%"

# Exit dengan kode error jika ada yang gagal
if [ $UNIT_EXIT -ne 0 ] || [ $INT_EXIT -ne 0 ] || [ $API_EXIT -ne 0 ] || [ $COV_EXIT -ne 0 ]; then
    echo ""
    echo "SOME TESTS FAILED — periksa output di atas."
    exit 1
fi
echo ""
echo "ALL TESTS PASSED!"
```

```bash
chmod +x scripts/run_tests.sh
./scripts/run_tests.sh
```

**Expected output (ringkasan):**
```
=== Summary ===
[PASS] Unit tests
[PASS] Integration tests
[PASS] API tests
[PASS] Coverage >= 70%

ALL TESTS PASSED!
```

### Langkah 5: Analisis Gap dan Test Coverage (15 menit)

**Mengapa langkah ini penting?** Menulis test bukan hanya "agar CI hijau" — tujuannya menemukan bug sebelum user menemukannya. Analisis gap menunjukkan area yang masih rawan.

```bash
# Jalankan coverage dengan detail per-baris
pytest tests/ --cov=app --cov-report=term-missing
```

**Expected output:**
```
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
app/__init__.py                 15      2    87%   22-23
app/models.py                   42      3    93%   45, 67-68
app/routes/buku.py              38      8    79%   55-58, 72-75
app/routes/auth.py              30     10    67%   35-40, 52-56
app/routes/peminjaman.py        35      5    86%   48-52
app/routes/health.py             8      0   100%
----------------------------------------------------------
TOTAL                          168     28    83%
```

**Langkah analisis:**

1. **Identifikasi file dengan coverage rendah:** `auth.py` (67%) — login failure, password reset belum di-test
2. **Periksa baris yang "Missing":** Baris 35-40 di `auth.py` mungkin error handling untuk token expired
3. **Prioritaskan:** Tulis test untuk business-critical path dulu (auth, peminjaman), bukan utility functions
4. **Isi template:**

```markdown
## Gap Analysis

| File | Coverage | Missing Lines | Test yang Perlu Ditambahkan |
|------|----------|---------------|---------------------------|
| auth.py | 67% | 35-40, 52-56 | Test login gagal, test token expired |
| buku.py | 79% | 55-58, 72-75 | Test update buku not found, test delete with peminjaman aktif |
```

### Langkah 6: Dokumentasi dan Commit (15 menit)

**Mengapa langkah ini penting?** Test yang baik tapi tidak di-commit sama saja tidak ada. Pastikan semua test masuk ke repository.

```bash
# Pastikan semua test passing sebelum commit
pytest tests/ -v --tb=short

# Commit semua test
git add tests/
git add scripts/run_tests.sh
git commit -m "test: tambah integration test dan API validation test

- Test alur peminjaman end-to-end (register->login->borrow->return)
- Test API validation (missing fields, invalid data, pagination)
- Test factory pattern untuk data test
- Test runner script untuk otomasi
- Coverage: 83%"

git push
```

## Troubleshooting Umum

| Error | Penyebab | Solusi |
|-------|----------|--------|
| `IntegrityError: UNIQUE constraint failed` | Factory membuat data duplikat | Reset factory counter di fixture `autouse` |
| `DetachedInstanceError` | Mengakses objek di luar app context | Gunakan `with app.app_context():` di test |
| `AssertionError: 401 != 201` | Test tidak login sebelum akses endpoint terproteksi | Tambahkan step login sebelum request |
| `ConnectionError` saat httpx test | Flask server belum berjalan | Jalankan `flask run --port 5001 &` dulu |
| Test lambat (>10 detik) | Terlalu banyak data di factory | Kurangi jumlah data, gunakan `scope='session'` |

## Tantangan Tambahan

1. **Basic:** Tulis integration test untuk fitur search + pagination secara bersamaan (search "Python" lalu paginate hasilnya)
2. **Intermediate:** Gunakan AI untuk generate test cases berdasarkan API specification — evaluasi kualitasnya: berapa test yang langsung PASS tanpa modifikasi? Berapa yang perlu diubah?
3. **Advanced:** Implementasikan test untuk concurrent access — dua user mencoba meminjam buku terakhir yang sama. Gunakan threading atau async untuk mensimulasikan race condition

## Refleksi dan AI Usage Log

### Pertanyaan Refleksi
1. Apa perbedaan utama yang Anda rasakan antara menulis unit test (Lab 09) dan integration test?
2. Mengapa test database isolation penting? Apa yang terjadi jika tidak ada isolasi?
3. Bagaimana mock vs real database mempengaruhi kepercayaan Anda terhadap hasil test?

### Template AI Usage Log

| No | Task | AI Tool | Prompt (ringkas) | Output Quality (1-5) | Modifikasi yang Diperlukan | Waktu Hemat |
|----|------|---------|------------------|----------------------|---------------------------|-------------|
| 1 | | | | | | |
| 2 | | | | | | |

> Isi log ini dengan jujur. Penggunaan AI diperbolehkan dan didorong — yang penting adalah **transparansi** dan **evaluasi kritis** terhadap output AI.

## Checklist Penyelesaian

- [ ] Test data factory (`factories.py`) berfungsi dengan BukuFactory, UserFactory, PeminjamanFactory
- [ ] Minimal 4 integration test alur peminjaman — PASS
- [ ] Minimal 5 API validation test — PASS
- [ ] Test runner script `run_tests.sh` berjalan dan menampilkan summary
- [ ] Coverage report >= 70% dengan analisis per-file
- [ ] Gap analysis terdokumentasi (file mana yang perlu test tambahan)
- [ ] Semua test dan script di-commit ke repository
- [ ] AI Usage Log diisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
