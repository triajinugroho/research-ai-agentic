# ANALISIS STRATEGIS MATA KULIAH
## Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (IF52510031)

**Program Studi Informatika — Universitas Al Azhar Indonesia**
**Semester Ganjil 2026/2027 · 3 SKS · Semester 5**
**Penyusun:** Tri Aji Nugroho, S.T., M.T.

---

## 1. POSISI STRATEGIS MATA KULIAH

### 1.1 Mengapa Mata Kuliah Ini Berbeda dari Mata Kuliah Lain

Visi Program Studi Informatika UAI 2025 menyebut tiga domain keilmuan: **Software Engineering**, **Data Science**, dan **Artificial Intelligence**. Mata kuliah ini adalah **satu-satunya mata kuliah wajib** yang secara langsung mewujudkan domain ketiga bagi seluruh mahasiswa.

Pada AI Curriculum Infusion Matrix, statusnya:

| Dimensi | Nilai | Maknanya |
|---------|-------|----------|
| Tahap | **U→A→C** | Menjembatani *Understand* → *Apply* → *Create* dalam satu semester |
| Mode | **Core** | AI adalah objek utama pembelajaran, bukan konteks contoh |
| Pilar | **AI Core** | Batu penjuru jalur AI Core & Advanced |
| Peran | **Fondasi wajib AI seluruh mahasiswa** | Bukan peminatan |

Dari 58 mata kuliah dalam kurikulum, hanya sebagian kecil berstatus **Core**. Mata kuliah inilah tempat mahasiswa pertama kali membangun model AI sendiri — dan satu-satunya kesempatan wajib untuk melakukannya bagi mahasiswa yang tidak mengambil peminatan AI.

### 1.2 Peran sebagai Simpul Prasyarat

```
DIBUTUHKAN OLEH                           MEMBUTUHKAN
──────────────────────────                ─────────────────────────
Jaringan Syaraf Tiruan &      ◄──┐   ┌──► Probabilitas dan Statistik
Pembelajaran Mendalam            │   │    (sem 1) — distribusi, Bayes,
                                 │   │    inferensi, evaluasi
Sains Data                    ◄──┤   │
                                 │   ├──► Struktur Data dan Algoritma
Pengolahan Bahasa Alami       ◄──┤   │    (sem 3) — kompleksitas,
                                 │   │    struktur representasi
Pengolahan Citra              ◄──┤   │
                                 │   ├──► Basis Data (sem 4) —
Web Semantik                  ◄──┤   │    pengambilan dan penggabungan
                                 │   │    data
Tugas Akhir (jalur AI)        ◄──┘   └──► Pemrograman (sem 1–2) — Python
```

Lima mata kuliah lanjutan bergantung padanya. Kelemahan pada mata kuliah ini **berlipat** ke seluruh jalur AI.

### 1.3 Relasi dengan Mata Kuliah Sejenis dalam Kurikulum

| Mata kuliah | Kode | Sem | Beda fokus |
|-------------|------|-----|-----------|
| **Dasar AI dan Pembelajaran Mesin** | IF52510031 | 5 | **Keluasan** — seluruh alur ML klasik, dari formulasi sampai evaluasi |
| Jaringan Syaraf Tiruan dan Pembelajaran Mendalam | IF52510032 | 5 | **Kedalaman** — arsitektur *deep learning* |
| Sains Data | — | 6 | **Skala dan alur data** — *pipeline*, *big data* |
| Pengolahan Bahasa Alami | IF52510024 | 7 | **Domain teks** |
| Pengolahan Citra | IF52510016 | 6 | **Domain citra** |

Pembagian ini menuntut disiplin: mata kuliah ini **tidak** mendalami *deep learning* (itu porsi IF52510032), dan **tidak** membahas NLP atau *computer vision* sebagai domain (itu porsi semester 6–7). Minggu 13 hanya memberi pengantar JST secukupnya untuk menjembatani.

> **Risiko yang paling nyata:** tergoda mengajarkan semuanya. Materi *deep learning*, NLP, dan CV dari kerangka kurikulum sebelumnya **harus dilepaskan** agar keluasan alur ML klasik tercakup tuntas.

---

## 2. ANALISIS SWOT

