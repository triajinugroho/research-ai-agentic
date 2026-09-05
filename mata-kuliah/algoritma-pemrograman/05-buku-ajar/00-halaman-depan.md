---
id: uai-inf101-buku-depan
tipe: bab-buku-ajar
judul: "Buku Ajar Algoritma dan Pemrograman — Halaman Depan"
kode_mk: INF-101
nama_mk: Algoritma dan Pemrograman
prodi: Informatika
bab: 0
level_ai: understand
cpmk: [CPMK-1, CPMK-2, CPMK-3, CPMK-4, CPMK-5, CPMK-6, CPMK-7]
sub_cpmk: []
bloom_c: []
bloom_a: []
bloom_p: []
versi: 2.0
status: draft
diperbarui: 2026-09-05
---

# BUKU AJAR
# ALGORITMA DAN PEMROGRAMAN
## Fondasi Computational Thinking dengan Python dan AI

### Untuk Mahasiswa Program Studi Informatika

**Penulis:**
# Tri Aji Nugroho, S.T., M.T.

**Program Studi Informatika**
**Fakultas Sains dan Teknologi**
**Universitas Al Azhar Indonesia**
**Jakarta, Februari 2026**

---

## Identitas Buku

| Komponen | Detail |
|----------|--------|
| Judul | Algoritma dan Pemrograman: Fondasi Computational Thinking dengan Python dan AI |
| Penulis | Tri Aji Nugroho, S.T., M.T. |
| Institusi | Universitas Al Azhar Indonesia |
| Fakultas | Sains dan Teknologi |
| Program Studi | Informatika |
| Edisi | Pertama, 2026 |
| Jumlah Bab | 14 Bab + Lampiran |
| Sasaran Pembaca | Mahasiswa S1 Informatika Semester 2 |
| Pendekatan | Outcome-Based Education (OBE), AI-Augmented |
| Bahasa Pemrograman | Python 3.x |
| Platform Praktikum | Google Colab |
| Tahun Terbit | 2026 |

---

## Kata Pengantar

بسم الله الرحمن الرحيم

*Assalamu'alaikum Warahmatullahi Wabarakatuh*

Segala puji bagi Allah SWT, Tuhan semesta alam, yang telah melimpahkan rahmat, taufik, dan hidayah-Nya sehingga buku ajar **"Algoritma dan Pemrograman: Fondasi Computational Thinking dengan Python dan AI"** ini dapat diselesaikan. Shalawat serta salam semoga senantiasa tercurah kepada Nabi Muhammad SAW, keluarga, sahabat, dan seluruh umatnya.

### Mengapa Buku Ini Ditulis?

Buku ini lahir dari keresahan sekaligus harapan. Keresahan melihat bahwa pembelajaran algoritma dan pemrograman sering kali terjebak dalam pendekatan yang terlalu prosedural --- mahasiswa menghafal sintaks tanpa memahami *mengapa* suatu solusi dirancang demikian. Harapannya, buku ini menjadi jembatan yang menghubungkan fondasi berpikir komputasional (*computational thinking*) dengan praktik pemrograman modern yang diperkaya oleh kecerdasan buatan (AI).

### Warisan Al-Khwarizmi

Kata "algoritma" sendiri berasal dari nama ilmuwan Muslim abad ke-9, **Abu Abdullah Muhammad ibn Musa al-Khwarizmi**, yang karyanya *Kitab al-Jabr wa al-Muqabala* menjadi fondasi aljabar modern. Sebagai institusi pendidikan yang berlandaskan nilai-nilai Islam, Universitas Al Azhar Indonesia memiliki tanggung jawab moral dan intelektual untuk melanjutkan tradisi keilmuan ini. Buku ini adalah salah satu wujud ikhtiar tersebut --- menghubungkan warisan intelektual peradaban Islam dengan tantangan teknologi masa kini.

### Era AI dan Transformasi Pembelajaran

Tahun 2026 menandai era di mana AI generatif telah menjadi bagian tak terpisahkan dari ekosistem pengembangan perangkat lunak. Mahasiswa tidak lagi bisa mengabaikan keberadaan tools seperti GitHub Copilot, ChatGPT, dan Claude sebagai asisten pemrograman. Namun, tanpa fondasi algoritma dan *computational thinking* yang kuat, penggunaan AI justru berpotensi menjadi jebakan --- menghasilkan kode yang berjalan tetapi tidak dipahami, efisien secara permukaan tetapi rapuh secara fundamental.

