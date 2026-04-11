# Minggu 10: Advanced Testing dan Test Automation

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 10 dari 16 |
| **Topik** | Advanced Testing dan Test Automation |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK-5: Merancang dan melaksanakan strategi pengujian perangkat lunak yang komprehensif (unit, integration, E2E) serta menerapkan quality assurance practices termasuk TDD dan AI-assisted testing |
| **Sub-CPMK** | Sub-CPMK-5.3: Menerapkan Test-Driven Development (TDD) dan AI-assisted testing (C4) |
| | Sub-CPMK-5.4: Mengevaluasi kualitas perangkat lunak menggunakan metrics (code coverage, cyclomatic complexity) (C5) |
| **Durasi** | 150 menit (3 x 50 menit) |
| **Metode** | Ceramah interaktif, demo E2E test, AI-assisted test generation exercise |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menganalisis** kapan E2E testing diperlukan dan trade-off-nya terhadap unit/integration test (C4)
2. **Menerapkan** E2E test menggunakan Playwright untuk menguji alur pengguna pada web application (C3)
3. **Mengevaluasi** aspek performance testing dan security testing (OWASP Top 10) dalam konteks web application (C5)
4. **Menganalisis** konsep mutation testing sebagai metrik kualitas test yang lebih akurat dibanding code coverage (C4)
5. **Menerapkan** AI tools (Copilot, Claude) untuk membantu generate dan review test cases secara bertanggung jawab (C4)

---

## Materi Pembelajaran

### 10.1 End-to-End (E2E) Testing

E2E testing menguji alur pengguna (*user flow*) secara keseluruhan -- dari UI hingga database dan kembali. E2E mensimulasikan bagaimana *pengguna nyata* menggunakan aplikasi.

```
Testing Pyramid — Posisi E2E Testing

       /\            E2E: Sedikit test, lambat, mahal,
      /  \           tapi PALING REALISTIS
     / E2E\          (menguji dari perspektif pengguna)
    /______\
   / Integ. \        Integration: Sedang
  /__________\
 /   Unit     \      Unit: Banyak test, cepat, murah,
/_______________\    tapi PALING TERISOLASI

Trade-off:
┌──────────────┬────────┬────────────┬──────────┬──────────────┐
│ Aspek        │ Unit   │ Integration│ E2E      │ Manual       │
├──────────────┼────────┼────────────┼──────────┼──────────────┤
│ Kecepatan    │ ★★★★★  │ ★★★        │ ★★       │ ★            │
│ Biaya        │ ★★★★★  │ ★★★        │ ★★       │ ★            │
│ Realisme     │ ★★     │ ★★★        │ ★★★★★    │ ★★★★★        │
│ Stabilitas   │ ★★★★★  │ ★★★★       │ ★★       │ ★            │
│ Maintenance  │ ★★★★★  │ ★★★        │ ★★       │ N/A          │
└──────────────┴────────┴────────────┴──────────┴──────────────┘
★ = rendah/murah, ★★★★★ = tinggi/mahal
```

**Kapan menggunakan E2E test?**
- Alur bisnis kritis (checkout, pembayaran, registrasi)
- Integrasi antar sistem (frontend + backend + database)
- Regression test untuk fitur utama
- Verifikasi sebelum release ke production

**Kapan TIDAK menggunakan E2E?**
- Logika bisnis yang bisa diuji dengan unit test
- Validasi input sederhana
- Kode yang sering berubah (E2E test rapuh / *flaky*)

#### Playwright -- Framework E2E Modern

Playwright mendukung multi-browser (Chromium, Firefox, WebKit) dan tersedia untuk Python maupun JavaScript. Dibuat oleh Microsoft, Playwright lebih modern dan stabil dibanding Selenium.

