# Rubrik Penilaian Tugas Pemrograman (TP1-TP6) — IF2206

| Informasi | Detail |
|-----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Komponen** | Tugas Pemrograman (25% dari nilai akhir) |
| **Jumlah Tugas** | 6 tugas (TP1-TP6) |
| **Platform** | GitHub Codespaces |
| **Pengumpulan** | Pull Request ke repository praktikum |

---

## Daftar Tugas Pemrograman

| Tugas | Topik | CPMK | Deadline | AI Policy |
|-------|-------|------|----------|-----------|
| TP1 | Flask Hello World + Git | CPMK-1, CPMK-4 | Minggu 3 | AI **tidak** diizinkan |
| TP2 | Git Branching & PR | CPMK-2 | Minggu 4 | AI **tidak** diizinkan |
| TP3 | REST API CRUD | CPMK-4 | Minggu 8 | AI diizinkan + log |
| TP4 | Database CRUD + ORM | CPMK-4 | Minggu 10 | AI diizinkan + log |
| TP5 | Testing Suite | CPMK-5 | Minggu 12 | AI diizinkan + log |
| TP6 | Docker + Deployment | CPMK-6 | Minggu 14 | AI diizinkan + log |

**Nilai Tugas = Rata-rata (TP1 + TP2 + TP3 + TP4 + TP5 + TP6)**

---

## Skala Penilaian Rubrik

Semua rubrik menggunakan skala 4 level:

| Level | Skor | Deskripsi Umum |
|-------|------|----------------|
| **Excellent** | 4 | Melebihi ekspektasi, kualitas profesional |
| **Good** | 3 | Memenuhi semua kriteria dengan baik |
| **Adequate** | 2 | Memenuhi kriteria minimum, ada kekurangan |
| **Inadequate** | 1 | Tidak memenuhi kriteria minimum |

**Rumus nilai per TP:**
```
Nilai TP = Σ (Skor Dimensi × Bobot Dimensi) / 4 × 100
```

---

## TP1: Flask Hello World + Git

### Informasi Tugas

| Aspek | Detail |
|-------|--------|
| **Topik** | Membuat aplikasi Flask Hello World dan menginisiasi repository Git |
| **CPMK** | CPMK-1 (Setup & Tools), CPMK-4 (Full-Stack Dev) |
| **Deadline** | Minggu 3 |
| **Prasyarat** | Lab 01 (Setup Dev Environment) |
| **AI Policy** | **Tidak diizinkan** — tugas ini menguji kemampuan dasar yang harus dikuasai mandiri |

### Deskripsi

Mahasiswa membuat aplikasi Flask sederhana dengan minimal 2 route (`/` dan `/about`), menginisiasi repository Git dengan `.gitignore` dan `README.md`, serta melakukan minimal 5 meaningful commits yang menunjukkan progres pengerjaan.

### Rubrik Penilaian TP1

| Dimensi | Bobot | 4 (Excellent) | 3 (Good) | 2 (Adequate) | 1 (Inadequate) |
|---------|-------|---------------|----------|---------------|-----------------|
| **Fungsionalitas** | 30% | Aplikasi berjalan sempurna dengan 3+ routes, template Jinja2, dan static files | Aplikasi berjalan dengan 2 routes sesuai instruksi | Aplikasi berjalan tapi hanya 1 route atau ada error minor | Aplikasi tidak berjalan atau tidak menggunakan Flask |
| **Struktur Kode** | 25% | Kode terstruktur rapi: separation of concerns, naming convention konsisten, comments memadai | Kode readable, ada structure dasar, minimal comments | Kode berjalan tapi berantakan, tidak ada comments | Kode tidak terstruktur, sulit dibaca, banyak dead code |
| **Git Usage** | 25% | 7+ meaningful commits, pesan commit konvensional, `.gitignore` lengkap, branching digunakan | 5+ commits dengan pesan deskriptif, `.gitignore` ada | 3-4 commits, pesan commit generik ("update", "fix") | < 3 commits atau 1 commit besar, tidak ada `.gitignore` |
| **Dokumentasi** | 20% | `README.md` lengkap: deskripsi, cara install, cara run, screenshot, teknologi yang digunakan | `README.md` ada dengan deskripsi dan cara run | `README.md` ada tapi minimal (hanya judul) | Tidak ada `README.md` |

### Deliverable Checklist TP1