Buku ini mengambil pendekatan unik: **AI-Augmented Learning**. Setiap bab dilengkapi dengan **AI Corner** yang mengajarkan mahasiswa cara berinteraksi dengan AI secara produktif dan kritis. Bukan menggantikan pemahaman, melainkan memperdalam dan memperluas kemampuan berpikir algoritmik.

### Pendekatan OBE (Outcome-Based Education)

Seluruh materi dalam buku ini dirancang mengikuti kerangka **Outcome-Based Education (OBE)**, di mana setiap bab memiliki Capaian Pembelajaran Mata Kuliah (CPMK) yang terukur dan terhubung langsung dengan Capaian Pembelajaran Lulusan (CPL) program studi. Setiap aktivitas pembelajaran --- dari latihan kode hingga proyek akhir --- dirancang untuk memastikan mahasiswa benar-benar mencapai kompetensi yang ditargetkan.

### Ucapan Terima Kasih

Penulis mengucapkan terima kasih yang sebesar-besarnya kepada:

1. **Rektor Universitas Al Azhar Indonesia** atas dukungan terhadap pengembangan bahan ajar berbasis riset dan inovasi.
2. **Dekan Fakultas Sains dan Teknologi** atas arahan strategis dalam pengembangan kurikulum berbasis OBE.
3. **Ketua Program Studi Informatika** beserta seluruh dosen sejawat atas diskusi akademik yang memperkaya konten buku ini.
4. **Mahasiswa Prodi Informatika UAI** yang menjadi inspirasi utama penulisan buku ini --- semoga buku ini membantu perjalanan kalian menjadi *problem solver* yang tangguh dan beretika.
5. **Keluarga tercinta** atas kesabaran dan dukungan tanpa henti selama proses penulisan.

Penulis menyadari bahwa buku ini masih jauh dari sempurna. Segala kritik dan saran yang membangun sangat diharapkan demi perbaikan edisi berikutnya. Semoga buku ini menjadi amal jariyah yang bermanfaat bagi pengembangan pendidikan informatika di Indonesia.

*Wallahu a'lam bishawab.*

*Wassalamu'alaikum Warahmatullahi Wabarakatuh*

Jakarta, Februari 2026

**Tri Aji Nugroho, S.T., M.T.**
Program Studi Informatika
Fakultas Sains dan Teknologi
Universitas Al Azhar Indonesia

---

## Daftar Isi

