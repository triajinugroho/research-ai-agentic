# PENUTUP

**Tri Aji Nugroho, S.T., M.T.**
Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (IF52510031) — Program Studi Informatika, Universitas Al Azhar Indonesia

---

## Yang Sudah Dilalui

Empat belas bab yang baru saja selesai dibaca sebenarnya menjawab satu pertanyaan, berulang-ulang dalam bentuk yang berbeda:

> **Kapan sebuah model layak dipercaya, dan untuk siapa?**

Bab 1–2 menjawabnya dengan cara paling mendasar: sebelum mempercayai model apa pun, pastikan masalahnya memang memerlukan model. Bab 3–5 memberi perhatian pada data, karena model tidak dapat lebih baik daripada apa yang melatihnya. Bab 6–9 membangun dan membandingkan model dengan protokol yang menjaga kejujuran perbandingannya. Bab 10–12 meluas ke pembelajaran tanpa supervisi, diagnosis, dan jaringan saraf. Bab 13–14 menutup dengan pertanyaan yang paling sulit: siapa yang dirugikan, dan siapa yang bertanggung jawab.

Bila ada satu kalimat yang pantas dibawa keluar dari mata kuliah ini, kalimat itu adalah: **setiap model memiliki batas keberlakuan, dan tugas insinyurnya adalah mengetahui batas itu dan menyatakannya.**

---

## Mengapa Mata Kuliah Ini Wajib bagi Semua

Pada Kurikulum Informatika 2025 Revisi 2026, mata kuliah ini berstatus **mode Core** pada AI Curriculum Infusion Matrix dan berperan sebagai **fondasi wajib AI seluruh mahasiswa** — bukan mata kuliah peminatan.

Penempatan itu disengaja. Visi program studi menyebut tiga domain keilmuan: *Software Engineering*, *Data Science*, dan *Artificial Intelligence*. Mata kuliah ini adalah satu-satunya mata kuliah wajib yang secara langsung mewujudkan domain ketiga bagi setiap lulusan — termasuk yang tidak akan bekerja di bidang AI.

Alasannya sederhana: pada 2026, hampir setiap lulusan informatika akan berhadapan dengan sistem berbasis pembelajaran mesin, entah sebagai pembangunnya, pengintegrasinya, pemeliharanya, atau orang yang harus menilai apakah sistem itu layak dipakai. Yang terakhir itu mungkin yang paling sering, dan paling menentukan.

### Lima Mata Kuliah yang Bergantung

| Mata kuliah | Yang dibawa dari sini |
|-------------|------------------------|
| Jaringan Syaraf Tiruan dan Pembelajaran Mendalam | Dasar pelatihan, *loss*, evaluasi, *overfitting* |
| Sains Data | Seluruh alur ML dan evaluasinya |
| Pengolahan Citra | Klasifikasi, metrik, validasi |
| Pengolahan Bahasa Alami | Klasifikasi, evaluasi, *embedding* sebagai fitur |
| Web Semantik | Representasi dan penalaran atas data |

Dan di ujungnya, **Tugas Akhir** — tempat seluruhnya diuji sekaligus, biasanya pada masalah yang belum pernah dikerjakan siapa pun sebelumnya.

---

## Tiga Hal yang Akan Bertahan

Sebagian besar nama algoritma pada Lampiran B akan terlupakan. Itu wajar dan tidak berbahaya — daftar algoritma dapat diperoleh siapa saja dalam hitungan detik. Tiga hal berikut yang sebaiknya tidak ikut terlupa.

### 1. Refleks Mencurigai Hasil yang Terlalu Bagus

Kebocoran data adalah satu-satunya jenis kesalahan dalam pembelajaran mesin yang *memberi hadiah* ketika dilakukan. Ia tidak menghasilkan galat; ia menghasilkan skor yang bagus.

Kapoor dan Narayanan menemukan kebocoran pada sebagian besar dari 294 makalah yang mereka telaah — makalah yang ditulis peneliti terlatih, melewati peninjauan sejawat, dan dipublikasikan. Yang membedakan mereka dari orang yang tidak terkena bukan kecerdasan, melainkan **kebiasaan curiga sebelum merayakan**.

### 2. Kebiasaan Menyertakan Pembanding

"Akurasi 94%" tidak bermakna apa pun sendirian. Ia bisa luar biasa atau lebih buruk daripada menebak.

Kebiasaan menyertakan *baseline* — dan simpangan, dan konteks — adalah salah satu dari sedikit hal yang, sekali terbentuk, terbawa sepanjang karier. Ia mengubah cara seseorang membaca klaim orang lain, bukan hanya cara ia melaporkan miliknya sendiri.

