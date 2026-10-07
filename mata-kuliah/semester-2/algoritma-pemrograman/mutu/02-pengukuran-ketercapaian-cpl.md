---
id: uai-inf101-mutu-02
tipe: mutu
judul: Pengukuran Ketercapaian CPL — Algoritma dan Pemrograman
kode_mk: INF-101
nama_mk: Algoritma dan Pemrograman
prodi: Informatika
siklus: 2025-2026-genap
kriteria_lam: [2-relevansi-pendidikan, 5-akuntabilitas]
tahap_ppepp: [P1-penetapan, E-evaluasi]
versi: 1.0
status: draft
diperbarui: 2026-09-05
---

# Pengukuran Ketercapaian CPL — INF-101

> Menjawab pertanyaan: **bagaimana kita mengukur, dan dari mana angkanya berasal.**
>
> Tanpa berkas ini, pernyataan "CPL tercapai" hanyalah klaim. Inilah artefak yang menjadikan ketercapaian CPL **dapat dihitung dan ditelusuri** — inti kriteria 5 (Akuntabilitas) LAM-INFOKOM 2.0.

## 1. Definisi dan Rumus

| Besaran | Rumus |
|---|---|
| **Skor Sub-CPMK** | Rata-rata skor seluruh butir asesmen yang ditandai Sub-CPMK tersebut |
| **Nilai CPMK** | `Σ (bobot asesmen × skor asesmen pada CPMK itu) ÷ Σ bobot` |
| **Nilai CPL** | Rata-rata tertimbang nilai CPMK yang mengampu CPL tersebut |
| **Ketercapaian kelas** | Persentase mahasiswa yang memperoleh nilai CPMK ≥ ambang |

**Prasyarat teknis:** setiap butir soal pada kuis, UTS, dan UAS **wajib ditandai kode Sub-CPMK**. Tanpa penandaan itu, rumus di atas tidak dapat dijalankan. Penandaan dilakukan pada kisi-kisi dan naskah ujian.

## 2. Instrumen Pengukuran

