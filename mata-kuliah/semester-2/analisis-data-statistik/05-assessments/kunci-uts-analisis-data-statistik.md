---
mata_kuliah: Analisis Data Statistik
kode_mk: IF2XXX
sks: 2 SKS (Teori + Praktikum Terintegrasi)
semester: Genap 2025/2026
jenis: UTS — Kunci Jawaban
---

# UJIAN TENGAH SEMESTER (UTS)
## Semester Genap Tahun Akademik 2025/2026

### KUNCI JAWABAN, RUBRIK PENSKORAN & PEMETAAN CPMK

> **RAHASIA — HANYA UNTUK DOSEN/ASISTEN PENGAMPU**

> *"Sesungguhnya Allah menyuruh kamu menyampaikan amanat kepada yang berhak menerimanya, dan (menyuruh kamu) apabila menetapkan hukum di antara manusia supaya kamu menetapkan dengan adil."*
> — **QS An-Nisa: 58**

**UNIVERSITAS AL AZHAR INDONESIA**
**Fakultas Sains dan Teknologi — Program Studi Informatika**

| Field             | Nilai                                                               |
|-------------------|---------------------------------------------------------------------|
| Mata Kuliah       | Analisis Data Statistik                                             |
| Kode MK / SKS     | IF2XXX / 2 SKS (Teori + Praktikum Terintegrasi)                     |
| Dosen             | Tri Aji Nugroho, S.T., M.T.                                         |
| Kelas             | [......]                                                            |
| Hari/Tanggal      | [......]                                                            |
| Waktu             | 120 menit                                                           |
| Sifat Ujian       | Closed-book — boleh kalkulator ilmiah & tabel distribusi (z, t, chi-square) |

---

## BAGIAN I — KUNCI PILIHAN GANDA (15 × 2 pt = 30 pt)

### PG No. 1

**Sub-CPMK:** 1.1 — Menjelaskan peran statistika di era data science dan AI
**Level Bloom:** C2
**Konteks:** Umum

**Jawaban:** B

**Pembahasan:**
Statistika adalah fondasi inferensi — dari data (sampel) ke pengetahuan (populasi) — dan menyediakan kerangka keputusan di bawah ketidakpastian. Opsi A terlalu sempit; C salah karena *machine learning* masih bergantung pada asumsi distribusi, validasi statistik, dan *uncertainty quantification*. D salah (statistika berguna di berbagai ukuran data); E salah (statistika ≠ hanya visualisasi).

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 2

**Sub-CPMK:** 1.3 — Menjelaskan prinsip etika data dan responsible AI
**Level Bloom:** C2
**Konteks:** Islami (amanah data)

**Jawaban:** A

**Pembahasan:**
Menggunakan data pribadi tanpa persetujuan melanggar *informed consent*; memakai data yang dikumpulkan untuk tujuan zakat kemudian dijual untuk pemasaran melanggar *purpose limitation*. Opsi B/C/D adalah atribut sistem teknis (bukan etika data pribadi) dan tidak menangkap inti pelanggaran. E salah karena bukan hanya interpretabilitas yang dilanggar — justru privasi & consent adalah pusat kasus.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 3

**Sub-CPMK:** 2.1 — Menghitung dan menginterpretasi ukuran pemusatan dan penyebaran data
**Level Bloom:** C3
**Konteks:** Indonesia (UMP 34 provinsi)

**Jawaban:** B

**Pembahasan:**
Pada distribusi *right-skewed* (ada outlier besar seperti DKI Jakarta), **mean** tertarik ke arah outlier sehingga tidak representatif. **Median** lebih robust terhadap outlier dan paling menggambarkan "tipikal". Modus kurang cocok untuk data kontinu seperti UMP; Range dan Varians adalah ukuran penyebaran, bukan pemusatan.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 4

**Sub-CPMK:** 2.1 — Menghitung dan menginterpretasi ukuran pemusatan dan penyebaran data
**Level Bloom:** C3
**Konteks:** JTBD (variasi nilai ujian pribadi)

**Jawaban:** C

**Pembahasan:**
Standar deviasi mengukur variabilitas di sekitar mean. SD = 3 (kecil) → data konsisten/homogen; SD = 12 (besar) → data fluktuatif. Rata-rata sama tidak berarti sebaran sama (A salah). B membalik interpretasi. D/E salah secara konseptual — mean & SD justru saling melengkapi (pusat + sebaran).

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 5

**Sub-CPMK:** 2.2 — Menggunakan pandas dan numpy untuk eksplorasi data
**Level Bloom:** C2
**Konteks:** Umum

