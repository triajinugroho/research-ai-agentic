# RENCANA TUGAS MAHASISWA (RTM)

## Mata Kuliah: Analisis Data Statistik
### Prodi Informatika — Universitas Al Azhar Indonesia — Semester Genap 2025/2026
### Dosen Pengampu: Tri Aji Nugroho, S.T., M.T.

---

## A. RINGKASAN TUGAS

| No | Tugas | Minggu | Tipe | Bobot | CPMK |
|----|-------|--------|------|-------|------|
| T1 | Eksplorasi Data Deskriptif | 2 | Individu | 2.5% | CPMK-2 |
| T2 | Data Storytelling & Visualisasi | 3 | Individu | 2.5% | CPMK-2 |
| T3 | Simulasi Distribusi & CLT | 5 | Individu | 2.5% | CPMK-3 |
| T4 | Uji Hipotesis pada Data Riil | 7 | Individu | 2.5% | CPMK-4 |
| T5 | Analisis Regresi | 9 | Individu | 2.5% | CPMK-5 |
| T6 | Perbandingan Kelompok (ANOVA/Non-Param) | 11 | Individu | 2.5% | CPMK-6 |
| K1 | Kuis 1: Fondasi (Minggu 1-4) | 4 | Individu | 3.33% | CPMK 1-3 |
| K2 | Kuis 2: Inferensi (Minggu 5-7) | 7 | Individu | 3.33% | CPMK 3-4 |
| K3 | Kuis 3: Pemodelan (Minggu 9-12) | 12 | Individu | 3.34% | CPMK 5-6 |
| PF | Proyek Akhir: Analisis Data End-to-End | 9-15 | Kelompok (2-3) | 25% | CPMK 1-7 |

**Total bobot tugas + kuis + proyek = 50%** (dari 100% total nilai)

---

## B. DETAIL SETIAP TUGAS

---

### TUGAS 1: Eksplorasi Data Deskriptif

**Minggu:** 2 | **Deadline:** Minggu 3 (sebelum kelas) | **Tipe:** Individu | **Bobot:** 2.5%

#### Deskripsi

Mahasiswa memilih satu dataset dari daftar yang disediakan (sumber: BPS Indonesia) dan melakukan eksplorasi data deskriptif lengkap menggunakan Python di Google Colab.

#### Deliverables

1. **Jupyter Notebook (.ipynb)** berisi:
   - Import dan preview dataset (5 baris pertama, info, shape)
   - Statistik deskriptif: mean, median, modus, std, min, max, Q1, Q3, IQR untuk minimal 3 variabel numerik
   - Identifikasi missing values dan outliers
   - Interpretasi tertulis (dalam markdown cell) untuk setiap temuan
2. Upload ke LMS UAI

#### Rubrik Penilaian

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Kelengkapan analisis** (30%) | Semua statistik deskriptif dihitung dengan benar, termasuk outlier detection | Sebagian besar statistik benar, 1-2 minor error | Statistik dasar ada tapi tidak lengkap | Banyak statistik yang hilang atau salah |
| **Kode Python** (25%) | Kode bersih, efisien, well-commented, menggunakan pandas idiomatik | Kode berjalan dengan benar, beberapa comment | Kode berjalan tapi tidak efisien atau tanpa comment | Kode error atau tidak lengkap |
| **Interpretasi** (30%) | Interpretasi mendalam, menghubungkan statistik dengan konteks dataset | Interpretasi benar tapi kurang kontekstual | Interpretasi superfisial atau hanya mengulang angka | Tidak ada interpretasi atau interpretasi salah |
| **Presentasi notebook** (15%) | Notebook terstruktur rapi, markdown headings, flow logis | Cukup terstruktur | Kurang terorganisir | Berantakan, sulit diikuti |

---

### TUGAS 2: Data Storytelling & Visualisasi

**Minggu:** 3 | **Deadline:** Minggu 4 (sebelum kelas) | **Tipe:** Individu | **Bobot:** 2.5%

#### Deskripsi

Menggunakan dataset yang sama dengan Tugas 1, mahasiswa membuat **minimal 5 visualisasi** yang menceritakan "data story" — sebuah narasi yang mengalir dari satu insight ke insight berikutnya.

#### Deliverables

1. **Jupyter Notebook (.ipynb)** berisi:
   - Minimal 5 visualisasi berbeda (histogram, scatter, box, bar, heatmap/line)
   - Setiap visualisasi memiliki judul, label axis, legend (jika relevan)
   - Narasi markdown yang menghubungkan visualisasi satu ke berikutnya
   - Minimal 1 temuan "surprising" atau insight yang tidak obvious
