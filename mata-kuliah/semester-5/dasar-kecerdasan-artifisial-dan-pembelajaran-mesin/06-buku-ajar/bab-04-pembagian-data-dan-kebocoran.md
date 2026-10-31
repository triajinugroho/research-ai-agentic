# BAB 4: PEMBAGIAN DATA DAN KEBOCORAN DATA

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK102-1` | Menjelaskan peran data latih, data validasi, dan data uji beserta alasan data uji hanya dipakai satu kali | C2 |
| `DAIML-Sub-CPMK102-1` | Menerapkan strategi pembagian data yang sesuai sifat datanya | C3 |
| `DAIML-Sub-CPMK102-1` | Menganalisis sebuah *pipeline* dan menemukan kebocoran di dalamnya | C4 |
| `DAIML-Sub-CPMK102-1` | Memperbaiki kebocoran dan melaporkan dampaknya terhadap skor | C5 |

---

## Cara Memakai Bab Ini

Bab ini disusun **satu konsep pada satu waktu**. Setiap konsep dibahas dengan urutan yang sama:

| Langkah | Isi | Tujuan |
|---------|-----|--------|
| **Situasi** | Masalah sehari-hari tanpa istilah teknis | Membentuk pemahaman awal |
| **Tebak Dahulu** | Pertanyaan yang dijawab sebelum membaca lanjutan | Mengaktifkan pengetahuan yang sudah dimiliki |
| **Contoh Kecil** | Data sangat sedikit yang dapat dihitung dengan tangan | Memahami mekanisme secara nyata |
| **Istilah dan Aturan** | Nama teknis dan kaidah | Menamai apa yang sudah dipahami |
| **Kode** | Kode yang mengulang contoh yang sama | Mencocokkan hasil hitungan tangan dengan hasil komputer |
| **Cek Pemahaman** | Satu soal singkat dengan jawaban | Memastikan konsep dikuasai sebelum lanjut |

**Saran belajar.** Jawablah *Tebak Dahulu* dan *Cek Pemahaman* secara tertulis sebelum membuka jawabannya. Menebak lalu keliru lebih bermanfaat daripada langsung membaca jawaban yang benar, karena kekeliruan itu memperlihatkan bagian yang perlu diperbaiki.

**Perkiraan waktu belajar mandiri:** 3 sampai 4 jam, tidak termasuk latihan soal.

**Seluruh angka dalam bab ini** (misalnya 0,644 atau 0,996) diperoleh dari kode yang dijalankan dengan `random_state` atau `seed` yang tertulis. Bila Anda menjalankan kode yang sama, angkanya akan sama.

---

## 4.1 Mengapa Satu Bab Penuh untuk Satu Jenis Kesalahan

### 4.1.1 Pemanasan: Ingat Kembali

Bab ini memakai konsep dari Bab 2, Bab 3, dan mata kuliah Probabilitas dan Statistik. Jawablah enam pertanyaan berikut **tanpa melihat catatan**. Hasilnya menunjukkan bagian mana yang perlu diulang.

1. Pada prapemrosesan (Bab 3), apa perbedaan antara `fit` dan `transform`?
2. Apa yang diukur oleh rerata dan oleh simpangan baku?
3. Apa fungsi `Pipeline` pada `scikit-learn`?
4. Apa perbedaan antara **fitur** dan **target**?
5. Bila sebuah kejadian memiliki peluang 1,2%, berapa kali kita perkirakan kejadian itu muncul dalam 200 pengamatan?
6. Mengapa `random_state` perlu ditetapkan?

<details>
<summary>Jawaban singkat</summary>

1. `fit` **mempelajari** nilai dari data (misalnya rerata dan simpangan baku). `transform` **memakai** nilai yang sudah dipelajari itu untuk mengubah data.
2. Rerata mengukur **pusat** data. Simpangan baku mengukur seberapa **tersebar** data di sekitar pusat itu.
3. `Pipeline` merangkai langkah prapemrosesan dan model menjadi satu rangkaian yang diperlakukan sebagai satu kesatuan.
4. Fitur adalah informasi yang **diberikan** kepada model. Target adalah hal yang **ingin diprediksi**.
5. 200 × 0,012 = **2,4** kali. Nilai ini disebut nilai harapan.
6. Agar proses yang mengandung keacakan menghasilkan hasil yang sama setiap kali dijalankan, sehingga eksperimen dapat diulang.

Bila dua atau lebih jawaban terasa asing, ulangi dahulu Bab 3 (nomor 1 dan 3) atau catatan Probabilitas dan Statistik (nomor 2 dan 5) sebelum melanjutkan.

</details>

### 4.1.2 Situasi: Soal Latihan yang Bocor

Bayangkan seorang dosen menyiapkan ujian akhir. Sebelum ujian, dosen itu membagikan **soal latihan**. Ternyata soal latihan tersebut sebagian besar **sama persis** dengan soal ujian.

Seorang mahasiswa menghafal soal latihan dan memperoleh nilai ujian 95. Apakah nilai 95 itu membuktikan bahwa mahasiswa tersebut **memahami materi**?

**Tebak dahulu.** Tuliskan jawaban Anda. Pertimbangkan: bila dosen mengganti seluruh soal dengan soal baru pada materi yang sama, apakah nilainya tetap 95?

Jawabannya: **tidak dapat dipastikan**. Nilai 95 hanya membuktikan bahwa mahasiswa itu menghafal soal yang sudah ia lihat. Nilai tersebut **tidak menggambarkan** kemampuannya menghadapi soal baru.

Pembelajaran mesin menghadapi persoalan yang sama. Model dilatih dari sebagian data, lalu **diuji** untuk mengetahui kemampuannya pada data yang belum pernah ia lihat. Apabila data uji sudah "bocor" ke dalam proses belajar, skor yang dihasilkan menyerupai nilai mahasiswa yang menghafal: **tinggi, tetapi menyesatkan**.

### 4.1.3 Mengapa Kesalahan Ini Berbahaya

Kapoor dan Narayanan (2023) mengidentifikasi **294 makalah ilmiah dari 17 bidang** yang memakai pembelajaran mesin dan terdampak kebocoran data. Akibatnya, sebagian hasil yang dilaporkan tidak dapat diulang, dan sebagian kesimpulan ilmiah yang telah dipublikasikan perlu dipertanyakan.

Kesalahan ini tidak hanya dilakukan pemula. Penyebabnya adalah satu sifat yang khas:

> **Kebocoran data adalah satu-satunya jenis kesalahan dalam pembelajaran mesin yang *memberi hadiah* ketika dilakukan.**

Kesalahan lain, misalnya salah penulisan kode, biasanya menghasilkan pesan galat atau skor yang buruk, sehingga segera disadari. Kebocoran justru menghasilkan **skor yang bagus**, dan skor yang bagus jarang dipertanyakan.

**Istilah.** *Kebocoran data* (*data leakage*) adalah keadaan ketika informasi dari data uji, atau informasi yang tidak tersedia saat prediksi sesungguhnya, ikut masuk ke dalam proses pembentukan model.

**Cek pemahaman 4.1.** Mengapa nilai 95 pada contoh di atas tidak membuktikan pemahaman, sedangkan nilai 95 pada ujian dengan soal yang benar-benar baru dapat membuktikannya?

<details>
<summary>Jawaban</summary>

Karena pada ujian dengan soal baru, mahasiswa tidak mungkin sekadar mengingat. Ia harus **menerapkan** pemahamannya pada hal yang belum pernah ia lihat. Itulah yang diukur oleh data uji yang bersih.

</details>

---

## 4.2 Tiga Peran Data

### 4.2.1 Situasi dan Analogi

Kembali ke contoh ujian. Seorang mahasiswa yang belajar dengan baik biasanya melalui tiga tahap:

| Tahap dalam belajar | Padanan dalam pembelajaran mesin | Fungsi |
|---------------------|-----------------------------------|--------|
| **Buku latihan** | **Data latih** | Tempat belajar. Boleh dibuka berkali-kali |
| **Tryout** | **Data validasi** | Mengukur kemajuan dan memilih cara belajar yang paling efektif |
| **Ujian akhir** | **Data uji** | Menilai kemampuan sesungguhnya. Hanya sekali |

Mahasiswa boleh mengerjakan tryout berulang kali, mengubah cara belajarnya, lalu mencoba lagi. Tetapi ujian akhir tidak boleh diulang. Bila ujian akhir diulang sambil terus memperbaiki cara belajar berdasarkan hasilnya, nilai ujian akhir tidak lagi mencerminkan kemampuan baru.

```
┌────────────────────────────────────────────────────────────┐
│                     SELURUH DATA                           │
├──────────────────────────┬──────────────┬──────────────────┤
│         LATIH            │   VALIDASI   │       UJI        │
│         (60%)            │    (20%)     │      (20%)       │
├──────────────────────────┼──────────────┼──────────────────┤
│ Model belajar dari sini  │ Memilih model│ Menaksir kinerja │
│                          │ & menyetel   │ pada data baru   │
├──────────────────────────┼──────────────┼──────────────────┤
│ Dipakai berkali-kali     │ Berkali-kali │ SEKALI, di akhir │
└──────────────────────────┴──────────────┴──────────────────┘
```

Persentase 60/20/20 hanyalah contoh. Proporsi dapat berbeda sesuai jumlah data.

### 4.2.2 Mengapa Data Uji Hanya Sekali: Percobaan Kecil

**Tebak dahulu.** Anda memiliki 30 model. **Semuanya hanya menebak secara acak** ("ya" atau "tidak" dengan peluang sama). Data uji berisi 50 baris. Anda memilih model dengan skor tertinggi pada data uji. Berapa kira-kira skor model terbaik itu? Bila model tersebut kemudian dipakai pada data yang benar-benar baru, berapa kira-kira skornya?

Jalankan percobaan berikut.

```python
import numpy as np