- [ ] File `app.py` dengan minimal 2 routes (`/` dan `/about`)
- [ ] Aplikasi dapat dijalankan dengan `flask run` tanpa error
- [ ] File `.gitignore` untuk Python/Flask
- [ ] File `README.md` dengan deskripsi dan instruksi menjalankan
- [ ] File `requirements.txt` dengan dependency Flask
- [ ] Minimal 5 meaningful Git commits
- [ ] Repository di-push ke GitHub

### Kesalahan Umum TP1

| Kesalahan | Dampak pada Nilai | Cara Menghindari |
|-----------|-------------------|------------------|
| Hanya 1 commit besar ("initial commit") | Git Usage = 1 | Commit setiap langkah signifikan |
| Tidak ada `requirements.txt` | Fungsionalitas -1 level | Jalankan `pip freeze > requirements.txt` |
| `README.md` hanya berisi judul | Dokumentasi = 1-2 | Ikuti template README minimal (deskripsi, install, run) |
| Menggunakan `print()` bukan `return` di route | Fungsionalitas = 2 | Flask route harus `return` string/template |
| File `__pycache__` ter-commit | Git Usage -1 level | Pastikan `.gitignore` mencakup `__pycache__/` |
| Virtual environment ter-commit | Git Usage -1 level | Tambahkan `venv/` ke `.gitignore` |

### Catatan Penilaian TP1

- TP1 adalah tugas **individual** pertama — dosen menilai kemampuan dasar.
- Kemampuan yang ditunjukkan di TP1 akan dibandingkan dengan performa saat **RTS (Minggu 8)**.
- Diskrepansi besar antara kualitas TP1 dan kemampuan saat RTS akan memicu investigasi.
- Mahasiswa dianjurkan mengerjakan TP1 **selama atau setelah Lab 01**, bukan menunda.

---

## TP2: Git Branching & Pull Request

### Informasi Tugas

| Aspek | Detail |
|-------|--------|
| **Topik** | Menerapkan Git branching strategy dan pull request workflow |
| **CPMK** | CPMK-2 (Version Control) |
| **Deadline** | Minggu 4 |
| **Prasyarat** | Lab 02 (Git Branching & PR Workflow) |
| **AI Policy** | **Tidak diizinkan** — tugas ini menguji kemampuan dasar Git yang harus dikuasai mandiri |

### Deskripsi

Mahasiswa menerapkan Git branching workflow pada repository TP1 (atau repository baru). Tugas mencakup: membuat minimal 3 feature branches, melakukan merge dengan menyelesaikan conflict, membuat pull request dengan deskripsi yang baik, dan melakukan code review terhadap PR rekan (peer review).

### Rubrik Penilaian TP2

| Dimensi | Bobot | 4 (Excellent) | 3 (Good) | 2 (Adequate) | 1 (Inadequate) |
|---------|-------|---------------|----------|---------------|-----------------|
| **Branching Strategy** | 30% | 4+ branches dengan naming convention konsisten (`feature/`, `fix/`), branch protection rules diterapkan | 3 branches dengan naming yang jelas | 2 branches, naming tidak konsisten | Hanya branch `main`, tidak ada branching |
| **Conflict Resolution** | 25% | Menyelesaikan 2+ merge conflicts dengan benar, commit merge bersih, tidak ada conflict markers tersisa | Menyelesaikan 1 merge conflict dengan benar | Mencoba resolve conflict tapi ada sisa markers atau kehilangan kode | Tidak ada evidence conflict resolution, atau conflict tidak terselesaikan |
| **Commit Quality** | 25% | Semua commits mengikuti conventional commits (`feat:`, `fix:`, `docs:`), atomic commits, pesan deskriptif | Sebagian besar commits deskriptif, beberapa mengikuti conventional commits | Commits ada tapi pesan generik ("update", "changes") | Sangat sedikit commits, pesan tidak informatif, commits terlalu besar |
| **PR & Review** | 20% | PR dengan deskripsi lengkap (what, why, how), screenshot, dan review constructive terhadap PR rekan | PR dengan deskripsi baik, melakukan review terhadap PR rekan | PR ada tapi deskripsi minimal, review superfisial | Tidak ada PR atau tidak melakukan review |

### Deliverable Checklist TP2

