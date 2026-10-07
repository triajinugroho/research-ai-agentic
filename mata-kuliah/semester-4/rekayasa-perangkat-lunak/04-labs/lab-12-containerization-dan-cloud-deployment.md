# Lab 12: Containerization dan Cloud Deployment

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 11 dari 13 (Minggu 12) |
| **Topik** | Docker, Dockerfile, docker-compose, Cloud Deployment (Railway/Render), Environment Variables |
| **CPMK** | CPMK-6 (Sub-CPMK 6.2) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 11 selesai, CI pipeline berjalan, Flask app fungsional |

## Tujuan

1. **Memahami** (C2) konsep containerization dan perbedaannya dengan virtualisasi tradisional
2. **Menulis** (C3) Dockerfile yang efisien untuk Flask application
3. **Mengkonfigurasi** (C3) docker-compose untuk multi-container setup (app + database)
4. **Men-deploy** (C3) aplikasi ke cloud platform (Railway/Render) dengan environment variables yang aman

## Konsep Singkat

### Masalah: "It Works on My Machine"

Salah satu masalah klasik dalam software engineering adalah perbedaan environment:
- Developer A: Python 3.11, macOS, SQLite
- Developer B: Python 3.10, Windows, PostgreSQL
- Server production: Python 3.9, Linux, PostgreSQL

Akibatnya: kode yang berjalan di laptop developer gagal di server production. Container menyelesaikan masalah ini dengan *membungkus* aplikasi beserta seluruh dependensinya.

### Container vs Virtual Machine

```
Virtual Machine:                Container:
+---+ +---+ +---+              +---+ +---+ +---+
|App| |App| |App|              |App| |App| |App|
+---+ +---+ +---+              +---+ +---+ +---+
|Lib| |Lib| |Lib|              |Lib| |Lib| |Lib|
+---+ +---+ +---+              +---+ +---+ +---+
|OS | |OS | |OS |              +--Container Engine-+
+---+ +---+ +---+              |     (Docker)      |
+----Hypervisor----+           +-------------------+
|   Host OS        |           |     Host OS       |
+------------------+           +-------------------+
|   Hardware       |           |    Hardware       |
+------------------+           +-------------------+
```

| Aspek | Virtual Machine | Container |
|-------|----------------|-----------|
| **Ukuran** | GB (full OS) | MB (hanya app + libs) |
| **Startup** | Menit | Detik |
| **Isolasi** | Penuh (OS level) | Process level |
| **Resource** | Berat (RAM, CPU terpisah) | Ringan (shared kernel) |
| **Use Case** | Isolasi penuh, OS berbeda | Microservices, CI/CD |

### Konsep Docker

| Istilah | Penjelasan | Analogi |
|---------|-----------|---------|
| **Image** | Template read-only berisi app + dependencies | Cetakan kue |
| **Container** | Instance berjalan dari image | Kue yang sudah jadi |
| **Dockerfile** | Instruksi untuk membuat image | Resep kue |
| **Registry** | Tempat menyimpan/berbagi image | Toko kue |
| **Volume** | Penyimpanan persisten di luar container | Rak penyimpanan |
| **Network** | Komunikasi antar container | Jalur antar toko |

### Alur Kerja Docker

```
Dockerfile  --->  docker build  --->  Image  --->  docker run  --->  Container
(resep)           (memasak)           (kue jadi)    (menyajikan)      (kue di meja)
```

### docker-compose: Orkestrasi Multi-Container

Aplikasi nyata biasanya terdiri dari beberapa container:
- Container 1: Flask application (web server)
- Container 2: PostgreSQL database
- Container 3: Redis cache (opsional)

`docker-compose` mendefinisikan dan menjalankan semua container ini dalam satu perintah.

### Cloud Deployment

Setelah aplikasi di-containerize, deployment ke cloud menjadi sederhana karena cloud platform tinggal menjalankan container yang sama persis.

