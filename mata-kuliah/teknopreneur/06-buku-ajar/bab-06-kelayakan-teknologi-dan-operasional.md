# BAB 6: KELAYAKAN TEKNOLOGI DAN OPERASIONAL

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `TEKNO-Sub-CPMKUAI21-1` | Mengevaluasi (C5) kelayakan teknologi, operasional, dan sumber daya sebuah usulan usaha, serta merumuskan asumsi paling berisiko beserta cara mengujinya | C4–C5 |

Setelah membaca bab ini, pembaca diharapkan mampu:

1. **Membedakan** (C2) empat jenis kelayakan yang harus dinilai.
2. **Menganalisis** (C4) beban operasional yang tersembunyi di balik sebuah janji produk.
3. **Mengidentifikasi** (C4) asumsi paling berisiko dalam rencana usaha.
4. **Merancang** (C5) uji termurah untuk asumsi tersebut.
5. **Menilai** (C5) kesesuaian antara kapasitas tim dan tuntutan usaha.

---

## 6.1 Empat Jenis Kelayakan

### 6.1.1 Yang Harus Dinilai Sebelum Membangun

| Jenis | Pertanyaan | Gejala bila diabaikan |
|-------|------------|----------------------|
| **Teknis** | Dapatkah dibuat dengan kemampuan dan waktu yang ada? | Proyek tak selesai di Minggu 15 |
| **Operasional** | Dapatkah dijalankan hari demi hari setelah jadi? | Berjalan saat demo, mati setelahnya |
| **Ekonomis** | Apakah pendapatan menutup biaya? | Dibahas di Bab 7 |
| **Hukum & etika** | Bolehkah dilakukan? | Dibahas di Bab 11 |

Kelayakan operasional adalah yang paling sering diabaikan mahasiswa Informatika, karena tidak terlihat dalam kode. Ia baru muncul ketika produk benar-benar dipakai orang.

### 6.1.2 Kelayakan Teknis: Pertanyaan yang Sebenarnya

Pertanyaan teknis yang tepat bukan *"bisakah ini dibuat?"* — hampir semua hal bisa dibuat. Pertanyaannya adalah:

| Pertanyaan | Mengapa penting |
|------------|-----------------|
| Bisakah dibuat **oleh tim ini** | Keterampilan yang ada, bukan yang mungkin dipelajari |
| Dalam **waktu yang tersedia** | 14 minggu, dengan lima mata kuliah lain berjalan |
| Dengan **biaya yang ada** | Anggaran mahasiswa, bukan anggaran perusahaan |
| Pada **perangkat pengguna** | Android 8, RAM 2 GB, sinyal tidak stabil |
| Tanpa **ketergantungan yang belum pasti** | Izin, API berbayar, kerja sama yang belum disepakati |

Baris terakhir adalah pembunuh diam-diam. Rencana yang bergantung pada satu API berbayar, satu izin dari dinas, atau satu kerja sama dengan koperasi yang belum dihubungi sesungguhnya bergantung pada asumsi yang belum diuji sama sekali.

### 6.1.3 Kelayakan Operasional: Apa yang Terjadi Setelah Jadi

Setiap janji produk memiliki beban operasional di baliknya.

| Janji produk | Beban operasional yang tersembunyi |
|--------------|-----------------------------------|
| "Perkiraan belanja setiap subuh" | Ada yang harus memastikan hitungan berjalan tiap hari, termasuk hari libur |
| "Data selalu tersinkron" | Ada yang menangani sinkronisasi gagal |
| "Dukungan pengguna" | Ada yang menjawab pesan; pukul berapa sampai pukul berapa? |
| "Data aman" | Ada yang mencadangkan; ada yang memulihkan bila hilang |
| "Harga selalu terbaru" | Ada yang memperbarui harga — dari mana, seberapa sering? |
| "Cocok untuk warung apa pun" | Ada yang menyesuaikan untuk setiap jenis warung |