```
Playwright vs Selenium vs Cypress
┌──────────────┬────────────┬──────────┬──────────┐
│ Fitur        │ Playwright │ Selenium │ Cypress  │
├──────────────┼────────────┼──────────┼──────────┤
│ Multi-browser│ ✓ (3)      │ ✓ (semua)│ ✗ (1)    │
│ Auto-wait    │ ✓          │ ✗        │ ✓        │
│ Bahasa       │ Python, JS,│ Banyak   │ JS only  │
│              │ C#, Java   │          │          │
│ Kecepatan    │ Cepat      │ Lambat   │ Cepat    │
│ API modern   │ ✓          │ ✗        │ ✓        │
│ Network mock │ ✓          │ ✗        │ ✓        │
└──────────────┴────────────┴──────────┴──────────┘
```

**E2E Test: Alur Registrasi Mahasiswa (Python + Playwright)**

```python
# test_registrasi.py — E2E test dengan Playwright (Python)
from playwright.sync_api import sync_playwright, expect

def test_registrasi_mahasiswa_berhasil():
    """E2E: Mahasiswa baru berhasil registrasi akun"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Buka halaman registrasi
        page.goto("http://localhost:3000/register")
        expect(page).to_have_title("Registrasi - Sistem Akademik UAI")

        # 2. Isi form registrasi
        page.fill("#nama", "Ahmad Fauzi")
        page.fill("#nim", "120042")
        page.fill("#email", "ahmad.fauzi@uai.ac.id")
        page.fill("#password", "rahasia123")
        page.fill("#konfirmasi-password", "rahasia123")

        # 3. Pilih program studi
        page.select_option("#prodi", "Informatika")

        # 4. Centang persetujuan
        page.check("#setuju-syarat")

        # 5. Klik tombol daftar
        page.click("button[type='submit']")

        # 6. Verifikasi redirect ke halaman sukses
        page.wait_for_url("**/register/success")
        expect(page.locator("h1")).to_contain_text("Registrasi Berhasil")
        expect(page.locator(".welcome-message")).to_contain_text("Ahmad Fauzi")

        browser.close()

def test_registrasi_email_sudah_terdaftar():
    """E2E: Registrasi gagal jika email sudah digunakan"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("http://localhost:3000/register")
        page.fill("#nama", "Siti Aminah")
        page.fill("#nim", "120043")
        page.fill("#email", "admin@uai.ac.id")  # Email sudah ada
        page.fill("#password", "rahasia456")
        page.fill("#konfirmasi-password", "rahasia456")
        page.select_option("#prodi", "Informatika")
        page.check("#setuju-syarat")
        page.click("button[type='submit']")

        # Verifikasi pesan error
        expect(page.locator(".error-message")).to_contain_text(
            "Email sudah terdaftar"
        )
        expect(page).to_have_url("**/register")  # Tetap di halaman register

        browser.close()
```

**E2E Test: Alur Login (JavaScript + Playwright)**

```javascript
// login.spec.js — E2E test dengan Playwright (JavaScript)
const { test, expect } = require('@playwright/test');

test.describe('Alur Login Sistem Akademik', () => {

  test('mahasiswa berhasil login dengan kredensial valid', async ({ page }) => {
    // 1. Buka halaman login
    await page.goto('http://localhost:3000/login');

    // 2. Isi form login
    await page.fill('#email', 'mahasiswa@uai.ac.id');
    await page.fill('#password', 'rahasia123');

    // 3. Klik tombol login
    await page.click('button[type="submit"]');

    // 4. Verifikasi berhasil masuk dashboard
    await expect(page).toHaveURL(/dashboard/);
    await expect(page.locator('h1')).toContainText('Dashboard');
    await expect(page.locator('.user-name')).toContainText('mahasiswa');
  });

  test('menampilkan error untuk password salah', async ({ page }) => {
    await page.goto('http://localhost:3000/login');
    await page.fill('#email', 'mahasiswa@uai.ac.id');
    await page.fill('#password', 'salah123');
    await page.click('button[type="submit"]');

    await expect(page.locator('.alert-error')).toBeVisible();
    await expect(page.locator('.alert-error')).toContainText(
      'Email atau password salah'
    );
  });

  test('redirect ke login jika akses dashboard tanpa autentikasi', async ({ page }) => {
    await page.goto('http://localhost:3000/dashboard');
    await expect(page).toHaveURL(/login/);
  });
});
```

