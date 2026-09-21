# RENCANA PEMBELAJARAN SEMESTER (RPS)

## UNIVERSITAS AL AZHAR INDONESIA
### Fakultas Sains dan Teknologi — Program Studi Informatika

---

## A. IDENTITAS MATA KULIAH

| Komponen | Detail |
|----------|--------|
| **Nama Mata Kuliah** | Probabilitas dan Statistik |
| **Kode Mata Kuliah** | IF52510033 |
| **Bobot SKS** | 3 SKS |
| **Semester** | 1 (Ganjil) |
| **Tahun Akademik** | 2026/2027 |
| **Kelompok MK** | MKP (Mata Kuliah Inti Prodi — Wajib) |
| **Rumpun Keilmuan** | Matematika & Fondasi Komputasi (R02) |
| **Bahan Kajian** | BK08 — Mathematical and Statistical Foundations |
| **Prasyarat** | — (tidak ada) |
| **Ko-requisite** | — (tidak ada) |
| **Dosen Pengampu** | Tri Aji Nugroho, S.T., M.T. |
| **Kelas** | IF26A, IF26H |
| **Waktu Pertemuan** | 1x per minggu @ 150 menit |
| **Platform** | LMS UAI (utama), Google Colab (komputasi), GitHub (portofolio) |
| **Kurikulum** | Kurikulum Informatika 2025 — Revisi 2026 |

---

## B. DESKRIPSI MATA KULIAH

Probabilitas dan Statistik adalah mata kuliah fondasi yang membekali mahasiswa Informatika dengan cara berpikir di bawah ketidakpastian (*reasoning under uncertainty*). Mata kuliah ini membahas statistika deskriptif, visualisasi data, dasar probabilitas, probabilitas bersyarat dan Teorema Bayes, peubah acak beserta distribusinya, distribusi sampling dan Teorema Limit Pusat, estimasi dan interval kepercayaan, uji hipotesis, ANOVA, uji chi-square, serta korelasi dan pengantar regresi linear.

Yang membedakan mata kuliah ini dari statistika umum adalah **orientasinya pada computing**. Probabilitas bukan sekadar hitungan peluang dadu — ia adalah bahasa yang dipakai untuk menyatakan ketidakpastian dalam sistem komputasi: berapa peluang sebuah paket jaringan hilang, seberapa yakin sebuah model klasifikasi pada prediksinya, apakah perbedaan waktu eksekusi dua algoritma nyata atau kebetulan. Karena itu setiap konsep diperkenalkan melalui persoalan Informatika dan data Indonesia, lalu dihitung dengan Python di Google Colab.

Mata kuliah ini adalah **fondasi wajib bagi seluruh jalur Kecerdasan Artifisial dan Sains Data** pada Kurikulum Informatika 2025. Distribusi probabilitas yang dipelajari di sini akan muncul kembali sebagai asumsi model pada Dasar Kecerdasan Artifisial dan Pembelajaran Mesin; uji hipotesis akan menjadi dasar pembandingan model; dan estimasi akan menjadi dasar pemahaman *confidence* sebuah prediksi. Pada AI Curriculum Infusion Matrix, mata kuliah ini berada pada tahap **F (Foundation)** dengan mode **K (Kontekstual)** — artinya AI hadir sebagai konteks dan alat bantu, bukan sebagai objek pembelajaran tersendiri. Fokusnya tegas: **mahasiswa harus menguasai fondasi ini secara mandiri, justru agar kelak tidak menjadi sekadar pengguna model/API.**

Pendekatan pembelajaran memadukan kuliah konseptual, komputasi statistik dengan Python (NumPy, pandas, matplotlib, seaborn, `scipy.stats`), latihan terbimbing, dan sebuah proyek analisis data akhir. Seluruh contoh menggunakan konteks Indonesia: data BPS, TransJakarta, layanan kesehatan, e-commerce lokal, dan data akademik Prodi Informatika UAI.

---

## C. CAPAIAN PEMBELAJARAN LULUSAN (CPL) YANG DIBEBANKAN

Rumusan CPL diambil dari [registri kurikulum terbaru](../00-kurikulum-if-2025-revisi-2026/03-cpl-prodi.md). Rumusan tidak boleh ditulis ulang di dokumen turunan.

| Kode | Unsur | Deskripsi CPL |
|------|-------|---------------|
| **CPL08** | Keterampilan Khusus | Mampu merancang dan mengembangkan algoritma untuk berbagai keperluan seperti *Intelligent Systems, Information Management, Algorithms and Complexity, Data Science, Human Computer Interaction, Graphics & Visual Computing, Network Security,* dan *Mobile Computing*. |
| **CPL10** | Keterampilan Khusus | Kemampuan merekayasa, membuat pemodelan dan visualisasi data yang tepat untuk kebutuhan organisasi dengan memperhatikan aspek keamanan data. |

---

