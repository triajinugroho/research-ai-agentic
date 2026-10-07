# BAB 9: MVP — MERANCANG YANG PALING SEDIKIT

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `TEKNO-Sub-CPMKUAI22-1` | Merancang (C6) produk minimum yang dapat diuji, menetapkan (C5) kriteria keberhasilan sebelum pengujian, dan menganalisis (C4) hasilnya | C4–C6 |

Setelah membaca bab ini, pembaca diharapkan mampu:

1. **Menjelaskan** (C2) arti "minimum" dan "viable" secara tepat.
2. **Membedakan** (C2) lima jenis MVP dan kapan masing-masing dipakai.
3. **Merancang** (C6) MVP yang menguji satu asumsi terbesar.
4. **Menetapkan** (C5) kriteria keberhasilan sebelum pengujian dimulai.
5. **Menganalisis** (C4) hasil pengujian termasuk hasil yang mengecewakan.

---

## 9.1 Dua Kata yang Sering Disalahpahami

### 9.1.1 "Minimum" Bukan "Setengah Jadi"

| Salah paham | Yang benar |
|-------------|------------|
| Versi kecil dari produk akhir | **Cara termurah menguji satu asumsi terbesar** |
| Produk dengan sedikit fitur | Bisa jadi bukan produk sama sekali |
| Prototipe yang belum rapi | Pengalaman utuh dalam ruang lingkup yang sempit |
| Yang bisa dibuat dalam waktu tersisa | Yang menjawab pertanyaan yang belum terjawab |

Ujian yang membedakan: **pertanyaan apa yang akan terjawab setelah ini dijalankan?** Bila tidak ada jawaban yang jelas, yang sedang dibangun bukan MVP melainkan produk kecil.

### 9.1.2 "Viable" Berarti Layak Dipakai, Bukan Layak Dipamerkan

Sesuatu disebut *viable* bila seseorang dapat memakainya untuk menyelesaikan urusannya secara nyata, dari awal sampai akhir, meskipun ruang lingkupnya sangat sempit.

```
BUKAN viable:
  Aplikasi dengan 8 layar, tetapi tak satu pun dapat
  dipakai menyelesaikan satu urusan sampai selesai.

VIABLE:
  Satu pesan WhatsApp berisi angka perkiraan belanja,
  dikirim setiap subuh, dihitung manual oleh tim.
  Pedagang benar-benar memakainya untuk berbelanja.
```

Contoh kedua tidak memiliki antarmuka, basis data, atau kode apa pun. Ia tetap MVP yang sah — dan lebih baik daripada contoh pertama — karena ia menjawab pertanyaan terbesar: apakah pedagang benar-benar mengubah keputusan belanjanya bila diberi angka.

### 9.1.3 Kesalahan Tersering pada Proyek Mahasiswa

| Kesalahan | Gejala | Akibat |
|-----------|--------|--------|
| Membangun semua fitur *Must have* | 8 minggu membangun, 1 minggu menguji | Tidak ada waktu memperbaiki |
| Menguji pada teman sendiri | Semua bilang bagus | Tidak belajar apa-apa |
| Tidak menetapkan kriteria dulu | "Cukup berhasil" ditentukan setelah melihat hasil | Hasil apa pun dianggap berhasil |
| Mementingkan tampilan | Waktu habis untuk warna dan animasi | Asumsi terbesar tak pernah diuji |
| Menunggu sampai sempurna | Belum diuji sampai Minggu 14 | Tidak ada kesempatan memperbaiki |

Baris ketiga adalah yang paling merusak karena paling halus. Kriteria keberhasilan yang ditetapkan setelah melihat hasil selalu terpenuhi.

---

## 9.2 Lima Jenis MVP

### 9.2.1 Perbandingannya

| Jenis | Bentuk | Menguji | Waktu | Biaya |
|-------|--------|---------|-------|-------|
| **Halaman penjelasan** | Satu halaman web berisi tawaran + tombol daftar | Apakah tawarannya menarik | 1–2 hari | ~Rp0 |
| **Prototipe kertas** | Gambar layar di kertas | Apakah alurnya dipahami | 1 hari | ~Rp0 |
| **Layanan manual (*concierge*)** | Tim mengerjakan langsung untuk beberapa orang | Apakah hasilnya bernilai | 1–2 minggu | Waktu tim |
| **Otomatis palsu (*Wizard of Oz*)** | Tampak otomatis, dikerjakan manusia | Apakah dipakai berulang | 2 minggu | Waktu tim |
| **Satu fitur** | Produk nyata, satu fungsi saja | Apakah dipakai dan dibayar | 3–4 minggu | Waktu + biaya layanan |

