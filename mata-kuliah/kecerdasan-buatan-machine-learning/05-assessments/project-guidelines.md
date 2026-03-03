# Panduan Proyek Akhir

## Mata Kuliah: Kecerdasan Buatan dan Machine Learning (IF3XXX, 4 SKS)
### Prodi Informatika — UAI — Semester Ganjil 2026/2027
### Dosen Pengampu: Tri Aji Nugroho, S.T., M.T.

---

## 1. Deskripsi Proyek

Proyek akhir merupakan kulminasi dari seluruh pembelajaran selama semester. Kelompok mahasiswa (2-3 orang) membangun **end-to-end ML pipeline** pada dataset riil Indonesia, menggunakan teknik machine learning yang telah dipelajari, dengan **AI sebagai partner yang didokumentasikan**.

Proyek ini menguji kemampuan mahasiswa untuk:
- Merumuskan problem statement dengan business value yang jelas
- Melakukan eksplorasi data dan feature engineering secara komprehensif
- Membandingkan minimal 3 algoritma ML yang berbeda
- Mengevaluasi dan memilih model terbaik dengan metrik yang tepat
- Menginterpretasi hasil secara kritis dan memberikan rekomendasi
- Berkolaborasi dengan AI secara bertanggung jawab
- Mengkomunikasikan temuan secara efektif

**Bobot:** 25% dari nilai akhir

---

## 2. Persyaratan Proyek

### 2.1 Dataset

| Kriteria | Persyaratan |
|----------|-------------|
| **Sumber** | Dataset publik Indonesia (BPS, Open Data, Kaggle Indonesia, dll.) |
| **Ukuran minimum** | 500 baris (rows) |
| **Variabel** | Minimal 5 fitur (kolom) |
| **Konteks** | Harus relevan dengan Indonesia atau konteks lokal |

### 2.2 Komponen Wajib

Setiap proyek harus mencakup komponen berikut:

1. **Problem Statement dengan Business Value**
   - Pertanyaan penelitian yang jelas dan spesifik
   - Mengapa masalah ini penting? Siapa yang diuntungkan?
   - Bagaimana ML bisa membantu menyelesaikan masalah ini?

2. **Eksplorasi Data (EDA)**
   - Statistik deskriptif lengkap
   - Minimal 5 visualisasi bermakna
   - Identifikasi dan penanganan missing values
   - Identifikasi dan penanganan outliers
   - Analisis distribusi dan korelasi antar fitur

3. **Feature Engineering**
   - Encoding variabel kategorikal
   - Scaling/normalisasi fitur numerik
   - Feature selection atau creation jika relevan
   - Train-test split (atau cross-validation)

4. **Modeling: Minimal 3 Algoritma Berbeda**
   - Minimal 3 model ML yang berbeda harus dibandingkan
   - Justifikasi pemilihan setiap algoritma
   - Hyperparameter tuning pada model terbaik
   - Contoh kombinasi: KNN + Random Forest + SVM, atau Decision Tree + Gradient Boosting + Neural Network

5. **Evaluasi dan Seleksi Model**
   - Metrik evaluasi yang tepat (accuracy, precision, recall, F1, AUC, dll.)
   - Perbandingan performa antar model dalam tabel/chart
   - Analisis confusion matrix untuk model terbaik
   - Cross-validation untuk validasi yang robust

6. **Kesimpulan dan Rekomendasi**
   - Ringkasan temuan utama
   - Rekomendasi model terbaik dan alasannya
   - Limitasi analisis
   - Saran untuk pengembangan selanjutnya

---

## 3. Timeline & Milestones

| Minggu | Milestone | Deliverable | Bobot |
|--------|-----------|-------------|-------|
| 9 | **Proposal Submission** | Proposal (1-2 halaman) via LMS | 10% |
| 10 | Pengumpulan & eksplorasi awal data | — | — |
| 11 | **Progress Report 1:** EDA + Baseline Model | Notebook progress (EDA selesai, baseline model berjalan) | Checkpoint |
| 12 | Eksperimen model & hyperparameter tuning | — | — |
| 13 | **Progress Report 2:** Model Optimization | Notebook progress (3+ model dibandingkan, tuning dilakukan) | Checkpoint |
| 14 | Finalisasi notebook, laporan, dan presentasi | — | — |
| 15 | **Final Submission:** Presentasi + Semua Deliverables | Notebook + Laporan + Slide + AI Log | 90% |

### Detail Milestone

#### Minggu 9: Proposal Submission

**Format:** 1-2 halaman PDF

