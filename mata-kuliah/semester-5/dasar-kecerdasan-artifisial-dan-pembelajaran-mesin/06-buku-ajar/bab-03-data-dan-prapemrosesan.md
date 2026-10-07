# BAB 3: DATA DAN PRAPEMROSESAN

**Tri Aji Nugroho, S.T., M.T.**

---

## Tujuan Pembelajaran

| Sub-CPMK | Deskripsi Capaian | Level Bloom |
|----------|-------------------|-------------|
| `DAIML-Sub-CPMK102-1` | Memeriksa kualitas dataset secara sistematis | C3 |
| `DAIML-Sub-CPMK102-1` | Menganalisis pola nilai hilang dan memilih penanganan yang sesuai | C4 |
| `DAIML-Sub-CPMK102-1` | Membangun `Pipeline` yang mencegah kebocoran secara struktural | C3 |

---

## 3.1 Mengapa Tiga Bab untuk Data

Survei praktisi berulang kali menunjukkan hal yang sama: sebagian besar waktu kerja pembelajaran mesin dihabiskan untuk data, bukan untuk model. Alasannya bukan ketidakefisienan, melainkan bahwa **mutu data membatasi mutu model secara mutlak**.

> Model tercanggih yang dilatih pada data yang cacat menghasilkan keluaran yang cacat — dengan tambahan bahaya bahwa keluarannya tampak meyakinkan.

Pergeseran perhatian dari model ke data (*data-centric AI*) adalah salah satu tren utama yang membentuk susunan buku ini: Bab 3, 4, dan 5 seluruhnya tentang data, dan model pertama baru muncul pada Bab 6.

---

## 3.2 Pemeriksaan Kualitas Data

### 3.2.1 Tujuh Perintah Pembuka

```python
import pandas as pd

df = pd.read_csv("data_umkm.csv")

print("1. Dimensi:", df.shape)

df.info()                                         # 2. tipe data dan non-null

display(df.describe().T.round(2))                 # 3. cari nilai mustahil

print((df.isna().mean() * 100).round(2)
      .sort_values(ascending=False))              # 4. nilai hilang per kolom

print("5. Duplikat penuh:", df.duplicated().sum())

for kol in df.select_dtypes(include="object"):    # 6. kardinalitas kategorik
    print(f"   {kol:22s} {df[kol].nunique():5d} unik")

print(df["target"].value_counts(normalize=True)   # 7. keseimbangan kelas
      .round(3))
```

Tujuh perintah ini menangkap sebagian besar masalah **sebelum** ia menjadi kesalahan analisis.

### 3.2.2 Tanda Bahaya dan Penyebabnya

| Tanda | Kemungkinan penyebab | Tindakan |
|-------|----------------------|----------|
| Nilai `-99`, `9999`, `0` pada kolom yang mustahil | Kode nilai hilang tidak diterjemahkan | Ubah menjadi `NaN` **sebelum apa pun** |
| Kolom numerik bertipe `object` | Pemisah ribuan atau satuan ikut terbaca | Bersihkan lalu konversi |
| Kardinalitas kategorik jauh lebih tinggi dari yang seharusnya | Perbedaan ejaan/kapitalisasi | Bakukan sebelum penyandian |
| Rata-rata jauh dari median | Kemencengan berat atau pencilan | Pertimbangkan transformasi |
| Satu kelas < 1% dari data | Ketidakseimbangan ekstrem | Sesuaikan metrik dan strategi (Bab 7) |
| **Kolom berkorelasi ~1 terhadap target** | **Kemungkinan kebocoran** | **Selidiki sebelum melanjutkan** |

> Baris terakhir adalah penemuan yang melegakan bila terjadi pada Bab 3, dan merusak bila baru ditemukan saat presentasi akhir.

---

## 3.3 Nilai Hilang

### 3.3.1 Tiga Pola

| Pola | Kepanjangan | Ciri | Penanganan yang sah |
|------|-------------|------|---------------------|
| **MCAR** | *Missing Completely At Random* | Tidak berkaitan dengan apa pun | Penghapusan baris aman |
| **MAR** | *Missing At Random* | Berkaitan dengan variabel lain yang teramati | Imputasi bersyarat |
| **MNAR** | *Missing Not At Random* | Berkaitan dengan nilai yang hilang itu sendiri | **Tidak dapat diperbaiki secara statistik** — wajib dinyatakan sebagai keterbatasan |

