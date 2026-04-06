# Lab 01: Setup GitHub Codespaces dan Git Workflow

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 1 dari 13 |
| **Topik** | Setup Development Environment, Git Basics |
| **CPMK** | CPMK-1 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |

## Tujuan

1. **Membuat** GitHub account dan repository untuk proyek SE
2. **Mengkonfigurasi** GitHub Codespaces sebagai development environment
3. **Menerapkan** perintah Git dasar (init, add, commit, push, pull)
4. **Membuat** aplikasi Flask "Hello World" pertama

## Persiapan

- Akun GitHub (daftar di github.com)
- Browser modern (Chrome/Firefox)

## Langkah-langkah

### Langkah 1: Buat Repository (10 menit)
1. Login ke GitHub → klik "New repository"
2. Nama: `rpl-proyek-[nama-tim]`
3. Pilih Private, centang "Add README"
4. Pilih .gitignore: Python

### Langkah 2: Buka Codespace (10 menit)
1. Klik tombol hijau "Code" → tab "Codespaces"
2. Klik "Create codespace on main"
3. Tunggu environment siap

### Langkah 3: Konfigurasi Environment (15 menit)
```bash
# Verifikasi tools
python --version    # Python 3.x
git --version       # Git 2.x
node --version      # Node.js

# Install dependencies
pip install flask

# Konfigurasi Git
git config user.name "Nama Anda"
git config user.email "email@uai.ac.id"
```

### Langkah 4: Buat Flask Hello World (20 menit)
```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Selamat Datang di RPL!</h1><p>Nama: [Nama Anda]</p>'

@app.route('/about')
def about():
    return '<h1>Tentang</h1><p>Proyek Rekayasa Perangkat Lunak - UAI</p>'

if __name__ == '__main__':
    app.run(debug=True)
```

```bash
# Jalankan
flask run
# Buka browser: http://localhost:5000
```

### Langkah 5: Git Workflow (20 menit)
```bash
git status                    # Lihat perubahan
git add app.py                # Stage file
git commit -m "feat: tambah Flask Hello World"
git push origin main          # Push ke remote
git log --oneline             # Lihat history
```

### Langkah 6: Buat .gitignore dan requirements.txt (15 menit)
```bash
# requirements.txt
echo "flask==3.0.0" > requirements.txt

# Commit
git add requirements.txt
git commit -m "chore: tambah requirements.txt"
git push
```

## Tantangan Tambahan

1. Tambahkan route `/mahasiswa` yang menampilkan daftar anggota tim
2. Buat branch `feature/about-page`, commit perubahan, dan merge ke main
3. Coba `git diff` dan `git stash`

## Checklist Penyelesaian

- [ ] Repository GitHub berhasil dibuat
- [ ] Codespace berjalan dan terkonfigurasi
- [ ] Flask Hello World berjalan di localhost:5000
- [ ] Minimal 3 commits di git log
- [ ] requirements.txt dan .gitignore ada

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