**Isi proposal:**
1. Judul proyek
2. Anggota kelompok (nama, NIM, pembagian tugas awal)
3. Latar belakang & motivasi
4. Problem statement dan pertanyaan penelitian
5. Deskripsi dataset (sumber, ukuran, variabel utama)
6. Rencana metode ML yang akan digunakan
7. Timeline kerja kelompok

#### Minggu 11: Progress Report 1

**Deliverable:** Jupyter Notebook yang menunjukkan:
- Dataset sudah dimuat dan dibersihkan
- EDA lengkap dengan visualisasi
- Baseline model sudah berjalan (minimal 1 model)
- Evaluasi awal tersedia

#### Minggu 13: Progress Report 2

**Deliverable:** Jupyter Notebook yang menunjukkan:
- Minimal 3 model sudah dibandingkan
- Hyperparameter tuning pada model terbaik
- Tabel perbandingan performa
- Draft kesimpulan

---

## 4. Deliverables

### 4.1 Jupyter Notebook (40% dari nilai proyek)

**Format:** File `.ipynb` yang sudah dijalankan semua cell-nya

**Struktur wajib:**
```
1. Judul & Anggota Kelompok
2. Latar Belakang & Problem Statement
3. Deskripsi Dataset (sumber, ukuran, variabel)
4. Exploratory Data Analysis (EDA)
   - Statistik deskriptif
   - Visualisasi data (minimal 5 chart bermakna)
   - Identifikasi & penanganan missing values
   - Identifikasi & penanganan outliers
5. Feature Engineering
   - Encoding, scaling, feature selection
   - Train-test split
6. Modeling
   - Model 1: [nama] — training, prediksi, evaluasi
   - Model 2: [nama] — training, prediksi, evaluasi
   - Model 3: [nama] — training, prediksi, evaluasi
   - Perbandingan performa (tabel + chart)
7. Hyperparameter Tuning (model terbaik)
8. Analisis Hasil & Interpretasi
9. Kesimpulan & Rekomendasi
10. Dokumentasi Penggunaan AI (wajib)
11. Referensi
```

**Kriteria kode:**
- Kode berjalan tanpa error dari awal sampai akhir (Restart & Run All)
- Well-commented (setiap blok kode ada penjelasan dalam Bahasa Indonesia)
- Menggunakan library yang dipelajari: pandas, numpy, matplotlib, seaborn, scikit-learn
- Markdown cells menjelaskan setiap langkah dan keputusan

### 4.2 Laporan Tertulis (20% dari nilai proyek)

**Format:** PDF, 5-8 halaman (tidak termasuk referensi dan lampiran)

**Struktur:**
1. **Pendahuluan** (1 halaman) — Latar belakang, motivasi, pertanyaan penelitian, business value
2. **Data & Metodologi** (1.5 halaman) — Deskripsi dataset, preprocessing, metode ML, justifikasi
3. **Hasil** (1.5-2 halaman) — Perbandingan model, visualisasi kunci, model terbaik
4. **Diskusi** (1-1.5 halaman) — Interpretasi, implikasi, limitasi, ethical considerations
5. **Kesimpulan & Rekomendasi** (0.5-1 halaman) — Ringkasan temuan, rekomendasi, future work
6. **Referensi** — Format APA

**Catatan:** Laporan ditulis dalam Bahasa Indonesia. Istilah teknis boleh dalam Bahasa Inggris.

### 4.3 Presentasi (20% dari nilai proyek)

**Format:** Slide deck (Google Slides/PowerPoint), 15 menit presentasi + 5 menit Q&A

**Struktur slide yang direkomendasikan:**

| No | Slide | Konten |
|----|-------|--------|
| 1 | Judul | Judul proyek, nama kelompok, tanggal |
| 2 | Masalah | Problem statement & business value |
| 3 | Data | Sumber, ukuran, variabel utama |
| 4 | EDA | Visualisasi kunci dari eksplorasi data |
| 5 | Metodologi | Algoritma yang digunakan (diagram/flowchart) |
| 6-8 | Hasil | Perbandingan model, confusion matrix, visualisasi performa |
| 9 | Diskusi | Interpretasi, limitasi, ethical considerations |
| 10 | Kesimpulan | Jawaban problem statement, rekomendasi |
| 11 | AI Usage | Ringkasan penggunaan AI dan refleksi |
| 12 | Q&A | Terima kasih, siap menerima pertanyaan |

