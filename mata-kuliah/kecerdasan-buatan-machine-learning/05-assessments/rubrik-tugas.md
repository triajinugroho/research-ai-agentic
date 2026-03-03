# Rubrik Penilaian Tugas

## Mata Kuliah: Kecerdasan Buatan dan Machine Learning (IF3XXX, 4 SKS)
### Prodi Informatika — UAI — Semester Ganjil 2026/2027
### Dosen Pengampu: Tri Aji Nugroho, S.T., M.T.

---

## Rubrik Universal 4-Point Scale

Semua tugas dinilai menggunakan skala 4 poin pada 5 dimensi utama:

| Dimensi | Bobot | Deskripsi |
|---------|-------|-----------|
| **Kebenaran Kode** | 30% | Ketepatan implementasi algoritma, kebenaran output, kode berjalan tanpa error |
| **Analisis & Interpretasi** | 25% | Kemampuan menjelaskan hasil dalam konteks, insight bermakna, diskusi limitasi |
| **Kualitas Kode Python** | 20% | Kebersihan, efisiensi, dokumentasi kode, penggunaan library yang tepat |
| **Dokumentasi & Penjelasan** | 15% | Struktur notebook, narrative flow, markdown cells, readability |
| **AI Usage Log** | 10% | Dokumentasi penggunaan AI sebagai learning partner, refleksi kritis |

---

## Detail Rubrik per Dimensi

### Dimensi 1: Kebenaran Kode (30%)

| Skor | Deskripsi |
|------|-----------|
| **4 — Sangat Baik** | Semua implementasi algoritma benar. Output lengkap dan terverifikasi. Model berjalan tanpa error. Metrik evaluasi dihitung dengan tepat. Menunjukkan pemahaman mendalam tentang algoritma yang diimplementasikan. |
| **3 — Baik** | Sebagian besar implementasi benar (1-2 minor error). Model berjalan. Metrik evaluasi sebagian besar benar. |
| **2 — Cukup** | Implementasi dasar ada tapi beberapa error signifikan. Model mungkin berjalan tapi hasil kurang tepat. Beberapa metrik salah atau tidak lengkap. |
| **1 — Kurang** | Banyak error dalam implementasi. Model tidak berjalan atau output salah. Metrik evaluasi tidak ada atau salah. |

### Dimensi 2: Analisis & Interpretasi (25%)

| Skor | Deskripsi |
|------|-----------|
| **4 — Sangat Baik** | Interpretasi mendalam dan kontekstual (Indonesia). Menghubungkan metrik dengan makna riil. Mengidentifikasi limitasi model. Memberikan insight yang tidak obvious. Membedakan overfitting vs underfitting. |
| **3 — Baik** | Interpretasi benar dan cukup kontekstual. Menyebutkan beberapa limitasi. Insight ada tapi standard. |
| **2 — Cukup** | Interpretasi superfisial — hanya menyebutkan angka metrik tanpa konteks. Atau interpretasi ada tapi beberapa salah. Tidak ada diskusi limitasi. |
| **1 — Kurang** | Tidak ada interpretasi, atau interpretasi salah secara fundamental (misal: "accuracy 90% berarti model sempurna" tanpa mempertimbangkan class imbalance). |

### Dimensi 3: Kualitas Kode Python (20%)

| Skor | Deskripsi |
|------|-----------|
| **4 — Sangat Baik** | Kode clean dan efisien. Menggunakan scikit-learn/TensorFlow idiomatik (Pipeline, cross_val_score). Comment informatif dalam Bahasa Indonesia. Variable names deskriptif. Bisa di-reproduce tanpa modifikasi. |
| **3 — Baik** | Kode berjalan dengan benar. Ada beberapa comment. Sebagian besar readable. Minor inefficiency. |
| **2 — Cukup** | Kode berjalan tapi tidak efisien (banyak repetisi, hardcoded values). Minim comment. Sulit dibaca. |
| **1 — Kurang** | Kode error, tidak lengkap, atau copy-paste tanpa pemahaman (obvious dari variable names atau structure yang tidak konsisten). |