## D. CAPAIAN PEMBELAJARAN MATA KULIAH (CPMK)

CPMK pada Kurikulum 2025 revisi 2026 adalah **rumusan tingkat prodi** yang melekat pada CPL dan dipakai bersama oleh beberapa mata kuliah. Rumusan tidak boleh diubah pada tingkat RPS.

| Kode | CPL | Level Bloom | Deskripsi CPMK |
|------|-----|-------------|----------------|
| **CPMK081** | CPL08 | C6/P4–P5 | Mampu merancang (C6/P4) dan mengembangkan (C6/P5) algoritma serta metode komputasi dengan memanfaatkan fondasi logika, matematika, probabilitas, dan statistika untuk menyelesaikan permasalahan *computing*. |
| **CPMK102** | CPL10 | C3–C4, P2–P3 | Mampu mengolah (C3/P2), menganalisis (C4), dan memvisualisasikan (C3/P3) data menggunakan metode statistik, komputasi, dan kecerdasan artifisial untuk menghasilkan informasi yang mendukung pengambilan keputusan organisasi. |

> CPMK081 juga diampu oleh Logika Informatika dan Jaringan Syaraf Tiruan dan Pembelajaran Mendalam.
> CPMK102 juga diampu oleh Analisis Data Statistik, Dasar Kecerdasan Artifisial dan Pembelajaran Mesin, Komputer Grafik, Pengolahan Citra, Sains Data, dan Pengolahan Bahasa Alami.

---

## E. SUB-CPMK

Sub-CPMK adalah **pembeda mata kuliah** — tingkat inilah yang menerjemahkan CPMK prodi menjadi capaian khas Probabilitas dan Statistik. Rumusan diambil verbatim dari [pemetaan kurikulum](../00-kurikulum-if-2025-revisi-2026/15b-subcpmk-tingkat-1-semester-1-2.md).

### Sub-CPMK 1 — `PS-Sub-CPMK081-1`

| Aspek | Isi |
|---|---|
| **CPL / CPMK** | CPL08 / CPMK081 |
| **Level Bloom** | C3–C4 |
| **Deskripsi** | Mampu menerapkan (C3) dan menganalisis (C4) konsep probabilitas, peubah acak, distribusi, estimasi, dan inferensi sebagai fondasi perancangan metode komputasi dan pembelajaran mesin. |
| **Materi / Knowledge Unit** | *Probability axioms; random variables; distributions; expectation; sampling; estimation; confidence interval; hypothesis testing.* |
| **Indikator** | 1. Menghitung probabilitas/distribusi pada soal kontekstual; 2. Menganalisis hasil inferensi berikut asumsinya. |
| **Kriteria** | Ketepatan rumus dan hitung; kecocokan asumsi; kualitas interpretasi. |
| **Bobot terhadap nilai akhir** | **45%** — Kuis 15% · Unjuk Kerja 5% · UAS 25% |

### Sub-CPMK 2 — `PS-Sub-CPMK102-1`

| Aspek | Isi |
|---|---|
| **CPL / CPMK** | CPL10 / CPMK102 |
| **Level Bloom** | C3–C4/P2–P3 |
| **Deskripsi** | Mampu mengolah (C3/P2), menganalisis (C4), dan memvisualisasikan (C3/P3) data menggunakan statistika deskriptif dan inferensial untuk menghasilkan kesimpulan yang valid. |
| **Materi / Knowledge Unit** | *Descriptive statistics; sampling; hypothesis testing; correlation; regression introduction; statistical visualization.* |
| **Indikator** | 1. Mengolah sampel dan menghasilkan visual statistik; 2. Menyimpulkan hasil uji secara tepat berdasarkan data. |
| **Kriteria** | Ketepatan prosedur; kesesuaian grafik; validitas interpretasi. |
| **Bobot terhadap nilai akhir** | **55%** — Observasi 25% · Unjuk Kerja 5% · UTS 25% |

---

## F. INDIKATOR CAPAIAN MINGGUAN

Karena Sub-CPMK pada kurikulum baru berjumlah sedikit dan berlaku untuk seluruh semester, capaian mingguan dinyatakan sebagai **indikator** yang menelusuri balik ke salah satu Sub-CPMK. Satu Sub-CPMK dicapai melalui beberapa minggu perkuliahan.