Kolom kanan adalah pekerjaan manusia yang berlangsung terus-menerus. Bila tidak ada yang mengerjakannya, janji pada kolom kiri menjadi `tadlis` — menyembunyikan cacat yang diketahui.

> Latihan yang mengubah cara pandang: ambil *pitch deck* tim Anda, dan untuk setiap janji di dalamnya tuliskan siapa namanya yang akan mengerjakannya pada hari Minggu pukul 05.00. Janji yang tidak ada namanya adalah janji yang belum layak diucapkan.

---

## 6.2 Beban Operasional yang Sering Terlewat

### 6.2.1 Daftar Periksa Operasional

| Aspek | Pertanyaan | Bila jawabannya "belum dipikirkan" |
|-------|------------|-----------------------------------|
| **Pendaftaran pengguna** | Siapa yang membantu pengguna pertama kali memakai? | Sebagian besar pengguna berhenti di hari pertama |
| **Data awal** | Dari mana data awal berasal? | Produk kosong saat dibuka pertama kali |
| **Kesalahan pengguna** | Apa yang terjadi bila pengguna salah input? | Data rusak, kepercayaan hilang |
| **Dukungan** | Ke mana pengguna bertanya? | Keluhan menumpuk tanpa penanganan |
| **Pembaruan** | Bagaimana perbaikan sampai ke pengguna? | Bug pertama menjadi permanen |
| **Penagihan** | Bagaimana uang diterima? | Tidak ada pendapatan meski ada pemakai |
| **Ketika tim lulus** | Siapa yang meneruskan? | Layanan mati tanpa pemberitahuan |

Baris terakhir adalah pertanyaan etis yang khas untuk proyek mahasiswa. Bila pedagang sungguh-sungguh mulai bergantung pada layanan tim, menghentikannya begitu saja setelah semester berakhir menimbulkan kerugian nyata bagi orang yang sudah memberikan kepercayaannya.

| Jalan keluar yang sah | Penjelasan |
|-----------------------|------------|
| Nyatakan sejak awal bahwa ini proyek kuliah dengan batas waktu | Kejujuran di muka menghilangkan `gharar` |
| Sediakan jalan keluar data | Pengguna dapat mengambil datanya kapan pun |
| Beri tenggang sebelum penutupan | Minimal satu bulan pemberitahuan |
| Rancang agar tidak menimbulkan ketergantungan mendadak | Cara lama tetap dapat dipakai |

### 6.2.2 Beban per Pengguna

Pertanyaan yang menentukan: **berapa menit kerja manusia yang dibutuhkan setiap pengguna, setiap bulan?**

```
Beban bulanan tim = jumlah pengguna × menit per pengguna

Contoh kasus berjalan:
  Pendaftaran & pendampingan awal :  45 menit (sekali)
  Pertanyaan & keluhan            :  10 menit/bulan
  Penyesuaian data                :   5 menit/bulan
                                     ──────────────────
  Rutin per pengguna per bulan    :  15 menit

  Pada 50 pengguna  :  750 menit  = 12,5 jam/bulan  → dapat ditangani
  Pada 200 pengguna : 3.000 menit = 50 jam/bulan    → melebihi kapasitas
  Pada 500 pengguna : 7.500 menit = 125 jam/bulan   → mustahil
```

Perhitungan sederhana ini menjawab pertanyaan yang sering tidak terjawab dalam rencana usaha mahasiswa: **pada jumlah pengguna berapa model ini patah?**

| Jawaban | Tindak lanjut |
|---------|---------------|
| Patah di 200 pengguna, target tahun pertama 79 | Aman; catat sebagai batas |
| Patah di 50, target 200 | Harus dikurangi bebannya atau ditambah orangnya |
| Tidak pernah dihitung | **Asumsi paling berisiko, dan tidak disadari** |

### 6.2.3 Mengurangi Beban Operasional

