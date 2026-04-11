# Minggu 11: DevOps, CI/CD, dan Deployment

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 11 dari 16 |
| **Topik** | DevOps, CI/CD, dan Deployment |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **Bahasa Pemrograman** | Python 3.x + JavaScript |
| **CPMK** | CPMK-6: Menerapkan praktik DevOps, CI/CD pipeline (GitHub Actions), containerization (Docker), cloud deployment, serta memahami software maintenance dan evolusi |
| **Sub-CPMK** | Sub-CPMK-6.1: Membangun CI/CD pipeline menggunakan GitHub Actions untuk otomatisasi build, test, dan deploy (C3) |
| | Sub-CPMK-6.2: Menerapkan containerization dengan Docker (Dockerfile, docker-compose) dan cloud deployment (C3) |
| **Durasi** | 150 menit (3 x 50 menit) |
| **Metode** | Ceramah interaktif, live demo CI/CD pipeline, hands-on GitHub Actions dan Docker |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menganalisis** budaya DevOps (CAMS: Culture, Automation, Measurement, Sharing) dan perbedaannya dengan model tradisional silo (C4)
2. **Menjelaskan** perbedaan Continuous Integration, Continuous Delivery, dan Continuous Deployment beserta trade-off masing-masing (C2)
3. **Menerapkan** GitHub Actions workflow lengkap untuk automated linting, testing, dan deployment (C3)
4. **Menerapkan** Docker: menulis Dockerfile dan docker-compose untuk containerization aplikasi Flask (C3)
5. **Mengevaluasi** opsi cloud deployment (Railway, Vercel, Render) dan memilih yang sesuai untuk proyek (C5)
6. **Menganalisis** deployment strategies (Big Bang, Rolling, Blue-Green, Canary) dan memilih strategi yang tepat berdasarkan konteks (C4)

---

## Materi Pembelajaran

### 11.1 DevOps: Budaya dan Prinsip

DevOps adalah **budaya dan praktik** yang menyatukan pengembangan (*Development*) dan operasional (*Operations*) untuk mempercepat delivery perangkat lunak berkualitas tinggi secara berkelanjutan. Istilah ini pertama kali dipopulerkan pada konferensi "DevOps Days" di Ghent, Belgia (2009) oleh Patrick Debois.

```
Model Tradisional (Silo) -- "Lempar ke Seberang Tembok"
┌──────────────┐     "Kode sudah     ┌──────────────┐
│              │      selesai, nih"   │              │
│  Development │────────────────────▶│  Operations  │
│              │                      │              │
│ "Kami coding │     "Kenapa error    │ "Kami deploy │
│  saja"       │◀─── di server?"     │  & jaga"     │
└──────────────┘                      └──────────────┘
    Masalah: Lambat, saling menyalahkan, feedback terlambat

Model DevOps -- Kolaborasi Berkelanjutan
┌────────────────────────────────────────────────────────┐
│                                                        │
│    Plan ──▶ Code ──▶ Build ──▶ Test ──▶ Release       │
│      ▲                                     │           │
│      │         CI/CD Pipeline              │           │
│      │         (Otomatis!)                 ▼           │
│    Learn ◀── Monitor ◀── Operate ◀── Deploy           │
│                                                        │
│     Dev ◀════ Tanggung jawab bersama ════▶ Ops         │
└────────────────────────────────────────────────────────┘
    Solusi: Cepat, kolaboratif, feedback cepat
```

**Analogi sederhana:**
- **Tanpa DevOps**: Seperti restoran di mana koki dan pelayan tidak pernah berkomunikasi. Koki memasak apa yang dia mau, pelayan bingung menjelaskan ke pelanggan.
- **Dengan DevOps**: Koki dan pelayan berkoordinasi terus-menerus, menu disesuaikan dengan feedback pelanggan, proses diperbaiki bersama.

#### CAMS -- Empat Pilar DevOps

| Pilar | Deskripsi | Contoh Praktik | Contoh di Indonesia |
|-------|-----------|----------------|---------------------|
| **Culture** | Kolaborasi tanpa silo, shared responsibility | Blameless postmortem, shared on-call | Gojek: post-incident review tanpa menyalahkan |
| **Automation** | Otomasi proses manual yang berulang | CI/CD pipeline, Infrastructure as Code | Tokopedia: auto-deploy 100+ service/hari |
| **Measurement** | Ukur kinerja dengan data | DORA metrics, error budget | Traveloka: monitoring SLA 99.9% |
| **Sharing** | Berbagi pengetahuan antar tim | Documentation, tech talks, retrospective | Bukalapak: engineering blog publik |

```
Visualisasi CAMS Framework:
┌──────────────────────────────────────────┐
│              CULTURE                      │
│   "Kita satu tim, bukan dua silo"        │
│                                          │
│  ┌────────────┐    ┌────────────────┐    │
│  │ AUTOMATION │    │  MEASUREMENT   │    │
│  │ CI/CD,     │◀──▶│ DORA metrics,  │    │
│  │ IaC, Test  │    │ error budget   │    │
│  └─────┬──────┘    └───────┬────────┘    │
│        │                   │             │
│        └───────┬───────────┘             │
│                ▼                         │
│          ┌──────────┐                    │
│          │ SHARING  │                    │
│          │ Docs,    │                    │
│          │ Retro,   │                    │
│          │ Blog     │                    │
│          └──────────┘                    │
└──────────────────────────────────────────┘
```

