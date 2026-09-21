# Minggu 12: Analisis Data dan Penarikan Simpulan

---

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata kuliah | Metodologi Penelitian (`IF52510021`) |
| Minggu | 12 dari 16 |
| Topik | Merencanakan analisis sebelum data ada |
| Sub-CPMK | `METPEN-Sub-CPMK071-1` |
| ICM | ICM-11 — Menyusun rencana analisis data yang sesuai dengan RQ dan jenis datanya |
| Durasi | 2 × 50 menit |
| Metode | Kuliah + lokakarya + **Kuis 3** |
| Bacaan | [Bab 11 — Analisis Data dan Penarikan Simpulan](../06-buku-ajar/bab-11-analisis-data-dan-penarikan-simpulan.md) |

---

## Tujuan Pembelajaran

1. **Memilih** (C4) teknik analisis yang sesuai RQ dan jenis data.
2. **Menyusun** (C3) rencana analisis yang ditetapkan sebelum data terkumpul.
3. **Menjelaskan** (C2) asumsi metode dan cara memeriksanya.
4. **Merumuskan** (C4) apa yang akan menjadi bukti bahwa dugaan tidak didukung.

---

## Materi Pembelajaran

### 12.1 Rencana Analisis Ditetapkan di Muka

| Bila rencana disusun sesudah data ada | Akibatnya |
|---------------------------------------|-----------|
| Peneliti mencoba banyak analisis | Salah satunya akan tampak berarti secara kebetulan |
| Hipotesis disesuaikan dengan hasil | Penelitian kehilangan daya ujinya |
| Bagian data yang tidak cocok tersisih | Simpulan bias |

Praktik yang menghindarinya: menuliskan rencana analisis **sebelum
pengumpulan data dimulai**, dan melaporkan penyimpangan dari rencana itu
beserta alasannya.

> Praktik ini dikenal sebagai *preregistration* dan kini lazim di banyak
> bidang. Untuk Tugas Akhir, tidak perlu didaftarkan pada lembaga mana pun;
> cukup **ditulis, diberi tanggal, dan dilampirkan dalam proposal**.

### 12.2 Analisis Kuantitatif

| RQ berbentuk | Data | Analisis |
|--------------|------|----------|
| Berapa banyak, seberapa sering | Nominal/ordinal | Frekuensi, persentase, modus |
| Seberapa besar rata-rata | Interval/rasio | Rerata, simpangan baku, interval kepercayaan |
| Apakah dua kelompok berbeda | Interval/rasio | Uji t, Mann-Whitney |
| Apakah >2 kelompok berbeda | Interval/rasio | ANOVA, Kruskal-Wallis |
| Apakah dua variabel berhubungan | Interval/rasio | Korelasi Pearson/Spearman |
| Apakah kategori berhubungan | Nominal | Uji chi-kuadrat |
| Memprediksi Y dari beberapa X | Interval/rasio | Regresi |

| Yang wajib dinyatakan | Mengapa |
|-----------------------|---------|
| Asumsi tiap uji | Uji yang asumsinya dilanggar menghasilkan simpulan keliru |
| Cara memeriksa asumsi | Normalitas, homogenitas ragam, kemandirian |
| Apa yang dilakukan bila asumsi tidak terpenuhi | Uji nonparametrik atau transformasi |
| Besar efek, bukan hanya nilai p | Nilai p tidak menyatakan besarnya perbedaan |

Baris terakhir perlu ditegaskan. Perbedaan yang signifikan secara statistik
dapat sangat kecil dan tidak berarti secara praktis. **Besar efek** (*effect
size*) menyatakan seberapa besar perbedaannya, dan pelaporannya kini menjadi
standar.

### 12.3 Analisis Kualitatif

| Tahap | Kegiatan |
|-------|----------|
| 1. Pengenalan data | Membaca seluruh transkrip; mencatat kesan awal |
| 2. Penandaan awal | Memberi penanda pada potongan yang bermakna |
| 3. Pengelompokan | Menyusun penanda menjadi tema kandidat |
| 4. Peninjauan tema | Memeriksa tema terhadap data; menggabungkan atau memecah |
| 5. Penamaan tema | Memberi nama yang tepat dan definisi |
| 6. Pelaporan | Menyusun narasi dengan kutipan pendukung |

