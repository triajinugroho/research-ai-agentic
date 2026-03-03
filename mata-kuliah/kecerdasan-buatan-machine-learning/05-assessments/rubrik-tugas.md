# Rubrik Penilaian Tugas Mingguan

## Mata Kuliah: Kecerdasan Buatan dan Machine Learning (IF3XXX, 4 SKS)
### Prodi Informatika — UAI — Semester Ganjil 2026/2027
### Dosen Pengampu: Tri Aji Nugroho, S.T., M.T.

---

## Rubrik Umum (General Rubric)

Semua tugas mingguan (T1-T6) dinilai menggunakan 5 dimensi utama:

| Dimensi | Bobot | Deskripsi |
|---------|-------|-----------|
| **Kebenaran Kode** | 30% | Ketepatan implementasi algoritma, output benar, kode berjalan tanpa error |
| **Analisis & Interpretasi** | 25% | Kemampuan menjelaskan hasil dalam konteks, insight bermakna |
| **Kualitas Kode** | 20% | Kebersihan, efisiensi, dokumentasi, penamaan variabel |
| **Dokumentasi & Penjelasan** | 15% | Struktur notebook, markdown narrative, flow logis |
| **AI Usage Log** | 10% | Dokumentasi penggunaan AI sebagai learning partner |

---

## Detail Rubrik per Dimensi (4-Point Scale)

### Dimensi 1: Kebenaran Kode (30%)

| Skor | Predikat | Deskripsi |
|------|----------|-----------|
| **4** | **Sangat Baik** | Semua implementasi benar. Model dibangun dan dievaluasi dengan tepat. Output lengkap dan terverifikasi. Menunjukkan pemahaman mendalam tentang algoritma yang digunakan. Handling edge cases. |
| **3** | **Baik** | Sebagian besar implementasi benar (1-2 minor error). Model berjalan dan memberikan output yang masuk akal. Sebagian besar output benar. |
| **2** | **Cukup** | Implementasi dasar ada tapi beberapa error signifikan. Model mungkin berjalan tapi hasilnya kurang tepat. Beberapa langkah penting terlewat. |
| **1** | **Kurang** | Banyak error dalam implementasi. Kode tidak berjalan atau output salah. Algoritma salah dipilih atau salah diimplementasikan. |

### Dimensi 2: Analisis & Interpretasi (25%)

| Skor | Predikat | Deskripsi |
|------|----------|-----------|
| **4** | **Sangat Baik** | Interpretasi mendalam dan kontekstual (Indonesia). Menghubungkan metrik dengan makna riil. Mengidentifikasi limitasi model. Memberikan insight yang tidak obvious. Membedakan overfitting vs underfitting. |
| **3** | **Baik** | Interpretasi benar dan cukup kontekstual. Menyebutkan beberapa limitasi. Insight ada tapi standard. Metrik dijelaskan dengan benar. |
| **2** | **Cukup** | Interpretasi superfisial — hanya menyebutkan angka tanpa konteks. Atau interpretasi ada tapi beberapa salah. Tidak ada diskusi limitasi. |
| **1** | **Kurang** | Tidak ada interpretasi, atau interpretasi salah secara fundamental (misal: "accuracy tinggi berarti model pasti bagus" tanpa mempertimbangkan class imbalance). |

### Dimensi 3: Kualitas Kode (20%)

| Skor | Predikat | Deskripsi |
|------|----------|-----------|
| **4** | **Sangat Baik** | Kode clean dan efisien. Menggunakan scikit-learn idiomatik (Pipeline, cross_val_score). Comment informatif dalam Bahasa Indonesia. Variable names deskriptif. Bisa di-reproduce tanpa modifikasi. |
| **3** | **Baik** | Kode berjalan dengan benar. Ada beberapa comment. Sebagian besar readable. Minor inefficiency (misal: repetisi kode yang bisa di-loop). |
| **2** | **Cukup** | Kode berjalan tapi tidak efisien (banyak repetisi, hardcoded values). Minim comment. Sulit dibaca. Penamaan variabel tidak deskriptif. |
| **1** | **Kurang** | Kode error, tidak lengkap, atau copy-paste tanpa pemahaman (obvious dari variable names, import tidak terpakai, atau structure). |

