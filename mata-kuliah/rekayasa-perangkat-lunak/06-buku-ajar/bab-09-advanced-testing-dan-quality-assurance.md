# BAB 9: ADVANCED TESTING DAN QUALITY ASSURANCE

**Oleh: Tri Aji Nugroho, S.T., M.T.**
**Mata Kuliah:** IF2205 Rekayasa Perangkat Lunak
**Program Studi Informatika — Universitas Al Azhar Indonesia**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom | Estimasi Waktu |
|-----------|-----------|-------------|----------------|
| 5.3 | Menerapkan Test-Driven Development (TDD) dan AI-assisted testing | C4 (Menganalisis) | 75 menit |
| 5.4 | Mengevaluasi kualitas perangkat lunak menggunakan metrics (code coverage, cyclomatic complexity) | C5 (Mengevaluasi) | 75 menit |

---

## Peta Konsep Bab 9

```
                    ┌───────────────────────────────┐
                    │  ADVANCED TESTING &            │
                    │  QUALITY ASSURANCE             │
                    └──────────┬────────────────────┘
                               │
       ┌───────────────────────┼───────────────────────┐
       │                       │                        │
 ┌─────▼──────┐       ┌───────▼───────┐       ┌───────▼───────┐
 │ TDD         │       │ Advanced      │       │ Quality       │
 │ Red-Green-  │       │ Testing       │       │ Assurance     │
 │ Refactor    │       │ Techniques    │       │ & Metrics     │
 └─────┬──────┘       └───────┬───────┘       └───────┬───────┘
       │                       │                        │
 ┌─────▼──────┐       ┌───────▼───────┐       ┌───────▼───────┐
 │ E2E Testing │       │ Security &    │       │ Code Coverage │
 │ Playwright  │       │ Performance   │       │ Cyclomatic    │
 │             │       │ Testing       │       │ Complexity    │
 └─────┬──────┘       └───────┬───────┘       └───────┬───────┘
       │                       │                        │
       └───────────────────────┼───────────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │ AI-Assisted Testing │
                    │ & Quality Gates     │
                    └─────────────────────┘
```

---

## 9.1 Test-Driven Development (TDD)

### 9.1.1 Filosofi TDD

> *"TDD is not a testing technique. It is a development technique."* — Kent Beck

TDD (*Test-Driven Development*) adalah teknik pengembangan di mana **test ditulis SEBELUM kode implementasi**. Ini bukan sekadar "menulis test" — ini mengubah cara berpikir developer tentang desain kode.

### 9.1.2 Siklus Red-Green-Refactor

```
        ┌─────────────────────────────────────────────────────┐
        │                                                     │
        │    ┌─── RED ──────────────────────┐                │
        │    │ 1. Tulis test yang GAGAL      │                │
        │    │    (belum ada implementasi)    │                │
        │    └──────────┬───────────────────┘                │
        │               │                                     │
        │    ┌──────────▼───────────────────┐                │
        │    │ GREEN                         │                │
        │    │ 2. Tulis kode MINIMAL agar    │                │
        │    │    test PASS (no more, no less)│                │
        │    └──────────┬───────────────────┘                │
        │               │                                     │
        │    ┌──────────▼───────────────────┐                │
        │    │ REFACTOR                      │                │
        │    │ 3. Perbaiki kode tanpa        │                │
        │    │    mengubah perilaku (DRY,     │                │
        │    │    clean code)                 │                │
        │    └──────────┬───────────────────┘                │
        │               │                                     │
        │               └─── Ulangi untuk fitur berikutnya ──┘
        │
        │   ATURAN EMAS:
        │   - Jangan tulis kode produksi tanpa test yang gagal
        │   - Jangan tulis lebih dari satu test yang gagal sekaligus
        │   - Jangan tulis lebih dari kode minimal untuk membuat test pass
        │
        └─────────────────────────────────────────────────────┘
```

### 9.1.3 TDD Walkthrough Lengkap — Sistem Dompet Digital

Mari kita bangun fitur **Dompet Digital** (seperti GoPay/OVO/Dana) menggunakan TDD murni. Setiap langkah mengikuti siklus Red-Green-Refactor.

**Iterasi 1: Cek Saldo Awal**

```python
# tests/test_dompet.py — RED: Tulis test yang GAGAL

def test_dompet_baru_saldo_nol():
    """Dompet baru harus memiliki saldo Rp 0."""
    dompet = Dompet(pemilik="Ahmad")
    assert dompet.saldo == 0
```

```bash
# Jalankan test → GAGAL (NameError: name 'Dompet' is not defined)
$ pytest tests/test_dompet.py -v
FAILED tests/test_dompet.py::test_dompet_baru_saldo_nol - NameError
```

```python
# app/dompet.py — GREEN: Implementasi MINIMAL

class Dompet:
    def __init__(self, pemilik: str):
        self.pemilik = pemilik
        self.saldo = 0
```

```bash
# Jalankan test → PASS!
$ pytest tests/test_dompet.py -v
PASSED tests/test_dompet.py::test_dompet_baru_saldo_nol
```

**Iterasi 2: Top Up Saldo**

```python
# RED: Test top up
def test_top_up_menambah_saldo():
    dompet = Dompet(pemilik="Ahmad")
    dompet.top_up(100_000)
    assert dompet.saldo == 100_000

def test_top_up_negatif_ditolak():
    dompet = Dompet(pemilik="Ahmad")
    with pytest.raises(ValueError, match="tidak boleh negatif"):
        dompet.top_up(-50_000)

def test_top_up_nol_ditolak():
    dompet = Dompet(pemilik="Ahmad")
    with pytest.raises(ValueError, match="harus lebih dari 0"):
        dompet.top_up(0)
```

```python
# GREEN: Implementasi minimal
class Dompet:
    def __init__(self, pemilik: str):
        self.pemilik = pemilik
        self.saldo = 0

    def top_up(self, jumlah: int):
        if jumlah < 0:
            raise ValueError("Jumlah top up tidak boleh negatif")
        if jumlah == 0:
            raise ValueError("Jumlah top up harus lebih dari 0")
        self.saldo += jumlah
```

**Iterasi 3: Transfer ke Dompet Lain**

```python
# RED: Test transfer
def test_transfer_berhasil():
    pengirim = Dompet(pemilik="Ahmad")
    penerima = Dompet(pemilik="Budi")
    pengirim.top_up(500_000)

    pengirim.transfer(penerima, 200_000)

    assert pengirim.saldo == 300_000
    assert penerima.saldo == 200_000

def test_transfer_saldo_tidak_cukup():
    pengirim = Dompet(pemilik="Ahmad")
    penerima = Dompet(pemilik="Budi")
    pengirim.top_up(50_000)

    with pytest.raises(ValueError, match="Saldo tidak cukup"):
        pengirim.transfer(penerima, 100_000)

def test_transfer_ke_diri_sendiri_ditolak():
    dompet = Dompet(pemilik="Ahmad")
    dompet.top_up(100_000)

    with pytest.raises(ValueError, match="tidak bisa transfer ke diri sendiri"):
        dompet.transfer(dompet, 50_000)

def test_transfer_minimum_10000():
    pengirim = Dompet(pemilik="Ahmad")
    penerima = Dompet(pemilik="Budi")
    pengirim.top_up(100_000)

    with pytest.raises(ValueError, match="Minimum transfer"):
        pengirim.transfer(penerima, 5_000)
```

