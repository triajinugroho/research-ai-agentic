# Lab 01: Setup GitHub Codespaces dan Git Workflow

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 1 dari 13 |
| **Topik** | Setup Development Environment, Git Basics, Flask Hello World |
| **CPMK** | CPMK-1 (Menjelaskan konsep dasar RPL, model proses, SWEBOK v4, etika profesi) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Browser modern (Chrome/Firefox), email aktif untuk registrasi GitHub |

---

## Tujuan

Setelah menyelesaikan lab ini, mahasiswa mampu:

1. **Membuat** (C6) akun GitHub dan repository yang terkonfigurasi untuk proyek Rekayasa Perangkat Lunak
2. **Mengkonfigurasi** (C3) GitHub Codespaces sebagai cloud-based development environment dengan `devcontainer.json`
3. **Menerapkan** (C3) perintah Git dasar (init, add, commit, push, pull) dalam workflow pengembangan
4. **Membuat** (C6) aplikasi Python/Flask sederhana dan memverifikasi hasilnya di browser

---

## Konsep Singkat

### Mengapa Development Environment Penting?

Dalam rekayasa perangkat lunak profesional, **konsistensi environment** adalah kunci kolaborasi tim yang efektif. Bayangkan skenario berikut: seorang developer menulis kode di Windows dengan Python 3.12, developer lain menggunakan macOS dengan Python 3.9 -- kode yang berjalan di satu mesin bisa gagal di mesin lain. Fenomena ini dikenal sebagai **"Works on my machine"** problem.

**GitHub Codespaces** menyelesaikan masalah ini dengan menyediakan cloud-based development environment yang identik untuk seluruh tim. Setiap anggota tim bekerja di lingkungan yang sama, termasuk versi Python, library yang terinstal, dan konfigurasi editor.

### Version Control dengan Git

**Git** adalah distributed version control system (VCS) yang memungkinkan:
- **Tracking perubahan** -- setiap modifikasi kode tercatat lengkap (siapa, kapan, apa)
- **Kolaborasi paralel** -- beberapa developer bisa bekerja bersamaan tanpa konflik
- **Rollback** -- kembali ke versi sebelumnya jika ada kesalahan
- **Branching** -- mengembangkan fitur baru tanpa mengganggu kode utama

```
Alur Git Dasar:
                                                      
  Working Directory ──git add──> Staging Area ──git commit──> Local Repo ──git push──> Remote (GitHub)
        │                                                          │
        └──────────────────── git pull ────────────────────────────┘
```

### Conventional Commits

Dalam proyek RPL, kita menggunakan **Conventional Commits** -- format pesan commit yang terstruktur:

```
<type>: <deskripsi singkat>

Tipe yang sering digunakan:
  feat:     Fitur baru
  fix:      Perbaikan bug
  docs:     Perubahan dokumentasi
  style:    Formatting (tidak mengubah logika)
  refactor: Refactoring kode
  test:     Menambah/memperbaiki test
  chore:    Maintenance (dependency, config)
```

> **Referensi:** Materi lengkap tersedia di modul Minggu 1 (`week-01`) dan Bab 1 Buku Ajar.

---

## Persiapan

