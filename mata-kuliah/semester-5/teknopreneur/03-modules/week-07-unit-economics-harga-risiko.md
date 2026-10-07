# Minggu 7: *Unit Economics*, Harga, dan Risiko

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Teknopreneur (`ST52510002`) |
| Minggu | 7 dari 16 |
| Topik | CAC, LTV, margin, *payback*; strategi harga; daftar risiko |
| Sub-CPMK | `TEKNO-Sub-CPMKUAI21-1` |
| Bloom | C4 → C5 |
| Durasi | 150 menit |
| Metode | Kuliah · Studio perhitungan · Presentasi silang |
| Penilaian | Observasi (Studio 7) · **Milestone 2 (P-02)** |

---

## Tujuan Pembelajaran

1. **Menghitung** (C3) CAC, LTV, margin kotor, dan *payback period*.
2. **Mengevaluasi** (C5) kelayakan finansial berdasarkan *unit economics*.
3. **Menentukan** (C5) strategi harga berdasarkan nilai dan bukti.
4. **Menyusun** (C4) daftar risiko dengan kemungkinan, dampak, dan mitigasi.

---

## Materi Pembelajaran

### 7.1 Mengapa *Unit Economics*

Sebuah usaha dapat tumbuh pesat dan tetap **tidak pernah dapat menguntungkan**, bila setiap pelanggan baru justru menambah kerugian. *Unit economics* menjawab satu pertanyaan:

> **Apakah melayani satu pelanggan menghasilkan lebih banyak daripada biayanya?**

Bila jawabannya tidak, pertumbuhan **memperburuk keadaan** — dan tidak ada besaran pasar yang dapat memperbaikinya.

---

### 7.2 Empat Besaran Pokok

#### 7.2.1 CAC — *Customer Acquisition Cost*

$$\text{CAC} = \frac{\text{Total biaya pemasaran dan penjualan}}{\text{Jumlah pelanggan baru}}$$

| Komponen yang sering dilupakan | Contoh |
|--------------------------------|--------|
| Waktu tim | 20 jam/bulan × nilai waktu |
| Biaya konten | Pembuatan materi promosi |
| Diskon dan promo | Potongan harga untuk pengguna awal |
| Biaya *onboarding* | Waktu membantu pengguna baru mulai |

> CAC yang hanya menghitung biaya iklan adalah CAC yang terlalu rendah. Pada tahap awal, **waktu tim adalah komponen terbesar** — dan ia nyata, meski tidak dibayarkan.

#### 7.2.2 LTV — *Lifetime Value*

$$\text{LTV} = \text{ARPU} \times \text{Margin kotor} \times \text{Rata-rata lama berlangganan}$$

di mana ARPU = pendapatan rata-rata per pengguna per periode.

| Contoh | Nilai |
|--------|-------|
| ARPU | Rp 50.000/bulan |
| Margin kotor | 70% |
| Rata-rata lama berlangganan | 8 bulan |
| **LTV** | 50.000 × 0,70 × 8 = **Rp 280.000** |

#### 7.2.3 Margin Kotor

$$\text{Margin kotor} = \frac{\text{Pendapatan} - \text{Biaya langsung}}{\text{Pendapatan}} \times 100\%$$

| Biaya langsung mencakup | Tidak mencakup |
|-------------------------|----------------|
| Biaya server per pengguna | Gaji tim pengembang |
| Biaya API per pemakaian | Sewa kantor |
| Biaya transaksi pembayaran | Biaya pemasaran |
| **Biaya dukungan per pengguna** | Biaya administrasi umum |

Baris terakhir sering dilupakan pada usaha yang dukungannya masih manual — dan pada tahap awal, ia bisa menjadi komponen terbesar.

#### 7.2.4 *Payback Period*

$$\text{Payback} = \frac{\text{CAC}}{\text{ARPU} \times \text{Margin kotor}}$$

Berapa bulan sampai biaya memperoleh pelanggan kembali.

---

### 7.3 Membaca Hasilnya

| Rasio LTV/CAC | Tafsir |
|---------------|--------|
| < 1 | **Setiap pelanggan baru menambah kerugian** — pertumbuhan memperburuk |
| 1–2 | Marginal; tidak ada ruang untuk kesalahan |
| **3** | Sering dijadikan patokan sehat |
| > 5 | Mungkin kurang berinvestasi pada pertumbuhan |

| *Payback period* | Tafsir |
|------------------|--------|
| < 6 bulan | Sangat baik; modal berputar cepat |
| 6–12 bulan | Wajar |
| 12–18 bulan | Butuh modal kerja besar |
| > 18 bulan | Sulit dibiayai tanpa pendanaan besar |

> **Peringatan tentang patokan:** angka 3 untuk LTV/CAC adalah kebiasaan industri, bukan hukum. Pada usaha yang baru berjalan beberapa bulan, **rata-rata lama berlangganan belum dapat diketahui** — dan LTV yang dihitung darinya adalah dugaan. Menyatakan ketidakpastian itu lebih jujur daripada menyajikan angka yang tampak pasti.

---

### 7.4 Analisis Sensitivitas

