# BAB 3: REQUIREMENTS ENGINEERING

**Tri Aji Nugroho, S.T., M.T.**
Rekayasa Perangkat Lunak (IF2205) — Prodi Informatika, Universitas Al Azhar Indonesia

---

## Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa mampu:

| Sub-CPMK | Deskripsi | Level Bloom | Estimasi Waktu |
|-----------|-----------|-------------|----------------|
| 2.1 | Menerapkan teknik elicitation (interview, observation, questionnaire, workshop, prototyping, document analysis) untuk mengumpulkan kebutuhan perangkat lunak | C3 (Menerapkan) | 90 menit |
| 2.2 | Menyusun dokumen Software Requirements Specification (SRS) sesuai standar IEEE 830/ISO 29148 | C3 (Menerapkan) | 90 menit |

---

## Estimasi Waktu

| Aktivitas | Durasi |
|-----------|--------|
| Membaca materi | 120 menit |
| Praktik elicitation & menulis SRS | 90 menit |
| Mengerjakan latihan soal | 60 menit |
| Eksplorasi AI Corner | 30 menit |
| **Total** | **5 jam** |

---

## Prasyarat

- Bab 1: Pengantar Rekayasa Perangkat Lunak (konsep SE, SWEBOK)
- Bab 2: Proses dan Model Pengembangan (Agile, Scrum)
- Pemahaman dasar tentang stakeholder dan konteks bisnis

---

## Peta Konsep Bab

```
                    ┌──────────────────────────────┐
                    │   REQUIREMENTS ENGINEERING    │
                    └──────────────┬───────────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
          ▼                        ▼                        ▼
┌─────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│   STAKEHOLDER   │   │     PROSES RE    │   │   DOKUMENTASI    │
│    ANALYSIS     │   │                  │   │      (SRS)       │
│                 │   │  Elicitation     │   │                  │
│ Power-Interest  │   │  Analysis        │   │  IEEE 830        │
│ Matrix          │   │  Specification   │   │  ISO 29148       │
│ Identifikasi    │   │  Validation      │   │  Template        │
│ Prioritas       │   │  Management      │   │  Traceability    │
└─────────────────┘   └──────────────────┘   └──────────────────┘
          │                        │                        │
          ▼                        ▼                        ▼
┌─────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│    ELICITATION   │   │ JENIS KEBUTUHAN │   │    VALIDASI      │
│    TECHNIQUES    │   │                  │   │                  │
│                 │   │  Functional      │   │  Review          │
│ Interview       │   │  Non-Functional  │   │  Prototyping     │
│ Observation     │   │  Domain          │   │  Test Case Gen   │
│ Questionnaire   │   │  Constraint      │   │  Walkthrough     │
│ Workshop        │   │                  │   │  Checklist       │
│ Prototyping     │   │                  │   │                  │
│ Document Anal.  │   │                  │   │                  │
└─────────────────┘   └──────────────────┘   └──────────────────┘
```

---

## 3.1 Pengantar Requirements Engineering

### 3.1.1 Mengapa Requirements Penting?

> **60% kegagalan proyek software disebabkan oleh requirements yang buruk** — Standish Group CHAOS Report

Requirements engineering (RE) adalah proses sistematik untuk **menemukan, mendokumentasikan, dan memelihara** kebutuhan perangkat lunak. RE merupakan fondasi dari seluruh proses software engineering — jika fondasi salah, seluruh bangunan akan runtuh.

Biaya memperbaiki kesalahan requirements meningkat secara eksponensial seiring fase pengembangan:

```
Biaya Relatif Perbaikan Bug per Fase
═══════════════════════════════════════════════════
Requirements  │ █ ($1)
Design        │ ████ ($5)
Coding        │ ██████████ ($10)
Testing       │ ██████████████████████ ($20)
Production    │ ██████████████████████████████████████████████████ ($100)
              └───────────────────────────────────────────────
              Sumber: Barry Boehm, "Software Engineering Economics"
```

### 3.1.2 Definisi dan Ruang Lingkup RE

Requirements engineering mencakup seluruh aktivitas yang terkait dengan penemuan, dokumentasi, dan pemeliharaan kebutuhan sistem. Menurut **SWEBOK v4**, Requirements Engineering adalah salah satu dari 15 Knowledge Areas, yang mencakup:

| Aspek | Penjelasan |
|-------|------------|
| **Requirement** | Kondisi atau kemampuan yang dibutuhkan pengguna untuk menyelesaikan masalah atau mencapai tujuan |
| **Requirements Engineering** | Proses sistematik untuk elicitation, analysis, specification, dan validation kebutuhan |
| **Requirements Analyst** | Orang yang bertanggung jawab mengelola proses RE (bisa juga disebut Business Analyst) |

### 3.1.3 Proses Requirements Engineering

Proses RE terdiri dari **lima fase utama** yang saling terkait dan sering dilakukan secara iteratif:

```
    ┌──────────┐     ┌──────────┐     ┌──────────────┐     ┌──────────┐     ┌──────────┐
    │ELICITATION│────▶│ ANALYSIS │────▶│SPECIFICATION │────▶│VALIDATION│────▶│MANAGEMENT│
    │(Kumpulkan)│     │(Analisis)│     │(Dokumentasi) │     │(Validasi)│     │(Kelola)  │
    └──────────┘     └──────────┘     └──────────────┘     └──────────┘     └──────────┘
          ▲                                                       │
          └───────────────────────────────────────────────────────┘
                              (Iterasi / Feedback Loop)
```

| Fase | Aktivitas Utama | Output |
|------|----------------|--------|
| **Elicitation** | Mengumpulkan kebutuhan dari stakeholder melalui berbagai teknik | Catatan interview, hasil survey, prototype |
| **Analysis** | Mendeteksi konflik, ambiguitas, dan gap; memprioritaskan kebutuhan | Model requirements, requirements terklasifikasi |
| **Specification** | Mendokumentasikan kebutuhan dalam format standar | Dokumen SRS (IEEE 830/ISO 29148) |
| **Validation** | Memastikan kebutuhan benar, lengkap, dan konsisten | Checklist validasi, sign-off stakeholder |
| **Management** | Mengelola perubahan kebutuhan sepanjang proyek | Change log, traceability matrix |

---

## 3.2 Stakeholder Analysis

### 3.2.1 Siapa Itu Stakeholder?

**Stakeholder** adalah siapa saja yang memiliki kepentingan (*interest*) atau pengaruh (*influence*) terhadap proyek software. Mengidentifikasi stakeholder dengan benar adalah langkah pertama dan paling krusial dalam RE.

### 3.2.2 Jenis Stakeholder

