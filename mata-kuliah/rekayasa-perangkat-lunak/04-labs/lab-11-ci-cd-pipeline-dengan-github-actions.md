# Lab 11: CI/CD Pipeline dengan GitHub Actions

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 10 dari 13 (Minggu 11) |
| **Topik** | GitHub Actions, CI Pipeline, Automated Testing |
| **CPMK** | CPMK-6 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |

## Tujuan

1. **Membuat** CI pipeline menggunakan GitHub Actions
2. **Mengkonfigurasi** automated linting dan testing
3. **Men-debug** pipeline yang gagal

## Langkah-langkah

### Langkah 1: Buat Workflow File (20 menit)
```bash
mkdir -p .github/workflows
```

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  test:
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
          pip install pytest pytest-cov flake8

      - name: Lint with flake8
        run: flake8 app/ --max-line-length=120

      - name: Run tests
        run: pytest tests/ --cov=app --cov-report=xml

      - name: Check coverage
        run: pytest tests/ --cov=app --cov-fail-under=70
```

### Langkah 2: Tambah Status Badge (10 menit)
Di README.md:
```markdown
![CI](https://github.com/USERNAME/REPO/actions/workflows/ci.yml/badge.svg)
```

### Langkah 3: Trigger Pipeline (15 menit)
```bash
git add .github/workflows/ci.yml
git commit -m "ci: tambah GitHub Actions CI pipeline"
git push
```
Buka GitHub → Actions tab → lihat pipeline berjalan.

### Langkah 4: Debug Failing Pipeline (25 menit)
Sengaja buat pipeline gagal:
1. Tambahkan kode yang melanggar flake8 → push → lihat error
2. Tambahkan test yang gagal → push → lihat error
3. Fix kedua masalah → push → pipeline hijau

### Langkah 5: Tambah Deploy Step (20 menit)
```yaml
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to Railway
        run: echo "Deploy step - configure with Railway token"
```

## Tantangan Tambahan

1. Tambahkan step untuk build Docker image di pipeline
2. Konfigurasi caching pip dependencies untuk pipeline lebih cepat

## Checklist Penyelesaian

- [ ] .github/workflows/ci.yml dibuat
- [ ] Pipeline berjalan otomatis saat push
- [ ] Lint + test steps berjalan
- [ ] Status badge di README
- [ ] Pernah debug pipeline gagal → hijau

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