Model *unit economics* dibangun di atas asumsi. Analisis sensitivitas menguji apa yang terjadi bila asumsi meleset.

| Asumsi | Nilai dasar | Pesimis (−50%) | Optimis (+50%) | Dampak pada LTV/CAC |
|--------|-------------|----------------|----------------|---------------------|
| Lama berlangganan | 8 bulan | 4 bulan | 12 bulan | 1,4 → **2,8** → 4,2 |
| Margin kotor | 70% | 35% | 85% | 1,4 → 2,8 → 3,4 |
| CAC | Rp 200.000 | Rp 100.000 | Rp 300.000 | 5,6 → 2,8 → 1,9 |

Kolom terakhir menunjukkan **asumsi mana yang paling menentukan**. Dalam contoh ini, lama berlangganan dan CAC sama-sama menentukan — dan keduanya adalah angka yang paling tidak pasti pada tahap awal.

> **Ketentuan mata kuliah ini:** analisis sensitivitas **wajib** pada minimal tiga asumsi utama. Model tanpa analisis sensitivitas menyajikan kepastian yang tidak dimilikinya.

---

### 7.5 Strategi Harga

#### 7.5.1 Tiga Dasar Penetapan Harga

| Dasar | Cara | Kelemahan |
|-------|------|-----------|
| **Berdasarkan biaya** | Biaya + margin | Mengabaikan nilai bagi pelanggan |
| **Berdasarkan kompetitor** | Sekitar harga pesaing | Mengabaikan pembeda kita |
| **Berdasarkan nilai** | Sebagian dari nilai yang diberikan | **Paling tepat**, paling sulit ditaksir |

#### 7.5.2 Menaksir Nilai dari Wawancara

Data untuk penetapan harga berbasis nilai berasal dari wawancara:

| Yang ditanyakan | Contoh jawaban | Yang diungkapnya |
|-----------------|----------------|------------------|
| "Berapa waktu yang habis untuk ini?" | "2 jam seminggu" | 8 jam/bulan |
| "Berapa kerugian yang timbul?" | "300–400 ribu sebulan" | Nilai masalah |
| "Berapa yang sudah Anda keluarkan untuk mengatasinya?" | "Pernah beli aplikasi 99 ribu" | Kesediaan membayar terbukti |
| "Apa yang terjadi bila ini tidak teratasi?" | "Ya rugi terus" | Urgensi |

> Pertanyaan ketiga adalah yang paling bernilai: ia menanyakan **apa yang sudah benar-benar dibayarkan**, bukan apa yang akan dibayarkan. Yang pertama adalah data; yang kedua adalah ramalan.

#### 7.5.3 Kekeliruan Khas Penetapan Harga

| Kekeliruan | Akibat |
|------------|--------|
| Menetapkan harga terlalu rendah "agar cepat banyak pengguna" | Sulit menaikkan; menarik pengguna yang tidak serius; margin tidak pernah cukup |
| Gratis selamanya tanpa rencana pendapatan | Biaya tumbuh, pendapatan tidak |
| Menyamai harga kompetitor tanpa alasan | Mengabaikan perbedaan nilai |
| Tidak pernah menguji harga | Asumsi tidak terverifikasi sampai terlambat |

> **Harga terlalu rendah lebih berbahaya daripada terlalu tinggi** pada tahap awal. Harga yang terlalu tinggi menghasilkan penolakan yang dapat dipelajari; harga yang terlalu rendah menghasilkan pengguna yang tidak menunjukkan apakah masalahnya benar-benar bernilai bagi mereka.

---

### 7.6 Daftar Risiko

#### 7.6.1 Kategori Risiko

| Kategori | Contoh |
|----------|--------|
| **Pasar** | Masalahnya tidak cukup terasa; segmen terlalu kecil |
| **Teknis** | Komponen inti tidak dapat dibangun sesuai rencana |
| **Operasional** | Beban dukungan melampaui kapasitas |
| **Finansial** | *Unit economics* tidak dapat positif; kehabisan modal |
| **Kompetitif** | Pemain besar masuk; alternatif gratis muncul |
| **Regulasi** | Aturan baru membatasi model bisnis |
| **Tim** | Anggota kunci keluar; konflik tidak terselesaikan |
| **Ketergantungan** | Penyedia menaikkan harga atau menghentikan layanan |

#### 7.6.2 Format Daftar Risiko

| ID | Risiko | Kemungkinan | Dampak | Tanda awal | Mitigasi |
|----|--------|-------------|--------|-----------|----------|
| R-01 | Pengguna berhenti setelah 2 bulan | Tinggi | Tinggi | Penurunan pemakaian minggu ke-6 | Wawancara pengguna yang berhenti; perbaiki *onboarding* |
| R-02 | Biaya API naik 3× | Sedang | Tinggi | Pengumuman penyedia | Siapkan alternatif; hitung ulang margin |
| R-03 | Anggota tim tidak dapat melanjutkan | Sedang | Sedang | Penurunan kontribusi | Dokumentasi; pembagian tugas tidak tunggal |

