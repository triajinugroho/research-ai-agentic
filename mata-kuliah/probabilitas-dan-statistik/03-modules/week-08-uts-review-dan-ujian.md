# Minggu 8: Ujian Tengah Semester (UTS)

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 8 |
| **Topik** | Review menyeluruh Minggu 1–7 dan pelaksanaan UTS |
| **CPL / CPMK** | CPL10 / CPMK102 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Bobot** | **25%** dari nilai akhir |
| **Durasi** | 50 menit review + 100 menit ujian |
| **Bentuk** | Tes tulis *closed book* |

---

## Tujuan Minggu Ini

1. **Mengonsolidasikan** (C4) seluruh konsep Minggu 1–7 dalam satu kerangka utuh.
2. **Mendemonstrasikan** (C3–C4) penguasaan statistika deskriptif, visualisasi, probabilitas, dan distribusi melalui tes tulis.

---

## Bagian 1: Review Terpadu (50 menit)

### 1.1 Peta Konsep Minggu 1–7

```
                    DATA
                      │
        ┌─────────────┴─────────────┐
        │                           │
  MENGGAMBARKAN                MEMODELKAN
  (Minggu 1–3)                 (Minggu 4–7)
        │                           │
   ┌────┴────┐              ┌───────┴───────┐
   │         │              │               │
 PEMUSATAN  PENYEBARAN   PROBABILITAS   DISTRIBUSI
 mean       varians       aksioma        diskret:
 median     simp. baku    penjumlahan    Bernoulli
 modus      IQR           perkalian      Binomial
   │         │            bersyarat      Poisson
   └────┬────┘            Bayes          Geometrik
        │                 kebebasan
   VISUALISASI                │          kontinu:
   histogram                  │          Uniform
   boxplot                    │          Eksponensial
   scatter                    │          Normal
        │                     │               │
        └──────────┬──────────┴───────────────┘
                   │
            siap untuk INFERENSI
               (Minggu 9–14)
```

### 1.2 Daftar Periksa Penguasaan

Tandai konsep yang sudah Anda kuasai. Konsep yang belum tercentang adalah prioritas belajar Anda.

**Minggu 1 — Pengantar**
- [ ] Membedakan populasi dan sampel; parameter (μ, σ, p) dan statistik (x̄, s, p̂)
- [ ] Mengklasifikasikan data ke nominal, ordinal, interval, rasio
- [ ] Menentukan operasi statistik yang sah untuk tiap skala
- [ ] Membedakan statistika deskriptif dan inferensial

**Minggu 2 — Statistika Deskriptif**
- [ ] Menghitung mean, median, modus secara manual
- [ ] Menentukan kapan median lebih tepat daripada mean
- [ ] Menghitung varians dan simpangan baku sampel (penyebut n−1)
- [ ] Menghitung kuartil, IQR, dan batas pencilan 1,5×IQR
- [ ] Menafsirkan kemencengan dari hubungan mean–median

**Minggu 3 — Visualisasi**
- [ ] Memilih grafik yang sesuai dengan jenis data dan pertanyaan
- [ ] Membaca boxplot (lima angka + pencilan)
- [ ] Mengenali teknik penyajian yang menyesatkan
- [ ] Menjelaskan dampak lebar bin pada histogram

**Minggu 4 — Dasar Probabilitas**
- [ ] Menentukan ruang sampel dan kejadian
- [ ] Menerapkan aturan komplemen dan penjumlahan umum
- [ ] Menghitung probabilitas bersyarat P(A|B)
- [ ] Menerapkan aturan perkalian (dengan dan tanpa pengembalian)
- [ ] Menghitung permutasi P(n,r) dan kombinasi C(n,r)

**Minggu 5 — Bayes**
- [ ] Menerapkan hukum probabilitas total
- [ ] Menerapkan Teorema Bayes
- [ ] Menjelaskan *base rate fallacy*
- [ ] Membedakan saling lepas dan saling bebas
- [ ] Menghitung keandalan sistem seri dan paralel

**Minggu 6 — Distribusi Diskret**
- [ ] Menjelaskan PMF dan CDF
- [ ] Menerapkan Binomial (syarat BINS) dan menghitung E[X], Var(X)
- [ ] Menerapkan Poisson dan mengenali ciri mean = varians
- [ ] Menerapkan Geometrik dan sifat tanpa memori
- [ ] Memilih distribusi yang tepat untuk sebuah kasus

**Minggu 7 — Distribusi Kontinu**
- [ ] Menjelaskan mengapa P(X = x) = 0 pada peubah kontinu
- [ ] Menerapkan distribusi Eksponensial untuk waktu tunggu
- [ ] Menghitung probabilitas Normal dengan skor-z dan **tabel**
- [ ] Menerapkan aturan empiris 68–95–99,7
- [ ] Membaca Q-Q plot

### 1.3 Lima Kesalahan yang Paling Sering Terjadi

| No | Kesalahan | Cara Menghindari |
|----|-----------|------------------|
| 1 | Menukar P(A\|B) dengan P(B\|A) | Tuliskan secara eksplisit: "yang diketahui apa, yang ditanya apa" |
| 2 | Memakai penyebut n (bukan n−1) untuk varians sampel | Baca soal: "sampel" atau "populasi"? |
| 3 | Memakai Binomial padahal percobaan tidak bebas | Periksa syarat BINS satu per satu |
| 4 | Salah arah pada tabel Normal (melihat P(Z > z) padahal tabel memberi P(Z < z)) | Selalu gambar kurva dan arsir daerah yang dicari |
| 5 | Menghitung rata-rata pada data ordinal atau nominal | Tentukan skala data sebelum memilih operasi |