| Minggu | Indikator Capaian Mingguan | Sub-CPMK | Bloom |
|--------|----------------------------|----------|-------|
| 1 | Menjelaskan peran ketidakpastian dalam sistem komputasi, membedakan populasi–sampel, dan mengenali jenis/skala data | PS-Sub-CPMK102-1 | C2 |
| 2 | Menghitung dan menafsirkan ukuran pemusatan, penyebaran, dan posisi pada data nyata | PS-Sub-CPMK102-1 | C3 |
| 3 | Memilih dan membuat visualisasi statistik yang sesuai dengan jenis data dan pertanyaan analisis | PS-Sub-CPMK102-1 | C3 |
| 4 | Menerapkan aksioma probabilitas, aturan penjumlahan/perkalian, dan probabilitas bersyarat | PS-Sub-CPMK081-1 | C3 |
| 5 | Menerapkan Teorema Bayes dan menganalisis kebebasan kejadian pada kasus computing | PS-Sub-CPMK081-1 | C3–C4 |
| 6 | Memodelkan fenomena diskret dengan distribusi Bernoulli, Binomial, Poisson, dan Geometrik | PS-Sub-CPMK081-1 | C3 |
| 7 | Memodelkan fenomena kontinu dengan distribusi Uniform, Eksponensial, dan Normal | PS-Sub-CPMK081-1 | C3 |
| 8 | **UJIAN TENGAH SEMESTER (UTS)** — cakupan Minggu 1–7 | PS-Sub-CPMK102-1 | C2–C4 |
| 9 | Menghitung ekspektasi dan varians, serta menjelaskan distribusi sampling dan Teorema Limit Pusat | PS-Sub-CPMK081-1 | C3–C4 |
| 10 | Menyusun estimasi titik dan interval kepercayaan serta menafsirkan maknanya secara tepat | PS-Sub-CPMK081-1 | C3–C4 |
| 11 | Merumuskan dan menguji hipotesis satu sampel, serta menafsirkan *p-value* dan galat Tipe I/II | PS-Sub-CPMK081-1 | C3–C4 |
| 12 | Menguji hipotesis dua sampel dan uji proporsi, serta memeriksa asumsi yang menyertainya | PS-Sub-CPMK102-1 | C3–C4 |
| 13 | Menerapkan ANOVA satu arah dan uji chi-square, serta menafsirkan hasilnya | PS-Sub-CPMK102-1 | C3–C4 |
| 14 | Menganalisis korelasi dan membangun model regresi linear sederhana beserta diagnostiknya | PS-Sub-CPMK102-1 | C4 |
| 15 | Mempresentasikan proyek analisis data statistik end-to-end dengan kesimpulan yang tervalidasi | PS-Sub-CPMK102-1 | C4 |
| 16 | **UJIAN AKHIR SEMESTER (UAS)** — cakupan komprehensif Minggu 1–15 | PS-Sub-CPMK081-1 | C3–C4 |

---

## G. TABEL RENCANA PEMBELAJARAN SEMESTER

### FASE 1: MEMBACA DATA — "Describe What Happened" (Minggu 1–3)

### Minggu 1: Pengantar Statistika, Data, dan Ketidakpastian dalam Computing

| Aspek | Uraian |
|-------|--------|
| **Materi** | Mengapa insinyur perangkat lunak perlu statistika; populasi vs sampel; jenis data (kualitatif/kuantitatif); skala pengukuran (nominal, ordinal, interval, rasio); statistika deskriptif vs inferensial; pengenalan Google Colab, NumPy, dan pandas |
| **Metode** | Kuliah interaktif, diskusi kasus, demo Colab |
| **Aktivitas Mahasiswa** | Pra-kelas: membaca Bab 1 · Di kelas: diskusi kasus "kapan rata-rata menipu" · Pasca-kelas: Lab 01 |
| **Penilaian** | Observasi (Lab 01) |
| **Estimasi Waktu** | Tatap muka 150' · Tugas terstruktur 180' · Mandiri 180' |
| **Referensi** | Walpole Bab 1; Downey Bab 1 |

### Minggu 2: Statistika Deskriptif — Pemusatan, Penyebaran, dan Posisi

| Aspek | Uraian |
|-------|--------|
| **Materi** | Mean, median, modus dan kapan masing-masing menyesatkan; range, varians, simpangan baku, koefisien variasi; kuartil, persentil, IQR; deteksi pencilan dengan aturan 1,5×IQR; kemencengan dan kurtosis |
| **Metode** | Kuliah, latihan terbimbing, komputasi dengan pandas |
| **Aktivitas Mahasiswa** | Pra-kelas: Bab 2 · Di kelas: menghitung manual lalu memverifikasi dengan pandas · Pasca-kelas: Lab 02 |
| **Penilaian** | Observasi (Lab 02) |
| **Estimasi Waktu** | Tatap muka 150' · Tugas terstruktur 180' · Mandiri 180' |
| **Referensi** | Walpole Bab 1; Bhattacharyya Bab 2 |

### Minggu 3: Visualisasi Data Statistik

