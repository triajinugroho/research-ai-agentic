# BAB 14: PROYEK AKHIR — ANALISIS DATA STATISTIK *END-TO-END*

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `PS-Sub-CPMK081-1` | Merancang alur analisis statistik utuh dari pertanyaan sampai kesimpulan | C6 |
| `PS-Sub-CPMK102-1` | Melaksanakan analisis deskriptif, visualisasi, dan inferensi atas data nyata | C3–C4 |
| `PS-Sub-CPMK102-1` | Menilai keterbatasan analisis sendiri dan mengomunikasikannya secara jujur | C5 |

---

## Pengantar: Mengapa Ada Bab Tentang Proyek

Tiga belas bab sebelumnya mengajarkan **potongan**. Bab ini mengajarkan **rangkaiannya**.

Perbedaannya besar. Pada soal latihan, seseorang sudah memilihkan ujinya, sudah membersihkan datanya, dan sudah memastikan asumsinya terpenuhi. Yang tersisa adalah menghitung. Pada persoalan nyata, tidak satu pun dari itu tersedia. Data datang berantakan, pertanyaan datang kabur, dan tidak ada kunci jawaban di belakang buku.

Bab ini adalah peta jalan untuk menghadapi keadaan itu — dan sekaligus tempat pembahasan paling terbuka dalam buku ini tentang **bagaimana AI boleh dan tidak boleh dipakai** dalam pekerjaan analisis.

> Rincian administratif proyek — tenggat, format, dan rubrik — ada pada [Panduan Proyek](../05-assessments/project-guidelines.md). Bab ini membahas **cara berpikirnya**, bukan ketentuannya.

---

## 14.1 Anatomi Sebuah Analisis Statistik

### 14.1.1 Enam Tahap

```
┌─────────────────────────────────────────────────────────────┐
│  1. PERTANYAAN      Apa yang sebenarnya ingin diketahui?     │
│         ↓                                                    │
│  2. DATA            Dari mana, seberapa layak dipercaya?     │
│         ↓                                                    │
│  3. PEMBERSIHAN     Apa yang diubah, dibuang, dan mengapa?   │
│         ↓                                                    │
│  4. DESKRIPTIF      Seperti apa bentuk datanya?              │
│         ↓                                                    │
│  5. INFERENSI       Apa yang dapat disimpulkan di luar       │
│                     sampel ini?                              │
│         ↓                                                    │
│  6. KOMUNIKASI      Apa yang dapat DAN TIDAK DAPAT           │
│                     disimpulkan?                             │
└─────────────────────────────────────────────────────────────┘
```

Alur ini **tidak lurus**. Tahap 4 sering memaksa kembali ke tahap 3; tahap 5 sering memaksa kembali ke tahap 1 karena ternyata pertanyaan awal tidak dapat dijawab dengan data yang ada. Bolak-balik semacam itu normal — yang tidak normal adalah menyembunyikannya.

### 14.1.2 Pembagian Waktu yang Realistis

Mahasiswa hampir selalu salah memperkirakan porsi waktu:

| Tahap | Perkiraan mahasiswa | Kenyataan |
|-------|---------------------|-----------|
| Mencari dan memperoleh data | 10% | 20% |
| Pembersihan data | 5% | **35%** |
| Analisis deskriptif | 20% | 15% |
| Analisis inferensial | **50%** | 10% |
| Penulisan dan komunikasi | 15% | 20% |

Perhitungan uji-t memakan lima menit. Memastikan bahwa kolom `provinsi` menuliskan "DI Yogyakarta", "D.I. Yogyakarta", dan "Yogyakarta" sebagai entitas yang sama memakan dua jam. Ini bukan kekurangan mata kuliah; ini memang pekerjaannya.

---

## 14.2 Tahap 1 — Merumuskan Pertanyaan

### 14.2.1 Dari Tema ke Pertanyaan

Tema bukan pertanyaan. "Kualitas udara Jakarta" adalah tema. Pertanyaan adalah kalimat yang dapat dijawab **benar atau salah** dengan data.

| Tingkat | Contoh |
|---------|--------|
| Tema | Kualitas udara Jakarta |
| Terlalu luas | Bagaimana kualitas udara Jakarta? |
| Mulai tajam | Apakah PM2.5 berbeda antar wilayah Jakarta? |
| **Dapat diuji** | **Apakah rata-rata PM2.5 harian berbeda secara signifikan antara lima stasiun pemantau DKI Jakarta sepanjang 2025?** |

Pertanyaan terakhir menyebutkan variabel (PM2.5 harian), unit pembanding (lima stasiun), periode (2025), dan secara tersirat menunjuk uji yang sesuai (ANOVA satu arah).

