# Minggu 14: Riset Berbantuan AI dan *Reproducibility*

---

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata kuliah | Metodologi Penelitian (`IF52510021`) |
| Minggu | 14 dari 16 |
| Topik | Pemakaian AI yang bertanggung jawab; penelitian yang dapat diulang |
| Sub-CPMK | `METPEN-Sub-CPMK071-1` |
| ICM | ICM-13 — Menyusun paket reproduksi dan Deklarasi AI yang lengkap |
| Durasi | 2 × 50 menit |
| Metode | Kuliah + lokakarya + uji reproduksi silang |
| Bacaan | [Bab 13 — Riset Berbantuan AI dan *Reproducibility*](../06-buku-ajar/bab-13-riset-berbantuan-ai-dan-reproducibility.md) |

---

## Tujuan Pembelajaran

1. **Menjelaskan** (C2) tingkatan *reproducibility* dan syaratnya.
2. **Menyusun** (C3) paket reproduksi yang dapat diikuti orang lain.
3. **Menilai** (C5) pemakaian AI dalam penelitian dari sisi integritas.
4. **Menyusun** (C3) Deklarasi AI yang lengkap dan jujur.

---

## Materi Pembelajaran

### 14.1 Kedudukan Minggu Ini

Mata kuliah ini berstatus **tahap A→C, mode E (Eksplisit)**, pilar **AI
Research** pada AI Curriculum Infusion Matrix, dengan peran *"AI-assisted
research + research on AI"*. Minggu ini adalah tempat peran itu dibahas
secara utuh.

| Sepanjang semester | Minggu ini |
|--------------------|------------|
| AI Corner tiap minggu membatasi pemakaian per tahap | Pemakaian AI dinilai sebagai persoalan integritas penelitian |
| Deklarasi AI dilampirkan pada tiap tugas | **Deklarasi AI disusun lengkap dan dinilai** |

### 14.2 Tingkatan Dapat-Diulang

| Tingkat | Arti | Yang diperlukan |
|---------|------|-----------------|
| **Dapat diulang** (*repeatable*) | Peneliti yang sama, alat yang sama, hasil sama | Catatan prosedur |
| **Dapat direproduksi** (*reproducible*) | Orang lain, data yang sama, hasil sama | Data + kode + petunjuk |
| **Dapat direplikasi** (*replicable*) | Orang lain, data baru, simpulan sama | Protokol yang lengkap |

Untuk proposal Tugas Akhir, yang dituntut adalah tingkat kedua: **orang lain
dapat memperoleh hasil yang sama dari data yang sama**.

### 14.3 Isi Paket Reproduksi

```
paket-reproduksi/
├── README.md              ← apa ini, bagaimana memakainya
├── data/
│   ├── mentah/            ← data asli (atau contoh bila rahasia)
│   ├── olahan/            ← hasil pembersihan
│   └── KAMUS-DATA.md      ← arti setiap kolom, satuan, nilai kosong
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
├── LINGKUNGAN.md          ← versi bahasa, pustaka, sistem
└── DEKLARASI-AI.md        ← pemakaian AI di setiap tahap
```

| Berkas | Isi minimal |
|--------|-------------|
| `README.md` | Urutan menjalankan; perkiraan waktu; apa yang dihasilkan |
| `KAMUS-DATA.md` | Setiap kolom: nama, tipe, satuan, rentang sah, arti nilai kosong |
| `LINGKUNGAN.md` | Versi persis bahasa dan setiap pustaka |
| `DEKLARASI-AI.md` | Tabel pemakaian AI per tahap + cara verifikasi |

### 14.4 Data yang Tidak Dapat Dibagikan

Banyak penelitian melibatkan data yang tidak boleh disebarkan: keterangan
pribadi, data organisasi, transkrip wawancara.

| Keadaan | Yang tetap dapat dibagikan |
|---------|---------------------------|
| Data pribadi | Data teragregasi; data contoh sintetis dengan struktur sama |
| Data organisasi | Statistik ringkas; kode dan prosedur lengkap |
| Transkrip wawancara | Buku penanda (*codebook*); kutipan yang diizinkan |
| Data berlisensi | Petunjuk cara memperolehnya |

Yang **selalu** dapat dibagikan: kode, instrumen, prosedur, kamus data, dan
Deklarasi AI. Ketidakmampuan membagikan data mentah bukan alasan untuk tidak
menyusun paket reproduksi.

### 14.5 Pemakaian AI dalam Penelitian

