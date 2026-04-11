# Lab 12: Docker Containerization dan Deployment

## Informasi Praktikum

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Praktikum** | 11 dari 13 (Minggu 12) |
| **Topik** | Docker, docker-compose, Cloud Deployment |
| **CPMK** | CPMK-6 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 11 (CI/CD) selesai |
| **Referensi Teori** | IF2205 Minggu 12 — Maintenance & Evolution |

## Tujuan

1. **Menulis** (C6) Dockerfile untuk Flask application dengan best practices
2. **Membuat** (C6) docker-compose setup multi-service (app + database)
3. **Men-deploy** (C3) aplikasi ke cloud platform (Railway/Render)
4. **Memahami** (C2) environment variables dan production vs development configuration

## Konsep Singkat

### Apa Itu Docker?

**Docker** adalah platform yang memungkinkan Anda mengemas aplikasi beserta semua dependensinya ke dalam sebuah **container** — unit standar yang berjalan sama di mana saja (laptop developer, CI server, production cloud).

```
Tanpa Docker                      Dengan Docker
============                      =============

Developer A:                      Developer A:
  Python 3.9                        [Container]
  SQLite                            Python 3.11 + PostgreSQL + Flask
  macOS                             Berjalan sama di macOS

Developer B:                      Developer B:
  Python 3.11                       [Container]
  PostgreSQL                        Python 3.11 + PostgreSQL + Flask
  Windows                           Berjalan sama di Windows

Server:                           Server:
  Python 3.10                       [Container]
  MySQL                             Python 3.11 + PostgreSQL + Flask
  Ubuntu                            Berjalan sama di Ubuntu

  "Works on my machine" bug          "It runs everywhere"
```

### Docker vs Virtual Machine

| Aspek | Docker Container | Virtual Machine |
|-------|-----------------|-----------------|
| **Ukuran** | MB (ringan) | GB (berat) |
| **Startup** | Detik | Menit |
| **Isolasi** | Process-level | OS-level |
| **Overhead** | Minimal | Signifikan |
| **Sharing** | Docker Hub | VM image (besar) |

### Konsep Kunci Docker

| Istilah | Penjelasan | Analogi |
|---------|-----------|---------|
| **Image** | Template read-only untuk membuat container | Resep masakan |
| **Container** | Instance yang berjalan dari image | Hidangan yang sudah jadi |
| **Dockerfile** | Instruksi untuk membuat image | Langkah-langkah resep |
| **docker-compose** | Menjalankan multi-container sekaligus | Menu lengkap (appetizer + main + dessert) |
| **Volume** | Persistent storage di luar container | Lemari penyimpanan bahan |
| **Port mapping** | Menghubungkan port container ke host | Nomor meja restoran |

> **Referensi teori:** Lihat modul IF2205 Minggu 12 — Maintenance & Evolution untuk pembahasan tentang deployment strategies, environment management, dan software evolution.

## Persiapan