**Jawaban:** B

**Pembahasan:**
`df['harga'].describe()` menghasilkan ringkasan lengkap: count, mean, std, min, 25%, 50%, 75%, max. Opsi lain hanya memberi sebagian: `.count()` hanya jumlah, `np.histogram` memberi frekuensi bin, `groupby` digunakan untuk agregasi per kelompok, `.unique()` memberi nilai unik.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 6

**Sub-CPMK:** 3.1 — Membuat visualisasi data yang efektif menggunakan matplotlib dan seaborn
**Level Bloom:** C3
**Konteks:** Indonesia (IHSG harian 2024)

**Jawaban:** C

**Pembahasan:**
Data *time-series* harian sepanjang setahun paling tepat ditampilkan dengan **line chart** agar tren dan pola temporal terlihat. Pie chart untuk proporsi kategori (bukan waktu); bar chart horizontal untuk perbandingan kategori; box plot tunggal tidak merepresentasikan dinamika waktu; scatter tanpa sumbu waktu menghilangkan informasi temporal.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 7

**Sub-CPMK:** 3.2 — Menerapkan prinsip storytelling with data untuk komunikasi temuan
**Level Bloom:** C4
**Konteks:** Umum

**Jawaban:** B

**Pembahasan:**
*Truncated y-axis* (sumbu Y tidak mulai dari 0) mendistorsi persepsi besaran relatif — lompatan 2% terlihat seperti 50%. Ini pelanggaran utama prinsip *visual integrity* (Tufte/Knaflic). Opsi A/C/D/E adalah pilihan desain yang tidak secara inheren menyesatkan (warna dan dua tahun OK selama skala jujur).

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 8

**Sub-CPMK:** 4.1 — Menghitung probabilitas dasar, conditional probability, dan menerapkan Bayes' theorem
**Level Bloom:** C3
**Konteks:** Islami (pembagian warisan)

**Jawaban:** D

**Pembahasan:**
Istri = 1/8, anak laki-laki = sisa = 1 − 1/8 = **7/8**. Proporsi ini berlaku pula sebagai "peluang" alokasi harta jika ditarik satu Rupiah acak. Opsi A adalah bagian istri (distraktor umum); B/C bilangan hafalan umum namun bukan sisa 1/8; E salah karena istri tetap dapat bagian.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 9

**Sub-CPMK:** 4.1 — Menghitung probabilitas dasar, conditional probability, dan menerapkan Bayes' theorem
**Level Bloom:** C4
**Konteks:** Indonesia (skrining TB)

**Jawaban:** C

**Pembahasan:**
Dengan Bayes:
- P(sakit) = 0,01; P(sehat) = 0,99
- P(pos|sakit) = 0,90; P(pos|sehat) = 1 − 0,95 = 0,05
- P(pos) = 0,90·0,01 + 0,05·0,99 = 0,009 + 0,0495 = 0,0585
- P(sakit|pos) = (0,90·0,01) / 0,0585 = 0,009 / 0,0585 ≈ **0,154 (15,4%)**

Opsi A (0,90) adalah jebakan klasik — itu sensitivitas, bukan posterior. Prevalensi rendah menekan posterior meski sensitivitas tinggi.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 10

**Sub-CPMK:** 4.2 — Mensimulasikan eksperimen probabilitas menggunakan Python
**Level Bloom:** C3
**Konteks:** Umum

**Jawaban:** B

**Pembahasan:**
Hukum bilangan besar: simulasi Monte Carlo konvergen ke nilai teoretis (1/6 ≈ 0,1667). Selisih 0,0005 adalah *sampling variation* normal. Bila simulasi diperbesar ke 1.000.000, hasilnya akan lebih dekat ke 0,1667. Opsi C salah (probabilitas riil tetap 1/6), D berlebihan, E mengabaikan teori.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 11

**Sub-CPMK:** 5.1 — Mengidentifikasi dan menerapkan distribusi probabilitas (Normal, Binomial, Poisson)
**Level Bloom:** C2
**Konteks:** Umum

**Jawaban:** B

**Pembahasan:**
Poisson memang dicirikan oleh satu parameter λ. A salah (Binomial diskret, parameter n & p). C salah (Normal tidak dibatasi n). D salah (Binomial untuk jumlah sukses, bukan waktu kontinu — gunakan Eksponensial). E salah (Normal: μ dan σ).

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 12