#### DORA Metrics -- Mengukur Kinerja DevOps

DORA (DevOps Research and Assessment) mengidentifikasi **4 key metrics** yang membedakan tim elite dari tim berkinerja rendah:

```
DORA Metrics -- 4 Indikator Utama:
┌────────────────────────┬──────────────┬──────────────┬──────────────┐
│ Metrik                 │ Elite        │ Medium       │ Low          │
├────────────────────────┼──────────────┼──────────────┼──────────────┤
│ Deployment Frequency   │ Multiple/hari│ 1x/minggu    │ 1x per bulan │
│ Lead Time for Change   │ < 1 jam      │ 1 minggu     │ > 6 bulan    │
│ Change Failure Rate    │ 0-15%        │ 16-30%       │ 46-60%       │
│ Time to Restore (MTTR) │ < 1 jam      │ < 1 hari     │ > 6 bulan    │
└────────────────────────┴──────────────┴──────────────┴──────────────┘

Target untuk proyek kelompok IF2205:
├── Deployment Frequency: Min. 1x per sprint
├── Lead Time: < 1 hari (push to deploy)
├── Change Failure Rate: < 30%
└── Time to Restore: < 4 jam
```

#### DevOps vs Traditional vs Agile

| Aspek | Traditional | Agile | DevOps |
|-------|------------|-------|--------|
| **Siklus rilis** | 6-12 bulan | 2-4 minggu | Setiap saat |
| **Feedback** | Setelah deploy | Per sprint | Terus-menerus |
| **Tim** | Terpisah (Dev vs Ops) | Dev terorganisir | Dev + Ops terpadu |
| **Testing** | Manual, akhir siklus | Otomatis, per sprint | Otomatis, setiap commit |
| **Deployment** | Manual, penuh risiko | Semi-otomatis | Fully automated |
| **Monitoring** | Reaktif | Proaktif | Proaktif + Self-healing |

**Konteks Indonesia:**
- **Gojek/GoTo**: Tim DevOps ~50 orang yang mengelola 1000+ microservices. Setiap engineer bertanggung jawab dari kode sampai production monitoring.
- **Tokopedia**: Menerapkan "You Build It, You Run It" -- developer yang menulis kode juga yang jaga saat terjadi insiden di production.
- **Bank BCA**: Transisi bertahap dari model tradisional ke DevOps untuk sistem core banking, dengan tetap menjaga compliance regulasi OJK.

### 11.2 CI/CD -- Continuous Integration & Continuous Delivery

```
┌────────────────────────────────────────────────────────────────┐
│                    CI/CD Pipeline Flow                          │
│                                                                │
│  Developer    Git Push    Auto Build    Auto Test    Feedback  │
│  ┌──────┐    ┌──────┐    ┌──────┐     ┌──────┐    ┌──────┐  │
│  │ Code │──▶│ Push │──▶│ Build│──▶  │ Test │──▶│Pass/ │  │
│  │      │    │      │    │& Lint│     │(unit,│    │Fail  │  │
│  └──────┘    └──────┘    └──────┘     │integ)│    └──┬───┘  │
│                                       └──────┘       │       │
│                                                      ▼       │
│  ┌────────────────────────────────────────────────────┐      │
│  │ Jika PASS:                                         │      │
│  │   CI ─── selesai (merge aman)                      │      │
│  │   CD (Delivery) ─── deploy ke staging ─ manual ──▶ prod  │
│  │   CD (Deployment) ── deploy otomatis ke production │      │
│  └────────────────────────────────────────────────────┘      │
└────────────────────────────────────────────────────────────────┘
```

#### Perbedaan CI, CD (Delivery), dan CD (Deployment)

| Aspek | CI | CD (Delivery) | CD (Deployment) |
|-------|-----|----------------|-----------------|
| **Build otomatis** | Ya | Ya | Ya |
| **Test otomatis** | Ya | Ya | Ya |
| **Deploy ke staging** | -- | Ya | Ya |
| **Deploy ke production** | -- | Manual trigger | Otomatis |
| **Risiko** | Rendah | Sedang | Tinggi (butuh test matang) |
| **Cocok untuk** | Semua proyek | Proyek medium | Proyek mature |
| **Contoh** | Startup baru | Tokopedia | Gojek microservices |

```python
# Ilustrasi konsep CI/CD dengan Python script sederhana
# File: scripts/ci_check.py

import subprocess
import sys

def run_linting():
    """Langkah 1: Cek kualitas kode dengan flake8."""
    print("=== STEP 1: Linting ===")
    result = subprocess.run(
        ["flake8", "src/", "--max-line-length=120"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"LINT GAGAL:\n{result.stdout}")
        return False
    print("Linting PASSED")
    return True

def run_tests():
    """Langkah 2: Jalankan unit test."""
    print("=== STEP 2: Testing ===")
    result = subprocess.run(
        ["pytest", "--cov=src", "-v", "--tb=short"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"TEST GAGAL:\n{result.stdout}")
        return False
    print("Tests PASSED")
    return True

def build_docker():
    """Langkah 3: Build Docker image."""
    print("=== STEP 3: Docker Build ===")
    result = subprocess.run(
        ["docker", "build", "-t", "toko-umkm:latest", "."],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"BUILD GAGAL:\n{result.stderr}")
        return False
    print("Docker build PASSED")
    return True

if __name__ == "__main__":
    steps = [run_linting, run_tests, build_docker]
    for step in steps:
        if not step():
            print("\nPIPELINE GAGAL! Perbaiki error di atas.")
            sys.exit(1)
    print("\nSEMUA TAHAP BERHASIL! Siap deploy.")
```

