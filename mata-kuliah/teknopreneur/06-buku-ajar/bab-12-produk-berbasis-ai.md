# BAB 12: PRODUK BERBASIS AI — KELAYAKAN DAN BATASNYA

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `TEKNO-Sub-CPMKUAI21-1` | Mengevaluasi (C5) kelayakan sebuah usaha yang bersandar pada kecerdasan artifisial, termasuk menyimpulkan bahwa AI tidak diperlukan | C4–C5 |

Setelah membaca bab ini, pembaca diharapkan mampu:

1. **Membedakan** (C2) persoalan yang memerlukan AI dari yang tidak.
2. **Menganalisis** (C4) kebutuhan data, biaya, dan risiko sebuah usulan produk AI.
3. **Mengevaluasi** (C5) kelayakan ekonomi produk berbasis AI.
4. **Menilai** (C5) risiko etis dan tanggung jawab atas keluaran AI.
5. **Merumuskan** (C5) keputusan memakai atau tidak memakai AI beserta alasannya.

---

## 12.1 Kedudukan Bab Ini

Sepanjang buku ini, AI Corner membahas AI sebagai **alat kerja tim** dengan batas-batasnya. Bab ini berbeda: di sini AI menjadi **objek penilaian kelayakan usaha**.

| Peran AI | Di mana |
|----------|---------|
| Alat kerja tim, dengan batas | AI Corner setiap bab |
| **Objek yang dinilai kelayakannya** | **Bab ini** |

Pertanyaan bab ini bukan "bagaimana memakai AI", melainkan: **apakah usaha yang bersandar pada AI ini layak dijalankan?** — dan jawabannya sering kali tidak.

> Mata kuliah ini berstatus **mode E (Eksplisit)** pada AI Curriculum Infusion Matrix. Yang dinilai bukan kemampuan membangun sistem AI — itu urusan Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — melainkan kemampuan **menimbang kelayakan usaha yang bersandar padanya**. Keputusan yang beralasan untuk **tidak** memakai AI bernilai sama tingginya dengan keputusan memakainya.

---

## 12.2 Kapan AI Benar-Benar Diperlukan

### 12.2.1 Ujian Empat Pertanyaan

| Pertanyaan | Bila jawabannya "tidak" |
|------------|------------------------|
| 1. Apakah persoalannya memerlukan pengenalan pola yang tidak dapat dituliskan sebagai aturan? | Pakai aturan biasa |
| 2. Apakah data yang diperlukan tersedia dalam jumlah memadai? | Kumpulkan data dulu, atau batalkan |
| 3. Apakah kesalahan sesekali dapat ditoleransi? | AI bukan pilihan yang tepat |
| 4. Apakah nilai tambahnya melebihi biaya dan risikonya? | Pakai cara yang lebih sederhana |

Keempatnya harus dijawab "ya". Satu saja "tidak" cukup untuk menyimpulkan bahwa AI bukan jawaban yang tepat.

### 12.2.2 Menerapkannya pada Kasus Berjalan

Usulan: memperkirakan kebutuhan belanja harian warung dengan model pembelajaran mesin.

| Pertanyaan | Jawaban | Penjelasan |
|------------|---------|------------|
| 1. Perlu pengenalan pola? | **Sebagian** | Pola hari dalam seminggu dan cuaca dapat ditangkap aturan sederhana |
| 2. Data memadai? | **Tidak** | 14 hari data per warung; model menuntut ratusan hari |
| 3. Kesalahan dapat ditoleransi? | Ya | Perkiraan meleset berarti belanja kurang tepat, bukan bencana |
| 4. Nilai > biaya? | **Tidak** | Rata-rata bergerak 7 hari sudah memberi sebagian besar manfaat |

**Kesimpulan: AI tidak diperlukan pada tahap ini.**

Perbandingan langsung:

| Pendekatan | Ketelitian (uji 14 hari, 5 warung) | Waktu membangun | Biaya jalan | Dapat dijelaskan kepada pengguna |
|------------|-----------------------------------|-----------------|-------------|--------------------------------|
| Rata-rata 7 hari terakhir | Galat rata-rata 23% | 2 jam | Rp0 | Ya, dalam satu kalimat |
| Rata-rata + koreksi hari | Galat rata-rata 18% | 6 jam | Rp0 | Ya |
| Model pembelajaran mesin | **Tidak dapat dilatih** | — | — | Tidak |

