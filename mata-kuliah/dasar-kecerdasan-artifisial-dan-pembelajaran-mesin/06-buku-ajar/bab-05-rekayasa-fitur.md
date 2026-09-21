# BAB 5: REKAYASA FITUR

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK102-1` | Merancang fitur baru dari data mentah dengan pengetahuan domain | C6 |
| `DAIML-Sub-CPMK102-1` | Menganalisis kontribusi tiap fitur terhadap kinerja validasi | C4 |
| `DAIML-Sub-CPMK102-1` | Mengevaluasi apakah sebuah fitur menimbulkan kebocoran | C5 |

---

## 5.1 Fitur Menentukan Batas Atas Kinerja

> *"Rekayasa fitur yang dilakukan dengan baik sering memberi peningkatan lebih besar daripada pergantian algoritma."* — Domingos (2012)

Model hanya dapat belajar dari apa yang diberikan kepadanya. Bila informasi yang dibutuhkan tidak ada dalam fitur, **tidak ada algoritma yang dapat memunculkannya**.

**Contoh yang paling jelas:** memprediksi kemacetan dari kolom `timestamp` mentah. Model kesulitan, karena jumlah detik sejak 1970 tidak bermakna bagi masalah ini. Setelah `timestamp` diurai menjadi `jam`, `hari_dalam_minggu`, `hari_libur`, dan `jam_sibuk`, model yang **sama persis** — tanpa satu pun hiperparameter diubah — menjadi jauh lebih baik.

| Tahap | Fitur | F1 validasi |
|-------|-------|-------------|
| *Baseline* | `timestamp` sebagai angka | 0,52 |
| + fitur waktu terurai | `jam`, `hari_minggu`, `akhir_pekan` | 0,71 |
| + penyandian siklik | `jam_sin`, `jam_cos` | 0,74 |
| + pengetahuan domain | `jam_sibuk`, `hari_libur` | 0,81 |

Peningkatan 0,29 tanpa mengganti model.

---

## 5.2 Membuat Fitur Baru

### 5.2.1 Fitur Waktu

```python
df["tanggal"] = pd.to_datetime(df["tanggal"])

df["tahun"]       = df["tanggal"].dt.year
df["bulan"]       = df["tanggal"].dt.month
df["hari_minggu"] = df["tanggal"].dt.dayofweek      # 0 = Senin
df["akhir_pekan"] = (df["hari_minggu"] >= 5).astype(int)
df["jam"]         = df["tanggal"].dt.hour
df["jam_sibuk"]   = df["jam"].isin([6,7,8,16,17,18,19]).astype(int)

# Hari besar nasional — memerlukan pengetahuan domain
libur = pd.to_datetime(["2026-01-01", "2026-03-20", "2026-05-01", "2026-08-17"])
df["hari_libur"] = df["tanggal"].dt.normalize().isin(libur).astype(int)
```

**Penyandian siklik** untuk variabel yang melingkar:

```python
import numpy as np

