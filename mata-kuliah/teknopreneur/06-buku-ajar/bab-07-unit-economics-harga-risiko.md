# BAB 7: *UNIT ECONOMICS*, HARGA, DAN RISIKO

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `TEKNO-Sub-CPMKUAI21-1` | Menganalisis (C4) kelayakan ekonomis per pelanggan dan mengevaluasi (C5) keputusan harga beserta risikonya secara etis | C4–C5 |

Setelah membaca bab ini, pembaca diharapkan mampu:

1. **Menjelaskan** (C2) mengapa kelayakan diuji pada satu pelanggan sebelum diuji pada seribu.
2. **Menerapkan** (C3) perhitungan CAC, LTV, margin kontribusi, dan titik impas.
3. **Menganalisis** (C4) kepekaan hasil terhadap perubahan asumsi.
4. **Mengevaluasi** (C5) keputusan harga dari sisi nilai dan dari sisi etika.
5. **Merumuskan** (C5) daftar risiko beserta mitigasinya.

---

## 7.1 Menguji Kelayakan pada Satu Pelanggan

### 7.1.1 Gagasan Pokoknya

Sebuah usaha yang merugi pada satu pelanggan akan merugi lebih besar pada seribu pelanggan. Pertumbuhan memperbesar apa pun yang sudah ada, termasuk kerugian.

Karena itu pertanyaannya disusun ulang: **apakah melayani satu pelanggan tambahan menghasilkan lebih banyak daripada biayanya?**

| Pertanyaan | Singkatan | Arti |
|------------|-----------|------|
| Berapa biaya memperoleh satu pelanggan? | **CAC** | *Customer Acquisition Cost* |
| Berapa nilai yang diberikan satu pelanggan selama ia bertahan? | **LTV** | *Lifetime Value* |
| Berapa sisa dari setiap rupiah pendapatan setelah biaya langsung? | **Margin kontribusi** | — |
| Berapa lama sampai CAC kembali? | **Masa balik modal** | *Payback period* |

### 7.1.2 Mengapa Ini Dibahas Sebelum Membangun

Tim yang menghitung *unit economics* pada Minggu 7 — sebelum satu baris kode ditulis — masih dapat mengubah tiga hal: segmen, harga, dan cara menjangkau pelanggan. Tim yang menghitungnya pada Minggu 14 hanya dapat menuliskannya dalam laporan.

> Hitungan ini bukan latihan akuntansi. Ia adalah **cara menemukan bahwa sebuah rencana tidak dapat berjalan, selagi mengubahnya masih murah**.

---

## 7.2 Biaya Memperoleh Pelanggan (CAC)

### 7.2.1 Menghitungnya dengan Jujur

```
CAC = (seluruh biaya untuk memperoleh pelanggan) ÷ (jumlah pelanggan yang diperoleh)
```

Yang sering dilupakan: **waktu tim adalah biaya**, meskipun tidak ada uang yang berpindah.

| Komponen | Contoh kasus berjalan | Nilai |
|----------|----------------------|-------|
| Perjalanan ke pasar (4 orang × 8 kali) | Transportasi | Rp320.000 |
| Waktu tim mendatangi warung | 40 jam × Rp20.000/jam (upah pembanding) | Rp800.000 |
| Cetak brosur dan kartu | 200 lembar | Rp150.000 |
| Kuota internet untuk pendampingan | 2 bulan | Rp100.000 |
| **Total biaya** | | **Rp1.370.000** |
| **Pelanggan diperoleh** | | **12 orang** |
| **CAC** | | **Rp114.167 per pelanggan** |

Angka Rp20.000/jam dipakai sebagai **upah pembanding** — perkiraan nilai waktu yang wajar bila anggota tim bekerja paruh waktu. Memasukkannya penting: tanpa itu, CAC tampak sangat rendah dan tim menyimpulkan bahwa penjualan langsung dari pintu ke pintu adalah saluran yang murah. Ia tidak murah; ia hanya tidak dibayar tunai.

### 7.2.2 CAC per Saluran

