---
id: uai-inf101-asesmen-framework
tipe: asesmen
judul: "Kerangka Asesmen — Algoritma dan Pemrograman"
kode_mk: INF-101
nama_mk: Algoritma dan Pemrograman
prodi: Informatika
asesmen_id: ASM-FRAMEWORK
mengukur_cpmk: [CPMK-1, CPMK-2, CPMK-3, CPMK-4, CPMK-5, CPMK-6, CPMK-7]
mengukur_sub_cpmk: []
bobot_persen: 100
ai_diizinkan: false
versi: 2.0
status: draft
diperbarui: 2026-09-05
---

# Framework Asesmen — Algoritma dan Pemrograman (Teori)

> **Mata Kuliah:** Algoritma dan Pemrograman — 2 SKS (Teori)
> **Kode MK:** INF-101
> **Dosen Pengampu:** Tri Aji Nugroho, S.T., M.T.
> **Program Studi:** Informatika, Universitas Al Azhar Indonesia
> **Semester:** Genap 2025/2026
> **Bahasa Pemrograman:** Python
> **Ko-requisite:** Praktikum Algoritma dan Pemrograman (INF-102)

---

## 1. Filosofi Asesmen

### 1.1 Assessment OF Learning dan Assessment FOR Learning

Framework asesmen mata kuliah ini dirancang dengan pendekatan ganda:

**Assessment OF Learning (Sumatif)**
Asesmen sumatif bertujuan mengukur pencapaian akhir mahasiswa terhadap Capaian Pembelajaran Mata Kuliah (CPMK). Instrumen utama pada komponen teori meliputi Ujian Tengah Semester (UTS) dan Ujian Akhir Semester (UAS). Hasil asesmen sumatif digunakan untuk menentukan nilai akhir mahasiswa.

> **Catatan:** Tugas pemrograman (T1-T6) dan Proyek Akhir dinilai secara terpisah dalam mata kuliah Praktikum Algoritma dan Pemrograman (INF-102).

**Assessment FOR Learning (Formatif)**
Asesmen formatif bertujuan memberikan umpan balik selama proses pembelajaran agar mahasiswa dapat memperbaiki dan meningkatkan pemahaman secara berkelanjutan. Instrumen pada komponen teori meliputi kuis (K1-K3), latihan di kelas, refleksi diri, dan partisipasi aktif. Umpan balik diberikan secara cepat dan konstruktif.

### 1.2 Alignment dengan Taksonomi Bloom

Seluruh asesmen dirancang mengacu pada jenjang kognitif Taksonomi Bloom yang Direvisi:

| Jenjang Bloom | Level | Instrumen Asesmen |
|---|---|---|
| Mengingat (C1) | Rendah | Kuis pilihan ganda, UTS bagian PG |
| Memahami (C2) | Rendah | Code tracing, essay konseptual |
| Menerapkan (C3) | Menengah | UTS/UAS tulis kode |
| Menganalisis (C4) | Menengah | Analisis kompleksitas, code review |
| Mengevaluasi (C5) | Tinggi | Perbandingan algoritma, essay analisis |
| Mencipta (C6) | Tinggi | Desain solusi (UAS), esai desain algoritma |

### 1.3 Asesmen Autentik

Asesmen autentik berarti tugas dan ujian dirancang agar relevan dengan dunia nyata (*real-world relevant*). Prinsip-prinsip asesmen autentik yang diterapkan:

- **Konteks nyata**: Soal dan tugas menggunakan skenario kehidupan sehari-hari di Indonesia (kasir warung, antrian rumah sakit, perpustakaan)
- **Keterampilan abad 21**: Mahasiswa tidak hanya menulis kode, tetapi juga mendokumentasikan, mempresentasikan, dan berkolaborasi
- **Literasi AI**: Mahasiswa belajar menggunakan AI sebagai alat bantu secara etis dan bertanggung jawab
- **Integritas akademik**: Setiap asesmen memiliki kebijakan AI yang jelas dan transparan

---

## 2. Komponen Penilaian

| No | Komponen | Bobot | Frekuensi | Sifat |
|---|---|---|---|---|
| 1 | Kuis (K1-K3) | 20% | 3 kali | Individu, in-class |
| 2 | Ujian Tengah Semester (UTS) | 30% | 1 kali | Individu, closed-book |
| 3 | Ujian Akhir Semester (UAS) | 40% | 1 kali | Individu, closed-book |
| 4 | Partisipasi | 10% | Sepanjang semester | Individu |
| | **Total** | **100%** | | |