### 2.1 Kekuatan (*Strengths*)

| # | Kekuatan | Dampak |
|---|----------|--------|
| S1 | Status **Core** pada AI Infusion Matrix memberi mandat kurikulum yang jelas | Tidak perlu memperebutkan legitimasi materi AI |
| S2 | Prasyarat statistik sudah dipenuhi di semester 1 | Dapat langsung masuk ke konsep evaluasi tanpa mengulang dasar |
| S3 | Bobot Unjuk Kerja 35% memungkinkan pembelajaran berbasis proyek | Mahasiswa membangun portofolio nyata |
| S4 | Ekosistem `scikit-learn` matang, gratis, dan berjalan di Colab | Tanpa hambatan infrastruktur |
| S5 | Ketersediaan dataset Indonesia terbuka meningkat pesat | Kasus relevan dan bermakna |
| S6 | Dua Sub-CPMK mencakup **membangun** (082) dan **mengevaluasi** (102) secara seimbang | Mencegah lulusan yang bisa melatih model tetapi tidak bisa menilainya |
| S7 | Nilai Islami (amanah, keadilan) memiliki kaitan langsung dengan isu *bias* dan *fairness* | Integrasi nilai menjadi alami, bukan tempelan |

### 2.2 Kelemahan (*Weaknesses*)

| # | Kelemahan | Mitigasi |
|---|-----------|----------|
| W1 | 3 SKS untuk cakupan yang sangat luas | Disiplin pada batas cakupan (§1.3); materi lanjut diarahkan ke MK lain |
| W2 | Tidak ada mata kuliah praktikum pendamping | Praktikum diintegrasikan dalam jam kuliah; 13 modul lab mandiri |
| W3 | Kesenjangan kemampuan Python antarmahasiswa | Lab 1 sebagai penyamaan; modul rujukan mandiri |
| W4 | Statistik semester 1 sering sudah terlupa di semester 5 | Bab 4 dan 7 memuat pengulangan terarah |
| W5 | Partisipasi berbobot 0% dapat menurunkan kehadiran | Nilai bergantung pada karya yang dikerjakan di kelas |
| W6 | Waktu komputasi terbatas di Colab gratis | Dataset dibatasi ukurannya; model klasik, bukan *deep* |

### 2.3 Peluang (*Opportunities*)

| # | Peluang | Pemanfaatan |
|---|---------|-------------|
| O1 | Permintaan tenaga AI/ML di Indonesia tumbuh pesat | Proyek diarahkan menjadi portofolio yang dapat ditunjukkan |
| O2 | Satu Data Indonesia dan portal data daerah terus berkembang | Kasus nyata berkonteks lokal |
| O3 | Isu AI bertanggung jawab menjadi perhatian regulator global dan nasional | Materi *fairness* menjadi pembeda lulusan |
| O4 | Kolaborasi dengan mata kuliah Teknopreneur (semester yang sama) | Proyek dapat diarahkan ke validasi masalah nyata |
| O5 | Model praterlatih dan *AutoML* memudahkan eksperimen | Waktu bergeser dari implementasi ke penalaran |
| O6 | Kebutuhan industri akan orang yang dapat **mengevaluasi** model AI | Sub-CPMK102-1 tepat menjawabnya |

### 2.4 Ancaman (*Threats*)

| # | Ancaman | Penanganan |
|---|---------|------------|
| T1 | **AI generatif dapat menghasilkan seluruh kode ML** | Asesmen digeser ke penalaran: mengapa model ini, mengapa metrik ini |
| T2 | Mahasiswa menjadi pengguna API tanpa memahami dasarnya | Perhitungan manual wajib pada UTS/UAS; implementasi dari nol pada beberapa lab |
| T3 | Kecepatan perubahan teknologi membuat materi cepat usang | Menekankan prinsip yang stabil (bias-varians, evaluasi), bukan versi pustaka |
| T4 | Kursus daring gratis yang tampak lebih menarik | Pembeda: umpan balik personal, kasus lokal, dan penekanan tanggung jawab |
| T5 | Ilusi kompetensi — merasa mahir karena model berjalan | Penekanan pada *error analysis* dan keterbatasan model |
| T6 | *Leakage* dan *overfitting* yang tidak disadari menghasilkan hasil palsu | Minggu 4 dikhususkan untuk ini; pengurangan nilai bila terjadi di proyek |