| Saluran | Biaya | Pelanggan | CAC | Dapat diperbesar? |
|---------|-------|-----------|-----|-------------------|
| Mendatangi langsung | Rp1.370.000 | 12 | Rp114.167 | Tidak — terbatas jam tim |
| Rujukan dari pelanggan lama | Rp50.000 (hadiah kecil) | 4 | Rp12.500 | **Ya, bila pelanggan puas** |
| Grup WhatsApp paguyuban pedagang | Rp0 | 3 | Rp0 | Terbatas jumlah grup |
| Iklan media sosial | Rp500.000 | 1 | Rp500.000 | Ya, tetapi mahal |

Kolom terakhir adalah yang paling menentukan arah. Saluran dengan CAC terendah pada tabel ini — rujukan — juga satu-satunya yang membesar dengan sendirinya seiring bertambahnya pelanggan yang puas. Saluran itu tidak dapat dipaksakan; ia hanya muncul bila produknya benar-benar berguna.

> Temuan bahwa **rujukan adalah saluran utama** berulang hampir di setiap kasus usaha kecil Indonesia, dan sering mengejutkan tim yang merencanakan anggaran iklan. Pedagang mempercayai pedagang lain; mereka tidak mempercayai iklan.

### 7.2.3 CAC yang Berubah Seiring Waktu

| Tahap | Keadaan | CAC |
|-------|---------|-----|
| 10 pelanggan pertama | Tim mendatangi sendiri, banyak penolakan | Tertinggi |
| 11–50 | Mulai ada rujukan, tim lebih terampil | Menurun |
| 51–200 | Rujukan dominan bila produk berguna | Terendah |
| 200+ | Segmen mudah habis, harus menjangkau yang lebih sulit | Naik kembali |

Baris terakhir sering tidak diperhitungkan dalam rencana pertumbuhan. Pelanggan yang paling mudah diyakinkan selalu diperoleh lebih dahulu; sisanya lebih mahal.

---

## 7.3 Nilai Seumur Hidup Pelanggan (LTV)

### 7.3.1 Perhitungannya

```
LTV = (pendapatan per bulan − biaya langsung per bulan) × (rata-rata bulan bertahan)
```

| Komponen | Nilai kasus berjalan | Sumber |
|----------|---------------------|--------|
| Harga langganan | Rp25.000/bulan | Keputusan tim, di bawah nilai kerugian yang dicegah |
| Biaya langsung (pesan, server, data) | Rp3.000/bulan | Hitungan penyedia layanan |
| **Margin kontribusi** | **Rp22.000/bulan (88%)** | |
| Rata-rata bertahan | 8 bulan | **Asumsi lemah — belum ada data** |
| **LTV** | **Rp176.000** | |

Baris "rata-rata bertahan" ditandai sebagai asumsi lemah, dan penandaan itu penting. Angka 8 bulan bukan hasil pengamatan; ia perkiraan. Seluruh kesimpulan pada bab ini bergantung padanya.

### 7.3.2 Rasio LTV/CAC

```
LTV / CAC = Rp176.000 / Rp114.167 = 1,54
```

| Rasio | Arti |
|-------|------|
| < 1 | Merugi pada setiap pelanggan; pertumbuhan memperbesar kerugian |
| 1–2 | **Bertahan hidup, tidak dapat tumbuh** |
| 3 | Sehat; tersedia ruang untuk tumbuh |
| > 5 | Mungkin kurang berinvestasi dalam memperoleh pelanggan |

Hasil 1,54 menempatkan usaha pada kategori kedua. Ini bukan kegagalan, melainkan **temuan yang berguna**: rencana sebagaimana adanya belum dapat tumbuh, dan masih ada waktu untuk mengubahnya.

### 7.3.3 Memperbaiki Rasio

| Cara | Pengaruh | Risiko |
|------|----------|--------|
| Menaikkan harga | LTV naik sebanding | Sebagian pelanggan pergi |
| Memperpanjang masa bertahan | LTV naik sebanding | Menuntut produk yang benar-benar berguna |
| Menurunkan CAC lewat rujukan | CAC turun tajam | Hanya terjadi bila pelanggan puas |
| Menurunkan biaya langsung | Margin naik sedikit | Ruangnya kecil (sudah 88%) |
| Menambah layanan berbayar | LTV naik | Menambah beban operasional |

