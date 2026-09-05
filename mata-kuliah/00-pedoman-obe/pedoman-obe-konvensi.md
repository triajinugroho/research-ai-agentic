---
id: uai-inf-pedoman-obe
tipe: pedoman
judul: Pedoman OBE & Konvensi Paket Mata Kuliah Informatika UAI
prodi: Informatika
fakultas: Sains dan Teknologi
universitas: Universitas Al Azhar Indonesia
versi: 2.0
status: berlaku
diperbarui: 2026-09-05
berlaku_untuk: [INF-101, INF-102, TBD-STAT, IF2205, IF2206, IF3XXX]
---

# Pedoman OBE & Konvensi Paket Mata Kuliah

> **Kedudukan dokumen.** Ini adalah *single source of truth* untuk seluruh RPS, buku ajar, modul, lab, dan asesmen di paket mata kuliah Prodi Informatika UAI. Bila terjadi perbedaan konvensi dengan dokumen manapun — termasuk `CLAUDE.md` dan berkas `prompt-*.md` — **dokumen ini yang berlaku**.

**Riwayat versi**

| Versi | Tanggal | Perubahan pokok |
|---|---|---|
| 0.1-draft | 2026-07 | Kerangka awal; usulan kode CPL format KKNI (**dibatalkan di v0.2**) |
| **2.0** | 2026-09-05 | CPL resmi prodi; taksonomi C/A/P; aturan resolusi tabrakan kode Sub-CPMK; pemetaan LAM-INFOKOM 2.0; PPEPP; IABEE; UNESCO Jan 2026; skema metadata Satu Data; aturan validasi |

---

## A. Tujuan & Ruang Lingkup

Pedoman ini memandu pembaruan paket 6 mata kuliah agar:

1. **Selaras standar terbaru** — Permendiktisaintek 39/2025, 10/2026, dan 14/2026; SN-Dikti; KKNI Level 6; Instrumen LAM-INFOKOM 2.0; kriteria IABEE.
2. **Tetap sederhana** — RPS inti ramping; detail berat dipindah ke dokumen pendamping ber-tautan. Ini bukan kompromi, melainkan sejalan dengan semangat deregulasi Permendiktisaintek 39/2025.
3. **Terlacak penuh** — rantai **Profil Lulusan → CPL → Bahan Kajian → CPMK → Sub-CPMK → materi → asesmen** utuh, konsisten, dan **dapat diverifikasi mesin**.
4. **Siap sistem AI** — setiap berkas punya metadata *machine-readable* sebagai fondasi tutor AI, penandaan otomatis butir soal, dan dasbor ketercapaian CPL.
5. **Berdampak** — kontribusi tiap mata kuliah pada kemajuan IPTEK dan kemanusiaan dinyatakan dengan indikator yang dapat dibuktikan.

---

## B. Dasar Hukum & Acuan

### B.1 Sistem Tiga Status — aturan integritas sitasi

Sebagian acuan di bawah diperoleh melalui penelusuran publik, bukan dari salinan resmi. **Menuliskan nomor pasal spekulatif ke dalam dokumen yang dibaca asesor adalah risiko reputasi yang nyata.** Karena itu setiap acuan diberi status:

| Status | Makna | Boleh dipakai untuk |
|:-:|---|---|
| ✅ | Teks/nomor terverifikasi | Sitasi lengkap, **termasuk nomor pasal** |
| 🟡 | Kerangka terverifikasi via penelusuran, teks resmi belum ada | Sitasi tingkat **nama peraturan + tahun**, *tanpa nomor pasal* |
| 🔲 | Menunggu dokumen | **Belum boleh disitasi** |

### B.2 Daftar Acuan

