# BAB 3: PERSONA, *JOBS-TO-BE-DONE*, DAN KONTEKS PENGGUNAAN

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `TEKNO-Sub-CPMK091-1` | Menganalisis (C4) catatan wawancara menjadi persona dan pernyataan *job* yang setiap unsurnya tertelusur ke kutipan | C4 |
| `TEKNO-Sub-CPMKFSTS12-1` | Menyusun (C3) sintesis bersama dalam tim tanpa satu orang mendominasi penafsiran | C3, A3 |

Setelah membaca bab ini, pembaca diharapkan mampu:

1. **Membedakan** (C2) persona berbasis bukti dari persona karangan.
2. **Menyusun** (C3) persona dari sekumpulan catatan wawancara.
3. **Merumuskan** (C3) pernyataan *Jobs-to-be-Done* untuk satu segmen.
4. **Menganalisis** (C4) peta perjalanan pengguna untuk menemukan titik nyeri terbesar.
5. **Menilai** (C5) apakah sebuah persona layak dijadikan dasar keputusan produk.

---

## 3.1 Persona: Alat, Bukan Hiasan

### 3.1.1 Untuk Apa Persona Dibuat

Setelah 15 wawancara, tim memiliki 15 orang yang berbeda. Mereka tidak dapat semuanya dilayani, dan tidak semuanya menghadapi persoalan yang sama. Persona adalah cara memadatkan 15 orang menjadi **dua atau tiga sosok yang dapat dipakai dalam percakapan sehari-hari tim**.

Ujian kegunaan sebuah persona sangat sederhana: apakah ia dapat memutuskan perdebatan.

```
Tanpa persona:
  A: "Menurutku harusnya ada fitur laporan bulanan."
  B: "Menurutku itu tidak perlu."
  → perdebatan selera, tidak selesai

Dengan persona:
  A: "Apakah Bu Sri akan membuka laporan bulanan?"
  B: "Bu Sri tidak pernah membuka laporan apa pun.
      Dia cuma butuh tahu besok belanja berapa."
  → keputusan, berdasar bukti
```

Persona yang tidak dapat dipakai seperti itu — yang hanya menjadi satu halaman berfoto dalam laporan akhir — adalah hiasan, dan mata kuliah ini tidak menilainya.

### 3.1.2 Persona Berbasis Bukti vs Persona Karangan

| Aspek | Persona karangan | Persona berbasis bukti |
|-------|------------------|------------------------|
| Asal | Dibayangkan tim | Disarikan dari catatan wawancara |
| Nama | "Budi, 28, suka teknologi" | "Bu Sri" — gabungan 6 narasumber sejenis |
| Isi | Hobi, merek favorit, kutipan indah | Alur kerja, keterbatasan, kutipan verbatim |
| Dapat ditelusuri | Tidak | **Setiap baris menunjuk nomor wawancara** |
| Dapat dibantah | Tidak | Ya — bila wawancara baru membantahnya |

Baris terakhir adalah pembeda yang menentukan. Persona berbasis bukti dapat berubah. Bila pada wawancara ke-16 ditemukan bahwa pedagang seusia Bu Sri ternyata aktif memakai aplikasi pesan untuk memesan bahan, persona itu diperbarui dan perubahannya dicatat.

> Detail yang tidak berpengaruh pada keputusan tidak perlu ada. Merek ponsel yang dipakai Bu Sri hanya relevan bila tim benar-benar akan membuat sesuatu yang berjalan di ponsel — dan pada tahap ini, tim belum memutuskan akan membuat apa pun.

### 3.1.3 Anatomi Persona yang Dipakai

```markdown
## Persona 1 — "Bu Sri"

Disarikan dari wawancara #01, #03, #05, #07, #11, #14 (6 dari 15)

| Aspek | Isi | Sumber |
|-------|-----|--------|
| Peran | Pemilik sekaligus juru masak warung makan | #03, #05 |
| Skala usaha | 30-60 porsi/hari, omzet Rp900rb-1,5jt/hari | #01, #07, #11 |
| Lama usaha | 4-8 tahun | semua |
| Dibantu | Satu anggota keluarga, tidak tetap | #03, #11, #14 |
| Jam tersibuk | 11.00-14.00, tidak dapat diganggu | #03-1, #05-2 |
| Alat yang dipakai | Buku tulis, kalkulator ponsel, WhatsApp | #01, #03, #07 |
| Pernah mencoba | Aplikasi kasir (2 orang), ditinggalkan | #03-2, #11-3 |

### Yang Paling Diinginkan
Tahu besok harus belanja berapa, tanpa harus mencatat apa pun
hari ini. — turunan dari #03-3, #05-4, #07-2

### Yang Paling Dihindari
Apa pun yang menambah pekerjaan pada jam 11.00-14.00. — #03-1

### Kutipan Penanda
"Belanja ya kira-kira aja. Lihat kemarin habis berapa,
besok kira-kira segitu." (#03-4)
```