| Cara | Contoh | Risiko |
|------|--------|--------|
| Otomatisasi | Pendaftaran mandiri tanpa pendampingan | Tingkat berhenti pakai naik |
| Penyederhanaan | Hapus fitur yang menimbulkan pertanyaan | Kehilangan sebagian nilai |
| Pembatasan segmen | Hanya melayani satu jenis warung | Pasar mengecil |
| Pemberdayaan pengguna | Panduan yang benar-benar dibaca | Butuh usaha penulisan |
| Komunitas | Pengguna lama membantu pengguna baru | Perlu waktu terbentuk |

Baris ketiga adalah pilihan yang paling sering benar untuk tim mahasiswa dan paling sulit diterima. Mempersempit segmen mengecilkan angka pasar dalam presentasi, tetapi membuat beban operasional dapat ditanggung — dan usaha yang dapat dijalankan lebih bernilai daripada usaha yang besar di atas kertas.

---

## 6.3 Asumsi Paling Berisiko

### 6.3.1 Mengurutkan Asumsi

Setiap rencana usaha berdiri di atas daftar asumsi. Tidak semuanya sama pentingnya.

| Sumbu | Pertanyaan |
|-------|------------|
| **Dampak bila salah** | Bila asumsi ini keliru, apakah usaha masih berjalan? |
| **Tingkat keyakinan** | Seberapa yakin kita, dan berdasarkan bukti apa? |

```
           Keyakinan RENDAH          Keyakinan TINGGI
        ┌──────────────────────┬──────────────────────┐
DAMPAK  │  ◄── UJI DULU        │  Pantau              │
BESAR   │      (prioritas 1)   │  (prioritas 3)       │
        ├──────────────────────┼──────────────────────┤
DAMPAK  │  Uji bila sempat     │  Abaikan             │
KECIL   │  (prioritas 2)       │  (prioritas 4)       │
        └──────────────────────┴──────────────────────┘
```

Kuadran kiri atas dikerjakan lebih dahulu, selalu. Tim yang menghabiskan waktu menyempurnakan hal-hal di kuadran kanan bawah sedang menunda pertanyaan yang menentukan nasib usahanya.

### 6.3.2 Asumsi yang Biasanya Ada di Kuadran Kiri Atas

| Asumsi | Mengapa berisiko tinggi |
|--------|------------------------|
| "Pengguna mau membayar" | Menyatakan mau ≠ membayar |
| "Pengguna mau mengubah kebiasaan" | Kebiasaan adalah pesaing terkuat |
| "Kami dapat menjangkau pengguna" | Saluran distribusi sering tidak ada |
| "Data yang diperlukan tersedia" | Sering baru diketahui setelah membangun |
| "Pihak ketiga bersedia bekerja sama" | Belum dihubungi sama sekali |

Asumsi kedua pantas diperhatikan khusus pada kasus berjalan. Perkiraan belanja hanya bernilai bila pedagang benar-benar mengubah cara mengambil keputusan subuh — dan perubahan kebiasaan yang sudah berjalan enam tahun adalah hal yang jauh lebih sulit daripada persoalan teknis mana pun dalam proyek ini.

### 6.3.3 Merancang Uji Termurah

Setiap asumsi berisiko diuji dengan cara **termurah yang masih memberi jawaban**.

| Asumsi | Uji mahal | Uji termurah |
|--------|-----------|--------------|
| Pengguna mau membayar | Bangun produk, pasang sistem bayar | **Minta uang muka Rp10.000 hari ini untuk layanan bulan depan** |
| Perkiraan belanja bermanfaat | Bangun sistem perkiraan otomatis | **Hitung manual untuk 3 warung selama 2 minggu, kirim lewat WhatsApp** |
| Pengguna mau memakai tiap hari | Bangun aplikasi, ukur retensi | **Kirim pesan harian selama 10 hari, hitung yang membalas** |
| Antarmuka dapat dipahami | Bangun aplikasi | **Gambar di kertas, minta orang menunjuk langkahnya** |
| Pihak ketiga mau bekerja sama | Susun proposal resmi | **Telepon dan tanyakan hari ini** |

