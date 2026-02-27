# Rubrik Penilaian Tugas

## Mata Kuliah: Analisis Data Statistik
### Prodi Informatika — UAI — Semester Genap 2025/2026

---

## Rubrik Universal 4-Point Scale

Semua tugas dinilai menggunakan skala 4 poin pada 4 dimensi utama:

| Dimensi | Bobot | Deskripsi |
|---------|-------|-----------|
| **Teknis** | 25% | Ketepatan perhitungan, pemilihan metode, kebenaran kode |
| **Interpretasi** | 30% | Kemampuan menjelaskan hasil dalam konteks, insight bermakna |
| **Kode Python** | 25% | Kualitas, kebersihan, dokumentasi, efisiensi kode |
| **Presentasi Notebook** | 20% | Struktur, flow, markdown narrative, readability |

---

## Detail Rubrik per Dimensi

### Dimensi 1: Teknis (25%)

| Skor | Deskripsi |
|------|-----------|
| **4 — Sangat Baik** | Semua perhitungan benar. Metode yang dipilih tepat dan dijustifikasi. Output lengkap dan terverifikasi. Menunjukkan pemahaman mendalam tentang konsep di balik perhitungan. |
| **3 — Baik** | Sebagian besar perhitungan benar (1-2 minor error). Metode tepat. Output ada dan sebagian besar benar. |
| **2 — Cukup** | Perhitungan dasar ada tapi beberapa error signifikan. Metode mungkin kurang tepat. Output tidak lengkap. |
| **1 — Kurang** | Banyak error dalam perhitungan. Metode salah atau tidak ada. Output minim atau error. |

### Dimensi 2: Interpretasi (30%)

| Skor | Deskripsi |
|------|-----------|
| **4 — Sangat Baik** | Interpretasi mendalam dan kontekstual. Menghubungkan angka dengan makna riil. Mengidentifikasi limitasi. Memberikan insight yang tidak obvious. Membedakan statistical vs practical significance. |
| **3 — Baik** | Interpretasi benar dan cukup kontekstual. Menyebutkan beberapa limitasi. Insight ada tapi standard. |
| **2 — Cukup** | Interpretasi superfisial — hanya mengulang angka tanpa konteks. Atau interpretasi ada tapi beberapa salah. Tidak ada diskusi limitasi. |
| **1 — Kurang** | Tidak ada interpretasi, atau interpretasi salah secara fundamental (misal: "p > 0.05 berarti H₀ terbukti benar"). |

### Dimensi 3: Kode Python (25%)

| Skor | Deskripsi |
|------|-----------|
| **4 — Sangat Baik** | Kode clean dan efisien. Menggunakan pandas/numpy idiomatik. Comment yang informatif (bukan obvious). Variable names deskriptif. Bisa di-reproduce tanpa modifikasi. |
| **3 — Baik** | Kode berjalan dengan benar. Ada beberapa comment. Sebagian besar readable. Minor inefficiency. |
| **2 — Cukup** | Kode berjalan tapi tidak efisien (banyak repetisi, hardcoded values). Minim comment. Sulit dibaca. |
| **1 — Kurang** | Kode error, tidak lengkap, atau copy-paste tanpa pemahaman (obvious dari variable names atau structure). |

### Dimensi 4: Presentasi Notebook (20%)

| Skor | Deskripsi |
|------|-----------|
| **4 — Sangat Baik** | Notebook terstruktur rapi dengan markdown headings. Flow logis dari introduction → analysis → conclusion. Narasi menghubungkan setiap bagian. Bisa dibaca seperti mini-report. |
| **3 — Baik** | Cukup terstruktur, ada beberapa heading. Flow cukup logis. Ada narasi tapi tidak selalu connecting. |
| **2 — Cukup** | Kurang terorganisir. Minim markdown. Code cells berurutan tapi tanpa penjelasan alur. |
| **1 — Kurang** | Tidak terstruktur. Cells berantakan. Tidak ada narasi. Sulit memahami apa yang dilakukan dan mengapa. |

---

## Konversi Skor ke Nilai

| Total Skor (max 16) | Nilai (0-100) | Huruf |
|---------------------|---------------|-------|
| 15-16 | 90-100 | A |
| 13-14 | 80-89 | A-/B+ |
| 11-12 | 70-79 | B+/B |
| 9-10 | 60-69 | B-/C+ |
| 7-8 | 50-59 | C |
| 5-6 | 40-49 | D |
| ≤4 | <40 | E |

**Formula:** `Nilai = (Total Skor / 16) × 100`

---

## Rubrik Spesifik per Tugas