**Tips presentasi:**
- Jangan baca slide — gunakan slide sebagai visual aid
- Setiap anggota kelompok harus mempresentasikan bagiannya
- Latihan sebelumnya — 15 menit cepat berlalu
- Fokus pada insight dan business value, bukan pada kode
- Siapkan jawaban untuk pertanyaan umum (mengapa memilih model ini, dll.)

### 4.4 AI Usage Log (10% dari nilai proyek)

**Format:** Section terakhir di Jupyter Notebook ATAU dokumen terpisah

**Template:**
```markdown
## Dokumentasi Penggunaan AI dalam Proyek

### Ringkasan
- Total interaksi AI: [jumlah]
- AI tools yang digunakan: [ChatGPT / Claude / Copilot / lainnya]
- Persentase estimasi kontribusi AI: [X%]

### Log Interaksi

#### Interaksi 1
- **Tahap:** [EDA / Feature Engineering / Modeling / Evaluasi / Interpretasi / Kode / Lainnya]
- **Prompt:** [copy-paste prompt yang digunakan]
- **Output AI:** [ringkasan output]
- **Keputusan:** [diterima / dimodifikasi / ditolak]
- **Alasan:** [mengapa menerima/memodifikasi/menolak]

#### Interaksi 2
[...dst]

### Refleksi
1. Pada tahap mana AI paling membantu?
2. Pada tahap mana AI kurang membantu atau menyesatkan?
3. Apa yang dipelajari dari berkolaborasi dengan AI?
4. Apakah hasil proyek akan berbeda tanpa AI? Mengapa?
```

---

## 5. Rubrik Penilaian Proyek Akhir

### 5.1 Ringkasan Bobot

| Komponen | Bobot dari Proyek | Bobot dari Nilai Akhir |
|----------|-------------------|------------------------|
| Proposal | 10% | 2.5% |
| EDA & Feature Engineering | 20% | 5% |
| Modeling & Evaluation | 25% | 6.25% |
| Analisis & Interpretasi | 15% | 3.75% |
| Presentasi | 20% | 5% |
| Dokumentasi & AI Log | 10% | 2.5% |
| **Total** | **100%** | **25%** |

### 5.2 Rubrik Detail: Proposal (10%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Problem statement** (5%) | Jelas, spesifik, business value teridentifikasi | Cukup jelas, business value ada tapi kurang spesifik | Terlalu umum | Tidak jelas |
| **Rencana metodologi** (5%) | Dataset jelas, metode direncanakan dengan justifikasi | Dataset ada, metode disebutkan | Dataset belum pasti, metode tidak jelas | Tidak ada rencana |

### 5.3 Rubrik Detail: EDA & Feature Engineering (20%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **EDA** (10%) | EDA komprehensif: deskriptif + 5+ visualisasi bermakna + insight mendalam + outlier handling | EDA solid dengan beberapa visualisasi dan insight | EDA dasar, visualisasi minimal | EDA tidak ada atau sangat minim |
| **Feature Engineering** (10%) | Encoding, scaling, feature selection/creation dilakukan dengan justifikasi | Preprocessing dasar dilakukan (encoding, scaling) | Preprocessing minimal, tanpa justifikasi | Tidak ada preprocessing |

### 5.4 Rubrik Detail: Modeling & Evaluation (25%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Model comparison** (15%) | 3+ model dibandingkan, hyperparameter tuning dilakukan, justifikasi kuat | 3 model dibandingkan, beberapa tuning | 2 model, tanpa tuning | 1 model atau model salah |
| **Evaluasi** (10%) | Metrik tepat, cross-validation, confusion matrix, perbandingan tabel + chart | Metrik tepat, beberapa evaluasi | Metrik dasar (accuracy saja) | Tidak ada evaluasi |

### 5.5 Rubrik Detail: Analisis & Interpretasi (15%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Interpretasi** (10%) | Interpretasi mendalam, kontekstual (Indonesia), limitasi didiskusikan, ethical considerations | Interpretasi benar, beberapa konteks | Interpretasi superfisial | Tidak ada atau salah |
| **Kesimpulan** (5%) | Kesimpulan menjawab problem statement, rekomendasi actionable | Kesimpulan ada, rekomendasi umum | Kesimpulan dangkal | Tidak ada kesimpulan |

### 5.6 Rubrik Detail: Presentasi (20%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Delivery** (7%) | Percaya diri, semua anggota presentasi, engaging | Cukup baik, sebagian besar lancar | Kurang percaya diri, monoton | Membaca slide, tidak jelas |
| **Visual & slide** (6%) | Slide clean, visualisasi jelas, tidak terlalu banyak teks | Slide cukup baik | Slide terlalu penuh teks | Slide buruk |
| **Q&A handling** (7%) | Menjawab dengan tepat dan percaya diri, menunjukkan pemahaman mendalam | Menjawab dengan benar | Menjawab sebagian | Tidak bisa menjawab |

