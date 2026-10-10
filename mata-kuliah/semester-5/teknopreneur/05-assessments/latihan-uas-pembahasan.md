---
id: uai-st52510002-latihan-uas-pembahasan
tipe: asesmen
judul: "Latihan UAS — Teknopreneur — Pembahasan dan Pedoman Skor"
kode_mk: ST52510002
nama_mk: Teknopreneur
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-09
---

# Pembahasan dan Pedoman Skor — Latihan UAS Teknopreneur

## Teknopreneur — ST52510002

> **Latihan UAS — bukan naskah UAS.** Pembahasan ini menyertai simulasi lengkap UAS Teknopreneur Ganjil 2026/2027 untuk berlatih: komposisi, durasi (90 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UAS. Naskah UAS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.
>
> **Kerjakan dulu [latihan UAS](latihan-uas.md) dalam 90 menit tanpa AI, tanpa catatan, dan tanpa membuka berkas ini.** Sesudahnya, nilai jawaban Anda per sub-butir dengan rubrik analitik, bandingkan dengan contoh jawaban *Kurang*, *Cukup*, dan *Baik* dari **tim fiktif** ([§1.6](#16-tim-fiktif-untuk-contoh-jawaban)), lalu pelajari bagian *Kesalahan umum*. UAS bersifat reflektif: tidak ada kunci jawaban yang dapat dihafal, karena setiap jawaban bertumpu pada proyek tim Anda sendiri. Yang dapat dipelajari dari berkas ini adalah **apa yang membuat refleksi bernilai tinggi** — kejadian bertanggal, bukti bersumber, pengakuan kekeliruan sendiri, perubahan yang benar-benar terjadi, dan rencana yang dapat diperiksa. Judul setiap butir mencantumkan skor · level Bloom · Sub-CPMK registri ([§1.5](#15-penandaan-butir)); cetak biru lengkap untuk dosen ada di [cetak biru butir dan panduan varian](latihan-uas-cetak-biru.md).
>
> Mata kuliah ST52510002 · Semester Ganjil 2026/2027 · persiapan UAS Minggu 16 · Skor total 100 · Penyusun: Tri Aji Nugroho, S.T., M.T.

---

## Daftar Isi

1. [Kaidah Umum Penilaian](#1-kaidah-umum-penilaian)
2. [Bagian A — Refleksi Berbasis Pengalaman](#2-bagian-a--refleksi-berbasis-pengalaman-40-poin)
3. [Bagian B — Analisis Tren](#3-bagian-b--analisis-tren-30-poin)
4. [Bagian C — Rencana Pengembangan Diri](#4-bagian-c--rencana-pengembangan-diri-30-poin)
5. [Rekap Skor dan Diagnosis Diri](#5-rekap-skor-dan-diagnosis-diri)
6. [Verifikasi Angka dengan Python](#6-verifikasi-angka-dengan-python)

---

## 1. Kaidah Umum Penilaian

### 1.1 Dari kaidah kisi-kisi ke unsur rubrik

Setiap sub-butir dinilai dengan **rubrik analitik**: beberapa unsur, masing-masing dengan skor penuh, sebagian, dan rendah. Tabel ini menunjukkan di mana kaidah penilaian [kisi-kisi UAS §5](kisi-kisi-uas.md#5-kaidah-penilaian) bekerja pada rubrik; bila tabel ini dan rubrik per butir berbeda, yang dipakai rubrik per butir.

| Kaidah kisi-kisi §5 | Unsur rubrik yang menerapkannya | Akibat pada skor unsur |
|---------------------|---------------------------------|------------------------|
| Refleksi berdasarkan **kejadian konkret dengan tanggal** | "minggu atau tanggal", "momen konkret", "perubahan dan rujukannya" | Penuh bila minggu atau tanggal disebut; kejadian umum ("waktu *Demo Day*") hanya sebagian |
| Menyebutkan **bukti dan sumbernya** | "sumber yang dapat ditelusuri", "bukti pembantah", "angka, keputusan, atau artefak tim" | Sumber umum ("dari wawancara", "data baru") hanya sebagian |
| **Mengakui kekeliruan sendiri** | A1(b) "peran Anda", A2 seluruhnya, C1(a) "keterbatasan diri sendiri"; pada B1(a) pengakuan peran sendiri boleh, tetapi tidak dituntut | Pengakuan yang spesifik menaikkan skor; menyalahkan anggota lain atau keadaan = 0 pada unsur itu |
| Rencana yang **dapat diperiksa** | A2(c) "bukti tertulis", B2(c) "ambang", C1(b) "luaran", C1(d) "tanda tertinggal" | Niat umum ("lebih rajin membaca", "lebih terbuka") = 0 |
| **Perubahan yang benar-benar terjadi** | A1(c) "perubahan yang benar-benar terjadi", B1(b) "perubahan dan rujukannya" | Perubahan yang baru direncanakan tetapi disajikan sebagai sudah terjadi = 0; keadaan tetap yang disebut perubahan = 0 |
| Menyebutkan **apa yang masih belum dipahami** | B1(b) keterbatasan bukti perubahan, B2(b) "yang belum dapat disimpulkan" | Penuh hanya bila spesifik untuk segmen tim |
| Pernyataan umum ("kami belajar banyak") | semua unsur | Tidak menambah skor |

### 1.2 Kejujuran refleksi dan perubahan yang benar-benar terjadi

1. **Mengakui kekeliruan menaikkan nilai** ([kisi-kisi §5.2](kisi-kisi-uas.md#52-tentang-kejujuran-dalam-refleksi)). Rubrik memberi poin khusus untuk pengakuan yang **spesifik** — apa yang Anda lakukan, kapan, dan mengapa — bukan untuk pengakuan umum ("kami kurang teliti").
2. **"Tidak ada yang berubah"** ([kisi-kisi §5.1](kisi-kisi-uas.md#51-peringatan-khusus)). Batang soal menyediakan **jalan keluar jujur** bagi kejadian yang tidak dimiliki setiap peserta, dengan skor maksimum yang ditetapkan di muka:
   - **A1** — angka yang tidak direvisi. Bila **bukti yang bertentangan** sudah ada tetapi angka tetap dipakai, (a) dinilai seperti biasa, sampai 6: mengakui bukti yang diabaikan adalah refleksi yang dihargai kisi-kisi §5.2. Bila **bukti pengujinya tidak pernah dikumpulkan**, unsur asumsi paling banyak 2 dari 3, sehingga (a) paling banyak 5.
   - **A1(c)** — keputusan yang tidak berubah, dinyatakan jujur beserta minggu, artefak, dan sebabnya: unsur perubahan paling banyak 1 dari 2 bila sebabnya bertumpu pada bukti (mis. revisi masih dalam rentang yang ditetapkan di muka), atau 0,5 bila sebab lain diakui jujur (mis. tenggat, enggan mengubah dokumen), sehingga (c) paling banyak 7 atau 6,5. Kesepadanan tetap dinilai menurut rubrik, sampai 4: penilaian jujur bahwa mempertahankan keputusan itu keliru — terlalu kecil — beserta alasannya bernilai penuh. Hanya klaim defensif — "tidak ada yang berubah", atau mempertahankannya "sudah benar sejak awal", tanpa sebab berbasis bukti — yang bernilai 0 pada unsur perubahan dan kesepadanan.
   - **Skor maksimum A1 per jalur** = (a) + (b) 6 + (c): (a) 6, atau 5 bila bukti pengujinya tidak pernah dikumpulkan; (c) 8 bila keputusan berubah, 7 bila tidak berubah dengan sebab berbasis bukti, atau 6,5 dengan sebab lain yang diakui jujur — sehingga A1 paling banyak 20, 19, 18,5, 18, atau 17,5.
   - **A2** — pendapat yang tidak pernah diuji: unsur bukti (a) paling banyak 0,5 dari 1, sehingga (a) paling banyak 5,5.
   - **B1(b)** — catatan yang paling mendekati perubahan: bagian perubahan paling banyak 0,5 dari 1, sehingga (b) paling banyak 5,5.

   **B1(a)** berbeda: bila semua lapis diperbarui sesuai irama, batang soal meminta lapis yang paling sedikit menghasilkan temuan yang dipakai beserta perkiraan jumlah temuan itu dibanding jumlah catatannya — **jalur alternatif bernilai penuh**, karena keadaan itu bukan kekurangan. Begitu pula **A2(b)**: bila bukti pembantah segera Anda terima, (b) menilai alasan Anda tidak menguji pendapat itu sebelum bukti datang — juga bernilai penuh. Klaim "semua keputusan kami tepat" tidak mendapat poin pada unsur adaptasi mana pun.
3. **Menyalahkan.** Jawaban yang menjelaskan kekeliruan dengan kesalahan anggota lain, narasumber, atau keadaan memperoleh 0 pada unsur penjelasan itu, walaupun keterangannya benar. Peran anggota lain boleh disebut sebagai fakta, tetapi penjelasan yang dinilai adalah tentang **diri Anda**.
4. **Kejujuran tidak dapat diganti panjang tulisan.** Jawaban panjang yang umum memperoleh skor lebih rendah daripada dua kalimat konkret.

### 1.3 Bukti dari ingatan dan pemeriksaan fakta

1. **Ujian ini *closed book*.** Angka perkiraan yang ditandai "±" dinilai sama dengan angka persis; bila kode kutipan tidak diingat, ciri narasumber dan minggu wawancaranya diterima sebagai rujukan yang dapat ditelusuri.
2. **Salah ingat yang jujur tidak mengurangi skor** (Petunjuk 6 lembar soal): minggu meleset satu, kode tertukar atau diganti ciri narasumber, atau angka perkiraan yang meleset sedikit tanpa mengubah kesimpulan — selama kejadiannya ada dalam berkas tim. Skor diberikan atas kekonkretan dan penalaran jawaban sebagaimana tertulis. **Fakta yang tidak dapat diverifikasi** — kejadian, kutipan, kode, angka, atau artefak (wawancara, uji, studio, *milestone*, jurnal keputusan, catatan pemindaian) yang bertentangan dengan berkas tim di luar salah ingat tadi, atau yang tidak ada padanannya di berkas tim — dinilai 0 pada unsurnya. Ini **bukan tuduhan pelanggaran**: catatan tim dapat saja tidak lengkap, mis. karena anggota lain lalai mencatat. Ketentuan integritas akademik ([Bab 14 §14.3.3](../06-buku-ajar/bab-14-proyek-akhir.md#1433-integritas-akademik)) baru dipakai bila ada petunjuk pemalsuan — mis. kejadian yang bertentangan dengan berkas tim dan tidak dapat dijelaskan sebagai salah ingat — dan sesudah mahasiswa serta timnya diberi kesempatan menunjukkan catatannya. **Pendapat, alasan, dan momen pribadi** yang wajar tidak tercatat — mis. pendapat yang Anda pertahankan dalam diskusi, alasan Anda menunda menerima bukti, atau saat keterbatasan Anda terasa — dinilai dari isinya, kecuali dibantah berkas tim. Saat menilai UAS, dosen dapat mencocokkan fakta (minggu, kode, angka, artefak) dengan berkas tim pada lembar mana pun — acak, dan setiap lembar yang faktanya meragukan. Kaidahnya sama untuk setiap lembar yang dicocokkan; proporsi lembar dan cara memilihnya ditetapkan dosen.
3. **Anggota satu tim** wajar menyebut fakta yang sama. Yang dinilai adalah refleksi pribadi — peran, penilaian, aturan, dan rencana — sehingga sub-butir A1(b), A2, dan C1 tidak dapat dijawab dengan kalimat yang sama oleh dua orang.
4. **Ketepatan isi proyek tidak dinilai ulang.** Apakah SOM, CAC, atau MVP tim Anda benar sudah dinilai pada studio dan *milestone*; di sini yang dinilai adalah cara Anda **membaca, merevisi, dan belajar** dari angka dan keputusan itu.

### 1.4 Cara menilai jawaban sendiri

1. **Nilai per unsur, lalu per sub-butir**, dan catat skornya pada [tabel rekap §5](#5-rekap-skor-dan-diagnosis-diri).
2. **Pembulatan:** skor unsur dicatat dalam kelipatan 0,5; total boleh berpecahan 0,5.
3. **Periksa fakta dulu.** Cocokkan minggu, kode, dan angka yang Anda tulis dengan catatan tim sebelum memberi skor. Salah ingat yang jujur ([§1.3](#13-bukti-dari-ingatan-dan-pemeriksaan-fakta) butir 2) tidak mengurangi skor — catat saja untuk dibaca ulang; fakta yang tidak dapat diverifikasi (bertentangan dengan catatan tim di luar salah ingat, atau tidak ada padanannya) bernilai 0 pada unsurnya — bukan tuduhan pelanggaran — sedangkan pendapat dan alasan pribadi yang wajar tidak tercatat dinilai dari isinya, kecuali dibantah catatan tim.
4. **Satu kekurangan dikurangi sekali.** Bila (b) atau (c) menyebut kembali kejadian yang sudah dinilai kurang di (a) — mis. tanpa sumber atau tanpa minggu — kekurangan itu hanya dikurangi pada (a); unsur (b) dan (c) dinilai dari penalarannya atas kejadian yang Anda tulis.
5. **Label tidak dihafal.** Istilah ("jenis bukti", "lapis", "pemicu") boleh diganti uraian yang setara maknanya.
6. **Jujur pada diri sendiri:** bila ragu di antara dua tingkat, ambil yang lebih rendah — atau minta teman setim membaca jawaban Anda dengan rubrik ini.

### 1.5 Penandaan butir

Judul tiap butir di §2–§4 memuat skor, level Bloom, Sub-CPMK, dan indikator registri. **Penandaan Sub-CPMK per butir menurut isi adalah bawaan sementara D-03(a); seluruh butir latihan ini menurut isinya mengukur `TEKNO-Sub-CPMKUAI32-1`, sehingga penandaan per butir sama dengan alokasi registri dan [RPS §G.1](../01-rps/rps-teknopreneur.md#g1-bobot-per-teknik-dan-sub-cpmk) — nilai UAS tetap tercatat 10% nilai akhir pada `TEKNO-Sub-CPMKUAI32-1`.** Indikator 2 ("merevisi asumsi bisnis setelah bukti pasar") diukur oleh Bagian A; indikator 1 ("menyusun rencana pembelajaran *entrepreneur* berbasis tren") oleh Bagian B dan C. Rinciannya ada pada [cetak biru](latihan-uas-cetak-biru.md).

Level Bloom pada judul butir adalah level butir itu sendiri. Tabel Informasi [Modul Minggu 16](../03-modules/week-16-uas-review-dan-ujian.md) mencantumkan **C5 → C6**; latihan ini — dan UAS — berada pada C4–C6: 24 poin C4 (menganalisis kejadian sendiri sebagai bahan refleksi), 43 poin C5, dan 33 poin C6. Pada sub-butir C4 dan C5, sebagian unsur menilai penyebutan fakta (nilai, sumber, minggu, keputusan, perubahan, rujukan) sebagai **prasyarat** — tanpa fakta itu, analisis atau penilaiannya tidak dapat diperiksa. Unsur fakta paling banyak setengah skor sub-butir, dan unsur analisis atau penilaian bernilai terbesar di sub-butirnya ([cetak biru, Level Bloom](latihan-uas-cetak-biru.md#level-bloom)).

### 1.6 Tim fiktif untuk contoh jawaban

> **Fiktif.** Tim, narasumber, angka, dan kejadian di bawah ini **rekaan** untuk contoh jawaban dan tidak menggambarkan tim mana pun. Contoh ditulis seolah-olah oleh **D.**, anggota fiktif tim itu. **Jangan menyalin contoh ini**: jawaban Anda harus tentang proyek Anda sendiri, dan jawaban yang menyalin tim fiktif dinilai 0.

| Minggu | Kejadian pada tim fiktif |
|:------:|--------------------------|
| 1 | P-00 — ranah: *kesulitan pengelola gelanggang bulu tangkis sewaan skala kecil (2–4 lapangan) di Kota Bekasi mengatur jadwal sewa*; dugaan awal: penyewa sulit memesan. Rencana pemindaian: **teknologi** — tarif layanan pesan untuk bisnis (halaman harga penyedia, bulanan); **perilaku** — pembayaran nontunai di klub olahraga amatir (pengumuman iuran di grup pesan dua klub bulu tangkis yang diikuti anggota tim, dua mingguan); **regulasi** — pajak daerah atas jasa sewa sarana olahraga (situs pemerintah kota, bulanan). Pemindaian pertama (Studio 1 Tantangan 3, keadaan awal), lapis perilaku: pengumuman iuran kedua klub meminta setoran tunai ke bendahara |
| 3–4 | Wawancara W01–W14 (semuanya pengelola gelanggang). W04-2: *"Yang bikin rugi itu klub yang batal jam enam sore, padahal sudah saya tolak orang lain."* W07-1: *"Penyewa saya kebanyakan klub, jadwalnya tetap tiap minggu. Pesan lewat HP juga sudah cukup."* Ditanya apakah mau berlangganan, 10 dari 14 pengelola menjawab "mau". P-01: arah berubah ke uang muka dan pembatalan oleh penyewa rutin |
| 5 | S-05: SOM = 140 gelanggang terjangkau × 10/14 × Rp75.000 × 12 bulan = Rp90 juta |
| 6 | Wawancara W15 (ketua klub penyewa rutin). W15-1: *"Mulai tahun ini anggota patungan lewat dompet digital, saya yang transfer ke gelanggang."* |
| 9 | S-07: model *unit economics* menganggap ±50% uang muka dibayar nontunai |
| 10 | Draf P-03: target *go-to-market* 30 gelanggang, diturunkan dari SOM S-05. MVP layanan manual dua minggu dimulai di 9 gelanggang (tim mengirim pengingat uang muka dan mencatat pembatalan). Uji tautan pemesanan: 3 dari 40 penyewa membuka tautan, tidak satu pun memesan |
| 11 | Akhir MVP: **2 dari 9 gelanggang membayar** Rp75.000 untuk bulan berikutnya, keduanya gelanggang 4 lapangan. Jurnal keputusan #09: target *go-to-market* 30 → 10 gelanggang; segmen dipersempit ke gelanggang 3–4 lapangan; harga tetap. S-05 dihitung ulang dengan proporsi 2/9: SOM ±Rp28 juta. Layanan berlanjut di kedua gelanggang yang membayar (gelanggang mitra) |
| 13 | S-13: tidak memakai model bahasa; pengingat berbasis aturan |
| 15 | *Demo Day*: penguji menanyakan cara menghitung CAC; D., yang menyusun S-07, tidak dapat menjelaskan mengapa waktu tim dihitung sebagai biaya |

Skor contoh dihitung dari rubrik per unsur; rinciannya ada di bawah setiap tabel contoh dan diperiksa ulang dengan Python pada [§6](#6-verifikasi-angka-dengan-python).

---

## 2. Bagian A — Refleksi Berbasis Pengalaman (40 poin)

### A1 [20] · C4–C5 · `TEKNO-Sub-CPMKUAI32-1` · indikator 2

#### Yang diukur

Indikator 2 registri — **merevisi asumsi bisnis setelah bukti pasar** — dengan kriteria **bukti adaptasi keputusan**. Butir ini menuntut tiga hal berurutan: menganalisis asumsi di balik sebuah angka dan cara bukti membantahnya (a), menilai jenis bukti yang membuat angka itu dipercaya lalu ditinggalkan serta cara tim — termasuk Anda — menerimanya (b), dan menunjukkan bahwa revisi angka benar-benar mengubah keputusan — dengan ukuran yang sepadan (c). Angka apa pun boleh dipilih; ketepatan perhitungan tim tidak dinilai di sini ([§1.3](#13-bukti-dari-ingatan-dan-pemeriksaan-fakta) butir 4). Tim yang tidak pernah merevisi angka memakai **jalan keluar** pada batang soal — angka yang tetap dipakai padahal ada bukti yang bertentangan dengannya, atau padahal bukti pengujinya tidak pernah dikumpulkan — dengan skor maksimum yang ditetapkan di muka ([§1.2](#12-kejujuran-refleksi-dan-perubahan-yang-benar-benar-terjadi) butir 2).

#### Bukti yang semestinya dirujuk

- Lembar SOM (S-05) atau model *unit economics* (S-07) tempat versi pertama muncul, beserta minggunya.
- Kode kutipan atau rekap wawancara yang menjadi dasar versi pertama.
- Catatan uji MVP, catatan harian, atau pembayaran nyata yang menjadi dasar versi terakhir.
- Entri jurnal keputusan ([Bab 14 §14.2.3](../06-buku-ajar/bab-14-proyek-akhir.md#1423-jurnal-keputusan)) atau bagian "apa yang berubah sejak Milestone 2" pada laporan P-03.

#### Rubrik analitik

| Sub | Unsur | Maks | Penuh | Sebagian | Rendah (0) |
|-----|-------|:----:|-------|----------|------------|
| (a) | Nilai kedua versi | 1 | Kedua nilai (perkiraan "±" sah); jalan keluar: nilai angka itu dan isi bukti yang bertentangan atau yang semestinya mengujinya (apa) | Satu versi saja = 0,5 | Tanpa angka |
| (a) | Sumber yang dapat ditelusuri | 1 | Kedua sumber dapat ditelusuri: kode kutipan, artefak (studio, *milestone*, catatan uji), atau perhitungan tim yang dapat ditunjuk; jalan keluar: sumber angka itu dan sumber bukti tadi (dari siapa), dinilai sama | Satu versi dapat ditelusuri, atau kedua versi bersumber umum ("dari wawancara", "uji MVP") = 0,5 | Tanpa sumber, atau hanya satu versi bersumber umum |
| (a) | Minggu atau tanggal | 1 | Per versi 0,5; jalan keluar: minggu angka itu dipakai dan minggu bukti muncul — atau, bila bukti tidak pernah dikumpulkan, kapan semestinya diperoleh — per bagian 0,5 | — | — |
| (a) | Asumsi yang dibantah | 3 | Asumsi dinyatakan sebagai pernyataan yang dapat salah **dan** dianalisis bagaimana bukti versi terakhir membantahnya — pada jalan keluar, bukti yang bertentangan dan diabaikan, dinilai sama | Asumsi dapat salah, tetapi cara bukti membantahnya tidak diuraikan = 2; asumsi samar ("kami terlalu optimistis") = 1; jalan keluar bila bukti pengujinya tidak pernah dikumpulkan — asumsi yang belum teruji, dinyatakan dapat salah, beserta bagaimana bukti itu akan mengujinya = 2 | Hanya mengulang angka |
| (b) | Jenis bukti kedua versi | 2 | Per versi 1: jenisnya disifatkan (pendapat tentang masa depan, perkiraan tim, angka AI tanpa rujukan, perilaku teramati, pembayaran nyata) | Hanya asal bukti ("dari wawancara", "dari uji MVP") tanpa menyifatkan = 0,5 per versi | — |
| (b) | Mana yang lebih dapat dipercaya | 2 | Alasan merujuk ciri bukti: peristiwa atau pendapat ([Bab 2 §2.1.2](../06-buku-ajar/bab-02-penemuan-masalah-dan-pelanggan.md#212-peristiwa-mengalahkan-pendapat)), jumlah orang ([Bab 5 §5.2.3](../06-buku-ajar/bab-05-ukuran-pasar-dan-kompetitor.md#523-memisahkan-asumsi-kuat-dan-lemah)) | Kesimpulan dengan alasan yang bukan ciri bukti ("lebih baru") atau tanpa alasan = 1 | Memilih pendapat di atas perilaku tanpa dasar |
| (b) | Penilaian atas cara versi pertama diterima, termasuk peran Anda | 2 | Mekanisme spesifik (tenggat, angka sesuai harapan, tidak ditandai lemah, angka AI tanpa rujukan diterima) **dan** peran Anda sendiri, **dinilai** menurut kekuatan buktinya — apa yang semestinya dilakukan; jalan keluar: mengapa angka itu tetap dipakai, dinilai sama | Mekanisme dan peran sendiri tanpa penilaian = 1,5; salah satunya saja = 1; umum tanpa peran sendiri ("kami kurang teliti") = 0,5 | Menyalahkan anggota lain, narasumber, atau keadaan |
| (c) | Keputusan yang bergantung pada angka | 1 | Keputusan konkret (target, segmen, harga, fitur, lanjut/ubah/hentikan) | Samar ("strategi kami") = 0,5 | Tidak disebut |
| (c) | Perubahan yang benar-benar terjadi | 2 | Sebelum → sesudah, keduanya konkret, dan sudah dijalankan | Perubahan tanpa keadaan sebelum atau tanpa rincian = 1; jalan keluar — keputusan tidak berubah, dinyatakan jujur dengan sebab yang bertumpu pada bukti (mis. revisi masih dalam rentang yang ditetapkan di muka) = 1, atau dengan sebab lain yang diakui jujur (mis. tenggat) = 0,5 | Perubahan yang baru direncanakan disajikan sebagai sudah terjadi; klaim defensif "tidak ada yang berubah" atau "sudah benar sejak awal" tanpa sebab berbasis bukti |
| (c) | Minggu dan artefak | 1 | Artefak (jurnal keputusan, laporan *milestone*, catatan uji) = 0,5; minggu = 0,5; jalan keluar: artefak dan minggu saat keputusan dipertahankan, dinilai sama | — | — |
| (c) | Kesepadanan | 4 | Penilaian (terlalu kecil / tepat / berlebihan) yang membandingkan besarnya revisi angka — bila angka tidak direvisi, kuatnya bukti tadi — dengan besarnya perubahan keputusan (mis. juga menimbang bagian keputusan yang tidak ikut berubah); untuk keputusan yang tidak berubah, penilaian apakah mempertahankannya tepat, dengan pembanding yang sama — termasuk pengakuan jujur bahwa mempertahankannya keliru | Penilaian dengan alasan umum = 2; penilaian tanpa alasan ("sudah tepat") = 0,5 | Tanpa penilaian; menilai keputusan yang tidak berubah "sudah benar sejak awal" atau "tepat" tanpa sebab berbasis bukti ([§1.2](#12-kejujuran-refleksi-dan-perubahan-yang-benar-benar-terjadi) butir 2) |

**Jalan keluar** ([§1.2](#12-kejujuran-refleksi-dan-perubahan-yang-benar-benar-terjadi) butir 2): angka yang tidak direvisi padahal bukti yang bertentangan sudah ada — (a) sampai 6; bukti pengujinya tidak pernah dikumpulkan — (a) paling banyak 5; keputusan yang tidak berubah — (c) paling banyak 7 (sebab berbasis bukti) atau 6,5 (sebab lain yang diakui jujur). A1 paling banyak 20, 19, 18,5, 18, atau 17,5 menurut jalurnya.

#### Contoh jawaban — tim fiktif ([§1.6](#16-tim-fiktif-untuk-contoh-jawaban))

| Tingkat | Jawaban | Skor |
|---------|---------|:----:|
| Kurang | (a) "SOM kami awalnya sekitar Rp90 juta, lalu turun jadi Rp28 juta karena ada data baru." (b) "Data baru lebih akurat. Anggota yang menghitung SOM kurang teliti." (c) "Kami belajar banyak bahwa angka itu penting. Keputusan kami tetap sama karena sudah benar sejak awal." | **2** |
| Cukup | (a) "Angka orang yang mau bayar langganan: awalnya 70% dari wawancara (Mg 4), lalu ternyata hanya 22% waktu uji MVP. Kami terlalu optimistis." (b) "Yang pertama dari wawancara, yang kedua dari uji MVP; yang kedua lebih benar karena lebih baru. Kami menerimanya karena kurang teliti." (c) "Target gelanggang di jurnal keputusan diubah dari 30 menjadi 10. Menurut saya sudah tepat." | **9,5** |
| Baik | (a) "Angka: proporsi gelanggang yang bersedia berlangganan. Versi pertama ±70% — 10 dari 14 pengelola menjawab 'mau' (wawancara Mg 3–4), dipakai pada SOM S-05 (Mg 5). Versi terakhir 2 dari 9 (±22%) yang benar-benar membayar Rp75.000 di akhir uji layanan manual (catatan uji, Mg 11). Asumsi yang dibantah: jawaban 'mau' berarti akan membayar — saat benar-benar diminta membayar, proporsinya tinggal ±sepertiga." (b) "Versi pertama pendapat tentang masa depan dari 14 orang; versi terakhir pembayaran nyata. Versi terakhir lebih dapat dipercaya karena berupa peristiwa, walaupun sampelnya hanya 9. Kami menerima versi pertama karena SOM harus selesai Mg 5 dan angkanya sesuai harapan; saya yang memasukkan 70% ke lembar SOM tanpa menandainya lemah — keliru: jawaban 'mau' semestinya diuji dulu dengan pembayaran." (c) "Angka itu dasar target *go-to-market* 30 gelanggang (draf P-03, Mg 10). Jurnal keputusan #09 (Mg 11): target menjadi 10 gelanggang dan segmen dipersempit ke gelanggang 3–4 lapangan. Target sepadan — angka turun ke ±sepertiga, target juga sepertiga — tetapi harga Rp75.000 tidak kami uji ulang, jadi perubahannya terlalu kecil pada harga." | **20** |

> **Rincian skor.** *Kurang:* (a) nilai 1 + sumber 0 (versi pertama tanpa sumber; versi terakhir "data baru" umum) + minggu 0 + asumsi 0 = 1; (b) jenis 0 + dipercaya 1 (tanpa alasan) + penerimaan 0 (menyalahkan anggota) = 1; (c) keputusan 0 + perubahan 0 ("sudah benar sejak awal" tanpa sebab berbasis bukti) + artefak 0 + kesepadanan 0 (sel Rendah: "sudah benar sejak awal" tanpa sebab berbasis bukti) = 0. *Cukup:* (a) 1 + 0,5 (kedua versi bersumber umum: "wawancara", "uji MVP") + 0,5 (minggu versi pertama saja) + 1 (asumsi samar) = 3; (b) 0,5 + 0,5 (asal tanpa jenis) + 1 ("lebih baru" bukan ciri bukti) + 0,5 (umum tanpa peran sendiri) = 2,5; (c) 1 + 2 + 0,5 (jurnal, tanpa minggu) + 0,5 (tanpa alasan) = 4. *Baik:* (a) 1 + 1 + 1 + 3 = 6; (b) 2 + 2 + 2 = 6; (c) 1 + 2 + 1 + 4 = 8.

#### Kesalahan umum

- **Memilih angka yang tidak pernah dipakai untuk keputusan** (mis. jumlah unduhan aplikasi pembanding). Unsur (c) lalu tidak dapat dijawab.
- **Menyebut sumber secara umum** ("dari wawancara", "dari riset") — tidak dapat ditelusuri. Sebut studio, *milestone*, catatan uji, atau kode kutipan.
- **Menilai versi terakhir lebih benar "karena lebih baru"**. Yang menentukan adalah jenis buktinya — pembayaran nyata mengalahkan jawaban "mau" ([Bab 2 §2.1.2](../06-buku-ajar/bab-02-penemuan-masalah-dan-pelanggan.md#212-peristiwa-mengalahkan-pendapat)).
- **Menyalahkan anggota yang menghitung** — skor unsur penilaian atas cara versi pertama diterima menjadi 0.
- **Mengarang revisi** karena merasa tidak punya angka yang direvisi. Pakai jalan keluar pada batang soal — angka yang tetap dipakai padahal ada bukti yang bertentangan, atau padahal bukti pengujinya tidak pernah dikumpulkan.
- **Menyajikan rencana sebagai perubahan** ("kami akan menurunkan harga") padahal belum dijalankan.
- **"Keputusan kami tetap karena sudah benar"** tanpa menunjukkan bahwa revisi angka sudah ditimbang. Bila keputusan memang tetap karena tenggat atau keengganan, katakan itu dan nilailah: pengakuan jujur dinilai, klaim "sudah benar" tanpa bukti tidak.

*Pelajari ulang:* [Bab 2 §2.1.2 (peristiwa mengalahkan pendapat)](../06-buku-ajar/bab-02-penemuan-masalah-dan-pelanggan.md#212-peristiwa-mengalahkan-pendapat) · [Bab 5 §5.2.3 (asumsi kuat dan lemah)](../06-buku-ajar/bab-05-ukuran-pasar-dan-kompetitor.md#523-memisahkan-asumsi-kuat-dan-lemah) · [Bab 8 §8.4.2 (mencatat perubahan model)](../06-buku-ajar/bab-08-model-bisnis-dan-proposisi-nilai.md#842-mencatat-perubahan-model) · [Bab 14 §14.2.3 (jurnal keputusan)](../06-buku-ajar/bab-14-proyek-akhir.md#1423-jurnal-keputusan)

---

### A2 [20] · C4–C6 · `TEKNO-Sub-CPMKUAI32-1` · indikator 2

#### Yang diukur

Adaptasi pada tingkat **pribadi**: kemampuan mengenali pendapat sendiri yang kalah oleh bukti dan menganalisis bagian yang dibantah (a), menilai dasar pendapat itu dan alasan diri sendiri menolak bukti — atau, bila bukti segera diterima, tidak menguji pendapat itu sebelum bukti datang — dapatkah dibenarkan (b), lalu **mengembangkan** (C6) aturan kerja yang mencegah hal serupa (c). Butir ini menerapkan langsung kaidah "mengakui kekeliruan sendiri" dan "menyalahkan anggota lain dinilai rendah" ([kisi-kisi §5](kisi-kisi-uas.md#5-kaidah-penilaian)). Mahasiswa yang tidak memiliki pendapat yang terbantah boleh memakai **jalan keluar** pada batang soal — pendapat yang dipertahankan tetapi tidak pernah diuji — agar tidak terdorong mengarang kejadian; jalan keluar ini kehilangan 0,5 poin pada unsur bukti (a) — (a) paling banyak 5,5 — karena menurut [kisi-kisi §5.1](kisi-kisi-uas.md#51-peringatan-khusus) tim yang benar-benar mewawancarai hampir selalu menemukan dugaan yang terbantah. Mahasiswa yang **segera menerima** bukti pembantahnya tidak memakai jalan keluar: (b) menilai alasan ia tidak menguji pendapat itu sebelum bukti datang, dengan skor maksimum sama.

#### Bukti yang semestinya dirujuk

- Catatan rapat atau catatan *sprint* tempat pendapat itu diajukan, dan keputusan yang sedang dibahas (mis. prioritas S-04, pilihan MVP, saluran *go-to-market*).
- Kutipan wawancara, hasil uji, atau angka yang membantah — dengan kode dan minggu.
- Catatan isu tim (P-05) atau jurnal keputusan, bila perbedaan pendapat itu tercatat.

#### Rubrik analitik

| Sub | Unsur | Maks | Penuh | Sebagian | Rendah (0) |
|-----|-------|:----:|-------|----------|------------|
| (a) | Pendapat Anda sendiri dan keputusannya | 1 | Pendapat diakui milik sendiri ("saya"), isinya konkret, beserta keputusan yang dibahas | Pendapat tim ("kami"), atau keputusan samar = 0,5 | Milik orang lain atau tidak ada |
| (a) | Bukti pembantah dan sumbernya | 1 | Bukti spesifik (kutipan, angka, hasil uji) dengan sumber yang dapat ditelusuri | Bukti tanpa rincian ("ternyata tidak dipakai saat uji") = 0,5; jalan keluar — bukti yang semestinya menguji pendapat itu, konkret (apa dan dari siapa) = 0,5 | Tanpa bukti |
| (a) | Minggu pendapat dan minggu bukti | 1 | Masing-masing 0,5 (jalan keluar: minggu pendapat; kapan semestinya diuji) | — | — |
| (a) | Bagian pendapat yang dibantah, dan bagaimana | 3 | Menunjuk bagian atau anggapan dalam pendapat yang dibantah dan cara bukti membantahnya (mis. bukti memperlihatkan perilaku yang berbeda dari yang diandaikan pendapat); jalan keluar: hasil bukti seperti apa yang akan membantah bagian mana, dinilai sama | Bukti disebut berlawanan dengan pendapat tanpa menunjuk bagian atau anggapan yang dibantahnya ("ternyata salah") = 1,5 | Bukti dan pendapat hanya didaftar, tanpa hubungan |
| (b) | Dasar pendapat waktu itu, dinilai | 3 | Dasar disebut (mis. dua kutipan pilihan sendiri, pengalaman pribadi, rancangan yang sudah dibuat) **dan** dinilai mutunya | Dasar disebut tanpa dinilai = 1,5; dinilai tanpa menyebut dasarnya ("dasarnya lemah") = 1 | Tidak ada |
| (b) | Alasan tidak segera menerima bukti, dinilai (bila bukti segera diterima: alasan tidak mengujinya sebelum bukti datang; jalan keluar: alasan tidak mengujinya) | 3 | Mekanisme pribadi yang spesifik (keterikatan pada rancangan, hanya membaca kutipan yang mendukung, enggan terlihat salah, tekanan tenggat) **dan** dinilai — dapat dibenarkan atau tidak, dengan alasan; bila bukti segera diterima, mekanisme yang membuat Anda tidak mengujinya lebih awal (mis. menganggapnya pasti karena pengalaman sendiri, mengira menguji bukan tugas saya) dinilai sama | Mekanisme spesifik tanpa dinilai = 2; mekanisme umum ("saya keras kepala", "kurang mendengarkan", "tidak terpikir") = 1 | Menyalahkan orang lain atau keadaan |
| (c) | Pemicu | 1,5 | Kapan aturan berlaku, dapat dikenali ("sebelum mengusulkan fitur dalam rapat tim") | Samar ("lain kali", "ke depan") = 0,5 | — |
| (c) | Tindakan | 2 | Tindakan konkret yang dapat dilakukan | Tindakan umum ("lebih banyak membaca data") = 1 | Sikap saja ("lebih terbuka", "lebih kompak") |
| (c) | Bukti tertulis | 1,5 | Catatan yang menunjukkan aturan dijalankan (mis. tabel kutipan pada catatan rapat bertanggal) | Catatan disebut tetapi tidak menunjukkan aturan dijalankan = 0,5 | — |
| (c) | Menjawab penyebab pada (b) | 1 | Aturan menyasar mekanisme yang diakui pada (b) | Sebagian = 0,5 | — |
| (c) | Penerapan balik pada kejadian (a) | 2 | Konkret: apa yang akan muncul lebih awal dan keputusan apa yang berbeda | Umum ("kami tidak akan salah lagi") = 0,5 | — |

#### Contoh jawaban — tim fiktif ([§1.6](#16-tim-fiktif-untuk-contoh-jawaban))

| Tingkat | Jawaban | Skor |
|---------|---------|:----:|
| Kurang | (a) "Tim kami salah memilih fitur karena ketua tim memaksakan pendapatnya." (b) "Seharusnya ketua tim mendengarkan anggota lain." (c) "Ke depan kami akan lebih kompak dan terbuka." | **0,5** |
| Cukup | (a) "Pada Mg 4 saya yakin aplikasi kami harus punya fitur pemesanan daring, tetapi ternyata penyewa tidak memakainya waktu uji MVP." (b) "Dasar saya waktu itu pengalaman saya sendiri memesan lapangan. Saya tidak segera menerima bukti karena kurang mendengarkan." (c) "Aturan: sebelum rapat, saya mencari kutipan yang mendukung dan yang membantah usulan saya." | **10** |
| Baik | (a) "Pada penyusunan prioritas S-04 (Mg 4) saya bersikeras pemesanan daring dengan jadwal lapangan waktu-nyata menjadi 'Must'. Pembantahnya W07-1 (Mg 4), lalu uji tautan pemesanan (catatan uji, Mg 10): 3 dari 40 penyewa membukanya, tidak satu pun memesan. Keduanya membantah anggapan saya bahwa penyewa kesulitan memesan: penyewa rutin berjadwal tetap dan cukup memesan lewat pesan." (b) "Dasar saya lemah: dua kutipan dari pengelola yang saya wawancarai sendiri dan pengalaman saya memesan lapangan — bukan pola dari 14 narasumber. Saya tidak segera menerima W07-1 karena sudah membuat rancangan layarnya pada Mg 3 dan sayang membuangnya, dan saya hanya membaca ulang kutipan yang mendukung — tidak dapat dibenarkan: rancangan bukan bukti tentang penyewa." (c) "Aturan: sebelum mengusulkan fitur dalam rapat tim, saya menulis tiga kutipan pendukung dan satu pembantah dari narasumber berbeda, lalu meminta satu anggota menambah pembantah; tabelnya dilampirkan pada catatan rapat bertanggal. Aturan ini menyasar kebiasaan membaca kutipan yang mendukung saja. Seandainya dipakai pada Mg 4, W07-1 muncul sebagai pembantah, pemesanan daring turun ke 'Could', dan waktu Mg 10 tidak terpakai untuk tautan pemesanan." | **20** |

> **Rincian skor.** *Kurang:* (a) pendapat 0 (milik ketua tim) + bukti 0 + minggu 0 + bagian yang dibantah 0 = 0; (b) 0 + 0 (menyalahkan) = 0; (c) pemicu 0,5 ("ke depan") + tindakan 0 (sikap) + 0 + 0 + 0 = 0,5. *Cukup:* (a) pendapat 0,5 (milik sendiri, tetapi keputusannya samar) + bukti 0,5 (tanpa rincian) + minggu 0,5 (minggu pendapat saja) + bagian yang dibantah 1,5 ("tetapi ternyata": berlawanan, tanpa menunjuk anggapan yang dibantah) = 3; (b) 1,5 (dasar — pengalaman sendiri — disebut tanpa dinilai) + 1 ("kurang mendengarkan", umum) = 2,5; (c) 1,5 + 2 + 0 (tanpa bukti tertulis — "mencari" tidak meninggalkan catatan) + 1 (menyasar "kurang mendengarkan") + 0 = 4,5. *Baik:* (a) 1 + 1 + 1 + 3 = 6; (b) 3 + 3 = 6; (c) 1,5 + 2 + 1,5 + 1 + 2 = 8.

#### Kesalahan umum

- **Menulis tentang pendapat tim atau pendapat anggota lain.** Butir ini meminta pendapat **Anda sendiri**; pendapat "kami" hanya mendapat sebagian kecil skor.
- **Menyalahkan** ("ketua tim memaksakan", "narasumber tidak jujur") — unsur penjelasan menjadi 0.
- **Aturan berupa sikap** ("lebih terbuka", "lebih mendengarkan"). Sikap tidak dapat diperiksa; tindakan dan catatannya dapat.
- **Aturan yang tidak menjawab penyebab di (b)** — mis. penyebabnya keterikatan pada rancangan, aturannya "mencatat semua keputusan".
- **Tanpa penerapan balik.** Aturan yang baik dapat ditunjukkan akan mengubah kejadian yang Anda ceritakan.
- **Mengarang kejadian** karena merasa tidak punya pendapat yang terbantah. Pakai jalan keluar pada batang soal — pendapat yang tidak pernah diuji — yang hanya kehilangan 0,5 poin; kejadian yang dikarang bernilai 0 ([§1.3](#13-bukti-dari-ingatan-dan-pemeriksaan-fakta)). Bila Anda segera menerima bukti pembantahnya, jangan mengarang penundaan: (b) menilai alasan Anda tidak mengujinya lebih awal, dengan skor yang sama.

*Pelajari ulang:* [Bab 3 §3.4.2 (menangani perbedaan penafsiran)](../06-buku-ajar/bab-03-persona-jtbd-konteks-penggunaan.md#342-menangani-perbedaan-penafsiran) · [Bab 2 §2.3.3 (ketika dugaan terbantah)](../06-buku-ajar/bab-02-penemuan-masalah-dan-pelanggan.md#233-ketika-dugaan-terbantah) · [Penutup — mengubah arah bukan kegagalan](../06-buku-ajar/penutup.md#ketiga-mengubah-arah-bukan-kegagalan)

---

## 3. Bagian B — Analisis Tren (30 poin)

### B1 [12] · C4–C5 · `TEKNO-Sub-CPMKUAI32-1` · indikator 1

#### Yang diukur

Kriteria **relevansi tren** dan materi *trend scanning*: kemampuan membandingkan rencana pemindaian dengan pelaksanaannya secara jujur (a), lalu menunjukkan **apa yang berubah sepanjang semester** pada tren yang dipantau tim dan dalam pemahaman sendiri — hal yang dijanjikan [Studio 1 Langkah 4](../04-labs/lab-01-pembentukan-tim-dan-pemindaian-tren.md#langkah-4-rencana-pemindaian-tren) dan [Modul 1 §1.3.3](../03-modules/week-01-lanskap-teknopreneurship.md#133-rencana-pembelajaran-semester) akan ditanyakan pada UAS — dengan menilai kekuatan bukti perubahan itu dan artinya bagi pemahaman sendiri, atau bagi angka atau keputusan tim (b). Perubahan boleh berasal dari catatan pemindaian atau dari temuan lapangan; percakapan dengan pelaku sering paling akurat ([Modul 1 §1.3.2](../03-modules/week-01-lanskap-teknopreneurship.md#132-sumber-pemindaian-untuk-konteks-indonesia)) tetapi jarang tercatat sebagai tren. Yang dinilai bukan banyaknya catatan, melainkan ketepatan membaca kekuatan dan kelemahan pemindaian tim sendiri.

#### Bukti yang semestinya dirujuk

- Formulir P-00 bagian 5 (tren, sumber, irama) dan dokumen pemindaian bersama — jumlah serta tanggal entri per lapis.
- Pembagian tugas pemindaian pada catatan *sprint*.
- Catatan pemindaian paling awal — keadaan awal pada [Studio 1 Tantangan 3](../04-labs/lab-01-pembentukan-tim-dan-pemindaian-tren.md#tantangan-3--pemindaian-pertama), bila tim mengerjakan tantangan tambahan itu — dan catatan terakhir untuk lapis yang sama; kode kutipan atau catatan uji yang memuat tanda perubahan, beserta minggunya.
- Angka atau keputusan tim yang tersentuh perubahan itu (mis. asumsi pada S-07, persyaratan S-04).

#### Rubrik analitik

| Sub | Unsur | Maks | Penuh | Sebagian | Rendah (0) |
|-----|-------|:----:|-------|----------|------------|
| (a) | Lapis, rencananya, dan perkiraan jumlah catatan dibanding rencana | 2,5 | Lapis + rencana P-00 untuk lapis itu (tren, sumber, irama) + perkiraan jumlah catatan dibanding rencana; jalur alternatif bila semua lapis diperbarui sesuai irama — lapis yang paling sedikit menghasilkan temuan yang dipakai + rencananya + perkiraan jumlah temuan itu dibanding jumlah catatannya — juga penuh. Rencana lapis lain tidak dinilai | Lapis + jumlah, tetapi rencana lapis itu tidak lengkap (tanpa sumber atau irama) atau tidak disebut = 2; lapis tanpa jumlah = 1 | "Semua baik" tanpa pembanding; tren yang bukan rencana P-00 tim (mis. daftar tren umum industri) |
| (a) | Penyebab | 3,5 | Penyebab pada cara tim atau Anda mengatur pemindaian (tanpa penanggung jawab, sumber tanpa tanggal atau pemberitahuan, irama yang tidak cocok dengan kecepatan berubah lapisnya — [Modul 1 §1.3.1](../03-modules/week-01-lanskap-teknopreneurship.md#131-tiga-lapis-tren)); peran Anda sendiri boleh disebut, tetapi tidak dituntut | Penyebab umum ("sibuk", "lupa") = 1 | Menyalahkan anggota lain |
| (b) | Perubahan dan rujukannya | 2 | Keadaan lebih dahulu → keadaan terakhir, keduanya konkret = 1; catatan, kode, atau ciri narasumber = 0,5; minggu = 0,5 | Hanya keadaan terakhir ("sekarang"), tanpa pembanding = 0,5 untuk bagian perubahan; jalan keluar — catatan yang paling mendekati, keadaannya konkret = 0,5 untuk bagian perubahan (catatan dan minggu tetap 0,5 + 0,5) | Tanpa keadaan lebih dahulu → terakhir, tanpa catatan, dan tanpa minggu (mis. pernyataan tren umum); keadaan tetap atau keluhan tetap disebut perubahan |
| (b) | Arti bagi pemahaman, angka, atau keputusan | 1,5 | Konkret dan dihubungkan dengan perubahan itu: apa yang dulu Anda kira dan sekarang Anda pahami, atau angka atau keputusan tim yang tersentuh; jalan keluar: artinya bagi cara tim memindai, dinilai sama | Umum ("kami jadi lebih paham pasar") = 0,5 | — |
| (b) | Kekuatan bukti perubahan | 2,5 | Menimbang kelebihan **dan** keterbatasan sumbernya dengan ciri bukti: kedekatan dengan segmen ([Modul 1 §1.3.2](../03-modules/week-01-lanskap-teknopreneurship.md#132-sumber-pemindaian-untuk-konteks-indonesia)), peristiwa atau pendapat ([Bab 2 §2.1.2](../06-buku-ajar/bab-02-penemuan-masalah-dan-pelanggan.md#212-peristiwa-mengalahkan-pendapat)), jumlah narasumber atau data ([Bab 5 §5.2.3](../06-buku-ajar/bab-05-ukuran-pasar-dan-kompetitor.md#523-memisahkan-asumsi-kuat-dan-lemah)), tanggal dan rentang pengamatan; jalan keluar: kelebihan dan keterbatasan catatan yang paling mendekati sebagai tanda perubahan — mengapa belum dapat disebut perubahan (mis. hanya satu titik waktu, sumber tanpa tanggal) — dinilai sama | Satu sisi saja, atau kelebihan saja tanpa keterbatasan = 1,5; kesimpulan tanpa alasan = 0,5 | Tanpa penilaian |

**Jalan keluar B1(b)** ([§1.2](#12-kejujuran-refleksi-dan-perubahan-yang-benar-benar-terjadi) butir 2): paling banyak 0,5 + 0,5 + 0,5 + 1,5 + 2,5 = **5,5 dari 6**. B1(a) tidak memiliki jalan keluar: jalur alternatifnya bernilai penuh.

#### Contoh jawaban — tim fiktif ([§1.6](#16-tim-fiktif-untuk-contoh-jawaban))

| Tingkat | Jawaban | Skor |
|---------|---------|:----:|
| Kurang | (a) "Tren yang kami pantau adalah AI, digitalisasi UMKM, dan ekonomi digital. Semuanya kami perbarui dengan baik." (b) "Digitalisasi UMKM terus meningkat sehingga usaha kami punya peluang besar." | **0,5** |
| Cukup | (a) "Kami memantau tarif layanan pesan, pembayaran digital, dan aturan pajak. Yang paling jarang diperbarui regulasi, karena kami sibuk dengan wawancara dan MVP." (b) "Ketua klub yang kami wawancarai pada Mg 6 bilang anggota sekarang patungan lewat dompet digital. Jadi pembayaran di segmen kami makin digital. Itu dapat dipercaya karena langsung dari pelaku." | **5,5** |
| Baik | (a) "Lapis regulasi paling jarang diperbarui. Rencana P-00: pajak daerah atas jasa sewa sarana olahraga, dari situs pemerintah kota, bulanan; catatannya hanya 1 (Mg 2) dari ±4 yang direncanakan. Penyebabnya, tugas itu tertulis 'bergiliran' sehingga tidak ada penanggung jawab, dan situs itu tidak memberi tanda bila ada aturan baru, sehingga irama bulanan terasa sia-sia." (b) "Lapis perilaku. Catatan pemindaian Mg 1 (grup pesan dua klub): iuran disetor tunai ke bendahara. W15-1 (Mg 6, ketua klub): kini anggota patungan lewat dompet digital, lalu ketua mentransfer ke gelanggang. Pemahaman saya berubah: pembayar gelanggang adalah ketua klub yang sudah nontunai — karena itu S-07 (Mg 9) menganggap ±50% uang muka nontunai. Bukti ini kuat untuk arah: langsung dari segmen dan berupa kebiasaan yang sudah berjalan, bukan rencana. Lemah untuk besarnya: baru satu narasumber, dan catatan awal hanya dari dua klub." | **12** |

> **Rincian skor.** *Kurang:* (a) lapis dan rencana 0 (daftar tren umum industri, bukan rencana P-00 tim; "semuanya baik" tanpa pembanding) + penyebab 0 = 0; (b) perubahan 0 (tanpa keadaan lebih dahulu → terakhir, tanpa catatan, dan tanpa minggu — dinilai dari (b) sendiri, bukan karena kekurangan (a) diulang) + arti 0,5 ("punya peluang besar", umum) + kekuatan bukti 0 = 0,5. *Cukup:* (a) 1 (lapis regulasi tanpa jumlah) + 1 ("sibuk") = 2; (b) perubahan 0,5 ("sekarang", tanpa keadaan sebelumnya) + ciri narasumber 0,5 + minggu 0,5 = 1,5; arti 0,5 ("makin digital", umum); kekuatan bukti 1,5 (kelebihan saja); jumlah (b) = 3,5. *Baik:* (a) 2,5 + 3,5 = 6; (b) 2 + 1,5 + 2,5 = 6.

#### Kesalahan umum

- **Menulis daftar tren umum industri** ("AI", "ekonomi digital") alih-alih tren yang benar-benar dipantau tim — [kisi-kisi §7](kisi-kisi-uas.md#7-yang-diuji-dan-yang-tidak) menyebutnya tidak diuji; unsur lapis dan rencana (a) bernilai 0. Pernyataan tren umum pada (b) juga tidak mendapat skor perubahan, tetapi karena (b) sendiri tidak memuat keadaan lebih dahulu → terakhir, catatan, dan minggu — bukan karena kekurangan (a) dikurangi lagi ([§1.4](#14-cara-menilai-jawaban-sendiri) butir 4).
- **"Semua lapis kami perbarui dengan baik"** tanpa jumlah catatan. Bila memang demikian, soal memberi jalan lain: lapis yang paling sedikit menghasilkan temuan yang dipakai, dan berapa temuan itu dibanding jumlah catatannya.
- **Penyebab "sibuk"**. Semua tim sibuk; yang membedakan adalah bagaimana pemindaian diatur — siapa, kapan, dipicu oleh apa.
- **Menyebut keadaan sekarang tanpa keadaan sebelumnya**, atau menyebut keluhan tetap sebagai tren (mis. "pengelola selalu repot mencatat"). Tren adalah **perubahan**; tunjukkan catatan lebih dahulu dan catatan terakhir.
- **Menilai bukti perubahan pasti benar** tanpa menyebut keterbatasannya (satu narasumber, satu wilayah, sumber tanpa tanggal).
- **Mengarang perubahan** karena catatan tim tidak memuatnya. Batang soal memberi jalan keluar — catatan yang paling mendekati, kekuatan dan keterbatasannya sebagai tanda perubahan, dan artinya bagi cara tim memindai — yang hanya kehilangan 0,5 poin; perubahan yang dikarang bernilai 0.

*Pelajari ulang:* [Modul 1 §1.3 (pemindaian tren dan *learning agility*)](../03-modules/week-01-lanskap-teknopreneurship.md#13-pemindaian-tren-dan-learning-agility) · [Modul 1 §1.3.3 (rencana pemindaian dinilai pada UAS)](../03-modules/week-01-lanskap-teknopreneurship.md#133-rencana-pembelajaran-semester) · [Studio 1 Langkah 4 (rencana pemindaian tren)](../04-labs/lab-01-pembentukan-tim-dan-pemindaian-tren.md#langkah-4-rencana-pemindaian-tren) dan [Tantangan 3 (keadaan awal)](../04-labs/lab-01-pembentukan-tim-dan-pemindaian-tren.md#tantangan-3--pemindaian-pertama) · [Bab 5 §5.2.3 (kekuatan bukti)](../06-buku-ajar/bab-05-ukuran-pasar-dan-kompetitor.md#523-memisahkan-asumsi-kuat-dan-lemah)

---

### B2 [18] · C5–C6 · `TEKNO-Sub-CPMKUAI32-1` · indikator 1

#### Yang diukur

Kriteria **relevansi tren** pada bahan yang sama untuk semua peserta: memilah kliping menurut dampaknya pada usaha **sendiri** (a), menilai kekuatan bukti sebuah kliping sebelum bertindak (b), dan **menyusun** pemicu keputusan yang ditetapkan di muka (c) — gagasan yang sama dengan kolom "tanda awal" daftar risiko ([Modul 7 §7.6.2](../03-modules/week-07-unit-economics-harga-risiko.md#762-format-daftar-risiko)) dan kriteria yang ditetapkan sebelum pengujian ([Bab 9 §9.3.1](../06-buku-ajar/bab-09-mvp-merancang-yang-paling-sedikit.md#931-ditetapkan-sebelum-bukan-sesudah)). Pilihan kliping pada (a) **bebas**: pilihan apa pun dinilai penuh bila alasannya bertumpu pada angka, keputusan, atau artefak tim.

#### Kelemahan bukti yang dapat dikenali pada setiap kliping

| Kliping | Yang sebenarnya dinyatakan | Kelemahan sumber atau cara memperoleh keterangan | Contoh yang belum dapat disimpulkan |
|---------|----------------------------|-----------------------------------------------|-------------------------------------|
| K1 | Tarif paket usaha kecil turun ±40% **mulai bulan depan**; kuota gratis untuk pengembang **dihapus** | Baru pengumuman — belum berlaku dan belum teruji pada biaya tim, sehingga baru berupa tanda awal ([Modul 7 §7.6.2](../03-modules/week-07-unit-economics-harga-risiko.md#762-format-daftar-risiko)); "membuka AI bagi jutaan UMKM" adalah pernyataan penyedia tentang layanannya sendiri, setara janji pemasaran di situs produk ([Bab 5 §5.3.3](../06-buku-ajar/bab-05-ukuran-pasar-dan-kompetitor.md#533-riset-kompetitor-yang-benar)), bukan hasil pengukuran | Biaya per pengguna tim sesudah perubahan; apakah tarif baru bertahan |
| K2 | 61% dan 18% dari **220 pengisi** — anggota asosiasi di tiga kota besar | Pesertanya bukan segmen tim: anggota asosiasi pedagang di tiga kota besar, yang datang sendiri lewat surel dan grup pesan sehingga cenderung yang sudah melek digital — mutu bukti bergantung pada sumber peserta ([Bab 9 §9.4.1](../06-buku-ajar/bab-09-mvp-merancang-yang-paling-sedikit.md#941-memilih-peserta)); "menerima" pembayaran belum berarti sering dipakai | Proporsi di segmen tim (kota, ukuran usaha, bukan anggota asosiasi) |
| K3 | **Rancangan** peraturan wali kota untuk **satu kota**, dalam uji publik | Isinya dapat berubah selama uji publik; tanggal berlaku belum ditetapkan; hanya berlaku di kota itu | Apakah kota tim terkena; berapa mitra tim yang sudah memiliki NIB ([Bab 11 §11.1.2](../06-buku-ajar/bab-11-tata-kelola-legalitas-etika.md#1112-perizinan-dasar)) |

**Kelemahan yang diterima.** Satu kelemahan sudah cukup untuk skor penuh unsur kelemahan B2(b). Yang diterima adalah kelemahan yang bertumpu pada bahan ajar — peristiwa atau pendapat ([Bab 2 §2.1.2](../06-buku-ajar/bab-02-penemuan-masalah-dan-pelanggan.md#212-peristiwa-mengalahkan-pendapat)), jenis dan jumlah sumber ([Bab 5 §5.2.1–§5.2.3](../06-buku-ajar/bab-05-ukuran-pasar-dan-kompetitor.md#523-memisahkan-asumsi-kuat-dan-lemah)), janji penyedia ([Bab 5 §5.3.3](../06-buku-ajar/bab-05-ukuran-pasar-dan-kompetitor.md#533-riset-kompetitor-yang-benar)), sumber peserta ([Bab 9 §9.4.1](../06-buku-ajar/bab-09-mvp-merancang-yang-paling-sedikit.md#941-memilih-peserta)), dan pengumuman sebagai tanda awal ([Modul 7 §7.6.2](../03-modules/week-07-unit-economics-harga-risiko.md#762-format-daftar-risiko)) — termasuk yang tercantum pada tabel; kelemahan setara lain yang alasannya tepat juga diterima.

**Catatan untuk (a), bukan kelemahan bukti:** dampak K1 **dua arah** — tarif turun, tetapi kuota gratis dihapus, sehingga tim yang selama ini memakai kuota gratis justru mulai membayar. Ini implikasi yang dinilai pada B2(a), bukan kelemahan sumber yang dinilai pada B2(b).

#### Bukti yang semestinya dirujuk

- Angka atau keputusan tim yang tersentuh: model *unit economics* (S-07), persyaratan (S-04), rencana *go-to-market* (P-03), keputusan pemakaian AI (S-13), audit etika dan kepatuhan (S-12).
- Untuk (c): catatan tim yang dapat dipakai sebagai sumber ukuran (catatan transaksi, catatan uji, dokumen pemindaian) beserta iramanya.

#### Rubrik analitik

| Sub | Unsur | Maks | Penuh | Sebagian | Rendah (0) |
|-----|-------|:----:|-------|----------|------------|
| (a) | Paling besar dan bagian usaha yang tersentuh | 2,5 | Mekanisme ke usaha sendiri dengan angka, keputusan, atau artefak tim | Mekanisme tanpa angka atau artefak = 1,5; umum ("akan memengaruhi usaha kami") = 0,5 | Tidak dipilih |
| (a) | Paling kecil dan alasannya | 1,5 | Alasan merujuk usaha sendiri (keputusan, angka, atau artefak) | Alasan umum = 0,5 | Tidak dipilih |
| (a) | Alasan perbandingan | 2 | Mengapa yang satu lebih besar daripada yang lain (besarnya dampak, kedekatan waktu, kepastian) | Peringkat dinyatakan — masing-masing boleh dengan alasannya sendiri — tetapi tanpa alasan mengapa yang satu lebih besar daripada yang lain ("K3 jelas lebih penting") = 1 | Hanya satu kliping yang dipilih |
| (b) | Yang sebenarnya dinyatakan | 1 | Isi pokok kliping — apa yang diumumkan, diukur, atau diatur, dan untuk siapa — disebut tepat tanpa diperluas (lihat tabel di atas) | — | Diperluas atau tidak disebut |
| (b) | Sumber dan cara memperoleh keterangan | 2 | Satu kelemahan khas kliping itu dikenali dengan tepat (tabel di atas; satu sudah cukup) | Sumber disebut tanpa kelemahannya = 0,5 | Keliru menilai (mis. "dari pemerintah, jadi pasti berlaku") |
| (b) | Yang belum dapat disimpulkan untuk segmen sendiri | 2 | Spesifik untuk segmen tim | Umum ("belum pasti") = 0,5 | — |
| (c) | Ukuran | 1,5 | Dapat diukur dan berkaitan dengan kliping | Samar = 0,5 | — |
| (c) | Sumber dan irama | 1,5 | Sumber konkret = 1; irama = 0,5 | Sumber umum ("berita") = 0 untuk sumber | — |
| (c) | Ambang | 1,5 | Angka atau keadaan yang jelas | Samar ("bila meningkat") = 0,5 | — |
| (c) | Keputusan yang berubah | 1,5 | Keputusan konkret pada usaha tim | Umum ("menyesuaikan") = 0,5 | — |
| (c) | Mendahului dampak | 1 | Ukuran dapat diperiksa sebelum dampak terasa | — | Ukuran yang baru terbaca sesudah dampak terjadi (mis. "bila peraturan sudah berlaku") |

#### Contoh jawaban — tim fiktif ([§1.6](#16-tim-fiktif-untuk-contoh-jawaban))

| Tingkat | Jawaban | Skor |
|---------|---------|:----:|
| Kurang | (a) "K1 paling besar karena AI makin murah sehingga usaha kami bisa lebih canggih." (b) "Semua sumber cukup terpercaya karena dimuat di kliping." (c) "Kami akan terus mengikuti perkembangan harga AI." | **1** |
| Cukup | (a) "K3 paling besar karena kalau aplikasi hanya boleh bermitra dengan usaha ber-NIB, banyak gelanggang kecil tidak bisa ikut. K1 paling kecil karena kami tidak memakai AI." (b) "K3 masih rancangan dan belum ada tanggal berlakunya, jadi belum pasti." (c) "Kami akan memantau berita tentang peraturan ini setiap bulan dan menyesuaikan diri bila sudah berlaku." | **9,5** |
| Baik | (a) "Paling besar: K2. Layanan kami mengingatkan dan mencatat uang muka; model *unit economics* S-07 menganggap ±50% uang muka dibayar nontunai, dan beban pencatatan manual kami bergantung pada angka itu. Paling kecil: K1 — sejak S-13 (Mg 13) kami tidak memakai model bahasa; pengingat kami berbasis aturan. K2 lebih besar karena menyentuh pembayaran yang setiap hari kami tangani, sedangkan K1 baru berarti bila keputusan S-13 dibatalkan." (b) "K2 hanya menyatakan bahwa 61% dari 220 anggota yang mengisi survei menerima pembayaran kode QR. Pengisinya memilih sendiri lewat surel dan grup pesan, jadi cenderung yang sudah melek digital, dan hanya di tiga kota besar. Yang belum dapat disimpulkan: proporsi di gelanggang kecil Kota Bekasi, dan seberapa sering kode QR benar-benar dipakai — menerima belum tentu dipakai." (c) "Ukuran: berapa ketua klub penyewa rutin di gelanggang mitra yang meminta tautan kode QR saat menerima pengingat uang muka. Sumber: catatan balasan pengingat, direkap tiap Senin. Ambang: ≥ 25% penerima pengingat, empat minggu berturut-turut. Keputusan: pengingat diberi tautan pembayaran kode QR dan pencatatan manual dihentikan. Permintaan itu muncul sebelum cara membayar dan beban pencatatan kami berubah." | **18** |

> **Rincian skor.** *Kurang:* (a) 0,5 (umum, dan bertentangan dengan keputusan tim sendiri) + 0 (tidak dipilih) + 0 (hanya satu kliping) = 0,5; (b) 0 + 0 (keliru menilai) + 0 = 0; (c) ukuran 0,5 (samar) + 0 + 0 + 0 + 0 = 0,5. *Cukup:* (a) 1,5 (mekanisme tanpa angka atau artefak) + 1,5 (keputusan tim tidak memakai AI) + 1 (peringkat dengan alasan masing-masing, tanpa alasan mengapa K3 lebih besar daripada K1) = 4; (b) dinyatakan 0 (isi kliping tidak disebut) + kelemahan 2 (rancangan, belum ada tanggal berlaku) + 0,5 ("belum pasti") = 2,5; (c) ukuran 0,5 + sumber 0 ("berita") dan irama 0,5 + ambang 1,5 ("sudah berlaku" keadaan yang jelas) + keputusan 0,5 + mendahului 0 = 3. *Baik:* (a) 2,5 + 1,5 + 2 = 6; (b) 1 + 2 + 2 = 5; (c) 1,5 + 1,5 + 1,5 + 1,5 + 1 = 7.

#### Kesalahan umum

- **Memilih kliping karena "paling penting secara umum"**, bukan karena dampaknya pada angka atau keputusan tim sendiri.
- **K1 dibaca "AI makin murah"** — padahal kuota gratis dihapus, sehingga tim yang selama ini memakai kuota gratis justru mulai membayar.
- **K2 diterima sebagai gambaran segmen sendiri** tanpa melihat siapa yang mengisi survei.
- **K3 dianggap sudah berlaku** karena berasal dari pemerintah.
- **Pemicu yang terlambat** — "bila peraturan sudah berlaku", "bila biaya kami sudah naik". Pemicu yang berguna terbaca **sebelum** dampaknya terasa.
- **Ambang tanpa angka** ("bila banyak yang memakai") — tidak dapat diperiksa.

*Pelajari ulang:* [Modul 7 §7.6.2 (tanda awal pada daftar risiko)](../03-modules/week-07-unit-economics-harga-risiko.md#762-format-daftar-risiko) · [Bab 5 §5.3.3 (janji pemasaran vs pemakaian nyata)](../06-buku-ajar/bab-05-ukuran-pasar-dan-kompetitor.md#533-riset-kompetitor-yang-benar) · [Bab 9 §9.4.1 (sumber peserta menentukan mutu bukti)](../06-buku-ajar/bab-09-mvp-merancang-yang-paling-sedikit.md#941-memilih-peserta) · [Bab 9 §9.3.1 (ditetapkan sebelum, bukan sesudah)](../06-buku-ajar/bab-09-mvp-merancang-yang-paling-sedikit.md#931-ditetapkan-sebelum-bukan-sesudah) · [Bab 12 §12.3.2 (biaya yang sering terlewat)](../06-buku-ajar/bab-12-produk-berbasis-ai.md#1232-biaya-yang-sering-terlewat) · [Bab 11 §11.1.2 (perizinan dasar)](../06-buku-ajar/bab-11-tata-kelola-legalitas-etika.md#1112-perizinan-dasar)

---

## 4. Bagian C — Rencana Pengembangan Diri (30 poin)

### C1 [30] · C4–C6 · `TEKNO-Sub-CPMKUAI32-1` · indikator 1

#### Yang diukur

Indikator 1 registri — **menyusun rencana pembelajaran *entrepreneur* berbasis tren** — dengan kriteria **kejelasan pembelajaran** dan **relevansi tren**. Batasan yang dicetak di soal (semester berikutnya, paling banyak 3 jam per minggu) membuat rencana dapat diperiksa kelayakannya. Butir ini menilai empat langkah: menemukan kesenjangan dari kejadian nyata (a), merancang cara menutupnya sebagai urutan langkah yang saling bergantung dengan luaran yang dapat diperiksa (b), mengaitkannya dengan tren (c), dan menyiapkan cara mengubah rencana bila tertinggal (d) — wujud pola pikir adaptif pada diri sendiri.

#### Bukti yang semestinya dirujuk

- Momen bertanggal: umpan balik penguji *Demo Day* (P-04), catatan wawancara yang buntu, revisi model S-07, catatan uji MVP yang tertunda.
- Catatan pemindaian tim atau kliping B2 untuk (c).
- Untuk (b) dan (d): nama kegiatan, sumber belajar, bulan, jam per minggu, alasan urutan langkah, bentuk luaran, dan pemeriksanya.

#### Rubrik analitik

| Sub | Unsur | Maks | Penuh | Sebagian | Rendah (0) |
|-----|-------|:----:|-------|----------|------------|
| (a) | Momen konkret | 2 | Minggu + kejadian spesifik | Kejadian disebut umum ("waktu *Demo Day*") = 1 | Tidak ada |
| (a) | Keterbatasan diri sendiri | 1,5 | Milik sendiri dan spesifik | Milik sendiri tetapi umum = 1; keterbatasan tim = 0,5 | Menyalahkan orang lain |
| (a) | Keterampilan yang kurang, dihubungkan dengan kejadian | 2,5 | Spesifik, dan dianalisis mengapa kekurangan itu — bukan hal lain — yang menghambat pada kejadian itu | Spesifik tanpa dihubungkan dengan kejadian = 1,5; umum ("komunikasi", "*public speaking*") = 1 | Tidak disebut |
| (b) | Langkah dan urutannya | 2,5 | Kegiatan konkret per langkah (apa dan berapa banyak), dengan alasan urutan — langkah sebelumnya menjadi prasyarat langkah berikutnya | Kegiatan konkret tanpa alasan urutan = 1,5; kegiatan dapat dikenali tetapi tanpa rincian = 1 | Niat umum ("lebih rajin membaca") |
| (b) | Sumber belajar | 1,5 | Konkret dan dapat diakses (bab atau buku tertentu, kursus tertentu, data atau orang) | Jenis sumber umum ("buku bisnis", "kursus daring") = 0,5 | — |
| (b) | Bulan dan beban dalam 3 jam per minggu | 2 | Setiap langkah berbulan dan berbeban ≤ 3 jam per minggu | Beban tanpa bulan, atau bulan tanpa beban = 1; melebihi 3 jam per minggu = 0,5 | — |
| (b) | Luaran yang dapat diperiksa | 2,5 | Bentuk luaran + pemeriksanya | Bentuk tanpa pemeriksa = 1,5 | Tidak ada |
| (b) | Koherensi dengan (a) | 1,5 | Rencana menyasar keterampilan pada (a) | Sebagian = 0,5 | — |
| (c) | Tren | 1,5 | Dari catatan pemindaian tim atau kliping B2 | Tren umum industri ("AI makin penting") = 0,5 | — |
| (c) | Arah dan alasannya | 2 | Lebih atau kurang bernilai, dengan alasan yang menghubungkan tren dan keterampilan | Alasan tipis atau tidak menyentuh keterampilan = 1 | — |
| (c) | Penilaian atas rencana (b) | 2,5 | Penyesuaian konkret, atau alasan mengapa tidak perlu disesuaikan | Penilaian tanpa penyesuaian atau alasan = 1 | Tidak ada |
| (d) | Waktu tinjau | 1,5 | Tanggal atau bulan di tengah semester | Periodik umum ("setiap bulan") = 1 | — |
| (d) | Tanda tertinggal | 2,5 | Dapat diperiksa (jumlah, luaran) | Samar ("merasa belum bisa") = 0,5 | — |
| (d) | Perubahan bila tertinggal | 2,5 | Konkret dan tetap dalam 3 jam per minggu | Umum, atau melampaui batas 3 jam per minggu = 1 | "Berusaha lebih keras" |
| (d) | Pemeriksa | 1,5 | Orang atau catatan tertentu | — | — |

#### Contoh jawaban — tim fiktif ([§1.6](#16-tim-fiktif-untuk-contoh-jawaban))

| Tingkat | Jawaban | Skor |
|---------|---------|:----:|
| Kurang | (a) "Teknopreneur itu luas, jadi semua orang perlu terus belajar." (b) "Saya akan lebih rajin membaca buku bisnis dan menonton video motivasi." (c) "Tren AI sangat penting di masa depan." (d) "Dengan tekad yang kuat saya yakin bisa." | **1** |
| Cukup | (a) "Saya kurang bisa *public speaking*; itu terlihat waktu *Demo Day*." (b) "Saya akan ikut kursus *public speaking* daring dan berlatih presentasi di organisasi, 3 jam per minggu sepanjang semester depan. Luaran: video presentasi 5 menit di akhir semester." (c) "Tren AI membuat presentasi makin penting karena banyak konten kini dibuat AI." (d) "Akhir Maret saya cek apakah sudah berlatih presentasi empat kali; kalau belum, jadwal latihan saya tambah." | **15** |
| Baik | (a) "*Demo Day* (Mg 15): penguji menanyakan cara kami menghitung CAC. Saya yang menyusun S-07, tetapi tidak dapat menjelaskan mengapa waktu tim dihitung sebagai biaya. Keterampilan yang kurang: menyusun model *unit economics* dari data mentah sendiri — komponen itu saya salin dari templat, jadi yang menghambat bukan cara saya berbicara, melainkan saya tidak memahami asal angkanya." (b) "Februari–Maret (±2 jam/minggu menyusun, ±1 jam/minggu membaca ulang Bab 7): model *unit economics* dua usaha jasa kecil di dekat rumah dari catatan penjualan pemiliknya, satu usaha per empat minggu. April–Mei (±3 jam/minggu): satu model untuk usaha langganan, lalu berlatih menjelaskannya 5 menit tanpa catatan — sesudah Februari–Maret karena saya hanya dapat menjelaskan model yang saya susun sendiri. Juni (±1 jam/minggu): merapikan ketiga model menurut catatan pemeriksa. Luaran: tiga lembar model bertanggal dengan asumsi tertulis, diperiksa asisten mata kuliah pada awal Juni 2027." (c) "K1: tarif pemanggilan model turun, tetapi kuota gratis dihapus — biaya per pemakaian makin menentukan margin produk digital, jadi keterampilan ini lebih bernilai. Rencana disesuaikan: setiap model wajib memuat satu baris biaya per pemakaian." (d) "Titik tinjau 31 Maret 2027. Tanda tertinggal: kurang dari dua model selesai dan diperiksa teman sekelas. Bila tertinggal: model ketiga dibatalkan dan April dipakai menyelesaikan model yang tertunda — tetap ±3 jam/minggu. Pemeriksa: teman sekelas, lewat lembar catatan jam belajar mingguan yang kami isi bersama." | **30** |

> **Rincian skor.** *Kurang:* (a) 0 + 0 + 0 = 0 (tanpa momen, tanpa keterbatasan diri, tanpa keterampilan); (b) langkah 0 (niat umum) + sumber 0,5 (jenis umum) + 0 + 0 + 0 = 0,5; (c) tren 0,5 (umum) + 0 + 0 = 0,5; (d) 0. *Cukup:* (a) momen 1 (umum) + keterbatasan 1 (milik sendiri, umum) + keterampilan 1 (umum) = 3; (b) langkah 1 (dapat dikenali, tanpa rincian dan tanpa urutan) + sumber 0,5 + bulan dan beban 1 (beban tanpa bulan) + luaran 1,5 (tanpa pemeriksa) + koherensi 1,5 = 5,5; (c) tren 0,5 + arah 1 + penilaian 0 = 1,5; (d) waktu 1,5 + tanda 2,5 + perubahan 1 (menambah jadwal, padahal (b) sudah memakai 3 jam per minggu, melampaui batas) + pemeriksa 0 = 5. *Baik:* (a) 2 + 1,5 + 2,5 = 6; (b) 2,5 + 1,5 + 2 + 2,5 + 1,5 = 10; (c) 1,5 + 2 + 2,5 = 6; (d) 1,5 + 2,5 + 2,5 + 1,5 = 8.

#### Kesalahan umum

- **Keterampilan generik** ("komunikasi", "manajemen waktu") tanpa momen yang membuktikannya kurang.
- **Rencana yang melampaui batas** — 3 jam per minggu adalah batasan soal; rencana 10 jam per minggu bukan rencana yang dapat dijalankan.
- **Luaran yang tidak dapat diperiksa** ("lebih percaya diri"). Luaran yang baik dapat diserahkan kepada orang lain untuk dinilai.
- **Tren umum industri** pada (c), atau tren yang tidak dikaitkan dengan keterampilan.
- **"Berusaha lebih keras"** sebagai rencana cadangan — itu bukan perubahan. **Menambah jam** hanya sah bila jumlahnya tetap ≤ 3 jam per minggu; bila rencana (b) sudah memakai 3 jam, menambah jam melampaui batas.

*Pelajari ulang:* [Modul 16 §16.10 (langkah selanjutnya)](../03-modules/week-16-uas-review-dan-ujian.md#1610-langkah-selanjutnya) · [Modul 16 §16.11 (kebiasaan yang layak dilanjutkan)](../03-modules/week-16-uas-review-dan-ujian.md#1611-kebiasaan-yang-layak-dilanjutkan) · [Penutup — melanjutkan sesudah ini](../06-buku-ajar/penutup.md#melanjutkan-sesudah-ini) · [Bab 9 §9.3.2 (bentuk kriteria yang baik)](../06-buku-ajar/bab-09-mvp-merancang-yang-paling-sedikit.md#932-bentuk-kriteria-yang-baik)

---

## 5. Rekap Skor dan Diagnosis Diri

Salin tabel ini, isi skor Anda per sub-butir, lalu hitung capaian (skor ÷ maks × 100%). Sub-butir dengan capaian di bawah ±70% menunjukkan **jenis bukti yang belum Anda kuasai** — dan biasanya bagian catatan tim yang perlu dibaca ulang sebelum UAS.

| Butir | Sub | Indikator registri | Bloom | Maks | Skor Anda | Bila capaian rendah |
|:-----:|:---:|--------------------|:-----:|:----:|:---------:|---------------------|
| A1 | (a) | 2 — merevisi asumsi | C4 | 6 | | Baca ulang S-05/S-07 dan catatan uji; catat versi pertama dan terakhir angka beserta minggunya |
| A1 | (b) | 2 | C5 | 6 | | Bab 2 §2.1.2; Bab 5 §5.2.3 — jenis dan kekuatan bukti |
| A1 | (c) | 2 | C5 | 8 | | Jurnal keputusan tim; Bab 8 §8.4.2 |
| A2 | (a) | 2 | C4 | 6 | | Catatan rapat dan *sprint*; kutipan pembantah |
| A2 | (b) | 2 | C5 | 6 | | Bab 3 §3.4.2 — perbedaan penafsiran |
| A2 | (c) | 2 | C6 | 8 | | Bentuk aturan: pemicu → tindakan → bukti tertulis |
| B1 | (a) | 1 — rencana berbasis tren | C4 | 6 | | P-00 bagian 5 dan dokumen pemindaian; Modul 1 §1.3 |
| B1 | (b) | 1 | C5 | 6 | | Catatan pemindaian paling awal dan terakhir; Modul 1 §1.3.2–§1.3.3 |
| B2 | (a) | 1 | C5 | 6 | | Angka dan keputusan tim (S-04, S-07, S-13, P-03) |
| B2 | (b) | 1 | C5 | 5 | | Bab 5 §5.2.3 dan §5.3.3, Bab 9 §9.4.1 — kekuatan bukti; siapa sumbernya |
| B2 | (c) | 1 | C6 | 7 | | Modul 7 §7.6.2 — tanda awal; Bab 9 §9.3.1 |
| C1 | (a) | 1 | C4 | 6 | | Umpan balik *Demo Day* dan catatan kerja sendiri |
| C1 | (b) | 1 | C6 | 10 | | Bab 9 §9.3.2 — ukuran yang dapat diperiksa |
| C1 | (c) | 1 | C5 | 6 | | Catatan pemindaian tim; kliping B2 |
| C1 | (d) | 1 | C6 | 8 | | Penutup — melanjutkan sesudah ini |
| **Jumlah** | | | | **100** | | |

| Kriteria registri (`TEKNO-Sub-CPMKUAI32-1`) | Sub-butir | Skor maks | Skor Anda | Capaian |
|---------------------------------------------|-----------|:---------:|:---------:|:-------:|
| Bukti adaptasi keputusan | A1(a)–(c), A2(a) | 26 | | |
| Kejelasan pembelajaran | A2(b)–(c), C1(a), C1(b), C1(d) | 38 | | |
| Relevansi tren | B1, B2, C1(c) | 36 | | |
| **Jumlah** | | **100** | | |

> Seluruh butir menandai `TEKNO-Sub-CPMKUAI32-1` ([§1.5](#15-penandaan-butir)); pembagian per kriteria hanya membantu Anda membaca kekuatan dan kelemahan sendiri. Nilai UAS dihitung sebagai skor UAS × 10%.

---

## 6. Verifikasi Angka dengan Python

UAS reflektif tidak memuat soal hitungan, tetapi pembahasan ini memuat angka yang dapat diperiksa: **skor maksimum** setiap unsur, sub-butir, butir, dan bagian; **skor contoh** *Kurang*, *Cukup*, dan *Baik* yang diturunkan dari rubrik — skor per unsur ditulis harfiah, termasuk untuk contoh *Baik*; pembagian skor per Bloom, indikator, dan kriteria; **skor maksimum jalan keluar** ([§1.2](#12-kejujuran-refleksi-dan-perubahan-yang-benar-benar-terjadi) butir 2); serta **angka tim fiktif**. Salin kode berikut ke satu sel Google Colab (atau Python 3.8 ke atas) lalu jalankan; tidak diperlukan pustaka tambahan. *Pemeriksaan ini dilakukan sesudah latihan — selama UAS tidak ada alat bantu apa pun.*

```python
# Verifikasi angka pembahasan Latihan UAS Teknopreneur
# Dapat dijalankan di Google Colab atau Python 3.8 ke atas; tanpa pustaka tambahan.

# Skor maksimum per unsur rubrik, per sub-butir (urutan unsur sama dengan tabel rubrik)
rubrik = {
    "A1(a)": [1, 1, 1, 3],          "A1(b)": [2, 2, 2],           "A1(c)": [1, 2, 1, 4],
    "A2(a)": [1, 1, 1, 3],          "A2(b)": [3, 3],              "A2(c)": [1.5, 2, 1.5, 1, 2],
    "B1(a)": [2.5, 3.5],            "B1(b)": [2, 1.5, 2.5],
    "B2(a)": [2.5, 1.5, 2],         "B2(b)": [1, 2, 2],           "B2(c)": [1.5, 1.5, 1.5, 1.5, 1],
    "C1(a)": [2, 1.5, 2.5],         "C1(b)": [2.5, 1.5, 2, 2.5, 1.5],
    "C1(c)": [1.5, 2, 2.5],         "C1(d)": [1.5, 2.5, 2.5, 1.5],
}
# Skor yang dicetak di lembar soal: (skor sub-butir, level Bloom)
cetak = {"A1(a)": (6, "C4"), "A1(b)": (6, "C5"), "A1(c)": (8, "C5"),
         "A2(a)": (6, "C4"), "A2(b)": (6, "C5"), "A2(c)": (8, "C6"),
         "B1(a)": (6, "C4"), "B1(b)": (6, "C5"),
         "B2(a)": (6, "C5"), "B2(b)": (5, "C5"), "B2(c)": (7, "C6"),
         "C1(a)": (6, "C4"), "C1(b)": (10, "C6"), "C1(c)": (6, "C5"), "C1(d)": (8, "C6")}

def rapi(x):
    """Tampilkan 20.0 sebagai 20, tetapi 2.5 tetap 2.5."""
    return int(x) if float(x).is_integer() else x

def jumlah(awalan):
    return rapi(sum(sum(v) for k, v in rubrik.items() if k.startswith(awalan)))

for sub, unsur in rubrik.items():
    assert sum(unsur) == cetak[sub][0], sub          # rubrik = skor yang dicetak
    assert all((2 * u) % 1 == 0 for u in unsur)       # kelipatan 0,5
butir = {b: jumlah(b) for b in ("A1", "A2", "B1", "B2", "C1")}
bagian = {g: jumlah(g) for g in "ABC"}
print("Skor per butir :", butir)
print("Skor per bagian:", bagian, "total", sum(bagian.values()))
assert butir == {"A1": 20, "A2": 20, "B1": 12, "B2": 18, "C1": 30}
assert bagian == {"A": 40, "B": 30, "C": 30}           # kisi-kisi §3: 40% · 30% · 30%

bloom = {}
for skor, lvl in cetak.values():
    bloom[lvl] = bloom.get(lvl, 0) + skor
print("Skor per Bloom :", dict(sorted(bloom.items())))
assert bloom == {"C4": 24, "C5": 43, "C6": 33}

kriteria = {"adaptasi": ["A1(a)", "A1(b)", "A1(c)", "A2(a)"],
            "pembelajaran": ["A2(b)", "A2(c)", "C1(a)", "C1(b)", "C1(d)"],
            "tren": ["B1(a)", "B1(b)", "B2(a)", "B2(b)", "B2(c)", "C1(c)"]}
per_kriteria = {k: sum(cetak[s][0] for s in v) for k, v in kriteria.items()}
indikator = {"indikator 2 (Bagian A)": bagian["A"], "indikator 1 (Bagian B dan C)": bagian["B"] + bagian["C"]}
print("Per kriteria   :", per_kriteria, "| per indikator:", indikator)
assert per_kriteria == {"adaptasi": 26, "pembelajaran": 38, "tren": 36}
assert sorted(sum(kriteria.values(), [])) == sorted(cetak)   # setiap sub-butir tepat satu kriteria

# Skor contoh jawaban per unsur, ditulis harfiah dari rincian skor (urutan unsur sama dengan rubrik)
contoh = {
    "A1": {"Kurang": [[1, 0, 0, 0], [0, 1, 0], [0, 0, 0, 0]],
           "Cukup":  [[1, .5, .5, 1], [1, 1, .5], [1, 2, .5, .5]],
           "Baik":   [[1, 1, 1, 3], [2, 2, 2], [1, 2, 1, 4]]},
    "A2": {"Kurang": [[0, 0, 0, 0], [0, 0], [.5, 0, 0, 0, 0]],
           "Cukup":  [[.5, .5, .5, 1.5], [1.5, 1], [1.5, 2, 0, 1, 0]],
           "Baik":   [[1, 1, 1, 3], [3, 3], [1.5, 2, 1.5, 1, 2]]},
    "B1": {"Kurang": [[0, 0], [0, .5, 0]],
           "Cukup":  [[1, 1], [1.5, .5, 1.5]],
           "Baik":   [[2.5, 3.5], [2, 1.5, 2.5]]},
    "B2": {"Kurang": [[.5, 0, 0], [0, 0, 0], [.5, 0, 0, 0, 0]],
           "Cukup":  [[1.5, 1.5, 1], [0, 2, .5], [.5, .5, 1.5, .5, 0]],
           "Baik":   [[2.5, 1.5, 2], [1, 2, 2], [1.5, 1.5, 1.5, 1.5, 1]]},
    "C1": {"Kurang": [[0, 0, 0], [0, .5, 0, 0, 0], [.5, 0, 0], [0, 0, 0, 0]],
           "Cukup":  [[1, 1, 1], [1, .5, 1, 1.5, 1.5], [.5, 1, 0], [1.5, 2.5, 1, 0]],
           "Baik":   [[2, 1.5, 2.5], [2.5, 1.5, 2, 2.5, 1.5], [1.5, 2, 2.5], [1.5, 2.5, 2.5, 1.5]]},
}
dicetak = {"A1": (2, 9.5, 20), "A2": (.5, 10, 20), "B1": (.5, 5.5, 12), "B2": (1, 9.5, 18), "C1": (1, 15, 30)}
total = {"Kurang": 0, "Cukup": 0, "Baik": 0}
for b, tingkat in contoh.items():
    subs = [s for s in rubrik if s.startswith(b)]
    assert tingkat["Baik"] == [rubrik[s] for s in subs], b    # contoh Baik (harfiah) = skor penuh rubrik
    for t, skor in tingkat.items():
        for s, u in zip(subs, skor):
            assert len(u) == len(rubrik[s]) and all(x <= m for x, m in zip(u, rubrik[s])), (b, t, s)
        nilai = sum(sum(u) for u in skor)
        total[t] += nilai
        assert nilai == dicetak[b][("Kurang", "Cukup", "Baik").index(t)], (b, t, nilai)
print("Skor contoh    :", dicetak, "| total", {t: rapi(n) for t, n in total.items()})
assert total == {"Kurang": 5, "Cukup": 49.5, "Baik": 100}

# Jalan keluar jujur (§1.2 butir 2): skor maksimum = maksimum rubrik dikurangi bagian yang tidak dapat diraih
maks = {s: sum(u) for s, u in rubrik.items()}
jalan_keluar = {"A1(a) bukti penguji tidak pernah dikumpulkan": maks["A1(a)"] - (3 - 2),
                "A1(c) keputusan tetap, sebab berbasis bukti": maks["A1(c)"] - (2 - 1),
                "A1(c) keputusan tetap, sebab lain diakui jujur": maks["A1(c)"] - (2 - .5),
                "A2(a) pendapat tidak pernah diuji": maks["A2(a)"] - (1 - .5),
                "B1(b) tidak ada perubahan tercatat": maks["B1(b)"] - (1 - .5)}
pilihan_a = (maks["A1(a)"], jalan_keluar["A1(a) bukti penguji tidak pernah dikumpulkan"])
pilihan_c = (maks["A1(c)"], jalan_keluar["A1(c) keputusan tetap, sebab berbasis bukti"],
             jalan_keluar["A1(c) keputusan tetap, sebab lain diakui jujur"])
jalur_a1 = sorted({rapi(a + maks["A1(b)"] + c) for a in pilihan_a for c in pilihan_c}, reverse=True)
print("Jalan keluar   :", {k: rapi(v) for k, v in jalan_keluar.items()})
print("A1 per jalur   :", jalur_a1)
assert list(jalan_keluar.values()) == [5, 7, 6.5, 5.5, 5.5]
assert jalur_a1 == [20, 19, 18.5, 18, 17.5]

# Angka tim fiktif (§1.6 dan contoh jawaban)
som_awal = 140 * 10 / 14 * 75_000 * 12          # S-05 (Mg 5): 140 gelanggang x 10/14 x Rp75.000 x 12 bulan
som_baru = 140 * 2 / 9 * 75_000 * 12            # S-05 dihitung ulang (Mg 11) dengan proporsi yang benar-benar membayar
print(f"Proporsi 'mau' : 10/14 = {10 / 14:.1%} (±70%); membayar 2/9 = {2 / 9:.1%} (±22%)")
print(f"SOM            : Rp{som_awal:,.0f} -> Rp{som_baru:,.0f}".replace(",", "."))
print(f"Rasio revisi   : {(2 / 9) / (10 / 14):.2f}; rasio target 10/30 = {10 / 30:.2f} (keduanya ±sepertiga)")
jam_c1 = {"Feb-Mar": 2 + 1, "Apr-Mei": 3, "Jun": 1}             # contoh Baik C1(b): jam per minggu per langkah
print(f"Uji tautan     : 3/40 = {3 / 40:.1%} membuka, 0 memesan; rencana C1(b) jam/minggu: {jam_c1}")
assert round(10 / 14, 2) == 0.71 and round(2 / 9, 2) == 0.22
assert round(som_awal) == 90_000_000 and round(som_baru) == 28_000_000
assert round((2 / 9) / (10 / 14), 2) == 0.31 and round(10 / 30, 2) == 0.33
assert max(jam_c1.values()) <= 3                                   # batas tercetak C1: 3 jam per minggu
print("Semua angka cocok dengan pembahasan.")
```

Keluaran yang diharapkan (Python memakai titik desimal):

```
Skor per butir : {'A1': 20, 'A2': 20, 'B1': 12, 'B2': 18, 'C1': 30}
Skor per bagian: {'A': 40, 'B': 30, 'C': 30} total 100
Skor per Bloom : {'C4': 24, 'C5': 43, 'C6': 33}
Per kriteria   : {'adaptasi': 26, 'pembelajaran': 38, 'tren': 36} | per indikator: {'indikator 2 (Bagian A)': 40, 'indikator 1 (Bagian B dan C)': 60}
Skor contoh    : {'A1': (2, 9.5, 20), 'A2': (0.5, 10, 20), 'B1': (0.5, 5.5, 12), 'B2': (1, 9.5, 18), 'C1': (1, 15, 30)} | total {'Kurang': 5, 'Cukup': 49.5, 'Baik': 100}
Jalan keluar   : {'A1(a) bukti penguji tidak pernah dikumpulkan': 5, 'A1(c) keputusan tetap, sebab berbasis bukti': 7, 'A1(c) keputusan tetap, sebab lain diakui jujur': 6.5, 'A2(a) pendapat tidak pernah diuji': 5.5, 'B1(b) tidak ada perubahan tercatat': 5.5}
A1 per jalur   : [20, 19, 18.5, 18, 17.5]
Proporsi 'mau' : 10/14 = 71.4% (±70%); membayar 2/9 = 22.2% (±22%)
SOM            : Rp90.000.000 -> Rp28.000.000
Rasio revisi   : 0.31; rasio target 10/30 = 0.33 (keduanya ±sepertiga)
Uji tautan     : 3/40 = 7.5% membuka, 0 memesan; rencana C1(b) jam/minggu: {'Feb-Mar': 3, 'Apr-Mei': 3, 'Jun': 1}
Semua angka cocok dengan pembahasan.
```

---

## Dokumen Terkait

1. [Latihan UAS](latihan-uas.md)
2. [Cetak biru butir dan panduan varian](latihan-uas-cetak-biru.md) (untuk dosen)
3. [Kisi-kisi UAS](kisi-kisi-uas.md)
4. [Modul Minggu 16](../03-modules/week-16-uas-review-dan-ujian.md)
5. [Penutup buku ajar](../06-buku-ajar/penutup.md)

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
