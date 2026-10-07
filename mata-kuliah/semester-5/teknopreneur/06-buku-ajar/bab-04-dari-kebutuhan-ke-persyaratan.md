# BAB 4: DARI KEBUTUHAN KE PERSYARATAN PRODUK

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `TEKNO-Sub-CPMK091-1` | Menganalisis (C4) kebutuhan pengguna menjadi persyaratan yang terukur, berprioritas, dan tertelusur ke bukti lapangan | C4 |

Setelah membaca bab ini, pembaca diharapkan mampu:

1. **Membedakan** (C2) kebutuhan, persyaratan, dan fitur.
2. **Menyusun** (C3) persyaratan yang terukur dan dapat diuji.
3. **Menerapkan** (C3) metode prioritas MoSCoW dan Kano.
4. **Menganalisis** (C4) matriks ketertelusuran dari kutipan sampai persyaratan.
5. **Menilai** (C5) apakah sekumpulan persyaratan masih setia pada bukti.

---

## 4.1 Tiga Hal yang Sering Tertukar

### 4.1.1 Kebutuhan, Persyaratan, Fitur

| | Kebutuhan | Persyaratan | Fitur |
|---|-----------|-------------|-------|
| Pertanyaan | Apa yang kurang dalam hidup orang? | Apa yang harus dipenuhi solusi? | Bagaimana wujudnya? |
| Bahasa | Bahasa pengguna | Bahasa terukur | Bahasa produk |
| Contoh | "Tidak tahu harus belanja berapa" | "Memberi angka perkiraan kebutuhan ≤2 menit sebelum belanja" | "Layar perkiraan belanja harian" |
| Berubah? | Jarang | Kadang | Sering |
| Ditentukan | Lapangan | Tim, dari lapangan | Tim |

Baris "berubah?" menjelaskan mengapa ketiganya harus dipisahkan. Fitur akan berganti berkali-kali sepanjang hidup sebuah usaha; kebutuhan yang mendasarinya hampir tidak berubah. Tim yang mencampur keduanya akan mengira perubahan fitur berarti perubahan arah, dan panik tanpa sebab.

### 4.1.2 Kesalahan Melompat

Kesalahan paling umum adalah melompat dari kebutuhan langsung ke fitur, melewati persyaratan.

```
SALAH:
  "Pedagang tidak tahu harus belanja berapa"
      → "Buat fitur prediksi stok dengan machine learning"

BENAR:
  Kebutuhan  : Pedagang tidak tahu harus belanja berapa
  Persyaratan: Sistem memberi angka perkiraan per bahan,
               tersedia sebelum pukul 04.00,
               tanpa input manual pada malam sebelumnya,
               dengan galat ≤20% dari kebutuhan aktual
  Fitur      : (banyak kemungkinan — termasuk yang bukan aplikasi)
```

Yang hilang dalam lompatan itu adalah **batasan**. Persyaratan versi benar di atas memuat empat batasan, dan salah satunya — "tanpa input manual pada malam sebelumnya" — berasal langsung dari peta perjalanan Bab 3 yang menunjukkan malam adalah saat kelelahan.

Batasan itu juga langsung mematikan sebagian besar solusi yang biasanya pertama terpikirkan. Aplikasi pencatatan stok, misalnya, justru menuntut input manual. Persyaratan yang disusun dengan benar **menyempitkan ruang solusi sebelum tim jatuh cinta pada salah satunya**.

### 4.1.3 Mengapa Persyaratan Bukan Fitur

Persyaratan yang baik dapat dipenuhi oleh beberapa fitur yang berbeda. Bila hanya ada satu cara memenuhinya, kemungkinan besar yang tertulis adalah fitur yang menyamar.

| Persyaratan | Kemungkinan pemenuhan |
|-------------|----------------------|
| Angka perkiraan tersedia sebelum pukul 04.00 tanpa input malam | (a) Hitungan dari data transaksi yang terkumpul otomatis; (b) pesan WhatsApp terjadwal berisi angka dari pola minggu lalu; (c) kartu cetak berisi tabel pola mingguan |
| Dapat dipakai sambil berjalan di pasar dengan satu tangan | (a) Tampilan satu layar tanpa gulir; (b) pesan suara; (c) daftar tercetak di kertas |

Kemungkinan (c) pada kedua baris sengaja dicantumkan. Solusi tanpa perangkat lunak sering memenuhi persyaratan dengan biaya dan risiko yang jauh lebih rendah — dan menemukan bahwa hal itu mungkin adalah salah satu hasil belajar yang paling berharga bagi mahasiswa Informatika.

---

