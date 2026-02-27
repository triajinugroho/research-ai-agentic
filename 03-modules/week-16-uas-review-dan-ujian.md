# Minggu 16: Review dan Ujian Akhir Semester (UAS)

## Mata Kuliah: Analisis Data Statistik
### Prodi Informatika — Universitas Al Azhar Indonesia — Semester Genap 2025/2026

---

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Minggu** | 16 |
| **Topik** | Review Komprehensif dan UAS |
| **CPMK** | CPMK 1-7 (Komprehensif, penekanan CPMK 5-7) |
| **Bloom's Taxonomy** | C4-C6 (Analyze, Evaluate, Create) |
| **Format UAS** | Closed-book + 1 lembar A4 catatan pribadi (ditulis tangan) |
| **Durasi UAS** | 100 menit |
| **Cakupan** | Minggu 9-15 (dengan dasar pemahaman Minggu 1-7) |

---

## Tujuan Pembelajaran

Modul review ini membantu mahasiswa untuk:

1. **Merangkum** seluruh materi semester dalam satu kerangka konseptual yang utuh
2. **Mengidentifikasi** hubungan antar topik dari Minggu 9 hingga Minggu 15
3. **Mengevaluasi** penguasaan masing-masing CPMK melalui checklist mandiri
4. **Berlatih** dengan soal-soal yang mewakili format UAS
5. **Menyusun** strategi persiapan UAS yang efektif

---

## 1. Ringkasan Materi Minggu 9-15

### 1.1 Peta Konsep: Minggu 9-15

```
                    ┌──────────────────────────────┐
                    │  ANALISIS DATA STATISTIK     │
                    │  (Minggu 9-15)               │
                    └──────────┬───────────────────┘
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
    ┌───────▼───────┐  ┌──────▼───────┐  ┌──────▼───────────┐
    │ HUBUNGAN      │  │ PERBANDINGAN │  │ ADVANCED &       │
    │ ANTAR VARIABEL│  │ KELOMPOK     │  │ AI-AUGMENTED     │
    │ (Mg 9-10)     │  │ (Mg 11-12)   │  │ (Mg 13-14)       │
    └───────┬───────┘  └──────┬───────┘  └──────┬───────────┘
            │                  │                  │
    ┌───────▼───────┐  ┌──────▼───────┐  ┌──────▼───────────┐
    │- Korelasi     │  │- One-way     │  │- Decision Tree   │
    │  (Pearson,    │  │  ANOVA       │  │- k-NN            │
    │  Spearman)    │  │- Post-hoc    │  │- Train/Test Split│
    │- Regresi      │  │  (Tukey HSD) │  │- Cross-Validation│
    │  Linear       │  │- Non-param   │  │- Confusion Matrix│
    │  Sederhana    │  │  (Mann-W,    │  │- Precision/Recall│
    │- Regresi      │  │  Kruskal-W)  │  │- AI Co-Analyst   │
    │  Berganda     │  │- Chi-Square  │  │- Prompt Eng.     │
    │- R², Adj R²   │  │- Logistic    │  │- Etika AI        │
    │- Diagnostik   │  │  Regression  │  │                   │
    │  Residual     │  │- Odds Ratio  │  │                   │
    └───────────────┘  └──────────────┘  └───────────────────┘
            │                  │                  │
            └──────────────────┼──────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │  PROYEK AKHIR       │
                    │  (Minggu 15)        │
                    │  Integrasi semua    │
                    │  metode di atas     │
                    └─────────────────────┘
```

### 1.2 Ringkasan per Minggu

#### Minggu 9: Korelasi dan Regresi Linear Sederhana

| Konsep | Detail Kunci |
|--------|-------------|
| **Korelasi Pearson** | Mengukur hubungan linear, range -1 sampai +1, asumsi: data kontinu & normal |
| **Korelasi Spearman** | Mengukur hubungan monoton (rank-based), tidak butuh normalitas |
| **Correlation ≠ Causation** | Korelasi tidak membuktikan sebab-akibat |
| **Regresi Linear Sederhana** | y = b0 + b1*x, b1 = slope, b0 = intercept |
| **R-squared** | Proporsi varians y yang dijelaskan oleh model (0-1) |
| **sklearn & statsmodels** | Dua library utama untuk regresi di Python |

#### Minggu 10: Regresi Berganda dan Evaluasi Model

| Konsep | Detail Kunci |
|--------|-------------|
| **Regresi Berganda** | y = b0 + b1*x1 + b2*x2 + ... + bp*xp |
| **Interpretasi koefisien** | "Kenaikan 1 unit x1 → kenaikan b1 unit y, dengan variabel lain konstan" |
| **Adjusted R-squared** | R² yang dipenalti untuk jumlah prediktor, lebih reliable untuk model comparison |
| **Diagnostik Residual** | Normalitas residual, homoscedasticity, linearity |
| **Multicollinearity** | Korelasi tinggi antar prediktor, deteksi dengan VIF > 10 |
| **Feature Selection** | Memilih prediktor terbaik untuk model |

#### Minggu 11: ANOVA dan Uji Non-Parametrik