Dua baris tengah bermuara pada hal yang sama: **produk harus benar-benar berguna**. Tidak ada penyesuaian angka yang dapat menggantikannya. Rasio LTV/CAC yang buruk paling sering merupakan gejala, bukan penyakit.

Perhitungan ulang bila masa bertahan menjadi 18 bulan dan separuh pelanggan datang dari rujukan:

```
LTV  = Rp22.000 × 18            = Rp396.000
CAC  = (114.167 + 12.500) ÷ 2   = Rp63.334
Rasio= 396.000 / 63.334         = 6,25
```

Perubahan dari 1,54 menjadi 6,25 tidak berasal dari perubahan harga sama sekali. Ia berasal dari produk yang cukup berguna sehingga orang bertahan dan menceritakannya.

---

## 7.4 Menetapkan Harga

### 7.4.1 Tiga Cara Menetapkan Harga

| Cara | Dasar | Kelemahan |
|------|-------|-----------|
| **Berbasis biaya** | Biaya + margin | Mengabaikan nilai bagi pengguna |
| **Berbasis pesaing** | Mengikuti harga pasar | Mengabaikan perbedaan produk |
| **Berbasis nilai** | Sebagian dari nilai yang diberikan | **Paling tepat, paling sulit** |

### 7.4.2 Harga Berbasis Nilai pada Kasus Berjalan

```
Nilai yang diberikan  : mencegah kerugian Rp300.000-400.000/bulan
Bila mencegah separuh : Rp150.000-200.000/bulan
Harga sebagai bagian  : 12-17% dari nilai  →  Rp25.000/bulan
```

| Pertanyaan | Jawaban |
|------------|---------|
| Mengapa tidak Rp100.000? | Nilai belum terbukti; pengguna belum percaya pada angka itu |
| Mengapa tidak Rp5.000? | Terlalu murah menimbulkan keraguan mutu; margin tak menutup beban |
| Mengapa tidak gratis? | Gratis menghilangkan bukti terkuat bahwa produk bernilai |

Baris terakhir perlu ditegaskan. Pengguna yang membayar Rp25.000 memberikan bukti yang tidak dapat digantikan oleh seribu pengguna gratis: ia menilai layanan ini lebih berharga daripada Rp25.000 miliknya. Itu satu-satunya bentuk persetujuan yang benar-benar mahal bagi pemberinya.

### 7.4.3 Harga dan Etika

| Praktik | Penilaian | Prinsip |
|---------|-----------|---------|
| Harga jelas sejak awal | Sah | Menghindari `gharar` |
| Uji coba gratis yang otomatis berlanjut tanpa pemberitahuan | **Tidak sah** | `gharar` — syarat tidak jelas saat menyetujui |
| Harga berbeda untuk segmen berbeda, dinyatakan terbuka | Sah | Boleh selama tidak menyembunyikan |
| Harga dinaikkan setelah pengguna terikat dan sulit pindah | **Tidak sah** | `ghabn` — memanfaatkan ketidakberdayaan |
| Menyembunyikan biaya tambahan sampai saat pembayaran | **Tidak sah** | `tadlis` |
| Potongan harga untuk pembayaran tahunan | Sah | Pertukaran yang jelas |

Baris kedua pantas diperhatikan karena praktik itu sangat lazim. Uji coba gratis itu sendiri tidak bermasalah; yang bermasalah adalah **penagihan otomatis tanpa pemberitahuan yang jelas sebelum masa gratis berakhir**. Perbaikannya sederhana dan tidak menghapus praktiknya: kirim pemberitahuan tiga hari sebelumnya, dengan satu ketukan untuk berhenti.

> Daftar ini adalah bentuk penerapan `gharar`, `tadlis`, dan `ghabn` yang diperkenalkan pada Bab 1. Ia akan dipakai lagi sebagai daftar periksa audit etika pada Bab 11.

---

## 7.5 Titik Impas dan Analisis Kepekaan

### 7.5.1 Titik Impas

```
Titik impas (pelanggan) = biaya tetap bulanan ÷ margin kontribusi per pelanggan
```