| Kode | Acuan | Status | Yang diserap ke dokumen |
|---|---|:-:|---|
| **[REG-1]** | Permendiktisaintek **No. 39 Tahun 2025** — Penjaminan Mutu Pendidikan Tinggi | 🟡 | 8 Standar Nasional Pendidikan; **7 pertimbangan perumusan CPL** (visi-misi PT, KKNI, perkembangan IPTEK, kebutuhan dunia kerja, ranah keilmuan prodi, kompetensi utama lulusan, kurikulum prodi sejenis); RPL wajib; *micro-credential*; fleksibilitas moda; dorongan akreditasi global |
| **[REG-2]** | Permendiktisaintek **No. 10 Tahun 2026** — Perubahan atas No. 39/2025. Ditetapkan 14 Juli 2026, diundangkan 16 Juli 2026, BN RI 2026 No. 477; mengubah 26 ketentuan Pasal 14–113 | ✅ Pasal 14 (1) · 🟡 selebihnya | **Kutipan verbatim Pasal 14 ayat (1):** *"Pelaksanaan proses pembelajaran diselenggarakan dengan menciptakan suasana belajar yang menyenangkan, inklusif, kolaboratif, kreatif, dan efektif."* Juga: pengakuan pembelajaran lampau, pendidikan jarak jauh, non-diskriminasi |
| **[REG-3]** | **Perpres No. 8 Tahun 2012** — KKNI, Level 6 untuk program sarjana | ✅ | Ranah CPL: Sikap, Pengetahuan, Kemampuan Umum, Keterampilan Khusus |
| **[REG-4]** | Matriks butir Instrumen Akreditasi LAM-INFOKOM | 🔲 | Penomoran butir penilaian |
| **[REG-5]** | SK Akreditasi **050/SK/LAM-INFOKOM/Ak/S/III/2025** — peringkat "Baik Sekali" | ✅ | Status akreditasi berjalan. **Atribusi yang benar: LAM-INFOKOM**, bukan BAN-PT |
| **[REG-6]** | Permendiktisaintek **No. 14 Tahun 2026** — Satu Data Diktisaintek | 🟡 | Empat prinsip struktural: **standar data, metadata, interoperabilitas, kode referensi/data induk**; kewajiban pelaporan PDDikti |
| **[REG-7]** | **Instrumen Akreditasi LAM-INFOKOM 2.0** (berlaku 2025, jenjang D1–S3) | 🟡 | Penyederhanaan 9 → **6 kriteria**; **setiap kriteria diukur dengan siklus PPEPP**; orientasi luaran dan mutu berkelanjutan |
| **[REG-8]** | **IKU Diktisaintek Berdampak 2026** | 🟡 | 6 indikator wajib + 5 pilihan + 1 partisipatif; frasa kebijakan *"Akreditasi Unggul yang Berdampak"* |
| **[REG-9]** | **UNESCO AI Competency Frameworks** — Siswa & Guru, **diperbarui 16 Januari 2026** | ✅ | **Siswa:** 12 kompetensi × 4 dimensi, level **Understand → Apply → Create**. **Guru:** 15 kompetensi × 5 dimensi |
| **[REG-10]** | ACM/IEEE-CS/AAAI — **Computer Science Curricula 2023 (CS2023)** | ✅ | Infusi *Society, Ethics, Professionalism* ke 18 *knowledge area*; *competency model* |
| **[REG-11]** | **IABEE** — kriteria akreditasi program sarjana bidang *computing* | 🟡 | Syarat OBE berjalan ≥1 tahun; penilaian atas CPL, kurikulum, proses, penilaian, penjaminan mutu, peningkatan berkelanjutan |

### B.3 Sitasi yang wajib diperbaiki

| Sitasi lama | Masalah | Ganti dengan |
|---|---|---|
| Permendikbud **No. 3 Tahun 2020** (SN-Dikti) | Sudah dicabut | [REG-1] / [REG-2] |
| "Permendikbudristek (2024) SN-Dikti" | **Peraturan ini tidak pernah ada** — sitasi fiktif | [REG-1] |
| "BAN-PT. (2025). SK Akreditasi No. 050/SK/LAM-INFOKOM/…" | Salah atribusi lembaga | [REG-5], atribusi **LAM-INFOKOM** |
| UNESCO dengan dua judul berbeda antar-berkas | Tidak konsisten | [REG-9], judul seragam |

**Garis keturunan regulasi:** Permendikbud 3/2020 → Permendikbudristek 53/2023 → Permendiktisaintek 39/2025 → 10/2026.

---

## C. Prinsip Desain (9 Prinsip)

