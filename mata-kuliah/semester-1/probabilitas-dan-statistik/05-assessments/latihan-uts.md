---
id: uai-if52510033-latihan-uts
tipe: asesmen
judul: "Latihan UTS — Probabilitas dan Statistik"
kode_mk: IF52510033
nama_mk: Probabilitas dan Statistik
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-08
---

# LATIHAN UJIAN TENGAH SEMESTER (SIMULASI)

## Probabilitas dan Statistik — IF52510033

> **Latihan UTS — bukan naskah UTS.** Simulasi lengkap UTS Probabilitas dan Statistik Ganjil 2026/2027 untuk berlatih: komposisi, durasi (100 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UTS. Naskah UTS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.
>
> **Cara memakai latihan ini.** Kerjakan dalam satu kali duduk dengan batas waktu **100 menit**, *closed book*, **tanpa AI** dan **tanpa membuka pembahasan** — sesuai aturan UTS ([kisi-kisi UTS §1](kisi-kisi-uts.md#1-ketentuan-ujian)). Siapkan kalkulator ilmiah *non-programmable* dan alat tulis; sebagai pengganti tabel yang dibagikan pengawas, pakai [Lampiran A.1 (tabel Z)](../06-buku-ajar/lampiran.md#a1-tabel-z--distribusi-normal-standar) dan [Lampiran A.2 (tabel t)](../06-buku-ajar/lampiran.md#a2-tabel-t--distribusi-student) buku ajar saja — bagian Lampiran lain, termasuk formularium, tidak boleh dibuka. Baru **sesudah** waktu habis, cocokkan jawaban Anda dengan [pembahasan dan pedoman skor](latihan-uts-pembahasan.md), lalu hitung skor Anda sendiri. Penandaan Sub-CPMK per butir ada di pembahasan dan di [cetak biru butir](latihan-uts-cetak-biru.md).

---

**UNIVERSITAS AL AZHAR INDONESIA**
Fakultas Sains dan Teknologi — Program Studi Informatika

| | |
|---|---|
| **Mata kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Asesmen** | Latihan UTS (simulasi) — persiapan UTS Semester Ganjil 2026/2027, Minggu 8 |
| **Kelas** | IF26A, IF26H |
| **Dosen pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Durasi** | 100 menit |
| **Sifat** | *Closed book* |
| **Cakupan** | Minggu 1–7 |

> **Amanah berlatih.** Latihan ini tidak dinilai; manfaatnya bergantung pada kejujuran Anda sendiri. Kerjakan tanpa bantuan orang lain, catatan, atau AI, dengan waktu yang benar-benar dibatasi — sama seperti amanah akademik yang berlaku saat UTS ([kerangka asesmen §7](assessment-framework.md#7-integritas-akademik)).

---

## Petunjuk Umum

1. **Alat bantu yang diizinkan:** kalkulator ilmiah *non-programmable* dan alat tulis.
2. **Tabel:** saat UTS, pengawas membagikan tabel distribusi Normal baku (luas kumulatif P(Z ≤ z)) dan tabel-t bersama lembar soal. Saat berlatih, pakai Lampiran A.1 dan A.2 buku ajar (formatnya sama).
3. **Rumus tidak disediakan** — hafalkan [daftar rumus kisi-kisi UTS §7](kisi-kisi-uts.md#7-daftar-rumus-yang-harus-dihafal).
4. **Dilarang:** catatan dan formularium dalam bentuk apa pun (termasuk Lampiran buku ajar; saat berlatih, buka hanya tabel A.1 dan A.2 sebagai pengganti tabel dari pengawas), telepon genggam, jam pintar, laptop, dan **AI dalam bentuk apa pun**.
5. Latihan terdiri atas empat bagian. Total skor **100**.

   | Bagian | Bentuk | Jumlah butir | Skor | Waktu saran |
   |---|---|---|---|---|
   | A | Pilihan ganda | 15 | 20 | 20 menit |
   | B | Isian / hitungan pendek | 8 | 25 | 25 menit |
   | C | Uraian terstruktur | 4 | 40 | 40 menit |
   | D | Studi kasus terpadu | 1 | 15 | 15 menit |

   Waktu saran mengikuti kisi-kisi UTS §2 dan jumlahnya sudah 100 menit, yaitu seluruh durasi. Waktu membaca seluruh soal (±5 menit) dan memeriksa ulang (±10 menit) yang dianjurkan [modul Minggu 8](../03-modules/week-08-uts-review-dan-ujian.md#strategi-mengerjakan-ujian) **tidak** ditambahkan di luar 100 menit, tetapi diambil dari waktu saran itu — jadi usahakan setiap bagian selesai sedikit lebih cepat daripada waktu sarannya.

   **Panjang latihan ini masih dikalibrasi.** Taksiran waktu kerjanya ±85–97 menit, sehingga bersama waktu membaca dan memeriksa, 100 menit bisa tidak cukup. Saat berlatih, catat waktu yang Anda pakai per bagian. Bila waktu habis, tandai butir terakhir yang selesai, lalu selesaikan sisanya dan catat waktu tambahannya terpisah. Panjang naskah UTS ditetapkan dari uji coba berwaktu sebelum UTS; bila dosen memintanya, serahkan catatan Anda tanpa nama sebagai data pendukung (yang dipakai hanya rekap agregatnya). Bila panjangnya disesuaikan, latihan ini diperbarui dengan cara yang sama.

6. Untuk Bagian B, C, dan D **tuliskan langkah**. Jawaban yang hanya berisi angka akhir tanpa langkah memperoleh **paling banyak 40%** skor butir. Beberapa perintah membatasi panjang jawaban (mis. "paling banyak 3 kalimat"); hitungan tidak termasuk batas itu. Batas ini membantu Anda mengatur waktu — yang dinilai adalah unsur jawaban, bukan panjangnya.
7. **Anjuran (tidak wajib):** tuliskan "diketahui" dan "ditanya" dalam notasi sebelum menghitung probabilitas; untuk soal Normal, buat sketsa kurva dan arsir daerah yang dicari. Kebiasaan ini mencegah salah arah, tetapi tidak dinilai tersendiri — yang dinilai adalah ketepatan langkah dan arah perhitungan.
8. Pakai koma sebagai pemisah desimal. Kecuali diminta lain, bulatkan probabilitas sampai **4 angka di belakang koma** dan nilai lain sampai **2 angka di belakang koma**. Tuliskan satuan.
9. **Kuartil:** gunakan posisi kuartil ke-p pada data terurut = (n − 1)·p + 1 (sama dengan bawaan `numpy.percentile` dan `pandas.quantile`).
10. **Tag butir:** tag seperti `[C3 · 1,5]` menyatakan level Bloom dan skor butir. Pada Bagian C dan D, skor dan level Bloom tiap sub-butir tertulis dalam kurung.
11. Seluruh data dalam latihan ini adalah **data rekaan**.

---

## Bagian A — Pilihan Ganda (15 butir, skor 20)

Lingkari **satu** jawaban yang paling tepat. Skor tiap butir (1 atau 1,5) tercantum pada tag butir.

**A1.** `[C3 · 1,5]`
Dataset pengguna sebuah dompet digital memuat kolom `id_pengguna` (bilangan bulat acak), `kota` (teks), `level_member` (Silver < Gold < Platinum), `saldo_rp` (desimal), dan `tahun_daftar` (bilangan bulat). Pasangan variabel → ringkasan atau pernyataan manakah yang **seluruhnya** sah?

- (a) `id_pengguna` → median; `level_member` → modus; `saldo_rp` → koefisien variasi
- (b) `kota` → modus; `level_member` → median; `saldo_rp` → "saldo X dua kali saldo Y"
- (c) `kota` → proporsi; `level_member` → rata-rata; `saldo_rp` → "saldo X tiga kali saldo Y"
- (d) `tahun_daftar` → "tahun 2024 sekian kali tahun 2012"; `kota` → modus; `saldo_rp` → mean

**A2.** `[C3 · 1,5]`
Untuk mengestimasi proporsi mahasiswa yang puas terhadap Wi-Fi kampus, tim mewawancarai 400 mahasiswa yang **sedang memakai Wi-Fi di perpustakaan** pada pukul 10.00–12.00. Hasilnya 74% menyatakan puas. Pernyataan manakah yang paling tepat?

- (a) Sampel kenyamanan; 74% tidak dapat digeneralisasi ke seluruh mahasiswa.
- (b) Karena n = 400 jauh di atas 30, sampel ini representatif bagi seluruh mahasiswa.
- (c) Ini sensus, karena semua pengguna perpustakaan pada jam itu ditanya.
- (d) Bias hilang bila hasilnya dilaporkan sebagai rata-rata, bukan proporsi.

**A3.** `[C2 · 1]`
Lama panggilan (menit) ke layanan pengaduan sebuah kota: sebagian besar 2–5 menit, tetapi beberapa panggilan darurat berlangsung lebih dari 30 menit. Pernyataan manakah yang paling mungkin benar?

- (a) Mean lebih kecil daripada median, karena panggilan panjang jumlahnya sedikit.
- (b) Mean kira-kira sama dengan median, karena sebagian besar panggilan 2–5 menit.
- (c) Modus pasti lebih besar daripada mean, karena modus tidak terpengaruh ekor.
- (d) Mean lebih besar daripada median, karena ekor kanan menarik mean ke atas.

**A4.** `[C2 · 1]`
Dua versi aplikasi presensi kampus memiliki mean waktu muat yang sama, 1,2 detik. Versi X: p95 = 1,8 detik. Versi Y: p95 = 6,5 detik. Pernyataan yang paling tepat adalah …

- (a) Kedua versi setara karena mean-nya sama, sehingga pengalaman pengguna pun sama.
- (b) Versi Y lebih baik, karena ekor yang panjang berarti sebagian pengguna dilayani sangat cepat.
- (c) Versi X lebih baik: 5% pengguna paling lambat di Y menunggu lebih dari 6,5 detik.
- (d) Kedua versi tidak dapat dibandingkan tanpa mengetahui modus waktu muat masing-masing.

**A5.** `[C2 · 1]`
Data waktu unggah berkas ke LMS mendapat satu nilai baru yang sangat besar (sebuah unggahan tersendat 15 menit). Pasangan ukuran manakah yang **paling sedikit** berubah?

- (a) Mean dan simpangan baku
- (b) Mean dan *range*
- (c) Median dan IQR
- (d) Simpangan baku dan *range*

**A6.** `[C3 · 1,5]`
Harga cabai rawit selama 30 hari di dua pasar sebuah kota: Pasar P rata-rata Rp60.000/kg dengan simpangan baku Rp9.000; Pasar Q rata-rata Rp45.000/kg dengan simpangan baku Rp7.200. Dengan memperhitungkan perbedaan tingkat harga kedua pasar, pernyataan yang paling tepat adalah …

- (a) Pasar P relatif lebih stabil, karena koefisien variasinya lebih kecil.
- (b) Pasar Q relatif lebih stabil, karena koefisien variasinya lebih kecil daripada P.
- (c) Pasar Q lebih stabil, karena simpangan bakunya Rp1.800 lebih kecil.
- (d) Kedua pasar sama stabil, karena koefisien variasinya sama.

**A7.** `[C3 · 1,5]`
Banyaknya aduan harian pada kanal pengaduan sebuah pemerintah daerah selama 360 hari memiliki Q1 = 40, median = 47, dan Q3 = 58. Kira-kira pada berapa hari banyaknya aduan berada di antara 47 dan 58?

- (a) Sekitar 11 hari
- (b) Sekitar 18 hari
- (c) Sekitar 90 hari
- (d) Sekitar 180 hari

**A8.** `[C3 · 1,5]`
Beban studi 40 mahasiswa pada satu semester: 18 SKS (6 orang), 20 SKS (14 orang), 21 SKS (12 orang), dan 24 SKS (8 orang). Median dan modus beban studi berturut-turut adalah …

- (a) 20 SKS dan 20 SKS
- (b) 20,5 SKS dan 20 SKS
- (c) 20,8 SKS dan 20 SKS
- (d) 21 SKS dan 24 SKS

**A9.** `[C3 · 1,5]`
Rata-rata ukuran 30 berkas tugas dari kelas X adalah 3,20 MB; rata-rata 20 berkas dari kelas Y adalah 3,45 MB. Rata-rata ukuran gabungan ke-50 berkas adalah …

- (a) 3,40 MB
- (b) 3,35 MB
- (c) 3,325 MB
- (d) 3,30 MB

**A10.** `[C3 · 1,5]`
Tim infrastruktur ingin melihat apakah latensi server naik seiring banyaknya pengguna serentak, **dan** apakah pola itu berbeda antara pusat data Jakarta dan pusat data Batam. Grafik yang paling tepat adalah …

- (a) Diagram pencar (*scatter plot*) pengguna serentak vs latensi, warna titik per pusat data
- (b) Diagram garis (*line chart*) rata-rata latensi harian, satu garis per pusat data
- (c) Diagram batang (*bar chart*) rata-rata latensi dan rata-rata pengguna per pusat data
- (d) Histogram latensi gabungan, dengan warna batang berbeda untuk tiap pusat data

**A11.** `[C3 · 1,5]`
Operator bus kota mengunggah grafik garis berjudul "Pengguna Aplikasi Tiket Terus Naik!". Grafik itu menampilkan pengguna aktif bulanan **Agustus–Desember 2025**: 40; 41,5; 43; 44; dan 45 ribu, dengan sumbu-y dimulai dari nol. Data lengkap operator: Januari 2025 tercatat 72 ribu pengguna aktif, lalu turun hampir setiap bulan sampai 40 ribu pada Agustus. Pernyataan yang paling tepat tentang grafik ini adalah …

- (a) Jujur, karena sumbu-y dimulai dari nol dan kelima angka yang ditampilkan benar.
- (b) Menyesatkan: rentang dipotong, padahal sepanjang 2025 pengguna turun ±37,5%.
- (c) Menyesatkan, karena data bulanan wajib disajikan dengan diagram batang.
- (d) Jujur asalkan sumber data dicantumkan di bawah grafik.

**A12.** `[C2 · 1]`
Seorang analis membuat histogram dari 2.000 data durasi sesi aplikasi dengan hanya 4 bin yang sangat lebar. Risiko utama pilihan ini adalah …

- (a) Histogram menjadi terlalu bergerigi sehingga derau tampak seperti pola.
- (b) Luas total histogram tidak lagi sebanding dengan banyaknya data.
- (c) Histogram berubah menjadi diagram batang kategori yang urutannya bebas.
- (d) Struktur penting, mis. dua puncak atau ekor panjang, tidak tampak.

**A13.** `[C3 · 1,5]`
Boxplot waktu pengiriman paket (jam) sebuah layanan logistik:

```
      ├────────[======|==============]──────────────────┤             ●
     12       20     26             40                 66            95   (jam)
```

*(Sketsa tidak berskala; gunakan angka yang tertera.)*

Ujung kumis bawah 12, Q1 = 20, median 26, Q3 = 40, ujung kumis atas 66, dan satu titik terpisah di 95. Pernyataan yang benar adalah …

- (a) Pagar atas pencilan 70 jam, sehingga titik 95 tergolong pencilan.
- (b) Rata-rata waktu pengiriman adalah 26 jam (garis di dalam kotak).
- (c) 25% pengiriman memerlukan lebih dari 66 jam.
- (d) Sebaran menceng ke kiri karena median lebih dekat ke Q1 daripada ke Q3.

**A14.** `[C2 · 1]`
Grafik garis berjudul "Tren Pengguna Aktif Aplikasi Kampus" dalam sebuah laporan tidak mencantumkan satuan sumbu-y, sumber data, dan periode pengambilan data. Masalah utama grafik ini adalah …

- (a) Grafik garis tidak boleh dipakai untuk data deret waktu.
- (b) Hanya masalah estetika; isi datanya tetap sama.
- (c) Klaim tren tidak dapat diverifikasi oleh pembaca.
- (d) Grafik seharusnya diganti diagram lingkaran.

**A15.** `[C3 · 1,5]`
Komposisi tujuh kategori aduan layanan internet kampus berkisar antara 12% dan 17% per kategori. Pengelola ingin pembaca dapat **mengurutkan** kategori dengan tepat. Pilihan grafik terbaik adalah …

- (a) Diagram lingkaran tiga dimensi yang dimiringkan
- (b) Diagram lingkaran dengan tujuh warna berbeda
- (c) Histogram persentase ketujuh kategori aduan
- (d) Diagram batang terurut, sumbu mulai dari nol

---

## Bagian B — Isian / Hitungan Pendek (8 butir, skor 25)

Tuliskan langkah singkat dan jawaban akhir.

**B1.** `[C3 · 2]`
Kolom `kode_pos` alamat mahasiswa disimpan bertipe bilangan bulat. Lima data: 12110, 12110, 16424, 12110, 40132. Seorang analis melaporkan "rata-rata kode pos mahasiswa = 18.577,2".

- (a) Tentukan skala pengukuran `kode_pos` dan jelaskan mengapa angka 18.577,2 tidak bermakna. *(1)*
- (b) Hitung satu ringkasan yang sah untuk kelima data itu beserta nilainya. *(1)*

**B2.** `[C3 · 2]`
Waktu *boot* (detik) **seluruh** lima server di ruang server sebuah laboratorium: 30, 34, 31, 37, 33. Hitung varians dan simpangan baku yang tepat untuk data ini, dan beri alasan pemilihan penyebutnya.

**B3.** `[C3 · 3]`
Aplikasi kuis daring menyusun satu paket latihan: **3 dari 9** soal logika ditampilkan satu per satu secara **berurutan** (urutan tampil dibedakan), lalu **2 dari 7** soal statistika ditampilkan **bersamaan dalam satu halaman** (urutan tidak dibedakan). Berapa banyak paket berbeda yang dapat disusun? Jelaskan mengapa Anda memakai permutasi atau kombinasi pada tiap bagian.

**B4.** `[C3 · 3]`
Model klasifikasi aduan warga memberi keluaran probabilitas untuk satu aduan: Banjir 0,42; Sampah 0,25; Jalan rusak 0,21; Lainnya 0,15. Keempat kategori saling lepas dan mencakup semua kemungkinan.

- (a) Apakah keluaran ini sah sebagai distribusi probabilitas? Rujuk aksioma yang relevan. *(1)*
- (b) Bila hanya nilai "Lainnya" yang keliru, berapa nilai yang benar? *(1)*
- (c) Dengan nilai terkoreksi, hitung P(bukan Banjir) dan P(Sampah ∪ Jalan rusak). *(1)*

**B5.** `[C3 · 4]`
Seleksi beasiswa prestasi sebuah yayasan berlangsung dalam tiga tahap berurutan: seleksi berkas, tes daring, dan wawancara. Pendaftar yang gugur di satu tahap tidak mengikuti tahap berikutnya. P(lolos berkas) = 0,6; P(lolos tes | lolos berkas) = 0,5; P(lolos wawancara | lolos tes) = 0,8.

- (a) Hitung probabilitas seorang pendaftar diterima. *(2)*
- (b) Seorang pendaftar diketahui **tidak** diterima. Berapa probabilitas ia gugur di tahap berkas? *(2)*

**B6.** `[C3 · 4]`
Sensor kualitas udara di sebuah halte mengirim data lewat jaringan seluler. Setiap percobaan kirim berhasil dengan peluang 0,7, saling bebas antarpercobaan, dan perangkat terus mengulang sampai berhasil. Misalkan X = banyaknya percobaan sampai berhasil pertama kali.

- (a) Tentukan distribusi X beserta parameternya, lalu hitung E[X]. *(1)*
- (b) Tim ingin membatasi banyaknya percobaan. Tentukan batas k terkecil agar peluang data terkirim dalam paling banyak k percobaan sedikitnya 0,99. *(1,5)*
- (c) Perangkat sudah gagal dua kali. Berapa probabilitas ia masih memerlukan lebih dari 3 percobaan **tambahan**? Sifat apa yang Anda gunakan? *(1,5)*

**B7.** `[C3 · 3]`
Sistem kendali mutu sebuah UMKM kopi menimbang setiap kemasan berlabel 250 g. Berat isi kemasan berdistribusi Normal dengan μ = 252 g dan σ = 4 g. Dengan tabel Normal baku, hitung:

- (a) proporsi kemasan yang beratnya di bawah label (< 250 g); *(1,5)*
- (b) proporsi kemasan yang beratnya antara 248 g dan 258 g. *(1,5)*

**B8.** `[C3 · 4]`
Daya tahan baterai (jam pemakaian normal) sebuah model ponsel berdistribusi Normal dengan μ = 30 jam dan σ = 4 jam.

- (a) Produsen ingin menetapkan batas garansi T sehingga hanya 3% ponsel memiliki daya tahan di bawah T. Tentukan T dengan tabel Normal baku. *(2,5)*
- (b) Tanpa tabel, gunakan aturan empiris 68–95–99,7 untuk memperkirakan persentase ponsel dengan daya tahan lebih dari 38 jam. *(1,5)*

---

## Bagian C — Uraian Terstruktur (4 butir, skor 40)

Jawaban dinilai pada empat aspek: ketepatan prosedur (35%), ketepatan hitung (25%), kecocokan asumsi (20%), dan validitas interpretasi (20%).

### C1. Durasi Penanganan Tiket Gangguan `[C3–C4 · 10]`

Unit Layanan TI kampus mencatat durasi penyelesaian (jam) sembilan tiket gangguan yang dipilih acak dari tiap gedung pada September 2026.

- **Gedung A:** 3, 4, 4, 5, 6, 6, 7, 8, 20 — jumlah kuadrat simpangan terhadap mean sudah dihitung: Σ(x − x̄)² = 210
- **Gedung B** (ringkasan sudah dihitung): n = 9; x̄ = 7,00; s = 2,55; min = 4; Q1 = 5; median = 7; Q3 = 9; maks = 10

(a) Untuk Gedung A, hitung mean, median, simpangan baku sampel, Q1, Q3, IQR, dan batas pencilan 1,5×IQR; tentukan nilai yang tergolong pencilan. *(4 poin · C3)*

(b) Kepala unit menulis: *"Rata-rata kedua gedung sama-sama 7 jam, jadi kinerja penanganan gangguan keduanya setara."* Analisis klaim ini dengan ukuran pemusatan **dan** ukuran penyebaran yang tepat. Gunakan hasil (a) dan ringkasan Gedung B; tidak perlu menghitung ukuran baru. Jawab dalam paling banyak 3 kalimat. *(2 poin · C4)*

(c) Boxplot Gedung B sudah digambar pada sumbu di bawah. Sketsa boxplot Gedung A di atasnya pada sumbu yang sama; tandai Q1, median, Q3, ujung kumis, dan pencilan. *(2 poin · C3)*

```
Gedung A

Gedung B              ├──[=====|=====]──┤
          +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+--
          0     2     4     6     8     10    12    14    16    18    20    22   (jam)
```

(d) Belakangan diketahui bahwa delapan dari sembilan tiket Gedung B terdiri atas dua jenis: gangguan jaringan (selesai 4–5 jam) dan penggantian perangkat keras (selesai 9–10 jam); satu tiket lain selesai 7 jam. Apa yang **tidak** tampak pada boxplot Gedung B, dan grafik apa yang Anda usulkan agar hal itu terlihat? Beri alasan. Jawab dalam paling banyak 3 kalimat. *(2 poin · C4)*

### C2. Kegagalan Transaksi Marketplace `[C3–C4 · 10]`

Rekap satu minggu 1.200 transaksi pada sebuah *marketplace* produk UMKM:

| Metode bayar | Berhasil | Gagal | Total |
|---|---|---|---|
| QRIS | 540 | 36 | 576 |
| *Virtual account* (VA) | 384 | 24 | 408 |
| Bayar di tempat (COD) | 180 | 36 | 216 |
| **Total** | **1.104** | **96** | **1.200** |

Satu transaksi dipilih acak dari 1.200 transaksi tersebut.

(a) Hitung P(gagal), P(gagal | COD), dan P(COD | gagal), lalu hitung P(COD ∪ gagal) dengan aturan penjumlahan umum. *(3,5 poin · C3)*

(b) Tim audit memilih acak 3 dari 96 transaksi gagal (tanpa pengembalian) untuk ditelusuri. Ada berapa himpunan 3 transaksi yang mungkin? Hitung probabilitas **tepat 2** dari 3 transaksi itu adalah transaksi COD. Jelaskan aturan pencacahan yang Anda pakai. *(4 poin · C3)*

(c) Manajer produk berkata: *"Kegagalan terutama disebabkan COD, jadi hapus saja COD."* Analis data membalas: *"Sebagian besar kegagalan justru bukan berasal dari COD."* Analisislah kedua pernyataan dengan hasil (a) dan laju kegagalan QRIS, P(gagal | QRIS), lalu tuliskan kesimpulan yang tidak melampaui data. Jawab dalam paling banyak 3 kalimat. *(2,5 poin · C4)*

### C3. Detektor Teks-AI dan Prinsip *Tabayyun* `[C3–C4 · 10]`

Sebuah perguruan tinggi menguji coba detektor teks-AI untuk laporan tugas. Laporan yang penggunaan AI-nya sudah diungkapkan di AI Usage Log tidak diperiksa detektor. Dari laporan yang diperiksa, audit semester lalu memperkirakan 5% ditulis AI tanpa diungkapkan dan sisanya (95%) ditulis sendiri. Uji internal menunjukkan detektor **menandai** 90% laporan yang ditulis AI tanpa diungkapkan dan **tidak menandai** 97% laporan yang ditulis sendiri.

(a) Tuliskan prior, *likelihood*, dan *evidence* dalam notasi, dan sebutkan asumsi yang Anda pakai tentang prior 5%. Hitung P(ditandai) dengan hukum probabilitas total, lalu P(AI | ditandai) dengan Teorema Bayes. *(3 poin · C3)*

(b) Lengkapi tabel frekuensi harapan untuk 2.000 laporan yang diperiksa. Dari tabel itu hitung P(ditulis sendiri | tidak ditandai). *(2 poin · C3)*

| 2.000 laporan yang diperiksa | Ditandai | Tidak ditandai | Total |
|---|---|---|---|
| Ditulis AI tanpa diungkapkan | | | |
| Ditulis sendiri | | | |
| **Total** | | | **2.000** |

(c) Laporan yang ditandai diperiksa detektor kedua dengan sensitivitas 85% dan spesifisitas 98%. Anggap hasil kedua detektor saling bebas bila status sebenarnya laporan diketahui (asumsi seperti pada Naive Bayes). Bila detektor kedua juga menandai, hitung probabilitas laporan itu ditulis AI. Lalu analisis apakah asumsi bebas bersyarat itu masuk akal untuk dua detektor teks-AI, beserta alasannya, dalam paling banyak 2 kalimat. *(2,5 poin · C3–C4)*

(d) Seorang pimpinan mengusulkan: *"Setiap laporan yang ditandai detektor pertama langsung diberi nilai nol."* Analisis usulan ini dengan angka dari (a)–(c), keterbatasan angka uji internal dan audit yang Anda pakai, serta prinsip *tabayyun* — memeriksa kebenaran sebelum menjatuhkan tuduhan (QS Al-Hujurat [49]: 6) — lalu usulkan **satu** langkah prosedur yang membuat keputusan lebih adil. Jawab dalam paling banyak 4 kalimat. *(2,5 poin · C4)*

### C4. Server Replika LMS `[C3–C4 · 10]`

LMS kampus dan basis datanya dijalankan pada beberapa server replika di pusat data kampus.

(a) Log 500 hari mencatat server S1 mati pada 25 hari, S2 mati pada 20 hari, dan keduanya mati pada hari yang sama sebanyak 9 hari. Ujilah apakah kejadian "S1 mati" dan "S2 mati" saling bebas memakai definisi formal. Apakah kedua kejadian itu saling lepas? Tafsirkan hasilnya bagi tim infrastruktur dalam paling banyak 2 kalimat. *(3 poin · C4)*

(b) Untuk keperluan perancangan, anggap setiap server tersedia dengan peluang 0,96, saling bebas. Dalam rancangan awal, semua permintaan masuk lewat satu *load balancer* (penyeimbang beban) yang tersedia dengan peluang 0,99, bebas dari server, lalu diteruskan ke tiga server aplikasi yang masing-masing merupakan replika penuh (cukup satu server hidup). Hitung keandalan layanan dari sisi pengguna. Keandalan layanan itu mendekati nilai berapa bila banyaknya replika terus ditambah? *(2 poin · C3)*

(c) Basis data LMS berjalan pada klaster empat server (S1–S4) dengan aturan **kuorum mayoritas**: klaster berfungsi bila **sedikitnya 3 dari 4** server hidup. Dengan peluang dan asumsi kebebasan pada (b), periksa syarat BINS, lalu hitung keandalan klaster dengan distribusi Binomial serta rata-rata banyaknya server yang hidup. *(3 poin · C3)*

(d) Berdasarkan temuan **uji kebebasan** di (a), syarat BINS mana yang tidak terpenuhi dalam kenyataan? Apakah angka di (c) terlalu optimistis atau terlalu pesimistis? Jelaskan dalam paling banyak 3 kalimat. *(2 poin · C4)*

---

## Bagian D — Studi Kasus Terpadu (1 butir, skor 15)

`[C4 · 15]` — butir utuh C4; skor dan level Bloom tiap sub-butir tertulis dalam kurung.

### Sistem Antrean Daring Rawat Jalan

Tim TI sebuah rumah sakit daerah mengelola sistem antrean daring untuk pendaftaran pasien rawat jalan. Log satu minggu (7 hari × 24 jam = 168 jam) memuat 1.400 pendaftaran dengan variabel berikut.

| Variabel | Contoh isi |
|---|---|
| `no_antrean` | B-017 |
| `poli` | Anak, Gigi, Penyakit Dalam, Mata |
| `waktu_tunggu_menit` | 0 sampai 260 |
| `status_sistem` | sukses / galat |
| `rating_kepuasan` | 1–5 bintang, diisi sukarela setelah dilayani (252 dari 1.400 pasien mengisi) |
| `jam_daftar` | 06.45, 07.10, 13.30, … |

**Ringkasan `waktu_tunggu_menit`** (n = 1.400): mean 47; median 31; Q1 18; Q3 52; p95 140; maks 260.

**Galat sistem per jam** selama 168 jam (total 298 galat):

| Periode | Banyak jam | Mean galat per jam | Varians galat per jam |
|---|---|---|---|
| Seluruh jam | 168 | 1,77 | 2,21 |
| Jam sibuk 07.00–10.00 | 21 | 3,62 | 3,25 |
| Jam lainnya | 147 | 1,51 | 1,53 |

**Catatan tim jaringan:** 70% galat bersumber dari gangguan jaringan dan 30% dari *bug* aplikasi. Galat jaringan memunculkan kode HTTP 504 pada 80% kasus; galat *bug* memunculkan kode 504 pada 10% kasus.

**D1.** Tentukan skala pengukuran `waktu_tunggu_menit`, `rating_kepuasan`, dan `jam_daftar`. Untuk `rating_kepuasan`, tentukan satu ukuran pemusatan yang sah. *(2 poin · C3)*

**D2.** Direktur meminta angka "waktu tunggu yang dialami pasien". Pilih ukuran yang akan Anda laporkan (boleh lebih dari satu) dan beri alasan berdasarkan bentuk sebaran. Seorang staf mengusulkan membuang semua data di atas batas pencilan 1,5×IQR "agar laporan bersih"; hitung batas itu dan analisis usulan tersebut. Jawab dalam paling banyak 3 kalimat di luar hitungan. *(3 poin · C4)*

**D3.** Pilih distribusi untuk memodelkan banyaknya galat sistem per jam dan tuliskan parameternya. Tuliskan dua asumsi yang harus dipenuhi, lalu periksa kelayakannya dengan tabel galat di atas. Apa keputusan pemodelan Anda? Jawab dalam paling banyak 4 kalimat di luar hitungan. *(3 poin · C4)*

**D4.** Untuk jam di luar 07.00–10.00, gunakan laju 1,5 galat per jam. (i) Berapa rata-rata waktu antargalat dalam menit? (ii) Hitung probabilitas tidak ada galat selama 45 menit ke depan dengan distribusi Eksponensial. (iii) Tanpa menghitung ulang, jelaskan dalam satu kalimat mengapa distribusi Poisson untuk banyaknya galat dalam 45 menit itu memberi probabilitas yang sama. *(3 poin · C3)*

**D5.** Sebuah galat dengan kode 504 baru saja muncul. Hitung probabilitas galat itu bersumber dari gangguan jaringan. Tim mana yang sebaiknya dihubungi lebih dulu, dan berapa probabilitas pilihan itu keliru? *(3 poin · C3)*

**D6.** Tuliskan **satu** kesimpulan yang **tidak** dapat ditarik dari data ini, dan jelaskan mengapa, dalam paling banyak 2 kalimat. *(1 poin · C4)*

---

**— Selesai. Periksa kembali satuan dan pembulatan, lalu cocokkan jawaban Anda dengan [pembahasan dan pedoman skor](latihan-uts-pembahasan.md). —**

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