**Setup Playwright di GitHub Codespaces:**

```bash
# Python
pip install playwright
playwright install chromium

# JavaScript
npm init playwright@latest
# Ikuti wizard: pilih TypeScript/JavaScript, test folder, dsb.
```

### 10.2 Performance Testing

Performance testing memastikan aplikasi tetap responsif di bawah berbagai kondisi beban. Ini sangat penting untuk aplikasi yang melayani banyak pengguna bersamaan.

```
Tipe-tipe Performance Testing
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  Load Testing        Stress Testing       Spike Testing  │
│  ┌─────────┐        ┌─────────┐         ┌────────┐     │
│  │ ▁▂▃▄▄▄▄ │        │ ▁▂▃▅▇██ │         │ ▁▁█▁▁▁ │     │
│  │         │        │   Break!│         │  Spike!│     │
│  └─────────┘        └─────────┘         └────────┘     │
│  Beban normal        Cari titik patah    Lonjakan       │
│  dan expected        (breaking point)    tiba-tiba      │
│                                                          │
│  Endurance Test      Scalability Test                    │
│  ┌──────────┐       ┌──────────┐                        │
│  │ ▄▄▄▄▄▄▄▄ │       │ ▂▃▄▅▆▇█ │                        │
│  │ Lama...  │       │ Tambah   │                        │
│  └──────────┘       │ resource │                        │
│  Stabilitas          └──────────┘                        │
│  jangka panjang      Scale up/out                        │
└──────────────────────────────────────────────────────────┘
```

| Tipe | Tujuan | Contoh Skenario Indonesia |
|------|--------|---------------------------|
| **Load Testing** | Respons di bawah beban normal | 10.000 user akses Tokopedia bersamaan |
| **Stress Testing** | Cari titik patah (*breaking point*) | Simulasi 1 juta request ke sistem PPDB |
| **Spike Testing** | Lonjakan mendadak | Flash sale Shopee 11.11 |
| **Endurance Testing** | Stabilitas jangka panjang | Sistem BPJS beroperasi 24/7 selama seminggu |
| **Scalability Testing** | Kemampuan auto-scale | Gojek saat jam makan siang vs dini hari |

**Contoh Load Test dengan Locust (Python):**

```python
# locustfile.py — Load test untuk API toko UMKM
from locust import HttpUser, task, between

class PenggunaToko(HttpUser):
    """Simulasi pengguna mengakses toko online UMKM"""
    wait_time = between(1, 3)  # Jeda 1-3 detik antar request

    @task(5)
    def lihat_katalog(self):
        """70% traffic: lihat daftar produk"""
        self.client.get("/api/produk")

    @task(3)
    def lihat_detail_produk(self):
        """Lihat detail produk tertentu"""
        self.client.get("/api/produk/1")

    @task(1)
    def buat_pesanan(self):
        """Buat pesanan baru (traffic rendah)"""
        self.client.post("/api/pesanan", json={
            "produk_id": 1,
            "jumlah": 2,
            "alamat": "Jl. Sisingamangaraja, Jakarta Selatan"
        })

    @task(1)
    def cek_status_pesanan(self):
        """Cek status pesanan"""
        self.client.get("/api/pesanan/1/status")
```

```bash
# Menjalankan Locust
$ pip install locust
$ locust -f locustfile.py --host=http://localhost:5000

# Buka http://localhost:8089 untuk UI Locust
# Set: Number of users = 100, Spawn rate = 10
```

**Contoh Load Test dengan k6 (JavaScript):**

```javascript
// load-test.js — k6 load test
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 50 },   // Ramp up ke 50 users
    { duration: '1m',  target: 50 },   // Tahan 50 users selama 1 menit
    { duration: '30s', target: 0 },    // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],   // 95% request < 500ms
    http_req_failed: ['rate<0.01'],     // Error rate < 1%
  },
};

export default function () {
  const res = http.get('http://localhost:5000/api/produk');
  check(res, {
    'status 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });
  sleep(1);
}
```

