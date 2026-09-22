# BAB 1: PENELITIAN DALAM INFORMATIKA

**Bahan rujukan penyelarasan kurikulum** — disusun Tri Aji Nugroho, S.T., M.T.
Pengampu mata kuliah menurut registri: **Andi Arniaty Arsyad, Ph.D.** (`AAA`).

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `METPEN-Sub-CPMK041-1` | Membedakan (C2) jenis penelitian Informatika dan menetapkan (C4) wilayah minat dengan pertimbangan yang tertulis | C2–C4 |

Setelah membaca bab ini, pembaca diharapkan mampu:

1. **Membedakan** (C2) penelitian dari pengembangan.
2. **Membedakan** (C2) empat jenis penelitian Informatika.
3. **Menjelaskan** (C2) kapan pembangunan artefak menghasilkan pengetahuan.
4. **Menilai** (C5) kelayakan sebuah wilayah topik.
5. **Menetapkan** (C4) satu wilayah minat beserta alasannya.

---

## 1.1 Apa yang Membedakan Penelitian

### 1.1.1 Pertanyaan yang Berbeda

Mahasiswa semester 7 telah membangun banyak hal: aplikasi, sistem, model,
antarmuka. Tidak semuanya penelitian — dan perbedaannya bukan soal
kerumitan.

| | Pengembangan | Penelitian |
|---|-------------|------------|
| Pertanyaan pokok | Bagaimana membuatnya bekerja? | Apa yang belum kita ketahui? |
| Ukuran keberhasilan | Sistem berjalan | **Pengetahuan bertambah** |
| Kegagalan | Sistem tidak berfungsi | Tidak ada — temuan negatif tetap temuan |
| Yang dilaporkan | Cara membangunnya | Apa yang dipelajari darinya |
| Nilai bagi orang lain | Dapat dipakai | Dapat dibangun di atasnya |
| Pembanding | Tidak diperlukan | Diperlukan |

Baris ketiga adalah pembeda yang paling sering mengejutkan. Dalam
pengembangan, sistem yang tidak berfungsi adalah kegagalan. Dalam penelitian,
hipotesis yang tidak didukung data adalah **hasil** — asalkan cara
memperolehnya sahih.

Perbedaan itu bukan kelonggaran. Ia adalah konsekuensi langsung dari tujuan
yang berbeda: penelitian bertujuan mengetahui, dan mengetahui bahwa sesuatu
tidak berlaku sama berharganya dengan mengetahui bahwa ia berlaku.

### 1.1.2 Ujian Sederhana

Pertanyaan yang memisahkan keduanya dapat diucapkan dalam satu kalimat:

> *Setelah pekerjaan ini selesai, apa yang kita ketahui yang tidak kita
> ketahui sebelumnya?*

Sebuah Tugas Akhir yang melaporkan "sistem berhasil dibangun dan berjalan
dengan baik" belum tentu melaporkan penelitian. Ia melaporkan bahwa sebuah
sistem ada — yang sudah diketahui sejak sistem itu selesai dibangun.

| Jawaban yang lemah | Jawaban yang kuat |
|--------------------|-------------------|
| "Sekarang ada aplikasi X" | "Sekarang diketahui bahwa pendekatan P menurunkan galat Q% pada keadaan R, dan gagal ketika S" |
| "Metode Y dapat diimplementasikan" | "Sekarang diketahui bahwa asumsi metode Y tidak terpenuhi pada data berbahasa Indonesia, karena Z" |
| "Sistem mendapat tanggapan positif" | "Sekarang diketahui bahwa staf menolak fitur T bukan karena kerumitannya, melainkan karena U" |

> Perhatikan pola pada kolom kanan: seluruhnya memuat **keadaan** — pada
> kondisi apa temuan itu berlaku. Pengetahuan yang tidak menyebutkan batas
> keberlakuannya sulit dipakai orang lain.

### 1.1.3 Hubungan Keduanya

Pengembangan dan penelitian bukan lawan. Dalam Informatika, keduanya sering
berjalan bersamaan: sesuatu dibangun **untuk** menjawab pertanyaan.

```
   PERTANYAAN
        ↓
   Apa yang perlu ada agar pertanyaan ini dapat dijawab?
        ↓
   MEMBANGUN  ← pengembangan berperan di sini
        ↓
   MENGUJI terhadap kriteria yang ditetapkan sebelum membangun
        ↓
   PENGETAHUAN
```

