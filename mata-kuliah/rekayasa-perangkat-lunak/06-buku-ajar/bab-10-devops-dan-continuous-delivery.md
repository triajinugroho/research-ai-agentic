# BAB 10: DEVOPS DAN CONTINUOUS DELIVERY

**Oleh: Tri Aji Nugroho, S.T., M.T.**
**Mata Kuliah:** IF2205 Rekayasa Perangkat Lunak
**Program Studi Informatika — Universitas Al Azhar Indonesia**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom | Estimasi Waktu |
|-----------|-----------|-------------|----------------|
| 6.1 | Membangun CI/CD pipeline menggunakan GitHub Actions untuk otomatisasi build, test, dan deploy | C3 (Menerapkan) | 90 menit |
| 6.2 | Menerapkan containerization dengan Docker (Dockerfile, docker-compose) dan cloud deployment (Railway/Render/Vercel) | C3-C4 (Menerapkan-Menganalisis) | 60 menit |

---

## Peta Konsep Bab

```
                    ┌──────────────────────────────────┐
                    │   DEVOPS & CONTINUOUS DELIVERY    │
                    └──────────────┬───────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        ▼                          ▼                          ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  DEVOPS CULTURE  │     │  CI/CD PIPELINE  │     │ CONTAINERIZATION│
│                  │     │                  │     │  & DEPLOYMENT   │
├──────────────────┤     ├──────────────────┤     ├──────────────────┤
│ • CAMS Framework │     │ • CI: Build+Test │     │ • Docker         │
│ • DORA Metrics   │     │ • CD: Delivery   │     │ • Dockerfile     │
│ • Blameless      │     │ • CD: Deployment │     │ • docker-compose │
│   Culture        │     │ • GitHub Actions │     │ • Multi-stage    │
│ • Shift-Left     │     │   (YAML, triggers│     │ • Cloud Deploy   │
│                  │     │   jobs, secrets)  │     │   (Railway,      │
│                  │     │ • Matrix builds   │     │    Render,       │
│                  │     │                  │     │    Vercel)       │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 ▼
                    ┌──────────────────────────────┐
                    │  INFRASTRUCTURE & MONITORING  │
                    │  • IaC (Intro)               │
                    │  • Health checks             │
                    │  • Logging & Metrics          │
                    └──────────────────────────────┘
```

---

## 10.1 DevOps Culture: Lebih dari Sekadar Tools

### 10.1.1 Apa Itu DevOps?

> **DevOps** adalah kultur, gerakan, atau praktik yang menekankan kolaborasi dan komunikasi antara software developers dan IT operations professionals, sambil mengotomatisasi proses delivery software dan perubahan infrastruktur. — *The DevOps Handbook* (Kim et al., 2016)

DevOps **bukan** sebuah tools, bukan sebuah job title, dan bukan sebuah tim terpisah. DevOps adalah **cara berpikir dan bekerja** yang mengintegrasikan development dan operations.

```
┌─────────────────────────────────────────────────────────────┐
│                   SEBELUM DevOps                             │
│                                                              │
│  Development Team          │          Operations Team        │
│  ─────────────────         │          ──────────────────     │
│  "Kode sudah jadi,         │         "Deployment gagal,     │
│   tinggal deploy"          │          kodenya bermasalah!"  │
│                            │                                 │
│           ←── WALL OF CONFUSION ──→                          │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                   SESUDAH DevOps                             │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │     Development  +  Operations  =  Shared Goals       │   │
│  │                                                       │   │
│  │  "Kita bersama bertanggung jawab atas kualitas        │   │
│  │   software DAN keandalan operasionalnya"              │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 10.1.2 The Three Ways of DevOps

Menurut *The Phoenix Project* dan *The DevOps Handbook*, ada tiga prinsip fundamental:

```
┌───────────────────────────────────────────────────────────────┐
│                    THE THREE WAYS                              │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  FIRST WAY: Flow (Left to Right)                              │
│  ═══════════════════════════════                              │
│  Dev → Build → Test → Deploy → Operate                       │
│  ─────────────────────────────────→                          │
│  Optimasi alur dari development ke production.                │
│  • Small batch sizes                                          │
│  • Limit WIP                                                  │
│  • Eliminate waste                                            │
│                                                               │
│  SECOND WAY: Feedback (Right to Left)                         │
│  ════════════════════════════════════                          │
│  ←─────────────────────────────────                          │
│  Feedback cepat dari production ke development.               │
│  • Monitoring & alerting                                      │
│  • Automated testing                                          │
│  • Post-incident reviews                                      │
│                                                               │
│  THIRD WAY: Continual Experimentation & Learning              │
│  ══════════════════════════════════════════════                │
│  ←────── Belajar → Eksperimen → Improve ──────→              │
│  Kultur eksperimen, belajar dari kegagalan.                   │
│  • Blameless postmortems                                      │
│  • Allocated time for improvement                             │
│  • Innovation sprints / hack days                             │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### 10.1.3 CAMS Framework

**CAMS** (Culture, Automation, Measurement, Sharing) adalah framework untuk mengevaluasi kematangan DevOps di sebuah organisasi:

| Pilar | Deskripsi | Contoh Praktik | Anti-Pattern |
|-------|-----------|----------------|-------------|
| **Culture** | Kolaborasi, trust, shared responsibility, blameless | Dev + Ops sprint bersama, blameless postmortems, shared on-call | "Itu masalah tim Ops, bukan tanggung jawab kita" |
| **Automation** | Otomatisasi proses repetitif end-to-end | CI/CD pipeline, Infrastructure as Code, automated testing | Deploy manual via FTP, testing manual sebelum release |
| **Measurement** | Keputusan berbasis data, bukan asumsi | DORA metrics, error budgets, SLOs/SLIs, dashboards | "Sepertinya deployment kemarin aman" tanpa data |
| **Sharing** | Knowledge sharing, transparansi, dokumentasi | Tech talks, runbooks, shared dashboards, open postmortems | Knowledge silo — hanya 1 orang yang tahu cara deploy |