2. Upload ke LMS UAI

#### Rubrik Penilaian

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Variasi & kesesuaian chart** (25%) | 5+ chart berbeda, setiap tipe sesuai dengan data | 4-5 chart, kebanyakan sesuai | 3-4 chart, beberapa kurang tepat | <3 chart atau banyak yang salah tipe |
| **Estetika & clarity** (25%) | Chart indah, label lengkap, warna bermakna, mudah dibaca | Cukup jelas, sebagian label ada | Label kurang, sulit dibaca | Tanpa label, membingungkan |
| **Storytelling** (30%) | Narasi mengalir logis, insight mendalam, conclusion kuat | Ada narasi tapi kurang mengalir | Narasi minim, hanya deskripsi chart | Tidak ada narasi |
| **Kode Python** (20%) | matplotlib/seaborn idiomatic, customized, reusable | Kode benar, beberapa customization | Kode berjalan tapi minimal customization | Kode error |

---

### TUGAS 3: Simulasi Distribusi & Central Limit Theorem

**Minggu:** 5 | **Deadline:** Minggu 6 (sebelum kelas) | **Tipe:** Individu | **Bobot:** 2.5%

#### Deskripsi

Mahasiswa melakukan simulasi untuk mendemonstrasikan Central Limit Theorem (CLT) dan mengeksplorasi distribusi probabilitas.

#### Deliverables

1. **Jupyter Notebook (.ipynb)** berisi:
   - Generate data dari 3 distribusi berbeda (misal: uniform, exponential, binomial) menggunakan numpy
   - Untuk masing-masing distribusi: plot histogram, hitung mean & std
   - Simulasi CLT: ambil 1000 sampel berukuran n (untuk n=5, 30, 100), hitung mean tiap sampel, plot distribusi sampling means
   - Visualisasi yang menunjukkan distribusi sampling mean mendekati normal seiring n bertambah
   - Interpretasi: apakah hasil simulasi sesuai teori CLT?
2. Upload ke LMS UAI

#### Rubrik Penilaian

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Simulasi CLT** (35%) | 3 distribusi, 3 ukuran sampel, visualisasi konvergensi jelas | 2 distribusi, 2 ukuran sampel, visualisasi ada | 1 distribusi, simulasi dasar | Simulasi tidak berjalan |
| **Pemahaman distribusi** (25%) | Menjelaskan parameter, shape, dan use case setiap distribusi | Penjelasan benar tapi kurang detail | Penjelasan superfisial | Tidak ada penjelasan |
| **Interpretasi CLT** (25%) | Menghubungkan simulasi dengan teori, menjelaskan implikasi praktis | Interpretasi benar tapi kurang mendalam | Interpretasi hanya mengulang teori | Interpretasi salah |
| **Kualitas kode** (15%) | Efisien, loop/function digunakan, well-documented | Kode berjalan, beberapa structure | Kode repetitif tapi berjalan | Kode error |

---

### TUGAS 4: Uji Hipotesis pada Data Riil

**Minggu:** 7 | **Deadline:** Minggu 9 (sebelum kelas, melewati UTS) | **Tipe:** Individu | **Bobot:** 2.5%

#### Deskripsi

Mahasiswa merumuskan hipotesis tentang fenomena di Indonesia, menemukan/menggunakan dataset yang relevan, dan melakukan uji hipotesis lengkap.

#### Deliverables

1. **Jupyter Notebook (.ipynb)** berisi:
   - Latar belakang masalah dan pertanyaan penelitian
   - Formulasi H₀ dan H₁ secara formal
   - Pemilihan dan justifikasi uji statistik yang tepat (z-test atau t-test)
   - Pelaksanaan uji hipotesis menggunakan scipy.stats
   - Perhitungan dan interpretasi: test statistic, p-value, confidence interval
   - Diskusi effect size dan practical significance
   - Kesimpulan: reject atau fail to reject H₀, dan apa artinya secara praktis
2. Upload ke LMS UAI

#### Rubrik Penilaian

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Formulasi hipotesis** (20%) | H₀ dan H₁ tepat, konteks jelas, pertanyaan relevan | H₀/H₁ benar tapi konteks kurang | H₀/H₁ ada tapi kurang tepat | Tidak ada atau salah |
| **Pemilihan uji** (20%) | Uji tepat dengan justifikasi lengkap (kenapa bukan uji lain) | Uji tepat tapi justifikasi minim | Uji kurang tepat | Salah uji |
| **Pelaksanaan & kode** (25%) | scipy.stats benar, output lengkap, well-documented | Kode benar, output ada | Kode berjalan tapi output tidak lengkap | Kode error |
| **Interpretasi** (25%) | Interpretasi p-value tepat, effect size didiskusikan, practical significance ada | Interpretasi p-value tepat | Interpretasi superfisial | Interpretasi salah (misal: p>0.05 = H₀ terbukti) |
| **Presentasi** (10%) | Notebook mengalir logis, bisa jadi mini-paper | Cukup terstruktur | Kurang terorganisir | Berantakan |