```python
# GREEN: Implementasi transfer
class Dompet:
    def __init__(self, pemilik: str):
        self.pemilik = pemilik
        self.saldo = 0

    def top_up(self, jumlah: int):
        if jumlah < 0:
            raise ValueError("Jumlah top up tidak boleh negatif")
        if jumlah == 0:
            raise ValueError("Jumlah top up harus lebih dari 0")
        self.saldo += jumlah

    def transfer(self, penerima: 'Dompet', jumlah: int):
        if penerima is self:
            raise ValueError("Tidak bisa transfer ke diri sendiri")
        if jumlah < 10_000:
            raise ValueError("Minimum transfer Rp 10.000")
        if jumlah > self.saldo:
            raise ValueError("Saldo tidak cukup")
        self.saldo -= jumlah
        penerima.saldo += jumlah
```

**Iterasi 4: Riwayat Transaksi**

```python
# RED: Test riwayat
def test_riwayat_transaksi_tercatat():
    dompet = Dompet(pemilik="Ahmad")
    dompet.top_up(500_000)

    assert len(dompet.riwayat) == 1
    assert dompet.riwayat[0]["tipe"] == "TOP_UP"
    assert dompet.riwayat[0]["jumlah"] == 500_000

def test_riwayat_transfer_tercatat():
    pengirim = Dompet(pemilik="Ahmad")
    penerima = Dompet(pemilik="Budi")
    pengirim.top_up(500_000)

    pengirim.transfer(penerima, 200_000)

    assert len(pengirim.riwayat) == 2  # top_up + transfer
    assert pengirim.riwayat[1]["tipe"] == "TRANSFER_KELUAR"
    assert penerima.riwayat[0]["tipe"] == "TRANSFER_MASUK"
```

```python
# GREEN + REFACTOR: Implementasi lengkap dengan riwayat
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict


class Dompet:
    """Dompet digital sederhana (seperti GoPay/OVO/Dana)."""

    MINIMUM_TRANSFER = 10_000

    def __init__(self, pemilik: str):
        self.pemilik = pemilik
        self.saldo = 0
        self.riwayat: List[Dict] = []

    def _catat(self, tipe: str, jumlah: int, keterangan: str = ""):
        self.riwayat.append({
            "tipe": tipe,
            "jumlah": jumlah,
            "saldo_setelah": self.saldo,
            "keterangan": keterangan,
            "waktu": datetime.now().isoformat(),
        })

    def top_up(self, jumlah: int):
        """Top up saldo dompet."""
        if jumlah < 0:
            raise ValueError("Jumlah top up tidak boleh negatif")
        if jumlah == 0:
            raise ValueError("Jumlah top up harus lebih dari 0")
        self.saldo += jumlah
        self._catat("TOP_UP", jumlah)

    def transfer(self, penerima: 'Dompet', jumlah: int):
        """Transfer saldo ke dompet lain."""
        if penerima is self:
            raise ValueError("Tidak bisa transfer ke diri sendiri")
        if jumlah < self.MINIMUM_TRANSFER:
            raise ValueError(f"Minimum transfer Rp {self.MINIMUM_TRANSFER:,}")
        if jumlah > self.saldo:
            raise ValueError("Saldo tidak cukup")

        self.saldo -= jumlah
        penerima.saldo += jumlah
        self._catat("TRANSFER_KELUAR", jumlah, f"Ke {penerima.pemilik}")
        penerima._catat("TRANSFER_MASUK", jumlah, f"Dari {self.pemilik}")
```

```bash
# Jalankan semua test → ALL PASS
$ pytest tests/test_dompet.py -v
tests/test_dompet.py::test_dompet_baru_saldo_nol          PASSED
tests/test_dompet.py::test_top_up_menambah_saldo           PASSED
tests/test_dompet.py::test_top_up_negatif_ditolak          PASSED
tests/test_dompet.py::test_top_up_nol_ditolak              PASSED
tests/test_dompet.py::test_transfer_berhasil               PASSED
tests/test_dompet.py::test_transfer_saldo_tidak_cukup      PASSED
tests/test_dompet.py::test_transfer_ke_diri_sendiri_ditolak PASSED
tests/test_dompet.py::test_transfer_minimum_10000          PASSED
tests/test_dompet.py::test_riwayat_transaksi_tercatat      PASSED
tests/test_dompet.py::test_riwayat_transfer_tercatat       PASSED

========================= 10 passed in 0.05s =========================
```

### 9.1.4 Manfaat dan Keterbatasan TDD

| Manfaat | Penjelasan |
|---------|------------|
| **Desain lebih baik** | Memaksa berpikir tentang interface sebelum implementasi |
| **Regression safety** | Setiap fitur baru sudah memiliki test |
| **Dokumentasi hidup** | Test = dokumentasi yang selalu up-to-date |
| **Confidence to refactor** | Bisa refactor tanpa takut merusak sesuatu |
| **Fewer bugs** | Studi menunjukkan 40-80% lebih sedikit bug (Microsoft, IBM) |

| Keterbatasan | Penjelasan |
|-------------|------------|
| **Learning curve** | Butuh waktu untuk terbiasa menulis test dulu |
| **Slower initially** | Awalnya terasa lebih lambat (tapi cepat di long term) |
| **Not for all scenarios** | Sulit untuk UI, exploratory coding, prototyping |
| **Overhead for simple code** | Overkill untuk getter/setter sederhana |

---

## 9.2 End-to-End (E2E) Testing dengan Playwright

### 9.2.1 Apa Itu E2E Testing?

E2E testing menguji alur lengkap aplikasi dari perspektif pengguna akhir — seperti seseorang yang benar-benar menggunakan aplikasi melalui browser.

```
  E2E Test Simulation:
  ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
  │ Browser │────►│ Frontend│────►│ Backend │────►│ Database│
  │ (User)  │     │ (HTML/  │     │ (Flask/ │     │ (SQL/   │
  │         │◄────│  JS)    │◄────│  Express)│◄────│  NoSQL) │
  └─────────┘     └─────────┘     └─────────┘     └─────────┘
       ▲
       │
  Playwright mengontrol browser secara otomatis,
  meniru interaksi pengguna nyata
```

### 9.2.2 Setup Playwright untuk Python

```bash
# Instalasi di GitHub Codespaces
pip install playwright pytest-playwright
playwright install chromium
```

### 9.2.3 E2E Test: Alur Login dan Dashboard

```python
# tests/e2e/test_login.py
"""E2E tests untuk alur login Sistem Perpustakaan UAI."""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:5000"


def test_login_berhasil(page: Page, base_url):
    """Test: mahasiswa berhasil login dan melihat dashboard."""
    # Arrange: navigasi ke halaman login
    page.goto(f"{base_url}/login")

    # Act: isi form dan submit
    page.fill("#username", "mahasiswa01")
    page.fill("#password", "password123")
    page.click("#btn-login")

    # Assert: redirect ke dashboard
    expect(page).to_have_url(f"{base_url}/dashboard")
    expect(page.locator("h1")).to_have_text("Dashboard")
    expect(page.locator(".welcome-message")).to_contain_text("mahasiswa01")


def test_login_gagal_password_salah(page: Page, base_url):
    """Test: login dengan password salah menampilkan error."""
    page.goto(f"{base_url}/login")
    page.fill("#username", "mahasiswa01")
    page.fill("#password", "wrongpassword")
    page.click("#btn-login")

    # Harus tetap di halaman login
    expect(page).to_have_url(f"{base_url}/login")
    expect(page.locator(".error-message")).to_contain_text(
        "Username atau password salah"
    )


def test_login_form_validasi_kosong(page: Page, base_url):
    """Test: submit form kosong menampilkan validasi."""
    page.goto(f"{base_url}/login")
    page.click("#btn-login")

    # Browser HTML5 validation atau custom validation
    expect(page.locator("#username")).to_have_attribute("required", "")
```