Kolom **Sumber** adalah bagian yang paling sering dihapus mahasiswa karena dianggap mengotori tampilan. Justru kolom itulah yang membuat persona dapat dipertahankan ketika dipertanyakan penguji.

---

## 3.2 *Jobs-to-be-Done*: Apa yang Sedang Diupayakan Orang

### 3.2.1 Gagasan Pokoknya

Orang tidak membeli produk; mereka **mempekerjakan** sesuatu untuk menyelesaikan urusan dalam hidupnya. Ketika ada cara yang lebih baik menyelesaikan urusan itu, produk lama diberhentikan.

| Yang dibeli | *Job* yang sebenarnya |
|-------------|----------------------|
| Buku tulis untuk stok | Menghindari rasa was-was saat belanja subuh |
| Aplikasi kasir | Terlihat rapi di mata pelanggan dan keluarga |
| Bantuan anak untuk menghitung | Menutup keterbatasan berhitung tanpa mengakuinya |

Kolom kanan menjelaskan hal yang tidak dapat dijelaskan kolom kiri: mengapa sebuah aplikasi kasir yang lebih lengkap dan lebih murah tetap ditinggalkan. Bila *job*-nya adalah "terlihat rapi", maka kelengkapan fitur tidak menambah apa pun, sedangkan kerepotan memakainya mengurangi banyak.

### 3.2.2 Bentuk Pernyataan *Job*

```
Ketika [SITUASI],
saya ingin [MOTIVASI],
sehingga saya dapat [HASIL YANG DIHARAPKAN].
```

Diisi dari studi kasus berjalan:

```
Ketika SAYA HENDAK BELANJA SUBUH DAN TIDAK INGAT
      PERSIS APA YANG HABIS KEMARIN,
saya ingin TAHU PERKIRAAN KEBUTUHAN HARI INI
      TANPA HARUS MENCATAT APA PUN SEMALAM,
sehingga saya dapat BELANJA SECUKUPNYA
      DAN TIDAK ADA BAHAN YANG TERBUANG.
```

Tiga ujian untuk pernyataan *job*:

| Ujian | Pertanyaan | Bila gagal |
|-------|------------|------------|
| **Bebas solusi** | Adakah kata "aplikasi", "sistem", "fitur"? | Tulis ulang tanpa kata itu |
| **Sudah ada sekarang** | Apakah *job* ini sudah dikerjakan orang hari ini dengan cara apa pun? | Bila tidak, mungkin bukan *job* nyata |
| **Tertelusur** | Kutipan mana yang mendasarinya? | Bila tidak ada, ia karangan |

Ujian kedua sering terlewat dan paling menentukan. Bila tidak ada seorang pun yang sedang mengupayakan hal itu dengan cara apa pun hari ini, kemungkinan besar itu bukan urusan yang dirasa perlu diselesaikan.

### 3.2.3 Tiga Lapis *Job*

| Lapis | Contoh pada kasus Bu Sri |
|-------|--------------------------|
| **Fungsional** — apa yang harus terjadi | Menentukan jumlah belanja yang tepat |
| **Emosional** — bagaimana ingin merasa | Tidak was-was saat menyerahkan uang ke pedagang sayur |
| **Sosial** — bagaimana ingin dilihat | Tidak terlihat boros oleh suami yang menanyakan pengeluaran |

Lapis fungsional adalah yang paling mudah ditemukan dan paling sering menjadi satu-satunya yang dicatat tim. Dua lapis lainnya menjelaskan hal-hal yang tampak tidak masuk akal — misalnya mengapa seseorang menolak solusi yang jelas lebih efisien.

Pada kasus di atas, lapis sosial menjelaskan sesuatu yang penting: solusi apa pun yang **menampilkan angka pengeluaran secara mencolok** berpotensi ditolak, bukan karena tidak berguna, melainkan karena membuka hal yang ingin dijaga.

---

## 3.3 Peta Perjalanan Pengguna

### 3.3.1 Memetakan Satu Hari

Peta perjalanan menggambarkan tahapan yang dilalui orang, apa yang dirasakannya di setiap tahap, dan di mana persoalan muncul.