```bash
# Jalankan k6
$ k6 run load-test.js
```

### 10.3 Security Testing Basics -- OWASP Top 10

OWASP (*Open Worldwide Application Security Project*) mendefinisikan 10 risiko keamanan teratas untuk web application. Setiap developer wajib memahami ini:

```
OWASP Top 10 (2021) — 5 Teratas yang Paling Relevan
┌─────┬────────────────────────┬───────────────────────────────┐
│ No  │ Risiko                 │ Dampak                        │
├─────┼────────────────────────┼───────────────────────────────┤
│ A01 │ Broken Access Control  │ User biasa akses data admin   │
│ A02 │ Cryptographic Failures │ Password/data sensitif bocor  │
│ A03 │ Injection              │ Attacker jalankan kode jahat  │
│ A07 │ Auth. Failures         │ Akun dibobol brute force      │
│ A09 │ Logging Failures       │ Serangan tidak terdeteksi     │
└─────┴────────────────────────┴───────────────────────────────┘
```

#### A03: SQL Injection -- Serangan Paling Klasik

```python
# ===== BURUK: Rentan SQL Injection =====
# Penyerang bisa input: ' OR '1'='1' --
# Query menjadi: SELECT * FROM users WHERE email = '' OR '1'='1' --'
def login_vulnerable(email, password):
    query = f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'"
    cursor.execute(query)  # BAHAYA!

# ===== BAIK: Parameterized Query =====
def login_secure(email, password):
    cursor.execute(
        "SELECT * FROM users WHERE email = %s AND password = %s",
        (email, password)  # Parameter terpisah dari query
    )
```

```javascript
// ===== BURUK: Rentan SQL Injection (Node.js) =====
app.get('/user', (req, res) => {
  const query = `SELECT * FROM users WHERE id = ${req.query.id}`;
  db.query(query);  // BAHAYA!
});

// ===== BAIK: Parameterized Query =====
app.get('/user', (req, res) => {
  db.query('SELECT * FROM users WHERE id = ?', [req.query.id]);
});
```

#### A02: Cryptographic Failures -- Hashing Password

```python
# ===== BURUK: Password tersimpan plaintext =====
def simpan_user(email, password):
    db.execute("INSERT INTO users VALUES (?, ?)", (email, password))
    # Jika database bocor, semua password terekspos!

# ===== BAIK: Password di-hash dengan bcrypt =====
import bcrypt

def simpan_user(email, password):
    # Hash password (salt otomatis ditambahkan)
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db.execute("INSERT INTO users VALUES (?, ?)", (email, hashed))

def verifikasi_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)
```

#### A01: Broken Access Control

```python
# ===== BURUK: Tidak ada pengecekan authorization =====
@app.route("/api/admin/users")
def get_all_users():
    return jsonify(User.query.all())  # Siapa saja bisa akses!

# ===== BAIK: Cek role sebelum akses =====
@app.route("/api/admin/users")
@login_required
def get_all_users():
    if current_user.role != "admin":
        abort(403, "Akses ditolak: hanya admin")
    return jsonify(User.query.all())
```

> **Nilai Islami -- Amanah (Kepercayaan):** Menjaga keamanan data pengguna adalah bentuk amanah. Dalam Islam, amanah adalah sifat yang sangat penting -- kebocoran data bukan hanya masalah teknis, tetapi juga pelanggaran kepercayaan yang diberikan pengguna kepada kita sebagai pengembang.

### 10.4 Code Coverage dan Mutation Testing

#### Code Coverage -- Mengukur Kuantitas Test

Code coverage mengukur **seberapa banyak kode** yang dieksekusi oleh test suite:

```bash
# Python — pytest-cov
$ pytest --cov=src --cov-report=term-missing --cov-report=html

# Output:
# Name               Stmts   Miss  Cover   Missing
# --------------------------------------------------
# src/auth.py           45      3    93%   67-69
# src/produk.py         32      0   100%
# src/pesanan.py        28      8    71%   15-18, 33-36
# --------------------------------------------------
# TOTAL                105     11    90%

# JavaScript — Jest built-in
$ npx jest --coverage

# Output:
# ------------|---------|----------|---------|---------|
# File        | % Stmts | % Branch | % Funcs | % Lines |
# ------------|---------|----------|---------|---------|
# auth.js     |   95.24 |    85.71 |     100 |   95.24 |
# produk.js   |     100 |      100 |     100 |     100 |
# ------------|---------|----------|---------|---------|
```

| Metrik Coverage | Deskripsi | Target Minimum |
|----------------|-----------|----------------|
| **Line Coverage** | % baris kode yang dieksekusi | >= 80% |
| **Branch Coverage** | % cabang if/else yang diuji | >= 70% |
| **Function Coverage** | % fungsi yang dipanggil | >= 90% |
| **Statement Coverage** | % statement yang dieksekusi | >= 80% |

**Peringatan: Coverage Tinggi != Test Berkualitas**

```python
# Contoh: Coverage 100% tapi test TIDAK bermakna!
def hitung_diskon(harga, persen):
    return harga * (1 - persen / 100)

def test_hitung_diskon():
    # Test ini mengeksekusi 100% kode...
    hitung_diskon(100, 10)
    # ...tapi TIDAK memverifikasi hasilnya!
    # Tidak ada assert -> test selalu lulus meski kode salah

# Test yang BERMAKNA:
def test_hitung_diskon_benar():
    assert hitung_diskon(100000, 10) == 90000
    assert hitung_diskon(50000, 0) == 50000
    assert hitung_diskon(100000, 100) == 0
```

#### Mutation Testing -- Mengukur Kualitas Test

Mutation testing mengukur **kualitas test** dengan memodifikasi (*mutate*) kode sumber dan memeriksa apakah test mendeteksi perubahannya:

```
Cara Kerja Mutation Testing:

Kode Asli:
  def hitung_diskon(harga, usia):
      if usia >= 60:
          return int(harga * 0.7)

Mutasi yang dibuat:
┌─────────┬──────────────────────┬────────────────────────┐
│ Mutan   │ Perubahan            │ Test harus...          │
├─────────┼──────────────────────┼────────────────────────┤
│ Mutan 1 │ usia >= 60 -> > 60   │ GAGAL (terdeteksi ✓)  │
│ Mutan 2 │ 0.7 -> 0.5           │ GAGAL (terdeteksi ✓)  │
│ Mutan 3 │ 0.7 -> 0.0           │ GAGAL (terdeteksi ✓)  │
│ Mutan 4 │ >= 60 -> >= 61       │ LULUS (survived ✗)    │
└─────────┴──────────────────────┴────────────────────────┘

Mutation Score = Mutan terdeteksi / Total mutan x 100%
              = 3 / 4 x 100% = 75%

Mutan 4 survived -> Artinya test kita KURANG TAJAM
  untuk nilai boundary 60. Perlu tambah test!
```

```bash
# Mutation testing di Python dengan mutmut
$ pip install mutmut
$ mutmut run --paths-to-mutate=src/

# Hasil:
# - 40 mutan dibuat
# - 35 terdeteksi (killed)
# - 5 survived (test kurang tajam!)
# Mutation score: 87.5%

# Lihat mutan yang survived:
$ mutmut results
```

```
Perbandingan Code Coverage vs Mutation Score:
┌──────────────────┬───────────────────┬──────────────────────┐
│ Metrik           │ Code Coverage     │ Mutation Score       │
├──────────────────┼───────────────────┼──────────────────────┤
│ Mengukur         │ Kuantitas test    │ Kualitas test        │
│ Pertanyaan       │ "Berapa % kode   │ "Apakah test bisa   │
│                  │  yang dieksekusi?"│  mendeteksi bug?"    │
│ Bisa dipalsukan? │ Ya (tanpa assert) │ Sulit               │
│ Biaya komputasi  │ Rendah            │ Tinggi (N x test)   │
│ Target           │ >= 80%            │ >= 70%               │
└──────────────────┴───────────────────┴──────────────────────┘
```