### 9.2.4 E2E Test: Alur Peminjaman Buku Lengkap

```python
# tests/e2e/test_peminjaman.py
"""E2E tests untuk alur peminjaman buku end-to-end."""
from playwright.sync_api import Page, expect


def test_alur_peminjaman_buku_lengkap(page: Page, base_url):
    """
    Test alur lengkap:
    1. Login
    2. Cari buku
    3. Pinjam buku
    4. Verifikasi di halaman peminjaman saya
    """
    # Step 1: Login
    page.goto(f"{base_url}/login")
    page.fill("#username", "mahasiswa01")
    page.fill("#password", "password123")
    page.click("#btn-login")
    expect(page).to_have_url(f"{base_url}/dashboard")

    # Step 2: Cari buku
    page.fill("#search-buku", "Algoritma")
    page.click("#btn-search")

    # Verifikasi hasil pencarian muncul
    expect(page.locator(".search-results .buku-item")).to_have_count(1)
    expect(page.locator(".buku-item .judul")).to_contain_text("Algoritma")

    # Step 3: Klik pinjam
    page.click(".buku-item .btn-pinjam")

    # Verifikasi dialog konfirmasi
    expect(page.locator(".modal-confirm")).to_be_visible()
    page.click(".modal-confirm .btn-ya")

    # Verifikasi pesan sukses
    expect(page.locator(".toast-success")).to_contain_text(
        "Peminjaman berhasil"
    )

    # Step 4: Cek di halaman peminjaman saya
    page.click("a[href='/peminjaman-saya']")
    expect(page.locator(".peminjaman-list .item")).to_have_count(1)
    expect(page.locator(".peminjaman-list .item .judul")).to_contain_text(
        "Algoritma"
    )


def test_peminjaman_buku_stok_habis(page: Page, base_url):
    """Test: tidak bisa meminjam buku yang stoknya habis."""
    page.goto(f"{base_url}/login")
    page.fill("#username", "mahasiswa01")
    page.fill("#password", "password123")
    page.click("#btn-login")

    page.goto(f"{base_url}/buku/999")  # Buku stok habis

    # Tombol pinjam harus disabled
    expect(page.locator("#btn-pinjam")).to_be_disabled()
    expect(page.locator(".stok-info")).to_contain_text("Stok: 0")
```

### 9.2.5 Kapan Menggunakan E2E Test?

| Gunakan E2E Test Untuk | Jangan Gunakan E2E Test Untuk |
|------------------------|-------------------------------|
| Critical user journeys (login, checkout, pembayaran) | Validasi logika bisnis sederhana |
| Smoke testing setelah deployment | Testing semua edge cases |
| Cross-browser compatibility | Unit-level testing |
| Verifikasi integrasi frontend-backend | Performa (gunakan load testing tools) |

---

## 9.3 Performance Testing

### 9.3.1 Jenis-Jenis Performance Testing

| Tipe | Tujuan | Contoh Skenario |
|------|--------|-----------------|
| **Load Testing** | Test dengan beban normal/expected | 1000 user simultan di Tokopedia saat normal |
| **Stress Testing** | Test di atas kapasitas maximum | 100.000 user simultan di saat flash sale |
| **Spike Testing** | Lonjakan beban tiba-tiba | Jam 12 malam saat promo 12.12 |
| **Endurance Testing** | Beban konstan untuk waktu lama | Server berjalan 72 jam tanpa restart |
| **Scalability Testing** | Test apakah sistem bisa di-scale | Tambah server, apakah throughput naik linear? |

### 9.3.2 Load Testing dengan Locust (Python)

```python
# locustfile.py — Load testing untuk API Perpustakaan
from locust import HttpUser, task, between


class MahasiswaUser(HttpUser):
    """Simulasi perilaku mahasiswa menggunakan sistem perpustakaan."""
    wait_time = between(1, 5)  # Jeda 1-5 detik antar request

    def on_start(self):
        """Login saat user mulai (setup)."""
        self.client.post("/api/auth/login", json={
            "username": "mahasiswa01",
            "password": "password123"
        })

    @task(5)  # Bobot 5: paling sering dilakukan
    def cari_buku(self):
        """Mahasiswa sering mencari buku."""
        self.client.get("/api/buku?q=algoritma")

    @task(3)  # Bobot 3: cukup sering
    def lihat_detail_buku(self):
        """Melihat detail buku tertentu."""
        self.client.get("/api/buku/1")

    @task(1)  # Bobot 1: jarang (perlu auth)
    def pinjam_buku(self):
        """Meminjam buku (jarang dilakukan)."""
        self.client.post("/api/peminjaman", json={
            "buku_id": 1
        })

    @task(2)
    def lihat_peminjaman(self):
        """Cek status peminjaman."""
        self.client.get("/api/peminjaman/saya")
```

```bash
# Jalankan Locust
locust -f locustfile.py --host=http://localhost:5000

# Buka http://localhost:8089 untuk UI
# Set: Number of users: 100, Spawn rate: 10/s

# Atau mode headless (untuk CI/CD):
locust -f locustfile.py --host=http://localhost:5000 \
  --users 100 --spawn-rate 10 --run-time 60s --headless
```

### 9.3.3 Metrik Performance yang Penting

```
  Response Time Distribution (example):
  ┌──────────────────────────────────────────────────┐
  │ < 200ms  ████████████████████████████████  80%   │  Target
  │ 200-500ms████████████████                  15%   │  Acceptable
  │ 500ms-1s ████                               4%   │  Warning
  │ > 1s     █                                  1%   │  Critical
  └──────────────────────────────────────────────────┘

  Key Metrics:
  ┌───────────────────┬──────────────┬─────────────────────┐
  │ Metrik            │ Target       │ Keterangan           │
  ├───────────────────┼──────────────┼─────────────────────┤
  │ Avg Response Time │ < 200ms      │ Rata-rata semua req  │
  │ P95 Response Time │ < 500ms      │ 95% req di bawah ini │
  │ P99 Response Time │ < 1s         │ 99% req di bawah ini │
  │ Throughput        │ > 100 req/s  │ Request per detik    │
  │ Error Rate        │ < 1%         │ % request yang gagal │
  │ Concurrent Users  │ > 500        │ User simultan        │
  └───────────────────┴──────────────┴─────────────────────┘
```

---

## 9.4 Security Testing

### 9.4.1 OWASP Top 10 (2021) — Overview

OWASP (*Open Web Application Security Project*) Top 10 adalah daftar 10 risiko keamanan web application yang paling kritis:

| # | Risiko | Deskripsi | Contoh Indonesia |
|---|--------|-----------|------------------|
| A01 | **Broken Access Control** | User bisa akses data/fitur orang lain | Nasabah BCA bisa lihat saldo nasabah lain |
| A02 | **Cryptographic Failures** | Data sensitif tidak dienkripsi | Password disimpan plaintext di database bank |
| A03 | **Injection** | SQL/NoSQL/OS command injection | Input di form login bisa drop database |
| A04 | **Insecure Design** | Desain yang secara fundamental tidak aman | Fitur "forgot password" tanpa rate limiting |
| A05 | **Security Misconfiguration** | Default config, stack traces di production | Flask debug=True di production |
| A06 | **Vulnerable Components** | Dependency dengan known vulnerabilities | Library Python/npm yang sudah EOL |
| A07 | **Auth Failures** | Autentikasi/session management lemah | Session tidak expire setelah logout |
| A08 | **Software & Data Integrity** | CI/CD pipeline tanpa integrity check | Package npm di-hijack (supply chain attack) |
| A09 | **Logging Failures** | Tidak cukup logging untuk deteksi serangan | Gagal login 1000x tanpa alert |
| A10 | **SSRF** | Server-Side Request Forgery | Attacker bisa akses internal API via server |

### 9.4.2 Contoh SQL Injection dan Pencegahannya

```python
# ================================
# RENTAN — SQL INJECTION
# ================================
@app.route('/api/buku/search')
def search_buku_rentan():
    keyword = request.args.get('q', '')
    # JANGAN LAKUKAN INI!
    query = f"SELECT * FROM buku WHERE judul LIKE '%{keyword}%'"
    result = db.engine.execute(query)
    return jsonify([dict(row) for row in result])

# Attacker bisa input: q='; DROP TABLE buku; --
# Query menjadi: SELECT * FROM buku WHERE judul LIKE '%'; DROP TABLE buku; --%'
# → Database buku TERHAPUS!

# ================================
# AMAN — Parameterized Query
# ================================
@app.route('/api/buku/search')
def search_buku_aman():
    keyword = request.args.get('q', '')
    # SQLAlchemy ORM — otomatis parameterized
    buku = Buku.query.filter(Buku.judul.contains(keyword)).all()
    return jsonify([b.to_dict() for b in buku])
```

### 9.4.3 Security Test Cases

```python
# tests/security/test_injection.py
"""Security tests untuk mencegah injection attacks."""
import pytest


class TestSQLInjection:
    """Test SQL injection pada API search."""

    @pytest.mark.parametrize("payload", [
        "'; DROP TABLE buku; --",
        "' OR '1'='1",
        "' UNION SELECT * FROM users --",
        "1; DELETE FROM buku WHERE 1=1",
        "' AND 1=(SELECT COUNT(*) FROM users) --",
    ])
    def test_search_menolak_sql_injection(self, client, payload):
        """API harus aman terhadap SQL injection payloads."""
        response = client.get(f'/api/buku/search?q={payload}')
        # Seharusnya tetap mengembalikan response normal (kosong)
        assert response.status_code == 200
        # Pastikan tidak ada error database
        assert "error" not in response.json


class TestXSS:
    """Test Cross-Site Scripting (XSS)."""

    @pytest.mark.parametrize("payload", [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "javascript:alert('XSS')",
        "' onmouseover='alert(1)'",
    ])
    def test_input_html_di_escape(self, client, payload):
        """Input HTML/JS harus di-escape, bukan dirender."""
        response = client.post('/api/buku', json={
            'judul': payload,
            'penulis': 'Test Author'
        })
        # Jika berhasil tersimpan, cek output ter-escape
        if response.status_code == 201:
            buku = client.get(f'/api/buku/{response.json["id"]}')
            assert "<script>" not in buku.json["judul"]


class TestBrokenAccessControl:
    """Test akses kontrol — user hanya bisa akses data sendiri."""

    def test_user_tidak_bisa_akses_peminjaman_orang_lain(self, client):
        """Mahasiswa A tidak bisa melihat peminjaman Mahasiswa B."""
        # Login sebagai mahasiswa A
        client.post('/api/auth/login', json={
            'username': 'mahasiswa_a', 'password': 'pass_a'
        })
        # Coba akses peminjaman mahasiswa B (ID: 999)
        response = client.get('/api/peminjaman/user/999')
        assert response.status_code == 403  # Forbidden
```

### 9.4.4 Konteks Indonesia: Regulasi OJK untuk Fintech

```
Regulasi OJK (Otoritas Jasa Keuangan) untuk Fintech/Banking:

┌─────────────────────────────────────────────────────────────────┐
│ POJK No. 4/POJK.05/2021 — Penyelenggara IKD                   │
│                                                                 │
│ Kewajiban Security Testing:                                     │
│ 1. Penetration testing minimal 1x per tahun                    │
│ 2. Vulnerability assessment setiap 6 bulan                     │
│ 3. Data nasabah wajib dienkripsi (at rest dan in transit)      │
│ 4. Two-factor authentication untuk transaksi                   │
│ 5. Logging dan audit trail minimal 5 tahun                     │
│ 6. Disaster recovery plan dan testing                          │
│                                                                 │
│ Sanksi: Pencabutan izin operasional, denda hingga              │
│ Rp 15 miliar per pelanggaran                                   │
└─────────────────────────────────────────────────────────────────┘

Implikasi untuk Developer:
- Security testing BUKAN opsional di industri keuangan Indonesia
- Setiap release harus melalui security review
- Compliance testing harus masuk dalam CI/CD pipeline
```

---

## 9.5 Mutation Testing

### 9.5.1 Apa Itu Mutation Testing?

Mutation testing mengevaluasi **kualitas test suite** Anda — bukan kualitas kode produksi. Caranya: secara otomatis membuat perubahan kecil (*mutants*) pada kode dan memeriksa apakah test mendeteksi perubahan tersebut.

```
  Proses Mutation Testing:
  ┌────────────────┐     ┌────────────────┐     ┌────────────────┐
  │ Kode Asli      │     │ Mutant #1      │     │ Mutant #2      │
  │ if x > 10:     │────►│ if x >= 10:    │     │ if x < 10:     │
  │   return True  │     │   return True  │     │   return True  │
  └────────┬───────┘     └────────┬───────┘     └────────┬───────┘
           │                      │                       │
    ┌──────▼──────┐       ┌──────▼──────┐        ┌──────▼──────┐
    │ Run Tests   │       │ Run Tests   │        │ Run Tests   │
    │ ✓ All pass  │       │ ✓ All pass  │        │ ✗ Test fail │
    └─────────────┘       └─────────────┘        └─────────────┘
                                │                         │
                          SURVIVED!                  KILLED!
                          (Test lemah)               (Test kuat)

  Mutation Score = Killed Mutants / Total Mutants × 100%
  Target: ≥ 80%
```

### 9.5.2 Jenis-Jenis Mutasi

| Tipe Mutasi | Kode Asli | Mutant | Operator |
|-------------|-----------|--------|----------|
| Relational | `x > 10` | `x >= 10` | ROR (Relational Operator Replacement) |
| Arithmetic | `a + b` | `a - b` | AOR (Arithmetic Operator Replacement) |
| Logical | `a and b` | `a or b` | LOR (Logical Operator Replacement) |
| Negation | `if valid:` | `if not valid:` | Negate Conditionals |
| Return | `return True` | `return False` | Return Value Mutation |
| Remove | `self.save()` | *(dihapus)* | Statement Deletion |