| Konsep | Detail Kunci |
|--------|-------------|
| **One-way ANOVA** | Membandingkan mean dari >= 3 kelompok, asumsi: normalitas + homogenitas varians |
| **F-statistic** | Rasio varians antar kelompok / varians dalam kelompok |
| **Post-hoc Tukey HSD** | Menentukan pasangan kelompok mana yang berbeda signifikan |
| **Mann-Whitney U** | Alternatif non-parametrik untuk 2-sample t-test |
| **Kruskal-Wallis** | Alternatif non-parametrik untuk one-way ANOVA |
| **Decision Tree Pemilihan Uji** | Normal + homogen → ANOVA; Tidak normal → Kruskal-Wallis |

#### Minggu 12: Analisis Data Kategorikal

| Konsep | Detail Kunci |
|--------|-------------|
| **Chi-Square Test** | Uji hubungan antara 2 variabel kategorikal |
| **Contingency Table** | Tabel frekuensi observasi vs expected |
| **Expected Frequency** | E = (Row Total * Column Total) / Grand Total |
| **Chi-Square Statistic** | chi2 = sum((O - E)^2 / E) |
| **Logistic Regression** | Memodelkan probabilitas kelas (output 0/1), menggunakan sigmoid function |
| **Odds Ratio** | exp(coefficient) — berapa kali lipat odds berubah per unit kenaikan prediktor |

#### Minggu 13: Pengantar Machine Learning Statistik

| Konsep | Detail Kunci |
|--------|-------------|
| **Statistik vs ML** | Inference vs prediction, model-driven vs data-driven |
| **Supervised Learning** | Data berlabel, termasuk classification dan regression |
| **Decision Tree** | Pertanyaan berurutan, information gain, bisa divisualisasikan |
| **k-NN** | Voting dari k tetangga terdekat, perlu standardisasi |
| **Train-Test Split** | Pisahkan data (80/20) untuk evaluasi yang realistis |
| **Cross-Validation** | K-fold untuk estimasi performa yang lebih robust |
| **Evaluation Metrics** | Accuracy, precision, recall, F1-score, confusion matrix |

#### Minggu 14: AI-Augmented Data Analysis

| Konsep | Detail Kunci |
|--------|-------------|
| **AI sebagai Co-Analyst** | Mampu: coding, penjelasan, brainstorm. Tidak mampu: judgment, konteks domain, tanggung jawab |
| **Prompt Engineering** | Framework CRIDE: Context, Role, Instruction, Data, Expectation |
| **Workflow Human-AI** | 6 langkah: Define → Draft → Review → Code → Verify → Iterate |
| **Hallucination** | AI bisa mengarang statistik, referensi, atau output yang salah |
| **Dokumentasi AI** | Transparansi wajib: catat prompt, output, modifikasi |
| **Etika Islam & AI** | Amanah (jujur), keadilan (fair), ihsan (keunggulan) |

---

## 2. Ringkasan Keseluruhan Semester: Big Picture

### 2.1 Bagaimana Semua Materi Terhubung

```
SEMESTER 1-7 (FONDASI)                 SEMESTER 9-15 (APLIKASI)
========================               ==========================

Statistik Deskriptif ─────────────────► EDA dalam Regresi & ANOVA
(Minggu 2-3)                           (Minggu 9-11)

Probabilitas & ──────────────────────► Fondasi untuk p-value,
Distribusi (Minggu 4-5)                confidence interval di semua uji

Sampling & Estimasi ─────────────────► Train-Test Split,
(Minggu 6)                             Cross-Validation (Minggu 13)

Uji Hipotesis ───────────────────────► ANOVA, Chi-Square, Koefisien
(Minggu 7)                             Regresi (Minggu 9-12)

                    ┌─────────────┐
                    │   UTS       │
                    │ (Minggu 8)  │
                    └──────┬──────┘
                           │
         Fondasi kuat memungkinkan
         aplikasi yang lebih advanced
                           │
                    ┌──────▼──────┐
Regresi + ANOVA + ─►│   PROYEK    │◄─ Machine Learning +
Chi-Square           │   AKHIR    │   AI-Augmented Analysis
(Minggu 9-12)       │ (Minggu 15)│   (Minggu 13-14)
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │    UAS      │
                    │ (Minggu 16) │
                    └─────────────┘
```

### 2.2 Decision Tree: Memilih Metode Statistik yang Tepat

Salah satu skill terpenting yang harus dikuasai untuk UAS adalah **memilih metode yang tepat**. Gunakan pohon keputusan berikut:

```
PERTANYAAN PENELITIAN
│
├── Apakah ingin melihat HUBUNGAN antar variabel?
│   │
│   ├── Kedua variabel NUMERIK?
│   │   ├── Hubungan LINEAR → Korelasi Pearson + Regresi Linear
│   │   └── Hubungan MONOTON (non-linear) → Korelasi Spearman
│   │
│   ├── Dependen NUMERIK, Independen KATEGORIKAL?
│   │   ├── 2 kelompok → t-test (atau Mann-Whitney)
│   │   └── >= 3 kelompok → ANOVA (atau Kruskal-Wallis)
│   │
│   ├── Dependen KATEGORIKAL, Independen KATEGORIKAL?
│   │   └── Chi-Square Test of Independence
│   │
│   └── Dependen BINER (0/1), Independen NUMERIK/CAMPURAN?
│       └── Logistic Regression
│
├── Apakah ingin MEMPREDIKSI?
│   │
│   ├── Target NUMERIK → Regresi Linear (sederhana/berganda)
│   └── Target KATEGORIKAL → Decision Tree, k-NN, Logistic Regression
│
└── Apakah ingin MEMBANDINGKAN kelompok?
    │
    ├── 2 kelompok, data NORMAL → t-test
    ├── 2 kelompok, data TIDAK NORMAL → Mann-Whitney U
    ├── >= 3 kelompok, data NORMAL + homogen → ANOVA + Tukey HSD
    └── >= 3 kelompok, asumsi tidak terpenuhi → Kruskal-Wallis
```

