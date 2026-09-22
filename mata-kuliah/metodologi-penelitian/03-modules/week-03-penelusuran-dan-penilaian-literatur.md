# Minggu 3: Penelusuran dan Penilaian Literatur

---

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata kuliah | Metodologi Penelitian (`IF52510021`) |
| Minggu | 3 dari 16 |
| Topik | Penelusuran sistematis dan penilaian mutu sumber |
| Sub-CPMK | `METPEN-Sub-CPMK071-1` |
| ICM | ICM-03 — Menelusuri literatur secara sistematis dan menilai mutu sumber |
| Durasi | 2 × 50 menit |
| Metode | Kuliah + praktik penelusuran + **Kuis 1** |
| Bacaan | [Bab 3 — Penelusuran dan Penilaian Literatur](../06-buku-ajar/bab-03-penelusuran-dan-penilaian-literatur.md) |

---

## Tujuan Pembelajaran

1. **Menyusun** (C3) protokol penelusuran yang dapat diulang.
2. **Menerapkan** (C3) rumus pencarian pada beberapa basis data.
3. **Menilai** (C5) mutu sebuah sumber dengan kriteria yang jelas.
4. **Memverifikasi** (C3) keberadaan sebuah sitasi melalui DOI.

---

## Materi Pembelajaran

### 3.1 Penelusuran yang Dapat Diulang

Perbedaan antara mencari dan menelusuri secara sistematis:

| | Mencari | Menelusuri sistematis |
|---|---------|----------------------|
| Kata kunci | Terpikir saat itu | Disusun lebih dahulu dengan sinonim |
| Basis data | Yang teringat | Ditetapkan dan dicatat |
| Kriteria memilih | Terasa relevan | Inklusi/eksklusi tertulis |
| Dapat diulang orang lain | Tidak | **Ya, dengan hasil sebanding** |
| Dapat dilaporkan | Tidak | Ya, dengan diagram alir |

### 3.2 Menyusun Rumus Pencarian

```
Langkah 1 — Uraikan pertanyaan menjadi konsep

  "Faktor apa yang menyebabkan penghentian pemakaian
   aplikasi layanan publik daerah?"

  Konsep A: penghentian pemakaian
  Konsep B: aplikasi layanan publik
  Konsep C: (konteks) pemerintah daerah

Langkah 2 — Kumpulkan sinonim per konsep

  A: discontinuance, abandonment, attrition, churn,
     "post-adoption", "continued use"
  B: "e-government", "public service app", "government app",
     "civic technology"
  C: "local government", municipal, regional, "developing country"

Langkah 3 — Gabungkan

  (discontinuance OR abandonment OR "continued use"
   OR "post-adoption")
  AND ("e-government" OR "public service app"
       OR "government application")
  AND ("local government" OR municipal OR "developing country")

Langkah 4 — Catat rumus persis per basis data
  (sintaksnya berbeda-beda; catat apa adanya)
```

Langkah 2 adalah yang paling menentukan hasil. Satu sinonim penting yang
terlewat dapat menyembunyikan seluruh cabang pustaka. Cara menemukannya:
baca 3–5 makalah yang sudah dimiliki, dan catat istilah yang mereka pakai.

### 3.3 Basis Data yang Dipakai

| Basis data | Cakupan | Akses |
|------------|---------|-------|
| **ACM Digital Library** | Ilmu komputer, HCI, RPL | Sebagian terbuka; langganan kampus |
| **IEEE Xplore** | Teknik, komputer | Langganan kampus |
| **ScienceDirect / Scopus** | Multidisiplin | Langganan kampus |
| **SpringerLink** | Multidisiplin | Sebagian terbuka |
| **Google Scholar** | Sangat luas | Terbuka; **mutu beragam** |
| **DOAJ** | Jurnal akses terbuka terkurasi | Terbuka |
| **arXiv** | Pracetak | Terbuka; **belum ditelaah sejawat** |
| **Garuda / SINTA** | Terbitan Indonesia | Terbuka |
| **Neliti** | Repositori Indonesia | Terbuka |