**Contoh MNAR:** pelaku UMKM berpenghasilan tinggi cenderung tidak mengisi kolom omzet. Imputasi rata-rata akan **selalu** menghasilkan taksiran yang terlalu rendah, berapa pun canggihnya metode yang dipakai — karena metode apa pun hanya dapat belajar dari data yang ada, dan yang hilang justru yang berbeda sifatnya.

### 3.3.2 Memeriksa Polanya

```python
import numpy as np

for kol in ["omzet_bulanan", "lama_usaha"]:
    hilang = df[kol].isna()
    print(f"\n--- {kol} ({hilang.sum()} hilang, {hilang.mean():.1%}) ---")
    for pembanding in df.select_dtypes(include=[np.number]).columns:
        if pembanding == kol:
            continue
        a = df.loc[hilang, pembanding].mean()
        b = df.loc[~hilang, pembanding].mean()
        if b and abs(a - b) / abs(b) > 0.15:       # selisih > 15%
            print(f"  {pembanding:20s} hilang={a:10.2f}  ada={b:10.2f}  "
                  f"selisih={abs(a-b)/abs(b):.1%}")
```

Bila rata-rata variabel lain sangat berbeda antara baris yang hilang dan yang tidak, kehilangan **tidak acak** — dan penghapusan baris akan menimbulkan bias.

### 3.3.3 Pilihan Penanganan

| Metode | Kapan sesuai | Risiko |
|--------|--------------|--------|
| Hapus baris | MCAR, proporsi kecil (< 5%) | Kehilangan data; bias bila bukan MCAR |
| Hapus kolom | Hilang > 60% dan kolom tidak penting | Kehilangan sinyal |
| Imputasi median | Numerik, MCAR/MAR | Mengecilkan varians |
| Imputasi kategori tersendiri | Kategorik | — |
| Imputasi per kelompok | MAR — misalnya median per provinsi | Perlu kelompok yang bermakna |
| `KNNImputer` | MAR dengan hubungan antarfitur | Lebih mahal; peka penskalaan |
| **Penanda "hilang"** | Ketika ketiadaan itu sendiri informatif | — |

```python
from sklearn.impute import SimpleImputer

# Numerik: median lebih tahan pencilan daripada rata-rata
imp_num = SimpleImputer(strategy="median")

# Kategorik: kategori tersendiri, bukan modus —
# karena "tidak diisi" sering bermakna
imp_kat = SimpleImputer(strategy="constant", fill_value="TIDAK_DIKETAHUI")

# Penanda: menambahkan kolom biner "nilai ini hilang"
imp_penanda = SimpleImputer(strategy="median", add_indicator=True)
```

> **Yang wajib dicatat setiap kali:** berapa baris/nilai terpengaruh, metode apa yang dipakai, dan **mengapa**. Kriteria kurikulum untuk `Sub-CPMK102-1` menyebut *"correctness preprocessing"* — dan kebenaran di sini mencakup alasan yang dapat dipertanggungjawabkan, bukan hanya kode yang berjalan.

---

## 3.4 Penyandian Variabel Kategorik

### 3.4.1 Nominal vs Ordinal

| Jenis | Ciri | Contoh | Penyandian |
|-------|------|--------|------------|
| **Nominal** | Tanpa urutan | Provinsi, jenis usaha | *One-Hot Encoding* |
| **Ordinal** | Ada urutan bermakna | Pendidikan, tingkat kepuasan | *Ordinal Encoding* dengan urutan **ditentukan sendiri** |

**Kekeliruan yang paling sering:** memberi nomor pada data nominal.

