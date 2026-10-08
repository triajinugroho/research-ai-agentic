---
id: uai-if52510031-latihan-uts
tipe: asesmen
judul: "Latihan UTS — Dasar Kecerdasan Artifisial dan Pembelajaran Mesin"
kode_mk: IF52510031
nama_mk: Dasar Kecerdasan Artifisial dan Pembelajaran Mesin
prodi: Informatika
versi: 1.0
status: draft
diperbarui: 2026-10-08
---

# LATIHAN UJIAN TENGAH SEMESTER (SIMULASI)

> **Latihan UTS — bukan naskah UTS.** Simulasi lengkap UTS Dasar Kecerdasan Artifisial dan Pembelajaran Mesin Ganjil 2026/2027 untuk berlatih: komposisi, durasi (120 menit), aturan alat bantu, dan tingkat kesulitannya sama dengan UTS. Naskah UTS sebenarnya disusun terpisah sebagai **varian** dari latihan ini — cetak biru butirnya sama (Sub-CPMK, level Bloom, skor), tetapi konteks, data, dan angkanya berbeda — dan tidak dipublikasikan.

## UNIVERSITAS AL AZHAR INDONESIA
### FAKULTAS SAINS DAN TEKNOLOGI — PROGRAM STUDI INFORMATIKA

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin |
| Kode | `IF52510031` |
| Semester | 5 — Ganjil 2026/2027 |
| Penyusun | Tri Aji Nugroho, S.T., M.T. |
| Waktu | **120 menit** |
| Sifat | ***Closed book*** |
| Alat bantu | **Kalkulator saja** |
| Cakupan | Minggu 1–7 |
| Kedudukan | Latihan mandiri, **tidak dinilai**. UTS sebenarnya: Minggu 8, Tes Tulis UTS berbobot 20% nilai akhir |

**Berkas pendamping:** [pembahasan dan pedoman skor](latihan-uts-pembahasan.md) · [cetak biru butir](latihan-uts-cetak-biru.md) · [kisi-kisi UTS](kisi-kisi-uts.md)

---

## Cara Memakai Latihan Ini

Baca bagian ini **sebelum** mulai menghitung waktu.

1. **Kerjakan seperti UTS sungguhan:** sediakan 120 menit tanpa jeda, kalkulator, dan lembar jawaban kosong. Kerjakan **tanpa alat bantu AI, tanpa catatan, dan tanpa membuka pembahasan** — aturannya sama dengan UTS.
2. Baru **sesudah** waktu habis, cocokkan jawaban Anda dengan [pembahasan](latihan-uts-pembahasan.md) dan nilai sendiri memakai pedoman skornya.
3. Catat butir yang skornya rendah, lalu baca ulang bab buku ajar yang dirujuk pembahasan untuk butir itu.
4. Jangan menghafal jawaban latihan ini. UTS sebenarnya memakai kasus, data, dan angka lain; yang terbawa ke ujian hanyalah **cara bernalar** pada setiap jenis butir.

---

## Petunjuk

1. Latihan terdiri atas **tiga bagian, 13 soal, total 100 poin**: A. Konsep (6 soal, 30 poin) · B. Analisis kasus (4 soal, 40 poin) · C. Perhitungan (3 soal, 30 poin). Bobot tiap soal dan sub-soal tertera di sampingnya.
2. Kerjakan pada lembar jawaban. Nomori jawaban sesuai nomor soal dan sub-soal. Urutan pengerjaan bebas.
3. **Tunjukkan langkah** pada setiap perhitungan. Tulis hasil dengan tiga angka di belakang koma kecuali diminta lain. Langkah benar dengan hasil akhir keliru karena salah hitung tetap bernilai sebagian besar; hasil tanpa langkah hanya bernilai sebagian.
4. Jawab dengan singkat dan tepat. Setiap jawaban Bagian A harus memuat **alasan**, dan soal yang meminta alasan dinilai terutama dari alasannya. Beberapa soal analisis tidak memiliki satu jawaban tunggal: penalaran yang tepat dan konsisten dinilai penuh walaupun kesimpulannya berbeda dari kunci.
5. Potongan kode pada soal tidak menuntut hafalan sintaks. Bila diminta menulis langkah atau kode, alur yang benar lebih penting daripada sintaks yang sempurna.
6. Yang **tidak** diperkenankan: catatan, buku, telepon, laptop, dan **alat bantu AI dalam bentuk apa pun**. Kalkulator di telepon genggam tidak diperkenankan.
7. Seluruh data, nama dataset, dan angka pada soal adalah **ilustrasi untuk keperluan latihan**, bukan data resmi lembaga mana pun.
8. Setiap soal atau sub-soal diberi tanda level Bloom dan poin, misalnya **[C4 · 5 poin]**.
9. Pembagian waktu yang disarankan: ±5 menit di awal untuk membaca petunjuk dan lembar rumus; Bagian A ±28 menit, B ±50 menit, C ±32 menit (jumlah ±110 menit, termasuk membaca soal); paling sedikit 5 menit di akhir untuk memeriksa jawaban.

