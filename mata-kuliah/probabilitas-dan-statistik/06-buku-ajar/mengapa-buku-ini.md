# Mengapa Buku Ini Ditulis

**Tri Aji Nugroho, S.T., M.T.**

---

## Sebuah Percakapan yang Berulang

Setiap tahun, percakapan ini terjadi lagi.

Seorang mahasiswa datang membawa hasil model *machine learning*-nya. Akurasinya 94%. Ia senang. Saya bertanya satu hal:

> "Berapa persen data yang berlabel positif?"

Ia tidak tahu. Kami buka datanya bersama: 3%. Artinya sebuah model yang selalu menjawab "negatif" akan mencapai akurasi 97% — lebih tinggi dari modelnya, tanpa mempelajari apa pun.

Mahasiswa itu bukan mahasiswa yang malas. Ia bisa memanggil `sklearn`, membangun *pipeline*, bahkan melakukan *hyperparameter tuning*. Yang tidak ia miliki adalah **kemampuan menilai apakah angka yang keluar itu masuk akal**.

Buku ini ditulis untuk mencegah percakapan itu terjadi lagi.

---

## Tiga Alasan Buku Ini Ada

### 1. Karena statistika kini menjadi fondasi, bukan pelengkap

Visi keilmuan Prodi Informatika UAI 2025 menetapkan tiga domain resmi: **Software Engineering, Data Science, dan Artificial Intelligence**. Dua dari tiga domain itu berdiri di atas probabilitas dan statistika.

Sepuluh mata kuliah di semester-semester berikutnya bergantung pada apa yang dibangun di mata kuliah ini — dari Analisis Data Statistik di semester 2 sampai Tugas Akhir di semester 8. AI Curriculum Infusion Matrix Prodi menyatakan peran mata kuliah ini dengan tegas:

> *Fondasi uncertainty, inference dan ML. Mahasiswa tidak boleh menjadi sekadar pengguna model/API.*

Kalimat terakhir itulah yang menjadi jangkar buku ini.

### 2. Karena buku statistika yang ada jarang berbicara kepada mahasiswa Informatika

Buku statistika umumnya menyapa mahasiswa statistika, ekonomi, atau ilmu sosial. Contohnya tinggi badan, hasil panen, dan survei politik. Semuanya sah — tetapi tidak menjawab pertanyaan yang dihadapi seorang sarjana Informatika:

- Dua algoritma berselisih 5 ms. Apakah itu nyata atau kebetulan?
- Berapa kapasitas server yang harus disiapkan agar 99% waktu tidak kewalahan?
- Model saya akurat 94%. Apakah itu bagus?
- Sistem deteksi intrusi saya akurat 98%, tetapi timnya mengabaikan alarm. Mengapa?

Setiap konsep dalam buku ini diperkenalkan melalui pertanyaan seperti itu — bukan melalui rumus yang kemudian dicarikan contohnya.

### 3. Karena AI mengubah apa yang layak dinilai dari seorang analis

Ketika sebuah model bahasa dapat menjalankan uji-t dalam tiga detik, nilai seorang sarjana Informatika bergeser. Bukan lagi pada **kemampuan menjalankan analisis**, melainkan pada:

- Menilai apakah analisis itu **layak dijalankan** pada data ini.
- Memeriksa apakah **asumsinya terpenuhi**.
- Menyatakan apa yang **tidak dapat disimpulkan**.
- Mengakui **keterbatasan** dengan jujur.

Itu semua adalah penalaran, bukan eksekusi. Dan penalaran hanya tumbuh dengan dilatih — tidak bisa dipinjam dari mesin.

Karena itulah kebijakan AI mata kuliah ini **lebih ketat** daripada mata kuliah lain di repositori ini. Bukan karena tidak percaya pada teknologi, melainkan karena pada tahap fondasi, **kemandirian intelektual adalah capaian pembelajaran itu sendiri**.

---

## Apa yang Membedakan Buku Ini

### Konteks dulu, rumus kemudian

Setiap bab dibuka dengan persoalan yang belum bisa dijawab, baru diperkenalkan alatnya. Bukan sebaliknya.

### Asumsi diperiksa, bukan diasumsikan

Ini pembeda terbesar antara seorang analis dan seorang pemakai pustaka. Hampir setiap bab memuat bagian tentang asumsi apa yang menyertai sebuah metode dan apa yang terjadi bila dilanggar.

### Interpretasi dinilai setara dengan perhitungan

Dalam buku ini — dan dalam penilaian mata kuliahnya — jawaban berupa angka tanpa tafsir bernilai separuh. Angka yang benar tetapi salah ditafsirkan lebih berbahaya daripada angka yang salah, karena ia terdengar meyakinkan.

### Kejujuran dilindungi secara eksplisit

Hasil "tidak signifikan" adalah temuan yang sah dan tidak mengurangi nilai. Yang justru berat sanksinya adalah memanipulasi data agar hasilnya terlihat mengesankan.

Ini bukan kelonggaran, melainkan penerapan nilai **amanah** dalam konteks yang paling konkret: melaporkan apa yang benar-benar ditemukan, bukan apa yang ingin ditemukan.

### AI Corner yang berbeda arah

Di mata kuliah lain, AI Corner mengajarkan cara memakai AI untuk bekerja lebih baik. Di buku ini, AI Corner mengajarkan **cara memeriksa AI** — kesalahan apa yang khas dilakukannya pada soal probabilitas, mengapa ia sering membalik arah persyaratan, dan mengapa ia tidak dapat memilihkan uji statistik untuk data yang tidak ia kenal konteksnya.

---

## Untuk Siapa Buku Ini

Buku ini ditulis untuk mahasiswa **semester pertama** Program Studi Informatika UAI. Artinya:

- **Tidak mengandaikan kemampuan pemrograman.** Kode Python diperkenalkan bertahap; pada bab-bab awal, kode tinggal dijalankan.
- **Tidak mengandaikan latar matematika yang seragam.** Mahasiswa dari SMA IPA, IPS, dan SMK sama-sama diterima, dan bab-bab awal menyediakan penyegaran.
- **Mengandaikan kesediaan untuk berpikir pelan.** Statistika tidak bisa dikebut. Beberapa konsep — terutama distribusi sampling pada Bab 8 — memang memerlukan waktu untuk mengendap.

---

## Sebuah Harapan

Saya berharap, setelah menyelesaikan buku ini, ketika Anda kelak melatih sebuah model dan melihat angka akurasi 94%, pertanyaan pertama yang muncul di benak Anda bukan *"bagus juga"* melainkan:

> *"Berapa base rate-nya? Apakah ini lebih baik daripada menebak kelas mayoritas? Berapa interval kepercayaannya? Bagaimana data ini dikumpulkan?"*

Pertanyaan-pertanyaan itulah yang membedakan seorang sarjana Informatika dari seorang pengguna pustaka. Dan pertanyaan-pertanyaan itulah yang buku ini ingin tanamkan.

Selamat belajar.

---

**Jakarta, Agustus 2026**

**Tri Aji Nugroho, S.T., M.T.**
Program Studi Informatika
Universitas Al Azhar Indonesia

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
