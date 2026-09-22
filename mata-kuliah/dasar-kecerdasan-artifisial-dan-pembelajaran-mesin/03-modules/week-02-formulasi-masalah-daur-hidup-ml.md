# Minggu 2: Formulasi Masalah dan Daur Hidup Pembelajaran Mesin

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 2 dari 16 |
| Topik | Dari masalah nyata ke *task* ML; *baseline*; daur hidup proyek ML |
| Sub-CPMK | `DAIML-Sub-CPMK082-1` · ICM-02 |
| Bloom | C4 (Menganalisis) → C6 (Merancang) |
| Durasi | 150 menit |
| Metode | Kuliah · Studi kasus · Latihan formulasi |
| Penilaian | Observasi (Lab 2) |

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Menganalisis** (C4) sebuah masalah nyata dan menentukan apakah ia dapat dirumuskan sebagai *task* pembelajaran mesin.
2. **Merumuskan** (C6) masalah menjadi spesifikasi *task* lengkap: target, fitur, jenis *task*, dan metrik.
3. **Memilih** (C5) metrik keberhasilan berdasarkan **dampak kesalahan**, bukan berdasarkan kebiasaan.
4. **Membangun** (P3) *baseline* dan menjelaskan mengapa ia wajib ada.
5. **Menjelaskan** (C2) tahapan daur hidup proyek ML dan mengapa ia berulang, bukan lurus.

---

## Materi Pembelajaran

### 2.1 Jurang antara Masalah dan *Task*

Masalah datang dalam bahasa organisasi. *Task* ML harus dinyatakan dalam bahasa data.

| Yang dikatakan pemangku kepentingan | Yang harus dirumuskan insinyur |
|-------------------------------------|--------------------------------|
| "Kami ingin mengurangi kredit macet." | Klasifikasi biner: memprediksi gagal bayar dalam 12 bulan dari data pengajuan. Metrik: *recall* pada kelas gagal bayar, dengan batas *precision* minimum. |
| "Kami ingin tahu pelanggan mana yang penting." | *Clustering* atas riwayat transaksi 12 bulan; atau klasifikasi *churn* bila definisi "penting" ternyata berarti "akan berhenti berlangganan". |
| "Sistemnya harus lebih pintar." | **Belum dapat dirumuskan.** Perlu dipertajam lebih dahulu. |

Baris ketiga adalah yang paling sering terjadi di lapangan. Menolak melanjutkan sebelum masalah dipertajam bukan sikap menyulitkan — ia mencegah pekerjaan berbulan-bulan yang tidak menjawab apa pun.

#### 2.1.1 Tujuh Pertanyaan Formulasi

Setiap proyek ML harus dapat menjawab tujuh pertanyaan ini **sebelum** satu baris kode ditulis:

| # | Pertanyaan | Contoh jawaban (kasus kelayakan kredit UMKM) |
|---|------------|----------------------------------------------|
| 1 | Keputusan apa yang akan diambil dari keluaran model? | Menyetujui, menolak, atau meneruskan ke penilai manusia |
| 2 | Apa **targetnya**, tepatnya? | Gagal bayar ≥ 90 hari dalam 12 bulan sejak pencairan |
| 3 | **Kapan** prediksi dibutuhkan? | Saat pengajuan — maka hanya data pada saat itu yang boleh dipakai |
| 4 | Fitur apa yang **tersedia pada saat itu**? | Data pengajuan, riwayat kredit, data usaha. **Bukan** data pembayaran yang belum terjadi |
| 5 | Apa **jenis kesalahan** yang lebih merugikan? | Menyetujui yang gagal bayar (kerugian) vs menolak yang layak (kehilangan nasabah dan berdampak sosial) |
| 6 | Apa **metrik** yang mencerminkan dampak itu? | *Recall* pada gagal bayar, dengan *precision* ≥ 0,4 |
| 7 | Apa **pembanding** yang harus dikalahkan? | Aturan penilaian manual yang berlaku saat ini |