```
TAHAP      Malam        Subuh        Pagi         Siang        Sore
           (tutup)      (belanja)    (persiapan)  (ramai)      (evaluasi)
───────────────────────────────────────────────────────────────────────
LAKUKAN    Bereskan     Ke pasar,    Masak,       Layani       Hitung
           dagangan     beli bahan   tata         pelanggan    uang
                                                   
PIKIRKAN   "Capek,      "Kira-kira   "Semoga      (tidak       "Untung
           besok lagi"  cukup ya?"   habis"       sempat       berapa
                                                  berpikir)    ya?"

RASAKAN    Lelah        WAS-WAS      Sibuk        Kewalahan    Lega/kecewa
                        ▲▲▲                                    
                        │                                      
TITIK      Tidak ada    ◄── NYERI TERBESAR                     
NYERI      data dari        Keputusan diambil                  
           kemarin          tanpa dasar                        
```

### 3.3.2 Membaca Peta Ini

| Temuan | Konsekuensi bagi rancangan |
|--------|---------------------------|
| Nyeri terbesar pada Subuh, bukan Sore | Solusi harus siap **sebelum** subuh, bukan menagih pencatatan malam |
| Siang tidak ada ruang berpikir | Apa pun yang menuntut perhatian jam 11–14 akan gagal |
| Malam adalah saat kelelahan | Meminta input data pada malam hari melawan keadaan |
| Sore ada jeda pendek | **Satu-satunya jendela** untuk input, bila memang diperlukan |

Baris terakhir adalah jenis temuan yang tidak akan pernah muncul dari lokakarya di dalam kelas. Ia hanya muncul dari mendengarkan orang menceritakan harinya.

### 3.3.3 Aturan Titik Nyeri Terbesar

Sebuah peta perjalanan biasanya memperlihatkan 3–5 titik nyeri. Tim harus memilih **satu** sebagai fokus.

| Kriteria pemilihan | Pertanyaan |
|--------------------|------------|
| Frekuensi | Berapa kali sehari/seminggu terjadi? |
| Besaran | Berapa kerugian atau waktu yang hilang? |
| Sudah dicoba diatasi | Apakah orang sudah mengeluarkan usaha untuk mengatasinya? |
| Dapat dijangkau tim | Dapatkah tim menyentuhnya dalam 14 minggu? |

Kriteria ketiga adalah penyaring terkuat. Nyeri yang belum pernah diupayakan siapa pun untuk diatasi biasanya bukan nyeri yang cukup besar — betapapun menyedihkan bunyinya ketika diceritakan.

---

## 3.4 Sintesis dalam Tim

### 3.4.1 Mengapa Sintesis Tidak Boleh Diserahkan kepada Satu Orang

Menyarikan 15 wawancara menjadi 2 persona adalah pekerjaan penafsiran. Penafsiran satu orang selalu membawa kecenderungannya sendiri, terutama kecenderungan untuk menemukan apa yang ia harapkan.

Karena itu sintesis dikerjakan bersama, dengan urutan berikut:

| Langkah | Cara | Waktu |
|---------|------|-------|
| 1. Baca sendiri | Setiap anggota membaca **seluruh** catatan, menandai sendiri | 30 menit |
| 2. Tempel penanda | Semua penanda ditempel di dinding/papan tanpa nama pembuat | 10 menit |
| 3. Kelompokkan bersama | Menyusun kelompok, berdebat tentang yang ambigu | 30 menit |
| 4. Namai kelompok | Beri nama yang memakai kata narasumber, bukan istilah tim | 10 menit |
| 5. Hitung sebaran | Berapa narasumber per kelompok | 10 menit |

Langkah 1 tidak dapat dilewati. Anggota yang tidak membaca catatan tidak dapat ikut menafsirkan — dan bila hanya satu orang yang membaca, tim sebenarnya sedang menerima kesimpulan satu orang.

> Inilah bentuk konkret kolaborasi yang dinilai pada `TEKNO-Sub-CPMKFSTS12-1`. Kolaborasi bukan berarti membagi pekerjaan menjadi potongan terpisah, melainkan **mengerjakan bagian yang sama dan membandingkan hasilnya**. Perbedaan penafsiran antaranggota adalah informasi, bukan gangguan.

### 3.4.2 Menangani Perbedaan Penafsiran

| Keadaan | Yang dilakukan |
|---------|----------------|
| Dua anggota menafsirkan satu kutipan berbeda | Kembali ke catatan; baca kalimat sebelum dan sesudahnya |
| Masih berbeda setelah dibaca ulang | Catat keduanya; jadikan pertanyaan wawancara berikutnya |
| Satu anggota bersikeras tanpa dasar kutipan | Tafsiran tanpa kutipan tidak dipakai |
| Semua sepakat terlalu cepat | Periksa apakah semua benar-benar membaca |

