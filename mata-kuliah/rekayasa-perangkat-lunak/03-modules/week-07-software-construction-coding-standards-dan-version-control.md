# Minggu 7: Software Construction — Coding Standards dan Version Control

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 7 dari 16 |
| **Topik** | Clean Code, Code Smell, Refactoring, Git Flow, Code Review |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **CPMK** | CPMK-4 |
| **Sub-CPMK** | 4.1 (Clean code & coding standards), 4.2 (Git branching & code review) |
| **Durasi** | 150 menit (3 × 50 menit) |
| **Metode** | Ceramah, live coding, code review exercise |

## Tujuan Pembelajaran

1. **Menerapkan** prinsip Clean Code dan coding standards dalam penulisan kode (C3)
2. **Mengidentifikasi** code smells dan menerapkan teknik refactoring (C4)
3. **Menggunakan** Git branching strategy (Git Flow) dan pull request workflow (C3)
4. **Melakukan** code review yang konstruktif dan efektif (C4)

## Materi Pembelajaran

### 7.1 Clean Code Principles

#### Apa Itu Clean Code?
> "Clean code is code that is easy to understand and easy to change." — Robert C. Martin

**Prinsip Utama:**

| Prinsip | Buruk | Baik |
|---------|-------|------|
| Nama bermakna | `def p(x)` | `def hitung_total_peminjaman(user_id)` |
| Fungsi kecil | Fungsi 200 baris | Fungsi < 20 baris, satu tanggung jawab |
| Satu level abstraksi | Campur logika bisnis + SQL | Pisahkan ke service dan repository layer |
| Minimal komentar | Komentar menjelaskan "apa" | Kode self-documenting, komentar menjelaskan "mengapa" |
| DRY (Don't Repeat) | Copy-paste kode | Extract ke fungsi reusable |

#### Contoh Refactoring
```python
# BURUK: Sulit dibaca, banyak tanggung jawab
def process(data):
    result = []
    for d in data:
        if d['type'] == 'buku' and d['stok'] > 0:
            d['available'] = True
            result.append(d)
    # kirim email
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com')
    server.send_message(f"Found {len(result)} items")
    return result

# BAIK: Terpisah, mudah dibaca
def filter_buku_tersedia(daftar_buku):
    """Filter buku yang masih memiliki stok."""
    return [buku for buku in daftar_buku if buku['stok'] > 0]

def tandai_ketersediaan(daftar_buku):
    """Tandai setiap buku sebagai available."""
    for buku in daftar_buku:
        buku['available'] = True
    return daftar_buku

def kirim_notifikasi(jumlah_buku):
    """Kirim notifikasi tentang buku tersedia."""
    notification_service.send(f"Ditemukan {jumlah_buku} buku tersedia")
```

### 7.2 Code Smells

| Code Smell | Deskripsi | Refactoring |
|-----------|-----------|-------------|
| **Long Method** | Fungsi terlalu panjang (> 20 baris) | Extract Method |
| **Duplicate Code** | Kode yang sama di beberapa tempat | Extract Method / Class |
| **God Class** | Class yang melakukan terlalu banyak | Split into smaller classes |
| **Magic Number** | Angka tanpa konteks (if status == 3) | Extract Constant |
| **Feature Envy** | Method lebih banyak mengakses data class lain | Move Method |
| **Dead Code** | Kode yang tidak pernah dieksekusi | Delete |

### 7.3 Git Branching Strategy

#### Git Flow
```
main        ──●──────────────────────●──────────────── (production)
              │                      ▲
              │                      │ merge
develop     ──●──●──●──●──●──●──●──●── (integration)
                  │     ▲  │     ▲
                  │     │  │     │
feature/login  ───●──●──┘  │     │
                           │     │
feature/search ────────●──●──┘     │
                                   │
bugfix/typo    ────────────────●──┘
```

**Branch Types:**

| Branch | Tujuan | Naming |
|--------|--------|--------|
| `main` | Production-ready code | `main` |
| `develop` | Integration branch | `develop` |
| `feature/*` | Fitur baru | `feature/nama-fitur` |
| `bugfix/*` | Perbaikan bug | `bugfix/deskripsi-bug` |
| `release/*` | Persiapan release | `release/v1.0.0` |
| `hotfix/*` | Perbaikan urgent di production | `hotfix/critical-fix` |

#### Git Workflow Sehari-hari
```bash
# 1. Buat branch baru dari develop
git checkout develop
git pull origin develop
git checkout -b feature/pencarian-buku

# 2. Kerjakan perubahan
git add .
git commit -m "feat: tambah fitur pencarian buku berdasarkan judul"

# 3. Push dan buat Pull Request
git push -u origin feature/pencarian-buku
# Buat PR di GitHub: feature/pencarian-buku → develop

# 4. Setelah review & approve, merge via GitHub
```

#### Conventional Commits
```
<type>(<scope>): <description>

feat: fitur baru
fix: perbaikan bug
docs: perubahan dokumentasi
style: formatting (tidak mengubah logic)
refactor: refactoring kode
test: menambah/memperbaiki test
chore: maintenance (dependencies, config)
```

Contoh:
```
feat(auth): tambah login dengan Google OAuth
fix(search): perbaiki pencarian case-insensitive
docs(readme): update instruksi instalasi
```

### 7.4 Code Review

#### Tujuan Code Review
1. **Menemukan bug** sebelum masuk ke production
2. **Menjaga kualitas** kode tetap konsisten
3. **Knowledge sharing** antar anggota tim
4. **Mentoring** — junior belajar dari senior

#### Code Review Checklist

| Kategori | Yang Diperiksa |
|----------|----------------|
| **Correctness** | Apakah kode berjalan sesuai requirement? |
| **Design** | Apakah desain sesuai dengan arsitektur? |
| **Readability** | Apakah kode mudah dibaca dan dipahami? |
| **Testing** | Apakah ada unit test yang memadai? |
| **Security** | Apakah ada potensi kerentanan (SQL injection, XSS)? |
| **Performance** | Apakah ada N+1 query atau bottleneck? |

#### Etika Code Review
```
❌ "Kode ini jelek, siapa yang nulis?"
✅ "Bagaimana kalau kita extract method ini supaya lebih mudah di-test?"

❌ "Ini salah semua"
✅ "Saya punya saran untuk bagian ini — apakah kita bisa diskusi?"

❌ Membiarkan PR berhari-hari tanpa review
✅ Review dalam 24 jam, beri feedback yang actionable
```

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Membaca tentang Clean Code principles
- Setup Git repository untuk proyek kelompok

### In-class (120 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-30 menit | Clean Code: prinsip, naming, functions | Ceramah + contoh |
| 30-50 menit | Code Smells & Refactoring | Live coding |
| 50-80 menit | Git Flow: branching strategy & conventional commits | Demo + praktik |
| 80-110 menit | **Workshop**: Code review exercise — review PR partner | Workshop |
| 110-120 menit | **K2: Kuis Design & Construction** + wrap-up | Kuis |

### Post-class (15 menit)
- Mulai coding proyek akhir dengan Git Flow
- Persiapan UTS (Minggu 1-7)

## Penugasan

**T4: Collaborative Coding & Code Review** (2.5% nilai akhir)
- **Deliverable:** PR yang sudah di-review oleh minimal 1 anggota tim + Git log yang menunjukkan conventional commits
- **AI Policy:** AI diizinkan + AI Usage Log

**K2: Kuis Design & Construction** (3% nilai akhir)
- **Cakupan:** Minggu 5-7 (Arsitektur, UML, Clean Code, Git)
- **Durasi:** 20 menit, closed-book, tanpa AI

## Referensi

1. Martin, R. C. (2009). *Clean Code*. Prentice Hall.
2. Fowler, M. (2019). *Refactoring* (2nd ed.). Addison-Wesley.
3. Chacon, S. & Straub, B. (2014). *Pro Git* (2nd ed.). Apress.
4. Driessen, V. (2010). "A successful Git branching model."

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
