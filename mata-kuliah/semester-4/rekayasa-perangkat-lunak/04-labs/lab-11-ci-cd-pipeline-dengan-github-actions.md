# Lab 11: CI/CD Pipeline dengan GitHub Actions

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 10 dari 13 (Minggu 11) |
| **Topik** | GitHub Actions, CI/CD Pipeline, Automated Linting, Testing, Deployment |
| **CPMK** | CPMK-6 (Sub-CPMK 6.1) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 09-10 selesai, repository GitHub aktif, pemahaman dasar YAML |

## Tujuan

1. **Memahami** (C2) konsep CI/CD dan manfaatnya dalam pengembangan perangkat lunak
2. **Membangun** (C3) CI pipeline dari nol menggunakan GitHub Actions (lint, test, build)
3. **Mengkonfigurasi** (C3) multi-stage pipeline dengan dependency antar jobs
4. **Men-debug** (C4) pipeline yang gagal dan memahami strategi troubleshooting

## Konsep Singkat

### Apa Itu CI/CD?

**Continuous Integration (CI)** adalah praktik menggabungkan (*merge*) kode dari semua developer ke branch utama secara sering (minimal 1x sehari), dengan setiap merge divalidasi oleh build dan test otomatis.

**Continuous Delivery (CD)** adalah ekstensi CI dimana kode yang lolos semua validasi *siap* di-deploy ke production kapan saja.

**Continuous Deployment** (satu langkah lebih jauh) melakukan deploy otomatis ke production tanpa intervensi manual.

```
Developer Push Code
       |
       v
  [CI Pipeline]
  +-----------+    +-----------+    +-----------+
  |   LINT    | -> |   TEST    | -> |   BUILD   |
  | (flake8)  |    | (pytest)  |    | (docker)  |
  +-----------+    +-----------+    +-----------+
       |                |                |
       v                v                v
     FAIL?            FAIL?           FAIL?
     -> Stop          -> Stop         -> Stop
                                        |
                                        v
                                  [CD Pipeline]
                                  +-----------+
                                  |  DEPLOY   |
                                  | (Railway) |
                                  +-----------+
                                        |
                                        v
                                   Production
```

### Mengapa CI/CD Penting?

| Tanpa CI/CD | Dengan CI/CD |
|-------------|--------------|
| "Kode saya jalan di laptop saya" | Diuji di environment standar |
| Bug ditemukan saat demo | Bug ditemukan saat push |
| Deploy manual, rawan human error | Deploy otomatis, konsisten |
| Merge conflict besar setelah berminggu-minggu | Conflict kecil, terdeteksi cepat |
| QA manual memakan waktu berhari-hari | Feedback dalam hitungan menit |

Perusahaan teknologi Indonesia seperti **Tokopedia** dan **Bukalapak** menerapkan CI/CD untuk deploy ratusan kali per hari dengan aman.

### GitHub Actions — Konsep Dasar

GitHub Actions adalah platform CI/CD yang terintegrasi langsung dengan GitHub. Konsep kunci:

| Konsep | Penjelasan | Analogi |
|--------|-----------|---------|
| **Workflow** | File YAML yang mendefinisikan pipeline | Resep masakan |
| **Event/Trigger** | Apa yang memicu workflow (push, PR, schedule) | Kapan memasak |
| **Job** | Kumpulan steps yang berjalan di satu runner | Satu tahap (misalnya: potong sayur) |
| **Step** | Satu tindakan dalam job | Satu instruksi (misalnya: cuci wortel) |
| **Runner** | Server virtual yang menjalankan job | Dapur |
| **Action** | Komponen reusable dari marketplace | Alat dapur siap pakai |

### Struktur File Workflow

```
.github/
└── workflows/
    ├── ci.yml       # Pipeline utama (lint + test)
    ├── deploy.yml   # Pipeline deployment (opsional)
    └── codeql.yml   # Security scanning (opsional)
```

### YAML Primer

