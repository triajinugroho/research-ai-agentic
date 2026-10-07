# Lab 09: Unit Testing dan Integration Testing

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 8 dari 13 (Minggu 9) |
| **Topik** | pytest, Fixtures, Parametrize, Mocking, TDD, Integration Tests, Coverage |
| **CPMK** | CPMK-5 (Sub-CPMK 5.1, 5.2) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 01-07 selesai, Flask app berjalan, pemahaman dasar Python functions |

## Tujuan

1. **Menulis** (C3) unit tests dengan pytest menggunakan fixtures, parametrize, dan mocking
2. **Menerapkan** (C3) siklus TDD — Red-Green-Refactor — untuk mengembangkan fitur baru
3. **Mengimplementasikan** (C3) integration tests untuk Flask API endpoints
4. **Menganalisis** (C4) code coverage report dan mengidentifikasi area yang belum teruji

## Konsep Singkat

### Mengapa Testing Penting?

Bayangkan Anda membangun sistem perpustakaan digital untuk UAI. Tanpa testing, setiap perubahan kode berpotensi merusak fitur yang sudah berjalan — mahasiswa tidak bisa meminjam buku, denda salah hitung, atau data hilang. Testing adalah "jaring pengaman" (*safety net*) yang memastikan software berfungsi sesuai spesifikasi.

### Piramida Testing (*Testing Pyramid*)

```
        /\
       /  \       E2E Tests (sedikit, lambat, mahal)
      /----\
     /      \     Integration Tests (sedang)
    /--------\
   /          \   Unit Tests (banyak, cepat, murah)
  /____________\
```

- **Unit Test**: Menguji satu fungsi/method secara terisolasi. Cepat (milidetik), mudah di-debug.
- **Integration Test**: Menguji interaksi antar komponen (misalnya API endpoint + database).
- **E2E Test**: Menguji alur lengkap dari perspektif pengguna (dibahas di Lab 10).

### Konsep Kunci pytest

| Konsep | Penjelasan | Kapan Digunakan |
|--------|-----------|-----------------|
| **Fixture** | Fungsi setup yang menyiapkan data/objek untuk test | Ketika beberapa test butuh data yang sama |
| **Parametrize** | Menjalankan test yang sama dengan input berbeda | Ketika menguji banyak variasi input-output |
| **Mock/Patch** | Mengganti dependensi eksternal dengan objek palsu | Ketika test tidak boleh bergantung pada DB/API asli |
| **Assert** | Pernyataan yang harus bernilai True agar test pass | Setiap test harus punya minimal 1 assertion |

### Test-Driven Development (TDD)

TDD adalah praktik menulis test **sebelum** menulis kode implementasi:

```
  RED              GREEN            REFACTOR
  (Tulis test,     (Tulis kode      (Perbaiki kode,
   test gagal)      minimal agar     test tetap pass)
      |              test pass)         |
      v                 |               v
   [FAIL] ---------> [PASS] -------> [PASS]
      ^                                 |
      |_________________________________|
            (Ulangi untuk fitur baru)
```

Manfaat TDD: (1) spesifikasi yang jelas sebelum coding, (2) kode minimal dan fokus, (3) refactoring aman karena ada test yang menjaga.

### Analogi Dunia Nyata

Seperti kontrol kualitas di pabrik: **unit test** = cek setiap komponen elektronik, **integration test** = cek komponen terpasang benar di papan sirkuit, **E2E test** = cek seluruh perangkat berfungsi dari perspektif pengguna.

## Persiapan

### Tools yang Dibutuhkan

```bash
# Pastikan berada di root directory proyek
pip install pytest pytest-cov pytest-mock flask

# Verifikasi instalasi
pytest --version
# Expected output: pytest 8.x.x
```

### Struktur Direktori

```
proyek-perpustakaan/
├── app/
│   ├── __init__.py          # create_app()
│   ├── models.py            # SQLAlchemy models
│   └── services/
│       ├── __init__.py
│       └── buku_service.py  # Business logic
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Shared fixtures
│   ├── test_buku_service.py # Unit tests
│   └── test_api.py          # Integration tests
├── requirements.txt
└── pytest.ini               # (opsional) konfigurasi pytest
```

### File Pendukung: BukuService

Pastikan file `app/services/buku_service.py` ada:

```python
# app/services/buku_service.py
class BukuService:
    """Service layer untuk manajemen buku perpustakaan."""

    def __init__(self):
        self._buku_list = []

    def tambah(self, buku: dict) -> dict:
        """Tambahkan buku baru ke koleksi."""
        buku["id"] = len(self._buku_list) + 1
        self._buku_list.append(buku)
        return buku

    def get_all(self) -> list:
        """Ambil semua buku."""
        return self._buku_list

    def get_by_id(self, buku_id: int) -> dict | None:
        """Cari buku berdasarkan ID."""
        for buku in self._buku_list:
            if buku["id"] == buku_id:
                return buku
        return None

    def search(self, keyword: str) -> list:
        """Cari buku berdasarkan keyword di judul atau penulis."""
        keyword_lower = keyword.lower()
        return [
            b for b in self._buku_list
            if keyword_lower in b["judul"].lower()
            or keyword_lower in b["penulis"].lower()
        ]

    def update_stok(self, buku_id: int, jumlah: int) -> dict | None:
        """Update stok buku. Jumlah bisa negatif (pengurangan)."""
        buku = self.get_by_id(buku_id)
        if buku is None:
            return None
        buku["stok"] += jumlah
        if buku["stok"] < 0:
            raise ValueError("Stok tidak boleh negatif")
        return buku
```

## Langkah-langkah

### Langkah 1: Setup pytest dan Shared Fixtures (10 menit)

**Mengapa:** Fixtures menghilangkan duplikasi kode setup di setiap test. File `conftest.py` dikenali pytest secara otomatis — semua fixture di dalamnya tersedia untuk seluruh test di direktori tersebut.

```bash
# Buat direktori dan file
mkdir -p tests
touch tests/__init__.py tests/conftest.py tests/test_buku_service.py tests/test_api.py
```

```python
# tests/conftest.py
import pytest
from app.services.buku_service import BukuService


@pytest.fixture
def service():
    """Fixture: BukuService dengan 2 buku sample."""
    svc = BukuService()
    svc.tambah({"judul": "Clean Code", "penulis": "Robert C. Martin", "stok": 5})
    svc.tambah({"judul": "Design Patterns", "penulis": "GoF", "stok": 3})
    return svc


@pytest.fixture
def empty_service():
    """Fixture: BukuService kosong."""
    return BukuService()
```

**Jalankan untuk memastikan setup benar:**

```bash
pytest tests/ -v
# Expected output:
# =================== no tests ran in 0.01s ===================
```

> **Troubleshooting:** Jika muncul `ModuleNotFoundError: No module named 'app'`, pastikan Anda menjalankan pytest dari root directory proyek (bukan dari dalam folder `tests/`). Alternatif: tambahkan file `pytest.ini` dengan isi `[pytest]` dan `pythonpath = .`

**Estimasi waktu:** 10 menit

---

### Langkah 2: Unit Tests dengan Fixtures dan Parametrize (20 menit)

**Mengapa:** Unit test memastikan setiap fungsi bekerja benar secara terisolasi. `@pytest.fixture` menyiapkan data, `@pytest.mark.parametrize` menjalankan test yang sama dengan banyak input tanpa duplikasi kode.