Baris ketiga adalah temuan yang jujur: dengan 70 baris data (5 warung × 14 hari), tidak ada model yang dapat dilatih secara bermakna. Menyatakan hal ini dalam laporan jauh lebih bernilai daripada memaksakan model yang dilatih pada data yang tidak memadai dan melaporkan ketelitian yang menyesatkan.

> Kapan AI menjadi masuk akal pada kasus ini? Ketika data sudah terkumpul selama satu tahun dari 100 warung — sekitar 36.500 baris — dan ketika selisih ketelitian antara aturan sederhana dan model terbukti cukup besar untuk membenarkan biayanya. Keduanya adalah keadaan yang dapat dituliskan sebagai syarat, dan itulah bentuk keputusan yang beralasan.

### 12.2.3 Persoalan yang Memang Memerlukan AI

| Persoalan | Mengapa aturan tidak cukup |
|-----------|---------------------------|
| Membaca tulisan tangan pada nota belanja | Variasi tulisan tak terbatas |
| Mengelompokkan keluhan pelanggan dari teks bebas | Ungkapan terlalu beragam |
| Mengenali jenis bahan dari foto | Ragam visual sangat besar |
| Memperkirakan permintaan dengan banyak faktor sekaligus | Interaksi antarfaktor rumit — **bila datanya ada** |

Baris terakhir menegaskan syarat yang sama: kemampuan teknis tidak menggantikan ketersediaan data.

---

## 12.3 Menilai Kelayakan Usaha Berbasis AI

### 12.3.1 Kebutuhan Data

| Pertanyaan | Mengapa menentukan |
|------------|-------------------|
| Dari mana data berasal? | Data yang harus dibeli mengubah seluruh perhitungan biaya |
| Siapa pemiliknya? | Data pengguna bukan milik tim |
| Bolehkah dipakai untuk melatih? | Memerlukan dasar pemrosesan yang sah |
| Berapa banyak yang diperlukan? | Sering jauh lebih besar dari dugaan |
| Berapa lama mengumpulkannya? | Sering melampaui satu semester |
| Apa yang terjadi bila datanya bias? | Keluaran meneruskan biasnya |

Pertanyaan ketiga sering terlewat dan berakibat serius. Data transaksi pedagang yang dikumpulkan untuk **memberi perkiraan belanja** tidak otomatis boleh dipakai untuk **melatih model yang dijual kepada pihak lain**. Tujuan pemrosesan yang berubah menuntut persetujuan baru; memakainya tanpa itu melanggar asas pembatasan tujuan pada UU PDP sekaligus merupakan bentuk `tadlis`.

### 12.3.2 Biaya yang Sering Terlewat

| Biaya | Sering diabaikan karena |
|-------|------------------------|
| Pemanggilan model per pengguna | Terlihat kecil per satuan, besar dalam jumlah |
| Pengumpulan dan pelabelan data | Dianggap pekerjaan sekali |
| Pemeliharaan saat mutu menurun | Tidak terlihat sampai terjadi |
| Penanganan keluaran yang salah | Butuh manusia |
| Biaya naik seiring pemakaian | Struktur biaya berbeda dari perangkat lunak biasa |

Baris terakhir adalah perbedaan mendasar. Perangkat lunak biasa memiliki biaya variabel per pengguna yang mendekati nol; produk yang memanggil model bahasa memiliki biaya yang tumbuh sebanding pemakaian.

```
Contoh perhitungan:
  Harga langganan        : Rp25.000/pengguna/bulan
  Pemanggilan model      : 30 kali/pengguna/bulan
  Biaya per pemanggilan  : Rp400
  Biaya model            : Rp12.000/pengguna/bulan
  Biaya lain             : Rp3.000/pengguna/bulan
  ──────────────────────────────────────────────
  Margin kontribusi      : Rp10.000 (40%)
```

Bandingkan dengan margin 88% pada pendekatan tanpa AI (§7.3.1). Selisih 48 poin persen itu harus dibayar oleh nilai tambah yang nyata bagi pengguna — dan bila nilai tambahnya tidak terasa, yang terjadi adalah margin yang tergerus tanpa alasan.

### 12.3.3 Ketika Biaya Model Melebihi Harga

| Keadaan | Tindakan |
|---------|----------|
| Biaya model > harga langganan | Model tidak layak; ganti pendekatan |
| Margin < 30% | Periksa apakah nilai tambahnya sebanding |
| Pemakaian tak terduga besar | Batasi pemanggilan per pengguna |
| Pengguna berat merugikan | Tetapkan batas wajar, nyatakan di muka |