```python
# CAMS Maturity Assessment Tool
class CAMSAssessment:
    """Tool untuk menilai kematangan DevOps berdasarkan CAMS."""

    QUESTIONS = {
        "culture": [
            "Dev dan Ops punya shared goals dan metrics?",
            "Apakah ada blameless postmortem setelah incident?",
            "Apakah semua tim merasa bertanggung jawab atas uptime?",
            "Apakah ada feedback loop antara Dev dan Ops?",
        ],
        "automation": [
            "Apakah build dan test terotomatisasi (CI)?",
            "Apakah deployment terotomatisasi (CD)?",
            "Apakah infrastructure didefinisikan sebagai code (IaC)?",
            "Apakah monitoring dan alerting otomatis?",
        ],
        "measurement": [
            "Apakah deployment frequency diukur?",
            "Apakah lead time for changes diukur?",
            "Apakah change failure rate diukur?",
            "Apakah mean time to restore (MTTR) diukur?",
        ],
        "sharing": [
            "Apakah ada tech talks atau knowledge sharing session?",
            "Apakah runbooks dan dokumentasi up-to-date?",
            "Apakah dashboards monitoring accessible untuk semua?",
            "Apakah postmortem hasilnya dibagikan ke semua tim?",
        ],
    }

    def assess(self, responses: dict) -> dict:
        """Hitung skor per pilar (0-100%)."""
        scores = {}
        for pillar, questions in self.QUESTIONS.items():
            answered_yes = sum(1 for q in questions if responses.get(q, False))
            scores[pillar] = (answered_yes / len(questions)) * 100
        scores["overall"] = sum(scores.values()) / 4
        return scores

    def print_report(self, scores: dict):
        """Tampilkan laporan kematangan DevOps."""
        print("=" * 50)
        print("     CAMS DevOps Maturity Report")
        print("=" * 50)
        for pillar in ["culture", "automation", "measurement", "sharing"]:
            bar = "█" * int(scores[pillar] / 10)
            print(f"  {pillar.upper():<15s} [{bar:<10s}] {scores[pillar]:.0f}%")
        print("-" * 50)
        overall = scores["overall"]
        level = (
            "Expert" if overall >= 80 else
            "Advanced" if overall >= 60 else
            "Intermediate" if overall >= 40 else
            "Beginner"
        )
        print(f"  OVERALL: {overall:.0f}% — Level: {level}")


# Contoh: Asesmen tim proyek mahasiswa
assessment = CAMSAssessment()
# Tim menjawab pertanyaan (True/False)
responses = {
    "Dev dan Ops punya shared goals dan metrics?": True,
    "Apakah ada blameless postmortem setelah incident?": False,
    "Apakah semua tim merasa bertanggung jawab atas uptime?": True,
    "Apakah ada feedback loop antara Dev dan Ops?": True,
    "Apakah build dan test terotomatisasi (CI)?": True,
    "Apakah deployment terotomatisasi (CD)?": True,
    "Apakah infrastructure didefinisikan sebagai code (IaC)?": False,
    "Apakah monitoring dan alerting otomatis?": False,
    "Apakah deployment frequency diukur?": False,
    "Apakah lead time for changes diukur?": False,
    "Apakah change failure rate diukur?": False,
    "Apakah mean time to restore (MTTR) diukur?": False,
    "Apakah ada tech talks atau knowledge sharing session?": True,
    "Apakah runbooks dan dokumentasi up-to-date?": False,
    "Apakah dashboards monitoring accessible untuk semua?": False,
    "Apakah postmortem hasilnya dibagikan ke semua tim?": False,
}
scores = assessment.assess(responses)
assessment.print_report(scores)
```

### 10.1.4 DORA Metrics

**DORA** (DevOps Research and Assessment) dari Google mengidentifikasi 4 metrik kunci yang membedakan tim elite dari tim low-performer:

| Metrik | Deskripsi | Elite | High | Medium | Low |
|--------|-----------|-------|------|--------|-----|
| **Deployment Frequency** | Seberapa sering deploy ke production | On-demand (multi/hari) | 1x/minggu - 1x/bulan | 1x/bulan - 6x/bulan | 1x/6bulan |
| **Lead Time for Changes** | Dari commit sampai running di production | < 1 jam | 1 hari - 1 minggu | 1 minggu - 1 bulan | > 6 bulan |
| **Change Failure Rate** | % deployment yang menyebabkan failure | 0-15% | 16-30% | 16-30% | 46-60% |
| **Time to Restore** | Waktu recovery dari failure | < 1 jam | < 1 hari | < 1 hari | > 6 bulan |

> **Konteks Indonesia:** Tokopedia dalam berbagai tech talks menyebutkan mereka melakukan ratusan deployment per minggu untuk microservices. Bukalapak menggunakan feature flags untuk melakukan deployment tanpa risiko — fitur baru bisa diaktifkan/dinonaktifkan tanpa deployment ulang.

---

## 10.2 Continuous Integration (CI)

### 10.2.1 Konsep CI

**Continuous Integration** adalah praktik di mana developer sering merge kode ke shared repository (minimal sekali sehari), dan setiap merge memicu build dan test otomatis.

```
                     CONTINUOUS INTEGRATION PIPELINE
    ┌────────────────────────────────────────────────────────────┐
    │                                                            │
    │   Developer    Shared       Build        Test      Report  │
    │   Push     →   Repository → Server   →   Suite  →         │
    │                                                            │
    │   ┌────┐      ┌──────┐    ┌────────┐  ┌────────┐  ┌────┐  │
    │   │git │ ───→ │GitHub│ ──→│ Install │→ │ Lint   │→ │ ✓  │  │
    │   │push│      │ repo │    │ deps    │  │ Test   │  │ or │  │
    │   └────┘      └──────┘    │ Build   │  │ Cover  │  │ ✗  │  │
    │                           └────────┘  └────────┘  └────┘  │
    │                                                            │
    │   Trigger: push, pull_request, schedule                    │
    └────────────────────────────────────────────────────────────┘
```

### 10.2.2 CI Best Practices

| No | Practice | Penjelasan |
|----|----------|-----------|
| 1 | **Commit sering** | Minimal sekali sehari — small changes lebih aman |
| 2 | **Fix broken build segera** | Broken build = prioritas #1 — semua berhenti sampai fix |
| 3 | **Test otomatis** | Setiap push harus trigger automated test suite |
| 4 | **Keep build fast** | Target < 10 menit — gunakan parallelism dan caching |
| 5 | **Everyone commits** | Semua anggota tim commit ke main branch |
| 6 | **Test in clone of production** | Environment test harus mirip production |
| 7 | **Make build self-testing** | Build yang sukses = semua test pass |
| 8 | **Automate deployment** | Bukan hanya test, tapi juga deployment |

---

## 10.3 GitHub Actions: Tutorial Lengkap

### 10.3.1 Konsep Dasar GitHub Actions

```
┌─────────────────────────────────────────────────────────────┐
│                  GITHUB ACTIONS HIERARCHY                     │
│                                                              │
│  Workflow (.github/workflows/*.yml)                          │
│  └── Event (trigger: push, PR, schedule, manual)            │
│      └── Job (runs on a runner: ubuntu, windows, macos)     │
│          └── Step (individual task)                          │
│              └── Action (reusable unit: actions/checkout@v4) │
│                                                              │
│  Workflow ── 1:N ──→ Jobs ── 1:N ──→ Steps ── use ──→ Actions│
│  (YAML file)         (parallel)      (sequential)           │
└─────────────────────────────────────────────────────────────┘
```

**Konsep kunci:**
- **Workflow**: File YAML di `.github/workflows/` — mendefinisikan pipeline
- **Event**: Trigger yang memulai workflow (push, pull_request, schedule, dll.)
- **Job**: Unit eksekusi yang berjalan pada satu runner. Jobs default berjalan **paralel**
- **Step**: Langkah individual dalam job. Steps berjalan **sequential**
- **Action**: Komponen reusable (dari marketplace atau custom)
- **Runner**: Server yang menjalankan job (GitHub-hosted atau self-hosted)
- **Secret**: Variable sensitif (API keys, tokens) yang dienkripsi