| Kategori | Contoh | Kontribusi ke Requirements |
|----------|--------|---------------------------|
| **Pengguna Langsung** (*End Users*) | Mahasiswa, pustakawan, kasir | Kebutuhan fungsional utama, usability |
| **Pengguna Tidak Langsung** | Manajer yang membaca laporan | Kebutuhan reporting dan dashboard |
| **Pemilik Sistem** (*System Owner*) | Kepala perpustakaan, direktur RS | Tujuan bisnis, batasan anggaran |
| **Pengembang** (*Development Team*) | Programmer, designer, tester | Kelayakan teknis (feasibility) |
| **Regulator** | Kemenkes, OJK, Kemendikbud | Kebutuhan kepatuhan regulasi |
| **Operator** | Admin IT, helpdesk | Kebutuhan operasional, maintenance |

### 3.2.3 Power-Interest Matrix

Power-Interest Matrix membantu menentukan strategi komunikasi dan keterlibatan setiap stakeholder:

```
                        INTEREST (Kepentingan)
                     Low                    High
                ┌──────────────────┬──────────────────┐
           High │   KEEP SATISFIED │  MANAGE CLOSELY  │
                │                  │                  │
    POWER       │  Rektor UAI      │  Kepala          │
    (Pengaruh)  │  Dekan FST       │  Perpustakaan    │
                │                  │  Pustakawan      │
                ├──────────────────┼──────────────────┤
           Low  │     MONITOR      │  KEEP INFORMED   │
                │                  │                  │
                │  Vendor hardware │  Mahasiswa        │
                │  ISP kampus      │  Dosen pengajar  │
                │                  │  Staff akademik  │
                └──────────────────┴──────────────────┘
```

**Strategi per kuadran:**

| Kuadran | Strategi | Contoh Aksi |
|---------|----------|-------------|
| **Manage Closely** (High Power, High Interest) | Libatkan aktif di setiap fase RE | Workshop mingguan, review SRS bersama |
| **Keep Satisfied** (High Power, Low Interest) | Update berkala, jangan mengecewakan | Laporan progres bulanan |
| **Keep Informed** (Low Power, High Interest) | Informasi rutin, dengarkan masukan | Newsletter, survey kepuasan |
| **Monitor** (Low Power, Low Interest) | Pantau jika ada perubahan posisi | Review periodik |

### 3.2.4 Contoh: Stakeholder Sistem Perpustakaan Digital UAI

```
┌────────────────────────────────────────────────────────────────┐
│           STAKEHOLDER MAP: Perpustakaan Digital UAI             │
├──────────────────────┬─────────────────────────────────────────┤
│ Stakeholder          │ Kebutuhan Utama                         │
├──────────────────────┼─────────────────────────────────────────┤
│ Mahasiswa (4000+)    │ Cari buku, pinjam online, perpanjang    │
│ Pustakawan (5)       │ Kelola katalog, pantau peminjaman       │
│ Kepala Perpustakaan  │ Laporan statistik, efisiensi operasi    │
│ Dosen (200+)         │ Cek ketersediaan referensi mata kuliah  │
│ Staff IT UAI (3)     │ Maintenance, backup, keamanan data      │
│ Kaprodi Informatika  │ Integrasi dengan sistem akademik        │
│ Wakil Rektor III     │ Compliance dengan aturan Kemendikbud    │
│ Penerbit buku        │ Akurasi data ISBN, metadata buku        │
└──────────────────────┴─────────────────────────────────────────┘
```

---

## 3.3 Teknik Elicitation

Elicitation adalah proses **mengumpulkan kebutuhan** dari stakeholder. Ini bukan sekadar "bertanya" — banyak kebutuhan tersembunyi (*tacit knowledge*) yang perlu digali dengan teknik yang tepat.

### 3.3.1 Perbandingan 6+ Teknik Elicitation

| Teknik | Deskripsi | Kapan Digunakan | Kelebihan | Kekurangan |
|--------|-----------|-----------------|-----------|------------|
| **Interview** | Tanya jawab langsung (terstruktur/semi-terstruktur) | Awal proyek, kebutuhan inti | Mendalam, bisa follow-up, membangun rapport | Memakan waktu, bias interviewer, tidak efisien untuk banyak stakeholder |
| **Observation** | Mengamati pengguna bekerja di lingkungan nyata | Proses bisnis kompleks, kebutuhan tersembunyi | Menemukan tacit knowledge, objektif | Hawthorne effect, memakan waktu, observer bias |
| **Questionnaire** | Survey tertulis (online/offline) | Banyak stakeholder, data kuantitatif | Skala besar, efisien, kuantitatif | Tidak bisa follow-up, response rate rendah, bias pertanyaan |
| **Workshop (JAD)** | Joint Application Development — sesi kolaboratif | Banyak stakeholder dengan konflik kepentingan | Konsensus cepat, kolaboratif, real-time clarification | Mahal, perlu fasilitator terampil, dominasi oleh senior |
| **Prototyping** | Mock-up/wireframe untuk mendapatkan feedback | UI/UX, requirements tidak jelas, validasi cepat | Visual, feedback konkret, mengurangi ambiguitas | Bisa salah ekspektasi ("ini sudah jadi ya?"), effort awal tinggi |
| **Document Analysis** | Pelajari dokumen, formulir, SOP yang sudah ada | Sistem pengganti (*legacy*), regulasi | Objektif, detail operasional, tidak mengganggu pengguna | Bisa outdated, tidak menangkap kebutuhan baru |
| **Focus Group** | Diskusi kelompok 5-8 orang terpilih | Memahami preferensi dan persepsi pengguna | Dinamika kelompok, ide beragam | Groupthink, dominasi oleh individu tertentu |
| **Brainstorming** | Diskusi terbuka tanpa kritik awal | Fase awal, inovasi, fitur baru | Kreatif, banyak ide | Bisa tidak fokus, perlu fasilitator |

### 3.3.2 Teknik Interview — Detail

Interview adalah teknik elicitation paling umum dan paling efektif untuk menggali kebutuhan mendalam.

**Jenis Interview:**

| Jenis | Karakteristik | Kapan Digunakan |
|-------|--------------|-----------------|
| **Structured** | Pertanyaan sudah disiapkan, urutan tetap | Kebutuhan sudah cukup jelas, perlu konfirmasi |
| **Semi-structured** | Ada panduan, tapi fleksibel untuk follow-up | Paling umum digunakan — seimbang antara struktur dan fleksibilitas |
| **Unstructured** | Diskusi bebas, hanya topik umum | Fase sangat awal, eksplorasi domain baru |

**Contoh Interview Script — Sistem Perpustakaan Kampus:**

