# Lab 07: Collaborative Coding dan Code Review

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 7 dari 13 |
| **Topik** | Git Flow, Conventional Commits, Pull Request, Code Review |
| **CPMK** | CPMK-4 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |

## Tujuan

1. **Menggunakan** Git Flow branching strategy
2. **Menerapkan** conventional commits dalam workflow
3. **Melakukan** code review yang konstruktif pada Pull Request

## Langkah-langkah

### Langkah 1: Setup Git Flow (15 menit)
```bash
git checkout main
git checkout -b develop
git push -u origin develop

# Buat feature branch
git checkout -b feature/pencarian-buku
```

### Langkah 2: Conventional Commits (20 menit)
Implementasi fitur sederhana dengan 5 commits:
```bash
git commit -m "feat(search): tambah form pencarian buku"
git commit -m "feat(search): implementasi API endpoint search"
git commit -m "test(search): tambah unit test pencarian"
git commit -m "docs(search): update API documentation"
git commit -m "style(search): fix formatting PEP 8"
```

### Langkah 3: Buat Pull Request (15 menit)
```bash
git push -u origin feature/pencarian-buku
```
Di GitHub: New Pull Request → feature/pencarian-buku → develop
- Judul: `feat: tambah fitur pencarian buku`
- Deskripsi: Apa yang berubah, cara testing, screenshots

### Langkah 4: Code Review (25 menit)
Review PR partner menggunakan checklist:

| Aspek | ✓/✗ | Komentar |
|-------|------|----------|
| Correctness | | Logika benar? |
| Readability | | Mudah dipahami? |
| Naming | | Nama variabel deskriptif? |
| Testing | | Ada test? |
| Security | | Ada SQL injection/XSS? |

Berikan minimal 3 review comments yang konstruktif.

### Langkah 5: Identifikasi Code Smells (15 menit)
Analisis kode sample dan temukan:
```python
# Kode dengan code smells
def process(d, t, u):
    if t == 1:
        d['s'] = 'active'
        # kirim email
        import smtplib
        # ... 50 baris kode email
    elif t == 2:
        d['s'] = 'inactive'
    return d
```
Identifikasi: Magic number, bad naming, long method, multiple responsibility.

## Tantangan Tambahan

1. Resolve merge conflict antara 2 feature branches
2. Setup branch protection rules di GitHub (require review)

## Checklist Penyelesaian

- [ ] Branch develop dan feature/ dibuat
- [ ] 5 conventional commits
- [ ] Pull Request dibuat dengan deskripsi lengkap
- [ ] Code review dilakukan (3+ comments)
- [ ] 3 code smells diidentifikasi dan di-refactor

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
