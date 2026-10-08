---
id: uai-if52510031-latihan-uts-pembahasan
tipe: asesmen
judul: "Latihan UTS — Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — Pembahasan dan Pedoman Skor"
kode_mk: IF52510031
nama_mk: Dasar Kecerdasan Artifisial dan Pembelajaran Mesin
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-08
---

# Pembahasan dan Pedoman Skor — Latihan UTS Dasar Kecerdasan Artifisial dan Pembelajaran Mesin

## Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — IF52510031

> **Latihan UTS — bukan naskah UTS.** Pembahasan ini menyertai simulasi lengkap UTS Dasar Kecerdasan Artifisial dan Pembelajaran Mesin Ganjil 2026/2027 untuk berlatih: komposisi, durasi (120 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UTS. Naskah UTS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.
>
> **Kerjakan dulu [latihan UTS](latihan-uts.md) dalam 120 menit tanpa AI dan tanpa membuka berkas ini.** Sesudahnya, nilai jawaban Anda dengan pedoman skor, lalu bandingkan dengan contoh jawaban *Kurang*, *Cukup*, dan *Baik*. Untuk butir yang skornya di bawah separuh, baca ulang bagian buku ajar pada baris **Rujukan** butir itu. Contoh jawaban *Baik* — tersedia untuk setiap soal Bagian A dan B serta setiap sub-soal analisis Bagian C — menunjukkan unsur yang dinilai, bukan satu-satunya rumusan yang benar, dan sengaja ditulis **seringkas jawaban bernilai penuh**: nilai penuh hanya menuntut unsur yang dinilai, sedangkan menulis lebih panjang tidak menambah skor dan menghabiskan waktu butir lain. Untuk sub-soal hitung, langkah pada pembahasan sudah merupakan jawaban lengkap. Tabel *jawaban model* memuat penjelasan untuk belajar, sehingga lebih panjang daripada yang perlu ditulis di ujian. Menghafal jawaban di sini tidak membantu: naskah UTS memakai konteks dan angka lain, jadi yang perlu dikuasai adalah **langkah dan alasannya**.

| Aspek | Keterangan |
|-------|------------|
| Soal | [Latihan UTS](latihan-uts.md) (13 soal, 100 poin) |
| Cetak biru | [Cetak biru butir dan panduan varian](latihan-uts-cetak-biru.md) |
| Penandaan | Judul tiap butir mencantumkan Sub-CPMK (kode registri), level Bloom, dan skor. Sub-CPMK ditetapkan **menurut isi butir** untuk analisis ketercapaian; bobot Tes Tulis UTS (20%) tetap tercatat pada `DAIML-Sub-CPMK102-1` sesuai registri ([cetak biru §1](latihan-uts-cetak-biru.md#1-prinsip-penandaan)) |
| Penyusun | Tri Aji Nugroho, S.T., M.T. |
| Verifikasi angka | Seluruh angka Bagian C, B2(b), dan A3 dihitung ulang dengan Python; perilaku potongan kode B1 dan B3 serta kode rujukan diperiksa pada scikit-learn 1.6 dan 1.9 (§5) |

---

## 0. Kaidah Umum Penilaian

Mengikuti kaidah penilaian [kisi-kisi UTS §8](kisi-kisi-uts.md#8-kaidah-penilaian) dan rubrik ujian tulis [kerangka asesmen §5.4](assessment-framework.md#54-rubrik-ujian-tulis).

| Situasi | Penilaian |
|---------|-----------|
| Jawaban benar, langkah ditunjukkan | Nilai penuh |
| Langkah benar, hasil akhir salah karena kekeliruan hitung | **Nilai sebagian besar**: poin langkah penuh, sedangkan poin hasil unsur itu dipotong **separuh, dibulatkan ke atas ke kelipatan 0,25** (bagian hasil 0,25 atau 0,5 → potong 0,25; 0,75 atau 1 → potong 0,5; 1,25 atau 1,5 → potong 0,75). Bila pedoman skor suatu unsur tidak memisahkan langkah dan hasil, separuh poinnya dianggap langkah dan separuh hasil. Hasil yang salah karena rumus atau langkah yang salah (mis. pembagi $n$ pada C3(a)) dinilai menurut tabel kesalahan umum §4. **Kesalahan terbawa** (*error carried forward*): angka keliru yang dipakai dengan benar di langkah berikutnya tidak dihukum dua kali |
| Hasil benar tanpa langkah | Paling banyak 50% poin sub-soal |
| Jawaban benar tanpa alasan pada soal yang meminta alasan | Paling banyak 40% poin — **hanya untuk butir yang pedoman skornya tidak merinci unsur alasan**. Bila pedoman skor butir merinci unsur alasan secara terpisah, rincian butir itulah yang berlaku (unsur alasan yang tidak ditulis bernilai 0, unsur lain dinilai menurut isinya) |
| Penalaran tepat, kesimpulan berbeda dari kunci tetapi konsisten | **Nilai penuh** — khususnya Bagian B; pembahasan mencantumkan alternatif yang sudah diantisipasi |
| Sintaks kode kurang tepat, alur benar | Tidak dikurangi (kisi-kisi §4: sintaks lengkap tidak diuji) |
| Pembulatan | Toleransi ±0,002 untuk metrik 0–1, ±0,02 untuk MAE/RMSE, ±0,01 untuk rasio RMSE/MAE; pembulatan di tengah langkah tidak dihukum bila hasil akhir berada dalam toleransi |
| Bahasa sebab-akibat pada data observasional (mis. "X menyebabkan Y") | Tidak ada pengurangan tersendiri ([kerangka asesmen §7.1](assessment-framework.md#71-tabel-pengurangan) adalah satu-satunya daftar pengurangan). Klaim sebab-akibat hanya memengaruhi unsur tafsir pada sub-soal yang memang menilainya: A1(ii) unsur "kausal vs korelasi" dan C3(d) unsur "bahasa jujur" |

**Satuan skor terkecil: 0,25 poin.** Skor dicatat per baris: satu baris = satu soal Bagian A (bagian berlabel di dalamnya tidak dipisah) atau satu sub-soal Bagian B/C — 33 baris skor ([cetak biru §2](latihan-uts-cetak-biru.md#2-tabel-cetak-biru-per-butir)).

Pada A3, A4, dan A5 soal hanya mencetak skor total. Rincian poin per baris pada pedoman skor di bawah sengaja tidak dicetak pada soal, agar bobot baris tidak menandai baris yang "tepat", "bukan masalah", atau "pertahankan".

Singkatan Sub-CPMK pada tabel: `082-1` = `DAIML-Sub-CPMK082-1`; `102-1` = `DAIML-Sub-CPMK102-1`.

---

## 1. Bagian A — Konsep (30 poin)

### A1. Layak Tidaknya Pembelajaran Mesin — `DAIML-Sub-CPMK082-1` · C4 · 5 poin

**Jawaban model** (Bab 1 §1.4)

| Usulan | Kesimpulan | Alasan | Pendekatan |
|--------|------------|--------|------------|
| (i) Tonase sampah TPST | **Layak** memakai ML | Ada pola (hari dalam minggu, hari libur, musim hujan) yang tidak dapat ditulis sebagai aturan pasti (pertanyaan 1); data tiga tahun tersedia (pertanyaan 2); kesalahan dapat ditoleransi — ada truk cadangan, dampaknya terbatas (pertanyaan 3); keluaran langsung dipakai menjadwalkan truk (pertanyaan 4) | Regresi dengan **pembagian temporal**; wajib mengalahkan *baseline* sederhana (pertanyaan 5), mis. tonase hari yang sama minggu lalu atau rata-rata empat minggu terakhir |
| (ii) Program sarapan sehat | **Tidak** memakai ML prediktif untuk menjawab pertanyaan ini | Keadaan "yang dibutuhkan sebab-akibat, bukan prediksi": ML mempelajari korelasi. Sekolah peserta **tidak dipilih acak** (diusulkan kepala sekolah), sehingga perbedaan nilai dapat berasal dari sifat sekolah pengusul, bukan dari program | Rancangan eksperimen atau inferensi kausal — mis. uji coba acak pada tahap perluasan program, atau pembanding sebelum–sesudah dengan sekolah bukan peserta yang sebanding. Bila hanya data observasional, kesimpulan memakai "dikaitkan dengan" |

**Pedoman skor**

| Bagian | Poin | Rincian |
|--------|------|---------|
| (i) | 2,5 | Kesimpulan "layak" 0,5 · alasan memakai ≥ 2 pertanyaan uji kelayakan atau keadaan 1,0 (satu pertanyaan saja 0,5) · pendekatan: regresi atau perkiraan deret waktu 0,25 + pembagian/evaluasi temporal 0,25 · pembanding (*baseline*) yang harus dikalahkan, yang diminta soal (pertanyaan 5 uji kelayakan, "pembanding sederhana") 0,5 — boleh muncul pada alasan maupun pendekatan |
| (ii) | 2,5 | Kesimpulan "tidak (ML prediktif)" 0,5 · kausal vs korelasi 0,75 · masalah seleksi non-acak 0,5 · pendekatan eksperimen/inferensi kausal 0,75 |

Alternatif yang diterima: pada (i), "layak, **dengan syarat**" (data hari libur lengkap, mengalahkan *baseline*) dinilai penuh. Pada (ii), "ML boleh dipakai sebagai alat eksplorasi, tetapi tidak untuk menjawab 'menyebabkan'" dinilai penuh bila pendekatan kausalnya disebut.

**Contoh jawaban**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "(i) Pakai ML. (ii) Pakai ML regresi untuk melihat pengaruh program." | 0,5 (hanya kesimpulan i) |
| Cukup | "(i) Perlu ML karena datanya banyak. (ii) Tidak, karena ML hanya korelasi." | 2,25 (i 1,0 — alasan hanya satu pertanyaan; pendekatan dan pembanding tidak ada · ii 1,25 — seleksi non-acak dan pendekatan tidak disebut) |
| Baik | "(i) Layak — ada pola libur/hujan yang tidak dapat ditulis sebagai aturan dan data 3 tahun tersedia; regresi dengan evaluasi temporal yang harus mengalahkan *baseline* 'tonase hari yang sama minggu lalu'. (ii) Tidak — pertanyaannya sebab-akibat, sedangkan ML hanya menangkap korelasi, dan sekolah peserta dipilih dari usulan (tidak acak); perlu uji coba acak." | 5 |

**Rujukan:** [Bab 1](../06-buku-ajar/bab-01-lanskap-kecerdasan-artifisial.md) §1.4.1 (lima keadaan), §1.4.2 (uji kelayakan enam pertanyaan).

---

### A2. Kembali ke Tahap Mana? — `DAIML-Sub-CPMK082-1` · C4 · 5 poin

**Jawaban model** (Bab 2 §2.5 dan §2.5.2)

| Situasi | Tahap | Alasan | Tindakan |
|---------|-------|--------|----------|
| (i) MAE naik terus sejak ruas tol baru | **Data** (tahap 2), dipicu pemantauan (tahap 6) | Kinerja menurun **setelah diterapkan** dan bertepatan dengan perubahan dunia nyata → pergeseran distribusi (*drift*): pola lalu lintas yang dipelajari model tidak lagi berlaku | Kumpulkan data sesudah ruas baru tersambung, latih ulang, pertimbangkan fitur penanda perubahan, perketat pemantauan |
| (ii) F1 model = F1 aturan sederhana | **Eksplorasi dan penyiapan** (tahap 3) | Model ≈ *baseline* → fitur yang tersedia tidak memuat sinyal tambahan untuk target ini (Bab 2 §2.4.2) | Kepada manajemen: **pakai aturan sederhana sekarang** — kinerja sama, lebih murah, mudah dijelaskan, tanpa biaya pemeliharaan model; model baru dipertimbangkan bila kelak mengungguli aturan dengan selisih yang bermakna setelah rekayasa fitur atau sumber data baru |

**Pedoman skor**

| Bagian | Poin | Rincian |
|--------|------|---------|
| (i) | 2,5 | Tahap 0,75 · bukti *drift* (naik terus sejak perubahan) 0,75 · tindakan (data baru + latih ulang) 1,0 — latih ulang tanpa menyebut pengumpulan data sesudah perubahan 0,5 |
| (ii) | 2,5 | Tahap 0,5 · alasan model ≈ *baseline* 0,75 · tindakan bagi manajemen: memakai aturan 1,0 · syarat selisih bermakna atau biaya pemeliharaan 0,25 |

Alternatif yang diterima (buku ajar memberi dua rujukan: diagram §2.5 menggambar panah dari tahap 6 ke tahap 1 "bila kinerja menurun", sedangkan tabel §2.5.2 menyebut *drift* kembali ke tahap 2):

| Situasi | Jawaban tahap | Perlakuan |
|---------|---------------|-----------|
| (i) | Formulasi masalah (tahap 1) | **Penuh** bila alasannya *drift* dan tindakannya memuat data baru/latih ulang |
| (i) | Eksplorasi dan penyiapan (tahap 3), atau penerapan dan pemantauan (tahap 6) saja | Poin tahap **0,25**; bukti dan tindakan tetap dinilai menurut isinya (pemantauan adalah tahap yang mendeteksi, bukan tahap yang diperbaiki) |
| (ii) | Data (tahap 2) | **Penuh** bila alasannya data yang ada kurang memuat sinyal dan diusulkan sumber data/fitur baru (§2.4.2 "Cari fitur lain"), disertai saran memakai aturan |
| (ii) | Formulasi masalah (tahap 1) | **Penuh** bila alasannya target mungkin tidak dapat diprediksi dari data yang ada, disertai saran memakai aturan |
| (ii) | *Baseline* dan model (tahap 4) dengan saran "ganti algoritma" | Poin tahap 0; alasan dan tindakan tetap dinilai menurut isinya |

**Contoh jawaban**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "(i) Evaluasi. (ii) Model, ganti algoritma yang lebih kuat." | 0 |
| Cukup | "(i) Data — pola lalu lintas berubah sejak ruas baru; latih ulang. (ii) Eksplorasi dan penyiapan — model tidak lebih baik daripada aturan, jadi fiturnya kurang; cari fitur baru." | 3,25 (i 2,0 — tindakan tanpa pengumpulan data baru 0,5 · ii 1,25 — tindakan bagi manajemen tidak ada) |
| Baik | "(i) Data — MAE naik terus sejak ruas baru tersambung: *drift*; kumpulkan data sesudah ruas baru, lalu latih ulang. (ii) Eksplorasi dan penyiapan — F1 model sama dengan aturan, jadi fitur tidak menambah sinyal; manajemen sebaiknya memakai aturan sekarang karena lebih murah, dan model baru dipakai bila kelak unggul dengan selisih bermakna." | 5 |

**Rujukan:** [Bab 2](../06-buku-ajar/bab-02-formulasi-masalah-daur-hidup-ml.md) §2.4.2 (membaca selisih terhadap *baseline*), §2.5 dan §2.5.2 (daur hidup dan pemicunya).

---

### A3. Membaca Hasil Pemeriksaan Kualitas Data — `DAIML-Sub-CPMK102-1` · C4 · 5 poin

| Temuan | Masalah? | Penyebab / alasan | Tindakan |
|--------|----------|-------------------|----------|
| T1 `berat_badan_kg` min −99 | **Ya** | Kode nilai hilang yang tidak diterjemahkan | Ubah −99 menjadi `NaN` **sebelum apa pun** (sebelum menghitung statistik atau imputasi), lalu tangani nilai hilang di dalam `Pipeline` |
| T2 `usia_tahun` = 0 di poli KIA | **Tidak** | Berat 2,5–9,8 kg pada seluruh 412 baris itu hanya mungkin untuk bayi, bukan ibu hamil atau nifas; bayi di bawah satu tahun wajar tercatat 0 tahun. Aturan "0 pada kolom yang mustahil → kode nilai hilang" (Bab 3 §3.2.2) tidak berlaku karena 0 di sini **tidak mustahil** | Tidak diminta soal. Nilai tambah: biarkan; pakai usia dalam bulan untuk balita |
| T3 korelasi 0,96 dengan target | **Ya** — curigai kebocoran | Jumlah kunjungan "tahun ini" kemungkinan ikut menghitung kunjungan ulang yang hendak diprediksi (informasi masa depan) | Periksa cara penghitungannya; ganti dengan "jumlah kunjungan dalam 12 bulan **sebelum** kunjungan ini"; jangan dirayakan sebelum diselidiki |

**Pedoman skor**

- **T1 (1,5):** penilaian masalah 0,25 · penyebab 0,5 · tindakan 0,75 (mengubah ke `NaN` tanpa menyebut urutan "sebelum statistik/imputasi" 0,5; "imputasi median" tanpa mengubah −99 ke `NaN` lebih dahulu 0,25).
- **T2 (1,75):** penilaian "bukan masalah" 0,25 · alasan yang memakai bukti (berat badan bayi dan/atau poli KIA) 1,5. Untuk temuan yang bukan masalah, soal hanya meminta alasan; tindakan ("biarkan", usia dalam bulan) adalah nilai tambah dan tidak diberi poin tersendiri. "Bukan masalah" tanpa alasan = 0,25. "Perlu diverifikasi — wajar untuk bayi, periksa silang berat badan" dinilai **penuh** bila kesimpulannya memakai data berat 2,5–9,8 kg. "Datanya sah, tetapi usia dalam tahun bulat hampir tidak membawa informasi bagi bayi — pakai usia dalam bulan" dinilai **penuh** bila memakai data berat badan bayi. "Masalah, ganti dengan NaN" yang mengabaikan data berat badan = 0.
- **T3 (1,75):** penilaian masalah 0,25 · penyebab (informasi masa depan/ikut menghitung target) 0,75 — menyebut "bocor"/"kebocoran" tanpa mekanismenya 0,25 · tindakan (periksa definisi, ganti dengan hitungan sebelum saat prediksi) 0,75.

**Contoh jawaban**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "T1 hapus barisnya. T2 usia 0 salah, hapus. T3 bagus, fitur kuat." | 0,25 (T1 penilaian) |
| Cukup | "T1 −99 kode hilang, ganti NaN. T2 tidak masalah. T3 korelasi tinggi, mungkin bocor." | 2,0 (T1 1,25 — urutan tidak disebut · T2 0,25 — tanpa alasan · T3 0,5 — penilaian 0,25 + penyebab sebagian 0,25 karena mekanisme kebocoran tidak disebut; tindakan tidak ada) |
| Baik | "T1 masalah: −99 adalah kode nilai hilang; ubah ke NaN sebelum menghitung statistik dan imputasi. T2 bukan masalah: berat 2,5–9,8 kg berarti bayi, jadi usia 0 tahun wajar. T3 masalah: jumlah kunjungan tahun ini ikut menghitung kunjungan ulang yang hendak diprediksi (informasi masa depan); ganti dengan jumlah kunjungan 12 bulan sebelum kunjungan ini." | 5 |

**Rujukan:** [Bab 3](../06-buku-ajar/bab-03-data-dan-prapemrosesan.md) §3.2.2 (tanda bahaya dan penyebabnya); [Bab 4](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md) §4.5.5 (kebocoran target).

---

### A4. Menganalisis Keputusan Prapemrosesan — `DAIML-Sub-CPMK102-1` · C4 · 5 poin

| Baris | Tepat? | Akibat pada k-NN | Perbaikan |
|-------|--------|------------------|-----------|
| 1 `skala_nyeri` | **Tidak** | Skala 0–10 bersifat **berurutan**; *one-hot* membuang urutan (nyeri 9 dianggap sama jauhnya dari 8 dan dari 0) dan menambah 11 kolom jarang yang memperbesar dimensi — jarak k-NN makin kurang bermakna | Perlakukan sebagai numerik lalu diskalakan, atau `OrdinalEncoder` dengan urutan 0–10 |
| 2 `biaya_rawat_sebelumnya` | **Kurang tepat** | Rerata dan simpangan baku tertarik oleh segelintir pencilan; mayoritas pasien termampatkan dalam rentang sangat sempit sehingga fitur ini praktis tidak membedakan pasien biasa, sementara pencilan berjarak sangat jauh | Transformasi `log(x+1)` lalu penskalaan, atau `RobustScaler` (median/IQR); terbaik: log lalu skala |
| 3 `cara_bayar` | **Tepat** | Nominal tanpa urutan, sedikit kategori → *one-hot* tepat; `handle_unknown="ignore"` mencegah prediksi gagal bila kelak muncul cara bayar baru | — |

**Pedoman skor:** baris 1 dan 2 (masing-masing 1,75) = penilaian 0,25 · akibat 0,75 · perbaikan 0,75. Baris 3 (1,5) = penilaian "tepat" 0,5 · alasan 1,0. Baris 2: `RobustScaler` saja dinilai penuh; "hapus pencilan" tanpa alasan = 0,25 pada perbaikan.

**Contoh jawaban**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "1 benar karena kategori. 2 benar, k-NN butuh penskalaan. 3 benar." | 0,5 (hanya penilaian baris 3) |
| Cukup | "1 salah, nyeri itu angka berurutan. 2 pakai RobustScaler karena pencilan. 3 tepat." | 2,5 (baris 1 0,75 — akibat pada dimensi dan perbaikan tidak ada · baris 2 1,25 — akibat hanya disinggung · baris 3 0,5 — tanpa alasan) |
| Baik | "1 tidak tepat: nyeri 0–10 berurutan; *one-hot* membuang urutan dan menambah 11 kolom, sehingga jarak k-NN kurang bermakna; perlakukan sebagai numerik lalu skala. 2 kurang tepat: pencilan menarik rerata dan simpangan baku, mayoritas pasien termampatkan sehingga tidak terbedakan; log(x+1) lalu skala, atau `RobustScaler`. 3 tepat: nominal dengan sedikit kategori; `handle_unknown` mencegah prediksi gagal pada cara bayar baru." | 5 |

**Rujukan:** [Bab 3](../06-buku-ajar/bab-03-data-dan-prapemrosesan.md) §3.4 (penyandian kategori, termasuk §3.4.3 `handle_unknown`) dan §3.5.2 (tiga penskala).

---

### A5. Merekayasa Fitur Waktu Antar — `DAIML-Sub-CPMK102-1` · C4 · 5 poin

| No | Keputusan | Alasan dan bentuk perubahan |
|----|-----------|-----------------------------|
| 1 `jarak_km`, `hujan` | **Ubah** (tambah) | Regresi linear tanpa interaksi menganggap efek hujan sama untuk semua jarak → tambah `jarak_km × hujan` dan pertahankan kedua fitur asal (Bab 5 §5.2.2) |
| 2 `lama_masak_aktual_menit` | **Buang** | Belum tersedia saat kurir menerima tugas → kebocoran temporal (informasi masa depan). Alternatif sah: ganti dengan rata-rata lama masak restoran itu pada 30 hari sebelumnya |
| 3 `kecepatan_rata_kurir_30hari` | **Pertahankan** | Informatif (kebiasaan kurir) dan **tersedia saat prediksi** karena dihitung dari 30 hari sebelum pesanan ini; pastikan perhitungan yang sama (hanya pengantaran sebelum waktu prediksi) dipakai pada data latih; kurir baru tanpa riwayat → imputasi + penanda (nilai tambah) |

**Pedoman skor**

- **Fitur 1 (1,75):** keputusan "ubah" 0,5 · alasan (efek hujan bergantung jarak; model linear tanpa interaksi tidak menangkapnya) 0,5 · bentuk (suku interaksi, fitur asal dipertahankan) 0,75.
- **Fitur 2 (1,75):** keputusan "buang" 0,5 · alasan 1,25: nilainya belum tersedia saat kurir menerima tugas (diisi ketika makanan siap), sehingga memakainya berarti memakai informasi masa depan. Nama jenis tidak diminta; "kebocoran temporal" maupun "kebocoran target" (lama masak adalah bagian dari waktu antar yang diprediksi) diterima bila disertai alasan ketersediaan saat prediksi. "Bocor"/"kebocoran" tanpa mekanisme = 0,25 pada alasan. "Ubah: ganti dengan rata-rata lama masak restoran pada 30 hari sebelumnya" dinilai penuh bila alasannya sama.
- **Fitur 3 (1,5):** keputusan "pertahankan" 0,5 · alasan informatif 0,25 · ketersediaan saat prediksi 0,75. Jendela "30 hari sebelum pesanan ini" sudah ditetapkan pada soal; tidak menyebut syarat waktu secara terpisah tidak dikurangi bila ketersediaan saat prediksi sudah disinggung.

**Contoh jawaban**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "Semua dipertahankan karena makin banyak fitur makin bagus." | 0 (keputusan menyeluruh tanpa menimbang tiap fitur; alasan keliru) |
| Cukup | "1 ubah, tambah fitur jarak × hujan. 2 buang karena bocor. 3 tetap karena informatif." | 2,75 (fitur 1 1,25 — tanpa alasan · fitur 2 0,75 — keputusan 0,5 + "bocor" tanpa mekanisme 0,25; tidak disebut bahwa nilainya belum ada saat kurir menerima tugas · fitur 3 0,75 — ketersediaan saat prediksi tidak disinggung) |
| Baik | "1 ubah: model linear tanpa interaksi menganggap efek hujan sama untuk semua jarak; tambah `jarak_km` × `hujan` dan pertahankan kedua fitur asal. 2 buang: nilainya belum ada saat kurir menerima tugas (informasi masa depan). 3 pertahankan: informatif dan tersedia saat prediksi karena dihitung dari 30 hari sebelum pesanan." | 5 |

**Rujukan:** [Bab 5](../06-buku-ajar/bab-05-rekayasa-fitur.md) §5.2.2 (fitur rasio dan interaksi), §5.2.3 (fitur agregat dan bahayanya); [Bab 4](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md) §4.5.2 (kebocoran temporal).

---

### A6. Mendiagnosis dari Tabel α — `DAIML-Sub-CPMK082-1` · C4 · 5 poin

**(a)** α = 0,001: ***overfit*** (varians tinggi) — RMSE latih 21 rendah, validasi 69 jauh lebih tinggi (selisih 48). α = 100.000: ***underfit*** (bias tinggi) — latih 97 dan validasi 99 sama-sama tinggi dan berdekatan. *(2,5 poin: tiap ujung diagnosis 0,5 + bukti angka 0,75)*

**(b)** Pilih **α = 10**: RMSE validasi terendah (34) dengan selisih latih–validasi kecil (30 vs 34). RMSE latih selalu mengecil ketika α mengecil karena model makin bebas menyesuaikan diri dengan data latih; memilih berdasarkan RMSE latih akan selalu jatuh pada α terkecil, yaitu model yang *overfit*. Pemilihan harus memakai data yang tidak dipakai melatih (validasi silang). Nilai tambah: *grid* lebih rapat di sekitar 10 (mis. 1–100). *(2,5 poin: pilihan dengan alasan validasi terendah 1,0 · selisih latih–validasi kecil 0,25 · mengapa bukan RMSE latih 1,25)*

**Contoh jawaban**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "(a) α kecil bagus karena RMSE latih paling kecil; α besar jelek. (b) α = 0,001." | 0 |
| Cukup | "(a) 0,001 *overfit*, 100.000 *underfit*. (b) α = 10 karena validasi terkecil." | 2,0 (a 1,0 — tanpa bukti · b 1,0 — tanpa alasan "bukan latih") |
| Baik | "(a) α = 0,001 *overfit*: RMSE latih 21 jauh di bawah validasi 69. α = 100.000 *underfit*: latih 97 dan validasi 99 sama-sama tinggi dan berdekatan. (b) α = 10: RMSE validasi terendah (34) dan selisih latih–validasi kecil. RMSE latih selalu turun ketika α mengecil, sehingga selalu memilih α terkecil yang *overfit*; pilih dengan data validasi." | 5 |

**Rujukan:** [Bab 6](../06-buku-ajar/bab-06-regresi-dan-metriknya.md) §6.3.3 (pengaruh α), §6.5.2 (mengenali kondisi model).

---

## 2. Bagian B — Analisis Kasus (40 poin)

### B1. Kebocoran pada Model Pasien Prolanis — `DAIML-Sub-CPMK102-1` · C4 (a, b) dan C3 (c) · 10 poin

**(a) Tiga kebocoran** — `DAIML-Sub-CPMK102-1` · C4 · 3 poin *(per kebocoran: baris 0,5 + jenis 0,5)*

| No | Baris | Jenis | Ringkas |
|----|-------|-------|---------|
| 1 | 2 | **Kebocoran prapemrosesan** | Median imputasi dihitung dari seluruh data, termasuk baris uji, sebelum pembagian |
| 2 | 5–6 | **Kebocoran kelompok** | Pembagian acak per baris; kunjungan pasien yang sama tersebar di latih dan uji |
| 3 | 9–15 (inti: 13–15) | **Kebocoran melalui pemilihan berulang** | `k` dipilih berdasarkan F1 data uji, lalu F1 itu dilaporkan sebagai kinerja |

Penamaan sebagian: baris 5–6 yang dinamai **"kebocoran duplikat"** = baris 0,5 · jenis **0,25**. Bab 4 §4.5.3 mendefinisikan duplikat sebagai baris yang sama atau nyaris sama di latih dan uji; di sini yang tersebar adalah satu **entitas** (pasien) dengan kunjungan berbeda, yaitu kebocoran kelompok (§4.5.4).

Nama jenis boleh diganti uraian mekanisme yang tepat dan menunjuk satu jenis, mis. "baris 13 memilih `k` dengan F1 data uji" (= pemilihan berulang) atau "baris 5 acak padahal satu pasien punya banyak baris" (= kelompok): jenis 0,5. Menyebut operasinya saja tanpa alasan kebocorannya, mis. "baris 2 `fillna`", bukan nama jenis: jenis 0.

Tidak diberi poin: "`StandardScaler` bocor" — penskala sudah di dalam `Pipeline` dan di-*fit* hanya pada `X_tr` (pengecoh). Soal meminta persoalan pembagian temporal diabaikan, sehingga "kebocoran temporal" tidak menggantikan salah satu dari tiga di atas; bila ditulis sebagai tambahan, tidak dikurangi.

**(b) Arah skor, kebocoran terbesar, dan mekanismenya** — `DAIML-Sub-CPMK102-1` · C4 · 4 poin

- **Arah** *(0,5)*: F1 yang dicetak **lebih tinggi** (terlalu optimistis) daripada kinerja pada pasien baru.
- **Kebocoran terbesar** *(1,5)*: **kebocoran kelompok**. Rata-rata enam baris per pasien dan ciri yang tetap per pasien (jenis kelamin, tinggi badan, usia saat terdaftar) membuat k-NN — yang berbasis jarak — dapat menemukan kunjungan lain pasien yang sama di antara tetangganya (Bab 4 §4.3.2: makin banyak baris per entitas, makin besar kebocorannya); ciri yang tetap per pasien memperkuatnya karena pada k-NN kunjungan lain pasien yang sama berjarak dekat. Penuh bila alasannya memakai sekurang-kurangnya satu ciri khas data ini — banyak baris per pasien, ciri tetap per pasien, atau k-NN berbasis jarak yang menemukan kunjungan lain pasien yang sama; memilih kebocoran kelompok tanpa alasan khas data ini = 0,75. Imputasi median hanya membocorkan satu angka statistik (kecil); pemilihan dari enam nilai `k` menambah optimisme kecil–sedang.
- **Mekanisme** *(2,0 = alur informasi 1,0 · akibat 1,0)*: rata-rata ±4 dari 5 kunjungan lain pasien yang sama berada di data latih (pembagian acak 80/20 per baris). Saat memprediksi satu kunjungan uji, sebagian tetangga yang ditemukan k-NN adalah kunjungan lain **pasien itu sendiri**, sehingga label pasien itu ikut terbawa ke prediksi. Sebagian keberhasilan model berasal dari mengenali pasien, bukan dari pola yang berlaku umum; pada pasien baru tetangga semacam itu tidak ada, sehingga F1 uji melebih-lebihkan kinerja saat penerapan.

Perlakuan pilihan lain: memilih **pemilihan berulang** sebagai yang terbesar dengan alasan masuk akal (banyak kandidat, data uji dipakai berkali-kali) → poin kebocoran terbesar paling banyak 0,75, karena struktur data per pasien (±6 kunjungan, ciri tetap) diabaikan; memilih **imputasi** → 0,25. Mekanisme selalu dinilai menurut kebocoran yang dipilih mahasiswa, asalkan kebocoran itu benar ada pada kode:

- *Pemilihan berulang:* enam model dibandingkan pada data uji dan yang terbaik dipilih; F1 tertinggi dari enam percobaan memuat keberuntungan pada data uji tertentu, dan data uji ikut membentuk keputusan, sehingga skornya bukan lagi taksiran kinerja pada data baru.
- *Prapemrosesan:* median `gula_puasa` dihitung dari seluruh 9.600 baris, termasuk ±20% baris yang kemudian menjadi data uji; nilai pengisi pada baris latih memuat informasi sebaran data uji. Dampaknya kecil karena yang bocor hanya satu statistik, tetapi prinsipnya sama dengan penskala yang di-*fit* sebelum pembagian.

**(c) Alur yang benar** — `DAIML-Sub-CPMK102-1` · C3 · 3 poin

Soal meminta **langkah bernomor atau pseudokode**; kode tidak wajib. Contoh jawaban:

1. Bagi data **per pasien** (`id_pasien`): 80% pasien untuk latih, 20% pasien untuk uji; seluruh kunjungan satu pasien berada di satu sisi.
2. Susun `Pipeline`: imputasi median → penskalaan → k-NN, sehingga median dan penskala di-*fit* pada data latih saja.
3. Pilih `k` dengan validasi silang **berkelompok per pasien** pada data latih (mis. `GroupKFold` 5 lipatan), menilai setiap `k` dengan F1 rerata lipatan.
4. Latih ulang `Pipeline` dengan `k` terpilih pada seluruh data latih, lalu hitung F1 pada data uji **satu kali** dan laporkan angka itu.

Kode rujukan (bukan tuntutan jawaban; `df` seperti pada soal — berkas CSV soal tidak tersedia, jadi untuk mencoba di Colab buat lebih dahulu `df` sintetis dengan kolom yang sama):

```python
import pandas as pd
from sklearn.model_selection import GroupShuffleSplit, GroupKFold, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score

X = df.drop(columns=["id_pasien", "tidak_terkontrol"])
y = df["tidak_terkontrol"]
grup = df["id_pasien"]

# 1) Pembagian BERKELOMPOK: seluruh kunjungan satu pasien berada di satu sisi
gss = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
i_latih, i_uji = next(gss.split(X, y, groups=grup))
X_tr, X_te = X.iloc[i_latih], X.iloc[i_uji]
y_tr, y_te = y.iloc[i_latih], y.iloc[i_uji]

# 2) Seluruh prapemrosesan di dalam Pipeline (median imputasi di-fit pada latih saja)
pipa = Pipeline([
    ("imputasi", SimpleImputer(strategy="median")),
    ("skala", StandardScaler()),
    ("knn", KNeighborsClassifier()),
])

# 3) Pilih k dengan validasi silang BERKELOMPOK pada data latih saja
cari = GridSearchCV(pipa, {"knn__n_neighbors": [3, 5, 7, 9, 11, 15]},
                    cv=GroupKFold(n_splits=5), scoring="f1")
cari.fit(X_tr, y_tr, groups=grup.iloc[i_latih])

# 4) Data uji dipakai SEKALI, setelah semua keputusan selesai
print("k terpilih:", cari.best_params_["knn__n_neighbors"])
print("F1 uji:", round(f1_score(y_te, cari.predict(X_te)), 3))
```

| Unsur | Poin |
|-------|------|
| Pembagian berkelompok per `id_pasien` (`GroupShuffleSplit`, `GroupKFold`, atau pembagian manual daftar pasien) untuk memisahkan data uji — hanya CV berkelompok, sedangkan data uji tidak dipisah per pasien = 0,5 | 1 |
| Imputasi di dalam `Pipeline` atau di-*fit* pada data latih saja (cukup disebut) | 0,5 |
| Pemilihan `k` dengan validasi silang pada data latih (0,5 bila CV tidak berkelompok) | 1 |
| Data uji dipakai satu kali di akhir | 0,5 |

Alternatif sah: pembagian tiga bagian latih/validasi/uji **per pasien** dengan `k` dipilih pada validasi. Unsur (c) dinilai terhadap ketiga kebocoran pada kode (kunci (a)), bukan terhadap jawaban (a) mahasiswa: perbaikan yang benar tetap diberi poin walaupun kebocorannya tidak disebut di (a). Sebaliknya, soal (c) meminta **seluruh** kebocoran pada kode hilang dan F1 menjadi taksiran jujur pada **pasien baru**, sehingga pembagian berkelompok tetap dituntut walaupun kebocoran kelompok terlewat di (a); kaidah kesalahan terbawa (§0) tidak berlaku karena (c) tidak bertumpu pada hasil (a).

**Contoh jawaban B1 (keseluruhan)**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "(a) Baris 10 scaler bocor, baris 2 fillna. (b) Lebih tinggi; data uji masuk ke latih. (c) Pakai Pipeline." | 1,0 (a 0,5 — baris 2 tanpa nama jenis · b 0,5 — arah saja · c 0 — imputasi tidak disebut, padahal kode soal sudah memakai `Pipeline` untuk penskala) |
| Cukup | "(a) Baris 2 prapemrosesan; baris 5 acak padahal satu pasien banyak baris (kelompok); baris 13 memilih k pakai data uji. (b) Lebih tinggi. Terbesar kelompok: pasien yang sama ada di latih dan uji sehingga model hafal. (c) 1. Pipeline dengan imputer, scaler, kNN. 2. GridSearchCV dengan GroupKFold untuk memilih k. 3. Uji di data uji." | 8,0 (a 3 · b 2,5 — pilihan tanpa alasan khas data 0,75, alur 0,75, akibat 0,5 · c 2,5 — data uji tidak dipisah per pasien: 0,5 dari 1) |
| Baik | "(a) Baris 2: kebocoran prapemrosesan. Baris 5–6: kebocoran kelompok. Baris 13–15: kebocoran melalui pemilihan berulang. (b) Lebih tinggi. Terbesar: kelompok, karena ±6 kunjungan per pasien dan ciri tetap membuat k-NN menemukan kunjungan lain pasien itu. Mekanisme: kunjungan lain pasien uji ada di data latih dan labelnya terbawa ke prediksi; model mengenali pasien, bukan pola, padahal pada pasien baru tetangga semacam itu tidak ada. (c) 1. Bagi per pasien: 80% pasien latih, 20% uji. 2. `Pipeline` imputasi median → skala → k-NN, di-*fit* pada latih. 3. Pilih `k` dengan CV berkelompok per pasien pada data latih. 4. Latih ulang dengan `k` terpilih; hitung F1 uji sekali." | 10 |

**Rujukan:** [Bab 4](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md) §4.3.2 (pembagian berkelompok), §4.5 (enam jenis kebocoran); [Bab 3](../06-buku-ajar/bab-03-data-dan-prapemrosesan.md) §3.6 (`Pipeline`).

---

### B2. Patroli Kebakaran Lahan Gambut — `DAIML-Sub-CPMK082-1` (a, d) dan `DAIML-Sub-CPMK102-1` (b, c) · C6 (a), C4 (b, c), dan C5 (d) · 10 poin

**(a) Target dan jenis *task*** — `DAIML-Sub-CPMK082-1` · C6 · 2 poin

Contoh: *"Sel bernilai 1 bila **terjadi kebakaran** (titik api terverifikasi regu atau tercatat sebagai areal terbakar) **seluas ≥ 0,5 ha** **dalam 7 hari** **sejak Senin pukul 07.00** saat patroli ditetapkan; selain itu 0."* Jenis *task*: **klasifikasi biner** yang keluaran probabilitasnya dipakai untuk **mengurutkan** sel (memilih 40 teratas).

| Unsur | Poin |
|-------|------|
| Peristiwa + ambang (luas/verifikasi); peristiwa tanpa ambang ("sel terbakar") = 0,25 | 0,5 |
| Jendela waktu (7 hari / satu minggu patroli) | 0,5 |
| Titik awal selaras keputusan (Senin 07.00) | 0,5 |
| Jenis *task* (klasifikasi biner untuk pemeringkatan; "*ranking*" saja juga benar) | 0,5 |

Ambang lain (≥ 1 titik api terverifikasi, ≥ 1 ha) diterima selama dinyatakan eksplisit.

**(b) Batas *recall*** — `DAIML-Sub-CPMK102-1` · C4 · 2 poin

$$\text{Kejadian} = 2.000 \times 3\% = 60 \text{ sel} \qquad \text{Recall maks} = \frac{40}{60} = 0{,}667$$

Artinya: dengan kapasitas 40 sel, sepertiga kejadian **pasti** tidak terpatroli walaupun model sempurna. Target kinerja harus dinyatakan relatif terhadap kapasitas (berapa dari 40 sel yang tepat, atau *recall* dibanding batas 0,667), bukan "*recall* ≥ 0,8". Bila cakupan lebih tinggi dibutuhkan, yang harus ditambah adalah kapasitas patroli, bukan modelnya. *(60 sel 0,5 · 0,667 0,5 · arti 1)*

**(c) Mengapa akurasi tidak menjawab; ambang dan metrik yang sesuai** — `DAIML-Sub-CPMK102-1` · C4 · 3 poin

- Akurasi 0,97 **sama dengan** akurasi model yang selalu menjawab "tidak terbakar" (1 − 0,03 = 0,97) → tidak memberi informasi apa pun *(1)*. "Menyesatkan karena data tidak seimbang" tanpa kaitan dengan angka 0,97 = 0,5.
- Ambang ditentukan **oleh kapasitas**, bukan ambang baku 0,5: urutkan sel menurut probabilitas tiap minggu dan ambil 40 teratas (ambang = probabilitas sel ke-40) *(1)*.
- Metrik: ***precision* pada 40 teratas** (berapa dari 40 sel yang benar terbakar) dan ***recall* pada 40 teratas** (dibandingkan batas 0,667), dirata-ratakan per minggu pada periode uji yang lebih akhir *(1)*. PR-AUC saja tanpa evaluasi 40 teratas = 0,25; F1 atau metrik lain pada ambang baku tanpa evaluasi 40 teratas = 0.

**(d) *Baseline* dan argumentasinya** — `DAIML-Sub-CPMK082-1` · C5 · 3 poin

- *Baseline* bermakna *(1)*: **cara penetapan yang berlaku saat ini** — 40 sel yang selama ini dipilih kepala balai, bila pilihannya tercatat (Bab 2 §2.4.1) — atau aturan sederhana yang dapat dihitung Senin pagi, mis. 40 sel dengan titik panas terbanyak minggu lalu, atau 40 sel dengan hari tanpa hujan terpanjang dan muka air terendah. Keduanya dinilai penuh.
- Argumentasi *(2 = dua alasan dari tiga berikut, masing-masing 1)*: (i) pembanding itu adalah cara yang **akan digantikan** model (atau yang dapat dijalankan balai tanpa model) dan hanya memakai informasi yang tersedia pada saat keputusan; (ii) *baseline* kelas terbanyak tidak memilih sel apa pun sehingga tidak bermakna untuk keputusan ini; (iii) model hanya layak dipakai bila mengungguli pembanding itu pada **metrik 40 teratas yang sama** dan periode uji yang sama. Satu alasan saja = 1.

Nilai tambah (tidak wajib): satu ukuran dampak di samping metrik teknis, mis. luas lahan terbakar atau waktu respons sejak titik api muncul (Bab 2 §2.3.3).

**Contoh jawaban B2 (keseluruhan)**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "(a) Target: sel terbakar atau tidak. (b) 60 sel. (c) Pakai F1 karena tidak seimbang. (d) *Baseline* kelas terbanyak." | 0,75 (a 0,25 — peristiwa tanpa ambang; jendela waktu, titik awal, dan jenis *task* tidak ada · b 0,5 — 60 sel saja · c 0 — tidak menjelaskan mengapa akurasi 0,97 gagal, dan F1 pada ambang baku bukan evaluasi 40 teratas · d 0 — kelas terbanyak tidak memilih sel apa pun) |
| Cukup | "(a) Kebakaran ≥ 1 titik api dalam 7 hari sejak Senin; klasifikasi biner. (b) 60, recall maks 0,667. (c) Akurasi menyesatkan karena tidak seimbang; pakai PR-AUC. (d) *Baseline*: titik panas minggu lalu." | 4,75 (a 2 · b 1 — arti tidak ada · c 0,75 — akurasi tidak dikaitkan dengan 0,97, tanpa ambang dari kapasitas · d 1 — tanpa argumentasi) |
| Baik | "(a) 1 bila sel terbakar (titik api terverifikasi, ≥ 0,5 ha) dalam 7 hari sejak Senin 07.00; selain itu 0. Klasifikasi biner untuk memeringkat sel. (b) Kejadian 2.000 × 3% = 60 sel; *recall* maks 40/60 = 0,667. Sepertiga kebakaran pasti tak terpatroli walau model sempurna, jadi target kinerja harus relatif terhadap kapasitas. (c) Akurasi 0,97 = akurasi model yang selalu menjawab 'tidak terbakar' (1 − 0,03), jadi tidak informatif. Ambang dari kapasitas: urutkan probabilitas, ambil 40 teratas. Metrik: *precision* dan *recall* 40 teratas per minggu. (d) *Baseline*: 40 sel dengan titik panas terbanyak minggu lalu. Alasan: dapat dijalankan Senin pagi tanpa model; *baseline* kelas terbanyak tidak memilih sel apa pun; model dipakai hanya bila unggul pada metrik 40 teratas yang sama." | 10 |

**Rujukan:** [Bab 2](../06-buku-ajar/bab-02-formulasi-masalah-daur-hidup-ml.md) §2.1–§2.4 (unsur target, metrik dan ukuran dampak, *baseline*); [Bab 7](../06-buku-ajar/bab-07-klasifikasi-dan-metriknya.md) §7.3.2 (akurasi menyesatkan), §7.4 (ambang keputusan).

---

### B3. Model Harga Sewa Kos — `DAIML-Sub-CPMK102-1` · C4 (a, b) dan C3 (c, d) · 10 poin

**(a) Baris 3–5** — `DAIML-Sub-CPMK102-1` · C4 · 3 poin *(per baris: masalah 0,5 + nama jenis 0,5)*

| Baris | Masalah | Jenis kekeliruan |
|-------|---------|------------------|
| 3 | Rata-rata harga per kecamatan dihitung dari **seluruh data**, termasuk harga baris uji dan harga baris itu sendiri | Diterima penuh: **kebocoran target** (fitur memuat target baris itu sendiri — "turunan dari target", Bab 4 §4.5.5), **kebocoran prapemrosesan** (agregat di-*fit* pada seluruh data sebelum pembagian), atau ***target encoding* yang bocor** |
| 4 | `harga_per_m2` dihitung **dari target**; harga = `harga_per_m2 × luas`, jadi model "mengetahui" jawabannya. Untuk iklan baru harga belum ada, sehingga fitur ini tidak dapat dihitung | **Kebocoran target** (diterima juga: kebocoran temporal — nilainya belum ada saat iklan baru dipasang) |
| 5 | `cat.codes` pada data **nominal** menghasilkan urutan abjad campur = 0, putra = 1, putri = 2; regresi linear menganggap urutan dan jarak itu bermakna | Penyandian keliru: nominal diberi nomor → pakai *one-hot* |

**(b) Pola nilai hilang dan akibat baris 6** — `DAIML-Sub-CPMK102-1` · C4 · 3 poin

- Pola: **MAR** — hilangnya luas bergantung pada `jenis_pengiklan` yang teramati *(0,5)*.
- Masalah baris 6: `dropna()` membuang ±30% baris yang hilangnya **tidak acak**, tanpa analisis pola → sampel latih tidak lagi mewakili populasi iklan (sampel bias) *(0,75)*.
- Akibat: banyak iklan perorangan (yang lebih murah) terbuang, sehingga porsi iklan agen di data latih membesar → saran harga untuk iklan perorangan cenderung **terlalu tinggi**, dan iklan baru tanpa luas tidak dapat diberi saran *(0,75)*.
- Penanganan: jangan hapus baris; imputasi bersyarat (median luas per `jenis_pengiklan`) **di dalam `Pipeline`** dengan penanda hilang (`add_indicator=True`); masukkan `jenis_pengiklan` sebagai fitur; catat sebagai keterbatasan *(1)*.

Alternatif: argumen **MNAR** ("pemilik kamar sempit enggan menulis luas") dinilai penuh bila konsisten — penanganannya penanda hilang dan pernyataan keterbatasan, karena MNAR tidak dapat diperbaiki secara statistik.

**(c) Fitur `bulan`** — `DAIML-Sub-CPMK102-1` · C3 · 2 poin

Regresi linear memberi **satu koefisien** untuk `bulan`, sehingga harga dianggap berubah lurus dari Januari ke Desember; model tidak dapat naik pada Juli–Agustus lalu turun lagi, dan Desember (12) dianggap paling jauh dari Januari (1) *(1)*. Bentuk yang tepat: fitur biner `musim_ajaran_baru` (Juli–Agustus = 1) — paling langsung; atau *one-hot* bulan. Penyandian siklik sin/cos: dengan menyebut keterbatasannya (satu gelombang halus kurang tepat untuk puncak sempit dua bulan) = 1; tanpa menyebutnya = 0,5 *(1)*.

**(d) Harga khas kecamatan** — `DAIML-Sub-CPMK102-1` · C3 · 2 poin

Soal tidak menyebut "tanpa kebocoran"; mahasiswa harus sendiri menghindari kebocoran yang ditemukan pada baris 3. Dasar seluruh jawaban: fitur dihitung dari **data latih saja**, setelah pembagian — idealnya di dalam `Pipeline` sehingga pada validasi silang dihitung ulang tiap lipatan latih — lalu diterapkan ke data uji dan iklan baru tanpa memakai harganya.

| Keadaan | Cara | Alasan |
|---------|------|--------|
| (i) Baris data latih | ***Cross-fitting***: bagi data latih menjadi mis. 5 lipatan; nilai fitur tiap baris dihitung dari lipatan **lain**. Diterima juga *leave-one-out* (rerata kecamatan tanpa baris itu sendiri), atau `TargetEncoder` — yang melakukan *cross-fitting* pada `fit_transform` | Bila rerata kecamatan memuat harga baris itu sendiri, fitur ikut "mengetahui" targetnya; makin sedikit iklan di kecamatan itu, makin besar porsinya (kecamatan dengan satu iklan: fitur = harganya sendiri). Model lalu terlalu mengandalkan fitur ini, padahal untuk iklan baru nilainya tidak memuat harga iklan itu |
| (ii) Kecamatan dengan sedikit iklan | Penghalusan: rerata kecamatan ditarik ke rerata seluruh data latih, $\frac{n_k\,\bar{y}_k + m\,\bar{y}}{n_k + m}$ ($n_k$ = jumlah iklan kecamatan itu, $m$ = bobot); atau gabungkan kecamatan kecil ke "LAINNYA" atau ke tingkat kota/kabupaten (Bab 3 §3.4.2); atau ambang minimum jumlah iklan | Rerata dari 1–3 iklan sangat bergantung pada iklan-iklan itu (variansnya besar), sehingga tidak dapat dipercaya sebagai "harga khas" |

| Unsur | Poin |
|-------|------|
| Dihitung dari data latih saja, lalu diterapkan ke data uji/iklan baru tanpa harga uji | 0,5 |
| (i) Nilai untuk baris latih tidak memakai harga baris itu sendiri, dengan alasan | 0,75 |
| (ii) Penghalusan, penggabungan kecamatan kecil, atau ambang minimum — dengan alasan (tanpa alasan = 0,5) | 0,75 |

Istilah *cross-fitting* dan *smoothing* tidak wajib; yang dinilai caranya. "`TargetEncoder` di dalam `Pipeline`" tanpa menjelaskan kedua keadaan = 1,25 (unsur pertama + (i)); penuh bila perilaku penghalusannya pada (ii) disebut. Untuk (i), "hitung dari data latih" tanpa mengecualikan baris itu sendiri = 0 pada unsur (i). "Rata-rata per kecamatan dari seluruh data" = 0. Nilai tambah: kecamatan yang belum ada di data latih diisi rerata global data latih, sehingga iklan baru tidak gagal diberi saran harga.

Kode rujukan (bukan tuntutan jawaban; `df`, `X`, `y` seperti pada soal, tetapi `X` **tanpa** `harga_rata_kecamatan` dan `harga_per_m2` — berkas CSV soal tidak tersedia, jadi untuk mencoba di Colab buat lebih dahulu `df` sintetis dengan kolom yang sama):

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, train_test_split

# Kolom kecamatan tidak ada di X, sehingga diambil dari df lewat indeks baris
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=1)
kec_tr = df.loc[X_tr.index, "kecamatan"]
kec_te = df.loc[X_te.index, "kecamatan"]
M = 20                       # bobot penghalusan: 20 "iklan semu" bernilai rerata global

def harga_khas(kec_fit, y_fit, kec_terap):
    """Rerata harga per kecamatan dari data fit, dihaluskan ke rerata global."""
    rerata_global = y_fit.mean()
    stat = y_fit.groupby(kec_fit).agg(["mean", "count"])
    halus = (stat["count"] * stat["mean"] + M * rerata_global) / (stat["count"] + M)  # (ii)
    return kec_terap.map(halus).fillna(rerata_global)      # kecamatan baru -> rerata global

# (i) baris latih: cross-fitting — nilai tiap baris dihitung dari lipatan LAIN
fitur_tr = pd.Series(np.nan, index=X_tr.index)
for i_a, i_b in KFold(n_splits=5, shuffle=True, random_state=1).split(X_tr):
    fitur_tr.iloc[i_b] = harga_khas(kec_tr.iloc[i_a], y_tr.iloc[i_a],
                                    kec_tr.iloc[i_b]).to_numpy()
# data uji / iklan baru: dari SELURUH data latih, tanpa harga uji
fitur_te = harga_khas(kec_tr, y_tr, kec_te)
X_tr = X_tr.assign(harga_khas_kec=fitur_tr)
X_te = X_te.assign(harga_khas_kec=fitur_te)
# Alternatif ringkas: pertahankan kolom kecamatan di X, lalu pakai TargetEncoder
# (scikit-learn >= 1.3) di dalam ColumnTransformer: cross-fitting pada fit_transform,
# penghalusan smooth="auto", kategori baru -> rerata target.
```

**Contoh jawaban B3 (keseluruhan)**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "(a) Baris 3 benar. Baris 4 fitur bagus. Baris 5 benar. (b) MCAR; dropna membersihkan data. (c) Normalisasi bulan. (d) Pakai rata-rata seluruh data." | 0 |
| Cukup | "(a) 3 bocor karena pakai seluruh data; 4 bocor karena dari harga; 5 harus one-hot. (b) MAR karena tergantung pengiklan; dropna menghapus banyak data; harus diimputasi. (c) Pakai sin/cos. (d) Hitung dari data latih setelah split; kecamatan yang sedikit iklannya digabung jadi 'lainnya'." | 5,25 (a 2,5 — baris 5 tanpa nama jenis/alasan urutan · b 1,25 — pola 0,5; masalah baris 6 0,25 karena tanpa "tidak acak"; akibat pada saran harga 0; penanganan 0,5 karena tanpa imputasi bersyarat/penanda · c 0,5 — alasan tidak ada; sin/cos tanpa menyebut keterbatasannya 0,5 · d 1,0 — baris latih tidak ditangani; penggabungan tanpa alasan 0,5) |
| Baik | "(a) 3: rata-rata kecamatan dari seluruh data, memuat harga baris itu sendiri — kebocoran target. 4: `harga_per_m2` dihitung dari target — kebocoran target. 5: nominal diberi nomor 0/1/2, regresi menganggap ada urutan — penyandian keliru (pakai *one-hot*). (b) MAR: hilangnya bergantung pada `jenis_pengiklan`. `dropna` membuang 30% baris yang hilangnya tidak acak, sampel bias; iklan perorangan yang murah banyak terbuang, sehingga saran harga perorangan terlalu tinggi. Imputasi median luas per `jenis_pengiklan` di `Pipeline` dengan penanda hilang. (c) Satu koefisien: harga berubah lurus dari bulan 1 ke 12, tak bisa naik pada Juli–Agustus lalu turun. Pakai fitur biner `musim_ajaran_baru` (Juli–Agustus = 1). (d) Hitung dari data latih saja, juga untuk data uji. (i) Baris latih: *cross-fitting* 5 lipatan — nilai tiap baris dari lipatan lain agar tidak memuat harganya sendiri. (ii) Kecamatan sedikit iklan: haluskan ke rerata global karena rerata 1–3 iklan tidak stabil." | 10 |

**Rujukan:** [Bab 3](../06-buku-ajar/bab-03-data-dan-prapemrosesan.md) §3.3 (nilai hilang), §3.4.2 (kardinalitas tinggi); [Bab 5](../06-buku-ajar/bab-05-rekayasa-fitur.md) §5.2.1 (fitur waktu), §5.2.3 (fitur agregat dan bahayanya); [Lab 03](../04-labs/lab-03-pipeline-prapemrosesan.md) Langkah 6.

---

### B4. "Sistem AI" Penetapan Penerima Bantuan Sosial — `DAIML-Sub-CPMK082-1` (a, c) dan `DAIML-Sub-CPMK102-1` (b, d) · C4 (a, b, d) dan C6 (c) · 10 poin

**(a) Uji kelayakan** — `DAIML-Sub-CPMK082-1` · C4 · 3 poin *(pertanyaan yang tepat 1 · bukti dari skenario 1 · batas kemampuan AI yang dikaitkan 1)*

Pilihan yang paling kuat (cukup memilih **satu**):

| Pertanyaan | Bukti dari skenario | Batas kemampuan AI |
|------------|---------------------|--------------------|
| P3/P6 — kesalahan dapat ditoleransi? konsekuensinya dan siapa yang dirugikan? | Keputusan **final, otomatis, tanpa verifikasi**; rumah tangga miskin yang tertolak tidak punya jalan koreksi (keadaan "kesalahan berakibat berat tanpa pengawasan manusia") | Model selalu memiliki galat; **sulit dijelaskan** kepada warga yang ditolak |
| P2 — data memadai dan bermutu? | Data **2019** dipakai untuk keputusan tahun depan; label dari usulan kepala desa yang terbukti dipengaruhi kedekatan keluarga | **Bergantung mutlak pada data latih** — bias dalam label menjadi bias dalam keputusan; **rapuh di luar distribusi latih** — kondisi rumah tangga telah berubah |
| P5 — pembanding sederhana? (diterima) | Tidak ada pembanding: tidak disebut kinerja proses verifikasi yang berlaku | Yang sah: **bergantung mutlak pada data latih** — tanpa pembanding, "akurasi 90%" terhadap label usulan kepala desa hanya mengukur seberapa baik model meniru label, termasuk biasnya |

Pada P5, batas kemampuan AI yang sah adalah yang tercantum pada tabel; batas lain yang tidak dikaitkan dengan ketiadaan pembanding = 0 pada unsur batas AI (paling banyak **2 dari 3**).

P3 dan P6 sama-sama diterima, masing-masing dengan buktinya — P3: keputusan final tanpa verifikasi dan tanpa jalan koreksi; P6: siapa yang dirugikan, yaitu rumah tangga miskin atau berpenghasilan tidak tetap yang tertolak. Bila mahasiswa menulis lebih dari satu pertanyaan, yang dinilai adalah pertanyaan terbaik; tidak ada poin tambahan.

**(b) Arah pergeseran akibat imputasi median** — `DAIML-Sub-CPMK102-1` · C4 · 2 poin

- Arah *(0,75)*: rumah tangga berpenghasilan tidak tetap diberi penghasilan "khas" yang **lebih tinggi** dari sebenarnya → tampak lebih sejahtera → cenderung dinilai **tidak layak**; kesalahan eksklusi justru menimpa kelompok termiskin.
- Mekanisme *(0,5)*: median dihitung dari rumah tangga yang **dapat** menyebut angkanya, umumnya berpenghasilan tetap dan lebih tinggi; pola hilangnya **MNAR** (bergantung pada penghasilan itu sendiri) atau sekurang-kurangnya terkait pekerjaan, sehingga nilai pengisi tidak mewakili kelompok yang hilang.
- Median per jenis pekerjaan *(0,75)*: **mengurangi** bias bila hilangnya dijelaskan oleh pekerjaan yang teramati (bagian MAR), tetapi **belum menyelesaikan** — di dalam satu jenis pekerjaan pun, yang tidak dapat menyebut angka cenderung berpenghasilan paling rendah atau paling tidak menentu (bagian MNAR). Yang diperlukan: penanda hilang sebagai fitur (`add_indicator=True`), indikator yang lebih andal (aset, kondisi rumah), verifikasi lapangan untuk rumah tangga ini, dan pernyataan keterbatasan. Menilai median per pekerjaan ("lebih baik", "sudah cukup") tanpa alasan = 0,25.

Alternatif: "sudah cukup karena hilangnya dijelaskan oleh pekerjaan (MAR)" diberi **0,5 dari 0,75** pada bagian ketiga bila alasannya konsisten dan disertai penanda hilang atau verifikasi.

**(c) Rancangan ulang** — `DAIML-Sub-CPMK082-1` · C6 · 3 poin *(1 per unsur)*

1. **Peran model:** pendukung keputusan — mengurutkan atau menandai rumah tangga untuk **diprioritaskan dalam verifikasi lapangan**; keputusan akhir oleh petugas berdasarkan verifikasi.
2. **Label:** hasil verifikasi lapangan independen terbaru dengan kriteria tertulis (mis. pengeluaran per kapita di bawah ambang tertentu pada pendataan tahun berjalan), bukan usulan kepala desa.
3. **Pengawasan:** mekanisme sanggah/pengaduan warga; audit berkala tingkat eksklusi per desa dan per kelompok pekerjaan (nelayan, buruh harian); pemutakhiran data berkala.

**(d) Dua jenis kesalahan dan metrik pengganti** — `DAIML-Sub-CPMK102-1` · C4 · 2 poin

- Perbandingan *(1)*: kesalahan **eksklusi** (layak, tidak menerima) merugikan rumah tangga miskin — kebutuhan dasar tak terpenuhi, berat dan sulit dipulihkan, serta menyalahi amanah penyaluran bantuan. Kesalahan **inklusi** (tidak layak, menerima) membuat anggaran bocor dan menimbulkan kecemburuan sosial, tetapi lebih dapat dikoreksi lewat verifikasi dan sanggahan. Menyebut kesalahan yang lebih berat tanpa alasan dampaknya = 0,5.
- Metrik pengganti *(1)*: ***recall* kelas "layak"** (tingkat eksklusi = 1 − *recall*) dengan batas *precision* minimum, diukur terhadap **label verifikasi independen** dan dilaporkan per desa/kelompok. *Recall* tanpa menyebut kelas atau batas *precision* = 0,5.

Nilai tambah: akurasi terhadap label 2023 mengukur **kesamaan dengan keputusan lama yang bias** — model yang meniru favoritisme justru dinilai "akurat".

**Contoh jawaban B4 (keseluruhan)**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "(a) Datanya banyak jadi layak ML. (b) Isi median sudah benar. (c) Pakai model yang lebih akurat seperti Random Forest. (d) Akurasi 90% sudah bagus." | 0 |
| Cukup | "(a) P2: data 2019 sudah lama dan label dari kepala desa bias. (b) Median membuat penghasilan terlalu tinggi sehingga dianggap tidak layak. Median per pekerjaan lebih baik. (c) Model hanya membantu, keputusan tetap manusia. (d) Eksklusi lebih berbahaya; pakai recall." | 5,0 (a 2,0 — pertanyaan dan bukti tepat, batas AI tidak disebut · b 1,0 — arah 0,75 + menilai median per pekerjaan tanpa alasan 0,25 · c 1,0 — label dan pengawasan tidak ada · d 1,0 — perbandingan tanpa alasan 0,5 + *recall* tanpa kelas/batas 0,5) |
| Baik | "(a) P2 (data memadai dan bermutu?): data 2019 dipakai untuk keputusan tahun depan, dan labelnya usulan kepala desa yang terbukti dipengaruhi kedekatan keluarga. Batas AI: bergantung mutlak pada data latih — bias label menjadi bias keputusan. (b) Median dari yang dapat menyebut angka (berpenghasilan tetap, lebih tinggi), jadi rumah tangga berpenghasilan tak tetap tampak lebih sejahtera dan dinilai tidak layak. Median per pekerjaan mengurangi, tetapi belum menyelesaikan: dalam satu pekerjaan pun, yang tak dapat menyebut angka cenderung paling miskin (MNAR). (c) (i) Model memeringkat rumah tangga untuk diprioritaskan dalam verifikasi lapangan; keputusan oleh petugas. (ii) Label: hasil verifikasi lapangan independen terbaru dengan kriteria tertulis. (iii) Sanggahan warga dan audit eksklusi per desa. (d) Eksklusi lebih berat: kebutuhan dasar keluarga miskin tak terpenuhi dan sulit dipulihkan; inklusi hanya membocorkan anggaran dan dapat dikoreksi lewat sanggahan. Metrik: *recall* kelas 'layak' dengan batas *precision* minimum." | 10 |

**Rujukan:** [Bab 1](../06-buku-ajar/bab-01-lanskap-kecerdasan-artifisial.md) §1.4.1 (lima keadaan), §1.4.2 (uji kelayakan enam pertanyaan), §1.5 (batas kemampuan AI); [Bab 2](../06-buku-ajar/bab-02-formulasi-masalah-daur-hidup-ml.md) §2.1 (unsur target); [Bab 3](../06-buku-ajar/bab-03-data-dan-prapemrosesan.md) §3.3.1 dan §3.3.3 (pola nilai hilang dan penanganannya).

---

## 3. Bagian C — Perhitungan (30 poin)

### C1. Dua Model Kunjungan Dokter Hewan — `DAIML-Sub-CPMK102-1` · C3 (a–c) dan C4 (d) · 10 poin

**(a) Metrik Model A** — C3 · 4 poin *(precision 1,25 = langkah 0,5 + hasil 0,75 · recall 1,25 = langkah 0,5 + hasil 0,75 · F1 1,5 = langkah 0,75 + hasil 0,75)*

| Metrik | Model A (TP 48, FN 32, FP 40, TN 880) | Model B (TP 64, FN 16, FP 150, TN 770) — diberikan pada soal |
|--------|---------------------------------------|---------------------------------------------------------------|
| Akurasi (diberikan pada soal) | (48 + 880) / 1.000 = 0,928 | (64 + 770) / 1.000 = 0,834 |
| *Precision* | 48 / (48 + 40) = 48/88 = **0,545** | 64 / (64 + 150) = 64/214 = 0,299 |
| *Recall* | 48 / (48 + 32) = 48/80 = **0,600** | 64 / (64 + 16) = 64/80 = 0,800 |
| F1 | 2 · 0,545 · 0,600 / (0,545 + 0,600) = **0,571** | 2 · 0,299 · 0,800 / (0,299 + 0,800) = 0,435 |

Bentuk setara: F1 = 2TP/(2TP + FP + FN) → A: 96/168 = 0,571; B: 128/294 = 0,435.

**(b)** Kebijakan "tidak ada kunjungan" (= model "selalu sehat"): akurasi = 920/1.000 = **0,920** — C3 · 1 poin *(langkah 0,5 · hasil 0,5)*. Akurasi Model A hanya 0,008 di atas angka ini.

**(c) Total biaya kesalahan** — C3 · 3 poin *(per model 1,5 = biaya FN 0,5 · biaya FP 0,5 · total 0,5)*

| Model | FN × Rp1.200.000 | FP × Rp150.000 | Total |
|-------|------------------|----------------|-------|
| A | 32 × 1,2 jt = Rp38,4 jt | 40 × 0,15 jt = Rp6,0 jt | **Rp44,4 juta** |
| B | 16 × 1,2 jt = Rp19,2 jt | 150 × 0,15 jt = Rp22,5 jt | **Rp41,7 juta** |

Tafsir alternatif yang diterima penuh: biaya kunjungan dikenakan pada **semua** peternak yang dikunjungi (TP + FP): A = 88 × 0,15 + 38,4 = Rp51,6 juta; B = 214 × 0,15 + 19,2 = Rp51,3 juta. B tetap sedikit lebih murah. Sebagai pembanding: kebijakan "tidak ada kunjungan" berbiaya 80 × 1,2 = Rp96 juta walaupun akurasinya 0,920.

**(d) Pilihan dan alasannya** — C4 · 2 poin

- Berdasarkan biaya, **Model B** lebih murah (Rp41,7 vs Rp44,4 juta) walaupun akurasi dan F1-nya lebih rendah *(0,75)*.
- Mengapa berlawanan *(1,25)*: akurasi dan F1 memperlakukan FN dan FP **setara** (F1 = 2TP/(2TP + FP + FN)) *(0,5)*, sedangkan biaya satu FN delapan kali biaya satu FP, sehingga selisih jumlah FN lebih menentukan biaya *(0,75)*. Rinciannya — B menukar 110 FP tambahan (Rp16,5 juta) dengan 16 FN lebih sedikit (Rp19,2 juta), dan akurasi didominasi kelas mayoritas — adalah nilai tambah.

Nilai tambah: sebelum memilih B, koperasi perlu memastikan **kapasitas dokter hewan** — B menuntut 214 kunjungan, A hanya 88; selisih total biaya juga kecil sehingga keputusan peka terhadap taksiran biaya per kasus terlewat.

**Contoh jawaban C1(d)**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "Model A karena akurasi dan F1 lebih tinggi." | 0 |
| Cukup | "Model B karena biayanya paling kecil." | 0,75 |
| Baik | "Model B (Rp41,7 juta < Rp44,4 juta). Akurasi dan F1 menghitung FN dan FP setara, padahal biaya satu FN 8× biaya satu FP." | 2 |

**Rujukan:** [Bab 7](../06-buku-ajar/bab-07-klasifikasi-dan-metriknya.md) §7.3.1 (perhitungan manual), §7.3.2 (akurasi menyesatkan), §7.4.1 (ambang dari biaya).

---

### C2. Dua Model Perkiraan Penumpang Penyeberangan — `DAIML-Sub-CPMK102-1` · C3 (a, b) dan C4 (c, d) · 10 poin

**(a) MAE dan RMSE Model P** — C3 · 4 poin *(MAE: nilai mutlak dan jumlahnya 0,75 + hasil 0,75 · RMSE: kuadrat galat dan jumlahnya 1,25 + hasil 1,25)*

Galat mengikuti lembar rumus: $e = y - \hat{y}$ (positif = perkiraan terlalu rendah). Kolom Q untuk pemeriksaan; nilai Q diberikan pada soal.

| Hari | $y$ | P | $e_P$ | $\lvert e_P\rvert$ | $e_P^2$ | Q | $e_Q$ | $\lvert e_Q\rvert$ | $e_Q^2$ |
|------|-----|---|-------|------|------|---|-------|------|------|
| 1 | 32 | 33 | −1 | 1 | 1 | 27 | +5 | 5 | 25 |
| 2 | 28 | 27 | +1 | 1 | 1 | 32 | −4 | 4 | 16 |
| 3 | 45 | 43 | +2 | 2 | 4 | 40 | +5 | 5 | 25 |
| 4 | 30 | 31 | −1 | 1 | 1 | 34 | −4 | 4 | 16 |
| 5 | 65 | 51 | +14 | 14 | 196 | 61 | +4 | 4 | 16 |
| **Jumlah** | | | | **19** | **203** | | | **22** | **98** |

$$\text{MAE}_P=\frac{19}{5}=3{,}800 \qquad \text{RMSE}_P=\sqrt{\frac{203}{5}}=\sqrt{40{,}6}\approx 6{,}372$$

(satuan: ribu penumpang; pada soal: $\text{MAE}_Q = 4{,}400$, $\text{RMSE}_Q = \sqrt{19{,}6} \approx 4{,}427$)

**(b) $R^2$ Model P** — C3 · 1 poin *($SS_{res}$ = 203 dari (a) 0,5 · $R^2$ 0,5)*

$$R^2_P = 1-\frac{SS_{res}}{SS_{tot}} = 1-\frac{203}{958}=1-0{,}212=0{,}788 \qquad (\text{pada soal: } R^2_Q = 1-\tfrac{98}{958}=0{,}898)$$

**(c) Rasio RMSE/MAE** — C4 · 2 poin

P: $6{,}372/3{,}8 = 1{,}677$ (Q pada soal: 1,006) *(0,75)*. Rasio P jauh di atas 1 (dan di atas 1,5): sedikit galat besar mendominasi RMSE. Penyebabnya **hari ke-5** — galat +14 (perkiraan terlalu rendah) menyumbang 196 dari 203, atau 96,6% $SS_{res}$; tanpa hari ke-5, MAE P = 1,25 dan RMSE P = 1,32. Rasio Q ≈ 1 menunjukkan galatnya tersebar merata *(1,25)*.

Contoh *Baik* (2 poin): "Rasio 6,372/3,8 = 1,677. Hari ke-5 (galat 14) menyumbang 196 dari 203 kuadrat galat; satu galat besar mendominasi RMSE."

**(d) Ukuran yang membedakan arah galat dan pilihan model** — C4 · 3 poin

Galat $e = y - \hat{y}$ positif berarti perkiraan **terlalu rendah** → kapal kurang (kerugian besar); negatif berarti terlalu tinggi → kelebihan kapal (hanya biaya operasional).

**Jawaban model.** Ukuran: **besar perkiraan terlalu rendah pada hari puncak** (hari ke-5). P: $65 - 51 = 14$ ribu terlalu rendah; Q: $65 - 61 = 4$ ribu terlalu rendah. Pilih **Model Q**. Harga yang dibayar Q: perkiraannya terlalu tinggi 4 ribu pada hari ke-2 dan ke-4 (kelebihan kapal — hanya biaya), dan Q kalah pada MAE (4,4 vs 3,8) serta MAPE (12,1% vs 7,2%) karena P lebih tepat pada hari biasa. RMSE juga mengunggulkan Q, tetapi RMSE **simetris**: ia menghukum kelebihan perkiraan Q sama beratnya dengan kekurangan, sehingga tidak menjawab yang diminta.

| Unsur | Poin |
|-------|------|
| **Ukuran** — membedakan arah galat dan dikaitkan dengan kerugian (terlalu rendah = kapal kurang) = 1; ukuran simetris (RMSE, galat maksimum tanpa arah) yang dikaitkan dengan galat besar pada hari puncak = 0,5; ukuran simetris tanpa kaitan dengan hari puncak, termasuk MAE/MAPE = 0 | 1 |
| **Hitung** — ukuran dihitung benar untuk kedua model = 1; hanya mengutip angka yang sudah ada pada (a) dan soal (mis. RMSE) = 0,5 | 1 |
| **Pilihan** — Q dengan alasan yang menimbang **kedua** jenis kerugian: kekurangan pada hari puncak (mahal) dan harga yang dibayar Q berupa kelebihan perkiraan pada hari biasa (murah) atau kalah MAE = 1; ukuran kerugian asimetris yang dihitung sudah memenuhi unsur ini. Q dengan alasan satu sisi saja = 0,5; P = 0 (kecuali baris bobot ≤ 2 pada tabel berikut) | 1 |

Ukuran lain yang diterima (diperiksa dengan Python, §5):

| Ukuran yang dipakai | Hasil | Perlakuan |
|---------------------|-------|-----------|
| Perkiraan terlalu rendah pada hari puncak (jawaban model) | P 14, Q 4 → Q | **Penuh** |
| Jumlah perkiraan terlalu rendah pada semua hari | P 1 + 2 + 14 = 17; Q 5 + 5 + 4 = 14 → Q | **Penuh** |
| Kerugian linear asimetris: galat terlalu rendah × $w$, galat terlalu tinggi × 1 | P = $17w + 2$; Q = $14w + 8$; **seri pada $w = 2$** | **Penuh** bila $w > 2$ dinyatakan dan dikaitkan dengan "antrean berjam-jam vs hanya biaya" → Q (mis. $w = 3$: P 53, Q 50). Bobot ringan ($w \le 2$) tidak mengunggulkan Q ($w = 1{,}5$: P 27,5 vs Q 29). Memakai $w \le 2$ dan memilih P dengan hitungan benar = **2,0** (ukuran 0,5 · hitung 1 · pilihan 0,5); penuh bila titik seri $w = 2$ ditunjukkan dan diargumentasikan bahwa kerugian sebenarnya melampauinya |
| Kerugian kuadrat asimetris (galat kuadrat terlalu rendah × $w$) | P = $201w + 2$; Q = $66w + 32$; Q unggul untuk setiap $w > 0{,}22$ | **Penuh** bila $w \ge 1$ → Q |
| Galat maksimum | P 14 (hari ke-5, terlalu rendah); Q 5 → Q | Tanpa arah: ukuran simetris → unsur ukuran 0,5 bila dikaitkan dengan galat besar pada hari puncak, 0 bila tidak (paling banyak 2,5; tanpa kaitan 2,0). Bila dinyatakan sebagai **galat terlalu rendah terbesar** (P 14, Q 5; keduanya perkiraan terlalu rendah), itu ukuran berarah → unsur ukuran 1; **penuh** bila unsur pilihan terpenuhi |
| RMSE | P 6,372; Q 4,427 → Q | Simetris — RMSE ikut menghukum kelebihan perkiraan Q — sehingga unsur ukuran **0,5 bila dikaitkan dengan galat besar pada hari puncak, 0 bila tidak** (lihat contoh *Cukup*); paling banyak 2,5, tanpa kaitan 2,0. Bila keputusan didasarkan pada galat **terlalu rendah** hari puncak yang dihitung untuk kedua model (P 14, Q 4) dan dinyatakan sebagai ukurannya, sedangkan RMSE hanya pendukung, yang dinilai adalah ukuran berarah itu (baris pertama tabel ini): **penuh** bila unsur pilihan terpenuhi |
| MAE atau MAPE → P | P 3,8 / 7,2%; Q 4,4 / 12,1% | 0 |

**Contoh jawaban C2(d)**

| Tingkat | Contoh | Skor |
|---------|--------|------|
| Kurang | "Model P karena MAE-nya lebih kecil." | 0 |
| Cukup | "Model Q karena RMSE-nya lebih kecil (4,427 vs 6,372)." | 1,0 (ukuran 0 · hitung 0,5 · pilihan 0,5) |
| Cukup (hafalan) | "Model Q berdasarkan RMSE: kesalahan besar pada hari puncak paling merugikan dan RMSE menghukum galat besar; P meleset 14 ribu pada hari ke-5, Q hanya 4 ribu." | 2,0 (ukuran simetris yang dikaitkan dengan hari puncak 0,5 · hitung 1 · pilihan 0,5 — arah galat dan harga yang dibayar Q tidak dibahas) |
| Baik | "Ukuran: perkiraan terlalu rendah pada hari puncak (berarti kapal kurang). P: 65 − 51 = 14 ribu; Q: 65 − 61 = 4 ribu. Pilih Q; harganya hanya kelebihan 4 ribu pada hari ke-2 dan ke-4 (biaya operasional)." | 3 |

**Rujukan:** [Bab 6](../06-buku-ajar/bab-06-regresi-dan-metriknya.md) §6.4.2 (perhitungan manual), §6.4.3 (rasio RMSE/MAE), §6.4.4 (memilih metrik).

---

### C3. Validasi Silang Acak dan Berkelompok — `DAIML-Sub-CPMK102-1` · C3 (a) dan C4 (b–d) · 10 poin

**(a) Simpangan baku sampel skema berkelompok** — C3 · 4 poin *(simpangan dan kuadratnya 2 · $s$ 2 = langkah 1 + hasil 1)*

Rerata diberikan pada soal: $\bar x = 0{,}70$ (= 3,50/5); simpangan: +0,04; −0,01; +0,07; −0,12; +0,02; kuadrat: 0,0016; 0,0001; 0,0049; 0,0144; 0,0004 → jumlah 0,0214;

$$s=\sqrt{\frac{0{,}0214}{4}}=\sqrt{0{,}00535}\approx 0{,}073$$

Pemeriksaan skema acak (diberikan pada soal): $\bar x = 4{,}35/5 = 0{,}87$; jumlah kuadrat simpangan 0,0010; $s=\sqrt{0{,}0010/4}\approx 0{,}016$.

**(b) Mengapa acak lebih tinggi; taksiran yang dilaporkan** — C4 · 2 poin

Pada skema acak, siswa dari sekolah yang sama berada di lipatan latih dan validasi; model mempelajari ciri khas sekolah dan memanfaatkannya pada validasi → **kebocoran kelompok**, taksiran terlalu optimistis untuk sekolah baru (selisih 0,87 − 0,70 = 0,17) *(1)*. Karena model dipakai di 30 sekolah **yang tidak ada di data**, yang dilaporkan adalah skema **berkelompok**: F1 0,70 ± 0,073 *(1)*.

**(c) Lipatan L4** — C4 · 2 poin

L4 (0,58) berada 0,12 di bawah rerata dan memuat sebagian besar sekolah pulau kecil → model **kurang andal untuk sekolah di pulau-pulau kecil**, yang sifatnya berbeda (akses, ekonomi, jarak tempuh); saat L4 menjadi lipatan validasi, data latih hanya memuat 5 dari 12 sekolah pulau kecil (5 dari ±40 sekolah latih) *(1)*. Yang harus diperiksa: kinerja per kelompok sekolah (pulau kecil vs lainnya — *recall* dan *precision* per kelompok), keterwakilan di data latih, kesamaan makna fitur dan mutu label di sekolah-sekolah itu; jangan dipakai di sana sebelum diperiksa *(1)*. (Tanpa L4: rerata 0,73, simpangan baku 0,034 — L4 adalah sumber utama sebaran.)

**(d) Jawaban satu kalimat kepada kepala dinas** — C4 · 2 poin

Contoh: *"Di sekolah yang belum pernah dilihat model, F1 yang dapat diharapkan sekitar 0,70 (antarlipatan 0,58–0,77) — bukan 0,87 — dan dapat lebih rendah di sekolah pulau kecil, sehingga hasilnya sebaiknya dipakai sebagai alat bantu penapisan yang ditinjau guru BK dan dipantau per kelompok sekolah."*

| Unsur | Poin |
|-------|------|
| Angka yang benar (≈ 0,70) beserta ketidakpastiannya (simpangan atau rentang); angka tanpa ketidakpastian = 0,5 | 1 |
| Peringatan untuk sekolah pulau kecil atau batas pemakaian | 0,5 |
| Bahasa jujur tanpa janji berlebihan; tidak menyebut 0,87 sebagai harapan | 0,5 |

Jawaban dua kalimat yang memuat unsur yang sama tidak dikurangi.

**Contoh jawaban C3(b)–(d)**

| Tingkat | Contoh | Skor (b+c+d dari 6) |
|---------|--------|---------------------|
| Kurang | "(b) Acak lebih bagus jadi pakai acak. (c) L4 kurang beruntung. (d) Kinerja model 0,87." | 0 |
| Cukup | "(b) Acak bocor karena sekolah sama di latih dan uji; laporkan 0,70. (c) Sekolah pulau kecil berbeda, model kurang bagus di sana. (d) Sekitar 0,70." | 4,0 (b 2 · c 1 — tanpa yang harus diperiksa · d 1 — tanpa ketidakpastian dan peringatan: angka 0,5 + bahasa jujur 0,5) |
| Baik | "(b) Skema acak: siswa sekolah yang sama ada di lipatan latih dan validasi — kebocoran kelompok, terlalu optimistis. Laporkan skema berkelompok: 0,70 ± 0,073. (c) L4 rendah (0,58) dan memuat sebagian besar sekolah pulau kecil: model kurang andal di sana. Periksa kinerja per kelompok sekolah dan keterwakilannya di data latih sebelum dipakai. (d) 'Di sekolah baru, F1 sekitar 0,70 (0,58–0,77 antarlipatan), bukan 0,87, dan bisa lebih rendah di sekolah pulau kecil.'" | 6 |

**Rujukan:** [Bab 4](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md) §4.3.2 (pembagian berkelompok), §4.5.4 (kebocoran kelompok).

---

## 4. Kesalahan Umum

| Soal | Kesalahan | Perlakuan |
|------|-----------|-----------|
| A3 T2 | Menganggap usia 0 sebagai kesalahan tanpa menimbang data berat badan 2,5–9,8 kg | 0 poin pada T2 |
| A4 baris 3 | Menyatakan keputusan yang tepat sebagai keliru ("semua baris pasti salah") | 0 poin pada baris 3 |
| A6 (b) | Memilih α dengan RMSE latih terkecil | 0 pada pilihan; alasan dinilai menurut isinya |
| B1 (a) | Menyebut `StandardScaler` bocor | Tidak diberi poin (penskala sudah di dalam `Pipeline`) |
| B1 (b) | Memilih imputasi median sebagai kebocoran terbesar | 0,25 dari 1,5 pada pilihan; mekanisme tetap dinilai |
| B2 (b) | Menulis *recall* maks = 40/2.000 | 0 pada nilai *recall*; poin 60 sel tetap bila benar |
| B3 (a) | Menganggap `cat.codes` tepat karena "kategorinya hanya tiga" | 0 pada baris 5 |
| C1 (a) | Menukar baris/kolom (FP ↔ FN) | Kesalahan terbawa; potong 0,5 sekali pada (a) |
| C2 (a) | RMSE dihitung sebagai rerata \|galat\| lalu diakarkan | 0 pada hasil RMSE |
| C2 (a) | Tanda galat $\hat{y}-y$ (kebalikan lembar rumus) | Tidak dikurangi; nilai mutlak dan kuadratnya sama — tetapi pada (d) arah "terlalu rendah" harus ditafsirkan dengan benar |
| C3 (a) | Pembagi $n$ (hasil 0,065) | 1 dari 2 pada $s$ |

---

## 5. Memeriksa Angka dengan Python

Blok berikut dapat dijalankan apa adanya di Google Colab untuk memeriksa angka Bagian C, B2(b), dan A3. Jalankan **sesudah** Anda menghitung sendiri dengan kalkulator — di UTS tidak ada komputer.

```python
# Memeriksa angka Latihan UTS Dasar AI/ML (Bagian C, B2b, dan A3)
import numpy as np

# A3 (T2): proporsi baris usia 0 dari seluruh data kunjungan
print("A3 baris usia 0:", round(100 * 412 / 12480, 1), "%")

# B2(b): batas recall akibat kapasitas 40 sel
kejadian = 2000 * 0.03
print("B2 kejadian:", kejadian, "| recall maks:", round(40 / kejadian, 3))

# C1: metrik dari matriks konfusi dan biaya kesalahan
def metrik(tp, fn, fp, tn):
    akurasi = (tp + tn) / (tp + fn + fp + tn)
    presisi = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * presisi * recall / (presisi + recall)
    return [round(x, 3) for x in (akurasi, presisi, recall, f1)]

print("C1 Model A:", metrik(48, 32, 40, 880))
print("C1 Model B:", metrik(64, 16, 150, 770))
print("C1 akurasi tanpa kunjungan:", 920 / 1000)
biaya = lambda fn, fp: fn * 1.2 + fp * 0.15          # dalam juta rupiah
print("C1 biaya A, B (juta):", round(biaya(32, 40), 1), round(biaya(16, 150), 1))

# C2: metrik regresi dan galat berarah (e = y - y_topi; positif = terlalu rendah)
y = np.array([32, 28, 45, 30, 65])
for nama, y_topi in (("P", np.array([33, 27, 43, 31, 51])), ("Q", np.array([27, 32, 40, 34, 61]))):
    e = y - y_topi
    mae, rmse = np.mean(np.abs(e)), np.sqrt(np.mean(e ** 2))
    r2 = 1 - np.sum(e ** 2) / np.sum((y - y.mean()) ** 2)
    print(f"C2 {nama}: MAE {mae:.3f} RMSE {rmse:.3f} R2 {r2:.3f} rasio {rmse / mae:.3f} "
          f"| terlalu rendah {e[e > 0].sum()} | terlalu tinggi {-e[e < 0].sum()} | hari ke-5 {e[4]}")
print("C2 SS_tot:", np.sum((y - y.mean()) ** 2))

# C3: rerata dan simpangan baku sampel (ddof=1 = pembagi n-1)
acak = np.array([0.86, 0.88, 0.87, 0.85, 0.89])
kelompok = np.array([0.74, 0.69, 0.77, 0.58, 0.72])
for nama, v in (("acak", acak), ("kelompok", kelompok)):
    print(f"C3 {nama}: rerata {v.mean():.3f} s {v.std(ddof=1):.3f} (pembagi n: {v.std(ddof=0):.3f})")
```

Keluaran yang diharapkan: A3 3,3%; B2 60 dan 0,667; C1 A [0,928; 0,545; 0,6; 0,571], B [0,834; 0,299; 0,8; 0,435], tanpa kunjungan 0,92, biaya 44,4 dan 41,7; C2 P: MAE 3,800, RMSE 6,372, R² 0,788, rasio 1,677, terlalu rendah 17, terlalu tinggi 2, hari ke-5 14; Q: 4,400, 4,427, 0,898, 1,006, 14, 8, 4; $SS_{tot}$ 958; C3 acak 0,870 dan 0,016, kelompok 0,700 dan 0,073 (pembagi $n$: 0,065).

Perilaku kode yang menjadi dasar kunci B1 dan B3 juga diperiksa pada data sintetis (scikit-learn 1.6 dan 1.9): kode soal B1 dan kode rujukan B1(c) berjalan, dan kode rujukan tidak menempatkan satu pasien pun di latih dan uji sekaligus. Arah pada B1(b) adalah arah yang **diharapkan**, bukan jaminan untuk setiap pembagian: pada data sintetis dengan sifat laten per pasien (kecenderungan tak teramati yang memengaruhi gula darah dan status terkontrol pasien di setiap kunjungannya; dua pembangkit, masing-masing 10 ulangan), F1 yang dicetak kode soal lebih tinggi daripada F1 model terpilihnya pada pasien baru di 8–9 dari 10 ulangan, dengan selisih rata-rata hanya ±0,02, dan perbandingannya dengan F1 alur yang benar pada satu pembagian dapat berbalik karena keragaman acak. Bila Anda mencoba dengan `df` sintetis sendiri dan memperoleh hasil yang berbalik, ulangi dengan beberapa `random_state` sebelum menyimpulkan. Pemeriksaan lain: `cat.codes` memberi campur = 0, putra = 1, putri = 2; kode rujukan B3(d) berjalan tanpa nilai kosong, dan kecamatan baru mendapat rerata global data latih; `TargetEncoder` bawaan memakai `smooth="auto"` dan `cv=5`.

---

## Rujukan Belajar

| Bagian latihan | Bab buku ajar |
|----------------|---------------|
| A1, B4(a) | [Bab 1 — Lanskap Kecerdasan Artifisial](../06-buku-ajar/bab-01-lanskap-kecerdasan-artifisial.md) |
| A2, B2(a, d), B4(c) | [Bab 2 — Formulasi Masalah dan Daur Hidup Pembelajaran Mesin](../06-buku-ajar/bab-02-formulasi-masalah-daur-hidup-ml.md) |
| A3, A4, B3(b), B4(b) | [Bab 3 — Data dan Prapemrosesan](../06-buku-ajar/bab-03-data-dan-prapemrosesan.md) |
| B1, B3(a), C3 | [Bab 4 — Pembagian Data dan Kebocoran Data](../06-buku-ajar/bab-04-pembagian-data-dan-kebocoran.md) |
| A5, B3(c, d) | [Bab 5 — Rekayasa Fitur](../06-buku-ajar/bab-05-rekayasa-fitur.md) |
| A6, C2 | [Bab 6 — Regresi dan Metriknya](../06-buku-ajar/bab-06-regresi-dan-metriknya.md) |
| B2(b, c), B4(d), C1 | [Bab 7 — Klasifikasi dan Metriknya](../06-buku-ajar/bab-07-klasifikasi-dan-metriknya.md) |

Kisi-kisi dan ketentuan UTS: [kisi-kisi UTS](kisi-kisi-uts.md) · [Modul Minggu 8](../03-modules/week-08-uts-review-dan-ujian.md).

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
