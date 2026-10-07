# Panduan Proyek Akhir

## Mata Kuliah: Kecerdasan Buatan dan Machine Learning (IF3XXX, 4 SKS)
### Prodi Informatika — UAI — Semester Ganjil 2026/2027
### Dosen Pengampu: Tri Aji Nugroho, S.T., M.T.

---

## 1. Deskripsi Proyek

Proyek akhir merupakan kulminasi dari seluruh pembelajaran selama semester. Kelompok mahasiswa (2-3 orang) membangun **end-to-end ML pipeline** pada dataset riil Indonesia, menggunakan teknik machine learning yang telah dipelajari, dengan **AI sebagai coding partner yang didokumentasikan**.

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
| **Sumber** | Dataset publik Indonesia (BPS, Open Data Jakarta, Kaggle Indonesia, dll.) |
| **Ukuran minimum** | 500 baris (rows) |
| **Fitur minimum** | 5 fitur (kolom) |
| **Konteks** | Harus relevan dengan Indonesia atau konteks lokal |

### 2.2 Jenis Proyek

Kelompok dapat memilih salah satu jenis proyek berikut:

| Jenis | Deskripsi | Algoritma Minimal |
|-------|-----------|-------------------|
| **Klasifikasi** | Prediksi kategori/label dari data tabular | 3 model klasifikasi (misal: Logistic Regression, Random Forest, SVM) |
| **Regresi** | Prediksi nilai numerik kontinu | 3 model regresi (misal: Linear Regression, Random Forest, Gradient Boosting) |
| **Clustering** | Segmentasi data tanpa label + analisis profil cluster | 2 metode clustering + 1 supervised sebagai validasi |
| **NLP** | Klasifikasi teks atau analisis sentimen bahasa Indonesia | Pipeline TF-IDF + 3 classifier |
| **Computer Vision** | Klasifikasi gambar menggunakan CNN | CNN from scratch + transfer learning + 1 model lain |

### 2.3 Komponen Wajib

Setiap proyek **harus** mencakup:

1. **Problem Statement dengan Business Value** — Pertanyaan penelitian yang jelas, mengapa penting, siapa yang diuntungkan
2. **Exploratory Data Analysis (EDA)** — Statistik deskriptif, minimal 5 visualisasi bermakna, missing values, outliers
3. **Feature Engineering** — Encoding, scaling, feature selection/creation, train-test split
4. **Modeling: Minimal 3 Algoritma Berbeda** — Justifikasi pemilihan, hyperparameter tuning pada model terbaik
5. **Evaluasi dan Seleksi Model** — Metrik yang tepat, perbandingan performa, confusion matrix, cross-validation
6. **Kesimpulan dan Rekomendasi** — Ringkasan temuan, limitasi, saran pengembangan

---

## 3. Timeline Proyek

| Minggu | Milestone | Deliverable |
|--------|-----------|-------------|
| 9 | Kickoff: pengumuman, pembentukan kelompok, brainstorm topik | — |
| 10 | Proposal disetujui | Proposal (1-2 halaman) via LMS |
| 11 | **Progress Report 1:** EDA + Baseline Model | Notebook progress: EDA selesai, baseline berjalan |
| 12 | Eksperimen model & hyperparameter tuning | — |
| 13 | **Progress Report 2:** Model Optimization | Notebook progress: 3+ model dibandingkan |
| 14 | Finalisasi + persiapan presentasi | — |
| 15 | **Presentasi + Peer Review** | Semua deliverables dikumpulkan |

### Detail Milestone

#### Minggu 10: Proposal Submission

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
- Menggunakan library yang dipelajari: pandas, numpy, matplotlib, seaborn, scikit-learn, TensorFlow/Keras
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
| 5 | Metodologi | Algoritma yang digunakan (diagram/flowchart pipeline) |
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
- Siapkan jawaban untuk pertanyaan umum (mengapa memilih model ini, bagaimana menangani overfitting, dll.)

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

### 4.5 Proposal & Progress Reports (10% dari nilai proyek — bagian dari total)

| Deliverable | Bobot | Deadline |
|-------------|-------|----------|
| Proposal | 4% | Minggu 10 |
| Progress Report 1 | 3% | Minggu 11 |
| Progress Report 2 | 3% | Minggu 13 |

---

## 5. Contoh Topik Proyek