> **Catatan:** Tugas Pemrograman (T1-T6) dan Proyek Akhir dinilai dalam mata kuliah terpisah: Praktikum Algoritma dan Pemrograman (INF-102).

---

## 3. Detail per Komponen

> **Catatan:** Tugas Pemrograman (T1-T6) dan Proyek Akhir tidak termasuk dalam komponen penilaian mata kuliah teori ini. Kedua komponen tersebut dinilai dalam mata kuliah Praktikum Algoritma dan Pemrograman (INF-102).

### 3.1 Kuis (K1-K3) — 20%

| Kode | Minggu | Cakupan | CPMK diukur | Format | Durasi | Bobot |
|---|:-:|---|---|---|---|:-:|
| `ASM-K1` | 4 | Minggu 1-4 (algoritma, variabel, seleksi, perulangan) | CPMK-3 | 10 PG + 2 *code tracing* | 20 menit | 7% |
| `ASM-K2` | 7 | Minggu 5-7 (fungsi, string, list & tuple) | CPMK-4, CPMK-5 | 10 PG + 2 *code tracing* | 20 menit | 7% |
| `ASM-K3` | 12 | Minggu 9-12 (dict & set, pencarian, pengurutan, rekursi) | CPMK-6 | 10 PG + 2 *code tracing* | 20 menit | 6% |

**Ketentuan Kuis:**
- Dikerjakan secara individu di kelas (*closed-book*, tanpa AI)
- Tidak ada kuis susulan kecuali dengan surat keterangan resmi
- Setiap butir soal **wajib ditandai kode Sub-CPMK** agar ketercapaian dapat dihitung

### 3.2 Ujian Tengah Semester (UTS) — 30%

| Aspek | Keterangan |
|---|---|
| Waktu | Minggu ke-8 sesuai kalender akademik UAI |
| Durasi | 100 menit |
| Sifat | Closed-book, tanpa catatan, tanpa AI |
| Cakupan | Minggu 1-7 (Fase 1: Fondasi + Fase 2: Modularitas) |
| Format | PG (20%) + Code Tracing (30%) + Tulis Kode (30%) + Essay/Desain (20%) |
| Alat | Kertas dan alat tulis (ujian tertulis manual) |

Detail kisi-kisi tersedia di dokumen **kisi-kisi-uts.md**.

### 3.3 Ujian Akhir Semester (UAS) — 40%

| Aspek | Keterangan |
|---|---|
| Waktu | Minggu ke-16 sesuai kalender akademik UAI |
| Durasi | 120 menit |
| Sifat | Closed-book + 1 lembar catatan A4 (tulisan tangan sendiri, bolak-balik), tanpa AI |
| Cakupan | Komprehensif (Minggu 1-15), penekanan pada Minggu 9-15 |
| Format | PG (20%) + Code Tracing (30%) + Tulis Kode (30%) + Essay/Analisis (20%) |
| Alat | Kertas, alat tulis, 1 lembar catatan A4 |

Detail kisi-kisi tersedia di dokumen **kisi-kisi-uas.md**.

### 3.4 Partisipasi — 10%

Penilaian partisipasi mencakup dua aspek:

| Aspek | Bobot | Keterangan |
|---|---|---|
| Kehadiran | 50% | Minimal 75% kehadiran. Di bawah 75% = tidak lulus |
| Kontribusi Diskusi | 50% | Aktif bertanya, menjawab, membantu teman, berpartisipasi dalam diskusi kelas |

> **Catatan:** Komponen Etika AI (AI Usage Log) dinilai dalam mata kuliah Praktikum (INF-102).

**Penilaian Kehadiran:**
- Hadir 100% = skor kehadiran penuh
- Setiap ketidakhadiran tanpa keterangan mengurangi skor kehadiran secara proporsional
- Izin sakit/resmi dengan surat keterangan tidak mengurangi skor

---

## 4. Matrix CPMK x Asesmen

> **Sumber tunggal.** Matriks ini **wajib identik** dengan RPS §G.2 ([`../01-rps/rps-algoritma-pemrograman.md`](../01-rps/rps-algoritma-pemrograman.md)). Bila berbeda, RPS yang berlaku.
>
> Matriks hanya memuat komponen yang terdaftar pada peta bobot §2. Komponen praktikum (tugas pemrograman, laporan, proyek) berada pada RPS INF-102.