### Dimensi 4: Dokumentasi & Penjelasan (15%)

| Skor | Deskripsi |
|------|-----------|
| **4 — Sangat Baik** | Notebook terstruktur rapi dengan markdown headings. Flow logis dari introduction → preprocessing → modeling → evaluation → conclusion. Narasi menghubungkan setiap bagian. Bisa dibaca seperti mini-report. |
| **3 — Baik** | Cukup terstruktur, ada beberapa heading. Flow cukup logis. Ada narasi tapi tidak selalu connecting. |
| **2 — Cukup** | Kurang terorganisir. Minim markdown. Code cells berurutan tapi tanpa penjelasan alur. |
| **1 — Kurang** | Tidak terstruktur. Cells berantakan. Tidak ada narasi. Sulit memahami apa yang dilakukan dan mengapa. |

### Dimensi 5: AI Usage Log (10%)

| Skor | Deskripsi |
|------|-----------|
| **4 — Sangat Baik** | Semua interaksi AI terdokumentasi (prompt, output, keputusan). Refleksi kritis: kapan AI membantu, kapan menyesatkan, lessons learned. Menunjukkan evaluasi kritis terhadap output AI. |
| **3 — Baik** | Sebagian besar interaksi terdokumentasi. Refleksi ada tapi kurang mendalam. |
| **2 — Cukup** | Dokumentasi minim — hanya menyebutkan "menggunakan ChatGPT" tanpa detail. Refleksi sangat singkat atau generik. |
| **1 — Kurang** | Tidak ada dokumentasi AI atau menyatakan tidak menggunakan AI padahal ada indikasi kuat penggunaan AI tanpa dokumentasi. |

---

## Konversi Skor ke Nilai

| Total Skor Tertimbang | Nilai (0-100) | Huruf |
|-----------------------|---------------|-------|
| 3.60 - 4.00 | 90-100 | A |
| 3.20 - 3.59 | 80-89 | A-/B+ |
| 2.80 - 3.19 | 70-79 | B+/B |
| 2.40 - 2.79 | 60-69 | B-/C+ |
| 2.00 - 2.39 | 50-59 | C |
| 1.60 - 1.99 | 40-49 | D |
| < 1.60 | <40 | E |

**Formula:** `Nilai = (Skor Tertimbang / 4.00) x 100`

**Skor Tertimbang** = (Kebenaran Kode x 0.30) + (Analisis x 0.25) + (Kualitas Kode x 0.20) + (Dokumentasi x 0.15) + (AI Log x 0.10)

---

## Daftar Tugas dan Peta CPMK

| No | Minggu | Topik Tugas | CPMK | Bobot |
|----|--------|-------------|------|-------|
| T1 | 2 | Eksplorasi Data & Preprocessing dengan Python | CPMK-1, CPMK-2 | 2.5% |
| T2 | 4 | EDA dan Feature Engineering untuk ML | CPMK-2 | 2.5% |
| T3 | 6 | Supervised Learning: Klasifikasi dengan Decision Tree & Random Forest | CPMK-3 | 2.5% |
| T4 | 10 | Unsupervised Learning: Clustering & PCA | CPMK-4 | 2.5% |
| T5 | 12 | Natural Language Processing pada Teks Bahasa Indonesia | CPMK-5, CPMK-6 | 2.5% |
| T6 | 14 | Etika AI & Responsible ML Pipeline | CPMK-6, CPMK-7 | 2.5% |
| | | **Total Tugas Mingguan** | | **15%** |

---

## Rubrik Spesifik per Tugas

### Tugas 1: Eksplorasi Data & Preprocessing dengan Python

**Minggu:** 2 | **CPMK:** CPMK-1 (C2), CPMK-2 (C3)