| Aspek | Uraian |
|-------|--------|
| **Materi** | Memilih grafik sesuai jenis data dan pertanyaan; histogram dan pemilihan lebar bin; boxplot dan violin plot; scatter plot; bar chart vs pie chart; prinsip kejujuran visual (sumbu, skala, rasio tinta-data); matplotlib dan seaborn |
| **Metode** | Kuliah, studio visualisasi, kritik grafik |
| **Aktivitas Mahasiswa** | Pra-kelas: Bab 3 · Di kelas: kritik grafik menyesatkan dari media · Pasca-kelas: Lab 03 |
| **Penilaian** | Observasi (Lab 03) + Kuis 1 (Minggu 1–3) |
| **Estimasi Waktu** | Tatap muka 150' · Tugas terstruktur 180' · Mandiri 180' |
| **Referensi** | Tufte Bab 2; dokumentasi seaborn |

### FASE 2: MENGUKUR PELUANG — "Reason About Uncertainty" (Minggu 4–7)

### Minggu 4: Dasar Probabilitas

| Aspek | Uraian |
|-------|--------|
| **Materi** | Eksperimen acak, ruang sampel, kejadian; aksioma Kolmogorov; aturan penjumlahan dan komplemen; probabilitas bersyarat; aturan perkalian; kaidah pencacahan (permutasi dan kombinasi) |
| **Metode** | Kuliah, latihan terbimbing, simulasi Monte Carlo sederhana |
| **Aktivitas Mahasiswa** | Pra-kelas: Bab 4 · Di kelas: menurunkan aturan dari aksioma · Pasca-kelas: Lab 04 |
| **Penilaian** | Observasi (Lab 04) |
| **Estimasi Waktu** | Tatap muka 150' · Tugas terstruktur 180' · Mandiri 180' |
| **Referensi** | Walpole Bab 2; Ross Bab 1–3 |

### Minggu 5: Teorema Bayes dan Kebebasan

| Aspek | Uraian |
|-------|--------|
| **Materi** | Hukum probabilitas total; Teorema Bayes; prior, likelihood, posterior; kebebasan dua kejadian; paradoks hasil tes positif (*base rate fallacy*); penerapan pada penyaring spam dan diagnosis |
| **Metode** | Kuliah, studi kasus, simulasi |
| **Aktivitas Mahasiswa** | Pra-kelas: Bab 5 · Di kelas: kasus tes penyakit dengan prevalensi rendah · Pasca-kelas: Lab 05 |
| **Penilaian** | Observasi (Lab 05) + Kuis 2 (Minggu 4–5) |
| **Estimasi Waktu** | Tatap muka 150' · Tugas terstruktur 180' · Mandiri 180' |
| **Referensi** | Walpole Bab 2.7; Downey Bab 5 |

### Minggu 6: Peubah Acak Diskret dan Distribusinya

| Aspek | Uraian |
|-------|--------|
| **Materi** | Peubah acak diskret; fungsi massa probabilitas (PMF) dan fungsi distribusi kumulatif (CDF); distribusi Bernoulli, Binomial, Poisson, dan Geometrik; memilih distribusi yang tepat untuk sebuah fenomena |
| **Metode** | Kuliah, pemodelan kasus, komputasi `scipy.stats` |
| **Aktivitas Mahasiswa** | Pra-kelas: Bab 6 · Di kelas: memodelkan kedatangan permintaan server · Pasca-kelas: Lab 06 |
| **Penilaian** | Observasi (Lab 06) |
| **Estimasi Waktu** | Tatap muka 150' · Tugas terstruktur 180' · Mandiri 180' |
| **Referensi** | Walpole Bab 3, 5; dokumentasi `scipy.stats` |

### Minggu 7: Peubah Acak Kontinu dan Distribusi Normal

| Aspek | Uraian |
|-------|--------|
| **Materi** | Peubah acak kontinu; fungsi densitas probabilitas (PDF); distribusi Uniform dan Eksponensial; distribusi Normal dan sifat-sifatnya; standardisasi dan skor-z; aturan empiris 68–95–99,7; pemeriksaan kenormalan dengan Q-Q plot |
| **Metode** | Kuliah, latihan terbimbing, komputasi |
| **Aktivitas Mahasiswa** | Pra-kelas: Bab 7 · Di kelas: latihan skor-z pada data nilai · Pasca-kelas: Lab 07, persiapan UTS |
| **Penilaian** | Observasi (Lab 07) |
| **Estimasi Waktu** | Tatap muka 150' · Tugas terstruktur 180' · Mandiri 180' |
| **Referensi** | Walpole Bab 4, 6 |

### Minggu 8: UJIAN TENGAH SEMESTER (UTS)

| Aspek | Uraian |
|-------|--------|
| **Cakupan** | Minggu 1–7: statistika deskriptif, visualisasi, probabilitas, Bayes, distribusi diskret dan kontinu |
| **Bentuk** | Tes tulis *closed book*, 100 menit. Kalkulator ilmiah dan satu lembar tabel distribusi diizinkan. **AI tidak diizinkan.** |
| **Bobot** | 25% dari nilai akhir — menelusuri ke PS-Sub-CPMK102-1 |
| **Referensi** | [Kisi-kisi UTS](../05-assessments/kisi-kisi-uts.md) |