1. **Outcome-first** — mulai dari capaian, bukan daftar materi. Tiap materi dan asesmen wajib punya "induk" Sub-CPMK.
2. **Lean by default** — bila sebuah detail dapat dipindah ke dokumen pendamping tanpa memutus keterlacakan, **pindahkan**.
3. **Satu fakta satu tempat** — tiap fakta (bobot, kode CPL, SKS, jadwal) ditulis sekali di sumbernya dan dirujuk di tempat lain.
4. **Machine-readable** — setiap berkas diawali YAML *front-matter* (§G).
5. **AI-augmented, bukan AI-dependent** — AI Corner dan AI Policy dipertahankan; integritas akademik (*amanah*) di atas segalanya.
6. **Konteks Indonesia & keislaman** — data BPS, kasus lokal, nilai keislaman terintegrasi secara alami.
7. **Closing the loop** — tiap mata kuliah punya mekanisme ukur ketercapaian CPL dan siklus perbaikan. Ini pembeda "Baik Sekali" → "Unggul".
8. **Berdampak & terukur** — kontribusi mata kuliah pada dampak keilmuan dan kemanusiaan dinyatakan dengan indikator yang dapat dibuktikan ([REG-8]).
9. **Inklusif & fleksibel** — desain pembelajaran memenuhi Pasal 14 ayat (1) [REG-2]; moda dan rekognisi dinyatakan eksplisit ([REG-1]).

---

## D. Arsitektur Dokumen per Mata Kuliah

```
<mata-kuliah>/
├── 00-strategic-analysis/   (MK teori) atau 00-pedoman-praktikum/ (MK praktikum)
├── 01-rps/                  RPS RAMPING (inti OBE) + metadata
├── 02-rtm/                  Rencana Tugas Mahasiswa
├── 03-modules/ | 03-modul-praktikum/
├── 04-labs/ | 04-assessments/
├── 05-assessments/ | 05-buku-ajar/
├── 06-buku-ajar/            (MK teori)
├── mutu/                    ⭐ dokumen pendamping mutu (§F)
└── datasets/
```

**Penyeragaman penomoran folder** (`05-buku-ajar` vs `06-buku-ajar`) dikerjakan di **akhir Fase 2** menggunakan `git mv` agar riwayat terjaga dan tidak mengaburkan *diff* migrasi kode.

---

## E. Kode & Taksonomi Kanonik

### E.0 Profil Lulusan

Registri: **`profil-lulusan.md`** — PL01–PL05, penanda IABEE, domain prodi *"Islamic Entrepreneur and Education"*.

### E.1 CPL — **PEMBATALAN REKOMENDASI v0.1**

> ⚠️ **Rekomendasi v0.1 dibatalkan.** Pedoman v0.1 menyarankan format KKNI `CPL-S/P/KU/KK`. Setelah dokumen resmi prodi diterima, terbukti kode resmi **berbeda**. Yang berlaku adalah kode resmi prodi, dipakai **verbatim**.

Registri: **`cpl-master.md`** — 11 CPL: `CPLUAI1`, `CPLUAI3`, `CPL03`, `CPL04`, `CPL05`, `CPL-FSTS1`, `CPL07`, `CPL08`, `CPL09`, `CPL10`, `CPLUAI2`.

**Aturan pengikat:**
1. **Rumusan CPL hanya hidup di `cpl-master.md`.** Dokumen turunan **dilarang** menulis ulang rumusan — cukup menyebut kode dan menautkan. Ini menutup penyebab konflik CPL tiga arah (T-4) secara struktural.
2. **Ranah KKNI adalah kolom, bukan bagian kode.** Tulis `CPL08` (Keterampilan Khusus), bukan `CPL-KK8`.
3. Setiap RPS wajib memuat **tabel jembatan** kode lama → kode resmi selama dokumen lama masih beredar.

### E.2 CPMK & Sub-CPMK — aturan resolusi tabrakan

> **Masalah yang diselesaikan (T-1).** Kode `CPMK-3.2` merujuk dua capaian berbeda: di RPS berarti *minggu 3, sub ke-2*; di modul dan buku ajar berarti *sub ke-2 dari CPMK-3*. Ini ambiguitas referensial — rantai OBE tidak dapat diverifikasi. Tercatat 718 kemunculan pada 89 berkas.

**Aturan baku:**