> **Pertanyaan 3 dan 4 adalah pencegah kebocoran data yang paling ampuh.** Sebagian besar kebocoran yang dibahas Minggu 4 berasal dari kelalaian menjawab keduanya dengan jujur.

---

### 2.2 Menentukan Jenis *Task*

```
Apa bentuk keluaran yang dibutuhkan?
│
├── ANGKA pada skala kontinu
│   └──────────────────────────────► REGRESI
│                                     (harga, durasi, jumlah)
│
├── KATEGORI dari himpunan terbatas
│   ├── Dua kategori ──────────────► KLASIFIKASI BINER
│   ├── Lebih dari dua, saling
│   │   meniadakan ────────────────► KLASIFIKASI MULTIKELAS
│   └── Lebih dari satu label
│       sekaligus ─────────────────► KLASIFIKASI MULTILABEL
│
├── KELOMPOK tanpa contoh label
│   └──────────────────────────────► CLUSTERING
│
├── URUTAN prioritas
│   └──────────────────────────────► RANKING
│
└── PENANDAAN yang tak lazim
    └──────────────────────────────► DETEKSI ANOMALI
```

#### 2.2.1 Kekeliruan Umum dalam Penentuan Jenis

| Kekeliruan | Contoh | Perbaikan |
|------------|--------|-----------|
| Mengubah regresi menjadi klasifikasi tanpa alasan | "Harga rumah: murah/sedang/mahal" | Bila keputusan memerlukan angka, pertahankan regresi; pengelompokan membuang informasi |
| Klasifikasi multikelas untuk label yang tidak saling meniadakan | Satu artikel berita bisa "politik" dan "ekonomi" sekaligus | Gunakan multilabel |
| *Clustering* padahal label tersedia | Mengelompokkan padahal ada data berlabel | Gunakan klasifikasi — jauh lebih terarah |
| Klasifikasi untuk masalah *ranking* | "Produk relevan/tidak" padahal yang dibutuhkan urutan | Gunakan *ranking* |

---

### 2.3 Memilih Metrik Berdasarkan Dampak

Ini yang membedakan insinyur ML dari pengguna pustaka.

#### 2.3.1 Prinsipnya

> Metrik bukan dipilih dari kebiasaan. Metrik dipilih dari **jawaban atas pertanyaan: kesalahan jenis mana yang lebih merugikan, dan seberapa besar?**

| Kasus | Kesalahan yang lebih merugikan | Metrik yang sesuai |
|-------|-------------------------------|---------------------|
| Deteksi dini kanker | Melewatkan yang sakit (negatif palsu) | ***Recall* tinggi**; *precision* boleh lebih rendah |
| Penyaring spam | Membuang e-mail penting (positif palsu) | ***Precision* tinggi** |
| Deteksi penipuan kartu kredit | Keduanya mahal, tapi kelas sangat tak seimbang | **PR-AUC**; F1 pada kelas minoritas |
| Prediksi harga rumah | Kesalahan besar jauh lebih buruk | **RMSE** (menghukum galat besar) |
| Prediksi lama antrean puskesmas | Semua kesalahan setara | **MAE** (mudah ditafsirkan: "meleset 7 menit") |
| Estimasi anggaran proyek | Kesalahan relatif yang penting | **MAPE** |

#### 2.3.2 Mengapa Akurasi Sering Menyesatkan

Kasus: deteksi penipuan dengan 1.000 transaksi, 10 di antaranya penipuan.

```python
# Model yang selalu menjawab "bukan penipuan"
# Akurasi = 990/1000 = 99%
# Recall pada kelas penipuan = 0/10 = 0%
```

Akurasi 99% terdengar sangat baik. Modelnya **sama sekali tidak berguna** — ia tidak pernah menemukan satu pun penipuan.