### 10.3.2 Workflow YAML Syntax

```yaml
# .github/workflows/ci.yml
# ================================
# CI Pipeline untuk Flask App
# ================================

name: CI Pipeline                    # Nama workflow (tampil di GitHub UI)

# ── TRIGGERS ──────────────────────
on:
  push:
    branches: [main, develop]        # Trigger saat push ke branch ini
  pull_request:
    branches: [main, develop]        # Trigger saat PR ke branch ini
  workflow_dispatch:                  # Trigger manual dari GitHub UI

# ── ENVIRONMENT VARIABLES ─────────
env:
  PYTHON_VERSION: '3.11'
  FLASK_ENV: testing

# ── JOBS ──────────────────────────
jobs:
  # Job 1: Lint (pengecekan style)
  lint:
    name: "Lint & Format Check"
    runs-on: ubuntu-latest           # Runner: Ubuntu terbaru

    steps:
      # Step 1: Checkout kode dari repository
      - name: Checkout code
        uses: actions/checkout@v4    # Action dari marketplace

      # Step 2: Setup Python
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
          cache: 'pip'               # Cache pip packages (lebih cepat)

      # Step 3: Install dependencies
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8 black isort

      # Step 4: Cek formatting dengan Black
      - name: Check formatting (Black)
        run: black --check app/ tests/

      # Step 5: Cek import order dengan isort
      - name: Check import order (isort)
        run: isort --check-only app/ tests/

      # Step 6: Lint dengan flake8
      - name: Lint with flake8
        run: flake8 app/ tests/ --max-line-length=120 --statistics

  # Job 2: Test (berjalan paralel dengan lint)
  test:
    name: "Run Tests"
    runs-on: ubuntu-latest
    needs: lint                      # Tunggu lint selesai dulu

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
          cache: 'pip'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run tests with coverage
        run: |
          pytest tests/ \
            --cov=app \
            --cov-report=xml \
            --cov-report=term-missing \
            --verbose
        env:
          DATABASE_URL: sqlite:///test.db
          SECRET_KEY: test-secret-key-for-ci

      - name: Upload coverage report
        if: success()                # Hanya jika test pass
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml
          fail_ci_if_error: false

  # Job 3: Build Docker image
  build:
    name: "Build Docker Image"
    runs-on: ubuntu-latest
    needs: test                      # Tunggu test pass dulu

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t myapp:${{ github.sha }} .

      - name: Test Docker image
        run: |
          docker run -d -p 5000:5000 --name test-app myapp:${{ github.sha }}
          sleep 5
          curl -f http://localhost:5000/health || exit 1
          docker stop test-app
```

### 10.3.3 Triggers (Events) Lengkap

| Trigger | Kapan Dijalankan | Contoh Use Case |
|---------|-----------------|-----------------|
| `push` | Saat push ke branch tertentu | CI pada setiap commit |
| `pull_request` | Saat PR dibuat/diupdate | Review checks |
| `schedule` | Cron schedule | Nightly builds, dependency checks |
| `workflow_dispatch` | Trigger manual | Deploy manual ke production |
| `release` | Saat release dibuat | Build dan publish package |
| `workflow_call` | Dipanggil workflow lain | Reusable workflows |

```yaml
# Contoh: Multiple triggers
on:
  push:
    branches: [main]
    paths:                           # Hanya trigger jika file tertentu berubah
      - 'app/**'
      - 'tests/**'
      - 'requirements.txt'
    paths-ignore:
      - '**.md'                      # Jangan trigger untuk file markdown

  pull_request:
    types: [opened, synchronize, reopened]

  schedule:
    - cron: '0 2 * * 1'             # Setiap Senin jam 2 pagi UTC
                                     # (9 pagi WIB)
  workflow_dispatch:
    inputs:
      environment:
        description: 'Target environment'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production
```

### 10.3.4 Secrets Management

```yaml
# Cara menyimpan dan menggunakan secrets
# 1. Buka Settings → Secrets and variables → Actions → New repository secret
# 2. Tambahkan: RAILWAY_TOKEN, DATABASE_URL, SECRET_KEY, dll.

# Penggunaan dalam workflow:
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Railway
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}    # Akses secret
        run: |
          npm install -g @railway/cli
          railway up --service myapp

      - name: Notify deployment
        env:
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
        run: |
          curl -X POST $SLACK_WEBHOOK \
            -H 'Content-type: application/json' \
            -d '{"text": "Deployment sukses! Commit: ${{ github.sha }}"}'
```

> **PENTING:** JANGAN pernah hardcode secrets dalam kode atau workflow file. Selalu gunakan GitHub Secrets. File `.env` HARUS ada di `.gitignore`.

### 10.3.5 Matrix Builds

Matrix builds memungkinkan menjalankan test di berbagai kombinasi environment:

```yaml
# Test di multiple Python versions dan OS
jobs:
  test:
    name: "Test Python ${{ matrix.python-version }} on ${{ matrix.os }}"
    runs-on: ${{ matrix.os }}

    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
        os: [ubuntu-latest, windows-latest, macos-latest]
        exclude:                     # Exclude kombinasi tertentu
          - os: windows-latest
            python-version: '3.10'
      fail-fast: false               # Jangan stop semua jika 1 gagal

    steps:
      - uses: actions/checkout@v4

      - name: Setup Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install and test
        run: |
          pip install -r requirements.txt
          pip install pytest
          pytest tests/ --verbose
```

### 10.3.6 Complete CI/CD Pipeline Example

```yaml
# .github/workflows/ci-cd.yml
# ================================================
# COMPLETE CI/CD PIPELINE — Flask App + Docker
# Stages: Lint → Test → Build → Deploy Staging → Deploy Production
# ================================================

name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  PYTHON_VERSION: '3.11'
  DOCKER_IMAGE: perpustakaan-app

jobs:
  # ─── STAGE 1: LINT ────────────────────
  lint:
    name: "Stage 1: Lint"
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
          cache: pip
      - run: pip install flake8 black
      - run: black --check app/ tests/
      - run: flake8 app/ --max-line-length=120

  # ─── STAGE 2: TEST ────────────────────
  test:
    name: "Stage 2: Test"
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
          cache: pip
      - run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - run: pytest tests/ --cov=app --cov-report=xml -v
        env:
          DATABASE_URL: sqlite:///test.db
          SECRET_KEY: ci-test-key

  # ─── STAGE 3: BUILD DOCKER ────────────
  build:
    name: "Stage 3: Build Docker"
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v4
      - run: |
          docker build -t ${{ env.DOCKER_IMAGE }}:${{ github.sha }} .
          docker build -t ${{ env.DOCKER_IMAGE }}:latest .
      - name: Smoke test container
        run: |
          docker run -d -p 5000:5000 --name smoke-test \
            -e SECRET_KEY=smoke-test \
            -e DATABASE_URL=sqlite:///test.db \
            ${{ env.DOCKER_IMAGE }}:latest
          sleep 5
          curl -f http://localhost:5000/health
          docker stop smoke-test

  # ─── STAGE 4: DEPLOY STAGING ──────────
  deploy-staging:
    name: "Stage 4: Deploy Staging"
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/develop'     # Hanya dari branch develop
    environment: staging                        # GitHub Environment protection
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to Railway (Staging)
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN_STAGING }}
        run: |
          npm install -g @railway/cli
          railway up --service perpustakaan-staging

  # ─── STAGE 5: DEPLOY PRODUCTION ───────
  deploy-production:
    name: "Stage 5: Deploy Production"
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'        # Hanya dari branch main
    environment: production                     # Requires manual approval
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to Railway (Production)
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN_PROD }}
        run: |
          npm install -g @railway/cli
          railway up --service perpustakaan-prod
```