Dua baris terakhir penting bagi penelitian berkonteks Indonesia. Sebagian
kesenjangan populasi hanya dapat dibuktikan dengan menunjukkan apa yang sudah
dan belum ada dalam pustaka Indonesia.

> **arXiv dan pracetak lain** boleh dipakai, tetapi statusnya harus
> dinyatakan. Naskah yang belum ditelaah sejawat tidak memiliki jaminan mutu
> yang sama, dan memperlakukannya setara dengan artikel jurnal adalah
> kekeliruan yang sering terjadi.

### 3.4 Menilai Mutu Sumber

| Kriteria | Pertanyaan | Tanda bahaya |
|----------|------------|--------------|
| **Telaah sejawat** | Apakah melalui *peer review*? | Terbit sangat cepat setelah pengiriman |
| **Reputasi tempat terbit** | Jurnal/konferensi dikenal di bidangnya? | Nama meniru terbitan terkenal |
| **Kejelasan metode** | Dapatkah metodenya diperiksa? | Metode tidak diuraikan |
| **Data dan ukuran sampel** | Disebutkan dan memadai? | Simpulan besar dari sampel kecil |
| **Keterbatasan diakui** | Ada bagian keterbatasan? | Tidak ada satu pun keterbatasan |
| **Kemutakhiran** | Sesuai dengan laju bidangnya? | Bidang cepat berubah, sumber 15 tahun |
| **Sitasi** | Dirujuk orang lain? | Nol sitasi setelah bertahun-tahun |

### 3.5 Penerbit Predator

| Ciri | Penjelasan |
|------|------------|
| Ajakan lewat surel yang memuji berlebihan | Terbitan bermutu tidak memburu naskah begitu |
| Menjanjikan terbit dalam hitungan hari | Telaah sejawat menuntut waktu |
| Biaya dinyatakan setelah naskah diterima | Ketidakjelasan yang disengaja |
| Dewan editor tidak dapat diverifikasi | Nama dicantumkan tanpa izin |
| Cakupan sangat luas | "Jurnal sains, teknologi, seni, dan humaniora" |

Cara memeriksa: telusuri nama jurnal pada DOAJ, periksa apakah terindeks pada
basis data yang dikenal, dan buka beberapa artikel terbitannya.

### 3.6 Verifikasi Sitasi — Ketentuan Mutlak

Setiap sitasi dalam seluruh keluaran mata kuliah ini wajib diverifikasi.

| Langkah | Tindakan |
|---------|----------|
| 1 | Salin DOI atau judul persis |
| 2 | Buka `https://doi.org/<DOI>` atau cari judulnya di basis data |
| 3 | Pastikan penulis, tahun, dan tempat terbit sama persis |
| 4 | **Buka naskahnya dan baca setidaknya abstrak dan simpulannya** |
| 5 | Bila tidak ditemukan: **buang sitasi itu** |

Langkah 4 sering dilewati. Sitasi yang ada tetapi tidak dibaca menghasilkan
kekeliruan yang berbeda dan sama seriusnya: makalah yang dirujuk ternyata
menyatakan hal yang berbeda dari yang diklaim.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

| # | Kegiatan |
|---|----------|
| 1 | Membaca [Bab 3](../06-buku-ajar/bab-03-penelusuran-dan-penilaian-literatur.md) |
| 2 | Memastikan akses basis data kampus berfungsi |
| 3 | Menyiapkan 5 sumber dari T2 dalam pengelola pustaka |

### Di Kelas (100 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–10 | **Kuis 1** — jenis kesenjangan dan verifikasi sitasi |
| 10–30 | Kuliah: menyusun rumus pencarian; basis data; PRISMA |
| 30–45 | Kuliah: menilai mutu sumber; penerbit predator |
| 45–55 | **Rehat** |
| 55–90 | **Lokakarya 3** — [Penelusuran Literatur Sistematis](../04-labs/lab-03-penelusuran-literatur-sistematis.md) |
| 90–100 | Latihan verifikasi: memeriksa 5 sitasi yang diberikan dosen — sebagian tidak ada |

