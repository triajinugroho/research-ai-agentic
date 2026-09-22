# Kisi-Kisi Ujian Tengah Semester

## Dasar Kecerdasan Artifisial dan Pembelajaran Mesin — IF52510031

**Minggu 8 · Bobot 20% · Sub-CPMK `DAIML-Sub-CPMK102-1`**
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

Minggu 1–7, dengan penekanan pada `DAIML-Sub-CPMK102-1`: penyiapan data, pembagian tanpa kebocoran, rekayasa fitur, dan pemilihan serta penafsiran metrik.

| Minggu | Topik | Porsi perkiraan |
|--------|-------|-----------------|
| 1 | Lanskap AI; kapan ML tidak dipakai | 8% |
| 2 | Formulasi *task*; metrik; *baseline* | 15% |
| 3 | Kualitas data; prapemrosesan; `Pipeline` | 18% |
| 4 | Pembagian data; **enam jenis kebocoran** | 22% |
| 5 | Rekayasa fitur; pemilihan fitur | 12% |
| 6 | Regresi; regularisasi; metrik regresi | 12% |
| 7 | Klasifikasi; matriks konfusi; metrik | 13% |

---

## 3. Komposisi Soal

| Bagian | Bobot | Bentuk | Jumlah soal |
|--------|-------|--------|-------------|
| **A. Konsep** | 30% | Uraian singkat | 6 soal |
| **B. Analisis kasus** | 40% | Analisis kode/skenario | 4 soal |
| **C. Perhitungan** | 30% | Hitung manual | 3 soal |

---

## 4. Yang Diuji dan Yang Tidak

| Diuji | Tidak diuji |
|-------|-------------|
| Penalaran atas prosedur | Hafalan nama fungsi |
| Perhitungan metrik secara manual | Sintaks lengkap `scikit-learn` |
| Menemukan kebocoran dari potongan kode | Menulis program panjang dari nol |
| Memilih metrik **beserta alasannya** | Menghafal nilai baku hiperparameter |
| Mendiagnosis kondisi model | Menurunkan rumus dari awal |
| Menilai kelayakan pemakaian ML | Menghafal tahun dan penulis makalah |

---

## 5. Rumus yang Disediakan

Lembar soal memuat:

$$\text{Akurasi}=\frac{TP+TN}{TP+TN+FP+FN} \qquad \text{Precision}=\frac{TP}{TP+FP} \qquad \text{Recall}=\frac{TP}{TP+FN}$$

$$\text{F1}=2\cdot\frac{P \cdot R}{P+R} \qquad \text{Spesifisitas}=\frac{TN}{TN+FP} \qquad \text{FPR}=\frac{FP}{FP+TN}$$

$$\text{MAE}=\frac{1}{n}\sum|y_i-\hat{y}_i| \qquad \text{RMSE}=\sqrt{\frac{1}{n}\sum(y_i-\hat{y}_i)^2} \qquad R^2=1-\frac{SS_{res}}{SS_{tot}}$$

$$\text{MAPE}=\frac{100\%}{n}\sum\left|\frac{y_i-\hat{y}_i}{y_i}\right|$$

---

## 6. Contoh Soal

### Bagian A — Konsep

**A1.** Sebutkan tiga keadaan ketika pembelajaran mesin **sebaiknya tidak** dipakai, beserta alasan dan pendekatan pengganti untuk masing-masing.

**A2.** Jelaskan perbedaan MCAR, MAR, dan MNAR. Mengapa MNAR tidak dapat diperbaiki secara statistik, dan apa yang harus dilakukan analis ketika menghadapinya?

**A3.** Sebuah dataset memuat kolom `pendidikan` dengan nilai SD, SMP, SMA, S1, S2. Seorang mahasiswa menyandikannya dengan `OneHotEncoder`. Rekan sekelompoknya menyandikannya dengan `OrdinalEncoder` tanpa menentukan urutan. Keduanya keliru — jelaskan kekeliruan masing-masing dan tuliskan cara yang benar.

**A4.** Jelaskan mengapa `Pipeline` mencegah kebocoran **secara struktural**, bukan sekadar merapikan kode.

**A5.** Sebutkan tiga algoritma yang **membutuhkan** penskalaan fitur dan tiga yang **tidak**. Jelaskan alasan perbedaannya.

**A6.** Jelaskan perbedaan Ridge dan Lasso, dan sebutkan satu keadaan ketika Lasso lebih disukai.

### Bagian B — Analisis Kasus

**B1.** Perhatikan potongan kode berikut:

```python
X_scaled = StandardScaler().fit_transform(X)
selector = SelectKBest(f_classif, k=10).fit(X_scaled, y)
X_sel = selector.transform(X_scaled)
X_tr, X_te, y_tr, y_te = train_test_split(X_sel, y, test_size=0.2)
model = RandomForestClassifier().fit(X_tr, y_tr)
print(model.score(X_te, y_te))
```

(a) Temukan **dua** kebocoran data pada kode di atas.
(b) Untuk masing-masing, jelaskan **mekanismenya** — bagaimana informasi berpindah dari data uji ke proses pelatihan.
(c) Tuliskan ulang kode tersebut dengan benar memakai `Pipeline`.
(d) Apakah skor yang dilaporkan akan lebih tinggi atau lebih rendah daripada kinerja sebenarnya? Jelaskan.

