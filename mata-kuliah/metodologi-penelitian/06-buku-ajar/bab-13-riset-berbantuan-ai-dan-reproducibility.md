# BAB 13: RISET BERBANTUAN AI DAN *REPRODUCIBILITY*

**Bahan rujukan penyelarasan kurikulum** — disusun Tri Aji Nugroho, S.T., M.T.
Pengampu mata kuliah menurut registri: **Andi Arniaty Arsyad, Ph.D.** (`AAA`).

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `METPEN-Sub-CPMK071-1` | Menerapkan (C3) prinsip *reproducibility* dan menganalisis (C4) integritas pemakaian AI dalam penelitian | C3–C4 |

Setelah membaca bab ini, pembaca diharapkan mampu:

1. **Menjelaskan** (C2) tingkatan *reproducibility* dan syaratnya.
2. **Menyusun** (C3) paket reproduksi yang dapat diikuti orang lain.
3. **Menganalisis** (C4) pemakaian AI per tahap dari sisi integritas.
4. **Menyusun** (C3) Deklarasi AI yang lengkap dan dapat diperiksa.
5. **Mengenali** (C4) ancaman khas penelitian yang meneliti sistem AI.

---

## 13.1 Kedudukan Bab Ini

Mata kuliah ini berstatus **tahap A→C, mode E (Eksplisit)**, pilar **AI
Research**, dengan peran *"AI-assisted research + research on AI"* pada AI
Curriculum Infusion Matrix.

| Peran | Berlaku bagi |
|-------|--------------|
| **AI sebagai alat kerja peneliti** | Seluruh mahasiswa |
| **AI sebagai objek penelitian** | Mahasiswa yang penelitiannya meneliti sistem AI |

Sepanjang buku ini, AI Corner membatasi pemakaian AI per tahap. Bab ini
membahas keduanya secara utuh, bersama dengan syarat yang menyatukan
keduanya: **penelitian yang dapat diulang**.

---

## 13.2 Tingkatan Dapat-Diulang

### 13.2.1 Tiga Tingkat

| Tingkat | Arti | Yang diperlukan |
|---------|------|-----------------|
| **Dapat diulang** (*repeatable*) | Peneliti yang sama, alat yang sama, hasil sama | Catatan prosedur |
| **Dapat direproduksi** (*reproducible*) | Orang lain, data yang sama, hasil sama | Data + kode + petunjuk |
| **Dapat direplikasi** (*replicable*) | Orang lain, data baru, simpulan sama | Protokol yang lengkap |

Untuk proposal Tugas Akhir, yang dituntut adalah **tingkat kedua**: orang
lain dapat memperoleh hasil yang sama dari data yang sama.

### 13.2.2 Mengapa Ini Bukan Formalitas

| Alasan | Penjelasan |
|--------|------------|
| Peneliti sendiri enam bulan kemudian | Orang yang paling sering memerlukan paket reproduksi adalah penulisnya |
| Pembimbing dan penguji | Dapat memeriksa klaim tanpa meminta penjelasan |
| Angkatan berikutnya | Dapat melanjutkan tanpa mengulang dari nol |
| Kepercayaan | Klaim yang dapat diperiksa lebih dipercaya |

Baris pertama sering mengejutkan. Kode yang ditulis tanpa catatan akan sulit
dipahami penulisnya sendiri setelah beberapa bulan.

---

## 13.3 Paket Reproduksi

### 13.3.1 Isinya