### 14.2.2 Uji Kelayakan Pertanyaan

Empat pertanyaan yang harus dijawab "ya" sebelum melangkah:

1. **Dapatkah dijawab dengan data yang benar-benar sudah saya buka?** Bukan data yang saya kira ada.
2. **Dapatkah dijawab dengan metode sampai Minggu 14?** Bila memerlukan regresi logistik atau analisis deret waktu, pertanyaannya harus disederhanakan.
3. **Apakah jawabannya belum saya ketahui?** Bila jawabannya sudah pasti, tidak ada yang dianalisis.
4. **Apakah saya sanggup menerima jawaban "tidak ada perbedaan"?** Bila tidak, pertanyaannya bukan pertanyaan — melainkan kesimpulan yang sedang dicarikan pembenaran.

### 14.2.3 Menyatakan Hipotesis Sejak Awal

Hipotesis ditulis **sebelum** data dilihat. Ini bukan formalitas, melainkan pencegah **HARKing** (*Hypothesizing After the Results are Known*) — merumuskan hipotesis setelah melihat hasil, lalu menyajikannya seolah-olah sudah diduga sejak awal.

```
H₀: μ₁ = μ₂ = μ₃ = μ₄ = μ₅
   (rata-rata PM2.5 harian sama di kelima stasiun)

H₁: sekurang-kurangnya satu stasiun memiliki rata-rata berbeda

α = 0,05     Uji: ANOVA satu arah
```

Menuliskannya di proposal Minggu 6 dan menyerahkannya sebelum analisis dimulai membuat disiplin ini dapat diperiksa.

---

## 14.3 Tahap 2 — Memperoleh dan Menilai Data

### 14.3.1 Yang Harus Dicatat pada Saat Mengunduh

| Butir | Mengapa penting |
|-------|-----------------|
| URL lengkap | Agar dapat ditelusuri ulang |
| Tanggal akses | Data terbuka sering diperbarui diam-diam |
| Jumlah baris dan kolom **saat diunduh** | Pembanding setelah pembersihan |
| Lisensi / ketentuan pakai | Amanah dalam memakai karya orang lain |
| Definisi tiap variabel | Tanpa ini, angka tidak bermakna |

Butir terakhir sering dilewati dan paling mahal akibatnya. "Jumlah penduduk" pada satu berkas BPS bisa berarti hasil proyeksi pertengahan tahun, sedangkan pada berkas lain berarti hasil sensus. Membandingkan keduanya seolah-olah setara menghasilkan kesimpulan yang salah sejak baris pertama.

### 14.3.2 Pemeriksaan Kelayakan Awal

```python
import pandas as pd

df = pd.read_csv("data_ipm_provinsi_2025.csv")

# 1. Bentuk data
print("Dimensi:", df.shape)

# 2. Tipe data dan nilai hilang
print(df.info())

# 3. Ringkasan numerik — cari nilai mustahil
print(df.describe())

# 4. Nilai hilang per kolom, dalam persen
print((df.isna().mean() * 100).round(2))

# 5. Duplikat
print("Baris duplikat:", df.duplicated().sum())

# 6. Konsistensi kategori
print(df["provinsi"].value_counts())
```

Enam perintah ini menangkap sebagian besar masalah sebelum menjadi kesalahan analisis.

### 14.3.3 Tanda Bahaya

| Tanda | Kemungkinan penyebab |
|-------|----------------------|
| Nilai `-99`, `999`, atau `0` pada kolom yang mustahil nol | Kode nilai hilang yang tidak diterjemahkan |
| Rata-rata jauh dari median | Kemencengan berat atau pencilan ekstrem |
| Nilai minimum negatif pada besaran yang tidak mungkin negatif | Kesalahan pencatatan |
| Jumlah kategori lebih banyak dari yang seharusnya | Perbedaan ejaan/kapitalisasi |
| Tanggal di masa depan | Kesalahan penguraian format tanggal |
| Kolom numerik terbaca sebagai `object` | Ada pemisah ribuan atau satuan yang ikut terbaca |

---

## 14.4 Tahap 3 — Pembersihan Data sebagai Keputusan Ilmiah

### 14.4.1 Setiap Pembersihan Adalah Keputusan, Bukan Teknis Belaka

Membuang baris mengubah populasi yang diwakili sampel. Karena itu setiap keputusan pembersihan harus dicatat dengan tiga unsur: **apa** yang dilakukan, **berapa banyak** yang terpengaruh, dan **mengapa**.