---

## 3. Checklist per CPMK: Apa yang Harus Dikuasai

Gunakan checklist ini untuk self-assessment. Tandai setiap item yang sudah Anda kuasai.

### CPMK-1: Peran Statistika dan Etika (Minggu 1)

```
[ ] Menjelaskan mengapa statistik penting di era data science dan AI
[ ] Mengidentifikasi perbedaan tipe data (nominal, ordinal, interval, rasio)
[ ] Memahami prinsip etika data: privacy, bias, consent
[ ] Menjelaskan konsep responsible AI
```

### CPMK-2: Statistika Deskriptif dan Visualisasi (Minggu 2-3)

```
[ ] Menghitung mean, median, modus, range, variance, std, IQR
[ ] Menggunakan pandas: describe(), info(), value_counts()
[ ] Membuat visualisasi: histogram, scatter, box plot, bar, heatmap
[ ] Menerapkan prinsip storytelling with data
```

### CPMK-3: Probabilitas dan Distribusi (Minggu 4-5)

```
[ ] Menghitung probabilitas dasar dan conditional probability
[ ] Menerapkan Bayes' theorem
[ ] Menjelaskan distribusi Normal, Binomial, Poisson
[ ] Memahami dan mendemonstrasikan Central Limit Theorem
```

### CPMK-4: Inferensi Statistik (Minggu 6-7)

```
[ ] Menghitung confidence interval
[ ] Merumuskan H0 dan H1 dengan benar
[ ] Melakukan z-test dan t-test (one-sample, two-sample, paired)
[ ] Menginterpretasi p-value dengan benar
[ ] Menjelaskan Type I/II error dan effect size
```

### CPMK-5: Korelasi dan Regresi (Minggu 9-10) -- FOKUS UAS

```
[ ] Menghitung dan menginterpretasi korelasi Pearson dan Spearman
[ ] Membangun model regresi linear sederhana dan menginterpretasi koefisien
[ ] Membangun model regresi berganda
[ ] Mengevaluasi model: R², adjusted R², residual plot
[ ] Mendeteksi multicollinearity (VIF)
[ ] Memahami correlation ≠ causation
```

### CPMK-6: ANOVA, Non-Parametrik, Kategorikal (Minggu 11-12) -- FOKUS UAS

```
[ ] Melakukan one-way ANOVA dan menginterpretasi F-statistic
[ ] Menjalankan post-hoc test (Tukey HSD)
[ ] Memilih antara parametrik vs non-parametrik berdasarkan asumsi
[ ] Melakukan Chi-Square test dan menghitung expected frequency
[ ] Membangun logistic regression sederhana
[ ] Menginterpretasi odds ratio
```

### CPMK-7: ML dan AI-Augmented Analysis (Minggu 13-14) -- FOKUS UAS

```
[ ] Membedakan paradigma statistik tradisional vs machine learning
[ ] Membangun model Decision Tree dan k-NN
[ ] Melakukan train-test split dan cross-validation
[ ] Menghitung dan menginterpretasi accuracy, precision, recall, F1
[ ] Membaca dan menginterpretasi confusion matrix
[ ] Menggunakan AI sebagai co-analyst secara bertanggung jawab
[ ] Mengevaluasi output AI secara kritis
[ ] Memahami prinsip etika AI dalam riset
```

---

## 4. Contoh Soal Latihan UAS

### Format UAS

| Bagian | Jumlah Soal | Bobot | Bloom's |
|--------|-------------|-------|---------|
| A. Pilihan Ganda Konseptual | 8 soal | 15% | C2-C4 |
| B. Hitungan dan Interpretasi | 3 soal | 30% | C3-C4 |
| C. Interpretasi Output | 3 soal | 25% | C4-C5 |
| D. Essay: Desain Analisis | 1 soal | 30% | C5-C6 |

> **Ingat:** UAS bersifat closed-book + 1 lembar A4 catatan pribadi (ditulis tangan). Siapkan catatan Anda dengan strategis!

---

### Bagian A: Pilihan Ganda Konseptual (Contoh)

**Soal 1.** Seorang peneliti mendapatkan R-squared = 0.85 dari model regresi linear berganda dengan 3 prediktor. Pernyataan mana yang **paling tepat**?

a) 85% variabel independen menjelaskan variabel dependen
b) 85% varians variabel dependen dapat dijelaskan oleh model
c) Ada hubungan kausal 85% antara prediktor dan variabel dependen
d) 85% data cocok dengan garis regresi

**Jawaban: b)** R-squared mengukur proporsi varians variabel dependen yang dapat dijelaskan oleh model regresi. Bukan tentang kausalitas (c) dan bukan tentang variabel independen itu sendiri (a).

---

**Soal 2.** Dalam konteks ANOVA, jika nilai F-statistic sangat besar, ini menunjukkan:

a) Varians di dalam kelompok jauh lebih besar dari varians antar kelompok
b) Varians antar kelompok jauh lebih besar dari varians di dalam kelompok
c) Semua kelompok memiliki mean yang sama
d) Data tidak berdistribusi normal

