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

## Tujuan

1. **Membuat** CI pipeline menggunakan GitHub Actions workflow
2. **Mengkonfigurasi** automated linting (flake8) dan testing (pytest)
3. **Men-debug** pipeline yang gagal dan memperbaikinya
4. **Memahami** CI/CD best practices untuk proyek tim

## Persiapan

- Repository GitHub proyek tim sudah ada
- Test suite dari Lab 09-10 sudah berjalan lokal
- Pahami konsep YAML syntax dasar

## Langkah-langkah

### Langkah 1: Buat Workflow File (20 menit)

```bash
mkdir -p .github/workflows
```

```yaml
# .github/workflows/ci.yml
name: CI Pipeline - Perpustakaan App

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

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install flake8
        run: pip install flake8

      - name: Run flake8
        run: flake8 app/ --max-line-length=120 --statistics

  test:
    name: Run Tests
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run unit tests
        run: pytest tests/test_models.py tests/test_routes.py -v

      - name: Run integration tests
        run: pytest tests/test_integration_peminjaman.py -v

      - name: Check coverage
        run: pytest tests/ --cov=app --cov-report=xml --cov-fail-under=70

      - name: Upload coverage
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: coverage-report
          path: coverage.xml
```

### Langkah 2: Commit dan Push (10 menit)

```bash
git add .github/workflows/ci.yml
git commit -m "ci: tambah GitHub Actions CI pipeline"
git push
```

Buka tab **Actions** di GitHub → lihat pipeline berjalan.

### Langkah 3: Tambah Status Badge (5 menit)

Tambahkan di `README.md` proyek:
```markdown
![CI](https://github.com/USERNAME/REPO/actions/workflows/ci.yml/badge.svg)
```

### Langkah 4: Debug Failing Pipeline (25 menit)

**Latihan 1 — Lint error:**
1. Tambahkan kode yang melanggar flake8 (line > 120 karakter)
2. Push → amati pipeline gagal di step lint
3. Fix kode → push lagi → pipeline hijau

**Latihan 2 — Test failure:**
1. Ubah assertion di salah satu test agar gagal
2. Push → amati pipeline gagal di step test
3. Fix test → push → pipeline hijau

**Latihan 3 — Missing dependency:**
1. Import library baru di `app/` tanpa menambahkan ke `requirements.txt`
2. Push → amati error
3. Tambah ke `requirements.txt` → push → pipeline hijau

### Langkah 5: Branch Protection Rules (15 menit)

Di GitHub Settings → Branches → Add rule:

1. Branch name pattern: `main`
2. ✅ Require a pull request before merging
3. ✅ Require status checks to pass before merging
   - Select: `Run Tests`
4. ✅ Require branches to be up to date

Test: buat branch baru → push → buat PR → lihat CI berjalan di PR.

### Langkah 6: PR Workflow (15 menit)

```bash
# Buat feature branch
git checkout -b feature/improve-search

# Buat perubahan kecil + test
# ...

git add .
git commit -m "feat(search): tambah filter by tahun terbit"
git push -u origin feature/improve-search

# Buka GitHub → Create Pull Request
# Lihat CI pipeline berjalan di PR
# Setelah CI hijau → Request review → Merge
```

## Tantangan Tambahan

1. Tambahkan step untuk caching pip dependencies (hemat waktu build)
2. Buat workflow terpisah untuk deployment (deploy on merge to main)
3. Tambahkan notification ke Slack/Discord saat pipeline gagal

## Checklist Penyelesaian

- [ ] `.github/workflows/ci.yml` dibuat dan valid
- [ ] Pipeline berjalan otomatis saat push
- [ ] Lint step (flake8) berjalan
- [ ] Test step (pytest) berjalan dengan coverage
- [ ] Status badge ditambahkan ke README
- [ ] Berhasil debug ≥ 1 pipeline failure → green
- [ ] Branch protection rule dikonfigurasi
- [ ] AI Usage Log diisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
