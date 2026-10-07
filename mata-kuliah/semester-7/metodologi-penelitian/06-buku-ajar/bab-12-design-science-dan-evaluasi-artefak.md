# BAB 12: *DESIGN SCIENCE* DAN EVALUASI ARTEFAK

**Bahan rujukan penyelarasan kurikulum** — disusun Tri Aji Nugroho, S.T., M.T.
Pengampu mata kuliah menurut registri: **Andi Arniaty Arsyad, Ph.D.** (`AAA`).

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `METPEN-Sub-CPMK091-1` | Menganalisis (C4) kendala *stakeholder* menjadi kriteria evaluasi artefak yang tertelusur dan dapat diukur | C4 |

Setelah membaca bab ini, pembaca diharapkan mampu:

1. **Menjelaskan** (C2) kapan pembangunan artefak menjadi penelitian.
2. **Membedakan** (C2) empat jenis artefak.
3. **Menetapkan** (C4) kriteria evaluasi yang tertelusur ke kebutuhan.
4. **Memilih** (C4) pembanding yang wajar.
5. **Menetapkan** (C5) ambang keberhasilan beserta alasannya.

---

## 12.1 Kapan Membangun Menjadi Penelitian

### 12.1.1 Lima Pembeda

| | Membangun saja | Penelitian perancangan |
|---|---------------|------------------------|
| Tujuan | Sistem berfungsi | Menjawab pertanyaan |
| Kriteria | Berjalan tanpa galat | Ditetapkan dari kebutuhan, **sebelum** membangun |
| Pembanding | Tidak ada | Keadaan sekarang atau pendekatan lain |
| Laporan | Cara membangunnya | Apa yang dipelajari |
| Kegagalan | Tidak dilaporkan | **Temuan** |

### 12.1.2 Pertanyaan yang Memisahkan

> *Setelah artefak ini selesai, apa yang kita ketahui yang tidak kita ketahui
> sebelumnya?*

Jawaban yang lemah menyebut keberadaan artefak. Jawaban yang kuat menyebut
**pengetahuan yang dapat dipakai orang lain** meskipun mereka tidak memakai
artefak itu.

| Lemah | Kuat |
|-------|------|
| "Sistem pencatatan untuk klinik tersedia" | "Diketahui bahwa kendala terbesar penerapan sistem pencatatan di klinik kecil bukan biaya, melainkan ketiadaan petugas yang dapat menjaga konsistensi data — yang terlihat dari gagalnya kriteria K-04 pada dua dari tiga klinik" |
| "Model klasifikasi mencapai akurasi 91%" | "Diketahui bahwa pendekatan X bertahan pada teks formal berbahasa Indonesia tetapi turun tajam (91% → 63%) pada teks dengan campur kode, yang menunjukkan bahwa asumsi tokenisasinya tidak berlaku" |

---

## 12.2 Empat Jenis Artefak

| Jenis | Contoh | Pengetahuan yang dihasilkan |
|-------|--------|----------------------------|
| **Konstruk** | Kosakata, taksonomi, skema pelabelan | Cara memandang persoalan |
| **Model** | Kerangka, representasi, arsitektur | Hubungan antarbagian persoalan |
| **Metode** | Algoritma, prosedur, teknik | Cara mengerjakan yang lebih baik |
| **Instansiasi** | Sistem, prototipe, alat | Bahwa sesuatu dapat diwujudkan, dan bagaimana perilakunya |

### 12.2.1 Kelemahan Khas Instansiasi

Mayoritas Tugas Akhir menghasilkan instansiasi — jenis yang paling sulit
menghasilkan pengetahuan yang dapat dipindahkan.

| Sebab | Penjelasan |
|-------|------------|
| Banyak hal khas pada sistem itu | Bahasa pemrograman, pustaka, perangkat keras |
| Keberhasilan sulit diatribusikan | Karena pendekatannya, atau karena implementasinya? |
| Konteks pengujian sempit | Satu organisasi, satu periode |

### 12.2.2 Menarik Keluar yang Dapat Dipindahkan

| Bukan | Melainkan |
|-------|-----------|
| "Sistem ini berhasil" | "Pendekatan X berhasil pada keadaan Y, dan gagal ketika Z" |
| "Akurasinya 94%" | "Akurasi turun tajam ketika Z, yang menunjukkan bahwa asumsi W tidak berlaku pada konteks ini" |
| "Pengguna puas" | "Kriteria yang paling menentukan penerimaan adalah V, bukan U yang selama ini diasumsikan" |
| "Metode diimplementasikan dengan sukses" | "Implementasi metode ini menuntut prasyarat P yang tidak disebutkan dalam pustaka aslinya" |