```python
# Catatan pembersihan — ditulis di notebook, bukan di kepala

n_awal = len(df)

# (1) Baris tanpa nilai IPM dibuang: IPM adalah variabel utama,
#     tidak masuk akal diimputasi untuk analisis ini.
df = df.dropna(subset=["ipm"])
print(f"Dibuang karena IPM kosong: {n_awal - len(df)} baris "
      f"({(n_awal - len(df)) / n_awal * 100:.1f}%)")

# (2) Nama provinsi dibakukan sebelum pengelompokan.
df["provinsi"] = (df["provinsi"].str.strip().str.title()
                    .replace({"D.I. Yogyakarta": "DI Yogyakarta",
                              "Dki Jakarta": "DKI Jakarta"}))

# (3) Pencilan DIPERIKSA, tidak otomatis dibuang.
q1, q3 = df["ipm"].quantile([0.25, 0.75])
iqr = q3 - q1
pencilan = df[(df["ipm"] < q1 - 1.5*iqr) | (df["ipm"] > q3 + 1.5*iqr)]
print("Teridentifikasi sebagai pencilan:")
print(pencilan[["provinsi", "ipm"]])
# Keputusan: DIPERTAHANKAN. DKI Jakarta memang memiliki IPM tertinggi;
# ini data sah, bukan kesalahan pencatatan. Membuangnya akan mengubah
# populasi yang diwakili menjadi "provinsi selain DKI".
```

### 14.4.2 Kapan Pencilan Boleh Dibuang

Hanya satu alasan yang sah: **ada bukti bahwa nilainya keliru**.

| Situasi | Tindakan |
|---------|----------|
| Umur tercatat 250 tahun | Buang atau perbaiki — jelas kesalahan input |
| Suhu tubuh 3,7 °C | Perbaiki — jelas 37 °C salah titik desimal |
| Gaji 100× median, terverifikasi benar | **Pertahankan** — laporkan dampaknya, pertimbangkan median |
| Provinsi dengan IPM jauh di atas lainnya | **Pertahankan** — itulah kenyataan yang hendak digambarkan |

> Membuang pencilan agar *p-value* menjadi signifikan bukan pembersihan data. Itu **manipulasi hasil**, dan ia tetap manipulasi meskipun dilakukan tanpa niat buruk.

### 14.4.3 Nilai Hilang

| Pola | Ciri | Penanganan yang wajar |
|------|------|-----------------------|
| MCAR — hilang sepenuhnya acak | Tidak berkaitan dengan apa pun | Pengecualian baris aman |
| MAR — hilang secara acak bersyarat | Berkaitan dengan variabel lain yang teramati | Pengecualian berpasangan atau imputasi, disertai penjelasan |
| MNAR — hilang tidak acak | Berkaitan dengan nilai yang hilang itu sendiri | **Tidak dapat diperbaiki secara statistik** — wajib dibahas sebagai keterbatasan |

Contoh MNAR: responden berpenghasilan sangat tinggi cenderung tidak mengisi kolom penghasilan. Rata-rata penghasilan yang dihitung dari data tersisa akan **selalu** terlalu rendah, berapa pun canggihnya metode imputasi yang dipakai.

---

## 14.5 Tahap 4 dan 5 — Analisis

### 14.5.1 Deskriptif Selalu Mendahului Inferensi

Tidak ada uji hipotesis yang dijalankan sebelum data dilihat bentuknya. Urutannya tetap:

1. Ukuran pemusatan dan penyebaran per kelompok, disertai **n per kelompok**.
2. Visualisasi yang sesuai jenis data (histogram, box plot, scatter plot).
3. Baru kemudian pemilihan uji.

Kuartet Anscombe pada Bab 3 sudah menunjukkan alasannya: empat himpunan data dengan statistik ringkasan yang nyaris identik dapat memiliki bentuk yang sama sekali berbeda.

### 14.5.2 Pohon Keputusan Pemilihan Uji

```
Apa yang ditanyakan?
│
├── Membandingkan RATA-RATA
│   ├── 1 kelompok vs nilai acuan ─────────► Uji-t satu sampel
│   ├── 2 kelompok bebas ──────────────────► Uji-t dua sampel bebas
│   │                                          (cek kesamaan varians)
│   ├── 2 kelompok berpasangan ────────────► Uji-t berpasangan
│   └── 3 kelompok atau lebih ─────────────► ANOVA satu arah
│                                              (+ uji lanjut bila signifikan)
│
├── Membandingkan PROPORSI
│   ├── 1 proporsi vs acuan ───────────────► Uji-z satu proporsi
│   └── 2 proporsi ────────────────────────► Uji-z dua proporsi
│
├── Menguji HUBUNGAN
│   ├── Dua variabel kategorik ────────────► Chi-square kebebasan
│   ├── Dua variabel numerik (linear) ─────► Korelasi Pearson
│   ├── Dua variabel numerik (monoton) ────► Korelasi Spearman
│   └── Memprediksi y dari x ──────────────► Regresi linear sederhana
│
└── Menguji KESESUAIAN sebaran
    └── Satu variabel kategorik vs harapan ► Chi-square kesesuaian
```

