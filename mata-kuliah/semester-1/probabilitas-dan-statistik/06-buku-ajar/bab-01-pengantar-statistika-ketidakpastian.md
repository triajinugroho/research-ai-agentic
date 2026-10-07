# BAB 1: PENGANTAR STATISTIKA DAN KETIDAKPASTIAN DALAM COMPUTING

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `PS-Sub-CPMK102-1` | Menjelaskan peran ketidakpastian dalam sistem komputasi dan membedakan statistika deskriptif dari inferensial | C2 |
| `PS-Sub-CPMK102-1` | Membedakan populasi dan sampel, parameter dan statistik | C2 |
| `PS-Sub-CPMK102-1` | Mengklasifikasikan data ke dalam empat skala pengukuran dan menentukan operasi yang sah | C2–C3 |

---

## 1.1 Tiga Pertanyaan yang Tidak Bisa Dijawab dengan Kode

Anda sedang belajar memprogram. Anda tahu bahwa program bersifat deterministik: masukan yang sama menghasilkan keluaran yang sama. Itu sifat yang membuat komputer dapat dipercaya.

Tetapi begitu program Anda berhadapan dengan **dunia nyata**, determinisme itu berhenti di perbatasan. Data yang masuk tidak deterministik. Dan tiga pertanyaan berikut — yang pasti Anda temui dalam karier — tidak dapat dijawab dengan `if`, `for`, atau `while`.

### 1.1.1 Apakah Selisih Ini Nyata?

Anda menulis dua versi fungsi pengurutan. Anda mengukur waktu eksekusinya masing-masing 30 kali:

| Versi | Rata-rata | Simpangan baku |
|-------|-----------|----------------|
| A | 120 ms | 14 ms |
| B | 115 ms | 16 ms |

Versi B lebih cepat 5 ms. Apakah itu berarti B **benar-benar** lebih cepat, atau selisih itu muncul karena kebetulan — beban CPU yang berbeda, *cache* yang kebetulan lebih hangat, proses latar yang tidak Anda kendalikan?

Kalau Anda menjalankan pengukuran sekali lagi besok, apakah B tetap menang?

> Ini bukan pertanyaan pemrograman. Ini pertanyaan **uji hipotesis dua sampel** — Bab 11.

### 1.1.2 Apakah Angka Ini Sebaik Kelihatannya?

Anda membangun model pendeteksi transaksi penipuan. Akurasinya **94%**. Anda melaporkannya ke tim.

Seorang rekan bertanya: berapa persen transaksi yang sebenarnya penipuan? Jawabannya: 3%.

Artinya sebuah model yang **selalu menjawab "bukan penipuan"** — model yang tidak mempelajari apa pun — akan mencapai akurasi 97%. Lebih tinggi dari model Anda.

> Ini pertanyaan tentang **base rate dan probabilitas bersyarat** — Bab 5.

### 1.1.3 Berapa Banyak yang Harus Disiapkan?

Aplikasi Anda menerima rata-rata 40 permintaan per menit. Anda menyiapkan server berkapasitas 40 permintaan per menit.

Hasilnya: sistem kewalahan hampir separuh waktu.

Mengapa? Karena "rata-rata 40" berarti kadang 28, kadang 55. Menyiapkan kapasitas persis sebesar rata-rata berarti gagal setiap kali beban di atas rata-rata.

> Ini pertanyaan tentang **distribusi Poisson dan kuantil** — Bab 6.

---

## 1.2 Apa Itu Statistika

> **Statistika** adalah ilmu tentang pengumpulan, pengorganisasian, analisis, interpretasi, dan penyajian data — serta tentang **penarikan kesimpulan di bawah ketidakpastian**.

Bagian terakhir itulah yang paling penting bagi Informatika.

### 1.2.1 Dua Dunia

```
        DUNIA DETERMINISTIK              DUNIA STATISTIK
        ────────────────────             ───────────────

  Masukan  │  x = 7                      │  40 permintaan/menit rata-rata
  Proses   │  if x > 5: return "besar"   │  variasi alami tak terhindarkan
  Keluaran │  SELALU "besar"             │  bisa 28, 55, atau 41
  Alat     │  logika, algoritma          │  probabilitas, distribusi
  Jaminan  │  benar atau salah           │  "95% yakin nilainya antara ..."
  Kesalahan│  bug — bisa diperbaiki      │  galat — bisa diukur, tak bisa dihapus
```