### 9.5.3 Mutation Testing dengan mutmut (Python)

```bash
# Instalasi
pip install mutmut

# Jalankan mutation testing
mutmut run --paths-to-mutate=app/ --tests-dir=tests/

# Lihat hasil
mutmut results

# Output contoh:
# Survived mutants:  12
# Killed mutants:    88
# Mutation score:    88.0%  (target: ≥80%)

# Lihat mutant yang survived (test lemah)
mutmut show 15
# app/dompet.py:
# - if jumlah < self.MINIMUM_TRANSFER:
# + if jumlah <= self.MINIMUM_TRANSFER:
# → Test tidak menangkap perubahan ini!
#   Artinya: test boundary untuk MINIMUM_TRANSFER kurang
```

---

## 9.6 AI-Assisted Testing

### 9.6.1 AI untuk Test Generation

AI (seperti Claude, Copilot, ChatGPT) bisa membantu generate test cases, tetapi HARUS dievaluasi oleh manusia.

```
PROMPT untuk AI Test Generation:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Buatkan pytest test cases yang komprehensif untuk fungsi berikut.
Gunakan @pytest.mark.parametrize untuk boundary values.
Sertakan test untuk:
1. Happy path (normal usage)
2. Edge cases (boundary values)
3. Error handling (invalid inputs)
4. Business rules

Fungsi:
def hitung_denda_peminjaman(hari_terlambat, tarif_per_hari=2000,
                             max_denda=100000):
    if hari_terlambat < 0:
        raise ValueError('Hari terlambat tidak boleh negatif')
    if tarif_per_hari <= 0:
        raise ValueError('Tarif harus positif')
    denda = hari_terlambat * tarif_per_hari
    return min(denda, max_denda)"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Contoh output AI yang PERLU dievaluasi:**

```python
# AI-generated tests — perlu review manusia
import pytest

@pytest.mark.parametrize("hari, tarif, max_d, expected", [
    (0,   2000, 100000, 0),       # Tidak terlambat
    (1,   2000, 100000, 2000),    # 1 hari terlambat
    (50,  2000, 100000, 100000),  # Tepat di max denda
    (51,  2000, 100000, 100000),  # Melebihi max denda (capped)
    (10,  5000, 100000, 50000),   # Tarif berbeda
    (100, 2000, 100000, 100000),  # Jauh di atas max
])
def test_hitung_denda_valid(hari, tarif, max_d, expected):
    assert hitung_denda_peminjaman(hari, tarif, max_d) == expected

def test_hitung_denda_hari_negatif():
    with pytest.raises(ValueError, match="negatif"):
        hitung_denda_peminjaman(-1)

def test_hitung_denda_tarif_nol():
    with pytest.raises(ValueError, match="positif"):
        hitung_denda_peminjaman(5, tarif_per_hari=0)

# REVIEW MANUSIA — AI sering MISS:
# 1. ✗ Boundary: hari_terlambat yang menghasilkan denda = max_denda - 1
# 2. ✗ Tipe data: apa yang terjadi jika hari_terlambat = 1.5 (float)?
# 3. ✗ Bisnis: apakah ada hari libur yang tidak dihitung?
# 4. ✗ Concurrency: dua orang bayar denda bersamaan?
```

### 9.6.2 AI untuk Property-Based Testing

```
PROMPT:
"Buatkan property-based tests menggunakan Hypothesis library
untuk fungsi hitung_denda_peminjaman. Definisikan properties:
1. Denda selalu non-negatif
2. Denda selalu <= max_denda
3. Denda monoton meningkat seiring hari_terlambat
4. Denda = 0 jika hari_terlambat = 0"
```

```python
# Property-based testing dengan Hypothesis
from hypothesis import given, strategies as st

@given(
    hari=st.integers(min_value=0, max_value=1000),
    tarif=st.integers(min_value=1, max_value=10000),
    max_denda=st.integers(min_value=1, max_value=1000000),
)
def test_denda_selalu_non_negatif(hari, tarif, max_denda):
    """Property: denda tidak pernah negatif."""
    result = hitung_denda_peminjaman(hari, tarif, max_denda)
    assert result >= 0

@given(
    hari=st.integers(min_value=0, max_value=1000),
    tarif=st.integers(min_value=1, max_value=10000),
    max_denda=st.integers(min_value=1, max_value=1000000),
)
def test_denda_tidak_melebihi_max(hari, tarif, max_denda):
    """Property: denda selalu <= max_denda."""
    result = hitung_denda_peminjaman(hari, tarif, max_denda)
    assert result <= max_denda
```

---

## 9.7 Code Coverage Analysis

### 9.7.1 Jenis-Jenis Coverage

| Tipe Coverage | Apa yang Diukur | Contoh |
|---------------|-----------------|--------|
| **Line Coverage** | Berapa baris yang dieksekusi | 85 dari 100 baris = 85% |
| **Branch Coverage** | Berapa cabang if/else yang dieksekusi | 6 dari 8 branches = 75% |
| **Path Coverage** | Berapa jalur eksekusi yang dilewati | Kombinasi semua cabang |
| **Function Coverage** | Berapa fungsi yang dipanggil | 18 dari 20 functions = 90% |
| **Condition Coverage** | Berapa kondisi boolean yang di-evaluasi true/false | `a and b` → test a=T, a=F, b=T, b=F |

### 9.7.2 Contoh Perbedaan Line vs Branch Coverage

```python
def kategori_nasabah(saldo, lama_tahun):
    """Tentukan kategori nasabah bank."""
    kategori = "Regular"                    # Line 1
    if saldo >= 500_000_000:                # Line 2, Branch 1-2
        kategori = "Priority"              # Line 3
    if lama_tahun >= 10:                    # Line 4, Branch 3-4
        kategori = "Loyal " + kategori     # Line 5
    return kategori                         # Line 6

# Test yang mencapai 100% LINE coverage tapi BUKAN 100% branch:
def test_nasabah_kaya_lama():
    result = kategori_nasabah(1_000_000_000, 15)
    assert result == "Loyal Priority"
# → Semua 6 baris ter-eksekusi (100% line coverage)
# → Tapi branch "saldo < 500jt" dan "lama < 10" TIDAK ter-test!
# → Branch coverage hanya 50% (2 dari 4 branches)

# Test tambahan untuk 100% branch coverage:
def test_nasabah_regular():
    result = kategori_nasabah(100_000, 2)
    assert result == "Regular"
# Sekarang semua branches ter-cover!
```

### 9.7.3 Menjalankan Coverage Analysis

```bash
# Python — pytest-cov
pytest --cov=app --cov-report=term-missing --cov-branch tests/

# Output:
# Name                       Stmts   Miss Branch BrPart  Cover   Missing
# ----------------------------------------------------------------------
# app/__init__.py                 5      0      0      0   100%
# app/dompet.py                  35      2      8      1    93%   42, 55
# app/services/buku.py           22      0      6      0   100%
# app/utils/validators.py        18      3      4      2    80%   28-29, 35
# ----------------------------------------------------------------------
# TOTAL                          80      5     18      3    93%

