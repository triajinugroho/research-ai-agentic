# BAB 11: ANALISIS DATA DAN PENARIKAN SIMPULAN

**Bahan rujukan penyelarasan kurikulum** — disusun Tri Aji Nugroho, S.T., M.T.
Pengampu mata kuliah menurut registri: **Andi Arniaty Arsyad, Ph.D.** (`AAA`).

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `METPEN-Sub-CPMK071-1` | Menerapkan (C3) prinsip analisis yang sesuai dan menganalisis (C4) batas simpulan yang dapat ditarik dari data | C3–C4 |

Setelah membaca bab ini, pembaca diharapkan mampu:

1. **Memilih** (C4) teknik analisis yang sesuai RQ dan jenis data.
2. **Menyusun** (C3) rencana analisis yang ditetapkan sebelum data terkumpul.
3. **Menjelaskan** (C2) asumsi metode dan cara memeriksanya.
4. **Merumuskan** (C4) kriteria penolakan dugaan.
5. **Mengenali** (C4) lompatan penalaran dari data ke simpulan.

---

## 11.1 Rencana Ditetapkan di Muka

### 11.1.1 Yang Terjadi Bila Tidak

| Praktik | Akibatnya |
|---------|-----------|
| Mencoba banyak analisis sampai ada yang berarti | Salah satunya akan tampak berarti secara kebetulan |
| Menyesuaikan hipotesis dengan hasil | Penelitian kehilangan daya ujinya |
| Menambah data sampai hasilnya signifikan | Tingkat galat sebenarnya jauh lebih besar dari yang dilaporkan |
| Menyisihkan data yang tidak cocok | Simpulan bias |
| Memilih ambang setelah melihat nilai p | Ambang menjadi formalitas |

Kelima praktik ini jarang dilakukan dengan niat menipu. Ia lahir dari
keinginan wajar untuk menemukan sesuatu — dan justru karena itu perlu dicegah
dengan cara yang tidak bergantung pada niat baik.

### 11.1.2 Pencegahannya

> **Tulis rencana analisis, beri tanggal, dan lampirkan** sebelum pengumpulan
> data dimulai. Penyimpangan dari rencana dilaporkan beserta alasannya.

Praktik ini dikenal sebagai *preregistration* dan kini lazim di banyak bidang.
Untuk Tugas Akhir, tidak perlu didaftarkan pada lembaga mana pun; tanggal pada
dokumen sudah memenuhi maksudnya.

| Yang dilaporkan | Contoh |
|-----------------|--------|
| Analisis sesuai rencana | "Sesuai rencana (lampiran E), uji t dua sampel bebas dipakai" |
| Penyimpangan | "Rencana menetapkan uji t; asumsi normalitas tidak terpenuhi (Shapiro-Wilk p=0,003), sehingga Mann-Whitney dipakai, sesuai ketentuan rencana §3" |
| Analisis tambahan | "Analisis berikut tidak direncanakan dan bersifat eksploratif" |

Baris terakhir penting: analisis yang tidak direncanakan boleh dilakukan,
asalkan **ditandai sebagai eksploratif** dan tidak diperlakukan sebagai
pengujian hipotesis.

---

## 11.2 Analisis Kuantitatif

### 11.2.1 Mencocokkan RQ, Data, dan Analisis

| RQ berbentuk | Data | Analisis |
|--------------|------|----------|
| Berapa banyak, seberapa sering | Nominal/ordinal | Frekuensi, persentase, modus |
| Seberapa besar rata-rata | Interval/rasio | Rerata, simpangan baku, interval kepercayaan |
| Apakah dua kelompok berbeda | Interval/rasio | Uji t; Mann-Whitney bila asumsi tak terpenuhi |
| Apakah >2 kelompok berbeda | Interval/rasio | ANOVA; Kruskal-Wallis |
| Apakah dua variabel berhubungan | Interval/rasio | Korelasi Pearson; Spearman untuk ordinal |
| Apakah kategori berhubungan | Nominal | Uji chi-kuadrat |
| Memprediksi Y dari beberapa X | Interval/rasio | Regresi |