| Yang wajib dilaporkan | Bentuknya |
|-----------------------|-----------|
| Cara penandaan | Induktif (dari data) atau deduktif (dari kerangka) |
| Jumlah penanda dan tema | Angka nyata |
| Kutipan pendukung tiap tema | Verbatim, dengan kode responden |
| **Kasus yang tidak sesuai tema** | Dilaporkan, tidak dibuang |
| Pemeriksaan kesesuaian | Bila ada penandaan silang |

### 12.4 Dari Temuan ke Simpulan

```
DATA          →  TEMUAN         →  TAFSIRAN      →  SIMPULAN
"12 dari 18      "Sebagian besar   "Hambatan        "RQ1 terjawab:
 menyebut         responden         pelatihan        faktor utama
 pelatihan"       menyebut          bersifat         yang disebut
                  pelatihan"        struktural,      adalah ...,
                                    bukan            dengan batasan
                                    individual"      bahwa ..."
```

| Lompatan yang sering terjadi | Bentuknya |
|------------------------------|-----------|
| Dari temuan langsung ke simpulan besar | "Pelatihan tidak memadai" → "Sistem gagal karena kebijakan pemerintah" |
| Dari korelasi ke sebab | "Berhubungan" → "menyebabkan" |
| Dari sampel ke populasi | 18 responden satu dinas → "staf pemerintah pada umumnya" |
| Dari tidak signifikan ke tidak ada | "p > 0,05" → "tidak ada perbedaan" |

Baris terakhir adalah kekeliruan logika yang sangat umum. Tidak ditemukannya
bukti perbedaan **bukan** bukti tidak adanya perbedaan — terutama pada
sampel kecil, yang memang tidak berdaya mendeteksi perbedaan kecil.

### 12.5 Apa yang Menjadi Bukti Penolakan

Bagian rencana analisis yang paling sering hilang dan paling menentukan:

```markdown
## Kriteria Penolakan Dugaan

Dugaan   : Keterjelasan sistem berhubungan negatif dengan
           niat menghentikan pemakaian.

Didukung bila  : Korelasi negatif, p < 0,05, |r| ≥ 0,3
Tidak didukung : |r| < 0,3 atau p ≥ 0,05
Tidak dapat
disimpulkan    : Sampel terkumpul < 60; asumsi dilanggar
                 dan alternatif nonparametrik juga tidak
                 memenuhi syarat

Yang akan dilaporkan dalam ketiga keadaan: seluruhnya.
```

Baris terakhir menegaskan hal yang sering tidak dipahami: **hasil yang tidak
mendukung dugaan tetap dilaporkan dan tetap merupakan hasil**. Penelitian
yang hanya dapat melaporkan satu kemungkinan hasil bukan penelitian.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

| # | Kegiatan |
|---|----------|
| 1 | Membaca [Bab 11](../06-buku-ajar/bab-11-analisis-data-dan-penarikan-simpulan.md) |
| 2 | Meninjau kembali catatan Probabilitas dan Statistik tentang uji hipotesis |

### Di Kelas (100 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–10 | **Kuis 3** — mencocokkan RQ, jenis data, dan analisis |
| 10–35 | Kuliah: analisis kuantitatif; asumsi; besar efek |
| 35–50 | Kuliah: analisis tematik; pelaporan yang lengkap |
| 50–60 | **Rehat** |
| 60–85 | **Lokakarya 12** — [Rencana Analisis Data](../04-labs/lab-12-rencana-analisis-data.md) |
| 85–100 | Latihan: menemukan lompatan penalaran pada 4 kutipan simpulan |

### Setelah Kelas

| # | Kegiatan |
|---|----------|
| 1 | Menyelesaikan **T11 — Rencana analisis data** (prasyarat) |
| 2 | Membaca [Bab 12](../06-buku-ajar/bab-12-design-science-dan-evaluasi-artefak.md) |

---

## Penugasan

### T11 — Rencana Analisis Data (prasyarat T14)

| Aspek | Ketentuan |
|-------|-----------|
| Keluaran | Dokumen bertanggal |
| Isi | Untuk setiap RQ: data, analisis, keluaran · asumsi metode + cara memeriksa · tindakan bila asumsi tidak terpenuhi · **kriteria penolakan dugaan** |
| Tenggat | Akhir Minggu 12 |