**Jawaban: b)** F = MSB / MSW (varians antar kelompok / varians dalam kelompok). F besar berarti perbedaan antar kelompok jauh lebih besar dibanding variabilitas di dalam kelompok, menunjukkan setidaknya satu kelompok berbeda signifikan.

---

**Soal 3.** Seorang mahasiswa ingin membandingkan performa model klasifikasi untuk mendeteksi email spam. Metrik mana yang paling tepat digunakan jika prioritas utamanya adalah **meminimalkan email penting yang masuk ke folder spam**?

a) Accuracy
b) Precision
c) Recall
d) F1-Score

**Jawaban: b)** Email penting yang masuk ke folder spam adalah False Positive (diprediksi spam padahal bukan). Precision = TP / (TP + FP) — memaksimalkan precision berarti meminimalkan False Positive.

---

### Bagian B: Hitungan dan Interpretasi (Contoh)

**Soal 4. Interpretasi Regresi (10%)**

Diberikan output regresi linear berganda berikut untuk memprediksi nilai IPK mahasiswa:

```
Variable          Coefficient    Std Error    t-stat    p-value
-----------------------------------------------------------
Intercept         1.250          0.320        3.906     0.000
jam_belajar       0.085          0.015        5.667     0.000
kehadiran (%)     0.012          0.004        3.000     0.003
jam_medsos        -0.043         0.020       -2.150     0.034

R-squared: 0.68    Adjusted R-squared: 0.66
F-statistic: 42.50    p-value (F): 0.000
n = 150
```

**Pertanyaan:**

a) Tuliskan persamaan regresi dari output di atas.

b) Interpretasikan koefisien variabel `jam_belajar` dalam konteks masalah.

c) Apakah variabel `jam_medsos` signifikan pada alpha = 0.05? Apa artinya?

d) Interpretasikan R-squared dan Adjusted R-squared. Apa perbedaan keduanya?

e) Seorang mahasiswa belajar 20 jam/minggu, kehadiran 90%, dan menghabiskan 10 jam/minggu di media sosial. Berapa prediksi IPK-nya?

**Jawaban:**

a) IPK = 1.250 + 0.085(jam_belajar) + 0.012(kehadiran) - 0.043(jam_medsos)

b) Dengan variabel lain konstan, setiap penambahan 1 jam belajar per minggu, IPK diprediksi meningkat sebesar 0.085 poin. Hubungan ini signifikan secara statistik (p < 0.001).

c) Ya, signifikan (p = 0.034 < 0.05). Koefisien negatif menunjukkan bahwa semakin banyak jam di media sosial, IPK cenderung menurun — setiap penambahan 1 jam medsos, IPK diprediksi turun 0.043 poin, dengan variabel lain konstan.

d) R-squared = 0.68 berarti 68% varians IPK dapat dijelaskan oleh ketiga prediktor secara bersama-sama. Adjusted R-squared = 0.66 memperhitungkan jumlah prediktor dalam model — lebih conservative dan lebih tepat untuk membandingkan model dengan jumlah prediktor berbeda.

e) IPK = 1.250 + 0.085(20) + 0.012(90) - 0.043(10)
   IPK = 1.250 + 1.700 + 1.080 - 0.430
   IPK = 3.600

---

**Soal 5. ANOVA Decision (10%)**

Seorang dosen ingin mengetahui apakah ada perbedaan rata-rata nilai ujian antara 4 kelas (A, B, C, D). Hasil pengecekan asumsi menunjukkan:

- Shapiro-Wilk test: semua kelas p > 0.05 (data normal)
- Levene's test: p = 0.012

**Pertanyaan:**

a) Berdasarkan hasil pengecekan asumsi, apakah ANOVA tepat digunakan? Jelaskan.

b) Jika Levene's test signifikan, uji alternatif apa yang bisa digunakan? Mengapa?

c) Misalkan Anda tetap melakukan ANOVA dan mendapatkan F(3, 116) = 4.82, p = 0.003. Langkah apa yang harus dilakukan selanjutnya?

**Jawaban:**

a) ANOVA membutuhkan 2 asumsi utama: normalitas dan homogenitas varians. Normalitas terpenuhi (Shapiro-Wilk p > 0.05 untuk semua kelas). Namun, homogenitas varians TIDAK terpenuhi (Levene's p = 0.012 < 0.05). Secara ketat, ANOVA standar kurang tepat karena asumsi homogenitas dilanggar.

b) Alternatif: (1) Welch's ANOVA — varian ANOVA yang tidak mengasumsikan homogenitas varians, menggunakan `scipy.stats.f_oneway` tidak mengoreksi ini, perlu library pingouin atau implementasi manual. (2) Kruskal-Wallis — uji non-parametrik yang tidak membutuhkan asumsi normalitas maupun homogenitas varians. Kruskal-Wallis lebih aman jika kedua asumsi dipertanyakan.

c) Karena p = 0.003 < 0.05, kita menolak H0 (rata-rata semua kelompok sama). Artinya, setidaknya satu pasangan kelas memiliki rata-rata yang berbeda secara signifikan. Langkah selanjutnya: **post-hoc test** (misal Tukey HSD) untuk menentukan pasangan kelas mana yang berbeda. Juga perlu menghitung effect size (eta-squared) untuk menilai practical significance.

---

**Soal 6. Chi-Square Computation (10%)**

Sebuah survei terhadap 200 mahasiswa menanyakan preferensi metode belajar (Online vs Offline) berdasarkan jurusan (Informatika vs Manajemen). Berikut data yang diperoleh:

| | Online | Offline | Total |
|--|--------|---------|-------|
| **Informatika** | 60 | 40 | 100 |
| **Manajemen** | 35 | 65 | 100 |
| **Total** | 95 | 105 | 200 |

**Pertanyaan:**

a) Rumuskan H0 dan H1 untuk uji chi-square test of independence.

b) Hitung expected frequency untuk setiap sel.

c) Hitung chi-square statistic.

d) Dengan df = 1 dan chi-square critical value (alpha=0.05) = 3.84, apa kesimpulan Anda?

**Jawaban:**

a)
- H0: Tidak ada hubungan antara jurusan dan preferensi metode belajar (variabel independen)
- H1: Ada hubungan antara jurusan dan preferensi metode belajar (variabel tidak independen)

b) Expected frequency = (Row Total x Column Total) / Grand Total

| | Online | Offline |
|--|--------|---------|
| **Informatika** | (100x95)/200 = 47.5 | (100x105)/200 = 52.5 |
| **Manajemen** | (100x95)/200 = 47.5 | (100x105)/200 = 52.5 |

c) chi2 = sum((O - E)^2 / E)

chi2 = (60-47.5)^2/47.5 + (40-52.5)^2/52.5 + (35-47.5)^2/47.5 + (65-52.5)^2/52.5

chi2 = (12.5)^2/47.5 + (-12.5)^2/52.5 + (-12.5)^2/47.5 + (12.5)^2/52.5

chi2 = 156.25/47.5 + 156.25/52.5 + 156.25/47.5 + 156.25/52.5

chi2 = 3.289 + 2.976 + 3.289 + 2.976

chi2 = 12.53

d) chi2 hitung (12.53) > chi2 tabel (3.84), maka kita **menolak H0**. Kesimpulan: terdapat hubungan yang signifikan antara jurusan dan preferensi metode belajar pada alpha = 0.05. Mahasiswa Informatika cenderung lebih memilih belajar online, sementara mahasiswa Manajemen cenderung memilih offline.

---

### Bagian C: Interpretasi Output (Contoh)

**Soal 7. ML Evaluation Metrics (8%)**

Berikut adalah confusion matrix dan classification report dari model Decision Tree untuk klasifikasi 3 jenis buah (Apel, Jeruk, Mangga):

```
Confusion Matrix:
              Predicted
              Apel  Jeruk  Mangga
Actual Apel  [ 18     2      0   ]
       Jeruk [  3    14      3   ]
       Mangga[  1     2     17   ]

Classification Report:
              precision    recall  f1-score   support
       Apel       0.82      0.90      0.86        20
      Jeruk       0.78      0.70      0.74        20
     Mangga       0.85      0.85      0.85        20

    accuracy                          0.82        60
   macro avg      0.82      0.82      0.81        60
weighted avg      0.82      0.82      0.81        60
```

**Pertanyaan:**

a) Model paling sering salah mengklasifikasikan buah apa? Jelaskan berdasarkan confusion matrix.

b) Untuk kelas "Jeruk", jelaskan arti precision = 0.78 dan recall = 0.70 dalam konteks masalah ini.

c) Jika Anda diminta meningkatkan performa model, strategi apa yang bisa dicoba?

**Jawaban:**

a) Model paling sering salah mengklasifikasikan **Jeruk**. Dari 20 jeruk sebenarnya, 3 salah diprediksi sebagai Apel dan 3 salah diprediksi sebagai Mangga (total 6 misklasifikasi, recall hanya 0.70). Ini terlihat dari baris Jeruk pada confusion matrix yang menunjukkan kesalahan paling banyak.

b) Precision 0.78 untuk Jeruk: dari semua buah yang diprediksi sebagai Jeruk (14 + 2 + 2 = 18), 78% di antaranya benar-benar Jeruk. Recall 0.70 untuk Jeruk: dari semua buah yang sebenarnya Jeruk (20 buah), hanya 70% yang berhasil terdeteksi sebagai Jeruk oleh model (14 dari 20). Model "melewatkan" 30% jeruk.

c) Strategi yang bisa dicoba: (1) Menyesuaikan hyperparameter, misal menambah `max_depth` pada Decision Tree. (2) Menambah fitur yang bisa membedakan Jeruk dari buah lain. (3) Mencoba algoritma lain seperti k-NN atau Random Forest. (4) Mengecek apakah data training seimbang untuk semua kelas. (5) Melakukan feature engineering atau menambah data training, khususnya untuk kelas Jeruk.

---

**Soal 8. Interpretasi Output Regresi (8%)**

Diberikan residual plot dari model regresi linear:

```
Residual Plot:
       |           *        *
   2   |     *   *   *  *        *
       |  *    *    *   *   *
   0   |----*---*---*----*---*---*---
       |   * *    *    *  *     *
  -2   |     *      *         *
       |           *
       +---+---+---+---+---+---+---
           Predicted Values →
```

**Pertanyaan:** Berdasarkan residual plot di atas, apakah asumsi regresi linear terpenuhi? Jelaskan 2 asumsi yang bisa dievaluasi dari plot ini.

**Jawaban:**

Dari residual plot ini, kita bisa mengevaluasi 2 asumsi:

1. **Linearity:** Residual sebaiknya tersebar acak di sekitar garis 0, tanpa pola sistematis. Dari plot di atas, residual terlihat tersebar cukup acak tanpa pola kurva (melengkung), sehingga asumsi linearitas tampak terpenuhi.

