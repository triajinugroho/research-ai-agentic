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
| **CPMK** | CPMK-5: Merancang strategi pengujian komprehensif (unit, integration, E2E) serta menerapkan TDD dan AI-assisted testing |
| **Sub-CPMK** | 10.1 Menganalisis teknik E2E testing dan kapan diterapkan dalam pipeline (C4) |
| | 10.2 Mengevaluasi pendekatan performance testing dan security testing dasar (C5) |
| | 10.3 Menerapkan AI-assisted testing untuk meningkatkan efisiensi pengujian (C4) |
| **Durasi** | 150 menit (3 × 50 menit) |
| **Metode** | Ceramah interaktif, demo E2E test, AI-assisted test generation exercise |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menganalisis** kapan E2E testing diperlukan dan trade-off-nya terhadap unit/integration test (C4)
2. **Menerapkan** E2E test sederhana menggunakan Playwright (C4)
3. **Mengevaluasi** aspek performance dan security testing dalam konteks web application (C5)
4. **Menganalisis** konsep mutation testing dan code coverage sebagai metrik kualitas test (C4)
5. **Menerapkan** AI tools untuk membantu generate dan review test cases (C4)

---

## Materi Pembelajaran

### 10.1 End-to-End (E2E) Testing

E2E testing menguji alur pengguna (*user flow*) secara keseluruhan — dari UI hingga database dan kembali.

```
Testing Pyramid — Trade-off
┌────────┐
│  E2E   │  Sedikit, lambat, mahal, tapi realistis
├────────┤
│ Integ. │  Sedang
├────────┤
│  Unit  │  Banyak, cepat, murah, tapi terisolasi
└────────┘
```

#### Playwright — Framework E2E Modern

Playwright mendukung multi-browser (Chromium, Firefox, WebKit) dan tersedia untuk Python maupun JavaScript.

```python
# test_login.py — E2E test dengan Playwright (Python)
from playwright.sync_api import sync_playwright

def test_login_berhasil():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Buka halaman login
        page.goto("http://localhost:3000/login")

        # Isi form login
        page.fill("#email", "mahasiswa@uai.ac.id")
        page.fill("#password", "rahasia123")
        page.click("button[type='submit']")

        # Verifikasi redirect ke dashboard
        page.wait_for_url("**/dashboard")
        assert "Dashboard" in page.title()

        browser.close()
```

```javascript
// login.spec.js — E2E test dengan Playwright (JavaScript)
const { test, expect } = require('@playwright/test');

test('mahasiswa berhasil login', async ({ page }) => {
  await page.goto('http://localhost:3000/login');
  await page.fill('#email', 'mahasiswa@uai.ac.id');
  await page.fill('#password', 'rahasia123');
  await page.click('button[type="submit"]');

  await expect(page).toHaveURL(/dashboard/);
  await expect(page.locator('h1')).toContainText('Dashboard');
});
```

### 10.2 Performance Testing

Performance testing memastikan aplikasi tetap responsif di bawah beban tinggi.

| Tipe | Tujuan | Tool |
|------|--------|------|
| **Load Testing** | Respons di bawah beban normal | Locust, k6 |
| **Stress Testing** | Titik patah (*breaking point*) | k6, Artillery |
| **Spike Testing** | Lonjakan tiba-tiba | k6 |
| **Endurance Testing** | Stabilitas jangka panjang | Locust |

**Contoh Indonesia:** Simulasi lonjakan akses pada sistem PPDB (Penerimaan Peserta Didik Baru) di hari pengumuman.

```python
# locustfile.py — Load test sederhana
from locust import HttpUser, task, between

class PenggunaSistemPPDB(HttpUser):
    wait_time = between(1, 3)  # Jeda 1-3 detik antar request

    @task(3)
    def lihat_pengumuman(self):
        self.client.get("/api/pengumuman")

    @task(1)
    def cek_hasil(self):
        self.client.get("/api/hasil/12345")
```

### 10.3 Security Testing Basics — OWASP Top 10

OWASP (*Open Worldwide Application Security Project*) mendefinisikan 10 risiko keamanan teratas:

| # | Risiko | Contoh | Pencegahan |
|---|--------|--------|------------|
| A01 | Broken Access Control | User biasa akses endpoint admin | Middleware authorization |
| A02 | Cryptographic Failures | Password tersimpan plaintext | bcrypt/argon2 hashing |
| A03 | Injection | SQL Injection via form input | Parameterized queries |
| A07 | Authentication Failures | Brute force login | Rate limiting, 2FA |

```python
# BURUK — Rentan SQL Injection
query = f"SELECT * FROM users WHERE email = '{email}'"

# BAIK — Parameterized query
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
```

