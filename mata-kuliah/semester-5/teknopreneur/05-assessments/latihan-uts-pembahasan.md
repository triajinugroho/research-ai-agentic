---
id: uai-st52510002-latihan-uts-pembahasan
tipe: asesmen
judul: "Latihan UTS — Teknopreneur — Pembahasan dan Pedoman Skor"
kode_mk: ST52510002
nama_mk: Teknopreneur
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-08
---

# Pembahasan dan Pedoman Skor — Latihan UTS Teknopreneur

**`ST52510002` · Semester Ganjil 2026/2027 · persiapan UTS Minggu 8 · Skor total 100**
**Penyusun:** Tri Aji Nugroho, S.T., M.T.

> **Latihan UTS — bukan naskah UTS.** Simulasi lengkap UTS Teknopreneur Ganjil 2026/2027 untuk berlatih: komposisi, durasi (90 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UTS. Naskah UTS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.
>
> **Buka berkas ini sesudah** Anda mengerjakan [latihan UTS](latihan-uts.md) selama 90 menit tanpa melihat pembahasan. Pasangan berkas untuk dosen: [cetak biru butir dan panduan varian](latihan-uts-cetak-biru.md).

---

## Daftar Isi

1. [Kaidah Umum Penilaian](#1-kaidah-umum-penilaian)
2. [Bagian A — Konsep](#2-bagian-a--konsep-30-poin)
3. [Bagian B — Analisis Kasus](#3-bagian-b--analisis-kasus-50-poin)
4. [Bagian C — Perancangan](#4-bagian-c--perancangan-20-poin)
5. [Rekap Skor dan Diagnosis Diri](#5-rekap-skor-dan-diagnosis-diri)
6. [Verifikasi Angka dengan Python](#6-verifikasi-angka-dengan-python)

---

## 1. Kaidah Umum Penilaian

### 1.1 Rentang skor per situasi

Tabel ini menjabarkan kaidah penilaian pada [kisi-kisi UTS §7](kisi-kisi-uts.md#7-kaidah-penilaian) menjadi rentang skor. Rentang berlaku untuk **setiap sub-butir**; rubrik per butir di §2–§4 menurunkannya menjadi poin.

| Situasi (kisi-kisi §7) | Penilaian | Rentang skor sub-butir |
|------------------------|-----------|------------------------|
| Jawaban tepat dengan alasan yang merujuk bahan | Nilai penuh | **100%** |
| **Penalaran tepat, kesimpulan berbeda dari kunci tetapi konsisten** (memenuhi K1–K4 di §1.2) | **Nilai penuh** | **100%** |
| Mengenali masalah tetapi perbaikannya kurang tepat | Nilai sebagian besar | **60–80%** |
| Jawaban tepat tanpa alasan, padahal soal meminta alasan | Nilai sebagian | **30–50%** |
| Jawaban umum tanpa merujuk bahan yang diberikan | Nilai sebagian kecil | **10–25%** |
| Kosong; bertentangan dengan bahan; memakai kutipan atau angka karangan sebagai bukti | — | **0%** |

### 1.2 Uji "berbeda tetapi konsisten" (K1–K4)

Kesimpulan yang berbeda dari kunci dinilai penuh bila memenuhi **keempat** syarat berikut.

| Kode | Syarat | Pertanyaan pemeriksa |
|------|--------|----------------------|
| **K1** | **Bertumpu pada bahan** | Apakah premisnya diambil dari bahan soal (dirujuk dengan kode/giliran/nomor) atau dari prinsip mata kuliah yang dinyatakan? |
| **K2** | **Sah** | Apakah langkah penalarannya tidak melompat, dan tidak ada kutipan atau angka yang dikarang? |
| **K3** | **Mengikuti** | Apakah kesimpulan benar-benar mengikuti dari premis yang dipakai? |
| **K4** | **Tidak mengabaikan bukti berlawanan** | Apakah bukti dalam bahan yang bertentangan dengan kesimpulannya diakui dan dijawab, bukan dilewati? |

| Keadaan | Rentang |
|---------|---------|
| K1–K4 terpenuhi | **100%** |
| K1–K3 terpenuhi; K4 dilanggar pada hal minor (ada bukti berlawanan yang tidak dibahas) | **60–80%** |
| K2 atau K3 gagal | **≤ 50%** |
| K1 gagal (tidak merujuk bahan sama sekali) | **≤ 25%** |

> **Contoh penerapan.** Pada B2(c), kunci menyimpulkan bahwa titik nyeri terbesar adalah rekap dan pertanggungjawaban akhir bulan, bukan P4: P4 unggul pada frekuensi, tetapi rekap unggul pada usaha mengatasi, yang menurut Bab 3 §3.3.3 adalah penyaring terkuat. Mahasiswa yang mempertahankan P4 karena frekuensinya mingguan **dinilai penuh** bila ia juga membahas bukti usaha mengatasi rekap (M04-1, M03-1) dan menjelaskan mengapa frekuensi tetap lebih menentukan (K4). Bila bukti itu tidak disinggung sama sekali, skornya 60–80%.

### 1.3 Cara menilai jawaban sendiri

1. **Nilai per sub-butir** dan catat skornya pada [tabel rekap §5](#5-rekap-skor-dan-diagnosis-diri), bukan hanya total butir — dari situ terlihat kemampuan mana yang masih lemah.
2. **Pembulatan:** skor sub-butir dicatat dalam kelipatan 0,5. Total boleh berpecahan 0,5.
3. **Kesalahan bawaan** (*error carried forward*): pada soal hitungan (B4), langkah yang benar tetapi memakai angka keliru dari langkah sebelumnya mendapat skor penuh untuk langkah itu. Kesalahan hanya dikurangi sekali, di tempat terjadinya. Pada B4(b), **langkah CAC** mencakup kelengkapan komponennya dan **langkah margin** mencakup biaya dukungan — keduanya dinilai pada nilainya, dan kesalahan bawaan berlaku mulai LTV/rasio (lihat pedoman skor B4).
4. **Istilah dan label:** ejaan istilah dan bahasa (Indonesia/Inggris) tidak dinilai, kecuali mengaburkan makna. **Label kerangka kerja tidak dinilai sebagai hafalan** ([kisi-kisi §4](kisi-kisi-uts.md#4-yang-diuji-dan-yang-tidak)): uraian yang setara maknanya mendapat skor yang sama dengan labelnya. Berlaku untuk setiap sub-butir yang memberi poin pada label, terutama: B3(b) — "penyewa justru terganggu bila ada" = terbalik; **A3(a)** — dimensi konteks penggunaan ([Modul 3 §3.4](../03-modules/week-03-persona-jtbd-konteks-penggunaan.md#34-konteks-penggunaan)): "bak gelap dan tergenang, tangan memegang senter" = fisik, "pemilik rumah tidak ada sehingga tanda tangan mustahil" = sosial, "180 meter sehari tidak cukup waktunya" = waktu; **A4** — jenis *constraint* ([Modul 4 §4.2](../03-modules/week-04-dari-kebutuhan-ke-persyaratan.md#42-constraint-batas-yang-tidak-dapat-ditawar)): "tidak sempat di jam sibuk" = waktu, "tidak sanggup bayar di atas 100 ribu" = biaya, "dilarang menyimpan file karena pernah ditegur kampus" = regulasi/aturan pihak lain.
5. **Bentuk jawaban:** Petunjuk 5 menyatakan jawaban ringkas, tabel, atau butir singkat sudah cukup. Jangan mengurangi skor karena jawaban tidak berbentuk kalimat utuh; pertanyaan wawancara pada C1(b) cukup ditulis sebagai kalimat tanya.
6. **Jujur pada diri sendiri:** bila ragu di antara dua rentang, ambil yang lebih rendah. Pedoman skor UTS disusun dengan kaidah yang sama.

### 1.4 Penandaan butir

Judul tiap butir di §2–§4 memuat skor, level Bloom, dan Sub-CPMK (kode registri). Penandaan Sub-CPMK per butir menurut isinya bersifat **sementara** dan dipakai untuk membaca ketercapaian; nilai UTS tetap masuk 10% nilai akhir pada `TEKNO-Sub-CPMK091-1` sesuai [RPS §G.1](../01-rps/rps-teknopreneur.md#g1-bobot-per-teknik-dan-sub-cpmk). Rinciannya ada pada [cetak biru](latihan-uts-cetak-biru.md).

Level Bloom pada judul butir adalah level butir itu sendiri. Tabel Informasi [Modul Minggu 8](../03-modules/week-08-uts-review-dan-ujian.md) mencantumkan **C2–C4**, yaitu rentang registri untuk `TEKNO-Sub-CPMK091-1`; butir latihan ini — dan UTS — berada pada C3–C6, dengan 42 dari 100 poin pada C5–C6 (menilai bahan dan merancang naskah wawancara).

---

## 2. Bagian A — Konsep (30 poin)

### A1 [9] · C3–C5 · `TEKNO-Sub-CPMKUAI32-1`

#### Kunci

**(a)** Ranah: **(2)** dan **(4)**. Solusi: **(1)** dan **(3)**.
Uji yang dipakai (salah satu): *"Dapatkah pernyataan ini dinyatakan tanpa menyebut produk atau teknologi?"*; atau *"Apakah ia menyatakan kesulitan seseorang, bukan wujud jawabannya?"*. (1) menyebut aplikasi pemesanan; (3) menyebut *chatbot* AI — keduanya menetapkan bentuk jawaban sebelum persoalannya diketahui.
*Catatan:* (4) memuat dugaan sebab ("karena tidak dapat memberi perkiraan biaya di tempat"). Ia tetap ranah karena tidak menetapkan bentuk solusi; jawaban yang menambahkan bahwa dugaan sebab itu masih harus diuji menunjukkan pemahaman yang baik (tidak menambah skor di atas maksimum).

**(b)** Alasan tim menjawab **"dapatkah dibangun?"** (kelayakan teknis). Yang belum dijawab: **adakah calon jemaah yang benar-benar mengalami kesulitan itu, seberapa sering dan berat, dan maukah mereka mengubah kebiasaan (memakai atau membayar) untuk mengatasinya?**
**Kaitannya:** penyebab kegagalan usaha teknologi yang paling sering adalah **tidak adanya kebutuhan pasar** — produknya berfungsi, tetapi tidak ada yang cukup membutuhkannya — bukan teknologi yang gagal (Bab 1 §1.1.3). Kematangan teknologi tidak menurunkan risiko itu sedikit pun. *Tambahan yang baik (tidak wajib):* teknologi yang sudah matang mudah ditiru, sehingga juga bukan keunggulan.

**(c)** Contoh ranah: *"Calon jemaah umrah yang baru pertama kali berangkat kesulitan memastikan kelengkapan dan kebenaran dokumen perjalanannya sebelum keberangkatan."* Rumusan lain diterima bila menyebut pelaku yang jelas, kesulitan yang dialaminya (bukan "butuh" suatu produk), dan tidak menyebut bentuk solusi.

#### Pedoman skor

| Sub | Maks | Rincian |
|-----|:----:|---------|
| (a) | 3 | Klasifikasi: 4 benar = 2; 3 benar = 1; 2 benar = 0,5. Uji dinyatakan dan dipakai dengan benar = 1 |
| (b) | 3 | Pertanyaan yang belum terjawab — ada-tidaknya kebutuhan atau permintaan (kesulitan nyata, seberapa sering dan berat, mau berubah atau membayar), bukan kelayakan teknis = 1,5 (pertanyaan yang masih berpusat pada produk, mis. "maukah jemaah memakai chatbot?", = 1). Kaitan dengan penyebab kegagalan tersering — tidak adanya kebutuhan pasar, yang tidak dijawab oleh kematangan teknologi = 1,5 (penyebab itu disebut tanpa dikaitkan dengan alasan tim = 1; penyebab lain tanpa dasar, mis. "kehabisan dana", = 0) |
| (c) | 3 | Pelaku jelas (mis. calon jemaah umrah, bukan "masyarakat") = 1. Kesulitan yang dialami pelaku = 1 (masih berbentuk keinginan atas sesuatu, mis. "butuh informasi yang cepat", = 0,5; "butuh chatbot/aplikasi" = 0). Bebas solusi — tanpa "chatbot", "AI", "aplikasi", "sistem", "digital" = 1 |

#### Contoh jawaban

| Tingkat | Jawaban | Skor |
|---------|---------|:----:|
| Kurang | (a) "1 dan 3 solusi, 2 dan 4 ranah." (b) "Teknologi bisa error, jadi tetap ada risiko." (c) "Jemaah umrah butuh chatbot dokumen." | 2 + 0 + 1 = **3** *((a) tanpa uji; (b) tidak menunjuk pertanyaan kebutuhan; (c) pelaku jelas, tetapi "butuh chatbot" adalah solusi)* |
| Cukup | (a) Sama, "karena 2 dan 4 terdengar seperti masalah". (b) "Belum dijawab: apakah jemaah mau memakai chatbot. Banyak usaha rintisan gagal karena tidak ada pasarnya." (c) "Calon jemaah umrah butuh informasi dokumen yang cepat." | 2 + 2 + 2,5 = **6,5** *((a) "terdengar seperti masalah" bukan uji; (b) pertanyaan masih berpusat pada chatbot (1), penyebab disebut tanpa dikaitkan dengan alasan tim (1); (c) kesulitan masih berbentuk keinginan (0,5))* |
| Baik | (a) Uji: dapatkah dinyatakan tanpa menyebut produk — (1)(3) gagal, (2)(4) lolos. (b) "Alasan itu hanya menjawab 'bisa dibangun'. Belum diketahui apakah jemaah benar-benar kesulitan mengurus dokumen dan mau berubah — padahal tidak adanya kebutuhan pasar adalah penyebab kegagalan tersering, dan risiko itu tidak berkurang karena teknologinya matang." (c) "Calon jemaah umrah pertama kali kesulitan memastikan dokumennya lengkap dan benar sebelum berangkat." | **9** |

#### Kesalahan umum

- Menggolongkan (4) sebagai solusi karena memuat kata "karena…". Dugaan sebab belum menetapkan bentuk jawaban; yang menjadikan pernyataan solusi adalah wujud produk ("aplikasi", "chatbot").
- Menjawab (b) dengan risiko teknis ("bisa error", "server down") — itu masih pertanyaan "dapatkah dibangun?", bukan "adakah yang membutuhkan?".
- Menulis ulang (3) sebagai "jemaah butuh aplikasi/informasi cepat" — kata "butuh" + benda adalah keinginan atau solusi yang disamarkan.

*Pelajari ulang:* [Bab 1 §1.1.3](../06-buku-ajar/bab-01-lanskap-teknopreneurship.md#113-mengapa-usaha-rintisan-gagal) · [Modul Minggu 1](../03-modules/week-01-lanskap-teknopreneurship.md)

---

### A2 [6] · C4 · `TEKNO-Sub-CPMK091-1`

#### Kunci

**(a)** Contoh keputusan yang **tidak dapat** diambil (salah satu):
- Masalah mana yang diselesaikan lebih dahulu: uang yang tertahan di stok (kapan dan berapa membeli) **atau** kesalahan barang keluar oleh karyawan?
- Apakah solusi dipakai satu orang, atau beberapa orang dengan peran berbeda (pemilik dan karyawan)?
- Apakah perhitungan harus memperhitungkan tempo pembayaran 30 hari?

Sebabnya: "Pak Joko" adalah **persona rata-rata** dari dua kelompok yang tujuan dan kendalanya berbeda — 7 toko mandiri-tunai dengan keluhan modal tertahan dan 5 toko berkaryawan-tempo dengan keluhan kesalahan barang keluar. Ciri "dua karyawan" dan "kadang tunai kadang tempo" tidak cocok dengan narasumber mana pun, dan pernyataannya tidak tertelusur ke kode wawancara; persona seperti itu tidak dapat memutuskan perdebatan tim.

**(b)** **Dua persona**: (1) pemilik toko mandiri, tunai, modal tertahan — W01, W02, W04, W05, W08, W10, W12 (7/12); (2) pemilik toko berkaryawan, tempo 30 hari, kesalahan barang keluar — W03, W06, W07, W09, W11 (5/12). Dasar pemisahan: perbedaan yang konsisten pada cara membayar, jumlah orang yang terlibat, dan keluhan utama.

#### Pedoman skor

| Sub | Maks | Rincian |
|-----|:----:|---------|
| (a) | 3 | Keputusan produk konkret yang tak terputuskan = 1 (generik, mis. "fitur utama" = 0,5). Sebab dijelaskan dengan merujuk ringkasan temuan = 2 — salah satu jalan cukup untuk skor penuh: (i) persona merata-ratakan dua kelompok yang tujuan atau kendalanya berbeda, dengan ciri atau jumlah kelompok dari ringkasan (7 toko tunai/modal tertahan vs 5 toko tempo/salah barang keluar); atau (ii) ciri "Pak Joko" ("dua karyawan", "kadang tunai kadang tempo") tidak cocok dengan narasumber mana pun pada ringkasan. Sebab benar tetapi tanpa ciri atau kode dari ringkasan (mis. "persona mencampur dua jenis toko") = 1. Ketidakcocokan dengan orang nyata **tidak dituntut** sebagai unsur terpisah, karena batang soal hanya meminta keputusan dan sebabnya |
| (b) | 3 | Dua persona dengan dasar pemisahan dari data = 1,5 (dasar tidak dari data = 0,5; "tiga atau lebih" tanpa dasar data = 0). Kode benar untuk kedua kelompok = 1,5 (satu kelompok saja = 0,5) |

#### Contoh jawaban

| Tingkat | Jawaban | Skor |
|---------|---------|:----:|
| Kurang | (a) "Persona kurang detail, perlu ditambah umur dan hobi." (b) "Satu persona cukup, tapi diperjelas." | 0 + 0 = **0** |
| Cukup | (a) "Tidak bisa menentukan fitur utama karena persona mencampur dua jenis toko." (b) "Dua persona: toko kecil tunai dan toko besar tempo." | 1,5 + 1,5 = **3** *((a) keputusan generik (0,5); sebab benar tetapi tanpa ciri kelompok dari ringkasan (1); (b) tanpa kode)* |
| Baik | (a) "Tidak dapat memutuskan masalah pertama: modal tertahan atau salah ambil barang. Persona merata-ratakan 7 toko tunai dan 5 toko tempo; 'dua karyawan, kadang tunai kadang tempo' tidak cocok dengan siapa pun." (b) Dua persona dengan dasar dan kode seperti kunci. | **6** |

#### Kesalahan umum

- Mengira masalahnya "persona kurang detail" lalu menambah umur, hobi, atau foto. Masalahnya bukan kurang detail, melainkan **mencampur dua kelompok** sehingga tidak mewakili siapa pun.
- Menyebut "fitur utama" sebagai keputusan yang tak terputuskan — terlalu umum; sebutkan pilihan yang benar-benar diperdebatkan (modal tertahan vs salah ambil barang).
- Menetapkan tiga persona atau lebih tanpa dasar data, atau dua persona tanpa kode wawancara.

*Pelajari ulang:* [Modul 3 §3.1.3 (berapa persona)](../03-modules/week-03-persona-jtbd-konteks-penggunaan.md#313-berapa-persona) · [Bab 3 §3.1](../06-buku-ajar/bab-03-persona-jtbd-konteks-penggunaan.md#31-persona-alat-bukan-hiasan)

---

### A3 [6] · C4–C5 · `TEKNO-Sub-CPMK091-1`

#### Kunci

**(a)** Tiga dari dimensi berikut, masing-masing dengan bukti:

| Dimensi | Bukti | Mengapa rancangan melanggarnya |
|---------|-------|-------------------------------|
| **Waktu** | O1 | ±180 meter per hari berarti sekitar 2 menit per meter termasuk berjalan (dengan anggapan 6–7 jam kerja); foto + 5 kolom + tanda tangan tidak muat |
| **Fisik / lingkungan** | O2, O3 | Bak gelap dan tergenang; tangan bersarung karet dan memegang senter — sulit memotret dan mengetik |
| **Sosial / orang yang terlibat** | O4 | Tanda tangan pemilik mustahil bila pemilik tidak ada dan pagar terkunci |
| **Perangkat dan infrastruktur** | O5 | Layar 5 inci, baterai habis pukul 13.00, sinyal hilang di gang — alur yang bergantung pada layar dan jaringan gagal |

**(b)** Perubahan konsep yang sesuai (salah satu, atau setara):
- Di lapangan hanya dicatat **angka meter dan kode rumah** (luring, satu tangan, angka besar); foto hanya untuk anomali; tanda tangan pemilik dihapus dan diganti verifikasi lewat tagihan atau pemberitahuan kepada pelanggan; sinkronisasi sekali di kantor — menghormati O1, O3, O4, O5.
- Tetap memakai formulir kertas yang sudah terbukti cocok di lapangan, lalu **digitalisasi sekali sehari di kantor** (mis. formulir baku yang dipindai) — menghormati O3, O5, O1.

*Catatan:* pembacaan angka otomatis dari foto (contoh fitur di soal) bergantung pada foto yang jelas, padahal bak gelap dan tergenang (O2), dan tidak menyelesaikan tanda tangan (O4), baterai dan sinyal (O5), atau tangan yang tidak bebas (O3). Menuliskan alasan ini tidak menambah skor, tetapi membantu menilai apakah usulan benar-benar perubahan konsep.

#### Pedoman skor

| Sub | Maks | Rincian |
|-----|:----:|---------|
| (a) | 3 | Per dimensi (maks tiga): dimensi tepat = 0,5 — **nama dimensi atau uraian setara** (§1.3 butir 4; mis. "bak gelap dan tergenang" = fisik, "pemilik tidak ada sehingga tanda tangan mustahil" = sosial; O5 boleh dinamai perangkat, infrastruktur, atau kendala); bukti (nomor pengamatan) cocok = 0,5. Dua dimensi dengan bukti yang sama dihitung satu. O2 dan O3 sama-sama dimensi **fisik** ([Modul 3 §3.4](../03-modules/week-03-persona-jtbd-konteks-penggunaan.md#34-konteks-penggunaan): di mana dipakai, tangan bebas) — dihitung satu walaupun dinamai berbeda (mis. "lingkungan" untuk O2 dan "tangan" untuk O3) |
| (b) | 3 | Usulan berupa **perubahan konsep** — mengubah apa yang dikerjakan petugas di lapangan, bukan menambah fitur = 1,5 (fitur tambahan, termasuk OCR atau mode gelap, = 0; perbaikan teknis pada alur yang sama, mis. "dibuat luring" saja, = 0,5). Dua pengamatan yang benar-benar dihormati usulan, dengan nomornya = 1,5 (satu pengamatan = 0,5) |

#### Contoh jawaban

| Tingkat | Jawaban | Skor |
|---------|---------|:----:|
| Kurang | (a) "Waktu: aplikasinya terlalu lama diisi; petugas juga tidak terbiasa teknologi." (b) "Tambah fitur OCR dan mode gelap." | 0,5 + 0 = **0,5** *((a) satu dimensi tanpa nomor pengamatan)* |
| Cukup | (a) Waktu (O1), fisik (O2), perangkat (O5). (b) "Aplikasi dibuat luring dan tombolnya besar (O3, O5)." | 3 + 2 = **5** *((b) masih alur yang sama, belum perubahan konsep)* |
| Baik | (a) Waktu O1 (±2 menit per meter), fisik O2–O3, sosial O4. (b) "Di lapangan cukup catat angka + kode rumah, luring; tanda tangan diganti verifikasi lewat tagihan; sinkron di kantor — menghormati O4 dan O5." | **6** |

#### Kesalahan umum

- Menyebut dimensi tanpa nomor pengamatan, atau memakai O2 dan O3 sebagai bukti untuk dua dimensi berbeda padahal keduanya fisik (dihitung satu).
- Menambahkan alasan yang tidak ada di bahan ("petugas tidak melek teknologi") — kutipan atau fakta karangan tidak dihitung (K2).
- Mengusulkan fitur (OCR, mode gelap, tombol besar) alih-alih mengubah **apa yang dikerjakan petugas** di depan meter.

*Pelajari ulang:* [Modul 3 §3.4 (konteks penggunaan)](../03-modules/week-03-persona-jtbd-konteks-penggunaan.md#34-konteks-penggunaan)

---

### A4 [6] · C4 · `TEKNO-Sub-CPMK091-1`

#### Kunci

| Kutipan | Jenis | Keras / lunak | Alasan |
|---------|-------|---------------|--------|
| F1 | Waktu (dan fisik: tangan terikat pada mesin) | **Keras pada jam 07.00–09.00** | Pada jendela itu memang tidak mungkin memegang hal lain; solusi apa pun tidak boleh menuntut perhatian di jam sibuk. Jawaban "belum dapat dipastikan" diterima bila mempertanyakan apakah keadaan itu terjadi setiap hari |
| F2 | Biaya | **Belum dapat dipastikan / cenderung lunak** | Berupa pendapat tentang harga di masa depan ("berat"), bukan peristiwa membayar; batas Rp100.000 dapat bergeser bila nilai yang diterima jelas. Yang dapat memastikannya adalah peristiwa — kapan terakhir membayar langganan atau alat untuk usaha, berapa, dan mengapa (tidak dituntut pada butir ini) |
| F3 | Regulasi/kebijakan pihak lain dan privasi data | **Keras** | Didukung peristiwa nyata (teguran kampus) dan perilaku yang sudah berubah (menghapus file tiap tutup toko); solusi tidak boleh menyimpan file pelanggan melewati hari itu. Juga soal **amanah** atas data orang lain |

#### Pedoman skor

| Sub | Maks | Rincian |
|-----|:----:|---------|
| — | 6 | Per kutipan (F1, F2, F3): jenis tepat = 1 — **nama jenis atau uraian setara** (§1.3 butir 4; mis. "tidak sempat di jam sibuk" = waktu, "tidak sanggup bayar di atas 100 ribu" = biaya, "dilarang menyimpan file sejak ditegur kampus" = regulasi/aturan pihak lain; F3 sebagai privasi data atau amanah juga tepat). Keras/lunak/belum pasti **dengan alasan** yang konsisten dan merujuk isi kutipan = 1 (alasan umum yang tidak merujuk isi kutipan, mis. "karena dikatakan pemiliknya", = 0,5; tanpa alasan = 0). Penilaian sifat yang berbeda dari kunci dinilai dengan K1–K4 (mis. F2 "keras" yang mengakui bahwa "berat" baru pendapat, tetapi menunjuk "listrik sejuta lebih" sebagai tekanan biaya nyata) |

#### Contoh jawaban

| Tingkat | Jawaban | Skor |
|---------|---------|:----:|
| Kurang | "F1 biaya, F2 biaya, F3 waktu; semuanya keras." | **1** *(jenis tepat hanya F2; sifat tanpa alasan)* |
| Cukup | "F1 waktu — keras; F2 biaya — lunak; F3 privasi — keras, karena pernah ditegur kampus." | **4** *(jenis 3; sifat beralasan hanya F3)* |
| Baik | Seperti kunci: jenis ketiganya; F1 keras pada jam sibuk (antrean 07.00–09.00, tangan pada mesin); F2 belum pasti karena baru pendapat tentang harga; F3 keras karena teguran nyata dan perilaku yang sudah berubah. | **6** |

#### Kesalahan umum

- Menilai semua kutipan "keras" hanya karena diucapkan narasumber. Yang membuat *constraint* keras adalah **peristiwa atau keadaan yang tidak dapat ditawar**, bukan nada bicara.
- Menganggap F2 pasti keras tanpa membahas bahwa "berat" baru pendapat tentang harga di masa depan.
- Menamai F3 "waktu" karena ada frasa "tiap tutup toko" — intinya larangan menyimpan data orang lain.

*Pelajari ulang:* [Modul 4 §4.2 dan §4.2.1](../03-modules/week-04-dari-kebutuhan-ke-persyaratan.md#421-memisahkan-constraint-keras-dan-lunak) · [Bab 1 §1.5.2 (amanah atas data)](../06-buku-ajar/bab-01-lanskap-teknopreneurship.md#152-amanah-atas-data-orang-lain)

---

### A5 [3] · C5 · `TEKNO-Sub-CPMKUAI21-1`

#### Kunci

Urutan kunci: **(i) > (iii) > (ii) > (iv)** — sejalan dengan Bab 6 §6.3.1: asumsi berdampak besar yang keyakinannya rendah diuji lebih dahulu.

| Urutan | Ketergantungan | Dampak bila salah | Kekuatan bukti |
|:------:|----------------|-------------------|----------------|
| 1 | (i) Data jadwal dari pengelola dermaga | **Sangat besar** — tanpa data jadwal tidak ada layanan | **Paling lemah** — belum ada kontak; tidak diketahui apakah datanya ada, berbentuk apa, dan boleh dibagikan |
| 2 | (iii) Ketua paguyuban meneruskan | Besar — inilah saluran distribusi kepada pedagang | Sedang — 2 dari 3 ketua, satu minggu, dengan pesan diketik tim (belum mencerminkan keadaan rutin) |
| 3 | (ii) Layanan pesan berbayar | Sedang — memengaruhi biaya per pesan dan margin, tetapi ada alternatif (pesan manual, grup) | Kuat — tarif terbuka |
| 4 | (iv) Komputasi awan gratis | Kecil — mudah dipindah, alternatif banyak | Kuat — sudah dipakai |

Alasan hanya diminta untuk butir **teratas**; tabel di atas (termasuk baris 2–4) adalah pegangan penilai, bukan jawaban yang dituntut. (ii) dan (iv) boleh bertukar di dua posisi terbawah karena buktinya sama-sama kuat. Urutan lain **konsisten** bila alasan butir teratasnya memakai kedua pertimbangan. Contoh yang dinilai penuh: menempatkan (iii) teratas dengan alasan bahwa jadwal dapat dicatat manual oleh tim dari papan pengumuman dermaga sehingga dampak (i) lebih kecil, sedangkan bukti (iii) hanya satu minggu dengan bantuan tim. Menempatkan (iv) teratas tanpa alasan dari kedua sumbu tidak konsisten.

#### Pedoman skor

| Sub | Maks | Rincian |
|-----|:----:|---------|
| — | 3 | Urutan = 1: butir teratas (i) — atau (iii) dengan alasan yang memenuhi K1–K4 — = 0,5; dua posisi terbawah ditempati (ii) dan (iv), dalam urutan mana pun = 0,5 (hanya salah satunya = 0). Alasan butir teratas dengan **kedua** pertimbangan (dampak bila salah, kekuatan bukti) = 2; satu pertimbangan = 1; satu pertimbangan yang bertentangan dengan bahan (mis. dampak besar bagi (iv), padahal sudah dipakai dan mudah dipindah) = 0,5. Alasan untuk butir lain tidak dituntut dan tidak menambah skor |

#### Contoh jawaban

| Tingkat | Jawaban | Skor |
|---------|---------|:----:|
| Kurang | "(iv) paling berisiko karena server gratis bisa mati, lalu (ii), (i), (iii)." | **0,5** *(urutan: teratas dan dua posisi terbawah tidak sesuai (0); alasan teratas hanya memakai sumbu dampak dan bertentangan dengan bukti bahwa (iv) sudah dipakai (0,5))* |
| Cukup | "(i) paling berisiko karena belum ada kontak sama sekali. Lalu (iii), (ii), (iv)." | **2** *(urutan 1; alasan teratas hanya memakai sumbu bukti (1))* |
| Baik | Urutan seperti kunci; (i) dampak terbesar (tanpa jadwal tidak ada layanan) dan bukti terlemah (belum ada kontak). | **3** |

#### Kesalahan umum

- Menempatkan risiko teknis (server gratis) teratas karena "terdengar teknis" — padahal dampaknya kecil dan buktinya kuat.
- Memberi alasan dengan satu sumbu saja; soal meminta **dua**: dampak bila salah **dan** kekuatan bukti.
- Menulis alasan panjang untuk keempat butir — tidak menambah skor dan menghabiskan waktu.

*Pelajari ulang:* [Bab 6 §6.3.1 (mengurutkan asumsi)](../06-buku-ajar/bab-06-kelayakan-teknologi-dan-operasional.md#631-mengurutkan-asumsi)

---

## 3. Bagian B — Analisis Kasus (50 poin)

### B1 [13] · C4 · `TEKNO-Sub-CPMK091-1`

#### Kunci

**(a)** Tiga dari kesalahan berikut, **berbeda jenisnya**:

| G | Kesalahan | Kerusakan pada mutu data |
|---|-----------|--------------------------|
| G1 | **Menyebut solusi di pembuka** ("mengembangkan aplikasi"); pembuka juga tidak menyatakan bukan untuk menjual dan durasi | Narasumber menilai gagasan, bukan menceritakan hidupnya; ia menjadi defensif (G2: "nggak ngerti HP") — seluruh wawancara condong ke aplikasi |
| G3 | **Pertanyaan memimpin**, berbentuk ya/tidak ("Pasti repot ya…") | Dugaan pewawancara disodorkan; jawaban "iya" adalah kesopanan |
| G5 | **Pertanyaan hipotetis tentang masa depan** sekaligus menyebut fitur | Meminta ramalan; "mau" (G6) tidak memprediksi perilaku |
| G7 | **Menyebut angka lebih dulu** | Mengunci jawaban; G8 hanya mengiyakan angka pewawancara |
| G9 | **Membetulkan/menggurui dan menjual solusi** (*barcode*) | Pewawancara berbicara lebih banyak; narasumber berhenti bercerita; kepercayaan rusak |
| G11 | **Penutup tanpa meminta rujukan** (dan izin menghubungi lagi) | Kehilangan jalan ke narasumber berikutnya — bagian paling bernilai per menit |
| G6→G7, G10→G11 | **Tidak menggali** petunjuk penting (WA malam-malam, peniti warna, HP hanya pagi dan malam) | Solusi tempelan dan *constraint* terlewat; diterima sebagai salah satu dari tiga bila berbeda jenis dari dua lainnya |

**(b)** Dua cara buatan sendiri (solusi tempelan) untuk **dua persoalan yang berbeda** — cucian tidak diambil (G6) dan cucian tertukar (G4, G10). "Tulis di buku" dan "WA satu-satu" pada G6 adalah **satu** cara untuk satu persoalan:
- **G6 — "Saya tulis di buku, terus kadang saya WA satu-satu malam-malam."** Cucian yang tidak diambil adalah nyeri nyata yang sudah ia tanggung dengan usaha sendiri (malam hari, satu per satu) — bukti kebutuhan yang jauh lebih kuat daripada "mau, mau". Cara ini juga memperlihatkan **kapan** ia dapat bertindak (malam).
- **G10 — "Saya mah pakai peniti warna aja dari dulu."** Masalah cucian tertukar sudah teratasi dengan cara murah yang berjalan bertahun-tahun (G4: paling sebulan sekali) — nyerinya kecil, dan solusi apa pun untuk masalah ini harus mengalahkan peniti; usulan *barcode* (G9) tidak berdasar.

**(c)**
- **Keinginan** (tidak boleh disalin menjadi kebutuhan): "pengingat buat pelanggan" (G6) dan "notifikasi" (yang disodorkan pewawancara di G5).
- **Kebutuhan (bebas solusi):** *"Cucian yang sudah selesai segera diambil pemiliknya sehingga rak tidak penuh, tanpa pemilik laundry harus menghubungi pelanggan satu per satu pada malam hari."* **Bukti:** G6.
- **Constraint (G10):** ponsel hanya tersedia pagi dan malam.
- **Persyaratan terukur (contoh):** *"Pemilik laundry dapat memberi tahu seluruh pelanggan yang cuciannya sudah siap lebih dari 7 hari [G6: 'lebih dari seminggu'] dalam satu kali kerja tidak lebih dari 10 menit [asumsi — perlu diuji], yang dapat dilakukan pagi atau malam tanpa memerlukan ponsel pada siang hari [G10], dan tanpa mengetik pesan satu per satu [G6]. Sumber: G6, G10."* Persyaratan ini dapat dipenuhi tanpa perangkat lunak baru — mis. satu pesan siaran dari aplikasi pesan yang sudah ada di ponsel, dikirim pagi hari kepada pelanggan yang tercatat di buku — dan **kebutuhannya** bahkan dapat dipenuhi tanpa perangkat lunak sama sekali (mis. kartu ambil bertanggal batas yang diberikan saat cucian diterima, yang mencegah cucian menumpuk). Keduanya tanda bahwa kebutuhan dan persyaratan ditulis bebas solusi. Perhatikan bedanya: kartu ambil memenuhi **kebutuhan**, tetapi tidak memenuhi **persyaratan** di atas, karena persyaratan itu menuntut pemberitahuan kepada pelanggan yang cuciannya sudah lewat 7 hari.
- *Varian konsisten:* kebutuhan "cucian kembali kepada pemilik yang benar" (G4, G10) diterima penuh **hanya** bila jawaban mengakui bahwa buktinya lemah (G4 berupa ringkasan "biasanya", sebulan sekali; peniti sudah bekerja); tanpa pengakuan itu 60–80% (K4).

#### Pedoman skor

| Sub | Maks | Rincian |
|-----|:----:|---------|
| (a) | 3 | Per kesalahan (maks 3, harus berbeda jenis): giliran + jenis tepat = 0,5; kerusakan pada data dijelaskan = 0,5. Dua kesalahan sejenis dihitung satu. Bila lebih dari tiga ditulis, yang dinilai tiga yang pertama. Bentuk tabel sudah cukup |
| (b) | 3 | Per cara (G6, G10): ditunjukkan dengan nomor giliran = 0,5; arti bagi tim dijelaskan (bukti nyeri dan usaha / nyeri kecil dan pesaing yang harus dikalahkan, atau setara) = 1 (sekadar "dia punya cara sendiri" = 0,5). Jawaban "buku" dan "WA satu-satu" (keduanya G6, satu persoalan) **dihitung satu cara** — dinilai penuh untuk cara G6; cara kedua (peniti, G10) yang tidak disebut = 0 |
| (c) | 7 | Kebutuhan bebas solusi (tanpa "pengingat", "notifikasi", "aplikasi") = 2. Nomor giliran bukti (G6) = 0,5. Persyaratan: pelaku + tindakan = 1 (pelaku tidak disebut atau berupa "sistem", mis. "pengingat terkirim otomatis", = 0,5); ukuran dari transkrip atau ditandai asumsi = 1 (angka karangan tanpa tanda = 0); batasan dari G10 sebagai batas yang dapat diperiksa (ponsel hanya pagi dan malam) = 2 (hanya disinggung, mis. "menyesuaikan waktu Ibu" = 0,5); sumber = 0,5 |

#### Contoh jawaban

| Tingkat | Jawaban (ringkas) | Skor |
|---------|-------------------|:----:|
| Kurang | (a) "G1 menyebut aplikasi; G3 mengarahkan; G9 bagus karena memberi solusi; G11 terlalu cepat." (b) "Peniti dan buku." (c) "Kebutuhan: aplikasi pengingat pengambilan cucian (G6)." | 1 + 0 + 0,5 = **1,5** *((a) dinilai tiga yang pertama: G1, G3 tanpa kerusakan data, G9 keliru; (b) tanpa nomor giliran dan tanpa arti)* |
| Cukup | (a) G1 menyebut aplikasi; G3 memimpin; G5 hipotetis — kerusakan dijelaskan untuk dua di antaranya. (b) "G10 peniti warna: sudah punya cara sendiri. G6 WA satu-satu: repot." (c) "Kebutuhan: pelanggan cepat mengambil cucian (G6). Persyaratan: pengingat terkirim otomatis setiap hari." | 2,5 + 2 + 3 = **7,5** *((c) kebutuhan 2 + bukti 0,5; persyaratan berupa fitur dengan pelaku "sistem" (0,5), tanpa ukuran dari transkrip, tanpa batasan G10 dan sumber)* |
| Baik | (a) G1, G3, G5 (atau G7, G9, G11) dengan kerusakan datanya. (b) Seperti kunci. (c) Kebutuhan bebas solusi + bukti G6 + persyaratan "pemilik laundry … > 7 hari, ≤ 10 menit [asumsi], pagi/malam tanpa ponsel siang hari, tanpa pesan satu per satu, sumber G6/G10". | **13** |

#### Kesalahan umum

- Menganggap G9 sebagai hal baik ("pewawancara memberi solusi"). Dalam wawancara masalah, menawarkan solusi merusak data.
- Memberi label jenis yang sama untuk tiga giliran (mis. semuanya "pertanyaan memimpin") — kesalahan sejenis dihitung satu. Bedakan: memimpin (G3), hipotetis (G5), menyebut angka lebih dulu (G7).
- Pada (b), menulis "buku" dan "WA" sebagai dua cara — keduanya satu cara untuk satu persoalan (G6); peniti warna (G10) terlewat.
- Pada (c), menyalin keinginan ("pengingat otomatis") sebagai kebutuhan; menulis pelaku "sistem"; memakai angka karangan tanpa tanda asumsi; atau hanya menyinggung G10 ("menyesuaikan waktu Ibu") tanpa batas yang dapat diperiksa.

*Pelajari ulang:* [Bab 2 §2.2.4 (yang tidak boleh diucapkan)](../06-buku-ajar/bab-02-penemuan-masalah-dan-pelanggan.md#224-yang-tidak-boleh-diucapkan) · [Bab 2 §2.5](../06-buku-ajar/bab-02-penemuan-masalah-dan-pelanggan.md#25-kesalahan-yang-berulang-setiap-tahun) · [Bab 4 §4.2.1 (unsur wajib persyaratan)](../06-buku-ajar/bab-04-dari-kebutuhan-ke-persyaratan.md#421-unsur-wajib)

---

### B2 [13] · C4–C5 · `TEKNO-Sub-CPMK091-1`

#### Kunci

**(a)**

| Baris | Penilaian | Alasan |
|-------|-----------|--------|
| P1 | *Contoh pada soal — tidak dinilai* (didukung) | M01-1 menyatakan sukarela dan bekerja di toko bangunan (catatan: baru 1 narasumber) |
| P2 | **Berlebihan** *(atau salah rujuk)* | M05-1 hanya menyebut satu orang berusia 63; "pensiunan" tidak disebut siapa pun, dan M01-1 justru masih bekerja |
| P3 | **Salah rujuk** | M04-1 justru membantah: *spreadsheet* dibuat orang lain dan ditinggalkan karena "nggak ada yang ngerti" |
| P4 | **Salah rujuk** *(atau berlebihan)* | M01-2 menggambarkan penghitungan, tetapi tidak menyebutnya kesulitan terbesar; M02-1 menyatakan yang paling berat adalah akhir bulan |
| P5 | *Contoh pada soal — tidak dinilai* (tanpa bukti) | Bersumber dari diskusi tim; berupa keinginan tim dalam bentuk solusi — dihapus |
| KP | **Tanpa bukti** | Tidak verbatim dan tanpa kode; harus diganti kutipan asli, mis. M05-1 atau M02-1 |

**(b)** Gagal pada ujian **bebas solusi** ("aplikasi yang otomatis merekap") dan **tertelusur** ("laporan lebih modern" tidak ada pada kutipan mana pun; yang dicari narasumber adalah dipercaya dan tidak dicurigai). Lolos ujian **sudah dikerjakan sekarang** bila dibaca dari tindakan merekap pada bagian *ingin*: rekap memang dikerjakan setiap akhir bulan secara manual (M02-1).
*Varian konsisten — gagal ketiganya.* Batang soal berbunyi "sekurang-kurangnya dua", jadi jawaban bahwa ujian **sudah dikerjakan sekarang** juga gagal **dapat dipertahankan** bila dibaca dari bagian *sehingga*: hasil "laporan keuangan masjid lebih modern" tidak sedang diupayakan siapa pun; yang diupayakan bendahara adalah pertanggungjawaban dan kepercayaan jamaah (M03-1, M05-1; juga M01-2). Jawaban ini dinilai dengan K1–K4 dan **penuh** bila alasannya bertumpu pada bagian *sehingga* dengan kode kutipan.
Rumusan ulang (contoh):
> *"Ketika akhir bulan saya harus menggabungkan infak dari kotak Jumat, transfer, QRIS, dan kotak keliling [M02-1], saya ingin setiap rupiah tercatat menurut sumbernya tanpa harus menyalin ulang sampai larut malam [M02-1], sehingga saya dapat mempertanggungjawabkan saldo kepada jamaah tanpa dicurigai atau dipermalukan [M05-1, M03-1]."*

Lapis pada bagian *sehingga*: **emosional** — takut dicurigai menyalahgunakan uang masjid (M05-1), malu ketika ditanya jamaah (M03-1); **sosial** — ingin terlihat amanah dan terbuka di mata jamaah (mutasi ditempel, M03-1; dicatat dengan saksi, M01-2, M05-1).

**(c)**

| Kriteria | Penghitungan kotak (P4) | Rekap dan pertanggungjawaban akhir bulan |
|----------|-------------------------|------------------------------------------|
| Frekuensi | **Mingguan** — setiap Jumat (M01-2). *Sebaran bukti:* 1 narasumber | **Bulanan** — akhir bulan (M02-1). *Sebaran bukti:* 3 narasumber (M02-1, M03-1, M05-1) |
| Usaha mengatasi | Belum ada upaya mengatasi lamanya menghitung; menghitung bertiga dengan saksi adalah tata cara menjaga amanah, bukan upaya mengatasi nyerinya | Sudah dicoba berkali-kali: *spreadsheet* (M04-1, ditinggalkan), cetak dan tempel mutasi (M03-1), dicatat dengan saksi (M05-1) |

Menurut definisi Bab 3 §3.3.3 ("berapa kali sehari/seminggu terjadi?"), **frekuensi berpihak pada P4**: penghitungan kotak terjadi setiap minggu, rekap sebulan sekali. Membaca frekuensi sebagai sebaran bukti (1 vs 3 narasumber) juga diterima — keduanya mendapat poin kriteria bila dirujuk dengan kode kutipan.

**Kesimpulan kunci:** P4 unggul pada frekuensi, tetapi rekap dan pertanggungjawaban akhir bulan unggul pada **usaha mengatasi** — kriteria yang menurut Bab 3 §3.3.3 adalah penyaring terkuat — sehingga penetapan P4 **kurang tepat**. Titik nyeri terbesar yang lebih didukung bukti adalah **rekap lintas sumber dan pertanggungjawaban akhir bulan**. *Pegangan tambahan (tidak diminta dan tidak menambah skor):* besarannya pun lebih berat — sampai tengah malam, selisih Rp350.000 dicari tiga malam (M02-1), malu ditanya jamaah (M03-1) — dibanding "kadang sampai jam dua" pada P4. Kesimpulan lain dinilai dengan uji K1–K4 (lihat contoh di §1.2).

#### Pedoman skor

| Sub | Maks | Rincian |
|-----|:----:|---------|
| (a) | 5 | Jumlah baris yang dinilai benar **dengan alasan**, dari empat baris yang diminta (P2, P3, P4, KP): 4 = 5; 3,5 = 4; 3 = 3,5; 2,5 = 3; 2 = 2; 1,5 = 1,5; 1 = 1; 0,5 = 0,5. Penilaian benar tanpa alasan dihitung setengah baris. Kategori alternatif yang tercantum di kunci (P2, P4) dihitung benar. P1 dan P5 dicetak sebagai contoh dan tidak dinilai |
| (b) | 4 | Ujian yang gagal ditunjukkan dengan alasan = 1: bebas solusi dan tertelusur (kunci) — satu saja = 0,5. Menyatakan ujian ketiga (**sudah dikerjakan sekarang**) juga gagal dinilai dengan K1–K4: **1** bila beralasan dari bagian *sehingga* dengan rujukan kutipan (lihat varian di kunci); "gagal ketiganya" **tanpa alasan** untuk ujian ketiga = 0,5. Rumusan ulang bebas solusi dengan format *ketika–ingin–sehingga* = 1,5. Bagian *sehingga* memuat lapis emosional/sosial yang bertumpu pada kutipan = 1 ("lebih rapi", "lebih cepat" saja = 0). Kode kutipan menyertai = 0,5 |
| (c) | 4 | Per kriteria (frekuensi, usaha mengatasi) diterapkan pada **kedua** titik nyeri — P4 dan rekap akhir bulan — dengan kode kutipan = 1,5 (tanpa kode = 1; hanya pada satu titik nyeri = 0,5). Frekuensi kejadian (mingguan vs bulanan) maupun sebaran bukti (1 vs 3 narasumber) sama-sama diterima. Kesimpulan eksplisit yang konsisten dengan kedua kriteria sebagaimana diterapkan = 1; bila kedua kriteria berlawanan arah (frekuensi kejadian berpihak pada P4), nilai 1 menuntut kesimpulan yang **menimbang** keduanya (mis. usaha mengatasi sebagai penyaring terkuat) — tanpa menimbang = 0,5. Kesimpulan yang mengabaikan bukti berlawanan dalam bahan, mis. menyetujui P4 tanpa menyinggung rekap akhir bulan, = 0. Kesimpulan yang berbeda dinilai dengan K1–K4. Kriteria besaran tidak diminta: menyebutnya tidak menambah skor |

#### Contoh jawaban

| Tingkat | Jawaban (ringkas) | Skor |
|---------|-------------------|:----:|
| Kurang | (a) "P2, P3, P4 didukung karena ada sumbernya; KP tanpa bukti." (b) "Job-nya sudah bagus, tinggal tambah fitur dasbor." (c) "Setuju, menghitung receh tiap Jumat melelahkan (M01-2)." | 0,5 + 0 + 0,5 = **1** *((a) satu baris benar tanpa alasan (KP); (c) frekuensi hanya untuk P4 (0,5); kesimpulan mengabaikan bukti rekap akhir bulan (0))* |
| Cukup | (a) P3 salah rujuk (M04-1 justru ditinggalkan); KP tanpa bukti (tanpa kode, bukan kutipan narasumber); P2 dan P4 "didukung". (b) "Gagal bebas solusi. Ulang: Ketika akhir bulan, saya ingin rekap infak cepat, sehingga laporan selesai." (c) "Frekuensi: P4 tiap Jumat, lebih sering daripada rekap akhir bulan. Usaha: rekap sudah dicoba dengan *spreadsheet* (M04-1). Jadi P4 kurang tepat." | 2 + 2 + 2 = **6** *((a) dua baris benar dengan alasan; (b) satu ujian, tanpa lapis emosional/sosial dan kode; (c) frekuensi pada kedua sisi tanpa kode (1), usaha hanya untuk rekap (0,5), kesimpulan tanpa menimbang frekuensi yang berpihak pada P4 (0,5))* |
| Baik | Seperti kunci: empat baris benar dengan alasan; dua ujian gagal ditunjukkan; *job* bebas solusi bertanda kode dengan "tanpa dicurigai atau dipermalukan"; frekuensi dan usaha mengatasi diterapkan pada P4 dan rekap dengan kode, lalu kesimpulan yang menimbang keduanya (usaha mengatasi sebagai penyaring terkuat). | **13** |

#### Kesalahan umum

- Menilai baris "didukung" hanya karena kolom sumbernya terisi. Periksa **isi** kutipan yang dirujuk: M04-1 justru membantah P3.
- Menulis ulang *job* yang masih menyebut aplikasi, rekap otomatis, atau dasbor; atau bagian *sehingga* hanya "lebih cepat/rapi" tanpa lapis emosional atau sosial dari kutipan.
- Menyetujui P4 hanya karena lebih sering, tanpa membahas usaha mengatasi rekap akhir bulan (M04-1, M03-1) — kesimpulan berbeda boleh, tetapi bukti yang berlawanan wajib dijawab (K4).
- Menulis bahwa rekap akhir bulan "lebih sering" daripada P4. Menurut Bab 3 §3.3.3 frekuensi adalah berapa kali kejadian terjadi — P4 setiap minggu, rekap sebulan sekali; yang membuat rekap lebih berat adalah usaha mengatasinya. Membaca frekuensi sebagai sebaran bukti (1 vs 3 narasumber) diterima bila dinyatakan demikian. Bila kedua kriteria berlawanan arah, kesimpulan yang baik menyatakannya lalu menimbangnya.

*Pelajari ulang:* [Bab 3 §3.1.2](../06-buku-ajar/bab-03-persona-jtbd-konteks-penggunaan.md#312-persona-berbasis-bukti-vs-persona-karangan) · [Bab 3 §3.2.2 (tiga ujian *job*)](../06-buku-ajar/bab-03-persona-jtbd-konteks-penggunaan.md#322-bentuk-pernyataan-job) · [Bab 3 §3.3.3 (titik nyeri terbesar)](../06-buku-ajar/bab-03-persona-jtbd-konteks-penggunaan.md#333-aturan-titik-nyeri-terbesar)

---

### B3 [12] · C4–C5 · `TEKNO-Sub-CPMK091-1`

#### Kunci

**(a)**

| ID | Kutipan induk | Kutipan yang menunjukkan tidak dibutuhkan atau ditolak | Status |
|----|---------------|--------------------------------------------------------|--------|
| R1 | tidak ada | **S04-1** — penyewa datang langsung, ingin melihat barang, dan tawar-menawar | **Tanpa induk** (bertentangan dengan bukti) |
| R2 | **S02-1** — bukti kondisi barang yang disepakati saat pengembalian, agar kerusakan/kehilangan tidak ditanggung pemilik; *constraint* S06-1 | — | Berinduk |
| R3 | tidak ada | **S07-2** — DP lewat transfer "nggak masalah" | **Tanpa induk** (tidak ada masalah yang dilayani) |
| R4 | tidak ada | **S05-2** — penagihan lewat pesan menyinggung penyewa (juga S07-2: pelunasan tunai saat barang kembali) | **Tanpa induk** (bertentangan dengan bukti) |
| R5 | **S01-2** — mencatat barang keluar-masuk tanpa mengandalkan ingatan dan nota saat musim ramai; *constraint* S06-1 | — | Berinduk, tetapi "praktis dan rapi" belum terukur (tidak dituntut) |

*Penalaran setara:* penilaian yang berbeda pada satu baris dinilai dengan K1–K4 bila bertumpu pada kutipan — mis. menganggap R5 belum layak disebut berinduk karena "praktis dan rapi" tidak dapat diturunkan dari S01-2, atau menunjuk S07-2 untuk R4 (pelunasan sudah berjalan tunai saat barang kembali).

**(b)**
- **R1** — **acuh** (tidak menambah kepuasan): penyewa ingin datang, melihat barang, dan tawar-menawar (S04-1). Tindakan: **Won't (kali ini)**, alasannya dicatat (boleh ditambah kapan ditinjau ulang, mis. bila segmen berubah ke penyewa perkotaan — tidak dinilai). *Varian konsisten:* "terbalik" bagi penyewa yang mengandalkan tatap muka dan tawar-menawar untuk membangun kepercayaan — diterima bila beralasan pada S04-1; pada varian ini R1 juga dicatat sebagai larangan ("tidak memaksa pemesanan daring").
- **R4** — **terbalik**: penagihan lewat pesan menyinggung penyewa yang baru selesai hajatan dan membuat mereka tidak menyewa lagi (S05-2); pelunasan juga sudah berjalan tunai saat barang kembali (S07-2). Tindakan: **Won't** dan **dicatat sebagai larangan** ("tidak mengirim penagihan otomatis kepada penyewa").

#### Pedoman skor

| Sub | Maks | Rincian |
|-----|:----:|---------|
| (a) | 5 | R2 (S02-1) dan R5 (S01-2): kode induk tepat = 1 masing-masing; menambahkan S06-1 sebagai *constraint* boleh, tidak menambah skor. R1, R3, R4: "tidak ada" beserta kode kutipan penunjuk yang tepat (R1: S04-1; R3: S07-2; R4: S05-2 atau S07-2) = 1 masing-masing ("tidak ada" tanpa kutipan penunjuk = 0,5). Menandai persyaratan lain (mis. R5) juga tanpa induk **tidak membatalkan** poin baris lain — baris itu sendiri dinilai dengan K1–K4. Bentuk tabel sudah cukup |
| (b) | 7 | Per persyaratan (R1, R4) = 3,5: jenis Kano **atau uraian hubungan kepuasan yang setara** (mis. "penyewa justru terganggu bila ada" untuk terbalik; "tidak berpengaruh pada kepuasan" untuk acuh) = 1 — label tidak wajib; alasan yang menautkan isi kutipan (S04-1 untuk R1; S05-2 untuk R4) dengan reaksi penyewa = 1 (kode saja tanpa isi = 0,5); tindakan prioritas *Won't* = 0,5; alasan *Won't* dicatat — dan, bila persyaratan itu dinilai **terbalik** (R4; juga R1 pada varian terbalik), dicatat sebagai **larangan** = 1. Kapan R1 ditinjau ulang tidak diminta soal dan tidak dinilai |

#### Contoh jawaban

| Tingkat | Jawaban (ringkas) | Skor |
|---------|-------------------|:----:|
| Kurang | (a) "Semua persyaratan berguna." (b) "R1 penggoda, R4 dasar." | 0 + 0 = **0** |
| Cukup | (a) R2 → S02-1, R5 → S01-2, R1 dan R4 "tidak ada"; R3 tidak dibahas. (b) "R4: penyewa justru tersinggung bila ditagih lewat HP (S05-2) → hapus. R1 tidak penting." | 3 + 3 = **6** *((a) R1 dan R4 tanpa kutipan penunjuk (0,5 + 0,5); (b) R4 tanpa catatan larangan (2,5); R1 hanya "tidak penting" tanpa bukti dan tindakan (0,5))* |
| Baik | Seperti kunci: R2 dan R5 dengan induknya; R1, R3, R4 "tidak ada" dengan kutipan penunjuk; R1 acuh dan R4 terbalik (atau uraian setara) dengan alasan dari kutipan, *Won't*, dan larangan untuk R4. | **12** |

#### Kesalahan umum

- Menulis "tidak ada" tanpa kutipan penunjuk — tanpa penunjuk, jawaban itu tidak dapat dibedakan dari tebakan.
- Menganggap R3 berinduk karena "pembayaran memang ada" — S07-2 menyatakan DP lewat transfer tidak bermasalah, jadi tidak ada persoalan yang dilayani.
- Menggolongkan R4 sebagai dasar atau kinerja, padahal S05-2 menyatakan penyewa justru tersinggung bila ditagih lewat pesan; atau menghapus R4 tanpa mencatatnya sebagai **larangan**, sehingga ia dapat muncul lagi pada sprint berikutnya.

*Pelajari ulang:* [Bab 4 §4.3.2 (model Kano)](../06-buku-ajar/bab-04-dari-kebutuhan-ke-persyaratan.md#432-model-kano) · [Bab 4 §4.3.3 (Kano × MoSCoW, larangan)](../06-buku-ajar/bab-04-dari-kebutuhan-ke-persyaratan.md#433-gabungan-keduanya) · [Bab 4 §4.4.2 (ujian ketertelusuran)](../06-buku-ajar/bab-04-dari-kebutuhan-ke-persyaratan.md#442-ujian-ketertelusuran)

---

### B4 [12] · C4–C5 · `TEKNO-Sub-CPMKUAI21-1` (a–b) · `TEKNO-Sub-CPMKUAI32-1` (c)

#### Kunci langkah demi langkah

**(a) Hitung ulang SOM:**

```
Jam lapangan      = 3 orang × 4 jam/minggu            = 12 jam/minggu
Pengemudi/jam     = 60 menit ÷ 30 menit               = 2 pengemudi/jam
Dijangkau/minggu  = 12 × 2                            = 24 pengemudi
Dijangkau/tahun   = 24 × 40 minggu                    = 960 pengemudi
Proporsi membayar = 3 ÷ 16                            = 18,75%
Pelanggan         = 960 × 3/16                        = 180 pelanggan
SOM tahun pertama = 180 × Rp35.000 × 12               = Rp75.600.000
```

**Pengali yang diganti dan alasannya:**
- **10% dapat dijangkau** — "target realistis" tanpa hitungan; kapasitas nyata tim (D1) hanya 960 per tahun.
- **75% bersedia membayar** — pendapat, bukan perilaku: "mau" ≠ membayar; yang sah adalah yang pernah membayar, 3/16 (D2).

**Pengali lain yang tetap bermasalah** (salah satu):

| Pengali | Masalah |
|---------|---------|
| 60.000 pengemudi | **Sumber tidak sah**: jawaban asisten AI tanpa rujukan; harus diganti angka yang dapat ditelusuri (pencacahan pangkalan di 3 kecamatan, data resmi bila ada) |
| 20% di 3 kecamatan | **Asumsi lemah** (perkiraan tim) — ditandai dan diuji, mis. dengan pencacahan |
| × 12 bulan | **Mengabaikan churn dan akuisisi bertahap**: tidak semua pelanggan membayar 12 bulan pada tahun pertama — 3 dari 12 berhenti dalam 2 bulan (D5, rata-rata ±7 bulan) dan akuisisi tersebar sepanjang 40 minggu (D1) |

SOM terkoreksi **Rp75.600.000**, seperlima angka tim (Rp378.000.000). Karena kapasitas tim yang mengikat (960 < 12.000), angka 60.000 dan 20% tidak memengaruhi hasil — tetapi tetap wajib diverifikasi untuk memastikan populasi di 3 kecamatan memang ≥ 960.
*Varian konsisten:* SOM yang **diturunkan lagi** untuk akuisisi bertahap atau churn (mis. rata-rata 6 bulan berbayar pada tahun pertama → 180 × Rp35.000 × 6 = Rp37.800.000) dinilai dengan K1–K4 — **penuh** bila asumsinya dinyatakan dan dihitung konsisten.

**(b) CAC, margin, LTV, rasio:**

```
Nilai waktu tim      = 42 jam × Rp25.000                          = Rp1.050.000
Total biaya akuisisi = 380.000 + 220.000 + 300.000 + 1.050.000    = Rp1.950.000
CAC                  = Rp1.950.000 ÷ 12                            = Rp162.500   (versi tim Rp50.000)

Biaya dukungan       = (12 ÷ 60) jam × Rp25.000                    = Rp5.000 per pelanggan per bulan
Biaya langsung       = 1.500 + 14.000 + 5.000                      = Rp20.500
Margin kontribusi    = 35.000 − 20.500                             = Rp14.500 per bulan (41,4%)

LTV (10 bulan)       = 14.500 × 10 = Rp145.000   → LTV/CAC = 145.000 ÷ 162.500 = 0,89

Pegangan untuk D5 (tidak wajib dihitung):
LTV (7 bulan)        = 14.500 × 7  = Rp101.500   → LTV/CAC = 101.500 ÷ 162.500 = 0,62
```

**Arti:** rasio **di bawah 1** — setiap pelanggan baru merugikan sekitar Rp17.500 selama 10 bulan masa bertahannya; biaya memperoleh pelanggan tidak pernah kembali, dan ekspansi justru memperbesar kerugian. **Pengaruh D5:** asumsi 10 bulan pun belum didukung data; laju berhenti pada uji coba menyiratkan ±7 bulan, sehingga LTV lebih kecil dan kerugian per pelanggan lebih besar (±Rp61.000; rasio ±0,62) — kesimpulan "tidak layak ekspansi" makin kuat. Pernyataan kualitatif ini sudah cukup; hitungan 7 bulan tidak dituntut. Angka "3,9" pada D6 muncul karena waktu tim (±54% biaya akuisisi), voucer, dan dukungan manual tidak dihitung.

*Varian voucer.* Voucer boleh **dikeluarkan dari CAC hanya bila dibebankan di tempat lain** — mis. sebagai biaya layanan bulan pertama atau pengurang LTV, Rp300.000 ÷ 12 = **Rp25.000 per pelanggan**:
```
CAC tanpa voucer   = (380.000 + 220.000 + 1.050.000) ÷ 12          = Rp137.500
LTV (10 bulan)     = 145.000 − 25.000 = Rp120.000  → rasio 0,87
LTV (7 bulan)      = 101.500 − 25.000 = Rp76.500   → rasio 0,56   (tidak wajib)
```
Kesimpulannya sama (rugi per pelanggan; biaya akuisisi + voucer baru pulih setelah ±11,2 bulan > masa bertahan) → **dinilai penuh**. Bila voucer **hilang dari analisis sama sekali** (CAC Rp137.500 tanpa membebankan voucer di mana pun; rasio tampak 1,05), poin voucer dan poin nilai CAC = **0** (langkah CAC tidak lengkap); LTV/rasio tetap dinilai dengan kaidah kesalahan bawaan, tetapi tafsiran "bertahan hidup/impas" pada 10 bulan tidak mendapat poin arti karena bertumpu pada komponen yang dihapus.

**(c) Revisi asumsi dan keputusan:**
- **Asumsi tim yang terbantah** (≥ 2): proporsi membayar 75% → 18,75% (D2); jangkauan 1.200 → 960 (D1); CAC Rp50.000 → Rp162.500 (waktu tim dan voucer); margin Rp19.500 → Rp14.500 (dukungan manual); masa bertahan 10 → ±7 bulan (D5); LTV/CAC 3,9 → 0,89 (lebih rendah lagi bila bertahan ±7 bulan).
- **Keputusan yang paling konsisten: UBAH** — jangan ekspansi; ubah saluran, isi paket, atau harga sebelum menambah wilayah. Alasannya: rasio di bawah 1 berarti setiap pelanggan baru merugi, dan masa bertahan nyata (±7 bulan, D5) membuatnya lebih buruk. **HENTIKAN** juga konsisten bila diargumentasikan bahwa rasio < 1 pada kedua masa bertahan dan ruang perbaikannya sempit (agar rasio = 3 pada 10 bulan, CAC harus ≤ Rp48.333; pada 7 bulan ≤ Rp33.833). **LANJUT EKSPANSI tidak konsisten** dengan hasil (a)–(b).

*Pengayaan — langkah sesudah keputusan (tidak diminta pada latihan ini dan tidak dinilai).* Keputusan "ubah" sebaiknya diikuti uji berikutnya yang kriteria keberhasilannya ditetapkan **sebelum** uji dimulai ([Bab 6 §6.3.3](../06-buku-ajar/bab-06-kelayakan-teknologi-dan-operasional.md#633-merancang-uji-termurah)). Contoh: *uji saluran rujukan selama 3 minggu di 4 pangkalan — ketua pangkalan memperkenalkan layanan pada pertemuan pangkalan, insentif Rp10.000 per pelanggan baru, kehadiran tim maksimal 2 jam-orang per pangkalan.* **Kriteria:** ≥ 8 pelanggan baru berbayar dengan CAC ≤ Rp45.000 (termasuk nilai waktu tim, insentif, dan transport) **dan** ≥ 8 dari 9 pelanggan lama masih aktif pada akhir minggu ke-3; bila tidak tercapai → hentikan atau ubah segmen.
*Dasar ambang:* CAC ≤ Rp45.000 memberi LTV/CAC ±3,2 bila bertahan 10 bulan, tetapi baru ±2,3 bila bertahan ±7 bulan. Kriteria kedua **tidak dapat memastikan** masa bertahan: dengan 9 pelanggan dan jendela 3 minggu, peluang lolosnya ±0,8 bila masa bertahan ±7 bulan dan ±0,9 bila 10 bulan (§6) — perbedaan 7 dan 10 bulan (laju berhenti ±14% vs 10% per bulan) baru terbaca dari pengamatan bulanan selama ≥ 3 bulan pada lebih banyak pelanggan. Karena itu **lolos uji ini membenarkan uji yang lebih besar, belum ekspansi**. Rancangan ini dapat mencapai ambangnya: 8 jam-orang × Rp25.000 + 8 × Rp10.000 = Rp280.000, atau Rp35.000 per pelanggan sebelum transport — masih ≤ Rp45.000 bila transport seluruh uji ≤ Rp80.000. Uji lain yang sah: mewawancarai 3 pelanggan yang berhenti (mengapa); menawarkan paket tanpa subsidi cek ringan dengan harga lebih rendah; meminta pembayaran 3 bulan di muka sebagai uji komitmen.

#### Pedoman skor

| Sub | Maks | Rincian |
|-----|:----:|---------|
| (a) | 4 | Kapasitas 960 dengan langkah = 1. Proporsi 3/16 dipakai = 0,5. SOM akhir dengan langkah = 0,5 (kesalahan bawaan berlaku). Alasan dua pengali yang diganti (10%: tanpa dasar kapasitas; 75%: "mau" ≠ membayar) = 0,5 masing-masing. Satu pengali lain yang bermasalah dengan alasan (60.000, 20%, **atau × 12 bulan**) = 1. *Varian:* hanya proporsi dikoreksi (1.200 × 3/16 = 225 → Rp94.500.000) atau hanya kapasitas dikoreksi (960 × 75% = 720 → Rp302.400.000) → bagian yang benar tetap dinilai. SOM yang disesuaikan untuk akuisisi bertahap/churn → K1–K4 (penuh bila konsisten) |
| (b) | 5 | **Langkah CAC = 1,5:** waktu tim dinilai dengan upah pembanding dan dimasukkan = 0,5; voucer dimasukkan — **atau** dibebankan sebagai biaya layanan/pengurang LTV dengan alasan — = 0,5; nilai CAC = 0,5. **Langkah margin = 1:** biaya dukungan = 0,5; margin kontribusi = 0,5. CAC dan margin dinilai **pada nilainya**: CAC yang dihitung dari komponen tidak lengkap, atau margin tanpa dukungan, mendapat 0 untuk nilai itu, karena kelengkapan komponen adalah bagian dari langkah tersebut — kesalahannya dikurangi sekali, di langkah CAC atau margin. **Kesalahan bawaan berlaku mulai LTV/rasio:** LTV dan rasio pada 10 bulan = 1. Arti (rasio < 1 → rugi per pelanggan, tidak layak ekspansi) = 1 (0,5 bila hanya "belum sehat", atau bila arti konsisten dengan angkanya sendiri yang keliru). Pengaruh D5 — masa bertahan ±7 bulan menurunkan LTV sehingga rasio lebih rendah/kerugian lebih besar, dengan atau tanpa hitungan = 0,5 |
| (c) | 3 | ≥ 2 asumsi tim yang terbantah, dengan angka lama → baru = 1,5 (satu asumsi = 0,5). Keputusan konsisten dengan hasil (a)–(b), dengan alasan = 1,5 (keputusan tanpa alasan = 0,5; "lanjut ekspansi" = 0, juga bila bertumpu pada angka keliru, karena mengabaikan bukti D2 dan D5). Uji berikutnya tidak diminta dan tidak menambah skor |

Kesalahan bawaan berlaku: angka keliru di (a), atau CAC/margin keliru di (b), yang dipakai dengan benar pada langkah berikutnya tidak dikurangi lagi. Pada (c) kesalahan bawaan tidak membenarkan keputusan yang bertentangan dengan bukti eksplisit dalam soal.

#### Contoh jawaban

| Tingkat | Jawaban (ringkas) | Skor |
|---------|-------------------|:----:|
| Kurang | (a) "Angka AI tidak valid. SOM = 900 × 420.000 = Rp378 juta." (b) "CAC = 600.000 ÷ 12 = Rp50.000; LTV = 19.500 × 10 = Rp195.000; rasio 3,9 → sehat; kalau bertahan 7 bulan (D5) rasionya turun ke 2,73." (c) "Lanjut ekspansi karena rasio > 3." | 1 + 2 + 0 = **3** |
| Cukup | (a) "960 × 3/16 = 180 → Rp75,6 juta; 10% diganti kapasitas D1, 75% diganti yang pernah membayar D2." (b) CAC Rp162.500; margin Rp19.500 (dukungan tidak dihitung); LTV Rp195.000, rasio 1,2 → "belum sehat"; "dengan 7 bulan (D5) rasionya 0,84, makin buruk". (c) "Ubah: 75% → 19%, CAC 50 ribu → 162,5 ribu." | 3 + 3,5 + 2 = **8,5** *((a) tanpa pengali lain; (b) langkah margin tanpa dukungan (0), arti hanya "belum sehat"; (c) dua asumsi terbantah (1,5), keputusan tanpa alasan (0,5))* |
| Baik | Seperti kunci: SOM Rp75,6 juta dengan alasan penggantian + "60.000 dari AI" (atau "× 12 abaikan churn"); CAC Rp162.500; margin Rp14.500; rasio 0,89 → rugi per pelanggan, makin rugi bila bertahan ±7 bulan (D5); asumsi terbantah "bayar 75% → 18,75%, CAC Rp50.000 → Rp162.500, LTV/CAC 3,9 → 0,89" dan keputusan "ubah, jangan ekspansi, karena setiap pelanggan baru merugi". | **12** |

> **Cara membaca contoh "Kurang".** (a) satu pengali lain yang bermasalah dikenali dengan alasan (1); SOM tidak dihitung ulang. (b) langkah CAC memakai komponen versi tim — tanpa waktu tim dan voucer — sehingga 0 (0 + 0 + 0, dinilai pada nilainya); langkah margin tanpa dukungan, 0. LTV/rasio 10 bulan dihitung benar dari angka itu (1, kesalahan bawaan), dibaca sesuai angkanya (0,5), dan pengaruh D5 dikenali (0,5). (c) "lanjut ekspansi" mengabaikan bukti eksplisit D2 dan D5 — melanggar K4 — sehingga 0, **termasuk** bila didasarkan pada angka yang keliru. Bila contoh dan rincian pedoman berbeda, yang dipakai rincian pedoman.

#### Kesalahan umum

- Menghitung CAC hanya dari uang yang keluar (bensin, parkir, stiker, brosur) → Rp50.000. **Waktu tim** (±54% biaya akuisisi) dan **voucer** adalah biaya memperoleh pelanggan.
- Lupa mengubah menit ke jam: dukungan 12 menit = 0,2 jam → Rp5.000, bukan 12 × Rp25.000.
- Memakai 75% ("mau") sebagai proporsi membayar — pendapat tentang masa depan bukan perilaku membayar.
- Menerima angka 60.000 karena "dari AI" tanpa mempersoalkan sumbernya — angka tanpa rujukan tidak boleh menjadi dasar perhitungan.
- Pada (c), menulis keputusan tanpa alasan dari angka (a)–(b), atau menyebut "asumsi terbantah" tanpa angka lama → baru.

*Pelajari ulang:* [Bab 5 §5.2 (menghitung dari bawah)](../06-buku-ajar/bab-05-ukuran-pasar-dan-kompetitor.md#52-menghitung-dari-bawah) · [Bab 7 §7.2.1 (CAC yang jujur)](../06-buku-ajar/bab-07-unit-economics-harga-risiko.md#721-menghitungnya-dengan-jujur) · [Bab 7 §7.3.2 (rasio LTV/CAC)](../06-buku-ajar/bab-07-unit-economics-harga-risiko.md#732-rasio-ltvcac) · [Bab 7 §7.3.3 (memperbaiki rasio)](../06-buku-ajar/bab-07-unit-economics-harga-risiko.md#733-memperbaiki-rasio) · [Bab 6 §6.3.3 (uji termurah, pengayaan)](../06-buku-ajar/bab-06-kelayakan-teknologi-dan-operasional.md#633-merancang-uji-termurah)

---

## 4. Bagian C — Perancangan (20 poin)

### C1 [20] · C4–C6 · `TEKNO-Sub-CPMK091-1`

#### Logika butir

Dugaan tim adalah dugaan **sebab**: pemesanan ganda terjadi karena **jumlah penerima** pesanan, bukan karena **jumlah jalur**. Temuan awal belum dapat membedakan keduanya — H01 (dua penerima, ada pemindahan tamu) cocok dengan dugaan, tetapi juga cocok dengan "banyak jalur"; H02 (satu penerima, empat jalur, tidak pernah salah) cocok dengan dugaan; H03 (dua penerima, belum pernah memindahkan tamu) sedikit melemahkannya. Dugaan hanya **dapat terbantah** oleh kasus pembanding:
- **satu penerima, banyak jalur, tetapi tetap terjadi pemesanan ganda** → yang berperan jalur, bukan jumlah penerima; atau
- **beberapa penerima, tetapi tidak pernah terjadi pemesanan ganda** (seperti H03) → penerima ganda bukan penyebab yang cukup; atau
- pemesanan ganda karena **sebab lain** (mis. situs pemesanan daring mengonfirmasi otomatis tanpa dicek).

Bab 2 §2.3.3: satu temuan yang membantah dugaan adalah alasan untuk **mengubah pertanyaan pada wawancara berikutnya**; Modul 2: bila semua wawancara mengonfirmasi dugaan, kemungkinan besar pertanyaannya yang memimpin.

#### Rubrik analitik

| Komponen | Maks | Penuh | Sebagian | Rendah |
|----------|:----:|-------|----------|--------|
| **(a)** Narasumber yang dapat membantah dugaan | 5 | **Kriteria 2,5** — kasus pembanding (lihat "Logika butir"), dikaitkan dengan temuan H01–H03. **Alasan 1,5** — mengapa kasus itu menguji dugaan (hasilnya dapat menunjukkan dugaan salah). **Cara 1** — satu cara konkret menemuinya minggu ini (mis. rujukan dari H02/H03 atau pengelola desa wisata; daftar homestay di situs pemesanan daring atau papan informasi desa; datang langsung akhir pekan) | Kriteria **1,5**: kasus pembanding tanpa kaitan dengan temuan. Alasan **0,5**: kurang jelas. Cara **0,5**: generik ("lewat internet", "datang langsung" tanpa tujuan) | Kriteria **0,5**: hanya mencari pengelola yang "pernah mengalami pemesanan ganda" atau "punya banyak penerima" tanpa alasan pembanding — itu mencari pembenaran. **0**: tidak ada |
| **(b)** Empat pertanyaan inti | 9 | **Per pertanyaan (maks 4): 1,5** — tentang peristiwa yang sudah terjadi dan terbuka (1) serta tidak memimpin dan tidak menyebut dugaan/"pemesanan ganda"/solusi (0,5). **Cakupan 3** — aspek yang tercakup: penerima dan jalur; di mana dan sedang apa penerima (konteks penggunaan); pencatatan dan penerusan; kali terakhir tamu dipindahkan/dibatalkan. 4 aspek = 3; 3 aspek = 2; 2 aspek = 1; 1 aspek = 0,5 | Pertanyaan tentang kebiasaan umum ("biasanya siapa yang…") atau berbentuk ya/tidak ("pernah ada tamu yang dipindahkan?") **0,5 + 0,5**. Pertanyaan terbuka tentang peristiwa yang **menyiratkan** dugaan (mis. "Ceritakan kali terakhir ada tamu yang kamarnya ternyata sudah terisi.") **1 + 0** | Pertanyaan yang menyebut dugaan langsung, hipotetis ("kalau ada…, mau?"), atau menawarkan solusi: **0** untuk pertanyaan itu |
| **(c)** Jawaban pendukung vs pelemah (**satu** pertanyaan) | 6 | Jawaban **pendukung** yang terkait jumlah penerima atau jalur — mis. beberapa orang menerima pesanan untuk kamar yang sama lewat jalur masing-masing (**2,5**). Jawaban **pelemah** yang **benar-benar melemahkan dugaan sebab** — satu penerima tetapi tetap ganda; banyak penerima tetapi tidak pernah ganda; sebab lain (**3,5**). Kedua sisi dinilai dengan syarat yang sama: harus **membedakan kedua sebab** (jumlah penerima vs jumlah jalur) | Pendukung yang hanya menunjukkan bahwa masalah ada (mis. "ya, sering") tanpa kaitan dengan penerima atau jalur: pendukung **0,5**. Pelemah yang sekadar "tidak pernah ada masalah" tanpa keterangan jumlah penerima: pelemah **0,5** | **0**: tidak ada, atau jawaban "pendukung" justru melemahkan / jawaban "pelemah" justru cocok dengan dugaan. Bila dua pertanyaan dijawab, dinilai yang lebih baik |

**Konsistensi:** pertanyaan yang berbeda dari contoh kunci dinilai dari sifatnya (peristiwa nyata, terbuka, tidak memimpin), bukan dari kemiripan kata. Pada (c), jawaban yang dipilih harus cocok dengan pertanyaan yang ditulis di (b); kesalahan pada (b) tidak dikurangi lagi di (c). Pembuka tidak diminta; pembuka yang tetap ditulis tidak dinilai, kecuali ia menyebut dugaan tim — maka pertanyaan (b) yang menyusul dinilai seolah memimpin (bagian "tidak memimpin" = 0).

#### Contoh unsur kunci

- **(a):** *"Pengelola yang menerima sendiri semua pesanan dari tiga jalur atau lebih, termasuk situs pemesanan daring — seperti H02, tetapi lebih ramai. Bila di rumah seperti itu tetap pernah ada tamu yang dipindahkan, penyebabnya bukan banyaknya penerima, dan dugaan kami salah. Cara: minta H02 atau pengelola desa wisata menyebutkan homestay yang terdaftar di situs pemesanan daring, lalu datang Sabtu ini."*
- **(b) Pertanyaan inti (contoh):**
  1. "Coba ceritakan pesanan terakhir yang masuk: siapa yang menerimanya, lewat apa, dan apa yang dilakukan sesudahnya?" *(penerima dan jalur)*
  2. "Waktu pesanan itu masuk, Bapak/Ibu sedang di mana dan sedang mengerjakan apa?" *(konteks penggunaan)*
  3. "Setelah pesanan itu diterima, bagaimana anggota keluarga yang lain tahu kamar itu sudah terisi? Boleh saya lihat catatannya?" *(pencatatan dan penerusan)*
  4. "Kapan terakhir kali Bapak/Ibu harus memindahkan atau membatalkan tamu? Ceritakan dari awal." *(peristiwa terakhir — mengungkap pemesanan ganda tanpa menyebutnya)*
- **(c) Contoh** (cukup **satu** pertanyaan):
  - Pertanyaan 3 — *mendukung:* "Kalau suami yang terima, ditulis di bukunya sendiri; saya baru tahu kalau tamunya datang." *Melemahkan:* "Siapa pun yang menerima langsung menulis di buku yang sama di meja depan, dan selama ini tidak pernah salah kamar walaupun yang menerima bertiga."
  - Pertanyaan 4 — *mendukung:* "Waktu itu anak saya terima WhatsApp, saya terima telepon, untuk kamar yang sama." *Melemahkan:* "Saya sendiri yang menerima semuanya; tamu dari situs daring ternyata masuk ke kamar yang sudah saya janjikan lewat WhatsApp" (satu penerima, banyak jalur) — atau "tamunya batal sendiri; kamarnya bocor" (sebab lain).

#### Contoh jawaban

| Tingkat | Ringkasan jawaban | Skor |
|---------|------------------|:----:|
| **Kurang** | (a) "Pengelola yang sering mengalami pemesanan ganda; cari di internet." (b) "Apakah Ibu sering mengalami pemesanan ganda?", "Biasanya siapa yang menerima pesanan?", "Kalau ada aplikasi yang menggabungkan semua pesanan, Ibu mau pakai?", "Berapa kerugian Ibu kalau tamu dipindah?" (c) Pertanyaan 1: mendukung "ya, sering"; melemahkan "tidak pernah". | (a) 0,5 + 0 + 0,5 · (b) 0 + 1 + 0 + 1 + cakupan 1 · (c) 0,5 + 0,5 = **5** *((b) dua aspek tercakup — penerima, tamu dipindah; (c) kedua sisi tidak membedakan kedua sebab)* |
| **Cukup** | (a) "Pengelola yang menerima sendiri pesanan dari banyak jalur, sebagai pembanding"; akses "datang langsung". (b) Pertanyaan 1 dan 4 seperti kunci; "Biasanya siapa yang menerima pesanan?"; "Ceritakan kali terakhir ada tamu yang kamarnya ternyata sudah terisi."; aspek "di mana dan sedang apa" tidak tercakup. (c) Pertanyaan 1: mendukung "suami terima telepon, saya terima WA, untuk kamar yang sama"; melemahkan "tidak pernah ada masalah". | (a) 1,5 + 0,5 + 0,5 · (b) 1,5 + 1,5 + 1 + 1 + cakupan 2 · (c) 2,5 + 0,5 = **12,5** |
| **Baik** | Seperti contoh unsur kunci: kasus pembanding dengan alasan dan cara konkret; empat pertanyaan peristiwa yang mencakup keempat aspek; satu pasang jawaban pendukung/pelemah yang membedakan kedua sebab. | **20** |

#### Kesalahan umum

- Mencari narasumber yang "pernah mengalami pemesanan ganda" saja — itu mencari pembenaran, bukan kasus yang dapat membantah dugaan.
- Pertanyaan yang menyebut "pemesanan ganda", menyiratkan dugaan ("ceritakan kali terakhir kamarnya ternyata sudah terisi"), berbentuk ya/tidak ("pernah ada tamu yang dipindahkan?"), atau hipotetis ("kalau ada aplikasi…, mau?").
- Pertanyaan kebiasaan umum ("biasanya…") alih-alih peristiwa terakhir ("ceritakan pesanan terakhir…").
- Jawaban pendukung dan pelemah yang hanya "ya, sering" / "tidak pernah" — keduanya tidak membedakan **jumlah penerima** dari **jumlah jalur**, padahal itulah yang diuji.

*Pelajari ulang:* [Bab 2 §2.2.3 (pertanyaan inti)](../06-buku-ajar/bab-02-penemuan-masalah-dan-pelanggan.md#223-pertanyaan-inti-yang-selalu-dipakai) · [Bab 2 §2.3.3 (ketika dugaan terbantah)](../06-buku-ajar/bab-02-penemuan-masalah-dan-pelanggan.md#233-ketika-dugaan-terbantah) · [Modul Minggu 2](../03-modules/week-02-penemuan-masalah-dan-pelanggan.md)

---

## 5. Rekap Skor dan Diagnosis Diri

Salin tabel ini, isi skor Anda per butir, lalu hitung capaian (skor ÷ maks × 100%). Butir dengan capaian di bawah ±70% adalah prioritas belajar sebelum UTS.

| Butir | Sub-CPMK (sementara) | Bloom | Maks | Skor Anda | Bila capaian rendah, pelajari ulang |
|:-----:|----------------------|:-----:|:----:|:---------:|-------------------------------------|
| A1 | UAI32-1 | C3–C5 | 9 | | Bab 1 — ranah vs solusi, penyebab kegagalan |
| A2 | 091-1 | C4 | 6 | | Modul 3 §3.1.3 — berapa persona |
| A3 | 091-1 | C4–C5 | 6 | | Modul 3 §3.4 — konteks penggunaan |
| A4 | 091-1 | C4 | 6 | | Modul 4 §4.2 — *constraint* keras dan lunak |
| A5 | UAI21-1 | C5 | 3 | | Bab 6 §6.3.1 — mengurutkan asumsi |
| B1 | 091-1 | C4 | 13 | | Bab 2 §2.2–§2.5 — wawancara; Bab 4 §4.2.1 — persyaratan terukur |
| B2 | 091-1 | C4–C5 | 13 | | Bab 3 §3.1–§3.3 — persona, *job*, titik nyeri |
| B3 | 091-1 | C4–C5 | 12 | | Bab 4 §4.3–§4.4 — Kano, ketertelusuran |
| B4 | UAI21-1 (a–b) · UAI32-1 (c) | C4–C5 | 12 | | Bab 5 §5.2; Bab 7 §7.2–§7.3; Bab 6 §6.3.3 |
| C1 | 091-1 | C4–C6 | 20 | | Bab 2 §2.2.3 dan §2.3.3 — pertanyaan peristiwa, menguji dugaan |
| **Jumlah** | | | **100** | | |

| Sub-CPMK (kode lengkap) | Butir / sub-butir | Skor maks | Skor Anda | Capaian |
|-------------------------|-------------------|:---------:|:---------:|:-------:|
| `TEKNO-Sub-CPMK091-1` — penemuan pelanggan dan perumusan kebutuhan | A2, A3, A4, B1, B2, B3, C1 | 76 | | |
| `TEKNO-Sub-CPMKUAI21-1` — pasar, kelayakan, *unit economics* | A5, B4(a), B4(b) | 12 | | |
| `TEKNO-Sub-CPMKUAI32-1` — ranah, adaptasi keputusan setelah bukti | A1, B4(c) | 12 | | |
| **Jumlah** | | **100** | | |

> Penandaan Sub-CPMK di atas bersifat sementara (lihat §1.4) dan hanya membantu Anda membaca kekuatan dan kelemahan sendiri. Nilai UTS dihitung sebagai skor UTS × 10%.

---

## 6. Verifikasi Angka dengan Python

Seluruh angka B4 pada pembahasan ini dapat Anda periksa ulang. Salin kode berikut ke satu sel Google Colab (atau Python 3.8 ke atas) lalu jalankan; tidak diperlukan pustaka tambahan. *Pemeriksaan ini dilakukan sesudah latihan — selama UTS tidak ada perangkat selain kalkulator.*

```python
# Verifikasi angka butir B4 — Latihan UTS Teknopreneur
# Dapat dijalankan di Google Colab atau Python 3.8 ke atas; tanpa pustaka tambahan.

from math import comb

def rp(x):
    """Format rupiah gaya Indonesia (titik sebagai pemisah ribuan)."""
    teks = f"{abs(round(x)):,}".replace(",", ".")
    return ("−Rp" if x < 0 else "Rp") + teks

harga = 35_000                                  # harga langganan per bulan

# ---- (a) SOM: versi tim vs versi terkoreksi ----------------------------
pelanggan_tim = 60_000 * 0.20 * 0.10 * 0.75     # 900 pelanggan
som_tim = pelanggan_tim * harga * 12
jangkau = 3 * 4 * (60 / 30) * 40                # D1: 3 orang x 4 jam x 2 pengemudi/jam x 40 minggu
pelanggan = jangkau * 3 / 16                    # D2: hanya yang PERNAH membayar
som = pelanggan * harga * 12
print(f"SOM tim        : {pelanggan_tim:.0f} pelanggan -> {rp(som_tim)}")
print(f"SOM terkoreksi : {jangkau:.0f} x 3/16 = {pelanggan:.0f} pelanggan -> {rp(som)}")

# ---- (b) CAC, margin kontribusi, LTV, rasio -----------------------------
nilai_waktu = 42 * 25_000                       # 42 jam x upah pembanding
biaya_akuisisi = 380_000 + 220_000 + 300_000 + nilai_waktu
cac = biaya_akuisisi / 12
cac_tim = (380_000 + 220_000) / 12              # versi tim: tanpa waktu dan voucer
dukungan = (12 / 60) * 25_000                   # 12 menit per pelanggan per bulan
margin = harga - (1_500 + 14_000 + dukungan)
margin_tim = harga - (1_500 + 14_000)
print(f"CAC            : {rp(biaya_akuisisi)} / 12 = {rp(cac)} (versi tim {rp(cac_tim)})")
print(f"Margin         : {rp(margin)} per bulan ({margin / harga:.1%}); versi tim {rp(margin_tim)}")
for bulan in (10, 7):                           # asumsi tim vs laju berhenti pada uji coba (D5)
    ltv = margin * bulan
    print(f"LTV {bulan:>2} bulan   : {rp(ltv)} -> LTV/CAC = {ltv / cac:.2f}; "
          f"selisih per pelanggan {rp(ltv - cac)}")
print(f"Rasio versi tim: {margin_tim * 10 / cac_tim:.1f}")

# ---- (c) pegangan HENTIKAN: ambang CAC agar rasio = 3 -----------------
for bulan in (10, 7):
    print(f"CAC maksimum agar rasio 3 ({bulan} bulan): {rp(margin * bulan / 3)}")

# ---- (c) pengayaan: kriteria kedua uji berikutnya (>= 8 dari 9 aktif setelah 3 minggu)
# Laju berhenti bulanan dianggap tetap = 1 / rata-rata bulan bertahan;
# 3 minggu = 3 x 12/52 bulan. Peluang lolos = P(8 atau 9 dari 9 bertahan).
lolos = {}
for bulan in (10, 7):
    p = (1 - 1 / bulan) ** (3 * 12 / 52)        # peluang satu pelanggan bertahan 3 minggu
    lolos[bulan] = sum(comb(9, j) * p**j * (1 - p)**(9 - j) for j in (8, 9))
    print(f"Peluang lolos kriteria kedua ({bulan} bulan): {lolos[bulan]:.2f}")

# Pemeriksaan otomatis: bila salah satu angka berubah, assert akan gagal
assert (jangkau, pelanggan, som) == (960, 180, 75_600_000)
assert (cac, margin) == (162_500, 14_500)
assert round(margin * 10 / cac, 2) == 0.89 and round(margin * 7 / cac, 2) == 0.62
assert round(lolos[10], 1) == 0.9 and round(lolos[7], 1) == 0.8   # hampir sama: kriteria tidak membedakan
print("Semua angka cocok dengan pembahasan.")
```

Keluaran yang diharapkan (Python memakai titik desimal):

```
SOM tim        : 900 pelanggan -> Rp378.000.000
SOM terkoreksi : 960 x 3/16 = 180 pelanggan -> Rp75.600.000
CAC            : Rp1.950.000 / 12 = Rp162.500 (versi tim Rp50.000)
Margin         : Rp14.500 per bulan (41.4%); versi tim Rp19.500
LTV 10 bulan   : Rp145.000 -> LTV/CAC = 0.89; selisih per pelanggan −Rp17.500
LTV  7 bulan   : Rp101.500 -> LTV/CAC = 0.62; selisih per pelanggan −Rp61.000
Rasio versi tim: 3.9
CAC maksimum agar rasio 3 (10 bulan): Rp48.333
CAC maksimum agar rasio 3 (7 bulan): Rp33.833
Peluang lolos kriteria kedua (10 bulan): 0.87
Peluang lolos kriteria kedua (7 bulan): 0.77
Semua angka cocok dengan pembahasan.
```

---

## Dokumen Terkait

1. [Latihan UTS](latihan-uts.md)
2. [Cetak biru butir dan panduan varian](latihan-uts-cetak-biru.md) (untuk dosen)
3. [Kisi-kisi UTS](kisi-kisi-uts.md)
4. [Modul Minggu 8](../03-modules/week-08-uts-review-dan-ujian.md)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
