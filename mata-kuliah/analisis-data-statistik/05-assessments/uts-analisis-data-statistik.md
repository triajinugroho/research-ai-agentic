---
mata_kuliah: Analisis Data Statistik
kode_mk: IF2XXX
sks: 2 SKS (Teori + Praktikum Terintegrasi)
semester: Genap 2025/2026
jenis: UTS
---

# UJIAN TENGAH SEMESTER (UTS)
## Semester Genap Tahun Akademik 2025/2026

**UNIVERSITAS AL AZHAR INDONESIA**
**Fakultas Sains dan Teknologi — Program Studi Informatika**

> *"Bacalah dengan (menyebut) nama Tuhanmu yang menciptakan."*
> — **QS Al-'Alaq: 1**

| Field             | Nilai                                                               |
|-------------------|---------------------------------------------------------------------|
| Mata Kuliah       | Analisis Data Statistik                                             |
| Kode MK / SKS     | IF2XXX / 2 SKS (Teori + Praktikum Terintegrasi)                     |
| Dosen             | Tri Aji Nugroho, S.T., M.T.                                         |
| Kelas             | [......]                                                            |
| Hari/Tanggal      | [......]                                                            |
| Waktu             | 120 menit                                                           |
| Sifat Ujian       | Closed-book — boleh kalkulator ilmiah & tabel distribusi (z, t, chi-square) |

---

## PETUNJUK PENGERJAAN

1. Bacalah **Basmalah** sebelum memulai ujian.
2. Tuliskan Nama, NIM, dan Kelas di lembar jawaban.
3. Kerjakan dengan jujur, mandiri, dan bertanggung jawab sesuai nilai integritas akademik dan etika Islami.
4. Dilarang menggunakan AI tools (ChatGPT, Copilot, dll.), kecuali dinyatakan lain pada sifat ujian.
5. **Pilihan Ganda:** tulis huruf jawaban (A/B/C/D/E) di lembar jawaban. **Esai:** jelaskan langkah analisis dan argumentasi. **Hitung/Interpretasi:** tunjukkan rumus, substitusi angka, hasil bertahap, lalu interpretasi kalimat. Bawa kalkulator ilmiah; tabel distribusi (z, t, chi-square) ringkas disediakan di halaman akhir soal ini.
6. Periksa kembali jawaban sebelum dikumpulkan.
7. Akhiri dengan **Hamdalah**.

> *"Sesungguhnya amal-amal itu tergantung pada niatnya."*
> — **HR. Bukhari-Muslim**

---

**Bobot Penilaian:**

| Bagian                          | Jumlah Soal | Poin per Soal | Total   |
|---------------------------------|-------------|---------------|---------|
| I. Pilihan Ganda                | 15          | 2             | 30      |
| II. Esai                        | 3           | 10            | 30      |
| III. Hitung / Interpretasi      | 3           | 13-14         | 40      |
| **Total**                       | **21**      | —             | **100** |

---

## BAGIAN I — PILIHAN GANDA (30 poin)

> **Sub-CPMK 1.1** — Menjelaskan peran statistika di era data science dan AI
> *Level Bloom:* C2 · *Konteks:* Umum

**1.** Manakah pernyataan berikut yang **paling tepat** menggambarkan peran statistika dalam era *data science* dan AI?

A. Statistika hanya dipakai untuk menghitung rata-rata pada laporan keuangan.
B. Statistika adalah fondasi inferensi dari data ke pengetahuan — mulai dari eksplorasi, estimasi, hingga pengambilan keputusan di bawah ketidakpastian.
C. Statistika sepenuhnya digantikan oleh *deep learning* karena *machine learning* tidak memerlukan asumsi distribusi.
D. Statistika hanya relevan bila ukuran data kurang dari 30 observasi.
E. Statistika hanya berperan pada tahap visualisasi data.

---

> **Sub-CPMK 1.3** — Menjelaskan prinsip etika data dan responsible AI
> *Level Bloom:* C2 · *Konteks:* Islami (amanah data)

**2.** Seorang peneliti menggunakan data profil jamaah sebuah masjid (nama, NIK, nomor HP) yang diperoleh dari panitia zakat tanpa meminta persetujuan jamaah, kemudian menjual data tersebut ke sebuah *startup* pemasaran. Prinsip etika data dan *responsible AI* manakah yang **paling jelas** dilanggar?