| Platform | Kelebihan | Free Tier |
|----------|-----------|-----------|
| **Railway** | Simple, GitHub integration | 500 jam/bulan |
| **Render** | Auto-deploy dari Git | Static sites gratis |
| **Fly.io** | Edge deployment, cepat | 3 shared VMs |

## Persiapan

### Verifikasi Docker di Codespaces

```bash
# Docker sudah pre-installed di Codespaces
docker --version
# Expected: Docker version 24.x.x

docker compose version
# Expected: Docker Compose version v2.x.x
```

### Pastikan Aplikasi Berjalan Lokal

```bash
# Jalankan Flask app tanpa Docker dulu
flask run --port 5000
# Buka http://localhost:5000 — pastikan berfungsi
# Ctrl+C untuk stop
```

### Pastikan requirements.txt Lengkap

```bash
# Generate requirements.txt jika belum ada
pip freeze > requirements.txt

# Pastikan berisi minimal:
cat requirements.txt | grep -E "Flask|gunicorn|SQLAlchemy"
# Expected: Flask==x.x.x, gunicorn==x.x.x, dll.
```

> **Troubleshooting:** Jika `pip freeze` menghasilkan terlalu banyak package, gunakan `pipreqs .` (install dulu: `pip install pipreqs`) untuk generate hanya package yang benar-benar diimport.

## Langkah-langkah

### Langkah 1: Menulis Dockerfile (20 menit)

**Mengapa:** Dockerfile adalah "resep" untuk membuat container image. Setiap instruksi membuat satu layer. Urutan instruksi penting untuk efisiensi caching.

```dockerfile
# Dockerfile

# 1. Base image: Python 3.11 slim (lebih kecil dari versi full)
FROM python:3.11-slim

# 2. Set working directory di dalam container
WORKDIR /app

# 3. Copy requirements.txt DULU (untuk caching layer)
#    Jika requirements.txt tidak berubah, Docker pakai cache
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy seluruh source code
#    Ini di-copy SETELAH install deps agar perubahan kode
#    tidak invalidate cache layer pip install
COPY . .

# 6. Expose port yang digunakan aplikasi
EXPOSE 5000

# 7. Environment variable default
ENV FLASK_APP=app
ENV FLASK_ENV=production

# 8. Healthcheck: Docker akan cek apakah container sehat
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

# 9. Command untuk menjalankan aplikasi
#    Gunakan gunicorn (production WSGI server), bukan flask run
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:create_app()"]
```

**Penjelasan urutan instruksi (caching strategy):**

```
Layer 1: FROM python:3.11-slim       <- Jarang berubah (cache ✓)
Layer 2: COPY requirements.txt       <- Berubah jika deps berubah
Layer 3: RUN pip install             <- Cache jika requirements.txt sama
Layer 4: COPY . .                    <- Berubah setiap kode berubah
Layer 5: CMD                         <- Jarang berubah (cache ✓)
```

> **Tips:** Jika Anda membalik urutan (COPY semua dulu, baru pip install), maka setiap perubahan kode akan mengulang pip install dari awal. Ini membuang waktu!

**Build dan jalankan:**

```bash
# Build image (titik di akhir = build context = direktori saat ini)
docker build -t perpustakaan-app .

# Expected output terakhir:
# Successfully built abc123def456
# Successfully tagged perpustakaan-app:latest

# Jalankan container
docker run -p 5000:5000 --name perpustakaan perpustakaan-app

# Buka browser: http://localhost:5000
# Expected: halaman utama perpustakaan

# Stop container (di terminal lain)
docker stop perpustakaan
docker rm perpustakaan
```

**Cek ukuran image:**

```bash
docker images perpustakaan-app
# Expected: SIZE ~150-250 MB (slim base)
```

> **Troubleshooting:**
> - `gunicorn not found`: Pastikan gunicorn ada di requirements.txt
> - `ModuleNotFoundError`: Dependency kurang di requirements.txt
> - Port conflict: Gunakan port lain `-p 5001:5000`

**Estimasi waktu:** 20 menit

---