> Inilah sebabnya pada mata kuliah ini, **melaporkan akurasi tanpa metrik lain pada data tak seimbang dikenai pengurangan nilai**. Pembahasan lengkapnya pada Minggu 7.

#### 2.3.3 Metrik Teknis vs Ukuran Dampak

| Metrik teknis | Ukuran dampak yang sebenarnya diinginkan |
|---------------|------------------------------------------|
| *Recall* 0,85 pada deteksi penipuan | Rupiah kerugian yang berhasil dicegah per bulan |
| MAE 7 menit pada prediksi antrean | Berkurangnya keluhan pasien |
| F1 0,72 pada penyaringan lamaran | Waktu penyaring manusia yang dihemat, dan keadilan hasilnya |

Keduanya harus dilaporkan. Metrik teknis untuk mengukur model; ukuran dampak untuk memutuskan apakah model layak dipakai.

---

### 2.4 *Baseline*: Pembanding yang Wajib Ada

#### 2.4.1 Mengapa Wajib

Angka kinerja tanpa pembanding tidak bermakna. "Akurasi 78%" bisa berarti sangat baik atau sangat buruk, bergantung pada berapa yang dicapai tanpa model sama sekali.

| Jenis *baseline* | Cara | Kapan dipakai |
|------------------|------|---------------|
| **Kelas terbanyak** | Selalu menjawab kelas yang paling sering | Klasifikasi |
| **Rata-rata/median** | Selalu menjawab nilai tengah | Regresi |
| **Acak berbobot** | Menjawab sesuai proporsi kelas | Klasifikasi |
| **Aturan sederhana** | `if-else` yang masuk akal | Selalu, bila memungkinkan |
| **Sistem yang berlaku saat ini** | Kinerja proses manual yang sedang dipakai | **Yang paling bermakna** |

```python
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.metrics import accuracy_score, mean_absolute_error

# Baseline klasifikasi: selalu memilih kelas terbanyak
dummy_clf = DummyClassifier(strategy="most_frequent", random_state=42)
dummy_clf.fit(X_train, y_train)
print("Baseline akurasi:", accuracy_score(y_test, dummy_clf.predict(X_test)))

# Baseline regresi: selalu menjawab median
dummy_reg = DummyRegressor(strategy="median")
dummy_reg.fit(X_train, y_train)
print("Baseline MAE:", mean_absolute_error(y_test, dummy_reg.predict(X_test)))
```

> **Aturan mata kuliah ini:** setiap laporan kinerja model **wajib** menyertakan skor *baseline* pada metrik yang sama. Model yang tidak mengungguli *baseline* bukan kegagalan yang memalukan — ia adalah temuan yang sah dan wajib dilaporkan apa adanya.

#### 2.4.2 Membaca Selisih terhadap *Baseline*

| Selisih | Tafsir |
|---------|--------|
| Model < *baseline* | Ada yang salah: fitur tidak informatif, target salah dirumuskan, atau data terlalu sedikit |
| Model ≈ *baseline* | Fitur yang tersedia tidak memuat sinyal untuk target ini |
| Model > *baseline* sedikit | Ada sinyal, tetapi lemah. Perlu dipertimbangkan apakah sepadan dengan biaya pemeliharaan |
| Model ≫ *baseline* | **Periksa kebocoran data lebih dahulu** sebelum merayakan |

Baris terakhir adalah nasihat yang paling sering diabaikan dan paling sering menyelamatkan.

---

### 2.5 Daur Hidup Proyek Pembelajaran Mesin