```
paket-reproduksi/
├── README.md              ← apa ini, bagaimana memakainya
├── data/
│   ├── mentah/            ← data asli (atau contoh bila rahasia)
│   ├── olahan/            ← hasil pembersihan
│   └── KAMUS-DATA.md      ← arti tiap kolom, satuan, nilai kosong
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

### 13.3.2 README

| Bagian | Isi minimal |
|--------|-------------|
| Apa ini | Satu paragraf |
| Yang diperlukan | Versi bahasa, pustaka, perkiraan waktu |
| Cara menjalankan | **Perintah persis yang diketik**, bukan "jalankan skripnya" |
| Yang dihasilkan | Tabel: berkas keluaran → isinya → muncul di naskah sebagai apa |
| Catatan tentang data | Apa yang dapat dibagikan, apa yang tidak, dan mengapa |

Tabel "yang dihasilkan" sering dilewati dan sangat berguna: ia menghubungkan
setiap angka dalam naskah dengan berkas yang menghasilkannya.

### 13.3.3 Kamus Data

| Kolom | Isi |
|-------|-----|
| Nama kolom | Sesuai berkas |
| Tipe | Angka, teks, tanggal, kategori |
| Satuan | Menit, rupiah, jumlah |
| Rentang sah | Nilai minimum dan maksimum yang mungkin |
| **Arti nilai kosong** | Tidak menjawab / tidak berlaku / tidak tercatat |
| Asal | Butir instrumen mana, atau dihitung dari apa |

Kolom "arti nilai kosong" menentukan hasil analisis dan sering diabaikan.
Nilai kosong yang berarti "tidak menjawab" ditangani berbeda dari yang
berarti "tidak berlaku bagi responden ini".

### 13.3.4 Data yang Tidak Dapat Dibagikan

| Keadaan | Yang tetap dapat dibagikan |
|---------|---------------------------|
| Data pribadi | Data teragregasi; data sintetis dengan struktur sama |
| Data organisasi | Statistik ringkas; kode dan prosedur lengkap |
| Transkrip wawancara | Buku penanda; kutipan yang diizinkan |
| Data berlisensi | Petunjuk cara memperolehnya |

Yang **selalu** dapat dibagikan: kode, instrumen, prosedur, kamus data, dan
Deklarasi AI. Ketidakmampuan membagikan data mentah bukan alasan untuk tidak
menyusun paket reproduksi.

---

## 13.4 Pemakaian AI dalam Penelitian

### 13.4.1 Per Tahap

| Tahap | Pemakaian yang sah | Yang tidak sah |
|-------|--------------------|----------------|
| Pencarian literatur | Menemukan kandidat, diverifikasi ke DOI | Mengambil sitasi tanpa verifikasi |
| Membaca | Meringkas naskah yang dimiliki, diperiksa ke aslinya | Menggantikan pembacaan |
| Perancangan | Menantang rancangan dengan pertanyaan | Memilih rancangan |
| Instrumen | Memeriksa butir bermakna ganda | Menyusun instrumen tanpa kerangka |
| **Pengumpulan data** | **— (tidak ada)** | **Mengarang data atau kutipan** |
| Analisis | Membantu menulis kode yang dipahami | Menafsirkan hasil |
| Penulisan | Memperbaiki tata bahasa dan kejelasan | Menulis bagian yang tidak dipahami |
| Penyuntingan | Memeriksa konsistensi angka antarbagian | Menambahkan klaim |

Satu baris tidak memiliki kolom tengah: **pengumpulan data**. Tidak ada
pemakaian AI yang sah untuk menghasilkan data penelitian. Data berasal dari
lapangan, dari sistem, atau dari arsip — atau tidak ada.

### 13.4.2 Prinsip yang Menyatukan

> **AI boleh dipakai untuk mempercepat, tidak boleh dipakai untuk
> menggantikan pemahaman.**

| Ujian | Penjelasan |
|-------|------------|
| Apakah bahannya berasal dari saya? | Bila tidak, keluarannya tidak dapat dipakai |
| Apakah keluarannya saya periksa? | Bila tidak, ia belum menjadi milik saya |
| Dapatkah saya menjelaskannya tanpa membacanya? | Bila tidak, saya belum memahaminya |
| Apakah pemakaiannya tercatat? | Bila tidak, *disclosure* belum terpenuhi |

### 13.4.3 Tiga Pertanyaan Penguji

| Pertanyaan | Bila jawabannya "tidak" |
|------------|------------------------|
| Dapatkah Anda menjelaskan setiap bagian naskah ini tanpa membacanya? | Bagian itu belum menjadi milik Anda |
| Sudahkah setiap sumber yang Anda sitasi Anda buka dan baca? | Sitasi yang belum dibaca dihapus |
| Apakah Deklarasi AI menggambarkan pemakaian yang sebenarnya? | Deklarasi diperbaiki |

Ketiganya diajukan pada pertahanan lisan Minggu 15.

---

## 13.5 Deklarasi AI

### 13.5.1 Bentuknya

```markdown
## Deklarasi Pemakaian AI

| Tahap | Perkakas | Untuk apa | Cara verifikasi |
|-------|----------|-----------|-----------------|
| Pencarian literatur | [nama] | Mencari kandidat dengan kata kunci Bab 3 | 41 kandidat disebut; 27 ditemukan di basis data; **14 tidak ada dan dibuang**. Dari 27, 22 dibaca penuh. |
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

### 13.5.2 Kolom yang Paling Diperhatikan

| Ciri baik | Ciri buruk |
|-----------|------------|
| Menyebut tahap dan bagian naskah secara spesifik | "Saya memakai AI untuk membantu penulisan" |
| Kolom verifikasi berisi **angka dan tindakan** | "Sudah diperiksa" |
| **Melaporkan yang dibuang** (14 sitasi tidak ada) | Hanya melaporkan yang dipakai |
| Menyebut apa yang **tidak** dibantu AI | Tidak menyebut |

Baris ketiga adalah ciri yang paling meyakinkan. Melaporkan bahwa 14 dari 41
kandidat sitasi ternyata tidak ada menunjukkan bahwa verifikasi benar-benar
dijalankan — dan menaikkan kepercayaan terhadap 27 sisanya.