### Langkah 2: Tambahkan .dockerignore (5 menit)

**Mengapa:** Sama seperti `.gitignore`, file `.dockerignore` mencegah file yang tidak perlu masuk ke image. Ini membuat image lebih kecil dan build lebih cepat.

```
# .dockerignore

# Python
__pycache__/
*.pyc
*.pyo
.pytest_cache/
htmlcov/
.coverage

# Virtual environment
venv/
.venv/
env/

# Git
.git/
.gitignore

# IDE
.vscode/
.idea/

# Docker
Dockerfile
docker-compose.yml
.dockerignore

# Docs
*.md
LICENSE

# Test results
test-results/
```

**Verifikasi dampak:**

```bash
# Rebuild — seharusnya lebih cepat dan image lebih kecil
docker build -t perpustakaan-app .
docker images perpustakaan-app
```

**Estimasi waktu:** 5 menit

---

### Langkah 3: Docker Compose — Multi-Container Setup (20 menit)

**Mengapa:** Aplikasi production biasanya butuh database terpisah. docker-compose mendefinisikan seluruh stack (app + database) dalam satu file dan menjalankannya dengan satu perintah.

```yaml
# docker-compose.yml

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/perpustakaan
      - FLASK_ENV=development
      - SECRET_KEY=dev-secret-key-ganti-di-production
    volumes:
      # Mount kode lokal untuk hot-reload saat development
      - .:/app
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: perpustakaan
    ports:
      - "5432:5432"
    volumes:
      # Data persisten — tidak hilang saat container restart
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d perpustakaan"]
      interval: 10s
      timeout: 5s
      retries: 5

# Volume untuk data persisten
volumes:
  pgdata:
```

**Penjelasan konfigurasi:**

| Konfigurasi | Penjelasan |
|-------------|-----------|
| `depends_on` + `condition` | `web` menunggu hingga `db` sehat sebelum start |
| `volumes: .:/app` | Sinkronisasi kode lokal ke container (dev mode) |
| `volumes: pgdata` | Data PostgreSQL persisten antar restart |
| `restart: unless-stopped` | Container otomatis restart jika crash |
| `healthcheck` | Docker secara berkala cek apakah DB siap |

**Jalankan stack:**

```bash
# Jalankan semua container di background
docker compose up -d

# Expected output:
# [+] Running 3/3
#  ✔ Network perpustakaan_default  Created
#  ✔ Container perpustakaan-db-1   Healthy
#  ✔ Container perpustakaan-web-1  Started

# Cek status
docker compose ps

# Expected:
# NAME                    STATUS              PORTS
# perpustakaan-db-1       running (healthy)   0.0.0.0:5432->5432/tcp
# perpustakaan-web-1      running             0.0.0.0:5000->5000/tcp

# Lihat logs
docker compose logs web
docker compose logs db

# Test aplikasi
curl http://localhost:5000/health
# Expected: {"status": "healthy"}
```

**Stop dan cleanup:**

```bash
# Stop semua container
docker compose down

# Stop dan hapus volume (data database hilang!)
docker compose down -v
```

> **Troubleshooting:**
> - `db: connection refused`: Database belum siap. Pastikan healthcheck dikonfigurasi dan `depends_on` menggunakan `condition: service_healthy`
> - `port already in use`: Ada proses lain di port 5000/5432. Gunakan `lsof -i :5000` untuk cek

**Estimasi waktu:** 20 menit

---

### Langkah 4: Health Check Endpoint (10 menit)

**Mengapa:** Health check endpoint memungkinkan monitoring tools, load balancer, dan Docker untuk mengetahui apakah aplikasi berjalan normal. Ini standar industri untuk production deployment.