### Topik dengan Dataset Publik Indonesia

| No | Topik | Dataset | Jenis Proyek | Algoritma yang Mungkin |
|----|-------|---------|--------------|------------------------|
| 1 | Prediksi harga rumah di Jakarta berdasarkan fitur properti | Open Data Jakarta / scraping | Regresi | Linear Regression, Random Forest, Gradient Boosting |
| 2 | Analisis sentimen review aplikasi e-commerce Indonesia | Google Play Store scraping | NLP | Naive Bayes, SVM, Logistic Regression (TF-IDF) |
| 3 | Klasifikasi jenis batik Indonesia dari gambar | Dataset batik (Kaggle/custom) | Computer Vision | CNN from scratch, Transfer Learning (VGG16), SVM (HOG features) |
| 4 | Prediksi tingkat kemiskinan per kabupaten/kota | BPS — Kemiskinan | Klasifikasi | Random Forest, SVM, KNN |
| 5 | Segmentasi pelanggan e-commerce berdasarkan pola belanja | Dataset e-commerce Indonesia | Clustering | K-Means, Hierarchical, DBSCAN + profiling |
| 6 | Prediksi kualitas udara DKI Jakarta | Open Data Jakarta / BMKG | Regresi/Klasifikasi | Random Forest, Gradient Boosting, Neural Network |
| 7 | Deteksi berita hoax Bahasa Indonesia | Dataset hoax Indonesia | NLP | Naive Bayes, SVM, Random Forest (TF-IDF) |
| 8 | Prediksi kelulusan tepat waktu mahasiswa | Data internal (anonim) | Klasifikasi | Decision Tree, Random Forest, Logistic Regression |
| 9 | Klasifikasi citra produk UMKM Indonesia | Dataset custom | Computer Vision | CNN, Transfer Learning, KNN (feature extraction) |
| 10 | Clustering provinsi Indonesia berdasarkan indikator pembangunan | BPS — IPM, Pendidikan, Kesehatan | Clustering | K-Means + PCA, Hierarchical, DBSCAN |

### Panduan Memilih Topik

- **Relevansi:** Pilih topik yang menarik bagi kelompok dan relevan dengan Indonesia
- **Ketersediaan data:** Pastikan dataset accessible dan memiliki minimal 500 baris, 5 fitur
- **Feasibility:** Pastikan bisa diselesaikan dalam 7 minggu dengan tools yang dipelajari
- **Kedalaman:** Harus bisa menerapkan dan membandingkan minimal 3 model ML
- **Originalitas:** Hindari duplikasi topik antar kelompok
- **Business value:** Pertanyaan penelitian harus memiliki implikasi praktis

---

## 6. Rubrik Penilaian Proyek Akhir

### 6.1 Jupyter Notebook (40%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **EDA** (10%) | EDA komprehensif: deskriptif + 5+ visualisasi bermakna + insight mendalam + outlier handling | EDA solid dengan beberapa visualisasi dan insight | EDA dasar, visualisasi minimal | EDA tidak ada atau sangat minim |
| **Feature Engineering** (10%) | Encoding, scaling, feature selection/creation dilakukan dengan justifikasi kuat | Preprocessing dasar dilakukan (encoding, scaling) | Preprocessing minimal, tanpa justifikasi | Tidak ada preprocessing |
| **Model Comparison** (10%) | 3+ model dibandingkan, hyperparameter tuning dilakukan, justifikasi kuat untuk setiap keputusan | 3 model dibandingkan, beberapa tuning | 2 model, tanpa tuning | 1 model atau model salah |
| **Kualitas Kode** (10%) | Kode clean, efficient, well-documented, reproducible. Comments informatif dalam Bahasa Indonesia | Kode berjalan, beberapa comment. Sebagian besar readable | Kode berjalan tapi berantakan, minim comment | Kode error, tidak lengkap |

### 6.2 Laporan Tertulis (20%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Struktur & writing** (7%) | Terstruktur rapi, bahasa akademik, flow logis | Cukup terstruktur, bahasa baik | Kurang terstruktur | Tidak terstruktur |
| **Metodologi** (6%) | Metode dijelaskan dan dijustifikasi dengan baik, termasuk alasan pemilihan | Metode dijelaskan | Metode disebutkan tanpa justifikasi | Metode tidak jelas |
| **Temuan & insight** (7%) | Temuan bermakna, didukung data, implikasi praktis jelas, limitasi didiskusikan | Temuan ada, didukung data | Temuan superfisial | Tidak ada temuan jelas |