**Sub-CPMK:** 5.2 — Menjelaskan dan mendemonstrasikan Central Limit Theorem
**Level Bloom:** C4
**Konteks:** Umum

**Jawaban:** B

**Pembahasan:**
CLT: untuk n cukup besar, distribusi x̄ ~ N(μ, σ/√n) meskipun populasi tidak normal. A salah (populasi belum tentu normal). C membalik arah CLT. D salah — varians sampel punya estimator s²; bukan klaim CLT. E salah — CLT berlaku untuk diskret maupun kontinu.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 13

**Sub-CPMK:** 6.1 — Menerapkan teknik sampling dan menghitung confidence interval
**Level Bloom:** C3
**Konteks:** JTBD (pengeluaran harian pribadi)

**Jawaban:** B

**Pembahasan:**
Interpretasi CI yang benar adalah *frequentist*: bila prosedur diulang banyak kali, ~95% interval akan memuat parameter populasi. A adalah kesalahpahaman Bayesian umum (parameter dianggap acak). C salah (CI bukan tentang data individual). D/E salah.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 14

**Sub-CPMK:** 7.1 — Melaksanakan uji hipotesis (z-test, t-test) dan menginterpretasi p-value
**Level Bloom:** C3
**Konteks:** Umum

**Jawaban:** B

**Pembahasan:**
Kaidah: jika p-value < α, tolak H₀. 0,018 < 0,05 → tolak H₀, ada bukti statistik mendukung H₁. A salah (kriteria yang dipakai bukan p > 0). C membalik logika. D/E salah.

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

### PG No. 15

**Sub-CPMK:** 7.2 — Menjelaskan error Type I/II dan effect size
**Level Bloom:** C4
**Konteks:** Umum

**Jawaban:** A

**Pembahasan:**
Definisi standar: **Tipe I** (α) = menolak H₀ yang benar (*false positive*); **Tipe II** (β) = gagal menolak H₀ yang salah (*false negative*). B membalik arah. C salah (dua konsep berbeda). D salah (β ≠ 1 − α). E salah (keduanya bisa terjadi di uji satu- maupun dua-sisi).

**Rubrik:** Benar = 2 poin | Salah/Kosong = 0 poin

---

## BAGIAN II — KUNCI ESAI (3 × 10 pt = 30 pt)

### Esai No. E1

**Sub-CPMK:** 1.3 — Menjelaskan prinsip etika data dan responsible AI
**Level Bloom:** C4
**Konteks:** Islami + Indonesia (data donatur masjid)

**Jawaban Ideal:**

**(a) Tiga prinsip etika data yang paling relevan (pilih 3 dari daftar berikut, contoh ideal):**

1. **Informed consent** — donatur berhak tahu untuk apa data mereka digunakan & menyetujuinya; data yang dikumpulkan untuk administrasi masjid tidak otomatis boleh dipakai untuk pemasaran fintech.
2. **Purpose limitation** — data harus digunakan hanya sesuai tujuan pengumpulan awal (kepentingan masjid), bukan ditransfer ke pihak ketiga untuk tujuan komersial yang berbeda.
3. **Privacy / data minimization** — data identitas (NIK, alamat, nominal) adalah data sensitif; hanya data seperlunya yang boleh diungkap, dan sebaiknya dalam bentuk anonim/agregat.

(Jawaban alternatif yang dapat diterima: *accountability*, *transparency*, *fairness*, *data protection*.)

**(b) Argumentasi keputusan:**
Pengurus **tidak boleh** menyerahkan data tersebut secara mentah karena data dikumpulkan untuk tujuan administrasi donasi, bukan untuk kerja sama komersial — artinya tidak ada *informed consent* untuk penggunaan sekunder ini. Dari sudut Islami, data jamaah merupakan **amanah** yang harus dijaga. Kerja sama hanya etis bila memenuhi syarat: (1) meminta persetujuan ulang (*opt-in*) dari donatur untuk tujuan baru, (2) menjelaskan manfaat & risiko, (3) menandatangani perjanjian yang membatasi penggunaan, serta (4) hanya membagikan data yang benar-benar diperlukan.

**(c) Dua langkah mitigasi praktis:**
1. **Anonimisasi / agregasi**: hilangkan NIK dan nama — bagikan hanya data agregat (mis. distribusi nominal donasi per segmen umur) tanpa identitas individu.
2. **Opt-in berbasis formulir baru**: kirim pemberitahuan ke donatur, minta persetujuan eksplisit, sertakan mekanisme *opt-out* dan batas waktu penggunaan data.

**Rubrik Penskoran (Total 10 poin):**