| No. | Konten | Halaman |
|-----|--------|---------|
| | Kata Pengantar | iii |
| | Daftar Isi | v |
| | Mengapa Buku Ini? | ix |
| | | |
| | **BAGIAN I: FONDASI** | |
| 1 | Bab 1: Pengantar Algoritma dan Computational Thinking | 1 |
| | 1.1 Apa Itu Algoritma? | 2 |
| | 1.2 Computational Thinking: Empat Pilar | 5 |
| | 1.3 Pengenalan Python dan Lingkungan Kerja | 10 |
| | 1.4 AI Corner: Mengenal AI sebagai Asisten Belajar | 15 |
| 2 | Bab 2: Variabel, Tipe Data, dan Operator | 19 |
| | 2.1 Konsep Variabel dan Penugasan | 20 |
| | 2.2 Tipe Data Dasar (int, float, str, bool) | 24 |
| | 2.3 Operator Aritmatika, Perbandingan, dan Logika | 28 |
| | 2.4 AI Corner: Bertanya kepada AI tentang Tipe Data | 33 |
| 3 | Bab 3: Struktur Kontrol: Seleksi | 37 |
| | 3.1 Percabangan if, elif, else | 38 |
| | 3.2 Nested Conditionals | 42 |
| | 3.3 Studi Kasus: Sistem Keputusan | 46 |
| | 3.4 AI Corner: Menggunakan AI untuk Memahami Logika | 50 |
| 4 | Bab 4: Struktur Kontrol: Perulangan | 53 |
| | 4.1 Perulangan for dan while | 54 |
| | 4.2 Kontrol Loop: break, continue, else | 58 |
| | 4.3 Nested Loops dan Pola | 62 |
| | 4.4 AI Corner: AI Menjelaskan Trace Eksekusi | 66 |
| | | |
| | **BAGIAN II: MODULARITAS** | |
| 5 | Bab 5: Fungsi dan Modularitas | 71 |
| | 5.1 Mendefinisikan dan Memanggil Fungsi | 72 |
| | 5.2 Parameter, Return Value, dan Scope | 76 |
| | 5.3 Dokumentasi dan Best Practices | 80 |
| | 5.4 AI Corner: AI untuk Debugging dan Refactoring Fungsi | 84 |
| 6 | Bab 6: String dan Pengolahan Teks | 89 |
| | 6.1 Operasi String dan Metode Bawaan | 90 |
| | 6.2 Formatting dan f-string | 94 |
| | 6.3 Studi Kasus: Text Processing | 98 |
| | 6.4 AI Corner: AI untuk Refactoring Kode String | 102 |
| 7 | Bab 7: List, Tuple, dan Operasi Koleksi | 105 |
| | 7.1 List: Membuat, Mengakses, dan Memanipulasi | 106 |
| | 7.2 Tuple dan Perbedaannya dengan List | 110 |
| | 7.3 List Comprehension | 114 |
| | 7.4 AI Corner: AI Membantu Debugging Koleksi | 118 |
| | | |
| | **BAGIAN III: STRUKTUR DATA & ALGORITMA** | |
| 8 | Bab 8: Dictionary, Set, dan Pemilihan Struktur Data | 123 |
| | 8.1 Dictionary: Key-Value Pairs | 124 |
| | 8.2 Set dan Operasi Himpunan | 128 |
| | 8.3 Memilih Struktur Data yang Tepat | 132 |
| | 8.4 AI Corner: AI untuk Desain Struktur Data | 136 |
| 9 | Bab 9: Algoritma Pencarian (Searching) | 141 |
| | 9.1 Linear Search | 142 |
| | 9.2 Binary Search | 146 |
| | 9.3 Analisis Perbandingan | 150 |
| | 9.4 AI Corner: AI Membandingkan Algoritma Pencarian | 154 |
| 10 | Bab 10: Algoritma Pengurutan (Sorting) | 157 |
| | 10.1 Bubble Sort dan Selection Sort | 158 |
| | 10.2 Insertion Sort dan Merge Sort | 162 |
| | 10.3 Visualisasi dan Perbandingan | 166 |
| | 10.4 AI Corner: AI Menjelaskan Trace Sorting | 170 |
| 11 | Bab 11: Rekursi dan Pemecahan Masalah | 175 |
| | 11.1 Konsep Rekursi dan Base Case | 176 |
| | 11.2 Rekursi vs Iterasi | 180 |
| | 11.3 Divide and Conquer | 184 |
| | 11.4 AI Corner: AI untuk Analisis Algoritma Rekursif | 188 |
| | | |
| | **BAGIAN IV: FRONTIER** | |
| 12 | Bab 12: Kompleksitas Algoritma (Big-O) dan Optimasi | 193 |
| | 12.1 Notasi Big-O | 194 |
| | 12.2 Analisis Kompleksitas Waktu dan Ruang | 198 |
| | 12.3 Strategi Optimasi | 202 |
| | 12.4 AI Corner: AI Pair Programming untuk Optimasi | 206 |
| 13 | Bab 13: AI-Augmented Programming dan Code Quality | 211 |
| | 13.1 AI sebagai Programming Partner | 212 |
| | 13.2 Prompt Engineering untuk Kode | 216 |
| | 13.3 Code Review dengan AI | 220 |
| | 13.4 Etika dan Batasan AI dalam Pemrograman | 224 |
| 14 | Bab 14: Proyek Akhir: Membangun Solusi End-to-End | 229 |
| | 14.1 Metodologi Pengembangan Proyek | 230 |
| | 14.2 Pilihan Tema Proyek | 234 |
| | 14.3 Implementasi dan Dokumentasi | 238 |
| | 14.4 AI Corner: AI dalam Siklus Proyek Penuh | 242 |
| | | |
| | Penutup: Refleksi dan Langkah ke Depan | 247 |
| | Lampiran A: Instalasi dan Konfigurasi Lingkungan Python | 251 |
| | Lampiran B: Referensi Cepat Sintaks Python | 255 |
| | Lampiran C: Panduan Penggunaan Google Colab | 259 |
| | Lampiran D: Kumpulan Soal Latihan Tambahan | 263 |
| | Lampiran E: Rubrik Penilaian Proyek Akhir | 269 |
| | Lampiran F: Glosarium Istilah | 273 |
| | Daftar Pustaka | 277 |