rng = np.random.default_rng(42)          # seed ditetapkan agar hasil sama
y_uji = rng.integers(0, 2, size=50)      # 50 label sebenarnya (0 atau 1)

skor = []
for model in range(30):
    tebakan = rng.integers(0, 2, size=50)    # model menebak acak
    skor.append((tebakan == y_uji).mean())   # proporsi tebakan yang benar

print("Rerata ke-30 model :", round(np.mean(skor), 3))
print("Skor model terbaik :", max(skor))
```

Hasil: rerata ke-30 model **0,496**, sedangkan skor model terbaik **0,64**.

Jalankan percobaan yang sama 1.000 kali dengan seed berbeda. Rerata skor model terbaik adalah **0,644**.

**Penjelasan.** Kemampuan sebenarnya setiap model adalah 0,5 (hanya menebak). Namun bila kita memilih yang terbaik dari 30 percobaan pada **data uji yang sama**, kita hampir pasti mendapat skor yang tampak lebih baik, **semata-mata karena kebetulan**. Pada data baru, model terpilih itu kembali ke sekitar 0,5.

Inilah alasan data uji hanya sekali. Setiap kali kita memakai skor data uji untuk memilih ("model A lebih baik, kita pakai A"), kita **memilih berdasarkan kebetulan** pada data tersebut. Setelah beberapa kali, skor uji tidak lagi menaksir kinerja pada data baru. Skor itu menjadi skor pada data yang **sudah ikut membentuk keputusan**.

**Istilah dan aturan.**

| Bagian | Peran | Aturan |
|--------|-------|--------|
| **Latih** | Model mempelajari pola | Boleh dipakai berulang |
| **Validasi** | Memilih model dan menyetel hiperparameter | Boleh dipakai berulang, tetapi setiap pemakaian sedikit mengurangi kejujurannya |
| **Uji** | Menaksir kinerja pada data yang belum pernah dilihat | **Dipakai satu kali, di paling akhir** |

Gejala ini disebut **kebocoran melalui pemilihan berulang** (§4.5.6).

**Cek pemahaman 4.2.** Seorang mahasiswa mencoba lima model, melihat skor uji masing-masing, memilih yang terbaik, lalu melaporkan skor itu sebagai "kinerja model". Apa kekeliruannya, dan apa perbaikannya?

<details>
<summary>Jawaban</summary>

Kekeliruannya: data uji dipakai untuk **memilih** model, sehingga skor yang dilaporkan cenderung lebih tinggi daripada kinerja sebenarnya. Perbaikan: pilih model memakai **data validasi**, lalu ukur model terpilih pada data uji **satu kali**.

</details>

---

## 4.3 Strategi Pembagian sesuai Sifat Data

Cara membagi data **tidak sama untuk semua data**. Kita membahas empat strategi, **satu per satu**, masing-masing disertai situasi yang membuatnya diperlukan.

| Sifat data | Strategi | Alat |
|------------|----------|------|
| Biasa, kelas seimbang | Acak | `train_test_split` |
| Kelas tak seimbang | **Stratifikasi** | `train_test_split(stratify=y)` |
| Ada urutan waktu | **Temporal** | `TimeSeriesSplit` |
| Ada entitas yang berulang | **Berkelompok** | `GroupKFold` |

Tabel ini adalah ringkasan. Bacalah bagian di bawahnya untuk memahami **alasan** tiap baris.

### 4.3.1 Pembagian Acak

**Situasi.** Anda memiliki data 1.000 siswa dengan jumlah lulus dan tidak lulus yang kurang lebih seimbang. Setiap siswa **tidak saling terkait** dan tidak ada urutan waktu yang bermakna.

Pada keadaan ini, pembagian acak sudah memadai: setiap baris memiliki peluang yang sama untuk masuk ke data latih atau data uji.

```python
from sklearn.model_selection import train_test_split