---

### TUGAS 5: Analisis Regresi

**Minggu:** 9 | **Deadline:** Minggu 10 (sebelum kelas) | **Tipe:** Individu | **Bobot:** 2.5%

#### Deskripsi

Mahasiswa membangun model regresi linear untuk memprediksi variabel target pada dataset Indonesia, mengevaluasi model, dan menginterpretasi hasilnya.

#### Deliverables

1. **Jupyter Notebook (.ipynb)** berisi:
   - Dataset Indonesia (pilihan: data ekonomi, pendidikan, kesehatan)
   - EDA pada variabel dependen dan independen (scatter plot, korelasi)
   - Regresi linear sederhana: fit, visualisasi garis regresi, interpretasi koefisien
   - Evaluasi: R², residual plot, interpretasi
   - Prediksi pada data baru dan diskusi limitasi model
2. Upload ke LMS UAI

#### Rubrik Penilaian

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **EDA & korelasi** (20%) | Scatter plot + korelasi + interpretasi hubungan antar variabel | Ada scatter dan korelasi | EDA minimal | Tidak ada EDA |
| **Model building** (25%) | Model dibangun dengan benar, koefisien diinterpretasi dalam konteks | Model benar, interpretasi ada | Model ada tapi interpretasi kurang | Model salah |
| **Evaluasi model** (25%) | R², residual plot, identifikasi asumsi yang terpenuhi/tidak | R² dan 1 diagnostik | Hanya R² | Tidak ada evaluasi |
| **Interpretasi & insight** (20%) | Insight bermakna, limitasi didiskusikan, saran perbaikan | Interpretasi benar, beberapa limitasi | Interpretasi superfisial | Tidak ada |
| **Kualitas kode** (10%) | sklearn/statsmodels idiomatic, well-documented | Kode berjalan | Kode berjalan tapi berantakan | Error |

---

### TUGAS 6: Perbandingan Kelompok (ANOVA / Non-Parametrik)

**Minggu:** 11 | **Deadline:** Minggu 12 (sebelum kelas) | **Tipe:** Individu | **Bobot:** 2.5%

#### Deskripsi

Mahasiswa menganalisis perbedaan antar kelompok (≥3 kelompok) menggunakan ANOVA atau uji non-parametrik, tergantung pada karakteristik data.

#### Deliverables

1. **Jupyter Notebook (.ipynb)** berisi:
   - Dataset dengan minimal 3 kelompok (misal: perbandingan antar provinsi, kategori, dll)
   - Cek asumsi: normalitas (Shapiro-Wilk) dan homogenitas varians (Levene)
   - Keputusan: ANOVA atau Kruskal-Wallis, dengan justifikasi
   - Pelaksanaan uji + post-hoc test jika signifikan
   - Visualisasi: box plot per kelompok
   - Interpretasi hasil dan implikasi praktis
2. Upload ke LMS UAI

#### Rubrik Penilaian

| Kriteria | Sangat Baik (4) | Baik (3) | Cukup (2) | Kurang (1) |
|----------|-----------------|----------|-----------|------------|
| **Cek asumsi** (25%) | Normalitas + homogenitas varians dicek, hasil diinterpretasi | 1 dari 2 asumsi dicek | Asumsi disebutkan tapi tidak dicek | Tidak ada |
| **Pemilihan uji** (20%) | Uji tepat berdasarkan asumsi, justifikasi lengkap | Uji tepat, justifikasi singkat | Uji mungkin tepat tapi tanpa justifikasi | Uji salah |
| **Pelaksanaan** (25%) | Uji + post-hoc benar, p-value diinterpretasi | Uji benar, post-hoc ada | Uji berjalan tapi kurang lengkap | Error |
| **Visualisasi** (15%) | Box plot informatif, annotated, per kelompok | Box plot ada | Visualisasi minimal | Tidak ada |
| **Interpretasi** (15%) | Praktis, kontekstual, limitasi didiskusikan | Benar tapi kurang konteks | Superfisial | Salah |

---

## C. DETAIL KUIS

### KUIS 1: Fondasi (Minggu 1-4)