> Perhitungan dan penafsiran uji-uji ini dibahas pada [Probabilitas dan
> Statistik](../../probabilitas-dan-statistik/README.md) dan Analisis Data
> Statistik. Yang ditambahkan di sini adalah **pertanggungjawaban atas
> pemilihannya**.

### 11.2.2 Asumsi

| Yang wajib dinyatakan | Mengapa |
|-----------------------|---------|
| Asumsi tiap uji | Uji yang asumsinya dilanggar menghasilkan simpulan keliru |
| Cara memeriksa asumsi | Agar dapat diperiksa orang lain |
| Tindakan bila tidak terpenuhi | Agar keputusan tidak diambil setelah melihat hasil |

Contoh untuk uji t dua sampel bebas:

| Asumsi | Cara memeriksa | Bila tidak terpenuhi |
|--------|----------------|----------------------|
| Normalitas dalam tiap kelompok | Shapiro-Wilk; grafik Q-Q | Mann-Whitney U |
| Homogenitas ragam | Uji Levene | Uji t Welch |
| **Kemandirian pengamatan** | **Dari rancangan, bukan dari data** | **Rancangan harus diubah** |

Baris ketiga menunjukkan hal penting: sebagian asumsi tidak dapat diperiksa
dari data, melainkan dijamin oleh rancangan. Bila rancangan melanggarnya —
misalnya mengukur orang yang sama berkali-kali dan memperlakukannya sebagai
pengamatan mandiri — tidak ada uji yang dapat memperbaikinya.

### 11.2.3 Besar Efek

| Yang dilaporkan | Menyatakan |
|-----------------|------------|
| Nilai p | Seberapa mungkin data ini muncul bila tidak ada efek |
| **Besar efek** | **Seberapa besar perbedaannya** |
| Interval kepercayaan | Rentang nilai yang masuk akal |

Ketiganya dilaporkan bersama. Nilai p sendiri tidak menyatakan besarnya
perbedaan: pada sampel besar, perbedaan yang sangat kecil dapat signifikan
secara statistik dan tidak berarti apa-apa secara praktis.

| Contoh | Penafsiran |
|--------|------------|
| p = 0,001; selisih rerata 0,3 detik dari 45 detik | Signifikan; tidak berarti secara praktis |
| p = 0,08; selisih rerata 12 detik dari 45 detik | Tidak signifikan pada 0,05; **mungkin berarti**; sampel mungkin terlalu kecil |

Baris kedua menunjukkan mengapa nilai p sendiri menyesatkan. Perbedaan 12
detik dari 45 detik besar; ketidaksignifikanannya mungkin menunjukkan bahwa
sampelnya kurang, bukan bahwa efeknya tidak ada.

---

## 11.3 Analisis Kualitatif

### 11.3.1 Enam Tahap Analisis Tematik

| Tahap | Kegiatan | Keluaran |
|-------|----------|----------|
| 1. Pengenalan data | Membaca seluruh transkrip; mencatat kesan awal | Catatan awal |
| 2. Penandaan | Memberi penanda pada potongan bermakna | Daftar penanda |
| 3. Pengelompokan | Menyusun penanda menjadi tema kandidat | Peta tema |
| 4. Peninjauan | Memeriksa tema terhadap data; menggabung atau memecah | Tema yang direvisi |
| 5. Penamaan | Memberi nama dan definisi tiap tema | Buku penanda final |
| 6. Pelaporan | Menyusun narasi dengan kutipan pendukung | Bab temuan |

### 11.3.2 Yang Wajib Dilaporkan