# HTML report (detail per baris):
pytest --cov=app --cov-report=html tests/
# Buka htmlcov/index.html
```

### 9.7.4 Coverage Bukan Segalanya

```
  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  "100% code coverage TIDAK menjamin software bebas bug"    │
  │                                                             │
  │  Contoh: fungsi dengan 100% coverage tapi masih buggy:     │
  │                                                             │
  │  def bagi(a, b):                                           │
  │      return a / b                                          │
  │                                                             │
  │  def test_bagi():                                          │
  │      assert bagi(10, 2) == 5  # 100% line coverage!       │
  │                                                             │
  │  → Tapi: bagi(10, 0) → ZeroDivisionError (tidak di-test!) │
  │  → Dan:  bagi(1, 3) → 0.333... (float precision issue?)   │
  │                                                             │
  │  Coverage mengukur KUANTITAS baris yang dijalankan,        │
  │  bukan KUALITAS assertions dan edge cases.                 │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘

  Rekomendasi Coverage Target:
  ┌─────────────────────────────┬────────────┐
  │ Jenis Sistem                │ Target     │
  ├─────────────────────────────┼────────────┤
  │ Proyek kuliah               │ ≥ 70%      │
  │ Aplikasi web umum           │ ≥ 80%      │
  │ Sistem keuangan/perbankan   │ ≥ 90%      │
  │ Safety-critical (avionics)  │ ≥ 100% MC/DC│
  └─────────────────────────────┴────────────┘
```

---

## 9.8 Cyclomatic Complexity

### 9.8.1 Definisi dan Perhitungan

**Cyclomatic complexity** mengukur jumlah jalur independen (*independent paths*) melalui kode. Semakin tinggi nilainya, semakin kompleks kode dan semakin banyak test yang dibutuhkan.

**Rumus:** `M = E - N + 2P`
- E = jumlah edges (panah) di control flow graph
- N = jumlah nodes (blok kode)
- P = jumlah connected components (biasanya 1)

**Cara praktis:** Hitung jumlah decision points (if, elif, for, while, and, or, except) + 1

```python
# Contoh: Cyclomatic Complexity = 5
def evaluasi_pinjaman(skor_kredit, penghasilan, agunan, riwayat):
    """CC = 5 (4 decision points + 1)"""
    if skor_kredit < 500:                  # Decision 1
        return "DITOLAK"
    if penghasilan < 5_000_000:            # Decision 2
        return "DITOLAK"
    if not agunan:                          # Decision 3
        if riwayat == "buruk":             # Decision 4
            return "DITOLAK"
        return "DISETUJUI_BUNGA_TINGGI"
    return "DISETUJUI"

# Minimum test paths = CC = 5:
# Path 1: skor < 500 → DITOLAK
# Path 2: skor OK, penghasilan < 5jt → DITOLAK
# Path 3: skor OK, penghasilan OK, tanpa agunan, riwayat buruk → DITOLAK
# Path 4: skor OK, penghasilan OK, tanpa agunan, riwayat baik → BUNGA_TINGGI
# Path 5: skor OK, penghasilan OK, ada agunan → DISETUJUI
```

### 9.8.2 Interpretasi Cyclomatic Complexity

```
  ┌──────────────┬───────────────────────────────────────┐
  │ CC Value     │ Interpretasi                          │
  ├──────────────┼───────────────────────────────────────┤
  │ 1-10         │ ✓ Sederhana, mudah ditest            │
  │ 11-20        │ ⚠ Moderate, perlu perhatian          │
  │ 21-50        │ ✗ Kompleks, sulit ditest & maintain  │
  │ > 50         │ ✗ Sangat kompleks, HARUS di-refactor │
  └──────────────┴───────────────────────────────────────┘
```

```bash
# Mengukur CC dengan radon (Python)
pip install radon

radon cc app/ -a -s

# Output:
# app/dompet.py
#     M 15:0 transfer - B (6)
#     M 25:0 top_up - A (3)
#     M 40:0 _catat - A (1)
#
# Average complexity: A (3.33)
# A = sangat baik, F = sangat buruk
```

---

## 9.9 Quality Gates

### 9.9.1 Definisi Quality Gates

Quality gates adalah **checkpoint otomatis** yang harus dilalui kode sebelum berpindah ke fase berikutnya. Jika kode tidak memenuhi standar, proses BERHENTI.

```
  Feature Branch ──► PR Created ──► Quality Gates ──► Merge
                                         │
                         ┌───────────────┼───────────────┐
                         │               │               │
                    ┌────▼────┐    ┌─────▼─────┐   ┌────▼────┐
                    │ Gate 1  │    │ Gate 2    │   │ Gate 3  │
                    │ Auto    │    │ Human     │   │ Final   │
                    │ Tests   │    │ Review    │   │ Check   │
                    └────┬────┘    └─────┬─────┘   └────┬────┘
                         │               │               │
                    Requirements:   Requirements:   Requirements:
                    ✓ Lint pass     ✓ 1+ reviewer   ✓ Integration
                    ✓ Unit tests      approve         tests pass
                      pass         ✓ No unresolved  ✓ No merge
                    ✓ Coverage       comments         conflicts
                      ≥ 80%        ✓ Code quality   ✓ Security
                    ✓ No critical    check            scan clean
                      security
                      issues
```

### 9.9.2 Implementasi Quality Gates di GitHub Actions

```yaml
# .github/workflows/quality-gate.yml
name: Quality Gates

on:
  pull_request:
    branches: [main, develop]

jobs:
  # Gate 1: Code Quality
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install flake8 black isort
      - name: Check formatting (Black)
        run: black --check app/ tests/
      - name: Check imports (isort)
        run: isort --check-only app/ tests/
      - name: Lint (flake8)
        run: flake8 app/ --max-line-length=120 --max-complexity=10

  # Gate 2: Testing
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - name: Run tests with coverage
        run: |
          pytest tests/ --cov=app --cov-branch \
            --cov-fail-under=80 --cov-report=xml
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v4

  # Gate 3: Security
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install safety bandit
      - name: Check dependencies for vulnerabilities
        run: safety check -r requirements.txt
      - name: Security analysis (Bandit)
        run: bandit -r app/ -ll  # Low severity and above

  # Gate 4: Complexity check
  complexity:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install radon
      - name: Check cyclomatic complexity
        run: |
          radon cc app/ -a -nb --total-average
          # Fail if average complexity > B (6)
          radon cc app/ -a -nb --total-average | grep -q "[AB]" || exit 1
```

### 9.9.3 Quality Gate Checklist untuk Proyek Kuliah

```
Quality Gate Checklist — Proyek RPL UAI:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pre-merge (otomatis via GitHub Actions):
  □ flake8 linting pass (PEP 8)
  □ Unit tests pass (pytest)
  □ Code coverage ≥ 70%
  □ No critical security issues (bandit)
  □ Cyclomatic complexity rata-rata ≤ 10

Pre-merge (manual — code review):
  □ Minimal 1 anggota tim approve PR
  □ Semua komentar review resolved
  □ Kode sesuai coding standards tim
  □ Test cases cover business logic

Pre-release:
  □ Integration tests pass
  □ E2E tests pass (critical paths)
  □ Documentation updated
  □ No known critical bugs