```
      ┌──────────────────────────────────────────────────────┐
      │                                                      │
      ▼                                                      │
┌─────────────┐   ┌─────────────┐   ┌─────────────┐          │
│ 1. FORMULASI│──►│ 2. DATA     │──►│ 3. EKSPLORASI│         │
│    MASALAH  │   │             │   │    & SIAPKAN │         │
└─────────────┘   └─────────────┘   └─────────────┘          │
      ▲                  ▲                  │                │
      │                  │                  ▼                │
      │                  │           ┌─────────────┐         │
      │                  └───────────│ 4. BASELINE │         │
      │                              │  & MODEL    │         │
      │                              └─────────────┘         │
      │                                     │                │
      │                                     ▼                │
      │                              ┌─────────────┐         │
      │                              │ 5. EVALUASI │         │
      │                              │  & ANALISIS │─────────┘
      │                              │   KESALAHAN │
      │                              └─────────────┘
      │                                     │
      │                                     ▼
      │                              ┌─────────────┐
      └──────────────────────────────│ 6. TERAPKAN │
          bila kinerja menurun       │  & PANTAU   │
                                     └─────────────┘
```

#### 2.5.1 Porsi Waktu yang Sebenarnya

| Tahap | Perkiraan mahasiswa | Kenyataan di lapangan |
|-------|---------------------|-----------------------|
| Formulasi masalah | 5% | **15%** |
| Pengumpulan dan penyiapan data | 15% | **45%** |
| Pemodelan | **60%** | 15% |
| Evaluasi dan analisis kesalahan | 10% | 15% |
| Penerapan dan pemantauan | 10% | 10% |

Kebalikan dari harapan kebanyakan orang. Mata kuliah ini mengikuti proporsi kenyataan: **tiga minggu penuh (3–5) dihabiskan untuk data sebelum satu model pun dilatih**.

#### 2.5.2 Mengapa Daur Ini Berulang

| Pemicu kembali ke tahap sebelumnya | Contoh |
|------------------------------------|--------|
| Evaluasi menunjukkan fitur kurang informatif | Kembali ke tahap 3 |
| Analisis kesalahan menunjukkan target salah dirumuskan | Kembali ke tahap 1 |
| Kinerja menurun setelah diterapkan (*drift*) | Kembali ke tahap 2 |
| Data ternyata tidak mencakup kelompok tertentu | Kembali ke tahap 2 |

Proyek ML yang berjalan lurus dari tahap 1 ke 6 tanpa pernah mundur hampir selalu berarti ada tahap yang dikerjakan asal-asalan.

---

### 2.6 Studi Kasus: Prediksi Keterlambatan Pengiriman

**Masalah yang disampaikan:** *"Pelanggan sering mengeluh paket telat. Bisakah kita prediksi?"*

**Formulasi lengkap:**

| Pertanyaan | Jawaban |
|------------|---------|
| Keputusan apa? | Menampilkan estimasi tiba yang realistis; memprioritaskan paket berisiko |
| Target | Terlambat = tiba > estimasi awal + 1 hari |
| Jenis *task* | Klasifikasi biner (bisa juga regresi selisih hari — dua pilihan yang sah) |
| Kapan prediksi dibutuhkan | **Saat paket diterima gudang asal** |
| Fitur yang tersedia saat itu | Asal, tujuan, berat, jenis layanan, hari dalam minggu, musim, riwayat kinerja rute |
| Fitur yang **tidak boleh** dipakai | Waktu tiba sebenarnya, status perjalanan setelah itu, keluhan pelanggan |
| Kesalahan yang lebih merugikan | Mengatakan tepat waktu padahal telat (kekecewaan pelanggan) |
| Metrik | *Recall* pada kelas terlambat, dengan *precision* ≥ 0,5 |
| *Baseline* | Aturan yang berlaku: "rute X biasanya 3 hari" |