```
Pipeline Visualization:

    ┌──────┐    ┌──────┐    ┌───────┐    ┌──────────┐    ┌────────────┐
    │ LINT │───→│ TEST │───→│ BUILD │───→│ DEPLOY   │───→│ DEPLOY     │
    │      │    │      │    │DOCKER │    │ STAGING  │    │ PRODUCTION │
    └──────┘    └──────┘    └───────┘    └──────────┘    └────────────┘
                                          (develop)       (main only)
                                                          (manual
                                                           approval)

    ←── CI (Continuous Integration) ──→←── CD (Continuous Delivery) ──→
```

---

## 10.4 Docker dan Containerization

### 10.4.1 Mengapa Docker?

Permasalahan klasik dalam software engineering:

```
┌────────────────────────────────────────────────────────────────┐
│  Developer A:  "Works on my machine! Python 3.11, PostgreSQL 15│
│  Developer B:  "Di laptop saya error — Python 3.9, MySQL 8"   │
│  Server:       "Deployment gagal — dependencies tidak cocok"   │
│                                                                │
│  ════════════════════════════════════════════════════════════   │
│                                                                │
│  SOLUSI: DOCKER CONTAINER                                      │
│                                                                │
│  ┌─────────────────────────────────────────┐                   │
│  │  Container = Aplikasi + Dependencies     │                   │
│  │  + Runtime + OS Libraries                │                   │
│  │                                          │                   │
│  │  Identik di SEMUA environment:           │                   │
│  │  Dev Laptop = CI Server = Production     │                   │
│  └─────────────────────────────────────────┘                   │
└────────────────────────────────────────────────────────────────┘
```

**Container vs Virtual Machine:**

```
    VIRTUAL MACHINE                     CONTAINER
┌─────────────────────┐          ┌─────────────────────┐
│  App A  │  App B    │          │  App A  │  App B    │
├─────────┼───────────┤          ├─────────┼───────────┤
│ Bins/   │ Bins/     │          │ Bins/   │ Bins/     │
│ Libs    │ Libs      │          │ Libs    │ Libs      │
├─────────┼───────────┤          ├─────────┴───────────┤
│ Guest   │ Guest     │          │   Container Engine   │
│ OS      │ OS        │          │   (Docker)           │
├─────────┴───────────┤          ├─────────────────────┤
│    Hypervisor        │          │    Host OS           │
├─────────────────────┤          ├─────────────────────┤
│    Host OS           │          │    Hardware          │
├─────────────────────┤          └─────────────────────┘
│    Hardware          │
└─────────────────────┘          Container: lightweight
VM: heavy (GB), slow boot        (MB), fast boot (seconds)
```

| Aspek | Virtual Machine | Container |
|-------|----------------|-----------|
| Ukuran | GB | MB |
| Boot time | Menit | Detik |
| Isolasi | Sangat kuat (OS terpisah) | Proses terpisah (shared kernel) |
| Resource usage | Tinggi | Rendah |
| Portability | Baik | Sangat baik |
| Use case | Isolasi kuat, multi-OS | Microservices, CI/CD, deployment |

### 10.4.2 Docker Concepts

```
┌────────────────────────────────────────────────────────────┐
│                   DOCKER WORKFLOW                           │
│                                                             │
│  Dockerfile  ──build──→  Image  ──run──→  Container        │
│  (resep)                 (template)       (instance)        │
│                                                             │
│  Analogi:                                                   │
│  Resep kue   ──bake──→  Cetakan ──cetak──→ Kue             │
│                                                             │
│  Satu Image bisa menghasilkan banyak Container identik      │
│                                                             │
│  Registry (Docker Hub, ghcr.io):                            │
│  ┌──────────────────────────────────────┐                   │
│  │  python:3.11-slim   postgres:15      │                   │
│  │  node:20-alpine     redis:7          │                   │
│  │  nginx:latest       ubuntu:22.04     │                   │
│  └──────────────────────────────────────┘                   │
│  → Tempat menyimpan dan berbagi Images                      │
└────────────────────────────────────────────────────────────┘
```

### 10.4.3 Dockerfile: Instruksi Lengkap

```dockerfile
# ================================================
# Dockerfile untuk Flask App — Perpustakaan Digital
# ================================================

# FROM: Base image — gunakan slim untuk ukuran lebih kecil
FROM python:3.11-slim

# LABEL: Metadata image
LABEL maintainer="tim-rpl@uai.ac.id"
LABEL description="Perpustakaan Digital UAI"
LABEL version="1.0"

# ENV: Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# WORKDIR: Set working directory di dalam container
WORKDIR /app

# COPY + RUN: Install dependencies dulu (memanfaatkan Docker cache layer)
# Jika requirements.txt tidak berubah, layer ini di-cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY: Copy seluruh source code
COPY . .

# RUN: Perintah saat build (misal: collect static files)
RUN python -m compileall app/

# EXPOSE: Dokumentasi port yang digunakan (tidak publish)
EXPOSE 5000

# HEALTHCHECK: Monitoring kesehatan container
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# USER: Jalankan sebagai non-root (security best practice)
RUN adduser --disabled-password --no-create-home appuser
USER appuser

# CMD: Perintah default saat container dijalankan
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:create_app()"]
```

**Dockerfile Instructions Reference:**

| Instruksi | Fungsi | Contoh |
|-----------|--------|--------|
| `FROM` | Base image | `FROM python:3.11-slim` |
| `WORKDIR` | Set working directory | `WORKDIR /app` |
| `COPY` | Copy file dari host ke image | `COPY . .` |
| `RUN` | Jalankan perintah saat build | `RUN pip install -r requirements.txt` |
| `ENV` | Set environment variable | `ENV FLASK_ENV=production` |
| `EXPOSE` | Dokumentasi port | `EXPOSE 5000` |
| `CMD` | Perintah default saat run | `CMD ["python", "app.py"]` |
| `ENTRYPOINT` | Perintah yang tidak bisa di-override | `ENTRYPOINT ["gunicorn"]` |
| `HEALTHCHECK` | Health monitoring | `HEALTHCHECK CMD curl localhost:5000/health` |
| `USER` | Jalankan sebagai user tertentu | `USER appuser` |
| `ARG` | Build-time variable | `ARG VERSION=1.0` |
| `VOLUME` | Mount point untuk data persistent | `VOLUME /app/data` |