# Jam 23 dan jam 0 berdekatan, tetapi selisih angkanya 23.
df["jam_sin"] = np.sin(2 * np.pi * df["jam"] / 24)
df["jam_cos"] = np.cos(2 * np.pi * df["jam"] / 24)
```

### 5.2.2 Fitur Rasio dan Interaksi

Sering lebih informatif daripada komponennya sendiri-sendiri:

| Fitur asal | Fitur turunan | Mengapa lebih baik |
|------------|---------------|--------------------|
| `omzet`, `jumlah_pegawai` | `omzet_per_pegawai` | Produktivitas, bebas skala usaha |
| `luas_bangunan`, `luas_tanah` | `rasio_bangunan` | Kepadatan bangunan |
| `total_pinjaman`, `pendapatan` | `rasio_beban_utang` | **Ukuran baku dalam penilaian kredit** |
| `jarak`, `waktu_tempuh` | `kecepatan_rata` | Kondisi lalu lintas |

> Baris ketiga menunjukkan poin terpenting bab ini: **fitur terbaik sering sudah dikenal oleh praktisi bidangnya**. Berbicara dengan seorang analis kredit selama satu jam lebih berguna daripada mencoba seratus kombinasi fitur secara acak.

### 5.2.3 Fitur Agregat dan Bahayanya

```python
# Rata-rata omzet per provinsi
df["omzet_rata_provinsi"] = df.groupby("provinsi")["omzet"].transform("mean")
df["omzet_relatif"] = df["omzet"] / df["omzet_rata_provinsi"]
```

**Perhatian:** perhitungan di atas memakai **seluruh data**, termasuk bagian uji. Ini adalah kebocoran. Pada pekerjaan yang benar, agregat semacam ini harus dihitung **di dalam `Pipeline`** sebagai transformer tersendiri, agar di-*fit* hanya pada lipatan latih.

### 5.2.4 Fitur Geografis Indonesia

```python
wilayah = {
    "DKI Jakarta": "Jawa", "Jawa Barat": "Jawa", "Jawa Tengah": "Jawa",
    "Sumatera Utara": "Sumatera", "Riau": "Sumatera",
    "Kalimantan Timur": "Kalimantan", "Sulawesi Selatan": "Sulawesi",
    "Papua": "Papua", "Bali": "Bali-Nusra",
}
df["pulau"] = df["provinsi"].map(wilayah).fillna("Lainnya")
```

Pengelompokan ini mengurangi kardinalitas dari 38 menjadi 6, sekaligus memuat informasi geografis yang bermakna.

---

## 5.3 Transformasi Fitur

| Transformasi | Rumus | Kapan dipakai |
|--------------|-------|---------------|
| Logaritma | $\log(x+1)$ | Menceng kanan berat (pendapatan, populasi) |
| Akar kuadrat | $\sqrt{x}$ | Menceng kanan sedang; data cacahan |
| Yeo-Johnson | Otomatis | Mencari transformasi terbaik; menerima nilai negatif |
| Binning | Pengelompokan rentang | Hubungan tidak monoton; menambah ketahanan |
| Polinomial | $x, x^2, x_1x_2$ | Hubungan melengkung dan interaksi |

```python
from sklearn.preprocessing import PowerTransformer, KBinsDiscretizer

pt = PowerTransformer(method="yeo-johnson")
binner = KBinsDiscretizer(n_bins=5, encode="ordinal", strategy="quantile")
```

> **Peringatan:** `PolynomialFeatures(degree=3)` pada 20 fitur menghasilkan lebih dari 1.700 kolom. Kombinasi *overfitting* dan kutukan dimensi hampir dipastikan. Derajat 2 sudah jarang diperlukan.

---

## 5.4 Pemilihan Fitur

### 5.4.1 Tiga Pendekatan

| Pendekatan | Cara | Kelebihan | Kekurangan |
|------------|------|-----------|------------|
| **Filter** | Statistik (korelasi, uji F, informasi bersama) | Cepat; bebas model | Mengabaikan interaksi antarfitur |
| **Wrapper** | Mencoba himpunan fitur dengan model (RFE) | Memperhitungkan interaksi | Mahal secara komputasi |
| **Embedded** | Terjadi saat pelatihan (Lasso, kepentingan pohon) | Efisien | Terikat pada model tertentu |

### 5.4.2 Pemilihan Fitur Adalah Sumber Kebocoran

```python
# ══════════ SALAH ══════════
X_terpilih = SelectKBest(k=15).fit_transform(X, y)    # ← y seluruhnya dipakai
X_tr, X_te = train_test_split(X_terpilih)
# Informasi target dari data uji sudah masuk ke pemilihan fitur.

# ══════════ BENAR ══════════
model = Pipeline([
    ("pemilihan", SelectKBest(k=15)),
    ("clf", RandomForestClassifier(random_state=42)),
])
# Dalam validasi silang, pemilihan di-fit ulang pada tiap lipatan latih.
```

Ini adalah jenis kebocoran yang paling sering luput, karena kodenya tampak wajar dan berjalan tanpa galat.

---

## 5.5 Kutukan Dimensi

Ketika jumlah fitur bertambah, data menjadi semakin jarang dalam ruang berdimensi tinggi.

| Akibat | Penjelasan |
|--------|------------|
| Jarak kehilangan makna | Pada dimensi tinggi, jarak antartitik menjadi hampir sama besar |
| Kebutuhan data meningkat eksponensial | Untuk kerapatan yang sama, jumlah data harus bertambah jauh lebih cepat |
| *Overfitting* lebih mudah terjadi | Model menemukan pola kebetulan dengan lebih mudah |
| Komputasi melonjak | Waktu latih bertambah |

**Kaidah praktis:** sebagai ancar-ancar awal, sekurang-kurangnya 10 baris data per fitur untuk model linear — lebih banyak lagi untuk model kompleks.

Tiga cara menguranginya:
1. **Pemilihan fitur** (§5.4) — membuang fitur, mempertahankan sisanya apa adanya.
2. **Reduksi dimensi** (PCA, Bab 11) — mengganti fitur dengan kombinasi.
3. **Regularisasi** (Bab 6) — menekan koefisien fitur yang tidak berguna.

---

## 5.6 Alur Kerja Rekayasa Fitur

```
  1. Pahami domain           ── berbicara dengan ahli; baca definisi variabel
         ↓
  2. Bangun BASELINE         ── fitur mentah apa adanya
         ↓
  3. Tambah fitur BERTAHAP   ── satu kelompok dalam satu waktu
         ↓
  4. Ukur pada VALIDASI      ── bukan pada latih, bukan pada uji
         ↓
  5. Periksa KEBOCORAN       ── "tersedia saat prediksi dibutuhkan?"
         ↓
  6. Catat yang BERHASIL     ── dan yang GAGAL, beserta dugaan sebabnya