Baris terakhir menuntut kehati-hatian etis. Membatasi pemakaian itu sah; **membatasinya tanpa menyatakannya di muka** adalah `gharar`.

---

## 12.4 Risiko Khas Produk AI

### 12.4.1 Keluaran yang Salah dengan Meyakinkan

Ini adalah risiko yang paling khas dan paling berbahaya. Sistem berbasis aturan yang gagal biasanya gagal dengan jelas; sistem berbasis model sering menghasilkan jawaban yang **salah tetapi terdengar benar**.

| Bidang | Akibat keluaran salah |
|--------|----------------------|
| Perkiraan belanja | Pedagang rugi karena membeli terlalu banyak |
| Saran kesehatan | Bahaya langsung bagi orang |
| Perhitungan keuangan | Kerugian uang |
| Informasi hukum | Keputusan yang merugikan |

| Mitigasi | Bentuknya |
|----------|-----------|
| Tampilkan rentang, bukan angka tunggal | "Perkiraan 8–11 kg" |
| Nyatakan tingkat keyakinan | "Perkiraan ini kurang andal untuk hari Jumat" |
| Sediakan jalan memeriksa | Tampilkan data yang mendasarinya |
| Manusia memutuskan | Sistem menyarankan, pengguna memutuskan |
| Nyatakan keterbatasan sejak awal | Bagian dari pemberitahuan pendaftaran |

Baris keempat adalah prinsip yang paling penting dipegang untuk usaha tahap awal: **sistem menyarankan, manusia memutuskan**. Selama pengguna tetap memegang keputusan dan memahami bahwa yang ia terima adalah saran, tanggung jawabnya berbagi. Sistem yang mengambil keputusan atas nama pengguna memikul tanggung jawab yang jauh lebih berat.

### 12.4.2 Bias

| Sumber bias | Contoh |
|-------------|--------|
| Data dari satu kelompok saja | Model dilatih dari warung di satu kecamatan makmur |
| Data historis yang timpang | Pola masa lalu yang tidak adil dilanggengkan |
| Pelabelan yang bias | Pelabel memiliki kecenderungan tertentu |
| Perbedaan konteks | Model dilatih di kota, dipakai di desa |

Pertanyaan yang perlu dijawab untuk setiap produk AI: **bagi siapa sistem ini bekerja lebih buruk, dan apakah mereka tahu?**

### 12.4.3 Tanggung Jawab atas Keluaran

| Pertanyaan | Jawaban yang benar |
|------------|-------------------|
| Siapa bertanggung jawab bila keluaran merugikan? | **Penyedia layanan**, bukan penyedia model |
| Cukupkah menyatakan "ini hanya AI"? | Tidak |
| Cukupkah syarat dan ketentuan? | Tidak, bila pengguna tidak memahaminya |
| Apa yang harus ada? | Batas yang dinyatakan jelas, cara memeriksa, dan manusia yang memutuskan |

Baris pertama sering disalahpahami. Tim yang memanggil model dari penyedia lain tetap bertanggung jawab kepada penggunanya atas apa yang disampaikan layanannya. Rantai teknisnya tidak mengalihkan tanggung jawab itu.

---

## 12.5 Keputusan yang Tercatat

Hasil bab ini berupa satu dokumen keputusan, bukan satu produk.

```markdown
## Keputusan Pemakaian AI — 10 November 2026

Usulan     : Memperkirakan kebutuhan belanja harian
             dengan model pembelajaran mesin.

Ujian empat pertanyaan:
  1. Perlu pengenalan pola?     Sebagian — aturan sederhana cukup
  2. Data memadai?              TIDAK — 70 baris, perlu ribuan
  3. Kesalahan dapat ditoleransi? Ya
  4. Nilai > biaya?             TIDAK — margin 88% → 40%

KEPUTUSAN  : Tidak memakai AI pada tahap ini.
Pendekatan : Rata-rata bergerak 7 hari dengan koreksi hari
             dalam seminggu. Galat 18% pada uji 14 hari.

Kapan ditinjau ulang:
  - Setelah data terkumpul ≥1 tahun dari ≥100 warung, ATAU
  - Bila galat pendekatan sederhana terbukti >30% dan
    menjadi keluhan utama pengguna.

Yang dicatat untuk peninjauan:
  Galat harian per warung disimpan sejak hari pertama,
  agar perbandingan kelak memiliki dasar.
```

