# PENUTUP

**Tri Aji Nugroho, S.T., M.T.**
Probabilitas dan Statistik (IF52510033) — Program Studi Informatika, Universitas Al Azhar Indonesia

---

## Yang Sudah Dilalui

Empat belas bab yang baru saja selesai dibaca sebenarnya hanya menjawab satu pertanyaan, berulang-ulang dalam bentuk yang berbeda:

> **Seberapa jauh saya boleh percaya pada apa yang saya lihat dalam data?**

Bab 1–3 menjawabnya dengan cara paling langsung: lihat dulu datanya, ringkas, gambarkan. Bab 4–7 memberi bahasa untuk ketidakpastian itu — probabilitas, peubah acak, distribusi. Bab 8–12 memberi alat untuk melangkah dari sampel ke populasi, lengkap dengan pengakuan bahwa langkah itu selalu mengandung risiko salah. Bab 13 menghubungkan dua variabel dan menunjukkan mengapa hubungan bukan sebab. Bab 14 merangkai semuanya menjadi satu pekerjaan utuh.

Bila ada satu kalimat yang pantas dibawa keluar dari mata kuliah ini, kalimat itu adalah: **setiap angka memiliki batas keberlakuan, dan tugas analis adalah mengetahui batas itu.**

---

## Mengapa Mata Kuliah Ini Diletakkan di Semester Pertama

Pada Kurikulum Informatika 2025 Revisi 2026, Probabilitas dan Statistik ditempatkan pada **semester 1**, bukan semester 4 atau 5. Penempatan itu disengaja.

Hampir semua mata kuliah yang akan ditempuh kemudian bergantung padanya:

| Mata kuliah lanjutan | Apa yang dipakai dari sini |
|----------------------|----------------------------|
| Struktur Data dan Algoritma | Analisis kasus rata-rata; ekspektasi |
| Basis Data | Estimasi kardinalitas; statistik untuk optimasi kueri |
| Jaringan Komputer | Teori antrean; probabilitas tabrakan paket |
| Dasar Kecerdasan Artifisial dan Pembelajaran Mesin | Distribusi, Bayes, evaluasi model, uji signifikansi |
| Penambangan Data | Seluruh isi buku ini |
| Pengolahan Citra dan Visi Komputer | Distribusi derau; penapisan statistik |
| Keamanan Siber | Analisis anomali; entropi |
| Interaksi Manusia-Komputer | Rancangan eksperimen; uji A/B |
| Metodologi Penelitian | Rancangan sampel; inferensi; pelaporan hasil |
| Tugas Akhir | Seluruh isi buku ini |

Dua baris terakhir yang paling sering disadari terlambat. Ketika mahasiswa tiba di Tugas Akhir dan harus membuktikan bahwa metode yang diusulkannya **benar-benar** lebih baik daripada metode pembanding, yang dibutuhkan bukan kemampuan memprogram — melainkan kemampuan merancang perbandingan yang sah dan menafsirkan hasilnya dengan jujur. Itulah isi mata kuliah ini.

---

## Tiga Hal yang Akan Bertahan

Sebagian besar rumus pada Lampiran B akan terlupakan. Itu wajar dan tidak berbahaya — rumus dapat dicari kembali dalam tiga puluh detik. Tiga hal berikut yang sebaiknya tidak ikut terlupa.

### 1. Refleks Melihat Data Sebelum Mempercayai Angka

Kuartet Anscombe pada Bab 3 memberi pelajaran yang tidak ada gantinya: empat himpunan data dengan rata-rata, varians, korelasi, dan garis regresi yang nyaris identik dapat memiliki bentuk yang sama sekali berbeda. Satu di antaranya bahkan sepenuhnya ditentukan oleh sebuah pencilan tunggal.

Siapa pun yang hanya membaca statistik ringkasannya akan salah pada tiga dari empat kasus.

### 2. Kebiasaan Bertanya "Seberapa Besar?", Bukan Hanya "Apakah Ada?"

*p-value* menjawab pertanyaan pertama. Ukuran efek menjawab pertanyaan kedua. Melaporkan hanya yang pertama adalah kebiasaan yang, dalam skala besar, telah menghasilkan banyak literatur ilmiah yang tidak dapat direproduksi.