- Docker dan docker-compose tersedia di Codespaces (sudah pre-installed)
- Proyek Flask dengan semua tests passing (dari Lab 09-11)
- Akun Railway (https://railway.app) atau Render (https://render.com) — gratis

**Verifikasi Docker:**
```bash
docker --version
docker compose version
```

**Expected output:**
```
Docker version 24.x.x, build xxxxx
Docker Compose version v2.x.x
```

## Langkah-langkah

### Langkah 1: Menulis Dockerfile dengan Best Practices (20 menit)

**Mengapa langkah ini penting?** Dockerfile menentukan bagaimana aplikasi dikemas. Dockerfile yang buruk menghasilkan image besar, lambat, dan tidak aman. Best practices membuat image kecil, cepat, dan production-ready.

**Buat file `.dockerignore` terlebih dahulu** — sama seperti `.gitignore` untuk Docker:
```
# .dockerignore
__pycache__/
*.pyc
.git/
.github/
.env
*.md
tests/
htmlcov/
.coverage
node_modules/
.venv/
venv/
```

**Mengapa .dockerignore penting?** Tanpa file ini, Docker akan menyalin semua file ke dalam image — termasuk `.git/` (puluhan MB), `node_modules/`, dan file test yang tidak perlu di production.

**Dockerfile sederhana (untuk mulai):**
```dockerfile
# Dockerfile
# 1. Base image — gunakan slim untuk ukuran lebih kecil
FROM python:3.11-slim

# 2. Set working directory di dalam container
WORKDIR /app

# 3. Copy requirements DULU (layer caching)
#    Jika requirements.txt tidak berubah, Docker akan pakai cache
#    dan tidak perlu install ulang dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy seluruh source code
COPY . .

# 5. Expose port yang digunakan Flask
EXPOSE 5000

# 6. Health check — Docker akan memeriksa apakah app masih berjalan
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

# 7. Jalankan dengan gunicorn (production WSGI server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:create_app()"]
```

**Multi-stage Build (untuk image lebih kecil):**
```dockerfile
# Dockerfile.multistage
# === STAGE 1: Builder ===
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# === STAGE 2: Production ===
FROM python:3.11-slim AS production

# Install curl untuk health check
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy hanya installed packages dari stage builder
COPY --from=builder /install /usr/local

# Copy source code
COPY . .

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

# Non-root user untuk keamanan
RUN useradd --create-home appuser
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:create_app()"]
```

**Perbandingan ukuran image:**
```
Tanpa multi-stage:  ~450 MB
Dengan multi-stage: ~180 MB   (60% lebih kecil!)
```

**Build dan test:**
```bash
docker build -t perpustakaan-app:v1 .
docker run -p 5000:5000 perpustakaan-app:v1
```

**Expected output:**
```
[2025-xx-xx] [INFO] Starting gunicorn 21.2.0
[2025-xx-xx] [INFO] Listening at: http://0.0.0.0:5000 (1)
[2025-xx-xx] [INFO] Using worker: sync
[2025-xx-xx] [INFO] Booting worker with pid: 7
[2025-xx-xx] [INFO] Booting worker with pid: 8
```

**Verifikasi:**
```bash
# Di terminal lain (atau tab baru di Codespaces)
curl http://localhost:5000/health
```

**Expected output:**
```json
{"status": "healthy", "database": "connected", "version": "1.0.0"}
```

> **Troubleshooting:** Jika `curl` gagal dengan `Connection refused`, tunggu beberapa detik (gunicorn butuh waktu startup). Jika tetap gagal, periksa log dengan `docker logs <container_id>`.

### Langkah 2: Docker Compose untuk Multi-Service (20 menit)

**Mengapa langkah ini penting?** Aplikasi production biasanya terdiri dari beberapa service (web app + database + cache). Docker Compose menjalankan semua service sekaligus dengan satu perintah.

```yaml
# docker-compose.yml
version: '3.8'

services:
  # === SERVICE 1: Web Application (Flask) ===
  web:
    build: .
    ports:
      - "5000:5000"               # Host port : Container port
    environment:
      - DATABASE_URL=postgresql://perpus_user:perpus_pass@db:5432/perpustakaan
      - SECRET_KEY=${SECRET_KEY:-dev-secret-key-change-in-prod}
      - FLASK_ENV=${FLASK_ENV:-development}
    depends_on:
      db:
        condition: service_healthy  # Tunggu sampai DB siap sebelum start web
    restart: unless-stopped
    volumes:
      - .:/app                     # Mount source code (untuk development)
    networks:
      - perpustakaan-network

  # === SERVICE 2: Database (PostgreSQL) ===
  db:
    image: postgres:15-alpine      # Alpine = image kecil (~80MB)
    environment:
      POSTGRES_USER: perpus_user
      POSTGRES_PASSWORD: perpus_pass
      POSTGRES_DB: perpustakaan
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data   # Persistent storage
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U perpus_user -d perpustakaan"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - perpustakaan-network

# VOLUMES: Data yang persisten (tidak hilang saat container dihapus)
volumes:
  pgdata:

# NETWORKS: Jaringan internal antar container
networks:
  perpustakaan-network:
    driver: bridge
```

**Perintah docker compose:**
```bash
# Jalankan semua service (build jika belum ada)
docker compose up -d --build

# Lihat status semua service
docker compose ps

# Lihat logs web app
docker compose logs -f web

# Lihat logs database
docker compose logs db

# Masuk ke container web (untuk debugging)
docker compose exec web bash

# Stop semua service
docker compose down

# Stop dan hapus data (termasuk database volume)
docker compose down -v
```

**Expected output `docker compose ps`:**
```
NAME                    COMMAND                  SERVICE   STATUS    PORTS
perpustakaan-web-1      "gunicorn --bind 0.0…"   web       Up        0.0.0.0:5000->5000/tcp
perpustakaan-db-1       "docker-entrypoint.s…"   db        Up        0.0.0.0:5432->5432/tcp
```

> **Troubleshooting:** Jika web service restart terus-menerus (`Restarting`), periksa log dengan `docker compose logs web`. Penyebab umum: DATABASE_URL salah, atau database belum siap (meskipun sudah pakai `depends_on` + healthcheck).

### Langkah 3: Health Check Endpoint (10 menit)

**Mengapa langkah ini penting?** Health check memberi tahu Docker (dan cloud platform) apakah aplikasi masih berjalan dengan benar. Tanpa health check, Docker tidak tahu apakah container "hidup tapi tidak berfungsi" (zombie container).

```python
# app/routes/health.py
from flask import Blueprint, jsonify
from app import db
import os

health_bp = Blueprint('health', __name__)

@health_bp.route('/health')
def health():
    """Health check endpoint untuk monitoring.

    Digunakan oleh:
    - Docker HEALTHCHECK
    - Load balancer (Railway/Render)
    - Monitoring tools (uptime checks)
    """
    status = {
        'status': 'healthy',
        'version': os.environ.get('APP_VERSION', '1.0.0'),
        'environment': os.environ.get('FLASK_ENV', 'production')
    }

    # Cek koneksi database
    try:
        db.session.execute(db.text('SELECT 1'))
        status['database'] = 'connected'
    except Exception as e:
        status['database'] = 'disconnected'
        status['status'] = 'degraded'

    http_code = 200 if status['status'] == 'healthy' else 503
    return jsonify(status), http_code
```

**Daftarkan blueprint di `app/__init__.py`:**
```python
from app.routes.health import health_bp
app.register_blueprint(health_bp)
```

**Test endpoint:**
```bash
curl http://localhost:5000/health | python -m json.tool
```

**Expected output:**
```json
{
    "status": "healthy",
    "database": "connected",
    "version": "1.0.0",
    "environment": "development"
}
```

### Langkah 4: Production vs Development Configuration (10 menit)

**Mengapa langkah ini penting?** Konfigurasi production dan development harus berbeda. Di development: debug ON, SQLite boleh. Di production: debug OFF, PostgreSQL wajib, secret key kuat.

```python
# config.py
import os

class Config:
    """Base configuration — shared antara dev dan prod."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-fallback-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Development — debug ON, error detail."""
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Log semua SQL query (berguna untuk debugging)

class ProductionConfig(Config):
    """Production — debug OFF, security ketat."""
    DEBUG = False
    SQLALCHEMY_ECHO = False

    # Validasi: SECRET_KEY wajib di-set via environment variable
    @staticmethod
    def init_app(app):
        if app.config['SECRET_KEY'] == 'dev-fallback-key':
            import warnings
            warnings.warn("SECRET_KEY belum di-set! Gunakan environment variable.")

class TestingConfig(Config):
    """Testing — database in-memory, testing mode ON."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Mapping nama config
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
```

**Buat `.env.example`** — template untuk developer baru (JANGAN commit `.env` asli):
```bash
# .env.example — Copy ke .env dan isi nilai yang sesuai
# cp .env.example .env

# Flask
SECRET_KEY=ganti-dengan-key-yang-kuat-minimal-32-karakter
FLASK_ENV=production

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/perpustakaan

# App
APP_VERSION=1.0.0
```

**Pastikan `.env` ada di `.gitignore`:**
```bash
echo ".env" >> .gitignore
```

### Langkah 5: Deploy ke Railway (25 menit)

**Mengapa langkah ini penting?** Deployment ke cloud platform adalah langkah terakhir yang membawa aplikasi Anda dari "berjalan di laptop" ke "bisa diakses siapa saja di internet".

**Step-by-step deployment ke Railway:**

**1. Persiapan file-file deployment:**
```bash
# Pastikan file-file ini ada:
ls Dockerfile requirements.txt Procfile

# Buat Procfile jika belum ada (Railway membacanya)
echo 'web: gunicorn "app:create_app()" --bind 0.0.0.0:$PORT' > Procfile
```

**2. Buat akun dan project di Railway:**
1. Buka https://railway.app dan login dengan GitHub
2. Klik "New Project"
3. Pilih "Deploy from GitHub repo"
4. Pilih repository proyek perpustakaan Anda
5. Railway akan otomatis mendeteksi Dockerfile

**3. Tambahkan PostgreSQL database:**
1. Di project Railway, klik "+ New"
2. Pilih "Database" > "Add PostgreSQL"
3. Railway otomatis membuat database dan mengisi variabel `DATABASE_URL`

**4. Set environment variables:**
Di Railway dashboard > Variables:

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | (generate random string: `python -c "import secrets; print(secrets.token_hex(32))"`) |
| `FLASK_ENV` | `production` |
| `DATABASE_URL` | (otomatis dari Railway PostgreSQL plugin) |
| `PORT` | (otomatis dari Railway) |

**5. Deploy:**
- Railway akan otomatis deploy saat Anda push ke branch `main`
- Tunggu hingga deployment selesai (biasanya 2-5 menit)
- Klik "Generate Domain" untuk mendapatkan URL publik

**6. Verifikasi deployment:**
```bash
# Ganti dengan URL Railway Anda
curl https://your-app.up.railway.app/health
```

**Expected output:**
```json
{"status": "healthy", "database": "connected", "version": "1.0.0", "environment": "production"}
```

**7. Inisialisasi database di production:**
```bash
# Jalankan migrasi database (jika menggunakan Flask-Migrate)
railway run flask db upgrade

# Atau seed data awal
railway run python seed_data.py
```

> **Opsi alternatif — Render:**
> 1. Buka https://render.com > New Web Service
> 2. Connect repository GitHub
> 3. Build Command: `pip install -r requirements.txt`
> 4. Start Command: `gunicorn "app:create_app()" --bind 0.0.0.0:$PORT`
> 5. Add PostgreSQL database
> 6. Set environment variables
> 7. Deploy

> **Troubleshooting deployment:**
> - **Build gagal:** Periksa Dockerfile syntax, pastikan requirements.txt lengkap
> - **App crash setelah deploy:** Periksa logs di Railway dashboard, biasanya missing env var
> - **Database error:** Pastikan DATABASE_URL mengarah ke PostgreSQL Railway, bukan SQLite
> - **502 Bad Gateway:** Pastikan app listen di `$PORT` (bukan hardcoded 5000)

### Langkah 6: Dokumentasi Deployment (5 menit)

**Mengapa langkah ini penting?** Developer lain (dan Anda di masa depan) perlu tahu cara menjalankan dan deploy aplikasi ini.

Tambahkan di `README.md` proyek:
```markdown
## Deployment

### Local Development (Docker Compose)
```bash
# Copy environment variables
cp .env.example .env

# Jalankan semua service
docker compose up -d --build

# Akses aplikasi
open http://localhost:5000

# Lihat logs
docker compose logs -f web

# Stop
docker compose down
```

### Production (Railway)
- URL: https://your-app.up.railway.app
- Database: Railway PostgreSQL
- CI/CD: Auto-deploy on push to main

### Environment Variables
Lihat `.env.example` untuk daftar lengkap variabel yang dibutuhkan.
```

## Troubleshooting Umum

| Error | Penyebab | Solusi |
|-------|----------|--------|
| `docker: Cannot connect to Docker daemon` | Docker service belum jalan | Di Codespaces, Docker sudah jalan. Di lokal: `sudo systemctl start docker` |
| `port 5000 already in use` | Port sudah dipakai proses lain | Ganti port: `docker run -p 5001:5000 ...` atau stop proses lain |
| `FATAL: password authentication failed` | Password PostgreSQL salah di docker-compose | Pastikan POSTGRES_PASSWORD di service db sama dengan yang di DATABASE_URL |
| `no such file: requirements.txt` | COPY gagal karena context salah | Pastikan Dockerfile ada di root project (sejajar dengan requirements.txt) |
| `unhealthy` di docker compose ps | Health check gagal | Periksa apakah endpoint `/health` ada dan curl terinstall di container |
| `502 Bad Gateway` di Railway | App tidak listen di PORT yang benar | Gunakan `$PORT` env var, bukan hardcoded 5000 |

## Tantangan Tambahan

1. **Basic:** Buat multi-stage Dockerfile dan bandingkan ukuran image dengan Dockerfile biasa (`docker images` untuk melihat ukuran)
2. **Intermediate:** Tambahkan service **Redis** di docker-compose sebagai cache layer. Gunakan untuk caching hasil query buku populer
3. **Advanced:** Konfigurasi auto-deploy: merge ke main di GitHub -> CI pipeline -> push Docker image ke GitHub Container Registry -> Railway auto-deploy dari registry

## Refleksi dan AI Usage Log

### Pertanyaan Refleksi
1. Apa manfaat terbesar Docker yang Anda rasakan dibandingkan menjalankan aplikasi langsung?
2. Mengapa kita perlu memisahkan konfigurasi development dan production?
3. Bagaimana Docker mendukung prinsip *amanah* — memastikan aplikasi berjalan sama di semua environment?

### Template AI Usage Log

| No | Task | AI Tool | Prompt (ringkas) | Output Quality (1-5) | Modifikasi yang Diperlukan | Waktu Hemat |
|----|------|---------|------------------|----------------------|---------------------------|-------------|
| 1 | | | | | | |
| 2 | | | | | | |

> Isi log ini dengan jujur. Penggunaan AI diperbolehkan dan didorong — yang penting adalah **transparansi** dan **evaluasi kritis** terhadap output AI.

## Checklist Penyelesaian

- [ ] `.dockerignore` dibuat dengan exclusion yang tepat
- [ ] Dockerfile valid — `docker build` dan `docker run` berhasil
- [ ] Memahami layer caching dan best practices Dockerfile
- [ ] `docker-compose.yml` dengan web + PostgreSQL berjalan (`docker compose up`)
- [ ] Health check endpoint `/health` berfungsi dan melaporkan status database
- [ ] Environment variables terkonfigurasi (`.env.example` ada di repo)
- [ ] Production config terpisah dari development config
- [ ] Deploy ke Railway/Render berhasil — URL publik accessible
- [ ] Health check di production mengembalikan "healthy"
- [ ] Dokumentasi deployment ditambahkan ke README
- [ ] AI Usage Log diisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