## 4.2 Menulis Persyaratan yang Terukur

### 4.2.1 Unsur Wajib

| Unsur | Pertanyaan | Contoh buruk | Contoh baik |
|-------|------------|--------------|-------------|
| **Pelaku** | Siapa? | "Sistem harus…" | "Pemilik warung dapat…" |
| **Tindakan** | Melakukan apa? | "…mengelola stok" | "…melihat perkiraan belanja" |
| **Ukuran** | Seberapa? | "…dengan cepat" | "…dalam ≤2 menit" |
| **Batasan** | Dalam keadaan apa? | (tidak ada) | "…tanpa koneksi internet" |
| **Sumber** | Dari bukti mana? | (tidak ada) | "#03-4, #07-2" |

Dua unsur terakhir adalah yang membedakan persyaratan lapangan dari daftar keinginan.

### 4.2.2 Mengubah Kata Sifat Menjadi Angka

Kata sifat tidak dapat diuji. Setiap kata sifat dalam persyaratan harus diganti dengan besaran.

| Kata sifat | Pertanyaan penggantinya | Hasil |
|------------|------------------------|-------|
| cepat | Berapa detik? Dibandingkan apa? | ≤3 detik; lebih cepat dari membuka buku catatan |
| mudah | Berapa langkah? Untuk siapa? | ≤3 ketukan; dapat diselesaikan pengguna baru tanpa dipandu |
| akurat | Galat berapa persen? | Galat ≤20% dari kebutuhan aktual |
| murah | Berapa rupiah? Dibanding apa? | ≤Rp25.000/bulan; di bawah nilai kerugian yang dicegah |
| ringan | Berapa MB? Di perangkat apa? | ≤30 MB; berjalan di Android 8 dengan RAM 2 GB |

Kolom tengah adalah kebiasaan yang perlu dilatih. Setiap kali kata sifat muncul, pertanyaannya selalu: *dibandingkan apa, dan bagaimana kita akan tahu?*

Baris "murah" menunjukkan hal penting: batas harga tidak ditentukan dari selera tim, melainkan dari **angka kerugian yang ditemukan di lapangan**. Kerugian Rp300–400 ribu per bulan menetapkan batas atas yang masuk akal; harga Rp25.000 berada jauh di bawahnya, sehingga perhitungan nilainya jelas bagi pengguna.

### 4.2.3 Persyaratan Non-Fungsional

| Jenis | Pertanyaan | Mengapa penting di konteks Indonesia |
|-------|------------|-------------------------------------|
| Ketersediaan | Berfungsi tanpa internet? | Sinyal tidak merata; pasar subuh sering blank spot |
| Perangkat | Berjalan di perangkat apa? | Sebagian besar pengguna memakai Android lama |
| Bahasa | Bahasa apa? Istilah apa? | Istilah teknis Inggris menjadi penghalang |
| Keterjangkauan data | Berapa kuota per bulan? | Kuota adalah biaya nyata yang diperhitungkan pengguna |
| Keamanan | Data apa yang disimpan? | Data pendapatan adalah hal yang sangat pribadi |
| Pemulihan | Bagaimana bila ponsel hilang? | Ponsel hilang atau rusak adalah kejadian biasa |

Persyaratan non-fungsional sering menjadi penentu kegagalan yang sesungguhnya. Sebuah solusi yang memenuhi seluruh persyaratan fungsional tetapi menuntut 500 MB kuota per bulan akan ditinggalkan, dan tim tidak akan pernah tahu alasannya bila tidak menanyakannya.

---

## 4.3 Menentukan Prioritas

### 4.3.1 MoSCoW

| Tingkat | Arti | Ujian |
|---------|------|-------|
| **Must have** | Tanpa ini solusi tidak berguna | Bila dihapus, masih adakah yang mau memakainya? |
| **Should have** | Penting tetapi ada jalan lain sementara | Adakah cara manual menggantikannya untuk sementara? |
| **Could have** | Menyenangkan bila ada | Adakah pengguna yang menyebutnya tanpa ditanya? |
| **Won't have (kali ini)** | Sengaja tidak dikerjakan sekarang | Sudahkah alasannya dicatat? |

Kategori keempat adalah yang paling sering dikosongkan dan paling berguna. Menuliskan secara eksplisit apa yang **tidak** akan dikerjakan sekarang — beserta alasannya — mencegah perdebatan yang sama berulang setiap dua minggu.

Ujian pada kolom kanan mencegah penyakit yang paling umum: semua persyaratan berakhir di kategori *Must have*. Bila lebih dari sepertiga persyaratan masuk *Must*, tim belum benar-benar memilih.

