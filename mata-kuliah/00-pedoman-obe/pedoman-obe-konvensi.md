---
tipe: pedoman
judul: Pedoman OBE & Konvensi Paket Mata Kuliah Informatika UAI
prodi: Informatika
fakultas: Sains dan Teknologi
universitas: Universitas Al Azhar Indonesia
versi: 0.1-draft
status: FASE 0 — fondasi (menunggu dokumen resmi prodi untuk finalisasi CPL)
diperbarui: 2026-07
---

# Pedoman OBE & Konvensi Paket Mata Kuliah

> **Kedudukan dokumen:** Ini adalah *single source of truth* untuk pembaruan seluruh RPS, buku ajar, modul, lab, dan asesmen di paket mata kuliah Prodi Informatika UAI. Semua dokumen lain mengacu ke sini. Jika terjadi perbedaan konvensi, dokumen ini yang berlaku.

**Status:** `v0.1-draft` — Fase 0. Bagian bertanda 🔲 **[MENUNGGU DOKUMEN RESMI]** belum final sampai Profil Lulusan & CPL resmi prodi, teks Permendiktisaintek 39/2025 & 10/2026, dan instrumen LAM-INFOKOM diterima.

---

## A. Tujuan & Ruang Lingkup

Pedoman ini memandu pembaruan paket 6 mata kuliah agar:

1. **Selaras standar terbaru** — Permendiktisaintek No. 39 Tahun 2025 (Penjaminan Mutu) beserta perubahannya No. 10 Tahun 2026 (mekanisme akreditasi), SN-Dikti, KKNI Level 6, dan instrumen LAM-INFOKOM.
2. **Tetap sederhana** — RPS inti ramping; detail berat dipindah ke dokumen pendamping ber-link (sejalan semangat deregulasi 39/2025).
3. **Terlacak penuh (traceable)** — rantai Profil Lulusan → CPL → CPMK → Sub-CPMK → materi → asesmen utuh dan konsisten lintas 6 MK.
4. **Siap sistem AI** — setiap file punya metadata *machine-readable* (YAML front-matter) sebagai fondasi AI tutor / adaptive learning / auto-assessment / analytics.
5. **Berdampak** — memetakan kontribusi tiap MK ke dampak keilmuan, teknologi, dan kemanusiaan (SDGs) serta nilai keislaman (*amanah*, warisan al-Khawarizmi).

---

## B. Dasar Hukum & Acuan

| Kode | Acuan | Status di repo |
|------|-------|----------------|
| **[REG-1]** | Permendiktisaintek **No. 39 Tahun 2025** — Penjaminan Mutu Pendidikan Tinggi (kerangka SN-Dikti & SPMI substantif) | 🔲 teks lengkap menunggu dari prodi |
| **[REG-2]** | Permendiktisaintek **No. 10 Tahun 2026** — Perubahan atas No. 39/2025 (26 ketentuan, Pasal 14–113; fokus mekanisme akreditasi & tata kelola BAN-PT). Ditetapkan 14 Juli 2026, diundangkan 16 Juli 2026, BN RI 2026 No. 477 | 🔲 teks lengkap menunggu dari prodi |
| **[REG-3]** | **Perpres No. 8 Tahun 2012** — Kerangka Kualifikasi Nasional Indonesia (KKNI), Level 6 untuk S1 | ✅ dapat langsung dirujuk |
| **[REG-4]** | Instrumen Akreditasi Program Studi **LAM-INFOKOM** (kriteria & matriks penilaian terbaru) | 🔲 menunggu dari prodi |
| **[REG-5]** | SK Akreditasi Prodi: **050/SK/LAM-INFOKOM/Ak/S/III/2025** — peringkat "Baik Sekali" | ✅ tercatat di repo |

> ⚠️ **Perbaikan sitasi wajib:** Rujukan lama **Permendikbud No. 3 Tahun 2020** (masih ada di `05-buku-ajar/lampiran.md`) sudah usang. Ganti ke [REG-1]/[REG-2]. Lineage: Permendikbud 3/2020 → Permendikbudristek 53/2023 → Permendiktisaintek 39/2025 → 10/2026.

---

## C. Prinsip Desain (7 Prinsip)

1. **Outcome-first** — mulai dari capaian, bukan daftar materi. Tiap materi/asesmen harus punya "induk" CPMK.
2. **Lean by default** — RPS memuat yang esensial; jika sebuah detail bisa dipindah ke dokumen pendamping tanpa memutus traceability, pindahkan.
3. **Satu kebenaran** — tiap fakta (bobot, kode CPL, jadwal) ditulis sekali di sumbernya, dirujuk di tempat lain. Tidak ada angka yang diketik-ulang beda versi.
4. **Machine-readable** — setiap file diawali YAML front-matter (lihat §G).
5. **AI-augmented, bukan AI-dependent** — AI Corner & AI Policy dipertahankan; integritas akademik (*amanah*) di atas segalanya.
6. **Konteks Indonesia & keislaman** — data BPS, kasus lokal, nilai keislaman terintegrasi natural.
7. **Closing the loop** — tiap MK punya mekanisme ukur ketercapaian CPL + siklus perbaikan (PPEPP). Ini pembeda "Baik Sekali" → "Unggul".