```python
# tests/test_buku_service.py
import pytest
from app.services.buku_service import BukuService


# --- Test fungsi search ---

def test_search_ditemukan(service):
    """Test: pencarian keyword yang ada mengembalikan hasil."""
    hasil = service.search("Clean")
    assert len(hasil) == 1
    assert hasil[0]["judul"] == "Clean Code"


def test_search_tidak_ditemukan(service):
    """Test: pencarian keyword yang tidak ada mengembalikan list kosong."""
    assert len(service.search("xyz")) == 0


def test_search_case_insensitive(service):
    """Test: pencarian tidak case-sensitive."""
    hasil_lower = service.search("clean")
    hasil_upper = service.search("CLEAN")
    assert len(hasil_lower) == 1
    assert len(hasil_upper) == 1


@pytest.mark.parametrize("keyword, expected_count", [
    ("Clean", 1),
    ("Design", 1),
    ("Martin", 1),       # Cari berdasarkan penulis
    ("GoF", 1),
    ("Python", 0),       # Tidak ada
    ("", 2),             # String kosong = semua cocok
])
def test_search_parametrize(service, keyword, expected_count):
    """Test: berbagai skenario pencarian dengan parametrize."""
    assert len(service.search(keyword)) == expected_count


# --- Test fungsi tambah ---

def test_tambah_buku(service):
    """Test: menambah buku meningkatkan jumlah koleksi."""
    service.tambah({"judul": "Refactoring", "penulis": "Fowler", "stok": 2})
    assert len(service.get_all()) == 3


def test_tambah_buku_mendapat_id(empty_service):
    """Test: buku yang ditambahkan mendapat ID otomatis."""
    buku = empty_service.tambah({"judul": "Test", "penulis": "A", "stok": 1})
    assert buku["id"] == 1


# --- Test fungsi get_by_id ---

def test_get_by_id_ditemukan(service):
    """Test: get_by_id dengan ID valid mengembalikan buku."""
    buku = service.get_by_id(1)
    assert buku is not None
    assert buku["judul"] == "Clean Code"


def test_get_by_id_tidak_ditemukan(service):
    """Test: get_by_id dengan ID invalid mengembalikan None."""
    assert service.get_by_id(999) is None


# --- Test fungsi update_stok ---

def test_update_stok_berhasil(service):
    """Test: update stok menambah/mengurangi dengan benar."""
    buku = service.update_stok(1, -2)  # Kurangi 2
    assert buku["stok"] == 3


def test_update_stok_negatif_raises_error(service):
    """Test: stok negatif memunculkan ValueError."""
    with pytest.raises(ValueError, match="Stok tidak boleh negatif"):
        service.update_stok(1, -100)  # Stok awal 5, kurangi 100


def test_update_stok_buku_tidak_ada(service):
    """Test: update stok buku yang tidak ada mengembalikan None."""
    result = service.update_stok(999, 5)
    assert result is None
```

**Jalankan tests:**

```bash
pytest tests/test_buku_service.py -v
```

**Expected output:**

```
tests/test_buku_service.py::test_search_ditemukan PASSED
tests/test_buku_service.py::test_search_tidak_ditemukan PASSED
tests/test_buku_service.py::test_search_case_insensitive PASSED
tests/test_buku_service.py::test_search_parametrize[Clean-1] PASSED
tests/test_buku_service.py::test_search_parametrize[Design-1] PASSED
tests/test_buku_service.py::test_search_parametrize[Martin-1] PASSED
tests/test_buku_service.py::test_search_parametrize[GoF-1] PASSED
tests/test_buku_service.py::test_search_parametrize[Python-0] PASSED
tests/test_buku_service.py::test_search_parametrize[-2] PASSED
tests/test_buku_service.py::test_tambah_buku PASSED
tests/test_buku_service.py::test_tambah_buku_mendapat_id PASSED
tests/test_buku_service.py::test_get_by_id_ditemukan PASSED
tests/test_buku_service.py::test_get_by_id_tidak_ditemukan PASSED
tests/test_buku_service.py::test_update_stok_berhasil PASSED
tests/test_buku_service.py::test_update_stok_negatif_raises_error PASSED
tests/test_buku_service.py::test_update_stok_buku_tidak_ada PASSED

=================== 16 passed in 0.05s ===================
```

> **Troubleshooting:** Jika test `test_search_parametrize[-2]` membingungkan, itu karena parameter string kosong `""` ditampilkan sebagai `-` di output. Ini normal.

**Estimasi waktu:** 20 menit

---

### Langkah 3: Mocking External Dependencies (15 menit)

**Mengapa:** Dalam dunia nyata, service sering bergantung pada API eksternal (misalnya cek ISBN ke API Google Books). Mocking mengganti dependensi tersebut dengan objek palsu sehingga unit test tetap cepat dan terisolasi.

```python
# tests/test_mocking.py
from unittest.mock import patch, MagicMock
from app.services.buku_service import BukuService


def test_mock_external_api():
    """
    Skenario: BukuService.validasi_isbn() memanggil API eksternal.
    Kita mock API tersebut agar test tidak bergantung pada internet.
    """
    service = BukuService()

    # Simulasikan fungsi yang memanggil API eksternal
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "totalItems": 1,
        "items": [{"volumeInfo": {"title": "Clean Code"}}]
    }

    with patch("requests.get", return_value=mock_response) as mock_get:
        # Jika BukuService punya method validasi_isbn:
        # result = service.validasi_isbn("978-0132350884")
        # assert result == True

        # Demonstrasi: verifikasi bahwa mock dipanggil dengan benar
        import requests
        resp = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:978-0132350884")
        assert resp.status_code == 200
        assert resp.json()["totalItems"] == 1
        mock_get.assert_called_once()


def test_mock_database_connection():
    """
    Skenario: Mock koneksi database yang gagal.
    Pastikan service menangani error dengan benar.
    """
    with patch("app.services.buku_service.BukuService.get_all") as mock_get_all:
        mock_get_all.side_effect = ConnectionError("Database tidak tersedia")

        service = BukuService()
        try:
            service.get_all()
            assert False, "Seharusnya raise ConnectionError"
        except ConnectionError as e:
            assert "Database tidak tersedia" in str(e)
```