Kolom kanan memiliki sifat yang sama: dapat dikerjakan dalam hitungan hari, berbiaya mendekati nol, dan **memberi jawaban yang sama tegasnya** dengan uji mahal.

Baris kedua adalah contoh yang paling penting dipahami. Menghitung manual untuk tiga warung selama dua minggu menjawab pertanyaan terbesar — apakah perkiraan ini benar-benar mengubah keputusan belanja — tanpa satu baris kode pun. Bila jawabannya tidak, tim baru saja menghemat tiga bulan.

> Prinsip ini sering disebut *Wizard of Oz*: layanan tampak otomatis bagi pengguna, padahal dikerjakan manusia di belakangnya. Ia sah selama pengguna tidak dibohongi tentang **apa yang ia terima**. Bila tim menyatakan "sistem otomatis kami" padahal dikerjakan manual, itu `tadlis`. Bila tim menyatakan "kami akan mengirimkan perkiraan setiap subuh" tanpa menyebut caranya, janji itu ditepati apa adanya dan tidak ada yang disembunyikan.

---

## 6.4 Kapasitas Tim

### 6.4.1 Menghitung Waktu yang Benar-Benar Ada

| Perhitungan | Angka |
|-------------|-------|
| Anggota tim | 4 orang |
| Jam kerja realistis per orang per minggu | 6 jam |
| Minggu efektif (dikurangi UTS, UAS, libur) | 11 minggu |
| **Total kapasitas tim** | **264 jam-orang** |

Dari 264 jam itu, sebagian besar sudah terpakai sebelum pembangunan dimulai:

| Kegiatan | Perkiraan jam |
|----------|--------------|
| Wawancara 15 narasumber (termasuk perjalanan) | 60 |
| Sintesis, dokumentasi, laporan mingguan | 50 |
| Penyusunan *deck* dan presentasi | 30 |
| Rapat tim | 35 |
| **Tersisa untuk membangun dan menguji** | **89 jam** |

Delapan puluh sembilan jam-orang adalah angka yang jauh lebih kecil daripada yang dibayangkan tim di Minggu 1. Ia setara dengan sekitar dua minggu kerja penuh satu orang.

| Yang muat dalam 89 jam | Yang tidak muat |
|------------------------|-----------------|
| Prototipe kertas dan pengujiannya | Aplikasi mobile native dua platform |
| Lembar kerja spreadsheet yang dipakai nyata | Sistem dengan akun, peran, dan basis data penuh |
| Bot pesan sederhana | Model pembelajaran mesin terlatih dari data sendiri |
| Halaman web satu layar | Sistem dengan sinkronisasi luring-daring |

### 6.4.2 Kesesuaian Tim dan Persoalan

| Pertanyaan | Bila jawabannya buruk |
|------------|----------------------|
| Adakah anggota yang benar-benar peduli pada persoalan ini? | Tim akan kehilangan tenaga di Minggu 8 |
| Dapatkah tim menemui penggunanya dengan mudah? | Bukti akan sulit dikumpulkan |
| Adakah keterampilan yang benar-benar tidak dimiliki siapa pun? | Sederhanakan ruang lingkup, bukan berharap belajar |
| Apakah semua anggota memahami persoalannya? | Satu orang akan mengerjakan segalanya |

Pertanyaan ketiga perlu dijawab dengan jujur pada Minggu 6, bukan Minggu 12. Mengubah ruang lingkup pada Minggu 6 adalah keputusan yang baik; pada Minggu 12 ia adalah penyelamatan darurat.

---

## AI Corner — Bab 6

### Batas Pemakaian

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI menyebutkan beban operasional yang biasa terlewat | Meminta AI menilai apakah proyek tim layak secara teknis |
| Meminta AI mengusulkan bentuk uji termurah untuk asumsi tertentu | Meminta AI memperkirakan berapa lama tim akan mengerjakannya |
| Meminta AI memeriksa apakah rencana memuat ketergantungan yang belum pasti | Meminta AI memutuskan ruang lingkup |
| Meminta AI menjelaskan istilah teknis yang belum dikenal | Meminta AI menyatakan bahwa teknologi tertentu "sudah matang" |