```

> **Mencatat fitur yang gagal sama pentingnya dengan mencatat yang berhasil.** Ia mencegah pengulangan percobaan yang sama, dan sering mengungkap sesuatu tentang datanya — misalnya bahwa suatu variabel yang diduga penting ternyata tidak memuat informasi yang berbeda dari variabel lain.

---

## AI Corner — Tahap *Understand → Apply*

### Di Mana AI Berguna dan Di Mana Ia Menyesatkan

Rekayasa fitur adalah salah satu bagian di mana bantuan AI paling berguna — **pada tingkat sintaks**, bukan pada tingkat keputusan.

| Berguna | Menyesatkan |
|---------|-------------|
| "Bagaimana cara mengurai kolom tanggal menjadi jam dan hari dalam pandas?" | "Fitur apa yang harus saya buat untuk data ini?" |
| "Tuliskan penyandian siklik untuk variabel jam." | "Apakah fitur ini akan membantu?" |
| "Bagaimana membuat transformer sendiri untuk `Pipeline`?" | "Fitur mana yang harus saya buang?" |

Alasannya sama dengan bab-bab sebelumnya: **fitur yang baik berasal dari pemahaman domain**, dan pemahaman itu tidak ada dalam prompt. AI dapat menyarankan "buat fitur rasio utang terhadap pendapatan" karena pola itu lazim dalam teks yang melatihnya — tetapi ia tidak tahu apakah kolom `pendapatan` pada data Anda berarti pendapatan kotor, bersih, atau hasil proyeksi.

### Bahaya Khusus: Saran Fitur yang Bocor

Diminta menyarankan fitur untuk memprediksi gagal bayar, model bahasa sangat mungkin menyarankan "riwayat keterlambatan pembayaran" — saran yang masuk akal secara umum, dan **bocor** bila prediksinya dibutuhkan saat pengajuan, sebelum ada pembayaran apa pun.

Karena itu setiap saran fitur, dari sumber mana pun, harus melewati pertanyaan yang sama: *"apakah nilai ini sudah ada pada saat prediksi dibutuhkan?"*

---

## Latihan Soal

### Tingkat Dasar

1. Uraikan kolom `timestamp` menjadi minimal lima fitur yang bermakna, dan jelaskan kegunaan masing-masing untuk memprediksi kepadatan penumpang kereta.

2. Jelaskan mengapa penyandian siklik diperlukan untuk variabel jam, dan mengapa `jam` sebagai angka 0–23 saja tidak memadai.

3. Untuk tiap pasang fitur berikut, buat satu fitur rasio yang lebih informatif dan jelaskan alasannya:
   (a) `total_belanja`, `jumlah_transaksi`
   (b) `jumlah_penduduk`, `luas_wilayah`
   (c) `jumlah_dokter`, `jumlah_penduduk`

4. Jelaskan perbedaan pemilihan fitur dan reduksi dimensi dalam dua kalimat.

### Tingkat Menengah

5. Sebuah tim menambahkan fitur `rata_rata_target_per_kategori` (*target encoding*) yang dihitung dari seluruh data sebelum pembagian.
   (a) Kebocoran jenis apa ini?
   (b) Jelaskan mekanismenya.
   (c) Mengapa kebocoran ini sangat sulit dikenali dari melihat kodenya saja?
   (d) Tuliskan cara yang benar.

6. Sebuah dataset memiliki 24 fitur dan 300 baris.
   (a) Berapa rasio baris per fitur?
   (b) Masalah apa yang dapat timbul?
   (c) Sebutkan tiga cara menanganinya beserta kelebihan masing-masing.
   (d) Bila `PolynomialFeatures(degree=2)` ditambahkan, berapa fitur yang dihasilkan? Apakah bijaksana?

7. Setelah menambahkan sepuluh fitur baru, F1 validasi naik dari 0,71 menjadi 0,73, sementara simpangan antarlipatan adalah 0,04.
   (a) Apakah peningkatan ini bermakna? Jelaskan.
   (b) Informasi apa yang masih dibutuhkan untuk memutuskan?
   (c) Biaya apa yang menyertai penambahan sepuluh fitur?
   (d) Apa yang akan Anda lakukan?

8. Seorang mahasiswa mencoba 40 kombinasi fitur, memilih yang terbaik berdasarkan skor **data uji**, lalu melaporkan skor itu sebagai kinerja akhir.
   (a) Kebocoran jenis apa ini?
   (b) Mengapa skornya bias ke atas?
   (c) Bagaimana cara yang benar?
   (d) Bila hanya ada satu himpunan data, teknik apa yang memberi taksiran tidak bias?

### Tingkat Mahir

9. Lakukan rekayasa fitur bertahap dengan model terkunci.
   (a) Pilih dataset nyata dengan kolom waktu dan kolom kategorik.
   (b) Kunci model dan hiperparameternya.
   (c) Bangun *baseline* dengan fitur mentah.
   (d) Tambahkan minimal lima kelompok fitur secara bertahap, ukur setiap tahap pada validasi silang.
   (e) Buat grafik peningkatan dengan pita simpangan.
   (f) **Catat minimal tiga fitur yang gagal** beserta dugaan sebabnya.

10. Bangun transformer agregat yang aman terhadap kebocoran.
    (a) Buat kelas transformer sendiri yang menghitung rata-rata target per kategori.
    (b) Pastikan `fit` hanya memakai data yang diberikan kepadanya.
    (c) Masukkan ke dalam `Pipeline` dan jalankan validasi silang.
    (d) Bandingkan skornya dengan versi yang dihitung dari seluruh data.
    (e) Jelaskan selisihnya dan mengapa versi kedua tidak sah.

11. Wawancarai seorang praktisi bidang tertentu (analis kredit, tenaga kesehatan, staf dinas) selama 30 menit tentang indikator apa yang mereka pakai untuk menilai sesuatu. Susun laporan satu halaman: indikator apa yang mereka sebut, bagaimana masing-masing dapat dijadikan fitur, dan mana yang berisiko bocor bila dipakai untuk prediksi.

---

## Rangkuman

1. **Fitur menentukan batas atas kinerja.** Model tidak dapat memunculkan informasi yang tidak ada.
2. Fitur waktu harus **diurai**; variabel siklik disandikan **sinus-kosinus**.
3. **Fitur rasio dan interaksi** sering lebih informatif daripada komponennya.
4. Fitur terbaik sering sudah dikenal praktisi bidangnya — **berbicara dengan ahli domain** lebih berguna daripada mencoba acak.
5. Fitur agregat **rawan kebocoran** bila dihitung dari seluruh data.
6. Transformasi log untuk sebaran menceng; **polinomial derajat tinggi hampir selalu berlebihan**.
7. Tiga pendekatan pemilihan fitur: **filter, wrapper, embedded**.
8. **Pemilihan fitur di luar `Pipeline` adalah kebocoran** yang paling sering luput.
9. **Kutukan dimensi:** data menjadi jarang; *overfitting* lebih mudah terjadi.
10. Tambahkan fitur **bertahap**, ukur pada **validasi**, dan **catat yang gagal**.

---

## Referensi

1. Zheng, A., & Casari, A. (2018). *Feature Engineering for Machine Learning*. O'Reilly.
2. Kuhn, M., & Johnson, K. (2019). *Feature Engineering and Selection*. CRC Press.
3. Domingos, P. (2012). A Few Useful Things to Know About Machine Learning. *CACM*, 55(10), 78–87.
4. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 2. O'Reilly.
5. Dokumentasi scikit-learn — *Feature selection*. <https://scikit-learn.org/stable/modules/feature_selection.html>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
