# Minggu 4: Pembagian Data dan Kebocoran Data

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 4 dari 16 |
| Topik | *Train/validation/test*, validasi silang, enam jenis kebocoran data |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-04 |
| Bloom | C2 (Memahami) → C3 (Menerapkan) → C4 (Menganalisis) |
| Durasi | 150 menit |
| Metode | Kuliah · Simulasi · Demonstrasi kegagalan · Praktikum |
| Penilaian | Observasi (Lab 4) · **Kuis 1** |
| Buku ajar | [Bab 4](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md) |

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Menjelaskan** (C2) peran berbeda antara data latih, validasi, dan uji.
2. **Menerapkan** (C3) strategi pembagian data yang sesuai sifat datanya: acak, stratifikasi, temporal, atau berkelompok.
3. **Menerapkan** (C3) validasi silang dan menafsirkan sebaran skor antarlipatan.
4. **Menganalisis** (C4) sebuah *pipeline* dan menemukan kebocoran data di dalamnya.
5. **Memperbaiki** (C5) kebocoran yang ditemukan dan melaporkan dampaknya terhadap skor.

---

## Cara Memakai Modul Ini

Modul ini adalah **panduan dosen**. Penjelasan lengkap, contoh kecil, dan jawaban *Cek Pemahaman* berada di [Bab 4](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md). Modul ini tidak mengulangnya, melainkan memuat **urutan mengajar**: apa yang dikatakan, pertanyaan yang diajukan, simulasi yang dijalankan, kekeliruan yang biasa muncul, dan cara memastikan mahasiswa memahami sebelum lanjut.

**Prinsip yang dipakai sepanjang pertemuan:**

| Prinsip | Wujud di kelas |
|---------|----------------|
| **Pengalaman dahulu, istilah kemudian** | Mahasiswa menebak dan mencoba sebelum diberi nama konsepnya |
| **Satu konsep pada satu waktu** | Tiap konsep diberi ruang dan diperiksa sebelum konsep berikutnya |
| **Menebak sebelum melihat hasil** | Mahasiswa menuliskan perkiraan angka terlebih dahulu |
| **Hitung kecil sebelum kode** | Data sepuluh baris dihitung dengan tangan, lalu dicocokkan dengan komputer |
| **Periksa pemahaman, bukan sekadar bertanya "sudah paham?"** | Mahasiswa menjawab soal singkat, bukan mengangguk |

---

## Peta Materi

| Bagian Bab 4 | Konsep | Bukti yang ditunjukkan di kelas |
|--------------|--------|----------------------------------|
| §4.1 | Mengapa kebocoran berbahaya | Analogi soal latihan yang bocor |
| §4.2 | Tiga peran data; data uji hanya sekali | 30 model penebak acak: skor terbaik **0,644** padahal kemampuan sebenarnya 0,5 |
| §4.3.1–4.3.2 | Pembagian acak dan stratifikasi | 12 penipuan dari 1.000 transaksi: peluang data uji kosong **6,8%** |
| §4.3.3 | Pembagian temporal | Galat acak **2,65** versus temporal **18,82** |
| §4.3.4 | Pembagian berkelompok | Akurasi acak **0,996** versus berkelompok **0,497** pada data tanpa pola |
| §4.4 | Validasi silang | 10 data, 5 lipatan, rerata dan simpangan baku dihitung dengan tangan |
| §4.5 | Enam jenis kebocoran | Notebook demonstrasi berisi empat kebocoran |
| §4.6 | Daftar periksa | Dipakai pada penutup dan Lab 4 |

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

Tugas prakelas dibuat ringan dan terarah agar waktu kelas dipakai untuk memahami, bukan membaca ulang.

| Langkah | Kegiatan | Durasi |
|---------|----------|--------|
| 1 | Menjawab enam soal **Pemanasan** (Bab 4 §4.1.1) secara tertulis tanpa melihat catatan | 10' |
| 2 | Membaca Bab 4 §4.1 sampai §4.4 dan menjawab setiap *Tebak Dahulu* secara tertulis | 35' |
| 3 | Membaca Bab 4 §4.5 (enam jenis kebocoran) sebagai bahan Kuis 1 | 15' |

