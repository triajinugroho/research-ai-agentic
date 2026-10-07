# Minggu 16: Ujian Akhir Semester (UAS)

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 16 |
| **Topik** | Review komprehensif dan pelaksanaan UAS |
| **CPL / CPMK** | CPL08 / CPMK081 |
| **Sub-CPMK** | `PS-Sub-CPMK081-1` |
| **Bobot** | **25%** dari nilai akhir |
| **Durasi** | 30 menit review + 120 menit ujian |
| **Bentuk** | Tes tulis *closed book* |

---

## Bagian 1: Review Komprehensif (30 menit)

### 1.1 Peta Utuh Mata Kuliah

```
                     PROBABILITAS DAN STATISTIK
                               │
         ┌─────────────────────┴─────────────────────┐
         │                                           │
   PS-Sub-CPMK102-1 (55%)                 PS-Sub-CPMK081-1 (45%)
   mengolah–menganalisis–                 menerapkan–menganalisis
   memvisualisasikan                      probabilitas & inferensi
         │                                           │
   ┌─────┴─────┐                        ┌────────────┼────────────┐
   │           │                        │            │            │
 DESKRIPTIF  VISUALISASI          PROBABILITAS  DISTRIBUSI   INFERENSI
 (M2)        (M3)                 (M4–M5)       (M6–M7)      (M9–M14)
   │           │                        │            │            │
 mean        histogram            aksioma      Bernoulli     CLT
 median      boxplot              bersyarat    Binomial      estimasi
 varians     scatter              Bayes        Poisson       interval
 IQR         kejujuran            kebebasan    Geometrik     uji hipotesis
 pencilan    visual                            Normal        ANOVA
                                               Eksponensial  chi-square
                                                             regresi
```

### 1.2 Sepuluh Konsep yang Wajib Dikuasai untuk UAS

UAS menekankan `PS-Sub-CPMK081-1`. Sepuluh konsep berikut adalah inti yang akan diuji:

| No | Konsep | Minggu | Mengapa penting |
|----|--------|--------|-----------------|
| 1 | Aturan penjumlahan dan perkalian probabilitas | 4 | Dasar semua perhitungan |
| 2 | Probabilitas bersyarat dan **P(A\|B) ≠ P(B\|A)** | 4–5 | Kesalahan paling umum |
| 3 | Teorema Bayes dan *base rate fallacy* | 5 | Muncul di hampir semua sistem AI |
| 4 | Memilih distribusi yang tepat (BINS untuk Binomial) | 6 | Pemodelan fenomena |
| 5 | Distribusi Normal, skor-z, membaca tabel | 7 | Dasar seluruh inferensi klasik |
| 6 | Teorema Limit Pusat dan galat baku σ/√n | 9 | Penghubung sampel ke populasi |
| 7 | Interval kepercayaan dan **tafsirnya yang benar** | 10 | Sering salah ditafsirkan |
| 8 | Uji hipotesis: H₀/H₁, galat Tipe I/II, *p-value* | 11 | Inti inferensi |
| 9 | Memilih uji dua sampel: bebas vs berpasangan | 12 | Kesalahan rancangan yang mahal |
| 10 | Korelasi bukan sebab-akibat | 14 | Etika interpretasi |

### 1.3 Daftar Rumus yang Harus Hafal

Tabel distribusi disediakan, tetapi rumus berikut **tidak** disediakan:

| Konsep | Rumus |
|--------|-------|
| Varians sampel | s² = Σ(xᵢ − x̄)² / (n − 1) |
| Probabilitas bersyarat | P(A\|B) = P(A ∩ B) / P(B) |
| Aturan penjumlahan | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) |
| Teorema Bayes | P(H\|E) = P(H)·P(E\|H) / P(E) |
| Binomial | P(X=k) = C(n,k) pᵏ(1−p)ⁿ⁻ᵏ |
| Poisson | P(X=k) = e^(−λ) λᵏ / k! |
| Skor-z | z = (x − μ) / σ |
| Galat baku | SE = σ/√n (atau s/√n) |
| Interval kepercayaan | x̄ ± t(α/2, n−1) · s/√n |
| Statistik t satu sampel | t = (x̄ − μ₀) / (s/√n) |
| Korelasi | r = Cov(X,Y) / (sₓ · s_y) |