# test_size=0.2: 20% data menjadi data uji
# random_state=42: agar pembagian sama setiap dijalankan
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

Strategi acak adalah **titik awal**, bukan jawaban untuk semua keadaan. Tiga bagian berikut menunjukkan keadaan yang membuatnya tidak memadai.

### 4.3.2 Stratifikasi: Bila Kelas Sangat Tidak Seimbang

**Situasi.** Sebuah bank memiliki 1.000 transaksi, di antaranya **hanya 12 transaksi penipuan** (1,2%). Anda membagi secara acak: 800 latih, 200 uji.

**Tebak dahulu.** Berapa transaksi penipuan yang Anda harapkan berada di data uji? Mungkinkah data uji **tidak berisi satu pun** transaksi penipuan?

**Contoh kecil.** Nilai harapan: 200 × 0,012 = **2,4** transaksi penipuan di data uji. Peluang data uji tidak berisi satu pun adalah sekitar **6,8%**, dihitung dengan distribusi hipergeometrik. Simulasi 2.000 pembagian acak memberi hasil serupa, yaitu **7,1%**.

Artinya, dari setiap 100 kali membagi, sekitar 7 kali data uji tidak memuat kasus penipuan sama sekali. Skor pada data uji seperti itu **tidak bermakna**, karena model tidak pernah diuji pada hal yang justru ingin dideteksi.

**Aturan.** *Stratifikasi* menjaga proporsi kelas yang sama pada setiap bagian. Dengan stratifikasi, data uji pada contoh ini **selalu** berisi 2 transaksi penipuan.

```python
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42   # stratify=y menjaga proporsi kelas
)
print("Penipuan di data uji:", y_uji.sum())   # hasil: 2
```

**Cek pemahaman 4.3.2.** Data 5.000 pasien memiliki 2% penderita penyakit langka. Bila data uji 20%, berapa penderita yang diharapkan di data uji, dan mengapa stratifikasi dianjurkan?

<details>
<summary>Jawaban</summary>

Data uji berisi 1.000 pasien. Penderita yang diharapkan: 1.000 × 0,02 = **20 orang**. Stratifikasi dianjurkan agar jumlah ini terjaga dan tidak, secara kebetulan, jauh lebih sedikit sehingga skor menjadi tidak stabil.

</details>

### 4.3.3 Pembagian Temporal: Bila Data Berurutan Waktu

**Situasi.** Sebuah toko mencatat penjualan harian selama 120 hari. Penjualan cenderung **naik** dari waktu ke waktu. Anda ingin memprediksi penjualan **hari-hari mendatang**.

**Tebak dahulu.** Bila data dibagi acak, apakah kondisi ujian menyerupai kondisi pemakaian sesungguhnya? Dalam pemakaian sesungguhnya, apakah kita pernah mengetahui data masa depan?

**Contoh kecil.** Pada pembagian acak, sebagian hari uji berada **di antara** hari latih. Untuk memprediksi hari ke-60, model telah melihat hari ke-59 dan ke-61. Ini sama dengan **mengintip masa depan**. Pada pemakaian sesungguhnya, hal itu mustahil.

```
  SALAH (acak):
  ───────────────────────────────────────────────►  waktu
  [U][L][L][U][L][U][L][L][U][L]   ← uji tersebar di antara latih
     Model "melihat masa depan"

  BENAR (temporal):
  ───────────────────────────────────────────────►  waktu
  [L][L][L][L][L][L][L][V][V][U][U] ← uji selalu setelah latih
```

Percobaan dengan data tren buatan 120 hari memberi hasil berikut (galat mutlak rerata, makin kecil makin baik):

| Cara membagi | Galat |
|--------------|-------|
| Acak | **2,65** |
| Temporal (90 hari pertama dilatih, 30 hari terakhir diuji) | **18,82** |

