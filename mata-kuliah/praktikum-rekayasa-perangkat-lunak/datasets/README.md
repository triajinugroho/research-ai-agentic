# Resource Guide — Praktikum Rekayasa Perangkat Lunak (IF2206)

## Development Platform

| Tool | Fungsi | Link |
|------|--------|------|
| GitHub Codespaces | Cloud IDE utama | github.com/codespaces |
| Python 3.x | Backend language | python.org |
| Flask | Web framework | flask.palletsprojects.com |
| Node.js | Frontend tooling | nodejs.org |

## Testing & Quality

| Tool | Fungsi |
|------|--------|
| pytest | Python testing framework |
| pytest-cov | Code coverage |
| Jest | JavaScript testing |
| flake8 | Python linting |
| Playwright | E2E testing |

## DevOps & Deployment

| Tool | Fungsi |
|------|--------|
| GitHub Actions | CI/CD pipeline |
| Docker | Containerization |
| Railway | Cloud deployment (free tier) |
| Render | Alternative deployment |

## Project Starter Template

```
nama-proyek/
├── app/
│   ├── __init__.py      # App factory
│   ├── models/          # SQLAlchemy models
│   ├── routes/          # Flask Blueprints
│   └── services/        # Business logic
├── static/              # CSS, JS
├── templates/           # HTML
├── tests/               # pytest tests
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Konteks Proyek Indonesia

Pilihan proyek menggunakan skenario lokal:
1. Sistem Perpustakaan Kampus
2. Aplikasi Manajemen UMKM
3. Sistem Antrian Puskesmas
4. E-Commerce Produk Lokal
5. Aplikasi Pengelolaan Zakat

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