Perhatikan baris terakhir. Dalam pemrograman, kesalahan adalah *bug* yang pada prinsipnya dapat dihilangkan. Dalam statistika, **galat tidak bisa dihilangkan** — ia hanya bisa **diukur dan dinyatakan**.

Seorang analis yang menyembunyikan galat tidak sedang membuat kesimpulan yang lebih kuat. Ia sedang berbohong.

### 1.2.2 Dua Cabang Statistika

| Aspek | **Deskriptif** | **Inferensial** |
|-------|----------------|-----------------|
| Tujuan | Merangkum data yang ada | Menyimpulkan tentang populasi dari sampel |
| Cakupan kesimpulan | Hanya data yang diamati | Melampaui data yang diamati |
| Ketidakpastian | Tidak ada | **Selalu ada, dan harus dinyatakan** |
| Alat utama | Mean, median, grafik | Interval kepercayaan, uji hipotesis |
| Bab dalam buku ini | 2–3 | 8–12 |

**Contoh perbedaannya:**

> *Deskriptif:* "Dari 120 mahasiswa yang disurvei, rata-rata waktu belajar adalah 14,2 jam per minggu."
>
> Pernyataan ini **pasti benar** untuk 120 orang itu. Tidak ada yang bisa dibantah.

> *Inferensial:* "Rata-rata waktu belajar seluruh mahasiswa Informatika UAI diperkirakan antara 13,1 dan 15,3 jam per minggu, dengan tingkat kepercayaan 95%."
>
> Pernyataan ini **mungkin salah**. Dan kita menyatakan seberapa besar kemungkinannya salah.

---

## 1.3 Populasi dan Sampel

### 1.3.1 Definisi dan Notasi

| Istilah | Definisi | Contoh |
|---------|----------|--------|
| **Populasi** | Seluruh anggota kelompok yang ingin dipelajari | Seluruh 1.847 mahasiswa aktif Prodi Informatika UAI |
| **Sampel** | Bagian populasi yang benar-benar diamati | 120 mahasiswa yang mengisi survei |
| **Parameter** | Nilai yang menggambarkan populasi | Rata-rata IPK seluruh mahasiswa |
| **Statistik** | Nilai yang dihitung dari sampel | Rata-rata IPK 120 responden |

**Notasi yang akan dipakai sepanjang buku ini:**

| Besaran | Parameter (populasi) | Statistik (sampel) |
|---------|----------------------|--------------------|
| Rata-rata | μ (mu) | x̄ (x bar) |
| Simpangan baku | σ (sigma) | s |
| Varians | σ² | s² |
| Proporsi | p | p̂ (p hat) |
| Ukuran | N | n |

> **Kebiasaan yang menolong:** huruf Yunani untuk populasi, huruf Latin untuk sampel. Bila Anda melihat μ dalam sebuah rumus, Anda sedang berbicara tentang sesuatu yang biasanya **tidak diketahui**.

### 1.3.2 Mengapa Tidak Mengambil Seluruh Populasi?

| Alasan | Contoh |
|--------|--------|
| **Biaya** | Sensus penduduk Indonesia menelan triliunan rupiah |
| **Waktu** | Memeriksa 10 juta baris log satu per satu |
| **Merusak** | Menguji ketahanan perangkat sampai rusak |
| **Tidak mungkin** | Populasi "seluruh pengguna aplikasi di masa depan" |

Dalam Informatika, alasan terakhir paling sering muncul — dan paling sering tidak disadari.

Ketika Anda mengukur waktu respons server dengan 1.000 permintaan, populasi yang sebenarnya Anda pelajari bukan 1.000 permintaan itu. Populasinya adalah **seluruh permintaan yang mungkin terjadi** pada sistem itu — sesuatu yang tak pernah bisa diamati seluruhnya, karena sebagiannya belum terjadi.

### 1.3.3 Sampel yang Baik dan yang Menyesatkan

| Jenis Sampel | Cara Pengambilan | Keterwakilan |
|--------------|------------------|--------------|
| **Acak sederhana** | Setiap anggota punya peluang sama terpilih | Baik |
| **Acak berlapis** (*stratified*) | Populasi dibagi kelompok, tiap kelompok diambil acak | Sangat baik |
| **Sistematis** | Ambil setiap anggota ke-k | Baik bila tidak ada pola periodik |
| **Kenyamanan** (*convenience*) | Siapa saja yang mudah dijangkau | **Lemah** |
| **Sukarela** (*voluntary*) | Siapa yang bersedia mengisi | **Lemah** |