**Contoh di Indonesia:**
- **Gojek**: Continuous Deployment untuk microservice -- ratusan deploy per hari
- **Tokopedia**: Continuous Delivery -- deploy ke staging otomatis, manual approval ke production
- **Dana (e-wallet)**: CI wajib untuk semua pull request, termasuk security scan
- **UMKM/Startup awal**: CI saja sudah cukup -- auto test di setiap push

### 11.3 GitHub Actions -- CI/CD dalam Praktik

GitHub Actions menggunakan file **YAML** di `.github/workflows/` untuk mendefinisikan pipeline otomatis. Ini adalah platform CI/CD yang paling populer di kalangan developer open-source.

#### Anatomi GitHub Actions Workflow

```
Struktur file .github/workflows/ci.yml:

Workflow (1 file YAML)
├── name: Nama pipeline
├── on: Trigger (kapan dijalankan?)
│   ├── push ke branch tertentu
│   ├── pull_request
│   └── schedule (cron)
└── jobs: Kumpulan pekerjaan
    ├── job-1: lint-and-test
    │   ├── runs-on: OS runner (ubuntu-latest)
    │   └── steps: Langkah-langkah
    │       ├── uses: actions/checkout@v4     # Clone repo
    │       ├── uses: actions/setup-python@v5 # Setup Python
    │       └── run: pytest --cov             # Jalankan perintah
    └── job-2: deploy
        ├── needs: [job-1]  <- Tunggu job-1 selesai
        └── steps: ...
```

```
Konsep Kunci GitHub Actions:
┌─────────────────────────────────────────────────────┐
│                     WORKFLOW                         │
│  (1 file YAML = 1 workflow)                          │
│                                                     │
│  ┌──────────────────┐  ┌──────────────────┐        │
│  │      JOB 1       │  │      JOB 2       │        │
│  │  (runs parallel) │  │  (runs parallel) │        │
│  │                  │  │                  │        │
│  │  Step 1: Checkout│  │  Step 1: Checkout│        │
│  │  Step 2: Setup   │  │  Step 2: Setup   │        │
│  │  Step 3: Install │  │  Step 3: Install │        │
│  │  Step 4: Lint    │  │  Step 4: Test    │        │
│  │  Step 5: Test    │  │                  │        │
│  └────────┬─────────┘  └────────┬─────────┘        │
│           └──────────┬──────────┘                   │
│                      ▼                              │
│           ┌──────────────────┐                      │
│           │      JOB 3       │                      │
│           │  needs: [1, 2]   │                      │
│           │  Deploy          │                      │
│           └──────────────────┘                      │
└─────────────────────────────────────────────────────┘
```

#### Workflow Lengkap: CI Pipeline untuk Proyek Flask + React

```yaml
# .github/workflows/ci.yml -- CI Pipeline Lengkap
name: CI Pipeline - Toko UMKM

# Kapan pipeline dijalankan?
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

# Kumpulan jobs
jobs:
  # ===== JOB 1: Lint & Test Backend (Python/Flask) =====
  test-backend:
    name: Backend - Lint & Test
    runs-on: ubuntu-latest

    steps:
      # Langkah 1: Checkout kode dari repository
      - name: Checkout repository
        uses: actions/checkout@v4

      # Langkah 2: Setup Python
      - name: Setup Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'  # Cache pip dependencies

      # Langkah 3: Install dependencies
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov flake8

      # Langkah 4: Linting dengan flake8
      - name: Lint dengan flake8
        run: |
          flake8 src/ --max-line-length=120 --statistics

      # Langkah 5: Jalankan unit test dengan coverage
      - name: Jalankan pytest dengan coverage
        run: |
          pytest --cov=src --cov-report=xml --cov-report=term-missing -v

      # Langkah 6: Upload coverage report
      - name: Upload coverage ke Codecov
        uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          file: ./coverage.xml

  # ===== JOB 2: Lint & Test Frontend (JavaScript/React) =====
  test-frontend:
    name: Frontend - Lint & Test
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js 20
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
          cache-dependency-path: frontend/package-lock.json

      - name: Install dependencies
        working-directory: frontend
        run: npm ci

      - name: Lint dengan ESLint
        working-directory: frontend
        run: npx eslint src/ --max-warnings=0

      - name: Jalankan Jest test
        working-directory: frontend
        run: npm test -- --coverage --watchAll=false

  # ===== JOB 3: Build Docker Image =====
  build-docker:
    name: Build Docker Image
    needs: [test-backend, test-frontend]  # Tunggu test selesai
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'   # Hanya di branch main

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Build Docker image
        run: |
          docker build -t toko-umkm:${{ github.sha }} .
          echo "Docker image berhasil di-build!"

  # ===== JOB 4: Deploy ke Railway =====
  deploy:
    name: Deploy ke Railway
    needs: [build-docker]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Deploy ke Railway
        uses: bervProject/railway-deploy@main
        with:
          railway_token: ${{ secrets.RAILWAY_TOKEN }}
          service: toko-umkm
```

