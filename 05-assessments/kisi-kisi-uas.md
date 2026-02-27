# Kisi-Kisi Ujian Akhir Semester (UAS)

## Mata Kuliah: Analisis Data Statistik
### Prodi Informatika — UAI — Semester Genap 2025/2026
### Dosen Pengampu: Tri Aji Nugroho, S.T., M.T.

---

## Informasi Umum

| Komponen | Detail |
|----------|--------|
| **Waktu** | Minggu 16, 100 menit |
| **Format** | Closed-book + 1 lembar A4 catatan pribadi (ditulis tangan, boleh bolak-balik) |
| **Cakupan** | Utama: Minggu 9-15 (CPMK 5-7); Komprehensif: CPMK 1-7 |
| **Bobot** | 25% dari nilai akhir |
| **Alat yang diizinkan** | Kalkulator non-programmable, 1 lembar catatan A4, alat tulis |

---

## Distribusi Soal

| Tipe Soal | Jumlah | Bobot | Bloom's |
|-----------|--------|-------|---------|
| Pilihan Ganda | 8 soal | 15% | C2-C4 |
| Hitungan & Interpretasi | 3 soal | 30% | C3-C5 |
| Interpretasi Output | 2 soal | 25% | C4-C5 |
| Essay Desain Analisis | 1 soal | 30% | C5-C6 |

---

## Kisi-Kisi Detail per Topik

### Minggu 9: Korelasi dan Regresi Linear (CPMK-5)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Menghitung dan menginterpretasi koefisien korelasi Pearson | C3-C4 | Hitungan |
| Membedakan korelasi Pearson dan Spearman | C4 | PG |
| Menjelaskan "correlation ≠ causation" | C4 | PG/Essay |
| Menginterpretasi koefisien regresi (slope, intercept) | C4 | Interpretasi |
| Menginterpretasi R² | C4 | Interpretasi |

**Contoh soal interpretasi:**
> Diberikan output regresi linear:
> ```
> ŷ = 15.3 + 2.8x
> R² = 0.72
> p-value (slope) = 0.001
> ```
> Di mana y = IPM (Indeks Pembangunan Manusia) dan x = pengeluaran pendidikan per kapita (juta rupiah).
>
> a. Interpretasikan slope 2.8 dalam konteks (4 poin)
> b. Interpretasikan R² = 0.72 (3 poin)
> c. Apakah bisa disimpulkan bahwa pengeluaran pendidikan MENYEBABKAN kenaikan IPM? Jelaskan. (3 poin)
>
> **Jawaban:**
> a. Setiap kenaikan 1 juta rupiah pengeluaran pendidikan per kapita, IPM diperkirakan naik 2.8 poin (ceteris paribus).
> b. 72% variasi dalam IPM dapat dijelaskan oleh pengeluaran pendidikan per kapita. Sisanya 28% dipengaruhi faktor lain.
> c. Tidak. Regresi menunjukkan asosiasi/korelasi, bukan kausalitas. Bisa jadi ada confounding variable (misal: tingkat urbanisasi) yang mempengaruhi keduanya.

---

### Minggu 10: Regresi Berganda (CPMK-5)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Menginterpretasi koefisien regresi berganda ("holding constant") | C4-C5 | Interpretasi |
| Membedakan R² dan adjusted R² | C4 | PG |
| Mengidentifikasi masalah multicollinearity dari VIF | C4 | Interpretasi |
| Mengevaluasi asumsi regresi dari residual plot | C5 | Interpretasi |

**Contoh soal PG:**
> Dalam regresi berganda, adjusted R² lebih direkomendasikan daripada R² karena:
> A. Adjusted R² selalu lebih besar dari R²
> B. Adjusted R² memperhitungkan jumlah prediktor dan menghukum penambahan variabel yang tidak bermakna
> C. R² tidak bisa digunakan dalam regresi berganda
> D. Adjusted R² mengukur kausalitas
>
> **Jawaban: B**

---

### Minggu 11: ANOVA dan Uji Non-Parametrik (CPMK-6)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Memilih antara ANOVA dan Kruskal-Wallis berdasarkan asumsi | C4 | PG |
| Menginterpretasi output ANOVA (F-statistic, p-value) | C4 | Interpretasi |
| Menjelaskan fungsi post-hoc test | C3 | PG |
| Menentukan kapan menggunakan uji non-parametrik | C4 | PG/Essay |