| Kriteria                                                                             | Poin |
|--------------------------------------------------------------------------------------|------|
| (a) Menyebutkan & menjelaskan 3 prinsip etika data yang relevan (masing-masing ~1,33 pt) | 4    |
| (b) Argumentasi keputusan jelas, terstruktur, menyebut syarat etis                   | 4    |
| (c) Dua langkah mitigasi praktis, konkret & realistis (2 pt × 1 masing-masing)        | 2    |

**Aturan Partial Credit:**
- 2 prinsip benar & dijelaskan → maksimal 3/4 pada (a); 1 prinsip → maksimal 1,5/4.
- (b) hanya memberi keputusan tanpa argumentasi → maksimal 2/4.
- (c) menyebut mitigasi tanpa penjelasan implementatif → maksimal 1/2.
- Bonus tidak berlaku; total (a)+(b)+(c) dibatasi 10.

---

### Esai No. E2

**Sub-CPMK:** 3.2 — Menerapkan prinsip storytelling with data untuk komunikasi temuan
**Level Bloom:** C5
**Konteks:** Indonesia (chart IHSG)

**Jawaban Ideal:**

**(a) Tiga kesalahan utama (pilih 3 dari daftar berikut):**

1. **Truncated y-axis** — sumbu Y dimulai dari 7.200 (bukan 0), menyebabkan kenaikan 1,8% terlihat seperti lompatan ~3x lipat. Ini mendistorsi persepsi besaran perbedaan (pelanggaran *visual integrity*).
2. **Pilihan warna menyesatkan (biased encoding)** — merah menyala + gradien + panah ke atas untuk 2024 vs abu-abu pudar untuk 2023 menciptakan *narrative bias* yang membesar-besarkan cerita "meroket", bukan menyajikan data secara netral.
3. **Minim anotasi & konteks** — tidak ada label nilai pasti (7.272 → 7.402), tidak ada sumber data, tidak ada catatan skala. Pembaca tidak bisa verifikasi magnitudo sebenarnya.
4. (Alternatif yang dapat diterima: *chart type yang tidak tepat* — bar chart untuk 2 titik time-series lebih baik disajikan sebagai line chart periodik; atau *judul sensasional* yang bias.)

**(b) Empat perbaikan konkret:**
1. **Mulai sumbu Y dari 0** (atau jika memang perlu zoom, tampilkan *broken axis* dengan tanda jelas) agar perbandingan proporsional.
2. **Tampilkan nilai pasti** di atas tiap bar (7.272 dan 7.402) + delta (+130 poin, +1,8%).
3. **Warna netral / konsisten** — pakai satu palet dengan kontras seperlunya; hindari gradien & panah emosional.
4. **Sertakan sumber data** (mis. IDX / BEI), periode (Des 2023 vs Des 2024), catatan kaki skala, dan judul yang faktual (mis. "IHSG Des 2023 vs Des 2024: Naik 1,8%").

**Rubrik Penskoran (Total 10 poin):**

| Kriteria                                                                          | Poin |
|-----------------------------------------------------------------------------------|------|
| (a) Identifikasi 3 kesalahan dengan penjelasan "mengapa menyesatkan" (2 pt × 3)   | 6    |
| (b) Minimal 4 perbaikan konkret & relevan (1 pt × 4)                               | 4    |

**Aturan Partial Credit:**
- 2 kesalahan teridentifikasi & dijelaskan → maksimal 4/6; 1 kesalahan → maksimal 2/6.
- Menyebut kesalahan tanpa penjelasan ("mengapa salah") → setengah poin untuk item tersebut.
- (b) < 4 perbaikan → 1 pt per perbaikan; perbaikan generik tanpa spesifik (mis. "perbaiki saja warnanya") → setengah poin.

---

### Esai No. E3

**Sub-CPMK:** 7.1 — Melaksanakan uji hipotesis (z-test, t-test) dan menginterpretasi p-value
**Level Bloom:** C4
**Konteks:** JTBD (klaim kalori pribadi)

**Jawaban Ideal:**

**(a) Hipotesis (uji satu-sisi, sisi kanan):**
- H₀: μ = 2000 kkal (klaim Anda benar)
- H₁: μ > 2000 kkal (dugaan teman: asupan sebenarnya lebih besar)

Uji **satu-sisi (kanan)** karena dugaan teman menunjuk arah spesifik "lebih dari", bukan sekadar "berbeda".

**(b) α = 0,05** adalah taraf konvensional (risiko kesalahan tipe I 5%) — cukup ketat untuk klaim pribadi dan sejalan dengan konvensi akademik/praktis.