> **Pernyataan amanah.** Lembar jawaban UTS memuat pernyataan berikut; biasakan sejak latihan: *"Dengan menuliskan nama dan NIM pada lembar jawaban, saya menyatakan mengerjakan ujian ini sendiri, tanpa bantuan orang lain maupun alat bantu yang tidak diperkenankan."*

---

## Lembar Rumus

$$\text{Akurasi}=\frac{TP+TN}{TP+TN+FP+FN} \qquad \text{Precision}=\frac{TP}{TP+FP} \qquad \text{Recall}=\frac{TP}{TP+FN}$$

$$\text{F1}=2\cdot\frac{P \cdot R}{P+R} \qquad \text{Spesifisitas}=\frac{TN}{TN+FP} \qquad \text{FPR}=\frac{FP}{FP+TN}$$

$$\text{MAE}=\frac{1}{n}\sum|y_i-\hat{y}_i| \qquad \text{RMSE}=\sqrt{\frac{1}{n}\sum(y_i-\hat{y}_i)^2} \qquad R^2=1-\frac{SS_{res}}{SS_{tot}}$$

$$\text{MAPE}=\frac{100\%}{n}\sum\left|\frac{y_i-\hat{y}_i}{y_i}\right|$$

$$\bar{x}=\frac{1}{n}\sum x_i \qquad s=\sqrt{\frac{\sum(x_i-\bar{x})^2}{n-1}} \quad \text{(simpangan baku sampel, pembagi } n-1\text{)}$$

---

## BAGIAN A — KONSEP (30 poin · disarankan 28 menit)

### A1. Layak Tidaknya Pembelajaran Mesin — **[C4 · 5 poin]**

Untuk **masing-masing** usulan kepada pemerintah kota berikut, analisislah apakah pembelajaran mesin (ML) layak dipakai dengan merujuk keadaan atau pertanyaan uji kelayakan yang relevan, lalu tentukan pendekatan yang sesuai. *(2,5 poin per usulan)*

- **(i)** Perkiraan tonase sampah harian yang masuk ke tempat pengolahan sampah terpadu (TPST) kota, dari catatan jembatan timbang tiga tahun terakhir, kalender hari libur, dan curah hujan, untuk menjadwalkan jumlah truk esok hari.
- **(ii)** Wali kota bertanya apakah program sarapan sehat di 40 SD **menyebabkan** kenaikan nilai rata-rata siswa. Tersedia data nilai seluruh SD di kota itu (peserta dan bukan peserta) selama dua tahun. Sekolah peserta dipilih dinas dari usulan kepala sekolah.

### A2. Kembali ke Tahap Mana? — **[C4 · 5 poin]**

Untuk setiap situasi berikut, analisislah buktinya untuk menentukan **tahap daur hidup proyek ML** yang harus didatangi kembali (formulasi masalah · data · eksplorasi dan penyiapan · *baseline* dan model · evaluasi dan analisis kesalahan · penerapan dan pemantauan), beserta alasan dan tindakannya. *(2,5 poin per situasi)*

