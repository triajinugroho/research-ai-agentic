# Lab 10: E2E Testing dan AI-Assisted Testing

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 9 dari 13 (Minggu 10) |
| **Topik** | Playwright E2E Testing, AI-Assisted Test Generation, Security Testing, Mutation Testing |
| **CPMK** | CPMK-5 (Sub-CPMK 5.3, 5.4) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 09 selesai, Flask app berjalan dengan halaman HTML, pemahaman dasar pytest |

## Tujuan

1. **Memahami** (C2) konsep End-to-End testing dan perbedaannya dengan unit/integration test
2. **Menulis** (C3) E2E test dengan Playwright untuk menguji alur pengguna
3. **Mengevaluasi** (C5) kualitas test yang dihasilkan AI dibandingkan test manual
4. **Menjelaskan** (C2) prinsip dasar security testing (OWASP Top 10) dan mutation testing

## Konsep Singkat

### Apa Itu E2E Testing?

End-to-End (E2E) testing menguji aplikasi dari perspektif pengguna nyata — mulai dari membuka browser, mengisi form, klik tombol, hingga melihat hasil. Berbeda dari unit test yang menguji fungsi terisolasi, E2E test memverifikasi bahwa *seluruh sistem* bekerja bersama.

```
Unit Test:        [Fungsi A] -----> assert output benar
Integration Test: [Fungsi A] + [Database] -----> assert data tersimpan
E2E Test:         [Browser] -> [UI] -> [API] -> [DB] -> [UI] -> assert halaman benar
```

### Mengapa E2E Testing Penting?

Bayangkan sistem akademik UAI: unit test memastikan fungsi `hitung_ipk()` benar, integration test memastikan data tersimpan di database, tetapi *hanya E2E test* yang bisa memastikan mahasiswa benar-benar bisa login, melihat KRS, dan mengunduh transkrip melalui browser.

### Playwright vs Selenium

| Aspek | Playwright | Selenium |
|-------|-----------|----------|
| **Bahasa** | Python, JS, Java, .NET | Python, JS, Java, C#, Ruby |
| **Browser** | Chromium, Firefox, WebKit | Chrome, Firefox, Safari, Edge |
| **Kecepatan** | Cepat (headless default) | Lebih lambat |
| **Auto-wait** | Ya (built-in) | Perlu explicit wait |
| **Setup** | `pip install playwright` | Perlu driver terpisah |
| **Debugging** | Trace viewer, codegen | Screenshot, logs |

Kita menggunakan **Playwright** karena lebih modern, cepat, dan memiliki fitur auto-wait yang mengurangi flaky tests.

### AI-Assisted Testing

AI tools (Claude, ChatGPT, Copilot) dapat membantu:
- **Generate test cases** dari spesifikasi atau kode sumber
- **Identifikasi edge cases** yang mungkin terlewat oleh developer
- **Generate test data** untuk skenario yang beragam

Namun AI juga memiliki keterbatasan:
- Bisa menghasilkan test yang *terlihat benar* tetapi sebenarnya tidak menguji apa-apa
- Kurang memahami business logic spesifik domain Anda
- Perlu dievaluasi dan dimodifikasi oleh manusia

### Security Testing dan OWASP Top 10

OWASP (*Open Worldwide Application Security Project*) menerbitkan daftar 10 risiko keamanan web paling kritis:

| No | Risiko OWASP | Contoh di Aplikasi Perpustakaan |
|----|-------------|--------------------------------|
| 1 | Broken Access Control | Mahasiswa bisa akses data admin |
| 2 | Cryptographic Failures | Password disimpan plain text |
| 3 | Injection (SQL/XSS) | Input `'; DROP TABLE buku;--` |
| 4 | Insecure Design | Tidak ada rate limiting pada login |
| 5 | Security Misconfiguration | Debug mode aktif di production |

### Mutation Testing

Mutation testing mengukur *kualitas* test suite Anda. Ide dasarnya: jika kita sengaja memasukkan bug (*mutant*) ke kode, apakah test suite kita mendeteksinya (*killed*)?

```
Kode asli:     if stok > 0: return True
Mutant 1:      if stok >= 0: return True    # Ubah > jadi >=
Mutant 2:      if stok > 1: return True     # Ubah 0 jadi 1
Mutant 3:      if stok > 0: return False    # Ubah True jadi False

Mutation Score = (mutants killed / total mutants) x 100%
```

