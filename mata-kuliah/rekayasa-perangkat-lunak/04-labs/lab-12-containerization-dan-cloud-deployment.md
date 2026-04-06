# Lab 12: Containerization dan Cloud Deployment

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 11 dari 13 (Minggu 12) |
| **Topik** | Docker, docker-compose, Cloud Deployment |
| **CPMK** | CPMK-6 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |

## Tujuan

1. **Menulis** Dockerfile untuk Flask application
2. **Membuat** docker-compose setup (app + database)
3. **Men-deploy** aplikasi ke cloud platform (Railway/Render)

## Langkah-langkah

### Langkah 1: Dockerfile (20 menit)
```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]
```

```bash
docker build -t perpustakaan-app .
docker run -p 5000:5000 perpustakaan-app
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
      - DATABASE_URL=sqlite:///data/app.db
      - FLASK_ENV=development
    volumes:
      - ./data:/app/data
    depends_on:
      - db
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: perpustakaan
    ports:
      - "5432:5432"
```

```bash
docker compose up -d
docker compose logs web
docker compose down
```

### Langkah 3: Health Check Endpoint (10 menit)
```python
@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200
```

### Langkah 4: Deploy ke Railway (30 menit)
1. Buka railway.app → login dengan GitHub
2. New Project → Deploy from GitHub repo
3. Set environment variables (DATABASE_URL, SECRET_KEY)
4. Deploy dan test URL publik

### Langkah 5: Environment Variables (10 menit)
```python
# config.py
import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
```

## Tantangan Tambahan

1. Multi-stage Dockerfile untuk image size yang lebih kecil
2. Deploy ke Render sebagai alternatif

## Checklist Penyelesaian

- [ ] Dockerfile berjalan (build + run berhasil)
- [ ] docker-compose.yml (app + database)
- [ ] Health check endpoint `/health`
- [ ] Berhasil deploy ke Railway/Render
- [ ] Environment variables terkonfigurasi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