- **(i)** Model perkiraan jumlah kendaraan per jam di sebuah gerbang tol bekerja baik selama setahun. Sejak ruas tol baru tersambung tiga bulan lalu, MAE-nya naik terus dari 120 menjadi 410 kendaraan/jam.
- **(ii)** Model prediksi pelanggan internet rumah yang akan berhenti berlangganan memperoleh F1 = 0,42 pada data uji — sama dengan F1 aturan sederhana "pelanggan yang menghubungi layanan keluhan ≥ 2 kali dalam sebulan terakhir" pada data uji yang sama. Pada situasi ini, tentukan tindakan bagi manajemen saat ini.

### A3. Membaca Hasil Pemeriksaan Kualitas Data — **[C4 · 5 poin]**

Data kunjungan pasien sebuah puskesmas (12.480 baris, 2024–2025) akan dipakai untuk memprediksi `kunjungan_ulang_30hari` (1 = pasien datang kembali dalam 30 hari). Pemeriksaan awal menghasilkan temuan berikut:

| No | Temuan |
|----|--------|
| T1 | `berat_badan_kg`: min = −99,0; median = 56,0; maks = 131,0 |
| T2 | `usia_tahun`: min = 0; ada 412 baris (3,3%) bernilai 0, seluruhnya tercatat di poli KIA (kesehatan ibu dan anak); `berat_badan_kg` pada 412 baris itu 2,5–9,8 kg |
| T3 | `jumlah_kunjungan_tahun_ini` berkorelasi 0,96 dengan target |

Untuk **setiap** temuan, analisislah apakah itu masalah. Bila ya, tentukan kemungkinan penyebabnya dan tindakan yang tepat; bila tidak, jelaskan mengapa. *(T1: 1,5 poin; T2 dan T3: masing-masing 1,75 poin)*

### A4. Menganalisis Keputusan Prapemrosesan — **[C4 · 5 poin]**

Sebuah RSUD membangun model **k-NN** untuk memprediksi pasien rawat jalan yang tidak datang pada jadwal kontrol berikutnya (*no-show*). Analis mengambil keputusan berikut:

| No | Kolom | Keterangan data | Keputusan analis |
|----|-------|-----------------|------------------|
| 1 | `skala_nyeri` | Bilangan 0–10 yang diisi perawat (0 = tidak nyeri, 10 = nyeri terberat) | `OneHotEncoder(handle_unknown="ignore")` |
| 2 | `biaya_rawat_sebelumnya` | Sangat menceng kanan; segelintir pasien bernilai ratusan juta rupiah, mayoritas di bawah Rp2 juta | `StandardScaler()` |
| 3 | `cara_bayar` | BPJS, umum, asuransi swasta | `OneHotEncoder(handle_unknown="ignore")` |

Untuk **setiap** baris, analisislah apakah keputusan itu tepat. Bila tidak, jelaskan akibatnya pada model k-NN dan tuliskan perbaikannya. *(Baris 1 dan 2: masing-masing 1,75 poin; baris 3: 1,5 poin)*

### A5. Merekayasa Fitur Waktu Antar — **[C4 · 5 poin]**

Sebuah layanan pesan-antar makanan di Surabaya memperkirakan **waktu antar (menit)** dengan **regresi linear**. Prediksi dibuat **saat kurir menerima tugas**. Analis menyiapkan tiga calon fitur:

| No | Calon fitur | Keterangan |
|----|-------------|------------|
| 1 | `jarak_km` dan `hujan` (0/1) | Dipakai sebagai dua fitur terpisah; pengamatan lapangan: hujan memperlambat jauh lebih besar pada pengantaran jarak jauh |
| 2 | `lama_masak_aktual_menit` | Diisi restoran ketika makanan siap diambil |
| 3 | `kecepatan_rata_kurir_30hari` | Rata-rata kecepatan kurir itu (km/jam) pada 30 hari sebelum pesanan ini |

Untuk **setiap** calon fitur, analisislah lalu tentukan: **pertahankan**, **ubah**, atau **buang**, beserta alasannya; bila diubah, tuliskan bentuk perubahannya. *(Fitur 1 dan 2: masing-masing 1,75 poin; fitur 3: 1,5 poin)*

### A6. Mendiagnosis dari Tabel α — **[C4 · 5 poin]**