> **Nilai Islami — Amanah (Kepercayaan):** Menjaga keamanan data pengguna adalah bentuk amanah. Kebocoran data (*data breach*) tidak hanya merugikan secara teknis, tetapi juga melanggar kepercayaan yang diberikan pengguna.

### 10.4 Code Coverage dan Mutation Testing

#### Code Coverage

Mengukur seberapa banyak kode yang dieksekusi oleh test suite:

```bash
# Python — pytest-cov
pytest --cov=src --cov-report=html

# JavaScript — Jest built-in
npx jest --coverage
```

| Metrik | Deskripsi | Target |
|--------|-----------|--------|
| Line Coverage | % baris yang dieksekusi | ≥ 80% |
| Branch Coverage | % cabang if/else yang diuji | ≥ 70% |
| Function Coverage | % fungsi yang dipanggil | ≥ 90% |

**Peringatan:** Coverage tinggi ≠ kualitas test tinggi. Test bisa mengeksekusi kode tanpa benar-benar memverifikasi hasilnya.

#### Mutation Testing

Mutation testing mengukur **kualitas test** dengan memodifikasi (*mutate*) kode sumber dan memeriksa apakah test mendeteksi perubahan:

```
Kode asli:    if usia >= 60: diskon = 0.3
Mutan 1:      if usia >= 60: diskon = 0.5    ← test harus GAGAL
Mutan 2:      if usia >  60: diskon = 0.3    ← test harus GAGAL
Mutan 3:      if usia >= 60: diskon = 0.0    ← test harus GAGAL

Mutation Score = Mutan terdeteksi / Total mutan × 100%
```

### 10.5 AI-Assisted Testing

AI tools dapat membantu berbagai aspek testing:

| Aspek | Bagaimana AI Membantu | Tool |
|-------|----------------------|------|
| **Test Generation** | Generate test cases dari kode/requirements | Copilot, Claude |
| **Test Data** | Generate data test yang realistis | ChatGPT, Faker + AI |
| **Bug Detection** | Analisis kode untuk potensi bug | Claude Code, SonarQube |
| **Test Review** | Review kualitas test suite | Claude, Code review AI |

#### Prompt Engineering untuk AI-Assisted Testing

```
Prompt CRIDE untuk test generation:

[Context] Saya memiliki fungsi Python berikut: {paste kode}
[Role] Kamu adalah QA engineer berpengalaman
[Instruction] Generate unit test yang komprehensif menggunakan pytest
[Details] Sertakan: happy path, edge cases, error handling, boundary values
[Examples] Format seperti: def test_nama_skenario():
```

**Penting:** Selalu review test yang di-generate AI — jangan langsung percaya tanpa verifikasi. AI bisa menghasilkan test yang *tampak* benar tetapi memiliki asumsi salah.

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)

- Membaca ringkasan OWASP Top 10: [owasp.org/Top10](https://owasp.org/www-project-top-ten/)
- Menginstal Playwright: `pip install playwright && playwright install` atau `npm init playwright@latest`
- Refleksi: "Apa perbedaan antara test yang banyak dan test yang berkualitas?"

### In-class (120 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-25 menit | E2E testing concepts + demo Playwright | Ceramah + demo |
| 25-45 menit | Performance testing dan security testing basics | Ceramah + contoh |
| 45-55 menit | Code coverage vs mutation testing | Ceramah + diskusi |
| 55-60 menit | *Break* | — |
| 60-90 menit | Hands-on: tulis E2E test untuk alur registrasi sederhana | Hands-on coding |
| 90-110 menit | AI-assisted test generation exercise: gunakan Claude/Copilot untuk generate test, lalu review | Exercise + diskusi |
| 110-120 menit | Diskusi: strategi testing mana yang cocok untuk proyek kelompok? | Diskusi kelas |

### Post-class (15 menit)

- Lanjutkan eksplorasi Playwright untuk proyek kelompok
- Jalankan `pytest --cov` pada modul proyek dan analisis hasilnya
- Catat pengalaman menggunakan AI untuk testing di AI Usage Log

---

## Referensi

1. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach*, 9th ed. McGraw-Hill. Chapter 22-24.
2. OWASP Foundation. (2021). *OWASP Top 10:2021*. [owasp.org](https://owasp.org/www-project-top-ten/)
3. Playwright documentation. [playwright.dev](https://playwright.dev/)
4. Fowler, M. (2018). "The Practical Test Pyramid." [martinfowler.com](https://martinfowler.com/articles/practical-test-pyramid.html)
5. Locust documentation. [locust.io](https://locust.io/)
6. Jest documentation — Coverage. [jestjs.io](https://jestjs.io/docs/cli#--coverage)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
