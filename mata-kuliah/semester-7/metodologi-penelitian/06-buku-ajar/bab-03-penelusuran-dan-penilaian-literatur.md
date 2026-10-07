# BAB 3: PENELUSURAN DAN PENILAIAN LITERATUR

**Bahan rujukan penyelarasan kurikulum** — disusun Tri Aji Nugroho, S.T., M.T.
Pengampu mata kuliah menurut registri: **Andi Arniaty Arsyad, Ph.D.** (`AAA`).

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `METPEN-Sub-CPMK071-1` | Menerapkan (C3) penelusuran literatur yang sistematis dan menganalisis (C4) mutu sumber secara kritis | C3–C4 |

Setelah membaca bab ini, pembaca diharapkan mampu:

1. **Menyusun** (C3) protokol penelusuran yang dapat diulang.
2. **Menerapkan** (C3) rumus pencarian pada beberapa basis data.
3. **Menganalisis** (C4) mutu sumber dengan kriteria yang jelas.
4. **Memverifikasi** (C3) keberadaan sitasi melalui DOI.
5. **Mengenali** (C4) sitasi yang dikarang.

---

## 3.1 Mencari dan Menelusuri

### 3.1.1 Perbedaannya

| | Mencari | Menelusuri sistematis |
|---|---------|----------------------|
| Kata kunci | Terpikir saat itu | Disusun lebih dahulu dengan sinonim |
| Basis data | Yang teringat | Ditetapkan dan dicatat |
| Kriteria memilih | "Terasa relevan" | Inklusi/eksklusi tertulis |
| Dapat diulang orang lain | Tidak | **Ya, dengan hasil sebanding** |
| Dapat dilaporkan | Tidak | Ya, dengan diagram alir dan angka |
| Dapat dibantah | Tidak | Ya |

Baris terakhir menjelaskan mengapa pembedaan ini penting. Klaim kesenjangan
yang bertumpu pada pencarian yang tidak tercatat tidak dapat diperiksa siapa
pun — termasuk oleh peneliti itu sendiri enam bulan kemudian.

### 3.1.2 Bukan Tinjauan Sistematis Penuh

Tinjauan sistematis (*systematic literature review*) adalah bentuk penelitian
tersendiri dengan tuntutan yang berat: dua penelaah independen, protokol yang
didaftarkan lebih dahulu, penilaian mutu terstruktur.

Yang dituntut pada mata kuliah ini adalah **penelusuran yang tercatat dan
dapat diulang** — sebagian prinsipnya, tanpa seluruh tuntutannya.

| Tinjauan sistematis penuh | Yang dituntut di sini |
|---------------------------|----------------------|
| Protokol didaftarkan lebih dahulu | Protokol ditulis dan diberi tanggal |
| Dua penelaah independen | Satu penelaah, dengan tinjauan sebaya |
| Penilaian mutu terstruktur | Kriteria mutu diterapkan dan dicatat |
| Ekstraksi data baku | Matriks sintesis (Bab 4) |
| ≥100 sumber lazim | ≥20 sumber dibaca penuh |

---

## 3.2 Menyusun Rumus Pencarian

### 3.2.1 Empat Langkah

```
Langkah 1 — Uraikan pertanyaan menjadi konsep

  "Faktor apa yang menyebabkan penghentian pemakaian
   aplikasi layanan publik daerah?"

  Konsep A: penghentian pemakaian
  Konsep B: aplikasi layanan publik
  Konsep C: pemerintah daerah / negara berkembang

Langkah 2 — Kumpulkan sinonim per konsep

  A: discontinuance, abandonment, attrition, churn,
     "post-adoption", "continued use", "continuance intention"
  B: "e-government", "public service app", "government app",
     "civic technology", "digital public service"
  C: "local government", municipal, regional,
     "developing country", Indonesia

Langkah 3 — Gabungkan dengan operator

  (discontinuance OR abandonment OR "continued use"
   OR "post-adoption")
  AND ("e-government" OR "public service app"
       OR "government application")
  AND ("local government" OR municipal OR "developing country")

Langkah 4 — Catat rumus persis per basis data
  Sintaks berbeda-beda; catat apa adanya, beserta tanggal
```

### 3.2.2 Langkah 2 Menentukan Hasil

Satu sinonim penting yang terlewat dapat menyembunyikan seluruh cabang
pustaka.

