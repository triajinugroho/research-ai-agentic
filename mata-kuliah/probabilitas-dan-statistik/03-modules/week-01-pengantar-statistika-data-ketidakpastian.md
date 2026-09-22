# Minggu 1: Pengantar Statistika, Data, dan Ketidakpastian dalam Computing

## Informasi Modul

| Komponen | Detail |
|----------|--------|
| **Mata Kuliah** | Probabilitas dan Statistik (IF52510033) |
| **Minggu ke-** | 1 |
| **Topik** | Pengantar statistika, jenis dan skala data, populasi vs sampel, pengenalan Google Colab |
| **CPL / CPMK** | CPL10 / CPMK102 |
| **Sub-CPMK** | `PS-Sub-CPMK102-1` |
| **Indikator Mingguan** | Menjelaskan peran ketidakpastian dalam sistem komputasi, membedakan populasi–sampel, dan mengenali jenis/skala data |
| **Level Bloom** | C2 (Memahami) |
| **Durasi** | 150 menit tatap muka |
| **Metode** | Kuliah interaktif, diskusi kasus, demo Google Colab |

---

## Tujuan Pembelajaran

Setelah mengikuti perkuliahan minggu ini, mahasiswa mampu:

1. **Menjelaskan** (C2) mengapa seorang sarjana Informatika memerlukan statistika, dengan menyebutkan sekurang-kurangnya tiga persoalan computing yang hanya dapat dijawab secara statistik.
2. **Membedakan** (C2) populasi dan sampel, parameter dan statistik, serta menjelaskan konsekuensinya bagi penarikan kesimpulan.
3. **Mengklasifikasikan** (C2) data ke dalam jenis kualitatif/kuantitatif dan empat skala pengukuran.
4. **Membedakan** (C2) statistika deskriptif dan statistika inferensial beserta kapan masing-masing dipakai.
5. **Menjalankan** (C3) notebook Google Colab sederhana untuk memuat dan menampilkan ringkasan sebuah dataset.

---

## Materi Pembelajaran

### 1. Mengapa Informatika Membutuhkan Statistika

#### 1.1 Tiga Pertanyaan yang Tidak Bisa Dijawab Tanpa Statistika

Bayangkan Anda sudah menjadi *software engineer*. Tiga situasi berikut akan Anda temui, dan tak satu pun bisa diselesaikan dengan logika pemrograman biasa:

**Situasi 1 — Dua algoritma, mana yang lebih cepat?**

Anda menulis dua versi fungsi pengurutan. Versi A berjalan rata-rata 120 ms, versi B rata-rata 115 ms. Apakah versi B benar-benar lebih cepat, atau selisih 5 ms itu hanya kebetulan karena beban CPU saat pengukuran?

> Ini bukan pertanyaan pemrograman. Ini pertanyaan **uji hipotesis dua sampel** (Minggu 12).

**Situasi 2 — Model klasifikasi Anda akurat 94%. Apakah itu bagus?**

Anda membangun model pendeteksi transaksi penipuan dengan akurasi 94%. Terdengar hebat — sampai Anda sadar bahwa hanya 3% transaksi yang memang penipuan. Model yang selalu menjawab "bukan penipuan" akan mencapai akurasi 97%.

> Ini pertanyaan tentang **base rate dan probabilitas bersyarat** (Minggu 5).

**Situasi 3 — Berapa kapasitas server yang perlu disiapkan?**

Aplikasi Anda menerima rata-rata 40 permintaan per menit. Berapa kapasitas maksimum yang harus disiapkan agar 99% dari waktu sistem tidak kewalahan?

> Ini pertanyaan tentang **distribusi Poisson dan kuantil** (Minggu 6).

#### 1.2 Definisi Statistika

> **Statistika** adalah ilmu tentang pengumpulan, pengorganisasian, analisis, interpretasi, dan penyajian data — serta tentang **penarikan kesimpulan di bawah ketidakpastian**.

