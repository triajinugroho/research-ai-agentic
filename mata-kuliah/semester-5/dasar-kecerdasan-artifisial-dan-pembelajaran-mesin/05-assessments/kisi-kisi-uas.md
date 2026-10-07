# Kisi-Kisi Ujian Akhir Semester

## Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — IF52510031

**Minggu 16 · Bobot 15% · Sub-CPMK `DAIML-Sub-CPMK082-1`**
**Tes tulis, *closed book*, 120 menit**

---

## 1. Ketentuan

| Aspek | Ketentuan |
|-------|-----------|
| Bentuk | Tes tulis di kelas |
| Durasi | 120 menit |
| Sifat | ***Closed book*** |
| Alat bantu yang diperkenankan | **Kalkulator saja** |
| Yang tidak diperkenankan | Catatan, buku, telepon, laptop, **alat bantu AI dalam bentuk apa pun** |
| Rumus | **Disediakan pada lembar soal** |

---

## 2. Cakupan

Seluruh materi semester, dengan penekanan pada Minggu 9–14 dan pada `DAIML-Sub-CPMK082-1`: **menganalisis karakteristik masalah dan merancang model yang sesuai**.

| Minggu | Topik | Porsi perkiraan |
|--------|-------|-----------------|
| 1–7 | Materi UTS (sebagai dasar perancangan) | 15% |
| 9 | Pohon keputusan; *ensemble* | 18% |
| 10 | SVM; Naive Bayes; pemilihan model | 17% |
| 11 | *Clustering*; deteksi anomali | 15% |
| 12 | PCA; kurva diagnostik | 12% |
| 13 | Jaringan saraf tiruan | 13% |
| 14 | AI generatif; *bias*; *fairness*; tanggung jawab | 10% |

---

## 3. Komposisi Soal

| Bagian | Bobot | Bentuk | Jumlah soal |
|--------|-------|--------|-------------|
| **A. Konsep** | 25% | Uraian singkat | 5 soal |
| **B. Perancangan solusi** | 45% | Merancang solusi ML untuk masalah baru | 2 soal besar |
| **C. Perhitungan** | 30% | Hitung manual | 3 soal |

Bagian B adalah yang terbesar — dan bentuknya berbeda dari UTS.

---

## 4. Bentuk Soal Bagian B

Soal perancangan **tidak memiliki satu jawaban benar**. Yang dinilai adalah ketepatan penalaran dan kelengkapan pertimbangan. Setiap soal menuntut enam hal:

| # | Yang diminta |
|---|--------------|
| (a) | Formulasi *task*: target, jenis *task*, **kapan prediksi dibutuhkan** |
| (b) | Fitur yang **tidak boleh** dipakai beserta alasannya |
| (c) | Metrik beserta alasan, dikaitkan dengan dampak kesalahan |
| (d) | Minimal tiga model kandidat beserta alasan pemilihannya |
| (e) | Protokol evaluasi yang adil (pembagian, validasi, *baseline*) |
| (f) | Dua risiko etis dan cara menanganinya |

---

## 5. Rumus yang Disediakan

$$H(S)=-\sum_i p_i\log_2 p_i \qquad G(S)=1-\sum_i p_i^2 \qquad IG(S,A)=H(S)-\sum_v \frac{|S_v|}{|S|}H(S_v)$$

$$\sigma(z)=\frac{1}{1+e^{-z}} \qquad \sigma'(z)=\sigma(z)\bigl(1-\sigma(z)\bigr) \qquad w \leftarrow w-\eta\frac{\partial L}{\partial w}$$

$$s(i)=\frac{b(i)-a(i)}{\max\{a(i),b(i)\}} \qquad \text{Precision}=\frac{TP}{TP+FP} \qquad \text{Recall}=\frac{TP}{TP+FN}$$

Nilai $\log_2$ yang sering dipakai juga disediakan dalam tabel kecil.

---

## 6. Contoh Soal

### Bagian A — Konsep

**A1.** Jelaskan mengapa metode *ensemble* umumnya mengungguli pohon tunggal. Kaitkan dengan tukar-tambah bias–varians.

**A2.** Jelaskan perbedaan *bagging* dan *boosting* dalam cara melatih pohon-pohonnya, dan sebutkan satu kelebihan serta satu kekurangan masing-masing.

**A3.** Sebuah tim melaporkan skor *silhouette* 0,68 pada hasil *clustering* mereka, lalu menyimpulkan bahwa klasternya bermakna. Jelaskan mengapa kesimpulan itu belum sah, dan apa yang masih harus dilakukan.

**A4.** Jelaskan mengapa ukuran-ukuran *fairness* (*demographic parity*, *equal opportunity*, *equalized odds*) **tidak dapat dipenuhi sekaligus** ketika angka kejadian dasar berbeda antarkelompok. Apa konsekuensinya bagi seorang insinyur?

**A5.** Sebuah model memiliki akurasi keseluruhan 0,88, tetapi *recall* pada kelompok yang hanya berjumlah 3% dari data adalah 0,45. Jelaskan (a) mengapa angka keseluruhan tidak memperlihatkan masalah ini, dan (b) apa yang harus dilaporkan pada *model card*.

### Bagian B — Perancangan Solusi

**B1.** Sebuah dinas kesehatan provinsi memiliki data kunjungan 40.000 pasien puskesmas selama tiga tahun, mencakup 15 variabel demografis dan klinis. Data terpusat pada lima kabupaten dari total 20 kabupaten di provinsi itu. Dinas ingin mengenali pasien yang berisiko **tidak kembali** untuk pengobatan lanjutan, agar dapat dihubungi lebih dahulu.