Pembagian acak tampak **jauh lebih baik**, padahal itu hanya karena model boleh mengintip. Galat 18,82 adalah gambaran yang **jujur** tentang prediksi masa depan.

**Aturan.** Pada data berurutan waktu, data uji harus selalu **lebih baru** daripada data latih.

```python
from sklearn.model_selection import TimeSeriesSplit
import numpy as np

# Contoh dengan 12 data agar mudah dibaca
tscv = TimeSeriesSplit(n_splits=5)
for i, (idx_latih, idx_uji) in enumerate(tscv.split(np.arange(12)), start=1):
    print(f"Lipatan {i}: latih={list(idx_latih)}  uji={list(idx_uji)}")
```

Keluaran:

```
Lipatan 1: latih=[0, 1]  uji=[2, 3]
Lipatan 2: latih=[0, 1, 2, 3]  uji=[4, 5]
Lipatan 3: latih=[0, 1, 2, 3, 4, 5]  uji=[6, 7]
Lipatan 4: latih=[0, 1, 2, 3, 4, 5, 6, 7]  uji=[8, 9]
Lipatan 5: latih=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  uji=[10, 11]
```

Perhatikan: pada setiap lipatan, indeks uji **selalu lebih besar** daripada seluruh indeks latih.

**Cek pemahaman 4.3.3.** Seorang analis memprediksi curah hujan bulan depan dan membagi data hujan 10 tahun secara acak. Apa masalahnya?

<details>
<summary>Jawaban</summary>

Model akan dilatih dengan data dari bulan-bulan **setelah** bulan yang diuji, sehingga ia "mengetahui masa depan". Skor ujinya terlalu optimistis. Seharusnya memakai pembagian temporal.

</details>

### 4.3.4 Pembagian Berkelompok: Bila Satu Entitas Muncul Berulang

**Situasi.** Sebuah rumah sakit mencatat **8.000 kunjungan dari 900 pasien**. Seorang pasien dapat berkunjung beberapa kali. Setiap kunjungan adalah satu baris.

**Tebak dahulu.** Bila baris dibagi acak, apakah pasien yang sama dapat muncul di data latih **dan** data uji? Bila ya, apa akibatnya terhadap skor?

**Contoh kecil.** Ya, pasien yang sama hampir pasti berada di kedua bagian. Model dapat **mengenali pasien**, bukan mempelajari pola penyakit. Ibarat mahasiswa yang diuji dengan soal dari soal-soal yang sudah ia kerjakan bersama dosennya: ia menjawab karena **mengenali soal**, bukan karena paham.

Percobaan: 300 nasabah, masing-masing 8 baris, dengan model pencari tetangga terdekat (*1-NN*). Label setiap nasabah **diacak**, sehingga sebenarnya **tidak ada pola yang dapat dipelajari**. Jawaban jujur seharusnya sekitar 0,5.

| Cara membagi | Akurasi |
|--------------|---------|
| Acak | **0,996** |
| Berkelompok (`GroupKFold`) | **0,497** |

Akurasi 0,996 pada data yang polanya **tidak ada** menunjukkan bahwa model hanya mengenali nasabah. Akurasi 0,497 adalah gambaran jujurnya.

**Aturan.** Seluruh baris milik satu entitas harus masuk ke bagian yang **sama**.

```python
from sklearn.model_selection import GroupKFold

# groups berisi id entitas (misalnya id pasien) untuk tiap baris
gkf = GroupKFold(n_splits=5)
for idx_latih, idx_uji in gkf.split(X, y, groups=id_pasien):
    ...   # seluruh baris satu pasien berada di lipatan yang sama
```

Semakin banyak baris per entitas, semakin besar kebocorannya.

**Cek pemahaman 4.3.4.** Data berisi 12.000 baris dari 1.500 nasabah. Berapa rata-rata baris per nasabah, dan mengapa angka ini penting?

<details>
<summary>Jawaban</summary>

12.000 ÷ 1.500 = **8 baris per nasabah**. Semakin banyak baris per entitas, semakin besar peluang entitas yang sama berada di latih dan uji sekaligus, sehingga kebocoran kelompok makin kuat.

</details>

### 4.3.5 Memilih Strategi: Tiga Pertanyaan

Untuk setiap data baru, jawablah tiga pertanyaan berikut **secara berurutan**:

```
  1. Apakah ada urutan waktu yang bermakna?
        ya  → TEMPORAL
        tidak ↓
  2. Apakah satu entitas muncul di lebih dari satu baris?
        ya  → BERKELOMPOK
        tidak ↓
  3. Apakah kelas sangat tidak seimbang?
        ya  → STRATIFIKASI
        tidak → ACAK
```

Dua strategi dapat digabung bila dua keadaan sekaligus berlaku, misalnya `StratifiedGroupKFold`. Alat ini tersedia di `scikit-learn`.

---

## 4.4 Validasi Silang

### 4.4.1 Situasi: Satu Pembagian Bisa Menyesatkan

**Situasi.** Anda memiliki hanya 10 data. Dengan 20% untuk validasi, data validasi hanya **2 baris**. Skor dari 2 baris sangat bergantung pada baris mana yang kebetulan terpilih.

**Tebak dahulu.** Bagaimana cara memperoleh taksiran yang lebih stabil **tanpa menambah data**?

**Gagasan.** Bagi data menjadi beberapa **lipatan** (*fold*), lalu **bergiliran** setiap lipatan menjadi validasi, sementara lipatan lain menjadi latih. Hasilnya beberapa skor, bukan satu.

### 4.4.2 Contoh Kecil: 10 Data, 5 Lipatan

Indeks data 0 sampai 9, dibagi 5 lipatan (masing-masing 2 data).

