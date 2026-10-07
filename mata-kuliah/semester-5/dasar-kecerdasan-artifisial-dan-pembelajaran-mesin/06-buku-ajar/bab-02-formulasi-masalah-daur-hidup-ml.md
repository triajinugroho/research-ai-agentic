# BAB 2: FORMULASI MASALAH DAN DAUR HIDUP PEMBELAJARAN MESIN

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK082-1` | Merumuskan masalah nyata menjadi spesifikasi *task* ML yang lengkap | C6 |
| `DAIML-Sub-CPMK082-1` | Memilih metrik keberhasilan berdasarkan dampak kesalahan | C5 |
| `DAIML-Sub-CPMK082-1` | Membangun *baseline* dan menafsirkan selisih terhadapnya | C3–C4 |

---

## 2.1 Jurang antara Masalah dan *Task*

Masalah datang dalam bahasa organisasi. *Task* pembelajaran mesin harus dinyatakan dalam bahasa data.

| Yang dikatakan pemangku kepentingan | Yang harus dirumuskan insinyur |
|-------------------------------------|--------------------------------|
| "Kami ingin mengurangi kredit macet." | Klasifikasi biner: memprediksi gagal bayar ≥ 90 hari dalam 12 bulan, dari data yang tersedia **saat pengajuan**. Metrik: *recall* pada kelas gagal bayar dengan batas *precision* minimum. |
| "Kami ingin tahu pelanggan mana yang penting." | Bergantung pada arti "penting". Bila "akan berhenti berlangganan" → klasifikasi *churn*. Bila "punya pola belanja serupa" → *clustering*. **Harus ditanyakan lebih dahulu.** |
| "Sistemnya harus lebih pintar." | **Belum dapat dirumuskan.** Perlu dipertajam. |

Baris ketiga adalah yang paling sering terjadi. Menolak melanjutkan sebelum masalah dipertajam bukan sikap menyulitkan — ia mencegah pekerjaan berbulan-bulan yang tidak menjawab apa pun.

### 2.1.1 Tujuh Pertanyaan Formulasi

Setiap proyek harus dapat menjawab tujuh pertanyaan ini **sebelum satu baris kode ditulis**.

| # | Pertanyaan | Contoh (kelayakan kredit UMKM) |
|---|------------|--------------------------------|
| 1 | Keputusan apa yang diambil dari keluaran model? | Menyetujui, menolak, atau meneruskan ke penilai manusia |
| 2 | Apa **targetnya**, tepatnya? | Menunggak ≥ 90 hari dalam 12 bulan sejak pencairan |
| 3 | **Kapan** prediksi dibutuhkan? | Saat pengajuan diterima |
| 4 | Fitur apa yang **tersedia pada saat itu**? | Data pengajuan, riwayat kredit sebelumnya, data usaha. **Bukan** riwayat pembayaran yang belum terjadi |
| 5 | **Jenis kesalahan mana** yang lebih merugikan? | Menyetujui yang gagal bayar (kerugian finansial) vs menolak yang layak (kehilangan nasabah; dampak sosial pada pelaku UMKM) |
| 6 | Apa **metrik** yang mencerminkan dampak itu? | *Recall* pada gagal bayar, dengan *precision* ≥ 0,4 |
| 7 | Apa **pembanding** yang harus dikalahkan? | Aturan penilaian manual yang berlaku saat ini |

> **Pertanyaan 3 dan 4 adalah pencegah kebocoran data yang paling ampuh.** Sebagian besar kebocoran yang dibahas Bab 4 berasal dari kelalaian menjawab keduanya dengan jujur.

### 2.1.2 Ketepatan pada Pertanyaan Kedua

"Gagal bayar" bukan target. Ia adalah tema. Target yang dapat dipelajari harus menyebutkan:

| Unsur | Contoh |
|-------|--------|
| Peristiwanya | Menunggak angsuran |
| Ambangnya | ≥ 90 hari |
| Jendela waktunya | Dalam 12 bulan |
| Titik awalnya | Sejak pencairan |

Tanpa keempat unsur itu, dua anggota tim yang sama dapat memberi label yang berbeda pada baris yang sama — dan model yang dilatih darinya mempelajari ketidakkonsistenan itu.

---

## 2.2 Menentukan Jenis *Task*

```
Apa bentuk keluaran yang dibutuhkan?
│
├── ANGKA pada skala kontinu ────────────► REGRESI
│
├── KATEGORI dari himpunan terbatas
│   ├── Dua kategori ────────────────────► KLASIFIKASI BINER
│   ├── Lebih dari dua, saling meniadakan ► KLASIFIKASI MULTIKELAS
│   └── Lebih dari satu label sekaligus ──► KLASIFIKASI MULTILABEL
│
├── KELOMPOK tanpa contoh label ─────────► CLUSTERING
├── URUTAN prioritas ────────────────────► RANKING
└── PENANDAAN yang tak lazim ────────────► DETEKSI ANOMALI
```

### 2.2.1 Empat Kekeliruan Umum

| Kekeliruan | Contoh | Perbaikan |
|------------|--------|-----------|
| Mengubah regresi menjadi klasifikasi tanpa alasan | "Harga rumah: murah/sedang/mahal" | Bila keputusan memerlukan angka, pertahankan regresi — pengelompokan membuang informasi |
| Multikelas untuk label yang tidak saling meniadakan | Satu berita bisa "politik" **dan** "ekonomi" | Gunakan multilabel |
| *Clustering* padahal label tersedia | Mengelompokkan padahal ada data berlabel | Gunakan klasifikasi — jauh lebih terarah |
| Klasifikasi untuk masalah *ranking* | "Relevan/tidak" padahal yang dibutuhkan urutan | Gunakan *ranking* |

---

## 2.3 Memilih Metrik dari Dampak Kesalahan

Ini yang membedakan insinyur ML dari pengguna pustaka.

### 2.3.1 Prinsipnya

> Metrik tidak dipilih dari kebiasaan. Metrik dipilih dari jawaban atas pertanyaan: **kesalahan jenis mana yang lebih merugikan, dan seberapa besar?**

| Kasus | Kesalahan yang lebih merugikan | Metrik yang sesuai |
|-------|-------------------------------|---------------------|
| Deteksi dini penyakit | Melewatkan yang sakit | ***Recall* tinggi** |
| Penyaring spam | Membuang surel penting | ***Precision* tinggi** |
| Deteksi penipuan (kelas 1%) | Keduanya mahal; kelas sangat timpang | **PR-AUC**; F1 kelas minoritas |
| Perkiraan harga properti | Kesalahan besar jauh lebih buruk | **RMSE** |
| Perkiraan lama antrean | Semua kesalahan setara | **MAE** — mudah ditafsirkan |
| Estimasi anggaran | Kesalahan relatif yang penting | **MAPE** |

### 2.3.2 Mengapa Akurasi Sering Menyesatkan

Deteksi penipuan: 1.000 transaksi, 10 penipuan.

```python
# Model yang SELALU menjawab "bukan penipuan"
# Akurasi = 990/1000 = 99,0%   <- tampak hebat
# Recall pada kelas penipuan = 0/10 = 0%   <- tidak berguna sama sekali
```

Model ini tidak menemukan satu pun penipuan, dan akurasinya lebih tinggi daripada model yang sebenarnya bekerja.

> **Karena itu, pada mata kuliah ini, melaporkan akurasi sebagai satu-satunya metrik pada data tak seimbang dikenai pengurangan nilai.** Bukan karena akurasi terlarang, melainkan karena ia sendirian tidak memberi informasi yang dibutuhkan.

### 2.3.3 Metrik Teknis dan Ukuran Dampak

| Metrik teknis | Ukuran dampak yang sebenarnya diinginkan |
|---------------|------------------------------------------|
| *Recall* 0,85 pada deteksi penipuan | Rupiah kerugian yang berhasil dicegah per bulan |
| MAE 7 menit pada perkiraan antrean | Berkurangnya keluhan pasien |
| F1 0,72 pada penyaringan lamaran | Waktu penyaring manusia yang dihemat, **dan keadilan hasilnya** |

Keduanya harus dilaporkan. Metrik teknis untuk mengukur model; ukuran dampak untuk memutuskan apakah model **layak dipakai**.

---

## 2.4 *Baseline*: Pembanding yang Wajib

### 2.4.1 Mengapa Wajib

"Akurasi 78%" tidak bermakna apa pun sendirian. Ia bisa berarti sangat baik atau lebih buruk daripada menebak, bergantung pada berapa yang dicapai **tanpa model sama sekali**.

| Jenis *baseline* | Cara | Kapan dipakai |
|------------------|------|---------------|
| Kelas terbanyak | Selalu menjawab kelas paling sering | Klasifikasi |
| Rata-rata/median | Selalu menjawab nilai tengah | Regresi |
| Acak berbobot | Menjawab sesuai proporsi kelas | Klasifikasi |
| Aturan sederhana | `if-else` yang masuk akal | Selalu, bila memungkinkan |
| **Sistem yang berlaku saat ini** | Kinerja proses manual yang sedang dipakai | **Yang paling bermakna** |

```python
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.metrics import f1_score, mean_absolute_error