```
═══════════════════════════════════════════════════════════════
INTERVIEW SCRIPT — Sistem Perpustakaan Digital UAI
Interviewer : Tim RE
Interviewee : Ibu Siti (Pustakawan Senior), 15 tahun pengalaman
Tanggal     : 15 Maret 2026
Durasi      : 45 menit
═══════════════════════════════════════════════════════════════

[OPENING — Bangun rapport, jelaskan tujuan]
P: Selamat pagi, Bu Siti. Terima kasih sudah meluangkan waktu.
   Kami sedang mengembangkan sistem perpustakaan digital.
   Kami ingin memahami bagaimana proses saat ini dan apa yang
   bisa diperbaiki. Apakah kami boleh merekam percakapan ini?

[PROSES SAAT INI — Pahami as-is]
P: Bisa ceritakan bagaimana proses peminjaman buku saat ini?
J: Mahasiswa datang, cari buku di rak atau tanya ke saya, 
   bawa ke meja sirkulasi, saya catat di buku log manual.
   Terkadang ada yang pinjam lewat WhatsApp, tapi tidak tercatat.

P: Berapa lama rata-rata proses peminjaman satu buku?
J: Kalau bukunya ketemu langsung, sekitar 5-10 menit.
   Tapi kalau harus cari-cari dulu, bisa 20-30 menit.

[MASALAH SAAT INI — Identifikasi pain points]
P: Apa masalah utama dengan proses saat ini?
J: 1) Sering kehilangan data — buku log basah atau hilang
   2) Mahasiswa tidak tahu buku sudah dipinjam atau belum
   3) Sulit tracking keterlambatan pengembalian
   4) Tidak ada statistik — berapa buku dipinjam per bulan?
   5) Buku sering disimpan di rak yang salah

[KEBUTUHAN MASA DEPAN — Identifikasi to-be]
P: Jika ada sistem baru, apa 3 fitur yang paling dibutuhkan?
J: 1) Pencarian buku online — mahasiswa cek dari HP
   2) Notifikasi otomatis untuk keterlambatan
   3) Laporan statistik peminjaman per bulan/semester

P: Apakah ada batasan yang perlu kami ketahui?
J: Koneksi internet di perpustakaan kadang lambat.
   Budget terbatas — tidak bisa beli server mahal.
   Staf saya ada 4 orang, tidak semua melek IT.

[CLOSING — Konfirmasi dan next steps]
P: Terima kasih, Bu Siti. Kami akan menyusun daftar kebutuhan
   berdasarkan percakapan ini dan mengirimkan untuk direview.
   Apakah ada hal lain yang ingin ditambahkan?
```

### 3.3.3 Teknik Observation — Detail

Observation berarti mengamati pengguna bekerja di lingkungan nyata. Sangat efektif untuk menangkap **tacit knowledge** — hal yang pengguna lakukan secara otomatis tanpa menyadarinya.

**Jenis Observation:**

| Jenis | Penjelasan | Contoh |
|-------|-----------|--------|
| **Passive** | Hanya mengamati, tidak ikut campur | Duduk di meja sirkulasi dan catat proses |
| **Active (Participatory)** | Ikut berpartisipasi dalam pekerjaan | Bantu pustakawan melayani mahasiswa selama sehari |
| **Ethnographic** | Observasi jangka panjang, pahami budaya | Tinggal di perpustakaan selama seminggu |

**Contoh Hasil Observation:**

```
═══════════════════════════════════════════════════════════════
OBSERVATION LOG — Perpustakaan UAI
Observer  : Andi (Requirements Analyst)
Tanggal   : 18 Maret 2026, 09:00-12:00
Lokasi    : Ruang Sirkulasi Perpustakaan Lantai 2
═══════════════════════════════════════════════════════════════

09:15 - Mahasiswa A datang, langsung ke rak Komputer. 
        Tidak menggunakan katalog, langsung browse rak.
        → [Insight] Katalog mungkin sulit digunakan atau
          mahasiswa tidak tahu cara pakainya.

09:32 - Mahasiswa B tanya ke pustakawan: "Buku Algoritma 
        Cormen ada ga?" Pustakawan cek di buku log manual
        (butuh 3 menit), ternyata sedang dipinjam.
        → [Insight] Perlu fitur cek ketersediaan real-time.

10:05 - Pustakawan menelepon mahasiswa X yang terlambat 
        mengembalikan buku 2 minggu. Nomor HP dari buku log.
        → [Insight] Perlu notifikasi otomatis + database kontak.

10:45 - 3 mahasiswa datang bersamaan, antri di satu meja.
        Pustakawan 2 sedang istirahat, hanya 1 yang melayani.
        → [Insight] Perlu self-service kiosk atau peminjaman online.

11:20 - Mahasiswa C mengembalikan buku, diletakkan di meja.
        Pustakawan akan shelving setelah jam 12.
        → [Insight] Buku tidak tersedia di rak meski sudah
          dikembalikan — perlu tracking status real-time.
```

### 3.3.4 Teknik Questionnaire — Detail

Questionnaire efektif untuk mengumpulkan data dari **banyak stakeholder** secara bersamaan.

**Tips Menyusun Questionnaire yang Efektif:**

1. **Gunakan campuran** pertanyaan tertutup (skala Likert) dan terbuka
2. **Urutkan** dari umum ke spesifik
3. **Hindari** pertanyaan leading (*"Bukankah sistem saat ini buruk?"*)
4. **Batasi** jumlah pertanyaan (15-25 pertanyaan, max 10 menit)
5. **Pilot test** dengan 3-5 responden sebelum distribusi massal

**Contoh Questionnaire Fragment:**

```
═══════════════════════════════════════════════════════════════
SURVEY KEBUTUHAN SISTEM PERPUSTAKAAN DIGITAL UAI
Target: Mahasiswa aktif UAI (semua fakultas)
═══════════════════════════════════════════════════════════════

Q1. Seberapa sering Anda mengunjungi perpustakaan kampus?
    ○ Setiap hari  ○ 2-3x seminggu  ○ 1x seminggu
    ○ 1-2x sebulan ○ Jarang/tidak pernah

Q2. Bagaimana Anda biasanya mencari buku di perpustakaan?
    □ Langsung ke rak  □ Tanya pustakawan  □ Katalog komputer
    □ Cari di internet  □ Lainnya: ___

Q3. Dari skala 1-5, seberapa penting fitur berikut?
                            Sangat          Sangat
                            Tidak           Penting
                            Penting
    Pencarian online         1  2  3  4  5
    Peminjaman online        1  2  3  4  5
    Notifikasi deadline      1  2  3  4  5
    Rekomendasi buku         1  2  3  4  5
    Review/rating buku       1  2  3  4  5
    Reservasi buku           1  2  3  4  5

Q4. Apa masalah terbesar yang Anda alami dengan perpustakaan
    saat ini? (jawaban bebas)
    ________________________________________________
```

### 3.3.5 Teknik Workshop (JAD) dan Prototyping

**Workshop / JAD (Joint Application Development):**

Sesi kolaboratif 2-4 jam dengan perwakilan semua stakeholder utama. Fasilitator memandu diskusi untuk mencapai konsensus tentang requirements.

