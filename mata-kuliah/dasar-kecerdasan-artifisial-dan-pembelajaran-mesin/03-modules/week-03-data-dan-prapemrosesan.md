# Minggu 3: Data dan Prapemrosesan

## Informasi Modul

| Aspek | Keterangan |
|-------|------------|
| Mata Kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin (`IF52510031`) |
| Minggu | 3 dari 16 |
| Topik | Kualitas data, nilai hilang, penyandian kategorik, penskalaan, `Pipeline` |
| Sub-CPMK | `DAIML-Sub-CPMK102-1` · ICM-03 |
| Bloom | C3 (Menerapkan) → C4 (Menganalisis) |
| Durasi | 150 menit |
| Metode | Kuliah · Demonstrasi · Praktikum |
| Penilaian | Observasi (Lab 3) |

---

## Tujuan Pembelajaran

Setelah mengikuti pertemuan ini, mahasiswa mampu:

1. **Memeriksa** (C3) kualitas dataset secara sistematis dan mengenali masalahnya.
2. **Menganalisis** (C4) pola nilai hilang dan memilih penanganan yang sesuai polanya.
3. **Menerapkan** (C3) penyandian variabel kategorik yang tepat untuk jenis datanya.
4. **Menjelaskan** (C2) mengapa penskalaan diperlukan oleh sebagian algoritma dan tidak oleh yang lain.
5. **Membangun** (P3) `Pipeline` dan `ColumnTransformer` yang mencegah kebocoran sejak awal.

---

## Materi Pembelajaran

### 3.1 Mengapa Tiga Minggu untuk Data

Survei industri berulang kali menunjukkan hal yang sama: praktisi ML menghabiskan sebagian besar waktunya pada data, bukan pada model. Alasannya bukan ketidakefisienan, melainkan bahwa **mutu data membatasi mutu model secara mutlak**.

> *Garbage in, garbage out.* Model tercanggih yang dilatih pada data yang cacat menghasilkan keluaran yang cacat — dengan tambahan bahaya bahwa keluarannya tampak meyakinkan.

Pergeseran perhatian dari model ke data (*data-centric AI*) adalah salah satu tren utama yang diuraikan pada [analisis strategis](../00-strategic-analysis/strategic-analysis.md) mata kuliah ini.

---

### 3.2 Pemeriksaan Kualitas Data

#### 3.2.1 Tujuh Perintah Pembuka

```python
import pandas as pd

df = pd.read_csv("data_umkm_jakarta.csv")

# 1. Bentuk data
print("Dimensi:", df.shape)

# 2. Tipe data dan jumlah non-null
df.info()

# 3. Ringkasan numerik — cari nilai yang mustahil
display(df.describe().T)

# 4. Nilai hilang per kolom, dalam persen
display((df.isna().mean() * 100).round(2).sort_values(ascending=False))

# 5. Baris duplikat
print("Duplikat penuh:", df.duplicated().sum())

# 6. Kardinalitas kolom kategorik
for kol in df.select_dtypes(include="object").columns:
    print(f"{kol:25s} {df[kol].nunique():5d} nilai unik")

# 7. Sebaran target — periksa keseimbangan kelas
print(df["target"].value_counts(normalize=True).round(3))
```

#### 3.2.2 Tanda Bahaya dan Penyebabnya

| Tanda | Kemungkinan penyebab | Tindakan |
|-------|----------------------|----------|
| Nilai `-99`, `9999`, `0` pada kolom yang mustahil | Kode nilai hilang tidak diterjemahkan | Ubah menjadi `NaN` sebelum apa pun |
| Kolom numerik bertipe `object` | Pemisah ribuan atau satuan ikut terbaca | Bersihkan lalu konversi |
| Kardinalitas kategorik sangat tinggi | Perbedaan ejaan/kapitalisasi | Bakukan sebelum penyandian |
| Rata-rata jauh dari median | Kemencengan berat atau pencilan | Pertimbangkan transformasi |
| Satu kelas < 1% dari data | Ketidakseimbangan ekstrem | Sesuaikan metrik dan strategi (Minggu 7) |
| Kolom dengan korelasi ~1 terhadap target | **Kemungkinan kebocoran** | Selidiki sebelum melanjutkan |

> Baris terakhir adalah penemuan yang paling melegakan bila terjadi di Minggu 3, dan paling merusak bila baru ditemukan di Minggu 14.

---

### 3.3 Nilai Hilang

#### 3.3.1 Tiga Pola

