# Lab 11: CI/CD dengan GitHub Actions

## Informasi Praktikum

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Praktikum** | 10 dari 13 (Minggu 11) |
| **Topik** | GitHub Actions CI Pipeline, Automated Testing, Linting |
| **CPMK** | CPMK-6 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 10 (Integration Testing) selesai |
| **Referensi Teori** | IF2205 Minggu 11 — DevOps & CI/CD |

## Tujuan

1. **Membuat** (C6) CI pipeline menggunakan GitHub Actions workflow
2. **Mengkonfigurasi** (C3) automated linting (flake8) dan testing (pytest)
3. **Men-debug** (C4) pipeline yang gagal dan memperbaikinya
4. **Memahami** (C2) CI/CD best practices untuk proyek tim

## Konsep Singkat

### Apa Itu CI/CD?

**CI (Continuous Integration)** adalah praktik menggabungkan kode dari semua developer ke shared repository secara berkala, dengan setiap perubahan diverifikasi oleh build dan test otomatis.

**CD (Continuous Delivery/Deployment)** adalah ekstensi dari CI di mana kode yang sudah lulus test secara otomatis di-deploy ke staging atau production.

```
CI/CD Pipeline — Alur Lengkap
==============================

  Developer     Git Push      GitHub Actions         Deployment
  =========     ========      ==============         ==========

  [Code] -----> [Push] -----> [Lint] -----> [Test] -----> [Build] -----> [Deploy]
                   |             |             |             |              |
                   |          flake8        pytest       Docker         Railway
                   |             |             |             |              |
                   |          Gagal?        Gagal?       Gagal?         Gagal?
                   |           |              |             |              |
                   +---- Notifikasi ke developer: "Pipeline FAILED"
                              Perbaiki kode, push lagi

  Prinsip: Setiap push otomatis diverifikasi.
           Kode yang gagal TIDAK boleh masuk ke main.
```

### Mengapa CI/CD Penting?

| Tanpa CI/CD | Dengan CI/CD |
|-------------|-------------|
| "Works on my machine" | Diuji di environment yang sama |
| Bug ditemukan saat demo | Bug ditemukan saat push |
| Merge conflict menumpuk | Integrasi sering, conflict kecil |
| Deploy manual, rawan error | Deploy otomatis, konsisten |
| Review kode tanpa bukti test | PR harus lulus CI dulu |

### Komponen GitHub Actions

| Istilah | Penjelasan | Contoh |
|---------|-----------|--------|
| **Workflow** | File YAML yang mendefinisikan pipeline | `.github/workflows/ci.yml` |
| **Event/Trigger** | Apa yang memicu workflow | `push`, `pull_request` |
| **Job** | Sekumpulan step yang berjalan di satu runner | `lint`, `test`, `build` |
| **Step** | Satu aksi dalam job | Checkout kode, install dependencies |
| **Runner** | Server yang menjalankan job | `ubuntu-latest` |
| **Action** | Komponen reusable | `actions/checkout@v4` |

> **Referensi teori:** Lihat modul IF2205 Minggu 11 — DevOps & CI/CD untuk pembahasan mendalam tentang DevOps culture, deployment strategies, dan infrastructure as code.

## Persiapan

- Repository GitHub proyek tim sudah ada
- Test suite dari Lab 09-10 sudah berjalan lokal
- Pahami konsep YAML syntax dasar
- Pastikan semua test PASS secara lokal sebelum membuat pipeline:
  ```bash
  pytest tests/ -v --tb=short
  flake8 app/ --max-line-length=120
  ```

## Langkah-langkah

### Langkah 1: Buat Workflow File dengan Penjelasan (20 menit)

**Mengapa langkah ini penting?** Workflow file adalah "resep" yang memberitahu GitHub Actions apa yang harus dilakukan setiap kali kode di-push. Tanpa ini, tidak ada otomasi.

```bash
mkdir -p .github/workflows
```

Buat file `.github/workflows/ci.yml` — setiap baris diberi komentar penjelasan:

```yaml
# .github/workflows/ci.yml
# Nama workflow — muncul di tab Actions di GitHub
name: CI Pipeline - Perpustakaan Digital UAI

# TRIGGER: Kapan workflow ini dijalankan?
on:
  push:
    branches: [main, develop]     # Dijalankan saat push ke main atau develop
  pull_request:
    branches: [main, develop]     # Dijalankan saat PR dibuka ke main atau develop

# JOBS: Apa saja yang dijalankan?
jobs:

  # === JOB 1: LINTING ===
  # Mengapa: Memastikan kode mengikuti standar penulisan Python (PEP 8)
  lint:
    name: Code Linting (flake8)
    runs-on: ubuntu-latest        # Runner: VM Ubuntu terbaru dari GitHub
    steps:
      # Step 1: Checkout — ambil kode dari repository
      - name: Checkout repository
        uses: actions/checkout@v4

      # Step 2: Setup Python — install Python di runner
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      # Step 3: Install flake8 — linter untuk Python
      - name: Install flake8
        run: pip install flake8

      # Step 4: Jalankan flake8 — periksa semua file di folder app/
      - name: Run flake8
        run: flake8 app/ --max-line-length=120 --statistics --show-source

  # === JOB 2: TESTING ===
  # Mengapa: Memastikan semua test tetap PASS setelah perubahan kode
  test:
    name: Run Tests (pytest)
    needs: lint                    # Hanya jalan JIKA job lint berhasil
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      # Cache pip dependencies — agar build lebih cepat pada run berikutnya
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

      - name: Run unit tests
        run: pytest tests/test_models.py tests/test_routes.py -v

      - name: Run integration tests
        run: pytest tests/test_integration_peminjaman.py -v

      # Coverage check — gagalkan pipeline jika coverage < 70%
      - name: Check coverage
        run: pytest tests/ --cov=app --cov-report=xml --cov-fail-under=70

      # Upload coverage report sebagai artifact
      - name: Upload coverage report
        if: always()               # Upload meskipun step sebelumnya gagal
        uses: actions/upload-artifact@v4
        with:
          name: coverage-report
          path: coverage.xml
          retention-days: 14       # Simpan selama 14 hari

  # === JOB 3: BUILD DOCKER (opsional, untuk CD) ===
  # Mengapa: Memastikan Docker image bisa di-build tanpa error
  build:
    name: Build Docker Image
    needs: test                    # Hanya jalan JIKA test berhasil
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'   # Hanya di branch main
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t perpustakaan-app:${{ github.sha }} .

      - name: Test Docker image runs
        run: |
          docker run -d --name test-container -p 5000:5000 \
            -e SECRET_KEY=test-secret \
            -e DATABASE_URL=sqlite:///test.db \
            perpustakaan-app:${{ github.sha }}
          sleep 5
          curl -f http://localhost:5000/health || exit 1
          docker stop test-container
```

**Penjelasan dependency antar jobs:**
```
  lint ──── berhasil? ───> test ──── berhasil? ───> build
   |                        |                        |
  GAGAL                   GAGAL                    GAGAL
   |                        |                        |
  Pipeline berhenti     Pipeline berhenti       Pipeline berhenti
```

### Langkah 2: Secrets Management (10 menit)

**Mengapa langkah ini penting?** Secrets (API keys, passwords, tokens) tidak boleh hardcoded di kode atau workflow file. GitHub menyediakan encrypted secrets.

**Setup secrets di GitHub:**
1. Buka repository di GitHub
2. Settings > Secrets and variables > Actions
3. Klik "New repository secret"
4. Tambahkan secrets yang diperlukan:

| Secret Name | Contoh Value | Digunakan di |
|-------------|-------------|-------------|
| `SECRET_KEY` | `super-secret-production-key-xyz` | Konfigurasi Flask |
| `DATABASE_URL` | `postgresql://user:pass@host/db` | Koneksi database production |
| `RAILWAY_TOKEN` | `railway-token-abc123` | Deployment ke Railway |

**Cara menggunakan secrets di workflow:**
```yaml
# Di workflow file, akses secrets dengan syntax:
env:
  SECRET_KEY: ${{ secrets.SECRET_KEY }}
  DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

> **Peringatan:** JANGAN pernah print/log nilai secret. GitHub otomatis menyensor secret di log, tapi jangan coba-coba menampilkannya.

### Langkah 3: Commit, Push, dan Amati Pipeline (10 menit)

**Mengapa langkah ini penting?** Ini momen kebenaran — apakah pipeline berjalan sesuai harapan?

```bash
git add .github/workflows/ci.yml
git commit -m "ci: tambah GitHub Actions CI pipeline