| Unsur | Mengapa penting |
|-------|-----------------|
| Ujian yang dijalankan | Menunjukkan keputusan beralasan |
| Keputusan yang tegas | Bukan "mungkin nanti" |
| Pendekatan pengganti | Persoalannya tetap diselesaikan |
| Syarat peninjauan | Keputusan dapat berubah bila keadaan berubah |
| Data yang dicatat | Peninjauan kelak punya dasar |

Dokumen semacam ini adalah yang dinilai pada Studio 13, dan bentuk paling langsung dari mode E: pemakaian AI dibahas terbuka, ditimbang dengan kriteria, dan diputuskan dengan alasan yang dapat diperiksa.

---

## AI Corner — Bab 12

### Bab Ini Adalah AI Corner-nya

Seluruh bab ini membahas AI sebagai objek penilaian. Bagian ini menambahkan satu hal: **batas pemakaian AI untuk menilai AI**.

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI menjelaskan kebutuhan data sebuah teknik | Meminta AI menilai apakah usaha tim layak memakai AI |
| Meminta AI menyebutkan risiko bias yang mungkin ada | Meminta AI menyatakan bahwa produk tim "aman dari bias" |
| Meminta AI memperkirakan struktur biaya pemanggilan | Menerima angka biaya tanpa memeriksa ke daftar harga penyedia |
| Meminta AI menyebutkan alternatif non-AI | Meminta AI memutuskan |

### Kecenderungan yang Perlu Diwaspadai

Ditanya apakah sebuah persoalan cocok diselesaikan dengan AI, model bahasa cenderung menjawab **ya**, dengan penjelasan yang meyakinkan tentang bagaimana pembelajaran mesin dapat diterapkan.

Kecenderungan ini wajar: teks yang membahas penerapan AI pada suatu bidang hampir seluruhnya ditulis oleh pihak yang ingin menerapkannya. Teks yang menyimpulkan "AI tidak diperlukan di sini" jarang ditulis dan jarang diterbitkan.

Karena itu, jawaban atas pertanyaan kelayakan tidak diambil dari model, melainkan dari **ujian empat pertanyaan §12.2.1 yang dijalankan atas data tim sendiri** — terutama pertanyaan kedua, yang hampir selalu menjadi penentu bagi proyek satu semester.

### Latihan Reflektif

Ajukan kepada asisten AI: *"Apakah perkiraan kebutuhan belanja warung makan cocok diselesaikan dengan machine learning?"*

Simpan jawabannya. Bandingkan dengan hasil ujian empat pertanyaan yang tim jalankan atas datanya sendiri. Jawab:

1. Apakah jawaban model menyebut kebutuhan jumlah data secara spesifik?
2. Apakah jawaban model menyebut kemungkinan bahwa AI tidak diperlukan?
3. Bila tim mengikuti jawaban itu, apa yang akan terjadi pada Minggu 15?

---

## Latihan Soal

### Tingkat Dasar

1. Sebutkan empat pertanyaan ujian kelayakan AI dan jelaskan mengapa keempatnya harus dijawab "ya".
2. Mengapa produk berbasis pemanggilan model memiliki struktur biaya yang berbeda dari perangkat lunak biasa?
3. Jelaskan risiko "keluaran salah dengan meyakinkan" dan sebutkan lima mitigasinya.
4. Siapa yang bertanggung jawab bila keluaran AI merugikan pengguna? Jelaskan.
5. Sebutkan empat sumber bias pada sistem berbasis data.

### Tingkat Menengah

6. Jalankan ujian empat pertanyaan pada tiga usulan berikut dan simpulkan masing-masing:
   - Mengelompokkan keluhan pelanggan dari pesan teks bebas
   - Menghitung total belanja bulanan dari catatan transaksi
   - Mengenali jenis sayuran dari foto untuk pencatatan otomatis

7. Hitung margin kontribusi untuk produk dengan harga Rp40.000/bulan, 80 pemanggilan model per pengguna per bulan pada Rp350 per pemanggilan, dan biaya lain Rp5.000/bulan. Tentukan apakah layak, dan bila tidak, sebutkan tiga cara memperbaikinya beserta pertukarannya.