Yang menentukan bukan ada-tidaknya pembangunan, melainkan **urutannya**.
Pertanyaan mendahului pembangunan, dan kriteria keberhasilan ditetapkan
sebelum baris kode pertama ditulis.

---

## 1.2 Empat Jenis Penelitian Informatika

### 1.2.1 Perbandingannya

| Jenis | Pertanyaan khas | Contoh |
|-------|-----------------|--------|
| **Eksploratif** | Apa yang sebenarnya terjadi di sini? | Bagaimana pengembang Indonesia memakai bantuan AI dalam pekerjaan hariannya? |
| **Deskriptif** | Seberapa banyak, seberapa sering? | Berapa proporsi aplikasi pemerintah daerah yang memenuhi kriteria aksesibilitas tertentu? |
| **Eksplanatif** | Apakah A memengaruhi B? | Apakah umpan balik langsung menurunkan galat entri data pada petugas administrasi? |
| **Perancangan** | Dapatkah artefak ini memenuhi kebutuhan X lebih baik? | Dapatkah metode P menurunkan waktu pemrosesan tanpa menurunkan ketelitian? |

### 1.2.2 Memilih Jenis

Jenis penelitian tidak dipilih; ia **ditentukan oleh keadaan pengetahuan**.

| Keadaan pengetahuan | Jenis yang sesuai |
|---------------------|-------------------|
| Fenomena belum dipahami sama sekali | Eksploratif |
| Fenomena dikenal, besarannya belum diketahui | Deskriptif |
| Besaran diketahui, sebabnya belum | Eksplanatif |
| Sebab diketahui, cara mengatasinya belum | Perancangan |

Urutan itu bukan kebetulan. Penelitian perancangan yang dilakukan sebelum
fenomenanya dipahami menghasilkan artefak yang menyelesaikan persoalan yang
belum tentu ada — kekeliruan yang sama dengan yang dibahas mata kuliah
[Teknopreneur](../../teknopreneur/README.md) dalam konteks usaha.

### 1.2.3 Penelitian Perancangan di Informatika

Mayoritas Tugas Akhir Informatika termasuk jenis keempat. Jenis itu memiliki
tuntutan khas yang sering tidak dipenuhi.

| Tuntutan | Bila tidak dipenuhi |
|----------|---------------------|
| Kebutuhan yang dipenuhi berasal dari lapangan | Artefak menyelesaikan persoalan yang diasumsikan |
| Kriteria ditetapkan sebelum membangun | Kriteria disesuaikan dengan hasil |
| Ada pembanding yang wajar | Keberhasilan tidak bermakna |
| Kegagalan dilaporkan | Laporan menjadi promosi |
| Pengetahuan ditarik keluar dari artefak | Hasilnya hanya berlaku untuk artefak itu |

Baris terakhir adalah kelemahan khas penelitian perancangan mahasiswa.
Sebuah sistem yang berhasil dibangun menghasilkan sistem; yang dituntut
adalah **pengetahuan yang dapat dipakai orang lain** meskipun mereka tidak
memakai sistem itu.

Cara menarik keluar pengetahuannya:

| Bukan | Melainkan |
|-------|-----------|
| "Sistem ini berhasil" | "Pendekatan X berhasil pada keadaan Y" |
| "Akurasinya 94%" | "Akurasi turun tajam ketika Z, yang menunjukkan bahwa asumsi W tidak berlaku pada konteks ini" |
| "Pengguna puas" | "Kriteria yang paling menentukan penerimaan adalah V, bukan U yang selama ini diasumsikan" |

---

## 1.3 Memilih Wilayah Minat

### 1.3.1 Lima Kriteria

| Kriteria | Pertanyaan | Bila lemah |
|----------|------------|------------|
| **Ketertarikan yang bertahan** | Masihkah menarik pada bulan keenam? | Pekerjaan akan terbengkalai |
| **Kemungkinan ada kesenjangan** | Sudah banyakkah yang meneliti ini? | Kontribusi sulit dijelaskan |
| **Akses ke data atau subjek** | Dapatkah diperoleh dalam satu semester? | **Penelitian tidak dapat dijalankan** |
| **Bekal yang dimiliki** | Adakah mata kuliah yang membekali? | Waktu habis untuk belajar dasar |
| **Pembimbing yang tersedia** | Adakah dosen yang dapat membimbing? | Kualitas bimbingan terbatas |