Mahasiswa membawa jawaban tertulis ke kelas. Kekeliruan pada *Tebak Dahulu* **tidak dinilai**. Kekeliruan itu bahan diskusi.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| 1. Pembuka dan pengaktifan ingatan | 10' | Tiga soal ingatan; pembahasan T-03 |
| 2. **Kuis 1** | 20' | Kualitas data, prapemrosesan, jenis kebocoran |
| 3. Konsep | 35' | Soal bocor; tiga peran data; simulasi; empat strategi; validasi silang |
| 4. Demonstrasi | 35' | **Kegiatan inti:** notebook dengan empat kebocoran |
| 5. Praktik | 40' | Mulai Lab 4 |
| 6. Penutup | 10' | Daftar periksa; tiket keluar |

Setiap segmen dijabarkan di bawah dengan format yang sama: **tujuan**, **yang dilakukan**, **pertanyaan dan jawaban yang diharapkan**, **kekeliruan yang biasa muncul**, dan **tanda mahasiswa siap lanjut**.

---

#### Segmen 1 — Pembuka dan Pengaktifan Ingatan (10 menit)

**Tujuan.** Mengaktifkan pengetahuan yang diandalkan pertemuan ini sebelum konsep baru diberikan.

**Yang dilakukan.** Tampilkan tiga soal berikut satu per satu. Mahasiswa menuliskan jawaban pada kertas atau kolom jajak pendapat selama satu menit, kemudian dosen membahas.

| Soal | Jawaban yang diharapkan | Bila banyak yang keliru |
|------|--------------------------|--------------------------|
| 1. Apa beda `fit` dan `transform`? | `fit` mempelajari nilai dari data; `transform` memakai nilai itu untuk mengubah data | Peragakan dengan tiga angka: hitung rerata (fit), lalu kurangkan (transform). Ini fondasi kebocoran prapemrosesan |
| 2. Rerata dan simpangan baku mengukur apa? | Pusat dan sebaran data | Tulis dua kumpulan angka dengan rerata sama dan sebaran berbeda (lihat Bab 4 §4.4.4) |
| 3. Apa fungsi `Pipeline`? | Merangkai langkah menjadi satu kesatuan sehingga `fit` hanya terjadi pada data latih | Tunda penjelasan lengkap ke segmen 4; cukup katakan "hari ini kita akan melihat alasannya" |

**Kemudian.** Bahas T-03 selama 5 menit: dua kesalahan paling sering pada pekerjaan Minggu 3. Jangan menyebut nama mahasiswa.

**Tanda siap lanjut.** Lebih dari separuh kelas menjawab soal 1 dengan benar. Bila kurang, tambahkan peragaan singkat pada soal 1.

---

#### Segmen 2 — Kuis 1 (20 menit)

Pelaksanaan dan cakupan **tidak berubah**: kualitas data, prapemrosesan, dan jenis kebocoran (dari bacaan prakelas). Kuis dikerjakan tertulis dan perorangan, dengan **alasan tertulis** (bobot 60% pada rubrik kuis).

Tujuan segmen ini ganda: menilai, dan **memperlihatkan** bagian yang belum dikuasai sehingga dosen dapat menyesuaikan segmen 3.

**Catatan dosen.** Catat tiga soal dengan jawaban salah terbanyak. Segmen 3 kembali pada konsep tersebut.

---

#### Segmen 3 — Konsep (35 menit)

Segmen ini terdiri atas **empat bagian**. Berpindahlah ke bagian berikutnya **hanya** bila tanda siap lanjut terpenuhi.

##### Bagian A — Soal yang Bocor (8 menit)

**Tujuan.** Mahasiswa memahami *mengapa* kebocoran membuat skor menyesatkan, tanpa istilah teknis.

**Yang dikatakan** (contoh ujaran):

> "Seorang dosen membagikan soal latihan. Ternyata sebagian besar sama persis dengan soal ujian. Seorang mahasiswa menghafalnya dan mendapat nilai 95. Pertanyaan saya: apakah nilai itu membuktikan ia **paham materi**?"

**Yang dilakukan.**

1. Beri 1 menit. Mahasiswa menuliskan jawaban dan satu alasan.
2. Minta tiga mahasiswa membacakan. Biasanya muncul "tidak, ia hanya menghafal".
3. Lanjutkan:

> "Bagaimana kalau semua soal diganti soal baru? Itulah yang kita ukur ketika menguji model: kemampuan pada soal yang **belum pernah dilihat**. Bila soal ujian sudah ikut dipakai belajar, skornya tinggi tetapi menyesatkan. Itulah **kebocoran data**."

4. Tunjukkan analogi tiga tahap pada Bab 4 §4.2.1: buku latihan = data latih, tryout = data validasi, ujian akhir = data uji.

**Pertanyaan dan jawaban yang diharapkan.**