#### Penjelasan Konsep YAML Penting

```yaml
# === SECRETS: Menyimpan data sensitif ===
# Jangan PERNAH hardcode token/password di YAML!
# Set di: GitHub repo -> Settings -> Secrets -> Actions
${{ secrets.RAILWAY_TOKEN }}    # Token deploy
${{ secrets.CODECOV_TOKEN }}    # Token coverage

# === CONDITIONAL: Kapan job dijalankan ===
if: github.ref == 'refs/heads/main'  # Hanya di branch main
if: github.event_name == 'push'      # Hanya saat push

# === NEEDS: Urutan eksekusi ===
needs: [test-backend, test-frontend]  # Tunggu kedua job selesai

# === CACHE: Percepat pipeline ===
cache: 'pip'   # Cache Python packages
cache: 'npm'   # Cache Node.js packages
```

```
Visualisasi Pipeline Execution:
┌───────────────────┐   ┌────────────────────┐
│ test-backend      │   │ test-frontend       │
│ (Python/Flask)    │   │ (JavaScript/React)  │
│ ~2 menit          │   │ ~3 menit            │
└────────┬──────────┘   └────────┬────────────┘
         │                       │
         └───────────┬───────────┘
                     │ (kedua job harus lulus)
              ┌──────▼──────┐
              │build-docker │
              │ ~1 menit    │
              └──────┬──────┘
                     │
              ┌──────▼──────┐
              │  deploy     │
              │ (Railway)   │
              │ ~2 menit    │
              └─────────────┘

Total: ~5 menit dari push ke live! (dibanding manual: 30+ menit)
```

#### Workflow Tambahan: Auto-label PR berdasarkan File yang Diubah

```yaml
# .github/workflows/labeler.yml
name: PR Labeler

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  label:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/labeler@v5
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
          # Config di .github/labeler.yml
```

```yaml
# .github/labeler.yml -- aturan labeling
backend:
  - 'src/**'
  - 'requirements.txt'

frontend:
  - 'frontend/**'
  - 'package.json'

docs:
  - '**/*.md'

ci:
  - '.github/**'
```

#### Status Badge -- Tampilkan Status Pipeline di README

```markdown
<!-- Tambahkan di README.md proyek -->
![CI Pipeline](https://github.com/username/toko-umkm/actions/workflows/ci.yml/badge.svg)

<!-- Hasilnya: badge hijau (passing) atau merah (failing) -->
```

### 11.4 Docker -- Containerization

Docker mengemas aplikasi beserta **semua dependensinya** ke dalam container yang portabel dan konsisten di semua environment.

```
Masalah Tanpa Docker -- "Works on My Machine"
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Laptop Dev 1 │   │ Laptop Dev 2 │   │ Server Prod  │
│ Python 3.11  │   │ Python 3.9   │   │ Python 3.8   │
│ pip v24      │   │ pip v22      │   │ pip v21      │
│ lib v2.0     │   │ lib v1.8     │   │ lib v1.5     │
│   JALAN OK   │   │   ERROR!     │   │   ERROR!     │
└──────────────┘   └──────────────┘   └──────────────┘
"Di laptop saya jalan kok..."

Solusi dengan Docker:
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Laptop Dev 1 │   │ Laptop Dev 2 │   │ Server Prod  │
│ ┌──────────┐ │   │ ┌──────────┐ │   │ ┌──────────┐ │
│ │Container │ │   │ │Container │ │   │ │Container │ │
│ │Python3.11│ │   │ │Python3.11│ │   │ │Python3.11│ │
│ │lib v2.0  │ │   │ │lib v2.0  │ │   │ │lib v2.0  │ │
│ │ JALAN OK │ │   │ │ JALAN OK │ │   │ │ JALAN OK │ │
│ └──────────┘ │   │ └──────────┘ │   │ └──────────┘ │
└──────────────┘   └──────────────┘   └──────────────┘
"Jalan di mana saja, dijamin sama!"
```

#### Container vs Virtual Machine (VM)

```
Virtual Machine:                    Container:
┌─────────────────────┐            ┌─────────────────────┐
│  App A   │  App B   │            │  App A   │  App B   │
│  Libs A  │  Libs B  │            │  Libs A  │  Libs B  │
│  Guest   │  Guest   │            │          │          │
│  OS      │  OS      │            │  (TANPA Guest OS)   │
│ (1-2 GB) │ (1-2 GB) │            │  (hanya MB)         │
├──────────┴──────────┤            ├─────────────────────┤
│    Hypervisor       │            │   Docker Engine     │
├─────────────────────┤            ├─────────────────────┤
│    Host OS          │            │    Host OS          │
└─────────────────────┘            └─────────────────────┘
Berat (GB), lambat start           Ringan (MB), start < 1 detik
```