| Tahap | Pemakaian yang sah | Yang tidak sah |
|-------|--------------------|----------------|
| Pencarian literatur | Menemukan kandidat, diverifikasi ke DOI | Mengambil sitasi tanpa verifikasi |
| Membaca | Meringkas naskah yang dimiliki, diperiksa ke aslinya | Menggantikan pembacaan |
| Perancangan | Menantang rancangan dengan pertanyaan | Memilih rancangan |
| Instrumen | Memeriksa butir yang bermakna ganda | Menyusun instrumen tanpa kerangka |
| Pengumpulan data | — | **Mengarang data atau kutipan** |
| Analisis | Membantu menulis kode yang dipahami | Menafsirkan hasil |
| Penulisan | Memperbaiki tata bahasa dan kejelasan | Menulis bagian yang tidak dipahami |
| Penyuntingan | Memeriksa konsistensi angka antarbagian | Menambahkan klaim |

Satu baris pada tabel itu tidak memiliki kolom kiri: **pengumpulan data**.
Tidak ada pemakaian AI yang sah untuk menghasilkan data penelitian; data
berasal dari lapangan atau tidak ada.

### 14.6 Tiga Pertanyaan Penguji

| Pertanyaan | Bila jawabannya "tidak" |
|------------|------------------------|
| Apakah Anda dapat menjelaskan setiap bagian naskah ini tanpa membacanya? | Bagian itu belum menjadi milik Anda |
| Apakah setiap sumber yang Anda sitasi sudah Anda buka dan baca? | Sitasi yang belum dibaca dihapus |
| Apakah Deklarasi AI Anda menggambarkan pemakaian yang sebenarnya? | Deklarasi diperbaiki |

Ketiganya diajukan pada pertahanan lisan Minggu 15.

### 14.7 Deklarasi AI yang Baik

```markdown
## Deklarasi Pemakaian AI

| Tahap | Perkakas | Untuk apa | Cara verifikasi |
|-------|----------|-----------|-----------------|
| Pencarian literatur | [nama] | Mencari kandidat dengan kata kunci Bab 3 | 41 kandidat disebut; 27 ditemukan di basis data; 14 tidak ada dan dibuang. Dari 27, 22 dibaca penuh. |
| Pemeriksaan instrumen | [nama] | Menandai butir bermakna ganda | 6 butir ditandai; 4 saya ubah, 2 saya pertahankan dengan alasan di §3.4 |
| Penulisan | [nama] | Memperbaiki tata kalimat §2.1–2.3 | Dibandingkan kalimat per kalimat dengan versi asli; tidak ada klaim baru |
| Kode analisis | [nama] | Membantu menulis fungsi pembersihan data | Saya telusuri baris per baris; saya uji pada 20 baris yang saya periksa manual |
| Penjelasan tandingan | [nama] | Mengajukan penjelasan lain atas pola temuan | 5 diajukan; 2 saya bahas di §5.3 sebagai ancaman validitas |

**Tidak memakai bantuan AI:** perumusan RQ (§1.3), pemilihan rancangan (§3.1),
penetapan ambang evaluasi (§3.6), seluruh data wawancara dan transkripsinya,
penarikan simpulan (§5).

Saya bertanggung jawab penuh atas seluruh isi naskah ini, termasuk bagian
yang disusun dengan bantuan perkakas di atas.

[nama], [NIM], [tanggal]
```

| Ciri deklarasi yang baik | Ciri yang buruk |
|--------------------------|-----------------|
| Menyebut tahap dan bagian naskah secara spesifik | "Saya memakai AI untuk membantu penulisan" |
| Kolom verifikasi berisi angka dan tindakan | Kolom verifikasi berisi "sudah diperiksa" |
| **Melaporkan yang dibuang** (14 sitasi tidak ada) | Hanya melaporkan yang dipakai |
| Menyebut apa yang **tidak** dibantu AI | Tidak menyebut |

Baris ketiga adalah ciri yang paling meyakinkan. Melaporkan bahwa 14 dari 41
kandidat sitasi ternyata tidak ada menunjukkan bahwa verifikasi benar-benar
dijalankan — dan menaikkan kepercayaan terhadap 27 sisanya.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

| # | Kegiatan |
|---|----------|
| 1 | Membaca [Bab 13](../06-buku-ajar/bab-13-riset-berbantuan-ai-dan-reproducibility.md) |
| 2 | Mengumpulkan seluruh berkas penelitian dalam satu folder |
| 3 | Menyusun draf Deklarasi AI dari catatan sepanjang semester |

### Di Kelas (100 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–25 | Kuliah: tingkatan reproduksi; isi paket; data yang tidak dapat dibagikan |
| 25–45 | Kuliah: pemakaian AI per tahap; anatomi Deklarasi AI yang baik |
| 45–55 | **Rehat** |
| 55–85 | **Lokakarya 14** — [Paket Reproduksi dan Deklarasi AI](../04-labs/lab-14-paket-reproduksi-dan-deklarasi-ai.md) |
| 85–100 | **Uji reproduksi silang**: menjalankan paket teman dan melaporkan di mana macet |