### 13.5.3 Yang Dinilai

| Yang dinilai | Bukan |
|--------------|-------|
| Apakah pemakaian berada dalam batas tiap bab | Seberapa sedikit AI dipakai |
| Apakah keluaran diperiksa, dan bagaimana | Apakah keluaran dipakai |
| Apakah ada pemakaian yang dilarang | Apakah tim "mandiri" |
| Apakah deklarasi jujur dan lengkap | Apakah deklarasi pendek |

Mata kuliah ini **tidak** memberi nilai lebih kepada mahasiswa yang tidak
memakai AI sama sekali. Yang dinilai adalah pemakaian yang beralasan,
berbatas, dan diperiksa — sesuai status mode E.

---

## 13.6 Meneliti Sistem AI

Bagian ini berlaku bagi mahasiswa yang **penelitiannya sendiri meneliti
sistem AI** — bagian *"research on AI"* dari peran mata kuliah ini.

### 13.6.1 Ancaman Khas

| Ancaman | Penanganan |
|---------|------------|
| **Data uji tercemar data latih** | Pisahkan tegas; laporkan cara pemisahan dan kapan dilakukan |
| Hasil bergantung pada benih acak | Jalankan beberapa kali; laporkan sebaran, bukan satu angka |
| Pembanding tidak disetel sebaik metode yang diusulkan | Setel keduanya dengan usaha sebanding; laporkan caranya |
| Versi model berubah | Catat versi dan tanggal persis |
| Keluaran tidak deterministik | Laporkan parameter; ulangi pengukuran |
| Data latih mengandung bias | Periksa sebaran; laporkan bagi siapa sistem bekerja lebih buruk |
| Metrik tidak sesuai tugas | Pilih metrik yang mencerminkan akibat kesalahan nyata |

### 13.6.2 Pencemaran Data

Ancaman nomor satu dan paling sering terjadi tanpa disadari.

| Bentuk | Contoh |
|--------|--------|
| Pemisahan dilakukan setelah praproses | Normalisasi dihitung dari seluruh data, termasuk data uji |
| Penyetelan memakai data uji | Parameter dipilih berdasarkan kinerja pada data uji |
| Duplikat lintas himpunan | Baris yang sama muncul di data latih dan uji |
| Kebocoran temporal | Data masa depan dipakai memprediksi masa lalu |
| Data uji dipakai berkali-kali | Setiap kali memeriksa, sedikit informasi bocor |

Baris terakhir halus: memeriksa kinerja pada data uji berkali-kali selama
pengembangan membuat data uji itu secara bertahap menjadi data validasi.

### 13.6.3 Keluaran yang Tidak Deterministik

Sistem yang keluarannya berbeda pada masukan yang sama menuntut pelaporan
yang berbeda.

| Yang wajib dilaporkan | Contoh |
|-----------------------|--------|
| Versi model dan tanggal | "Model [nama] versi [x], diakses 12–18 November 2026" |
| Seluruh parameter | Suhu, panjang maksimum, dan lainnya |
| Jumlah pengulangan | "Setiap pengukuran diulang 5 kali" |
| **Sebaran hasil** | "Rerata 87,2%; rentang 84,1–89,6%" |
| Cara menangani variasi | "Nilai yang dilaporkan adalah rerata dari 5 kali" |

Melaporkan satu angka dari satu kali pengukuran pada sistem yang tidak
deterministik adalah pelaporan yang menyesatkan, meskipun angkanya benar.

---

## AI Corner — Bab 13

### Bab Ini Adalah AI Corner-nya

Seluruh bab membahas AI. Bagian ini menambahkan satu hal: **batas pemakaian
AI untuk menyusun Deklarasi AI itu sendiri**.

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI memeriksa kelengkapan format deklarasi | **Menyusun isi deklarasi** |
| Meminta AI memeriksa apakah kolom verifikasi cukup spesifik | Mengisi kolom verifikasi |
| Meminta AI memeriksa kelengkapan README paket reproduksi | Membuat petunjuk yang tidak Anda uji |

Deklarasi yang isinya disusun AI adalah pernyataan tentang pemakaian AI yang
disusun oleh AI. Ketidakjujurannya berlapis.

### Pemakaian yang Dianjurkan

```
Berikut Deklarasi AI yang saya susun:
[tempelkan]

Tugas Anda:
1. Tandai baris yang kolom verifikasinya tidak berisi angka
   atau tindakan yang konkret.
2. Tandai tahap penelitian yang tidak saya sebutkan sama
   sekali (lihat daftar tahap di Bab 13).
3. Periksa apakah saya menyebutkan bagian yang TIDAK dibantu AI.

Jangan menulis atau melengkapi isi deklarasi saya.
```

---

## Latihan Soal

### Tingkat Dasar