| Aspek | Virtual Machine | Container (Docker) |
|-------|----------------|-------------------|
| **Ukuran** | GB (termasuk Guest OS) | MB (hanya app + libs) |
| **Startup** | Menit | Detik |
| **Isolasi** | Penuh (OS terpisah) | Process-level |
| **Overhead** | Besar | Minimal |
| **Cocok untuk** | Multi-OS, legacy app | Microservices, CI/CD |

#### Konsep Dasar Docker

```
Docker Architecture:
┌─────────────────────────────────────────────┐
│                Docker Host                   │
│                                             │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │Container│  │Container│  │Container│    │
│  │(Flask)  │  │(React)  │  │(Postgres│    │
│  │Port 5000│  │Port 3000│  │Port 5432│    │
│  └────┬────┘  └────┬────┘  └────┬────┘    │
│       │            │            │           │
│  ┌────▼────────────▼────────────▼────┐     │
│  │        Docker Engine              │     │
│  └───────────────────────────────────┘     │
│                                             │
│  ┌───────────────────────────────────┐     │
│  │   Docker Images (template)        │     │
│  │   python:3.11-slim, postgres:15   │     │
│  └───────────────────────────────────┘     │
└─────────────────────────────────────────────┘

Image vs Container:
├── Image  = Resep masakan (template, read-only)
├── Container = Masakan jadi (instance, running)
└── Dari 1 image, bisa buat banyak container
```

#### Dockerfile -- Resep untuk Build Image

```dockerfile
# Dockerfile untuk aplikasi Flask (Toko UMKM)
# Setiap baris = 1 layer dalam image

# 1. Base image: Python 3.11 (versi slim = lebih kecil)
FROM python:3.11-slim

# 2. Set working directory di dalam container
WORKDIR /app

# 3. Salin file requirements DULU (untuk caching layer)
COPY requirements.txt .

# 4. Install dependencies Python
RUN pip install --no-cache-dir -r requirements.txt

# 5. Salin seluruh kode aplikasi
COPY . .

# 6. Expose port yang digunakan Flask
EXPOSE 5000

# 7. Environment variable
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# 8. Perintah untuk menjalankan aplikasi
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

#### Multi-Stage Build -- Optimasi Ukuran Image

```dockerfile
# Multi-stage build: 2 stage
# Stage 1: Build (install semua tools)
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Production (hanya hasil build)
FROM python:3.11-slim AS production

WORKDIR /app

# Salin hanya packages yang sudah diinstall
COPY --from=builder /install /usr/local

COPY . .

# Buat non-root user untuk keamanan
RUN useradd --create-home appuser
USER appuser

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

```
Perbandingan ukuran image:
┌─────────────────────┬──────────┐
│ Pendekatan          │ Ukuran   │
├─────────────────────┼──────────┤
│ python:3.11         │ ~920 MB  │
│ python:3.11-slim    │ ~130 MB  │
│ Multi-stage + slim  │ ~95 MB   │
└─────────────────────┴──────────┘
```

```bash
# Perintah Docker yang sering digunakan
$ docker build -t toko-umkm:latest .     # Build image
$ docker run -p 5000:5000 toko-umkm      # Jalankan container
$ docker images                           # Lihat semua image
$ docker ps                               # Container yang berjalan
$ docker ps -a                            # Semua container
$ docker logs <container_id>              # Lihat log
$ docker stop <container_id>              # Hentikan container
$ docker rm <container_id>                # Hapus container
$ docker rmi <image_id>                   # Hapus image
$ docker exec -it <id> bash               # Masuk ke container
```

#### Docker Compose -- Orkestrasi Multi-Container

Untuk aplikasi yang terdiri dari beberapa service (web + database + cache), gunakan Docker Compose:

```yaml
# docker-compose.yml untuk Toko UMKM
version: '3.8'

services:
  # === Service 1: Aplikasi Flask ===
  web:
    build: .                          # Build dari Dockerfile di folder ini
    ports:
      - "5000:5000"                   # Expose port
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/toko_umkm
      - SECRET_KEY=${SECRET_KEY}      # Ambil dari .env file
      - FLASK_ENV=development
    volumes:
      - .:/app                        # Mount kode lokal (hot-reload)
    depends_on:
      - db                            # Tunggu database siap
    restart: unless-stopped

  # === Service 2: Database PostgreSQL ===
  db:
    image: postgres:15                # Gunakan image resmi
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: toko_umkm
    volumes:
      - pgdata:/var/lib/postgresql/data  # Persist data
    ports:
      - "5432:5432"

  # === Service 3: Redis (opsional, untuk caching) ===
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

# Named volumes untuk persistensi data
volumes:
  pgdata:
```

```bash
# Perintah Docker Compose
$ docker-compose up -d            # Jalankan semua services (background)
$ docker-compose ps               # Status semua services
$ docker-compose logs -f          # Lihat log (follow mode)
$ docker-compose logs web         # Log service tertentu
$ docker-compose exec web bash    # Masuk ke container web
$ docker-compose down             # Hentikan semua services
$ docker-compose down -v          # Hentikan + hapus volumes (HATI-HATI!)
$ docker-compose build --no-cache # Rebuild tanpa cache
```