---

## D. Arsitektur Dokumen per Mata Kuliah

Struktur folder dibakukan (memperbaiki penomoran yang saat ini tak seragam — mis. Algoritma pakai `05-buku-ajar`, MK lain `06-buku-ajar`):

```
<mata-kuliah>/
├── 00-strategic-analysis/   (MK teori)  atau  00-pedoman-praktikum/ (MK praktikum)
├── 01-rps/                  RPS RAMPING (inti OBE) + metadata
├── 02-rtm/                  Rencana Tugas Mahasiswa
├── 03-modules/ | 03-modul-praktikum/   materi mingguan
├── 04-labs/ | 04-assessments/          lab / asesmen
├── 05-assessments/ | 05-buku-ajar/     asesmen / buku ajar
├── 06-buku-ajar/            buku ajar (MK teori)
├── mutu/                    ⭐ BARU — dokumen pendamping mutu (lihat §F)
└── datasets/
```

**Prinsip RPS ramping + pendamping:** RPS = kontrak inti yang cukup dibaca dalam 1 duduk. Rubrik rinci, lembar pengukuran CPL, dan siklus PPEPP hidup di folder `mutu/` dan cukup **di-link** dari RPS.

---

## E. Kode & Taksonomi OBE Kanonik

### E.1 Sistem kode CPL — **KANONIK: format KKNI**

Saat ini ada **dua sistem** yang bertabrakan: `CPL-1..6` (4 MK) vs `CPL-S/P/KU/KK` (pasangan RPL). Dibakukan ke **format KKNI/SN-Dikti**:

| Prefix | Ranah | Contoh |
|--------|-------|--------|
| **CPL-S** | Sikap | CPL-S1, CPL-S2, … |
| **CPL-P** | Pengetahuan | CPL-P1, … |
| **CPL-KU** | Keterampilan Umum | CPL-KU1, … |
| **CPL-KK** | Keterampilan Khusus | CPL-KK1, … |

> 🔲 **[MENUNGGU DOKUMEN RESMI]** Daftar CPL final diambil **verbatim** dari dokumen kurikulum prodi — **tidak dikarang**. Setiap RPS wajib memuat **tabel jembatan** `CPL lama (1..6) ↔ CPL kanonik (S/P/KU/KK)` agar dokumen lama tetap terlacak.

### E.2 Penomoran CPMK & Sub-CPMK — **perbaikan traceability**

Masalah saat ini: Sub-CPMK dinomori per-**minggu** (`CPMK-9.1` untuk minggu 9), sehingga tidak jelas menempel ke CPMK induk yang mana (padahal CPMK hanya 7).

**Aturan baku:**
- **CPMK** = `CPMK-1 … CPMK-n` (identitas capaian, **bukan** nomor minggu).
- **Sub-CPMK** = `Sub-CPMK-<induk>.<urut>` → mis. `Sub-CPMK-3.2` = sub kedua dari CPMK-3. **Minggu** dicatat di kolom terpisah, bukan di dalam kode.
- Setiap Sub-CPMK menyertakan level Bloom (C1–C6).

---

## F. Dokumen Pendamping Mutu (folder `mutu/`)

Tiga artefak ringkas ini yang mengubah "materi bagus" → "bukti akreditasi Unggul":

| File | Isi | Menjawab kriteria |
|------|-----|-------------------|
| `mutu/pemetaan-profil-lulusan-cpl.md` | Profil Lulusan prodi → CPL yang dibebankan ke MK ini | Keterkaitan CPL–profil |
| `mutu/pengukuran-ketercapaian-cpl.md` | Indikator kinerja tiap CPMK + **ambang** (mis. *"≥70% mahasiswa mencapai skor ≥70"*) + sumber data asesmen | Pengukuran ketercapaian CPL |
| `mutu/ppepp-cqi.md` | Siklus **P**enetapan–**P**elaksanaan–**E**valuasi–**P**engendalian–**P**eningkatan tingkat MK: hasil ukur → tindak lanjut semester berikutnya | *Closing the loop* / CQI |

> Ketiganya sengaja **ringkas (1–2 halaman)** agar tetap sederhana. Ini juga fondasi Fase 3 (agregasi ke level program).

---

## G. Skema Metadata Machine-Readable (untuk sistem AI)

Setiap file `.md` diawali YAML front-matter. Ini sekaligus **bukti traceability** (akreditasi) dan **sumber data terstruktur** (sistem AI ke depan).

```yaml
---
tipe: rps            # rps | modul | bab-buku-ajar | lab | asesmen | rubrik | rtm | mutu | pedoman
kode_mk: INF-101
nama_mk: Algoritma dan Pemrograman
sks: 2
semester: genap
tahun_akademik: 2025/2026
prodi: Informatika
minggu: [1, 2]                 # untuk modul/lab
cpl: [CPL-P2, CPL-KK1]         # ID CPL kanonik (§E.1)
cpmk: [CPMK-1, CPMK-2]
sub_cpmk: [Sub-CPMK-1.1, Sub-CPMK-1.2]
bloom: [C2, C3]
prasyarat: []
versi: 1.0
diperbarui: 2026-07
---
```