| Komponen | Nilai |
|----------|-------|
| Biaya tetap bulanan (server, layanan pesan, perkakas) | Rp450.000 |
| Margin kontribusi per pelanggan | Rp22.000 |
| **Titik impas** | **21 pelanggan** |

Angka 21 adalah angka yang dapat dipahami dan dikejar. Ia jauh lebih berguna bagi tim daripada proyeksi pendapatan tiga tahun.

### 7.5.2 Analisis Kepekaan

Setiap angka dalam perhitungan adalah asumsi. Analisis kepekaan menanyakan: **asumsi mana yang paling menentukan hasil?**

| Asumsi | Nilai dasar | Bila turun 30% | Bila naik 30% | Pengaruh pada LTV/CAC |
|--------|-------------|----------------|---------------|----------------------|
| Harga | Rp25.000 | Rp17.500 | Rp32.500 | 1,54 → 1,05 / 2,03 |
| Masa bertahan | 8 bulan | 5,6 bulan | 10,4 bulan | 1,54 → 1,08 / 2,00 |
| CAC | Rp114.167 | Rp79.917 | Rp148.417 | 1,54 → 2,20 / 1,19 |
| Biaya langsung | Rp3.000 | Rp2.100 | Rp3.900 | 1,54 → 1,60 / 1,48 |

| Pembacaan | Kesimpulan |
|-----------|------------|
| Baris terakhir hampir tidak berpengaruh | Menghemat biaya langsung bukan prioritas |
| Tiga baris pertama berpengaruh besar | Harga, retensi, dan CAC adalah yang menentukan |
| CAC memiliki rentang terlebar | **Prioritas pertama: menurunkan CAC lewat rujukan** |

Analisis ini mengubah daftar pekerjaan tim. Tanpa ia, tim mungkin menghabiskan minggu-minggu berikutnya mengoptimalkan biaya server — pekerjaan yang terasa produktif dan hampir tidak berpengaruh.

### 7.5.3 Daftar Risiko

| Risiko | Kemungkinan | Dampak | Mitigasi |
|--------|-------------|--------|----------|
| Pengguna berhenti setelah bulan pertama | Tinggi | Tinggi | Ukur retensi sejak pengguna pertama; wawancara yang berhenti |
| Perkiraan tidak akurat sehingga dipercaya lalu merugikan | Sedang | **Sangat tinggi** | Tampilkan rentang, bukan angka tunggal; nyatakan batas ketelitian |
| Kompetitor besar menambahkan fitur serupa | Rendah | Tinggi | Perdalam segmen; hubungan pribadi |
| Tim tidak dapat melanjutkan setelah lulus | Tinggi | Tinggi | Nyatakan sejak awal; rencana penghentian yang etis |
| Data pengguna bocor | Rendah | Sangat tinggi | Simpan seminimal mungkin; jangan simpan yang tak dipakai |

Baris kedua adalah risiko yang paling khas untuk kasus ini dan paling sering terlewat. Bila seorang pedagang mengubah keputusan belanjanya berdasarkan angka yang tim berikan, dan angka itu keliru, kerugiannya nyata dan ditanggung orang lain. Menampilkan rentang alih-alih angka tunggal, serta menyatakan secara terbuka bahwa ini perkiraan, adalah kewajiban — bukan pilihan rancangan.

---

## AI Corner — Bab 7

### Batas Pemakaian

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI memeriksa rumus perhitungan | Meminta AI menentukan harga produk tim |
| Meminta AI menjelaskan istilah keuangan | Meminta AI memperkirakan masa bertahan pelanggan |
| Meminta AI menyusun kerangka analisis kepekaan | Meminta AI mengisi angka CAC atau LTV |
| Meminta AI menyebutkan risiko yang biasa terlewat | Meminta AI menilai apakah rasio tim "baik" |

### Mengapa Angka Acuan dari AI Menyesatkan

Ditanya tentang rasio LTV/CAC yang baik, model akan menjawab "3:1" dengan yakin. Angka itu memang lazim disebut — dalam konteks **usaha rintisan perangkat lunak B2B di Amerika Utara yang didanai modal ventura**, dengan struktur biaya, harapan pertumbuhan, dan ketersediaan modal yang sama sekali berbeda dari tim mahasiswa yang melayani 79 warung di tiga kecamatan.