```python
# SALAH — model akan menganggap Papua (33) "sebelas kali" Aceh (3)
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

Bila urutan diserahkan ke abjad, "D3" akan berada sebelum "S1" dan "SD" — urutan yang tidak bermakna apa pun.

### 3.4.2 Kardinalitas Tinggi

Kolom dengan ratusan nilai unik (misalnya kode kecamatan) menghasilkan ratusan kolom bila di-*one-hot*.

| Strategi | Cara | Catatan |
|----------|------|---------|
| Penggabungan | Kategori jarang → "LAINNYA" | Sederhana dan aman |
| Pengelompokan bermakna | Kecamatan → kota → provinsi | Memerlukan pengetahuan domain |
| *Frequency encoding* | Ganti dengan frekuensi kemunculan | Aman terhadap kebocoran |
| *Target encoding* | Ganti dengan rata-rata target | **Sangat rawan kebocoran** — wajib di dalam validasi silang |

### 3.4.3 `handle_unknown` Bukan Detail Kecil

```python
OneHotEncoder(handle_unknown="ignore")
```

Tanpa parameter ini, model **gagal total** ketika menemui kategori yang tidak muncul di data latih. Pada data Indonesia ini terjadi setiap kali ada pemekaran wilayah atau penambahan kategori layanan.

---

## 3.5 Penskalaan Fitur

### 3.5.1 Siapa yang Membutuhkan

| Membutuhkan penskalaan | Tidak membutuhkan |
|------------------------|-------------------|
| k-NN (berbasis jarak) | Pohon keputusan |
| SVM (berbasis margin) | *Random Forest* |
| Regresi dengan regularisasi | *Gradient boosting* |
| Jaringan saraf tiruan | Naive Bayes (sebagian besar varian) |
| K-Means, PCA | — |

Alasannya: algoritma berbasis jarak memperlakukan fitur berentang besar sebagai lebih penting, **semata-mata karena satuannya**. Fitur "omzet" dalam rupiah (jutaan) akan menenggelamkan fitur "jumlah pegawai" (satuan) pada perhitungan jarak Euclidean.

### 3.5.2 Tiga Penskala

| Penskala | Rumus | Hasil | Kapan dipakai |
|----------|-------|-------|---------------|
| `StandardScaler` | $(x-\mu)/\sigma$ | Rata-rata 0, simpangan 1 | Umum; data mendekati normal |
| `MinMaxScaler` | $(x-\min)/(\max-\min)$ | Rentang [0, 1] | Ketika rentang tetap dibutuhkan |
| `RobustScaler` | $(x-Q_2)/IQR$ | Berpusat pada median | **Ketika ada pencilan** |

Pada data Indonesia yang sering menceng kanan berat — pendapatan, omzet, populasi — `RobustScaler` biasanya lebih sesuai.

---

## 3.6 `Pipeline`: Pencegah Kebocoran Struktural

### 3.6.1 Masalah yang Dipecahkannya

```python
# ══════════ SALAH — KEBOCORAN ══════════
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)              # ← seluruh data, termasuk uji
X_tr, X_te, y_tr, y_te = train_test_split(X_scaled, y)
# Rata-rata dan simpangan data uji sudah "bocor" ke penskala.

# ══════════ BENAR ══════════
X_tr, X_te, y_tr, y_te = train_test_split(X, y, random_state=42)
scaler = StandardScaler()
X_tr = scaler.fit_transform(X_tr)               # fit HANYA pada latih
X_te = scaler.transform(X_te)                   # transform saja pada uji
```

Kebocoran semacam ini mudah terjadi, tidak menghasilkan galat, dan sulit terlihat. `Pipeline` mencegahnya **secara struktural** — kesalahan itu menjadi tidak mungkin dilakukan.

### 3.6.2 `Pipeline` dan `ColumnTransformer`

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import RobustScaler, OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

kol_num      = ["omzet_bulanan", "lama_usaha", "jumlah_pegawai"]
kol_nominal  = ["jenis_usaha", "provinsi"]
kol_ordinal  = ["pendidikan_pemilik"]
urutan_pend  = [["SD", "SMP", "SMA", "D3", "S1", "S2"]]

alur_num = Pipeline([
    ("imputasi", SimpleImputer(strategy="median")),
    ("skala", RobustScaler()),
])

alur_nominal = Pipeline([
    ("imputasi", SimpleImputer(strategy="constant", fill_value="TIDAK_DIKETAHUI")),
    ("sandi", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
])

alur_ordinal = Pipeline([
    ("imputasi", SimpleImputer(strategy="most_frequent")),
    ("sandi", OrdinalEncoder(categories=urutan_pend,
                             handle_unknown="use_encoded_value",
                             unknown_value=-1)),
])

prapemrosesan = ColumnTransformer([
    ("num", alur_num, kol_num),
    ("nom", alur_nominal, kol_nominal),
    ("ord", alur_ordinal, kol_ordinal),
])

model = Pipeline([
    ("pra", prapemrosesan),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced",
                               random_state=42)),
])

model.fit(X_train, y_train)       # seluruh langkah di-fit pada latih saja
```