### 10.4.4 Multi-Stage Builds

Multi-stage build menghasilkan image yang lebih kecil dengan memisahkan tahap build dan runtime:

```dockerfile
# ================================================
# Multi-stage Dockerfile — lebih kecil, lebih aman
# ================================================

# Stage 1: Builder — install dependencies dan build
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Runtime — hanya copy yang dibutuhkan
FROM python:3.11-slim AS runtime

WORKDIR /app

# Copy installed packages dari builder
COPY --from=builder /install /usr/local

# Copy source code
COPY app/ app/
COPY migrations/ migrations/
COPY config.py .

# Security: non-root user
RUN adduser --disabled-password --no-create-home appuser
USER appuser

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]

# Hasil: image runtime JAUH lebih kecil karena
# tidak mengandung build tools dan cache
```

```python
# Perbandingan ukuran image
image_sizes = {
    "python:3.11 (full)": "1.01 GB",
    "python:3.11-slim": "153 MB",
    "python:3.11-alpine": "57 MB",
    "Single-stage (slim)": "~250 MB",
    "Multi-stage (slim)": "~180 MB",
}

print("=== Docker Image Size Comparison ===")
for image, size in image_sizes.items():
    print(f"  {image:<30s} {size}")
```

### 10.4.5 Docker Compose

Docker Compose mendefinisikan dan menjalankan **multi-container** applications:

```yaml
# docker-compose.yml
# ================================================
# Perpustakaan Digital UAI — Docker Compose
# Services: Web App + Database + Redis Cache
# ================================================

version: '3.8'

services:
  # ─── Web Application ─────────────
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://perpus_user:rahasia123@db:5432/perpustakaan
      - REDIS_URL=redis://cache:6379/0
      - SECRET_KEY=${SECRET_KEY:-dev-secret-key}
      - FLASK_ENV=${FLASK_ENV:-development}
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    volumes:
      - .:/app                      # Hot reload saat development
      - /app/__pycache__             # Exclude pycache
    restart: unless-stopped
    networks:
      - app-network

  # ─── PostgreSQL Database ──────────
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: perpus_user
      POSTGRES_PASSWORD: rahasia123
      POSTGRES_DB: perpustakaan
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data    # Persistent data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql  # Init script
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U perpus_user"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - app-network

  # ─── Redis Cache ──────────────────
  cache:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redisdata:/data
    networks:
      - app-network

# ─── Volumes (Persistent Storage) ───
volumes:
  pgdata:
    driver: local
  redisdata:
    driver: local

# ─── Networks ────────────────────────
networks:
  app-network:
    driver: bridge
```

### 10.4.6 Docker Commands Cheat Sheet

```bash
# ══════════════════════════════════════
# DOCKER COMMANDS CHEAT SHEET
# ══════════════════════════════════════

# ─── IMAGE COMMANDS ──────────────────
docker build -t perpustakaan-app .            # Build image
docker build -t perpustakaan-app:1.0 .        # Build dengan tag
docker images                                  # List semua images
docker rmi perpustakaan-app:1.0               # Hapus image

# ─── CONTAINER COMMANDS ─────────────
docker run -p 5000:5000 perpustakaan-app      # Run container
docker run -d -p 5000:5000 perpustakaan-app   # Run di background (-d)
docker run -d --name my-app \                 # Run dengan nama + env vars
  -p 5000:5000 \
  -e DATABASE_URL=sqlite:///app.db \
  -e SECRET_KEY=my-secret \
  perpustakaan-app

docker ps                                      # List running containers
docker ps -a                                   # List semua containers
docker stop my-app                             # Stop container
docker start my-app                            # Start container
docker rm my-app                               # Hapus container
docker logs my-app                             # Lihat logs
docker logs -f my-app                          # Follow logs (live)
docker exec -it my-app /bin/bash               # Masuk ke container

# ─── DOCKER COMPOSE COMMANDS ────────
docker compose up                              # Start semua services
docker compose up -d                           # Start di background
docker compose up --build                      # Rebuild sebelum start
docker compose down                            # Stop dan hapus semua
docker compose down -v                         # + hapus volumes
docker compose logs web                        # Logs service 'web'
docker compose logs -f                         # Follow all logs
docker compose ps                              # Status semua services
docker compose exec web flask db upgrade       # Run command di service

# ─── CLEANUP ─────────────────────────
docker system prune                            # Hapus unused resources
docker system prune -a                         # Hapus SEMUA unused
docker volume prune                            # Hapus unused volumes
```

---

## 10.5 Cloud Deployment

### 10.5.1 Platform Deployment untuk Proyek Kuliah

| Platform | Tipe | Free Tier | Cocok Untuk | Deployment Method |
|----------|------|-----------|-------------|-------------------|
| **Railway** | PaaS | $5/bulan credit (trial) | Flask/Node.js + DB | CLI atau GitHub auto-deploy |
| **Render** | PaaS | Static sites gratis, web service 750 jam/bulan | Portfolio, web app | GitHub auto-deploy |
| **Vercel** | Serverless | Generous (hobby) | Frontend, Next.js, API routes | GitHub auto-deploy |
| **Fly.io** | Container | 3 shared VMs, 160GB bandwidth | Docker apps | CLI (flyctl) |
| **Koyeb** | Container | 1 nano instance | Docker, microservices | GitHub atau Docker |

### 10.5.2 Railway Deployment Step-by-Step

```
┌───────────────────────────────────────────────────────────────┐
│          RAILWAY DEPLOYMENT STEPS                              │
│                                                                │
│  1. SETUP                                                      │
│     • Buat akun di railway.app                                 │
│     • Install Railway CLI: npm install -g @railway/cli         │
│     • Login: railway login                                     │
│                                                                │
│  2. CREATE PROJECT                                             │
│     • railway init (atau hubungkan GitHub repo)                │
│     • Tambah PostgreSQL service dari dashboard                 │
│     • Railway otomatis set DATABASE_URL                        │
│                                                                │
│  3. CONFIGURE                                                  │
│     • Set environment variables di dashboard:                  │
│       SECRET_KEY, FLASK_ENV=production                         │
│     • Pastikan ada Procfile atau Dockerfile                    │
│                                                                │
│  4. DEPLOY                                                     │
│     • railway up (deploy dari local)                           │
│     • ATAU hubungkan GitHub → auto-deploy saat push            │
│                                                                │
│  5. VERIFY                                                     │
│     • railway open (buka app di browser)                       │
│     • railway logs (lihat logs)                                │
│                                                                │
└───────────────────────────────────────────────────────────────┘
```

**File konfigurasi yang dibutuhkan:**

```
# Procfile — menentukan cara menjalankan app
web: gunicorn app:create_app()
```

```
# runtime.txt — menentukan versi Python
python-3.11.8
```