Kriteria ketiga adalah penyaring terkuat dan paling sering diabaikan. Topik
yang menarik tetapi datanya tidak dapat diperoleh bukan topik yang dapat
dikerjakan — betapapun pentingnya persoalan itu.

> Cara memeriksanya konkret: sebutkan **siapa** yang memiliki data atau
> menjadi subjeknya, dan **sudahkah dihubungi**. Jawaban "nanti akan
> dihubungi" pada Minggu 1 sudah cukup; jawaban yang sama pada Minggu 8
> adalah tanda bahaya.

### 1.3.2 Menyempitkan Topik

Topik yang terlalu luas tidak dapat dijawab dalam satu penelitian.

```
Tingkat 1 (terlalu luas)
  Penerapan AI di pendidikan
        ↓  siapa? apa yang diamati?
Tingkat 2
  Pemakaian bantuan AI oleh dosen dalam menilai tugas
        ↓  apa yang belum diketahui?
Tingkat 3
  Alasan dosen berhenti memakai fitur penilaian otomatis
  pada sistem akademik kampus
```

| Ujian tingkat 3 | Bila "tidak" |
|-----------------|--------------|
| Dapatkah disebut siapa yang akan ditanya atau diamati? | Persempit lagi |
| Dapatkah disebut apa yang akan diukur atau digali? | Persempit lagi |
| Dapatkah dikerjakan dalam waktu yang tersedia? | Persempit lagi |

Penyempitan terasa seperti kehilangan. Sesungguhnya ia adalah satu-satunya
cara menghasilkan jawaban — pertanyaan luas menghasilkan jawaban kabur.

### 1.3.3 Tanda Topik yang Bermasalah

| Tanda | Sebabnya bermasalah |
|-------|---------------------|
| "Saya ingin membuat aplikasi untuk X" | Solusi mendahului pertanyaan |
| Topik masih pada tingkat 1 | Tidak dapat dijawab dalam satu penelitian |
| Data harus diperoleh dari lembaga yang belum dihubungi | Asumsi terbesar belum diuji |
| Tidak ada seorang pun yang terdampak | Arti penting sulit dijelaskan |
| Sudah sangat banyak diteliti tanpa sudut baru | Kesenjangannya tipis |
| Anda tidak dapat membayangkan meninggalkannya | Kemungkinan sudah diputuskan lebih dahulu |

Baris terakhir perlu penjelasan. Topik yang tidak dapat dibayangkan
ditinggalkan biasanya adalah topik yang sudah diputuskan sebelum bukti
dicari, dan sisa pekerjaan menjadi pencarian pembenaran.

Karena itu tugas pertama mata kuliah ini menuntut mahasiswa menuliskan:
**apa yang akan membuat saya meninggalkan topik ini?**

---

## 1.4 Peran Metodologi

### 1.4.1 Metodologi Bukan Daftar Prosedur

Metodologi sering dipahami sebagai kumpulan prosedur yang harus diikuti:
pilih metode, tentukan sampel, jalankan uji. Pemahaman itu menjelaskan
mengapa bab metodologi pada banyak Tugas Akhir terbaca seperti salinan buku
teks.

Metodologi sesungguhnya adalah **rangkaian keputusan yang harus
dipertanggungjawabkan**.

| Keputusan | Pertanggungjawabannya |
|-----------|----------------------|
| Mengapa pertanyaan ini yang diteliti? | Kesenjangan yang bersumber (Bab 2–3) |
| Mengapa rancangan ini? | Alternatif yang ditolak dan alasannya (Bab 8) |
| Mengapa subjek ini, sejumlah itu? | Perhitungan atau saturasi (Bab 9) |
| Mengapa ambang ini? | Kendala lapangan atau pustaka (Bab 12) |
| Mengapa simpulan ini dapat ditarik? | Data dan batasnya (Bab 11) |

Setiap baris pada kolom kanan adalah satu bab dalam buku ini. Bab metodologi
yang baik bukan bab yang menjelaskan apa itu uji t; ia bab yang menjelaskan
**mengapa uji t, dan apa yang terjadi bila asumsinya tidak terpenuhi**.

### 1.4.2 Mengapa di Semester 7