| Butir | Bentuknya |
|-------|-----------|
| Cara penandaan | Induktif (dari data) atau deduktif (dari kerangka), atau campuran |
| Jumlah penanda dan tema | Angka nyata pada setiap tahap |
| Kutipan pendukung tiap tema | Verbatim, dengan kode responden |
| **Kasus yang tidak sesuai tema** | Dilaporkan, tidak dibuang |
| Pemeriksaan kesesuaian | Bila ada penandaan silang, beserta jenis perbedaannya |
| Perubahan buku penanda | Kapan, karena data apa |

Baris keempat membedakan analisis yang jujur dari yang dipoles. Kasus yang
tidak sesuai tema hampir selalu ada, dan menjelaskannya sering lebih
informatif daripada tema itu sendiri.

### 11.3.3 Kutipan sebagai Bukti

| Pemakaian yang lemah | Pemakaian yang kuat |
|----------------------|---------------------|
| Satu kutipan panjang per tema | Beberapa kutipan pendek dari responden berbeda |
| Kutipan dipilih karena paling jelas | Kutipan mewakili sebaran, termasuk yang ragu |
| Kutipan tanpa kode responden | "(N7)" agar dapat ditelusuri |
| Kutipan tanpa konteks | Disertai keterangan situasi bila perlu |

Kutipan yang seluruhnya berasal dari dua responden yang paling artikulatif
memberi kesan bahwa tema itu kuat, padahal mungkin hanya kuat pada dua orang.

---

## 11.4 Dari Temuan ke Simpulan

### 11.4.1 Empat Lapis

```
DATA          →  TEMUAN         →  TAFSIRAN      →  SIMPULAN
"12 dari 18      "Sebagian besar   "Hambatan        "RQ1 terjawab:
 menyebut         responden         pelatihan        faktor utama
 pelatihan"       menyebut          bersifat         yang disebut
                  pelatihan"        struktural,      adalah ...,
                                    bukan            dengan batasan
                                    individual"      bahwa ..."
```

| Lapis | Sifatnya | Dapat dibantah dengan |
|-------|----------|----------------------|
| Data | Apa yang tercatat | Memeriksa catatan |
| Temuan | Rangkuman data | Menghitung ulang |
| Tafsiran | **Penalaran peneliti** | Penjelasan tandingan |
| Simpulan | Jawaban atas RQ, dengan batasnya | Keduanya di atas |

Lapis ketiga adalah tempat sebagian besar perdebatan terjadi. Tafsiran tidak
mengikuti secara otomatis dari temuan; ia keputusan peneliti yang harus
dipertanggungjawabkan.

### 11.4.2 Lompatan yang Sering Terjadi

| Lompatan | Bentuknya | Perbaikan |
|----------|-----------|-----------|
| Temuan → simpulan besar | "Pelatihan tidak memadai" → "Sistem gagal karena kebijakan pemerintah" | Batasi pada yang didukung data |
| Korelasi → sebab | "Berhubungan" → "menyebabkan" | Pakai kata yang tepat; sebutkan bahwa rancangan tidak menguji sebab |
| Sampel → populasi | 18 responden satu dinas → "staf pemerintah pada umumnya" | Nyatakan batas populasi |
| Tidak signifikan → tidak ada | "p > 0,05" → "tidak ada perbedaan" | "Tidak ditemukan bukti perbedaan pada sampel ini" |
| Berhasil pada kasus → berlaku umum | "Sistem berhasil di 3 dinas" → "pendekatan ini efektif" | Sebutkan keadaan yang menyertainya |

### 11.4.3 Kekeliruan "Tidak Signifikan Berarti Tidak Ada"

Kekeliruan logika yang paling umum dalam penulisan ilmiah.

| Pernyataan | Benar? |
|------------|--------|
| "p > 0,05, sehingga tidak ada perbedaan" | **Salah** |
| "p > 0,05, sehingga tidak ditemukan bukti perbedaan pada sampel ini" | Benar |
| "p > 0,05 dengan besar efek kecil dan interval kepercayaan sempit, sehingga perbedaan yang berarti secara praktis dapat dikesampingkan" | Benar, dan lebih informatif |