**Contoh soal hitungan/interpretasi:**
> Seorang peneliti membandingkan pengeluaran bulanan (ribu rupiah) mahasiswa dari 3 wilayah.
> Output ANOVA:
> ```
> F-statistic: 4.82
> p-value: 0.012
>
> Group means:
>   Jawa: 1850
>   Sumatera: 1620
>   Kalimantan: 1780
>
> Shapiro-Wilk (normality): p = 0.23
> Levene (homogeneity): p = 0.45
> ```
>
> a. Apakah asumsi ANOVA terpenuhi? Jelaskan. (4 poin)
> b. Apa kesimpulan dari uji ANOVA ini? (α = 0.05) (3 poin)
> c. Langkah apa yang harus dilakukan setelah ANOVA signifikan? (3 poin)
>
> **Jawaban:**
> a. Ya, asumsi terpenuhi: normalitas OK (Shapiro p=0.23 > 0.05, gagal tolak H₀ normalitas), homogenitas varians OK (Levene p=0.45 > 0.05).
> b. F=4.82, p=0.012 < 0.05 → tolak H₀. Terdapat perbedaan signifikan dalam pengeluaran antar minimal satu pasang wilayah.
> c. Post-hoc test (misal Tukey's HSD) untuk menentukan PASANGAN MANA yang berbeda signifikan.

---

### Minggu 12: Analisis Data Kategorikal (CPMK-6)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Melakukan dan menginterpretasi chi-square test | C3-C4 | Hitungan |
| Menghitung expected frequencies | C3 | Hitungan |
| Membedakan chi-square dan logistic regression | C4 | PG |
| Menginterpretasi odds ratio | C4 | Interpretasi |

**Contoh soal hitungan:**
> Survei 200 mahasiswa tentang preferensi platform belajar:
>
> |  | LMS | YouTube | MOOC | Total |
> |--|-----|---------|------|-------|
> | Informatika | 40 | 30 | 30 | 100 |
> | Manajemen | 25 | 45 | 30 | 100 |
> | Total | 65 | 75 | 60 | 200 |
>
> a. Hitung expected frequency untuk cell "Informatika - LMS" (3 poin)
> b. Jika chi-square statistic = 6.41 dan p-value = 0.041, apa kesimpulannya? (4 poin)
> c. Berdasarkan data, jelaskan pola preferensi yang terlihat (3 poin)
>
> **Jawaban:**
> a. E = (100 × 65) / 200 = 32.5
> b. p=0.041 < 0.05, tolak H₀. Terdapat hubungan signifikan antara jurusan dan preferensi platform.
> c. Informatika cenderung lebih memilih LMS (40 vs expected 32.5), sementara Manajemen lebih memilih YouTube (45 vs expected 37.5).

---

### Minggu 13: Machine Learning Statistik (CPMK-7)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Membedakan supervised dan unsupervised learning | C2 | PG |
| Menginterpretasi confusion matrix | C4 | Interpretasi |
| Menghitung accuracy, precision, recall dari confusion matrix | C3 | Hitungan |
| Menjelaskan pentingnya train-test split | C3 | PG |

**Contoh soal interpretasi:**
> Confusion matrix dari model klasifikasi spam:
> ```
>                 Predicted
>              Spam    Not Spam
> Actual Spam   85        15
>   Not Spam    10       190
> ```
>
> a. Hitung accuracy, precision (untuk Spam), dan recall (untuk Spam) (6 poin)
> b. Model ini lebih baik dalam mendeteksi spam atau menghindari false alarm? Jelaskan. (4 poin)
>
> **Jawaban:**
> a. Accuracy = (85+190)/300 = 91.7%; Precision(Spam) = 85/(85+10) = 89.5%; Recall(Spam) = 85/(85+15) = 85%
> b. Precision (89.5%) > Recall (85%), artinya model lebih baik dalam menghindari false alarm (labeling non-spam sebagai spam) dibanding mendeteksi semua spam.

---

### Minggu 14: AI-Augmented Analysis (CPMK-7)

| Indikator | Bloom's | Tipe Soal |
|-----------|---------|-----------|
| Menjelaskan kelebihan dan keterbatasan AI sebagai co-analyst | C5 | Essay |
| Mengevaluasi output analisis yang mungkin dari AI | C5 | Essay |
| Menjelaskan prinsip dokumentasi penggunaan AI | C4 | PG |

**Contoh soal PG:**
> Seorang mahasiswa menggunakan ChatGPT untuk menganalisis data. Output AI menyatakan: "Korelasi antara es krim dan drowning adalah r = 0.85, sehingga makan es krim menyebabkan tenggelam." Respons yang paling tepat adalah:
>
> A. Output benar, korelasi tinggi menunjukkan kausalitas
> B. Output salah karena korelasi rendah
> C. Korelasi mungkin benar, tapi kesimpulan kausalitas salah — perlu mempertimbangkan confounding variable (suhu)
> D. AI tidak bisa menghitung korelasi
>
> **Jawaban: C**

---

## Soal Komprehensif (dari materi UTS)

UAS juga mencakup konsep dari Minggu 1-7 secara tersirat, khususnya:
- Tipe data dan skala pengukuran (dalam konteks memilih uji)
- Statistika deskriptif (sebagai bagian EDA dalam essay)
- Probabilitas dan distribusi (sebagai dasar inferensi)
- Confidence interval dan uji hipotesis (dalam konteks regresi)

---

## Contoh Soal Essay Desain Analisis (30%)

> **Skenario:** Kementerian Kesehatan Indonesia ingin mengetahui faktor-faktor yang mempengaruhi status gizi balita (kategori: gizi baik, gizi kurang, gizi buruk) di 34 provinsi. Data yang tersedia meliputi: pendapatan rumah tangga (numerik, juta Rp), tingkat pendidikan ibu (SD/SMP/SMA/PT), akses ke fasilitas kesehatan (ya/tidak), wilayah (Jawa/Sumatera/Kalimantan/Sulawesi/Papua), dan jumlah anak (numerik).
>
> Sebagai data analyst, desain analisis statistik lengkap:
>
> a. Identifikasi variabel dependen dan independen. Tentukan tipe data masing-masing. (5 poin)
> b. Metode statistik apa saja yang relevan untuk menjawab pertanyaan penelitian? Jelaskan MINIMAL 3 metode berbeda dan justifikasi pemilihan masing-masing. (10 poin)
> c. Untuk salah satu metode yang Anda pilih, jelaskan asumsi yang perlu diperiksa dan apa yang dilakukan jika asumsi tidak terpenuhi. (5 poin)
> d. Bagaimana Anda akan menggunakan AI sebagai co-analyst dalam proyek ini? Berikan contoh 2 prompt spesifik yang akan Anda gunakan. (5 poin)
> e. Sebutkan 2 limitasi potensial dari analisis ini. (5 poin)

---

## Tips Menghadapi UAS

1. **Buat lembar catatan yang efektif** — Fokuskan pada rumus, decision tree pemilihan uji, dan interpretasi kunci
2. **Latihan interpretasi output** — Banyak soal tentang membaca output Python, bukan menghitung manual
3. **Pahami "kapan pakai apa"** — Decision tree: tipe data + jumlah kelompok + asumsi → uji yang tepat
4. **Siapkan untuk essay desain** — Latih berpikir sistematis: data → pertanyaan → metode → asumsi → interpretasi
5. **Review konsep UTS** — Fondasi tetap penting, terutama uji hipotesis dan confidence interval
6. **Jangan hanya hafal** — UAS menguji kemampuan menerapkan dan mengevaluasi, bukan menghafal

### Decision Tree untuk Lembar Catatan

```
Pertanyaan Penelitian
├── Hubungan antar variabel?
│   ├── Keduanya numerik → Korelasi (Pearson/Spearman) + Regresi
│   ├── Keduanya kategorikal → Chi-Square
│   └── Numerik + Kategorikal → t-test / ANOVA
├── Perbandingan kelompok?
│   ├── 2 kelompok
│   │   ├── Data normal → t-test (independent/paired)
│   │   └── Data tidak normal → Mann-Whitney U
│   └── >2 kelompok
│       ├── Data normal + varians homogen → One-way ANOVA + Tukey
│       └── Asumsi tidak terpenuhi → Kruskal-Wallis
└── Prediksi?
    ├── Target numerik → Regresi Linear
    └── Target kategorikal → Logistic Regression / Decision Tree / k-NN
```

---

*Kisi-kisi ini merupakan panduan cakupan materi. Soal ujian sebenarnya mungkin bervariasi dalam format dan tingkat kesulitan.*