Bagian terakhir itulah yang paling penting bagi Informatika. Sebuah program komputer bersifat deterministik: masukan yang sama menghasilkan keluaran yang sama. Tetapi **data** yang masuk ke program itu tidak deterministik — ia datang dari dunia nyata yang penuh variasi.

```
                DUNIA DETERMINISTIK          DUNIA STATISTIK
                ────────────────────         ─────────────────
  Masukan  →    if x > 5: return "besar"  |  40 permintaan/menit rata-rata
  Keluaran →    selalu sama               |  bisa 28, bisa 55, bisa 41
  Alat     →    logika, algoritma         |  probabilitas, distribusi
  Jaminan  →    benar atau salah          |  "95% yakin nilainya antara ..."
```

#### 1.3 Peran dalam Kurikulum Informatika UAI

Mata kuliah ini adalah **fondasi (tahap F)** bagi jalur Kecerdasan Artifisial dan Sains Data. Perhatikan apa yang akan Anda temui kelak:

| Kelak Anda Belajar | Yang Sebenarnya Dipakai | Dipelajari di Minggu |
|--------------------|-------------------------|----------------------|
| *Train/test split* pada ML | Sampling acak | 9 |
| *Confidence* sebuah prediksi model | Probabilitas | 4–7 |
| Membandingkan dua model ML | Uji hipotesis | 11–12 |
| *Loss function* (MSE) | Varians | 2, 9 |
| Naive Bayes classifier | Teorema Bayes | 5 |
| Regularisasi dan *overfitting* | Distribusi sampling | 9 |
| *Fairness* pada model AI | Probabilitas bersyarat | 5 |

> **Catatan kurikulum.** Pada AI Curriculum Infusion Matrix, mata kuliah ini berstatus **mode Kontekstual (K)** — artinya AI hadir sebagai konteks, bukan sebagai alat yang Anda gunakan untuk mengerjakan tugas. Prinsipnya tegas: *mahasiswa tidak boleh menjadi sekadar pengguna model/API*.

---

### 2. Populasi dan Sampel

#### 2.1 Definisi

| Istilah | Definisi | Contoh |
|---------|----------|--------|
| **Populasi** | Seluruh anggota kelompok yang ingin dipelajari | Seluruh 1.847 mahasiswa aktif Prodi Informatika UAI |
| **Sampel** | Bagian dari populasi yang benar-benar diamati | 120 mahasiswa yang mengisi survei |
| **Parameter** | Nilai yang menggambarkan populasi | Rata-rata IPK seluruh mahasiswa (μ) |
| **Statistik** | Nilai yang dihitung dari sampel | Rata-rata IPK 120 responden (x̄) |

Notasi yang dipakai sepanjang mata kuliah ini:

| Besaran | Parameter (populasi) | Statistik (sampel) |
|---------|----------------------|--------------------|
| Rata-rata | μ (mu) | x̄ (x bar) |
| Simpangan baku | σ (sigma) | s |
| Varians | σ² | s² |
| Proporsi | p | p̂ (p hat) |
| Ukuran | N | n |

#### 2.2 Mengapa Tidak Mengambil Seluruh Populasi?

```
  Alasan          Contoh
  ──────────────  ─────────────────────────────────────────────
  Biaya           Sensus penduduk Indonesia: triliunan rupiah
  Waktu           Menguji 10 juta baris log satu per satu
  Merusak         Uji ketahanan perangkat sampai rusak
  Tidak mungkin   Populasi "seluruh pengguna aplikasi di masa depan"
```

Dalam Informatika, alasan terakhir paling sering muncul. Ketika Anda menguji waktu respons server dengan 1.000 permintaan, populasi sebenarnya adalah **seluruh permintaan yang mungkin terjadi** — sesuatu yang tak pernah bisa diamati seluruhnya.

#### 2.3 Sampel yang Baik dan yang Menyesatkan

Sebuah sampel berguna hanya bila **representatif** terhadap populasi.