**Deskripsi:** Melakukan eksplorasi dan preprocessing pada dataset Indonesia (misal: data BPS, data pendidikan) menggunakan NumPy, Pandas, dan scikit-learn preprocessing.

| Kriteria | Poin Kunci |
|----------|------------|
| **Kebenaran Kode** | Data dimuat dengan benar (pandas). Missing values diidentifikasi dan ditangani (imputation/deletion). Encoding kategorikal (OneHotEncoder/LabelEncoder) benar. Scaling fitur (StandardScaler/MinMaxScaler) benar. Tidak ada data leakage (fit pada training, transform pada test). |
| **Analisis & Interpretasi** | "Dataset memiliki 15% missing values pada kolom pendapatan, diisi dengan median karena distribusi skewed" — bukan hanya "menggunakan fillna()". Penjelasan mengapa memilih teknik imputation tertentu. |
| **Kualitas Kode** | Penggunaan `df.info()`, `df.describe()`, `df.isnull().sum()`. sklearn.preprocessing Pipeline. Kode modular dan reusable. |
| **Dokumentasi** | Sections: Load Data → Overview → Missing Values → Encoding → Scaling → Summary |
| **AI Usage** | Dokumentasi jika menggunakan AI untuk debugging preprocessing atau memahami konsep encoding |

---

### Tugas 2: EDA dan Feature Engineering untuk ML

**Minggu:** 4 | **CPMK:** CPMK-2 (C3-C4)

**Deskripsi:** Melakukan EDA komprehensif dan feature engineering pada dataset ML, termasuk visualisasi, deteksi outlier, korelasi, dan pembuatan fitur baru.

| Kriteria | Poin Kunci |
|----------|------------|
| **Kebenaran Kode** | Minimal 5 visualisasi berbeda dan bermakna (histogram, boxplot, scatter, heatmap, pairplot). Outlier detection (IQR/z-score) benar. Feature creation (polynomial, interaction, binning) diterapkan. Train-test split dengan stratification. |
| **Analisis & Interpretasi** | Narasi yang menghubungkan visualisasi: "Dari heatmap korelasi terlihat bahwa fitur X dan Y sangat berkorelasi (r=0.85), sehingga salah satu perlu dihapus untuk menghindari multikolinearitas" |
| **Kualitas Kode** | matplotlib + seaborn, customization (warna, label, ukuran). Feature engineering menggunakan sklearn transformers. |
| **Dokumentasi** | Data Story mengalir: Dataset Overview → Distribution Analysis → Correlation → Outliers → Feature Engineering → Ready for Modeling |
| **AI Usage** | Dokumentasi jika menggunakan AI untuk inspirasi visualisasi atau teknik feature engineering |

---

### Tugas 3: Supervised Learning — Klasifikasi dengan Decision Tree & Random Forest

**Minggu:** 6 | **CPMK:** CPMK-3 (C4)

**Deskripsi:** Membangun, melatih, dan mengevaluasi model Decision Tree dan Random Forest untuk klasifikasi pada dataset Indonesia (misal: klasifikasi kelayakan kredit nasabah bank).

| Kriteria | Poin Kunci |
|----------|------------|
| **Kebenaran Kode** | Decision Tree dan Random Forest dibangun dengan sklearn. Cross-validation diterapkan (stratified k-fold). Confusion matrix dan classification report benar. Feature importance diekstrak dan divisualisasikan. Hyperparameter tuning (max_depth, n_estimators) dengan GridSearchCV. |
| **Analisis & Interpretasi** | "Random Forest (accuracy 87%, F1 0.84) outperform Decision Tree (accuracy 79%, F1 0.76) karena ensemble mengurangi overfitting. Feature importance menunjukkan 'penghasilan' sebagai faktor terpenting." |
| **Kualitas Kode** | sklearn Pipeline dengan preprocessing + model. Visualisasi pohon keputusan. Perbandingan model dalam tabel. ROC curve jika binary classification. |
| **Dokumentasi** | Preprocessing → Model 1 (DT) → Model 2 (RF) → Comparison → Feature Importance → Best Model Selection |
| **AI Usage** | Dokumentasi jika menggunakan AI untuk hyperparameter tuning strategy atau interpretasi feature importance |