### 9.2.2 Memilih Jenis Berdasarkan Asumsi

| Asumsi terbesar | Jenis MVP yang tepat |
|-----------------|---------------------|
| Orang tertarik pada tawarannya | Halaman penjelasan |
| Orang memahami cara memakainya | Prototipe kertas |
| Hasilnya benar-benar bernilai | **Layanan manual** |
| Orang memakainya berulang kali | Otomatis palsu |
| Orang mau membayar | Satu fitur + pembayaran nyata |

Pemilihan dimulai dari asumsi, bukan dari kemampuan tim. Tim yang memilih "satu fitur" karena anggotanya senang membuat aplikasi sedang membangun untuk dirinya sendiri.

### 9.2.3 Layanan Manual pada Kasus Berjalan

```
Minggu 10-11 — MVP layanan manual

Peserta   : 5 warung (dari narasumber yang sudah dikenal)
Durasi    : 14 hari
Yang tim kerjakan setiap hari:
  20.00  Telepon/WhatsApp warung, tanyakan yang habis hari ini
  21.00  Hitung perkiraan kebutuhan besok (spreadsheet)
  04.00  Kirim pesan berisi daftar dan jumlah perkiraan

Beban    : ±40 menit/hari untuk 5 warung
Tidak ada: aplikasi, basis data, akun, kode
```

| Yang dipelajari | Tidak akan diketahui dari membangun aplikasi |
|-----------------|---------------------------------------------|
| Pukul berapa pesan benar-benar dibaca | Data pemakaian aplikasi tidak menjelaskan alasan |
| Kata apa yang membuat pesan diabaikan | Tidak terlihat dalam log |
| Bahwa 2 dari 5 meneruskan pesan ke anaknya yang belanja | **Pengguna sebenarnya bukan yang diwawancarai** |
| Bahwa perkiraan meleset paling jauh pada hari Jumat | Pola yang hanya terlihat dengan menghitung manual |

Baris ketiga adalah jenis temuan yang mengubah seluruh arah produk. Bila yang berbelanja adalah anak pemiliknya, maka persona, bahasa pesan, dan bahkan proposisi nilai perlu ditinjau ulang. Temuan semacam itu muncul dari 14 hari kerja manual dan hampir mustahil diperoleh dengan cara lain.

---

## 9.3 Menetapkan Kriteria Keberhasilan

### 9.3.1 Ditetapkan Sebelum, Bukan Sesudah

| Waktu penetapan | Yang terjadi |
|-----------------|--------------|
| Sebelum pengujian | Hasil dapat dinilai jujur |
| Sesudah melihat hasil | **Hasil apa pun menjadi "berhasil"** |

Kriteria ditulis dan ditandatangani seluruh anggota tim sebelum peserta pertama dihubungi. Dalam mata kuliah ini, kriteria yang ditetapkan setelah pengujian tidak diterima.

### 9.3.2 Bentuk Kriteria yang Baik

```markdown
## Kriteria Keberhasilan MVP — ditetapkan 5 Oktober 2026

Asumsi yang diuji:
  Pemilik warung akan mengubah keputusan belanja
  bila diberi angka perkiraan setiap subuh.

Cara mengukur:
  Setiap hari ke-7 dan ke-14, tanyakan kepada peserta:
  "Kemarin, belanjanya mengikuti angka dari kami atau
   perkiraan sendiri?"

BERHASIL bila:
  ≥3 dari 5 peserta menyatakan mengikuti angka kami
  pada ≥8 dari 14 hari.

GAGAL bila:
  <2 dari 5 peserta, atau ≥2 peserta berhenti membalas
  sebelum hari ke-14.

Bila GAGAL, langkah berikutnya:
  Wawancara ketiga peserta yang tidak mengikuti,
  fokus pada apa yang membuat mereka tidak percaya
  pada angka itu.
```