### 1.3.4 Kasus Bias yang Klasik

> Anda ingin mengetahui rata-rata kecepatan internet mahasiswa UAI. Anda menyebar kuesioner daring.

Siapa yang mengisi? Mahasiswa yang internetnya lancar. Mahasiswa dengan koneksi buruk justru kesulitan membuka formulirnya — sebagian bahkan tidak pernah melihat undangannya.

Hasil survei akan **melebih-lebihkan** kecepatan internet rata-rata.

> **Yang paling penting dipahami:** bias ini **tidak dapat diperbaiki dengan menambah responden**. Menaikkan jumlah responden dari 100 menjadi 10.000 hanya membuat Anda lebih yakin pada angka yang salah.
>
> Bias sampel diperbaiki dengan memperbaiki **cara pengambilan sampel**, bukan dengan memperbesar ukurannya. Ini prinsip yang akan berulang sepanjang buku ini.

**Kasus historis.** Pada pemilu presiden Amerika Serikat 1936, majalah *Literary Digest* melakukan survei dengan 2,4 juta responden — jumlah yang luar biasa besar. Mereka memprediksi Alf Landon menang telak. Hasilnya: Franklin Roosevelt menang telak.

Mengapa? Daftar responden diambil dari pemilik telepon dan pelanggan majalah — yang pada masa Depresi Besar adalah kelompok berpenghasilan tinggi, bukan cerminan pemilih Amerika. Sementara itu George Gallup memprediksi dengan tepat memakai hanya 50.000 responden yang dipilih secara representatif.

**Pelajarannya:** 50.000 sampel representatif mengalahkan 2,4 juta sampel bias.

---

## 1.4 Jenis dan Skala Data

### 1.4.1 Peta Jenis Data

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
 (tanpa         (berurut)  (terhitung)       (terukur)
  urutan)
    │               │         │                   │
 jenis OS       prioritas  jumlah bug         waktu respons
 bahasa prog.   bug        jumlah klik        ukuran berkas
 status HTTP    rating     jumlah pengguna    suhu prosesor
```

### 1.4.2 Empat Skala Pengukuran

| Skala | Ciri Khas | Operasi yang Sah | Contoh Informatika |
|-------|-----------|------------------|--------------------|
| **Nominal** | Sekadar label, tanpa urutan | =, ≠, modus, frekuensi, proporsi | Bahasa pemrograman, status HTTP, jenis perangkat, alamat IP |
| **Ordinal** | Punya urutan, jarak tidak bermakna | + di atas nominal: median, kuartil, persentil | Prioritas bug, rating aplikasi 1–5, tingkat pendidikan |
| **Interval** | Jarak bermakna, **nol bukan berarti tidak ada** | + di atas ordinal: mean, simpangan baku | Suhu Celsius, tahun kalender, skor ujian |
| **Rasio** | Jarak bermakna, **nol berarti benar-benar tidak ada** | Semua operasi, termasuk rasio antar nilai | Waktu respons, ukuran berkas, jumlah pengguna, IPK |

### 1.4.3 Mengapa Skala Menentukan Analisis

Ini bukan klasifikasi akademis yang boleh dilewati. **Skala menentukan operasi statistik apa yang boleh dilakukan** — dan komputer tidak akan mencegah Anda melakukan yang terlarang.

#### Kesalahan 1: Merata-rata Data Ordinal

Prioritas bug dikodekan sebagai `1 = rendah`, `2 = sedang`, `3 = tinggi`. Seorang mahasiswa menghitung rata-ratanya: **2,4**.

> **Apa artinya prioritas 2,4?**
>
> Tidak ada. Skala ordinal tidak menjamin jarak "rendah→sedang" sama dengan "sedang→tinggi". Mungkin selisih antara sedang dan tinggi jauh lebih besar daripada antara rendah dan sedang — tetapi pengkodean 1-2-3 menyembunyikannya.
>
> Yang sah adalah **median** ("prioritas tengah adalah sedang") atau **modus** ("prioritas paling sering adalah tinggi").

#### Kesalahan 2: Membuat Rasio dari Data Interval

Suhu CPU dua mesin: 40°C dan 80°C. Apakah mesin kedua "dua kali lebih panas"?

> **Tidak.** Celsius adalah skala **interval** — titik nolnya sembarang (titik beku air), bukan ketiadaan panas.
>
> Dalam Kelvin (skala rasio): 313 K dan 353 K. Jelas bukan dua kali lipat.

#### Kesalahan 3: Menganggap Tipe Data Python = Skala Pengukuran

```python
import pandas as pd