**Statistik uji: t-test 1-sampel** dipilih karena: (i) standar deviasi populasi σ tidak diketahui (yang diketahui hanya s sampel), (ii) n = 10 kecil sehingga distribusi sampel mengikuti t dengan df = n − 1 = 9.

Rumus:
```
t = (x̄ − μ₀) / (s / √n)
```

**(c) Daerah kritis & perhitungan:**
- df = 9, α = 0,05 satu-sisi → **t_kritis = 1,833** (tabel t). Daerah kritis: t > 1,833.
- Substitusi: t = (2150 − 2000) / (200 / √10) = 150 / (200 / 3,162) = 150 / 63,246 ≈ **2,372**.

**(d) Keputusan & interpretasi praktis:**
t_hitung (2,372) > t_kritis (1,833) → **Tolak H₀** pada α = 0,05.

Interpretasi: "Berdasarkan 10 hari pencatatan, ada bukti statistik yang cukup (pada tingkat keyakinan 95%) bahwa asupan kalori harian saya sebenarnya **lebih dari 2000 kkal**. Dugaan teman saya didukung data."

**Rubrik Penskoran (Total 10 poin):**

| Kriteria                                                              | Poin |
|-----------------------------------------------------------------------|------|
| (a) H₀, H₁ ditulis benar + uji satu-sisi dengan alasan                | 2    |
| (b) Justifikasi α + pilihan t-test + rumus benar                      | 3    |
| (c) Daerah kritis df=9 t=1,833 + substitusi benar → t ≈ 2,37          | 3    |
| (d) Keputusan tolak H₀ + interpretasi praktis 1-2 kalimat yang tepat  | 2    |

**Aturan Partial Credit:**
- Salah arah uji (dua-sisi) tetapi logika konsisten → -1 pada (a) + penyesuaian daerah kritis di (c).
- Rumus benar tapi salah hitung 1 langkah → -1 pada (c).
- Keputusan benar tanpa interpretasi bahasa praktis → -1 pada (d).
- Memakai z-test dengan n=10 tanpa σ populasi → -2 (pilihan statistik salah).

---

## BAGIAN III — KUNCI HITUNG / INTERPRETASI (40 pt)

### Hitung No. H1

**Sub-CPMK:** 2.1 — Menghitung dan menginterpretasi ukuran pemusatan dan penyebaran data
**Level Bloom:** C3
**Konteks:** Indonesia (harga beras 10 provinsi)

**Data/Skenario:** 10 harga beras (Rp/kg, sudah terurut): 11.000, 11.500, 12.000, 12.000, 12.500, 13.000, 13.500, 13.500, 14.000, 14.500.

**Langkah Perhitungan:**

**(a) Mean (x̄):**

1. Rumus: x̄ = (Σ xᵢ) / n
2. Substitusi: Σ xᵢ = 11.000 + 11.500 + 12.000 + 12.000 + 12.500 + 13.000 + 13.500 + 13.500 + 14.000 + 14.500 = **127.500**
3. Hasil: x̄ = 127.500 / 10 = **Rp 12.750 / kg**

**(b) Median & Modus:**

1. Median = rata-rata data ke-5 & ke-6 = (12.500 + 13.000) / 2 = **Rp 12.750 / kg**
2. Modus = nilai yang muncul paling sering = **Rp 12.000 dan Rp 13.500** (bimodal, masing-masing muncul 2×)

**(c) Standar deviasi sampel (s):**

1. Rumus: s = √[ Σ(xᵢ − x̄)² / (n − 1) ]
2. Deviasi (xᵢ − x̄) untuk x̄ = 12.750:

| xᵢ     | (xᵢ − x̄) | (xᵢ − x̄)²     |
|--------|-----------|----------------|
| 11.000 | −1.750    | 3.062.500      |
| 11.500 | −1.250    | 1.562.500      |
| 12.000 | −750      | 562.500        |
| 12.000 | −750      | 562.500        |
| 12.500 | −250      | 62.500         |
| 13.000 | +250      | 62.500         |
| 13.500 | +750      | 562.500        |
| 13.500 | +750      | 562.500        |
| 14.000 | +1.250    | 1.562.500      |
| 14.500 | +1.750    | 3.062.500      |
| **Σ**  | 0         | **11.625.000** |

3. s² = 11.625.000 / (10 − 1) = 11.625.000 / 9 ≈ **1.291.666,67**
4. s = √1.291.666,67 ≈ **Rp 1.136,43 / kg** (boleh dibulatkan Rp 1.136 atau ≈ Rp 1.137 / kg).