```
Format Workshop RE (3 jam)
═══════════════════════════════════════════════
Sesi 1 (45 min) │ Presentasi visi produk + demo prototipe
Sesi 2 (60 min) │ Brainstorming requirements per kelompok
                 │ (gunakan sticky notes / Miro board)
Sesi 3 (45 min) │ Presentasi dan diskusi antar kelompok
Sesi 4 (30 min) │ Prioritisasi bersama (MoSCoW voting)
Closing (15 min) │ Rangkuman keputusan + next steps
```

**Prototyping:**

Membuat representasi visual dari sistem untuk mendapatkan feedback cepat.

| Jenis Prototype | Fidelity | Tools | Kapan |
|----------------|----------|-------|-------|
| **Paper Prototype** | Low | Kertas, spidol | Sangat awal, brainstorming |
| **Wireframe** | Low-Medium | Figma, Balsamiq, draw.io | Setelah requirements awal |
| **Clickable Prototype** | Medium-High | Figma, Adobe XD | Validasi flow pengguna |
| **Working Prototype** | High | HTML/CSS, Flask | Validasi teknis + UX |

### 3.3.6 Teknik Document Analysis

Mempelajari dokumen yang sudah ada untuk memahami sistem *as-is* dan regulasi yang berlaku.

**Dokumen yang Perlu Dianalisis:**

| Jenis Dokumen | Contoh | Informasi yang Didapat |
|---------------|--------|----------------------|
| **SOP** | SOP Peminjaman Buku | Alur proses saat ini |
| **Formulir** | Form peminjaman, kartu anggota | Data yang dikumpulkan |
| **Laporan** | Laporan peminjaman bulanan | Metrik dan KPI |
| **Regulasi** | Peraturan Rektor tentang perpustakaan | Batasan dan aturan |
| **Sistem lama** | Screenshot, manual sistem terdahulu | Fitur yang sudah ada |
| **Complaint log** | Buku saran, email keluhan | Pain points pengguna |

---

## 3.4 Jenis Requirements

### 3.4.1 Functional Requirements (FR)

Functional requirements mendefinisikan **APA** yang sistem harus lakukan — fungsi, fitur, dan perilaku spesifik.

**Contoh FR untuk Sistem Perpustakaan Digital UAI:**

```
═══════════════════════════════════════════════════════════════
FUNCTIONAL REQUIREMENTS — Perpustakaan Digital UAI
═══════════════════════════════════════════════════════════════

FR-01: Sistem HARUS memungkinkan mahasiswa mendaftar 
       menggunakan NIM dan email kampus (@uai.ac.id).

FR-02: Sistem HARUS menampilkan katalog buku dengan 
       pencarian berdasarkan judul, penulis, ISBN, atau 
       kategori.

FR-03: Sistem HARUS memproses peminjaman buku dengan batas 
       maksimal 3 buku per mahasiswa secara bersamaan.

FR-04: Sistem HARUS mengirim notifikasi email/WhatsApp 
       3 hari sebelum batas pengembalian.

FR-05: Sistem HARUS memungkinkan pustakawan menambah, 
       mengedit, dan menghapus data buku dari katalog.

FR-06: Sistem HARUS menghasilkan laporan statistik 
       peminjaman per bulan, per kategori, dan per prodi.

FR-07: Sistem HARUS mencatat riwayat peminjaman setiap 
       anggota (mahasiswa dan dosen).

FR-08: Sistem HARUS mendukung perpanjangan masa peminjaman 
       secara online (maksimal 1 kali per peminjaman).

FR-09: Sistem HARUS menghitung dan menampilkan denda 
       keterlambatan (Rp 1.000 per hari per buku).

FR-10: Sistem HARUS memungkinkan mahasiswa mereservasi buku 
       yang sedang dipinjam oleh orang lain.
```

**Tips menulis FR:**
- Gunakan kata kerja jelas: "Sistem HARUS..." (wajib), "Sistem SEBAIKNYA..." (opsional)
- Satu requirement = satu fungsi (jangan gabung beberapa fitur)
- Berikan ID unik (FR-01, FR-02, dst.)

### 3.4.2 Non-Functional Requirements (NFR)

Non-functional requirements mendefinisikan **BAGAIMANA** sistem harus bekerja — kualitas, batasan, dan constraint.

**Kategori NFR berdasarkan ISO 25010 (Software Quality Model):**

```
                    ┌─────────────────────────┐
                    │   SOFTWARE QUALITY      │
                    │   (ISO 25010)           │
                    └────────────┬────────────┘
                                 │
    ┌────────┬────────┬─────────┼─────────┬─────────┬────────┐
    ▼        ▼        ▼         ▼         ▼         ▼        ▼
┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
│Functio-││Perfor- ││Compati-││Usabi-  ││Relia-  ││Secu-   ││Maintain│
│nality  ││mance   ││bility  ││lity    ││bility  ││rity    ││ability │
└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘└────────┘
```

**Contoh NFR dengan metrik terukur:**

| ID | Kategori | Requirement | Metrik |
|----|----------|-------------|--------|
| NFR-01 | **Performance** | Halaman pencarian harus loading dalam < 3 detik pada koneksi 4G | Response time |
| NFR-02 | **Scalability** | Sistem harus mendukung 500 pengguna bersamaan tanpa degradasi | Concurrent users |
| NFR-03 | **Security** | Data personal (NIM, email) harus dienkripsi saat tersimpan (AES-256) | Encryption standard |
| NFR-04 | **Availability** | Sistem harus memiliki uptime minimal 99.5% (downtime max 8.76 jam/tahun) | SLA |
| NFR-05 | **Usability** | Mahasiswa baru harus bisa menyelesaikan peminjaman buku dalam < 5 menit tanpa training | Task completion time |
| NFR-06 | **Compatibility** | Sistem harus berjalan di Chrome, Firefox, Safari versi terbaru, dan mobile browser | Browser support |
| NFR-07 | **Reliability** | Sistem harus mampu recovery dalam < 1 jam setelah kegagalan | Mean Time to Recovery |
| NFR-08 | **Maintainability** | Kode harus memiliki test coverage minimal 70% | Code coverage |
| NFR-09 | **Accessibility** | Sistem harus memenuhi WCAG 2.1 Level AA | Accessibility standard |
| NFR-10 | **Localization** | Sistem harus mendukung bahasa Indonesia sebagai bahasa utama | Language support |

### 3.4.3 Perbandingan FR vs NFR

| Aspek | Functional Requirements | Non-Functional Requirements |
|-------|------------------------|---------------------------|
| **Fokus** | Apa yang sistem lakukan | Bagaimana sistem bekerja |
| **Contoh** | "Sistem bisa mencari buku" | "Pencarian respond < 2 detik" |
| **Sumber** | Stakeholder, proses bisnis | Standar industri, regulasi, SLA |
| **Testable** | Ya — cek apakah fitur ada | Ya — ukur metrik kualitas |
| **Impact jika gagal** | Fitur tidak ada | Sistem lambat, rentan, sulit dipakai |
| **Prioritas** | Langsung terlihat oleh pengguna | Sering diabaikan tapi krusial |

