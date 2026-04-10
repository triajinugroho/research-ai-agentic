# Minggu 3: Requirements Engineering dan Analisis Kebutuhan

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak |
| **Kode** | IF2205 |
| **Minggu** | 3 dari 16 |
| **Topik** | Requirements Engineering: Elicitation, Analysis, Specification, Validation |
| **Dosen** | Tri Aji Nugroho, S.T., M.T. |
| **Program Studi** | Informatika, Universitas Al Azhar Indonesia |
| **Semester** | Genap 2025/2026 |
| **CPMK** | CPMK-2 |
| **Sub-CPMK** | 2.1 (Teknik elicitation), 2.2 (Menyusun SRS IEEE 830) |
| **Durasi** | 150 menit (3 × 50 menit) |
| **Metode** | Ceramah, role-play elicitation, praktik menulis SRS |

## Tujuan Pembelajaran

1. **Menerapkan** teknik elicitation (interview, observation, prototyping) untuk mengumpulkan kebutuhan (C3)
2. **Membedakan** functional dan non-functional requirements (C2)
3. **Menyusun** dokumen SRS sesuai standar IEEE 830/ISO 29148 (C3)
4. **Menerapkan** teknik validasi requirements (C3)

## Materi Pembelajaran

### 3.1 Pengantar Requirements Engineering

**Fakta:** 60% kegagalan proyek software disebabkan oleh requirements yang buruk (Standish Group).

Proses RE:
```
Elicitation → Analysis → Specification → Validation → Management
(Kumpulkan)   (Analisis)  (Dokumentasi)  (Validasi)   (Kelola perubahan)
```

### 3.2 Teknik Elicitation

| Teknik | Deskripsi | Kapan Digunakan |
|--------|-----------|-----------------|
| **Interview** | Tanya jawab langsung dengan stakeholder | Awal proyek, requirements inti |
| **Questionnaire** | Survey tertulis untuk banyak stakeholder | Banyak stakeholder, konfirmasi |
| **Observation** | Mengamati pengguna bekerja | Proses bisnis yang kompleks |
| **Prototyping** | Membuat mock-up untuk feedback | UI/UX, requirements tidak jelas |
| **Brainstorming** | Diskusi terbuka untuk ide | Inovasi, fase awal |
| **Document Analysis** | Mempelajari dokumen existing | Sistem pengganti |

### 3.3 Functional vs Non-Functional Requirements

**Functional Requirements (FR):** Apa yang sistem *harus lakukan*
- FR-01: Sistem harus memungkinkan pengguna mendaftar dengan email dan password
- FR-02: Sistem harus menampilkan daftar buku yang tersedia

**Non-Functional Requirements (NFR):** *Bagaimana* sistem harus bekerja
- NFR-01: Halaman harus loading dalam < 3 detik (Performance)
- NFR-02: Sistem harus mendukung 1000 pengguna bersamaan (Scalability)
- NFR-03: Data pengguna harus dienkripsi (Security)

### 3.4 Software Requirements Specification (SRS)

Struktur SRS (IEEE 830):

```
1. Pendahuluan
   1.1 Tujuan
   1.2 Ruang Lingkup
   1.3 Definisi dan Akronim
   1.4 Referensi
2. Deskripsi Umum
   2.1 Perspektif Produk
   2.2 Fungsi Produk
   2.3 Karakteristik Pengguna
   2.4 Batasan
   2.5 Asumsi dan Dependensi
3. Kebutuhan Spesifik
   3.1 Functional Requirements
   3.2 Non-Functional Requirements
   3.3 External Interface Requirements
```

### 3.5 Validasi Requirements

Checklist validasi:
- [ ] Apakah requirement **jelas** (tidak ambigu)?
- [ ] Apakah requirement **testable** (bisa diuji)?
- [ ] Apakah requirement **consistent** (tidak bertentangan)?
- [ ] Apakah requirement **complete** (mencakup semua kebutuhan)?
- [ ] Apakah requirement **feasible** (bisa diimplementasi)?

## Kegiatan Pembelajaran

### Pre-class (15 menit)
- Membaca template SRS di lampiran buku ajar
- Memikirkan: "Apa saja kebutuhan sistem perpustakaan kampus?"

### In-class (120 menit)

| Waktu | Aktivitas | Metode |
|-------|-----------|--------|
| 0-30 menit | Pengantar RE, teknik elicitation | Ceramah interaktif |
| 30-60 menit | **Role-play Elicitation**: Interview stakeholder perpustakaan | Role-play kelompok |
| 60-90 menit | Menulis FR dan NFR, struktur SRS | Ceramah + praktik |
| 90-110 menit | Hands-on: Mulai menulis SRS untuk Sistem Perpustakaan | Praktik individu |
| 110-120 menit | Validasi requirements & preview T1 | Diskusi |

### Post-class (15 menit)
- Lanjutkan menulis SRS untuk T1

## Penugasan

**T1: Menulis SRS untuk Sistem Informasi Perpustakaan Kampus** (2.5% nilai akhir)
- **Deadline:** Minggu 4 (sebelum kelas)
- **Format:** Markdown, submit via LMS
- **Minimum:** 10 functional requirements, 5 non-functional requirements
- **AI Policy:** AI diizinkan + wajib AI Usage Log

## Referensi

1. Wiegers, K. E. & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press.
2. IEEE Std 830-1998. *Recommended Practice for Software Requirements Specifications*.
3. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 4-5.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