| Pertanyaan | Jawaban yang diharapkan |
|------------|--------------------------|
| "Boleh mengulang tryout?" | Boleh, tryout memang untuk berlatih |
| "Boleh mengulang ujian akhir sambil memperbaiki cara belajar dari hasilnya?" | Tidak. Nilainya tidak lagi mencerminkan kemampuan baru |

**Kekeliruan yang biasa muncul.**

| Kekeliruan | Cara meluruskan |
|------------|-----------------|
| "Skor tinggi berarti model bagus" | Tanyakan: "Untuk nilai 95 tadi, bagus untuk apa? Menghafal atau memahami?" |
| "Kebocoran itu kesalahan yang jelas terlihat" | Tegaskan: kebocoran **tidak menghasilkan pesan galat**. Ia menghasilkan skor bagus |

**Tanda siap lanjut.** Mahasiswa dapat menjelaskan dengan kata sendiri mengapa nilai 95 dari soal bocor tidak membuktikan pemahaman.

##### Bagian B — Simulasi: 30 Penebak Acak (9 menit)

**Tujuan.** Mahasiswa **mengalami sendiri** bahwa memilih berdasarkan skor uji menghasilkan skor yang menyesatkan.

**Yang dikatakan.**

> "Saya punya 30 model. Semuanya **hanya menebak acak**, kemampuan sebenarnya 50%. Data uji berisi 50 baris. Saya memilih model dengan skor uji tertinggi. **Tuliskan perkiraan Anda**: berapa skor model terbaik itu? Dan bila dipakai pada data baru, berapa skornya?"

**Yang dilakukan.**

1. Beri 1 menit. Mahasiswa menuliskan dua angka.
2. Dosen menjalankan kode berikut **secara langsung**:

```python
import numpy as np

rng = np.random.default_rng(42)
y_uji = rng.integers(0, 2, size=50)

skor = []
for model in range(30):
    tebakan = rng.integers(0, 2, size=50)
    skor.append((tebakan == y_uji).mean())

print("Rerata ke-30 model :", round(np.mean(skor), 3))   # 0.496
print("Skor model terbaik :", max(skor))                 # 0.64
```

3. Tampilkan hasil: rerata **0,496**, terbaik **0,64**. Bandingkan dengan perkiraan mahasiswa.
4. Sampaikan: "Bila percobaan ini diulang 1.000 kali, rerata skor terbaik adalah **0,644**."

**Pertanyaan dan jawaban yang diharapkan.**

| Pertanyaan | Jawaban yang diharapkan |
|------------|--------------------------|
| "Mengapa skor terbaik 0,64 padahal semua model hanya menebak?" | Karena kebetulan. Dari 30 percobaan, pasti ada yang kebetulan tinggi |
| "Skor model itu pada data baru?" | Kembali ke sekitar 0,5 |
| "Apa hubungannya dengan data uji hanya sekali?" | Setiap kali memilih berdasarkan skor uji, kita memilih berdasarkan kebetulan pada data itu |

**Kekeliruan yang biasa muncul.**

| Kekeliruan | Cara meluruskan |
|------------|-----------------|
| "Berarti 30 model ini sebenarnya cukup baik, 0,64" | Ingatkan: semuanya penebak acak. Kemampuan sebenarnya 0,5 |
| "Cukup pilih yang terbaik, itu sudah wajar" | Pilih memakai **data validasi**, lalu ukur sekali pada data uji |

**Tanda siap lanjut.** Mahasiswa dapat menjawab Cek Pemahaman 4.2 (Bab 4): kekeliruan memilih model berdasarkan skor uji, dan perbaikannya.

##### Bagian C — Empat Strategi Pembagian (10 menit)

**Tujuan.** Mahasiswa memilih strategi dengan **tiga pertanyaan berurutan**, bukan menghafal tabel.

**Yang dilakukan.** Tampilkan empat situasi berturut-turut. Untuk setiap situasi, mahasiswa menebak lebih dahulu **apa yang salah bila dibagi acak**, lalu dosen menyingkap hasilnya.

| Situasi | Tebak: apa masalah bila dibagi acak? | Bukti | Strategi |
|---------|---------------------------------------|-------|----------|
| 1.000 transaksi, 12 penipuan (1,2%) | Data uji bisa tidak berisi penipuan | Peluang data uji kosong **6,8%**; harapan 2,4 kasus | **Stratifikasi** |
| Penjualan harian 120 hari, cenderung naik | Model mengintip masa depan | Galat acak **2,65** vs temporal **18,82** | **Temporal** |
| 8.000 kunjungan dari 900 pasien | Pasien yang sama ada di latih dan uji | Akurasi **0,996** vs **0,497** pada data tanpa pola | **Berkelompok** |
| 1.000 siswa, kelas seimbang, saling lepas | Tidak ada masalah khusus | — | **Acak** |