---

## Peta Capaian Pembelajaran

### Hubungan CPL – CPMK – Bab

Peta ini **identik dengan RPS** ([`../01-rps/rps-algoritma-pemrograman.md`](../01-rps/rps-algoritma-pemrograman.md) §C–D). Rumusan lengkap CPL tidak diulang di sini — sumber tunggalnya adalah [`../../00-pedoman-obe/cpl-master.md`](../../00-pedoman-obe/cpl-master.md).

| CPL | Unsur | CPMK pengampu | Bab |
|---|---|---|---|
| **CPL03** — Pengetahuan cara kerja sistem komputer; penerapan algoritma untuk memecahkan masalah | Pengetahuan | CPMK-1, CPMK-2, CPMK-5, CPMK-6 | 1, 2, 7–11 |
| **CPL07** — Pemikiran logis, kritis, sistematis, inovatif dengan nilai-nilai Islami | Kemampuan Umum | CPMK-1, CPMK-3, CPMK-6 | 1, 3, 4, 9–11 |
| **CPL08** — Merancang dan mengembangkan algoritma untuk berbagai keperluan komputasi | Keterampilan Khusus | CPMK-2, CPMK-3, CPMK-4, CPMK-5, CPMK-6, CPMK-7 | 2–14 |
| **CPLUAI1** — Ketakwaan, etika, integritas, kepedulian sosial | Sikap | CPMK-7 | 13, 14 |
| **CPLUAI3** — Penalaran kritis, kreativitas, etika Islami dan akademik | Sikap | CPMK-7 | 13, 14 |

### Rantai Keterlacakan

```
Profil Lulusan (PL01, PL03, PL04)
  └── CPL (CPL03, CPL07, CPL08, CPLUAI1, CPLUAI3)
        └── Bahan Kajian (BK12, BK14, BK01)
              └── CPMK-1 .. CPMK-7
                    └── Sub-CPMK-1.1 .. Sub-CPMK-7.12  (55 capaian)
                          └── Bab 1-14  +  Asesmen (ASM-*)
```

| CPMK | Rumusan ringkas | Bab |
|---|---|---|
| **CPMK-1** | Konsep algoritma, *computational thinking*, dan peran pemrograman di era AI | 1 |
| **CPMK-2** | Variabel, tipe data, operator, dan ekspresi | 2 |
| **CPMK-3** | Struktur kontrol: seleksi dan perulangan | 3, 4 |
| **CPMK-4** | Fungsi, pengolahan string, dan modularitas | 5, 6 |
| **CPMK-5** | Pemilihan dan penggunaan struktur data | 7, 8 |
| **CPMK-6** | Algoritma pencarian, pengurutan, dan rekursi | 9, 10, 11 |
| **CPMK-7** | Efisiensi algoritma dan pemrograman berbantuan AI yang bertanggung jawab | 12, 13, 14 |

### Empat Fase Pembelajaran

```
 +-----------------+    +------------------+    +------------------------+    +----------------+
 |   FASE 1        |    |   FASE 2         |    |   FASE 3               |    |   FASE 4       |
 |   FONDASI       |--->|   MODULARITAS    |--->|   STRUKTUR DATA &      |--->|   FRONTIER     |
 |   (Bab 1-4)     |    |   (Bab 5-7)      |    |   ALGORITMA (Bab 8-11) |    |   (Bab 12-14)  |
 +-----------------+    +------------------+    +------------------------+    +----------------+
 |                 |    |                  |    |                        |    |                |
 | - Algoritma     |    | - Fungsi         |    | - Dictionary & Set     |    | - Big-O        |
 | - CT pillars    |    | - String         |    | - Searching            |    | - AI-Augmented |
 | - Variabel      |    | - List & Tuple   |    | - Sorting              |    | - Proyek Akhir |
 | - Seleksi       |    | - Modularitas    |    | - Rekursi              |    | - Code Quality |
 | - Perulangan    |    | - Reusability    |    | - Divide & Conquer     |    | - Optimasi     |
 |                 |    |                  |    |                        |    |                |
 | AI: Mengenal    |    | AI: Debugging    |    | AI: Desain &           |    | AI: Pair       |
 |     tools       |    |     Refactoring  |    |     Perbandingan       |    |     Programming |
 +-----------------+    +------------------+    +------------------------+    +----------------+
        |                       |                        |                          |
        v                       v                        v                          v
   Memahami              Menulis kode            Memilih struktur            Membangun solusi
   masalah &             modular &               data & algoritma            lengkap dengan
   merancang solusi      terdokumentasi          yang tepat                  bantuan AI
```