### 1.4 Lima Kesalahan Paling Mahal di UAS

| No | Kesalahan | Cara menghindari |
|----|-----------|------------------|
| 1 | Membalik arah persyaratan: menjawab P(B\|A) padahal ditanya P(A\|B) | Tulis "diketahui" dan "ditanya" dalam notasi sebelum menghitung |
| 2 | Memakai Binomial padahal percobaan tidak bebas atau n tidak tetap | Periksa syarat BINS satu per satu, tuliskan pemeriksaannya |
| 3 | Salah arah membaca tabel Normal | Selalu gambar kurva dan arsir daerah yang dicari |
| 4 | Menyimpulkan "H₀ terbukti benar" ketika gagal menolak | Gunakan kalimat baku: "bukti tidak cukup untuk menyatakan..." |
| 5 | Menyatakan sebab-akibat dari korelasi | Gunakan kata "berkaitan dengan", bukan "menyebabkan" |

---

## Bagian 2: Pelaksanaan Ujian (120 menit)

### 2.1 Ketentuan

| Aspek | Ketentuan |
|-------|-----------|
| **Durasi** | 120 menit |
| **Sifat** | *Closed book* |
| **Alat bantu yang diizinkan** | Kalkulator ilmiah non-programmable, alat tulis |
| **Disediakan pengawas** | Tabel distribusi Normal baku, tabel-t, tabel chi-square, tabel F |
| **Yang dilarang** | Telepon genggam, jam pintar, laptop, catatan, **AI dalam bentuk apa pun** |
| **Cakupan** | Komprehensif Minggu 1–15, penekanan Minggu 9–14 |
| **Sub-CPMK yang dinilai** | `PS-Sub-CPMK081-1` |
| **Syarat mengikuti** | Kehadiran minimal 75% |

### 2.2 Komposisi Soal

| Bagian | Bentuk | Jumlah | Bobot | Level Bloom |
|--------|--------|--------|-------|-------------|
| A | Pilihan ganda | 15 soal | 15% | C2–C3 |
| B | Isian dan hitungan pendek | 10 soal | 20% | C3 |
| C | Uraian terstruktur | 5 soal | 40% | C3–C4 |
| D | Studi kasus terpadu | 1 soal | 25% | C4 |

### 2.3 Sebaran Materi

| Pokok Bahasan | Minggu | Bobot |
|---------------|--------|-------|
| Statistika deskriptif dan visualisasi | 2–3 | 8% |
| Probabilitas dasar dan pencacahan | 4 | 12% |
| Teorema Bayes dan kebebasan | 5 | 14% |
| Distribusi diskret | 6 | 10% |
| Distribusi kontinu dan Normal | 7 | 12% |
| Distribusi sampling dan CLT | 9 | 10% |
| Estimasi dan interval kepercayaan | 10 | 12% |
| Uji hipotesis satu dan dua sampel | 11–12 | 14% |
| ANOVA, chi-square, korelasi–regresi | 13–14 | 8% |

Rincian per butir ada pada [kisi-kisi UAS](../05-assessments/kisi-kisi-uas.md).

### 2.4 Bentuk Soal Studi Kasus Terpadu (Bagian D)

Satu skenario Informatika yang menuntut rangkaian keputusan:

1. Menentukan jenis dan skala data.
2. Memilih ukuran ringkasan yang tepat.
3. Memodelkan sebuah fenomena dengan distribusi yang sesuai.
4. Menghitung probabilitas yang diminta.
5. Menyusun interval kepercayaan.
6. **Memilih uji hipotesis yang tepat dan menyebutkan asumsinya.**
7. Menjalankan uji dan menafsirkan hasilnya.
8. Menyatakan apa yang **tidak** dapat disimpulkan dari analisis tersebut.

> Butir 6 dan 8 memiliki bobot terbesar. Keduanya mengukur penalaran, bukan kemampuan berhitung.

### 2.5 Kriteria Penilaian Uraian

Mengikuti kriteria `PS-Sub-CPMK081-1` — **ketepatan rumus dan hitung; kecocokan asumsi; kualitas interpretasi**:

| Aspek | Bobot | Keterangan |
|-------|-------|------------|
| Ketepatan rumus | 30% | Rumus yang dipilih sesuai jenis persoalan |
| Ketepatan hitung | 25% | Hasil benar sampai akhir, satuan tepat |
| Kecocokan asumsi | 25% | Asumsi disebutkan dan diperiksa kelayakannya |
| Kualitas interpretasi | 20% | Angka diterjemahkan menjadi kesimpulan kontekstual yang tidak melampaui data |

> Jawaban yang hanya berisi angka akhir memperoleh **maksimal 40%** bobot soal. Langkah benar dengan salah hitung kecil tetap memperoleh sebagian besar nilai.

---

## Strategi Mengerjakan

1. **Alokasikan waktu:** Bagian A 15 menit · B 25 menit · C 50 menit · D 25 menit · periksa ulang 5 menit.
2. Kerjakan Bagian D **lebih dahulu** bila Anda merasa waktunya akan sempit — bobotnya paling besar.
3. Untuk setiap soal probabilitas, **tulis notasi** "diketahui" dan "ditanya" sebelum menghitung.
4. Untuk setiap soal distribusi Normal, **gambar kurva** dan arsir daerahnya.
5. Untuk setiap uji hipotesis, tulis H₀ dan H₁ **secara eksplisit** — ada nilai untuk ini.
6. Tuliskan **satuan** pada setiap jawaban akhir.
7. Bila ragu antara dua uji, **tulis alasan pemilihan Anda** — penalaran yang benar tetap bernilai meski pilihannya kurang optimal.

---

## Setelah UAS

| Kegiatan | Waktu |
|----------|-------|
| Pengumuman nilai akhir | Sesuai kalender akademik UAI |
| Periode sanggah nilai | 3 hari kerja setelah pengumuman |
| Rekap ketuntasan Sub-CPMK | Minggu 17, disampaikan ke Program Studi |
| Ujian susulan (dengan surat keterangan sah) | Maksimal 7 hari setelah jadwal UAS |

---

## Penutup Mata Kuliah

Selamat, Anda telah menyelesaikan mata kuliah fondasi bagi jalur Kecerdasan Artifisial dan Sains Data Prodi Informatika UAI.

**Yang Anda bawa dari mata kuliah ini:**

1. Kemampuan **menyatakan ketidakpastian secara jujur** — bukan menyembunyikannya di balik angka tunggal.
2. Kebiasaan **memeriksa asumsi sebelum menyimpulkan** — pembeda antara analis dan pemakai pustaka.
3. Kesadaran bahwa **signifikan secara statistik tidak sama dengan penting secara praktis**.
4. Kemampuan membaca klaim berbasis angka **secara kritis**, termasuk klaim yang datang dari sistem AI.
5. Landasan **amanah** dalam melaporkan hasil: tidak memaksakan signifikansi, tidak menyembunyikan keterbatasan.

**Ke mana selanjutnya:**

| Semester | Mata Kuliah | Yang akan dikembangkan |
|----------|-------------|------------------------|
| 2 | Analisis Data Statistik (IF52520025) | Regresi berganda, data kategorikal, analisis multivariat |
| 4 | Sains Data (IF52520026) | Pemodelan data berskala besar |
| 5 | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (IF52510031) | Distribusi sebagai asumsi model, metrik sebagai statistik |
| 5 | Jaringan Syaraf Tiruan dan Pembelajaran Mendalam (IF52510032) | Probabilitas sebagai dasar *loss function* |
| 7 | Metodologi Penelitian (IF52510021) | Uji hipotesis sebagai validasi temuan |
| 8 | Tugas Akhir (IF52520022) | Seluruh kerangka validasi empiris |

> Ketika kelak Anda melatih sebuah model dan melihat angka akurasi 94%, Anda akan bertanya: *"Berapa base rate-nya? Apakah 94% itu lebih baik daripada menebak kelas mayoritas? Berapa interval kepercayaannya?"* — **pertanyaan itulah yang mata kuliah ini tanamkan**, dan itulah yang membedakan seorang sarjana Informatika dari seorang pengguna pustaka.

---

## Referensi

1. [Kisi-kisi UAS](../05-assessments/kisi-kisi-uas.md)
2. [Kerangka asesmen](../05-assessments/assessment-framework.md)
3. Buku ajar Bab 1–14
4. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.). Pearson.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