| Acuan yang lazim disebut | Konteks aslinya | Relevansi bagi tim ini |
|--------------------------|-----------------|------------------------|
| LTV/CAC = 3 | SaaS B2B terdanai VC | Terbatas; tidak ada modal untuk dibakar |
| *Churn* bulanan <5% | Langganan korporat | Tidak sebanding dengan pedagang mikro |
| Masa balik modal 12 bulan | Usaha dengan landasan dana | Tim mahasiswa tidak punya 12 bulan |
| Pertumbuhan 20%/bulan | Usaha rintisan tahap awal terdanai | Tidak relevan bagi usaha yang dibiayai penjualan |

Yang menjadi acuan bagi tim bukan angka-angka itu, melainkan **angka tim sendiri yang diukur berulang**: apakah CAC bulan ini lebih rendah daripada bulan lalu, apakah pelanggan bertahan lebih lama.

### Pemakaian yang Dianjurkan: Pemeriksa Konsistensi

```
Berikut perhitungan unit economics tim saya:
[tempelkan tabel]

Tugas Anda:
1. Periksa apakah ada angka yang tidak konsisten antar tabel.
2. Tandai angka yang tidak punya keterangan sumber.
3. Sebutkan komponen biaya yang umum terlewat dalam perhitungan
   CAC untuk penjualan langsung.

Jangan mengusulkan angka pengganti dan jangan menilai apakah
rasio ini baik atau buruk.
```

Butir 1 adalah pemakaian yang paling bernilai. Tabel yang disusun beberapa minggu dengan beberapa orang hampir selalu mengandung ketidakkonsistenan — harga Rp25.000 di satu tempat dan Rp30.000 di tempat lain — dan hal semacam itu adalah yang pertama ditemukan penguji.

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan mengapa kelayakan diuji pada satu pelanggan sebelum diuji pada seribu.
2. Tuliskan rumus CAC, LTV, margin kontribusi, dan titik impas.
3. Mengapa waktu tim harus dihitung sebagai biaya dalam CAC?
4. Sebutkan tiga cara menetapkan harga dan kelemahan masing-masing.
5. Mengapa pengguna yang membayar Rp25.000 memberi bukti yang tidak dapat digantikan seribu pengguna gratis?

### Tingkat Menengah

6. Hitung CAC untuk tim yang menghabiskan Rp800.000 transportasi, 60 jam waktu tim (upah pembanding Rp20.000/jam), dan Rp200.000 cetakan, untuk memperoleh 15 pelanggan. Bandingkan dengan CAC bila 5 dari 15 pelanggan itu datang dari rujukan tanpa biaya, dan jelaskan mengapa perbandingan itu penting bagi rencana.

7. Sebuah usaha memiliki harga Rp40.000/bulan, biaya langsung Rp12.000/bulan, masa bertahan 6 bulan, dan CAC Rp250.000. Hitung margin kontribusi, LTV, dan rasio LTV/CAC. Tentukan kategorinya, lalu usulkan dua perubahan yang membawa rasio ke atas 3, dengan menyebutkan risiko masing-masing.

8. Susun analisis kepekaan untuk usaha tersebut dengan empat asumsi pada variasi ±30%. Tentukan asumsi mana yang paling menentukan dan apa artinya bagi prioritas pekerjaan tim delapan minggu ke depan.

9. Nilailah lima praktik penetapan harga berikut dengan prinsip `gharar`, `tadlis`, `ghabn`. Untuk yang tidak sah, usulkan perbaikan yang tidak menghapus praktiknya.
   - Uji coba 14 hari, berlanjut otomatis tanpa pemberitahuan
   - Harga khusus untuk pelanggan 50 pertama, dinyatakan terbuka
   - Biaya pencairan dana yang baru muncul saat penarikan
   - Kenaikan harga 40% setelah setahun, dengan pemberitahuan sebulan
   - Paket termurah dibuat sengaja tidak berguna agar orang memilih yang mahal