| CPMK | Rumusan ringkas | `ASM-K1` | `ASM-K2` | `ASM-K3` | `ASM-UTS` | `ASM-UAS` | `ASM-PAR` |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|
| **CPMK-1** | Konsep algoritma, *computational thinking*, peran pemrograman di era AI | | | | ✓ | ✓ | ✓ |
| **CPMK-2** | Variabel, tipe data, operator, dan ekspresi | | | | ✓ | ✓ | ✓ |
| **CPMK-3** | Struktur kontrol: seleksi dan perulangan | ✓ | | | ✓ | ✓ | ✓ |
| **CPMK-4** | Fungsi, pengolahan string, dan modularitas | | ✓ | | ✓ | ✓ | ✓ |
| **CPMK-5** | Pemilihan dan penggunaan struktur data | | ✓ | | ✓ | ✓ | ✓ |
| **CPMK-6** | Algoritma pencarian, pengurutan, dan rekursi | | | ✓ | | ✓ | ✓ |
| **CPMK-7** | Efisiensi algoritma dan pemrograman berbantuan AI | | | | | ✓ | ✓ |

**Keterangan:** ✓ = CPMK diukur melalui instrumen tersebut.

> **Catatan cakupan.** Seluruh CPMK juga diukur melalui tugas pemrograman dan proyek akhir pada INF-102. Rincian penghitungan ketercapaian: [`../mutu/02-pengukuran-ketercapaian-cpl.md`](../mutu/02-pengukuran-ketercapaian-cpl.md).

---

## 5. Kebijakan Penggunaan AI (AI Usage Policy)

Mata kuliah ini mengadopsi pendekatan **"AI-Augmented Learning"** di mana AI dianggap sebagai alat bantu yang harus digunakan secara etis dan bertanggung jawab.

### 5.1 Tabel Kebijakan AI per Komponen (Teori)

| No | Komponen | AI Diperbolehkan? | Dokumentasi Diperlukan? | Keterangan |
|---|---|---|---|---|
| 1 | Kuis (K1-K3) | Tidak | Tidak | Dikerjakan di kelas tanpa perangkat elektronik |
| 2 | UTS | Tidak | Tidak | Closed-book, tanpa AI, ujian tertulis |
| 3 | UAS | Tidak | Tidak | Closed-book + 1 lembar catatan, tanpa AI |
| 4 | Partisipasi | Ya (untuk persiapan) | Tidak | Boleh gunakan AI untuk menyiapkan materi diskusi |

> **Catatan:** Kebijakan AI untuk Tugas Pemrograman (T1-T6) dan Proyek Akhir diatur dalam mata kuliah Praktikum Algoritma dan Pemrograman (INF-102).

### 5.2 Prinsip AI Usage

1. **Transparansi**: Selalu dokumentasikan penggunaan AI dalam AI Usage Log
2. **Pemahaman**: Mahasiswa harus mampu menjelaskan setiap baris kode yang dihasilkan AI
3. **Kreativitas**: AI digunakan untuk mempercepat, bukan menggantikan proses berpikir
4. **Integritas**: Mengklaim karya AI sebagai karya sendiri tanpa dokumentasi = pelanggaran akademik

### 5.3 Sanksi Pelanggaran

| Pelanggaran | Sanksi |
|---|---|
| Menggunakan AI saat kuis/UTS/UAS | Nilai 0 untuk komponen tersebut |
| Copy-paste kode AI tanpa pemahaman (terdeteksi saat tanya jawab) | Nilai 0 untuk komponen + pelaporan ke prodi |
| Plagiarisme antar mahasiswa | Nilai 0 untuk semua pihak + pelaporan ke prodi |

---

## 6. Konversi Nilai Akhir

Nilai akhir dihitung berdasarkan bobot masing-masing komponen dan dikonversi ke huruf mutu sesuai ketentuan Universitas Al Azhar Indonesia:

| Nilai Angka | Huruf Mutu | Bobot | Keterangan |
|---|---|---|---|
| 85 - 100 | A | 4.00 | Sangat Baik |
| 80 - 84 | A- | 3.75 | |
| 75 - 79 | B+ | 3.50 | |
| 70 - 74 | B | 3.00 | Baik |
| 65 - 69 | B- | 2.75 | |
| 60 - 64 | C+ | 2.50 | |
| 55 - 59 | C | 2.00 | Cukup |
| 50 - 54 | C- | 1.75 | |
| 40 - 49 | D | 1.00 | Kurang |
| 0 - 39 | E | 0.00 | Tidak Lulus |