```
Visualisasi Docker Compose Network:
┌──────────────────────────────────────────────┐
│            docker-compose.yml                │
│                                              │
│  ┌──────────┐  ┌───────────┐  ┌──────────┐ │
│  │  web      │  │  db        │  │  redis   │ │
│  │ (Flask)   │──│ (Postgres) │  │ (Cache)  │ │
│  │ :5000     │  │ :5432      │  │ :6379    │ │
│  └──────────┘  └───────────┘  └──────────┘ │
│       │              │              │        │
│  ┌────▼──────────────▼──────────────▼───┐   │
│  │      Docker Network (bridge)         │   │
│  │  Service saling terhubung via nama   │   │
│  │  web bisa akses db via "db:5432"     │   │
│  │  web bisa akses redis via "redis"    │   │
│  └──────────────────────────────────────┘   │
└──────────────────────────────────────────────┘
```

#### .dockerignore -- File yang Tidak Perlu di-Copy

```
# .dockerignore
__pycache__/
*.pyc
.env
.git/
.github/
node_modules/
*.md
tests/
.pytest_cache/
.coverage
.vscode/
```

### 11.5 Cloud Deployment

Setelah aplikasi ter-containerize, langkah berikutnya adalah deploy ke cloud agar bisa diakses publik.

| Platform | Tipe | Kelebihan | Kekurangan | Cocok Untuk |
|----------|------|-----------|------------|-------------|
| **Railway** | PaaS | Full-stack, DB included, Docker support | Free tier terbatas ($5/bulan) | Backend + DB (Flask + PostgreSQL) |
| **Vercel** | PaaS | Auto-deploy, CDN global, gratis | Hanya frontend/serverless | Frontend (React, Next.js) |
| **Render** | PaaS | Simple, free tier, auto-deploy | Cold start lambat (30 detik) | API, static sites |
| **Fly.io** | PaaS | Edge deployment, Docker-native | Setup lebih kompleks | Docker containers |
| **GitHub Pages** | Static | Gratis, terintegrasi GitHub | Hanya static files | Dokumentasi, landing page |

#### Deploy ke Railway -- Step by Step

```
Alur Deploy ke Railway:
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ 1. Push ke   │──▶│ 2. Railway   │──▶│ 3. App Live  │
│ GitHub main  │    │ auto-build   │    │ di URL publik│
│              │    │ & deploy     │    │              │
└──────────────┘    └──────────────┘    └──────────────┘

Cara Setup:
1. Buat akun di railway.app (login via GitHub)
2. New Project -> Deploy from GitHub Repo
3. Connect GitHub repository
4. Set environment variables (DATABASE_URL, SECRET_KEY, dll.)
5. Railway auto-detect Dockerfile atau Procfile
6. Setiap push ke main -> auto-deploy!
```

```bash
# Alternatif: Deploy via Railway CLI
$ npm install -g @railway/cli
$ railway login
$ railway link           # Link ke project
$ railway up             # Deploy!
$ railway logs           # Lihat logs
$ railway variables      # Lihat environment variables
```

```python
# Contoh Procfile untuk Railway (tanpa Docker)
# File: Procfile
# web: gunicorn app:app --bind 0.0.0.0:$PORT

# Contoh config runtime.txt
# File: runtime.txt
# python-3.11.8

# Pastikan environment variable PORT digunakan
import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
```

### 11.6 Deployment Strategies

```
Deployment Strategies Comparison:
┌──────────────────────────────────────────────────────┐
│                                                      │
│ 1. Big Bang (sekaligus)     2. Rolling Update        │
│ ┌─────┐    ┌─────┐         ┌─────┐ ┌─────┐         │
│ │v1.0 │ -> │v2.0 │         │v1.0 │ │v2.0 │ (pelan) │
│ │v1.0 │    │v2.0 │         │v1.0 │ │v2.0 │         │
│ │v1.0 │    │v2.0 │         │v1.0 │ │v1.0 │         │
│ └─────┘    └─────┘         └─────┘ └─────┘         │
│ Risiko: TINGGI              Risiko: SEDANG           │
│                                                      │
│ 3. Blue-Green               4. Canary                │
│ ┌─────┐ ┌─────┐            ┌─────┐                  │
│ │BLUE │ │GREEN│            │v2.0 │ 10% traffic      │
│ │v1.0 │ │v2.0 │            │v1.0 │ 90% traffic      │
│ └──┬──┘ └──┬──┘            └─────┘                  │
│    └─switch─┘              Jika OK -> rollout 100%   │
│ Risiko: RENDAH             Risiko: RENDAH            │
└──────────────────────────────────────────────────────┘
```

| Strategy | Deskripsi | Downtime? | Rollback | Biaya Infra | Cocok Untuk |
|----------|-----------|-----------|----------|-------------|-------------|
| **Big Bang** | Ganti semua sekaligus | Ya | Sulit | Rendah | Proyek kecil, startup awal |
| **Rolling** | Ganti satu per satu | Tidak | Sedang | Rendah | Proyek medium |
| **Blue-Green** | Dua environment, switch traffic | Tidak | Mudah | Tinggi (2x) | Proyek besar |
| **Canary** | Kirim % kecil ke versi baru | Tidak | Mudah | Sedang | Proyek kritis |