| Cara menemukan sinonim | Penjelasan |
|------------------------|------------|
| Baca kata kunci pada 3–5 makalah yang sudah dimiliki | Sumber terbaik; penulis bidang itu memakai istilah bidang itu |
| Perhatikan istilah dalam judul dan abstraknya | Sering berbeda dari dugaan awal |
| Periksa istilah Indonesia dan Inggris | Untuk basis data Garuda dan SINTA |
| Perhatikan variasi ejaan dan bentuk | *behavior/behaviour*, *organisation/organization* |
| Periksa istilah yang sudah usang | Bidang berubah; istilah lama mungkin dipakai pada makalah lebih tua |

> Contoh nyata: penelitian tentang "penghentian pemakaian" dalam pustaka
> sistem informasi sering memakai istilah *discontinuance* atau *IS
> continuance*, hampir tidak pernah *stop using*. Tim yang mencari dengan
> istilah sehari-hari akan menemukan sangat sedikit dan menyimpulkan bahwa
> kesenjangan itu besar — padahal yang besar adalah kekeliruan pencariannya.

### 3.2.3 Diagram Alir

Bentuk sederhana dari PRISMA, wajib dilampirkan:

```
Identifikasi
  ACM DL          : 142
  IEEE Xplore     :  87
  Scopus          : 203
  Garuda/SINTA    :  31
  Google Scholar  : 118  (50 pertama diperiksa)
  ──────────────────────
  Total           : 511
  Duplikat dibuang: 147
        ↓
Penyaringan (judul & abstrak)
  Diperiksa       : 364
  Dibuang         : 298
  Alasan tersering: tidak membahas penghentian pemakaian
        ↓
Kelayakan (naskah penuh)
  Diperiksa       :  66
  Dibuang         :  24
  Alasan          : 11 tak dapat diakses; 13 konteks tidak sesuai
        ↓
Disertakan        :  42  (22 dibaca penuh untuk sintesis)
```

Angka pada setiap tahap bukan hiasan. Ia menunjukkan bahwa penelusuran
benar-benar dijalankan, dan memungkinkan pembaca menilai apakah
penyaringannya wajar.

---

## 3.3 Menilai Mutu Sumber

### 3.3.1 Tujuh Kriteria

| Kriteria | Pertanyaan | Tanda bahaya |
|----------|------------|--------------|
| **Telaah sejawat** | Melalui *peer review*? | Terbit beberapa hari setelah pengiriman |
| **Reputasi tempat terbit** | Jurnal/konferensi dikenal di bidangnya? | Nama meniru terbitan terkenal |
| **Kejelasan metode** | Dapatkah metodenya diperiksa? | Metode tidak diuraikan |
| **Data dan sampel** | Disebutkan dan memadai? | Simpulan besar dari sampel kecil |
| **Keterbatasan diakui** | Ada bagian keterbatasan? | Tidak ada satu pun keterbatasan |
| **Kemutakhiran** | Sesuai laju bidangnya? | Bidang cepat berubah, sumber 15 tahun |
| **Sitasi** | Dirujuk orang lain? | Nol sitasi setelah bertahun-tahun |

Kriteria kelima sering paling informatif. Makalah yang tidak mengakui satu
pun keterbatasan biasanya ditulis tanpa telaah yang memadai — atau melalui
telaah yang tidak menuntutnya.

### 3.3.2 Pracetak

| Jenis | Status | Cara memperlakukan |
|-------|--------|--------------------|
| Artikel jurnal terindeks | Telah ditelaah sejawat | Dapat dipakai sebagai dasar |
| Prosiding konferensi bereputasi | Telah ditelaah sejawat | Dapat dipakai |
| **Pracetak (arXiv, SSRN)** | **Belum ditelaah** | **Boleh dipakai; statusnya wajib dinyatakan** |
| Laporan teknis lembaga | Beragam | Nyatakan jenisnya |
| Skripsi/tesis | Telah diuji, tidak ditelaah sejawat | Boleh; nyatakan jenisnya |
| Tulisan blog, media | Tidak ditelaah | Hanya untuk fenomena, bukan untuk klaim ilmiah |

Baris ketiga penting bagi bidang komputasi, di mana pracetak sangat lazim dan
sering menjadi rujukan utama. Memakainya sah; **memperlakukannya setara
dengan artikel jurnal adalah kekeliruan**.

### 3.3.3 Penerbit Predator