```python
# app/routes/health.py
from flask import Blueprint, jsonify
from datetime import datetime

health_bp = Blueprint('health', __name__)


@health_bp.route('/health')
def health_check():
    """
    Health check endpoint.
    Digunakan oleh:
    - Docker HEALTHCHECK
    - Cloud platform (Railway/Render)
    - Monitoring tools (UptimeRobot, dll)
    """
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0'
    }), 200


@health_bp.route('/health/detailed')
def detailed_health():
    """
    Health check detail — cek koneksi ke database.
    JANGAN expose ke publik di production (informasi sensitif).
    """
    checks = {
        'app': 'healthy',
        'database': 'unknown'
    }

    try:
        # Coba query sederhana ke database
        from app import db
        db.session.execute(db.text('SELECT 1'))
        checks['database'] = 'healthy'
    except Exception as e:
        checks['database'] = f'unhealthy: {str(e)}'

    status = 'healthy' if all(
        v == 'healthy' for v in checks.values()
    ) else 'degraded'

    return jsonify({
        'status': status,
        'checks': checks,
        'timestamp': datetime.utcnow().isoformat()
    }), 200 if status == 'healthy' else 503
```

**Register blueprint di app factory:**

```python
# Di app/__init__.py, tambahkan:
from app.routes.health import health_bp
app.register_blueprint(health_bp)
```

**Test:**

```bash
curl http://localhost:5000/health
# Expected: {"status": "healthy", "timestamp": "2026-04-11T10:30:00", "version": "1.0.0"}

curl http://localhost:5000/health/detailed
# Expected: {"status": "healthy", "checks": {"app": "healthy", "database": "healthy"}, ...}
```

**Estimasi waktu:** 10 menit

---

### Langkah 5: Environment Variables dan Config (10 menit)

**Mengapa:** Konfigurasi yang berbeda antara development dan production (database URL, secret key, debug mode) harus dikelola melalui environment variables, **bukan** hardcoded di kode.

```python
# config.py
import os


class Config:
    """Konfigurasi dasar (shared semua environment)."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-fallback-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Konfigurasi untuk development."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'sqlite:///dev.db'  # Default: SQLite untuk development
    )


class ProductionConfig(Config):
    """Konfigurasi untuk production."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # Production HARUS punya DATABASE_URL
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        # Railway menggunakan 'postgres://' tapi SQLAlchemy butuh 'postgresql://'
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
            'postgres://', 'postgresql://', 1
        )


class TestingConfig(Config):
    """Konfigurasi untuk testing."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# Mapping nama config
config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
```

**Gunakan di app factory:**

```python
# app/__init__.py
from config import config_map

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')

    app = Flask(__name__)
    app.config.from_object(config_map[config_name])
    # ... rest of setup
```

**File `.env` untuk development lokal (JANGAN commit ke Git!):**

```bash
# .env (tambahkan ke .gitignore!)
FLASK_ENV=development
SECRET_KEY=my-dev-secret-key
DATABASE_URL=postgresql://user:pass@localhost:5432/perpustakaan
```

> **PENTING:** Tambahkan `.env` ke `.gitignore`:
> ```bash
> echo ".env" >> .gitignore
> ```

**Estimasi waktu:** 10 menit

---

### Langkah 6: Deploy ke Railway (25 menit)

**Mengapa:** Deploy ke cloud adalah langkah terakhir dalam pipeline SE. Railway dipilih karena mendukung Docker deployment langsung dari GitHub dan memiliki free tier yang cukup untuk proyek kuliah.

**Langkah 6a: Persiapan akun Railway**

1. Buka https://railway.app
2. Sign up / Login dengan akun GitHub
3. Klik "New Project"

**Langkah 6b: Deploy dari GitHub**

1. Pilih "Deploy from GitHub repo"
2. Pilih repository perpustakaan Anda
3. Railway otomatis mendeteksi Dockerfile

**Langkah 6c: Konfigurasi environment variables**

Di Railway dashboard, buka tab "Variables" dan tambahkan:

```
FLASK_ENV=production
SECRET_KEY=<generate random string yang panjang>
DATABASE_URL=<otomatis dari Railway PostgreSQL add-on>
```

**Langkah 6d: Tambah PostgreSQL database**

1. Di project Railway, klik "New" > "Database" > "PostgreSQL"
2. Railway otomatis mengisi `DATABASE_URL` di environment variables