```python
# config.py — konfigurasi environment-aware
import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-change-in-prod')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Fix untuk PostgreSQL URL dari Railway
    # Railway memberikan postgres:// tapi SQLAlchemy butuh postgresql://
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
            'postgres://', 'postgresql://', 1
        )

class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = 'production'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


# Pilih config berdasarkan environment
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}
```

### 10.5.3 Environment Variables dan Secrets

```python
# ══════════════════════════════════════
# ENVIRONMENT VARIABLES BEST PRACTICES
# ══════════════════════════════════════

# .env (JANGAN commit ke Git — harus ada di .gitignore!)
# DATABASE_URL=postgresql://user:pass@localhost:5432/perpustakaan
# SECRET_KEY=super-secret-key-yang-sangat-panjang-dan-random
# FLASK_ENV=development
# MIDTRANS_SERVER_KEY=SB-Mid-server-xxx
# SMTP_PASSWORD=password-email

# .env.example (COMMIT ke Git — template untuk tim)
# DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
# SECRET_KEY=change-this-in-production
# FLASK_ENV=development
# MIDTRANS_SERVER_KEY=your-midtrans-key
# SMTP_PASSWORD=your-email-password
```

```python
# Cara membaca environment variables di Python
import os
from dotenv import load_dotenv

# Load dari file .env (untuk development)
load_dotenv()

# Akses environment variables
database_url = os.environ.get('DATABASE_URL')
secret_key = os.environ.get('SECRET_KEY')

# Validasi — pastikan variabel penting ada
required_vars = ['DATABASE_URL', 'SECRET_KEY']
missing = [var for var in required_vars if not os.environ.get(var)]
if missing:
    raise EnvironmentError(
        f"Missing required environment variables: {', '.join(missing)}"
    )
```

### 10.5.4 Health Check Endpoint

```python
# Health check — endpoint untuk monitoring
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/health')
def health_check():
    """Health check endpoint untuk monitoring dan load balancer."""
    health = {
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0',
        'checks': {}
    }

    # Check 1: Database connection
    try:
        db.session.execute(text('SELECT 1'))
        health['checks']['database'] = 'connected'
    except Exception as e:
        health['status'] = 'unhealthy'
        health['checks']['database'] = f'error: {str(e)}'

    # Check 2: Redis connection (jika ada)
    try:
        redis_client.ping()
        health['checks']['cache'] = 'connected'
    except Exception:
        health['checks']['cache'] = 'unavailable'

    status_code = 200 if health['status'] == 'healthy' else 503
    return jsonify(health), status_code


@app.route('/ready')
def readiness_check():
    """Readiness check — apakah app siap menerima traffic."""
    try:
        db.session.execute(text('SELECT 1'))
        return jsonify({'ready': True}), 200
    except Exception:
        return jsonify({'ready': False}), 503
```

---

## 10.6 Infrastructure as Code (Intro)

### 10.6.1 Konsep IaC

**Infrastructure as Code** (IaC) adalah praktik mengelola dan provisioning infrastruktur melalui kode (file konfigurasi) daripada melalui manual process.

```
┌────────────────────────────────────────────────────────────┐
│                   TANPA IaC                                 │
│                                                             │
│  Admin: "Saya setup server manual lewat dashboard"          │
│  • Klik-klik di UI provider                                 │
│  • Konfigurasi satu per satu                                │
│  • Tidak ada record apa yang dikonfigurasi                  │
│  • Sulit direplikasi                                        │
│  • "Snowflake servers" — setiap server unik                 │
│                                                             │
├────────────────────────────────────────────────────────────┤
│                   DENGAN IaC                                │
│                                                             │
│  Semua infrastruktur didefinisikan dalam file konfigurasi:  │
│  • Version controlled (Git)                                 │
│  • Repeatable (bisa di-apply ulang)                         │
│  • Reviewable (code review untuk infra changes)             │
│  • Auditable (history perubahan jelas)                      │
│  • Self-documenting                                         │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

**Tools IaC populer:**

| Tool | Tipe | Bahasa | Use Case |
|------|------|--------|----------|
| **Terraform** | Provisioning | HCL | Multi-cloud infrastructure |
| **Ansible** | Configuration | YAML | Server configuration |
| **Docker Compose** | Container orchestration | YAML | Multi-container apps |
| **Kubernetes** | Container orchestration | YAML | Production container orchestration |
| **Pulumi** | Provisioning | Python/JS/Go | IaC menggunakan bahasa pemrograman |

```yaml
# Contoh sederhana: docker-compose.yml ADALAH bentuk IaC
# Mendefinisikan infrastruktur lokal sebagai kode

version: '3.8'
services:
  web:
    build: .
    ports: ["5000:5000"]
    depends_on: [db, cache]

  db:
    image: postgres:15
    volumes: [pgdata:/var/lib/postgresql/data]

  cache:
    image: redis:7

volumes:
  pgdata:

# Satu perintah: docker compose up
# = 3 containers, 1 network, 1 volume — semua terdefinisi sebagai kode
```

---

## 10.7 Monitoring Basics

### 10.7.1 Mengapa Monitoring?

> "You can't improve what you don't measure." — Peter Drucker

Monitoring memberikan **visibility** ke dalam sistem yang berjalan di production. Tanpa monitoring, tim bekerja "buta" — hanya tahu ada masalah ketika user melaporkan.

### 10.7.2 Key Metrics (The Four Golden Signals)

Google SRE (Site Reliability Engineering) mendefinisikan 4 sinyal utama:

| Signal | Deskripsi | Contoh | Alert Threshold |
|--------|-----------|--------|-----------------|
| **Latency** | Waktu yang dibutuhkan untuk melayani request | Response time p99 < 500ms | > 1 detik |
| **Traffic** | Jumlah demand pada sistem | Requests per second (RPS) | Anomaly detection |
| **Errors** | Rate of requests yang gagal | 5xx error rate < 1% | > 5% |
| **Saturation** | Seberapa "penuh" resource sistem | CPU > 80%, Memory > 90% | > 85% |

### 10.7.3 Logging Best Practices

```python
# Structured logging — lebih baik dari print()
import logging
import json
from datetime import datetime

# Setup logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
logger = logging.getLogger(__name__)


# BURUK: print() untuk logging
def process_order_bad(order_id):
    print(f"Processing order {order_id}")     # Tidak ada level
    print(f"Order {order_id} done")           # Tidak terstruktur


# BAIK: Structured logging
def process_order_good(order_id: str, customer_id: str):
    """Proses order dengan structured logging."""
    logger.info(
        "Processing order",
        extra={
            "order_id": order_id,
            "customer_id": customer_id,
            "action": "order_processing_started",
        }
    )

    try:
        # ... proses order ...
        logger.info(
            "Order processed successfully",
            extra={
                "order_id": order_id,
                "action": "order_processing_completed",
                "duration_ms": 150,
            }
        )
    except Exception as e:
        logger.error(
            "Order processing failed",
            extra={
                "order_id": order_id,
                "action": "order_processing_failed",
                "error": str(e),
            },
            exc_info=True  # Include traceback
        )
        raise


