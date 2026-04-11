# Lab 1: Setup Dev Environment & GitHub Codespaces

## Informasi Praktikum

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Praktikum** | 1 dari 13 |
| **Topik** | Setup Dev Environment & GitHub Codespaces |
| **CPMK** | CPMK-1 (Mengkonfigurasi lingkungan pengembangan perangkat lunak modern) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Akun email aktif, browser modern (Chrome/Edge/Firefox) |

**Referensi Teori:** [IF2205 Minggu 1 — Pengantar Rekayasa Perangkat Lunak & SDLC](../../../rekayasa-perangkat-lunak/03-modules/week-01-pengantar-rekayasa-perangkat-lunak-dan-sdlc.md)

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. **Membuat** (*create* — C6) akun GitHub dan repository baru untuk proyek Perpustakaan Digital UAI
2. **Mengkonfigurasi** (*configure* — C3) GitHub Codespaces dengan devcontainer untuk environment Python/Flask
3. **Mengimplementasikan** (*implement* — C3) aplikasi Flask sederhana dengan minimal 3 route
4. **Menerapkan** (*apply* — C3) workflow dasar Git (add, commit, push) untuk version control

---

## Konsep Singkat

### Mengapa Development Environment Penting?

Dalam rekayasa perangkat lunak, **consistency of environment** adalah fondasi produktivitas tim. Bayangkan sebuah tim di mana setiap anggota memiliki versi Python berbeda, library berbeda, dan konfigurasi berbeda — bug "works on my machine" menjadi mimpi buruk.

**GitHub Codespaces** menyelesaikan masalah ini dengan menyediakan **cloud-based development environment** yang identik untuk semua anggota tim. Setiap Codespace adalah container Linux lengkap yang berjalan di cloud, diakses melalui browser atau VS Code.

> Pelajari lebih lanjut tentang SDLC dan pentingnya environment setup di [Modul IF2205 Minggu 1](../../../rekayasa-perangkat-lunak/03-modules/week-01-pengantar-rekayasa-perangkat-lunak-dan-sdlc.md).

### Arsitektur GitHub Codespaces