1. **CPMK** = `CPMK-1` … `CPMK-n`. Ini identitas capaian, **bukan nomor minggu**.
2. **Sub-CPMK** = `Sub-CPMK-<CPMK induk>.<urut>` — **wajib berprefiks, bertanda hubung, tanpa spasi**. Contoh: `Sub-CPMK-3.2` = sub ke-2 dari CPMK-3.
3. **String telanjang `CPMK-x.y` DILARANG** untuk Sub-CPMK. Larangan ini dipilih justru karena membuat sisa migrasi dapat dideteksi dengan satu ekspresi reguler, dan menghapus ambiguitas terhadap kode CPMK induk.
4. **Minggu tidak pernah masuk ke dalam kode.** Minggu adalah kolom tabel dan field `minggu:` pada metadata.
5. Varian `Sub-CPMK 1.1` (spasi) dan `CPMK-1.1` (tanpa prefiks) **tidak sah**.
6. Setiap mata kuliah wajib punya **tabel migrasi kode lama → kanonik** di `00-pedoman-obe/migrasi/<kode-mk>.md`, **disimpan permanen** — bukan dihapus setelah migrasi — agar nilai dan soal semester sebelumnya tetap terlacak.

### E.3 Bahan Kajian

Registri: **`registri-bahan-kajian.md`** — BK01–BK22 dan matriks BK × CPL.

**Pembebanan CPL ke mata kuliah diturunkan dari Bahan Kajian, bukan dipilih bebas.** Alurnya: Mata Kuliah → Bahan Kajian → CPL → Profil Lulusan.

### E.4 Kode Asesmen

Diperlukan karena matriks CPMK × asesmen dan lembar pengukuran CPL membutuhkan ID stabil, bukan label bebas.

| Pola | Makna |
|---|---|
| `ASM-K1` … `ASM-Kn` | Kuis ke-n |
| `ASM-UTS` / `ASM-UAS` | Ujian Tengah / Akhir Semester |
| `ASM-T1` … `ASM-Tn` | Tugas ke-n |
| `ASM-PRJ` | Proyek akhir |
| `ASM-PAR` | Partisipasi |
| `ASM-LAP1` … | Laporan praktikum (MK praktikum) |
| `ASM-RES` | Responsi (MK praktikum) |

### E.5 Taksonomi Tiga Ranah

Registri: **`taksonomi-cap.md`** — C1–C6 (Kognitif), A1–A5 (Afektif), P1–P5 (Psikomotorik) beserta Kata Kerja Operasional.

**Perubahan dari v0.1:** repositori sebelumnya hanya memakai C1–C6. Prodi mensyaratkan **tiga ranah**. Namun ranah A dan P **hanya diterapkan bila alami** — memaksakan ketiganya pada setiap Sub-CPMK menghasilkan rumusan artifisial yang melemahkan dokumen.

---

## F. Dokumen Pendamping Mutu (folder `mutu/`)

Tiga artefak ringkas yang mengubah "materi bagus" menjadi "bukti akreditasi Unggul".

| Berkas | Peran | Pagu |
|---|---|---|
| `mutu/01-peta-mutu-mk.md` | Kedudukan MK · **PL→CPL→BK→CPMK** (tingkat kontribusi K/M/T) · kontribusi ke 6 kriteria LAM · kontribusi IKU · diferensiasi misi · unit rekognisi | ≤1,5 halaman |
| `mutu/02-pengukuran-ketercapaian-cpl.md` | Rumus · instrumen pengukuran · ambang & kategori · lembar hasil per siklus · sumber data dan keterlacakan | ≤2 halaman |
| `mutu/03-ppepp-cqi.md` | Kalender PPEPP · log siklus berjalan · rencana tindak lanjut · riwayat perubahan (tag/commit) | ≤1,5 halaman |

**Mengapa tiga, bukan satu atau enam.** Satu berkas gabungan mencampur "penetapan" (stabil) dengan "hasil" (berubah tiap semester), menyulitkan telaah dan pemversian. Enam berkas per kriteria LAM menghasilkan 36 dokumen tipis di enam mata kuliah, karena kriteria 3, 4, dan 6 sesungguhnya bersifat tingkat program studi. **Asesor lebih menghargai tiga dokumen yang konsisten daripada enam dokumen bertumpuk.**

---

## G. Skema Metadata

Registri lengkap: **`kamus-data-metadata.md`**.

**Wajib pada semua berkas:** `id`, `tipe`, `judul`, `kode_mk`, `nama_mk`, `prodi`, `versi`, `status`, `diperbarui`.