Baris terakhir menunjukkan jenis pengetahuan yang sering dihasilkan
instansiasi dan jarang dilaporkan: **apa yang diperlukan untuk membuat
sesuatu bekerja yang tidak tertulis dalam makalah aslinya**.

---

## 12.3 Kriteria Evaluasi yang Tertelusur

### 12.3.1 Rantai Ketertelusuran

```
Kutipan narasumber (Bab 6)
      ↓
Kendala berkode K-__
      ↓
Kriteria kebutuhan
      ↓
Kriteria evaluasi + ambang
      ↓
Cara mengukur
```

Rantai inilah yang diperiksa pada penilaian proposal, dengan bobot **30%**
dari komponen T14.

### 12.3.2 Tabel Kriteria

| Kriteria | **Tertelusur ke** | Cara mengukur | Ambang | Sumber ambang |
|----------|-------------------|---------------|--------|---------------|
| Waktu penyelesaian satu berkas | K-01 (N1, N3: "paling cuma 5 menit per berkas kalau lagi ramai") | Pencatatan waktu, 20 percobaan, 5 pengguna | ≤3 menit | Kendala: 5 menit tersedia; sisanya untuk verifikasi |
| Berjalan pada perangkat kantor | K-02 (pengamatan: 3 unit RAM 4 GB) | Uji pada 3 perangkat nyata | Tanpa galat; respons ≤2 detik | Keadaan sekarang |
| Tahan koneksi terputus | K-03 (N2; log sistem) | Uji pemutusan buatan, 10 kali | Pekerjaan tidak hilang bila terputus ≤10 menit | Kendala: rata-rata gangguan 6 menit |
| Dapat dipakai tanpa pelatihan | K-04 (N1: pergantian staf tinggi) | Uji pengguna, tugas baku, 5 pengguna baru | ≥4 dari 5 selesai tanpa dipandu | Kendala: tidak ada waktu pelatihan |
| Ketelitian ekstraksi | KB-01 (N1, N2, N3) | Bandingkan dengan pemeriksaan manual, 200 berkas | ≥95% | Pustaka [sitasi] pada tugas serupa |

### 12.3.3 Kolom yang Menentukan

| Kolom | Mengapa wajib |
|-------|---------------|
| **Tertelusur ke** | Membedakan kriteria penelitian dari daftar keinginan pengembang |
| Cara mengukur | Prosedur yang dapat diulang orang lain |
| Ambang | Angka, ditetapkan sebelum evaluasi |
| **Sumber ambang** | Menjawab "mengapa angka itu?" |

Kolom kedua dan keempat bersama-sama menjawab pertanyaan penguji yang paling
sering: *"mengapa 3 menit, bukan 5?"* dan *"bagaimana Anda mengukurnya?"*

---

## 12.4 Menetapkan Ambang

### 12.4.1 Empat Sumber yang Sah

| Sumber | Contoh | Kekuatan |
|--------|--------|----------|
| **Kendala lapangan** | 3 menit, karena staf punya 5 menit dan butuh sisa untuk verifikasi | Paling kuat |
| **Keadaan sekarang** | Lebih baik dari cara manual yang memakan 8 menit | Kuat |
| **Pustaka** | Ketelitian ≥95%, sesuai [sitasi] pada tugas serupa | Kuat |
| **Standar yang berlaku** | Sesuai pedoman aksesibilitas | Kuat |

### 12.4.2 Yang Tidak Sah

| Sumber | Contoh | Mengapa tidak sah |
|--------|--------|-------------------|
| Angka bulat yang terdengar baik | "Akurasi 90%" | Tidak berasal dari mana pun |
| Angka yang lazim dalam pustaka bidang lain | "F1 ≥ 0,8" | Konteks, tugas, dan akibat kesalahan berbeda |
| Angka yang dicapai artefak | Ditetapkan setelah melihat hasil | Selalu terpenuhi |
| Angka dari jawaban asisten AI | — | Tidak tertelusur |

Baris ketiga adalah ancaman terbesar dan paling sulit dikenali dari luar.
Cara mencegahnya: **tuliskan kriteria, beri tanggal, dan lampirkan** sebelum
evaluasi dimulai.