df = pd.read_csv("nilai_mahasiswa_if.csv")
print(df.dtypes)
# nim               int64   ← angka, tetapi SKALANYA NOMINAL
# kelas            object
# nilai_uts         int64   ← interval
# jam_belajar     float64   ← rasio
```

```python
# pandas akan dengan senang hati menghitung ini:
print(df["nim"].mean())
# 2026010120.5

# Angka ini tidak bermakna sama sekali.
# Komputer tidak tahu bahwa NIM adalah identitas, bukan besaran.
```

> **Prinsip yang harus Anda bawa:** tipe data adalah cara komputer **menyimpan** nilai. Skala pengukuran adalah cara manusia **memaknai** nilai. Keduanya berbeda, dan hanya Anda yang tahu yang kedua.

### 1.4.4 Panduan Praktis

```python
def operasi_yang_sah(skala):
    """Mengembalikan operasi statistik yang sah untuk suatu skala."""
    sah = {
        "nominal":  ["frekuensi", "modus", "proporsi"],
        "ordinal":  ["frekuensi", "modus", "median", "kuartil", "persentil"],
        "interval": ["frekuensi", "modus", "median", "mean", "simpangan baku"],
        "rasio":    ["frekuensi", "modus", "median", "mean", "simpangan baku",
                     "koefisien variasi", "rasio antar nilai"],
    }
    return sah[skala]

# Selalu petakan skala SEBELUM menganalisis
skala_kolom = {
    "nim":          "nominal",
    "kelas":        "nominal",
    "nilai_uts":    "interval",
    "nilai_uas":    "interval",
    "jam_belajar":  "rasio",
    "asal_sekolah": "nominal",
}

for kolom, skala in skala_kolom.items():
    print(f"{kolom:14s} ({skala:9s}) → {', '.join(operasi_yang_sah(skala)[:4])}")
