# Lab 10: E2E Testing dan AI-Assisted Testing

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 9 dari 13 (Minggu 10) |
| **Topik** | Playwright E2E, AI Test Generation, Performance Testing |
| **CPMK** | CPMK-5 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |

## Tujuan

1. **Menulis** E2E test dengan Playwright
2. **Menggunakan** AI untuk generate test cases dan membandingkan dengan manual
3. **Menjalankan** basic performance test

## Langkah-langkah

### Langkah 1: Setup Playwright (10 menit)
```bash
pip install playwright pytest-playwright
playwright install chromium
```

### Langkah 2: E2E Test Login (25 menit)
```python
# tests/test_e2e.py
from playwright.sync_api import Page

def test_login_berhasil(page: Page):
    page.goto("http://localhost:5000/login")
    page.fill("#username", "mahasiswa01")
    page.fill("#password", "password123")
    page.click("#btn-login")
    assert page.url.endswith("/dashboard")

def test_login_gagal(page: Page):
    page.goto("http://localhost:5000/login")
    page.fill("#username", "wrong")
    page.fill("#password", "wrong")
    page.click("#btn-login")
    assert page.locator(".error-message").is_visible()
```

### Langkah 3: AI-Assisted Test Generation (25 menit)
1. Pilih 3 fungsi dari proyek Anda
2. Gunakan AI (Claude/ChatGPT) untuk generate test cases
3. Bandingkan:

| Aspek | AI-Generated | Manual |
|-------|-------------|--------|
| Happy path | ✓/✗ | ✓/✗ |
| Edge cases | ✓/✗ | ✓/✗ |
| Business logic | ✓/✗ | ✓/✗ |
| Correctness | _/5 benar | _/5 benar |

### Langkah 4: Basic Performance Test (20 menit)
```python
# locustfile.py
from locust import HttpUser, task, between

class PerpustakaanUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def search_buku(self):
        self.client.get("/api/buku?q=algoritma")

    @task(1)
    def get_detail(self):
        self.client.get("/api/buku/1")
```
```bash
pip install locust
locust -f locustfile.py --headless -u 10 -r 2 -t 30s --host http://localhost:5000
```

## Tantangan Tambahan

1. E2E test untuk alur peminjaman buku end-to-end
2. Bandingkan response time dengan 10 vs 50 concurrent users

## Checklist Penyelesaian

- [ ] 2+ E2E tests dengan Playwright
- [ ] AI-generated tests untuk 3 fungsi
- [ ] Perbandingan AI vs manual tests tercatat
- [ ] Performance test berjalan (locust)
- [ ] AI Usage Log diisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