### Dimensi 4: Dokumentasi & Penjelasan (15%)

| Skor | Predikat | Deskripsi |
|------|----------|-----------|
| **4** | **Sangat Baik** | Notebook terstruktur rapi dengan markdown headings. Flow logis dari introduction --> preprocessing --> modeling --> evaluation --> conclusion. Narasi menghubungkan setiap bagian. Bisa dibaca seperti mini-report. |
| **3** | **Baik** | Cukup terstruktur, ada beberapa heading. Flow cukup logis. Ada narasi tapi tidak selalu connecting antar bagian. |
| **2** | **Cukup** | Kurang terorganisir. Minim markdown. Code cells berurutan tapi tanpa penjelasan alur. |
| **1** | **Kurang** | Tidak terstruktur. Cells berantakan. Tidak ada narasi. Sulit memahami apa yang dilakukan dan mengapa. |

### Dimensi 5: AI Usage Log (10%)

| Skor | Predikat | Deskripsi |
|------|----------|-----------|
| **4** | **Sangat Baik** | Setiap interaksi AI terdokumentasi lengkap (prompt, output, keputusan, alasan). Refleksi kritis tentang kapan AI membantu dan tidak. Menunjukkan kemampuan mengevaluasi output AI. |
| **3** | **Baik** | Dokumentasi ada dan cukup lengkap. Refleksi ada tapi kurang mendalam. Beberapa interaksi terdokumentasi. |
| **2** | **Cukup** | Dokumentasi minim — hanya menyebutkan "menggunakan ChatGPT" tanpa detail. Refleksi sangat singkat atau tidak ada. |
| **1** | **Kurang** | Tidak ada dokumentasi penggunaan AI, atau menyatakan tidak menggunakan AI padahal ada indikasi kuat penggunaan AI tanpa dokumentasi. |

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

## Rubrik Spesifik per Tugas

### Tugas 1 (T1): Eksplorasi Data & Preprocessing dengan Python
**Minggu:** 2 | **CPMK:** CPMK-1, CPMK-2

| Dimensi | Poin Kunci yang Dinilai |
|---------|------------------------|
| **Kebenaran Kode** | Data dimuat dengan benar (pandas). Missing values diidentifikasi dan ditangani (imputation/deletion). Encoding kategorikal (OneHotEncoder/LabelEncoder) benar. Scaling fitur (StandardScaler/MinMaxScaler) benar. |
| **Analisis & Interpretasi** | "Dari 15 fitur, 3 fitur memiliki missing values >10%..." — bukan hanya "ada missing values". Penjelasan mengapa memilih teknik imputation tertentu. Insight dari distribusi data. |
| **Kualitas Kode** | Penggunaan `df.info()`, `df.describe()`, `df.isnull().sum()`. Kode preprocessing modular. Visualisasi distribusi dan korelasi. |
| **Dokumentasi** | Sections: Load Data --> Overview --> Missing Values --> Encoding --> Scaling --> Summary |
| **AI Log** | Dokumentasi jika menggunakan AI untuk memahami teknik preprocessing |

---

### Tugas 2 (T2): Implementasi Supervised Learning: Klasifikasi
**Minggu:** 4 | **CPMK:** CPMK-3

| Dimensi | Poin Kunci yang Dinilai |
|---------|------------------------|
| **Kebenaran Kode** | Train-test split benar (stratified jika class imbalanced). Minimal 2 model klasifikasi diimplementasikan (misal: KNN + Decision Tree). Prediksi dan evaluasi benar. |
| **Analisis & Interpretasi** | Mengapa memilih algoritma tersebut? Perbandingan performa antar model. Interpretasi confusion matrix: "Model salah mengklasifikasikan 15 kasus positif sebagai negatif, yang berarti..." |
| **Kualitas Kode** | Penggunaan scikit-learn Pipeline. `classification_report` dan `confusion_matrix`. Visualisasi confusion matrix dengan heatmap. |
| **Dokumentasi** | Sections: Dataset Overview --> Preprocessing --> Model 1 --> Model 2 --> Comparison --> Conclusion |
| **AI Log** | Dokumentasi jika menggunakan AI untuk debugging atau memilih model |