### 5.7 Rubrik Detail: Dokumentasi & AI Log (10%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Kelengkapan dokumentasi** (5%) | Semua interaksi AI terdokumentasi dengan detail, kode well-commented | Sebagian besar terdokumentasi | Dokumentasi minim | Tidak ada dokumentasi |
| **Refleksi kritis** (5%) | Refleksi mendalam tentang kapan AI membantu/tidak, lessons learned | Refleksi ada tapi kurang mendalam | Refleksi sangat singkat | Tidak ada refleksi |

---

## 6. Contoh Topik Proyek

### Topik dengan Dataset Publik Indonesia

| No | Topik | Dataset | Algoritma yang Mungkin |
|----|-------|---------|------------------------|
| 1 | Prediksi harga rumah di Jakarta berdasarkan fitur properti | Open Data Jakarta / scraping | Linear Regression, Random Forest, Gradient Boosting |
| 2 | Klasifikasi sentimen review aplikasi e-commerce Indonesia | Google Play Store scraping | Naive Bayes, SVM, Logistic Regression (TF-IDF) |
| 3 | Prediksi tingkat kemiskinan per kabupaten/kota | BPS — Kemiskinan | Random Forest, SVM, KNN |
| 4 | Segmentasi pelanggan berdasarkan pola belanja | Dataset e-commerce Indonesia | K-Means, Hierarchical Clustering, DBSCAN |
| 5 | Prediksi kelulusan tepat waktu mahasiswa | Data internal (anonim) | Decision Tree, Random Forest, Logistic Regression |
| 6 | Klasifikasi jenis penyakit berdasarkan gejala | Dataset kesehatan publik | KNN, SVM, Neural Network |
| 7 | Prediksi curah hujan berdasarkan data historis BMKG | BMKG open data | Random Forest, Gradient Boosting, Linear Regression |
| 8 | Deteksi berita hoax Bahasa Indonesia | Dataset hoax Indonesia | Naive Bayes, SVM, Random Forest (TF-IDF) |
| 9 | Prediksi kualitas udara DKI Jakarta | Open Data Jakarta | Random Forest, SVM, Neural Network |
| 10 | Clustering provinsi Indonesia berdasarkan indikator pembangunan | BPS — IPM, Pendidikan, Kesehatan | K-Means, PCA + Clustering, Hierarchical |

### Panduan Memilih Topik

- **Relevansi:** Pilih topik yang menarik bagi kelompok dan relevan dengan Indonesia
- **Ketersediaan data:** Pastikan dataset accessible dan memiliki minimal 500 baris
- **Feasibility:** Pastikan bisa diselesaikan dalam 7 minggu dengan tools yang dipelajari
- **Kedalaman:** Harus bisa menerapkan dan membandingkan minimal 3 model ML
- **Originalitas:** Hindari duplikasi topik antar kelompok
- **Business value:** Pertanyaan penelitian harus memiliki implikasi praktis

---

## 7. Kebijakan AI (AI Policy)

### Prinsip

AI (ChatGPT, Claude, Copilot) diizinkan sebagai **partner**, bukan pengganti. Penggunaan harus transparan dan terdokumentasi.

### Boleh

- Menggunakan AI untuk debugging kode
- Meminta AI menjelaskan konsep algoritma
- Menggunakan AI untuk brainstorm pendekatan modeling
- Copy-paste kode dari AI **jika dipahami dan didokumentasikan**
- Menggunakan AI untuk memahami error message
- Meminta AI review interpretasi hasil

### Tidak Boleh

- Submit seluruh notebook yang dihasilkan AI tanpa pemahaman
- Tidak mendokumentasikan penggunaan AI
- Claim pekerjaan AI sebagai 100% pekerjaan sendiri
- Menggunakan AI untuk menulis seluruh laporan tanpa modifikasi

### Konsekuensi

- **Tidak ada AI Log:** Pengurangan 10% dari nilai proyek
- **AI Log tidak lengkap:** Pengurangan proporsional
- **Tidak bisa menjelaskan kode/hasil saat presentasi:** Pengurangan signifikan dari nilai presentasi dan Q&A

---

## 8. Panduan Submission

### Apa yang Dikumpulkan (Minggu 15, sebelum presentasi)