| Unsur | Mengapa wajib |
|-------|---------------|
| Asumsi yang diuji | Agar jelas pertanyaan apa yang dijawab |
| Cara mengukur | Agar tidak diperdebatkan kemudian |
| Ambang berhasil | Angka, bukan kesan |
| Ambang gagal | **Agar kegagalan dapat dikenali** |
| Langkah bila gagal | Agar kegagalan tetap produktif |

Unsur keempat adalah yang paling sering hilang. Tanpa ambang gagal yang eksplisit, tim akan selalu menemukan sisi positif dari hasil apa pun.

### 9.3.3 Ukuran yang Menyesatkan

| Ukuran | Mengapa menyesatkan | Penggantinya |
|--------|---------------------|--------------|
| Jumlah pendaftar | Mendaftar itu gratis | Jumlah yang memakai pada hari ke-7 |
| Jumlah unduhan | Mengunduh bukan memakai | Jumlah yang menyelesaikan tugas utama |
| Jumlah penayangan | Bukan minat | Jumlah yang meninggalkan kontak |
| "Semua bilang suka" | Kesopanan | Jumlah yang membayar di muka |
| Waktu di dalam aplikasi | Bisa berarti kebingungan | Waktu sampai tugas selesai |

Baris terakhir perlu diperhatikan. Untuk produk yang tujuannya menghemat waktu pengguna, **waktu pemakaian yang lebih lama adalah gejala buruk**. Ukuran yang dipinjam dari produk hiburan sering tidak sesuai untuk produk kerja.

---

## 9.4 Menjalankan Pengujian

### 9.4.1 Memilih Peserta

| Sumber peserta | Kualitas bukti |
|----------------|----------------|
| Narasumber wawancara yang sudah dikenal | Baik — sudah terbukti mengalami persoalannya |
| Rujukan dari narasumber | Baik — segmen sesuai |
| Orang asing dari segmen yang sama | Terbaik — tidak ada kesungkanan |
| Teman dan keluarga | **Tidak dipakai** — bias kesopanan terlalu besar |
| Sesama mahasiswa | Tidak dipakai, kecuali memang segmennya |

Ketentuan mata kuliah ini: **MVP diuji pada minimal 5 orang di luar tim**, dan teman dekat serta keluarga tidak dihitung.

### 9.4.2 Yang Dicatat Setiap Hari

```markdown
## Catatan Harian MVP — Hari ke-6

| Peserta | Pesan terkirim | Dibaca | Dibalas | Mengikuti? |
|---------|----------------|--------|---------|------------|
| W-01 | 04.00 | 04.12 | Ya | Ya |
| W-02 | 04.00 | 05.40 | Tidak | Tidak ditanya |
| W-03 | 04.00 | 04.05 | Ya | Sebagian |
| W-04 | 04.00 | — | — | — |
| W-05 | 04.00 | 04.20 | Ya | Ya |

Kejadian:
- W-04 tidak membaca sejak hari ke-4. Dihubungi sore ini:
  ponsel rusak, sedang dipinjami anaknya.
- W-03 berkata angka cabainya "kebanyakan terus".
  Perlu diperiksa: apakah tim salah memperkirakan
  atau warung ini memang memakai lebih sedikit.

Waktu tim hari ini: 45 menit
```

Kolom "Dibaca" pada tabel itu menghasilkan temuan operasional yang penting: W-02 membaca pukul 05.40, setelah waktu belanja. Bagi peserta itu, layanan tidak berguna sama sekali betapapun akurat angkanya. Temuan semacam ini mengubah rancangan, bukan sekadar menjadi catatan.

### 9.4.3 Menghadapi Hasil yang Mengecewakan

| Hasil | Tafsiran yang salah | Tafsiran yang benar |
|-------|--------------------|--------------------|
| 1 dari 5 mengikuti | "Perlu lebih banyak fitur" | Periksa mengapa 4 lainnya tidak percaya |
| 2 peserta berhenti | "Mereka tidak serius" | Wawancarai; alasannya adalah temuan |
| Semua mengikuti tetapi tak mau bayar | "Nanti setelah lebih lengkap" | Nilainya belum cukup besar |
| Perkiraan sering meleset | "Perlu model yang lebih canggih" | Periksa dulu apakah datanya memadai |