### 3.4.4 Domain Requirements dan Constraints

Selain FR dan NFR, ada juga:

- **Domain Requirements**: kebutuhan yang berasal dari domain aplikasi (regulasi, standar industri)
  - Contoh: "Sistem BPJS harus sesuai dengan Permenkes No. 28/2014 tentang JKN"
- **Constraints**: batasan yang membatasi solusi desain
  - Contoh: "Sistem harus menggunakan database MySQL karena lisensi yang dimiliki kampus"

---

## 3.5 Software Requirements Specification (SRS)

### 3.5.1 Apa Itu SRS?

**Software Requirements Specification (SRS)** adalah dokumen formal yang mendefinisikan secara lengkap dan tidak ambigu apa yang harus dilakukan perangkat lunak. SRS menjadi **kontrak** antara stakeholder dan tim pengembang.

### 3.5.2 Standar SRS: IEEE 830 dan ISO 29148

| Aspek | IEEE 830 (1998) | ISO/IEC/IEEE 29148 (2018) |
|-------|-----------------|---------------------------|
| **Status** | Standar klasik, masih banyak digunakan | Standar terbaru, menggantikan IEEE 830 |
| **Fokus** | Template SRS | Seluruh proses requirements engineering |
| **Kelebihan** | Sederhana, banyak referensi | Lebih komprehensif, life cycle perspective |
| **Penggunaan** | Proyek tradisional & akademik | Proyek besar, standar internasional |

### 3.5.3 Template Lengkap SRS (IEEE 830)

```
═══════════════════════════════════════════════════════════════
     SOFTWARE REQUIREMENTS SPECIFICATION (SRS)
     Sistem Perpustakaan Digital — Universitas Al Azhar Indonesia
     Versi: 1.0 | Tanggal: 20 Maret 2026
═══════════════════════════════════════════════════════════════

1. PENDAHULUAN
   1.1 Tujuan
       Dokumen ini mendeskripsikan kebutuhan fungsional dan 
       non-fungsional untuk Sistem Perpustakaan Digital UAI 
       versi 1.0.

   1.2 Ruang Lingkup
       Sistem mencakup: katalog online, peminjaman/pengembalian
       digital, notifikasi otomatis, dan laporan statistik.
       Tidak termasuk: e-book reader, integrasi OPAC nasional.

   1.3 Definisi, Akronim, dan Singkatan
       - SRS   : Software Requirements Specification
       - NIM   : Nomor Induk Mahasiswa
       - OPAC  : Online Public Access Catalog
       - UAI   : Universitas Al Azhar Indonesia

   1.4 Referensi
       - IEEE Std 830-1998
       - ISO/IEC/IEEE 29148:2018
       - Peraturan Perpustakaan UAI No. 12/2024

   1.5 Overview Dokumen
       Bagian 2 menjelaskan deskripsi umum produk.
       Bagian 3 mendefinisikan kebutuhan spesifik.

2. DESKRIPSI UMUM
   2.1 Perspektif Produk
       Sistem ini menggantikan proses manual peminjaman buku
       menggunakan buku log. Sistem berdiri sendiri (standalone)
       dengan rencana integrasi ke SIA UAI di versi 2.0.

       ┌──────────┐     ┌──────────────────┐     ┌──────────┐
       │ Browser  │────▶│  Web Application │────▶│ Database │
       │(Mhs/Dosen│     │  (Flask/Python)  │     │ (MySQL)  │
       │/Pustaka- │     │                  │     │          │
       │  wan)    │◀────│  - Auth Module   │◀────│          │
       └──────────┘     │  - Catalog Module│     └──────────┘
                        │  - Loan Module   │
                        │  - Report Module │
                        └──────────────────┘

   2.2 Fungsi Produk (Ringkasan)
       - Manajemen katalog buku
       - Peminjaman dan pengembalian buku
       - Pencarian dan filter buku
       - Notifikasi otomatis
       - Laporan dan statistik

   2.3 Karakteristik Pengguna
       | Pengguna   | Jumlah | Kemampuan IT      |
       |------------|--------|-------------------|
       | Mahasiswa  | ~4000  | Menengah-tinggi   |
       | Dosen      | ~200   | Rendah-menengah   |
       | Pustakawan | 5      | Rendah-menengah   |
       | Admin IT   | 2      | Tinggi            |

   2.4 Batasan
       - Database harus MySQL (lisensi kampus)
       - Hosting di server kampus (tidak cloud)
       - Budget pengembangan: Rp 50 juta
       - Deadline: 6 bulan dari kick-off

   2.5 Asumsi dan Dependensi
       - Koneksi internet kampus stabil (min 10 Mbps)
       - Data buku existing akan dimigrasi dari Excel
       - Mahasiswa memiliki akun email @uai.ac.id

3. KEBUTUHAN SPESIFIK
   3.1 External Interface Requirements
       3.1.1 User Interface
             - Responsive web design (desktop + mobile)
             - Bahasa Indonesia sebagai default
             - Warna sesuai branding UAI (hijau-emas)
       
       3.1.2 Hardware Interface
             - Barcode scanner untuk ISBN buku
             - Printer untuk slip peminjaman (opsional)
       
       3.1.3 Software Interface
             - Database: MySQL 8.0
             - Email: SMTP server kampus
             - WhatsApp API: Twilio/Fonnte
       
       3.1.4 Communications Interface
             - HTTPS untuk semua komunikasi
             - REST API untuk integrasi masa depan

   3.2 Functional Requirements
       [FR-01 sampai FR-10 seperti di Section 3.4.1]

   3.3 Non-Functional Requirements
       [NFR-01 sampai NFR-10 seperti di Section 3.4.2]

   3.4 Design Constraints
       - Framework: Flask (Python)
       - ORM: SQLAlchemy
       - Frontend: HTML/CSS/JavaScript (Bootstrap 5)
       - Version Control: Git + GitHub
```

### 3.5.4 Kualitas Requirements yang Baik

Setiap requirement yang ditulis dalam SRS harus memenuhi kriteria berikut:

| Kriteria | Penjelasan | Contoh Buruk | Contoh Baik |
|----------|-----------|--------------|-------------|
| **Unambiguous** (Jelas) | Hanya ada satu interpretasi | "Sistem harus cepat" | "Response time < 3 detik pada koneksi 4G" |
| **Testable** (Bisa diuji) | Ada kriteria pass/fail yang jelas | "Sistem harus user-friendly" | "Mahasiswa baru bisa meminjam buku dalam < 5 menit tanpa training" |
| **Consistent** (Konsisten) | Tidak bertentangan dengan requirement lain | FR-03: "Max 3 buku" vs FR-08: "Max 5 buku" | Pastikan angka konsisten di seluruh dokumen |
| **Complete** (Lengkap) | Mencakup semua kebutuhan yang diketahui | Tidak ada requirements tentang error handling | Tambahkan: "Sistem harus menampilkan pesan error yang informatif" |
| **Feasible** (Layak) | Bisa diimplementasikan dengan teknologi yang ada | "Sistem harus 100% bebas bug" | "Test coverage minimal 80%" |
| **Traceable** (Bisa dilacak) | Bisa dilacak ke sumber dan ke implementasi | Requirement tanpa ID atau sumber | "FR-01 [Sumber: Interview Bu Siti, 15/3/2026]" |

