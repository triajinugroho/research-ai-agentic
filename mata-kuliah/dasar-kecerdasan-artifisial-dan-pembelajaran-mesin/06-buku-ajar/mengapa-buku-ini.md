# MENGAPA BUKU INI DITULIS

**Tri Aji Nugroho, S.T., M.T.**

---

## Ada Ratusan Kursus Pembelajaran Mesin. Mengapa Menambah Satu Lagi?

Pertanyaan itu wajar, dan jawabannya menentukan bentuk buku ini.

Sebagian besar materi pembelajaran mesin yang tersedia — baik kursus daring, video, maupun buku — menekankan **algoritma**. Urutannya hampir selalu sama: regresi linear, regresi logistik, pohon keputusan, SVM, jaringan saraf, dan seterusnya. Setiap algoritma dijelaskan, diimplementasikan, dan diukur akurasinya pada dataset yang sudah bersih.

Mahasiswa yang menyelesaikan materi semacam itu dapat melatih model. Yang sering tidak dapat mereka lakukan adalah:

- Mengenali bahwa masalah yang diajukan **tidak memerlukan** pembelajaran mesin.
- Menyadari bahwa akurasi 97% yang mereka capai berasal dari **kebocoran data**.
- Menjelaskan mengapa modelnya bekerja jauh lebih buruk untuk sebagian orang.
- Mengatakan "model ini belum layak dipakai" ketika memang demikian.

Keempat hal itu adalah yang paling dibutuhkan di lapangan, dan yang paling jarang diajarkan.

---

## Tiga Keputusan yang Membentuk Buku Ini

### 1. Data Mendapat Tiga Bab, Sebelum Satu Model pun Dilatih

Bab 3, 4, dan 5 seluruhnya tentang data: kualitas, pembagian, kebocoran, rekayasa fitur. Model pertama baru muncul di Bab 6.

Ini kebalikan dari kebanyakan materi, dan disengaja. Survei praktisi berulang kali menunjukkan bahwa sebagian besar waktu kerja nyata dihabiskan untuk data, bukan untuk model. Lebih penting lagi: **kegagalan proyek pembelajaran mesin di lapangan jauh lebih sering disebabkan data daripada pilihan algoritma.**

Bab 4 secara khusus dikhususkan untuk **kebocoran data** — satu-satunya jenis kesalahan dalam pembelajaran mesin yang *memberi hadiah* ketika dilakukan. Kebocoran tidak menghasilkan pesan galat; ia menghasilkan skor yang bagus. Itulah yang membuatnya berbahaya, dan itulah sebabnya ia memperoleh satu bab penuh.

### 2. Setiap Model Datang Bersama Metriknya

Tidak ada bab "algoritma" yang terpisah dari bab "evaluasi". Bab 6 membahas regresi **dan** MAE, RMSE, R², MAPE. Bab 7 membahas klasifikasi **dan** matriks konfusi, *precision*, *recall*, ROC.

Alasannya sederhana: model tanpa evaluasi yang tepat tidak berarti apa-apa. Seorang yang dapat melatih *gradient boosting* tetapi melaporkan akurasi pada data dengan 2% kelas positif belum memahami apa yang dikerjakannya.

### 3. Angka Kinerja Selalu Menuntut Pembanding

Sepanjang buku ini, setiap kali sebuah model dievaluasi, **skor *baseline* disertakan**. `DummyClassifier` muncul sejak Bab 2 dan tidak pernah hilang.

"Akurasi 78%" tidak bermakna apa pun sendirian. Ia bisa luar biasa atau bisa lebih buruk daripada menebak, bergantung pada berapa yang dicapai tanpa model sama sekali. Kebiasaan menyertakan pembanding adalah salah satu dari sedikit hal yang, sekali terbentuk, terbawa sepanjang karier.

---

## Konteks Indonesia Bukan Hiasan

Seluruh contoh dalam buku ini memakai data dan persoalan Indonesia: IPM provinsi dari BPS, kelayakan kredit UMKM, kepadatan TransJakarta, keluhan layanan publik, harga properti Jabodetabek.

Ini bukan sekadar pilihan gaya. Data Indonesia memiliki ciri yang tidak muncul pada dataset latihan internasional:

- **Nama wilayah tidak baku** — "DI Yogyakarta", "D.I. Yogyakarta", dan "Yogyakarta" adalah entitas yang sama, tetapi tidak bagi komputer.
- **Pemekaran wilayah** membuat kategori berubah antartahun.
- **Definisi variabel berbeda antar-terbitan** — hal yang hanya dapat diperiksa melalui SIRUSA.
- **Data terpusat di Jawa** — biasanya lebih dari 60% baris, yang berarti model yang dilatih darinya bekerja lebih buruk untuk wilayah lain.

Butir terakhir bukan sekadar persoalan teknis. Ia adalah persoalan keadilan, dan ia dibahas sebagai demikian pada Bab 13.

---

## Tentang AI Generatif

Buku ini ditulis pada masa ketika model bahasa dapat menghasilkan seluruh kode pembelajaran mesin yang diperlukan untuk sebuah proyek, dalam hitungan detik.

Menutup mata terhadap kenyataan itu akan membuat buku ini tidak berguna. Melarangnya sepenuhnya akan membuatnya tidak jujur. Karena itu posisinya dinyatakan terbuka dan tegas:

| Boleh dibantu AI | Tidak boleh dibantu AI |
|------------------|------------------------|
| Menulis kode `scikit-learn` rutin | Memformulasikan masalah menjadi *task* ML |
| Memperbaiki galat; menjelaskan dokumentasi | Memilih model dan hiperparameter |
| Menyarankan jenis visualisasi | Memilih dan menafsirkan metrik |
| Menyunting bahasa laporan | Menganalisis kesalahan dan keterbatasan |

Pembatasan di kolom kanan bukan kekhawatiran akan kecurangan. Alasannya teknis dan dapat diperiksa: **model bahasa tidak mengetahui konteks data Anda**. Ia tidak tahu bagaimana data dikumpulkan, siapa yang tercakup dan siapa yang tidak, atau apa arti sebenarnya sebuah kolom pada instansi penerbitnya. Seluruh keputusan di kolom kanan bergantung pada pengetahuan itu.

Lebih jauh lagi: empat hal di kolom kanan **justru merupakan Sub-CPMK mata kuliah ini**. Menyerahkannya kepada alat sama dengan tidak mengikuti mata kuliah.

---

## Nilai yang Melekat pada Pekerjaan Ini

Program Studi Informatika UAI menempatkan nilai etika dan keislaman sebagai pembeda lulusannya. Pada bidang pembelajaran mesin, kaitannya lebih langsung daripada yang mungkin diduga.

**Amanah** dalam bidang ini berwujud sangat konkret. Seorang insinyur pembelajaran mesin bekerja dengan sesuatu yang hampir tidak dapat diperiksa oleh orang lain. Ketika sebuah laporan menyatakan "tidak ada kebocoran data", hampir tak seorang pun akan membaca ulang seluruh notebook untuk memastikannya. Ketika sebuah laporan **tidak** menyebutkan bahwa modelnya bekerja jauh lebih buruk untuk penduduk Papua, hampir tak seorang pun akan mengetahuinya.

Di sinilah amanah bekerja — bukan sebagai aturan yang ditegakkan pengawas, melainkan sebagai sesuatu yang hanya diketahui oleh pelakunya sendiri, dan oleh Allah.

**Adil (`al-'adl`)** juga memperoleh wujud teknis yang tegas. Bab 13 menunjukkan bahwa sebuah model dapat berakurasi tinggi secara keseluruhan dan tetap sistematis merugikan kelompok tertentu — biasanya kelompok yang paling sedikit terwakili dalam data, yang sering kali juga kelompok yang paling rentan. Mengukurnya menuntut usaha tambahan yang tidak diminta siapa pun. Melaporkannya menuntut kesediaan memperlihatkan kelemahan karya sendiri.

Dan **tanggung jawab (`mas'uliyyah`)** menjawab pertanyaan yang tidak memiliki jawaban teknis: siapa yang bertanggung jawab ketika sebuah model merugikan seseorang? Pertanyaan itu selalu terjawab dengan nama seseorang — tidak pernah dengan nama sebuah model.

---

## Apa yang Sengaja Tidak Ada

Agar keluasan alur pembelajaran mesin klasik tercakup tuntas dalam 3 SKS, buku ini **tidak** membahas mendalam:

| Yang tidak dibahas | Mata kuliah yang membahasnya |
|--------------------|------------------------------|
| Arsitektur *deep learning* (CNN, RNN, Transformer) | Jaringan Syaraf Tiruan dan Pembelajaran Mendalam |
| Pemrosesan teks dan bahasa | Pengolahan Bahasa Alami |
| Pemrosesan citra dan visi komputer | Pengolahan Citra |
| *Pipeline* data skala besar dan MLOps | Sains Data |

Bab 12 hanya memberi pengantar jaringan saraf secukupnya untuk menjembatani — termasuk pembahasan jujur tentang mengapa, pada data tabular, metode berbasis pohon **masih sering mengunggulinya**.

Keputusan untuk melepaskan materi-materi itu adalah keputusan yang sulit, dan ia dibuat dengan alasan yang sama yang mendasari seluruh buku ini: lebih baik menguasai alur utuh dengan benar daripada mengenal banyak nama algoritma secara dangkal.

---

## Siapa yang Buku Ini Tujukan

Mahasiswa semester 5 Informatika UAI yang telah menempuh Probabilitas dan Statistik, Dasar-dasar Pemrograman, Struktur Data dan Algoritma, dan Basis Data.

Buku ini mengandaikan kemampuan Python dasar dan ingatan tentang distribusi, probabilitas bersyarat, serta inferensi statistik. Bagian yang paling sering terlupa — terutama karena rentang empat semester sejak Probabilitas dan Statistik — diulang secara terarah pada Bab 4 dan 7.

---

## Sebuah Harapan

Bila ada satu hal yang diharapkan terbawa setelah buku ini selesai dibaca, ia bukan kemampuan menyebut nama dua belas algoritma. Daftar algoritma dapat diperoleh siapa saja dalam hitungan detik.

Yang diharapkan adalah tiga kebiasaan:

1. **Menanyakan apakah masalah ini memang memerlukan pembelajaran mesin** — dan berani menjawab tidak.
2. **Mencurigai hasil yang terlalu bagus** sebelum merayakannya.
3. **Memeriksa siapa yang dirugikan** sebelum menyatakan sebuah model siap dipakai.

Ketiganya tidak memerlukan kecerdasan luar biasa. Ketiganya memerlukan kejujuran — terhadap data, terhadap pembaca laporan, dan terhadap diri sendiri.

---

**Jakarta, September 2026**

**Tri Aji Nugroho, S.T., M.T.**
Program Studi Informatika
Universitas Al Azhar Indonesia
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