### 4.3.2 Model Kano

Model Kano memilah persyaratan menurut hubungan antara pemenuhannya dan kepuasan pengguna.

| Jenis | Bila ada | Bila tidak ada | Contoh pada kasus berjalan |
|-------|----------|----------------|---------------------------|
| **Dasar** | Tidak disadari | Sangat kecewa | Angka yang ditampilkan benar |
| **Kinerja** | Makin baik makin puas | Makin buruk makin kecewa | Ketepatan perkiraan belanja |
| **Penggoda** | Senang tak terduga | Tidak apa-apa | Pengingat otomatis saat harga bahan turun |
| **Acuh** | Tidak peduli | Tidak peduli | Pilihan tema warna |
| **Terbalik** | Justru terganggu | Lebih baik | Notifikasi setiap transaksi |

Baris terakhir adalah yang paling sering diabaikan tim dan paling merusak. Beberapa hal yang dianggap tim sebagai peningkatan justru mengurangi kepuasan pengguna. Pada kasus Bu Sri, notifikasi per transaksi akan mengganggu pada jam 11–14 — jam yang menurut peta perjalanan tidak boleh disentuh.

Cara membedakan keduanya adalah bertanya **dua arah**: "Bagaimana perasaan Anda bila ada X?" dan "Bagaimana perasaan Anda bila tidak ada X?" Jawaban "terganggu" pada pertanyaan pertama menandai persyaratan terbalik.

### 4.3.3 Gabungan Keduanya

| | Must | Should | Could | Won't |
|---|------|--------|-------|-------|
| **Dasar** | ✅ selalu di sini | — | — | — |
| **Kinerja** | Sebagian | ✅ sebagian besar | — | — |
| **Penggoda** | — | — | ✅ | Sebagian |
| **Acuh** | — | — | — | ✅ |
| **Terbalik** | — | — | — | ✅ **dan dicatat sebagai larangan** |

Sel kanan bawah menghasilkan jenis dokumen yang jarang dibuat tim mahasiswa tetapi sangat berguna: **daftar hal yang sengaja tidak akan dibuat**, lengkap dengan alasan dan kutipan sumbernya.

---

## 4.4 Matriks Ketertelusuran

### 4.4.1 Bentuknya

| ID | Kutipan sumber | Kebutuhan | Persyaratan | MoSCoW | Kano |
|----|----------------|-----------|-------------|--------|------|
| R-01 | #03-3, #07-2, #11-4 | Tidak tahu jumlah belanja | Memberi angka perkiraan per bahan sebelum pukul 04.00, galat ≤20% | Must | Kinerja |
| R-02 | #03-1, #05-2 | Tidak ada waktu mencatat saat ramai | Tidak menuntut input apa pun antara pukul 10.00–15.00 | Must | Dasar |
| R-03 | #03-2, #11-3 | Aplikasi sebelumnya terasa ribet | Tugas utama selesai dalam ≤3 ketukan | Must | Dasar |
| R-04 | #05-4 | Sinyal buruk di pasar | Berfungsi penuh tanpa koneksi internet | Must | Dasar |
| R-05 | #07-5 | Ingin tahu tren mingguan | Menampilkan ringkasan 7 hari | Should | Kinerja |
| R-06 | — | (usulan tim) | Ekspor data ke spreadsheet | Won't | Acuh |

Baris R-06 sengaja dicantumkan dengan kolom sumber kosong. Persyaratan yang tidak punya sumber **boleh** ada, tetapi harus ditandai demikian dan hampir selalu berakhir di *Won't*. Menandainya secara jujur jauh lebih baik daripada mengarang kutipan untuk membenarkannya.

### 4.4.2 Ujian Ketertelusuran

Matriks diperiksa dengan tiga pertanyaan:

| Pertanyaan | Bila jawabannya buruk |
|------------|----------------------|
| Berapa persen persyaratan punya kolom sumber terisi? | <70% → tim lebih banyak mengarang daripada mendengar |
| Adakah kutipan penting yang tidak menjadi persyaratan apa pun? | Ya → periksa; mungkin ada kebutuhan yang terlewat |
| Adakah persyaratan *Must* tanpa sumber? | Ya → turunkan atau cari buktinya |

Pertanyaan kedua sering menghasilkan temuan. Kutipan yang tidak terpakai bukan berarti tidak penting — kadang ia menunjuk kebutuhan yang tim belum siap menghadapinya, dan menyadarinya lebih baik daripada melewatkannya diam-diam.

### 4.4.3 Ketika Bukti Bertentangan