- [ ] Minimal 3 feature branches dengan naming convention
- [ ] Minimal 1 merge conflict yang diselesaikan (documented)
- [ ] Minimal 10 commits mengikuti conventional commit format
- [ ] Minimal 2 pull requests dengan deskripsi lengkap
- [ ] Code review terhadap minimal 1 PR rekan (comment constructive)
- [ ] Branch `main` bersih dan bisa di-build tanpa error
- [ ] Screenshot atau log yang menunjukkan conflict resolution

### Kesalahan Umum TP2

| Kesalahan | Dampak pada Nilai | Cara Menghindari |
|-----------|-------------------|------------------|
| Membuat branch tapi langsung merge tanpa perubahan | Branching = 1-2 | Setiap branch harus punya perubahan bermakna |
| Conflict markers (`<<<<<<<`) tersisa di kode | Conflict Resolution = 1 | Cek file setelah merge, jalankan `grep -r "<<<" .` |
| Commit message: "asdf", "test", "aaa" | Commit Quality = 1 | Gunakan format: `feat: tambah halaman about` |
| PR tanpa deskripsi | PR & Review = 1-2 | Tulis what, why, how di PR description |
| Tidak melakukan review PR rekan | PR & Review = 1-2 | Beri comment constructive di PR teman |
| Force push ke `main` | Branching = 1 | Jangan pernah force push ke `main` |

### Catatan Penilaian TP2

- Dosen akan memeriksa **Git history** secara detail (bukan hanya hasil akhir).
- Branch yang dibuat tapi tidak digunakan (tidak ada commit di dalamnya) tidak dihitung.
- Merge conflict harus **alami** (bukan sengaja dibuat dengan cara yang tidak realistis).
- Peer review harus **constructive** — comment "LGTM" saja tanpa feedback spesifik dinilai rendah.

---

## TP3: REST API CRUD

### Informasi Tugas

| Aspek | Detail |
|-------|--------|
| **Topik** | Mengimplementasikan REST API dengan operasi CRUD lengkap |
| **CPMK** | CPMK-4 (Full-Stack Dev) |
| **Deadline** | Minggu 8 |
| **Prasyarat** | Lab 06 (Backend Development) |
| **AI Policy** | AI **diizinkan** dengan AI Usage Log wajib |

### Deskripsi

Mahasiswa mengimplementasikan REST API menggunakan Flask untuk satu resource utama (misalnya `books`, `users`, atau resource sesuai proyek tim). API harus mendukung operasi CRUD lengkap (Create, Read, Update, Delete) dengan proper error handling, input validation, dan dokumentasi API.

### Rubrik Penilaian TP3

| Dimensi | Bobot | 4 (Excellent) | 3 (Good) | 2 (Adequate) | 1 (Inadequate) |
|---------|-------|---------------|----------|---------------|-----------------|
| **REST Compliance** | 30% | 5+ endpoints mengikuti RESTful convention sempurna (HTTP methods, status codes, URL naming, JSON response), mendukung pagination dan filtering | 5 endpoints CRUD lengkap dengan HTTP methods dan status codes yang benar | 3-4 endpoints, sebagian besar RESTful tapi ada inkonsistensi | < 3 endpoints atau tidak mengikuti REST convention |
| **Error Handling** | 25% | Error handling komprehensif: 400 (Bad Request), 404 (Not Found), 409 (Conflict), 500 (Server Error), custom error messages informatif | Error handling untuk 404 dan 400, pesan error jelas | Error handling minimal (hanya try-except generic) | Tidak ada error handling, aplikasi crash saat input salah |
| **Input Validation** | 25% | Validasi lengkap: tipe data, required fields, format (email, tanggal), panjang string, sanitasi input | Validasi tipe data dan required fields | Validasi minimal (hanya cek field ada atau tidak) | Tidak ada validasi input |
| **Dokumentasi API** | 20% | Dokumentasi lengkap: setiap endpoint didokumentasikan (URL, method, request body, response, contoh curl/Postman), README updated | Dokumentasi endpoints di README dengan contoh request/response | Dokumentasi ada tapi tidak lengkap (hanya daftar URL) | Tidak ada dokumentasi API |

### Deliverable Checklist TP3