### 3.6.3 Empat Keuntungan

| Keuntungan | Penjelasan |
|------------|------------|
| **Mencegah kebocoran** | `fit` otomatis hanya pada bagian latih dalam validasi silang |
| **Reproduksibilitas** | Seluruh langkah tersimpan sebagai satu objek |
| **Penyetelan menyeluruh** | `GridSearchCV` dapat menyetel parameter prapemrosesan sekaligus model |
| **Penerapan yang aman** | Data baru diproses persis seperti data latih |

> **Ketentuan yang berlaku sejak bab ini:** seluruh prapemrosesan wajib berada di dalam `Pipeline`. Transformasi yang diterapkan pada data lengkap sebelum pembagian dikenai pengurangan nilai, sekalipun hasilnya tampak benar.

---

## AI Corner — Tahap *Understand → Apply*

### Mengapa AI Tidak Dapat Memutuskan Penanganan Data

Diminta menangani nilai hilang, model bahasa akan menyarankan imputasi median atau rata-rata — hampir selalu, dan hampir tanpa syarat. Saran itu tepat untuk MCAR dan sebagian MAR, dan **keliru untuk MNAR**.

Persoalannya bukan bahwa AI tidak mengetahui perbedaan ketiga pola itu; ia dapat menjelaskannya dengan baik bila ditanya. Persoalannya adalah bahwa **menentukan pola mana yang berlaku menuntut pengetahuan tentang bagaimana data dikumpulkan** — dan itu tidak ada dalam prompt.

| Pertanyaan yang menentukan | Hanya dapat dijawab oleh |
|----------------------------|--------------------------|
| Mengapa kolom ini kosong pada sebagian baris? | Orang yang memahami proses pengumpulannya |
| Apakah responden yang tidak mengisi berbeda sifatnya? | Orang yang memahami konteksnya |
| Apakah "0" berarti nol, atau berarti tidak diisi? | Dokumen definisi variabel dari penerbitnya |
| Apakah pencilan ini kesalahan atau kenyataan? | Orang yang memahami domainnya |

### Pemakaian yang Wajar pada Bab Ini

```
Saya punya kolom omzet dengan 12% nilai hilang. Setelah saya periksa,
baris yang hilang memiliki rata-rata jumlah pegawai 3× lebih tinggi
daripada yang terisi. Saya menduga ini MNAR — pelaku usaha besar
enggan mengisi.

Keputusan saya: tidak mengimputasi, melainkan menambahkan penanda
"omzet_tidak_diisi" sebagai fitur, dan menyatakan ini sebagai
keterbatasan.

Tolong periksa: adakah kelemahan dalam penalaran ini?
```

Prompt ini menunjukkan tiga hal: pemeriksaan sudah dilakukan, keputusan sudah dibuat beserta dasarnya, dan yang diminta adalah pemeriksaan — bukan keputusan.

---

## Latihan Soal

### Tingkat Dasar

1. Jelaskan perbedaan MCAR, MAR, dan MNAR, masing-masing dengan satu contoh dari konteks Indonesia.

2. Untuk masing-masing kolom, tentukan penyandian yang tepat beserta alasannya:
   (a) `provinsi` (38 nilai)
   (b) `tingkat_kepuasan` (Sangat Tidak Puas … Sangat Puas)
   (c) `jenis_kelamin`
   (d) `kode_kecamatan` (2.400 nilai)

3. Sebutkan tiga algoritma yang membutuhkan penskalaan dan tiga yang tidak, beserta alasan perbedaannya.

4. Jelaskan dalam tiga kalimat mengapa `Pipeline` mencegah kebocoran **secara struktural**, bukan sekadar merapikan kode.

### Tingkat Menengah

5. Sebuah dataset survei UMKM memiliki 18% nilai hilang pada kolom `omzet_tahunan`. Pemeriksaan menunjukkan baris yang hilang memiliki `jumlah_pegawai` rata-rata 12, sedangkan yang terisi rata-rata 4.
   (a) Pola apa yang paling mungkin?
   (b) Mengapa imputasi median akan memperburuk keadaan?
   (c) Sebutkan dua penanganan yang lebih sesuai.
   (d) Apa yang wajib ditulis pada bagian keterbatasan laporan?