A. *Informed consent* (persetujuan sadar) dan *purpose limitation* (pembatasan tujuan pemakaian data).
B. *Reproducibility* (keterulangan hasil analisis).
C. *Scalability* (kemampuan sistem menangani beban besar).
D. *Latency* (waktu respons sistem).
E. *Interpretability* saja, tanpa pelanggaran privasi.

---

> **Sub-CPMK 2.1** — Menghitung dan menginterpretasi ukuran pemusatan dan penyebaran data
> *Level Bloom:* C3 · *Konteks:* Indonesia (UMP 34 provinsi)

**3.** Data Upah Minimum Provinsi (UMP) 34 provinsi Indonesia memiliki sebaran yang sangat *right-skewed* — DKI Jakarta jauh di atas mayoritas provinsi lain. Ukuran pemusatan (central tendency) yang **paling representatif** untuk menggambarkan UMP "tipikal" provinsi di Indonesia adalah...

A. Mean (rata-rata aritmatika).
B. Median.
C. Modus.
D. Range.
E. Varians.

---

> **Sub-CPMK 2.1** — Menghitung dan menginterpretasi ukuran pemusatan dan penyebaran data
> *Level Bloom:* C3 · *Konteks:* JTBD (variasi nilai ujian pribadi)

**4.** Selama satu semester, Anda mencatat 8 nilai kuis mingguan pribadi Anda. Rata-rata = 82 dengan standar deviasi 3. Teman Anda mencatat dengan rata-rata sama (82) tetapi standar deviasi 12. Interpretasi yang **paling tepat**:

A. Nilai Anda dan teman memiliki sebaran yang sama karena rata-ratanya sama.
B. Teman Anda lebih konsisten karena variansnya lebih besar.
C. Nilai Anda lebih konsisten (lebih homogen) dibanding teman Anda; nilai teman Anda lebih fluktuatif dari minggu ke minggu.
D. Standar deviasi tidak dapat dipakai untuk membandingkan konsistensi.
E. Mean dan SD adalah ukuran yang saling bertentangan, tidak bisa dipakai bersamaan.

---

> **Sub-CPMK 2.2** — Menggunakan pandas dan numpy untuk eksplorasi data
> *Level Bloom:* C2 · *Konteks:* Umum

**5.** Diberikan DataFrame `df` berkolom `harga`, fungsi pandas/numpy mana yang paling tepat dipanggil untuk mendapatkan **ringkasan statistik deskriptif** (count, mean, std, min, quartiles, max) dalam satu perintah?

A. `df['harga'].count()`
B. `df['harga'].describe()`
C. `np.histogram(df['harga'])`
D. `df.groupby('harga').size()`
E. `df['harga'].unique()`

---

> **Sub-CPMK 3.1** — Membuat visualisasi data yang efektif menggunakan matplotlib dan seaborn
> *Level Bloom:* C3 · *Konteks:* Indonesia (IHSG harian 2024)

**6.** Anda memiliki data penutupan harian IHSG (Indeks Harga Saham Gabungan) sepanjang tahun 2024 (± 240 titik tanggal). Jenis grafik (*chart*) yang **paling tepat** untuk menampilkan tren pergerakan indeks dari waktu ke waktu adalah...

A. Pie chart.
B. Bar chart horizontal.
C. Line chart (time-series).
D. Box plot tunggal.
E. Scatter plot tanpa sumbu waktu.

---

> **Sub-CPMK 3.2** — Menerapkan prinsip storytelling with data untuk komunikasi temuan
> *Level Bloom:* C4 · *Konteks:* Umum

**7.** Sebuah presentasi menampilkan bar chart "Pertumbuhan Pendapatan 2023 vs 2024" dengan sumbu Y dimulai dari 98 (bukan 0), menggunakan warna merah menyala untuk 2024 dan abu-abu untuk 2023, tanpa label satuan. Kenaikan sebenarnya hanya 2%, tetapi visual terlihat seperti lompatan 50%. Pelanggaran prinsip *storytelling with data* yang **paling utama** di sini adalah...

A. Penggunaan bar chart (seharusnya pakai pie chart).
B. *Truncated y-axis* yang mendistorsi persepsi besaran perbedaan.
C. Penggunaan dua warna yang berbeda.
D. Menampilkan dua tahun sekaligus.
E. Jumlah data terlalu banyak.

---

> **Sub-CPMK 4.1** — Menghitung probabilitas dasar, conditional probability, dan menerapkan Bayes' theorem
> *Level Bloom:* C3 · *Konteks:* Islami (pembagian warisan sederhana)