- [ ] Minimal 5 REST endpoints (GET all, GET by id, POST, PUT, DELETE)
- [ ] HTTP status codes yang benar untuk setiap response
- [ ] Error handling untuk kasus: not found, bad request, server error
- [ ] Input validation untuk semua POST/PUT requests
- [ ] JSON response format yang konsisten
- [ ] File `README.md` dengan dokumentasi API (endpoints, contoh request/response)
- [ ] File `requirements.txt` updated
- [ ] Testing manual via curl atau Postman (screenshot di README)
- [ ] AI Usage Log (jika menggunakan AI)

### Kesalahan Umum TP3

| Kesalahan | Dampak pada Nilai | Cara Menghindari |
|-----------|-------------------|------------------|
| Menggunakan GET untuk create/delete | REST Compliance = 1-2 | POST untuk create, DELETE untuk delete, PUT untuk update |
| Semua response return 200 (termasuk error) | REST Compliance = 2 | Gunakan status code yang tepat: 201, 400, 404, 500 |
| Tidak ada try-except, aplikasi crash | Error Handling = 1 | Wrap setiap handler dengan error handling |
| Menerima input tanpa validasi | Input Validation = 1 | Cek required fields, tipe data, format |
| API docs hanya "ada 5 endpoint" | Dokumentasi = 1-2 | Dokumentasikan URL, method, body, response, contoh |
| Menggunakan AI tanpa log | Pelanggaran AI policy | Selalu isi AI Usage Log |

### Contoh Endpoint yang Baik vs Kurang Baik

**Baik (Excellent):**
```python
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found", "book_id": book_id}), 404
    return jsonify({"data": book.to_dict()}), 200
```

**Kurang baik (Inadequate):**
```python
@app.route('/books')
def get_book():
    return str(books)  # Tidak RESTful, tidak JSON, tidak ada error handling
```

---

## TP4: Database CRUD + ORM

### Informasi Tugas

| Aspek | Detail |
|-------|--------|
| **Topik** | Mengintegrasikan database dengan ORM dan operasi CRUD |
| **CPMK** | CPMK-4 (Full-Stack Dev) |
| **Deadline** | Minggu 10 |
| **Prasyarat** | Lab 07 (Database Integration & ORM) |
| **AI Policy** | AI **diizinkan** dengan AI Usage Log wajib |

### Deskripsi

Mahasiswa mengintegrasikan database SQLite menggunakan SQLAlchemy ORM ke aplikasi Flask dari TP3. Tugas mencakup: mendefinisikan 3+ models dengan relationships, membuat migrations, mengimplementasikan seed data, dan mengubah endpoints TP3 agar menggunakan database (bukan in-memory data).

### Rubrik Penilaian TP4

| Dimensi | Bobot | 4 (Excellent) | 3 (Good) | 2 (Adequate) | 1 (Inadequate) |
|---------|-------|---------------|----------|---------------|-----------------|
| **Model Design** | 30% | 4+ models dengan relationships yang tepat (1:N, M:N), field types sesuai, constraints (unique, nullable), dan index yang relevan | 3 models dengan 1:N relationship, field types benar | 2 models, relationship sederhana, beberapa field types tidak tepat | 1 model atau tidak menggunakan ORM, tidak ada relationships |
| **ORM Usage** | 25% | CRUD operations sepenuhnya via ORM, menggunakan query chaining, eager/lazy loading tepat, session management benar | CRUD via ORM benar, query dasar berfungsi | Sebagian CRUD via ORM, sebagian raw SQL, ada query yang tidak efisien | Mayoritas raw SQL, ORM tidak dimanfaatkan |
| **Migration** | 25% | Flask-Migrate terintegrasi, migration files tersedia, upgrade/downgrade berjalan, seed data script otomatis | Migration files ada dan berjalan, seed data manual | Migration ada tapi tidak lengkap (hanya initial), seed data hardcoded | Tidak ada migration, database dibuat manual |
| **Query Quality** | 20% | Query efisien: menggunakan filter, join, pagination di level database, menghindari N+1 problem | Query berfungsi benar, menggunakan filter dasar | Query berjalan tapi tidak efisien (memuat semua data lalu filter di Python) | Query error atau menghasilkan data yang salah |

### Deliverable Checklist TP4