YAML (*YAML Ain't Markup Language*) adalah format konfigurasi yang digunakan GitHub Actions. Aturan penting:

```yaml
# Indentasi menggunakan SPASI (BUKAN tab)
# 2 spasi per level adalah konvensi

key: value                    # String
number: 42                    # Integer
boolean: true                 # Boolean
list:                         # List
  - item1
  - item2
nested:                       # Nested object
  child_key: child_value
multiline: |                  # Multi-line string
  baris pertama
  baris kedua
```

## Persiapan

### Pastikan Repository GitHub Aktif

```bash
# Verifikasi remote repository
git remote -v
# Expected: origin  https://github.com/USERNAME/REPO.git

# Pastikan branch utama up-to-date
git status
git pull origin main
```

### Pastikan Test Suite Berjalan Lokal

```bash
# Jalankan test sebelum membuat pipeline
pytest tests/ -v
# Expected: semua test PASS

# Jalankan linter
pip install flake8
flake8 app/ --max-line-length=120
# Expected: tidak ada error (atau error yang sudah diketahui)
```

> **Troubleshooting:** Jika test gagal lokal, perbaiki dulu sebelum membuat CI pipeline. Pipeline akan gagal juga karena menjalankan test yang sama.

## Langkah-langkah

### Langkah 1: Buat Workflow File CI Dasar (15 menit)

**Mengapa:** Ini adalah fondasi pipeline Anda. Workflow dasar memvalidasi bahwa kode bisa diinstall dan test berjalan di environment bersih (bukan laptop developer).

```bash
# Buat direktori untuk workflows
mkdir -p .github/workflows
```

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

# Kapan pipeline dijalankan (trigger)
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

# Definisi pekerjaan (jobs)
jobs:
  lint:
    name: Code Linting
    runs-on: ubuntu-latest
    steps:
      - name: Checkout kode
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8

      - name: Jalankan flake8
        run: |
          flake8 app/ --max-line-length=120 --statistics
          echo "Linting berhasil!"

  test:
    name: Unit & Integration Tests
    runs-on: ubuntu-latest
    needs: lint  # Hanya jalan jika lint berhasil
    steps:
      - name: Checkout kode
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Jalankan tests dengan coverage
        run: |
          pytest tests/ --cov=app --cov-report=term-missing --cov-report=xml -v

      - name: Cek minimum coverage
        run: |
          pytest tests/ --cov=app --cov-fail-under=70
```

**Penjelasan setiap bagian:**

| Bagian | Fungsi |
|--------|--------|
| `on: push/pull_request` | Trigger: jalankan saat push ke main/develop atau saat PR dibuat |
| `runs-on: ubuntu-latest` | Runner: gunakan server Ubuntu terbaru dari GitHub |
| `needs: lint` | Dependency: job `test` menunggu `lint` selesai dulu |
| `actions/checkout@v4` | Action: clone repository ke runner |
| `actions/setup-python@v5` | Action: install Python versi tertentu |
| `--cov-fail-under=70` | Gagalkan pipeline jika coverage < 70% |

**Estimasi waktu:** 15 menit

---

### Langkah 2: Tambah Caching untuk Pipeline Lebih Cepat (10 menit)

**Mengapa:** Tanpa caching, setiap run pipeline mengunduh ulang semua dependencies (bisa 1-2 menit). Dengan caching, dependencies diambil dari cache (beberapa detik).

Modifikasi job `test` di `ci.yml`, tambahkan step caching sebelum install:

```yaml
  test:
    name: Unit & Integration Tests
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - name: Checkout kode
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      # BARU: Cache pip dependencies
      - name: Cache pip packages
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Jalankan tests dengan coverage
        run: |
          pytest tests/ --cov=app --cov-report=term-missing --cov-report=xml -v

      - name: Cek minimum coverage
        run: |
          pytest tests/ --cov=app --cov-fail-under=70
```

**Cara kerja cache:**
1. Run pertama: tidak ada cache, install dari internet, simpan ke cache
2. Run berikutnya: jika `requirements.txt` tidak berubah, ambil dari cache (jauh lebih cepat)
3. Jika `requirements.txt` berubah: cache miss, install ulang, cache baru disimpan

> **Tips:** Cache key menggunakan hash dari `requirements.txt`. Setiap kali file berubah, cache otomatis diperbarui.

**Estimasi waktu:** 10 menit

---

### Langkah 3: Push dan Lihat Pipeline Berjalan (10 menit)

**Mengapa:** Ini momen kebenaran (*moment of truth*) — apakah pipeline berjalan di server GitHub sama seperti di lokal?

```bash
# Stage dan commit workflow file
git add .github/workflows/ci.yml
git commit -m "ci: tambah GitHub Actions CI pipeline (lint + test)"
git push origin main
```

**Lihat pipeline di GitHub:**

1. Buka repository di browser: `https://github.com/USERNAME/REPO`
2. Klik tab **Actions**
3. Klik workflow run terbaru
4. Lihat setiap job dan step

**Expected: pipeline hijau (semua step pass)**

```
CI Pipeline
  ├── lint .............. ✅ (30 detik)
  └── test .............. ✅ (1 menit 20 detik)
```

**Jika pipeline gagal:** Klik job yang gagal, baca log error, perbaiki, push lagi. Ini normal — jarang sekali pipeline berhasil di percobaan pertama.

> **Troubleshooting umum:**
> - `ModuleNotFoundError`: dependency tidak ada di `requirements.txt`
> - `flake8 error`: kode melanggar style guide, perbaiki atau tambahkan exception
> - `pytest error`: test gagal di environment bersih (biasanya karena hardcoded path)

**Estimasi waktu:** 10 menit

---

### Langkah 4: Debug Pipeline yang Gagal (20 menit)

**Mengapa:** Di dunia nyata, pipeline sering gagal. Kemampuan membaca log error dan memperbaiki pipeline adalah skill DevOps yang penting.

**Latihan 4a: Sengaja gagalkan linting**

```python
# Tambahkan kode yang melanggar flake8 di app/routes.py
import os, sys, json  # E401: multiple imports on one line
x=1  # E225: missing whitespace around operator
def f( x ):  # E211: whitespace before '('
    pass
```

```bash
git add app/routes.py
git commit -m "test: sengaja gagalkan linting"
git push
```

Buka Actions tab, lihat error message dari flake8. Perhatikan format:

```
app/routes.py:1:1: E401 multiple imports on one line
app/routes.py:2:2: E225 missing whitespace around operator
```

**Latihan 4b: Sengaja gagalkan test**

```python
# Tambahkan test yang gagal di tests/test_fail.py
def test_sengaja_gagal():
    assert 1 == 2, "Test ini sengaja dibuat gagal"
```

```bash
git add tests/test_fail.py
git commit -m "test: sengaja gagalkan test"
git push
```

**Latihan 4c: Perbaiki kedua masalah**

```bash
# Perbaiki linting errors
# Hapus test yang gagal
rm tests/test_fail.py
# Perbaiki kode di app/routes.py

git add -A
git commit -m "fix: perbaiki linting errors dan hapus failing test"
git push
```

**Verifikasi: pipeline kembali hijau.**

> **Tips:** Di dunia nyata, jangan langsung push fix ke main. Buat branch, push, buat PR, pastikan pipeline hijau, baru merge.

**Estimasi waktu:** 20 menit

---

### Langkah 5: Tambah Secrets Management (15 menit)

**Mengapa:** Password, API keys, dan tokens **TIDAK BOLEH** di-hardcode dalam kode atau YAML. GitHub Secrets menyimpan data sensitif secara terenkripsi dan hanya tersedia saat pipeline berjalan.

**Langkah 5a: Tambah secret di GitHub**

1. Buka repository di GitHub
2. Settings > Secrets and variables > Actions
3. Klik "New repository secret"
4. Tambahkan:
   - Name: `RAILWAY_TOKEN`
   - Value: (token dari Railway dashboard)

**Langkah 5b: Gunakan secret di workflow**

```yaml
  deploy:
    name: Deploy to Railway
    runs-on: ubuntu-latest
    needs: test
    # Hanya deploy dari branch main (bukan PR atau develop)
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    steps:
      - name: Checkout kode
        uses: actions/checkout@v4

      - name: Install Railway CLI
        run: npm install -g @railway/cli

      - name: Deploy
        run: railway up --service perpustakaan-app
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
```

**Penjelasan:**

| Konsep | Penjelasan |
|--------|-----------|
| `${{ secrets.RAILWAY_TOKEN }}` | Mengakses secret terenkripsi |
| `if: github.ref == 'refs/heads/main'` | Hanya deploy dari main branch |
| `needs: test` | Deploy hanya jika test pass |
| `env:` | Inject secret sebagai environment variable |

**PENTING — Yang TIDAK BOLEH dilakukan:**

```yaml
# SALAH: hardcode token
env:
  RAILWAY_TOKEN: rly_abc123xyz  # JANGAN PERNAH!

# BENAR: gunakan secrets
env:
  RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
```

> **Troubleshooting:** Jika deploy gagal dengan "unauthorized", pastikan secret name persis sama (case-sensitive). Cek juga apakah token masih valid.

**Estimasi waktu:** 15 menit

---

### Langkah 6: Status Badge dan Notifikasi (10 menit)

**Mengapa:** Status badge memberikan informasi cepat tentang kesehatan proyek. Tim bisa langsung melihat apakah pipeline hijau tanpa harus membuka GitHub Actions.

**Langkah 6a: Tambah badge di README.md**

```markdown
# Perpustakaan Digital

![CI Pipeline](https://github.com/USERNAME/REPO/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-70%25-green)

Sistem manajemen perpustakaan digital untuk Universitas Al Azhar Indonesia.
```

Ganti `USERNAME` dan `REPO` dengan akun dan repository Anda.

**Langkah 6b: Verifikasi badge**

```bash
git add README.md
git commit -m "docs: tambah CI status badge di README"
git push
```

Buka README di GitHub — badge harus menampilkan status "passing" (hijau) atau "failing" (merah).

**Langkah 6c: Workflow lengkap final**

Berikut workflow lengkap yang menggabungkan semua langkah:

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  lint:
    name: Code Linting
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install flake8
      - run: flake8 app/ --max-line-length=120 --statistics

  test:
    name: Tests + Coverage
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
      - run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - run: pytest tests/ --cov=app --cov-report=term-missing -v
      - run: pytest tests/ --cov=app --cov-fail-under=70

  deploy:
    name: Deploy
    runs-on: ubuntu-latest
    needs: test
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    steps:
      - uses: actions/checkout@v4
      - run: npm install -g @railway/cli
      - run: railway up --service perpustakaan-app
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
```

**Estimasi waktu:** 10 menit

---

### Langkah 7: Pull Request Workflow (20 menit)

**Mengapa:** Di tim, kode tidak langsung di-push ke main. Developer membuat branch, push, buat PR, pipeline berjalan otomatis, tim review, baru merge. Ini adalah workflow standar industri.

```bash
# Buat feature branch
git checkout -b feature/improve-search

# Lakukan perubahan kecil (misalnya improve search function)
# ... edit kode ...

# Commit dan push
git add .
git commit -m "feat: improve search dengan partial match"
git push -u origin feature/improve-search
```

**Buat Pull Request di GitHub:**

1. Buka repository > Pull Requests > New Pull Request
2. Base: `main`, Compare: `feature/improve-search`
3. Isi judul dan deskripsi
4. Pipeline CI otomatis berjalan pada PR

**Verifikasi:**
- Di halaman PR, lihat status check di bagian bawah
- Tunggu hingga semua checks pass (hijau)
- Jika gagal, push fix ke branch yang sama — pipeline otomatis re-run

```
Merge blocked:
  ✅ lint — passed
  ✅ test — passed
  → Ready to merge!
```

> **Tips:** Aktifkan branch protection rules di Settings > Branches > Add rule:
> - Require status checks to pass before merging
> - Require pull request reviews before merging

**Estimasi waktu:** 20 menit

## Tantangan Tambahan

### Tantangan 1: Basic — Tambah Step Build Docker Image

Tambahkan job baru `build` yang membangun Docker image setelah test berhasil:
```yaml
build:
  needs: test
  steps:
    - run: docker build -t perpustakaan-app .
```

### Tantangan 2: Intermediate — Matrix Testing

Konfigurasi pipeline untuk menjalankan test di multiple Python versions (3.10, 3.11, 3.12) menggunakan strategy matrix:
```yaml
strategy:
  matrix:
    python-version: ['3.10', '3.11', '3.12']
```

### Tantangan 3: Advanced — Scheduled Security Scan

Buat workflow terpisah yang berjalan otomatis setiap hari (schedule) untuk menjalankan security scan menggunakan `pip-audit`:
```yaml
on:
  schedule:
    - cron: '0 6 * * 1'  # Setiap Senin jam 6 pagi UTC
```

## Refleksi & AI Usage Log

Setelah menyelesaikan lab ini, isi AI Usage Log jika Anda menggunakan AI tools:

| No | Task | Tool | Prompt (ringkas) | Output | Modifikasi |
|----|------|------|------------------|--------|------------|
| 1 | ... | ... | ... | ... | ... |

**Pertanyaan refleksi:**
1. Apa manfaat utama CI/CD yang Anda rasakan setelah lab ini?
2. Mengapa pipeline sering gagal di percobaan pertama? Apa pelajarannya?
3. Bagaimana CI/CD mengubah cara tim berkolaborasi?
4. Kapan sebaiknya deploy otomatis vs manual approval?

## Checklist Penyelesaian

- [ ] `.github/workflows/ci.yml` dibuat dan terpush ke GitHub
- [ ] Pipeline berjalan otomatis saat push (terlihat di Actions tab)
- [ ] Job lint berjalan dengan flake8
- [ ] Job test berjalan dengan pytest + coverage
- [ ] Pipeline caching dikonfigurasi
- [ ] Pernah debug pipeline gagal dan memperbaikinya (minimal 1x)
- [ ] Secrets dikonfigurasi (tidak ada hardcoded token)
- [ ] Status badge ditampilkan di README.md
- [ ] Refleksi dan AI Usage Log diisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
