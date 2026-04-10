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
| **CPMK** | CPMK-6: Menerapkan DevOps, CI/CD, containerization (Docker), cloud deployment, dan software maintenance |
| **Sub-CPMK** | 11.1 Menganalisis prinsip DevOps dan manfaatnya dalam siklus pengembangan (C4) |
| | 11.2 Menerapkan CI/CD pipeline menggunakan GitHub Actions (C4) |
| | 11.3 Mengevaluasi strategi containerization dan cloud deployment (C5) |
| **Durasi** | 150 menit (3 × 50 menit) |
| **Metode** | Ceramah interaktif, live demo CI/CD pipeline, hands-on GitHub Actions |

---

## Tujuan Pembelajaran

Setelah menyelesaikan modul ini, mahasiswa diharapkan mampu:

1. **Menganalisis** budaya DevOps (CAMS: Culture, Automation, Measurement, Sharing) dan perbedaannya dengan model tradisional (C4)
2. **Menjelaskan** konsep Continuous Integration, Continuous Delivery, dan Continuous Deployment (C2)
3. **Menerapkan** GitHub Actions workflow untuk automated testing dan deployment (C4)
4. **Menerapkan** Docker dasar: Dockerfile dan docker-compose untuk containerization (C4)
5. **Mengevaluasi** opsi cloud deployment (Vercel, Railway) untuk proyek web application (C5)

---

## Materi Pembelajaran

### 11.1 DevOps: Budaya dan Prinsip

DevOps adalah **budaya dan praktik** yang menyatukan pengembangan (*Development*) dan operasional (*Operations*) untuk mempercepat delivery perangkat lunak berkualitas.

```
Model Tradisional (Silo):
┌──────────┐    "Lempar ke    ┌──────────┐
│   Dev    │───seberang───▶│   Ops    │
│ "Kode    │    tembok"     │ "Deploy  │
│  selesai"│                │  & jaga" │
└──────────┘                └──────────┘
     ❌ Lambat, saling menyalahkan

Model DevOps:
┌────────────────────────────────────────┐
│     Dev ←──── Kolaborasi ────▶ Ops     │
│  Plan → Code → Build → Test → Deploy  │
│    ▲         CI/CD Pipeline        │   │
│    └───── Monitor → Feedback ──────┘   │
└────────────────────────────────────────┘
     ✓ Cepat, tanggung jawab bersama
```

#### CAMS — Pilar DevOps

| Pilar | Deskripsi | Contoh Praktik |
|-------|-----------|----------------|
| **Culture** | Kolaborasi, tanpa silo | Shared responsibility, blameless postmortem |
| **Automation** | Otomasi proses manual | CI/CD, Infrastructure as Code |
| **Measurement** | Ukur kinerja | DORA metrics, deployment frequency |
| **Sharing** | Berbagi pengetahuan | Documentation, retrospective |

### 11.2 CI/CD — Continuous Integration & Continuous Delivery

```
Continuous Integration (CI):
  Developer push → Auto build → Auto test → Feedback
  "Setiap push ke repository memicu build & test otomatis"

Continuous Delivery (CD):
  CI + Auto deploy ke staging → Manual approval → Production
  "Kode selalu siap di-deploy kapan saja"

Continuous Deployment:
  CI + Auto deploy langsung ke production
  "Setiap perubahan yang lolos test langsung live"
```

| Aspek | CI | CD (Delivery) | CD (Deployment) |
|-------|-----|----------------|-----------------|
| **Build otomatis** | ✓ | ✓ | ✓ |
| **Test otomatis** | ✓ | ✓ | ✓ |
| **Deploy staging** | — | ✓ | ✓ |
| **Deploy production** | — | Manual | Otomatis |
| **Risiko** | Rendah | Sedang | Tinggi (butuh test matang) |

### 11.3 GitHub Actions — CI/CD dalam Praktik

GitHub Actions menggunakan file **YAML** di `.github/workflows/` untuk mendefinisikan pipeline:

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test-backend:
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

      - name: Jalankan unit test
        run: pytest --cov=src --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v4

  test-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install & test
        run: |
          npm ci
          npm test -- --coverage

  deploy:
    needs: [test-backend, test-frontend]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - name: Deploy ke Railway
        run: echo "Deploy ke production..."
        # Railway/Vercel deploy command di sini