**Langkah 6e: Verifikasi deployment**

```bash
# Railway memberikan URL publik, misalnya:
curl https://perpustakaan-production.up.railway.app/health

# Expected:
# {"status": "healthy", "timestamp": "...", "version": "1.0.0"}
```

**Langkah 6f: Test fitur di production**

1. Buka URL publik di browser
2. Coba login, cari buku, pinjam buku
3. Pastikan semua fitur berjalan seperti di lokal

> **Troubleshooting:**
> - `Application failed to respond`: Cek logs di Railway dashboard
> - `Database connection error`: Pastikan `DATABASE_URL` sudah diset dan aplikasi menggunakan config production
> - `502 Bad Gateway`: Gunicorn belum siap, tunggu beberapa detik lalu refresh
> - Build gagal: Pastikan Dockerfile valid dan semua dependencies ada di requirements.txt

**Estimasi waktu:** 25 menit

---

### Langkah 7: Multi-Stage Dockerfile (10 menit)

**Mengapa:** Multi-stage build menghasilkan image yang lebih kecil dengan memisahkan stage build dari stage runtime. Ini best practice untuk production.

```dockerfile
# Dockerfile.multistage

# Stage 1: Build — install dependencies
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Runtime — hanya copy yang dibutuhkan
FROM python:3.11-slim AS runtime
WORKDIR /app

# Copy installed packages dari builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy source code
COPY . .

EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:create_app()"]
```

**Bandingkan ukuran:**

```bash
docker build -t perpustakaan:single -f Dockerfile .
docker build -t perpustakaan:multi -f Dockerfile.multistage .

docker images | grep perpustakaan
# perpustakaan   single   ...   250MB
# perpustakaan   multi    ...   180MB  (lebih kecil!)
```

**Estimasi waktu:** 10 menit

## Tantangan Tambahan

### Tantangan 1: Basic — Docker Compose dengan Redis

Tambahkan Redis sebagai cache layer di docker-compose.yml. Konfigurasi Flask untuk menggunakan Redis sebagai session store.

### Tantangan 2: Intermediate — Deploy ke Render

Deploy aplikasi yang sama ke Render (https://render.com) sebagai alternatif Railway. Bandingkan:
- Kemudahan setup
- Kecepatan deployment
- Free tier limitations

### Tantangan 3: Advanced — Monitoring dan Logging

Tambahkan container monitoring (cAdvisor atau Prometheus) di docker-compose.yml. Konfigurasi aplikasi untuk mengirim logs terstruktur (JSON format) dan visualisasikan dengan container Grafana.

## Refleksi & AI Usage Log

Setelah menyelesaikan lab ini, isi AI Usage Log jika Anda menggunakan AI tools:

| No | Task | Tool | Prompt (ringkas) | Output | Modifikasi |
|----|------|------|------------------|--------|------------|
| 1 | ... | ... | ... | ... | ... |

**Pertanyaan refleksi:**
1. Apa perbedaan utama menjalankan aplikasi dengan `flask run` vs Docker container?
2. Mengapa environment variables lebih baik daripada hardcode konfigurasi?
3. Apa tantangan terbesar saat deploy ke cloud? Bagaimana Anda mengatasinya?
4. Dalam konteks Indonesia, apa pertimbangan memilih cloud provider (harga, lokasi data center, compliance)?

## Checklist Penyelesaian

- [ ] Dockerfile ditulis dan image berhasil di-build
- [ ] Container berjalan dan aplikasi bisa diakses
- [ ] `.dockerignore` dikonfigurasi
- [ ] `docker-compose.yml` dengan app + database berjalan
- [ ] Health check endpoint `/health` berfungsi
- [ ] Environment variables dikonfigurasi (tidak ada hardcoded secrets)
- [ ] Aplikasi berhasil di-deploy ke Railway/Render
- [ ] URL production bisa diakses dan fitur berjalan
- [ ] Refleksi dan AI Usage Log diisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