| Pola | Kepanjangan | Ciri | Penanganan yang sah |
|------|-------------|------|---------------------|
| **MCAR** | *Missing Completely At Random* | Hilang tidak berkaitan dengan apa pun | Penghapusan baris aman |
| **MAR** | *Missing At Random* | Hilang berkaitan dengan variabel lain yang teramati | Imputasi bersyarat |
| **MNAR** | *Missing Not At Random* | Hilang berkaitan dengan nilai yang hilang itu sendiri | **Tidak dapat diperbaiki secara statistik** — wajib dinyatakan sebagai keterbatasan |

**Contoh MNAR:** pelaku UMKM berpenghasilan tinggi cenderung tidak mengisi kolom omzet. Imputasi rata-rata akan **selalu** menghasilkan taksiran yang terlalu rendah, berapa pun canggihnya metode yang dipakai.

#### 3.3.2 Pilihan Penanganan

| Metode | Kapan sesuai | Risiko |
|--------|--------------|--------|
| Hapus baris | MCAR dan proporsinya kecil (< 5%) | Kehilangan data; bias bila bukan MCAR |
| Hapus kolom | Hilang > 60% dan kolom tidak penting | Kehilangan sinyal |
| Imputasi rata-rata/median | Numerik, MCAR/MAR | Mengecilkan varians |
| Imputasi modus | Kategorik | Memperkuat kelas mayoritas |
| Imputasi berbasis kelompok | MAR — misalnya median per provinsi | Perlu kelompok yang bermakna |
| `KNNImputer` | MAR dengan hubungan antarfitur | Lebih mahal; peka penskalaan |
| **Penanda "hilang"** | Ketika ketiadaan itu sendiri informatif | — |

```python
from sklearn.impute import SimpleImputer

# Numerik: median lebih tahan pencilan daripada rata-rata
imp_num = SimpleImputer(strategy="median")

# Kategorik: kategori tersendiri, bukan modus —
# karena "tidak diisi" sering bermakna
imp_kat = SimpleImputer(strategy="constant", fill_value="TIDAK_DIKETAHUI")
```

> **Yang wajib dicatat setiap kali:** berapa baris/nilai terpengaruh, metode apa yang dipakai, dan **mengapa**. Kriteria kurikulum untuk Sub-CPMK102-1 menyebut *"correctness preprocessing"* — dan kebenaran di sini mencakup alasan, bukan hanya kode yang berjalan.

---

### 3.4 Penyandian Variabel Kategorik

#### 3.4.1 Nominal vs Ordinal

Perbedaan ini menentukan penyandian yang benar.

| Jenis | Ciri | Contoh | Penyandian |
|-------|------|--------|------------|
| **Nominal** | Tanpa urutan | Provinsi, jenis usaha, warna | *One-Hot Encoding* |
| **Ordinal** | Ada urutan bermakna | Pendidikan (SD<SMP<SMA<S1), tingkat kepuasan | *Ordinal Encoding* dengan urutan **ditentukan sendiri** |

**Kekeliruan yang paling sering:** memberi nomor pada data nominal.

```python
# SALAH — model akan menganggap Papua (33) "sepuluh kali" Aceh (3)
df["provinsi_kode"] = df["provinsi"].astype("category").cat.codes

# BENAR — nominal disandikan one-hot
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
```

```python
# BENAR untuk ordinal — urutan DITENTUKAN, bukan diserahkan ke abjad
from sklearn.preprocessing import OrdinalEncoder
urutan = [["SD", "SMP", "SMA", "D3", "S1", "S2", "S3"]]
enc_ord = OrdinalEncoder(categories=urutan)
```

#### 3.4.2 Kardinalitas Tinggi

Kolom dengan ratusan nilai unik (misalnya kode kecamatan) menghasilkan ratusan kolom bila di-*one-hot*.

| Strategi | Cara | Catatan |
|----------|------|---------|
| Penggabungan | Gabungkan kategori jarang menjadi "LAINNYA" | Sederhana dan aman |
| Pengelompokan bermakna | Kecamatan → kota → provinsi | Memerlukan pengetahuan domain |
| *Frequency encoding* | Ganti dengan frekuensi kemunculan | Aman terhadap kebocoran |
| *Target encoding* | Ganti dengan rata-rata target | **Sangat rawan kebocoran** — wajib di dalam validasi silang |

> *Target encoding* adalah penyebab kebocoran yang sering luput. Ia dibahas kembali pada Minggu 4 dan 5.

#### 3.4.3 `handle_unknown` Bukan Detail Kecil

```python
OneHotEncoder(handle_unknown="ignore")
```