# Log levels:
# DEBUG    → Detail untuk debugging (jangan di production)
# INFO     → Event normal (request processed, user logged in)
# WARNING  → Situasi tidak ideal tapi masih berjalan
# ERROR    → Error yang perlu perhatian
# CRITICAL → Sistem down atau data corruption
```

### 10.7.4 Application Monitoring Setup

```python
# Simple monitoring middleware untuk Flask
from functools import wraps
import time

# In-memory metrics (untuk demo — di production gunakan Prometheus/Datadog)
metrics = {
    "total_requests": 0,
    "error_count": 0,
    "total_response_time": 0.0,
}

def track_request(f):
    """Decorator untuk tracking metrics per endpoint."""
    @wraps(f)
    def decorated(*args, **kwargs):
        start_time = time.time()
        metrics["total_requests"] += 1

        try:
            response = f(*args, **kwargs)
            return response
        except Exception as e:
            metrics["error_count"] += 1
            raise
        finally:
            duration = (time.time() - start_time) * 1000  # ms
            metrics["total_response_time"] += duration

    return decorated


@app.route('/metrics')
def get_metrics():
    """Endpoint untuk expose metrics."""
    total = metrics["total_requests"] or 1
    return jsonify({
        "total_requests": metrics["total_requests"],
        "error_count": metrics["error_count"],
        "error_rate": f"{(metrics['error_count'] / total) * 100:.2f}%",
        "avg_response_time_ms": f"{metrics['total_response_time'] / total:.2f}",
    })


# Penggunaan
@app.route('/books')
@track_request
def list_books():
    return jsonify(book_service.get_all())
```

---

## Studi Kasus Komprehensif: Membangun CI/CD Pipeline untuk Proyek Perpustakaan Digital

### Konteks
Tim proyek RPL (4 orang) membangun "Perpustakaan Digital UAI" menggunakan Flask + PostgreSQL. Mereka perlu setup CI/CD pipeline dari nol.

### Langkah 1: Struktur Proyek

```
perpustakaan-digital/
├── .github/
│   └── workflows/
│       └── ci-cd.yml           # GitHub Actions pipeline
├── app/
│   ├── __init__.py             # Flask app factory
│   ├── models.py               # SQLAlchemy models
│   ├── routes/
│   │   ├── books.py
│   │   └── auth.py
│   └── services/
│       └── book_service.py
├── tests/
│   ├── conftest.py
│   ├── test_books.py
│   └── test_auth.py
├── migrations/                  # Flask-Migrate
├── Dockerfile
├── docker-compose.yml
├── Procfile                     # Untuk Railway
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### Langkah 2: .gitignore yang Lengkap

```
# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.eggs/
venv/
.venv/

# Environment
.env
.env.local
.env.production

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Testing
.coverage
htmlcov/
coverage.xml
.pytest_cache/

# Docker
*.log
```

### Langkah 3: Pipeline Configuration

```yaml
# .github/workflows/ci-cd.yml
name: Perpustakaan Digital CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: pip
      - run: pip install flake8 black
      - run: black --check app/ tests/
      - run: flake8 app/ --max-line-length=120

  test:
    needs: quality
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_USER: test_user
          POSTGRES_PASSWORD: test_pass
          POSTGRES_DB: test_perpustakaan
        ports: ['5432:5432']
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: pip
      - run: pip install -r requirements.txt && pip install pytest pytest-cov
      - run: pytest tests/ --cov=app --cov-report=xml -v
        env:
          DATABASE_URL: postgresql://test_user:test_pass@localhost:5432/test_perpustakaan
          SECRET_KEY: test-secret-key

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install -g @railway/cli
      - run: railway up --service perpustakaan-prod
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
```

### Langkah 4: Dockerize

```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN adduser --disabled-password appuser && chown -R appuser /app
USER appuser
EXPOSE 5000
HEALTHCHECK --interval=30s CMD curl -f http://localhost:5000/health || exit 1
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:create_app()"]
```

### Hasil Akhir
- Setiap push ke `develop` → lint + test otomatis
- Setiap PR ke `main` → lint + test + build check
- Setiap merge ke `main` → automatic deployment ke Railway
- Tim bisa fokus menulis kode, bukan manual deployment

> **Lesson:** Pipeline CI/CD investasi waktu di awal (2-4 jam setup), tetapi menghemat puluhan jam selama proyek berjalan. Bug ditemukan lebih cepat, deployment konsisten, dan tim lebih percaya diri melakukan perubahan.

---

## AI Corner: AI untuk DevOps (Level: Advanced)

### 10.AI.1 AI untuk Menulis GitHub Actions Workflow

**Prompt:**
```
Buatkan GitHub Actions workflow untuk Flask app dengan:
- Python 3.11
- Lint (flake8 + black)
- Test (pytest dengan coverage > 80%)
- Build Docker image
- Deploy ke Railway (hanya dari branch main)
- PostgreSQL service container untuk testing
Gunakan caching untuk pip. Jelaskan setiap bagian.
```

**Evaluasi:**
- Apakah workflow syntax benar? (Jalankan di repo test)
- Apakah secrets di-handle dengan benar? (Bukan hardcoded)
- Apakah job dependencies benar? (needs: sesuai urutan)

### 10.AI.2 AI untuk Menulis Dockerfile

**Prompt:**
```
Buatkan multi-stage Dockerfile untuk Flask app yang:
- Menggunakan python:3.11-slim sebagai base
- Menginstall dependencies dari requirements.txt
- Menjalankan sebagai non-root user
- Memiliki healthcheck
- Ukuran image seminimal mungkin
Jelaskan setiap instruksi dan best practice yang diterapkan.
```

**Evaluasi:**
- Apakah layer ordering optimal? (dependencies sebelum source code)
- Apakah ada security best practices? (non-root, no cache)
- Apakah multi-stage benar-benar mengurangi size?

### 10.AI.3 AI untuk Debug CI/CD Errors

**Prompt:**
```
GitHub Actions saya gagal di step ini. Berikut error log-nya:

[error log di sini]

Apa penyebabnya dan bagaimana cara fix?
Berikan solusi spesifik yang bisa langsung saya terapkan.
```

**Tips:** AI sangat baik untuk debugging CI errors karena error messages biasanya cukup deskriptif dan pattern-based.

### 10.AI.4 AI untuk Optimasi Docker

**Prompt:**
```
Analisis Dockerfile berikut dan berikan saran optimasi untuk:
1. Mengurangi ukuran image
2. Meningkatkan build speed (layer caching)
3. Meningkatkan security
4. Menambahkan best practices yang hilang

[paste Dockerfile]
```

### 10.AI.5 AI untuk Generate docker-compose.yml

**Prompt:**
```
Buatkan docker-compose.yml untuk development environment:
- Flask web app (build dari Dockerfile)
- PostgreSQL 15 dengan data persistent
- Redis 7 untuk caching
- pgAdmin untuk database management
- Network terpisah
- Health checks untuk semua services
```