Contoh untuk RPS:

```yaml
---
id: uai-inf101-rps
tipe: rps
judul: Rencana Pembelajaran Semester — Algoritma dan Pemrograman
kode_mk: INF-101
nama_mk: Algoritma dan Pemrograman
sks: 2
sks_teori: 2
sks_praktikum: 0
semester_jenis: genap
semester_kurikulum: 2
tahun_akademik: 2025/2026
siklus: 2025-2026-genap
moda: kombinasi
prodi: Informatika
dosen: Tri Aji Nugroho, S.T., M.T.
prasyarat: []
korekuisit: [INF-102, TBD-STAT]
pl: [PL01, PL03, PL04]
cpl: [CPL03, CPL07, CPL08, CPLUAI1, CPLUAI3]
bk: [BK12, BK14, BK01]
cpmk: [CPMK-1, CPMK-2, CPMK-3, CPMK-4, CPMK-5, CPMK-6, CPMK-7]
cpl_status: resmi
versi: 2.0
status: berlaku
diperbarui: 2026-09-05
---
```

**Aturan:** *front-matter* **mencerminkan** isi dokumen, tidak menggantikannya. Ketidaksesuaian antara keduanya adalah cacat yang ditangkap validator.

---

## H. Template RPS Ramping

### H.1 Peta perubahan bagian (perbaikan T-7)

> **Cacat pada v0.1.** Template A–K usulan v0.1 tidak kompatibel dengan A–K yang sudah dipakai empat mata kuliah, dan **menghapus bagian "Profil Proyek Akhir" tanpa menyatakan ke mana ia dipindahkan**. Tabel berikut menutup celah itu.

| Lama | Bagian lama | Baru | Bagian baru | Keterangan |
|:-:|---|:-:|---|---|
| A | Identitas | **A** | Identitas | + `Moda Pembelajaran`; SKS ditulis **hanya di sini** |
| B | Deskripsi | **B** | Deskripsi | + kontribusi riset/dampak |
| C | CPL | **C** | Profil Lulusan, CPL & Bahan Kajian | rumusan dihapus → rujuk `cpl-master.md` + tabel jembatan |
| D | CPMK | **D** | CPMK | + ranah C/A/P + kode `ASM-*` |
| E | Sub-CPMK | **E** | Sub-CPMK | kode kanonik + kolom Minggu + C/A/P |
| F | Tabel RPS | **F** | Rencana Pembelajaran 16 Minggu | kolom Metode memuat unsur Pasal 14 (1) |
| G | Peta Evaluasi | **G** | Peta Evaluasi | matriks wajib sahih terhadap peta bobot |
| — | — | **H** | **Pengukuran Ketercapaian CPL** | **BARU** — ringkas + tautan `mutu/02` |
| H | Konversi Nilai | **I** | Konversi Nilai | bergeser satu huruf |
| I | Referensi | **J** | Referensi | bergeser; sitasi [REG-*] |
| J | Kebijakan Khusus | **K** | Kebijakan Khusus | + RPL, moda, inklusivitas |
| K | Profil Proyek Akhir | **L** | Proyek Akhir *(ringkas)* | **isi dipindah** ke `04-assessments/project-guidelines.md`; RPS menyisakan ringkasan ≤5 baris + tautan |

### H.2 Aturan bentuk

- **Pagu RPS: ≤550 baris.** Target Fase 1 untuk INF-101: **≤480 baris** (dari 550) — RPS harus **lebih pendek** meski cakupan mutu bertambah. Bila RPS bertambah panjang, pekerjaan dinyatakan gagal memenuhi sasaran.
- Mata kuliah praktikum memakai kerangka yang sama. **Bagian E (Sub-CPMK) tidak boleh dihilangkan** — ini perbaikan wajib untuk IF2206 yang saat ini memakai kode Sub-CPMK tanpa mendefinisikannya.
- Mata kuliah praktikum **mewarisi** CPL dan rubrik proyek dari mata kuliah teori pasangannya; jangan ditulis ulang.

---

## I. Aturan Konsistensi