2. **Homoscedasticity (constant variance):** Sebaran residual sebaiknya memiliki lebar yang relatif konstan sepanjang sumbu predicted values. Dari plot di atas, sebaran terlihat cukup konstan (tidak ada pola "corong" yang melebar atau menyempit), sehingga asumsi homoscedasticity tampak terpenuhi.

Secara keseluruhan, berdasarkan residual plot ini, asumsi regresi linear tampak terpenuhi dengan cukup baik.

---

**Soal 9. Evaluasi Output AI (9%)**

Seorang mahasiswa menggunakan AI untuk membantu analisis dan mendapatkan output berikut:

> "Berdasarkan analisis, ditemukan korelasi Pearson r = 0.92 antara jumlah es krim yang terjual dan jumlah kasus tenggelam per bulan. Dengan p-value < 0.001, kita dapat menyimpulkan bahwa menjual es krim **menyebabkan** peningkatan kasus tenggelam. Oleh karena itu, disarankan untuk membatasi penjualan es krim di musim panas."

**Pertanyaan:**

a) Identifikasi kesalahan interpretasi dalam output AI ini.

b) Apa penjelasan yang lebih tepat untuk korelasi ini?

c) Apa pelajaran dari kasus ini tentang penggunaan AI?

**Jawaban:**

a) Kesalahan utama: AI menyimpulkan **kausalitas** dari korelasi. Pernyataan "menjual es krim menyebabkan peningkatan kasus tenggelam" adalah salah. Korelasi tinggi (r = 0.92) dan p-value signifikan TIDAK membuktikan hubungan sebab-akibat. Rekomendasi kebijakan berdasarkan kausalitas palsu ini berbahaya.

b) Penjelasan yang lebih tepat: keduanya dipengaruhi oleh **variabel tersembunyi (confounding variable)** — yaitu suhu/cuaca panas. Saat cuaca panas, penjualan es krim meningkat DAN aktivitas berenang meningkat (sehingga risiko tenggelam naik). Hubungan antara es krim dan tenggelam bersifat **spurious correlation**.

c) Pelajaran: (1) AI bisa menghasilkan interpretasi yang terdengar meyakinkan tapi secara logika salah. (2) Prinsip "correlation ≠ causation" harus selalu diterapkan saat mengevaluasi output AI. (3) Manusia perlu memiliki **critical thinking** untuk menilai apakah kesimpulan AI masuk akal secara logis dan domain knowledge.

---

### Bagian D: Essay — Desain Analisis (Contoh)

**Soal 10. Design an Analysis Plan (30%)**

Sebuah perusahaan e-commerce di Indonesia ingin memahami faktor-faktor yang mempengaruhi keputusan pelanggan untuk melakukan pembelian ulang (repeat purchase). Mereka memiliki dataset dengan variabel berikut:

| Variabel | Tipe | Deskripsi |
|----------|------|-----------|
| `repeat_purchase` | Binary (0/1) | Apakah pelanggan membeli ulang dalam 3 bulan |
| `total_spending` | Numerik | Total pengeluaran di transaksi pertama (Rupiah) |
| `satisfaction_score` | Numerik | Skor kepuasan pelanggan (1-10) |
| `delivery_time` | Numerik | Waktu pengiriman (hari) |
| `product_category` | Kategorikal | Elektronik / Fashion / Makanan / Rumah Tangga |
| `payment_method` | Kategorikal | Transfer / E-wallet / COD |
| `age_group` | Kategorikal | <25 / 25-35 / 36-50 / >50 |
| `gender` | Binary | Male / Female |

n = 500 pelanggan

**Pertanyaan:** Rancang rencana analisis data end-to-end untuk menjawab pertanyaan: "Faktor apa yang paling mempengaruhi keputusan repeat purchase?" Rencana harus mencakup:

a) Eksplorasi data apa yang akan Anda lakukan? (sebutkan minimal 3 langkah spesifik)

b) Uji statistik apa yang akan Anda gunakan? Jelaskan mengapa untuk masing-masing uji.

c) Jika Anda ingin membangun model prediktif, metode ML apa yang tepat? Bagaimana cara mengevaluasinya?

d) Bagaimana Anda akan menggunakan AI sebagai co-analyst dalam proses ini? Sebutkan 2 prompt spesifik yang akan Anda gunakan.

e) Apa limitasi dari analisis ini?

**Jawaban (Contoh jawaban yang baik):**

a) **Eksplorasi Data:**
1. Statistik deskriptif untuk semua variabel — mean, median, std untuk numerik; frekuensi untuk kategorikal. Cek distribusi `repeat_purchase` (seberapa balanced kelas 0 dan 1).
2. Visualisasi hubungan: box plot `satisfaction_score` per `repeat_purchase`, bar chart proporsi repeat purchase per `product_category`, scatter plot `total_spending` vs `satisfaction_score` dengan warna berdasarkan repeat purchase.
3. Korelasi matrix untuk variabel numerik — identifikasi multicollinearity potensial. Cross-tabulation `product_category` x `repeat_purchase` untuk melihat pola.