Jika mutation score rendah, artinya test Anda terlalu lemah — banyak bug potensial yang tidak terdeteksi.

## Persiapan

### Tools yang Dibutuhkan

```bash
# Install Playwright
pip install playwright pytest-playwright
playwright install chromium

# Install mutation testing tool
pip install mutmut

# Verifikasi
playwright --version
# Expected: Version 1.4x.x
```

### Pastikan Aplikasi Berjalan

```bash
# Di terminal terpisah, jalankan Flask app
flask run --port 5000

# Verifikasi di terminal lain
curl http://localhost:5000
# Expected: HTML response (halaman utama)
```

> **Troubleshooting:** Di Codespaces, pastikan port 5000 di-forward. Klik tab "Ports" di bagian bawah VS Code, tambahkan port 5000 jika belum ada.

## Langkah-langkah

### Langkah 1: Setup Playwright dan Test Pertama (15 menit)

**Mengapa:** Sebelum menulis E2E test kompleks, pastikan Playwright terkonfigurasi dan bisa mengakses aplikasi. Test pertama yang sederhana memvalidasi setup.

```python
# tests/test_e2e.py
import pytest
from playwright.sync_api import Page, expect


def test_homepage_loads(page: Page):
    """Test: halaman utama bisa diakses dan menampilkan judul."""
    page.goto("http://localhost:5000")

    # Verifikasi judul halaman
    expect(page).to_have_title("Perpustakaan Digital")

    # Verifikasi elemen utama ada
    heading = page.locator("h1")
    expect(heading).to_be_visible()
    expect(heading).to_contain_text("Perpustakaan")


def test_navigation_links(page: Page):
    """Test: link navigasi utama berfungsi."""
    page.goto("http://localhost:5000")

    # Klik link "Katalog"
    page.click("a[href='/katalog']")
    expect(page).to_have_url("http://localhost:5000/katalog")

    # Klik link "Login"
    page.click("a[href='/login']")
    expect(page).to_have_url("http://localhost:5000/login")
```

**Jalankan:**

```bash
pytest tests/test_e2e.py -v --headed  # --headed untuk melihat browser
# Atau tanpa browser (headless, lebih cepat):
pytest tests/test_e2e.py -v
```

**Expected output:**

```
tests/test_e2e.py::test_homepage_loads PASSED
tests/test_e2e.py::test_navigation_links PASSED

=================== 2 passed in 3.21s ===================
```

> **Troubleshooting:** Jika muncul `Error: Browser closed unexpectedly`, coba `playwright install --with-deps chromium`. Di Codespaces, headless mode (`--headed` dihapus) biasanya lebih stabil.

**Estimasi waktu:** 15 menit

---

### Langkah 2: E2E Test Alur Login (20 menit)

**Mengapa:** Login adalah alur kritis di hampir semua aplikasi web. E2E test login memverifikasi interaksi antara form HTML, backend authentication, dan session management.

```python
# tests/test_e2e_login.py
from playwright.sync_api import Page, expect


def test_login_berhasil(page: Page):
    """Test: login dengan kredensial valid mengarahkan ke dashboard."""
    page.goto("http://localhost:5000/login")

    # Isi form login
    page.fill("#username", "mahasiswa01")
    page.fill("#password", "password123")

    # Klik tombol login
    page.click("#btn-login")

    # Verifikasi: redirect ke dashboard
    expect(page).to_have_url("http://localhost:5000/dashboard")

    # Verifikasi: nama pengguna ditampilkan
    welcome = page.locator(".welcome-message")
    expect(welcome).to_contain_text("mahasiswa01")


def test_login_gagal_password_salah(page: Page):
    """Test: login dengan password salah menampilkan error."""
    page.goto("http://localhost:5000/login")

    page.fill("#username", "mahasiswa01")
    page.fill("#password", "wrong_password")
    page.click("#btn-login")

    # Verifikasi: tetap di halaman login
    expect(page).to_have_url("http://localhost:5000/login")

    # Verifikasi: pesan error ditampilkan
    error = page.locator(".error-message")
    expect(error).to_be_visible()
    expect(error).to_contain_text("Username atau password salah")


def test_login_gagal_field_kosong(page: Page):
    """Test: submit form login dengan field kosong."""
    page.goto("http://localhost:5000/login")

    # Langsung klik login tanpa isi field
    page.click("#btn-login")

    # Verifikasi: HTML5 validation mencegah submit
    # atau pesan error ditampilkan
    expect(page).to_have_url("http://localhost:5000/login")


def test_logout(page: Page):
    """Test: logout menghapus session dan redirect ke login."""
    # Login dulu
    page.goto("http://localhost:5000/login")
    page.fill("#username", "mahasiswa01")
    page.fill("#password", "password123")
    page.click("#btn-login")

    # Klik logout
    page.click("#btn-logout")

    # Verifikasi: redirect ke halaman login
    expect(page).to_have_url("http://localhost:5000/login")

    # Verifikasi: akses dashboard tanpa login = redirect
    page.goto("http://localhost:5000/dashboard")
    expect(page).to_have_url("http://localhost:5000/login")
```