**8.** Seorang ayah wafat meninggalkan harta Rp 120.000.000 dan dua ahli waris: seorang istri dan seorang anak laki-laki tunggal. Menurut ketentuan syariah, istri berhak 1/8 dari harta dan anak laki-laki mendapat sisanya (sebagai *ashabah*). Jika seluruh harta dianggap peluang total = 1, berapa **proporsi** harta yang diterima anak laki-laki?

A. 1/8
B. 1/4
C. 1/2
D. 7/8
E. 1 (seluruhnya)

---

> **Sub-CPMK 4.1** — Menghitung probabilitas dasar, conditional probability, dan menerapkan Bayes' theorem
> *Level Bloom:* C4 · *Konteks:* Indonesia (skrining TB)

**9.** Prevalensi TB di suatu kota di Indonesia = 1%. Sebuah alat skrining memiliki sensitivitas 90% (*P(positif|sakit) = 0,90*) dan spesifisitas 95% (*P(negatif|sehat) = 0,95*). Jika seseorang hasilnya **positif**, berapa probabilitas (posterior) ia benar-benar sakit TB? *(pakai Bayes)*

A. 0,90
B. 0,50
C. 0,154 (≈ 15,4%)
D. 0,95
E. 0,01

---

> **Sub-CPMK 4.2** — Mensimulasikan eksperimen probabilitas menggunakan Python
> *Level Bloom:* C3 · *Konteks:* Umum

**10.** Anda mensimulasikan 10.000 lemparan dadu adil dengan Python (`np.random.randint(1, 7, 10000)`), lalu menghitung proporsi munculnya angka 6. Hasil simulasi = 0,1672. Interpretasi yang **paling tepat**:

A. Simulasi salah karena nilai teoretis harus tepat 1/6 = 0,1667.
B. Hasil simulasi konsisten dengan probabilitas teoretis 1/6 ≈ 0,1667; selisih kecil adalah variasi acak yang wajar dan mengecil bila jumlah simulasi diperbesar.
C. Probabilitas riil angka 6 adalah 0,1672, bukan 1/6.
D. Dadu pasti tidak adil.
E. Hasil simulasi tidak ada hubungannya dengan nilai teoretis.

---

> **Sub-CPMK 5.1** — Mengidentifikasi dan menerapkan distribusi probabilitas (Normal, Binomial, Poisson)
> *Level Bloom:* C2 · *Konteks:* Umum

**11.** Manakah pernyataan berikut yang **benar** tentang distribusi probabilitas?

A. Distribusi Binomial adalah distribusi kontinu dengan parameter μ dan σ.
B. Distribusi Poisson dicirikan oleh satu parameter λ (rata-rata kejadian per satuan waktu/ruang) dan umum dipakai untuk kejadian jarang.
C. Distribusi Normal hanya valid bila n ≤ 30.
D. Distribusi Binomial cocok untuk mencatat waktu kedatangan pelanggan yang kontinu.
E. Distribusi Normal tidak memiliki parameter.

---

> **Sub-CPMK 5.2** — Menjelaskan dan mendemonstrasikan Central Limit Theorem
> *Level Bloom:* C4 · *Konteks:* Umum

**12.** Pernyataan yang **paling tepat** tentang *Central Limit Theorem* (CLT) adalah...

A. Distribusi populasi selalu normal, apa pun bentuk datanya.
B. Untuk ukuran sampel n yang cukup besar (umumnya n ≥ 30), distribusi rata-rata sampel (x̄) mendekati normal dengan mean μ dan standar deviasi σ/√n, meskipun distribusi populasinya tidak normal.
C. CLT hanya berlaku bila data populasi sudah normal.
D. CLT menyatakan bahwa varians sampel selalu sama dengan varians populasi.
E. CLT hanya dipakai untuk data diskret.

---

> **Sub-CPMK 6.1** — Menerapkan teknik sampling dan menghitung confidence interval
> *Level Bloom:* C3 · *Konteks:* JTBD (estimasi pengeluaran harian pribadi)

**13.** Dari catatan 30 hari pengeluaran makan harian Anda diperoleh 95% *confidence interval* untuk rata-rata pengeluaran: **(Rp 42.000; Rp 58.000)**. Interpretasi yang **paling tepat**:

A. Ada peluang 95% bahwa rata-rata pengeluaran populasi (seluruh hari di masa depan) berada di antara Rp 42.000 dan Rp 58.000.
B. Bila prosedur sampling & perhitungan CI ini diulang berkali-kali dengan sampel berbeda, sekitar 95% interval yang terbentuk akan memuat rata-rata populasi sebenarnya.
C. 95% dari hari individual akan memiliki pengeluaran antara Rp 42.000 dan Rp 58.000.
D. Rata-rata sampel pasti berada di luar interval tersebut.
E. Interval ini tidak memuat informasi tentang populasi.

---

> **Sub-CPMK 7.1** — Melaksanakan uji hipotesis (z-test, t-test) dan menginterpretasi p-value
> *Level Bloom:* C3 · *Konteks:* Umum

**14.** Pada sebuah uji hipotesis dengan α = 0,05 diperoleh *p-value* = 0,018. Keputusan yang **tepat** adalah...

A. Terima H₀ karena *p-value* > 0.
B. Tolak H₀ karena *p-value* (0,018) < α (0,05); ada bukti statistik untuk mendukung H₁.
C. Tolak H₀ karena *p-value* > α.
D. Tidak cukup informasi, perlu hitung ulang rata-rata.
E. *p-value* tidak relevan terhadap keputusan hipotesis.

---

> **Sub-CPMK 7.2** — Menjelaskan error Type I/II dan effect size
> *Level Bloom:* C4 · *Konteks:* Umum

**15.** Manakah pasangan definisi *error* Tipe I dan Tipe II berikut yang **benar**?

A. Tipe I = menolak H₀ padahal H₀ benar; Tipe II = gagal menolak H₀ padahal H₀ salah.
B. Tipe I = menerima H₀ padahal H₀ salah; Tipe II = menolak H₀ padahal H₀ benar.
C. Tipe I dan Tipe II adalah hal yang sama.
D. Tipe I = α sama dengan *p-value*; Tipe II = β sama dengan 1 - α.
E. Tipe I hanya terjadi pada uji dua-sisi, Tipe II hanya pada uji satu-sisi.

---

## BAGIAN II — ESAI (30 poin)

> **Sub-CPMK 1.3** — Menjelaskan prinsip etika data dan responsible AI
> *Level Bloom:* C4 · *Konteks:* Islami + Indonesia (data jamaah masjid)

**E1. (10 poin)** Pengurus sebuah masjid di Jakarta mengumpulkan data donatur (nama, NIK, alamat, nominal donasi) selama lima tahun melalui formulir fisik tanpa mencantumkan kebijakan privasi. Sebuah *startup* fintech menawarkan kerja sama: pengurus menyerahkan seluruh data donatur, sebagai imbal balik masjid mendapatkan dana operasional. Pengurus ragu antara manfaat dana vs amanah data jamaah.

a) Identifikasi **tiga (3) prinsip etika data / responsible AI** yang paling relevan dengan kasus ini (contoh: *informed consent*, *purpose limitation*, *data minimization*, *privacy*, *accountability*). Jelaskan masing-masing dalam 1-2 kalimat. (4 poin)

b) Berikan **argumentasi keputusan**: apakah pengurus boleh menyerahkan data tersebut? Jelaskan syarat yang harus dipenuhi agar (jika boleh) kerja sama itu etis. (4 poin)

c) Usulkan **dua (2) langkah mitigasi praktis** bila kerja sama tetap dilanjutkan (mis. anonimisasi, opt-in, perjanjian pembatasan penggunaan). (2 poin)

---

> **Sub-CPMK 3.2** — Menerapkan prinsip storytelling with data untuk komunikasi temuan
> *Level Bloom:* C5 · *Konteks:* Indonesia (chart IHSG)

**E2. (10 poin)** Sebuah media keuangan daring merilis grafik berjudul *"IHSG Meroket 2024!"* dengan karakteristik berikut:

- Jenis: bar chart vertikal membandingkan IHSG Des 2023 vs Des 2024.
- Sumbu Y dimulai dari **7.200** (bukan 0), skala maksimum 7.350.
- Kenaikan aktual: dari 7.272 ke 7.402 (≈ **1,8%**), tetapi visual bar 2024 terlihat **≈ 3x** lebih tinggi dari bar 2023.
- Warna: 2023 abu-abu pudar, 2024 merah menyala dengan efek gradien dan ikon panah ke atas.
- Tidak ada label nilai pasti (hanya "2023" dan "2024" di sumbu X), tidak ada sumber data, tidak ada catatan skala.