### Tingkat Mahir

10. **Latihan lapangan.** Uji harga produk Anda dengan cara yang paling tegas: tawarkan kepada lima calon pengguna nyata dan minta pembayaran di muka untuk satu bulan layanan. Laporkan berapa yang membayar, berapa yang menolak, dan alasan yang disebutkan. Bandingkan hasil ini dengan jawaban atas pertanyaan *"berapa Anda mau membayar?"* yang diajukan kepada orang yang sama sebelumnya. Jelaskan selisihnya.

11. Susun perhitungan *unit economics* lengkap untuk proyek tim Anda — CAC per saluran, LTV, margin kontribusi, titik impas, dan analisis kepekaan empat asumsi. Tandai setiap angka dengan kekuatan buktinya. Tutup dengan satu paragraf yang menyatakan: pada keadaan seperti apa tim akan menyimpulkan bahwa usaha ini **tidak** layak dilanjutkan.

12. Rancang skema harga untuk produk Anda yang memenuhi tiga syarat sekaligus: (a) menghasilkan rasio LTV/CAC di atas 3 pada asumsi yang wajar; (b) lolos seluruh daftar periksa `gharar`/`tadlis`/`ghabn`; (c) dapat dipahami pengguna dalam satu kalimat. Tunjukkan perhitungannya, lalu jelaskan pertukaran apa yang Anda terima untuk memenuhi ketiganya — karena biasanya ketiganya tidak dapat dimaksimalkan bersamaan.

---

## Rangkuman

| Gagasan pokok | Rumusan singkat |
|---------------|-----------------|
| Alasan menghitung | Pertumbuhan memperbesar apa pun yang ada, termasuk kerugian |
| Waktu tim | Adalah biaya, meskipun tidak dibayar tunai |
| Saluran terbaik | Rujukan — termurah dan satu-satunya yang membesar sendiri |
| Rasio LTV/CAC | 1,54 berarti bertahan hidup tanpa dapat tumbuh |
| Perbaikan rasio | Hampir selalu bermuara pada produk yang benar-benar berguna |
| Harga berbasis nilai | Sebagian dari kerugian yang dicegah, bukan biaya + margin |
| Gratis | Menghilangkan bukti terkuat bahwa produk bernilai |
| Etika harga | Uji coba yang berlanjut diam-diam adalah `gharar`, dan mudah diperbaiki |
| Kepekaan | Menunjukkan pekerjaan mana yang berpengaruh dan mana yang sia-sia |
| Risiko khas | Perkiraan yang dipercaya lalu keliru merugikan orang lain |

---

## Referensi

1. Croll, A., & Yoskovitz, B. (2013). *Lean Analytics*. O'Reilly Media.
2. Skok, D. (2018). *SaaS Metrics 2.0: A Guide to Measuring and Improving What Matters*. For Entrepreneurs.
3. Nagle, T. T., & Müller, G. (2017). *The Strategy and Tactics of Pricing* (6th ed.). Routledge.
4. Ramanujam, M., & Tacke, G. (2016). *Monetizing Innovation: How Smart Companies Design the Product Around the Price*. Wiley.
5. Antonio, M. S. (2001). *Bank Syariah: Dari Teori ke Praktik*. Gema Insani.
6. Dewan Syariah Nasional MUI. (2000). *Fatwa DSN-MUI tentang Jual Beli*. DSN-MUI.
7. Otoritas Jasa Keuangan. (2023). *Pedoman Perlindungan Konsumen Sektor Jasa Keuangan*. OJK.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul mingguan | [Minggu 7 — *Unit Economics*, Harga, dan Risiko](../03-modules/week-07-unit-economics-harga-risiko.md) |
| Studio | [Studio 7 — Model *Unit Economics*](../04-labs/lab-07-model-unit-economics.md) |
| Bab sebelumnya | [Bab 6 — Kelayakan Teknologi dan Operasional](bab-06-kelayakan-teknologi-dan-operasional.md) |
| Bab berikutnya | [Bab 8 — Model Bisnis dan Proposisi Nilai](bab-08-model-bisnis-dan-proposisi-nilai.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