Pada n = 10.000, perbedaan yang sama sekali tidak berarti secara praktis akan tetap menghasilkan p < 0,001. Analis yang berhenti di situ akan melaporkan temuan yang, meski benar secara teknis, menyesatkan pembacanya.

### 3. Keberanian Menuliskan Apa yang Tidak Dapat Disimpulkan

Ini yang paling sulit, dan paling membedakan.

Menuliskan *"data ini tidak dapat menunjukkan sebab-akibat karena tidak ada pengacakan"* terasa seperti melemahkan tulisan sendiri. Sebenarnya sebaliknya: kalimat semacam itu menunjukkan bahwa penulisnya memahami rancangannya sendiri. Yang melemahkan sebuah laporan justru klaim yang melampaui apa yang didukung datanya — karena satu klaim semacam itu cukup untuk membuat seluruh laporan diragukan.

---

## Statistika dan Amanah

Nilai **amanah** dalam mata kuliah ini bukan tempelan pada bagian akhir silabus. Ia melekat pada pekerjaannya sendiri.

Seorang analis data bekerja dengan sesuatu yang tidak dapat diperiksa langsung oleh pembacanya. Ketika sebuah laporan menyatakan "12 baris dibuang karena nilai IPM kosong", hampir tak seorang pun akan mengunduh datanya dan menghitung ulang. Ketika sebuah laporan **tidak** menyebutkan bahwa 300 baris dibuang karena mengganggu hasil, hampir tak seorang pun akan mengetahuinya.

Di sinilah amanah bekerja — bukan sebagai aturan yang ditegakkan pengawas, melainkan sebagai sesuatu yang hanya diketahui oleh pelakunya sendiri, dan oleh Allah.

Bentuk sehari-harinya sederhana dan dapat diperiksa dalam setiap tugas:

- Mencatat berapa baris dibuang dan mengapa, meski tak seorang pun bertanya.
- Melaporkan hasil yang tidak signifikan, meski hasil itu mengecewakan.
- Mempertahankan pencilan yang sah, meski membuangnya akan membuat grafik lebih rapi.
- Menuliskan keterbatasan, meski mengurangi kesan meyakinkan.
- Mencantumkan bantuan AI yang dipakai, meski tidak ada yang akan tahu bila disembunyikan.

Kelima hal itu tidak menuntut kemampuan teknis tambahan. Yang dituntutnya adalah kesediaan untuk jujur ketika tidak jujur pun tidak akan ketahuan.

> Data tidak berbicara sendiri. Selalu ada seseorang yang memilih data mana yang ditampilkan, uji mana yang dilaporkan, dan kalimat mana yang ditulis. Kejujuran orang itu adalah satu-satunya yang menjaga agar angka tetap bermakna.

---

## Tentang AI — Sekali Lagi

Mata kuliah ini berstatus **tahap F (Foundation), mode K (Kontekstual)** pada AI Curriculum Infusion Matrix. Artinya AI hadir sebagai alat yang diakui, diatur, dan tidak diajarkan sebagai materi tersendiri.

Ada alasan mengapa pembatasannya justru lebih ketat di sini daripada di banyak mata kuliah lain. Model bahasa sangat mahir menghasilkan kalimat yang **terdengar** seperti analisis statistik yang baik. Ia dapat menuliskan interpretasi *p-value* yang rapi tanpa pernah melihat datanya, menyarankan uji yang lazim tanpa mengetahui apakah pengamatannya berpasangan, dan menyusun bagian keterbatasan yang meyakinkan tanpa mengetahui bagaimana data itu dikumpulkan.

Seluruh keputusan yang paling menentukan dalam analisis data bergantung pada pengetahuan yang **tidak ada** dalam prompt: siapa yang tercakup dalam sampel dan siapa yang tidak, bagaimana kolom itu didefinisikan oleh instansi penerbitnya, dan apa yang mungkin salah dalam pengumpulannya.

Karena itu pembagiannya tetap: **AI untuk kode dan bahasa; manusia untuk metode dan makna.**