---

### Tugas 3 (T3): Evaluasi Model & Hyperparameter Tuning
**Minggu:** 6 | **CPMK:** CPMK-3

| Dimensi | Poin Kunci yang Dinilai |
|---------|------------------------|
| **Kebenaran Kode** | Cross-validation diimplementasikan dengan benar (stratified k-fold). GridSearchCV atau RandomizedSearchCV diterapkan. ROC curve dan AUC dihitung. Learning curves divisualisasikan. |
| **Analisis & Interpretasi** | Membedakan overfitting vs underfitting dari learning curves. Mengapa model A lebih baik dari model B? Apakah tuning signifikan meningkatkan performa? Penjelasan tradeoff precision-recall. |
| **Kualitas Kode** | Penggunaan `cross_val_score`, `GridSearchCV`, `learning_curve`. Plotting ROC curves. Tabel perbandingan performa. |
| **Dokumentasi** | Sections: Baseline Evaluation --> Cross-Validation --> Hyperparameter Tuning --> Learning Curves --> Best Model --> Conclusion |
| **AI Log** | Dokumentasi jika menggunakan AI untuk memahami metrik evaluasi atau tuning strategies |

---

### Tugas 4 (T4): Unsupervised Learning: Clustering & PCA
**Minggu:** 10 | **CPMK:** CPMK-4

| Dimensi | Poin Kunci yang Dinilai |
|---------|------------------------|
| **Kebenaran Kode** | K-Means diimplementasikan dengan benar. Elbow method dan/atau silhouette score digunakan untuk menentukan k optimal. PCA diterapkan dan explained variance ratio dihitung. Visualisasi cluster (2D/3D). |
| **Analisis & Interpretasi** | Mengapa memilih k=N? Apa karakteristik setiap cluster? Bagaimana cluster bisa diterjemahkan ke segmen bisnis? Berapa komponen PCA yang diperlukan untuk 95% variance? |
| **Kualitas Kode** | Penggunaan `KMeans`, `PCA`, `silhouette_score`. Scatter plot clusters dengan centroid. Elbow plot dan cumulative explained variance plot. |
| **Dokumentasi** | Sections: Data Preparation --> Scaling --> Elbow/Silhouette --> Clustering --> PCA --> Interpretation --> Conclusion |
| **AI Log** | Dokumentasi jika menggunakan AI untuk interpretasi cluster |

---

### Tugas 5 (T5): Natural Language Processing pada Teks Bahasa Indonesia
**Minggu:** 12 | **CPMK:** CPMK-5

| Dimensi | Poin Kunci yang Dinilai |
|---------|------------------------|
| **Kebenaran Kode** | Text preprocessing benar (tokenization, stopwords removal untuk Bahasa Indonesia, TF-IDF). Model NLP (Naive Bayes/SVM) diimplementasikan. Evaluasi model NLP benar. |
| **Analisis & Interpretasi** | Bagaimana preprocessing mempengaruhi hasil? Kata-kata mana yang paling penting (top TF-IDF features)? Analisis kesalahan model: teks mana yang salah diklasifikasikan dan mengapa? |
| **Kualitas Kode** | Penggunaan `TfidfVectorizer`, `CountVectorizer`, Pipeline NLP. Word cloud atau visualisasi frekuensi kata. Handling teks Bahasa Indonesia (stopwords). |
| **Dokumentasi** | Sections: Dataset Description --> Text Preprocessing --> Feature Extraction --> Modeling --> Error Analysis --> Conclusion |
| **AI Log** | Dokumentasi jika menggunakan AI untuk memahami NLP concepts atau preprocessing teks Indonesia |

---