| CPMK | Sub-CPMK | Asesmen pengukur | Bobot | Indikator ketercapaian |
|---|---|---|:-:|---|
| **CPMK-1** | 1.1 – 1.4 | `ASM-UTS` (blok A), `ASM-UAS`, `ASM-PAR` | 30% · 40% · 10% | Mampu mendefinisikan algoritma, menjelaskan empat pilar CT, menyusun *pseudocode*/*flowchart*, dan menjalankan program di Colab |
| **CPMK-2** | 2.1 – 2.4 | `ASM-UTS` (blok B), `ASM-UAS`, `ASM-PAR` | 30% · 40% · 10% | Mampu memilih tipe data yang tepat, menerapkan operator, dan membangun program interaktif |
| **CPMK-3** | 3.1 – 3.8 | **`ASM-K1`**, `ASM-UTS` (blok C), `ASM-UAS`, `ASM-PAR` | 7% · 30% · 40% · 10% | Mampu menulis seleksi dan perulangan yang benar secara sintaks dan logika, termasuk *nested* |
| **CPMK-4** | 4.1 – 4.8 | **`ASM-K2`**, `ASM-UTS` (blok D), `ASM-UAS`, `ASM-PAR` | 7% · 30% · 40% · 10% | Mampu membangun fungsi modular ber-*docstring* dan mengolah teks serta berkas |
| **CPMK-5** | 5.1 – 5.7 | **`ASM-K2`**, `ASM-UTS` (blok E), `ASM-UAS`, `ASM-PAR` | 7% · 30% · 40% · 10% | Mampu memanipulasi koleksi dan **memberi justifikasi** pemilihan struktur data |
| **CPMK-6** | 6.1 – 6.12 | **`ASM-K3`**, `ASM-UAS`, `ASM-PAR` | 6% · 40% · 10% | Mampu mengimplementasikan dan men-*trace* algoritma pencarian, pengurutan, dan rekursi serta membandingkan kompleksitasnya |
| **CPMK-7** | 7.1 – 7.12 | `ASM-UAS`, `ASM-PAR` | 40% · 10% | Mampu menentukan Big-O, mengoptimasi kode, menyusun *prompt* efektif, dan mengisi AI Usage Log secara jujur |

**Catatan ranah non-kognitif.** Sub-CPMK beranah **A** (7.5, 7.8, 7.11, 7.12) diukur melalui kelengkapan dan kejujuran AI Usage Log serta kualitas telaah sejawat, bukan melalui soal pilihan ganda. Sub-CPMK beranah **P** diukur melalui unjuk kerja koding — sebagian besar berlangsung di INF-102 dan hasilnya dirujuk silang ke sini.

## 3. Ambang dan Kategori

### 3.1 Kategori ketercapaian individu

| Rentang nilai CPMK | Kategori |
|---|---|
| ≥ 85 | Sangat Tercapai |
| 70 – 84 | Tercapai |
| 55 – 69 | Perlu Perbaikan |
| < 55 | Tidak Tercapai |

### 3.2 Ambang ketercapaian kelas

> **Usulan:** sebuah CPMK dinyatakan **tercapai di tingkat kelas** bila **≥ 70% mahasiswa memperoleh nilai CPMK ≥ 70**.

🔲 **Status: usulan.** Penetapan resmi menunggu SK program studi. Nomor SK dicatat pada §5 setelah terbit.

CPMK yang tidak memenuhi ambang **wajib** memicu tindakan pada tahap Pengendalian atau Peningkatan (`03-ppepp-cqi.md`).

## 4. Lembar Hasil per Siklus

Diisi pada tahap **Evaluasi** (minggu 17). Kosong pada awal siklus bukan kelemahan — ia menunjukkan siklus baru saja dimulai.

### Siklus 2025-2026-genap

| CPMK | n | Rata-rata | % ≥ ambang | Status | Catatan |
|---|:-:|:-:|:-:|:-:|---|
| CPMK-1 | | | | ⏳ | |
| CPMK-2 | | | | ⏳ | |
| CPMK-3 | | | | ⏳ | |
| CPMK-4 | | | | ⏳ | |
| CPMK-5 | | | | ⏳ | |
| CPMK-6 | | | | ⏳ | |
| CPMK-7 | | | | ⏳ | |

### Rekapitulasi CPL

| CPL | CPMK pengampu | Nilai CPL | Status |
|---|---|:-:| :-: |
| **CPL03** | CPMK-1, 2, 5, 6 | | ⏳ |
| **CPL07** | CPMK-1, 3, 6 | | ⏳ |
| **CPL08** | CPMK-2, 3, 4, 5, 6, 7 | | ⏳ |
| **CPLUAI1** | CPMK-7 | | ⏳ |
| **CPLUAI3** | CPMK-7 | | ⏳ |

Legenda status: ⏳ belum dievaluasi · ✅ tercapai · ⚠️ perlu perbaikan · ❌ tidak tercapai.

## 5. Sumber Data dan Keterlacakan

| Aspek | Ketentuan |
|---|---|
| **Nilai mentah** | Disimpan pada LMS/Google Classroom mata kuliah, per butir soal |
| **Penandaan Sub-CPMK** | Tercantum pada `../04-assessments/kisi-kisi-uts.md`, `kisi-kisi-uas.md`, dan naskah ujian |
| **Penghitung** | Dosen pengampu |
| **Waktu penghitungan** | Minggu ke-17, setelah nilai akhir terkumpul |
| **Penelaah** | Dosen sejawat rumpun keilmuan (telaah sejawat = bukti kriteria 1) |
| **SK penetapan ambang** | 🔲 belum terbit |
| **Rekognisi (RPL)** | Bila ada mahasiswa jalur RPL, sumber bukti dan hasil asesmennya dicatat pada baris terpisah tabel §4 |

**Prinsip keterlacakan:** dari nilai akhir seorang mahasiswa harus dapat ditelusuri mundur ke butir soal, lalu ke Sub-CPMK, lalu ke CPMK, lalu ke CPL, lalu ke Profil Lulusan. Rantai ini diperiksa otomatis oleh `tools/validasi-obe.py` (aturan V3 dan V5).

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