- [ ] Minimal 3 SQLAlchemy models dengan relationships (1:N minimum)
- [ ] Migration files via Flask-Migrate (`flask db init`, `flask db migrate`, `flask db upgrade`)
- [ ] Seed data script (`seed.py` atau Flask CLI command)
- [ ] Semua endpoints TP3 sekarang menggunakan database (bukan in-memory)
- [ ] Query menggunakan ORM (bukan raw SQL)
- [ ] File `models.py` terpisah dari `app.py` (separation of concerns)
- [ ] Database file (`.db`) ada di `.gitignore`
- [ ] README updated dengan instruksi setup database
- [ ] AI Usage Log (jika menggunakan AI)

### Kesalahan Umum TP4

| Kesalahan | Dampak pada Nilai | Cara Menghindari |
|-----------|-------------------|------------------|
| Semua models dalam `app.py` (tidak terpisah) | Model Design -1 level | Buat `models.py` terpisah |
| Tidak ada relationships antar-model | Model Design = 1-2 | Definisikan `db.relationship()` dan `db.ForeignKey()` |
| Menggunakan raw SQL di tengah kode ORM | ORM Usage = 2 | Gunakan ORM methods: `.query.filter_by()`, `.add()`, `.commit()` |
| Tidak ada migration files | Migration = 1 | Gunakan `flask db init`, `flask db migrate`, `flask db upgrade` |
| File `.db` ter-commit ke GitHub | Model Design -1 level | Tambahkan `*.db` ke `.gitignore` |
| N+1 query problem (loop query) | Query Quality = 2 | Gunakan `joinedload()` atau `subqueryload()` |
| Seed data hardcoded di `app.py` | Migration = 2 | Buat `seed.py` terpisah |

### Contoh Model Design yang Baik

```python
# models.py — Contoh Excellent
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref='author', lazy='select')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    isbn = db.Column(db.String(13), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    categories = db.relationship('Category', secondary=book_categories, backref='books')
```

---

## TP5: Testing Suite

### Informasi Tugas

| Aspek | Detail |
|-------|--------|
| **Topik** | Menulis test suite komprehensif untuk aplikasi Flask |
| **CPMK** | CPMK-5 (Testing) |
| **Deadline** | Minggu 12 |
| **Prasyarat** | Lab 09 (Unit Testing) dan Lab 10 (Integration Testing) |
| **AI Policy** | AI **diizinkan** dengan AI Usage Log wajib |

### Deskripsi

Mahasiswa menulis test suite untuk aplikasi Flask dari TP3-TP4 menggunakan pytest. Suite harus mencakup unit tests untuk models dan utility functions, serta integration tests untuk API endpoints. Target coverage minimal 80%.

### Rubrik Penilaian TP5

| Dimensi | Bobot | 4 (Excellent) | 3 (Good) | 2 (Adequate) | 1 (Inadequate) |
|---------|-------|---------------|----------|---------------|-----------------|
| **Coverage** | 25% | Coverage >= 90%, semua models dan endpoints tercakup, laporan coverage tersedia | Coverage >= 80%, sebagian besar models dan endpoints tercakup | Coverage >= 60%, beberapa models/endpoints belum tercakup | Coverage < 60% atau tidak ada coverage report |
| **Test Quality** | 30% | Tests meaningful: setiap test punya 1 assertion jelas, test names deskriptif, fixtures digunakan, test terorganisir per module | Tests berjalan dan meaningful, beberapa menggunakan fixtures | Tests berjalan tapi banyak yang redundan atau trivial | Tests tidak berjalan atau hanya `assert True` |
| **TDD Evidence** | 25% | Git history menunjukkan test-first approach: commit test sebelum commit implementasi di beberapa fitur, RED-GREEN-REFACTOR visible | Beberapa tests ditulis bersamaan dengan kode (commit history menunjukkan), ada evidence iterasi | Tests ditulis setelah semua kode selesai (1 commit besar untuk tests) | Tidak ada evidence kapan tests ditulis, semua dalam 1 commit |
| **Edge Cases** | 20% | Edge cases komprehensif: empty input, boundary values, invalid types, concurrent access, error scenarios | Beberapa edge cases: empty input, invalid data | Hanya happy path yang ditest | Tidak ada variasi test case |

### Deliverable Checklist TP5

- [ ] File test terpisah: `test_models.py`, `test_routes.py` (minimal)
- [ ] Minimal 15 test cases (unit + integration)
- [ ] Test fixtures menggunakan `conftest.py`
- [ ] Test database terpisah dari production database
- [ ] Coverage report >= 80% (output `pytest --cov`)
- [ ] Screenshot coverage report di README
- [ ] Edge cases: minimal 3 test untuk input tidak valid
- [ ] Semua tests passing (`pytest` exit code 0)
- [ ] `requirements.txt` updated (pytest, pytest-cov)
- [ ] AI Usage Log (jika menggunakan AI)