### FASE 3: MENARIK KESIMPULAN — "Infer Beyond the Sample" (Minggu 9–13)

### Minggu 9: Ekspektasi, Varians, dan Distribusi Sampling

| Aspek | Uraian |
|-------|--------|
| **Materi** | Ekspektasi dan varians peubah acak; sifat linearitas ekspektasi; distribusi sampling rata-rata; galat baku; Teorema Limit Pusat (CLT) dan mengapa ia menjadi tulang punggung inferensi |
| **Metode** | Kuliah, simulasi CLT, diskusi |
| **Aktivitas Mahasiswa** | Pra-kelas: Bab 8 · Di kelas: simulasi CLT dari distribusi miring · Pasca-kelas: Lab 09 |
| **Penilaian** | Observasi (Lab 09) |
| **Estimasi Waktu** | Tatap muka 150' · Tugas terstruktur 180' · Mandiri 180' |
| **Referensi** | Walpole Bab 4, 8 |

### Minggu 10: Estimasi Titik dan Interval Kepercayaan

| Aspek | Uraian |
|-------|--------|
| **Materi** | Estimator dan sifatnya (tak bias, efisien, konsisten); interval kepercayaan untuk rata-rata (σ diketahui/tidak diketahui); distribusi-t; interval kepercayaan untuk proporsi; penentuan ukuran sampel; **tafsir yang benar** atas "95% kepercayaan" |
| **Metode** | Kuliah, latihan terbimbing, simulasi cakupan interval |
| **Aktivitas Mahasiswa** | Pra-kelas: Bab 9 · Di kelas: simulasi 100 interval kepercayaan · Pasca-kelas: Lab 10 |
| **Penilaian** | Observasi (Lab 10) + Kuis 3 (Minggu 9–10) |
| **Estimasi Waktu** | Tatap muka 150' · Tugas terstruktur 180' · Mandiri 180' |
| **Referensi** | Walpole Bab 9 |

### Minggu 11: Uji Hipotesis Satu Sampel

| Aspek | Uraian |
|-------|--------|
| **Materi** | Hipotesis nol dan alternatif; galat Tipe I dan Tipe II; tingkat signifikansi dan kuasa uji; uji-z dan uji-t satu sampel; uji satu sisi vs dua sisi; ***p-value* dan salah tafsir yang umum**; signifikansi statistik vs signifikansi praktis |
| **Metode** | Kuliah, latihan terbimbing, diskusi etika pelaporan |
| **Aktivitas Mahasiswa** | Pra-kelas: Bab 10 · Di kelas: bedah klaim "terbukti secara statistik" · Pasca-kelas: Lab 11 |
| **Penilaian** | Observasi (Lab 11) |
| **Estimasi Waktu** | Tatap muka 150' · Tugas terstruktur 180' · Mandiri 180' |
| **Referensi** | Walpole Bab 10; pernyataan ASA tentang *p-value* |

### Minggu 12: Uji Hipotesis Dua Sampel dan Uji Proporsi

| Aspek | Uraian |
|-------|--------|
| **Materi** | Uji-t dua sampel bebas; uji-t berpasangan; uji proporsi satu dan dua sampel; pemeriksaan asumsi (kenormalan, homogenitas ragam, kebebasan); uji Levene; alternatif nonparametrik (Mann-Whitney, Wilcoxon) |
| **Metode** | Kuliah, latihan terbimbing, studi kasus A/B testing |
| **Aktivitas Mahasiswa** | Pra-kelas: Bab 11 · Di kelas: merancang A/B test untuk aplikasi kampus · Pasca-kelas: Lab 12 |
| **Penilaian** | Observasi (Lab 12) |
| **Estimasi Waktu** | Tatap muka 150' · Tugas terstruktur 180' · Mandiri 180' |
| **Referensi** | Walpole Bab 10; Kohavi *Trustworthy Online Controlled Experiments* Bab 2 |

### Minggu 13: ANOVA Satu Arah dan Uji Chi-Square