| Keadaan mahasiswa semester 7 | Akibatnya |
|------------------------------|-----------|
| Sedang atau akan mengambil Tugas Akhir | Keluaran kelas dapat menjadi proposal TA |
| Sudah menempuh Analisis Data Statistik | Dasar analisis tersedia |
| Sudah mengerjakan proyek RPL dan Teknopreneur | Terbiasa mengumpulkan kebutuhan pengguna |
| Waktu terbagi dengan KP atau magang | Beban mingguan harus realistis |

Mata kuliah ini **memakai** bekal itu, tidak mengulangnya. Perhitungan uji
statistik dibahas pada Probabilitas dan Statistik; wawancara kebutuhan
pengguna dilatih pada Teknopreneur dan RPL. Yang ditambahkan di sini adalah
**pertanggungjawaban atas pilihan-pilihan itu**.

---

## AI Corner — Bab 1

### Mata Kuliah Mode Eksplisit

Mata kuliah ini berstatus **tahap A→C, mode E (Eksplisit)**, pilar **AI
Research** pada AI Curriculum Infusion Matrix. Pemakaian AI dibahas terbuka
dan **dinilai** — termasuk kewajiban menyatakannya dalam Deklarasi AI yang
menjadi bagian setiap keluaran.

| Boleh pada tahap ini | Tidak boleh |
|----------------------|-------------|
| Meminta AI menjelaskan perbedaan jenis penelitian | Meminta AI memilih topik penelitian Anda |
| Meminta AI menyebutkan sudut pandang yang mungkin terlewat | Meminta AI membuat daftar judul untuk dipilih |
| Meminta AI menjelaskan istilah yang belum dikenal | **Meminta AI menyebutkan siapa yang sudah meneliti topik ini** |
| Meminta AI memeriksa apakah topik Anda sudah cukup sempit | Meminta AI menilai apakah topik Anda "bagus" |

### Mengapa Larangan Ketiga Paling Penting

Ditanya siapa yang sudah meneliti suatu topik, model bahasa menghasilkan
nama penulis, judul, dan tahun yang **terdengar benar**. Sebagian di
antaranya nyata; sebagian tidak.

Yang membuatnya berbahaya pada Bab 1: pada tahap ini mahasiswa belum
memiliki kebiasaan memverifikasi, dan sitasi yang masuk ke catatan sekarang
akan sulit dibedakan dari sitasi asli tiga bulan kemudian.

Pencarian literatur yang dapat diverifikasi dimulai pada Bab 3, dengan
prosedur yang dirancang khusus untuk menangkap sitasi yang tidak ada.

### Deklarasi AI Dimulai Sekarang

Setiap keluaran, dimulai dari tugas pertama, disertai Deklarasi AI —
**termasuk bila tidak memakai AI sama sekali**, yang dinyatakan demikian.

Mata kuliah ini tidak memberi nilai lebih kepada mahasiswa yang tidak memakai
AI. Yang dinilai adalah pemakaian yang beralasan, berbatas, dan diperiksa.
Bentuk deklarasinya ada pada
[RPS §I.3](../01-rps/rps-metodologi-penelitian.md).

### Latihan Reflektif

Ajukan kepada sebuah asisten AI: *"Sebutkan 5 topik penelitian Informatika
yang menarik untuk Tugas Akhir."*

Simpan jawabannya. Setelah menyelesaikan sintesis literatur pada Minggu 4,
buka kembali dan jawab:

1. Berapa topik dari daftar itu yang ternyata sudah sangat banyak diteliti?
2. Kesenjangan yang Anda temukan — adakah dalam daftar itu?
3. Apa yang membuat daftar itu terdengar meyakinkan padahal tidak bertumpu
   pada pustaka mana pun?

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan perbedaan pertanyaan pokok antara pengembangan dan penelitian.
2. Sebutkan empat jenis penelitian Informatika beserta pertanyaan khasnya.
3. Mengapa hipotesis yang tidak didukung data tetap merupakan hasil?
4. Sebutkan lima kriteria memilih wilayah minat penelitian.
5. Apa ujian satu kalimat yang memisahkan penelitian dari pengembangan?

### Tingkat Menengah

6. Untuk setiap pernyataan berikut, tentukan apakah ia menggambarkan
   penelitian atau pengembangan, dan tuliskan versi penelitiannya:
   - "Membangun aplikasi presensi berbasis pengenalan wajah"
   - "Menerapkan algoritma A untuk optimasi rute pengiriman"
   - "Membuat sistem informasi perpustakaan sekolah"