### 14.5.3 Yang Wajib Dilaporkan pada Setiap Uji

| Unsur | Contoh |
|-------|--------|
| Uji yang dipakai dan alasannya | "ANOVA satu arah, karena membandingkan rata-rata lima kelompok bebas" |
| Pemeriksaan asumsi beserta buktinya | "Shapiro-Wilk p = 0,21 (normal); Levene p = 0,08 (varians homogen)" |
| Statistik uji dan derajat bebas | "F(4, 1820) = 12,43" |
| *p-value* | "p < 0,001" |
| **Ukuran efek** | "η² = 0,027 — efek kecil" |
| **Interval kepercayaan** | "Selisih rata-rata 3,2 µg/m³; IK 95% [1,4; 5,0]" |
| Kesimpulan dalam bahasa persoalan | "Terdapat perbedaan, tetapi besarnya kecil secara praktis" |

Dua baris bertanda tebal adalah yang paling sering hilang dari laporan mahasiswa — dan justru dua baris itulah yang membedakan laporan yang berguna dari laporan yang hanya melaporkan "signifikan".

---

## 14.6 Tahap 6 — Mengomunikasikan Batas

### 14.6.1 Tiga Kalimat yang Harus Ada

Setiap laporan analisis harus memuat tiga jenis kalimat:

1. **Apa yang ditemukan** — "Rata-rata PM2.5 berbeda antar stasiun (F(4, 1820) = 12,43; p < 0,001)."
2. **Seberapa besar** — "Namun η² = 0,027; hanya 2,7% keragaman yang dijelaskan oleh lokasi stasiun."
3. **Apa yang tidak dapat disimpulkan** — "Data ini tidak dapat menunjukkan *penyebab* perbedaan tersebut; kepadatan lalu lintas dan arah angin tidak terukur dalam data."

### 14.6.2 Kalimat yang Harus Dihindari

| Hindari | Ganti dengan |
|---------|--------------|
| "Terbukti bahwa..." | "Data ini konsisten dengan..." |
| "X menyebabkan Y" (data observasional) | "X berkaitan dengan Y" |
| "Tidak ada perbedaan" (p > α) | "Tidak ditemukan cukup bukti adanya perbedaan" |
| "Sangat signifikan" | "p = 0,003" — sebutkan angkanya |
| "Penelitian ini tidak memiliki keterbatasan" | Tidak ada gantinya. Kalimat ini selalu keliru. |

### 14.6.3 Mengapa Hasil Nihil Bernilai

Bias publikasi — kecenderungan hanya melaporkan hasil yang signifikan — adalah salah satu penyebab krisis reproduktibilitas di banyak bidang ilmu. Bila sepuluh tim menguji hipotesis yang sama dan hanya satu memperoleh p < 0,05 secara kebetulan, lalu hanya tim itu yang melaporkan hasilnya, maka literatur menjadi menyesatkan secara sistematis.

Melaporkan "tidak ditemukan perbedaan" dengan prosedur yang benar adalah **sumbangan ilmiah yang sah**. Dalam mata kuliah ini, ia bernilai sama tingginya dengan hasil signifikan.

---

## 14.7 AI Corner — Tingkat Mahir: Tanggung Jawab atas Keluaran AI

Bagian ini lebih panjang daripada AI Corner pada bab-bab sebelumnya, karena proyek akhir adalah tempat pertama mahasiswa memakai AI pada pekerjaan yang utuh dan dinilai.

### 14.7.1 Posisi Mata Kuliah Ini

Mata kuliah ini berstatus **tahap F (Foundation), mode K (Kontekstual)** pada AI Curriculum Infusion Matrix Kurikulum Informatika 2025 Revisi 2026. Artinya: AI **bukan materi yang diajarkan**, melainkan alat yang kehadirannya diakui dan diatur.

Pembagiannya tegas:

| Boleh dibantu AI | Tidak boleh dibantu AI |
|------------------|------------------------|
| Menulis kode `pandas`/`matplotlib` | **Memilih uji statistik** |
| Memperbaiki galat sintaks | **Memutuskan cara menangani nilai hilang** |
| Menjelaskan pesan kesalahan | **Menafsirkan *p-value* dan ukuran efek** |
| Menyunting tata bahasa laporan | **Menarik kesimpulan** |
| Menyarankan jenis grafik | **Memutuskan pencilan dibuang atau tidak** |
| Meringkas dokumentasi pustaka | **Menulis bagian keterbatasan** |

Pembatas di kolom kanan bukan kekhawatiran akan kecurangan. Alasannya teknis: **AI tidak mengetahui konteks data Anda**. Ia tidak tahu bagaimana data dikumpulkan, siapa yang tercakup dan siapa yang tidak, atau apa arti sebenarnya sebuah kolom pada instansi penerbitnya. Keputusan-keputusan di kolom kanan seluruhnya bergantung pada pengetahuan itu.

### 14.7.2 Empat Kekeliruan Khas AI pada Analisis Statistik

**(1) Memilih uji berdasarkan kata, bukan struktur data.**

Diminta "membandingkan dua kelompok", model bahasa hampir selalu menyarankan uji-t dua sampel bebas — termasuk ketika datanya berpasangan (pengukuran sebelum dan sesudah pada orang yang sama). Uji yang benar adalah uji-t berpasangan, dan perbedaannya besar: uji berpasangan jauh lebih berdaya karena menghilangkan keragaman antar individu.

**(2) Membalik arah penafsiran *p-value*.**

Keluaran seperti *"p = 0,03 berarti peluang 3% bahwa H₀ benar"* masih sering muncul. Ini keliru. *p-value* adalah peluang memperoleh data seekstrem ini **bila H₀ benar** — bukan peluang H₀ benar. Kekeliruan yang sama dibahas pada Bab 10; AI mengulanginya karena kekeliruan itu juga berlimpah pada teks yang menjadi bahan latihannya.

**(3) Melompat ke bahasa sebab-akibat.**

Diberi hasil korelasi, AI kerap menuliskan "peningkatan X mendorong Y" tanpa diminta. Data observasional tidak mendukung kalimat semacam itu. Ini dibahas tuntas pada Bab 13.

**(4) Membuat angka yang tidak ada.**

Bila diminta menafsirkan hasil tanpa diberi keluaran sebenarnya, model dapat menghasilkan nilai statistik yang tampak masuk akal tetapi sepenuhnya karangan. Setiap angka dalam laporan harus dapat ditelusuri ke sel notebook yang menghasilkannya.

### 14.7.3 Cara Memakai AI yang Menguatkan, Bukan Melemahkan

Perbedaannya terletak pada **urutan**:

| Melemahkan | Menguatkan |
|------------|------------|
| Bertanya kepada AI → menerima jawaban | Memutuskan sendiri → meminta AI menguji keputusan itu |
| "Uji apa yang harus saya pakai?" | "Saya memilih ANOVA satu arah karena lima kelompok bebas, data numerik, asumsi sudah saya periksa. Apa kelemahan pilihan ini?" |
| "Tafsirkan hasil ini" | "Tafsiran saya: [tulisan sendiri]. Adakah klaim yang melampaui data?" |
| "Buatkan bagian keterbatasan" | "Ini keterbatasan yang saya temukan. Jenis keterbatasan apa yang umumnya terlewat pada rancangan seperti ini?" |

Pola kolom kanan mempertahankan mahasiswa sebagai pengambil keputusan dan menempatkan AI sebagai pemeriksa. Pola kolom kiri memindahkan penalaran keluar dari kepala mahasiswa — dan penalaran itulah yang diuji pada UAS, tanpa bantuan apa pun.

### 14.7.4 Contoh Prompt yang Baik

```
Saya sedang menganalisis data IPM 38 provinsi Indonesia (BPS, 2025).

Pertanyaan: apakah rata-rata IPM berbeda antara wilayah barat dan
timur Indonesia?

Keputusan saya:
- Uji-t dua sampel bebas (dua kelompok, saling bebas, data rasio)
- Shapiro-Wilk: p = 0,31 dan p = 0,18 → asumsi kenormalan terpenuhi
- Levene: p = 0,02 → varians TIDAK homogen, maka saya memakai
  Welch's t-test

Tolong periksa: apakah ada kelemahan dalam alur penalaran ini?
Jangan berikan kesimpulan atas data saya — saya hanya ingin
pemeriksaan atas pilihan metodenya.
```

Prompt ini menunjukkan tiga hal sekaligus: keputusan sudah dibuat, dasarnya sudah ditulis, dan batas bantuan yang diminta sudah dinyatakan.

### 14.7.5 AI Usage Log