### 3.5.5 Anti-Pattern: Requirement yang Buruk

```
═══════════════════════════════════════════════════════════════
CONTOH REQUIREMENTS BURUK DAN PERBAIKANNYA
═══════════════════════════════════════════════════════════════

BURUK: "Sistem harus memiliki performa yang baik"
  → Ambigu, tidak terukur
BAIK:  "Halaman harus loading < 3 detik pada koneksi 4G
        dengan beban 200 concurrent users"

BURUK: "Sistem harus aman"
  → Terlalu umum
BAIK:  "Password harus minimal 8 karakter dengan kombinasi
        huruf besar, huruf kecil, angka, dan simbol.
        Session timeout setelah 30 menit tidak aktif."

BURUK: "Sistem harus bisa menangani banyak data"
  → "Banyak" berapa?
BAIK:  "Database harus mampu menyimpan minimal 100.000 
        record buku dan 50.000 record anggota."

BURUK: "Sistem harus user-friendly"
  → Subjektif
BAIK:  "90% pengguna harus berhasil menyelesaikan task
        peminjaman buku pada percobaan pertama (usability
        testing)."

BURUK: "Sistem harus support semua browser"
  → Tidak realistis
BAIK:  "Sistem harus berjalan di Chrome 120+, Firefox 120+,
        Safari 17+, dan Edge 120+ (desktop dan mobile)."
```

---

## 3.6 Validasi Requirements

### 3.6.1 Mengapa Validasi Penting?

Validasi memastikan bahwa requirements yang didokumentasikan **benar-benar mencerminkan kebutuhan stakeholder**. Validasi berbeda dari verifikasi:

| Aspek | Verifikasi (*Verification*) | Validasi (*Validation*) |
|-------|---------------------------|------------------------|
| **Pertanyaan** | "Apakah kita membangun produk dengan **benar**?" | "Apakah kita membangun produk yang **benar**?" |
| **Fokus** | Kesesuaian dengan spesifikasi | Kesesuaian dengan kebutuhan nyata |
| **Dilakukan oleh** | Tim QA/pengembang | Stakeholder + tim RE |

### 3.6.2 Teknik Validasi Requirements

| Teknik | Deskripsi | Efektif Untuk |
|--------|-----------|--------------|
| **Requirements Review** | Stakeholder membaca SRS dan memberikan feedback formal | Semua jenis requirements |
| **Prototyping** | Buat mock-up/prototype untuk konfirmasi pemahaman | UI/UX requirements, unclear requirements |
| **Test Case Generation** | Jika bisa dibuat test case, requirement cukup jelas dan testable | Functional requirements |
| **Walkthrough** | Presentasi SRS kepada stakeholder, jelaskan setiap requirement | Requirements kompleks |
| **Inspection** | Review formal dengan checklist oleh tim independent | Proyek kritikal, safety-critical |
| **Model Validation** | Validasi model (use case, activity diagram) bersama stakeholder | Requirements yang dimodelkan |

### 3.6.3 Checklist Validasi Requirements

```
═══════════════════════════════════════════════════════════════
CHECKLIST VALIDASI SRS — Perpustakaan Digital UAI
═══════════════════════════════════════════════════════════════

COMPLETENESS (Kelengkapan)
  □ Semua stakeholder sudah diidentifikasi?
  □ Semua functional requirements tercover?
  □ Non-functional requirements sudah lengkap?
  □ Error handling dan edge cases sudah dipertimbangkan?
  □ Semua external interfaces sudah didefinisikan?

CONSISTENCY (Konsistensi)
  □ Tidak ada requirement yang bertentangan?
  □ Terminologi konsisten di seluruh dokumen?
  □ Angka dan batasan konsisten?
  □ Tidak ada duplikasi requirements?

CLARITY (Kejelasan)
  □ Setiap requirement hanya memiliki satu interpretasi?
  □ Tidak ada kata ambigu ("cepat", "baik", "banyak")?
  □ Semua istilah teknis sudah didefinisikan di glossary?

TESTABILITY (Kemampuan diuji)
  □ Setiap requirement memiliki kriteria pass/fail?
  □ Metrik untuk NFR sudah terukur?
  □ Test case bisa dibuat untuk setiap requirement?

FEASIBILITY (Kelayakan)
  □ Semua requirement bisa diimplementasi dengan budget?
  □ Timeline realistis untuk scope requirements?
  □ Teknologi yang dipilih mendukung semua requirements?

TRACEABILITY (Ketertelusuran)
  □ Setiap requirement memiliki ID unik?
  □ Setiap requirement bisa dilacak ke sumbernya?
  □ Forward traceability ke design/test sudah disiapkan?
```

---

## 3.7 Requirements Traceability Matrix (RTM)

### 3.7.1 Apa Itu RTM?

**Requirements Traceability Matrix** adalah tabel yang melacak setiap requirement dari sumber awalnya hingga implementasi dan pengujian. RTM memastikan tidak ada requirement yang "hilang" selama pengembangan.

### 3.7.2 Contoh RTM

| Req ID | Requirement | Sumber | Prioritas | Design | Code | Test Case | Status |
|--------|------------|--------|-----------|--------|------|-----------|--------|
| FR-01 | Registrasi dengan NIM + email | Interview Bu Siti | Must | D-01 | auth.py | TC-01 | Done |
| FR-02 | Pencarian katalog buku | Survey Mhs, Interview | Must | D-02 | catalog.py | TC-02 | In Progress |
| FR-03 | Peminjaman max 3 buku | SOP Perpustakaan | Must | D-03 | loan.py | TC-03 | Planned |
| FR-04 | Notifikasi deadline | Interview Bu Siti | Should | D-04 | notify.py | TC-04 | Planned |
| NFR-01 | Response time < 3 detik | Best practice | Must | D-05 | - | TC-P01 | Planned |

### 3.7.3 Jenis Traceability

```
               BACKWARD                        FORWARD
            TRACEABILITY                     TRACEABILITY
                 │                                │
    ┌────────────┤                                │
    ▼            │                                ▼
┌─────────┐  ┌──┴───────┐  ┌──────────┐  ┌──────────┐
│ Sumber  │──│Requirement│──│  Design  │──│Test Case │
│(Stk/Reg)│  │  (SRS)   │  │  (Code)  │  │ (Result) │
└─────────┘  └──────────┘  └──────────┘  └──────────┘

Backward: "Requirement ini berasal dari mana?"
Forward:  "Requirement ini diimplementasikan di mana? 
           Dan diuji dengan test case apa?"
```