**Tips menulis E2E test yang stabil:**

| Praktik | Baik | Buruk |
|---------|------|-------|
| **Selector** | `#btn-login` (ID unik) | `.btn` (class umum) |
| **Waiting** | Gunakan `expect()` (auto-wait) | `time.sleep(2)` |
| **Data** | Test user khusus untuk testing | Data production |
| **Isolation** | Setiap test independen | Test bergantung urutan |

> **Troubleshooting:** Jika test gagal dengan timeout, kemungkinan selector salah. Gunakan `playwright codegen http://localhost:5000` untuk merekam interaksi dan mendapatkan selector yang benar secara otomatis.

**Estimasi waktu:** 20 menit

---

### Langkah 3: AI-Assisted Test Generation (25 menit)

**Mengapa:** AI bisa mempercepat penulisan test, tetapi kualitasnya perlu dievaluasi. Latihan ini melatih kemampuan *critical evaluation* terhadap output AI — skill yang semakin penting di era AI-augmented development.

**Langkah 3a: Pilih 3 fungsi dari proyek Anda**

Contoh fungsi yang dipilih:
1. `search_buku(keyword)` — pencarian buku
2. `pinjam_buku(user_id, buku_id)` — proses peminjaman
3. `hitung_denda(hari_terlambat)` — perhitungan denda

**Langkah 3b: Tulis test manual untuk 1 fungsi (5 menit)**

```python
# Test manual untuk search_buku
def test_search_manual_keyword_valid():
    result = search_buku("algoritma")
    assert len(result) >= 1
    assert all("algoritma" in b["judul"].lower() for b in result)

def test_search_manual_keyword_kosong():
    result = search_buku("")
    assert isinstance(result, list)

def test_search_manual_special_chars():
    result = search_buku("<script>alert('xss')</script>")
    assert isinstance(result, list)  # Tidak crash
```

**Langkah 3c: Gunakan AI untuk generate test (10 menit)**

Berikan prompt berikut ke Claude atau ChatGPT:

```
Saya memiliki fungsi Python berikut untuk sistem perpustakaan:

def search_buku(keyword: str) -> list[dict]:
    """Cari buku berdasarkan keyword di judul. Return list of dicts with keys: id, judul, penulis, stok."""
    # implementasi menggunakan SQLAlchemy query

Buatkan pytest test cases yang komprehensif. Cover:
- Happy path (keyword ditemukan)
- Keyword tidak ditemukan
- Edge cases (string kosong, karakter spesial, very long string)
- Case sensitivity
- Partial match vs exact match
```

**Langkah 3d: Bandingkan dan evaluasi (10 menit)**

Isi tabel perbandingan berikut:

| Aspek | AI-Generated Tests | Manual Tests | Keterangan |
|-------|-------------------|--------------|------------|
| **Jumlah test** | ___ test | ___ test | |
| **Happy path** | Ada / Tidak | Ada / Tidak | |
| **Edge cases** | ___ kasus | ___ kasus | AI biasanya menemukan lebih banyak |
| **Business logic** | Tepat / Tidak | Tepat / Tidak | Manual biasanya lebih akurat |
| **Runnable tanpa modifikasi** | ___/total pass | ___/total pass | |
| **False positives** | ___ test | ___ test | Test pass tapi tidak menguji apa-apa |
| **Waktu penulisan** | ___ menit | ___ menit | |