Baris kedua perlu ditegaskan: **peserta yang berhenti adalah sumber informasi terbaik dalam seluruh pengujian**. Mereka mengalami produk dan memutuskan tidak melanjutkannya — dan alasan mereka biasanya adalah hal yang paling perlu diperbaiki. Mewawancarai mereka terasa tidak nyaman, dan justru karena itu jarang dilakukan.

---

## AI Corner — Bab 9

### Batas Pemakaian

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI menyusun kerangka kriteria keberhasilan | Meminta AI menetapkan ambang berhasil untuk tim |
| Meminta AI menandai ukuran yang menyesatkan | Meminta AI menafsirkan hasil pengujian |
| Memakai AI membuat kerangka halaman penjelasan | Memakai AI membuat kesaksian pengguna palsu |
| Meminta AI menyebutkan kemungkinan penyebab peserta berhenti | Meminta AI menyimpulkan mengapa peserta tim berhenti |

Baris ketiga kolom kanan adalah pelanggaran berat. Kesaksian pengguna yang dibuat AI, betapapun halaman itu hanya sebuah uji, adalah `tadlis` — dan bila dipakai mengumpulkan pendaftar, ia menipu orang yang nyata.

### MVP Adalah Tempat AI Paling Berguna dan Paling Berbahaya

| Paling berguna | Paling berbahaya |
|----------------|------------------|
| Membuat kerangka halaman web dalam 2 jam alih-alih 2 hari | Membuat produk yang tampak jadi padahal belum diuji |
| Merapikan bahasa pesan kepada peserta | Mengarang kesaksian pengguna |
| Membuat contoh data untuk uji coba internal | Memakai contoh data itu dalam demo tanpa menyatakannya |
| Mempercepat pembuatan alat bantu internal tim | Membuat tim melewati tahap layanan manual |

Baris terakhir adalah bahaya yang paling halus. Karena AI membuat pembangunan terasa murah, godaan untuk langsung membangun menjadi jauh lebih besar daripada sebelumnya — dan tahap layanan manual, yang menghasilkan temuan terpenting, menjadi yang pertama dilewati.

> Kemudahan membangun tidak mengubah pertanyaan yang perlu dijawab. Aplikasi yang dibuat dalam dua hari dengan bantuan AI tetap tidak menjawab apakah pedagang akan mengubah keputusan belanjanya — dan 14 hari kerja manual tetap menjawabnya.

### Bila Demo Memakai Data Contoh

Ketentuan yang berlaku pada Demo Day:

| Keadaan | Kewajiban |
|---------|-----------|
| Data dalam demo adalah contoh | **Nyatakan di layar**: "data contoh" |
| Sebagian alur dikerjakan manual | Nyatakan bagian mana |
| Angka hasil adalah simulasi | Nyatakan dasarnya |
| Pengguna dalam demo adalah anggota tim | Nyatakan |

Menyatakannya tidak melemahkan presentasi. Penguji yang berpengalaman mengenali demo yang dipoles, dan kejujuran yang dinyatakan lebih dahulu selalu lebih baik daripada ketahuan saat tanya jawab.

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan arti "minimum" dan "viable" dalam MVP, dan sebutkan ujian yang membedakan MVP dari produk kecil.
2. Sebutkan lima jenis MVP beserta asumsi yang paling tepat diuji masing-masing.
3. Mengapa kriteria keberhasilan harus ditetapkan sebelum pengujian?
4. Sebutkan lima unsur wajib dokumen kriteria keberhasilan.
5. Mengapa "jumlah pendaftar" adalah ukuran yang menyesatkan?

### Tingkat Menengah

6. Untuk tiga asumsi berikut, tentukan jenis MVP yang paling tepat dan jelaskan alasannya:
   - "Mahasiswa mau membayar Rp15.000 untuk ringkasan materi kuliah."
   - "Pemilik kos mau memakai sistem pencatatan pembayaran."
   - "Orang mau menerima pengingat minum obat lewat pesan suara."

7. Susun dokumen kriteria keberhasilan lengkap (format §9.3.2) untuk MVP proyek tim Anda. Pastikan ambang gagal dan langkah bila gagal terisi.