Ketiadaan bukti bukan bukti ketiadaan — terutama pada sampel kecil, yang
memang tidak berdaya mendeteksi perbedaan kecil.

---

## 11.5 Kriteria Penolakan Dugaan

### 11.5.1 Bagian yang Sering Hilang

```markdown
## Kriteria Penolakan — H2

Dugaan : Keterjelasan sistem berhubungan negatif dengan
         niat menghentikan pemakaian.

Didukung bila       : Korelasi negatif, p < 0,05, |r| ≥ 0,3
Tidak didukung bila : |r| < 0,3 atau p ≥ 0,05
Tidak dapat
disimpulkan bila    : Sampel terkumpul < 60; atau asumsi
                      dilanggar dan alternatif nonparametrik
                      juga tidak memenuhi syarat

Yang akan dilaporkan dalam ketiga keadaan: seluruhnya.
```

Untuk penelitian kualitatif:

```markdown
## Kriteria Penolakan — P1

Proposisi : Keterjelasan sistem berperan dalam keputusan
            pengguna untuk melanjutkan pemakaian.

Didukung bila       : Tema muncul pada ≥8 dari 15 responden,
                      dan tidak ada kasus yang jelas membantah
Tidak didukung bila : Tema muncul pada <5 responden, atau
                      ditemukan ≥3 kasus yang membantah
Yang dilakukan bila ada kasus membantah:
                      Dianalisis, dilaporkan, tidak dibuang;
                      dicari apa yang membedakannya
```

### 11.5.2 Mengapa Wajib

| Tanpa kriteria penolakan | Dengan kriteria penolakan |
|--------------------------|---------------------------|
| Hasil apa pun dapat ditafsirkan mendukung | Hasil dinilai terhadap ambang yang sudah ditetapkan |
| "Cenderung mendukung", "mengindikasikan" | Didukung atau tidak didukung, dengan angkanya |
| Penelitian tidak dapat gagal | Penelitian dapat menghasilkan jawaban "tidak" |

Penelitian yang hanya dapat melaporkan satu kemungkinan hasil bukan
penelitian — dan hampir selalu dikenali penguji dari kalimat-kalimat yang
tidak tegas pada bab pembahasan.

### 11.5.3 Hasil Negatif Tetap Kontribusi

| Hasil | Kontribusinya |
|-------|---------------|
| Hubungan yang diduga tidak ditemukan | Mengoreksi anggapan yang lazim; mengarahkan penelitian berikutnya |
| Artefak tidak memenuhi kriteria | Menunjukkan batas pendekatan itu pada konteks ini |
| Temuan pustaka tidak berlaku di sini | **Kontribusi kesenjangan populasi yang jelas** |
| Tema yang diharapkan tidak muncul | Menunjukkan bahwa persoalannya berbeda dari yang diasumsikan |

Baris ketiga adalah alasan mengapa kesenjangan populasi merupakan pilihan
yang aman untuk Tugas Akhir: kedua kemungkinan hasil sama-sama informatif.

---

## AI Corner — Bab 11

### Batas Pemakaian

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI menjelaskan asumsi sebuah uji statistik | Memilih uji tanpa Anda memahaminya |
| Meminta AI membantu menulis kode analisis | Menyerahkan kode yang tidak dapat Anda jelaskan |
| Meminta AI memeriksa apakah simpulan melampaui data | Menafsirkan hasil analisis Anda |
| Meminta AI menandai lompatan penalaran dalam draf | Menulis bagian pembahasan |

### Kode yang Berjalan Tanpa Galat Bukan Analisis yang Benar

Bantuan AI membuat penulisan kode analisis jauh lebih cepat. Bahayanya
spesifik: **kode yang berjalan tanpa galat tidak berarti analisis yang
benar**.