**(d) Q1, Q3, IQR:**

Metode interpolasi (posisi (n+1)·p):

- Posisi Q1 = (10+1) × 0,25 = 2,75 → antara data ke-2 (11.500) & ke-3 (12.000)
  Q1 = 11.500 + 0,75 × (12.000 − 11.500) = 11.500 + 375 = **Rp 11.875 / kg**
- Posisi Q3 = (10+1) × 0,75 = 8,25 → antara data ke-8 (13.500) & ke-9 (14.000)
  Q3 = 13.500 + 0,25 × (14.000 − 13.500) = 13.500 + 125 = **Rp 13.625 / kg**
- IQR = Q3 − Q1 = 13.625 − 11.875 = **Rp 1.750 / kg**

(Metode alternatif — membagi dua setengah bawah/atas tanpa median: Q1 = 12.000, Q3 = 13.500, IQR = 1.500. Jawaban dengan metode eksplisit yang konsisten dapat diterima.)

**(e) Interpretasi:**

Mean ≈ Median = Rp 12.750/kg → sebaran harga beras **cenderung simetris**. Deviasi dari Q2 ke Q1 (12.750 − 11.875 = 875) ≈ deviasi Q2 ke Q3 (13.625 − 12.750 = 875) juga memperkuat kesan simetri. Standar deviasi ~ Rp 1.136 dari mean Rp 12.750 menunjukkan variasi harga antar-provinsi yang moderat (~9%), tidak ekstrem.

**Rubrik Penskoran (Total 13 poin):**

| Kriteria                                              | Poin |
|-------------------------------------------------------|------|
| (a) Rumus mean + hitung Σxᵢ + hasil 12.750 benar      | 2    |
| (b) Median benar + modus bimodal teridentifikasi       | 2    |
| (c) Rumus s, tabel deviasi kuadrat, s ≈ 1.136         | 4    |
| (d) Q1 = 11.875 + Q3 = 13.625 + IQR = 1.750           | 3    |
| (e) Interpretasi simetri berdasarkan mean vs median   | 2    |

**Aturan Partial Credit:**
- Rumus benar tapi salah hitung 1 langkah → -30% poin bagian perhitungan.
- Metode kuartil alternatif konsisten (Q1=12.000, Q3=13.500, IQR=1.500) → nilai penuh (3 pt) bila logika ditulis eksplisit.
- Lupa n−1 di SD (pakai n) → -2 (tetap hitung s² populasi).
- Interpretasi benar meski angka sedikit salah → tetap beri 1/2.

---

### Hitung No. H2

**Sub-CPMK:** 5.1, 5.2 — Mengidentifikasi dan menerapkan distribusi probabilitas (Normal, Binomial, Poisson); Menjelaskan dan mendemonstrasikan Central Limit Theorem
**Level Bloom:** C3
**Konteks:** JTBD (jarak lari mingguan)

**Data/Skenario:** X ~ N(μ = 5,0; σ = 0,8) dalam km.

**Langkah Perhitungan:**

**(a) P(X > 6):**

1. Rumus Z-score: Z = (X − μ) / σ
2. Substitusi: Z = (6 − 5,0) / 0,8 = 1 / 0,8 = **1,25**
3. Dari tabel Z: P(Z ≤ 1,25) = 0,8944 → **P(Z > 1,25) = 1 − 0,8944 = 0,1056**
4. Hasil: P(X > 6) ≈ **0,1056 atau 10,56%**

Interpretasi: sekitar 10,6% sesi, Anda berlari lebih dari 6 km.

**(b) P(4,2 < X < 5,8):**

1. Z₁ = (4,2 − 5,0) / 0,8 = −0,8 / 0,8 = **−1,00**
2. Z₂ = (5,8 − 5,0) / 0,8 = 0,8 / 0,8 = **+1,00**
3. P(−1 < Z < 1) = P(Z < 1) − P(Z < −1) = 0,8413 − (1 − 0,8413) = 0,8413 − 0,1587 = **0,6826**
4. Hasil: P(4,2 < X < 5,8) ≈ **0,6826 atau 68,26%** — konsisten dengan aturan empiris ±1σ.

**(c) P(x̄ > 5,2) untuk n = 16 (CLT):**