| Putaran | Latih | Validasi |
|---------|-------|----------|
| 1 | 2, 3, 4, 5, 6, 7, 8, 9 | 0, 1 |
| 2 | 0, 1, 4, 5, 6, 7, 8, 9 | 2, 3 |
| 3 | 0, 1, 2, 3, 6, 7, 8, 9 | 4, 5 |
| 4 | 0, 1, 2, 3, 4, 5, 8, 9 | 6, 7 |
| 5 | 0, 1, 2, 3, 4, 5, 6, 7 | 8, 9 |

```
  ┌────┬────┬────┬────┬────┐
  │ V  │ L  │ L  │ L  │ L  │  → skor 1
  ├────┼────┼────┼────┼────┤
  │ L  │ V  │ L  │ L  │ L  │  → skor 2
  ├────┼────┼────┼────┼────┤
  │ L  │ L  │ V  │ L  │ L  │  → skor 3
  ├────┼────┼────┼────┼────┤
  │ L  │ L  │ L  │ V  │ L  │  → skor 4
  ├────┼────┼────┼────┼────┤
  │ L  │ L  │ L  │ L  │ V  │  → skor 5
  └────┴────┴────┴────┴────┘
       Kinerja = rerata ± simpangan baku
```

Setiap data **tepat satu kali** menjadi validasi dan **empat kali** menjadi latih.

**Menghitung dengan tangan.** Misalkan kelima skor adalah 0,62; 0,89; 0,58; 0,91; 0,70.

1. **Rerata** = (0,62 + 0,89 + 0,58 + 0,91 + 0,70) ÷ 5 = 3,70 ÷ 5 = **0,74**.
2. **Selisih terhadap rerata:** −0,12; +0,15; −0,16; +0,17; −0,04.
3. **Kuadrat selisih:** 0,0144; 0,0225; 0,0256; 0,0289; 0,0016. Jumlahnya **0,0930**.
4. **Ragam sampel** = 0,0930 ÷ (5 − 1) = 0,02325.
5. **Simpangan baku sampel** = √0,02325 ≈ **0,153**.

Hasil dilaporkan sebagai **0,74 ± 0,15**.

**Catatan.** Pembagi pada langkah 4 adalah n − 1 (simpangan baku *sampel*). Fungsi `skor.std()` pada `numpy` secara bawaan memakai pembagi n dan menghasilkan 0,136. Tuliskan pada laporan **mana yang Anda pakai**.

### 4.4.3 Kode

```python
from sklearn.model_selection import cross_val_score, StratifiedKFold
import numpy as np

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# PENTING: yang divalidasi-silang adalah PIPELINE, bukan model saja.
# Dengan begitu prapemrosesan di-fit ulang pada tiap lipatan
# dan tidak pernah melihat lipatan validasi.
skor = cross_val_score(pipeline, X_latih, y_latih, cv=cv, scoring="f1")

print(f"F1 = {skor.mean():.3f} ± {skor.std(ddof=1):.3f}")   # ddof=1: simpangan baku sampel
print("Per lipatan:", np.round(skor, 3))
```

Perhatikan bahwa validasi silang dilakukan pada **data latih** saja. Data uji tetap disimpan untuk penilaian akhir satu kali.

### 4.4.4 Membaca Simpangan Antarlipatan

Rerata saja tidak cukup. Bandingkan dua keadaan berikut:

| Skor ketiga lipatan | Rerata | Simpangan baku sampel |
|---------------------|--------|-----------------------|
| 0,79; 0,80; 0,81 | 0,80 | **0,01** |
| 0,60; 0,80; 1,00 | 0,80 | **0,20** |

Rerata keduanya sama, 0,80, tetapi artinya sangat berbeda. Pada baris pertama kinerja **stabil**. Pada baris kedua kinerja **sangat bergantung pada lipatan**, sehingga angka 0,80 tidak dapat dipercaya begitu saja.

| Keadaan | Tafsir | Tindakan |
|---------|--------|----------|
| Simpangan < 0,02 | Kinerja stabil | Dapat dipercaya |
| 0,02–0,05 | Wajar pada data terbatas | Laporkan rerata **dan** simpangan |
| > 0,10 | Data sedikit, atau ada lipatan yang sangat berbeda | Selidiki lipatan yang menyimpang |
| Satu lipatan jauh lebih rendah | Ada kelompok atau periode yang berbeda sifat | Periksa apakah strategi pembagian sudah tepat |

> **Melaporkan rerata tanpa simpangan menyembunyikan informasi penting.**

**Cek pemahaman 4.4.** Skor validasi silang 5 lipatan adalah 0,81; 0,80; 0,82; 0,81; 0,41. Apa yang menarik perhatian Anda, dan apa langkah pertama yang diambil?

<details>
<summary>Jawaban</summary>

Satu lipatan (0,41) **jauh lebih rendah** daripada empat lainnya. Rerata (0,73) menyembunyikan hal ini. Langkah pertama: **periksa isi lipatan itu**. Mungkin ia memuat kelompok atau periode yang berbeda sifat, atau memuat data yang bermasalah. Setelah itu, periksa apakah strategi pembagian sudah tepat.

</details>

---

## 4.5 Enam Jenis Kebocoran

Setiap jenis kebocoran dibahas dengan pola yang sama: **kasus**, **mekanisme** (mengapa bocor), **cara mengenali**, dan **cara mencegah**.

### 4.5.1 Kebocoran Prapemrosesan

**Kasus.** Transformasi seperti penskalaan di-*fit* pada **seluruh data** sebelum data dibagi.

**Contoh kecil.** Sepuluh nilai umur: 20, 22, 23, 25, 26, 28, 30, 45, 50, 90. Misalkan delapan nilai pertama menjadi data latih dan dua nilai terakhir (50 dan 90) menjadi data uji. Penskalaan baku mengubah setiap nilai menjadi *skor z* = (nilai − rerata) ÷ simpangan baku.