### 12.4.3 Mengukur Keadaan Sekarang

Ambang dari "keadaan sekarang" hanya kuat bila keadaan sekarang **benar-benar
diukur**, bukan diperkirakan.

| Diperkirakan | Diukur |
|--------------|--------|
| "Cara manual memakan sekitar 10 menit" | "Pengamatan pada 15 berkas: rata-rata 8,3 menit (SD 2,1)" |
| "Kesalahan sering terjadi" | "Pemeriksaan 200 berkas arsip: 11 kesalahan entri (5,5%)" |
| "Staf kesulitan mencari data lama" | "Pengukuran waktu pencarian 20 kasus: rata-rata 4,2 menit; 3 kasus tidak ditemukan" |

Pengukuran keadaan sekarang sering menjadi **kontribusi tersendiri** — banyak
organisasi tidak mengetahui angka ini tentang dirinya sendiri.

---

## 12.5 Pembanding

### 12.5.1 Pilihan

| Pembanding | Kapan sesuai | Bahaya |
|------------|--------------|--------|
| **Keadaan sekarang** | Hampir selalu; paling bermakna | Sulit diukur bila tidak tercatat |
| Pendekatan lain dari pustaka | Bila ada yang setara | Implementasi ulang mungkin tidak adil |
| Versi sederhana artefak sendiri | Menguji sumbangan tiap bagian | — |
| Batas bawah (*naive baseline*) | Menunjukkan persoalan tidak sepele | **Tidak cukup sendirian** |

### 12.5.2 Keadilan Pembanding

| Pertanyaan | Bila jawabannya buruk |
|------------|----------------------|
| Apakah pembanding disetel dengan usaha yang sebanding? | Perbandingan tidak adil |
| Apakah keduanya diuji pada data yang sama? | Perbandingan tidak sahih |
| Apakah pembanding dijalankan pada perangkat yang sama? | Perbedaan mungkin dari perangkat |
| Apakah orang yang menjalankan keduanya sama terampilnya? | Perbedaan mungkin dari keterampilan |

> Membandingkan hanya dengan batas bawah yang sengaja lemah adalah bentuk
> ketidakjujuran yang halus. Sebuah metode yang mengalahkan tebakan acak
> belum menunjukkan apa pun bila cara yang dipakai orang sekarang jauh lebih
> baik daripada tebakan acak.

### 12.5.3 Melaporkan Penyetelan

Bila pembanding adalah pendekatan lain yang perlu disetel, **usaha penyetelan
wajib dilaporkan**.

```markdown
Penyetelan pembanding:
  Metode B disetel dengan pencarian kisi pada 3 parameter,
  36 kombinasi, memakai data validasi yang sama.
  Metode yang diusulkan disetel dengan prosedur yang sama,
  jumlah kombinasi yang sama.
  Waktu penyetelan: masing-masing ±4 jam komputasi.
```

Tanpa laporan ini, pembaca tidak dapat menilai apakah perbandingannya adil.

---

## 12.6 Melaporkan Kegagalan

### 12.6.1 Yang Wajib Dilaporkan

| Butir | Contoh |
|-------|--------|
| Kriteria yang tidak tercapai | "Waktu penyelesaian 3,8 menit; ambang 3 menit tidak tercapai" |
| Keadaan di mana artefak gagal | "Gagal pada berkas dengan tulisan tangan; 12% dari sampel" |
| Kemungkinan sebabnya | Dengan bukti, bukan dugaan |
| Apa yang sudah dicoba | Iterasi yang tidak berhasil |
| Apa artinya bagi pengetahuan | "Menunjukkan bahwa pendekatan ini menuntut prasyarat P" |

### 12.6.2 Mengapa Kegagalan Menaikkan Nilai

| Penelitian dengan seluruh kriteria tercapai | Penelitian dengan sebagian kriteria gagal |
|---------------------------------------------|-------------------------------------------|
| Kriteria mungkin terlalu longgar | Kriteria cukup menantang |
| Kriteria mungkin ditetapkan setelah hasil | Kriteria jelas ditetapkan sebelumnya |
| Pembaca tidak tahu batas pendekatan itu | **Batas pendekatan terlihat** |
| Sulit dipercaya | Lebih dapat dipercaya |