### Mengapa AI Memperkirakan Waktu Terlalu Optimis

Ketika ditanya berapa lama sebuah fitur dapat dibuat, model bahasa menghasilkan angka yang mencerminkan **teks yang pernah dibacanya** — tutorial, artikel, dan dokumentasi, yang hampir semuanya ditulis oleh orang yang sudah menguasai hal itu dan menuliskan jalur yang sudah bersih dari kesalahan.

Yang tidak tercermin dalam teks semacam itu:

| Yang hilang | Contoh |
|-------------|--------|
| Waktu belajar tim yang belum pernah memakainya | Berhari-hari untuk hal yang dijelaskan dalam 5 menit |
| Waktu memperbaiki kesalahan yang tidak ada di tutorial | Galat lingkungan, versi pustaka, izin perangkat |
| Waktu koordinasi antaranggota | Menunggu, menjelaskan, menggabungkan |
| Waktu yang hilang karena mata kuliah lain | Lima mata kuliah lain juga menuntut |

Karena itu perkiraan waktu diambil dari **kapasitas nyata tim** (§6.4.1), bukan dari jawaban model.

### Pemakaian yang Dianjurkan: Pencari Beban Tersembunyi

```
Rencana usaha kami: mengirimkan perkiraan kebutuhan belanja
harian kepada pemilik warung makan setiap pukul 04.00 melalui
WhatsApp.

Sebutkan pekerjaan manusia yang harus dilakukan terus-menerus
agar janji itu tertepati setiap hari selama setahun, termasuk
hari libur dan saat terjadi kesalahan.

Jangan menilai apakah rencana ini baik. Jangan mengusulkan
teknologi. Hanya sebutkan pekerjaannya.
```

Ini adalah salah satu pemakaian AI yang paling produktif dalam mata kuliah ini. Daftar yang dihasilkan biasanya memuat tiga sampai lima hal yang belum terpikir oleh tim — dan setiap butirnya kemudian **diperiksa sendiri oleh tim**, bukan diterima begitu saja.

---

## Latihan Soal

### Tingkat Dasar

1. Sebutkan empat jenis kelayakan dan pertanyaan pokok masing-masing.
2. Mengapa kelayakan operasional paling sering diabaikan mahasiswa Informatika?
3. Sebutkan beban operasional tersembunyi di balik janji "data selalu tersinkron".
4. Jelaskan dua sumbu pengurutan asumsi dan sebutkan kuadran mana yang dikerjakan lebih dahulu.
5. Apa yang dimaksud uji *Wizard of Oz*, dan kapan ia menjadi `tadlis`?

### Tingkat Menengah

6. Ambil tiga janji dari *pitch deck* mana pun yang Anda kenal. Untuk masing-masing, tuliskan pekerjaan manusia yang harus berlangsung terus-menerus di baliknya, beserta perkiraan menit per pengguna per bulan.

7. Hitung beban operasional bulanan untuk sebuah layanan dengan asumsi: pendampingan awal 30 menit sekali, keluhan 8 menit/bulan, penyesuaian 4 menit/bulan. Tentukan pada jumlah pengguna berapa model ini patah bila tim memiliki 40 jam/bulan. Usulkan dua cara menggeser titik patah itu beserta risikonya.

8. Susun lima asumsi paling berisiko untuk proyek tim Anda, tempatkan pada kuadran §6.3.1, lalu rancang uji termurah untuk dua asumsi di kuadran kiri atas. Untuk masing-masing, sebutkan berapa hari dan berapa rupiah biayanya.

9. Hitung kapasitas tim Anda dengan cara §6.4.1. Bandingkan sisa jam untuk membangun dengan ruang lingkup yang sedang direncanakan. Bila tidak muat, sebutkan tiga hal yang akan dikurangi dan alasannya.