| Cara | Rerata | Simpangan baku | Skor z untuk umur 90 |
|------|--------|----------------|-----------------------|
| **Bocor** (statistik dari seluruh 10 data) | 35,9 | 20,33 | (90 − 35,9) ÷ 20,33 = **2,66** |
| **Benar** (statistik hanya dari 8 data latih) | 27,375 | 7,31 | (90 − 27,375) ÷ 7,31 = **8,57** |

Pada cara yang bocor, nilai uji 90 tampak hanya **agak** ekstrem (2,66). Padahal terhadap data latih, nilai itu **sangat** ekstrem (8,57). Cara yang bocor **melembutkan** keganjilan data uji karena nilai ujinya ikut membentuk rerata dan simpangan bakunya.

**Mekanisme.** Statistik dihitung dengan ikut memakai data uji. Informasi dari data uji menyusup ke dalam model melalui hasil transformasi.

**Cara mengenali.** Dalam kode, `fit` atau `fit_transform` dipanggil pada seluruh data **sebelum** `train_test_split`.

**Cara mencegah.** Gunakan `Pipeline`, sehingga `fit` hanya terjadi pada data latih.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# SALAH: statistik dihitung dari seluruh data
# X_skala = StandardScaler().fit_transform(X)
# X_latih, X_uji = train_test_split(X_skala)

# BENAR: bagi dahulu, penskalaan dipelajari hanya dari data latih
model = Pipeline([
    ("skala", StandardScaler()),
    ("klasifikasi", LogisticRegression()),
])
model.fit(X_latih, y_latih)          # fit hanya melihat data latih
```

### 4.5.2 Kebocoran Temporal

**Kasus.** Fitur memuat informasi yang **belum tersedia** pada saat prediksi dibutuhkan.

**Contoh kecil.**

| Kasus | Waktu prediksi dibutuhkan | Fitur yang bocor | Mengapa belum tersedia |
|-------|---------------------------|------------------|-------------------------|
| Prediksi gagal bayar | Saat pengajuan kredit | Riwayat pembayaran setelah pencairan | Belum terjadi |
| Prediksi keterlambatan paket | Saat paket masuk gudang | Status perjalanan berikutnya | Belum terjadi |
| Prediksi putus kuliah | Akhir semester 3 | IPK semester 5 | Belum terjadi |

**Mekanisme.** Data historis yang kita miliki sudah lengkap, sehingga kolom masa depan tersedia saat pelatihan. Pada pemakaian sesungguhnya, kolom itu **kosong** karena kejadiannya belum terjadi.

**Cara mengenali.** Untuk **setiap fitur**, tanyakan: *"Apakah nilai ini sudah ada pada saat prediksi dibutuhkan?"*

**Cara mencegah.** Jawablah jujur pertanyaan 3 dan 4 pada formulasi Bab 2: *kapan prediksi dibutuhkan, dan apa yang tersedia pada saat itu?* Susun **daftar fitur terlarang** sebelum pemodelan.

### 4.5.3 Kebocoran Duplikat

**Kasus.** Baris yang sama, atau nyaris sama, muncul di data latih **dan** data uji.

**Contoh kecil.** Data 200 baris dengan label **acak** (jawaban jujur seharusnya 0,5) diduplikasi sehingga menjadi 400 baris, lalu dibagi acak. Dengan model pencari tetangga terdekat (*1-NN*):

| Keadaan | Akurasi |
|---------|---------|
| Data tanpa duplikat | **0,55** |
| Data dengan setiap baris diduplikasi | **0,833** |

Pada data duplikat, banyak baris uji **memiliki kembaran** di data latih, sehingga model cukup mengingat jawabannya.

**Mekanisme.** Model "mengenali" baris yang pernah ia lihat.

**Cara mengenali dan mencegah.** Periksa duplikat **sebelum** membagi data.

```python
print("Duplikat penuh            :", df.duplicated().sum())
print("Duplikat tanpa kolom id   :", df.drop(columns=["id"]).duplicated().sum())
```

Pemeriksaan kedua penting karena dua baris yang sama dapat tampak berbeda hanya karena kolom `id`-nya berbeda.

### 4.5.4 Kebocoran Kelompok

**Kasus.** Satu entitas tersebar di data latih dan data uji.

**Contoh kecil.** Telah dibahas pada §4.3.4: akurasi 0,996 pada pembagian acak, padahal jawaban jujurnya 0,497.

**Mekanisme.** Model mengenali entitas, bukan mempelajari pola.

**Cara mencegah.** `GroupKFold` (§4.3.4).

### 4.5.5 Kebocoran Target

**Kasus.** Sebuah fitur sebenarnya merupakan **turunan** atau **akibat** dari target.

**Contoh kecil.**

| Fitur mencurigakan | Mengapa bocor |
|--------------------|---------------|
| `jumlah_tagihan_tertunggak` untuk memprediksi gagal bayar | Ia *adalah* gagal bayar |
| `lama_dirawat` untuk memprediksi keparahan penyakit | Akibat dari keparahan, bukan sebab |
| `nomor_invoice` untuk memprediksi pembelian | Hanya ada bila pembelian terjadi |

Percobaan: target biner dengan tiga fitur biasa, lalu satu fitur tambahan yang dibuat sebagai akibat dari target.

| Keadaan | ROC-AUC |
|---------|---------|
| Tanpa fitur bocor | **0,779** |
| Dengan fitur bocor | **1,000** |

Korelasi fitur bocor terhadap target adalah **0,979**.

**Mekanisme.** Fitur memuat jawaban secara langsung.

**Cara mengenali.** Korelasi terhadap target mendekati sempurna, atau kinerja model jauh di atas yang masuk akal.

**Cara mencegah.** Pertanyaan yang sama dengan §4.5.2, ditambah: *"Apakah kolom ini ada karena target sudah terjadi?"*

### 4.5.6 Kebocoran melalui Pemilihan Berulang

**Kasus.** Data uji dipakai berkali-kali untuk memilih model, fitur, atau hiperparameter.

**Contoh kecil.** Percobaan 30 model penebak acak di §4.2.2: skor terbaik 0,644 padahal kemampuan sebenarnya 0,5.

Ada versi yang lebih halus: **pemilihan fitur di luar validasi silang**. Data 300 baris dan 50 fitur yang **seluruhnya acak** (tidak ada pola sama sekali):

| Cara | Akurasi validasi silang |
|------|--------------------------|
| Memilih 5 fitur terbaik dari **seluruh data**, lalu validasi silang | **0,577** (bocor) |
| Pemilihan fitur **di dalam** `Pipeline` | **0,457** |

Jawaban jujur untuk data tanpa pola adalah sekitar 0,5. Cara pertama tampak lebih baik karena pemilihan fitur sudah **melihat label** seluruh data.

**Cara mencegah.** Pilih memakai data validasi, dan sentuh data uji **sekali saja**. Masukkan seluruh langkah pemilihan ke dalam `Pipeline`.

```python
from sklearn.feature_selection import SelectKBest, f_classif