### 3. Keberanian Mengukur untuk Siapa Model Ini Gagal

Ini yang paling sulit, dan paling membedakan.

Menjalankan audit per kelompok menuntut usaha tambahan yang tidak diminta siapa pun. Melaporkan bahwa model bekerja jauh lebih buruk untuk suatu kelompok menuntut kesediaan memperlihatkan kelemahan karya sendiri — biasanya pada saat yang paling tidak nyaman, menjelang peluncuran.

Tidak ada pustaka yang akan mengingatkan. Tidak ada galat yang akan muncul. Hanya ada seseorang yang memutuskan untuk memeriksa, atau tidak.

---

## Pembelajaran Mesin dan Amanah

Nilai **amanah** dalam mata kuliah ini bukan tempelan pada bagian akhir silabus. Ia melekat pada pekerjaannya sendiri, dan pada bidang ini kaitannya lebih langsung daripada di banyak bidang lain.

Seorang insinyur pembelajaran mesin bekerja dengan sesuatu yang hampir tidak dapat diperiksa oleh orang lain. Ketika sebuah laporan menyatakan "tidak ada kebocoran data", hampir tak seorang pun akan membaca ulang seluruh notebook untuk memastikannya. Ketika sebuah laporan **tidak** menyebutkan bahwa modelnya melewatkan separuh kasus di Papua, hampir tak seorang pun akan mengetahuinya.

Di sinilah amanah bekerja — bukan sebagai aturan yang ditegakkan pengawas, melainkan sebagai sesuatu yang hanya diketahui oleh pelakunya sendiri, dan oleh Allah.

Bentuk sehari-harinya sederhana dan dapat diperiksa dalam setiap tugas:

- Menyertakan *baseline*, meski ia memperkecil kesan hebat hasil kita.
- Melaporkan simpangan, meski ia melemahkan klaim keunggulan model kita.
- Memeriksa kebocoran ketika skor sangat bagus, meski lebih menyenangkan untuk tidak memeriksanya.
- Menjalankan audit per kelompok, meski tidak ada yang memintanya.
- Menuliskan keterbatasan, meski mengurangi kesan meyakinkan.
- Mencantumkan bantuan AI yang dipakai, meski tidak ada yang akan tahu bila disembunyikan.

Keenamnya tidak menuntut kemampuan teknis tambahan. Yang dituntutnya adalah kesediaan untuk jujur ketika tidak jujur pun tidak akan ketahuan.

**Adil (`al-'adl`)** memperoleh wujud teknis yang tegas pada Bab 13: sebuah model dapat berakurasi tinggi secara keseluruhan dan tetap sistematis merugikan kelompok tertentu — biasanya kelompok yang paling sedikit terwakili dalam data, yang di Indonesia sering juga kelompok yang paling rentan. Angka rata-rata menyembunyikannya dengan sempurna.

Dan **tanggung jawab (`mas'uliyyah`)** menjawab pertanyaan yang tidak memiliki jawaban teknis: siapa yang bertanggung jawab ketika sebuah model merugikan seseorang? Pertanyaan itu selalu terjawab dengan nama seseorang — tidak pernah dengan nama sebuah model.

---

## Tentang AI — Sekali Lagi

Mata kuliah ini berstatus **mode Core**: AI adalah objek utama pembelajaran, bukan sekadar alat bantu. Justru karena itu pembatasan pemakaiannya lebih rinci daripada mata kuliah lain.

Pembagiannya dinyatakan berulang kali sepanjang buku ini: **AI untuk kode dan bahasa; manusia untuk formulasi, pemilihan, penafsiran, dan tanggung jawab.**

Empat hal di kolom kedua bukan dipilih karena sulit. Keempatnya dipilih karena menuntut pengetahuan yang tidak ada dalam prompt: kapan data setiap kolom tersedia, berapa biaya nyata tiap jenis kesalahan, bagaimana data dikumpulkan, siapa yang tidak tercakup di dalamnya.

Dan karena keempatnya justru merupakan **Sub-CPMK mata kuliah ini**. Menyerahkannya kepada alat sama dengan tidak mengikuti mata kuliah.

Pembagian ini bukan penolakan terhadap teknologi. Justru sebaliknya — ia adalah syarat agar teknologi itu dapat dipakai dengan bertanggung jawab. Seorang lulusan yang memahami pembelajaran mesin akan memakai AI jauh lebih efektif daripada yang tidak, **karena ia tahu kapan keluarannya keliru.**

Dan ketika sebuah sistem ternyata merugikan orang, yang dimintai pertanggungjawaban tidak pernah alatnya.

---