Model Ridge (dengan `StandardScaler` di dalam `Pipeline`) memperkirakan konsumsi listrik bulanan rumah tangga (kWh) dari 40 fitur. Hasil untuk lima nilai α:

| α | 0,001 | 0,1 | 10 | 1.000 | 100.000 |
|---|-------|-----|----|-------|---------|
| RMSE latih (kWh) | 21 | 24 | 30 | 58 | 97 |
| RMSE validasi, rerata 5 lipatan (kWh) | 69 | 48 | 34 | 61 | 99 |

- **(a)** Diagnosis kondisi model pada α = 0,001 dan pada α = 100.000. Tunjukkan bukti dari tabel. *(2,5 poin)*
- **(b)** Nilai α mana yang Anda pilih? Jelaskan mengapa pemilihan tidak didasarkan pada RMSE latih. *(2,5 poin)*

---

## BAGIAN B — ANALISIS KASUS (40 poin · disarankan 50 menit)

### B1. Kebocoran pada Model Pasien Prolanis — **[10 poin]**

Sebuah puskesmas ingin memprediksi apakah pasien diabetes peserta Prolanis akan berstatus **tidak terkontrol** pada pemeriksaan triwulan berikutnya. Data berisi **9.600 baris kunjungan dari 1.600 pasien** (rata-rata 6 kunjungan per pasien). Selain ciri yang berubah tiap kunjungan (gula darah puasa, kepatuhan minum obat), data memuat ciri yang **tetap** per pasien (jenis kelamin, tinggi badan, usia saat terdaftar di Prolanis). Model akan dipakai untuk **pasien baru** yang mendaftar tahun depan. Abaikan persoalan pembagian temporal pada soal ini.

```python
 1  df = pd.read_csv("kunjungan_prolanis.csv")
 2  df["gula_puasa"] = df["gula_puasa"].fillna(df["gula_puasa"].median())
 3  X = df.drop(columns=["id_pasien", "tidak_terkontrol"])
 4  y = df["tidak_terkontrol"]
 5  X_tr, X_te, y_tr, y_te = train_test_split(
 6      X, y, test_size=0.2, stratify=y, random_state=7)
 7
 8  terbaik = None
 9  for k in [3, 5, 7, 9, 11, 15]:
10      model = Pipeline([("skala", StandardScaler()),
11                        ("knn", KNeighborsClassifier(n_neighbors=k))])
12      model.fit(X_tr, y_tr)
13      f1 = f1_score(y_te, model.predict(X_te))
14      if terbaik is None or f1 > terbaik[1]:
15          terbaik = (k, f1)
16  print("k terbaik:", terbaik[0], "| F1 uji:", round(terbaik[1], 3))
```

- **(a)** Analisislah kode di atas dan temukan **tiga** kebocoran. Untuk masing-masing, tunjukkan nomor barisnya dan jenisnya menurut enam jenis kebocoran yang dipelajari. **[C4 · 3 poin]**
- **(b)** Ke arah mana F1 yang dicetak baris 16 menyimpang dari kinerja model pada pasien baru? Dari ketiga kebocoran, pilih yang Anda perkirakan **paling besar** dampaknya pada data ini, lalu analisislah **mekanismenya**: bagaimana informasi dari data uji sampai ke model atau ke angka yang dilaporkan. **[C4 · 4 poin]**
- **(c)** Terapkan perbaikan: tuliskan ulang alur baris 2–16 sebagai **langkah bernomor atau pseudokode** (nama kelas dan fungsi pustaka tidak wajib) sehingga seluruh kebocoran hilang dan F1 yang dicetak menjadi taksiran jujur kinerja model pada pasien baru. **[C3 · 3 poin]**

### B2. Patroli Kebakaran Lahan Gambut — **[10 poin]**

Balai pengendalian kebakaran hutan dan lahan di Kalimantan Tengah membagi kawasan gambut wilayah kerjanya menjadi **2.000 sel** (1 km × 1 km). Setiap **Senin pukul 07.00**, kepala balai menetapkan **paling banyak 40 sel** yang dipatroli regu darat selama minggu itu.