> Kegiatan 85–100 adalah ujian yang paling tegas. Paket yang terlihat lengkap
> bagi penyusunnya hampir selalu macet di tangan orang lain — biasanya pada
> hal yang dianggap "sudah jelas".

### Setelah Kelas

| # | Kegiatan |
|---|----------|
| 1 | Menyelesaikan **T13 — Paket reproduksi + Deklarasi AI** (5%) |
| 2 | Menyelesaikan **T14 — Proposal lengkap** untuk seminar Minggu 15 |
| 3 | Menyiapkan presentasi 12 menit |

---

## Penugasan

### T13 — Paket Reproduksi dan Deklarasi AI (5%, Unjuk Kerja) ★

| Aspek | Ketentuan |
|-------|-----------|
| Keluaran | Satu folder/arsip + dokumen penjelas |
| Isi | Daftar berkas · data/contoh data · kode atau prosedur · petunjuk langkah demi langkah · lingkungan dan versi · **Deklarasi AI lengkap** |
| Uji | Teman sekelas dapat mengikuti petunjuknya sampai selesai |
| Tenggat | Akhir Minggu 14 |

---

## AI Corner — Minggu 14

Seluruh modul ini membahas AI. Bagian ini menambahkan satu hal: **batas
pemakaian AI untuk menyusun Deklarasi AI itu sendiri**.

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI memeriksa kelengkapan format deklarasi | Meminta AI menyusun isi deklarasi |
| Meminta AI memeriksa apakah kolom verifikasi sudah spesifik | Meminta AI mengisi kolom verifikasi |
| Meminta AI memeriksa kelengkapan paket reproduksi | Meminta AI membuat petunjuk yang tidak Anda uji |

Deklarasi yang isinya disusun AI adalah pernyataan tentang pemakaian AI yang
disusun oleh AI — dan ketidakjujurannya berlapis.

### Catatan tentang "Penelitian tentang AI"

Peran mata kuliah ini disebut *"AI-assisted research + research on AI"*.
Bagian kedua berlaku bagi mahasiswa yang **penelitiannya sendiri meneliti
sistem AI**. Bagi mereka, ancaman validitas tambahan berlaku:

| Ancaman khas penelitian tentang AI | Penanganan |
|-----------------------------------|------------|
| Data uji tercemar data latih | Pisahkan tegas; laporkan cara pemisahan |
| Hasil bergantung pada benih acak | Jalankan beberapa kali; laporkan sebarannya |
| Pembanding tidak disetel sebaik metode yang diusulkan | Setel keduanya dengan usaha yang sebanding; laporkan caranya |
| Versi model berubah | Catat versi dan tanggal persis |
| Keluaran tidak deterministik | Laporkan parameter; ulangi pengukuran |

Baris terakhir sering menjadi persoalan yang tidak diperkirakan. Sistem yang
keluarannya berbeda pada pemanggilan yang sama menuntut pelaporan yang
berbeda dari sistem deterministik — dan menyatakannya adalah bagian dari
*reproducibility*.

---

## Referensi

1. Munafò, M. R., et al. (2017). A Manifesto for Reproducible Science. *Nature Human Behaviour*, 1(1), 0021.
2. Peng, R. D. (2011). Reproducible Research in Computational Science. *Science*, 334(6060), 1226–1227.
3. ACM. (2020). *Artifact Review and Badging Version 2.0*. Association for Computing Machinery.
4. Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for Scientific Data Management and Stewardship. *Scientific Data*, 3, 160018.
5. COPE. (2023). *Authorship and AI Tools: COPE Position Statement*. Committee on Publication Ethics.
6. Gundersen, O. E., & Kjensmo, S. (2018). State of the Art: Reproducibility in Artificial Intelligence. *Proceedings of AAAI-18*.
7. Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the Dangers of Stochastic Parrots. *Proceedings of FAccT '21*, 610–623.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Bab buku ajar | [Bab 13](../06-buku-ajar/bab-13-riset-berbantuan-ai-dan-reproducibility.md) |
| Lokakarya | [Lokakarya 14](../04-labs/lab-14-paket-reproduksi-dan-deklarasi-ai.md) |
| Mata kuliah terkait | [Dasar AI dan Pembelajaran Mesin](../../dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/README.md) |
| Minggu sebelumnya | [Minggu 13](week-13-design-science-dan-evaluasi-artefak.md) |
| Minggu berikutnya | [Minggu 15 — Seminar Proposal](week-15-seminar-proposal.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