1. Distribusi sampling: x̄ ~ N(μ, σ/√n) = N(5,0; 0,8/√16) = N(5,0; 0,2)
2. Standard error: SE = σ/√n = 0,8/4 = **0,2**
3. Z = (x̄ − μ) / SE = (5,2 − 5,0) / 0,2 = 0,2 / 0,2 = **1,00**
4. P(Z > 1,00) = 1 − 0,8413 = **0,1587**
5. Hasil: P(x̄ > 5,2) ≈ **0,1587 atau 15,87%**

Interpretasi: peluang rata-rata jarak 16 sesi melebihi 5,2 km hanya ~15,9%, jauh lebih kecil dari probabilitas satu sesi individual melebihi 5,2 km (sekitar 40%). Inilah efek "rata-rata sampel lebih stabil" dari CLT.

**Rubrik Penskoran (Total 13 poin):**

| Kriteria                                                        | Poin |
|-----------------------------------------------------------------|------|
| (a) Rumus Z + Z = 1,25 + baca tabel → 0,1056                    | 4    |
| (b) Z₁ = −1, Z₂ = 1 + P(−1 < Z < 1) = 0,6826                    | 4    |
| (c) SE = 0,2 + Z = 1 + P(Z > 1) = 0,1587 + interpretasi CLT     | 5    |

**Aturan Partial Credit:**
- Rumus benar tapi salah konversi Z → -1 per bagian.
- Lupa membagi √n di SE (pakai σ langsung) → -3 pada (c).
- Nilai tabel sedikit berbeda (mis. 0,8944 vs 0,8925) → terima selama selisih < 0,005.
- Interpretasi benar meski perhitungan sedikit salah → beri 50% bagian interpretasi.

---

### Hitung No. H3

**Sub-CPMK:** 7.1 — Melaksanakan uji hipotesis (z-test, t-test) dan menginterpretasi p-value
**Level Bloom:** C4
**Konteks:** Indonesia (klaim TransJakarta)

**Data/Skenario:** Klaim μ ≤ 45 menit; sampel n = 16, x̄ = 48, s = 6; α = 0,05; populasi diasumsikan approximately normal.

**Langkah Perhitungan:**

**(a) Hipotesis (uji satu-sisi, sisi kanan):**
- **H₀: μ ≤ 45 menit** (klaim TransJakarta benar — rata-rata waktu tempuh tidak melebihi 45 menit)
- **H₁: μ > 45 menit** (waktu tempuh sebenarnya lebih dari 45 menit)

Alasan uji satu-sisi: kita hanya peduli arah spesifik "melebihi" klaim — tidak tertarik pada kemungkinan waktu tempuh jauh lebih cepat.

**(b) Pemilihan statistik uji:**

Gunakan **t-test 1-sampel** karena: (i) σ populasi tidak diketahui (hanya s sampel), (ii) n = 16 relatif kecil (< 30). Distribusi sampling x̄ mengikuti t-distribusi dengan **df = n − 1 = 15**.

Rumus:
```
t = (x̄ − μ₀) / (s / √n)
```

**(c) Perhitungan nilai t:**

1. s / √n = 6 / √16 = 6 / 4 = **1,5**
2. Selisih: x̄ − μ₀ = 48 − 45 = **3**
3. t = 3 / 1,5 = **2,0**

**(d) Daerah kritis & perbandingan:**

- df = 15, α = 0,05 satu-sisi → dari tabel t: **t_kritis = 1,753**.
- Daerah kritis: t > 1,753.
- Perbandingan: t_hitung = **2,0** > t_kritis = **1,753** → statistik uji jatuh di daerah kritis.

**(e) Keputusan & interpretasi:**

**Tolak H₀** pada α = 0,05.

Interpretasi praktis untuk manajemen TransJakarta: *"Berdasarkan sampel 16 perjalanan, ada bukti statistik yang cukup (pada tingkat keyakinan 95%) bahwa rata-rata waktu tempuh rute X **lebih dari 45 menit**. Klaim 'waktu tempuh ≤ 45 menit' tidak terbukti; perlu evaluasi operasional (kepadatan lalu lintas, halte transit, frekuensi armada) untuk memperbaiki kinerja rute."*

**Rubrik Penskoran (Total 14 poin):**

| Kriteria                                                              | Poin |
|-----------------------------------------------------------------------|------|
| (a) H₀, H₁ benar + identifikasi satu-sisi kanan beserta alasan        | 2    |
| (b) Pilih t-test (alasan σ tidak diketahui, n kecil) + rumus benar    | 3    |
| (c) Substitusi angka: s/√n = 1,5; selisih = 3; t = 2,0                | 3    |
| (d) df=15 t_kritis=1,753 + perbandingan benar (t_hitung > t_kritis)   | 3    |
| (e) Keputusan "tolak H₀" + interpretasi praktis bahasa manajerial     | 3    |