1. Semester Genap 2025/2026; publikasi materi kuliah **2026**; "Jakarta, Februari 2026".
2. Nama mata kuliah formal lengkap ("Algoritma dan Pemrograman"); nama dosen "Tri Aji Nugroho, S.T., M.T." tanpa singkatan.
3. Bab 13 = AI-Augmented; Bab 14 = Proyek Akhir. Rujukan "proyek akhir" mengarah ke Bab 14.
4. Bobot asesmen tiap mata kuliah berjumlah tepat **100%**, dan **matriks CPMK × asesmen wajib sahih terhadap peta bobot** — tidak boleh memuat komponen yang tidak ada di peta bobot.
5. Setiap berkas diakhiri footer tagline prodi.
6. **[BARU]** Setiap berkas diawali YAML *front-matter* (§G).
7. **[BARU]** Kode PL/CPL/BK/CPMK/Sub-CPMK/asesmen mengikuti §E.
8. **[BARU]** Sitasi regulasi mengikuti §B dengan sistem tiga status.
9. **[BARU] SKS ditulis hanya di RPS §A.** Modul dan bab buku ajar menulis `Estimasi waktu: N × 50 menit` **tanpa menyebut SKS**. Ini menutup konflik "2 SKS vs 3 SKS" secara struktural.

> **Latar keputusan SKS.** INF-101 berbobot **2 SKS teori**; INF-102 berbobot **1 SKS praktikum** dan berdiri terpisah. Estimasi "3 × 50 menit" pada modul mencerminkan **sesi gabungan teori + praktikum**, bukan bobot INF-101. Karena SKS adalah data induk yang dilaporkan ke PDDikti ([REG-6]), penulisannya dipusatkan di satu tempat.

---

## J. Peta Jalan Pembaruan

| Fase | Keluaran | Status |
|---|---|---|
| **0** | Pedoman ini + 6 registri prodi + mitigasi generator | ✅ selesai |
| **1** | Pilot **INF-101** sebagai *golden template*: tabel migrasi, RPS, 3 artefak mutu, buku ajar, 16 modul, asesmen, validator | 🔄 berjalan |
| **2** | Propagasi ke 5 mata kuliah; penanganan khusus IF2206; penyeragaman folder | ⏳ |
| **2.5** | **Sinkronisasi generator** — `prompt-*.md`, `CLAUDE.md`, `README.md`. **Wajib**; tanpa ini regenerasi konten membatalkan Fase 1–2 | ⏳ |
| **3** | Lapisan program: matriks CPL × MK, pemetaan LAM-INFOKOM 2.0, pemetaan IABEE, SPMI/PPEPP program | ⏳ |
| **4** | Perbaikan referensi menyeluruh (dapat paralel dengan Fase 2) | ⏳ |
| **5** | `obe-registry.json` — indeks *machine-readable* sebagai fondasi sistem pendidikan berbantuan AI | ⏳ |

---

## K. Status Dokumen Acuan

| Dokumen | Status |
|---|---|
| Profil Lulusan resmi prodi | ✅ diterima |
| Daftar CPL resmi prodi (11 CPL) | ✅ diterima |
| Matriks CPL × Bahan Kajian | ✅ diterima |
| Tabel taksonomi C/A/P + KKO | ✅ diterima |
| Teks lengkap Permendiktisaintek 39/2025 & 10/2026 | 🟡 kerangka terverifikasi, salinan resmi belum ada |
| Matriks butir Instrumen LAM-INFOKOM 2.0 | 🔲 menunggu |
| Penetapan ambang ketercapaian CPL (SK) | 🔲 menunggu — sementara ditandai "usulan" |
| Penetapan resmi pembebanan BK per mata kuliah | 🔲 menunggu — sementara ditandai [PERLU VALIDASI PRODI] |

Salinan resmi dapat ditaruh di `00-pedoman-obe/sumber/`.

---

## L. Pemetaan ke 6 Kriteria LAM-INFOKOM 2.0

Instrumen 2.0 menyederhanakan 9 → 6 kriteria, dan **mengukur setiap kriteria dengan siklus PPEPP** ([REG-7]).