---

## Petunjuk Penggunaan Buku

### Bagaimana Menggunakan Buku Ini

Buku ini dirancang untuk digunakan selama **satu semester** (16 minggu perkuliahan) pada mata kuliah Algoritma dan Pemrograman. Setiap bab dirancang untuk diselesaikan dalam **satu hingga dua pertemuan** (masing-masing 2x50 menit), dengan proporsi:

- **30% Teori** --- Membaca dan memahami konsep melalui penjelasan dan ilustrasi
- **50% Praktik** --- Mengerjakan latihan kode secara langsung di Google Colab
- **20% Refleksi & AI** --- Berinteraksi dengan AI Corner dan mendiskusikan hasil

Mahasiswa disarankan untuk mengikuti urutan bab secara berurutan, karena setiap bab membangun di atas konsep yang telah dipelajari di bab sebelumnya.

### Konvensi Ikon

Sepanjang buku ini, Anda akan menemui ikon-ikon berikut yang menandai bagian-bagian khusus:

| Ikon | Nama | Keterangan |
|------|------|------------|
| **[AI]** | **AI Corner** | Aktivitas yang melibatkan interaksi dengan AI tools (ChatGPT, Claude, Copilot). Bagian ini mengajarkan cara menggunakan AI secara produktif dan kritis untuk memperdalam pemahaman algoritma. |
| **[L]** | **Latihan** | Soal-soal latihan yang harus dikerjakan untuk menguji pemahaman. Tersedia dalam tiga tingkat: Dasar, Menengah, dan Tantangan. |
| **[T]** | **Tips** | Saran praktis dan best practices dari pengalaman industri yang membantu menulis kode yang lebih baik dan efisien. |
| **[!]** | **Peringatan** | Kesalahan umum (*common pitfalls*) yang sering dilakukan pemula. Perhatikan bagian ini untuk menghindari bug dan miskonsepsi. |
| **[C]** | **Studi Kasus** | Contoh penerapan konsep dalam skenario dunia nyata, mulai dari sistem informasi hingga analisis data. |
| **[R]** | **Refleksi** | Pertanyaan reflektif yang mendorong mahasiswa untuk berpikir lebih dalam tentang konsep yang dipelajari dan menghubungkannya dengan pengalaman pribadi. |
| **[D]** | **Diskusi** | Topik untuk didiskusikan bersama dosen atau teman sejawat di kelas atau forum diskusi daring. |

### Prasyarat (Prerequisite)

Untuk mengikuti buku ini dengan baik, mahasiswa diharapkan memiliki:

1. **Kemampuan dasar komputer** --- Mampu mengoperasikan komputer, browser web, dan mengelola file.
2. **Logika matematika dasar** --- Memahami konsep logika dasar (AND, OR, NOT), aritmatika, dan aljabar sederhana.
3. **Akses internet** --- Diperlukan untuk menggunakan Google Colab dan AI tools.
4. **Akun Google** --- Untuk mengakses Google Colab sebagai platform praktikum utama.
5. **Rasa ingin tahu** --- Kemauan untuk belajar, bereksperimen, dan tidak takut membuat kesalahan.

Tidak diperlukan pengalaman pemrograman sebelumnya. Buku ini dimulai dari dasar dan membangun pemahaman secara bertahap.

### Platform Praktikum: Google Colab

Seluruh kode dalam buku ini dirancang untuk dijalankan di **Google Colaboratory (Google Colab)**, sebuah lingkungan notebook interaktif berbasis cloud yang:

- **Gratis** --- Tidak memerlukan instalasi atau biaya tambahan
- **Berbasis browser** --- Dapat diakses dari perangkat apapun dengan browser modern
- **Mendukung Python** --- Sudah terpasang Python beserta pustaka-pustaka populer
- **Kolaboratif** --- Memungkinkan berbagi dan bekerja sama secara real-time
- **Terintegrasi Google Drive** --- Menyimpan notebook secara otomatis

Panduan lengkap penggunaan Google Colab tersedia di **Lampiran C**.

---

## Progresi AI Literacy

Buku ini memperkenalkan keterampilan AI secara bertahap melalui fitur **AI Corner** di setiap bab. Progresi dirancang agar mahasiswa membangun kepercayaan diri dan kemampuan kritis secara incremental:

### Tahapan Progresi

Progresi mengikuti **UNESCO AI Competency Framework for Students** (pembaruan 16 Januari 2026), yang menetapkan tiga tingkat penguasaan: **Understand → Apply → Create**. Label lokal (Dasar/Menengah/Lanjut/Mahir) tetap dipakai sebagai padanan, namun tingkat UNESCO yang menjadi acuan.

| Tingkat UNESCO | Padanan lokal | Bab | Fokus AI Corner | Kompetensi yang dibangun |
|---|---|:-:|---|---|
| **Understand** | Dasar | 1 | Mengenal AI sebagai asisten belajar | Mengidentifikasi AI tools dan memahami cara kerjanya secara umum |
| **Understand** | Dasar | 2 | Bertanya kepada AI tentang tipe data dan galat | Menyusun *prompt* sederhana untuk penjelasan konsep dasar |
| **Understand** | Dasar | 3 | Memahami logika percabangan dengan AI | Meminta AI menjelaskan alur eksekusi kode sederhana |
| **Understand** | Dasar | 4 | AI menjelaskan *trace* eksekusi perulangan | Memvalidasi prediksi sendiri dengan bantuan AI |
| **Apply** | Menengah | 5 | AI untuk *debugging* dan *refactoring* fungsi | Menemukan bug dan memperbaiki struktur kode |
| **Apply** | Menengah | 6 | AI untuk *refactoring* kode pengolahan string | Mengevaluasi saran *refactoring* AI secara kritis |
| **Apply** | Menengah | 7 | AI membantu *debugging* koleksi data | Memahami galat pada struktur data kompleks |
| **Apply** | Lanjut | 8 | AI untuk desain struktur data | Berdiskusi tentang pemilihan struktur data yang optimal |
| **Apply** | Lanjut | 9 | AI membandingkan algoritma pencarian | Meminta AI menganalisis *trade-off* antar algoritma |
| **Apply** | Lanjut | 10 | AI menjelaskan *trace* pengurutan | Memvisualisasikan dan memahami algoritma kompleks |
| **Apply** | Lanjut | 11 | AI untuk analisis algoritma rekursif | Berdiskusi tentang strategi pemecahan masalah rekursif |
| **Create** | Mahir | 12 | AI *pair programming* untuk optimasi | Berkolaborasi mengoptimasi kompleksitas algoritma |
| **Create** | Mahir | 13 | *Code review* dan *prompt engineering* lanjut | Menggunakan AI secara profesional dan menjaga kualitas kode |
| **Create** | Mahir | 14 | AI dalam siklus proyek penuh | Mengintegrasikan AI di seluruh fase pengembangan |

### Empat Dimensi Kompetensi AI (UNESCO)

Kerangka UNESCO menetapkan empat dimensi yang seluruhnya tersentuh buku ini:

| Dimensi | Wujud dalam buku ini |
|---|---|
| ***Human-centred mindset*** | AI sebagai mitra, bukan pengganti — ditegaskan sejak Bab 1 dan diuji tanpa AI pada UTS/UAS |
| ***Ethics of AI*** | Bab 13: etika, batasan, dan AI Usage Log; diukur melalui Sub-CPMK-7.8 (ranah afektif A3) |
| ***AI techniques and applications*** | AI Corner di seluruh 14 bab, dengan kedalaman meningkat |
| ***AI system design*** | Bab 14: integrasi AI di seluruh siklus pengembangan proyek |

### Prinsip Etis Penggunaan AI

Sepanjang progresi AI Literacy, mahasiswa juga akan mempelajari prinsip-prinsip etis:

1. **Transparansi** --- Selalu nyatakan ketika menggunakan bantuan AI dalam tugas.
2. **Verifikasi** --- Jangan pernah menerima output AI tanpa memahami dan memverifikasinya.
3. **Pemahaman** --- Gunakan AI untuk memperdalam pemahaman, bukan menggantikannya.
4. **Integritas Akademik** --- Pahami batas antara bantuan AI yang diperbolehkan dan pelanggaran akademik.
5. **Pengembangan Diri** --- Targetkan kemandirian; AI adalah alat bantu, bukan penopang permanen.

---

*Buku ini diterbitkan pada Februari 2026 oleh Program Studi Informatika, Fakultas Sains dan Teknologi, Universitas Al Azhar Indonesia, Jakarta.*

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