**Aturan Partial Credit:**
- Uji dua-sisi tetapi logika konsisten → -1 pada (a), t_kritis jadi 2,131 (boleh, keputusan "tidak tolak H₀" bila konsisten → -0 untuk (d) & (e) dengan interpretasi yang tepat).
- Z-test keliru dipakai → -2 pada (b) (pilihan statistik salah), perhitungan selanjutnya dinilai dengan rumus yang dipakai.
- Rumus benar tapi salah hitung 1 langkah → -1 pada (c).
- Keputusan benar tanpa interpretasi manajerial → -1 pada (e).

---

## RINGKASAN DISTRIBUSI

### Tabel A — Pemetaan Sub-CPMK → Nomor Soal → Poin

| Sub-CPMK | Deskripsi (ringkas)                                  | Nomor Soal          | Total Poin |
|----------|------------------------------------------------------|---------------------|-----------:|
| 1.1      | Peran statistika di era DS/AI                        | PG #1               | 2          |
| 1.3      | Etika data & responsible AI                          | PG #2, E1           | 12         |
| 2.1      | Ukuran pemusatan & penyebaran                        | PG #3, PG #4, H1    | 17         |
| 2.2      | pandas/numpy untuk eksplorasi                        | PG #5               | 2          |
| 3.1      | Visualisasi data (matplotlib/seaborn)                | PG #6               | 2          |
| 3.2      | Storytelling with data                               | PG #7, E2           | 12         |
| 4.1      | Probabilitas dasar, conditional, Bayes               | PG #8, PG #9        | 4          |
| 4.2      | Simulasi probabilitas dengan Python                  | PG #10              | 2          |
| 5.1      | Distribusi probabilitas (Normal/Binomial/Poisson)    | PG #11, H2 (1/2)    | 8,5        |
| 5.2      | Central Limit Theorem                                | PG #12, H2 (1/2)    | 8,5        |
| 6.1      | Sampling & confidence interval                       | PG #13              | 2          |
| 7.1      | Uji hipotesis (z/t-test) & p-value                   | PG #14, E3, H3      | 26         |
| 7.2      | Error Tipe I/II & effect size                        | PG #15              | 2          |
| **Total**|                                                      |                     | **100**    |

*Catatan:* H2 (13 pt) memetakan 5.1 + 5.2 (masing-masing 6,5 pt untuk perhitungan distribusi Normal dan bagian CLT).

### Tabel B — Distribusi Level Bloom

| Level | Jumlah Soal | Rincian Poin                                     | Total Poin | % Poin |
|-------|-------------|--------------------------------------------------|-----------:|-------:|
| C2    | 4           | PG #1 + PG #2 + PG #5 + PG #11 = 4×2             | 8          | 8%     |
| C3    | 9           | PG #3, #4, #6, #8, #10, #13, #14 (7×2) + H1 + H2 = 14 + 26 | 40         | 40%    |
| C4    | 7           | PG #7, #9, #12, #15 (4×2) + E1 + E3 + H3 = 8+10+10+14      | 42         | 42%    |
| C5    | 1           | E2 = 10                                          | 10         | 10%    |
| **Total** | **21**  |                                                  | **100**    | 100%   |

*Catatan:* Distribusi memenuhi target aplikasi-berat: C2 = 8% (≤ 20%), C3+C4 = 82% (dominasi aplikasi), C4+C5 = 52% (analisis–evaluasi). Toleransi ±1 soal per level terpenuhi.

### Tabel C — Distribusi Konteks

| Konteks            | Jumlah Soal | Nomor Soal                                              |
|--------------------|-------------|---------------------------------------------------------|
| Umum               | 8           | PG #1, #5, #7, #10, #11, #12, #14, #15                  |
| Indonesia          | 6           | PG #3, #6, #9, E2, H1, H3                               |
| JTBD personal      | 4           | PG #4, PG #13, E3, H2                                   |
| Islami             | 3           | PG #2, PG #8, E1                                        |
| **Total**          | **21**      |                                                         |

---

**Akhir Kunci Jawaban — Semoga Allah memberi keberkahan pada setiap penilaian yang adil.**

> *"Fa'in 'amiltum fa-innamaa ta'maluuna li-anfusikum."*
> (Maka jika kamu beramal, sesungguhnya kamu beramal untuk dirimu sendiri.)
