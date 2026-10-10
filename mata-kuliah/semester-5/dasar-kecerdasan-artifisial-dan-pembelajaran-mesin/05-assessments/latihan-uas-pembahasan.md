---
id: uai-if52510031-latihan-uas-pembahasan
tipe: asesmen
judul: "Latihan UAS — Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — Pembahasan dan Pedoman Skor"
kode_mk: IF52510031
nama_mk: Dasar Kecerdasan Artifisial dan Pembelajaran Mesin
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-09
---

# Pembahasan dan Pedoman Skor — Latihan UAS Dasar Kecerdasan Artifisial dan Pembelajaran Mesin

## Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — IF52510031

> **Latihan UAS — bukan naskah UAS.** Pembahasan ini menyertai simulasi lengkap UAS Dasar Kecerdasan Artifisial dan Pembelajaran Mesin Ganjil 2026/2027 untuk berlatih: komposisi, durasi (120 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UAS. Naskah UAS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.
>
> **Kerjakan dulu [latihan UAS](latihan-uas.md) dalam 120 menit tanpa AI dan tanpa membuka berkas ini.** Sesudahnya, nilai jawaban Anda dengan pedoman skor, lalu bandingkan dengan contoh jawaban *Kurang*, *Cukup*, dan *Baik*. Untuk butir yang skornya di bawah separuh, baca ulang bagian buku ajar pada baris **Pelajari ulang** butir itu. Contoh jawaban *Baik* — tersedia untuk setiap soal Bagian A dan B serta setiap sub-soal analisis Bagian C — menunjukkan unsur yang dinilai, bukan satu-satunya rumusan yang benar, dan sengaja ditulis **seringkas jawaban bernilai penuh**: nilai penuh hanya menuntut unsur yang dinilai, sedangkan menulis lebih panjang tidak menambah skor dan menghabiskan waktu butir lain. Untuk sub-soal hitung, langkah pada pembahasan sudah merupakan jawaban lengkap. Bagian *jawaban model* memuat penjelasan untuk belajar, sehingga lebih panjang daripada yang perlu ditulis di ujian. Menghafal jawaban di sini tidak membantu: naskah UAS memakai konteks dan angka lain, jadi yang perlu dikuasai adalah **langkah dan alasannya**.

| Aspek | Keterangan |
|-------|------------|
| Soal | [Latihan UAS](latihan-uas.md) (10 soal, 100 poin) |
| Cetak biru | [Cetak biru butir dan panduan varian](latihan-uas-cetak-biru.md) |
| Penandaan | Judul tiap butir mencantumkan Sub-CPMK (kode registri), level Bloom, dan skor. Sub-CPMK ditetapkan **menurut isi butir** untuk analisis ketercapaian (bawaan sementara D-03(a)); bobot Tes Tulis UAS (15%) tetap tercatat pada `DAIML-Sub-CPMK082-1` sesuai alokasi registri dan RPS ([cetak biru §1](latihan-uas-cetak-biru.md#1-prinsip-penandaan)) |
| Penyusun | Tri Aji Nugroho, S.T., M.T. |
| Verifikasi angka | Seluruh angka Bagian C, A2, dan A4 — nilai akhir maupun nilai antara yang tertulis pada langkah, termasuk nilai berpembulatan per langkah C1 dan C2 — serta angka pendukung B1 dan B2 dihitung ulang dengan Python; tabel jarak dan hasil K-Means C3 diperiksa pada scikit-learn 1.6 dan 1.9 (§5) |

---

## 0. Kaidah Umum Penilaian

Mengikuti kaidah penilaian [kisi-kisi UAS §8](kisi-kisi-uas.md#8-kaidah-penilaian-bagian-b) dan rubrik ujian tulis [kerangka asesmen §5.4](assessment-framework.md#54-rubrik-ujian-tulis).

| Situasi | Penilaian |
|---------|-----------|
| Jawaban benar, langkah ditunjukkan | Nilai penuh |
| Langkah benar, hasil akhir salah karena kekeliruan hitung | **Nilai sebagian besar**: poin langkah penuh, sedangkan poin hasil unsur itu dipotong **separuh, dibulatkan ke atas ke kelipatan 0,25** (bagian hasil 0,25 atau 0,5 → potong 0,25; 0,75 atau 1 → potong 0,5). Bila pedoman skor suatu unsur tidak memisahkan langkah dan hasil, separuh poinnya dianggap langkah dan separuh hasil. Hasil yang salah karena rumus atau langkah yang salah dinilai menurut tabel kesalahan umum §4. **Kesalahan terbawa** (*error carried forward*): angka keliru yang dipakai dengan benar di langkah berikutnya tidak dihukum dua kali |
| Hasil benar tanpa langkah | Paling banyak 50% poin sub-soal |
| Jawaban benar tanpa alasan pada soal yang meminta alasan | Paling banyak 40% poin — **hanya untuk butir yang pedoman skornya tidak merinci unsur alasan**. Bila pedoman skor butir merinci unsur alasan secara terpisah, rincian butir itulah yang berlaku |
| **Bagian B:** jawaban berbeda dari kunci, penalaran tepat dan konsisten | **Nilai penuh** ([kisi-kisi §8](kisi-kisi-uas.md#8-kaidah-penilaian-bagian-b)). Pembahasan mencantumkan alternatif yang sudah diantisipasi; alternatif lain dinilai dengan unsur pedoman skor yang sama |
| Nama kelas atau fungsi pustaka | Tidak dinilai: "*gradient boosting*" sama dengan `HistGradientBoostingClassifier`; sintaks tidak diuji |
| Pembulatan | Toleransi ±0,002 untuk *entropy*, *Gini*, *information gain*, dan *silhouette*; ±0,0005 untuk C2 (empat desimal); pembulatan di tengah langkah tidak dihukum bila hasil akhir berada dalam toleransi |

**Satu pernyataan, satu unsur.** Bila pedoman skor merinci beberapa unsur, satu frasa jawaban hanya dinilai untuk **satu** unsur — unsur yang paling sesuai dengan isinya. Contoh: pada A3, "tidak perlu menentukan k" adalah sifat metode, bukan karakteristik data; pada A4, "validasi masih naik" tanpa angka yang ditulis sebagai alasan membeli dinilai pada alasan, bukan pada bukti dari tabel.

**Satuan skor terkecil: 0,25 poin.** Skor dicatat per baris: satu baris = satu soal Bagian A (bagian berlabel di dalamnya tidak dipisah) atau satu sub-soal Bagian B/C — 30 baris skor ([cetak biru §2](latihan-uas-cetak-biru.md#2-tabel-cetak-biru-per-butir)).

**Kaidah Bagian B.** Keenam butir dinilai dengan unsur [kisi-kisi §8](kisi-kisi-uas.md#8-kaidah-penilaian-bagian-b):

| Butir | Poin | Yang dinilai (kisi-kisi §8) |
|-------|------|-----------------------------|
| (a) Formulasi *task* | 2,5 | Ketepatan target dan penentuan kapan prediksi dibutuhkan |
| (b) Kolom terlarang | 2,5 | Ketepatan mengenali kebocoran, bukan jumlah kolom yang disebut: **hanya dua kolom pertama yang ditulis yang dinilai** |
| (c) Metrik | 2,5 | Keterkaitan dengan dampak kesalahan, bukan nama metriknya |
| (d) Model kandidat | 4,5 | Kesesuaian dengan sifat data dan kebutuhan; alasan yang ditulis |
| (e) Protokol evaluasi | 5,5 | Kesesuaian strategi pembagian; validasi dan penyetelan; perbandingan; kehadiran *baseline* |
| (f) Risiko etis | 5 | Kekonkretan, bukan pernyataan umum |

Singkatan Sub-CPMK pada tabel: `082-1` = `DAIML-Sub-CPMK082-1`; `102-1` = `DAIML-Sub-CPMK102-1`.

---

## 1. Bagian A — Konsep (25 poin)

### A1. *Ensemble* untuk Dua Masalah — `DAIML-Sub-CPMK082-1` · C4 · 5 poin

**Jawaban model** (Bab 8 §8.3.1–§8.3.3)

| Tim | Kondisi | Apakah rencana menolong? | Perubahan yang lebih tepat |
|-----|---------|--------------------------|----------------------------|
| (i) | ***Underfit*** (bias tinggi): F1 latih 0,61 ≈ validasi 0,60, keduanya rendah | **Tidak.** Merata-ratakan banyak pohon mengurangi **varians**, bukan bias. Setiap pohon `max_depth=2` sama terbatasnya, sehingga F1 validasi rata-rata 300 pohon tidak akan naik berarti — bahkan dapat turun: dengan subset fitur acak bawaan *Random Forest*, banyak pohon dangkal tidak memakai `stok_akhir_minggu_ini` | Tambah kompleksitas atau sinyal: longgarkan `max_depth` (dipilih dengan validasi silang), tambah fitur informatif, atau *boosting* (pohon berurutan memperbaiki kesalahan pohon sebelumnya) |
| (ii) | ***Overfit*** (varians tinggi): latih 1,00, validasi 0,71 | **Tidak banyak.** *Ensemble* seharusnya mengurangi varians, tetapi rumus $\text{Var}(\bar X)=\sigma^2/n$ berlaku bila penduganya **tidak berkorelasi**. Dengan `max_features=None` setiap pohon mempertimbangkan seluruh fitur, sehingga hampir semuanya memotong lebih dahulu pada `stok_akhir_minggu_ini` dan menjadi sangat mirip. Rata-rata pohon yang berkorelasi kuat hampir sama dengan satu pohon (0,71 vs 0,70); menambah pohon tidak mengurangi korelasi itu | `max_features="sqrt"` (subset fitur acak pada setiap percabangan) agar pohon kurang berkorelasi — itulah pembeda *Random Forest* dari *bagging*; dapat ditambah `min_samples_leaf` |

**Pedoman skor**

| Bagian | Poin | Rincian |
|--------|------|---------|
| (i) | 2,5 | Diagnosis *underfit*/bias tinggi dengan bukti angka 0,5 · mengapa rencana tidak menolong: rata-rata mengurangi varians, bukan bias 1,0 · perubahan yang menambah kompleksitas atau sinyal 1,0 |
| (ii) | 2,5 | Diagnosis *overfit*/varians tinggi dengan bukti angka 0,5 · mekanisme: `max_features=None` + fitur dominan → pohon berkorelasi → rata-rata hampir tidak mengurangi varians, dan menambah pohon tidak mengubahnya 1,0 ("pohon berkorelasi" tanpa dikaitkan dengan `max_features` atau fitur dominan 0,5) · `max_features` lebih kecil 1,0 (hanya pembatasan kedalaman atau `min_samples_leaf` tanpa `max_features` 0,5) |

Alternatif yang diterima: pada (i), "rencana tidak menolong; ganti dengan *gradient boosting*" dinilai penuh bila alasannya bias, bukan varians. Pada (ii), "buang fitur `stok_akhir_minggu_ini` agar pohon beragam" = 0 pada perubahan, karena membuang sinyal terkuat.

**Contoh jawaban**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "(i) Rencana tepat karena *Random Forest* lebih baik daripada pohon. (ii) Tambah pohon agar lebih stabil." | 0 |
| Cukup | "(i) *Underfit*: latih 0,61 dan validasi 0,60 sama-sama rendah; perdalam pohon. (ii) *Overfit*: latih 1,00, validasi 0,71; batasi `max_depth`." | 2,5 (i 1,5 — alasan rencana tidak menolong tidak ada · ii 1,0 — mekanisme tidak ada; perubahan tanpa `max_features` 0,5) |
| Baik | "(i) *Underfit*: latih 0,61 ≈ validasi 0,60, keduanya rendah. Rata-rata pohon mengurangi varians, bukan bias, jadi 300 pohon kedalaman 2 tidak menaikkan F1; perdalam pohon (pilih dengan CV) atau pakai *boosting*. (ii) *Overfit*: latih 1,00, validasi 0,71. Dengan `max_features=None` semua pohon memotong dulu pada `stok_akhir_minggu_ini`, jadi pohonnya berkorelasi dan rata-ratanya ≈ satu pohon; menambah pohon tidak mengubahnya. Pakai `max_features="sqrt"`." | 5 |

**Pelajari ulang:** [Bab 8 §8.3.1](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md#831-mengapa-berhasil) (mengapa *ensemble* berhasil), [§8.3.2](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md#832-bagging-dan-random-forest) (*bagging* dan *Random Forest*), [§8.3.3](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md#833-boosting) (*boosting*).

---

### A2. Membaca Perbandingan Model — `DAIML-Sub-CPMK082-1` · C4 · 5 poin

**Jawaban model** (Bab 9 §9.4.2, §9.2.2)

**(i)** $2\cdot SE = 2(0{,}0077) = 0{,}0154 < 0{,}0172$ → syarat pertama terpenuhi. Selisih per lipatan: +0,031; +0,028; +0,030; −0,001; −0,002 → hanya **3 dari 5** lipatan searah, kurang dari 4 → syarat kedua **tidak** terpenuhi. Kesimpulan rekan keliru karena hanya memakai separuh aturan: **belum dapat disimpulkan** HistGB lebih baik. Keunggulan HistGB terpusat pada L1–L3. Tindak lanjut: perlakukan keduanya setara dan pilih yang lebih sederhana (regresi logistik: lebih murah, lebih mudah dijelaskan — "model sederhana ≈ model kompleks → pilih yang sederhana", Bab 9 §9.4.2); atau, sebelum memutuskan, selidiki mengapa selisih hanya muncul pada L1–L3. (Nilai tambah di luar hitungan manual: uji formal *corrected resampled t-test*, Lab 10 Tantangan 4.)

**(ii)** Keduanya **tidak bermakna**: SVM − NB, $2\cdot SE = 0{,}010 > 0{,}006$ dan searah 3/5; HistGB − NB, $2\cdot SE = 0{,}012 > 0{,}004$ dan searah 2/5. Dua model kompleks yang disetel tidak mengungguli Naive Bayes tanpa penyetelan, padahal ketiganya jauh di atas *baseline*: model sudah menangkap sinyal yang ada, sehingga **kemungkinan besar pembatasnya adalah fitur (sinyal data), bukan algoritma** — "ada yang perlu diselidiki — biasanya pada fiturnya" (Bab 9 §9.2.2). Tindak lanjut: pakai model yang paling sederhana (NB) bila kinerjanya memadai, dan arahkan upaya ke penyelidikan dan rekayasa fitur atau sumber data baru, bukan ke penyetelan tambahan.

**Pedoman skor**

| Bagian | Poin | Rincian |
|--------|------|---------|
| (i) | 2,5 | Syarat pertama diperiksa dengan angka ($2\cdot SE = 0{,}0154 < 0{,}0172$) 0,5 · syarat kedua: hanya 3 dari 5 lipatan searah 0,75 · kesimpulan "belum dapat disimpulkan/tidak bermakna" 0,5 · tindak lanjut: pilih yang lebih sederhana, atau selidiki mengapa selisih hanya muncul pada L1–L3 sebelum memutuskan 0,75 |
| (ii) | 2,5 | Kedua pasangan tidak bermakna, dengan alasan dari salah satu syarat 0,75 · sumber keterbatasan (diminta batang soal): kemungkinan besar fitur/sinyal data, bukan algoritma 0,75 · tindak lanjut: pilih model sederhana (NB) 0,5 + arahkan upaya ke fitur/data 0,5 |

Alternatif yang diterima: pada (i), "pilih HistGB bila biaya dan keterjelasan tidak menjadi soal, tetapi laporkan bahwa keunggulannya belum terbukti" dinilai penuh pada tindak lanjut. Menghitung ulang $SE$ dari $d_i$ (0,0077 atau 0,0076) tidak dituntut dan tidak menambah skor.

**Contoh jawaban**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "(i) Benar, $\bar d$ lebih besar dari $2\cdot SE$. (ii) SVM terbaik karena reratanya tertinggi." | 0 |
| Cukup | "(i) $2\cdot SE$ = 0,0154 < 0,0172, tetapi L4 dan L5 negatif, jadi tidak bermakna. (ii) Keduanya tidak bermakna karena $\bar d$ < $2\cdot SE$; pakai NB." | 3,0 (i 1,75 — tindak lanjut tidak ada · ii 1,25 — sumber keterbatasan tidak ada; tindak lanjut tanpa fitur/data 0,5) |
| Baik | "(i) $2\cdot SE$ = 0,0154 < 0,0172, syarat pertama terpenuhi, tetapi $d_i$ positif hanya pada L1–L3 (3 dari 5), jadi belum dapat disimpulkan HistGB lebih baik. Pilih regresi logistik yang lebih sederhana. (ii) Keduanya tidak bermakna (searah 3/5 dan 2/5). Model kompleks tidak mengungguli NB padahal semuanya jauh di atas *baseline*, jadi kemungkinan besar pembatasnya fitur, bukan algoritma. Pakai NB dan perbaiki fitur atau cari data baru." | 5 |

**Pelajari ulang:** [Bab 9 §9.4.2](../06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md#942-membaca-hasil-perbandingan) (aturan berpasangan dan "pilih yang sederhana"), [§9.2.2](../06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md#922-varian) (Naive Bayes sebagai pembanding cepat); [Lab 10 Tantangan 4](../04-labs/lab-10-svm-naive-bayes-penyetelan.md#tantangan-4--uji-formal-corrected-resampled-t-test) (uji formal, nilai tambah); [Bab 14 §14.4.2](../06-buku-ajar/bab-14-proyek-akhir.md#1442-protokol-perbandingan).

---

### A3. Memilih Metode *Clustering* — `DAIML-Sub-CPMK082-1` · C4 · 5 poin

**Jawaban model** (Bab 10 §10.2.2, §10.4, §10.5)

| Kebutuhan | Karakteristik penentu | Metode | Alasan |
|-----------|-----------------------|--------|--------|
| (i) Titik longsor | Klaster **memanjang** (tidak bulat); **jumlah zona tidak diketahui**; ada **pencilan**; 1.800 titik | **DBSCAN** | Mengelompokkan menurut kerapatan sehingga bentuk klaster bebas; tidak perlu menetapkan k; titik terpencil ditandai sebagai derau, bukan dipaksa masuk zona. K-Means mengandaikan klaster bulat, sehingga deret memanjang terpotong menjadi gumpalan. Catatan: `eps` peka dan perlu ditentukan (mis. grafik *k-distance*) |
| (ii) Segmen pengguna | **2,4 juta** baris; **k ditetapkan kebutuhan** (5 paket); fitur sudah diskalakan | **K-Means** | Berskala baik pada data besar dan k dapat ditetapkan langsung sesuai lima paket (kriteria kebermaknaan); pusat klaster memberi profil segmen. *Hierarchical* berkompleksitas $O(n^2)$–$O(n^3)$, tidak layak untuk 2,4 juta baris; DBSCAN tidak dapat diminta menghasilkan tepat lima segmen. Periksa pencilan nilai transaksi yang dapat menarik pusat |

**Pedoman skor:** per kebutuhan 2,5 = karakteristik penentu 1,0 (sekurang-kurangnya dua yang relevan, seperti diminta batang soal; satu saja 0,5) · metode 0,5 · alasan yang mengaitkan sifat metode dengan karakteristik itu 1,0 (satu sifat 0,5).

Alternatif yang diterima: pada (i), *hierarchical clustering* dengan *single linkage* (klaster memanjang; 1.800 titik masih layak) = metode 0,25, karena pencilan tetap dipaksa masuk klaster; alasan dinilai menurut isinya. Pada (ii), "K-Means pada subsampel lalu menetapkan seluruh pengguna ke pusat terdekat" dinilai penuh.

**Contoh jawaban**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "(i) K-Means dengan *elbow*. (ii) *Hierarchical* agar ada dendrogram." | 0 |
| Cukup | "(i) Jumlah zona tidak diketahui: DBSCAN, karena tidak perlu menentukan k. (ii) Datanya besar: K-Means, karena cepat." | 3,0 (per kebutuhan: satu karakteristik 0,5 · metode 0,5 · satu sifat metode 0,5) |
| Baik | "(i) Zona memanjang mengikuti sungai, jumlahnya tidak diketahui, ada titik terpencil: DBSCAN — bentuk klaster bebas, tanpa k, pencilan menjadi derau; K-Means akan memotong deret itu menjadi gumpalan bulat. (ii) 2,4 juta pengguna dan k sudah ditetapkan 5: K-Means — cepat pada data besar dan k dapat ditetapkan; *hierarchical* terlalu berat dan DBSCAN tidak dapat diminta tepat lima segmen." | 5 |

**Pelajari ulang:** [Bab 10 §10.2.2](../06-buku-ajar/bab-10-pembelajaran-tanpa-supervisi.md#1022-asumsi-dan-batasnya) (asumsi K-Means), [§10.4](../06-buku-ajar/bab-10-pembelajaran-tanpa-supervisi.md#104-hierarchical-clustering), [§10.5.1](../06-buku-ajar/bab-10-pembelajaran-tanpa-supervisi.md#1051-perbandingan-ketiga-metode) (perbandingan ketiga metode), [§10.3.3](../06-buku-ajar/bab-10-pembelajaran-tanpa-supervisi.md#1033-kriteria-ketiga-yang-paling-menentukan) (kebermaknaan k).

---

### A4. Membeli Data Tambahan? — `DAIML-Sub-CPMK102-1` · C4 · 5 poin

**Jawaban model** (Bab 11 §11.3.1–§11.3.2)

| Tim | Diagnosis dan bukti | Beli data? | Tindakan |
|-----|---------------------|------------|----------|
| P | **Kurang data** (baris "selisih mengecil tetapi belum mendatar" pada tabel Bab 11 §11.3.1): selisih latih–validasi menyempit dari 0,35 ke 0,11, dan validasi **masih naik** ±0,05–0,07 setiap data digandakan. Selisih 0,11 masih tanda *overfit* (varians tinggi; ≥ 0,10, ambang praktis `diagnosis_kurva` Lab 12), tetapi terus menyempit — varians itu masih turun bila data bertambah. Kedua tanda itu sebaiknya disebut, seperti diagnosis kurva pohon tanpa batas pada Lab 12 Langkah 5 | **Ya** — kurva validasi belum mendatar, jadi data tambahan kemungkinan masih menaikkan kinerja | Beli; sambil itu regularisasi dapat diperkuat |
| Q | ***Underfit***: latih 0,68 dan validasi 0,67 rendah, berdekatan, dan **mendatar** sejak 2.000 baris | **Tidak** — kurva sudah datar; data tambahan tidak akan banyak membantu | Tambah fitur informatif, pakai model yang lebih kompleks, atau kurangi regularisasi |

**Pedoman skor**

| Bagian | Poin | Rincian |
|--------|------|---------|
| Tim P | 2,5 | Diagnosis "kurang data" atau "*overfit*/varians tinggi" 0,5 (keduanya penuh) · bukti dengan angka dari tabel: selisih menyempit (0,35 → 0,11) dan/atau validasi naik (0,64 → 0,82) 0,75; selisih latih–validasi pada satu ukuran saja, tanpa tren 0,25 · keputusan membeli 0,5 · alasan dari tren validasi (kurva validasi belum mendatar, jadi data tambahan masih menaikkan kinerja) 0,75 |
| Tim Q | 2,5 | Diagnosis *underfit* 0,5 dengan bukti dari tabel 0,5 · keputusan tidak membeli 0,25 dengan alasan kurva datar 0,5 · tindakan yang lebih tepat 0,75 |

Bukti dan alasan dinilai terpisah menurut kaidah "satu pernyataan, satu unsur" (§0): bukti menuntut angka dari tabel (diminta batang soal: "diagnosis dengan bukti angka dari tabel"); alasan menuntut kaitan tren kurva dengan manfaat data tambahan.

Alternatif yang diterima: pada P, diagnosis "kurang data (selisih mengecil, validasi belum mendatar)" — istilah tabel Bab 11 §11.3.1 — dan "*overfit* yang selisihnya menyempit" sama-sama dinilai penuh; "beli bila biaya sepadan dengan kenaikan ±0,05 yang diperkirakan" dinilai penuh pada keputusan. Pada Q, diagnosis "pas tetapi rendah" dengan alasan yang sama dinilai penuh pada diagnosis.

**Contoh jawaban**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "P: model sudah bagus karena latih 0,93, tidak perlu data. Q: beli data agar F1 naik." | 0 |
| Cukup | "P: *overfit*, latih 0,93 jauh di atas validasi 0,82; beli data karena validasi masih naik. Q: *underfit*; jangan beli karena kurvanya datar." | 3,25 (P 2,0 — diagnosis 0,5 · bukti selisih pada satu ukuran tanpa tren 0,25 · keputusan 0,5 · "validasi masih naik" sebagai alasan 0,75 · Q 1,25 — diagnosis 0,5 · bukti angka tidak ada · keputusan 0,25 · alasan 0,5 · tindakan tidak ada) |
| Baik | "P: kurang data — selisih menyempit dari 0,35 ke 0,11 dan validasi masih naik ±0,05 tiap data digandakan; kurva validasi belum mendatar, jadi data tambahan masih membantu: beli. Q: *underfit* — latih 0,68 dan validasi 0,67 rendah, berdekatan, datar sejak 2.000 baris; data tambahan tidak membantu, jangan beli; tambah fitur atau pakai model yang lebih kompleks." | 5 |

**Pelajari ulang:** [Bab 11 §11.3.1](../06-buku-ajar/bab-11-reduksi-dimensi-dan-visualisasi.md#1131-tiga-pola-dan-diagnosisnya) (pola dan diagnosis), [§11.3.2](../06-buku-ajar/bab-11-reduksi-dimensi-dan-visualisasi.md#1132-pertanyaan-berbiaya-nyata) ("apakah menambah data akan membantu?"); [Lab 12 Langkah 5](../04-labs/lab-12-pca-dan-visualisasi-model.md#langkah-5-kurva-pembelajaran) (kurva yang menunjukkan tanda *overfit* sekaligus kurang data).

---

### A5. PCA dan t-SNE dalam Laporan Model — `DAIML-Sub-CPMK102-1` · C4 · 5 poin

**Jawaban model** (Bab 11 §11.1.2, §11.2, §11.2.1)

| Keputusan | Masalah | Perbaikan |
|-----------|---------|-----------|
| (i) PCA → regresi logistik | PCA **mengganti** ke-30 fitur dengan kombinasi linear; koefisien model melekat pada PC1–PC6, yang masing-masing campuran seluruh fitur. Koefisien itu memang dapat diproyeksikan balik ke fitur asli lewat *loading* (bobot tiap fitur = jumlah *loading* × koefisien komponen), tetapi bobot hasil proyeksi itu tidak dipilih untuk menjelaskan: hampir setiap fitur ikut mendapat bobot, fitur yang berkorelasi berbagi bobot, dan 10% varians dibuang tanpa melihat target. Alasan penolakan per klaim menjadi tidak langsung dan sulit dipertanggungjawabkan kepada petani dalam fitur asli (mis. luas lahan, curah hujan), padahal petani berhak atas penjelasan. Lagi pula 90% varians fitur bukan jaminan 90% informasi tentang target | Regresi logistik (atau pohon dangkal) pada fitur asli yang dipilih — dengan pemilihan fitur atau regularisasi — sehingga setiap alasan dapat ditunjukkan; PCA cukup dipakai untuk eksplorasi |
| (ii) t-SNE | (1) **Jarak antarklaster pada t-SNE tidak bermakna** — tidak dapat disimpulkan "sangat berbeda", dan klaster yang tampak dapat berubah dengan `perplexity`. (2) **t-SNE bukan prapemrosesan model**: pemetaannya tidak dapat diterapkan pada klaim baru (tabel Bab 11 §11.2), sehingga fitur itu tidak tersedia saat model dipakai | Buang koordinat t-SNE dari fitur. Periksa perbedaan kedua kelompok dengan cara lain: bandingkan profil fitur asli antarkelompok, atau ukur kinerja model per kelompok |

**Pedoman skor**

| Bagian | Poin | Rincian |
|--------|------|---------|
| (i) | 2,5 | Masalah: keterjelasan hilang 0,5 karena komponen adalah campuran seluruh fitur 0,75 ("PCA mengurangi informasi" saja 0,25) · perbaikan: tinggalkan PCA pada model akhir 0,5 + model pada fitur asli yang dapat ditafsirkan 0,75 |
| (ii) | 2,5 | Jarak antarklaster t-SNE tidak bermakna 0,75 · t-SNE tidak layak sebagai fitur (klaim baru tidak dapat dipetakan, atau hasil bergantung `perplexity`) 0,75 · perbaikan: buang fitur itu 0,5 + verifikasi perbedaan dengan cara lain 0,5 |

Alternatif yang diterima: pada (i), argumen bahwa koefisien komponen dapat diproyeksikan balik ke fitur asli lewat *loading* ($W^\top\beta$), disertai keterbatasannya — bobot campuran yang tidak dipilih untuk menjelaskan, fitur berkorelasi berbagi bobot, sehingga alasan per klaim tidak langsung — dinilai penuh pada unsur masalah.

**Contoh jawaban**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "(i) Bagus karena 90% varians tetap. (ii) Bagus, t-SNE menunjukkan perbedaan yang jelas." | 0 |
| Cukup | "(i) PCA membuat model sulit dijelaskan; jangan pakai PCA. (ii) Jarak pada t-SNE tidak bermakna; buang fitur t-SNE." | 2,25 (i 1,0 — mengapa sulit dijelaskan dan model penggantinya tidak ada · ii 1,25 — alasan tidak layak sebagai fitur dan verifikasi tidak ada) |
| Baik | "(i) Koefisien melekat pada komponen, campuran ke-30 fitur; proyeksi balik hanya memberi bobot campuran, jadi alasan penolakan sulit dijelaskan kepada petani. Pakai regresi logistik pada fitur asli terpilih; PCA cukup untuk eksplorasi. (ii) Jarak antarklaster t-SNE tidak bermakna, dan t-SNE tidak dapat memetakan klaim baru, jadi tidak layak menjadi fitur. Buang fitur itu; bandingkan profil fitur asli kedua kelompok." | 5 |

**Pelajari ulang:** [Bab 11 §11.1.2](../06-buku-ajar/bab-11-reduksi-dimensi-dan-visualisasi.md#1112-apa-yang-diperoleh-dan-apa-yang-hilang) (PCA bukan pemilihan fitur), [§11.2](../06-buku-ajar/bab-11-reduksi-dimensi-dan-visualisasi.md#112-t-sne-dan-umap) (t-SNE tidak dapat diterapkan ke data baru dan tidak disarankan sebagai prapemrosesan model), [§11.2.1](../06-buku-ajar/bab-11-reduksi-dimensi-dan-visualisasi.md#1121-tiga-kekeliruan-membaca-t-sne) (tiga kekeliruan membaca t-SNE); [Bab 13 §13.4](../06-buku-ajar/bab-13-ai-generatif-dan-ai-bertanggung-jawab.md#134-explainability) (model yang dapat ditafsirkan).

---

## 2. Bagian B — Perancangan Solusi (45 poin)

### B1. Paket COD yang Ditolak Penerima — `DAIML-Sub-CPMK082-1` (a, d, e, f) dan `DAIML-Sub-CPMK102-1` (b, c) · C6 (a, e), C4 (b, c), C5 (d, f) · 22,5 poin

**(a) Formulasi *task*** — `082-1` · C6 · 2,5 poin

Contoh: *"1 bila paket COD pesanan itu **ditolak penerima** sehingga dikembalikan ke penjual, diamati sampai status akhir pengiriman (paling lama 14 hari sejak pesanan dibuat); 0 bila diterima dan dibayar."* Jenis *task*: **klasifikasi biner**; probabilitasnya dipakai untuk menandai pesanan. Prediksi dibutuhkan **saat penjual membuat pesanan pengiriman**, sebelum paket dijemput — telepon konfirmasi harus terjadi sebelum ongkos kirim terpakai, sehingga hanya informasi yang ada pada saat itu yang boleh dipakai.

| Unsur | Poin |
|-------|------|
| Peristiwa yang dihitung (ditolak penerima, dikembalikan ke penjual) | 0,5 |
| Batas waktu pengamatan (status akhir, mis. ≤ 14 hari sejak pesanan) | 0,5 |
| Jenis *task* (klasifikasi biner; "pemeringkatan risiko" juga benar) | 0,5 |
| Saat prediksi: saat pesanan pengiriman dibuat/sebelum dijemput = 1,0; "sebelum diantar" tanpa menyebut sebelum penjemputan = 0,5; saat paket tiba di gudang tujuan atau sesudahnya = 0 | 1,0 |

Alternatif yang diterima: klasifikasi tiga kelas (diterima, ditolak, gagal diantar karena penerima tidak dapat dihubungi) dinilai penuh bila setiap kelas didefinisikan.

**(b) Kolom yang tidak boleh dipakai** — `102-1` · C4 · 2,5 poin

| Kolom | Alasan |
|-------|--------|
| `jumlah_percobaan_antar` | Baru diketahui **saat pengantaran**, sesudah saat prediksi, dan nilainya terkait erat dengan hasil pengantaran itu sendiri — kebocoran temporal/target |
| `balas_konfirmasi_otomatis` | Pesannya baru dikirim **ketika paket tiba di gudang kota tujuan**, sesudah paket dijemput — informasi masa depan (kebocoran temporal) |

Pengecoh yang sah: `riwayat_tolak_pembeli` dihitung dari pesanan **sebelum** tanggal pesanan, jadi tersedia saat prediksi (nilai tambah: pastikan data latih menghitungnya dengan batas waktu yang sama).

**Pedoman skor:** per kolom 1,25 = kolom 0,5 · alasan 0,75 (nilainya belum ada saat pesanan dibuat/informasi sesudah saat prediksi; "bocor" tanpa mekanisme 0,25). Nama jenis kebocoran tidak diminta. Hanya dua kolom pertama yang ditulis yang dinilai; kolom sah yang disebut terlarang bernilai 0. Batang soal meminta kolom yang menimbulkan kebocoran data; kolom yang ditolak karena alasan etis (mis. `kecamatan_tujuan` sebagai proksi wilayah) bukan kebocoran: bernilai 0 di sini dan argumennya dinilai pada (f).

**(c) Dampak kesalahan dan metrik** — `102-1` · C4 · 2,5 poin

- **FN** (paket yang akan ditolak tidak ditandai): perusahaan menanggung ongkos kirim pulang-pergi ±Rp38.000, dan stok penjual tertahan ±10 hari.
- **FP** (pesanan wajar ditandai): biaya telepon ±Rp3.000, dan sebagian pembeli jujur membatalkan pesanan — penjual kehilangan penjualan, pembeli terganggu.
- Per kejadian FN jauh lebih mahal (±12,7 kali biaya telepon bila pembatalan diabaikan), tetapi FP tidak gratis karena pembatalan.
- Metrik: ***recall* kelas "ditolak" dengan batas *precision* minimum** (membatasi telepon sia-sia dan pembatalan), dengan ambang dipilih dari total biaya kesalahan pada data validasi; PR-AUC untuk membandingkan peringkat model. Akurasi tidak sesuai: tidak menandai pesanan apa pun sudah memberi akurasi 0,91.

| Unsur | Poin |
|-------|------|
| Dampak FN yang konkret | 0,5 |
| Dampak FP yang konkret (biaya telepon dan/atau pembatalan) | 0,5 |
| Mana yang lebih berat beserta alasannya | 0,25 |
| Metrik yang dikaitkan dengan perbandingan itu: *recall* dengan batas *precision*, total biaya/ambang dari biaya, atau PR-AUC beserta penentuan ambang = 1,25; *recall* tanpa batas *precision* atau tanpa menyebut kelas = 0,75; F1 tanpa kaitan dengan biaya yang tidak setara = 0,5; akurasi = 0 | 1,25 |

**(d) Model kandidat** — `082-1` · C5 · 4,5 poin

| Kandidat | Argumentasi yang dikaitkan dengan kasus |
|----------|----------------------------------------|
| *Gradient boosting* (mis. `HistGradientBoostingClassifier`) | Data tabular campuran 480.000 baris; versi berbasis histogram cepat pada data sebesar ini; menangkap interaksi (mis. nilai barang × kategori × jam pesan); sering terbaik pada data tabular |
| *Random Forest* | Dapat dilatih paralel pada 480.000 baris, tidak peka pencilan `nilai_barang`, dan tidak menuntut banyak penyetelan; pembanding *ensemble* yang stabil |
| Regresi logistik | Sederhana dan cepat; probabilitasnya dapat dipakai untuk menentukan ambang dari biaya; mudah dijelaskan kepada penjual dan petugas |
| Naive Bayes (diterima) | Pembanding sangat cepat; bila model kompleks tidak mengunggulinya, kemungkinan besar masalahnya ada pada fitur (Bab 9 §9.2.2) |

Kurang sesuai tanpa penanganan: SVM RBF ($O(n^2)$–$O(n^3)$ pada 480.000 baris), k-NN (prediksi lambat; jarak pada ±7.000 kategori kecamatan). Jaringan saraf tiruan (`MLPClassifier`) **diterima sebagai model**: dapat dilatih pada data sebesar ini, tetapi pada data tabular umumnya tidak mengungguli *gradient boosting*, penyetelannya lebih banyak, dan lebih sulit dijelaskan ([Bab 12 §12.6](../06-buku-ajar/bab-12-pengantar-jaringan-saraf-tiruan.md#126-kapan-jst-tidak-diperlukan)). Nilai tambah: `kecamatan_tujuan` berkardinalitas tinggi ditangani dengan *target encoding* yang di-*cross-fit* atau digabung ke kabupaten (Bab 3 §3.4.2).

**Pedoman skor:** per kandidat 1,5 = model yang sesuai 0,5 · alasan yang dikaitkan dengan sifat data atau kebutuhan kasus ini 1,0 (alasan benar tetapi umum, mis. "sederhana", "kuat" = 0,5; "akurat", "populer", "canggih" = 0,25). Kandidat yang tidak sesuai tanpa penanganan (SVM RBF, k-NN) = model 0, alasan dinilai menurut isinya; dengan penanganan yang sah (mis. `LinearSVC`, subsampel) dinilai penuh bila alasannya tepat. **Jaringan saraf tiruan** (termasuk "*deep learning*") = model 0,5; alasannya dinilai menurut isinya — "canggih" atau "data besar/banyak" = 0,25. Lebih dari tiga kandidat: dinilai tiga yang terbaik.

**(e) Protokol evaluasi** — `082-1` · C6 · 5,5 poin

1. **Pembagian temporal:** latih Januari–Desember 2025, uji Januari–Juni 2026, dipakai sekali di akhir. Model dipakai untuk pesanan masa depan, dan pola penolakan berubah menurut waktu (musim belanja, promosi); pembagian acak per baris juga menempatkan pesanan yang lebih baru dari pembeli yang sama di data latih.
2. **Validasi dan penyetelan** hanya pada data latih, dengan validasi silang berurutan waktu (mis. 5 lipatan maju; bila memakai validasi bersarang, lipatan luar dan dalamnya juga berurutan waktu); seluruh prapemrosesan, termasuk penyandian kecamatan, di dalam `Pipeline`.
3. **Membandingkan kandidat:** semua kandidat dinilai pada **lipatan yang sama** dengan metrik (c); dua teratas dibandingkan dengan selisih berpasangan per lipatan — bermakna bila $\lvert\bar d\rvert > 2\cdot SE$ **dan** searah pada sebagian besar lipatan (pada 5 lipatan: minimal 4); bila tidak, pilih yang lebih sederhana.
4. ***Baseline*:** aturan yang dapat dijalankan saat pesanan dibuat, mis. "tandai pembeli dengan `riwayat_tolak_pembeli` ≥ 1" (atau aturan yang berlaku sekarang).

| Unsur | Poin |
|-------|------|
| Pembagian (alasannya diminta batang soal): temporal dengan alasan = 1,5; temporal tanpa alasan = 1,0; berkelompok per pembeli tanpa urutan waktu = 0,75; acak per baris (termasuk bertingkat) = 0 | 1,5 |
| Validasi dan penyetelan: hanya pada data latih 0,5 · validasi silang berurutan waktu (termasuk validasi bersarang dengan lipatan berurutan waktu) 0,5; validasi silang atau bersarang tanpa urutan waktu (termasuk *GridSearchCV* dengan lipatan bawaan) 0,25 · data uji dipakai sekali 0,25 | 1,25 |
| Membandingkan: lipatan sama untuk semua kandidat 0,5 · selisih berpasangan dengan kedua syarat aturan praktis 1,0 (hanya $\lvert\bar d\rvert > 2\cdot SE$ tanpa syarat arah 0,5; membandingkan rerata atau rerata ± simpangan 0) | 1,5 |
| *Baseline* yang paling bermakna (diminta batang soal): aturan sederhana yang dapat dijalankan saat pesanan dibuat, atau sistem yang berlaku sekarang = 1,25; kelas terbanyak saja = 0,75 — *baseline* yang sah (Bab 2 §2.4.1), tetapi bukan yang paling bermakna di sini: tidak menandai pesanan apa pun, sehingga *recall*-nya 0; tetap berguna sebagai acuan biaya | 1,25 |

**(f) Dua risiko etis** — `082-1` · C5 · 5 poin

Cukup dua; contoh yang diterima:

| Risiko | Siapa dirugikan dan bagaimana | Penanganan |
|--------|-------------------------------|------------|
| Proksi wilayah | `kecamatan_tujuan` membawa informasi tingkat ekonomi dan akses perbankan. Pembeli di daerah terpencil atau berpenghasilan rendah — yang paling bergantung pada COD karena tidak memiliki rekening — lebih sering ditandai, ditelepon, dan sebagian batal, sehingga akses belanja daring mereka berkurang | Audit per kelompok wilayah: proporsi pesanan ditandai, FPR (pembeli jujur yang ditelepon), dan *recall*. Pilih ukuran *fairness* yang dipakai — mis. FPR setara antarwilayah — dan nyatakan pengorbanannya: bila *base rate* penolakan berbeda antarwilayah, tidak ada pengklasifikasi yang berguna (non-trivial) yang dapat memenuhi semua ukuran sekaligus |
| Label selektif dan umpan balik | Pesanan yang ditandai lalu dibatalkan tidak pernah diketahui hasilnya; pada pelatihan ulang, kelompok yang paling sering ditandai kehilangan label, sehingga kesalahan model pada kelompok itu tidak terlihat dan dapat menguat | Sisihkan sampel acak kecil pesanan berisiko yang tidak ditelepon untuk mengukur kinerja sebenarnya; catat pembatalan akibat telepon secara terpisah |
| Cap dan jalur keberatan | Pembeli tidak tahu mengapa dicurigai; cap "pembeli bermasalah" melekat lintas toko | Petugas tidak menyebut "berisiko tinggi"; riwayat penolakan kedaluwarsa setelah periode tertentu; jalur keberatan |
| Privasi | Riwayat penolakan lintas toko dipakai tanpa diketahui pembeli | Batasi akses dan masa simpan; nyatakan dalam kebijakan privasi |

**Pedoman skor:** per risiko 2,5 = risiko konkret (siapa dirugikan dan mekanisme khas kasus ini) 1,5 — siapa dirugikan disebut tetapi mekanismenya tidak lengkap 1,0; risiko umum tanpa mekanisme (mis. "bias", "privasi") 0,5 · penanganan yang konkret, dapat dijalankan, dan menyasar risiko itu 1,0 (mis. "audit per wilayah" untuk risiko wilayah, "sisihkan sampel acak yang tidak ditelepon" untuk label selektif) — penanganan umum yang tidak khas risiko itu (mis. "pastikan adil", "enkripsi data", "libatkan manusia", "perbaiki data") 0,5; penanganan yang tidak menjawab risikonya 0. Dua risiko dengan mekanisme yang sama dihitung satu.

Dalam kerangka nilai program studi, audit per kelompok dan jalur keberatan adalah wujud *al-'adl* dan *la darar* ([Bab 13 §13.2.2](../06-buku-ajar/bab-13-ai-generatif-dan-ai-bertanggung-jawab.md#1322-model-akurat-yang-tetap-merugikan)): sistem yang memengaruhi akses orang pada layanan harus bekerja setara, dan dampak buruknya pada kelompok mana pun harus diketahui dan dipertanggungjawabkan.

**Contoh jawaban B1 (keseluruhan)**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "(a) Memprediksi paket ditolak. (b) `ongkir` dan `kecamatan_tujuan`. (c) Akurasi, karena paling umum. (d) *Deep learning* karena datanya besar; SVM; KNN. (e) *Split* 70/30. (f) AI bisa salah." | 1,25 (a 0,5 — peristiwa saja · d 0,75 — jaringan saraf ("*deep learning*") model 0,5 + alasan "data besar" 0,25; SVM dan KNN tanpa alasan dan tanpa penanganan 0 · butir lain 0) |
| Cukup | "(a) Target: paket ditolak atau tidak; klasifikasi. Prediksi sebelum paket diantar. (b) `jumlah_percobaan_antar` karena terjadi setelah pesanan; `riwayat_tolak_pembeli` karena memakai data target. (c) Paket ditolak lebih merugikan karena ongkir hilang; pakai F1. (d) *Random Forest* karena akurat; regresi logistik sebagai pembanding sederhana; HistGB karena data 480.000 baris dan tabular. (e) Bagi acak 80/20 bertingkat; GridSearchCV pada data latih; bandingkan rerata F1; *baseline* kelas terbanyak. (f) Bias terhadap wilayah tertentu; audit per wilayah. Privasi data pembeli; enkripsi." | 11,25 (a 1,5 — batas waktu tidak ada; "sebelum diantar" 0,5 · b 1,25 — kolom kedua sah · c 1,25 — dampak FP tidak ada; F1 tanpa kaitan 0,5 · d 3,25 — RF alasan "akurat" 0,25; logistik alasan umum 0,5; HistGB penuh · e 1,5 — pembagian acak 0; penyetelan pada data latih 0,5 + *GridSearchCV* tanpa urutan waktu 0,25; rerata 0; kelas terbanyak 0,75 · f 2,5 — kedua risiko umum 0,5 · "audit per wilayah" penanganan konkret 1,0 · "enkripsi" penanganan umum 0,5) |
| Baik | "(a) 1 bila paket ditolak penerima dan dikembalikan ke penjual, diamati sampai status akhir (≤ 14 hari sejak pesanan); 0 bila diterima. Klasifikasi biner. Prediksi saat penjual membuat pesanan pengiriman, sebelum dijemput. (b) `jumlah_percobaan_antar`: baru diketahui saat pengantaran. `balas_konfirmasi_otomatis`: pesannya baru dikirim saat paket tiba di gudang tujuan. Keduanya informasi masa depan. (c) FN: ongkir pulang-pergi Rp38.000 dan stok tertahan 10 hari. FP: telepon Rp3.000 dan sebagian pembeli jujur batal. FN lebih mahal. Metrik: *recall* kelas ditolak dengan batas *precision* minimum; ambang dipilih dari total biaya. (d) HistGB: 480.000 baris tabular, cepat, menangkap interaksi nilai × kategori. *Random Forest*: dapat dilatih paralel pada 480.000 baris dan tidak peka pencilan `nilai_barang`. Regresi logistik: probabilitasnya untuk ambang biaya, mudah dijelaskan ke penjual. (e) Latih 2025, uji Januari–Juni 2026 sekali, karena model dipakai untuk pesanan mendatang. Penyetelan dengan CV berurutan waktu di data latih. Semua kandidat pada lipatan yang sama; dua teratas dibandingkan berpasangan: $\lvert\bar d\rvert > 2\cdot SE$ dan searah ≥ 4 dari 5 lipatan. *Baseline*: tandai pembeli dengan riwayat tolak ≥ 1. (f) Kecamatan menjadi proksi daerah miskin/terpencil: pembeli di sana, yang paling bergantung pada COD, lebih sering ditelepon dan batal. Tangani: audit FPR dan proporsi ditandai per wilayah, pilih ukuran *fairness* dan nyatakan pengorbanannya. Pesanan yang ditandai lalu batal tak pernah berlabel, sehingga kesalahan pada kelompok itu tidak terlihat. Tangani: sisihkan sampel acak yang tidak ditelepon untuk memantau kinerja." | 22,5 |

**Pelajari ulang:** [Bab 2 §2.1.1–§2.1.2](../06-buku-ajar/bab-02-formulasi-masalah-daur-hidup-ml.md#211-tujuh-pertanyaan-formulasi) (formulasi dan unsur target), [§2.3](../06-buku-ajar/bab-02-formulasi-masalah-daur-hidup-ml.md#23-memilih-metrik-dari-dampak-kesalahan) (metrik dari dampak kesalahan); [Bab 4 §4.5.2](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md#452-kebocoran-temporal) (kebocoran temporal), [§4.3.1](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md#431-pembagian-temporal) (pembagian temporal); [Bab 7 §7.4.1](../06-buku-ajar/bab-07-klasifikasi-dan-metriknya.md#741-menentukan-ambang-dari-biaya) (ambang dari biaya); [Bab 8 §8.3.4](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md#834-perbandingan) dan [Bab 9 §9.4](../06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md#94-merancang-perbandingan-yang-adil) (pemilihan model, perbandingan adil); [Bab 13 §13.3](../06-buku-ajar/bab-13-ai-generatif-dan-ai-bertanggung-jawab.md#133-mengukur-fairness) dan [§13.2.1](../06-buku-ajar/bab-13-ai-generatif-dan-ai-bertanggung-jawab.md#1321-enam-sumber) (*fairness*, sumber *bias*).

---

### B2. Perkiraan Produktivitas Padi per Desa — `DAIML-Sub-CPMK082-1` (a, d, e, f) dan `DAIML-Sub-CPMK102-1` (b, c) · C6 (a, e), C4 (b, c), C5 (d, f) · 22,5 poin

**(a) Formulasi *task*** — `082-1` · C6 · 2,5 poin

Contoh: *"Produktivitas padi desa pada musim berjalan, dalam ton gabah kering panen per hektare, diukur dengan survei ubinan saat panen."* Jenis *task*: **regresi**. Prediksi dibutuhkan pada **minggu ke-10 sejak tanam** (16 − 6), sehingga hanya data sampai minggu ke-10 yang boleh dipakai.

| Unsur | Poin |
|-------|------|
| Besaran dan satuan (ton GKP/ha, per desa per musim); besaran tanpa satuan = 0,25 | 0,5 |
| Cara dan waktu pengukuran (survei ubinan saat panen) | 0,5 |
| Jenis *task*: regresi | 0,5 |
| Saat prediksi: minggu ke-10 = 1,0; "6 minggu sebelum panen" tanpa dinyatakan dalam minggu sejak tanam = 0,5 | 1,0 |

Alternatif yang diterima: "regresi; untuk pemakaian prioritas bantuan, hasilnya diambangkan (mis. di bawah 4,5 ton/ha)" dinilai penuh. Klasifikasi biner saja dengan ambang yang dikaitkan dengan prioritas bantuan = 0,25 pada jenis *task*, karena pemakaian serapan gabah membutuhkan angka.

**(b) Kolom yang tidak boleh dipakai** — `102-1` · C4 · 2,5 poin

| Kolom | Alasan |
|-------|--------|
| `produksi_ton` | Dicatat **saat panen**, dan produksi = produktivitas × luas panen, jadi memuat target — kebocoran target dan temporal |
| `indeks_hijau_m11` … `indeks_hijau_m16` (juga diterima: `m10`–`m16`) | Pada minggu ke-10 citra minggu ke-11 sampai ke-16 **belum ada** — informasi masa depan (kebocoran temporal) |

Pengecoh yang sah: `rerata_produktivitas_3_musim_lalu` (masa lalu), `pupuk_tersalur_kg_ha` (sampai minggu ke-6), `luas_tanam_ha` (diketahui sejak tanam), `hujan_kumulatif_8_minggu`.

**Pedoman skor:** per kolom atau kelompok kolom 1,25 = kolom 0,5 · alasan 0,75 ("bocor" tanpa mekanisme 0,25). Menyebut seluruh `indeks_hijau_m1`–`m16` = kolom 0,25 (hanya sebagiannya terlarang); alasannya penuh bila menyebut minggu sesudah minggu ke-10. Soal tidak menyatakan apakah citra minggu ke-10 sudah tersedia saat keputusan diambil, sehingga `m10`–`m16` dengan alasan bahwa citra minggu keputusan belum tentu lengkap juga dinilai penuh. Hanya dua kolom atau kelompok pertama yang ditulis yang dinilai; kolom sah yang disebut terlarang bernilai 0.

**(c) Dampak kesalahan dan metrik** — `102-1` · C4 · 2,5 poin

- **Terlalu tinggi:** BUMD menyiapkan gudang dan dana melebihi kebutuhan (biaya menganggur), dan desa itu tidak diprioritaskan bantuan benih padahal hasilnya rendah — petani yang paling membutuhkan tidak terbantu.
- **Terlalu rendah:** kapasitas serapan kurang, sehingga gabah petani tidak terserap dan dijual murah ke tengkulak; desa diprioritaskan bantuan padahal tidak perlu (anggaran tidak tepat sasaran).
- Kedua arah merugikan pihak yang berbeda, sehingga arah galat perlu dilaporkan, bukan hanya besarnya; untuk serapan, yang penting galat **dalam ton** (galat ton/ha × luas tanam), bukan per hektare.
- Metrik: **MAE** (ton/ha, mudah dipahami dinas), dihitung juga dalam ton dengan bobot `luas_tanam_ha`; ditambah **rerata galat bertanda** (arah) dan galat **per kabupaten/kelompok desa**. Bila kekurangan serapan dinilai lebih mahal, galat terlalu rendah diberi bobot lebih besar (kerugian asimetris).

| Unsur | Poin |
|-------|------|
| Dampak perkiraan terlalu tinggi yang konkret | 0,5 |
| Dampak perkiraan terlalu rendah yang konkret | 0,5 |
| Perbandingan: mana yang lebih berat untuk pemakaian mana, atau mengapa arah galat harus dibedakan | 0,25 |
| Metrik utama yang dikaitkan dengan dampak: MAE/RMSE dengan alasan dari dampak = 0,75; MAE atau RMSE tanpa kaitan dengan dampak (alasan umum atau tanpa alasan) = 0,5; $R^2$ saja = 0,25 | 0,75 |
| Ukuran pelengkap yang memperlihatkan perbedaan dampak (diminta batang soal): ukuran **berarah** — rerata galat bertanda, galat terlalu tinggi dan terlalu rendah dilaporkan terpisah, atau galat bertanda dalam ton (galat × luas tanam) — = 0,5; ukuran tanpa arah — galat dalam ton tanpa tanda, atau galat per kelompok (mis. per kabupaten) — = 0,25 | 0,5 |

Ukuran pelengkap tidak menuntut metrik di luar Bab 6: rerata galat bertanda adalah rerata kolom *Galat* (masih bertanda, sebelum diambil nilai mutlaknya untuk MAE) pada perhitungan manual [Bab 6 §6.4.2](../06-buku-ajar/bab-06-regresi-dan-metriknya.md#642-perhitungan-manual). Kolom itu memakai galat = prediksi − sebenarnya ($\hat y - y$; 750 − 800 = −50), sehingga rerata **positif** berarti perkiraan cenderung **terlalu tinggi**; konvensi sebaliknya ($e = y - \hat y$, seperti pada Latihan UTS) sama benarnya bila dipakai konsisten. Batang soal meminta ukuran yang memperlihatkan perbedaan dampak perkiraan terlalu tinggi dan terlalu rendah, jadi hanya ukuran berarah yang bernilai penuh. Galat dalam ton (galat per hektare × luas tanam) memperlihatkan besarnya dampak pada serapan dan bernilai penuh bila bertanda. Kerugian asimetris adalah nilai tambah.

**(d) Model kandidat** — `082-1` · C5 · 4,5 poin

| Kandidat | Argumentasi yang dikaitkan dengan kasus |
|----------|----------------------------------------|
| Regresi Ridge | Kolom indeks mingguan berkorelasi sangat kuat; regularisasi menstabilkan koefisien; cepat; koefisiennya dapat dijelaskan kepada dinas |
| *Gradient boosting* (atau *Random Forest*) | Interaksi tak linear (irigasi × hujan × varietas) pada data tabular 19.200 baris; sering terbaik pada data tabular |
| PCA lalu Ridge (pada kolom indeks) | Meringkas kolom indeks yang tersedia (minggu 1–10) menjadi sedikit komponen yang tidak berkorelasi; harganya, keterjelasan per minggu hilang |
| Jaringan saraf tiruan (diterima sebagai model) | Dapat dicoba sebagai pembanding, tetapi pada data tabular 19.200 baris umumnya tidak mengungguli *gradient boosting*, penyetelannya lebih banyak, dan sulit dijelaskan kepada dinas — "paling canggih" bukan alasan |

**Pedoman skor:** sama dengan B1(d), termasuk aturan jaringan saraf tiruan: model 0,5; alasan "paling canggih" atau "datanya banyak" = 0,25 (19.200 baris tabular bukan alasan memilih jaringan saraf). Pohon keputusan dan *ensemble* pohon (*Random Forest*, *gradient boosting*) diterima sebagai model regresi tanpa menyebut versi regresinya, karena materinya menyebut agregasi rata-rata untuk regresi ([modul Minggu 9 §9.3.2](../03-modules/week-09-pohon-keputusan-dan-ensemble.md#932-bagging-dan-random-forest): "suara terbanyak (klasifikasi) atau rata-rata (regresi)"; [Bab 8 §8.3.2](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md#832-bagging-dan-random-forest)) dan menggambarkan *boosting* sebagai pohon yang memperbaiki residual ([§8.3.3](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md#833-boosting)). **SVM** hanya diajarkan sebagai pengklasifikasi (Bab 9 §9.1, `SVC`), sehingga "SVM" tanpa menyebut versi regresinya = model 0; SVR yang disebut dengan alasan yang tepat dinilai menurut aturan umum.

**(e) Protokol evaluasi** — `082-1` · C6 · 5,5 poin

1. **Pembagian per musim (temporal):** latih 2022–2024 (6 musim), uji dua musim 2025, dipakai sekali di akhir. Model dipakai untuk musim yang akan datang, dan desa-desa pada musim yang sama berbagi cuaca serta serangan hama; pembagian acak per baris menempatkan musim yang sama di latih dan uji, sehingga hasilnya terlalu optimistis.
2. **Validasi dan penyetelan** hanya pada data latih, dengan lipatan per musim (tinggalkan satu musim, atau lipatan maju menurut waktu); penskalaan, PCA, dan penyetelan α atau kedalaman pohon di dalam `Pipeline`.
3. **Membandingkan kandidat** pada lipatan musim yang sama, dengan selisih berpasangan per lipatan: bermakna bila $\lvert\bar d\rvert > 2\cdot SE$ **dan** searah pada sebagian besar lipatan (≥ 80%).
4. ***Baseline*:** `rerata_produktivitas_3_musim_lalu` — perkiraan yang dapat dibuat dinas tanpa model.

| Unsur | Poin |
|-------|------|
| Pembagian (alasannya diminta batang soal): per musim/temporal dengan alasan = 1,5; tanpa alasan = 1,0; berkelompok per desa tanpa urutan waktu = 0,5; acak per baris = 0 | 1,5 |
| Validasi dan penyetelan: seperti B1(e) — hanya pada data latih 0,5 · lipatan per musim atau maju menurut waktu (termasuk validasi bersarang dengan lipatan seperti itu) 0,5; validasi silang atau bersarang tanpa pengelompokan per musim atau urutan waktu (termasuk *GridSearchCV* dengan lipatan bawaan) 0,25 · data uji dipakai sekali 0,25 | 1,25 |
| Membandingkan: seperti B1(e) | 1,5 |
| *Baseline* yang paling bermakna (diminta batang soal): rerata tiga musim lalu atau produktivitas musim yang sama tahun lalu = 1,25; rerata seluruh data latih = 0,75 — *baseline* yang sah (Bab 2 §2.4.1), tetapi mengabaikan riwayat desa yang sudah tersedia tanpa model | 1,25 |

Pembagian berkelompok tanpa urutan waktu bernilai lebih rendah di sini (per desa, 0,5) daripada pada B1(e) (per pembeli, 0,75). Model B2 dipakai untuk **desa yang sama** pada musim mendatang, sehingga pengelompokan per desa menguji generalisasi ke desa baru — bukan skenario pemakaiannya — dan tetap mencampur musim yang berbagi guncangan cuaca dan hama di latih dan uji. Pada B1, pengelompokan per pembeli setidaknya menutup kebocoran antarpesanan pembeli yang sama, dan model memang juga dipakai untuk pembeli baru; yang tidak ditangkapnya adalah perubahan pola menurut waktu (musim belanja, promosi).

**(f) Dua risiko etis** — `082-1` · C5 · 5 poin

| Risiko | Siapa dirugikan dan bagaimana | Penanganan |
|--------|-------------------------------|------------|
| Bias pengukuran dan representasi | Desa terpencil, desa yang citranya sering tertutup awan, atau desa dengan sedikit plot ubinan memiliki fitur dan label yang lebih bising, sehingga galatnya lebih besar dan prioritas bantuannya lebih sering salah — justru pada desa yang rentan | Laporkan galat per kelompok desa (terpencil, tadah hujan, berawan); sertakan rentang ketidakpastian; verifikasi lapangan sebelum keputusan untuk desa yang datanya buruk |
| Satu perkiraan per desa untuk petani yang berbeda sifat (sejenis bias agregasi) | Produktivitas desa adalah rata-rata; satu angka per desa diberlakukan pada petani yang lahannya berbeda sifat, sehingga petani kecil di lahan tadah hujan di desa yang rata-ratanya tinggi kehilangan bantuan benih | Model hanya untuk perencanaan tingkat desa; penetapan penerima tetap memakai pendataan petani; jalur usulan dan keberatan kelompok tani |
| Umpan balik | Bantuan dan serapan mengikuti perkiraan: desa yang diperkirakan rendah tidak disiapkan gudang, petani menjual ke tengkulak, dan hasilnya tidak tercatat lengkap — data musim berikutnya ikut bias | Catat bantuan dan serapan yang diberikan; pantau galat per desa dari musim ke musim |
| Penyalahgunaan angka | Perkiraan dipakai untuk menilai kinerja penyuluh atau kepala desa | Nyatakan "bukan untuk" pada *model card*; batasi pemakaian |

**Pedoman skor:** sama dengan B1(f).

**Contoh jawaban B2 (keseluruhan)**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "(a) Memprediksi produktivitas padi. (b) `varietas_dominan` dan `irigasi_teknis`. (c) $R^2$. (d) Jaringan saraf karena paling canggih; SVM; pohon keputusan. (e) Bagi acak 80/20. (f) Data bisa salah." | 1,75 (a 0,25 — besaran tanpa satuan · c 0,25 — $R^2$ saja · d 1,25 — jaringan saraf: model 0,5 + alasan "canggih" 0,25; SVM tanpa versi regresinya, tanpa alasan, 0; pohon keputusan tanpa alasan 0,5 · butir lain 0) |
| Cukup | "(a) Produktivitas ton/ha; regresi; prediksi 6 minggu sebelum panen. (b) `produksi_ton` karena dari panen; `rerata_produktivitas_3_musim_lalu` karena memakai target. (c) Terlalu rendah lebih buruk karena gabah tidak terserap; pakai RMSE. (d) Ridge karena fitur berkorelasi; *Random Forest* karena akurat; jaringan saraf karena data banyak. (e) Latih 2022–2024, uji 2025; *GridSearchCV* pada data latih; bandingkan rerata MAE; *baseline* rerata data latih. (f) Desa terpencil datanya kurang sehingga galatnya besar; perbaiki data. Petani kecil kehilangan bantuan; libatkan manusia." | 12,5 (a 1,5 — cara pengukuran tidak ada; saat prediksi tidak dinyatakan dalam minggu 0,5 · b 1,25 — kolom kedua sah · c 1,25 — dampak terlalu tinggi tidak ada; RMSE tanpa kaitan dengan dampak 0,5 · d 3,0 — Ridge penuh; RF 0,75; jaringan saraf 0,5 + alasan "data banyak" yang keliru untuk 19.200 baris 0,25 · e 2,5 — temporal tanpa alasan 1,0; penyetelan pada data latih 0,5 + *GridSearchCV* tanpa lipatan per musim 0,25; rerata 0; *baseline* rerata 0,75 · f 3,0 — tiap risiko menyebut siapa dirugikan tanpa mekanisme lengkap 1,0 + penanganan umum 0,5) |
| Baik | "(a) Produktivitas padi desa musim berjalan (ton GKP/ha) dari ubinan saat panen. Regresi. Prediksi pada minggu ke-10 sejak tanam. (b) `produksi_ton`: dicatat saat panen dan memuat target. `indeks_hijau_m11`–`m16`: belum ada pada minggu ke-10. (c) Terlalu tinggi: gudang dan dana BUMD menganggur, dan desa tidak mendapat bantuan padahal hasilnya rendah. Terlalu rendah: gabah tidak terserap dan dijual murah ke tengkulak. Kedua arah merugikan pihak berbeda. Metrik: MAE, karena kedua arah sama-sama merugikan; pelengkap: rerata galat bertanda agar arah galat terlihat. (d) Ridge: kolom indeks sangat berkorelasi, regularisasi menstabilkan koefisien, mudah dijelaskan. *Gradient boosting*: interaksi irigasi × hujan × varietas pada data tabular. PCA lalu Ridge: meringkas indeks minggu 1–10 yang berkorelasi, walau keterjelasan per minggu hilang. (e) Latih 2022–2024, uji 2025 sekali; acak per baris akan mencampur musim yang sama. Penyetelan dengan lipatan per musim di data latih, di dalam `Pipeline`. Lipatan sama untuk semua kandidat; bandingkan berpasangan: $\lvert\bar d\rvert > 2\cdot SE$ dan searah ≥ 80% lipatan. *Baseline*: rerata produktivitas tiga musim lalu. (f) Desa terpencil atau sering berawan datanya bising, galatnya besar, prioritasnya salah; tangani: laporkan galat per kelompok desa dan verifikasi lapangan. Petani kecil tadah hujan di desa yang rata-ratanya tinggi kehilangan bantuan; tangani: model hanya untuk perencanaan, penerima tetap dari pendataan petani dengan jalur keberatan." | 22,5 |

**Pelajari ulang:** [Bab 2 §2.1.2](../06-buku-ajar/bab-02-formulasi-masalah-daur-hidup-ml.md#212-ketepatan-pada-pertanyaan-kedua) (unsur target); [Bab 4 §4.5.5](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md#455-kebocoran-target) (kebocoran target), [§4.3.1](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md#431-pembagian-temporal); [Bab 6 §6.4.4](../06-buku-ajar/bab-06-regresi-dan-metriknya.md#644-memilih-metrik) (memilih metrik regresi), [§6.3.1](../06-buku-ajar/bab-06-regresi-dan-metriknya.md#631-gagasannya) (regularisasi); [Bab 11 §11.1.2](../06-buku-ajar/bab-11-reduksi-dimensi-dan-visualisasi.md#1112-apa-yang-diperoleh-dan-apa-yang-hilang) (PCA); [Bab 12 §12.6](../06-buku-ajar/bab-12-pengantar-jaringan-saraf-tiruan.md#126-kapan-jst-tidak-diperlukan) (kapan JST tidak diperlukan); [Bab 13 §13.2.1](../06-buku-ajar/bab-13-ai-generatif-dan-ai-bertanggung-jawab.md#1321-enam-sumber) (sumber *bias*), [§13.6.1](../06-buku-ajar/bab-13-ai-generatif-dan-ai-bertanggung-jawab.md#1361-enam-pertanyaan-sebelum-menerapkan-model).

---

## 3. Bagian C — Perhitungan (30 poin)

### C1. Memilih Percabangan Akar — `DAIML-Sub-CPMK102-1` (a–c) dan `DAIML-Sub-CPMK082-1` (d) · C3 (a–c) dan C4 (d) · 10 poin

**(a) *Entropy* dan *Gini* akar** — C3 · 2 poin *(entropy: langkah 0,5 + hasil 0,5 · Gini: langkah 0,5 + hasil 0,5)*

$$p_{\text{terlambat}}=\tfrac{12}{48}=0{,}25 \qquad H(S)=0{,}25(2{,}000)+0{,}75(0{,}415)=0{,}500+0{,}311=\mathbf{0{,}811}$$

$$G(S)=1-(0{,}25^2+0{,}75^2)=1-(0{,}0625+0{,}5625)=\mathbf{0{,}375}$$

**(b) Kandidat P** — C3 · 3 poin *(entropy cabang Ya 0,5 · entropy cabang Tidak: langkah 0,5 + hasil 0,5 · rerata berbobot 0,75 · IG 0,75)*

$$H(\text{Ya})=H(8/16)=\mathbf{1{,}000} \qquad H(\text{Tidak})=0{,}125(3{,}000)+0{,}875(0{,}193)=0{,}375+0{,}169=\mathbf{0{,}544}$$

$$\tfrac{16}{48}(1{,}000)+\tfrac{32}{48}(0{,}544)=0{,}333+0{,}363=0{,}696 \qquad IG_P=0{,}811-0{,}696=\mathbf{0{,}115}\ \text{(presisi penuh 0,116)}$$

**(c) Kandidat R** — C3 · 2 poin *(entropy cabang Ya 0,25 · entropy cabang Tidak 0,75 · rerata berbobot 0,5 · IG 0,5)*

$$H(\text{Ya})=H(3/3)=\mathbf{0}\ \text{(murni)} \qquad H(\text{Tidak})=0{,}2(2{,}322)+0{,}8(0{,}322)=0{,}464+0{,}258=\mathbf{0{,}722}$$

$$\tfrac{3}{48}(0)+\tfrac{45}{48}(0{,}722)=0{,}677 \qquad IG_R=0{,}811-0{,}677=\mathbf{0{,}134}$$

**(d) Pilihan pohon dan kelayakannya** — `082-1` · C4 · 3 poin

- Pohon tanpa pembatasan memilih **R** (IG 0,134 > P 0,115–0,116 > Q 0,062) *(0,5)*.
- Tidak layak *(1,5)*: `nomor_anggota` hanya nomor urut pendaftaran, bukan ciri yang berkaitan dengan keterlambatan *(0,5)*. Percabangan itu memisahkan **3 peminjaman** yang kebetulan terlambat: daun sekecil itu adalah hafalan, dan fitur dengan banyak nilai berbeda menawarkan banyak titik potong sehingga mudah menemukan potongan kebetulan. Aturan itu menghafal 3 peminjaman, tidak berkaitan dengan sebab keterlambatan, dan tidak pernah berlaku untuk anggota baru (nomor urutnya selalu di atas 1.203) *(1,0)*.
- Dengan `min_samples_leaf=5`, R tidak diizinkan (daun 3 < 5); P dan Q diizinkan, dan pohon memilih **P** (0,116 > 0,062) *(1,0 — alasannya diminta batang soal; P tanpa alasan 0,5)*. Nilai tambah: buang `nomor_anggota` dari fitur.

**Contoh jawaban C1(d)**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "R, karena IG-nya terbesar, jadi itu percabangan terbaik." | 0,5 |
| Cukup | "R karena IG terbesar. Tidak layak karena nomor anggota hanya nomor urut. Dengan `min_samples_leaf=5` pilih P." | 1,5 (R 0,5 · tidak layak 0,5 — pengenal disebut, daun kecil/hafalan tidak · P tanpa alasan 0,5) |
| Baik | "R (IG 0,134 terbesar). Tidak layak: nomor anggota hanya nomor urut, dan cabangnya memisahkan 3 peminjaman yang kebetulan terlambat — hafalan yang tidak berlaku untuk anggota baru. Dengan `min_samples_leaf=5` daun R (3) tidak diizinkan, jadi pohon memilih P (0,116 > 0,062)." | 3 |

**Pelajari ulang:** [Bab 8 §8.1.2–§8.1.4](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md#812-memilih-percabangan) (*entropy*, IG, *Gini*), [§8.2](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md#82-overfitting-pada-pohon) (`min_samples_leaf`), [§8.4.1](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md#841-demonstrasi-biasnya) (fitur berkardinalitas tinggi).

---

### C2. Satu Langkah Pelatihan Jaringan Saraf — `DAIML-Sub-CPMK102-1` (a–d) dan `DAIML-Sub-CPMK082-1` (e) · C3 (a–d) dan C4 (e) · 10 poin

Langkah di bawah memakai angka yang dibulatkan empat desimal pada setiap langkah, seperti yang ditulis mahasiswa dengan kalkulator. Bila digit keempatnya berbeda, nilai presisi penuh — konvensi [Bab 12 §12.4.2](../06-buku-ajar/bab-12-pengantar-jaringan-saraf-tiruan.md#1242-backpropagation--perhitungan-manual) dan keluaran Python §5 — ditulis dalam kurung. Keduanya benar (toleransi ±0,0005).

**(a)** — C3 · 2 poin *($z_1$ 0,25 · $z_2$ 0,25 · $h_1$ 0,75 · $h_2$ 0,75)*

$$z_1=0{,}3(2)+(-0{,}2)(1)=\mathbf{0{,}4} \qquad z_2=-0{,}1(2)+0{,}4(1)=\mathbf{0{,}2}$$

$$h_1=\frac{1}{1+e^{-0{,}4}}=\frac{1}{1{,}6703}=\mathbf{0{,}5987} \qquad h_2=\frac{1}{1+e^{-0{,}2}}=\frac{1}{1{,}8187}=\mathbf{0{,}5498}$$

**(b)** — C3 · 1,5 poin *($z_{\text{out}}$ 0,5 · $\hat y$ 0,5 · $L$ 0,5)*

$$z_{\text{out}}=0{,}8(0{,}5987)+(-0{,}5)(0{,}5498)=0{,}4790-0{,}2749=\mathbf{0{,}2041}\ \text{(presisi penuh 0,2040)}$$

$$\hat y=\sigma(0{,}2041)=\mathbf{0{,}5508} \qquad L=(1-0{,}5508)^2=0{,}4492^2=\mathbf{0{,}2018}$$

**(c)** — C3 · 3 poin *($\delta_{\text{out}}$: $\partial L/\partial\hat y$ 0,25 + $\sigma'$ 0,25 + hasil 0,5 · dua gradien masing-masing 0,5 · dua pembaruan masing-masing 0,5)*

$$\frac{\partial L}{\partial\hat y}=-2(0{,}4492)=-0{,}8984\ \text{(presisi penuh }-0{,}8983\text{)} \qquad \sigma'(z_{\text{out}})=0{,}5508(0{,}4492)=0{,}2474 \qquad \delta_{\text{out}}=-0{,}8984\times0{,}2474=\mathbf{-0{,}2223}$$

$$\frac{\partial L}{\partial v_1}=\delta_{\text{out}}h_1=-0{,}2223(0{,}5987)=\mathbf{-0{,}1331} \qquad \frac{\partial L}{\partial v_2}=\delta_{\text{out}}h_2=-0{,}2223(0{,}5498)=\mathbf{-0{,}1222}$$

$$v_1\leftarrow0{,}8-0{,}5(-0{,}1331)=0{,}8+0{,}06655=\mathbf{0{,}8666}\ \text{(presisi penuh 0,8665)} \qquad v_2\leftarrow-0{,}5-0{,}5(-0{,}1222)=\mathbf{-0{,}4389}$$

**(d)** — C3 · 1,5 poin *($\delta_{h_2}$ 0,75 · $\partial L/\partial w_{22}$ 0,25 · $w_{22}$ baru 0,5)* — memakai $v_2$ **sebelum** diperbarui (−0,5), sesuai petunjuk soal dan contoh [Bab 12 §12.4.2](../06-buku-ajar/bab-12-pengantar-jaringan-saraf-tiruan.md#1242-backpropagation--perhitungan-manual), yang memakai $v_1$ lama (0,6) pada $\delta_{h_1}$: seluruh gradien satu langkah dihitung dari bobot sebelum pembaruan.

$$\delta_{h_2}=\delta_{\text{out}}\cdot v_2\cdot h_2(1-h_2)=(-0{,}2223)(-0{,}5)(0{,}5498)(0{,}4502)=0{,}11115\times0{,}2475=\mathbf{0{,}0275}$$

$$\frac{\partial L}{\partial w_{22}}=\delta_{h_2}\cdot x_2=0{,}0275(1)=\mathbf{0{,}0275} \qquad w_{22}\leftarrow0{,}4-0{,}5(0{,}0275)=0{,}4-0{,}01375=\mathbf{0{,}3863}\ \text{(presisi penuh 0,3862)}$$

**(e) Arah perubahan** — `082-1` · C4 · 2 poin

- $v_2$ **naik** (−0,5 → −0,4389) dan $w_{22}$ **turun** (0,4 → 0,3863) *(0,5)*.
- $v_2$: $h_2>0$ dikalikan $v_2<0$, sehingga suku $v_2h_2$ **mengurangi** $z_{\text{out}}$. $v_2$ yang kurang negatif memperkecil pengurangan itu → $z_{\text{out}}$ naik → $\hat y$ naik menuju 1 *(0,5)*.
- $w_{22}$: karena $v_2<0$, $h_2$ justru menekan keluaran. Menurunkan $w_{22}$ menurunkan $z_2$ dan $h_2$, sehingga suku negatif $v_2h_2$ mengecil → $z_{\text{out}}$ dan $\hat y$ naik. Dalam aturan rantai: $\delta_{h_2}$ positif karena dua tanda negatif ($\delta_{\text{out}}<0$, $v_2<0$), sehingga *gradient descent* menurunkan $w_{22}$ *(1,0)*.

Pemeriksaan (§5): bila hanya $v_2$ yang diperbarui, $\hat y$ menjadi 0,5591; bila hanya $w_{22}$, 0,5513 — keduanya di atas 0,5508.

Kesalahan terbawa: arah dinilai terhadap hasil (c)–(d) mahasiswa sendiri; alasan dinilai menurut ketepatannya.

**Contoh jawaban C2(e)**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "Keduanya harus naik karena $\hat y$ masih di bawah target." | 0 |
| Cukup | "$v_2$ naik, $w_{22}$ turun. $v_2$ naik karena $\hat y$ harus naik." | 0,5 (alasan tanpa peran tanda $v_2$ 0) |
| Baik | "$v_2$ naik, $w_{22}$ turun. Karena $v_2<0$, suku $v_2h_2$ mengurangi $z_{\text{out}}$; $v_2$ yang kurang negatif mengurangi pengurangan itu, jadi $\hat y$ naik. $w_{22}$ turun membuat $h_2$ turun, dan karena $v_2<0$ suku negatif itu mengecil, sehingga $\hat y$ juga naik." | 2 |

**Pelajari ulang:** [Bab 12 §12.4.2](../06-buku-ajar/bab-12-pengantar-jaringan-saraf-tiruan.md#1242-backpropagation--perhitungan-manual) (langkah maju-mundur dan gradien lapis tersembunyi); [Lab 13](../04-labs/lab-13-jaringan-saraf-tiruan.md) Langkah 2 (pembaruan bobot lapis tersembunyi dan arahnya).

---

### C3. *Silhouette* Hasil Pengelompokan Desa Wisata — `DAIML-Sub-CPMK102-1` (a–c) dan `DAIML-Sub-CPMK082-1` (d) · C3 (a, b) dan C4 (c, d) · 10 poin

**(a) $a(i)$, $b(i)$, $s(i)$** — C3 · 4 poin *(per desa: $a$ 0,5 · $b$ 1,0 = rerata ke kedua klaster lain 0,5 + memilih yang terkecil 0,5 · $s$ 0,5)*

| Desa | $a(i)$ — klaster sendiri | Rerata ke klaster lain | $b(i)$ | $s(i)$ |
|------|--------------------------|------------------------|--------|--------|
| D2 (A) | $(2{,}0+1{,}0)/2=1{,}5$ | ke B: $(8{,}5+4{,}2)/2=6{,}35$; ke C: $(5{,}0+6{,}0)/2=5{,}5$ | 5,5 (C) | $(5{,}5-1{,}5)/5{,}5=\mathbf{0{,}727}$ |
| D5 (B) | $4{,}2$ (hanya D4) | ke A: $(5{,}8+4{,}2+3{,}6)/3=4{,}533$; ke C: $(3{,}6+4{,}2)/2=3{,}9$ | 3,9 (C) | $(3{,}9-4{,}2)/4{,}2=\mathbf{-0{,}071}$ |

**(b) Rerata** — C3 · 1 poin *(jumlah 0,5 · hasil 0,5)*

$$\bar s=\frac{0{,}720+0{,}727+0{,}714+0{,}306-0{,}071+0{,}794+0{,}804}{7}=\frac{3{,}994}{7}=\mathbf{0{,}571}$$

**(c) Arti $s(\text{D5})$ dan tindakannya** — `102-1` · C4 · 2 poin

- Arti *(1,0)*: $s(\text{D5})<0$ karena $b(\text{D5})=3{,}9<a(\text{D5})=4{,}2$ — rata-rata jarak D5 ke anggota klaster C lebih kecil daripada ke satu-satunya teman sekelompoknya. D5 berada di perbatasan B dan C dan **kemungkinan salah ditempatkan**; klaster B sendiri renggang (dua anggotanya berjarak 4,2). "Negatif berarti salah tempat" tanpa perbandingan $a$ dan $b$ atau tanpa menyebut klaster C = 0,5.
- Tindakan *(1,0)*: periksa profil D5 pada indikator asli dan bandingkan dengan B dan C; pertimbangkan memindahkannya ke C, atau tandai sebagai desa perbatasan yang programnya diputuskan dengan peninjauan langsung — jangan memakai label klaster D5 begitu saja. "Pindahkan" tanpa memeriksa profil atau menyebut klaster tujuan = 0,5; "hapus D5" tanpa alasan = 0,25.
- Nilai tambah: K-Means menempatkan D5 di B karena K-Means memakai jarak ke **pusat** klaster (pusat B berada di antara D4 dan D5), sedangkan *silhouette* memakai rata-rata jarak ke **anggota**.

**(d) k = 2 atau k = 3** — `082-1` · C4 · 3 poin

- *Silhouette* k = 3 (0,571) lebih tinggi daripada k = 2 (0,501), tetapi selisihnya tidak besar, dan *silhouette* hanya mengukur pemisahan **geometris**, bukan kebermaknaan *(1,0; angka tanpa keterbatasannya 0,5)*.
- Kebermaknaan *(1,25; menyebut batas dua program tanpa mengaitkannya dengan profil klaster 0,75)*: dinas hanya sanggup dua program. Dengan k = 2, setiap klaster langsung mendapat satu program: A (kunjungan rendah, tinggal singkat) dan gabungan B + C (tinggal panjang). Dengan k = 3, C (kunjungan rendah, tinggal panjang) terpisah dari B (kunjungan tinggi) — perbedaan yang bermakna bila programnya berbeda menurut kunjungan.
- Saran yang konsisten *(0,75)*. Dua saran diterima penuh: **k = 2** — sesuai dua program, dengan selisih *silhouette* yang kecil; atau **k = 3** dengan memetakan dua program ke tiga klaster (mis. A dan C sama-sama mendapat program promosi karena kunjungannya rendah; B mendapat program pengelolaan pengunjung). "k = 3 karena *silhouette*-nya tertinggi" tanpa kebermaknaan = 0,5 + 0 + 0,25 = 0,75.

**Contoh jawaban C3(c)–(d)**

| Tingkat | Contoh | Skor (c + d dari 5) |
|---------|--------|---------------------|
| Kurang | "(c) D5 bagus karena dekat ke klaster lain. (d) k = 3 karena *silhouette* tertinggi." | 0,75 (c 0 · d 0,75) |
| Cukup | "(c) Negatif berarti D5 salah tempat; pindahkan. (d) k = 3 lebih tinggi (0,571 vs 0,501), tetapi dinas hanya punya dua program, jadi k = 2." | 3,0 (c 1,0 — arti 0,5 + tindakan tanpa pemeriksaan profil 0,5 · d 2,0 — keterbatasan *silhouette* tidak disebut 0,5; kebermaknaan tanpa profil klaster 0,75; saran 0,75) |
| Baik | "(c) $b$ = 3,9 < $a$ = 4,2: D5 rata-rata lebih dekat ke C daripada ke D4, jadi di perbatasan dan mungkin salah tempat. Periksa profil aslinya; pindahkan ke C atau tinjau programnya secara langsung. (d) 0,571 vs 0,501: k = 3 sedikit lebih terpisah, tetapi *silhouette* hanya geometris. Dinas hanya sanggup dua program: k = 2 memisahkan A (kunjungan rendah, tinggal singkat) dari desa bertinggal panjang, langsung sesuai dua program. Saran: k = 2." | 5 |

**Pelajari ulang:** [Bab 10 §10.3.2](../06-buku-ajar/bab-10-pembelajaran-tanpa-supervisi.md#1032-silhouette) (*silhouette*), [§10.3.3](../06-buku-ajar/bab-10-pembelajaran-tanpa-supervisi.md#1033-kriteria-ketiga-yang-paling-menentukan) (kriteria ketiga), [§10.6.2](../06-buku-ajar/bab-10-pembelajaran-tanpa-supervisi.md#1062-metrik-tidak-menggantikan-penilaian-manusia) (metrik tidak menggantikan penilaian manusia), [§10.7](../06-buku-ajar/bab-10-pembelajaran-tanpa-supervisi.md#107-menafsirkan-klaster).

---

## 4. Kesalahan Umum

| Soal | Kesalahan | Perlakuan |
|------|-----------|-----------|
| A1 (i) | Menganggap *Random Forest* selalu lebih baik daripada pohon tunggal | 0 pada alasan rencana |
| A2 (i) | Hanya memeriksa $\lvert\bar d\rvert > 2\cdot SE$ | Paling banyak 0,5 dari 1,75 pada pemeriksaan dan kesimpulan |
| A2 (ii) | Memilih model berdasarkan rerata tertinggi | 0 pada unsur "kedua pasangan tidak bermakna"; sumber keterbatasan dan tindak lanjut dinilai menurut isinya |
| A3 (ii) | Memilih *hierarchical clustering* untuk 2,4 juta baris | 0 pada metode |
| A5 (ii) | Menganggap jarak antarklaster t-SNE sebagai ukuran perbedaan | 0 pada unsur itu |
| B1 (b), B2 (b) | Menyebut kolom masa lalu yang sah (`riwayat_tolak_pembeli`, `rerata_produktivitas_3_musim_lalu`) sebagai kebocoran | 0 untuk kolom itu |
| B1 (e), B2 (e) | Pembagian acak per baris; membandingkan rerata ± simpangan | 0 pada unsur itu |
| C1 (b), (c) | Rerata biasa (tidak berbobot) *entropy* kedua cabang | 0 pada rerata berbobot di sub-soal pertama tempat kesalahan itu muncul (biasanya (b)). Bila kesalahan konsep yang sama diulang pada sub-soal berikutnya, ia **tidak dipotong lagi** — dipotong sekali, seperti C3(a) — dan rerata berbobot sub-soal itu dinilai sebagai kesalahan terbawa. IG, dan pilihan kandidat pada (d), dinilai sebagai kesalahan terbawa terhadap angka mahasiswa sendiri |
| C1 (d) | Memilih P "karena IG-nya terbesar" | 0 pada pilihan pohon — kecuali konsisten dengan IG hasil hitungan sendiri pada (b)–(c) (kesalahan terbawa: nilai penuh pada pilihan); alasan dan `min_samples_leaf` dinilai menurut isinya |
| C2 (a) | Memakai $w_{12}$ untuk $h_1$ (konvensi indeks tertukar) | Kesalahan terbawa; potong 0,5 sekali pada (a) |
| C2 (c) | Lupa faktor $\sigma'(z_{\text{out}})$ pada $\delta_{\text{out}}$ | 0,5 dari 1,0 pada $\delta_{\text{out}}$; gradien dan pembaruan dinilai sebagai kesalahan terbawa |
| C2 (d) | Lupa $v_2$ atau $h_2(1-h_2)$ pada $\delta_{h_2}$ | 0,25 dari 0,75 pada $\delta_{h_2}$ |
| C2 (d) | Memakai $v_2$ yang sudah diperbarui (−0,4389), bertentangan dengan petunjuk soal → $\delta_{h_2}\approx0{,}0241$, $w_{22}\approx0{,}3879$–$0{,}3880$ | Potong 0,25 pada $\delta_{h_2}$; $\partial L/\partial w_{22}$ dan $w_{22}$ dinilai sebagai kesalahan terbawa; arah pada (e) tetap sama |
| C3 (a) | $b(i)$ = rerata jarak ke **semua** titik di luar klaster, atau ke klaster terjauh | 0,5 dari 1,0 pada $b$ |
| C3 (a) | Menyertakan jarak titik ke dirinya sendiri (0) dalam $a(i)$ | 0 pada $a$; $s$ dinilai sebagai kesalahan terbawa |
| C3 (a) | Kesalahan konsep yang sama (salah satu dari dua baris di atas) pada D2 **dan** D5 | Dipotong **sekali**, pada desa pertama; desa kedua tidak dipotong lagi untuk kesalahan yang sama |

---

## 5. Memeriksa Angka dengan Python

Blok berikut dapat dijalankan apa adanya di Google Colab untuk memeriksa angka A2, A4, B1, B2, dan Bagian C — nilai presisi penuh dan nilai berpembulatan per langkah yang tertulis pada pembahasan. Jalankan **sesudah** Anda menghitung sendiri dengan kalkulator — di UAS tidak ada komputer.

```python
# Memeriksa angka Latihan UAS Dasar AI/ML (A2, A4, B1, B2, dan Bagian C)
import numpy as np

def ringkas(d):
    """Rerata, simpangan baku sampel (ddof=1), SE, dan banyak lipatan searah."""
    d = np.asarray(d, float)
    d_bar, s_d = d.mean(), d.std(ddof=1)
    se = s_d / np.sqrt(len(d))
    searah = int((np.sign(d) == np.sign(d_bar)).sum())
    return d_bar, s_d, se, searah

# A2(i): HistGB - regresi logistik, ROC-AUC per lipatan
hgb = np.array([0.861, 0.874, 0.855, 0.842, 0.866])
logit = np.array([0.830, 0.846, 0.825, 0.843, 0.868])
d = hgb - logit
d_bar, s_d, se, searah = ringkas(d)
print("A2(i) d_i:", np.round(d, 3), f"| d_bar {d_bar:.4f} s_d {s_d:.4f} SE {se:.4f} "
      f"2SE {2*se:.4f} (dari SE soal: {2*0.0077:.4f}) | searah {searah}/5 "
      f"| bermakna: {abs(d_bar) > 2*se and searah >= 4}")

# A2(ii): contoh skor lipatan yang KONSISTEN dengan ringkasan pada soal
nb = np.array([0.600, 0.625, 0.610, 0.605, 0.615])
svm = nb + np.array([0.020, 0.012, 0.005, -0.004, -0.003])
hgb2 = nb + np.array([0.022, 0.012, -0.004, -0.006, -0.004])
for nama, m in (("SVM-NB", svm), ("HistGB-NB", hgb2)):
    d_bar, s_d, se, searah = ringkas(m - nb)
    # 2SE dihitung dari SE tiga desimal yang tercetak pada soal, seperti yang dilakukan mahasiswa
    print(f"A2(ii) {nama}: d_bar {d_bar:.3f} SE {se:.3f} 2SE(soal) {2*round(se, 3):.3f} "
          f"positif {int((m - nb > 0).sum())}/5 "
          f"| F1 rerata {m.mean():.3f} | bermakna: {abs(d_bar) > 2*se and searah >= 4}")
print("A2(ii) F1 rerata NB:", round(nb.mean(), 3))

# A4: selisih latih - validasi Tim P dan kenaikan validasi setiap data digandakan
p_latih, p_val = np.array([0.99, 0.97, 0.95, 0.93]), np.array([0.64, 0.71, 0.77, 0.82])
print("A4 Tim P selisih:", np.round(p_latih - p_val, 2), "| kenaikan validasi:", np.round(np.diff(p_val), 2))

# B1: akurasi model "semua diterima" dan rasio biaya FN : FP (tanpa pembatalan)
print("B1 akurasi kelas terbanyak:", round(1 - 0.09, 2), "| rasio biaya:", round(38000 / 3000, 1))
# B2: minggu keputusan dan jumlah baris
print("B2 minggu keputusan:", 16 - 6, "| baris:", 2400 * 8)

# C1: entropy, Gini, dan information gain
def H(*n):
    p = np.array(n, float) / sum(n)
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) + 0.0   # + 0.0 agar tidak tercetak -0.0
def G(*n):
    p = np.array(n, float) / sum(n)
    return float(1 - (p ** 2).sum())
def IG(induk, anak):
    N = sum(sum(a) for a in anak)
    return H(*induk) - sum(sum(a) / N * H(*a) for a in anak)
akar = (12, 36)
print(f"C1 H(akar) {H(*akar):.3f} | G(akar) {G(*akar):.3f}")
for nama, anak in (("P", [(8, 8), (4, 28)]), ("Q", [(9, 15), (3, 21)]), ("R", [(3, 0), (9, 36)])):
    rerata_bobot = sum(sum(a) / 48 * H(*a) for a in anak)
    print(f"C1 {nama}: H cabang {[round(H(*a), 3) for a in anak]} | rerata berbobot {rerata_bobot:.3f} "
          f"| IG {IG(akar, anak):.3f}")
# C1 dengan tabel -log2 p pada lembar rumus (tiga desimal), seperti dihitung dengan kalkulator
log = {0.25: 2.000, 0.75: 0.415, 0.125: 3.000, 0.875: 0.193, 0.2: 2.322, 0.8: 0.322}
r3 = lambda v: round(v, 3)
suku = lambda *pq: [r3(p * log[p]) for p in pq]          # suku p * (-log2 p), tiga desimal
s_akar, s_p, s_r = suku(0.25, 0.75), suku(0.125, 0.875), suku(0.2, 0.8)
h_akar, h_p, h_r = r3(sum(s_akar)), r3(sum(s_p)), r3(sum(s_r))
s_bobot_p = [r3(16/48 * 1.000), r3(32/48 * h_p)]
bobot_p, bobot_r = r3(sum(s_bobot_p)), r3(45/48 * h_r)
print(f"C1 (tabel) akar: suku {s_akar} H {h_akar:.3f} | Gini 1-({0.25**2}+{0.75**2}) = {1 - 0.25**2 - 0.75**2}")
print(f"C1 (tabel) P: suku H(Tidak) {s_p} = {h_p:.3f} | suku rerata {s_bobot_p} = {bobot_p:.3f} "
      f"| IG {h_akar - bobot_p:.3f}")
print(f"C1 (tabel) R: suku H(Tidak) {s_r} = {h_r:.3f} | rerata berbobot {bobot_r:.3f} | IG {h_akar - bobot_r:.3f}")

# C2: satu langkah maju-mundur jaringan 2-2-1 (sigmoid, bias 0)
sig = lambda z: 1 / (1 + np.exp(-z))
x1, x2, y, eta = 2.0, 1.0, 1.0, 0.5
w11, w21, w12, w22, v1, v2 = 0.3, -0.2, -0.1, 0.4, 0.8, -0.5
z1, z2 = w11*x1 + w21*x2, w12*x1 + w22*x2
h1, h2 = sig(z1), sig(z2)
z_out = v1*h1 + v2*h2
y_hat = sig(z_out)
L = (y - y_hat) ** 2
d_out = -2 * (y - y_hat) * y_hat * (1 - y_hat)
g_v1, g_v2 = d_out * h1, d_out * h2
d_h2 = d_out * v2 * h2 * (1 - h2)
g_w22 = d_h2 * x2
print(f"C2 z1 {z1:.4f} z2 {z2:.4f} h1 {h1:.4f} h2 {h2:.4f} | z_out {z_out:.4f} y_hat {y_hat:.4f} L {L:.4f}")
print(f"C2 dL/dy_hat {-2*(y-y_hat):.4f} sigma' {y_hat*(1-y_hat):.4f} delta_out {d_out:.4f} "
      f"| dL/dv1 {g_v1:.4f} dL/dv2 {g_v2:.4f} | v1 {v1 - eta*g_v1:.4f} v2 {v2 - eta*g_v2:.4f}")
print(f"C2 delta_h2 {d_h2:.4f} dL/dw22 {g_w22:.4f} w22 {w22 - eta*g_w22:.4f}")
# Pemeriksaan arah: y_hat bila hanya v2 diperbarui, dan bila hanya w22 diperbarui
y_v2 = sig(v1*h1 + (v2 - eta*g_v2)*h2)
y_w22 = sig(v1*h1 + v2*sig(w12*x1 + (w22 - eta*g_w22)*x2))
print(f"C2 y_hat jika hanya v2 diperbarui {y_v2:.4f} | jika hanya w22 diperbarui {y_w22:.4f}")
# C2 dengan pembulatan empat desimal pada SETIAP langkah (seperti dengan kalkulator; setengah dibulatkan ke atas)
from decimal import Decimal, ROUND_HALF_UP
r4 = lambda v: float(Decimal(repr(float(v))).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))
print(f"C2 (per langkah) 1+e^-z1 {r4(1 + np.exp(-z1)):.4f} 1+e^-z2 {r4(1 + np.exp(-z2)):.4f}")
H1, H2 = r4(sig(z1)), r4(sig(z2))
print(f"C2 (per langkah) v1*h1 {r4(v1*H1):.4f} | v2*h2 {r4(v2*H2):.4f}")
Z = r4(r4(v1*H1) - r4(-v2*H2))
Y = r4(sig(Z)); E = r4(y - Y)
DY, SP = r4(-2*E), r4(Y*(1 - Y))
DO = r4(DY*SP)
GV1, GV2 = r4(DO*H1), r4(DO*H2)
P2, HH = DO*v2, r4(H2*(1 - H2))
DH2 = r4(P2*HH)
print(f"C2 (per langkah) z_out {Z:.4f} y_hat {Y:.4f} L {r4(E*E):.4f} dL/dy_hat {DY:.4f} sigma' {SP:.4f} "
      f"delta_out {DO:.4f} | dL/dv1 {GV1:.4f} dL/dv2 {GV2:.4f} | eta*dL/dv1 {eta*GV1:.5f} "
      f"v1 {r4(v1 - eta*GV1):.4f} v2 {r4(v2 - eta*GV2):.4f}")
print(f"C2 (per langkah) delta_out*v2 {P2:.5f} h2(1-h2) {HH:.4f} delta_h2 {DH2:.4f} "
      f"eta*dL/dw22 {eta*DH2:.5f} w22 {r4(w22 - eta*DH2):.4f}")
# Kesalahan umum C2(d): memakai v2 yang sudah diperbarui
v2_baru = v2 - eta*g_v2
d_h2_salah = d_out * v2_baru * h2 * (1 - h2)
print(f"C2 (salah: v2 baru) delta_h2 {d_h2_salah:.4f} w22 {w22 - eta*d_h2_salah:.4f} "
      f"| per langkah: delta_h2 {r4(DO*r4(v2 - eta*GV2)*HH):.4f} w22 {r4(w22 - eta*r4(DO*r4(v2 - eta*GV2)*HH)):.4f}")

# C3: silhouette dari tabel jarak pada soal (dibulatkan 1 desimal)
D = np.array([
    [0.0, 2.0, 2.2, 10.0, 5.8, 7.0, 8.0],
    [2.0, 0.0, 1.0, 8.5, 4.2, 5.0, 6.0],
    [2.2, 1.0, 0.0, 7.8, 3.6, 5.1, 6.1],
    [10.0, 8.5, 7.8, 0.0, 4.2, 6.1, 6.0],
    [5.8, 4.2, 3.6, 4.2, 0.0, 3.6, 4.2],
    [7.0, 5.0, 5.1, 6.1, 3.6, 0.0, 1.0],
    [8.0, 6.0, 6.1, 6.0, 4.2, 1.0, 0.0]])
def silhouette(D, label):
    s = []
    for i in range(len(D)):
        sendiri = [j for j in range(len(D)) if label[j] == label[i] and j != i]
        a = D[i, sendiri].mean()
        b = min(D[i, [j for j in range(len(D)) if label[j] == k]].mean()
                for k in set(label) if k != label[i])
        s.append((b - a) / max(a, b))
    return np.array(s)
k3 = ["A", "A", "A", "B", "B", "C", "C"]
k2 = ["A", "A", "A", "BC", "BC", "BC", "BC"]
s3, s2 = silhouette(D, k3), silhouette(D, k2)
print("C3 s (k=3):", np.round(s3, 3), "| rerata", round(s3.mean(), 3))
print("C3 s (k=2):", np.round(s2, 3), "| rerata", round(s2.mean(), 3))
print("C3 D2: a =", D[1, [0, 2]].mean(), "| ke B =", round(D[1, 3:5].mean(), 3), "| ke C =", round(D[1, 5:].mean(), 3))
print("C3 D5: a =", D[4, 3], "| ke A =", round(D[4, :3].mean(), 3), "| ke C =", round(D[4, 5:].mean(), 3))
print("C3 jumlah s (k=3):", round(float(np.round(s3, 3).sum()), 3))

# C3 (lanjutan): tabel jarak berasal dari koordinat terskala rekaan; hasil K-Means k=3 dan k=2
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples
X = np.array([[2, 0], [2, 2], [3, 2], [8, 8], [5, 5], [2, 7], [2, 8]], float)
print("C3 tabel jarak cocok dengan koordinat:",
      np.allclose(np.round(np.sqrt(((X[:, None] - X[None]) ** 2).sum(-1)), 1), D))
# Pembulatan satu desimal: D2, D5, D4 segaris, jadi d(D2,D4) = d(D2,D5) + d(D5,D4) sebelum dibulatkan
jarak = lambda i, j: float(np.linalg.norm(X[i] - X[j]))
print(f"C3 sebelum dibulatkan: d(D2,D4) {jarak(1, 3):.3f} | d(D2,D5) {jarak(1, 4):.3f} | d(D5,D4) {jarak(4, 3):.3f}")
for k in (3, 2):
    km = KMeans(n_clusters=k, n_init=20, random_state=42).fit(X)
    s_k = silhouette_samples(D, km.labels_, metric="precomputed")
    print(f"C3 K-Means k={k}: label {km.labels_} | silhouette {np.round(s_k, 3)}")
    if k == 3:
        print("C3 jarak D5 ke tiap pusat:", np.round(np.linalg.norm(km.cluster_centers_ - X[4], axis=1), 2))
```

Keluaran yang diharapkan: A2(i) $d_i$ = [0,031; 0,028; 0,03; −0,001; −0,002], $\bar d$ 0,0172, $s_d$ 0,0171, SE 0,0077, 2SE 0,0153 (dari SE pada soal: 2 × 0,0077 = 0,0154), searah 3/5, tidak bermakna; A2(ii) SVM − NB 0,006, SE 0,005, 2SE 0,010, positif 3/5, F1 0,617; HistGB − NB 0,004, SE 0,006, 2SE 0,012, positif 2/5, F1 0,615; NB 0,611; keduanya tidak bermakna; A4 selisih Tim P [0,35; 0,26; 0,18; 0,11], kenaikan validasi [0,07; 0,06; 0,05]; B1 0,91 dan 12,7; B2 minggu 10 dan 19.200 baris; C1 H akar 0,811, G akar 0,375, P [1,0; 0,544] rerata berbobot 0,696 IG 0,116, Q [0,954; 0,544] IG 0,062, R [0,0; 0,722] rerata berbobot 0,677 IG 0,134; C1 dengan tabel $-\log_2 p$: suku akar 0,5 + 0,311, suku H(Tidak) P 0,375 + 0,169, suku rerata P 0,333 + 0,363, IG P 0,115, suku H(Tidak) R 0,464 + 0,258, IG R 0,134; C2 (presisi penuh) $z_1$ 0,4000, $z_2$ 0,2000, $h_1$ 0,5987, $h_2$ 0,5498, $z_{\text{out}}$ 0,2040, $\hat y$ 0,5508, $L$ 0,2018, $\partial L/\partial\hat y$ −0,8983, $\sigma'$ 0,2474, $\delta_{\text{out}}$ −0,2223, gradien −0,1331 dan −0,1222, $v_1$ 0,8665, $v_2$ −0,4389, $\delta_{h_2}$ 0,0275, $\partial L/\partial w_{22}$ 0,0275, $w_{22}$ 0,3862, $\hat y$ 0,5591 dan 0,5513; C2 (per langkah) 1,6703 dan 1,8187, 0,4790 dan −0,2749, $z_{\text{out}}$ 0,2041, −0,8984, −0,06655, $v_1$ 0,8666, 0,11115, 0,2475, 0,01375, $w_{22}$ 0,3863; C2 dengan $v_2$ baru (kesalahan umum) $\delta_{h_2}$ 0,0241, $w_{22}$ 0,3879 (per langkah 0,3880); C3 k = 3 [0,72; 0,727; 0,714; 0,306; −0,071; 0,794; 0,804] rerata 0,571 (jumlah 3,994), k = 2 [0,727; 0,747; 0,717; 0,38; 0,118; 0,374; 0,443] rerata 0,501, D2 a 1,5, ke B 6,35, ke C 5,5, D5 a 4,2, ke A 4,533, ke C 3,9; sebelum dibulatkan d(D2, D4) 8,485, d(D2, D5) 4,243, d(D5, D4) 4,243.

Bagian terakhir blok memeriksa bahwa tabel jarak C3 dibulatkan dari koordinat terskala rekaan D1 (2, 0), D2 (2, 2), D3 (3, 2), D4 (8, 8), D5 (5, 5), D6 (2, 7), D7 (2, 8) (`True`). Karena dibulatkan satu desimal, seperti dinyatakan soal, tabel tidak memenuhi ketaksamaan segitiga secara persis: d(D2, D4) = 8,5 > 4,2 + 4,2, padahal sebelum dibulatkan 8,485 = 4,243 + 4,243 (D2, D5, dan D4 segaris). Hitungan *silhouette* tidak terpengaruh. Pada koordinat itu, K-Means k = 3 menghasilkan klaster A/B/C seperti pada soal (label [0 0 0 1 1 2 2]) dan k = 2 menggabungkan B dan C (label [0 0 0 1 1 1 1]); `silhouette_samples(D, label, metric="precomputed")` sama dengan fungsi manual di atas (diperiksa pada scikit-learn 1.6 dan 1.9; nomor label dapat berbeda antarversi, pengelompokannya sama). Jarak D5 ke pusat klaster: A 4,53, B 2,12, C 3,91 — itulah sebabnya K-Means menempatkan D5 di B walaupun *silhouette*-nya negatif.

---

## Rujukan Belajar

| Bagian latihan | Bab buku ajar |
|----------------|---------------|
| B1 (a), B2 (a) | [Bab 2 — Formulasi Masalah dan Daur Hidup Pembelajaran Mesin](../06-buku-ajar/bab-02-formulasi-masalah-daur-hidup-ml.md) |
| B1 (b, e), B2 (b, e) | [Bab 4 — Pembagian Data dan Kebocoran Data](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md) |
| B2 (c) | [Bab 6 — Regresi dan Metriknya](../06-buku-ajar/bab-06-regresi-dan-metriknya.md) |
| B1 (c) | [Bab 7 — Klasifikasi dan Metriknya](../06-buku-ajar/bab-07-klasifikasi-dan-metriknya.md) |
| A1, C1, B1 (d), B2 (d) | [Bab 8 — Pohon Keputusan dan *Ensemble*](../06-buku-ajar/bab-08-pohon-keputusan-dan-ensemble.md) |
| A2, B1 (d, e), B2 (e) | [Bab 9 — SVM, Naive Bayes, dan Pemilihan Model](../06-buku-ajar/bab-09-svm-naive-bayes-pemilihan-model.md) |
| A3, C3 | [Bab 10 — Pembelajaran Tanpa Supervisi](../06-buku-ajar/bab-10-pembelajaran-tanpa-supervisi.md) |
| A4, A5, B2 (d) | [Bab 11 — Reduksi Dimensi dan Visualisasi Kinerja Model](../06-buku-ajar/bab-11-reduksi-dimensi-dan-visualisasi.md) |
| C2, B2 (d) | [Bab 12 — Pengantar Jaringan Saraf Tiruan](../06-buku-ajar/bab-12-pengantar-jaringan-saraf-tiruan.md) |
| B1 (f), B2 (f) | [Bab 13 — AI Generatif dan AI yang Bertanggung Jawab](../06-buku-ajar/bab-13-ai-generatif-dan-ai-bertanggung-jawab.md) |

Kisi-kisi dan ketentuan UAS: [kisi-kisi UAS](kisi-kisi-uas.md) · [Modul Minggu 16](../03-modules/week-16-uas-review-dan-ujian.md).

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