Kolom **tanda awal** adalah yang membedakan daftar risiko yang berguna: ia menjawab *"bagaimana kita tahu risiko ini mulai terjadi, sebelum terlambat?"*

#### 7.6.3 Risiko Terbesar Biasanya Risiko Pasar

Untuk usaha tahap awal, risiko yang paling mungkin menggagalkan adalah **"tidak ada yang cukup membutuhkannya"**. Ini sesuai dengan penyebab kegagalan terbanyak yang dibahas pada Minggu 1.

Karena itu, mitigasi yang paling penting bukan teknis melainkan: **terus menguji dengan pelanggan nyata, dan bersedia mengubah arah bila buktinya mengatakan demikian.**

---

### 7.7 Milestone 2 — Bukti Kelayakan

Yang dikumpulkan pada Minggu 7:

| Berkas | Isi |
|--------|-----|
| Perhitungan pasar (S-05) | *Bottom-up*, bersumber |
| Penilaian kelayakan (S-06) | Teknis dan operasional |
| Model *unit economics* (S-07) | Dengan analisis sensitivitas |
| Daftar risiko | Minimal 8, dengan tanda awal dan mitigasi |
| Catatan wawancara | **Minimal 12** terdokumentasi |
| **Kesimpulan kelayakan** | **Lanjut, ubah arah, atau hentikan** — berbasis angka |

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 7 buku ajar](../06-buku-ajar/bab-07-unit-economics-harga-risiko.md).
- Mengumpulkan data biaya nyata: harga API, biaya server, biaya transaksi.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | Pembahasan S-06; tim dengan hambatan operasional menjelaskan |
| Konsep | 35' | Empat besaran pokok; membaca rasio |
| **Studio** | 45' | **Kegiatan inti:** membangun model di spreadsheet, termasuk sensitivitas |
| Konsep | 25' | Strategi harga; kekeliruan khas |
| Studio | 25' | Daftar risiko dengan tanda awal |
| Penutup | 10' | Pengumpulan P-02 |

**Kegiatan inti — model yang dapat diubah:** spreadsheet dibangun dengan **sel asumsi terpisah** sehingga mengubah satu angka langsung mengubah seluruh hasil. Dosen menantang: *"ubah lama berlangganan menjadi 3 bulan. Apa yang terjadi? Apakah usaha ini masih layak?"*

Latihan ini sering mengungkap bahwa kelayakan usaha bergantung pada satu asumsi yang belum pernah diuji.

### Setelah Kelas (120 menit)

- Menyelesaikan [Studio 7](../04-labs/lab-07-model-unit-economics.md).
- Mempersiapkan UTS dengan [kisi-kisi](../05-assessments/kisi-kisi-uts.md).

---

## Penugasan

**S-07 — Model *Unit Economics*** dan **P-02 — Milestone 2**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Spreadsheet model + daftar risiko + berkas Milestone 2 |
| Isi model | CAC · LTV · margin kotor · *payback* · titik impas · **analisis sensitivitas 3 asumsi** |
| Daftar risiko | Minimal 8, dengan **tanda awal** dan mitigasi |
| Kesimpulan | **Lanjut, ubah, atau hentikan** — berbasis angka |
| Tenggat | Akhir Minggu 7 |
| Bobot | 6,25% (Observasi) |
| Yang menggugurkan | Model tanpa analisis sensitivitas; biaya waktu tim tidak dihitung |

---

## Rangkuman

1. ***Unit economics* menjawab:** apakah melayani satu pelanggan menghasilkan lebih dari biayanya?
2. Bila LTV/CAC < 1, **pertumbuhan memperburuk keadaan** — besaran pasar tidak menolong.
3. **CAC yang hanya menghitung biaya iklan terlalu rendah**; waktu tim adalah komponen terbesar pada tahap awal.
4. Margin kotor wajib memasukkan **biaya dukungan per pengguna** bila masih manual.
5. Patokan LTV/CAC = 3 adalah kebiasaan industri, **bukan hukum** — dan LTV tahap awal selalu dugaan.
6. **Analisis sensitivitas wajib**; model tanpanya menyajikan kepastian yang tidak dimilikinya.
7. Harga berbasis **nilai** paling tepat; datanya berasal dari wawancara.
8. Pertanyaan harga paling bernilai: **"berapa yang sudah Anda keluarkan untuk mengatasinya?"**
9. **Harga terlalu rendah lebih berbahaya daripada terlalu tinggi** pada tahap awal.
10. Daftar risiko wajib memuat **tanda awal** — bagaimana tahu risiko mulai terjadi sebelum terlambat.
11. Risiko terbesar usaha tahap awal hampir selalu **risiko pasar**.

---

## Referensi

1. Croll, A., & Yoskovitz, B. (2013). *Lean Analytics*. O'Reilly.
2. Blank, S., & Dorf, B. (2020). *The Startup Owner's Manual*, Bab 8. Wiley.
3. Osterwalder, A., & Pigneur, Y. (2010). *Business Model Generation*. Wiley.
4. Skok, D. *SaaS Metrics 2.0*. <https://www.forentrepreneurs.com/saas-metrics-2/>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