1. **Jupyter Notebook:** `ProyekML_Kelompok[X]_[TopikSingkat].ipynb`
2. **Laporan PDF:** `Laporan_Kelompok[X]_[TopikSingkat].pdf`
3. **Slide presentasi:** `Presentasi_Kelompok[X]_[TopikSingkat].pptx` atau link Google Slides
4. **Dataset** (jika kecil) atau **link ke dataset** (jika besar)

### Dimana Mengumpulkan

- **LMS UAI** — Upload semua file (wajib)
- **GitHub** — Push notebook ke repository kelompok (disarankan, bonus portfolio)
- **Google Colab** — Share link notebook yang bisa dijalankan (opsional)

### Checklist Sebelum Submit

- [ ] Notebook berjalan dari awal sampai akhir tanpa error (Restart & Run All)
- [ ] Dataset memiliki minimal 500 baris
- [ ] Minimal 3 model ML dibandingkan
- [ ] Hyperparameter tuning dilakukan pada model terbaik
- [ ] Semua visualisasi terlihat di notebook
- [ ] Dokumentasi AI Usage lengkap
- [ ] Laporan PDF formatted rapi, 5-8 halaman
- [ ] Slide presentasi ready
- [ ] Semua anggota tahu bagian presentasinya
- [ ] Referensi lengkap (dataset, library, paper jika ada)

---

## 9. Panduan Peer Review

Setiap mahasiswa akan me-review **2 kelompok lain** menggunakan form berikut:

### Form Peer Review

```
Kelompok yang di-review: _______________
Reviewer: _______________

Beri skor 1-4 untuk setiap kriteria:

1. Kejelasan problem statement & business value:  [ ] 1  [ ] 2  [ ] 3  [ ] 4
2. Kualitas EDA dan visualisasi:                  [ ] 1  [ ] 2  [ ] 3  [ ] 4
3. Kesesuaian pemilihan model:                     [ ] 1  [ ] 2  [ ] 3  [ ] 4
4. Kedalaman evaluasi dan interpretasi:            [ ] 1  [ ] 2  [ ] 3  [ ] 4
5. Kualitas presentasi:                            [ ] 1  [ ] 2  [ ] 3  [ ] 4
6. Dokumentasi penggunaan AI:                      [ ] 1  [ ] 2  [ ] 3  [ ] 4

Komentar konstruktif (wajib, minimal 3 kalimat):
_____________________________________________

Hal terbaik dari proyek ini:
_____________________________________________

Saran perbaikan:
_____________________________________________
```

**Nilai peer review berkontribusi 5% dari nilai presentasi** (bagian dari 20% presentasi).

---

## 10. FAQ

**Q: Bolehkah menggunakan dataset dari Kaggle?**
A: Boleh, asalkan ada relevansi dengan Indonesia atau mahasiswa bisa menjelaskan konteksnya dengan jelas. Prioritaskan dataset Indonesia.

**Q: Apakah harus 3 model supervised saja?**
A: Tidak harus. Bisa kombinasi supervised dan unsupervised (misal: clustering untuk segmentasi + klasifikasi untuk prediksi), asalkan minimal 3 model dibandingkan.

**Q: Berapa minimum akurasi model yang diterima?**
A: Tidak ada minimum akurasi. Yang dinilai adalah proses: pemilihan model yang tepat, evaluasi yang benar, dan interpretasi yang mendalam. Model dengan akurasi rendah tapi analisis bagus lebih baik dari model akurasi tinggi tanpa penjelasan.

**Q: Bagaimana jika dataset tidak cukup besar?**
A: Cari dataset yang lebih besar, atau gabungkan beberapa dataset terkait. Minimal 500 baris. Konsultasikan dengan dosen jika kesulitan.

**Q: Apakah semua anggota kelompok mendapat nilai yang sama?**
A: Pada prinsipnya ya, kecuali ada bukti kontribusi yang sangat tidak merata. Setiap kelompok akan mengisi peer evaluation internal.

**Q: Bolehkah menggunakan deep learning (neural network)?**
A: Boleh sebagai salah satu dari 3+ model yang dibandingkan. Namun, pastikan juga ada model tradisional (non-deep learning) untuk perbandingan. Penggunaan deep learning tanpa pemahaman justru akan mengurangi nilai.

**Q: Seberapa banyak AI boleh digunakan?**
A: Tidak ada batas, ASALKAN didokumentasikan dan mahasiswa memahami setiap langkah. Jika ditanya saat presentasi dan tidak bisa menjelaskan, itu masalah serius.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