```

---

## 9.10 Studi Kasus: Testing Strategy untuk Fintech Indonesia

### Skenario: Aplikasi Pembayaran QRIS

Anda adalah QA Lead untuk startup fintech yang membangun aplikasi pembayaran QRIS (Quick Response Code Indonesian Standard). Aplikasi harus comply dengan regulasi Bank Indonesia dan OJK.

### Testing Strategy Komprehensif:

```
  ┌──────────────────────────────────────────────────────────────┐
  │ LEVEL 1: UNIT TESTING (Target: 90% coverage)                │
  │                                                              │
  │ • Validasi format QRIS (standar Bank Indonesia)             │
  │ • Perhitungan biaya merchant (MDR)                          │
  │ • Enkripsi/dekripsi data transaksi                          │
  │ • Rate limiting logic                                       │
  │ • Input validation (nominal, PIN)                           │
  │                                                              │
  │ Tools: pytest + parametrize + mocking                       │
  └──────────────────────────────────────────────────────────────┘
  ┌──────────────────────────────────────────────────────────────┐
  │ LEVEL 2: INTEGRATION TESTING (Target: 85% critical paths)   │
  │                                                              │
  │ • API endpoint → Database (transaksi tercatat)              │
  │ • Payment gateway integration (BCA, Mandiri, BNI)           │
  │ • Notifikasi service (SMS, push notification)               │
  │ • Settlement batch processing                               │
  │                                                              │
  │ Tools: pytest + TestContainers + mock external APIs          │
  └──────────────────────────────────────────────────────────────┘
  ┌──────────────────────────────────────────────────────────────┐
  │ LEVEL 3: E2E TESTING (Target: semua critical user journeys) │
  │                                                              │
  │ • Scan QR → Konfirmasi → PIN → Pembayaran berhasil         │
  │ • Pembayaran gagal (saldo kurang, timeout, QR expired)      │
  │ • Refund flow                                               │
  │ • Riwayat transaksi                                         │
  │                                                              │
  │ Tools: Playwright (web), Appium (mobile)                    │
  └──────────────────────────────────────────────────────────────┘
  ┌──────────────────────────────────────────────────────────────┐
  │ LEVEL 4: SECURITY TESTING (Wajib untuk fintech)             │
  │                                                              │
  │ • Penetration testing (OWASP Top 10)                        │
  │ • SQL injection, XSS, CSRF                                  │
  │ • API rate limiting dan brute force protection               │
  │ • Data encryption verification (AES-256)                    │
  │ • PIN brute force (max 3 attempts, lock 30 menit)           │
  │                                                              │
  │ Tools: OWASP ZAP, Burp Suite, bandit (Python)              │
  └──────────────────────────────────────────────────────────────┘
  ┌──────────────────────────────────────────────────────────────┐
  │ LEVEL 5: PERFORMANCE TESTING                                 │
  │                                                              │
  │ • Load test: 10.000 transaksi/menit (normal)                │
  │ • Stress test: 100.000 transaksi/menit (promo cashback)     │
  │ • Response time P99 < 3 detik                               │
  │ • Endurance: 72 jam tanpa memory leak                       │
  │                                                              │
  │ Tools: Locust, k6                                           │
  └──────────────────────────────────────────────────────────────┘
```

---

## 9.11 AI Corner: AI untuk Advanced Testing dan QA (Level: Advanced)

### 9.11.1 AI untuk TDD Coaching

```
PROMPT:
"Saya ingin mengembangkan fitur 'refund transaksi' untuk aplikasi
e-commerce menggunakan TDD. Aturan bisnis:
- Refund hanya bisa dalam 7 hari setelah transaksi
- Refund memerlukan alasan (min 20 karakter)
- Dana dikembalikan ke saldo dompet, bukan ke rekening bank
- Maksimum 1 refund per transaksi
- Admin harus approve refund > Rp 1.000.000

Berikan langkah TDD (Red-Green-Refactor) iterasi per iterasi."
```

### 9.11.2 AI untuk Security Test Generation

```
PROMPT:
"Analisis Flask API endpoint berikut untuk kerentanan OWASP Top 10.
Untuk setiap kerentanan yang ditemukan, buatkan:
1. Deskripsi risiko
2. Contoh exploit
3. pytest test case yang mendeteksi kerentanan
4. Rekomendasi perbaikan

@app.route('/api/user/profile', methods=['PUT'])
@login_required
def update_profile():
    data = request.get_json()
    user = User.query.get(data['user_id'])
    user.name = data['name']
    user.email = data['email']
    user.role = data.get('role', user.role)
    db.session.commit()
    return jsonify(user.to_dict())"
```

**Evaluasi:** AI yang baik akan mendeteksi:
- Broken Access Control (user bisa update profil orang lain via `data['user_id']`)
- Mass Assignment (`data.get('role')` — user bisa jadi admin!)
- Missing input validation (email format, name length)

### 9.11.3 AI untuk Performance Optimization

```
PROMPT:
"SQLAlchemy query berikut memiliki N+1 problem dan slow response.
Analisis dan berikan:
1. Penjelasan mengapa lambat
2. Query yang dioptimasi
3. Locust test untuk membandingkan performance sebelum/sesudah

@app.route('/api/peminjaman')
def list_peminjaman():
    peminjaman = Peminjaman.query.all()
    result = []
    for p in peminjaman:
        result.append({
            'id': p.id,
            'buku': p.buku.judul,           # N+1 query!
            'peminjam': p.user.nama,         # N+1 query!
            'tanggal': p.tanggal.isoformat()
        })
    return jsonify(result)"
```

### 9.11.4 AI untuk Mutation Testing Analysis

```
PROMPT:
"Berikut adalah mutants yang SURVIVED (tidak terdeteksi test suite saya).
Untuk setiap survived mutant, buatkan test case yang akan KILL mutant tersebut:

1. app/dompet.py line 35:
   - if jumlah < 10000:
   + if jumlah <= 10000:

2. app/dompet.py line 42:
   - self.saldo -= jumlah
   + self.saldo -= jumlah + 1

3. app/validators.py line 15:
   - return len(pin) == 6
   + return len(pin) >= 6"
```

### 9.11.5 Evaluasi AI-Generated Quality Metrics

```
PROMPT:
"Evaluasi quality metrics berikut untuk proyek Flask e-commerce
dan berikan rekomendasi perbaikan:

Code Coverage: 72% (line), 58% (branch)
Cyclomatic Complexity: average 8.5, max 25
Mutation Score: 65%
Defect Density: 8.2 per KLOC
Test-to-Code Ratio: 0.6
Dependencies with known vulnerabilities: 3