b) **Uji Statistik:**
- **Chi-Square test:** Untuk menguji hubungan antara variabel kategorikal (product_category, payment_method, age_group, gender) dengan repeat_purchase (kategorikal). Alasan: kedua variabel bersifat kategorikal.
- **t-test atau Mann-Whitney:** Untuk membandingkan rata-rata total_spending, satisfaction_score, dan delivery_time antara kelompok repeat (1) vs non-repeat (0). Alasan: membandingkan 2 kelompok pada variabel numerik. Pilih Mann-Whitney jika data tidak normal.
- **Logistic Regression:** Untuk memodelkan probabilitas repeat_purchase berdasarkan seluruh prediktor secara simultan. Alasan: variabel dependen bersifat biner (0/1), dan kita ingin mengetahui kontribusi relatif setiap prediktor melalui odds ratio.

c) **Model Prediktif:**
- **Metode:** Logistic Regression (baseline, interpretable) dan Decision Tree (untuk comparison, lebih mudah divisualisasikan).
- **Evaluasi:** Train-test split 80/20 dengan stratify. Metrik utama: **precision dan recall** karena jika kelas imbalanced, accuracy bisa menyesatkan. F1-score sebagai metrik keseimbangan. Confusion matrix untuk melihat detail kesalahan. 5-fold cross-validation untuk estimasi performa yang robust.

d) **Penggunaan AI sebagai Co-Analyst:**
- Prompt 1: "Saya memiliki dataset e-commerce dengan 500 pelanggan. Variabel dependen saya adalah repeat_purchase (binary). Saya sudah melakukan chi-square test dan mendapatkan p-value yang signifikan untuk product_category. Bantu saya menginterpretasi odds ratio dari logistic regression dan jelaskan bagaimana cara mengkonversi coefficient menjadi odds ratio di Python menggunakan statsmodels."
- Prompt 2: "Saya membangun Decision Tree dan Logistic Regression untuk memprediksi repeat purchase. Decision Tree accuracy = 0.78, Logistic Regression accuracy = 0.82. Tapi Decision Tree recall untuk kelas 1 lebih tinggi. Bantu saya memutuskan model mana yang lebih baik, pertimbangkan konteks bisnis di mana kita ingin mengidentifikasi pelanggan yang berpotensi repeat."

e) **Limitasi:**
- Data hanya 500 pelanggan — mungkin tidak cukup untuk generalisasi ke seluruh populasi pelanggan
- Tidak ada informasi tentang faktor psikologis (brand loyalty, pengalaman customer service) yang bisa mempengaruhi repeat purchase
- Correlation ≠ causation — kita bisa menemukan faktor yang berkorelasi tapi belum tentu menyebabkan repeat purchase
- Potensi selection bias — 500 pelanggan ini mungkin tidak representatif
- Model hanya melihat data historis, tidak mempertimbangkan perubahan tren ke depan

---

## 5. Tips Menghadapi UAS

### 5.1 Strategi Persiapan

| Kapan | Apa yang Dilakukan |
|-------|-------------------|
| **1 minggu sebelum** | Review semua materi Minggu 9-14, buat ringkasan per topik |
| **3-4 hari sebelum** | Kerjakan soal latihan di atas, identifikasi area lemah |
| **1-2 hari sebelum** | Buat lembar catatan A4 (lihat panduan di bawah), review area lemah |
| **Malam sebelumnya** | Tidur cukup! Otak yang istirahat berpikir lebih jernih |
| **Pagi hari H** | Baca sekilas lembar catatan, datang tepat waktu |

### 5.2 Panduan Membuat Lembar Catatan A4

Anda diperbolehkan membawa **1 lembar A4 catatan** (bolak-balik, ditulis tangan). Berikut saran isi yang strategis:

**Halaman Depan:**
- Decision tree pemilihan metode statistik (lihat bagian 2.2)
- Rumus kunci: korelasi, regresi, chi-square, F-statistic
- Definisi penting: R-squared, adjusted R-squared, VIF, odds ratio, precision, recall, F1

**Halaman Belakang:**
- Checklist asumsi per uji (ANOVA: normalitas + homogenitas; chi-square: expected freq >= 5; dll.)
- Template interpretasi: "Koefisien b1 berarti...", "P-value < 0.05 berarti..."
- Confusion matrix template dan rumus precision/recall
- Perbandingan: kapan pakai Pearson vs Spearman, ANOVA vs Kruskal-Wallis, t-test vs Mann-Whitney

> **Tips:** Tulis tangan dengan rapi — proses menulis sendiri sudah merupakan bentuk belajar. Gunakan warna dan highlight untuk item-item kunci.

### 5.3 Tips Saat Ujian

1. **Baca semua soal** terlebih dahulu — alokasikan waktu proporsional sesuai bobot
2. **Mulai dari soal yang paling dikuasai** — bangun momentum dan kepercayaan diri
3. **Tunjukkan proses berpikir** — di soal hitungan dan essay, langkah-langkah mendapat nilai
4. **Interpretasi = nilai tinggi** — jangan hanya hitung angka, selalu jelaskan artinya
5. **Soal essay:** Gunakan struktur yang jelas (numbering, sub-heading) agar mudah dibaca penilai
6. **Jangan kosongkan jawaban** — jawaban parsial lebih baik dari tidak ada jawaban
7. **Cek waktu** — sisakan 10 menit terakhir untuk review

---

## 6. Format UAS

