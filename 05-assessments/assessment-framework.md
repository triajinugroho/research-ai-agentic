# Kerangka Penilaian (Assessment Framework)

## Mata Kuliah: Analisis Data Statistik
### Prodi Informatika — UAI — Semester Genap 2025/2026

---

## 1. Filosofi Penilaian

Penilaian pada mata kuliah ini dirancang berdasarkan prinsip **Authentic Assessment** yang sesuai dengan era AI:

- **Menilai pemahaman, bukan hafalan** — Mahasiswa dinilai berdasarkan kemampuan menerapkan dan menginterpretasi, bukan menghafal rumus
- **Proses sama pentingnya dengan produk** — Dokumentasi proses analisis (termasuk AI usage) dinilai
- **Diversifikasi metode** — Kombinasi exam (tanpa AI), tugas (dengan AI), dan proyek (kolaborasi human-AI)
- **Umpan balik formatif** — Kuis dan tugas memberikan feedback untuk perbaikan, bukan hanya nilai

---

## 2. Komponen Penilaian

| Komponen | Bobot | Jenis | AI Policy |
|----------|-------|-------|-----------|
| **Tugas Mingguan** (6x) | 15% | Individu, take-home | AI diizinkan + documented |
| **Kuis** (3x) | 10% | Individu, in-class | Closed-book, tanpa AI |
| **UTS** | 20% | Individu, in-class | Closed-book, tanpa AI |
| **Proyek Akhir** | 25% | Kelompok (2-3), take-home | AI sebagai co-analyst + documented |
| **UAS** | 25% | Individu, in-class | Closed-book + 1 lembar catatan |
| **Partisipasi** | 5% | Individu, ongoing | N/A |

---

## 3. Detail per Komponen

### 3.1 Tugas Mingguan (15%)

**Frekuensi:** 6 tugas selama semester (Minggu 2, 3, 5, 7, 9, 11)

**Format:** Jupyter Notebook yang dikumpulkan via LMS UAI

**Rubrik umum:** Setiap tugas dinilai pada 4 dimensi:
1. **Teknis** (25%) — Ketepatan perhitungan dan kode
2. **Interpretasi** (30%) — Kemampuan menjelaskan hasil dalam konteks
3. **Kode** (25%) — Kualitas, kebersihan, dan dokumentasi kode Python
4. **Presentasi** (20%) — Struktur notebook dan narrative flow

**Skala:** 0-100 per tugas, dirata-rata untuk 15%

### 3.2 Kuis (10%)

**Frekuensi:** 3 kuis (Minggu 4, 7, 12)

**Format:** 30 menit, kertas, closed-book

**Tipe soal:** Pilihan ganda (konseptual) + soal singkat (hitungan & interpretasi)

**Tujuan:** Memastikan pemahaman konseptual tanpa bantuan AI

### 3.3 UTS (20%)

**Waktu:** Minggu 8, 100 menit

**Format:** Closed-book, written exam

**Cakupan:** Minggu 1-7 (CPMK 1-4)

**Struktur soal:**
| Tipe | Bobot | Deskripsi |
|------|-------|-----------|
| Pilihan Ganda | 20% | 10 soal konseptual |
| Hitungan | 40% | 3-4 soal step-by-step |
| Interpretasi Output | 20% | Diberikan output Python, interpretasikan |
| Essay Analisis | 20% | Desain analisis untuk skenario tertentu |

### 3.4 Proyek Akhir (25%)

**Periode:** Minggu 9-15

**Format:** Kelompok 2-3 orang

**Deliverables:**
1. Jupyter Notebook (40%)
2. Laporan tertulis 3-5 halaman (30%)
3. Presentasi 10 menit (20%)
4. AI Usage Log (10%)

**Rubrik detail:** Lihat `project-guidelines.md`

### 3.5 UAS (25%)

**Waktu:** Minggu 16, 100 menit

**Format:** Closed-book + 1 lembar A4 catatan pribadi (ditulis tangan)

**Cakupan:** Minggu 9-15 (penekanan CPMK 5-7), komprehensif

**Struktur soal:**
| Tipe | Bobot | Deskripsi |
|------|-------|-----------|
| Pilihan Ganda | 15% | 8 soal konseptual |
| Hitungan & Interpretasi | 30% | 3 soal (regresi, ANOVA, chi-square) |
| Interpretasi Output | 25% | Output ML/regresi, interpretasikan |
| Essay Desain Analisis | 30% | Diberikan masalah riil, desain analisis end-to-end |

### 3.6 Partisipasi & Etika AI (5%)