**B2.** Sebuah rumah sakit ingin membangun model untuk memprediksi apakah pasien akan kembali dirawat dalam 30 hari setelah pulang. Data yang tersedia memuat kolom: usia, jenis kelamin, diagnosis, lama dirawat, jumlah obat saat pulang, **biaya perawatan lanjutan**, dan **jumlah kunjungan dokter setelah pulang**.

(a) Kapan prediksi dibutuhkan?
(b) Dua kolom mana yang **tidak boleh** dipakai sebagai fitur? Jelaskan alasannya.
(c) Jenis kebocoran apa yang akan terjadi bila kolom itu dipakai?
(d) Metrik apa yang sesuai untuk masalah ini? Kaitkan dengan dampak kesalahan.

**B3.** Sebuah tim melaporkan hasil berikut untuk model deteksi penipuan (proporsi penipuan 1,5%):

| Metrik | Nilai |
|--------|-------|
| Akurasi | 0,987 |
| Precision | 0,21 |
| Recall | 0,64 |

(a) Mengapa akurasi 0,987 **tidak** menunjukkan model yang baik di sini?
(b) Berapa akurasi model yang selalu menjawab "bukan penipuan"? Tunjukkan perhitungannya.
(c) Apa arti *precision* 0,21 bagi petugas yang harus memeriksa peringatan?
(d) Bila biaya melewatkan penipuan jauh lebih besar daripada biaya pemeriksaan sia-sia, ambang keputusan sebaiknya dinaikkan atau diturunkan? Jelaskan dampaknya pada *precision* dan *recall*.

**B4.** Sebuah data penjualan harian selama dua tahun dibagi dengan `train_test_split(X, y, test_size=0.2, random_state=42)`.

(a) Jenis kebocoran apa yang terjadi?
(b) Jelaskan mengapa ini menghasilkan taksiran kinerja yang terlalu optimistis.
(c) Tuliskan strategi pembagian yang benar.
(d) Gambarkan skema pembagian yang benar untuk lima lipatan.

### Bagian C — Perhitungan

**C1.** Sebuah model klasifikasi diuji pada 500 kasus dengan hasil:

```
                 PREDIKSI
             Negatif   Positif
  Negatif      410        40
  Positif       18        32
```

(a) Hitung akurasi, *precision*, *recall*, spesifisitas, dan F1. Tunjukkan langkahnya.
(b) Berapa proporsi kelas positif pada data uji?
(c) Berapa akurasi model yang selalu menjawab negatif?
(d) Berdasarkan (a)–(c), apakah model ini berguna? Jelaskan dalam dua kalimat.

**C2.** Sebuah model regresi memprediksi harga rumah (juta rupiah):

| Sebenarnya | 800 | 1.200 | 600 | 2.000 | 900 |
|------------|-----|-------|-----|-------|-----|
| Prediksi | 750 | 1.150 | 640 | 1.400 | 920 |

(a) Hitung MAE.
(b) Hitung RMSE.
(c) Hitung MAPE.
(d) Mengapa RMSE jauh lebih besar daripada MAE di sini? Pengamatan mana yang menyebabkannya?
(e) Bila kesalahan besar pada rumah mahal **sangat merugikan**, metrik mana yang sebaiknya dipakai untuk memilih model? Jelaskan.

**C3.** Sebuah eksperimen validasi silang 5 lipatan menghasilkan skor F1 berikut untuk dua model:

| | L1 | L2 | L3 | L4 | L5 |
|---|----|----|----|----|----|
| Model A | 0,72 | 0,75 | 0,71 | 0,74 | 0,73 |
| Model B | 0,60 | 0,88 | 0,65 | 0,91 | 0,71 |

(a) Hitung rerata dan simpangan baku sampel untuk masing-masing.
(b) Model mana yang reratanya lebih tinggi?
(c) Model mana yang sebaiknya dipilih? Jelaskan dengan memperhatikan simpangannya.
(d) Apa dugaan Anda tentang penyebab simpangan besar pada Model B, dan apa yang akan Anda periksa?

---

## 7. Persiapan yang Disarankan

| Kegiatan | Perkiraan waktu |
|----------|-----------------|
| Membaca ulang Bab 1–7 buku ajar | 5 jam |
| Mengerjakan Latihan Soal tingkat Menengah tiap bab | 4 jam |
| Mengerjakan contoh soal pada dokumen ini | 3 jam |
| Meninjau kembali praktikum yang sudah dikerjakan | 2 jam |
| **Berlatih perhitungan manual tanpa komputer** | **2 jam** |

Baris terakhir yang paling sering dilewati dan paling menentukan pada Bagian C.

---

## 8. Kaidah Penilaian

| Situasi | Penilaian |
|---------|-----------|
| Jawaban benar, langkah ditunjukkan | Nilai penuh |
| Langkah benar, hasil akhir salah karena kekeliruan hitung | Nilai sebagian besar |
| Hasil benar tanpa langkah | Nilai sebagian |
| Jawaban benar tanpa alasan pada soal yang meminta alasan | Nilai sebagian |
| Penalaran tepat, kesimpulan berbeda dari kunci tetapi konsisten | **Nilai penuh** |

> Baris terakhir berlaku khususnya pada Bagian B. Beberapa soal tidak memiliki satu jawaban benar; yang dinilai adalah ketepatan penalarannya.

---

## 9. Dokumen Terkait

1. [Modul Minggu 8 — tinjauan dan ujian](../03-modules/week-08-uts-review-dan-ujian.md)
2. [Kerangka asesmen](assessment-framework.md)
3. Bab 1–7 [buku ajar](../06-buku-ajar/00-halaman-depan.md)
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