dummy_clf = DummyClassifier(strategy="most_frequent", random_state=42)
dummy_clf.fit(X_train, y_train)
print("Baseline F1 :", f1_score(y_test, dummy_clf.predict(X_test), zero_division=0))

dummy_reg = DummyRegressor(strategy="median")
dummy_reg.fit(X_train, y_train)
print("Baseline MAE:", mean_absolute_error(y_test, dummy_reg.predict(X_test)))
```

### 2.4.2 Membaca Selisih terhadap *Baseline*

| Selisih | Tafsir | Tindakan |
|---------|--------|----------|
| Model < *baseline* | Ada yang salah: fitur tidak informatif, target keliru dirumuskan, atau data terlalu sedikit | Kembali ke formulasi |
| Model ≈ *baseline* | Fitur yang tersedia tidak memuat sinyal untuk target ini | Cari fitur lain; atau nyatakan temuan ini |
| Model > *baseline* sedikit | Ada sinyal, tetapi lemah | Pertimbangkan apakah sepadan dengan biaya pemeliharaan |
| Model ≫ *baseline* | **Periksa kebocoran data lebih dahulu** | Jangan merayakan sebelum memeriksa |

Baris terakhir adalah nasihat yang paling sering diabaikan dan paling sering menyelamatkan.

---

## 2.5 Daur Hidup Proyek Pembelajaran Mesin

```
      ┌──────────────────────────────────────────────────────┐
      ▼                                                      │