### Tingkat Mahir

10. **Latihan lapangan.** Jalankan satu uji *Wizard of Oz* selama tujuh hari untuk salah satu asumsi terbesar proyek Anda, dengan minimal tiga pengguna nyata. Laporkan: apa yang dikerjakan manual, berapa menit per hari, berapa banyak pengguna yang bertahan sampai hari ketujuh, dan apa yang Anda pelajari yang tidak akan diketahui dari membangun sistem otomatis. Nyatakan pula bagaimana Anda menjaga agar pengguna tidak dibohongi.

11. Susun rencana penghentian layanan yang etis untuk proyek tim Anda, dengan asumsi semester berakhir dan tim lulus. Cakup: apa yang dinyatakan kepada pengguna sejak awal, bagaimana data dikembalikan, berapa lama tenggang pemberitahuan, dan apa yang dilakukan bila ada pengguna yang sudah membayar. Kaitkan setiap butir dengan prinsip `gharar` atau `amanah`.

12. Tim Anda menemukan bahwa asumsi "pengguna mau mengubah kebiasaan subuh yang sudah berjalan enam tahun" berada di kuadran kiri atas. Rancang tiga uji berbeda untuk asumsi ini, masing-masing dengan biaya dan tingkat ketegasan jawaban yang berbeda. Jelaskan uji mana yang Anda pilih dan mengapa, lalu sebutkan hasil seperti apa yang akan membuat tim mengubah arah usaha sepenuhnya.

---

## Rangkuman

| Gagasan pokok | Rumusan singkat |
|---------------|-----------------|
| Empat kelayakan | Teknis, operasional, ekonomis, hukum & etika |
| Pertanyaan teknis yang tepat | Bukan "bisakah dibuat" melainkan "oleh tim ini, dalam waktu ini" |
| Beban operasional | Setiap janji produk memiliki pekerjaan manusia di baliknya |
| Ujian janji | Siapa namanya yang mengerjakannya Minggu pukul 05.00? |
| Titik patah | Pada jumlah pengguna berapa beban melebihi kapasitas tim |
| Asumsi berisiko | Dampak besar + keyakinan rendah dikerjakan lebih dahulu |
| Uji termurah | Hitungan manual untuk 3 orang menjawab sama tegasnya dengan sistem penuh |
| Kapasitas nyata | ±89 jam-orang tersisa untuk membangun, jauh di bawah dugaan awal |
| Penghentian layanan | Kewajiban etis yang direncanakan sejak awal, bukan dipikirkan di akhir |

---

## Referensi

1. Ries, E. (2011). *The Lean Startup*. Crown Business.
2. Maurya, A. (2012). *Running Lean: Iterate from Plan A to a Plan That Works* (2nd ed.). O'Reilly Media.
3. Bland, D. J., & Osterwalder, A. (2019). *Testing Business Ideas*. Wiley.
4. Brooks, F. P. (1995). *The Mythical Man-Month: Essays on Software Engineering* (Anniversary ed.). Addison-Wesley.
5. Beyer, B., Jones, C., Petoff, J., & Murphy, N. R. (2016). *Site Reliability Engineering*. O'Reilly Media.
6. Kahneman, D., Lovallo, D., & Sibony, O. (2011). Before You Make That Big Decision. *Harvard Business Review*, 89(6), 50–60.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul mingguan | [Minggu 6 — Kelayakan Teknologi dan Operasional](../03-modules/week-06-kelayakan-teknologi-dan-operasional.md) |
| Studio | [Studio 6 — Uji Kelayakan Teknologi](../04-labs/lab-06-uji-kelayakan-teknologi.md) |
| Bab sebelumnya | [Bab 5 — Ukuran Pasar dan Analisis Kompetitor](bab-05-ukuran-pasar-dan-kompetitor.md) |
| Bab berikutnya | [Bab 7 — *Unit Economics*, Harga, dan Risiko](bab-07-unit-economics-harga-risiko.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