**Aturan:** ID di `cpl`/`cpmk`/`sub_cpmk` harus persis sama dengan yang dipakai di tabel dokumen — inilah yang membuat mesin (dan manusia) bisa menautkan materi ↔ capaian ↔ asesmen secara otomatis. Ini enabler untuk: AI tutor yang sadar CPMK, auto-tagging soal ke Sub-CPMK, dan dashboard ketercapaian CPL.

---

## H. Template RPS Ramping (kerangka inti)

Dibakukan untuk **6 MK** (menyatukan varian A–K, A–J, dan A–H yang ada sekarang). Bagian **inti** wajib; bagian **[→ mutu/]** cukup di-link.

| § | Bagian | Sifat |
|---|--------|-------|
| A | Identitas Mata Kuliah | inti |
| B | Deskripsi Singkat | inti |
| C | CPL yang Dibebankan (+ tabel jembatan kode lama↔kanonik) | inti |
| D | CPMK (+ peta ke CPL & Bab buku) | inti |
| E | Sub-CPMK per minggu (kode §E.2 + Bloom) | inti |
| F | Rencana Pembelajaran 16 Minggu (materi, metode, pengalaman belajar, indikator, bobot) | inti |
| G | Peta Evaluasi (bobot 100% + matriks CPMK×asesmen) | inti |
| H | Pengukuran Ketercapaian CPL & Perbaikan | **[→ mutu/]** ringkas + link |
| I | Kebijakan (AI Policy, kehadiran, integritas) | inti |
| J | Referensi (sitasi [REG-*] terbaru) | inti |
| K | Konversi Nilai | inti |

> MK praktikum (INF-102, IF2206) memakai kerangka sama; §D–E boleh disederhanakan tapi **Sub-CPMK tidak boleh dihilangkan** (perbaikan untuk IF2206 yang saat ini tanpa Sub-CPMK).

---

## I. Aturan Konsistensi (wajib, dari CLAUDE.md + tambahan)

1. Semester Genap 2025/2026; publikasi materi kuliah **2026**; "Jakarta, Februari 2026".
2. Nama MK formal lengkap (mis. "Algoritma dan Pemrograman"); nama dosen "Tri Aji Nugroho, S.T., M.T." tanpa singkatan.
3. Bab 13 = AI-Augmented; Bab 14 = Proyek Akhir. Rujukan "proyek akhir" → Bab 14.
4. Bobot asesmen tiap MK **total 100%** (lihat CLAUDE.md untuk rincian per MK).
5. Setiap file diakhiri footer tagline (lihat bawah).
6. **[BARU]** Setiap file diawali YAML front-matter (§G).
7. **[BARU]** Kode CPL/CPMK/Sub-CPMK mengikuti §E.
8. **[BARU]** Sitasi regulasi mengikuti §B ([REG-*]).

---

## J. Peta Jalan Pembaruan

| Fase | Keluaran | Status |
|------|----------|--------|
| **0** | Pedoman ini + template + skema metadata | 🔄 berjalan (dokumen ini v0.1) |
| **1** | Pilot **Algoritma & Pemrograman** jadi *golden template* (RPS + 3 artefak `mutu/` + buku ajar sinkron + metadata) | ⏳ menunggu dokumen resmi |
| **2** | Propagasi ke 5 MK lain; beresi IF2205/IF2206; seragamkan penomoran folder | ⏳ |
| **3** | Lapisan program: katalog Profil Lulusan, CPL master, matriks CPL×MK se-prodi, paket SPMI/PPEPP | ⏳ |
| **4** | Fondasi AI: indeks *machine-readable* seluruh learning object + blueprint AI education system | ⏳ |

---

## K. Checklist Handover (yang diperlukan untuk memulai Fase 1)

Agar Fase 1 *accreditation-grade* dan bukan rekonstruksi, mohon sediakan:

- [ ] 🔲 **Profil Lulusan resmi prodi** (daftar profil + deskripsi)
- [ ] 🔲 **Daftar CPL resmi prodi** (kode S/P/KU/KK + rumusan lengkap)
- [ ] 🔲 **Teks/rangkuman Permendiktisaintek 39/2025** (khususnya pasal standar kompetensi lulusan, proses, penilaian, RPS)
- [ ] 🔲 **Teks/rangkuman Permendiktisaintek 10/2026** (pasal yang menyentuh ketercapaian CPL & bukti mutu)
- [ ] 🔲 **Instrumen/matriks LAM-INFOKOM terbaru** (butir kriteria kurikulum & mutu)
- [ ] ⬜ (Opsional) Ambang ketercapaian CPL yang prodi kehendaki (mis. target ≥70% / ≥70)

Boleh di-*paste* sebagai teks di chat, atau taruh sebagai file di repo (mis. `mata-kuliah/00-pedoman-obe/sumber/`) lalu beri tahu saya.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