Penguji berpengalaman justru curiga pada penelitian perancangan yang seluruh
kriterianya tercapai sempurna. Kecurigaan itu beralasan.

---

## 12.7 Untuk Penelitian Non-Artefak

Mahasiswa yang penelitiannya tidak membangun artefak menggantinya dengan
kriteria mutu penelitian:

| Aspek | Kriteria | Ambang | Cara memeriksa |
|-------|----------|--------|----------------|
| Kecukupan data | Saturasi tema | Tidak ada tema baru pada 3 wawancara terakhir | Tabel tema per wawancara |
| Kualitas analisis | Kesesuaian antarpenilai | Kappa ≥0,6 pada 20% data | Penandaan silang |
| Ketertelusuran | Setiap tema punya kutipan pendukung | ≥3 kutipan dari responden berbeda per tema | Rantai bukti |
| Kasus menyimpang | Dicari dan dianalisis | Minimal 1 dicari untuk tiap tema | Catatan analisis |
| Pemeriksaan anggota | Tafsiran ditunjukkan kepada responden | ≥3 responden | Catatan koreksi |

Penggantian ini disepakati dengan dosen pengampu.

---

## AI Corner — Bab 12

### Batas Pemakaian

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI menyebutkan aspek evaluasi yang lazim untuk jenis artefak tertentu | **Menetapkan ambang untuk artefak Anda** |
| Meminta AI memeriksa keterukuran kriteria | Mengisi kolom "tertelusur ke" |
| Meminta AI menanyakan "mengapa angka itu?" untuk tiap ambang | Menerima ambang tanpa menelusurinya ke kendala |
| Meminta AI menyebutkan pembanding yang mungkin terlewat | Menilai apakah artefak Anda "sudah baik" |

### Mengapa Ambang dari Model Tidak Dapat Dipakai

Ditanya berapa ambang akurasi yang wajar, model menjawab dengan angka yang
lazim dalam pustaka — 90%, 95%, F1 0,8. Angka itu nyata dan berasal dari
konteks penelitian lain: tugas berbeda, data berbeda, dan **akibat kesalahan
yang berbeda**.

| Konteks | Akibat kesalahan | Ambang yang wajar |
|---------|------------------|-------------------|
| Penyaringan surel iklan | Satu surel penting masuk folder sampah | Mungkin 90% memadai |
| Ekstraksi data berkas administrasi | Kesalahan menyebabkan kerja ulang seluruh berkas | Mungkin ≥95% perlu |
| Penyaringan awal untuk diperiksa manusia | Kesalahan dikoreksi pemeriksa | Mungkin 80% memadai |

Ambang yang sahih berakar pada keadaan penelitian Anda: seberapa besar
kerugian dari setiap kesalahan, dan berapa yang ditoleransi penggunanya.

### Pemakaian yang Dianjurkan — Penantang Ambang

```
Berikut kriteria evaluasi artefak saya, dengan ambang dan
penelusurannya ke kendala lapangan:
[tempelkan tabel lengkap dengan kolom "tertelusur ke"]

Tugas Anda:
1. Untuk setiap ambang, tanyakan "mengapa angka itu dan bukan
   angka lain?" — dan tandai baris yang penelusuran saya
   tidak menjawabnya.
2. Tandai kriteria yang cara mengukurnya belum dapat diulang
   orang lain.
3. Sebutkan aspek yang biasanya dievaluasi pada artefak
   sejenis dan tidak ada dalam daftar saya — hanya namanya.
4. Tandai kriteria yang tidak berhubungan dengan kendala
   mana pun.

Jangan mengusulkan angka. Jangan mengisi kolom penelusuran.
```

---

## Latihan Soal

### Tingkat Dasar

1. Sebutkan lima pembeda antara membangun saja dan penelitian perancangan.
2. Sebutkan empat jenis artefak dan pengetahuan yang dihasilkan masing-masing.
3. Mengapa instansiasi paling sulit menghasilkan pengetahuan yang dapat dipindahkan?
4. Sebutkan empat sumber ambang yang sah dan empat yang tidak sah.
5. Mengapa melaporkan kegagalan menaikkan nilai penelitian perancangan?

### Tingkat Menengah

6. Untuk tiga artefak berikut, rumuskan "pengetahuan yang dihasilkan" dalam bentuk yang dapat dipindahkan:
   - Sistem presensi berbasis pengenalan wajah untuk sekolah
   - Model klasifikasi keluhan pelanggan berbahasa Indonesia
   - Antarmuka pencarian katalog untuk perpustakaan