┌─────────────┐   ┌─────────────┐   ┌──────────────┐         │
│ 1. FORMULASI│──►│ 2. DATA     │──►│ 3. EKSPLORASI│         │
│    MASALAH  │   │             │   │    & SIAPKAN │         │
└─────────────┘   └─────────────┘   └──────────────┘         │
      ▲                  ▲                  │                │
      │                  │                  ▼                │
      │                  │           ┌─────────────┐         │
      │                  └───────────│ 4. BASELINE │         │
      │                              │  & MODEL    │         │
      │                              └─────────────┘         │
      │                                     │                │
      │                                     ▼                │
      │                              ┌─────────────┐         │
      │                              │ 5. EVALUASI │─────────┘
      │                              │ & ANALISIS  │
      │                              │  KESALAHAN  │
      │                              └─────────────┘
      │                                     │
      │                                     ▼
      │                              ┌─────────────┐
      └──────────────────────────────│ 6. TERAPKAN │
          bila kinerja menurun       │  & PANTAU   │
                                     └─────────────┘
```

### 2.5.1 Porsi Waktu yang Sebenarnya

| Tahap | Perkiraan pemula | Kenyataan di lapangan |
|-------|------------------|-----------------------|
| Formulasi masalah | 5% | **15%** |
| Pengumpulan dan penyiapan data | 15% | **45%** |
| Pemodelan | **60%** | 15% |
| Evaluasi dan analisis kesalahan | 10% | 15% |
| Penerapan dan pemantauan | 10% | 10% |

Buku ini mengikuti proporsi kenyataan: **tiga bab penuh (3–5) dicurahkan untuk data sebelum satu model pun dilatih**.

### 2.5.2 Mengapa Daur Ini Berulang

| Pemicu kembali | Contoh |
|----------------|--------|
| Evaluasi menunjukkan fitur kurang informatif | Kembali ke tahap 3 |
| Analisis kesalahan menunjukkan target salah dirumuskan | Kembali ke tahap 1 |
| Kinerja menurun setelah diterapkan (*drift*) | Kembali ke tahap 2 |
| Data ternyata tidak mencakup kelompok tertentu | Kembali ke tahap 2 |

Proyek yang berjalan lurus dari tahap 1 ke 6 tanpa pernah mundur hampir selalu berarti ada tahap yang dikerjakan asal-asalan.

---

## 2.6 Studi Kasus: Prediksi Keterlambatan Pengiriman

**Masalah yang disampaikan:** *"Pelanggan sering mengeluh paket telat. Bisakah kita prediksi?"*

| Pertanyaan | Jawaban |
|------------|---------|
| Keputusan apa | Menampilkan estimasi tiba yang realistis; memprioritaskan paket berisiko |
| Target | Terlambat = tiba > estimasi awal + 1 hari |
| Jenis *task* | Klasifikasi biner (alternatif sah: regresi selisih hari) |
| Kapan dibutuhkan | **Saat paket diterima gudang asal** |
| Fitur yang tersedia saat itu | Asal, tujuan, berat, jenis layanan, hari, musim, riwayat kinerja rute |
| **Fitur yang tidak boleh** | Waktu tiba sebenarnya; status perjalanan berikutnya; keluhan pelanggan |
| Kesalahan yang lebih merugikan | Mengatakan tepat waktu padahal telat |
| Metrik | *Recall* pada kelas terlambat, dengan *precision* ≥ 0,5 |
| *Baseline* | Aturan yang berlaku: "rute X biasanya 3 hari" |

> **Perhatikan baris "fitur yang tidak boleh".** Memasukkan status perjalanan akan menghasilkan akurasi mendekati sempurna — dan model yang sama sekali tidak dapat dipakai, karena informasi itu belum ada saat prediksi dibutuhkan. Ini adalah **kebocoran temporal**, bahasan utama Bab 4.

---

## AI Corner — Tahap *Understand*

### Mengapa Formulasi Tidak Boleh Diserahkan kepada AI

Diminta merumuskan masalah menjadi *task* ML, model bahasa akan menghasilkan jawaban yang tampak rapi dan lengkap. Masalahnya terletak pada apa yang **tidak** diketahuinya:

| Yang tidak diketahui AI | Akibatnya pada formulasi |
|-------------------------|--------------------------|
| Kapan data setiap kolom benar-benar tersedia | Fitur yang bocor akan disarankan sebagai fitur |
| Bagaimana kolom itu didefinisikan penerbitnya | Target dapat dirumuskan atas dasar yang keliru |
| Apa konsekuensi nyata tiap jenis kesalahan | Metrik dipilih dari kebiasaan, bukan dari dampak |
| Siapa yang akan memakai keluarannya dan bagaimana | *Task* dapat tidak menjawab kebutuhan sebenarnya |

Keempat butir itu persis merupakan pertanyaan 2–6 pada §2.1.1.

### Cara Memakai AI yang Menguatkan

Perbedaannya terletak pada **urutan**:

| Melemahkan | Menguatkan |
|------------|------------|
| "Rumuskan masalah ini sebagai *task* ML." | "Saya merumuskannya begini: [formulasi sendiri]. Adakah fitur yang saya sebut yang berisiko bocor?" |
| "Metrik apa yang harus saya pakai?" | "Saya memilih *recall* karena melewatkan kasus positif berbiaya 100× lebih besar. Apa kelemahan pilihan ini?" |
| "Buatkan daftar fitur." | "Ini daftar fitur saya. Untuk masing-masing, apakah pertanyaan 'tersedia saat prediksi dibutuhkan?' sudah saya jawab dengan benar?" |

Pola kolom kanan mempertahankan mahasiswa sebagai pengambil keputusan dan menempatkan AI sebagai **pemeriksa**. Pola kolom kiri memindahkan penalaran keluar dari kepala mahasiswa — dan penalaran itulah yang diuji pada UAS, tanpa bantuan apa pun.

---

## Latihan Soal

### Tingkat Dasar

1. Ubah tiga tema berikut menjadi formulasi *task* ML lengkap dengan target yang tepat (empat unsur §2.1.2):
   (a) Mengurangi angka putus sekolah.
   (b) Memperbaiki layanan puskesmas.
   (c) Menurunkan tingkat pengembalian barang di toko daring.

2. Tentukan jenis *task* untuk masing-masing:
   (a) Memperkirakan IPM kabupaten dari indikator sosial-ekonomi.
   (b) Menentukan apakah sebuah ulasan produk bernada positif, netral, atau negatif.
   (c) Menandai artikel berita dengan semua topik yang relevan.
   (d) Mengurutkan produk berdasarkan kemungkinan dibeli.

3. Untuk masing-masing kasus, tentukan metrik yang sesuai beserta alasannya:
   (a) Deteksi dini gizi buruk pada balita.
   (b) Penyaringan otomatis lamaran kerja.
   (c) Perkiraan kebutuhan stok obat puskesmas.

4. Jelaskan dalam dua kalimat mengapa *baseline* wajib disertakan dalam setiap laporan kinerja model.

### Tingkat Menengah

5. Sebuah kampus ingin membangun model untuk mengenali mahasiswa berisiko putus kuliah, dengan data akademik semester 1–4.
   (a) Rumuskan target dengan empat unsur §2.1.2.
   (b) Kapan prediksi dibutuhkan agar berguna?
   (c) Sebutkan tiga fitur yang **tidak boleh** dipakai beserta alasannya.
   (d) Apa yang akan dilakukan kampus dengan daftar mahasiswa berisiko? Bagaimana jawaban itu memengaruhi pemilihan metrik?

6. Sebuah tim melaporkan akurasi 0,94 pada model deteksi kanker dengan proporsi kasus positif 4%.
   (a) Berapa akurasi model yang selalu menjawab "tidak kanker"?
   (b) Apakah 0,94 menunjukkan model yang baik? Jelaskan.
   (c) Metrik apa yang seharusnya dilaporkan, dan mengapa?
   (d) Apa yang harus ditanyakan kepada tim itu sebelum hasilnya dipercaya?

7. Sebuah model memperoleh F1 0,91 sementara *baseline* kelas terbanyak memperoleh F1 0,88.
   (a) Apakah model ini berguna? Jelaskan pertimbangannya.
   (b) Informasi apa yang masih dibutuhkan untuk memutuskan?
   (c) Biaya apa yang harus diperhitungkan sebelum menerapkan model ini?
   (d) Apa yang akan Anda sarankan?

8. Sebuah model memperoleh ROC-AUC 0,995 pada masalah prediksi *churn* pelanggan.
   (a) Apa reaksi pertama Anda?
   (b) Sebutkan tiga hal yang akan Anda periksa.
   (c) Fitur seperti apa yang paling mungkin menjadi penyebabnya?
   (d) Bagaimana cara memastikannya?

### Tingkat Mahir

9. Susun formulasi lengkap untuk sebuah masalah nyata.
   (a) Pilih satu masalah dari lingkungan Anda sendiri.
   (b) Jawab ketujuh pertanyaan §2.1.1 secara lengkap.
   (c) Tentukan target dengan keempat unsur §2.1.2.
   (d) Susun daftar fitur yang boleh dan tidak boleh, masing-masing dengan alasannya.
   (e) Tetapkan **ambang keberhasilan** sebelum melihat data apa pun.
   (f) Rancang *baseline* yang paling bermakna untuk masalah itu.

10. Bandingkan dua formulasi untuk masalah yang sama.
    (a) Ambil masalah "mengurangi kemacetan di satu ruas jalan".
    (b) Rumuskan sebagai masalah **regresi** (memperkirakan kepadatan).
    (c) Rumuskan sebagai masalah **klasifikasi** (macet/tidak).
    (d) Untuk masing-masing: metrik apa, dan siapa yang memakai keluarannya?
    (e) Formulasi mana yang lebih berguna, dan dalam keadaan apa yang lain lebih baik?

11. Lakukan audit formulasi atas sebuah proyek ML yang dipublikasikan (makalah, laporan lembaga, atau *notebook* publik).
    (a) Apakah ketujuh pertanyaan §2.1.1 terjawab dari dokumennya?
    (b) Apakah *baseline* disertakan?
    (c) Apakah metrik dipilih dengan alasan yang dinyatakan?
    (d) Adakah fitur yang Anda curigai bocor? Jelaskan dasarnya.
    (e) Tuliskan tiga pertanyaan yang akan Anda ajukan kepada penulisnya.

---

## Rangkuman

1. Masalah organisasi harus **diterjemahkan** menjadi *task* ML; sebagian tidak dapat diterjemahkan dan harus dipertajam lebih dahulu.
2. **Tujuh pertanyaan formulasi** wajib terjawab sebelum kode ditulis.
3. Target harus menyebutkan **peristiwa, ambang, jendela waktu, dan titik awal**.
4. **Pertanyaan 3 dan 4** — kapan prediksi dibutuhkan, dan apa yang tersedia saat itu — adalah pencegah kebocoran paling ampuh.
5. Jenis *task* ditentukan oleh **bentuk keluaran yang dibutuhkan**, bukan oleh algoritma yang ingin dicoba.
6. **Metrik dipilih dari dampak kesalahan.** Akurasi pada data tak seimbang menyesatkan.
7. Metrik teknis **dan** ukuran dampak keduanya harus dilaporkan.
8. ***Baseline* wajib.** Angka kinerja tanpa pembanding tidak bermakna.
9. Model yang jauh mengungguli *baseline* harus **diperiksa kebocorannya lebih dahulu**.
10. Daur hidup ML **berulang**, bukan lurus; 45% waktu nyata dihabiskan untuk data.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 2. O'Reilly.
2. Huyen, C. (2022). *Designing Machine Learning Systems*, Bab 2–3. O'Reilly.
3. Müller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*, Bab 1. O'Reilly.
4. Sculley, D., et al. (2015). Hidden Technical Debt in Machine Learning Systems. *NeurIPS*.
5. Dokumentasi scikit-learn — *Dummy estimators*. <https://scikit-learn.org/stable/modules/model_evaluation.html#dummy-estimators>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
