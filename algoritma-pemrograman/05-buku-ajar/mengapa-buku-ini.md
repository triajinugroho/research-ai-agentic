# Mengapa Buku Ini? — Positioning & Diferensiasi

**Tri Aji Nugroho, S.T., M.T.**
Algoritma dan Pemrograman — Prodi Informatika, Universitas Al Azhar Indonesia

---

## 1. Latar Belakang

Mengapa menulis satu lagi buku ajar tentang algoritma dan pemrograman?

Pertanyaan ini wajar — bahkan perlu — diajukan. Dunia pendidikan ilmu komputer sudah memiliki ratusan buku teks tentang algoritma, dari yang sangat teoretis hingga yang sangat praktis, dari yang setebal 1.200 halaman hingga yang bergambar lucu dan hanya 256 halaman. Nama-nama seperti Cormen, Sedgewick, dan Knuth sudah menjadi ikon dalam kanon literatur ilmu komputer. Lalu, apa yang masih kurang?

Jawabannya terletak pada sebuah kesenjangan yang sangat spesifik — sebuah celah yang tidak bisa dijawab oleh buku manapun yang tersedia saat ini, karena celah itu berada di persimpangan empat kebutuhan sekaligus:

**Pertama, bahasa.** Hampir seluruh buku algoritma dan pemrograman berkualitas tinggi ditulis dalam bahasa Inggris. Ini menciptakan hambatan ganda bagi mahasiswa Indonesia semester awal: mereka harus memahami konsep abstrak (algoritma, logika, struktur data) sekaligus menerjemahkan bahasa pengantar. Riset kognitif menunjukkan bahwa *cognitive load* meningkat signifikan ketika pembelajar harus memproses informasi dalam bahasa kedua, terutama untuk materi yang sudah secara inheren abstrak. Mahasiswa informatika semester 2 — yang baru pertama kali belajar pemrograman secara formal — membutuhkan buku yang menjelaskan konsep dalam bahasa ibu mereka, tanpa mengorbankan ketepatan terminologi teknis internasional.

**Kedua, konteks.** Buku-buku internasional menggunakan contoh dan dataset dari konteks Amerika: harga rumah di San Francisco, data cuaca di New York, sistem perpustakaan University of Michigan. Contoh-contoh ini terasa asing bagi mahasiswa Indonesia dan mengurangi kemampuan mereka untuk menghubungkan konsep abstrak dengan pengalaman nyata. Buku ajar yang menggunakan harga barang di pasar tradisional Jakarta, data TransJakarta, sistem antrian Puskesmas, atau data BPS akan jauh lebih bermakna secara pedagogi — mahasiswa dapat langsung *melihat* relevansi algoritma dalam kehidupan sehari-hari mereka.

**Ketiga, kurikulum.** Tidak ada buku algoritma internasional yang dirancang berdasarkan kerangka *Outcome-Based Education* (OBE) dan KKNI (*Kerangka Kualifikasi Nasional Indonesia*). Padahal, seluruh perguruan tinggi di Indonesia diwajibkan menggunakan standar ini oleh SN-Dikti. Dosen yang mengadopsi buku internasional harus melakukan pemetaan manual antara konten buku dengan CPMK (*Capaian Pembelajaran Mata Kuliah*), Sub-CPMK, dan taksonomi Bloom — pekerjaan yang memakan waktu dan rawan inkonsistensi.

**Keempat, dan paling krusial: era AI.** Sejak akhir 2022, dunia pemrograman telah berubah secara fundamental. GitHub Copilot, ChatGPT, Claude, dan berbagai AI coding assistant lainnya telah mengubah cara programmer profesional bekerja. Survei GitHub Developer Survey 2025 menunjukkan bahwa lebih dari 92% developer profesional menggunakan AI dalam workflow mereka. Namun, **belum ada satu pun buku algoritma dan pemrograman — dalam bahasa apapun — yang mengintegrasikan AI sebagai coding partner secara sistematis di setiap bab.** Buku-buku yang ada ditulis untuk era sebelum AI; mereka mengajarkan cara menulis kode dari nol, tetapi tidak mengajarkan cara berkolaborasi dengan AI untuk menulis kode yang lebih baik, lebih cepat, dan lebih bertanggung jawab.

Buku **"Algoritma dan Pemrograman: Fondasi Computational Thinking dengan Python dan AI"** hadir untuk menjawab keempat kesenjangan tersebut secara simultan. Buku ini bukan sekadar terjemahan atau adaptasi dari buku internasional. Ini adalah buku yang dirancang dari awal (*ground-up*) untuk mahasiswa informatika Indonesia di era AI — dengan bahasa Indonesia, konteks Indonesia, kurikulum OBE/KKNI, dan integrasi AI yang progresif dari bab pertama hingga bab terakhir.

---

## 2. Lanskap Buku Ajar Algoritma & Pemrograman

Untuk memahami positioning buku ini, penting untuk meninjau lanskap buku ajar yang sudah ada. Berikut adalah lima buku utama yang sering dijadikan rujukan dalam pendidikan algoritma dan pemrograman, beserta kekuatan dan keterbatasan masing-masing.