| Komponen | Bobot | Deskripsi |
|----------|-------|-----------|
| Kehadiran | 2% | Minimal 75% kehadiran, bonus untuk 100% |
| Kontribusi diskusi | 1.5% | Aktif bertanya/menjawab di kelas atau forum LMS |
| Refleksi AI Ethics | 1.5% | 2x refleksi singkat (Minggu 7 & 14) tentang pengalaman menggunakan AI |

---

## 4. Rubrik Universal (4-Point Scale)

Semua tugas menggunakan skala 4 poin yang dikonversi ke persentase:

| Skor | Predikat | Deskripsi | Konversi |
|------|----------|-----------|----------|
| 4 | **Sangat Baik (A)** | Melebihi ekspektasi, menunjukkan pemahaman mendalam dan kemampuan kritis | 85-100% |
| 3 | **Baik (B)** | Memenuhi ekspektasi, pemahaman solid dengan minor gaps | 70-84% |
| 2 | **Cukup (C)** | Memenuhi sebagian ekspektasi, pemahaman dasar ada tapi banyak gap | 55-69% |
| 1 | **Kurang (D/E)** | Tidak memenuhi ekspektasi minimum, pemahaman sangat terbatas | 0-54% |

---

## 5. Peta CPMK — Asesmen — Bloom's

| CPMK | Bloom's | Asesmen Formatif | Asesmen Sumatif |
|------|---------|-------------------|-----------------|
| CPMK-1 (Peran statistika & etika) | C2 | Lab 01, diskusi | T1, K1, UTS |
| CPMK-2 (Deskriptif & visualisasi) | C3 | Lab 02, Lab 03 | T1, T2, K1, UTS |
| CPMK-3 (Probabilitas & distribusi) | C3 | Lab 04, Lab 05 | T3, K1, UTS |
| CPMK-4 (Inferensi statistik) | C4 | Lab 06, Lab 07 | T4, K2, UTS |
| CPMK-5 (Korelasi & regresi) | C4-C5 | Lab 09, Lab 10 | T5, K3, UAS |
| CPMK-6 (ANOVA & non-parametrik) | C4 | Lab 11, Lab 12 | T6, K3, UAS |
| CPMK-7 (AI-augmented analysis) | C5-C6 | Lab 13, Lab 14 | Proyek, UAS |

---

## 6. Strategi Anti-Plagiarisme di Era AI

### 6.1 Prinsip

Bukan tentang **mencegah** penggunaan AI, tapi tentang **memastikan pemahaman genuine** di balik pekerjaan yang dikumpulkan.

### 6.2 Mekanisme

| Strategi | Implementasi |
|----------|-------------|
| **Diversifikasi asesmen** | 50% in-class (tanpa AI) + 50% take-home (dengan AI) |
| **AI Usage Documentation** | Wajib dokumentasi prompt & refleksi untuk setiap tugas |
| **Spot check** | Random oral questioning di kelas: "Jelaskan kode di baris X" |
| **Unique datasets** | Setiap mahasiswa menganalisis subset data yang berbeda |
| **Process-based grading** | Menilai git history / notebook revision, bukan hanya final product |
| **Peer review** | Mahasiswa saling review proyek — sulit jika tidak memahami materi |
| **Refleksi tertulis** | "Apa yang paling sulit? Bagaimana AI membantu/tidak membantu?" |

### 6.3 Panduan untuk Mahasiswa

**Boleh:**
- Menggunakan AI untuk debugging kode
- Meminta AI menjelaskan konsep yang sulit
- Menggunakan AI untuk brainstorm pendekatan analisis
- Copy-paste kode dari AI **jika dipahami dan didokumentasikan**

**Tidak boleh:**
- Submit output AI tanpa modifikasi dan pemahaman
- Menggunakan AI saat kuis dan ujian
- Claim pekerjaan AI sebagai 100% pekerjaan sendiri
- Tidak mendokumentasikan penggunaan AI

---

## 7. Feedback & Improvement Cycle

```
Tugas dikumpulkan → Dinilai (maks 7 hari) → Feedback tertulis
     ↓                                            ↓
Mahasiswa review feedback                 Revisi jika perlu (bonus)
     ↓
Kuis (cek pemahaman tanpa AI)
     ↓
Loop ke tugas berikutnya
```

Mahasiswa yang **merevisi tugas** berdasarkan feedback (dalam 1 minggu setelah feedback) mendapat **bonus 5% dari nilai tugas tersebut**.

---

*Dokumen ini merupakan bagian dari RPS mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia.*