7. Persempit tiga topik berikut dari tingkat 1 ke tingkat 3, dan uji hasilnya
   dengan tiga pertanyaan §1.3.2:
   - "Keamanan siber di Indonesia"
   - "Pemakaian media sosial oleh remaja"
   - "Efisiensi basis data"

8. Ambil satu Tugas Akhir angkatan sebelumnya di program studi Anda. Jawab:
   pengetahuan apa yang dihasilkannya? Bila sulit dijawab, apa yang kurang
   dari rumusannya, dan bagaimana memperbaikinya tanpa mengubah apa yang
   dibangun?

9. Untuk satu artefak yang pernah Anda bangun (tugas kuliah atau proyek),
   rumuskan tiga pertanyaan penelitian yang pembangunan artefak itu dapat
   membantu menjawabnya.

### Tingkat Mahir

10. **Latihan lapangan.** Temui satu orang yang bekerja pada bidang yang Anda
    minati. Tanyakan: bagian mana dari pekerjaannya yang paling sering salah,
    dan apa yang sudah dicoba untuk mengatasinya. Catat jawabannya verbatim.
    Bandingkan dengan dugaan Anda sebelum bertemu, lalu rumuskan satu
    pertanyaan penelitian yang lahir dari percakapan itu.

11. Pilih satu makalah penelitian perancangan (*design science*) di bidang
    Anda. Analisis: apa artefaknya, kriteria apa yang dipakai, dari mana
    kriteria itu berasal, apa pembandingnya, dan **pengetahuan apa yang
    ditarik keluar dari artefak itu**. Nilai mana di antara kelimanya yang
    paling lemah dan mengapa.

12. Susun peta topik lengkap sesuai
    [Lokakarya 1](../04-labs/lab-01-peta-topik-dan-minat-penelitian.md),
    termasuk bagian "syarat meninggalkan". Untuk syarat itu, jelaskan:
    bagaimana Anda akan mengetahuinya, kapan, dan apa yang akan Anda lakukan
    bila syarat itu terpenuhi pada Minggu 6 — saat sebagian besar pekerjaan
    sudah dilakukan.

---

## Rangkuman

| Gagasan pokok | Rumusan singkat |
|---------------|-----------------|
| Pembeda penelitian | Pertanyaannya, bukan kerumitan pekerjaannya |
| Ujian satu kalimat | Apa yang kita ketahui sekarang yang tidak diketahui sebelumnya? |
| Temuan negatif | Tetap hasil, asalkan cara memperolehnya sahih |
| Urutan yang menentukan | Pertanyaan mendahului pembangunan; kriteria mendahului kode |
| Empat jenis penelitian | Ditentukan oleh keadaan pengetahuan, bukan dipilih menurut selera |
| Penelitian perancangan | Menuntut penarikan pengetahuan keluar dari artefak |
| Penyaring terkuat | Akses ke data atau subjek dalam satu semester |
| Penyempitan topik | Terasa seperti kehilangan; satu-satunya cara menghasilkan jawaban |
| Metodologi | Rangkaian keputusan yang harus dipertanggungjawabkan |
| Batas AI di bab ini | Tidak boleh menyebut penelitian terdahulu sebelum ada verifikasi |

---

## Referensi

1. Booth, W. C., Colomb, G. G., Williams, J. M., Bizup, J., & FitzGerald, W. T. (2016). *The Craft of Research* (4th ed.). University of Chicago Press.
2. Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in Information Systems Research. *MIS Quarterly*, 28(1), 75–105.
3. Creswell, J. W., & Creswell, J. D. (2023). *Research Design* (6th ed.). SAGE Publications.
4. Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., & Wesslén, A. (2012). *Experimentation in Software Engineering*. Springer.
5. Easterbrook, S., Singer, J., Storey, M. A., & Damian, D. (2008). Selecting Empirical Methods for Software Engineering Research. Dalam *Guide to Advanced Empirical Software Engineering*. Springer.
6. Gregor, S., & Hevner, A. R. (2013). Positioning and Presenting Design Science Research for Maximum Impact. *MIS Quarterly*, 37(2), 337–355.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul mingguan | [Minggu 1](../03-modules/week-01-penelitian-dalam-informatika.md) |
| Lokakarya | [Lokakarya 1](../04-labs/lab-01-peta-topik-dan-minat-penelitian.md) |
| Bab berikutnya | [Bab 2 — Masalah Penelitian dan Kesenjangan](bab-02-masalah-penelitian-dan-kesenjangan.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