---

## AI Corner — Minggu 12

| Boleh | Tidak boleh |
|-------|-------------|
| Meminta AI menjelaskan asumsi sebuah uji statistik | Meminta AI memilih uji untuk data Anda tanpa Anda memahaminya |
| Meminta AI membantu menulis kode analisis | Menyerahkan kode yang tidak dapat Anda jelaskan |
| Meminta AI memeriksa apakah simpulan Anda melampaui data | Meminta AI menafsirkan hasil analisis Anda |
| Meminta AI menandai lompatan penalaran dalam draf | Meminta AI menulis bagian pembahasan |

### Kode Analisis yang Tidak Dipahami

Bantuan AI membuat penulisan kode analisis jauh lebih cepat. Bahayanya
spesifik dan serius: kode yang berjalan tanpa galat **tidak berarti analisis
yang benar**.

| Kekeliruan yang tidak menimbulkan galat | Akibat |
|-----------------------------------------|--------|
| Memakai uji t pada data ordinal | Simpulan tidak sahih |
| Tidak memeriksa asumsi normalitas | Nilai p tidak bermakna |
| Salah menentukan variabel bebas dan terikat | Simpulan terbalik |
| Data hilang ditangani diam-diam oleh pustaka | Sampel berbeda dari yang dilaporkan |
| Uji berulang tanpa koreksi | Temuan palsu |

Ketentuan mata kuliah ini: **setiap baris analisis harus dapat dijelaskan
penulisnya** — mengapa uji itu, apa asumsinya, dan apa artinya bila asumsi
dilanggar. Ini diperiksa pada pertahanan lisan Minggu 15.

### Pemakaian yang Dianjurkan

```
RQ saya : [tempelkan]
Jenis data setiap variabel : [sebutkan skala masing-masing]
Rancangan : [sebutkan]
Analisis yang saya rencanakan : [sebutkan]

Tugas Anda:
1. Sebutkan asumsi yang harus dipenuhi analisis itu.
2. Untuk setiap asumsi, sebutkan cara memeriksanya.
3. Sebutkan analisis alternatif bila asumsi tidak terpenuhi.
4. Tanyakan kepada saya hal-hal yang belum saya nyatakan
   dan diperlukan untuk menilai kesesuaian analisis ini.

Jangan menyimpulkan bahwa analisis saya sudah tepat.
```

Butir 4 sering menghasilkan pertanyaan yang menunjukkan lubang dalam rencana
— misalnya tentang penanganan data hilang atau tentang kemandirian
pengamatan.

---

## Referensi

1. Field, A. (2024). *Discovering Statistics Using IBM SPSS Statistics* (6th ed.). SAGE Publications.
2. Braun, V., & Clarke, V. (2006). Using Thematic Analysis in Psychology. *Qualitative Research in Psychology*, 3(2), 77–101.
3. Miles, M. B., Huberman, A. M., & Saldaña, J. (2020). *Qualitative Data Analysis* (4th ed.). SAGE Publications.
4. Wasserstein, R. L., & Lazar, N. A. (2016). The ASA Statement on p-Values. *The American Statistician*, 70(2), 129–133.
5. Nosek, B. A., et al. (2018). The Preregistration Revolution. *PNAS*, 115(11), 2600–2606.
6. Lakens, D. (2013). Calculating and Reporting Effect Sizes. *Frontiers in Psychology*, 4, 863.

---

## Tautan Terkait

| Jenis | Berkas |
|-------|--------|
| Bab buku ajar | [Bab 11](../06-buku-ajar/bab-11-analisis-data-dan-penarikan-simpulan.md) |
| Lokakarya | [Lokakarya 12](../04-labs/lab-12-rencana-analisis-data.md) |
| Mata kuliah terkait | [Probabilitas dan Statistik](../../probabilitas-dan-statistik/README.md) |
| Minggu sebelumnya | [Minggu 11](week-11-validitas-reliabilitas-dan-ancamannya.md) |
| Minggu berikutnya | [Minggu 13](week-13-design-science-dan-evaluasi-artefak.md) |
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