pipa = Pipeline([
    ("pilih", SelectKBest(f_classif, k=5)),     # dipelajari ulang di tiap lipatan
    ("klasifikasi", LogisticRegression()),
])
skor = cross_val_score(pipa, X, y, cv=5)
```

**Cek pemahaman 4.5.** Sebutkan jenis kebocoran pada setiap kasus: (a) Skala dihitung dari seluruh data. (b) Kolom `status_verifikasi` diisi setelah keputusan kredit dibuat. (c) 20% baris data muncul dua kali. (d) Data deret waktu dibagi acak.

<details>
<summary>Jawaban</summary>

(a) Kebocoran **prapemrosesan**. (b) Kebocoran **temporal** atau **target**, karena nilai itu baru ada setelah keputusan. (c) Kebocoran **duplikat**. (d) Kebocoran **temporal**, melalui pembagian yang salah.

</details>

---

## 4.6 Daftar Periksa Kebocoran

Wajib dijalankan sebelum mengumpulkan pekerjaan apa pun:

- [ ] Seluruh transformasi berada di dalam `Pipeline`
- [ ] `fit` hanya pernah dipanggil pada data latih
- [ ] Data uji tidak dipakai untuk memilih model, fitur, atau hiperparameter
- [ ] Bila ada urutan waktu: pembagian temporal, bukan acak
- [ ] Bila ada entitas berulang: `GroupKFold`
- [ ] Duplikat diperiksa sebelum pembagian
- [ ] Setiap fitur lolos pertanyaan: *"tersedia saat prediksi dibutuhkan?"*
- [ ] Tidak ada fitur yang merupakan turunan target
- [ ] **Skor yang mencurigakan tinggi sudah diselidiki, bukan dirayakan**

> **Kaidah praktis:** bila kinerja model jauh melampaui yang masuk akal untuk masalah itu, kemungkinan terbesarnya bukan bahwa modelnya hebat, melainkan bahwa ada kebocoran yang belum ditemukan.

---

## AI Corner — Tahap *Understand → Apply*

### Kebocoran Adalah Kesalahan yang Tidak Dapat Dideteksi Alat

Tidak ada pustaka yang dapat memeriksa apakah sebuah fitur "tersedia saat prediksi dibutuhkan". Pertanyaan itu menuntut pengetahuan tentang **proses bisnis** yang menghasilkan data: kapan setiap kolom terisi, oleh siapa, dan dalam urutan apa.

Model bahasa dapat mengenali pola kebocoran yang **tampak dari kode**, misalnya `fit_transform` sebelum `train_test_split`. Ia **tidak** dapat mengenali kebocoran yang tersembunyi dalam **makna kolom**, karena ia tidak mengetahui arti kolom itu pada organisasi yang menerbitkannya.

| Dapat dideteksi dari kode | Hanya dapat dikenali dari pemahaman domain |
|---------------------------|--------------------------------------------|
| `fit` di luar `Pipeline` | Kolom `lama_dirawat` adalah akibat, bukan sebab |
| Pembagian acak pada data bertanggal | Kolom `nomor_invoice` hanya ada bila transaksi terjadi |
| Pemilihan fitur sebelum pembagian | Kolom `status_verifikasi` diisi setelah keputusan dibuat |

### Pemakaian yang Wajar

```
Ini daftar 18 fitur saya untuk memprediksi gagal bayar kredit,
yang diprediksi SAAT PENGAJUAN diterima:
[daftar fitur dengan penjelasan singkat tiap kolom]

Saya sudah menandai 3 fitur sebagai berisiko bocor: [sebutkan].