6. Perhatikan potongan kode berikut:
   ```python
   df["pendidikan_num"] = df["pendidikan"].astype("category").cat.codes
   ```
   Kolom `pendidikan` berisi: SD, SMP, SMA, D3, S1, S2.
   (a) Urutan apa yang dihasilkan kode ini?
   (b) Mengapa urutan itu keliru?
   (c) Tuliskan kode yang benar.
   (d) Apa akibatnya pada model regresi linear bila kekeliruan ini dibiarkan?

7. Sebuah kolom `kode_pos` memiliki 3.200 nilai unik pada dataset 8.000 baris.
   (a) Berapa kolom yang dihasilkan bila di-*one-hot*?
   (b) Masalah apa yang akan timbul?
   (c) Sebutkan tiga strategi penanganan beserta kelebihan masing-masing.
   (d) Strategi mana yang paling aman terhadap kebocoran? Jelaskan.

8. Sebuah tim menerapkan `StandardScaler().fit_transform(X)` lalu membagi data.
   (a) Informasi apa yang bocor, dan dari mana ke mana?
   (b) Apakah skornya akan lebih tinggi atau lebih rendah daripada kinerja sebenarnya?
   (c) Dalam keadaan apa selisihnya besar, dan dalam keadaan apa kecil?
   (d) Tuliskan versi yang benar dengan `Pipeline`.

### Tingkat Mahir

9. Bangun *pipeline* prapemrosesan lengkap untuk dataset nyata.
   (a) Unduh satu dataset dari BPS atau Satu Data Indonesia.
   (b) Jalankan tujuh perintah pembuka dan catat seluruh masalah yang ditemukan.
   (c) Analisis pola nilai hilang pada setiap kolom yang memilikinya.
   (d) Bangun `ColumnTransformer` yang menangani numerik, nominal, dan ordinal secara terpisah.
   (e) Dokumentasikan setiap keputusan dengan format: apa, berapa banyak, mengapa.
   (f) Tunjukkan selisih skor dengan dan tanpa `Pipeline`.

10. Bandingkan strategi imputasi secara empiris.
    (a) Ambil dataset lengkap tanpa nilai hilang.
    (b) Hilangkan 15% nilai secara MCAR (acak murni).
    (c) Hilangkan 15% nilai secara MAR (bergantung kolom lain).
    (d) Bandingkan empat strategi imputasi pada keduanya, ukur selisih terhadap nilai asli.
    (e) Jelaskan mengapa peringkat strategi berbeda antara MCAR dan MAR.

11. Tulislah pedoman satu halaman berjudul *"Mendokumentasikan Keputusan Prapemrosesan"*. Sertakan: format catatan yang wajib, lima contoh catatan yang baik dan yang buruk, serta alasan mengapa dokumentasi ini merupakan bagian dari kebenaran teknis, bukan sekadar kerapian.

---

## Rangkuman

1. **Mutu data membatasi mutu model secara mutlak** — karena itu tiga bab dicurahkan untuknya.
2. **Tujuh perintah pembuka** menangkap sebagian besar masalah sebelum menjadi kesalahan.
3. Tiga pola nilai hilang (**MCAR/MAR/MNAR**) menuntut penanganan berbeda; **MNAR tidak dapat diperbaiki** dan wajib dinyatakan.
4. **Nominal disandikan one-hot; ordinal disandikan berurut** dengan urutan ditentukan sendiri.
5. `handle_unknown="ignore"` mencegah kegagalan total pada kategori baru.
6. **Penskalaan dibutuhkan algoritma berbasis jarak**, tidak dibutuhkan algoritma berbasis pohon.
7. `RobustScaler` lebih sesuai pada data Indonesia yang sering menceng berat.
8. **`Pipeline` mencegah kebocoran secara struktural** — bukan sekadar merapikan kode.
9. Setiap keputusan prapemrosesan dicatat: **apa, berapa banyak, mengapa**.
10. **Menentukan pola nilai hilang menuntut pengetahuan tentang pengumpulan data** — hal yang tidak dimiliki alat bantu mana pun.

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