| # | Kriteria | Wujud di tingkat mata kuliah | Artefak bukti | Status repo |
|:-:|---|---|---|---|
| 1 | **Budaya Mutu** | Siklus PPEPP berjalan dan terdokumentasi; telaah sejawat | `mutu/03` + **riwayat commit/tag git** | **BARU** |
| 2 | **Relevansi Pendidikan** | Keselarasan PL→CPL→BK→CPMK→materi→asesmen; kemutakhiran IPTEK; keterserapan kebutuhan dunia kerja | RPS §C–H, `mutu/01`, `00-strategic-analysis/`, CS2023 & SWEBOK v4 | ADA sebagian |
| 3 | **Relevansi Penelitian** | Penyerapan hasil riset dosen ke materi; proyek akhir bertema riset | `mutu/01` §3 + penandaan tema proyek | LEMAH |
| 4 | **Relevansi PkM** | Studi kasus dan tema proyek yang menjawab kebutuhan masyarakat | Penandaan tema berdampak di `project-guidelines.md` | LEMAH |
| 5 | **Akuntabilitas** | Ketertelusuran nilai; transparansi rubrik; validitas data | `mutu/02`, matriks CPMK × asesmen, rubrik, metadata | **BARU sebagian** |
| 6 | **Diferensiasi Misi** | Nilai keislaman, AI-augmented, konteks Indonesia, domain *Islamic Entrepreneur and Education* | `mutu/01` §5 | ADA tapi implisit |

**Bacaan jujur atas status ini:** kekuatan repositori terkonsentrasi pada kriteria 2 dan 6. Kriteria **1 dan 5 — yang justru membedakan "Baik Sekali" dari "Unggul" — belum berwujud sama sekali** sebelum pembaruan ini.

---

## M. PPEPP sebagai Tulang Punggung

Karena setiap kriteria LAM 2.0 diukur dengan PPEPP, siklus ini **bukan lampiran** melainkan kerangka waktu yang menaungi seluruh dokumen mata kuliah.

| Tahap | Kegiatan di tingkat mata kuliah | Waktu | Bukti |
|---|---|---|---|
| **P**enetapan | RPS, rubrik, dan ambang ketercapaian ditetapkan | sebelum minggu 1 | RPS `status: berlaku` + `git tag` awal siklus |
| **P**elaksanaan | Perkuliahan sesuai RPS | minggu 1–16 | Modul mingguan, AI Usage Log, berita acara |
| **E**valuasi | Menghitung ketercapaian CPMK/CPL dari nilai | minggu 17 | `mutu/02` §4 lembar hasil |
| **P**engendalian | Koreksi dalam siklus berjalan untuk CPMK di bawah ambang | minggu 9–16 | `mutu/03` §2 log tindakan |
| **P**eningkatan | Perubahan RPS/materi untuk siklus berikutnya | sebelum siklus baru | `mutu/03` §3 + `git diff` antar-tag |

> **Wawasan arsitektural.** Repositori ini berbasis git, sehingga **riwayat commit adalah jejak bukti PPEPP yang paling kredibel dan paling murah** — ia memperlihatkan *apa* yang berubah, *kapan*, dan *mengapa*, tanpa dokumen tambahan. Konsekuensinya: setiap siklus diberi tag (`siklus-2025-2026-genap`), setiap berkas mutu memuat field `siklus:`, dan commit dibuat bertahap per langkah — karena granularitas riwayat itulah yang menjadi bukti.

### M.1 Jalur IABEE (akreditasi internasional)

PL01 dan PL02 dirumuskan mengikuti kerangka IABEE ([REG-11]). Bukti mutu yang sama melayani dua jalur:

| Aspek | LAM-INFOKOM 2.0 | IABEE |
|---|---|---|
| Rumusan & pengukuran CPL | Kriteria 2 & 5 | Penilaian CPL |
| Siklus perbaikan | Kriteria 1 (PPEPP) | Peningkatan berkelanjutan |
| Rubrik & keterlacakan nilai | Kriteria 5 | Sistem penilaian |
| Keunikan program | Kriteria 6 | — |

Artinya `mutu/01`–`mutu/03` **tidak perlu digandakan** untuk IABEE; cukup dipetakan ulang pada Fase 3 (`pemetaan-iabee.md`).

---

## N. Rekognisi & Fleksibilitas

Registri: **`rekognisi-dan-fleksibilitas.md`** — RPL, *micro-credential*, moda pembelajaran, klausul inklusivitas.

Beban administrasi ditaruh di tingkat prodi. **Di RPS hanya bertambah satu baris** (`Moda Pembelajaran` pada §A); **di `mutu/01` hanya bertambah satu tabel** unit rekognisi.