```

---

## 1.5 Peran Mata Kuliah Ini dalam Kurikulum

Mata kuliah ini berada pada semester pertama bukan karena mudah, melainkan karena **sepuluh mata kuliah setelahnya bergantung padanya**.

| Kelak Anda Belajar | Yang Sebenarnya Dipakai | Bab |
|--------------------|-------------------------|-----|
| *Train/test split* pada ML | Sampling acak | 8 |
| *Confidence* sebuah prediksi model | Probabilitas | 4–7 |
| Membandingkan dua model ML | Uji hipotesis | 10–11 |
| *Loss function* (MSE) | Varians | 2, 8 |
| Naive Bayes classifier | Teorema Bayes | 5 |
| *Overfitting* dan regularisasi | Distribusi sampling | 8 |
| *Fairness* pada model AI | Probabilitas bersyarat | 5 |
| Evaluasi model (presisi, recall) | Probabilitas bersyarat | 5 |

Pada AI Curriculum Infusion Matrix Prodi Informatika UAI, mata kuliah ini berstatus **tahap F (Foundation)** dengan mode **K (Kontekstual)**, dan perannya dinyatakan sebagai:

> *Fondasi uncertainty, inference dan ML. Mahasiswa tidak boleh menjadi sekadar pengguna model/API.*

---

## AI Corner — Tingkat Dasar

### Mengapa AI Corner di Buku Ini Berbeda

Di sebagian besar mata kuliah, bagian AI Corner mengajarkan cara memakai AI untuk bekerja lebih efisien. **Di buku ini arahnya berbeda.**

Mata kuliah ini adalah **fondasi**. Yang sedang dibangun bukan kemampuan menghasilkan jawaban, melainkan kemampuan **menilai apakah sebuah jawaban masuk akal**. Kemampuan itu tidak bisa dipinjam dari mesin — ia hanya tumbuh dengan dilatih.

Karena itu AI Corner di buku ini membahas: **apa yang AI lakukan dengan baik, apa yang ia lakukan dengan buruk, dan mengapa Anda harus tetap bisa memeriksanya.**

### Yang Boleh dan Tidak Boleh

| Kegiatan | Status |
|----------|--------|
| Meminta AI menjelaskan konsep dengan cara lain | **Boleh** |
| Meminta AI memberi contoh tambahan | **Boleh** |
| Meminta AI memeriksa hitungan yang **sudah Anda kerjakan sendiri** | **Boleh** |
| Meminta AI membantu menulis kode visualisasi | **Boleh, wajib dicatat di AI Usage Log** |
| Meminta AI mengerjakan soal latihan Anda | **Tidak boleh** |
| Memakai AI saat kuis atau ujian | **Tidak boleh** |

### Latihan: Memeriksa AI

Cobalah bertanya kepada sebuah asisten AI:

> *"Apakah boleh menghitung rata-rata dari kolom NIM mahasiswa?"*

Perhatikan jawabannya. Model yang baik akan menjelaskan bahwa NIM adalah identitas, bukan besaran. Tetapi **sebagian model akan menjawab dengan kode Python yang menghitungnya** — karena secara teknis memang bisa.

Ini pelajaran pertama Anda tentang AI: **ia menjawab pertanyaan yang Anda ajukan, bukan pertanyaan yang seharusnya Anda ajukan.** Yang mengetahui pertanyaan mana yang seharusnya diajukan, hanya Anda.

### Prompt yang Baik untuk Belajar

| Kurang baik | Lebih baik |
|-------------|------------|
| "Kerjakan soal ini" | "Saya sudah mengerjakan soal ini dan mendapat 0,24. Bisakah kamu jelaskan apakah pendekatan saya masuk akal?" |
| "Apa itu skala ordinal" | "Berikan tiga contoh data ordinal dari dunia pengembangan perangkat lunak, dan jelaskan mengapa merata-ratakannya keliru" |
| "Buatkan kode" | "Saya ingin memeriksa skala tiap kolom. Ini kode saya — apa yang kurang?" |

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan perbedaan populasi dan sampel dengan satu contoh dari konteks Informatika.

2. Tentukan skala pengukuran untuk setiap variabel berikut:

   | No | Variabel | Skala? |
   |----|----------|--------|
   | a | Nomor Induk Mahasiswa | |
   | b | Waktu eksekusi program (ms) | |
   | c | Tingkat kepuasan pengguna (sangat buruk → sangat baik) | |
   | d | Jumlah *commit* per hari | |
   | e | Sistem operasi yang digunakan | |
   | f | Tahun rilis perangkat lunak | |
   | g | Ukuran berkas (MB) | |
   | h | Status kode HTTP (200, 404, 500) | |

3. Lengkapi tabel notasi berikut:

   | Besaran | Parameter | Statistik |
   |---------|-----------|-----------|
   | Rata-rata | | |
   | Simpangan baku | | |
   | Proporsi | | |
   | Ukuran | | |

4. Manakah pernyataan berikut yang bersifat deskriptif dan mana yang inferensial?
   (a) "Dari 200 permintaan yang dicatat, 12 mengalami galat."
   (b) "Tingkat galat sistem diperkirakan antara 4% dan 8%."
   (c) "Rata-rata waktu respons minggu ini adalah 214 ms."
   (d) "Optimasi baru kemungkinan besar menurunkan waktu respons."

5. Sebutkan tiga alasan mengapa kita mengambil sampel alih-alih seluruh populasi, masing-masing dengan satu contoh dari Informatika.

### Tingkat Menengah

6. Sebuah tim ingin mengetahui kepuasan pengguna aplikasi kampus. Mereka memasang formulir umpan balik di dalam aplikasi, dan siapa pun boleh mengisinya.
   (a) Jenis sampel apa ini?
   (b) Siapa yang kemungkinan besar mengisi, dan siapa yang tidak?
   (c) Ke arah mana hasilnya akan bias?
   (d) Apakah menambah jumlah responden dari 200 ke 5.000 memperbaiki masalahnya? Jelaskan.
   (e) Usulkan cara pengambilan sampel yang lebih baik.

7. Seorang mahasiswa menulis kode berikut:

   ```python
   df["prioritas_numerik"] = df["prioritas"].map(
       {"rendah": 1, "sedang": 2, "tinggi": 3}
   )
   print(f"Rata-rata prioritas: {df['prioritas_numerik'].mean():.2f}")
   ```

   (a) Skala apa data `prioritas`?
   (b) Mengapa perhitungan ini bermasalah?
   (c) Apa yang seharusnya dihitung, dan bagaimana kodenya?
   (d) Adakah kondisi di mana merata-ratakan data ordinal dapat dibenarkan? Jelaskan.

8. Jelaskan mengapa suhu 80°C **bukan** "dua kali lebih panas" dari 40°C, tetapi berkas 80 MB **memang** "dua kali lebih besar" dari berkas 40 MB. Kaitkan dengan skala pengukuran.

9. Sebuah laporan menyatakan: *"Survei kami terhadap 15.000 pengembang menunjukkan bahwa 78% memakai Visual Studio Code."* Survei disebar melalui kanal Twitter perusahaan pembuat sebuah *extension* VS Code.
   (a) Apa populasi yang ingin digambarkan?
   (b) Apa populasi yang sebenarnya tersampel?
   (c) Apa nama bias ini?
   (d) Bagaimana seharusnya klaim itu dituliskan agar jujur?

### Tingkat Mahir

10. Kasus *Literary Digest* 1936 menunjukkan 2,4 juta sampel bias kalah akurat dari 50.000 sampel representatif.
    (a) Jelaskan secara konseptual mengapa memperbesar sampel tidak mengurangi bias.
    (b) Rancang sebuah percobaan simulasi dengan Python untuk mendemonstrasikannya. Tuliskan langkah-langkahnya (kode boleh dalam bentuk kerangka).
    (c) Apakah ada situasi di dunia Informatika yang berisiko mengulangi kesalahan serupa? Beri satu contoh konkret.

11. Anda diminta merancang pengukuran kinerja sebuah API.
    (a) Tentukan populasi dan sampel secara eksplisit.
    (b) Variabel apa saja yang akan Anda ukur, dan apa skala masing-masing?
    (c) Bagaimana Anda mengambil sampel agar representatif? Pertimbangkan waktu, jenis endpoint, dan jenis pengguna.
    (d) Bias apa yang mungkin muncul dan bagaimana mencegahnya?
    (e) Ukuran ringkasan apa yang akan Anda laporkan, dan mengapa bukan rata-rata saja?

12. Tulislah esai singkat (300–400 kata) menjawab pertanyaan: *"Mengapa seorang sarjana Informatika yang mahir memanggil pustaka machine learning tetap memerlukan pemahaman statistika?"* Sertakan sekurang-kurangnya dua contoh konkret dari bab ini.

---

## Rangkuman

1. Statistika adalah ilmu **menarik kesimpulan di bawah ketidakpastian** — kemampuan yang tidak dapat digantikan oleh logika pemrograman.
2. Dalam pemrograman, kesalahan adalah *bug* yang dapat dihilangkan. Dalam statistika, **galat hanya dapat diukur dan dinyatakan**, tidak dihapus.
3. **Populasi** adalah yang ingin diketahui; **sampel** adalah yang diamati. Parameter (μ, σ, p) menggambarkan populasi; statistik (x̄, s, p̂) dihitung dari sampel.
4. Sampel berguna hanya bila **representatif**. Sampel sukarela dan kenyamanan rawan bias.
5. **Bias sampel tidak dapat diperbaiki dengan memperbesar sampel** — ia hanya membuat Anda lebih yakin pada angka yang salah.
6. Empat skala pengukuran — nominal, ordinal, interval, rasio — menentukan operasi statistik yang sah.
7. **Tipe data komputer bukan skala pengukuran.** `df["nim"].mean()` berjalan tanpa galat, tetapi hasilnya tidak bermakna.
8. **Statistika deskriptif** merangkum data yang ada; **statistika inferensial** menyimpulkan tentang populasi dan selalu menyertakan ketidakpastian.
9. Mata kuliah ini adalah **fondasi jalur AI dan Sains Data**; sepuluh mata kuliah berikutnya bergantung padanya.

---

## Referensi

1. Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2016). *Probability and Statistics for Engineers and Scientists* (9th ed.), Bab 1. Pearson.
2. Montgomery, D. C., & Runger, G. C. (2018). *Applied Statistics and Probability for Engineers* (7th ed.), Bab 1. Wiley.
3. Downey, A. B. (2014). *Think Stats: Exploratory Data Analysis in Python* (2nd ed.), Bab 1. O'Reilly Media.
4. Squire, P. (1988). Why the 1936 Literary Digest Poll Failed. *Public Opinion Quarterly*, 52(1), 125–133.
5. Stevens, S. S. (1946). On the Theory of Scales of Measurement. *Science*, 103(2684), 677–680.
6. Badan Pusat Statistik. *Statistik Indonesia 2025*. <https://www.bps.go.id>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
