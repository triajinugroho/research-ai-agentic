# Lab 05: Frontend Development — HTML, CSS, dan JavaScript

## Informasi Praktikum

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Praktikum** | 5 dari 13 (Minggu 5) |
| **Topik** | Frontend Development: HTML5, CSS3, JavaScript, Jinja2 |
| **CPMK** | CPMK-4 (Mengimplementasikan komponen full-stack) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 04 (User Story & Sprint Planning) selesai |
| **Sprint** | Sprint 0 — Foundation |

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. **Membangun** (*C6*) struktur proyek Flask dengan app factory pattern dan template inheritance menggunakan Jinja2
2. **Mengimplementasikan** (*C3*) halaman web responsif dengan HTML5 semantik dan CSS3 (Flexbox, navigation bar, card layout)
3. **Menerapkan** (*C3*) interaktivitas frontend menggunakan JavaScript (search filter, form validation, dynamic table sorting)
4. **Mengintegrasikan** (*C4*) komponen frontend (templates, static files, flash messages) dalam arsitektur Flask

## Konsep Singkat

### Arsitektur Frontend dalam Aplikasi Web

Pada kuliah teori IF2205 Minggu 5 (*Arsitektur Perangkat Lunak dan Design Patterns*), Anda telah mempelajari pola arsitektur seperti MVC (Model-View-Controller) dan layered architecture. Dalam praktikum ini, kita fokus pada **View layer** — bagian yang berinteraksi langsung dengan pengguna.

```
┌─────────────────────────────────────────────┐
│                 Browser (Client)             │
│  ┌──────────┐  ┌──────────┐  ┌───────────┐  │
│  │  HTML5    │  │  CSS3     │  │ JavaScript│  │
│  │ (Struktur)│  │ (Styling) │  │ (Behavior)│  │
│  └──────────┘  └──────────┘  └───────────┘  │
└──────────────────┬──────────────────────────┘
                   │  HTTP Request/Response
┌──────────────────▼──────────────────────────┐
│              Flask (Server)                   │
│  ┌──────────────────────────────────────┐    │
│  │  Jinja2 Template Engine              │    │
│  │  base.html → child templates         │    │
│  │  Template Inheritance (DRY Principle) │    │
│  └──────────────────────────────────────┘    │
│  ┌──────────┐  ┌──────────┐  ┌───────────┐  │
│  │  Routes   │  │  Models   │  │  Static   │  │
│  │ (Controller)│ (Data)    │  │ (CSS/JS)  │  │
│  └──────────┘  └──────────┘  └───────────┘  │
└──────────────────────────────────────────────┘
```

**Konsep kunci yang dipraktikkan:**