8. Susun dokumen Keputusan Pemakaian AI (format §12.5) untuk proyek tim Anda, dengan keempat ujian dijawab berdasarkan data nyata tim.

9. Untuk satu produk AI yang Anda kenal, jawab: bagi siapa sistem ini kemungkinan bekerja lebih buruk, apa sebabnya, dan apakah kelompok itu diberi tahu? Usulkan satu perbaikan yang konkret.

### Tingkat Mahir

10. **Latihan pembanding.** Untuk persoalan tim Anda, bangun dua pendekatan: satu berbasis aturan sederhana, satu memanggil model. Ukur keduanya pada data yang sama: ketelitian, waktu membangun, biaya per pengguna per bulan, dan kemampuan menjelaskan hasil kepada pengguna. Simpulkan mana yang dipakai dan mengapa. Bila pendekatan sederhana menang, jelaskan apa artinya bagi rencana usaha.

11. Rancang mekanisme penanganan keluaran yang salah untuk produk Anda: bagaimana pengguna mengetahui keluaran itu mungkin salah, bagaimana ia memeriksanya, bagaimana ia melaporkannya, dan apa yang tim lakukan atas laporan itu. Kaitkan setiap bagian dengan prinsip `gharar` atau `tadlis`.

12. Sebuah tim menemukan bahwa memakai AI akan menurunkan margin dari 85% menjadi 35%, tetapi memperbaiki ketelitian perkiraan dari galat 23% menjadi 16%. Susun analisis lengkap: pada keadaan seperti apa pertukaran itu sepadan, apa yang harus diketahui dari pengguna untuk memutuskannya, dan bagaimana tim akan mengujinya sebelum berkomitmen. Rumuskan keputusan Anda beserta syarat peninjauan ulangnya.

---

## Rangkuman

| Gagasan pokok | Rumusan singkat |
|---------------|-----------------|
| Kedudukan bab | AI sebagai objek penilaian kelayakan, bukan sebagai alat |
| Ujian kelayakan | Empat pertanyaan; satu "tidak" sudah cukup untuk menolak |
| Penentu tersering | Ketersediaan data — hampir selalu menjadi penghalang di satu semester |
| Kesimpulan kasus berjalan | AI tidak diperlukan; rata-rata bergerak sudah memberi sebagian besar manfaat |
| Struktur biaya | Biaya tumbuh sebanding pemakaian, berbeda dari perangkat lunak biasa |
| Risiko khas | Keluaran salah yang terdengar benar |
| Prinsip mitigasi | Sistem menyarankan, manusia memutuskan |
| Tanggung jawab | Melekat pada penyedia layanan, tidak beralih ke penyedia model |
| Hasil bab ini | Dokumen keputusan beralasan, termasuk keputusan tidak memakai AI |
| Kecenderungan AI | Cenderung menjawab "ya, AI cocok" — karena itulah teks yang pernah dibacanya |

---

## Referensi

1. Ng, A. (2021). *AI Transformation Playbook*. Landing AI.
2. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media.
3. Sculley, D., et al. (2015). Hidden Technical Debt in Machine Learning Systems. *Advances in Neural Information Processing Systems*, 28.
4. Mitchell, M., et al. (2019). Model Cards for Model Reporting. *Proceedings of FAccT '19*, 220–229.
5. Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the Dangers of Stochastic Parrots. *Proceedings of FAccT '21*, 610–623.
6. Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and Machine Learning: Limitations and Opportunities*. MIT Press.
7. Republik Indonesia. (2022). *Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi*.
8. Kementerian Komunikasi dan Informatika. (2023). *Panduan Etika Kecerdasan Artifisial Indonesia*. Kominfo.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul mingguan | [Minggu 13 — Produk Berbasis AI](../03-modules/week-13-produk-berbasis-ai.md) |
| Studio | [Studio 13 — Kelayakan Produk AI](../04-labs/lab-13-kelayakan-produk-ai.md) |
| Mata kuliah terkait | [Dasar Kecerdasan Artifisial dan Pembelajaran Mesin](../../dasar-kecerdasan-artifisial-dan-pembelajaran-mesin/README.md) |
| Bab sebelumnya | [Bab 11 — Tata Kelola, Legalitas, dan Etika](bab-11-tata-kelola-legalitas-etika.md) |
| Bab berikutnya | [Bab 13 — *Pitching* dan Komunikasi Bisnis](bab-13-pitching-dan-komunikasi-bisnis.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