---

## O. Bahasa "Berdampak" (IKU)

Menyelaraskan kosakata paket ini dengan kebijakan nasional *"Akreditasi Unggul yang Berdampak"* ([REG-8]), bukan menambah dokumen.

`mutu/01` §4 memuat tabel **maksimal 4 baris** berisi IKU yang benar-benar tersentuh mata kuliah tersebut.

> **Aturan tegas: jangan menuliskan angka capaian IKU.** Angka adalah kewenangan program studi. Yang ditulis hanya *jalur kontribusi* dan *artefak buktinya*.

---

## P. Kerangka Kompetensi AI (UNESCO, Januari 2026)

Mengganti progresi buatan sendiri **Dasar/Menengah/Lanjut/Mahir** dengan level resmi kerangka **Siswa**: **Understand → Apply → Create** ([REG-9]).

| Level UNESCO | Bab buku ajar | Dimensi dominan |
|---|---|---|
| **Understand** | 1–4 | *AI techniques and applications*; *Human-centred mindset* |
| **Apply** | 5–11 | *AI techniques and applications*; *Ethics of AI* |
| **Create** | 12–14 | *AI system design*; *Ethics of AI* (tanggung jawab penuh) |

Label lokal Dasar/Menengah/Lanjut/Mahir boleh dipertahankan sebagai padanan, tetapi **level UNESCO yang menjadi acuan**. Keuntungannya: bersandar pada kerangka internasional — mendukung dorongan akreditasi global [REG-1] dan jalur IABEE — tanpa menulis ulang isi AI Corner. Yang berubah hanya label level dan satu tabel di `00-halaman-depan.md`.

---

## Q. Aturan Validasi

Ditegakkan oleh `tools/validasi-obe.py` dan `checklist-verifikasi.md`.

| # | Validasi | Menangkap |
|---|---|---|
| **V1** | *Front-matter* ada; YAML sah; field wajib lengkap; enumerasi dan tanggal sah | Metadata rusak |
| **V2** | Keunikan `id` di seluruh repositori | Tabrakan identitas |
| **V3** | **Integritas referensial** — `sub_cpmk`→§E RPS, `cpmk`→§D, `cpl`→`cpl-master.md`, `bk`→registri BK | Sub-CPMK "hantu" |
| **V4** | **Larangan pola lama** — menolak `CPMK-<angka>.<angka>` telanjang dan `Sub-CPMK <angka>` (spasi) | Kambuhnya tabrakan kode |
| **V5** | **Cakupan** — tiap CPMK punya ≥1 Sub-CPMK; tiap Sub-CPMK dirujuk ≥1 materi **dan** ≥1 asesmen | Rantai OBE putus (*constructive alignment*) |
| **V6** | Jumlah bobot asesmen = 100%; matriks sahih terhadap peta bobot | Matriks asesmen tidak sahih |
| **V7** | **Data induk konsisten** — `nama_mk`, `kode_mk`, `tahun_akademik`, dosen seragam; **`sks` hanya di RPS** | Konflik SKS |
| **V8** | Konvensi — footer tagline; Bab 13 = AI; Bab 14 = Proyek Akhir; tahun 2026 | Regresi konvensi |
| **V9** | Sitasi — nol rujukan "Nomor 3 Tahun 2020"; tiap `[REG-*]` yang dirujuk terdefinisi | Sitasi usang |
| **V10** | Tautan relatif antar-berkas tidak putus | Tautan mati |
| **V11** | **Pagu ukuran** — RPS ≤550 baris; tiap berkas `mutu/` ≤180 baris | Pembengkakan dokumen |
| **V12** | RPS `status: berlaku` ditolak selama `cpl_status: interim` | Pengesahan prematur |

**Yang tetap memerlukan manusia:** mutu rumusan Sub-CPMK (kata kerja operasional dan terukur), kesesuaian level taksonomi dengan bentuk asesmen, keselarasan isi materi dengan Sub-CPMK, dan kebenaran substansi regulasi. Ditangani `checklist-verifikasi.md` **dengan tanda tangan penelaah sejawat** — telaah sejawat itu sendiri adalah bukti kriteria 1 (Budaya Mutu).

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