```
┌──────────────────────────────────────────────────────────┐
│                     BROWSER / VS Code                     │
│                    (Client Interface)                      │
├──────────────────────────────────────────────────────────┤
│                                                          │
│    ┌──────────────────────────────────────────────┐      │
│    │           GitHub Codespace (Cloud VM)         │      │
│    │                                              │      │
│    │   ┌────────────────┐  ┌──────────────────┐   │      │
│    │   │   VS Code IDE  │  │  Terminal (bash)  │   │      │
│    │   │   - Editor     │  │  - Python 3.11   │   │      │
│    │   │   - Extensions │  │  - pip / venv    │   │      │
│    │   │   - Git GUI    │  │  - Flask         │   │      │
│    │   └────────────────┘  └──────────────────┘   │      │
│    │                                              │      │
│    │   ┌────────────────────────────────────┐     │      │
│    │   │     .devcontainer/devcontainer.json │     │      │
│    │   │     (Konfigurasi environment)       │     │      │
│    │   └────────────────────────────────────┘     │      │
│    └──────────────────────────────────────────────┘      │
│                                                          │
│    ┌──────────────────────────────────────────────┐      │
│    │              GitHub Repository                │      │
│    │   perpustakaan-uai (source of truth)         │      │
│    └──────────────────────────────────────────────┘      │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### Proyek Semester: Perpustakaan Digital UAI

Sepanjang semester ini, kita akan membangun **Sistem Perpustakaan Digital UAI** — sebuah aplikasi web yang memungkinkan mahasiswa mencari buku, meminjam buku, dan mengelola koleksi perpustakaan. Lab 1 ini adalah langkah pertama: menyiapkan fondasi proyek.

### Flask — Micro Web Framework

**Flask** adalah micro web framework Python yang ringan namun powerful. Cocok untuk pembelajaran karena:
- Mudah dipahami (minimal boilerplate)
- Routing yang intuitif dengan decorator `@app.route()`
- Bisa berkembang dari Hello World hingga aplikasi produksi

---

## Persiapan

Sebelum praktikum dimulai, pastikan:

- [ ] Browser modern (Chrome, Edge, atau Firefox) sudah terpasang
- [ ] Koneksi internet stabil (Codespaces membutuhkan koneksi aktif)
- [ ] Sudah membaca [Modul IF2205 Minggu 1](../../../rekayasa-perangkat-lunak/03-modules/week-01-pengantar-rekayasa-perangkat-lunak-dan-sdlc.md)
- [ ] Alamat email aktif untuk registrasi GitHub

**Tools yang akan digunakan:**

| Tool | Versi | Fungsi |
|------|-------|--------|
| GitHub | — | Hosting repository & Codespaces |
| Python | 3.11 | Bahasa pemrograman backend |
| Flask | 3.x | Web framework |
| Git | (built-in) | Version control |
| VS Code (web) | (built-in) | Code editor di Codespaces |

---

## Langkah-langkah

### Langkah 1: Membuat Akun GitHub dan Repository (15 menit)

**Mengapa langkah ini penting:**
GitHub adalah platform kolaborasi standar industri untuk software engineering. Repository adalah "rumah" kode proyek kita — semua lab praktikum ke depan akan menggunakan repository yang sama.

**Instruksi:**

1. Buka [github.com](https://github.com) dan klik **Sign up**
2. Ikuti proses registrasi (jika belum punya akun)
3. Setelah login, klik tombol **+** di pojok kanan atas, pilih **New repository**
4. Isi form berikut:

| Field | Nilai |
|-------|-------|
| Repository name | `perpustakaan-uai` |
| Description | `Sistem Perpustakaan Digital UAI - Praktikum RPL IF2206` |
| Visibility | **Public** |
| Initialize | Centang **Add a README file** |
| .gitignore template | **Python** |
| License | **MIT License** |

5. Klik **Create repository**

**Expected Output:**

Anda seharusnya melihat halaman repository baru dengan:
- File `README.md` yang berisi nama repository
- File `.gitignore` untuk Python
- File `LICENSE` (MIT)

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| "Repository name already exists" | Tambahkan suffix NIM, misal `perpustakaan-uai-2024001` |
| Email belum terverifikasi | Cek inbox email, klik link verifikasi dari GitHub |
| Halaman loading terus | Refresh browser, pastikan koneksi internet stabil |

---

### Langkah 2: Membuka GitHub Codespaces (10 menit)

**Mengapa langkah ini penting:**
Codespaces memberikan environment yang konsisten untuk semua mahasiswa — tidak perlu install software di komputer lokal. Ini mencegah masalah "works on my machine" yang sering terjadi di tim pengembangan.

**Instruksi:**

1. Di halaman repository `perpustakaan-uai`, klik tombol hijau **<> Code**
2. Pilih tab **Codespaces**
3. Klik **Create codespace on main**
4. Tunggu 1-2 menit hingga environment selesai dimuat

**Expected Output:**

Anda seharusnya melihat VS Code di browser dengan:
- **Explorer** panel di kiri (menampilkan file README.md, .gitignore, LICENSE)
- **Editor** di tengah
- **Terminal** di bagian bawah (bisa dibuka dengan `Ctrl+\``)

Verifikasi di terminal:

```bash
# Cek versi Python
python3 --version
```

Output yang diharapkan:

```
Python 3.12.x
```

```bash
# Cek versi Git
git --version
```

Output yang diharapkan:

```
git version 2.x.x
```

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| Codespace gagal dimuat | Tunggu 1 menit, refresh. Jika masih gagal, hapus dan buat ulang |
| Terminal tidak muncul | Tekan `Ctrl+\`` atau menu **Terminal > New Terminal** |
| "You've used all your Codespaces hours" | Hubungi dosen untuk akses GitHub Education |

---

### Langkah 3: Konfigurasi Dev Container (10 menit)

**Mengapa langkah ini penting:**
File `devcontainer.json` memastikan **semua anggota tim mendapat environment yang identik** saat membuka Codespace. Ini adalah praktik profesional yang digunakan di perusahaan teknologi untuk menjamin konsistensi.

**Instruksi:**

1. Di terminal Codespaces, buat folder `.devcontainer`:

```bash
mkdir -p .devcontainer
```