| Komponen | Detail |
|----------|--------|
| **Cakupan** | Minggu 9-15 (CPMK 5-7), dengan pemahaman dasar CPMK 1-4 |
| **Format** | Closed-book + 1 lembar A4 catatan pribadi (ditulis tangan, bolak-balik) |
| **Durasi** | 100 menit |
| **Tipe soal** | PG (15%) + Hitungan & Interpretasi (30%) + Interpretasi Output (25%) + Essay (30%) |
| **Bobot** | 25% dari nilai akhir |
| **Alat yang diizinkan** | Alat tulis, lembar catatan A4, kalkulator (non-programmable) |
| **TIDAK diizinkan** | HP, laptop, AI tools, buku, catatan selain 1 lembar A4 |

---

## 7. Pesan Penutup: Ke Mana Setelah Ini?

### 7.1 Apa yang Sudah Kalian Capai

Selama 16 minggu ini, kalian telah membangun fondasi yang **sangat kuat** dalam analisis data statistik:

- **Berpikir dengan data** — Dari statistik deskriptif hingga machine learning
- **Coding dengan Python** — pandas, numpy, matplotlib, seaborn, scipy, sklearn
- **Berkolaborasi dengan AI** — Secara bertanggung jawab dan beretika
- **Mengkomunikasikan temuan** — Dari visualisasi hingga presentasi
- **Mengambil keputusan berbasis bukti** — Dari p-value hingga evaluation metrics

Ini bukan akhir perjalanan — ini adalah **fondasi** untuk langkah-langkah selanjutnya.

### 7.2 Mata Kuliah Lanjutan di Prodi Informatika UAI

| Mata Kuliah | Hubungan dengan Statistik |
|-------------|--------------------------|
| **Data Mining** | Teknik ML yang lebih advanced (clustering, association rules) |
| **Machine Learning** | Deep learning, neural networks, NLP — fondasi dari Minggu 13 |
| **Big Data Analytics** | Statistik untuk data skala besar (Hadoop, Spark) |
| **Kecerdasan Buatan** | Fondasi probabilistik AI, Bayesian methods |
| **Riset Operasi** | Optimasi berbasis data dan model statistik |
| **Tugas Akhir / Skripsi** | Analisis data PASTI dibutuhkan, apapun topiknya |

### 7.3 Sertifikasi yang Relevan

| Sertifikasi | Provider | Relevansi |
|-------------|----------|-----------|
| **Google Data Analytics Certificate** | Google (Coursera) | Langsung melanjutkan skill yang dipelajari |
| **IBM Data Science Professional Certificate** | IBM (Coursera) | Termasuk ML dan Python advanced |
| **Microsoft Certified: Azure Data Scientist** | Microsoft | Cloud-based data science |
| **SAS Certified Specialist** | SAS | Industri analytics tradisional |
| **TensorFlow Developer Certificate** | Google | Deep learning (lanjutan dari Minggu 13) |

### 7.4 Karir di Bidang Data

| Posisi | Skill Utama | Hubungan dengan Mata Kuliah Ini |
|--------|------------|--------------------------------|
| **Data Analyst** | SQL, Python, Statistik, Visualisasi | Langsung relevan — ini yang kalian pelajari |
| **Business Intelligence Analyst** | Dashboard, SQL, Statistik Deskriptif | Fondasi Minggu 2-3 + visualisasi |
| **Data Scientist** | ML, Statistik Advanced, Python | Minggu 9-13 sebagai fondasi |
| **ML Engineer** | Deep Learning, MLOps, Software Eng | Lanjutan dari Minggu 13 + skill software |
| **Research Analyst** | Inferensi Statistik, Riset | Minggu 4-7 + 9-12 |

### 7.5 Pesan Terakhir

> Statistik bukan tentang angka — statistik adalah tentang **memahami dunia melalui data**. Di era AI, kemampuan ini tidak menjadi kurang penting — justru **lebih penting dari sebelumnya**. AI bisa menghitung, tapi Anda yang memutuskan pertanyaan apa yang perlu dijawab, metode apa yang tepat, dan apa artinya bagi manusia.
>
> Kalian sekarang memiliki fondasi untuk menjadi **data thinkers** — orang yang tidak hanya menggunakan tools, tapi **memahami** mengapa tools itu bekerja dan kapan tools itu menyesatkan.
>
> *Selamat telah menyelesaikan mata kuliah ini. Semoga ilmu yang dipelajari menjadi berkah dan bermanfaat.*
>
> **Barakallahu fiikum.**

---

## Referensi Keseluruhan (Semester)

### Referensi Utama
1. Diez, D. M., Cetinkaya-Rundel, M., & Barr, C. D. (2019). *OpenIntro Statistics (4th ed.)*. OpenIntro.
2. McKinney, W. (2022). *Python for Data Analysis (3rd ed.)*. O'Reilly Media.
3. Downey, A. B. (2021). *Think Stats: Exploratory Data Analysis in Python (2nd ed.)*. O'Reilly Media.

### Referensi Pendukung
4. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning with Applications in Python (ISLP)*. Springer.
5. VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media.
6. Bruce, P., & Bruce, A. (2020). *Practical Statistics for Data Scientists (2nd ed.)*. O'Reilly Media.
7. Muller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*. O'Reilly Media.

### Referensi Online
8. scikit-learn Documentation: [scikit-learn.org](https://scikit-learn.org)
9. pandas Documentation: [pandas.pydata.org](https://pandas.pydata.org)
10. BPS (Badan Pusat Statistik): [bps.go.id](https://bps.go.id)

---

*Modul ini merupakan bagian dari mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia. Semester Genap 2025/2026.*

*Semoga sukses di UAS dan di perjalanan selanjutnya!*
