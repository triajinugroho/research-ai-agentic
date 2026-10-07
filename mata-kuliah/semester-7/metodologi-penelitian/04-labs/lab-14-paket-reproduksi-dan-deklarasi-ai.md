# Lokakarya 14: Paket Reproduksi dan Deklarasi AI

---

## Informasi Lokakarya

| Aspek | Keterangan |
|-------|------------|
| Mata kuliah | Metodologi Penelitian (`IF52510021`) |
| Lokakarya | 14 — menyertai [Minggu 14](../03-modules/week-14-riset-berbantuan-ai-dan-reproducibility.md) |
| Sub-CPMK | `METPEN-Sub-CPMK071-1` |
| Durasi | 30 menit + uji reproduksi silang 15 menit |
| Keluaran | **T13** (5%, Unjuk Kerja) |

---

## Tujuan Lokakarya

Menyusun paket yang memungkinkan orang lain mengulang penelitian Anda, dan
Deklarasi AI yang jujur dan dapat diperiksa.

---

## Persiapan

| # | Yang disiapkan |
|---|----------------|
| 1 | Seluruh berkas penelitian terkumpul dalam satu folder |
| 2 | Catatan pemakaian AI sepanjang semester |
| 3 | Instrumen, protokol, rencana analisis (T9–T11) |

---

## Langkah-Langkah

### Langkah 1 — Menyusun Struktur Folder (8 menit)

```
paket-reproduksi/
├── README.md
├── data/
│   ├── mentah/
│   ├── olahan/
│   └── KAMUS-DATA.md
├── kode/
│   ├── 01-pembersihan.*
│   ├── 02-analisis.*
│   └── 03-gambar.*
├── instrumen/
│   ├── kuesioner.pdf
│   ├── panduan-wawancara.md
│   └── lembar-persetujuan.pdf
├── hasil/
│   ├── tabel/
│   └── gambar/
├── LINGKUNGAN.md
└── DEKLARASI-AI.md
```

Bila data belum terkumpul (keadaan lazim pada tahap proposal), isi
`data/mentah/` dengan **data contoh bertruktur sama**, diberi tanda jelas.

### Langkah 2 — Menulis README (7 menit)

```markdown
# Paket Reproduksi — [judul penelitian]

## Apa ini
[Satu paragraf]

## Yang diperlukan
- [bahasa/perangkat] versi ___
- Pustaka: lihat LINGKUNGAN.md
- Perkiraan waktu menjalankan: ___ menit

## Cara menjalankan
1. [langkah persis, termasuk perintah yang diketik]
2.
3.

## Yang dihasilkan
| Berkas keluaran | Isi | Muncul di naskah |
|-----------------|-----|------------------|
| hasil/tabel/t1.csv | | Tabel 4.1 |
| hasil/gambar/g1.png | | Gambar 4.2 |

## Catatan tentang data
[Apa yang dapat dibagikan, apa yang tidak, dan mengapa]

## Kontak
[nama, surel institusi]
```

| Ujian README | Bila gagal |
|--------------|------------|
| Langkah menjalankan berisi perintah persis | "Jalankan skripnya" tidak cukup |
| Tabel keluaran menghubungkan berkas ke naskah | Pembaca tidak tahu mana yang mana |
| Catatan data menjelaskan pembatasan | Data yang hilang tanpa penjelasan mencurigakan |

### Langkah 3 — Menyusun Kamus Data (5 menit)

| Kolom | Tipe | Satuan | Rentang sah | Arti nilai kosong | Asal |
|-------|------|--------|-------------|-------------------|------|
| | | | | | butir __ kuesioner |
| | | | | | dihitung dari __ |

Kolom "arti nilai kosong" sering diabaikan dan menentukan hasil analisis.
Nilai kosong yang berarti "tidak menjawab" berbeda dari yang berarti "tidak
berlaku" — dan penanganannya berbeda.

### Langkah 4 — Menyusun Deklarasi AI (10 menit)

```markdown
## Deklarasi Pemakaian AI

| Tahap | Perkakas | Untuk apa | Cara verifikasi |
|-------|----------|-----------|-----------------|
| | | | |
| | | | |

**Tidak memakai bantuan AI:** [sebutkan bagian secara spesifik]

Saya bertanggung jawab penuh atas seluruh isi naskah ini.

[nama], [NIM], [tanggal]
```

Telusuri semester Anda tahap demi tahap:

| Tahap | Pernahkah memakai AI? | Untuk apa | Bagaimana diperiksa |
|-------|----------------------|-----------|---------------------|
| Pemilihan topik (Mg 1) | | | |
| Kesenjangan (Mg 2) | | | |
| Penelusuran (Mg 3) | | | |
| Sintesis (Mg 4) | | | |
| RQ (Mg 5) | | | |
| *Stakeholder* (Mg 6) | | | |
| Kerangka (Mg 7) | | | |
| Rancangan (Mg 9) | | | |
| Instrumen (Mg 10) | | | |
| Validitas (Mg 11) | | | |
| Analisis (Mg 12) | | | |
| Kriteria (Mg 13) | | | |
| Penulisan proposal | | | |