### 10.5 AI-Assisted Testing

AI tools dapat membantu berbagai aspek testing -- dari generate test case hingga analisis coverage gap:

```
AI dalam Testing Pipeline
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  1. Requirements    2. Test Design    3. Test Code       │
│  ┌──────────┐      ┌──────────┐     ┌──────────┐       │
│  │ AI bantu │      │ AI bantu │     │ AI bantu │       │
│  │ analisis │─────▶│ generate │────▶│ generate │       │
│  │ user     │      │ test     │     │ test     │       │
│  │ stories  │      │ cases    │     │ code     │       │
│  └──────────┘      └──────────┘     └──────────┘       │
│                                          │               │
│  4. Test Review     5. Bug Analysis      │               │
│  ┌──────────┐      ┌──────────┐         │               │
│  │ AI bantu │      │ AI bantu │◀────────┘               │
│  │ review   │      │ analisis │                          │
│  │ kualitas │      │ root     │                          │
│  │ test     │      │ cause    │                          │
│  └──────────┘      └──────────┘                          │
│                                                          │
│  PENTING: Semua output AI harus di-REVIEW manusia!       │
└──────────────────────────────────────────────────────────┘
```

| Aspek Testing | Bagaimana AI Membantu | Tool | Akurasi |
|---------------|----------------------|------|---------|
| **Test Generation** | Generate test cases dari kode/requirements | Copilot, Claude | 70-80% perlu review |
| **Test Data** | Generate data test realistis Indonesia | Claude, Faker + AI | Baik |
| **Bug Detection** | Analisis kode untuk potensi bug | Claude Code, SonarQube | Sedang |
| **Test Review** | Review kualitas test suite | Claude, CodeRabbit | Baik |
| **Coverage Gap** | Identifikasi area yang belum ter-test | Copilot, Claude | Baik |

#### Prompt Engineering untuk AI-Assisted Testing (CRIDE)

```
[Context]
Saya memiliki fungsi Python untuk menghitung ongkos kirim
dalam aplikasi toko online UMKM. Framework: Flask + pytest.

[Role]
Kamu adalah QA engineer senior yang ahli dalam test design.

[Instruction]
Generate unit test yang komprehensif menggunakan pytest
untuk fungsi hitung_ongkir() di bawah ini.

[Details]
- Sertakan: happy path, edge cases, error handling, boundary values
- Gunakan teknik: Equivalence Partitioning dan BVA
- Format: class TestHitungOngkir dengan method test_*
- Gunakan pytest.mark.parametrize jika ada banyak kasus serupa
- Tambahkan docstring untuk setiap test menjelaskan skenario

[Examples]
def test_ongkir_dalam_jawa_ringan():
    """Berat <= 1kg, tujuan Jawa -> Rp 10.000"""
    assert hitung_ongkir(berat_kg=0.5, tujuan="Jakarta") == 10000
```

**Contoh penggunaan AI untuk generate test:**