### Kesalahan Umum TP5

| Kesalahan | Dampak pada Nilai | Cara Menghindari |
|-----------|-------------------|------------------|
| Tests hanya `assert True` | Test Quality = 1 | Setiap test harus test sesuatu yang bermakna |
| Semua tests dalam 1 file besar | Test Quality = 2 | Pisahkan: `test_models.py`, `test_routes.py` |
| Test menggunakan production database | Test Quality = 2 | Gunakan test database terpisah di `conftest.py` |
| Tidak ada `conftest.py` | Test Quality = 2 | Buat fixtures untuk test client dan test database |
| Coverage < 60% | Coverage = 1 | Test setiap model CRUD dan setiap API endpoint |
| Semua tests di 1 commit | TDD Evidence = 1-2 | Commit tests dan implementasi secara iteratif |
| Hanya test happy path | Edge Cases = 1-2 | Test juga: empty input, invalid id, duplicate data |

### Contoh Test yang Baik vs Kurang Baik

**Baik (Excellent):**
```python
def test_create_book_missing_title(client):
    """Test bahwa POST /books tanpa title mengembalikan 400"""
    response = client.post('/api/books', json={"isbn": "1234567890"})
    assert response.status_code == 400
    assert "title" in response.json["error"].lower()

def test_get_nonexistent_book(client):
    """Test bahwa GET /books/999 mengembalikan 404"""
    response = client.get('/api/books/999')
    assert response.status_code == 404
```

**Kurang baik (Inadequate):**
```python
def test_book():
    assert True  # Test tidak bermakna

def test_api():
    pass  # Test kosong
```

---

## TP6: Docker + Deployment

### Informasi Tugas

| Aspek | Detail |
|-------|--------|
| **Topik** | Containerization dengan Docker dan deployment ke cloud platform |
| **CPMK** | CPMK-6 (CI/CD & Deploy) |
| **Deadline** | Minggu 14 |
| **Prasyarat** | Lab 11 (CI/CD) dan Lab 12 (Docker & Deployment) |
| **AI Policy** | AI **diizinkan** dengan AI Usage Log wajib |

### Deskripsi

Mahasiswa membuat Dockerfile dan docker-compose.yml untuk aplikasi Flask dari TP3-TP5, kemudian melakukan deployment ke cloud platform (Railway, Render, atau platform sejenis). Aplikasi harus bisa diakses via URL publik.

### Rubrik Penilaian TP6

| Dimensi | Bobot | 4 (Excellent) | 3 (Good) | 2 (Adequate) | 1 (Inadequate) |
|---------|-------|---------------|----------|---------------|-----------------|
| **Dockerfile Quality** | 30% | Multi-stage build, image size optimal (< 200MB), non-root user, health check, `.dockerignore` lengkap, best practices diikuti | Single-stage build yang benar, `.dockerignore` ada, image berjalan | Dockerfile berjalan tapi tidak optimal (image besar, tidak ada `.dockerignore`) | Dockerfile error atau tidak bisa build |
| **Compose Config** | 25% | `docker-compose.yml` dengan 2+ services (app + db), volumes untuk persistence, environment variables dari `.env`, networks terpisah | `docker-compose.yml` dengan app service, environment variables | `docker-compose.yml` minimal (hanya 1 service, hardcoded config) | Tidak ada `docker-compose.yml` |
| **Deployment** | 25% | Aplikasi live di URL publik, HTTPS, environment variables aman, auto-deploy dari GitHub, monitoring basic | Aplikasi live di URL publik, environment variables dikonfigurasi | Aplikasi di-deploy tapi sering crash atau tidak stabil | Tidak berhasil deploy atau URL tidak bisa diakses |
| **Dokumentasi** | 20% | README lengkap: instruksi Docker build/run, deployment steps, URL live, arsitektur diagram, troubleshooting | README dengan instruksi Docker dan URL deployment | README ada tapi instruksi tidak lengkap | Tidak ada dokumentasi deployment |

### Deliverable Checklist TP6