Tanpa parameter ini, model akan **gagal total** ketika menemui kategori baru di data uji atau di produksi — kategori yang tidak muncul di data latih. Pada data Indonesia, ini terjadi setiap kali ada pemekaran wilayah atau kategori baru ditambahkan.

---

### 3.5 Penskalaan Fitur

#### 3.5.1 Algoritma yang Membutuhkan dan Tidak

| Membutuhkan penskalaan | Tidak membutuhkan |
|------------------------|-------------------|
| k-NN (berbasis jarak) | Pohon keputusan |
| SVM (berbasis jarak/margin) | *Random Forest* |
| Regresi dengan regularisasi (Ridge/Lasso) | *Gradient boosting* |
| Jaringan saraf tiruan | Naive Bayes (sebagian besar varian) |
| K-Means, PCA | — |

Alasannya: algoritma berbasis jarak memperlakukan fitur dengan rentang besar sebagai lebih penting, semata-mata karena satuannya. Fitur "pendapatan" dalam rupiah (jutaan) akan menenggelamkan fitur "jumlah anggota keluarga" (satuan) pada perhitungan jarak Euclidean.

#### 3.5.2 Tiga Penskala

| Penskala | Rumus | Hasil | Kapan dipakai |
|----------|-------|-------|---------------|
| `StandardScaler` | $(x-\mu)/\sigma$ | Rata-rata 0, simpangan baku 1 | Umum; data mendekati normal |
| `MinMaxScaler` | $(x-\min)/(\max-\min)$ | Rentang [0, 1] | Ketika rentang tetap dibutuhkan |
| `RobustScaler` | $(x - Q_2)/IQR$ | Berpusat pada median | **Ketika ada pencilan** |

```python
from sklearn.preprocessing import StandardScaler, RobustScaler

# Data pendapatan Indonesia sangat menceng kanan dengan pencilan nyata
# (bukan kesalahan) — RobustScaler lebih sesuai
scaler = RobustScaler()
```

---

### 3.6 `Pipeline`: Pencegah Kebocoran Struktural

#### 3.6.1 Masalah yang Dipecahkannya

```python
# ══════════ SALAH — KEBOCORAN DATA ══════════
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)          # ← seluruh data, termasuk uji
X_tr, X_te, y_tr, y_te = train_test_split(X_scaled, y)
# Rata-rata dan simpangan baku data uji sudah "bocor" ke penskala.
# Skor yang dihasilkan terlalu optimistis.

# ══════════ BENAR ══════════
X_tr, X_te, y_tr, y_te = train_test_split(X, y, random_state=42)
scaler = StandardScaler()
X_tr = scaler.fit_transform(X_tr)           # fit HANYA pada data latih
X_te = scaler.transform(X_te)               # transform saja pada data uji
```

Kebocoran semacam ini mudah terjadi dan sulit terlihat. `Pipeline` mencegahnya **secara struktural** — kesalahan itu menjadi tidak mungkin dilakukan.

#### 3.6.2 `Pipeline` dan `ColumnTransformer`

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

kol_numerik  = ["luas_usaha", "omzet_bulanan", "lama_usaha", "jumlah_pegawai"]
kol_kategorik = ["jenis_usaha", "provinsi", "status_tempat"]

# Alur untuk kolom numerik
alur_num = Pipeline([
    ("imputasi", SimpleImputer(strategy="median")),
    ("penskalaan", StandardScaler()),
])