Setiap laporan wajib melampirkan catatan pemakaian AI. Formatnya:

| No | Bagian | Alat | Permintaan (ringkas) | Keluaran dipakai? | Verifikasi yang dilakukan |
|----|--------|------|----------------------|-------------------|---------------------------|
| 1 | Notebook §3 | Claude | Cara membuat box plot berkelompok dengan seaborn | Ya, dengan penyesuaian label | Dijalankan; grafik diperiksa terhadap data |
| 2 | Notebook §2 | ChatGPT | Arti pesan galat `SettingWithCopyWarning` | Ya, penjelasannya | Diperiksa ke dokumentasi pandas |
| 3 | Laporan §4 | Claude | Pemeriksaan atas tafsiran saya sendiri | Sebagian — satu klaim saya perbaiki | Dibandingkan dengan Bab 10 buku ini |
| 4 | Laporan §5 | — | Tidak memakai AI | — | Ditulis sendiri |

**Pernyataan penutup log** ditandatangani seluruh anggota:

> *Kami menyatakan bahwa seluruh keputusan metodologis — pemilihan uji, penanganan data, dan penafsiran hasil — dibuat oleh anggota kelompok. Bantuan AI terbatas pada hal-hal yang tercatat di atas, dan seluruh keluarannya telah kami verifikasi.*

Mencatat pemakaian AI **tidak mengurangi nilai**. Tidak mencatatnya, padahal memakainya, adalah pelanggaran integritas akademik. Inilah **amanah** dalam bentuknya yang paling sehari-hari: menyatakan apa adanya tentang bagaimana sebuah pekerjaan dikerjakan.

### 14.7.6 Pertanyaan yang Akan Diajukan

Pada sesi tanya jawab, akan ada satu pertanyaan tentang AI: *"Bagian mana yang dibantu AI? Jelaskan salah satu baris kodenya."*

Mahasiswa yang memakai AI sesuai pembagian §14.7.1 akan menjawabnya dengan mudah. Mahasiswa yang menyalin tanpa memahami akan tersendat pada baris pertama. Pertanyaan ini bukan jebakan — ia hanya memeriksa apa yang seharusnya sudah benar sejak awal.

---

## 14.8 Kesalahan yang Paling Sering Terjadi

| Kesalahan | Akibat | Pencegahan |
|-----------|--------|------------|
| Menjalankan uji sebelum melihat data | Uji salah, asumsi dilanggar | Deskriptif dan grafik selalu lebih dahulu |
| Mengganti uji setelah melihat *p-value* | *p-hacking* | Tetapkan uji di proposal |
| Menguji banyak hal lalu melaporkan yang signifikan | Galat Tipe I melonjak | Nyatakan seluruh uji yang dijalankan |
| Membuang pencilan tanpa alasan | Kesimpulan tidak sah | Catat alasan substantif |
| Melaporkan p tanpa ukuran efek | Pembaca tidak tahu besarnya | Selalu sertakan keduanya |
| Menyimpulkan sebab-akibat | Klaim melampaui rancangan | Periksa: adakah pengacakan? |
| Grafik tanpa label sumbu | Tidak terbaca | Daftar periksa sebelum mengumpulkan |
| Notebook tidak dapat dijalankan ulang | Hasil tidak dapat direproduksi | Jalankan ulang dari sel pertama sebelum mengumpulkan |
| Keterbatasan ditulis sebagai formalitas | Menunjukkan analisis tidak dipahami | Tulis lima butir §6.3 panduan proyek |

---

## 14.9 Daftar Periksa Akhir

Sebelum mengumpulkan, setiap butir berikut harus dapat dijawab "ya":

**Pertanyaan dan data**
- [ ] Pertanyaan penelitian tertulis dan dapat diuji
- [ ] Hipotesis ditulis sebelum analisis dijalankan
- [ ] Sumber data lengkap dengan tautan dan tanggal akses
- [ ] Definisi setiap variabel dipahami dan dicatat

**Pembersihan**
- [ ] Jumlah baris awal dan akhir dilaporkan
- [ ] Setiap pembuangan data disertai alasan substantif
- [ ] Pencilan diperiksa, dan keputusannya dijelaskan
- [ ] Penanganan nilai hilang dinyatakan beserta polanya

**Analisis**
- [ ] Deskriptif dan visualisasi mendahului inferensi
- [ ] Alasan pemilihan uji tertulis
- [ ] Seluruh asumsi diperiksa dan buktinya ditampilkan
- [ ] Ukuran efek dilaporkan
- [ ] Interval kepercayaan dilaporkan