---

## 3.8 Studi Kasus: Kompleksitas Requirements BPJS Kesehatan

### 3.8.1 Konteks

BPJS Kesehatan adalah sistem jaminan kesehatan nasional yang melayani **200+ juta peserta** di seluruh Indonesia. Pengembangan sistem informasinya merupakan salah satu proyek RE paling kompleks di Indonesia.

### 3.8.2 Tantangan RE pada Sistem BPJS

| Tantangan | Penjelasan | Dampak |
|-----------|-----------|--------|
| **Stakeholder sangat banyak** | Pasien, RS, klinik, dokter, apotek, Kemenkes, DJSN, DPR | Konflik kepentingan, requirements bertentangan |
| **Regulasi berubah sering** | Permenkes berubah 2-3x setahun | Requirements tidak stabil, rework tinggi |
| **Skala masif** | 200+ juta peserta, 25.000+ faskes | NFR (scalability, availability) sangat ketat |
| **Integrasi kompleks** | Bridging dengan 5000+ RS, apotek, lab | Interface requirements sangat banyak |
| **Keamanan data medis** | Data kesehatan sensitif, regulasi privasi | Security requirements ketat |

### 3.8.3 Pelajaran dari BPJS untuk Mahasiswa

```
═══════════════════════════════════════════════════════════════
LESSONS LEARNED: RE Sistem Berskala Besar
═══════════════════════════════════════════════════════════════

1. STAKEHOLDER MANAGEMENT
   → Identifikasi semua stakeholder sejak awal
   → Gunakan Power-Interest Matrix
   → Fasilitasi konflik antar stakeholder

2. REQUIREMENTS PRIORITIZATION
   → Tidak semua bisa dibuat sekaligus
   → Gunakan MoSCoW + iterative delivery
   → MVP (Minimum Viable Product) first

3. CHANGE MANAGEMENT
   → Requirements PASTI berubah
   → Siapkan proses change request formal
   → Impact analysis sebelum menyetujui perubahan

4. TRACEABILITY
   → RTM wajib untuk proyek besar
   → Setiap requirement harus bisa dilacak
   → Gunakan tools (Jira, Azure DevOps)

5. VALIDASI BERKELANJUTAN
   → Jangan validasi hanya di akhir
   → Prototype early, validate often
   → User acceptance testing (UAT) berkala
```

---

## 3.9 AI Corner: AI untuk Requirements Engineering (Level: Basic)

### 3.9.1 Pengantar AI dalam RE

AI (seperti ChatGPT, Claude, Copilot) dapat menjadi **asisten** dalam proses requirements engineering. Namun, AI **tidak menggantikan** interaksi langsung dengan stakeholder — AI tidak memahami konteks lokal, politik organisasi, atau kebutuhan implisit.

### 3.9.2 Menggunakan AI untuk Brainstorm Requirements

**Prompt:**
```
Saya sedang mengembangkan Sistem Perpustakaan Digital untuk 
kampus universitas di Jakarta dengan 4000 mahasiswa.
Sistem akan menggantikan proses manual (buku log).

Buatkan 15 functional requirements dan 10 non-functional 
requirements. Gunakan format:
- FR-XX: Sistem HARUS [deskripsi]
- NFR-XX: [Kategori] — [deskripsi dengan metrik terukur]
```

**Evaluasi Output AI:**
- Apakah requirements sesuai konteks Indonesia (bukan konteks US/Eropa)?
- Apakah ada requirements yang tidak relevan untuk kampus kecil-menengah?
- Apakah NFR memiliki metrik yang terukur?
- Apakah ada kebutuhan yang missed oleh AI (misal: integrasi WhatsApp, BPJS, dll.)?

### 3.9.3 Menggunakan AI untuk Menyusun Interview Script

**Prompt:**
```
Buatkan daftar 15 pertanyaan interview untuk elicitation 
requirements Sistem Perpustakaan Digital kampus.
Interviewee: Pustakawan senior dengan 10 tahun pengalaman.

Format pertanyaan: semi-structured interview.
Kelompokkan pertanyaan menjadi:
1. Proses saat ini (as-is)
2. Masalah dan pain points  
3. Kebutuhan masa depan (to-be)
4. Batasan dan constraint
```

### 3.9.4 Menggunakan AI untuk Validasi Requirements

**Prompt:**
```
Analisis requirements berikut dan identifikasi masalah:
1. Ambigu — requirement yang bisa diinterpretasi berbeda
2. Tidak testable — tidak ada kriteria pass/fail
3. Inkonsisten — bertentangan satu sama lain
4. Incomplete — ada gap yang perlu diisi

Requirements:
FR-01: Sistem harus cepat
FR-02: Sistem harus aman
FR-03: Mahasiswa bisa meminjam max 3 buku
FR-04: Dosen bisa meminjam max 10 buku
FR-05: Semua pengguna bisa meminjam max 5 buku
...
```

### 3.9.5 Menggunakan AI untuk Generate SRS Draft

**Prompt:**
```
Buatkan draft SRS sesuai template IEEE 830 untuk Sistem 
Perpustakaan Digital kampus dengan spesifikasi:
- 4000 mahasiswa, 200 dosen
- Web-based (Flask + MySQL)
- Fitur: katalog, peminjaman, notifikasi, laporan
- Hosting: server kampus

Sertakan: user interface requirements, hardware interface,
software interface, dan communication interface.
```

### 3.9.6 Batasan dan Peringatan

> **PENTING**: AI bisa menghasilkan requirements yang terlihat profesional tetapi:
> - Tidak sesuai konteks lokal (misal: mengasumsikan credit card payment padahal di Indonesia lebih umum transfer bank/QRIS)
> - Terlalu generik (tidak spesifik untuk domain perpustakaan kampus)
> - Missing cultural context (tidak mempertimbangkan jam ibadah, libur nasional Indonesia)
> - Over-engineered (merekomendasikan microservices untuk sistem yang hanya butuh monolith)
>
> **Selalu validasi output AI dengan stakeholder sebenarnya.**

### 3.9.7 Hands-on: Coba dan Evaluasi

**Latihan AI Corner:**
1. Gunakan ChatGPT/Claude untuk generate 10 FR untuk "Sistem Kantin UAI"
2. Review setiap requirement: apakah memenuhi 6 kriteria (jelas, testable, konsisten, lengkap, feasible, traceable)?
3. Perbaiki requirements yang tidak memenuhi kriteria
4. Catat di **AI Usage Log**: prompt yang digunakan, output AI, modifikasi yang dilakukan, refleksi

---

## Latihan Soal

### Level Dasar (C1-C2): 5 Soal

1. Jelaskan **lima tahap** proses requirements engineering beserta output masing-masing tahap.