**Konsep penting Mock:**

| Method Mock | Kegunaan | Contoh |
|-------------|----------|--------|
| `return_value` | Menentukan nilai kembalian | `mock.return_value = 42` |
| `side_effect` | Menentukan efek samping (exception, dll) | `mock.side_effect = ValueError()` |
| `assert_called_once()` | Verifikasi mock dipanggil tepat 1x | `mock.assert_called_once()` |
| `assert_called_with(args)` | Verifikasi argumen pemanggilan | `mock.assert_called_with("isbn")` |

**Estimasi waktu:** 15 menit

---

### Langkah 4: TDD — Red-Green-Refactor (20 menit)

**Mengapa:** TDD memaksa Anda berpikir tentang *spesifikasi* sebelum *implementasi*. Ini menghasilkan kode yang lebih terarah dan testable. Di industri, TDD banyak digunakan di perusahaan seperti Gojek dan Tokopedia untuk fitur-fitur kritis.

**Skenario:** Implementasikan fungsi `hitung_denda()` untuk perpustakaan.

**Langkah 4a: RED — Tulis test yang gagal**

```python
# tests/test_denda.py
import pytest


def test_hitung_denda_normal():
    """3 hari terlambat x Rp1.000 = Rp3.000"""
    from app.services.denda import hitung_denda
    assert hitung_denda(hari_terlambat=3, tarif_per_hari=1000) == 3000


def test_hitung_denda_nol_hari():
    """0 hari terlambat = Rp0 (tidak ada denda)"""
    from app.services.denda import hitung_denda
    assert hitung_denda(hari_terlambat=0, tarif_per_hari=1000) == 0


def test_hitung_denda_hari_negatif():
    """Hari negatif = ValueError"""
    from app.services.denda import hitung_denda
    with pytest.raises(ValueError, match="tidak boleh negatif"):
        hitung_denda(hari_terlambat=-1, tarif_per_hari=1000)


def test_hitung_denda_maksimum():
    """Denda tidak boleh melebihi Rp50.000"""
    from app.services.denda import hitung_denda
    assert hitung_denda(hari_terlambat=100, tarif_per_hari=1000) == 50000
```

```bash
pytest tests/test_denda.py -v
# Expected: 4 FAILED (ModuleNotFoundError — belum ada implementasi)
```

**Langkah 4b: GREEN — Tulis implementasi minimal**

```python
# app/services/denda.py
DENDA_MAKSIMUM = 50000  # Rp50.000


def hitung_denda(hari_terlambat: int, tarif_per_hari: int = 1000) -> int:
    """
    Hitung denda keterlambatan pengembalian buku.

    Args:
        hari_terlambat: Jumlah hari terlambat (>= 0)
        tarif_per_hari: Tarif denda per hari (default Rp1.000)

    Returns:
        Total denda dalam Rupiah (maksimum Rp50.000)

    Raises:
        ValueError: Jika hari_terlambat negatif
    """
    if hari_terlambat < 0:
        raise ValueError("Jumlah hari tidak boleh negatif")

    denda = hari_terlambat * tarif_per_hari
    return min(denda, DENDA_MAKSIMUM)
```

```bash
pytest tests/test_denda.py -v
# Expected: 4 PASSED
```

**Langkah 4c: REFACTOR — Perbaiki tanpa merusak test**

```python
# app/services/denda.py (versi refactored)
from dataclasses import dataclass

DENDA_MAKSIMUM = 50000


@dataclass
class HasilDenda:
    """Hasil perhitungan denda dengan detail."""
    hari_terlambat: int
    tarif_per_hari: int
    total: int
    is_maksimum: bool


def hitung_denda(hari_terlambat: int, tarif_per_hari: int = 1000) -> int:
    """Hitung denda keterlambatan (backward compatible)."""
    if hari_terlambat < 0:
        raise ValueError("Jumlah hari tidak boleh negatif")
    denda = hari_terlambat * tarif_per_hari
    return min(denda, DENDA_MAKSIMUM)


def hitung_denda_detail(hari_terlambat: int, tarif_per_hari: int = 1000) -> HasilDenda:
    """Hitung denda dengan detail lengkap (fungsi baru dari refactoring)."""
    total = hitung_denda(hari_terlambat, tarif_per_hari)
    return HasilDenda(
        hari_terlambat=hari_terlambat,
        tarif_per_hari=tarif_per_hari,
        total=total,
        is_maksimum=(total == DENDA_MAKSIMUM)
    )
```