**Komunikasi**
- [ ] Tidak ada klaim sebab-akibat dari data observasional
- [ ] Bagian keterbatasan membahas minimal empat butir
- [ ] Setiap grafik punya judul, label dengan satuan, dan n
- [ ] Setiap angka dalam laporan dapat ditelusuri ke notebook

**Integritas**
- [ ] AI Usage Log lengkap dan ditandatangani
- [ ] Notebook dapat dijalankan ulang tanpa galat
- [ ] Seluruh anggota memahami keseluruhan isi

---

## Latihan Soal

### Tingkat Dasar

1. Ubahlah tiga tema berikut menjadi pertanyaan penelitian yang dapat diuji, lengkap dengan variabel dan unit pembanding:
   (a) Kemacetan Jakarta.
   (b) Prestasi akademik mahasiswa.
   (c) Harga bahan pokok.

2. Untuk setiap situasi, sebutkan uji yang sesuai berdasarkan pohon keputusan §14.5.2:
   (a) Membandingkan rata-rata waktu tunggu di tiga puskesmas.
   (b) Menguji apakah proporsi mahasiswa yang lulus berbeda antara dua kelas.
   (c) Menguji hubungan antara jam belajar dan nilai ujian.
   (d) Menguji apakah pilihan jurusan berkaitan dengan asal daerah.

3. Sebuah kelompok melaporkan: *"Hasil uji signifikan (p < 0,05), sehingga terbukti bahwa metode A lebih baik."* Sebutkan tiga hal yang salah dari kalimat tersebut.

4. Dari daftar berikut, tandai mana yang boleh dan tidak boleh dibantu AI menurut §14.7.1:
   (a) Menulis kode untuk membaca berkas CSV.
   (b) Menentukan apakah memakai uji-t atau Mann-Whitney.
   (c) Memperbaiki tata bahasa paragraf pembahasan.
   (d) Menuliskan tafsiran atas nilai *p* yang diperoleh.

### Tingkat Menengah

5. Sebuah kelompok menemukan bahwa data mereka memiliki 18% nilai hilang pada kolom penghasilan, dan responden berpenghasilan tinggi diduga enggan mengisinya.
   (a) Pola nilai hilang apa ini?
   (b) Mengapa imputasi rata-rata akan memperburuk keadaan?
   (c) Apa yang wajib ditulis pada bagian keterbatasan?
   (d) Apakah analisis masih dapat dilanjutkan? Dengan syarat apa?

6. Sebuah kelompok menjalankan delapan uji-t antar pasangan kelompok, lalu melaporkan satu yang signifikan.
   (a) Berapa kira-kira peluang memperoleh setidaknya satu hasil signifikan secara kebetulan bila α = 0,05?
   (b) Apa nama praktik ini?
   (c) Uji apa yang seharusnya dipakai sejak awal?
   (d) Bila hasil tetap ingin dilaporkan, apa yang wajib disertakan?

7. Perhatikan catatan pembersihan berikut: *"Data dibersihkan dari pencilan sehingga distribusi menjadi normal dan uji-t dapat dipakai."*
   (a) Apa yang salah secara metodologis?
   (b) Apa yang berubah dari populasi yang diwakili?
   (c) Sebutkan dua alternatif yang sah.
   (d) Bagaimana seharusnya kalimat itu ditulis?

8. Sebuah kelompok memperoleh p = 0,41 dan menulis: *"Tidak ada perbedaan antara kedua kelompok."*
   (a) Mengapa kalimat itu keliru?
   (b) Tuliskan versi yang benar.
   (c) Informasi tambahan apa yang membuat hasil nihil ini lebih informatif?
   (d) Apakah nilai kelompok ini dirugikan oleh hasil nihil? Jelaskan berdasarkan rubrik.

9. Bacalah keluaran AI berikut: *"Korelasi r = 0,62 antara jam belajar dan IPK menunjukkan bahwa menambah jam belajar akan meningkatkan IPK sekitar 0,62 poin."*
   (a) Sebutkan dua kekeliruan dalam kalimat ini.
   (b) Kekeliruan tipe berapa dari §14.7.2?
   (c) Tuliskan versi yang benar.
   (d) Pemeriksaan apa yang seharusnya dilakukan mahasiswa sebelum memakai kalimat itu?

### Tingkat Mahir

10. Susunlah proposal lengkap untuk sebuah pertanyaan penelitian pilihan sendiri.
    (a) Rumuskan pertanyaan utama dan dua pertanyaan turunan.
    (b) Tentukan sumber data nyata; unduh dan laporkan dimensinya.
    (c) Tulis H₀ dan H₁ secara formal.
    (d) Tentukan uji beserta alasannya, dan sebutkan asumsi yang harus diperiksa.
    (e) Perkirakan tiga keterbatasan sebelum analisis dimulai.