### 2.1 CLRS — *Introduction to Algorithms* (Cormen, Leiserson, Rivest, Stein)

Buku yang sering disebut sebagai *"the Bible of algorithms"* ini adalah standar emas untuk mata kuliah algoritma di universitas-universitas top dunia, termasuk MIT tempat buku ini lahir. Edisi keempat (2022) mencakup lebih dari 1.300 halaman yang membahas hampir setiap algoritma dan struktur data yang relevan dalam ilmu komputer.

**Kekuatan:** Kedalaman teori yang tak tertandingi, pembuktian matematis yang rigorous, cakupan topik yang komprehensif (dari sorting dan graph algorithms hingga NP-completeness dan approximation algorithms).

**Keterbatasan untuk konteks kita:** CLRS ditargetkan untuk mahasiswa *graduate* atau mahasiswa *undergraduate* tahun akhir yang sudah memiliki fondasi matematika diskret dan pengalaman pemrograman. Buku ini menggunakan pseudocode, bukan bahasa pemrograman yang bisa dijalankan. Bagi mahasiswa informatika semester 2 yang baru belajar pemrograman, CLRS terlalu berat — ibarat memberikan *textbook* kalkulus multivariabel kepada siswa yang baru belajar aljabar dasar. Tentu saja, tidak ada integrasi AI, konteks Indonesia, maupun pemetaan OBE/KKNI.

### 2.2 Sedgewick & Wayne — *Algorithms* (4th Edition)

Robert Sedgewick dari Princeton University menghadirkan pendekatan yang lebih visual dan berorientasi praktik dibanding CLRS. Buku ini dikenal karena visualisasi algoritma yang excellent dan website companion (algs4.cs.princeton.edu) yang menyediakan kode, animasi, dan *auto-grading assignments*.

**Kekuatan:** Visualisasi yang sangat baik, pendekatan praktis, website pendukung yang interaktif, koneksi antara teori dan implementasi yang elegan.

**Keterbatasan untuk konteks kita:** Buku ini berbasis Java — bahasa yang bukan pilihan utama untuk mata kuliah pemrograman dasar di banyak universitas Indonesia yang kini beralih ke Python. Level kontennya ditargetkan untuk CS2 hingga CS3, mengasumsikan mahasiswa sudah menguasai pemrograman dasar. Seluruh contoh dan konteks tetap dalam ranah Amerika. Tidak ada integrasi AI, OBE, maupun konteks lokal Indonesia.

### 2.3 *Grokking Algorithms* (Aditya Bhargava)

Buku ini mengambil pendekatan yang sangat berbeda — menjelaskan algoritma melalui ilustrasi *hand-drawn* yang menggemaskan dan narasi yang sangat kasual. Bhargava berhasil membuat topik seperti *binary search*, *recursion*, dan *dynamic programming* terasa mudah diakses oleh pembaca tanpa latar belakang ilmu komputer formal.

**Kekuatan:** Ilustrasi yang brilliant, bahasa yang sangat accessible, menggunakan Python untuk contoh kode, mampu menjelaskan konsep rumit dengan analogi sederhana.

**Keterbatasan untuk konteks kita:** Cakupan topik yang dangkal — buku ini hanya membahas beberapa algoritma dasar dan tidak cukup untuk sebuah mata kuliah satu semester penuh. Tidak ada latihan soal yang terstruktur, tidak ada proyek akhir, tidak ada pemetaan kurikulum. Buku ini lebih cocok sebagai bacaan pendamping (*supplementary reading*), bukan buku ajar utama. Konteks tetap Amerika, bahasa Inggris, tanpa integrasi AI.

### 2.4 *Think Python* (Allen B. Downey)

Buku karya Allen Downey ini adalah salah satu buku CS1 terbaik yang menggunakan Python. Tersedia gratis secara online, buku ini mengajarkan pemrograman dasar dan *computational thinking* melalui Python dengan pendekatan yang jelas dan terstruktur. Edisi terbaru sudah mengadopsi beberapa fitur Python modern.

**Kekuatan:** Gratis dan *open access*, menggunakan Python, ditargetkan untuk pemula (CS1), bahasa yang jelas dan ringkas, cakupan topik yang sesuai untuk mata kuliah pengantar pemrograman.

**Keterbatasan untuk konteks kita:** Seluruh konteks dan contoh berasal dari budaya Amerika. Tidak ada integrasi AI — buku ini ditulis untuk era sebelum AI coding assistants menjadi mainstream. Tidak ada pemetaan OBE/KKNI, tidak ada latihan bertingkat, tidak ada proyek akhir yang komprehensif. Buku ini menggunakan Thonny sebagai IDE, bukan Google Colab yang lebih accessible untuk konteks Indonesia.

### 2.5 *Learning Python* (Mark Lutz)

Buku Mark Lutz ini adalah referensi Python yang paling komprehensif — edisi kelima setebal lebih dari 1.600 halaman mencakup hampir setiap aspek bahasa Python. Buku ini menjadi rujukan standar bagi programmer yang ingin memahami Python secara mendalam.

