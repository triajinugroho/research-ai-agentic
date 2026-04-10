# BAB 9: ADVANCED TESTING DAN QUALITY ASSURANCE

**Oleh: Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom |
|-----------|-----------|-------------|
| 5.3 | Merancang E2E testing dan performance testing strategy | C4 (Menganalisis) |
| 5.4 | Menerapkan QA practices termasuk AI-assisted testing dan quality gates | C5 (Mengevaluasi) |

---

## 9.1 End-to-End (E2E) Testing

### 9.1.1 Apa Itu E2E Testing?

E2E testing menguji alur lengkap dari perspektif pengguna — mulai dari membuka browser hingga mendapatkan hasil yang diharapkan.

### 9.1.2 Playwright untuk E2E Testing

```python
# test_e2e_login.py
from playwright.sync_api import sync_playwright

def test_login_berhasil():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        page.goto("http://localhost:5000/login")
        page.fill("#username", "mahasiswa01")
        page.fill("#password", "password123")
        page.click("#btn-login")
        
        assert page.url == "http://localhost:5000/dashboard"
        assert page.inner_text("h1") == "Dashboard"
        
        browser.close()

def test_login_gagal():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        page.goto("http://localhost:5000/login")
        page.fill("#username", "wrong")
        page.fill("#password", "wrong")
        page.click("#btn-login")
        
        error = page.inner_text(".error-message")
        assert "Username atau password salah" in error
        
        browser.close()
```

## 9.2 Performance Testing

| Tipe | Tujuan | Tool |
|------|--------|------|
| **Load Testing** | Test dengan beban normal | Locust, k6 |
| **Stress Testing** | Test di atas kapasitas | Locust, k6 |
| **Spike Testing** | Lonjakan tiba-tiba | k6 |
| **Endurance Testing** | Beban lama (memory leak) | k6 |

```python
# locustfile.py — Load Testing
from locust import HttpUser, task, between

class PerpustakaanUser(HttpUser):
    wait_time = between(1, 3)
    
    @task(3)
    def cari_buku(self):
        self.client.get("/api/buku?q=algoritma")
    
    @task(1)
    def lihat_detail(self):
        self.client.get("/api/buku/1")
```

## 9.3 Security Testing Basics

| Vulnerability | Deskripsi | Mitigasi |
|--------------|-----------|----------|
| **SQL Injection** | Input yang memanipulasi query SQL | Gunakan ORM/parameterized queries |
| **XSS** | Script injection via input user | Escape output, CSP headers |
| **CSRF** | Request palsu dari site lain | CSRF token |
| **Broken Auth** | Session hijacking, brute force | Rate limiting, secure cookies |

```python
# RENTAN SQL Injection
query = f"SELECT * FROM buku WHERE judul = '{user_input}'"

# AMAN dengan parameterized query (SQLAlchemy)
buku = Buku.query.filter(Buku.judul.contains(user_input)).all()
```

## 9.4 Quality Assurance (QA)

### 9.4.1 QA vs Testing

| QA | Testing |
|----|----|
| **Preventif** — mencegah cacat | **Detektif** — menemukan cacat |
| Proses dan standar | Eksekusi test |
| Sepanjang SDLC | Fase testing |

### 9.4.2 Quality Metrics

| Metrik | Formula | Target |
|--------|---------|--------|
| Code Coverage | Lines tested / total lines × 100% | ≥ 80% |
| Defect Density | Bugs / KLOC (1000 lines) | < 5 |
| Mean Time to Repair | Total repair time / number of repairs | < 4 jam |
| Test Pass Rate | Tests passed / total tests × 100% | ≥ 95% |

### 9.4.3 Quality Gates

Quality gates adalah checkpoint sebelum kode masuk ke fase berikutnya:

```
Feature Branch → PR Created
    ↓
[Quality Gate 1: Automated Tests]
    ✓ All unit tests pass
    ✓ Coverage ≥ 80%
    ✓ No critical security issues
    ↓
[Quality Gate 2: Code Review]
    ✓ Minimal 1 reviewer approve
    ✓ No unresolved comments
    ↓
[Quality Gate 3: Integration]
    ✓ Integration tests pass
    ✓ No merge conflicts
    ↓
Merge to develop
```

## 9.5 AI-Assisted Testing

### 9.5.1 AI untuk Test Generation

```
Prompt: "Buatkan pytest test cases untuk fungsi berikut, 
termasuk happy path, edge cases, dan error handling:

def hitung_denda(hari_terlambat, tarif_per_hari=1000):
    if hari_terlambat < 0:
        raise ValueError('Hari terlambat tidak boleh negatif')
    return hari_terlambat * tarif_per_hari"
```

### 9.5.2 Evaluasi AI-Generated Tests

| Aspek | AI Kuat | AI Lemah |
|-------|---------|----------|
| Happy path coverage | ✓ | |
| Edge cases | Sebagian | Boundary values sering miss |
| Business logic | | Tidak paham konteks bisnis |
| Integration scenarios | | Sulit tanpa konteks arsitektur |
| Security tests | Basic | Advanced penetration |

---

## AI Corner: AI untuk Advanced Testing (Level: Advanced)

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| E2E test generation | "Buatkan Playwright test untuk alur peminjaman buku end-to-end" | Review selectors dan assertions |
| Security analysis | "Analisis kode Flask ini untuk potensi kerentanan keamanan" | AI sebagai first pass, bukan pengganti security audit |
| Performance tips | "Bagaimana mengoptimasi query SQLAlchemy yang N+1?" | Verify dengan profiling tools |

---

## Latihan Soal

### Level Dasar (C1-C2)
1. Jelaskan perbedaan E2E testing, integration testing, dan unit testing.
2. Sebutkan 4 jenis performance testing.
3. Apa perbedaan QA dan testing?

### Level Menengah (C3-C4)
4. Buatlah E2E test case untuk alur pendaftaran mahasiswa baru.
5. Identifikasi 3 kerentanan keamanan dalam kode Flask berikut dan perbaiki.
6. Rancang quality gates untuk CI/CD pipeline proyek Sistem Perpustakaan.

### Level Mahir (C5-C6)
7. Evaluasi: "Apakah AI bisa menggantikan QA engineer?" — berikan argumen pro dan kontra.
8. Rancang test automation strategy lengkap untuk aplikasi e-commerce (unit, integration, E2E, performance, security).

---

## Rangkuman

1. **E2E testing** menguji alur lengkap dari perspektif pengguna menggunakan Playwright/Selenium.
2. **Performance testing** (load, stress, spike, endurance) memastikan aplikasi performant di bawah beban.
3. **Security testing** mencegah SQL injection, XSS, CSRF, dan kerentanan OWASP Top 10.
4. **QA** bersifat preventif — membangun kualitas ke dalam proses, bukan hanya menemukan bug.
5. **Quality gates** memastikan kode melewati standar kualitas sebelum merge.
6. **AI-assisted testing** berguna untuk generating test cases tetapi perlu evaluasi manusia untuk edge cases dan business logic.

---

## Referensi

1. Whittaker, J. A. (2009). *Exploratory Software Testing*. Addison-Wesley.
2. OWASP Foundation. (2021). *OWASP Top 10 Web Application Security Risks*.
3. Playwright Documentation. (2024). *Playwright for Python*. playwright.dev.
4. Humble, J. & Farley, D. (2010). *Continuous Delivery*. Addison-Wesley.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