Baris kedua adalah jalan keluar yang paling sehat dan paling sering dilupakan: perbedaan penafsiran yang tidak dapat diselesaikan di meja **diselesaikan di lapangan**.

---

## 3.5 Kesalahan yang Berulang

| Kesalahan | Gejalanya | Perbaikan |
|-----------|-----------|-----------|
| Persona berisi hobi dan merek | Tidak ada satu pun baris yang mengubah keputusan | Hapus; isi dengan alur kerja dan keterbatasan |
| Persona adalah diri sendiri | Usia dan kebiasaan mirip anggota tim | Periksa kolom sumber; bila kosong, ia karangan |
| Terlalu banyak persona | 5–6 persona untuk 15 wawancara | Gabungkan; 2–3 sudah cukup |
| *Job* mengandung kata "aplikasi" | Solusi menyelinap ke dalam rumusan | Tulis ulang bebas solusi |
| Peta perjalanan tanpa emosi | Hanya daftar langkah | Tambahkan baris "rasakan"; di situ nyeri terlihat |
| Titik nyeri lebih dari satu | Tim tidak berani memilih | Pakai empat kriteria §3.3.3 |

---

## AI Corner — Bab 3

### Mengapa Sintesis Tidak Dapat Diwakilkan

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI memeriksa apakah persona mengandung detail yang tidak berguna | Meminta AI membuat persona dari deskripsi umum |
| Meminta AI menguji apakah pernyataan *job* masih mengandung solusi | Meminta AI merumuskan *job* tanpa membaca catatan tim |
| Meminta AI menyebutkan tahap yang mungkin terlewat dalam peta perjalanan | Meminta AI membuat peta perjalanan dari imajinasi |
| Meminta AI merapikan bahasa persona yang sudah disusun | Meminta AI menambah kutipan agar persona terlihat kaya |

### Yang Hilang Ketika AI Menyintesis

Sebuah model bahasa yang diberi 15 transkrip dapat menghasilkan persona yang rapi dan masuk akal dalam hitungan detik. Persona itu akan memuat pola yang **paling sering disebut dengan kata yang serupa**.

Yang hilang adalah pola yang disebut dengan kata yang berbeda-beda oleh orang yang berbeda. Justru di situlah temuan yang bernilai sering berada: enam narasumber menyebut hal yang sama dengan enam ungkapan yang tidak beririsan, dan hanya orang yang mendengarkan keenamnya yang menyadari bahwa mereka membicarakan hal yang satu.

Kemampuan mengenali kesamaan di balik ungkapan yang berbeda adalah inti keterampilan yang dinilai pada `TEKNO-Sub-CPMK091-1`. Menyerahkannya kepada AI berarti tidak mempelajarinya.

### Pemakaian yang Dianjurkan: Penguji Persona

```
Berikut persona yang tim saya susun dari 6 wawancara:
[tempelkan persona]

Untuk setiap baris, tanyakan kepada saya: keputusan produk apa
yang akan berubah bila baris ini berbeda? Tandai baris yang
tidak mengubah keputusan apa pun.

Jangan menambahkan baris baru.
```

Kalimat terakhir penting dan sering perlu diulang. Tanpa itu, model cenderung "melengkapi" persona dengan detail yang tidak berasal dari catatan tim — dan detail tambahan itu, sekali tertulis, sangat sulit dibedakan dari temuan asli beberapa minggu kemudian.

---

## Latihan Soal

### Tingkat Dasar

1. Sebutkan ujian kegunaan sebuah persona dan berikan satu contoh perdebatan tim yang dapat diselesaikan olehnya.
2. Jelaskan tiga lapis *job* dan berikan contoh masing-masing untuk seorang mahasiswa yang memilih tempat belajar.
3. Mengapa kolom "Sumber" dalam persona tidak boleh dihapus?
4. Tulis pernyataan *job* dengan format lengkap untuk: seseorang yang membeli kopi di kedai dekat kantor setiap pagi.
5. Apa tiga ujian yang harus dilewati sebuah pernyataan *job*?

### Tingkat Menengah

6. Berikut persona yang disusun sebuah tim. Sebutkan **lima** masalah di dalamnya dan perbaiki.

   ```
   Persona: Rina, 24 tahun, mahasiswa S1
   - Suka kopi dan musik indie
   - Pakai iPhone 14
   - Aktif di Instagram
   - Ingin aplikasi yang simpel dan modern
   - "Saya butuh solusi yang mempermudah hidup saya"
   ```