| Kebutuhan | Detail |
|-----------|--------|
| Browser | Chrome atau Firefox versi terbaru |
| Akun GitHub | Daftar gratis di [github.com](https://github.com) jika belum punya |
| Email | Gunakan email kampus (`@uai.ac.id`) jika memungkinkan |
| Koneksi Internet | Stabil (Codespaces memerlukan koneksi aktif) |

---

## Langkah-langkah

### Langkah 1: Buat Akun GitHub dan Repository (15 menit)

**Mengapa:** GitHub adalah platform kolaborasi kode terbesar di dunia. Repository adalah "folder proyek" yang dilacak oleh Git. Membuat repository dengan konfigurasi yang tepat sejak awal menghemat waktu di kemudian hari.

**Instruksi:**

1. Buka [github.com](https://github.com) dan klik **Sign Up** (jika belum punya akun)
2. Isi username (saran: gunakan format `nama-uai`, contoh: `budi-uai`)
3. Setelah login, klik tombol **"+"** di kanan atas, pilih **"New repository"**
4. Isi form repository:

| Field | Isi |
|-------|-----|
| Repository name | `rpl-proyek-[nama-tim]` (contoh: `rpl-proyek-alpha`) |
| Description | "Proyek Rekayasa Perangkat Lunak - Semester Genap 2025/2026 - UAI" |
| Visibility | **Private** |
| Initialize | Centang "Add a README file" |
| .gitignore | Pilih template **Python** |
| License | Pilih **MIT License** |

5. Klik **"Create repository"**

**Expected Output:** Repository baru muncul di halaman GitHub dengan 3 file: `README.md`, `.gitignore`, dan `LICENSE`.

> **Troubleshooting:** Jika nama repository sudah terpakai, tambahkan suffix angka (misalnya `rpl-proyek-alpha-01`). Nama repository hanya boleh mengandung huruf, angka, dan tanda hubung.

---

### Langkah 2: Buka dan Jelajahi Codespace (10 menit)

**Mengapa:** GitHub Codespaces menyediakan VS Code di browser dengan environment Linux lengkap. Tidak perlu install apa pun di laptop -- semua berjalan di cloud.

**Instruksi:**

1. Di halaman repository, klik tombol hijau **"Code"**
2. Pilih tab **"Codespaces"**
3. Klik **"Create codespace on main"**
4. Tunggu 1-2 menit hingga environment siap

**Expected Output:** VS Code terbuka di browser dengan file explorer di kiri dan terminal di bawah.

**Jelajahi Codespace:**
- **File Explorer** (kiri): melihat dan mengelola file
- **Terminal** (bawah): menjalankan perintah bash
- **Extensions** (kiri, ikon kotak): menambah plugin
- **Source Control** (kiri, ikon branch): melihat perubahan Git

> **Troubleshooting:** Jika Codespace lambat, coba refresh browser. Jika gagal dibuat, pastikan akun GitHub sudah diverifikasi (cek email). Akun free mendapatkan 60 jam/bulan Codespaces.

---

### Langkah 3: Konfigurasi Environment dan devcontainer.json (15 menit)

**Mengapa:** File `devcontainer.json` memastikan setiap anggota tim mendapatkan environment yang identik. Ini adalah praktik standar di industri (digunakan di perusahaan seperti Gojek, Tokopedia) untuk menghindari "works on my machine" problem.

**Instruksi:**

1. Buka terminal di Codespace dan verifikasi tools yang tersedia:

```bash
# Verifikasi Python
python3 --version
# Expected: Python 3.x.x (misalnya Python 3.12.1)

# Verifikasi Git
git --version
# Expected: git version 2.x.x

# Verifikasi Node.js (untuk frontend nantinya)
node --version
# Expected: v20.x.x atau lebih baru
```

2. Konfigurasi identitas Git (penting agar commit tercatat atas nama Anda):

```bash
git config user.name "Nama Lengkap Anda"
git config user.email "email@uai.ac.id"

# Verifikasi konfigurasi
git config --list | grep user
# Expected:
# user.name=Nama Lengkap Anda
# user.email=email@uai.ac.id
```

3. Buat file konfigurasi Codespace. Buat folder `.devcontainer/` dan file `devcontainer.json`:

```bash
mkdir -p .devcontainer
```

4. Buat file `.devcontainer/devcontainer.json` dengan isi:

```json
{
  "name": "RPL Project Environment",
  "image": "mcr.microsoft.com/devcontainers/python:3.12",
  "features": {
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "postCreateCommand": "pip install -r requirements.txt",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.flake8",
        "esbenp.prettier-vscode",
        "bierner.markdown-mermaid"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "editor.formatOnSave": true
      }
    }
  },
  "forwardPorts": [5000]
}
```

**Expected Output:** File `.devcontainer/devcontainer.json` tersimpan. Saat Codespace dibuat ulang, environment akan otomatis terkonfigurasi sesuai spesifikasi ini.

**Estimasi waktu:** 15 menit

> **Troubleshooting:** Jika `python3 --version` tidak ditemukan, coba `python --version`. Di Codespace, biasanya keduanya tersedia. Jika ada error pada JSON, pastikan tidak ada koma (`,`) setelah elemen terakhir di setiap blok.

---

### Langkah 4: Buat Aplikasi Flask Hello World (20 menit)

**Mengapa:** Flask adalah micro-framework Python untuk web development. Membuat aplikasi sederhana sekarang memvalidasi bahwa environment berfungsi dan memberikan fondasi untuk proyek akhir semester.

**Instruksi:**

1. Install Flask:

```bash
pip install flask
```

2. Buat file `app.py`:

```python
# app.py - Aplikasi Flask pertama untuk proyek RPL
# Rekayasa Perangkat Lunak (IF2205) - Universitas Al Azhar Indonesia

from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    """Halaman utama - menampilkan informasi proyek."""
    return '''
    <h1>Selamat Datang di Proyek RPL!</h1>
    <p><strong>Tim:</strong> [Nama Tim Anda]</p>
    <p><strong>Anggota:</strong></p>
    <ul>
        <li>[Nama 1] - [NIM 1]</li>
        <li>[Nama 2] - [NIM 2]</li>
        <li>[Nama 3] - [NIM 3]</li>
    </ul>
    <p><strong>Mata Kuliah:</strong> Rekayasa Perangkat Lunak (IF2205)</p>
    <p><a href="/about">Tentang Proyek</a> | <a href="/api/status">API Status</a></p>
    '''

@app.route('/about')
def about():
    """Halaman tentang proyek."""
    return '''
    <h1>Tentang Proyek</h1>
    <p>Proyek ini dikembangkan sebagai bagian dari mata kuliah
    Rekayasa Perangkat Lunak di Universitas Al Azhar Indonesia.</p>
    <p><a href="/">Kembali</a></p>
    '''

@app.route('/api/status')
def status():
    """API endpoint - mengembalikan status aplikasi dalam format JSON."""
    return jsonify({
        "status": "running",
        "aplikasi": "RPL Project",
        "versi": "0.1.0",
        "timestamp": datetime.now().isoformat(),
        "tim": "[Nama Tim]"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

3. Jalankan aplikasi:

```bash
flask run --host=0.0.0.0 --port=5000
```

4. Codespace akan menampilkan notifikasi untuk membuka port 5000. Klik **"Open in Browser"**.

**Expected Output:**

- Halaman utama menampilkan "Selamat Datang di Proyek RPL!" beserta info tim
- URL `/about` menampilkan halaman tentang proyek
- URL `/api/status` mengembalikan JSON:

```json
{
  "status": "running",
  "aplikasi": "RPL Project",
  "versi": "0.1.0",
  "timestamp": "2026-04-11T10:30:00.000000",
  "tim": "[Nama Tim]"
}
```

**Estimasi waktu:** 20 menit

> **Troubleshooting:** Jika port 5000 tidak terbuka otomatis, buka tab **PORTS** di bagian bawah Codespace, cari port 5000, dan klik ikon globe untuk membuka di browser. Jika error `ModuleNotFoundError: No module named 'flask'`, jalankan ulang `pip install flask`.

---

### Langkah 5: Git Workflow - Add, Commit, Push (20 menit)

**Mengapa:** Menguasai Git workflow dasar adalah keterampilan wajib bagi software engineer. Setiap perubahan harus di-commit dengan pesan yang bermakna agar tim bisa memahami riwayat pengembangan.

**Instruksi:**

1. Hentikan Flask server (tekan `Ctrl+C` di terminal), lalu periksa status Git:

```bash
git status
```

**Expected Output:**
```
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .devcontainer/
        app.py

nothing added to commit but untracked files present
```

2. Buat file `requirements.txt`:

```bash
echo "flask==3.1.0" > requirements.txt
```

3. Stage dan commit semua file baru satu per satu (praktik yang baik -- jangan `git add .`):

```bash
# Commit 1: devcontainer
git add .devcontainer/devcontainer.json
git commit -m "chore: tambah konfigurasi devcontainer untuk Codespaces"

# Commit 2: aplikasi Flask
git add app.py
git commit -m "feat: buat aplikasi Flask Hello World dengan 3 route"

# Commit 3: dependencies
git add requirements.txt
git commit -m "chore: tambah requirements.txt dengan Flask dependency"
```

4. Push semua commit ke GitHub:

```bash
git push origin main
```

5. Verifikasi riwayat commit:

```bash
git log --oneline
```

**Expected Output:**
```
abc1234 chore: tambah requirements.txt dengan Flask dependency
def5678 feat: buat aplikasi Flask Hello World dengan 3 route
ghi9012 chore: tambah konfigurasi devcontainer untuk Codespaces
jkl3456 Initial commit
```

**Diskusi kelas (5 menit):** Mengapa kita membuat commit terpisah untuk setiap perubahan logis, bukan satu commit besar? Bagaimana ini membantu saat debugging di kemudian hari?

**Estimasi waktu:** 20 menit

> **Troubleshooting:** Jika `git push` gagal dengan error "permission denied", pastikan Codespace terhubung ke repository Anda (bukan fork orang lain). Jika diminta authentication, Codespace seharusnya sudah terotentikasi secara otomatis.

---

### Langkah 6: Eksplorasi Git - Branch dan Merge (20 menit)

**Mengapa:** Branching adalah fitur terpenting Git untuk kolaborasi tim. Setiap fitur dikembangkan di branch terpisah, lalu di-merge ke branch utama setelah selesai. Ini mencegah kode yang belum stabil masuk ke versi utama.

**Instruksi:**

1. Buat branch baru untuk fitur tim:

```bash
# Buat dan pindah ke branch baru
git checkout -b feature/halaman-tim

# Verifikasi branch aktif
git branch
# Expected:
#   main
# * feature/halaman-tim
```

2. Tambahkan route baru di `app.py` (tambahkan sebelum `if __name__`):

```python
@app.route('/tim')
def tim():
    """Halaman daftar anggota tim."""
    anggota = [
        {"nama": "Anggota 1", "nim": "20230001", "peran": "Product Owner"},
        {"nama": "Anggota 2", "nim": "20230002", "peran": "Scrum Master"},
        {"nama": "Anggota 3", "nim": "20230003", "peran": "Developer"},
    ]
    html = "<h1>Tim Proyek RPL</h1><table border='1'>"
    html += "<tr><th>Nama</th><th>NIM</th><th>Peran</th></tr>"
    for a in anggota:
        html += f"<tr><td>{a['nama']}</td><td>{a['nim']}</td><td>{a['peran']}</td></tr>"
    html += "</table><p><a href='/'>Kembali</a></p>"
    return html
```

3. Commit dan push branch:

```bash
git add app.py
git commit -m "feat: tambah halaman daftar anggota tim"
git push -u origin feature/halaman-tim
```

4. Merge branch ke main:

```bash
git checkout main
git merge feature/halaman-tim
git push origin main

# Lihat log untuk memastikan merge berhasil
git log --oneline --graph
```

**Expected Output:**
```
*   abc1234 Merge branch 'feature/halaman-tim'
|\
| * def5678 feat: tambah halaman daftar anggota tim
|/
* ghi9012 chore: tambah requirements.txt dengan Flask dependency
* ...
```

**Estimasi waktu:** 20 menit

> **Troubleshooting:** Jika terjadi merge conflict, buka file yang berkonflik (ditandai `<<<<<<<`), pilih versi yang benar, hapus penanda konflik, lalu `git add` dan `git commit`. Minta bantuan asisten jika ini terjadi pertama kali.

---

## Tantangan Tambahan

### Tantangan 1: Dasar
Tambahkan route `/mahasiswa` yang menampilkan daftar seluruh anggota tim dalam format HTML yang rapi (gunakan CSS inline sederhana). Route harus menampilkan foto placeholder, nama, NIM, dan bidang minat.

### Tantangan 2: Menengah
Buat branch `feature/api-mahasiswa`, implementasikan endpoint `/api/mahasiswa` yang mengembalikan data dalam format JSON, commit dengan conventional commits, lalu buat Pull Request (bukan merge langsung) ke `main` melalui GitHub web interface.

### Tantangan 3: Lanjutan
Konfigurasi `devcontainer.json` yang lebih lengkap: tambahkan `postStartCommand` untuk menjalankan Flask otomatis, tambahkan extension `GitHub Copilot`, dan buat `docker-compose.yml` sederhana yang mendefinisikan service `web` untuk aplikasi Flask.

---

## Refleksi & AI Usage Log

Sebelum meninggalkan lab, isi refleksi berikut di file `docs/refleksi-lab-01.md`:

1. **Apa yang saya pelajari hari ini?** (minimal 3 poin)
2. **Apa yang masih membingungkan?** (minimal 1 poin)
3. **Bagaimana ini relevan dengan proyek akhir?**

Jika menggunakan AI (ChatGPT, Copilot, Claude) selama lab, catat di **AI Usage Log**:

| Prompt yang Diberikan | Output AI | Modifikasi yang Dilakukan | Refleksi |
|----------------------|-----------|--------------------------|----------|
| (contoh prompt) | (ringkasan output) | (apa yang diubah/ditambah) | (apa yang dipelajari) |

---

## Checklist Penyelesaian

- [ ] Akun GitHub aktif dan terkonfigurasi
- [ ] Repository `rpl-proyek-[nama-tim]` dibuat dengan README, .gitignore, LICENSE
- [ ] Codespace berjalan dan environment terverifikasi (Python, Git, Node.js)
- [ ] File `devcontainer.json` tersimpan di `.devcontainer/`
- [ ] Flask Hello World berjalan di localhost:5000 dengan 3 route (`/`, `/about`, `/api/status`)
- [ ] Minimal 4 commits tercatat di `git log` dengan pesan conventional commits
- [ ] `requirements.txt` ada dan berisi dependency Flask
- [ ] Branch `feature/halaman-tim` dibuat, di-commit, dan di-merge ke `main`
- [ ] File refleksi `docs/refleksi-lab-01.md` terisi

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