```python
# Fungsi yang akan di-test (diberikan ke AI)
def hitung_ongkir(berat_kg: float, tujuan: str) -> int:
    """Hitung ongkos kirim berdasarkan berat dan tujuan."""
    JAWA = ["Jakarta", "Bandung", "Surabaya", "Semarang", "Yogyakarta"]

    if berat_kg <= 0:
        raise ValueError("Berat harus positif")
    if not tujuan:
        raise ValueError("Tujuan tidak boleh kosong")

    base = 10000 if tujuan in JAWA else 20000
    if berat_kg <= 1:
        return base
    tambahan = int((berat_kg - 1) * (5000 if tujuan in JAWA else 10000))
    return base + tambahan

# === Output AI (setelah review dan perbaikan manusia): ===
import pytest

class TestHitungOngkir:
    """Test suite untuk hitung_ongkir - generated AI, reviewed human"""

    # Happy path
    def test_ringan_dalam_jawa(self):
        """Berat 0.5kg ke Jakarta -> Rp 10.000"""
        assert hitung_ongkir(0.5, "Jakarta") == 10000

    def test_ringan_luar_jawa(self):
        """Berat 0.5kg ke Makassar -> Rp 20.000"""
        assert hitung_ongkir(0.5, "Makassar") == 20000

    def test_berat_dalam_jawa(self):
        """Berat 3kg ke Bandung -> 10000 + 2*5000 = 20.000"""
        assert hitung_ongkir(3, "Bandung") == 20000

    def test_berat_luar_jawa(self):
        """Berat 3kg ke Medan -> 20000 + 2*10000 = 40.000"""
        assert hitung_ongkir(3, "Medan") == 40000

    # Boundary values
    def test_tepat_1kg_jawa(self):
        """Boundary: tepat 1kg masih base price"""
        assert hitung_ongkir(1.0, "Jakarta") == 10000

    def test_sedikit_diatas_1kg_jawa(self):
        """Boundary: 1.1kg -> ada tambahan"""
        assert hitung_ongkir(1.1, "Jakarta") == 10500

    # Error cases
    def test_berat_nol(self):
        with pytest.raises(ValueError, match="Berat harus positif"):
            hitung_ongkir(0, "Jakarta")

    def test_berat_negatif(self):
        with pytest.raises(ValueError, match="Berat harus positif"):
            hitung_ongkir(-1, "Jakarta")

    def test_tujuan_kosong(self):
        with pytest.raises(ValueError, match="Tujuan tidak boleh kosong"):
            hitung_ongkir(1, "")
```

**PENTING: Selalu Review Test yang Di-generate AI!**

```
Checklist Review Test dari AI:
┌─────────────────────────────────────────────────────────┐
│ ✓ Apakah test benar-benar menguji perilaku yang tepat?  │
│ ✓ Apakah expected value sudah dihitung manual?           │
│ ✓ Apakah edge cases ter-cover?                          │
│ ✓ Apakah test tidak mengulang kasus yang sama?           │
│ ✓ Apakah assertion cukup spesifik?                      │
│ ✓ Apakah test bisa gagal jika kode berubah salah?       │
│ ✗ Jangan percaya AI 100% — cek setiap expected value!   │
└─────────────────────────────────────────────────────────┘
```

### 10.6 Strategi Testing untuk Proyek Kelompok

```
Rekomendasi Testing Strategy untuk Proyek Akhir
┌────────────────────────────────────────────────────────┐
│ Layer        │ Tool        │ Target    │ Prioritas     │
├──────────────┼─────────────┼───────────┼───────────────┤
│ Unit Test    │ pytest/Jest │ >= 70%    │ ★★★★★ (wajib) │
│ Integration  │ pytest      │ API utama │ ★★★★ (penting)│
│ E2E Test     │ Playwright  │ 2-3 flow  │ ★★★ (ideal)   │
│ Security     │ Manual check│ OWASP A01 │ ★★★ (penting) │
│              │             │ A02, A03  │               │
│ Performance  │ Manual/k6   │ Baseline  │ ★★ (bonus)    │
└──────────────┴─────────────┴───────────┴───────────────┘

Sprint 2 (W10-11): Setup unit test + integration test
Sprint 3 (W12-13): Tambah E2E test + security check
Sprint 4 (W14):    Coverage >= 70%, fix security issues
```

---

## Kegiatan Pembelajaran

### Pre-class (20 menit)