### 10.AI.6 Batasan AI dalam DevOps

| AI Bisa | AI Tidak Bisa |
|---------|--------------|
| Generate workflow YAML | Mengetahui secrets dan credentials Anda |
| Debug CI error messages | Memahami infrastruktur production Anda sepenuhnya |
| Optimize Dockerfile | Menjamin keamanan deployment |
| Suggest monitoring setup | Menggantikan understanding of your system |
| Generate docker-compose | Test apakah pipeline benar-benar berjalan |

> **Peringatan Etis:** Saat menggunakan AI untuk generate CI/CD configurations, JANGAN pernah share secrets, API keys, atau credentials dalam prompt. AI provider bisa menyimpan conversation history. Gunakan placeholder seperti `${{ secrets.MY_SECRET }}` dalam prompt.

---

## Latihan Soal

### Level Dasar (C1-C2)

1. Jelaskan perbedaan Continuous Integration, Continuous Delivery, dan Continuous Deployment.
2. Sebutkan dan jelaskan 4 pilar CAMS framework dalam DevOps.
3. Apa keuntungan menggunakan Docker dibandingkan instalasi langsung di server? Sebutkan minimal 4 keuntungan.
4. Jelaskan hierarki GitHub Actions: Workflow → Event → Job → Step → Action.
5. Apa itu multi-stage build dalam Docker dan mengapa penting?

### Level Menengah (C3-C4)

6. Buatlah GitHub Actions workflow file (YAML) yang melakukan:
   - Lint dengan flake8
   - Test dengan pytest dan coverage report
   - Build Docker image
   - Deploy ke staging (hanya dari branch `develop`)
   Sertakan penjelasan setiap bagian.

7. Tulis Dockerfile dan docker-compose.yml untuk Flask app yang terhubung ke PostgreSQL dan Redis. Pastikan:
   - Multi-stage build
   - Non-root user
   - Health check
   - Persistent data untuk database

8. Analisis: Mengapa prinsip "infrastructure as code" penting? Bandingkan setup manual vs IaC untuk skenario: tim Anda perlu membuat environment staging yang identik dengan production.

9. Sebuah tim memiliki DORA metrics berikut:
   - Deployment Frequency: 1x per bulan
   - Lead Time: 2 minggu
   - Change Failure Rate: 30%
   - MTTR: 3 hari
   Klasifikasikan level tim ini dan berikan 3 rekomendasi improvement.

10. Jelaskan mengapa environment variables TIDAK boleh di-hardcode dalam kode dan TIDAK boleh di-commit ke Git. Berikan contoh bagaimana seharusnya mengelola secrets di development, CI/CD, dan production.

### Level Mahir (C5-C6)

11. Rancang CI/CD pipeline lengkap untuk aplikasi e-commerce tim Anda — dari developer push hingga running di production. Gambarkan pipeline stages, tools yang digunakan, dan strategy untuk zero-downtime deployment.

12. Evaluasi: Railway vs Render vs Vercel untuk proyek kuliah web app (Flask + PostgreSQL + Redis). Pertimbangkan: free tier limitations, ease of setup, Docker support, database support, auto-deploy dari GitHub.

13. Sebuah startup Indonesia memiliki 20 microservices yang masing-masing perlu CI/CD pipeline. Rancang strategi untuk:
    - Shared/reusable workflow templates
    - Centralized secrets management
    - Monitoring dan alerting
    - Rollback strategy

14. Analisis kritis: "Docker menyelesaikan semua masalah deployment." Setujukah? Diskusikan situasi di mana Docker bukan solusi terbaik dan alternatifnya.

15. Rancang monitoring dan alerting strategy untuk proyek kuliah yang sudah di-deploy. Tentukan: metrics apa yang diukur, threshold alert, tools yang digunakan, dan runbook untuk 3 skenario failure yang umum.

---

## Rangkuman

1. **DevOps** adalah kultur kolaborasi antara Development dan Operations yang bertujuan memperpendek siklus delivery sambil menjaga kualitas. CAMS framework (Culture, Automation, Measurement, Sharing) adalah alat evaluasi kematangan DevOps.
2. **Three Ways of DevOps**: Flow (optimasi alur Dev → Ops), Feedback (feedback cepat Ops → Dev), dan Continual Learning (kultur eksperimen dan perbaikan berkelanjutan).
3. **DORA Metrics** (Deployment Frequency, Lead Time, Change Failure Rate, MTTR) adalah standar industri untuk mengukur performa DevOps. Tim elite deploy on-demand dengan lead time < 1 jam.
4. **Continuous Integration (CI)** memastikan setiap commit di-build dan di-test otomatis. Best practices: commit sering, fix broken build segera, keep build fast (< 10 menit).
5. **GitHub Actions** adalah platform CI/CD terintegrasi di GitHub. Komponen utama: Workflow (YAML), Events (triggers), Jobs (paralel), Steps (sequential), Actions (reusable), Secrets (encrypted variables).
6. **Docker** mengisolasi aplikasi dalam container — memastikan environment identik dari development sampai production. Dockerfile mendefinisikan image, docker-compose mendefinisikan multi-container setup.
7. **Multi-stage builds** menghasilkan Docker image yang lebih kecil dengan memisahkan tahap build (install dependencies, compile) dan runtime (hanya binary yang dibutuhkan).
8. **Cloud deployment** (Railway, Render, Vercel) memudahkan deployment proyek kuliah. Pastikan: environment variables aman, health check endpoint tersedia, dan auto-deploy terhubung ke GitHub.
9. **Infrastructure as Code** (IaC) mendefinisikan infrastruktur sebagai file konfigurasi yang version controlled, repeatable, dan reviewable. Docker Compose adalah bentuk IaC untuk development environment.
10. **Monitoring** memberikan visibility ke dalam sistem production. Four Golden Signals: Latency, Traffic, Errors, Saturation. Gunakan structured logging dan expose metrics endpoint.

---

## Referensi

1. Kim, G., Humble, J., Debois, P., & Willis, J. (2016). *The DevOps Handbook: How to Create World-Class Agility, Reliability, & Security in Technology Organizations*. IT Revolution Press.
2. Humble, J. & Farley, D. (2010). *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*. Addison-Wesley.
3. Docker Documentation. (2025). *Docker Docs*. docs.docker.com.
4. GitHub. (2025). *GitHub Actions Documentation*. docs.github.com/en/actions.
5. Forsgren, N., Humble, J., & Kim, G. (2018). *Accelerate: The Science of Lean Software and DevOps*. IT Revolution Press.
6. Kim, G., Behr, K., & Spafford, G. (2013). *The Phoenix Project: A Novel about IT, DevOps, and Helping Your Business Win*. IT Revolution Press.
7. Beyer, B., Jones, C., Petoff, J., & Murphy, N. R. (2016). *Site Reliability Engineering: How Google Runs Production Systems*. O'Reilly.
8. Railway Documentation. (2025). *Railway Docs*. docs.railway.app.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