7. Susun tabel kriteria evaluasi lengkap untuk artefak Anda, dengan kolom "tertelusur ke" berisi kode kendala dari Bab 6.

8. Untuk setiap ambang dalam tabel Anda, tentukan sumbernya dari empat sumber sah. Tandai ambang yang belum memiliki sumber dan tentukan cara memperolehnya.

9. Tentukan pembanding untuk artefak Anda. Jalankan empat pertanyaan keadilan §12.5.2 dan laporkan hasilnya.

### Tingkat Mahir

10. **Mengukur keadaan sekarang.** Untuk satu kriteria dalam tabel Anda, ukur keadaan sekarang secara nyata — bukan diperkirakan. Laporkan metode pengukuran, jumlah pengamatan, dan hasilnya dengan sebarannya. Jelaskan apa yang berubah pada ambang Anda setelah pengukuran itu.

11. Tunjukkan tabel kriteria Anda kepada salah satu narasumber dari Bab 6. Tanyakan: "Kalau sistemnya memenuhi ini semua, apakah Bapak/Ibu akan memakainya?" Catat jawabannya verbatim. Bila jawabannya ragu atau tidak, gali kriteria apa yang kurang, dan tambahkan ke tabel dengan penelusurannya.

12. Susun rencana pelaporan kegagalan untuk artefak Anda: untuk setiap kriteria, tulis apa yang akan Anda laporkan bila ambangnya tidak tercapai, dan **pengetahuan apa yang tetap dihasilkan** dari kegagalan itu. Jelaskan mengapa menuliskannya sebelum evaluasi lebih sehat daripada menyusunnya setelah hasil terlihat.

---

## Rangkuman

| Gagasan pokok | Rumusan singkat |
|---------------|-----------------|
| Pembeda penelitian perancangan | Kriteria mendahului pembangunan; ada pembanding; kegagalan dilaporkan |
| Pertanyaan pemisah | Apa yang kita ketahui yang tidak diketahui sebelumnya |
| Kelemahan instansiasi | Paling sulit menghasilkan pengetahuan yang dapat dipindahkan |
| Menarik keluar pengetahuan | "Pendekatan X berhasil pada keadaan Y, gagal ketika Z" |
| Rantai ketertelusuran | Kutipan → kendala → kriteria → ambang → cara mengukur |
| Kolom "tertelusur ke" | Membedakan kriteria penelitian dari daftar keinginan |
| Ambang sah | Kendala lapangan, keadaan sekarang, pustaka, standar |
| Ancaman terbesar | Ambang ditetapkan setelah melihat hasil |
| Keadaan sekarang | Diukur, bukan diperkirakan; sering menjadi kontribusi tersendiri |
| Pembanding | Penyetelan wajib dilaporkan; batas bawah tidak cukup sendirian |
| Kegagalan | Menaikkan nilai; kriteria yang seluruhnya tercapai mengundang kecurigaan |

---

## Referensi

1. Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in Information Systems Research. *MIS Quarterly*, 28(1), 75–105.
2. Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A Design Science Research Methodology for Information Systems Research. *Journal of Management Information Systems*, 24(3), 45–77.
3. Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A Framework for Evaluation in Design Science Research. *European Journal of Information Systems*, 25(1), 77–89.
4. Gregor, S., & Hevner, A. R. (2013). Positioning and Presenting Design Science Research for Maximum Impact. *MIS Quarterly*, 37(2), 337–355.
5. Wieringa, R. J. (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer.
6. March, S. T., & Smith, G. F. (1995). Design and Natural Science Research on Information Technology. *Decision Support Systems*, 15(4), 251–266.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul mingguan | [Minggu 13](../03-modules/week-13-design-science-dan-evaluasi-artefak.md) |
| Lokakarya | [Lokakarya 13](../04-labs/lab-13-kriteria-evaluasi-artefak.md) |
| Sumber kendala | [Bab 6 — *Stakeholder*, Kebutuhan, dan Konteks](bab-06-stakeholder-kebutuhan-dan-konteks.md) |
| Bab sebelumnya | [Bab 11](bab-11-analisis-data-dan-penarikan-simpulan.md) |
| Bab berikutnya | [Bab 13 — Riset Berbantuan AI dan *Reproducibility*](bab-13-riset-berbantuan-ai-dan-reproducibility.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