| Komponen | Detail |
|----------|--------|
| **Waktu** | Minggu 4, 30 menit pertama pertemuan |
| **Format** | Closed-book, kertas |
| **Cakupan** | Statistika deskriptif, visualisasi, probabilitas dasar, Bayes |
| **Tipe soal** | 5 PG + 3 soal singkat |
| **Contoh soal** | "Diberikan data: 3, 5, 7, 7, 10, 15. Hitung mean, median, dan identifikasi apakah data skewed." |

### KUIS 2: Inferensi (Minggu 5-7)

| Komponen | Detail |
|----------|--------|
| **Waktu** | Minggu 7, 30 menit terakhir pertemuan |
| **Format** | Closed-book, kertas |
| **Cakupan** | Distribusi, CLT, sampling, confidence interval, uji hipotesis |
| **Tipe soal** | 5 PG + 3 soal singkat |
| **Contoh soal** | "Sebuah sampel berukuran 36 memiliki mean 72 dan std 12. Hitung 95% confidence interval untuk population mean." |

### KUIS 3: Pemodelan (Minggu 9-12)

| Komponen | Detail |
|----------|--------|
| **Waktu** | Minggu 12, 30 menit pertama pertemuan |
| **Format** | Closed-book, kertas |
| **Cakupan** | Korelasi, regresi, ANOVA, chi-square |
| **Tipe soal** | 5 PG + 2 soal interpretasi output + 1 soal essay |
| **Contoh soal** | "Diberikan output regresi: ŷ = 3.5 + 2.1x, R² = 0.78. Interpretasikan slope dan R²." |

---

## D. PANDUAN SUBMISSION

### D.1 Format File

- **Tugas:** Jupyter Notebook (.ipynb) — pastikan semua cell sudah dijalankan (output terlihat)
- **Penamaan file:** `T[nomor]_[NIM]_[NamaDepan].ipynb` (contoh: `T1_2025001_Ahmad.ipynb`)
- **Kuis:** Dikerjakan di kertas saat perkuliahan
- **Proyek akhir:** Notebook + Laporan PDF + Slide presentasi

### D.2 Platform Submission

1. **Upload ke LMS UAI** (elearning.uai.ac.id) — **wajib** untuk semua tugas
2. **Push ke GitHub** — **disarankan** untuk membangun portfolio (repository pribadi mahasiswa)
3. **Google Colab sharing link** — sebagai backup jika LMS bermasalah

### D.3 AI Usage Documentation

Untuk setiap tugas yang menggunakan AI, tambahkan section di akhir notebook:

```markdown
## Dokumentasi Penggunaan AI

### AI Tool yang Digunakan
- [Nama tool, misal: Claude, ChatGPT]

### Prompt yang Digunakan
1. [Copy-paste prompt yang digunakan]
2. [...]

### Output AI yang Dimanfaatkan
- [Deskripsi singkat bagian mana yang menggunakan bantuan AI]

### Modifikasi yang Dilakukan
- [Apa yang diubah dari output AI dan mengapa]

### Refleksi
- [Apa yang dipelajari dari interaksi dengan AI? Apakah AI membantu atau justru menyesatkan?]
```

---

## E. TIMELINE KESELURUHAN

```
Minggu 1  ─── Perkenalan, setup
Minggu 2  ─── Lab 02 → TUGAS 1 (due Minggu 3)
Minggu 3  ─── Lab 03 → TUGAS 2 (due Minggu 4)
Minggu 4  ─── KUIS 1 + Lab 04
Minggu 5  ─── Lab 05 → TUGAS 3 (due Minggu 6)
Minggu 6  ─── Lab 06
Minggu 7  ─── Lab 07 + KUIS 2 → TUGAS 4 (due Minggu 9)
Minggu 8  ─── === UTS ===
Minggu 9  ─── Lab 09 → TUGAS 5 (due Minggu 10) + [PROYEK: Kickoff]
Minggu 10 ─── Lab 10 + [PROYEK: Proposal due]
Minggu 11 ─── Lab 11 → TUGAS 6 (due Minggu 12) + [PROYEK: EDA]
Minggu 12 ─── Lab 12 + KUIS 3 + [PROYEK: Analisis]
Minggu 13 ─── Lab 13 + [PROYEK: Draft]
Minggu 14 ─── Lab 14 + [PROYEK: Finalisasi]
Minggu 15 ─── PRESENTASI PROYEK AKHIR
Minggu 16 ─── === UAS ===
```

---

*Dokumen RTM ini merupakan bagian dari RPS mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia.*