## Langkah Selanjutnya

### Bila Ingin Mendalami

| Minat | Ke mana |
|-------|---------|
| Arsitektur *deep learning* | Jaringan Syaraf Tiruan dan Pembelajaran Mendalam (IF52510032) |
| Alur data dan skala besar | Sains Data |
| Teks dan bahasa | Pengolahan Bahasa Alami (IF52510024) |
| Citra dan visi komputer | Pengolahan Citra (IF52510016) |
| Representasi pengetahuan | Web Semantik (IF52510003) |
| Keadilan algoritmik | *Fairness and Machine Learning* (Barocas et al., gratis daring) |
| Inferensi kausal | *The Book of Why* (Pearl & Mackenzie) |
| Penerapan dan pemeliharaan | *Designing Machine Learning Systems* (Huyen) |

### Kebiasaan yang Layak Dilanjutkan

1. **Selalu bangun *baseline* lebih dahulu**, pada pekerjaan apa pun.
2. **Curigai skor yang terlalu bagus** sebelum merayakannya.
3. **Ukur kinerja per kelompok**, bukan hanya agregat.
4. **Catat keputusan dan alasannya**, termasuk yang ternyata keliru.
5. **Nyatakan keterbatasan** sebelum orang lain menemukannya.

Kelima kebiasaan itu tidak memerlukan alat khusus, tidak menambah waktu kerja secara berarti, dan membedakan seorang insinyur dari seorang pengguna pustaka lebih daripada algoritma mana pun yang dikuasainya.

### Satu Latihan yang Layak Dilanjutkan

**Audit satu klaim berbasis AI setiap minggu.** Ambil satu berita, iklan produk, atau laporan yang mengklaim memakai kecerdasan artifisial, lalu tanyakan:

- Apa *baseline*-nya?
- Metrik apa yang dilaporkan, dan mana yang tidak?
- Data apa yang melatihnya, dan siapa yang tidak tercakup?
- Apa yang **tidak** dapat dilakukan sistem itu?

Empat pertanyaan ini dapat dijawab oleh siapa pun yang menyelesaikan mata kuliah ini, dan tidak dapat dijawab oleh sebagian besar orang lain. Kemampuan itu, lebih daripada kemampuan melatih model, adalah yang akan paling sering dibutuhkan.

---

## Ucapan Terima Kasih

Buku ini disusun untuk mahasiswa Program Studi Informatika Universitas Al Azhar Indonesia, mengacu pada **Kurikulum Informatika 2025 Revisi 2026**, khususnya pemetaan `DAIML-Sub-CPMK082-1` dan `DAIML-Sub-CPMK102-1` pada mata kuliah **IF52510031**.

Terima kasih disampaikan kepada Tim Kurikulum Program Studi Informatika UAI atas penyusunan kerangka OBE dan AI Curriculum Infusion Matrix yang menjadi dasar seluruh struktur buku ini, dan kepada para mahasiswa yang pertanyaannya di kelas — terutama yang sulit dijawab — membentuk bagian terbaik dari penjelasan di dalamnya.

Kritik dan koreksi atas isi buku ini sangat diharapkan, dan akan diperbaiki pada edisi berikutnya.

---

## Penutup

Kecerdasan artifisial sering dibicarakan sebagai persoalan kemampuan: seberapa besar modelnya, seberapa tinggi akurasinya, seberapa cepat kemajuannya.

Mata kuliah ini memperlakukannya sebagai persoalan **penilaian**: apakah masalah ini memang memerlukan model, apakah data ini layak dipercaya, apakah perbandingan ini adil, untuk siapa sistem ini bekerja lebih buruk, dan siapa yang memikul akibatnya.

Pertanyaan-pertanyaan itu tidak menjadi lebih mudah seiring model menjadi lebih besar. Justru sebaliknya: semakin mampu sebuah sistem, semakin besar akibat dari penilaian yang keliru tentang batas kemampuannya.

Dalam dunia di mana keputusan yang menyentuh hidup orang semakin sering melibatkan sistem yang dipelajari dari data, kemampuan menilai kapan sebuah sistem layak dipercaya bukan lagi keterampilan teknis. Ia adalah bentuk tanggung jawab.

Semoga buku ini membantu membentuknya.

---

**Jakarta, September 2026**

**Tri Aji Nugroho, S.T., M.T.**
Program Studi Informatika
Universitas Al Azhar Indonesia

---

| Navigasi |
|----------|
| [Halaman Depan](00-halaman-depan.md) · [Mengapa Buku Ini](mengapa-buku-ini.md) · [Bab 14](bab-14-proyek-akhir.md) · [Lampiran](lampiran.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