**Kekuatan:** Cakupan Python yang paling komprehensif, penjelasan mendalam tentang setiap fitur bahasa, cocok sebagai referensi jangka panjang.

**Keterbatasan untuk konteks kita:** Buku ini adalah referensi bahasa Python, bukan buku tentang algoritma atau ilmu komputer fundamental. Tidak mengajarkan *computational thinking*, analisis algoritma, atau pemecahan masalah — hanya mengajarkan *how to use Python*. Terlalu tebal dan detail untuk mahasiswa semester 2. Tidak ada integrasi AI, OBE, konteks Indonesia, atau latihan yang terstruktur untuk kebutuhan akademis.

---

## 3. Tabel Perbandingan Komprehensif

Tabel berikut menyajikan perbandingan menyeluruh antara buku ini dengan lima buku utama di atas berdasarkan 15 kriteria yang relevan untuk konteks pendidikan algoritma dan pemrograman di Indonesia:

| Kriteria | CLRS | Sedgewick | Grokking | Think Python | Learning Python | **Buku Ini** |
|----------|:----:|:---------:|:--------:|:------------:|:--------------:|:------------:|
| **Bahasa pengantar** | English | English | English | English | English | **Indonesia** |
| **Target pembaca** | Graduate | CS2-CS3 | Self-learners | CS1/Intro | General | **Informatika S1 Sem 2** |
| **Bahasa pemrograman** | Pseudocode | Java | Python | Python | Python | **Python (Google Colab)** |
| **Integrasi AI/LLM** | Tidak | Tidak | Tidak | Tidak | Tidak | **Ya — setiap bab** |
| **Konteks dataset/contoh** | American | American | American | American | American | **Indonesia** |
| **Berbasis OBE/KKNI** | Tidak | Tidak | Tidak | Tidak | Tidak | **Ya — pemetaan CPMK** |
| **Nilai-nilai Islami** | Tidak | Tidak | Tidak | Tidak | Tidak | **Ya — terintegrasi** |
| **Warisan Al-Khwarizmi** | Mentioned | Mentioned | Not mentioned | Not mentioned | Not mentioned | **Ya — Bab 1 & throughout** |
| **Visualisasi algoritma** | Minimal | Excellent | Excellent | Moderate | Minimal | **Ya + interaktif (Colab)** |
| **Latihan bertingkat (3 level)** | Problem sets | Lab exercises | Tidak | Exercises | Tidak | **Ya — Dasar/Menengah/Mahir** |
| **Proyek akhir end-to-end** | Tidak | Tidak | Tidak | Exercises | Tidak | **Ya — Bab 14** |
| **Harga / Akses** | ~$80+ | ~$70+ | ~$40+ | Gratis | ~$50+ | **Gratis (institusional)** |
| **Platform executable** | Tidak | Website | Tidak | Thonny | Tidak | **Google Colab-ready** |
| **AI Corner per bab** | Tidak | Tidak | Tidak | Tidak | Tidak | **Ya — 14 bab** |
| **AI Usage pedagogy** | Tidak | Tidak | Tidak | Tidak | Tidak | **Ya — progresif 4 level** |

> **Catatan penting:** Tabel ini bukan dimaksudkan untuk mendiskreditkan buku-buku yang sudah mapan dan teruji. CLRS tetap menjadi rujukan algoritmik terbaik di dunia. Sedgewick tetap tak tertandingi dalam visualisasi. Grokking tetap menjadi gerbang masuk yang brilliant bagi pemula. Think Python tetap menjadi salah satu buku CS1 terbaik yang pernah ditulis. Learning Python tetap menjadi referensi bahasa Python paling komprehensif. Setiap buku memiliki posisi dan audiens optimalnya masing-masing. Yang buku ini tawarkan adalah sesuatu yang **tidak satupun dari mereka berikan**: sebuah buku algoritma dan pemrograman berbahasa Indonesia, berkonteks Indonesia, berbasis OBE, dan mengintegrasikan AI sebagai mitra belajar secara sistematis.

---

## 4. Tujuh Diferensiator Utama

### 4.1 Pertama di Indonesia: AI sebagai Coding Partner Terintegrasi Setiap Bab

Ini bukan sekadar menambahkan satu bab tentang AI di akhir buku. Buku ini mengintegrasikan AI sebagai **coding partner** di setiap bab melalui fitur **"AI Corner"** — sebuah bagian khusus yang mengajarkan mahasiswa cara berinteraksi dengan AI untuk topik yang sedang dipelajari.

Progresi AI literacy dalam buku ini dirancang secara bertahap dan terukur:

| Level | Bab | Kompetensi AI |
|-------|-----|---------------|
| **Dasar** | 1-4 | Menulis prompt sederhana, meminta penjelasan konsep, memvalidasi pemahaman dasar |
| **Menengah** | 5-7 | Menggunakan AI untuk debugging, meminta bantuan refactoring, membandingkan pendekatan solusi |
| **Lanjut** | 8-11 | AI-assisted problem solving, memvalidasi output AI secara kritis, co-designing algoritma |
| **Mahir** | 12-14 | AI pair programming end-to-end, prompt engineering untuk kode kompleks, evaluasi etis penggunaan AI |