### 6.3 Presentasi (20%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Delivery** (7%) | Percaya diri, semua anggota presentasi, engaging | Cukup baik, sebagian besar lancar | Kurang percaya diri, monoton | Membaca slide, tidak jelas |
| **Visual & slide** (6%) | Slide clean, visualisasi jelas, tidak terlalu banyak teks | Slide cukup baik | Slide terlalu penuh teks | Slide buruk |
| **Q&A handling** (7%) | Menjawab dengan tepat dan percaya diri, menunjukkan pemahaman mendalam terhadap pipeline ML | Menjawab dengan benar | Menjawab sebagian | Tidak bisa menjawab |

### 6.4 AI Usage Log (10%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Kelengkapan dokumentasi** (5%) | Semua interaksi AI terdokumentasi dengan detail (prompt, output, keputusan) | Sebagian besar terdokumentasi | Dokumentasi minim | Tidak ada dokumentasi |
| **Refleksi kritis** (5%) | Refleksi mendalam tentang kapan AI membantu/tidak, lessons learned, evaluasi kritis output AI | Refleksi ada tapi kurang mendalam | Refleksi sangat singkat | Tidak ada refleksi |

### 6.5 Proposal & Progress (10%)

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Proposal** (4%) | Jelas, spesifik, business value teridentifikasi, rencana metodologi solid | Cukup jelas, rencana ada | Terlalu umum | Tidak jelas atau tidak dikumpulkan |
| **Progress Reports** (6%) | Tepat waktu, menunjukkan kemajuan signifikan pada setiap checkpoint | Tepat waktu, kemajuan cukup | Terlambat atau kemajuan minimal | Tidak dikumpulkan |

---

## 7. Panduan Peer Review

Setiap mahasiswa akan me-review **2 kelompok lain** menggunakan form berikut:

### Form Peer Review

```
Kelompok yang di-review: _______________
Reviewer: _______________

Beri skor 1-4 untuk setiap kriteria:

1. Kejelasan problem statement & business value:  [ ] 1  [ ] 2  [ ] 3  [ ] 4
2. Kualitas EDA dan visualisasi:                  [ ] 1  [ ] 2  [ ] 3  [ ] 4
3. Kesesuaian pemilihan model ML:                 [ ] 1  [ ] 2  [ ] 3  [ ] 4
4. Kedalaman evaluasi dan interpretasi:            [ ] 1  [ ] 2  [ ] 3  [ ] 4
5. Kualitas presentasi dan demo:                   [ ] 1  [ ] 2  [ ] 3  [ ] 4
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

## 8. Kebijakan AI (AI Policy)

### Prinsip

AI (ChatGPT, Claude, Copilot) diizinkan sebagai **coding partner**, bukan pengganti. Penggunaan harus transparan dan terdokumentasi. Prinsip **amanah** (kejujuran) menjadi landasan: mahasiswa harus memahami setiap baris kode dan keputusan model.

### Boleh

- Menggunakan AI untuk debugging kode ML
- Meminta AI menjelaskan konsep algoritma yang sulit
- Menggunakan AI untuk brainstorm pendekatan modeling
- Copy-paste kode dari AI **jika dipahami dan didokumentasikan**
- Menggunakan AI untuk memahami error message
- Meminta AI review interpretasi hasil model

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

## 9. Panduan Submission

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
- [ ] Dataset memiliki minimal 500 baris dan 5 fitur
- [ ] Minimal 3 model ML dibandingkan
- [ ] Hyperparameter tuning dilakukan pada model terbaik
- [ ] Semua visualisasi terlihat di notebook
- [ ] Dokumentasi AI Usage lengkap
- [ ] Laporan PDF formatted rapi, 5-8 halaman
- [ ] Slide presentasi ready
- [ ] Semua anggota tahu bagian presentasinya
- [ ] Referensi lengkap (dataset, library, paper jika ada)

---

## 10. FAQ

**Q: Bolehkah menggunakan dataset dari Kaggle?**
A: Boleh, asalkan ada relevansi dengan Indonesia atau mahasiswa bisa menjelaskan konteksnya. Prioritaskan dataset Indonesia.

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
