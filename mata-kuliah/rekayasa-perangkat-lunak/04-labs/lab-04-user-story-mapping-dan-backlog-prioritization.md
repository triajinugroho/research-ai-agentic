# Lab 04: User Story Mapping dan Backlog Prioritization

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 4 dari 13 |
| **Topik** | User Stories, INVEST, Acceptance Criteria, MoSCoW |
| **CPMK** | CPMK-2 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |

## Tujuan

1. **Menulis** 15 user stories dengan format dan kriteria INVEST
2. **Menulis** acceptance criteria dalam format Given-When-Then
3. **Menerapkan** MoSCoW prioritization dan story points estimation

## Langkah-langkah

### Langkah 1: Tulis 15 User Stories (30 menit)
Format: "As a [role], I want [feature], so that [benefit]"

Contoh untuk Sistem Perpustakaan:
1. As a mahasiswa, I want login dengan NIM, so that saya bisa akses sistem
2. As a mahasiswa, I want mencari buku berdasarkan judul, so that saya bisa menemukan buku
3. As a mahasiswa, I want meminjam buku online, so that tidak perlu antri
4. As a pustakawan, I want melihat peminjaman terlambat, so that bisa kirim reminder
5. ... (tulis 15 total)

Validasi setiap story dengan INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable.

### Langkah 2: Tulis Acceptance Criteria (20 menit)
Untuk 5 story teratas, tulis Given-When-Then:

```gherkin
Story: Pencarian buku berdasarkan judul

Scenario: Pencarian berhasil
  Given mahasiswa sudah login
  When mahasiswa mencari dengan keyword "algoritma"
  Then sistem menampilkan daftar buku mengandung "algoritma"
  And setiap buku menampilkan judul, penulis, stok

Scenario: Pencarian tanpa hasil
  Given mahasiswa sudah login
  When mahasiswa mencari dengan keyword "xyzabc"
  Then sistem menampilkan "Buku tidak ditemukan"
```

### Langkah 3: MoSCoW Prioritization (15 menit)
Kelompokkan 15 stories ke MoSCoW:
- **Must:** Login, Search, Peminjaman (sistem tidak jalan tanpa ini)
- **Should:** Notifikasi, Filter, Profil
- **Could:** Dark mode, Export PDF
- **Won't:** Mobile app, AI recommendation

### Langkah 4: Story Points Estimation (20 menit)
Gunakan Planning Poker (Fibonacci: 1, 2, 3, 5, 8, 13):
1. Baca story → diskusi → semua tunjukkan angka bersamaan
2. Jika perbedaan > 3 → diskusi ulang
3. Catat estimasi di tabel

| # | Story | Prioritas | Points |
|---|-------|-----------|--------|
| 1 | Login | Must | 3 |
| 2 | Search | Must | 5 |
| ... | ... | ... | ... |

## Tantangan Tambahan

1. Pecah 1 Epic menjadi 5 smaller stories
2. Buat Story Map (aktivitas → tasks → stories)

## Checklist Penyelesaian

- [ ] 15 user stories tertulis dan INVEST-validated
- [ ] Acceptance criteria GWT untuk 5 stories
- [ ] MoSCoW prioritization lengkap
- [ ] Story points untuk semua stories
- [ ] Semua tercatat di GitHub Issues

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