- Lint dengan flake8 (max-line-length=120)
- Test dengan pytest (unit + integration)
- Coverage check (minimum 70%)
- Docker build (hanya di branch main)
- Pip caching untuk build lebih cepat"
git push
```

Buka tab **Actions** di GitHub:
1. Klik workflow run terbaru
2. Amati setiap job dan step berjalan secara real-time
3. Klik pada step yang gagal untuk melihat error detail

**Expected: pipeline hijau (semua step berhasil)**

### Langkah 4: Tambah Status Badge di README (5 menit)

**Mengapa langkah ini penting?** Status badge memberikan indikator visual langsung di halaman repository — apakah project dalam keadaan "sehat" atau tidak.

Tambahkan di awal `README.md` proyek:
```markdown
# Perpustakaan Digital UAI

![CI Pipeline](https://github.com/USERNAME/REPO/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-83%25-brightgreen)

> Sistem Perpustakaan Digital untuk Universitas Al Azhar Indonesia
```

Ganti `USERNAME/REPO` dengan username dan nama repository Anda.

**Cara mendapatkan badge URL:**
1. Buka tab Actions di GitHub
2. Klik workflow "CI Pipeline"
3. Klik tombol "..." (tiga titik) > "Create status badge"
4. Copy Markdown yang dihasilkan

### Langkah 5: Debug Failing Pipeline (25 menit)

**Mengapa langkah ini penting?** Di dunia nyata, pipeline akan sering gagal. Kemampuan men-debug pipeline sama pentingnya dengan membuatnya.

**Latihan 1 — Lint error (8 menit):**

1. Tambahkan kode yang melanggar flake8:
```python
# app/routes/buku.py — tambahkan baris ini (sengaja terlalu panjang)
def helper_function_dengan_nama_sangat_panjang_yang_melebihi_batas_120_karakter_sehingga_flake8_akan_menolaknya(parameter1, parameter2, parameter3):
    pass
```

2. Commit dan push:
```bash
git add .
git commit -m "test: sengaja tambah lint error untuk latihan debug"
git push
```

3. Buka Actions tab — amati pipeline gagal di step lint:
```
app/routes/buku.py:42:121: E501 line too long (165 > 120 characters)
1     E501 line too long
```

4. Fix dan push lagi:
```bash
# Perbaiki: potong baris atau rename fungsi
git add .
git commit -m "fix: perbaiki lint error E501 (line too long)"
git push
```

5. Amati pipeline menjadi hijau kembali.

**Latihan 2 — Test failure (8 menit):**

1. Ubah assertion di test agar gagal:
```python
# tests/test_models.py — ubah sementara
def test_create_buku(app):
    with app.app_context():
        buku = Buku(judul='Algoritma Python', pengarang='Ahmad', tahun=2025)
        db.session.add(buku)
        db.session.commit()
        assert buku.judul == 'SALAH SENGAJA'  # Ini akan gagal
```

2. Commit, push, amati pipeline gagal di step test
3. Perbaiki kembali assertion, push — pipeline hijau

**Latihan 3 — Missing dependency (9 menit):**

1. Import library baru tanpa menambahkan ke `requirements.txt`:
```python
# app/routes/buku.py
import pandas  # Library yang belum ada di requirements.txt
```

2. Push — amati error: `ModuleNotFoundError: No module named 'pandas'`
3. Tambahkan `pandas` ke `requirements.txt` (atau hapus import jika tidak perlu)
4. Push — pipeline hijau

**Pola debug pipeline:**
```
Pipeline gagal
    |
    +---> Baca error message di log
    |
    +---> Identifikasi step yang gagal (lint? test? build?)
    |
    +---> Reproduksi error secara lokal:
    |       - Lint error: jalankan `flake8 app/` lokal
    |       - Test error: jalankan `pytest tests/ -v` lokal
    |       - Build error: jalankan `docker build .` lokal
    |
    +---> Fix, commit, push, amati pipeline kembali hijau
```

### Langkah 6: Branch Protection Rules (10 menit)

**Mengapa langkah ini penting?** Branch protection memastikan kode di branch `main` selalu dalam keadaan "sehat" — tidak ada yang bisa push langsung tanpa review dan CI hijau.

Di GitHub: Settings > Branches > Add rule:

1. **Branch name pattern:** `main`
2. Centang:
   - [x] Require a pull request before merging
   - [x] Require approvals (minimal 1 reviewer)
   - [x] Require status checks to pass before merging
     - Pilih: `Run Tests (pytest)`
     - Pilih: `Code Linting (flake8)`
   - [x] Require branches to be up to date before merging

**Efeknya:**
- Push langsung ke `main` akan ditolak
- PR hanya bisa di-merge jika CI hijau DAN ada approval
- Ini mencegah kode rusak masuk ke production

### Langkah 7: PR Workflow dengan CI (10 menit)

**Mengapa langkah ini penting?** Workflow ini adalah alur sehari-hari developer: buat branch, kerjakan fitur, buka PR, tunggu CI hijau, minta review, merge.

```bash
# 1. Buat feature branch
git checkout -b feature/improve-search

# 2. Buat perubahan kecil (misalnya: tambah filter by tahun)
# Edit app/routes/buku.py dan tests/test_search.py
# ...

# 3. Commit dan push
git add .
git commit -m "feat(search): tambah filter by tahun terbit"
git push -u origin feature/improve-search

# 4. Buka GitHub -> Create Pull Request
# 5. Lihat CI pipeline berjalan di PR
# 6. Setelah CI hijau -> Request review -> Merge
```

**Di halaman PR, Anda akan melihat:**
```
Checks
------
[PASS] Code Linting (flake8)      — 15s
[PASS] Run Tests (pytest)          — 45s
[PASS] Build Docker Image          — 2m 10s

All checks have passed
[Merge pull request]
```

## Troubleshooting Pipeline yang Gagal

| Gejala di Log | Penyebab Umum | Solusi |
|--------------|--------------|-------|
| `E501 line too long` | Baris melebihi max-line-length | Potong baris atau tambahkan `# noqa: E501` (hanya jika benar-benar perlu) |
| `ModuleNotFoundError` | Package tidak ada di requirements.txt | Tambahkan package ke requirements.txt |
| `FAILED tests/...` | Test gagal — logic error | Jalankan test lokal dulu untuk debug |
| `coverage below 70%` | Test coverage turun karena kode baru tanpa test | Tulis test untuk kode baru |
| `docker build failed` | Dockerfile error (syntax, missing file) | Jalankan `docker build .` lokal |
| `rate limit exceeded` | Terlalu banyak workflow run | Tunggu beberapa menit, atau optimasi trigger |
| `Resource not accessible` | Permission issue pada GITHUB_TOKEN | Periksa Settings > Actions > General > Workflow permissions |

## Tantangan Tambahan

1. **Basic:** Tambahkan step untuk caching pip dependencies agar waktu build lebih cepat (sudah ada contohnya di workflow di atas — pastikan berfungsi)
2. **Intermediate:** Buat workflow terpisah `.github/workflows/deploy.yml` yang otomatis deploy ke Railway saat merge ke main. Gunakan `railway-token` secret
3. **Advanced:** Tambahkan notification ke Discord webhook saat pipeline gagal. Gunakan action `discord-webhook` atau `curl` ke Discord webhook URL

## Refleksi dan AI Usage Log

### Pertanyaan Refleksi
1. Bagaimana perasaan Anda saat pipeline pertama kali "hijau"? Saat pertama kali "merah"?
2. Apakah CI/CD mengubah cara Anda menulis dan mengecek kode sebelum push?
3. Bagaimana CI/CD mendukung prinsip *amanah* dalam kerja tim — memastikan setiap perubahan diverifikasi?

### Template AI Usage Log

| No | Task | AI Tool | Prompt (ringkas) | Output Quality (1-5) | Modifikasi yang Diperlukan | Waktu Hemat |
|----|------|---------|------------------|----------------------|---------------------------|-------------|
| 1 | | | | | | |
| 2 | | | | | | |

> Isi log ini dengan jujur. Penggunaan AI diperbolehkan dan didorong — yang penting adalah **transparansi** dan **evaluasi kritis** terhadap output AI.

## Checklist Penyelesaian

- [ ] `.github/workflows/ci.yml` dibuat dan valid — YAML syntax benar
- [ ] Pipeline berjalan otomatis saat push ke main/develop
- [ ] Lint step (flake8) berjalan dan mendeteksi error
- [ ] Test step (pytest) berjalan dengan unit + integration test
- [ ] Coverage check >= 70% dan report di-upload sebagai artifact
- [ ] Docker build step berjalan (di branch main)
- [ ] Status badge ditambahkan ke README
- [ ] Berhasil debug >= 2 pipeline failure dan memperbaikinya (green)
- [ ] Branch protection rule dikonfigurasi di main
- [ ] PR workflow berjalan (buat PR, CI hijau, merge)
- [ ] Secrets terkonfigurasi di GitHub repository settings
- [ ] AI Usage Log diisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