| Kekeliruan yang tidak menimbulkan galat | Akibat |
|-----------------------------------------|--------|
| Memakai uji t pada data ordinal | Simpulan tidak sahih |
| Tidak memeriksa asumsi normalitas | Nilai p tidak bermakna |
| Salah menentukan variabel bebas dan terikat | Simpulan terbalik |
| Data hilang ditangani diam-diam oleh pustaka | Sampel berbeda dari yang dilaporkan |
| Uji berulang tanpa koreksi | Temuan palsu |
| Satuan atau skala tidak sesuai | Angka benar secara hitungan, salah secara makna |

Keenam kekeliruan ini menghasilkan keluaran yang tampak wajar. Tidak ada
pesan galat yang memperingatkan.

### Ketentuan Mata Kuliah Ini

> **Setiap baris analisis harus dapat dijelaskan penulisnya** — mengapa uji
> itu, apa asumsinya, apa artinya bila asumsi dilanggar, dan bagaimana data
> hilang ditangani.

Ini diperiksa pada pertahanan lisan Minggu 15, dengan cara yang sederhana:
penguji menunjuk satu baris kode atau satu angka dalam tabel dan meminta
penjelasan.

### Pemakaian yang Dianjurkan

```
RQ saya : [tempelkan]
Jenis data setiap variabel : [sebutkan skala masing-masing]
Rancangan : [sebutkan]
Analisis yang saya rencanakan : [sebutkan]

Tugas Anda:
1. Sebutkan asumsi yang harus dipenuhi analisis itu.
2. Untuk setiap asumsi, sebutkan cara memeriksanya.
3. Sebutkan analisis alternatif bila asumsi tidak terpenuhi.
4. Tanyakan kepada saya hal-hal yang belum saya nyatakan dan
   diperlukan untuk menilai kesesuaian analisis ini.

Jangan menyimpulkan bahwa analisis saya sudah tepat.
Jangan menafsirkan hasil apa pun.
```

Butir 4 sering menunjukkan lubang dalam rencana — misalnya tentang penanganan
data hilang atau kemandirian pengamatan.

---

## Latihan Soal

### Tingkat Dasar

1. Sebutkan lima praktik yang dicegah oleh rencana analisis yang ditetapkan di muka.
2. Mengapa sebagian asumsi tidak dapat diperiksa dari data?
3. Jelaskan perbedaan antara nilai p dan besar efek.
4. Sebutkan enam tahap analisis tematik.
5. Mengapa "p > 0,05 sehingga tidak ada perbedaan" keliru?

### Tingkat Menengah

6. Untuk setiap kutipan berikut, sebutkan lompatan penalarannya dan tulis versi yang benar:
   - "Uji korelasi menunjukkan r = 0,62 (p < 0,01), sehingga beban kerja menyebabkan penurunan pemakaian."
   - "Dari 18 responden, 12 menyebut pelatihan. Dengan demikian dua pertiga staf pemerintah daerah mengalami masalah pelatihan."
   - "Uji t menghasilkan p = 0,12, sehingga tidak ada perbedaan antara kelompok A dan B."
   - "Sistem memperoleh akurasi 94%, lebih tinggi dari tebakan acak (50%), sehingga terbukti efektif untuk dipakai di lapangan."

7. Susun rencana analisis untuk setiap RQ Anda, mencakup: data, analisis, keluaran, asumsi, cara memeriksa, dan tindakan bila tidak terpenuhi.

8. Tulis kriteria penolakan untuk setiap hipotesis atau proposisi dalam penelitian Anda, dengan ketiga keadaan (didukung, tidak didukung, tidak dapat disimpulkan).

9. Untuk penelitian kualitatif, susun rencana pelaporan yang mencakup keenam butir §11.3.2, termasuk bagaimana kasus yang tidak sesuai tema akan ditangani.

### Tingkat Mahir

