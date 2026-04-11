# Lab 2: Git Branching dan Pull Request Workflow

## Informasi Praktikum

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Praktikum Rekayasa Perangkat Lunak (IF2206) |
| **Praktikum** | 2 dari 13 |
| **Topik** | Git Branching dan Pull Request Workflow |
| **CPMK** | CPMK-2 (Menerapkan version control dan kolaborasi tim menggunakan Git) |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |
| **Prasyarat** | Lab 1 selesai, repository `perpustakaan-uai` sudah ada dengan Flask app |

**Referensi Teori:**
- [IF2205 Minggu 2 — Proses dan Model Pengembangan Perangkat Lunak](../../../rekayasa-perangkat-lunak/03-modules/week-02-proses-dan-model-pengembangan-perangkat-lunak.md)
- [IF2205 Minggu 7 — Software Construction, Coding Standards & Version Control](../../../rekayasa-perangkat-lunak/03-modules/week-07-software-construction-coding-standards-dan-version-control.md)

---

## Tujuan Praktikum

Setelah menyelesaikan praktikum ini, mahasiswa mampu:

1. **Merancang** (*design* — C6) branching strategy yang terstruktur untuk proyek tim
2. **Menerapkan** (*apply* — C3) workflow Git branching (create, switch, merge) dengan conventional commits
3. **Membuat** (*create* — C6) Pull Request di GitHub lengkap dengan deskripsi dan self-review
4. **Menyelesaikan** (*resolve* — C4) merge conflict yang terjadi saat menggabungkan branch

---

## Konsep Singkat

### Mengapa Branching Penting?

Dalam pengembangan perangkat lunak tim, **branching** memungkinkan setiap developer bekerja secara paralel tanpa mengganggu kode orang lain. Bayangkan jika semua anggota tim mengedit file yang sama di branch yang sama secara bersamaan — chaos!

> Pelajari lebih lanjut tentang model pengembangan dan version control di [Modul IF2205 Minggu 2](../../../rekayasa-perangkat-lunak/03-modules/week-02-proses-dan-model-pengembangan-perangkat-lunak.md) dan [Modul IF2205 Minggu 7](../../../rekayasa-perangkat-lunak/03-modules/week-07-software-construction-coding-standards-dan-version-control.md).

### Git Flow Strategy

Kita akan menggunakan **simplified Git Flow** yang cocok untuk tim kecil:

```
main          ──●──────────────────●──────────────────●── (production-ready)
                │                  ↑                  ↑
                │                  │ merge PR          │ merge PR
                │                  │                  │
develop       ──●──●──────●───────●──●───────●───────●── (integration)
                   │      ↑          │       ↑
                   │      │ merge    │       │ merge
                   │      │          │       │
feature/books ────●──●──●─┘          │       │
                                     │       │
feature/search ─────────────────────●──●──●─┘
```

### Conventional Commits

Format standar untuk pesan commit yang **konsisten dan otomatis-parseable**:

```
<type>(<scope>): <description>

<body opsional>
```

| Type | Kapan Digunakan | Contoh |
|------|----------------|--------|
| `feat` | Fitur baru | `feat(books): add search endpoint` |
| `fix` | Perbaikan bug | `fix(auth): handle empty password` |
| `docs` | Dokumentasi | `docs: update API documentation` |
| `chore` | Maintenance | `chore: update dependencies` |
| `refactor` | Refactoring kode | `refactor(books): simplify query logic` |
| `test` | Menambah test | `test(books): add unit test for search` |
| `style` | Formatting | `style: fix indentation in app.py` |

### Pull Request Workflow

```
Developer                    GitHub                     Reviewer
    │                          │                          │
    │  1. Create branch        │                          │
    │  2. Write code           │                          │
    │  3. Commit & push        │                          │
    │─────────────────────────>│                          │
    │  4. Create Pull Request  │                          │
    │─────────────────────────>│  5. Notify reviewer      │
    │                          │─────────────────────────>│
    │                          │  6. Review code          │
    │                          │<─────────────────────────│
    │  7. Address feedback     │                          │
    │─────────────────────────>│                          │
    │                          │  8. Approve              │
    │                          │<─────────────────────────│
    │  9. Merge PR             │                          │
    │─────────────────────────>│                          │
    │  10. Delete branch       │                          │
    │─────────────────────────>│                          │
```

---

## Persiapan

Sebelum praktikum dimulai, pastikan:

- [ ] Lab 1 sudah selesai (repository `perpustakaan-uai` dengan Flask app)
- [ ] Codespace bisa dibuka dan terminal berfungsi
- [ ] Sudah membaca [Modul IF2205 Minggu 2](../../../rekayasa-perangkat-lunak/03-modules/week-02-proses-dan-model-pengembangan-perangkat-lunak.md)
- [ ] Memahami perintah dasar Git (add, commit, push) dari Lab 1

**Tools yang akan digunakan:**

| Tool | Fungsi |
|------|--------|
| Git | Version control, branching, merging |
| GitHub | Pull Request, code review |
| Terminal | Menjalankan perintah Git |

---

## Langkah-langkah

### Langkah 1: Setup Branching Strategy (10 menit)

**Mengapa langkah ini penting:**
Sebelum mulai coding, tim harus sepakat tentang **branching strategy**. Tanpa konvensi yang jelas, branch akan berantakan dan integrasi kode menjadi sulit. Ini mirip dengan menyepakati aturan lalu lintas sebelum berkendara.

**Instruksi:**

1. Buka Codespace untuk repository `perpustakaan-uai`
2. Pastikan Anda di branch `main` dan up-to-date:

```bash
git checkout main
git pull origin main
```

3. Buat branch `develop` dari `main`:

```bash
git checkout -b develop
git push -u origin develop
```

4. Verifikasi branch:

```bash
git branch -a
```

**Expected Output:**

```
* develop
  main
  remotes/origin/HEAD -> origin/main
  remotes/origin/develop
  remotes/origin/main
```

5. Buat file `CONTRIBUTING.md` yang mendokumentasikan branching strategy tim:

```bash
cat > CONTRIBUTING.md << 'EOF'
# Panduan Kontribusi — Perpustakaan Digital UAI

## Branching Strategy

Proyek ini menggunakan simplified Git Flow:

| Branch | Tujuan | Siapa yang merge |
|--------|--------|-----------------|
| `main` | Kode production-ready | Lead developer via PR |
| `develop` | Integrasi fitur terbaru | Tim via PR |
| `feature/*` | Pengembangan fitur baru | Developer |
| `fix/*` | Perbaikan bug | Developer |

## Alur Kerja

1. Buat feature branch dari `develop`: `git checkout -b feature/nama-fitur develop`
2. Kerjakan fitur di branch tersebut
3. Commit dengan format conventional commits
4. Push dan buat Pull Request ke `develop`
5. Minta review dari minimal 1 anggota tim
6. Setelah disetujui, merge dan hapus feature branch

## Conventional Commits

Format: `<type>(<scope>): <deskripsi>`

Contoh:
- `feat(books): add search by title endpoint`
- `fix(auth): validate empty email field`
- `docs: update API endpoint documentation`

## Aturan

- JANGAN commit langsung ke `main`
- Setiap fitur HARUS melalui Pull Request
- Minimal 1 reviewer sebelum merge
- Selesaikan semua merge conflict sebelum merge
EOF
```

```bash
git add CONTRIBUTING.md
git commit -m "docs: add contributing guidelines with branching strategy"
git push origin develop
```

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| "Branch already exists" | Gunakan `git checkout develop` tanpa `-b` |
| "Failed to push" | Jalankan `git pull origin develop` dulu, lalu push lagi |

---

### Langkah 2: Membuat Feature Branch dan Menambah Route Baru (15 menit)

**Mengapa langkah ini penting:**
Feature branch mengisolasi pekerjaan kita. Jika ada masalah, kita bisa dengan mudah membuang branch tanpa mengganggu kode yang sudah stabil di `develop`. Ini memberikan **safety net** untuk eksperimen.

**Instruksi:**

1. Buat feature branch dari `develop`:

```bash
git checkout develop
git checkout -b feature/books-detail
```

2. Verifikasi posisi branch:

```bash
git branch
```

Expected output:

```
  develop
* feature/books-detail
  main
```

3. Buka `app.py` dan tambahkan route baru di bawah route `/books` yang sudah ada. Tambahkan kode berikut **sebelum** blok `if __name__ == "__main__":`:

```python
@app.route("/books/<int:book_id>")
def book_detail(book_id):
    """Detail informasi satu buku berdasarkan ID."""
    buku = next(
        (b for b in DAFTAR_BUKU_SAMPLE if b["id"] == book_id),
        None
    )
    if buku is None:
        return jsonify({
            "error": "Buku tidak ditemukan",
            "book_id": book_id,
            "saran": "Cek daftar buku di /books"
        }), 404

    return jsonify({
        "buku": buku,
        "status_peminjaman": "Tersedia" if buku["tersedia"] else "Sedang dipinjam"
    })


@app.route("/books/search")
def search_books():
    """Pencarian buku berdasarkan query parameter."""
    from flask import request

    query = request.args.get("q", "").lower()
    if not query:
        return jsonify({
            "error": "Parameter pencarian 'q' diperlukan",
            "contoh": "/books/search?q=algorithm"
        }), 400

    hasil = [
        b for b in DAFTAR_BUKU_SAMPLE
        if query in b["judul"].lower() or query in b["penulis"].lower()
    ]

    return jsonify({
        "query": query,
        "total_hasil": len(hasil),
        "hasil": hasil
    })
```

4. Test aplikasi:

```bash
source venv/bin/activate
python app.py &
sleep 2
curl http://localhost:5000/books/1
curl http://localhost:5000/books/99
curl "http://localhost:5000/books/search?q=algorithm"
kill %1
```

**Expected Output untuk `/books/1`:**

```json
{
  "buku": {
    "id": 1,
    "isbn": "978-0262033848",
    "judul": "Introduction to Algorithms",
    "kategori": "Computer Science",
    "penulis": "Thomas H. Cormen et al.",
    "tersedia": true
  },
  "status_peminjaman": "Tersedia"
}
```

**Expected Output untuk `/books/99`:**

```json
{
  "book_id": 99,
  "error": "Buku tidak ditemukan",
  "saran": "Cek daftar buku di /books"
}
```

5. Commit perubahan dengan conventional commit:

```bash
git add app.py
git commit -m "feat(books): add book detail and search endpoints

- Add GET /books/<id> for individual book detail
- Add GET /books/search?q= for searching books by title or author
- Return 404 for non-existent book ID
- Return 400 when search query is missing"
```

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| IndentationError | Pastikan semua kode Python menggunakan 4 spasi |
| Route tidak ditemukan (404) | Pastikan kode ditambahkan **sebelum** `if __name__` |
| Server tidak mau berhenti | Jalankan `pkill -f "python app.py"` |

---

### Langkah 3: Push Branch dan Buat Pull Request (15 menit)

**Mengapa langkah ini penting:**
Pull Request (PR) adalah **gerbang kualitas** sebelum kode masuk ke branch utama. PR memungkinkan review, diskusi, dan dokumentasi perubahan. Di industri, tidak ada kode yang masuk ke production tanpa melalui PR.

**Instruksi:**

1. Push feature branch ke GitHub:

```bash
git push -u origin feature/books-detail
```

2. Buka GitHub di browser. Anda akan melihat notifikasi kuning:

```
feature/books-detail had recent pushes — Compare & pull request
```

3. Klik **Compare & pull request**

4. Isi form PR dengan template berikut:

**Title:** `feat(books): add book detail and search endpoints`

**Description** (paste ke kolom deskripsi):

```markdown
## Ringkasan

Menambahkan dua endpoint baru untuk fitur buku di Perpustakaan Digital UAI:
- `GET /books/<id>` — melihat detail satu buku
- `GET /books/search?q=` — mencari buku berdasarkan judul atau penulis

## Perubahan

- [x] Route `/books/<int:book_id>` dengan response detail buku
- [x] Route `/books/search` dengan query parameter
- [x] Error handling: 404 untuk buku tidak ditemukan, 400 untuk query kosong

## Cara Testing

1. Jalankan `python app.py`
2. Test: `curl http://localhost:5000/books/1` (seharusnya return detail buku)
3. Test: `curl http://localhost:5000/books/99` (seharusnya return 404)
4. Test: `curl "http://localhost:5000/books/search?q=algorithm"` (seharusnya return 1 hasil)

## Checklist

- [x] Kode berjalan tanpa error
- [x] Semua endpoint tested
- [x] Commit menggunakan conventional commit format
- [ ] Code review dari anggota tim
```

5. Pastikan:
   - **Base branch:** `develop` (BUKAN `main`)
   - **Compare branch:** `feature/books-detail`

6. Klik **Create pull request**

**Expected Output:**

Halaman Pull Request terbuka dengan:
- Title dan description yang terformat
- Tab **Files changed** menunjukkan perubahan di `app.py`
- Status "Open" dengan label merge target ke `develop`

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| Base branch menunjuk ke `main` | Klik dropdown "base" dan pilih `develop` |
| "There isn't anything to compare" | Pastikan sudah push branch: `git push -u origin feature/books-detail` |
| Conflict detected | Akan ditangani di Langkah 5 |

---

### Langkah 4: Self-Review dan Code Review (10 menit)

**Mengapa langkah ini penting:**
Code review menangkap bug, meningkatkan kualitas kode, dan menyebarkan pengetahuan di tim. Bahkan **self-review** (mereview kode sendiri) efektif mengurangi kesalahan — karena kita membaca kode dengan perspektif berbeda setelah selesai menulisnya.

**Instruksi:**

1. Di halaman PR, klik tab **Files changed**

2. Review setiap perubahan dengan checklist berikut:

**Self-Review Checklist:**

| No | Aspek | Pertanyaan | Status |
|----|-------|-----------|--------|
| 1 | Fungsionalitas | Apakah kode melakukan apa yang dimaksud? | |
| 2 | Error handling | Apakah error cases ditangani dengan baik? | |
| 3 | Naming | Apakah nama variabel dan fungsi deskriptif? | |
| 4 | Style | Apakah kode konsisten dengan style yang ada? | |
| 5 | Security | Apakah ada input yang tidak divalidasi? | |
| 6 | Documentation | Apakah docstring ada untuk setiap fungsi? | |

3. Tambahkan review comment di GitHub:
   - Hover di baris kode yang ingin dikomentari
   - Klik icon **+** biru di kiri nomor baris
   - Tulis komentar review, misalnya: "LGTM - error handling untuk book_id yang tidak ditemukan sudah baik"
   - Klik **Add single comment**

4. Setelah selesai review, klik tombol hijau **Review changes**, pilih **Approve**, dan tambahkan komentar:

```
Self-review selesai. Kode berfungsi dengan baik, error handling sudah ditangani, 
dan mengikuti conventional commit format.
```

**Expected Output:**

PR menampilkan:
- Minimal 1 review comment di baris kode
- Status "Approved" dari self-review

---

### Langkah 5: Simulasi dan Resolusi Merge Conflict (20 menit)

**Mengapa langkah ini penting:**
Merge conflict **pasti terjadi** dalam proyek tim. Kemampuan menyelesaikan conflict dengan benar adalah skill krusial. Lebih baik belajar di lingkungan praktikum daripada panik saat deadline proyek.

**Instruksi:**

1. Pertama, **merge PR dari Langkah 3** di GitHub:
   - Buka halaman PR
   - Klik **Merge pull request** > **Confirm merge**
   - Klik **Delete branch** untuk membersihkan feature branch

2. Kembali ke terminal Codespaces. Update local:

```bash
git checkout develop
git pull origin develop
```

3. Sekarang kita akan **simulasi conflict**. Buat dua branch yang mengedit baris yang sama:

```bash
# Branch A: mengubah deskripsi di route home
git checkout -b feature/update-home-message
```

4. Edit `app.py` — ubah pesan di route `home()`. Ganti baris:

```python
        "pesan": "Selamat datang di Perpustakaan Digital UAI!",
```

Menjadi:

```python
        "pesan": "Selamat datang di Sistem Perpustakaan Digital UAI - Melayani Civitas Akademika",
```

5. Commit dan push:

```bash
git add app.py
git commit -m "feat(home): update welcome message with full description"
git push -u origin feature/update-home-message
```

6. Kembali ke develop dan buat branch kedua:

```bash
git checkout develop
git checkout -b feature/update-home-version
```

7. Edit `app.py` — ubah baris yang SAMA. Ganti baris:

```python
        "pesan": "Selamat datang di Perpustakaan Digital UAI!",
```

Menjadi:

```python
        "pesan": "Selamat datang di Perpustakaan Digital UAI! [v0.2.0]",
```

8. Commit:

```bash
git add app.py
git commit -m "feat(home): add version number to welcome message"
```

9. Sekarang, merge branch pertama ke develop dulu:

```bash
git checkout develop
git merge feature/update-home-message
```

Output:

```
Updating abc1234..def5678
Fast-forward
 app.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

10. Lalu coba merge branch kedua — **CONFLICT!**

```bash
git merge feature/update-home-version
```

**Expected Output:**

```
Auto-merging app.py
CONFLICT (content): Merge conflict in app.py
Automatic merge failed; fix conflicts and then commit the result.
```

11. Lihat file yang conflict:

```bash
git status
```

Output:

```
Unmerged paths:
  both modified:   app.py
```

12. Buka `app.py` di editor. Cari bagian conflict (ditandai dengan `<<<<<<<`):

```python
<<<<<<< HEAD
        "pesan": "Selamat datang di Sistem Perpustakaan Digital UAI - Melayani Civitas Akademika",
=======
        "pesan": "Selamat datang di Perpustakaan Digital UAI! [v0.2.0]",
>>>>>>> feature/update-home-version
```

13. **Resolve conflict** — gabungkan kedua perubahan menjadi satu yang lebih baik:

```python
        "pesan": "Selamat datang di Sistem Perpustakaan Digital UAI - Melayani Civitas Akademika [v0.2.0]",
```

Hapus semua marker conflict (`<<<<<<<`, `=======`, `>>>>>>>`).

14. Selesaikan merge:

```bash
git add app.py
git commit -m "fix: resolve merge conflict in home welcome message

- Combined full description from feature/update-home-message
- Added version number from feature/update-home-version"
```

15. Push hasil merge:

```bash
git push origin develop
```

16. Bersihkan branch yang sudah tidak diperlukan:

```bash
git branch -d feature/update-home-message
git branch -d feature/update-home-version
git push origin --delete feature/update-home-message
```

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| Bingung bagian mana yang harus dipertahankan | `HEAD` = versi branch saat ini, bagian setelah `=======` = versi branch yang di-merge |
| Conflict masih ada setelah edit | Pastikan SEMUA marker (`<<<<<<<`, `=======`, `>>>>>>>`) sudah dihapus |
| `git merge --abort` | Gunakan ini jika ingin membatalkan merge dan mulai ulang |
| "Not possible to fast-forward" | Ini normal ketika ada divergent history, Git akan membuat merge commit |

---

### Langkah 6: Verifikasi Git History dan Clean Up (10 menit)

**Mengapa langkah ini penting:**
Git history yang bersih dan terstruktur memudahkan debugging di masa depan. Ketika terjadi bug, Anda bisa melacak kapan dan mengapa perubahan tertentu dibuat melalui commit history.

**Instruksi:**

1. Lihat git log yang rapi:

```bash
git log --oneline --graph --all
```

**Expected Output** (commit hash akan berbeda):

```
*   abc1234 (HEAD -> develop, origin/develop) fix: resolve merge conflict in home welcome message
|\
| * def5678 feat(home): add version number to welcome message
* | ghi9012 feat(home): update welcome message with full description
|/
* jkl3456 feat(books): add book detail and search endpoints
* mno7890 docs: add contributing guidelines with branching strategy
* pqr1234 (origin/main, main) docs: update README with project description
* stu5678 chore: update .gitignore for Python/Flask project
* vwx9012 feat: create initial Flask app with home, about, and books routes
* yza3456 chore: add devcontainer configuration
* bcd7890 Initial commit
```

2. Lihat statistik commit:

```bash
git shortlog -sn
```

Output menunjukkan jumlah commit per author.

3. Lihat semua branch (lokal dan remote):

```bash
git branch -a
```

Expected output (branch feature sudah dihapus):

```
* develop
  main
  remotes/origin/develop
  remotes/origin/main
```

4. Verifikasi aplikasi masih berjalan setelah semua merge:

```bash
source venv/bin/activate
python app.py &
sleep 2
curl http://localhost:5000/
kill %1
```

Pastikan pesan welcome yang digabungkan muncul dengan benar.

**Troubleshooting:**

| Masalah | Solusi |
|---------|--------|
| Branch remote masih ada | `git fetch --prune` untuk membersihkan referensi remote yang sudah dihapus |
| Git log terlalu panjang | Tambah `-10` untuk limit: `git log --oneline -10` |

---

### Langkah 7: Merge Develop ke Main via Pull Request (10 menit)

**Mengapa langkah ini penting:**
Di workflow profesional, `main` branch selalu berisi kode yang **production-ready**. Merge dari `develop` ke `main` dilakukan melalui PR untuk memastikan kualitas kode terjaga.

**Instruksi:**

1. Push develop terbaru:

```bash
git push origin develop
```

2. Di GitHub, buat Pull Request baru:
   - **Base:** `main`
   - **Compare:** `develop`
   - **Title:** `release: merge develop to main — Lab 2 completion`
   - **Description:**

```markdown
## Ringkasan

Merge semua perubahan dari Lab 2 ke main branch.

## Perubahan yang Termasuk

- Branching strategy documentation (CONTRIBUTING.md)
- Book detail endpoint (GET /books/<id>)
- Book search endpoint (GET /books/search?q=)
- Updated welcome message with version
- Resolved merge conflict exercise

## Testing

Semua endpoint telah ditest manual via curl.
```

3. Klik **Create pull request** > **Merge pull request** > **Confirm merge**

**Expected Output:**

Repository `main` branch sekarang berisi semua perubahan dari Lab 2, termasuk CONTRIBUTING.md dan route baru.

---

### Langkah 8: Dokumentasi Branching Workflow (10 menit)

**Mengapa langkah ini penting:**
Mendokumentasikan apa yang telah dilakukan memperkuat pemahaman dan menciptakan referensi untuk masa depan.

**Instruksi:**

Buat file `docs/git-workflow.md` sebagai dokumentasi:

```bash
mkdir -p docs

cat > docs/git-workflow.md << 'EOF'
# Git Workflow — Perpustakaan Digital UAI

## Branching Strategy

```
main (production)
  └── develop (integration)
        ├── feature/books-detail
        ├── feature/update-home-message
        └── feature/update-home-version
```

## Conventional Commit Types

| Type | Deskripsi |
|------|-----------|
| feat | Fitur baru |
| fix | Perbaikan bug |
| docs | Dokumentasi |
| chore | Maintenance |
| refactor | Refactoring |
| test | Testing |

## Workflow Summary

1. Buat feature branch dari `develop`
2. Code + commit (conventional commits)
3. Push + buat PR ke `develop`
4. Review + merge
5. Periodically merge `develop` ke `main`

## Lessons Learned

- Merge conflict terjadi ketika dua branch mengubah baris yang sama
- Resolve dengan memilih/menggabungkan perubahan secara manual
- Branch yang sudah di-merge sebaiknya dihapus untuk menjaga kebersihan
EOF
```

```bash
git checkout main
git pull origin main
git checkout -b docs/git-workflow
git add docs/git-workflow.md
git commit -m "docs: add git workflow documentation"
git push -u origin docs/git-workflow
```

Buat PR ke `main` di GitHub dan merge.

---

## Tantangan Tambahan

### Tantangan 1: Branch Protection Rules (Basic)

Di GitHub repository settings, aktifkan **branch protection rule** untuk branch `main`:
- Require pull request before merging
- Require at least 1 review approval

Dokumentasikan langkah-langkahnya di laporan.

### Tantangan 2: Git Aliases untuk Produktivitas (Intermediate)

Buat Git aliases untuk perintah yang sering digunakan:

```bash
git config --local alias.co "checkout"
git config --local alias.br "branch"
git config --local alias.st "status"
git config --local alias.lg "log --oneline --graph --all"
git config --local alias.cm "commit -m"
```

Coba gunakan: `git lg` seharusnya menampilkan log grafik yang rapi.

### Tantangan 3: Interactive Rebase untuk Clean History (Advanced)

Buat feature branch baru dengan 5 commit "WIP" (work in progress). Kemudian gunakan `git rebase` untuk menggabungkan (*squash*) 5 commit tersebut menjadi 1 commit yang rapi sebelum membuat PR. Ini adalah teknik yang sering digunakan di perusahaan teknologi untuk menjaga git history tetap bersih.

Petunjuk:
```bash
git rebase -i HEAD~5
# Ubah 'pick' menjadi 'squash' untuk commit yang ingin digabung
```

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

- [ ] Branch `develop` berhasil dibuat dari `main`
- [ ] File `CONTRIBUTING.md` ada di repository dengan branching strategy
- [ ] Feature branch `feature/books-detail` dibuat dan berisi 2 route baru
- [ ] Pull Request dibuat dengan deskripsi lengkap (template PR)
- [ ] Self-review dilakukan dengan minimal 1 review comment di PR
- [ ] PR berhasil di-merge ke `develop`
- [ ] Merge conflict berhasil disimulasikan dan diselesaikan
- [ ] Git log menunjukkan minimal 5 conventional commits yang rapi
- [ ] Branch yang sudah di-merge telah dihapus (clean up)
- [ ] Develop berhasil di-merge ke `main` via PR
- [ ] Semua perubahan sudah di-push ke GitHub
- [ ] Dokumentasi workflow ada di `docs/git-workflow.md`

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