| Ciri kolom verifikasi yang baik | Ciri yang buruk |
|--------------------------------|-----------------|
| "41 kandidat disebut; 27 ditemukan; 14 tidak ada dan dibuang" | "Sudah diperiksa" |
| "Dibandingkan kalimat per kalimat dengan versi asli" | "Sudah dibaca ulang" |
| "6 butir ditandai; 4 saya ubah, 2 saya pertahankan (alasan §3.4)" | "Saran diterima sebagian" |

> **Melaporkan yang dibuang adalah ciri paling meyakinkan.** Menyatakan bahwa
> 14 dari 41 kandidat sitasi ternyata tidak ada menunjukkan verifikasi
> benar-benar dijalankan — dan menaikkan kepercayaan terhadap 27 sisanya.

---

## Uji Reproduksi Silang (15 menit)

Bertukar paket dengan teman. Jalankan paketnya **tanpa bertanya apa pun**.

```markdown
## Laporan Uji Reproduksi
Penyusun : [nama]     Penguji : [nama]

| Langkah | Berhasil? | Di mana macet | Apa yang saya tebak |
|---------|-----------|---------------|---------------------|
| 1 | | | |
| 2 | | | |

Berapa kali saya harus menebak: ___
Berapa kali saya ingin bertanya: ___

Yang paling membantu dalam paket ini:
Yang paling perlu diperbaiki:
```

Setiap tebakan adalah bagian paket yang belum lengkap. Paket yang terlihat
lengkap bagi penyusunnya hampir selalu macet di tangan orang lain — biasanya
pada hal yang dianggap "sudah jelas".

---

## Tantangan Tambahan

| # | Tantangan |
|---|-----------|
| 1 | Jalankan paket Anda sendiri **di komputer lain** atau dengan folder baru. Catat setiap kali gagal karena jalur berkas atau pustaka yang tidak tercatat. |
| 2 | Buat data sintetis yang menyerupai data nyata Anda (ukuran, sebaran, pola nilai kosong). Bagikan itu alih-alih data asli, dan jelaskan cara membuatnya. |
| 3 | Untuk penelitian tentang sistem AI: catat versi persis model, tanggal pemanggilan, seluruh parameter, dan jalankan pengukuran ≥3 kali. Laporkan sebaran hasilnya. |

Tantangan 3 berlaku khusus bagi mahasiswa yang penelitiannya meneliti sistem
AI — bagian *"research on AI"* dari peran mata kuliah ini. Sistem yang
keluarannya tidak deterministik menuntut pelaporan yang berbeda.

---

## Daftar Periksa Penyelesaian

| # | Butir | ☐ |
|---|-------|---|
| 1 | Struktur folder tersusun lengkap | ☐ |
| 2 | README memuat langkah menjalankan yang persis | ☐ |
| 3 | Tabel keluaran menghubungkan berkas ke naskah | ☐ |
| 4 | Kamus data lengkap, termasuk arti nilai kosong | ☐ |
| 5 | LINGKUNGAN.md mencatat versi persis | ☐ |
| 6 | Data yang tidak dapat dibagikan dijelaskan, dengan data contoh | ☐ |
| 7 | **Deklarasi AI menelusuri seluruh tahap semester** | ☐ |
| 8 | Kolom verifikasi berisi angka dan tindakan | ☐ |
| 9 | Bagian yang tidak dibantu AI disebutkan | ☐ |
| 10 | Uji reproduksi silang dijalankan; temuan ditanggapi | ☐ |
| 11 | Paket dijalankan ulang di lingkungan bersih | ☐ |

---

## AI Corner — Lokakarya 14

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI memeriksa kelengkapan format deklarasi | **Menyusun isi deklarasi** |
| Meminta AI memeriksa apakah kolom verifikasi cukup spesifik | Mengisi kolom verifikasi |
| Meminta AI memeriksa kelengkapan README | Membuat petunjuk yang tidak Anda uji |

Deklarasi yang isinya disusun AI adalah pernyataan tentang pemakaian AI yang
disusun oleh AI. Ketidakjujurannya berlapis.

### Tiga Pertanyaan yang Akan Diajukan Minggu 15

| Pertanyaan | Bila jawabannya "tidak" |
|------------|------------------------|
| Dapatkah Anda menjelaskan setiap bagian naskah ini tanpa membacanya? | Bagian itu belum menjadi milik Anda |
| Sudahkah setiap sumber yang disitasi Anda buka dan baca? | Sitasi yang belum dibaca dihapus |
| Apakah Deklarasi AI menggambarkan pemakaian yang sebenarnya? | Perbaiki deklarasinya |

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul | [Minggu 14](../03-modules/week-14-riset-berbantuan-ai-dan-reproducibility.md) |
| Bab buku ajar | [Bab 13](../06-buku-ajar/bab-13-riset-berbantuan-ai-dan-reproducibility.md) |
| Seminar | [Minggu 15 — Seminar Proposal](../03-modules/week-15-seminar-proposal.md) |
| Lokakarya sebelumnya | [Lokakarya 13](lab-13-kriteria-evaluasi-artefak.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