```bash
pytest tests/test_denda.py -v
# Expected: masih 4 PASSED (refactor tidak merusak test yang ada)
```

> **Tips:** Commit di setiap tahap TDD: `git commit -m "test: RED - test hitung_denda"`, lalu `git commit -m "feat: GREEN - implementasi hitung_denda"`, lalu `git commit -m "refactor: tambah HasilDenda dataclass"`.

**Estimasi waktu:** 20 menit

---

### Langkah 5: Integration Tests untuk Flask API (20 menit)

**Mengapa:** Integration test memverifikasi bahwa komponen-komponen (route, service, database) bekerja bersama dengan benar. Berbeda dari unit test yang mengisolasi setiap komponen.

```python
# tests/test_api.py
import pytest
from app import create_app, db


@pytest.fixture
def client():
    """Fixture: Flask test client dengan database sementara."""
    app = create_app("testing")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()


# --- Test GET endpoints ---

def test_get_buku_empty(client):
    """Test: GET /api/buku pada database kosong mengembalikan list kosong."""
    resp = client.get("/api/buku")
    assert resp.status_code == 200
    assert resp.json == []


def test_get_buku_not_found(client):
    """Test: GET /api/buku/999 mengembalikan 404."""
    resp = client.get("/api/buku/999")
    assert resp.status_code == 404


# --- Test POST endpoint ---

def test_create_buku_berhasil(client):
    """Test: POST /api/buku dengan data valid mengembalikan 201."""
    resp = client.post("/api/buku", json={
        "judul": "Clean Code",
        "penulis": "Robert C. Martin",
        "stok": 5
    })
    assert resp.status_code == 201
    assert resp.json["judul"] == "Clean Code"
    assert "id" in resp.json


def test_create_buku_tanpa_judul(client):
    """Test: POST /api/buku tanpa judul mengembalikan 400."""
    resp = client.post("/api/buku", json={
        "penulis": "Author",
        "stok": 5
    })
    assert resp.status_code == 400


def test_create_then_get(client):
    """Test: POST lalu GET — data konsisten."""
    # Buat buku
    client.post("/api/buku", json={
        "judul": "Design Patterns", "penulis": "GoF", "stok": 3
    })

    # Ambil semua buku
    resp = client.get("/api/buku")
    assert resp.status_code == 200
    assert len(resp.json) == 1
    assert resp.json[0]["judul"] == "Design Patterns"


# --- Test PUT endpoint ---

def test_update_buku(client):
    """Test: PUT /api/buku/<id> mengupdate data."""
    # Buat dulu
    create_resp = client.post("/api/buku", json={
        "judul": "Old Title", "penulis": "Author", "stok": 1
    })
    buku_id = create_resp.json["id"]

    # Update
    resp = client.put(f"/api/buku/{buku_id}", json={
        "judul": "New Title", "stok": 10
    })
    assert resp.status_code == 200
    assert resp.json["judul"] == "New Title"


# --- Test DELETE endpoint ---

def test_delete_buku(client):
    """Test: DELETE /api/buku/<id> menghapus data."""
    create_resp = client.post("/api/buku", json={
        "judul": "To Delete", "penulis": "Author", "stok": 1
    })
    buku_id = create_resp.json["id"]

    resp = client.delete(f"/api/buku/{buku_id}")
    assert resp.status_code == 200

    # Verifikasi sudah terhapus
    get_resp = client.get(f"/api/buku/{buku_id}")
    assert get_resp.status_code == 404
```

**Jalankan integration tests:**

```bash
pytest tests/test_api.py -v
```

**Expected output:**

```
tests/test_api.py::test_get_buku_empty PASSED
tests/test_api.py::test_get_buku_not_found PASSED
tests/test_api.py::test_create_buku_berhasil PASSED
tests/test_api.py::test_create_buku_tanpa_judul PASSED
tests/test_api.py::test_create_then_get PASSED
tests/test_api.py::test_update_buku PASSED
tests/test_api.py::test_delete_buku PASSED

=================== 7 passed in 0.12s ===================
```