Pada Bab 1, mahasiswa belajar hal dasar seperti bertanya kepada AI: *"Jelaskan apa itu algoritma dengan contoh kehidupan sehari-hari."* Pada Bab 14, mahasiswa sudah mampu menggunakan AI sebagai mitra pemrograman untuk membangun aplikasi end-to-end — menulis prompt yang presisi, memvalidasi setiap output, mendokumentasikan seluruh interaksi dalam AI Usage Log, dan mengevaluasi kontribusi AI secara kritis.

Pendekatan ini menjawab realitas dunia kerja: lulusan informatika tahun 2026 ke depan akan bekerja dengan AI, bukan menggantikan AI atau digantikan AI. Mereka perlu memahami kapan AI membantu, kapan AI menyesatkan, dan bagaimana menggunakan AI secara bertanggung jawab. Tidak ada buku algoritma lain — dalam bahasa apapun, dari penerbit manapun — yang menyediakan pedagogi AI selengkap ini.

### 4.2 100% Konteks Indonesia

Seluruh contoh, studi kasus, dan dataset dalam buku ini berasal dari konteks Indonesia. Ini bukan sekadar mengganti nama variabel dari "John" menjadi "Budi" — ini adalah desain pedagogis yang fundamental.

| Topik Buku | Contoh Konteks Indonesia |
|------------|--------------------------|
| Variabel & tipe data | Menghitung harga barang di warung, konversi mata uang Rupiah |
| Percabangan (if/else) | Menentukan tarif TransJakarta berdasarkan jarak, menghitung diskon Ramadhan |
| Perulangan (loop) | Mencetak pola batik sederhana, menghitung total belanja di pasar tradisional |
| Fungsi | Kalkulator IPK mahasiswa UAI, konversi nilai huruf ke angka |
| String | Mengolah data nama-nama kota Indonesia, memformat NIK (Nomor Induk Kependudukan) |
| List & Tuple | Mengelola daftar mahasiswa, data harga bahan pokok dari BPS |
| Dictionary & Set | Buku telepon digital, frekuensi kata dalam teks bahasa Indonesia |
| Searching | Mencari data mahasiswa berdasarkan NIM, mencari kota berdasarkan kode pos |
| Sorting | Mengurutkan data harga properti di Jakarta, mengurutkan ranking mahasiswa |
| Rekursi | Menghitung faktorial bilangan, deret Fibonacci dalam konteks perencanaan keuangan |
| Big-O | Membandingkan efisiensi pencarian data penduduk Indonesia (270+ juta record) |
| Proyek akhir | Aplikasi kasir warung, sistem antrian Puskesmas, game tebak kata bahasa Indonesia |

Riset dalam *situated learning theory* menunjukkan bahwa pembelajaran lebih efektif ketika contoh-contoh yang digunakan relevan dengan pengalaman dan budaya peserta didik. Mahasiswa yang menghitung harga cabai di pasar Tanah Abang akan lebih mudah memahami konsep variabel dan operasi aritmatika dibanding mahasiswa yang menghitung harga apel di supermarket New York — bukan karena contoh yang satu lebih baik dari yang lain secara teknis, melainkan karena konteks yang familiar mengurangi *extraneous cognitive load* sehingga kapasitas kognitif lebih banyak tersedia untuk memproses konsep inti.

### 4.3 Berbasis OBE/KKNI dengan Pemetaan CPMK Eksplisit

Buku ini bukan sekadar kumpulan materi — buku ini adalah bagian integral dari sebuah ekosistem kurikulum yang dirancang berdasarkan *Outcome-Based Education* (OBE) sesuai standar SN-Dikti dan KKNI Level 6 (Sarjana).

Setiap bab dalam buku ini memiliki:

- **Pemetaan CPMK** yang jelas — mahasiswa dan dosen tahu persis capaian pembelajaran apa yang ditargetkan
- **Sub-CPMK** dengan kata kerja Bloom yang terukur — dari C1 (mengingat) hingga C6 (mencipta)
- **Keterkaitan eksplisit** dengan RPS (*Rencana Pembelajaran Semester*) 16 minggu
- **Latihan soal bertingkat** yang mengukur ketercapaian Sub-CPMK pada tiga level: Dasar, Menengah, dan Mahir

Berikut ringkasan pemetaan CPMK buku ini:

| CPMK | Deskripsi | Bloom | Bab |
|------|-----------|-------|-----|
| CPMK-1 | Menjelaskan konsep dasar algoritma, computational thinking, dan peran pemrograman di era AI | C2 | 1 |
| CPMK-2 | Menerapkan variabel, tipe data, operator, dan ekspresi | C3 | 2 |
| CPMK-3 | Menerapkan struktur kontrol (seleksi dan perulangan) | C3 | 3, 4 |
| CPMK-4 | Menerapkan fungsi, string processing, dan modularitas | C3-C4 | 5, 6 |
| CPMK-5 | Menganalisis dan memilih struktur data yang tepat | C4 | 7, 8 |
| CPMK-6 | Menganalisis dan mengimplementasikan algoritma pencarian, pengurutan, dan rekursi | C4-C5 | 9, 10, 11 |
| CPMK-7 | Mengevaluasi efisiensi algoritma dan merancang solusi end-to-end dengan AI | C5-C6 | 12, 13, 14 |

Tidak ada buku algoritma internasional yang menyediakan pemetaan OBE/KKNI semacam ini. Dosen yang menggunakan buku ini tidak perlu melakukan pemetaan manual — semuanya sudah tersedia, terverifikasi, dan siap digunakan langsung dalam RPS dan laporan akreditasi.

### 4.4 Google Colab-Ready — Tanpa Instalasi, Gratis, Aksesibel

Seluruh kode Python dalam buku ini dirancang untuk berjalan langsung di **Google Colab** — platform cloud-based notebook dari Google yang gratis dan hanya memerlukan browser serta akun Google.

Mengapa ini penting untuk konteks Indonesia?

1. **Eliminasi hambatan teknis.** Tidak semua mahasiswa memiliki laptop dengan spesifikasi cukup untuk menginstal Python, Anaconda, atau IDE berat seperti PyCharm. Dengan Google Colab, mahasiswa cukup membuka browser — bahkan dari smartphone — untuk mulai menulis dan menjalankan kode Python.

2. **Konsistensi lingkungan.** Tidak ada lagi masalah "di laptop saya jalan, tapi di laptop saya tidak" yang sering terjadi ketika mahasiswa menggunakan sistem operasi, versi Python, atau konfigurasi yang berbeda-beda. Google Colab menyediakan lingkungan yang identik untuk semua pengguna.

3. **Kolaborasi mudah.** Dosen dapat membagikan notebook yang langsung siap dijalankan oleh mahasiswa. Mahasiswa dapat berkolaborasi dalam satu notebook, mirip dengan Google Docs. Submission tugas dapat dilakukan melalui link Colab.

4. **Aksesibilitas ekonomi.** Google Colab gratis. Bagi mahasiswa yang belum memiliki laptop, mereka dapat mengakses Colab dari komputer lab kampus, warnet, atau bahkan smartphone. Ini mendukung prinsip inklusivitas dalam pendidikan.

Setiap bab dalam buku ini menyertakan kode yang telah diuji di Google Colab, lengkap dengan komentar dalam bahasa Indonesia dan petunjuk untuk menjalankannya. Bab 1 bahkan menyediakan panduan langkah demi langkah untuk membuat akun Google Colab dan menjalankan program Python pertama.

### 4.5 Warisan Al-Khwarizmi & Nilai-Nilai Islami

Tahukah Anda bahwa kata **"algoritma"** — istilah yang menjadi judul buku ini dan inti dari seluruh ilmu komputer — berasal dari nama seorang ilmuwan Muslim?

**Muhammad ibn Musa al-Khwarizmi** (sekitar 780–850 M), seorang matematikawan, astronom, dan geograf dari Persia yang bekerja di *Baitul Hikmah* (House of Wisdom) di Baghdad, menulis kitab *Al-Kitab al-Mukhtasar fi Hisab al-Jabr wal-Muqabalah* yang menjadi dasar aljabar modern. Nama "Al-Khwarizmi" kemudian di-Latinkan menjadi "Algoritmi" dan akhirnya menjadi kata "algorithm" yang kita gunakan hari ini. Kata "aljabar" (*algebra*) pun berasal dari judul kitabnya.

Buku ini mengangkat warisan Al-Khwarizmi bukan sekadar sebagai trivia sejarah di paragraf pembuka, melainkan sebagai **narasi yang hidup** sepanjang buku. Di Bab 1, mahasiswa belajar tentang kontribusi monumental Al-Khwarizmi dan bagaimana tradisi ilmiah Islam menjadi fondasi ilmu komputer modern. Di bab-bab selanjutnya, koneksi ini terus dijaga — mengingatkan mahasiswa bahwa mereka adalah pewaris tradisi intelektual yang kaya.

Sebagai buku ajar di **Universitas Al Azhar Indonesia**, buku ini juga menanamkan nilai-nilai Islami secara natural — bukan dipaksakan — dalam konteks pemrograman:

- **Amanah** (*trustworthiness*): Kejujuran dalam menulis kode, tidak plagiat, academic integrity saat menggunakan AI
- **Keadilan** (*al-'Adl*): Fairness dalam pengujian program, menangani edge cases, tidak bias dalam algoritma
- **Ihsan** (*excellence*): Clean code, best practices, *continuous improvement* — menulis kode terbaik yang kita mampu
- **Transparansi**: Code readability, dokumentasi yang jelas, semangat open source
- **Ilmu yang bermanfaat**: Orientasi bahwa kemampuan programming harus digunakan untuk kebaikan masyarakat

Nilai-nilai ini bukan sisipan terpisah, melainkan terintegrasi secara kontekstual dalam studi kasus, diskusi etika, dan refleksi di akhir setiap bab. Mahasiswa belajar bahwa menjadi programmer yang baik bukan hanya tentang menulis kode yang benar, tetapi juga tentang menulis kode yang bertanggung jawab.

### 4.6 AI Literacy Progresif 4 Tingkat

Integrasi AI dalam buku ini bukan *one-size-fits-all*. AI Corner di setiap bab dirancang dengan progresi yang cermat, mengikuti prinsip *scaffolding* dalam teori pembelajaran:

**Tingkat 1 — Dasar (Bab 1-4): AI sebagai Tutor**

Pada fase ini, mahasiswa baru mengenal AI dan belajar menggunakannya sebagai alat bantu pemahaman. Aktivitas AI Corner berfokus pada:
- Meminta AI menjelaskan konsep yang belum dipahami
- Membandingkan penjelasan AI dengan penjelasan di buku
- Menulis prompt sederhana dan mengamati hasilnya
- Menyadari bahwa AI bisa salah dan perlu divalidasi

Contoh prompt Bab 2: *"Jelaskan perbedaan antara tipe data int dan float dalam Python, berikan contoh kasus di mana perbedaannya penting."*

**Tingkat 2 — Menengah (Bab 5-7): AI sebagai Debugging Partner**

Pada fase ini, mahasiswa mulai menggunakan AI untuk membantu proses pengembangan kode:
- Meminta AI membantu menemukan bug dalam kode
- Menggunakan AI untuk refactoring kode menjadi lebih modular
- Membandingkan solusi sendiri dengan solusi yang disarankan AI
- Belajar menulis prompt yang lebih spesifik dan kontekstual

Contoh prompt Bab 5: *"Saya punya fungsi Python berikut yang menghitung diskon. Bisakah kamu review dan sarankan perbaikan? [kode]"*

**Tingkat 3 — Lanjut (Bab 8-11): AI sebagai Co-Designer**

Pada fase ini, mahasiswa berkolaborasi dengan AI untuk merancang solusi:
- Co-designing algoritma: mendiskusikan pendekatan sebelum menulis kode
- Meminta AI menjelaskan trade-off antara berbagai struktur data
- Memvalidasi output AI secara kritis — tidak menerima begitu saja
- Mendokumentasikan interaksi dengan AI dalam AI Usage Log

Contoh prompt Bab 10: *"Saya perlu mencari data mahasiswa berdasarkan NIM dalam list yang sudah terurut. Bandingkan pendekatan linear search vs binary search, jelaskan kapan masing-masing lebih tepat, dan berikan implementasi Python keduanya."*

**Tingkat 4 — Mahir (Bab 12-14): AI sebagai Pair Programmer**

Pada fase ini, mahasiswa menggunakan AI sebagai mitra pemrograman profesional:
- AI pair programming end-to-end: dari perumusan masalah hingga deployment
- Prompt engineering yang sophisticated untuk kode kompleks
- Evaluasi etis penggunaan AI — kapan AI membantu vs kapan AI menggantikan belajar
- Membangun proyek akhir dengan AI sebagai partner yang terdokumentasi

Contoh prompt Bab 14: *"Saya ingin membangun sistem antrian Puskesmas dengan Python. Bantu saya merancang arsitektur program: apa saja modul yang dibutuhkan, struktur data yang tepat, dan algoritma antrian yang efisien. Jangan langsung berikan kode — diskusikan desainnya dulu."*

Progresi ini memastikan bahwa mahasiswa membangun kompetensi AI secara bertahap dan solid — mereka tidak langsung "lompat" ke AI pair programming tanpa terlebih dahulu memahami dasar-dasar interaksi dengan AI dan membangun kebiasaan validasi kritis.

### 4.7 Bahasa Indonesia dengan Terminologi Bilingual

Buku ini ditulis sepenuhnya dalam **Bahasa Indonesia** — menghilangkan hambatan bahasa yang sering dirasakan oleh mahasiswa semester awal. Namun, buku ini tidak mengorbankan ketepatan terminologi internasional.

Pendekatan yang digunakan adalah **terminologi bilingual**: setiap istilah teknis disajikan dalam bahasa Indonesia disertai padanan bahasa Inggris dalam tanda kurung saat pertama kali muncul.

Contoh-contoh:
- *Perulangan* (*loop*)
- *Percabangan* (*branching* / *conditional*)
- *Fungsi* (*function*)
- *Tipe data* (*data type*)
- *Pencarian* (*searching*)
- *Pengurutan* (*sorting*)
- *Rekursi* (*recursion*)
- *Kompleksitas waktu* (*time complexity*)

Pendekatan ini memberikan dua keuntungan sekaligus:

1. **Pemahaman konsep yang lebih dalam.** Mahasiswa memahami konsep dalam bahasa ibu mereka — mengurangi *cognitive load* dan memungkinkan fokus penuh pada pemahaman konseptual.

2. **Kesiapan global.** Mahasiswa tetap mengenal terminologi bahasa Inggris yang akan mereka temui di dunia kerja, dokumentasi teknis, Stack Overflow, dan literatur internasional.

Glosarium bilingual lengkap disediakan di Lampiran C untuk referensi cepat.

---

## 5. Apa yang Buku Ini Bukan

Transparansi tentang cakupan dan batasan buku ini sama pentingnya dengan menjelaskan keunggulannya. Berikut adalah penegasan tentang apa yang buku ini **bukan** — beserta rujukan alternatif yang tepat:

| Buku ini bukan... | Untuk itu, lihat... |
|--------------------|---------------------|
| Buku algoritma tingkat lanjut (graduate) — tidak membahas graph algorithms lanjutan, dynamic programming, NP-completeness | CLRS (Cormen et al.), Kleinberg & Tardos — *Algorithm Design* |
| Buku OOP (Object-Oriented Programming) — tidak membahas class, inheritance, polymorphism, design patterns | Head First Design Patterns, Clean Code (Robert C. Martin) |
| Buku struktur data lanjutan (trees, graphs, heaps) — hanya membahas list, tuple, dict, set | Goodrich et al. — *Data Structures and Algorithms in Python*, Sedgewick |
| Panduan competitive programming — tidak membahas teknik kompetisi, contest strategy | Halim — *Competitive Programming Handbook*, Laaksonen — *Guide to Competitive Programming* |
| Referensi lengkap bahasa Python — tidak membahas semua fitur Python secara mendalam | Lutz — *Learning Python*, docs.python.org |
| Tutorial web development — tidak membahas HTML, CSS, JavaScript, framework web | Tutorial Django, Flask, FastAPI |
| Buku data science/machine learning — tidak membahas neural networks, deep learning, model training | Hands-On ML (Aurelien Geron), ISL/ISLP (James et al.) |

Buku ini berada di **irisan strategis** antara empat domain: *computational thinking*, pemrograman dasar Python, algoritma fundamental, dan AI literacy. Buku ini dirancang untuk memberikan fondasi yang kokoh (*strong foundation*) — bukan cakupan yang luas (*broad coverage*). Mahasiswa yang menyelesaikan buku ini akan memiliki pondasi yang solid untuk melangkah ke topik-topik lanjutan di atas.

Secara visual, posisi buku ini dapat digambarkan sebagai berikut:

```
                    ┌─────────────────────────────┐
                    │   Algoritma Lanjutan (CLRS)  │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    │   Struktur Data Lanjutan     │
                    │   (Goodrich, Sedgewick)      │
                    └──────────────┬──────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         │                         │                         │
    ┌────┴────┐          ┌─────────┴─────────┐        ┌──────┴──────┐
    │   OOP   │          │  ╔═══════════════╗ │        │    Data     │
    │ (Clean  │          │  ║  BUKU INI:    ║ │        │  Science   │
    │  Code)  │          │  ║  Fondasi      ║ │        │ (Hands-On  │
    └─────────┘          │  ║  Algoritma +  ║ │        │    ML)     │
                         │  ║  Python +     ║ │        └────────────┘
                         │  ║  AI Literacy  ║ │
                         │  ╚═══════════════╝ │
                         └───────────────────┘
```

Buku ini adalah **titik awal** — fondasi dari mana mahasiswa dapat berkembang ke berbagai arah sesuai minat dan karir mereka.

---

## 6. Untuk Siapa Buku Ini?

Buku ini dirancang untuk beberapa kategori pembaca dengan tingkat kebutuhan yang berbeda:

### 6.1 Audiens Primer: Mahasiswa S1 Informatika Semester 2, Universitas Al Azhar Indonesia

Ini adalah audiens utama buku ini. Mahasiswa informatika UAI semester 2 (Genap 2025/2026) yang mengambil mata kuliah Algoritma dan Pemrograman akan menggunakan buku ini sebagai buku ajar utama sepanjang 16 minggu perkuliahan. Buku ini selaras dengan RPS, CPMK, jadwal perkuliahan, dan sistem asesmen yang telah dirancang secara terpadu.

**Profil mahasiswa yang diasumsikan:**
- Sudah menyelesaikan mata kuliah Pengantar Informatika dan/atau Logika Matematika di semester 1
- Memiliki pemahaman dasar tentang komputer dan internet
- Belum tentu memiliki pengalaman pemrograman formal sebelumnya
- Memiliki akses ke komputer/laptop dan internet
- Bersemangat tetapi mungkin cemas menghadapi pemrograman pertama kali

### 6.2 Audiens Sekunder: Mahasiswa Prodi Lain yang Belajar Pemrograman Dasar

Mahasiswa dari program studi non-informatika — seperti Teknik Elektro, Sistem Informasi, Matematika, atau bahkan prodi non-teknik yang mewajibkan mata kuliah pemrograman dasar — dapat menggunakan buku ini sebagai panduan belajar. Pendekatan yang sangat step-by-step, penggunaan bahasa Indonesia, dan konteks lokal membuat buku ini accessible untuk mahasiswa dengan berbagai latar belakang.

### 6.3 Audiens Tersier: Dosen yang Ingin Mengajar dengan Pendekatan Modern

Dosen pengampu mata kuliah algoritma dan pemrograman di universitas lain dapat mengadopsi atau mengadaptasi buku ini. Pemetaan OBE/KKNI dapat disesuaikan dengan kurikulum masing-masing institusi, sementara materi inti, contoh kode, dan latihan tetap relevan. Khususnya, integrasi AI Corner memberikan kerangka kerja (*framework*) yang belum tersedia di buku manapun untuk dosen yang ingin mengajarkan *AI-augmented programming* secara sistematis.

### 6.4 Self-Learners: Siapapun yang Ingin Belajar Algoritma + Python dalam Bahasa Indonesia

Buku ini juga cocok untuk *self-learners* — individu yang ingin belajar pemrograman secara mandiri. Struktur yang jelas, progresi yang terukur, latihan bertingkat, dan aksesibilitas Google Colab membuat buku ini dapat diikuti tanpa bimbingan dosen. Namun, perlu dicatat bahwa beberapa komponen (seperti proyek akhir dan presentasi) dirancang untuk konteks kelas dan memerlukan adaptasi untuk pembelajaran mandiri.

---

## 7. Bagaimana Buku Ini Lahir?

Buku ini lahir dari pertemuan tiga kebutuhan yang datang secara bersamaan.

**Kebutuhan pertama: tuntutan akreditasi dan OBE.** Ketika Program Studi Informatika Universitas Al Azhar Indonesia mempersiapkan akreditasi dan menerapkan kurikulum berbasis OBE sesuai SN-Dikti, setiap mata kuliah memerlukan buku ajar yang selaras dengan Capaian Pembelajaran Lulusan (CPL) dan Capaian Pembelajaran Mata Kuliah (CPMK). Buku-buku internasional, meskipun berkualitas tinggi, tidak menyediakan pemetaan ini. Diperlukan buku ajar yang *by design* dibangun di atas kerangka OBE/KKNI — bukan buku yang dipaksakan masuk ke dalam kerangka tersebut setelah ditulis.

**Kebutuhan kedua: revolusi AI dalam pemrograman.** Tahun 2023-2026 menyaksikan perubahan paradigma dalam cara programmer bekerja. AI coding assistants bukan lagi eksperimen — mereka adalah realitas sehari-hari. Survei demi survei menunjukkan bahwa developer profesional menggunakan AI untuk menulis, me-review, dan men-debug kode. Namun, kurikulum pendidikan pemrograman belum bergerak untuk mengakomodasi realitas ini. Mahasiswa belajar menulis kode seolah-olah AI tidak ada, lalu lulus dan menemukan bahwa dunia kerja mengharapkan mereka mampu bekerja *dengan* AI. Buku ini lahir dari keyakinan bahwa pendidikan pemrograman harus mempersiapkan mahasiswa untuk dunia nyata — dan dunia nyata sekarang melibatkan AI.

**Kebutuhan ketiga: keinginan untuk menghubungkan warisan Islam dengan ilmu komputer modern.** Kata "algoritma" berasal dari nama Al-Khwarizmi — seorang ilmuwan Muslim dari abad ke-9. Kata "aljabar" berasal dari judul kitabnya. Fakta ini sering disebut sekilas di buku-buku barat, tetapi tidak pernah diangkat sebagai narasi yang bermakna. Di Universitas Al Azhar Indonesia — sebuah institusi yang mengusung visi *"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — ada kesempatan unik untuk menghidupkan kembali koneksi ini. Bukan untuk klaim superioritas, melainkan untuk menginspirasi: bahwa tradisi intelektual Islam adalah bagian integral dari sejarah ilmu komputer, dan mahasiswa Muslim hari ini adalah pewaris tradisi itu.

Ketiga kebutuhan ini — OBE, AI, dan identitas Islami — bertemu dalam satu buku. Hasilnya adalah buku ajar yang tidak sekadar mengajarkan Python dan algoritma, tetapi juga mempersiapkan mahasiswa untuk menjadi *problem solver* yang kompeten secara teknis, literate dalam AI, dan berakar pada nilai-nilai etika.

Buku ini ditulis dengan satu keyakinan sederhana: **mahasiswa Indonesia berhak memiliki buku algoritma dan pemrograman yang berbicara dalam bahasa mereka, menggunakan contoh dari dunia mereka, selaras dengan kurikulum mereka, dan mempersiapkan mereka untuk era AI yang sedang mereka masuki.**

Itulah mengapa buku ini ditulis. Itulah mengapa buku ini perlu ada.

---

**Jakarta, Februari 2026**

**Tri Aji Nugroho, S.T., M.T.**
Dosen Pengampu Mata Kuliah Algoritma dan Pemrograman
Program Studi Informatika, Fakultas Sains dan Teknologi
Universitas Al Azhar Indonesia

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