a) Identifikasi **tiga (3) kesalahan utama** pada grafik tersebut (selain judul sensasional) dan jelaskan **mengapa** masing-masing termasuk *misleading visualization*. (6 poin)

b) Rancang **perbaikan konkret** yang harus dilakukan sebelum grafik layak ditayangkan (minimal 4 perbaikan praktis — contoh: pilihan chart, sumbu, label, sumber, anotasi). (4 poin)

---

> **Sub-CPMK 7.1** — Melaksanakan uji hipotesis (z-test, t-test) dan menginterpretasi p-value
> *Level Bloom:* C4 · *Konteks:* JTBD (klaim asupan kalori pribadi)

**E3. (10 poin)** Anda membuat klaim pribadi: *"Rata-rata asupan kalori harian saya = 2000 kkal"*. Teman Anda menduga Anda sebenarnya mengonsumsi **lebih dari** 2000 kkal per hari. Anda mencatat asupan selama **10 hari**: rata-rata sampel x̄ = **2.150 kkal**, standar deviasi sampel s = **200 kkal**. Asumsikan data approximately normal. Gunakan α = 0,05.

a) Tuliskan **hipotesis** H₀ dan H₁ dalam notasi simbolik. Jelaskan apakah uji bersifat satu-sisi atau dua-sisi, dan beri alasannya. (2 poin)

b) Justifikasi pemilihan **α = 0,05** (1 kalimat) dan pilih **statistik uji yang tepat** (z atau t) beserta **rumusnya**. (3 poin)

c) Tentukan **daerah kritis** menggunakan tabel yang sesuai (df = 9), lalu hitung **nilai statistik uji** dengan menunjukkan substitusi angka. (3 poin)

d) Nyatakan **keputusan** (tolak/gagal tolak H₀) dan tulis **interpretasi praktis** dalam 1-2 kalimat yang dimengerti teman non-statistik Anda. (2 poin)

---

## BAGIAN III — HITUNG / INTERPRETASI (40 poin)

> **Sub-CPMK 2.1** — Menghitung dan menginterpretasi ukuran pemusatan dan penyebaran data
> *Level Bloom:* C3 · *Konteks:* Indonesia (harga beras medium 10 provinsi)

**H1. (13 poin)** Dinas Pangan mencatat harga beras medium (Rp/kg) pada 10 provinsi berikut (data sudah diurutkan dari terkecil ke terbesar):

```
11.000 | 11.500 | 12.000 | 12.000 | 12.500 | 13.000 | 13.500 | 13.500 | 14.000 | 14.500
```

Lakukan analisis berikut dengan **menunjukkan rumus, substitusi, dan hasil**:

a) Hitung **mean (x̄)** harga beras. (2 poin)

b) Hitung **median** dan **modus**. (2 poin)

c) Hitung **standar deviasi sampel (s)** — boleh pakai rumus definisi atau rumus komputasi; tunjukkan langkah perhitungan deviasi kuadratnya. (4 poin)

d) Tentukan **Q1, Q3, dan IQR**. (3 poin)

e) Berikan **interpretasi** singkat (1-2 kalimat): apakah sebaran harga beras cenderung simetris atau *skewed*? Gunakan perbandingan mean vs median dan/atau posisi Q1, Q2, Q3 sebagai argumen. (2 poin)

---

> **Sub-CPMK 5.1 & 5.2** — Mengidentifikasi dan menerapkan distribusi probabilitas (Normal, Binomial, Poisson); Menjelaskan dan mendemonstrasikan Central Limit Theorem
> *Level Bloom:* C3 · *Konteks:* JTBD (target fitness mingguan — jarak lari)

**H2. (13 poin)** Anda mencatat jarak lari per sesi selama beberapa bulan. Distribusi jarak lari Anda diasumsikan **Normal** dengan rata-rata μ = **5,0 km** dan standar deviasi σ = **0,8 km**.

a) Hitung **P(X > 6)** — probabilitas Anda lari lebih dari 6 km pada satu sesi. Tunjukkan perhitungan *Z-score* dan penggunaan tabel Z di lampiran. (4 poin)

b) Hitung **P(4,2 < X < 5,8)** — probabilitas jarak lari berada antara 4,2 km dan 5,8 km. (4 poin)

c) Anda berencana berlari **n = 16 sesi** dalam sebulan. Menggunakan Central Limit Theorem, hitung **P(x̄ > 5,2 km)** — peluang rata-rata jarak lari 16 sesi melebihi 5,2 km. Tunjukkan rumus standar error x̄ dan konversi ke Z. (5 poin)