**Yang dikatakan** (setelah keempat situasi):

> "Jangan menghafal. Untuk setiap data baru, tanyakan tiga hal berurutan: apakah ada urutan waktu? Apakah satu entitas muncul berulang? Apakah kelas sangat tidak seimbang? Jawabannya menentukan strategi." (Bab 4 §4.3.5)

**Kekeliruan yang biasa muncul.**

| Kekeliruan | Cara meluruskan |
|------------|-----------------|
| "Acak selalu paling adil" | Tunjukkan baris penjualan harian: acak tampak paling baik padahal ia mengintip |
| "Stratifikasi sama dengan pembagian berkelompok" | Stratifikasi menjaga **proporsi kelas**; berkelompok menjaga **entitas tidak terpisah**. Keduanya menjawab pertanyaan berbeda |
| "Skor lebih tinggi berarti strateginya lebih baik" | Skor yang lebih tinggi pada pembagian yang salah adalah **tanda bahaya** |

**Tanda siap lanjut.** Mahasiswa menjawab Cek Pemahaman 4.3.3 (curah hujan 10 tahun dibagi acak) dengan benar.

##### Bagian D — Validasi Silang dengan Hitungan Tangan (8 menit)

**Tujuan.** Mahasiswa memahami validasi silang sebagai **giliran**, lalu membaca rerata dan simpangan baku.

**Yang dilakukan.**

1. Tampilkan tabel 10 data dan 5 lipatan (Bab 4 §4.4.2). Tunjuk satu putaran: "Pada putaran 1, data 0 dan 1 menjadi validasi, delapan lainnya menjadi latih."
2. Tanyakan: "Berapa kali data nomor 4 menjadi validasi? Berapa kali menjadi latih?" (Jawaban: sekali dan empat kali.)
3. Hitung bersama rerata dan simpangan baku skor 0,62; 0,89; 0,58; 0,91; 0,70 **di papan**:
   - rerata = 0,74
   - kuadrat selisih berjumlah 0,0930
   - ragam sampel = 0,0930 ÷ 4 = 0,02325
   - simpangan baku sampel ≈ 0,153
4. Tunjukkan perbandingan: {0,79; 0,80; 0,81} dan {0,60; 0,80; 1,00} sama-sama rerata 0,80, tetapi simpangan baku 0,01 dan 0,20.

**Kekeliruan yang biasa muncul.**

| Kekeliruan | Cara meluruskan |
|------------|-----------------|
| "Validasi silang melatih lima model yang berbeda lalu memilih yang terbaik" | Setiap putaran melatih ulang model dengan konfigurasi **yang sama**, untuk menaksir kinerja, bukan memilih lipatan |
| "Cukup lapor rerata" | Perlihatkan dua kumpulan skor tadi |
| "`std()` selalu benar" | `skor.std()` memakai pembagi n (0,136); simpangan sampel memakai n − 1 (0,153). Sebutkan yang dipakai |
| "Validasi silang dilakukan pada seluruh data termasuk data uji" | Dilakukan pada **data latih**; data uji disimpan untuk sekali di akhir |

**Tanda siap lanjut.** Mahasiswa menghitung sendiri rerata pada Soal 8(a) dan menyatakan hasil sebagai "0,74 ± 0,15".

---

#### Segmen 4 — Demonstrasi: Empat Kebocoran Tersembunyi (35 menit)

**Tujuan.** Mahasiswa **melihat** dampak nyata tiap kebocoran dan belajar bahwa memperbaikinya menurunkan skor.

**Persiapan dosen.** Siapkan notebook yang sengaja berisi empat kebocoran:

1. `StandardScaler` di-*fit* sebelum pembagian (prapemrosesan)
2. Pemilihan fitur berdasarkan korelasi terhadap target pada seluruh data (pemilihan)
3. Data deret waktu dibagi secara acak (temporal)
4. Kolom yang merupakan turunan langsung dari target (target)

Skor sebelum perbaikan: 0,97. Setelah keempatnya diperbaiki: 0,71. **Selisih inilah pelajarannya.**

**Yang dilakukan, satu kebocoran pada satu waktu** (± 7 menit masing-masing; 7 menit sisanya untuk pembuka dan rekap):

