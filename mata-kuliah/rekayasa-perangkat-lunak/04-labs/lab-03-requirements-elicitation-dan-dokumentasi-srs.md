# Lab 03: Requirements Elicitation dan Dokumentasi SRS

## Informasi Lab

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Rekayasa Perangkat Lunak (IF2205) |
| **Lab** | 3 dari 13 |
| **Topik** | Interview Elicitation, SRS IEEE 830 |
| **CPMK** | CPMK-2 |
| **Durasi** | 100 menit |
| **Platform** | GitHub Codespaces |

## Tujuan

1. **Menerapkan** teknik interview untuk elicitation requirements
2. **Membedakan** functional dan non-functional requirements
3. **Menyusun** dokumen SRS sesuai IEEE 830

## Persiapan

- Partner untuk role-play interview
- Template SRS (lihat Lampiran D buku ajar)

## Langkah-langkah

### Langkah 1: Role-Play Interview (25 menit)
Berpasangan — satu sebagai **analyst**, satu sebagai **stakeholder** (pustakawan):

Contoh pertanyaan:
1. Bagaimana proses peminjaman buku saat ini?
2. Apa masalah utama yang sering terjadi?
3. Fitur apa yang paling Anda butuhkan?
4. Berapa banyak buku dan pengguna yang harus didukung?
5. Apakah ada aturan khusus (batas pinjam, denda)?

Catat hasil interview di Markdown.

### Langkah 2: Identifikasi Requirements (20 menit)
Dari hasil interview, tulis:

**10 Functional Requirements:**
```markdown
| ID | Deskripsi | Prioritas |
|----|-----------|-----------|
| FR-01 | Sistem harus memungkinkan mahasiswa login dengan NIM | Must |
| FR-02 | Sistem harus menampilkan katalog buku dengan pencarian | Must |
| ...  | ... | ... |
```

**5 Non-Functional Requirements:**
```markdown
| ID | Kategori | Deskripsi | Metrik |
|----|----------|-----------|--------|
| NFR-01 | Performance | Halaman loading < 3 detik | Response time |
| ...  | ... | ... | ... |
```

### Langkah 3: Tulis SRS (30 menit)
Buat file `docs/srs.md` mengikuti template IEEE 830:
1. Pendahuluan (tujuan, ruang lingkup, definisi)
2. Deskripsi Umum (perspektif produk, karakteristik pengguna)
3. Kebutuhan Spesifik (FR, NFR, interface requirements)

### Langkah 4: Validasi (15 menit)
Tukarkan SRS dengan tim lain. Gunakan checklist:
- [ ] Setiap requirement jelas (tidak ambigu)?
- [ ] Setiap requirement testable?
- [ ] Requirement konsisten (tidak bertentangan)?
- [ ] Requirement lengkap?

## Tantangan Tambahan

1. Tambahkan Use Case Narrative untuk 2 use case utama
2. Buat interview script untuk stakeholder kedua (admin)

## Checklist Penyelesaian

- [ ] Hasil interview tercatat
- [ ] 10 FR + 5 NFR terdokumentasi
- [ ] SRS.md mengikuti struktur IEEE 830
- [ ] Validasi checklist terisi
- [ ] File di-commit dan push ke repository

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