| Jenis Sampel | Cara | Keterwakilan |
|--------------|------|--------------|
| Acak sederhana | Setiap anggota punya peluang sama terpilih | Baik |
| Acak berlapis (*stratified*) | Populasi dibagi kelompok, tiap kelompok diambil acak | Sangat baik |
| Sistematis | Ambil setiap ke-k | Baik bila tidak ada pola periodik |
| Kenyamanan (*convenience*) | Siapa saja yang mudah dijangkau | **Lemah** — sering bias |
| Sukarela | Siapa yang mau mengisi | **Lemah** — bias responden |

**Contoh bias yang klasik.** Anda ingin mengetahui rata-rata kecepatan internet mahasiswa UAI. Anda menyebar kuesioner daring. Siapa yang mengisi? Mahasiswa yang internetnya lancar. Mahasiswa dengan internet buruk justru tidak sempat mengisi.

> Hasil survei itu akan **melebih-lebihkan** kecepatan internet rata-rata. Ini disebut *self-selection bias*, dan tidak bisa diperbaiki dengan menambah jumlah responden.

---

### 3. Jenis dan Skala Data

#### 3.1 Kualitatif vs Kuantitatif

```
                        DATA
                          │
            ┌─────────────┴─────────────┐
            │                           │
      KUALITATIF                  KUANTITATIF
      (kategorikal)                 (numerik)
            │                           │
    ┌───────┴───────┐         ┌─────────┴─────────┐
    │               │         │                   │
 NOMINAL        ORDINAL    DISKRET            KONTINU
 (tanpa         (berurut)  (bisa dihitung)   (bisa diukur)
  urutan)
    │               │         │                   │
 jenis OS       tingkat    jumlah bug         waktu respons
 bahasa prog.   kepuasan   jumlah klik        ukuran berkas
 status HTTP    rating     jumlah user        suhu CPU
```

#### 3.2 Empat Skala Pengukuran

| Skala | Ciri | Operasi yang Sah | Contoh Informatika |
|-------|------|------------------|--------------------|
| **Nominal** | Sekadar label, tanpa urutan | = , ≠ , modus, frekuensi | Bahasa pemrograman, status HTTP, jenis perangkat |
| **Ordinal** | Punya urutan, jarak tidak bermakna | + di atas nominal: median, kuartil | Prioritas bug (rendah/sedang/tinggi), rating aplikasi 1–5 |
| **Interval** | Jarak bermakna, **nol bukan berarti tidak ada** | + di atas ordinal: mean, simpangan baku | Suhu Celsius, tahun kalender |
| **Rasio** | Jarak bermakna, **nol berarti benar-benar tidak ada** | Semua operasi, termasuk rasio | Waktu respons, ukuran berkas, jumlah pengguna, IPK |

#### 3.3 Mengapa Skala Menentukan Analisis

Ini bukan sekadar klasifikasi akademis. **Skala menentukan operasi statistik apa yang boleh dilakukan.**

**Contoh kesalahan yang sering terjadi:**

Prioritas bug dikodekan sebagai `1 = rendah`, `2 = sedang`, `3 = tinggi`. Seorang mahasiswa menghitung rata-ratanya dan mendapat 2,4.

> **Apa artinya prioritas 2,4?** Tidak ada artinya. Skala ordinal tidak menjamin jarak antara "rendah→sedang" sama dengan "sedang→tinggi". Yang sah adalah **median** ("prioritas tengah adalah sedang") atau **modus** ("prioritas paling sering adalah tinggi").

**Contoh kedua:**

Suhu CPU 40°C dan 80°C. Apakah yang kedua "dua kali lebih panas"?

> **Tidak.** Celsius adalah skala interval — titik nolnya sembarang (titik beku air), bukan ketiadaan panas. Dalam Kelvin (skala rasio), 313 K dan 353 K — jelas bukan dua kali lipat.

**Panduan cepat:**