# Alur untuk kolom kategorik
alur_kat = Pipeline([
    ("imputasi", SimpleImputer(strategy="constant", fill_value="TIDAK_DIKETAHUI")),
    ("penyandian", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
])

# Menggabungkan keduanya berdasarkan kolom
prapemrosesan = ColumnTransformer([
    ("num", alur_num, kol_numerik),
    ("kat", alur_kat, kol_kategorik),
])

# Alur lengkap: prapemrosesan + model, sebagai satu kesatuan
model = Pipeline([
    ("prapemrosesan", prapemrosesan),
    ("klasifikasi", LogisticRegression(max_iter=1000, random_state=42)),
])

model.fit(X_train, y_train)          # seluruh langkah di-fit pada data latih saja
skor = model.score(X_test, y_test)   # data uji hanya ditransformasi
```

#### 3.6.3 Empat Keuntungan `Pipeline`

| Keuntungan | Penjelasan |
|------------|------------|
| **Mencegah kebocoran** | `fit` otomatis hanya pada bagian latih dalam validasi silang |
| **Reproduksibilitas** | Seluruh langkah tersimpan sebagai satu objek |
| **Penyetelan menyeluruh** | `GridSearchCV` dapat menyetel parameter prapemrosesan sekaligus model |
| **Penerapan yang aman** | Data baru diproses persis seperti data latih |

> **Ketentuan mata kuliah ini:** mulai Lab 3, seluruh prapemrosesan wajib berada di dalam `Pipeline`. Transformasi yang diterapkan pada data lengkap sebelum pembagian dikenai pengurangan nilai, sekalipun hasilnya tampak benar.

---

## Kegiatan Pembelajaran

### Sebelum Kelas (60 menit)

- Membaca [Bab 3 buku ajar](../06-buku-ajar/bab-03-data-dan-prapemrosesan.md).
- Mengunduh satu dataset dari BPS atau Satu Data Indonesia dan menjalankan tujuh perintah pembuka §3.2.1.

### Di Kelas (150 menit)

| Segmen | Durasi | Kegiatan |
|--------|--------|----------|
| Pembuka | 10' | Tinjauan; pembahasan T-02 |
| Konsep | 35' | Pemeriksaan kualitas data; pola nilai hilang |
| Demonstrasi | 25' | Membedah dataset BPS yang belum bersih, langsung di kelas |
| Konsep | 30' | Penyandian kategorik; penskalaan |
| Demonstrasi | 30' | **Kegiatan inti:** membangun `Pipeline` + `ColumnTransformer` dari nol; menunjukkan selisih skor dengan dan tanpa kebocoran |
| Penutup | 20' | Rangkuman; memulai Lab 3 |

**Demonstrasi kegagalan yang wajib ditunjukkan:** jalankan penskalaan sebelum pembagian data, catat skornya; lalu jalankan dengan `Pipeline`, catat skornya. Selisihnya membuat konsep kebocoran menjadi konkret sebelum dibahas formal pada Minggu 4.

### Setelah Kelas (120 menit)

- Menyelesaikan [Lab 3](../04-labs/lab-03-pipeline-prapemrosesan.md).
- Menyiapkan data untuk proposal proyek (jatuh tempo Minggu 5).

---

## Penugasan

**T-03 — *Pipeline* Prapemrosesan**

| Aspek | Ketentuan |
|-------|-----------|
| Luaran | Notebook Colab |
| Isi | (a) Pemeriksaan kualitas lengkap atas dataset yang diberikan; (b) Identifikasi pola nilai hilang beserta alasan penanganannya; (c) `ColumnTransformer` untuk kolom numerik dan kategorik; (d) `Pipeline` lengkap sampai model; (e) Catatan keputusan: apa, berapa banyak, mengapa |
| Tenggat | Awal pertemuan Minggu 4 |
| Bobot | 1,9% (Observasi) |

---

## Rangkuman

1. Mutu data **membatasi** mutu model secara mutlak; karena itu tiga minggu penuh dicurahkan untuknya.
2. **Tujuh perintah pembuka** menangkap sebagian besar masalah sebelum menjadi kesalahan analisis.
3. Tiga pola nilai hilang (**MCAR/MAR/MNAR**) menuntut penanganan berbeda; MNAR tidak dapat diperbaiki dan wajib dinyatakan.
4. **Nominal disandikan one-hot; ordinal disandikan berurut** dengan urutan ditentukan sendiri.
5. `handle_unknown="ignore"` mencegah kegagalan total saat menemui kategori baru.
6. **Penskalaan dibutuhkan algoritma berbasis jarak**, tidak dibutuhkan algoritma berbasis pohon.
7. `RobustScaler` lebih sesuai bila ada pencilan yang sah.
8. **`Pipeline` mencegah kebocoran secara struktural** — bukan sekadar merapikan kode.
9. Setiap keputusan prapemrosesan dicatat: **apa, berapa banyak, mengapa**.

---

## Referensi

1. Géron, A. (2022). *Hands-On Machine Learning* (3rd ed.), Bab 2. O'Reilly.
2. Müller, A. C., & Guido, S. (2016). *Introduction to Machine Learning with Python*, Bab 4. O'Reilly.
3. Little, R. J. A., & Rubin, D. B. (2019). *Statistical Analysis with Missing Data* (3rd ed.). Wiley.
4. Dokumentasi scikit-learn — *Preprocessing data*. <https://scikit-learn.org/stable/modules/preprocessing.html>
5. Dokumentasi scikit-learn — *Pipelines and composite estimators*. <https://scikit-learn.org/stable/modules/compose.html>
6. Badan Pusat Statistik. *Sistem Informasi Rujukan Statistik*. <https://sirusa.bps.go.id>
---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