---

## 3. ANALISIS LIMA KEKUATAN PORTER (ADAPTASI PENDIDIKAN)

### 3.1 Ancaman Pendatang Baru — **Tinggi**

Kursus AI/ML daring bermunculan setiap bulan, banyak yang gratis dan dibuat oleh praktisi ternama.

**Respons:** yang tidak dapat ditiru kursus daring adalah (a) umpan balik atas pekerjaan mahasiswa secara personal, (b) konteks masalah Indonesia, (c) pertanggungjawaban lisan di depan penguji, dan (d) integrasi nilai etika yang diuji, bukan sekadar disebut.

### 3.2 Daya Tawar "Pemasok" (Materi dan Perangkat) — **Rendah**

`scikit-learn`, `pandas`, Colab, dan dataset terbuka seluruhnya gratis dan berlisensi permisif. Tidak ada ketergantungan pada vendor.

**Catatan risiko:** ketergantungan pada Google Colab adalah satu-satunya titik lemah. Mitigasi: seluruh notebook dirancang agar juga berjalan di lingkungan lokal dengan `pip install -r requirements.txt`.

### 3.3 Daya Tawar "Pembeli" (Mahasiswa dan Industri) — **Tinggi**

Mahasiswa semester 5 sudah mampu membandingkan mutu pengajaran, dan industri memiliki ekspektasi yang jelas terhadap lulusan yang mengaku menguasai ML.

**Respons:** capaian mata kuliah dinyatakan dalam bentuk yang dapat diperiksa — sebuah repositori proyek yang dapat dijalankan ulang, dengan *model card* dan analisis keterbatasan.

### 3.4 Ancaman Produk Substitusi — **Sedang-Tinggi**

*AutoML*, layanan AI siap pakai, dan asisten AI dapat menghasilkan model tanpa memahami dasarnya.

**Respons:** justru menjadikannya materi. Minggu 2 membahas **kapan tidak perlu ML**, dan Minggu 14 membahas apa yang tidak dapat digantikan alat otomatis: penilaian atas kelayakan data, keadilan model, dan tanggung jawab atas keputusan.

### 3.5 Persaingan Antarmata Kuliah — **Sedang**

Di semester 5 mahasiswa juga mengambil Jaringan Syaraf Tiruan, Teknopreneur, dan mata kuliah lain dengan beban proyek.

**Respons:** jadwal proyek dirancang bertahap sejak Minggu 5 agar tidak menumpuk di akhir; dan proyek diizinkan berbagi tema dengan Teknopreneur selama luaran keduanya berbeda dan dinyatakan terbuka.

---

## 4. ANALISIS TREN: AI DI TAHUN 2026

### 4.1 Lima Pergeseran yang Memengaruhi Isi Mata Kuliah

| Tren | Implikasi bagi mata kuliah |
|------|----------------------------|
| **Model besar menjadi komoditas** | Nilai bergeser dari "bisa melatih model" ke "bisa menilai apakah model layak dipakai" → penguatan Sub-CPMK102-1 |
| **Regulasi AI menguat** (EU AI Act, pedoman nasional) | Dokumentasi model (*model card*), telusur data, dan analisis dampak menjadi keterampilan wajib → Minggu 14 |
| **ML klasik tetap dominan pada data tabular** | Pohon keputusan dan *gradient boosting* tetap relevan industri → porsi Minggu 9–10 dipertahankan |
| **Perhatian pada kualitas data melampaui perhatian pada model** (*data-centric AI*) | Minggu 3–5 (prapemrosesan, kebocoran, rekayasa fitur) diberi porsi tiga minggu penuh |
| **AI generatif sebagai alat kerja sehari-hari** | Dibahas terbuka sebagai alat, dengan batas yang tegas → kebijakan AI pada RPS §K |

### 4.2 Apa yang Tidak Berubah

Di tengah perubahan cepat, empat hal berikut tetap menjadi inti dan karena itu menjadi tulang punggung asesmen tertulis:

1. **Tukar-tambah bias dan varians** — dasar seluruh pemilihan model.
2. **Kebocoran data** — penyebab tunggal terbanyak hasil yang tampak bagus tetapi palsu.
3. **Metrik harus sesuai masalah** — akurasi pada data tak seimbang tetap menyesatkan seperti sepuluh tahun lalu.
4. **Korelasi bukan sebab-akibat** — berlaku sama pada model sesederhana regresi maupun sekompleks transformer.

Keempatnya dapat diuji tanpa komputer, dan karena itu menjadi inti UTS dan UAS.

### 4.3 Posisi terhadap AI Generatif

Mata kuliah ini **tidak melarang** AI generatif dan juga **tidak memujanya**. Kebijakannya:

| Kegiatan | Status |
|----------|--------|
| Menulis kode `scikit-learn` rutin | **Boleh**, dengan pencatatan |
| Menjelaskan galat dan dokumentasi | **Boleh** |
| Memilih model dan metrik | **Tidak boleh** — ini yang dinilai |
| Menafsirkan hasil evaluasi | **Tidak boleh** — ini yang dinilai |
| Menulis analisis keterbatasan dan *model card* | **Tidak boleh** — ini yang dinilai |
| Selama UTS dan UAS | **Tidak boleh sama sekali** |

Alasannya bukan kekhawatiran akan kecurangan, melainkan bahwa ketiga hal di kolom "tidak boleh" **justru merupakan Sub-CPMK mata kuliah ini**.

---

## 5. STRATEGI PEMBELAJARAN

### 5.1 Tiga Prinsip

**(1) Data lebih dahulu, model kemudian.**
Tiga minggu penuh (3–5) dihabiskan untuk data sebelum satu model pun dilatih. Ini kebalikan dari kebanyakan kursus daring, dan disengaja: kegagalan proyek ML di lapangan jauh lebih sering disebabkan data daripada model.

**(2) Evaluasi sejajar dengan pembangunan.**
Setiap model yang diperkenalkan langsung disertai metrik dan cara menafsirkannya. Tidak ada minggu "belajar model" yang terpisah dari "belajar mengevaluasi".

**(3) Setiap klaim harus dapat dipertanggungjawabkan.**
Angka akurasi tanpa *baseline*, tanpa interval, dan tanpa analisis kesalahan tidak diterima — pada lab maupun proyek.

### 5.2 Rancangan Pertemuan (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 15' | Tinjauan singkat; kaitan dengan minggu sebelumnya |
| Konsep | 45' | Penjelasan dengan turunan dan contoh manual |
| Demonstrasi | 30' | Implementasi langsung di Colab, termasuk kegagalannya |
| Praktik terbimbing | 45' | Mahasiswa mengerjakan lab; dosen berkeliling |
| Penutup | 15' | Rangkuman; kesalahan umum yang ditemui; tugas |

### 5.3 Strategi Proyek

Proyek dikerjakan bertahap sejak Minggu 5, bukan menumpuk di akhir:

| Minggu | Tahap | Bobot dalam proyek |
|--------|-------|--------------------|
| 5 | Pemilihan masalah dan data; proposal | Prasyarat |
| 7 | *Baseline* dan evaluasi awal | 5% |
| 11 | Iterasi model dan analisis kesalahan | 5% |
| 14 | Laporan, notebook, *model card* | 15% |
| 15 | Presentasi dan tanya jawab | 10% |

Pembagian ini membuat kegagalan terdeteksi lebih awal dan memberi ruang perbaikan.

### 5.4 Integrasi Nilai Islami

Berbeda dengan mata kuliah lain, kaitannya di sini sangat langsung:

| Nilai | Wujud dalam mata kuliah |
|-------|-------------------------|
| **Amanah** | Melaporkan kinerja model apa adanya, termasuk kegagalannya; mencatat bantuan AI |
| **Adil** (`al-'adl`) | Analisis *fairness*: apakah model bekerja sama baiknya untuk semua kelompok? |
| **Tidak berbuat kerusakan** (`la darar`) | Analisis dampak: siapa yang dirugikan bila model salah? |
| **Tanggung jawab** (`mas'uliyyah`) | Keputusan tetap milik manusia; model adalah alat |
| **Ilmu yang bermanfaat** | Proyek diarahkan ke masalah nyata masyarakat Indonesia |