```python
# Aturan praktis memilih operasi

def operasi_yang_sah(skala):
    """Mengembalikan daftar operasi statistik yang sah untuk suatu skala."""
    sah = {
        "nominal":  ["frekuensi", "modus", "proporsi"],
        "ordinal":  ["frekuensi", "modus", "median", "kuartil", "persentil"],
        "interval": ["frekuensi", "modus", "median", "mean", "simpangan baku"],
        "rasio":    ["frekuensi", "modus", "median", "mean", "simpangan baku",
                     "koefisien variasi", "rasio antar nilai"],
    }
    return sah[skala]

print(operasi_yang_sah("ordinal"))
# ['frekuensi', 'modus', 'median', 'kuartil', 'persentil']
```

---

### 4. Statistika Deskriptif vs Inferensial

| Aspek | Deskriptif | Inferensial |
|-------|------------|-------------|
| **Tujuan** | Merangkum data yang ada | Menyimpulkan tentang populasi dari sampel |
| **Cakupan kesimpulan** | Hanya data yang diamati | Melampaui data yang diamati |
| **Ketidakpastian** | Tidak ada | Selalu ada, dan harus dinyatakan |
| **Alat** | Mean, median, grafik | Interval kepercayaan, uji hipotesis |
| **Di MK ini** | Minggu 2–3 | Minggu 9–14 |

**Contoh perbedaannya:**

> *Deskriptif:* "Dari 120 mahasiswa yang disurvei, rata-rata waktu belajar adalah 14,2 jam per minggu."
> — Pernyataan ini **pasti benar** untuk 120 orang itu.

> *Inferensial:* "Rata-rata waktu belajar seluruh mahasiswa Informatika UAI diperkirakan antara 13,1 dan 15,3 jam per minggu, dengan tingkat kepercayaan 95%."
> — Pernyataan ini **mungkin salah**, dan kita menyatakan seberapa besar kemungkinannya.

> **Prinsip yang akan berulang sepanjang mata kuliah ini:** statistika inferensial tidak pernah memberi kepastian. Ia memberi **kesimpulan beserta ukuran ketidakpastiannya**. Analis yang menyembunyikan ketidakpastian itu tidak sedang membuat kesimpulan yang lebih kuat — ia sedang berbohong.

---

### 5. Pengenalan Lingkungan Kerja: Google Colab

#### 5.1 Mengapa Colab

- Berjalan di peramban — tidak perlu instalasi.
- Pustaka statistik (NumPy, pandas, matplotlib, seaborn, SciPy) sudah terpasang.
- Notebook dapat dibagikan dan dijalankan ulang oleh dosen — penting untuk reproduksibilitas.
- Gratis dan dapat diakses dari ponsel maupun komputer kampus.

#### 5.2 Sel Pertama: Memeriksa Lingkungan

```python
# Memeriksa versi pustaka yang tersedia di Colab
import sys
import numpy as np
import pandas as pd
import matplotlib
import scipy

print(f"Python      : {sys.version.split()[0]}")
print(f"NumPy       : {np.__version__}")
print(f"pandas      : {pd.__version__}")
print(f"matplotlib  : {matplotlib.__version__}")
print(f"SciPy       : {scipy.__version__}")
```

#### 5.3 Memuat dan Melihat Data

```python
import pandas as pd

# Memuat dataset nilai mahasiswa (disediakan di LMS)
df = pd.read_csv("nilai_mahasiswa_if.csv")

# Tiga hal pertama yang SELALU dilakukan pada dataset baru
print("Ukuran data (baris, kolom):", df.shape)
print("\nLima baris pertama:")
print(df.head())
print("\nTipe data tiap kolom:")
print(df.dtypes)
```

Keluaran yang diharapkan:

```
Ukuran data (baris, kolom): (240, 6)

Lima baris pertama:
          nim  kelas  nilai_uts  nilai_uas  jam_belajar asal_sekolah
0  2026010001  IF26A         78         82         12.5      SMA IPA
1  2026010002  IF26A         65         71          8.0      SMK TKJ
2  2026010003  IF26H         88         91         18.0      SMA IPA
3  2026010004  IF26H         54         60          5.5      SMA IPS
4  2026010005  IF26A         72         69         11.0      SMK RPL

Tipe data tiap kolom:
nim               int64
kelas            object
nilai_uts         int64
nilai_uas         int64
jam_belajar     float64
asal_sekolah     object
dtype: object
```

#### 5.4 Mengenali Skala Setiap Kolom

Sebelum menganalisis apa pun, tentukan skala tiap kolom.

```python
# Memetakan skala pengukuran untuk setiap kolom dataset
skala_kolom = {
    "nim":          "nominal",   # identitas, bukan angka untuk dihitung
    "kelas":        "nominal",   # IF26A dan IF26H tidak punya urutan
    "nilai_uts":    "interval",  # skor ujian, nol tidak berarti "tanpa pengetahuan"
    "nilai_uas":    "interval",
    "jam_belajar":  "rasio",     # nol jam benar-benar berarti tidak belajar
    "asal_sekolah": "nominal",
}

for kolom, skala in skala_kolom.items():
    print(f"{kolom:14s} → {skala}")
```

> **Perhatikan `nim`.** Kolomnya bertipe `int64`, tetapi menghitung rata-rata NIM adalah tindakan yang tidak bermakna. **Tipe data Python tidak sama dengan skala pengukuran statistik.** Inilah kesalahan yang paling sering dilakukan pemula.

#### 5.5 Ringkasan Awal

```python
# Ringkasan statistik untuk kolom numerik
print(df.describe())

# Ringkasan untuk kolom kategorikal
print("\nDistribusi kelas:")
print(df["kelas"].value_counts())

print("\nDistribusi asal sekolah:")
print(df["asal_sekolah"].value_counts())
```

> Perhatikan bahwa `df.describe()` juga menghitung statistik untuk kolom `nim`. Ini contoh nyata bahwa **komputer tidak tahu skala data** — kitalah yang harus tahu.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (Mandiri — 60 menit)

1. Membaca [Bab 1 buku ajar](../06-buku-ajar/bab-01-pengantar-statistika-ketidakpastian.md).
2. Membuat akun Google dan membuka <https://colab.research.google.com> — pastikan dapat membuat notebook baru.
3. Menuliskan satu contoh persoalan dari pengalaman sendiri (aplikasi, game, media sosial) yang menurut Anda melibatkan ketidakpastian.

### Di Kelas (150 menit)

| Waktu | Kegiatan |
|-------|----------|
| 0–15' | Pembukaan, kontrak perkuliahan, penjelasan kebijakan AI |
| 15–45' | Kuliah: mengapa Informatika butuh statistika + tiga situasi pembuka |
| 45–60' | **Diskusi kelompok:** "Kapan rata-rata menipu?" — setiap kelompok mencari satu contoh |
| 60–70' | Istirahat |
| 70–100' | Kuliah: populasi–sampel, jenis dan skala data |
| 100–120' | **Latihan kelas:** mengklasifikasikan 15 variabel ke dalam skala yang tepat |
| 120–145' | Demo Google Colab: memuat dataset, memeriksa ukuran dan tipe |
| 145–150' | Penutup, penjelasan Lab 01 |

#### Bahan Diskusi: "Kapan Rata-Rata Menipu?"

Setiap kelompok (3–4 orang) mencari satu kasus nyata dan menjelaskan mengapa rata-rata menyesatkan. Contoh pemicu:

- Rata-rata gaji lulusan sebuah jurusan adalah Rp 25 juta — padahal seorang lulusannya menjadi pengusaha dengan penghasilan Rp 2 miliar.
- Rata-rata waktu respons API adalah 200 ms — padahal 5% pengguna mengalami 8 detik.
- Rata-rata kedalaman sungai adalah 1,2 meter — apakah aman diseberangi?