| Ciri | Penjelasan |
|------|------------|
| Ajakan lewat surel yang memuji berlebihan | Terbitan bermutu tidak memburu naskah |
| Menjanjikan terbit dalam hitungan hari | Telaah sejawat menuntut waktu |
| Biaya dinyatakan setelah naskah diterima | Ketidakjelasan yang disengaja |
| Dewan editor tidak dapat diverifikasi | Nama sering dicantumkan tanpa izin |
| Cakupan sangat luas | "Sains, teknologi, seni, dan humaniora" |
| Nama meniru jurnal terkenal | Satu kata berbeda |

| Cara memeriksa | Langkah |
|----------------|---------|
| 1 | Cari nama jurnal pada DOAJ |
| 2 | Periksa indeksasi: Scopus, Web of Science, SINTA |
| 3 | Buka beberapa artikel terbitannya; nilai mutunya sendiri |
| 4 | Telusuri satu-dua nama dewan editor |

---

## 3.4 Verifikasi Sitasi

### 3.4.1 Ketentuan Mutlak

Setiap sitasi dalam seluruh keluaran mata kuliah ini wajib diverifikasi.

| Langkah | Tindakan |
|---------|----------|
| 1 | Salin DOI atau judul persis |
| 2 | Buka `https://doi.org/<DOI>` atau cari judulnya di basis data |
| 3 | Pastikan **penulis, tahun, judul, dan tempat terbit sama persis** |
| 4 | **Buka naskahnya dan baca minimal abstrak dan simpulannya** |
| 5 | Bila tidak ditemukan: **buang sitasi itu** |

### 3.4.2 Mengapa Langkah 4 Tidak Boleh Dilewati

Sitasi yang ada tetapi tidak dibaca menimbulkan kekeliruan yang berbeda dan
sama seriusnya.

| Kekeliruan | Contoh |
|------------|--------|
| Makalah menyatakan hal yang berbeda | Disitasi sebagai pendukung, padahal membantah |
| Temuan berlaku pada konteks lain | Disitasi tanpa menyebut bahwa konteksnya berbeda |
| Yang disitasi adalah kutipan dari makalah lain | Rantai sitasi yang tidak diperiksa |
| Nada keraguan penulis hilang | "Mengindikasikan kemungkinan" menjadi "membuktikan" |

Baris terakhir adalah kekeliruan yang paling halus dan paling sering. Penulis
yang berhati-hati menulis *"hasil ini mengindikasikan kemungkinan hubungan
yang memerlukan penelitian lanjutan"*; yang menyitasinya tanpa membaca
menulis *"penelitian [sitasi] menemukan bahwa A memengaruhi B"*.

---

## 3.5 Sitasi yang Dikarang

### 3.5.1 Ancaman Integritas Paling Serius Saat Ini

Model bahasa menghasilkan sitasi yang tidak ada, dengan bentuk yang tidak
dapat dibedakan dari sitasi nyata.

| Bentuk | Penjelasan | Kesulitan mengenali |
|--------|------------|---------------------|
| Penulis nyata, judul tidak ada | Nama peneliti terkenal + judul yang masuk akal | Sedang |
| DOI yang formatnya benar tetapi tidak menunjuk apa pun | `10.1016/j.xxxx.2021.xx.xxx` | Mudah — buka saja |
| Jurnal nyata, volume/halaman tidak ada | Sesuai bidangnya | Sedang |
| **Campuran: penulis dari satu makalah, judul dari makalah lain** | Setiap unsurnya nyata | **Sangat sulit** |

Bentuk terakhir adalah yang paling berbahaya. Mencari nama penulisnya
menemukan orang yang nyata; mencari judulnya menemukan makalah yang nyata;
hanya memeriksa keduanya bersama-sama mengungkap bahwa gabungannya tidak ada.

### 3.5.2 Tidak Ada Ciri dari Bentuknya

Latihan yang dilakukan pada kelas Minggu 3: dosen membagikan lima sitasi,
sebagian di antaranya tidak ada. Mahasiswa diminta menemukan mana.

Pelajaran dari latihan itu hampir selalu sama: **tidak ada ciri yang dapat
dikenali dari bentuk sitasinya**. Sitasi yang dikarang tampak sama rapinya,
sama masuk akalnya, dan sama sesuainya dengan topik.

Satu-satunya cara memastikan adalah membukanya.

### 3.5.3 Akibat dalam Penilaian