Pada 15 wawancara, akan ada kutipan yang saling bertentangan.

| Contoh pertentangan | Cara menanganinya |
|--------------------|-------------------|
| 8 orang ingin sederhana, 3 orang ingin lengkap | Periksa apakah 3 orang itu segmen berbeda |
| 1 orang membayar mahal, 14 orang menolak berbayar | Periksa apa yang berbeda pada 1 orang itu |
| Narasumber sama berkata berbeda di dua kesempatan | Kembali bertanya; kemungkinan konteksnya berbeda |

Pertentangan bukan cacat data, melainkan petunjuk adanya **segmen yang berbeda**. Penemuan bahwa 3 dari 15 narasumber sebenarnya menjalankan usaha dengan skala dan kebutuhan yang lain sering kali lebih bernilai daripada persyaratan mana pun dalam matriks.

---

## AI Corner — Bab 4

### Batas Pemakaian

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI menandai kata sifat yang belum terukur | Meminta AI menyusun daftar persyaratan dari nama produk |
| Meminta AI mengusulkan besaran untuk kata sifat, untuk diperiksa tim | Meminta AI menentukan prioritas MoSCoW |
| Meminta AI memeriksa apakah persyaratan masih berupa fitur terselubung | Meminta AI mengisi kolom sumber |
| Meminta AI menyebutkan persyaratan non-fungsional yang biasa terlewat | Meminta AI menyimpulkan kebutuhan dari persona yang belum ada |

Baris ketiga pada kolom kanan perlu ditegaskan: **mengisi kolom sumber dengan bantuan AI berarti memalsukan ketertelusuran**. Kolom itu adalah pernyataan bahwa seseorang dalam tim benar-benar mendengar kalimat tersebut diucapkan.

### Pemakaian yang Dianjurkan: Pemburu Kata Sifat

```
Berikut daftar persyaratan produk tim saya:
[tempelkan daftar]

Tugas Anda:
1. Tandai setiap kata sifat atau keterangan yang belum terukur.
2. Untuk masing-masing, ajukan pertanyaan yang harus saya jawab
   agar menjadi terukur.
3. Tandai persyaratan yang sebenarnya sudah berupa fitur.

Jangan mengusulkan persyaratan baru dan jangan menebak angkanya.
```

Perintah baris terakhir penting. Tanpa itu, model akan mengisi angka yang terdengar masuk akal — misalnya "≤3 detik" — dan angka itu tidak berasal dari mana pun. Angka dalam persyaratan harus berasal dari lapangan (berapa lama orang bersedia menunggu) atau dari pembanding (berapa lama membuka buku catatan), bukan dari kebiasaan penulisan dokumen teknis.

### Mengapa Prioritas Tidak Dapat Diserahkan

Prioritas adalah keputusan tentang **apa yang bersedia dikorbankan tim**. AI tidak memikul akibat dari keputusan itu; tim yang memikulnya, dalam bentuk waktu 14 minggu yang terbatas dan nilai proyek akhir.

Lebih jauh, prioritas yang benar bergantung pada hal yang tidak diketahui model: berapa anggota tim, keterampilan apa yang dimiliki, berapa lama waktu yang tersedia setiap minggu, dan seberapa jauh narasumber dapat ditemui lagi. Prioritas yang disusun tanpa mengetahui hal-hal itu adalah prioritas untuk tim yang tidak ada.

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan perbedaan kebutuhan, persyaratan, dan fitur dengan satu contoh yang sama untuk ketiganya.
2. Ubah lima persyaratan berikut menjadi terukur:
   - "Aplikasi harus cepat."
   - "Tampilan harus mudah dipahami."
   - "Data harus aman."
   - "Harga harus terjangkau."
   - "Sistem harus andal."
3. Sebutkan lima unsur wajib sebuah persyaratan.
4. Apa ujian untuk membedakan *Must have* dari *Should have*?
5. Apa yang dimaksud persyaratan **terbalik** dalam model Kano, dan berikan satu contoh.

### Tingkat Menengah

6. Berikut daftar sebuah tim. Untuk masing-masing, tentukan apakah ia kebutuhan, persyaratan, atau fitur, lalu perbaiki yang salah tempat.
   - "Tombol tambah barang di pojok kanan bawah"
   - "Pedagang tidak punya catatan pembelian bulan lalu"
   - "Riwayat 30 hari terakhir dapat dilihat tanpa koneksi"
   - "Grafik batang mingguan"
   - "Pemilik tidak percaya pada hitungan pegawainya"