#### Latihan Kelas: Menentukan Skala

Tentukan skala pengukuran untuk setiap variabel berikut:

| No | Variabel | Skala? |
|----|----------|--------|
| 1 | Nomor Induk Mahasiswa | |
| 2 | Waktu eksekusi program (milidetik) | |
| 3 | Tingkat kepuasan pengguna (sangat buruk → sangat baik) | |
| 4 | Jumlah *commit* per hari | |
| 5 | Sistem operasi yang digunakan | |
| 6 | Tahun rilis perangkat lunak | |
| 7 | Ukuran berkas (MB) | |
| 8 | Peringkat aplikasi di Play Store (1–5 bintang) | |
| 9 | Suhu prosesor (°C) | |
| 10 | Status kode HTTP (200, 404, 500) | |
| 11 | Persentase penggunaan CPU | |
| 12 | Jenis kelamin responden | |
| 13 | Jumlah pengikut akun media sosial | |
| 14 | Tingkat pendidikan (SMA, S1, S2, S3) | |
| 15 | Alamat IP | |

*Kunci dibahas di kelas. Perhatikan nomor 4, 6, 8, 10, dan 15 — semuanya berupa angka, tetapi tidak semuanya boleh dirata-rata.*

### Setelah Kelas (Mandiri — 180 menit)

1. Mengerjakan [Lab 01](../04-labs/lab-01-setup-colab-eksplorasi-data.md).
2. Mengerjakan Latihan Soal Bab 1 tingkat Dasar dan Menengah.
3. Mulai memikirkan tema proyek akhir (proposal dikumpulkan Minggu 6).

---

## Penugasan

| Kode | Tugas | Bobot | Batas Waktu |
|------|-------|-------|-------------|
| T-01 | Laporan Lab 01 — Setup Colab dan eksplorasi data pertama | 1,92% (bagian dari Observasi 25%) | Sebelum kelas Minggu 2 |

**Ketentuan:**
- Notebook `.ipynb` dengan nama `Lab01_NIM_NamaLengkap.ipynb`.
- Seluruh sel harus dapat dijalankan ulang dari atas ke bawah tanpa galat.
- Setiap keluaran statistik disertai kalimat interpretasi.
- AI Usage Log wajib diisi pada sel terakhir.

---

## Rangkuman

1. Statistika adalah ilmu **menarik kesimpulan di bawah ketidakpastian** — kemampuan yang tidak dapat digantikan oleh logika pemrograman.
2. Tiga persoalan computing yang menuntut statistika: membandingkan kinerja, menilai kualitas model, dan merencanakan kapasitas.
3. **Populasi** adalah yang ingin diketahui; **sampel** adalah yang benar-benar diamati. Parameter (μ, σ, p) menggambarkan populasi; statistik (x̄, s, p̂) dihitung dari sampel.
4. Sampel hanya berguna bila **representatif**. Sampel sukarela dan sampel kenyamanan rawan bias yang **tidak dapat diperbaiki dengan memperbesar sampel**.
5. Empat skala pengukuran — nominal, ordinal, interval, rasio — menentukan operasi statistik apa yang sah. **Tipe data Python bukan skala pengukuran.**
6. Statistika **deskriptif** merangkum data yang ada; statistika **inferensial** menyimpulkan tentang populasi dan selalu menyertakan ketidakpastian.
7. Mata kuliah ini adalah **fondasi** jalur AI dan Sains Data. Yang dibangun di sini adalah kemampuan menilai apakah keluaran sebuah model masuk akal.

---

## Referensi

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 1. Pearson.
2. Downey, A. B. (2014). *Think Stats* (2nd ed.), Bab 1. O'Reilly Media.
3. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.), Bab 1. Wiley.
4. Badan Pusat Statistik. *Statistik Indonesia 2025*. <https://www.bps.go.id>
5. Dokumentasi pandas — *Getting Started*. <https://pandas.pydata.org/docs/getting_started/>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