Rancang solusinya, dengan menjawab (a)–(f) pada §4.

**B2.** Sebuah koperasi simpan pinjam dengan 12.000 anggota ingin memahami **pola kelompok anggotanya** untuk merancang produk yang sesuai. Data yang tersedia: riwayat simpanan, riwayat pinjaman, frekuensi transaksi, jenis usaha, dan lama keanggotaan. Tidak ada label apa pun.

(a) Paradigma pembelajaran apa yang sesuai? Jelaskan.
(b) Tentukan algoritma kandidat beserta alasannya.
(c) Bagaimana menentukan jumlah kelompok?
(d) Bagaimana mengevaluasi hasilnya, mengingat tidak ada jawaban benar?
(e) Apa yang harus ada dalam laporan agar hasilnya berguna bagi pengurus koperasi?
(f) Sebutkan satu risiko etis dari pengelompokan anggota dan cara menanganinya.

### Bagian C — Perhitungan

**C1.** Sebuah simpul pohon keputusan memuat 200 sampel: 120 kelas A dan 80 kelas B. Percabangan pada fitur X menghasilkan:

| Cabang | n | Kelas A | Kelas B |
|--------|---|---------|---------|
| X ≤ 5 | 120 | 90 | 30 |
| X > 5 | 80 | 30 | 50 |

(a) Hitung *entropy* simpul induk.
(b) Hitung *entropy* masing-masing cabang.
(c) Hitung *information gain* percabangan ini.
(d) Hitung *Gini impurity* simpul induk.
(e) Sebuah fitur lain memberi *information gain* 0,08. Percabangan mana yang akan dipilih pohon? Jelaskan.

**C2.** Sebuah jaringan 2-2-1 dengan aktivasi sigmoid memiliki bobot:

| Lapis | Bobot |
|-------|-------|
| Masukan → tersembunyi | $w_{11}=0{,}4$, $w_{12}=0{,}6$, $w_{21}=0{,}3$, $w_{22}=0{,}2$; bias 0 |
| Tersembunyi → keluaran | $v_1=0{,}5$, $v_2=0{,}8$; bias 0 |

Masukan $x = [1, 1]$, target $y = 0$, laju pembelajaran $\eta = 0{,}2$.

(a) Hitung $z_1$, $z_2$, $h_1$, $h_2$.
(b) Hitung $z_{\text{out}}$ dan $\hat{y}$.
(c) Hitung *loss* dengan MSE.
(d) Hitung $\delta_{\text{out}}$.
(e) Hitung $\partial L/\partial v_1$ dan $\partial L/\partial v_2$, lalu perbarui $v_1$ dan $v_2$.
(f) Apakah kedua bobot naik atau turun? Jelaskan mengapa arah itu masuk akal.

**C3.** Sebuah perbandingan model menghasilkan:

| Model | ROC-AUC rerata | Simpangan |
|-------|----------------|-----------|
| Random Forest | 0,842 | 0,018 |
| Gradient Boosting | 0,851 | 0,022 |
| SVM (RBF) | 0,838 | 0,015 |
| Baseline | 0,500 | 0,000 |

(a) Model mana yang reratanya tertinggi?
(b) Hitung simpangan gabungan antara dua model teratas ($\sqrt{s_1^2+s_2^2}$).
(c) Apakah selisih antara keduanya lebih besar daripada simpangan gabungan itu? Apa kesimpulannya?
(d) Bila *Random Forest* jauh lebih cepat dilatih dan lebih mudah dijelaskan, model mana yang Anda rekomendasikan? Jelaskan.
(e) Apa yang akan Anda periksa bila salah satu model menghasilkan ROC-AUC 0,98?

---

## 7. Persiapan yang Disarankan

| Kegiatan | Perkiraan waktu |
|----------|-----------------|
| Membaca ulang Bab 8–13 buku ajar | 5 jam |
| Meninjau kembali Bab 1–7 secara ringkas | 2 jam |
| Mengerjakan Latihan Soal tingkat Mahir tiap bab | 4 jam |
| **Berlatih soal perancangan** pada dokumen ini | **4 jam** |
| Berlatih perhitungan manual tanpa komputer | 2 jam |

Bagian B berbobot 45% — porsi terbesar. Berlatih merancang solusi untuk masalah yang belum pernah dilihat lebih berguna daripada menghafal materi.

---

## 8. Kaidah Penilaian Bagian B

Karena soal perancangan tidak memiliki satu jawaban benar:

| Unsur | Yang dinilai |
|-------|--------------|
| Formulasi *task* | Ketepatan target dan penentuan kapan prediksi dibutuhkan |
| Fitur terlarang | Ketepatan mengenali kebocoran, bukan jumlah fitur yang disebut |
| Metrik | **Keterkaitan dengan dampak kesalahan**, bukan nama metriknya |
| Model kandidat | Kesesuaian dengan sifat data dan kebutuhan; alasan yang ditulis |
| Protokol evaluasi | Kesesuaian strategi pembagian; kehadiran *baseline* |
| Risiko etis | Kekonkretan, bukan pernyataan umum |

> Jawaban yang berbeda dari kunci tetapi penalarannya tepat dan konsisten memperoleh **nilai penuh**.

---

## 9. Dokumen Terkait

1. [Modul Minggu 16 — tinjauan dan ujian](../03-modules/week-16-uas-review-dan-ujian.md)
2. [Kerangka asesmen](assessment-framework.md)
3. Bab 8–13 [buku ajar](../06-buku-ajar/00-halaman-depan.md)
4. [Lampiran buku ajar](../06-buku-ajar/lampiran.md) — formularium
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