> Kegiatan 90–100 adalah latihan yang mengubah sikap. Dari lima sitasi yang
> diberikan, sebagian sengaja dibuat tidak ada. Mahasiswa yang menemukannya
> sendiri memahami mengapa ketentuan verifikasi diberlakukan.

### Setelah Kelas

| # | Kegiatan |
|---|----------|
| 1 | Menyelesaikan **T3 — Protokol penelusuran** (5%), ≥40 kandidat |
| 2 | Membaca [Bab 4](../06-buku-ajar/bab-04-sintesis-literatur-dan-state-of-the-art.md) |

---

## Penugasan

### T3 — Protokol Penelusuran Literatur (5%, Observasi)

| Aspek | Ketentuan |
|-------|-----------|
| Keluaran | Protokol + catatan hasil + diagram alir PRISMA |
| Isi | Kata kunci & sinonim · basis data · rumus per basis data · kriteria inklusi/eksklusi · jumlah per tahap · ≥40 kandidat |
| Tenggat | Akhir Minggu 3 |

---

## AI Corner — Minggu 3

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI mengusulkan sinonim untuk konsep pencarian | **Meminta AI memberikan daftar referensi** |
| Meminta AI menjelaskan sintaks pencarian sebuah basis data | Menyalin sitasi dari jawaban AI tanpa verifikasi |
| Memakai perkakas penelusuran yang menampilkan sumber aslinya | Memakai ringkasan AI sebagai pengganti membaca |
| Meminta AI menjelaskan istilah dalam abstrak | Meminta AI menilai mutu jurnal |

### Sitasi yang Dikarang

Ini adalah ancaman integritas akademik paling serius dalam penulisan ilmiah
saat ini, dan mata kuliah ini menanganinya secara langsung.

| Gejala | Contoh |
|--------|--------|
| Penulis nyata, judul tidak ada | Nama peneliti terkenal + judul yang masuk akal tetapi tak pernah ditulis |
| DOI yang formatnya benar tetapi tidak menunjuk apa pun | `10.1016/j.xxxx.2021.xx.xxx` |
| Jurnal nyata, nomor terbitan tidak ada | Volume dan halaman yang tidak sesuai |
| Campuran: penulis dari satu makalah, judul dari makalah lain | Paling sulit dikenali |

Bentuk terakhir adalah yang paling berbahaya karena setiap unsurnya nyata.
Satu-satunya penangkalnya adalah **membuka DOI dan memastikan seluruh unsur
sitasi cocok**.

### Perkakas yang Menampilkan Sumber

Sebagian perkakas penelusuran berbantuan AI menampilkan tautan ke sumber
aslinya, bukan menghasilkan sitasi dari ingatan model. Perkakas semacam itu
boleh dipakai — dengan syarat yang tidak berubah: **setiap sumber tetap
dibuka, diverifikasi, dan dibaca**.

---

## Referensi

1. Kitchenham, B., & Charters, S. (2007). *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. EBSE Technical Report EBSE-2007-01.
2. Page, M. J., et al. (2021). The PRISMA 2020 Statement. *BMJ*, 372, n71.
3. Grames, E. M., et al. (2019). An Automated Approach to Identifying Search Terms for Systematic Reviews. *Methods in Ecology and Evolution*, 10(10), 1645–1654.
4. Grudniewicz, A., et al. (2019). Predatory Journals: No Definition, No Defence. *Nature*, 576(7786), 210–212.
5. Wohlin, C. (2014). Guidelines for Snowballing in Systematic Literature Studies. *Proceedings of EASE '14*.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Bab buku ajar | [Bab 3](../06-buku-ajar/bab-03-penelusuran-dan-penilaian-literatur.md) |
| Lokakarya | [Lokakarya 3](../04-labs/lab-03-penelusuran-literatur-sistematis.md) |
| Sumber pustaka | [Panduan Sumber Pustaka dan Data](../../metodologi-penelitian/datasets/README.md) |
| Minggu sebelumnya | [Minggu 2](week-02-masalah-penelitian-dan-kesenjangan.md) |
| Minggu berikutnya | [Minggu 4](week-04-sintesis-literatur-dan-state-of-the-art.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