| Aspek | Uraian |
|-------|--------|
| **Materi** | Masalah perbandingan ganda; ANOVA satu arah; tabel ANOVA dan statistik F; uji lanjut Tukey; uji chi-square kesesuaian; uji chi-square kebebasan; ukuran efek (Cramér's V) |
| **Metode** | Kuliah, latihan terbimbing, komputasi |
| **Aktivitas Mahasiswa** | Pra-kelas: Bab 12 · Di kelas: membandingkan tiga metode belajar · Pasca-kelas: Lab 13 |
| **Penilaian** | Observasi (Lab 13) + Kuis 4 (Minggu 11–13) |
| **Estimasi Waktu** | Tatap muka 150' · Tugas terstruktur 180' · Mandiri 180' |
| **Referensi** | Walpole Bab 13, 10.13 |

### FASE 4: MENGHUBUNGKAN DAN MENYIMPULKAN — "Model the Relationship" (Minggu 14–16)

### Minggu 14: Korelasi dan Pengantar Regresi Linear

| Aspek | Uraian |
|-------|--------|
| **Materi** | Kovarians dan korelasi Pearson; korelasi Spearman; **korelasi bukan kausalitas**; regresi linear sederhana; metode kuadrat terkecil; koefisien determinasi R²; pemeriksaan residual; pengantar regresi berganda |
| **Metode** | Kuliah, latihan terbimbing, studi kasus korelasi palsu |
| **Aktivitas Mahasiswa** | Pra-kelas: Bab 13 · Di kelas: bedah kasus korelasi palsu · Pasca-kelas: Lab 14, finalisasi proyek |
| **Penilaian** | Observasi (Lab 14) |
| **Estimasi Waktu** | Tatap muka 150' · Tugas terstruktur 180' · Mandiri 180' |
| **Referensi** | Walpole Bab 11; Bab 13 buku ajar |

### Minggu 15: Presentasi Proyek Analisis Data Statistik

| Aspek | Uraian |
|-------|--------|
| **Materi** | Presentasi proyek kelompok: perumusan pertanyaan, deskripsi data, analisis deskriptif, inferensi, kesimpulan, dan keterbatasan; sesi tanya jawab dan umpan balik sejawat |
| **Metode** | Presentasi, diskusi, *peer review* |
| **Aktivitas Mahasiswa** | Presentasi 15 menit + tanya jawab 5 menit per kelompok |
| **Penilaian** | **Unjuk Kerja 10%** — 5% PS-Sub-CPMK081-1 + 5% PS-Sub-CPMK102-1 |
| **Estimasi Waktu** | Tatap muka 150' · Tugas terstruktur 180' · Mandiri 180' |
| **Referensi** | [Panduan proyek](../05-assessments/project-guidelines.md) |

### Minggu 16: UJIAN AKHIR SEMESTER (UAS)

| Aspek | Uraian |
|-------|--------|
| **Cakupan** | Komprehensif Minggu 1–15, dengan penekanan pada Minggu 9–14 (inferensi, ANOVA, chi-square, korelasi–regresi) |
| **Bentuk** | Tes tulis *closed book*, 120 menit. Kalkulator ilmiah dan satu lembar tabel distribusi diizinkan. **AI tidak diizinkan.** |
| **Bobot** | 25% dari nilai akhir — menelusuri ke PS-Sub-CPMK081-1 |
| **Referensi** | [Kisi-kisi UAS](../05-assessments/kisi-kisi-uas.md) |

---

## H. PETA EVALUASI (ASSESSMENT MAP)

### H.1 Ringkasan Bobot Penilaian

Bobot mengikuti penetapan kurikulum pada sheet `Copy of (Ref) 15` — melekat pada Sub-CPMK, bukan pada komponen nilai bebas.

| Teknik Penilaian | PS-Sub-CPMK081-1 | PS-Sub-CPMK102-1 | Total |
|------------------|------------------|------------------|-------|
| Partisipasi | – | – | **–** |
| Kuis | 15% | – | **15%** |
| Observasi (Praktek/Tugas) | – | 25% | **25%** |
| Unjuk Kerja (Presentasi/Proyek) | 5% | 5% | **10%** |
| Tes Tulis (UTS) | – | 25% | **25%** |
| Tes Tulis (UAS) | 25% | – | **25%** |
| **Total** | **45%** | **55%** | **100%** |

### H.2 Rincian Instrumen

| Teknik | Instrumen | Jumlah | Bobot | Minggu |
|--------|-----------|--------|-------|--------|
| Kuis | Kuis tertulis singkat 20 menit | 4 | 15% (masing-masing 3,75%) | 3, 5, 10, 13 |
| Observasi | Laporan lab Google Colab | 13 | 25% (masing-masing ±1,92%) | 1–7, 9–14 |
| Unjuk Kerja | Proyek analisis data kelompok + presentasi | 1 | 10% | 15 |
| Tes Tulis | UTS | 1 | 25% | 8 |
| Tes Tulis | UAS | 1 | 25% | 16 |

### H.3 Timeline Asesmen

| Minggu | Asesmen | Sub-CPMK | Bobot |
|--------|---------|----------|-------|
| 3 | Kuis 1 — deskriptif & visualisasi | PS-Sub-CPMK081-1 | 3,75% |
| 5 | Kuis 2 — probabilitas & Bayes | PS-Sub-CPMK081-1 | 3,75% |
| 6 | Proposal proyek (tanpa bobot, syarat lanjut) | — | — |
| 8 | **UTS** | PS-Sub-CPMK102-1 | 25% |
| 10 | Kuis 3 — sampling & estimasi | PS-Sub-CPMK081-1 | 3,75% |
| 13 | Kuis 4 — uji hipotesis & ANOVA | PS-Sub-CPMK081-1 | 3,75% |
| 14 | Laporan proyek dikumpulkan | PS-Sub-CPMK081-1 + 102-1 | (dinilai Minggu 15) |
| 15 | **Presentasi proyek** | PS-Sub-CPMK081-1 + 102-1 | 10% |
| 1–7, 9–14 | Laporan lab (13 laporan) | PS-Sub-CPMK102-1 | 25% |
| 16 | **UAS** | PS-Sub-CPMK081-1 | 25% |

---

## I. KONVERSI NILAI

| Rentang Nilai Akhir | Huruf | Bobot | Kategori |
|---------------------|-------|-------|----------|
| 85,00 – 100 | A | 4,00 | Sangat Baik |
| 80,00 – 84,99 | A− | 3,70 | Sangat Baik |
| 75,00 – 79,99 | B+ | 3,30 | Baik |
| 70,00 – 74,99 | B | 3,00 | Baik |
| 65,00 – 69,99 | B− | 2,70 | Cukup Baik |
| 60,00 – 64,99 | C+ | 2,30 | Cukup |
| 55,00 – 59,99 | C | 2,00 | Cukup |
| 45,00 – 54,99 | D | 1,00 | Kurang |
| 0 – 44,99 | E | 0,00 | Gagal |

**Syarat kelulusan mata kuliah:** nilai akhir minimal **C (55,00)** dan kehadiran minimal **75%**.

---

## J. REFERENSI

### Referensi Utama

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.). Pearson.
2. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.). Wiley.
3. Downey, A. B. (2014). *Think Stats: Exploratory Data Analysis in Python* (2nd ed.). O'Reilly Media.

