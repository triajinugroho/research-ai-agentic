---
id: uai-if52510031-latihan-uas
tipe: asesmen
judul: "Latihan UAS — Dasar Kecerdasan Artifisial dan Pembelajaran Mesin"
kode_mk: IF52510031
nama_mk: Dasar Kecerdasan Artifisial dan Pembelajaran Mesin
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-09
---

# LATIHAN UJIAN AKHIR SEMESTER (SIMULASI)

## Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — IF52510031

> **Latihan UAS — bukan naskah UAS.** Simulasi lengkap UAS Dasar Kecerdasan Artifisial dan Pembelajaran Mesin Ganjil 2026/2027 untuk berlatih: komposisi, durasi (120 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UAS. Naskah UAS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.
>
> **Cara memakai latihan ini.** Kerjakan dalam satu kali duduk dengan batas waktu **120 menit**, *closed book*, hanya dengan kalkulator dan lembar jawaban kosong, **tanpa AI**, tanpa catatan, dan **tanpa membuka pembahasan** — sesuai aturan UAS ([kisi-kisi UAS §1](kisi-kisi-uas.md#1-ketentuan)). Catat menit yang Anda pakai per bagian (A, B, C). Bila waktu habis, tandai butir terakhir yang selesai, selesaikan sisanya, dan catat waktu tambahannya terpisah. Bila dosen memintanya, serahkan catatan itu tanpa nama — yang dipakai hanya rekap agregatnya, untuk memastikan waktu UAS cukup. Baru **sesudah** semua soal selesai, cocokkan jawaban Anda dengan [pembahasan dan pedoman skor](latihan-uas-pembahasan.md), nilai sendiri dengan pedoman skornya, lalu baca ulang bagian buku ajar yang dirujuk pembahasan untuk butir yang skornya rendah. Jangan menghafal jawaban: UAS sebenarnya memakai kasus, data, dan angka lain, jadi yang terbawa ke ujian hanyalah **cara bernalar** pada setiap jenis butir. Penandaan Sub-CPMK per butir ada di pembahasan dan di [cetak biru butir](latihan-uas-cetak-biru.md).

---

**UNIVERSITAS AL AZHAR INDONESIA**
Fakultas Sains dan Teknologi — Program Studi Informatika

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin |
| Kode | `IF52510031` |
| Semester | 5 — Ganjil 2026/2027 |
| Penyusun | Tri Aji Nugroho, S.T., M.T. |
| Waktu | **120 menit** |
| Sifat | ***Closed book*** |
| Alat bantu | **Kalkulator saja** |
| Cakupan | Seluruh semester (Minggu 1–14), penekanan Minggu 9–14 |
| Kedudukan | Latihan mandiri, **tidak dinilai**. UAS sebenarnya: Minggu 16, Tes Tulis UAS berbobot 15% nilai akhir |

**Berkas pendamping:** [pembahasan dan pedoman skor](latihan-uas-pembahasan.md) · [cetak biru butir](latihan-uas-cetak-biru.md) · [kisi-kisi UAS](kisi-kisi-uas.md) · [Latihan UTS](latihan-uts.md)

---

## Petunjuk

1. Latihan terdiri atas **tiga bagian, 10 soal, total 100 poin**: A. Konsep (5 soal, 25 poin) · B. Perancangan solusi (2 soal, 45 poin) · C. Perhitungan (3 soal, 30 poin). Bobot tiap soal dan sub-soal tertera di sampingnya.
2. Kerjakan pada lembar jawaban. Nomori jawaban sesuai nomor soal dan sub-soal. Urutan pengerjaan bebas.
3. **Tunjukkan langkah** pada setiap perhitungan. Tulis hasil dengan tiga angka di belakang koma, kecuali C2 (empat angka). Seluruh nilai $\log_2$ yang diperlukan ada pada tabel di lembar rumus. Langkah benar dengan hasil akhir keliru karena salah hitung tetap bernilai sebagian besar; hasil tanpa langkah hanya bernilai sebagian.
4. Jawab dengan singkat dan tepat. Setiap jawaban Bagian A harus memuat **alasan**, dan soal yang meminta alasan dinilai terutama dari alasannya.
5. **Bagian B tidak memiliki satu jawaban benar.** Yang dinilai adalah ketepatan penalaran dan kelengkapan pertimbangan pada keenam butir (a)–(f) ([kisi-kisi UAS §8](kisi-kisi-uas.md#8-kaidah-penilaian-bagian-b)); jawaban yang berbeda dari kunci tetapi penalarannya tepat dan konsisten memperoleh nilai penuh. Jawab setiap butir dengan beberapa kalimat atau poin ringkas, bukan esai.
6. Yang **tidak** diperkenankan: catatan, buku, telepon, laptop, dan **alat bantu AI dalam bentuk apa pun**. Kalkulator di telepon genggam tidak diperkenankan.
7. Seluruh data, nama lembaga, dan angka pada soal adalah **ilustrasi untuk keperluan latihan** (rekaan), bukan data resmi lembaga mana pun.
8. Setiap soal atau sub-soal diberi tanda level Bloom dan poin, misalnya **[C4 · 5 poin]**.
9. Pembagian waktu yang disarankan: ±5 menit di awal untuk membaca petunjuk dan lembar rumus; Bagian A ±26 menit, B ±44 menit, C ±37 menit (jumlah ±107 menit, termasuk membaca soal); paling sedikit 5 menit di akhir untuk memeriksa jawaban.

> **Pernyataan amanah.** Naskah UAS mencetak pernyataan berikut; menuliskan nama dan NIM pada lembar jawaban berarti menyetujuinya, sehingga pernyataan itu tidak perlu disalin. Biasakan sejak latihan membacanya sebelum mulai: *"Dengan menuliskan nama dan NIM pada lembar jawaban, saya menyatakan mengerjakan ujian ini sendiri, tanpa bantuan orang lain maupun alat bantu yang tidak diperkenankan."*

---

## Lembar Rumus

$$H(S)=-\sum_i p_i\log_2 p_i \qquad G(S)=1-\sum_i p_i^2 \qquad IG(S,A)=H(S)-\sum_v \frac{|S_v|}{|S|}H(S_v)$$

$$\sigma(z)=\frac{1}{1+e^{-z}} \qquad \sigma'(z)=\sigma(z)\bigl(1-\sigma(z)\bigr) \qquad w \leftarrow w-\eta\frac{\partial L}{\partial w}$$

$$s(i)=\frac{b(i)-a(i)}{\max\{a(i),b(i)\}} \qquad \text{Precision}=\frac{TP}{TP+FP} \qquad \text{Recall}=\frac{TP}{TP+FN}$$

$$\bar{x}=\frac{1}{k}\sum_i x_i \qquad s=\sqrt{\frac{\sum_i(x_i-\bar{x})^2}{k-1}} \quad \text{(}x_i\text{ = skor lipatan ke-}i\text{; simpangan baku sampel, pembagi } k-1\text{)}$$

$$d_i=\text{skor}_{A,i}-\text{skor}_{B,i} \qquad \bar d=\frac{1}{k}\sum_i d_i \qquad s_d=\sqrt{\frac{\sum_i(d_i-\bar d)^2}{k-1}} \qquad SE=\frac{s_d}{\sqrt{k}}$$

Notasi: $s(i)$ = *silhouette* titik $i$; $x_i$ = skor lipatan ke-$i$ dengan rerata $\bar{x}$ (setara dengan lembar rumus UTS, dengan $k$ (banyak lipatan) menggantikan $n$); $s$ dan $s_d$ = simpangan baku sampel (skor lipatan dan selisih berpasangan).

**Nilai $-\log_2 p$ yang sering dipakai**

| $p$ | 0,1 | 0,125 | 0,2 | 0,25 | 0,3 | 1/3 | 0,375 | 0,4 | 0,5 |
|-----|-----|-------|-----|------|-----|-----|-------|-----|-----|
| $-\log_2 p$ | 3,322 | 3,000 | 2,322 | 2,000 | 1,737 | 1,585 | 1,415 | 1,322 | 1,000 |

| $p$ | 0,6 | 0,625 | 2/3 | 0,7 | 0,75 | 0,8 | 0,875 | 0,9 | 1 |
|-----|-----|-------|-----|-----|------|-----|-------|-----|---|
| $-\log_2 p$ | 0,737 | 0,678 | 0,585 | 0,515 | 0,415 | 0,322 | 0,193 | 0,152 | 0 |

---

## BAGIAN A — KONSEP (25 poin · disarankan 26 menit)

### A1. *Ensemble* untuk Dua Masalah — **[C4 · 5 poin]**

Sebuah distributor air minum kemasan (rekaan) memprediksi apakah sebuah toko mitra akan **kehabisan stok minggu depan** (klasifikasi biner, metrik F1) dari 18 fitur. Satu fitur, `stok_akhir_minggu_ini`, jauh lebih kuat daripada fitur lainnya. Dua tim melaporkan hasilnya (F1 validasi = rerata 5 lipatan):

| Tim | Model saat ini | F1 latih | F1 validasi | Rencana tim |
|-----|----------------|----------|-------------|-------------|
| (i) | Pohon keputusan `max_depth=2` | 0,61 | 0,60 | Mengganti pohon itu dengan *Random Forest* 300 pohon yang masing-masing tetap `max_depth=2` |
| (ii) | *Random Forest* 300 pohon tanpa batas kedalaman, `max_features=None` (setiap percabangan mempertimbangkan ke-18 fitur) | 1,00 | 0,71 | Menambah jumlah pohon menjadi 1.000, karena hasilnya hampir sama dengan satu pohon tanpa batas (latih 1,00; validasi 0,70) |

Untuk **masing-masing** tim, analisislah kondisi modelnya (diagnosis dengan bukti angka dari tabel) dan apakah rencananya dapat memperbaiki F1 validasi dengan merujuk pada cara *ensemble* mengurangi galat, lalu tentukan perubahan yang lebih tepat. *(2,5 poin per tim)*

### A2. Membaca Perbandingan Model — **[C4 · 5 poin]**

Aturan praktis mata kuliah: selisih dua model yang dinilai pada lipatan yang sama dianggap bermakna bila $\lvert\bar d\rvert > 2\cdot SE$ **dan** arah selisihnya sama pada sekurang-kurangnya 4 dari 5 lipatan. Untuk **masing-masing** situasi berikut, analisislah hasilnya dengan aturan itu, lalu tentukan tindak lanjut yang tepat. *(2,5 poin per situasi)*

**(i)** Model prediksi ketidakhadiran peserta pelatihan daring, ROC-AUC pada lima lipatan yang sama:

| Lipatan | L1 | L2 | L3 | L4 | L5 |
|---------|----|----|----|----|----|
| *HistGradientBoosting* | 0,861 | 0,874 | 0,855 | 0,842 | 0,866 |
| Regresi logistik | 0,830 | 0,846 | 0,825 | 0,843 | 0,868 |

Seorang rekan menghitung $d_i$ = HistGB − logistik, memperoleh $\bar d = 0{,}0172$ dan $SE = 0{,}0077$, lalu menyimpulkan: *"$\lvert\bar d\rvert > 2\cdot SE$, jadi HistGB lebih baik secara bermakna."*

**(ii)** Pada masalah lain (F1, lima lipatan yang sama), SVM (RBF) dan *HistGradientBoosting* yang disetel dengan anggaran sebanding dibandingkan dengan *Gaussian Naive Bayes* tanpa penyetelan. SVM − NB: $\bar d = 0{,}006$, $SE = 0{,}005$, selisih positif pada 3 dari 5 lipatan. HistGB − NB: $\bar d = 0{,}004$, $SE = 0{,}006$, positif pada 2 dari 5 lipatan. F1 ketiga model 0,61–0,62, jauh di atas F1 *baseline* (0,31). Pada situasi ini, analisislah juga apa yang ditunjukkan hasil tersebut tentang sumber keterbatasan kinerja ketiga model.

### A3. Memilih Metode *Clustering* — **[C4 · 5 poin]**

Untuk **masing-masing** kebutuhan berikut, analisislah sekurang-kurangnya dua karakteristik data yang menentukan pilihan metode, lalu tentukan metode yang paling sesuai di antara K-Means, *hierarchical clustering*, dan DBSCAN beserta alasannya. *(2,5 poin per kebutuhan)*

- **(i)** Badan penanggulangan bencana sebuah kabupaten (rekaan) ingin menemukan zona rawan dari 1.800 titik kejadian longsor sepuluh tahun terakhir (koordinat). Pada peta, titik-titik itu berderet memanjang mengikuti lereng di sepanjang aliran sungai, dan ada beberapa titik yang terpencil sendirian. Jumlah zona tidak diketahui.
- **(ii)** Sebuah aplikasi dompet digital (rekaan) ingin membagi 2,4 juta penggunanya menjadi **tepat lima segmen**, karena tim pemasaran telah menyiapkan lima paket promosi. Fiturnya (frekuensi transaksi, nilai rata-rata transaksi, jumlah jenis layanan yang dipakai) sudah diskalakan.

### A4. Membeli Data Tambahan? — **[C4 · 5 poin]**

Dua tim di sebuah perusahaan asuransi kesehatan (rekaan) ditawari tambahan 8.000 baris data berlabel dengan biaya yang sama. Kurva pembelajaran masing-masing (F1, rerata 5 lipatan):

| Ukuran data latih | 1.000 | 2.000 | 4.000 | 8.000 |
|-------------------|-------|-------|-------|-------|
| Tim P — latih | 0,99 | 0,97 | 0,95 | 0,93 |
| Tim P — validasi | 0,64 | 0,71 | 0,77 | 0,82 |
| Tim Q — latih | 0,69 | 0,68 | 0,68 | 0,68 |
| Tim Q — validasi | 0,65 | 0,67 | 0,67 | 0,67 |

Untuk **masing-masing** tim, analisislah kurvanya untuk mendiagnosis kondisi model (diagnosis dengan bukti angka dari tabel), lalu tentukan apakah tim itu sebaiknya membeli data tambahan; bila tidak, tentukan tindakan yang lebih tepat. *(2,5 poin per tim)*

### A5. PCA dan t-SNE dalam Laporan Model — **[C4 · 5 poin]**

Sebuah tim membangun model untuk memutuskan **klaim asuransi usaha tani** (rekaan) diterima atau ditolak, dari 30 fitur. Petani yang klaimnya ditolak berhak menerima penjelasan alasan penolakannya. Laporan tim memuat dua keputusan:

- **(i)** *"Ke-30 fitur kami ringkas dengan PCA menjadi 6 komponen pertama (90% varians), lalu keenam komponen itu menjadi masukan regresi logistik agar model lebih ringkas."*
- **(ii)** *"Pada plot t-SNE, klaim dari kelompok tani dataran tinggi membentuk klaster yang letaknya jauh dari klaster dataran rendah, jadi kedua kelompok itu sangat berbeda. Koordinat t-SNE dua dimensi itu kami tambahkan sebagai fitur model."*

Untuk **masing-masing** keputusan, analisislah masalahnya, lalu tentukan perbaikannya. *(2,5 poin per keputusan)*

---

## BAGIAN B — PERANCANGAN SOLUSI (45 poin · disarankan 44 menit)

Kedua soal menuntut enam hal yang sama ([kisi-kisi UAS §4](kisi-kisi-uas.md#4-bentuk-soal-bagian-b)). Jawab setiap butir (a)–(f) secara ringkas.

### B1. Paket COD yang Ditolak Penerima — **[22,5 poin]**

Sebuah perusahaan jasa pengiriman (rekaan) melayani pengiriman bayar di tempat (*cash on delivery*, COD) untuk ribuan toko daring. Sekitar **9%** paket COD **ditolak penerima** saat diantar. Setiap paket yang ditolak dikembalikan ke penjual: perusahaan menanggung ongkos kirim pulang-pergi (rata-rata Rp38.000) dan stok penjual tertahan ±10 hari. Perusahaan ingin menandai pesanan COD yang berisiko agar pembelinya dapat ditelepon petugas untuk konfirmasi ulang **sebelum paket dijemput dari penjual** (±Rp3.000 per panggilan); sebagian pembeli yang ditelepon membatalkan pesanan walaupun sebenarnya akan menerimanya. Pesanan pengiriman dibuat penjual di aplikasi, lalu paket dijemput kurir pada hari yang sama atau esoknya.

Data: 480.000 pesanan COD selama 18 bulan (Januari 2025–Juni 2026) dari ±150.000 pembeli di seluruh Indonesia; rata-rata 3,2 pesanan per pembeli. Kolom yang tersedia:

| Kolom | Keterangan |
|-------|------------|
| `nilai_barang`, `ongkir` | Rupiah, tercatat saat pesanan dibuat |
| `kategori_barang` | 25 kategori |
| `jumlah_percobaan_antar` | Berapa kali kurir mencoba mengantar paket itu |
| `kecamatan_tujuan` | ±7.000 kecamatan |
| `riwayat_tolak_pembeli` | Jumlah paket yang pernah ditolak pembeli itu **sebelum** tanggal pesanan |
| `balas_konfirmasi_otomatis` | Apakah pembeli membalas pesan otomatis yang dikirim sistem ketika paket tiba di gudang kota tujuan |
| `jam_pesan` | Jam pesanan dibuat |
| `ditolak` | Target: 1 = paket ditolak penerima |

- **(a)** Rumuskan *task*-nya: target (peristiwa yang dihitung dan batas waktu pengamatannya), jenis *task*, dan **kapan** prediksi dibutuhkan. **[C6 · 2,5 poin]**
- **(b)** Analisislah kolom yang tersedia, lalu tentukan **dua** kolom yang tidak boleh dipakai sebagai fitur karena menimbulkan kebocoran data (*data leakage*), beserta alasannya. **[C4 · 2,5 poin]**
- **(c)** Analisislah kerugian akibat kedua jenis kesalahan model pada kasus ini dan mana yang lebih berat, lalu tentukan metrik evaluasi yang mencerminkan hasil analisis itu. **[C4 · 2,5 poin]**
- **(d)** Pilih minimal tiga model kandidat, dan beri argumentasi pemilihan masing-masing yang dikaitkan dengan sifat data atau kebutuhan kasus ini. **[C5 · 4,5 poin]**
- **(e)** Rancang protokol evaluasi yang adil: cara membagi data beserta alasannya (termasuk pemakaian data uji), cara memvalidasi dan menyetel hiperparameter, cara membandingkan kandidat, dan *baseline* yang paling bermakna untuk kasus ini. **[C6 · 5,5 poin]**
- **(f)** Nilailah dua risiko etis penerapan model ini — siapa yang dirugikan dan bagaimana — lalu tetapkan cara menangani masing-masing. **[C5 · 5 poin]**

### B2. Perkiraan Produktivitas Padi per Desa — **[22,5 poin]**

Dinas pertanian sebuah provinsi (rekaan) ingin memperkirakan **produktivitas padi (ton gabah kering panen per hektare) setiap desa** pada musim tanam berjalan. Perkiraan dipakai untuk dua hal: merencanakan kapasitas gudang dan dana serapan gabah oleh badan usaha milik daerah (BUMD) pangan, dan menetapkan desa prioritas bantuan benih. Keputusan diambil **6 minggu sebelum panen**; panen umumnya pada **minggu ke-16 sejak tanam**. Seorang anggota tim mengusulkan jaringan saraf tiruan karena "paling canggih".

Data: 2.400 desa × 8 musim tanam (2022–2025) = 19.200 baris; rata-rata produktivitas 5,4 ton/ha. Kolom yang tersedia:

| Kolom | Keterangan |
|-------|------------|
| `indeks_hijau_m1` … `indeks_hijau_m16` | Indeks kehijauan tanaman dari citra satelit (sudah berupa angka), satu kolom per minggu sejak tanam; kolom yang berdekatan berkorelasi sangat kuat |
| `hujan_kumulatif_8_minggu` | Curah hujan kumulatif minggu ke-1 sampai ke-8 sejak tanam (mm) |
| `irigasi_teknis` | Ya/Tidak |
| `varietas_dominan` | 12 varietas |
| `luas_tanam_ha` | Luas tanam padi desa itu pada musim tersebut |
| `pupuk_tersalur_kg_ha` | Pupuk bersubsidi yang tersalur ke desa itu sampai minggu ke-6 sejak tanam |
| `rerata_produktivitas_3_musim_lalu` | Rata-rata produktivitas desa itu pada tiga musim sebelumnya |
| `produksi_ton` | Total gabah desa itu pada musim tersebut, dicatat saat panen |
| `produktivitas` | Target: ton/ha, dari survei ubinan saat panen |

- **(a)** Rumuskan *task*-nya: target (besaran dan cara pengukurannya), jenis *task*, dan **kapan** prediksi dibutuhkan (nyatakan dalam minggu sejak tanam). **[C6 · 2,5 poin]**
- **(b)** Analisislah kolom yang tersedia, lalu tentukan **dua** kolom atau kelompok kolom yang tidak boleh dipakai sebagai fitur karena menimbulkan kebocoran data (*data leakage*), beserta alasannya. **[C4 · 2,5 poin]**
- **(c)** Bandingkan dampak perkiraan yang terlalu tinggi dan yang terlalu rendah pada kedua pemakaian perkiraan, lalu tentukan metrik evaluasi yang sesuai dengan perbandingan itu, beserta ukuran pelengkap yang memperlihatkan perbedaan dampak tersebut. **[C4 · 2,5 poin]**
- **(d)** Pilih minimal tiga model kandidat, dan beri argumentasi pemilihan masing-masing yang dikaitkan dengan sifat data atau kebutuhan kasus ini. **[C5 · 4,5 poin]**
- **(e)** Rancang protokol evaluasi yang adil: cara membagi data beserta alasannya (termasuk pemakaian data uji), cara memvalidasi dan menyetel hiperparameter, cara membandingkan kandidat, dan *baseline* yang paling bermakna untuk kasus ini. **[C6 · 5,5 poin]**
- **(f)** Nilailah dua risiko etis penerapan model ini — siapa yang dirugikan dan bagaimana — lalu tetapkan cara menangani masing-masing. **[C5 · 5 poin]**

---

## BAGIAN C — PERHITUNGAN (30 poin · disarankan 37 menit)

### C1. Memilih Percabangan Akar — **[10 poin]**

Perpustakaan daerah sebuah kota (rekaan) membangun pohon keputusan untuk memprediksi peminjaman yang **terlambat dikembalikan** (positif). Simpul akar memuat **48 peminjaman: 12 terlambat dan 36 tepat waktu**. Tiga kandidat percabangan:

| Kandidat | Cabang | n | Terlambat | Tepat waktu |
|----------|--------|---|-----------|-------------|
| P: `durasi_pinjam_hari` > 14 | Ya | 16 | 8 | 8 |
| | Tidak | 32 | 4 | 28 |
| Q: `usia_peminjam` ≤ 25 | Ya | 24 | 9 | 15 |
| | Tidak | 24 | 3 | 21 |
| R: `nomor_anggota` ≤ 1.203 | Ya | 3 | 3 | 0 |
| | Tidak | 45 | 9 | 36 |

`durasi_pinjam_hari` dipilih peminjam saat meminjam; `nomor_anggota` adalah nomor urut pendaftaran anggota. *Information gain* kandidat Q telah dihitung: 0,062.

- **(a)** Hitung *entropy* dan *Gini impurity* simpul akar. **[C3 · 2 poin]**
- **(b)** Hitung *entropy* kedua cabang kandidat P, lalu *information gain*-nya. **[C3 · 3 poin]**
- **(c)** Hitung *information gain* kandidat R. **[C3 · 2 poin]**
- **(d)** Tentukan kandidat yang dipilih pohon tanpa pembatasan. Analisislah apakah percabangan itu layak dipakai untuk memprediksi peminjaman baru, lalu tentukan, beserta alasannya, kandidat yang dipilih bila pohon dilatih dengan `min_samples_leaf=5` (di antara ketiga kandidat). **[C4 · 3 poin]**

### C2. Satu Langkah Pelatihan Jaringan Saraf — **[10 poin]**

Jaringan 2-2-1 memakai aktivasi sigmoid pada lapis tersembunyi dan keluaran; seluruh bias 0.

| Lapis | Bobot |
|-------|-------|
| Masukan → tersembunyi | $w_{11}=0{,}3$, $w_{21}=-0{,}2$ (ke $h_1$); $w_{12}=-0{,}1$, $w_{22}=0{,}4$ (ke $h_2$) |
| Tersembunyi → keluaran | $v_1=0{,}8$, $v_2=-0{,}5$ |

dengan $z_1=w_{11}x_1+w_{21}x_2$, $z_2=w_{12}x_1+w_{22}x_2$, dan $z_{\text{out}}=v_1h_1+v_2h_2$. Satu contoh latih: $x=[2,\ 1]$, target $y=1$, laju pembelajaran $\eta=0{,}5$. *Loss* $L=(y-\hat y)^2$, sehingga $\partial L/\partial\hat y=-2(y-\hat y)$.

- **(a)** Hitung $z_1$, $z_2$, $h_1$, dan $h_2$. **[C3 · 2 poin]**
- **(b)** Hitung $z_{\text{out}}$, $\hat y$, dan $L$. **[C3 · 1,5 poin]**
- **(c)** Hitung $\delta_{\text{out}}$, $\partial L/\partial v_1$, dan $\partial L/\partial v_2$, lalu perbarui $v_1$ dan $v_2$. **[C3 · 3 poin]**
- **(d)** Hitung $\delta_{h_2}$ (pakai $v_2$ sebelum diperbarui) dan $\partial L/\partial w_{22}$, lalu perbarui $w_{22}$. **[C3 · 1,5 poin]**
- **(e)** Tentukan arah perubahan (naik atau turun) $v_2$ dan $w_{22}$ dari hasil (c) dan (d). Analisislah, dengan memperhatikan tanda $v_2$, mengapa kedua perubahan itu sama-sama mendorong $\hat y$ mendekati target. **[C4 · 2 poin]**

### C3. *Silhouette* Hasil Pengelompokan Desa Wisata — **[10 poin]**

Dinas pariwisata sebuah kabupaten (rekaan) mengelompokkan tujuh desa wisata rintisan, D1–D7, dengan K-Means (k = 3) berdasarkan dua indikator yang sudah diskalakan: jumlah kunjungan per bulan dan lama tinggal rata-rata. Hasilnya: klaster A = {D1, D2, D3}, B = {D4, D5}, C = {D6, D7}. Jarak Euclidean antardesa pada data terskala (dibulatkan satu desimal):

|    | D1 | D2 | D3 | D4 | D5 | D6 | D7 |
|----|----|----|----|----|----|----|----|
| **D1** | 0 | 2,0 | 2,2 | 10,0 | 5,8 | 7,0 | 8,0 |
| **D2** | 2,0 | 0 | 1,0 | 8,5 | 4,2 | 5,0 | 6,0 |
| **D3** | 2,2 | 1,0 | 0 | 7,8 | 3,6 | 5,1 | 6,1 |
| **D4** | 10,0 | 8,5 | 7,8 | 0 | 4,2 | 6,1 | 6,0 |
| **D5** | 5,8 | 4,2 | 3,6 | 4,2 | 0 | 3,6 | 4,2 |
| **D6** | 7,0 | 5,0 | 5,1 | 6,1 | 3,6 | 0 | 1,0 |
| **D7** | 8,0 | 6,0 | 6,1 | 6,0 | 4,2 | 1,0 | 0 |

Profil klaster pada indikator asli: A — kunjungan rendah, lama tinggal singkat · B — kunjungan tinggi, lama tinggal sedang sampai panjang · C — kunjungan rendah, lama tinggal panjang.

- **(a)** Hitung $a(i)$, $b(i)$, dan $s(i)$ untuk D2 dan D5. **[C3 · 4 poin]**
- **(b)** Nilai *silhouette* lima desa lainnya: D1 0,720 · D3 0,714 · D4 0,306 · D6 0,794 · D7 0,804. Hitung rerata *silhouette* ketujuh desa. **[C3 · 1 poin]**
- **(c)** Analisislah arti nilai $s(\text{D5})$ yang Anda peroleh, lalu tentukan apa yang perlu dilakukan terhadap D5 sebelum hasil pengelompokan dipakai. **[C4 · 2 poin]**
- **(d)** Dengan k = 2 (klaster A tetap; B dan C bergabung), rerata *silhouette* 0,501. Dinas hanya sanggup menjalankan **dua** jenis program pendampingan tahun ini. Bandingkan hasil k = 2 dan k = 3 dengan mempertimbangkan *silhouette* (termasuk apa yang tidak diukurnya) dan kebermaknaan hasil bagi dinas, lalu tentukan k yang Anda sarankan beserta alasannya. **[C4 · 3 poin]**

---

**— Selesai. Periksa kembali nomor jawaban Anda, lalu buka [pembahasan](latihan-uas-pembahasan.md). —**

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