| Langkah | Dosen | Mahasiswa |
|---------|-------|-----------|
| 1. Tampilkan sel yang berisi kebocoran **tanpa menyebut** namanya | Jalankan, tunjukkan skor | Menuliskan: "Apakah ada yang janggal di sel ini?" |
| 2. Tebak | "Bila ini diperbaiki, skornya naik, turun, atau tetap? Berapa kira-kira?" | Menuliskan perkiraan angka |
| 3. Perbaiki | Ubah kode dan jalankan | Mengamati |
| 4. Bandingkan | Isi tabel di papan | Mencocokkan dengan perkiraan |
| 5. Nama dan mekanisme | Sebut jenis kebocoran dan **mengapa** skor turun | Menyalin jenis dan mekanisme dengan kata sendiri |

**Tabel untuk diisi bersama:**

| Tahap | Kebocoran yang diperbaiki | Skor sesudah | Penurunan |
|-------|---------------------------|--------------|-----------|
| Awal | — | 0,97 | — |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | 0,71 | |

Isi kolom skor sesudah sesuai hasil notebook yang disiapkan. Tabel ini adalah **bukti yang dibawa mahasiswa ke praktik**.

**Pertanyaan pancingan di akhir demonstrasi.**

| Pertanyaan | Jawaban yang diharapkan |
|------------|--------------------------|
| "Skor mana yang lebih berguna bagi perusahaan, 0,97 atau 0,71?" | 0,71, karena itulah gambaran kinerja pada data baru |
| "Mengapa tidak ada pesan galat pada notebook awal?" | Kode benar secara sintaksis. Kebocoran adalah kesalahan **logika** |
| "Kebocoran mana yang paling sulit ditemukan?" | Kebocoran target dan temporal, karena bergantung pada **arti kolom**, bukan pada kode |

**Kekeliruan yang biasa muncul.**

| Kekeliruan | Cara meluruskan |
|------------|-----------------|
| "Skor turun, berarti perbaikan merusak model" | Skor turun karena skor awal **menyesatkan**. Yang dibandingkan adalah keadaan jujur dengan keadaan tidak jujur |
| "Cukup memakai `Pipeline`, semua kebocoran hilang" | `Pipeline` mencegah satu jenis. Kebocoran temporal, duplikat, kelompok, dan target tetap memerlukan pemeriksaan sendiri |
| "Alat otomatis dapat menemukan semua kebocoran" | Tidak. Kebocoran dalam **makna kolom** hanya dikenali dengan pengetahuan domain (lihat *AI Corner* Bab 4) |

**Tanda siap lanjut.** Mahasiswa dapat menjelaskan **mekanisme** (bukan hanya nama) minimal dua dari empat kebocoran.

---

#### Segmen 5 — Praktik: Mulai Lab 4 (40 menit)

**Tujuan.** Mahasiswa memburu kebocoran secara mandiri pada notebook baru.

**Yang dilakukan.** Mahasiswa mulai [Lab 4](../04-labs/lab-04-validasi-silang-deteksi-kebocoran.md). Dosen berkeliling dan memakai urutan bantuan **bertahap** berikut, agar mahasiswa tidak langsung menerima jawaban:

| Tingkat bantuan | Ucapan dosen |
|-----------------|--------------|
| 1 | "Baca ulang sel ini. Apa yang dilakukan baris kedua terhadap data uji?" |
| 2 | "Gunakan tiga pertanyaan pada §4.3.5 untuk data ini. Jawabanmu apa?" |
| 3 | "Fitur ini: apakah nilainya sudah ada pada saat prediksi dibutuhkan?" |
| 4 | Tunjuk sel yang bermasalah, tetapi minta mahasiswa menjelaskan sebabnya |

**Kebuntuan yang biasa muncul.**

| Kebuntuan | Penyebab umum | Bantuan |
|-----------|---------------|---------|
| Tidak menemukan kebocoran kelompok | Tidak memeriksa kolom pengenal entitas | "Adakah kolom yang berulang nilainya? Berapa baris per nilai?" |
| Salah menafsirkan skor turun | Menganggap perbaikan merusak model | Rujuk tabel demonstrasi |
| Validasi silang memberi hasil berbeda tiap dijalankan | `random_state` belum ditetapkan | Ingatkan kebijakan reproduksibilitas (RPS §K.2) |

**Catatan.** Pemakaian AI mengikuti kebijakan mata kuliah (RPS §K.1): AI boleh membantu menulis kode rutin, tetapi menemukan dan menafsirkan kebocoran adalah **tugas mahasiswa** dan wajib dicatat pada AI Usage Log.