1. Sebutkan tiga tingkatan dapat-diulang dan apa yang diperlukan masing-masing.
2. Sebutkan isi minimal README paket reproduksi.
3. Mengapa kolom "arti nilai kosong" dalam kamus data penting?
4. Tahap penelitian mana yang tidak memiliki pemakaian AI yang sah? Mengapa?
5. Sebutkan empat ciri Deklarasi AI yang baik dan empat yang buruk.

### Tingkat Menengah

6. Untuk penelitian Anda, tentukan data apa yang dapat dan tidak dapat dibagikan, beserta alasannya. Untuk yang tidak dapat dibagikan, tentukan apa yang tetap Anda sertakan.

7. Susun kamus data untuk salah satu berkas data Anda, dengan seluruh kolom §13.3.3 terisi.

8. Susun Deklarasi AI yang menelusuri seluruh tahap penelitian Anda sejak Minggu 1, dengan kolom verifikasi berisi angka dan tindakan.

9. Untuk penelitian yang meneliti sistem AI: periksa rancangan Anda terhadap tujuh ancaman §13.6.1. Untuk setiap ancaman yang berlaku, tuliskan penanganannya.

### Tingkat Mahir

10. **Uji reproduksi silang.** Tukarkan paket reproduksi dengan teman. Jalankan paketnya tanpa bertanya apa pun. Catat setiap kali Anda harus menebak dan setiap langkah yang macet. Laporkan hasilnya kepada penyusunnya, lalu perbaiki paket Anda sendiri berdasarkan laporan yang Anda terima.

11. Jalankan paket Anda sendiri di lingkungan yang bersih — komputer lain, atau folder baru dengan pustaka yang dipasang ulang. Catat setiap kegagalan yang disebabkan jalur berkas, versi pustaka, atau pengaturan yang tidak tercatat. Perbaiki LINGKUNGAN.md.

12. Untuk penelitian yang memakai sistem AI dalam analisisnya: jalankan pengukuran yang sama sebanyak 5 kali dengan parameter yang sama. Laporkan sebaran hasilnya. Jelaskan apa yang akan berubah dalam pelaporan Anda bila Anda hanya menjalankannya sekali, dan mengapa itu menyesatkan.

---

## Rangkuman

| Gagasan pokok | Rumusan singkat |
|---------------|-----------------|
| Tingkat yang dituntut | *Reproducible* — orang lain memperoleh hasil sama dari data sama |
| Yang paling sering memerlukan paket | Penulisnya sendiri, enam bulan kemudian |
| README | Perintah persis, bukan "jalankan skripnya" |
| Kamus data | Arti nilai kosong menentukan hasil analisis |
| Data rahasia | Bukan alasan tidak menyusun paket reproduksi |
| Tahap tanpa pemakaian AI yang sah | Pengumpulan data |
| Prinsip yang menyatukan | Mempercepat boleh; menggantikan pemahaman tidak |
| Ciri deklarasi terkuat | Melaporkan yang dibuang |
| Yang dinilai dari deklarasi | Batas dan pemeriksaannya, bukan sedikitnya pemakaian |
| Ancaman utama meneliti AI | Pencemaran data uji oleh data latih |
| Keluaran tak deterministik | Laporkan sebaran, bukan satu angka |

---

## Referensi

1. Munafò, M. R., et al. (2017). A Manifesto for Reproducible Science. *Nature Human Behaviour*, 1(1), 0021.
2. Peng, R. D. (2011). Reproducible Research in Computational Science. *Science*, 334(6060), 1226–1227.
3. ACM. (2020). *Artifact Review and Badging Version 2.0*. Association for Computing Machinery.
4. Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for Scientific Data Management and Stewardship. *Scientific Data*, 3, 160018.
5. Gundersen, O. E., & Kjensmo, S. (2018). State of the Art: Reproducibility in Artificial Intelligence. *Proceedings of AAAI-18*.
6. Kapoor, S., & Narayanan, A. (2023). Leakage and the Reproducibility Crisis in Machine-Learning-Based Science. *Patterns*, 4(9), 100804.
7. COPE. (2023). *Authorship and AI Tools: COPE Position Statement*. Committee on Publication Ethics.
8. Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the Dangers of Stochastic Parrots. *Proceedings of FAccT '21*, 610–623.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul mingguan | [Minggu 14](../03-modules/week-14-riset-berbantuan-ai-dan-reproducibility.md) |
| Lokakarya | [Lokakarya 14](../04-labs/lab-14-paket-reproduksi-dan-deklarasi-ai.md) |
| Mata kuliah terkait | [Dasar AI dan Pembelajaran Mesin](../../dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/README.md) |
| Bab sebelumnya | [Bab 12](bab-12-design-science-dan-evaluasi-artefak.md) |
| Bab berikutnya | [Bab 14 — Proposal Penelitian](bab-14-proposal-penelitian.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