**Lakukan untuk ketiga fungsi**, lalu jawab:
1. Kapan AI-generated test paling berguna?
2. Di area mana AI test paling sering salah?
3. Apa strategi terbaik: AI-first lalu edit, atau manual-first lalu AI review?

> **Tips:** Perhatikan apakah AI menggunakan mock yang benar, apakah assertion cukup spesifik (bukan hanya `assert result is not None`), dan apakah test benar-benar independen satu sama lain.

**Estimasi waktu:** 25 menit

---

### Langkah 4: Security Testing Awareness (15 menit)

**Mengapa:** Keamanan bukan fitur opsional — ini adalah *requirement*. Untuk konteks Indonesia, kasus kebocoran data (BPJS, e-HAC, Tokopedia) menunjukkan pentingnya security testing sejak awal pengembangan.

**Langkah 4a: Test SQL Injection sederhana**

```python
# tests/test_security.py
def test_sql_injection_search(client):
    """Test: input berbahaya tidak menyebabkan SQL injection."""
    # Payload SQL injection klasik
    payloads = [
        "'; DROP TABLE buku;--",
        "' OR '1'='1",
        "1; SELECT * FROM users",
        "' UNION SELECT username, password FROM users--",
    ]

    for payload in payloads:
        resp = client.get(f"/api/buku?q={payload}")
        # Harus tetap mengembalikan response valid (bukan error 500)
        assert resp.status_code in [200, 400], \
            f"SQL injection mungkin berhasil dengan payload: {payload}"
        # Tidak boleh mengembalikan data dari tabel lain
        if resp.status_code == 200:
            for buku in resp.json:
                assert "password" not in buku


def test_xss_prevention(client):
    """Test: input HTML/script tidak dieksekusi."""
    xss_payload = "<script>alert('XSS')</script>"
    resp = client.post("/api/buku", json={
        "judul": xss_payload,
        "penulis": "Test",
        "stok": 1
    })

    if resp.status_code == 201:
        # Jika tersimpan, pastikan di-escape saat ditampilkan
        buku_id = resp.json["id"]
        get_resp = client.get(f"/api/buku/{buku_id}")
        # Response JSON seharusnya aman, tapi cek di HTML rendering
        assert "<script>" not in get_resp.get_data(as_text=True) or \
               resp.json["judul"] == xss_payload  # JSON storage OK, HTML must escape
```

**Langkah 4b: Checklist security sederhana**

Evaluasi aplikasi Anda terhadap checklist ini:

```
[ ] Password di-hash (bcrypt/argon2), bukan plain text
[ ] Session timeout dikonfigurasi
[ ] CSRF protection aktif (Flask-WTF)
[ ] Input divalidasi di backend (bukan hanya frontend)
[ ] Error messages tidak mengexpose detail teknis ke user
[ ] HTTPS digunakan di production
[ ] Environment variables untuk secrets (bukan hardcode)
[ ] Rate limiting pada endpoint login
```

> **Tips:** Jangan abaikan security karena ini "hanya proyek kuliah". Kebiasaan baik dimulai dari sekarang. Di industri, security vulnerability bisa menyebabkan kerugian miliaran rupiah.

**Estimasi waktu:** 15 menit

---

### Langkah 5: Mutation Testing (15 menit)

**Mengapa:** Code coverage 90% tidak berarti test Anda berkualitas tinggi. Mutation testing memberikan metrik yang lebih jujur tentang seberapa efektif test Anda mendeteksi bug.

```bash
# Jalankan mutation testing pada module denda
mutmut run --paths-to-mutate=app/services/denda.py --tests-dir=tests/
```

**Expected output:**

```
- Mutant 1: survived (stok > 0 -> stok >= 0)
- Mutant 2: killed (return True -> return False)
- Mutant 3: killed (hari * tarif -> hari + tarif)
- Mutant 4: survived (< 0 -> <= 0)

Mutation score: 2/4 = 50%
```

**Analisis hasil:**

```bash
# Lihat mutant yang survived (tidak terdeteksi test)
mutmut results
```

```
Survived mutants:
  - Line 10: changed > to >=
  - Line 15: changed < to <=
```

**Artinya:** Test Anda tidak cukup spesifik untuk membedakan `>` dan `>=`. Anda perlu menambahkan boundary test:

```python
def test_hitung_denda_boundary_zero():
    """Boundary: tepat 0 hari = denda 0 (bukan negatif)."""
    assert hitung_denda(0) == 0  # Memastikan > vs >= benar

def test_hitung_denda_boundary_minus_one():
    """Boundary: -1 hari harus raise error (bukan return 0)."""
    with pytest.raises(ValueError):
        hitung_denda(-1)  # Memastikan < vs <= benar
```

```bash
# Jalankan ulang mutation testing
mutmut run --paths-to-mutate=app/services/denda.py --tests-dir=tests/
# Expected: Mutation score meningkat
```

> **Troubleshooting:** `mutmut` bisa lambat untuk codebase besar. Batasi scope dengan `--paths-to-mutate` ke file spesifik. Jika terlalu lama, Ctrl+C dan analisis hasil parsial.

**Estimasi waktu:** 15 menit

---

### Langkah 6: Playwright Codegen dan Trace (10 menit)

**Mengapa:** Playwright memiliki tools built-in yang mempercepat penulisan E2E test. Codegen merekam interaksi Anda menjadi kode test, dan trace viewer membantu debugging test yang gagal.

**Codegen — record interaksi menjadi kode:**

```bash
playwright codegen http://localhost:5000
```

Ini membuka browser + inspector. Lakukan interaksi (klik, isi form, dll) dan Playwright otomatis generate kode Python. Salin kode yang dihasilkan ke file test Anda.

**Trace — debugging visual untuk test yang gagal:**

```python
# Tambahkan di conftest.py untuk recording trace
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "record_video_dir": "test-results/videos/",
    }
```

```bash
# Jalankan test dengan trace
pytest tests/test_e2e.py --tracing=on

# Buka trace viewer
playwright show-trace test-results/trace.zip
```

Trace viewer menampilkan:
- Screenshot setiap langkah
- Network requests
- Console logs
- DOM snapshot

> **Tips:** Trace sangat berguna untuk debugging flaky tests (test yang kadang pass, kadang gagal). Biasanya masalahnya adalah timing — elemen belum muncul saat assertion dijalankan.

**Estimasi waktu:** 10 menit

## Tantangan Tambahan

### Tantangan 1: Basic — E2E Test Pencarian Buku

Tulis E2E test lengkap untuk fitur pencarian buku:
1. Buka halaman katalog
2. Ketik keyword di search box
3. Klik tombol cari
4. Verifikasi hasil sesuai keyword
5. Test juga skenario: tidak ditemukan, keyword kosong

### Tantangan 2: Intermediate — AI Test Evaluation Report

Buat laporan perbandingan AI vs manual testing untuk seluruh 3 fungsi. Hitung:
- Total waktu penulisan (AI vs manual)
- Jumlah bug yang ditemukan oleh masing-masing
- Kualitas assertion (spesifik vs generic)
- Kesimpulan: kapan gunakan AI, kapan manual?

### Tantangan 3: Advanced — Kill All Surviving Mutants

Jalankan mutation testing pada seluruh `app/services/`. Untuk setiap surviving mutant:
1. Analisis mengapa mutant survive
2. Tulis test baru untuk kill mutant tersebut
3. Target: mutation score >= 80%

## Refleksi & AI Usage Log

Setelah menyelesaikan lab ini, isi AI Usage Log:

| No | Task | Tool | Prompt (ringkas) | Output | Evaluasi | Modifikasi |
|----|------|------|------------------|--------|----------|------------|
| 1 | ... | ... | ... | ... | .../5 | ... |

**Pertanyaan refleksi:**
1. Apa kelebihan dan kekurangan E2E test dibanding unit test?
2. Seberapa akurat AI dalam menghasilkan test cases? Di area mana AI paling membantu?
3. Apa yang Anda pelajari dari mutation testing tentang kualitas test Anda?
4. Risiko keamanan mana yang paling relevan untuk proyek Anda?

## Checklist Penyelesaian

- [ ] Playwright terinstall dan berjalan
- [ ] 3+ E2E tests dengan Playwright (homepage, login berhasil, login gagal)
- [ ] AI-generated tests untuk 3 fungsi, lengkap dengan evaluasi
- [ ] Tabel perbandingan AI vs manual tests terisi
- [ ] Security test minimal 1 skenario (SQL injection atau XSS)
- [ ] Mutation testing dijalankan dan hasilnya dianalisis
- [ ] Refleksi dan AI Usage Log diisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