8. Rancang MVP jenis layanan manual untuk proyek Anda: siapa pesertanya, apa yang tim kerjakan setiap hari, berapa lama, dan berapa beban waktunya. Sebutkan tiga hal yang akan Anda pelajari yang tidak akan diketahui dari membangun aplikasi.

9. Sebuah tim melaporkan: *"MVP kami berhasil, 47 orang mendaftar dan semua bilang aplikasinya bagus."* Sebutkan empat masalah dalam laporan ini dan susun laporan pengganti yang memakai ukuran yang tepat.

### Tingkat Mahir

10. **Latihan lapangan.** Jalankan MVP selama minimal 10 hari dengan minimal 5 peserta di luar tim dan di luar lingkaran teman. Buat catatan harian sesuai format §9.4.2. Laporkan hasilnya terhadap kriteria yang Anda tetapkan sebelumnya — termasuk bila hasilnya gagal — dan uraikan langkah berikutnya sesuai yang sudah Anda tuliskan.

11. Wawancarai setiap peserta yang berhenti sebelum pengujian selesai. Untuk setiap orang, catat alasan yang disebutkan dan alasan yang Anda duga sebenarnya. Susun ketiga temuan terpenting menjadi perubahan rancangan yang konkret. Jelaskan mengapa wawancara semacam ini terasa tidak nyaman dan mengapa tetap harus dilakukan.

12. Tim Anda memiliki 89 jam-orang tersisa (§6.4.1). Susun dua rencana MVP yang berbeda: satu yang menghabiskan seluruh jam untuk membangun satu fitur, dan satu yang memakai 20 jam untuk layanan manual selama dua minggu lalu 60 jam untuk membangun berdasarkan temuannya. Bandingkan keduanya dari sisi: pertanyaan apa yang terjawab, risiko yang tersisa di Minggu 15, dan apa yang dapat ditunjukkan pada Demo Day. Pertahankan pilihan Anda.

---

## Rangkuman

| Gagasan pokok | Rumusan singkat |
|---------------|-----------------|
| Arti "minimum" | Cara termurah menguji asumsi terbesar, bukan versi kecil produk |
| Arti "viable" | Dapat dipakai menyelesaikan urusan nyata sampai selesai |
| Ujian MVP | Pertanyaan apa yang terjawab setelah ini dijalankan? |
| Lima jenis | Halaman, prototipe kertas, layanan manual, otomatis palsu, satu fitur |
| Memilih jenis | Dimulai dari asumsi, bukan dari kesenangan tim |
| Kriteria | Ditetapkan sebelum peserta pertama dihubungi, dengan ambang gagal |
| Peserta | Minimal 5 di luar tim; teman dan keluarga tidak dihitung |
| Peserta yang berhenti | Sumber informasi terbaik dalam seluruh pengujian |
| Bahaya AI di sini | Membuat membangun terasa murah sehingga layanan manual dilewati |
| Demo | Data contoh dan bagian manual wajib dinyatakan |

---

## Referensi

1. Ries, E. (2011). *The Lean Startup*. Crown Business.
2. Maurya, A. (2012). *Running Lean* (2nd ed.). O'Reilly Media.
3. Bland, D. J., & Osterwalder, A. (2019). *Testing Business Ideas*. Wiley.
4. Klein, L. (2013). *UX for Lean Startups*. O'Reilly Media.
5. Knapp, J., Zeratsky, J., & Kowitz, B. (2016). *Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days*. Simon & Schuster.
6. Krug, S. (2014). *Don't Make Me Think, Revisited* (3rd ed.). New Riders.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul mingguan | [Minggu 10 — MVP: Merancang yang Paling Sedikit](../03-modules/week-10-mvp-merancang-yang-paling-sedikit.md) |
| Studio | [Studio 10 — Rancang dan Uji MVP](../04-labs/lab-10-rancang-dan-uji-mvp.md) |
| Bab sebelumnya | [Bab 8 — Model Bisnis dan Proposisi Nilai](bab-08-model-bisnis-dan-proposisi-nilai.md) |
| Bab berikutnya | [Bab 10 — *Go-to-Market* dan Eksperimen Pertumbuhan](bab-10-go-to-market-dan-eksperimen.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