Tim data mengusulkan model untuk "memprediksi kebakaran" dari data per sel per minggu 2019–2025: jumlah hari tanpa hujan, muka air tanah gambut terakhir terukur, jarak ke kanal dan ke permukiman, tutupan lahan, dan jumlah titik panas minggu sebelumnya. Rata-rata **3% sel-minggu** mengalami kebakaran. Pada data uji, tim melaporkan **akurasi 0,97**.

- **(a)** Usulan "memprediksi kebakaran" belum dapat dipelajari. Rumuskan targetnya dengan **keempat unsur** target, selaras dengan saat keputusan diambil, dan tentukan jenis *task*-nya. **[C6 · 2 poin]**
- **(b)** Pada minggu yang jumlah kejadiannya sama dengan rata-rata, hitung jumlah sel yang terbakar dan *recall* tertinggi yang mungkin dicapai bila ke-40 sel yang dipatroli **semuanya** tepat, lalu analisislah arti angka itu bagi penetapan target kinerja model. **[C4 · 2 poin]**
- **(c)** Analisislah mengapa akurasi 0,97 **tidak** menjawab pertanyaan kepala balai, "Apakah 40 sel yang kita patroli sudah tepat?" Usulkan cara menetapkan ambang dan metrik evaluasi yang sesuai dengan keputusan itu. **[C4 · 3 poin]**
- **(d)** Pilih **pembanding** (*baseline*) yang paling bermakna untuk model ini dan beri argumentasi pilihan Anda. **[C5 · 3 poin]**

### B3. Model Harga Sewa Kos — **[10 poin]**

Sebuah situs iklan memperkirakan **harga sewa kos per bulan (ribu rupiah)** di Yogyakarta dengan **regresi linear**. Model akan dipakai untuk menyarankan harga ketika pemilik memasang **iklan baru**.

```python
 1  df = pd.read_csv("iklan_kos_yogyakarta.csv")
 2  df["bulan"] = pd.to_datetime(df["tanggal_iklan"]).dt.month
 3  df["harga_rata_kecamatan"] = df.groupby("kecamatan")["harga_sewa"].transform("mean")
 4  df["harga_per_m2"] = df["harga_sewa"] / df["luas_kamar_m2"]
 5  df["tipe_kode"] = df["tipe"].astype("category").cat.codes   # putra/putri/campur
 6  df = df.dropna()
 7  X = df[["luas_kamar_m2", "jarak_kampus_km", "kamar_mandi_dalam", "ac",
 8          "bulan", "harga_rata_kecamatan", "harga_per_m2", "tipe_kode"]]
 9  y = df["harga_sewa"]
10  X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=1)
11  model = LinearRegression().fit(X_tr, y_tr)
```

Keterangan: `luas_kamar_m2` kosong pada **30% iklan**, hampir seluruhnya iklan **pemilik perorangan** (kolom `jenis_pengiklan`), yang rata-rata harganya lebih rendah daripada iklan agen. Permintaan kos memuncak menjelang tahun ajaran baru (**Juli–Agustus**). Abaikan persoalan pembagian temporal pada soal ini.

- **(a)** Untuk baris **3, 4, dan 5**, analisislah masalahnya dan beri nama jenis kekeliruannya. **[C4 · 3 poin]**
- **(b)** Berdasarkan keterangan, tentukan pola nilai hilang yang paling mungkin pada `luas_kamar_m2`. Analisislah akibat baris 6 terhadap saran harga untuk iklan pemilik perorangan, lalu usulkan penanganan yang lebih tepat. **[C4 · 3 poin]**
- **(c)** Fitur `bulan` (1–12) dimasukkan apa adanya ke regresi linear. Jelaskan mengapa bentuk itu tidak dapat menangkap lonjakan Juli–Agustus, lalu terapkan penyandian yang tepat pada fitur `bulan`. **[C3 · 2 poin]**
- **(d)** Informasi "harga khas kecamatan" tetap ingin dipakai sebagai fitur, padahal sebagian kecamatan hanya memiliki 1–3 iklan. Terapkan cara memperoleh nilai fitur ini untuk **(i)** baris-baris data latih dan **(ii)** kecamatan yang iklannya sedikit, masing-masing dengan alasan singkat (boleh berupa langkah atau kode ringkas). **[C3 · 2 poin]**