Tolong periksa daftar ini terhadap pertanyaan "apakah nilai ini
sudah ada pada saat pengajuan diterima?" dan sebutkan bila ada
yang saya lewatkan. Jangan ubah daftar saya; cukup tunjukkan
yang perlu saya periksa ulang.
```

Prompt ini berhasil karena memberikan konteks yang tidak dimiliki AI (arti tiap kolom dan kapan prediksi dibutuhkan), sekaligus membatasi perannya pada pemeriksaan.

**Pengingat.** Pada praktikum dan proyek, *menandai fitur sebagai berisiko bocor* adalah penilaian Anda sendiri. AI boleh memeriksa daftar yang sudah Anda susun, tetapi tidak menggantikan penilaian itu, dan pemakaiannya wajib dicatat pada AI Usage Log.

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan peran berbeda data latih, validasi, dan uji. Mengapa data uji hanya boleh dipakai sekali? (Petunjuk: ingat percobaan 30 model penebak acak pada §4.2.2.)

2. Tentukan strategi pembagian yang tepat untuk masing-masing, dengan menjawab tiga pertanyaan §4.3.5:
   (a) Data 50.000 transaksi dengan 1,2% penipuan.
   (b) Data penjualan harian selama tiga tahun.
   (c) Data 8.000 kunjungan dari 900 pasien.
   (d) Data 400 provinsi-tahun tanpa urutan yang bermakna.

3. Sebutkan enam jenis kebocoran data dan berikan satu contoh singkat untuk masing-masing.

4. Sebuah laporan menyebutkan "F1 = 0,84". Informasi apa yang hilang, dan mengapa ia penting?

### Tingkat Menengah

5. Perhatikan kode berikut:
   ```python
   X_scaled = StandardScaler().fit_transform(X)
   pemilih = SelectKBest(f_classif, k=10).fit(X_scaled, y)
   X_sel = pemilih.transform(X_scaled)
   X_tr, X_te, y_tr, y_te = train_test_split(X_sel, y, test_size=0.2)
   ```
   (a) Temukan dua kebocoran.
   (b) Jelaskan mekanisme masing-masing.
   (c) Tuliskan versi yang benar dengan `Pipeline`.
   (d) Kebocoran mana yang dampaknya lebih besar? Jelaskan.

6. Sebuah tim memprediksi keterlambatan pengiriman dan memperoleh ROC-AUC 0,997.
   (a) Apa reaksi pertama Anda?
   (b) Sebutkan tiga fitur yang paling mungkin menjadi penyebabnya.
   (c) Bagaimana cara memastikan dugaan itu?
   (d) Apa yang akan terjadi pada skornya setelah fitur itu dibuang?

7. Sebuah data memuat 12.000 baris dari 1.500 nasabah (rata-rata 8 baris per nasabah).
   (a) Kebocoran jenis apa yang terjadi bila dibagi secara acak?
   (b) Jelaskan mengapa model dapat "mengenali" nasabah.
   (c) Tuliskan kode pembagian yang benar.
   (d) Apakah selisih skornya akan besar atau kecil? Faktor apa yang menentukannya?

8. Validasi silang 5 lipatan menghasilkan skor: 0,62; 0,89; 0,58; 0,91; 0,70.
   (a) Hitung rerata dan simpangan baku sampel, dengan langkah seperti pada §4.4.2. (Hasil yang dapat Anda cocokkan: rerata 0,74.)
   (b) Apa yang ditunjukkan sebaran ini?
   (c) Sebutkan tiga kemungkinan penyebabnya.
   (d) Apa yang akan Anda periksa lebih dahulu?

### Tingkat Mahir

9. Bangun demonstrasi kebocoran yang dapat diajarkan.
   (a) Ambil dataset nyata dengan urutan waktu.
   (b) Bangun notebook yang mengandung **empat** jenis kebocoran berbeda.
   (c) Catat skornya.
   (d) Perbaiki satu per satu, catat skor setelah tiap perbaikan.
   (e) Buat grafik penurunan skor terhadap tahap perbaikan.
   (f) Tuliskan penjelasan mengapa tiap perbaikan menurunkan skor.

10. Audit sebuah proyek pembelajaran mesin publik.
    (a) Pilih satu *notebook* atau makalah yang tersedia terbuka.
    (b) Terapkan daftar periksa §4.6.
    (c) Untuk setiap butir yang tidak terpenuhi, jelaskan risikonya.
    (d) Perkirakan arah dan besar biasnya.
    (e) Tuliskan tiga pertanyaan yang akan Anda ajukan kepada penulisnya.

11. Tulislah pedoman satu halaman berjudul *"Memeriksa Kebocoran pada Data yang Anda Terima dari Orang Lain"*. Sertakan: pertanyaan yang harus diajukan kepada penyedia data, tanda-tanda yang dapat dikenali dari data itu sendiri, dan cara menyatakan temuan kepada pihak yang memberi data tanpa menuduh.

---

## Rangkuman

1. **Kebocoran data memberi hadiah ketika dilakukan**; itulah yang membuatnya berbahaya.
2. Data uji **dipakai satu kali, di paling akhir**. Memilih model berdasarkan skor uji berarti memilih berdasarkan kebetulan: pada percobaan, skor terbaik dari 30 penebak acak mencapai 0,644 padahal kemampuan sebenarnya 0,5.
3. Strategi pembagian mengikuti **sifat data**: temporal bila ada urutan waktu, berkelompok bila ada entitas berulang, stratifikasi bila kelas tak seimbang, acak bila tidak ada keadaan khusus.
4. **Pembagian acak pada data berurutan waktu menghasilkan kebocoran** karena model mengintip masa depan.
5. Yang divalidasi-silang adalah **`Pipeline`**, bukan model saja.
6. Laporkan **rerata dan simpangan baku** antarlipatan, dan sebutkan jenis simpangan baku yang dipakai.
7. **Enam jenis kebocoran:** prapemrosesan, temporal, duplikat, kelompok, target, pemilihan berulang.
8. **Skor yang terlalu bagus adalah tanda bahaya**, bukan tanda keberhasilan.
9. Kebocoran yang tersembunyi dalam **makna kolom** tidak dapat dideteksi alat mana pun; ia menuntut pemahaman domain.
10. Daftar periksa §4.6 dijalankan sebelum setiap pengumpulan.

---

## Referensi

1. Kapoor, S., & Narayanan, A. (2023). Leakage and the Reproducibility Crisis in ML-based Science. *Patterns*, 4(9), 100804.
2. Kaufman, S., Rosset, S., & Perlich, C. (2012). Leakage in Data Mining. *ACM TKDD*, 6(4), 1–21.
3. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 2. O'Reilly.
4. Müller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*, Bab 5. O'Reilly.
5. Dokumentasi scikit-learn — *Cross-validation*. <https://scikit-learn.org/stable/modules/cross_validation.html>

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