**Konteks Indonesia:**
- **Gojek**: Canary deployment -- fitur baru dirilis ke 5% pengguna di Jakarta dulu, baru rollout nasional
- **Tokopedia**: Blue-green deployment untuk fitur e-commerce kritis (checkout, pembayaran)
- **Dana**: Rolling update untuk layanan e-wallet -- zero downtime karena regulasi BI
- **Startup awal**: Big bang cukup -- downtime beberapa menit masih acceptable

```python
# Simulasi canary deployment check
def canary_health_check(canary_metrics: dict, threshold: dict) -> str:
    """
    Evaluasi apakah canary deployment aman untuk full rollout.
    
    Args:
        canary_metrics: metrik dari canary instance
        threshold: batas yang diizinkan
    
    Returns:
        "ROLLOUT" jika aman, "ROLLBACK" jika bermasalah
    """
    # Cek error rate
    if canary_metrics["error_rate"] > threshold["max_error_rate"]:
        return "ROLLBACK"
    
    # Cek latency (waktu respons)
    if canary_metrics["p99_latency_ms"] > threshold["max_latency_ms"]:
        return "ROLLBACK"
    
    # Cek throughput tidak turun drastis
    if canary_metrics["requests_per_sec"] < threshold["min_rps"]:
        return "ROLLBACK"
    
    return "ROLLOUT"

# Contoh penggunaan
canary = {
    "error_rate": 0.02,        # 2% error
    "p99_latency_ms": 250,     # 250ms
    "requests_per_sec": 1000   # 1000 req/s
}

batas = {
    "max_error_rate": 0.05,    # Maks 5% error
    "max_latency_ms": 500,     # Maks 500ms
    "min_rps": 800             # Min 800 req/s
}

keputusan = canary_health_check(canary, batas)
print(f"Keputusan: {keputusan}")  # Output: ROLLOUT
```

### 11.7 Monitoring dan Observability

Setelah deploy, kita perlu memantau kesehatan aplikasi:

```
Three Pillars of Observability:
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│    LOGS      │  │   METRICS    │  │   TRACES     │
│              │  │              │  │              │
│ "Apa yang    │  │ "Berapa      │  │ "Bagaimana   │
│  terjadi?"   │  │  angkanya?"  │  │  alurnya?"   │
│              │  │              │  │              │
│ Contoh:      │  │ Contoh:      │  │ Contoh:      │
│ Error log,   │  │ CPU usage,   │  │ Request flow │
│ Access log   │  │ Response time│  │ antar service│
└──────────────┘  └──────────────┘  └──────────────┘
```

```python
# Contoh: Health check endpoint untuk monitoring
from flask import Flask, jsonify
import psutil
import datetime

app = Flask(__name__)

@app.route("/health")
def health_check():
    """Endpoint untuk monitoring tools (uptime check)."""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "1.2.0",
        "checks": {
            "database": cek_koneksi_db(),
            "disk_space": f"{psutil.disk_usage('/').percent}%",
            "memory": f"{psutil.virtual_memory().percent}%"
        }
    }), 200

def cek_koneksi_db():
    """Cek apakah database bisa diakses."""
    try:
        # db.session.execute("SELECT 1")
        return "connected"
    except Exception:
        return "disconnected"
```

> **Nilai Islami -- Tadarruj (Bertahap):** Dalam Islam, perubahan yang bertahap lebih diutamakan daripada perubahan drastis sekaligus. Deployment strategy seperti canary dan rolling update sejalan dengan prinsip *tadarruj* -- memperkenalkan perubahan secara bertahap untuk meminimalkan risiko. Rasulullah SAW bersabda: "Sesungguhnya Allah menyukai jika salah seorang di antara kalian mengerjakan suatu pekerjaan, ia menyempurnakannya" (HR. Al-Baihaqi) -- ini mendorong kita untuk melakukan deployment dengan hati-hati dan terukur.

---

## Kegiatan Pembelajaran

### Pre-class (20 menit)