**Syarat Kelulusan:**
- Nilai minimal **C (55)** untuk lulus mata kuliah
- Kehadiran minimal **75%** dari total pertemuan

> **Catatan:** Mata kuliah Praktikum Algoritma dan Pemrograman (INF-102) memiliki syarat kelulusan tersendiri.

### Formula Perhitungan Nilai Akhir

```
Nilai Akhir = (Kuis x 0.20) + (UTS x 0.30) + (UAS x 0.40) + (Partisipasi x 0.10)
```

**Contoh Perhitungan:**

| Komponen | Nilai | Bobot | Kontribusi |
|---|---|---|---|
| Kuis | 75 | 20% | 15.00 |
| UTS | 70 | 30% | 21.00 |
| UAS | 72 | 40% | 28.80 |
| Partisipasi | 85 | 10% | 8.50 |
| **Total** | | **100%** | **73.30** |

Nilai akhir = **73.30** -> Huruf mutu: **B**

---

## 7. Kalender Asesmen

| Minggu | Asesmen | Keterangan |
|:-:|---|---|
| 4 | `ASM-K1` — Kuis 1 | Awal pertemuan Minggu 4, 20 menit |
| 7 | `ASM-K2` — Kuis 2 | Awal pertemuan Minggu 7, 20 menit |
| 8 | `ASM-UTS` | Sesuai jadwal akademik UAI |
| 12 | `ASM-K3` — Kuis 3 | Awal pertemuan Minggu 12, 20 menit |
| 16 | `ASM-UAS` | Sesuai jadwal akademik UAI |
| 1-16 | `ASM-PAR` — Partisipasi | Kehadiran dan kontribusi diskusi sepanjang semester |

> Kalender ini identik dengan RPS §G.3. Kuis 2 dijadwalkan **Minggu 7**, bukan Minggu 8, agar tidak bertumpuk dengan UTS.

> **Catatan:** Kalender tugas pemrograman dan proyek akhir tersedia pada dokumen INF-102.

---

## 8. Mekanisme Remedial dan Perbaikan

- **Kuis**: Tidak ada remedial; 1 kuis terendah di-drop (nilai terbaik 2 dari 3 yang dihitung)
- **UTS/UAS**: Tidak ada remedial

> **Catatan:** Mekanisme remedial untuk Tugas Pemrograman (T1-T6) dan Proyek Akhir diatur dalam mata kuliah Praktikum Algoritma dan Pemrograman (INF-102).

---

## 9. Komunikasi dan Transparansi

- Seluruh nilai diumumkan melalui LMS (Learning Management System) UAI dalam waktu **7 hari kerja** setelah asesmen
- Mahasiswa berhak mengajukan **keberatan nilai** dalam waktu **3 hari kerja** setelah pengumuman
- Dosen menyediakan **office hours** (2 jam/minggu) untuk konsultasi terkait asesmen
- Umpan balik tertulis diberikan untuk setiap kuis dan ujian

---

## 10. Hubungan dengan Praktikum Algoritma dan Pemrograman (INF-102)

Mata kuliah Algoritma dan Pemrograman (INF-101) merupakan komponen teori yang berjalan berdampingan (*ko-requisite*) dengan mata kuliah Praktikum Algoritma dan Pemrograman (INF-102). Kedua mata kuliah memiliki penilaian yang **terpisah** dan menghasilkan **nilai akhir masing-masing**.

**Komponen yang dinilai dalam Praktikum (INF-102):**

| No | Komponen | Keterangan |
|---|---|---|
| 1 | Tugas Pemrograman (T1-T6) | Tugas coding mingguan dengan AI Usage Log |
| 2 | Laporan Praktikum | Dokumentasi dan refleksi setiap sesi praktikum |
| 3 | Proyek Akhir | Proyek integratif individu/kelompok |
| 4 | Responsi | Ujian praktik langsung di laboratorium |

> Mahasiswa wajib mengikuti **kedua** mata kuliah (INF-101 dan INF-102) pada semester yang sama. Detail komponen penilaian, bobot, dan rubrik untuk praktikum tersedia dalam dokumen framework asesmen Praktikum Algoritma dan Pemrograman (INF-102).

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* -- Program Studi Informatika, Universitas Al Azhar Indonesia