2. Apa perbedaan antara **functional requirements** dan **non-functional requirements**? Berikan masing-masing 3 contoh untuk Sistem Informasi Akademik.

3. Sebutkan dan jelaskan **6 teknik elicitation** beserta kelebihan dan kekurangan masing-masing.

4. Sebutkan **6 kriteria** requirement yang baik menurut standar IEEE dan berikan contoh untuk setiap kriteria.

5. Jelaskan perbedaan antara **validasi** dan **verifikasi** requirements. Kapan masing-masing dilakukan?

### Level Menengah (C3-C4): 7 Soal

6. Buatlah **Power-Interest Matrix** untuk stakeholder proyek "Sistem Informasi Rumah Sakit" dengan minimal 8 stakeholder. Tentukan strategi komunikasi untuk setiap kuadran.

7. Buatlah **10 functional requirements** dan **5 non-functional requirements** (dengan metrik terukur) untuk Sistem Informasi Perpustakaan Kampus. Setiap requirement harus memiliki ID unik dan memenuhi 6 kriteria kualitas.

8. Tuliskan **interview script** (minimal 12 pertanyaan) untuk elicitation kebutuhan Sistem Antrian Puskesmas. Kelompokkan pertanyaan menjadi: proses saat ini, masalah, kebutuhan masa depan, dan batasan.

9. Analisis mengapa requirement berikut adalah requirement yang **buruk**, dan perbaiki menjadi requirement yang testable:
   - "Sistem harus memiliki performa yang baik"
   - "Sistem harus user-friendly"
   - "Sistem harus support banyak pengguna"
   - "Sistem harus aman dari hacker"

10. Buatlah **Requirements Traceability Matrix (RTM)** untuk 5 functional requirements dari Sistem Perpustakaan Digital, yang melacak dari sumber hingga test case.

11. Rancang **questionnaire** (15 pertanyaan, campuran terbuka dan tertutup) untuk mengumpulkan kebutuhan Sistem E-Commerce UMKM dari perspektif penjual dan pembeli.

12. Bandingkan teknik elicitation **interview** vs **workshop (JAD)** vs **prototyping** untuk skenario berikut:
    - Proyek baru tanpa sistem existing
    - Penggantian sistem legacy
    - Penambahan fitur ke sistem yang sudah berjalan

### Level Mahir (C5-C6): 7 Soal

13. Seorang klien startup e-commerce meminta fitur baru setiap minggu dan mengubah prioritas setiap sprint. Bagaimana Anda mengelola requirements yang terus berubah? Rancang proses **requirements management** yang cocok untuk konteks Agile.

14. Evaluasi SRS berikut untuk "Sistem Parkir Kampus" dan identifikasi **minimal 7 masalah** (ambiguitas, inkonsistensi, incompleteness, infeasibility):
    - "Sistem harus cepat dan responsif"
    - "Sistem mendukung semua kendaraan"
    - "Tarif parkir sesuai kebijakan kampus"
    - "Sistem harus aman"
    - "Sistem bisa diakses 24 jam"
    - "Mahasiswa bisa parkir gratis"
    - "Staff membayar Rp 5.000 per hari"
    - "Semua pengguna membayar parkir"

15. Anda ditugaskan sebagai Requirements Analyst untuk proyek "Sistem Informasi Zakat" yang mencakup pengumpulan, distribusi, dan pelaporan zakat. Buatlah **SRS lengkap** (IEEE 830) dengan minimal 15 FR dan 8 NFR.

16. Analisis **trade-off** antara non-functional requirements berikut dan jelaskan strategi penyelesaiannya:
    - Performance vs Security (enkripsi memperlambat response time)
    - Usability vs Security (banyak langkah autentikasi = lebih aman tapi ribet)
    - Cost vs Availability (99.99% uptime sangat mahal)

17. Rancang proses **Requirements Engineering lengkap** untuk proyek "Digitalisasi Layanan Kelurahan" — dari stakeholder identification hingga requirements sign-off. Sertakan timeline, teknik elicitation yang digunakan per stakeholder, dan deliverable setiap fase.

18. Bandingkan pendekatan RE dalam **Waterfall** vs **Agile**. Kapan SRS lengkap diperlukan? Kapan user story cukup? Berikan analisis dengan contoh proyek nyata di Indonesia.

19. Anda menemukan bahwa 3 dari 5 stakeholder utama memiliki requirements yang saling bertentangan. Rancang strategi **conflict resolution** dan jelaskan teknik negosiasi yang akan Anda gunakan.

---

## Rangkuman

1. **Requirements Engineering (RE)** adalah proses sistematik untuk menemukan, mendokumentasikan, dan memelihara kebutuhan software — RE yang buruk adalah penyebab utama kegagalan proyek.

2. **Stakeholder analysis** menggunakan Power-Interest Matrix untuk menentukan strategi keterlibatan setiap stakeholder.

3. **Proses RE** terdiri dari 5 fase iteratif: Elicitation, Analysis, Specification, Validation, dan Management.

4. **6+ teknik elicitation** (interview, observation, questionnaire, workshop, prototyping, document analysis) memiliki kelebihan dan kekurangan masing-masing — gunakan kombinasi beberapa teknik.

5. **Functional requirements** mendefinisikan APA yang sistem lakukan; **Non-functional requirements** mendefinisikan BAGAIMANA sistem bekerja (harus memiliki metrik terukur).

6. **SRS (IEEE 830/ISO 29148)** adalah format standar untuk dokumentasi requirements — terdiri dari Pendahuluan, Deskripsi Umum, dan Kebutuhan Spesifik.

7. Requirements harus memenuhi 6 kriteria kualitas: **jelas, testable, konsisten, lengkap, feasible, dan traceable**.

8. **Validasi** memastikan requirements sesuai kebutuhan stakeholder sebenarnya — gunakan review, prototyping, test case generation, dan walkthrough.

9. **Requirements Traceability Matrix (RTM)** melacak setiap requirement dari sumber hingga implementasi dan pengujian.

10. **AI** bisa membantu brainstorm dan draft requirements, tetapi **tidak menggantikan** interaksi langsung dengan stakeholder — selalu validasi output AI.

---

## Referensi

1. Wiegers, K. E. & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press.
2. IEEE Std 830-1998. *Recommended Practice for Software Requirements Specifications*.
3. ISO/IEC/IEEE 29148:2018. *Systems and Software Engineering — Life Cycle Processes — Requirements Engineering*.
4. Sommerville, I. (2016). *Software Engineering* (10th ed.). Chapter 4-5. Pearson.
5. Robertson, S. & Robertson, J. (2012). *Mastering the Requirements Process* (3rd ed.). Addison-Wesley.
6. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill.
7. IEEE Computer Society. (2024). *SWEBOK v4* — Knowledge Area: Software Requirements.
8. Standish Group. (2020). *CHAOS Report: Beyond Infinity*.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
