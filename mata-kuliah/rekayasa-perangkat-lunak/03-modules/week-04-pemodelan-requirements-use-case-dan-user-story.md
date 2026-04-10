# Minggu 4: Pemodelan Requirements — Use Case dan User Story

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 4 dari 16 |
| **Topik** | Use Case Diagram, User Stories, Acceptance Criteria, Product Backlog |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **CPMK** | CPMK-2 |
| **Sub-CPMK** | 2.3 (Use Case Diagram & Narrative), 2.4 (User Stories, INVEST, Backlog) |
| **Durasi** | 150 menit (3 × 50 menit) |
| **Metode** | Ceramah, workshop user story writing, backlog prioritization |

## Tujuan Pembelajaran

1. **Membuat** Use Case Diagram dan Use Case Narrative untuk memodelkan requirements (C3)
2. **Menulis** User Stories dengan kriteria INVEST (C3)
3. **Menulis** Acceptance Criteria dalam format Given-When-Then (C3)
4. **Menerapkan** teknik prioritisasi (MoSCoW) untuk Product Backlog (C3)

## Materi Pembelajaran

### 4.1 Use Case Modeling

#### Use Case Diagram
Elemen utama:
- **Actor** — siapa yang berinteraksi dengan sistem
- **Use Case** — apa yang bisa dilakukan
- **Relasi** — include (wajib), extend (opsional), generalization (inheritance)

Contoh: Sistem Antrian Puskesmas
```
    ┌─────────────┐     ┌──────────────────┐
    │   Pasien     │────▶│ Daftar Antrian    │
    └─────────────┘     └──────────────────┘
          │              ┌──────────────────┐
          └─────────────▶│ Lihat Status      │
                         └──────────────────┘
    ┌─────────────┐     ┌──────────────────┐
    │   Petugas    │────▶│ Panggil Pasien    │
    └─────────────┘     └──────────────────┘
          │              ┌──────────────────┐
          └─────────────▶│ Input Rekam Medis │
                         └──────────────────┘
```

### 4.2 User Stories

Format: **"As a [role], I want [feature], so that [benefit]"**

Contoh:
- "As a **mahasiswa**, I want **mencari buku berdasarkan judul**, so that **saya bisa menemukan buku yang dibutuhkan dengan cepat**"
- "As a **pustakawan**, I want **melihat daftar peminjaman yang terlambat**, so that **saya bisa mengirim reminder**"

#### INVEST Criteria

| Kriteria | Deskripsi |
|----------|-----------|
| **I**ndependent | Tidak bergantung pada story lain |
| **N**egotiable | Bisa didiskusikan dan diubah |
| **V**aluable | Memberikan nilai bagi pengguna |
| **E**stimable | Bisa diestimasi effort-nya |
| **S**mall | Cukup kecil untuk 1 sprint |
| **T**estable | Bisa diverifikasi hasilnya |

### 4.3 Acceptance Criteria (Given-When-Then)

```gherkin
Given pustakawan sudah login ke sistem
When pustakawan mencari buku dengan keyword "algoritma"
Then sistem menampilkan daftar buku yang mengandung kata "algoritma"
And setiap buku menampilkan judul, penulis, dan status ketersediaan
```

### 4.4 Product Backlog & Prioritisasi

#### MoSCoW Method

| Prioritas | Deskripsi | Contoh |
|-----------|-----------|--------|
| **Must** have | Wajib ada, sistem tidak bisa berjalan tanpa ini | Login, pendaftaran, pencarian buku |
| **Should** have | Penting tapi tidak kritis | Filter pencarian, notifikasi |
| **Could** have | Nice to have | Dark mode, export PDF |
| **Won't** have (now) | Tidak untuk rilis ini | Mobile app, AI recommendation |

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Review hasil T1 (SRS)
- Baca tentang User Stories dan INVEST criteria

### In-class (120 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-30 menit | Use Case Diagram & Narrative | Ceramah + contoh |
| 30-60 menit | User Stories & INVEST, Acceptance Criteria | Ceramah + demo |
| 60-90 menit | **Workshop**: Tulis 15 user stories untuk proyek kampus | Workshop kelompok |
| 90-110 menit | Product Backlog & MoSCoW prioritization | Praktik |
| 110-120 menit | **Kuis K1** preview & wrap-up | Diskusi |

### Post-class (15 menit)
- Selesaikan T2: User Story Mapping
- Persiapan Kuis K1

## Penugasan

**T2: User Story Mapping & Acceptance Criteria** (2.5% nilai akhir)
- **Deliverable:** 15 user stories (INVEST) + acceptance criteria + product backlog yang diprioritaskan
- **AI Policy:** AI diizinkan + AI Usage Log

**K1: Kuis Fondasi RPL & Requirements** (4% nilai akhir)
- **Cakupan:** Minggu 1-4
- **Durasi:** 30 menit, closed-book, tanpa AI

## Referensi

1. Cohn, M. (2004). *User Stories Applied*. Addison-Wesley.
2. Cockburn, A. (2001). *Writing Effective Use Cases*. Addison-Wesley.
3. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 4.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