---

#### Segmen 6 — Penutup (10 menit)

**Yang dilakukan.**

1. **Daftar periksa (5 menit).** Tampilkan Bab 4 §4.6. Mahasiswa memilih **dua butir** yang menurut mereka paling sering terlewat, lalu menjelaskan alasannya kepada teman sebelah.
2. **Tiket keluar (5 menit).** Mahasiswa menjawab tertulis tiga pertanyaan, lalu menyerahkannya sebelum keluar:

| No | Pertanyaan | Jawaban yang diharapkan |
|----|------------|--------------------------|
| 1 | Mengapa data uji hanya dipakai sekali? | Memilih berdasarkan skor uji berarti memilih berdasarkan kebetulan; skor uji tidak lagi jujur |
| 2 | Data penjualan harian tiga tahun: strategi apa dan mengapa? | Temporal, karena acak membuat model mengintip masa depan |
| 3 | Satu hal yang masih membingungkan hari ini | Jawaban bebas |

**Pemanfaatan tiket keluar.** Dosen membaca jawaban nomor 3 dan menyampaikan **dua pertanyaan terbanyak** pada awal pertemuan berikutnya.

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 4](../04-labs/lab-04-validasi-silang-deteksi-kebocoran.md).
- Menyelesaikan proposal proyek (jatuh tempo Minggu 5).
- Menjawab Latihan Soal tingkat Dasar (Bab 4) untuk persiapan Kuis 2.

---

## Bila Waktu Kurang

Urutan pemangkasan, dari yang paling aman:

1. Percepat Segmen 1 menjadi dua soal ingatan (hilangkan soal 2).
2. Perpendek Bagian C pada Segmen 3: bahas hanya **temporal** dan **berkelompok** di kelas, sisanya sebagai bacaan.
3. Pada Segmen 4, demonstrasikan **tiga** kebocoran dan jadikan satu sebagai tugas Lab.

**Yang tidak dipangkas:** Bagian A dan Bagian B pada Segmen 3. Dua bagian itu membentuk pemahaman inti bahwa skor yang tinggi dapat menyesatkan.

---

## Penugasan

**T-04 — Validasi Silang dan Perburuan Kebocoran**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook perbaikan + laporan temuan 1 halaman |
| Isi | (a) Menemukan seluruh kebocoran pada notebook yang diberikan; (b) Menjelaskan **mekanisme** tiap kebocoran; (c) Memperbaikinya; (d) Melaporkan skor sebelum dan sesudah; (e) Menerapkan validasi silang yang benar dengan pelaporan rerata ± simpangan |
| Tenggat | Awal pertemuan Minggu 5 |
| Bobot | 2,0% (Observasi, Sub-CPMK102-1) |

---

## Rangkuman

1. **Kebocoran data memberi hadiah ketika dilakukan**; itulah yang membuatnya berbahaya.
2. Data uji **dipakai satu kali, di paling akhir**. Memilih berdasarkan skor uji berarti memilih berdasarkan kebetulan.
3. Strategi pembagian mengikuti **sifat data**: temporal untuk deret waktu, berkelompok untuk entitas berulang, stratifikasi untuk kelas tak seimbang, acak bila tidak ada keadaan khusus.
4. Pembagian acak pada data deret waktu **selalu** menghasilkan kebocoran.
5. Yang divalidasi-silang adalah **`Pipeline`**, bukan model saja.
6. Laporkan **rerata dan simpangan** antarlipatan, serta jenis simpangan bakunya.
7. **Enam jenis kebocoran:** prapemrosesan, temporal, duplikat, kelompok, target, dan pemilihan berulang.
8. Skor yang terlalu bagus adalah **tanda bahaya**, bukan tanda keberhasilan.
9. Daftar periksa kebocoran (Bab 4 §4.6) dijalankan sebelum setiap pengumpulan.

---

## Referensi

1. Kapoor, S., & Narayanan, A. (2023). Leakage and the Reproducibility Crisis in ML-based Science. *Patterns*, 4(9), 100804.
2. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 2. O'Reilly.
3. Müller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*, Bab 5. O'Reilly.
4. Kaufman, S., Rosset, S., & Perlich, C. (2012). Leakage in Data Mining. *ACM TKDD*, 6(4), 1–21.
5. Dokumentasi scikit-learn — *Cross-validation*. <https://scikit-learn.org/stable/modules/cross_validation.html>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