Pembagian ini bukan penolakan terhadap teknologi. Justru sebaliknya — ia adalah syarat agar teknologi itu dapat dipakai dengan bertanggung jawab. Seorang lulusan yang memahami statistika akan memakai AI jauh lebih efektif daripada yang tidak, karena ia tahu kapan keluarannya keliru.

Dan ketika sebuah kesimpulan analisis ternyata salah, yang dimintai pertanggungjawaban tidak pernah alatnya.

---

## Langkah Selanjutnya

### Bila Ingin Mendalami Statistika

| Topik | Di mana dipelajari |
|-------|--------------------|
| Regresi berganda dan pemilihan model | Penambangan Data; belajar mandiri |
| Rancangan eksperimen lanjut | Metodologi Penelitian |
| Statistika Bayesian | Belajar mandiri; *Statistical Rethinking* (McElreath) |
| Analisis deret waktu | Belajar mandiri; mata kuliah pilihan |
| Statistika nonparametrik | Perluasan dari Bab 11–12 |
| Inferensi kausal | *The Book of Why* (Pearl & Mackenzie) |

### Bila Ingin Melanjutkan ke Pembelajaran Mesin

Regresi linear pada Bab 13 adalah model pembelajaran mesin paling sederhana. Yang berubah pada mata kuliah **Dasar Kecerdasan Artifisial dan Pembelajaran Mesin** adalah kompleksitas modelnya — sedangkan pertanyaan pokoknya tetap sama:

- Apakah perbedaan kinerja antara dua model ini nyata, atau sekadar keragaman sampel?
- Apakah data uji benar-benar mewakili data yang akan ditemui di lapangan?
- Seberapa yakin model ini pada prediksinya, dan atas dasar apa?

Ketiganya adalah pertanyaan statistika. Mahasiswa yang menguasai buku ini akan menemukan bahwa bagian tersulit dari pembelajaran mesin bukanlah algoritmanya, melainkan mengevaluasinya dengan jujur.

### Latihan yang Layak Dilanjutkan

1. **Ambil satu dataset BPS setiap bulan** dan tulis satu paragraf temuan yang jujur. Kebiasaan ini lebih berguna daripada membaca tiga buku tambahan.
2. **Audit satu berita berbasis data setiap minggu** dengan Lampiran F. Berapa banyak dari dua belas kesalahan itu yang ditemukan?
3. **Simpan catatan analisis sendiri** — keputusan apa yang diambil, mengapa, dan apa yang ternyata keliru. Ini yang membentuk penilaian (*judgement*), dan penilaian tidak dapat dipelajari dari buku.

---

## Ucapan Terima Kasih

Buku ini disusun untuk mahasiswa Program Studi Informatika Universitas Al Azhar Indonesia, mengacu pada **Kurikulum Informatika 2025 Revisi 2026**, khususnya pemetaan `PS-Sub-CPMK081-1` dan `PS-Sub-CPMK102-1` pada mata kuliah **IF52510033 — Probabilitas dan Statistik**.

Terima kasih disampaikan kepada Tim Kurikulum Program Studi Informatika UAI atas penyusunan kerangka OBE yang menjadi dasar seluruh struktur buku ini, dan kepada para mahasiswa yang pertanyaannya di kelas — terutama yang sulit dijawab — membentuk bagian terbaik dari penjelasan di dalamnya.

Kritik dan koreksi atas isi buku ini sangat diharapkan, dan akan diperbaiki pada edisi berikutnya.

---

## Penutup

Statistika sering dianggap sebagai mata kuliah tentang rumus. Sebenarnya ia adalah mata kuliah tentang **kerendahan hati intelektual** — tentang bagaimana mengatakan "saya cukup yakin" dan "saya tidak tahu" dengan tepat, dan tentang menolak mengatakan lebih dari yang didukung bukti.

Dalam dunia yang semakin dipenuhi klaim berbasis data — dari iklan produk sampai kebijakan publik, dari hasil riset sampai keluaran model bahasa — kemampuan membedakan klaim yang sah dari yang tidak bukan lagi keterampilan teknis. Ia adalah bentuk tanggung jawab.

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
