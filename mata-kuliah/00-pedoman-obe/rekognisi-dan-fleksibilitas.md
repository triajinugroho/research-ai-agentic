---
id: uai-inf-rekognisi-fleksibilitas
tipe: pedoman
judul: Rekognisi Pembelajaran Lampau, Micro-credential, dan Fleksibilitas Moda
prodi: Informatika
universitas: Universitas Al Azhar Indonesia
versi: 1.0
status: draft
diperbarui: 2026-09-05
berlaku_untuk: [INF-101, INF-102, TBD-STAT, IF2205, IF2206, IF3XXX]
---

# Rekognisi & Fleksibilitas Pembelajaran

> **Dasar regulasi.** Permendiktisaintek No. 39 Tahun 2025 menjadikan **Rekognisi Pembelajaran Lampau (RPL) wajib**, mengakomodasi program *micro-credential*, dan membuka jalur lintas program studi, kampus, serta negara. Permendiktisaintek No. 10 Tahun 2026 **Pasal 14 ayat (1)** menegaskan: *"Pelaksanaan proses pembelajaran diselenggarakan dengan menciptakan suasana belajar yang menyenangkan, inklusif, kolaboratif, kreatif, dan efektif."*
>
> **Prinsip desain:** beban administrasi ditaruh di **tingkat program studi (berkas ini)**, bukan di setiap RPS. RPS hanya bertambah satu baris `Moda Pembelajaran` pada §A, dan satu tabel kecil "Unit Rekognisi" pada `mutu/01`.

## A. Rekognisi Pembelajaran Lampau (RPL)

### A.1 Jenis bukti yang dapat diakui

| Jenis bukti | Contoh | Mekanisme asesmen |
|---|---|---|
| **Sertifikat kompetensi** | Sertifikasi industri, *bootcamp* terverifikasi, kursus daring bersertifikat | Verifikasi keaslian + uji petik terhadap Sub-CPMK terkait |
| **Portofolio karya** | Repositori kode publik, aplikasi yang dipublikasikan, kontribusi *open source* | Telaah portofolio + wawancara teknis terhadap CPMK |
| **Pengalaman kerja** | Pengalaman profesional relevan yang terdokumentasi | Surat keterangan + asesmen unjuk kerja |
| **Pembelajaran mandiri** | Proyek pribadi yang terdokumentasi | Demonstrasi + uji lisan |

### A.2 Prinsip pengakuan

1. Rekognisi diberikan terhadap **Sub-CPMK atau CPMK tertentu**, bukan terhadap mata kuliah secara utuh — inilah yang membuat rekognisi dapat diaudit.
2. Bukti harus **memenuhi ambang ketercapaian yang sama** dengan mahasiswa jalur reguler. Rekognisi mengubah *cara* pembuktian, bukan *standar* capaian.
3. Setiap rekognisi dicatat pada `mutu/02-pengukuran-ketercapaian-cpl.md` mata kuliah terkait, dengan sumber bukti yang dapat ditelusuri.
4. 🔲 **[MENUNGGU PENETAPAN PRODI]** — batas maksimum SKS yang dapat direkognisi dan pejabat yang berwenang mengesahkan.

## B. Unit Micro-credential

Unit rekognisi **tidak perlu dikarang** — struktur fase pembelajaran yang sudah ada di paket mata kuliah ini adalah basis alaminya.

### B.1 INF-101 Algoritma dan Pemrograman

| Unit | Cakupan | Minggu | CPMK |
|---|---|---|---|
| **U1 — Fondasi Berpikir Komputasional** | Algoritma, *computational thinking*, variabel, tipe data, struktur kontrol | 1–4 | CPMK-1, CPMK-2, CPMK-3 |
| **U2 — Modularitas dan Pengolahan Data** | Fungsi, *string processing*, list, tuple | 5–7 | CPMK-4, CPMK-5 |
| **U3 — Struktur Data dan Algoritma Klasik** | Dictionary, set, *searching*, *sorting*, rekursi | 9–12 | CPMK-5, CPMK-6 |
| **U4 — Efisiensi dan Pemrograman Berbantuan AI** | Big-O, optimasi, *AI-augmented programming*, proyek | 13–15 | CPMK-7 |

Unit untuk lima mata kuliah lain disusun pada Fase 2 mengikuti pola yang sama.

### B.2 Syarat penerbitan

Sebuah unit dinyatakan tercapai bila seluruh Sub-CPMK di dalamnya memenuhi ambang ketercapaian, dibuktikan melalui asesmen yang terdaftar pada matriks CPMK × asesmen.

## C. Fleksibilitas Moda Pembelajaran

Setiap RPS menyatakan moda pada §A Identitas:

| Nilai | Makna |
|---|---|
| `tatap-muka` | Seluruh sesi luring |
| `daring` | Seluruh sesi dalam jaringan |
| `kombinasi` | *Blended* — sebagian luring, sebagian daring/asinkron |

### C.1 Penjagaan integritas asesmen daring

Kebijakan AI pada setiap RPS tetap berlaku penuh pada moda daring. Untuk asesmen sumatif daring (UTS/UAS) berlaku tambahan: identitas terverifikasi, pengawasan yang proporsional, dan variasi butir soal antarmahasiswa. Prinsipnya: **moda boleh berubah, standar pembuktian tidak.**

## D. Klausul Inklusivitas dan Non-diskriminasi

Sesuai Pasal 14 Permendiktisaintek No. 10 Tahun 2026, penyelenggaraan seluruh mata kuliah dalam paket ini **tidak membedakan** mahasiswa berdasarkan latar belakang pendidikan, sosial, ekonomi, budaya, maupun bahasa.

Wujud operasionalnya dalam paket ini:

| Aspek | Wujud konkret |
|---|---|
| **Ekonomi** | Seluruh perangkat wajib berbiaya nol: Google Colab, GitHub Codespaces, referensi utama yang tersedia bebas |
| **Latar belakang pendidikan** | Tidak ada prasyarat pemrograman; materi dimulai dari nol |
| **Bahasa** | Pengantar Bahasa Indonesia; istilah teknis disertai padanan Inggris |
| **Aksesibilitas** | Materi tersedia sebagai teks Markdown yang terbaca oleh pembaca layar; kode disertai penjelasan naratif |
| **Suasana belajar** | Metode kolaboratif dan kreatif (*pair programming*, *think-pair-share*, *peer review*) tercantum eksplisit pada kolom Metode/Strategi setiap RPS |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