10. **Latihan data simulasi.** Buat data berbentuk seperti data yang akan Anda kumpulkan (ukuran sama, skala sama, isi acak). Jalankan seluruh rencana analisis pada data itu. Catat setiap langkah yang macet, setiap keputusan yang harus Anda ambil di tempat, dan setiap informasi yang ternyata tidak Anda rencanakan untuk dikumpulkan. Perbaiki rencana.

11. Dengan ukuran sampel yang Anda rencanakan, hitung seberapa besar efek yang masih dapat dideteksi. Bila jawabannya "hanya efek yang sangat besar", jelaskan apa artinya bagi simpulan Anda, dan apa yang akan Anda nyatakan bila hasilnya tidak signifikan.

12. Tulis dua versi bagian simpulan: satu bila dugaan didukung, satu bila tidak. Untuk versi kedua, jelaskan kontribusi apa yang tetap dihasilkan dan bagaimana Anda akan merumuskannya. Bandingkan panjang dan kekuatan kedua versi — bila versi kedua jauh lebih lemah, periksa apakah rancangan Anda benar-benar dapat menghasilkan hasil negatif yang bermakna.

---

## Rangkuman

| Gagasan pokok | Rumusan singkat |
|---------------|-----------------|
| Rencana di muka | Mencegah lima praktik yang lahir dari keinginan wajar menemukan sesuatu |
| Penyimpangan | Boleh, asalkan dilaporkan beserta alasannya |
| Analisis tak terencana | Boleh, asalkan ditandai eksploratif |
| Asumsi kemandirian | Dijamin rancangan, bukan diperiksa dari data |
| Besar efek | Dilaporkan bersama nilai p; p sendiri menyesatkan |
| Kasus tidak sesuai tema | Dilaporkan, tidak dibuang; sering lebih informatif |
| Kutipan | Dari responden yang beragam, dengan kode agar tertelusur |
| Empat lapis | Data → temuan → tafsiran → simpulan; lapis ketiga milik peneliti |
| Kekeliruan terumum | Tidak signifikan dianggap berarti tidak ada |
| Kriteria penolakan | Membuat penelitian dapat menghasilkan jawaban "tidak" |
| Batas AI | Setiap baris analisis harus dapat dijelaskan penulisnya |

---

## Referensi

1. Field, A. (2024). *Discovering Statistics Using IBM SPSS Statistics* (6th ed.). SAGE Publications.
2. Braun, V., & Clarke, V. (2006). Using Thematic Analysis in Psychology. *Qualitative Research in Psychology*, 3(2), 77–101.
3. Miles, M. B., Huberman, A. M., & Saldaña, J. (2020). *Qualitative Data Analysis: A Methods Sourcebook* (4th ed.). SAGE Publications.
4. Wasserstein, R. L., & Lazar, N. A. (2016). The ASA Statement on p-Values: Context, Process, and Purpose. *The American Statistician*, 70(2), 129–133.
5. Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The Preregistration Revolution. *PNAS*, 115(11), 2600–2606.
6. Lakens, D. (2013). Calculating and Reporting Effect Sizes to Facilitate Cumulative Science. *Frontiers in Psychology*, 4, 863.
7. Saldaña, J. (2021). *The Coding Manual for Qualitative Researchers* (4th ed.). SAGE Publications.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Modul mingguan | [Minggu 12](../03-modules/week-12-analisis-data-dan-penarikan-simpulan.md) |
| Lokakarya | [Lokakarya 12](../04-labs/lab-12-rencana-analisis-data.md) |
| Mata kuliah terkait | [Probabilitas dan Statistik](../../probabilitas-dan-statistik/README.md) |
| Bab sebelumnya | [Bab 10](bab-10-validitas-reliabilitas-dan-ancamannya.md) |
| Bab berikutnya | [Bab 12 — *Design Science* dan Evaluasi Artefak](bab-12-design-science-dan-evaluasi-artefak.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