- Membaca ringkasan OWASP Top 10: [owasp.org/Top10](https://owasp.org/www-project-top-ten/)
- Menginstal Playwright: `pip install playwright && playwright install chromium` atau `npm init playwright@latest`
- Jalankan `pip-audit` atau `npm audit` pada proyek kelompok, catat hasilnya
- Refleksi: "Apa perbedaan antara test yang banyak dan test yang berkualitas?"

### In-class (110 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-20 menit | E2E testing concepts + posisi di testing pyramid | Ceramah + diskusi |
| 20-35 menit | Demo Playwright: tulis E2E test untuk alur login | Live demo |
| 35-50 menit | Performance testing (Locust/k6) dan security testing (OWASP Top 10) | Ceramah + contoh |
| 50-55 menit | *Break* | -- |
| 55-70 menit | Code coverage vs mutation testing: mengukur kualitas test | Ceramah + diskusi |
| 70-90 menit | Hands-on: tulis E2E test untuk alur registrasi proyek kelompok | Hands-on coding |
| 90-105 menit | AI-assisted test generation: gunakan Claude/Copilot untuk generate test, lalu review bersama | Exercise + diskusi |
| 105-110 menit | Diskusi: strategi testing mana yang cocok untuk proyek kelompok? | Diskusi kelas |

### Post-class (20 menit)

- Lanjutkan eksplorasi Playwright untuk proyek kelompok (tambah 1-2 E2E test)
- Jalankan `pytest --cov` pada modul proyek dan analisis hasilnya -- identifikasi area yang belum ter-cover
- Catat pengalaman menggunakan AI untuk testing di AI Usage Log
- Lanjutkan pengerjaan tugas T4

---

## Latihan & Diskusi

### Soal 1 (C2 -- Memahami)
Jelaskan apa yang dimaksud dengan E2E testing. Mengapa E2E test ditempatkan di puncak testing pyramid dan jumlahnya paling sedikit? Berikan contoh 3 alur E2E test yang penting untuk aplikasi e-commerce UMKM.

### Soal 2 (C3 -- Menerapkan)
Tulis E2E test menggunakan Playwright (Python atau JavaScript) untuk menguji alur berikut pada aplikasi toko online:
1. User membuka halaman produk
2. User menambahkan produk ke keranjang
3. User melihat keranjang -- produk yang ditambahkan harus muncul
4. User menghapus produk dari keranjang -- keranjang harus kosong

### Soal 3 (C4 -- Menganalisis)
Perhatikan kode berikut:

```python
def login(email, password):
    query = f"SELECT * FROM users WHERE email = '{email}'"
    user = db.execute(query).fetchone()
    if user and user.password == password:
        return create_token(user)
    return None
```

Identifikasi minimal 3 kerentanan keamanan berdasarkan OWASP Top 10. Untuk masing-masing, jelaskan risikonya dan tuliskan kode yang sudah diperbaiki.

### Soal 4 (C5 -- Mengevaluasi)
Sebuah proyek memiliki code coverage 92% tetapi mutation score hanya 45%. Apa artinya ini? Jelaskan kemungkinan penyebabnya dan langkah-langkah konkret untuk meningkatkan mutation score tanpa menulis test yang berlebihan.

### Soal 5 (C5 -- Mengevaluasi)
Anda menggunakan AI (Claude) untuk generate 20 test cases untuk fungsi `hitung_ongkir()`. Setelah review, Anda menemukan bahwa 5 test cases memiliki expected value yang salah dan 3 test cases menguji skenario yang sama. Evaluasi:
a) Apakah AI-assisted testing efektif dalam kasus ini?
b) Apa strategi review yang seharusnya Anda terapkan?
c) Kapan AI-assisted testing paling berguna dan kapan kurang tepat?

---

## Referensi

1. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach*, 9th ed. McGraw-Hill. Chapter 22-24.
2. OWASP Foundation. (2021). *OWASP Top 10:2021*. [owasp.org](https://owasp.org/www-project-top-ten/)
3. Playwright documentation. [playwright.dev](https://playwright.dev/)
4. Fowler, M. (2018). "The Practical Test Pyramid." [martinfowler.com](https://martinfowler.com/articles/practical-test-pyramid.html)
5. Locust documentation. [locust.io](https://locust.io/)
6. k6 documentation. [k6.io](https://k6.io/)
7. Jest documentation -- Coverage. [jestjs.io](https://jestjs.io/docs/cli#--coverage)
8. IEEE Computer Society. (2024). *SWEBOK v4* -- Chapter 10: Software Testing.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