- [ ] `Dockerfile` yang bisa di-build tanpa error
- [ ] `.dockerignore` file
- [ ] `docker-compose.yml` dengan minimal app service
- [ ] Aplikasi berjalan di Docker (`docker-compose up`)
- [ ] Deployment ke cloud platform (Railway/Render/sejenis)
- [ ] URL publik yang bisa diakses (lampirkan di README)
- [ ] Environment variables tidak di-hardcode (gunakan `.env`)
- [ ] README updated dengan instruksi Docker dan deployment
- [ ] Screenshot aplikasi berjalan di cloud
- [ ] AI Usage Log (jika menggunakan AI)

### Kesalahan Umum TP6

| Kesalahan | Dampak pada Nilai | Cara Menghindari |
|-----------|-------------------|------------------|
| Dockerfile menggunakan `python:3.x` bukan `python:3.x-slim` | Dockerfile Quality = 2-3 | Gunakan slim atau alpine image untuk ukuran kecil |
| Hardcode secrets di Dockerfile | Dockerfile Quality = 1-2 | Gunakan environment variables dan `.env` |
| Tidak ada `.dockerignore` | Dockerfile Quality = 2 | Buat `.dockerignore` (mirip `.gitignore`) |
| `docker-compose.yml` tanpa environment variables | Compose = 2 | Gunakan `env_file: .env` di compose |
| Deployment gagal dan tidak ada troubleshooting | Deployment = 1 | Dokumentasikan error dan langkah troubleshooting |
| URL deployment tidak bisa diakses saat grading | Deployment = 1-2 | Pastikan aplikasi tetap live hingga setelah grading |

### Contoh Dockerfile yang Baik

```dockerfile
# Multi-stage build — Excellent level
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .
RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
EXPOSE 5000
HEALTHCHECK CMD curl --fail http://localhost:5000/health || exit 1
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]
```

---

## Kebijakan Umum Tugas Pemrograman

### Pengumpulan

1. Semua tugas dikumpulkan melalui **pull request** ke repository praktikum di GitHub.
2. Deadline dihitung berdasarkan **timestamp commit terakhir** sebelum deadline.
3. Branch naming: `tp-N/NIM` (contoh: `tp-1/2210001`).
4. PR description harus mencakup: deskripsi singkat, checklist deliverables, screenshot (jika relevan).

### Late Policy

| Keterlambatan | Penalti |
|---------------|---------|
| Tepat waktu | Tidak ada penalti |
| <= 1 hari | Pengurangan 10% |
| 2-3 hari | Pengurangan 25% |
| 4-7 hari | Pengurangan 50% |
| > 7 hari | Tidak diterima (nilai 0) |

### Kebijakan AI Detail

#### TP1 dan TP2: AI Tidak Diizinkan

TP1 dan TP2 menguji kemampuan fundamental (Flask basics dan Git workflow) yang **harus** dikuasai secara mandiri. Kemampuan ini akan diuji langsung saat responsi (RTS). Penggunaan AI pada TP1-TP2 yang terdeteksi akan dianggap sebagai **pelanggaran akademik**.

Cara deteksi:
- Perbandingan kemampuan saat TP vs saat responsi
- Analisis commit pattern (commit terlalu sempurna tanpa iterasi)
- Similarity check antar-submission

#### TP3-TP6: AI Diizinkan dengan Log

Untuk TP3-TP6, AI boleh digunakan sebagai **pair programmer** dengan ketentuan:
1. **AI Usage Log wajib** dilampirkan di setiap submission.
2. Mahasiswa harus bisa **menjelaskan setiap baris kode** jika ditanya saat responsi atau demo.
3. Output AI harus **dimodifikasi dan disesuaikan** — bukan copy-paste langsung.
4. AI tidak boleh digunakan untuk **menulis seluruh tugas dari nol** — mahasiswa harus menunjukkan pemahaman dengan menulis kode sendiri terlebih dahulu, lalu menggunakan AI untuk improvement.

### Format AI Usage Log

```markdown
## AI Usage Log — TP[N]

| No | Tanggal | Tool | Prompt (ringkas) | Output (ringkas) | Modifikasi | Pemahaman |
|----|---------|------|------------------|------------------|------------|-----------|
| 1 | YYYY-MM-DD | ChatGPT/Claude/Copilot | ... | ... | ... | Y/N |
```

### Remedial