> **Perhatikan baris "fitur yang tidak boleh dipakai".** Memasukkan status perjalanan akan menghasilkan akurasi mendekati sempurna — dan model yang sama sekali tidak dapat dipakai, karena pada saat prediksi dibutuhkan, informasi itu belum ada. Ini adalah **kebocoran temporal**, bahasan utama Minggu 4.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 2 buku ajar](../06-buku-ajar/bab-02-formulasi-masalah-daur-hidup-ml.md).
- Menyiapkan satu masalah nyata dari lingkungan sendiri (kampus, keluarga, tempat kerja) yang diduga dapat diselesaikan dengan ML.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | Tinjauan Minggu 1; pembahasan T-01 |
| Konsep | 40' | Tujuh pertanyaan formulasi; penentuan jenis *task* |
| Latihan | 30' | **Kegiatan inti:** berpasangan, merumuskan tiga masalah menjadi spesifikasi lengkap |
| Konsep | 25' | Pemilihan metrik berdasarkan dampak; *baseline* |
| Demonstrasi | 30' | Membangun *baseline* dengan `DummyClassifier`; membaca selisihnya |
| Penutup | 15' | Daur hidup ML; penugasan |

**Tiga masalah untuk latihan formulasi:**

1. Sebuah puskesmas ingin mengurangi waktu tunggu pasien.
2. Sebuah koperasi simpan pinjam ingin menurunkan angka kredit macet.
3. Sebuah kampus ingin mengenali mahasiswa yang berisiko putus kuliah.

Untuk masing-masing, tentukan: target tepatnya, kapan prediksi dibutuhkan, fitur yang boleh dan tidak boleh dipakai, kesalahan yang lebih merugikan, metrik, dan *baseline*.

> Nomor 3 memuat persoalan etis yang dibahas singkat: apa yang akan dilakukan kampus dengan daftar mahasiswa berisiko? Bila jawabannya "membantu", model berguna. Bila jawabannya "mencoret dari beasiswa", model merugikan orang yang justru paling membutuhkan. Pembahasan ini diulang lebih dalam pada Minggu 14.

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 2](../04-labs/lab-02-formulasi-masalah-baseline.md).
- Mulai memikirkan tema proyek kelompok (proposal jatuh tempo Minggu 5).

---

## Penugasan

**T-02 — Formulasi Masalah dan *Baseline***

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Dokumen formulasi (1 halaman) + notebook *baseline* |
| Isi | (a) Formulasi lengkap satu masalah dengan tujuh pertanyaan §2.1.1; (b) Metrik beserta alasan pemilihannya dikaitkan dengan dampak kesalahan; (c) *Baseline* yang dibangun dan skornya; (d) Daftar fitur yang **tidak boleh** dipakai beserta alasannya |
| Tenggat | Awal pertemuan Minggu 3 |
| Bobot | 1,9% (Observasi) |

---

## Rangkuman

1. Masalah organisasi harus **diterjemahkan** menjadi *task* ML; sebagian masalah tidak dapat diterjemahkan dan harus dipertajam lebih dahulu.
2. **Tujuh pertanyaan formulasi** wajib terjawab sebelum kode ditulis.
3. Pertanyaan "**kapan prediksi dibutuhkan**" dan "**fitur apa yang tersedia saat itu**" adalah pencegah kebocoran paling ampuh.
4. Jenis *task* ditentukan oleh **bentuk keluaran yang dibutuhkan**, bukan oleh algoritma yang ingin dicoba.
5. **Metrik dipilih dari dampak kesalahan**, bukan dari kebiasaan. Akurasi pada data tak seimbang menyesatkan.
6. Metrik teknis dan ukuran dampak keduanya harus dilaporkan.
7. ***Baseline* wajib ada.** Angka kinerja tanpa pembanding tidak bermakna.
8. Model yang jauh mengungguli *baseline* harus **diperiksa kebocorannya lebih dahulu**.
9. Daur hidup ML **berulang**, bukan lurus; 45% waktu nyata dihabiskan untuk data.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 2. O'Reilly.
2. Huyen, C. (2022). *Designing Machine Learning Systems*, Bab 2–3. O'Reilly.
3. Müller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*, Bab 1. O'Reilly.
4. Sculley, D., et al. (2015). Hidden Technical Debt in Machine Learning Systems. *NeurIPS*.
5. Dokumentasi scikit-learn — *Dummy estimators*. <https://scikit-learn.org/stable/modules/model_evaluation.html#dummy-estimators>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