Konteks: Ini adalah proyek kuliah RPL Semester 4."
```

### 9.11.6 Hands-On: AI Quality Audit

**Aktivitas:**
1. Pilih modul dari proyek kelompok Anda (min 100 baris kode)
2. Jalankan coverage report: `pytest --cov --cov-branch`
3. Jalankan complexity check: `radon cc -a`
4. Minta AI: "Audit kualitas kode ini berdasarkan metrics dan rekomendasikan 5 perbaikan prioritas"
5. Implementasikan minimal 2 rekomendasi
6. Bandingkan metrics sebelum dan sesudah

> **Etika AI dalam QA:** Dalam industri fintech Indonesia yang diregulasi OJK, AI-generated tests tidak boleh menjadi satu-satunya garis pertahanan. Regulasi mengharuskan human oversight dalam security testing. AI adalah pemercepat, bukan pengganti professional security auditor.

---

## Latihan Soal

### Level Dasar (C1-C2) — 6 Soal

1. Jelaskan siklus TDD Red-Green-Refactor. Mengapa test harus ditulis SEBELUM implementasi?

2. Apa perbedaan antara QA (Quality Assurance) dan testing? Berikan masing-masing 2 contoh aktivitas.

3. Sebutkan 5 risiko OWASP Top 10 dan jelaskan masing-masing secara singkat.

4. Jelaskan perbedaan antara line coverage, branch coverage, dan path coverage. Mengapa branch coverage lebih informatif dari line coverage?

5. Apa itu mutation testing? Apa yang diukur oleh mutation score?

6. Jelaskan 4 jenis performance testing (load, stress, spike, endurance) dengan contoh skenario masing-masing.

### Level Menengah (C3-C4) — 7 Soal

7. Implementasikan TDD (Red-Green-Refactor) untuk fitur **"Kalkulator Pajak PPh 21 Indonesia"**:
   - Penghasilan 0 - 60 juta: tarif 5%
   - 60 juta - 250 juta: tarif 15%
   - 250 juta - 500 juta: tarif 25%
   - > 500 juta: tarif 30%
   Tulis minimal 3 iterasi TDD lengkap.

8. Buatlah Playwright E2E test untuk alur **pendaftaran mahasiswa baru** di portal kampus: buka halaman daftar -> isi form (nama, email, jurusan, upload foto) -> submit -> verifikasi halaman konfirmasi.

9. Diberikan kode berikut, hitung cyclomatic complexity-nya dan tentukan jumlah minimum test paths:
   ```python
   def proses_pembayaran(metode, nominal, saldo, is_verified):
       if metode == "transfer" and nominal > 100000000:
           if not is_verified:
               return "perlu_verifikasi"
       if saldo < nominal:
           return "saldo_kurang"
       if metode == "kredit" and not is_verified:
           return "kredit_perlu_verifikasi"
       return "berhasil"
   ```

10. Buatlah security test cases (pytest) untuk mendeteksi 3 kerentanan OWASP pada endpoint Flask yang menerima input dari user (search, login, update profile).

11. Implementasikan quality gates di GitHub Actions workflow untuk proyek Flask dengan: linting (flake8), testing (pytest, coverage >= 75%), security check (bandit).

12. Tulis Locust load test script untuk API endpoint `/api/transaksi` dengan skenario: 500 virtual users, masing-masing melakukan 3 operasi (cek saldo, transfer, cek riwayat).

13. Analisis kode berikut dan identifikasi semua kemungkinan mutant. Untuk setiap mutant, tentukan apakah test yang diberikan akan KILL atau SURVIVE:
    ```python
    def is_eligible_for_scholarship(ipk, semester, is_active):
        return ipk >= 3.5 and semester <= 8 and is_active

    def test_eligible():
        assert is_eligible_for_scholarship(3.8, 4, True) == True
    ```

### Level Mahir (C5-C6) — 7 Soal

14. Rancang testing strategy komprehensif untuk aplikasi **Dana/OVO/GoPay** (dompet digital Indonesia). Tentukan: test cases per level, tools, coverage target, dan bagaimana memenuhi regulasi BI/OJK.

15. Evaluasi: "TDD memperlambat development." Berikan analisis berimbang dengan data dari studi empiris (Microsoft, IBM) dan konteks proyek kuliah vs industri.

16. Sebuah aplikasi fintech memiliki metrics berikut: line coverage 95%, branch coverage 60%, mutation score 45%. Mengapa situasi ini problematik meskipun line coverage tinggi? Bagaimana cara memperbaikinya?

17. Rancang AI-assisted testing workflow untuk tim developer 4 orang. Tentukan: kapan menggunakan AI untuk generate tests, kapan manual testing diperlukan, dan quality gates apa yang harus ada.

18. Bandingkan pendekatan testing untuk: (a) startup yang baru launch MVP, (b) perusahaan fintech yang sudah comply OJK, (c) proyek open source dengan banyak kontributor. Bagaimana TDD, coverage target, dan security testing berbeda?

19. Desain mutation testing strategy untuk modul pembayaran dengan 50+ fungsi. Bagaimana Anda memprioritaskan fungsi mana yang perlu mutation testing? Apa threshold mutation score yang Anda tetapkan?

20. Evaluasi penggunaan AI (Claude/Copilot) untuk security testing pada sistem perbankan Indonesia. Identifikasi: (a) apa yang bisa diandalkan ke AI, (b) apa yang harus tetap dilakukan manusia, (c) risiko over-reliance pada AI. Hubungkan dengan regulasi OJK.

---

## Rangkuman

1. **TDD (Test-Driven Development)** mengikuti siklus Red-Green-Refactor: tulis test gagal, implementasi minimal, refactor. Studi menunjukkan 40-80% lebih sedikit bug.

2. **E2E testing** dengan Playwright menguji alur lengkap dari perspektif pengguna melalui browser automation. Gunakan hanya untuk critical user journeys.

3. **Performance testing** memiliki 4 jenis utama: load, stress, spike, dan endurance. Locust (Python) adalah tools populer untuk load testing.

4. **Security testing** wajib mengacu pada OWASP Top 10. Untuk fintech Indonesia, regulasi OJK mengharuskan penetration testing minimal 1x per tahun.

5. **Mutation testing** mengevaluasi kualitas test suite dengan membuat perubahan kecil pada kode dan memeriksa apakah test mendeteksinya. Target mutation score >= 80%.

6. **Code coverage** memiliki beberapa level (line, branch, path). Branch coverage lebih informatif dari line coverage. Target bervariasi: 70% (kuliah) sampai 90%+ (perbankan).

7. **Cyclomatic complexity** mengukur jumlah jalur independen melalui kode. Target: <= 10 per fungsi.

8. **Quality gates** adalah checkpoint otomatis (lint, test, coverage, security) yang harus dilalui sebelum kode di-merge.

9. **AI-assisted testing** membantu generate test cases dan mendeteksi kerentanan, tetapi tetap memerlukan human oversight, terutama untuk security dan business logic.

10. **Fintech Indonesia** (GoPay, OVO, Dana) harus comply dengan regulasi BI dan OJK yang mensyaratkan testing keamanan yang ketat.

---

## Referensi

1. Beck, K. (2003). *Test Driven Development: By Example*. Addison-Wesley.
2. Whittaker, J. A. (2009). *Exploratory Software Testing*. Addison-Wesley.
3. OWASP Foundation. (2021). *OWASP Top 10 Web Application Security Risks*. https://owasp.org/Top10/
4. Playwright Documentation. (2025). *Playwright for Python*. https://playwright.dev/python/
5. Humble, J. & Farley, D. (2010). *Continuous Delivery*. Addison-Wesley.
6. Jia, Y. & Harman, M. (2011). *An Analysis and Survey of the Development of Mutation Testing*. IEEE TSE.
7. OJK. (2021). *POJK No. 4/POJK.05/2021 tentang Penyelenggara Inovasi Keuangan Digital*.
8. Locust Documentation. (2025). *Locust: Modern Load Testing*. https://locust.io/

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