### Referensi Pendukung

4. Ross, S. M. (2019). *A First Course in Probability* (10th ed.). Pearson.
5. Bhattacharyya, G. K., & Johnson, R. A. (2019). *Statistics: Principles and Methods* (8th ed.). Wiley.
6. Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press.
7. Kohavi, R., Tang, D., & Xu, Y. (2020). *Trustworthy Online Controlled Experiments*. Cambridge University Press.

### Referensi Online

8. Badan Pusat Statistik Republik Indonesia — <https://www.bps.go.id>
9. Portal Satu Data Indonesia — <https://data.go.id>
10. Dokumentasi SciPy `scipy.stats` — <https://docs.scipy.org/doc/scipy/reference/stats.html>
11. Dokumentasi seaborn — <https://seaborn.pydata.org>
12. Wasserstein, R. L., & Lazar, N. A. (2016). The ASA Statement on p-Values. *The American Statistician*, 70(2), 129–133.

---

## K. KEBIJAKAN KHUSUS MATA KULIAH

### K.1 Kebijakan Penggunaan AI

Pada AI Curriculum Infusion Matrix, mata kuliah ini berstatus **tahap F (Foundation), mode K (Kontekstual)**. Artinya: **tidak ada Sub-CPMK AI tersendiri**, dan AI **bukan** objek pembelajaran. AI diperlakukan sebagai alat bantu belajar dengan batas yang tegas.

| Kegiatan | Status AI | Ketentuan |
|----------|-----------|-----------|
| Memahami konsep, mencari penjelasan alternatif | **Diizinkan** | Bebas digunakan untuk belajar |
| Memeriksa kembali hasil hitungan yang sudah dikerjakan sendiri | **Diizinkan** | Hitungan manual harus dikerjakan lebih dulu |
| Membantu menulis/memperbaiki kode visualisasi | **Diizinkan dengan catatan** | Wajib dicantumkan di AI Usage Log; mahasiswa harus bisa menjelaskan tiap baris |
| Mengerjakan soal latihan atau kuis | **Tidak diizinkan** | Melanggar amanah akademik |
| UTS dan UAS | **Tidak diizinkan** | Ujian bersifat *closed book* |
| Menentukan uji statistik dan menafsirkan hasil pada proyek | **Tidak diizinkan sebagai penentu** | Keputusan dan tafsir harus berasal dari mahasiswa; AI boleh dipakai untuk memeriksa, bukan memutuskan |

**AI Usage Log wajib dilampirkan** pada setiap laporan lab dan laporan proyek. Format tersedia pada [kerangka asesmen](../05-assessments/assessment-framework.md).

> **Mengapa dibatasi seketat ini.** Mata kuliah ini adalah fondasi jalur AI dan Sains Data Prodi Informatika UAI. Mahasiswa yang menyerahkan penalaran probabilistik kepada AI sejak semester 1 akan kehilangan kemampuan menilai apakah keluaran sebuah model masuk akal — persis kemampuan yang paling dibutuhkan ketika kelak bekerja dengan model AI. Pembatasan ini bukan ketidakpercayaan pada teknologi, melainkan investasi pada kemandirian intelektual.

### K.2 Kebijakan Kehadiran