| Tindakan | Akibat |
|----------|--------|
| Mencantumkan sitasi tanpa membukanya | Keluaran tidak dinilai |
| Sitasi yang tidak dapat diverifikasi ditemukan | Diperlakukan sama dengan pemalsuan data |
| Berulang | Diproses sesuai ketentuan fakultas |

Perlakuan yang setara dengan pemalsuan data bukan kekerasan yang
berlebih-lebihan. Sitasi adalah pernyataan bahwa sebuah karya ada dan
menyatakan sesuatu; sitasi yang dikarang adalah pernyataan palsu yang dapat
menyesatkan peneliti berikutnya yang membangun di atasnya.

---

## AI Corner — Bab 3

### Bab dengan Batas Terketat

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI mengusulkan sinonim untuk konsep pencarian | **Meminta AI memberikan daftar referensi** |
| Meminta AI menjelaskan sintaks pencarian sebuah basis data | Menyalin sitasi dari jawaban AI tanpa verifikasi |
| Memakai perkakas penelusuran yang menampilkan tautan sumber aslinya | Memakai ringkasan AI sebagai pengganti membaca |
| Meminta AI menjelaskan istilah dalam abstrak yang Anda baca | Meminta AI menilai mutu sebuah jurnal |

### Perkakas yang Menampilkan Sumber

Sebagian perkakas penelusuran berbantuan AI menampilkan tautan ke sumber
aslinya, bukan menghasilkan sitasi dari "ingatan" model. Perkakas semacam itu
**boleh dipakai** — dan dapat sangat menghemat waktu pada tahap identifikasi.

Syaratnya tidak berubah:

| Syarat | Penjelasan |
|--------|------------|
| Setiap sumber dibuka | Tautan diikuti sampai naskah aslinya |
| Setiap unsur sitasi diperiksa | Penulis, tahun, judul, tempat terbit |
| Setiap sumber dibaca | Minimal abstrak, metode, simpulan |
| Pemakaian dicatat dalam Deklarasi AI | Termasuk berapa yang dibuang |

Butir terakhir menghasilkan ciri deklarasi yang paling meyakinkan:
melaporkan berapa kandidat yang ternyata tidak ada.

### Pemakaian yang Dianjurkan

```
Saya meneliti penghentian pemakaian aplikasi layanan publik
di pemerintah daerah.

JANGAN memberikan daftar referensi atau nama penelitian.

Sebutkan saja:
1. Istilah teknis apa yang biasa dipakai dalam pustaka untuk
   konsep "penghentian pemakaian sistem informasi"
2. Istilah apa yang biasa dipakai untuk "aplikasi layanan
   publik pemerintah"
3. Basis data mana yang paling mungkin memuat pustaka ini
4. Bagaimana sintaks pencarian frasa pada masing-masing
```

Perintah **JANGAN** ditulis dengan huruf besar karena perlu ditegaskan.
Tanpa itu, model hampir selalu menyelipkan "beberapa penelitian yang relevan
antara lain…" — dan daftar itu cenderung bertahan dalam catatan mahasiswa
sampai berminggu-minggu kemudian.

### Latihan Wajib

```markdown
| # | Sitasi yang diberikan | DOI dibuka? | Penulis cocok? | Judul cocok? | Ada? |
|---|----------------------|-------------|----------------|--------------|------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

Berapa yang tidak ada: ___
Ciri apa yang membedakannya dari yang nyata: ___
```

Baris terakhir biasanya sulit dijawab — dan itulah pelajarannya.

---

## Latihan Soal

### Tingkat Dasar

1. Sebutkan enam pembeda antara mencari dan menelusuri secara sistematis.
2. Sebutkan empat langkah menyusun rumus pencarian.
3. Sebutkan tujuh kriteria menilai mutu sumber.
4. Apa status pracetak, dan bagaimana memperlakukannya?
5. Sebutkan lima langkah verifikasi sitasi.

### Tingkat Menengah

6. Untuk pertanyaan penelitian berikut, uraikan menjadi konsep, kumpulkan minimal tiga sinonim per konsep, dan susun rumus pencariannya:
   *"Kendala apa yang menghambat guru sekolah dasar memakai perangkat lunak pembelajaran adaptif?"*

7. Sebuah tim menemukan hanya 6 hasil dari pencariannya dan menyimpulkan bahwa kesenjangannya sangat besar. Sebutkan empat kemungkinan penyebab hasil yang sedikit itu, dan cara memeriksa masing-masing.