### B4. "Sistem AI" Penetapan Penerima Bantuan Sosial — **[10 poin]**

Pemerintah sebuah kabupaten mengusulkan "sistem AI" yang **secara otomatis dan final** menetapkan rumah tangga penerima bantuan sosial tahun depan **tanpa verifikasi lapangan**. Rencana tim:

- **Data:** pendataan kesejahteraan 68.000 rumah tangga tahun 2019 — jumlah anggota, kondisi rumah, pekerjaan kepala rumah tangga, aset, penghasilan bulanan.
- **Label:** keputusan "layak/tidak layak" yang diusulkan kepala desa pada penyaluran 2020–2023. Inspektorat pernah menemukan usulan penerima di sejumlah desa yang dipengaruhi kedekatan keluarga.
- **Nilai hilang:** `penghasilan_bulanan` kosong pada 15% rumah tangga, paling sering pada rumah tangga berpenghasilan tidak tetap (buruh harian, nelayan kecil) yang tidak dapat menyebut angkanya. Tim berencana mengisinya dengan median.
- **Ukuran keberhasilan:** akurasi ≥ 90% terhadap label tahun 2023.

- **(a)** Analisislah usulan ini dengan **uji kelayakan enam pertanyaan**: pilih dua pertanyaan yang jawabannya paling bermasalah, tunjukkan buktinya dari skenario, dan kaitkan masing-masing dengan satu **batas kemampuan AI** yang relevan. **[C4 · 3 poin]**
- **(b)** Analisislah ke arah mana rencana imputasi median menggeser keputusan bagi rumah tangga berpenghasilan tidak tetap. Apakah mengganti median keseluruhan dengan median per jenis pekerjaan sudah menyelesaikan masalah itu? Beri alasan. **[C4 · 2 poin]**
- **(c)** Rancang ulang usulan ini dengan menetapkan: (i) peran model, (ii) definisi label yang lebih tepat, dan (iii) satu mekanisme pengawasan. **[C6 · 3 poin]**
- **(d)** Bandingkan dampak dua jenis kesalahan — rumah tangga layak yang tidak menerima dan rumah tangga tidak layak yang menerima — lalu tentukan metrik pengganti "akurasi ≥ 90%" yang sesuai dengan perbandingan itu. **[C4 · 2 poin]**

---

## BAGIAN C — PERHITUNGAN (30 poin · disarankan 32 menit)

### C1. Dua Model Kunjungan Dokter Hewan — **[10 poin]**

Sebuah koperasi susu di Jawa Timur memakai model untuk memilih peternak anggota yang perlu dikunjungi dokter hewan karena sapinya diduga terkena **mastitis subklinis**, peradangan ambing tanpa gejala tampak yang menurunkan mutu susu (**positif = mastitis**). Pada data uji **1.000 peternak** (80 kasus mastitis), dua model menghasilkan:

```
                 MODEL A                                  MODEL B
                      PREDIKSI                                 PREDIKSI
 AKTUAL         Sehat    Mastitis       AKTUAL           Sehat    Mastitis
 Sehat            880        40         Sehat              770       150
 Mastitis          32        48         Mastitis            16        64
```

Untuk Model B telah dihitung: akurasi 0,834; *precision* 0,299; *recall* 0,800; F1 0,435.

Taksiran biaya: setiap kasus mastitis yang **terlewat** merugikan peternak **Rp1.200.000**; setiap kunjungan dokter hewan ke peternak yang ternyata sehat menghabiskan **Rp150.000**.

- **(a)** Hitung akurasi, *precision*, *recall*, dan F1 untuk **Model A**. Tunjukkan langkahnya. **[C3 · 4 poin]**
- **(b)** Kebijakan "tidak ada kunjungan sama sekali" setara dengan model yang memprediksi setiap peternak "sehat". Hitung akurasi kebijakan itu. **[C3 · 1 poin]**
- **(c)** Hitung total biaya kesalahan Model A dan Model B. **[C3 · 3 poin]**
- **(d)** Tentukan model yang dipilih, lalu analisislah mengapa akurasi dan F1 memberi peringkat yang berlawanan dengan total biaya. **[C4 · 2 poin]**