- Mahasiswa dengan nilai TP < 56 dapat mengajukan remedial (maksimal 2 TP per semester).
- Remedial: revisi tugas sesuai feedback dosen, deadline 7 hari.
- Nilai remedial maksimal **70** (setara B).
- Pengajuan remedial paling lambat 1 minggu setelah nilai diumumkan.

---

## Contoh Perhitungan Nilai

### Contoh: Mahasiswa A — TP3 (REST API CRUD)

| Dimensi | Bobot | Skor (1-4) | Kontribusi |
|---------|-------|------------|------------|
| REST Compliance | 30% | 4 | 1.20 |
| Error Handling | 25% | 3 | 0.75 |
| Input Validation | 25% | 3 | 0.75 |
| Dokumentasi API | 20% | 4 | 0.80 |
| **Total** | **100%** | | **3.50** |

```
Nilai TP3 = (3.50 / 4) × 100 = 87.5 → A
```

### Contoh: Mahasiswa B — TP3 (REST API CRUD)

| Dimensi | Bobot | Skor (1-4) | Kontribusi |
|---------|-------|------------|------------|
| REST Compliance | 30% | 2 | 0.60 |
| Error Handling | 25% | 2 | 0.50 |
| Input Validation | 25% | 1 | 0.25 |
| Dokumentasi API | 20% | 2 | 0.40 |
| **Total** | **100%** | | **1.75** |

```
Nilai TP3 = (1.75 / 4) × 100 = 43.75 → E (eligible untuk remedial)
```

---

## Hubungan Antar-TP (Progressive Building)

Tugas Pemrograman dirancang sebagai **proyek berkelanjutan** (progressive building). Setiap TP membangun di atas TP sebelumnya:

```
TP1 (Flask + Git)
  └── TP2 (Git Branching) → menerapkan branching pada repo TP1
        └── TP3 (REST API) → menambahkan API endpoints ke aplikasi Flask
              └── TP4 (Database) → mengganti in-memory data dengan SQLAlchemy ORM
                    └── TP5 (Testing) → menulis test suite untuk TP3-TP4
                          └── TP6 (Docker) → containerize dan deploy TP3-TP5
```

**Implikasi:**
- Mahasiswa yang tidak menyelesaikan TP3 akan kesulitan di TP4-TP6.
- TP1-TP2 bersifat independen (bisa dikerjakan di repo terpisah).
- TP3-TP6 sebaiknya dalam **satu repository** yang sama untuk menunjukkan progres.
- Dosen akan melihat kesinambungan kode antar-TP.

---

## Keterkaitan TP dengan Proyek Akhir

| TP | Skill yang Dibangun | Relevansi ke Proyek Akhir |
|----|---------------------|---------------------------|
| TP1 | Setup Flask, Git basics | Fondasi setup proyek tim |
| TP2 | Branching, PR, code review | Workflow kolaborasi tim |
| TP3 | REST API, error handling | Backend proyek |
| TP4 | Database, ORM, migration | Data layer proyek |
| TP5 | Testing, coverage, TDD | Quality assurance proyek |
| TP6 | Docker, deployment | Deployment proyek |

Mahasiswa yang konsisten mengerjakan TP1-TP6 dengan baik akan memiliki **keunggulan signifikan** dalam mengerjakan proyek akhir, karena semua skill sudah dipraktikkan secara individual terlebih dahulu.

---

## Ringkasan Quick Reference

| TP | Topik | CPMK | Deadline | Dimensi Kunci | AI |
|----|-------|------|----------|---------------|-----|
| TP1 | Flask Hello World + Git | CPMK-1, CPMK-4 | Minggu 3 | Fungsionalitas, Struktur Kode, Git, Docs | Tidak |
| TP2 | Git Branching & PR | CPMK-2 | Minggu 4 | Branching, Conflicts, Commits, PR | Tidak |
| TP3 | REST API CRUD | CPMK-4 | Minggu 8 | REST, Errors, Validation, API Docs | Ya + Log |
| TP4 | Database CRUD + ORM | CPMK-4 | Minggu 10 | Models, ORM, Migration, Queries | Ya + Log |
| TP5 | Testing Suite | CPMK-5 | Minggu 12 | Coverage, Quality, TDD, Edge Cases | Ya + Log |
| TP6 | Docker + Deployment | CPMK-6 | Minggu 14 | Dockerfile, Compose, Deploy, Docs | Ya + Log |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