- Kehadiran minimal **75%** (12 dari 16 pertemuan) sebagai syarat mengikuti UAS.
- Ketidakhadiran karena sakit atau tugas institusi wajib disertai surat keterangan paling lambat 7 hari.
- Keterlambatan lebih dari 20 menit dicatat sebagai tidak hadir, kecuali dengan alasan yang dapat diterima.

### K.3 Kebijakan Keterlambatan Tugas

| Keterlambatan | Pengurangan Nilai |
|---------------|-------------------|
| ≤ 24 jam | −10% |
| 24–48 jam | −25% |
| 48–72 jam | −50% |
| > 72 jam | Tidak dinilai (nilai 0) |

Perpanjangan hanya diberikan atas alasan medis atau kedaruratan keluarga dengan bukti pendukung.

### K.4 Kebijakan Integritas Akademik (Amanah)

Integritas akademik dalam mata kuliah ini berpijak pada nilai **amanah** — apa yang dituliskan mahasiswa dalam laporan adalah kesaksian atas pekerjaannya sendiri.

Perbuatan berikut tergolong pelanggaran:

1. Menyalin pekerjaan mahasiswa lain, seluruhnya maupun sebagian.
2. Memakai keluaran AI tanpa mencantumkannya pada AI Usage Log.
3. **Memanipulasi atau mengarang data** agar hasil uji menjadi signifikan.
4. Melaporkan hasil uji yang tidak benar-benar dijalankan.
5. Membawa alat bantu terlarang ke dalam ujian.

Sanksi berjenjang: teguran tertulis → nilai nol pada instrumen terkait → nilai E untuk mata kuliah → pelaporan ke Program Studi.

> **Catatan khusus statistika.** Butir 3 dan 4 adalah pelanggaran yang paling khas — dan paling berbahaya — pada mata kuliah ini. Hasil yang "tidak signifikan" adalah temuan yang sah dan **tidak mengurangi nilai**. Yang dinilai adalah ketepatan prosedur dan kejujuran interpretasi, bukan apakah hipotesis mahasiswa terbukti.

---

## L. PROFIL PROYEK AKHIR

### Deskripsi Singkat

Mahasiswa bekerja dalam kelompok 3–4 orang untuk melakukan **analisis data statistik end-to-end** atas sebuah persoalan nyata berkonteks Indonesia: merumuskan pertanyaan, memperoleh dan membersihkan data, melakukan analisis deskriptif dan visualisasi, menjalankan inferensi yang sesuai, lalu menarik kesimpulan beserta keterbatasannya.

### Luaran

| Luaran | Bentuk | Minggu |
|--------|--------|--------|
| Proposal | 2 halaman: pertanyaan penelitian, sumber data, rencana analisis | 6 |
| Notebook analisis | Google Colab yang dapat dijalankan ulang | 14 |
| Laporan | 8–12 halaman dengan AI Usage Log | 14 |
| Presentasi | 15 menit + tanya jawab 5 menit | 15 |

### Bobot dan Penelusuran

Proyek bernilai **10%** dari nilai akhir melalui teknik Unjuk Kerja, terbagi rata: 5% menelusuri ke `PS-Sub-CPMK081-1` (ketepatan inferensi dan asumsi) dan 5% ke `PS-Sub-CPMK102-1` (pengolahan, visualisasi, dan interpretasi).

Rincian lengkap pada [panduan proyek](../05-assessments/project-guidelines.md).

---

## M. KETERKAITAN DENGAN MATA KULIAH LAIN

| Mata Kuliah | Hubungan | Keterangan |
|-------------|----------|------------|
| Analisis Data Statistik (IF52520025, Sem 2) | **Lanjutan langsung** | Mendalami regresi berganda, data kategorikal, dan analisis multivariat; juga mengampu CPMK102 |
| Matematika Diskrit (IF52520003, Sem 2) | Pelengkap | Kaidah pencacahan dan struktur diskret |
| Sains Data (IF52520026, Sem 4) | Penerus | Memakai inferensi sebagai dasar pemodelan data |
| Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (IF52510031, Sem 5) | **Penerus utama** | Distribusi, estimasi, dan evaluasi statistik menjadi fondasi pemodelan ML |
| Jaringan Syaraf Tiruan dan Pembelajaran Mendalam (IF52510032, Sem 5) | Penerus | Mengampu CPMK081 yang sama pada tingkat lanjut |
| Metodologi Penelitian (IF52510021, Sem 7) | Penerus | Uji hipotesis sebagai dasar validasi temuan penelitian |

---

## N. PENGESAHAN

| Peran | Nama | Tanda Tangan | Tanggal |
|-------|------|--------------|---------|
| Dosen Pengampu | Tri Aji Nugroho, S.T., M.T. | | |
| Koordinator Rumpun Matematika & Fondasi Komputasi | Riri Safitri, S.Si., M.T. | | |
| Ketua Program Studi Informatika | | | |

Jakarta, Agustus 2026

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