```

#### Anatomi GitHub Actions Workflow

```
Workflow (.yml)
├── name: Nama pipeline
├── on: Trigger (push, pull_request, schedule)
└── jobs:
    ├── job-1:
    │   ├── runs-on: OS runner
    │   └── steps:
    │       ├── uses: Action dari marketplace
    │       └── run: Perintah shell
    └── job-2:
        └── needs: [job-1]  ← dependency
```

### 11.4 Docker Basics — Containerization

Docker mengemas aplikasi beserta dependensinya ke dalam **container** yang portabel.

```
Tanpa Docker:                    Dengan Docker:
"Di laptop saya jalan kok..."    "Jalan di mana saja!"
┌─────────┐  ┌─────────┐       ┌───────────────────┐
│ Dev PC   │  │ Server  │       │  Container        │
│ Python   │  │ Python  │       │ ┌───────────────┐ │
│  3.11    │  │  3.9    │       │ │ App + Python  │ │
│ lib v2   │  │ lib v1  │       │ │ 3.11 + lib v2 │ │
│  ❌ Beda │  │  ❌     │       │ └───────────────┘ │
└─────────┘  └─────────┘       └───────────────────┘
```

#### Dockerfile

```dockerfile
# Dockerfile untuk aplikasi Flask
FROM python:3.11-slim

WORKDIR /app

# Salin dan install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin kode aplikasi
COPY . .

# Expose port
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "app.py"]
```

#### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

### 11.5 Cloud Deployment

| Platform | Kelebihan | Cocok Untuk |
|----------|-----------|-------------|
| **Vercel** | Deploy otomatis, gratis untuk hobby | Frontend (Next.js, React) |
| **Railway** | Full-stack, database included | Backend + DB |
| **Render** | Simple, free tier | API, static sites |
| **Fly.io** | Edge deployment, Docker-native | Docker containers |

> **Konteks Indonesia:** Startup lokal seperti Gojek dan Tokopedia menggunakan praktik DevOps intensif. Gojek memproses jutaan transaksi per hari dengan ratusan microservice yang di-deploy secara otomatis melalui CI/CD pipeline.

---

## Kegiatan Pembelajaran

### Pre-class (15 menit)

- Buat akun Railway atau Vercel (gratis)
- Install Docker Desktop atau pastikan Docker tersedia di Codespaces
- Baca: "What is DevOps?" dari Atlassian

### In-class (120 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-25 menit | Konsep DevOps, CAMS, CI/CD | Ceramah + diskusi |
| 25-55 menit | Live demo: buat GitHub Actions workflow dari scratch | Live coding |
| 55-60 menit | *Break* | — |
| 60-80 menit | Docker basics: Dockerfile + docker-compose demo | Demo + hands-on |
| 80-105 menit | Hands-on: setup CI/CD pipeline untuk proyek kelompok | Hands-on |
| 105-120 menit | Cloud deployment overview + Q&A | Diskusi kelas |

### Post-class (15 menit)

- Lengkapi CI/CD setup untuk repository proyek kelompok
- Eksplorasi: tambahkan status badge GitHub Actions ke README proyek
- Mulai kerjakan tugas T5

---

## Penugasan

### T5 — CI/CD Pipeline Configuration

| Komponen | Detail |
|----------|--------|
| **Tipe** | Kelompok |
| **Deadline** | Minggu 13 |
| **Deliverable** | 1) File `.github/workflows/ci.yml`, 2) Dockerfile, 3) Dokumentasi pipeline |

**Instruksi:**
1. Buat GitHub Actions workflow yang mencakup: install dependencies, jalankan linting, jalankan test suite, dan build
2. Buat Dockerfile untuk aplikasi proyek kelompok
3. (Opsional) Deploy ke Railway/Vercel dan tunjukkan URL live
4. Dokumentasikan pipeline dalam `docs/ci-cd.md` di repository proyek

---

## Referensi

1. Humble, J. & Farley, D. (2010). *Continuous Delivery*. Addison-Wesley.
2. Kim, G. et al. (2016). *The DevOps Handbook*. IT Revolution Press.
3. GitHub Actions documentation. [docs.github.com/actions](https://docs.github.com/en/actions)
4. Docker documentation. [docs.docker.com](https://docs.docker.com/)
5. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering*, 9th ed. Chapter 29.
6. Railway documentation. [docs.railway.app](https://docs.railway.app/)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