8. Nilailah empat sumber berikut dengan tujuh kriteria §3.3.1. Untuk masing-masing, tentukan apakah dapat dipakai sebagai dasar klaim, dan dengan catatan apa:
   - Artikel di jurnal terindeks Scopus Q1, 2019, sampel 340
   - Pracetak arXiv, 2026, tanpa bagian keterbatasan
   - Prosiding konferensi nasional, 2024, sampel 12, metode tidak diuraikan
   - Artikel jurnal yang terbit 9 hari setelah pengiriman

9. Susun diagram alir penelusuran untuk topik Anda dengan angka nyata pada setiap tahap. Jelaskan alasan pembuangan tersering pada tahap penyaringan.

### Tingkat Mahir

10. **Latihan verifikasi.** Ambil daftar pustaka dari satu Tugas Akhir angkatan sebelumnya di program studi Anda. Pilih 10 sitasi secara acak dan verifikasi seluruhnya sesuai lima langkah §3.4.1. Laporkan: berapa yang dapat diverifikasi, berapa yang unsurnya tidak cocok, dan berapa yang tidak dapat ditemukan. Jelaskan apa yang Anda pelajari tentang ketelitian yang diperlukan.

11. **Penelusuran bola salju.** Ambil tiga makalah paling relevan bagi topik Anda. Telusuri mundur (daftar pustakanya) dan maju (yang menyitasinya). Laporkan berapa sumber penting yang ditemukan dengan cara ini yang **tidak** muncul pada pencarian kata kunci Anda, dan jelaskan mengapa mereka terlewat.

12. Minta seorang teman menjalankan protokol penelusuran Anda persis seperti tertulis, tanpa bertanya. Bandingkan jumlah hasil pada setiap tahap dengan hasil Anda. Bila berbeda jauh, identifikasi bagian protokol yang tidak jelas dan perbaiki. Laporkan kedua versi protokol dan selisih hasilnya.

---

## Rangkuman

| Gagasan pokok | Rumusan singkat |
|---------------|-----------------|
| Pembeda penelusuran sistematis | Dapat diulang orang lain dengan hasil sebanding |
| Langkah yang menentukan hasil | Pengumpulan sinonim; satu istilah terlewat menyembunyikan cabang pustaka |
| Diagram alir | Angka pada setiap tahap; bukan hiasan |
| Pracetak | Boleh dipakai; statusnya wajib dinyatakan |
| Kriteria mutu paling informatif | Ada-tidaknya bagian keterbatasan |
| Verifikasi | Lima langkah; langkah 4 (membaca) tidak boleh dilewati |
| Sitasi yang dikarang | Bentuk campuran paling berbahaya; tak ada ciri dari bentuknya |
| Satu-satunya penangkal | Membuka DOI dan memeriksa seluruh unsur |
| Akibat | Sitasi yang tak terverifikasi setara pemalsuan data |
| Perkakas AI | Boleh, bila menampilkan sumber dan setiap sumber tetap dibuka |

---

## Referensi

1. Kitchenham, B., & Charters, S. (2007). *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. EBSE Technical Report EBSE-2007-01.
2. Page, M. J., et al. (2021). The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews. *BMJ*, 372, n71.
3. Wohlin, C. (2014). Guidelines for Snowballing in Systematic Literature Studies. *Proceedings of EASE '14*.
4. Grames, E. M., Stillman, A. N., Tingley, M. W., & Elphick, C. S. (2019). An Automated Approach to Identifying Search Terms for Systematic Reviews. *Methods in Ecology and Evolution*, 10(10), 1645–1654.
5. Grudniewicz, A., et al. (2019). Predatory Journals: No Definition, No Defence. *Nature*, 576(7786), 210–212.
6. Petersen, K., Vakkalanka, S., & Kuzniarz, L. (2015). Guidelines for Conducting Systematic Mapping Studies in Software Engineering. *Information and Software Technology*, 64, 1–18.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul mingguan | [Minggu 3](../03-modules/week-03-penelusuran-dan-penilaian-literatur.md) |
| Lokakarya | [Lokakarya 3](../04-labs/lab-03-penelusuran-literatur-sistematis.md) |
| Sumber pustaka | [Panduan Sumber Pustaka dan Data](../datasets/README.md) |
| Bab sebelumnya | [Bab 2](bab-02-masalah-penelitian-dan-kesenjangan.md) |
| Bab berikutnya | [Bab 4 — Sintesis Literatur dan *State of the Art*](bab-04-sintesis-literatur-dan-state-of-the-art.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