### Tugas 6 (T6): Etika AI & Responsible ML Pipeline
**Minggu:** 14 | **CPMK:** CPMK-6, CPMK-7

| Dimensi | Poin Kunci yang Dinilai |
|---------|------------------------|
| **Kebenaran Kode** | Audit bias pada model yang sudah dibangun. Metrik fairness dihitung (demographic parity, equal opportunity). Pipeline end-to-end yang reproducible. Model interpretability (feature importance, SHAP jika memungkinkan). |
| **Analisis & Interpretasi** | Apakah model bias terhadap kelompok tertentu? Bagaimana mitigasi bias? Refleksi tentang dampak sosial model. Integrasi nilai-nilai Islam (amanah, adalah) dalam pipeline ML. |
| **Kualitas Kode** | Pipeline lengkap dari data load hingga evaluasi. Kode audit fairness. Visualisasi feature importance. Dokumentasi lengkap setiap langkah. |
| **Dokumentasi** | Sections: Problem Statement --> Pipeline Design --> Bias Audit --> Fairness Metrics --> Mitigation --> Ethical Reflection --> Conclusion |
| **AI Log** | Dokumentasi penggunaan AI secara keseluruhan selama tugas. Refleksi komprehensif tentang peran AI sebagai partner. |

---

## Panduan Submission

### Format Pengumpulan

| Komponen | Detail |
|----------|--------|
| **Format file** | Jupyter Notebook (.ipynb) yang sudah dijalankan semua cell-nya |
| **Nama file** | `T[N]_NIM_NamaLengkap.ipynb` (misal: `T1_12345_AhmadFauzi.ipynb`) |
| **Platform** | Upload via LMS UAI |
| **Deadline** | 1 minggu setelah tugas diberikan, pukul 23:59 WIB |
| **Keterlambatan** | Pengurangan 10% per hari keterlambatan (maks 3 hari) |

### Checklist Sebelum Submit

- [ ] Notebook berjalan dari awal sampai akhir tanpa error (Restart & Run All)
- [ ] Semua visualisasi terlihat
- [ ] Setiap code cell memiliki penjelasan markdown di atasnya
- [ ] AI Usage Log lengkap (di section terakhir notebook)
- [ ] Nama dan NIM tertulis di cell pertama
- [ ] Semua library yang diperlukan di-import di cell awal
- [ ] Kode menggunakan comment dalam Bahasa Indonesia
- [ ] Dataset disertakan atau link ke dataset dicantumkan

### Panduan Revisi (Bonus)

Mahasiswa yang **merevisi tugas** berdasarkan feedback dosen (dalam 1 minggu setelah feedback diberikan) mendapat **bonus 5% dari nilai tugas tersebut**. Revisi harus jelas menunjukkan perubahan yang dilakukan.

---

## Panduan untuk Mahasiswa

### Cara Mendapat Nilai Maksimal

1. **Jangan hanya menjalankan kode** — Jelaskan apa yang dilakukan dan MENGAPA
2. **Interpretasi > Angka** — Output `classification_report` tanpa interpretasi = setengah nilai
3. **Konteks Indonesia** — Hubungkan temuan dengan situasi riil di Indonesia
4. **Dokumentasi AI** — Jika pakai AI, dokumentasikan dengan jujur (nilai amanah)
5. **Review sebelum submit** — Restart & Run All, pastikan tidak ada error
6. **Struktur notebook rapi** — Gunakan markdown headings, narasi yang connecting

### Kesalahan Umum yang Mengurangi Nilai

- Hanya menempel output tanpa interpretasi
- Copy-paste kode tanpa memahami apa yang dilakukan
- Tidak melakukan preprocessing sebelum modeling
- Tidak melakukan train-test split (data leakage)
- Menggunakan accuracy saja untuk dataset imbalanced
- Notebook tanpa struktur (langsung code tanpa markdown)
- Tidak mendokumentasikan penggunaan AI
- Tidak menangani missing values atau outliers
- Tidak melakukan feature scaling sebelum KNN/SVM

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