### C2. Dua Model Perkiraan Penumpang Penyeberangan — **[10 poin]**

Operator pelabuhan penyeberangan memperkirakan jumlah penumpang harian (**ribu orang**) untuk menentukan jumlah kapal yang dioperasikan. Dua model diuji pada lima hari; **hari ke-5 adalah puncak arus mudik**.

| Hari | 1 | 2 | 3 | 4 | 5 |
|------|---|---|---|---|---|
| Sebenarnya ($y$) | 32 | 28 | 45 | 30 | 65 |
| Model P ($\hat{y}$) | 33 | 27 | 43 | 31 | 51 |
| Model Q ($\hat{y}$) | 27 | 32 | 40 | 34 | 61 |

Rerata nilai sebenarnya $\bar{y} = 40$ dan $SS_{tot} = \sum(y_i-\bar{y})^2 = 958$. Untuk Model Q telah dihitung: MAE = 4,400; RMSE = 4,427; $R^2$ = 0,898.

- **(a)** Hitung MAE dan RMSE **Model P**. **[C3 · 4 poin]**
- **(b)** Hitung $R^2$ Model P, dengan $SS_{res} = \sum(y_i-\hat{y}_i)^2$ untuk Model P. **[C3 · 1 poin]**
- **(c)** Hitung rasio RMSE/MAE Model P (rasio Model Q = 1,006), lalu analisislah pengamatan yang menyebabkan rasio Model P jauh lebih besar. **[C4 · 2 poin]**
- **(d)** Kekurangan kapal pada hari puncak menimbulkan antrean kendaraan berjam-jam, sedangkan kelebihan satu kapal pada hari biasa hanya menambah biaya operasional. Tetapkan satu ukuran pembanding yang **membedakan perkiraan terlalu rendah dari perkiraan terlalu tinggi** sesuai kerugian itu (boleh ukuran yang tidak ada pada lembar rumus), hitung ukuran itu untuk kedua model, bandingkan, lalu tentukan model yang dipilih. **[C4 · 3 poin]**

### C3. Validasi Silang Acak dan Berkelompok — **[10 poin]**

Dinas pendidikan sebuah provinsi kepulauan membangun model untuk memprediksi siswa SMA yang berisiko putus sekolah, dari data **6.000 siswa di 50 sekolah**. Model akan dipakai di **30 sekolah lain yang tidak ada di data**. Model yang sama dinilai dengan dua skema validasi silang 5 lipatan (metrik F1):

| Skema | L1 | L2 | L3 | L4 | L5 |
|-------|----|----|----|----|----|
| Acak (`KFold`) | 0,86 | 0,88 | 0,87 | 0,85 | 0,89 |
| Berkelompok per sekolah (`GroupKFold`) | 0,74 | 0,69 | 0,77 | 0,58 | 0,72 |

Lipatan **L4** pada skema berkelompok memuat 7 dari 12 sekolah yang terletak di **pulau-pulau kecil**; setiap lipatan lain memuat paling banyak 2 sekolah semacam itu.

- **(a)** Hitung rerata dan simpangan baku sampel (pembagi $n-1$) skema **berkelompok**. Untuk skema acak telah dihitung: rerata 0,870; simpangan baku sampel 0,016. **[C3 · 4 poin]**
- **(b)** Analisislah mengapa rerata skema acak jauh lebih tinggi, dan tentukan taksiran mana yang harus dilaporkan untuk penerapan di 30 sekolah baru. **[C4 · 2 poin]**
- **(c)** Analisislah apa yang ditunjukkan skor L4 tentang kinerja model di sekolah-sekolah pulau kecil, dan apa yang harus diperiksa sebelum model dipakai di sana. **[C4 · 2 poin]**
- **(d)** Kepala dinas bertanya, "Berapa kinerja yang dapat kami harapkan di sekolah baru?" Hubungkan hasil (a)–(c) menjadi jawaban **satu kalimat** yang jujur dan dapat dipertanggungjawabkan. **[C4 · 2 poin]**

---

**— Selesai. Periksa kembali nomor jawaban Anda, lalu buka [pembahasan](latihan-uts-pembahasan.md). —**

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