- Buat akun Railway ([railway.app](https://railway.app/)) -- gratis dengan login GitHub
- Pastikan Docker tersedia di GitHub Codespaces (sudah pre-installed): `docker --version`
- Install GitHub CLI: `gh auth login` (untuk melihat workflow status dari terminal)
- Baca: "What is DevOps?" dari Atlassian ([atlassian.com/devops](https://www.atlassian.com/devops))
- Jalankan di terminal Codespaces:
  ```bash
  docker run hello-world  # Verifikasi Docker berjalan
  gh workflow list        # Lihat workflow yang ada
  ```

### In-class (110 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-20 menit | Konsep DevOps (CAMS, DORA metrics), perbedaan CI/CD/CD, konteks Indonesia | Ceramah + diskusi |
| 20-45 menit | Live demo: buat GitHub Actions workflow dari scratch (YAML walkthrough step-by-step) | Live coding |
| 45-50 menit | *Break* | -- |
| 50-70 menit | Docker basics: Dockerfile + multi-stage build + docker-compose demo | Demo + hands-on |
| 70-95 menit | Hands-on: setup CI/CD pipeline untuk proyek kelompok, commit workflow YAML | Hands-on |
| 95-110 menit | Cloud deployment overview (Railway) + deployment strategies + monitoring + Q&A | Ceramah + diskusi |

### Post-class (20 menit)

- Lengkapi CI/CD setup untuk repository proyek kelompok (file `.github/workflows/ci.yml`)
- Tambahkan GitHub Actions status badge ke README proyek
- Coba deploy proyek ke Railway (ikuti panduan di materi 11.5)
- Tambahkan health check endpoint (`/health`) ke aplikasi Flask
- Mulai kerjakan tugas T5

---

## Latihan & Diskusi

### Soal 1 (C2 -- Memahami)
Jelaskan perbedaan antara Continuous Integration, Continuous Delivery, dan Continuous Deployment. Untuk proyek akhir kelompok Anda (tim 3-4 orang, 3 bulan), mana yang paling tepat dan mengapa? Kaitkan jawaban Anda dengan DORA metrics.

### Soal 2 (C3 -- Menerapkan)
Tulis GitHub Actions workflow (YAML) untuk proyek Node.js yang melakukan:
1. Checkout repository
2. Setup Node.js 20
3. Install dependencies dengan `npm ci`
4. Jalankan ESLint
5. Jalankan Jest test dengan coverage
6. Deploy ke Vercel (hanya jika push ke branch `main`)

Sertakan penggunaan cache dan secrets yang tepat.

### Soal 3 (C4 -- Menganalisis)
Perhatikan Dockerfile berikut:

```dockerfile
FROM python:3.11
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

Identifikasi minimal 5 masalah atau area improvement pada Dockerfile ini. Tulis ulang Dockerfile yang sudah diperbaiki dengan multi-stage build dan jelaskan alasan setiap perubahan.

### Soal 4 (C4 -- Menganalisis)
Sebuah startup fintech di Jakarta memiliki 500.000 pengguna aktif dan ingin melakukan update besar pada sistem pembayaran. Analisis deployment strategy mana yang paling tepat (Big Bang, Rolling, Blue-Green, atau Canary). Pertimbangkan: risiko downtime, kemudahan rollback, biaya infrastruktur, dan regulasi OJK terkait layanan keuangan.

### Soal 5 (C5 -- Mengevaluasi)
Tim Anda memiliki CI pipeline yang memakan waktu 15 menit untuk setiap run. Developer mengeluh feedback terlalu lambat. Evaluasi langkah-langkah berikut untuk mempercepat pipeline dan urutkan berdasarkan impact:
a) Cache dependencies (pip/npm)
b) Run lint dan test secara paralel (separate jobs)
c) Pisahkan test unit (cepat) dari test E2E (lambat) -- trigger E2E hanya di `main`
d) Gunakan runner yang lebih powerful (larger runner)
e) Skip test untuk perubahan dokumentasi saja (path filter)

Berikan estimasi penghematan waktu untuk setiap strategi.

---

## Penugasan

### T5 -- CI/CD Pipeline Configuration

| Komponen | Detail |
|----------|--------|
| **Tipe** | Kelompok (3-4 orang) |
| **Bobot** | 2.5% dari nilai akhir |
| **Deadline** | Minggu 13 |
| **Deliverable** | 1) File `.github/workflows/ci.yml`, 2) `Dockerfile`, 3) `docker-compose.yml`, 4) Dokumentasi `docs/ci-cd.md` |
| **CPMK** | CPMK-6 |

**Instruksi:**
1. Buat **GitHub Actions workflow** yang mencakup:
   - Install dependencies (Python dan/atau Node.js)
   - Jalankan linting (flake8/ESLint)
   - Jalankan test suite (pytest/Jest) dengan coverage
   - Build Docker image
2. Buat **Dockerfile** untuk aplikasi proyek kelompok (gunakan multi-stage build)
3. Buat **docker-compose.yml** yang mencakup minimal: web app + database
4. Tambahkan **health check endpoint** (`/health`) ke aplikasi
5. (Bonus) Deploy ke Railway/Vercel dan tunjukkan URL live
6. Dokumentasikan pipeline dalam `docs/ci-cd.md` -- sertakan screenshot pipeline hijau (passing)

**Kriteria Penilaian:**

| Kriteria | Bobot |
|----------|-------|
| GitHub Actions workflow berjalan (green) | 30% |
| Dockerfile best practices (multi-stage, slim image, non-root user) | 20% |
| Docker Compose bisa `docker-compose up` berhasil | 20% |
| Dokumentasi pipeline jelas dan lengkap | 15% |
| Bonus: Live deployment URL + health check endpoint | 15% |

---

## Referensi

1. Humble, J. & Farley, D. (2010). *Continuous Delivery*. Addison-Wesley.
2. Kim, G., Humble, J., Debois, P. & Willis, J. (2016). *The DevOps Handbook*. IT Revolution Press.
3. GitHub Actions documentation. [docs.github.com/actions](https://docs.github.com/en/actions)
4. Docker documentation. [docs.docker.com](https://docs.docker.com/)
5. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering*, 9th ed. McGraw-Hill. Chapter 29.
6. Railway documentation. [docs.railway.app](https://docs.railway.app/)
7. Forsgren, N., Humble, J. & Kim, G. (2018). *Accelerate: The Science of Lean Software and DevOps*. IT Revolution.
8. Docker Compose documentation. [docs.docker.com/compose](https://docs.docker.com/compose/)
9. Sommerville, I. (2016). *Software Engineering*, 10th ed. Pearson. Chapter 25.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