Nilai **adil** memperoleh tempat khusus: Minggu 14 membahas bagaimana model yang akurat secara keseluruhan dapat sistematis merugikan kelompok tertentu — dan mengapa ini bukan sekadar persoalan teknis.

---

## 6. RISIKO PELAKSANAAN DAN MITIGASI

| Risiko | Kemungkinan | Dampak | Mitigasi |
|--------|-------------|--------|----------|
| Cakupan terlalu luas untuk 3 SKS | Tinggi | Tinggi | Batas cakupan §1.3 ditegakkan; materi lanjut dirujuk ke MK lain |
| Mahasiswa tertinggal pada Python | Sedang | Sedang | Lab 1 sebagai penyamaan; materi rujukan mandiri |
| Proyek menumpuk di akhir semester | Tinggi | Tinggi | Lima tahap bertenggat (§5.3) |
| Kode proyek dihasilkan AI tanpa pemahaman | Tinggi | Tinggi | Tanya jawab lisan Minggu 15; AI Usage Log wajib |
| Kebocoran data tidak disadari di proyek | Sedang | Tinggi | Minggu 4 khusus; daftar periksa wajib sebelum pengumpulan |
| Colab tidak dapat diakses saat praktikum | Rendah | Sedang | Notebook dapat dijalankan lokal; berkas cadangan disiapkan |
| Dataset proyek ternyata tidak layak | Sedang | Sedang | Persetujuan proposal Minggu 5 mensyaratkan data sudah diunduh dan dibuka |

---

## 7. RENCANA PENINGKATAN BERKELANJUTAN

| Siklus | Kegiatan |
|--------|----------|
| Tengah semester | Survei singkat setelah UTS; penyesuaian kecepatan materi |
| Akhir semester | Analisis capaian per Sub-CPMK; identifikasi indikator dengan capaian terendah |
| Antarsemester | Pembaruan dataset dan versi pustaka; penyesuaian materi tren |
| Dua tahunan | Peninjauan cakupan terhadap perkembangan kurikulum ACM/IEEE dan kebutuhan industri |

### Indikator Keberhasilan

| Indikator | Target |
|-----------|--------|
| Mahasiswa mencapai Sub-CPMK082-1 (skor ≥ 3 dari 4) | ≥ 75% |
| Mahasiswa mencapai Sub-CPMK102-1 (skor ≥ 3 dari 4) | ≥ 75% |
| Proyek dengan notebook yang dapat dijalankan ulang | 100% |
| Proyek dengan *model card* lengkap | 100% |
| Proyek tanpa kebocoran data | ≥ 90% |
| Mahasiswa melanjutkan ke MK jalur AI | ≥ 40% |

---

## 8. SIMPULAN STRATEGIS

Mata kuliah ini berdiri pada titik yang tidak biasa: ia adalah **satu-satunya kesempatan wajib** bagi setiap mahasiswa Informatika UAI untuk membangun model AI sendiri, sekaligus **prasyarat bagi lima mata kuliah lanjutan**, dalam bobot hanya 3 SKS.

Ketegangan antara keluasan cakupan dan keterbatasan waktu adalah persoalan strategis utamanya. Jalan keluarnya bukan memadatkan lebih banyak materi, melainkan memilih dengan tegas apa yang **tidak** diajarkan — dan menyerahkannya kepada mata kuliah yang memang dirancang untuk itu.

Yang menjadi pembeda lulusan mata kuliah ini bukan banyaknya algoritma yang dikenal. Di tahun 2026, daftar algoritma dapat diperoleh siapa saja dalam hitungan detik. Pembedanya adalah tiga kemampuan yang tidak dapat diambil alih alat:

1. **Menilai apakah sebuah masalah layak diselesaikan dengan ML** — dan berani mengatakan tidak.
2. **Mengevaluasi model dengan metrik yang tepat** — dan mengenali hasil yang terlalu bagus untuk benar.
3. **Mempertanggungjawabkan dampak model** — termasuk kepada kelompok yang tidak terwakili dalam data.

Ketiganya adalah wujud **amanah** dalam bidang yang, lebih daripada bidang lain dalam informatika, keputusannya menyentuh hidup orang banyak.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
