# BAB 10: DEVOPS DAN CONTINUOUS DELIVERY

**Oleh: Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi | Level Bloom |
|-----------|-----------|-------------|
| 6.1 | Menerapkan CI/CD pipeline menggunakan GitHub Actions | C3 (Menerapkan) |
| 6.2 | Mengimplementasikan containerization (Docker) dan cloud deployment | C4 (Menganalisis) |

---

## 10.1 DevOps Culture

### 10.1.1 Apa Itu DevOps?

> **DevOps** = Development + Operations — sekumpulan praktik yang mengintegrasikan pengembangan software dan operasi IT untuk memperpendek siklus delivery.

```
     Plan → Code → Build → Test
       ↑                      ↓
    Monitor ← Operate ← Deploy ← Release
```

### 10.1.2 CALMS Framework

| Pilar | Deskripsi |
|-------|-----------|
| **C**ulture | Kolaborasi Dev + Ops, shared responsibility |
| **A**utomation | CI/CD pipeline, infrastructure as code |
| **L**ean | Eliminasi waste, small batch sizes |
| **M**easurement | Data-driven decisions, metrics |
| **S**haring | Knowledge sharing, blameless postmortems |

## 10.2 Continuous Integration (CI)

CI adalah praktik di mana developer sering merge kode ke shared repository, dan setiap merge memicu build dan test otomatis.

### 10.2.1 GitHub Actions

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
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

### 10.2.2 CI Best Practices

1. **Commit sering** — minimal sekali sehari
2. **Fix broken build segera** — prioritas #1
3. **Test otomatis** — setiap push harus trigger test
4. **Keep build fast** — target < 10 menit
5. **Everyone commits** — semua anggota tim

## 10.3 Continuous Delivery (CD)

### 10.3.1 CI vs CD vs CD

| Konsep | Deskripsi |
|--------|-----------|
| **Continuous Integration** | Merge + build + test otomatis |
| **Continuous Delivery** | + deploy ke staging otomatis, production manual |
| **Continuous Deployment** | + deploy ke production otomatis |

### 10.3.2 Deployment Pipeline

```yaml
# Extended pipeline dengan deployment
  deploy-staging:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/develop'
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to Railway
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
        run: railway up --service app
```

## 10.4 Docker dan Containerization

### 10.4.1 Mengapa Docker?

| Masalah | Solusi Docker |
|---------|---------------|
| "Works on my machine" | Container identik di semua environment |
| Dependency conflicts | Isolated environment per container |
| Complex setup | `docker compose up` — satu perintah |
| Inconsistent environments | Same image: dev = staging = production |

### 10.4.2 Dockerfile untuk Flask

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies dulu (cache layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 5000

# Jalankan aplikasi
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]
```

### 10.4.3 Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/perpustakaan
      - FLASK_ENV=development
    depends_on:
      - db
    volumes:
      - .:/app

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: perpustakaan
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

### 10.4.4 Docker Commands

```bash
# Build image
docker build -t perpustakaan-app .

# Run container
docker run -p 5000:5000 perpustakaan-app

# Docker Compose
docker compose up -d      # Start semua services
docker compose down        # Stop dan hapus
docker compose logs web    # Lihat logs
```

## 10.5 Cloud Deployment

### 10.5.1 Platform Deployment

| Platform | Tipe | Free Tier | Cocok Untuk |
|----------|------|-----------|-------------|
| **Railway** | PaaS | 500 jam/bulan | Proyek kuliah |
| **Render** | PaaS | Static + Web Service | Portfolio |
| **Vercel** | Serverless | Generous | Frontend + API |
| **Fly.io** | Container | 3 shared VMs | Docker apps |

### 10.5.2 Environment Variables

```bash
# .env (JANGAN commit ke Git!)
DATABASE_URL=postgresql://user:pass@localhost/db
SECRET_KEY=super-secret-key-jangan-hardcode
FLASK_ENV=production
```

```python
# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
```

### 10.5.3 Health Check Endpoint

```python
@app.route('/health')
def health_check():
    try:
        db.session.execute('SELECT 1')
        return jsonify({'status': 'healthy', 'database': 'connected'}), 200
    except Exception as e:
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500
```

## 10.6 Monitoring Basics

Key metrics to monitor:
- **Response time** — berapa lama request diproses
- **Error rate** — persentase request yang gagal (5xx)
- **Throughput** — jumlah request per detik
- **Uptime** — persentase waktu sistem berjalan

---

## AI Corner: AI untuk DevOps (Level: Advanced)

| Aktivitas | Prompt Contoh | Catatan |
|-----------|---------------|---------|
| CI/CD config | "Buatkan GitHub Actions workflow untuk Flask app dengan pytest, linting, dan deploy ke Railway" | Review secrets handling |
| Dockerfile | "Buatkan multi-stage Dockerfile untuk Flask app dengan Gunicorn" | Periksa security best practices |
| Debug pipeline | "GitHub Actions saya gagal di step ini: [paste error]. Bagaimana cara fix?" | AI bagus untuk debugging CI errors |

---

## Latihan Soal

### Level Dasar (C1-C2)
1. Jelaskan perbedaan CI, CD (Delivery), dan CD (Deployment).
2. Sebutkan 5 CALMS pilar DevOps.
3. Apa keuntungan Docker dibanding instalasi langsung?

### Level Menengah (C3-C4)
4. Buatlah GitHub Actions workflow yang: lint, test, build Docker image, deploy ke staging.
5. Tulis Dockerfile dan docker-compose.yml untuk Flask app + PostgreSQL.
6. Analisis: mengapa "works on my machine" masih terjadi dan bagaimana Docker menyelesaikannya?

### Level Mahir (C5-C6)
7. Rancang CI/CD pipeline lengkap untuk aplikasi e-commerce tim Anda — dari commit ke production.
8. Evaluasi: Railway vs Render vs Vercel — platform mana yang paling cocok untuk proyek kuliah dan mengapa?

---

## Rangkuman

1. **DevOps** mengintegrasikan Development dan Operations — CALMS framework.
2. **CI** memastikan setiap commit di-build dan di-test otomatis.
3. **CD** memperpanjang CI dengan automated deployment ke staging/production.
4. **GitHub Actions** adalah platform CI/CD terintegrasi di GitHub.
5. **Docker** mengisolasi aplikasi dalam container — konsisten di semua environment.
6. **Cloud deployment** (Railway, Render, Vercel) memudahkan deployment proyek kuliah.

---

## Referensi

1. Kim, G. et al. (2016). *The DevOps Handbook*. IT Revolution Press.
2. Humble, J. & Farley, D. (2010). *Continuous Delivery*. Addison-Wesley.
3. Docker Documentation. (2024). *Docker Docs*. docs.docker.com.
4. GitHub. (2024). *GitHub Actions Documentation*. docs.github.com/actions.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
