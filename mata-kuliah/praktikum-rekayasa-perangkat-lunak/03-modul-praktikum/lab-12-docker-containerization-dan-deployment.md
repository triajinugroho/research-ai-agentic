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

## Tujuan

1. **Menulis** Dockerfile untuk Flask application
2. **Membuat** docker-compose setup multi-service (app + database)
3. **Men-deploy** aplikasi ke cloud platform (Railway/Render)
4. **Memahami** environment variables dan production configuration

## Persiapan

- Docker dan docker-compose tersedia di Codespaces
- Proyek Flask dengan semua tests passing
- Akun Railway atau Render (gratis)

## Langkah-langkah

### Langkah 1: Menulis Dockerfile (20 menit)

```dockerfile
# Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements terlebih dahulu (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh source code
COPY . .

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

# Jalankan dengan gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:create_app()"]
```

Build dan test:
```bash
docker build -t perpustakaan-app:v1 .
docker run -p 5000:5000 perpustakaan-app:v1
# Buka http://localhost:5000 — pastikan berjalan
```

### Langkah 2: Docker Compose (20 menit)

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
      - SECRET_KEY=dev-secret-key-change-in-prod
      - FLASK_ENV=development
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
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d perpustakaan"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  pgdata:
```

```bash
# Jalankan semua service
docker compose up -d

# Lihat logs
docker compose logs -f web

# Cek status
docker compose ps

# Stop semua
docker compose down
```

### Langkah 3: Health Check Endpoint (10 menit)

```python
# app/routes/health.py
from flask import Blueprint, jsonify
from app import db

health_bp = Blueprint('health', __name__)

@health_bp.route('/health')
def health():
    """Health check endpoint untuk monitoring."""
    try:
        # Cek koneksi database
        db.session.execute(db.text('SELECT 1'))
        db_status = 'connected'
    except Exception:
        db_status = 'disconnected'

    return jsonify({
        'status': 'healthy',
        'database': db_status,
        'version': '1.0.0'
    }), 200
```

### Langkah 4: Production Configuration (10 menit)

```python
# config.py
import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-fallback-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # Pastikan SECRET_KEY di-set via environment variable
```

Buat `.env.example` (template, JANGAN commit `.env` asli):
```bash
# .env.example
SECRET_KEY=ganti-dengan-key-yang-kuat
DATABASE_URL=postgresql://user:pass@localhost:5432/perpustakaan
FLASK_ENV=production
```

### Langkah 5: Deploy ke Railway/Render (25 menit)

**Opsi A — Railway:**
1. Buka [railway.app](https://railway.app) → Login dengan GitHub
2. New Project → Deploy from GitHub repo
3. Add PostgreSQL plugin
4. Set environment variables: `SECRET_KEY`, `DATABASE_URL` (auto dari plugin)
5. Deploy → dapatkan URL publik

**Opsi B — Render:**
1. Buka [render.com](https://render.com) → Login dengan GitHub
2. New Web Service → Connect repository
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `gunicorn app:create_app()`
5. Add PostgreSQL database
6. Set environment variables
7. Deploy

**Verifikasi:**
```bash
# Test URL production
curl https://your-app.railway.app/health
# Harus return: {"status": "healthy", "database": "connected"}
```

### Langkah 6: Dokumentasi Deployment (5 menit)

Tambahkan di `README.md` proyek:
```markdown
## Deployment

### Local Development
\`\`\`bash
docker compose up -d
\`\`\`

### Production
Deployed on Railway/Render. URL: [link]
```

## Tantangan Tambahan

1. Buat multi-stage Dockerfile untuk image size lebih kecil
2. Tambahkan nginx sebagai reverse proxy di docker-compose
3. Konfigurasi auto-deploy dari CI pipeline (merge to main → deploy)

## Checklist Penyelesaian

- [ ] Dockerfile valid — build dan run berhasil
- [ ] docker-compose.yml (app + PostgreSQL) berjalan
- [ ] Health check endpoint `/health` berfungsi
- [ ] Environment variables terkonfigurasi (`.env.example`)
- [ ] Deploy ke Railway/Render berhasil — URL publik accessible
- [ ] Dokumentasi deployment di README
- [ ] AI Usage Log diisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