7. Susun matriks ketertelusuran (6 kolom seperti §4.4.1) dengan minimal 5 baris untuk satu persoalan yang Anda amati. Tandai baris yang kolom sumbernya kosong dan jelaskan mengapa Anda tetap mencantumkannya.

8. Sebuah tim memiliki 18 persyaratan, 15 di antaranya berkategori *Must have*. Jelaskan apa yang salah, dan uraikan langkah untuk memperbaikinya dengan ujian §4.3.1.

9. Untuk persyaratan *"Sistem memberi angka perkiraan belanja sebelum pukul 04.00 tanpa input manual malam sebelumnya"*, sebutkan **tiga** kemungkinan pemenuhan yang berbeda, minimal satu di antaranya tanpa perangkat lunak. Bandingkan ketiganya dari sisi biaya dan risiko.

### Tingkat Mahir

10. **Latihan lapangan.** Ambil lima persyaratan yang tim Anda susun. Bawa kembali kepada dua narasumber asli dan tanyakan dua arah untuk masing-masing: bagaimana perasaannya bila ada, dan bila tidak ada. Klasifikasikan hasilnya menurut Kano. Laporkan persyaratan mana yang ternyata **terbalik** atau **acuh** — dan apa yang berubah dalam daftar prioritas karenanya.

11. Susun daftar **Won't have** lengkap dengan alasan dan kutipan sumber untuk proyek tim Anda, minimal tujuh butir. Untuk setiap butir jelaskan keadaan apa yang, bila ditemukan kemudian, akan memindahkannya menjadi *Should have*. Jelaskan mengapa dokumen semacam ini lebih berguna daripada daftar fitur yang direncanakan.

12. Tim Anda menemukan pertentangan: 12 dari 15 narasumber menolak membayar, sedangkan 3 sisanya sudah membayar solusi lain. Analisis apakah ketiganya merupakan segmen yang berbeda. Rumuskan dua kemungkinan arah usaha yang muncul dari analisis itu, sebutkan persyaratan mana yang berubah pada masing-masing arah, dan tentukan bukti tambahan apa yang paling murah dikumpulkan untuk memilih di antaranya.

---

## Rangkuman

| Gagasan pokok | Rumusan singkat |
|---------------|-----------------|
| Tiga tingkatan | Kebutuhan (bahasa pengguna) → persyaratan (terukur) → fitur (wujud) |
| Kesalahan melompat | Langsung dari kebutuhan ke fitur menghilangkan batasan |
| Guna persyaratan | Menyempitkan ruang solusi sebelum tim jatuh cinta pada salah satunya |
| Kata sifat | Setiap kata sifat diganti besaran; angkanya berasal dari lapangan |
| Non-fungsional | Sering menjadi sebab kegagalan yang sesungguhnya |
| MoSCoW | Kategori *Won't* adalah yang paling berguna dan paling sering kosong |
| Kano terbalik | Beberapa "peningkatan" justru mengurangi kepuasan |
| Ketertelusuran | <70% persyaratan bersumber berarti tim lebih banyak mengarang |
| Pertentangan bukti | Petunjuk adanya segmen berbeda, bukan cacat data |

---

## Referensi

1. Wiegers, K., & Beatty, J. (2013). *Software Requirements* (3rd ed.). Microsoft Press.
2. Cohn, M. (2004). *User Stories Applied: For Agile Software Development*. Addison-Wesley.
3. Kano, N., Seraku, N., Takahashi, F., & Tsuji, S. (1984). Attractive Quality and Must-Be Quality. *Journal of the Japanese Society for Quality Control*, 14(2), 39–48.
4. Clegg, D., & Barker, R. (1994). *Case Method Fast-Track: A RAD Approach*. Addison-Wesley. (Sumber MoSCoW.)
5. Robertson, S., & Robertson, J. (2012). *Mastering the Requirements Process* (3rd ed.). Addison-Wesley.
6. Gothelf, J., & Seiden, J. (2021). *Lean UX: Designing Great Products with Agile Teams* (3rd ed.). O'Reilly Media.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul mingguan | [Minggu 4 — Dari Kebutuhan ke Persyaratan](../03-modules/week-04-dari-kebutuhan-ke-persyaratan.md) |
| Studio | [Studio 4 — Matriks Kebutuhan-Persyaratan](../04-labs/lab-04-matriks-kebutuhan-persyaratan.md) |
| Bab sebelumnya | [Bab 3 — Persona, JTBD, dan Konteks Penggunaan](bab-03-persona-jtbd-konteks-penggunaan.md) |
| Bab berikutnya | [Bab 5 — Ukuran Pasar dan Analisis Kompetitor](bab-05-ukuran-pasar-dan-kompetitor.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