### Tugas 1: Eksplorasi Data Deskriptif

| Kriteria | Poin Kunci |
|----------|------------|
| **Teknis** | Mean, median, modus, std, IQR dihitung benar. Missing values diidentifikasi. Outlier detection dengan IQR method. |
| **Interpretasi** | "Rata-rata IPM adalah 71.2, artinya secara rata-rata provinsi di Indonesia berada di kategori..." bukan hanya "mean = 71.2" |
| **Kode** | Penggunaan `df.describe()`, `df.info()`, manual computation dengan numpy |
| **Notebook** | Sections: Load Data → Overview → Descriptive Stats → Outliers → Summary |

### Tugas 2: Data Storytelling & Visualisasi

| Kriteria | Poin Kunci |
|----------|------------|
| **Teknis** | 5+ chart berbeda, tipe chart sesuai data, label lengkap |
| **Interpretasi** | Narasi yang menghubungkan chart: "Dari histogram kita lihat bahwa... scatter plot menunjukkan..." |
| **Kode** | matplotlib + seaborn, customization (warna, ukuran, style) |
| **Notebook** | Data Story mengalir: Opening → Exploration → Key Findings → Conclusion |

### Tugas 3: Simulasi Distribusi & CLT

| Kriteria | Poin Kunci |
|----------|------------|
| **Teknis** | 3 distribusi, 3 ukuran sampel, simulasi CLT benar, histogram sampling means |
| **Interpretasi** | Menjelaskan KENAPA sampling means mendekati normal, implikasi praktis CLT |
| **Kode** | numpy.random, loop/function untuk simulasi, scipy.stats |
| **Notebook** | Setup → Distribusi Asal → Simulasi CLT → Visualisasi Konvergensi → Interpretasi |

### Tugas 4: Uji Hipotesis pada Data Riil

| Kriteria | Poin Kunci |
|----------|------------|
| **Teknis** | H₀/H₁ benar, uji tepat, scipy.stats digunakan dengan benar, effect size dihitung |
| **Interpretasi** | p-value diinterpretasi dengan benar, practical significance vs statistical significance |
| **Kode** | scipy.stats ttest functions, clean hypothesis testing workflow |
| **Notebook** | Background → Hypothesis → Test Selection → Execution → Interpretation → Conclusion |

### Tugas 5: Analisis Regresi

| Kriteria | Poin Kunci |
|----------|------------|
| **Teknis** | Korelasi benar, model regresi dibangun, R² diinterpretasi, residual plot |
| **Interpretasi** | "Setiap kenaikan 1 juta pendapatan, IPM naik 0.3 poin" — interpretasi koefisien dalam konteks |
| **Kode** | sklearn LinearRegression, scatter + line plot, residual analysis |
| **Notebook** | EDA → Correlation → Model Building → Evaluation → Prediction → Limitations |

### Tugas 6: Perbandingan Kelompok

| Kriteria | Poin Kunci |
|----------|------------|
| **Teknis** | Asumsi dicek (Shapiro, Levene), uji tepat (ANOVA/Kruskal-Wallis), post-hoc jika signifikan |
| **Interpretasi** | "Terdapat perbedaan signifikan antar wilayah (F=..., p=...). Post-hoc menunjukkan Wilayah A berbeda dari..." |
| **Kode** | scipy.stats f_oneway/kruskal, assumption checking, box plots |
| **Notebook** | Data Overview → Assumption Check → Test Selection → Execution → Post-hoc → Conclusion |

---

## Panduan untuk Mahasiswa

### Cara Mendapat Nilai Maksimal

1. **Jangan hanya menjalankan kode** — Jelaskan apa yang dilakukan dan MENGAPA
2. **Interpretasi > Angka** — Output .describe() tanpa interpretasi = setengah nilai
3. **Konteks Indonesia** — Hubungkan temuan dengan situasi riil di Indonesia
4. **Dokumentasi AI** — Jika pakai AI, dokumentasikan dengan jujur
5. **Review sebelum submit** — Restart & Run All, pastikan tidak ada error

### Kesalahan Umum yang Mengurangi Nilai

- Hanya menempel output tanpa interpretasi
- Copy-paste kode tanpa memahami apa yang dilakukan
- Tidak mengecek asumsi sebelum uji statistik
- Interpretasi p-value yang salah
- Notebook tanpa struktur (langsung code tanpa markdown)
- Tidak mendokumentasikan penggunaan AI

---

*Dokumen ini merupakan bagian dari RPS mata kuliah Analisis Data Statistik, Prodi Informatika, Universitas Al Azhar Indonesia.*