11. Ambil sebuah laporan analisis data yang dipublikasikan (artikel media, laporan lembaga, atau *notebook* publik), lalu audit dengan §14.9.
    (a) Butir mana yang dipenuhi dan mana yang tidak?
    (b) Adakah klaim sebab-akibat yang tidak didukung rancangan?
    (c) Apakah ukuran efek dilaporkan?
    (d) Tuliskan tiga pertanyaan yang akan Anda ajukan kepada penulisnya.

12. Lakukan simulasi *p-hacking* dan tuliskan pelajarannya.
    (a) Bangkitkan dua kelompok dari **distribusi yang sama** (sehingga H₀ benar).
    (b) Jalankan uji-t. Catat *p-value*.
    (c) Ulangi 1.000 kali; hitung berapa persen menghasilkan p < 0,05.
    (d) Sekarang pada setiap ulangan, tambahkan data satu per satu dan berhenti begitu p < 0,05 (maksimal 100 tambahan). Hitung berapa persen "berhasil".
    (e) Bandingkan (c) dan (d), lalu jelaskan mengapa selisihnya sebesar itu.
    (f) Tuliskan satu paragraf tentang apa yang wajib dilakukan peneliti untuk mencegahnya.

13. Tulislah pernyataan pribadi (satu halaman) berjudul *"Batas Saya dalam Memakai AI untuk Analisis Data"*. Sertakan: apa yang akan dan tidak akan Anda serahkan kepada AI beserta alasannya, bagaimana Anda memverifikasi keluaran AI, dan bagaimana Anda akan menjelaskan kepada atasan bahwa sebuah kesimpulan adalah tanggung jawab Anda, bukan tanggung jawab alat.

---

## Rangkuman

1. Analisis statistik utuh terdiri atas enam tahap: **pertanyaan, data, pembersihan, deskriptif, inferensi, komunikasi** — dan alurnya tidak lurus.
2. **Pembersihan data memakan porsi waktu terbesar**, bukan perhitungan uji.
3. Tema bukan pertanyaan. Pertanyaan yang baik menyebutkan **variabel, unit pembanding, dan periode**.
4. **Hipotesis ditulis sebelum data dilihat**, untuk mencegah HARKing.
5. Setiap keputusan pembersihan dicatat dengan **apa, berapa banyak, dan mengapa**.
6. Pencilan hanya dibuang bila **terbukti keliru** — bukan agar hasil menjadi rapi.
7. **Deskriptif dan grafik selalu mendahului inferensi.**
8. Setiap uji dilaporkan lengkap dengan **asumsi, statistik uji, p, ukuran efek, dan interval kepercayaan**.
9. Laporan wajib menyatakan **apa yang tidak dapat disimpulkan**.
10. **Hasil nihil bernilai sama** dengan hasil signifikan bila prosedurnya benar.
11. AI boleh membantu **kode dan bahasa**; tidak boleh menggantikan **pemilihan uji, penanganan data, dan penafsiran** — karena AI tidak mengetahui konteks data Anda.
12. **AI Usage Log wajib.** Mencatat tidak mengurangi nilai; menyembunyikan adalah pelanggaran amanah.
13. Tanggung jawab atas setiap angka dan setiap kalimat dalam laporan tetap berada pada **analisnya**, bukan pada alatnya.

---

## Referensi

1. Wickham, H., & Grolemund, G. (2023). *R for Data Science* (2nd ed.), Bab "Workflow". O'Reilly. (Kerangka alur kerja; konsepnya berlaku lintas bahasa.)
2. Peng, R. D., & Matsui, E. (2018). *The Art of Data Science*. Leanpub.
3. Wasserstein, R. L., & Lazar, N. A. (2016). The ASA Statement on p-Values. *The American Statistician*, 70(2), 129–133.
4. Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-Positive Psychology. *Psychological Science*, 22(11), 1359–1366.
5. Kerr, N. L. (1998). HARKing: Hypothesizing After the Results are Known. *Personality and Social Psychology Review*, 2(3), 196–217.
6. Little, R. J. A., & Rubin, D. B. (2019). *Statistical Analysis with Missing Data* (3rd ed.). Wiley.
7. Badan Pusat Statistik. *Sistem Informasi Rujukan Statistik*. <https://sirusa.bps.go.id>
8. Tim Kurikulum Informatika UAI (2026). *AI Curriculum Infusion Matrix*, Kurikulum Informatika 2025 Revisi 2026.
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