---

## Bagian 2: Pelaksanaan Ujian (100 menit)

### 2.1 Ketentuan Ujian

| Aspek | Ketentuan |
|-------|-----------|
| **Durasi** | 100 menit |
| **Sifat** | *Closed book* |
| **Alat bantu yang diizinkan** | Kalkulator ilmiah non-programmable, alat tulis |
| **Disediakan pengawas** | Satu lembar tabel distribusi Normal baku dan tabel-t |
| **Yang dilarang** | Telepon genggam, jam pintar, laptop, catatan apa pun, **AI dalam bentuk apa pun** |
| **Cakupan** | Minggu 1–7 |
| **Sub-CPMK yang dinilai** | `PS-Sub-CPMK102-1` |

### 2.2 Komposisi Soal

| Bagian | Bentuk | Jumlah | Bobot | Level Bloom |
|--------|--------|--------|-------|-------------|
| A | Pilihan ganda | 15 soal | 20% | C2–C3 |
| B | Isian singkat / hitungan pendek | 8 soal | 25% | C3 |
| C | Uraian terstruktur | 4 soal | 40% | C3–C4 |
| D | Studi kasus terpadu | 1 soal | 15% | C4 |

### 2.3 Sebaran Materi

| Pokok Bahasan | Minggu | Bobot |
|---------------|--------|-------|
| Jenis data, skala, populasi–sampel | 1 | 8% |
| Ukuran pemusatan, penyebaran, posisi, pencilan | 2 | 20% |
| Visualisasi dan pemilihan grafik | 3 | 12% |
| Aksioma, aturan penjumlahan/perkalian, bersyarat, pencacahan | 4 | 20% |
| Probabilitas total, Bayes, kebebasan | 5 | 18% |
| Distribusi diskret (Binomial, Poisson, Geometrik) | 6 | 12% |
| Distribusi kontinu (Eksponensial, Normal, skor-z) | 7 | 10% |

Rincian lengkap ada pada [kisi-kisi UTS](../05-assessments/kisi-kisi-uts.md).

### 2.4 Kriteria Penilaian Soal Uraian

Mengikuti kriteria `PS-Sub-CPMK102-1` — **ketepatan prosedur, kesesuaian grafik, validitas interpretasi**:

| Aspek | Bobot | Keterangan |
|-------|-------|------------|
| Ketepatan prosedur | 35% | Langkah benar dan berurutan; rumus yang dipilih sesuai |
| Ketepatan hitung | 25% | Hasil akhir benar, satuan tepat, pembulatan wajar |
| Kecocokan asumsi | 20% | Asumsi distribusi/uji disebutkan dan diperiksa |
| Validitas interpretasi | 20% | Angka diterjemahkan menjadi kesimpulan kontekstual |

> **Penting:** jawaban yang hanya berisi angka akhir tanpa langkah memperoleh nilai **maksimal 40%** dari bobot soal. Sebaliknya, langkah yang benar dengan salah hitung kecil tetap memperoleh sebagian besar nilai. Yang dinilai adalah **penalaran**, bukan kecepatan berhitung.

---

## Strategi Mengerjakan Ujian

1. **Baca seluruh soal lebih dulu** (5 menit). Kerjakan yang paling dikuasai terlebih dahulu.
2. **Untuk soal probabilitas:** tuliskan "diketahui" dan "ditanya" dalam notasi. Banyak kesalahan terjadi karena salah membaca arah persyaratan.
3. **Untuk soal distribusi Normal:** selalu gambar kurva dan arsir daerah yang dicari sebelum membaca tabel.
4. **Untuk soal distribusi diskret:** periksa syarat BINS sebelum memakai Binomial.
5. **Tuliskan satuan.** Jawaban "0,0338" berbeda maknanya dari "3,38%".
6. **Sisakan 10 menit** untuk memeriksa ulang, terutama pembulatan dan satuan.

---

## Setelah Ujian

| Kegiatan | Waktu |
|----------|-------|
| Pembahasan soal UTS | Minggu 9, 10 menit pertama |
| Pengumuman nilai | Paling lambat 14 hari setelah ujian |
| Periode sanggah nilai | 3 hari setelah pengumuman |
| Ujian susulan (dengan surat keterangan sah) | Maksimal 7 hari setelah jadwal UTS |

---

## Persiapan Minggu 9

Minggu depan kita memasuki **fase inferensial** — bagian paling penting dari mata kuliah ini. Semua yang dipelajari sampai Minggu 7 adalah persiapan untuk ini.

**Yang perlu disiapkan:**
1. Membaca [Bab 8 buku ajar](../06-buku-ajar/bab-08-ekspektasi-varians-sampling.md).
2. Memastikan konsep **varians** dan **distribusi Normal** benar-benar dipahami — keduanya menjadi fondasi Teorema Limit Pusat.
3. **Memastikan pengumpulan data proyek sedang berjalan.** Analisis deskriptif proyek sebaiknya sudah dimulai pada Minggu 10–11.

---

## Referensi

1. [Kisi-kisi UTS](../05-assessments/kisi-kisi-uts.md)
2. [Kerangka asesmen](../05-assessments/assessment-framework.md)
3. Buku ajar Bab 1–7
4. Walpole, R. E., et al. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 1–6. Pearson.

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