2. Buat file `.devcontainer/devcontainer.json`:

```bash
cat > .devcontainer/devcontainer.json << 'EOF'
{
    "name": "Perpustakaan UAI - Python Flask",
    "image": "mcr.microsoft.com/devcontainers/python:3.11",
    "features": {
        "ghcr.io/devcontainers/features/node:1": {
            "version": "lts"
        }
    },
    "customizations": {
        "vscode": {
            "extensions": [
                "ms-python.python",
                "ms-python.debugpy",
                "esbenp.prettier-vscode",
                "dbaeumer.vscode-eslint",
                "GitHub.copilot"
            ],
            "settings": {
                "python.defaultInterpreterPath": "/usr/local/bin/python",
                "editor.formatOnSave": true,
                "editor.tabSize": 4
            }
        }
    },
    "postCreateCommand": "pip install flask",
    "forwardPorts": [5000],
    "portsAttributes": {
        "5000": {
            "label": "Flask App",
            "onAutoForward": "openBrowser"
        }
    }
}
EOF
```

**Expected Output:**

Verifikasi file telah dibuat:

```bash
cat .devcontainer/devcontainer.json
```

Anda harus melihat isi JSON yang lengkap seperti di atas.

> **Catatan:** Untuk sesi ini, devcontainer akan berlaku saat Codespace berikutnya dibuka. Kita akan lanjut menggunakan Codespace yang sudah aktif.

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| "Permission denied" | Pastikan Anda di root folder repository: `cd /workspaces/perpustakaan-uai` |
| JSON syntax error saat rebuild | Validasi JSON di [jsonlint.com](https://jsonlint.com) |

---

### Langkah 4: Setup Virtual Environment dan Install Flask (10 menit)

**Mengapa langkah ini penting:**
Virtual environment mengisolasi dependencies proyek kita dari sistem Python global. Ini mencegah konflik versi library antar proyek — praktik wajib dalam pengembangan Python profesional.

**Instruksi:**

1. Buat virtual environment:

```bash
python3 -m venv venv
```

2. Aktifkan virtual environment:

```bash
source venv/bin/activate
```

3. Verifikasi virtual environment aktif:

```bash
which python
```

Output yang diharapkan:

```
/workspaces/perpustakaan-uai/venv/bin/python
```

4. Install Flask:

```bash
pip install flask
```

5. Buat file `requirements.txt`:

```bash
pip freeze > requirements.txt
```

6. Verifikasi instalasi:

```bash
python -c "import flask; print(f'Flask versi: {flask.__version__}')"
```

Output yang diharapkan:

```
Flask versi: 3.1.x
```

**Expected Output:**

File `requirements.txt` seharusnya berisi (versi bisa berbeda):

```
blinker==1.9.0
click==8.1.8
Flask==3.1.0
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.2
Werkzeug==3.1.3
```

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| `python3: command not found` | Coba `python` tanpa angka 3 |
| `pip install` timeout | Coba lagi, koneksi internet mungkin lambat |
| Virtual env tidak aktif (tidak ada `(venv)` di prompt) | Jalankan ulang `source venv/bin/activate` |

---

### Langkah 5: Membuat Aplikasi Flask — Perpustakaan Digital UAI (20 menit)

**Mengapa langkah ini penting:**
Ini adalah momen pertama kita menulis kode untuk Sistem Perpustakaan Digital UAI. Tiga route yang kita buat merepresentasikan halaman utama aplikasi — fondasi yang akan terus dikembangkan di lab-lab berikutnya.

**Instruksi:**

1. Buat file `app.py` di root repository:

```python
"""
Sistem Perpustakaan Digital UAI
Praktikum Rekayasa Perangkat Lunak (IF2206)
Universitas Al Azhar Indonesia
"""

from flask import Flask, jsonify

app = Flask(__name__)

# ============================================================
# Data sementara (akan diganti database di Lab 7)
# ============================================================
PERPUSTAKAAN_INFO = {
    "nama": "Perpustakaan Digital UAI",
    "universitas": "Universitas Al Azhar Indonesia",
    "alamat": "Jl. Sisingamangaraja No.2, Jakarta Selatan",
    "jam_operasional": "Senin-Jumat 08:00-16:00",
    "total_koleksi": 15000,
    "versi_sistem": "0.1.0"
}

DAFTAR_BUKU_SAMPLE = [
    {
        "id": 1,
        "judul": "Introduction to Algorithms",
        "penulis": "Thomas H. Cormen et al.",
        "isbn": "978-0262033848",
        "kategori": "Computer Science",
        "tersedia": True
    },
    {
        "id": 2,
        "judul": "Software Engineering: A Practitioner's Approach",
        "penulis": "Roger S. Pressman",
        "isbn": "978-0078022128",
        "kategori": "Software Engineering",
        "tersedia": True
    },
    {
        "id": 3,
        "judul": "Clean Code: A Handbook of Agile Software Craftsmanship",
        "penulis": "Robert C. Martin",
        "isbn": "978-0132350884",
        "kategori": "Software Engineering",
        "tersedia": False
    }
]


# ============================================================
# Route Definitions
# ============================================================

@app.route("/")
def home():
    """Halaman utama Perpustakaan Digital UAI."""
    return jsonify({
        "pesan": "Selamat datang di Perpustakaan Digital UAI!",
        "deskripsi": "Sistem informasi perpustakaan Universitas Al Azhar Indonesia",
        "versi": PERPUSTAKAAN_INFO["versi_sistem"],
        "endpoints": {
            "home": "/",
            "about": "/about",
            "books": "/books"
        }
    })


@app.route("/about")
def about():
    """Informasi tentang Perpustakaan Digital UAI."""
    return jsonify({
        "tentang": "Perpustakaan Digital UAI",
        "info": PERPUSTAKAAN_INFO,
        "teknologi": {
            "backend": "Python Flask",
            "database": "Segera hadir (Lab 7)",
            "frontend": "Segera hadir (Lab 5)"
        },
        "pengembang": "Mahasiswa Praktikum RPL IF2206"
    })


@app.route("/books")
def books():
    """Daftar koleksi buku perpustakaan."""
    return jsonify({
        "total": len(DAFTAR_BUKU_SAMPLE),
        "buku": DAFTAR_BUKU_SAMPLE
    })


# ============================================================
# Entry Point
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("  Perpustakaan Digital UAI")
    print("  Universitas Al Azhar Indonesia")
    print("  Server berjalan di http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, host="0.0.0.0", port=5000)
```

**Expected Output:**

Verifikasi file telah dibuat:

```bash
wc -l app.py
```

Output: sekitar 95-100 baris.

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| Indentation error saat copy-paste | Pastikan gunakan 4 spasi (bukan tab) untuk Python |
| Salah ketik di kode | Bandingkan dengan kode di atas karakter per karakter |

---

### Langkah 6: Menjalankan Aplikasi Flask (10 menit)

**Mengapa langkah ini penting:**
Menjalankan aplikasi dan memverifikasi bahwa setiap route berfungsi adalah **praktik dasar testing** — kita memastikan kode yang ditulis benar-benar bekerja sebelum di-commit.

**Instruksi:**

1. Pastikan virtual environment aktif (ada `(venv)` di prompt)

2. Jalankan aplikasi:

```bash
python app.py
```

Output yang diharapkan di terminal:

```
==================================================
  Perpustakaan Digital UAI
  Universitas Al Azhar Indonesia
  Server berjalan di http://localhost:5000
==================================================
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://xxx.xxx.xxx.xxx:5000
```

3. Codespaces akan otomatis mendeteksi port 5000. Klik **Open in Browser** pada notifikasi yang muncul, atau buka tab **PORTS** di bagian bawah dan klik URL untuk port 5000.

4. Test setiap route di browser (atau buka terminal baru dengan `Ctrl+Shift+\``):

```bash
# Test route utama
curl http://localhost:5000/

# Test route about
curl http://localhost:5000/about

# Test route books
curl http://localhost:5000/books
```

**Expected Output untuk route `/`:**

```json
{
  "deskripsi": "Sistem informasi perpustakaan Universitas Al Azhar Indonesia",
  "endpoints": {
    "about": "/about",
    "books": "/books",
    "home": "/"
  },
  "pesan": "Selamat datang di Perpustakaan Digital UAI!",
  "versi": "0.1.0"
}
```

**Expected Output untuk route `/books`:**

```json
{
  "buku": [
    {
      "id": 1,
      "judul": "Introduction to Algorithms",
      ...
    }
  ],
  "total": 3
}
```

5. Hentikan server dengan `Ctrl+C` di terminal.

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| `ModuleNotFoundError: No module named 'flask'` | Aktifkan venv dulu: `source venv/bin/activate` lalu `pip install flask` |
| Port 5000 sudah dipakai | Ganti port: `app.run(port=5001)` atau kill proses: `lsof -i :5000` lalu `kill <PID>` |
| Browser menampilkan error 502 | Tunggu beberapa detik agar server siap, lalu refresh |
| "Address already in use" | Hentikan proses lama: `pkill -f "python app.py"` |

---

### Langkah 7: Membuat .gitignore dan Commit ke Repository (15 menit)

**Mengapa langkah ini penting:**
Version control adalah **jantung dari rekayasa perangkat lunak modern**. Setiap perubahan yang bermakna harus di-commit dengan pesan yang jelas. File `.gitignore` memastikan file yang tidak perlu (seperti virtual environment) tidak masuk ke repository.

**Instruksi:**

1. Update `.gitignore` untuk memastikan isi lengkap:

```bash
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Virtual Environment
venv/
env/
.venv/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Flask
instance/
.webassets-cache

# Environment variables
.env
.flaskenv

# Distribution
dist/
build/
*.egg-info/
EOF
```

2. Cek status repository:

```bash
git status
```

Expected output:

```
On branch main
Changes not staged for commit:
  modified:   .gitignore

Untracked files:
  .devcontainer/
  app.py
  requirements.txt
```

3. Commit pertama — devcontainer setup:

```bash
git add .devcontainer/devcontainer.json
git commit -m "chore: add devcontainer configuration for Python Flask environment"
```

4. Commit kedua — aplikasi Flask:

```bash
git add app.py requirements.txt
git commit -m "feat: create initial Flask app with home, about, and books routes

- Add Flask application with 3 routes (/, /about, /books)
- Include sample book data for Perpustakaan Digital UAI
- Add requirements.txt with Flask dependencies"
```

5. Commit ketiga — gitignore update:

```bash
git add .gitignore
git commit -m "chore: update .gitignore for Python/Flask project"
```

6. Push semua commit ke GitHub:

```bash
git push origin main
```

7. Verifikasi commit history:

```bash
git log --oneline
```

**Expected Output:**

```
abc1234 chore: update .gitignore for Python/Flask project
def5678 feat: create initial Flask app with home, about, and books routes
ghi9012 chore: add devcontainer configuration for Python Flask environment
jkl3456 Initial commit
```

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| `git push` gagal — permission denied | Pastikan Anda bekerja di Codespace yang terhubung ke repo Anda sendiri |
| "Author identity unknown" | Jalankan: `git config user.email "email@uai.ac.id"` dan `git config user.name "Nama Anda"` |
| Accidentally committed venv/ | Jalankan `git rm -r --cached venv/` lalu commit ulang |

---

### Langkah 8: Verifikasi di GitHub dan Eksplorasi Repository (10 menit)

**Mengapa langkah ini penting:**
Verifikasi memastikan bahwa semua pekerjaan kita sudah tersimpan dengan benar di cloud (GitHub). Ini juga melatih kebiasaan **memeriksa hasil kerja** — praktik profesional yang mencegah masalah di kemudian hari.

**Instruksi:**

1. Buka repository di browser: `https://github.com/<username>/perpustakaan-uai`
2. Verifikasi file yang ada:

| File/Folder | Harus Ada |
|-------------|-----------|
| `.devcontainer/devcontainer.json` | Ya |
| `app.py` | Ya |
| `requirements.txt` | Ya |
| `.gitignore` | Ya (updated) |
| `README.md` | Ya |
| `LICENSE` | Ya |
| `venv/` | **Tidak** (harus di-ignore) |

3. Klik tab **Commits** (atau icon clock) — seharusnya ada minimal 4 commits (termasuk "Initial commit")
4. Klik salah satu commit untuk melihat **diff** — perubahan yang terjadi di commit tersebut

5. Perbarui `README.md` dengan deskripsi proyek:

```bash
cat > README.md << 'EOF'
# Perpustakaan Digital UAI

Sistem informasi perpustakaan berbasis web untuk Universitas Al Azhar Indonesia.

## Teknologi

- **Backend:** Python 3.11 + Flask
- **Database:** SQLite + SQLAlchemy (segera hadir)
- **Frontend:** HTML/CSS/JS + Jinja2 (segera hadir)

## Cara Menjalankan

1. Buka repository ini di GitHub Codespaces
2. Aktifkan virtual environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Jalankan server: `python app.py`
5. Buka browser: `http://localhost:5000`

## API Endpoints

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/` | Halaman utama |
| GET | `/about` | Informasi perpustakaan |
| GET | `/books` | Daftar koleksi buku |

## Tim Pengembang

Mahasiswa Praktikum RPL IF2206 — Universitas Al Azhar Indonesia

## Lisensi

MIT License
EOF
```

```bash
git add README.md
git commit -m "docs: update README with project description and API endpoints"
git push origin main
```

**Expected Output:**

Repository di GitHub menampilkan README.md yang terformat rapi dengan tabel endpoint, instruksi menjalankan, dan deskripsi proyek.

---

## Tantangan Tambahan

### Tantangan 1: Route Tambahan (Basic)

Tambahkan route `/contact` yang mengembalikan informasi kontak perpustakaan (alamat, email, telepon). Commit dengan pesan conventional commit yang tepat.

### Tantangan 2: Error Handling (Intermediate)

Tambahkan custom error handler untuk error 404 (Not Found) dan 500 (Internal Server Error) yang mengembalikan response JSON yang informatif:

```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Halaman tidak ditemukan",
        "status": 404,
        "saran": "Cek kembali URL endpoint yang tersedia di /"
    }), 404
```

### Tantangan 3: Health Check Endpoint (Advanced)

Buat route `/health` yang mengembalikan status sistem termasuk:
- Status server (up/down)
- Waktu server saat ini (gunakan `datetime`)
- Uptime sejak server dimulai
- Versi Python dan Flask yang digunakan

Ini adalah pola umum yang digunakan di production untuk monitoring.

---

## Refleksi & AI Usage Log

Setelah menyelesaikan praktikum, isi tabel berikut di laporan Anda:

| No | Tanggal | Tool AI | Prompt yang Diberikan | Output AI | Modifikasi yang Dilakukan | Refleksi Pembelajaran |
|----|---------|---------|----------------------|-----------|--------------------------|----------------------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

**Panduan pengisian:**
- **Tool AI:** ChatGPT, Claude, GitHub Copilot, dll.
- **Prompt:** Apa yang Anda tanyakan ke AI
- **Output AI:** Ringkasan jawaban yang diberikan AI
- **Modifikasi:** Perubahan yang Anda lakukan terhadap output AI
- **Refleksi:** Apa yang Anda pelajari dari interaksi ini

> Kejujuran dalam mencatat penggunaan AI adalah bagian dari nilai **Amanah** yang dijunjung tinggi di UAI.

---

## Checklist Penyelesaian

- [ ] Akun GitHub aktif dan terverifikasi
- [ ] Repository `perpustakaan-uai` berhasil dibuat (public)
- [ ] Codespace berjalan lancar dan bisa mengakses terminal
- [ ] File `devcontainer.json` ada di folder `.devcontainer/`
- [ ] Virtual environment berhasil dibuat dan diaktifkan
- [ ] Flask terinstal dan `requirements.txt` ada
- [ ] File `app.py` memiliki 3 route (`/`, `/about`, `/books`) yang berfungsi
- [ ] Aplikasi Flask berjalan di port 5000 dan bisa diakses via browser
- [ ] Minimal 4 commits dengan pesan conventional commit yang jelas
- [ ] Semua perubahan sudah di-push ke GitHub
- [ ] `README.md` sudah diperbarui dengan deskripsi proyek
- [ ] File `venv/` tidak masuk ke repository (ada di `.gitignore`)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