> **Troubleshooting:** Jika muncul error `create_app('testing')`, pastikan `app/__init__.py` memiliki factory function yang menerima parameter config. Alternatif: gunakan `app.config.from_mapping(TESTING=True)`.

**Estimasi waktu:** 20 menit

---

### Langkah 6: Coverage Analysis (15 menit)

**Mengapa:** Code coverage menunjukkan persentase kode yang dieksekusi oleh test. Coverage 70%+ adalah target minimum — tetapi ingat, 100% coverage tidak menjamin bebas bug. Yang penting adalah *kualitas* test, bukan hanya kuantitas.

```bash
# Jalankan semua test dengan coverage
pytest tests/ --cov=app --cov-report=term-missing -v
```

**Expected output:**

```
---------- coverage: platform linux, python 3.11 ----------
Name                          Stmts   Miss  Cover   Missing
-------------------------------------------------------------
app/__init__.py                  15      2    87%   22-23
app/models.py                    30      5    83%   45-49
app/services/buku_service.py     28      3    89%   31-33
app/services/denda.py            12      0   100%
-------------------------------------------------------------
TOTAL                            85     10    88%
```

**Membaca Coverage Report:**

| Kolom | Penjelasan |
|-------|-----------|
| `Stmts` | Jumlah statement (baris kode yang bisa dieksekusi) |
| `Miss` | Jumlah statement yang TIDAK dieksekusi oleh test |
| `Cover` | Persentase coverage = (Stmts - Miss) / Stmts |
| `Missing` | Nomor baris yang belum tercakup test |

**Generate HTML report untuk analisis visual:**

```bash
pytest tests/ --cov=app --cov-report=html
# Buka htmlcov/index.html di browser
```

> **Tips:** Baris yang ditandai merah di HTML report adalah kandidat utama untuk test baru. Prioritaskan baris di business logic (services) dibanding boilerplate (config).

> **Troubleshooting:** Jika coverage sangat rendah (<50%), kemungkinan besar import path salah. Pastikan `--cov=app` sesuai dengan nama package Python Anda.

**Estimasi waktu:** 15 menit

## Tantangan Tambahan

### Tantangan 1: Basic — Tambah Edge Case Tests

Tambahkan minimal 5 test tambahan untuk edge cases yang belum tercakup:
- Apa yang terjadi jika `stok` bernilai 0?
- Apa yang terjadi jika `judul` berisi karakter spesial (emoji, HTML tag)?
- Apa yang terjadi jika `tarif_per_hari` bernilai 0?

### Tantangan 2: Intermediate — Mock External Service

Implementasikan dan test fitur `cek_ketersediaan_antar_kampus()` yang memanggil API perpustakaan kampus lain. Gunakan `unittest.mock.patch` agar test tidak bergantung pada API eksternal. Target: 3 test (berhasil, API down, buku tidak ditemukan).

### Tantangan 3: Advanced — Capai 90% Coverage

Analisis coverage report, identifikasi semua baris yang belum tercakup (`Missing`), dan tulis test untuk mencapai coverage >= 90%. Dokumentasikan baris mana saja yang *sengaja* tidak ditest dan alasannya (misalnya error handling untuk kasus yang sangat jarang terjadi).

## Refleksi & AI Usage Log

Setelah menyelesaikan lab ini, isi AI Usage Log jika Anda menggunakan AI tools:

| No | Task | Tool | Prompt (ringkas) | Output | Modifikasi yang Dilakukan |
|----|------|------|------------------|--------|--------------------------|
| 1 | ... | ... | ... | ... | ... |

**Pertanyaan refleksi:**
1. Apa perbedaan utama yang Anda rasakan antara menulis unit test vs integration test?
2. Apakah TDD (test-first) terasa lebih sulit atau lebih mudah dibanding test-after? Mengapa?
3. Apa insight dari coverage report — area mana yang paling sulit di-test?

## Checklist Penyelesaian

- [ ] Shared fixtures di `conftest.py` berfungsi
- [ ] 10+ unit tests berjalan pass (termasuk parametrize)
- [ ] Mocking didemonstrasikan minimal 1 skenario
- [ ] TDD: bukti 3 commit (RED → GREEN → REFACTOR)
- [ ] 5+ integration tests untuk API endpoints
- [ ] Coverage report dihasilkan dan dipahami (target >= 70%)
- [ ] Refleksi dan AI Usage Log diisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