- **Jinja2 Template Inheritance**: Prinsip DRY (Don't Repeat Yourself) — buat `base.html` sekali, extend di setiap halaman. Ini analog dengan *inheritance* di OOP.
- **Separation of Concerns**: HTML untuk struktur, CSS untuk presentasi, JavaScript untuk behavior. Setiap file punya tanggung jawab tunggal.
- **Responsive Design**: Desain yang menyesuaikan ukuran layar (mobile, tablet, desktop) menggunakan CSS Flexbox dan media queries.
- **Progressive Enhancement**: Halaman tetap berfungsi tanpa JavaScript; JS menambahkan pengalaman yang lebih baik.

> **Referensi Teori:** Modul IF2205 Minggu 5 — [Arsitektur Perangkat Lunak dan Design Patterns](../../rekayasa-perangkat-lunak/03-modules/week-05-arsitektur-perangkat-lunak-dan-design-patterns.md)

## Persiapan

1. **GitHub Codespaces** sudah terkonfigurasi dan repository proyek tim sudah di-clone
2. **Python 3.10+** dan **Flask** terinstal (`pip install flask`)
3. Pastikan sudah membaca modul teori IF2205 Minggu 5
4. Siapkan browser dengan Developer Tools (F12) untuk inspeksi HTML/CSS

Struktur proyek yang akan kita bangun di lab ini:

```
perpustakaan-uai/
├── app/
│   ├── __init__.py          # App factory (create_app)
│   ├── routes/
│   │   └── main.py          # Route handlers untuk halaman
│   ├── templates/
│   │   ├── base.html        # Base template (Jinja2 inheritance)
│   │   ├── index.html       # Homepage Perpustakaan
│   │   ├── books.html       # Daftar buku (tabel)
│   │   └── login.html       # Halaman login
│   └── static/
│       ├── css/
│       │   └── style.css    # Stylesheet responsif
│       └── js/
│           └── main.js      # JavaScript interaktivitas
├── config.py                # Konfigurasi (akan dilengkapi Lab 06)
└── run.py                   # Entry point
```

---

## Langkah-langkah

### Langkah 1: Inisialisasi Struktur Proyek Flask (10 menit)

**Mengapa langkah ini penting?** Struktur proyek yang baik (app factory pattern) memudahkan scaling, testing, dan kolaborasi tim. Ini mengikuti prinsip *Separation of Concerns* dari arsitektur berlapis yang dipelajari di teori.

Buat struktur direktori proyek:

```bash
# Dari root repository Anda
mkdir -p perpustakaan-uai/app/routes
mkdir -p perpustakaan-uai/app/templates
mkdir -p perpustakaan-uai/app/static/css
mkdir -p perpustakaan-uai/app/static/js
touch perpustakaan-uai/app/__init__.py
touch perpustakaan-uai/app/routes/__init__.py
touch perpustakaan-uai/app/routes/main.py
touch perpustakaan-uai/config.py
touch perpustakaan-uai/run.py
```

Buat file `app/__init__.py` — **App Factory Pattern**:

```python
# app/__init__.py
from flask import Flask


def create_app():
    """
    Factory function untuk membuat instance Flask app.
    Menggunakan Application Factory Pattern agar app bisa
    di-create ulang untuk testing (Lab 09) dan konfigurasi berbeda.
    """
    app = Flask(__name__)

    # Konfigurasi dasar (akan diperluas di Lab 06)
    app.config['SECRET_KEY'] = 'kunci-rahasia-perpustakaan-uai'

    # Register Blueprint
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
```

Buat file `run.py` — entry point:

```python
# run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

**Expected Output** — Jalankan `python run.py`:

```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

> **Troubleshooting:**
> - `ModuleNotFoundError: No module named 'flask'` → Jalankan `pip install flask`
> - `Address already in use` → Ganti port: `app.run(port=5001)` atau matikan proses lain di port 5000
> - Jika di Codespaces, URL akan di-forward otomatis — klik tab "Ports" di panel bawah

---

### Langkah 2: Buat Base Template dengan Jinja2 Inheritance (15 menit)

**Mengapa langkah ini penting?** Template inheritance menerapkan prinsip DRY — elemen yang berulang (navbar, footer, meta tags) hanya ditulis sekali di `base.html`. Setiap halaman hanya perlu mendefinisikan konten uniknya melalui `{% block %}`.

Buat file `app/routes/main.py`:

```python
# app/routes/main.py
from flask import Blueprint, render_template, request, flash, redirect, url_for

main_bp = Blueprint('main', __name__)

# Data sementara (akan diganti dengan database di Lab 07)
BUKU_DATA = [
    {'id': 1, 'judul': 'Algoritma dan Pemrograman Python', 'pengarang': 'Ahmad Fauzi', 'tahun': 2024, 'isbn': '978-602-001-001', 'kategori': 'Pemrograman'},
    {'id': 2, 'judul': 'Rekayasa Perangkat Lunak Modern', 'pengarang': 'Budi Santoso', 'tahun': 2023, 'isbn': '978-602-001-002', 'kategori': 'Software Engineering'},
    {'id': 3, 'judul': 'Basis Data: Konsep dan Implementasi', 'pengarang': 'Citra Dewi', 'tahun': 2024, 'isbn': '978-602-001-003', 'kategori': 'Database'},
    {'id': 4, 'judul': 'Jaringan Komputer dan Internet', 'pengarang': 'Dimas Pratama', 'tahun': 2022, 'isbn': '978-602-001-004', 'kategori': 'Jaringan'},
    {'id': 5, 'judul': 'Kecerdasan Buatan: Teori dan Praktik', 'pengarang': 'Eka Putri', 'tahun': 2025, 'isbn': '978-602-001-005', 'kategori': 'AI'},
    {'id': 6, 'judul': 'Struktur Data dengan Python', 'pengarang': 'Fajar Hidayat', 'tahun': 2023, 'isbn': '978-602-001-006', 'kategori': 'Pemrograman'},
]


@main_bp.route('/')
def index():
    """Halaman utama Perpustakaan Digital UAI."""
    jumlah_buku = len(BUKU_DATA)
    buku_terbaru = sorted(BUKU_DATA, key=lambda x: x['tahun'], reverse=True)[:3]
    return render_template('index.html', jumlah_buku=jumlah_buku, buku_terbaru=buku_terbaru)


@main_bp.route('/books')
def books():
    """Halaman daftar semua buku."""
    return render_template('books.html', buku_list=BUKU_DATA)


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Halaman login pengguna."""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            flash('Username dan password harus diisi!', 'error')
        elif username == 'admin' and password == 'admin123':
            flash(f'Selamat datang, {username}!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Username atau password salah!', 'error')

    return render_template('login.html')
```

Buat file `app/templates/base.html`:

```html
<!-- app/templates/base.html -->
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Perpustakaan Digital UAI{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar">
        <div class="nav-brand">
            <a href="{{ url_for('main.index') }}">📚 Perpustakaan Digital UAI</a>
        </div>
        <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">
            &#9776;
        </button>
        <ul class="nav-links" id="navLinks">
            <li><a href="{{ url_for('main.index') }}" class="{% if request.endpoint == 'main.index' %}active{% endif %}">Beranda</a></li>
            <li><a href="{{ url_for('main.books') }}" class="{% if request.endpoint == 'main.books' %}active{% endif %}">Katalog Buku</a></li>
            <li><a href="{{ url_for('main.login') }}" class="{% if request.endpoint == 'main.login' %}active{% endif %}">Login</a></li>
        </ul>
    </nav>

    <!-- Flash Messages -->
    <div class="container">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">
                        {{ message }}
                        <button class="alert-close" onclick="this.parentElement.remove()">&times;</button>
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <!-- Konten halaman (diisi oleh child template) -->
        {% block content %}{% endblock %}
    </div>

    <!-- Footer -->
    <footer class="footer">
        <p>&copy; 2026 Perpustakaan Digital — Universitas Al Azhar Indonesia</p>
        <p><em>"Problem Solvers in Digital, Driven by Ethics and Islamic Values"</em></p>
    </footer>

    <!-- JavaScript -->
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
```

**Expected Output** — Buka halaman di browser. Anda akan melihat navbar, container konten (masih kosong karena belum ada child template), dan footer.

> **Troubleshooting:**
> - `jinja2.exceptions.TemplateNotFound` → Pastikan file `base.html` ada di folder `app/templates/`, bukan di root
> - CSS/JS tidak loading → Periksa `url_for('static', ...)` dan pastikan folder `app/static/` ada

---

### Langkah 3: Buat Halaman Beranda dan Katalog Buku (15 menit)

**Mengapa langkah ini penting?** Setiap halaman menggunakan `{% extends "base.html" %}` untuk mewarisi layout. Ini menunjukkan keunggulan template inheritance — perubahan di `base.html` langsung berlaku di semua halaman.

Buat file `app/templates/index.html`:

```html
<!-- app/templates/index.html -->
{% extends "base.html" %}

{% block title %}Beranda — Perpustakaan Digital UAI{% endblock %}

{% block content %}
<section class="hero">
    <h1>Selamat Datang di Perpustakaan Digital UAI</h1>
    <p>Sistem informasi perpustakaan untuk civitas akademika Universitas Al Azhar Indonesia.
       Cari, pinjam, dan kelola koleksi buku secara digital.</p>
    <a href="{{ url_for('main.books') }}" class="btn btn-primary">Lihat Katalog Buku</a>
</section>

<section class="stats">
    <div class="stat-card">
        <h3>{{ jumlah_buku }}</h3>
        <p>Total Buku</p>
    </div>
    <div class="stat-card">
        <h3>5</h3>
        <p>Kategori</p>
    </div>
    <div class="stat-card">
        <h3>120</h3>
        <p>Anggota Aktif</p>
    </div>
</section>

<section class="recent-books">
    <h2>Buku Terbaru</h2>
    <div class="card-grid">
        {% for buku in buku_terbaru %}
        <div class="card">
            <div class="card-body">
                <h3 class="card-title">{{ buku.judul }}</h3>
                <p class="card-text">Pengarang: {{ buku.pengarang }}</p>
                <p class="card-text">Tahun: {{ buku.tahun }}</p>
                <span class="badge">{{ buku.kategori }}</span>
            </div>
        </div>
        {% endfor %}
    </div>
</section>
{% endblock %}
```

Buat file `app/templates/books.html`:

```html
<!-- app/templates/books.html -->
{% extends "base.html" %}

{% block title %}Katalog Buku — Perpustakaan Digital UAI{% endblock %}

{% block content %}
<h1>Katalog Buku Perpustakaan</h1>

<!-- Search Bar -->
<div class="search-container">
    <input type="text" id="searchInput" class="search-input"
           placeholder="Cari buku berdasarkan judul, pengarang, atau kategori..."
           aria-label="Cari buku">
    <span class="search-count" id="searchCount">Menampilkan {{ buku_list|length }} buku</span>
</div>

<!-- Tabel Buku -->
<div class="table-responsive">
    <table class="data-table" id="bookTable">
        <thead>
            <tr>
                <th data-sort="id" class="sortable">No &#x25B4;&#x25BE;</th>
                <th data-sort="judul" class="sortable">Judul &#x25B4;&#x25BE;</th>
                <th data-sort="pengarang" class="sortable">Pengarang &#x25B4;&#x25BE;</th>
                <th data-sort="tahun" class="sortable">Tahun &#x25B4;&#x25BE;</th>
                <th>ISBN</th>
                <th data-sort="kategori" class="sortable">Kategori &#x25B4;&#x25BE;</th>
            </tr>
        </thead>
        <tbody>
            {% for buku in buku_list %}
            <tr>
                <td>{{ buku.id }}</td>
                <td>{{ buku.judul }}</td>
                <td>{{ buku.pengarang }}</td>
                <td>{{ buku.tahun }}</td>
                <td>{{ buku.isbn }}</td>
                <td><span class="badge">{{ buku.kategori }}</span></td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>

<p class="empty-state" id="emptyState" style="display: none;">
    Tidak ada buku yang sesuai dengan pencarian Anda.
</p>
{% endblock %}
```

**Expected Output** — Akses `http://127.0.0.1:5000/`:

```
Selamat Datang di Perpustakaan Digital UAI
Sistem informasi perpustakaan untuk civitas akademika...
[Lihat Katalog Buku]

Total Buku: 6    Kategori: 5    Anggota Aktif: 120

Buku Terbaru:
- Kecerdasan Buatan: Teori dan Praktik (2025)
- Algoritma dan Pemrograman Python (2024)
- Basis Data: Konsep dan Implementasi (2024)
```

Akses `http://127.0.0.1:5000/books` — tabel dengan 6 buku ditampilkan.

> **Troubleshooting:**
> - Halaman kosong → Pastikan `{% extends "base.html" %}` ada di baris pertama child template
> - Data tidak muncul → Periksa variabel yang dikirim dari `render_template()` di `main.py`

---

### Langkah 4: Tambahkan CSS Responsif (15 menit)

**Mengapa langkah ini penting?** CSS yang terstruktur membuat aplikasi terlihat profesional dan dapat diakses di berbagai perangkat. Kita menggunakan Flexbox untuk layout yang fleksibel dan CSS custom properties (variables) untuk konsistensi warna.

Buat file `app/static/css/style.css`:

```css
/* app/static/css/style.css */
/* === CSS Variables === */
:root {
    --primary-color: #1a5276;    /* Biru UAI */
    --primary-light: #2980b9;
    --secondary-color: #27ae60;
    --accent-color: #e74c3c;
    --bg-color: #f8f9fa;
    --text-color: #2c3e50;
    --border-color: #dee2e6;
    --white: #ffffff;
    --shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    --radius: 8px;
}

/* === Reset & Base === */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--bg-color);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

/* === Navigation Bar === */
.navbar {
    background-color: var(--primary-color);
    padding: 0 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: var(--shadow);
}

.nav-brand a {
    color: var(--white);
    text-decoration: none;
    font-size: 1.3rem;
    font-weight: bold;
    padding: 1rem 0;
    display: inline-block;
}

.nav-toggle {
    display: none;
    background: none;
    border: none;
    color: var(--white);
    font-size: 1.5rem;
    cursor: pointer;
}

.nav-links {
    list-style: none;
    display: flex;
    gap: 0.5rem;
}

.nav-links a {
    color: rgba(255, 255, 255, 0.85);
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: var(--radius);
    transition: background-color 0.3s, color 0.3s;
}

.nav-links a:hover,
.nav-links a.active {
    background-color: rgba(255, 255, 255, 0.15);
    color: var(--white);
}

/* === Container === */
.container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 2rem 1.5rem;
    flex: 1;
}

/* === Hero Section === */
.hero {
    text-align: center;
    padding: 3rem 1rem;
    background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
    color: var(--white);
    border-radius: var(--radius);
    margin-bottom: 2rem;
}

.hero h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
}

.hero p {
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

/* === Buttons === */
.btn {
    display: inline-block;
    padding: 0.7rem 1.5rem;
    border: none;
    border-radius: var(--radius);
    cursor: pointer;
    text-decoration: none;
    font-size: 1rem;
    transition: background-color 0.3s, transform 0.2s;
}

.btn:hover {
    transform: translateY(-2px);
}

.btn-primary {
    background-color: var(--secondary-color);
    color: var(--white);
}

.btn-primary:hover {
    background-color: #219a52;
}

/* === Stats Section === */
.stats {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.stat-card {
    flex: 1;
    background: var(--white);
    padding: 1.5rem;
    text-align: center;
    border-radius: var(--radius);
    box-shadow: var(--shadow);
}

.stat-card h3 {
    font-size: 2rem;
    color: var(--primary-color);
}

/* === Card Grid === */
.card-grid {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
}

.card {
    flex: 1;
    min-width: 250px;
    background: var(--white);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    overflow: hidden;
    transition: transform 0.3s;
}

.card:hover {
    transform: translateY(-4px);
}

.card-body {
    padding: 1.5rem;
}

.card-title {
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
    color: var(--primary-color);
}

.card-text {
    color: #666;
    margin-bottom: 0.3rem;
}

.badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    background-color: var(--primary-light);
    color: var(--white);
    border-radius: 20px;
    font-size: 0.8rem;
    margin-top: 0.5rem;
}

/* === Search === */
.search-container {
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    flex-wrap: wrap;
}

.search-input {
    flex: 1;
    min-width: 250px;
    padding: 0.7rem 1rem;
    border: 2px solid var(--border-color);
    border-radius: var(--radius);
    font-size: 1rem;
    transition: border-color 0.3s;
}

.search-input:focus {
    outline: none;
    border-color: var(--primary-light);
}

.search-count {
    color: #888;
    font-size: 0.9rem;
}

/* === Data Table === */
.table-responsive {
    overflow-x: auto;
}

.data-table {
    width: 100%;
    border-collapse: collapse;
    background: var(--white);
    border-radius: var(--radius);
    overflow: hidden;
    box-shadow: var(--shadow);
}

.data-table th,
.data-table td {
    padding: 0.8rem 1rem;
    text-align: left;
    border-bottom: 1px solid var(--border-color);
}

.data-table th {
    background-color: var(--primary-color);
    color: var(--white);
    font-weight: 600;
}

.data-table th.sortable {
    cursor: pointer;
    user-select: none;
}

.data-table th.sortable:hover {
    background-color: var(--primary-light);
}

.data-table tbody tr:hover {
    background-color: #eef5fc;
}

.data-table tbody tr:nth-child(even) {
    background-color: #f8f9fa;
}

.empty-state {
    text-align: center;
    padding: 2rem;
    color: #888;
    font-style: italic;
}

/* === Alert / Flash Messages === */
.alert {
    padding: 1rem 1.5rem;
    border-radius: var(--radius);
    margin-bottom: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.alert-success {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

.alert-error {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}

.alert-close {
    background: none;
    border: none;
    font-size: 1.2rem;
    cursor: pointer;
    color: inherit;
}

/* === Login Form === */
.form-container {
    max-width: 420px;
    margin: 2rem auto;
    background: var(--white);
    padding: 2rem;
    border-radius: var(--radius);
    box-shadow: var(--shadow);
}

.form-container h2 {
    text-align: center;
    margin-bottom: 1.5rem;
    color: var(--primary-color);
}

.form-group {
    margin-bottom: 1.2rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.4rem;
    font-weight: 600;
    color: var(--text-color);
}

.form-group input {
    width: 100%;
    padding: 0.7rem 1rem;
    border: 2px solid var(--border-color);
    border-radius: var(--radius);
    font-size: 1rem;
    transition: border-color 0.3s;
}

.form-group input:focus {
    outline: none;
    border-color: var(--primary-light);
}

.form-group .error-text {
    color: var(--accent-color);
    font-size: 0.85rem;
    margin-top: 0.3rem;
    display: none;
}

.form-group input.invalid {
    border-color: var(--accent-color);
}

.form-group input.invalid + .error-text {
    display: block;
}

/* === Footer === */
.footer {
    background-color: var(--primary-color);
    color: rgba(255, 255, 255, 0.8);
    text-align: center;
    padding: 1.5rem;
    margin-top: auto;
}

.footer p {
    margin: 0.3rem 0;
}

/* === Responsive Design (Mobile First) === */
@media (max-width: 768px) {
    .nav-toggle {
        display: block;
    }

    .nav-links {
        display: none;
        flex-direction: column;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background-color: var(--primary-color);
        padding: 1rem;
    }

    .nav-links.show {
        display: flex;
    }

    .hero h1 {
        font-size: 1.5rem;
    }

    .stats {
        flex-direction: column;
    }

    .card-grid {
        flex-direction: column;
    }

    .card {
        min-width: auto;
    }
}
```

**Expected Output** — Refresh browser. Anda akan melihat:
- Navbar biru dengan brand "Perpustakaan Digital UAI" dan link navigasi
- Hero section dengan gradient biru dan tombol hijau "Lihat Katalog Buku"
- Card statistik yang tersusun horizontal (3 kolom)
- Footer biru di bawah halaman

Coba resize browser ke ukuran mobile (< 768px):
- Navbar links tersembunyi, diganti hamburger menu
- Stats dan cards berubah menjadi 1 kolom

> **Troubleshooting:**
> - CSS tidak berubah setelah edit → Hard refresh browser (Ctrl+Shift+R) karena caching
> - Layout berantakan → Periksa apakah semua CSS class names di HTML cocok dengan selector CSS
> - Di Codespaces, forward port dan buka preview di tab browser baru untuk hasil terbaik

---

### Langkah 5: Buat Halaman Login dengan Form (10 menit)

**Mengapa langkah ini penting?** Form adalah komponen inti aplikasi web. Halaman login mendemonstrasikan HTML form, method POST, dan integrasi dengan flash messages dari Flask.

Buat file `app/templates/login.html`:

```html
<!-- app/templates/login.html -->
{% extends "base.html" %}

{% block title %}Login — Perpustakaan Digital UAI{% endblock %}

{% block content %}
<div class="form-container">
    <h2>Login Perpustakaan</h2>
    <form id="loginForm" method="POST" action="{{ url_for('main.login') }}" novalidate>
        <div class="form-group">
            <label for="username">Username</label>
            <input type="text" id="username" name="username"
                   placeholder="Masukkan username" required
                   minlength="3" maxlength="50"
                   aria-describedby="usernameError">
            <span class="error-text" id="usernameError">Username minimal 3 karakter</span>
        </div>

        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" name="password"
                   placeholder="Masukkan password" required
                   minlength="6"
                   aria-describedby="passwordError">
            <span class="error-text" id="passwordError">Password minimal 6 karakter</span>
        </div>

        <button type="submit" class="btn btn-primary" style="width: 100%;">
            Masuk
        </button>
    </form>

    <p style="text-align: center; margin-top: 1rem; color: #888;">
        <em>Demo: username <code>admin</code>, password <code>admin123</code></em>
    </p>
</div>
{% endblock %}
```

**Expected Output** — Akses `http://127.0.0.1:5000/login`:
- Form login dengan input username dan password
- Klik "Masuk" tanpa mengisi → flash message "Username dan password harus diisi!"
- Isi `admin` / `admin123` → redirect ke beranda dengan flash "Selamat datang, admin!"
- Isi credential salah → flash message "Username atau password salah!"

---

### Langkah 6: Tambahkan JavaScript — Search Filter dan Form Validation (20 menit)

**Mengapa langkah ini penting?** JavaScript menambahkan interaktivitas di sisi client — pengguna mendapat feedback instan tanpa harus menunggu response dari server. Ini meningkatkan User Experience (UX) sesuai prinsip *responsive interaction*.

Buat file `app/static/js/main.js`:

```javascript
// app/static/js/main.js
// ============================================================
// JavaScript untuk Perpustakaan Digital UAI
// Fitur: Navigation toggle, Search filter, Table sorting,
//         Form validation
// ============================================================

document.addEventListener('DOMContentLoaded', function () {

    // --- 1. Mobile Navigation Toggle ---
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');

    if (navToggle && navLinks) {
        navToggle.addEventListener('click', function () {
            navLinks.classList.toggle('show');
        });
    }

    // --- 2. Search Filter (Halaman Katalog Buku) ---
    const searchInput = document.getElementById('searchInput');
    const bookTable = document.getElementById('bookTable');
    const searchCount = document.getElementById('searchCount');
    const emptyState = document.getElementById('emptyState');

    if (searchInput && bookTable) {
        searchInput.addEventListener('input', function () {
            const query = this.value.toLowerCase().trim();
            const rows = bookTable.querySelectorAll('tbody tr');
            let visibleCount = 0;

            rows.forEach(function (row) {
                // Cari di semua kolom (judul, pengarang, kategori, dll.)
                const text = row.textContent.toLowerCase();
                const isMatch = text.includes(query);
                row.style.display = isMatch ? '' : 'none';
                if (isMatch) visibleCount++;
            });

            // Update counter
            if (searchCount) {
                searchCount.textContent = 'Menampilkan ' + visibleCount + ' buku';
            }

            // Tampilkan empty state jika tidak ada hasil
            if (emptyState) {
                emptyState.style.display = visibleCount === 0 ? 'block' : 'none';
            }
        });
    }

    // --- 3. Dynamic Table Sorting ---
    const sortableHeaders = document.querySelectorAll('.data-table th.sortable');

    sortableHeaders.forEach(function (header) {
        let ascending = true;

        header.addEventListener('click', function () {
            const table = header.closest('table');
            const tbody = table.querySelector('tbody');
            const rows = Array.from(tbody.querySelectorAll('tr'));
            const columnIndex = Array.from(header.parentNode.children).indexOf(header);
            const sortKey = header.getAttribute('data-sort');

            rows.sort(function (rowA, rowB) {
                let cellA = rowA.children[columnIndex].textContent.trim();
                let cellB = rowB.children[columnIndex].textContent.trim();

                // Cek apakah nilai numerik (untuk kolom tahun, id)
                if (sortKey === 'tahun' || sortKey === 'id') {
                    return ascending
                        ? parseInt(cellA) - parseInt(cellB)
                        : parseInt(cellB) - parseInt(cellA);
                }

                // Sorting string (case-insensitive)
                return ascending
                    ? cellA.localeCompare(cellB, 'id')
                    : cellB.localeCompare(cellA, 'id');
            });

            // Re-append rows dalam urutan baru
            rows.forEach(function (row) {
                tbody.appendChild(row);
            });

            // Toggle arah sort
            ascending = !ascending;

            // Visual indicator: highlight kolom yang di-sort
            sortableHeaders.forEach(function (h) {
                h.classList.remove('sorted-asc', 'sorted-desc');
            });
            header.classList.add(ascending ? 'sorted-desc' : 'sorted-asc');
        });
    });

    // --- 4. Form Validation (Halaman Login) ---
    const loginForm = document.getElementById('loginForm');

    if (loginForm) {
        const usernameInput = document.getElementById('username');
        const passwordInput = document.getElementById('password');

        // Validasi real-time saat user mengetik
        function validateField(input, minLength) {
            const value = input.value.trim();
            if (value.length < minLength) {
                input.classList.add('invalid');
                return false;
            } else {
                input.classList.remove('invalid');
                return true;
            }
        }

        if (usernameInput) {
            usernameInput.addEventListener('blur', function () {
                validateField(this, 3);
            });
            usernameInput.addEventListener('input', function () {
                if (this.classList.contains('invalid')) {
                    validateField(this, 3);
                }
            });
        }

        if (passwordInput) {
            passwordInput.addEventListener('blur', function () {
                validateField(this, 6);
            });
            passwordInput.addEventListener('input', function () {
                if (this.classList.contains('invalid')) {
                    validateField(this, 6);
                }
            });
        }

        // Validasi saat submit
        loginForm.addEventListener('submit', function (event) {
            let isValid = true;

            if (usernameInput && !validateField(usernameInput, 3)) {
                isValid = false;
            }
            if (passwordInput && !validateField(passwordInput, 6)) {
                isValid = false;
            }

            if (!isValid) {
                event.preventDefault();
                // Fokus ke field pertama yang error
                const firstInvalid = loginForm.querySelector('.invalid');
                if (firstInvalid) firstInvalid.focus();
            }
        });
    }

    // --- 5. Auto-dismiss Flash Messages ---
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.style.opacity = '0';
            alert.style.transition = 'opacity 0.5s';
            setTimeout(function () {
                alert.remove();
            }, 500);
        }, 5000);  // Hilang setelah 5 detik
    });

});
```

**Expected Output** — Test fitur JavaScript:

1. **Search filter** (halaman `/books`): Ketik "python" di search box → hanya buku yang mengandung "python" yang ditampilkan. Counter berubah menjadi "Menampilkan 2 buku".

2. **Table sorting** (halaman `/books`): Klik header kolom "Tahun" → tabel terurut ascending. Klik lagi → descending.

3. **Form validation** (halaman `/login`): Klik field username, ketik "ab" lalu klik keluar field → border merah muncul dengan pesan "Username minimal 3 karakter".

4. **Mobile navigation**: Resize browser ke < 768px → hamburger icon muncul. Klik untuk toggle menu.

5. **Flash auto-dismiss**: Setelah login gagal, flash message otomatis hilang setelah 5 detik.

> **Troubleshooting:**
> - JavaScript tidak jalan → Buka Console (F12 → Console) untuk melihat error
> - `Uncaught TypeError: Cannot read properties of null` → Elemen belum ada di DOM; pastikan `DOMContentLoaded` membungkus semua kode
> - Search filter tidak bekerja → Pastikan `id="searchInput"` dan `id="bookTable"` ada di HTML

---

### Langkah 7: Implementasi Flash Messages dan Navigasi Antar Halaman (10 menit)

**Mengapa langkah ini penting?** Flash messages memberi feedback kepada pengguna setelah aksi (login berhasil/gagal). Ini adalah pola UX standar yang menggunakan fitur bawaan Flask (`flash()` + `get_flashed_messages()`).

Flash messages sudah diimplementasikan di `base.html` (Langkah 2) dan di route `login()` (Langkah 2). Sekarang, verifikasi semuanya bekerja end-to-end:

```bash
# Jalankan server
cd perpustakaan-uai
python run.py
```

**Skenario pengujian:**

| Aksi | URL | Expected Result |
|------|-----|-----------------|
| Buka beranda | `/` | Hero section, stats, 3 buku terbaru |
| Klik "Katalog Buku" | `/books` | Tabel 6 buku, search box, sortable headers |
| Ketik "python" di search | `/books` | 2 buku ditampilkan, counter update |
| Klik header "Tahun" | `/books` | Tabel terurut berdasarkan tahun |
| Buka login | `/login` | Form login dengan validation |
| Submit tanpa isi | `/login` | Client-side validation mencegah submit |
| Isi credential salah | `/login` | Flash merah "Username atau password salah!" |
| Isi admin/admin123 | `/login` → `/` | Redirect ke beranda, flash hijau "Selamat datang!" |
| Resize ke mobile | Semua halaman | Hamburger menu, layout 1 kolom |

**Expected Output di Terminal** (server log):

```
127.0.0.1 - - [11/Apr/2026 10:00:00] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [11/Apr/2026 10:00:05] "GET /books HTTP/1.1" 200 -
127.0.0.1 - - [11/Apr/2026 10:00:10] "GET /login HTTP/1.1" 200 -
127.0.0.1 - - [11/Apr/2026 10:00:15] "POST /login HTTP/1.1" 302 -
127.0.0.1 - - [11/Apr/2026 10:00:15] "GET / HTTP/1.1" 200 -
```

> **Troubleshooting:**
> - Flash message tidak muncul → Pastikan `SECRET_KEY` di-set di `app.config` (diperlukan oleh session Flask)
> - Redirect setelah POST tidak terjadi → Pastikan `return redirect(url_for('main.index'))` ada setelah `flash()`
> - Style flash message tidak tampil → Pastikan class `alert-success` dan `alert-error` ada di CSS

---

### Langkah 8: Verifikasi Akhir dan Commit (5 menit)

**Mengapa langkah ini penting?** Menyimpan pekerjaan ke Git memastikan progress tidak hilang dan rekan tim bisa melihat kontribusi Anda. Gunakan conventional commit messages yang dipelajari di Lab 02.

```bash
# Cek semua file yang dibuat
ls -la app/
ls -la app/templates/
ls -la app/static/css/
ls -la app/static/js/

# Pastikan server berjalan tanpa error
python run.py &
curl http://127.0.0.1:5000/          # Homepage
curl http://127.0.0.1:5000/books     # Katalog
curl http://127.0.0.1:5000/login     # Login page
kill %1

# Commit ke Git
git add .
git commit -m "feat(frontend): add HTML/CSS/JS pages for Perpustakaan Digital

- Add base.html with Jinja2 template inheritance
- Add index.html (homepage), books.html (katalog), login.html
- Add responsive CSS with Flexbox and mobile breakpoints
- Add JavaScript: search filter, table sorting, form validation
- Implement flash messages for user feedback"
```

**Expected Output** — Verifikasi bahwa file-file berikut ada dan tidak kosong:

```
app/__init__.py          ✓ App factory dengan Blueprint
app/routes/main.py       ✓ 3 routes (index, books, login)
app/templates/base.html  ✓ Jinja2 base template
app/templates/index.html ✓ Homepage
app/templates/books.html ✓ Katalog buku
app/templates/login.html ✓ Login form
app/static/css/style.css ✓ Responsive CSS
app/static/js/main.js   ✓ JavaScript interactivity
run.py                   ✓ Entry point
```

---

## Tantangan Tambahan

### Level 1 — Basic
Tambahkan halaman **"Tentang Kami"** (`about.html`) yang berisi informasi tentang Perpustakaan Digital UAI. Halaman harus menggunakan template inheritance dari `base.html` dan memiliki route `/about`. Tambahkan link "Tentang" di navbar.

### Level 2 — Intermediate
Implementasikan **dark mode toggle** menggunakan JavaScript. Simpan preferensi pengguna di `localStorage` sehingga tema tetap konsisten saat halaman di-refresh. Tambahkan tombol toggle di navbar dan buat CSS class `.dark-mode` yang mengubah warna background dan text.

### Level 3 — Advanced
Buat halaman **"Detail Buku"** (`book_detail.html`) yang menampilkan informasi lengkap satu buku saat user mengklik judul di tabel katalog. Gunakan route dynamic `/books/<int:id>`. Tambahkan tombol "Kembali ke Katalog" dan tampilkan informasi buku dalam layout card yang menarik.

---

## Refleksi & AI Usage Log

Setelah menyelesaikan praktikum, jawab pertanyaan refleksi berikut:

1. Apa keuntungan menggunakan template inheritance dibanding copy-paste HTML di setiap file?
2. Bagaimana CSS Flexbox membantu membuat layout responsif tanpa media queries yang kompleks?
3. Mengapa form validation perlu dilakukan di client-side (JavaScript) DAN server-side (Flask)?
4. Bagaimana arsitektur frontend ini berkaitan dengan pola MVC yang dipelajari di teori?

### AI Usage Log

Jika Anda menggunakan AI tools (ChatGPT, Claude, Copilot) selama praktikum ini, catat di tabel berikut:

| No | Prompt/Pertanyaan ke AI | Tool | Output yang Digunakan | Modifikasi yang Dilakukan | Pemahaman (1-5) |
|----|-------------------------|------|----------------------|---------------------------|-----------------|
| 1  | Contoh: "Bagaimana cara membuat navbar responsif dengan Flexbox?" | Claude | Kode CSS navbar | Menyesuaikan warna dan breakpoint | 4 |
| 2  | | | | | |
| 3  | | | | | |

> **Catatan:** Penggunaan AI sebagai *learning partner* diperbolehkan. Yang **tidak** diperbolehkan adalah meng-copy seluruh kode tanpa memahami logikanya. Tulis refleksi jujur tentang kontribusi AI vs pemahaman mandiri Anda.

---

## Checklist Penyelesaian

- [ ] Struktur proyek Flask lengkap (app factory pattern, routes, templates, static)
- [ ] `base.html` dengan Jinja2 template inheritance (navbar, footer, block content, flash messages)
- [ ] `index.html` — homepage dengan hero section, statistik, dan buku terbaru
- [ ] `books.html` — tabel katalog buku dengan data dari server
- [ ] `login.html` — form login dengan method POST
- [ ] CSS responsif (navbar, card layout, tabel, form styling, mobile breakpoint)
- [ ] JavaScript search filter berfungsi di halaman katalog
- [ ] JavaScript table sorting berfungsi (klik header kolom)
- [ ] JavaScript form validation berfungsi (client-side)
- [ ] Flash messages muncul untuk login berhasil dan gagal
- [ ] Semua 3+ halaman rendering dengan benar dan navigasi antar halaman berfungsi
- [ ] Kode di-commit ke Git dengan pesan commit yang deskriptif
- [ ] AI Usage Log diisi untuk sesi ini

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