---

> **Sub-CPMK 7.1** — Melaksanakan uji hipotesis (z-test, t-test) dan menginterpretasi p-value
> *Level Bloom:* C4 · *Konteks:* Indonesia (klaim waktu tempuh TransJakarta)

**H3. (14 poin)** PT TransJakarta mengklaim bahwa waktu tempuh rata-rata rute X tidak lebih dari **45 menit**. Seorang pengamat mengumpulkan sampel acak **n = 16** perjalanan dan memperoleh rata-rata sampel x̄ = **48 menit** dengan standar deviasi sampel s = **6 menit**. Data diasumsikan approximately normal. Uji klaim tersebut pada taraf signifikansi **α = 0,05**.

a) Tuliskan **H₀ dan H₁** dalam notasi simbolik. Tentukan apakah ujinya satu-sisi atau dua-sisi, beserta alasannya. (2 poin)

b) Identifikasi **statistik uji yang tepat** (z-test atau t-test) dengan alasan singkat (perhatikan n dan apakah σ populasi diketahui). Tuliskan **rumus**nya. (3 poin)

c) Hitung **nilai statistik uji** dengan menunjukkan substitusi angka bertahap. (3 poin)

d) Tentukan **daerah kritis** / **nilai kritis** menggunakan tabel t di lampiran (df = n - 1). Bandingkan nilai statistik uji vs nilai kritis. (3 poin)

e) Tulis **keputusan statistik** (tolak/gagal tolak H₀) dan **interpretasi praktis** dalam bahasa non-teknis untuk manajemen TransJakarta. (3 poin)

---

## LAMPIRAN — Tabel Distribusi (Ringkas)

> *Catatan:* Nilai pada tabel di bawah sudah cukup untuk menyelesaikan seluruh soal UTS ini. Untuk nilai df / z yang tidak tertera, gunakan nilai terdekat dan nyatakan asumsinya pada lembar jawaban.

### Tabel Z — Distribusi Normal Standar

Tabel Z berikut memberikan **P(Z ≤ z)** (luas kumulatif di bawah kurva normal standar dari −∞ hingga z) dan **P(Z > z) = 1 − P(Z ≤ z)**:

| z    | P(Z ≤ z) | P(Z > z) |
|------|----------|----------|
| 0,25 | 0,5987   | 0,4013   |
| 0,50 | 0,6915   | 0,3085   |
| 1,00 | 0,8413   | 0,1587   |
| 1,25 | 0,8944   | 0,1056   |
| 1,28 | 0,8997   | 0,1003   |
| 1,64 | 0,9495   | 0,0505   |
| 1,96 | 0,9750   | 0,0250   |
| 2,33 | 0,9901   | 0,0099   |
| 2,58 | 0,9951   | 0,0049   |

Sifat simetri: P(Z < −z) = P(Z > z); P(−z < Z < z) = 2·P(Z ≤ z) − 1.

### Tabel t — Nilai Kritis (one-tailed)

| df | t(α=0,10) | t(α=0,05) | t(α=0,025) | t(α=0,01) |
|----|-----------|-----------|------------|-----------|
| 9  | 1,383     | 1,833     | 2,262      | 2,821     |
| 10 | 1,372     | 1,812     | 2,228      | 2,764     |
| 14 | 1,345     | 1,761     | 2,145      | 2,624     |
| 15 | 1,341     | 1,753     | 2,131      | 2,602     |
| 20 | 1,325     | 1,725     | 2,086      | 2,528     |
| 29 | 1,311     | 1,699     | 2,045      | 2,462     |

### Tabel Chi-Square — Nilai Kritis (upper-tail)

| df | χ²(0,10) | χ²(0,05) | χ²(0,025) | χ²(0,01) |
|----|----------|----------|-----------|----------|
| 5  | 9,236    | 11,070   | 12,833    | 15,086   |
| 9  | 14,684   | 16,919   | 19,023    | 21,666   |
| 15 | 22,307   | 24,996   | 27,488    | 30,578   |

---

## Penutup

> *"Barang siapa menempuh suatu jalan untuk mencari ilmu, niscaya Allah akan memudahkan baginya jalan menuju surga."*
> — **HR. Muslim**

**"Man jadda wajada"** — Siapa bersungguh-sungguh, pasti berhasil.

**~ Selamat Mengerjakan — Jazakumullahu khairan ~**