7. Ubah tiga pernyataan berikut menjadi pernyataan *job* yang bebas solusi:
   - "Pengguna butuh aplikasi pengingat minum obat."
   - "Pedagang butuh dashboard penjualan."
   - "Mahasiswa butuh platform berbagi catatan kuliah."

8. Gambarkan peta perjalanan (tahap, lakukan, pikirkan, rasakan) untuk seorang mahasiswa yang mengurus perpanjangan KRS. Tandai titik nyeri terbesar dan jelaskan alasan pemilihannya dengan empat kriteria §3.3.3.

9. Dua anggota tim menafsirkan kutipan *"Pernah beli aplikasi kasir, tapi ribet"* secara berbeda. Anggota A: masalahnya antarmuka. Anggota B: masalahnya narasumber tidak melihat manfaatnya sejak awal. Rumuskan satu pertanyaan wawancara yang akan menyelesaikan perbedaan ini di lapangan.

### Tingkat Mahir

10. **Latihan lapangan.** Dari delapan wawancara yang Anda kumpulkan pada Bab 2, susun dua persona lengkap dengan kolom sumber. Untuk setiap persona, tuliskan tiga keputusan produk yang dapat diputuskan olehnya, dan satu pertanyaan yang **tidak** dapat dijawabnya — lalu sebutkan data tambahan apa yang diperlukan.

11. Susun peta perjalanan untuk salah satu persona tersebut, lalu lakukan hal berikut: tunjukkan peta itu kepada salah satu narasumber asli dan minta ia mengoreksinya. Catat setiap koreksi. Jelaskan mengapa koreksi itu tidak dapat diperkirakan dari meja, dan apa yang berubah pada pilihan titik nyeri terbesar.

12. Sebuah tim menemukan bahwa lapis *job* emosional dan sosial dari personanya saling bertentangan: secara emosional narasumber ingin merasa terkendali, tetapi secara sosial ia tidak ingin terlihat mengawasi pengeluaran keluarganya. Jelaskan bagaimana pertentangan ini membatasi ruang rancangan solusi, dan rumuskan dua pendekatan yang menghormati keduanya. Tunjukkan bukti kutipan seperti apa yang diperlukan untuk memilih di antara keduanya.

---

## Rangkuman

| Gagasan pokok | Rumusan singkat |
|---------------|-----------------|
| Guna persona | Menyelesaikan perdebatan tim dengan bukti, bukan selera |
| Ujian persona | Setiap baris harus mengubah sebuah keputusan; bila tidak, hapus |
| Kolom sumber | Yang membedakan persona dari karangan |
| *Jobs-to-be-Done* | Orang mempekerjakan sesuatu untuk menyelesaikan urusan, bukan membeli produk |
| Tiga lapis *job* | Fungsional, emosional, sosial — dua terakhir menjelaskan penolakan yang tampak tak masuk akal |
| Peta perjalanan | Baris "rasakan" adalah tempat nyeri terlihat |
| Titik nyeri terpilih | Satu saja, dipilih dengan empat kriteria |
| Sintesis tim | Semua membaca semua; perbedaan tafsir diselesaikan di lapangan |

---

## Referensi

1. Christensen, C. M., Hall, T., Dillon, K., & Duncan, D. S. (2016). *Competing Against Luck: The Story of Innovation and Customer Choice*. HarperBusiness.
2. Cooper, A., Reimann, R., Cronin, D., & Noessel, C. (2014). *About Face: The Essentials of Interaction Design* (4th ed.). Wiley.
3. Ulwick, A. W. (2016). *Jobs to Be Done: Theory to Practice*. Idea Bite Press.
4. Kalbach, J. (2020). *Mapping Experiences: A Complete Guide to Customer Alignment Through Journeys, Blueprints, and Diagrams* (2nd ed.). O'Reilly Media.
5. Goodwin, K. (2009). *Designing for the Digital Age: How to Create Human-Centered Products and Services*. Wiley.
6. Saldaña, J. (2021). *The Coding Manual for Qualitative Researchers* (4th ed.). SAGE Publications.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul mingguan | [Minggu 3 — Persona, JTBD, dan Konteks Penggunaan](../03-modules/week-03-persona-jtbd-konteks-penggunaan.md) |
| Studio | [Studio 3 — Persona dan Peta Perjalanan](../04-labs/lab-03-persona-dan-peta-perjalanan.md) |
| Bab sebelumnya | [Bab 2 — Penemuan Masalah dan Pelanggan](bab-02-penemuan-masalah-dan-pelanggan.md) |
| Bab berikutnya | [Bab 4 — Dari Kebutuhan ke Persyaratan Produk](bab-04-dari-kebutuhan-ke-persyaratan.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