---

### Tugas 4: Unsupervised Learning — Clustering & PCA

**Minggu:** 10 | **CPMK:** CPMK-4 (C3-C4)

**Deskripsi:** Menerapkan K-Means clustering dan PCA pada dataset Indonesia (misal: segmentasi pelanggan e-commerce, clustering provinsi berdasarkan indikator pembangunan BPS).

| Kriteria | Poin Kunci |
|----------|------------|
| **Kebenaran Kode** | K-Means dengan pemilihan K optimal (Elbow + Silhouette). Hierarchical clustering dengan dendrogram. PCA dengan explained variance ratio. Visualisasi cluster dalam 2D (PCA space). Profiling setiap cluster. |
| **Analisis & Interpretasi** | "Cluster 1 (25% pelanggan) adalah 'heavy spenders': rata-rata transaksi Rp 500K/bulan, frekuensi 8x/bulan. Cluster 2 adalah 'occasional buyers'..." — profiling cluster bermakna dan actionable |
| **Kualitas Kode** | sklearn cluster dan decomposition. Elbow plot dan silhouette visualization. Scatter plot dengan warna per cluster. Cluster profiling table. |
| **Dokumentasi** | Data Overview → Scaling → Elbow/Silhouette → Clustering → PCA Visualization → Cluster Profiling → Business Insight |
| **AI Usage** | Dokumentasi jika menggunakan AI untuk interpretasi cluster atau strategi profiling |

---

### Tugas 5: NLP pada Teks Bahasa Indonesia

**Minggu:** 12 | **CPMK:** CPMK-5 (C3), CPMK-6 (C3-C4)

**Deskripsi:** Membangun pipeline NLP untuk analisis sentimen atau klasifikasi teks Bahasa Indonesia (misal: analisis sentimen ulasan produk e-commerce Tokopedia/Shopee).

| Kriteria | Poin Kunci |
|----------|------------|
| **Kebenaran Kode** | Text preprocessing: tokenisasi, case folding, stopword removal (Bahasa Indonesia), stemming (Sastrawi). TF-IDF vectorization. Klasifikasi teks dengan minimal 2 model (Naive Bayes, SVM, Logistic Regression). Evaluasi per kelas (precision, recall, F1). |
| **Analisis & Interpretasi** | "SVM dengan TF-IDF menghasilkan F1 macro 0.82, lebih baik dari Naive Bayes (0.75). Kelas 'netral' paling sulit diprediksi (F1=0.68) karena ambiguitas bahasa informal e-commerce." |
| **Kualitas Kode** | sklearn Pipeline (TF-IDF + classifier). Sastrawi untuk stemming Indonesia. Word cloud visualisasi. Error analysis pada misklasifikasi. |
| **Dokumentasi** | Data Loading → Text Cleaning → Preprocessing (tokenize, stem) → Vectorization → Modeling → Evaluation → Error Analysis |
| **AI Usage** | Dokumentasi jika menggunakan AI untuk text preprocessing strategy atau debugging NLP pipeline |

---

### Tugas 6: Etika AI & Responsible ML Pipeline

**Minggu:** 14 | **CPMK:** CPMK-6 (C4), CPMK-7 (C5-C6)

**Deskripsi:** Menganalisis bias dan fairness pada model ML, membangun pipeline ML yang responsible, dan merefleksikan penggunaan AI sepanjang semester.

| Kriteria | Poin Kunci |
|----------|------------|
| **Kebenaran Kode** | Audit bias pada model (performa per subgrup). Implementasi fairness metrics (demographic parity, equal opportunity). Model saving dengan joblib/pickle. Experiment logging (parameter, metrics). Reproducibility (random seed, versi library). |
| **Analisis & Interpretasi** | "Model menunjukkan recall lebih rendah untuk kelompok usia >50 tahun (67% vs 85% untuk usia <30). Ini berpotensi diskriminatif dan perlu mitigasi." Refleksi mendalam tentang etika AI dan nilai-nilai Islam (amanah, keadilan/al-'adl). |
| **Kualitas Kode** | Fairness audit code. Model persistence (save/load). Environment reproducibility. Pipeline end-to-end yang clean. |
| **Dokumentasi** | Model Audit → Bias Detection → Fairness Metrics → Mitigation Strategy → Model Saving → Reproducibility → Ethical Reflection |
| **AI Usage** | Refleksi komprehensif penggunaan AI sepanjang semester: kapan membantu, kapan menyesatkan, lessons learned |

---

## Panduan untuk Mahasiswa

### Cara Mendapat Nilai Maksimal

1. **Jangan hanya menjalankan kode** — Jelaskan apa yang dilakukan dan MENGAPA memilih pendekatan tersebut
2. **Interpretasi > Angka** — Output `classification_report` tanpa interpretasi = setengah nilai
3. **Konteks Indonesia** — Hubungkan temuan dengan situasi riil di Indonesia
4. **Dokumentasi AI** — Jika pakai AI, dokumentasikan dengan jujur (prinsip amanah)
5. **Review sebelum submit** — Restart & Run All, pastikan tidak ada error
6. **Perbandingan bermakna** — Jangan hanya menjalankan model, tapi jelaskan MENGAPA satu model lebih baik

### Kesalahan Umum yang Mengurangi Nilai

- Hanya menempel output tanpa interpretasi
- Copy-paste kode tanpa memahami apa yang dilakukan
- Tidak melakukan preprocessing (encoding, scaling) sebelum modeling
- Tidak melakukan train-test split (data leakage)
- Menggunakan accuracy sebagai satu-satunya metrik pada dataset imbalanced
- Notebook tanpa struktur (langsung code tanpa markdown)
- Tidak mendokumentasikan penggunaan AI
- Tidak menangani missing values atau outliers
- Melakukan fit scaler pada seluruh dataset (bukan hanya training data)

---

## Kebijakan Submission

### Format Pengumpulan

| Komponen | Detail |
|----------|--------|
| **Format file** | Jupyter Notebook (.ipynb) yang sudah dijalankan semua cell-nya |
| **Nama file** | `T[N]_NIM_NamaLengkap.ipynb` (misal: `T1_12345_AhmadFauzi.ipynb`) |
| **Platform** | Upload via LMS UAI |
| **Deadline** | 1 minggu setelah tugas diberikan, pukul 23:59 WIB |

### Keterlambatan

- Keterlambatan 1-3 hari: penalti -20% dari nilai tugas
- Keterlambatan >3 hari: nilai maksimal 50% dari rubrik
- Force majeure: dikonsultasikan dengan dosen pengampu

### Revisi (Bonus)

Mahasiswa yang **merevisi tugas** berdasarkan feedback dosen (dalam 1 minggu setelah feedback diberikan) mendapat **bonus 5% dari nilai tugas tersebut**. Revisi harus jelas menunjukkan perubahan yang dilakukan.

### Checklist Sebelum Submit

- [ ] Notebook berjalan dari awal sampai akhir tanpa error (Restart & Run All)
- [ ] Semua visualisasi terlihat
- [ ] Setiap code cell memiliki penjelasan markdown di atasnya
- [ ] AI Usage Log lengkap (di section terakhir notebook)
- [ ] Nama dan NIM tertulis di cell pertama
- [ ] Semua library yang diperlukan di-import di cell awal
- [ ] Kode menggunakan comment dalam Bahasa Indonesia
- [ ] Dataset disertakan atau link ke dataset dicantumkan

---

*Dokumen ini merupakan bagian dari RPS mata kuliah Kecerdasan Buatan dan Machine Learning, Prodi Informatika, Universitas Al Azhar Indonesia.*

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
